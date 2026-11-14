# R51：实圆图的同宽 Wiener 复合与实际参数 KAM 域门

2026-11-12，independent-audit。

**状态：已证明的中间结论。** 对实轴上取实值的真实解析圆图，
复合所需的虚部范围由其导数和 strip 宽度控制，与其沿实轴的
大位移没有直接关系。本文用两条边界上的完整 $H^1$ Fourier
估计支付同宽 Wiener 复合 norm，再给 R31 一个可替换的域门。
初始共轭无需接近恒等；迭代中的所有共轭、二阶 Taylor 线和
参数线都由同一已付导数预算控制。

本文没有证明当前实际返回的误差、参数横截或复角域；它提供的
是真实计算可以使用的较小域条件及相应 norm 费用，不是将一个
点值 strip 包含关系直接冒充 Wiener 算子界。

## 1. 实圆图的虚部控制

角变量周期为 $2\pi$，$\mathcal A_s$ 使用 Wiener 范数
$$
\|v\|_s=\sum_{k\in\mathbb Z}|v_k|e^{s|k|}.
\tag{1.1}
$$
设 $H(z)=z+h(z)$ 是 degree-one 提升，$h\in\mathcal A_s$，
$H'$ 连续于闭 strip，且
$$
H(x)\in\mathbb R\quad(x\in\mathbb R),\qquad
\|H'\|_s\le M.
\tag{1.2}
$$
这里可用更直接的 $\sup_{|\operatorname{Im}z|\le s}|H'(z)|\le M$
代替。沿真实竖直线积分，准确有
$$
\boxed{\quad |\operatorname{Im}H(x+iy)|\le M|y|,\qquad |y|\le s.\quad}
\tag{1.3}
$$
因为 $H(x)$ 为实数，
$H(x+iy)-H(x)=\int_0^y iH'(x+it)dt$。这个证明不使用
$\|H-\operatorname{id}\|$ 小性，也允许任意实常数平移。
本节的实轴条件必须真的成立；不能向任意带有额外虚平移的图
转授 (1.3)。

## 2. 两条边界给完整同宽 Wiener 复合界

设 $v\in\mathcal A_S$ 为周期函数，且
$$
\delta=S-Ms>0.
\tag{2.1}
$$
定义明确常数
$$
\boxed{\quad \mathcal C(M,\delta)=
3\left(1+\frac{M}{e\delta}\right).\quad}
\tag{2.2}
$$

**定理 2.1。** 在上述真实输入下，
$$
\boxed{\quad
\|v\circ H\|_s\le\mathcal C(M,\delta)\|v\|_S.
\quad}
\tag{2.3}
$$
这是同一个 $\mathcal A_s$ 的全 Fourier 和估计，未损失额外
输出 strip 宽度。

**证明。** 记 $g=v\circ H$。由 (1.3)，在两条边界
$z=x\pm is$ 上，$H(z)$ 都落在闭 strip
$|\operatorname{Im}w|\le Ms$ 内。因此
$$
|g(x\pm is)|\le\|v\|_S,\qquad
|g_x(x\pm is)|\le M\|v'\|_{Ms}
                        \le\frac{M}{e\delta}\|v\|_S.
\tag{2.4}
$$
最后一步是逐频率的
$|k|e^{-\delta|k|}\le(e\delta)^{-1}$，不是额外假定一个更高
导数输入。

由于 $H(z+2\pi)=H(z)+2\pi$，$g$ 为 $2\pi$ 周期。Parseval 在
两条真实边界给
$$
\begin{aligned}
\sum_k\langle k\rangle^2|g_k|^2e^{2s|k|}
&\le\|g(\cdot+is)\|_{H^1}^2+\|g(\cdot-is)\|_{H^1}^2\\
&\le2\left[1+\left(\frac{M}{e\delta}\right)^2\right]\|v\|_S^2.
\end{aligned}
\tag{2.5}
$$
又有简单的可验证界
$$
\sum_{k\in\mathbb Z}\langle k\rangle^{-2}
\le1+2\left(\frac12+\int_1^\infty\frac{dx}{1+x^2}\right)
=2+\frac\pi2<4.
\tag{2.6}
$$
所以 Cauchy--Schwarz 给
$$
\|g\|_s
<2\sqrt2\left[1+\left(\frac{M}{e\delta}\right)^2\right]^{1/2}
 \|v\|_S
\le\mathcal C(M,\delta)\|v\|_S.
\tag{2.7}
$$
若不预先在闭边界工作，先取 $s'<s$，用相同上界，再令 $s'\uparrow s$；
Fourier 和的单调极限给同一结论。$H'$ 的实际一致界保证所有
边界 $H^1$ 项合法。$\square$

一个可选的更紧版本是将 $v$ 的均值单独保留：
$$
\|v\circ H\|_s
\le |v_0|+\mathcal C(M,\delta)\|v-v_0\|_S.
\tag{2.8}
$$
故实际参数导数若大部分为常数，不必把常数部分也乘整个复合费。

## 3. 对全部实线段的一致差量和 Taylor 界

若 $H_0,H_1$ 均实于实轴且
$\|H_i'\|_s\le M$，则
$H_t=(1-t)H_0+tH_1$，$0\le t\le1$，也满足相同假设。
对所有这些线段，(2.3) 的常数可共同取
$\mathcal C(M,S-Ms)$。所以真实积分恒等式给
$$
\|v\circ H_1-v\circ H_0\|_s
\le\mathcal C(M,S-Ms)\|v'\|_S\|H_1-H_0\|_s,
\tag{3.1}
$$
只要右边实际导数属于 $\mathcal A_S$。

更一般地，给实参数区间内的实际 $C^2$ 族 $F_a$，全部空间
导数按其解析延拓理解。若在该区间的 $\mathcal A_S$ 上有
$$
\|\partial_aF_a\|_S\le\bar P,\quad
\|\partial_x\partial_aF_a\|_S\le\bar Q,\quad
\|\partial_a^2F_a\|_S\le\bar T,\quad
\|\partial_x^2F_a\|_S\le\bar B,
\tag{3.2}
$$
那么在所有合法实参数线段和所有上述 $H_t$ 上，四个**复合后**
的实际 Wiener 范数由
$$
P=\mathcal C\,\bar P,\qquad Q=\mathcal C\,\bar Q,\qquad
T=\mathcal C\,\bar T,\qquad B=\mathcal C\,\bar B
\tag{3.3}
$$
统一控制。若已给均值/非均值的独立界，可用 (2.8) 逐项收紧。

例如 $F_{a+\Delta a}(H+\Delta H)$ 的完整二阶 Taylor 积分余项
在 $\mathcal A_s$ 中不超过
$$
\frac B2\|\Delta H\|_s^2
 +Q\|\Delta H\|_s|\Delta a|+\frac T2|\Delta a|^2.
\tag{3.4}
$$
因为参数与空间线段上的二阶导数先由 (3.3) 得到真实复合界，
再使用 Wiener Banach 代数。没有要求复参数解析；这里只沿原
实际实参数区间使用 $C^2$ Taylor 公式。

## 4. R31 的替代域门：全部明确常数

以下重述应用所需输入，避免把本篇仅理解为一次形式替换。
角仍取 $2\pi$，$\alpha=2\pi\rho$ 为指定实际目标，且
$$
|e^{ik\alpha}-1|\ge(K|k|)^{-1}\qquad(k\ne0).
\tag{4.1}
$$
实际族 $F_a(x)=x+\alpha+f(a,x)$ 在
$|a-a_0|<r_a$ 中为实保向提升，并满足 (3.2)。
给真实初始共轭 $H_0=x+h_0$，实于实轴，满足
$$
\|H_0'\|_{s_0}\le M_0,\qquad
\|1/H_0'\|_{s_0}\le R_0,\qquad H_0'>0,\qquad M_0,R_0\ge1.
\tag{4.2}
$$
同一实际对象还须供应
$$
\|F_{a_0}\circ H_0-H_0\circ R_\alpha\|_{s_0}\le\varepsilon_0,
\tag{4.3}
$$
$$
\left|\left\langle
\frac{(\partial_aF_{a_0})\circ H_0}{H_0'\circ R_\alpha}
\right\rangle\right|\ge\sigma_0>0.
\tag{4.4}
$$
初始误差和横截不能由本篇的复合界自动产生。

先按 R31 取
$$
M=M_0+1,\qquad R=2R_0,
\qquad \boxed{\quad S>Ms_0.\quad}
\tag{4.5}
$$
用固定正余量
$$
\delta_*=S-Ms_0,\qquad
\mathcal C_*=\mathcal C(M,\delta_*)
\tag{4.6}
$$
在 (3.3) 中计算 $P,Q,T,B$。下面常数与 R31 的定义相同，但
这里的四个输入已包含真实复合费：
$$
\begin{aligned}
L_a&=2R/\sigma_0,&
A_*&=R(1+PL_a),&
L_H&=MK A_*,\\
C_*&=K A_*+\tfrac B2L_H^2+Q L_HL_a+\tfrac T2L_a^2,&
Z_*&=R_0QL_H+R_0TL_a+PR_0^2L_H.
\end{aligned}
\tag{4.7}
$$
选择 $0<\delta_0<s_0/4$、$\delta_0\le1$。假设
$$
\boxed{\quad
\varepsilon_0\le\delta_0^2
\min\left\{\frac1{32C_*},\frac1{4R_0L_H},
                         \frac{\sigma_0}{8Z_*}\right\},
\qquad 2L_a\varepsilon_0<r_a.
\quad}
\tag{4.8}
$$

**定理 4.1。** 在这些实际输入下，存在
$|a_\infty-a_0|<r_a$ 及实解析保向圆提升 $H_\infty$，在
$s_\infty=s_0-4\delta_0>0$ 上满足
$$
F_{a_\infty}\circ H_\infty=H_\infty\circ R_\alpha.
\tag{4.9}
$$
准确累计上界为
$$
\begin{aligned}
|a_\infty-a_0|&\le2L_a\varepsilon_0,\\
\|H_\infty-H_0\|_{s_\infty}&\le2L_H\varepsilon_0/\delta_0,\\
\|H_\infty'-H_0'\|_{s_\infty}&\le2L_H\varepsilon_0/\delta_0^2,
\qquad H_\infty'\ge1/(2R_0)\quad\hbox{于实轴}.
\end{aligned}
\tag{4.10}
$$
这里不要求 R31 原来的
$s_0+\|h_0\|_{s_0}+2L_H\varepsilon_0/\delta_0<S$。
它被真实 (4.5) 及已明确支付的 (3.3) 取代。

## 5. 中间共轭、Taylor 线与真实参数范围的证明

为使 (4.5) 对**全部迭代对象**成立，必须同时控制导数，而不
只是检查初始 $M_0$。下面按 R31 的真实自动约化证明此事。

令当前误差为 $E=F_a\circ H-H\circ R_\alpha$，设
$b=(H'\circ R_\alpha)^{-1}$、$c=(\partial_aF_a)\circ H$。
同一步的实际修正为
$$
\Delta a=-\frac{\langle bE\rangle}{\langle bc\rangle},
\quad
w\circ R_\alpha-w=b(E+c\Delta a),\quad \langle w\rangle=0,
\quad \Delta H=H'w.
\tag{5.1}
$$
在当前 $\|H'\|\le M,\|1/H'\|\le R$、
$|\langle bc\rangle|\ge\sigma_0/2$ 下，本篇 (3.3) 给
$\|c\|\le P$，故
$$
|\Delta a|\le L_a\varepsilon,\quad
\|\Delta H\|_{s-\delta}\le L_H\varepsilon/\delta,\quad
\|(\Delta H)'\|_{s-2\delta}\le L_H\varepsilon/\delta^2.
\tag{5.2}
$$
同调源的均值由 $\Delta a$ 准确消掉；$w,\Delta H,\Delta a$ 都
为真实实对象。准确误差导数恒等式给新误差
$E_{\rm new}=E'w+\mathcal Q$。用 (3.4) 与 Cauchy 界，得到
$$
\varepsilon_{\rm new}\le C_*\varepsilon^2/\delta^2.
\tag{5.3}
$$

取 $\delta_j=2^{-j}\delta_0$、
$s_j=s_0-2\sum_{i<j}\delta_i$、
$q_0=4C_*\varepsilon_0/\delta_0^2\le1/8$。与 R31 相同的递推给
$$
\varepsilon_j\le\varepsilon_0\,4^{-j}q_0^{\,2^j-1}.
\tag{5.4}
$$
因此在每个相应已缩域内，真实绝对增量的总和满足
$$
\sum_j|\Delta a_j|<2L_a\varepsilon_0,\quad
\sum_j\|\Delta H_j\|<2L_H\varepsilon_0/\delta_0,\quad
\sum_j\|(\Delta H_j)'\|<2L_H\varepsilon_0/\delta_0^2
                         \le\frac1{2R_0}.
\tag{5.5}
$$
**同一预算包括每个当前步骤的部分线段。** 在计算完
$(\Delta a_j,\Delta H_j)$、尚未使用二阶 Taylor 公式之前，(5.2)
和已知的前 $j$ 步 majorant 已经给
$$
\left\|\left(H_j+t\Delta H_j-H_0\right)'\right\|_{s_{j+1}}
\le\sum_{i\le j}\|(\Delta H_i)'\|
\le\frac1{2R_0},\qquad 0\le t\le1.
\tag{5.6}
$$
这里可用 (5.4) 定义的数值 majorant 之剩余正项作上界，并不
先假设后续解已存在。因此
$$
\|(H_j+t\Delta H_j)'\|_{s_{j+1}}
\le M_0+\frac1{2R_0}\le M,
\tag{5.7}
$$
且所有这些图实于实轴。对整个 Taylor 线，(1.3) 给
$|\operatorname{Im}(H_j+t\Delta H_j)|\le Ms_{j+1}\le Ms_0<S$。
(2.3) 的实际同宽常数至多固定的 $\mathcal C_*$。
这就在使用 (5.3) 之前核对了它所需的复合域，闭合归纳而没有
循环授予中间导数界。

当前步 $H_j$ 在 $s_j$ 上也满足相同导数预算；从初始到当前
对象的比较线 $(1-t)H_0+tH_j$ 在 $s_j$ 上同样合法。
逆导数的 Neumann 级数给 $\|1/H_j'\|\le2R_0$，实轴下界为
$1/(2R_0)$。真实参数的所有线段都位于
$|a-a_0|<r_a$，因为 (4.8)、(5.5) 给每个部分绝对位移都
小于 $2L_a\varepsilon_0$。

在这些**实际**参数/空间线段上，(3.3) 控制横截的变化：
$$
\|c-c_0\|
\le2QL_H\varepsilon_0/\delta_0+2TL_a\varepsilon_0,
$$
$$
\|b-b_0\|\le4R_0^2L_H\varepsilon_0/\delta_0^2,
$$
$$
|\langle bc\rangle-\langle b_0c_0\rangle|
\le4Z_*\varepsilon_0/\delta_0^2\le\sigma_0/2.
\tag{5.8}
$$
所以参数横截也一直存在。最终由 (5.4)–(5.5) 的收敛和真实
复合连续性得到 (4.9)–(4.10)，其余结论按 R31 的同一证明。
$\square$

这里 $M=M_0+1$ 只是方便与 R31 原符号一致。由 (5.7)，还可
直接选更紧的
$$
M=M_0+\frac1{2R_0}
\tag{5.9}
$$
来重新计算 (4.5)–(4.8) 的全部常数；相同导数小量门已经足够。
不能只缩小域门里的 $M$ 而仍沿用另一次计算中不匹配的常数。

## 6. 当前 dyadic 初值的角尺度与实际用途

R48 的明确有理多项式使用归一角 $x=4\theta$，周期 $2\pi$。
其 $s_0=1/32$、$M_0=4.587414$、$R_0=7.254348$ 可以直接填入
本篇，但实际映射族的 $S,\bar P,\bar Q,\bar T,\bar B$、
$\varepsilon_0,\sigma_0,r_a$ 仍须针对同一个返回图支付。

仅作域门的准确比较，取保守 $M=M_0+1$：
$$
Ms_0=\frac{5.587414}{32}=0.1746066875.
\tag{6.1}
$$
因此合法候选的原始 strip 只需满足 $S>0.1746066875$，并支付
相应的 $\mathcal C_*$；并非必须为了实位移 $\|h_0\|\approx0.7066$
把原图延拓到约 $0.738$ 的 strip。若选更小初始带
$s_0=1/512$、$M_0=2.496492$，则
$$
(M_0+1)s_0=0.0068290859375.
\tag{6.2}
$$
这些数字只比较充分域门，不证明当前实际返回已在该域解析，也
不说明较窄带的最终 KAM 小量门已满足。特别 $\mathcal C_*$ 在
$S-Ms_0$ 很小时会增大，应一并进入 (4.7)–(4.8)。

回到原材料角，真正的提升是
$$
H_\theta(\theta)=\frac14H_0(4\theta).
\tag{6.3}
$$
相应 physical strip 宽为 $s_\theta=s_x/4$，位移 Wiener norm
为归一角的四分之一，而导数与逆导数的 norm 在对应带上保持
同一数值。$x$ 中目标转角 $2\pi\rho$ 对应
$\theta$ 中转角 $(\pi/2)\rho$。这一尺度必须同时用于真实返回、
R31/R51 的共轭及 R46/R50 的 $1/j$ 完整相位，不能只改其中一个
角频分母。

本篇的结论只替换解析复合与域预算。全 PDE 的低阶相位、正负
组件、完整源、持握约束和最终可见振幅仍继续使用各自的实际
证明输入，不能由圆周归一化的存在性单独推出。
