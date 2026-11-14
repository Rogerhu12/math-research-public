# R32：单素数分母在秩一 Mordell 曲线上的统一指数窗口

日期：2026-11-12；会话：serre-uniformity-astra-cont/2026-11-12。

**状态：已证明的有明确范围的全局结果。** 对 R19 的右端 $q^p$ 和 $8q^p$，固定 $p\bmod6$ 后得到一条不再依赖 $p$ 的 Mordell 曲线。若该曲线秩一，Ingram–Silverman 已发表的统一原始除子**例外个数**定理给出一个统一长度的指数窗口。窗口的位置仍可能随 Mordell–Weil 生成元在 $q$ 处的分母深度变化；本文没有把个数界换成最大指标界，也没有假定相关曲线都秩一。

## 1. 统一常数和陈述

使用下述已发表输入：存在整数 $M\ge1$，使对每条 $j$ 不变量为整数的 $D/\mathbb Q$、每个无限阶点 $R\in D(\mathbb Q)$，在全局极小整 Weierstrass 模型上写
$$
x([n]R)=A_n/B_n^2,\qquad
B_n>0,\qquad \gcd(A_n,B_n)=1,
$$
则集合
$$
\mathcal Z(D,R)=
\{n\ge1:B_n\text{ 没有原始素因子}\}
$$
满足
$$|\mathcal Z(D,R)|\le M. \tag{32.1}$$
这里原始素因子指整除 $B_n$、却不整除任何 $B_m$（$1\le m<n$）的素数。

这是 Ingram–Silverman, *Uniform estimates for primitive divisors in elliptic divisibility sequences* (2012) 的统一个数定理。等价的所需形式已在 Ingram (2009), Theorem 3 中列出：界 $M_1(K,\nu(D/K))$ 只依赖数域和分裂乘性约化素数的数目。本文固定 $K=\mathbb Q$，且 $j(D)=0$，故 $\nu(D/\mathbb Q)=0$，可取一个绝对常数 $M=M_1(\mathbb Q,0)$。来源及可核查的准确范围见第 7 节。本文不为 $M$ 声称未经核实的数值。

固定素数 $q>7$，取
$$
c\in\{1,8\},\qquad r\in\{1,5\},
$$
定义
$$
D=D_{q,r,c}:\quad V^2=U^3-27c q^r.
\tag{32.2}
$$

**定理 R32。** 若 $\operatorname{rank}D(\mathbb Q)=1$，则 $D(\mathbb Q)$ 无挠点，故可以写成 $\mathbb ZR$，其中 $R$ 只差一个符号。定义
$$
a=a_q(R)=\max\{0,-\tfrac12v_q(U(R))\}\in\mathbb Z_{\ge0}.
\tag{32.3}
$$
对每个 $k\ge1$，若有整数 $X,W$ 满足
$$
X^3-27W^2=cq^{\,6k+r},\qquad q\nmid XW,
\tag{32.4}
$$
则
$$
\boxed{\quad k=a+v_q(n),\qquad \tau(n)\le M+1,\qquad
a\le k\le a+M\quad}
\tag{32.5}
$$
对某个正整数 $n$ 成立，其中 $\tau(n)$ 是正因子个数。

因而对同一个 $q,r,c$，可能出现的指数 $6k+r$ 都在区间
$$
[\,6a+r,\;6a+6M+r\,]
\tag{32.6}
$$
内。若生成元在 $q$ 处整，即 $a=0$，则所有这些指数满足绝对界
$$6k+r\le6M+r. \tag{32.7}$$
此外，满足 (32.4) 的不同解对 $(X,\{W,-W\})$，连同变化的 $k$，总数至多为 $M+1$。

在 R19 的应用中，把素数指数写成 $p=6k+r$。族 I、III 取 $c=1$，族 II 取 $c=8$。R19 的额外模 $2$、模 $3$ 条件只会进一步删去解，故不影响此必要条件。

**秩零分支。** 若 $\operatorname{rank}D(\mathbb Q)=0$，则 (32.4) 对所有 $k\ge1$ 均无解。

**不限制秩的推论。** 对 (32.4) 给出的点 $P$，若 $P=[q^s]R_0$、$R_0\in D(\mathbb Q)$，则必有 $s\le M$。取一个在有理 Mordell–Weil 群中不能再被任何整数 $>1$ 整除的点 $R_0$，写 $P=[n]R_0$，则仍有 $\tau(n)\le M+1$ 及
$$a_q(R_0)=k-v_q(n)\ge k-M. \tag{32.7a}$$
因此大的 Fermat 指数必须留下一个本身已有深分母的不可整除有理点；并不能全由一个浅分母点的高次倍数产生。此推论的证明见第 5.1 节。

## 2. 固定 Mordell 曲线和精确分母

由 (32.4) 置
$$
U=\frac{3X}{q^{2k}},\qquad
V=\frac{27W}{q^{3k}}.
\tag{32.8}
$$
直接计算得
$$V^2=U^3-27cq^r.$$
因为 $q\nmid3XW$，这给出
$$
v_q(U)=-2k,\qquad v_q(V)=-3k,
$$
且 $U,V$ 在所有其他有限素数处整。因此在 (32.2) 的模型上，该点的正规化 $U$ 分母恰为 $q^{2k}$，并非仅仅“分母支持于 $q$”。

显示模型确为全局极小整模型。其判别式为
$$
\Delta_D=-2^4\,3^9c^2q^{2r}.
\tag{32.9}
$$
在 $2$ 处的赋值是 $4$ 或 $10$，在 $3$ 处为 $9$，在 $q$ 处为 $2$ 或 $10$，在其他素数处为零；所有赋值都小于 $12$。若一个整 Weierstrass 模型不是极小的，改为极小模型的判别式赋值至少下降 $12$。这里将产生负赋值，故不可能。

所以 (32.1) 所要求的“极小模型分母”就是 (32.8) 使用的分母，无模型缩放误差。$D$ 的 $j$ 不变量为零，满足统一定理的整 $j$ 假设。

反向使用 (32.8) 时，不能把任意 $\{q\}$-整点都当作 R19 的解：还须验证 $3\mid q^{2k}U$、$27\mid q^{3k}V$ 及 R19 的奇偶条件。本文主要使用必要方向，因此不遗漏这一限制。

## 3. q 处的整个局部群：没有隐藏的初始深度例外

以下写
$$b=-27cq^r,\qquad D:V^2=U^3+b.$$
这里 $v_q(b)=r\in\{1,5\}$。

### 3.1 每个局部点都具有非奇异约化

首先证明
$$D(\mathbb Q_q)=D_0(\mathbb Q_q). \tag{32.10}$$
若一个整仿射点约化到尖点 $(0,0)$，则 $v_q(U),v_q(V)>0$。当 $r=1$ 时，$v_q(U^3+b)=1$，不可能等于平方的赋值。

当 $r=5$ 时，若 $v_q(U)=1$，则右端赋值为 $3$；若 $v_q(U)\ge2$，则右端赋值为 $5$。两者仍为奇数。不存在 $3v_q(U)=5$ 的抵消情形。因此也没有约化到尖点的有理点。

非整仿射点满足通常的赋值关系 $v_q(U)=-2m$、$v_q(V)=-3m$，$m\ge1$，在射影模型上约化到无穷点。故全部局部点都属于 $D_0$，证明 (32.10)。这也直接避开了未检查的分支群假设。

### 3.2 整圆盘参数和一个显式对数

令
$$t=-U/V,\qquad w=-1/V.$$
Weierstrass 方程变为
$$w=t^3+bw^3. \tag{32.11}$$
对每个 $t\in\mathbb Z_q$，右式视为关于 $w$ 的方程，其导数 $1-3bw^2$ 为单位，故有唯一解 $w\in\mathbb Z_q$，满足 $w\equiv t^3\pmod q$。$t=0$ 对应无穷点；$t$ 为单位对应非奇异仿射约化；$v_q(t)=m\ge1$ 对应形式群深度 $m$。由此 $t$ 是整个 $D_0(\mathbb Q_q)$ 的整圆盘参数。

形式群的通用系数具有权重齐次性。此处只有权重 $6$ 的系数 $b$ 非零，所以群律中总次数 $6m+1$ 的项含因子 $b^m$。于是群律级数在 $\mathbb Z_q^2$ 上收敛，并与椭圆曲线加法一致；这把通常只在 $q\mathbb Z_q$ 上使用的形式群延拓到整个整圆盘。

对不变微分直接求导得
$$
\omega=\frac{dU}{2V}=\frac{dt}{1-3bw^2}.
\tag{32.12}
$$
写 $w=t^3F(bt^6)$，则 $F(s)=1+sF(s)^3$。Lagrange 反演给出
$$
F(s)=\sum_{m\ge0}\frac1{2m+1}\binom{3m}{m}s^m.
$$
又
$$
\frac1{1-3sF(s)^2}=F(s)+2sF'(s)
=\sum_{m\ge0}\binom{3m}{m}s^m.
$$
因此形式对数是明确的级数
$$
\mathcal L(t)=
\sum_{m\ge0}
\frac{\binom{3m}{m}}{6m+1}\,b^m t^{6m+1}.
\tag{32.13}
$$

当 $m\ge1$，由于 $q>7$，有 $q^m>6m+1$，故
$$
v_q(6m+1)\le m-1.
$$
从而 (32.13) 的每个非线性系数都被 $q$ 整除，且系数的赋值趋于无穷。因此
$$\mathcal L(t)=t+qH(t)$$
对某个整系数、系数趋零的收敛级数 $H$ 成立。$H$ 在 $\mathbb Z_q$ 上为 $1$-Lipschitz，故
$$
v_q(\mathcal L(t)-\mathcal L(s))=v_q(t-s).
\tag{32.14}
$$
用收缩映射 $t\mapsto z-qH(t)$ 可对每个 $z\in\mathbb Z_q$ 求出唯一逆像。形式恒等式 $\mathcal L(\mathcal F(t,s))=\mathcal L(t)+\mathcal L(s)$（$\mathcal F$ 表示群律）适用于上述收敛级数，因此得到保持滤过的群同构
$$
\mathcal L:D(\mathbb Q_q)\overset{\sim}{\longrightarrow}\mathbb Z_q,
\qquad
D_m(\mathbb Q_q)\longleftrightarrow q^m\mathbb Z_q
\quad(m\ge1).
\tag{32.15}
$$

这证明两个关键事实：

1. $D(\mathbb Q_q)$ 无挠点，故 $D(\mathbb Q)$ 无挠点。
2. 若 $R$ 在 $q$ 处整，则 $\mathcal L(R)$ 为单位，$[q]R$ 的深度**恰好**为 $1$；若 $R$ 已在深度 $a\ge1$ 的形式群中，则任意非零整数 $n$ 满足
   $$
   v_q(t([n]R))=a+v_q(n).
   $$

统一写法正是
$$
v_q(t([n]R))=a_q(R)+v_q(n).
\tag{32.16}
$$
这里明确使用 $q>7$；未把小剩余特征可能出现的加性 $q$ 挠点例外带入论证。

## 4. 原始除子的个数界怎样约束乘法指标

现在假定 $\operatorname{rank}D(\mathbb Q)=1$，选生成元 $R$。第 3 节已证明没有有理挠点，所以 (32.8) 中的点是 $\pm[n]R$，其中 $n\ge1$。

令 $(B_m)$ 是 $R$ 的正规化分母 EDS。由第 2 节，
$$B_n=q^k. \tag{32.17}$$
EDS 的整除性质给出
$$d\mid n\quad\Longrightarrow\quad B_d\mid B_n.$$
例如逐素数看，这是形式群对整数乘法稳定、分母赋值在乘法下不下降的直接结果。故对每个 $d\mid n$，$B_d$ 只可能含素数 $q$。

设
$$n_0=\min\{m\ge1:q\mid B_m\}.$$
由 (32.15)，$n_0=1$ 当 $a>0$，而 $n_0=q$ 当 $a=0$。因为 $q\mid B_n$，必有 $n_0\mid n$。

除 $d=n_0$ 外，每个正因子 $d\mid n$ 都属于 $\mathcal Z(D,R)$：

- 若 $B_d=1$，它没有任何素因子；
- 若 $q\mid B_d$，则 $n_0<d$，$q$ 已在更早的项中出现；又没有其他素因子。

因此
$$\tau(n)-1\le|\mathcal Z(D,R)|\le M.$$
尤其 $\tau(n)\ge v_q(n)+1$，所以
$$v_q(n)\le M. \tag{32.18}$$
结合 (32.8) 的 $t$ 深度 $k$ 和 (32.16)，立即得到 (32.5)–(32.7)。

注意这个论证只用**例外指标的个数**。它没有断言这些指标都不超过 $M$。例如一个很大的素数指标仍可以是唯一例外；通过考察它的全部因子，本文只控制了乘法指标的 $q$ 进赋值和因子个数。

最后，每个产生解的 $n$，除了可能的 $n_0$ 外，都在 $\mathcal Z(D,R)$ 中，故正指标至多 $M+1$ 个。对固定 $q,r,c,n$，点 $[n]R$ 确定 $k$ 及 $(X,\{W,-W\})$。这证明定理的解数断言。

## 5. 秩零以及固定分母的有限性

若 $\operatorname{rank}D(\mathbb Q)=0$，第 3 节的无挠点结论给 $D(\mathbb Q)=\{O\}$，所以不可能出现 (32.8) 的仿射点，证明秩零分支。

不作秩假设时，对固定 $q,r,c$，Siegel 的 $S$-整点定理仍保证 $D(\mathbb Z[1/q])$ 有限。因此固定 $q$ 的全部指数只有有限多个。这个结论的常数及点集依赖 $q$；它本身不能证明绝对指数上界。

第 1 节秩一结果比这个定性结论更精确：窗口的**长度**由绝对常数控制，但窗口起点是一个明确的全局量 $6a_q(R)+r$。

### 5.1 任意秩：全局 q 整除深度至多 M

第 4 节的因子计数实际不要求 $R$ 生成整个 Mordell–Weil 群；它只要求 $P=[n]R$ 且 $R$ 无限阶。因第 3 节排除了挠点，任何非零有理 $R$ 均满足这一要求。

若 $P=[q^s]R_0$，对 $R_0$ 的 EDS 使用同一论证，得到
$$s+1=\tau(q^s)\le M+1,$$
即 $s\le M$。这里没有将局部 $q$ 整除误当作有理群中的整除。

更一般，由 Mordell–Weil 有限生成及无挠性，可把任意非零 $P$ 写成 $P=[n]R_0$，使 $R_0$ 在该自由阿贝尔群中为本原向量。第 4 节给 $\tau(n)\le M+1$、$v_q(n)\le M$；(32.16) 则给 (32.7a)。整除性还保证 $R_0$ 的分母只含 $q$。

若 $k>M$，则 $P$ 在局部群 $D(\mathbb Q_q)\simeq\mathbb Z_q$ 中可被 $q^{M+1}$ 整除，却不能在 $D(\mathbb Q)$ 中被 $q^{M+1}$ 整除。这只是一个位置的局部与整体差别；没有声称 $P$ 在所有完成域都可被这一整数整除，也没有违反任何局部整体整除定理。

## 6. 留下的真实全局问题

本结果没有排除所有 $p\equiv3\pmod4$。仍有以下互不混同的缺口：

1. 相关 Mordell 曲线的秩可能大于一。此时不同的点不必属于一个固定生成元的倍数序列；第 5.1 节只控制每个点的有理整除深度。若点本身已是本原向量，其乘法指标只是 $1$，原始除子定理不限制它本身的 $q$ 分母深度。
2. 即使秩一，生成元也可能已有 $q$ 分母，而且 $a_q(R)$ 尚无本文所需的绝对上界。对任何产生 (32.4) 的曲线，整除性还强迫 $R$ 的分母只含 $q$，但这没有排除很大的初始深度。
3. $M$ 的存在和“$q$ 处整生成元”子情形的统一排除都是无条件定理；但本文没有给全部 $q$ 一个秩一或整生成元定理。不能把这个可核查子情形变成对所有分母素数的结论。
4. R23 已说明全部局部同余条件可以同时满足；上述 $a_q(R)$ 是有理 Mordell–Weil 群嵌入局部群后的量，属于真正的全局约束，不由局部圆盘自身的结构决定。

尤其，局部群 (32.15) 包含任意深度的点；而任意非零有理点的 $q^m$ 倍也会进入任意深的局部邻域。原始除子定理解释了这条倍数序列为什么最终引入新的分母素数，但没有证明每个有理点都必须从一个浅分母的有理点出发。

## 7. 文献和核查范围

- P. Ingram, J. H. Silverman, *Uniform estimates for primitive divisors in elliptic divisibility sequences*, in *Number Theory, Analysis and Geometry* (2012), 243–271，[出版社原始页面](https://link.springer.com/chapter/10.1007/978-1-4614-1260-1_12)，DOI 10.1007/978-1-4614-1260-1_12。其摘要明确区分“整 $j$ 情形统一控制 Zsigmondy 集合的大小”和另行研究最大指标；本文只使用前者。
- P. Ingram, *A quantitative primitive divisor result for points on elliptic curves*, J. Théor. Nombres Bordeaux **21** (2009), 609–634，[期刊原文](https://www.numdam.org/item/10.5802/jtnb.691.pdf)，Theorem 3（文内 p. 610）明确陈述 $M_1(K,\nu)$ 和 $M_2(K,\sigma)$ 的依赖。本篇取 $K=\mathbb Q,\nu=0$。同文 §2 给正规化 EDS 定义。该论文专门研究的尖锐显式界针对 congruent-number 曲线，本文没有把那些显式数字移用于 $j=0$ 曲线。
- 局部群的第 3 节已给独立推导。可交叉核对 M. Kosters, R. Pannekoek, *On the structure of elliptic curves over finite extensions of $\mathbb Q_p$ with additive reduction*, [arXiv:1703.07888v1](https://arxiv.org/html/1703.07888v1)，Theorem 1、Corollary 2 和 Proposition 12：加性模型的形式群可延拓到整圆盘，未分歧基域的例外只在 $2,3,5,7$。本篇没有依赖该预印本例外表来省略计算。
- M. Streng, *Divisibility sequences for elliptic curves with complex multiplication*, Algebra & Number Theory **2** (2008), 183–208，[期刊原文](https://msp.org/ant/2008/2-2/ant-v2-n2-p04-p.pdf)，Introduction 的主定理是在固定曲线与固定无限阶点上建立 CM 指标的原始除子存在性。它不是任意变化 Mordell–Weil 生成元深度的绝对界，故没有填补第 6 节的缺口。

本文件不把上述已有定理本身作为新结果；新增的是对 R19 单素数分母三族的精确正规化、局部深度计算及统一指数窗口推论。
