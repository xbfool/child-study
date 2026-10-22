"""一份题源生成 PDF、每日 Markdown、离线 HTML 和进度记录。"""
from pathlib import Path
import html
import json
import re
import csv
import os
import sys
from xml.sax.saxutils import escape

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from pypdf import PdfReader
from materials.lessons import LESSONS
from materials.guide import PARENT, WH
from materials.cheatsheet_custom import make_crop_cheatsheet

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'output'
PDF = OUT / 'pdf'
FONT = os.environ.get('STUDY_FONT', 'C:/Windows/Fonts/simsun.ttc')
if not Path(FONT).exists():
    raise SystemExit('请用 STUDY_FONT 指定支持中文的 TrueType 字体路径。')
pdfmetrics.registerFont(TTFont('CN', FONT, subfontIndex=0))
pdfmetrics.registerFontFamily('CN', normal='CN', bold='CN', italic='CN', boldItalic='CN')
W, H = A4
M = 35
CW = W - M * 2
INK = HexColor('#162d44')
MUTED = HexColor('#526579')
BLUE = HexColor('#225b92')
GREEN = HexColor('#177663')
ORANGE = HexColor('#aa5b19')
MIN_Y = []

def rich(s):
    """画线目标同时加底色；答案中的普通文本不接受原始 HTML。"""
    s = escape(s)
    parts = s.split('**')
    return ''.join('<u><font backColor="#fff2b8">'+x+'</font></u>' if i % 2 else x
                   for i, x in enumerate(parts))

def para(c, text, x, y, width, size=10.7, leading=14.2, color=INK):
    style = ParagraphStyle('p', fontName='CN', fontSize=size, leading=leading, textColor=color)
    p = Paragraph(rich(text), style)
    _, height = p.wrap(width, H)
    p.drawOn(c, x, y-height)
    return y-height

def header(c, day, answer=False):
    c.setFillColor(BLUE if not answer else GREEN)
    c.rect(0, H-9, W, 9, fill=1, stroke=0)
    y = para(c, f"DAY {day['day']:02d}  {day['title']}", M, H-29, CW, 15, 20)
    label = '家长答案与订正提示' if answer else '姓名：____________  日期：____________  用时：______'
    y = para(c, label, M, y-8, CW, 9.6, 13, MUTED)
    return y-13

def footer(c, number, answer=False):
    c.setStrokeColor(HexColor('#d7dfe7'))
    c.line(M, 31, W-M, 31)
    label = '家长答案' if answer else '学生练习'
    c.setFillColor(MUTED)
    c.setFont('CN', 8)
    c.drawString(M, 19, f'{label} · 40 天英语句型练习 · 第 {number} 页')
    c.drawRightString(W-M, 19, '原创练习 · 2026-10-22')

def section(c, label, y, color=BLUE):
    c.setFillColor(color)
    c.roundRect(M, y-17, CW, 20, 3, fill=1, stroke=0)
    para(c, label, M+8, y-1, CW-16, 10, 13, white)
    return y-25

def get_review(d):
    n = d['day']
    if n == 1:
        sources = [(1, 2), (1, 8)]
    else:
        sources = [(n-1, (n*3) % 10), (max(1, n-7 if n>7 else n-3), (n*3+4) % 10)]
    return [dict(LESSONS[a-1]['main'][b], source=f'Day {a:02d} A{b+1}') for a, b in sources]

def question(c, q, label, y, answer=False, size=10.5):
    if answer:
        y = para(c, f"{label}  {q['answer']}", M+3, y, CW-6, 10.2, 13.5)
        y = para(c, f"订正：{q['why']}", M+17, y-2, CW-20, 9.0, 12.0, MUTED)
        return y-7
    y = para(c, f"{label}  {q['prompt']}", M+3, y, CW-6, size, 14)
    c.setStrokeColor(HexColor('#b9c6d2'))
    c.setLineWidth(.45)
    c.line(M+19, y-14, W-M-3, y-14)
    return y-21

def make_books():
    for is_answer, filename in [(False, '学生练习册.pdf'), (True, '家长答案与订正.pdf')]:
        c = canvas.Canvas(str(PDF/filename), pagesize=A4)
        c.setTitle(filename[:-4])
        c.setAuthor('child-study')
        for d in LESSONS:
            c.bookmarkPage(f"day{d['day']}")
            c.addOutlineEntry(f"Day {d['day']:02d} {d['title']}", f"day{d['day']}")
            y = header(c, d, is_answer)
            if not is_answer:
                y = para(c, '今天先看：'+d['focus'], M+6, y, CW-12, 10, 13)
                if d['example']:
                    y = para(c, '看一个例子：'+d['example'], M+6, y-5, CW-12, 9.7, 13, BLUE)
                y -= 12
            y = section(c, 'A  今日练习（10 题）' if not is_answer else 'A  今日练习参考答案', y)
            for i, q in enumerate(d['main'], 1):
                y = question(c, q, str(i)+'.', y, is_answer)
            y = section(c, 'B  订正后换句再试（2 题）' if not is_answer else 'B  换句题参考答案', y-3, GREEN)
            for i, q in enumerate(d['transfer'], 1):
                y = question(c, q, 'B'+str(i)+'.', y, is_answer)
            label = 'C  旧题复练（先遮住规则；Day 1 隔五分钟回头）' if d['day']==1 else 'C  旧题复练（先遮住规则卡）'
            y = section(c, label if not is_answer else 'C  旧题复练参考答案', y-3, ORANGE)
            for i, q in enumerate(get_review(d), 1):
                if is_answer:
                    q = dict(q, why=q['why']+' 来源：'+q['source'])
                y = question(c, q, 'C'+str(i)+'.', y, is_answer)
            if not is_answer:
                y = para(c, 'A 区：独立对 ___ / 10；看提示对 ___；待订正 ___。易错题号：________', M+3, y-2, CW-6, 9, 12, MUTED)
                y = para(c, '订正后我能说清：问什么 → 找谁 → 选哪套 → 哪个词要变。', M+3, y-3, CW-6, 9, 12, MUTED)
            MIN_Y.append((filename, d['day'], round(y, 1)))
            if y < 42:
                raise ValueError(f'页面内容超出安全区：{filename} Day {d["day"]}: {y}')
            footer(c, d['day'], is_answer)
            c.showPage()
        c.save()

def card(c, x, y, width, height, title, lines, color=BLUE, size=11.2):
    c.setFillColor(HexColor('#f5f8fb'))
    c.setStrokeColor(HexColor('#ccd8e3'))
    c.roundRect(x, y-height, width, height, 9, fill=1, stroke=1)
    c.setFillColor(color)
    c.roundRect(x, y-28, width, 28, 8, fill=1, stroke=0)
    para(c, title, x+11, y-6, width-22, 12, 16, white)
    yy = y-39
    for line in lines:
        yy = para(c, line, x+12, yy, width-24, size, size+4)-7
    if yy+7 < y-height+2:
        raise ValueError('速查卡内容超出：'+title)
    return yy

def arrow(c, x, y):
    c.setStrokeColor(MUTED)
    c.setLineWidth(1.5)
    c.line(x, y, x, y-12)
    c.line(x, y-12, x-4, y-7)
    c.line(x, y-12, x+4, y-7)

def cheat_header(c, title, sub):
    c.setFillColor(INK)
    c.rect(0, H-91, W, 91, fill=1, stroke=0)
    para(c, title, M, H-24, CW, 21, 27, white)
    para(c, sub, M, H-61, CW, 10.5, 14, HexColor('#d5e6f3'))

def make_cheatsheet():
    c = canvas.Canvas(str(PDF/'句型速查图.pdf'), pagesize=A4)
    c.setTitle('句型速查图 · 问句路线与疑问词感叹句')
    c.setAuthor('child-study')
    cheat_header(c, '改句时，先走对这条路', '速查图 1 / 2    先看题目要什么 → 圈出主语 → 选结构 → 检查要变的词')
    y = H-108
    card(c, M, y, CW, 65, '先问：我是要“问一句”，还是“改否定”？', [
        '问一句：一般疑问句问“是不是 / 能不能”；特殊疑问句先选“问什么”。'
    ], INK, 10.5)
    arrow(c, W/2, y-70)
    top = y-91
    gap = 12
    half = (CW-gap)/2
    card(c, M, top, half, 126, '① 句中已有 be', [
        'am / is / are → 放在主语前',
        'She is happy. → Is she happy?',
        '否定：She isn’t happy.'
    ], BLUE, 10.8)
    card(c, M+half+gap, top, half, 126, '② 句中已有 can', [
        'can → 放在主语前；后接原形',
        'She can swim. → Can she swim?',
        '否定：She can’t swim.'
    ], GREEN, 10.8)
    top -= 139
    card(c, M, top, CW, 131, '③ 一般现在时普通动词：请 do / does 来帮忙', [
        'I / you / we / they → Do；he / she / it / 单个人或物 → Does',
        'She likes cats. → Does she like cats?    否定：She doesn’t like cats.',
        '出现 does / doesn’t，后面的动词回原形：likes → like；has → have。'
    ], ORANGE, 11.1)
    top -= 144
    card(c, M, top, half, 140, 'have 的两套，别拼在一起', [
        'She has a bike.',
        '→ Does she have a bike?',
        'She has got a bike.',
        '→ Has she got a bike?'
    ], BLUE, 10.4)
    card(c, M+half+gap, top, half, 140, '“某处有”和“正在做”', [
        'There is a cat. → Is there a cat?',
        'There are cats. → Are there cats?',
        'She is reading. → Is she reading?',
        '别把 is / are 漏掉。'
    ], GREEN, 10.4)
    top -= 153
    card(c, M, top, CW, 145, '原形与三单：最后再检查一次', [
        '普通动词肯定句：She likes / watches / studies / has…；I / you 不算三单。',
        '通常加 s；ch / sh / s / x 等结尾加 es；辅音字母 + y → ies；have → has。',
        'can / do / does / don’t / doesn’t 后的主要动词，用原形。',
        'Let’s play. / Let him play.    否定：Let’s not play. / Don’t let him play.',
        '祈使句：Open the door. → Don’t open the door. / Don’t be late.'
    ], INK, 10.5)
    footer(c, 1)
    c.showPage()
    cheat_header(c, '我要问什么？我要感叹什么？', '速查图 2 / 2    画线信息选疑问词；要表达“多么……啊”，再走 What / How')
    top = H-110
    card(c, M, top, CW, 81, '普通特殊疑问句：疑问词 + 一般疑问句的结构', [
        '地点：Where is Tom?    喜好：What does Tom like?    能力：What can Tom draw?',
        '例外提醒：问“谁做”时 who 当主语 → Who likes cats?（不用再加 does）'
    ], BLUE, 10.5)
    top -= 94
    rows = [
        ('什么 what', '谁 who', '谁的 whose', '哪里 where'),
        ('何时 when', '几点 what time', '星期 what day', '日期 what date'),
        ('为何 why', '哪个 which', '方式 / 状态 how', '几岁 how old'),
        ('颜色 what colour', '尺码 what size', '学科 what subject', '种类 what kind of'),
        ('可数数量 how many + 复数', '量 / 价格 how much', '', ''),
        ('多长 / 多久 how long', '多远 how far', '多常 how often', '还要多久 how soon'),
    ]
    c.setFillColor(INK)
    c.setFont('CN', 12)
    c.drawString(M+2, top, '按信息找疑问词')
    top -= 10
    col = CW/4
    for n, row in enumerate(rows):
        c.setFillColor(HexColor('#edf4fa') if n%2==0 else HexColor('#f7f9fb'))
        c.rect(M, top-39, CW, 39, fill=1, stroke=0)
        if n == 4:
            para(c, row[0], M+7, top-10, CW/2-14, 10.4, 14)
            para(c, row[1], M+CW/2+7, top-10, CW/2-14, 10.4, 14)
        else:
            for i, s in enumerate(row):
                para(c, s, M+i*col+7, top-8, col-13, 10.2, 13)
        top -= 39
    top -= 11
    top = para(c, '拓展：多高 how tall；多重 how heavy；宾语“谁”也可用 whom。\n提建议：What about / How about + 名词或动词 ing。', M+5, top, CW-10, 9.7, 13, MUTED)-14
    card(c, M, top, CW, 101, 'What：后面带“名词这一包”', [
        '一个可数物：What a nice bag it is! / What an old bike it is!',
        '复数：What nice bags they are!    不可数：What nice weather it is!',
        '单数可数用 a / an；复数、不可数不用。'
    ], GREEN, 10.5)
    top -= 111
    card(c, M, top, CW, 84, 'How：后面突出“怎么样”', [
        '形容词：How nice the bag is!    副词：How fast Tom runs!',
        '主语和动词保持陈述语序：the bag is；不是 is the bag。'
    ], ORANGE, 10.7)
    top -= 97
    card(c, M, top, CW, 77, '最后看一眼：问号，还是感叹号？', [
        'What colour is the bag?（问颜色）  /  How beautiful the bag is!（感叹）',
        '问句常把 be / can / do / does 放主语前；本套感叹句保留陈述语序。'
    ], INK, 10.2)
    if top-77 < 42:
        raise ValueError('速查图 2 页超出安全区')
    footer(c, 2)
    c.showPage()
    c.save()

CSS = '''
:root{color-scheme:light;font-family:"Microsoft YaHei","PingFang SC",sans-serif;color:#163047;background:#edf2f7}
body{margin:0}main{max-width:920px;margin:28px auto;padding:0 18px}h1{font-size:28px}h2{font-size:19px}
a{color:#225b92}nav{display:flex;flex-wrap:wrap;gap:10px}nav a,.btn{background:white;padding:10px 15px;border-radius:8px;border:1px solid #ccd8e3;text-decoration:none}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;margin:24px 0}.tile{background:white;border:1px solid #d1dce6;border-radius:10px;padding:17px}.tile p{font-size:14px;color:#53677c;line-height:1.6}
.sheet{box-sizing:border-box;background:white;margin:20px auto;padding:30px 36px;max-width:800px;border:1px solid #d1dce6;break-after:page}
.meta,.hint{font-size:13px;line-height:1.65;color:#53677c}.hint{padding:10px;background:#f0f6fc}.example{color:#225b92;font-size:13px}
.q{font-size:14px;line-height:1.6;margin:7px 0}.blank{height:19px;border-bottom:1px solid #bcc9d6;margin-left:22px}
mark{background:#fff0a8;text-decoration:underline}h3{background:#eaf2f9;padding:6px 9px;font-size:14px;margin:15px 0 8px}.answer{color:#176451;font-size:14px}.why{font-size:12px;color:#586c7d;margin:3px 0 10px}
@page{size:A4;margin:10mm}@media print{body{background:white}main{margin:0;padding:0;max-width:none}.screen{display:none!important}.sheet{border:0;margin:0;max-width:none;padding:0;width:100%;min-height:276mm}.q{font-size:10.5pt}.meta,.hint,.example{font-size:9pt}h1{font-size:17pt}h3{font-size:10pt}.blank{height:14px}.q{margin:5px 0}.sheet:last-child{break-after:auto}}
'''

def hr(s):
    return re.sub(r'\*\*(.*?)\*\*', r'<mark>\1</mark>', html.escape(s))

def html_doc(title, content):
    return '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><style>'+CSS+'</style><body><main>'+content+'</main></body></html>'

def md_day(d, answer=False):
    lines = [f"# Day {d['day']:02d} · {d['title']}", '']
    if not answer:
        lines += ['姓名：____________  日期：____________  用时：______', '', '今天先看：'+d['focus'], '']
        if d['example']:
            lines += ['例子：'+d['example'], '']
    for label, items in [('A 今日练习', d['main']), ('B 订正后换句再试', d['transfer']), ('C 旧题复练', get_review(d))]:
        lines += ['## '+label, '']
        for i,q in enumerate(items, 1):
            if answer:
                lines += [f"{i}. **{q['answer']}**", '', f"   订正：{q['why']}"+(' 来源：'+q['source'] if 'source' in q else ''), '']
            else:
                lines += [f"{i}. {q['prompt']}", '', '   ____________________________________________________________', '']
    return '\n'.join(lines)

def sheet_html(d, answer=False):
    body = f'<article class="sheet" id="day{d["day"]:02d}"><h1>Day {d["day"]:02d} · {html.escape(d["title"])}</h1>'
    if not answer:
        body += '<p class="meta">姓名：____________ 日期：____________ 用时：______</p><p class="hint">'+hr(d['focus'])+'</p>'
        if d['example']: body += '<p class="example">例子：'+hr(d['example'])+'</p>'
    for title, items in [('A 今日练习',d['main']),('B 订正后换句再试',d['transfer']),('C 旧题复练',get_review(d))]:
        body += '<h3>'+title+'</h3>'
        for i,q in enumerate(items,1):
            if answer:
                body += f'<p class="answer">{i}. {hr(q["answer"])}</p><p class="why">订正：{hr(q["why"])}</p>'
            else:
                body += f'<div class="q">{i}. {hr(q["prompt"])}<div class="blank"></div></div>'
    if not answer:
        body += '<p class="meta">A 区：独立对 ___ / 10；看提示对 ___；待订正 ___。<br>订正：说意思 → 找主语 → 选结构 → 完整重写 → 换句再试。</p>'
    return body+'</article>'

def make_text_outputs():
    for path in [OUT/'每日练习', OUT/'家长答案']:
        path.mkdir(parents=True,exist_ok=True)
    student_html, answer_html = [], []
    for d in LESSONS:
        name = f"Day{d['day']:02d}"
        for answer, folder in [(False,'每日练习'),(True,'家长答案')]:
            (OUT/folder/(name+'.md')).write_text(md_day(d,answer),encoding='utf-8')
            body = sheet_html(d,answer)
            toolbar = '<p class="screen"><a href="../../index.html">返回目录</a> · <button onclick="window.print()">打印本页</button></p>'
            (OUT/folder/(name+'.html')).write_text(html_doc(name,toolbar+body),encoding='utf-8')
            (answer_html if answer else student_html).append(body)
    (OUT/'学生练习册.html').write_text(html_doc('学生练习册',''.join(student_html)),encoding='utf-8')
    (OUT/'家长答案与订正.html').write_text(html_doc('家长答案与订正',''.join(answer_html)),encoding='utf-8')
    (ROOT/'家长使用说明.md').write_text(PARENT,encoding='utf-8')
    whmd = '# 疑问词完整索引\n\n| 问法 | 问信息 | 例子 | 练习日 |\n|---|---|---|---|\n'
    whmd += '\n'.join('| '+' | '.join(row)+' |' for row in WH)
    whmd += '\n\nwhat season / sport / food 等按 what + 名词迁移；how high / fast / wide 等按 how + 形容词 / 副词迁移。拓展项目不与核心项目同一天强行要求。\n'
    (ROOT/'疑问词索引.md').write_text(whmd,encoding='utf-8')
    (OUT/'题库.json').write_text(json.dumps([dict(d,review=get_review(d)) for d in LESSONS],ensure_ascii=False,indent=2),encoding='utf-8')
    with (OUT/'空白进度记录.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['天数','主题','日期','独立正确_共10题','提示后正确','B区正确_共2题','C区正确_共2题','错因_M_S_A_V_W_P','下次复练日期','备注'])
        writer.writerows([d['day'],d['title'],'','','','','','','',''] for d in LESSONS)
    tiles = ''.join(f'<section class="tile"><b>Day {d["day"]:02d} · {html.escape(d["title"])}</b><p>{"独立复习" if d["checkpoint"] else "分项学习与练习"}</p><a href="output/每日练习/Day{d["day"]:02d}.html">打开 / 打印今日练习</a><details><summary>家长入口</summary><a href="output/家长答案/Day{d["day"]:02d}.html">答案与订正</a></details></section>' for d in LESSONS)
    index = '<h1>40 天英语句型练习</h1><p>从模糊到清晰：先理解，再选择结构，再完整改句。</p><nav><a href="output/pdf/学生练习册.pdf">学生练习册 PDF（A4）</a><a href="output/pdf/家长答案与订正.pdf">家长答案 PDF（A4）</a><a href="output/pdf/句型速查图-A4裁剪版.pdf">速查图 A4 裁剪版（成品 185 × 270 mm）</a><a href="output/pdf/句型速查图.pdf">速查图原 A4 版</a><a href="家长使用说明.md">家长使用说明</a></nav><p class="hint">每天 A 区 10 题 + B 区 2 道换句题 + C 区 2 道旧题复练。学生 PDF 每页对应一天。前期可以看速查图；复习页先独立完成。</p><div class="grid">'+tiles+'</div>'
    (ROOT/'index.html').write_text(html_doc('40 天英语句型练习',index),encoding='utf-8')
    schedule = '\n'.join(f"| {d['day']:02d} | {d['title']} | [练习](output/每日练习/Day{d['day']:02d}.md) | [家长答案](output/家长答案/Day{d['day']:02d}.md) |" for d in LESSONS)
    readme = '''# 40 天英语句型练习

面向小学阶段，把模糊的句型知识拆开练，再逐步混合。题目为原创，非官方教材配套。

## 直接使用

- [学生练习册 PDF](output/pdf/学生练习册.pdf)：40 页，每页一天。
- [家长答案与订正 PDF](output/pdf/家长答案与订正.pdf)：40 页，与学生页一一对应。
- [速查图 A4 裁剪版 PDF](output/pdf/句型速查图-A4裁剪版.pdf)：纸张仍是 A4，正中是 185 × 270 mm 成品区域，四周白边，附浅灰裁剪虚线。
- [速查图 A4 版](output/pdf/句型速查图.pdf)：保留原来的 A4 版。
- [裁剪版图片 1](output/速查图-A4裁剪版-1.png) / [裁剪版图片 2](output/速查图-A4裁剪版-2.png)：对应裁剪版预览。
- [速查图 1 图片](output/速查图-1.png) / [速查图 2 图片](output/速查图-2.png)：手机查看或直接打印。
- [家长使用说明](家长使用说明.md) / [疑问词索引](疑问词索引.md)。
- 下载整个仓库后，双击 `index.html` 可离线按天查看和打印；不需要安装依赖。GitHub 页面直接查看 Markdown 或下载 PDF 即可。

每天 10 道主练 + 2 道订正换句 + 2 道回顾，共 560 题次（含有意安排的旧题重复）。40 天表示学习顺序，可以按实际负担拆分，不强求连续 40 天做完。

裁剪版打印：纸张选 **A4**、纵向、**实际大小 / 100%**、每张 1 页；打印后沿浅灰虚线裁剪，成品为 185 × 270 mm。无需注册自定义纸张。左右白边各 12.5 mm，上下白边各 13.5 mm；图内另保留 8 mm 阅读边距。内容按成品尺寸重新排版，不是把旧 A4 整张缩小。

## 学习顺序

| 天数 | 今日主题 | 学生版 | 家长版 |
|---|---|---|---|
'''+schedule+'''

## 维护与重建

题目源文件在 `materials/lessons.py`，每题包含题干、参考答案和订正要点；`materials/guide.py` 保存使用说明和疑问词索引。生成物均可重新构建。

```powershell
python -m pip install -r requirements.txt
python build.py
```

默认使用 Windows 宋体 `C:/Windows/Fonts/simsun.ttc`；其他系统运行前把 `STUDY_FONT` 环境变量设为可用的中文 TrueType 字体路径。PDF 已内嵌所用字体的字形子集。

速查图预览图片使用 Poppler 生成：

```powershell
pdftoppm -f 1 -l 2 -scale-to 1600 -png output/pdf/句型速查图.pdf output/速查图
pdftoppm -f 1 -l 2 -scale-to 1800 -png output/pdf/句型速查图-A4裁剪版.pdf output/速查图-A4裁剪版
```

`output/空白进度记录.csv` 是空白模板。孩子的实际作答和记录请放在已忽略的 `personal/` 目录，不提交到公开仓库。

范围、答案变体和参考资料见 [家长使用说明](家长使用说明.md)。不包含完整的过去时、将来时、现在完成时系列；have got 只讲拥有义。
'''
    (ROOT/'README.md').write_text(readme,encoding='utf-8')

def validate():
    assert len(LESSONS)==40
    assert [d['day'] for d in LESSONS]==list(range(1,41))
    for d in LESSONS:
        assert len(d['main'])==10 and len(d['transfer'])==2 and len(get_review(d))==2
        for q in d['main']+d['transfer']+get_review(d):
            assert all(q[k] for k in ('prompt','answer','why'))
            assert q['prompt'].count('**')%2==0
    for filename,count in [('学生练习册.pdf',40),('家长答案与订正.pdf',40),('句型速查图.pdf',2)]:
        reader = PdfReader(PDF/filename)
        assert len(reader.pages)==count,filename
        for n,page in enumerate(reader.pages,1):
            text = page.extract_text()
            assert len(text)>180,(filename,n)
            if count==40:
                expected = LESSONS[n-1]
                key = 'prompt' if filename=='学生练习册.pdf' else 'answer'
                compact = lambda s: re.sub(r'\s+', '', s.replace('**',''))
                actual = compact(text)
                for q in expected['main']+expected['transfer']+get_review(expected):
                    assert compact(q[key]) in actual,(filename,n,q[key])
    custom = PdfReader(PDF/'句型速查图-A4裁剪版.pdf')
    assert len(custom.pages)==2
    for page in custom.pages:
        assert abs(float(page.mediabox.width)*25.4/72-210)<.01
        assert abs(float(page.mediabox.height)*25.4/72-297)<.01
        assert len(page.extract_text())>700
    previous = json.loads((OUT/'构建检查.json').read_text(encoding='utf-8')) if not MIN_Y else {}
    positions = MIN_Y or previous['layout_checks']
    report = dict(days=40,main_items=400,transfer_items=80,review_slots=80,total_slots=560,
                  pdf_pages={'student':40,'answers':40,'cheatsheet':2,'cheatsheet_A4_crop':2},
                  crop_cheatsheet_page_mm=[210,297],crop_cheatsheet_finished_mm=[185,270],
                  min_content_y=min(v[2] for v in positions),
                  safe_bottom_y=42,layout_checks=positions)
    (OUT/'构建检查.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='layout_checks'},ensure_ascii=False))

if __name__=='__main__':
    PDF.mkdir(parents=True,exist_ok=True)
    if '--custom-cheatsheet-only' not in sys.argv:
        make_books()
        make_cheatsheet()
    make_crop_cheatsheet(PDF/'句型速查图-A4裁剪版.pdf')
    make_text_outputs()
    validate()
