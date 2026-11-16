# 真正58后继：保持末环的原102前缀全曲面修复

日期：2026-11-16。**这是一个新的完整body耦合问题；还没有数值结果或第59点。** 仅源码/参数/纸面接口在本地准备，全部新数学值、frame、周期原函数、解析导数与优化只在本公开仓库Actions执行。

## 1. 为什么这次问题不同

[上一范围](true58-free-R1-R2-ring-success-wholebody-failure-20261116.md)已经在同一原172盒中得到自由R1/R2的有限环解：环曲率粗16.393442215426443/细16.393396474844106，但唯一全body预测η6.979414564941248、κ69803.90363577171失败，0actual，真实accepted index仍58。旧自由36环问题已经闭账，本任务不改初点再求同一个环最优值。

[R514](../results/R514-complete-fifty-one-ring-controls-and-conditional-seventeen-variable-curvature-fibers.md)给了原前六径向样条B3…B8的准确支持结构：其u54、v48共102个系数在s>.765的整个后缀值、一jets、二jets均零；端点处按原光滑支持同样保零。它们能够影响上一候选的s=.585、.7125两个违规区域，却不改变s=.78已获得的环二jets。

因此固定上一free36**未接受**候选的全部其余66独立坐标，只开放这102个原控制。原末51/Q/height/new9保持同一once-rounded168值。该102维仿射纤维是本任务唯一物理参数空间；不新增基、改g、改reference或放宽原盒。

## 2. 原输入身份与新的费用起点

唯一accepted source仍是run43859882465/research133273598120/source0e6fafbf7bce37cd851dfc972b2de1ff3d0d5881的真实58。其physical为94950b2bd5d7b5241e14333a4315b073f64840f74849a7909d6de8cb3cc29f54，ind168为e2d52f849596a5e7bbf596b66d7805587acc944c1549c5648ee4e115548ed2bf；原两网4454/4549池和v15/14顺序逐字保留。

未接受ring candidate来自run43884276617/research133358065602/source7ac3c637ec9fb7d151e7b0f7f2ee314dd137533c：

- RING_SOLUTION 148788B /752025d1ef9dd9adb557aa7bf0f1c3899fb8a4cd417d00233289c0ff066ab3ae；
- COMPLETE 344760B /396b50f3bfda35ec5131a3fdff61592a4c1dd27d2f69625da2e377965042f381；
- FINAL_CLOCK 7596B /78152b9c0ea685146a3c34c1792660d42ea9f50b99b0dfb24f3d50feffcfa423；
- 原raw日志38467120B /64d1bd45673f9de4b533008b812acc4300024f34a976edeeb1886fd896076a80；
- candidate physical为ab59622808faafbb1a1896a2edc670585c13373869665fb95c31b6ca8a1f2773，array_digest为b252055bf59dbdd9e4d22691b2fd1c8ae35f88b2795c7a38f894876cd50c5da7；
- 原168数组rawbytes binding为5da50ccd367a7d1f5c9f621737c5b2bafcaba2db0eb39e3875adcb3fe6fffbf0，准确binary64向量按原记录逐项恢复。

只读取三个原log：58 COMPLETE/CACHE2/FINAL、永久55 constructor COMPLETE、上述free36三记录。旧ring17/ray/joint模型不再读取或执行，新的102模型不需要重算已解环。永久55只提供原reference/height-map constructor，绝不冒当前几何态。

祖科学账2974.589423877秒/147原full值已经关闭。本次全部imports、三个原输入body读取、字段恢复、新frame/Pi/J、求解、失败和stdout均从同一个真实pre-import时钟计入新600秒；旧余额不转入或重置。

## 3. 先支付该纤维不可能改变的后缀

上次全body预测没有保存完整大数组；hash、峰值与摘要不能替代这些数组。本次新付一次固定g的a/a_s/a_ss及所需height和两网scalar/frame/完整周期原函数，得到当前未接受ring candidate的真实完整body值。

直接从这些本次新值检查s≥153/200的固定后缀，使用：

1. 原58 η基准.26600541463999305与原下降要求1/10000000，得本次完整body metric budget；
2. 原58配置的全body曲率cap、原未平方四PSD、独立direct主曲率及原法向面积下界；
3. 原相同网格、原metric定义、实际G/Qcross及原数值容差。

若后缀原门失败，原102支持结构不能改变该后缀几何，故这个纤维不能修复该必要门。本范围立即记录fixed-suffix-excludes-this-numerical-fiber，**0solver**，保所有已付输入/失败字段与费用。不把这个有限原门观察外推成一般曲面无解或其它51/R0方向不可行；下一必须换真正几何问题。

若后缀通过，直接用同一已付完整初值进入下面的一个solver。没有额外的冻结复核任务，也不先单独运行后再免费恢复本次数据。

## 4. 原102坐标、固定约束行和完整两网值

后端103变量为102个直接物理前缀增量和一个非负phase-I slack。102坐标的剩余上下界直接来自准确原172盒；不另造一个小trust盒、改变物理缩放或切出不同reference。起点为已构造ring candidate在此纤维的零增量；初始slack从本次真实新原行违约计算，不能假定初点可行。

固定约束集由原58两池内真实metric/curvature行及s索引111、131上两网**整个角圈**的两metric、四PSD行组成。原池顺序保留、重复行按明确ID处理，不在这次求解中做自适应换池或重新启动。

优化阶段的selected行仅用于形成有限约束及解析Jac；**每一个新的后端物理点仍实际计算两张完整网格的非线性值**，保存原全域最大metric、曲率、最小面积及各原门真假。单独selected行通过不能产生候选。

解析Jac按原angular kernels/virtual selected jets、owned-radial批宽4构造，只开放原u前6×9/v前6×8，不展开fullgrid×102巨大张量。Jac只在后端实际请求的点构造，并分别记录started/completed/failed；240是不同新点value次数上限，不能写成所有点都已经付Jac。

同一字面点的已付selected值和Jac可缓存。每点保真实小selected输入以便首次Jac消费，初点的必要scalar输入及suffix保MODEL；其余fullbody大场只保最近实际点。若后来请求旧点的首次Jac，可新付必要小径向scalar上下文；不得重跑旧ordinary/U/T/fullvalue来伪造缓存。原计时和事件记录必须区分value与derivative。

## 5. 单一求解与真实候选资格

一次SciPy1.17.0 SLSQP，min phase-I slack，固定ftol1e−9，maxiter120，最多240个不同新点value，solver最长180秒且受总600秒剩余额度约束。原点/参数/固定行尺度、全部实际回调、失败、最后原raw103和完整OptimizeResult字段均按其原意义保存。

成功状态仅说明后端局部返回；它不证明准确全局可行或最优。非成功状态也不宣称整个102纤维不可行。没有换solver、换起点、重复同一问题或加大旧预算。

原返回的168候选必须与该raw点的已付全网值及确切坐标一致，保持全部冻结坐标逐位不变，准确重嵌原172盒。资格还要求完整两网实际metric下降至少1e−7、原曲率PSD/direct与面积门全部通过。原返回没有对应的真实全网summary时不得接受，不为了报告重新计算一个旧点。

若本次准备的初点已完整通过全网门，可直接作为唯一候选而不启动solver，仍不从旧free36环资格推定body合格。合格后才调用至多一个原actual pair。原十四门包括全部支持/镜像/cap/metric/curvature等条件；没有通过预测就免去十四门。两网原actual接受且准确172盒真，才记录59并输出同一ordinary已付selected二jets与U/T cache。未通过时accepted index仍58。

本次不新增全body曲率“目标值”来替换原58验收cap。末环继承的低曲率和整面最终reach是不同义务；主README仍需以后全域、全时间曲率与非局部reach认证。

## 6. 完整账目、输出与真实停止范围

外层started计数限额：

| counter | 上限 |
|---|---:|
| fixed_metric_evaluations | 1 |
| prefix102_model_builds | 1 |
| new_body_input_preparations | 1 |
| fixed_suffix_checks | 1 |
| prefix102_solver_sessions | 1 |
| actual_trial_pairs | 1 |
| actual_grid_values | 2 |

所有内部scalar/frame/Pi/selected-J/新点value及失败由module同时保实际次数/时间，与外层同钟。它们不在祖full ordinary值147上伪增，但也不称免费。只有原actual ordinary另增原full值；model新值/导数的次数独立明列。内层事件时间不重复相加到最终clock。

MODEL保存本次必要输入、固定后缀二jets及原门值；SOLVE_TRACE保存raw103历史、原selected残差与全域summary、初始和最后实际已付Jac及真正partial。完整大数组的具体保存范围见[module合同](true58-fixed-ring-prefix102-model-contract-20261116.md)。已释放的成功中间大数组明确不作后继免费输入，原返回若对应已释放数组也只报告实际保留的summary，不重算。

科学stdout上限256MiB。stdlib observer只读一次已完成research日志，raw cap320MiB、语义输出8MiB；对大数组保原dtype/shape/hash而不重做数学。真实完整科学输入、输出只在原Actions stdout和临时runner；不上传artifact/Release/cache，不把payload写Git。所有大输出与COMPLETE flush后，FINAL_CLOCK给权威新费用，未用余额关闭。

workflow仅在新request推送触发，先真实pull两仓、核根/题README和私有QUEUE元状态，变更则按差异先执行新规则。报告job也真实pull。新源manifest保原337源hash，绑定本次全部新module、包装、合同、设计及request祖身份；令牌不进入科学进程或源文件。

## 7. 完成后的衔接

本次范围的任一返回都会记录真实状态、原源身份、费用及限制，并继续open。后缀失败则研究能改变后缀的低阶控制；solver失败则按已付全域与原行结果确定新的几何问题；真accepted59也仍须继续把同g误差降至主阈值，并付连续全域全时C²嵌入、非局部reach、宏观握持位移和完整网格展示。

该有限计算的600秒是本范围的费用边界，不是主课题停止条件。
