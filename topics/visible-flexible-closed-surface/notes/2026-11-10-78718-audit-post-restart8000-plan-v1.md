# restart8000 成功后原生产链计划器：完整独立审查

日期：2026-11-10。审查者：independent_audit；会话 Astra-visible-flex-78718bd0。审者没有参与主 M14 的初猜、节点预算、参数选择或优化。

## 1. 结论与边界

**冻结 plan-v1 通过完整源码、成功入口与后续接线审查。** 它把已审 restart8000 完整出口门接到原单容器生产家族，要求新鲜完整审计与已保存报告逐字段一致，再解析该次成功 CP 自己最后的真实尾包。它保留基础 prefix、目标、桥、共同 cut、完整两侧证书、原正常终门和同图网格的全部既有依赖，没有把局部、预检或旧图证书作为完成缓存。

计划器只生成未来命令及其依赖。本审没有成功主计算可消费，**没有运行正向计划生成，没有创建未来生产目录，没有调用 producer、solver、区间数学后端或网格算法**。本人独立实际完成一次纯静态输入检查及两次负门执行，结果见第 7 节。不存在成功 CP 时没有伪造一个正例，也没有调用 command_plan 绕过成功门生成生产 argv。

本结论与主运行是否成功完全分开。root 的真实自然退出仍由 root 的实际工具回执和自己的观察记录支付；计划器无法凭任意 JSON 本身证明真实进程曾退出。本审没有消费或轮询 root session 72917，也没有把旧 session 2770 的不可访问状态判为成功、失败或仍运行。

## 2. 绑定对象和实际阅读范围

全文审查：

| 对象 | B | SHA256 |
| --- | ---: | --- |
| scripts/78718-plan-post-restart8000-v1.py | 32491 | c6ef233eb40517bf1986b3ea25d0bb31d102d4b219727c6d69a97b38ee1e0456 |
| notes/2026-11-10-78718-numerical-post-restart8000-chain.md | 19010 | f3cb14844116c529463a1402ad31e29a0dd18daa663378898d6eefc9ae12a926 |
| notes/2026-11-10-78718-numerical-post-restart8000-frozen-entry-01.json | 3669 | 22bc9c3f54172315864fdb599dd58a026bc16f5768cbb6fe044dbc2bfe7f05cb |
| notes/2026-11-10-78718-numerical-original-independent-seed-scope.md | 7930 | 3aeb66ddba71c8cf85a9029ff817e8823cea535d438f6872db6025d4c0a53b3f |

另重新对照已完整审过的 restart8000 final auditor 的整个 final_audit/main、原 terminal.Files.file 的解析顺序、原 exporter/网格 manifest 字段和相关 CLI。回看原独立全链协议 §§1、3、5–10 和本人的 [run02 生产链审稿](2026-11-10-78718-audit-run02-production-chain.md)，核新入口除了成功对象/来源身份外没有删去真实生产步骤。

本次没有声称重新证明所有已审旧数学程序。所用旧源实物 SHA 已全部复核，固定来源集合与之前已审入口相同；本次完整新代码与新接线是实际审查对象。数据和数组仅在终端内读取/散列，未输出数组内容。

## 3. 成功门是完整原审计，而不是缩小的摘要谓词

### 3.1 启动前的路径与身份约束

build 先要求未来 run 是当前 topic notes 下另名、尚不存在的直接子目录；计划输出是 notes 下尚不存在的新文件，不能位于未来 run 内。这样写计划不会提前创建生产目录。main 再以 exclusive binary create 写输出，拒覆盖历史计划或拒绝报告；输出严格小于 1 MB。

成功入口 audited_success 要求实际 sys.executable 等于被冻结的 primary Python 绝对路径；先核完整 final auditor 的 SHA 为 cd090888e4552317bce183c3b5788710ced9e17eea965b9489252e96d2f3496f，再 import 该实际源。launch 必须是 restart8000 的显式 schema，执行原 c.validate_inputs，并核传入 launch 路径就是其绑定的 launch_path。

它没有只读取 root 成功字段、首 DN 报告、guard completion 或 CP.solver_success，也没有从活动日志或 mtime 推断出口。旧 run02 的失败 CP 作为已声明的求解输入仍保留，但不是此后生产图的成品。

### 3.2 新鲜完整 final 与保存报告完全一致

计划器构造的 report 初始字段与原 auditor.main 完全相同：scope=auditor.__doc__、mode=final、ready=False、solver_calls=0、active_trace_read=False。随后直接调用原 final_audit(context, observed)，合并结果，置 ready=True，并要求精确成功 status。

我逐行核对了原 final_audit：它要求 root 的 observed-process-completed、observer、非空真实回执、正 session id、同 stem、整数 exit 0；重新比较 reproduction 的 launch、全部 source bindings、实际 argv、委托 argv、Newton/CSC 定义与完整运行时记录；要求实际 BVP 调用、正常恢复、无 restore_error；要求程序数学成功/无 error/请求 exit 0；真正重新调用 check_outputs，核 CP、全部 PP、summary、各 outer/final tail 和完整关闭文件。root observation 必须绑定这些真实关闭文件及 launch/reproduction。

计划器随后用规范 JSON 比较新鲜结果与独立保存的完整 final 报告，不能用部分字段吻合替代。原 auditor.main 与计划器产生的 report 没有一个随时间变化的额外字段差异；路径、来源和实际文件身份都要一致。read_json 拒非有限 JSON 常数，same 使用排序键、固定分隔符及 allow_nan=False。没有把 saved report 当作避免完整出口重读的缓存。

成功观察的真实性来自 root 真正持有的工具退出回执；程序对声明的观察做同运行、文件闭包和成功状态核验。本审的两负门证明缺观察和错运行观察不能通过，不宣称对任意伪造来源事实作出了数学防伪证明。

### 3.3 成功 CP 自己的最后尾包

完整 final 后，计划器再次重算 CP 实物 identity，并与 final.prefix_CP 全等。它只从该 CP 的 tail_seam.tail_record 解析尾路径，正确相对于 CP 父目录处理相对路径；文件名必须等于该次 context.out.name 加 CP.tail_calls 对应的最后编号。

这个尾实物的 path/bytes/SHA 必须逐字段等于完整 final.required_closed_files 中已经审计关闭的那一件。它不是预填首包编号，也不能用旧 seed 尾或失败 run02 的尾替代。本次物理 linear port 还必须等于固定 LINEAR_PORT_SHA。

因此成功后用于 mirror exporter 的是本次成功 prefix CP，用于 tail exporter 的是它自己的最终 audited tail，两者没有互换。最后在 plan 中记录的 own_successful_checkpoint 和 own_final_audited_tail 仍由实际文件计算 identity，不填未来猜测 SHA。

## 4. 固定输入与原终门参考对象

verify_fixed_inputs 只进行散列与 JSON metadata 检查。它首先钉住五份冻结 provenance 索引，再按其中实物路径逐一验证：43 个 source-root 快照、原 literal source 闭包、manifest、原 21 终门源码、额外径向/点界源码、linear port、原 M8 manifest 与八个 raw gzip、tight/lowmetric 原值包与其数据文件、两包相同的六定义、原 height/positive-alpha/bookkeeping 证明及 M12 参考头部。没有调用原尾 reader、区间算术或物理流。

本人实际重新执行所得 **127 项绑定与作者静态报告逐字段相同**。代码中全部字面生产/模板/附加 source 共 22 件，实物 path/bytes/SHA 均处于这份精确闭包，而不是只确认同名文件存在。固定 source inventory 的 source_snapshot_count=43、terminal_required_source_count=21、哈希全符、无未解决字面引用等谓词保持。

Bindings 对同一实际路径合并 roles，并要求重复遇到时 path/bytes/SHA 全等，不能在一次计划中把两个不同版本悄悄归到同一路径。build 进一步绑定成功 launch 全闭包、所有实际 final 关闭输出、reproduction、root observation、计划器与 auditor 自身、实际 Python/Node 二进制。源文件在以后实际运行每步时仍要遵守计划的开始/结束来源与输入身份记录，计划不会代替未来那次执行。

### M8 背景与 M12 终门参考没有混用

M8 tight/lowmetric 的参数预检只建立固定 w/w_r 来源身份，不产生本次新图。计划用实际新 tail-manifest 调用原 transfer-v3；没有使用 check-parameters-only 去冒充转移。

原 terminal 的 M12 真点下界仍要读取原参考实物。现有静态状态是 26 件缺项：24 个 raw、原尾 CP、原 point packet 头；另有一个必须待真实 packet 头取回才能确定的 data 后代。missing 对象仅给来自已钉 metadata 的 expected SHA，缺时没有 actual identity；未知后代只记录要解析的 data_file/data_sha256，不编造值。

existing_reference 与原 terminal.Files.file 的候选顺序完全相同：原路径、parent/原路径、topic/原路径、repo/原路径、parent/basename。若实际找到文件就按预期 hash/可用大小核验；否则明确 deferred。terminal_reference_ready 只有所有对象存在且没有未知后代才为真。

允许在 M12 大文件尚未取回时产生“未来生产命令计划”并不等于允许 terminal 通过；terminal command 的完成条件明确要求它们先实际存在，原 normal candidate gate 自身也实际读取/核验。plan_ready 只表示主成功身份已核且命令计划已生成，不表示所有未来输入或证书已经完成。

## 5. 全部生产接线与互斥分支

本计划原单容器家族固定；source M14/N512、native depth12/parts8/steps32 来自已审主入口，下面的 export/Cartesian 参数属于各自有限表示。审查没有重新选择或优化它们。

| 阶段 | 必须消费/产生的对象及核查 |
| --- | --- |
| tail-export | 本次最终 audited tail；原 endpoint exporter，depth8/steps32/flow32/angular512/degree192、critical cell0/base64、ratio .05/endpoint .025、差分 .00005、诊断128与三分数。无 plan-only。等真实 exit0、manifest、全部 shards 和后来写出的 collar 都关闭。 |
| tail-radial / collar / first | 自有新 manifest/collar；精确锚、正增量、共享行与全分片、完整 collar 检查；first 依赖两检查。原参数解析与输出名均吻合。 |
| prefix-base | 本次成功 CP、固定原 linear port；原 mirror exporter；Cartesian M24/angular768/quadrature8/subdivide1/ell0。只通过已审文件 cap 包装，不换算法。 |
| prefix-target / base-metric | 自己实际基础图的 analytic target 与基础 metric，供 bridge 真正读取。不能拿共同图 metric 或作者旧 report 代替。 |
| bridge / common-cut | 同一新尾、基础图与基础 metric；原 exact bridge，width .15 的 common-cut make；按实际尾 signed modes 扩展，不能把 M24 当最终扩列模式数。 |
| prefix geometry / baseline / moment | 同一 closed-map；分别重新执行完整几何、baseline 与矩界。geometry/moment 的 angular/radial 不误说成能收紧 baseline metric。 |
| optional complete angular | 只有 baseline 经目标转移后不足才按原流程诊断并使用完整角分支。argv 无 intervals 局部限制；budget2e-9、128 arcs、depth4 为原初档。 |
| background-k / tail-full | 原紧背景经实际 new-manifest 转包；full angular128/radial1/background6/算法阈值8.5/block128，无 limit 或局部跨限制；包括 collar(-1)及全有限跨。 |
| optional background-e / metric-only / completeness | 只有完整 full 的 metric 不够时使用同新 manifest 的低 metric 包、完整 metric-only，再与本次 full curvature 报告做覆盖检查。metric-only 不冒充曲率来源。 |
| closed-budget | 选择完整 baseline 或 angular 的本次证书；同一 geometry/moment、tail-first、原 height/positive-alpha 和实际 background-k；原目标只转移一次。 |
| whole / terminal | 每个选择路径分别命名；whole 只在 metric-only 路径带可选参数。terminal 是正常 candidate 模式、精确 1/500000000，非负例模式，必须实际 M12 来源与改善门。 |
| mesh plan / height / build | 同一 closed-map/whole；原 angular144、prefix128/tail64/collar4/cap12；原实际 height sampler；未来真实 manifest 给出三件实际文件。 |
| PL / same-plan review 模板 | 三个精确时刻 0、1/4、1/2；真实闭 manifest 选择 file/time_exact 并核 sha256/stored_bytes；独立 same-plan manifest 必须来自真实外部独立 build，不能造占位文件。 |

所有 source CLI 名字、旗标与位置参数同已审原接口；尤其尾 exporter 第一个参数是 tail CP，bridge 用基础 metric；whole 的 tail-metric-certificate 真正可选；mesh 的高度 sampler 使用实际 radii/source-root/calibrations/alpha。原 exporter 的 mesh_files 确实有 time_exact、file、sha256、stored_bytes，故延迟模板字段正确。

### 四个最终路线不会互借不存在的报告

两个 prefix 选择乘两个 tail 选择得到 baseline-full、baseline-metric-only、angular-full、angular-metric-only 四条互斥路线。每条 whole、terminal 和 mesh 输出另名；计划本身不替审者选择一条。完整 baseline 已够时无需执行 angular；完整 full 已够时无需 metric-only，并且该 route 的 whole argv 真正省略 metric-only 选项。

angular 的预算比较在原程序内部先作 epsilon*(1+eta)+eta 的精确 Fraction 转移；本计划中的 branch_policy 与它一致。terminal 仍从所选真实闭证书组合，普通 whole 的 1e-6 不会被当作最终 2e-9。

command_plan 的所有 id 唯一、依赖 id 存在且所有可执行 argv 元素必须为字符串。循环在源码层声明 40 个条件命令节点和 16 个未来解析模板；本审只核源码结构，没有通过调用该函数制造一份未获主成功支持的命令计划。分支 condition 是人可读的执行条件，不是这里已经执行过的自动决策。

expected_output_paths 是此时能准确命名的头部/报告路径，不冒充未知未来 raw/row/mesh 的完整清单；每步 completion rule 要求真实关闭后记录全部自有输出。各后端仍必须运行其原完整覆盖与源绑定门。

### 文件上限与未解析模板

prefix-base 原容器用 RLIMIT_FSIZE=4,999,999 的已审纯包装。超限是真失败，部分输出不是图；不因此降 modes/nodes 或把旧数据顶替。原 mesh writer 在选择后缀前检查 raw<5MB，大于1MB时 gzip，并检查 stored<5MB；因此 `.ply`/`.ply.gz` 必须由真实 manifest 决定，模板不预猜。

本 v1 只列原单容器 source。此后另名存储 v2 已由 [完整独审](2026-11-10-78718-audit-storage-family-v2.md) 通过来源闭包，但不能因此悄悄改当前计划的 source 或 hash。真要切换必须以新身份明确给出该支路的计划和实际报告；这是保持既有来源，不是增加数学门。

## 6. 原种子说明的身份与可声称范围

配套说明准确区分：原97项 reference 的公开前置是旧真 M14/N512 prefix 及其自己 tail_0002；direct-CSC run02 的141项 closure 从这对输入开始；restart8000 的直接输入则是本轮失败 run02 CP 与自己的 tail_0003。这不是旧 R21 M12，也不是未来成功 CP。原 reference 已作为新输入门的闭包在本次负门前真正重核；我没有调用种子初始化或求解。

原独跑协议允许已有已审 warm/较粗解作为真实前置，不要求重新搜索全部失败初猜或再次做每一段 continuation；同时对“一次冻结命令的精确 replay”明确只改 I/O、原 seed/数值选项不变。这两个层次不能互换。

因此配套说明对两种未执行路线的区分合理：另名并先冻结审查的旧 M14→cold8000 是不同输入路线，不能称当前 failed-CP restart 的仅 I/O 重放；旧 M14→6500→自己的实际中间 CP→8000 更直接重现当前两段生成算法，但第一段的真实出口不能预造或强迫为失败。若使用不同数学 payload，需为自己的同 g 图完整重新认证，并明确交付对象，不能套作者证书。

**本审没有选择哪条路线，也不批准一个未实现的 cold8000 入口为已经可执行或已满足最终独跑。** 当前计划的 remaining_final_obligations 正确保留真正原种子 solver→有限图→完整连续后端→网格流程；单独读 prepare/final、只读 CP、同 plan mesh byte review 都不能替代它。没有新增必须回到 M12 的要求，也没有把 hash/metadata 检查称为独立计算。

## 7. 本人实际小检查与精确证据

### 7.1 纯静态来源检查

真实工具 **d9912d，exit 0**。以冻结 primary Python 编译/import plan-v1，只调用 verify_fixed_inputs；在调用前将 module 的 command_plan 局部替换为直接报错函数，防止静态检查意外生成生产计划。没有修改源文件。检查完整冻结入口中全部源/文档/报告实物 SHA，核固定返回值与作者真实静态报告逐字段相同，核 22 个实际命令源都在精确绑定内，并确认没有 import NumPy/SciPy。

报告 [独立静态检查](2026-11-10-78718-audit-post-restart8000-static-01.json)，7,118 B，SHA256 **0f1b982c3b519ec938860a60c805f08c47cdb52f51e8a6af9be28a379756d845**。127 固定绑定、26 缺参考对象、1 未知后代、0 solver/producer、0 成功计划。这是本人真实执行；作者 a0190a 的原结果另外保留。

### 7.2 缺少真实出口拒绝

真实工具 **d556fe，自然 exit 2**。传当前真实 restart8000-02 launch，但传本人明确尚不存在的 root exit/final 路径；全新未创建的本人 run 名字。原输入校验后在缺失观察处拒绝，输出 NOT_READY_OR_REJECTED，plan_ready=false、complete_final_audit_replayed=false、production_commands_emitted=0。

报告 [缺出口负门](2026-11-10-78718-audit-post-restart8000-missing-exit-01.json)，266 B，SHA256 **542903ae4255fad4a58f569ada19c3aad299cc750a2a702084a079825fd805c0**。

### 7.3 借用旧失败运行观察拒绝

真实工具 **7b4a3f，自然 exit 2**。仍传当前真实新 launch，却传旧 direct-CSC run02 的真实 root-observed-exit；拒绝 Wrong actual root observation identity，0 生产命令，未读一个“成功 final”占位物。

报告 [错运行负门](2026-11-10-78718-audit-post-restart8000-wrong-run-01.json)，269 B，SHA256 **d33813790de79a23589262f44db58aedebdd383b155b5b7f881374f5e668c393**。两负报告的字节与作者同类实际负例相同，但这里保留各自真实回执，绝不以旧执行冒充新执行。

这三项是本次仅有执行。没有扩张成伪造正向 CP 测试，没有主 BVP、DN、RHS、Newtons 或 producer。两个本人 prospective run 目录保持不存在。现有证据足以解决计划器的静态来源和拒绝边界；其未来正向执行仍需真实成功输入，不能在本审预支。

## 8. 后续实际义务保持

没有发现此冻结计划器的实质数学或接线缺口。未来只有 root 的真实主成功及原完整 final 正向通过，才可生成正向计划；之后每一所选后端都要真正执行、记录自然出口、输入/来源及全部自己输出，原正常 terminal 必须实际通过精确界和改善条件。

G5、全时间几何条件、README 网格/独跑要求及强振幅/reach 后续目标仍各自保持。有限数值计划与证书不证明严格无限尾存在。本审通过只结清这个纯计划器的审查，不作为主问题或任何阶段的最终完成宣告。
