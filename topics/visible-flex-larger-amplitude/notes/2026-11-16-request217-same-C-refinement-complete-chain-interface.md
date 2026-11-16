# Request217：同现场完整 C 重算与三个真实场的全域误差续链

作者：ChatGPT（AI）；geometry agent提供源接线初稿，exact_refinement整理完整调用与必要读回接口  
日期：2026-11-16  
状态：**条件接线与源码；尚无本请求的实际场、运行或数值结论。**

本入口把已发表 R489 的完整头部重算、R492 的同语义叶求值、R495 的实际场族适配、R500 的全尾 E 查询和 R504 的完整 metric / evidence 消费者，接到一个真正同 job 的完整 BVP 与几何链上。首场和两个后继场均须由各自原求解器真实返回；没有以 SHA、原种子或尚未完成的阶段补造 checkpoint。

运行底座是冻结220祖先合同及 request222 的明确 source-only JSON 工程修复。冻结220的全部原科学角色、原457来源、深度2完整物理点采样、原 full453→frozen450、五个精化因子、M128旧112加新模态 union、五几何、held、公共材料证据和临时显示责任保留。220首跑的 source-only 列表错误不作为任何数学反证；实际217必须先应用独立修复合同，再调用原完整角色。该工程修复来源的最终身份在交付清单与 request 中明示，不将原220失败任务当作已有科学输入。原220的 f6ca 请求只是祖先；实际 H4afc.bind_request 接受临时工作视图中的真实 derived220 路径和新SHA，随后 namespace 内 refinement220-request.json 与它逐字相同。新的66182B/7a74a8e6 source plan只把 R503 policy JSON排除出仅收 Python源的子生成器列表；该policy仍在外层完整pin中，字节和科学消费不变。旧plan保留历史pin、新plan另列，因此修复底座为279公开+179生成=458来源；本217另加7公开+8真实生成，组合表为473项，实际JSON并集已核无名称碰撞。222entry、两个请求/工作流、生成计划和其它元数据仍按各自完整descriptor另行绑定；这个计数不代替未声明导入路径的逐项来源责任。

本文件解释新增角色的实际调用、条件正确性和未付范围。它不另立 BVP 接受条件；没有新增 fixture、独立重跑、全338解析列或全局 C² 收敛前门。

## 1. 同一个准确对象与不同包围对象

保留原实际 C 的配置、校准账、stored reference、查询配方、证明和恢复源码来源；保留同一原 cut 的二进制字以及所有原许可 root 序列。原完整源是 f12f 的160×9有序头部和六个 primitive，深端仍是原完整根族；新调用不能把已完成的原数值输出改名为某个新的准确 C。

R489 的新计算采用另一组显式积分/查询工作参数，实际重新生成全部1440源片、六 primitive、累计径向端点和原查询计划。其 complete 或 partial 结果、各实际账本、cut 二阶完整读回和未完成范围都有新的身份。新工作参数是计算资源与包围精度参数，不能把尚未达成的 value-width 目标改成数学失败。

对每个相同语义的准确值 $x$，若旧、新正确包围分别为 $I_0$ 与 $I_1$，则

$$
x\in I_0\cap I_1.
$$

这里的量词对原允许的每条 root 序列成立。相交没有选取某个盒中点，也没有声称任意独立分量盒点都能由同一 root 序列共同实现。若实际两包围不相交，当前 consumer 报告来源/包围不一致；不能据此宣布原 C 族为空。

对每个被选择的真实层级分别而言，原 CP、accurate definition、所有状态节点字、该层 R249 定义数据和当前材料映射均保持原实际对象；同C包围重算不修改它们。不同层由各自原求解器真实重求，允许场本身和当前材料图改变；只有原共目标签名要求的准确C/十词及首次W/H/marker和材料/构造来源按原共同图合同保持。R492 与新登记视图只提供这些同一表达式的另一个向外求值方式。原 descriptor 仍属于原文件；新 provider / 新 enclosure receipt 分开保留。

新的求值方式若在某个闭域单元证明了原来未决的radius/speed或度量不等式，那是本次consumer的实际结果；它不改写旧factory的初点域记录，不回填某个未返回的native或旧parent接受，也不以新metric作为原BVP前门。

因此，**仅重算 C 的包围不会改变同一准确场的真实等距误差上确界**。同场旧、新上界之差最多表示已证明包围的改善。不同实际精化层的误差比较仍须消费各自真实场和同一个准确目标；不能把“较紧的包围”冒充“场的误差已经严格下降”。

## 2. 真实来源组合

新增 source plan 有八个实际输出，全部写入真实 computations/HERE 的新 basename。旧文件不覆盖，不通过运行时 monkey-patch 修改旧类或模块全局。

| 新角色 | 真实原数学正文 | 本次确切来源修改 |
|---|---|---|
| head | R489 完整头部与 cut 重算 | 登记实际220首 driver / launcher / deadline，独立 schema 和必要 frame |
| leaf | R492 同语义 E0/E1/E2 与准确 cut 求值 | 绑定本次真实 head 源与 schema |
| bridge | R495 实际场族适配 | 绑定本次 leaf，明确实际220增模态 Cut / Prefix 来源 |
| tail | R500 完整 E(r) 查询桥 | 绑定本次 head / leaf，原 old/new 完整域与 live refine 算法保留 |
| metric0 | R495→R504 原112 live完整 metric | 使用本次 bridge / tail；原四 Loewner、闭 DFS 和全覆盖不变 |
| metric1 | R495→R504 分辨率112 live完整 metric | 同上，实际 CP 属于原真实五因子精化 |
| metric2 | R495→R504 增模态 live完整 metric | 同上，并登记实际220 M 的 Cut / Prefix / Cuff / Cap |
| evidence | R495→R504 全域 operator-norm 与系列比较 | 三层使用同一新必要 schema，实际220材料来源；原测量、全t证明和比较不变 |

生成器逐个核完整 baseline 的 bytes/SHA，按完整 literal replacement/count 顺序形成每个中间文本，再核每个中间与最终 bytes/SHA。三个 metric 和 evidence 的 R495、R504 中间文本只在内存中按真实完整身份核定，不需要另写无关的旧输出文件。所有八个最终目标在任何写入之前必须不存在；实际写入采用独占新文件，不能覆盖祖先。

原220的179个生成源先通过 request222明确修复后的真实源物化路径生成并绑定；四个原outer及全部46个最后源view保持祖先字节，旧有层次/剩余祖先view保留实际来源。此后才允许读取其中作为本次baseline的原R464文本。不能在生成前校验一个尚不存在的视图，更不能把计划中的身份当作已产生的文件。

额外静态运行来源为七个公开 Python 文件：四个已发表的 baseline 加本次 runner、reader、composition。加上八个新实际生成文件，与修复底座458个不重复来源构成473项实际运行源；source plan 是另行完整绑定的元数据输入。这里的473严格指当前组合表的458+15项；不声称只凭这个数已证明任意传递导入闭包。实际source-set相等检查仍在Actions中执行，源码阶段不预填其实际通过。

## 3. 两个实际调用时机

第一个 slot 在原首次完整 closed/shared 角色及其必要读回之后，原220联合精化角色之前。它读取实际 BVP-launch、实际 driver adapter-status、真实 accepted frozen450 CP，以及首场真实 shared result 和原 cuff atlas。若这些对象不存在或原 accepted/quiet 条件未返回，新增角色只写准确的 not-started 范围。

有真实首场时，新 head 角色最多启动一次。它不修改旧 C 结果；原 C 与新 C 同时保留。完整 cut 叶、同语义比较及进程退出/quiet 实际齐备后，允许新增 metric0 与 measure0。新 head 的全部旧/new查询未必都完成；合法的完整旧粗界继续被 consumer 使用，不新增“新 query complete 才可开始”的门。

随后原220继续它原来的真五因子112重求和 M128 union 重求，保原 H、完整响应/J、FD、fullDN、最终审计、几何、held、原证据与显示流程。新增 metric/evidence 的 pass、fail、区间重叠、异常或预算停止均不能取代这些角色的原接受公式。

第二个 slot 只在原220联合角色实际返回后读取其已产生的 level1/level2。每个层级仍须沿实际 owner→完整 driver→实际 CP 绑定。它不能从初猜、未接受点、元数据摘要或只有 SHA 的缺失文件构造场。若首 slot 没有启动 head、但此时有实际完整场且还有原钟余额，可启动原声明的一次 head；已经真正启动过的 head 不会暗中重试。

每个新 metric/measurement 最多一次。measurements 按真实层号排列后，只有至少两个实际返回结果才调用原 compare。区间不可比较、输入范围不齐或包围重叠都作为原结果记录；不会以 $U_{\mathrm{new}}<L_{\mathrm{old}}$ 为新的求解接受门。

## 4. 全域与全t责任

每次新 metric 都使用原当前场的完整 root plan 和闭 DFS，保全部 prefix、tail、cut patch、collar、两反射片、上下帽、边界与 seam。不得拿 cut 三盒扩展成整个尾域，不得凭 completed/work-resolution 标签替代 whole-query 闭域证明。

R500 先绑定该场原定义中的完整旧 C result 和输入身份，再绑定真实新 head/query 结果。对实际查询区间，旧、新都完整时取合法相交；只有一方完整时保其完整界；多个合法闭 query 区间只按完整并集覆盖取 hull；有未覆盖间隙时仍未付。原有效粗界不因新查询资源停止被删除。

新 live path 的源片与累计端点来自真实重新积分的完整头部。它不是仅把旧累计盒再次切分。原输入根族的不确定宽度和其它无法靠工作精度消除的信息宽度仍保留，不承诺任意细分终止或最终上界必然下降。

这里新接的全尾查询只涉及 E 的值。cut 的 E/E_r/E_rr 及准确 patch 六jet来自实际 R492。**没有新增或冒称全尾 E_r/E_rr 查询已经接入。** 原完整场 F 的节点定义及它与某个真实 ODE 连续轨迹的误差责任仍按原 R409/R416/R459 分责。

measure 使用真实首材料 B、首 plan 和 assembly，核同准确闭目标的完整签名。各层当前材料图到首图的映射方向仍是原定理的 $\Theta_j^{-1}\circ\Theta_0$；不能仅以十词或 W/H/markers 相等声称同 g。帽使用原 Cartesian 图，seam 与材料 gluing 条件仍为原完整 consumer 责任。

全t相对 operator error 的转移沿原共同材料共轭与同时拉回 $(E,G)$ 的可逆同余，结合整个角圈覆盖与固定帽。它不是宣称固定 g 在任意 q 平移下旋转对称。实际 t 查询仍按原嵌套计划4、8、16运行；有限点查询不替代全t命题。

## 5. 原钟和本次资源选择

唯一 namespace、初始时间及18900秒科学计划、2700秒读回预留来自真正原 job。科学来源严格取 BVP-launch 实际绑定的 actual_job_deadline；缺失时不能用一份自造截止时间启动科学。

| 新责任 | 显式计划 |
|---|---:|
| 完整新 head + cut +自身关闭 | 1800秒 |
| 其中原 f12f head 工作 cap | 1650秒 |
| 原完整 cut 读回预留 | 120秒 |
| 子进程关闭预留 | 30秒 |
| 每个完整 metric | 240秒 |
| 每个全域 operator measurement | 300秒 |
| 系列 compare | 120秒 |
| 每个必要 metadata reader | 至多300秒，裁同一原读回截止时间 |
| 暂存盘 free reserve | 2147483648 bytes |
| 后继开始前的终测/关闭计划预留 | 900秒 |

新 head 工作参数为 precision384、积分 absolute128/relative112、analytic guard8、evaluation limit100000、value-width32、原 max_depth48、query_depth16、max_panels400000、max_query_nodes400000。每个均是实际新声明的工作参数，原 f12f CLI 自己检查原合法域。它们不是一个已经完成的精度证书。

原 query 工作选择、metric eta 与完整参数从冻结底座的实际 work_choices 读取。新增 measurement 继续原 interval256/sqrt128/全覆盖计划；t点仍原4、8、16与原四公共材料见证。这里不另造一个 epsilon 来把原 native/RMS 容差改称 relative-metric floor。

全部 cap 在真正启动时裁原剩余科学秒数。head/metric 仍保900计划预留，measurement/compare可使用终测余额但仍保原关闭时间。声明上限之和不是完成保证。旧前置阶段的原计时边界不由本入口追认成一个此前不存在的总绝对杀钟；新增 owned 子程实际按原已绑定绝对截止时间停止。

每个新科学调用使用原4afc OwnedTree，独立 session、实际PID/start_ticks、实际子孙观察、TERM→KILL、wait/reap 与最终 quiet。R489自身的两子程也保原5bb OwnedChild；新外层只把其实际 phases/producer_process 中的进程字段投影到旧 OwnedTree 可读的 stages/leader 形状，保原结果身份，不复制或改写科学状态。

原 rules runner 仍是真实公共 pull/check 过程；两个新规则目录各自有 parent/run/return 身份。父 Python 可能处在 runner 公共组，因此父只按 PID/start_ticks 检查；不能把仍活的公共 runner 组误称为未停止的科学组。

## 6. CLI 与实际输入

所有路径均取真实工作视图 computations/HERE、原 namespace 和相同 GITHUB_RUN_ID / GITHUB_SHA。入口 CLI 在 Actions 中调用；文中命令只是接口，不是已执行记录。`OUTER`与`OUTER_SHA`表示末表所列真实217请求路径与完整SHA。

| 路径参数 | workflow实际来源 |
|---|---|
| `--base` | `$VISIBLE_BASE`，原205 namespace，起点不重开 |
| `--computations` | `$VISIBLE_COMPUTATIONS`，222工作视图内topic/computations，与实际脚本HERE一致 |
| `--source-topic` | `$VISIBLE_SOURCE_TOPIC`，原恢复步骤写入GITHUB_ENV、位于原BASE的公开数学源码目录；它不是工作视图的topic目录 |
| `--proof-directory` | `$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/results`，GITHUB_WORKSPACE经222环境文件明确指向工作视图 |

每个实际slot先加载同一222环境文件。下列请求参数和路径不能用一个存在于别处的同名文件替代。

标准库 composition：

- bind：读完整冻结底座、实际工程修复合同、本次 request、plan 和已存在原 namespace clock。
- preflight：执行原冻结完整 metadata/AST/recipe 绑定块；仅将它检查的 workflow 路径明确改成本次真实工作流。原代码块和改前/改后身份单列。
- prepare：原底座所有真实源齐备后，生成并绑定八个新名，Actions 内做原性质的源码语法检查。
- readback：返回独立 source composition 必要对象。
- cleanup：先绑定本次必要marker/quiet，再委托实际222entry.cleanup；222entry保其修复读回/工作视图身份与原清理参数，最后调用原220 reader的九scope/quiet清理。不能越过中间层直接删raw。

新 runner：

~~~text
python -u "$VISIBLE_COMPUTATIONS/geometry_20261116_request217_same_C_refinement.py" rules \
  --phase first \
  --request "$OUTER" --request-sha256 "$OUTER_SHA" \
  --base "$VISIBLE_BASE" --computations "$VISIBLE_COMPUTATIONS" \
  --source-topic "$VISIBLE_SOURCE_TOPIC" \
  --proof-directory "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/results"
~~~

第二次仅把 phase 改为 successors。rules调用同源run并建立真正独占科学session；不能绕过原rules用裸 subprocess.run 启动长科学过程。

新 reader：

~~~text
python -u "$VISIBLE_COMPUTATIONS/root_20261116_request217_same_C_necessary.py" \
  --request "$OUTER" --request-sha256 "$OUTER_SHA" \
  --base "$VISIBLE_BASE" --computations "$VISIBLE_COMPUTATIONS" \
  --prepare-outcome "$PREPARE_OUTCOME" \
  --first-outcome "$FIRST_OUTCOME" --successors-outcome "$SUCCESSORS_OUTCOME"
~~~

原220祖先 request、222修复后真实执行的 derived220 request、repair receipt、本次217 outer request及实际 source generation receipt 分开存放。原220checkout不改；新metadata/source工作视图有自身真实路径与身份，不能把derived请求新字节回标为旧f6ca。修复后的derived220原件为99330 B / 2d1c3a7d56093f0009367bce0e201af14692b51541b759aa3d60b7737dfdaad2。entry先建立原visible-current-C-actual202-ten450-closed-geometry205 namespace与唯一起点，再形成`$RUNNER_TEMP/request222-runtime-metadata-workspace`；原checkout中的f6ca祖先请求不改。每个实际run块先source `$RUNNER_TEMP/request222-runtime-env.sh`，使GITHUB_WORKSPACE、VISIBLE_COMPUTATIONS、proof_directory和cwd均指真实工作视图，再从其中原220请求相对路径读取新字节。该视图的.git指向原对象库，只用于真实来源访问，不把临时derived文件宣称为Git已提交文件。原3b8 rules runner另外在RUNNER_TEMP创建独立partial clone/mirror做pull/rebase与双README检查；它记录当前科学工作视图，但不在该视图中执行这些Git写操作。最终entry与workflow的实际身份在末表登记。任何一个运行编号、源标签或路径替换都不能代替其完整 bytes/SHA 和原 producer 的真实绑定。

## 7. 必要读回与清理

每个语义角色的完整必要对象分别返回：完整新 head；三个实际 metric；实际存在的三个 measurement；实际 compare。原成功大数组/完整逐行科学账本按原必要范围留在同 job，返回完整身份及已选的失败/未访地址，不能假称全部科学行已独立复算。

每个必要对象各自仍有90000字节限制。极端未决或stderr过大时保原件，不分包、不编码、不提高门槛，不为塞入上限丢弃必要失败地址。最终主摘要本身超过90000B时reader返回70；某个独立角色body未完整返回、超限或身份不合时，该角色complete=false，最终主reader通常返回2，不能把所有子路径统称为70。源/输入初始化异常可在主摘要建立前直接异常退出，不能补造完整receipt或marker。新组合摘要只汇总 actual stage scope、各原必要身份、原规则元数据、原退出/资源/外部中断及quiet；不把数个大正文再复制进 job outputs/report。

measure/compare 的数学退出2并不自动令必要读取失败；若其原完整必要对象实际返回且来源/指针/quiet齐备，原数学错误、partial和未访按正文保留。相反，仅有exit0、hash或某个frame名字也不能补造缺失原值。

新清理 marker 位于 same-C217-readback/readback-complete.json，绑定 repository、run_id、source_commit、complete、quiescent 与必要摘要 bytes/SHA。composition另有独立必要 marker。实际次序为217新增完整marker与quiet→222entry.cleanup的真实修复/工作视图责任→原220九scope及原quiet清理。原所有底座成功读回步骤、原marker、原owner observation、原允许删除路径继续检查。任一必要未返、scope未知、真实进程仍活或原身份不符都保原raw；本入口不在单个阶段结束时先退科学输入。

report只接新增必要summary身份和步骤outcome。完整新增正文保在compute日志各自frame中；这一点不减少终态唯一读取者对新增必要scope的责任。


### 7.1 最终必要 reader 的明确范围

当前 reader 为 root_20261116_request217_same_C_necessary.py，35746 B / c64ef46a766d91ccb2f5dc684b4b663f8bdc75aa31e57c3f1f866f186c63600e。它通过真实runner.Binding读取实际derived220，不另把祖先f6ca写成当前请求。CLI为上一节的七个必需参数组，prepare/first/successors的实际step outcome均保留。

主schema是 request217-complete-same-C-consumer-necessary-readback-v1，主frame为：

~~~text
BEGIN_REQUEST217_SAME_C_COMPLETE_NECESSARY
END_REQUEST217_SAME_C_COMPLETE_NECESSARY
~~~

marker schema是 request217-complete-same-C-consumer-readback-marker-v1，路径为 base/same-C217-readback/readback-complete.json。只有完整必要scope、真实quiet、已完成归属观察且无外部signal才写complete/quiet marker。reader本身不删除raw。

八个stage按原固定顺序全部保留。未启动者返回其真正reason，不要求不存在的结果文件。已启动者必须有真实result，按对应原source/schema和完整bytes/SHA绑定后读取其必要对象：

| stage | 原必要对象的真实取得方式 |
|---|---|
| head_recompute | 调同一head source的readback；保原complete/quiet marker和新source/cut未付范围 |
| level0_metric、level1_metric、level2_metric | 各自原metric目录的summary.json，核source/schema/result指针后完整发该角色frame |
| level0_measure、level1_measure、level2_measure | 同一evidence source的readback；核原actual_complete_result |
| compare | 同一evidence source的series readback；保持完整系列schema和原层/比较结果 |

这些是不同语义责任的独立原必要对象，不是把一个超过90000 B的对象切成八份。主摘要只再保这些正文的完整身份及实际scope；report不复制每个大对象，唯一终态读取者仍须按compute中原角色frame读齐实际必要正文。

完整source-generation metadata及完整orchestration/stages/fields/errors/unstarted scope保在主必要对象。实际科学children的stderr保全原字节，以UTF-8 surrogateescape表示；stdout返回完整原文件身份，原必需result/error/pending已分别由相应必要body返回，不声称stdout全行都另传。

### 7.2 原 rules 选择器与固定必要列

规则元数据继续使用已刊34b49f02原selector。它对一般长string的1800限制、日志选段1200及首2末1、一般超过16项列表的原身份处理，均是既有范围；本reader没有将其提升为完整规则树或全部原日志已传。原读取错误、omission索引身份与这个边界会明示。

仅对该selector已经选出的固定rule-file字段，新reader使用公开固定列。每行标记json、json_readme、text或literal；只有严格符合两README固定路径/40hex词的map才按准确相同值共享。未知形状整行literal保留，不做任意科学JSON压缩。

expand_rule_files给出明确逆表示，但不在运行中新增对拍或接受门。原选中值、类型、null与缺键、负零、错误及原行序都保持；没有删新的失败字段来塞摘要。这个固定必要元数据表示不改变原科学接受判据。


## 8. 条件正确性与当前未付

若原底座真实返回首场与后继场、同job原 C 和材料/构造文件仍在、八个新 source view真实生成、R489完整来源/新cut绑定成立，并且各完整consumer按原包围算法返回，则：

1. 对原每个许可C成员，新leaf/cut/tail区间仍包含同一个准确函数值；新source不改变它的定义或CP。
2. 原metric闭覆盖和四Loewner证据适用于这个同一准确场和目标，所有未付闭单元仍在原pending/ledger。
3. 原operator-norm measurement的上下界与全t转移沿同一目标签名有效；原比较只能作其明确报告的比较。
4. source-only修复、生成计划、身份和时钟编排均不提供一个新的接受父或一个数值误差结论。
5. 原BVP/精化/几何/held/display仍按其实际原来源和原阈值执行，不从新增consumer的结果反推其成功。

本请求还没有实际accepted450、后继M128场、新 C 包围、metric pass、全域reach、held/δE或误差下降结论。即使某一层metric通过同一eta，也不足以声称误差持续下降至机器精度或原solver容差。原solver残差到全域relative-metric floor的缺失传递责任没有被这个新入口补造。

暂未加入：新的M>128实验；新半线/root语义；改变十个准确参数；另一段C/root realization选择；全尾导数新query API；新的BVP接受公式；自动延长18900+2700；自动把显示图当metric或嵌入证明。

完整交付身份、最终修复子合同与真实argv以 publication manifest 和本次小 outer request 的最终表为准。尚未执行的源验证和算术全部留在实际Actions，不在本地导入、AST、编译或试跑。


## 9. 已刊数学依据与最终发布身份

本次只组合真实来源和调用，不重复以下已发表条件证明，也不增加一个独立审核或科学前门：

| 已刊结果 | 本次使用的准确责任 |
|---|---|
| [R489](../results/R489-same-C-complete-head-recomputation-and-cut-enclosure-intersection.md) | 原全1440/six、同语义完整重算与cut叶交、原钟及真实子程 |
| [R492](../results/R492-same-C-leaf-refinement-for-the-fixed-target-and-accurate-cut-field.md) | 同根族三语义叶进入准确target/L与准确cut七系数/完整六jet |
| [R495](../results/R495-same-C-refined-leaf-complete-metric-consumers.md) | 四明确真实场族的先原loader后独立新叶view，以及metric/evidence入口 |
| [R500](../results/R500-same-C-recomputed-head-and-complete-tail-query-enclosures.md) | 新真实source累计半径进入全尾0阶E闭查询，旧/新/live覆盖交与fallback |
| [R504](../results/R504-recomputed-C-query-complete-metric-and-evidence-consumers.md) | 完整metric和series真实consumer、原root/DFS/全t与必要范围 |

### 9.1 最终六个执行与元数据文件

以下表为实际冻结字节，不包含尚未产生的运行结果。除workflow外，路径均在本课题；完整diff及临时publication清单只作交接，不另存可再生展开。

| 责任 | 正式相对路径 | bytes | SHA-256 |
|---|---|---:|---|
| 同C两slot runner | topics/visible-flex-larger-amplitude/computations/geometry_20261116_request217_same_C_refinement.py | 45394 | 3c56bbdd264babfe128d2895a8498bb3003669b60fc17245c608a3b59004a2f7 |
| 全部必要 reader | topics/visible-flex-larger-amplitude/computations/root_20261116_request217_same_C_necessary.py | 35746 | c64ef46a766d91ccb2f5dc684b4b663f8bdc75aa31e57c3f1f866f186c63600e |
| 完整composition | topics/visible-flex-larger-amplitude/computations/root_20261116_request217_same_C_composition.py | 30178 | ea0b98b410e04dc1abcc0eeb20f38d3cbd74a84a4854a258ce3ab749cdc4406f |
| 完整八view计划 | topics/visible-flex-larger-amplitude/notes/request217-complete-same-C-source-plan.json | 80964 | 68c284041ccb330e4d61f66161a0799643b9fd83c90016ddcdde3d9649a4b4de |
| 独立217请求 | topics/visible-flex-larger-amplitude/notes/current-C-same-semantic-head-refinement217-request.json | 26106 | dbb6c4c6b4e8fecb955c40fa90c271733dccddef70c3bda9104829bd86a6a75c |
| 独立217完整workflow | .github/workflows/visible-current-C-same-semantic-head-refinement217.yml | 86586 | e361dfc2b7b932a6ec9ddbf923612c95af329ad23c2181252a9f3f8fdaf6c2a7 |

四个额外公开数学baseline属于已有论文/source责任，仍明确绑定原字节：

| 原baseline | bytes | SHA-256 |
|---|---:|---|
| computations/geometry_20261116_same_C_full_head_refinement.py | 42246 | 0ce2f7ab8d1cfc95097ac8089c41ecc1f888343c8432255bd91b1d6cc5d3f8f8 |
| computations/geometry_20261116_same_C_refined_leaf_target_and_cut.py | 35549 | a7b1bd9d64db43986b5718d664dc6209227cd89a0cd9fb490e8dc6f9f4482aa7 |
| computations/geometry_20261116_same_C_refined_metric_family_bridge.py | 12303 | 06656a5ed8bd020d7ab476ed9790f8fc9e4e75d3e7f61ef9c9cc1fb765ddfc74 |
| computations/geometry_20261116_same_C_refined_head_tail_queries.py | 29687 | 2ab6b97fc77c520ed8b888d31a766d9e4e744fb40dc8af46dfd4d287f015b580 |

### 9.2 八个实际生成源

这些身份是计划规定的完整输出；只有本次 Actions 已生成且 source-generation receipt 实际核回后，才是该运行已绑定的真实文件。它们不作为 Git 中已存在的 source 文件声明。

| 角色 | computations/HERE 中的新 basename | bytes | SHA-256 |
|---|---|---:|---|
| head | geometry_20261116_request217_same_C_full_head.py | 42305 | 061cccfe69eea8121ceac1026d3962a06b067bdf877de580d35633a40d5c1b99 |
| leaf | geometry_20261116_request217_same_C_leaf_target_cut.py | 35531 | d856dd587792a7954d8b2973c6f64ae10c72d2e7907f78c15434c7e4093b9c97 |
| bridge | geometry_20261116_request217_same_C_metric_family.py | 12358 | 380669effe0187bfee7a09aa9e6e8585292a7ed0f828a9d0ffbfa405472c4877 |
| tail | geometry_20261116_request217_same_C_tail_queries.py | 29686 | c5f08411bc4d051e23f7107197c395d320cfc2c6fbf230ae51d853bd7b977ba3 |
| metric0 | geometry_20261116_request217_same_C_original112_metric.py | 57273 | ed8b07eaf0cf44913892c64dca54f2bfc2c51d662137f0ee8f3492d43fc2e776 |
| metric1 | geometry_20261116_request217_same_C_resolution112_metric.py | 57300 | f133274cf0296083e93b9582056e84bbe1cabd5ec11b0a473033eb0380fbd987 |
| metric2 | geometry_20261116_request217_same_C_incremental_M_metric.py | 57429 | 41b6ea186be015b59f30d01f1de06f5e28e6bc455cacded0fdc9489201d7ead8 |
| evidence | geometry_20261116_request217_same_C_metric_evidence.py | 65311 | 86477b9ee1610ed363bcd898d423552c02ca5134b4712c5f5914de6d1922cb2a |

| 角色 | 实际新 schema | 原必要 frame（存在时） |
|---|---|---|
| head | request217-actual220-same-C-complete-head-and-cut-refinement-v1 | REQUEST217_SAME_C_FULL_HEAD_REFINEMENT_NECESSARY |
| leaf | request217-same-C-refined-leaf-target-cut-v1 | 由调用者读原结果；无独立最终必要 frame |
| bridge | request217-same-C-refined-leaf-actual220-metric-family-v1 | 由调用者读原结果；无独立最终必要 frame |
| tail | request217-same-semantic-C-recomputed-head-tail-queries-v1 | 由调用者读原结果；无独立最终必要 frame |
| metric0 | request217-same-C-original112-live-complete-metric-v1 | REQUEST217_RECOMPUTED_C_ORIGINAL112_METRIC |
| metric1 | request217-same-C-resolution112-live-complete-metric-v1 | REQUEST217_RECOMPUTED_C_RESOLUTION112_METRIC |
| metric2 | request217-same-C-incremental_M-live-complete-metric-v1 | REQUEST217_RECOMPUTED_C_INCREMENTAL_M_METRIC |
| evidence | request217-fixed-target-recomputed-C-metric-evidence-v1 | REQUEST217_RECOMPUTED_C_FIXED_TARGET_EVIDENCE |


### 9.3 实际修复子合同和祖先绑定

| 责任 | 真实路径/角色 | bytes | SHA-256 |
|---|---|---:|---|
| 冻结220祖先请求（原checkout） | topics/visible-flex-larger-amplitude/notes/current-C-coast-base-zero-linear-gzip-incremental-M-refinement220-request.json | 99218 | f6ca63871733d3f5e48ef3eb8d540fc137806ceb1ae74cef01af6b21e25f3aba |
| actual derived220（工作视图） | topics/visible-flex-larger-amplitude/notes/current-C-coast-base-zero-linear-gzip-incremental-M-refinement220-request.json | 99330 | 2d1c3a7d56093f0009367bce0e201af14692b51541b759aa3d60b7737dfdaad2 |
| 222修复entry | topics/visible-flex-larger-amplitude/computations/root_20261116_request222_source_classification_repair.py | 28224 | 20360bb001f3849b3468071b4ca6f7b4017d5aa2bb7fb476791316d1a96a432f |
| 222完整source-only plan | topics/visible-flex-larger-amplitude/notes/request222-coast-base-source-only-repair-plan.json | 66182 | 7a74a8e65b7283bfe9acb36a27a38dbef01e8ee0507eff0ac4c3548015288ddf |
| 222独立小请求 | topics/visible-flex-larger-amplitude/notes/current-C-coast-base-source-classification-repair222-request.json | 9442 | 37f0b3b767eb233d2e714a143b4055e47dfc4629f2963e046b0511e05ba63672 |
| 222完整祖先workflow | .github/workflows/visible-current-C-coast-base-source-classification-repair222.yml | 99393 | 312005867b9a144c04e2cc47afb7620de2d43b1ecb3f9f9ad2a509f8746458d3 |

222修复子合同的完整接口为 [request222接口](2026-11-16-request222-frozen220-source-classification-repair-interface.md)，其源码条件见 [R510](../results/R510-frozen220-source-list-repair-and-single-clock-composition.md)。这里消费它的真实文件与声明，不消费某个222运行中或尚未返回的科学结果。217建立自己的真实run/source，并从同现场输入重做全部原科学。

修复source必要frame是BEGIN_REQUEST222_SOURCE_CLASSIFICATION_REPAIR_NECESSARY / END_REQUEST222_SOURCE_CLASSIFICATION_REPAIR_NECESSARY；唯一marker为base/request222-repair-readback-complete.json，schema为request222-frozen220-source-classification-repair-v1-readback-complete-v1。该scope完整返回只表示不可变source-preparation元数据已读，不自称进程quiet，也不提供任何数学通过。其body超过90000 B返回70且不写marker；实际初始化未完成的范围保持原错误，不假造derived receipt。新增217最终清理仍须其真正marker与summary身份，再由原220reader承担原九scope/quiet责任。

临时普通文件副本和source-copy-index保在RUNNER_TEMP，原checkout不改；无源码视图、diff或可再生科学大账被作为Git证据提交。222/217内部沿用205和220名称只标识明确子合同，实际运行的repository/run/source始终来自当前Actions环境，不把旧任务结论迁移过来。

### 9.4 当前workflow、真正slot与源验证范围

222六件已于main 6643ea831419fb5adf1fd5d21fdbc918fe86c4cd发表；该运行的后续科学结果不作为217输入。这里保留实际99393 B / 312005867b9a144c04e2cc47afb7620de2d43b1ecb3f9f9ad2a509f8746458d3，不使用一个未运行的修订版。

222的PYPINS全文仍把旧220 workflow作为原语法检查对象；不得倒写成222已检查了自身全部workflow。217的composer从该真实222文件提取完整19255 B / cc39da8308e718f4b755670730d855c204c0785a9ebb21b025b62868cf1b0281块，只将其中声明的旧220 workflow pathname替为本次真正217 workflow，再在Actions正常执行该metadata/源码语法块。完整原块、改后块、实际当前workflow与outer request身份记录在same-C217-composition/actual-upstream-preflight.json。这是当前217真实接线，不修改旧222执行字节，也不声称一种额外科学审核。

工作流保push与workflow_dispatch入口；当前compute360min、原contents:write/actions:read及report5min不变。两个新slot分别是same_C_first与same_C_successors，均由原绑定clock裁剩余时间。原refinement只要求其原bind220实际准备条件，不依赖新metric/measure通过。新增source/readback步骤是same_C_bind、same_C_prepare、same_C_composition_scalar和same_C_scalar；修复readback为repair_scope。第一次source准备失败时只保其真实错误与partial元数据，不能补造已接受场或完整成功receipt。

实际cleanup环境保原九outcome：C、cut、construction、far、BVP、rules、closed、refinement、composition。新composer另外接收本次composition和necessary两个实际outcome；其marker与最新quiet齐后，原222cleanup与原220scope仍逐一承担各自条件。report仅输出新必要summary的bytes/SHA、实际步骤outcome及原compute状态；全部新增科学必要body与准确pending scope仍只在compute日志。绿色report不能代替这些正文或任何数学成功。


上表与最终request的真实source descriptor一致；实际217结果编号仍为R490。没有实际run时不填写accepted父、完成查询、数值误差、全域pass或清理成功。
