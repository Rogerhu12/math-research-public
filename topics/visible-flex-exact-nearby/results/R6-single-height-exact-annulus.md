# R6：单高度谐波、自由径向度量与精确周期嵌入环带

**状态：已证明的正向中间结论；主目标未完成。**

## 命题

存在 $\varepsilon_0>0$、$\ell>0$ 及实解析函数 $\mu_*:(-\varepsilon_0,\varepsilon_0)\to\mathbb R$，
满足 $\mu_*(0)=\sqrt3/2$，并有如下性质。对每个
$0<|\varepsilon|<\varepsilon_0$，以下确定的五维常微分方程初值问题给出
$I=[-\ell,\ell]$ 上的实解析函数 $a,\mu,U,W,y$：
$$
(a,\mu,U,W,y)(0)=(1,\mu_*(\varepsilon),1/2,\varepsilon,0).
$$
令 $u(r)=\int_0^r U(s)\,ds$，则存在实解析嵌入
$$
F_\varepsilon:I\times(\mathbb R/2\pi\mathbb Z)\longrightarrow\mathbb R^3
$$
满足
$$
F_\varepsilon^*\langle\cdot,\cdot\rangle=dr^2+a(r)^2d\theta^2,\qquad
(F_\varepsilon)_3=u(r)+W(r)\cos2\theta.
$$
其像不是任何轴的旋转曲面。全部角向单值性由下述一个标量周期条件精确实现，
不是把有限 Fourier 解当作完整 PDE 解，也不依赖数值残差。

这里 $\varepsilon_0,\ell$ 只有局部存在性保证，未给出达到可见幅度的数值；
$F_\varepsilon$ 是带边环带，尚无固定旋转开领圈或闭曲面。
不同 $\varepsilon$ 对应的输出度量可以不同。固定一个 $\varepsilon$ 后，
其材料角相位作用保持该输出度量，但单带相位的像仅作刚体旋转，
不能单独提供本题要求的 $\delta_E>0$。

## 证明

## 1. 完整 Darboux 方程的五维 ODE

有限 Cartesian Fourier 可能过于僵硬。现只令高度为
$$
z(r,\theta)=u(r)+W(r)\cos(n\theta),\qquad
g=dr^2+a(r)^2d\theta^2,\quad n\ge2,
$$
允许平面坐标的精确重建拥有无限 Fourier 展开。设
$$
U=u',\quad V=W',\quad \mu=a'/a,\quad
\lambda=n^2/a^2,\quad K=-a''/a,\quad
Q=V-\mu W,\quad J=\mu V-\lambda W.
$$
在正交标架 $(\partial_r,a^{-1}\partial_\theta)$ 下，
$$
\nabla^2z=
\begin{pmatrix}
U'+V'\cos(n\theta)&-nQ\sin(n\theta)/a\\
-nQ\sin(n\theta)/a&\mu U+J\cos(n\theta)
\end{pmatrix},
$$
而
$$
|\nabla z|^2=(U+V\cos(n\theta))^2+\lambda W^2\sin^2(n\theta).
$$
因此完整的、未截断的 Darboux 恒等式
$\det_g\nabla^2z=K(1-|\nabla z|^2)$
等价于以下三式：
$$
\begin{aligned}
\mu UU'-\lambda Q^2&=K(1-U^2-\lambda W^2),\\
J U'+\mu U V'&=-2KUV,\\
J V'+\lambda Q^2&=-K(V^2-\lambda W^2).
\end{aligned}\tag{11}
$$
因为两边都是 $\cos(n\theta)$ 的二次多项式，这三式控制全部角频，不存在被遗漏的更高模式。

在 $W\ne0$ 时引入 $y=V/W$，并令
$$
\mathcal T=U^2\lambda(\lambda-\mu^2)
 -(1-\lambda W^2)(\mu y-\lambda)^2.
$$
当 $\mathcal T\ne0$ 时，(11) 等价于
$$
\begin{aligned}
a'&=a\mu,\qquad \mu'=-K-\mu^2,\qquad W'=Wy,\\
K&=\frac{\lambda(y-\mu)^2
  \bigl(W^2(\mu y-\lambda)^2-U^2\mu^2\bigr)}
 {\mathcal T},\\
U'&=\frac{U\lambda(y-\mu)^2
  \bigl(\mu(U^2-1)+W^2(-\mu y^2+2\lambda y)\bigr)}
 {\mathcal T},\\
y'&=\frac{\lambda(y-\mu)^2
  \bigl(U^2(\mu y+\lambda)+\mu y-\lambda
         +W^2y^2(-\mu y+\lambda)\bigr)}
 {\mathcal T}-y^2 .
\end{aligned}\tag{12}
$$
右边在 $W=0$ 也解析延伸；若初始 $W\ne0$，则 $W'=Wy$ 在有界正则区间保持其符号。
直接将 (12) 乘回分母、代入 (11)，即可验证恒等式，故使用这一 ODE 不是把 PDE 截断后再期待尾部变小。

### 一个实际正则的非零曲率入口

取 $n=2$，在 $r=0$ 规定
$$
a=1,\qquad U=\frac12,\qquad
\mu=\frac{\sqrt3}{2},\qquad W=0,\qquad y=0.
$$
有
$$
\mathcal T=-\frac{51}{4},\qquad
K=\frac3{68},\qquad
(a',\mu',U',W',y')
=\left(\frac{\sqrt3}{2},-\frac{27}{34},
       \frac{3\sqrt3}{68},0,\frac{12}{17}\right).
$$
沿 (12) 求导还得到
$$
K'=-\frac{699\sqrt3}{9826}\ne0.
$$
这些数值均为以上有理式的准确代入。为具体检查最后一项，$K$ 对
$(a,\mu,U,W,y)$ 的梯度在入口等于
$$
\left(\frac{24}{289},\frac{33\sqrt3}{289},
      \frac{64}{289},0,-\frac{13\sqrt3}{289}\right).
$$
与上列向量场点积正是 $-699\sqrt3/9826$。
故小的非零 $W$ 初值给出一个正则的精确高度解；尚须处理平面开发的周向 holonomy，
不能仅由 (11) 宣称闭环。

## 2. 全角闭合的标量周期条件

若
$$
1-|\nabla_gz|^2>0,
$$
则 $h=g-dz^2$ 为正定度量。其二维曲率恒等式为
$$
K_h=
\frac{K_g(1-|\nabla_gz|^2)-\det_g\nabla^2z}
     {(1-|\nabla_gz|^2)^2}.
\tag{13}
$$
为核对符号与分母，考虑 Lorentz 乘积 $((M,g)\times\mathbb R,g-dt^2)$ 中的图
$p\mapsto(p,z(p))$。记 $q=1-|\nabla_gz|^2>0$；图的诱导度量是 $h$，
$\det h=q\det g$，单位类时法向可取 $(\nabla_gz,1)/\sqrt q$。
第二基本形式等于 $\nabla_g^2z/\sqrt q$（整体符号不影响行列式），
故其相对于 $h$ 的行列式为 $\det_g\nabla^2z/q^2$。
乘积环境的切平面截面曲率为 $K_g/q$。
类时法向的 Gauss 方程给 $K_h=K_g/q-\det_g\nabla^2z/q^2$，即 (13)。
所以 (11) 使 $h$ 精确平坦。其在带的普适覆盖上的开发
$D=(X,Y)$ 满足 $D^*(dx^2+dy^2)=h$，从而 $(X,Y,z)$ 精确实现 $g$。

此处不能省略开发的全局周期。由于高度是单余弦模，$h$ 关于
$\theta=0$ 和 $\theta=\pi/n$ 的反射均不变。开发把这两条反射的固定径线映为两条直线；
两个反射在开发平面上也分别是对这两条直线的反射。
设两线的有向夹角为 $\beta$。材料角平移 $2\pi/n$ 是这两反射的复合，
所以完整 $2\pi$ 周期的平面 holonomy 为这个复合的 $n$ 次。
因此
$$
\beta=\pi/n
\tag{14}
$$
保证完整 holonomy 为恒等。这里两线因 $\beta\ne0\pmod\pi$ 而相交；
复合是绕交点的旋转，故 (14) 同时消去平移部分，而非只检查旋转矩阵。

该标量可由初始圆上的一维积分精确计算。记
$$
A=1-(U+V\cos n\theta)^2,\quad
B=nW\sin n\theta(U+V\cos n\theta),\quad
C=a^2-n^2W^2\sin^2n\theta,
$$
以及
$$
\alpha=\sqrt A,\qquad b=B/\sqrt A,\qquad
c=\sqrt{AC-B^2}/\sqrt A.
$$
则 $h=(\alpha\,dr+b\,d\theta)^2+c^2d\theta^2$。
若 $\gamma$ 是开发中第一标架向量的方向角，平面闭性方程给
$$
\gamma_r=\frac{b_r-\alpha_\theta}{c},\qquad
\gamma_\theta=\frac{c_r+b\gamma_r}{\alpha}.
$$
因此可取
$$
\beta=\int_0^{\pi/n}\frac{c_r+b(b_r-\alpha_\theta)/c}{\alpha}\,d\theta.
\tag{15}
$$
所有 $r$ 导数由 (12) 直接给出。平坦性保证结果不依赖所选初始径向位置。

### 一条完整的局部存在推论

在第 1 节入口，改令 $W(0)=\varepsilon$，保留 $a(0)=1,U(0)=1/2,y(0)=0$，
把 $\mu(0)$ 作为待选参数。由于 $\mathcal T$ 与 $1-|\nabla z|^2$ 在入口都严格离零，
ODE 右端在入口附近为实解析且分母 $\mathcal T\ne0$；取一个小的共同径向区间，
普通常微分方程存在定理给所有邻近初值在该区间上的解及其实解析参数依赖。
此区间内 $a>0$、$q>0$ 由严格初始不等式和连续性保持。
式 (15) 的被积函数的平方根均取正支，$r$ 导数全由 (12) 给出，故其对
$(\varepsilon,\mu(0))$ 的依赖实解析，而非额外假设。
当 $\varepsilon=0$ 时，
$$
\beta(0,\mu(0))
=\frac{\pi}{n}\frac{\mu(0)}{\sqrt{1-U(0)^2}},
\qquad
\partial_{\mu(0)}\beta
=\frac{\pi}{n\sqrt{1-U(0)^2}}\ne0.
$$
普通有限维隐函数定理于是给出
$\mu(0)=\mu_*(\varepsilon)$，$\mu_*(0)=\sqrt3/2$，使 (14) 精确成立。
这证明：充分小的非零 $\varepsilon$ 给出一个完整周向周期的精确嵌入环带，
而非仅在一个角扇区上存在的局部图。当 $\varepsilon=0,\mu(0)=\sqrt3/2$ 时，$W$ 恒零，
(11) 的零模方程使 $a\mu/\sqrt{1-U^2}$ 保持为 $1$，所以开发可取
$(X,Y)=(a(r)\cos\theta,a(r)\sin\theta)$。
因为初始 $a'>0$、$U>0$，缩短区间后这是一个嵌入的旋转带。
开发的初始 Euclidean 刚体规范固定以后，开发方程及 $z$ 随初值连续依赖，
故在紧子带上得到 $C^2$ 接近。紧嵌入在 $C^1$ 拓扑下开放：
近对角点对由有限局部图的统一可逆导数控制，离开这些局部图的点对
由原嵌入的正距离分离控制。因此再缩小 $\varepsilon_0$ 即得到上述嵌入性。

这一环带不为任何轴的旋转曲面。在该小区间 $K'\ne0$；若有轴旋转，
其内蕴 Killing 场必须沿 $K$ 的等值圆，Killing 方程又迫使它为
常数倍的 $\partial_\theta$。一个简单旋转圆上的固定 Cartesian 高度只能有零模和一模；
本构造却有非零二模 $W(r)\cos2\theta$，矛盾。

**仍缺的部分：** 这是一条小振幅、带边的精确环带定理。正则 ODE 中
$W'=Wy$ 不能在有限端点上自行变成固定旋转开领圈；
两个开领圈的退化过渡、闭曲面拼接、可见振幅和定量 reach 均未完成。
式 (12)、(14)、(15) 给下一步具体的有限维射击问题，不能把局部推论写作本题完成。
