# R31：真实参数与非近恒等共轭的定量归一化

2026-11-12，visible-exact-astra-f6a2。

**状态：已证明的中间结论。** R30 的简化门从近恒等共轭出发，并先输出
一个平移反项。本结果允许实际初始共轭有较大的导数变化，直接改动给定
圆周映射族的真实参数。它提供一组有限、显式的充分不等式，保证所得参数
上的实际映射确实共轭到指定 Diophantine 旋转，不另加无法实现的平移项。

这里的映射族、复域、实际参数横截及误差均是待验证的输入。本文没有
构造本题的完整转折返回图，也没有将一个圆周共轭定理称为等距 PDE 的逆。

## 1. 空间、真实参数族和初始对象

圆周坐标为 $x\pmod{2\pi}$，使用 R30 的 Wiener 范数
$$
\|v\|_s=\sum_{k\in\mathbb Z}|v_k|e^{s|k|}.
$$
记 $\langle v\rangle=v_0$。该空间是 Banach 代数，并有
$$
\|v'\|_{s-\delta}\le\frac1{e\delta}\|v\|_s,
\qquad
\|v\circ(\operatorname{id}+h)\|_r
\le\|v\|_{r+\|h\|_r}.
\tag{1.1}
$$

固定 $\alpha=2\pi\rho$。假设已经证明，对于全部 $k\ne0$，
$$
|e^{ik\alpha}-1|\ge\frac1{K|k|},\qquad K>0.
\tag{1.2}
$$
于是零均值同调方程满足
$$
\|(T_\alpha-I)^{-1}v\|_{s-\delta}
\le\frac K{e\delta}\|v\|_s.
\tag{1.3}
$$
R30 给出了多个满足 (1.2) 的明确二次无理数；全部部分商不超过 $A$
时可以取 $K=(A+2)/4$。以下证明只使用 (1.2)，无需另引用定性 KAM 结论。

给定真实参数区间 $|a-a_0|<r_a$，设
$$
F_a(x)=x+\alpha+f(a,x)
$$
是实保向圆微分同胚的提升。假设 $a\mapsto f(a,\cdot)$ 是取值于
$\mathcal A_S$ 的 $C^2$ 族，并在整个区间内具有统一界
$$
\|\partial_a F_a\|_S\le P,\quad
\|\partial_x\partial_a F_a\|_S\le Q,\quad
\|\partial_a^2F_a\|_S\le T,\quad
\|\partial_x^2F_a\|_S\le B.
\tag{1.4}
$$
这些导数是周期函数，故其范数有定义。$P,Q,T,B$ 均为已给的非负数。
参数可以是几何均值的一条已定义曲线；不要求它直接在返回角上加常数。

给初始提升 $H_0(x)=x+h_0(x)$，$h_0\in\mathcal A_{s_0}$ 实值于实轴，
且 $H_0'>0$。须真正验证 $1/H_0'\in\mathcal A_{s_0}$，并给
$$
\|H_0'\|_{s_0}\le M_0,\qquad
\|1/H_0'\|_{s_0}\le R_0.
\tag{1.5}
$$
可以增大常数使 $M_0,R_0\ge1$。这不要求 $\|H_0'-1\|<1$；
例如一个实轴上强烈伸缩的初始共轭仍可使用，只需支付其实际复逆导数范数。

定义同一对象上的初始误差和真实横截
$$
E_0=F_{a_0}\circ H_0-H_0\circ R_\alpha,
\qquad \|E_0\|_{s_0}\le\varepsilon_0,
\tag{1.6}
$$
$$
\left|
\left\langle
\frac{(\partial_aF_{a_0})\circ H_0}{H_0'\circ R_\alpha}
\right\rangle\right|\ge\sigma_0>0.
\tag{1.7}
$$
这里只需要准确加权平均不为零，不要求参数导数处处同号。
纯径向作用量导数不能在没有实际对应的情况下替代 (1.7)。

## 2. 可以直接代数核验的门

选择 $0<\delta_0< s_0/4$，且 $\delta_0\le1$。置
$$
M=M_0+1,\qquad R=2R_0,\qquad
L_a=\frac{2R}{\sigma_0},
$$
$$
A_*=R(1+PL_a),\qquad L_H=MK A_*,
\tag{2.1}
$$
$$
C=K A_*+\frac B2 L_H^2+Q L_HL_a+\frac T2 L_a^2,
$$
$$
Z=R_0 Q L_H+R_0 T L_a+P R_0^2 L_H.
\tag{2.2}
$$
所有常数都来自已显示的数据。由 (1.7)，$P>0$，故 $C,Z,L_H,L_a>0$。

假设
$$
\boxed{\quad
\varepsilon_0\le\delta_0^2
\min\left\{\frac1{32C},\frac1{4R_0L_H},
                       \frac{\sigma_0}{8Z}\right\},
\quad}
\tag{2.3}
$$
以及两个真实域余量
$$
\boxed{\quad
2L_a\varepsilon_0<r_a,\qquad
s_0+\|h_0\|_{s_0}+\frac{2L_H\varepsilon_0}{\delta_0}<S.
\quad}
\tag{2.4}
$$

则存在 $|a_\infty-a_0|<r_a$ 和实解析保向圆微分同胚 $H_\infty$，
在 $s_\infty=s_0-4\delta_0>0$ 上满足
$$
\boxed{\quad F_{a_\infty}\circ H_\infty
                 =H_\infty\circ R_\alpha.\quad}
\tag{2.5}
$$
参数和共轭的总改变量满足
$$
\boxed{\begin{aligned}
|a_\infty-a_0|&\le2L_a\varepsilon_0,\\
\|H_\infty-H_0\|_{s_\infty}
 &\le 2L_H\varepsilon_0/\delta_0,\\
\|H_\infty'-H_0'\|_{s_\infty}
 &\le 2L_H\varepsilon_0/\delta_0^2.
\end{aligned}\quad}
\tag{2.6}
$$
实轴上还有 $H_\infty'\ge1/(2R_0)>0$。不另加平移反项。

## 3. 真实参数的一步自动约化

设当前对象为 $(a,H)$，$H=x+h$，误差
$E=F_a\circ H-H\circ R_\alpha$ 在宽度 $s$ 上满足 $\|E\|_s\le\varepsilon$。
归纳保持
$$
\|H'\|_s\le M,\qquad \|1/H'\|_s\le R,
\qquad
\left|\left\langle\frac{(\partial_aF_a)\circ H}{H'\circ R_\alpha}
\right\rangle\right|\ge\sigma_0/2.
\tag{3.1}
$$
记 $H'_R=H'\circ R_\alpha$、$b=1/H'_R$、$c=(\partial_aF_a)\circ H$。
令
$$
\Delta a=-\frac{\langle bE\rangle}{\langle bc\rangle},
\qquad
w\circ R_\alpha-w=b(E+c\Delta a),\qquad\langle w\rangle=0,
\qquad\Delta H=H'w.
\tag{3.2}
$$
同调源的均值由第一式准确消去，且
$$
|\Delta a|\le L_a\varepsilon,\qquad
\|b(E+c\Delta a)\|_s\le A_*\varepsilon.
$$
由 (1.3) 及 $1/e<1$，
$$
\|w\|_{s-\delta}\le KA_*\varepsilon/\delta,
\qquad
\|\Delta H\|_{s-\delta}\le L_H\varepsilon/\delta.
\tag{3.3}
$$
再应用一次 Cauchy 界，
$$
\|(\Delta H)'\|_{s-2\delta}\le L_H\varepsilon/\delta^2.
\tag{3.4}
$$

由误差的准确导数恒等式
$$
(\partial_xF_a)(H)H'-H'_R=E'
$$
得到新误差
$$
E_{\rm new}=E'w+\mathcal Q,
\tag{3.5}
$$
其中 $\mathcal Q$ 是 $F_{a+\Delta a}(H+\Delta H)$ 在 $(a,H)$ 的完整
二阶 Taylor 积分余项。这一项包含参数与空间的交叉导数，不能删去。
沿实参数线段、在允许的复合域内，(1.4) 给
$$
\|\mathcal Q\|_{s-2\delta}
\le \frac B2\|\Delta H\|^2
       +Q\|\Delta H\|\,|\Delta a|+\frac T2|\Delta a|^2.
$$
又 $\|E'\|_{s-\delta}\le\varepsilon/\delta$。
使用 $0<\delta\le1$，逐项得到
$$
\boxed{\quad
\|E_{\rm new}\|_{s-2\delta}
\le C\varepsilon^2/\delta^2.
\quad}
\tag{3.6}
$$
这里的二次消去依赖准确误差恒等式；它不是关于任意 PDE 主符号扰动的断言。

## 4. 完整收敛与参数横截的保持

取
$$
\delta_j=2^{-j}\delta_0,\qquad
s_j=s_0-2\sum_{i<j}\delta_i,\qquad
q_0=4C\varepsilon_0/\delta_0^2\le1/8.
$$
(3.6) 给 $q_{j+1}\le q_j^2$，所以
$$
\varepsilon_j\le\varepsilon_0\,4^{-j}q_0^{2^j-1}.
\tag{4.1}
$$
在每一步更小的实际域上，(3.3)--(3.4) 和参数界可求和，得到
$$
\sum_j|\Delta a_j|<2L_a\varepsilon_0,
\quad
\sum_j\|\Delta H_j\|<2L_H\varepsilon_0/\delta_0,
\quad
\sum_j\|(\Delta H_j)'\|<2L_H\varepsilon_0/\delta_0^2.
\tag{4.2}
$$
例如三条对应的几何级数分别不超过
$(1-q_0/4)^{-1}$、$(1-q_0/2)^{-1}$、$(1-q_0)^{-1}$，均严格小于 $2$。

现在核对这些估计的归纳输入。由 (2.3)，任意已完成步骤的导数改变量
满足
$$
\|H'-H_0'\|\le\frac1{2R_0}\le\frac12.
$$
于是 $\|H'\|\le M_0+1=M$；在同一缩小的 Wiener 空间内，
$$
\frac1{H'}=\frac1{H_0'}
\left(1+\frac{H'-H_0'}{H_0'}\right)^{-1}
$$
的 Neumann 级数给 $\|1/H'\|\le2R_0=R$。
实轴上 $H_0'\ge1/R_0$，故 $H'\ge1/(2R_0)>0$。

还必须保持真实横截，不能只证明初始分母不为零。由 (1.4)、(4.2)，
对 $c=(\partial_aF_a)\circ H$ 有
$$
\|c-c_0\|
\le Q\|H-H_0\|+T|a-a_0|
\le2QL_H\varepsilon_0/\delta_0+2TL_a\varepsilon_0.
$$
逆导数之差满足
$$
\|b-b_0\|
\le RR_0\|H'-H_0'\|
\le4R_0^2L_H\varepsilon_0/\delta_0^2.
$$
因此，用 $\delta_0\le1$，
$$
\begin{aligned}
|\langle bc\rangle-\langle b_0c_0\rangle|
&\le R\|c-c_0\|+P\|b-b_0\|\\
&\le\frac{4Z\varepsilon_0}{\delta_0^2}
\le\sigma_0/2.
\end{aligned}
\tag{4.3}
$$
这支付 (3.1) 的第三个输入，且保持分母符号。

(2.4) 和 (4.2) 保证所有参数线段都留在原参数区间，所有复合
$F_{a_j+t\Delta a_j}(H_j+t\Delta H_j)$ 都使用已给的宽度 $S$。
故 (1.4) 的四个界确实在每一步合法，归纳闭合。

由 (4.1)--(4.2)，参数、共轭及其导数在正宽度 $s_\infty$ 上收敛，
误差趋零。连续性给 (2.5)，累计界给 (2.6)。所得提升次数为一，实轴导数
正，故是保向圆微分同胚；局部解析反函数在紧圆周拼接给解析逆。证毕。

## 5. 与本课题实际均值及 PDE 的接口

若 $F_a$ 是同一候选族的真实特征返回提升，则 (1.7) 中的
$\partial_aF_a$ 应由真实二阶几何量、特征流及端点变化共同计算。
R29 已给固定切口的流变化公式；转折曲线随参数移动时还须加入其端点项。
如果 $a$ 是多个均值参数沿其它约束求出的曲线，(1.4)、(1.7) 必须沿
这条曲线读取，不能只改其中一个均值而忽略约束补偿项。

本结果把圆周参数归一化所需数据列为实际对象的有限范数与一个真实横截，
并付清迭代过程中横截的保持。因此可以在获得合格返回图后直接使用，
而无需把它先改造成近恒等共轭，或把输出反项误认作几何自由度。
所得共轭再由 R30 §4 转换为纯复合或半密度传输的全频逆；若完整 PDE
传输含额外幅度、低阶项或转折散射，它们仍须另行保留并估计。

本节不认为当前浮点样条已经满足 (1.4)--(1.7)、(2.3)--(2.4)。
当前样条也尚未构造精确等距闭面及固定帽；课题主目标仍未完成。

文献背景：参数圆周共轭的自动约化与 Figueras--Haro--Luque 的
*Effective bounds for the measure of rotations*, Nonlinearity 33 (2020),
Theorem 3.1 属同一方法。本文所有常数和收敛不等式已在上文独立证明，
没有借用未验证的外部小量门。
[作者机构原文](https://diposit.ub.edu/server/api/core/bitstreams/9ee43039-37e7-410e-9117-893bcf91b300/content)。
