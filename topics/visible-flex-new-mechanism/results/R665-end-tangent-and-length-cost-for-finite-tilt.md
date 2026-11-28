# R665：真实有限倾斜、法管厚度和经线两端转向的联合长度

2026-11-28。对 R655、R659 的两斜平帽，在 [R657](R657-sharp-inner-radius-and-wide-adjacent-morse-kernels.md) 的径向弦外，还必须支付有界主曲率的端切向转动。此门只看固定度量和真实帽姿；一对相反母线可以完全消去未知水平、竖直平移。把经线长设置为裸弦超额的 $1.01$ 倍，对于 $a\le .1,b=.22,\sin\vartheta=.36,T=.03$ 的整个精确设计均不够。另一方面，R659 的真实拱形参考经线长对各方位独立的曲率受限两点两切向问题留有正余量。

## 1. 固定旋转度量的真实空间测地线

设真实 $C^2$ 圆环对 $g=E(r)dr^2+r^2d\varphi^2$ 等距，$E>0$，与两个标准平圈至少一阶匹配。令 $s=\int_a^r\sqrt E\,dr$，$S=s(b)$。因 $g=ds^2+r(s)^2d\varphi^2$，$\Gamma^s_{ss}=\Gamma^\varphi_{ss}=0$，每条固定 $\varphi$ 的 $r$ 线用 $s$ 参数是单位速测地线。其空间速度 $P$ 单位，空间加速度纯法向，故若 $\max_i|\kappa_i|\le1/T$，则 $|P'|\le1/T$。在要求真实开 $T$ 法管的一般 $C^2$ 实体上，曲率界本身也是 reach 的必要条件。此处 $T=.03$ 是 [R655](R655-offset-rigid-cap-and-thick-inner-hold.md) 采用的物理单位厚度。

对任一单位方向 $e$，设两个空间端切向与 $e$ 的球面角距为 $A,B\in[0,\pi]$。离起点弧长 $s$ 处的角距至少 $\max(0,A-s/T,B-(S-s)/T)$，因为端切向的球面路长至多为曲线经过的弧长除以 $T$。在 $S\ge T(A+B)$ 时，端点支持的两段长度 $TA,TB$ 不重叠，沿经线积分 $P\cdot e$ 得
$$
 e\cdot [F(b)-F(a)]\le S-T[q(A)+q(B)],\qquad q(v)=v-\sin v.       \tag{1}
$$
不满足分段条件时，仍可直接积分上述三项的最大值所给的余弦上界。不能在重叠处重复扣长度。只用一端时，仅需 $S\ge TA$ 即可单扣 $Tq(A)$。

## 2. 两条相反经线消去任意平移

取外框的 $x,z$ 平面。正材料径向的外、内端切向分别 $p=(1,0)$、$q_i=(\cos\vartheta,-\sin\vartheta)$。相反材料径向端切向为它们的负向。设内中心在外框的任意空间位置为 $C$。两经线从内到外的空间位移分别为 $D_0-C,-D_0-C$，其中
$$
D_0=bp-aq_i=(b-a\cos\vartheta,a\sin\vartheta),\quad L=|D_0| .
$$
选 $e_\beta=(\cos\beta,\sin\beta)$ 并在相反经线上选 $-e_\beta$，让 $0\le\beta\le\pi-\vartheta$。两条线的起、终端角距分别都为 $\vartheta+\beta,\beta$，故 (1) 的右端相同；左端的较大者是 $D_0\cdot e_\beta+|C\cdot e_\beta|$。准确必要式为
$$
 S\ge D_0\cdot e_\beta+|C\cdot e_\beta|
       +T[ q(\vartheta+\beta)+q(\beta)],\qquad
 S\ge T(\vartheta+2\beta).                                      \tag{2}
$$
后一项是施用门槛。令 $\gamma=\arg(D_0)$ 得消去全部中心平移的特例
$$
\boxed{S\ge L+T[q(\vartheta+\gamma)+q(\gamma)] .}              \tag{3}
$$
给定真实中心时，(2) 可加回其非负项。对斜测地线的两个真实端切向也可直接用 (1)。

**排除恒定百分之一裸弦超额设计。** 令 $0<a\le.1,b=.22,T=.03,\sin\vartheta=.36$。$L\ge b-a\ge.12$，$\cos\vartheta>.93,\vartheta<.37$，且 $\gamma\le a\sin\vartheta/(b-a)\le.3$，故 $T(\vartheta+2\gamma)<.03<S$ 对所有满足裸弦的设计成立。此时
$$
 L-(b-a)=\frac{2ab(1-\cos\vartheta)}{L+b-a}
 \le \frac{(.1)(.22)(.07)}{.12}<.01284 .
$$
把 $S=(b-a)+1.01(L-b+a)$ 作为精确定义，仅留 $S-L<.000129$。而由 $\arcsin y-y\ge y^3/6$，
$$
Tq(\vartheta+\gamma)\ge .03(\arcsin(.36)-.36)
\ge .03(.36)^3/6>.000233 .
$$
所以任何中心的这种精确设计已经不可能有厚度 $.03$ 的指定姿态。该论证只用端姿、固定 $S$ 和法曲率。R657 真实 run 的已保留最宽 $a=.09840949$，但实际目标是通过浮点积分设高度尺度，$S$ 本身未有连续包围；其积分读数与新门的差是后继重新选择弧长的依据，不能称该 run 的每个浮点输入已获严格排除。

## 3. R659 拱形输入的正长度余量

固定 $a=.075,b=.22,\sin\vartheta=.36,C=0$。一般方位 $\varphi$ 的两端单位径向切向 $p=e_r(\varphi),q_i=R_y(\vartheta)p$ 张成一个平面，其夹角 $\alpha$ 满足 $\cos\alpha=1-(1-\cos\vartheta)\cos^2\varphi$，故 $0\le\alpha\le\vartheta$。在此平面中，坐标可取 $p$ 角零、$q_i$ 角 $-\alpha$，$D=bp-aq_i$。这里只解决每个方位独立的空间端点和端切向，不假定这些曲线已经构成同度量浸入。

有一个实际曲率受限的弧—直—弧曲线从内圈到外圈：第一段以半径 $T$ 从切角 $-\alpha$ 转至 $\beta$，直段长 $\ell$，末段以同半径从 $\beta$ 转回零。要求总位移为 $D$。记
$$
 f(\beta)=D\cdot(-\sin\beta,\cos\beta)
           +T[2-\cos(\beta+\alpha)-\cos\beta].
$$
$f(0)\ge0$。因 $D_x\ge .145,D_z\le .027,\alpha<.37$，$\sin(.25)>.247$ 和 $1-\cos x\le x^2/2$ 给
$$
 f(.25)<-.145(.247)+.027+(.03/2)(.62^2+.25^2)<0 .
$$
故可取 $\beta\in[0,.25)$ 使 $f(\beta)=0$。两圆弧在 $e_\beta^\perp$ 上的位移之和恰为 $-T[2-\cos(\beta+\alpha)-\cos\beta]$；$f=0$ 已匹配这一分量。设
$$
\ell=D\cdot e_\beta-T[\sin(\beta+\alpha)+\sin\beta]>0 ,
$$
其正性由 $.145\cos(.25)-.03(.62+.25)>0$ 得出，另一个分量也准确匹配。总长
$$
 S_{\rm path}=D\cdot e_\beta+T[q(\beta+\alpha)+q(\beta)]
 \le L+(.03/6)(.62^3+.25^3)< L+.00128 .                     \tag{4}
$$
使用了 $|D|\le L$ 与 $q(v)\le v^3/6$。当 $\alpha=0$ 也可直接取平直段。两圆弧与直段为 $C^{1,1}$，其曲率处处在通常几乎处处意义下不超过 $1/T$。这也给该独立两点两切向问题的最短长度：任何更短但尚满足裸弦的曲线长至少 $b-a=.145>T(\alpha+2\beta)$，故应用 (1) 于同一 $e_\beta$ 给 $S\ge S_{\rm path}$。这里只作长度门支付，不把这条拼弧自身当成所求 $C^2$ 闭面。

[R659 的有符号双坡参考](../notes/2026-11-28-r659-direct-finite-tilt-latitude-scope.md)有
$$
 S_{\rm seed}\ge .145[1+(4/9)(128/385)(.72)^2]>.155 .
$$
相反 $L^2=.145^2+2(.075)(.22)(1-\cos\vartheta)<.145^2+2(.075)(.22)(.07)<(.153)^2$，故 (4) 给 $S_{\rm path}<.15428$，在全部方位留正的长度余量。非零体场、实际中心和设计度量均可改变 $S$，应在实际有限角输出上使用 (1)–(3) 而非沿用种子值。本文没有把相互独立的母线极值当成二维法向、纬圈长度、同一旋转度量或全局法管的证明。
