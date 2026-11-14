# R45：同一等距鞍环的全时间 reach 超过初态直径的 3%

**状态：已证明，未参与者全文独审及冻结有理脚本实际独立重放通过；仍是有边环带结果。**

正式登记：root / Astra-visible-flex-db6f0b0e，2026-11-09。
完整作者源固定于 commit 907b834ff56c005ae63cb9757ec6b379d4523b57，
blob 1185f00e0909752adcfea61aa4de03c68ef0f461。
全文独审为 notes/2026-11-09-db6f-tail-review-ruled-annulus-reach-three-percent.md，
commit 2b369645562b3b536fa1ca5fb9a2ea80821258b3，
blob c3d428786de14fd0f3096feb5682e75fc48504d4。
独立审稿人未参与本证明；其于2026-11-09 22:36:00 UTC在functions.exec实际重放
冻结完整JavaScript源，25项精确有理门通过（源blob d0eae43daf679db23f1018927f4591469e4bbc9b）。
root全文读回该完整审稿后正式采纳。基础族已另登记R44；
本文件仅更新标题及登记状态，数学正文保持作者固定源。
2026-11-09。本文只加强已冻结鞍环族的几何估计，不改变其度量、半宽或构造。
允许把隐函数族的正时间区间进一步缩短；这不改变初态和共同度量。
基稿为 geometry-explicit-ruled-saddle-annulus-recovered-v2.md，
commit 456c246b252e102e5a3d29c45b9d4dde7146dcea、
blob 725771192a0ca6a7b2bf09e0302005e011c4be68。

基稿作者为独立几何分工；本增强证明由 root 推导。
本稿不读取或运行主数值候选，不付 G5、闭合连接或可见幅度。
原 v2 的独审不自动支付本稿。

## 1. 精确陈述及统一范围

沿用基稿的 $b>0$、$w=b/20$、固定材料域
$M=[-w,w]\times(\mathbb R/\ell\mathbb Z)$ 及精确族

$$
F_\tau(v,u)=c_\tau(\theta_\tau(u))+v\,d_\tau(\theta_\tau(u)),
\qquad g=dv^2+(b^2+v^2)du^2.
\tag{1}
$$

其中 $|d_\tau|=1$、$k_\tau=|d_\tau'|>0$、
$c_\tau'=b\,d_\tau\times d_\tau'$，撇号表示原角 $\theta$ 导数。
基稿已构造正的 $\varepsilon$，使全部 $|\tau|<\varepsilon$ 的曲线闭合、
材料度量相同、固定片逐点不动，且非零充分小时间的像在全 $\mathrm E(3)$ 下不全等。

**定理。** 可进一步缩小 $\varepsilon>0$，使全部这些时间均满足

$$
\operatorname{reach}(F_\tau(M))\ge \frac b5.
\tag{2}
$$

基稿初态直径 $D=\operatorname{diam}F_0(M)<13b/2$ 因而给

$$
\frac{\operatorname{reach}(F_\tau(M))}{D}>
\frac{2}{65}>\frac3{100}
\quad\text{对全部时间成立。}
\tag{3}
$$

这里的 reach 是包含两条边界的紧像之最近点唯一半径。
本结论不使带边域成为闭曲面，也不产生有效时间幅度或 $\delta_{\rm hold}\ge .05D$。

## 2. 统一微分界和主曲率界

基稿已有 $C^\infty$ 依赖，可把正参数区间缩小，使

$$
\begin{gathered}
\|c_\tau'-c_0'\|_\infty\le b/40,\qquad
\|c_\tau''\|_\infty<7b,\qquad
\|d_\tau''\|_\infty\le20,\\
\frac{14}{5}\le k_\tau\le\frac{31}{10},\qquad
|\kappa_\tau|\le\frac34 .
\end{gathered}
\tag{4}
$$

前三界已由基稿第7节给出。速度范围有严格余量，因为
$2\sqrt2\le k_0<3$。下面核 $\kappa$ 界的严格余量。

基稿记 $\eta=-3+2\sqrt2$、$\sigma=\sqrt{1-\eta^2}$、
$X=\sigma^2\sin^23\theta$，并有

$$
\kappa_0=(d_0)_z\,\Phi(X),\qquad
\Phi(X)=\frac{17+3\eta+X}{(8+X)^{3/2}}.
$$

在 $0\le X\le\sigma^2$ 上，$\Phi>0$、$\Phi'<0$。
由 $\eta<-1/6$、$\sigma<1$、$\sqrt2>113/80$，

$$
|\kappa_0|
\le \sigma\Phi(0)
<\frac{33/2}{16(113/80)}
=\frac{165}{226}<\frac34.
\tag{5}
$$

正则球面曲线的 $\kappa$ 对 $C^2$ 数据连续，故最后一界可由同一次缩区间取得。

令 $a=\sqrt{b^2+v^2}$。在材料正交单位标架
$(\partial_v,a^{-1}\partial_u)$ 中，基稿第二基本形式给形算子

$$
S_\tau=
\begin{pmatrix}
0&-b/a^2\\
-b/a^2&\kappa_\tau/a
\end{pmatrix}.
$$

因 $a\ge b$，其算子范数至多

$$
\|S_\tau\|
\le\frac{3+\sqrt{73}}{8b}<\frac{3}{2b}=:\Lambda .
\tag{6}
$$

此界包括所有点、两条边界及全部时间，不只端点采样。

## 3. 更强的中心线全局弦界

在基稿的固定水平旋转后，

$$
i(c_0)_W=Re^{i\theta}+Pe^{7i\theta}+Qe^{-5i\theta},
\qquad 7P+5Q=\frac{b\sigma}{2}.
$$

对最短圆周角距 $\delta\in[0,\pi]$，几何级数恒等式给
$|\sin(n\delta/2)|\le |n|\sin(\delta/2)$。
只估水平坐标即可得到

$$
|c_0(\theta)-c_0(\phi)|
\ge 2(R-7P-5Q)\sin(\delta/2).
\tag{7}
$$

由 $\eta>-7/40$、$\sigma>49/50$，

$$
R-7P-5Q=\frac{b\sigma(\eta+5)}2
>\frac{9457}{4000}b.
$$

对 $c_\tau-c_0$ 沿最短角弧积分，并用
$\delta\le\pi\sin(\delta/2)$、$\pi<22/7$，从 (4)、(7) 得

$$
\begin{aligned}
|c_\tau(\theta)-c_\tau(\phi)|
&\ge\left(\frac{9457}{2000}-\frac{22}{280}\right)b\sin(\delta/2)\\
&>\frac{23}{5}b\sin(\delta/2)
\ge\frac{161}{110}b\delta .
\end{aligned}
\tag{8}
$$

不等式的严格形式只在 $\delta>0$ 时使用。
这比把竖直余项与水平余项一起减去的旧估计更强。

在 $p=c_\tau(\theta)$ 取任意单位 $\nu\perp c_\tau'(\theta)$。
(4) 的二阶 Taylor 余项与 (8) 给

$$
2|\nu\cdot(q-p)|
\le7b\delta^2
\le\frac{7}{(161/110)^2b}|q-p|^2
\le\frac{|q-p|^2}{\rho_c},
\qquad \rho_c:=\frac{3b}{10}.
\tag{9}
$$

最后一步使用 $(161/110)^2/7>3/10$。
对任意空间点及其最近中心线点，(9) 使距离平方的差在半径 $\rho_c$ 内
严格为正；中心线紧且无边，所以最近点存在且其差向量正交切线。
因此

$$
\operatorname{reach}(c_\tau)\ge\rho_c=\frac{3b}{10}.
\tag{10}
$$

这同时核定全圈单射，且 $w<\rho_c$ 保证基稿的正宽嵌入仍成立。

## 4. 接近的环带点必有接近的原角

写两个像点为
$x=p+v d_\tau(\theta)$、$y=q+\widehat v d_\tau(\phi)$，
并记空间弦长 $h=|x-y|$。
在 $p,q$ 分别应用 (9)，利用两条 ruling 都正交相应中心切线，

$$
(x-y)\cdot(p-q)
\ge\left(1-\frac{w}{\rho_c}\right)|p-q|^2
=\frac56|p-q|^2 .
$$

因而

$$
|p-q|\le\frac65h.
\tag{11}
$$

若 $h<2b/5$，联立 (8)、(11) 得

$$
\sin(\delta/2)<\frac{12}{115}.
$$

另一方面，

$$
\sin(21/200)
\ge\frac{21}{200}-\frac{(21/200)^3}{6}
>\frac{12}{115}.
$$

$\sin$ 在 $[0,\pi/2]$ 严格递增，所以

$$
h<2b/5\quad\Longrightarrow\quad\delta<21/100.
\tag{12}
$$

这里只用已证全局弦估计；没有从局部图的存在直接推断角距小。

## 5. 近点对的内在距离与空间弦比较

选实现 $\delta$ 的有符号最短角差 $\Delta\theta$，
令 $\Delta v=\widehat v-v$。
在原角 $\theta$ 对
$c_\tau(\phi)-c_\tau(\theta)+\widehat v(d_\tau(\phi)-d_\tau(\theta))$
作 Taylor 展开，可写

$$
y-x=Z+\mathcal R,\qquad
Z=\Delta v\,d_\tau(\theta)
 +\bigl(c_\tau'(\theta)+\widehat v\,d_\tau'(\theta)\bigr)\Delta\theta.
$$

由 $d_\tau\perp c_\tau',d_\tau'$ 及
$c_\tau'\perp d_\tau'$，两项正交，且

$$
|Z|^2
=(\Delta v)^2+(b^2+\widehat v^2)k_\tau(\theta)^2\delta^2
\ge(\Delta v)^2+(14b\delta/5)^2 .
\tag{13}
$$

(4) 给余项

$$
|\mathcal R|\le\frac12(7b+w\cdot20)\delta^2=4b\delta^2.
$$

在 (12) 的近点情形，若 $\delta>0$，则

$$
\frac{|\mathcal R|}{|Z|}
\le\frac{10}{7}\delta<\frac3{10}.
$$

$\delta=0$ 时余项为零，结论相同。因此

$$
|Z|\le\frac{10}{7}h.
\tag{14}
$$

把 $v$ 和最短角 lift 同时线性插值，得到留在 $M$ 内的一条比较路径。
其度量在原角写成
$dv^2+(b^2+v^2)k_\tau(\theta)^2d\theta^2$。
由于

$$
\sqrt{1+1/400}<801/800,\qquad
(31/10)(801/800)<25/8,
$$

该路径长度不超过

$$
\sqrt{(\Delta v)^2+(25b\delta/8)^2}
\le\frac{125}{112}|Z|.
$$

结合 (14)，内在距离满足

$$
d_g(P,Q)\le C h,\qquad C=\frac{625}{392},
\quad \text{只要 }h<2b/5.
\tag{15}
$$

这没有把内在距离与材料坐标差或空间弦混为一谈。

## 6. 最短测地线确实留在带边域内

(15) 只给长度上界。用于二阶法向估计的路径还须为内在测地线；
一般带边域的最短路径不能无条件如此处理，故单独证明。

把相同度量 (1) 延伸到完整圆柱
$\widehat M=\mathbb R\times(\mathbb R/\ell\mathbb Z)$。
因 $g\ge dv^2+b^2du^2$，这是完备 Riemannian 流形：
$g$-Cauchy 列先在完整平坦乘积收敛，在所得有限 $v$ 邻域内两度量等价，
故也按 $g$ 收敛。Hopf–Rinow 定理给任意 $P,Q$ 的最短测地线。

按弧长 $s$ 参数化时，测地线方程给

$$
v''=v(u')^2,\qquad J=(b^2+v^2)u'=\text{常数}.
\tag{16}
$$

若 $J=0$，则 $u$ 常值、$v$ 仿射，线段留在端点 $v$ 之间。
若 $J\ne0$，则 $u'$ 处处非零；$v$ 不可能有严格正的内部极大值，
因为那时 (16) 给 $v''>0$；也不可能有严格负的内部极小值。
两端都满足 $|v|\le w$，故整条最短测地线满足 $|v|\le w$。
因此完整圆柱上的最短测地线已经位于 $M$ 内，
并实现带边域内在距离，其长度可用 (15) 控制。

## 7. 包含边界的最近点唯一性

取任意空间点 $z$，设 $p=F_\tau(P)$ 是其最近环带点，
$r=|z-p|<b/5$。最近点因紧性存在。
任取另一个点 $q=F_\tau(Q)\ne p$，记 $h=|q-p|$。

若 $h\ge2b/5$，则 $h>2r$，直接有

$$
|z-q|^2-r^2\ge h^2-2rh>0.
\tag{17}
$$

若 $h<2b/5$，取第6节保证留在 $M$ 内的单位速最短测地线 $\gamma$，
长度 $L=d_g(P,Q)\le Ch$。
最近点条件沿这条可行路径的右导数给

$$
(z-p)\cdot(F_\tau\circ\gamma)'(0)\le0 .
\tag{18}
$$

即便 $P$ 在 $v=\pm w$，(18) 也成立；不要求 $z-p$ 等于曲面通常单位法向。
内在单位速测地线的空间加速度为第二基本形式，
故由 (6) 有 $|(F_\tau\circ\gamma)''|\le\Lambda$。
积分 Taylor 余项得

$$
(z-p)\cdot(q-p)\le\frac12r\Lambda L^2
\le\frac12r\Lambda C^2h^2.
$$

于是

$$
|z-q|^2-r^2\ge(1-r\Lambda C^2)h^2>0,
\tag{19}
$$

因为

$$
r\Lambda C^2<
\frac{3}{10}\left(\frac{625}{392}\right)^2
=\frac{1171875}{1536640}<1.
\tag{20}
$$

(17)、(19) 覆盖全部不同点，每个距像小于 $b/5$ 的空间点最近点唯一。
这证明 (2)。代入基稿的初态直径严格上界 $D<13b/2$，即得 (3)。

## 8. 实际检查和结论边界

附属纯整数/有理数检查器：
scripts/db6f-geometry-ruled-annulus-reach-rationals.js。
2026-11-09 22:30:29 UTC，root 在可用的 functions.exec JavaScript 隔离运行时
实际执行同一完整源字符串，25个精确有理门全部通过。
这不是失联终端中的 Node/Python 重跑，也不是数值几何运行；
来源字符串将作为<100KB纯文本保存，程序只输出计数和范围。
可在恢复后用 Node 直接运行该文件。

脚本只核常数，不证明最短测地线存在、全局弦论证或边界最近点推导；
这些部分由本文完整证明及其未参与者全文独审支付。
旧大数据、主solver或存储C都不曾被本稿调用。

时间区间仍只有正存在性，未给有效振幅。固定材料片和全 $\mathrm E(3)$
非全等由基稿保留，缩小正区间不会消灭其非平凡性。
最终还缺实际闭合的同度量连接，以及满足可见幅度的有效构造；
本稿不改变README完成标准或QUEUE状态。
