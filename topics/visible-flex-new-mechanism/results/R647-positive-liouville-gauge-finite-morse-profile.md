# R647：低密度指数的有理 Morse 双核、正 Liouville 因子与有限中心

2026-11-28，接续 R630/R639/R644。这里先将二/三核改为 Morse 的第二/第三径向等级，再改变同一谱下的正 Liouville 密度因子。每个 profile 始终使用这个新背景自己的左正规第一模解。它不同于已计算的“固定旧 $P=e^{-2\eta X}$、改右端第一模 Cauchy 数据”的有限小 $\nu$ 分支。下面证明准确有理谱、完整径向合法性与可计算的有限中心公式；尚未声称某个新有限 profile 已达宏观角或 reach。

## 1. 同一谱允许另一个正密度因子

取明确有限参数

$$
\rho(X)=s^2(e^{-X}-e^{-2X})-B_M,\quad s=11/5,
\quad B_M=3/100,\quad \eta^2=37/100,
$$
$$
H_j=-\partial_X^2+\eta^2-j^2\rho.
$$

R630 的 Morse 代换给全部离散谱

$$
\boxed{E_{j,N}=\frac{37+3j^2-(11j-5N)^2}{100},
\quad N=2n+1>0,\quad N<11j/5.}                       \tag{0a}
$$

因此 $(j,N)=(2,3),(3,5)$ 准确为零；其它非零离散谱绝对值至少 $1/100$，连续谱阈值为 $(37+3j^2)/100$。不能据此删去其它零模：例如 $(157,291)$、$(198,367)$ 也给零能。第 4 节明确处理这个接口。第一模只有 $N=1$ 一个离散谱，值为 $1/25>0$。

写 $t=e^{-X}$、$z_j=2jst$，两条指定核为

$$
\begin{aligned}
\psi_2&=t^{7/10}e^{-2st}\bigl((2s-2)-4st\bigr),\\
\psi_3&=\frac12t^{4/5}e^{-3st}
\bigl[z_3^2-2(3s-3)z_3+(3s-4)(3s-3)\bigr].
\end{aligned}                                                   \tag{0b}
$$

负组件的两个 $t$ 根为 $t_\pm=(11\pm\sqrt{118})/22$；其间 $\rho>0$，外部 $\rho<0$，故物理 $w'$ 的负区仍恰为一个组件。$\psi_2$ 恰有一个零点 $t=3/11$；$\psi_3$ 恰有两个零点 $t=(6\pm\sqrt{10})/22$。它们全在负组件内，且三个节点严格交错：

$$
t_-<\frac{6-\sqrt{10}}{22}<\frac3{11}
<\frac{6+\sqrt{10}}{22}<t_+.
$$

两核在正区没有节点；乘同一严格正 $\sigma^{-1}$ 不改这些节点或类型分类。

记 $X_L=-\log t_+$、$X_R=-\log t_-$。令

$$
\beta_M=\sqrt{2/5},\quad
a_U=\beta_M-3/5>0,\quad b_U=1+2\beta_M,
$$
$$
\psi=\psi_1=e^{-st}(2st)^{\beta_M}
 U(a_U,b_U,2st)>0,\qquad u=\psi'/\psi.
$$

这里 $H_1$ 的点态势会变号，不能借 R630 的“处处正势”论证 $\psi'>0$。所需径向界可直接从 Tricomi 正积分支付。对概率密度正比于
$e^{-zv}v^{a_U-1}(1+v)^{b_U-a_U-1}$，分部积分给

$$
z\mathbb E(v)
=a_U+(b_U-a_U-1)\mathbb E\frac{v}{1+v}\ge a_U.
$$

因 $b_U-a_U-1=\beta_M+3/5>0$，以及
$u=st-\beta_M+z\mathbb E(v)$，得到整个实线上的准确不等式

$$
\boxed{u+\eta\ge st+\eta-3/5
=st+(\sqrt{37}-6)/10>0.}                             \tag{0c}
$$

令 $u_R=u(X_R)$、$\psi_R=\psi(X_R)$。式 (0c) 特别保证下面的 admissible 区间非空。

任取

$$
-\eta<a_R<\min\{\eta,u_R\},\qquad
\nu_R=u_R-a_R>0.
$$

定义

$$
\sigma(X)=\psi_R\left[
\cosh\bigl(\eta(X-X_R)\bigr)
+\frac{a_R}{\eta}\sinh\bigl(\eta(X-X_R)\bigr)\right],
\qquad P=\sigma^2.                                      \tag{1}
$$

由于 $|a_R|<\eta$，$\sigma$ 是两条正指数的正线性组合；它在全线严格为正，且 $\sigma''/\sigma=\eta^2$。因此全部 $H_j$、二三双核、其它整数谱及负组件行程角均与本节新有理参考完全相同，并非仅保持某两条有限频率方程。

令

$$
W=\sigma\psi'-\sigma'\psi,
\quad r=\psi/\sigma,
\quad \nu=r_X/r=u-\sigma'/\sigma,
\quad w=\lambda W,\qquad \lambda>0.                    \tag{2}
$$

归一化给 $r(X_R)=1$，且

$$
W'= -\rho\sigma\psi,\qquad
W(X_R)=\psi_R^2\nu_R>0.                              \tag{3}
$$

在 $X\to-\infty$，左正规渐近给 $W\to0^+$。在 $(-\infty,X_L)$，$W'>0$；在 $(X_L,X_R)$，$W'<0$，但末值仍正；在 $(X_R,\infty)$，$W'>0$。故 **$W>0$ 于整条实线**，从而 $r_X>0$、$w>0$。这一次没有旧有限 Cauchy 分支的左侧 $r_X=0$ 截断。

记 $\beta_M=\sqrt{\eta^2+B_M}>\eta$。左端 $\psi$ 的超指数衰减给 $r\to0$；右端 $\psi\sim C e^{\beta_M X}$，而 $\sigma\sim A e^{\eta X}$，故 $r\to\infty$。因此 (2) 给全线到 $(0,\infty)$ 的真正径向坐标。

对任意 $H_j\psi_j=0$，置 $f_j=\psi_j/\sigma$，直接计算得

$$
\boxed{(wf_j')'-j^2(w'/r)f_j
      =-\frac{\lambda\sigma}{r_X}H_j\psi_j=0.}          \tag{4}
$$

这里左边撇号是物理 $r$ 导数，右边 $X$ 导数只出现于 $H_j$。实际行程角为

$$
\int_{w'<0}\sqrt{-w'/(rw)}\,dr
=\int_{X_L}^{X_R}\sqrt\rho\,dX,                       \tag{5}
$$

与 $a_R$、$\lambda$ 都无关。

该行程角明确为

$$
T=\pi\alpha,\qquad \alpha=(11-\sqrt3)/10,
\qquad |\sin(jT)|\ge\frac1{50j}\quad(j\ge1).          \tag{5a}
$$

为验证常数，取 $k$ 为 $j\alpha$ 的最近整数。整数
$(10k-11j)^2-3j^2$ 非零，绝对值至少一；另一个共轭因子绝对值至多 $(2\sqrt3+5)j$。因此
$\operatorname{dist}(j\alpha,\mathbb Z)\ge[10(2\sqrt3+5)j]^{-1}$，再用 $|\sin\pi x|\ge2\operatorname{dist}(x,\mathbb Z)$ 即得 (5a)。

端点值 $a_R=-\eta$ 作为单边极限恢复本新谱的指数密度，但归一化仍为 $r(X_R)=1$。这不等于 R630 的旧核等级，不能继承旧 $\beta$ 的数值或符号。

## 2. 有限中心的真实高度与曲率

令 $a(X)=\sigma'/\sigma$，则 $a'=\eta^2-a^2$，$\nu=u-a$。全部实际量可由同一 $\psi,\psi'$ 与初等双曲函数读取：

$$
\begin{aligned}
r_X&=r\nu,& w&=\lambda\sigma\psi\nu,\\
h_X&=w r_X=\lambda\psi^2\nu^2,&
w_r&=-\lambda\sigma^2\rho/\nu,\\
\kappa_\theta&=\frac{w}{r\sqrt{1+w^2}},&
\kappa_r&=\frac{-\lambda\sigma^2\rho}
 {\nu(1+w^2)^{3/2}}.
\end{aligned}                                                   \tag{6}
$$

因此在负组件 $[X_L,X_R]$ 上可指定一个真实有限高度 $H_0>0$，准确取

$$
\lambda=H_0\left(\int_{X_L}^{X_R}\psi^2\nu^2\,dX\right)^{-1}.
                                                               \tag{7}
$$

这不是只重新给 $w(X_R)$ 赋值。旧小 $\nu$ 表格中的巨大高度来自另一条 $\psi$；那些数字既不证明这里低矮，也不构成这里的下界。公式 (6)–(7) 需要实际评价后才有新几何数值。

积分还满足可用于同一求值的准确恒等式

$$
\int_A^B\psi^2\nu^2\,dX
=[\psi^2\nu]_A^B+\int_A^B\rho\psi^2\,dX.             \tag{8}
$$

在真实两根间，半径比、总高度、两主曲率和端口 Cauchy 数据均属于同一个已指定的 $a_R,\lambda$，不得混用不同 $a_R$ 的有利数值。

单凭 (6) 的曲率上界仍不等于整个闭面 reach；完整连接与全局法向管仍需实际支付。右正区的 $w$ 最终增长为 $e^{(\beta_M+\eta)X}$，所以不能从核心低高度推断可以免费取任意长正 buffer。

## 3. 该 profile 自己的二阶端口

令 (0b) 的两核按一个明确有限点规范为 $f=f_2=\psi_2/\sigma$、$g=f_3=\psi_3/\sigma$。R635 仍准确适用；全线两端的边界项为零，所以完整参考端口只需 $\beta_0$。定义

$$
F=\psi_2/\psi=f/r,\qquad G=\psi_3/\psi=g/r.
$$

代入 R628 的完整公式得到

$$
\boxed{\beta_0=-\frac1{2\lambda}\int_{-\infty}^{\infty}
\left[\frac{\sigma\psi F'G'}{W^2}
      -\frac{8F'G+3FG'}W\right]\,dX.}                 \tag{9}
$$

此处 $F',G'$ 是 $X$ 导数。等价地，记 $p_j=\psi_j'-a\psi_j$，则被积函数为

$$
-\frac1{2\lambda\sigma\psi^3}
\left[\frac{p_2p_3}{\nu^2}
 -\frac{9p_2\psi_3+4\psi_2p_3}{\nu}
 +12\psi_2\psi_3\right].                             \tag{10}
$$

从 (10) 到 (9) 的常数项准确为 $1-9-4+12=0$。两核始终属于同一个新 $w$，没有把旧径向转换的 $\beta_0$ 移交过来。

左端的完整被积函数为 $e^{-2s e^{-X}}$ 乘一个固定次幂；右端为一个严格衰减指数。具体地，$\psi_2\sim e^{-\alpha_2X}$、$\psi_3\sim e^{-\alpha_3X}$，$\alpha_2=7/10$、$\alpha_3=4/5$，右端 (10) 的衰减率至少是 $\alpha_2+\alpha_3+3\beta_M+\eta>0$。因此每个固定 admissible $a_R$ 的积分绝对收敛。R635 的 $K$ 右端衰减率为 $\alpha_2+\alpha_3+\beta_M-\eta>0$，左端同样超指数衰减，故 $\beta_{w^2}=0$。

在单指数端点 $a_R=-\eta$，两条右端衰减率分别改为 $\alpha_2+\alpha_3+3\beta_M-\eta$ 和 $\alpha_2+\alpha_3+\beta_M+\eta$，仍严格为正；所以该比较支也有同样的完整参考积分与零边界项。

在 admissible 参数的紧子区间上，这些估计给参数连续性。指数端点也可用共同控制通过：先选一个有限 $X_1$，使 $u\ge\eta+(\beta_M-\eta)/2$ 于 $X\ge X_1$。记 $d_0=(\sqrt{37}-6)/10$；当 $a_R$ 足够接近 $-\eta$ 时，$a=\sigma'/\sigma\le-\eta+d_0/2$ 于 $X\le X_1$。结合 (0c)，整个实线有一个与该小参数无关的正 $\nu$ 下界。同时 $\sigma\ge c e^{-\eta X}$，$|a|\le\eta$，代入 (10) 即有共同可积控制。本新核对的端口符号尚须自己评价和证明；R637 的旧严格区间不能移交。

有限 cut 的端口必须保留

$$
\beta_{w^2,[A,B]}=-\frac12[K]_{r(A)}^{r(B)}.
$$

在实际平尾尚未接上前，任何有限积分只标作核心贡献，不能当作整个连接器的端口。

## 4. 同一谱背景继续进入真尾与非线性系统的接口

本有理谱的额外零模必须先处理。若在正区用 $e^\zeta\sigma$，零阶势变化准确为

$$
Q_\zeta=\zeta''+2a\zeta'+(\zeta')^2.                 \tag{11}
$$

左端 $a\to-\eta$，(0b) 中的 Laguerre 首项使 $\psi_2,\psi_3$ 的完整左端幂仍分别为 $t^{s-1/2}e^{-2st}$、$t^{3s/2-1/2}e^{-3st}$。因此 R639 两个远左正 bump 的响应行尺度、可逆极限矩阵及恢复代价 $C_L\le\operatorname{poly}(L)e^{6sL}$ 原样适用。对 $j\ge4$ 的近零归一特征函数，左正区质量仍为 $\operatorname{poly}(L)e^{-8sL}$；取一个有限 $L$ 令两者乘积小于 $1/2$。

先将常势改为 $\eta_\epsilon^2=\eta^2+\epsilon$，然后用这两个 bump 准确恢复指定二/三核。选一个有限正 $\epsilon$，使 $(1+C_L)\epsilon<1/400$，则 (0a) 的所有原非零谱保持至少 $3/400$ 的间隔，所有额外零模的位移在 $(\epsilon/2,3\epsilon/2)$。这一步使用 R639 已证的统一质量估计，包含低整数和全部高整数，不只渐近高频。第一模谱仍严格为正；其左正规解也仍正。

对固定 admissible $a_R$，还可令 $\epsilon$ 小到保留 $W(X_R)>0$。修复后 $\sigma=e^\zeta\sigma_{\epsilon}$ 与 $\psi$ 满足同一个零阶势，故准确的 $W'=-\rho\sigma\psi$ 不变，(3) 的全线单调性论证仍成立。由 R633 的四个真实正区控制保持两谱行和径向 Cauchy 行，可将后续 profile 改动限制在真实物理紧区间；节点远左没有新增零点，不影响满秩首项。

这给新中心的统一线性谱准备，但真正装配仍须为该中心选有限 cuts、控制和真平尾稳定线；它们的数值几何不能从原 R639 背景移交。本稿不把谱相同当作已经完成该有限装配。

一旦实际装配和该背景的非零端口已支付，R644 的 proof 只消费实际 $r,w$、两核、统一参考逆与端口；它不要求 $\sigma$ 必为单指数。然而 R644 的局部幅值常数仍需这一个新背景自己的估计。垂直尺度 (7) 也不产生免费有限倾角。

下一实际计算只评价本节明确的 $(s,\eta^2,B_M)=(11/5,37/100,3/100)$、(1)–(10)、同一核心及固定 buffer 的几何和真实端数据，用来选可进入有限非线性求根的低矮输入。已有 R630 原分支、失败/高度成本及其数值费用完整保留，不重跑旧范围，也不把有限核心当成已闭合曲面。
