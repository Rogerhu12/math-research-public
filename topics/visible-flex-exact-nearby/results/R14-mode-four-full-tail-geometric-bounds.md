# R14：第四模主干、真实平尾与双 bump 的统一几何余量

2026-11-10，geometry-transfer。

**状态：已证明；主课题的中间结论。** 本文对第四模新背景独立证明几何
界，再把 [R11](R11-matched-mode-four-physical-tail-connector.md) 的实际
connector、真实 R72 无限平尾和附录 A 的双 bump 一并纳入。曲率估计
覆盖平尾的全部实际过渡层；reach 使用全局法向管单射。
结果包含具有内点且尺寸合格的两个平盘握持集，以及 R11 真无穷小场
在该集上为零。它不构成有限幅精确等距族。

源：
[R7](R7-metric-bump-uniform-tail-angle-separation.md) §1—2、
[R11](R11-matched-mode-four-physical-tail-connector.md) §4—8、附录 A；
quantitative-newton-twist-flex 的
[R72](../../quantitative-newton-twist-flex/results/R72-large-width-inner-tail-to-cut128.md)
§2、§9.2、§11.2。未从 $n_*=3$ 的 R5 转授几何数值。

## 1. 结论及统一参数

未改第四模主干为
$$
\delta_4=\frac{\sqrt2}{4},\quad A_4=2+\delta_4,\quad
Q(x)=2-A_4\operatorname{sech}^2x,\quad
h''=Qh,\quad h(0)=1,\ h'(0)=0,
$$
$$
a=h^{-1},\qquad z(x)=\int_0^x h^{-2},\qquad X=a e_r+z e_z.
$$
第 2—7 节暂简写 $\delta=\delta_4$。
补两极后，它是闭 $C^2$ 嵌入球面，且
$$
h>\frac78,\quad z_\infty<\frac{11}{4},\quad
\sup|X|<3,\quad D<6,\quad K<\frac{12}{5},\quad
\sigma:=\inf X\cdot n>\frac34,
$$
$$
\frac{\operatorname{reach}(X)}D>\frac5{72}.
\tag{1.1}
$$

接尾统一选择
$$
T\ge9,\qquad 0<\ell\le\frac1{16},\qquad
L=3+2\ell,\qquad \gamma_0=\frac{\ell^2}{512}.
\tag{1.2}
$$
允许 R11 附录 A 的全部参数矩形
$|s|\le\gamma_0,\ 0\le u\le\gamma_0$，特别包含其真正的第四模匹配
曲线及全部共同好参数。在两端以 R11 的真实构造接尾，并选择其放大参数
$\Omega$ 满足原有全部参数门及
$$\boxed{\Omega\ge2^{360}.} \tag{1.3}$$
这个附加门只是一个方便的充分值，可继续增大 $\Omega$；不会改变核心
或破坏 R11 的匹配停时。全部几何常数对每个有限 $T\ge9$ 一致，
没有使用 $T$ 的上界；例如可取 $T=2^{24}$。仍须满足 R11 自身的
输入门，本文不以 (1.3) 代替那些与实际输入有关的条件。

所得闭背景 $\widetilde X$ 在整个双 bump 参数矩形上统一满足
$$
\boxed{\widetilde D<6,\qquad
 \widetilde K<\frac{10}{3},\qquad
 \widetilde\sigma>\frac34,\qquad
 \frac{\operatorname{reach}(\widetilde X)}{\widetilde D}>\frac1{20}.}
\tag{1.4}
$$
此外，全主体的 Gauss 曲率有更强的单侧界
$$G<\frac{100}{27}<4.$$
两端真平盘可选闭子盘的并集为 $H$，其内部非空，且
$$
\frac{\operatorname{diam}\widetilde X(H)}{\widetilde D}
>\frac{300}{961}>\frac15.
\tag{1.5}
$$
沿 R11 真匹配曲线，其全局非刚体无穷小场在 $H$ 上恒零。
本题允许握持区不连通，故这两个子盘可以共同作为该集合。

为避免符号混淆，核心势记 $Q=h''/h$；
connector 的控制量始终另记
$$\widetilde q=\omega'/\omega^2,\qquad \omega=h'/h.$$

## 2. 正性及核心上的新比较函数

记 $\mu=\sqrt2$。由
$$\frac13<\delta<\frac38,\qquad \frac73<A_4<\frac{19}{8}$$
以及 $g=\operatorname{sech}^{\delta}x$，有
$$
\frac{g''}{g}=\delta^2\tanh^2x-\delta\operatorname{sech}^2x,
\qquad
Q-\frac{g''}{g}=(2-\delta^2)\tanh^2x\ge0.
$$
在 $h$ 尚为正的区间，
$$
(h'g-hg')'=(2-\delta^2)\tanh^2x\,hg\ge0.
$$
因初值给 $h/g=1$、$(h/g)'=0$ 于零点，得到 $h/g\ge1$。
假如 $h$ 有首次零点，这个不等式与 $g>0$ 矛盾。因此 $h>0$
于全实轴，并由唯一性为偶函数。

在 $0\le x\le1$ 取这个背景专用的上比较函数
$$
H(x)=1-\frac{x^2}{6}+\frac{x^4}{5}.
$$
它为正，且由 $\tanh x\le x$ 得
$$Q=-\delta+A_4\tanh^2x\le-\delta+A_4x^2.$$
令 $t=x^2$，直接展开：
$$
H''-QH
\ge(1-t)\left[
 \delta-\frac13+
 \left(\frac1{15}-\frac{\delta}{6}\right)t+
 \frac{2+\delta}{5}t^2\right]\ge0.
\tag{2.1}
$$
其中三个括号系数均正；尤其
$1/15-\delta/6>1/240$。Wronskian
$(H'h-Hh')'=(H''-QH)h\ge0$ 给 $h\le H$。
$H$ 在此区间的最大值在端点，故
$$
h(x)\le\frac{31}{30}\qquad(0\le x\le1).
\tag{2.2}
$$

## 3. 负势面积、全局下界和 $h'(1)>0$

$Q$ 在正半轴严格增加，只过零一次。令
$$N=\int_0^\infty Q_-(x)\,dx.$$
由 $\tanh x\le x$，
$$
\bigl(\tanh x-x+x^3/3\bigr)'=x^2-\tanh^2x\ge0,
$$
因此在 $0\le x\le1/2$ 上，
$$\tanh x\ge x-x^3/3\ge(11/12)x.$$
于是
$$
Q(x)>-\frac38+\frac{15}{8}x^2
\qquad(0\le x\le1/2).
$$
因为 $(7/3)(11/12)^2=847/432>15/8$。在 $x=1/2$ 时右端
已为正，故单调性又排除更远处的负势。因而
$$
N<\int_0^{1/\sqrt5}\left(\frac38-\frac{15}{8}x^2\right)\,dx
=\frac1{4\sqrt5}<\frac18.
\tag{3.1}
$$
在 $Q<0$ 的整个区间，$h''<0$，所以 $h\le1$。
因此对全部 $x\ge0$，
$$h'(x)=\int_0^x Qh\ge-N.$$
积分给 $h>7/8$ 于 $[0,1]$。

另记
$$I=\int_0^1Q(x)\,dx=2-A_4\tanh1.$$
初等级数界 $8/3<e<11/4$ 给
$$\frac34<\tanh1<\frac{10}{13},$$
因而
$$
\frac9{52}<I<\frac14.
\tag{3.2}
$$
在正势部分用 $h>7/8$，在负势部分用 $h\le1$，得
$$
h'(1)>\frac78(I+N)-N
>\frac{63}{416}-\frac1{64}
=\frac{113}{832}>\frac18.
\tag{3.3}
$$
另一方面丢掉负项并用 (2.2) 给
$$h'(1)<\frac{31}{30}(I+N)<\frac{31}{80}<\frac25.
\tag{3.4}
$$
由 $\cosh1>3/2$，
$$
Q(x)\ge Q(1)>2-\frac{19}{8}\frac49=\frac{17}{18}>\frac89
\qquad(x\ge1).
\tag{3.5}
$$
所以 $h'$ 从 $x=1$ 起严格为正并增加。这证明了全局下界
$h>7/8$，而非仅在一个有限区间上的估计。

## 4. 闭面、半高和直径

令 $c=2\sqrt2/3$，则 $c^2=8/9$。由 (3.3)、(3.5) 及线性比较，
$$
h(1+t)\ge h(1)\cosh(ct)+\frac{h'(1)}c\sinh(ct)
>\frac78\cosh(ct)\qquad(t\ge0).
\tag{4.1}
$$
因此
$$
z_\infty
<\frac{64}{49}
+\frac{64}{49}\int_0^\infty\operatorname{sech}^2(ct)\,dt
=\frac{64}{49}\left(1+\frac3{2\sqrt2}\right).
$$
用 $\sqrt2>7/5$ 即得
$$z_\infty<\frac{928}{343}<\frac{11}{4}.$$
又 $a<8/7$，所以
$$
|X|^2=a^2+z^2<
\frac{64}{49}+\frac{121}{16}
=\frac{6953}{784}<9.
\tag{4.2}
$$
故 $D<6$。

为付清两极，令 $\omega=h'/h$。它在 $x\ge1$ 为正，满足
$\omega'=Q-\omega^2$，且从 $\omega(0)=0$ 的首次交叉论证给
$\omega<\sqrt2$。因 $Q\to2$，常数系数 Riccati 上下比较给
$\omega\to\sqrt2$。经线两端的弧长积分收敛；在上极点把 $z$
视为 $a$ 的函数，
$$
z_a=-\frac1{h'},\qquad
\frac{z_a}{a}=-\frac h{h'}\longrightarrow-\frac1{\sqrt2},
\qquad
z_{aa}=-\frac{h''h^2}{h'^3}\longrightarrow-\frac1{\sqrt2}.
$$
因此旋转图的 Cartesian Hessian 在轴上连续趋于
$-I/\sqrt2$。补点是正则 $C^2$ 图。下极点由反射给出。
$z$ 严格增加，内部每个高度只有一个圆，故闭面嵌入。

## 5. 曲率界

两个主曲率准确为
$$
\kappa_\theta=\frac h p,\qquad
\kappa_s=\frac{h^2h''}{p^3}
=Q\left(\frac h p\right)^3.
\tag{5.1}
$$
在 $[0,1]$，$|Q|<2$ 和 (2.2) 给
$$
|\kappa_\theta|\le\frac{31}{30},\qquad
|\kappa_s|<2\left(\frac{31}{30}\right)^3<\frac{12}{5}.
$$
在 $x\ge1$，令 $E=h'^2-c^2h^2$，则
$$E'=2h'(Q-c^2)h>0.$$
并且
$$
E(1)>-c^2h(1)^2
\ge-\frac89\left(\frac{31}{30}\right)^2
=-\frac{1922}{2025}>-1.
$$
所以 $p^2=1+h'^2>c^2h^2$，进而
$$
\kappa_\theta<\frac1c=\frac3{2\sqrt2},\qquad
|\kappa_s|<\frac2{c^3}=\frac{27}{8\sqrt2}<\frac{12}{5}.
\tag{5.2}
$$
末个有理比较等价于 $\sqrt2>45/32$，平方即可验证。
偶性给下半面，两极由连续性覆盖，故 $K<12/5$。

## 6. 支撑函数的三个区间

外法向给
$$
X\cdot n=\frac{a+zh'}{\sqrt{1+h'^2}}.
\tag{6.1}
$$
先在 $0\le x\le1$：

- 若 $h'\le0$，则 $|h'|<1/8$、$z<64/49<4/3$、
  $a\ge30/31>15/16$。又
  $p<49/48$，因为 $p^2<65/64<2401/2304$。
  因此
  $$X\cdot n>
  \frac{15/16-(4/3)(1/8)}{49/48}
  =\frac{37}{49}>\frac34.$$
- 若 $h'\ge0$，则 $h'\le h'(1)<2/5$。
  这里 $Q$ 只过零一次，$h'$ 在该零点前下降、之后增加，
  所以上界确实成立。于是 $p<11/10$，
  $$X\cdot n\ge a/p>\frac{15/16}{11/10}
  =\frac{75}{88}>\frac34.$$

在 $x\ge1$，由 (2.2)
$$
z(x)\ge z(1)=\int_0^1h^{-2}\,dx\ge\frac{900}{961}=:\zeta_1.
$$
令 $t=h'/p\in(0,1)$。由 (5.2) 的 $p/h>c$，
$$
X\cdot n=\frac1{hp}+zt
>c(1-t^2)+\zeta_1t.
$$
右端是 $[0,1]$ 上的凹二次函数，故不小于两端值中的较小者
$\min(c,\zeta_1)>3/4$。另一半面相同，因此
$\sigma>3/4$ 为全局界。

## 7. Reach 包含全局双点控制

这里使用的是已经在本题
[R1 第 3.2 节](../results/R1-explicit-geometric-neighborhood.md)
写明的正支撑 offset 论证，而非“曲率有界就有 reach”的局部推断。

具体地，若闭嵌入球面有 $X\cdot n\ge\sigma>0$ 且
$\|A\|\le K$，则对每个
$|t|<\min(\sigma,1/K)$，法向偏移 $X_t=X+tn$ 的微分可逆，
且 $X_t\cdot n\ge\sigma-|t|>0$。径向投影
$X_t/|X_t|:S^2\to S^2$ 是局部微分同胚，依紧性成为覆盖，
再由 $S^2$ 单连通得到它是全局微分同胚。
所以每个 $X_t$ 是一个径向图。固定径向方向沿 $t$ 求导，
其半径导数等于 $1/(n\cdot e_r)>0$，因此不同 $t$ 的径向图
严格嵌套。法向管整体单射，给
$$\operatorname{reach}(X)\ge\min(\sigma,1/K).$$
本背景的两个下界都严格大于 $5/12$，因而 reach 严格大于
$5/12$，再用 $D<6$ 得 $5/72$ 的比例。

## 8. 全部共同切点 $T\ge9$ 的明确输入

本节先证明所有 $T\ge5$ 都具有所需几何输入，再取 (1.2)，以同时保留
R13 所需的未改屏障。由 $\cosh2>11/3$，
$$
Q(x)>2-\frac{19}{8}\frac9{121}>\frac74\qquad(x\ge2).
$$
令 $c_2=\sqrt7/2>13/10$。因 $\omega(2)>0$，Riccati 比较给
$$
\omega(x)>c_2\tanh(c_2(x-2))\qquad(x\ge2).
$$
由 $e>27/10$ 得 $e^4>51$，所以 $\tanh2>25/26$；
因此
$$\frac54<\omega(x)<\sqrt2\qquad(x\ge4). \tag{8.1}$$
另由 (4.1)，
$$
h(5)>\frac78\cosh(4c)>
\frac78\cosh(7/2)>10.
$$
末个不等式可直接用
$\cosh(7/2)>1+49/8+2401/384=5137/384$ 验证。
所以在任意 $T\ge9$ 处
$$
a_0<\frac1{10},\qquad
\frac54<\omega_0<\sqrt2,\qquad
z_0\ge\frac{900}{961}=:\zeta_1.
\tag{8.2}
$$
由 $0<Q<2$，
$$-1<\widetilde q_0=Q/\omega_0^2-1<7/25<1.$$
而真实第四模的
$$R_0=-\frac{\sqrt2\tanh T}{4\omega_0}$$
严格位于 $(-3/10,-1/5)$：上、下估计分别用
$\omega_0<\sqrt2$、$\omega_0>5/4$ 及 $\tanh T>4/5$。
这给 R11 §3 的全部真实输入。

双 bump 区的左端
$$B=T-L\ge9-\frac{25}{8}=\frac{47}{8}>5.$$
因此它不侵入未改核心 $[0,5]$，也与 R13 的共同选择兼容。

## 9. 双 bump 的曲率、支撑及高度费用

写
$$
\zeta=s\phi_1+u\phi_2,\qquad \widehat h=h e^\zeta,
\qquad |s|\le\gamma_0,\quad0\le u\le\gamma_0.
$$
两个支持不相交。R7 的具体 quintic 导数界逐点给
$$
|\zeta|\le\gamma_0\le2^{-17},\qquad
|\zeta'|\le\frac{15\ell}{1024}<\frac1{1000},\qquad
|\zeta''|\le\frac3{16}.
\tag{9.1}
$$
于是
$$
\widehat\omega=\omega+\zeta'>\frac65,\qquad
\widehat Q=Q+\zeta''+2\omega\zeta'+(\zeta')^2,
$$
$$
|\widehat Q-Q|<
\frac3{16}+\frac3{1000}+\frac1{10^6}<\frac15.
\tag{9.2}
$$
这里用了 (8.1) 的 $\omega<\sqrt2<3/2$。
故整个区间 $[B,T]$，包括两个支持之间的空隙，都有
$$
\widehat a<\frac{e^{\gamma_0}}{10}<\frac19,\qquad
\widehat\omega>\frac65,\qquad
|\widehat Q|<\frac{11}{5}.
$$
直接使用准确曲率公式给
$$
|\widehat\kappa_\theta|\le\frac1{\widehat\omega}<\frac56,
\qquad
|\widehat\kappa_s|
\le\frac{|\widehat Q|}{\widehat\omega^3}
<\frac{275}{216}<\frac{12}{5}.
\tag{9.3}
$$
在这段上 $\widehat z\ge z(1)\ge\zeta_1$，所以
$$
\widehat X\cdot\widehat n
\ge\frac{\zeta_1}{\sqrt{1+(\widehat a/\widehat\omega)^2}}
>\frac{\zeta_1}{11/10}>\frac34.
\tag{9.4}
$$
更早部分完全未改，仍有第 5—6 节的界。

高度差只在两个支持上产生。由 $h>10$、总支持长度 $2\ell\le1/8$，
以及 $e^{2\gamma_0}-1<3\gamma_0$，
$$
|\widehat z(T)-z(T)|
\le\int_{\operatorname{supp}\zeta}h^{-2}|e^{-2\zeta}-1|\,dx
<\frac{3\gamma_0}{800}<\frac1{10000}.
\tag{9.5}
$$
$\zeta,\zeta',\zeta''$ 在外端全为零，故 (8.2) 的 $a_0,\omega_0$
和 $\widetilde q_0$ 完全不变；外端高度只增加上述已付的平移量。
特别，接尾开始时仍有 $z_0\ge\zeta_1$，且
$z_0<11/4+1/10000$。

## 10. 有限 connector 的全过程几何

用 R11 的 $t=\log(h/h_0)$ 参数，
$$
\omega_t=\widetilde q\omega,\qquad a=a_0e^{-t},
\qquad z_t=a^2/\omega.
\tag{10.1}
$$
准确旋转公式为
$$
\kappa_\theta=\frac1{\sqrt{a^2+\omega^2}},\qquad
\kappa_s=\frac{(1+\widetilde q)\omega^2}
 {(a^2+\omega^2)^{3/2}},
$$
$$
X\cdot n=\frac{a^2+z\omega}{\sqrt{a^2+\omega^2}}.
\tag{10.2}
$$
因此曲率不含未付的 $h$ 大因子。

R11 的短过渡长度为 $\eta=2^{-24}$。全部准备段满足
$-1\le\widetilde q\le2$，其中 $\widetilde q=-1$ 的主段长度小于
$\log(11/8)$，另有两个长度 $\eta$ 的过渡。因此在每个中间点
$$
\omega>\frac54e^{-\log(11/8)-2\eta}
=\frac{10}{11}e^{-2\eta}
>\frac{10}{11}\frac{99}{100}=\frac9{10}.
\tag{10.3}
$$
这里 $e^{-2\eta}\ge1-2\eta>99/100$。
随后 $\widetilde q=2$ 的放大段使 $\omega$ 增加。
所以准备和放大全过程由 (10.2) 得
$$
|\kappa_\theta|<10/9,\qquad
|\kappa_s|<10/3.
\tag{10.4}
$$

末端两过渡及中间 $\widetilde q=-1$ 段，由 R11 §5 的实际停时
小于 $\log(9/8)$，每个前缀均满足
$$
\omega>\frac89e^{-9\eta}\Omega>\frac45\Omega.
$$
这不是只在最终点的估计：任何前缀的负积分都不超过
$\log(9/8)+9\eta$。该段 $-8\le\widetilde q\le2$，故
$$
|\kappa_\theta|\le\frac5{4\Omega},\qquad
|\kappa_s|\le\frac{35}{4\Omega}<1
\tag{10.5}
$$
由 (1.3) 得最后一步。特别，整个有限 connector 都有 $\omega>9/10$。

支撑的统一下界直接由 $z\ge z_0\ge\zeta_1$、$a\le a_0<1/10$：
$$
X\cdot n\ge
 \frac{\zeta_1}{\sqrt{1+(a_0/(9/10))^2}}
>\frac{\zeta_1}{11/10}>\frac34.
\tag{10.6}
$$
其高度增量不论总放大时间多长，都有
$$
\Delta z_{\rm con}
<\frac{10}{9}\int_0^\infty a_0^2e^{-2t}\,dt
=\frac59a_0^2.
\tag{10.7}
$$
放大参数极大不会破坏这个界。

## 11. 真实 R72 无限平尾的全 profile 估计

本节的 $\delta_*=\delta_{128}=(2/25)2^{-128}$ 与第 2—7 节的
$\delta_4$ 无关。令
$$
b=r_{128}\in(1,2),\qquad
\overline W_b=\frac{\delta_*^6}{b^7}.
$$
R72 §2 给每个实际胞元
$$
\overline W(\bar r)=\frac{\delta_n^6p_*(\bar r)}{\bar r^7},
\qquad
1\le\bar r\le2,\qquad \delta_n\le\delta_*,
$$
$$
p_*:\quad1,\quad64/\delta_n,\quad\delta_n/\alpha,\quad
1/\delta_n,\quad64,\qquad \alpha=65/64.
\tag{11.1}
$$
四个 log-quintic 过渡的 $y$ 长度是
$\eta_n=\delta_n^{3/2}/(4\sqrt2)$，且
$d\bar r/dy=\bar r/\sqrt{12}$。
最大 log 跳幅不超过 $\log65+2|\log\delta_n|$。
用 $|S'|\le15/8$，得到
$$
\left|\frac{d\log p_*}{d\bar r}\right|
\le15\sqrt6\,\delta_n^{-3/2}
    \bigl(\log65+2|\log\delta_n|\bigr).
\tag{11.2}
$$
并且
$$\overline W\le64\delta_n^5.$$
因此
$$
|\overline W_{\bar r}|
\le448\delta_n^5+
960\sqrt6\bigl(\log65+2|\log\delta_n|\bigr)\delta_n^{7/2}.
\tag{11.3}
$$
该估计也覆盖所有常平台；在端点由连续性覆盖。

因为 $\log65<5$、$|\log\delta_n|>1$、$\sqrt6<5/2$，
右端严格小于
$2^{14}(1+|\log\delta_n|)\delta_n^{7/2}$。
函数 $(1+|\log d|)d^{7/2}$ 在 $0<d<1$ 递增。
故整个无限尾，包括极限平区，都满足
$$
\boxed{
M_{\rm tail}:=
\sup\max\left\{\frac{\overline W(\bar r)}{\bar r},
                 |\overline W_{\bar r}(\bar r)|\right\}
\le2^{14}(1+|\log\delta_*|)\delta_*^{7/2}.}
\tag{11.4}
$$
这是完整真实过渡层的估计。没有把切口的
$\bar r\overline W_{\bar r}/\overline W=-7$
延用到过渡内部。

现在用 R11 的准确物理缩放。记末端 $H_e=h_e$，则
$$
\rho=\frac1{H_eb},\qquad
\lambda=\frac1{H_e^2b\omega_e\overline W_b},\qquad
z(r)=\lambda\bar z(r/\rho)+z_{\rm shift}.
$$
物理坡度及其导数满足
$$
W(r)=\frac\lambda\rho\overline W(r/\rho),\qquad
W_r(r)=\frac\lambda{\rho^2}\overline W_{\bar r}(r/\rho),
\qquad
\boxed{\frac\lambda{\rho^2}
=\frac{b}{\omega_e\overline W_b}.}
\tag{11.5}
$$
特别，这个二阶缩放量独立于 $H_e$；不能用 $\lambda$ 单独估计曲率。

由 $\omega_e>4\Omega/5$，
$$
\frac\lambda{\rho^2}M_{\rm tail}
<
\frac{5\,2^{12}b^8(1+|\log\delta_*|)\delta_*^{-5/2}}{\Omega}.
\tag{11.6}
$$
$\delta_*>2^{-132}$、$\log2<7/10$ 给
$|\log\delta_*|<93$。用 $b<2$，上式分子小于
$$
5\cdot2^{20}\cdot94\cdot2^{330}
=470\cdot2^{350}<2^{359}.
$$
因此 (1.3) 保证
$$
\frac{W(r)}r<1,\qquad |W_r(r)|<1
\tag{11.7}
$$
于整个物理无限尾。径向图 $z_r=-W$ 的两主曲率是
$$
\frac{W}{r\sqrt{1+W^2}},\qquad
\frac{W_r}{(1+W^2)^{3/2}},
$$
故绝对值均小于 $1$。真平区的曲率为零，R72 §9.2 的 $C^2$ 平坦
极限保证接合正则；不要求退化 Sturm 坐标一直延伸到盘心。

记有限 connector 的末端半径为 $r_e=1/H_e\le a_0$。
由 (11.7)，真实尾的高度增量满足
$$
\Delta z_{\rm tail}
=\int_{r_{\rm flat}}^{r_e}W(r)\,dr
\le\frac{r_e^2-r_{\rm flat}^2}{2}
<\frac12a_0^2.
\tag{11.8}
$$
这里 $r_{\rm flat}>0$ 是物理平坦极限半径；再向盘心的平区没有高度
增量。法向支撑则满足
$$
X\cdot n=\frac{z+rW}{\sqrt{1+W^2}}
\ge\frac{\zeta_1}{\sqrt{1+a_0^2}}
>\frac{\zeta_1}{11/10}>\frac34.
\tag{11.9}
$$
平盘上的支撑为其高度，同样大于 $\zeta_1$。

## 12. 拼接后的直径、全局 reach 和握持尺寸

R11 已证明实际背景与无穷小场的完整二阶 jet 匹配；
第 9 节的 bump 也保持端点二阶 jet。经线在正端的所有新部分半径
严格减小、高度严格增加，随后接水平盘；负端镜像。因此所得曲面
仍为闭 $C^2$ 嵌入。

第 5、9、10、11 节共同给
$$\widetilde K<10/3,\qquad \widetilde\sigma>3/4.$$
全部新部分的半径小于 $1/9$，因此全局半径仍小于 $8/7$。
每一侧的最大高度由 (9.5)、(10.7)、(11.8) 控制：
$$
z_{\max}<
\frac{11}{4}+\frac1{10000}
+\left(\frac59+\frac12\right)\frac1{100}
=\frac{11}{4}+\frac1{10000}+\frac{19}{1800}
<\frac{277}{100}.
$$
于是
$$
\sup|\widetilde X|^2<
\frac{64}{49}+\frac{76729}{10000}
=\frac{4399721}{490000}<9,
$$
即 $\widetilde D<6$。第 7 节的全局法向管论证再次适用，给
$$
\operatorname{reach}(\widetilde X)>
\min\left\{\frac34,\frac3{10}\right\}
=\frac3{10},\qquad
\frac{\operatorname{reach}(\widetilde X)}{\widetilde D}>\frac1{20}.
$$

还可直接付清供固定曲率标记使用的 Gauss 上界。
主干准确有 $G=Q(h/p)^4$，bump 处同样使用
$G=\widehat Q/(\widehat a^2+\widehat\omega^2)^2$；
connector 则有
$$G=\frac{(1+\widetilde q)\omega^2}{(a^2+\omega^2)^2}.$$
负 Gauss 区域自动满足上界，正区域逐段估计如下：

| 区域 | Gauss 曲率上界 |
|---|---:|
| 未改核心 $0\le x\le1$ | $2(31/30)^4<100/27$ |
| 未改尾 $x\ge1$ | $2(9/8)^2=81/32<100/27$ |
| 双 bump | $(11/5)/(6/5)^4=1375/1296<100/27$ |
| 准备及放大 | $3/(9/10)^2=100/27$，严格小于 |
| 末端过渡及实际 R72 全尾 | $|G|<1$ |
| 平盘 | $G=0$ |

所以整个同一闭背景统一满足
$$\boxed{G<100/27<4.}$$
这比从主曲率平方得到的粗界更强，但仍只针对本文实际背景；
未来有限幅校正后的 Gauss 曲率须另外转移或验证。

在两个真平盘内各取半径为该平盘半径一半的闭子盘，令 $H$ 为其
参数原像的并集。这是闭集且内部非空。两盘心的距离至少为
$2\zeta_1=1800/961$，所以
$$
\frac{\operatorname{diam}\widetilde X(H)}{\widetilde D}
>\frac{1800/961}{6}=\frac{300}{961}>\frac15.
$$
沿 R11 的真实第四模匹配曲线，$Z$ 在整片平盘上为零；
特别 $Z|_H=0$，并非只在两极点上为零。

## 13. 对主目标的使用范围

已经付清的是同一个实际对象的几何：新主干、双 bump、
有限 connector、R72 全部无限过渡层和两个真平盘。
增大 $\Omega$ 同时满足 R11 的原输入门及 (1.3)，所以本几何结论
不与其第四模线性匹配或尾高度规范发生冲突。

此处的 $H$ 尺寸及无穷小固定性是实际成立的。尚没有一族有限幅
$F_t$ 在同一精确度量下保持该 $H$，也没有证明
$\delta_{\rm hold}\ge0.05D$ 或 $\delta_{\rm E}>0$。
将一个线性尾输入送入 R72 的非线性图后，高模两迹和 mean 的输出
仍须与同一个核心—connector 算子联立处理；本文只消除了该正向路线
上的背景厚度、真实平帽和握持尺寸缺口。
