# R610 接口：同一实际前缀锚与 R601 相对度量输运

作者：ChatGPT /root（AI）。日期：2026-11-16 UTC。

**可信度：已证明（完整源码接口及数学消费的条件命题）；尚未实际执行新组件。** 本文件与[完整证明](../results/R610-actual-prefix-anchor-and-R601-relative-metric-transport.md)一同交付。它说明怎样在真实原调用链消费 R601 已完成的 C0/C1 缺陷，不把 source pin、计划中的完整覆盖或 job success 当作当前场已经取得小误差。

## 1. 完整交付与唯一入口

| 角色 | 路径 | UTF-8 字节 | SHA256 |
|---|---|---:|---|
| 新源 | computations/geometry_20261116_actual_prefix_R601_metric_transport.py | 31602 | 4b49ea2a80ef8215d04fda4d607f6bb288a31728c927e0beddbec56f1da6d4fe |
| 数学与来源证明 | results/R610-actual-prefix-anchor-and-R601-relative-metric-transport.md | 20682 | cab5c2e3cee0abc91acd1e4c641d05320566a8090110914b7b04a3334412f4c8 |

源 schema 为 R610-actual-prefix-anchor-and-R601-relative-metric-transport-v1。唯一公开构造入口为：

~~~python
bind_loaded_prefix_metric_transport(
    continuous_rhs_defect, *, metric_kernel
) -> BoundPrefixMetricTransport
~~~

参数 continuous_rhs_defect 必须是调用者已经实际构造的那个 R601 BoundContinuousRHSDefect；metric_kernel 是同 job 原完整 metric kernel 的实际导入模块。接口没有允许 caller 直接传入 rho、A、mu、入口残差、长度或数值门槛的参数。

对象接口为：

~~~python
observer.describe()
observer.retire(cell, diagnostic, *, split)
observer.summary(
    actual_R601_summary, *,
    original_coverage,
    complete_cell_ledger,
    original_error,
    original_stop,
    close_errors,
)
~~~

没有独立 main、CLI、workflow、子进程或第二次扫描。未来 caller 的完整 source plan 需要加入这份真实来源，并按原闭包逐值核回。本文不是某个已经发布入口的就地补丁，不把 R610 自动记入249、250、251或252已经执行的来源。

## 2. 绑定的是哪些实际对象

构造首先要求 GITHUB_ACTIONS=true、GITHUB_REPOSITORY=Rogerhu12/math-research-public。源码自己的 HERE、各实际模块路径和全部文件 SHA 都取自该公开 checkout 的 computations；不能把复制来的同名对象或另一个运行的 summary 传入。

| 原对象 | 完整源字节/SHA256 | 真实约束 |
|---|---|---|
| R601 | 23113 / 12450be1cbdd289b69f74535d98fa42586506709244ed066b338c98cd494490d | geometry_20261116_actual_analytic_saved_RHS_C1_defect.py 的真实类与模块 |
| Active | 33310 / 675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b | geometry_20261115_shared_active_interval_balls.py 的原完整 prefix 方法 |
| metric kernel | 35473 / a601e5b5dca3c7d87ea7b78a4eb0cebf0b7884d9d4663570f262d6cda578ed17 | geometry_20261115_shared_field_relative_metric.py 的实际模块 |
| 保存场原材料内核 | 16911 / 51eab8cdc878e22ad2c57bab129b1ef31463799596fcc40399fd8b0714ccbea0 | geometry_20261114_large_core_saved_prefix.py，仍在实际 loader 已核来源闭包内 |

R601 的 tubes、field、current、saved、api、check、M、N、sqrt_bits 原对象直接复用。其中 saved 是 R596 的已绑定完整缺陷观察对象；field.saved 才是实际保存场 loader。两个层次不可混用。R610 核 tubes.field、saved.field、current.field 是同一个 field，核 saved.check、tubes.budget_check 与 R601.check 是同一个 callable。

field 的 prefix_coefficients、prefix、registered_world、material_angle、evaluate 必须实际继承自已核 Active.ExactFiniteField 对应函数，比较的是绑定方法的 __func__。accurate-cut 类型只在别处改 cut_targets/expression_identity，当前前缀因此仍是原准确完整表达。只核一个函数名或 prefix_coefficients 字节不够。

动态 M 的 field.saved 类模块也记录完整身份，并要求存在于它自己已经核过的 source_sha256。没有把旧 M96 数据或一个固定112 loader 强套到当前 M。当前 core 与 density 都有恰好 M 个元素；实际物理行数为3M+2，两 mean 保留。

describe 返回完整 binding 的深拷贝及准确有理值的字符串表示。binding 包含实际 R601 来源和 binding identity、R553 binding、Active/kernel/loader/材料内核来源、全部 checked source closure identity、原完整 checkpoint、全部 array words identities、当前 field expression 和 target binding identities、M/N/行布局、坐标和原材料正下界。identity 负责来源与复现，不声称该对象的全部数组或 ledger 已随必要正文运输。

## 3. 在原遍历中的接点和顺序

调用者必须在原完整遍历开始前构造一个 R610 observer，随后沿原有每次 retirement 调用一次。准确位置是：

1. 原 cell 的 R553 inspect 已完成，完整 diagnostic 已形成。
2. 原 metric/DFS 逻辑自行作 split 决策。
3. 原 R553 commit 已用该 cell 和原决策记账。
4. 调用 R610.retire，传同一个 cell、完整 diagnostic 与实际 split 布尔。
5. 把返回短记录加入该 cell 原临时 ledger 行，再写原完整 ledger。

上述顺序保原 split、队列、目标调用、field 调用和原接受判据。R610 不决定是否细分，不能为取得较窄 A(0) 再作额外 target 查询，也不能在 finish 时遍历一次旧诊断来补计已经错过的责任。

非 prefix cell 返回 None，不加入本组件 prefix 计数；原 caller 对该 cell 的全部原责任照常完成。prefix split 行表明责任转给全部原孩子；split 父格不作为最终正分母或入口锚。

对 prefix terminal，retire 要求：

| 检查 | 含义 |
|---|---|
| retired/split/terminal 与 R553 当前 committed/split/terminal 相等 | 立即跟随同一原 retirement，拒绝跳过或重复 |
| R553 last_observed_address 等于当前 cell | 同一个实际 cell |
| diagnostic schema/cell 正确且 available=true | 当前完整可用诊断 |
| scalar_box.actual_same_target_return 是原同次 context | 不从第二次目标求值或旧缓存借半径 |
| context 原 numeric s 区间等于 cell.radial | 同一完整闭径向域 |
| context.radius 等于 scalar_box.A 且 A 下界正 | 同一次半径外包与正分母 |
| cell 在实际 prefix piece 两闭端点内 | 不混片、不把尾部当当前前缀 |

每一条返回记录都有原 cell/decision/index、完整 diagnostic identity、paid、入口候选状态、完整 reasons/error。每个原 ledger 行保该完整短记录。组件只另存计数、滚动 SHA、首末 unpaid；必要正文不冒原所有 ledger 行已逐条传回。

retire 捕获 ORDINARY 所列普通值、算术、类型、键、索引、属性和 IO 错误，记录完整 traceback 与 unpaid。它不把自身不可用改成原 metric 拒绝。RuntimeError 类型的原 ResourceStop 和 MemoryError 不在 ORDINARY 内，沿原控制流传播。

## 4. 入口 A(0) 的真实来源

实际左端为零且属于 prefix_span=0 的 terminal cell，才可提供入口候选。这里消费的半径区间是原整个 cell 的 target 外包，包含该准确允许 C 族全体的 A(0)。

所有这些区间作准确交集，返回 observed_entry_radius_enclosure；保 entry_radius_candidate_cells、首末实际 target-return witness 及每行完整来源。交集为空是未付错误，不能用中点修成一个新目标。原完整覆盖仍须真的到达至少一个入口 terminal；根计划中写着入口，不等于该入口已经观察。

实际 field.x[0] 必须为零，field.x[-1] 的准确提升必须正并与 current.target.numeric_length 相同。积分用这个完整数值径向长度 L_numeric。真实目标长度 L_true 继续只通过原 mu=L_true/L_numeric 进入目标，不把两长度认成同一个数。

rho 下界取当前 field.rho_lower，并核与当前 field.saved.rho_lower_exact 准确相等且正。这是当前 loader 已按 R237 对当前全 core 支付的全圈正界。metric kernel 的 angle_density 返回 Theta_q=2*pi*rho；本组件没有把它误当 rho。R601 C1 和本文一律用物理角 phi 弧度。

## 5. 首节点完整模式锚的形成

只有原 R601 与覆盖完整性全部成立以后，summary 才形成锚。它使用同一 R596 已检查的 raw physical/core 字节，由 R596 的 row_words/exact_word 提升全部3M+2首节点词和全部M个core词。再次核这些真实值与 field.nodal 首节点、field.core、field.saved.core 相等；逐模式核 field.density=(1-n*n)*core。

竖向 mean 的角导数为零，但原字节仍读入并给准确值。负零保在完整原词身份里；其准确有理零只表示实数值，不声称二进制词未发生数学表示变化。

完整返回 actual_complete_anchor 包含：

| 字段组 | 返回内容 |
|---|---|
| 原字节/维度 | 首节点词数、core词数、两组 SHA、全部模式残差 rows 的 identity |
| 实际残差和 | r0-1、B_r、B_t_without_radius_difference、B_t、B_z |
| 完整材料 | full_material_density_lower/upper |
| 准确目标 | actual_entry_radius_enclosure、max abs(1-A0)、候选数、首末 witness |
| 向外锚 | 平方和、向外 sqrt、complete_entry_relative_angular_length_error_upper |
| 范围标记 | core-entry_r、各z模式、A0均未假设相等或为零；原BC打印值未代替准确值 |

逐模式量及完整推导见证明§5。代码不查询新角网格，不缩模式，不删除两 mean，不作第二次 DFT/FFT，也不调用新的 field six jets。其锚为

$$
q_0=\frac{\operatorname{sqrt}_{\rm upper}(B_r^2+B_t^2+B_z^2)}
{A_{0,-}\rho_-}
$$

并对最终正比值向上舍入。没有要求这个量已经很小；宽目标外包和小正分母均按原式扩大实际界。

## 6. finish 的唯一所有权

原 caller 仍拥有 R601.summary 的唯一实际科学完成调用。先取得它实际返回的**整个** necessary 对象，再把该对象送入 R610.summary。不用自建成功子字典，不从另一次 run 或另一个 field 读回两个数字代替它。

R610 从不调用 R601.summary，也不重复 R580/R596 finish、指数、alias 或全节点形成。它要求当前 R601 状态及返回值同时满足：

- summary_calls 恰为1，finish_started=true，pending=None，非 recovery；
- actual returned binding 与当前 describe 完全相等；
- 返回的两个原 summary 与 R601 的 analytic_summary/saved_summary 缓存完全相等；
- complete_prefix_bound 与 last_completed_composition 完全相等；
- formation_error、last_formation_error、原 stop/error/close_errors 均空；
- 原 complete coverage 真，coverage identity 相等，complete ledger identity 相同；
- 原 validate_complete_originals 对同一 coverage/ledger 的全部检查成立；
- R610 retirement 与 R553 observed/committed/split/terminal 相等，terminal>0，全部 positive、unpaid=0，实际入口存在。

summary 的 original_R601_complete_flag_and_original_cover_returned 只是早期 eligible 条件标记。最终实际消费成功要读 actual_R601_binding_and_complete_transport_consumed 与 complete_prefix_relative_metric_bound，不能把 eligible 本身当完整证明。

## 7. 返回的完整前缀相对界

R601 原完整 bound 必须声明当前 M/N/3M+2、实际 numeric s、physical phi radians、real Cartesian world frame 与原 upper sigma=1。读取的原数值字段只有：

~~~text
complete_prefix_unprojected_physical_RHS_defect_upper
complete_prefix_unprojected_physical_RHS_world_phi_derivative_upper
~~~

两者仍包含原无限尾、全部 alias、完整保存 RHS 形成差及 world C1 连接项；不重新选择成功的局部子范围。R553 minima 必须恰为 A、mu、P、W，全部准确正。只有原完整覆盖后，它们才能作为全前缀下界。

最终完整 bound 的核心字段为：

| 返回字段 | 形成式或责任 |
|---|---|
| complete_unprojected_RHS_C0_upper / complete_unprojected_RHS_world_phi_C1_upper | 同一实际 R601 的 B0/B1 |
| complete_relative_radial_defect_upper | 向上 B0/mu_lower |
| complete_abs_angular_length_radial_derivative_upper | 向上 B1/(A_lower*rho_lower) |
| actual_numeric_prefix_radial_length | 原完整 L_numeric |
| complete_radial_transport_integral_upper | 向上 L_numeric 乘上行输运率 |
| complete_relative_angular_length_error_upper | 向上 q0 加完整径向积分 |
| normalized_Gram_absolute_entry_upper | a=2delta+delta²、b=delta(1+q)、c=2q+q²，逐步向上 |
| complete_prefix_relative_Gram_operator_upper | 向上 (a+c+sqrt((a-c)²+4b²))/2 |
| actual_complete_anchor / actual_R553_complete_positive_domain_lower | 全部实际锚和正分母 |
| actual_R601_complete_bound_identity / actual_complete_original_cell_ledger | 同一次原输入与完整覆盖责任 |

sqrt 使用实际 R601.api 中原 R521 的 sqrt_bounds；其余向上用同一 R580 relative_dyadic_bounds 的上端点。每步形成前调用同一原 check，逐模式形成也用它。没有新容差、额外 q<1 门或取最小值覆盖原 metric 结果的逻辑。

矩阵公式使用向上后的非负 a/b/c。其合法性来自非负对称比较矩阵最大特征值对各项单调，而非声称 (a-c)² 对两项都单调。完整证明同时保留正分母、全径向路径、所有角与闭端点，不能把局部 visited extrema 当这些全局量。

## 8. 完整必要、异常与原90000限制

R610 summary 原样嵌入 actual_original_R601_summary 的完整对象，包括所有 R580/R596 旧 errors、unknown、unpaid、partial scopes。额外返回完整 binding、原 error/stop/close_errors、coverage/ledger身份、全部 retirement 计数、首末 unpaid、入口区间、当前完整 bound、formation_error、last_formation_error、pending与未付清单。

普通新界形成错误记录真实类型/message/traceback和当时操作；current complete=false，原 metric/solver 判断不改。真正 ResourceStop/MemoryError 传播给原 caller。原 caller 记录真实 stop 后若需完成必要元数据，可以再次调用本组件 summary 的 halted 分支；该分支不再次形成锚、Gram或任何原 finish。

原 stop 之后即使对象留有此前完整 bound，也只在 previous_completed_bound_not_current_after_a_stop 下返回，当前 complete=false。不能用这个旧缓存覆盖真实停止，也不能再次无 stop 调科学 summary；后者被原 finish_started 检查拒绝。

本组件没有独立90000上限或stdout传输。未来 caller 的原完整 source/science necessary、全body90000/真实70和cleanup合同继续。若同一完整必要对象另含完全相等的 R601 全体，可以只对这一具名生产者层作同体可逆共享，且按包含全部关系报告的最终whole正文比较严格变小。不能任意遍历科学树压缩、拆包、丢旧错误或把runner内已形成当成功运输。此处没有承诺未来必要一定装得下。

## 9. 坐标、反射与仍未支付的闭面范围

结果针对同一当前前缀、整闭径向区间、全部物理角、所有前缀接缝和原两反射片。原 proper SE2 registration 保范数/Gram；全竖向反射也保 Gram，但速度支解释要翻为负的原 upper sigma，不能因此辨认 native worker 的支。

相对算子范数在 induced metric 与同一 target 同时拉回时不变。实际共同首材料坐标与 full-phase API 的来源绑定、完整应用仍需未来 caller 真正支付。本组件未执行这些 API，不假设固定有限N DFT与任意角平移交换。

下列责任在每份 summary 的 unpaid 中明确保留：真实 common-first-material/full-phase 应用；tail/collar/accurate-cut-patch 的连续缺陷及 cuff 锚；完整帽/接缝绑定；全闭面相对度量及同目标实际 refinement；reach、held-image amplitude、含反射非刚性和全闭面直径。原非零112/338/450求解及所有末门也未由本组件产生。

## 10. 当前可复现状态与紧接工作

本条写作只生成作者源码、文字证明、接口和 UTF-8/SHA 元数据，没有本地 import、AST、compile、测试或数值计算。没有实际新run/head/job可以登记为本组件科学执行。

完整源与证明现在独立刊入，不增加外部审查或fixture前置门。紧接工作是把上述接点接入真正拥有 R601 与原全部 ledger 的完整 caller，形成全部真实来源级联；继续原公开 Actions 的同一科学钟、同一整域、同一所有原数值门及完整必要回读。后续实际返回再单独登记，不能回写旧run的覆盖或科学状态。
