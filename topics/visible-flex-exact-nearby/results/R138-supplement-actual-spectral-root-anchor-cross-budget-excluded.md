# R138 实际结论：谱体与根锚容量的交叉门仍被排除

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

**已证明：** 完整SG实际结果虽然通过自己的body三门和RN逐项必要筛查，
但把它与当前RA标量容量接收器及relative的非负二变量费用组合后，完整
$2\times2$吸收门仍不可能通过。只需已有两个SG整球与RN已证根EE下界，
无需新的积分、有限Gram、高逆或数组。

本结论只排这个明确的所选充分预算；不证明实际边界问题奇异，
不排真正全高逆、可达根迹或采用不同signed能量结构的其他方法。

## 1. 完整新SG实际输入保持成功

run **44767124478/1** 的整个科学结果及execution为：

| 文件 | bytes | SHA256 |
|---|---:|---|
| [spectral-body-energy-budget.json](../notes/spectral_body_energy_budget_ci/run-44767124478-1/spectral-body-energy-budget.json) | 24640 | `24c5923eb7a0b34c566c785ec11e33e7881b3ce6c35613a60cb9532238cf1b5e` |
| [execution.json](../notes/spectral_body_energy_budget_ci/run-44767124478-1/execution.json) | 15484 | `ce2787cd11267f3d47dcbab8f2dd76851ca64ebec09a72767bac313235f7438a` |

科学结果 `complete=proved=true`、`failure=null`，整个4651片完成，保存5条新球。
其body三门与原声明的三个RN必要比较都为true，这些原结果不改为false。
本篇检验的是另外的、含完整根预算的二维吸收门。

只读本次的两条完整上界记录：

| 字段 | midpoint integer | radius | exponent |
|---|---|---:|---:|
| `aEE_spectral_upper` | `74816542958334535116379100769473178089148570072783772646639111335480792824882377` | 2 | -80 |
| `aEB_spectral_upper` | `60036018934862754788552480743099657439132622985318147039712942401887941116256548` | 2 | -80 |

依原 `complete_decimal_ball_v1`，$[M-R,M+R]10^e$ 是整个保存球。
其lower端直接、严格给出两个有理比较

$$
a_{EE,sp}>7/10,\qquad a_{EB,sp}>3/5.
\tag{RX.1}
$$

这些是已选且保存的算法upper本身的数值lower比较，不是实际残差或最优
体误差的lower。整个 $a_{BB}\ge0$原值保持；下文只故意把它放宽为更有利的0。

## 2. 全高Schur必要性给出的根EE下界

[RN.9–RN.14](R138-supplement-root-anchored-spectral-budget-necessary-screen.md)
已经用原high41的完整frame/mean包围严格给
$\|\omega_{96}\|_2<1$、$\|\omega'_{96}\|_2<377$。
同一个原RS integrand逐点受 $(24/25)$旧integrand控制，故旧whole $T<125$
直接给改进试探上界 $\widehat T<120$。这一证明没有重跑原单积分。

因此不论原低负型通过怎样的真正 $D_H^{-1}$、角依赖正压缩乘子逆或更紧
完整high Schur得到，只要继续使用RA/LC的同一个标量容量读出与relative
非负费用格式，根费用必满足

$$
b_{EE}\ge\bigl(\alpha_E^{root}(W)\bigr)^2>37/30,
\qquad b_{EB}\ge0,\quad b_{BB}\ge0.
\tag{RX.2}
$$

源 $H$、其mean、physical-density费用与剩余high/source Young费都保留；
它们在该格式中只增大相应非负系数。只用(RX.2)的更有利放宽，并不在实际
根映射里将这些源置零。

此处没有使用已被RN.17单独排除的统一 $\lambda_H^{-1}C^*C$代替整个high逆。
即使真正 $C^*D_H^{-1}C$能够达到这条必要根界附近，下面的交叉费用已经足够。

## 3. 一个准确有理方向使最终矩阵无法正定

原relative R.30的完整吸收矩阵为

$$
\mathcal M=
\begin{pmatrix}
2-a_{EE,sp}-b_{EE}&-(a_{EB,sp}+b_{EB})/2\\
-(a_{EB,sp}+b_{EB})/2&1-a_{BB}-b_{BB}
\end{pmatrix}.
\tag{RX.3}
$$

取有理测试方向 $(\sqrt E,\sqrt B)=(1,3/10)$，只用(RX.1)–(RX.2)即有

$$
\begin{split}
(1,3/10)\,\mathcal M\,(1,3/10)^t
&<\left(2-\frac7{10}-\frac{37}{30}\right)
   -\frac35\frac3{10}+\left(\frac3{10}\right)^2\\
&=\frac1{15}-\frac9{100}
=-\frac7{300}<0.
\end{split}
\tag{RX.4}
$$

所以 $\mathcal M$不正定，完整三门不可能全true。这个测试比只看第一对角项
严格更强：RN逐项必要比较仍可全通过，已有body交叉项却已经超过所剩余量。
测试方向只是这一个预算矩阵的代数见证，不是声称实际未知PDE方向能够自由
选择该 $E/B$比，也不是构造实际BVP的非零核。

## 4. 后继范围

同一SG/RA/relative非负费用组合下，重新构造更大的finite Gram、提高高逆截断
或仅把已成统一lambda换成真正high逆，不能修复(RX.4)；本篇已对真正high
Schur保留其最有利必要根界。原5条SG scalar、其条件性allowance、RD的局部
Gamma、原high positivity、low96核迹injectivity等结论仍然有效。

要继续能量路线，须实质改变被使用的体/根比较或利用本格式未消费的signed可达迹
关系，而不能把已排预算的strict gate重标为true。原直接逆、完整物理外行、
负区/germ/接口与全局非线性目标依然按各自合同推进。
