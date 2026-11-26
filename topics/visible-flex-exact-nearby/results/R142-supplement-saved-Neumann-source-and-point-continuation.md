# R142 补篇：已存真低逆后的四源、全部端点及全径向观察的可接续证书

2026-11-26，visible-exact-astra-198c63d-20261126。

本篇记为 **NS**。它接已经实际保存并读回、且严格通过的 PS 六球，补足原来未成的四个源响应及全实径向观察。PS 的完整 defect 目标、比较 Green 目标、已接受源积分和已接受观察格均只消费。这里没有新的数值结果，也没有预先生成成功前件。

锚点：

- 原 R141 193 维比较 Green、真实低系数 lift 和全格观察：`scripts/fourfold_codazzi_low_centre_verified_green_math.py` 的 `actual_low_source_bound`，以及 `scripts/fourfold_codazzi_low_centre_shared_scalar_factors.py` 的 `whole_box_projection_bound`。
- 原 GM.1–17 精确矩与 PS.1–8：`results/R142-supplement-durable-complete-parent-source-moment-prefixes.md`、`scripts/fourfold_codazzi_low_centre_streamed_parent_moments.py`。
- 已核的独立 point-only Z：`scripts/fourfold_codazzi_low_centre_point_covariance_materialization.py`。它没有旧 defect 的 Y、同格双三角、全体 HS 或 atoms 范数。
- 后续物理门仍是 B4–B21，随后是 P1–P16 与 L1–L25；本篇只把新的实际低输出 kind 接到原公式，不改变这三组公式。

## NS.1　唯一适用对象与已付前件

底层对象始终是原 WVC 的同一 hybrid low 变系数问题，真实径向长度、155 个母格、1424 个比较子格、193 个状态坐标、独立 root97 及 outer96 保持。193 维角向块不是径向截断。完整原族、修复下系数、两个实际边界列以及所有原符号，均由原七份科学定义及完整同对象 admission 固定。

PS 的原六个完整上界为

$$
b^2,\qquad r^2,\qquad o^2,\qquad
b,\qquad a,\qquad c ,
\tag{NS.1}
$$

分别对应 defect 的 body HS 平方、root97 HS 平方、outer96 HS 平方、body 算子范数、联合 193 atoms 范数、body 与 atoms 联合范数。这里采用文件保存读回后的完整球。令其 body 范数球的有向上端为 $\varepsilon$，唯一入口条件为 $\varepsilon<1$。PS 的 `strict_gate_uses_saved_decimal_upper`、`strict_low_coefficient_gate_passed` 及 `actual_low_hybrid_inverse_proved` 均必须为真，155 个完整源母格前缀、1424 子格和 193 outputs 也必须齐全。

若 PS 在六球和该数学目标已经正式保存后，于后处理阶段失败，仍保留原 complete/proved/failure/returncode；不把执行失败改成成功。只在完整源码、manifest、execution receipt、全部字段和上述已存目标共同核验后，才消费这六球。PS 的 scope 字段准确使用 `ordinary_four_source_and_whole_point_certificate_not_claimed`，不得套旧 R142 的另一字段名。

本入口只接受这个真实 PS 结果，或同一已发布 NS owner 产生的合法后续前缀。原 R142 45761859526/1 已确定没有六球，不能冒充本篇前件。新的对称部 $\theta$ 证书属于独立的 R149 分支，本入口不把它当作 $\varepsilon$。

## NS.2　四个固定源域与完整源变量分解

四个 role 仍为

1. `ordinary_raw_low_source`；
2. `transformed_low_source`；
3. `low_second_kind_correction`；
4. `centre_high0_return_source`。

每个 role 的输入范数、变换、独立列及完整 family source，完全沿用原 provider；没有把四个输入空间合并成同一个 common 输入。对每个未成源 $\alpha$，PS 的源变量分解直接给出

$$
s_{\alpha,\bullet}^{\,2}
=
\sum_{i=0}^{154} s_{\alpha,\bullet,i}^{\,2},
\qquad
\bullet\in\{\mathrm{body},\mathrm{root97},\mathrm{outer96}\}.
\tag{NS.2}
$$

每一项的源变量落在第 $i$ 个完整母格，输出仍覆盖**整个**实径向区间及全部相应 atoms。共同的 A/B/K 与 root carry 是比较算子的完整输出协方差；两条同子格三角项仍在原有带符号完整和中。这里没有引入接口边界条件，也不把不同径向输出片段假设成正交。

PS 纯模块已经容许任意非空、互异的原 source roles。故同一母格可同时累计当前尚未成的全部 role。每个被接受的母格保存每个 role 的三个完整平方上界；恢复时只为尚未接受的母格调用 `provider.packet`。若前缀已有全部155格，只消费这三个平方球并作尚缺的开方，不重积分任何母格。

原 point-only Z 也可以在未成源格的同一母模板内物化，从而共用 H/Q 模板和局部 frame。它不增加新的源 norm 目标。若恢复时还需要 point 观察，已经接受源积分所对应的、尚未发布的 point Z 仍须真实物化；这笔费用不被免除。

## NS.3　六个 comparison 球与实际源 lift

全部155母格读回后，对尚缺的源 comparison 生成

$$
n_{\alpha,b}=\sqrt{s_{\alpha,b}^{\,2}},\qquad
n_{\alpha,a}=\sqrt{s_{\alpha,r}^{\,2}+s_{\alpha,o}^{\,2}},\qquad
n_{\alpha,c}=\sqrt{s_{\alpha,b}^{\,2}+s_{\alpha,r}^{\,2}+s_{\alpha,o}^{\,2}}.
\tag{NS.3}
$$

三个平方和这三个范数共六球，先形成独立完整候选，整件保存、整件读回并核包含，才进入正式 `comparison_source_norms`。后续实际 lift 从这些正式球及原 PS defect 球读取依赖。即使此后预算中断，也不得重算已成的六个 comparison 球。

记原 defect 的 atoms 上界为 $a_D$，有向正余量为 $g=(1-\varepsilon)_\mathrm{lower}$。原低 lift 的费用为

$$
N_{\alpha,b}=\frac{n_{\alpha,b}}{g},\qquad
N_{\alpha,a}=n_{\alpha,a}+a_DN_{\alpha,b},\qquad
N_{\alpha,c}=\sqrt{N_{\alpha,b}^{\,2}+N_{\alpha,a}^{\,2}}.
\tag{NS.4}
$$

对于 second-kind role，继续使用原完整图范数公式

$$
N_{\mathrm{2nd}}
=
\frac{
\sqrt{(2+N_{\alpha,b})^2+N_{\alpha,a}^{\,2}}
+\sqrt{N_{\alpha,b}^{\,2}+N_{\alpha,a}^{\,2}}
}{2}.
\tag{NS.5}
$$

这些是原 `actual_low_source_bound` 的直接调用，不是新推测的 resolvent。原完整 PS body 球在每个实际源记录中原样复用。新的源球须在候选中整件读回并核包含，随后才把该源及对应 target 同时接受；因此“comparison 已付、actual lift 尚未付”与“完整源已付”是两个明确状态。

root97 与 outer96 的平方继续单独保留，未被 atoms 的合并值覆盖。后续 B4–B21 仍可分别构造真实两端 receiver。high0-return 仅是原低源，仍不授予 full CFB 或完整正侧逆。

## NS.4　全径向观察需要自己的 point 核

全实径向观察继续使用原局部公式。对每个完整子格的四个闭子盒，比较投影 $P_0$、真实 defect point receiver $R_D$ 与完整 body-output column $C_0$ 给出

$$
\|P(r)\|
\le
\|P_0(r)\|+\frac{\|R_D(r)\|\,\|C_0(r)\|}{g}.
\tag{NS.6}
$$

$R_D$ 使用完整真实 defect 的源协方差，$C_0$ 使用共同 A/B。原 mean 状态、physical S/S-inverse 权和全区间的源贡献均保留。这项不能从 body 的 L2 范数恢复。

point-only helper 精确复用 GM 的独立 Z 分支及其全尾包围。它返回 IL/IR 与 OL/OR，但不返回 `same_panel_complete_HS2_upper`，也不冒充带两三角的完整 HS packet。因此 NS 没有重新计算旧 defect 的 body 或 atoms 范数。

对 raw 投影还原使用原物理权条件数，随后原 matching 下界为

$$
\sigma_{\min,\mathrm{raw}}(r)
\ge
\frac{1}{\sqrt2\,\|P_{\mathrm{raw}}(r)\|}.
\tag{NS.7}
$$

每个新接受的 refined cell 必须完成其全部四个闭子盒。保存状态是截至该格的 weighted 上界最大值、raw 上界最大值、matching 正下界最小值以及一个实际 witness box。三个完整球先保存读回，恢复时上界只取保存球上端，下界只取保存球下端。一个未成 cell 的局部结果不进入接受游标。

因此恢复只重新观察未接受的 cell；为新观察所需的未发布全域 Z、源左右累积协方差及比较 A/B 可以重新物化，已接受的观察目标本身不重做。只有全部1424格、5696闭盒以及四个完整源都齐全，才形成最终 `whole_interval_transversality`，三个球和 witness 从已验证前缀原样转入。

## NS.5　完整身份、事务及后续物理门

新科学 kind 为 `complete_R142_low193_neumann_source_point_continuation_v1`。它显式保存两种前件引用：

- `completed_prior_low_defect` 始终直接指向原 PS 的完整 actual/execution/manifest，不随恢复链丢失；
- `completed_prior_neumann_prefix` 指向本次实际消费的直接前件，完整保留其执行状态、失败对象、已成目标和当时 current target。

每次续接的 manifest 保留上一 manifest 中每个输入的同路径完整 bytes/blob/SHA，原21历史/native定义也不改。角色改名只可用于不冲突地保存既有整件引用，不能替换文件。原比较模型、完整 reference identity、原七科学定义、155/1424分割、193 atoms 与同一 PS 六球都逐项一致。

候选文件先原子写入临时名，验证完整 bytes 与完整解析对象相同，再验证每个新球包含全部有向值，才将**同一批 bytes** 原子移到正式输出并推进状态。预算检查不得删去刚完成并已验证的母格或 point cell。异常分支 complete=false、proved=false，但正式接受的数学前缀与已成目标完整保留。

本次运行只登记尚缺的原 source/point targets，按原顺序排列。已成源即使不在本次 target 列表，仍完整复制到输出；不能把五个潜在目标都计为本次新成功。若全部 source/point 科学目标都已存在，metadata 路由不再创建重复科学运行。

后续58门只接受完整成功的实际 NS 证书、原 PS 六球、四源含193 atoms、5696盒的全径向观察，以及原 weighted high/D 等实际输入。NS kind 被显式区分；它不冒充原 R142 六目标，也不改变原 R149 $\theta$ 分支。58、224、32的原数学公式及原计数不变。

即便上述低证书完成，完整 CFB、真实 physical outer gate、原七端口、两 WPN 行、负侧连接、真实 $\nu$/phase 兼容及非线性闭合仍须各自实际付清。本篇没有把它们标成成功。

## NS.6　执行界限

owner 使用原 Python 3.12.14、python-flint 0.9.0、320-bit definition admission 与768-bit directed arithmetic。新 source/point 科学预算19600秒，公共 worker child20100秒；旧 R142/PS 的真实执行记录保持各自原值，不回写历史。公共 Actions 的360分钟上限不变。

新文件仅为纯定义与实际入口；没有实际 PS εtrue 前件时，生成器只输出 readiness。不得提供 dummy actual、预填 source bounds，或以 packet 数量代替完整源积分。
