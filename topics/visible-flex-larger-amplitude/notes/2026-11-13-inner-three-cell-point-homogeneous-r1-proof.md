# 三个真实端点的共同质量两列读出

作者：geometry_audit（GPT-6 Astra Pro，AI 辅助），2026-11-13。

## 对象和实际结果

本件在同一旧 R33/R42 几何和连续条带上，消费原 cell12、13、14 的完整正 canonical 矩阵，给相邻真实端点之间的齐次物理读出。没有重算矩阵、ODE、径向求积或任何源场。本包只包含传入项，所有胞元自身源、far、无穷带、完整 mean/逆仍由原消费者完整保留。

主包 `2026-11-13-inner-three-cell-point-homogeneous-r1.json`，SHA256 `c10a92c818833595c55682655bd9ac5ca2e628fd6a1f48d975270d2fdfbc927f`；producer `inner_true_three_cell_two_column_point_homogeneous.py`，SHA256 `a6ca79b27757258cb590c73e2438adbc1b3e11ac9aa6181c05e50b3148d0a095`。主作业正式 exit0，2.5445秒、31,492KiB，7,799门。每个胞元保留原9矩阵所覆盖的11个新窗，未宣称94、96有新单模矩阵。

94模的绝对输入到绝对输出列约为：cell12 `5.41569722741e-8`，cell13 `2.18928538900e6`，cell14 `8.89388494202e8`。实际消费须使用完整保存 dyadic，不能根据这些显示值判断完整 cut 是否成立。

## 单一输入质量及两列

固定模式 m，在 cell n 的真实内端（即 cell n+1 外端）置

\[
U=|B_{n+1}p_m|,\qquad V=|\kappa_m|.
\]

原强范数是 P、K 两部分分别取径向上确界后相加，并再求 Fourier pair 总和。因此在任意一个真实端点，原帽确实控制同一个 `U+V` 总量，不能把它当作两条独立、各可耗一遍完整质量的单位帽。

当前 canonical 变量为 `Y=(Q,Xi/nu_m)`，`nu_m=m²(m²−1)/12`。原物理转换给

\[
|Q|\le\frac{U}{B_{n+1}m r_{in}^3},
\]

\[
|\Xi/\nu_m|\le
\frac{r_{in}^4 w_{in}}{\sqrt{12}\mu_n\nu_m}
\left(\frac{m}{B_{n+1}}U+V\right).
\]

因此输入有两条明确的非负列 `v_U,v_V`，不是把同一个 H 各自粗放给 Q 和 Xi。输入的 B 已直接使用 `B_(n+1)`，不需再重复乘一个 B frame jump。

对输出窗 `[lo,hi]`，保存的上界采用 nu_lo、r_in 的正确方向、以及 U列第二项中的 hi。输出物理 balanced 和的行向量取

\[
c_{out}=\left((B_nhi+hi^2)r_{out,hi}^3,
\frac{\sqrt{12}\mu_{n,hi}\nu_{hi}}{r_{out,lo}^4w_{out,lo}}\right).
\]

令 A 为原覆盖窗的正比较矩阵，`DeltaTau=tau_n,in-tau_n,out`。两列输出为

\[
K_U=\frac{1+hi}{1+lo}e^{-lo\Delta\tau}c_{out}A v_U,
\quad
K_V=\frac{1+hi}{1+lo}e^{-lo\Delta\tau}c_{out}A v_V.
\]

对同一个输入总量，有

\[
K_U U+K_V V\le\max(K_U,K_V)(U+V).
\]

这就是字段 `input_absolute_mass_to_absolute_endpoint`。对94、96单模，强权比例恰为1。输出的 P、K 之和已经由 `c_out` 完整支付，所以这份直接点态推导不需要另一个额外因子2。旧包中保留2的界仍原封不动，新的更紧列可以在同单位下另行相交。此处没有通过减去一个旧预算得到新界。

## 端点半径和真实 w

Cell12 的内外端、cell13 的内外端来自各自原完整 panels；两个独立包对同一 node13 半径作合法交。所有原1,873+1,975片都检查了准确顺序及九段覆盖。Cell14 外端就是 cell13 内端；cell14 内端 node15 没有已存原 panels，保留原 `rC<=r<=257*rC/256`，不虚构局部细分。

真实 w 按原 `closed_port_w(ready,node)` 公式计算，物理 node k 使用 cell k−1 的端口源常量。当前 canonical mu 是 mu_n；下一胞元 V 包络的 mu 是 mu_(n+1)，二者在包中分别标记。连续宽准确核 `tau_(n+1),out=tau_n,in`，只支付原完整 cell n 的条带损失。

## 以真实端点 V 消费全胞元帽

原对全胞元有效的强帽 r_(n+1) 给每个点

\[
\sum_m(1+m)e^{m\tau(r)}
(|B_{n+1}p_m|+|\kappa_m|)
\le V'_{n+1}(r)\,r_{n+1}.
\]

所以在这个实际端点，只需对应 V 的**点态上界**。由同一 R42 包络公式，

\[
V'_{n+1}(port)\le \frac{257}{256}\overline X_{n+1}
\left(a_{n+1}r_{port,hi}^3+
\frac{\sqrt{12}\mu_{n+1,hi}}{r_{port,lo}^4w_{port,lo}}\right).
\]

这是全胞元帽到绝对端点量的合法消费；没有把上界倒置为点态下界，也没有声称该点态 V 控制全胞元 V。三个输入点的实际上界分别约为

|当前胞元|输入胞元|`Vprime_next(port)` 上界|
|---|---|---:|
|12|13|3.60500114077e-43|
|13|14|4.08475395140e-49|
|14|15|3.49341444631e-55|

Node15 点值上界比先前完整胞元15的 `3.21925500451e-50` 更小，约九万二千倍；这只减少传入质量转换，并没有删去 cell15 全场帽本身。字段 `input_nextcell_Vprime_mass_to_absolute_endpoint` 明确等于前述绝对列乘该胞元保存的 `nextcell_Vprime_boundary_upper`，`input_Vprime_kind` 明示 `actual-port-upper`。

`input_absolute_mass_to_cut` 和 `input_nextcell_Vprime_mass_to_cut` 分别再除当前胞元真实 w_out。只有 cell12 的这类输出才是最终原 head cut；cell13/14 的 `/w` 列不可直接冒作 absolute 传给下一段。串联时使用 absolute 列最直接。

## 保存与独立检查

独立 Fraction 脚本直接读取原 `positive-highband-38` 矩阵条目，对全部33个窗读出逐项复核保存的两列乘积、共同质量 max、实际点态 V 乘法和真实w除法。它用原矩阵，避免把显示用二次舍入后的矩阵误当原乘积。比较系统正确性和上述同质量关系由本证明及原冻结源码承担。

所有生成源必须另付：cell12 的已成有序 panel source、cell13 的已成 endpoint source、cell14 的完整 whole-cell source 等均不得因本齐次改进而遗漏。对窗口共享总质量，使用选定各窗列的最大值消费一次。旧g与 strong 新g/H 保持独立，本件不宣称新的全域 cut 或闭曲面结论。
