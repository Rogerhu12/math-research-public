# 实际 H、参数端点与完整平方返回的可执行接口

2026-11-12，visible-exact-astra-f6a2。实际有限 H 部分已算；全流与 KAM 门仍未齐。

`scripts/fourfold_parameter_endpoint_kam.py` 接 R82 的完整三个有序积分，
保留全部 Fourier 乘积频率、三个系数选择费、真实流误差和完整三阶 Taylor 余项。
`endpoint_three_orders` 返回真实端点及其一二参数导数的同带有限近似和全误差；
没有将中心参数导数当成整个参数盒的界。

同一准确 H516 与 q1024 的 Neumann 乘积已实际重算。全频 reciprocal 误差在
A_(1/512)、A_(5/2048)、A_(1/256) 分别小于 2.509e−13、3.503e−13、1.049e−12。
它们是当前 H 的误差，非其他初值共轭的继承常数。文件
`2026-11-12-actual-finite-H-parameter-endpoint-budgets.json` 记录准确输入 SHA 和完整有向值。
`half_return_data` 对完整有限 P1 与 q(x+d) 的乘积取有符号零模，并加 R82 (82.31)
的全部误差；复指数与有限运算的舍入保持在 Arb 球内。

## 完整返回的导数和横截

令同一参数盒的 C_p=x+d+u_p 在外宽 a 上满足
||u||≤U、||∂p C||≤P、||∂p² C||≤T，且中心 ||u_0||≤ε。
在内宽 b<a 上取 Δ=a−b>U，d_*=Δ−U。Fourier Cauchy 界给

$$
J=1+\frac{U}{e d_*},\qquad Q_C=\frac{P}{e d_*},\qquad B_C=\frac{2U}{d_*^2}.
$$

真实全返回是 G=C∘C，所有复合路径留在所付外带。两次链式法则准确给

$$
P_G\le(1+J)P,\quad Q_G\le2JQ_C+B_CJP,
$$
$$
T_G\le(1+J)T+2Q_CP+B_CP^2,\quad B_G\le B_C(J^2+J).
$$

中心误差 ||G_0−x−2d||_b≤2ε。中心平均并不准确等于半返回平均的两倍：

$$
\partial_pG_0=C_{p,0}(C_0)+(1+u'_{0}(C_0))C_{p,0}.
$$

先与 C_{p,0}(x+d)+C_{p,0}(x) 相减，再分别用线段积分和乘积界，得到

$$
\left|\langle\partial_pG_0\rangle-2\langle C_{p,0}\rangle\right|
\le Q_C\varepsilon+\frac{\varepsilon P}{e d_*}.
$$

这里 u'_0 用中心 ε 支付，参数盒只以 U 支付复合域。故已证半横截 σ 时，
完整横截下界是 2σ 减去右端，必须仍严格为正。函数 `half_to_full_bounds`
逐项实现这些界，保留真实平方关系，绝不对保存的 A=P∘H 直接平方。

`r31_gates` 同时检验 R31 的小误差、真实参数盒和解析域三门，输出参数/共轭
总位移。它是有向算术接口；只有实际全参数输入均已支付才可宣布真实 KAM。
当前 finite-only CLI 明确输出 actual_R31_accepted=false。

## 下一实际输入

完整前向 g0 密度继续由 v2 controller 从已保存前缀推进。signed g1/g2 首419叶已完成，
其全腿积分及真正窄参数盒 B2 仍由参数源程序计算。最终还会用有限 P1*q 的真实
导数范数与全误差支付 Q，避免以极粗 P/(eΔ) 作为唯一选择。以上接口不宣称
等距 PDE 的全反馈逆、低块或非线性零解已经完成。

## 以有限导数支付 Q，并稳定到真实参数盒

另一个独立接口 `scripts/fourfold_parameter_sharp_spatial.py` 保持上述已算有限 H
程序不变。设在外宽 a 已严格知道中心

$$
\|C_{p,0}-L\|_a\le e_1,\qquad L=P_1q(x+d),
$$

其误差正是 (82.31) 推导给出的**全 A_a 范数**界，不只平均误差。
在整个参数盒 |p−p0|≤η 上另有 ||C_pp||_a≤T。于内宽 b<a，逐模 Cauchy 和实参数
微积分基本定理准确给

$$
P_b\le\|L\|_b+e_1+\eta T,\qquad
Q_b\le\|L'\|_b+\frac{e_1+\eta T}{e(a-b)}.
$$

有限 L、L′ 的所有乘积频率均保留。未知真实函数的宽损失只乘完整误差和参数
变化，没有把有限主部的实际导数扩大成 ||L||/[e(a−b)]。统一 u 界仍支付 B、J
及平方的复合域；平方平均误差可用中心 P、Q 和中心 u′ 界进一步收紧。
这些公式不依赖额外第三参数导数，但 T 必须已在真实整个盒中支付。


## R86 接法与真正全参数盒（2026-11-12 15:58UTC）

新入口 `fourfold_parameter_endpoint_spatial_v2.py` 保留上述所有端点有限乘积、
全频率和真实三阶 Taylor 费，只把三个坐标误差换成 R86 的空间导数预算。
在实际轨迹带上，令 $A_j,B_j,C_j$ 是三条真实源及其有限近似的公共积分上界。
严格检查 $A_0<s_d-\sigma$ 后，普通参数导数满足
\[
 Z\le e^{A_1}B_0,\qquad
 W\le e^{A_1}(C_0+A_2Z^2+2B_1Z).
\]
这是变分方程的 Gronwall 上界；同时可用所选完整有限 $w_1,w_2$ 与已付坐标误差
之和收紧 $Z,W$。两种上界均真实成立，取较小者。不能从部分段运行声称完整返回。

对共同实参数盒 $|p-p_0|\le\eta$，参考 $Y,q$ 独立于参数；因此
\[
 A_j^{\rm box}\le A_j^{\rm center}+\eta B_j^{\rm box}.
\]
若基础有限源仍选中心的多项式，则其完整误差也必须付
$E_{0j}^{\rm box}\le E_{0j}^{\rm center}+\eta B_j^{\rm box}$。
uniform cover 的 $B_j,C_j$ 必须在同一盒、同一物理对象、同一标签带上证明；
只用中心 $A_j$ 或中心 $C_j$ 都不够。

全盒无需另求二阶有限多项式即可得到较粗但真实的统一上界：先用上式的
$A^{\rm box},B^{\rm box},C^{\rm box}$ 计算 $Z,W$，取
$r=\sigma+A_0^{\rm box}$、$Q_0=1/4+\|U'\|_{A_r}$、
$Q_1=\|U''\|_{A_r}$，则归一端点 $\Gamma=4Y_{\rm end}(X)$ 给
\[
 P_\Gamma\le\mathcal H(\sigma-a)4Q_0Z,\qquad
 T_\Gamma\le\mathcal H(\sigma-a)4(Q_1Z^2+Q_0W).
\]
这里 $\mathcal H(d)=\sqrt{2\coth d-1}$，支付真实 sup 到 Wiener 的严格带损。
先检查整个参数盒的 R63 逆门
$R(E_{\rm center}+\eta P_\Gamma)\le r_H/2$，才可以写
\[
 P_C\le\widetilde R P_\Gamma,\qquad
 T_C\le\widetilde R(T_\Gamma+B_H P_C^2).
\]
若中心 signed 多项式已经给 $\|C_p(p_0)\|_{A_a}\le P_0$，利用真正
全盒已知的 $T_C$ 可再取 $P_C\leftarrow\min(P_C,P_0+\eta T_C)$，然后以
这个已证明较小的 $P_C$ 收紧 $T_C$。有限次交替每一步都从有效上界出发，
不预先假设一个有利的二次方程根。最后
$U_C\le\min(R_{\rm disp}(E_{\rm center}+\eta P_\Gamma),
 u_{\rm center}+\eta P_C)$。这使粗正值全盒一阶上界不会无必要地放大
$B_H P_C^2$；仍须把所有真实全550段输入补齐后才执行最终 R31 门。

## 中心一阶源和全盒二阶源的混合选取

全盒一阶源的逐点参数区间误差，若再付空间 Cauchy 费，可能无必要地放大
R86 的 $2B_0E_{11}$ 项。已有精确中心 $g_1$ 与真正全盒 $g_2$ 时，可直接选
三个有限近似为 $(\widehat g_0^c,\widehat g_1^c,\widehat g_2^I)$。
这是不同来源的三个准确有限多项式；R86 从未要求它们自己形成一个参数族。
真实源仍必须是同一族的 $g,g_p,g_{pp}$。

在同一个轨迹标签带及共同实参数盒，普通参数微分与空间微分可交换，故对
$j=0,1,2$，实参数微积分基本定理给
\[
 B_j^I\le B_j^c+\eta C_j^I,\qquad
 A_j^I\le A_j^c+\eta B_j^I,
\]
\[
 E_{1j}^I\le E_{1j}^c+\eta C_j^I,\qquad
 E_{0j}^I\le E_{0j}^c+\eta B_j^I.
\]
$C_j^I,E_{2j}^I$ 直接用全盒二阶源证书。所有量是相同带上的积分 sup 上界；
没有对真误差作同宽 Wiener 提升，也没有要求或假定第三阶参数导数。

对应有序有限量必须按这个混合选取重新准确加总：第一积分取中心的 $G_0,G_1$
和全盒的 $G_2$；局部 $2J(g_1,g_1)$ 取中心完整系数；局部混合 $g_0,g_2$
项付全盒报告的完整剩余范数，跨段三种所有频率继续显式保留。
不能只换误差数字却继续沿用全盒一阶有限多项式的旧 $C,D$。
`hybrid_parameter_source_bounds` 只执行上面的有向转移，完整身份、逐段有限量
选取及全550段时间闭合须由实际累积器提供。


平均横截的误差还可单独在实圆支付。保持中心有限 $L=P_1q(x+d)$ 完全相同，
以 $a=0$ 的同一 H 局部逆常数和 $\mathcal H(\sigma)$ 再执行 R82 的参数转移，
给真实 $|\langle C_p\rangle|$ 的第二个下界；取两个有效下界中较大者。
复带上的 $P,Q,T$ 仍使用原来的 $a>0$ 预算，不能把较小的实圆误差移作宽带误差。
新的完整入口 `fourfold_actual_parameter_endpoint_kam.py` 采用这个区分，
严格拒绝所有不足550段的输入，并分别保存实圆平均与复带范数账单。
