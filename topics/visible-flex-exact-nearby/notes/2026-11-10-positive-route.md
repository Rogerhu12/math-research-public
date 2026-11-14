# 正向精确路线：自由平均度量与有限 Fourier 消元

会话 `positive_exact_route`，2026-11-10。状态：本文的恒等式与有限 ansatz 分类已直接推导；没有构造出满足本题全部指标的精确闭曲面。本文不是完成声明。

## 1. 本题可以把径向平均度量作为输出

本题允许另选 $g$。因而对一条候选带 $F:I\times S^1\to\mathbb R^3$，可以求
$$
P_{\ne0}(F_r\cdot F_r)=P_{\ne0}(F_r\cdot F_\theta)
=P_{\ne0}(F_\theta\cdot F_\theta)=0,
\tag{1}
$$
其中 $P_{\ne0}$ 是材料角 Fourier 非零模投影。若 $F$ 是浸入，(1) 精确成立，则其诱导度量为
$$
g=E(r)\,dr^2+2B(r)\,dr\,d\theta+C(r)\,d\theta^2,\qquad C>0,\quad EC-B^2>0.
$$
这是一个精确、$S^1$ 不变的输出度量；没有理由再强迫其三个平均分量等于原数值解采用的预定平均分量。

设
$$
\psi=\theta+\chi(r),\quad \chi'=B/C,\qquad
s'=\sqrt{E-B^2/C},\qquad a(s)=\sqrt{C(r(s))}.
$$
直接代入得 $g=ds^2+a(s)^2d\psi^2$。该坐标变换在每个圆上仍为次数一映射，材料角平移在新旧坐标中都是同一个 $S^1$ 作用。若两开领圈已精确为旋转嵌入，(1) 的修正取为领圈上零，便不会改变这些领圈。两端的 $\chi$ 常数可以不同；相位作用不因此改变。

注意：把近似诱导度量取角平均并不能证明平均度量被原图实现。真正必须求解的仍是 (1)。这一消元只删除三个径向平均方程，不支付全频逆估计与两端闭合。

## 2. 有限 Cartesian Fourier 的完整方程

令
$$
F(r,\theta)=\sum_{k=-N}^N c_k(r)e^{ik\theta},\qquad
c_{-k}=\overline{c_k},\quad c_0\in\mathbb R^3.
$$
点积在复向量上作双线性延拓。令不存在的 $c_k$ 为零。则 (1) 等价于对每个 $1\le |j|\le2N$ 同时满足
$$
\sum_{k+l=j}c'_k\cdot c'_l=0,
\quad
\sum_{k+l=j}i l\,c'_k\cdot c_l=0,
\quad
\sum_{k+l=j}(-kl)c_k\cdot c_l=0.
\tag{2}
$$
这是真正有限的微分代数系统，并非只把方程投影回 $|j|\le N$。必须保留至 $2N$ 的所有模式；若 (2) 完整成立，任何更高角模都由于乘积次数而严格为零。因而该路线原则上可免除无限 Fourier 尾，但不能只解低模。

三个平均输出为
$$
E=\sum_k c'_k\cdot\overline{c'_k},\quad
B=\sum_k(-ik)c'_k\cdot\overline{c_k},\quad
C=\sum_k k^2c_k\cdot\overline{c_k}.
\tag{3}
$$
其中 $B$ 因现实条件为实数。这里双计正负模正是实际 Fourier 归一的结果。

### 最高模的固定复平面

在 $c_N\ne0$ 的区间，(2) 的 $j=2N$ 给
$$
c_N\cdot c_N=0,\qquad c'_N\cdot c'_N=0.
$$
对第一式求导亦有 $c_N\cdot c'_N=0$。在 $\mathbb C^3$ 中，一个非零零向量 $v$ 的正交补中，所有零向量均为 $v$ 的倍数：经复正交变换令 $v=(1,i,0)$，正交条件给 $w_1+iw_2=0$，零条件进一步给 $w_3=0$。因此
$$
c'_N=\lambda(r)c_N,\qquad c_N(r)=\alpha(r)v_0,
\tag{4}
$$
其中 $v_0$ 为固定复零向量。局部选择 $c_N$ 一个不为零的分量即可定义连续 $\lambda$ 并积分，故没有除以零向量的隐含步骤。其余低模仍可变化，(4) 不是一般不可能性结论。

## 3. 两个反向圆模和一个竖直模：精确消元

尝试
$$
F=(A(r)\cos(n\theta)+B(r)\cos(m\theta),\
 A(r)\sin(n\theta)-B(r)\sin(m\theta),\
 z_0(r)+C(r)\cos(p\theta)),
\tag{5}
$$
其中 $m,n\ge1$、$m\ne n$、$p=(m+n)/2\in\mathbb N$，且在所讨论区间 $ABC\ne0$。假设 $A,B,C,z_0$ 为实函数。

$G=F_\theta^2$ 的非零角模仅为 $m+n=2p$，它的系数为
$$
-2mnAB-\frac{p^2C^2}{2}.
$$
故
$$
C^2=-\frac{4mn}{p^2}AB.\tag{6}
$$
$F_r\cdot F_\theta$ 的 $p$ 模为 $-p z'_0C\sin(p\theta)$，所以 $z'_0=0$。同一张量的 $2p$ 模给
$$
m A'B+nAB'+\frac p2 CC'=0.\tag{7}
$$
用 (6) 的导数代入 (7)，由于 $m\ne n$，得到
$$
mA'B-nAB'=0.\tag{8}
$$
在 $A,B$ 不变号区间，令 $A=a\rho^n$，则 $B=b\rho^m$，而 (6) 给
$$
C=c\rho^p,\quad c^2=-\frac{4mn}{p^2}ab,
\quad ab<0.\tag{9}
$$
$F_r^2$ 的 $2p$ 模为 $2A'B'+C'^2/2$，由 (9) 自动为零。因此 (9) 连同常数 $z_0$ 是 (5) 的完整非退化精确解，并非仅有限模线性解。

全部平均度量变为
$$
F_r^2=(nA-mB)^2(\rho'/\rho)^2,
\qquad F_\theta^2=(nA-mB)^2,
\qquad F_r\cdot F_\theta=0.\tag{10}
$$
取 $u=\log\rho$ 后得到共形参数。各 Cartesian 分量分别是 $e^{nu}\cos n\theta$、$e^{mu}\cos m\theta$、$e^{pu}\cos p\theta$ 及其正弦，故
$$
F_{uu}+F_{\theta\theta}=0.
$$
结合 (10) 可直接推出该非退化解是极小曲面。$n=1,m=3$ 是 Enneper 型实例。这里的推导解释了为何该最短有限 ansatz 虽有精确非旋转周期环带，却不给固定旋转领圈：$B=b\rho^m$ 与 $C=c\rho^p$ 在正半径处不会独立消失，且不能加入变化的平均高度 $z_0$。

本题仍允许更丰富的有限 ansatz，例如至少两个竖直非零模、更多横向频率以及角相位随 $r$ 的变化。以上计算不排除它们；但不应重复把 (5) 当成新的非极小闭合机制。

## 4. 文献核对的精确范围

J. N. Clelland、T. A. Ivey、N. Tehseen、P. J. Vassiliou，*Isometric Embedding and Darboux Integrability*（2018），arXiv:1801.00241，Theorem 7 的欧氏双曲可积度量包括
$$
\cos^4u\,du^2+\sin^2u\,dv^2,\qquad K=-\sec^4u.
$$
原文 §5 的详细任意函数表达是 Lorentzian 度量在 $\mathbb R^{1,2}$ 中的例子，不能把该公式直接当作本题的欧氏闭曲面。原文来源：https://arxiv.org/pdf/1801.00241 。

下一项具体工作：在 (2) 的完整 $2N$ 模约束下，扩展 (5) 的竖直频率并寻找允许 $z'_0\ne0$、$K$ 变号、两个旋转开领圈的解。若有限系统强迫所有非旋转支为极小，须从证明中具体指出迫使它的频率恒等式，不能只由以上子族推论一般分类。

## 5. 两个竖直模的实际消元尝试

下面只记录一个确实算到末端的实系数子族，不把它推广为一般分类。设
$$
X+iY=a e^{i\theta}+b e^{-i\theta}
       +c e^{3i\theta}+d e^{-3i\theta}+e e^{-5i\theta},
\qquad Z=h+f\cos2\theta+g\cos4\theta.
$$
在最高模式非零的一个归一化支上，最高八模的三个度量方程可取
$c=\rho^3$、$e=-4\rho^5/15$、$g=\rho^4$，$\rho>0$。
其余 $G$ 方程先解出
$$
d=\frac{4a\rho^2}{27}-\frac{4f\rho}{9},\qquad
b=-\frac{3ad+f^2}{\rho^3(3+4\rho^2/3)}.
$$
$G$ 的二模剩余等于非零常数乘以
$$
(4a\rho^2-9a-12f\rho)
\bigl((2a\rho-3f)^2+\rho^6(4\rho^2+9)^2\bigr).
$$
第二因子严格正，故
$$
f=\frac{a(4\rho^2-9)}{12\rho},\qquad
d=a/3,\qquad
b=-\frac{a^2(4\rho^2+9)}{48\rho^5}.
$$
取 $\rho$ 为径向参数。$F_\rho\cdot F_\theta$ 的六模、四模依次给
$$
\frac{da}{d\rho}=\frac{a(4\rho^2+9)}{\rho(4\rho^2+3)},\qquad
\frac{dh}{d\rho}=-\frac{a^2(4\rho^2+27)}
                         {12\rho^5(4\rho^2+3)}.
$$
把它们代回二模，剩下
$$
\frac{a(a^2+16\rho^8)(4\rho^2+9)^2}
     {144\rho^6(4\rho^2+3)}=0,
$$
所以该实支又退化到 $a=0$。复相位、更一般的频率排列和非有限 Cartesian 重建不受此计算排除。

## 6. 改为有限高度：完整 Darboux 方程的五维 ODE

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
这些数值均为以上有理式的准确代入。故小的非零 $W$ 初值给出一个正则的精确高度解；尚须处理平面开发的周向 holonomy，不能仅由 (11) 宣称闭环。

## 7. 单高度模式的全角闭合：一个标量周期条件

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
这个公式可直接由 $h_{ij}=g_{ij}-z_i z_j$ 的 Levi-Civita 连接计算，或对
$(M,h)\times\mathbb R$ 内的图 $(p,z(p))$ 用 Gauss 方程得到。
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

在第 6 节入口，改令 $W(0)=\varepsilon$，保留 $a(0)=1,U(0)=1/2,y(0)=0$，
把 $\mu(0)$ 作为待选参数。由于 $\mathcal T$ 与 $1-|\nabla z|^2$ 在入口都严格离零，
ODE 解和 (15) 对 $(\varepsilon,\mu(0))$ 在小邻域内解析依赖。
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
而非仅在一个角扇区上存在的局部图。嵌入性由其在固定小径向区间内
对原旋转嵌入的 $C^1$ 接近得到。

这一环带不为任何轴的旋转曲面。在该小区间 $K'\ne0$；若有轴旋转，
其内蕴 Killing 场必须沿 $K$ 的等值圆，Killing 方程又迫使它为
常数倍的 $\partial_\theta$。一个简单旋转圆上的固定 Cartesian 高度只能有零模和一模；
本构造却有非零二模 $W(r)\cos2\theta$，矛盾。

**仍缺的部分：** 这是一条小振幅、带边的精确环带定理。正则 ODE 中
$W'=Wy$ 不能在有限端点上自行变成固定旋转开领圈；
两个开领圈的退化过渡、闭曲面拼接、可见振幅和定量 reach 均未完成。
式 (12)、(14)、(15) 给下一步具体的有限维射击问题，不能把局部推论写作本题完成。

## 8. 单高度模在投影退化驻点的几何检查

这一检查针对第 6 节模型的闭合路线，不排除多高度模、无限角频或一般闭曲面弯曲。
设某个真实 $C^2$ 嵌入 $F$ 精确实现
$dr^2+a(r)^2d\theta^2$，高度为 $u(r)+W(r)\cos n\theta$，
$n\ge2$。假设在 $r=r_0$ 有 $W>0,W'=0$。所有量以下均取在该圈上。
欧氏投影恒等式给 $q=1-|\nabla z|^2\ge0$。

若 $q$ 在该圈处处正，第 6 节的正则 ODE 有
$$
\mathcal T=\lambda\bigl[\lambda(U^2-1+\lambda W^2)-U^2\mu^2\bigr]<0,
\qquad
y'=-\frac{\lambda^2\mu^2(1-U^2)}{\mathcal T}\ge0 .
$$
当 $\mu\ne0$ 时严格正，故不是 $W$ 的局部极大；当 $\mu=0$ 时为正则平衡点，
唯一性使该解在相邻区间恒定。

关键是不能只停在这个正定情形。若 $q$ 在圈上有零，则
$$
U^2+\lambda W^2=1,\qquad S=\sqrt{1-U^2}=nW/a>0.
$$
令 $J$ 表示水平面转 $\pi/2$，并写
$$
F_r=(S T(\theta),U),\qquad |T(\theta)|=1.
$$
由 $F_r\cdot F_\theta=0$ 与 $|F_\theta|=a$，必有
$$
F_\theta=
\bigl(aU\sin(n\theta)T(\theta)+b(\theta)JT(\theta),
      -aS\sin(n\theta)\bigr),
\qquad b(\theta)^2=a^2\cos^2(n\theta).
$$
因为 $F$ 为 $C^2$，$T,b$ 均为 $C^1$。
$\cos(n\theta)$ 的零点简单；若 $b/(a\cos n\theta)$ 在这样的零点两侧改变符号，
$b'$ 的两个极限相反且非零，违背 $C^1$。
故存在一个对全部 $\theta$ 相同的 $\sigma\in\{1,-1\}$，使
$b=\sigma a\cos(n\theta)$。

写 $T_\theta=\varphi' JT$。径向微分 $|F_\theta|^2=a^2$ 得
$$
a a'=F_\theta\cdot F_{r\theta}
     =\sigma a S\varphi'(\theta)\cos(n\theta).
$$
在余弦零点得到 $a'=0$，继而在其余点得到 $\varphi'=0$；连续性给 $T$ 恒定。
于是
$$
F_\theta=
a\sin(n\theta)(U T,-S)
+\sigma a\cos(n\theta)(JT,0).
$$
右边的两个固定向量正交且长度一。积分表明该圈为同一平面圆绕行 $n$ 次，
与 $F$ 嵌入矛盾。

因此在这个单高度模中，不能以穿过 $q=0$ 的正振幅驻点逃过前面的极大值检测。
若 $W$ 在有限带两端都零且内部非零，取 $|W|$ 的正最大值：
正定情形的平衡点唯一性与退化情形的多重覆盖分别排除它。
这里没有排除多高度模的振幅峰；下一步应允许至少两个独立高度模，
或者只在核心使用有限高度，而在开领圈用无限角频退化桥。


## 9. 双高度模的精确周期模块

完整正向命题见 results/R10-two-height-modes-exact-periodic-annulus.md。
高度取 $z=a(\cos\theta+b\cos^3\theta)$；完整 Darboux 方程只剩两个
关于 $K=-a''/a$ 与 $\xi=b''+2(a'/a)b'$ 的线性式，给出四维有理 ODE。
法向采用有符号的 $\nu=\cos\theta\sqrt{R(\cos^2\theta)}$，
第二基本形式在投影折叠线上解析。两个互相垂直的反射平面自动消除
全部欧氏单值性缺陷。入口 $(a,\mu,b,p)=(1,0,-1/10,1/100)$
给真实非旋转、非极小嵌入环带；截面支撑差 $>.179$、
直径 $<3.11$ 由有理不等式证明。

这只是精确非轴对称模块。绕空间轴整体旋转的支撑差不是固定帽下的
$\delta_E$，也没有闭合。下一条正向任务是研究 $b,p\to0$ 时
$a'^2\to1$ 的退化尾，使非旋转高度在有限边界有足够零 jet，
然后接到真实固定旋转开领圈。


## 10. R10 的有限半径旋转平尾不能从原始系统产生

此处只决定 R10 的接帽路线，不排除多模、一般高度或 R11 真无限层平尾。
结论在原始式 R10 (8) 上证明，不使用 $\Delta^{-1}$ 或 $R^{-1}$。

设在有限边界 $r_0$ 上，$a,b$ 有 $C^2$ 延拓，
$a(r_0)>0$ 且 $b(r_0)=b'(r_0)=0$。假设原始两个 Darboux 系数式在一侧成立。
则 $b$ 在该侧的某邻域恒为零。

证明分两种情形。记 $p=b'$、$\mu=a'/a$、$K=-a''/a$；
这些背景系数在边界附近有界。

若 $a'(r_0)^2\ne1$，则 $A=a'^2+6b-1$ 一致离零。
第一式
$$
A(b''+2\mu b')+CK=9p^2,\qquad C=a^2\mu p+b(3b+4)
$$
立即给 $|p'|\le C_0(|b|+|p|)$，由零初值和 Gronwall 得结论。

若 $a'(r_0)^2=1$，则 $d=a^2\mu=aa'$ 一致离零。
写 $B=dp+eb$，其中 $e=a'^2-9$。取固定足够大的 $L$，使
在 $|p|\ge L|b|$ 的区域有 $|B|\ge c|p|$。又
$D=a^2p(p+b\mu)$ 在该区域满足 $|D|\le C_1p^2$。
第二式 $B\xi+DK=-9p^2$ 因而给
$|\xi|\le C_2|p|$，进而 $|p'|\le C_3|p|$。
考虑局部 Lipschitz 函数
$$
V=\max\{|p|,L|b|\}.
$$
在 $|p|$ 占优处有 $D^+V\le C_3V$；
在 $L|b|$ 占优处有 $D^+V\le L|p|\le LV$。
在相等处取两方向导数的最大值，仍得同一界；
零集上的几乎处处导数为零。故 $V'\le\max(C_3,L)V$ 几乎处处，
而 $V(r_0)=0$，再次由 Gronwall 得 $V=0$。

这覆盖 $a'^2\to1$ 的真正投影退化端，因此不能依靠该退化在 R10 的
同一双高度系统里接入旋转开领圈。没有排除 $a\to0$ 的极点。
以 $x=\log a$、$t=a'^2$、$q=b_x$ 分析极点的形式领先项，
若 $b\sim B a^m$ 且 $t=1+O(b)$，第二系数式给
$m(m+4)(m-2)=0$；正的平滑候选是 $b=O(a^2)$。
这仅是极点候选渐近，不提供固定开集，也未声称已完成真正闭面。

由此转向 R11/R12 的第四模真实平尾背景，尝试完整非均值非线性近似；
不再增加只提供局部环带的有限高度变体。
