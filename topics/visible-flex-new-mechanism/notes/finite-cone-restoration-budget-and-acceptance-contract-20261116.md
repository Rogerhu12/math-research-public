# 有限 Lorentz 主模型：最新 checkpoint 恢复、独立费用与原验收合同

日期：2026-11-16。状态：**完整静态合同；未执行新开发、几何、J/JVP、LP 或锥求解。最新入口已由根读取的 terminal-paid-slot 实际回执确定；新算法资源上限已由根按§8.1明确冻结，源码/请求待审，尚无执行。** 本文先按原任务真实结局选取 source，不把算法预期写成观测。

本文落实 [有限锥数学设计](finite-cone-affine-metric-design-20261116.md)，只改变原 metric 仿射范数的有限主模型求解方式。原物理数据、完整两网、曲率与几何验收继续由冻结实现定义。

## 1. 真实问题及本次新机制

旧完整两网 affine-e/f 模型已用有限单位球法向切面作为 LP 松弛。某些 primary 在可用内层调用数结束时仍存在显著 epigraph gap；此时成功的松弛 LP 不等于完整仿射模型的下降方向，更不能称数学驻点。原末槽接口现已真实消费第64次 LP，见下方实际入口。本文不把它重新命名为新预算中的一次免费调用。

拟议新机制对一个实际原行/分支同时加入其整个 Lorentz 范数约束，避免在同一行上逐个增加方向。原两网完整 oracle 仍查找尚未纳入的原行。所有现存原线性约束与法向支持均保留，首次实现不删除所谓“被锥蕴含”的旧行。

这一变化是仿射 proposal 算法的变化，不是新几何自由度、放大 trust cap 或放松实际门。固定 g、b0、永久锚、159→163 映射、两网及原 target、epsilon、曲率阈值均不因此改变。

## 1.1 已收到的真实末槽结局

根从唯一原日志读取的来源是 [run43789033043](https://github.com/Rogerhu12/math-research-public/actions/runs/43789033043)，job133043031523，source `a08ed9fb3bd44ece17befa23651b281e67f6bb1b`。本稿只消费根传回的已付字段及冻结源码，不另下载原日志。

| 原对象 | UTF-8字节 | SHA256 |
|---|---:|---|
| 原stdout | 2957208 | `a465b5f6b09de317c8b9b541953171968543e91f3de3ad52ae4bac9e6dc5f8c0` |
| 原MODEL JSON+LF | 146427 | `1d449ca76a8706ab0481b51b91c21d23d01cd2645124036dba205755ba638609` |
| 原COMPLETE JSON+LF | 2682421 | `af48ff341b831df4ce24038b33aa2153161fa8f5da7a2d0387f29b042123c45b` |

实际有1次新primary、0次新SOC；原累计64次为63primary+1SOC。4次新value是恢复两网与一次完整alpha1 trial的两网，累计62。两网各14门全真，但候选的fine eta比原接受点更差，真实两网gain为 `-2.391806995405421e-6`，并学习1条coarse soft行。因此原实际分支返回最后接受点，未接受新候选。

最新完整恢复入口据此为：

- accepted index27、physical SHA `bff1348df63200e43bb720e98fa359b057e7370dfbc2090095ba2800803f173c`、两网 eta `0.26610226672562226`；这次保留27是实际结论。
- coarse/fine pool为4439/4533，版本8/6；必须使用新pool，不能回到原MODEL28的4438/4533。
- B为0.000125，两streak为0/0；不重置回原MODEL28的0.00025。
- bank为512，state SHA仍 `3d674785e4f46a8a5489ab49e6ff7de20d889eec92e4c7a6776ece452acf1611`；独立旧supplement及新prepared-support provenance仍须完整消费。
- learning为36events/35commits/pending0；gamma为coarse `43.39425351670855`、fine `44.0738041005123`，state SHA `44eb8308c6ee5b2c1ab3b73951f6f111a5a5a7423636ea7a132b19b53003b00d`。
- 最终science累计 `356.129820261` 秒，本次增量 `85.071541299` 秒；process为 `86.310207106` 秒。checkpoint自身较早的 `356.127966801` 不能替代最终COMPLETE总钟。

这次新候选exact159未成功写入公开语义输出：wrapper只在 `evaluated(step)` 捕获，但冻结 `_candidate` 调 `slack(step)`，单次末槽没有进入下一轮cuts的 `evaluated` 路径。raw model里的exact step又被旧semantic selector摘要；learning只存方向/点SHA与norm。不能为补失值重跑第64次 LP，下一方法不得依赖这个未知向量。已付attainer、原行和exact unit normals可继续作为支持来源，不能宣称重构了未知候选或其接触点。

新 finite-cone 初始物理缓存仍须在本次runner按上面最新接受点构造；其输入点虽不变，pool/controller/learning已经改变，必须建立新的完整模型binding。新机制能减少同一行的方向松弛，但不保证消除这次实际非线性偏差或新soft行问题。

## 2. 唯一恢复源由最新实际回执决定

执行请求必须提供以下明确且互相一致的输入；任何一项未绑定均不得进入新科学：

1. 当前 terminal-paid-slot 最终 run/job/source 与原 raw log 指纹，以及 REQUEST、COMPLETE、必要 MODEL 原 JSON+LF 指纹。
2. 完整 future checkpoint；若最后入口只产生失败回执而没有新 checkpoint，应明确引用最后一个仍有效的完整 checkpoint，并另行合并其后所有真实失败成本。不能以 failure 的标量摘要伪造完整 checkpoint。
3. 最后真实接受点 exact binary64 independent159、完整 physical163、原 reference163、九物理 height/null 定义与原精确 coupled box。
4. 全 coarse/fine row ID、原顺序、版本、history、容量；不得通过重新 initialize/expand 偷换池或丢掉已有行。
5. 当前 bank 的有序 entries/context/hash/counters；独立 supplemental 支持的完整列表及来源；terminal-slot 新的 prepared-support provenance 若实际存在，也应读取。
6. curvature learning 的 coefficients、maximizers、events、commits、pending 与 migration lineage；实际 controller 的 B、legacy streak、covered streak。
7. 原已执行全部科学、value、primary LP、SOC、失败入口和准备成本；旧开发回执只读复用。

若末槽有新接受，只能从那个最新点开始。若无新接受，继续最后真实点，同时保留末槽实际候选、支持信息及费用。未保存的旧 proposed step 或历史 exact vectors 仍标记未知；不由标量轨迹猜造。

这里不要求未来 source 仍有512 bank、4 supplements 或 pending0。应按最新真实 checkpoint 的精确内容恢复；原末槽准备的新支持可在新中心重新成为合法支持，不能因它未存入 bank 就丢弃。若某项缺少足够可恢复字段，应先指出缺口，不重跑旧优化寻找同一状态。

## 3. 三种身份必须分开

### 3.1 物理身份

下列内容应按最新实际 source 核对：固定 g/b0/锚、完整 reference、坐标映射、物理 exact159→163、完整两网、原 primitive order、null-height 物理定义、精确盒及 gate 数学定义。新有限锥算法不改变它们。

必要 ordinary 两网评价只调用当前 direct-reference adapter；结果与 source 已保存 scalar/gate 收据按原容差比较。该比较不是未保存旧几何数组的 hash 核。两网缓存应在同一 runner/object 上立即供 selected J、observable factories、完整 oracle 和下一实际 trial 消费。

### 3.2 数学模型身份

对每个新模型冻结并记录：

- 当前真实中心与物理 SHA；
- coarse/fine grid 定义、所有 selected row ID/顺序/版本；
- 原 scalar A/b/c/lower/upper、step_scale、原 guard 的 frozen gamma/targets；
- selected e/f/de/df 的原数组摘要与两网 cache binding；
- 两 observable factories 完成后最终 complete-model/oracle binding；
- 所有保留支持的来源、重建后的 A/b 摘要；
- 本轮新增完整锥的原 grid/row/branch、observable 摘要与模型归属。

若只是 solver policy 改变，而这些数学域全同，不得伪造它们发生了变化；反之，也不得用一个新 schema 名字豁免实际不同的坐标、pool 或导数。

### 3.3 求值/策略/资源身份

新 solver、版本、参数、调用预算和报告域有自己的 policy。不得宣称它们的完整哈希等于旧 objective policy。

原 bank 的 context 包含 factorization SHA，learning context 还包含 cfg 与 norm-context SHA。因此是否能逐字恢复 context，要对真实新定义逐字段判断。若只显式 solver policy 变化且未进入这些域，可保原 context；若资源字段进入 factorizer/cfg 哈希，则需要准确 migration receipt：

- 原物理字段、epsilon、网格、坐标、尺度保持；
- 每个旧 normal 仍是原单位球中的合法向量；
- 在新中心/新模型用真实 e0/f0/de/df 重新组装支持；
- 旧 events 与 commits 保留其原 context 和原 hash，不改写成“本来属于新 context”；
- 已提交的 gamma 可作为同物理原单位 proposal 经验值迁移，但它不成为跨中心严格误差上界，也不重新训练旧事件；
- 未来 pending 事件只按原下一模型提交规则消费一次，不能在恢复时任意新增 commit。

## 4. 161变量的原数组合同

准确原 primary 变量为
$$
x=(z_1,\ldots,z_{159},\rho,h)\in\mathbb R^{161},
\qquad p=\operatorname{diag}(s)z.
$$

这里最后的 h 是原 LP 范数辅助量，不是几何 height。原 correction LP 的322维合同与这个 primary 不同，不能混用。

冻结入口为原 `primary`、其 `CompleteGridAffineModel` 及所有保留支持。实现应核：

- `primary is model.primary`；
- `A.shape[1] == len(c) == len(lower) == len(upper) == 161`；
- `step_scale.shape == (159,)`，有限且严格正；
- 原 c、有限上下界、所有 original rows 和 guard RHS 逐项保留；
- e/f 是当前值，de/df 是物理159导数，组装时只乘一次 step_scale；
- original soft branch 只为 group0/1；原 flat row 必须是该真实 grid 的合法 integer ID，不能先强转 float 再装作 integer；
- 不把 selected scalar-function index 与完整 oracle 的四个 maxima index 当作可固定的原网格行。新增锥必须落到其真实 attainer 的 original row。

可以用已存在的 selected-point e/f/de/df 复用当前导数；缺失原行调用原 `oracle.original_row`，其实际行 J 时间/缓存计入本任务。不得把旧中心的 dense J 或旧 A/b 作为新中心数组。

## 5. 锥组装与原单位残差

原 branch 为
$$
\phi_\sigma(e,f)
=\frac{\sigma e+\sqrt{e^2+4f^2+\epsilon^2}}2,
\qquad \sigma=\pm1.
$$

设 $d=d_e\operatorname{diag}(s)$、$g=d_f\operatorname{diag}(s)$。单行锥为
$$
b_i-A_ix=
\left(2(\eta_i+\rho)-\sigma(e_0+dz),\ e_0+dz,\
2(f_0+gz),\epsilon\right)\in\mathcal L_4.
$$
准确系数是
$$
b_i=(2\eta_i-\sigma e_0,e_0,2f_0,\epsilon),
$$
$$
A_i=
\begin{pmatrix}
\sigma d&-2&0\\
-d&0&0\\
-2g&0&0\\
0&0&0
\end{pmatrix}.
$$
各锥的最后一列为0，原 norm 辅助约束和 c 不删。当前原 soft target 相同，仍应从原模型读取；不把 curvature proposal guard 混成 metric target 的新常数。

原线性约束 $Ax\le b$ 以 nonnegative cone 保留。每个有限 upper/lower bound 转为相应一行不等式；无限边界不生成错误的有限大数。目标采用原 c，二次矩阵为零，不添加正则项改变原模型。

对一个实际返回向量，设 $(t,q)=b_i-A_ix$。保存有符号
$$
r_i^{\rm cone}=\|q\|_2-t,
\qquad r_i^{\rm metric}=r_i^{\rm cone}/2
=\phi_\sigma(e,f)-\eta_i-\rho.
$$
报告可以另给 positive violation，但不能丢原有符号值或把负舍入裁剪成“数学零”。求解器的归一残差和 tol_feas 不能替代上述原 metric 单位判断。

锥组装采用 Clarabel 官方的 $Ax+s=b$ 约定、CSC 数据、NonnegativeConeT 与 SecondOrderConeT(4)。只用其直接 Python API，不引入另一建模层。版本与全部设置须在实际请求冻结，当前草案接口按根已审候选0.11.1设计；没有安装或调用该库。

## 6. 有限选行与完整 oracle 的合同

首次 finite cone set 应按明确规则从当前 selected soft rows，以及实际已保留 bank/supplement/paid-attainer 的原行集合建立。重复同一 grid/flat branch 只建一个锥；已有支持行本身全部继续保留。不能把“4个 maxima”误称4个覆盖全网的固定锥。

每轮调用后：

1. 若 solver 没有允许状态的有限161向量，按具体状态返回；不能以 success 字段推物理可行。
2. 重建实际物理步 p，保原 h/rho，核原 linear rows、bounds 和每个已纳入锥的原单位残差。
3. 对 p 调一次原完整两网 affine oracle。其扫描费用、缓存命中、真实 attainers 和必要 row-J 分开记录。
4. 使用原 `_candidate` 的完整 slack、rho 上调与原残差门，形成可比较的修复候选。
5. 若有原规则允许的真实正模型改善候选，交原实际 trial 验收；不能把 solver 目标值直接作为实际改善。
6. 若 epigraph gap 未达且本轮仍获明确后继额度，按当前真实 violating attainers 增加尚未纳入的整行锥。增量必须是新原行，而不是重新对同一个原行生成另一个单位方向。
7. 如果 violating row 已在 cone set 中，先记录该锥的原单位残差/solver tolerance，不能重复加同一锥掩盖求解或单位问题。
8. 达到额度、没有新行或没有允许候选时，保最后真实接受点与准确停止理由。有限浮点求解不授全局数学驻点。

一个模型内的中心、targets、gamma、A/J 和 binding 不变，因而较早已按完整 oracle 修复的 incumbent 继续满足后来加入的合法锥；这只在相同冻结模型内成立。换中心或 guard 后必须重建，不把旧 incumbent 的可行性借到新模型。

## 7. 直接复用原修复门，保留三个不同量

原 `frame_metric_affine_spectral_model._candidate` 准确执行：

- $\rho_{\rm full}=\text{model.slack}(p)$，这调用完整 oracle；
- $\rho_{\rm aux}=\max(\rho_{\rm full},\rho_{\rm solver})$；
- 返回变量 $(p/step\_scale,\rho_{\rm aux},h_{\rm solver})$；
- 对全部保留原 linear rows/bounds 重算 residual/objective；
- gain 为 $\rho_0-\rho_{\rm full}$；
- raw gap 为 $\rho_{\rm full}-\rho_{\rm solver}$，gap tolerance 沿原函数。

锥 adapter 向这个函数提供准确的 `normalized_step_norm` 与 `predicted_metric_slack`，并将来源标为新 conic solver。它不得伪造 HiGHS success 或旧 LP 调用。

必须分别报告 solver rho、完整 affine rho、上调后的 rho_aux。即便 solver rho 非最小或高于 fullrho，也不能擅自用 fullrho 改写原辅助变量；原函数的 max 保持。原 linear residual 与新增 cone residual均在修复后核；原 full-affine gap 超容差但有允许的修复正改善，仍须明确 inexact，不自动删去原允许候选分支。

新代码不复制另一套实际 geometry/gate/strict descent。实际 trial 仍检查同一完整两网各14门、原 coupled box、固定 g/b0、合法物理位移及严格 metric 改善。需要 backtrack 或 SOC 时也必须由后续明确 outer 合同调用原路径；本文不给新 SOC 免费次数。

## 8. 新独立账，不能复活原64账

原 direct task 与其末槽的完整累计账必须封存为 ancestor。最新实际回执决定它是否为63或64次，不能先填预期值。两次/更多入口失败时间已经包含的部分不能再加一次；process/import/development 与 scientific 的交叠必须明示。

新算法按§8.1的明确独立预算执行；以下字段缺一不可，没有隐含默认值，最终请求必须逐项一致：

| 字段 | 含义 |
|---|---|
| new_scientific_seconds_limit | 本次输入读取前起的新科学墙钟上限 |
| max_new_solver_calls | 新所有实际 solver 调用总上限 |
| max_new_cone_calls | 其中 conic primary/可能修正的上限 |
| max_new_legacy_LP_calls | 如批准使用原 LP/SOC，其独立上限 |
| max_new_actual_values | 新 coarse/fine ordinary 实际调用总上限 |
| max_single_solver_seconds | 单次实际 solver 时间上限 |
| max_cone_calls_per_model | 同冻结模型最多锥调用数 |
| SOC_reservation_policy | 是否预留、如何消费、无使用时如何记录 |
| allowed_candidate_statuses | 哪些原 solver 状态允许进入原残差与完整oracle检查 |

solver 总调用数等于 cone 与 legacy LP 两类调用之和。legacy LP 若含 SOC，还须分 primary/SOC。锥的 library 名字不能让它变成“0次 LP所以免费”的优化调用。每次调用在 backend constructor/solve 启动前入账；constructor 或 solver 异常亦算一次 started call。组装/J/oracle/行查找的时间计科学钟，但不是一个凭空 solver 调用。

原值计数按实际 coarse/fine分别收费；cache命中保持原规则，不把已开始未返回的工作伪记免费。单次非抢占调用返回后超过墙钟时，记录实际超额并退出，不能称“上限内完成”。

完整累计费用至少分三层：

1. 早先已关闭的原 epoch 历史；
2. direct task +末槽的全部真实历史；
3. 本次新 finite-cone task 的 input/prepare、ordinary、J/row-J、assembly、solver、full oracle、actual trials、report各段与总科学钟。

资源字段若必须写入 cfg，逐字段列旧值/新值并更新真实新定义。不得继续沿用旧“所有预算未变”标签描述一个独立新预算，也不得因此修改数学/gate参数。

## 8.1 根冻结的新预算与原全局余量取交

本次明确执行额度如下。这是新 finite-cone 方法的预算，不是原64-LP任务的延长；原HiGHS账64=63primary+1SOC封存。

| 请求字段 | 冻结值 |
|---|---|
| new_scientific_seconds_limit | 1200 |
| max_new_solver_calls | 32 |
| max_new_cone_calls | 32 |
| max_new_legacy_LP_calls | 0 |
| max_new_actual_values | 96，含必要恢复粗/细 |
| max_single_solver_seconds | 10 |
| max_cone_calls_per_model | 4 |
| SOC_reservation_policy | none；本次无legacy LP/SOC调用 |
| allowed_candidate_statuses | Solved、AlmostSolved；均仍须原残差/完整oracle/真两网验收 |

冻结 Clarabel 0.11.1，max_iter=200、max_threads=1、tol_gap_abs=tol_gap_rel=tol_feas=1e-9。每次time_limit取10、新科学钟余量、原全局科学钟余量三者最小值；其它有效settings连同实际包版本在原结果完整记录。AlmostSolved的降低精度标签不能豁免原单位门；不以backend返回有限向量自动接受。

原cfg64/160/1800/10及其SHA逐字保持。新outer不进入旧LP/SOC调用门，不复活64余额；另记新conic次数及所有求解器总次数64+new_conic。原objective全局value从62起、全局科学钟回溯最终356.129820261；同时检查原value160/science1800和新96/1200。故本次value额度比原剩98更紧，科学额度也比原剩余更紧；非抢占超额实际保费用后退出。

新科学钟在读取任何恢复输入前启动，输入读取、准备、冷geometry、J、assembly、solver、完整oracle、trial及报告都按合同计费。新必要开发/API检查另列其实际费，既有11/9只读复用，不重做。

原field/factorizer/coordinate/grid/width/cfg均不变，bank memory context和learning immutable context逐字段核原值恢复；objective evaluation definition保旧数学字段并显式追加finite-cone method身份，完整objective SHA因此真实改变。新factory建立实际新model/oracle binding。旧events/context不改标签，最新gamma/pool/B继承；不得为了沿用旧hash掩盖完整方法变化。

新返回solver向量直接保存exact159，在任何status、wall、residual、oracle筛选前捕获；最终semantic报告必须原样保该记录，保存成功布尔由记录是否存在导出。旧LP64丢失向量仍标未知。

## 9. source freeze、首次检查与输出

首次执行前，应按最终源码接口固定最小新开发范围：

- 新锥符号、step_scale仅一次、两分支与原单位半残差；
- 保留原161变量、原线性/bounds/objective及旧支持集合；
- 新调用账在constructor/solver异常前已记录、独立cap/clock不借旧64余额；
- 新返回向量桥接原 `_candidate`，保 rho/rho_aux 与完整oracle、后续cone约束的冻结模型范围。

这是覆盖新接口的必要范围，不重跑旧 geometry、9/11开发、旧谱闭式或旧优化。准确组数/case数只能在新源码与fixture写定后给出，不先报 passed 或预定为已付。

标准输出保原 source/manifest/包版本、每轮 solver status/time/原残差/gap/actual gain、所有新14门、费用、停止原因和完整最终可恢复 checkpoint。密集A/J、原日志与可重算payload不入Git/artifact/Actions cache。必要small support provenance、source IDs和精确normal可随原结果日志保留，以便下一次只读恢复；这不授权跨run存科学数组。

当前冻结此合同、§8.1显式预算与待审 adapter；outer/transfer/audit/必要新接口检查及唯一请求仍待完整静态核读。恢复源按§1.1最新实际checkpoint绑定，最终原回执逐字段核，根统一公开调度；合同发布本身不表示实际通过。

## 10. 原接口来源

- [frame_metric_norm_direction_memory.py](../scripts/frame_metric_norm_direction_memory.py)：`support_row`、`memory_context`、`NormDirectionBank.rebuilt` 与原started-call账。
- [frame_metric_affine_spectral_model.py](../scripts/frame_metric_affine_spectral_model.py)：`AffineSpectralModel`、`_cut_lp`、`_candidate`。
- [frame_complete_affine_metric_oracle.py](../scripts/frame_complete_affine_metric_oracle.py)：真实原行、完整四maxima、step/JVP与attainer绑定。
- [frame_metric_direct_reference_epoch.py](../scripts/frame_metric_direct_reference_epoch.py)：直接求值身份、独立supplement与已有learning迁移。
- [frame_metric_terminal_paid_slot_transfer.py](../scripts/frame_metric_terminal_paid_slot_transfer.py)、[resume](../scripts/frame_metric_terminal_paid_slot_resume.py)、[recovery](../scripts/frame_metric_terminal_paid_slot_recovery.py)：已完成的末槽源、费用与边界；当前结局准确为64LP/62value/accepted27，不采用其入口未完成时的旧状态。
- [Clarabel官方Python入口](https://clarabel.org/stable/python/getting_started_py/)与[官方settings](https://clarabel.org/stable/api_settings/)：仅核API/状态/矩阵约定；未运行library。
