# R15：秩一谱收缩、临界零型与非零极限的传递条件

**状态：以下命题均给出完整证明；它们是中间结论，不解决一般 Hilbert ISP，不主张文献新颖性。**

日期：2026-11-12。会话：Astra-ISP-e2cb8f94；并行研究：general_routes。

本文推进 `open.md` 中怎样把近似秩一扰动传到非零极限的缺口。有限维投影锚点的结果另见 [R17](R17-finite-dimensional-anchor-surgery.md)。所得结果包括可用的正面判据和弱极限相消丢失的障碍。全篇内积对第一变量线性，$u\otimes v$ 表示 $x\mapsto\langle x,v\rangle u$。

## 1. 整函数的无零圆盘给出全部矩的定量界

设 $T\in B(H)$ 拟幂零，$F=u\otimes v$ 的秩至多一，定义

$$
b_j=\operatorname{tr}(T^{j-1}F)=\langle T^{j-1}u,v\rangle\quad(j\ge1),
\qquad h_F(z)=\sum_{j\ge1}b_jz^j.
$$

这里允许 $F=0$，此时全部 $b_j=0$。定义只依赖 $T$ 的整函数级数主控量

$$
\mathcal S_T(R)=\sum_{j\ge0}\|T^j\|R^{j+1}\quad(R\ge0).
\tag{1.1}
$$

拟幂零性保证每个 $R$ 的级数有限，且

$$|h_F(z)|\le\|F\|\mathcal S_T(|z|).\tag{1.2}$$

秩一预解式恒等式给出

$$
\lambda\in\sigma(T+F),\quad\lambda\ne0
\quad\Longleftrightarrow\quad
q_F(1/\lambda)=0,
\qquad q_F=1-h_F.
\tag{1.3}
$$

为使本笔记自含，令 $R_\lambda=(\lambda I-T)^{-1}$。若 $c=1-\langle R_\lambda u,v\rangle\ne0$，则直接相乘得到

$$
(\lambda I-T-F)^{-1}x
=R_\lambda x+c^{-1}\langle R_\lambda x,v\rangle R_\lambda u.
$$

若 $c=0$，非零向量 $R_\lambda u$ 满足 $(T+F)R_\lambda u=\lambda R_\lambda u$。这同时证明了 (1.3) 两个方向。

### 命题 1：圆盘无零点的定量矩估计

设 $R>0$，$\|F\|\le M$，并假设 $q_F$ 在 $|z|\le R$ 无零点。记

$$L(R)=\log\bigl(1+M\mathcal S_T(R)\bigr).$$

则对所有整数 $m\ge1$，

$$
|b_m|\le\frac1{R^m}
\sum_{k=1}^m\binom{m-1}{k-1}\frac{(2L(R))^k}{k!}.
\tag{1.4}
$$

如果另有 $b_1=\cdots=b_{m-1}=0$，则有更强的界

$$|b_m|\le \frac{2L(R)}{R^m}.\tag{1.5}$$

**证明。** 在圆盘上取唯一满足 $g(0)=0$ 的解析对数 $q_F=e^g$；因为 $q_F(0)=1$，这样的归一化可以取到。由 (1.2)，

$$\operatorname{Re}g(z)=\log|q_F(z)|\le L(R)\quad(|z|\le R).$$

写 $g(z)=\sum_{j\ge1}c_jz^j$。对 $0<r<R$，实部的 Fourier 系数给出

$$
c_jr^j=\frac1\pi\int_0^{2\pi}\operatorname{Re}g(re^{it})e^{-ijt}\,dt.
$$

常数 $L(R)$ 对此非零 Fourier 模式的积分为零；又由调和均值公式，$\operatorname{Re}g$ 在该圆周的平均为零。因此

$$
|c_j|r^j
\le\frac1\pi\int_0^{2\pi}\bigl(L(R)-\operatorname{Re}g(re^{it})\bigr)\,dt
=2L(R).
$$

令 $r\uparrow R$，得到 $|c_j|\le2L(R)R^{-j}$。由 $h_F=1-e^g$，逐项比较形式幂级数的第 $m$ 个系数可得

$$
|b_m|\le\sum_{k=1}^m\frac1{k!}
\sum_{j_1+\cdots+j_k=m\atop j_i\ge1}|c_{j_1}\cdots c_{j_k}|.
$$

正整数有序分拆 $(j_1,\ldots,j_k)$ 的个数为 $\binom{m-1}{k-1}$，所以得到 (1.4)。若前 $m-1$ 个 $b_j$ 为零，则 $g=\log(1-h_F)=-b_mz^m+O(z^{m+1})$，故 $c_m=-b_m$，由已经证明的 $c_m$ 估计得到 (1.5)。证毕。

### 谱半径下界的直接用法

如果 $b_1=\cdots=b_{m-1}=0$，且一个 $R>0$ 满足

$$R^m|b_m|>2\log\bigl(1+\|F\|\mathcal S_T(R)\bigr),\tag{1.6}$$

则 $q_F$ 必在 $|z|\le R$ 有零点。该零点不是 $0$，故 (1.3) 给出 $T+F$ 的非零特征值 $\lambda$，满足 $|\lambda|\ge1/R$。不满足低阶矩消失时，可用 (1.4) 的右端代替 (1.5)。这些估计允许任意复相位，并不依赖正性。

## 2. 对 R5 阶数边界的补充：允许临界阶的零型

R5 的有限阶判据要求 $|h(z)|\le C\exp(C|z|^\rho)$ 且 $\rho<m$。命题 1 给出稍宽的准确条件。

### 命题 2：临界阶零型的单参数判据

设整函数 $h$ 满足 $h(0)=0$、$h(z)=O(z^m)$，并且

$$
\log\left(1+\max_{|z|\le R}|h(z)|\right)=o(R^m)
\quad(R\to\infty).
\tag{2.1}
$$

若存在 $\alpha\ne0$ 使 $1-\alpha h$ 无零点，则 $h\equiv0$。

**证明。** 令 $1-\alpha h=e^g$ 且 $g(0)=0$。对任意 $R$ 使用命题 1 证明中的 Fourier 系数界，有

$$
|c_j|\le2R^{-j}\log\left(1+|\alpha|\max_{|z|\le R}|h(z)|\right).
$$

由 (2.1)，令 $R\to\infty$，所有 $j\ge m$ 的 $c_j$ 均为零；而 $h=O(z^m)$ 说明 $g=O(z^m)$，所以 $c_1,\ldots,c_{m-1}$ 也为零。因此 $g=0$，进而 $h=0$。证毕。

所以可以把 R5 中的严格增长阶条件替换为 (2.1)。这覆盖“增长阶恰为 $m$、但该阶的型为零”的情形。R5 的临界例子 $h(z)=1-e^{z^m}$ 满足 $\log M_h(R)\asymp R^m$，不满足 (2.1)，故与此补充完全相容。

这仍没有构造一个满足拟幂零性的非零秩一扰动，不能从增长条件本身推得 ISP。

## 3. 有界秩一族：谱收缩等价于所有矩消失

### 命题 3：谱半径与矩的序列判据

设 $T$ 拟幂零并满足

$$\log\bigl(1+\mathcal S_T(R)\bigr)=o(R).\tag{3.1}$$

设 $F_n$ 的秩至多一且 $\sup_n\|F_n\|<\infty$。则以下两项等价：

$$r(T+F_n)\longrightarrow0;\tag{3.2}$$

$$\operatorname{tr}(T^jF_n)\longrightarrow0\quad\text{对每个固定 }j\ge0.\tag{3.3}$$

**证明。** 令 $M=\sup_n\|F_n\|$，并写 $b_{n,m}=\operatorname{tr}(T^{m-1}F_n)$。

先设 (3.2)。对每个固定 $R$，充分大的 $n$ 满足 $r(T+F_n)<1/R$，由 (1.3)，$q_{F_n}$ 在 $|z|\le R$ 无零点。因此命题 1 给出

$$
\limsup_{n\to\infty}|b_{n,m}|
\le\frac1{R^m}\sum_{k=1}^m\binom{m-1}{k-1}\frac{(2L(R))^k}{k!}.
$$

由 (3.1)，$L(R)=o(R)$。固定 $m$ 后令 $R\to\infty$，右边每一项均趋零，证明 (3.3)。

反之，若 (3.3) 成立，则对任意固定 $R$，有 $h_{F_n}\to0$ 于 $|z|\le R$ 一致。理由是每个有限首段的系数趋零，而尾段有一致可求和上界

$$|b_{n,m}|R^m\le M\|T^{m-1}\|R^m.$$ 

因此充分大的 $n$ 满足 $\sup_{|z|\le R}|h_{F_n}(z)|<1$，故 $q_{F_n}$ 在该圆盘无零点，由 (1.3) 得 $r(T+F_n)<1/R$。$R$ 任意，得到 (3.2)。这个反向推论不需要 (3.1)。证毕。

### 一个可由幂直接检查的充分条件

若

$$j\|T^j\|^{1/j}\longrightarrow0,\tag{3.4}$$

则 (3.1) 成立。事实上，给定 $\varepsilon>0$，充分大的 $j$ 有

$$\|T^j\|\le(\varepsilon/j)^j\le\varepsilon^j/j!,$$

于是 $\mathcal S_T(R)$ 被一个固定多项式加上 $R e^{\varepsilon R}$ 控制；除以 $R$ 取对数上极限至多 $\varepsilon$，再令 $\varepsilon\downarrow0$。

特别地，R9 的 $A$ 满足 (3.1)：由 [R13](R13-all-normalized-powers-and-binary-cluster-set.md) 的精确幂范数及 [R14](R14-backward-minimal-images-all-exponents.md) 的 $L_k\ge16^k$，当 $j\ge1$、$k=\lfloor\log_2j\rfloor$ 时，$\|A^j\|\le a_k\le e^{-16^k}\le e^{-j^4/16}\le e^{-j^2/16}$。还可完成平方得到，对 $R\ge1$，

$$
\mathcal S_T(R)
\le CC_cR\exp\!\left(\frac{(\log R)^2}{4c}\right),
\qquad C_c=2+\sqrt{\pi/c}.
\tag{3.5}
$$

这里使用高斯格点和的一致上界 $\sum_{j\in\mathbb Z}e^{-c(j-a)^2}\le2+\int_{\mathbb R}e^{-cx^2}\,dx$；按峰值两侧单调性将各格点项与相邻单位区间积分比较即可证明。因此 (1.6) 中的对数上界只有 $O((\log R)^2)$。

**实际含义。** 对该 $A$ 搜索有界复秩一扰动时，“扰动后谱半径趋零”准确等价于每个固定矩的相消误差趋零。但这不意味着扰动有非零可用极限；下一节给出确切反例和可用的附加紧致性条件。

## 4. 两个弱极限不能保留相消；一个强极限可以

### 命题 4：非零 WOT 秩一极限可以丢掉全部拟幂零性

在 $H=\ell^2(\{0,1,2,\ldots\})$ 上，令

$$u_n=e_0+e_n,\qquad v_n=e_0-e_n,\qquad F_n=u_n\otimes v_n\quad(n\ge1).$$

则 $\|F_n\|=2$，$F_n^2=0$，但

$$F_n\longrightarrow e_0\otimes e_0\quad\text{于 WOT}.\tag{4.1}$$

极限是非零正交投影，其谱半径为 $1$。

**证明。** $\langle u_n,v_n\rangle=0$ 给出 $F_n^2=0$。对任意固定 $x,y$，$\langle x,e_n\rangle,\langle e_n,y\rangle\to0$，直接展开 $\langle F_nx,y\rangle$ 得到 (4.1)。因此，虽然两个向量各自都弱趋于 $e_0$，其配对从恒等于零变为一。证毕。

取 $T=0$，已经得到“$T+F_n$ 全拟幂零、$F_n$ 有非零 WOT 秩一极限，但 $T+F$ 不拟幂零”的反例。若希望 $T\ne0$，可在一个额外的二维正交直和分量上放一个非零二阶幂零算子，且令各 $F_n$ 在该分量为零；结论不变。

这里所有 $F_n$ 的范数都有固定正下界，两个因子的弱极限也都非零。因此这些条件仍不能代替所需的矩连续性。

### 命题 5：一个因子强收敛的可用传递判据

设 $T$ 拟幂零，$u_n\to u$ 强、$v_n\rightharpoonup v$ 弱，且 $T+u_n\otimes v_n$ 全拟幂零。则 $T+u\otimes v$ 拟幂零。若 $T$ 还满足 (3.1)，且 $u,v\ne0$，则

$$
M=\overline{\operatorname{span}}\{T^ju:j\ge0\}\subset v^\perp
$$

是非零真闭 $T$-不变子空间。

**证明。** 弱收敛使 $v_n$ 一致有界；所以对每个 $j$，

$$
\langle T^ju_n,v_n\rangle-\langle T^ju,v\rangle
=\langle T^j(u_n-u),v_n\rangle+\langle T^ju,v_n-v\rangle\longrightarrow0.
$$

利用 (1.2) 的一致尾界，$h_{u_n\otimes v_n}\to h_{u\otimes v}$ 在每个紧圆盘上一致。因此无零点整函数 $1-h_{u_n\otimes v_n}$ 的极限 $1-h_{u\otimes v}$ 仍无零点：若极限在某点有零点，它不恒为零，因为在 $0$ 取值一；在该零点周围取一个不含其他零点的小圆，Rouché 定理就会强迫充分大的近似函数在圆内也有零点，矛盾。由 (1.3)，极限扰动拟幂零。

在 (3.1) 下，命题 2 的 $m=1$ 情形给出 $h_{u\otimes v}=0$，所以全部矩消失，得到所写的 $M$。证毕。

强弱角色可对调，证明相同。也可以允许基算子 $T_n\to T$ 于算子范数，前提是每个 $T_n$、$T$ 和 $T_n+u_n\otimes v_n$ 均拟幂零：对每个紧 $K\subset\mathbb C\setminus\{0\}$，预解式恒等式及 Neumann 小扰动展开使 $(\lambda I-T_n)^{-1}\to(\lambda I-T)^{-1}$ 在 $K$ 一致，再用同样的行列式/Rouché 论证。不能只以“谱半径对算子范数连续”替代此证明，因为一般谱半径并无这种连续性。

### 命题 6：非零 WOT 极限加上无范数损失足以补回强收敛

设 $F_n$ 秩至多一，$F_n\to F$ 于 WOT，且 $\|F_n\|\to\|F\|$。则 $F$ 秩至多一，且 $F_n\to F$ 于 Hilbert–Schmidt 范数，因而也于算子范数。

**证明。** 任意四个固定向量给出的 $2\times2$ 矩阵元行列式对 $F_n$ 均为零；取极限仍为零，所以 $\operatorname{rank}F\le1$。秩至多一给出 $\|F_n\|_{HS}=\|F_n\|$ 和 $\|F\|_{HS}=\|F\|$。WOT 收敛蕴含对任意有限秩算子 $K$ 的 Hilbert–Schmidt 配对收敛；由一致 HS 范数界和有限秩算子在 HS 空间的稠密性，得到 $F_n\rightharpoonup F$ 于该 Hilbert 空间。其范数也收敛，因此 $F_n\to F$ 于 HS 范数。证毕。

命题 4 的例子正好具有范数损失：$\|F_n\|=2$，而 $\|F\|=1$。对实际模型若要利用命题 6，需要另外证明无范数损失，现有有限截断没有给出这个条件。

## 5. 适用边界与来源

仍缺少一个具有非零强弱极限，或无范数损失极限的秩一族构造。一般有界算子也尚未无损归约到 (3.1) 的拟幂零类；这些判据不能据此当作一般 ISP 的解答。

相关来源为 Adi Tcaciuc, *On quasinilpotent operators and the invariant subspace problem*, J. Math. Anal. Appl. 477 (2019), 187–195；[作者 arXiv v2 全文](https://arxiv.org/html/1805.03277v2)，Lemma 2.1、Theorem 2.3。本文所用预解式、整函数和极限论证均已独立写全，没有把文献的双参数等价化当作存在性证明。
