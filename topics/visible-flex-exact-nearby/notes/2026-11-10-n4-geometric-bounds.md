# $n_*=4$ 未改主干的独立几何界

2026-11-10，geometry-transfer。

本文只处理新的未接尾旋转背景
$$
\delta=\frac{\sqrt2}{4},\qquad A_4=2+\delta,\qquad
Q(x)=2-A_4\operatorname{sech}^2x,\qquad
h''=Qh,\quad h(0)=1,\ h'(0)=0.
$$
为避免和 connector 文稿的 $q=\omega'/\omega^2$ 混淆，此处把
$h''/h$ 记作 $Q$。以下常数全部对这个 $n_*=4$ 背景重新证明，
不从 R5 的 $n_*=3$ 数据转授。

## 1. 结论

置
$$
a=h^{-1},\qquad z(x)=\int_0^x h^{-2},\qquad
X=a e_r+z e_z,\qquad p=\sqrt{1+h'^2}.
$$
两端补点后得到闭 $C^2$ 嵌入球面，且
$$
h>\frac78,\qquad z_\infty<\frac{11}{4},\qquad
\sup|X|<3,\qquad D<6,
$$
$$
K:=\sup\max\{|\kappa_\theta|,|\kappa_s|\}<\frac{12}{5},
\qquad
\sigma:=\inf X\cdot n>\frac34.
$$
由正支撑的全局 offset 论证，
$$
\boxed{\operatorname{reach}(X)>\frac5{12},\qquad
       \frac{\operatorname{reach}(X)}D>\frac5{72}>\frac3{100}.}
$$
这里最后一项并非仅由曲率推出；全局两点不碰撞由第 7 节说明。

还会得到方便接尾的界：在 $x\ge1$，
$$
h'>0,\qquad z\ge\frac{900}{961},\qquad
\frac h{\sqrt{1+h'^2}}<\frac3{2\sqrt2}.
\tag{1.1}
$$
本文没有证明非线性弯曲，也没有把接尾后的曲面自动纳入以上数值。

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

## 8. Connector 几何可直接使用的公式

此节只登记公式，不替代对实际 connector 的控制区间证明。
在正半面令 $\omega=h'/h>0$，
$\widetilde q=\omega'/\omega^2$，并仍写 $a=1/h$。
则
$$
\kappa_\theta=\frac1{\sqrt{a^2+\omega^2}},\qquad
\kappa_s=\frac{(1+\widetilde q)\omega^2}
 {(a^2+\omega^2)^{3/2}},
$$
$$
X\cdot n=\frac{a^2+z\omega}{\sqrt{a^2+\omega^2}},\qquad
\frac{dz}{d(\log h)}=\frac{a^2}{\omega}.
\tag{8.1}
$$
所以若从某个 $a_0$ 开始的全部接尾区已另证
$\omega\ge\omega_*>0$ 和 $-8\le\widetilde q\le2$，则
$$
K_{\rm connector}\le\frac7{\omega_*},\qquad
\sigma_{\rm connector}\ge
 \frac{z_0}{\sqrt{1+(a_0/\omega_*)^2}},
\qquad
\Delta z\le\frac{a_0^2}{2\omega_*}.
\tag{8.2}
$$
最后一个积分假设该参数区一直到 $a=0$；有限 connector 的高度增量
只会更小。若真平尾以另外的径向坐标表示，则须对它另行证明相应曲率、
支撑和高度界，不能只凭有限 connector 的控制范围跨过接缝。

这些公式解释了为什么在足够远的帽上先把 $\omega$ 放大，再进行
$\widetilde q=-8$ 的匹配，有机会同时付清厚度与正支撑。
实际最低 $\omega$、停时长度及真尾尺度由接尾构造另外给定。



完整登记及真实平尾、双 bump 的统一几何见 [R14](../results/R14-mode-four-full-tail-geometric-bounds.md)。R14 对全部有限切点 T≥9 统一成立，并已将接后 reach/D 下界提高到 1/20。
