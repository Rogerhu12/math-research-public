# R8：Pöschl–Teller 闭背景上的真实二阶非均值校正

2026-11-10，geometry-transfer。

**状态：已证明；主课题的中间结论。** 本文从 R4 的真实全直线算子
$L_6^{-1}$ 构造一个闭面上的 $C^2$ 二阶向量场，准确消掉非均值度量误差的
二阶项。输出径向平均度量后，剩余误差准确从三阶开始。本结果不是非线性
等距族，也没有提供固定开集 $H$。有限区间浮点计算只放在配套诊断笔记，
不参加本文证明。

依赖：[R4](R4-explicit-one-mode-sturm-background.md) 第 1—6 节。
本文不使用 R5 的数值几何界，不改变 R4 的势或其端点条件。

## 1. 明确陈述与记号

保留 R4 的
$$
\mu=\sqrt2,\quad A=2+\frac{\mu}{3},\quad
q(x)=2-A\operatorname{sech}^2x,\quad
L_j=-\partial_x^2+j^2q(x).
\tag{1.1}
$$
令 $h$ 为 $h''=qh,\ h(0)=1,\ h'(0)=0$ 的正偶解，并写
$$
v=h',\qquad p=\sqrt{1+v^2},\qquad
a=h^{-1},\qquad z' =h^{-2},\qquad
\frac{ds}{dx}=\frac p{h^2}.
\tag{1.2}
$$
背景
$$X(x,\theta)=a(x)e_r(\theta)+z(x)e_z$$
补上两极后是 R4 已证明的闭 $C^2$ 嵌入球面 $S$。以下撇号恒指
$x$ 导数，下标 $s$ 指经线弧长导数。圆柱标架为
$$e_r=(\cos\theta,\sin\theta,0),\quad
e_\theta=(-\sin\theta,\cos\theta,0),\quad e_z=(0,0,1).$$

取 $n=3,\ m=2n=6$，以及 R4 的真实核与无穷小弯曲
$$
y=\operatorname{sech}^{3\mu}x,\qquad
U=\frac yh,\qquad T=-\frac Un,\qquad
W=\frac vh\,y-\frac{y'}{n^2},
\tag{1.3}
$$
$$
Z=U\cos(n\theta)e_r+T\sin(n\theta)e_\theta+W\cos(n\theta)e_z.
\tag{1.4}
$$
定义标量源
$$
P=\frac12\left[\left(n-\frac1n\right)^2U^2+n^2W^2\right],
\tag{1.5}
$$
$$
Q=\frac12\left[\left(n-\frac1n\right)UU_s+nWW_s\right],
\qquad
R=-\frac12\left[U_s^2+W_s^2-\frac{U_s^2}{n^2}\right].
\tag{1.6}
$$
再置
$$
C=\frac{P}{2a}=\frac{hP}{2},\qquad
J=(hC)'-mpQ,\qquad
f=\frac{m^2p^2}{2h^2}R-J',
\tag{1.7}
$$
并用 R4 的自伴全直线逆定义
$$
\eta=L_6^{-1}f,\qquad \eta\in H^2(\mathbb R).
\tag{1.8}
$$
这个定义是无穷区间上的唯一解，未用截断 Robin 条件替代。最后令
$$
U_6=\frac{\eta}{h},\qquad
T_6=\frac{C-U_6}{m},\qquad
W_6=\frac vh\,\eta-\frac{\eta'}{m^2}+\frac J{m^2},
\tag{1.9}
$$
$$
Y=U_6\cos(m\theta)e_r+T_6\sin(m\theta)e_\theta
  +W_6\cos(m\theta)e_z.
\tag{1.10}
$$

**定理。** 以上 $f$ 属于 $L^2(\mathbb R)$，因而 (1.8) 定义良好。
$Y$ 在两个极点取零后为全局 $C^2$ 向量场，且两极上的值、一阶导数、
二阶导数全部为零。它准确满足
$$
\mathcal B_X(Y)=-\mathcal P_{\ne0}(dZ\cdot dZ),
\qquad
\mathcal B_X(Y)_{ij}
=\langle X_i,Y_j\rangle+\langle Y_i,X_j\rangle.
\tag{1.11}
$$
这里 $\mathcal P_0$ 是参数球面旋转作用的张量平均，
$\mathcal P_{\ne0}=I-\mathcal P_0$；在内部 $(s,\theta)$ 坐标中就是对
各张量分量取 $\theta$ 平均。

因此对
$$F_\varepsilon=X+\varepsilon Z+\varepsilon^2Y$$
及输出径向度量
$$
g_\varepsilon=g_0+
 \varepsilon^2\mathcal P_0(dZ\cdot dZ)+
 \varepsilon^4\mathcal P_0(dY\cdot dY),
\qquad g_0=X^*e,
\tag{1.12}
$$
有全局准确恒等式
$$
F_\varepsilon^*e-g_\varepsilon
=\varepsilon^3\mathcal P_{\ne0}
   (dZ\cdot dY+dY\cdot dZ)
 +\varepsilon^4\mathcal P_{\ne0}(dY\cdot dY).
\tag{1.13}
$$
$g_\varepsilon$ 对每个实数 $\varepsilon$ 都正定；充分小的
$|\varepsilon|$ 下 $F_\varepsilon$ 是闭 $C^2$ 嵌入。
(1.13) 的右端一般仍非零，本定理没有将它改成精确等距方程。

## 2. 源项来自实际向量场的度量二次项

写 $k=n-1/n$。由 $T=-U/n$，
$$
Z_\theta=-kU\sin(n\theta)e_r-nW\sin(n\theta)e_z,
$$
$$
Z_s=U_s\cos(n\theta)e_r-\frac{U_s}{n}\sin(n\theta)e_\theta
       +W_s\cos(n\theta)e_z.
\tag{2.1}
$$
所以三个非均值二次项为
$$
\mathcal P_{\ne0}|Z_\theta|^2=-P\cos(m\theta),
$$
$$
\mathcal P_{\ne0}\langle Z_s,Z_\theta\rangle=-Q\sin(m\theta),
$$
$$
\mathcal P_{\ne0}|Z_s|^2=-R\cos(m\theta).
\tag{2.2}
$$
特别地，$R$ 定义前的负号和 $Q$ 的 $1/2$ 都是由真正的度量分量算出，
不属于符号约定。本文混合分量始终指矩阵条目 $g_{s\theta}$；
若写成二次型，其 $ds\,d\theta$ 项另有常规系数 $2$。

对一般 $m$ 阶场
$$\widehat Y=\widehat U\cos(m\theta)e_r+
 \widehat T\sin(m\theta)e_\theta+\widehat W\cos(m\theta)e_z,$$
直接求导得到三个线性度量方程
$$
2a(\widehat U+m\widehat T)=P,
\tag{2.3}
$$
$$
a\widehat T_s-a_s(m\widehat U+\widehat T)-mz_s\widehat W=Q,
\tag{2.4}
$$
$$
2(a_s\widehat U_s+z_s\widehat W_s)=R.
\tag{2.5}
$$
由 (2.2)，它们正好等价于 (1.11)。

## 3. 把三个方程准确消成真实 $L_6$

(2.3) 先给 $\widehat T=(C-\widehat U)/m$。由
$$a_s=-v/p,\qquad z_s=1/p,\qquad \partial_s=(h^2/p)\partial_x,$$
把这个式子代入 (2.4)，再乘以 $mp$，得到
$$
m^2\widehat W=(m^2-1)v\widehat U-h\widehat U'+J.
\tag{3.1}
$$
令 $\eta=h\widehat U$，右端恰为 $m^2(v/h)\eta-\eta'+J$，
因而 (3.1) 就是 (1.9) 的第三式。

同样，(2.5) 等价于
$$
\widehat W'-v\widehat U'=\frac{p^2}{2h^2}R.
\tag{3.2}
$$
设 $w=v/h$，则 $w'+w^2=q$。利用 (1.9) 算得
$$
\widehat W'-v\widehat U'
=q\eta-\frac{\eta''}{m^2}+\frac{J'}{m^2}
=\frac{L_m\eta+J'}{m^2}.
\tag{3.3}
$$
因此第三个方程准确等价于 $L_m\eta=f$。对 $m=6$，R4 第 3—4 节
给出 $\ker L_6=0$ 及真实 $L^2$ 逆。一旦下节证明 $f\in L^2$，
(1.8)—(1.10) 即同时满足全部三个度量方程。没有遗留积分常数或端点
匹配方程。

这些函数还保持所需反射结构：$h,p,q,y,U,P,C,R$ 为偶函数，
$v,W,Q,J$ 为奇函数，所以 $f$ 为偶函数。$L_6$ 与实共轭、反射交换，
逆解的唯一性遂给 $\eta$ 为实偶函数。于是 $U_6,T_6$ 为偶函数，
$W_6$ 为奇函数。

## 4. 源项的真实双端衰减

先补强 R4 的 $h'/h\to\mu$，以固定指数处理各个源项。
在 $x\ge0$ 上，$w=h'/h$ 满足
$$w'=q-w^2,\qquad w(0)=0.$$
因 $q<\mu^2$，在 $w=\mu$ 处导数严格为负，故首次交叉论证给
$w<\mu$。令 $d=\mu-w>0$，则
$$
d'+(\mu+w)d=A\operatorname{sech}^2x.
\tag{4.1}
$$
R4 已证 $w\to\mu$，故存在 $x_0$ 与常数 $\kappa>2$，使
$\mu+w\ge\kappa$ 于 $x\ge x_0$。又
$\operatorname{sech}^2x\le4e^{-2x}$。积分因子于是给
$$
0<d(x)\le d(x_0)e^{-\kappa(x-x_0)}
 +4A\int_{x_0}^x e^{-\kappa(x-t)}e^{-2t}\,dt
 =O(e^{-2x}).
\tag{4.2}
$$
因此 $(\log h-\mu x)'=-d$ 可积，其积分极限有限。存在 $c>0$ 使
$$
h(x)=ce^{\mu x}(1+O(e^{-2x})),\qquad
w(x)=\mu+O(e^{-2x}).
\tag{4.3}
$$
对 Riccati 方程求导，归纳得到 $w-\mu$ 的每个固定有限阶导数都是
$O(e^{-2x})$；$h$ 的每个固定有限阶导数则是 $O(e^{\mu x})$。
偶性给另一端的相应陈述。

由于 $y$ 及其各阶导数为 $O(e^{-3\mu|x|})$，并且
$$p\asymp h,\qquad \frac{h^2}{p}=O(e^{\mu|x|}),$$
(1.3)—(1.7) 给出下表。每一行同时适用于任意预先固定的有限阶
$x$ 导数；这是由乘积法则及 (4.3) 得到的双端界。

| 量 | 双端衰减阶 |
|---|---|
| $U$ | $O(e^{-4\mu|x|})$ |
| $W$ | $O(e^{-3\mu|x|})$ |
| $U_s$ | $O(e^{-3\mu|x|})$ |
| $W_s$ | $O(e^{-2\mu|x|})$ |
| $P$ | $O(e^{-6\mu|x|})$ |
| $Q$ | $O(e^{-5\mu|x|})$ |
| $R$ | $O(e^{-4\mu|x|})$ |
| $C$ | $O(e^{-5\mu|x|})$ |
| $J$ | $O(e^{-4\mu|x|})$ |
| $f$ | $O(e^{-4\mu|x|})$ |

最后一行使用 $p^2/h^2=h^{-2}+w^2$ 连同各固定阶导数有界。
特别地，$f$ 光滑且属于 $L^2(\mathbb R)$，所以第 3 节所用的真实逆
确实作用在合法源上。由 ODE 正则性，$\eta$ 在每个有限区间光滑。

## 5. 逆解衰减及两极 $C^2$ 延拓

这里只使用真实 $H^2$ 解，不用有限区间解替代它。$H^1(\mathbb R)$
函数有连续代表且趋零于两端：例如从平方的导数积分与 Cauchy--Schwarz
得到尾部上界。因此 $\eta$ 与 $\eta'$ 都趋零。

R4 第 5 节已给 $q\ge1$ 于 $x\ge2$。取
$$\beta=4\mu,\qquad b(x)=e^{-\beta(x-2)},\qquad x\ge2.$$
因为 $\beta^2=32$，
$$
L_6b=(36q-32)b\ge4b.
\tag{5.1}
$$
第 4 节保证
$$M_f:=\sup_{x\ge2}|f(x)|e^{\beta(x-2)}<\infty.$$
取任意
$$B\ge\max\{|\eta(2)|,\ M_f/4\}.$$
则 $Bb\pm\eta$ 在左端非负，趋于零，且
$$L_6(Bb\pm\eta)\ge4Bb-|f|\ge0.$$
若其中一个函数取负值，因它在无穷远趋零，会在内部取得负的最小值；
在该点 $-u''+36qu<0$，与上式矛盾。故
$$|\eta(x)|\le Be^{-4\mu(x-2)}\qquad(x\ge2).$$
偶性处理另一端，得到
$$
\eta=O(e^{-4\mu|x|}).
\tag{5.2}
$$
由 $\eta''=36q\eta-f$，二阶导数有同样衰减；由
$\eta'(x)=-\int_x^\infty\eta''(t)\,dt$，一阶导数也有同样衰减。
继续求导即可覆盖所需的任意固定有限阶导数。

于是 (1.9) 给
$$
U_6,T_6=O(e^{-5\mu|x|}),\qquad
W_6=O(e^{-4\mu|x|}),
\tag{5.3}
$$
同样包括各固定阶 $x$ 导数。这比仅要求衰减指数大于 $2\mu$ 更强。

在上极点用 R4 的真实平面图坐标
$$(\xi,\zeta)=(r\cos\theta,r\sin\theta),\qquad r=a=1/h.$$
由 (4.3)，$r\asymp e^{-\mu x}$，且
$$\partial_r=-\frac{h^2}{v}\partial_x=O(h)\partial_x.$$
系数的一次 $x$ 导数也为 $O(h)$；二次径向求导至多花费 $O(h^2)$。
Cartesian 求导还会出现 $r^{-1}\partial_\theta$，但 (1.10) 的角频率
固定，故同样每阶至多花费一个 $O(h)$。由 (5.3)，
$$
|Y|=O(r^4),\qquad |D_{\xi,\zeta}Y|=O(r^3),\qquad
|D^2_{\xi,\zeta}Y|=O(r^2).
\tag{5.4}
$$
这些是完整环境向量场的 Cartesian 分量估计，包含圆柱标架对
$\theta$ 的导数。取 $Y(0)=0$ 后，沿线段积分一阶、二阶导数，或直接
使用 (5.4) 的差商，即可证明延拓为 $C^2$，且二 jet 为零。
下极点完全相同。由连续性，已经在内部成立的 (1.11) 也覆盖两极。

## 6. 完整度量展开与输出平均

R4 已证 $\mathcal B_X(Z)=0$，而第 2—5 节证明了 (1.11)。
因此准确展开给
$$
F_\varepsilon^*e
=g_0+\varepsilon^2\bigl(\mathcal B_X(Y)+dZ\cdot dZ\bigr)
 +\varepsilon^3(dZ\cdot dY+dY\cdot dZ)
 +\varepsilon^4dY\cdot dY.
\tag{6.1}
$$
二阶括号恰为 $\mathcal P_0(dZ\cdot dZ)$。三阶混合项只有
$m-n=3$ 与 $m+n=9$ 阶角模式，因而均值为零；四阶项只有均值与
$2m=12$ 阶模式。这给 (1.12)—(1.13)，并特别给
$$g_\varepsilon=\mathcal P_0(F_\varepsilon^*e).$$

为明确均值，而非仅给抽象投影，写
$A_6=U_6,\ B_6=T_6,\ C_6=W_6$，则在 $(s,\theta)$ 坐标中
$$
g_{\varepsilon,ss}
=1+\frac{\varepsilon^2}{2}
  \left[(1+n^{-2})U_s^2+W_s^2\right]
 +\frac{\varepsilon^4}{2}
  \left[(A_6)_s^2+(B_6)_s^2+(C_6)_s^2\right],
\tag{6.2}
$$
$$
g_{\varepsilon,\theta\theta}
=a^2+\varepsilon^2P+\frac{\varepsilon^4}{2}
 \left[(mA_6+B_6)^2+(A_6+mB_6)^2+m^2C_6^2\right],
\qquad g_{\varepsilon,s\theta}=0.
\tag{6.3}
$$
坐标退化的极点处使用旋转群平均的张量定义，避免把
$g_{\theta\theta}=0$ 误当成度量退化。平均的每个二次项都是半正定，
且 $g_0$ 是正定度量，故 $g_\varepsilon$ 对全部实参数正定。
在极点这些附加项均为零。$X,Z,Y$ 的 $C^2$ 正则性保证上述度量及
残差在闭面上至少为 $C^1$。

由于 $Z,Y$ 是固定闭面上的 $C^2$ 场，$\varepsilon Z+\varepsilon^2Y$
在 $C^1$ 中趋零；闭嵌入的 $C^1$ 开放性遂保证充分小参数的嵌入性。
也可直接分两步看：有限坐标覆盖给统一局部浸入与局部单射，
紧集上相隔固定参数距离的点对由 $X$ 的单射性有正的像距离；
足够小的 $C^1$、$C^0$ 变化分别保持这两类点对不重合。
这只是存在某个小参数区间，不给指定有限振幅的认证。

## 7. 结果的使用范围

本结果把 R4 的一个真实无穷小场推进到真实全局二阶校正：
没有形式截断径向 ODE，没有未付的两极延拓，也没有把非均值二阶源留给
另一个未知解。输出平均度量后，剩余非均值误差具有准确的三阶、四阶
多项式表达，可作为下一步共振投影或后验求解的具体输入。

仍须解决的内容是三阶起的方程（特别是三阶重新出现的 $n=3$ 核投影）、
有限振幅的收敛或后验定理，以及具有内点的固定握持集。两极的零二 jet
不能替代固定开帽。本文也没有把某个浮点残差很小解释成精确等距。

复现入口：
[脚本](../scripts/poschl_teller_second_order.py)、
[诊断笔记](../notes/2026-11-10-poschl-teller-second-order-diagnostic.md)、
[诊断 JSON](../notes/2026-11-10-poschl-teller-second-order-diagnostic.json)。
