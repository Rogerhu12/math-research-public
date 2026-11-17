# 不含 µ 的有限混合 Darboux 系统

会话：`true_a_analysis`。下式是原有限 Fourier momentum 方程的变量变换。它不主张任意边界数据都有解，也不主张局部 Gram 奇异处的全局边值 Jacobian 必可逆。

## 变量与完整非线性密度

沿任意已给定的物理剖面参数 x，记 `s=r_x/r`、`ell=(log w)_x`。原代码的非均值高度变量为 `Q_j=H_j/r^4`，momentum 为 `pi_j`。在正交归一的非均值实 Fourier 基下，定义

\[
v_j=\frac{r^3Q_j}{\sqrt2 w}=\frac{H_j}{\sqrt2 rw},\qquad
t_j=\frac{\varepsilon\sqrt{12}\,\mu}{\sqrt2 r^4w^2}\pi_j.
\]

`epsilon` 是原 radial orientation；它与 `s` 的实际符号不要混用。令 `v(u)` 表示归一高度的非均值 Fourier 和，L 包含独立零模及全部表示的非均值模式。记

\[
P=\partial_u v,\quad T=\partial_u^2v,\quad K=L-T,
\quad U=\partial_uL-(\partial_u^2+1)P,
\]

\[
E=1+w^2,\quad D=1-w^2(2K+K^2+EP^2),\quad S=1-w^2P^2,
\quad A=1+K+ET.
\]

用原程序完全相同的非线性密度

\[
B=\frac{2K+K^2+EP^2}{\sqrt D(1+\sqrt D)}
 +\frac{(1+K)T}{S\sqrt D},\qquad
F=\frac{(1+K)U}{S\sqrt D}.
\]

有限离散 Fourier 投影记为 Pi_N；均值与非均值投影均完整保留。代数约束是

\[
\Pi_N B=(0,t).
\tag{A}
\]

实现可用原 `moments=L+quad` 的消去线性项写法，数值上更稳定；不能删掉零模或非线性乘积。所有求积点仍要求原严格 D/S 下界。A 或有限 Gram 不作为新的正定性假设，但应报告其符号、谱和条件数。

## 等价的显式微分部分

原 Q 方程给出

\[
v_j'=\big((m_j^2-1)s-\ell\big)v_j+sL_j.
\tag{V}
\]

在 t 的导数中，原 pi 方程的 `4s pi` 与比例因子的 `-4s` 恰好相消，得到

\[
t'=-2\ell t+s\,\partial_u(\Pi_N F).
\tag{T}
\]

对仅 cosine 的表示，最后一项第 j 分量就是 `s m_j <F,sqrt(2)sin(m_j u)>`，与原代码逐项一致。对同时包含 cosine/sine 的表示，该有限基的导数矩阵给出 `-s Q_N(F phi_j')`。这里的顺序是先作实际离散投影，再对有限 Fourier 和求导，因而完整保留原程序的非线性 alias；不以点态求导后再求积来替代它。

均值高度可在完成后积分 `z_mean'=r_x w(1+L_0)`。在 r,w 连续的物理 cell 接口，v,t,L 都是物理变量，无须使用内部 µ 缩放。非常小 w 仍可能导致数值动态范围问题；变量变换并未证明任意深度的稳定条件数。

## 混合边值离散

设有 k 个径向区间，端点加中点共 `2k+1` 个节点，每节点保留 `(v,t,L)`。设非均值维数为 d（reflection 情形 d=M；完整 cosine/sine 情形 d=2M），则每节点有 `3d+1` 个未知。

每个节点施加 d+1 条约束 (A)。对微分状态 y=(v,t)，每个区间用完整 Hermite–Simpson 两组约束

\[
y_m-\tfrac12(y_l+y_r)-\tfrac h8(f_l-f_r)=0,
\]

\[
y_r-y_l-\tfrac h6(f_l+4f_m+f_r)=0.
\]

再加 2d 条真实边界条件。方程数是
`(d+1)(2k+1)+4dk+2d=(3d+1)(2k+1)`。
这套残差是原方程的有限边值离散，没有在任一点除 A 或求 G 的逆。全局 Jacobian 是否可逆仍必须实测；局部 G 奇异不自动导致，也不自动避免，全局问题的奇异。

## 精确锥回归

R10 常斜率锥中 `ell=0`，非均值高度 H_j 与 r 成正比，所以 v 常数，且

\[
L_j=-(m_j^2-1)v_j.
\]

于是 U 恒为零，(V) 与 (T) 的右端都严格为零。独立求解均值约束并计算完整 t 后，可以逐项检查代数式、微分式、方向 Jacobian 和边值求解。这个回归也可同时使用 cos/sin：旋转材料角只将相应的两列作正交旋转。

单锥回归不等于反射非平谷中可穿过 A=0。尤其反射轴上混合第二基本形式为零且 K_g 不为零时，有限曲率的精确 Gauss 方程禁止该轴 A 为零。探索非反射核时必须保留完整 cos/sin、检查混合第二基本形式和点态 Gauss 残差；不能仅凭有限线性代数成功声称几何可行。
