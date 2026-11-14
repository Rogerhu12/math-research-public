# R150 附录：有限对数 jet、Vandermonde 尾相消与一般多项式循环性

日期：2026-11-13（UTC）。作者：kernel_resume_1cf / Astra-ISP-1cf8c51d；AI 辅助：GPT-6 Astra Pro。
状态：已证明。

本稿在[对数加权齐次稿及其 §10](R150-appendix-logarithmic-weighted-homogeneous-resonances-below-degree-two.md)之外增加一个可检查的有限 jet 判据。旧稿用普通消失阶 $m$ 支付 $D<2m$；这里同时消去有限个实际行的不同尾阶，以数值矩阵的逆定义真实线性组合。新判据容许一般非齐次多项式，并给出普通消失阶仅为 1、加权次数任意大的新族。

全文保留原完整混合 Bell 系数。所有变化坐标都是有限线性的；不向无界算子代入非线性解析坐标，也不从分别循环的向量推断其点态乘积循环。

## 1. 固定原函数、有限 jet 与主定理

对每个固定 $\rho>0$，沿用原实际行
$$
a_j^{(\rho)}
=\frac{\rho(\log(j+2))^{\rho-1}}{j+2},
\qquad
u_\rho=-\kappa_\rho+\sum_{j\ge0}a_j^{(\rho)}\chi_j,
\tag{1.1}
$$
其中唯一实常数 $\kappa_\rho$ 由
$$
\sum_{j<n}a_j^{(\rho)}
=(\log(n+2))^\rho+\kappa_\rho+
O\!\left(n^{-1}(\log(n+2))^{\rho-1}\right)
\tag{1.2}
$$
确定。每行属于 $\ell^2\setminus\ell^1$。这里的原常数固定，不随测试头改变。

先取两两不同的正实数
$\alpha_1,\ldots,\alpha_\ell$，令 $u_\nu=u_{\alpha_\nu}$，
$X_\nu=X_{u_\nu}$ 为原规范闭 first。定义固定数值矩阵
$$
\boxed{
M_{\nu r}=\alpha_\nu\binom{\alpha_\nu-1}{r-1},
\qquad 1\le \nu,r\le\ell.
}
\tag{1.3}
$$
广义二项式按有限多项式定义。其行列式是
$$
\boxed{
\det M=
\frac{\prod_{\nu=1}^{\ell}\alpha_\nu}
{\prod_{r=1}^{\ell}(r-1)!}
\prod_{\nu<\mu}(\alpha_\mu-\alpha_\nu)\ne0.
}
\tag{1.4}
$$
这是普通数值矩阵的逆，不涉及未知算子上的可逆性。

将非零标量多项式 $F\in\mathbb C[x_1,\ldots,x_\ell]$ 按原权分解：
$$
F=\sum_{D\in\mathcal D}G_D,\qquad
G_D(x)=\sum_{\alpha\cdot\beta=D}f_\beta x^\beta.
\tag{1.5}
$$
$\mathcal D\subset[0,\infty)$ 是有限集，删去零分量。权可为任意正实数，无需有理比例。

对每个分量定义真正有限的标量多项式
$$
\mathcal J_D(t)=G_D(\mathbf1+Mt),\qquad
\omega(\beta)=\sum_{r=1}^{\ell}r\beta_r,
$$
$$
\boxed{
\nu_D=\min\{\omega(\beta):[t^\beta]\mathcal J_D\ne0\}.
}
\tag{1.6}
$$
因为 $M$ 可逆且 $G_D\ne0$，这个最小值有限；
$G_D(\mathbf1)\ne0$ 时恰为 0。

设至少一个分量在 $\mathbf1$ 处不为零，并令
$$
\boxed{
d_0=\max\{D:G_D(\mathbf1)\ne0\},\qquad
c_0=G_{d_0}(\mathbf1)\ne0.
}
\tag{1.7}
$$
只对更高分量作要求：
$$
\boxed{
D>d_0\quad\Longrightarrow\quad D-d_0<\nu_D.
}
\tag{1.8}
$$
这些更高分量都满足 $\nu_D\ge1$。若不存在更高分量，(1.8) 为空条件。

**定理 1。** 在 (1.1)—(1.8) 下，任意原复 $\ell^2$ first 指数
$w=w_*+\sum_jw_j\chi_j$ 都满足：

1. 若 $d_0>0$，则对每个非零标量多项式 $Q$，
   $$
   \boxed{Q(F(u_1,\ldots,u_\ell))e^w\text{ 对原实际 }A\text{ 循环}.}
   \tag{1.9}
   $$
   特别全部 $[F(u)-\lambda]^r e^w$，$\lambda\in\mathbb C,\ r\ge1$，均循环。
2. 若 $d_0=0$，则 (1.9) 对每个满足 $Q(c_0)\ne0$ 的 $Q$ 成立。
   特别全部 $[F(u)-\lambda]^r e^w$，$\lambda\ne c_0,\ r\ge1$，均循环。

主定理还包括 $F(u)^r e^w$：因为 $c_0\ne0$，两种情形都允许 $Q(z)=z^r$。

**全相消推论。** 若每个 $G_D(\mathbf1)=0$，但
$$
\boxed{D<\nu_D\quad(D\in\mathcal D),}
\tag{1.10}
$$
则对每个 $Q(0)\ne0$，都有
$$
\boxed{Q(F(u))e^w\text{ 循环}.}
\tag{1.11}
$$
特别所有非零参数 $\lambda$ 的全部点态幂成立。
这也可将 $F$ 换为 $F-\lambda$、加入真实的零权常数分量 $-\lambda$，再用定理 1。

若部分 $\alpha_\nu$ 重复，先在原 $F$ 中把对应变量置为同一个变量，再删去零分量。这一步合法是因为 (1.1) 给出的原函数及其固定常数完全相同。若合并后 $F$ 为常数 $c$，则目标准确为 $Q(c)e^w$，当且仅当 $Q(c)\ne0$ 时循环；其余情形使用不同权的上述定理。

## 2. 实际中心与覆盖全远尾的估计

令
$$
F_n=\{0,\ldots,n-1\},\qquad S=S_n=\log(n+2),
$$
$$
s_{\nu n}=-\kappa_{\alpha_\nu}+\sum_{j<n}a_j^{(\alpha_\nu)},
\qquad p_{\nu n}=s_{\nu n}/S^{\alpha_\nu}.
$$
由 (1.2)，
$$
\boxed{p_{\nu n}=1+O((nS)^{-1}).}
\tag{2.1}
$$
(1.2) 的证明是比较最终递减函数
$\rho(\log x)^{\rho-1}/x$ 与逐个单位区间积分；尾误差由该处的函数值控制，有限低位只改变一个固定常数。

对任意固定 $R\ge0$，
$$
\boxed{
\sum_{j\ge n}
\frac{[1+\log((j+2)/(n+2))]^R}{(j+2)^2}
\le C_R/n.
}
\tag{2.2}
$$
将 $x_j=\log((j+2)/(n+2))$ 按 $[h,h+1)$ 分组：
每组位数至多 $C(n+2)e^h$，分母至少
$(n+2)^2e^{2h}$，再求和
$\sum_h(1+h)^Re^{-h}$ 即得。
因此后文非整数幂的余项均覆盖任意大的 $j/n$，并不只在近尾作 Taylor 近似。

## 3. 真实线性 jet 行及其分阶尾预算

在原共同深词域中作有限线性变化
$$
Z_{\nu n}=\frac{X_\nu-s_{\nu n}}{S^{\alpha_\nu}},
\qquad
\boxed{J_n=M^{-1}Z_n.}
\tag{3.1}
$$
无需把任何一个自然无界和宣称为在最大交域上已经闭。后续只使用这些有限词的规范共同实现。

第 $r$ 个 $J_{rn}$ 的补集行为
$$
b_{rnj}=\sum_\nu(M^{-1})_{r\nu}
\frac{a_j^{(\alpha_\nu)}}{S^{\alpha_\nu}},
\qquad j\ge n.
$$
置
$$
f_r(y)=\sum_\nu(M^{-1})_{r\nu}
\alpha_\nu(1+y)^{\alpha_\nu-1}.
$$
由 (1.3)，$f_r$ 在 0 处的前 $\ell$ 个 Taylor 系数准确为
$$
[y^h]f_r(y)=\delta_{r,h+1},
\qquad 0\le h\le\ell-1.
\tag{3.2}
$$
特别它的前 $r-1$ 个低阶系数消失。对所有 $y\ge0$，有限次积分余项给
$$
|f_r(y)|\le C y^{r-1}(1+y)^R
\tag{3.3}
$$
，其中 $r=1$ 按 $y^0=1$ 解释；取一个依赖固定权族的足够大 $R$ 即可。
这是因为固定阶导数均是有限个 $(1+y)^\rho$ 的线性组合。

准确代入 $x=\log((j+2)/(n+2))$ 后，
$$
b_{rnj}=\frac1{S(j+2)}f_r(x/S).
$$
由 $S\ge1$、(3.3) 与 (2.2)，
$$
\boxed{
|b_{rnj}|\le
\frac{C x^{r-1}(1+x)^R}{S^r(j+2)},\qquad
\|b_{rn,\ge n}\|_2\le Cn^{-1/2}S^{-r}.
}
\tag{3.4}
$$

另一方面，正行的前缀和为 $O(S^{\alpha_\nu})$，所以
$$
\sum_{j<n}\left|
\sum_\nu(M^{-1})_{r\nu}a_j^{(\alpha_\nu)}/S^{\alpha_\nu}
\right|\le C.
\tag{3.5}
$$
在 $X_\nu-s_{\nu n}$ 中，有限头准确是
$\sum_{j<n}a_j^{(\alpha_\nu)}(V_j-I)$；
因此 (3.5) 对应真正带 $N_j$ 因子的头，固定原常数已由准确中心扣除。

由 (1.8) 选一个固定数 $0<\delta<1$，满足
$$
\frac{D-d_0}{\nu_D}<\delta
\quad(D>d_0).
\tag{3.6}
$$
没有更高分量时任取 $0<\delta<1$。定义实际线性变量
$$
\boxed{V_{rn}=S^{\delta r}J_{rn}.}
\tag{3.7}
$$
由 (3.4)—(3.5)，全部有限模式共同满足
$$
\boxed{
\varepsilon_n:=\sum_r g_{V_r,n}
\le Cn^{-1/2}S^{\delta-1},\qquad
\text{头绝对系数和}\le CS^{\delta\ell}.
}
\tag{3.8}
$$
这里使用 $S^{-r(1-\delta)}\le S^{-(1-\delta)}$，对所有 $r\ge1$ 成立。

## 4. 一般非齐次多项式的有限系数极限

以有限个交换标量变量 $v=(v_1,\ldots,v_\ell)$ 记实际变化
$$
x_\nu=S^{\alpha_\nu}
\left(p_{\nu n}+\sum_rM_{\nu r}S^{-\delta r}v_r\right).
\tag{4.1}
$$
这是原算子共同域上 (3.1)、(3.7) 的同一有限线性恒等式。
由各分量的原加权齐次性，
$$
S^{-d_0}F(x)
=\sum_D S^{D-d_0}
G_D\!\left(p_n+M\,\operatorname{diag}(S^{-\delta r})v\right).
\tag{4.2}
$$

先将 $p_n$ 换成 $\mathbf1$。一个原非零系数
$[t^\beta]\mathcal J_D$ 在 (4.2) 中的倍率准确为
$$
S^{D-d_0-\delta\omega(\beta)}.
\tag{4.3}
$$
当 $D\le d_0$ 时，该指数不大于 0；
等号只可能在 $D=d_0,\beta=0$。
当 $D>d_0$ 时，$\omega(\beta)\ge\nu_D$，由 (3.6) 指数严格为负。
因此形式中心下的整个有限多项式逐系数趋于 $c_0$。

必须再支付实际中心差。固定有限多项式
$G_D(p+Mt)$ 的每个系数都是 $p$ 的多项式；
在 $p$ 的一个固定邻域，系数差由 $C|p-\mathbf1|$ 控制。
由 (2.1)，真实 (4.2) 的任一系数误差至多
$$
\frac Cn S^{D-d_0-1-\delta\omega(\beta)}
\le \frac Cn S^{\max(0,D-d_0-1)}
\longrightarrow0.
\tag{4.4}
$$
有限个权和有限个单项式使这个估计一致成立。于是得到准确结论：
$$
\boxed{
S^{-d_0}F(x(v,n))\longrightarrow c_0
\quad\text{逐个有限标量系数}.
}
\tag{4.5}
$$
特别全部系数一致有界；没有把实际 $s_n$ 等同于 $S^\alpha$。

若 $Q$ 的次数为 $q$，最高系数为 $q_q\ne0$，令
$$
K=Q\circ F,\qquad b=q d_0.
$$
(4.5) 及有限多项式的乘法给
$$
\boxed{
S^{-b}K(x(v,n))\longrightarrow c_K,\qquad
c_K=
\begin{cases}
q_qc_0^q,&d_0>0,\\
Q(c_0),&d_0=0.
\end{cases}
}
\tag{4.6}
$$
定理允许的 $Q$ 都有 $c_K\ne0$。非零常数 $Q$ 的情形也按此解释。

全相消推论中，改选 $\delta>\max_D D/\nu_D$ 且 $\delta<1$，同一证明给
$F(x(v,n))\to0$ 逐系数，故整个 $Q(F(x(v,n)))\to Q(0)$。
以下证明只需 (4.6) 的非零常数极限，因此也一并覆盖该推论。

## 5. 原完整 Bell 的实际头与小补集

令 $m_0=\deg K$，并令 $D_*=\max\mathcal D$。
$K$ 的各原单项式权不超过 $qD_*$。
(4.1) 中常数和变量系数均至多 $CS^{\alpha_\nu}$，故对每个固定原多重指标 $\beta$，
$$
\boxed{
\max_\theta\left|[v^\theta]S^{-b}(\partial^\beta K)(x(v,n))\right|
\le CS^{qD_*}.
}
\tag{5.1}
$$
这里仅取粗略上界，已足支付所有原偏导；没有以普通总次数下降替代实际多尺度预算。

保留原实际生成函数
$$
H(\xi,V)=e^{-\xi V}(\cosh\xi\,I+V\sinh\xi),
\quad
B_w=\prod_jH(w_j,V_j),
$$
$$
\mathcal B_w(t)=
\prod_jH\!\left(w_j+\sum_\nu t_\nu a_j^{(\alpha_\nu)},V_j\right)
H(w_j,V_j)^{-1}.
\tag{5.2}
$$
把 $w$ 加作 [R145 §§2、8](R145-multimode-bell-mixed-domains-cyclicity.md) 的额外实际模式，并在其参数 1 处取共同整轨道，得到循环向量
$\xi_w=B_w^{-1}e^w$ 的全部原混合自然词域。
[R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md) 给规范最大闭图及该原指数图核心。

取字符为零的规范对数 $L_j(\xi)=\log H(\xi,V_j)$。
[R154 §3](R154-supercubic-modes-all-polynomials-exponential-weights.md) 的实际参数积分，以及[完全居中临界幂稿 §§4–5](R150-appendix-centered-critical-powers-gradient-tail-cancellation-and-nonzero-parameters.md)，给
$$
L_j^{(h)}(w_j)=N_jU_{hj},\quad
\sup_j\|U_{hj}\|<\infty
\quad(h\ge1\text{ 固定}),
$$
$$
L_j'(w_j)=w_jN_jW_j,\qquad \sup_j\|W_j\|<\infty.
\tag{5.3}
$$
后一式由 $L_j'(0)=0$ 及实际二阶商积分而来；
这些是实际 $N_j$ 商，不由“字符为零”免费推出。

尽管各原行不可和，它们均在 $\ell^2$。
高位的局部统一界
$\|L_j(w_j+\xi)-L_j(w_j)\|\le C(|w_j||\xi|+|\xi|^2)$
由 $\ell^2\times\ell^2$ 支付范数绝对收敛及逐次微分。
因此对 $\gamma\ne0$，原混合 log-Bell 累积量准确为
$$
\kappa_\gamma
=\partial^\gamma\log\mathcal B_w(0)
=\sum_j\left(\prod_\nu(a_j^{(\alpha_\nu)})^{\gamma_\nu}\right)
L_j^{(|\gamma|)}(w_j).
\tag{5.4}
$$

取固定整数
$$
M_0\ge\max(1,\ell,qD_*).
$$
对有限族 $1\le|\gamma|\le m_0$ 作准确拆分
$$
\boxed{
S^{M_0}\kappa_\gamma=H_{\gamma n}+E_{\gamma n},\qquad
H_{\gamma n}=\sum_{j<n}N_jB_{\gamma jn}.
}
\tag{5.5}
$$
(5.3)、一阶的 $\ell^2\times\ell^2$、高阶的 $\ell^2$ 乘积给
$$
\sum_{\gamma,j<n}\|B_{\gamma jn}\|\le CS^{M_0}.
\tag{5.6}
$$
置 $A_0=\max_\nu(\alpha_\nu-1)_+$。原行由
$C(\log(j+2))^{A_0}/(j+2)$ 控制；所以二阶及以上的乘积尾和至多
$CS^{m_0A_0}/n$，一阶由 (5.3) 再付
$CS^{A_0}n^{-1/2}\|w_{\ge n}\|_2$。从而
$$
\boxed{
\max_\gamma\|E_{\gamma n}\|
\le CS^{M_0+m_0A_0}
\left(n^{-1}+n^{-1/2}\|w_{\ge n}\|_2\right)
\longrightarrow0.
}
\tag{5.7}
$$
任意固定多项式对数因子都被 $n^{-1/2}$ 支付；未要求指数行有额外尾速度。

记 $C_\beta^w=\partial^\beta\mathcal B_w(0)$。当 $\beta\ne0$ 时，它是有限个 $\kappa_\gamma$ 的固定多项式，且没有常数项。原完整 Bell 是
$$
\boxed{
P_K(X)=\sum_\beta\frac{C_\beta^w}{\beta!}(\partial^\beta K)(X),
\qquad
K(u)e^w=B_wP_K(X)\xi_w.
}
\tag{5.8}
$$
这里没有重算、删去或只保各行自身的 Bell 系数。

对 $\beta=0$ 使用整体有限系数极限 (4.6)。
对 $\beta\ne0$ 使用 (5.1)、(5.5)；
含 $h\ge1$ 个累积量的单项式数值系数至多
$$
CS^{qD_*-M_0h}\le C.
\tag{5.9}
$$
因此 $S^{-b}P_K(X)$ 是固定次数、固定个数字母的精确多项式，
字母为 $V_{rn}$、带实际 $N_j$ 的有限头 $H_{\gamma n}$，以及小有界 $E_{\gamma n}$。
将 $E_{\gamma n}$ 吸收进交换有界系数，再拆开每个 $V_{rn}$ 的实际头和补集 first，得到共同预算
$$
\boxed{
A_n=\max(1,\text{全部头绝对费用})\le CS^{M_0},
\qquad
\varepsilon_n\le Cn^{-1/2}S^{\delta-1}.
}
\tag{5.10}
$$
所有显式头和补集 first 置零后，算子常数项趋于
$$
\boxed{c_K I.}
\tag{5.11}
$$
因为基础项由 (4.6) 支付，每个其他剩余 Bell 项至少含一个 (5.7) 的小算子。不存在把零字符系数当单位的步骤。

## 6. 真实进位、整个有限柱与长迭代

以下将所需预算写全，以明确增长头与小有界常数的量词。
记 $\mathsf Q_n=Q_{F_n}$ 为整个前 $n$ 位的柱投影。

实际关系
$$
N_j^2=\eta_jN_{j+1},\qquad
\eta_j\le e^{-770\,16^j},\qquad \|N_j\|\le1
$$
及 [R251](R251-arbitrary-coordinate-heads-and-rearrangement-invariant-first-centers.md) 的进位计数给：
若混合头词长度 $h\ge\max(2n,16)$，则
$$
\|\text{头词}\|\le A_n^h e^{-\gamma h^4},
\qquad\gamma=770/16^4.
\tag{6.1}
$$
头字母中的系数可为任意共同交换的有界 $A'$ 元素；先把系数移开，真正接受进位计数的是剩余的实际 $N_j$ 产品。无需那些系数物理支撑也在前 $n$ 位。

同一 R251 的补集指数次数尺度及有限多行极化给：
任意长度 $j$ 的混合补集伴随词，在整个 $\mathsf Q_nH$ 上有真实自然域，且
$$
\|\text{尾词}\,\mathsf Q_n\|
\le(C\varepsilon_n\sqrt j)^j.
\tag{6.2}
$$
全部有界交换系数保持共同词域，可移到左侧用原 $H$ 范数估计。

取有限整数
$$
\boxed{p_n=\lceil nS^{1-\delta}\rceil.}
\tag{6.3}
$$
由于 $0<\delta<1$，
$$
p_n/n\to\infty,\quad
\varepsilon_n\sqrt{p_n}=O(S^{-(1-\delta)/2})\to0,\quad
\frac n{p_n}\log A_n\to0.
\tag{6.4}
$$

设 $\mathscr T_n$ 是上述伴随字母的固定次数多项式，
系数一致有界，算子常数 $\Delta_{0n}\to0$。
将小常数也作为一个尾字母，记
$$
\delta_n=A_ne^{-\gamma(2n)^3},\qquad
e_n=\|\Delta_{0n}\|+C\varepsilon_n\sqrt{D'p_n},
$$
其中 $D'$ 是固定次数上界。展开 $\mathscr T_n^{p_n}$ 时，
每项头长 $h$、尾长 $j$、小常数字母数 $c$ 满足
$p_n\le h+j+c\le D'p_n$。字母种数、次数和系数界只付 $C_0^{p_n}$。

若 $h\ge2n$，用 (6.1) 将头根费用降为 $\delta_n$；
其余用 (6.2) 及小常数，得
$C_0^{p_n}(\delta_n+e_n)^{p_n}$。
若 $h<2n$，至少有 $p_n-2n$ 个尾或常数字母，得
$C_0^{p_n}A_n^{2n}e_n^{p_n-2n}$。
于是
$$
\boxed{
\|\mathscr T_n^{p_n}\mathsf Q_n\|^{1/p_n}
\le C_0\left[
\delta_n+e_n+
A_n^{2n/p_n}e_n^{\,1-2n/p_n}
\right]\longrightarrow0.
}
\tag{6.5}
$$
当 $e_n=0$ 时低头部分为零，按该值解释。
只要求 $\|\Delta_{0n}\|\to0$，不要求
$p_n\|\Delta_{0n}\|\to0$。

## 7. 原最大图排核及循环性

非零常数 $K$ 的结论直接由 $e^w$ 循环；以下取 $\deg K\ge1$。
令 $\mathcal P_K$ 是 (5.8) 的规范最大闭实现，
$\Pi$ 为其核的正交投影。
R186 给原全 $H$ 上的 $C$ 自伴性及 $\xi_w$ 的图核心；
不向未知限制或子商传递 $C$ 自伴性。

在原共同伴随深词域上 $\Pi P_K^*=0$。
令
$$
\boxed{
\mathscr T_n=I-\frac{S^{-b}P_K^*}{\overline{c_K}}.
}
\tag{7.1}
$$
由 (5.10)—(5.11)，其小算子常数和全部其他字母恰满足 §6。

对每个固定 $n$，(3.1)、(3.7) 只是有限个原 first 的线性组合；
补集 first 则再减去实际有界有限头。所有有限词恒等式均在同一原共同深域上成立。
R251 将整个 $\mathsf Q_nH$ 送入任意所需有限混合伴随词域，
包括当前有限的 $p_nD'$ 阶；
所有有界系数保持这些域。
故可逐次严格使用 $\Pi\mathscr T_n f=\Pi f$，得到
$$
\Pi\mathsf Q_n=\Pi\mathscr T_n^{p_n}\mathsf Q_n.
\tag{7.2}
$$
没有把 $n$ 依赖的系数穿过 $\Pi$，也没有让核向量免费进入高阶自然域。

(6.5) 使右侧算子范数趋零，而 $\mathsf Q_n\to I$ 强，
所以 $\Pi=0$。
原全 $H$ 的 $C$ 自伴性给 $\mathcal P_K$ 像稠密；
$\xi_w$ 的原图核心和实际有界交换单位 $B_w$ 再由 (5.8)
给 $K(u)e^w$ 循环。这证明定理及全相消推论。
整个 $Q(F)$ 的 Bell 在 (5.8) 中重新使用，未采用未经证明的循环向量乘法规则。

## 8. 三模式、简单零点而三阶 jet 的新例子

取任意 $0<D<3$，令
$$
(\alpha_1,\alpha_2,\alpha_3)=(D,D/2,D/3),
\qquad
G(x)=x_1-4x_2^2+3x_3^3.
\tag{8.1}
$$
它是原权次数 $D$ 的齐次多项式，
$G(\mathbf1)=0$，且
$\nabla G(\mathbf1)=(1,-8,9)\ne0$，普通消失阶为 1。

对 (1.3) 的矩阵，直接求导可核得
$$
\nabla G(\mathbf1)M_1=0,\qquad
\nabla G(\mathbf1)M_2=0,\qquad
D^2G(\mathbf1)[M_1,M_1]=0,
$$
$$
\boxed{\nabla G(\mathbf1)M_3=D^3/6\ne0.}
\tag{8.2}
$$
前一行恰消掉 jet 权 1、2 的全部单项式；
后一行保留 jet 权 3，故 $\nu_D=3$。
因此
$$
\boxed{
Q\!\left(u_D-4u_{D/2}^2+3u_{D/3}^3\right)e^w
\text{ 对全部 }Q(0)\ne0\text{ 循环}.
}
\tag{8.3}
$$
特别全部非零参数和点态幂成立。

当 $2\le D<3$ 时，普通消失阶仍为 1，
已超出旧严格条件 $D<2m=2$。
这里提高的是实际线性 jet 尾相消阶，不是把普通零点重数误算成 3。

## 9. 任意高 jet 阶及任意大的加权次数

固定整数 $R\ge2$ 和任意 $D>0$。令
$$
z_p=\frac1p,\qquad
\alpha_p=\frac Dp,\qquad
c_p=\frac1{\prod_{q\ne p}(z_p-z_q)}
\quad(1\le p\le R),
$$
$$
\boxed{G_{R,D}(x)=\sum_{p=1}^R c_p x_p^p.}
\tag{9.1}
$$
所有 $c_p\ne0$。由 Lagrange 插值比较最高系数，
$$
\boxed{
\sum_{p=1}^R c_p z_p^a=
\begin{cases}
0,&0\le a<R-1,\\
1,&a=R-1.
\end{cases}
}
\tag{9.2}
$$
所以 $G_{R,D}(\mathbf1)=0$，而各梯度分量 $pc_p\ne0$，普通消失阶准确为 1。
每项的原权为 $p(D/p)=D$。

下面证明其有限 jet 阶准确为 $R$，包括所有混合单项式。
设 $\beta\ne0$，普通次数 $h=|\beta|$，jet 权
$q=\sum_{j=1}^R j\beta_j$。
在 $(1+\sum_jM_{pj}t_j)^p$ 中，$t^\beta$ 的系数为
$$
\frac{(p)_h}{\beta!}
\prod_j\left[\alpha_p\binom{\alpha_p-1}{j-1}\right]^{\beta_j}.
\tag{9.3}
$$
$h>p$ 时使用落阶乘 $(p)_h=0$，同一式仍成立。
关键是
$$
(p)_h\alpha_p^h
=D^h\prod_{\ell=0}^{h-1}(1-\ell/p).
\tag{9.4}
$$
对 $h\ge1$，右侧作为 $z_p=1/p$ 的多项式次数至多 $h-1$；
剩余二项式乘积的次数至多
$\sum_j(j-1)\beta_j=q-h$。
因此 (9.3) 是 $z_p$ 的一个次数至多 $q-1$ 的多项式。
对它乘 $c_p$ 求和，(9.2) 消掉所有 $q<R$ 的 jet 单项式。

再取线性单项式 $t_R$。其系数是
$$
\sum_p c_p pM_{pR}
=D\sum_p c_p\binom{Dz_p-1}{R-1}.
$$
后一多项式的最高系数为 $D^{R-1}/(R-1)!$，于是
$$
\boxed{
[t_R]\,G_{R,D}(\mathbf1+Mt)
=\frac{D^R}{(R-1)!}\ne0,\qquad \nu_D=R.
}
\tag{9.5}
$$

由全相消推论，得到
$$
\boxed{
0<D<R
\quad\Longrightarrow\quad
Q\!\left(\sum_{p=1}^R c_p(u_{D/p})^p\right)e^w
\text{ 对全部 }Q(0)\ne0\text{ 循环}.
}
\tag{9.6}
$$
特别全部非零 $\lambda$、整数 $r\ge1$ 的
$\left[\sum_pc_p(u_{D/p})^p-\lambda\right]^r e^w$ 成立。

$R=3$ 时 $c=(3,-12,9)$，除以 3 正是 §8 的多项式。
给定任意大的有限 $D$，选固定整数 $R>D$，便得到该权次数、普通简单零点的新范围。模式数始终固定有限；没有让它随柱大小 $n$ 增长。

## 10. 范围、可检查性与尚未得到的结论

判据只需有限步骤：合并重复原模式，列出原权分量 $G_D$，计算固定矩阵 $M$，展开有限多项式 $G_D(\mathbf1+Mt)$，取最低整数 jet 权，再检查 (1.8) 或 (1.10)。无需寻找未知不变子空间、原 first 的谱，或构造无界逆。

旧 $D<2m$ 稿及此前单一临界幂非零参数是本稿的相关已知范围；
§§8–9 明确给出旧普通消失阶判据不含的简单零点族。
一般非齐次定理还允许较低真实中心项 $S^{d_0}c_0$ 保留下来，并将较高共振分量按各自 jet 阶同时控制。

严格不等式用于选择 $\delta<1$，从而在 (6.4) 同时支付长于头位数的迭代、尾根费用和增长头费用。
本稿不把等号端点、盘内零参数、无限模式或任意向量循环性列为已证。
真实正常见证的源预算、无权饱和及普通复 Hilbert 不变子空间问题仍未由这些多项式类完成。

## 11. 共同复对数幂的严格 jet 判据与全部 first 为全平面连续谱的新族

本节把已经完整支付的严格有限 jet 证明扩到共同复指数。
它不使用空谱 first，也不扩大临界等号范围。
固定 $\zeta\in\mathbb C$ 满足 $\operatorname{Re}\zeta>0$，
保留两两不同的正实数 $\alpha_\nu$，置
$$
\rho_\nu=\zeta\alpha_\nu.
$$

### 11.1 固定复中心常数

对任意固定复数 $\rho$ 满足 $\sigma=\operatorname{Re}\rho>0$，定义
$$
a_j^{(\rho)}
=\frac{\rho(\log(j+2))^{\rho-1}}{j+2},
\qquad
u_\rho=-\kappa_\rho+\sum_j a_j^{(\rho)}\chi_j.
\tag{11.1}
$$
所有复幂使用正实对数底的确定定义
$t^\rho=\exp(\rho\log t)$，$t>0$。
该行属于 $\ell^2\setminus\ell^1$。

这里 $\kappa_\rho$ 必须重新按原复行确定，不能使用实指数的常数。
令 $f_\rho(x)=\rho(\log x)^{\rho-1}/x$。
其导数满足
$$
|f_\rho'(x)|\le
C_\rho x^{-2}\bigl[(\log x)^{\sigma-1}
+(\log x)^{\sigma-2}\bigr]
$$
于充分大的 $x$。
逐个单位区间比较求和与积分，所得误差级数绝对收敛。
因此存在唯一固定复数 $\kappa_\rho$，使
$$
\boxed{
\sum_{j<n}a_j^{(\rho)}
=S^\rho+\kappa_\rho+O(n^{-1}S^{\sigma-1}),
\qquad S=\log(n+2).
}
\tag{11.2}
$$
这一步用导数绝对估计，不对复函数声称单调。
所以原实际中心仍准确满足
$$
s_{\nu n}=S^{\rho_\nu}+O(n^{-1}S^{\operatorname{Re}\rho_\nu-1}),
\qquad
\boxed{p_{\nu n}:=s_{\nu n}/S^{\rho_\nu}
=1+O((nS)^{-1}).}
\tag{11.3}
$$

### 11.2 复 Vandermonde 的实际全尾

改用固定复数矩阵
$$
M^\zeta_{\nu r}
=\rho_\nu\binom{\rho_\nu-1}{r-1}.
\tag{11.4}
$$
其行列式仍由 (1.4) 的同一多项式计算给出，
将各 $\alpha_\nu$ 换成 $\rho_\nu$ 即可。
$\zeta\ne0$ 且原权不同，故它可逆。

定义原共同深域上的有限线性变量
$$
Z_{\nu n}=\frac{X_{u_{\rho_\nu}}-s_{\nu n}}{S^{\rho_\nu}},
\qquad
J_n=(M^\zeta)^{-1}Z_n.
$$
令
$$
f_r(y)=\sum_\nu((M^\zeta)^{-1})_{r\nu}
\rho_\nu(1+y)^{\rho_\nu-1}.
$$
同一数值矩阵恒等式给
$$
[y^h]f_r(y)=\delta_{r,h+1}\qquad(0\le h<\ell).
$$
对实 $y\ge0$，这些复幂的固定阶导数仍满足
$C(1+y)^B$ 的模长界；
积分余项于是给 $|f_r(y)|\le Cy^{r-1}(1+y)^B$。
第 $r$ 行真实尾系数准确为
$$
\frac1{S(j+2)}
f_r\!\left(\frac{\log((j+2)/(n+2))}{S}\right).
$$
主稿 §2 的全远尾分组估计直接给
$$
\boxed{g_{J_r,n}\le Cn^{-1/2}S^{-r}.}
\tag{11.5}
$$

头绝对量也有真实预算，而不是复求和相消：
$$
|a_j^{(\rho)}|
=\frac{|\rho|(\log(j+2))^{\sigma-1}}{j+2},
\qquad
\sum_{j<n}|a_j^{(\rho)}|=O(S^\sigma).
$$
除以 $|S^\rho|=S^\sigma$ 后得到 $O(1)$。
故对任意固定 $0<\delta<1$，
$$
V_{rn}=S^{\delta r}J_{rn}
$$
与主稿完全相同地满足
$$
\varepsilon_n\le Cn^{-1/2}S^{\delta-1},\qquad
\text{头绝对量}\le CS^{\delta\ell}.
\tag{11.6}
$$

### 11.3 一般原多项式的准确复缩放

仍按原正实权 $\alpha$ 将 $F$ 分成 $G_D$，
而在本节定义
$$
\mathcal J_D^\zeta(t)=G_D(\mathbf1+M^\zeta t),
\qquad
\nu_D^\zeta=\min\{\omega(\beta):[t^\beta]\mathcal J_D^\zeta\ne0\}.
$$
若存在非零曲线分量，令
$$
d_0=\max\{D:G_D(\mathbf1)\ne0\},\qquad
c_0=G_{d_0}(\mathbf1).
$$
本节严格条件为
$$
\boxed{
D>d_0\quad\Longrightarrow\quad
(\operatorname{Re}\zeta)(D-d_0)<\nu_D^\zeta.
}
\tag{11.7}
$$
取 $\delta<1$ 严格大于全部比值。
实际线性逆式是
$$
x_\nu=S^{\rho_\nu}
\left[p_{\nu n}+\sum_rM^\zeta_{\nu r}S^{-\delta r}v_r\right].
$$
原加权齐次等式逐单项式给
$$
S^{-\zeta d_0}F(x(v,n))
=\sum_D S^{\zeta(D-d_0)}
G_D\!\left(p_n+M^\zeta\operatorname{diag}(S^{-\delta r})v\right).
\tag{11.8}
$$
一个 jet 单项式的倍率模长准确为
$$
S^{(\operatorname{Re}\zeta)(D-d_0)-\delta\omega(\beta)}.
$$
因此主稿 §4 的有限系数证明原样成立：
较低曲线分量按模长趋零，更高分量由 (11.7) 消去；
实际 $p_n-\mathbf1$ 的误差始终是一个固定对数幂乘 $n^{-1}$。
故
$$
\boxed{S^{-\zeta d_0}F(x(v,n))\longrightarrow c_0
\quad\text{逐系数}.}
\tag{11.9}
$$
这里归一化是完整复数 $S^{-\zeta d_0}$，
不是只除以其模长而忽略原中心相位。

于是主定理的全部结论成立，目标函数改为
$F(u_{\rho_1},\ldots,u_{\rho_\ell})$：

- $d_0>0$ 时，所有非零外层 $Q$ 均可；
- $d_0=0$ 时，要求 $Q(c_0)\ne0$；
- 若所有曲线分量都为零，要求
  $(\operatorname{Re}\zeta)D<\nu_D^\zeta$，并允许所有 $Q(0)\ne0$。

为完整核实原 Bell，设 $q=\deg Q$、$K=Q\circ F$、
$D_*=\max\mathcal D$。
原偏导代入后的绝对系数至多
$CS^{(\operatorname{Re}\zeta)qD_*}$。
所以在主稿 §5 选整数
$$
M_0\ge\max(1,\ell,(\operatorname{Re}\zeta)qD_*)
$$
即可支付每个非基础 Bell 项。
复原行的全部混合累积量仍由同一实际 $N_j$ 商计算；
尾绝对估计只把 $A_0$ 换成
$\max_\nu(\operatorname{Re}\rho_\nu-1)_+$。
R145 的有限复 $\ell^2$ 模式、额外 $w$ 参数和 R186 的共同自然词域、规范最大图均适用，不新增域假设。

若 $d_0>0$，设 $c_n=S^{\zeta qd_0}$；
若 $d_0=0$ 或全相消则取 $c_n=1$。
原归一 Bell 为 $c_n^{-1}P_K$。
因此未知核迭代必须使用准确伴随标量
$$
\boxed{
\mathscr T_n
=I-\frac{\overline{c_n}^{\, -1}P_K^\dagger}{\overline{c_K}},
}
\tag{11.10}
$$
其中 $c_K$ 是 (4.6) 对应的非零极限。
其余仍取 $p_n=\lceil nS^{1-\delta}\rceil$，
真实 carry、混合尾和小常数根界完全由主稿 §§5–7 支付。
(11.10) 把 $P_K^\dagger$ 留在未知投影右侧最左的算子位置；
没有将复相位或其他系数穿过投影。
所以结论仍针对完整原点态 $Q(F)e^w$，并非自然算子幂的替代。

### 11.4 每个非实复幂 first 都有全平面连续谱

现在假设 $\operatorname{Im}\zeta\ne0$。
每个 $\rho_\nu$ 都有正实部和非零虚部。
对任意这样的 $\rho$，写 $\sigma=\operatorname{Re}\rho>0$。
原绝对头和与复头和分别满足
$$
\sum_{j<n}|a_j^{(\rho)}|
=\frac{|\rho|}{\sigma}S^\sigma+O(1),
\qquad
\sum_{j<n}a_j^{(\rho)}=S^\rho+O(1).
$$
对任意固定实角 $\theta$，其真实相位缺陷部分和因此有
$$
\begin{aligned}
\sum_{j<n}\left(|a_j^{(\rho)}|
-\operatorname{Re}(e^{-i\theta}a_j^{(\rho)})\right)
&=\frac{|\rho|}{\sigma}S^\sigma
-\operatorname{Re}(e^{-i\theta}S^\rho)+O(1)\\
&\ge\left(\frac{|\rho|}{\sigma}-1\right)S^\sigma+O(1)
\longrightarrow\infty.
\end{aligned}
\tag{11.11}
$$
$O(1)$ 可对 $\theta$ 一致；严格正系数来自 $\operatorname{Im}\rho\ne0$。

由已全文核验的
[R138 定理1及 §§4—7](R138-first-chaos-complete-spectrum-classification.md)，得到
$$
\boxed{
\sigma(X_{u_\rho})=\sigma_{\rm ap}(X_{u_\rho})=\mathbb C,
\quad\text{每个谱点均为连续谱点}.
}
\tag{11.12}
$$
固定复常数 $-\kappa_\rho$ 不改变“全部复平面”的结论。
本节的多项式排核因此没有隐藏空谱锚。
它也不把各 first 的连续谱误读为目标点态多项式具有非零核。

### 11.5 任意高阶简单零点的复幂共振

固定整数 $R\ge2$，以及任意复数 $\mathfrak D$ 满足
$$
0<\operatorname{Re}\mathfrak D<R,\qquad
\operatorname{Im}\mathfrak D\ne0.
$$
取
$$
\rho_p=\mathfrak D/p,\qquad
c_p=\left[\prod_{q\ne p}(1/p-1/q)\right]^{-1},
\qquad
G(x)=\sum_{p=1}^R c_px_p^p.
$$
这对应 $\alpha_p=1/p$、$\zeta=\mathfrak D$、原实权次数 $D=1$。
主稿 §9 的 Lagrange 消去是关于参数 $\mathfrak D$ 的纯多项式恒等式，故对复数仍逐项有效：
每个 jet 权 $q<R$ 的混合系数为零，而
$$
[t_R]\,G(\mathbf1+M^\zeta t)=\frac{\mathfrak D^R}{(R-1)!}\ne0.
$$
所以 $\nu_1^\zeta=R$，普通消失阶仍恰为 1。
由 (11.7) 的全相消版本，
$$
\boxed{
Q\!\left(\sum_{p=1}^R c_p(u_{\mathfrak D/p})^p\right)e^w
\text{ 对所有 }Q(0)\ne0\text{ 循环}.
}
\tag{11.13}
$$
特别全部非零参数、全部点态幂和任意复 $\ell^2$ 指数权成立，
同时每一个参与的原 first 都有 (11.12) 的全平面连续谱。

例如取 $\mathfrak D=5/2+i\tau$、任意 $\tau\ne0$，得到
$$
\boxed{
\left[u_{\mathfrak D}-4u_{\mathfrak D/2}^{\,2}
+3u_{\mathfrak D/3}^{\,3}-\lambda\right]^r e^w
\text{ 对全部 }\lambda\ne0,\ r\ge1,\ w\text{ 循环}.
}
$$
原中心复相位在三项中准确相消；各行的相位随物理位不断旋转。
这与此前共同 $3/-1$ 幅度产生的全平面例子不同，
也不由中心值占最大单项式比例的旧直接多尺度条件覆盖。

本补节只使用严格 jet 不等式；没有把复指数的临界等号、盘内零参数、无限模式或普通 ISP 计为已完成。

## 后续：合并矩方法与已解除的参数限制

[复对数合并矩池](R150-appendix-merged-complex-logarithmic-moment-pools-and-all-resonant-zero-parameters.md)以不同的正则化/矩阵提升方法，现已证明任意两个不同复对数模式的全部非零普通多项式，以及本系列 G_R 高阶共振族在所有 Re𝔇>0 下的全部参数、点态幂和指数权，包含零参数。原函数及固定中心不变；本稿已证的柱预算、单位条件和较多模式的其他范围仍保持各自准确假设。一般目标的最高合并矩系数全部为零时，不由新定理自动处理。
