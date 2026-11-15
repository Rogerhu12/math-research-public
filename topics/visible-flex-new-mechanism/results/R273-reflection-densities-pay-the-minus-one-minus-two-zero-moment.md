# R273：真实左尾与平方密度对称自动支付另一 Gaussian 第零外矩

日期：2026-11-15。**完整纸面证明；没有执行求积、符号程序、人工检查或研究计算。**

本稿接 [R270 的真实奇母扰动与四变量 IFT](R270-odd-mother-perturbation-pays-a-further-Gaussian-zero-moment.md)。对该稿已经构造的最终四个完整 block，原 $A_{-1,-2}$ 面积的第零外矩对全部 $\theta$ **已经准确为零**；不需要再增加母形参数、再解一条 IFT，或修改已经选定的有限正宽 profile。

关键不是把单包的二次场假定为紧支撑。四条原 self 含有真正的 $\mu_0^2$ 项；它们与 [R259 的有序跨包核](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md) 合成一个完整 primitive 配对。该配对的 even 角部分由真实平方密度的镜像对称消去，odd 角部分仍由原十二完整副本支付。

结论增加一个完整角函数的第零外矩。原72条面积账中，R270 后尚未支付的20条形式 even 等式可减为18条；这不是独立秩结论。本稿不支付 $A_{-1,-2}$ 的 $I_1,I_2$，也不声称完整 ruling 已解。

## 1. 原槽、原系数与固定约定

沿用同一右锚 primitive

$$
J(F)(x)=\int_x^{r_*}F(y)\,dy,\qquad J'=-F,
$$

及原对称双线性二次算子。为避免 $s_0,s_1$ 混记，写

$$
L=\Phi_{p_0},\quad T=\Phi_{s_1},\quad
R=\Phi_{r_1},\quad U=\Phi_{s_0}.
\tag{1}
$$

这里 $T$ 只是 $\Phi_{s_1}$ 的简称，不是 R238 的能量算子 $\mathcal T$。Gaussian 方向仍是

$$
B_{-1}=dL+eT,\qquad B_{-2}=aR+bU.
\tag{2}
$$

$a,b,d,e$ 完全使用原 germ 的系数。下文的恒等式不需要除以其中任何一个，也不需要额外排除它们的退化点。特别适用于 R270 采用的小非零共振参数。

对任意实紧微包 $u$，定义

$$
v=u',\quad r=u'',\quad t=u''',\quad
\mu=\int r^2,\quad
N(u)=\int v r^3,\quad
M(u)=\int x r^4.
\tag{3}
$$

外配对为 $I_0(p,q)=\int p''q''$。本文的 self 规范是

$$
S_{X,Y}(u)=2I_0\{u,[X,Y](u;u\odot u)\}.
\tag{4}
$$

因此它与“单独的 $I_0$”相差因子2。交换子保持 R259 的完整三槽顺序，不能只用 pure 对角值代替整个圆。

## 2. 四条 nonlegal self：原 primitive 与 Green 项

置

$$
A=J(r^2),\quad
A_1=J(xr^2),\quad
A_2=J(x^2r^2+2v^2).
$$

原二次对角式为

$$
\begin{aligned}
R(u,u)&=v^2+xA,& U(u,u)&=A_1,\\
L(u,u)&=uv-\frac{xv^2}{2}-\frac{x^2A}{4}+\frac{A_2}{4},&
T(u,u)&=xv^2+xA_1+\frac{A_2}{2}.
\end{aligned}
\tag{5}
$$

这些单包输出一般都有左多项式尾。需要的准确导数是

$$
\begin{aligned}
R'&=2vr+A-xr^2,& R''&=2(v-xr)t,\\
U'&=-xr^2,& U''&=-r^2-2xrt,\\
L''&=(u-xv)t-\frac{xr^2+A}{2},\\
T''&=(2xv-3x^2r)t+2vr-2xr^2.
\end{aligned}
\tag{6}
$$

R259 的 local cubic 函数为

$$
F_R=F_U=-\frac13\int r^3,\qquad
F_L=-\frac12\int vr^2,\qquad
F_T=\int(vr^2-xr^3).
\tag{7}
$$

对单包，先计算这些 local 表达式沿原二次输出的变分，再补真实 Green 项。其符号可固定为

$$
S_{X,Y}
=
DF_X[\Phi_Y(u,u)]-DF_Y[\Phi_X(u,u)]
+
\left(X'''Y-X''Y'+X'Y''-XY'''\right)_{\rm left}.
\tag{8}
$$

右端所有原输出及导数在共同零 collar 为零。式(8)来自原 local adjoint，不把 local 函数身份扩展成“任意非紧 profile 的原函数”。

单包左尾为

$$
R=\mu x,\quad U=\mu_1,\quad
L=-\frac{\mu x^2}{4}+\frac{\mu_2}{4},\quad
T=\mu_1x+\frac{\mu_2}{2}.
\tag{9}
$$

因此四对中只有 $(L,R)$ 的 Green 项非零，准确为 $+\mu^2/2$。另外

$$
\int A r^2=\frac{\mu^2}{2}.
\tag{10}
$$

这个 primitive 的左常尾必须先保留。代入(6)—(10)，得到

$$
\boxed{
\begin{aligned}
S_{L,R}(u)&=\frac{N-M}{3},\\
S_{L,U}(u)&=\frac{N-M}{3}-\frac{\mu^2}{4},\\
S_{T,R}(u)&=\frac{8N}{3}-\frac{11M}{6}+\frac{\mu^2}{2},\\
S_{T,U}(u)&=\frac{2N}{3}-\frac{5M}{6}.
\end{aligned}}
\tag{11}
$$

为明确端项没有隐藏，第一条的 local 变分差是 $(N-M)/3-\mu^2/2$，加上(8)的 $+\mu^2/2$ 后才得到(11)。第二、第三条剩余的 $\mu^2$ 不能因“最终圆合法”就在单包层删掉。

所需分部积分只有紧 $u$ 的恒等式，例如

$$
\int vr^2t=-\frac13\int r^4,\quad
\int xv r^2t=-\frac13(N+M),\quad
\int ur^2t=-\frac N3,\quad
\int v^2rt=-N.
\tag{12}
$$

式(12)第一条仅为独立可用的短式；其余三条直接给(11)的 $N,M$ 系数。

## 3. 完整有序微包公式

取按从左至右排序、互不交的真实微包

$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i.
$$

伴随母包也可按其内部真实子包展开成这种形式，不能把一个方向不同的 outer 包直接当成单个 rank-one 包。

记

$$
c_i=a_i\cos\theta+b_i\sin\theta,\qquad
d_i=a_i^2-c_i^2,
$$

以及

$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta.
$$

定义三个原系数组合

$$
k=\frac{db}{2}-ea,\qquad
p=\frac{d(a+b)+2e(4a+b)}{3},\qquad
\mathfrak d=2d(a+b)+e(11a+5b).
\tag{13}
$$

由(11)，单包 self 是

$$
S_{B_{-1},B_{-2}}(u)
=pN(u)-\frac{\mathfrak d}{6}M(u)-\frac{k}{2}\mu^2.
\tag{14}
$$

R259 的原跨包核为

$$
\Gamma_{B_{-1},B_{-2},0}(\mathbf m_i,\mathbf m_j)
=-k\,\mu_i\mu_j\qquad(i<j).
\tag{15}
$$

self 与 cross 必须共同保留。定义真正的二导槽密度

$$
D_\rho=f''{}^2-\phi_\theta''{}^2
=\sum_i d_i u_i''{}^2.
\tag{16}
$$

这不是 $(f^2-\phi_\theta^2)''''$。原函数配对准确展开为

$$
\int\phi_\theta''{}^2J(D_\rho)
=
\frac12\sum_i c_i^2d_i\mu_i^2
+\sum_{i<j}c_i^2d_j\mu_i\mu_j.
\tag{17}
$$

于是完整外槽恒等式是

$$
\boxed{
\begin{aligned}
2I_0\{\phi_\theta,[B_{-1},B_{-2}](\phi_\theta;D_\theta)\}
={}&p\sum_i c_i^2d_iN(u_i)
-\frac{\mathfrak d}{6}\sum_i c_i^2d_iM(u_i)\\
&-k\int\phi_\theta''{}^2J(D_\rho).
\end{aligned}}
\tag{18}
$$

这里没有将微包左尾删除，也没有把不同 Gaussian 面积的系数互相抵消。式(18)是同一 $A_{-1,-2}$ 的完整角函数。

## 4. 合法三矩把有序项化为两个准确系数

令

$$
F=f''{}^2,\qquad G=g''{}^2,\qquad K=f''g''.
$$

真实二阶圆的零矩给

$$
\int(F-G)=0,\qquad \int K=0,\qquad \int D_\rho=0.
\tag{19}
$$

因此 $J(D_\rho)$ 真正两端为零，且

$$
\int D_\rho J(D_\rho)
=\frac12\left(\int D_\rho\right)^2=0.
$$

由 $\phi_\theta''{}^2=F-D_\rho$ 得到

$$
\boxed{
\int\phi_\theta''{}^2J(D_\rho)
=
\sin^2\theta\,\int FJ(F-G)
-
2\cos\theta\sin\theta\,\int FJ(K).
}
\tag{20}
$$

这是原 primitive 的准确恒等式，不是假定其余条件能把它局部化。写成 R259 的四次角基时，$\sin^2\theta=\cos^2\theta\sin^2\theta+\sin^4\theta$；第二项也有两个 odd 系数。

假设一个完整 base 的 $F,G$ 关于同一中心 $\xi$ 都是偶函数。由(19)，$J(F-G)$ 关于 $\xi$ 为奇函数，且两端为零。故

$$
\int FJ(F-G)=0.
\tag{21}
$$

原定义区间不必整体关于 $\xi$ 对称：所有被积函数可在共同零 collar 外延零，再在实线上作这项反射。式(21)不涉及 $K$ 的奇偶，也没有声称第二个积分自动为零。

## 5. R270 的有限正宽实际 block 满足所需条件

下面使用的是 R270 主 IFT 的**真正有限正宽解**，不是只在 $\delta=0$ 的 leading 系数。

### 5.1 两类平方密度的真实镜像对称

原 low 中心为

$$
t_{k,\ell}=64A(k-c)+A(\ell-31.5),
\qquad 0\le\ell<64,
$$

high 中心为

$$
t_k^{(\rho)}=B(k-c)+\rho A\sigma_k,\qquad
\rho\in\{0,20\},
$$

其中 $n=2048$、$c=(n-1)/2$，
$\sigma_k=(-1)^{\operatorname{popcount}(\lfloor k/4\rfloor)}$。
因为512个四点组的 Thue–Morse 序列反转变号，

$$
\sigma_{n-1-k}=-\sigma_k.
$$

故 high 中心逐点成镜像对；low 在 $(k,\ell)\mapsto(n-1-k,63-\ell)$ 下同样成镜像对。每一类的实平方幅度和宽度固定，均值准确为0。

R270 的普通母包 $u$ 仍然 even，虽然右子包有真实奇扰动；左子包取镜像。这给 $u''{}^2$ 偶。其 TM3 同源伴随 $\widehat u$ 满足 $\widehat u''{}^2=u''{}^2$，故也给同一个平方密度。因此原方向版与伴随版、$\rho=0$ 与 $\rho=20$ 四个 base 都满足(21)。

### 5.2 Local $N$ 的 even 角部分为零

对 even 母包，$N(u)=\int u'(u'')^3=0$。正宽度缩放和平移不改变这个零。伴随版应先拆到真实内部子包；但 even 角系数只含方向的平方和四次方，TM3 的符号不改变这些系数，所有同源导数四次乘积也保持。因此它们准确重组回整个母包的同一个 $N(u)=0$。

所以(18)第一项的两个 even 系数为零。这里没有预先删除 odd 系数。

### 5.3 Local $M$ 的 even 角部分为零

记 $C=\int(u'')^4$。母包 even 给

$$
M\!\left(w^{3/2}u((x-\xi)/w)\right)=\frac{C\xi}{w}.
\tag{22}
$$

两类方向平方为

$$
(a_i^2,b_i^2)=
\begin{cases}
(\alpha q,q),&\text{low，宽度比 }q,\\
(\beta,1),&\text{high，宽度比 }1,
\end{cases}
$$

且原准确代数关系为

$$
q=\frac{1}{16(1-\alpha)^2},\qquad
\beta=\frac{5-\alpha}{1-\alpha}.
\tag{23}
$$

local 四次角函数的两个 even 系数是

$$
\sum_i(a_i^4-5a_i^2b_i^2)M(u_i),\qquad
\sum_i b_i^2(a_i^2-b_i^2)M(u_i).
\tag{24}
$$

不带中心的相应四次和，分别由

$$
64\alpha q(\alpha-5)+\beta(\beta-5)=0,\qquad
64q(\alpha-1)+(\beta-1)=0
\tag{25}
$$

准确消去。两类中心各自均值为0，故共同平移后的 $M$ 和也为0。伴随细分的 even 四次密度与普通版相同，仍适用(22)—(25)。

式(23)—(25)对主 IFT 分支上每个实际 $\alpha(\delta)$ 都成立；真实位置对称也不随其余母参数改变。因此这里没有把只在 leading 根上的消失延用到有限 $\delta$。

结合(18)、(20)、(21)，每个尚未作 odd 包装的完整 base 的 $A_{-1,-2},I_0$ **even 角部分准确为零**。

## 6. 完整复制、odd 支付与最后正幅混合

原八完整副本用于支付完整第三，原十二完整副本用于支付全部36条 odd Gaussian 角条件。它们不是单微包副本：每个被复制的 base 已经有真实三矩，因此其内槽 $D_\theta$ 的三矩为零，所有相应二次 inner 场在整个副本左侧准确为零。不同完整副本之间的(15)跨项因此消失。

even 零也在任意共同平移下保持。具体说，$N$ 不变；$M$ 只增加平移量乘相应的无中心四次和，而其 even 部分由(25)为零；(20)的 primitive 配对共同平移不变。共同实幅度只把这些四次式乘其四次方。故八副本保留已有 even 零。

十二副本按 R259 的实际四次幅权和 $g$ 翻号消去两个剩余 odd 角系数；这里不以平方相同代替该完整包装步骤。于是每个 R270 最终位置 block 都满足

$$
I_0\{\phi_\theta,[B_{-1},B_{-2}](\phi_\theta;D_\theta)\}=0
\qquad\text{对全部 }\theta.
\tag{26}
$$

R269/R270 的四个 block 在各自最终位置先独立解真实有限宽 IFT，再作正幅四次混合。每个完整 block 的 inner 三矩已经为零，所以跨 block 核同样消失；其自身(26)乘正四次幅权仍为零。因此最后用来同时支付 $Q$ 与 sine-four 的幅度选择完整保留(26)。

## 7. 新结论的准确范围

R270 的实际四变量分支已经支付本稿(26)，无需新的几何计算、额外形状参数、重新安装 germ 或修改目标 seed。该结论与 R270 的原三矩、完整第三、六能量、整个 $A_{-2,-3}$ 和 $A_{-1,-3}$、全部36条 odd 面积条件、$A_{1,-3}$ 及 $A_{1,-1}$ 的完整第零外矩共同成立。

新增的是 $A_{-1,-2}$ 的**一个完整外矩**，即其两个尚欠 even 形式系数。原账余18条形式 even 等式，不能当成微分独立秩、连续几何存在证明或所有 Gaussian 面积已经为零。特别，$A_{-1,-2}$ 的第一、第二外矩仍须从原 self、真实有序历史与同一构造继续处理。
