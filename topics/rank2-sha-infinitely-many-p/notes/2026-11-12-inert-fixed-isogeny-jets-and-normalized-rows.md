# 惰性固定同源的全 jet 与共同参考除去后的解析行

日期：2026-11-12。状态：本文的函数恒等式、整性、解析行、首层比较及
五次模型的全精度校准均已证明。尚未证明实际十七次行的中心导数在
无穷多个惰性素数非零。

本文接续[十七维 theta 基与除 $p$ jet](2026-11-12-inert-seventeen-theta-basis-and-divided-jet.md)，
保留 theta 本身的 Bell 交叉项。选择与目标同次数的
$\theta_T((4-i)z)$ 作参考，实际商已经是原椭圆曲线上的固定有理函数，
不必先引入四次或十七次根覆盖。解析变换后再除去共同参考，
不使用“函数乘积的 Mellin 变换等于两个 Mellin 变换的乘积”。

## 1. 固定同源的准确全 jet 恒等式

沿用

$$
E_0:y^2=x^3-x,\qquad dz=dx/(2y),\qquad T=(0,0),\qquad
\theta(z)=\theta_T(z),\quad \theta(0)=1.
$$

置 $\alpha=4-i$、$a=\bar\alpha=4+i$、$N=17$，
$S\in E_0[a]$、$R=T+S$。记

$$
\varphi_R(z)=\frac{\sigma(R+z)}{\sigma(R)}
             \exp(-\bar Rz/\mathcal A),\qquad
h_{a,R}(z)=\frac{\Psi_a(R+z)}{\Psi_a(R)},\qquad
\Psi_a(z)=\frac{\sigma(az)}{\sigma(z)^N}.
\tag{1.1}
$$

比值 $h_{a,R}$ 是一个固定有理函数在固定挠点的完整展开，
其常数项为 $1$。任何一致选择的 $\Psi_a$ 常数规范都在此比值中消失。
因为 $[a]R=T$，有

$$
\boxed{\quad
 \varphi_R(z)^N=\frac{\theta(az)}{h_{a,R}(z)}.
 \quad}                                                       \tag{1.2}
$$

**证明。** 先用 sigma 除法的定义展开右边。若所选复代表满足
$aR=T+\lambda$，则准周期公式中的额外指数为

$$
 a\eta_\lambda+\frac{a\bar T-N\bar R}{\mathcal A}=0,
 \qquad \eta_\lambda=\bar\lambda/\mathcal A.
$$

因此代表元引入的指数准确相消，常数项又都为 $1$，得到 (1.2)。
这也说明不能遗漏 $\exp(-\bar Rz/\mathcal A)$。$\square$

令前文的 $f_S(z)=\varphi_R(\alpha z)$，则

$$
 f_S(z)=\theta(Nz)^{1/N}h_{a,R}(\alpha z)^{-1/N}.             \tag{1.3}
$$

所有根都取常数项 $1$ 的唯一正式根。特别地，对 $S=0$，
$f_0(z)=\theta(\alpha z)$。两式相除给

$$
 r_S(z):=\frac{f_S(z)}{f_0(z)},\qquad
 r_S(z)^N=\frac{h_{a,T}(\alpha z)}{h_{a,R}(\alpha z)}.
\tag{1.4}
$$

这里 $r_S$ 本身已经是 $L(E_0)$ 中的有理函数，
$L=\mathbb Q(i,E_0[17])$：$f_S$ 与 $f_0$ 是同一个次数 $17$
线丛的截面，自动因子完全相同。其极点至多为

$$
\mathcal D=[\alpha]^{-1}(T),
\tag{1.5}
$$

的十七个简单点，且 $r_S(O)=1$。从 (1.4) 取根不是需要另选的
覆盖或分支；它恢复的是这个已经有理、常数项为 $1$ 的商。

## 2. 实际截面的参考商只在原曲线上

设 $V=x^{-2}$，沿用已经精确认证的

$$
q(V)=V+\frac35V^2-\frac15V^3+\frac15V^4,
$$

$$
u_\alpha(V)=1+(12-20i)V+(-10+28i)V^2
                  +(-20-12i)V^3+(1+4i)V^4.
$$

则

$$
A(z)=\theta(z)^{17}q(V),\qquad
f_0(z)=\theta(\alpha z)=\theta(z)^{17}u_\alpha(V),
$$

$$
\boxed{\quad A(z)=f_0(z)R_*(z),\qquad
 R_*:=\frac{q(x^{-2})}{u_\alpha(x^{-2})}
       =\sum_S a_Sr_S\in K(E_0),\quad K=\mathbb Q(i).
 \quad}                                                       \tag{2.1}
$$

系数 $a_S$ 是十七维 Fourier 逆变换给出的固定代数数，并且
$\sum_Sa_S=0$。商 $R_*$ 在 $O$ 的展开为 $z^4+O(z^8)$。
在 $T$ 处，分子截面 $A$ 与 $f_0$ 都有一阶零点，故商无极点；
其余十六个 $[\alpha]^{-1}T$ 点是实际简单极点。

最后一个断言也可从已证明的乘积

$$
A=\theta(z)\theta(2z)\sigma(z)^2
      \sigma((2+i)z)\sigma((2-i)z)/5
$$

核实：除 $T$ 外，其零点的阶只含 $2,5$，而
$[\alpha]^{-1}T\setminus\{T\}$ 的点有非零 $17$ 主部分。
故两者不相交。

这项同次数参考选择与
[四次参考覆盖](2026-11-12-reference-cover-class-and-exact-kernel.md)
并不矛盾。两种参考的商分别为 $A/\theta(\alpha z)$ 和
$A/\theta(2z)^{17/4}$；它们的代数性对象不同。

## 3. 所有目标惰性素数的局部整性与解析半径

以下 $p\ge7$、$p\equiv3\pmod4$。取 $L$ 中的一个 $p$ 进位，
以 $\mathcal O$ 表示其整数环，赋值规范为 $v_p(p)=1$。
这些 $p$ 不等于 $2,5,17$。
又因曲线在 $p$ 处良好且 $17$ 素于 $p$，$17$ 挠点表示在 $p$ 处
未分歧，故 $L/\mathbb Q$ 在这些 $p$ 未分歧。于是本篇所有系数的
赋值为整数，下面 Gauss 估计中的向上取整都是合法的。

由于有关同源及固定挠点都在 $p$ 处良好且可分，
$h_{a,R}$ 是 $R$ 的正式盘上的整单位，$r_S$ 是 $O$ 正式盘上的
整函数，常数项为 $1$。更准确地，在 $t=-x/y$ 中，

$$
h_{a,R}(t)\in1+t\mathcal O[[t]],\qquad
r_S(t)\in1+t\mathcal O[[t]],\qquad
R_*(t)\in t^4\mathcal O[[t^4]].                              \tag{3.1}
$$

这里关于 $r_S$ 的整性亦可由 (1.4) 直接得到：其右边在该正式盘
为常数项 $1$ 的整单位，而 $N=17$ 在 $\mathcal O$ 中可逆。
唯一 $N$ 次根递推只须逐次除以 $N$。$a_S\in\mathcal O$ 已在前文
逐点证明。所有极点的约化都离开 $O$，没有用到不受控的局部分母。

令

$$
d=p+1,\quad r=d/4,\quad
c=[t^d]\log(\sigma(\log_Et)/t),\quad v_p(c)=-1,\quad
\rho=p^{-1/(2p)}.
\tag{3.2}
$$

[实际半因子的第一层证明](2026-11-12-inert-half-factor-first-layer.md)
已证明 $t=t(z)$ 在此闭盘上是等距坐标，且

$$
G_\theta(z):=e^{-cz^d}\theta(z)
$$

在 $|z|\le\rho$ 解析，常数项 $1$，
$\|G_\theta\|_\rho=1$、$\|G_\theta-1\|_\rho<1$。
此处 $e^{-cz^d}\theta$ 首先是正式乘积；不要求两个因子分别在
整个闭盘收敛。

置

$$
G_S(z):=e^{-Nc z^d}f_S(z).
\tag{3.3}
$$

因为 $\alpha^d\equiv N\pmod p$，

$$
G_0(z)=e^{c(\alpha^d-N)z^d}G_\theta(\alpha z)
\tag{3.4}
$$

在同一个闭盘解析且 Gauss 范数为 $1$。指数中的系数是整的，
并且 $d/(2p)>1/(p-1)$，所以该额外指数及其逆都在闭盘上收敛。
再由 $G_S=G_0r_S$，得到全部十七行的统一控制

$$
\|G_S\|_\rho\le1.
\tag{3.5}
$$

下面的加强是首层比较的关键。令
$\mathcal P_4f(z)=\frac14\sum_{\epsilon^4=1}f(\epsilon z)$。
因为 $G_0$ 是 $i$ 不变的，而 $[i]t=it$，(3.1) 给

$$
\mathcal P_4(G_S-G_0)
=G_0(\mathcal P_4r_S-1),\qquad
\|\mathcal P_4(G_S-G_0)\|_\rho\le\rho^4.                  \tag{3.6}
$$

目标 $A$ 的对应整根余项也有
$\|e^{-Nc z^d}A\|_\rho\le\rho^4$。
这是同一个较强半径结论的另一证明，直接使用固定有理参考商。

## 4. 十七个解析行与共同参考的准确消去

写 $G_S=\sum_ng_{S,n}z^n$，并定义

$$
J_{S,p}(u)=\sum_{h\ge0}g_{S,dh}(Nc)^{-h}(u)_h,
\quad (u)_h=u(u-1)\cdots(u-h+1).
\tag{4.1}
$$

由 (3.5)，其下降阶乘系数满足

$$
v_p\bigl(g_{S,dh}(Nc)^{-h}\bigr)
\ge\left\lceil\frac{h(p-1)}{2p}\right\rceil.               \tag{4.2}
$$

因此这些都是真正的解析函数，在
$|u|<p^{(p-1)/(2p)}$ 上收敛，并且

$$
J_{S,p}(0)=1,\qquad J_{S,p}\in1+pu\mathcal O\langle u\rangle,
$$

$$
J_{S,p}(k)=k!(Nc)^{-k}[z^{dk}]f_S(z)\qquad(k\in\mathbb Z_{\ge0}).
\tag{4.3}
$$

后一个等式是指数卷积的有限二项式恒等式；并非只在某个模数下成立。
实际半因子准确为

$$
J_{A,p}(u)=\sum_Sa_SJ_{S,p}(u).
\tag{4.4}
$$

设 $J_{\theta,p}$ 是规范
$J_{\theta,p}(k)=k!c^{-k}[z^{dk}]\theta(z)$ 的参考半因子。
它由原参考 $S(z)=\theta(2z)$ 的半因子 $J_{0,p}^{\mathrm{ref}}$
准确给出

$$
J_{\theta,p}(u)=(2^{1-p})^uJ_{0,p}^{\mathrm{ref}}(u),
\qquad J_{\theta,p}(0)=1.
$$

置 $b_p=\alpha^d/N\in1+p\mathcal O$。由 (4.3) 与解析唯一性，

$$
\boxed{\quad J_{0,p}(u)=b_p^uJ_{\theta,p}(u).\quad}         \tag{4.5}
$$

它在 $\mathbb Z_p$ 上为解析单位。现在定义的是**解析行的比值**

$$
K_{S,p}(u):=J_{S,p}(u)/J_{0,p}(u),\qquad
K_{S,p}(0)=1,\quad K_{0,p}=1.
\tag{4.6}
$$

由 $\sum a_S=0$，有全精度的中心关系

$$
\boxed{\quad
J_{A,p}'(0)=\sum_Sa_SK_{S,p}'(0).
\quad}                                                       \tag{4.7}
$$

共同的 $J_{\theta,p}'(0)$ 及
$d\log_p\alpha-\log_pN$ 都已经准确相消。
这并未断言 $K_{S,p}$ 是有理函数 $r_S$ 的独立 Mellin 变换；
(4.1) 中 $G_0$ 与 $r_S$ 的全部卷积项仍然在内。

## 5. 新解析行与原除 $p$ jet 的首层准确相同

沿用前文的整多项式 $C_n$ 及

$$
\kappa_p=-\frac12(-1)^r\binom{2r}{r},\qquad
Z_{S,p}=\frac{C_d(U_S,X_S,Y_S)+\kappa_p}{p}\in\mathcal O.
\tag{5.1}
$$

由于 $d$ 为 $4$ 的倍数，$z^{dh}$ 系数不受 $\mathcal P_4$ 影响。
(3.6) 给差行的系数界

$$
v_p\bigl((g_{S,dh}-g_{0,dh})(Nc)^{-h}\bigr)
\ge\left\lceil\frac{h(p-1)+4}{2p}\right\rceil.
\tag{5.2}
$$

故 $h\ge2$ 的项全部属于 $p^2\mathcal O$。$h=1$ 项中指数
常数的贡献相消，所以

$$
J_{S,p}(u)-J_{0,p}(u)
\equiv \frac{\alpha^dp}{Nc\,d!}(Z_{S,p}-Z_{0,p})u\pmod{p^2}.
\tag{5.3}
$$

利用 $d!/p\equiv-1\pmod p$、$\alpha^d/N\equiv1\pmod p$，得到

$$
\boxed{\quad
\frac{K_{S,p}'(0)}p
\equiv-\frac{Z_{S,p}-Z_{0,p}}{pc}\pmod p.
\quad}                                                       \tag{5.4}
$$

所有除数 $pc$ 都是单位。加权求和后，(4.7) 给

$$
\frac{J_{A,p}'(0)}p
\equiv-\frac1{pc}\sum_Sa_SZ_{S,p}
\equiv\frac{\beta_{p+1}}{17pc}\pmod p,                       \tag{5.5}
$$

与 R54 的首层比较完全一致。这里高阶项的消失来自 (5.2)，
而非未经控制地只保留第 $p+1$ 阶矩。

此外，取任意有限 $H$，(5.2) 也给中心导数差的完整精度证书：
将下降阶乘项的导数求和至 $H$ 后，余项赋值至少

$$
\left\lceil\frac{(H+1)(p-1)+4}{2p}\right\rceil+v_p(H!).    \tag{5.6}
$$

因 $J_{0,p}(0)=1$，$K_{S,p}'(0)=J_{S,p}'(0)-J_{0,p}'(0)$；
故 (5.6) 同样是 (4.7) 中每条非平凡行的可核精度。

## 6. 固定同源的 $[p]$ 交换式保留的是全 jet

在相同规范下，sigma 除法函数的交换恒等式为

$$
\Psi_a(pP)\Psi_p(P)^N
=\Psi_p(aP)\Psi_a(P)^{p^2}.
$$

在 $P=R+z$ 与 $P=R$ 取比，得到

$$
\boxed{\quad
h_{p,R}(z)^N
=h_{p,T}(az)\,h_{a,R}(z)^{p^2}/h_{a,pR}(pz).
\quad}                                                       \tag{6.1}
$$

因此它可以在任何所需的有限精度、有限阶数下使用，且 $pR$ 仅在
一个固定挠点集合中置换。取对数只给

$$
N\log h_{p,R}(z)=\log h_{p,T}(az)+p^2\log h_{a,R}(z)
                         -\log h_{a,pR}(pz).                \tag{6.2}
$$

要重建目标，仍须按 (1.2) 取根、按 (2.1) 加权，并执行 (4.1)
的卷积。只取 $h_{p,R}(0)=1$，或只取 (6.2) 的一个高阶导数，
都没有保留 (5.1) 的 Bell 多项式。

## 7. 五次模型恢复全部对数，而不只恢复单位检测

作为同一解析构造的独立校准，令
$\gamma=2+i$、$\bar\gamma=2-i$、$M=5$，并使用已经证明的

$$
C(z)=\theta(z)\sigma(z)^4
     =\frac{\theta(\gamma z)-\theta(\bar\gamma z)}{4i}.
$$

两个同次数参考行准确为

$$
J_{+,p}(u)=(\gamma^d/M)^uJ_{\theta,p}(u),\qquad
J_{-,p}(u)=(\bar\gamma^d/M)^uJ_{\theta,p}(u).
$$

共同除以 $J_{+,p}$ 后，$K_+=1$，
$K_-=(\bar\gamma/\gamma)^{du}$。所以

$$
J_{C,p}'(0)=\frac{d}{4i}\log_p(\gamma/\bar\gamma)\ne0,
\qquad
v_pJ_{C,p}'(0)=v_pU_{p+1}(4,5).                              \tag{7.1}
$$

这恢复了[五次模型](2026-11-12-degree-five-theta-lucas-interface.md)
的完整非零对数及任意深度；首层只检测后一个赋值是否为 $1$。
实际十七次展开的 $K_{S,p}$ 尚未被证明为这类固定代数数的指数。

## 8. 目前可使用的几何对象与尚未建立的等式

新的参考商至少把自然有理微分放在原椭圆曲线上：

$$
R_*\omega\in H^0(E_0,\Omega^1(\mathcal D)),\qquad
\omega=dx/(2y).
$$

在特征零，映射

$$
H^0(E_0,\Omega^1(\mathcal D))\longrightarrow
H^1_{\rm dR}(E_0\setminus\mathcal D)
\tag{8.1}
$$

是单射。若一个至多简单极点的微分为 $dF$，$F$ 的任意极点都会使
$dF$ 有至少二阶极点，矛盾；因此 $F$ 无极点、为常数，微分为零。
所以这里不会再次丢掉四次覆盖上出现的那两条高阶 exact 模式。

但 (8.1) 尚不是 $J_{A,p}'(0)$ 的比较定理：参考因子
$\theta(\alpha z)$ 仍为正次数线丛的截面，它的全部解析卷积保留于
(4.1)。本篇没有把裸 Cartier 算子或任意一个 Coleman 积分直接
等同于 (4.7)。

一手文献 [K. Bannai, H. Furusho, S. Kobayashi,
*p-adic Eisenstein--Kronecker series for CM elliptic curves and the Kronecker limit formulas*,
Nagoya Math. J. 219 (2015), 269--302](https://www.math.nagoya-u.ac.jp/~furusho/paper/BFK.pdf)
Theorem 1.2、Definition 5.1 给所有良好 $p$ 的 Coleman
$\log_p\theta_R$；其 §5.3 的权插值另外要求普通约化。
该 log 的系数与这里 theta 本身的 Bell 系数不同，因此不能仅凭
第二 Kronecker 极限公式把 (4.7) 改写成固定椭圆单位的对数。
尚需证明的是这些**已明确构造的解析行**与某个保留完整连接及局部
规范的代数周期之间的实际等式，或直接证明它们的特定加权导数非零。
