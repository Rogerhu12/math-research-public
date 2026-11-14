# R236 — 原首关系次数的精度夹逼、第一带有限像与低次重因子

日期：2026-11-13。**状态：同一原前缀的跨精度包含、所有深层的首层次数门、第一带完整像的长度及一个实际高重因子判据均已证明。** 本文没有证明双完整中央零迫出低次原核，没有把模 $p$ 因子自由提升成原 $p^N$ 关系。

本篇固定同一个原 $k$；精度或源次数改变时不更换窗口。承接 R233 的实际首项理想，并直接使用 R196 已证明的原 graph–Hasse 核。

## 1. 同一个原评价与次数记号

令 $p=4r-1\ge19$，$\mathcal O=\mathbf Z_p$。原权 $e_n$、有限环 $T_{k,N}$ 和环同态
$$
j_{k,N}:(\mathcal O/p^N)[A,C]\longrightarrow T_{k,N}
\tag{1}
$$
均取 R233 的定义。它们与原 $w$ 完整前缀整等价；源仍是原 $A,C=B-A$。

记 $\mathcal K_N=\ker j_{k,N}$，其总次数首项理想为 $\mathcal R(N)$。对 $0\le t<N$，仍令
$$
\mathcal I_{N,t}
=\frac{(\mathcal R(N):p^t)+p(\mathcal O/p^N)[A,C]}
 {p(\mathcal O/p^N)[A,C]},
\qquad
d_{N,t}=\min\{d:(\mathcal I_{N,t})_d\ne0\}.
\tag{2}
$$
这始终是 R233 的实际 colon 理想。

另外，定义同一原首层的最小关系次数
$$
\delta_1(k)=
\min\{d:\ker(j_{k,1}|_{\mathbf F_p[A,C]_{\le d}})\ne0\}.
\tag{3}
$$
它有限，例如足够高次的原 $C$ 幂已由阶截断而为零。这里没有把 (3) 的关系默认提升到更高精度。

## 2. 真实 colon 理想的跨精度夹逼

对 $N\ge2$，准确有
$$
\boxed{\quad
\mathcal I_{N,t}\subset\mathcal I_{N-1,t}
\quad(0\le t\le N-2),
\quad}
\tag{4}
$$
以及
$$
\boxed{\quad
\mathcal I_{N-1,t-1}\subset\mathcal I_{N,t}
\quad(1\le t\le N-1).
\quad}
\tag{5}
$$

**证明。** 若 $\overline H\in(\mathcal I_{N,t})_d$，则存在原齐次提升 $H$ 和 $\deg Q<d$，使
$$
j_{k,N}(p^tH+Q)=0.
$$
当 $t\le N-2$ 时，模 $p^{N-1}$ 约化保留这个最高次数部分，给 (4)。

反之，若
$$
j_{k,N-1}(p^{t-1}H+Q)=0,
$$
取整提升后将整条关系乘以 $p$，即得
$$
j_{k,N}(p^tH+pQ)=0.
$$
这给 (5)。第二步乘的是全部实际关系，第一步也保留全部低次补偿。没有除去某个未经核准的 $p$ 因子。$\square$

特别，在 $1\le t\le N-2$ 时，
$$
\boxed{\quad
d_{N-1,t}\le d_{N,t}\le d_{N-1,t-1}.
\quad}
\tag{6}
$$
允许 $+\infty$。迭代 (5) 还给
$$
d_{N,t}\le d_{N-t,0}.
\tag{7}
$$
这类传播本身不提供新的低次初始关系；一个已知固定深度输入只自动覆盖相应的有限层数。

## 3. 所有深层都必须先经过同一个原模 $p$ 核

**定理 1。** 对全部 $N\ge1$、$0\le t<N$，有
$$
\boxed{\quad
d_{N,t}\ge\delta_1(k),\qquad
d_{N,N-1}=\delta_1(k).
\quad}
\tag{8}
$$

**证明。** 设 $d=d_{N,t}<\infty$。由定义存在 primitive 齐次 $H$ 及原低次 $Q$，满足
$$
J_{<k}(p^tH+Q)\in p^NL_k,\qquad \deg Q<d.
$$
令整个多项式 $p^tH+Q$ 的实际公共系数赋值为 $b$。因为最高部分是 $p^tH$，有 $b\le t<N$。只除以这个实际内容，得到 primitive 原多项式 $P$，满足
$$
\deg P\le d,\qquad J_{<k}(P)\in p^{N-b}L_k\subset pL_k.
$$
故其非零约化落在 (3) 的核中，$\delta_1(k)\le d$。

取 (3) 中一个最小次数的非零关系 $\overline P$，其最高齐次部分 $\overline H$ 非零。任意整提升 $P$ 都满足 $J_{<k}(P)\in pL_k$。整条乘以 $p^{N-1}$ 后给模 $p^N$ 的实际关系，其最高部分是 $p^{N-1}H$。因此
$\overline H\in(\mathcal I_{N,N-1})_{\delta_1(k)}$，反向不等式成立。$\square$

所以 R233 的正比例深层方案，首先必须在同一 $k$ 找到次数低于相应比例的原模 $p$ 关系。高精度层数不能绕过这一首层门。(8) 只比较最小次数，不声称最高 colon 理想作为整个理想与 $\mathcal I_{1,0}$ 相等。

### 3.1. 正比例深 Smith 收益必先给固定比例低次首层关系

令 $M_d=(d+1)(d+2)/2$，并置
$$
d_*=\min\bigl(D,\delta_1(k)-1\bigr).
$$
按 (3)，原 $J_{<k}|_{E_{d_*}}$ 模 $p$ 单射，所以它有一个大小 $M_{d_*}$ 的单位 minor。该 minor 仍在原 $E_D$ 的同一个矩阵中。因此全矩阵的正 Smith 指数数目（包含特征零 kernel 的 $+\infty$ 指数）至多 $M_D-M_{d_*}$，从而对每个 $N\ge1$ 准确有
$$
\boxed{\quad
B_N(D,k)\le
N\left(M_D-M_{\min(D,\delta_1(k)-1)}\right).
\quad}
\tag{8a}
$$
特别，若 $\delta_1(k)>D$，则 $B_N(D,k)=0$ 对所有 $N$ 成立。

若某条路线在同一个原目标中取得
$B_N(D,k)\ge cNM_D$，其中固定 $c\in(0,1)$，则 (8a) 迫使
$$
\boxed{\quad
\delta_1(k)\le \sqrt{1-c}\,D+O_c(1).
\quad}
\tag{8b}
$$
因此 R223 所需的正比例深 Smith 或相应累计交集收益，不论以哪种方法构造，都必须先使原模 $p$ kernel 在固定比例较低的次数出现。这不是只针对 R233 某个充分构造的限制。

(8a) 没有使用中央零；它把双完整零尚需提供的首层算术输入明确化。更深的提升步骤不能代替 (8b) 所需的原低次关系。


## 4. 第一带的同一个实际 graph 理想及完整像长度

现在限制为 R196 的准确第一带
$$
k=rq+s,\qquad 0\le s<r,\qquad 0\le q\le p-2,\qquad k\ge1.
\tag{9}
$$
取原整轴 $f(y),c(y)$，并令
$$
\phi(A)=c(f^{-1}(A))=v_0A^2+O(A^3),
\qquad Z=C-\phi(A).
\tag{10}
$$
以下在 $\mathbf F_p$ 中读取。R196 证明：同一个原多项式
$$
P(A,Z+\phi(A))
=\sum_{j\ge0}a_j(A)Z^j
$$
属于原 $\ker j_{k,1}$，准确等价于
$$
a_j\in A^{(r-2j)_+}\mathbf F_p[[A]]
\quad(0\le j<q),\qquad
a_q\in A^{(s-2q)_+}\mathbf F_p[[A]].
\tag{11}
$$
也即属于实际的形式图理想
$$
\mathfrak M_{q,s}=
\left(
 A^{(r-2j)_+}Z^j\ (0\le j<q),\
 A^{(s-2q)_+}Z^q,\ Z^{q+1}
\right).
\tag{12}
$$
这里 (10) 的所有系数来自原轴；在限制原总次数时，不能把 $Z$ 当成一个免费的新多项式变量。

### 4.1. 全部原多项式像的准确长度

(12) 给一个有限商，其单项式基为
$$
A^aZ^j,\quad
0\le j<q,\ 0\le a<(r-2j)_+,
$$
再加上
$$
A^aZ^q,\quad 0\le a<(s-2q)_+.
\tag{13}
$$
因此完整原模 $p$ 像的维数准确为
$$
\boxed{\quad
\mu_{q,s}=
\sum_{j=0}^{q-1}(r-2j)_++(s-2q)_+.
\quad}
\tag{14}
$$

为说明这是原多项式像而不是更大的形式源：当 $q\ge1$ 时，商中 $A^r=0$，所以 $\phi(A)$ 只需其确定的 $r-1$ 阶截断，且
$Z=C-\phi_{<r}(A)$ 本来就在原多项式像中。$q=0$ 时同理只需模 $A^s$。故原 $\mathbf F_p[A,C]$ 确实满射到 (12) 的有限商。R196 的 kernel 等价式遂识别该商与原完整像。

特别，当 $q<r/2$ 时，
$$
\mu_{q,s}=qr-q(q-1)+(s-2q)_+,
$$
从而
$$
\boxed{\quad
k-\mu_{q,s}=q(q-1)+\min(s,2q).
\quad}
\tag{15}
$$
在 $q=O(1)$ 的大素数主带，这只给 $O(1)$ 个目标维数缺口。

### 4.2. 维数计数真正给到的次数

由 (14)，只要
$$
\binom{d+2}{2}>\mu_{q,s},
\tag{16}
$$
原 $E_d\bmod p$ 就有非零核。因此
$$
\boxed{\quad
\delta_1(k)\le
\min\left\{d:\binom{d+2}{2}>\mu_{q,s}\right\}
=\sqrt{2\mu_{q,s}}+O(1).
\quad}
\tag{17}
$$
这是无条件存在一个原关系的次数上界；没有给其更深提升。

当 $q=O(1)$ 且 $k\sim M_D=(D+1)(D+2)/2$ 时，(15)–(17) 的保证仍只是 $d/D\to1$。它本身不给 R233 所需的某个固定 $\theta<1$。若 $k$ 更大，单靠这个维数保证还可能超过当前 $D$。

### 4.3. 原稀疏单位行给出的下侧

R191/R209 的真实原行也给一个有用的对照。若 $2d<r$，则可按角阶
$\ell=m+c$ 选取
$$
rh+\ell,\qquad
0\le h<
\#\{m:\lceil\ell/2\rceil\le m\le\min(\ell,d)\}.
\tag{18}
$$
对角块为互异整数 $m$ 的单位 Vandermonde；全部所需行不超过
$$
r\lfloor d/2\rfloor+2\lceil d/2\rceil.
$$
所以
$$
\boxed{\quad
2d<r,\quad
k>r\lfloor d/2\rfloor+2\lceil d/2\rceil
\ \Longrightarrow\ \delta_1(k)>d.
\quad}
\tag{19}
$$
这是对同一个原模 $p$ 矩阵的单位 minor，不是仅有理秩的判断。

例如在 $4q<r$ 时，(19) 给
$$
\delta_1(k)\ge
\begin{cases}
2q,&s\le2q,\\
2q+1,&s>2q.
\end{cases}
\tag{20}
$$
在 (20) 与 (17) 之间，真正的最小次数仍由原 $\phi$ 的实际截断决定。

## 5. 实际中央删除不改变这个首层对象

用原轴的确定系数定义辅助比较轴
$$
f^\circ(y)=f(y)-\sum_{h\ge1}[y^{rh}]f\,y^{rh},
\qquad
c^\circ(y)=c(y)-\sum_{h\ge1}[y^{rh}]c\,y^{rh}.
\tag{21}
$$
这里只删除实际已有的中央项，并以同一个原第一带公式定义比较矩阵。它不被当成另一条全局椭圆曲线。

原第一带模 $p$ 行准确为
$$
\overline J_{rh+\ell}(P)
=\frac{a^h}{h!}[y^\ell](E^h\overline P)(f,c),
\qquad 0\le\ell<r,\quad h\le p-2,
\tag{22}
$$
其中 $a$ 是 R199/R203 的原单位，$E=A\partial_A+C\partial_C$。因为 (21) 不改变低于 $r$ 次的轴系数，(22) 直接给
$$
\boxed{\quad
\overline J=\overline J^\circ
\quad\text{在同一个原源及同一个第一带前缀上。}
\quad}
\tag{23}
$$
故 $\delta_1(k)$ 与完整首层 kernel 不因这个合法的实际比较而改变。这个等式本身不需要双完整中央零。

双完整零的进一步信息属于真实更高 $p$ 精度；R203 已保留其准确整行和高阶残差。若要由它们推出
$\delta_1(k)\le\theta D$，仍需使用原 theta/径向方程对 (10) 的额外算术约束。(23) 不能被用作“未来轴可任意选择”的模型论证，也不否认固定原函数可能具有这样的约束。

## 6. 很低次的原第一层关系必须含高重因子

下面的判据直接作用于 R196 的同一个实际原 kernel，不假定自由选取图系数。

**定理 2。** 假设 $q\ge2$，且
$$
0\ne P\in\ker(j_{k,1}|_{\mathbf F_p[A,C]}),
\qquad \deg P=d<p,
$$
并满足
$$
\boxed{\quad r-2(q-1)>d(d-1).\quad}
\tag{24}
$$
则 $P$ 含有一个依赖 $C$ 的非恒定不可约因子，重数至少为 $q$。特别，其次数不超过 $d/q$。

**证明。** 由 (11)，对全部 $0\le j<q$ 有
$$
\operatorname{ord}_A
\bigl((\partial_C^{[j]}P)(A,\phi(A))\bigr)\ge r-2j.
\tag{25}
$$
(24) 使这些下界在所需最小处为正。若 $P$ 仅依赖 $A$，则第零条已经迫
$\operatorname{ord}_AP\ge r>d$，不可能。

反设在 $\mathbf F_p(A)[C]$ 中，$P$ 的每个非恒定因子重数都小于 $q$。因为 $d<p$，这些因子关于 $C$ 可分，且 Hasse 导数在当前次数范围与通常的除阶乘导数一致。于是
$$
\gcd\bigl(P,\partial_C^{[1]}P,\ldots,
                  \partial_C^{[q-1]}P\bigr)=1
\quad\text{在 }\mathbf F_p(A)[C]\text{ 中}.
\tag{26}
$$
超过 $C$ 次数的导数置零。

在 $\overline{\mathbf F}_p$ 上选常数 $\lambda_j$，使
$$
Q=\sum_{j=1}^{q-1}\lambda_j\partial_C^{[j]}P
\tag{27}
$$
与 $P$ 在 $\overline{\mathbf F}_p(A)[C]$ 中互素。这样的常数组合存在：对 $P$ 的每个因子，不被它整除的导数至少有一个；坏组合分别属于一个真线性子空间，代数闭域无限，有限个这样的子空间不能覆盖全部选择。这里不要求 $\mathbf F_p$ 本身有足够多的可选点。

有 $\deg Q\le d-1$，且 (25) 给
$$
\operatorname{ord}_A Q(A,\phi(A))\ge r-2(q-1).
\tag{28}
$$
因此
$$
R(A)=\operatorname{Res}_C(P,Q)\ne0.
$$
若 $e=\deg_CP$、$f=\deg_CQ$，Sylvester 行列式的总次数界给
$$
\deg_A R
\le df+(d-1)e-ef
=d(d-1)-(d-e)(d-1-f)
\le d(d-1).
\tag{29}
$$
这也包括 $f=0$ 的情况。

同一 Sylvester 构造给无分母的多项式恒等式
$$
R(A)=U(A,C)P(A,C)+V(A,C)Q(A,C).
\tag{30}
$$
代入实际整图 $C=\phi(A)$，由 (25)、(28) 得
$$
\operatorname{ord}_A R\ge r-2(q-1)>d(d-1),
$$
与 (29) 及 $R\ne0$ 矛盾。故 (26) 不成立。关于 $C$ 的可分性遂迫 $P$ 有重数至少 $q$ 的因子；由 Gauss 引理可以取为
$\mathbf F_p[A,C]$ 中依赖 $C$ 的不可约因子。$\square$

此判据没有把 $A$ 的 content 因子当成所需因子：论证在
$\mathbf F_p(A)[C]$ 中识别了一个真正的 $C$ 因子。

## 7. 对深关系候选的应用及提升界限

若某个实际 colon 见证出现在次数 $d$，且满足 (24)，则按 R233 只除整条关系的实际公共内容后，可得到一个非零原模 $p$ kernel 向量 $\overline P$，其次数至多 $d$。因
$\deg\overline P(\deg\overline P-1)\le d(d-1)$，定理 2 适用。于是这个真实深关系的首层约化必有上述高重因子。

这只约束首层。它没有给出：

- 该因子自身在同一个 $k$ 中为零；
- 原整关系是该因子的 $q$ 次幂；
- 该模 $p$ 因子可在原次数预算内提升；
- 除去重因子以后，R233 的 $\beta_T$ 或 R218 的真实交集障碍自动消失。

原目标是带幂零元的有限环，乘积为零不能反推任一因子为零。若要利用这个因子得到更深原关系，仍须支付 R233 同一前缀中的实际 Hensel 障碍，以及全部低次补偿。

在 $p\asymp D^2$、$q=O(1)$ 的主带，(24) 给一个明确的很低次数候选筛；它没有覆盖所有 $d< D$。它的作用是识别哪些低次候选首先来自原多项式的重因子，再要求真正的后续提升。

### 7.1. 与 R223 大素数主带的准确交集

这个判据不覆盖 $d\sim D$ 的一般候选。令
$$
k\sim\kappa D^2,\qquad p\sim\alpha D^2,\qquad d\sim\theta D.
$$
固定整数 $q\ge2$ 时，$q=\lfloor k/r\rfloor$ 与 (24) 的有正宽度同时成立范围为
$$
\boxed{\quad
\max\!\left(\frac{4\kappa}{q+1},\,4\theta^2\right)
<\alpha<\frac{4\kappa}{q},
\quad}
\tag{31}
$$
右端的等号在 $q$ 带的端点可以允许；使用严格内区间可避免取整及端点误差。该范围非空准确要求
$$
\theta^2<\kappa/q.
\tag{32}
$$
特别，$q\ge2,\ \kappa\le1$ 时不能把它应用于 $\theta$ 接近一的全部候选。

不使用渐近记号时，给定 $k,d,q$ 的准确整数范围是
$$
\boxed{\quad
\max\!\left(
 \left\lfloor\frac{k}{q+1}\right\rfloor+1,\
 d(d-1)+2q-1
\right)
\le r\le\left\lfloor\frac{k}{q}\right\rfloor,
\quad p=4r-1\text{ 为目标素数}.
\quad}
\tag{33}
$$
这是同一个固定 $k$ 的范围，没有改用较短的前缀。

例如，若所用末前缀满足
$k/D^2\in[1/2+o(1),\,1+o(1)]$，取 $d\le2D/5$，则整个 $q=2$ 带
$$
\frac{k}{3}<r\le\frac{k}{2},
\qquad
\frac{4k}{3}<p+1\le2k
\tag{34}
$$
对充分大 $D$ 都满足 (24)。因为其下端有
$r>(1/6+o(1))D^2$，而
$d(d-1)+2\le(4/25)D^2+O(D)$。
所以这确实落在 $p\asymp D^2$ 的已付主带中，而不是只落在 $r>k$ 的窗口之外。

(31)–(34) 仍是候选的必要结构限制。若存在所需的原 primitive 深关系，它的模 $p$ 约化在此范围必须含高重因子；这可把后续提升计算集中到实际因子及其法向修正。当前没有证明这些修正可解，没有由重复因子得到正的 $\gamma$ 或 $\iota$ 下界，也没有排除落在 (24) 范围之外的其他低次候选。


## 8. 目前可落实的算术任务

(8) 把深层的起点固定为原 $\delta_1(k)$；(11)–(14) 给出这个首层对象的准确原图与完整像；(17)–(20) 说明无条件次数界目前覆盖的范围；(24) 进一步筛出很低次数的重因子情形。

因此 R233 所需的正比例深交集，仍须原双完整中央条件在这个固定对象上给出额外输入：首先迫出合适的低次原 graph–Hasse 关系，然后控制其真实提升或直接给多层 colon 的首关系次数上界。只增加形式递推的层数不会提供这一输入。本文也没有从有限素数计算推断它；没有新增目标素数扫描。

## 依赖

- [R233：原首项理想、colon shadow 与 Hensel 障碍](R233-original-cross-degree-leading-ideals-and-hensel-shadows.md)。
- [R196：完整原第一带 graph–Hasse kernel](R196-continuous-first-band-euler-pade-kernel.md)。
- [R191：原第一带稀疏单位行与次数消去](R191-first-band-source-divisibility-and-global-multiplicity.md)。
- [R209：同源降阶及混合 Euler Schur 像](R209-coherent-source-reduction-and-mixed-euler-schur-image.md)。
- [R203：实际全部中央方向及高精度残差](R203-finite-central-companion-and-rational-row-lattices.md)。
- [R223：正比例深 Smith 与原产品输入](R223-large-prime-deep-smith-and-original-product-input.md)。

主目标仍未完成。
