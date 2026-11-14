# 中央 theta 对角的有理下降与指数型整函数

日期：2026-11-12。**状态：下列复解析与定义域结论已证明；有限处 jet 预算尚未完成。**

**后续进展。** [R44](../results/R44-central-diagonal-global-coefficient-budget.md)
现已证明本图像的全部截断系数缩放预算为 $2\log k+O(1)$，
不能用它达到下文的充分门槛；真正 vanishing-jet 评价映射的最优估计仍待研究。

接续 `anticyclotomic-theta-diagonal` 笔记，保留其全部规范：
$$
f=34(1+i),\quad Nf=2312,\quad
\Gamma=\Omega_E\mathbb Z[i],\quad \Omega=\Omega_E/f,\quad
A=\Omega_E^2/\pi_{\mathbb C}.
$$
其中 $\Omega_E>0$；固定双级数 $\mathscr K$ 的中央对角为
$d_m=[z^mw^m]\mathscr K(z,w)\in K=\mathbb Q(i)$。
已证准确式为
$$
m!d_m=A(\mathfrak f)^{-m}\Omega^{-2m-1}
L_{\mathfrak f}(\bar\psi^{2m+1},m+1),\qquad
A(\mathfrak f)=Nf/\pi_{\mathbb C}.
\tag{1}
$$

本文证明，这条具体对角在复侧远比整个双级数简单：经一次固定的代数缩放，
它是有理系数、非代数、增长阶至多一的整函数。
结论不是从“双级数非 D-finite”推出来的，而来自 (1) 的完整阶乘。

## 1. 固定下降到有理数

定义
$$
e_m=\frac{d_m}{f^{2m+1}},\qquad
\mathscr D(Z)=\sum_{m\ge0}e_mZ^m.
\tag{2}
$$

**命题 1。** 对每个 $m\ge0$，$e_m\in\mathbb Q$。

**证明。** 曲线定义于 $\mathbb Q$，其 Hecke 字符满足
$\psi(\bar{\mathfrak a})=\overline{\psi(\mathfrak a)}$。
对理想施共轭说明 $L(\bar\psi^{2m+1},s)=L(\psi^{2m+1},s)$；
在实 $s$ 处，这个值因而是实数，等式经解析延拓保持。
由 (1)、$\Omega=\Omega_E/f$，
$$
e_m=
\frac{1}{m!\,\Omega_E}
\left(\frac{\pi_{\mathbb C}}{Nf\,\Omega_E^2}\right)^m
L_{\mathfrak f}(\psi^{2m+1},m+1)\in\mathbb R.
\tag{3}
$$
另一方面 $d_m,f\in K$，所以 $e_m\in K\cap\mathbb R=\mathbb Q$。
证毕。

这一步不把复周期当作有理数；代数性先由固定 torsion 初值和微分递推得到，
再取 $K\cap\mathbb R$。
所有目标 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$ 都满足 $v_p(f)=0$，
因此这个下降保留中央有限证书的准确赋值。

## 2. 固定导子、变化无穷型的中央值上界

置
$$
\chi_m=\psi^{2m+1}N^{-m-1/2},\qquad
\mathcal L_m(s)=L(\chi_m,s)
=L(\psi^{2m+1},s+m+1/2).
\tag{4}
$$
$\chi_m$ 是 unitary Hecke 字符。$\psi$ 的有限部分取值于 $\mu_4$；
指数 $2m+1$ 是奇数，故不改变其核与导子。
所以所有 $\chi_m$ 的有限导子都是同一个 $\mathfrak f$。
特别地，(3) 的 $L_{\mathfrak f}$ 没有额外删除一个本来未分歧的素位。

写
$$
\mathcal L_m(s)=\sum_{n\ge1}\frac{a_m(n)}{n^s}.
$$
每个理想的 unitary 权绝对值为一，故
$$
|a_m(n)|\le r_K(n)\le d(n),
\tag{5}
$$
其中 $r_K(n)$ 为范数 $n$ 的整理想数，$d(n)$ 是通常的约数个数。
后一不等式也可从 $\zeta_K(s)=\zeta(s)L(s,\chi_{-4})$ 的系数公式逐项得到。

Hecke 的函数方程在这里写为
$$
\Lambda_m(s)=Q^s\Gamma(s+m+1/2)\mathcal L_m(s),\qquad
Q=\frac{\sqrt{|D_K|Nf}}{2\pi_{\mathbb C}},
\tag{6}
$$
$$
\Lambda_m(s)=W_m\Lambda_{\bar\chi_m}(1-s),\qquad |W_m|=1.
$$
省去的因子只依赖 $m$，在两边相同。
因为无穷型 $2m+1$ 非零，完成函数是整函数；对偶的 gamma 因子相同。
此处不要求 $W_m=+1$，也不要求中央值非零。

**引理。** 存在与 $m$ 无关的常数 $C$，使
$$
|\mathcal L_m(1/2)|\le C\sqrt{m+1}\log(m+2).
\tag{7}
$$

给出所需上界的直接平滑函数方程证明，以明确其对变化无穷型的统一性。
取 $G(u)=e^{u^2}$，定义
$$
V_m(n)=\frac1{2\pi i}\int_{(3/4)}
\frac{\Gamma(m+1+u)}{\Gamma(m+1)}
\left(\frac Qn\right)^u e^{u^2}\frac{du}{u}.
\tag{8}
$$
把 $\Lambda_m(1/2+u)G(u)/u$ 的积分从 $\Re u=3/4$ 移到
$-3/4$，仅跨过 $u=0$。完成函数整，gamma 的最右极点
$-m-1$ 也不在该条带内。由 (6)、$G(-u)=G(u)$，得到
$$
\mathcal L_m(1/2)
=\sum_{n\ge1}\frac{a_m(n)}{\sqrt n}V_m(n)
+W_m\sum_{n\ge1}\frac{\bar a_m(n)}{\sqrt n}V_m(n).
\tag{9}
$$
初始线及移换后右半平面上 Dirichlet 级数均绝对收敛；
$e^{u^2}$ 的竖直快速衰减保证移线及求和交换。
如果对偶系数记作 $a_{\bar\chi_m}$，它们正等于 $\bar a_m$。

记 $M=m+1$。对固定 $B>1$，将 (8) 移到 $\Re u=B$，得
$$
|V_m(n)|\le C_B(M/n)^B.
\tag{10}
$$
将其移到 $\Re u=-1/2$，取出 $u=0$ 的留数，则
$$
V_m(n)=1+O((n/M)^{1/2}).
\tag{11}
$$
这里的常数均对 $m$ 一致。
例如在这两条直线上，gamma 的积分表达式给
$|\Gamma(M+\sigma+it)|\le\Gamma(M+\sigma)$，
而固定实移位的 gamma 比为 $O_\sigma(M^\sigma)$；
再积分 $|e^{(\sigma+it)^2}|=e^{\sigma^2-t^2}$ 即可。
$Q$ 是固定常数，已吸收到 $C_B$ 中。

于是 $|V_m(n)|\ll1$ 当 $n\le M$，而 $n>M$ 时可用 (10) 的 $B=2$。
由
$$
\sum_{n\le X}d(n)\le X(1+\log X)
$$
及分部求和，
$$
\sum_{n\le M}\frac{d(n)}{\sqrt n}\ll\sqrt M\log(2M),\qquad
M^2\sum_{n>M}\frac{d(n)}{n^{5/2}}
\ll\sqrt M\log(2M).
$$
代入 (9) 得 (7)。这个证明只给绝对值上界，不给算术分母的上界。

## 3. 非多项式整函数与增长

令
$$
\tau=\frac{\pi_{\mathbb C}}{Nf\,\Omega_E^2}
=\frac1{Nf\,A}>0.
$$
由 (3)、(7)，
$$
|e_m|\le C_1\frac{\tau^m\sqrt{m+1}\log(m+2)}{m!}.
\tag{12}
$$
因此 (2) 在整个复平面绝对收敛。进一步，用
$\sqrt{m+1}\log(m+2)\ll(m+1)^2$，有
$$
\boxed{\quad
\max_{|Z|\le R}|\mathscr D(Z)|
\le C_2\{1+3\tau R+(\tau R)^2\}e^{\tau R}.
\quad}
\tag{13}
$$
所以 $\mathscr D$ 的复增长阶至多为一，指数型至多为 $\tau$。
这里没有证明其准确增长阶或准确指数型。

**命题 2。** $\mathscr D$ 不是多项式，因而超越于 $\mathbb C(Z)$。

**证明。** 固定一个目标素数，例如 $p=13$。
R40 已由已发表反圆分理论得到 $F^-_p(T)\ne0$，不需要 Sha 有限。
固定 theta 笔记又已证明 $F^{\Theta,-}_p=U^-_pF^-_p$，其中 $U^-_p$ 为整单位。
因此可写
$$
F^{\Theta,-}_p(T)=T^rB(T),\qquad B(0)\ne0.
$$
取 $m_n=(p-1)p^n$、$t_n=(1+p)^{m_n}-1$。
$t_n$ 非零且趋于零，故对充分大的 $n$，$B(t_n)\ne0$，从而
$F^{\Theta,-}_p(t_n)\ne0$。
其精确插值式的周期、阶乘和 Euler 因子都非零，所以
$d_{m_n}\ne0$、$e_{m_n}\ne0$，产生无穷多个非零系数。

最后，单值整函数若在 $\mathbb C(Z)$ 上代数，则它在无穷远至多有
有限阶极点（可由代数方程的根界直接看出），所以是多项式。
与刚证结论矛盾。证毕。

此证明利用一个固定 $p$ 的分支非恒零来证明复函数非多项式；
它完全没有把同一事实用作无穷多个 $p$ 的有限性证明。

## 4. 算术目标在新图像上的准确位置

对每个目标 $p$，$f$ 是单位，故中央 theta 笔记的判据变为
$$
e_{p-1}\in p^2\mathbb Z_p,\qquad
e_{p-1}\notin p^4\mathbb Z_p
\Longrightarrow\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}.
\tag{14}
$$
完整的存在性判据是
$$
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\iff\exists n\ge0:\
v_p(e_{(p-1)p^n})+2(p^n-1)<4(n+1).
\tag{15}
$$
注意 (12) 是复上界，而 (14)、(15) 是不同有限处的赋值条件。
有理数可以在实绝对值很小的同时带有很大的分母；不能直接由 (12)
推出任何一个 $p$ 的 (14)。

现在得到固定的非代数形式曲线
$$
\widehat C:\quad Y=\mathscr D(Z)\subset\widehat{\mathbb A^2_{\mathbb Q}}_{(0,0)}.
\tag{16}
$$
$d_0=0$ 已由秩二及解析秩零定理的逆否命题得到，故基点确为 $(0,0)$。
它有全平面整一致化，增长阶至多一，且系数在 $\mathbb Q$。
与此前 $E\times\mathbb P^1$ 中增长阶二的曲线相比，
这里若使用 Herblot Theorem 6.1，相应充分算术门槛为 $\alpha<1/2$：
取任意足够接近一的 $\rho>1$，在闭包维数二、定义域 $\mathbb Q$、
单一 germ 的情形，条件是 $\alpha<1/(2\rho)$。
具体地，一致化 $Z\mapsto[1:Z:\mathscr D(Z)]$ 的 tautological 截面
$(1,Z,\mathscr D(Z))$ 由 (13) 满足这一增长条件，故不是只从某个
坐标函数的非定量延拓推断一致化的阶数。
详细 jet 规范沿用 `herblot-trace-curve-threshold` 笔记。

**尚未证明的输入**是 (16) 的实际有限处 jet 预算，以及假设几乎全部
目标 $p$ 的 Sha 初级部分无限时，该预算会否降到上述门槛以下。
不能把双级数的普通整性、单项的复上界，或只在 $m=p-1$ 处的
有限深度整除，直接替代全部 jet 的条件。
本文没有断言 $\mathscr D$ 为 D-finite，也没有断言它不为 D-finite。

## 来源与证明依赖

- 固定 theta 笔记：导子轨道、$d_m\in K$、公式 (1) 的完整阶乘及 Katz 单位比较；
  [R40](../results/R40-anticyclotomic-second-coefficient-and-full-selmer.md)：
  完整 Selmer 判据与反圆分分支非恒零。
- H. Iwaniec、E. Kowalski，*Analytic Number Theory*，AMS Colloquium
  Publications 53 (2004)，Chapter 5，Theorem 5.3 与 Proposition 5.4，
  [出版记录](https://doi.org/10.1090/coll/053)。
  本文 (8)–(11) 已写出所需特殊情形的移线证明与统一常数，不把随无穷型
  变化的隐含常数视为固定。
- J. B. Conrey、N. C. Snaith，*On the orthogonal symmetry of L-functions of a
  family of Hecke Grössencharacters*，§1.1，
  [作者原文](https://arxiv.org/pdf/1212.2681)：Hecke 角度家族的解析规范及函数方程背景。
  该文具体研究 $\mathbb Q(\sqrt{-7})$；本文不使用其特定家族的均值或非零结果。
- M. Herblot，*Algebraic points on meromorphic curves*，Theorem 6.1，
  [作者原文](https://webusers.imj-prg.fr/~mathilde.herblot/publi/SL.pdf)。
  本文只代入已经实现的定义域、闭包维数及复增长，不宣称其算术假设已满足。
