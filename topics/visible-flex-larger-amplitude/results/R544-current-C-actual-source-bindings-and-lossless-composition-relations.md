# R544：实际 native 与闭面来源接线，以及完整 composition 的具名无损关系

作者：OpenAI / ChatGPT exact_refinement agent（AI）  
日期：2026-11-16  
性质：冻结源码上的条件实现结论；未执行新的科学计算，未宣称 request230 已运行。

## 544.1 本文支付的责任

本结论针对 [R490](R490-actual217-complete-shallow-sampling-and-source-binding-stops.md) 已记录的三个工程缺口：首轮 BVP 已实际启动，但启动器传入的 tail-client 路径与当前 driver 的明确来源不同；独立闭面入口自报的 `ENTRY` 与其实际生成文件名不同；完整 composition 的原必要读回超过单份 90,000 B。

前两项修复真实调用与自报来源，保留原来源 guard。第三项只整理完整元数据中反复出现的“向 `source_sha256` 添加一个来源”这一已具名关系。它保留原对象全部字段、键存在性、值类型、成员次序和原 change 行次序，不改科学选择，不拆分一个正文，不提高 90,000 B。

实现由两个小 Python 模块和一个显式字面源码计划组成。计划完整登记 41 个受来源变更影响的当前组件，以及 8 个同 C 消费者，共 49 个新实际源码视图。旧 8 个 request217 视图先按冻结计划重建为祖先，因此这一新生成步骤在现场最多形成 57 个来源文件。各文件均有完整 baseline、字面出现次数及输出 bytes/SHA。生成器不导入科学模块，不求场、不做 numerical fixture。

本包是后继 R545 / request230 的可调用来源和读回实现。实际 outer request、工作流、marker 以及原清理链的最终调用由 R545 接线；本结论不会把“已有函数”写成“新科学链已执行”。实际结果号 R546 只留给真正运行后的记录。

## 544.2 两个来源错误的准确位置

### 544.2.1 首轮 native owner 路径

actual217 的首 driver 是：

- `geometry_20261116_actual202_coast_base_zero_linear_gzip_ten_full453_frozen450.py`，34,462 B，SHA-256 `b754fc536d00e90e8e18ecb1f160bb01f635b0ba2b77b2f685a942b7df942d6c`；
- 其 `CLIENT_NAME` 指向 `geometry_20261116_current_C_zero_linear_gzip_joint_tail_client.py`；
- 该实际 client 为 23,360 B，SHA-256 `3870315a04182550272001150d4faf0b2511846a31643a592df2af54f85cfbdb`；
- 对应 legacy driver 为 65,419 B，SHA-256 `bf5e988d5bc40e3777533bc2e3abfc137b3609333fff9c923df55a0a76f0ad17`，其完整 pin 与上述 client 相符。

原 guard 同时要求命令行 client 的真实路径等于 `HERE/CLIENT_NAME`，并要求实际文件 SHA 等于 legacy 中该名字的 pin。这个 guard 合法，也没有因本结论而放宽。

实际 launcher 为 20,522 B，SHA-256 `b3ce2f2ae7b018236d5a20e1d3177d1cfc337dc698e2939539a560e474bba08f`。其 argv 仍把 `--tail-client` 指向 `geometry_20261115_current_C_pruefer_joint_tail_client.py`。这与上述当前 driver 合同不一致，足以解释已经返回的来源拒绝；不需要猜测未返回的 native 数值或旧 config 正文。

新 launcher 仅在该实际 argv 接点替换为当前 client 名称，成为：

`geometry_20261116_actual202_bound230_coast_base_zero_linear_gzip_ten_full453_frozen450_launch.py`，20,531 B，SHA-256 `d8dc4e9158610d72246b5865c0f9970e66ba6a9777b01b8e1e53b176c674f277`。

原 driver、原 current client、原 legacy driver 的数学正文和上述 guard 均保留。依赖 launcher 完整身份的 reader、父来源注册和后继来源链必须分别声明新实际身份，不能只把旧 basename 改称“新 owner”。

### 544.2.2 闭面独立入口的自报文件名

actual217 的闭面入口实际文件为：

`geometry_20261116_request220_actual202_coast_base_zero_linear_gzip_coast_closed_postsolve.py`，47,489 B，SHA-256 `9c7af17273844fc221aeb923ada60b194f5a64bab4cb87d8bb2ff0bf11942b62`。

但该源码的 `ENTRY` 字面仍为 `geometry_20261116_request220_actual202_zero_linear_gzip_coast_closed_postsolve.py`，缺少实际文件名中的 `coast_base` 组成。原 `bind_request` 读取 `postsolve.orchestrator`，要求其文件名等于 `ENTRY` 或 topic 下该计算文件，并核自身完整 bytes/SHA。因此即使来源记录保留了真实文件身份，错误的自报文件名仍会拒绝实际入口。

新文件明确命名为：

`geometry_20261116_request230_actual202_bound_coast_closed_postsolve.py`，47,491 B，SHA-256 `332fd828093ec663a4484359f7560e8d207cac7b648ea41e0608f6bb9dff6a1d`。

其 `ENTRY` 与真实新文件名一致；自身 schema、frame 和 readback marker 明确采用 request230 身份。原文件/bytes/SHA 校验、全部 postsolve 子角色、原科学条件和清理责任保留。

上述定位来自实际217冻结源码的逐字重建及完整身份，而不是仅按异常文字分类。actual222 的独立终态来源核对也报告了相同的 b3ce launcher、b754 driver、387 client 和 9c7a 入口；其运行数值、日志、停止时间仍由对应 R511 独立记录。本结论不把两个运行合并成一个实际轨迹。

## 544.3 为什么必须传递到完整来源链

依赖方有的检查 launcher 的 SHA，有的检查 worker、sampler、checkpoint 或 SavedPrefix 的完整身份；几何消费者还通过 source tuple 绑定其 parent。一个上游来源名改变后，只有替换一行启动器不足以形成可调用的后继链。

本计划对这些真实依赖作拓扑级联。分组如下：

| 来源角色 | 新视图数 | 具体责任 |
| --- | ---: | --- |
| 首轮 launcher、必要 reader、构造 policy、postsolve/reader/held、独立 closed 入口 | 7 | 当前 client argv、真实父 launcher 与闭面入口自身份 |
| 同 far 的 worker、client、sampler、driver、owner、必要 reader、postsolve/reader/held | 9 | 保原完整112 far复用及新网格、真实 native 和全450求解 |
| union-M 的 worker、client、sampler、checkpoint、driver、owner、phase reader、必要 reader | 8 | 原112与新增模态的真实来源及新M父、状态、全部返回责任 |
| union-M Saved/radial/prefix/shared/cut/atlas/caps/material/reach/metric/held，以及 evidence/display/postsolve链 | 17 | 当前完整M场到闭面和所有原消费者的实际来源 |
| 同 C 的 head、leaf、bridge、tail、三层 metric、evidence | 8 | 原R489/R492/R495/R500/R504同C语义与新实际来源共存 |
| 合计 | 49 | 每个视图均有独立实际名称和完整输出身份 |

41 个核心视图保留原科学 API 的语义 schema，来源变化由新文件名及完整身份明示；不能据仍兼容的 API schema 声称旧源码被执行。8 个同 C 视图另将独立 request217 schema/frame 显式变为 request230。closed 入口也有独立新 schema/frame。

计划只包含 95 个不同的透明字面替换定义。每个视图列出其实际使用的替换、严格出现次数、完整 baseline 与完整 output。涉及数值型 `bytes` 的更改仅是五处实际 source descriptor：两个 worker descriptor 和 closed `SOURCE_ROLES` 中三个实际来源大小；不是科学参数或数值预算。

输出源总计 1,972,880 B，只在公开 Actions 的真实 computations 目录形成，不作为重复展开文件加入 Git。两个小模块、计划和本文/接口才是本次发表项。原所有祖先源码保留，原生成文件不覆盖；不能把这一源码文字生成当成科学 raw 数据归档。

## 544.4 来源修复的条件结论

**命题 1。** 假定所有原公开 baseline、前六层原生成来源、原 request217 计划和本次计划均按完整 bytes/SHA 绑定，且 49 个实际新文件按计划在同一真实 HERE 生成。后继 caller 使用本计划的新 launcher 与新 closed 入口，并在各原 source tuple 中声明对应新实际身份，则 §544.2 的两处特定路径/自报名不一致被消除；各原来源 guard 的条件本身未放宽。

证明。首 launcher 的唯一实际 argv 替换把路径从旧 client 改为未改 driver 的 `CLIENT_NAME`，两者指向同一真实 computations 目录中的原当前 client。其完整 SHA 仍由原 legacy pin 检查。closed 文件的新 `ENTRY` 等于其真实独立文件名，来源对象的 bytes/SHA 则绑定该实际新文件。其余来源依赖按有向引用逐一替换为已明确生成的子文件名、完整 hash，必要 bytes 同步。字面计数和完整输出身份保证使用的是所声明的整个源码，而非只有一段看似相同的文字。证毕。

此命题不声称原 solver 能接受任何步，不声称完整 native/FD/fullDN、450、geometry、reach、held 或 metric 已完成，也不把源绑定成功当成数值证明。原 source guard 之外的实际失败仍必须原样返回。

本次不是 binary64 运行轨迹相同的证明。恢复正确 callee 后，先前未到达的科学代码将首次执行，且新准备工作会消耗同一原绝对时间。只有数学正文、原目标定义、原阈值与资源合同保持；不预填将来的接受步、运行时间或结果。

## 544.5 composition 的原对象与所选关系

R490 返还的 93,236 B 是完整 composition 文件的身份，不是已经回传的必要 frame 正文的独立长度。原 producer 在将完整对象 canonical 化后检查单份长度并失败，故本结论不把缺少正文的历史对象补成一个实际测量样本。

本次选择器只认识原 `changes` 产生的以下完整四键行：

1. `path` 为 `/source_sha256/` 后接一个明确 ASCII source basename；
2. `before_present is False`；
3. `after_present is True`；
4. `after` 为完整 64 字符小写 SHA-256。

basename 只接受 `[A-Za-z0-9_.-]+`，排除空名、`.`、`..`、斜杠及 JSON-pointer 转义。任何额外键、不同值类型、不是新增的变更、特殊名字、不同四键次序的行，均完整留在 literal 行序列。此处不存在对任意 scientific JSON 的通用字典编码。

被识别的行改写为明确三列：

| 列 | 含义 |
| --- | --- |
| `original_change_index` | 该行在原完整 change 列表的零基地址 |
| `source_basename` | 完整原 source 名称 |
| `after_sha256` | 完整原64字符SHA |

共享关系头明确 `source_dictionary='source_sha256'`、完整四键原次序、三列角色名及原总行数。其他原变更按原相对顺序保存在 `other_changes_in_original_order`。根对象除 `exact_member_changes` 外全部 deepcopy 保留，根成员原次序另明示。没有删除任何旧 pin、历史身份、原错误、条件声明、实际子结果或未完成范围。

## 544.6 无损性与完整行序

**命题 2。** 对 `compose` 接受的任一可 canonical JSON 原对象 $D$，其返回值 $C(D)$ 满足 `expand(C(D))` 等于 $D$ 的完整语义对象；同时保留原根键存在性和成员顺序、每个 source addition 的四键顺序，以及全部 change 行的顺序。这里没有把整数与浮点、负零与正零、空值与缺键互换。

证明分两种情形。若输入不是所识别结构，未找到合法 source addition，或候选完整正文不严格缩短，`compose` 返回原对象 deepcopy，`expand` 对该普通对象同样返回 deepcopy，结论直接成立。

否则，记原 change 行数为 $n$，被替换的行地址集合为 $I$。每个三列行保留唯一原地址 $i\in I$、完整 source 名和完整 SHA。逆映射在这些地址恢复 `path` 的固定前缀、原 false/true 布尔值与完整 SHA，并按记录的原四键次序构造字典。其余地址按递增次序从 literal 队列取下一整行。原扫描本来按地址递增遍历，因此 literal 队列正好覆盖 $[0,n)\setminus I$，没有跨 context 分组、排序或去重。恢复列表逐地址等于原列表。

根其余成员从完整 deepcopy 取得，按 `original_member_order` 逐一复位；被抽出的 change 成员插回其原位置。其余嵌套对象没有变换，所以其原字段、类型和次序也被保留。全部数值均不参加数值求值或字符串再解释，负零、null、缺键、原 error 字符串及未识别对象沿原 JSON/Python 对象语义保存。证毕。

`expand` 还按固定格式检查关系结构、地址唯一递增、总行数、完整成员集和恢复后 canonical identity。这个显式逆说明数据含义，供需要读取关系的消费者使用；科学 caller 不通过新增逆展开对拍来决定数值是否接受。原 source bytes/SHA 条件仍是原来源条件，并未增设 numerical gate。

canonical 采用 UTF-8、`ensure_ascii=False`、排序键、无空白紧凑分隔、`allow_nan=False`，末尾一个 LF。本文的精确还原对象不声称恢复历史文件任意缩进、CRLF 或序列化前不存在于 JSON 语义中的对象身份。原完整文件另保其真实文件 bytes/SHA。

## 544.7 可证明的大小改进与原90K边界

**命题 3。** 对同一原完整 canonical 对象 $D$，`compose` 所选单份正文的字节数不大于 $D$ 的 canonical 正文字节数；选用关系形式时严格较小。

证明。实现先形成原完整 canonical bytes，再形成含全部关系头、原根键次序、完整其余对象、全部 literal 行、全部新增源三列和原 canonical identity 的候选。只有候选总长度严格小于原总长度才返回候选；否则返回原对象。比较对象是完整正文，而不是某一局部表。证毕。

对于源码允许的 ASCII source basename，设名字长为 $L$、原 change 地址 $i$ 的十进制位数为 $d(i)$。独立 canonical 行不计外层列表逗号时，原四键行长为 $145+L$，三列行长为 $72+L+d(i)$；每行减少 $73-d(i)$ 字节。完整 shared header、原顺序及 identity 的开销已由上述全正文比较计入。因此这是一个具体具名重复的消除，不是预测某个未知历史大对象必会压到90K。

即使候选严格缩短，仍可能超过90,000 B。后继 caller 必须继续对**实际选中完整 bytes**检查原上限；超限明确未完整读回，不能分包、截断、去字段、提升限额或以 hash 重建大正文。`breakdown` 只给实际选中完整正文 identity，以及 source additions、literal changes、其余完整对象等具名部分的实际 canonical 字节数，不提供可重组任意 JSON 的编码。

原完整 composition 在 Actions 内原样保留，仍可用于原 `verify_runtime` 与同现场来源校验。必要关系正文的身份与原完整文件身份应各自登记；两者不能伪称相同。

## 544.8 真正生成顺序与原时钟

新 `root_20261116_current_C_bound_source_views.py` 接受四个显式 CLI 参数：

- `--computations`：当前 checkout 或已明确 metadata 工作视图的真实 computations；
- `--plan`、`--plan-sha256`：本次完整计划及实际完整 SHA；
- `--out`：原 namespace 下一个新鲜直接子目录。

它要求真实 GitHub Actions、原仓库、实际 run/source。`HERE` 必须等于所传 computations；计划和全部源码按真实普通文件读取，完整 identity 核对。输出名字必须新鲜，原文件不能覆盖。

原前六层来源已经形成后，生成器先从冻结 request217 完整计划重建8个历史消费者。每个 baseline、每项字面出现次数、每个中间及最终输出的完整 bytes/SHA 均登记。原 Actions-only 源码语法处理保留；本次文本实现阶段没有运行 import、AST、compile 或科学求值。

随后直接调用未改的 R496 元数据字面引擎，在同一 HERE 形成49个当前视图。该引擎本身的完整来源是11,895 B、SHA-256 `4d4c507edd571b67655fd2e66fb4bcfa173b1239928443831a81a925c4869ec4`。JSON policy/plan 不混入其 Python/JavaScript source-only 列表；本计划该列表只额外声明新的元数据 formatter。

完整生成结果记录历史8与当前49的每个实际文件、当前 engine 退出及完整 stdout/stderr 身份、未写历史角色、未确认当前角色、实际 exception 和当前 source view 地址。若未完成，不能只报“49个预期输出”代替真实已形成文件，也不能把下游科学标为已启动。

原 clock 文件必须仍是实际 job/source 的 `request205-owned-job-science-deadline-v1`，科学期自 namespace 起18,900秒，必要读回预留2,700秒。本生成器只读该原钟，并将准备工作纳入原绝对期限；不建立第二个起点，不给后继每阶段重开全额预算。完成时还核原 clock 字节未变。

## 544.9 后继实际caller的接口责任

R545 需要把本实现接到真实新 request230，至少保持以下关系：

1. 公开小 request 保留原全部输入、原科学参数和所有祖先来源，明确本次 helper、generator、完整计划及其49输出；同C的历史8也显式登记。
2. 所有原层先按真实生成顺序完成，之后实际调用本生成器；后续 argv、`postsolve.orchestrator`、原 source role map 和必要 reader 均引用新实际文件，不能只替换日志标签。
3. 旧220/205名字若仍作为内部 ancestry/API路径，必须明确其历史语义。实际 run/source、当前 derived request、工作视图、字节身份和outer230号分别记录，不能把旧运行或未返回旧 derived205 全文冒充现场父件。
4. composition 仍完整生成、现场校验；读回只对这一个完整对象调用 `compose`，不重新选择科学字段。单份90K检查针对实际返回bytes。
5. compact necessary marker 同时绑定实际必要正文和原完整 composition 文件两份身份。原 marker 中二者曾相同的写法必须在新 caller/reader/cleanup 中明确分开，不能只改输出却沿用旧同一身份假设。
6. 全部原必要 scopes、source preparation、同C八角色、PID/start-time/pgid/session及真实quiet条件保留。任何必要读回未完、来源不明或真实own未静止，均不得清理raw。
7. 科学partial可以有完整必要读回；来源、读回或清理成功也不能代替 full453、450、FD/native、metric/reach/held 任一原科学结论。

以上是本模块的真实消费者合同，不是新增科学接受标准。R545 的完整差异和接口将给出实际文件及调用位置；本结论不提前声明该接线已执行。

## 544.10 发表边界与可信度

本次三个运行来源的完整身份为：

| 文件 | bytes | SHA-256 |
| --- | ---: | --- |
| `root_20261116_complete_source_composition_relations.py` | 8567 | `7bc351fe46ce6c8bf94ba067b106a0a21bd89950277910fe46006c502815b163` |
| `root_20261116_current_C_bound_source_views.py` | 16140 | `78ac0c9624beaa1ea2dd660f761b8c49ef56c49794d3928233625d86faff5104` |
| `r544-current-C-actual-binding-source-plan.json` | 76039 | `10002d1bacbf88792750884537ae16b0c1993049be8bb2306502339032a98a2b` |

完整计划是每个生成来源的精确映射，不依赖本表缩写或猜测。接口为 [R544 实际来源与完整 composition 关系接口](../notes/2026-11-16-current-C-actual-source-binding-and-composition-relations-interface.md)。

可信度来自原实际错误记录、已固定源码的字面控制流、完整来源映射和上述有限对象的条件证明。没有科学运行、数值对拍、性能测量、重复域审计或新验收fixture。它支付两条实际来源接点和一种完整必要元数据表示；原准确C、十词、同g/材料条件、全部全域证明、native/FD/fullDN、mesh/M/t及原资源未完成责任均按各自真实运行继续承担。
