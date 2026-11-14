# R10：双高度模、投影折叠与精确周期嵌入环带

**状态：已证明的正向中间结论；主目标未完成。**

## 命题

存在 $\ell>0$ 及实解析嵌入
$$
F:[-\ell,\ell]\times(\mathbb R/2\pi\mathbb Z)\longrightarrow\mathbb R^3
$$
满足
$$
F^*\langle\cdot,\cdot\rangle=dr^2+a(r)^2d\theta^2,\qquad
F_3=a(r)\{\cos\theta+b(r)\cos^3\theta\}.
\tag{1}
$$
函数 $a,b$ 由下述四维有理 ODE 及明确的有理初值
$$
(a,\mu,b,p)(0)=(1,0,-1/10,1/100),\qquad
\mu=a'/a,\quad p=b'
\tag{2}
$$
确定。该环带不是任何轴的旋转曲面，亦非极小曲面；
完整角向单值性由两个垂直反射平面自动保证，无待解的周期方程。

初始截面 $\Gamma=F(\{0\}\times S^1)$ 的 $YZ$ 投影严格凸且简单。
适当选择坐标后，
$$
\max_\Gamma Z=9/10,\qquad
\max_\Gamma Y>1079/1000,\qquad
\operatorname{diam}\Gamma<311/100.
\tag{3}
$$
它与绕 $X$ 轴转 $\pi/2$ 后的像的 Hausdorff 距离大于 $179/1000$；
缩小 $\ell$ 后，整个带的相应刚体转动也有超过直径 $5\%$ 的像位移。

这里解决的是完整非线性方程，不是 Fourier 截断方程。
但这仍是带边模块：没有固定旋转开领圈、闭曲面或题定 reach 下界。
上述整体转动是刚体运动，$\delta_E=0$，不能计作本题要求的握持弯曲。

## 1. 完整 Darboux 方程的四维 ODE

记
$$
c=\cos\theta,\quad s=\sin\theta,\quad y=c^2,\quad
K=-a''/a,\quad \xi=b''+2\mu b'.
$$
以下 $A,B,C,D$ 均为标量，$C$ 不是第二基本形式：
$$
\begin{aligned}
A&=a^2\mu^2+6b-1,\\
B&=a^2\mu p+b(a^2\mu^2-9),\\
C&=a^2\mu p+b(3b+4),\\
D&=a^2p(p+b\mu),\qquad \Delta=AD-BC.
\end{aligned}\tag{4}
$$
在 $\Delta\ne0$ 的开集上使用
$$
\begin{aligned}
a'&=a\mu,& \mu'&=-K-\mu^2,& b'&=p,& p'&=\xi-2\mu p,\\
K&=-\frac{9p^2(A+B)}{\Delta},&
\xi&=\frac{9p^2(C+D)}{\Delta}.
\end{aligned}\tag{5}
$$
为检查所有角频，设 $z=a(c+bc^3)$。
在正交标架 $(\partial_r,a^{-1}\partial_\theta)$ 下，
$$
\begin{aligned}
z_r&=ac\{\mu+(p+\mu b)y\},&
a^{-1}z_\theta&=-s(1+3by),\\
(\nabla^2z)_{11}&=ac\{-K+(\xi-Kb)y\},\\
(\nabla^2z)_{12}&=-3p\,s\,c^2,\\
(\nabla^2z)_{22}&=\frac c a(A+By).
\end{aligned}\tag{6}
$$
同时 $1-|\nabla z|^2=c^2R(y)$，其中
$$
\begin{aligned}
R(y)={}&1-6b-a^2\mu^2\\
&+\{6b-9b^2-2a^2\mu(p+\mu b)\}y\\
&+\{9b^2-a^2(p+\mu b)^2\}y^2.
\end{aligned}\tag{7}
$$
完整 Darboux 恒等式
$\det_g\nabla^2z=K(1-|\nabla z|^2)$ 除去公共因子 $c^2$
后是 $y$ 的二次多项式。常数项自动相消，其余两项恰为
$$
A\xi+CK=9p^2,\qquad B\xi+DK=-9p^2.
\tag{8}
$$
求解此二阶线性系统即得 (5)，因此没有遗漏高角频。

## 2. 在投影折叠线上重建真实曲面

当 $R(y)>0$ 对 $0\le y\le1$ 成立时，选择有符号法向高度
$$
\nu=c\sqrt{R(c^2)}.
$$
不能将它换成 $|c|\sqrt R$。定义对称张量 $h$ 的正交标架分量
$$
h_{11}=\frac{a\{-K+(\xi-Kb)y\}}{\sqrt R},\quad
h_{12}=-\frac{3p\,s\,c}{\sqrt R},\quad
h_{22}=\frac{A+By}{a\sqrt R}.
\tag{9}
$$
它们在 $c=0$ 处仍解析，且
$$
\nabla^2z=\nu h,\qquad |\nabla z|^2+\nu^2=1,\qquad \det_g h=K.
\tag{10}
$$
最后一式先在 $c\ne0$ 处由 Darboux 方程得到，再由连续性延拓。

还须检查 Codazzi。令 $S$ 为 $h$ 的自伴算子，$v=\nabla z$。
在 $\nu\ne0$ 处微分 $|v|^2+\nu^2=1$ 得
$d\nu(X)=-\langle SX,v\rangle$。交换 $\nabla v=\nu S$ 的协变微分得
$$
\nu\{(\nabla_XS)Y-(\nabla_YS)X\}
=R^g(X,Y)v+\langle SX,v\rangle SY-\langle SY,v\rangle SX=0.
$$
末次相消是二维代数恒等式：对角化 $S$，两项分别为
$K(\langle v,Y\rangle X-\langle v,X\rangle Y)$ 及其负数。
因此 Codazzi 在 $\nu\ne0$ 处成立，再由解析性延拓到 $c=0$。

在单连通覆盖带上，Gauss–Codazzi 保证正交标架方程可积：
$$
\begin{array}{lll}
(e_1)_r=h_{11}N,&(e_2)_r=h_{12}N,&N_r=-h_{11}e_1-h_{12}e_2,\\
(e_1)_\theta=a'e_2+ah_{12}N,&
(e_2)_\theta=-a'e_1+ah_{22}N,&
N_\theta=-ah_{12}e_1-ah_{22}e_2.
\end{array}\tag{11}
$$
并且 $dF=e_1\,dr+ae_2\,d\theta$ 闭合。
由 (10) 及 $d\nu(X)=-\langle SX,v\rangle$，
$z_re_1+a^{-1}z_\theta e_2+\nu N$ 是一个固定环境单位向量。
把它选为 $e_Z$ 并调整平移，便得到第三坐标恰为 $z$ 的解析等距浸入。
投影在 $c=0$ 处的折叠并不使真实曲面退化。

## 3. 完整角周期，无剩余平移

数据 $g,h$ 分别在 $\theta\mapsto-\theta$ 和
$\theta\mapsto\pi-\theta$ 下不变：$h_{12}$ 的系数变号与 $d\theta$ 变号相抵。
在 $\theta=0$ 上，$h_{12}=0$，所以 $e_2(r,0)$ 是固定水平向量，
而 $F(r,0)$ 位于与它垂直的固定竖直平面 $P_0$。
比较位置和完整标架，重建的唯一性给
$$
F(r,-\theta)=\mathcal R_0F(r,\theta),
$$
其中 $\mathcal R_0$ 是 $P_0$ 的反射。

在 $\theta=\pi/2$ 上，$z=z_r=\nu=0$ 且 $a^{-1}z_\theta=-1$。
于是 $e_2=-e_Z$，$e_1,N$ 水平，固定曲线位于 $P_1=\{Z=0\}$。
同样比较位置与标架得
$$
F(r,\pi-\theta)=\mathcal R_1F(r,\theta).
$$
两平面相交且垂直，所以 $(\mathcal R_1\mathcal R_0)^2$ 为恒等刚体运动，
包括平移部分也为零。因此
$$
F(r,\theta+\pi)=\mathcal R_1\mathcal R_0F(r,\theta),\qquad
F(r,\theta+2\pi)=F(r,\theta).
\tag{12}
$$
这证明完整浸入单值，而不仅是法向或旋转角的周期。

## 4. 有理入口及非旋转性

暂令初值 (2) 中 $p(0)=\varepsilon$ 变化于 $0\le\varepsilon\le1/100$。
在 $r=0$，
$$
\Delta=\frac{333}{1000}-\frac85\varepsilon^2>0,\qquad
R(y)=\frac85-\frac{69}{100}y+
\left(\frac9{100}-\varepsilon^2\right)y^2\ge1-\varepsilon^2>0.
\tag{13}
$$
普通 ODE 局部存在及参数连续依赖在此紧初值段上给共同的小带宽。
当 $\varepsilon=1/100$ 时，
$$
K(0)=\frac{63}{33284}>0,\quad
\xi(0)=-\frac{33291}{33284000},\quad
K'(0)=\frac{3026486511}{46091044812880}>0.
\tag{14}
$$
最后一式可由下列一般恒等式直接核对：
$$
K'(0)=
-\frac{2430000\varepsilon^3
(16000\varepsilon^4-26260\varepsilon^2+999)}
{(1600\varepsilon^2-333)^3}.
$$
缩小带宽使 $K'\ne0$。若像为某轴的旋转曲面，其旋转 Killing 场
必须切于 $K$ 等值圈，故为 $f(r,\theta)\partial_\theta$。
Killing 方程给 $f_r=f_\theta=0$。嵌入的角圈只能绕空间圆一周，
任一 Cartesian 高度在角变量中因此只有零模和一模；
但 (1) 有非零三模 $ab\cos3\theta/4$，矛盾。
在 $r=0,\theta=\pi/2$ 处还有
$h_{11}+h_{22}=(-K-8/5)/\sqrt{8/5}\ne0$，故曲面非极小。

## 5. 对明确初值证明嵌入

在 $r=\theta=0$ 选择
$$
F=(0,0,9/10),\quad
e_1=(\sqrt{1-\varepsilon^2},0,\varepsilon),\quad e_2=(0,1,0),\quad
N=(-\varepsilon,0,\sqrt{1-\varepsilon^2}).
\tag{15}
$$
初始圈上 $a'=0$，故
$$
(e_1)_\theta=h_{12}N,\qquad (e_2)_\theta=h_{22}N,\qquad
h_{22}=\frac{-8/5+(9/10)c^2}{\sqrt R}<0.
$$
由 (13)，
$$
\int_0^{2\pi}|h_{12}|\,d\theta
\le\frac{6\varepsilon}{\sqrt{1-\varepsilon^2}}<\frac2{33}.
\tag{16}
$$
因此 $e_1\cdot e_X>99/100-2/33>0$。
截面切向量 $e_2$ 的 $YZ$ 投影不可能为零，否则 $e_2$ 平行 $e_X$，
与 $e_2\perp e_1$ 矛盾。投影曲率的分子为
$$
\det(e_X,e_2,(e_2)_\theta)=h_{22}(e_1\cdot e_X)<0.
\tag{17}
$$
在 $\varepsilon=0$ 时截面为平面凸卵形：
$$
Z_0=c-\frac1{10}c^3,\quad
Y_0'=c\sqrt{R_0(c^2)},\quad Y_0(0)=0,\quad
R_0(y)=\frac85-\frac{69}{100}y+\frac9{100}y^2.
\tag{18}
$$
其切向量绕行一次。整个 $0\le\varepsilon\le1/100$ 是闭正则平面曲线同伦，
所以切向绕数不变。曲率同号且总转角绝对值 $2\pi$ 的闭正则平面曲线
严格凸且简单：单调切向角参数使每个方向的支撑线恰有唯一切点。
因此 $\varepsilon=1/100$ 的 $YZ$ 投影及空间截面均嵌入。

中央圈附近已经是浸入。嵌入中央圈的紧性给带状嵌入邻域：
有限个局部嵌入图处理相近材料点，分离的中央点对有正距离，
连续性处理其余点对。缩小 $\ell$ 后，整个闭环带嵌入。

## 6. 明确的截面几何尺度

固定 $\varepsilon=1/100$。由 (15)、(16)，$|(e_1)_Y|<2/33$；
高度恒等式给 $(e_1)_Z=\varepsilon c^3$。结合 $(e_1)_X>0$，
$$
(e_1)_X\ge\sqrt{1-\frac4{1089}-\frac1{10000}}>
\frac{997}{1000},\qquad |(e_2)_X|<\frac{31}{500}.
\tag{19}
$$
写 $e_1=(S t,w)$，其中 $w=\varepsilon c^3$、$S=\sqrt{1-w^2}$、
$t$ 为水平单位向量；$J$ 为水平旋转 $\pi/2$。
设 $v=(e_2)_Z=-s(1-3c^2/10)$。正交性和 $N_Z=\nu$ 给
$$
(e_2)_{\rm hor}=-\frac{wv}{S}t+\frac{\nu}{S}Jt.
\tag{20}
$$
在第一象限，$t_X>997/1000$、$|t_Y|<61/1000$，
且 $\sqrt R\ge(9999/10000)\sqrt{R_0}$。式 (20) 的 $Y$ 分子为正，
而 $S\le1$，故
$$
Y_\theta\ge\frac{997}{1000}\frac{9999}{10000}
c\sqrt{R_0(c^2)}-\frac{61}{100000}c^3>0
\quad(0\le\theta<\pi/2).
\tag{21}
$$
令 $u=\sin\theta$。平方验证
$\sqrt{1+51u^2/100+9u^4/100}\ge1+u^2/4$，故
$$
\int_0^{\pi/2}c\sqrt{R_0(c^2)}\,d\theta
=\int_0^1\sqrt{1+\frac{51}{100}u^2+\frac9{100}u^4}\,du
\ge\frac{13}{12}.
$$
因此
$$
Y(\pi/2)>
\frac{997}{1000}\frac{9999}{10000}\frac{13}{12}
-\frac{61}{100000}\frac23
=\frac{129548239}{120000000}>\frac{1079}{1000}.
\tag{22}
$$
两反射平面是 $\{Y=0\}$、$\{Z=0\}$，所以这是完整圈的 $Y$ 最大值。

另一方面，$Y_\theta^2\le1-Z_\theta^2=c^2R_0(c^2)$，
所以 $\max|Y|\le\sqrt{8/5}$；显然 $\max|Z|=9/10$。
两反射均不改变 $X$，完整圈的 $X$ 值域已在第一象限中出现，
其宽度由 (19) 小于 $(\pi/2)(31/500)<1/10$。于是
$$
(\operatorname{diam}\Gamma)^2
<\frac1{100}+4\cdot\frac85+4\cdot\frac{81}{100}
=\frac{193}{20}<\left(\frac{311}{100}\right)^2.
\tag{23}
$$
令 $\mathcal Q$ 绕 $X$ 轴转 $\pi/2$，将 $Y$ 方向转至 $Z$ 方向。
Hausdorff 距离支配任一单位方向的支撑函数差，所以
$$
d_H(\Gamma,\mathcal Q\Gamma)>
\frac{1079}{1000}-\frac9{10}=\frac{179}{1000}.
\tag{24}
$$
进一步缩小带宽，可使整带直径小于 $16/5$、整带的 $\max Z<91/100$。
中央圈仍在带中，因此
$$
d_H(F([-\ell,\ell]\times S^1),\mathcal QF([-\ell,\ell]\times S^1))
>\frac{169}{1000}
>\frac1{20}\operatorname{diam}F([-\ell,\ell]\times S^1).
\tag{25}
$$

这只是模块形状的尺度信息。绕空间轴整体旋转没有固定握持区，并且
$\delta_E=0$。仍须构造真实旋转开领圈、相对相位、闭合、全局嵌入及 reach；
本定理不能作为主任务完成。
