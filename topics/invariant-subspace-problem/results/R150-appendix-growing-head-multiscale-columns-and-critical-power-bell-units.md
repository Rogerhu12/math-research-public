# R150 附录：增长头的多尺度柱预算与临界幂相消的完整 Bell 单位

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf。

状态：完整证明；根代理与 kernel_resume_1cf 已全文独立核查。

本稿承接真实多尺度全柱定理，但允许原标量多项式在各中心的最大单项式尺度上发生深相消。新的归一变化尺度不必等于中心：归一头可以增长，实际尾必须额外支付一个对数头成本。完整 Bell 常数保留为一个真实有界单位，不能只看原标量中心，也不能把整个 $A'$ 当作只有一个字符的代数。

## 1. 原族、变化尺度与明确预算

取固定有限原 first 族
$$
u_\nu=a_{\nu,*}+\sum_ja_{\nu j}\chi_j,\qquad
a_{\nu\cdot}\in\ell^2,\qquad X_\nu=X_{u_\nu},
\quad 1\le\nu\le q.
$$
不要求其中任何 $X_\nu$ 空谱。

对递增穷尽有限位集 $F_n$，记
$$
d_n=|F_n|,\quad
s_{\nu n}=a_{\nu,*}+\sum_{F_n}a_{\nu j},\quad
b_{\nu n}=\sum_{F_n}|a_{\nu j}|,\quad
g_{\nu n}=\|a_{\nu,F_n^c}\|_2.
$$
选实际正实变化尺度
$$
\boxed{t_{\nu n}\ge1.}
\tag{1.1}
$$
它们不是强行等于 $|s_{\nu n}|$。置
$$
A_n=\max\left(1,6\sum_{\nu=1}^q\frac{b_{\nu n}}{t_{\nu n}}\right),
\quad
\varepsilon_n=\sum_{\nu=1}^q\frac{g_{\nu n}}{t_{\nu n}},
\quad
\ell_n=1+\log A_n.
$$
核心条件为
$$
\boxed{d_n\varepsilon_n^2\ell_n\to0.}
\tag{1.2}
$$

(1.1) 与每行原 $\ell^2$ 范数给
$$
\boxed{A_n\le C\sqrt{d_n}\quad\text{最终成立}.}
\tag{1.3}
$$
这条真实头界会用于高头次数；不能仅保留 (1.2) 却删除 (1.1) 后继续引用 (1.3)。

## 2. 完整多项式的实际常数单位准则

设 $\mathcal P$ 是某个固定原有限 Bell 多项式的规范最大实现，其共同深域核心写作
$$
P(X_1,\ldots,X_q),
$$
$P$ 的次数为固定 $D\ge1$，全部系数有界并属于实际交换子代数 $\mathfrak C=A'$。保留 R186 的 $C$ 自伴性和原指数图核心。

取非零标量 $c_n$，按有限多项式系数定义
$$
P_n(z)=c_n^{-1}
P(s_{1n}+t_{1n}z_1,\ldots,s_{qn}+t_{qn}z_q)
=\sum_{|\alpha|\le D}E_{\alpha n}z^\alpha.
\tag{2.1}
$$
要求
$$
\boxed{
\sup_{n,\alpha}\|E_{\alpha n}\|<\infty,\qquad
E_{0n}\text{ 是有界单位},\qquad
\sup_n\|E_{0n}^{-1}\|<\infty
}
\tag{2.2}
$$
（允许删去有限初始指标）。

**定理 1。** 在 (1.1)—(1.2)、(2.2) 下，
$$
\boxed{\ker\mathcal P=0.}
\tag{2.3}
$$
所以对相应原完整点态 Bell 目标，$C$ 自伴性和已付指数图核心给循环性。

(2.2) 检验的是全部实际系数。若只知标量主项非零而未付完整 Bell 常数的单位性及逆范数，不够使用此定理。

## 3. 支付增长有限头的根估计

在原共同伴随词域上写
$$
\frac{X_\nu^*-\overline{s_{\nu n}}}{t_{\nu n}}
=H_{\nu n}+T_{\nu n}.
$$
R251 的任意有限位集、同一补集次数尺度及固定多行 Cauchy 极化给：

- 混合头词总次数为 $h$ 时，其范数不超过 $A_n^h$；
- 当 $h\ge\max(2d_n,16)$ 时，进一步不超过
  $A_n^h e^{-\gamma h^4}$；
- 混合尾词总次数为 $j$ 时，在整个 $Q_{F_n}H$ 上不超过
  $(C_q\varepsilon_n\sqrt j)^j$，全部所用自然词域同时合法。

这些是[真实多尺度稿 §2](R150-appendix-multiscale-column-budgets-bell-covariance-and-full-plane-joint-polynomials.md)的输入，只把固定有界头改为实际 $A_n$。一行版的对数头支付已见
[R243 §§2—3](R243-partial-sum-centers-and-log-tail-polynomial-cyclicity.md)。

定义
$$
\delta_n=A_n e^{-\gamma(2d_n)^3}.
$$
由 (1.3)，$\delta_n\to0$。充分大时，对于 $h\ge2d_n$，
$$
A_n^h e^{-\gamma h^4}\le\delta_n^h.
\tag{3.1}
$$

由 (1.2)，可选整数 $p_n$ 同时满足
$$
\boxed{
p_n/d_n\to\infty,\qquad
\varepsilon_n\sqrt{p_n}\to0,\qquad
(d_n/p_n)\log A_n\to0.
}
\tag{3.2}
$$
例如 $v_n=d_n\varepsilon_n^2>0$ 时，取
$$
L_n=\sqrt{\ell_n/v_n},\qquad p_n=\lceil d_nL_n\rceil.
$$
则
$$
v_nL_n=\sqrt{v_n\ell_n}\to0,\qquad
\ell_n/L_n=\sqrt{v_n\ell_n}\to0.
$$
若 $\varepsilon_n=0$，另取 $p_n$ 足够大使其余两式成立。

设 $\mathscr T_n$ 是 $H_{\nu n},T_{\nu n}$ 的次数至多 $D$ 的多项式，常数项严格为零，所有有界伴随交换系数一致有界。展开
$\mathscr T_n^{p_n}$。每个项的头总次数 $h$ 与尾总次数 $j$ 满足
$$
p_n\le h+j\le Dp_n.
$$
固定次数的总绝对系数和至多 $C_D^{p_n}$。置
$$
D_n=C_q\varepsilon_n\sqrt{Dp_n}\to0.
$$

若 $h\ge2d_n$，该项在 $Q_{F_n}H$ 上至多
$\delta_n^hD_n^j$；最终 $\delta_n+D_n<1$，所以这部分总和不超过
$$
C_D^{p_n}(\delta_n+D_n)^{p_n}.
$$
若 $h<2d_n$，则 $j\ge p_n-2d_n$，这部分不超过
$$
C_D^{p_n}A_n^{2d_n}D_n^{p_n-2d_n}.
$$
因此
$$
\boxed{
\|\mathscr T_n^{p_n}Q_{F_n}\|^{1/p_n}
\le C_D\left[
\delta_n+D_n+
A_n^{2d_n/p_n}D_n^{\,1-2d_n/p_n}
\right]\to0.
}
\tag{3.3}
$$
零尾时第二部分没有非零项，按零解释。最后极限正是 (3.2) 的三个预算。

这里没有要求头次数占 $p_n$ 的固定比例。$h<2d_n$ 的整段由
$A_n^{2d_n}$ 与尾的 $p_n-2d_n$ 次支付，因此允许 (1.3) 内增长的头。

## 4. 准确消去完整 Bell 常数

反设 $\ker\mathcal P\ne0$，令 $\Pi$ 为其正交投影。原共同伴随深域上有
$$
\Pi P^*=0.
$$
令
$$
\boxed{
\mathscr T_n
=I-\frac{P^*}{\overline{c_n}}\,(E_{0n}^{-1})^*.
}
\tag{4.1}
$$
按归一变量 $(X_\nu^*-\overline{s_{\nu n}})/t_{\nu n}$ 展开时，其常数项准确为
$$
I-E_{0n}^*(E_{0n}^{-1})^*=0.
$$
由 (2.2)，其余系数一致有界。全部系数与原伴随 first 交换并保持全部所需自然词域。

即使没有声称 $\Pi$ 与 $(E_{0n}^{-1})^*$ 交换，仍准确有
$$
\Pi\mathscr T_n=\Pi
$$
在共同深域上成立，因为 (4.1) 将 $P^*$ 放在该有界逆因子的左侧。真实自然词域及迭代给
$$
\Pi Q_{F_n}=\Pi\mathscr T_n^{p_n}Q_{F_n}.
$$
由 (3.3)，右侧趋零，而 $Q_{F_n}\to I$ 强，矛盾。定理1证毕。

## 5. 实际 Bell 系数所在的局部代数

下节需要用一个具体非零字符证明极限单位。此处使用的是
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},
$$
而不是将整个 $\mathfrak C=A'$ 当作只有一个字符的代数。

固定原两行 $(u,z)$ 和原指数权 $w$，记
$$
H(\xi,V)=e^{-\xi V}(\cosh\xi\,I+V\sinh\xi),\qquad
B_w=\prod_jH(w_j,V_j).
$$
把 $w$ 加为 [R145 §§2、8](R145-multimode-bell-mixed-domains-cyclicity.md) 的第三个实际模式并在其参数1处取值，原真实整轨道支付
$\xi_w=B_w^{-1}e^w$ 的全部原 $X_u,X_z$ 混合域，以及
$$
K(u,z)e^w=B_w P_K(X_u,X_z)\xi_w.
\tag{5.1}
$$
完整系数来自
$$
\mathcal B_w(s,t)
=\prod_jH(w_j+s a_j+t b_j,V_j)H(w_j,V_j)^{-1},
$$
$$
C_{ij}^w=\partial_s^i\partial_t^j\mathcal B_w(0,0).
$$
每个有限因子属于 $\mathcal A$；原局部一致范数极限及 Cauchy 导数仍在这个闭代数中，所以
$$
\boxed{C_{ij}^w\in\mathcal A.}
\tag{5.2}
$$

R32 的唯一字符 $\chi$ 满足 $\chi(V_j)=1$。标量恒等式
$$
H(\xi,1)=e^{-\xi}(\cosh\xi+\sinh\xi)=1
$$
使整个 $\mathcal B_w(s,t)$ 的字符恒为1。因此
$$
\boxed{
C_{00}^w=I,\qquad
\chi(C_{ij}^w)=0\quad(i+j>0).
}
\tag{5.3}
$$
这是实际有界系数的字符计算，保留任意复指数权，并没有删除其一阶 Bell 项。

## 6. 两条临界对数幂行及真实有限位移

固定整数 $k\ge2$，定义正系数
$$
a_j=\frac1{j+2},\qquad
b_j=\frac1{k(j+2)(\log(j+2))^{\,1-1/k}}.
\tag{6.1}
$$
两行均在 $\ell^2\setminus\ell^1$。

令
$$
T_n=(\log(n+2))^{1/k}.
$$
积分比较的余项可明确写为有限常数：
$$
\sum_{j<n}a_j=T_n^k+\kappa_a+O(n^{-1}),
$$
$$
\sum_{j<n}b_j=T_n+\kappa_b+
O\!\left(\frac1{nT_n^{k-1}}\right).
\tag{6.2}
$$
常数存在的理由是两个被求和函数最终正、递减；每个整数区间上“左端值减积分”的和单调有界，其尾不超过该处函数值。

固定任意复数 $c\ne0$，取实际原函数
$$
\boxed{
u=-\kappa_a+\sum_ja_j\chi_j,\qquad
z=c-\kappa_b+\sum_jb_j\chi_j.
}
\tag{6.3}
$$
前 $n$ 个物理位的准确中心为
$$
s_{1n}=T_n^k+O(n^{-1}),\qquad
s_{2n}=T_n+c+O((nT_n^{k-1})^{-1}).
\tag{6.4}
$$
$-\kappa_a$、$c-\kappa_b$ 都是固定的原常数，未按 $n$ 改变输入函数。

我们要证明
$$
\boxed{
[z^k-u-\lambda]^r e^w\text{ 对全部 }\lambda\in\mathbb C,\ r\ge1,\ w
\text{ 循环。}
}
\tag{6.5}
$$

这时 $s_{2n}^k$ 与 $s_{1n}$ 的主尺度都是 $T_n^k$，而
$$
(s_{2n}^k-s_{1n})/T_n^{k-1}\longrightarrow kc.
$$
所以此前要求中心值占最大单项式尺度固定比例的直接判据确实失败；比值只有 $O(T_n^{-1})$。

### 6.1 真实尾支付增长头

取前 $n$ 位作 $F_n$，$d_n=n$，并选择
$$
R_n=T_n^{k-1},\qquad t_{1n}=R_n,\qquad t_{2n}=1.
\tag{6.6}
$$
删除有限初始指标后两尺度都不小于1。

积分或二进区间比较给
$$
g_{1n}=O(n^{-1/2}),\qquad
g_{2n}=O(n^{-1/2}T_n^{-(k-1)}).
$$
因此
$$
\varepsilon_n=O((\sqrt n R_n)^{-1}),\qquad
A_n=O(T_n),
$$
以及
$$
\boxed{
n\varepsilon_n^2(1+\log A_n)
=O\!\left(\frac{1+\log T_n}{T_n^{2(k-1)}}\right)\to0.
}
\tag{6.7}
$$
这是 (1.2) 的具体预算；并没有用单一中心比为零代替它。

## 7. 临界相消后全部 Bell 系数与常数极限

固定 $\lambda,r,w$，令
$$
K(x,y)=(y^k-x-\lambda)^r.
$$
记原完整 Bell 为
$$
P_K(X,Y)
=\sum_{i,j\ge0}\frac{C_{ij}^w}{i!\,j!}
(\partial_x^i\partial_y^jK)(X,Y).
\tag{7.1}
$$

以 (6.6) 的变化尺度定义有限标量多项式
$$
Q_n(U,V)
=\frac{(s_{2n}+V)^k-(s_{1n}+R_nU)-\lambda}{R_n}.
$$
逐系数使用 (6.4) 得
$$
\boxed{Q_n(U,V)\longrightarrow k(c+V)-U.}
\tag{7.2}
$$
高于一次的 $V^j$ 系数为 $O(T_n^{1-j})$；常数项趋 $kc$，$U$ 系数恰为 $-1$。因此全部系数都有统一界。

原偏导准确满足
$$
\boxed{
R_n^{-r}
(\partial_x^i\partial_y^jK)
(s_{1n}+R_nU,s_{2n}+V)
=R_n^{-i}\partial_U^i\partial_V^jQ_n(U,V)^r.
}
\tag{7.3}
$$
这里不只说总次数降低，而逐项保留了 $x$ 方向额外的 $R_n^{-i}$。

将 (7.3) 代入完整 (7.1)，得到
$$
P_n(U,V)
:=R_n^{-r}P_K(s_{1n}+R_nU,s_{2n}+V)
$$
在 $\mathcal A$ 系数范数中逐系数收敛到
$$
\boxed{
P_\infty(U,V)
=\sum_{j=0}^r\frac{C_{0j}^w}{j!}
\partial_V^j[k(c+V)-U]^r.
}
\tag{7.4}
$$
因为 $R_n\to\infty$，所有 $i>0$ 项消失；$j>r$ 的极限导数为零。有限总阶使这些极限无需交换无穷 Bell 级数。

特别，完整常数系数
$$
E_n=P_n(0,0)
$$
按算子范数趋于
$$
\boxed{
E_\infty=k^r\sum_{j=0}^r
\binom rj c^{r-j}C_{0j}^w
\in\mathcal A.
}
\tag{7.5}
$$
用 §5 的准确字符，
$$
\boxed{\chi(E_\infty)=(kc)^r\ne0.}
\tag{7.6}
$$
$\mathcal A$ 的局部性因此使 $E_\infty$ 为真实有界单位。
由 $E_n\to E_\infty$，充分大时 $E_n$ 也是单位，且 Neumann 公式给统一逆范数，例如
$$
\|E_n^{-1}\|\le2\|E_\infty^{-1}\|.
$$

(7.4) 同时支付 (2.2) 的全部非恒定系数界，不只是常数。
故取 $c_n=R_n^r$，§6.1 与定理1完整适用，证明 (6.5)。

任意复指数权的高阶 $C_{0j}^w$ 都保留在 (7.5) 内；真正的单位性来自其整体非零字符，不能把它们直接丢掉。

## 8. 适用范围与准确剩余的完全居中分支

可以同时把固定复 $\beta$ 加回另一原行：
$$
v=\beta u+z.
$$
真实多尺度稿 §5 已付全部 Bell 的参数线性协变及同一正则器的双向最大图识别，所以 (6.5) 等价地给
$$
\boxed{
[(v-\beta u)^k-u-\lambda]^re^w
\text{ 对全部 }\lambda,r,w\text{ 循环。}
}
$$
原中心比仍趋于 $\beta$，最高普通符号在 $(1,\beta)$ 处为零；新的中心尺度也发生临界幂相消。此次排除依靠 (6.7) 和整个 (7.5) 的实际单位。

若 $c=0$，(7.5) 的字符为零。本稿没有给 $E_\infty$ 有界逆，也没有把它的拟幂零性当作单位性；完全居中的临界幂分支仍需另证。

旧范围扣除：R243 已有一行对数头根界；本稿新增固定多行、变化尺度和完整常数单位。R236 的[固定盘](R236-appendix-fixed-disk-kernel-inverses-and-sparse-linear-deviations.md)、[辅助共同圆](R236-appendix-auxiliary-scale-joint-resolvent-and-independent-tail-gaps.md)及[普通矩池稿](R236-appendix-ordinary-pointwise-moment-expansion-and-veronese-pools.md)分别要求辅助行可和，而 (6.1) 的两条行都不可和，不能直接套用那些范围。已有空谱自然多项式/有界辅助/固定复直线受控剪切的交集按原来源扣除；这里以较小的 $b$ 为主时 $a_j/b_j=k(\log(j+2))^{1-1/k}\to\infty$，而以 $a$ 为主的原最高符号又落在持久线性根。

一般更深相消、无此变化尺度预算的有限慢行、任意向量循环性、真正常见证的源上界及普通复 Hilbert ISP 继续开放。
