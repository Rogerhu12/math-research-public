# R267 第二附录：Blaschke 块收缩强单位与线性次数逆下型

日期：2026-11-13（UTC）。作者：normal_states；Astra-ISP-1cf8c51d 复核。

状态：以下实际收缩乘积、非零强极限、同一组收缩强单位以及线性次数逆下界均已证明，属于中间结论。各块的逆减去恒等未必增生；本稿直接使用并完整验证其逆为收缩。未声称新正则器已为慢符号的有界右倍数，也未给任意见证的 R244 聚合界。

## 1. 有限纯块的 Blaschke 收缩

在 $q\ge4$ 个位的纯有限块上，令
$$
D_q=\sum_{j=1}^qE_j,\qquad
T_q=\frac{2D_q}{q+2},\qquad a=\frac34.
$$
[R267 第一附录](R267-appendix-summable-vacuum-drift-and-super-square-root-inverse-growth.md) 的逐层 Schur 界给
$$
\|D_q\|\le\frac{q+1}{2},\qquad
\|T_q\|\le\frac{q+1}{q+2}<1.
\tag{1.1}
$$
定义
$$
R_q^0=(aI+T_q)(I+aT_q)^{-1},\qquad
U_q^0=(R_q^0)^{-1}=(I+aT_q)(aI+T_q)^{-1}.
\tag{1.2}
$$
$T_q$ 幂零，两个分母均可逆。直接相乘有
$$
\boxed{
I-(R_q^0)^*R_q^0
=(1-a^2)(I+aT_q^*)^{-1}(I-T_q^*T_q)(I+aT_q)^{-1}\ge0.
}
\tag{1.3}
$$
所以 $R_q^0$ 是收缩，等价地
$$
\|U_q^0x\|\ge\|x\|\qquad\text{对全部块向量 }x.
\tag{1.4}
$$
不据此声称 $U_q^0-I$ 增生；收缩与这种更强的预解式性质必须分清。

还准确有
$$
\boxed{
U_q^0=aI+(1-a^2)(aI+T_q)^{-1}.
}
\tag{1.5}
$$

## 2. 真空源的均值和方差仍为可和规模

令 $\Omega=\Omega_+^{\otimes q}$、$g_q=U_q^0\Omega$、
$\alpha_q=\langle g_q,\Omega\rangle$。由有限维积分，
$$
g_q=a\Omega+(1-a^2)\int_0^\infty e^{-as}v_q(s)\,ds,
$$
$$
v_q(s)=e^{-sT_q}\Omega
=\bigotimes_{j=1}^q
\left(\left(1-\frac{s}{q+2}\right)\Omega_+
+\frac{s}{q+2}\chi\right).
\tag{2.1}
$$
记
$$
h_q(s)=\langle v_q(s),\Omega\rangle
=\left(1-\frac{s}{q+2}\right)^q.
$$

以下三个估计在 R267 第一附录中已逐式证明，这里保留其完整量词：
$$
\|v_q(s)\|\le e^{s/2}\qquad(s\ge0),
\tag{2.2}
$$
而对 $0\le s\le(q+2)/4$，
$$
\|v_q(s)-h_q(s)\Omega\|
\le\frac{s}{\sqrt q}e^{-3s/8},
$$
$$
|h_q(s)-e^{-s}|
\le\frac{2s+s^2}{q}e^{-2s/3}.
\tag{2.3}
$$
全局 (2.2) 来自
$1-2x+2x^2\le e^x$，$x\ge0$；
其证明使用 $e^x+2-4x\ge6-4\log4>0$。所以这里的积分尾由
$e^{-(a-1/2)s}=e^{-s/4}$ 支配，不存在大 $s$ 失控。

由于
$$
a+\frac{1-a^2}{a+1}=1,
$$
将 (2.3) 代入 (2.1)，并在 $(q+2)/4$ 分段，可取
$$
\boxed{
|\alpha_q-1|\le\frac{12}{q},\qquad
\|g_q-\alpha_q\Omega\|\le\frac6{\sqrt q},\qquad
\|g_q-\Omega\|\le\frac{20}{\sqrt q}.
}
\tag{2.4}
$$
例如均值的小区间误差不超过
$$
\frac{7}{16q}\int_0^\infty(2s+s^2)e^{-17s/12}ds<\frac1q,
$$
其尾至多 $2e^{-(q+2)/16}<11/q$。
正交部分的小区间不超过
$\frac{7}{16\sqrt q}\int_0^\infty s e^{-9s/8}ds$，
尾至多 $\frac72e^{-(q+2)/16}$；两者之和小于 $6/\sqrt q$。

此外由 (2.2)，
$$
\boxed{
\|g_q\|\le a+\frac{1-a^2}{a-1/2}=\frac52.
}
\tag{2.5}
$$
(1.4) 保证 $\|g_q\|\ge1$，故
$$
\boxed{
0\le\|g_q\|^2-1
=2(\alpha_q-1)+\|g_q-\Omega\|^2
\le\frac{424}{q}.
}
\tag{2.6}
$$
$\alpha_q$ 为实数，但本稿不要求 $\alpha_q-1$ 非负；后面的乘积引理会支付其绝对可和性。

## 3. 反向全块上的线性指数下界

令 $\chi_{[q]}=\prod_{j=1}^q\chi_j$。每位反向矩为
$\langle E\chi,\chi\rangle=-1/2$，于是 (1.5) 给正积分
$$
\boxed{
\langle U_q^0\chi_{[q]},\chi_{[q]}\rangle
=a+(1-a^2)\int_0^\infty
e^{-as}\left(1+\frac{s}{q+2}\right)^qds.
}
\tag{3.1}
$$
令
$$
s_0=\frac{q+2}{3},\qquad
\kappa=\log\frac43-\frac14>0.
$$
对整个长度1的区间 $s\in[s_0,s_0+1]$，
$$
e^{-as}\left(1+\frac{s}{q+2}\right)^q
\ge
\exp\left(q\log\frac43-\frac{q+2}{4}-\frac34\right)
=e^{\kappa q-5/4}.
$$
因此
$$
\boxed{
\langle U_q^0\chi_{[q]},\chi_{[q]}\rangle
\ge c_0e^{\kappa q},\qquad
c_0=\frac7{16}e^{-5/4}>0.
}
\tag{3.2}
$$
该下界使用了一整段积分区间，未把单点值当作积分下界。数值上
$\kappa\approx0.03768207245$；精确式用于证明。初等界
$\log(1+x)>x-x^2/2$ 在 $x=1/3$ 给
$\kappa>1/36$，足以支付后面所有固定常数。

## 4. 真实有限 Walsh 提升及收缩的正确缩放

将第2节的纯 $g_q$ 放在原模型的有限位块 $F$ 上，$q=|F|$、$m=\min F$，
写
$$
g_F=\sum_{J\subseteq F}c_J\chi_J,\qquad
X_{g_F}=\sum_{J\subseteq F}c_JV_J\in\mathcal A.
$$
纯有限算子由其真空列唯一确定，所以
$$
U_F^0=\sum_{J\subseteq F}c_JV_J^0
=(I+aT_F)(aI+T_F)^{-1},
\qquad
T_F=\frac2{q+2}\sum_{j\in F}E_j.
\tag{4.1}
$$

与 R267 第一附录相同的实际逐位望远镜，结合
$\sum|c_J|\le2^{q/2}\|g_F\|\le\frac52\,2^{q/2}$，给
$$
\boxed{
\|X_{g_F}-U_F^0\|\le
32q9^q e^{-77016^m}
=:\varepsilon(F).
}
\tag{4.2}
$$
取位置使 $\varepsilon(F)<1/2$。因为 $\|(U_F^0)^{-1}\|\le1$，
通常有界扰动逆公式给
$$
X_{g_F}^{-1}\in B(H),\qquad
\|X_{g_F}^{-1}\|\le\frac1{1-\varepsilon(F)}.
$$
所以应定义
$$
\boxed{
\widetilde U_F=\frac{X_{g_F}}{1-\varepsilon(F)},\qquad
\widetilde R_F=\widetilde U_F^{-1}
=(1-\varepsilon(F))X_{g_F}^{-1}.
}
\tag{4.3}
$$
于是 $\|\widetilde R_F\|\le1$。这些是实际有界交换子。

本节使用的是正标量缩放，不是向逆词加标量后擅称增生。
$\widetilde U_F-I$ 无须增生；R244 只需要后面验证的收缩强单位。

准确真空源为
$$
\widetilde g_F=\widetilde U_F1
=\frac{g_F}{1-\varepsilon(F)},
$$
仍只依赖 $F$。若 $q\ge4096$ 且 $\varepsilon(F)\le q^{-2}$，由第2节可安全取
$$
\boxed{
|\langle\widetilde g_F,1\rangle-1|\le\frac{32}{q},
\qquad
0\le\|\widetilde g_F\|^2-1\le\frac{600}{q}.
}
\tag{4.4}
$$
第一均值为正实数；第二下界也直接来自
$\widetilde R_F\widetilde g_F=1$ 及收缩性。

## 5. 物理块选择及可和漂移乘积

可使用 R267 第一附录同样的大小：
$$
q_\nu=4096+
\left\lceil(\nu+2)(\log(\nu+2))^{3/2}\right\rceil,
\qquad
Q_n=\sum_{\nu=n}^{2n}q_\nu.
$$
已有
$$
\sum_\nu q_\nu^{-1}<3,\qquad
Q_n\asymp n^2(\log n)^{3/2},\qquad
Q_{n+1}/Q_n\longrightarrow1.
\tag{5.1}
$$
递归把连续块 $F_\nu=[m_\nu,m_\nu+q_\nu)$ 放在互不交的更高位置，要求
$$
\varepsilon(F_\nu)=32q_\nu9^{q_\nu}e^{-77016^{m_\nu}}
\le2^{-\nu}q_\nu^{-2},
\tag{5.2}
$$
$$
8Q_\nu6^{Q_\nu-1}e^{-77016^{m_\nu}}
\le2^{-\nu}e^{-1000}.
\tag{5.3}
$$
每一步均可行；右侧全部事先已知。原 carry 并未被忽略。

记各块的 $\widetilde U_\nu,\widetilde R_\nu,\widetilde g_\nu$ 如第4节，并定义
$$
P_n=\prod_{\nu=1}^n\widetilde R_\nu,\qquad
U_n=\prod_{\nu=1}^n\widetilde U_\nu,\qquad
g_n=U_n1.
$$
因为有限 Walsh 符号支撑于互不交位块，
$$
\boxed{g_n=\prod_{\nu=1}^n\widetilde g_\nu}
\tag{5.4}
$$
为准确的普通 Walsh 块乘积。常数项可以不同于1，不影响位独立性。

令
$$
A_\nu=\|\widetilde g_\nu\|^2,\qquad
b_\nu=\langle\widetilde g_\nu,1\rangle.
$$
由 (4.4)，
$$
A_\nu\ge1,\quad b_\nu>0,\quad
\sum_\nu(A_\nu-1)<\infty,\quad
\sum_\nu|b_\nu-1|<\infty.
\tag{5.5}
$$
所以对尾真空列 $g_{n,m}=\prod_{\nu=n+1}^m\widetilde g_\nu$，
$$
\|g_{n,m}-1\|^2
=\prod_{\nu=n+1}^mA_\nu+1
-2\prod_{\nu=n+1}^mb_\nu
\longrightarrow0
\tag{5.6}
$$
一致于 $m>n$。两个尾积分别趋于1，分别由 (5.5) 的两种绝对可和性控制。这里不再用“每个均值至少1”的旧特例。

因此 $g_n$ 在 $H$ 中收敛，记极限为 $g$，且
$$
\boxed{
1\le\|g\|\le\exp\!\left(300\sum_\nu q_\nu^{-1}\right)
<e^{900}<e^{1000}.
}
\tag{5.7}
$$
前缀和尾的正交张量分离给
$\|g_m-g_n\|=\|g_n\|\|g_{n,m}-1\|$，从而上述确为 $L^2$ 收敛。

## 6. 非零实际极限、同一组强单位和逆核心

令 $Q_{n,m}=\prod_{\nu=n+1}^m\widetilde R_\nu$。
它是收缩，且 $Q_{n,m}g_{n,m}=1$，故
$$
\|(Q_{n,m}-I)1\|\le\|g_{n,m}-1\|\longrightarrow0.
\tag{6.1}
$$
交换性、统一收缩界及 $1$ 的循环性把此结论延伸到整个 $H$。
于是 $P_n$ 强收敛到收缩 $P\in\mathfrak C$。

由 $P_ng_n=1$、$g_n\to g$，得到 $Pg=1$，故 $P\ne0$。
固定 $n$ 时，$P_mU_n=Q_{n,m}$；让 $m\to\infty$ 再让 $n\to\infty$，得到
$$
\boxed{
\|PU_n\|\le1,\qquad PU_n\longrightarrow I\quad\mathrm{SOT}.
}
\tag{6.2}
$$
这是原来同一组有界逆词 $U_n$，并未假设它们自身一致有界。

因此 $P$ 在全 $H$ 及每个有限放大实际不变旗子商中都单射、稠密像。
[R244 聚合附录](R244-appendix-aggregate-inverse-graph-moment-criterion-and-cyclic-factor.md) 适用，给循环 $g=P^{-1}1$ 和准确最小闭图
$$
\boxed{
G=P^{-1}=X_g,\qquad
G\chi_J=V_Jg\quad(J\text{ 有限}).
}
\tag{6.3}
$$
全部有限 Walsh 柱为 $G$ 的图核心。以下逆测试因而是实际算子的真实域运算。

## 7. 保留全部 carry 的线性次数下型

取
$$
J_n=\bigcup_{\nu=n}^{2n}F_\nu,\qquad x_n=\chi_{J_n},
\qquad\|x_n\|=1,\quad |J_n|=Q_n.
$$
由 (6.3)，$Gx_n=V_{J_n}g$。

先只对纯比较算子 $V_{J_n}^0$ 作张量计算。
未选块的 $\|\widetilde g_\nu\|\ge1$；选中块内，由纯有限代数交换性，
$$
V_{F_\nu}^0\widetilde g_\nu
=\frac{U_{F_\nu}^0\chi_{F_\nu}}
{1-\varepsilon(F_\nu)}.
$$
利用 (3.2)，
$$
\boxed{
\|V_{J_n}^0g\|
\ge c_0^{\,n+1}e^{\kappa Q_n}.
}
\tag{7.1}
$$

实际比较由 (5.3)、(5.7) 直接给
$$
\|Gx_n-V_{J_n}^0g\|
\le8Q_n6^{Q_n-1}e^{-77016^{m_n}}\|g\|
\le2^{-n}.
\tag{7.2}
$$
所以
$$
\boxed{
\|Gx_n\|
\ge\frac12c_0^{\,n+1}e^{\kappa Q_n}.
}
\tag{7.3}
$$
$q_\nu\ge4096$ 及第3节的固定常数保证主项远大于误差；也可以仅保留充分大 $n$，不改变后面结论。

由于 $(n+1)/Q_n\to0$，
$$
\boxed{
\liminf_{n\to\infty}\frac{\log\|Gx_n\|}{Q_n}\ge\kappa
=\log\frac43-\frac14.
}
\tag{7.4}
$$
若像第一附录一样在有限柱上定义次数成本 $M_P(q)$，其单调性及
$Q_{n+1}/Q_n\to1$ 还给
$$
\liminf_{q\to\infty}\frac{\log M_P(q)}q\ge\kappa,
\tag{7.5}
$$
允许 $M_P(q)=\infty$。未由此断言任一无限维固定次数层都包含在逆域中。

这里没有在实际压缩上使用纯代数同态。实际运算只有
$Gx_n=V_{J_n}g$；纯块乘积用于右端的比较项，而 (7.2) 支付全部真实误差。
高窗口使最小测试位随 $n$ 增大，避免固定早期 carry 乘不断增长的测试范数。

## 8. 小正线性指数域及全部次线性域的像障碍

令
$$
H_\sigma=\operatorname{Dom}e^{\sigma\mathcal N}.
$$
若对某个 $0<\sigma<\kappa$ 有 $H_\sigma\subseteq\operatorname{Ran}P$，
闭图定理将给
$$
\|Gu\|\le C_\sigma\|e^{\sigma\mathcal N}u\|.
$$
代入 $x_n$ 与 (7.3) 矛盾。因此
$$
\boxed{
H_\sigma\not\subseteq\operatorname{Ran}P
\qquad(0<\sigma<\kappa).
}
\tag{8.1}
$$
端点 $\sigma=\kappa$ 不由本下界决定。

还能保留一个共同向量量词。令
$$
\mathcal E_{<1}=
\bigcap_{\substack{0<\beta<1\\t>0}}
\operatorname{Dom}e^{t(1+\mathcal N)^\beta}.
$$
取递增可数余终子族
$\beta_k=1-1/(k+1)$、$t_k=k$，得到自然 Fréchet 拓扑。
若 $\mathcal E_{<1}\subseteq\operatorname{Ran}P$，闭图定理使
$G:\mathcal E_{<1}\to H$ 连续，从而由某个固定 $\beta<1,t>0$ 的图范数控制。
但
$$
t(1+Q_n)^\beta-\kappa Q_n+O(n)\longrightarrow-\infty,
$$
再次与 (7.3) 矛盾。于是
$$
\boxed{
\exists f\in\mathcal E_{<1},\qquad
f\notin\operatorname{Ran}P.
}
\tag{8.2}
$$
这是同一个向量具有全部次线性拉伸次数矩，仍没有 $P$ 原像。

R261 的全部非零规范一阶正预解式积包含每个正平方根域，所以本稿 $P$ 严格不属于该范围。更具体地，R263 的
$\sigma_*=1/(60e^2)$ 小于本稿 $\kappa$，故
$$
H_{\sigma_*}\not\subseteq\operatorname{Ran}P.
$$
因此不能再通过“$H_{\sigma_*}$ 整体包含在该 $P$ 的像中”把 R263 的分母障碍套到本构造；这里该前提实际为假。

## 9. 仍须解决的正态接口

$P$ 已具备 R244 聚合等价的全部结构前提：实际交换性、$Pg=1$、
循环第一因子、真实逆核心和一致收缩的同组强单位。
新逆增长可达到线性次数指数，而非旧一阶类的平方根零型。

不过，大逆范数只发生在已指定的方向上。它不自动控制一个假想正常湮灭者的全部矩，尤其不自动证明
$$
|\phi(X_u)|\le C_\phi\|P^{-1}u\|
$$
对每个有限柱 $u$ 同时成立。

本稿也没有建立 $P=SR$ 的有界因式，或给 R253 的 $q_m$ 非消失下界。
“旧分母排除条件不适用”只表示其特定前提已被打破，不能改写成新分母存在。
接下来应利用见证本身的矩方程选块、零点或参数，支付完整聚合 Gram 控制；一般正常正湮灭者及普通 ISP 仍开放。
