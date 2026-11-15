# 完整两网模型已覆盖的软行学习：普通步增长计数设计

日期：2026-11-15。状态：原源码只读推导及新实现合同；没有执行新的人工检查、几何评价、LP、J/JVP 或科学阶段。

建议文件：notes/complete-model-covered-soft-ordinary-growth-design-20261115.md。

责任与分工：tail_cost 负责本设计及随后三个独立新源码；root 负责审读、输入转移、audit、request、workflow、refs 和唯一公共 Actions 调度。所有已发表源保持冻结，本稿不授权回放上一阶段。

## 1. 已有证据与本次唯一改动

本设计从已完成的 run 43758666042 / job 132948276657 / source aca67097b60b7eacdcf20798395ce6d4d1ab2845 的真实 future_direct_checkpoint 继续。完整结果见 [首实际结论](soc-pair-reservation-first-actual-result-20261115.md)，该稿已由 root 发布为 commit 13186d2ffc65f1d1aa69a3b8ab4b89ad061b4b86。

本轮七个模型均在第一次完整普通步接受。原始共享预算实际启动 11 个 primary LP、0 个 SOC LP；剩余 1 个 LP 因新 pair-allocation 规则停止，未称原 12 个额度耗尽。七模型全部保留原门、真实学习及完整模型预测。以下五个模型的旧 conservative_growth 检查只有同一个 false：

| 模型 | 完整实际/预测比值 | 新 coarse/fine 行 | 旧 growth 的唯一 false |
| --- | ---: | ---: | --- |
| 1 | 0.988581908914915 | 5 / 1 | no_new_coarse_or_fine_rows |
| 2 | 0.863831201141653 | 5 / 0 | 同上 |
| 3 | 0.8966608218205857 | 1 / 0 | 同上 |
| 5 | 0.8838295384584869 | 1 / 0 | 同上 |
| 6 | 0.9977108268211448 | 1 / 0 | 同上 |

这些新增行均属于原 soft metric 两分支；两网 omitted hard rows 都是 0。模型 4、7 没有新行，旧 growth 各自合格，但模型 5 清掉模型 4 的成功计数。因此终态旧 success_streak=1，B 仍为 0.000125。这个观察指出一个可以准确改变的控制条件；它没有证明增加 B 一定提高下降量，也没有把未发生的 SOC 当作通过测试。

新规则只允许：一个已由原完整两网门接受的、质量足够高的普通全步，在真实新行全部是既有完整 affine-e/f 模型已覆盖的 soft witness 时，保留一个独立的普通步增长连续计数。新硬行仍立即使新计数失效。原普通步、SOC、缩径、接受与失败返回逻辑均不重定义。

本稿不扩大物理变量、步长上限、约束容差或任何 LP/值/时间额度；也不重新运行旧阶段以观察未触发的分支。

## 2. 原模型为何已经覆盖新增 soft witness

固定本模型的真实接受点 x，令 d 为试验实际浮点点 y 与 x 的差，而不是记录的未舍入名义提案。对于原 coarse/fine 两张完整网格的每个点 i，定义

\[
e_i(x)=\langle X_s,X_s\rangle-1,\qquad
f_i(x)=\langle T,X_s\rangle .
\]

原单方向 JVP 给出同一点、同几何、同完整角积分的线性形式 de_i(d)、df_i(d)。使用冻结的正 epsilon，两个原平滑分支是

\[
\phi_\pm(e,f)=
 \frac{\pm e+\sqrt{e^2+4f^2+\epsilon^2}}2 .
\tag{1}
\]

原 CompleteDirectionalMetricOracle 在每张网格上逐径向拥有行、完整原 theta 网格计算两个最大值。设原目标为 eta_star、原外域固定下界为 rho_out，则本模型的完整预测为

\[
\rho_x(d)=\max\left\{
0,\rho_{\rm out},
\max_{g\in\{c,f\}}\max_{i,\sigma\in\{-,+\}}
 \bigl[\phi_\sigma(e_i(x)+de_i(d),f_i(x)+df_i(d))-\eta_\star\bigr]
\right\}.
\tag{2}
\]

所以任意新学到的原 group 0 或 group 1、原合法 ID，早已属于式 (2) 的定义域。把该 ID 加入 selected 池不增加一个此前未参与式 (2) 的 soft 函数。该 ID 可以影响后续 selected 行、初始切面和实际学习；这些操作全部照常保留。

这个结论只关于完整有限网格的 affine-e/f 模型。它不声称真实非线性值已被全局上界控制，不覆盖未采样的连续曲面，也不把硬 curvature/strip/ball/mirror 行的学习解释成 soft 函数域不变。

浮点实现仍使用原链式重构容差和原 JVP/ordinary 接口。新控制不声称逐比特的数学全局范数证明，不产生区间证书，也不另放宽原 replay 容差。它只要求本次真实的完整 oracle 计算、原模型绑定和实际接受证据齐全。

### 2.1 必须使用实际 d 的完整预测

原 trial_quality 使用

\[
D_x(d)=
 \max\{0,\eta_{\rm true}(x)-\eta_\star\}-\rho_x(d),\qquad
R_x(d)=\frac{\eta_{\rm true}(x)-\eta_{\rm true}(y)}{D_x(d)}.
\tag{3}
\]

新资格必须沿用同一原定义：D_x(d) 有限并严格大于原 linear_model_improvement_floor，R_x(d) 有限且至少原 3/4。不能用 inner LP 的 raw rho、旧 selected-only 预测、SOC 的 y 处线性模型或名义 p 替换式 (3)。

当前实现已经在 actual_metric_error 和 trial_quality 路径计算式 (2)。新 witness 只读取该次成功缓存及报告，不额外做一次全网 JVP。若原缓存没有实际 d 的成功结果，新例外不适用，返回冻结控制器；不补跑计算制造资格。

### 2.2 repaired inexact 不自动失去资格

inner cutting-plane 是否达到 epigraph gap 容差，与实际返回点是否通过原 repaired rho、完整行残差和真实两网门是不同事实。本次模型 7 的 gap 未达到原容差，但返回的 repaired candidate 通过原残差和真实门，旧 growth 已判其合格。

新规则不额外要求 returned_epigraph_gap_met=true。它保留 returned_inexact_cut_model、原停因、raw LP rho、repaired rho、完整实际 d 的 rho_x(d) 和实际比值五者的区别。资格必须来自原已允许的返回点和式 (3)，不能由有限切平面下界直接授予。

## 3. 新 witness 的准确对象与时机

拟新增 OrdinaryCoveredContext，注册在本次 live objective 中，不从孤立报告的 passed 布尔值构造。

在原 selected_model 及 primary_observable_model 两个 factory 全部完成之后，保存：

1. 原 primary 对象及最终 CompleteGridAffineModel/RememberingCompleteModel 对象的引用；
2. 模型号、真实 x 的只读副本、原物理 x SHA、真实159到163坐标/映射与原盒宽度身份；
3. 最终 model_binding，包括两 factory 后的 radius_independent_model_sha256；
4. 原 coarse/fine pool versions、完整未过滤 selection.ids 的顺序及各 hash；
5. 两原 grid definition、原点数、完整 theta/radial 身份；
6. 完整模型 binding、oracle center binding、原 selected e/f/de/df 和原 scalar/J 绑定；
7. 原 model_B、target、epsilon、outside floor、source cfg SHA。

只在已经完成原学习、准备作 next-radius 更新时检查这个 context。不能把仍含旧 selected 标量签名的早期对象称最终绑定。

本次无 rebind primary factory；普通 accepted y 的 soft 学习不要求为增长控制再建一次扩大后的 J。旧模型继续以自己的原 pool versions 和 immutable selected 数组为来源；新增 IDs 只用来证明它们属于相同完整 oracle 的 soft 域。下一模型仍按原学习池正常重建 J、e/f 和切面。

### 3.1 原/新池的合法差

对于每张网格，令 I_old 为 context 保存的原 selection.ids，I_new 为学习后真实 objective.pool 或 objective.fine_pool。要求：

- I_old、I_new 都是无重复的原整数 ID；
- 全部旧 ID 保留，旧 ID 的相对顺序保持；原池不会被新规则删行、换 ID 或压缩；
- I_new 与 live objective 当前版本及顺序完全一致；
- DeltaI=I_new\I_old 的数量与 trial 中真实 new_coarse_rows/new_fine_rows 完全一致；
- 每个 DeltaI 的原 group = floor(ID / original_point_count) 都在 {0,1}；
- 每个 ID 在该原 grid 的合法范围内；不能将新网格、重编号、细网 ID 或输出标签冒为原 ID；
- coarse_omitted_hard_rows=fine_omitted_hard_rows=0；
- 原 capacity/learning 报告未报溢出，真实学习记录、added ID、omitted 计数、pool history 全部保留。

DeltaI 为空的普通步也可进入新连续计数，但不称发生了 soft-learning 例外。若任何新增原 group>=2，即使该行在当前 y 的真实门仍合格，新增分支也失效并将新 streak 清零；原控制结果保留。

不要求旧 pool version 与学习后 version 相等：它们本来就可能因真实学习而改变。需要的是旧模型正确绑定旧版本、新池正确记录新版本，以及两者间准确 ID 差。把这个检查写成“所有版本不变”会误拒本设计的目标情况。

### 3.2 完整 oracle 的实际 d 证据

要求 live context 满足：

- primary.state、oracle.state 与保存 x 逐字节一致；
- 原模型 final binding 与原 model record 一致；
- primary.affine_spectral_model 正是所注册的 complete 对象；selected 包装、oracle 和 memory 包装没有换成其他模型；
- oracle 的 source cfg、reference163、exact height reference、factorization、ordinary evaluation、两网和原 point count 与保存定义一致；
- 实际 y 从 trial 的 exact binary64 159 坐标读取，其 physical163 身份和原接受记录一致；
- d=y-x 有限，原 subspace.apply(x,d[columns]) 精确重现同一 y；不拿名义 proposed_step 作差；
- oracle.cache 中实际 d 的 hash 对应相同字节数组，且成功结果含两原网准确覆盖点数、四个有限最大值和同一 center binding；
- 对非零 d，其已完成 direction event 具有两网完整 owned-row 覆盖；不能以 started/raised 事件充数；
- trial 的 full_prediction_binding_sha256、accepted_base_total_step_sha256、complete_affine_four_maxima、complete_affine_smooth_slack 及 scale_feedback.prediction 指向这同一次结果；
- 式 (2) 的 outside floor、target 与原模型一致，式 (3) 的真实 eta 与两网实际决定一致。

array_digest 与 array_hash 等既有函数各自保原字节域；实现不能因为名称相似就跨域强比字符串。先比较真实数组，再在各字段自己的既有 hash 规范下核对。

新 controller 不调用 oracle.evaluate、original_row、linear_rows、evaluate、fine_decision 或任何 LP。缓存缺失只使新资格 unavailable。原 source/config 违约等已有 fatal gate 仍保持 fatal；新 witness 自己不能把这些原错误降级为成功。

## 4. 普通步合资格条件

每次先完整调用冻结的 next_expanded_layout_hold_trust，得到原返回值 (B_old,s_old,report_old)。传入的 legacy_streak 是独立保存的旧计数，不把新 soft-covered streak 偷传给旧控制器。

取 report_old 内原 conservative_growth 的检查。新的 ordinary 资格需要同时满足：

1. 只有一次 trial，kind=primary-metric-short-step，alpha_exact="1"，真实 accepted_as_next_iterate=true，结果为原 accepted-two-grid-true-metric-descent。
2. 没有 correction、SOC、arc 或 backtrack。
3. 原 complete_actual_two_grid_gates 为真，两个原完整实际决定、所有个别硬门、cap/box、原旧 metric 合格；原接受下降要求不变。
4. 原 valid_high_complete_ratio 为真，并由第 3.2 节的同 x 完整模型重认式 (3)。
5. 原 actual_step_uses_radius 为真；此外从真实 d 及原 subspace.M/width 读取实际 body-normalized 范数，要求有限且至少 (9/10)B。原 p 诊断仍保存，二者不混称逐比特相同。
6. 原 old_shrink_not_requested_or_applied 为真：传入 current_trust=B_before，原缩径规则没有触发，原前置拒绝没有降低 B。
7. 第 3 节的 live context、实际 d、原/新池差以及全 soft 覆盖证据全部通过。
8. 原 primary 返回点已通过原 finite primal、repaired residual/bounds、两网实际接受；不增加“exact convex optimum”或“gap 必达”要求。
9. 新 policy 明确安装，source cfg SHA 完全未变。

第 1–6 项保留原检查原值。第 7 项取代的只是“任何新行都会清 streak”这一部分，不编辑旧 no_new_coarse_or_fine_rows=false。旧字段仍 false，新字段明确说明为何不同的新增规则允许记一次 covered success。

全步使用半径的额外实际范数只读原矩阵、宽度和真实坐标差。没有新的方向、J 或几何评价；也不通过缩放矩阵、改度量或扩大容差使其通过。

## 5. 两个 streak、优先级和一次更新

保留两个 0/1 状态：

- legacy_streak：冻结旧控制器的真实输入/输出计数；
- covered_ordinary_streak：本新增完整覆盖规则的连续合资格普通模型数，尚未消费的值为 0 或 1。

入口沿真实 checkpoint 继承 B=0.000125、legacy_streak=1。covered_ordinary_streak 明确从 0 开始。不会回溯把上次七模型重新裁判，也不会把上次五次 soft 学习补算成既有成功；因此无旧科学或控制轨迹重跑。原末 legacy=1 不重置。

每模型的精确次序如下。

### 5.1 先取得完整旧结果

原冻结 next_expanded_layout_hold_trust 只调用一次，输入模型原件、原 current_trust、当前 legacy_streak 和完全不改的 cfg。保存完整 report_old，包括原17个 successful-SOC条件、expanded-layout hold 条件、原普通 growth 和所有触发索引。

任何 original curvature/poor-quality/rejection 缩径先执行。SOC retain 若原规则真实通过，仍返回其原结果。新增 ordinary 规则不撤销缩径，不把 SOC 步计为普通成功。

### 5.2 更新表

设 C 是第 4 节的新 ordinary 资格，n 是输入 covered_ordinary_streak。

| 情形 | 下一 B | legacy_streak | covered_ordinary_streak |
| --- | --- | --- | --- |
| C=false | 完整 B_old | 完整 s_old | 0 |
| C=true，旧规则本轮已消费合资格 pair（实际增长或 pair-at-cap） | 完整 B_old | 原 s_old（为0） | 0 |
| C=true，旧规则没有消费 pair，n=0 | 完整 B_old | 完整 s_old | 1 |
| C=true，旧规则没有消费 pair，n=1 | min(2 B_before,原mapped cap) | 0 | 0 |

最后一行还要求 B_old=B_before；否则新规则不可覆盖原结果。正常 C=true 已排除原缩径。新增 pair 在 cap 处仍被消费，记录 qualified_pair_at_cap=true，不假称实际增长。

“旧规则消费 pair”必须同时识别 grew_for_next_model 和 qualified_pair_at_cap，而不只检查 B 是否改变。这样同一个合资格模型不会被旧、新计数重复使用。任何实际增长或在 cap 处完成一对，均清两个未消费计数；未消费的一个 covered success 可以跨一次 soft witness 学习保留，但不能跨不合资格模型、SOC、backtrack、硬行学习或缩径保留。

这是两个明确状态的因果更新，不是对旧历史的 counterfactual 回放。旧报告中的 s_old 保持原值；若新增 pair 导致实际输出 legacy=0，则另字段说明“本次新 pair 已消费，实际下一输入清零”。下一次调用旧控制器只读取这个真实新状态，不冒称它是没有新政策时的旧轨迹。

### 5.3 原阈值和上限不变

本当前 mapped159 控制器实际使用：

- 连续两个合资格模型；
- ratio 至少 3/4；
- 实际 norm 至少 9/10 个 B；
- growth factor=2；
- B 最大值为 entry_tail159_maximum_body_radius_exact=1/4000；
- T 半径仍 B/8，H 半径仍 4B。

不能误用较早通用字段 trust_growth_maximum_box_fraction_exact=1/1000 替代当前 mapped cap。最小 B、原物理163盒、159坐标外包、固定总高与原所有容差保持。

## 6. 当前最优 checkpoint 的唯一入口

只消费本次完成日志内的 future_direct_checkpoint：

| 项目 | 准确入口 |
| --- | --- |
| source | aca67097b60b7eacdcf20798395ce6d4d1ab2845 |
| run / job | 43758666042 / 132948276657 |
| 最佳真实两网 max eta | 0.2663015219132816 |
| physical state SHA256 | 0c1d344dab070999d503e79243f2b946662f590f76f9dbffea8b97cbf56a9ad2 |
| 原 ordered coarse/fine 池 | 4432 / 4358 |
| 原 ordered norm bank | 59 entries |
| bank state SHA256 | 24cc1f35aca23a584999ff7544b4e961a0fad24e78270fa13aac3f65c9053c50 |
| B / 旧 streak | 0.000125 / 1 |
| 新 covered streak | 0，从未回放旧模型得到 |
| source cfg SHA256 | b4f83d6d2c59e97ea61e8f7d54a6f2f8ded263d2fab5f04df29492d08798fae6 |
| coordinate definition SHA256 | b37cadb78c9b9e70a6359bbf81d3debbd4089104ce5758105739c9278752a580 |

原 reference163、159 当前点、完整163物理点、59个有序 bank entries/context 和两完整池在 runner 内存恢复。原 bank 不重播方向事件、不重新选择 normals，不在源码内硬编码这些可重算 payload。

源原日志 3729117 B，SHA256 0260f3a8d1233afbdad4227ae5260ae5956bcd58c0cea6dd53e2f399ea3409c9；COMPLETE 原 JSON+LF 为 951619 B，SHA256 b12af5a0b05735260db68162a3f6879d151ca939afca5abed1ea7e4505b168c8。原 DEV 45342 B，SHA256 f8eab10dd3840abfe7883647d643cc6dd9f17eba893b5d1e6e382b73795e5da4，四组19项通过只读复用。

首个真实 complete model 安装前仍要求59-entry bank及原context/hash严格匹配。新 objective 不调用硬写22-entry的旧构造器并谎报输入数；采用已付 direct-checkpoint 恢复函数和相同 RememberingCompleteObjective 初始化模式，另设真实59-entry契约。

不修改 cfg：policy、实现源身份及新增 streak 放在 objective.evaluation_definition / audit / request，不能改变 factorization_definition 或 bank memory_context 所依赖的原 cfg digest。g、immutable b0、exact H reference 与真实物理点都保持。

## 7. 最小新增源码与静态接线

本设计后拟新增三份小 UTF-8 源，旧所有源不改：

1. scripts/frame_metric_covered_soft_growth.py  
   定义 POLICY="same159-complete-model-covered-soft-ordinary-growth-v1"、CoveredSoftGrowthObjective、只读 OrdinaryCoveredContext 捕获/核验，以及返回两个 streak 的 next_covered_soft_growth_trust。复用原 bank restore/first-model gate、完整模型、所有普通/SOC函数，不复制几何或 LP。
2. scripts/frame_metric_covered_soft_growth_recovery.py  
   基于已付显式 pair-reserved outer 的必要小差异：新类入口、最终factory后的 context登记、模型末一次新controller调用、两个计数/输出。原 primary allocation、scoped ceiling 的 try/finally、same-y expanded SOC、实际 gates、学习和恢复保持原函数调用与原顺序。不 monkeypatch。
3. scripts/frame_metric_covered_soft_growth_development.py  
   只包含第 9 节新接口小fixture。所有旧10/7/cache/四组19项只读复用，没有旧科学初始化。

root 另提供唯一 direct transfer / audit / workflow / request。source绑定清单在源码冻结后据真实 imports 补齐，本设计不预报一个未经构造的最终数量。

新 outer 的旧 function return 结构保持，新增字段独立：

- 原 final_consecutive_growth_qualifying_models 表示真实 legacy 输入，另加 final_covered_ordinary_growth_streak；
- 原完整 scale_feedback_update 保留在 frozen_scale_feedback；
- 新 covered_soft_ordinary_growth 记录资格、source context、两个计数前后、pair消费、old next B、new next B；
- 原 successful_SOC_radius_retention 及 expanded_layout_SOC_radius_retention 保留原字段与真假；
- 下一模型 trust_before_model 与上一新输出逐项核对，才记 grown_radius_actually_used。只发出 next B、不再有后继模型时只记 proposed-not-used。

不得从 post-learning current pool 对旧 primary 的选中数组强行改签名。complete model 的 frozen旧selection绑定与 live新池覆盖是两个不同对象，必须分别保存。

## 8. 预算与真实代价

总额度保持 12 started LP、40 ordinary physical values、120 active seconds、每 LP最多原10秒。pair reservation 的临时 ceiling 及其异常 try/finally 恢复完全复用，SOC机会仍只是资源资格。所有 newly started primary/SOC LP 在启动前记共享账；未使用的1个剩余槽仍可能因无paired primary退出。

新 controller 不做普通几何、J、JVP、优化或 LP，只比较既存数组/缓存、ID集合、模型身份和原真实步范数。其 bookkeeping 时间仍属于同一 active clock，不能报告为总体免费。若对大数组重新 hash，须计这部分 wall time；不生成新的 full-J 或fullscan。

真实可能代价：

- 增长后的 B 可能导致曲率或其他硬门失败，触发原缩径、SOC、backtrack 和更多新硬行；
- 同一12 LP内可能减少成功普通模型数，可能更早耗完40值或120秒；
- 大步可能使原三次内层切平面仍返回 repaired inexact，或无合格 incumbent；
- 可能很快遇到 cap，或者由于质量/绑定/新硬行条件而根本不增长；
- 更大的 selected池/范数bank会有真实重建和切面费用，全部原账保留。

本次没有SOC发生，不能把设计动机写成“新SOC已经证明会收益”。新的可验证目标是：规则何时资格成立、是否真实消费pair、下个模型是否使用增长B，以及实际η/κ/门/成本发生了什么。任何与上一运行的速度或下降量比较都须承认轨迹、row bank和状态不同，不做未受控因果归因。

## 9. 只覆盖新逻辑的开发检查

首轮只在公共 Actions 执行以下四个新小组；没有旧developer或真实几何/LP调用。

### A. 完整覆盖 witness 的正反接口

以原小数组类型构造最终两factory绑定、原两网ID/版本、已有实际 d 缓存和trial记录；真正走新context捕获/核验。正向分别覆盖一张网/两张网新增soft及0新增。反向检查一个新hard、旧ID删除/重复、错网或越界ID、计数不符、stale complete binding、实际 d 缓存缺失/不完整扫描。明确不调用 oracle.evaluate 或 original_row。

### B. 两计数与原 fallback

只用小模型/原控制器纯函数验证：旧streak1继承而新0；两次covered普通步触发原倍数；中间坏ratio/硬行清新计数；旧无新行pair先增长时清两计数；cap处消费pair；成功SOC、不合格SOC、poor-ratio和原缩径保原完整结果。保旧false字段，不通过改旧模型造资格。

### C. 返回点与实际步身份

repaired inexact但残差/实际门均通过的输入可合资格；raw LP rho不能替代完整实际d；名义p与rounded实际d不同的fixture必须认实际d；分母0/负/非有限、错误物理映射/height reference、错source cfg不会获得新增长。

### D. 59-entry入口及显式报告接线

新bank input只接受当前59 entries/context/hash；不重跑旧恢复算法测试，可复用已付小bank工具的数据结构但只查新增expected count和完整source字段。显式outer人工stub只确认factory后登记、学习不删除、两个streak传递、后继B使用标记、旧controller及旧pair-allocation调用次数/返回结构保持。总预算和旧scoped ceiling不重做已付数值套件。

这些项目的人工数据不能混入真实运行，报告需将人工API通过与后续唯一科学continuation分开。

## 10. 结果必须如何呈示

每个实际模型需要输出一条有界记录：

- old B、old/new pool versions/counts/hash及新增原 IDs/groups；
- 原 legacy controller完整结果和原失败条件；
- 新context/final complete binding/actual d SHA及两个完整覆盖点数；
- 真实两网η、原predicted decrease、ratio、实际body norm/B；
- 新资格的逐项checks及唯一或多个失败原因；
- legacy/covered streak前后、pair由哪条规则消费；
- old next B、最终next B、是否在后继模型实际使用；
- 保留的原学习、hard omitted、SOC17字段、LP配额与inexact标签；
- bookkeeping elapsed与无额外 geometry/J/JVP/LP/value 调用的实际计数。

阶段末单列：真实增长提案数、实际后继使用数、新soft-covered资格数、新hard reset数、旧fallback数、SOC机会/启动/接受数、未使用LP、完整最后两网门及最佳点。若未触发，直接报告未触发，不复跑同阶段等它发生。

## 11. 来源与结论范围

原式和API来自同一冻结source aca67097b60b7eacdcf20798395ce6d4d1ab2845：

- frame_metric_entry_tail_height159.py：next_mapped_trust / growth_definition，原两次成功、原3/4与9/10门、mapped cap及原缩径优先；
- frame_metric_height159_soc_hold.py：model_binding、原17项successful-SOC条件；
- frame_metric_expanded_layout_hold.py：完整checkpoint恢复及新增expanded-SOC hold优先级；
- frame_complete_affine_metric_oracle.py：两个完整网格四最大值、实际单方向缓存与成功覆盖；
- frame_metric_height159_complete_affine.py：同x实际总步prediction及原selected误差分账；
- frame_metric_affine_spectral_model.py、frame_metric_norm_direction_memory.py：原rho修复、返回incumbent、真实norm记忆；
- frame_metric_soc_pair_reservation.py及其显式recovery：当前12LP资源分配与原函数调用顺序。

数学依据是式 (2) 的有限网格覆盖恒等；新的下一半径规则仍是一个有证据门控的提案策略。它不证明下一步可行、不证明收敛、更不改变当前未达到eta=0.26及目标曲率的事实。本设计完成后可实现三个新增源并交root唯一公共首验；当前没有执行新检查或科学。
