# R41：连接动量到真实全角根的显式逆与 Wiener 门

**状态：已证明的代数、解析与局部流接口。** 本文没有把保存的有限 Fourier 径向轨道认证为精确解，也没有支付胞元 $0,\ldots,11$ 的径向误差。

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

## 1. 对象与结论

固定一个真实半径 $r>0$，背景斜率 $0<w\leq1/2$，记

$$
z=w^2,\qquad E=1+z,\qquad
p=\frac{h_\theta}{r}=wP,\qquad h_r=k=w(1+K).
\tag{41.1}
$$

本文的 $K$ 是包括零模的**归一高度径向扰动**，不是主曲率。设真实水平度量

$$
\bar g=g-dh^2,\qquad g=E\,dr^2+r^2\,d\theta^2
\tag{41.2}
$$

正定。令

$$
S=1-zP^2=1-p^2,\qquad
D=ES-z(1+K)^2=E(1-p^2)-k^2.
\tag{41.3}
$$

沿半径圆的水平单位切向转角导数为

$$
\Omega=
\frac{1+kp_\theta/S}{\sqrt D}
=\frac{1+z(1+K)P_\theta/S}{\sqrt D}.
\tag{41.4}
$$

给定的**完整连接数据**写成

$$
\Gamma=1+zG,\qquad \Omega=\Gamma.
\tag{41.5}
$$

若 $G$ 的平均值为零，则 (41.5) 直接强制完整转角积分等于 $2\pi$；零模不是事后丢掉或补成零的非线性高度变量。下文给出：

- (41.5) 的显式、避免除以很小的 $z$ 的全角逆；
- 一个可直接由完整输入 $P,P_\theta,G$ 核销的 Wiener 小球；
- 完整 mean、半周位置闭合和单 cut Darboux 二阶迹；
- 与真实无截断径向连接流的双向关系及其正则性条件。

## 2. 显式逆与分支

设

$$
T=P_\theta,\qquad b=\frac{T}{S},\qquad
A=\Gamma^2+zb^2,
\tag{41.6}
$$

并定义

$$
R=\Gamma^2(1-EP^2)+2G+zG^2,\qquad
J=b^2+AR.
\tag{41.7}
$$

当以下量均为实数，且

$$
S>0,\quad \Gamma>0,\quad A>0,\quad R>0,
\tag{41.8}
$$

时取 $\sqrt J$ 的正根，定义

$$
y=\frac{\sqrt J-b}{A}>0,\qquad K=y-1.
\tag{41.9}
$$

若另有 $D=ES-zy^2>0$ 及 $1+zby>0$，则 (41.9) 解原来没有平方的方程 (41.5)。相反，任一 $y>0$ 满足原式及 (41.8)，必等于 (41.9)。

**证明。** 将原式平方并乘以 $D$，得到

$$
\Gamma^2(ES-zy^2)=(1+zby)^2.
\tag{41.10}
$$

因为

$$
ES=1+z(1-EP^2),\qquad
\frac{\Gamma^2-1}{z}=2G+zG^2,
\tag{41.11}
$$

消去共同的常数项并除以 $z>0$，(41.10) 等价于

$$
Ay^2+2by-R=0.
\tag{41.12}
$$

在 (41.8) 下，两根乘积 $-R/A<0$，故恰有一个正根，即 (41.9)。附加的 $D>0$ 和 $1+zby>0$ 恢复平方前的正号。反向论证相同。证毕。

为避免在 $y$ 接近 $1$ 时减去两个接近的数，使用完全相同的恒等式

$$
\boxed{
K=
\frac{2(G-b)+zG^2-\Gamma^2EP^2-zb^2}
{\sqrt{b^2+AR}+A+b}.}
\tag{41.13}
$$

事实上，将 $\sqrt J-(A+b)$ 乘以其共轭即得此式。它没有 $(\Gamma^2-1)/z$ 的数值消差；定义好 $P,G$ 以后，(41.13) 不再除以小量 $w$ 或 $z$。$w$ 很小时输入 $P,G$ 的缩放仍须由实际数据支付。

## 3. 一阶 Wiener 范数及完整解析根

对 $\tau\geq0$，记

$$
\|f\|_{\tau,1}
=\sum_{m\in\mathbb Z}(1+|m|)e^{\tau|m|}|f_m|.
\tag{41.14}
$$

这是含常数 $1$ 的 Banach 代数，因为

$$
(1+|m+n|)e^{\tau|m+n|}
\leq(1+|m|)(1+|n|)e^{\tau|m|}e^{\tau|n|}.
\tag{41.15}
$$

以下根是完整 Fourier 函数，不在任何步骤投影到有限模。

### 定理 41A

设 $P,T=P_\theta,G$ 均属于 (41.14)，且在实角上为实值。设 $0<w\leq1/2$，并令

$$
\eta=\|P\|_{\tau,1}+\|T\|_{\tau,1}+\|G\|_{\tau,1}
\leq\frac1{32}.
\tag{41.16}
$$

则用 Banach 代数中的 Neumann 级数解释 $S^{-1}$，用以 $1$ 为中心的二项级数解释 $\sqrt J$，(41.13) 定义唯一的近背景正分支根，并且

$$
\|K\|_{\tau,1}\leq\frac98\eta.
\tag{41.17}
$$

它满足完整 (41.5)。在每个实角上同时有

$$
\begin{aligned}
S&\geq1-\eta^2/4>0,\\
\Gamma&\geq1-\eta/4>0,\\
D&\geq1-\frac35\eta>0,\\
1+zby&\geq1-\frac9{32}\eta>0,\\
y+ET&\geq1-\frac{19}{8}\eta>0.
\end{aligned}
\tag{41.18}
$$

“唯一”指正根 $y>0$ 的原连接方程分支；它不排除远离本域、改变方向或改变根号的其它代数表达式。

**证明。** 本节所有范数都指 (41.14)。记 $g=\|G\|$、$t=\|T\|$、$p=\|P\|$，故 $g+t+p=\eta$。由

$$
\|zP^2\|\leq\eta^2/4\leq1/4096
\tag{41.19}
$$

可得

$$
\|b\|\leq\frac{t}{1-\eta^2/4}
\leq\frac{257}{256}\,t.
\tag{41.20}
$$

所有下面的估计均在同一个完整 Banach 代数内进行。首先

$$
\|A-1\|
\leq\frac12g+\frac1{16}g^2+\frac14\|b\|^2
\leq\frac12\eta+\frac13\eta^2
\leq\frac{17}{32}\eta.
\tag{41.21}
$$

其次，因 $E\leq5/4$ 和 $\|\Gamma\|\leq1+\eta/4$，

$$
\begin{aligned}
\|R-1\|
&\leq\frac52g+\frac5{16}g^2
   +\frac54(1+\eta/4)^2p^2\\
&\leq\frac52\eta+2\eta^2
\leq\frac{21}{8}\eta.
\end{aligned}
\tag{41.22}
$$

从而

$$
\begin{aligned}
\|J-1\|
&\leq\|A-1\|+\|R-1\|
  +\|A-1\|\|R-1\|+\|b\|^2\\
&\leq\frac{101}{32}\eta+3\eta^2
\leq\frac{13}{4}\eta<\frac18.
\end{aligned}
\tag{41.23}
$$

这里使用
$(17/32)(21/8)+(257/256)^2<3$。
二项级数在范数中绝对收敛，且

$$
\|\sqrt J-1\|
\leq1-\sqrt{1-\|J-1\|}
\leq\|J-1\|.
\tag{41.24}
$$

因此 (41.13) 的分母 $L=\sqrt J+A+b$ 满足

$$
\|L-2\|
\leq\left(\frac{13}{4}+\frac{17}{32}
                  +\frac{257}{256}\right)\eta\leq5\eta,
\qquad
\|L^{-1}\|\leq\frac1{2-5\eta}\leq\frac{32}{59}.
\tag{41.25}
$$

其分子 $N$ 满足

$$
\begin{aligned}
\|N\|
&\leq2(g+\|b\|)+\frac14g^2
  +\frac54(1+\eta/4)^2p^2+\frac14\|b\|^2\\
&\leq\frac{257}{128}\eta+2\eta^2
\leq\frac{265}{128}\eta.
\end{aligned}
\tag{41.26}
$$

故 $\|K\|\leq(265/236)\eta\leq(9/8)\eta$，证明 (41.17)。又 (41.21)–(41.23) 保证在实角上 $A,R,J$ 均为正。定义的平方根与正实平方根一致，故由代数恒等式确有 $y=1+K=(\sqrt J-b)/A>0$。

其余分支门也可以不诉诸采样直接得到：

$$
\|D-1\|
\leq\frac14\left(2\|K\|+\|K\|^2+\frac54p^2\right)
\leq\frac9{16}\eta+\frac{161}{256}\eta^2
\leq\frac35\eta,
\tag{41.27}
$$

以及

$$
\|zby\|
\leq\frac14\frac{257}{256}\eta
\cdot\left(1+\frac9{256}\right)
\leq\frac9{32}\eta.
\tag{41.28}
$$

最后

$$
\|K+ET\|\leq\frac98\eta+\frac54\eta
=\frac{19}{8}\eta.
\tag{41.29}
$$

得到 (41.18)。由第 2 节恢复原式，正根唯一。全部构造只用绝对收敛的 Banach 代数运算，故保留所有非线性产生的高频与 mean。证毕。

**正则性说明。** 输入门明确需要 $P_\theta\in W_{\tau,1}$，即一个额外的角导数，不能只拿 $\|P\|_{\tau,1}$ 免费替代它。当 $\tau>0$ 时得到相应开复条带内的解析函数；在边界条带上本文使用的是绝对 Fourier 范数，不通过角网格最大值估计。

## 4. 完整 mean、周期和单 cut 两阶迹

若 $G_0=0$，则由恒等式 $\Omega=1+zG$，

$$
\frac1{2\pi}\int_0^{2\pi}\Omega\,d\theta=1.
\tag{41.30}
$$

由 (41.17) 得到的 $K_0$ 一般不为零。它正是连接条件选出的完整 mean slope correction $wK_0$。本文没有把有限投影算出的 mean 当成 (41.30) 的精确根。

若进一步 $P,G$ 为 $\pi$ 周期且 $\int P=0$，则 $S,K,D,\Gamma$ 也为 $\pi$ 周期。取

$$
\gamma_\theta=\Gamma,\quad
t=(\cos\gamma,\sin\gamma),\quad
a=r\sqrt S,\quad X_\theta=a\,t.
\tag{41.31}
$$

由 $\Gamma$ 的 $\pi$ 周期及平均值 $1$，任意长度为 $\pi$ 的转角积分均为 $\pi$，于是

$$
t(\theta+\pi)=-t(\theta),\qquad
X_\theta(\theta+\pi)=-X_\theta(\theta).
\tag{41.32}
$$

故 $\int_0^{2\pi}X_\theta\,d\theta=0$，位置严格闭合；$\int h_\theta=rw\int P=0$ 给高度严格闭合。又 $\Gamma>0$、$a>0$，故该水平边界是转角一次的严格凸闭曲线，可接 R30 的真实 Cartesian trace 公式。这里只从一个 cut 的数据得到闭合边界，不推出整个尾的平面 development 已单值。

若 $w_r$ 也由同一个真实源给定，则定义

$$
q=
\frac{E(k_\theta-p)^2/r+w w_r(1-p^2+kp_\theta)}
{k+Ep_\theta}.
\tag{41.33}
$$

定理 41A 保证分母
$k+Ep_\theta=w(y+ET)>0$。因此 $h_{rr}=q$ 给出唯一的完整 Darboux 二阶迹。其证明是将

$$
\det(\operatorname{Hess}_g h)
=K_g(1-|\nabla_g h|^2),\qquad
K_g=\frac{E'}{2rE^2},\quad E'=2ww_r
\tag{41.34}
$$

按 $h_{rr}$ 解开；展开可得 (41.33)。这同时包含所有 mean 与非线性高频。所给 $h,k,q$ 是一个精确的**单 cut 高度两阶迹**；是否存在沿整个固定径向区间满足同一方程并接到深尾的高度，仍是另一个问题。

## 5. 与无截断真实径向流的关系

设在一个开径向区间内 $w>0$ 且 $w\in C^2$。为使用经典曲率和 connection 公式，本节先要求 $p,k$ 为 $C^2$，从而构造的高度为 $C^3$，水平度量为 $C^2$。分段光滑源可逐段使用，再以所需的公共迹拼接；不能仅由终端 $C^2$ 声明默认所有中间经典三阶计算都成立。

假设

$$
\partial_r(rp)=k_\theta,\qquad
S>0,\quad D>0.
\tag{41.35}
$$

令 $n$ 为 $t$ 的左法向，并记

$$
a=r\sqrt S,\qquad
u=-\frac{kp}{\sqrt S},\qquad
v=-\frac{\sqrt D}{\sqrt S}.
\tag{41.36}
$$

拟构造水平 development 时有
$X_\theta=a t,\ X_r=u t+v n$。恒等式 $X_{r\theta}=X_{\theta r}$ 的切向分量给出

$$
\gamma_\theta=\frac{a_r-u_\theta}{-v}
=\frac{1+kp_\theta/S}{\sqrt D}=\Omega;
\tag{41.37}
$$

法向分量给出

$$
\gamma_r=\frac{u\Omega+v_\theta}{a}
=\frac{k(k_\theta-p)}{rS\sqrt D}=:\Psi.
\tag{41.38}
$$

为核对最后一个化简，使用
$D_\theta=-2Epp_\theta-2kk_\theta$；
含 $pp_\theta$ 的其余系数正好为
$E-k^2/S-D/S=0$。

由此，在 (41.35) 下，局部水平平直性的精确兼容条件是

$$
\Omega_r=\Psi_\theta.
\tag{41.39}
$$

若 (41.39) 成立，则在任一单连通小邻域先积分闭一形式
$\Psi\,dr+\Omega\,d\theta$ 得 $\gamma$，再由 (41.37)–(41.38) 积分水平向量一形式
$(u t+v n)\,dr+a t\,d\theta$ 得 $X$。它的内积为

$$
|X_r|^2=E-k^2,\quad
X_r\cdot X_\theta=-rkp,\quad
|X_\theta|^2=r^2(1-p^2).
\tag{41.40}
$$

同时，(41.35) 使 $k\,dr+rp\,d\theta$ 闭，在局部积分得 $h$。因此 $(X,h)$ 的第一基本形式恰为 $g$，并且其投影 Jacobian 为 $r\sqrt D>0$。反向从这样的局部等距高度图求 frame，必得到 (41.35)、(41.37)–(41.39)。

在定理 41A 的分支内将 $\Omega=\Gamma=1+w^2G$、$k=w(1+K(P,G))$ 代入，记 $\lambda=w_r/w$，得到完整径向系统

$$
\boxed{
\begin{aligned}
P_r&=\frac{K_\theta-P}{r}-\lambda P,\\
G_r&=-2\lambda G+
\frac1r\partial_\theta\left[
\frac{(1+K)(K_\theta-P)}
{(1-w^2P^2)\sqrt{1-w^2(2K+K^2+EP^2)}}\right].
\end{aligned}}
\tag{41.41}
$$

这是一个含全部角模及完整根的精确系统。第一式是高度兼容，第二式是水平 connection 的平直性；没有把有限投影的余项设为零。

平均第一式表明 $\int rp$ 沿半径保持。平均 $\Gamma_r=\Psi_\theta$ 表明 $\int\Gamma$ 沿半径保持。因此若某个 cut 有 $\int P=0$ 和 $G_0=0$，则所有同连通区间的 cut 继续满足高度周期与转角周期。高度零模最后由

$$
\frac{d h_0}{dr}=w(1+K_0)
\tag{41.42}
$$

及一次积分常数确定。真实整个 annulus 的平移周期、全局单值、全局图和 cuff 正则性仍按 R30/R32 的条件处理，不能从局部流等价省略它们。

在每个 $\mu$ 为常数的原胞元中，设 $Q=h_\perp/r^4$，并使用源代码的 plain-cosine 连接动量

$$
\Pi=\frac{\sigma r^4(\Omega-1)}{\sqrt{12}\mu},
\qquad \sigma\in\{-1,1\}.
\tag{41.43}
$$

则 (41.41) 等价于其完整 Fourier 系数流

$$
\begin{aligned}
(Q_m)_r&=\frac{k_m}{r^4}-\frac4rQ_m,\\
\Pi_r&=\frac4r\Pi+
\frac{\sigma r^3w^2}{\sqrt{12}\mu}
\partial_\theta\left[\frac{(1+K)(K_\theta-P)}{S\sqrt D}\right].
\end{aligned}
\tag{41.44}
$$

原 worker 的有限系统是对这些表达式的有限投影与有限角求根，另外还有径向离散；本定理没有证明那些操作的误差为零或已经获得所需上界。

## 6. 如何接实际强尾数据

若完整输入用 real sine/cosine 系数给定，

$$
h_\perp=\sum_{m\geq1}H_m\cos(m\theta),\qquad
\Pi=\sum_{m\geq1}\Pi_m\cos(m\theta),
\tag{41.45}
$$

则

$$
P=-\sum_{m\geq1}\frac{mH_m}{rw}\sin(m\theta),
\qquad
G=\sum_{m\geq1}\frac{\sigma\sqrt{12}\mu\Pi_m}{r^4w^2}
\cos(m\theta).
\tag{41.46}
$$

故 (41.16) 的一项可直接核算的上界为

$$
\eta\leq
\sum_{m\geq1}(1+m)e^{\tau m}
\left[
\frac{m(1+m)|H_m|}{rw}
+\frac{\sqrt{12}\mu|\Pi_m|}{r^4w^2}
\right].
\tag{41.47}
$$

实正弦或余弦的两个 signed Fourier 系数各为实幅度的一半；(41.47) 已将它们相加，不能再多乘或少乘 $2$。若使用 $Q_m$，第一分式应写为 $m(1+m)r^3|Q_m|/w$。

应用于当前新实源时必须保留以下身份：

1. $r,w,w_r,\mu$ 来自同一 R26 实源，不把 stored 浮点半径当成严格实半径。当前真实 $R_{\rm out}$ 与名义 binary $0.3$ 有严格正的差。
2. 原胞元接口的 $\Pi$ 按源定义作真实 $\rho=2^{11/4}$ 规范转换。用浮点 $\rho$ 重新生成的有限候选不能充当精确规范恒等式。
3. 若强前缀约束的是**完整固定 $H$**，应在真实半径用 $Q_m=H_m/r^4$。原保存的 binary $Q$ 所定义的邻近高度与这个固定 $H$ 不自动相同。
4. 将未保存的输入 $\Pi_m,H_m$ 置零，可以**定义一个新的完整角向候选**；不能因此断言真正径向解的未表示模为零。公式 (41.13) 随即会重新产生无穷多个 $K$ 模。
5. 先前 tail_outer_saved_port_norms.py 的 13 端口包核算的是保存 $Q$ 与新返回 binary $L$ 定义的有限角候选；它没有验证 (41.47)，也没有把该 $L$ 认证为本文的完整根。

可继续做的具体接口是：对保存的全部 109 个原 segment 端点，在 R26 的严格端点半径及同实源上计算 (41.47)，并区分端口候选、固定 cut-$H$ 候选及真正待证的径向误差盒。该步骤仍只提供离散的强范数入口；把全部径向面板、完整高频、Darboux 残差及深端匹配纳入同一个存在论证，才可以接到 R31/R32 的整尾结论。

## 7. 用有限多项式残差认证完整根与保存候选之差

直接把 (41.17) 用作实际强范数上界可能较粗。可以保留已有有限候选的精细谱，并用一个**有限**多项式残差支付它与完整根之间的全部误差。

### 定理 41B

在定理 41A 的同一输入下，设 $\widehat K\in W_{\tau,1}$ 为任意实值候选，包括其 mean，且

$$
\|\widehat K\|_{\tau,1}\leq\frac1{16}.
\tag{41.48}
$$

令 $\widehat y=1+\widehat K$，构造

$$
\mathcal E=
(\Gamma^2S^2+zT^2)\widehat y^2
+2TS\widehat y-RS^2.
\tag{41.49}
$$

则完整真实根满足

$$
\boxed{\ \|K-\widehat K\|_{\tau,1}
\leq\frac47\|\mathcal E\|_{\tau,1}.\ }
\tag{41.50}
$$

因此若 $\widehat K_\perp$ 表示候选的全部非零模，则

$$
\|P\|_{\tau,1}+\|K_\perp\|_{\tau,1}
\leq\|P\|_{\tau,1}
+\|\widehat K_\perp\|_{\tau,1}
+\frac47\|\mathcal E\|_{\tau,1}.
\tag{41.51}
$$

mean 的误差也不超过 (41.50) 的右端。式 (41.51) 是接 R33 的真实角向强范数门，而不是有限采样范数。

**证明。** 记

$$
e=A\widehat y^2+2b\widehat y-R=\frac{\mathcal E}{S^2}.
\tag{41.52}
$$

由 $Ay+b=\sqrt J$ 以及两个二次式作差，

$$
e=(\widehat y-y)(A\widehat y+b+\sqrt J).
\tag{41.53}
$$

此处没有有限投影。由第 3 节的界，分母的 Banach 代数范数满足

$$
\|A\widehat y+b+\sqrt J-2\|
\leq5\eta+(1+17\eta/32)\|\widehat K\|.
\tag{41.54}
$$

其严格小于 $2$，所以分母可在同一 Wiener 代数中求逆。又
$\|S^{-2}\|\leq(1-\eta^2/4)^{-2}$。从 (41.52)–(41.54) 得到

$$
\|K-\widehat K\|
\leq
\frac{\|\mathcal E\|}
{(1-\eta^2/4)^2
 [2-5\eta-(1+17\eta/32)\|\widehat K\|]}.
\tag{41.55}
$$

在 $\eta\leq1/32,\ \|\widehat K\|\leq1/16$ 下，该分母不小于

$$
\left(1-\frac1{4096}\right)^2
\left[2-\frac5{32}-\frac{1+17/1024}{16}\right]
>\frac74.
\tag{41.56}
$$

这是一个直接的有理数不等式，故 (41.50) 成立。零模投影和非零模投影均不增大 (41.14)，于是得到 (41.51) 与 mean 断言。证毕。

若 $P,G,\widehat K$ 都是最大物理角频率不超过 $m_{\max}$ 的三角多项式，则 (41.49) 本身最大频率不超过 $8m_{\max}$。因此可用严格有限卷积计算其全部系数及 (41.14)，没有角采样混叠、无穷级数截断或遗漏的 residual 高频。完整根 $K$ 仍然通常有无穷多个频率，(41.50) 同时控制它们。

保存的 binary 正交 cosine 根 $L$ 可定义

$$
\widehat K_0=L_0,\qquad
\widehat K_m=\sqrt2L_m+\frac{m^2r^3Q_m}{w}
\quad(m>0)
\tag{41.57}
$$

作为 real-cosine 幅度。只要 $r,w,Q$ 的真实定义和包络明确，这就给出一个具体候选；不要求原有限求根“已经被严格认证”。原求根的舍入、有限投影和角 quadrature 偏差会通过 $\mathcal E$ 被重新计算。若所用 $Q$ 改为固定 cut-$H$ 的 $H/r^4$，也必须在 (41.57) 中一致修改，不能混用两个 cut。

这仍是每个指定径向点的结论。让每个系数成为一个整径向面板上相同函数的严格包络，或先支付有限径向重建及真实流的误差，才可据 (41.50) 获得整个面板的强范数；109 个端点本身不足以代替这个步骤。

## 8. 引用与范围

- R26：真实浅头与外半径径向源函数、严格积分和参数身份。
- R19/R30：完整 mean、精确 cut 的 Cartesian 两阶迹、转角及位置闭合。
- R31/R32：完整高度满足 Darboux 后的曲率预算和全局水平图条件。
- R33：固定变量 strip 的全频强空间、完整非线性源与有限头闭合预算。
- 固定源 scripts/78718-tail-fourier-root-momentum.mjs：有限 projected connection root 与径向系数的实现，用于识别实际数据格式；本文证明不依赖该离散求解的收敛声称。

本文已支付的是精确全角代数逆、解析输入门、完整零模与局部真实流接口。外 $0,\ldots,11$ 胞元的连续真实轨道、与强前缀同 $H$ 的匹配误差、固定 $g$ 精化及完整闭曲面的几何门仍分别保留。
