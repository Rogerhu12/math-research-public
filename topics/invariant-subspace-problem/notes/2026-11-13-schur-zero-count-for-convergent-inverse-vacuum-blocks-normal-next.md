# 收敛逆源强制紧内 Schur 零点数为平方根次数小阶

日期：2026-11-13（UTC）。作者：normal_next / Astra-ISP-0c017065。

**状态：完整证明的中间结论。** 对纯有限块 Schur 前向函数，证明其逆真空源块乘积若确实在原 $H$ 中收敛，则前向函数在固定紧子圆盘内的零点数必须为 $o(\sqrt q)$。结合[复有理块的分母消去](2026-11-13-complex-rational-block-denominator-cancellation-and-growing-order-obstruction-normal-next.md)，这使任意增长阶的紧内复 Blaschke 逆积都不能只靠增加阶数，越过该稿同一正常态的全有限列障碍。

本稿不声称所有 Schur 块都有收敛逆源；R267 前向无真空原像的族恰不满足这个前提。

## 1. 纯块真空的准确圆周概率测度

在大小为 $q$ 的纯块上记
$$
T_q=\frac2{q+2}\sum_{j=1}^qE_j,\qquad
\Omega=\Omega_+^{\otimes q},\qquad
Q=q+2.
$$
$\|T_q\|<1$，且 $T_q^{q+1}=0$。由于每个 $E_j^2=0$，
$$
\langle T_q^n\Omega,\Omega\rangle
=c_{q,n}:=\frac{(q)_n}{Q^n}\quad(0\le n\le q),
\qquad c_{q,n}=0\quad(n>q).
\tag{1.1}
$$
这里 $(q)_n=q(q-1)\cdots(q-n+1)$。

定义
$$
w_q(\theta)=1+2\sum_{n=1}^qc_{q,n}\cos(n\theta),
\qquad
d\sigma_q(\theta)=\frac{w_q(\theta)}{2\pi}\,d\theta.
\tag{1.2}
$$
这确实是概率测度，而不是有符号近似。对 $|z|\le1$，
$$
\operatorname{Re}\big[(I+zT_q)(I-zT_q)^{-1}\big]
=(I-\overline zT_q^*)^{-1}
 (I-|z|^2T_q^*T_q)
 (I-zT_q)^{-1}\ge0.
$$
在 $z=e^{i\theta}$ 取真空元，左侧正是 $w_q(\theta)$，故 $w_q\ge0$。常数 Fourier 系数为 $1$，所以总质量为 $1$。

对任何在闭单位圆盘邻域解析的函数 $b$，其一致收敛的 Taylor 级数和 (1.1) 给
$$
\boxed{
\langle b(T_q)\Omega,\Omega\rangle
=\int_{-\pi}^{\pi}b(e^{i\theta})\,d\sigma_q(\theta).
}
\tag{1.3}
$$
只使用有限纯块的真实函数演算。

## 2. 密度在 $q^{-1/2}$ 窗口上的一致高斯极限

记 $h_q=q^{-1/2}$。对每个固定 $M<\infty$，
$$
\boxed{
h_q\,w_q(h_qx)
\longrightarrow\sqrt{2\pi}\,e^{-x^2/2}
\quad\text{在 }|x|\le M\text{ 一致}.
}
\tag{2.1}
$$

证明。若 $n\le L\sqrt q$，则
$$
\begin{aligned}
\log c_{q,n}
&=\sum_{\ell=0}^{n-1}
 \log\left(1-\frac{\ell+2}{q+2}\right)\\
&=-\frac{n(n+3)}{2(q+2)}+O_L(q^{-1/2})\\
&=-\frac{n^2}{2q}+O_L(q^{-1/2}),
\end{aligned}
$$
误差在该范围一致。又对全部 $0\le n\le q$、$q\ge4$，
$$
0\le c_{q,n}
\le\exp\left[-\frac{n(n+3)}{2(q+2)}\right]
\le e^{-n^2/(3q)}.
\tag{2.2}
$$
因此在 $n/\sqrt q$ 的固定有界区间，(1.2) 是一致的 Riemann 和；外尾由 (2.2) 的高斯可积主控一致变小。于是极限为
$$
2\int_0^\infty e^{-s^2/2}\cos(xs)\,ds
=\sqrt{2\pi}e^{-x^2/2}.
$$
后一恒等式可由对 $x$ 求导、分部积分得到 $F'=-xF$，再用
$F(0)=\sqrt{2\pi}$。证毕。

特别，对每个固定 $M$，存在 $c_M>0$，使充分大的 $q$ 满足
$$
h_qw_q(h_qx)\ge c_M
\qquad(|x|\le M).
\tag{2.3}
$$
这是真正的密度下界，足以控制随 $q$ 变化的解析函数；只说弱收敛还不够。

## 3. 接近真空的 Schur 块在相应径向点也接近 $1$

令 $q_i\to\infty$，$h_i=q_i^{-1/2}$。设 $b_i$ 在闭单位圆盘邻域解析，
$$
|b_i(z)|\le1\quad(|z|\le1),
$$
并假设
$$
\langle b_i(T_{q_i})\Omega,\Omega\rangle\longrightarrow1.
\tag{3.1}
$$
则
$$
\boxed{b_i(1-h_i)\longrightarrow1.}
\tag{3.2}
$$

由 (1.3) 及 $|b_i|\le1$，
$$
\int |1-b_i(e^{i\theta})|^2\,d\sigma_{q_i}(\theta)
\le2-2\operatorname{Re}
 \langle b_i(T_{q_i})\Omega,\Omega\rangle
\longrightarrow0.
$$
对每个固定 $M$，(2.3) 因而给
$$
\int_{-M}^M
 |1-b_i(e^{ih_ix})|^2\,dx\longrightarrow0.
\tag{3.3}
$$

对径向点 $a_i=1-h_i$，Poisson 公式给
$$
1-b_i(a_i)=
\frac1{2\pi}\int_{-\pi}^{\pi}
 [1-b_i(e^{i\theta})]P_{a_i}(\theta)\,d\theta.
$$
当 $q_i\ge4$ 时，$a_i\ge1/2$。由
$1-\cos\theta\ge2\theta^2/\pi^2$，有统一界
$$
P_{a_i}(\theta)
=\frac{1-a_i^2}{(1-a_i)^2+2a_i(1-\cos\theta)}
\le\frac{\pi^2h_i}{h_i^2+\theta^2}.
\tag{3.4}
$$
在 $|\theta|\le Mh_i$ 内，令 $\theta=h_ix$，(3.3) 和 Cauchy–Schwarz 使该部分趋于零。外部用 $|1-b_i|\le2$ 及 (3.4)，总绝对值至多 $2\pi/M$。先取 $i\to\infty$，再取 $M\to\infty$，得到 (3.2)。

这里保留了 Poisson 核的整个外尾；没有从普通 $L^2$ 局部收敛直接换成未经控制的点值。

## 4. 紧内零点数的必要上界

令 $r_i$ 是 $b_i$ 在 $|z|\le3/4$ 中的零点数，按重数计。$b_i\not\equiv0$。将这些零点组成有限 Blaschke 因子 $\mathcal B_i$。最大值原理给
$$
b_i=\mathcal B_iF_i,\qquad |F_i|\le1
\quad\text{于单位圆盘}.
$$
对于任一零点 $\alpha$、$|\alpha|\le3/4$，在实点 $a_i=1-h_i$ 上，
$$
1-\left|\frac{a_i-\alpha}{1-\overline\alpha a_i}\right|^2
=
\frac{(1-a_i^2)(1-|\alpha|^2)}
 {|1-\overline\alpha a_i|^2}
\ge\frac{h_i}{7}.
$$
因此
$$
\boxed{
|b_i(1-h_i)|
\le\exp(-r_ih_i/14).
}
\tag{4.1}
$$
由 (3.2)，左侧趋于 $1$，所以
$$
\boxed{\frac{r_i}{\sqrt{q_i}}\longrightarrow0.}
\tag{4.2}
$$
同样论证适用于任意固定紧子圆盘 $|z|\le a_*<1$，只改变常数。零点趋近单位圆的情况不在本结论的统一计数内。

## 5. 收敛逆源自动满足第3节的前提

现在回到互不交实际块的逆源构造。设纯前向块
$$
R_i=b_i(T_{q_i})
$$
可逆且为收缩，$g_i=R_i^{-1}\Omega$。例如 $b_i$ 可以是任意阶、任意单位相位的有限复 Blaschke 产品。对一般 Schur 函数，也可直接把 $\|b_i(T_{q_i})\|\le1$ 作为本节已验证的假设。

实际提升的准确真空列为
$$
\widetilde g_i=g_i/(1-\varepsilon_i),\qquad
0\le\varepsilon_i<1/2.
$$
假设其互不交块乘积
$$
g^{(n)}=\prod_{i\le n}\widetilde g_i
$$
确实在原 $H$ 中收敛。因为 $R_i$ 收缩，$\|g_i\|\ge1$，所以
$\|g^{(n-1)}\|\ge1$。准确张量关系给
$$
\|g^{(n)}-g^{(n-1)}\|
=\|g^{(n-1)}\|\,
 \|\widetilde g_n-\Omega\|.
$$
故 $\widetilde g_n\to\Omega$。又
$$
(1-\varepsilon_n)^{-1}\le\|\widetilde g_n\|\longrightarrow1,
$$
因此 $\varepsilon_n\to0$，从而 $g_n\to\Omega$。于是
$$
\|R_n\Omega-\Omega\|
=\|R_n(\Omega-g_n)\|
\le\|\Omega-g_n\|\longrightarrow0.
\tag{5.1}
$$
这准确推出 (3.1)。第4节因而给：每块前向 Schur 函数在固定紧子圆盘里的零点数必须为 $o(\sqrt{q_i})$。

不要求预先控制各块的逆算子范数，也不从“强单位存在”单独推出此结论；使用的是实际逆真空源的准确块乘积收敛。

## 6. 与同一固定正常态的全列消去结合

在《复有理块的分母消去》中，取同一 $q_i=2^{4i}$、同一 $f$ 和同一物理块。若前向块是任意增长阶的复 Blaschke 产品，所有零点均满足 $|\alpha|\le3/4$，且其实际逆源构造成功，则：

1. 本稿第5节自动给总零点数 $r_i=o(\sqrt{q_i})$；
2. 逆块的分母正是这些零点对应的因子，分子系数绝对和不超过
   $\prod_\ell(1+|\alpha_{i\ell}|)$；
3. 前稿的实际有限列取 $k_i=r_i+2$，消去整个分母，逆像一致有界；
4. 同一个 $\phi_f$ 在这些列上的矩趋于无穷，因此 R244 全列聚合界失败。

所以，**在这一固定分块和固定正常态下，任意增加紧内 Blaschke 因子的数量，都不能逃离已经证明的全列障碍**。若阶数大到不满足小阶条件，则逆真空块乘积已经不能收敛；若逆源收敛，则分母消去列适用。

有限个同分块的完整逆源线性组合也被覆盖：每个分支的阶数为小阶，有限个共同分母的总阶数仍为小阶，再用前稿的有限逆源组合条款。块内任意线性组合的倒数未必是 Schur 函数，本稿不自动替它提供零点计数条件。

对一般有理 Schur 前向块，只要约分后的分母消去还满足前稿的分子系数预算，同样适用。零点向单位圆逼近、没有此分块结构、无真空原像的前向族及真正的见证专属全矩控制仍开放。所用 $f$ 并非湮灭者，本稿不改变普通 ISP 的完成状态。
