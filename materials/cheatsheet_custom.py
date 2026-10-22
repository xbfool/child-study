"""在 A4 PDF 中居中排入 185 × 270 mm 速查图，白边与虚线方便裁剪。"""
from io import BytesIO
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from pypdf import PdfReader, PdfWriter, Transformation

W, H = 185*mm, 270*mm
M = 8*mm
CW = W-2*M
INK, BLUE, GREEN, ORANGE = map(HexColor, ['#162d44','#225b92','#177663','#aa5b19'])


def make_crop_cheatsheet(path):
    content = BytesIO()
    c = canvas.Canvas(content, pagesize=(W,H))
    c.setTitle('句型速查图 · A4 裁剪版 · 成品 185 × 270 mm')
    c.setAuthor('child-study')
    bottom_positions = []

    def p(text,x,y,width,size=10.5,color=INK):
        obj = Paragraph(escape(text), ParagraphStyle('custom',fontName='CN',
                        fontSize=size,leading=size+3.8,textColor=color))
        _,height=obj.wrap(width,H)
        obj.drawOn(c,x,y-height)
        return y-height

    def box(x,y,width,height,title,lines,color=BLUE,size=10.5):
        c.setStrokeColor(HexColor('#ccd8e3'))
        c.setFillColor(HexColor('#f5f8fb'))
        c.roundRect(x,y-height,width,height,7,fill=1,stroke=1)
        c.setFillColor(color)
        c.roundRect(x,y-24,width,24,7,fill=1,stroke=0)
        p(title,x+10,y-4,width-20,11.4,white)
        yy=y-33
        for text in lines:
            yy=p(text,x+10,yy,width-20,size)-5
        assert yy+5 >= y-height+3, ('卡片溢出', title, yy, y-height)
        bottom_positions.append(y-height)

    def header(title,subtitle):
        y=H-M
        c.setFillColor(INK)
        c.roundRect(M,y-58,CW,58,8,fill=1,stroke=0)
        p(title,M+12,y-8,CW-24,19,white)
        p(subtitle,M+12,y-35,CW-24,9.4,HexColor('#d5e6f3'))
        return y-70

    def footer(number):
        c.setStrokeColor(HexColor('#ccd8e3'))
        c.line(M,34,W-M,34)
        c.setFont('CN',8)
        c.setFillColor(INK)
        c.drawString(M,22,'句型速查图 · 成品 185 × 270 mm')
        c.drawRightString(W-M,22,f'{number} / 2')

    y=header('改句时，先走对这条路', '先看要求 → 圈出主语 → 选结构 → 检查要变的词')
    box(M,y,CW,55,'先看题目：问一句，还是改否定？',[
        '一般疑问句问“是不是 / 能不能”；特殊疑问句先选“问什么”。'
    ],INK)
    c.setStrokeColor(INK)
    mid=W/2
    c.line(mid,y-58,mid,y-68)
    c.line(mid,y-68,mid-3,y-64)
    c.line(mid,y-68,mid+3,y-64)
    y-=73
    gap=10
    half=(CW-gap)/2
    box(M,y,half,105,'① 句中已有 be',[
        'am / is / are → 放主语前',
        'She is happy. → Is she happy?',
        '否定：She isn’t happy.'
    ],BLUE,10.3)
    box(M+half+gap,y,half,105,'② 句中已有 can',[
        'can → 放主语前；后接原形',
        'She can swim. → Can she swim?',
        '否定：She can’t swim.'
    ],GREEN,10.3)
    y-=115
    box(M,y,CW,118,'③ 一般现在时普通动词：请 do / does 帮忙',[
        'I / you / we / they → Do；he / she / it / 单个人或物 → Does',
        'She likes cats. → Does she like cats?',
        '否定：She doesn’t like cats.',
        'does / doesn’t 后回原形：likes → like；has → have。'
    ],ORANGE,10.5)
    y-=128
    box(M,y,half,112,'have：看清有没有 got',[
        'She has a bike.',
        '→ Does she have a bike?',
        'She has got a bike.',
        '→ Has she got a bike?'
    ],BLUE,10.1)
    box(M+half+gap,y,half,112,'某处有 / 正在做',[
        'There is a cat. → Is there a cat?',
        'There are cats. → Are there cats?',
        'She is reading. → Is she reading?',
        '别把 is / are 漏掉。'
    ],GREEN,10.1)
    y-=122
    box(M,y,CW,155,'原形与三单：最后再检查一次',[
        '普通动词肯定句：She likes / watches / studies / has…；I / you 不算三单。',
        '通常加 s；ch / sh / s / x 等结尾加 es；辅音字母 + y → ies；have → has。',
        'can / do / does / don’t / doesn’t 后的主要动词，用原形。',
        'Let’s play. / Let him play. → Let’s not play. / Don’t let him play.',
        '祈使句：Open the door. → Don’t open the door. / Don’t be late.'
    ],INK,10.2)
    footer(1)
    c.showPage()

    y=header('我要问什么？我要感叹什么？','画线信息选疑问词；表达“多么……啊”时，再走 What / How')
    box(M,y,CW,95,'特殊疑问句：疑问词 + 一般疑问句的结构',[
        '地点：Where is Tom?    喜好：What does Tom like?',
        '能力：What can Tom draw?',
        '问“谁做”，who 自己当主语：Who likes cats?（不用再加 does）'
    ],BLUE,10.4)
    y-=107
    y=p('按信息找疑问词',M+2,y,CW-4,11.6)-5
    rows=[
        ('什么 what','谁 who','谁的 whose','哪里 where'),
        ('何时 when','几点 what time','星期 what day','日期 what date'),
        ('为何 why','哪个 which','方式 / 状态 how','几岁 how old'),
        ('颜色 what colour','尺码 what size','学科 what subject','种类 what kind of'),
        ('可数数量 how many + 复数','量 / 价格 how much'),
        ('多长 / 多久 how long','多远 how far','多常 how often','还要多久 how soon')
    ]
    for i,row in enumerate(rows):
        c.setFillColor(HexColor('#edf4fa') if i%2==0 else HexColor('#f7f9fb'))
        c.rect(M,y-30,CW,30,fill=1,stroke=0)
        width=CW/len(row)
        for j,text in enumerate(row):
            yy=p(text,M+j*width+6,y-6,width-12,10.1)
            assert yy>=y-28,('疑问词表格溢出',text)
        y-=30
    y-=8
    y=p('拓展：how tall 多高；how heavy 多重；whom 宾语“谁”。',M+4,y,CW-8,9.6)-3
    y=p('提建议：What about / How about + 名词或动词 ing。',M+4,y,CW-8,9.6)-10
    box(M,y,CW,100,'What：后面带“名词这一包”',[
        '一个可数物：What a nice bag it is! / What an old bike it is!',
        '复数：What nice bags they are!    不可数：What nice weather it is!',
        '单数可数用 a / an；复数、不可数不用。'
    ],GREEN,10.4)
    y-=110
    box(M,y,CW,79,'How：后面突出“怎么样”',[
        '形容词：How nice the bag is!    副词：How fast Tom runs!',
        '主语和动词保持陈述语序：the bag is；不是 is the bag。'
    ],ORANGE,10.4)
    y-=89
    box(M,y,CW,71,'最后看一眼：问号，还是感叹号？',[
        'What colour is the bag?（问颜色）',
        'How beautiful the bag is!（感叹：主语和动词不倒装）'
    ],INK,10.2)
    assert min(bottom_positions)>=43, ('页面底部溢出',min(bottom_positions))
    footer(2)
    c.showPage()
    c.save()
    content.seek(0)
    inner = PdfReader(content)
    writer = PdfWriter()
    dx,dy=(A4[0]-W)/2,(A4[1]-H)/2
    for page in inner.pages:
        outer = writer.add_blank_page(width=A4[0],height=A4[1])
        outer.merge_transformed_page(page,Transformation().translate(dx,dy))
        guides = BytesIO()
        guide_canvas = canvas.Canvas(guides,pagesize=A4)
        guide_canvas.setStrokeColor(HexColor('#9ba8b4'))
        guide_canvas.setLineWidth(.5)
        guide_canvas.setDash(3,3)
        guide_canvas.rect(dx,dy,W,H,fill=0,stroke=1)
        guide_canvas.setDash()
        guide_canvas.setFillColor(HexColor('#526579'))
        guide_canvas.setFont('CN',8)
        guide_canvas.drawCentredString(A4[0]/2,A4[1]-8*mm,
                                      'A4 打印 · 实际大小 / 100% · 沿虚线裁剪后 185 × 270 mm')
        guide_canvas.save()
        guides.seek(0)
        outer.merge_page(PdfReader(guides).pages[0])
    writer.add_metadata({'/Title':'句型速查图 · A4 裁剪版 · 成品 185 × 270 mm',
                         '/Author':'child-study'})
    with open(path,'wb') as stream:
        writer.write(stream)
    return min(bottom_positions)
