# R588　完整来源必要对象与原 RootStats 的具名可逆关系

作者：OpenAI / ChatGPT root（AI）。日期：2026-11-16。

**可信度：已证明（限本文的有限元数据表示、逆映射和实际来源接口条件）；尚无新科学运行、实际字节收益、原必要读回成功或数学接受。**

本件支付 R537、R552、R555 已明确显示的另一项责任：原必要对象虽然在同 job 被完整选择，却可能超过原单份 90000 字节上限。当前不足不是可以删掉的错误、末次记录或未访地址；也不能用外层退出码、SHA、成功 report 或旧实验数字补出没有返回的正文。本件给出只作用于明确命名的来源记录和 RootStats 成员的关系表示。它保留输入选择的每个原值及其类型，不增加科学字段选择，不改变任何原数值或接受门。

完整作者源为 computations/root_20261116_complete_named_source_and_root_statistics_relations.py，19120 B / SHA256 6f7cb8049e8b77b26964deb675e5868d6b374ac2e07c49b6517c8e51d7db0dad。该文件只作 JSON 元数据操作；没有文件读写、数组加载、求解器、编译器、subprocess、科学时钟或额外数值检查。本文没有在作者环境 import、AST、编译、执行或作 fixture。

## 588.1　实际问题与本件的范围

[R552](R552-actual232-root-reuse-and-two-incomplete-necessary-readbacks.md) 的 actual232 已返回来源生成及402项绑定成功，随后科学/rules/outer退出1；完整来源必要169036 B、科学必要144265 B分别超限，只返回1818 B及1130 B的不完整对象。[R555](R555-actual233-science-return-and-two-necessary-overflow-boundaries.md) 的 actual233 来源397项和原恢复成功，完整来源153703 B、科学122410 B同样未返回。[R537](R537-actual226-complete-source-return-and-scientific-necessary-overflow.md) 则明确来源56393 B完整、科学109972 B未返。

这些是三个不同实际运行。它们不能证明某个已知内部错误重复出现，也不能证明每份未返对象具体由哪些字段占满。本件没有那些大正文，不能把它们当作 fixture 或可恢复输入。可用依据是上述真实超限，以及已刊 reader/generator 的完整确定源码。新的表示只能在下一次真实 run 内消费其实际选择对象，不能修改旧 run 的事实。

当前直接源码基线是 [R573/request240](R573-request240-exact-root-synthesis-products-and-complete-current-model-entry.md)：

| 来源 | bytes | SHA256 |
|---|---:|---|
| 来源生成器 | 38611 | 3bb1084dfb44d675db8f186b138c5fb68ac6da9a1978f25c013e2bc5609f9cf2 |
| 当前必要 reader | 63394 | e48c769418ffac56a2e931cbee4bc4474ad2067007e561c2aaa49f9a4291701b |
| 当前 root adapter | 20999 | cdc734c9b704ffa77f46b32054cff1dbae4df10e91f6be66f4ddeb53a4237fcf |
| 当前 root primal | 27592 | 8952e5a65a04e918d00ef990a1355ba3c1912284dfc2c482d8f861aa896b660a |
| 当前 root trace | 36252 | 138c6aaaba86628befd71b398bd2d393e661cb4abdab7781d6ef1ba0bebe05bb |

这些基线已刊，当前R573 run仍独立冻结；本件不推断其未来结果。新的真实调用链另由R589/request246支付。本件没有新 run 或新父。

## 588.2　表示对象及精确性口径

输入是原 reader 已经选出的解析 JSON 元数据，不是 scientific raw，也不是任意完整科学树。原选择器决定哪些文件、错误、路径、统计、部分进度和未访状态必须返回；本件在该选择完成后才处理其中两个固定域：

1. 完整原 source-preparation necessary 对象；
2. 原 RootWordMetadata 的八个明确命名 catalogue，在其既有外层列表示之前。

“完整保留”指输入到本件的每个 JSON 值、类型、数组顺序、字段存在性及字典成员顺序均可重建。此前选择器若已经形成具名表、非有限标量展示或相等对象引用，本件完整保留其定义与值，再按原逆映射解释。它不倒退声称恢复了原日志空格、原JSON重复键、gzip字节、未选择的 raw 数组或 IEEE NaN payload。

原 canonical JSON 使用 sort_keys、ASCII、紧凑分隔符和一个末LF。其序列化字节不是原二进制科学状态。本件需要比较完整列值时，使用保成员顺序的 JSON 表示，并另核严格类型/值/顺序相等；不用数值近似、浮点容差、摘要碰撞或文件basename相同来合并不同记录。

## 588.3　固定关系族

源中 FAMILIES 是封闭的名称集合。来源域只允许：

| 族 | 被表示的原对象 |
|---|---|
| source_binding | 五代R535/R550/R561/R564/R572实际binding及其installed schema |
| verified_source_identity | 与当前完整已核source map相符的原file/bytes/SHA三字段 |
| source_run_context | 已识别binding内的原run对象 |
| source_inventory_rows | 四代已定义的完整ordered source inventory记录 |
| source_literal_change_rows | 四代已定义的完整ordered literal change记录 |
| source_identity_catalogue | 四代完整具名source catalogue定义 |
| source_literal_sha256 | 上一行内唯一明确literal_sha256_values列的原字符串 |

另有 owner compilation、physical source input两个既有具名来源族。统计域只允许R550/R561/R564/R572各自的完整section、path、last。没有用于一般数值数组、任意科学对象或任意字符串的字典编码族。

source_scope可以遍历已经选出的完整来源对象以定位这些明确source schema及严格身份三元组；它不扩展原选择。科学域没有采用这种一般遍历：root_record只读取八个已命名catalogue及四个已命名RootStats成员，其余所有成员原样保留。

未知schema，包括list/dict/null形式的异常schema，不能被当作已知source schema。未知catalogue或未知RootStats成员不会被丢弃，也不因不了解其含义而填默认值。

## 588.4　完整行与列的有限表示

对固定关系族f，设其实际原记录依次为

$$
v_0,\ldots,v_{n-1}.
$$

只有完整有序 JSON 表示相同且严格类型/值/顺序相同的记录才能共用索引。不同整数/浮点数、布尔/整数、正零/负零、null/缺失、不同成员序或数组序，都不能因通常语言的宽松相等而共享。

每个原记录本身仍是完整字典。按它实际有序key元组分组。对某组的第j列：

- 若该列每个原值严格相同，保一个constant；
- 否则保每个原值组成的original_values，顺序正是该组的原记录顺序。

每组另外保完整columns及original_record_indices；record_count明确给出原catalogue长度。原记录的所有未知key也进入columns，没有仅选择某些已知计数。若两个记录key集合相同但顺序不同，它们属于不同组。

**命题588.A。** 该列表示唯一重建每个被登记的完整原记录。

证明：每个原索引只在一个组中出现一次。按该组columns的原顺序插入字段；每列取constant或其原位置的original_values。两种情形均等于该位置的原值。存在的key由columns穷尽；未出现的key不会被生成。原索引决定完整记录序。因此所有记录逐项重建，且缺失/null及原顺序均保留。证毕。

代码的restore_relation对record_count、索引范围/唯一性、列数、列key唯一性和original_values长度作元数据格式核对。这是给出的逆程序，并不被安装成solver或metric接受门；未来入口也不得将一次独立反解对拍加为科学前置条件。

## 588.5　有限引用、冲突与逆映射

被登记的记录用唯一专属成员R588_named_metadata_row指向[family,index]。原输入若任何位置已含该成员，本接口整域返回原值并明确applied=false；不会猜原字段是引用，也不会覆盖它。这个冲突处理是保留原元数据的fallback，不改变科学状态。

新引用只在上述固定族的合法位置形成。其完整行仍在同一必要对象的关系表中；没有仅保存外部路径或SHA，不依赖未来获取旧raw。相同来源的长路径、完整digest和未知字段都至少在一个完整原记录中存在。

对于source_literal_sha256，关系行是唯一列sha256的字典，逆映射在该族专门取出原字符串。它只替代具名literal_sha256_values中的元素；不将一般字符串或科学数字改成索引。

记录子项先处理，父项后登记。输入是实际解析JSON有限树，故新关系无环；共享相同已见记录也不会引入回边。逆函数仍显式检测active引用，防止损坏输入伪装成有限记录。

**命题588.B。** 对本模块成功形成的任一applied=true关系，restore_relation恢复传入的完整选定元数据；applied=false时返回本来就未修改的输入。

证明：先由命题588.A展开每个完整行。按原有限对象深度归纳，标量/未知原值保持；列表逐原顺序处理；字典未知字段按原成员序保持。每个生成引用按其完整关系行还原，子引用已满足归纳假设。固定literal SHA族再取回原字符串，恰好抵消唯一列的包装。保留成员冲突时未发生任何替换。无其他转换步骤，结论成立。证毕。

本命题不以SHA相等代替值相等。source map中的SHA只限制哪一原身份可以进入具名来源族；被登记记录的原file、bytes、sha256三个值全部仍保。

## 588.6　严格source identity条件

source_identity只接受实际字典且key集合恰为file、bytes、sha256；bytes必须是非负的Python int，bool不算int；file必须是字符串。其path只能逐字等于当前source basename或当前真实computations绝对目录加该basename，不能通过resolve猜另一个路径等价。

原sha256字符串须与调用者已核完整source map的该basename逐字相同。只有此时，完整原三字段进入verified_source_identity表。以下情形保原值：

- 缺字段、额外字段或bytes异常类型；
- 未登记basename、不同digest、其他目录；
- tmp输出、executable、科学array或日志等不属于该source map的身份；
- 仅有同名文件而真实路径不相符。

该函数不读文件，不能独立证明文件存在或实际bytes正确。实际source map、来源字节和receipt的形成仍由原已核caller负责。本件只是完整保留这个已返回的记录，没有另造实际观察值。

绝对和相对file字符串不同就保为不同记录；不同bytes或digest也不合并。完整source路径与字节值并未被一个不可逆basename替代。

## 588.7　五代完整binding与真实编译责任

R572的真实prepare_sources返回actual_R564_source_binding，后者依次含R561、R550、R535。这些是完整source-only ancestry，不是五次安装；实际owner仍是一次直接R572安装，随后原main真实g++。本件保这一原结构。

source_binding只识别五个已刊binding schema及各自installed schema。它沿四个明确actual_Rxxx_source_binding字段处理祖先；沿actual_headers、actual_original_sources、actual_generated_sources处理来源身份；沿actual_adapter/source_plan/actual_cpp_source及两个compiler function来源字段处理严格身份；run作为具名上下文完整保存。所有其他字段原样保留。

实际compile record通过dict(synthesis_binding,...)保相同binding schema，同时增加actual_compiler_command、generated include、compile返回码、executable、stdout/stderr、compiler_completed=true及来源责任。它与prepare的compiler_completed=false完整值不同，所以不会共享成同一完整记录。子祖先若相同可以共享，但这个差别和全部新增字段始终保留。

installed记录的actual_compile_not_yet_called也按原值保。任何来源表、安装表或prep success均不能推出g++已运行。完整原编译命令、返回码、include/executable/log的tmp身份不会因为source-only祖先相同而消失。

原persistent CPP、main、solve、replay、GNU选项、原300秒compile cap、同owned PGID及TERM/KILL/reap均不在本件修改范围。本件不执行其中任何动作。

## 588.8　完整既有来源表，不删除历史transport

原R573 readback会真实调用原R565 reader。原child若70，则保其transport70/false，核固定同job完整overflow文件的bytes/SHA，再读取全部正文。其内还含R562/R551/R547的原范围。新接口不得只读原小fallback后声称完整，也不得将原70改0。

本模块接收的是此时已经完整读取的原selected source对象。R551/R562/R565/R573的named source catalogue、ordered inventory、ordered literal change records分别保其完整schema、列、row、key order、inverse说明、实际已观察bytes、原field存在性及其他未知成员。只把严格相同的完整具名记录共用索引。

唯一额外跨这些catalogue共享的字符串列，是各自literal_sha256_values。其完整digest每个字符原样保留，原数组元素顺序保留。新共享不改变各旧table的原index意义；先展开本件得到原完整digest数组，随后原table的逆映射照原定义运行。

源中的错误、traceback、完整stderr、not_generated后缀、phase、原request/run/source、旧false与所有源地址均未被列白名单删去。本件不承诺这些不可共享部分很小，尤其多次不同错误文本仍必须完整占用原必要体积。

## 588.9　原RootStats的八个实际catalogue

R573的RootWordMetadata已有八个明确catalogue：

| 名称 | 本件处理 |
|---|---|
| root_statistics | 只处理下节四个实际成员，其他完整保 |
| root_finite_word_cache | 保原R535整个对象和原外层表 |
| owner_compilation | 完整具名记录及严格source identities |
| root_cache_compile_binding | 五代实际binding识别 |
| root_finite_word_cache_source_preparation | 同上；不造compile完成 |
| root_finite_word_cache_source_binding | 同上 |
| root_finite_word_cache_compiler_installation | 同上；installed责任保 |
| physical_source_input_binding | 完整具名来源记录；非source身份原样保 |

未来未知catalogue完整保为原值。每个原catalogue仍保其既有原索引序及R573引用语义；本件不重新编号原owner记录、evaluation、trial、stage或实际call。

真实接线位置应在RootWordMetadata.describe内，对self.values这份完整选定catalogue作处理，然后继续原root_word_table外层列结构。原self.originals、原share资格、原evaluation选择及所有科学值不改。完整逆序分三步：先按原root_word_table的columns/original_record_indices重建八个catalogue的当前行；再在这些行上调用restore_relation展开本件具名子关系；最后按R573原引用语义解释各catalogue。不能在外层列尚未重建时把列名字符串误当完整引用字典。这是真实接口责任，尚未由本组件自动安装。

## 588.10　四个统计成员、全部path与full last

直接从当前primal及四个已刊header的真实serializer取以下名称：

| RootStats成员 | schema族 | 实际paths |
|---|---|---|
| root_accepted_evaluation_reuse | R550 | primal、trace_variation |
| exact_dyadic_angular_average | R561 | root_residual、root_gram、primal_flux |
| exact_lifted_factor_product | R564 | root_residual、root_gram、primal_flux |
| exact_root_synthesis_products | R572 | fixed_fallback_P、fixed_fallback_Pt、L、evaluation_u_words、evaluation_u_fallback |

每个section须匹配其真实完整schema，才处理上述path。未匹配schema、未出现path、present null、其他原类型都保原值。对实际dict path，完整原key进入path关系；其last若为dict，完整未知key也进入last关系。last_present与last=null仍原样保，不由计数推填。

因此R550每路径13项、R561每路径10项、R564每路径17项以及R572五路径各17项均完整。代码没有用这些已知数量截断字典；未来未知计数或额外字段同样保留。原full last中的phase、angle、index、biased exponents、discarded bits、integer_rounding_formed、rounding_relation、rounded_up、carry及null状态不删、不合并成“最后成功”。

统计仅记录原实际执行工作。source生成成功不补统计；跳过工作不加虚拟计数；不由exact_normal多就宣称运行加速或owner接受。R564/R572快捷分支不执行原首个Q乘法这一历史事实也不被表表示改回“原每条Q指令相同”。

## 588.11　类型、非有限值和未知字段

same先要求Python类型完全一致。bool与int、int与float不同；有限浮点零还比较copysign，故0.0与-0.0不同。字典须有相同有序key元组并逐值相同，列表须长度及顺序相同。不会用1==True或普通dict集合相等代替完整资格。

nonfinite浮点不共享。ordered序列化要求allow_nan=false；若某完整记录不能如此表示，该记录直接保原值。模块不把NaN改null、无穷改有限数或补未知类型。既有reader的safe_selected仍独立负责其既有非有限标量展示；本件不抢先改变它，更不声称保NaN payload。

在已知record中，unknown key作为完整列存在。在未知RootStats/catalogue里，整个原值保持。输入已经含专属marker时整域不转换。上述fallback均不影响原科学退出码或已接受状态，最坏可能仍导致必要超限。

## 588.12　两原必要scope与90000/70

来源与科学必要本来就是两个独立原scope。本件不会把一个大的科学对象拆成多个body，也不把一个新catalogue放到另一个未来frame中来规避单体上限。每个采用的关系表须与它所表示的值放在同一原必要对象内。

下一真实入口可以在形成这同一完整selected对象后，比较“原表示”和“具名关系表示”的实际序列化长度，只在后者严格较小时采用。若不能变小，保原完整表示；这只是已选元数据的运输选择，不是新的数值门或独立科学测试。任一方案仍超过90000，必须沿原分支记录完整同job身份、返回70、necessary_readback_complete=false并禁止相应cleanup。

关系有固定表头成本，所以单个或毫无重复的记录可能变大。本文不预测actual240/246最终大小，不从R552/R555未返对象猜各字段比例，也不保证下一次fit。只要真实完整body返回，才可报告其字节数和各项实际科学状态。

## 588.13　原clock、quiet、错误和清理不变

科学必要仍在原runtime.bind及真实quiet之后读取各实际目录；quiet未知不读取科学原件。新metadata共享在原同job读回/清理余额内运行，不重开clock、不追加科学时间、不重跑owner或RHS、不从另一个run借数据。

R573的原source stderr、科学original_errors、metadata_read_errors、全部actual_file_receipts、unstarted/unreturned范围、各原reader returncode、outer/rules/science exit、external/resource字段必须继续全部保留。模块没有selector白名单删除这些顶层数据。普通表示错误应完整返回原readback异常并保持不完整，不能用空表冒成功。

清理仍由原所有必要complete、各真实owned quiet以及原marker决定。applied=true、关系表可逆或长度更小不等于necessary_readback_complete，更不等于science accepted。actual233/232的removed=false不会被本件追认成删除成功；旧raw不会重新保存为Git、Release或artifact。

## 588.14　组件完成与后续入口

本件已完成：薄元数据源、严格类型/顺序资格、完整列表示、专属冲突fallback、有限逆程序、实际五代binding与四类统计serializer的对应，以及两原scope/90000/quiet责任说明。逆命题对该有限程序逐构造成立，不要求先作额外fixture或科学对拍才可发表。

尚未完成：R589/request246的真正新调用者、完整source-plan/CLI/normal及recovery接线、正式发布和唯一派发、实际来源/科学必要回传、原owner/replay/model/FD/fullDN结果。旧240及其他在跑run保持其冻结来源；没有把本件注入它们。

完整非零112/338/450仍未接受。同一g、完整闭C²族、全t reach/relative metric、固定H/整像held/含反射δE、完整D和固定目标的实际refinement仍须由原课题链支付。本元数据结论不缩减其中任何数学条件，也不是课题完成的替代。
