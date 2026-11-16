# 接受54的全新原约束模型、逐新行交换与首个真实下一点

日期：2026-11-16。主课题未完成。本设计承接[真实接受54](true53-four-cut-exchange-first-actual-accepted54-20261116.md)，只准备这个新物理点的必要模型和新方向；不是恢复已关闭的53模型任务。本文的源码工作均为文本，没有本地导入、编译、开发验证、求导或求解。唯一科学入口为本公开仓库 Actions。

## 1. 当前真实输入及关闭的祖先

唯一源run43827509699/research133164733399，source
513aa99d7c361bb67dbc1d04e32f3d563fe6b1b9，workflow
visible-true53-augmented-master.yml。原raw58360528 B /
SHA256 5e7c358eb5b11db5ebb6eaf4551bec80079e3b443615daf001d846597d985701。
只读同一原stdout的COMPLETE1、CACHE2、FINAL_CLOCK1，精确bytes/SHA在request与transfer常数中。

真正接受点54的physical身份为
c0214406cebe6f39eda0b11fa2db5fecb883d9323c696005447427b39410f253；
η粗.2660119435311364、细.26601238103375724，κ细57.99930616102216。
原两网14门全真，但η不是δhold，.26目标、主reach与连续门未付。
池4453/4549、版本14/14，B=.00025、streak0/0；
完整bank、guard learning及被动controller以原checkpoint为准。

原全部祖先的最终权威费用为1877.294171609秒、130普通值；
含53任务两次失败和最终五轮新行交换，53任务合计218.31438091800004秒。
这些任务全部关闭。旧HiGHS64、cone32、Hildreth、原53有限问题/方向/J不得再执行。

## 2. 为什么要付新的两次普通值

已付CACHE2的U/T/e/f/radial/theta是实际54的原普通缓存，完整绑定
0beeb7463fdf2cef41449f653a84153688491b1b9da201b8f777b1181471ec73。
它没有positions、curvature、完整二jet及Jacobian。
原全部硬约束及SelectedMetricObservables的ordinary binding需要这些数据，
不能用旧53硬J冒54，也不能声称已付cache含它没有导出的数组。

因此新任务允许**两次且仅两次必要hard-model普通值**，粗/细各一次。
其内部连带计算U/T等工作计入实际费用，不虚称为零。
这两份fresh ordinary值同时作为primary、selected-J、e/f基线与完整JVP的唯一基线。
CACHE2只读回并保其已付来源，不将其数组和新primary混拼成双基线。
不另外重放源54的接受决策或初/末独立geometry审计。

固定原g、b0、159→163坐标、永久enriched reference c0、全部原配置不改。
原cfg中的160次/1800秒只作为关闭祖先元数据保留；
新Fresh54Ledger拥有自己的单一600秒，不靠改旧cfg伪装预算。

## 3. 新模型与十九个种子

粗/细各一次原selected-J，包含该点原池全部硬行与metric软行；
不是仅取极值少数行。第一jet上下文各一次，保原primitive、角算子和null高度。
原physical163盒、耦合物理范数、hard targets、frozen guard和原容差保留。

同一COMPLETE中原53最终master提供19个额外metric标签：
初始5个加后续14个。只继承grid/group/flat_row_id/有理坐标；
旧梯度仅留来源hash，数值不复制。
每个标签在54重新调用原metric_row：
若已在当前selected-J，使用这份新54梯度；否则只求新54单行导数。
标签与selected-J去重，不重复付同点同一新行。

输出一个原MODEL，含完整selected-J/软梯度、原硬域、e/f、
19标签及新seed梯度。求解后新增的attainer梯度逐条输出原记录，
不需要再打印整MODEL。

## 4. 原单位有限问题及严格新增行交换

变量为159个z、物理无穷范数h及正尺度gain γ，
物理位移p=.001*qscale*z，实际gain d=.001γ；
μ=1e−6，target=.26。原约束为：

- hard：−Jhard p + hard_h*h ≤ base−target，原1e−7容差；
- 原±K物理盒、±K−h范数行，以及原160个外界上下界；
- 每条原metric梯度g：g·p+μh+.001γ≤φ0−φbranch，原1e−9容差；
- 原target常支：μh+.001γ≤φ0−.26。

硬行数、全selected软行数由当前54模型读取，不沿用旧2937/5743/9658
作为不变数学假设。所有原行完整装入，未删除或软化硬门。
每次有限解后，以实际浮点加法得到候选、再减回真实rounded159位移，
检查原163准确盒与原hard域；随后一次完整双网JVP分离。
metric最终gain重新用全网四支最大值和真实范数计算。

若方向合格，转原legal line；若不合格，只追加尚未有的新原attainer行，
再解严格变化的有限问题。同一矩阵binding只能尝试一次；
无新行即停止这个固定有限目标，不冒不可行、驻点或一般无下降。
最多32个全新finite问题、32次完整双网分离、147个新单行导数；
147=19种子上界+32轮每轮四支。
每问题原predictor/corrector代数保96迭代/192系统，整个任务3072/6144。
没有HiGHS、cone、SOC、Hildreth、正则化或后备solver。

## 5. 同一个方向的原legal line与actual门

只使用末个合格rounded方向已付e/f/de/df。
原hard和physical163盒给准确及原容差legal α区间；
α=0始终是原物理零基线，不能拿正下界冒作零。
原62次搜索查询和至多2次实际fallback查询共64次、一个session，
不为scalar重做JVP或普通geometry。

实际候选最多3个pair/6个普通值。依次使用所选α、
再向合法下界二分两次；每次先付准确163盒/真实roundedhard域，
再按原regularity决定是否做fine，原14门及最小η下降1e−7不改。
实际几何只承认原两网通过且严格下降的点，
下一接受编号才是55。任何未通过的trial新增行都按原value-only学习记录；
若需要新行，该固定方向就停，不能用旧J/guard继续猜接受。
bank/γ/控制器及learning保持被动来源，不凭新lp反馈重训。

接受时直接从这次真实ordinary内存导出新点U/T/e/f，
不重做geometry/JVP，也不把direction预测当实际缓存。
完整checkpoint保全部原信息；若无新接受，实际选点仍为54。

## 6. 唯一新账与原输出

单调时钟从Python科学imports和输入读取之前开始，单次新分配600秒，
包括源日志/24输入恢复、普通值、selected-J、firstjet上下文、新行、
finite迭代/系统、scalar、实际trial、失败、复制/hash与全部输出。
任何越时或失败如实记started计数；后续若需修复，不剪去本次已付费用。

| 资源 | 新上限 |
|---|---:|
| 必要hard-model普通值 | 2 |
| selected-J粗/细 | 2 |
| firstjet上下文粗/细 | 2 |
| 完整双网分离 | 32 |
| 新metric单行 | 147 |
| 严格新finite问题 | 32 |
| finite迭代/系统 | 3072 / 6144 |
| scalar session/查询 | 1 / 64 |
| actual pair/普通值 | 3 / 6 |
| 数学stdout分配 | 112 MiB |

祖先130值与新model/actual的debit和实际geometry started分别报告；
最终FINAL_CLOCK晚于所有大型MODEL/cache/COMPLETE输出，是新的权威累计。
原父事件嵌套计时不重复相加。源54grand total加这个新时钟才是新累计。

科学结果只在原公开stdout与runner临时文件；Git只存源码/参数/
run/SHA/人读结论。read-only report单次读原research stdout，
不装数值库、不执行model/solver；只选原字段、bytes/hash和明确省略信息，
不重新求值或修补结果。MODEL/cache原数组保持在原research日志。

## 7. 规则与完成边界

每个workflow的research/report都先真实部分clone/pull main，
比较根/题README，空diff记已读SHA，有改则只读差异并按新规处理；
同次私有QUEUE核本会话唯一进行中，凭证在科学入口前移除。
root独占refs/push/Actions；非快进必须实际pull --rebase后续推。

本任务得到更低η或新的有效方向都只是必要推进；
不能代替同一g下1e−6且精化收敛、整域整时reach、宏观无对齐位移、
材料握持及真正C²闭嵌入连续族。未满足主README的所有完成门时继续open。
