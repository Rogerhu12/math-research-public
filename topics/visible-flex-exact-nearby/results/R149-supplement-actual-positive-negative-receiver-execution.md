# R149 执行补篇：原14个物理端口的56个真实负侧 receiver

2026-11-26，visible-exact-astra-198c63d-20261126 / low_inverse。

本文件配套 [PN 解析接线](R149-supplement-complete-positive-inverse-to-true-negative-and-incoming.md) 与以下实际入口，定义一次完整的新56标量目标。目前没有实际58/224/32的成功输入，因此本提交只提供源码；不附将来结果的 manifest，不运行科学部分。完成状态由公开执行的整个结果及其执行记录决定。

| 文件 | 作用 |
|---|---|
| [pure math](../scripts/fourfold_codazzi_positive_inverse_negative_receivers_math.py) | 原空间 receiver 算式；没有 IO 或科学入口。 |
| [owner](../scripts/fourfold_codazzi_positive_inverse_negative_receivers_owner.py) | 先接纳完整 actual 文件，再只计算本56量，逐条完整保存和读回。 |
| [public worker](../scripts/fourfold_codazzi_positive_inverse_negative_receivers_public_worker.py) | 使用原小标量公开执行框架；绑定源码、读取规矩、保留前缀并公开结果。 |
| [metadata generator](../scripts/make_positive_inverse_negative_receivers_manifest.py) | 仅当真实前置齐备时生成本目标的 manifest 与 workflow；它不导入数值包。 |

## EX1. 一个明确的新目标和原单位

输入是 P224 完整14列，各自保留原物理端口的范数。输出按每列四条的顺序排列，恰有56条；没有为14列各自添加新的 common high 输入变换。

| 输出代码 | 完整数学量 |
|---|---|
| true_full_root_mixed | 真物理根的 low-even96、low-odd96/moving-mean97 和原 high mixed trace 的直和界。 |
| complete_negative_waist_density | 原 strict/Cauchy 负传播后的 primitive pair 与两个 physical mean 的完整联合界。 |
| left_normalized_joint_two_branches | 对该原物理端口应用原有序左 receiver 后，两分支联合界。 |
| WPL_physical_primitive | 同一物理端口的 WPL 完整 primitive 行界。 |

设保存的 P224 第 $j$ 列两条根观察为 $d_j,z_j$。用原 SP 根到腰常数 $C_R$、实际 WX 的 $B_{H,0}$ 和固定 $J_s=268435456$ 的 WTA 逆界 $K_{W,0}$，本目标定义
$$
R_j=\sqrt{{\bf1}_{j=9}+d_j^2+z_j^2},\quad
W_j=C_RR_j,\quad
B_j=B_{H,0}K_{W,0}W_j,\quad
P_j=B_{H,0}\sqrt{1/2}\,W_j .
$$
第9列才是原 independent root-even96 单位输入。其他列不能由使用同一个左 receiver 而被改名成 $H^{-4/3}$ common input。$z_j$ 已包含原 high 输出 factor9，故不再重复乘9；low mixed 权不大于 normalized Euclidean 权。四式中的三根块确为原 Fourier/physical 正交分块，不宣称14个端口的解彼此正交。

$B_j$ 是两分支联合界，也可直接给任一分支；没有额外 $\sqrt2$。$P_j$ 使用 $\sqrt{1/2}$ 的有向上界相乘，不除以一个 $\sqrt2$ 上界。它和 $B_j$ 是不同的原输出，故 WPL 行不额外乘 $K_{W,0}$。两个 physical mean 都由 $W_j$ 的完整腰密度范数控制。

## EX2. 实际输入的完整闭合

owner 在导入 flint 前读取所有固定文件的完整 UTF8 bytes，核 bytes、SHA256 和 Git blob SHA。不是从显示摘要或摘出的字段建立 actual 身份。

1. actual58、actual224、actual32 各有 scientific、execution、manifest 三个完整文件。全部必须 complete、proved、无 failure，原字段、参数、整套目标名与记录数精确匹配；execution 的 scientific-file receipt 必须绑定同一整文件。
2. 224 显式绑定同一58；32 显式绑定同一58与224。三者使用的 low、D 和 weighted-high whole references 相同。共同 reference_identity 逐字段等于已成 D 的完整 WVC/原153链/选定153链/24480/真根身份。原 family 恢复与 physical 图已由真实58接纳，不能凭标签换成另一算子。
3. SP、PW、WX 各读取原完整 execution，包含它的整个 actual_scientific_receipt；核原 run、source、manifest、全部成功 gates 和原零重算记录。SP 与 PW 的 exact_family_identity 相同，中心及方向的完整定义 SHA 固定；PW 所复制的四个 SP gain records 逐字段与 SP 原球相等。
4. WTA 单独读取完整 scientific 及 execution，核科学文件的 bytes/SHA receipt。其 copied_SP_family_identity 和所列原 SP source/manifest 恰等于本次整 SP receipt；原 $10^{-8}$ direction 半径保持。只消费该实际结果中固定 $J_s$ 的四门已成条目，包含有限补和两个 mean 的 identity。
5. WX 使用同一 selected conjugacy、固定 $\eta_0$、原完整 root interval 与 $10^{-8}$ family 范围，保留 density Jacobian、normalized measure 和独立 physical mean identity。实际左 $H^{-1}$ 输出因子与 common-input 记录中的同一因子逐字一致；旋转只使用原等距结论，不交换 Fourier projection 或右输入变换。

旧完成的五个实际小文件固定为：

| 角色 | 原路径 |
|---|---|
| SP execution | notes/primitive_mean_strict_propagation_ci/run-43731464771-1/execution.json |
| PW execution | notes/positive_ports_to_waist_density_ci/run-43734233535-1/execution.json |
| WTA scientific | notes/waist_normalizer_coefficients_ci/run-43763134339-1/actual-scientific-conclusion.json |
| WTA execution | notes/waist_normalizer_coefficients_ci/run-43763134339-1/execution.json |
| WX execution | notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json |

其固定 SHA256 在 owner 的 FIXED_SMALL_INPUTS 中，generator 只读取当前原 bytes 并原样 pin。旧 $C_R,C_O,C_1,C_2$、$B_{H,0}$、$K_{W,0}$ 及旧224/32目标都不重算；本56目标实际使用 $C_R,B_{H,0},K_{W,0}$ 和原224的两根行，32作为准确完整正侧路线的实际前置读取。旧32绝对值表不被恢复成 signed matrix。

## EX3. 保存、读回与 scope

每个新结果先取有向 upper，序列化为完整60位 decimal ball，写入临时候选 scientific 文档，并原子保存后读取整个文件。读回文档必须完整相等，读回球必须有限且包含原 upper；这些核验成功后，才把相同 bytes 提交为正式 completed 前缀并更新内存状态。候选核验失败或被中断不会使正式前缀含一个未核记录。依赖顺序使用保存球的上端：

- $R_j$ 整球保存读回后才计算 $W_j$；
- $W_j$ 整球保存读回后才计算 $B_j,P_j$；
- 每列四条全部完成后才转下一列；只有56条与精确 target_order 全部一致才设置本目标 proved。

因此输出舍入不会在后继公式中被忽略。所有原 source norm 保持原单位，没有对一般 $L^2$ WPN 状态取端点，也没有删除两个均值。执行失败时保留完整已算前缀及失败原因，不把不足56条称为完整成功。

本目标不包含 particular physical WPN source packet、common $\Phi/\Upsilon$ 输入大小、负侧 ordinary 新源大小或 signed finite entries。这些需要各自真实 whole 输入。相应字段准确为 false；没有 dummy packet。另一独立目标可以按 PN.19c/SC.8 支付同一个完整 raw ordinary 源的负侧贡献，但它不在本56目标中。完整 incoming、true $\nu$/phase Schur、nonlinear 解和题目完成也不由本目标自动授予。

## EX4. 真前置出现后的执行方式

generator 接受仓库根路径、真实 WPN result 目录和原 WPN manifest。若文件未出现、实际不完整或门为 false，只输出 ready=false 的 metadata；不导入数值包、不创建科学 manifest 或 workflow。

真前置全部完成后，明确提供新的 manifest/workflow 路径。generator 将5个纯执行/算式源码、5个固定旧 actual 小文件、6个直接证明、9个真正前置文件及1个已读规矩 receipt 合为26个完整当前输入，所有 Python 文件先 AST 检查。规矩 receipt 必须仍与当前根 README 和课题 README 相同。

公开 workflow 使用原固定 Python 3.12.14 / python-flint 0.9.0，320 bit；worker 继续原文件体积、目录容量、读取规矩、科学子进程无 token、逐前缀发布和非快进 rebase/push 循环。新目标有单独 consumed marker，不自动重试科学。owner 科学部分最多900秒，工作流30分钟；不启动一个重叠的低逆运行。

这里不预估56值会小到足够关闭完整 incoming，也不将任一尚不存在的结果绑定为 actual。真正改进是把已成的完整正侧逆按原空间接到14个实物理端口的完整负腰 receiver，使后续真实列和 Schur 可直接消费明确的小记录。
