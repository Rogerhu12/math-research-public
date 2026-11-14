# R4：一个显式单共振背景、全整数频率谱隙与闭面无穷小弯曲

2026-11-10，visible-exact-astra-76e8。

**状态：已证明；主课题的中间结论。** 本文另选径向度量，不冒用 flat17
的几何或误差证书。得到的是闭旋转背景、一个真正的全局无穷小弯曲，以及
背景标量 Sturm 算子的完整频率逆估计。没有得到非线性等距弯曲族，没有
固定开帽，也没有把无穷小振幅升级为 $5\%$。

## 1. 明确陈述

令
$$
\mu=\sqrt2,\qquad A=2+\frac{\sqrt2}{3},\qquad
V(x)=A\operatorname{sech}^2x-2,\qquad x\in\mathbb R.
\tag{1.1}
$$
对每个整数 $n\ge1$，在 $L^2(\mathbb R)$ 上取自伴算子
$$
L_n=-\frac{d^2}{dx^2}-n^2V(x),\qquad D(L_n)=H^2(\mathbb R).
\tag{1.2}
$$
则：

1. $\ker L_n=0$，除非 $n=3$；$\ker L_3$ 恰为
   $$\operatorname{span}\{y_3\},\qquad y_3(x)=\operatorname{sech}^{3\sqrt2}x.$$
2. 对 $n\ne3$ 的所有谱点，以及 $n=3$ 的所有非零谱点，
   $$|\lambda|>\frac1{1000n^2}.$$
   因而去掉上述唯一核后，真实全频逆满足
   $$\|L_n^{-1}f\|_2\le1000n^2\|f\|_2.$$
   这是全部整数频率的证明，不是有限频率扫描。
3. 唯一解
   $$h''+Vh=0,\qquad h(0)=1,\quad h'(0)=0$$
   处处严格为正。由
   $$a=\frac1h,\qquad z(x)=\int_0^x\frac{du}{h(u)^2},\qquad
   X(x,\theta)=(a(x)\cos\theta,a(x)\sin\theta,z(x))$$
   定义的旋转曲面在两端各补一个点后，是连通闭 $C^2$ 嵌入球面。
4. 该闭面上存在下面第 6 节给出的明确非刚体 $C^2$ 无穷小等距弯曲，
   并在两个极点连同全部二 jet 为零。**两个点不构成本题所需有内点的 $H$。**

## 2. 从因式分解付清完整谱

对实数 $\ell>0$，写
$$H_\ell=-\partial_x^2-\ell(\ell+1)\operatorname{sech}^2x,$$
$$B_\ell=\partial_x+\ell\tanh x.$$
直接展开得
$$
B_\ell^*B_\ell=H_\ell+\ell^2,\qquad
B_\ell B_\ell^*=H_{\ell-1}+\ell^2.
\tag{2.1}
$$
因此 $\operatorname{sech}^{\ell}x$ 是 $H_\ell$ 的特征值 $-\ell^2$
对应的 $L^2$ 特征函数，且为 $B_\ell$ 的全部核。对其余负特征值，
$B_\ell$ 与 $B_\ell^*$ 给出和 $H_{\ell-1}$ 的一一对应，保持特征值。
相应特征函数指数衰减，故这些操作在算子域内合法。

当 $0<\ell\le1$ 时，
$$H_{\ell-1}=-\partial_x^2+\ell(1-\ell)\operatorname{sech}^2x\ge0.$$
递降到此情形，得全部负离散谱恰为
$$-(\ell-j)^2,\qquad j=0,1,\ldots,\quad j<\ell.
\tag{2.2}
$$
递升 $B^*$ 给出所有这些特征函数；递降又排除了额外负特征值。
势函数有界且趋零，乘法势相对自由算子的 resolvent 为紧算子：在有限区间
用 $H^2\hookrightarrow L^2$ 的紧嵌入，在区间外用势的上确界趋零近似。
故本质谱为 $[0,\infty)$。这也说明负谱没有遗漏连续部分。

令
$$\ell_n=\frac{\sqrt{1+4An^2}-1}{2},\qquad \ell_n(\ell_n+1)=An^2.$$
于是 $L_n=H_{\ell_n}+2n^2$ 的本质谱为 $[2n^2,\infty)$，其下全部谱为
$$E_{n,j}=2n^2-(\ell_n-j)^2,\qquad 0\le j<\ell_n,\quad j\in\mathbb Z.
\tag{2.3}
$$
这里的非整数 $\ell_n$ 也已由 (2.1) 的递降论证覆盖，不依赖只对整数深度
成立的无反射公式。

## 3. 唯一共振及统一算术下界

若 $E_{n,j}=0$，则 $\ell_n=n\sqrt2+j$。将其代入定义得到
$$
\bigl(n^2-3n(2j+1)\bigr)\sqrt2=3j(j+1).
\tag{3.1}
$$
两侧的有理性强迫整数系数各为零。由 $j\ge0$ 得 $j=0$，继而 $n=3$。
反过来，$\ell_3=3\sqrt2$，确实给这个零特征值及 $y_3$。

下面付统一距离，而不仅排除精确相等。记
$$p=n^2-3n(2j+1),\qquad q=3j(j+1).$$
除 $(n,j)=(3,0)$ 外，$2p^2-q^2$ 是非零整数，故
$$
|p\sqrt2-q|\ge\frac1{\sqrt2|p|+|q|}.
\tag{3.2}
$$
由 $A<5/2$、$\ell_n<2n$ 和 $j<\ell_n$，保守地有
$$|p|\le16n^2,\qquad |q|\le18n^2,\qquad
\sqrt2|p|+|q|<42n^2.$$
又
$$
(\ell_n-n\sqrt2-j)(\ell_n+n\sqrt2+j+1)
=\frac{p\sqrt2-q}{3},
\tag{3.3}
$$
且第二因子小于 $7n$。所以
$$|\ell_n-n\sqrt2-j|>\frac1{882n^3}.$$
因 $\ell_n-j>0$，
$$
|E_{n,j}|=(n\sqrt2+\ell_n-j)|n\sqrt2-\ell_n+j|
>\frac1{882n^2}>\frac1{1000n^2}.
\tag{3.4}
$$
本质谱下端 $2n^2$ 也满足此界。自伴谱定理即给第 1 节的逆估计。
对 $n=3$ 在 $y_3^\perp$ 上取逆；其实际非零谱下端还大于
$6\sqrt2-1>7$，但不需使用这个改进。

### 3.1 三阶核的明确低模横截性

暂时只改变势的深度 $A$，保持常数项 $-2$。三阶块的最低特征值是
$$E_{3,0}(A)=18-\ell_3(A)^2,\qquad
\ell_3(A)(\ell_3(A)+1)=9A.$$
因此在本背景处
$$
\frac{dE_{3,0}}{dA}
=-\frac{18\ell_3}{2\ell_3+1}
=-\frac{54\sqrt2}{6\sqrt2+1}\in(-9,-8).
\tag{3.5}
$$
同样的界在 $12/5\le A\le5/2$ 上成立，因为该区间内 $\ell_3>4$。
这是一项已付常数的低模调参方向。**改变 $A$ 后不能将 (3.4) 自动转授给
全部高模。** 即使深度变化极小，高频相位变化仍随频率增长；若为了接尾
恢复三阶核而动了核心，必须在新参数上重新证明全频谱隙。

## 4. 无固定角带损失的标量逆

设 $y=L_n^{-1}f$，在 $n=3$ 时已投影去核。因为 $|V|\le2$，方程和 (3.4) 给
$$
\|y\|_2\le1000n^2\|f\|_2,
\qquad \|y''\|_2\le2001n^4\|f\|_2.
\tag{4.1}
$$
分部积分及 Cauchy--Schwarz 给
$$\|y'\|_2^2\le\|y\|_2\|y''\|_2,
\qquad \|y'\|_2\le1500n^3\|f\|_2.
\tag{4.2}
$$
因此 Fourier 系数按任何角 Sobolev 权或指数权求和，都只增加明确的有限次
多项式频率权，没有固定的 $e^{c|n|}$ 角带损失。角均值 $n=0$ 不在此逆的
定义内；本题 R3 的自由平均也不能被误说成已自动处理了全部非线性均值。

这些估计针对**径向背景**的标量 $L_n$。不能据此假定大幅非径向线性化有
相同的块对角分解或相同的逆。

## 5. 从势构造真正的闭旋转背景

线性 ODE 的系数全局有界光滑，故 $h$ 全局存在且为偶函数。
设它在 $R>0$ 第一次为零。在 $[-R,R]$ 上，$h\in H^1_0$ 且 $L_1h=0$。
但由 (2.1)
$$L_1=B_{\ell_1}^*B_{\ell_1}+(2-\ell_1^2).$$
又 $\ell_1<6/5$，因为 $A<5/2<(6/5)(11/5)$，所以
$$2-\ell_1^2>14/25>0.$$
积分得 $0\ge(14/25)\int h^2$，矛盾。因此 $h>0$。

当 $x\ge2$ 时，$h''=(2-A\operatorname{sech}^2x)h\ge h$。
如果 $h'$ 始终不变正，则 $h'$ 单调增加到零，$h$ 单调下降到零。
将 $h''\ge h$ 乘负数 $h'$ 并从当前点积分到无穷远，得
$-h'\ge h$，从而 $h$ 指数衰减。由方程，$h'$、$h''$ 也指数衰减。
偶延拓便给 $L_1$ 的非零 $L^2$ 零向量，与严格正性矛盾。
故 $h'>0$ 最终成立。

令 $v=h'/h$。在这个尾区它为正，满足
$$v'=2-A\operatorname{sech}^2x-v^2.$$
用 $w'=2\pm\varepsilon-w^2$ 的标量比较先得 $v$ 有界，再令
$\varepsilon\downarrow0$，得到
$$\frac{h'}h\longrightarrow\sqrt2,\qquad
\frac{h''}h\longrightarrow2\qquad(x\to+\infty).
\tag{5.1}
$$
特别地，$h$ 最终指数增长。由偶性，另一端相同。

定义经线弧长 $s$：
$$\frac{ds}{dx}=\frac{\sqrt{1+h'^2}}{h^2},\qquad
\frac{dz}{dx}=\frac1{h^2},\qquad a=\frac1h.$$
两积分均在两端收敛，并且
$$a_s=-\frac{h'}{\sqrt{1+h'^2}},\qquad
z_s=\frac1{\sqrt{1+h'^2}},\qquad a_s^2+z_s^2=1.
\tag{5.2}
$$
故内部诱导度量准确为 $ds^2+a(s)^2d\theta^2$。$z$ 严格增加，$a>0$，
所以旋转参数化在内部无自交。

在上极点附近 $h'>0$，把 $z$ 视为 $a$ 的函数。有
$$z_a=-\frac1{h'},\qquad
\frac{z_a}{a}=-\frac h{h'}\to-\frac1{\sqrt2},\qquad
z_{aa}=-\frac{h''h^2}{h'^3}\to-\frac1{\sqrt2}.
\tag{5.3}
$$
因此旋转图的 Cartesian Hessian 在轴上连续趋于
$-I/\sqrt2$；补极点后为真正的 $C^2$ 正则图。下极点同理。
两极高度不同，内部各高度只有一个圆，所以完整面为嵌入球面。

最后直接核对本题所用 Sturm 势，而不是只作形式命名。由 (5.2)
$$a_{ss}=-\frac{h^2h''}{(1+h'^2)^2},\qquad z_s=(1+h'^2)^{-1/2},$$
于是
$$\frac{a^3a_{ss}}{z_s^4}=-\frac{h''}{h}=V.
\tag{5.4}
$$
这与 visible 课题 R77/R79 的径向 Sturm 变量相同。背景在中央有负 Gauss
曲率，在两极趋向 Gauss 曲率 $1/2$；同一背景的定量 reach 比例现由本题 R5 另行完整证明。

## 6. 真正的全局 $C^2$ 无穷小弯曲

这一步把标量核转成实际向量场，避免只给一个形式源解。
一般先令 $y''+n^2Vy=0$，并置
$$U=\frac yh=ay,\qquad T=-\frac Un,\qquad
W=\frac{h'}h y-\frac{y'}{n^2}.$$
在圆柱标架 $e_r=(\cos\theta,\sin\theta,0)$、
$e_\theta=(-\sin\theta,\cos\theta,0)$ 中定义
$$
Z=U\cos(n\theta)e_r+T\sin(n\theta)e_\theta
  +W\cos(n\theta)e_z.
\tag{6.1}
$$
线性化的三个等距方程精确为
$$
U+nT=0,
$$
$$
aT_s=a_s(nU+T)+nz_sW,
$$
$$
a_sU_s+z_sW_s=0.
\tag{6.2}
$$
前两式由定义直接成立。第二式也可写成
$$W=\frac{(n^2-1)h'U-hU'}{n^2},$$
这里以及本节其余带撇号均对 $x$ 求导。第三式等价于 $W'=h'U'$。
将上式求导后，所需关系恰为
$$hU''+2h'U'-(n^2-1)h''U=0,$$
其左端准确等于 $(hU)''-n^2h''U$。由于 $y=hU$，这等价于
$$y''-n^2(h''/h)y=y''+n^2Vy=0.$$
更直接地，把 $y=hU$ 代入即可逐项核实。因而
$$\langle dX,dZ\rangle+\langle dZ,dX\rangle=0$$
在整个内部严格成立。

现在取 $n=3$、$y=y_3$。两极附近 $y$ 及其任意有限次 $x$ 导数都是
$O(e^{-3\sqrt2|x|})$。由 (5.1)，$h$ 的增长指数可夹在
$\sqrt2\pm\varepsilon$，而 $h'/h$ 及其前两阶导数有界。
在极点的真实平面坐标 $(a\cos\theta,a\sin\theta)$ 中，径向一次求导
至多带来 $O(h)$，二次求导至多带来 $O(h^2)$。因此 $Z$ 的全部二阶
Cartesian 导数趋零，因为
$$h^2e^{-3\sqrt2|x|}\longrightarrow0.$$
角向除以 $a$ 的项也满足同一界。将 $Z$ 在两极取零即得全局 $C^2$
向量场，两个极点上的零二 jet 也随之成立；(6.2) 由连续性覆盖极点。

在 $x=0$ 的腰圈上，$a=1,h'=0,y=1,y'=0$，参考法向为 $e_r$，
故 $Z\cdot n=\cos3\theta$。任一环境无穷小刚体场
$b+\omega\times X$ 在该圆上的法向分量只有一阶 Fourier 模。
所以 $Z$ 非刚体。

## 7. 对主问题的使用范围与仍欠内容

此背景把“需要假定一个未付常数的全频非共振条件”替换成了 (3.4) 的
明确算术证明；三阶模、完整逆及闭旋转几何来自同一个对象。
但线性族 $X+\varepsilon Z$ 的二阶度量误差一般为
$\varepsilon^2(dZ)^TdZ$，不能称精确等距族。

下一步至少需要：在非径向邻域建立真实全频逆和非线性收敛；把非线性振幅
做到本题比例；如使用相位作用，付两个真正固定开帽的退化尾及完整二 jet。
仅有两极的零二 jet 不产生开握持区。若改造两端尾，也必须重新证明新的
物理 Robin 条件与本算术谱隙的兼容，不能直接复制 (3.4)。

随附 `scripts/poschl_teller_seed.py` 只作浮点探索和复现候选参数；它的采样
曲率、支撑或有限频谱不参与上述证明，也不充当严格几何证书。
