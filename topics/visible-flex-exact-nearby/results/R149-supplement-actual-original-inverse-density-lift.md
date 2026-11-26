# R149 actual IL：同一真逆坐标误差及原 finite compound 三阶导数

**已证明（公开 Actions 的四个完整有向结果）。**
会话 `visible-exact-astra-fb31ed6-20261127`，2026-11-27。

公开 run [45896427415/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45896427415)
在 source commit `eb774fb06c6cb6dc51ffac0b31e5ebe833f359b1`
触发，四个首次目标全部完成。完整
[actual](../notes/inverse_density_lift_ci/run-45896427415-1/actual-original-inverse-density-lift.json)
为 20378 B，SHA-256
`9427186020322b43d99d49fc239c2150949f3155cafc66217ac01469bea88b5e`；
完整 [execution](../notes/inverse_density_lift_ci/run-45896427415-1/execution.json)
为 19685 B，SHA-256
`8abee7df4e00e4296b6147929e10c729f852a011ea4e5e7c50a0f87874dbd499`。
两者 `complete=true`，科学对象 `proved=true`、returncode0，
只有一个 scientific child，旧目标和旧 producer 调用数均为0。

## 同一对象与全部结果球

采用 [IL.1–5](R149-supplement-complete-inverse-density-lift-derivative-bounds.md)
的原定义，$p=H\circ X_-^{-1}$ 是同一 selected 参数的真逆坐标；
$\widehat p=K_{48}\circ A_-$ 保留原第二条 terminal phase 的完整
64 阶 Fourier 系数和 rational mean。物理周期为 $\pi/2$，频率为
$4n$；误差 strip 为 $1/256$。下表逐字列出四个正式保存的完整球，
均标记 `bound="upper"`；使用时取该整球的上端点。

| 完整新目标 | 实际完整球 |
|---|---|
| $\|p-\widehat p\|_{1/256}\le E_p$ | `[2.21054222404005527958731169633697080708888809577944065467398e-7 +/- 3.08e-67]` |
| $\|\widehat p'\|_{L^\infty(\mathbb R)}\le P_1$ | `[1.02497389146846531897511147053857165825279168205072928086814 +/- 4.40e-60]` |
| $\|\widehat p''\|_{L^\infty(\mathbb R)}\le P_2$ | `[0.132456684413518897187454839768456601610926289735132693095105 +/- 4.93e-61]` |
| $\|\widehat p'''\|_{L^\infty(\mathbb R)}\le P_3$ | `[0.813048772268810782153506954847723484297119491228603649461362 +/- 2.63e-61]` |

这不是 sampled maximum，也不是两腿差的小范数。$E_p$ 使用完整
旧 W 的共轭差、R31 的正单腿参数 majorant、selected 参数变化的
完整正上界 $d_*\ge|\delta_*|$，以及 post48 的完整 transport/root
费用。$P_1,P_2,P_3$ 则分别使用所有原系数的有向绝对值和完整链式
法则。独立 terminal rotation 未并入有限 postcomposition。

## 完整准入和实际执行

[manifest](../notes/2026-11-27-inverse-density-lift-inputs.json) 为15992 B，
SHA-256 `eca231e77b0248c5585c751c157f82fc6d86985bb4fd24722bc51c9029b71a1d`。
实际 owner 的 SHA 为
`8b950580895a010414fcddf7652eb19c2c5ed4008f389ec72b5eb660ef6dc8c6`。
它先完整准入40个 current 文件及6份原历史 native；原169-cover与
wiener的全部258个 rational complex coefficient pairs一致，两个
central imaginary components 精确为0，正负频精确共轭。
全部原 source、process、publication、manifest 和整载体 SHA 都在
actual 的 `whole_completed_inputs` 与 execution 的 receipt 中保留。

实际 Python3.12.14、python-flint0.9.0、320 bits；四个新结果分别
candidate保存、整球读回、正式保存、再次读回。科学 child 的实测
wall time 为0.23988039200003186秒。原 ODE、KAM、Wiener widening、
post48 fit、旧 DFT、旧 residual/norm 目标均未再次执行。恢复的历史
载体仅在 Actions 临时目录中使用，仓库未重新加入这些数据或数组。

## 直接后继与结论范围

这份完整对象可直接供
[IR](R149-supplement-complete-inverse-density-row-residuals.md) 的96条
same-sign inverse-density行认证消费；无需再计算 $E_p$ 或上述三个
导数。它也提供
[DB](R149-supplement-complete-Theta-row-regularity-and-negative-window-density-inverse.md)
的 true-map Cauchy 导数补项所需完整输入。

本次尚未计算96条行、施加原 $A$、支付 $\Theta$ 的实际 one-loss
误差或闭合 physical mean/$\nu$/phase Schur。正侧全逆、真实 PDE
signed matrices 以及本课题的非线性完成标准保持各自原义务。
