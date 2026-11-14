# 完整静态独审：W14 / release-LU / direct CSC 新入口

独立审查人：tail_review_continued_2，2026-11-10。
已全文读取五份新Python源、完整方法说明、全部前向变换账本及三份冻结旧入口。
并复核所接两份检查器的真实输出schema和已审LU选择器的加载方式。
没有参与这五份入口源的具体实现。

**结论：接受完整新入口的静态源码范围，未发现阻断性源码问题。**
真实检查报告与root外部退出证据、明确的新函数身份、prepare单属性选择及恢复、
原数学参数和全部旧关闭门都得到保留。
**这不是可执行性或运行通过声明。**
本次没有Python/AST、factory、安装、矩阵、负门、纯准备、BVP或DN实际运行，
没有config、launch、新候选或通过报告。

## 1. 冻结出版清单与七件完整来源

出版清单：
[10b4787a990d03a9e5e5176a9b86e0ba4cff366c](https://github.com/Rogerhu12/math-research/blob/10b4787a990d03a9e5e5176a9b86e0ba4cff366c/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-spectral-true-m14-direct-csc-publication.json)，
blob208765a6e30cf7ede59113a61a0f57daf8228025，
4,552 B，
SHA-256 cf131f1574d92b1e315ab13074bf9fd59be3d236b0387e7cf7e114e810ce6b04。

七件文件合149,366 B，每件小于100,000 B：

| 相对路径 | 固定提交 | 字节 |
|---|---|---:|
| scripts/db6f-prefix-direct-csc-entry-gates.py | a804d0121309ac33ed4f1c3ee88c0a7586d7a47b | 20547 |
| scripts/db6f-prefix-select-direct-csc.py | 9af49bff30bae6307ff15167f918e3b40e2406db | 14009 |
| scripts/db6f-prefix-spectral-true-m14-direct-csc.py | 4682653bd3f69028709959d5667ffa47f0003204 | 24690 |
| scripts/db6f-prefix-prepare-spectral-true-m14-direct-csc.py | d01c9ae6e672ca7ad04755ea087a3564177d1bb3 | 13103 |
| scripts/db6f-prefix-audit-spectral-true-m14-direct-csc.py | 82ddbdffef930266a5aadb52bcbc24a513a01897 | 31225 |
| notes/2026-11-09-db6f-prefix-spectral-true-m14-direct-csc-source-transforms.json | 9b7640066e07bb0935c6a9907332e08f0b9eac41 | 29639 |
| notes/2026-11-09-db6f-prefix-spectral-true-m14-direct-csc-method.md | fc77e15562addd75b2e065aaac7768a6dccd21c7 | 16153 |

按表顺序的完整SHA-256：
1. d110a15669612ae75207d98b46b8ee31c41d5f98dc8a9b693a06a4cbc399606b。
2. e1083f63e26a5a248c9e8911308ba515f3b57c0d914b4bb8aceb6b6dc0660a49。
3. b6fd772b5f44819186fc7e31af370ffa199bfa5c9b14a2722b36345bcf26cd24。
4. 2e843363c57aee7d96b3359fc0735604f9c0fdbafce8ad4adb2feb421d4f3116。
5. b6222f3394c53eebd8409c922ed2e009de85b4bcdbfa5a6e8c8d57b2294967e0。
6. 1a3b90585de2cf352641e922b054413267a6906f6e061887a129dae3f7882e23。
7. 5e6cd1ddfe08d07f77ee32cccd9596529ef616189f75e2a3a316e52298d36f36。

Git blob按同一顺序为
25d9e33b56c27c10fce0b33e3259dc4d4b272504、
b80d31ec94d295cadd2d00a4839aa3a1afa1a231、
05424747517e97e7f6b4a5368d9f809312ad6f65、
fcc88cd81da8d0e1d9b87b1842878457315f7dc7、
024b3f6cb4889c6f06d63fc33e05f9b931ef9f3d、
8e49eb79e40f851279e2fea0e60de9d13d2b87e6、
71bbfd25052bef1c85d53bb3a5b79a10091aa161。
全部固定全文、字节、blob与SHA已独立核同。

## 2. 旧入口保留与完整变换重放

三份原release-LU源从固定10b4787a快照读取，符合既有冻结身份：

| 原入口 | 字节 | SHA-256 |
|---|---:|---|
| runner | 20496 | 2db1fe8b9171c3d9a7a4ac0d11311cff8daec1aa36bb8cd91130148903070ed0 |
| preparer | 9757 | 2018226a193294d7791492ec44d595e19ae004079ae717eb5557db249a21949c |
| auditor | 25074 | ee0d6aeadc4cfbe25ef4788581cebf81d5a50cfdb77b9a47f83d9d6df3071989 |

原文件路径分别是scripts/中的
db6f-prefix-spectral-true-m14-release-lu.py、
db6f-prefix-prepare-spectral-true-m14-release-lu.py、
db6f-prefix-audit-spectral-true-m14-release-lu.py。
这次只读原件，没有覆盖。

实际独立V8全文重放按账本顺序应用22、12、9项替换，
每一步先核当前文本中的出现次数，最后比较整个新文本及SHA。
三份结果全部逐字相同。
所以并未只比较几个选中片段而忽略文件其他位置。

所有替换也已逐项读过。
runner新增CSC来源、前提与运行记录、finally恢复；
preparer新增实际证据门和闭包；
auditor新增CSC身份/恢复检查及明示的新schema/status。
原数学表达式、尾部算法与数值阈值没有在这些替换中改写。

## 3. 两份前置检查必须是真实闭件

唯一foundation目标是v2，SHA
8e2bb061ef1fee94672601132cedb8ca7565d4006a327474f039f501e5f516cf。
其完整静态独审为
[398944aa07f18b8d44e614aa86cfe1bea14454ec](https://github.com/Rogerhu12/math-research/blob/398944aa07f18b8d44e614aa86cfe1bea14454ec/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-direct-csc-foundation-v2.md)。

纯源码/整数检查器固定SHA为
e437630f9718a898b31d16b21a2616034b0984d17a6b05ac5913f6cc7ec509dd。
新门核它的实际schema/status、checker/foundation与六份SciPy来源，
四项完整文本/AST重放、3/2项函数变换、中点更新恰一次、
原全局COO构造不存在、36个精确布局行、8个非法尺寸与5个损坏布局拒绝。
本次重新对照了检查器实际source_checks、assert_layout、integer_checks及main的输出：
字段、顺序与类型相容，不是凭方法文档猜schema。
它仍必须声明factory=false、matrix/solver=0及未作字节重放。

小矩阵字节检查器固定SHA为
197da92ec9ca8768c1b5a876aeed2b5164056fa7e3a3b3d790cd9eb626ee5bbc。
其完整静态独审为
[e4a15f7f830690c13d947ae764c648d445327ec8](https://github.com/Rogerhu12/math-research/blob/e4a15f7f830690c13d947ae764c648d445327ec8/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-direct-csc-byte-test.md)。
新门要求真正completed、PASS、无error、内部返回0，
原/新各15次attempt和completed及零求解计数。
逐场景核同一spec与顺序、完整三缓冲摘要/形状、canonical、
独立输入和副作用检查、指定中点/边界变化、所需符号零。

expected_specs从已固定测试源的唯一字面量return做AST读取，
不导入测试模块，更不调用它生成矩阵。
metadata门只核实际报告和来源，不能靠它自己“验证字节相等”。
真正字节比较由冻结测试源及外部执行证据承担。

## 4. root实际退出、文件闭包和类型门

四份文档必须互异：
pure_report、pure_observed、byte_report、byte_observed。
两份观察文件都要求observer=/root、
status=observed-process-completed、
actual_exit_code为非bool的整数0及非空tool_receipt。
短检查不强求长会话session_id；
真实长耦合关闭仍保留原session门。

观察command的Python必须是绝对路径，
解析到当前sys.executable的同一实际文件。
脚本、--foundation、--out及纯检查的--scipy-source-root逐项对应；
选项不得重复或增加未知项。
实际恢复时应按方法记录解析后的明确路径，
旧计划中的python3展示不能充作这个观察证据。

观察files逐项重读字节与SHA，
记录必须等于完整path/bytes/SHA身份；
本报告、对应检查器、foundation和六份SciPy源均不得遗漏。
额外闭文件可以列出，但同样真实重哈希。
观察文件本身再进入launch闭包，没有自引用哈希循环。

JSON读取拒绝重复键和NaN/Infinity。
核心布尔门使用is True/is False，
数值或结构比较用canonical JSON，使true与1、0与0.0不被普通Python相等混同。
source_map要求恰好六个无重复模块、各自冻结SHA并位于同一SciPy根。
verify_prerequisites重新读四份实际输入，
重新构造完整证据对象并与保存对象逐字段一致比较。

这些是有效的可追踪记录合同，
不应把一份写着observer=/root的计划或手造通过JSON当成真实外部执行。
当前这四份实际文档仍不存在，本文没有生成它们。

## 5. factory快照只规范化诚实loader身份

真实字节测试使用模块标签
_db6f_direct_csc_small_byte_test；
将来的运行使用新标签
db6f_direct_csc_selected_foundation_v2。
两个标签均显式记录，不伪装为原SciPy函数。

gate核factory的准确schema、foundation全字节身份、
六个实际源、NumPy/SciPy版本、十个原callback记录和两个新函数记录。
新函数必须位于固定foundation、正确qualname与首行。
运行记录schema包括module、qualname、filename、firstlineno及code SHA。

比较时只把两个新函数的module标签改为明确占位，
并把来源集合按module排序；
文件路径、完整SHA/bytes、版本、函数名、首行和code digest均保留。
真实两次factory由同一个冻结源产生，排序不改变其来源身份。

actual_sparse_byte_replay=pending必须保留在factory快照内。
实际字节测试成功属于外层报告，
不允许事后把factory创建时的pending篡成“当时已通过”。
新运行的fresh factory须与这个真实测试快照完整对应。

## 6. 初次选择：只改动态全局prepare入口

选择器导入只定义标准库辅助函数。
select_prepare_sys先完整重核前置证据，再核SciPy backend名称与_bvp.py SHA。
实际原prepare_sys、construct_global_jac、compute_jac_indices、solve_bvp
通过固定源code object、globals、defaults/kwdefaults和closure门。

solve_bvp的原默认值列表也与固定源一致。
W14必须仍持有同一个backend，且scipy_solve_bvp仍是原solve_bvp对象。
原solve_bvp运行时从backend动态读取prepare_sys，
因此可以让原求解外壳使用新prepare闭包，
而不替换原exported construct或indices。

foundation在新的真实模块名下编译加载，源SHA先核；
factory只做定义与来源绑定，不构造矩阵。
正常化快照相等后才生成Selection并赋值

scipy.integrate._bvp.prepare_sys = functions.prepare_sys。

这是该选择器对SciPy命名空间唯一的属性选择。
原exported construct_global_jac、compute_jac_indices和solve_bvp都保留。
Newton由另一份已审release-LU选择器预先选择，
CSC模块不再选择或更换Newton。

若选择后检查异常，只在当前prepare仍是本次新函数时恢复原prepare并重抛；
加载/factory失败清除新模块注册，不吞掉失败。
整个协议尚未实际调用，本节是完整源码审查。

## 7. 闭包、原helper和每次BVP的身份检查

新prepare闭包须恰含
collocation_fun、construct_global_jac、estimate_bc_jac、estimate_fun_jac。
其中constructor必须是本次新函数。
新construct闭包须恰含
csc_matrix、get_index_dtype、np、stacked_matmul。
没有旧i_jac/j_jac全局数组闭包。

Selection记录原exported对象与code、新storage helper对象与code、
CSC类五个方法、原callback/NumPy引用和EPS；
还记录当前已选Newton的对象与完整code identity。
每次check核当前prepare仍是本次函数，
新函数globals/defaults/kwdefaults及每个closure cell不变，
原exports未换、相关callback和helper code符合保存身份。

W14仍必须调用原solve_bvp，
Newton对象与code不变；
其STATS、np、splu别名由原release-LU Selection.check继续独立检查。
本次额外读取了冻结LU selector，确认它加载完整派生源于
db6f_lu_lifetime_selected_definition_v1，
与新auditor的code编译来源约定相容。

runner在每次真实BVP前后记录before/after Newton与CSC身份，
同时保留14个原物理callback身份和W14记录。
原数学callback的来源并未用新CSC声明替代。
本报告不把静态闭包分析冒充实际Python closure或安装协议通过。

## 8. 纯准备顺序与来源闭包

preparer在导入runner/NumPy之前先核四份实际前置文档。
缺失或正常拒绝返回NOT_READY_ACTUAL_CSC_CHECKS_REQUIRED；
--check-current-gate只检查这项，零写入、零factory、零solver。
本轮连这个负门都没有实际执行。

正常纯准备才导入定义，读取原97绑定参考bundle、
原checkpoint及其自有实际尾包，复核旧包schema。
它不建立候选、restart、flow、RHS、Newton安装或weighted solver factory。

原闭包继续保留；
新增三份历史release-LU入口、五个新源、foundation/两checker、
四份真实证据、六份SciPy源及新方法/账本。
本地Python依赖扫描继续包含原coupled main，
不会因跳过未使用依赖CLI而漏掉真实主流程。
所有callback文件均在完整绑定集合中。

新schema明确是db6f-spectral-true-m14q512-direct-csc-v1。
所有验证通过后才独占创建新config/launch/preparation三个小metadata文件。
stem必须完全未用。
如果之后发生I/O失败，已有文件仍属于这一失败尝试，
不能据部分文件存在宣称纯准备成功或重用stem。

preparer自身可写launch也不等于完整运行获审。
root未来仍须把本完整审稿、实际前置结果和真实资源/空间条件
纳入其运行前审查；方法明确保留这层责任。
当前没有预造计数、未来正packet或新的launch。

## 9. 原参数和有限方程保持

expected_config、expected_parser_argv及without_io整函数逐字未变。
tail config仍仅调整五个I/O键，
全部非I/O字段按canonical typed身份与原config相同。

完整保留的主要设置为：

| 项目 | 原值 |
|---|---|
| prefix模式 / 角样本 / 审计角样本 | M14 / 512 / 1024 |
| prefix最大节点 | 6500 |
| prefix tol / bc_tol / physical_bc_tol选项 | 2e-9 / 1e-8 / 2e-11 |
| tail深度 / shootingParts / steps / auditSteps | 12 / 8 / 32 / 32 |
| tail solveTolerance / maxIterations | 2e-9 / 36 |
| 原projectionFloor默认 | 0.05 |
| Node heap | 1536 |
| 求解选择 | fixed、lagged-tail、preserve-restart-mesh、显式空warmup |

default初猜边界修正仍为true，
原材料字段、gauge amplitude、warp reference、chart和真实尾参数不变。
N512仍只是角quadrature，未改称径向加密。
8轮outer、实际DN/J、BC与最终seam流程全部保留。
没有引入分块QR、新Newton方向、不同merit、SuperLU排序或另一套容差。

## 10. 实际runner、首包与恢复状态

第一次真实BVP入口前，仍先核原f6 install和14个物理callback，
显式选择已审release-LU，然后选择CSC。
原main在此之前产生的真实第一DN/J仍按旧程序处理；
CSC factory本身没有DN或矩阵调用。

第一尾包只在实际闭包存在时核其完整request、height与source/config，
形成ACTUAL_FIRST_DN_CLOSED_BEFORE_INNER_BVP记录。
它只支付一包实际DN，不支付完整BVP或外层关闭。

selected_solver仍是原W14 wrapper；
返回值和物理PPoly、物理RMS/BC由原已审路径核算。
每轮异常保留在对应call记录；
finally还核before/after身份并更新实际reproduction。

外层旧check_outputs通过后才暂记有限耦合成功。
最外finally恢复原prepare，记录原→新→原，
且明确不恢复/更换另行已选的Newton。
成功恢复要求原prepare对象回到backend，并核共享身份。

如果restore检查或恢复失败，状态改为失败、
mathematical_success=false、请求非零退出。
因此“原数值门已过但恢复失败”不能变成最终成功。
遇到已被其他内容破坏的运行身份时，不承诺任何未经检查的清理已完成；
最终审计必须看到真实成功restoration记录。

## 11. 全部旧数学关闭门和新的CSC门

完整check_packet、polynomial_endpoint、
check_newton_lifetime_record三个原函数逐字不变。
check_outputs仅更换明示的状态标签，
其他旧数学逻辑未删改；
check_runtime_records只新增CSC前后身份核查。

保留的有限关闭内容包括：
- 原八源、精确request/config、真实tail residual严格小于2e-9；
- 616个Jacobian项、17个jet字段、865×28 staged states、13×28 raw states及其镜像；
- 43物理状态、14参数、13 correction scales和固定材料字段；
- 全部有限quintic chunks的SHA、每件小于5MB、float64/形状/有限值和连续状态分片；
- 原物理RMS<=2e-9、每轮inner_success、1至8轮actual outer及最终实际BC<=1e-8；
- 保存PPoly真正端高对应最后实际seam请求，896角样本、后续实际Jac/audit及原记录身份；
- W14返回物理坐标、roundtrip、原物理RMS/BC和14个真实callback来源。

这里保留physical_bc_tol=2e-11这个原输入选项，
但没有把它另写成旧关闭代码未要求的最终BC阈值。
二jet mismatch和sampled/source metric仍按原范围记录，
没有新增二jet数值门，也没有把采样metric当成连续整图证书。

新auditor另外核CSC schema、真实前提与factory对应、
原exported函数、新函数、storage helper和Newton的code digest。
_compiled_runtime_record从绑定完整源编译并沿qualname定位code，
不执行这些callback。
它把文件位置、module、首行和marshal code摘要与运行记录比较，
而非只相信一个人写入的函数名。

初次selection必须等于首轮before_csc，
restoration前状态必须等于末轮after_csc，
恢复后prepare必须是最初原函数，Newton身份不变。
任何restore_error都拒绝。

## 12. 首包、最终tool退出与连续数学结论分开

first模式只审已闭首包，不读活动trace，
也不伪要求整轮过程已退出。
它准确返回PASS_FIRST_ACTUAL_M14_DN_ONLY。

final模式保留原root真实长会话观察：
非bool整数exit0、正session_id、非空tool_receipt、
正确stem及完整闭输出绑定。
程序自己请求的exit code不能代替此观察。

final还独立重读所有实际输出，
重算保存多项式端点并重核原有限门，
要求与reproduction里已保存的关闭检查逐字结构相同。
新最终PASS标签只称TRUE_M14_W14_DIRECT_CSC_FINITE_COUPLED_CLOSE。
它不支付连续XYZ、整图metric、reach、像幅度、闭曲面或G5。

## 13. 本次真实V8文本回执及一次已纠正的辅助检查

回执一：
tail-review-direct-csc-entry-full-text-replay-01，
clock实际2026-11-10 00:22:56 UTC。
三份完整源的22/12/9项顺序替换，
每步出现次数、最终全文/字节/SHA全部实际相同。

该cell另有一个辅助函数比较写错了抽取器返回类型：
抽取器返回数组，初次却按函数名索引，
导致那个辅助比较未真正取到函数文本。
这个问题在封任何报告之前已发现。
它不影响同cell已经逐字完成的三份完整文件重放；
但初次的“12函数”计数不作为证据。

回执二：
tail-review-direct-csc-entry-functions-text-replay-02，
clock实际2026-11-10 00:23:17 UTC。
这次对每个函数明确要求恰一个非空抽取，
再比较完整文本并计算SHA。
12个完整函数实际一致：

equal、without_io、write_json、expected_config、expected_parser_argv、
runtime_original_newton、runtime_newton、select_runtime_newton、
runtime_callbacks、check_packet、polynomial_endpoint、
check_newton_lifetime_record。

前三个关键数学/存储审计函数的整段文本SHA分别为：
- check_packet：f73042a44141d80a1e847e66d070c06af3f356ceb82eb35a13640128e1a24b3e。
- polynomial_endpoint：fe89a03b7e7d346a84220cf919a36b0dcd8641a829e65ef0d1d1b33605336cf3。
- check_newton_lifetime_record：83e1c769d946036aa6f15c5026e4a69ddd3a1837a72a090f5029e08a5e4c9098。

以上两次都是JavaScript/V8的小文本检查。
没有Python AST、NumPy数组、factory、安装、选择/恢复、
check-current-gate或数值求解实际执行；
没有Python或shell exit0可报告。

## 14. 接受边界和恢复后仍需支付的动作

本报告接受五源与计划的完整静态设计，
并核明旧数学门未放宽、前置证据和运行身份链完整。
它不保证实际Python可执行性、closure运行身份、
平台marshal表现、全部source gate或真实小矩阵字节会通过。
这些正是恢复后实际检查要解决的事项。

两份冻结检查器各需真实执行及root独立自然退出观察；
新选择/检查/恢复协议和纯准备也各需真实验证。
之后才能依据实际新launch、完整来源和当时资源条件考虑新的主运行。
本稿不启动该过程，也不修改任何既有resource/space guard。

没有承诺实际内存峰值下降到某个cap、SuperLU成功或非线性收敛。
旧资源失败及失联原因没有因本源码而被重新解释。
旧文件全部保留；任何后续修订另存新身份，
不能把未运行项改记为已通过。
