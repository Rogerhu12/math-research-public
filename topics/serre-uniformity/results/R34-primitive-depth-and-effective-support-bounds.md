# R34：原始点的任意局部深度与依赖分母支撑的显式界

日期：2026-11-12；会话：serre-uniformity-astra-cont/2026-11-12。

**状态：已证明，范围明确。** R32 把单素数分母的大指数归结到 Mordell–Weil 原始点本身的深分母。本文证明：秩至少二时，即使固定一条相关 Mordell 曲线，原始有理点在指定素数处也可以任意深；这些点必然逐渐引入其他分母。另一方面，已发表的有效整点与判别式界给出真正无条件、但依赖分母素数或支撑的上界。两者没有矛盾，也都没有解决绝对一致性。

## 1. 固定曲线与局部参数

固定素数 $q>7$，$r\in\{1,5\}$、$c\in\{1,8\}$，令
$$
D=D_{q,r,c}:\quad V^2=U^3-27cq^r.
\tag{34.1}
$$
以下第 2、3 节也适用于把右端常数 $-27cq^r$ 换成 $+27cq^r$；证明只用其 $q$ 进赋值为 $1$ 或 $5$、绝对值为 $27cq^r$。为保持与 R32 的记号一致，先采用显示的负号。

R32 第 3 节独立证明了保持滤过的群同构
$$
\mathcal L:D(\mathbb Q_q)\xrightarrow{\sim}\mathbb Z_q.
\tag{34.2}
$$
这里 $\mathcal L$ 是整圆盘参数 $t=-U/V$ 上的收敛形式对数，满足
$$
v_q(\mathcal L(P))=v_q(t(P)).
$$
若 $P\ne O$，定义
$$
a_q(P)=\max\{0,-\tfrac12v_q(U(P))\}.
$$
则 $v_q(\mathcal L(P))=a_q(P)$，且 $a_q(P)=k\ge1$ 等价于
$$
v_q(U(P))=-2k,\qquad v_q(V(P))=-3k.
\tag{34.3}
$$

特别地 $D(\mathbb Q_q)$ 无挠点，故 $D(\mathbb Q)$ 也无挠点。本文说“原始有理点”，是指在自由阿贝尔群 $D(\mathbb Q)$ 中不能写成 $[n]R$、$n>1$ 的非零点；这不是整数坐标之间互素的同义词。

## 2. 秩至少二时，原始点本身可以任意深

**定理 R34(a)。** 假设 $m=\operatorname{rank}D(\mathbb Q)\ge2$。则存在整数 $a_0\ge0$，使对每个
$$k\ge\max\{1,a_0\}$$
都有一个 Mordell–Weil 原始点 $P_k\in D(\mathbb Q)$ 满足 $a_q(P_k)=k$。如果 $D(\mathbb Q)$ 含一个在 $q$ 处整的非零点，则可以取 $a_0=0$。

**证明。** 取一个真正的 $\mathbb Z$-基
$$D(\mathbb Q)=\mathbb ZR_1\oplus\cdots\oplus\mathbb ZR_m.$$
令
$$a_0=\min_i v_q(\mathcal L(R_i)).$$
所有对数都非零，因为 (34.2) 单射。重新编号，使 $R_2$ 达到这个最小值，并取任一不同的基向量 $R_1$。于是
$$
\alpha=q^{-a_0}\mathcal L(R_1)\in\mathbb Z_q,\qquad
\beta=q^{-a_0}\mathcal L(R_2)\in\mathbb Z_q^\times.
$$
给定 $k\ge\max\{1,a_0\}$，写 $e=k-a_0\ge0$。由于 $\beta$ 可逆，可以选取整数
$$0\le n_k<q^{e+1}$$
使
$$\alpha+n_k\beta\equiv q^e\pmod{q^{e+1}}.$$
置
$$P_k=R_1+[n_k]R_2.$$
它的 Mordell–Weil 坐标是 $(1,n_k,0,\ldots,0)$，故为原始向量。群对数给出
$$
v_q(\mathcal L(P_k))
=a_0+v_q(\alpha+n_k\beta)
=a_0+e=k.
$$
这证明所需精确深度，而不只是深度至少为 $k$。

如果存在一个 $q$ 整的非零有理点 $T$，则 $\mathcal L(T)$ 为单位。将 $T$ 写为基向量的整数线性组合，便知至少一个 $\mathcal L(R_i)$ 是单位，否则所有线性组合都被 $q$ 整除。因此 $a_0=0$。证毕。

这个论证必须从一个 Mordell–Weil 基或已知饱和的原始子格出发。仅有两个线性独立点，并不能自动保证每个 $R_1+[n]R_2$ 在整个有理点群中原始；上述基的选取避免了这一缺口。

不同 $k$ 的点必不相同。若需要一个粗糙的构造高度估计，典范高度的正定二次型性质还给出
$$
\widehat h(P_k)\le
2\widehat h(R_1)+2q^{2(k-a_0+1)}\widehat h(R_2).
\tag{34.4}
$$
这个上界不控制其他分母，更不能保证 $P_k$ 来自 R19。

### 2.1 一个无条件的具体高秩例子

取
$$
q=113,\qquad r=c=1,\qquad
D:\ V^2=U^3-3051.
$$
它有整数点
$$P=(15,18),\qquad Q=(51,360),$$
因为 $15^3-3051=18^2$、$51^3-3051=360^2$。

模 $7$ 是好约化，并得到
$$\widetilde D:\quad V^2=U^3+1.$$
逐一代入 $U\in\mathbb F_7$，该群的点为
$$
O,\ (0,\pm1),\ (1,\pm3),\ (2,\pm3),\ (4,\pm3),
\ (3,0),\ (5,0),\ (6,0).
$$
倍点公式给出
$$
2\widetilde D(\mathbb F_7)=\{O,(0,1),(0,6)\}.
$$
另一方面，
$$
\overline P=(1,4),\qquad
\overline Q=(2,3),\qquad
\overline P-\overline Q=(4,3).
$$
这三个点都不属于 $2\widetilde D(\mathbb F_7)$，所以 $\overline P,\overline Q$ 在
$\widetilde D(\mathbb F_7)/2\widetilde D(\mathbb F_7)$ 中线性独立。约化映射经过
$$D(\mathbb Q)/2D(\mathbb Q),$$
而后者因无挠而具有 $\mathbb F_2$ 维数 $\operatorname{rank}D(\mathbb Q)$。于是
$$\operatorname{rank}D(\mathbb Q)\ge2.$$
又 $P$ 在 $113$ 处整，故 R34(a) 的 $a_0=0$。这条固定曲线上存在每个精确深度 $k\ge1$ 的原始有理点。

这并不是 R19 的反例。它没有宣称这些原始点只在 $113$ 有分母，也没有宣称 $113$ 满足 R13 对某个大素数 $p$ 的全部分母条件。

## 3. 控制全部分母以后，深度有显式上界

以下使用 von Känel (2014), Corollary 7.4 的已发表有效结果。设 $S$ 为有限素数集、$N_S=\prod_{\ell\in S}\ell$，$b\in\mathbb Z\setminus\{0\}$，定义
$$
A_S(b)=2^8\,3^5 N_S^2
\prod_{\substack{\ell\notin S\\v_\ell(b)>0}}
\ell^{\min\{2,v_\ell(b)\}}.
\tag{34.5}
$$
对任意 $U,V\in\mathbb Z[S^{-1}]$ 满足 $V^2=U^3+b$，该定理给出
$$
h(U),h(V)\le h(b)+4A_S(b)\bigl(\log A_S(b)\bigr)^2.
\tag{34.6}
$$
这里 $h$ 是绝对对数 Weil 高度；对既约有理数 $a/d$，$d>0$，有
$h(a/d)=\log\max\{|a|,d\}$。第 6 节给出原始来源和准确引用。

**定理 R34(b)。** 取 $S=\{q\}$ 以及 (34.1)。令
$$
A_q=
\begin{cases}
2^8\,3^7q^2,&c=1,\\
2^{10}\,3^7q^2,&c=8,
\end{cases}
\qquad
H_q=r\log q+\log(27c)+4A_q(\log A_q)^2.
\tag{34.7}
$$
则任何只在 $q$ 有分母的非零有理点 $T$ 都满足
$$
\boxed{\quad a_q(T)\le\frac{H_q}{3\log q}.\quad}
\tag{34.8}
$$
因此这个界是无条件且适用于任意秩的，量级为 $O(q^2\log q)$。

**证明。** 对 $b=-27cq^r$，$h(b)=r\log q+\log(27c)$。在 (34.5) 中，$q$ 已被放入 $S$，其赋值不进入外部乘积。当 $c=1$ 时，外部乘积为 $3^2$；当 $c=8$ 时，为 $2^2 3^2$。这正给出 (34.7)。

若 $a_q(T)=a\ge1$，则 (34.3) 说明 $V(T)$ 的既约分母恰为 $q^{3a}$，所以
$$3a\log q\le h(V(T))\le H_q.$$
若 $a=0$，结论显然成立。证毕。

### 3.1 对 R32 的深生成元给出一个实际界

假设 $D(\mathbb Q)=\mathbb ZR$，且存在 R32 的某个解点 $P=[n]R$，其正规化分母为 $q^k$。极小模型分母的整除性质 $B_1\mid B_n$ 强迫 $R$ 也只在 $q$ 有分母。因此 (34.8) 真正适用于该生成元：
$$a_q(R)\le \frac{H_q}{3\log q}.$$

这回答了“深生成元能否无条件有一个实际上界”的有限范围问题；常数明确依赖 $q$。不应略去“生成元只在 $q$ 有分母”的理由：任意有理生成元并不自动是 $\{q\}$-整点。也不应将右端随 $q$ 增长的界读成 R32 所缺少的绝对起点界。

同一论证也约束 R32 第 5.1 节的原始点 $R_0$，因为 $B(R_0)\mid B(P)$。它不需要秩一。

### 3.2 高秩构造必然离开每个固定分母支撑

更一般，固定任何包含 $q$ 的有限素数集 $S$。将 (34.5) 的 $A_S(-27cq^r)$ 代入 (34.6)，得到每个 $S$-整点的 $q$ 深度界
$$
a_q(T)\le
\frac{r\log q+\log(27c)+
4A_S(-27cq^r)\bigl(\log A_S(-27cq^r)\bigr)^2}
{3\log q}.
\tag{34.9}
$$
因此 R34(a) 的序列 $P_k$ 对足够大的 $k$ 必有一个分母素数不在 $S$。这给出有效的“离开固定支撑”结论，甚至不必只诉诸 Siegel 有限性。

尤其不能把高秩的 $q$ 进逼近当作单素数分母解的构造。它精确说明：全局原始性和一个位置的任意深度可以同时成立；真正需要控制的是所有其他有限位置。

## 4. 对本题 Frey 曲线更强的支撑界

R19 的额外原始性与奇偶条件提供了更强输入：相应的 Frey 曲线 $F$ 满足
$$
|\Delta_{\min}(F)|=2^\delta |Z|^p,\qquad
N_F=32\operatorname{rad}(|Z|),\qquad
\delta\in\{6,9,12\}.
\tag{34.10}
$$
这里 $\delta$ 分别对应族 I、II、III；无论 $Z$ 正负，取绝对值后的公式成立。

von Känel (2014), Corollary 6.2 给每条 $F/\mathbb Q$ 的无条件不等式
$$
\log|\Delta_{\min}(F)|
\le3N_F(\log N_F)^2+124.
\tag{34.11}
$$

**定理 R34(c)。** 任何 R19 解，写
$$R_Z=\operatorname{rad}(|Z|)>1,$$
必满足
$$
\boxed{\quad
p\log|Z|
\le96R_Z\bigl(\log(32R_Z)\bigr)^2+124-\delta\log2.
\quad}
\tag{34.12}
$$
特别地，
$$
p\le
\frac{96R_Z\bigl(\log(32R_Z)\bigr)^2+124-\delta\log2}
{\log|Z|}.
\tag{34.13}
$$
当 $|Z|=q^e$、$q$ 为素数且 $e\ge1$ 时，
$$
pe\le
\frac{96q\bigl(\log(32q)\bigr)^2+124-\delta\log2}
{\log q}.
\tag{34.14}
$$
对 $e=1$，这是一个 $O(q\log q)$ 的显式指数界，不需要任何 Mordell–Weil 秩假设。

**证明。** 将 (34.10) 直接代入 (34.11)：
$$
\delta\log2+p\log|Z|
\le3(32R_Z)\bigl(\log(32R_Z)\bigr)^2+124.
$$
移项即得 (34.12)，而 $\log|Z|>0$，所以可以除以它。$|Z|=q^e$ 时再用 $\log|Z|=e\log q$。证毕。

### 4.1 固定允许素数集时的完全显式有限性

若预先固定有限集合 $T$，要求所有 $q\mid Z$ 都属于 $T$，并令
$$R_T=\prod_{q\in T}q,$$
则 $N_F\le32R_T$。由于 $x\mapsto x(\log x)^2$ 在 $x\ge1$ 上递增，(34.11) 给出
$$
p\log|Z|\le96R_T\bigl(\log(32R_T)\bigr)^2+124.
\tag{34.15}
$$
这里还可保留负项 $-\delta\log2$；为得到统一显示的简单界，舍去该负项。又本题 $|Z|\ge5$，故
$$
p\le
\frac{96R_T\bigl(\log(32R_T)\bigr)^2+124}{\log5}.
\tag{34.16}
$$
这不仅说固定支撑只有有限多个指数，还给出显式界。对每个这样的 $p$，(34.15) 又界定 $|Z|$，因此可能的有符号 $Z$ 有限且可有效枚举。

不能因为 $T$ 可在证明中任意选择，就把常数认作绝对常数：取不同的 $T$ 会改变右端。

## 5. 为什么这些结果仍不产生绝对指数界

R13 强迫新分母素数满足 $q\equiv\pm1\pmod{4p}$；其中分裂素数还有 $q\ge4p^2+1$。这些是对 $q$ 的下界。R34(c) 给出的是
$$p\ll q\log q$$
这样的反向上界，它允许 $q$ 随 $p$ 任意增长，不能和前述下界合成矛盾。

R32 的原始除子定理限制了“有理群中做多少次全局 $q$ 倍乘”，但原始点本身仍可以有深分母。R34(a) 在一个实际高秩曲线上证明了这一现象，不允许把全部原始点的局部深度视为自动有界。R34(b)、(c) 进一步说明：限制全部分母后确有有效界，但现有界仍随支撑增长。

因此仍缺少的全局输入可以准确表述为：对满足 R19 全部条件的解，在分母支撑允许变化时，排除 $p\to\infty$。本文没有声称所有 $D_{q,r,c}$ 秩一，没有假设深生成元不存在，也没有把高度界、原始除子个数界或局部逼近扩大为统一整性定理。

## 6. 文献与可核查输入

- R. von Känel, *Integral points on moduli schemes of elliptic curves*, **Transactions of the London Mathematical Society 1** (2014), 85–115，DOI [10.1112/tlms/tlu003](https://doi.org/10.1112/tlms/tlu003)；[出版社完整原文](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/tlms/tlu003)。Corollary 6.2 是 (34.11)；§7.3.2 的定义及 Corollary 7.4 是 (34.5)–(34.6)。这些是已经发表的无条件结果，不依赖 BSD、GRH 或 $abc$。本文只取用这两个准确陈述，随后显式代入本题参数。
- 本仓库 [R32](R32-prime-denominator-rank-one-window.md) 第 2–3 节给 (34.1) 模型的极小性、整个 $\mathbb Q_q$ 点群的形式对数同构与精确滤过；本文没有另用未核查的局部分支群分类。
- 本仓库 [R19](R19-converse-fermat-fixed-cm.md) 的 (19.3) 给本题精确极小判别式与导子。若只给一条任意 Mordell 曲线或不满足 R19 原始性的数据，不得直接套用 (34.10)。

本文件的新内容是高秩原始点的精确深度构造、可手算的具体例子，以及现成有效定理在本课题中的准确参数化推论；没有将所引高度定理本身称为新结果。
