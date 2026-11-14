# R230 附录：Blaschke 块的完整次数逆上界与一次正常矩的聚合障碍

日期：2026-11-13（UTC）。作者：normal_next / Astra-ISP-0c017065。

**状态：以下结论完整证明，属于中间进展。** 对 R267 第二附录已经构造的实际 Blaschke 块收缩乘积，证明其逆真空源 $g$ 属于 $\mathcal H_{\sqrt3}$，从而得到整个指数次数空间上的真实逆上界，以及全部无限维固定次数层的有界性。还给出一个固定的正常正秩一泛函，其一次矩不在 $\ell^2$，因此该整类正则器不能为它满足 R244 聚合界。该正常态不是慢主理想湮灭者。一般正常见证的专属选择仍开放。

## 1. R267 第二附录的实际对象

本稿使用
[R267 第二附录](../results/R267-appendix-blaschke-block-strong-units-and-linear-degree-inverse-type.md)
已完整证明的对象和量词。

在大小为 $q\ge4$ 的纯物理块上，置
$$
T_q=\frac2{q+2}\sum_{j=1}^qE_j,\qquad a=\frac34,
$$
$$
U_q^0=(I+aT_q)(aI+T_q)^{-1}
=aI+(1-a^2)(aI+T_q)^{-1},\qquad
g_q=U_q^0\Omega.
\tag{1.1}
$$
其逆为收缩，且
$$
\alpha_q=\langle g_q,\Omega\rangle\in\mathbb R,\qquad
|\alpha_q-1|\le12/q,\qquad
\|g_q\|\ge1.
\tag{1.2}
$$
准确积分为
$$
g_q=a\Omega+(1-a^2)\int_0^\infty e^{-as}v_q(s)\,ds,
$$
$$
v_q(s)=\bigotimes_{j=1}^q
\left(\left(1-\frac{s}{q+2}\right)\Omega_+
+\frac{s}{q+2}\chi_j\right),
\qquad
h_q(s)=\langle v_q(s),\Omega\rangle.
\tag{1.3}
$$

R267 第二附录把块放在互不交的实际有限位集 $F_i$ 上，作真实 Walsh 提升，再按正标量缩放，得到实际扩张因子 $\widetilde U_i$ 及其收缩逆 $\widetilde R_i$，准确真空列为
$$
\widetilde g_i=\widetilde U_i1
=\frac{g_{q_i}}{1-\varepsilon_i},
\qquad
0\le\varepsilon_i\le q_i^{-2}.
\tag{1.4}
$$
其 $q_i\ge4096$、$\sum_iq_i^{-1}<\infty$，而各物理位及更强 carry 预算依该附录选择。已证明
$$
P_n=\prod_{i\le n}\widetilde R_i\longrightarrow P
\quad\mathrm{SOT},
\qquad
g_n=\prod_{i\le n}\widetilde g_i\longrightarrow g\quad\text{于 }H,
$$
$$
Pg=1,\qquad P\ne0,\qquad G=P^{-1}=X_g,
\tag{1.5}
$$
并有同一组收缩强主理想单位。特别有限 Walsh 多项式是 $G$ 的完整图核心，且
$$
Gu=X_ug
\quad\text{对每个有限 Walsh 多项式 }u.
\tag{1.6}
$$
本稿不重证这些全局构造；以下补充此前尚未给出的完整次数上界。

## 2. $\sqrt3$ 加权有限块的全积分控制

记
$$
r=\sqrt3,\qquad
\|f\|_r=\|r^{\mathsf N}f\|,
\qquad
\mathsf N\chi_B=|B|\chi_B.
$$
对 (1.3) 的纯块，令 $x=s/(q+2)$。因为各位正交，
$$
\|r^{\mathsf N}v_q(s)\|^2
=[1-2x+4x^2]^q.
\tag{2.1}
$$

### 2.1 一个留有严格积分余量的初等上界

对所有 $x\ge0$，
$$
\boxed{1-2x+4x^2\le e^{(29/20)x}.}
\tag{2.2}
$$
证明。令 $c=29/20$，
$H(x)=e^{cx}-1+2x-4x^2$。其导数
$H'(x)=ce^{cx}+2-8x$ 的最小值为
$$
2+\frac8c\left(1-\log\frac8{c^2}\right).
$$
该值为正，因为
$$
\log\frac8{c^2}
=\log4+\log\frac{800}{841}
<\frac75-\frac{41}{841}
<\frac{109}{80}=1+\frac c4.
$$
这里 $\log(1-u)\le-u$，而 $\log4<7/5$ 可由 $e^{7/5}$ 的前六个 Taylor 项直接验证。于是 $H'>0$、$H(0)=0$，得到 (2.2)。

由 (2.1)—(2.2)，准确有
$$
\boxed{\|r^{\mathsf N}v_q(s)\|\le e^{29s/40}.}
\tag{2.3}
$$
这与积分权 $e^{-3s/4}$ 留下 $1/40$ 的严格正差，故不会在大 $s$ 处失控。

### 2.2 非真空部分的加权 $q^{-1/2}$ 界

在 $0\le x\le1/4$ 上，
$$
1-2x+4x^2\le1-x.
$$
两个正数的 $q$ 次幂作差，给
$$
\begin{aligned}
\|r^{\mathsf N}v_q(s)-h_q(s)\Omega\|^2
&=[1-2x+4x^2]^q-(1-x)^{2q}\\
&\le3q x^2[1-2x+4x^2]^{q-1}.
\end{aligned}
$$
因 $q\ge4$，
$$
\boxed{
\|r^{\mathsf N}v_q(s)-h_q(s)\Omega\|
\le\frac{\sqrt3\,s}{\sqrt q}e^{-s/4}
\quad(0\le s\le(q+2)/4).
}
\tag{2.4}
$$
对于全部 $s\ge0$，减去真空正交投影不会增加范数，故这个非真空部分亦不超过 (2.3) 的上界。

于是由 (1.3)，
$$
\begin{aligned}
\|r^{\mathsf N}g_q-\alpha_q\Omega\|
&\le\frac{7\sqrt3}{16\sqrt q}
 \int_0^\infty s e^{-s}ds
+\frac7{16}\int_{(q+2)/4}^\infty e^{-s/40}ds\\
&=\frac{7\sqrt3}{16\sqrt q}
+\frac{35}{2}e^{-(q+2)/160}\\
&\le\frac{100}{\sqrt q}.
\end{aligned}
\tag{2.5}
$$
例如
$\sup_{q>0}\sqrt q\,e^{-q/160}=\sqrt{80/e}<11/2$
已足以给最后的安全常数。

将 (1.2) 与 (2.5) 作正交平方和，得到
$$
1\le\|g_q\|_r^2
\le(1+12/q)^2+10^4/q
\le1+\frac{10060}{q}.
\tag{2.6}
$$
下界来自 $r\ge1$ 及 $\|g_q\|\ge1$。

## 3. 实际无限源的端点次数矩

在真实提升中，真空列仍准确是 (1.4)，不是纯近似。由于
$\varepsilon_i\le q_i^{-2}\le1/4$，
$$
(1-\varepsilon_i)^{-2}\le1+4\varepsilon_i.
$$
因此 (2.6) 给安全的统一界
$$
\boxed{
1\le\|\widetilde g_i\|_r^2
\le1+\frac{2^{14}}{q_i}.
}
\tag{3.1}
$$
例如对 $q\ge4$，
$10060+4/q+40240/q^2\le12576<2^{14}$ 即可。

各块互不交，次数算子对张量因子相加。准确普通 Walsh 块乘积 $g_n$ 因而满足
$$
\|g_n\|_r^2
=\prod_{i\le n}\|\widetilde g_i\|_r^2
\le\exp\left(2^{14}\sum_iq_i^{-1}\right)<\infty.
\tag{3.2}
$$
又 $g_n\to g$ 于原 $H$，所以每个 Walsh 系数收敛。对加权非负平方和用 Fatou，即得
$$
\boxed{
g\in\mathcal H_{\sqrt3},\qquad
\|g\|_{\sqrt3}
\le\exp\left(2^{13}\sum_iq_i^{-1}\right).
}
\tag{3.3}
$$
无需假设实际算子乘积与纯模型同态。这里只使用已经证明的真实真空列恒等式，以及有限块上计算出的加权范数。R267 的强收敛与 carry 选择均保持原样。

## 4. 整个指数次数空间的真实逆上界

[R255](../results/R255-optimal-sqrt3-degree-threshold-and-normal-factorization.md)
定理 A 及 §5 给实际最小闭乘积
$$
\odot:\mathcal H_{\sqrt3}\times\mathcal H_{\sqrt3}\to H,
\qquad
\|f\odot u\|\le C_*\|f\|_{\sqrt3}\|u\|_{\sqrt3},
\quad C_*=1+\epsilon_{\sqrt3}<2.
\tag{4.1}
$$
这适用于任意两输入，不只适用于正态的对角配对。

固定 $u\in\mathcal H_{\sqrt3}$，取有限 Walsh $u_n\to u$ 于该加权范数。由 (1.6) 和 (4.1)，
$$
Gu_n=X_{u_n}g=g\odot u_n\longrightarrow g\odot u
\quad\text{于 }H.
$$
因为 $G=P^{-1}$ 为闭算子，
$$
\boxed{
u\in\operatorname{Dom}G,\qquad Gu=g\odot u,\qquad
\|Gu\|\le C_g\|u\|_{\sqrt3},
\quad C_g=C_*\|g\|_{\sqrt3}<\infty.
}
\tag{4.2}
$$
也可直接从 $P(Gu_n)=u_n$ 和 $P$ 有界取极限，验证
$P(g\odot u)=u$；因此这是实际原像，不是形式逆词。

若使用 $H_\sigma=\operatorname{Dom}e^{\sigma\mathsf N}$ 的参数，(4.2) 就是
$$
\boxed{H_{\log\sqrt3}\subseteq\operatorname{Ran}P.}
\tag{4.3}
$$

令 $\mathcal D_d$ 为完整的次数至多 $d$ 的闭 Walsh 子空间，允许任意高位和无限平方可和系数。则
$\|u\|_{\sqrt3}\le3^{d/2}\|u\|$ 对整个 $\mathcal D_d$ 成立，所以
$$
\boxed{
\mathcal D_d\subseteq\operatorname{Ran}P,\qquad
\|G|_{\mathcal D_d}\|\le C_g3^{d/2}
\quad(d=0,1,\ldots).
}
\tag{4.4}
$$
这不是只控制每个单独 $\chi_B$；它控制整个无限维固定次数层以及任意线性组合。

因此 R267 第二附录的有限柱次数成本 $M_P(d)$ 实际总是有限，并满足
$$
\limsup_{d\to\infty}\frac{\log M_P(d)}d\le\log\sqrt3.
\tag{4.5}
$$
结合该附录既有下界，
$$
\kappa=\log(4/3)-1/4
\le\liminf_{d\to\infty}\frac{\log M_P(d)}d
\le\limsup_{d\to\infty}\frac{\log M_P(d)}d
\le\log\sqrt3.
\tag{4.6}
$$
这里不声称精确指数型已经算出。$\sigma<\kappa$ 的既有非像结论与 (4.3) 完全相容，二者之间仍有间隔。

## 5. 聚合界对每个固定次数的必要 $\ell^2$ 矩条件

设正常泛函 $\phi$ 对这个 $P$ 满足 R244 聚合界
$$
|\phi(X_u)|\le C_\phi\|Gu\|
\qquad(u\text{ 为有限 Walsh 多项式}).
\tag{5.1}
$$
记
$$
m_B=\phi(V_B).
$$
对支撑在次数至多 $d$ 的任意有限系数列，
$$
\left|\sum_{|B|\le d}u_Bm_B\right|
=|\phi(X_u)|
\le C_\phi C_g3^{d/2}\left(\sum|u_B|^2\right)^{1/2}.
$$
Riesz 表示或直接取有限截断最优系数，得到
$$
\boxed{
\sum_{|B|\le d}|m_B|^2
\le C_\phi^2C_g^2\,3^d
\qquad(d=0,1,\ldots).
}
\tag{5.2}
$$
特别一次矩 $(\phi(V_j))_{j\ge0}$ 必须属于 $\ell^2$。

该条件是聚合分解的必要条件，不被声称充分。一般正常泛函的一次矩只有既有的高位消失结论，不能据正常性将它换成平方可和。

## 6. 一个固定正常正态同时阻止整个端点源类

选互不交有限位块 $B_k$，满足
$$
|B_k|=2^{4k},\qquad c_k=2^{-k-2},\qquad k\ge1.
$$
将块依次放到足够高的位置，使
$$
8\eta_j\frac{49}{48}\le c_k^2
\qquad(j\in B_k).
\tag{6.1}
$$
真实 $\eta_j\le e^{-77016^j}$ 保证每一步可行。令
$$
f=1+\sum_{k\ge1}c_k\chi_{B_k},\qquad
\rho_f=f\otimes f,\qquad \phi_f(T)=\langle Tf,f\rangle.
\tag{6.2}
$$
$\sum c_k=1/4$，故级数一致收敛，$f$ 连续且
$3/4\le f\le5/4$。各块大小为偶数，所以原反射共轭满足 $Cf=f$。又 Walsh 正交性给
$$
\|f\|^2=1+\sum c_k^2=\frac{49}{48}.
$$

令 $D_j=I-2E_j$ 为纯 Cayley 位算子。其 Walsh 矩阵为
$$
D_j=\begin{pmatrix}0&-I\\I&2I\end{pmatrix},
\qquad
\operatorname{Re}D_j=2P_j,
$$
其中 $P_j$ 保留所有含位 $j$ 的 Walsh 系数。对 $j\in B_k$，
$$
\operatorname{Re}\langle D_jf,f\rangle=2c_k^2.
$$
实际估计 $\|V_j-D_j\|\le8\eta_j$ 和 (6.1) 因而给
$$
\boxed{
\operatorname{Re}\phi_f(V_j)\ge c_k^2
\qquad(j\in B_k).
}
\tag{6.3}
$$
于是
$$
\sum_j|\phi_f(V_j)|^2
\ge\sum_k |B_k|c_k^4
=\sum_k2^{-8}
=\infty.
\tag{6.4}
$$

因此这个同一个正、正常、秩一、连续且 $C$ 实的泛函不可能对任何满足
$g=P^{-1}1\in\mathcal H_{\sqrt3}$ 的 R244 强单位正则器满足聚合界。尤其它同时阻止 R267 第二附录的全部物理块位置选择满足该界，尽管这些正则器已具有线性次数逆下型。

若对这样的 $P$ 还有
$Pf\in\operatorname{Dom}X_f$，则 R244 的逐输入配对结论会给聚合表示，再与 (6.4) 矛盾。因此也可准确写成
$$
Pf\notin\operatorname{Dom}X_f
$$
对上述整类 $P$ 成立。

本例非负，且其 Walsh 系数绝对可和；它早已属于 R235/R237 可排的正常态类，不是慢主理想湮灭者。它只表明，提高少数逆方向的增长率乃至达到线性次数下型，仍不能替代对指定正常矩的完整控制。

## 7. 当前剩余问题

本稿给出的是整个次数空间上的真实上界，而不是为任意正常见证完成配对。对假想见证仍须证明 R244 的全部有限列聚合界；(5.2) 和 (6.4) 显示其中已经有非平凡的一次层障碍。

一般正常湮灭者可能具有不同的一次矩几何，也可能要求 $P^{-1}1$ 离开 $\mathcal H_{\sqrt3}$ 乃至离开全部一阶共同域。这里没有证明这些情况发生或不发生，没有给 $P=SR$ 的有界因式，也没有给 R253 的完整 $q_m$ 非消失下界。普通 Hilbert ISP 仍未解决。
