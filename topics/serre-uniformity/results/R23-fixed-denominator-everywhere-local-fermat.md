# R23：固定单素数分母的 Fermat 方程连同辛同余条件处处局部可解

日期：2026-11-12；会话：serre-uniformity-astra-cont/2026-11-12。

**状态：已证明。** 本文构造的是一个固定方程的处处局部解，不是一组三个有理数或整数的全局解。每个局部解都带有与固定 CM 曲线的实际辛 $p$-挠点同构，并满足族 I 的原始性及约化条件。对所有 $p>37$ 都能如此构造，故仅依靠这些局部条件无法排除任何剩余的素数同余类。

## 1. 陈述

固定
$$
A:y^2=x^3-x,\qquad p>37\ \text{为素数},
$$
并置
$$
d=p(p^2-1),\qquad
g=1+\frac{(p^2-1)(2p-1)}4,\qquad
B=(d+3)^2.
\tag{23.1}
$$
“辛同构”在本文中指严格保持 Weil 配对的同构；这当然也满足通常只要求配对乘子为平方的定义。

**定理 R23。** 存在无穷多个素数 $q>B$，满足
$$
q\equiv1\pmod{4p},\qquad q\ge4p^2+1,
$$
且 $q$ 在 $\mathbb Q(A[p])$ 中完全分裂，对每个这样的构造素数 $q$，固定方程
$$
C_{q,p}:\quad X^3-27W^2=q^p
\tag{23.2}
$$
具有以下性质。对 $\mathbb Q$ 的每个位置 $v$，都有一组局部解 $(X_v,W_v)$，使
$$
F_v:y^2=x^3-X_vx-2W_v
$$
满足辛同构
$$
\phi_v:A[p]\overset{\sim}{\longrightarrow}F_v[p]
\quad\text{作为 }G_{\mathbb Q_v}\text{-模}.
\tag{23.3}
$$
对每个有限素数 $\ell$，可令 $X_\ell,W_\ell\in\mathbb Z_\ell$，且：

1. 若 $\ell\ne q$，则 $X_\ell,W_\ell$ 不同时被 $\ell$ 整除；若 $\ell=q$，二者都是单位。因此 $(X_\ell,W_\ell,Z=q)$ 满足全部局部原始性条件。
2. 在 $2$ 处可令 $X_2\equiv1\pmod4$、$4\mid W_2$，且 $F_2$ 与 $A$ 在 $\mathbb Q_2$ 上同构；显示模型极小，导子指数为 $5$。
3. 在 $3$ 和 $p$ 处也可令 $F_v\simeq A$。特别地，$3\nmid X_3$；若 $p\equiv3\pmod4$，则 $F_p$ 好超奇异。
4. 在 $q$ 处 $F_q$ 分裂乘性约化，显示模型极小，$v_q(\Delta)=p$，且其 Tate 参数属于 $\mathbb Q_q^{\times p}$。
5. 在其余奇素数处 $F_\ell$ 好约化。

因此局部导子和极小判别式数据同时吻合
$$
N=32q,\qquad \Delta=64q^p.
\tag{23.4}
$$
这里 (23.4) 只是这一族局部模型的共同数值数据，并未断言存在把它们粘合起来的有理椭圆曲线。

**进一步的无条件推论。** 当 $p\equiv1\pmod4$ 时，参数化 (23.2)、(23.3) 的辛层覆盖的光滑射影完备化处处局部有点，却没有有理点，是亏格为 $g$ 的射影 Hasse 原理反例。对所有 $p>37$，该完备化的边界都没有有理点；但当 $p\equiv3\pmod4$ 时，本文不声称其仿射部分没有有理点。

## 2. 辛层覆盖及其几何连通性

先证明一个在有限域和特征零中都适用的几何计算。设 $k$ 为代数闭域，其特征为零，或为大于 $B$ 的素数。取 $c\in k^\times$，令
$$
C_c:\quad X^3-27W^2=c.
$$
它的光滑射影完备化 $\overline C_c$ 是亏格 $1$ 曲线，只有一个无穷点 $O$，并有
$$v_O(X)=-2,\qquad v_O(W)=-3.$$
考虑 $C_c$ 上的椭圆曲线族
$$
\mathcal F:y^2=x^3-Xx-2W.
$$
其不变量为
$$
c_4=48X,\quad c_6=1728W,\quad
\Delta=64c,\quad j=\frac{1728X^3}{c}.
\tag{23.5}
$$
所以 $\mathcal F$ 在全部仿射基曲线 $C_c$ 上光滑。$j:\overline C_c\to\mathbb P^1$ 的唯一极点在 $O$，阶为 $6$，故其次数恰为 $6$。

选定常值二维辛 $\mathbb F_p$-空间 $V$。辛同构
$$V\overset\sim\longrightarrow\mathcal F[p]$$
构成 $C_c$ 上次数为 $d=|\operatorname{SL}_2(\mathbb F_p)|$ 的有限 étale 覆盖。其几何单值群 $G$ 包含于 $\operatorname{SL}_2(\mathbb F_p)$。下面证明 $G$ 恰为整个群，从而此覆盖连通。

### 2.1 无穷点的惯性

在 $O$ 取局部参数 $t$。把椭圆曲线坐标替换为 $x=t^{-2}x',y=t^{-3}y'$，得到整模型，其
$$
v_t(c_4)=2,\qquad v_t(c_6)=3,\qquad v_t(\Delta)=12,\qquad v_t(j)=-6.
$$
再作关于 $t^{-1}$ 的二次扭曲，$c_4$ 成为单位而判别式赋值变为 $6$，所以该扭曲是分裂乘性曲线；剩余域为代数闭域，故无非分裂歧义。

由 Tate 参数描述，原曲线在惯性上的模 $p$ 表示为这个 Tate 表示乘以分歧二次特征。一个温和惯性生成元的像可写成
$$
-\begin{pmatrix}1&6\\0&1\end{pmatrix}
$$
（改变生成元只把右上角乘以非零标量）。因为 $p>3$，它的阶是 $2p$。因此 $G$ 包含一个非平凡上幺幂元，而该元素的幂给出全部上幺幂群
$$
U=\left\{\begin{pmatrix}1&a\\0&1\end{pmatrix}:a\in\mathbb F_p\right\}.
\tag{23.6}
$$

### 2.2 排除不变直线

如果 $G$ 保持一条 $\mathbb F_p$ 直线，则 $\mathcal F$ 在函数域 $k(C_c)$ 上有有理循环 $p$-子群。由 $X_0(p)$ 的模解释，得到非恒定映射
$$\overline C_c\longrightarrow X_0(p)$$
与 $j$ 映射相容。

$X_0(p)\to X(1)$ 的次数为 $p+1$：在一般椭圆曲线上有恰好 $p+1$ 个循环 $p$-子群，且一般自同构 $\{\pm1\}$ 保持每个子群。因此映射次数的乘法给出
$$p+1\mid\deg(j)=6,$$
与 $p>37$ 矛盾。这一论证也包括可能的不可分次数，因为非恒定有限曲线映射的总次数仍相乘。

### 2.3 一个初等矩阵论证

无须调用完整有限子群分类。$U$ 的唯一不变直线是 $\mathbb F_pe_1$。由上段，存在 $h\in G$ 将它移到不同的直线。上幺幂群传递作用于其余射影直线，所以可先乘一个 $u\in U$，使 $uh$ 将 $\mathbb F_pe_1$ 送到 $\mathbb F_pe_2$。

于是 $(uh)U(uh)^{-1}$ 是全部下幺幂群。上、下幺幂矩阵通过初等行变换生成 $\operatorname{SL}_2(\mathbb F_p)$，故
$$G=\operatorname{SL}_2(\mathbb F_p).$$

## 3. 亏格与所有大素数处的点

上述覆盖只可能在 $O$ 上方分歧，因为仿射族上判别式处处为单位。其惯性阶已算为 $2p$。在所考虑的正特征中，特征大于 $B>d$，故覆盖温和。

令 $Y\to C_c$ 为辛层覆盖，$\overline Y$ 为光滑射影完备化。Riemann–Hurwitz 公式给出
$$
2g(\overline Y)-2
=d\left(1-\frac1{2p}\right),
$$
因此
$$
g(\overline Y)=1+\frac{(p^2-1)(2p-1)}4=g.
\tag{23.7}
$$
几何无穷点的数目为
$$
r=\frac d{2p}=\frac{p^2-1}{2},\qquad 2g+r=d+2.
\tag{23.8}
$$

现在设 $\ell>B$，$\ell\ne q$，在 $\mathbb F_\ell$ 上取 $c=q^p$，并把常值空间 $V$ 换成 $A[p]$ 的约化。具体地定义
$$
Y_{q,p}/\mathbb F_\ell
=\operatorname{Isom}^{\mathrm{sp}}(A[p],\mathcal F[p])
\quad\text{位于 }C_{q,p}/\mathbb F_\ell\text{ 上方}.
$$
它是前面几何覆盖的一个下降形式；第 2 节说明它几何连通，亏格仍为 $g$。Hasse–Weil 界及删去无穷点给出
$$
\#Y_{q,p}(\mathbb F_\ell)
\ge \ell+1-2g\sqrt\ell-r.
\tag{23.9}
$$
因为 $\sqrt\ell>d+3=2g+r+1$，右边严格为正。所以总有仿射 $\mathbb F_\ell$ 点，包含一组 $(\overline X,\overline W)$ 和一个辛 $p$-挠点同构。

这些点可提升到 $\mathbb Z_\ell$：基曲线光滑；$\ell\ne p$；两条椭圆曲线均有好约化。因此辛同构空间是基曲线上的有限 étale 概形，Hensel 引理同时提升参数和同构。

这里直接在每个 $\mathbb F_\ell$ 上证明几何连通性和亏格，不需要预先断言某个未检查的射影整数模型在所有大素数处有好约化。

## 4. 同时解决全部小素数

定义有限整数
$$
M=2^4\,3^2
\prod_{\substack{5\le\ell\le B\\\ell\text{ 为素数}}}\ell.
\tag{23.10}
$$
令
$$L=\mathbb Q(A[p])\,\mathbb Q(\zeta_M).$$
这是有限 Galois 扩张。Chebotarev 密度定理保证在 $L$ 中完全分裂的素数有正密度，因而有无穷多个这样的素数 $q>B$。选取其中任意一个。于是
$$q\equiv1\pmod M,$$
且 $A[p]$ 在 $G_{\mathbb Q_q}$ 上平凡。

对每个 $\ell\le B$，$q$ 是 $\mathbb Q_\ell$ 中的十二次幂：

- $\ell\ge5$ 时，$q\in1+\ell\mathbb Z_\ell$，而 $12$ 在 $\mathbb Z_\ell$ 中可逆，Hensel 引理给出十二次根。
- $\ell=2$ 时，$q\in1+16\mathbb Z_2$；$\mathbb Z_2^\times$ 的四次幂恰含 $1+16\mathbb Z_2$，取三次幂在 $2$ 进单位上是自同构，故 $q$ 为十二次幂。
- $\ell=3$ 时，$q\in1+9\mathbb Z_3$；三次幂把 $1+3\mathbb Z_3$ 双射到 $1+9\mathbb Z_3$，第四次幂在 $1+3\mathbb Z_3$ 上是自同构。

取 $u_\ell\in\mathbb Z_\ell^\times$ 满足 $u_\ell^{12}=q^p$，置
$$
X_\ell=u_\ell^4,\qquad W_\ell=0.
\tag{23.11}
$$
这确实满足 (23.2)。相应的
$$F_\ell:y^2=x^3-u_\ell^4x$$
由坐标缩放 $(x,y)=(u_\ell^2x_A,u_\ell^3y_A)$ 与 $A$ 同构；椭圆曲线同构严格保持 Weil 配对。

特别地，在 $2$ 处 $X_2\equiv1\pmod{16}$、$W_2=0$，满足更强的固定惯性域条件；在 $3,p$ 处也获得所要求的局部模型。这里 $p\le B$ 已包含在小素数集合中。

## 5. 新分母素数 q 处的单位部分

不能只检查判别式赋值是 $p$；本节还控制 Tate 参数的单位。

在 $\mathbb Q_q$ 中取
$$
W_q=\frac1{216}.
$$
多项式
$$X^3-\left(q^p+\frac1{1728}\right)$$
模 $q$ 在 $X=1/12$ 有单根，故 Hensel 引理给出单位根 $X_q$。于是
$$
X_q^3-27W_q^2=q^p.
$$
相应的 $F_q$ 具有
$$
c_4=48X_q\in\mathbb Z_q^\times,\qquad
c_6=8,\qquad
\Delta=64q^p.
$$
所以显示模型极小并为乘性约化。分裂性等价于 $-c_6=-8$ 在剩余域中为平方；因为 $q\equiv1\pmod{16}$，此条件成立。

还得到精确公式
$$
j(F_q)=1728+q^{-p}.
\tag{23.12}
$$
令 $\tau_q$ 为 Tate 参数。由 Tate $j$ 展开的逆展开，
$$
\tau_q=j^{-1}(1+O(j^{-1}))
=q^p(1+O(q^p)).
$$
因此 $\tau_q/q^p\in1+q\mathbb Z_q$。由于 $q\ne p$，取 $p$ 次幂在此主单位群上是自同构，所以
$$\tau_q\in\mathbb Q_q^{\times p}.$$
又 $q\equiv1\pmod p$，故 $\mu_p\subset\mathbb Q_q$；Tate 曲线的 $p$ 挠点由 $\mu_p$ 和 $\tau_q^{1/p}$ 生成，所以 $F_q[p]$ 的 Galois 作用平凡。

按 $q$ 的选取，$A[p]$ 的局部 Galois 作用也平凡。两个二维辛空间之间当然有严格保持配对的同构。这证明 (23.3) 在 $q$ 处也成立。

## 6. 实位置、原始性及模型的独立性

实位置取 $W_\infty=0$、$X_\infty=q^{p/3}>0$，相应曲线与 $A/\mathbb R$ 同构。

对 $\ell\ne q$，等式右边是 $\ell$ 进单位；若 $X_\ell,W_\ell$ 同时被 $\ell$ 整除，左边就被 $\ell$ 整除，矛盾。对 $\ell=q$，第 5 节明确给出两个单位。$q$ 与 $6p$ 互素，故其余原始性条件成立。

所有奇素数 $\ell\ne q$ 处，整模型的判别式 $64q^p$ 是单位，故好约化。在 $q$ 处为极小分裂乘性，在 $2$ 处判别式赋值为 $6$ 且与 $A$ 同构，证明陈述中的约化和导子数据。

这里不同位置的 $X_v,W_v$ 没有被要求来自同一组有理数。正是这个全局相容性问题仍然没有解决。固定的 $Z=q$、精确方程、全部原始性和实际局部辛同构都已经同时保留，故这比只满足一个有限 Frobenius 窗口更强。

若希望避免局部参数 $W_v=0$，也可在这些点附近作任意足够小的非零扰动。特征零中，辛同构覆盖是有限 étale 的，具有给定局部点的覆盖在足够小的解析邻域内仍有截面；基曲线也是光滑的。扰动可保持整性及所有赋值条件。不过这不是主陈述所需的额外输入。

## 7. 分裂指数时的射影局部整体反例

在 $\mathbb Q$ 上定义仿射曲线 $Y_{q,p}$，其点为 (23.2) 的解连同严格辛同构 $A[p]\simeq F[p]$。第 2—3 节的几何论证在特征零同样适用，所以它是一条几何连通光滑曲线。前面已证明它在每个完成域有点，且可选具有原始整坐标的局部点。

设 $Y_{q,p}(\mathbb Q)$ 有点，对应 $X,W\in\mathbb Q$。先证明对应 $F$ 必非 CM，这里不必假定 $X,W$ 为整数。

若 $j(F)$ 在 $q$ 处整，则从
$$j(F)=1728X^3/q^p$$
得到 $3v_q(X)\ge p$。因 $p\ne3$，其实 $3v_q(X)>p$。由
$$27W^2=X^3-q^p$$
可知 $2v_q(W)=p$，但左边是偶整数，右边是奇数，矛盾。所以 $v_q(j(F))<0$，$j(F)$ 不是代数整数，$F$ 非 CM。

如果 $p\equiv1\pmod4$，$A[p]$ 的像包含于分裂 Cartan 正规化子；R1 的完整像定理排除了非 CM 曲线在 $p>37$ 时具有这样的像。故
$$
Y_{q,p}(\mathbb Q)=\varnothing,\qquad
Y_{q,p}(\mathbb Q_v)\ne\varnothing\quad\text{对全部 }v.
\tag{23.13}
$$
还需排除射影边界上的有理点，不能从仿射空集直接跳到射影空集。记 $\overline Y_{q,p}$ 为光滑射影完备化。

### 7.1 尖点给出不变直线，而 A[p] 不可约

只使用全级模曲线尖点的标准模解释。几何尖点由退化的广义椭圆曲线及全级 $p$ 结构表示；可以取 Néron $p$ 边形。其恒等分支为 $\mathbb G_m$，而其中的 $p$ 挠点 $\mu_p$ 是一个典范的阶 $p$ 子群。经由级结构拉回，得到 $A[p]$ 中的一条直线 $L$。

这个直线不依赖于所选尖点代表：广义椭圆曲线的同构保持恒等分支，故保持其中的 $\mu_p$；级结构的 $\pm1$ 歧义也保持同一条直线。因此得到一个与 Galois 作用相容的赋值
$$
\{\text{$X_A^+(p)$ 的几何尖点}\}
\longrightarrow\{\text{$A[p]$ 中的直线}\}.
$$
若尖点定义于 $\mathbb Q$，其对应直线必在 $G_{\mathbb Q}$ 下稳定。这里只需要“不变直线”这个必要条件，无须对尖点上特征的精确 cyclotomic 因子作约定。

现在直接证明 $A[p]$ 对所有 $p>37$ 不可约：

- 若 $p\equiv3\pmod4$，R13 §2 已证明 $A$ 在 $p$ 好超奇异，且惯性像为完整非分裂 Cartan。此群在 $\mathbb F_p^2$ 上没有不变直线。
- 若 $p\equiv1\pmod4$，$A$ 在 $p$ 好普通。也可直接验证 Hasse 不变量：$(x^3-x)^{(p-1)/2}$ 中 $x^{p-1}$ 的系数为带符号的 $\binom{(p-1)/2}{(p-1)/4}$，模 $p$ 非零。因为 $i\in\mathbb Q_p$，CM 环 $\mathbb Z_p[i]\simeq\mathbb Z_p\times\mathbb Z_p$ 的两个幂等元把 $A[p]$ 分成两条局部 Galois 特征线。普通约化的连通—étale 正合列在这些 CM 幂等元下分裂，所以惯性像包含
  $$
  \left\{\begin{pmatrix}t&0\\0&1\end{pmatrix}:t\in\mathbb F_p^\times\right\}.
  \tag{23.14}
  $$
  这里连通分量在惯性上的特征为 $\chi_p$，étale 分量不分歧，而 $\chi_p(I_p)=\mathbb F_p^\times$。此群的仅有不变直线就是两条 CM 特征线。复共轭把 CM 自同态 $i$ 变为 $-i$，从而交换两条特征线。因此没有一条直线在全部 $G_{\mathbb Q}$ 下稳定。

两种情况均证明不可约性，故 $X_A^+(p)$ 没有有理尖点。这个固定 $A$ 的论证不依赖最新预印本的完整尖点分类；Freitas–Mocanu v4, Proposition 3.6 给出的一般判据与这里的必要条件相符。

### 7.2 从固定判别式覆盖映到模曲线

在 $Y_{q,p}$ 上的通用曲线及通用严格辛同构给出自然 $\mathbb Q$ 态射
$$
Y_{q,p}\longrightarrow X_A^+(p),\qquad
(X,W,\phi)\longmapsto(F_{X,W},\phi).
$$
目标射影，源的完备化光滑，所以这个态射唯一延拓为
$$\overline Y_{q,p}\longrightarrow X_A^+(p).$$
它与 $j$ 态射相容。$\overline Y_{q,p}\setminus Y_{q,p}$ 的每个点都位于 $\overline C_{q,p}$ 的无穷点上方；第 2 节已证明 $j$ 在该点有极点。因此边界的像都是 $X_A^+(p)$ 的尖点。

若边界有一个 $\mathbb Q$ 点，其像就是有理尖点，与第 7.1 节矛盾。故对全部 $p>37$，
$$
(\overline Y_{q,p}\setminus Y_{q,p})(\mathbb Q)=\varnothing.
\tag{23.15}
$$
结合 (23.13)，当 $p\equiv1\pmod4$ 时得到
$$
\overline Y_{q,p}(\mathbb Q)=\varnothing,\qquad
\overline Y_{q,p}(\mathbb Q_v)\ne\varnothing\quad\text{对全部 }v.
\tag{23.16}
$$
每个局部点原本就位于仿射部分，所以射影化不会损失它们。亏格是第 3 节计算的 $g$。

当 $p\equiv3\pmod4$，排除仿射有理点所需的全局矛盾不可用。本定理只证明同一批局部条件处处可满足，以及有理点若存在必须位于仿射部分；不能据此推出或否定全局点的存在。

## 8. 标准输入、来源和适用边界

本证明的几何单值群及亏格计算在第 2—3 节逐步给出，未当作外部黑箱。标准输入是 Tate 均匀化、$X_0(p)$ 的模解释、Riemann–Hurwitz、有限域曲线的 Hasse–Weil 界及 Chebotarev：

- Tate 均匀化及逆 $j$ 展开的具体版本见 R2、R7；可核查 J. H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves* (1994), Chapter V。
- $X_0(p)$ 的一般纤维含 $p+1$ 个循环子群，也对应模多项式双次数 $(p+1,p+1)$；参见 H. Darmon, *Rational points on curves* (2008), §3.1，[作者正文](https://www.math.mcgill.ca/darmon/pub/Articles/Expository/12.Clay/paper.pdf)，关于 $X_0(p)$ 和模多项式的部分。
- Chebotarev 的完全分裂素数正密度是无条件版本；参见 J.-P. Serre, *Quelques applications du théorème de densité de Chebotarev*, Publ. Math. IHÉS **54** (1981), 123–201，[DOI及全文入口](https://numdam.org/articles/10.1007/BF02698692/)。
- 大剩余特征处使用 Weil 界再提升点是标准方法；近期同类用途可核查 N. Freitas, D. Mocanu, *Local points on twists of $X(p)$ with applications*, [arXiv:2509.04294v4](https://arxiv.org/html/2509.04294v4)（2026-09-28），Theorem 4.5。本篇使用的是固定判别式的另一条覆盖，故已重新证明其连通性、亏格和删去无穷点后的界，没有把该文的 $X(p)$ 亏格直接代入。
- 射影边界只使用广义椭圆曲线的尖点模解释，以及第 7.1 节给出的 $A[p]$ 不可约性证明；普通/超奇异惯性所用标准形式与 R7、R13 的 Serre 1972 引用一致。Freitas–Mocanu v4, Proposition 3.6 另给出更强的一般尖点判据，此处仅用作交叉核对。文中的 $X_A^+(p)$ 与本文辛层覆盖不是同一条曲线；第 7.2 节明确构造二者之间的态射。

**对主问题的意义有限而精确：** 即使保留非空且只有一个素数的分母、精确 Fermat 等式、完整局部导子、超奇异约化及配对类型，再要求所有完成域上的实际挠点同构，仍不能仅以局部不可解排除任一 $p\equiv3\pmod4$ 的无限同余类。尚需一个真正的全局相容性或高度输入。本文没有完成 Serre 一致性。
