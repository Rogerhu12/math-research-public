# 奇偶反对角路线：平方约化没有消除闭图问题

日期：2026-11-12。会话：Astra-ISP-b382c564；并行推导：defect-route。

**结论状态。** 下文的块矩阵、子空间传递、图分类、拟相似及无界图例子均给出完整证明，是中间结论。“每个与非标量自伴单位对合反交换的拟幂零算子都有非平凡闭不变子空间”在本轮没有被证明，也没有被否定；不能把它当作外部已知定理。

## 1. 原始问题和精确块形式

设 $J=J^*=J^{-1}$ 非标量，$JT=-TJ$。令

$$H_+=\ker(J-I),\qquad H_-=\ker(J+I).$$

两者均非零，$H=H_+\oplus H_-$。反交换等式逐项给出

$$
T=\begin{pmatrix}0&A\\B&0\end{pmatrix},
\quad A:H_-\to H_+,\quad B:H_+\to H_-,
\qquad
T^2=\begin{pmatrix}AB&0\\0&BA\end{pmatrix}.
\tag{1.1}
$$

所以奇偶投影约化 $T^2$。但 $H_+$ 和 $H_-$ 一般均不对 $T$ 不变。

若 $T$ 有非零核，则其核已经是非平凡闭不变子空间（非零拟幂零算子的核不可能是整个空间）；若 $\overline{\operatorname{Ran}T}\ne H$ 且 $T\ne0$，该闭值域也是非平凡闭不变子空间。零算子当然有很多不变子空间。因此尚需研究的情形可以假设 $T$ 单射且值域稠密，等价于 $A,B$ 都单射且值域稠密。此时 $H_+,H_-$ 都必须无限维。

拟幂零条件由谱半径公式给出

$$r(T)=0\iff r(AB)=r(BA)=0.$$

它不蕴含 $A$ 或 $B$ 有有界逆。

## 2. 可直接使用的乘积子空间传递

### 命题 2.1

若 $N\subset H_+$ 为非零真闭 $AB$-不变子空间，则

$$\mathcal M=N\oplus\overline{BN}$$

是非零真闭 $T$-不变子空间。

**证明。** $B N\subset\overline{BN}$，而由 $ABN\subset N$、$A$ 有界及 $N$ 闭，有

$$A\overline{BN}\subset\overline{ABN}\subset N.$$

这正是块形式 (1.1) 所要求的不变性。正交直和闭；第一分量 $N$ 保证非零和非满。证毕。

交换 $A,B$ 可得到对应的 $BA$ 版本。特别地，若任一乘积算子的普通 ISP 能被解决，就能解决这个 $T$。

### 命题 2.2

若 $A,B$ 都单射且值域稠密，则 $AB$ 有非平凡闭不变子空间，当且仅当 $BA$ 有。

**证明。** 设 $N\subset H_-$ 是非零真闭 $BA$-不变子空间，取 $L=\overline{AN}\subset H_+$。由 $A$ 单射，$L\ne0$；由 $ABAN=A(BAN)\subset AN$，$L$ 对 $AB$ 不变。若 $L=H_+$，则

$$BH_+=B\overline{AN}\subset\overline{BAN}\subset N.$$

$B$ 的值域稠密和 $N$ 闭迫使 $N=H_-$，矛盾。故 $L$ 真。反向交换 $A,B$。证毕。

这一步的真性使用了另一个交织算子的稠密值域；不是一般的“取拟仿射像再闭包自然保持真性”。

## 3. 剩余子空间可能是无界闭图

称算子“传递”指其闭不变子空间只有零和全空间。以下是条件性结构描述，不断言传递算子存在。

### 命题 3.1

设 $A,B$ 为上述单射稠密值域算子，且 $AB$（因此也 $BA$）传递。若 $M\subset H_+\oplus H_-$ 是非零真闭 $T$-不变子空间，则存在稠密定义的闭线性算子

$$X:\mathcal D(X)\subset H_+\longrightarrow H_-$$

使 $X$ 单射、值域稠密，并有

$$
M=\operatorname{Graph}X,
\qquad
AX\mathcal D(X)\subset\mathcal D(X),
\qquad
XAXu=Bu\quad(u\in\mathcal D(X)).
\tag{3.1}
$$

还满足

$$
AB\mathcal D(X)\subset\mathcal D(X),
\qquad XABu=BAXu\quad(u\in\mathcal D(X)).
\tag{3.2}
$$

反之，任何非零稠密定义的闭 $X$ 满足 (3.1)，其图就是 $T$ 的非零真闭不变子空间。

**证明。** $M\cap H_+$ 对 $AB$ 不变；若非零，则由传递性它等于 $H_+$。再由 $T$-不变性和 $B$ 的稠密值域得 $M=H$，矛盾。因此 $M\cap H_+=0$。同理 $M\cap H_-=0$。

后一等式保证第一坐标投影在 $M$ 上单射，故 $M$ 是某线性算子 $X$ 的图；前一等式给 $X$ 单射。$M$ 闭使 $X$ 闭。$M$ 的两个坐标投影的闭包分别对 $AB,BA$ 不变；二者都非零，否则 $M$ 将落在某个坐标空间而与刚证的零交矛盾。由传递性，两个闭包分别为 $H_+,H_-$。所以定义域和值域都稠密。

对 $u\in\mathcal D(X)$，

$$T(u,Xu)=(AXu,Bu)\in M$$

恰好给出 (3.1)。再施加一次 $T$，得到

$$T^2(u,Xu)=(ABu,BAXu)\in M,$$

这给出 (3.2)。反向由同一个块乘法立即成立；图非零，且任何图都不含非零的垂直向量，所以真。证毕。

当 $A=I$ 时，(3.1) 就是

$$X\mathcal D(X)\subset\mathcal D(X),\qquad X^2u=Bu\quad(u\in\mathcal D(X)).$$

这正是一个可能无界的闭平方根图问题。对于一般非可逆 $A$，即使 $X$ 闭，也不能自动断言 $AX$ 闭。

### 与奇偶变换的关系

若 $M$ 对 $T$ 不变，则 $JM$ 也对 $T$ 不变，因为 $TJ=-JT$。$M\cap JM$ 和 $\overline{M+JM}$ 都同时对 $T,J$ 不变。如果其中一个非零且真，就得到按奇偶分解的子空间并可回到乘积算子。尚未排除的是

$$M\cap JM=0,\qquad\overline{M+JM}=H,$$

而 $M+JM$ 可能不闭。对于图 $X$，这个问题具体变成两个图 $\operatorname{Graph}(X)$ 和 $\operatorname{Graph}(-X)$ 的和；其定义域或值域可能仅稠密。

## 4. 与 companion 算子的关系是拟相似，不是自动的有界相似

令 $Q=AB$，并在 $H_+\oplus H_+$ 上定义

$$C_Q=\begin{pmatrix}0&I\\Q&0\end{pmatrix}.$$

考虑

$$
W(u,v)=(u,Av),\qquad
Y(u,v)=(v,Bu).
$$

当 $A,B$ 单射且值域稠密时，$W,Y$ 也单射且值域稠密。直接计算得

$$WT=C_QW,\qquad TY=YC_Q,\qquad WY=C_Q,\qquad YW=T.\tag{4.1}$$

所以 $T$ 与 $C_Q$ 拟相似。但是不能由此把 $C_Q$ 的任意不变子空间直接闭包传递为 $T$ 的非平凡不变子空间。

具体的危险可由一个初等例子看出：在 $\ell^2(\mathbb N)$ 上令 $De_n=n^{-1}e_n$、$y=(1/n)_{n\ge1}$、$N=y^\perp$。$D$ 单射且值域稠密，$N$ 闭且真，但 $\overline{DN}=H$。因为若 $z\perp DN$，则 $Dz\in\mathbb Cy$；而 $y\notin\operatorname{Ran}D$（否则原像为常数列），所以 $Dz=0$，进而 $z=0$。

若 $A$ 有有界逆，$W$ 才成为有界同构，(4.1) 才给有界相似。此时若 $Q$ 有有界平方根 $R$，则

$$X=A^{-1}R$$

满足 $XAX=A^{-1}R^2=B$，从而其图不变。在一般单射稠密值域情形，不能擅自使用这个 $A^{-1}$。

## 5. 平方有界且拟幂零，不保证闭平方根有界

以下例子完全在 Hilbert 空间内，并保留单射、稠密定义域、稠密值域和拟幂零平方，直接排除一个可能的闭图捷径。

在 $K=\ell^2(\mathbb Z)$ 上，定义正权

$$
r_{2m}=1+|m|,\qquad
r_{2m+1}=\frac{e^{-m^2}}{(1+|m|)(1+|m+1|)}
\quad(m\in\mathbb Z).
$$

令

$$
Re_j=r_je_{j+1},\qquad
\mathcal D(R)=\left\{u:\sum_jr_j^2|u_j|^2<\infty\right\}.
$$

$R$ 稠密定义、闭、单射且值域稠密：有限支撑序列包含在定义域和值域中；闭性由逐坐标收敛或“闭对角乘法再复合酉移位”得到。$r_{2m}\to\infty$ 表明 $R$ 无界。

但是相邻权的乘积为

$$
q_{2m}=r_{2m}r_{2m+1}=\frac{e^{-m^2}}{1+|m+1|},
\qquad
q_{2m+1}=r_{2m+1}r_{2m+2}=\frac{e^{-m^2}}{1+|m|}.
$$

它们均不超过一，且在两端趋零。定义有界算子

$$Qe_j=q_je_{j+2}.$$

有限坐标截断在范数下逼近 $Q$，故 $Q$ 紧；所有 $q_j>0$ 又使 $Q$ 单射且值域稠密。对 $u\in\mathcal D(R)$，

$$\sum_jr_{j+1}^2r_j^2|u_j|^2=\sum_jq_j^2|u_j|^2\le\|u\|^2,$$

所以 $Ru\in\mathcal D(R)$，并且

$$R^2u=Qu\qquad(u\in\mathcal D(R)).\tag{5.1}$$

此外，对每种奇偶性，$Q^n$ 的权乘积至多为

$$\exp\left\{-\sum_{l=0}^{n-1}(m+l)^2\right\}.$$

对实数 $m$ 取极小值也有

$$\sum_{l=0}^{n-1}(m+l)^2\ge\frac{n(n^2-1)}{12}.$$

因此

$$\|Q^n\|\le\exp\{-n(n^2-1)/12\},\qquad r(Q)=0.$$

于是 $C_Q$ 也是有界、单射、稠密值域、拟幂零的反对角算子，而

$$\operatorname{Graph}R$$

是它的非零真闭不变子空间：

$$C_Q(u,Ru)=(Ru,Qu)=(Ru,R^2u)\in\operatorname{Graph}R,$$

这里最后一步合法正是因为已经验证 $Ru\in\mathcal D(R)$。这个例子不声称 $Q$ 没有其他有界平方根；它证明的是，不能从“给定闭图平方根的平方有有界拟幂零延拓”推出该图平方根有界。

## 6. 一手文献核对及其使用边界

### 6.1 Halmos 平方问题

C. Foias, I. B. Jung, E. Ko, C. Pearcy, *Transitive operators and a problem of Halmos*, Indiana Univ. Math. J. **56** (2007), no. 1, 119–133，[DOI](https://doi.org/10.1512/iumj.2007.56.2948)，[作者机构原文](https://dspace.ewha.ac.kr/bitstream/2015.oak/234287/1/transitive%20operators.pdf)。

该文引言明确提出：若 $T^2$ 有非平凡闭不变子空间，是否 $T$ 也有？其 (1.2) 正是 $C_Q$ 形式；Lemma 2.1 在假设 $Q$ 传递时将 $C_Q$ 的非平凡闭不变子空间描述为可能无界的平方根图。本文 §3 给出了所需一般块形式的独立证明。该来源不能被引用成“平方约化自动解决 ISP”。

M. Contino, E. A. Gallardo-Gutiérrez, *A note on a Halmos problem*, Bull. London Math. Soc. **56** (2024), no. 12, 3681–3688，[DOI](https://doi.org/10.1112/blms.13159)，[arXiv:2409.01167v1](https://arxiv.org/abs/2409.01167v1)。其 Theorem 2.1 对拟幂零 $T$ 使用 $(T-\alpha I)^n$，要求 $\alpha\ne0$；Theorem 3.1 需要 $C_Q$ 与 $C_{-Q}$ 的**共同**不变子空间。这两项均不能替代本题所需的 $T^2$ 结论。

### 6.2 为什么非零平移没有解决奇偶问题

事实上，对于拟幂零 $T$ 及任何在零点附近全纯且 $p'(0)\ne0$ 的函数 $p$，局部解析反函数 $g$ 满足 $g(p(z))=z$。全纯函数演算给出 $T=g(p(T))$，而 $p(T)-p(0)I$ 拟幂零，使 $g$ 的局部 Taylor 级数在该算子上按范数收敛。因此

$$\operatorname{Lat}(p(T))=\operatorname{Lat}(T).$$

这包括 $p(z)=(z-\alpha)^n$、$\alpha\ne0$，但不包括 $p(z)=z^2$：后者在零点的导数为零，且没有零点附近的单值全纯平方根反函数。拟幂零谱恰含零，所以不能把这一步省掉。

作为直接相关的来源核验，2409.01167v1 的 Proposition 2.7 关于格相等的字面陈述不能使用。取无限维空间上的

$$T=\operatorname{diag}(1,-1)\oplus2I,$$

则 $0$ 属于 $\rho(T^2)$ 的无界分支，但 $\operatorname{span}\{(1,1,0)\}$ 对 $T^2$ 不变、对 $T$ 不变性不成立。错误捷径正是未经额外选支条件写出 $f(T^2)=T$。本笔记不依赖该命题。

## 7. 对当前模型的结论和未解决点

对于当前 $T_\lambda=S+\lambda V$，奇偶单位对合确实反交换，故 (1.1) 可用；已证的单射稠密值域与拟幂零性质并未使图条件自动成立。

可用的下一步是：证明偶部乘积 $AB$ 有非平凡闭不变子空间，使用命题 2.1；或者直接构造满足 (3.1) 的有界图/闭稠密域图，并逐项验证定义域稳定和图闭性。仅知 $T_\lambda^2$ 被奇偶投影约化，尚不完成其中任何一项。

本轮文献检索与推导没有找到可以不加条件地封闭这一差距的定理。不得把未知的图存在性、有界平方根存在性或拟相似传递真性写成已经成立。
