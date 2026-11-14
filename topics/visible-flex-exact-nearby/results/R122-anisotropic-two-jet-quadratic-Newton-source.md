# R122：真实 Newton 二次源的各向异性二阶恒等式

2026-11-13，visible-exact-astra-ac0d。

**状态：已证明的精确恒等式及完整点态估计。** 本篇接 R117/R118，保留真实更新后的球面坐标。新的二次源没有单独的径向纯二阶平方或角向纯二阶平方；这允许在得到实际修正场以后，直接使用它的各向异性二阶数据。本篇没有供应尚缺的完整强逆，也没有证明某个未算出的修正场满足收敛条件。

## 1. 固定目标、真实更新和坐标

令 $F:M\to\mathbb R^3$ 是当前 $C^2$ 严格星形嵌入，$g_0$ 是一次固定的目标度量。设 $V:M\to\mathbb R^3$ 是 $C^2$ 修正，记

$$
f=g_0-g_F,\qquad \mathfrak r=f-Dg_F[V],\qquad F_+=F+V.
\tag{122.1}
$$

假设 $F_+$ 仍是严格星形嵌入。这个性质须由实际图的 $C^1$ 正性与全局嵌入预算另证；本篇不从一个二阶形式恒等式推出它。

令 $\chi_+:S^2\to M$ 是 **$F_+$** 的径向投影的反映射，并在标准单位球面 $(S^2,\sigma)$ 上定义

$$
W=V\circ\chi_+,\quad
\rho_+=|F_+\circ\chi_+|^{-1},\quad a=\rho_+^2,\quad
\overline{\mathfrak r}=\chi_+^*\mathfrak r.
\tag{122.2}
$$

所有下面的梯度、Hessian、迹和正交标架都属于同一个更新后的球面图。不能把旧球面图中的 $D^2V$ 原样代入本篇的 $\nabla_\sigma^2W$。

由欧氏诱导度量的准确二次展开，

$$
g_{F+V}=g_F+Dg_F[V]+dV\mathbin\cdot dV.
$$

所以更新后的真实缺陷准确为

$$
f_+:=\chi_+^*g_0-g_{F_+\circ\chi_+}
=\overline{\mathfrak r}-dW\mathbin\cdot dW.
\tag{122.3}
$$

这里的点积是环境 $\mathbb R^3$ 的点积。尤其当原应变方程被精确求解时，$\mathfrak r=0$；没有选择新的目标来消除这项残差。

沿用 R117 的完整球面兼容算子

$$
\mathcal C T=\operatorname{div}_\sigma\operatorname{div}_\sigma T
-\Delta_\sigma\operatorname{tr}_\sigma T
-\operatorname{tr}_\sigma T,
\qquad q_+=-\tfrac12\mathcal C(a f_+).
\tag{122.4}
$$

## 2. 二阶张量恒等式

记 $U=dW$、$H=\nabla_\sigma^2W$、$T=dW\cdot dW$，以及一形式

$$
Z_i=\langle W_i,\Delta_\sigma W\rangle
-\sum_j\langle H_{ij},W_j\rangle.
\tag{122.5}
$$

**引理122.1。** 对每个 $C^2$ 的 $W:S^2\to\mathbb R^3$，$\mathcal CT$ 在分布意义下具有连续代表，且

$$
\mathcal CT=|\Delta_\sigma W|^2-|H|^2-2|U|^2.
\tag{122.6}
$$

**证明。** 先设 $W$ 光滑，对每个环境分量逐项求和。在一点的球面正交正规标架中，

$$
(\operatorname{div}T)_j
=\langle\Delta W,W_j\rangle+\tfrac12\nabla_j|U|^2.
$$

再散度一次并减去 $\Delta\operatorname{tr}T+\operatorname{tr}T$，得到

$$
\mathcal CT=|\Delta W|^2+\langle U,d\Delta W\rangle
-\tfrac12\Delta|U|^2-|U|^2.
$$

标量 Bochner 恒等式在单位球面上为

$$
\tfrac12\Delta|U|^2=|H|^2+\langle U,d\Delta W\rangle+|U|^2.
$$

最后一项来自 $\operatorname{Ric}_\sigma=\sigma$；也可直接交换第三协变导数得到。两式中的三阶项准确抵消，得到 (122.6)。对 $C^2$ 的 $W$ 作 $C^2$ 光滑逼近：右侧一致收敛，$T$ 的兼容算子在分布意义下收敛，因此同一等式和连续代表仍成立。$\square$

对任意对称二张量 $T$ 逐项使用乘积法则，有

$$
\mathcal C(aT)=a\mathcal CT
+2\langle da,\operatorname{div}T-d\operatorname{tr}T\rangle
+\nabla^2a:T-(\Delta a)\operatorname{tr}T.
\tag{122.7}
$$

当 $T=dW\cdot dW$ 时，中间的一形式恰为 $Z$。这给出完整坐标无关公式

$$
\boxed{
\begin{aligned}
q_+={}&-\tfrac12\mathcal C(a\overline{\mathfrak r})
+\frac a2\bigl(|\Delta W|^2-|H|^2-2|U|^2\bigr)\\
&+\langle da,Z\rangle
+\tfrac12\{\nabla^2a:T-(\Delta a)\operatorname{tr}T\}.
\end{aligned}}
\tag{122.8}
$$

若 $\mathfrak r=0$，整个右侧只含当前真实更新图和修正场的二阶数据。近似应变逆留下的首项必须另付完整兼容源；只有 $\|\mathfrak r\|_{C^1}$ 的界不能删除它。

## 3. 无纯二阶平方的完全展开

在一个正交标架 $(e_1,e_2)$ 中写

$$
u_i=\nabla_iW,\qquad H_{ij}=(\nabla^2W)_{ij},\qquad
a_i=\nabla_i a,\quad a_{ij}=(\nabla^2a)_{ij}.
$$

二维对称 Hessian 满足准确恒等式

$$
\tfrac12\bigl(|\operatorname{tr}H|^2-|H|^2\bigr)
=H_{11}\cdot H_{22}-|H_{12}|^2.
$$

同时

$$
Z_1=u_1\cdot H_{22}-u_2\cdot H_{12},\qquad
Z_2=u_2\cdot H_{11}-u_1\cdot H_{12}.
$$

因此对精确应变修正 $\mathfrak r=0$，

$$
\boxed{
\begin{aligned}
q_+={}&a\{H_{11}\cdot H_{22}-|H_{12}|^2-|u_1|^2-|u_2|^2\}\\
&+a_1\{u_1\cdot H_{22}-u_2\cdot H_{12}\}
+a_2\{u_2\cdot H_{11}-u_1\cdot H_{12}\}\\
&-\tfrac12a_{22}|u_1|^2-\tfrac12a_{11}|u_2|^2
+a_{12}u_1\cdot u_2.
\end{aligned}}
\tag{122.9}
$$

没有 $|H_{11}|^2$ 或 $|H_{22}|^2$。这不是忽略项，而是完整兼容式中两个纯二阶平方准确相消。混合项 $|H_{12}|^2$ 和所有球面曲率、权函数导数项均保留。

## 4. 可供逐盒计算的各向异性界

在同一个已认证点或连续区域上，假设有真实两阶数据的上界

$$
|u_i|\le U_i,\quad |H_{11}|\le X,\quad |H_{22}|\le Y,\quad
|H_{12}|\le Z_*,\quad
0<a\le A_0,\quad |a_i|\le A_i,\quad |a_{ij}|\le A_{ij}.
$$

由 (122.9) 直接得到

$$
\boxed{
\begin{aligned}
|q_+|\le{}&A_0(XY+Z_*^2+U_1^2+U_2^2)\\
&+A_1(U_1Y+U_2Z_*)+A_2(U_2X+U_1Z_*)\\
&+\tfrac12A_{22}U_1^2+\tfrac12A_{11}U_2^2+A_{12}U_1U_2.
\end{aligned}}
\tag{122.10}
$$

更精细时可直接把 (122.9) 的点积作为相关量作区间运算，不必先取三角上界。式 (122.10) 只作充分估计，不从某个大上界推导真实源不小。

例如某一方向的 $Y$ 较大时，二阶部分只以 $XY$ 与 $Z_*^2$ 出现；是否有用取决于同一实际修正场的 $X,Z_*,U_i$。不能单凭方向性直觉便宣称该修正的二次源小。R120 所记录的**初始**源大值也不属于 (122.9) 的更新后源，不能混用。

## 5. 在材料坐标直接消费，不需要数值反解球面坐标

令

$$
y_+=F_+/|F_+|,\qquad s_+=y_+^*\sigma,
\qquad a=|F_+|^{-2}
$$

为材料坐标中的真实量。只要径向投影是前述已认证的微分同胚，$y_+$ 就是 $(M,s_+)$ 到球面的等距坐标变换。因此可直接用

$$
(\nabla_{s_+}^2V)_{ij}
=\partial_{ij}V-\Gamma(s_+)^k_{ij}\partial_kV
\tag{122.11}
$$

在材料坐标计算 (122.8)，或取相对于 $s_+$ 的真正正交标架代入 (122.9)。$s_+$ 的一阶 jet 只需要 $F_+$ 的二阶 jet，所以 (122.11) 没有隐藏当前几何三阶需求。

材料密度源为

$$
q_{+,\mathrm{mat}}=j_+q_+,\qquad j_+=\sqrt{\det s_+}
\tag{122.12}
$$

（在所用正向材料面积坐标中）。分量和密度必须在同一盒内同时包围；不能把球面标量源上界直接认作材料源上界。

实际计算可以先保留坐标不变形式 (122.8)：其中 $|\Delta V|^2-|\nabla^2V|^2$ 应通过二维混合行列式的相关式形成，避免先分别包围两个大平方。若选择正交标架，必须另外控制从原材料坐标到该标架的真实变换，不能把 $(r,\theta)$ 无条件当作单位正交方向。

## 6. 与本题其余缺口的连接

本篇允许在实际强逆产出修正 $V$ 以后，替代 R118 的统一 $C^2$ 平方粗估计，直接支付更新后的二次源。它没有改变 R118 已证的界，也没有缩小或重定义固定目标。它还准确保留了近似逆的线性兼容残差项。

当前仍需同一个真实完整反馈强逆、实际修正的连续全域二阶数据、更新图的正性/嵌入、对应的强角档和收敛预算。高角 Sobolev 或解析范数必须对 (122.9) 的全部乘积另作相应估计；本篇的点态恒等式不自动提供那些高档。最终可见位移、固定开帽和 reach 也仍须由同一极限族实现。
