# 新深谷标量度量的完整固定 g 求解入口

2026-11-26，Astra-larger-e4e2a2bf-20261126 / construction。

本实现把 [R690 的深谷尾输入](../results/R690-quasimonotone-tail-and-deep-valley-input.md) 接到全部原 q/core/H 自由变量、正权完整观测、H² 母范数和 D/L 幅度约束上。目标从第一条方向之前就固定为

\[
g_n=ds^2+a_{\rm new}(s)^2d\theta^2.
\]

它不是 R684 的 moving-mean 设计。没有使用 `MeanMetricOperator`，没有删除角零模，没有将新 a 当作随后会被均值归一化抵消的中间量。当前交付是完整源码、精确来源与可执行参数；**没有据此宣称新场已求解、达到连续误差阈值或完成本课题。**

## 1. 为什么这里必须改变真正固定的目标

令材料角 \(\theta=\Theta(\phi)\)、\(\rho=\Theta'(\phi)\)，并记

\[
E=|F_s|^2,\qquad B=F_s\cdot F_\phi/\rho,\qquad C=|F_\phi|^2/\rho^2.
\]

若原始归一化使用一个旋转标量 a，则原 Gram 残差为

\[
r_a=(E-1,\ B/a,\ C/a^2-1).
\]

对 R684 的固定物理角正权均值，设 \(\bar E=\sum_jw_jE_j\)、\(\bar C=\sum_jw_jC_j\)，其中 \(\sum w_j=1\)。其设计残差恰为

\[
\left(E/\bar E-1,\ B/\sqrt{\bar E\bar C},\ C/\bar C-1\right).
\]

这里 a 已经完全消去。因此，只替换参考 a 并继续对当前场取角均值，不能要求最终度量仍保留 R690 所设计的深谷尾。即使 keep-q 因新的 lift 而改变了实际物理场，也不能把这个目标约束的缺失说成已修复。

本完整分支直接优化

\[
r_n(F)=\left(|F_s|^2-1,\ \frac{F_s\cdot F_\phi}{a_{\rm new}\rho},\
\frac{|F_\phi|^2}{a_{\rm new}^2\rho^2}-1\right).
\]

每一个原有径向、角向和交叉 Gram 行都在；其零误差目标明确是 \(E=1,B=0,C=a_{\rm new}^2\)。全部自由 core 变化所引起的 \(\Theta,\rho,F\) 链由原完整 physical J/J* 支付。没有 moving-mean 投影或针对当前 F 重估目标的步骤。

## 2. 新输入与原自由空间的边界

新 factory 的 canonical model 为 `deep-valley-fixed-scalar-fullclosed-lift-v1`，底层固定 profile 为 R690 的完整精确公式。它保留同一个原解析输入和准确 S、同一符号网格、同一物理 eta 起终点、同一 width、同一固定 core 前三个系数，以及全部原 q/core/H 坐标。lambda 固定为 1。实际尾场使用

\[
F=q+\eta a_{\rm new}e_r(\Theta)
 +(\eta H-\eta I_{\rm new})e_z
\]

及原 canonical 接口规则；新的 R 是 \(a_{\rm new}(S)\)。新 R、观测 a、完整 a/I scalar jets 和误差 carrier 都随新输入明确保存。

原 `ReferenceObserved`、`ReferenceNative`、`point_adapter` 和 physical first-jet builder 的函数本体仍来自字节冻结的 R671 源。它们通过实际新的 `reference_tail_context`、`lift_at` 和 a carrier 读取新场。新 factory 自己的 definition、profile identity、source SHA 与新节点/观测来源单独记录，不能把新 model 冒作旧 R671 definition。

`save_carrier` 与 `bundle_arrays` 委托原完整实现，但动态调用当前 `self.definition()` 和 `self.metadata()`，所以实际保存新 canonical model 和新 carrier SHA。完整 driver 将 inherited affine 和 observation metadata 的 representation 明确改为新 schema，同时保留真正物理实现的来源记录。

固定 g 并不固定 H、q 或自由 core。H 的帽平移不改变固定帽自身 metric；当前相位见证 p 仍依赖全部当前 core。幅度 v2 helper 保持完整 dp 分支、两种见证符号及真实当前新 R 的同 bits 绑定。

## 3. 原母范数与真实完整非线性筛

原 integrated/physical-height/angular-H² 母范数的尺度取决于同一 S、mesh、width、频率与 h=eta，均在这一输入更换中保留。完整 `DoubleIntegrated`、三角 physical-height map、原 coarse B/B*、原 whitening 与所有自由变量不删减。新 a/f/k 改变实际场和目标；它们没有被用来静默重定义方向范数。

完整 driver 沿用已刊 amplitude v2 的每条原几何 C 作为 prefix，追加实际选中的 D/L 两符号、帽直径及 H 行。首参数固定为 Dmarked=4.2、L=.9、Hmin=1.01，原几何工作行上限 192；幅度选行最多额外 12 条。实际行数、原缓存、新 combined 缓存及两者总 bytes 按每方向报告，不把最多行数当真实行数。

每个可能接受的 nonlinear trial 必须通过当前全 grid、全部永久 arbitrary 地点、曲率及幅度的真实同场读数。新极值与选中地点进入永久记忆，回溯拒绝不删除。记忆变化后，当前父也重新读取曲率和幅度才可开始新的可行 QP。非有限值明确 incomplete。新 helper v2 仅修复已确认的重复 `sign` 关键字记录异常；行公式与预算不变。

新 prepare 保留 q/core/H 的数值字，不等于保留物理场。新 seed 进入真正完整初始 Gram 与几何/幅度筛；旧证书不会进入当前接受条件。若该 seed 未通过，报告说明是在本有限必要筛上不能启动可行原点分支，不能据此证明数学上不可能，也不会默删见证或放松预算。之后需要明确恢复可行性或换实际输入继续。

这些屏仍是必要有限读数。最终连续 metric、embedding、全图幅度、包含反射的 E³ 商和 reach 必须用这个新场及新 profile 的完整证书支付；不能把必要 K 产品称作 reach。

## 4. 新模型的 current coarse Gram

原 [R681](../results/R681-current-J-coarse-frame-preconditioning.md) assembler 对 `tail.definition` 的源身份绑定旧 factory，因而会正确拒绝新 definition。本入口提供独立完整 `deep_scalar_coarse_moments.py`，保留原 R681 角矩、径向收缩与 whitening 的全部代数，只把 canonical definition 的核验改为实际新 factory/profile；first-jet builder 仍核原 R671 代码。

对原 coarse B 的字节冻结结构，每个 coarse 列的自由 core 首块恒为零，因此此局部收缩中 \(\delta\rho=0\)。全外层 J 仍保所有 core 自由度。以 \((\delta F_s,\delta F_\phi)\) 为六维 moving-frame 变量，三个 Gram 行的局部导数为

\[
D_{\rm loc}=
\begin{pmatrix}
2F_s^T&0\\
F_\phi^T/(a_{\rm new}\rho)&F_s^T/(a_{\rm new}\rho)\\
0&2F_\phi^T/(a_{\rm new}\rho)^2
\end{pmatrix}.
\]

当前 R664 正残差 Hessian 块作用于这些列，然后使用完整角权、原径向 weights 和原 coarse B 收缩。没有均值低秩扣除。其目标就是同一个完整 direct-fixed-scalar bridge 的 coarse \(A_c^TA_c\)，外层因子仍为

\[
\gamma=\frac{k}{\mathrm{scale}^2 C_0},\qquad
C_0=N_{\rm full}\sum_s w_s.
\]

现存同 x 的实际 physical first-jet cache、实际新 a 数组、rho、全部角行、当前 Hessian、同一个 whitening R 都进入该式；不换旧残差、旧 profile 或旧 coarse Gram。完整 assembler 的科学收缩段与原 da083 源逐行相同。

可选 SPD 准备保实际 mu、原母范数和 \(\beta=1/\mu^2\)，接 [R685 的约束 active-face inverse](../results/R685-constrained-active-face-preconditioner.md) 与 v5。小 SPD、算术或资源不可用时，在任何 PCG iteration 前明确选择同一个完整固定新 g 问题的 v3；源身份与模型错误则直接报错，不伪装成允许的模型切换。没有 jitter、谱裁剪或悄改 damping。

准备期间对真实 direct physical `jvp/vjp/residual/raw_residual` 四个入口作临时计数并在 finally 恢复原方法；报告实测 counts。没有单位列 J sweep 或新增数值 fixture。

## 5. 旧父到新 seed 的完整位置迁移

`prepare_deep_scalar_actions.py` 先使用原 exact-binary complete-history collector，从实际旧父完整 report、每次 trial/active/final 位置及显式历史 manifests 求 union，并在**旧父真实 carrier** 上解析 grid 地址。失败执行的已见点也作为明确 manifest 并入。然后才调用新 factory 的 prepare，产生新 seed、observations、nodes、reference profiles 和 `locations.json`。

新位置文件只转移同一符号 mesh 的 cell/u/physical-phi 地址。新 bundle/carrier SHA 与旧来源 SHA 分别记录。没有把旧 K、距离、Gram 或接受状态移到新场。

`launch_deep_scalar_amplitude_actions.py` 的首次模式核 actual preparation report 中 new seed、observations、nodes、locations 的字节身份，要求 CLI 实际给出的 locations 与报告相同。它只走实际新位置数组，不遍历原 provenance 中的旧地址。后继模式接受完整同固定 profile 的新 solver parent，并保全部实际 current history。两个模式都要求 source/model/eta/current carrier 一致；显式额外位置源也必须属于这个 current carrier。

## 6. 可执行初始预算与输出

[完整首三步](../computations/resume-20261126-deep-fixed-scalar-first-steps.json) 给出完整三个顺序步骤：

1. 从真实 v2 幅度父 `643627931a699a9f9a9e928ca5a6e4a61bd7855eafeaaf5b6fb434db92f0eeaa` 创建新固定 profile seed。完整父路径为 `{work}/mean-metric-design-amplitude-protected-v2-first/`，额外收失败 v1 report 与历史 compact geometry manifest。
2. 在新的 `{work}/deep-fixed-scalar-prepare-first/{seed.npz,observations.npz,nodes.json,locations.json}` 上启动真正固定 \(g_n\) 的完整两方向求解，输出 `{work}/deep-fixed-scalar-amplitude-first/`。
3. 独立完整来源 reader 只读取实际新 report，输出 `{work}/postprocess/deep-fixed-scalar-amplitude-first-summary.json`。

参数明确为 p=4、epsilon=.001、scale=.05、实际 mu=.01、2 directions × 64 advances，保持原正径向混合测度、全角 2048、原 192 C 上限及 .992/.025 必要曲率筛。R687 centered Phi 只减固定常数，原 Phi、真梯度与 Hessian 单位仍实报。

这里的 stopping threshold 显式取 1e-9，只是新分支这份数值算法的停止参数。它不是 README 的“原求解容差”定义，也不会令零步退出变成误差持续下降或机器精度收敛证据。报告和 reader 均保实际方向数、实际接受数、零步、真实 max 改变量与 stopping scope。

旧 fixed-a、R684 moving-mean 与本 fixed-new-a 的 Phi 不可直接相减。reader 只在同一次新目标、相同 p/epsilon/scale 和相同 observation normalization 下报告初末 Phi 差。真正固定问题精化还必须支付同一 profile 的合法重建/转移、同父测度比较及真实精度收敛；现有只接受旧 canonical schema 的 R676 不可通过改标签直接套用。

首次执行命令分别是 JSON `script` 加其完整 `args`。通常续接用 `--parent-report` 取代 `--preparation-report`，其余 current bundle/carrier/node/profile 仍实际绑定。不能把 old carrier 或旧 nodes 路径照抄到新分支。

## 7. 完整源与核验范围

| 完整源 | Bytes | SHA256 |
|---|---:|---|
| deep_scalar_coarse_moments.py | 28784 | dcfa30b688104b27efeddfbe6921af25ba33ba6202be43f815d5b8d8bfc69395 |
| fullclosed_deep_scalar_amplitude_qp.py | 67914 | d3c35492a9cef5b4b005829f0ce502d8a377195541b64893f4ab063f0676ba95 |
| prepare_deep_scalar_actions.py | 6808 | 5e3abe9c683731ff8c7d6ac71ec4fefff8fa6d21aafc355642f51e1c98fe953c |
| launch_deep_scalar_amplitude_actions.py | 20077 | b458ee7656bd44b82ffa996b9be4d32ecf71d1ad6fa75e181e1c4dc4bc4a0d88 |
| read_deep_scalar_amplitude_report.py | 11703 | 02c2a75204054065552ae751f1951af054d8a2af7830cfcc857e10e7f533f84c |

新 factory 绑定 `4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1`，新 scalar 绑定 `e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2`；共用幅度 helper v2 为 d494、screen v2 为 e6be，原 physical factory 为 2e0219、R685 v5 为 76b275。全 SHA 在各完整小源中逐项保存。

代理静态原始三步请求为9213 B、SHA256 `f48b4a44026b5be8a9c8ec9a73bdc7675f3b5ee26a50583b28b305f80fa641e2`；本次最终刊载请求另补实际输出身份、完整方向归因字段及两类新生缓存的自然返回清理，不改任何科学argv。最终逐值请求以本节上述链接为准。

所有五源 AST/compile 及尾空白核过。纯 `--print-command` 的 preparation 41 argv / 19 flags 与实际新 factory CLI 匹配；solver 157 argv / 77 flags 与完整新 driver 匹配。geometry 独立静态核 from_files/create_pair、new a/R carrier、save_carrier/bundle_arrays 和同模型 keep-q 边界；solver 独立核完整 R681 代数、实际 direct bridge/J、同 mu/A/C、v5 与四入口计数恢复。没有本地执行科学计算或预设性能/下降结论。

## 8. 当前已返标量与执行衔接

R690首标量 [stage54](2026-11-26-actual-deep-valley-complete-scalar-input.md) 已真实完整返回，1e−18请求未达但全域盒有效。当前prepare另消费同一明确输入并生成自身carrier；它不会把先前宽盒冒作已达到1e−18，也没有新增此前必须通过的精度门。首实际旧父64362793及其全永久位置已经存在，新seed与初始全Gram/几何必须实际读取，任何失败均保原记录继续修复或换方向。新canonical的连续reader须独立支付新a/I；旧f122不会被改标签直接消费。
