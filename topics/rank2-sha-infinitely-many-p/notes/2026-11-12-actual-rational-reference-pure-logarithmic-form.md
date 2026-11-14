# 实际同次数参考微分的纯对数分解与零迹证书

日期：2026-11-12。状态：本文的固定函数、规范、留数分解、零迹及
实际解析行的代数改写均已证明。没有把解析行直接认定为某个
Coleman 积分或固定单位的普通 $p$ 进对数。

## 1. 固定原曲线与实际参考商

承接[全 jet 与归一解析行](2026-11-12-inert-fixed-isogeny-jets-and-normalized-rows.md)，
取

$$
E_0:y^2=x^3-x,\quad \omega=dx/(2y),\quad D=d/\omega,
\quad T=(0,0),\quad \alpha=4-i,\quad N=17.
$$

令 $X=x^2$，实际商为

$$
R_*=A/\theta_T(\alpha z)=Q(X)/U(X),
$$

$$
Q(X)=X^3+\frac35X^2-\frac15X+\frac15,
$$

$$
U(X)=X^4+(12-20i)X^3+(-10+28i)X^2
                         +(-20-12i)X+1+4i.                  \tag{1.1}
$$

它在 $O$ 为 $z^4+O(z^8)$，极点正好是
$\mathcal D^\circ=[\alpha]^{-1}(T)\setminus\{T\}$ 的十六个简单点。
所有这些点都形如 $P=T+S$，$0\ne S\in E_0[\alpha]$。

记 $\rho_P=\operatorname{res}_P(R_*\omega)$。
若 $V_P=x(P)^{-2}$，原来的四次多项式为
$u_\alpha(V)=V^4U(V^{-1})$，则

$$
\rho_P=-\frac{x(P)^3q(V_P)}{4y(P)u_\alpha'(V_P)},\qquad
q(V)=V+\frac35V^2-\frac15V^3+\frac15V^4.                    \tag{1.2}
$$

这是 $D(x^{-2})=-4y/x^3$ 给出的准确留数。
全局留数定理给 $\sum_P\rho_P=0$。又
$\rho_{iP}=i\rho_P$，因为 $[i]^*(R_*\omega)=iR_*\omega$。

## 2. 正确的 $T$ 锚点与完全代数的 Miller 规范

对每个 $P=T+S\in\mathcal D^\circ$，取唯一规范

$$
\operatorname{div}g_P=17(P)-17(T),\qquad g_P(O)=1.
\tag{2.1}
$$

这样的 $g_P\in L(E_0)^\times$ 存在，$L=\mathbb Q(i,E_0[17])$，
因为 $17(P-T)=0$。不能把这里的 $T$ 改为 $O$ 而仍使用 $17$：
$P$ 通常有 $34$ 阶。

此规范有无周期的明确构造。令 $f_{17,S}$ 为 Miller 函数，

$$
\operatorname{div} f_{17,S}=17(S)-17(O),\qquad
g_P(Z)=\frac{f_{17,S}(Z-T)}{f_{17,S}(-T)}.                  \tag{2.2}
$$

分母非零。由 $1\to2\to4\to8\to16\to17$ 的加法链，使用

$$
f_{m+n,S}=f_{m,S}f_{n,S}\,
          \frac{\ell_{[m]S,[n]S}}{v_{[m+n]S}},\qquad f_{1,S}=1,
$$

即可逐项构造它；最后一步 $[16]S=-S$ 使用竖线 $x-x(S)$。
所有中间函数的常数都在 (2.2) 中消去。

在任意目标惰性 $p\ge7$ 处，所有涉及的 $2$、$17$ 挠点都有可分
良好约化且仍互异。Miller 的线及竖线在 $-T$ 的零、极点不会出现：
这些零极点的 $17$ 主部分不能等于非零 $2$ 挠点。
所以 $g_P$ 在 $O$ 的正式盘是常数项 $1$ 的整单位。

## 3. 分解的整体加法常数由规范准确确定

对 $P\in\mathcal D^\circ$，定义固定有理函数

$$
B_P(Z)=\frac{y(Z)+y(P)}{x(Z)-x(P)}-\frac{y(Z)}{x(Z)}.
\tag{3.1}
$$

$B_P\omega$ 仅在 $P,T$ 有简单极点，留数分别为 $1,-1$，
而 $B_P(O)=0$。在 $-P$，第一项的可去奇点应先约去。
因此按极点、留数和 $O$ 处值比较，准确有

$$
R_* =\sum_P\rho_P B_P.                                   \tag{3.2}
$$

令

$$
U_P=\zeta(P)-\bar P/\mathcal A.
$$

这个量是代数数；且由于 $[\alpha]P=T$、$U_T=0$，sigma 除法给

$$
U_P=-\frac1{17}D\log\Psi_\alpha(P),\qquad
\Psi_\alpha(z)=\sigma(\alpha z)/\sigma(z)^{17}.             \tag{3.3}
$$

为精确核查加法常数，(2.1) 的函数也可写为

$$
g_P(z)=
 \left(\frac{\sigma(z-P)\sigma(-T)}
             {\sigma(z-T)\sigma(-P)}\right)^{17}
 \exp\!\left(\frac{17(\bar P-\bar T)z}{\mathcal A}\right).
\tag{3.4}
$$

它是椭圆函数：$17(P-T)\in\Gamma$ 使平移乘子成为 $1$；
除子和 $O$ 处值与 (2.1) 相同，故它与 Miller 构造完全相等。
由 zeta 加法公式

$$
\zeta(z-P)-\zeta(z-T)
 =-\zeta(P)+\zeta(T)+B_P(z)
$$

逐项求导，得

$$
\boxed{\quad B_P\omega=\frac1{17}d\log g_P+U_P\omega.\quad}
\tag{3.5}
$$

所以

$$
R_*\omega=c\omega+\frac1{17}\sum_P\rho_Pd\log g_P,
\qquad c=\sum_P\rho_PU_P.                                 \tag{3.6}
$$

这一步并非只由留数确定：留数只确定模 $K\omega$ 的类；
(3.4)–(3.5) 准确固定了可能剩下的 holomorphic 项。

## 4. 留数定理把 $c$ 化成固定同源核的平均

考虑原曲线上的有理微分 $R_*d\log\Psi_\alpha$。
它在 $P\in\mathcal D^\circ$ 的留数为
$\rho_PD\log\Psi_\alpha(P)$。在非零 $Q\in E_0[\alpha]$
处，$\Psi_\alpha$ 有一阶零点，故留数为 $R_*(Q)$。
在 $O$，$d\log\Psi_\alpha$ 的简单极点乘以
$R_*=z^4+O(z^8)$ 后没有留数；其余地方无极点。

全局留数定理与 (3.3) 于是给

$$
\boxed{\quad c=\frac1{17}\sum_{Q\in E_0[\alpha]}R_*(Q).
\quad}                                                       \tag{4.1}
$$

其中 $Q=O$ 的项为 $0$。
这也是十七维 theta Fourier 展开中 $f_0=\theta(\alpha z)$
的系数 $a_0$：在 $Q\in E_0[\alpha]$ 上，
$f_S(Q)/f_0(Q)=e_\alpha(Q,S)$，对 $Q$ 求平均后，
字符正交性仅保留 $S=0$ 项。这正是
[固定十七点基的 Fourier 逆式](2026-11-12-inert-seventeen-theta-basis-and-divided-jet.md)
(11) 的 $S=0$ 情形。下面对实际 $Q/U$ 证明这个平均恰为零。

## 5. 一个四次商代数中的精确零迹

固定 sigma 除法多项式为

$$
\boxed{\quad
\Psi_\alpha(x)=K(x^2),\qquad
K(X)=(4-i)X^4+(-12+20i)X^3+(28+10i)X^2
                           +(-20-12i)X-i.
\quad}                                                       \tag{5.1}
$$

这里 $K$ 的四个根正好参数化非零 $E_0[\alpha]$ 点的四个
$\mu_4$ 轨道，每个轨道有四个点。
一个简便的符号交叉核验是 $u_\alpha(V)=iK(V)$，这里仅把两个
四次多项式代入同一个形式变量 $V$；$K$ 在 (5.1) 中的实际输入是
$X=x^2$。不要将这个恒等式误写为 $U=iK$：
$U(X)=X^4u_\alpha(X^{-1})$ 是反序多项式。

(5.1) 的有限验证之所以充分，是因为 $\Psi_\alpha$ 仅在 $O$
有十六阶极点且在 $i$ 下不变，故必为 $x^2$ 的四次多项式。
其首项为 $\alpha x^8$。由 $x''=6x^2-2$ 求出

$$
z^2x=1+\frac{z^4}{5}+\frac{z^8}{75}
               +\frac{2z^{12}}{4875}+\frac{z^{16}}{82875}+O(z^{20}),
$$

再使用 $\log(\sigma/z)''=-(x-z^{-2})$，比较
$\sigma(\alpha z)/\sigma(z)^{17}$ 的五个系数即得 (5.1)。

在 $K[X]/(K(X))$ 中，$U$ 可逆，且

$$
\frac QU\equiv H(X):=
\frac{(7+28i)X^3+(-145-70i)X^2
                  +(-119+136i)X+17-102i}{2560}.             \tag{5.2}
$$

一个可直接乘开核查的证书为

$$
UH-Q=K\cdot
\frac{7iX^3+(138+87i)X^2+(-164+9i)X+34-87i}{2560}.
\tag{5.3}
$$

这个四维商代数的 Newton 幂迹为

$$
\operatorname{Tr}(1)=4,\quad
\operatorname{Tr}(X)=4-4i,\quad
\operatorname{Tr}(X^2)=-12-40i,\quad
\operatorname{Tr}(X^3)=-236-92i.
\tag{5.4}
$$

代入 (5.2) 给 $\operatorname{Tr}(Q/U)=0$。因此 (4.1) 得

$$
\boxed{\quad a_0=c=0,\qquad
 R_*\omega=\frac1{17}\sum_{P\in\mathcal D^\circ}
                         \rho_Pd\log g_P.
\quad}                                                       \tag{5.5}
$$

这是实际微分的纯对数分解，所有函数与系数都固定在 $p$ 变化之前。
可复核脚本为
[check-inert-rational-reference-trace.py](../scripts/check-inert-rational-reference-trace.py)；
它只使用有理高斯数精确算术，不用数值近似或数据库。

## 6. 对实际归一解析行的准确改写及其限制

对一个在 $O$ 正则、在固定正式盘整的有理函数 $R$，令

$$
\ell_p(R)=\left.\frac{d}{du}
       \frac{J_{\theta(\alpha z)R,p}(u)}{J_{\theta(\alpha z),p}(u)}
       \right|_{u=0}.
\tag{6.1}
$$

本篇使用的各 $D\log g_P$ 在所需盘满足该定义的解析估计。
它是线性的，且 $\ell_p(1)=0$。由 (5.5) 得到的是一个真正的
全精度恒等式

$$
\boxed{\quad
J_{A,p}'(0)=\frac1{17}\sum_P\rho_P\,\ell_p(D\log g_P).
\quad}                                                       \tag{6.2}
$$

注意这里的 $D\log g_P$ 是有理函数；没有先假定
$\ell_p(D\log g_P)$ 是 $g_P$ 在某个点处的普通对数。

若另外给定两个固定代数点 $Q_0,Q_1$，避开上述除子，
则同一微分的 Coleman 积分确实可以由 (5.5) 写成

$$
\int_{Q_0}^{Q_1}R_*\omega
=\frac1{17}\sum_P\rho_P
       \log_p\!\left(\frac{g_P(Q_1)}{g_P(Q_0)}\right).
\tag{6.3}
$$

这是由 $\int d\log g=\log g$ 得到的另一条等式。
要把 (6.2) 与 (6.3) 相等，仍须实际指定端点、切向或周期泛函并
证明比较。维数有限、极点都是挠点或参考已除去，都不自动给出这种等式。
特别地，$R_*\omega$ 在 $[-1]$ 下为负，而 $O$ 与所有二挠点都
被 $[-1]$ 固定；在没有极点的二挠点间，其普通 Coleman 积分为零。
这已被本实际截面排除为所需比较：在 $p=7$，
$\beta_8=97/60\equiv5$，且 $17\cdot7c\equiv5\pmod7$，
所以已证首层式给 $J_{A,7}'(0)/7\equiv1\pmod7$。
这一步不需要借助另一个五次模型。

几何上，模数支撑在挠点的广义 Jacobian 在同源意义下是
原椭圆曲线与一个环面的乘积；(5.5) 在这里还明确消除了实际微分的
holomorphic 项。所以后续如能证明正确比较，所需候选已缩成上述
固定对数函数，而不用再次引入未知的椭圆积分项。
