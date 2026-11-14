# 闭理想标准性：原文条件、非绝对级数的解析乘法障碍

日期：2026-11-12。独立文献与模型核验稿；不宣称全部闭理想已经标准。

本稿固定实际径向 dyadic odometer 算子 $A$ 及其有单位范数闭代数

$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}.
$$

结论分三类。第一，说明“每个非零闭理想包含一个 $A$ 的幂”的准确含义。第二，逐项检查可获得的原始文献，记录实际权不满足的条件。第三，证明一个比 $\mathcal L_W\subsetneq\mathcal A$ 更强的实际障碍：R112 的同一元素 $S$ 在乘以任意非零收敛解析芽 $F(A)$ 后仍不属于 $\mathcal L_W$；另外，$\mathcal A$ 上每个非零乘法算子都不弱紧。这些障碍不构成非标准闭理想的例子。

## 1. 固定记号及已证接口

引用 R32 的规范系数与 Fejér 范数收敛。对 $X\in\mathcal A$，记其唯一形式级数为

$$
X\sim\sum_{n\ge0}c_n(X)A^n,
\qquad
\kappa_n(X)=W_nc_n(X),
\qquad W_n=\|A^n\|.
$$

每个规范系数都是连续线性泛函，且

$$
|\kappa_n(X)|\le\|X\|.
\tag{1.1}
$$

形式乘法与算子乘法相容。令 $M_n=A^n/W_n$，故 $\|M_n\|=1$。本模型的准确二进制乘积公式是

$$
W_n=\prod_{j:b_j(n)=1}d_j,
\quad d_j=W_{2^j}=e^{-\Lambda_j},
\quad
\Lambda_j=100\,16^j-105\,8^j+(150j+25)2^j.
\tag{1.2}
$$

特别地，$W_0=1$、$W_1=e^{-20}$，且两个非负整数的二进制支撑不交时

$$
W_{a+b}=W_aW_b.
\tag{1.3}
$$

一般情况下 $W_{a+b}\le W_aW_b$。$W_n^{1/n}\to0$。相邻权比为

$$
\frac{W_{n+1}}{W_n}=\alpha_{v_2(n+1)}.
\tag{1.4}
$$

以下只使用这些已证事实及 R112 的明确构造。

## 2. 含一个幂与闭理想标准性等价

定义

$$
J_r=\{X\in\mathcal A:c_0(X)=\cdots=c_{r-1}(X)=0\},
\qquad J_0=\mathcal A.
$$

由系数连续性及 Fejér 范数收敛，

$$
J_r=\overline{A^r\mathcal A},
\qquad
\mathcal A/J_N\simeq\mathbb C[z]/(z^N).
\tag{2.1}
$$

这里第一式的反包含要用 Fejér：对 $X\in J_r$，其 Fejér 多项式没有低于 $r$ 的项，所以每个都属于 $A^r\mathbb C[A]$。这不是把任意理想作 gauge 平均。

**引理 2.1。** 若非零闭理想 $I\subseteq\mathcal A$ 包含某个 $A^N$，则 $I=J_r$，其中

$$
r=\min\{\operatorname{ord}X:0\ne X\in I\}.
$$

**证明。** $J_N\subseteq I$。若 $r=0$，则 $I$ 含一个在 $\mathcal A$ 中可逆的元素，结论立即成立。否则在有限维商 $\mathcal A/J_N$ 内，选择 $X\in I$ 的首非零次数 $r$。其像等于 $z^r u(z)$，其中 $u(0)\ne0$，故 $u$ 在 $\mathbb C[z]/(z^N)$ 中可逆。于是 $z^r\in I/J_N$，从而 $A^r\in I$。由 (2.1)，$J_r\subseteq I$；$r$ 的最小性给出反包含。证毕。

因此下列三条等价：

1. 每个非零闭理想含某个 $A^N$；
2. 每个非零闭理想等于某个 $J_r$；
3. 对任意 $0\ne X\in\mathcal A$，都有 $\overline{X\mathcal A}=J_{\operatorname{ord}X}$。

若这些性质成立，则 $\mathcal A$ 的每个非零元素在 $H$ 上单射：取 $A^r$ 为 $XQ_n$ 的范数极限，$Xh=0$ 将推出 $A^rh=0$，而实际 $A$ 单射。再用已有的反线性对称，可得稠密值域。

**尚未证明的部分是上列等价性质本身。** R32 的形式环无零因子，只能推出 $\mathcal A$ 内部没有代数零因子。它不能单独推出 Hilbert 空间核为零，也不能证明任意闭理想对 gauge 作用不变。

## 3. 两种范数完成不能混同

定义绝对规范幂级数代数

$$
\mathcal L_W
=\left\{\sum_{n\ge0}a_nM_n:\sum_{n\ge0}|a_n|<\infty\right\},
\qquad
\|X\|_{\mathcal L_W}=\sum_{n\ge0}|\kappa_n(X)|.
\tag{3.1}
$$

由

$$
M_iM_j=\frac{W_{i+j}}{W_iW_j}M_{i+j},
\quad 0<\frac{W_{i+j}}{W_iW_j}\le1,
$$

它是有单位 Banach 代数，并有单射、连续、像稠密的同态

$$
\mathcal L_W\longrightarrow\mathcal A,
\qquad \|X\|\le\|X\|_{\mathcal L_W}.
$$

形式变量记法下，它就是 $\ell^1(W)$。R112 已证明该包含严格。因而关于 $\ell^1(W)$ 范数闭理想的定理，不因多项式在两边都稠密而自动成为关于 $\mathcal A$ 范数闭理想的定理。

## 4. R112 元素无法由任何有限幂正则化

本节只从 R112 的具体分解中抽取所需数据，完整 Hadamard 构造见
`2026-11-12-bounded-quadratic-no-l1-power-series-0c-agent.md`。

该稿构造了 $S\in\mathcal A$ 及

$$
S=P+E,\qquad P\in\mathcal A,\quad E\in\mathcal L_W.
\tag{4.1}
$$

有两两不交、整体向高位移动的有限指标块 $I_b,J_b$，大小均为

$$
N_b=2^{4b},\qquad t_b=2^{-b},
$$

以及 Hadamard 矩阵 $H_b$，使得对 $i\in I_b,j\in J_b$，

$$
u_{ij}=t_bN_b^{-3/2}(H_b)_{ij},
\qquad
\kappa_{2^i+2^j}(P)=4u_{ij}.
\tag{4.2}
$$

不同指标对给出不同的二进制双位指数，而且

$$
\sum_{i\in I_b,j\in J_b}|u_{ij}|
=t_bN_b^{1/2}=2^b.
\tag{4.3}
$$

**命题 4.1。** 对每个固定整数 $k\ge0$，

$$
A^kS\notin\mathcal L_W.
\tag{4.4}
$$

**证明。** 固定 $k$。充分高的整块中，每个 $i,j$ 都高于 $k$ 的全部非零二进制位。对 $n=2^i+2^j$，(1.3) 给出 $W_{n+k}=W_nW_k$。由于乘 $A^k$ 只是把形式系数平移，

$$
\kappa_{n+k}(A^kP)
=\frac{W_{n+k}}{W_n}\kappa_n(P)
=4W_ku_{ij}.
\tag{4.5}
$$

这里不存在其他系数向同一指数卷积抵消的问题：乘子是单项式，映射 $n\mapsto n+k$ 单射。由 (4.3)，$A^kP$ 的规范系数绝对和发散。另一方面，$A^k\in\mathcal L_W$，所以 $A^kE\in\mathcal L_W$。若 $A^kS\in\mathcal L_W$，则相减将给出 $A^kP\in\mathcal L_W$，矛盾。证毕。

特别地，对任意 $k\ge0$，

$$
A^k\mathcal A\not\subseteq\mathcal L_W.
\tag{4.6}
$$

### 4.1 任何非零收敛解析芽也不能正则化同一元素

**推论 4.2。** 若 $F\in\mathbb C\{z\}$ 非零，则

$$
F(A)S\notin\mathcal L_W.
\tag{4.7}
$$

**证明。** 写 $F(z)=z^ku(z)$，$u(0)\ne0$。$u$ 与 $u^{-1}$ 均为收敛解析芽。其 Taylor 系数至多指数增长，而 $W_n^{1/n}\to0$，故两者在 $A$ 的 Taylor 演算都属于 $\mathcal L_W$，并互为逆元。因此若 $F(A)S\in\mathcal L_W$，则

$$
A^kS=u(A)^{-1}F(A)S\in\mathcal L_W,
$$

与命题 4.1 矛盾。证毕。

这一推论只讨论**实际乘积是否属于** $\mathcal L_W$。它没有断言 $\overline{S\mathcal A}$ 不含 $A^N$：该闭包使用更弱的算子范数，$\mathcal L_W$ 在此范数下不闭，乘积可在 $\mathcal A$ 中收敛而不在 $\mathcal L_W$ 中收敛。

## 5. 实际权不满足已核验的星形条件

令 $h(n)=-\log W_n$。Thomas 1998 的式 (1.3)、Definition 1.4（原页 162）要求存在 $\varepsilon>0$，使得对全部 $0\le m<n$，

$$
\frac{n\,[h(n)-h(m)]}{(n-m)h(n)}\ge\varepsilon.
\tag{5.1}
$$

其无对数形式为

$$
W_n^{\,1-\varepsilon(n-m)/n}\le W_m.
$$

本模型取 $m=2^j,n=2^j+1$，有

$$
h(m)=\Lambda_j,
\quad h(n)=\Lambda_j+20,
\quad
\frac{n\,[h(n)-h(m)]}{(n-m)h(n)}
=\frac{20(2^j+1)}{\Lambda_j+20}\longrightarrow0.
\tag{5.2}
$$

因此没有任何正的 $\varepsilon$ 可用。这已经使 Thomas 1998 Theorem 2.9 不适用，无须再推测其峰点假设。普通 star-shaped 条件也失败：$h(n)/n$ 在上述相邻点从高值下降。

这一障碍不能用通常的等价权修改消除。若

$$
-\log\widetilde W_n=h(n)+cn+O(1)
$$

且 $\widetilde W$ 仍为正的递减根式权，则在同一相邻点，分子对应的增量为 $20+c+O(1)$，分母的平均斜率仍趋于无穷。因此 (5.1) 的下确界仍为零。这里特别包括对权乘常数范围内的等价修改及固定指数重标度。

同样，$\log W_n$ 不是凹序列：在 $n+1=2^j$ 的大幅下降之后，下一步下降仅为 $20$，相邻斜率不是非增序列。本文不据未获得全文的 Grabiner 1975 原文作更强应用。

## 6. 无固定幂使平移变紧，非零乘法甚至不弱紧

对每个固定 $k\ge1$，由 (1.3)，充分大 $j$ 时

$$
\frac{W_{2^j+k}}{W_{2^j}}=W_k>0.
$$

再结合次乘性，得到准确式

$$
\limsup_{n\to\infty}\frac{W_{n+k}}{W_n}=W_k.
\tag{6.1}
$$

所以在相应加权序列空间中，固定幂右平移的权不趋于零。特别地，不能把本模型当作权比趋零的 Donoghue 型紧移位。

下面还有一个仅依赖实际规范系数的更强结论。

**命题 6.1。** 对每个 $0\ne F\in\mathcal A$，Banach 空间 $\mathcal A$ 上的乘法算子

$$
L_F:X\longmapsto FX
$$

非紧。

**证明。** 选 $r$ 使 $c_r(F)\ne0$，置 $a=|c_r(F)|W_r>0$。取多项式 $P$ 满足 $\|F-P\|<a/8$。由 (1.1)，

$$
|c_r(P)|W_r\ge a-\|F-P\|>7a/8.
$$

记 $D=\deg P$。选所有足够大的 $j$，使 $2^j>D$。此时 $PM_{2^j}$ 的形式支撑包含于 $[2^j,2^j+D]$，这些区间两两不交，并且

$$
\kappa_{2^j+r}(PM_{2^j})
=c_r(P)\frac{W_{2^j+r}}{W_{2^j}}
=c_r(P)W_r.
$$

故对不同的充分大 $j,\ell$，由 (1.1)，

$$
\|PM_{2^j}-PM_{2^\ell}\|>7a/8.
$$

于是

$$
\|FM_{2^j}-FM_{2^\ell}\|
>7a/8-2\|F-P\|>5a/8.
$$

而所有 $M_{2^j}$ 的范数均为 $1$。$L_F$ 把一个有界序列映为无收敛子列的序列，故非紧。证毕。

这里的非紧性发生在 **Banach 空间 $\mathcal A$ 的乘法表示**，不要与原始 $H$ 上的算子 $F$ 混写。它也不意味着闭理想非标准；非紧性和标准理想是不同性质。

### 6.1 Banach 弱拓扑与原 Hilbert 表示的弱算子拓扑给出更强障碍

以下加强由根代理指出，并在此给完整证明。

**命题 6.2。** 对每个 $0\ne F\in\mathcal A$，$L_F:\mathcal A\to\mathcal A$ 不弱紧。

**证明。** 写 $N_j=M_{2^j}$。它们都在 $\mathcal A$ 的闭单位球内，且 R12 的实际模型给

$$
N_j\xrightarrow[j\to\infty]{\mathrm{WOT}\text{ on }H}\frac12 I.
\tag{6.2}
$$

为说明这一极限不只是形式近似，实际一位块等式给 $N_j=E_j+\eta_j E_j^*N_{j+1}$，其中 $E_j=e_{10}$ 作用于第 $j$ 位，$\eta_j\to0$，故 $\|N_j-E_j\|\le\eta_j$。对固定的柱函数 $x,y$，充分高的第 $j$ 位是公平乘积常向量，因而 $\langle E_jx,y\rangle=\frac12\langle x,y\rangle$。由柱函数稠密及一致有界性，即得 (6.2)。于是

$$
FN_j\xrightarrow{\mathrm{WOT}\text{ on }H}\frac12F.
\tag{6.3}
$$

反设 $L_F$ 弱紧。则序列 $FN_j$ 在 $\mathcal A$ 的 Banach 弱拓扑中有收敛子网，极限记为 $X\in\mathcal A$。这里仅使用相对弱紧集的弱紧闭包及紧空间中的子网性质。

对每个固定 $n$，$FN_j$ 的形式首阶至少为 $2^j$，所以 $\kappa_n(FN_j)=0$ 最终成立。每个 $\kappa_n$ 是 $\mathcal A$ 上连续线性泛函，故 $\kappa_n(X)=0$ 对所有 $n$ 成立。R32 的系数忠实性推出 $X=0$。

另一方面，每个 Hilbert 矩阵元 $T\mapsto\langle Tx,y\rangle$ 也是 $\mathcal A$ 上连续线性泛函，因而该 Banach 弱收敛子网在 $H$-WOT 中也收敛到零。但 (6.3) 强制同一子网收敛到 $F/2\ne0$，矛盾。证毕。

因此，试图先在 $\mathcal A$ 上找到非零弱紧乘子，再以此控制闭理想或正则化系数，也没有这样的乘子可用。证明没有假定 Banach 弱拓扑与 $H$-WOT 相同；恰恰是两类连续泛函对假设的弱极限给出不相容的要求。

## 7. 原始文献逐项核验

本节只记录直接阅读过的定理条件。网络核验日期均为 2026-11-12；页码使用刊物原页码。临时 PDF 不属于仓库交付。

### 7.1 Peters 2024：规范代数、gauge 理想与真实可除性

Justin R. Peters, *Singly generated radical operator algebras*, New York J. Math. **30** (2024), 398–421。

- 官方全文：<https://nyjm.albany.edu/j/2024/30-15v.pdf>。
- 原文 Proposition 3.7，pp. 408–409：关于 $\|S\|$ 与 $\|Se_0\|_2$ 的范数比较，要求单边移位权绝对值非增且平方可和。
- Proposition 3.10，p. 410，及 Corollary 3.11，pp. 410–411：相应理想与不变子空间接口保留前述权条件。
- Proposition 3.12，p. 411：其主理想结论使用真正的有界分解 $S=T^kQ$，$Q$ 在相应有单位代数中；形式首项存在不足以给出这一分解。
- Proposition 3.13，pp. 411–412：代数无零因子，不是所有闭理想标准性。

实际权比 $\alpha_{v_2(n+1)}$ 在无限多个 $n$ 上等于 $\alpha_0>0$，既不平方可和，也不是非增序列，故不能使用前两条范数接口。第三条的可除条件必须另证，不能由形式阶数替代。R32 自含建立的规范系数仍然有效。

### 7.2 Thomas 1998：$\varepsilon$-star-shaped 是实质假设

Marc P. Thomas, *Closed ideals in the Banach algebra $\ell^1(\omega)$ when $\omega$ is $\varepsilon$-star shaped*, Proc. Edinburgh Math. Soc. **41** (1998), 161–176，DOI: 10.1017/S0013091500019489。

- 官方全文：<https://www.cambridge.org/core/services/aop-cambridge-core/content/view/38EA008451377E4B25BFF3EE98CF432C/S0013091500019489a.pdf/closed-ideals-in-the-banach-algebra-1w-when-w-is-star-shaped.pdf>。
- Definitions 1.1、1.2、1.4，pp. 161–162，分别给根式代数权、普通星形和 $\varepsilon$-星形条件。
- Theorem 2.9，pp. 174–175，证明续至 p. 176：除 $\varepsilon$-星形外，还要求给定首阶的 $\varepsilon$-峰点集合无限，才推出该元素生成标准闭理想。

第 5 节已经在本模型直接否定第一项关键条件；不能以 $W_n$ 衰减很快替代它。该文讨论的是 $\ell^1(\omega)$ 范数，另有第 3 节的完成空间差异。其引言引用 Domar 1987；本次未获得 Domar 原文，故不冒称已经逐项核实该文的全部条件。

### 7.3 Thomas 1984：已知反例不是任意半乘性权的定理

Marc P. Thomas, *A non-standard ideal of a radical Banach algebra of power series*, Acta Math. **152** (1984), 199–217，DOI: 10.1007/BF02392197。

- 大学文献库全文：<https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6353-11511_2006_Article_BF02392197.pdf>。
- 该文构造特定的半乘性权和生成元；下述结论须同时满足其下降点、权及系数的构造条件。
- p. 204 的条件 (A) 对下降点 $n(j)$ 要求 $n(1)=1$、$n(2)\ge4$，且 $n(j+1)>n(j)(n(j)+1)$；pp. 204–205 还有权和系数条件 (B)、(C)。Theorem 3.20，pp. 215–216，在这些具体构造条件下得到非标准闭理想。

本模型的整个下降尺度序列为 $2^j$，不满足条件 (A)。另选稀疏 dyadic 子序列还必须重新核对原文权与系数的构造条件 (B)、(C) 及其递推；本稿没有建立这个接口。因此不能由该文的特定反例直接判定实际闭理想标准或非标准。本次根核验取得了 p. 204 的条件 (A) 与 p. 215 的 Theorem 3.20 原文检索页；没有据未重新取得的式 (2.1) 原页作更强的递推比较。

### 7.4 Grabiner–Thomas 1985：转移引理所缺的包含关系

Sandy Grabiner and Marc P. Thomas, *Non-unicellular strictly cyclic quasinilpotent shifts on Banach spaces*, J. Operator Theory **13** (1985), 163–170。

- 官方全文：<https://jot.theta.ro/jot/archive/1985-013-001/1985-013-001-012.pdf>。
- 原文 Lemma 3.1，p. 166，假设两个 Banach 幂级数代数满足 $Rz^k\subseteq B\subseteq R$；在这个真实集合包含下，$R$ 内的非标准元素乘 $z^k$ 可转移为 $B$ 内的非标准元素。
- 同页 Theorem 3.2 为给定的归一化 $M$-基**构造**合适的权及非标准元素；不是对预先给定的任意权的断言。

若尝试在 Lemma 3.1 中放 $R=\mathcal A$、$B=\mathcal L_W$，命题 4.1 对每一个固定 $k$ 都否定所需包含 $Rz^k\subseteq B$。这指出该转移接口在实际模型中准确缺少什么，而不是只说两个范数不同。

## 8. 临时原文与核验位置

执行器曾在本轮重置，以下为重下载时采用的固定缓存名；正文来源和页码不依赖缓存继续存在：

- `/tmp/isp_ideal_sources/grabiner-thomas-1985.pdf`；关键原图 p. 166。
- `/tmp/isp_ideal_sources/thomas-1984.pdf`；关键条件原图 p. 204，结论 pp. 215–216。
- `/tmp/isp_ideal_sources/thomas-1998.pdf`；关键条件原图 p. 162，结论 pp. 174–176。
- `/tmp/isp_ideal_sources/peters-2024.pdf`；关键接口 pp. 408–412。

R112 的构造及 R32 的系数系统是本稿实际算子推论的内部依据；上述四篇原文只负责文献条件核验。尚无一篇在本次核验中给出覆盖整个实际 $\mathcal A$ 的闭理想标准性定理。另一方面，根代理与其他子任务正在对具有定量尾衰减的具体元素证明标准主理想；那些正结论与本稿的非正则化障碍相容。
