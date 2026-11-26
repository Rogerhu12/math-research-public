# R271 附录：实际 Riordan 强头的完整 Fock 源运输及原同源差值费用

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本稿把原 Riordan 形式逆作用于完整有限 Fock 列，保留准确新头 $\psi_m(A_m+D_<)/d_0$ 的全部强位混合项。三角代换和其逆均有独立于增长头长的原 Hilbert 范数界；在同一个实际完整源上，其差由原正高度能量支付。随后仍用原未加权 Gram 重新最小化。拉回原头后的物理列保留一个明确的小差值，以准确恢复原同一个 $u$。本稿不把此差值在未付的 MP 度量中自动视为小，也不宣布稳定范围端点或绝对孔权已付。

依据：

- [原 Riordan 完整／裸来源运输](R271-appendix-relative-hole-riordan-conjugacy-full-bare-source-transport-and-uniform-budget.md)，§§5--6。
- [指数强前缀实际方差完整源极限](R271-appendix-exponential-strong-prefix-actual-variance-source-limit.md)。
- [原物理相干翻译与同源身份](R271-appendix-vacuum-source-moments-all-strong-physical-transport-and-weighted-inverse.md)，§§3--4。

内积对第一变量线性。本文所有投影、Gram 和 inverse 均使用原未加权物理内积。

## 1. 同一个原强头、实际方差和解析函数

按原 Riordan 稿取
$$
d=2^m,\quad m\ge10,\quad
\tau=\frac{\Lambda_{m-1}+14d^3+\log16}{d/2-1},\quad
R=2\left\lceil2e^\tau\right\rceil,\quad x=m+R,\quad h=d+R .
\tag{1.1}
$$
这里原链权满足
$$
\Lambda_i=100\,16^i-105\,8^i+(150i+25)2^i,\qquad d_0=e^{-20}.
$$
偶数取整不改变原稿所用 $R\ge4e^\tau$、$h\le2R$ 或其全部绝对系数预算。令
$$
C=A_m+D_{[m,x)},\qquad C^h=0,\qquad
S_x=\sum_{i\ge x}(i+1)^{-4},\qquad
\delta_x=\sum_{i\ge x}(i+1)^{-2}.
\tag{1.2}
$$
整个强物理块仍在 $C$ 中，不作线性化替换。

本稿取
$$
S_x\le s\le2S_x,\qquad
\widehat C=\frac{\psi_m(C)}{d_0},\qquad
g(z)=\frac{\psi_m(z)}{d_0z}.
\tag{1.3}
$$
函数在零点按 $g(0)=1$ 延拓；代入有限幂零头时只需有限个系数。与依赖稿完全一致地记
$$
\phi(z)=-\psi_m(-z)/d_0,\qquad
\chi(z)=\phi^{-1}(z)=-F_m(-d_0z),\qquad
U_\theta(r)=\sum_{p\ge1}\left|[z^p]\frac{\theta(z)}z\right|r^p .
$$
原绝对系数预算给
$$
hU_\chi(2\delta_x)\le M_0,\qquad
hU_\phi(\delta_x)\le2M_0,\qquad
M_0=16(1+e^{1070}),\qquad \mathcal C_0=e^{2M_0}.
\tag{1.4}
$$

置 $H=h-1$、$r_s=\sqrt{Hs}$。原 $R$ 远大于 $8d$，所以
$H\le(9/8)x$、$x\ge8$。由积分比较，
$$
S_x\le\frac1{3x^3},\qquad \delta_x\ge\frac1{x+1},
$$
从而
$$
r_s^2\le\frac3{4x^2}\le\frac1{(x+1)^2}\le\delta_x^2.
\tag{1.5}
$$
中间不等式在 $x\ge8$ 时由 $3(x+1)^2\le4x^2$ 得到。故下文真正 Fock 尺度 $r_s$ 落在 (1.4) 已付的解析半径中。

## 2. 完整列上的解析函数预算

先取任意闭的 $C$ 不变子空间 $F$。因为 $C$ 有限维且
$\widehat C=Cg(C)$、$g(0)=1$，同一 $F$ 也对 $\widehat C$ 不变，且反向由 $\chi$ 成立。

定义完整列与原压缩 Gram
$$
\mathcal R_C a=\left(\frac{(-C)^ja}{\sqrt{j!s^j}}\right)_{j=0}^{H},\qquad
H_{C,F}=\mathcal R_C^*\mathcal R_C\big|_F\ge I_F.
\tag{2.1}
$$
星号在这里按从 $F$ 出发的列算子取。令 $f$ 为同一头 forcing，
$$
a=H_{C,F}^{-1}P_Ff,\qquad k=\mathcal R_Ca,\qquad
E_j=\frac{\|C^ja\|^2}{j!s^j},\qquad
\varepsilon=\sum_{j=1}^HE_j,\qquad \mu=\sum_{j=1}^HjE_j .
$$
对每个 $p\ge1$，逐层换指标准确给
$$
\|C^pk\|^2=s^p\sum_{\ell=p}^{H}\frac{\ell!}{(\ell-p)!}E_\ell .
\tag{2.2}
$$
于是
$$
\|C^pk\|\le r_s^p\sqrt{\varepsilon},\qquad
\|C^pk\|\le\sqrt s\,r_s^{p-1}\sqrt\mu .
\tag{2.3}
$$
对任意 $b(z)=b(0)+\sum_{p\ge1}b_pz^p$，只要其绝对系数和
$U_b(r_s)=\sum_{p\ge1}|b_p|r_s^p$ 有限，就有
$$
\boxed{
\|(b(C)-b(0))k\|
\le U_b(r_s)\min\left\{\sqrt\varepsilon,\frac{\sqrt\mu}{\sqrt H}\right\}.
}
\tag{2.4}
$$
这里 $C$ 作用在全部列的原头因子上。此式保留整个完整列，不是仅估零行。

特别，$g(z)=\phi(-z)/(-z)$，故 $U_g=U_\phi$。由 (1.4)--(1.5)，
$$
\boxed{
\|(g(C)-I)k\|
\le\frac{2M_0}{h}\sqrt\varepsilon,\qquad
\|(g(C)-I)k\|
\le\frac{2M_0}{h\sqrt x}\sqrt\mu .
}
\tag{2.5}
$$
第二式使用 $U_g(r_s)\le(r_s/\delta_x)U_g(\delta_x)$，及
$\sqrt s/\delta_x\le\sqrt{2/(3x^3)}(x+1)\le x^{-1/2}$。没有引入额外的 Cauchy 圆周常数。

## 3. 全辅助塔的精确三角代换

在同一个头 Hilbert 空间张量辅助空间
$\operatorname{span}\{e_0,\ldots,e_H\}$ 上，定义
$$
(B_\phi z)_j=
\sum_{p=0}^{H-j}
\sqrt{\frac{(j+p)!}{j!}}\,s^{p/2}
[\zeta^p]\left(\frac{\phi(\zeta)}\zeta\right)^j z_{j+p},
\qquad 0\le j\le H .
\tag{3.1}
$$
这里 $z=(z_0,\ldots,z_H)$ 是向量，$\zeta$ 只是形式变量。
$B_\phi$ 只作用辅助因子，所有原物理头坐标保持不动。

直接把 $z=\mathcal R_Ca$ 代入 (3.1)，得到
$$
(B_\phi\mathcal R_Ca)_j
=\frac{\phi(-C)^ja}{\sqrt{j!s^j}}
=\frac{(-\widehat C)^ja}{\sqrt{j!s^j}}.
$$
因此
$$
\boxed{B_\phi\mathcal R_C=\mathcal R_{\widehat C}.}
\tag{3.2}
$$
由于原形式复合 $\phi\circ\chi=\chi\circ\phi=z$，
有限三角矩阵的系数复合准确给
$$
B_\phi^{-1}=B_\chi .
\tag{3.3}
$$
只截辅助 $0,\ldots,H$ 不产生末端项：每个输出系数只读取同一或更高输入层，且所有需要的形式恒等式均按次数 $\le H$ 成立。

令 $i_0$ 插入辅助零层，$P_0=i_0^*$。由 $j=0$ 行只有恒等项，
而非零层不读取零层，
$$
P_0B_\phi=P_0,\qquad B_\phi i_0=i_0,\qquad B_\phi^*i_0=i_0.
\tag{3.4}
$$
同样的恒等式适用于 $B_\chi$。

## 4. 原范数和真正来源的正高度费用

设 $\mathsf N$ 是辅助数算子。对任一 $\theta=\phi,\chi$，写
$u(\zeta)=\sum_{p\ge1}|[\zeta^p](\theta(\zeta)/\zeta)|\zeta^p$。
若 $\beta_p=[\zeta^p]((1+u(\zeta))^h-1)$，则对 $1\le j\le H$、$p\ge1$，
$$
\left|[\zeta^p]\left(\frac{\theta(\zeta)}\zeta\right)^j\right|
\le\frac jh\,\beta_p.
\tag{4.1}
$$
这是因为每个 $k\ge1$ 都有
$\binom jk\le(j/h)\binom hk$，再逐个正系数比较。

截断辅助 annihilation 的范数至多 $\sqrt H$。将 (3.1) 按 $p$ 求和，
(4.1) 和 (1.4)--(1.5) 给
$$
\boxed{
\|B_\phi\|,\ \|B_\phi^{-1}\|,\ \|B_\phi^*\|,\
\|(B_\phi^{-1})^*\|\le\mathcal C_0 .
}
\tag{4.2}
$$
更精确地，$\|B_\theta-I\|\le e^{hU_\theta(r_s)}-1\le\mathcal C_0-1$。

所有这些差都同时消掉辅助零层。故对旧完整源 $k$，
$$
\|(B_\theta-I)k\|,\ \|(B_\theta^*-I)k\|
\le(\mathcal C_0-1)\sqrt\varepsilon .
$$
此外，(4.1) 分别给
$j/\sqrt{j+p}\le\sqrt h$、$j/\sqrt j\le\sqrt h$，所以
$$
\boxed{
\|(B_\theta-I)k\|,\ \|(B_\theta^*-I)k\|
\le(\mathcal C_0-1)\,D(k),\qquad
D(k):=\min\left\{\sqrt\varepsilon,\sqrt{\mu/h}\right\}.
}
\tag{4.3}
$$
第二种界在辅助零层上按零延拓 $\mathsf N^{-1/2}$，没有除零。
式 (4.2)--(4.3) 是整个实际来源列的费用；不把 $B_\phi$ 换成逐高度任意可选的映射。

## 5. 保留原未加权最小者的完整重新最小化

令
$$
E=\operatorname{Ran}\mathcal R_C|_F,\qquad
\widehat E=\operatorname{Ran}\mathcal R_{\widehat C}|_F=B_\phi E,
\qquad P=P_E,\qquad B=B_\phi .
$$
这些空间都闭，因为列算子保留零行并有范数下界 $1$。
设
$$
k=P_Ei_0f,\qquad \widehat k=P_{\widehat E}i_0f,\qquad
K=P B^*B|_E .
$$
则 $K$ 是原 $E$ 度量中的正算子，且
$$
\mathcal C_0^{-2}I_E\le K\le\mathcal C_0^2I_E,\qquad
\boxed{\widehat k=BK^{-1}k.}
\tag{5.1}
$$
这是完整原 Gram 投影公式；(3.4) 给右端 forcing 仍是同一个 $k$。

由
$$
(K-I)k=P\big((B^*-I)k+B^*(B-I)k\big)
$$
和 (4.3)，
$$
\|(K-I)k\|\le(1+\mathcal C_0)(\mathcal C_0-1)D(k).
$$
又
$\|BK^{-1}z\|^2=\langle K^{-1}z,z\rangle\le\mathcal C_0^2\|z\|^2$，
所以
$$
\boxed{
\|\widehat k-k\|\le3\mathcal C_0^3 D(k),\qquad
\|B^{-1}\widehat k-k\|\le2\mathcal C_0^4 D(k).
}
\tag{5.2}
$$
第二式就是 $B^{-1}\widehat k=K^{-1}k$ 的原列范数比较。
记 $\widehat a=P_0\widehat k$，则 (3.4) 同时保证
$$
B^{-1}\widehat k=\mathcal R_C\widehat a .
\tag{5.3}
$$
因此拉回后零行没有另行修改，而原 $C$ 完整列的放大已包含在 (5.2)，不能只用 $\|\widehat a-a\|$ 代替。

以上对任何同一个 $C$ 不变真子空间 $F$ 成立。
但其右端 $\varepsilon$ 始终是该 $F$ 的原完整源能量；
没有将全空间的能量极限移入未知 $F_0$。

## 6. 实际完整头的强极限与原母窗口

本节只取完整 $F=\mathcal H_{<x}$，以及同一个原有限物理 forcing $f$，
特别允许 $f=f_1=e_1$。沿 (1.1) 令 $m\to\infty$。
原 $\tau\le13d^3$ 给
$x+1\le e^{26d^3}/4$，整个高度 $H=h-1$ 合法。
对 (1.3) 中任意同一序列 $s=s_m$，已有实际方差完整源定理给
$$
a_m\longrightarrow P_{\ker T}f,\qquad
\varepsilon_m\longrightarrow0,\qquad
k_m\longrightarrow P_{\ker T}f\otimes e_0 .
\tag{6.1}
$$
这些向量均按原物理真空嵌入共同空间。(5.2) 遂给
$$
\boxed{
\widehat k_m\longrightarrow P_{\ker T}f\otimes e_0,\qquad
B_m^{-1}\widehat k_m\longrightarrow P_{\ker T}f\otimes e_0 .
}
\tag{6.2}
$$
特别，$s_m=S_{x_m}$ 本身合法，无须先挑一个未知连续方差子列。
新头仍准确为 $\psi_m(A_m+D_{[m,x_m)})/d_0$；
(6.2) 没有把它改称 $B_m/d_0+D_{[m,x_m)}$。

若保原 Riordan 母窗，取
$$
Q_*=\left\lfloor e^{(1601/64)d^3}\right\rfloor.
$$
依赖稿已给 $2h+R<Q_*/2$。故本稿完整物理列所需
$Q\ge R+H$ 可选于同一原 $4d\le Q\le Q_*$，而全部旧真帽
$n+2h+R<Q_*$ 的窗口仍按原要求保留。此处没有调用一次不同基头的免费改组。

## 7. 拉回原物理列、准确同源修正及剩余边界

定义原物理相干翻译
$$
\mathscr P_{x,s}(z)
=\sum_{j=0}^{H}z_j\otimes
\frac{(D_x^*)^j\Omega}{\sqrt{j!s^j}},
\qquad D_x=\sum_{i\ge x}(i+1)^{-2}E_i .
\tag{7.1}
$$
不同真实远孔层正交，且
$$
\frac{\|(D_x^*)^j\Omega\|^2}{j!s^j}
=\frac{j!\,e_j((i+1)^{-4}:i\ge x)}{s^j}
\le(S_x/s)^j\le1.
$$
所以 $\mathscr P_{x,s}$ 是原物理范数中的收缩。

令
$$
F^{\rm old}=\mathscr P_{x,s}k,\qquad
\widetilde F=\mathscr P_{x,s}B^{-1}\widehat k,\qquad
\Delta F=F^{\rm old}-\widetilde F .
$$
则
$$
\boxed{\|\Delta F\|\le2\mathcal C_0^4D(k).}
\tag{7.2}
$$
这些列的原 $m$ 后总孔支撑均不超过 $R+H$。
对于上一节的同一完整 forcing 和任意原合法 $Q\ge R+H$，
原逐列低方程给
$$
u_{m,Q,f}=(P_{V_{m,Q}}-P_{K_{m,Q}})F^{\rm old}.
$$
因而准确有
$$
\boxed{
u_{m,Q,f}
=(P_{V_{m,Q}}-P_{K_{m,Q}})\widetilde F
 +(P_{V_{m,Q}}-P_{K_{m,Q}})\Delta F .
}
\tag{7.3}
$$
$K_{m,Q}\subset V_{m,Q}$，故第二项范数不超过 (7.2)。
式 (7.3) 保留同一个 $f,w/u$ 接口；原内部顶部和两端 partial 都继续作用于这同一个完整和。没有把 $\widetilde F$ 单独宣称为原同源最小者。

$B_\phi$ 与有限头内的物理孔权交换，但 (7.1) 会把辅助第 $j$ 层变成真实远孔第 $j$ 层。因此原远孔指数权对应 $32^{\mathsf N}$，它与 $B_\phi$ 不交换；其两向共轭须另付相应扩大解析半径。本文不由 (4.2) 推出该指数权界。

同样，(7.2) 是原 Hilbert 范数费用。若某个完整 MP、核外第二 Green、左／裸返回或真实帽读数放大这个差值，其费用仍须保留并实际支付。正辅助方差的完整核和 (6.2) 的普通强极限也没有给出 $P_{\ker T}f\in\overline{B\ker T}$。
