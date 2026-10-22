"""速查图、家长指南的结构化文字，和题库分开维护。"""

WH = [
    ('what', '什么 / 什么事', 'What does Ben like?', '21、38'),
    ('who', '谁（人）', 'Who helps Ben? / Who does Ben help?', '22、29'),
    ('whose', '谁的（归属）', 'Whose bag is this?', '22'),
    ('where', '哪里（地点）', 'Where is the cat?', '21'),
    ('when', '什么时候', 'When does Ben swim?', '23'),
    ('what time', '几点（钟点）', 'What time does Ben get up?', '23'),
    ('what day', '星期几', 'What day is it?', '23'),
    ('what date', '几月几日（日期）', 'What date is it?', '23'),
    ('why', '为什么（原因）', 'Why is Ben happy?', '27'),
    ('which + 名词', '哪一个（给定范围里选择）', 'Which bag does Ben like?', '26'),
    ('how', '怎样 / 如何 / 身体怎么样', 'How does Ben go to school?', '24、27'),
    ('how old', '几岁（年龄）', 'How old is Ben?', '24'),
    ('how many + 复数名词', '多少个（可数）', 'How many books does Ben have?', '24、25'),
    ('how much', '多少钱 / 多少量（不可数）', 'How much is it? / How much milk…?', '25'),
    ('what colour', '什么颜色', 'What colour is the bag?', '26'),
    ('what size', '什么尺码', 'What size shoes does Ben wear?', '26'),
    ('what subject', '什么学科', 'What subject does Ben like?', '26'),
    ('what kind of', '什么种类', 'What kind of animals does Ben like?', '26'),
    ('how long', '多长 / 持续多久', 'How long is the ruler?', '28'),
    ('how far', '多远（距离）', 'How far is it from A to B?', '28'),
    ('how often', '多久一次（频率）', 'How often does Ben swim?', '28'),
    ('how soon', '还要多久（拓展）', 'How soon will Dad come back?', '28'),
    ('how tall / how heavy', '多高 / 多重（拓展）', 'How tall / heavy is Ben?', '28'),
    ('whom', '谁（宾语，正式用法，拓展）', 'Whom does Ben help?', '29'),
    ('what about / how about', '……怎么样（提建议）', 'What about playing a game?', '26、拓展'),
]

PARENT = '''# 家长使用说明

这是一套面向小学阶段的英语句型基础重建材料，按“各项都需要从头理清”编排。以当前提出的学习范围为主，不声称是上海新版教材的官方配套或完整考试大纲。

## 今天就能开始

1. 打开 `output/pdf/学生练习册.pdf`，打印第 1 页；PDF 第几页就是第几天。
2. 把两张速查图放在旁边。需要 185 × 270 mm 成品时，使用 `output/pdf/句型速查图-A4裁剪版.pdf`：仍选 A4、实际大小 / 100% 打印，再沿虚线裁剪。原 A4 版保存在 `output/pdf/句型速查图.pdf`。新内容允许查图，复习卷先独立做。
3. 读“今天先看”和例子，孩子用自己的话说一次规则；家长不要先把本页题目讲完。
4. 做 A 区 10 题，记录“独立对 / 看提示对 / 待订正”。约 15～20 分钟是安排起点，实际按孩子负担调整，没做完可以拆两次。
5. 对照独立的家长答案。先找一个错误原因，再让孩子遮住答案重做原题，随后做 B 区两道换句题。
6. C 区两道旧题用于隔天及更早内容的复练；Day 1 则隔五分钟回头重做。做旧题先遮住规则卡，不会时再打开。

## 订正怎么做

不要只抄答案。每道错题按“说意思 → 找主语 → 选结构 → 完整重写 → 换句再试”走一遍。

例如：错写 `Does Lucy has a bike?`。先问“这里问的是有没有车吗？”再指出“Lucy 是第三人称单数，所以前面用 Does；Does 已经承担变化，后面写 have”。遮住答案重写，再做一题 `Ben has a ruler.` 的一般疑问句。

错误标记只选最先卡住的一项：

- M：意思 / 题目要求没读清，或不知道在问哪部分。
- S：结构选错，例如把 Is、Can、Does 混用。
- A：主语与形式不配，例如 boys is、she have。
- V：动词形式错，例如 does likes、can swims、let him goes。
- W：疑问词、名词单复数、代词或 a / an / some / any 选错。
- P：大小写、标点、漏词或拼写。

写对但靠猜、讲不出理由的题记 △；在提示下完成记 H。二者都不算“独立掌握”。这些标记帮助安排复练，不是给孩子贴标签。

## 什么时候往下走

以下是本套材料的家庭使用建议，不是测评标准：A 区至少 8 / 10 能独立完成，B 区两道换句题能在订正后独立完成，就继续下一天；不到这个程度，可以把同一天拆开、隔天再做。第一次答错不代表不能继续，先看错误集中在哪里。

Day 5、10、15、30、35、39、40 是独立复习页，不给新课规则；Day 36 允许说思路并查图。综合卷 A、B 分开两天做，结束一周后再挑易错题。40 天是顺序，不是硬性期限。

## 批改边界

- 本套答案是参考答案，不能只按字符串一模一样批改。is not / isn't、does not / doesn't、cannot / can't 等完整与缩写形式通常等价；题目指定缩写时例外。
- 只指定“用 He / They 改写”时，按语义需要改主语和动词，不随意把所有名词都变复数。明确“改为复数句”时，再整体处理指示词、冠词、名词和一致关系。
- 第一、第二人称不规定机械互换。仅在题目明确对话身份时改 I / you、my / your；其余保持原叙述视角。
- 普通 have 的练习明确指定 Do / Does；have got 的练习要求保留 got。英语中拥有义 have 还有其他变体，本套选择两套清晰的常用结构，不把其他合法用法一概判错。
- some 在普通询问中常改 any，但请求和邀请中可保留 some。不能只看问号。
- What / How 感叹句练学校常见的完整陈述语序。口语中还有省略和其他感叹表达，不在本套主练范围。
- whose 与 who's（who is / who has 的缩写）不同；此处主练 who is 的理解。
- How often 与 When 有时都能提出符合语义的问题；题目限定问法时按限定，未限定时结合信息目标判断。本套优先让频率信息对应 How often。
- What about / How about + 名词或动词 ing 属于提建议，与一般的“画线提问”分开理解。

## 范围与词汇

核心包括：主语和代词、be、can、第三人称单数、do / does、have / has、have got、there be、some / any、现在进行时、单复数改写、祈使句、let / Let's、一般疑问句、特殊疑问句、What / How 感叹句。

疑问词按“问什么”整理：what、who、whose、where、when、what time、what day、what date、why、which、how、how old、how many、how much、what colour、what size、what subject、what kind of、how long、how far、how often；how soon、how tall、how heavy、whom 是拓展识别。what season / sport / food 等可在 what + 名词的结构上迁移；how high / fast / wide 等可在 how + 形容词 / 副词上迁移，不把任意组合都单列成固定疑问词。

一般过去时、现在完成时、将来时的完整改句体系不在本套核心内；how soon 里有 will 的拓展例子，只要求识别问法。have got 在本套只讲“拥有”。日后需要时，可另做时态系列。

词汇不认识可以直接告诉中文，不把查生词混成今天的语法目标。常见词：pupil 小学生；ruler 尺子；kite 风筝；tail 尾巴；skate 滑冰；study 学习；subject 学科；size 尺码；weather 天气；news 消息；useful 有用的；interesting 有趣的；centimetre 厘米；kilometre 千米；kilogram 千克；once 一次；twice 两次。

## 参考资料

题目和版面为本项目原创编写，以下资料仅用于核对规则，不复制练习题。它们不是上海四年级考试范围证明。

- 教育部：《义务教育课程方案和课程标准（2022年版）》发布页：https://www.moe.gov.cn/srcsite/A26/s8001/202204/t20220420_619921.html
- British Council，Present simple – verb to be：https://learnenglishkids.britishcouncil.org/grammar-vocabulary/grammar-practice/present-simple-verb-be
- British Council，Present simple：https://learnenglish.britishcouncil.org/free-resources/grammar/a1-a2/present-simple
- British Council，Have got：https://learnenglishkids.britishcouncil.org/zh-hans/grammar-practice/have-got
- British Council，Question words：https://learnenglishteens.britishcouncil.org/grammar/a1-a2-grammar/question-words
- Cambridge，Let, let's：https://dictionary.cambridge.org/grammar/british-grammar/let
- Cambridge，Exclamations：https://dictionary.cambridge.org/grammar/british-grammar/exclamations

核对日期：2026-10-22。请不要把孩子姓名、学校、实际作答或成绩上传公开仓库；记录表可留在本地 `personal/` 目录。
'''
