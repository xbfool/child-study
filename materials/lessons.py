"""原创题目。每行：题目 | 参考答案 | 订正要点。**标出提问目标**。"""

LESSONS = []

def day(title, focus, example, rows, transfer, checkpoint=False):
    def parse(text):
        result = []
        for line in text.strip().splitlines():
            parts = [x.strip() for x in line.split('|')]
            if len(parts) != 3:
                raise ValueError(line)
            result.append(dict(prompt=parts[0], answer=parts[1], why=parts[2]))
        return result
    main, fix = parse(rows), parse(transfer)
    assert len(main) == 10 and len(fix) == 2, title
    LESSONS.append(dict(day=len(LESSONS)+1, title=title, focus=focus,
                        example=example, main=main, transfer=fix, checkpoint=checkpoint))

day('先找“谁”，再选 am / is / are',
    '先圈出句子在说谁。I 配 am；he / she / it、一个人或物配 is；you / we / they、复数配 are。you 指一个人时也配 are。',
    'My sister is happy. → My sister 是一个人，相当于 she，所以用 is。', '''
圈出主语（句子在说谁）：The little girl is happy. | The little girl | 主语要圈完整，不只圈 girl。
圈出主语：Tom and Ben are friends. | Tom and Ben | 两个人合起来作主语。
填 am / is / are：I ___ nine. | am | I 配 am。
填 am / is / are：You ___ my friend. | are | you 即使指一个人也配 are。
填 am / is / are：My father ___ tall. | is | My father 是一个人。
填 am / is / are：The cats ___ small. | are | cats 是复数。
用 he / she / it / they 替换主语：My mother is a teacher. | She is a teacher. | mother 用 she。
用代词替换主语：The red bag is new. | It is new. | 一个物品用 it。
用代词替换主语：Lucy and Lily are happy. | They are happy. | 两个人用 they。
改正错误：My brother are ten. | My brother is ten. | brother 是一个人，配 is。
''', '''
填 am / is / are：The boys ___ in the room. | are | boys 是复数。
用代词替换主语：The dog is hungry. | It is hungry. | 一只动物，此处用 it。
''')

day('be：肯定与否定',
    '句中已有 am / is / are，否定时就在它后面加 not。is not = isn’t；are not = aren’t；am not 不能写成 amn’t。',
    'The dog is big. → The dog is not big.', '''
改为否定句：She is happy. | She is not happy. | 在 is 后加 not；isn't 也对。
改为否定句：They are in the classroom. | They are not in the classroom. | 在 are 后加 not；aren't 也对。
改为否定句，保留 I：I am tired. | I am not tired. | I 不需自动改成 you。
写出缩写：He is not tall. | He isn't tall. | is not 缩写成 isn't。
写出缩写：We are not late. | We aren't late. | are not 缩写成 aren't。
写出完整形式：It isn't cold. | It is not cold. | isn't = is not。
选词：The boys (isn't / aren't) hungry. | aren't | boys 是复数。
改正错误：Lucy not is sad. | Lucy is not sad. | not 放在 is 后。
改正错误：The bag doesn't is blue. | The bag is not blue. | 这里用 is 的否定，不加 doesn't。
改为肯定句：The flowers aren't red. | The flowers are red. | 去掉 not，保留 are。
''', '''
改为否定句：Ben is at home. | Ben is not at home. | is 后加 not；isn't 也对。
改正错误：I amn't hungry. | I am not hungry. | am not 没有 amn't 这种标准缩写。
''')

day('be：一般疑问句和简短回答',
    '一般疑问句是在问“是不是”。把 am / is / are 放到主语前面，句末用问号。简短回答要根据所问的人选代词。',
    'Lucy is happy. → Is Lucy happy? → Yes, she is. / No, she isn’t.', '''
改为一般疑问句：Ben is a pupil. | Is Ben a pupil? | is 提到 Ben 前。
改为一般疑问句：The bags are heavy. | Are the bags heavy? | are 提前，bags 不变。
改为一般疑问句：The cat is under the chair. | Is the cat under the chair? | is 提前，其余顺序保留。
作肯定简短回答：Is Lucy ten? | Yes, she is. | Lucy 用 she，回答保留 is。
作否定简短回答：Are the boys tired? | No, they aren't. | boys 用 they。
作否定简短回答：Is the milk hot? | No, it isn't. | milk 用 it。
选词：___ your sister at school? (Is / Does) | Is | 表示“在哪里”，原结构是 sister is。
连词成句：your / are / friends / they / ? | Are they your friends? | Are + 主语 they + 其余部分。
改正错误：Does Tom is happy? | Is Tom happy? | 已有 is，不再加 does。
按对话回答，回答者是你本人：Are you ready?（肯定） | Yes, I am. | 对方问 you，你用 I 回答。
''', '''
改为一般疑问句：The book is on the desk. | Is the book on the desk? | is 放主语前。
作否定简短回答：Are the cats hungry? | No, they aren't. | cats 用 they，are 配 aren't。
''')

day('can：会不会、能不能',
    'can 后接动词原形，主语换成 he / she 也不加 s。否定用 cannot / can’t；提问时把 can 放在主语前。',
    'She can swim. → Can she swim? → She can’t swim.', '''
选词：Tom can (swim / swims). | swim | can 后用原形。
改为否定句：Lucy can dance. | Lucy can't dance. | can't 后仍是 dance；cannot 也对。
改为一般疑问句：The boy can ride a bike. | Can the boy ride a bike? | can 提前，ride 不变。
作肯定简短回答：Can Ben run fast? | Yes, he can. | 用 can 回答。
作否定简短回答：Can the girls sing? | No, they can't. | girls 用 they。
用 She 改写整句：They can draw. | She can draw. | can 和 draw 都不加 s。
改正错误：He cans jump. | He can jump. | can 没有这里的 cans 形式。
改正错误：Does Lucy can swim? | Can Lucy swim? | can 自己提前，不加 does。
连词成句：can / the / fly / bird / ? | Can the bird fly? | can + 主语 + 原形。
先写中文意思，再改一般疑问句：Tom can cook. | 汤姆会做饭。Can Tom cook? | 先理解能力，再把 can 提前。
''', '''
改为否定句：The dog can swim. | The dog can't swim. | can 后加 not。
改正错误：Can she dances? | Can she dance? | can 后动词用原形。
''')

day('小复习一：be 和 can 分清楚',
    '独立完成。本页不提供规则或例题；先判断要表达什么，再决定怎样改。', '', '''
填空：The children ___ happy. (am / is / are) | are | children 是复数。
改为一般疑问句：The girl is tired. | Is the girl tired? | is 提前。
改为一般疑问句：The girl can skate. | Can the girl skate? | can 提前。
改为否定句：The boys are at home. | The boys are not at home. | are 后加 not；aren't 也对。
改为否定句：The boys can swim. | The boys can't swim. | can't 后用原形。
作肯定简短回答：Is your father tall? | Yes, he is. | father 用 he。
作否定简短回答：Can Lucy draw? | No, she can't. | Lucy 用 she，can 配 can't。
改正错误：The cat are small. | The cat is small. | 一只 cat 配 is。
改正错误：She can sings. | She can sing. | can 后还原。
按对话回答，回答者是你本人：Are you a pupil?（肯定） | Yes, I am. | 问 you，回答 I。
''', '''
改为一般疑问句：The ducks are in the water. | Are the ducks in the water? | are 提前。
改正错误：Is Ben can ride a bike? | Can Ben ride a bike? | 能不能用 can 这套结构。
''', True)

day('普通动词：先看主语是不是第三人称单数',
    '一般现在时中，I / you / we / they 后普通动词通常用原形；he / she / it、一个人的名字或单数名词作主语时，动词要用第三人称单数形式。“第三人称单数”不是“只要一个人”：I、you 不属于这一组。',
    'I like cats. / Tom likes cats. / Tom and Lucy like cats.', '''
判断主语是否第三人称单数（是 / 否）：I | 否 | I 是第一人称。
判断主语是否第三人称单数（是 / 否）：you（指一个人） | 否 | you 是第二人称。
判断主语是否第三人称单数（是 / 否）：My sister | 是 | 一个姐姐 / 妹妹，相当于 she。
判断主语是否第三人称单数（是 / 否）：Tom and Ben | 否 | 两个人，是复数。
选词：I (like / likes) milk. | like | I 后用原形。
选词：She (like / likes) milk. | likes | she 后用三单形式。
选词：The boys (play / plays) football. | play | boys 是复数。
选词：My father (read / reads) books every day. | reads | father 是一个人。
用 He 改写：They eat rice every day. | He eats rice every day. | eat 变 eats。
改正错误：You likes apples. | You like apples. | you 后不用三单形式。
''', '''
选词：The dog (run / runs) every morning. | runs | dog 是单数主语。
用 They 改写：She likes cats. | They like cats. | 复数主语配 like。
''')

day('第三人称单数：s、es、ies 和特殊变化',
    '多数动词加 s；以 s / x / ch / sh 等结尾常加 es；辅音字母 + y 结尾，变 y 为 ies；元音字母 + y 直接加 s。记住 have → has、do → does、go → goes。',
    'play → plays；study → studies；watch → watches；have → has。', '''
写出第三人称单数形式：read | reads | 直接加 s。
写出第三人称单数形式：watch | watches | ch 后加 es。
写出第三人称单数形式：wash | washes | sh 后加 es。
写出第三人称单数形式：study | studies | 辅音字母 d + y，变 ies。
写出第三人称单数形式：play | plays | a 是元音字母，保留 y 加 s。
写出第三人称单数形式：go | goes | 记住 goes。
写出第三人称单数形式：do | does | 特殊变化 does。
写出第三人称单数形式：have | has | 特殊变化 has。
用所给词填空：My sister ___ English every day. (study) | studies | 主语是单数，study 变 studies。
用所给词填空：Ben ___ TV after dinner. (watch) | watches | Ben 配 watches。
''', '''
用所给词填空：The baby ___ at night. (cry) | cries | 辅音字母 r + y，变 ies。
改正错误：Lucy plaies tennis every week. | Lucy plays tennis every week. | play 是元音字母 + y。
''')

day('do / does：普通动词的一般疑问句',
    '一般现在时的普通动词提问，I / you / we / they 等用 Do，he / she / it 等用 Does。加了 Does，后面的动词回原形。do 在这里帮助提问，不必翻译成“做”。',
    'Lucy likes cats. → Does Lucy like cats?', '''
填 Do / Does：___ the boys like football? | Do | boys 是复数。
填 Do / Does：___ your mother read books? | Does | mother 是单数。
改为一般疑问句：They play tennis. | Do they play tennis? | Do + they + 原形。
改为一般疑问句：He plays tennis. | Does he play tennis? | plays 回到 play。
改为一般疑问句：Lucy studies English. | Does Lucy study English? | studies 回到 study。
改为一般疑问句：Ben goes to school by bus. | Does Ben go to school by bus? | goes 回到 go。
作肯定简短回答：Does Tom like milk? | Yes, he does. | does 问，does 答。
作否定简短回答：Do the girls play football? | No, they don't. | Do 问，don't 否定回答。
改正错误：Does she watches TV? | Does she watch TV? | does 后用原形。
改正错误：Is Ben like apples? | Does Ben like apples? | like 是普通动词，用 does 提问。
''', '''
改为一般疑问句：The cat drinks milk. | Does the cat drink milk? | drinks 还原为 drink。
作否定简短回答：Does Lucy go to school by bike? | No, she doesn't. | Lucy 用 she，配 doesn't。
''')

day('don’t / doesn’t：普通动词的否定句',
    '一般现在时的普通动词否定：I / you / we / they 等用 don’t；he / she / it 等用 doesn’t；后面都接动词原形。',
    'She likes milk. → She doesn’t like milk.', '''
选词：I (don't / doesn't) like fish. | don't | I 配 don't。
选词：My brother (don't / doesn't) play tennis. | doesn't | brother 是单数。
改为否定句：They read books every day. | They don't read books every day. | 普通动词前加 don't。
改为否定句：Lucy reads books every day. | Lucy doesn't read books every day. | reads 回到 read。
改为否定句：Ben studies Chinese. | Ben doesn't study Chinese. | studies 回到 study。
改为否定句：The dog eats rice. | The dog doesn't eat rice. | eats 回到 eat。
改正错误：He doesn't likes bananas. | He doesn't like bananas. | doesn't 后不保留 s。
改正错误：They aren't play football. | They don't play football. | 这里是普通动词的一般现在时。
改为肯定句：She doesn't watch TV on Monday. | She watches TV on Monday. | 去掉 doesn't 后，watch 恢复三单。
按对话回答，回答者是你本人：Do you like milk?（否定） | No, I don't. | 问 you，回答 I。
''', '''
改为否定句：My father goes to work by car. | My father doesn't go to work by car. | goes 还原成 go。
改为肯定句：The boy doesn't wash his hands before lunch. | The boy washes his hands before lunch. | 单数主语，wash 加 es。
''')

day('小复习二：be / can / do 三路混合',
    '独立完成。本页不提供规则或例题；同样是“提问”，要先看原句的结构。', '', '''
改为一般疑问句：Lucy is a pupil. | Is Lucy a pupil? | be 结构，is 提前。
改为一般疑问句：Lucy can draw. | Can Lucy draw? | can 提前。
改为一般疑问句：Lucy draws cats. | Does Lucy draw cats? | 普通动词，does + 原形。
改为否定句：The boys are tired. | The boys are not tired. | are 后加 not。
改为否定句：The boys can skate. | The boys can't skate. | can 后加 not。
改为否定句：The boys skate every Sunday. | The boys don't skate every Sunday. | 复数主语，don't + 原形。
用所给词填空：My sister ___ to school every day. (walk) | walks | 普通动词肯定句用三单。
改正错误：Does he is ten? | Is he ten? | is 提问，不加 does。
改正错误：Can she plays football? | Can she play football? | can 后用原形。
作否定简短回答：Does Ben study English? | No, he doesn't. | Does 问，doesn't 答。
''', '''
改为一般疑问句：The bird sings every morning. | Does the bird sing every morning? | sings 还原为 sing。
改为否定句：The bird can sing. | The bird can't sing. | 用 can 的否定。
''', True)

day('have / has：谁有，谁吃，谁上课',
    '一般现在时肯定句中，I / you / we / they 用 have；he / she / it 等第三人称单数用 has。have 可以表示“有”，也出现在 have breakfast、have a lesson 等搭配中。',
    'They have a ball. / She has a ball. / She has breakfast at seven.', '''
选词：I (have / has) a new bag. | have | I 配 have。
选词：You (have / has) a red pen. | have | you 配 have。
选词：Tom (have / has) a bike. | has | Tom 是三单主语。
选词：The girls (have / has) long hair. | have | girls 是复数。
用所给词填空：My father ___ breakfast at seven. (have) | has | have breakfast 表示吃早饭。
用所给词填空：We ___ an English lesson on Monday. (have) | have | we 配 have。
用 She 改写：They have a cat. | She has a cat. | have 变 has。
用 They 改写：He has two books. | They have two books. | has 变 have。
改正错误：My brother haves a football. | My brother has a football. | have 的三单是 has。
改正错误：She can has some milk now. | She can have some milk now. | can 后用原形 have。
''', '''
用所给词填空：The dog ___ a long tail. (have) | has | 一只狗配 has。
用 We 改写：She has lunch at school. | We have lunch at school. | 复数主语配 have。
''')

day('have：用 do / does 提问和否定',
    '本页练不带 got 的 have，统一使用 do / does 这套：Does she have…? / She doesn’t have…；have breakfast 也按普通动词处理。',
    'He has a bike. → Does he have a bike? → He doesn’t have a bike.', '''
改为一般疑问句（用 Do）：They have a ball. | Do they have a ball? | have 作普通动词。
改为一般疑问句（用 Does）：Lucy has a bike. | Does Lucy have a bike? | has 还原为 have。
改为否定句（用 doesn't）：Ben has a kite. | Ben doesn't have a kite. | doesn't 后用 have。
改为否定句（用 don't）：The boys have a dog. | The boys don't have a dog. | boys 配 don't。
改为一般疑问句：She has breakfast at home. | Does she have breakfast at home? | has breakfast 中 has 也还原。
作肯定简短回答：Does Lucy have a sister? | Yes, she does. | does 问，does 答。
作否定简短回答：Do the boys have a ball? | No, they don't. | Do 问，don't 答。
改正错误：Does Ben has a ruler? | Does Ben have a ruler? | does 后不能保留 has。
改正错误：She doesn't has lunch at school. | She doesn't have lunch at school. | doesn't 后用 have。
改为肯定句：He doesn't have a pet. | He has a pet. | 去掉 doesn't 后，have 变 has。
''', '''
改为一般疑问句（用 Does）：The cat has a long tail. | Does the cat have a long tail? | has 变 have。
改为否定句（用 doesn't）：My mother has tea after lunch. | My mother doesn't have tea after lunch. | 否定用 doesn't have。
''')

day('have got：另一套结构，别混搭',
    '表示“拥有”时，have / has got 是另一套：提问把 have / has 提前；否定在它后面加 not。不要把 does 与 has got 拼在一起。此处是“拥有”，不是现在完成时教学。',
    'She has got a bike. → Has she got a bike? → She hasn’t got a bike.', '''
选词：Tom (have / has) got a blue bag. | has | Tom 配 has got。
改为一般疑问句，保留 got：They have got a kite. | Have they got a kite? | have 提前，got 保留。
改为一般疑问句，保留 got：Lucy has got a doll. | Has Lucy got a doll? | has 提前。
改为否定句，保留 got：He has got a bike. | He hasn't got a bike. | has 后加 not。
作肯定简短回答：Has Ben got a ball? | Yes, he has. | has 问，has 答，简答不必写 got。
作否定简短回答：Have the girls got any books? | No, they haven't. | have 问，haven't 答。
改正错误，保留 got：Does she has got a cat? | Has she got a cat? | have got 结构不用 does。
改写同义句，用 has got：Tom has a ruler. | Tom has got a ruler. | 这里两种形式都表示拥有。
改写同义句，用 Does 且不含 got：Has Lucy got a kite? | Does Lucy have a kite? | 换成普通 have 结构。
选择表达“她每天七点吃早饭”：She (has / has got) breakfast at seven every day. | has | 日常吃早饭用 has breakfast。
''', '''
改为一般疑问句，保留 got：The dog has got big ears. | Has the dog got big ears? | has 提前。
改写同义句，用 doesn't 且不含 got：He hasn't got a sister. | He doesn't have a sister. | 转换整套结构，不能混搭。
''')

day('there be：某处有；some / any 看语境',
    'there is / are 表示“某处有”；人“拥有”通常用 have / has。there be 提问把 is / are 提前，简答用 there。普通询问或否定中 some 常改 any；请求、邀请中可保留 some。',
    'There are some books on the desk. → Are there any books on the desk?', '''
填 is / are：There ___ a cat under the table. | is | a cat 是单数。
填 is / are：There ___ three books in the bag. | are | three books 是复数。
填 is / are：There ___ some milk in the glass. | is | milk 是不可数名词。
选词：Tom (has / there is) a red bag. | has | Tom 拥有一个包。
改为一般疑问句：There is a ball in the box. | Is there a ball in the box? | is 提到 there 前。
改为一般疑问句（普通询问）：There are some apples on the table. | Are there any apples on the table? | are 提前，some 变 any。
改为否定句：There is some water in the bottle. | There isn't any water in the bottle. | is 后加 not，some 变 any。
作肯定简短回答：Are there any books on the desk? | Yes, there are. | there be 的简答保留 there。
作否定简短回答：Is there a dog in the room? | No, there isn't. | 不能用 it isn't 代替本题简答。
选词：Would you like (some / any) milk?（邀请对方喝一点） | some | 邀请中可以用 some，不能见问号就改 any。
''', '''
改为一般疑问句（普通询问）：There is some juice in the cup. | Is there any juice in the cup? | is 提前，some 变 any。
改为否定句：There are some birds in the tree. | There aren't any birds in the tree. | are not + any。
''')

day('小复习三：have、have got、there be',
    '独立完成。本页不提供规则或例题；看清题目要求保留哪一套结构。', '', '''
填空：My sister ___ a new bike. (have / has) | has | 单数主语配 has。
改为一般疑问句（用 Does）：Tom has a pet. | Does Tom have a pet? | does + have。
改为否定句（用 doesn't）：Lucy has lunch at home. | Lucy doesn't have lunch at home. | doesn't 后用 have。
改为一般疑问句，保留 got：Ben has got a toy car. | Has Ben got a toy car? | has 提前。
作否定简短回答：Has Lucy got a ruler? | No, she hasn't. | has 问，hasn't 答。
填空：There ___ two cats under the tree. (is / are) | are | 两只猫配 are。
改为一般疑问句（普通询问）：There are some oranges in the box. | Are there any oranges in the box? | are 提前，some 变 any。
作否定简短回答：Are there any flowers in the room? | No, there aren't. | there 的简答。
改正错误：Does she has a brother? | Does she have a brother? | does 后还原。
改正错误：There have three books on the desk. | There are three books on the desk. | 表示某处有，使用 there are。
''', '''
改为否定句，保留 got：The boy has got a robot. | The boy hasn't got a robot. | has 后加 not。
作肯定简短回答：Does the girl have a kite? | Yes, she does. | 用 does 回答。
''', True)

day('现在进行时：be + 动词 ing',
    '描述正在发生的动作，用 am / is / are + 动词 ing。问句把 be 提前；否定在 be 后加 not。动词 ing 不能代替 be，句中也不用再加 do / does。',
    'Tom is reading. → Is Tom reading? → Tom isn’t reading.', '''
填空：Lucy ___ reading now. (am / is / are) | is | Lucy 配 is。
填空：The boys ___ playing football now. (am / is / are) | are | boys 配 are。
写出 ing 形式：make | making | 去掉不发音的 e 再加 ing。
写出 ing 形式：run | running | 双写 n 再加 ing。
写出 ing 形式：swim | swimming | 双写 m 再加 ing。
改为一般疑问句：Lucy is drawing a cat. | Is Lucy drawing a cat? | is 提前，drawing 保留。
改为否定句：The children are singing. | The children aren't singing. | are 后加 not。
作肯定简短回答：Is Ben sleeping? | Yes, he is. | is 问，is 答。
改正错误：She reading a book now. | She is reading a book now. | 正在做，需要 is reading。
改正错误：Does Tom playing football now? | Is Tom playing football now? | 进行时用 is 提问。
''', '''
改为一般疑问句：The dog is running now. | Is the dog running now? | is 提前。
改为否定句：They are making a cake. | They aren't making a cake. | are 后加 not。
''')

day('每天做，和正在做',
    'every day / usually 等常描述习惯，用一般现在时；明确说 now / Look! / Listen! 且描述正在发生的动作时，用现在进行时。先理解时间和意思，不只找词。',
    'She reads every day. / She is reading now.', '''
用所给词填空：Tom ___ football every Sunday. (play) | plays | 习惯动作，单数主语用 plays。
用所给词填空：Look! Tom ___ football. (play) | is playing | 眼前正在踢球。
用所给词填空：The girls ___ every morning. (sing) | sing | 复数主语的习惯动作用原形。
用所给词填空：Listen! The girls ___. (sing) | are singing | 正在唱歌，are + singing。
改为一般疑问句：Lucy reads every day. | Does Lucy read every day? | 一般现在时用 does。
改为一般疑问句：Lucy is reading now. | Is Lucy reading now? | 现在进行时用 is。
改为否定句：Ben swims every Saturday. | Ben doesn't swim every Saturday. | doesn't 后用 swim。
改为否定句：Ben is swimming now. | Ben isn't swimming now. | is 后加 not。
把 every day 改为 now，并改写：She makes a cake every day. | She is making a cake now. | makes 变 is making。
把 now 改为 every day，并改写：He is washing his hands now. | He washes his hands every day. | is washing 变 washes。
''', '''
改为一般疑问句：The boy walks to school every day. | Does the boy walk to school every day? | does + walk。
改为一般疑问句：The boy is walking to school now. | Is the boy walking to school now? | is + 主语 + walking。
''')

day('改单复数：整句一起检查',
    '改单复数时，要检查指示词、主语、be、普通动词、名词和代词。this / that 对应 these / those；a / an 在复数句中去掉。can 后动词始终用原形。',
    'This is a small cat. → These are small cats.', '''
改为复数句：This is a red apple. | These are red apples. | this / is / a / apple 都要检查。
改为复数句：That is an egg. | Those are eggs. | that 变 those，去掉 an。
改为单数句：These are books. | This is a book. | these 变 this，补 a。
改为单数句：Those are orange bags. | That is an orange bag. | orange 以元音音素开头，用 an。
用 They 改写：He has a kite. | They have a kite. | 只指定换主语，a kite 不必变复数。
用 They 改写：She plays football. | They play football. | plays 变 play。
用 He 改写：They can ride bikes. | He can ride bikes. | 只换主语，can ride 不变。
将 The child 改成 The children 并改写：The child is happy. | The children are happy. | child 的复数是 children。
将 The mouse 改成 The mice 并改写：The mouse has a long tail. | The mice have long tails. | 本题改成多只老鼠，have，尾巴用复数。
改正错误：These is a books. | These are books. | these 配 are，复数名词前去掉 a。
''', '''
改为复数句：This is a big box. | These are big boxes. | box 复数加 es。
用 She 改写：They go to school by bus. | She goes to school by bus. | go 变 goes。
''')

day('祈使句：请做、别做',
    '祈使句常省略主语 you，以动词原形开头；否定常用 Don’t + 动词原形。Be quiet. 的否定是 Don’t be quiet.；“保持安静”常说 Be quiet.，“别吵”常说 Don’t be noisy.',
    'Open the door. → Don’t open the door. / Be late. → Don’t be late.', '''
选词：(Open / Opens) the book, please. | Open | 祈使句用原形。
改为否定祈使句：Close the window. | Don't close the window. | Don't + close。
改为否定祈使句：Run in the classroom. | Don't run in the classroom. | Don't + run。
改为否定祈使句：Be late. | Don't be late. | be 也要保留原形。
改为肯定祈使句：Don't touch the box. | Touch the box. | 去掉 Don't，首字母大写。
用所给词填空：Don't ___ here. (swim) | swim | Don't 后用原形。
连词成句：quiet / be / please / . | Please be quiet. / Be quiet, please. | please 可在句首或句末。
改正错误：Doesn't run here. | Don't run here. | 否定祈使句用 Don't。
改正错误：Don't are late. | Don't be late. | Don't 后用 be 原形。
用祈使句表达“请坐下”。 | Sit down, please. / Please sit down. | Sit 用原形，please 表礼貌。
''', '''
改为否定祈使句：Eat in the library. | Don't eat in the library. | Don't + eat。
改正错误：Don't touches the flowers. | Don't touch the flowers. | Don't 后不加 es。
''')

day('let / Let’s：后面接谁，动作怎么写',
    'Let’s = Let us，常表示“我们一起……吧”。Let + me / him / her / us / them + 动词原形。Let’s 的常用否定是 Let’s not + 原形；Don’t let him… 是“不让他……”。',
    'Let’s play. / Let him play. / Let’s not run here.', '''
选词：Let's (play / plays) football. | play | Let's 后用原形。
选词：Let (he / him) open the door. | him | let 后的人称代词用宾格。
选词：Let (they / them) help us. | them | let 后用 them。
把 Let's 写成完整形式：Let's go home. | Let us go home. | 本题只展开缩写。
改为常用否定形式：Let's swim here. | Let's not swim here. | Let's not + 原形。
改为否定祈使句：Let him open the box. | Don't let him open the box. | Don't let + 宾语 + 原形。
改正错误：Let her goes first. | Let her go first. | her 后用 go 原形。
改正错误：Lets play a game. | Let's play a game. | 建议一起做事，Let's 有撇号。
用 Let's 表达“我们一起做蛋糕吧”。 | Let's make a cake. | Let's 后用 make。
用 Let 表达“让我帮你”。 | Let me help you. | me 是宾格，help 用原形。
''', '''
改为常用否定形式：Let's eat here. | Let's not eat here. | Let's not + eat。
改正错误：Let she read the book. | Let her read the book. | let 后用宾格 her。
''')

day('what / where：先确定是在问什么',
    '画线内容是物或所做的事，常用 what；是地点，用 where。先选疑问词，再按原句结构组织问句。目标内容要从问句里拿掉。',
    'Tom is in the park. → Where is Tom? / Tom likes apples. → What does Tom like?', '''
只写疑问词：The bag is **under the desk**. | Where | 问地点。
只写疑问词：Lucy likes **apples**. | What | 问喜欢什么。
对画线部分提问：The cat is **in the box**. | Where is the cat? | Where + is + 主语。
对画线部分提问：The boys are **in the library**. | Where are the boys? | 复数主语配 are。
对画线部分提问：Tom likes **milk**. | What does Tom like? | What + does，likes 还原。
对画线部分提问：They play football **in the park**. | Where do they play football? | 普通动词、复数主语用 do。
对画线部分提问：Lucy reads books **at home**. | Where does Lucy read books? | does 后用 read。
对画线部分提问：Ben can draw **a dog**. | What can Ben draw? | What + can + 主语 + draw。
改正错误：Where does Lucy reads books? | Where does Lucy read books? | does 后用原形。
改正错误，使它只问猫在哪里：Where is the cat in the box? | Where is the cat? | 地点已被 where 代替。
''', '''
对画线部分提问：The dog is **under the tree**. | Where is the dog? | 地点用 Where，is 提前。
对画线部分提问：Lily eats **rice** for lunch. | What does Lily eat for lunch? | does 后用 eat。
''')

day('who / whose：谁，还是谁的',
    'who 问人；whose 问归属。“谁的书”可用 Whose book。Tom’s 表示“汤姆的”；his / her 是“他的 / 她的”。问物品主人时，别误用 who。',
    'She is Lucy. → Who is she? / This is Tom’s bag. → Whose bag is this?', '''
选疑问词：(Who / Whose) is that boy? He is Ben. | Who | 问那个人是谁。
选疑问词：(Who / Whose) bag is this? It is Lucy's. | Whose | 问包属于谁。
对画线部分提问：She is **Lucy**. | Who is she? | 问身份，用 Who。
对画线部分提问，保留 bag：This is **Tom's** bag. | Whose bag is this? | Whose + bag，is this。
对画线部分提问，保留 books：These are **Ben's** books. | Whose books are these? | books 是复数，配 are。
对画线部分提问，保留 pen：That is **her** pen. | Whose pen is that? | her 表示归属。
选择符合问题的回答：Whose ruler is it? (It's red. / It's Lily's.) | It's Lily's. | whose 要回答主人。
选择符合问题的回答：Who is he? (He's Tom. / It's Tom's.) | He's Tom. | who 要回答人是谁。
改正错误：Who's bag is this? | Whose bag is this? | who's = who is，不是 whose。
连词成句：these / whose / are / shoes / ? | Whose shoes are these? | Whose + 名词 + are + these。
''', '''
对画线部分提问，保留 coat：This is **Mary's** coat. | Whose coat is this? | 询问归属。
对画线部分提问：He is **Mr Li**. | Who is he? | 询问身份。
''')

day('when / what time / what day / what date',
    'when 问时间，范围较广；what time 常问几点；what day 问星期几；what date 问日期。题目指定用哪个时，就按指定问法写。',
    'It is Monday. → What day is it? / It is 22 October. → What date is it?', '''
只写疑问词组，问几点：It is **seven o'clock**. | What time | 问钟点。
只写疑问词组，问星期：It is **Tuesday**. | What day | 问星期几。
只写疑问词组，问日期：It is **1 June**. | What date | 问日期。
对画线部分提问，用 What time：Tom gets up **at six**. | What time does Tom get up? | does 后 get 用原形，去掉 at six。
对画线部分提问，用 When：They play football **on Sunday**. | When do they play football? | When + do + 主语。
对画线部分提问：It is **Friday**. | What day is it? | 星期用 What day。
对画线部分提问：It is **10 September**. | What date is it? | 日期用 What date。
对画线部分提问：It is **eight o'clock**. | What time is it? | 问现在几点。
改正错误：What time does Lucy goes to school? | What time does Lucy go to school? | does 后用 go。
对画线部分提问，用 When：Ben has a music lesson **on Tuesday**. | When does Ben have a music lesson? | has 还原为 have。
''', '''
对画线部分提问，用 What time：Lucy goes to bed **at nine**. | What time does Lucy go to bed? | does + go。
对画线部分提问：It is **Wednesday**. | What day is it? | 问星期。
''')

day('how / how old / how many',
    'how 可以问状态或方式；how old 问年龄；how many + 可数名词复数，问数量。how many 不是单独放句首就结束，常要带上所数的东西。',
    'She is ten. → How old is she? / There are three cats. → How many cats are there?', '''
选词：___ is your mother? She is fine. (How / How old) | How | fine 回答状态。
选词：___ is Ben? He is nine. (How / How old) | How old | nine 在此回答年龄。
对画线部分提问：Lucy is **ten years old**. | How old is Lucy? | 去掉整个年龄信息。
对画线部分提问：The children are **fine**. | How are the children? | how 问状态。
对画线部分提问：There are **four** books on the desk. | How many books are there on the desk? | How many + books + are there。
对画线部分提问：Tom has **two** sisters. | How many sisters does Tom have? | has 还原为 have。
对画线部分提问：They have **three** balls. | How many balls do they have? | balls 用复数。
改正错误：How many book does Lucy have? | How many books does Lucy have? | how many 后名词用复数。
连词成句：old / your / is / how / brother / ? | How old is your brother? | How old + is + 主语。
选择符合问题的回答：How many dogs are there? (They are brown. / There are two.) | There are two. | 要回答数量。
''', '''
对画线部分提问：There are **five** girls in the room. | How many girls are there in the room? | 问数量而不是人是谁。
对画线部分提问：Lucy's sister is **eight**. | How old is Lucy's sister? | 整个主语保留，问年龄。
''')

day('how much：多少，还是多少钱',
    'how much + 不可数名词可以问量；How much is / are…? 可以问价格。how many 后接可数名词复数。钱的多少与物品的数量要分清。',
    'How much milk is there? / How much are the shoes? / How many shoes are there?', '''
填 many / much：How ___ water is there? | much | water 是不可数名词。
填 many / much：How ___ apples are there? | many | apples 可数复数。
填 many / much：How ___ rice does Tom have? | much | rice 不可数。
对画线部分提问：The bag is **fifty yuan**. | How much is the bag? | 问价格，单数物品配 is。
对画线部分提问：The shoes are **eighty yuan**. | How much are the shoes? | shoes 复数配 are。
对画线部分提问：Lucy has **some** milk. | How much milk does Lucy have? | 问牛奶的量，用 How much milk。
对画线部分提问：There is **some** juice in the bottle. | How much juice is there in the bottle? | 问不可数名词的量。
对画线部分提问：There are **six** eggs in the box. | How many eggs are there in the box? | eggs 可数，用 How many。
改正错误：How many is this book?（问价格） | How much is this book? | 问价格用 How much。
改正错误：How much bananas does Ben have? | How many bananas does Ben have? | bananas 可数复数。
''', '''
对画线部分提问：The toy car is **thirty yuan**. | How much is the toy car? | 问单个物品价格。
填 many / much：How ___ bread is there? | much | bread 不可数。
''')

day('which 和 what 的各种搭配',
    'which 常在给定范围里选“哪一个”；what 常问“什么”。what colour / size / subject / kind of… 分别问颜色、尺码、学科、种类。固定词组要整体理解。',
    'The red bag or the blue bag? → Which bag…? / The bag is red. → What colour…?', '''
选词：___ bag do you like, the red one or the blue one? (Which / Where) | Which | 在两个包中选择。
对画线部分提问：The kite is **yellow**. | What colour is the kite? | 问颜色。
对画线部分提问：The shoes are **black**. | What colour are the shoes? | shoes 是复数。
对画线部分提问，用 What subject：Lucy likes **English**. | What subject does Lucy like? | subject 问学科，does + like。
对画线部分提问：Ben wears **size 32** shoes. | What size shoes does Ben wear? | 问鞋的尺码，wear 用原形。
对画线部分提问，用 Which bag：Tom likes **the blue bag**, not the red one. | Which bag does Tom like? | 有给定的选择范围。
填空：What ___ animals does Lucy like? She likes cats.（问种类） | kind of | What kind of animals 问动物种类。
用 What about 提建议：“喝些果汁怎么样？” | What about some juice? | What about + 名词短语。
选词：What about (play / playing) football? | playing | about 后接动词 ing。
改正错误：What colour does the bag is? | What colour is the bag? | 原句结构是 bag is，不能加 does。
''', '''
对画线部分提问：The flowers are **pink**. | What colour are the flowers? | 问颜色，用 are。
用 How about 改写同义句：What about playing a game? | How about playing a game? | How about 后也接动词 ing。
''')

day('why / how：原因、方式与天气',
    'why 问原因，常用 because 回答；how 问方式，可以用 by bus / on foot 等回答。How is the weather? 与 What is the weather like? 都可以问天气。',
    'He walks to school. → How does he go to school? / He is happy because… → Why is he happy?', '''
选词：___ is Lucy happy? Because it is her birthday. (Why / Where) | Why | because 回答原因。
选词：___ does Tom go to school? By bus. (How / How old) | How | 问出行方式。
对画线部分提问：Ben goes to school **by bike**. | How does Ben go to school? | 问方式，does + go。
对画线部分提问：The children go to the park **on foot**. | How do the children go to the park? | 复数主语用 do。
对画线部分提问：Lucy is sad **because her cat is ill**. | Why is Lucy sad? | why 代替整个原因部分。
对画线部分提问：Tom likes winter **because he can make a snowman**. | Why does Tom like winter? | why + does，likes 还原。
按天气提问，用 How：It is **sunny** today. | How is the weather today? | 问天气状态。
改写同义问句，用 What：How is the weather today? | What is the weather like today? | What…like 是完整天气问法。
改正错误：Why does Ben likes summer? | Why does Ben like summer? | does 后用原形。
选择符合问题的回答：Why are you tired? (By bus. / Because I run a lot.) | Because I run a lot. | why 要回答原因。
''', '''
对画线部分提问：Lily goes to the library **by bus**. | How does Lily go to the library? | 方式用 How。
对画线部分提问：The boy is happy **because he has a new bike**. | Why is the boy happy? | 原句有 is，直接用 is 组问句。
''')

day('how long / far / often / soon：分清量的种类',
    'how long 问长度或持续多久；how far 问距离；how often 问频率；how soon 问还要多久，常用 in + 时间回答。how tall / heavy 问身高 / 体重。本页后两题为拓展识别。',
    'two hours → How long；two kilometres → How far；twice a week → How often；in two days → How soon。', '''
选择词组（How long / How far）：___ is the ruler? It is twenty centimetres long. | How long | 问物体长度。
选择词组（How long / How far）：___ is it from Ben's home to school? It is two kilometres. | How far | 问两地距离。
选择词组（How often / How soon）：___ does Lucy swim? Twice a week. | How often | 问频率。
选择词组（How often / How soon）：___ will Dad come back? In two days. | How soon | 问从现在起还要多久。
对画线部分提问，用 How long：Tom reads **for twenty minutes** every day. | How long does Tom read every day? | 问持续时长，does + read。
对画线部分提问：Lucy plays tennis **twice a week**. | How often does Lucy play tennis? | 问频率。
对画线部分提问，用 How far：It is **three kilometres** from the park to the school. | How far is it from the park to the school? | 问距离。
对画线部分提问，用 How long：The ruler is **thirty centimetres long**. | How long is the ruler? | 问长度。
拓展选词（How tall / How heavy）：___ is Ben? He is 140 centimetres tall. | How tall | 问身高。
拓展选词（How tall / How heavy）：___ is the box? It is five kilograms. | How heavy | 问重量。
''', '''
对画线部分提问：Ben visits his grandma **once a week**. | How often does Ben visit his grandma? | 频率用 How often。
选择词组（How far / How soon）：___ will the bus come? In five minutes. | How soon | 从现在起还要五分钟；只要求选词组。
''')

day('who 问主语，和 who 问宾语',
    '问“谁做这件事”，who 自己当主语，通常不额外加 do / does；问“某人帮助谁、喜欢谁”，原主语保留，常要用 do / does。whose 仍然问归属。',
    'Lucy helps Tom. → Who helps Tom? / Who does Lucy help?', '''
对画线部分提问：**Lucy** likes apples. | Who likes apples? | 谁喜欢？who 代替主语，likes 保留。
对画线部分提问：**Ben** plays football every day. | Who plays football every day? | who 作主语。
对画线部分提问：**Tom** can swim. | Who can swim? | who 代替 Tom，保留 can。
对画线部分提问：**Lucy** is reading. | Who is reading? | who 代替主语。
对画线部分提问：Lucy helps **Tom**. | Who does Lucy help? / Whom does Lucy help? | Lucy 仍是主语；口语常用 who，正式也可 whom。
对画线部分提问：Tom likes **Miss Li**. | Who does Tom like? / Whom does Tom like? | likes 还原为 like。
对画线部分提问：**Ben** has a red bike. | Who has a red bike? | who 作主语，保留 has。
对画线部分提问，保留 bike：This is **Ben's** bike. | Whose bike is this? | 问归属用 whose。
改正错误，表达“谁喜欢牛奶？”：Who does likes milk? | Who likes milk? | who 本身是主语。
只写中文区别：Who helps Ben? / Who does Ben help? | 谁帮助本？ / 本帮助谁？ | 前一句问帮助者，后一句问被帮助者。
''', '''
对画线部分提问：**Lily** reads books every day. | Who reads books every day? | who 代替主语。
对画线部分提问：Ben helps **Lily**. | Who does Ben help? / Whom does Ben help? | Ben 是保留的主语。
''')

day('小复习四：疑问词与结构一起选',
    '独立完成。不提供规则或例题；画线部分就是要问的信息。', '', '''
对画线部分提问：The dog is **under the chair**. | Where is the dog? | 地点用 Where，be 结构用 is。
对画线部分提问，保留 coat：This is **Lucy's** coat. | Whose coat is this? | 问归属。
对画线部分提问：Tom likes **bananas**. | What does Tom like? | 问喜欢什么，does + like。
对画线部分提问：Ben is **eleven**. | How old is Ben? | 问年龄。
对画线部分提问：There are **seven** books on the desk. | How many books are there on the desk? | 问数量，books 用复数。
对画线部分提问：The dress is **sixty yuan**. | How much is the dress? | 问价格。
对画线部分提问，用 What time：Lucy gets up **at seven**. | What time does Lucy get up? | 问钟点，gets 还原。
对画线部分提问：Tom walks to school **because his home is near the school**. | Why does Tom walk to school? | 问原因，walks 还原。
对画线部分提问：**Ben** has a pet. | Who has a pet? | who 作主语不加 does。
对画线部分提问：Lily reads books **every day**. | How often does Lily read books? | 问频率；When does Lily read books? 也可表达时间询问，但本页优先频率问法。
''', '''
对画线部分提问：The shoes are **white**. | What colour are the shoes? | 问颜色。
对画线部分提问：Lucy goes to the park **by bus**. | How does Lucy go to the park? | 问方式。
''', True)

day('What 感叹句：一个人或物',
    '感叹句表达“多么……啊”，不是在提问。单数可数名词常用 What a / an + 形容词 + 名词 + 主语 + be!；a / an 看后面紧跟词的开头音。',
    'It is a nice day. → What a nice day it is!', '''
填 a / an：What ___ nice book it is! | a | nice 以辅音音素开头。
填 a / an：What ___ interesting book it is! | an | interesting 以元音音素开头。
填 a / an：What ___ useful book it is! | a | useful 开头是 /j/，是辅音音素。
用 What 改为完整感叹句：It is a big dog. | What a big dog it is! | What a + big dog + it is。
用 What 改为完整感叹句：It is an old bike. | What an old bike it is! | old 前用 an。
用 What 改为完整感叹句：She is a kind girl. | What a kind girl she is! | 保留 she is 的陈述语序。
用 What 改为完整感叹句：He is a tall boy. | What a tall boy he is! | What 后接名词短语。
连词成句：a / what / day / lovely / it / is / ! | What a lovely day it is! | 名词短语提前，it is 不倒装。
改正错误：What a nice bag is it! | What a nice bag it is! | 本套练标准陈述语序。
在句末填 ? 或 !：What a beautiful flower it is___ | ! | 表达感叹，不是提问。
''', '''
用 What 改为完整感叹句：It is a small cat. | What a small cat it is! | 单数 cat 前保留 a。
用 What 改为完整感叹句：It is an interesting story. | What an interesting story it is! | interesting 前用 an。
''')

day('What 感叹句：复数和不可数名词',
    '复数可数名词、不可数名词的 What 感叹句不加 a / an。What + 形容词 + 复数名词 / 不可数名词 + 主语 + 动词! 仍保持陈述语序。',
    'They are nice flowers. → What nice flowers they are! / It is good news. → What good news it is!', '''
选词：What (a / 不填) beautiful flowers they are! | 不填 | flowers 是复数。
选词：What (a / 不填) nice weather it is! | 不填 | weather 不可数。
用 What 改为完整感叹句：They are lovely cats. | What lovely cats they are! | 复数 cats 前无 a。
用 What 改为完整感叹句：They are big boxes. | What big boxes they are! | boxes 用复数。
用 What 改为完整感叹句：It is clean water. | What clean water it is! | water 不可数，无 a。
用 What 改为完整感叹句：It is good news. | What good news it is! | news 不可数，不能加 a。
用 What 改为完整感叹句：It is nice weather. | What nice weather it is! | weather 不可数。
改正错误：What a beautiful birds they are! | What beautiful birds they are! | birds 是复数，去掉 a。
改正错误：What an interesting books they are! | What interesting books they are! | books 是复数，去掉 an。
连词成句：what / children / happy / they / are / ! | What happy children they are! | children 是复数，无 a。
''', '''
用 What 改为完整感叹句：They are small ducks. | What small ducks they are! | 复数不用 a。
用 What 改为完整感叹句：It is sweet milk. | What sweet milk it is! | milk 不可数。
''')

day('How 感叹句：形容词和副词',
    'How + 形容词 / 副词 + 主语 + 动词!；How 后面可以接 beautiful、fast、well 等。不要因为中文都是“多么”就把 What 和 How 混用。',
    'The girl is happy. → How happy the girl is! / Tom runs fast. → How fast Tom runs!', '''
选词：(How / What) tall Ben is! | How | tall 是形容词，后面直接接主语 Ben。
选词：(How / What) a tall boy Ben is! | What | a tall boy 是名词短语。
用 How 改为完整感叹句：The cat is cute. | How cute the cat is! | How + cute + the cat is。
用 How 改为完整感叹句：The flowers are beautiful. | How beautiful the flowers are! | 主语 flowers 为复数。
用 How 改为完整感叹句：Lucy is kind. | How kind Lucy is! | How 后不加 a。
用 How 改为完整感叹句：Tom runs fast. | How fast Tom runs! | fast 修饰 runs，保留三单。
用 How 改为完整感叹句：Ben swims well. | How well Ben swims! | well 修饰动作。
用 How 改为完整感叹句：The children sing beautifully. | How beautifully the children sing! | beautifully 修饰 sing。
改正错误：How beautiful are the flowers! | How beautiful the flowers are! | 本套练陈述语序。
改正错误：How a nice book it is! | What a nice book it is! / How nice the book is! | 选完整的一套，不能混搭。
''', '''
用 How 改为完整感叹句：The boy is clever. | How clever the boy is! | How + 形容词 + 主语 + be。
用 How 改为完整感叹句：Lily dances well. | How well Lily dances! | well 提前，dances 保留三单。
''')

day('同一个意思，用 What 和 How 两种表达',
    'What 感叹句突出名词短语；How 感叹句突出形容词 / 副词。改写时要重新组织主语，不能只换第一个词。',
    'What a nice bag it is! ↔ How nice the bag is!', '''
用 How 改写同义感叹句：What a big dog it is! | How big the dog is! | big 后直接接主语 the dog。
用 What 改写同义感叹句：How big the dog is! | What a big dog it is! | 单数 dog 前要有 a。
用 How 改写同义感叹句：What beautiful flowers they are! | How beautiful the flowers are! | the flowers 变为主语。
用 What 改写同义感叹句：How beautiful the flowers are! | What beautiful flowers they are! | flowers 是复数，无 a。
用 How 改写同义感叹句：What nice weather it is! | How nice the weather is! | the weather 作主语。
用 What 改写同义感叹句：How nice the weather is! | What nice weather it is! | weather 不可数，无 a。
用 How 改写同义感叹句：What an interesting book it is! | How interesting the book is! | How 后直接接 interesting。
用 What 改写同义感叹句：How kind the girl is! | What a kind girl she is! | she 指 the girl。
填 What / How：___ fast the boy runs! | How | fast 是副词，后接主语。
改正错误：What beautiful the flowers are! | How beautiful the flowers are! / What beautiful flowers they are! | 改成任意一套完整结构。
''', '''
用 How 改写同义感叹句：What a cute cat it is! | How cute the cat is! | cute 后接主语 the cat。
用 What 改写同义感叹句：How old the bike is! | What an old bike it is! | old 前用 an。
''')

day('小复习五：感叹和提问别混',
    '独立完成。不提供规则或例题；先看题目要求是在提问，还是在感叹。', '', '''
用 What 改为完整感叹句：It is a lovely dog. | What a lovely dog it is! | 单数 dog 前用 a。
用 What 改为完整感叹句：They are beautiful trees. | What beautiful trees they are! | 复数不用 a。
用 What 改为完整感叹句：It is nice weather. | What nice weather it is! | weather 不可数。
用 How 改为完整感叹句：The boy runs fast. | How fast the boy runs! | runs 保留三单。
用 How 改为完整感叹句：The girls are happy. | How happy the girls are! | 陈述语序 girls are。
填 a / an：What ___ interesting game it is! | an | interesting 前用 an。
对画线部分提问：The bag is **red**. | What colour is the bag? | 这里是在问颜色。
用 How 改为完整感叹句：The bag is beautiful. | How beautiful the bag is! | 这里是在感叹。
改正错误：What a beautiful flowers they are! | What beautiful flowers they are! | flowers 复数，去掉 a。
用 How 改写同义感叹句：What a clever girl she is! | How clever the girl is! / How clever she is! | How 后接 clever，再接主语。
''', '''
用 What 改为完整感叹句：It is an old house. | What an old house it is! | old 前用 an。
对画线部分提问：The flowers are **yellow**. | What colour are the flowers? | 问颜色，末尾用问号。
''', True)

day('混合练习一：先说思路，再动笔',
    '每题先口头说两件事：题目要问 / 改什么？原句属于哪种结构？需要时可翻前面的规则，做完标记“独立”或“看过提示”。',
    'She has a bike.（一般疑问句，用 Does）→ 拥有；普通 have 结构 → Does she have a bike?', '''
改为一般疑问句：The girl is in the room. | Is the girl in the room? | be 结构，is 提前。
改为一般疑问句：The girl can make a cake. | Can the girl make a cake? | can 提前，make 不变。
改为一般疑问句：The girl makes cakes on Sunday. | Does the girl make cakes on Sunday? | does + make。
改为否定句（用 doesn't）：Tom has a dog. | Tom doesn't have a dog. | has 还原为 have。
对画线部分提问：Ben is reading **in the library**. | Where is Ben reading? | 地点用 Where，进行时用 is。
对画线部分提问：Lucy has **three** pencils. | How many pencils does Lucy have? | 问数量，has 还原。
改为否定祈使句：Touch the flowers. | Don't touch the flowers. | Don't + 原形。
改正错误：Let him goes home. | Let him go home. | let + 宾格 + 原形。
用 What 改为完整感叹句：It is a nice picture. | What a nice picture it is! | What + 单数名词短语。
用 How 改为完整感叹句：The boy swims well. | How well the boy swims! | How + 副词 + 主语 + 动词。
''', '''
对画线部分提问：Tom goes to school **at eight**.（用 What time） | What time does Tom go to school? | does 后用 go。
改为一般疑问句，保留 got：Lily has got a red bag. | Has Lily got a red bag? | has 提前。
''')

day('混合练习二：开始独立改句',
    '先独立做，再订正；遇到难题先留空，全部做完后再看提示。', '', '''
用所给词填空：Lucy's brother ___ English every day. (study) | studies | 单数主语，study 变 studies。
改为一般疑问句：The boys are making a cake. | Are the boys making a cake? | 进行时把 are 提前。
改为否定句：Ben can ride a bike. | Ben can't ride a bike. | can 后加 not。
改为一般疑问句（普通询问）：There are some eggs in the box. | Are there any eggs in the box? | are 提前，some 变 any。
对画线部分提问，保留 bag：This is **Lily's** bag. | Whose bag is this? | 询问归属。
对画线部分提问：The toy is **forty yuan**. | How much is the toy? | 询问价格。
对画线部分提问：**Tom** helps Lucy. | Who helps Lucy? | who 作主语，保留 helps。
用 How 改写同义感叹句：What beautiful birds they are! | How beautiful the birds are! | the birds 作主语。
改为常用否定形式：Let's play here. | Let's not play here. | Let's not + 原形。
根据对话情境选 some / any：May I have ___ water, please?（请求喝一点水） | some | 请求并期待肯定回应，可以用 some。
''', '''
对画线部分提问：Lucy helps **Ben**. | Who does Lucy help? / Whom does Lucy help? | Lucy 保留，does + help。
用 What 改为完整感叹句：It is good news. | What good news it is! | news 不可数，不加 a。
''')

day('混合练习三：同词不同作用',
    '独立完成。本页出现的 do、have、what、how，要结合整句理解。', '', '''
改为一般疑问句：Ben does his homework after dinner. | Does Ben do his homework after dinner? | 第一个 Does 帮助提问，后面的 do 表示做作业。
改为否定句：Lucy does her homework at school. | Lucy doesn't do her homework at school. | doesn't 后用 do 原形。
对画线部分提问：Tom is **a teacher**.（问职业，用 What…do） | What does Tom do? | 问职业，不是正在做什么。
对画线部分提问：Tom is **reading a book** now.（用 doing 提问） | What is Tom doing now? | 问正在做的动作。
改为一般疑问句（用 Does）：Lucy has breakfast at seven. | Does Lucy have breakfast at seven? | 日常吃早饭是 have 结构。
改为一般疑问句，保留 got：Lucy has got a pet. | Has Lucy got a pet? | 拥有的 have got 结构。
对画线部分提问：It is **Monday**. | What day is it? | 星期不是日期。
对画线部分提问：It is **12 May**. | What date is it? | 日期不是星期。
用 How 改为完整感叹句：The dress is beautiful. | How beautiful the dress is! | 感叹，用陈述语序。
对画线部分提问：The dress is **blue**. | What colour is the dress? | 问颜色，用疑问语序。
''', '''
改为一般疑问句：Lily does her homework every day. | Does Lily do her homework every day? | Does + 主语 + do。
对画线部分提问：Ben is **making a kite** now.（用 doing 提问） | What is Ben doing now? | is + 主语 + doing。
''')

day('综合卷 A：不看提示',
    '独立完成并记录用时。做完后再看答案；写对但解释不清的题标“△”，订正后做换句题。', '', '''
改为一般疑问句：The children are in the park. | Are the children in the park? | children 复数，用 are。
改为一般疑问句：Tom can speak English. | Can Tom speak English? | can 提前。
改为一般疑问句：Lucy watches TV after dinner. | Does Lucy watch TV after dinner? | watches 还原。
改为否定句（用 doesn't）：Ben has a red bike. | Ben doesn't have a red bike. | has 还原。
对画线部分提问：There are **eight** ducks in the water. | How many ducks are there in the water? | 问数量，ducks 用复数。
对画线部分提问，保留 book：That is **Tom's** book. | Whose book is that? | 问归属。
对画线部分提问：Lily goes to school **on foot**. | How does Lily go to school? | 问方式，go 用原形。
改为否定祈使句：Let him touch the box. | Don't let him touch the box. | Don't let + 宾语 + 原形。
用 What 改为完整感叹句：It is an interesting film. | What an interesting film it is! | interesting 前用 an。
用 How 改为完整感叹句：The girls dance well. | How well the girls dance! | well 修饰 dance，陈述语序。
''', '''
对画线部分提问：Ben plays football **three times a week**. | How often does Ben play football? | 问频率。
改为一般疑问句：The girl is making a card. | Is the girl making a card? | 进行时把 is 提前。
''', True)

day('综合卷 B：隔天换句再检查',
    '独立完成并记录用时。与综合卷 A 分开做；两卷都能独立完成，再把易错题隔一周重做。', '', '''
用所给词填空：My father ___ to work by bus every day. (go) | goes | 单数主语的一般现在时。
改为一般疑问句，保留 got：Ben has got a robot. | Has Ben got a robot? | has got 结构。
改为否定句：The children are running now. | The children aren't running now. | are 后加 not。
作否定简短回答：Does Lucy have a ruler? | No, she doesn't. | does 问，doesn't 答。
对画线部分提问：**Lily** likes cats. | Who likes cats? | who 作主语。
对画线部分提问：Tom is happy **because it is his birthday**. | Why is Tom happy? | 原因用 Why，be 结构用 is。
对画线部分提问：The shoes are **ninety yuan**. | How much are the shoes? | 问价格，复数用 are。
改为常用否定形式：Let's swim in the river. | Let's not swim in the river. | Let's not + 原形。
用 What 改为完整感叹句：They are beautiful pictures. | What beautiful pictures they are! | 复数不用 a。
用 How 改写同义感叹句：What a cute dog it is! | How cute the dog is! | the dog 改作主语。
''', '''
对画线部分提问，用 What time：Ben has lunch **at twelve**. | What time does Ben have lunch? | has 还原为 have。
对画线部分提问：Lucy has **four** books. | How many books does Lucy have? | 数量用 How many，has 还原。
''', True)
