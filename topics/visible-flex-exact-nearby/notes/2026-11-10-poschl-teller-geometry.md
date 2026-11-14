# 显式单共振背景的全解析几何界

2026-11-10，visible-exact-astra-76e8 / geometry_transfer。

**状态：已证明，正文登记为 R5。** 全部结论通过解析比较和有理不等式得到；没有使用浮点 ODE 轨道、采样曲率或采样支撑作证书。本结果量化 R4 的闭旋转背景，另给宽松扰动预算和显式固定小平帽的几何改造；不构造非线性弯曲，也不把改帽前的谱结论搬到改帽后。

## 1. 对象及结论

沿用本题 R4 的唯一背景。令

$$
\delta=\frac{\sqrt2}{3},\qquad A=2+\delta,
\qquad q(x)=2-A\operatorname{sech}^2x,
$$

$$
h''=qh,\qquad h(0)=1,\qquad h'(0)=0.
\tag{1.1}
$$

记

$$
v=h',\quad p=\sqrt{1+v^2},\quad a=h^{-1},
\quad z(x)=\int_0^x h(u)^{-2}\,du,
$$

$$
X(x,\theta)=(a(x)\cos\theta,a(x)\sin\theta,z(x)).
\tag{1.2}
$$

R4 §5 已证明两端补极点后得到闭 $C^2$ 嵌入球面。本 note 的界为

$$
\boxed{h(x)>4/5\quad(x\in\mathbb R)},\qquad
\boxed{Z:=z(+\infty)<13/4},
\tag{1.3}
$$

$$
\boxed{|X|<\frac{\sqrt{194}}4,\quad
D:=\operatorname{diam}X(S^2)<7},
\tag{1.4}
$$

$$
\boxed{|\kappa_i|<12/5,\qquad X\cdot n>7/10},
\tag{1.5}
$$

以及全局厚度

$$
\boxed{\operatorname{reach}(X(S^2))\ge5/12,
\qquad \frac{\operatorname{reach}(X(S^2))}{D}>\frac5{84}>0.0595.}
\tag{1.6}
$$

这里 $n$ 是外法向，中心固定为原点。证明包含实际曲面的全局支撑和法向管，故 (1.6) 不是仅凭局部主曲率作出的推断。$5/84$ 比本题要求的 $0.03$ 留有明确余量，但这个旋转背景自身没有非平凡的相位弯曲。

## 2. 一个简单的正性比较及局部下界

以下只需

$$7/15<\delta<1/2,\qquad A<5/2.\tag{2.1}$$

令 $y(x)=\operatorname{sech}^{\delta}x$。直接求导给

$$
\frac{y''}y=\delta^2-\delta(\delta+1)\operatorname{sech}^2x,
$$

$$
q-\frac{y''}y=(2-\delta^2)\tanh^2x\ge0.
\tag{2.2}
$$

在 $h$ 的任意正区间上，Wronskian 满足

$$
(h'y-hy')'=(q-y''/y)hy\ge0.
$$

它在 $0$ 处为零，因此 $(h/y)'\ge0$，且 $h/y\ge1$。若 $h$ 在正半轴有首个零点，这个不等式在首零点前成立，取极限矛盾。因此 $h>0$ 且

$$h(x)\ge\operatorname{sech}^{\delta}x\qquad(x\ge0).\tag{2.3}$$

这也独立给出 R4 的正性，不需要其谱因式分解。

在 $0\le x\le1$，由 $\delta<1/2$，

$$h(x)\ge\frac1{\sqrt{\cosh x}}\ge\frac1{\sqrt{\cosh1}}>\frac45.\tag{2.4}$$

最后一步可纯有理验证：$\cosh1$ 从 $1/4!$ 开始的级数项比至多 $1/30$，故

$$
\cosh1<\frac32+\frac{1/24}{1-1/30}
=\frac{179}{116}<\frac{25}{16}.
$$

## 3. 区间 [0,1] 上的显式上解

令 $u=x^2$，并取

$$H(x)=1-\frac{x^2}{5}+\frac{x^4}{5}.
\tag{3.1}$$

将证明 $h\le H\le1$ 于 $[0,1]$。

首先，对 $0\le x\le1$ 有

$$\tanh^2x\le\frac{3x^2}{3+2x^2}.\tag{3.2}$$

一个直接证明是

$$
\frac{\sinh^2x}{x^2}
=\sum_{j\ge0}c_jx^{2j},\qquad
c_j=\frac{2^{2j+1}}{(2j+2)!},
$$

其中 $c_0=1$ 且 $c_{j+1}/c_j\le1/3$。因此
$\sinh^2x\le3u/(3-u)$，再应用递增函数 $s\mapsto s/(1+s)$ 即得 (3.2)。

由 $q=-\delta+(2+\delta)\tanh^2x$、(2.1)、(3.2)，以及 $u\le1$，

$$q(x)\le Q(u):=\frac{-21+97u}{15(3+2u)}.\tag{3.3}$$

$H$ 在本区间严格为正。直接有理展开给

$$
H''-QH
=\frac{15-26u+478u^2-97u^3}{75(3+2u)}>0.
\tag{3.4}
$$

分子的正性无需数值求最小值：由于 $0\le u\le1$，

$$
15-26u+478u^2-97u^3
\ge15-26u+381u^2
=381\left(u-\frac{13}{381}\right)^2
+15-\frac{169}{381}>0.
$$

故 $H''-qH>0$。又 $H(0)=h(0)$、$H'(0)=h'(0)=0$，利用已证 $h>0$ 得

$$
(H'h-Hh')'=h(H''-qH)>0,
$$

所以 $(H/h)'>0$ 于 $(0,1]$，$H\ge h$。结合 $H=1-u(1-u)/5\le1$，得到

$$\boxed{4/5<h(x)\le1\qquad(0\le x\le1).}\tag{3.5}$$

而 $h(x)<1$ 对 $0<x\le1$ 成立。

## 4. 在 x=1 处严格转为增长，并付清整个尾

$q$ 在正半轴严格增加，且 $q(0)=-\delta>-1/2$。由
$\cosh(1/2)>1+(1/2)^2/2=9/8$，有

$$q(1/2)>2-\frac{5/2}{81/64}=\frac2{81}>0.$$

所以负部仅支持在 $(0,1/2)$。这里 $q_-=\max\{-q,0\}$、$q_+=\max\{q,0\}$。由 $\tanh x\le x$，直接对差求导可得 $\tanh x\ge x-x^3/3$；故在 $[0,1/2]$ 上 $\tanh x\ge11x/12$。利用 $A>12/5$、$\delta<1/2$，

$$q(x)\ge-\frac12+\frac{121}{60}x^2\qquad(0\le x\le1/2).$$

因此负部积分满足

$$
N:=\int_0^1q_-(x)\,dx
\le\int_0^{\sqrt{30}/11}
\left(\frac12-\frac{121}{60}x^2\right)dx
=\frac{\sqrt{30}}{33}<\frac16.
\tag{4.1}
$$

总积分是

$$T:=\int_0^1q(x)\,dx=2-A\tanh1>1/13.\tag{4.2}$$

这里 $\tanh1<10/13$ 可由 $e<11/4$ 得出：
$e^2<121/16<23/3$，而 $\tanh1=(e^2-1)/(e^2+1)$。
所用 $e<11/4$ 亦是有理级数界：

$$e<1+1+1/2+1/6+\frac{1/24}{1-1/5}=87/32<11/4.$$

记 $P=\int_0^1q_+$。由 (3.5)，负部用 $h\le1$，正部用 $h>4/5$，得到

$$
h'(1)=\int_0^1qh
>\frac45P-N
=\frac45T-\frac15N
>\frac4{65}-\frac1{30}
=\frac{11}{390}>0.
\tag{4.3}
$$

对 $x\ge1$，用 $\cosh1>3/2$，有

$$q(x)>2-\frac{5/2}{9/4}=\frac89=:k^2,
\qquad k=\frac{2\sqrt2}{3}.\tag{4.4}$$

因为 $h>0$，$h''>0$；由 (4.3)，$h'>0$ 在整个 $[1,\infty)$ 上成立。因此 (3.5) 的下界扩展到全半轴。由偶性，全轴都有 $h>4/5$。

与常系数方程比较，或直接写 $\partial_x^2-k^2$ 的正 Green 核，给

$$h(x)>\frac45\cosh(k(x-1))\qquad(x\ge1).\tag{4.5}$$

于是

$$
Z=\int_0^\infty\frac{dx}{h(x)^2}
<\frac{25}{16}+\frac{25}{16}\int_0^\infty\operatorname{sech}^2(ku)\,du
=\frac{25}{16}+\frac{75}{32\sqrt2}<\frac{13}{4}.
\tag{4.6}
$$

最后一个比较等价于 $75<54\sqrt2$，平方后是 $5625<5832$。

还需要一个全尾能量界。由 (4.4) 及 $h'>0$，

$$
\frac d{dx}\left(h'^2-\frac89h^2\right)
=2hh'\left(q-\frac89\right)>0.
$$

在 $x=1$，$h(1)<1$，故

$$h'^2-\frac89h^2>-\frac89\qquad(x\ge1).\tag{4.7}$$

特别地

$$
p^2>\frac89h^2+\frac19,
\qquad h^2<1+\frac98v^2.
\tag{4.8}
$$

## 5. 直径和实际主曲率

由 $a=1/h<5/4$ 和 $|z|<13/4$，

$$|X|^2<\frac{25+169}{16}=\frac{194}{16}.$$

因此 $D<\sqrt{194}/2<7$，没有假定直径由两极取得，也没有把采样包围球当作全图界。

由 R4 §5 的经线公式，实际主曲率的绝对值由

$$\kappa_\theta=\frac hp,\qquad
\kappa_r=\frac{h^2h''}{p^3}
=q\left(\frac hp\right)^3
\tag{5.1}$$

给出（整体法向符号不影响以下绝对值）。在 $[0,1]$，$h/p\le h\le1$；在 $[1,\infty)$，(4.8) 给

$$\frac hp<\frac3{2\sqrt2}.$$

又 $|q|\le2$，故全轴有

$$
|\kappa_\theta|\le\frac3{2\sqrt2}<\frac{12}{5},\qquad
|\kappa_r|\le\frac{27}{8\sqrt2}<\frac{12}{5}.
\tag{5.2}
$$

后一比较平方后为 $135^2<2\cdot96^2$，即 $18225<18432$。R4 已证明补极点为 $C^2$，所以主曲率界在两极由连续性保留。

## 6. 同心正支撑下界

外法向及支撑准确为

$$n=\frac{e_r+v e_z}{p},\qquad
X\cdot n=\frac{1/h+zv}{\sqrt{1+v^2}}.\tag{6.1}$$

因为 $h$ 偶、$v$ 奇、$z$ 奇，支撑为偶函数，只需 $x\ge0$。

### 6.1 在 0≤x≤1 且 v≤0 的部分

由 (4.1) 和 $h\le1$，

$$v(x)=\int_0^xqh\ge-N>-1/6.$$

又 $1/h\ge1$、$z\le25/16$。所以

$$X\cdot n>\frac{1-25/96}{\sqrt{1+1/36}}
=\frac{71}{16\sqrt{37}}>\frac7{10}.\tag{6.2}$$

### 6.2 在 0≤x≤1 且 v≥0 的部分

由 $h\le1$、$q\le2$，有 $v(x)\le2x$，而 $z(x)\ge x$。故

$$X\cdot n\ge\frac{1+v^2/2}{\sqrt{1+v^2}}\ge1.\tag{6.3}$$

最后一步平方即得，差为 $v^4/4$。

### 6.3 整个 x≥1 的尾

这里 $z\ge z(1)>1$、$v>0$。由 (4.8)，

$$h^2<1+\frac98v^2<(p+v)^2.$$

所以 $1/h>1/(p+v)=p-v$，从而

$$X\cdot n=\frac{1/h+zv}{p}>1.$$

三部分合起来证明全轴 $X\cdot n>7/10$。两极的支撑等于 $Z>1$，所以补极点后也有统一下界。

## 7. 全局 reach 与用途

本题 R1 §3.2（亦即相邻课题 R10）的法向管命题适用于真实闭 $C^2$ 图：

$$
X\cdot n\ge\sigma>0,\quad |\kappa_i|\le K
\quad\Longrightarrow\quad
\operatorname{reach}(X(S^2))\ge\min\{\sigma,1/K\}.
$$

其理由是所有 $|s|<\min\{\sigma,1/K\}$ 的平行面 $X+sn$ 都是正径向图，且各射线上的半径随 $s$ 严格增加，所以整条法向管全局单射。

取 $\sigma=7/10$、$K=12/5$，得到

$$\operatorname{reach}(X(S^2))\ge5/12,$$

再用 $D<7$ 即得 (1.6)。这些界与 R4 的全整数频率谱隙属于同一个明确背景，不引用 flat17 的任何几何证书。

## 8. 允许位置误差 .1、二阶误差 1 的明确几何邻域

在上述真实背景 $S=X(S^2)$ 上取 Cartesian 校正 $G=\mathrm{id}+U$。导数使用参考诱导联络，设

$$
\boxed{\|U\|_\infty\le\frac1{10},\qquad
\|\nabla U\|_\infty\le\frac1{10},\qquad
\|\nabla^2U\|_\infty\le1.}
\tag{8.1}
$$

这里是当前归一化下的绝对数值，不是把 $d$ 混入的相对量。R1 §3 的曲率变换立即给

$$K_{\rm new}\le
\frac{12/5+1}{(1-1/10)^2}=\frac{340}{81}.
\tag{8.2}$$

正支撑用 R1 已证的较准法向角关系。若 $b=\|\nabla U\|\le1/10$，则

$$
|n_{\rm new}-n|^2
\le\frac{2b^2}{1+\sqrt{1-b^2}}
\le\frac2{199}<\left(\frac{101}{1000}\right)^2.
$$

所以新图的同心支撑满足

$$
\sigma_{\rm new}>
\frac7{10}-\frac72\frac{101}{1000}-\frac1{10}
=\frac{493}{2000}>\frac{81}{340}.
\tag{8.3}
$$

沿直线同伦的同一正支撑界还保证它是嵌入。因此

$$
\boxed{\operatorname{reach}(G(S))\ge\frac{81}{340},
\qquad D_{\rm new}<\frac{36}{5},
\qquad \frac{\operatorname{reach}(G(S))}{D_{\rm new}}
>\frac9{272}>0.03308.}
\tag{8.4}
$$

这给非线性构造可直接使用的宽几何预算；(8.1) 自身不说明任何等距方程或可见振幅已经成立。

## 9. 一个实际的显式 C² 小平帽改造

本节构造两个具有内部的平帽，保留 (8.4)。它只是更换径向背景，改帽后的 Sturm 逆和三阶共振必须另证。

### 9.1 在 x≥12 处付清平面图的二阶近似

令 $w=h'/h$。Riccati 方程为 $w'=q-w^2$。因为 $q\le2$、$w(0)=0$，标量比较给 $w<\sqrt2$。另一方面，$e>8/3$ 且

$$(8/3)^{12}>100000,$$

所以对 $x\ge6$，

$$q(x)>2-10e^{-2x}>\frac{19999}{10000}=:\gamma^2.$$

由 $w(6)>0$，常系数比较给

$$w(x)\ge\gamma\tanh(\gamma(x-6)).$$

这里 $\gamma>140/99$；当 $x\ge12$，$\gamma(x-6)>8$。又 $e^{16}>2^{16}>19999$，故 $\tanh8>9999/10000$。于是

$$
\boxed{\frac{707}{500}
=\frac{140}{99}\frac{9999}{10000}
<w(x)<\sqrt2\qquad(x\ge12).}
\tag{9.1}
$$

在上极点附近以 $r=a=1/h$ 为平面极径，把原曲面写为 $z=f(r)$，并记 $\kappa=1/\sqrt2$。由 R4 的准确公式，

$$f'(r)=-\frac r{w},\qquad f''(r)=-\frac q{w^3}.$$

定义

$$E(r)=Z-f(r)-\frac{\kappa r^2}{2}.$$

在 (9.1) 的区域，径向 Hessian 的两个特征值为
$q/w^3-\kappa$ 和 $1/w-\kappa$。用

$$
\frac{707}{1000}<\kappa,\quad
\frac{2}{(707/500)^3}<\frac{708}{1000},\quad
\frac{500}{707}<\frac{708}{1000},
$$

以及 $q/w^3\ge(19999/20000)\kappa$，得到

$$
\boxed{\|D^2E\|<\frac1{1000},\qquad
|DE|<\frac r{1000},\qquad
|E|<\frac{r^2}{2000}.}
\tag{9.2}
$$

后两式由极点处 $E=DE=0$ 积分得到。所有常数不涉及数值 ODE。

### 9.2 显式三次径向剖面

置 $L=11/2$。定义连续分段仿射函数

$$
\beta(u)=
\begin{cases}
1,&0\le u\le1,\\
3-2u,&1\le u\le2,\\
-1,&2\le u\le7/2,\\
2u-8,&7/2\le u\le9/2,\\
11/2-u,&9/2\le u\le11/2,\\
0,&u\ge11/2.
\end{cases}
$$

直接积分给 $\int_0^L\beta=0$、$\int_0^Lu\beta(u)\,du=-29/24$。令

$$
\Phi(u)=\int_u^L(s-u)\beta(s)\,ds\quad(0\le u\le L),
\qquad \Phi(u)=0\quad(u\ge L).
$$

则 $\Phi$ 为 $C^2$ 分段三次函数，$\Phi''=\beta$，且

$$
\Phi(u)=-29/24+u^2/2\quad(0\le u\le1),\qquad
|\Phi''|\le1,\qquad |\Phi'(u)/u|\le1.
\tag{9.3}
$$

最后一式来自 $\Phi'(u)=\int_0^u\beta$。因此径向函数 $\Phi(|y|)$ 的完整平面 Hessian 范数至多 1，且在原点和外边缘均真正 $C^2$。

另取 $C^2$ 截断函数

$$
\chi(u)=
\begin{cases}
1,&u\le1,\\
1-10t^3+15t^4-6t^5,\quad t=u-1,&1\le u\le2,\\
0,&u\ge2.
\end{cases}
$$

有 $|\chi|\le1$、$|\chi'|\le15/8$、$|\chi''|\le6$；后两项由 $\chi'=-30t^2(1-t)^2$ 及 $\max_{|w|\le1}15|w|(1-w^2)=10/\sqrt3<6$ 得到。

### 9.3 明确选择帽半径并验证所有校正界

取

$$\varepsilon=10^{-10}.$$

由于 $h''\le2h$，正 Green 核比较给 $h(x)\le\cosh(\sqrt2x)$。因此

$$h(12)<e^{18}<3^{18}<10^9,\qquad a(12)>10^{-9}>L\varepsilon.$$

所以支撑区域 $r\le L\varepsilon$ 完全落在已经证明 (9.2) 的极点图内。定义上帽的竖直校正

$$
\psi(r)=\kappa\varepsilon^2\Phi(r/\varepsilon)
+\chi(r/\varepsilon)E(r),
\tag{9.4}
$$

并在其支撑之外延零。下帽作 $z=0$ 镜像校正。

在 $r\le\varepsilon$ 内，(9.3)、(9.4) 精确给

$$f(r)+\psi(r)=Z-\frac{29\kappa}{24}\varepsilon^2,$$

所以新帽确实是一片平圆盘；不是只在极点有零二 jet。

由 (9.2) 和截断导数界，$r\le2\varepsilon$ 上有

$$
|(\chi E)''|
\le\frac1{1000}
+2\frac{15}{8\varepsilon}\frac{2\varepsilon}{1000}
+\frac6{\varepsilon^2}\frac{(2\varepsilon)^2}{2000}
=\frac{41}{2000}.
$$

切向 Hessian 特征值的绝对值至多 $23/8000$。所以

$$\|D^2\psi\|\le\kappa+\frac{41}{2000}<\frac34.$$

又 $D\psi(0)=0$，并在外边缘有零二 jet，因而

$$|D\psi|\le\frac34r<5\varepsilon,\qquad
|\psi|<12\varepsilon^2.$$

将它转为参考曲面的诱导联络范数，不需要 $C^3$：图度量为
$g_{ij}=\delta_{ij}+f_if_j$，并有
$\Gamma_{ij}^k=g^{k\ell}f_\ell f_{ij}$。在该小图上 $|Df|<r$、$\|D^2f\|<1$，所以

$$
\|\nabla^2(\psi e_z)\|
\le\|D^2\psi\|+|Df|\,\|D^2f\|\,|D\psi|
<\frac34(1+r^2)<1.
$$

诱导度量不小于平面度量，故一阶范数也至多 $|D\psi|$。两帽的支撑互不相交，校正延零为全局 $C^2$。因此这个实际改造严格满足 (8.1)，并保有 (8.4) 的 reach 比例。

两闭平帽的参数原像组成 $H$，内部非空；修改后的参数化记为 $X_{\rm cap}$。旧两极间距 $2Z>2$，而两极各移动不超过 $1/10$，所以

$$\operatorname{diam}X_{\rm cap}(H)>9/5,\qquad
\frac{\operatorname{diam}X_{\rm cap}(H)}{D_{\rm new}}>\frac14>\frac15.$$

这个 $H$ 可以由两块不相连的帽组成，符合本题对握持区的定义。当前改造仍为旋转背景；它未带来形状变化。要把它用于弯曲族，必须重新证明改帽后真实非径向方程的可解性、频率逆、公共两 jet 和非线性振幅，不能保留 R4 的原 Sturm 势或把原核直接截断后称为等距弯曲。
