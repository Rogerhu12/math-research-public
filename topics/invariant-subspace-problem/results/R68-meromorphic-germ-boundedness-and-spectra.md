# R68：芽分式有界性的忠实判据与完整谱三分

日期：2026-11-12（UTC）。经主会话逐段核验。**状态：已证明。**

设 $\mathscr O=\mathbb C\{z,w\}$，$A,L$ 为 R60/R62 的实际算子。R66 已为每个分式 $R=F/G\in\operatorname{Frac}\mathscr O$ 定义唯一的最大闭实现

$$
T_R=G(A,L)^{-1}F(A,L),
$$

并证明其最小图等于最大图。本条证明其真实有界性完全忠实于解析芽：

$$
\boxed{T_R\text{ 有界}\iff R\in\mathscr O.} \tag{0.1}
$$

在有界情形 $T_R=R(A,L)\in\mathcal A$；不存在一个非全纯分式以某个隐藏在完整交换子内的有界算子实现。

因此每个非恒定分式的谱恰属以下三种情形：

| 分式在原点的性质 | 最大闭实现的谱 |
|---|---|
| $R\in\mathscr O$ | $\sigma(T_R)=\{R(0,0)\}$，该点为连续谱 |
| $R\notin\mathscr O$、$1/R\in\mathscr O$ | $\sigma(T_R)=\varnothing$ |
| $R\notin\mathscr O$、$1/R\notin\mathscr O$ | $\sigma(T_R)=\sigma_c(T_R)=\mathbb C$ |

常数分式 $R=c$ 给通常的有界标量算子 $cI$。

本条使用的是原 $L$ 的明确高位对数结构，不将结论未经证明扩到全部 $\mathcal A$ 或任意强交换子。主工具是混合高 dyadic 位的一个精确系数展开，以及低位解析函数在明确小圆上的 Cauchy 界。没有依赖浮点计算。

## 1. 模型、形式曲线及有限解析演算

沿用

$$
d_j=W_{2^j},\qquad W_n=\|A^n\|,\qquad
\Lambda_j=-\log d_j.
$$

这里用大写 $\Lambda_j$ 表示尺度，避免与谱参数混淆。R49 给出

$$
\Lambda_j=100\,16^j-105\,8^j+(150j+25)2^j,
\qquad
\Lambda_j\ge16\Lambda_{j-1},\qquad
\Lambda_0=20. \tag{1.1}
$$

特别地，$\Lambda_j/2^j$ 严格递增，且 $\Lambda_j\ge20\,16^j$。实际赋值权 $a_j$ 超快趋零；例如由既定权公式或 $a_j=a_0\prod_{i<j}\eta_i$、$\eta_i\le e^{-770\,16^i}$，它比 $j$ 的任意负幂更快趋零。

设

$$
\delta_j=\frac2{(j+2)^2+1},\qquad r_j=1-\delta_j,
$$

$$
\gamma_j(t)=\log(1+t)-\log(1+r_jt).
$$

这些函数在 $|t|<1$ 解析，$\gamma_j(0)=0$、$\gamma_j'(0)=\delta_j$。原 $L$ 为范数收敛算子级数

$$
L=\sum_{j\ge0}\gamma_j(A^{2^j}/d_j).
$$

其形式系数曲线记作

$$
\ell(z)=\sum_{j\ge0}\gamma_j(z^{2^j}/d_j)\in z\mathbb C[[z]]. \tag{1.2}
$$

每个固定形式次数只涉及有限多个 $j$。不声称 $\ell$ 在任何非零圆盘收敛；事实上系数增长正是后面证明的来源。

对 $H\in\mathscr O$，R62 的绝对范数演算与 R32 的连续形式系数相容：

$$
c\bigl(H(A,L)\bigr)=H(z,\ell(z)). \tag{1.3}
$$

因为 $A$、$L$ 的形式阶都至少为 $1$，每个固定次数只涉及 $H$ 的有限 Taylor 项；对范数绝对收敛级数使用连续系数泛函即得 (1.3)。R62 演算单射，R32 的形式系数也单射，故

$$
0\ne H\in\mathscr O\implies H(z,\ell(z))\ne0. \tag{1.4}
$$

因此每个非零分式 $R=F/G$ 都能沿这条形式曲线求值，得到

$$
r(z):=R(z,\ell(z))\in\mathbb C((z)).
$$

它是只有有限负阶的形式 Laurent 级数。

## 2. 真实有界因子强迫带权形式系数有界

R49 的等距含单位 $*$-表示

$$
\pi:C^*(I,A)\longrightarrow B(\ell^2(\mathbb N_0))
$$

把 $A$ 映为单边加权移位

$$
Je_k=a_{v_2(k+1)}e_{k+1},
\qquad
J^ne_k=\frac{W_{n+k}}{W_k}e_{n+k}.
$$

它只在此被用于转移正算子序，不转移原 Hilbert 表示的核。

### 引理 2.1

若存在任意 $B\in B(H)$ 满足

$$
G(A,L)B=F(A,L), \tag{2.1}
$$

则 $r(z)=R(z,\ell(z))$ 没有负阶，写 $r(z)=\sum_{n\ge0}r_nz^n$ 后，必有

$$
\boxed{|r_n|W_n\le\|B\|\quad(n\ge0).} \tag{2.2}
$$

**证明。** 从 (2.1) 得

$$
F(A,L)F(A,L)^*
\le\|B\|^2G(A,L)G(A,L)^*.
$$

应用 $\pi$ 后，在 $\operatorname{Ran}\pi(G(A,L))^*$ 上定义

$$
S\bigl(\pi(G(A,L))^*x\bigr)=\pi(F(A,L))^*x.
$$

正序界使其良定义且有界，范数至多 $\|B\|$。连续延伸到该值域闭包，再在正交补置零。取 $T=S^*$ 得

$$
\pi(G(A,L))T=\pi(F(A,L)),\qquad \|T\|\le\|B\|.
$$

写 $Te_0=\sum_{n\ge0}b_nW_ne_n$，则 $|b_n|W_n\le\|B\|$。两个解析算子在这个表示中下三角，其形式移位系数由 (1.3) 给出。逐坐标比较得到

$$
G(z,\ell(z))\sum_{n\ge0}b_nz^n=F(z,\ell(z)).
$$

每个坐标只涉及有限项；即使重排为单变量级数后没有范数绝对收敛，也不影响这一步。由 (1.4) 分母形式级数非零，形式 Laurent 商唯一，所以 $r=\sum b_nz^n$，并得到 (2.2)。证毕。

因此只要发现负阶，或发现一列 $|r_n|W_n\to\infty$，就排除了整个 $B(H)$ 内的有界因子，而不只排除 $\mathcal A$ 内部的商。

## 3. 非全纯分式必被有限次横向导数检出

### 引理 3.1

若 $R\in\operatorname{Frac}\mathscr O$ 但 $R\notin\mathscr O$，则存在有限整数 $q\ge0$，使

$$
(\partial_w^qR)(z,\ell(z))
$$

具有严格负阶。

**证明。** 反设所有这些形式 Laurent 级数都没有负阶。由于 $G(z,\ell(z))\ne0$，在域 $\mathbb C((z))$ 上对新变量 $t$ 作形式 Taylor 展开合法：

$$
\widetilde R(z,t)
=R(z,\ell(z)+t)
=\sum_{q\ge0}\frac{1}{q!}
(\partial_w^qR)(z,\ell(z))t^q.
$$

反设使 $\widetilde R\in\mathbb C[[z,t]]$，并且

$$
G(z,\ell(z)+t)\widetilde R(z,t)=F(z,\ell(z)+t).
$$

$\ell(0)=0$，所以替换 $t=w-\ell(z)$ 是二维形式幂级数环的合法连续自同构。施加它可得某个 $Q\in\mathbb C[[z,w]]$ 满足 $GQ=F$。

R66 §4.1 已自含证明：两个收敛解析芽之间的这种形式可除性必为收敛解析可除性。其证明使用清分母 Bézout，将约去公共因子后的分母化为 $z^N$ 的形式因子，再以 $z$ 的素性迫使剩余因子为解析单位。因此 $F/G\in\mathscr O$，与假设矛盾。证毕。

若引理给 $q=0$，引理 2.1 已经排除有界实现。以下处理 $q\ge1$：固定这样的 $q$，并写

$$
(\partial_w^qR)(z,\ell(z))
=a z^{-s}+\text{更高阶项},
\qquad a\ne0,\quad s\ge1. \tag{3.1}
$$

不要求 $q$ 是最小可能值。

## 4. 低位截断的明确解析圆与统一 Laurent 系数界

写 $R=F/G$，并固定

$$
g=\operatorname{ord}_zG(z,\ell(z)),\qquad
G(z,\ell(z))=a_gz^g+\cdots,\quad a_g\ne0.
$$

$g$ 是有限非负整数。若 $g=0$，则 $G(0,0)\ne0$，从而 $R$ 本来全纯。因此在非全纯情形可取 $g\ge1$。

令低位解析截断

$$
\ell_{<j}(z)=\sum_{i<j}\gamma_i(z^{2^i}/d_i). \tag{4.1}
$$

对于 $j\ge1$，置

$$
b_j=\frac{\Lambda_{j-1}}{2^{j-1}},\qquad
\rho_j^{\,\mathrm{out}}=\frac12e^{-b_j},
\qquad
\rho_j=(\rho_j^{\,\mathrm{out}})^2. \tag{4.2}
$$

### 4.1 外圆上所有低位函数都落入一个固定小邻域

对 $|z|\le\rho_j^{\,\mathrm{out}}$、$i<j$，由 (1.1)，

$$
\left|\frac{z^{2^i}}{d_i}\right|
\le2^{-2^i}\exp\left(\Lambda_i-2^ib_j\right)
\le2^{-2^i}\le\frac12.
$$

利用

$$
\gamma_i(t)=\int_{r_i}^{1}\frac{t}{1+ut}\,du,
$$

可得 $|\gamma_i(t)|\le2\delta_i|t|$。固定 $i$ 时，上述输入随 $j\to\infty$ 趋零，且被可和序列 $2^{-2^i}$ 控制。所以

$$
\sup_{|z|\le\rho_j^{\,\mathrm{out}}}
|\ell_{<j}(z)|\longrightarrow0. \tag{4.3}
$$

因此对充分大的 $j$，$F,G$ 及任意有限个所需偏导数都能在 $(z,\ell_{<j}(z))$ 上解析求值，并在整个外圆盘上一致有界。

### 4.2 内圆内的分母只有原点零点

记 $G_j(z)=G(z,\ell_{<j}(z))$。其范数在外圆盘上一致有界，设为 $K$。而 $\ell-\ell_{<j}$ 的形式阶为 $2^j$，故 $G_j$ 的任何固定有限阶 Taylor jet 最终都与 $G(z,\ell(z))$ 相同。

特别地，当 $2^j>2g$ 后，$G_j$ 的 $0,\ldots,2g$ 阶系数是固定的，首个非零项为 $a_gz^g$。在内圆 $|z|=\rho_j=(\rho_j^{\,\mathrm{out}})^2$ 上，外圆 Cauchy 界控制剩余尾和：

$$
\left|\sum_{n\ge2g+1}[z^n]G_j\,z^n\right|
\le K\frac{(\rho_j/\rho_j^{\,\mathrm{out}})^{2g+1}}
{1-\rho_j/\rho_j^{\,\mathrm{out}}}
=K\frac{(\rho_j^{\,\mathrm{out}})^{2g+1}}
{1-\rho_j^{\,\mathrm{out}}}.
$$

除以主项模 $|a_g|\rho_j^g=|a_g|(\rho_j^{\,\mathrm{out}})^{2g}$ 后，右边趋零。固定的 $g+1,\ldots,2g$ 阶项相对于主项也趋零。因此当 $j$ 足够大时，

$$
|G_j(z)-a_gz^g|\le\tfrac12|a_g|\rho_j^g
\quad(|z|=\rho_j). \tag{4.4}
$$

辐角原理给 $G_j$ 在内圆内恰有 $g$ 个零点；它在 $0$ 已有恰为 $g$ 的零点阶数，故内圆中没有别的零点。特别地，

$$
|G_j(z)|\ge\tfrac12|a_g|\rho_j^g
\quad(|z|=\rho_j). \tag{4.5}
$$

排除内圆内的其他零点是必要的；仅有边界下界还不足以把下面的积分当作原点 Laurent 系数。

### 4.3 固定有限次导数的 Laurent 系数界

记 $R_h=\partial_w^hR$。递推可写

$$
R_h=\frac{N_h}{G^{h+1}},
$$

其中 $N_h$ 是解析芽：$N_0=F$，且

$$
N_{h+1}=G\partial_wN_h-(h+1)N_h\partial_wG.
$$

对固定 $0\le h\le q$，(4.3) 给这些分子在外圆上一致有界。结合 (4.5)，存在与 $j$ 无关的有限 $C_h$，使内圆上

$$
|R_h(z,\ell_{<j}(z))|
\le C_h\rho_j^{-g(h+1)}.
$$

函数在内圆中仅可能于 $0$ 有极点，故对任意整数 $n$ 的 Laurent 系数，

$$
\boxed{
\left|[z^n]R_h(z,\ell_{<j}(z))\right|
\le C_h\rho_j^{-n-g(h+1)}.
} \tag{4.6}
$$

特别地，对 $0\le h\le q$、$n\le2^{j+1}$，由
$-\log\rho_j=2b_j+2\log2$ 得

$$
\begin{aligned}
\log\left|[z^n]R_h(z,\ell_{<j})\right|
&\le \log C_h+(2b_j+2\log2)(2^{j+1}+g(h+1))\\
&\le 8\Lambda_{j-1}+O_{F,G,q}(b_j+2^j+1)\\
&\le \frac35\Lambda_j
\end{aligned} \tag{4.7}
$$

对充分大的 $j$ 成立。最后一步用 $\Lambda_j\ge16\Lambda_{j-1}$，以及
$b_j/\Lambda_j\to0$、$2^j/\Lambda_j\to0$。若某个系数为零，不等式按直接模界理解。这个 $3/5$ 可由任何固定介于 $1/2$ 与 $1$ 的数替换。

## 5. 混合高位系数：一个精确主项加有限个错误项

固定 (3.1) 的 $q,s,a$。对大整数 $J$，置

$$
K=J+q-1,\qquad
N_J=\sum_{i=J}^{K}2^i=2^{K+1}-2^J,
\qquad
P_J=\sum_{i=J}^{K}\Lambda_i.
$$

将求 $r_{N_J-s}=[z^{N_J-s}]R(z,\ell(z))$ 的严格渐近式。

### 5.1 高于 $K$ 的位不贡献目标系数

对充分大的截断层，$G(z,\ell_{<j}(z))$ 的形式阶恒为 $g$。因此对所有整数 $h\ge0$，

$$
\operatorname{ord}_zR_h(z,\ell_{<j}(z))\ge-g(h+1). \tag{5.1}
$$

若一个形式增量 $\Delta(z)$ 的阶为 $D>g$，则 Taylor 展开

$$
R_h(z,\ell_{<j}+\Delta)
=\sum_{k\ge0}\frac1{k!}R_{h+k}(z,\ell_{<j})\Delta^k
$$

在 $\mathbb C((z))$ 中逐阶合法，因为第 $k$ 项的阶至少为

$$
k(D-g)-g(h+1)\longrightarrow+\infty. \tag{5.2}
$$

取 $\Delta=\ell-\ell_{<K+1}$，其阶为 $2^{K+1}$。当 $h=0$ 时，所有 $k\ge1$ 的项阶至少为 $2^{K+1}-2g$。而目标次数为 $2^{K+1}-2^J-s$。对大 $J$，$2^J+s>2g$，所以

$$
[z^{N_J-s}]R(z,\ell)
=[z^{N_J-s}]R(z,\ell_{<K+1}). \tag{5.3}
$$

### 5.2 从最高位往下，每层只剩零次与一次

对 $J\le j\le K$，令

$$
h=K-j,\qquad
n_j=\sum_{i=J}^{j}2^i-s=2^{j+1}-2^J-s.
$$

使用

$$
\ell_{<j+1}=\ell_{<j}+
\gamma_j(z^{2^j}/d_j),
$$

在 (5.2) 中取 $D=2^j$。任何至少二次 Taylor 项的阶至少为

$$
2\cdot2^j-g(h+3).
$$

只要 $2^J+s>g(q+3)$，它就严格大于 $n_j$，所以这些项不影响目标系数。

一次 Taylor 项中，

$$
\gamma_j(z^{2^j}/d_j)
=\frac{\delta_j}{d_j}z^{2^j}
+\text{阶至少 }2^{j+1}\text{ 的项}.
$$

后面的高阶项与 $R_{h+1}$ 相乘，其阶也大于 $n_j$。于是得到**精确**递推：

$$
\begin{aligned}
[z^{n_j}]R_h(z,\ell_{<j+1})
&=[z^{n_j}]R_h(z,\ell_{<j})\\
&\quad+\frac{\delta_j}{d_j}
[z^{n_j-2^j}]R_{h+1}(z,\ell_{<j}).
\end{aligned} \tag{5.4}
$$

连续选择一次分支，直到最低选定位 $J$，给出

$$
r_{N_J-s}
=a\prod_{i=J}^{K}\frac{\delta_i}{d_i}
+\sum_{j=J}^{K}E_{J,j}, \tag{5.5}
$$

其中

$$
E_{J,j}
=\left(\prod_{i=j+1}^{K}\frac{\delta_i}{d_i}\right)
[z^{n_j}]R_{K-j}(z,\ell_{<j}). \tag{5.6}
$$

这里主项末端的系数确实等于固定 $a$：$\ell-\ell_{<J}$ 的阶为 $2^J$，由 (5.2) 对 $h=q$ 得两次求值之差的阶至少为 $2^J-g(q+2)>-s$；所以

$$
[z^{-s}]R_q(z,\ell_{<J})
=[z^{-s}]R_q(z,\ell)=a.
$$

(5.5) 已包含所有高位与低位贡献，没有遗漏同一 dyadic 位的高次项：它们在目标次数上被 (5.2) 的严格形式阶界排除了。

### 5.3 错误项全部比主项小

主项为

$$
M_J=a\,e^{P_J}\prod_{i=J}^{K}\delta_i.
$$

由 (4.7)，每个错误项满足

$$
|E_{J,j}|
\le\left(\prod_{i=j+1}^{K}\delta_i e^{\Lambda_i}\right)
e^{(3/5)\Lambda_j}.
$$

因为 $q$ 固定而 $\delta_i\asymp J^{-2}$，

$$
\frac{|E_{J,j}|}{|M_J|}
\le C_{q,a}J^{2q}
\exp\left(\frac35\Lambda_j-\sum_{i=J}^{j}\Lambda_i\right)
\le C_{q,a}J^{2q}e^{-(2/5)\Lambda_J}.
$$

错误项只有 $q$ 个，所以 (5.5) 给

$$
\boxed{
r_{N_J-s}
=a\,e^{P_J}\prod_{i=J}^{K}\delta_i\,(1+o(1)).
} \tag{5.7}
$$

### 5.4 真实带权系数发散

$N_J$ 的二进制展开在 $J,\ldots,K$ 恰取 $1$。R13 的无进位范数乘法给

$$
W_{N_J}=\prod_{i=J}^{K}d_i=e^{-P_J}.
$$

对大 $J$，固定 $s<2^J$；且 $v_2(N_J)=J$、$v_2(N_J-t)=v_2(t)$ 对 $1\le t<s$ 成立。因此

$$
W_{N_J-s}=\frac{e^{-P_J}}{a_JW_{s-1}}.
$$

与 (5.7) 相乘，得到本条的核心渐近式：

$$
\boxed{
r_{N_J-s}W_{N_J-s}
=\frac{a}{a_JW_{s-1}}
\prod_{i=J}^{J+q-1}\delta_i\,(1+o(1)).
} \tag{5.8}
$$

右边模趋于无穷，因为 $a\ne0$、$W_{s-1}>0$ 固定，分子中的有限乘积仅按 $J^{-2q}$ 衰减，而 $a_J$ 超快趋零。

## 6. 有界性忠实定理

**定理 6.1。** 对任意 $R=F/G\in\operatorname{Frac}\mathscr O$，$G\ne0$，最大闭实现 $T_R$ 有界，当且仅当 $R\in\mathscr O$。有界时它恰为范数解析演算 $R(A,L)$。

**证明。** 若 $R$ 全纯，则 $F=GR$ 是解析芽恒等式。解析演算给

$$
F(A,L)=G(A,L)R(A,L).
$$

$G(A,L)$ 单射，所以最大图对每个 $u\in H$ 的唯一输出是 $R(A,L)u$；因此 $T_R$ 处处定义且有界。

反之，若最大闭实现有界，则其定义域必须为全 $H$：它稠密定义，受统一范数控制的连续延伸与图闭性迫使每个 $H$ 向量属于定义域。于是存在 $B\in B(H)$ 满足 (2.1)。

若 $R$ 非全纯，引理 3.1 给有限 $q$。$q=0$ 时形式负阶直接违背引理 2.1；$q\ge1$ 时 (5.8) 的带权系数发散违背 (2.2)。两种情况都矛盾。因此 $R$ 全纯。证毕。

特别地，若 $F(A,L)=G(A,L)B$ 且 $B$ 是任意有界算子，则

$$
B=(F/G)(A,L)\in\mathcal A.
$$

这里既未预设 $B\in\mathcal A$，也未预设它属于具体 UHF 代数；这些结论由真实有界性强迫出来。

### 6.1 与先前系数结论的相容性检验

这些是对通用公式的符号代入，不承担上述证明。

- 对 $R=w/z$，取 $q=1$，$\partial_wR=1/z$，于是 $s=1,a=1$；(5.8) 恢复 $L$ 不可有界除以 $A$。
- 对 $R=z/w$，$\ell(z)=c_1z+\cdots$，取 $q=1$ 得 $s=1,a=-c_1^{-2}$；恢复 R49 的 $m=1$ 反向障碍。
- 对 $R=z^m/w$，取 $q=m$，得到 $s=1,a=(-1)^mm!c_1^{-m-1}$；恢复 R49 的多高位主项。
- 对 $R=z^m/(w-c_1z)$，分母沿形式曲线首阶为 $2$。当 $m=1$ 时已有负阶；其余取 $q=\lceil m/2\rceil$，所得 $s=2(q+1)-m$ 与 R65 首阶抵消分支一致。

## 7. 全部分式最大闭实现的谱三分

以下设 $R$ 非恒定。因此每个 $R-\lambda$ 都是非零分式。

R62 与 R66 的最大图框架给

$$
\ker(T_R-\lambda)=0,\qquad
\overline{\operatorname{Ran}(T_R-\lambda)}=H
\quad(\lambda\in\mathbb C). \tag{7.1}
$$

具体地，若 $R=F/G$，则

$$
T_R-\lambda=T_{(F-\lambda G)/G},
$$

等号含定义域：$Fu\in\operatorname{Ran}G(A,L)$ 当且仅当
$(F(A,L)-\lambda G(A,L))u$ 属于这个值域。交换图坐标又给

$$
(T_R-\lambda)^{-1}=T_{1/(R-\lambda)}.
$$

因此由定理 6.1，

$$
\boxed{
\lambda\in\rho(T_R)
\iff \frac1{R-\lambda}\in\mathscr O.
} \tag{7.2}
$$

### 7.1 $R$ 全纯且非恒定

此时 $1/(R-\lambda)$ 全纯当且仅当 $\lambda\ne R(0,0)$。所以

$$
\sigma(T_R)=\{R(0,0)\}.
$$

由 (7.1)，唯一谱点为连续谱点。

### 7.2 $R$ 非全纯，但 $1/R$ 全纯

写 $H=1/R\in\mathscr O$。必有 $H(0,0)=0$；否则 $H$ 是解析单位，$R=1/H$ 也全纯。对任意 $\lambda$，

$$
\frac1{R-\lambda}=\frac{H}{1-\lambda H}\in\mathscr O.
$$

故 $\rho(T_R)=\mathbb C$、$\sigma(T_R)=\varnothing$。这是闭无界算子允许的空谱，不是有界算子。

### 7.3 $R$ 与 $1/R$ 都非全纯

若存在某个 $\lambda$ 使 $H=1/(R-\lambda)$ 全纯，则 $H(0,0)$ 不能非零，否则 $R=\lambda+1/H$ 全纯。于是 $H(0,0)=0$，而

$$
\frac1R=\frac{H}{1+\lambda H}\in\mathscr O,
$$

再次矛盾。所以没有任何预解点。结合 (7.1)，

$$
\sigma(T_R)=\sigma_c(T_R)=\mathbb C.
$$

三种情形穷尽全部非恒定分式。恒定 $R=c$ 时，最大实现为 $cI$，谱为单点 $\{c\}$，该点是特征值。

### 7.4 具体例子

$$
\begin{array}{c|c}
R & \sigma(T_R)\\ \hline
w & \{0\}\ \text{（连续谱）}\\
1/z & \varnothing\\
1/w & \varnothing\\
w/z & \mathbb C\ \text{（全部连续谱）}\\
z/w & \mathbb C\ \text{（全部连续谱）}\\
(1+w)/z & \varnothing
\end{array}
$$

$w/z$ 与 $z/w$ 正好恢复 R65 的两个实际比值。

## 8. 范围

本条完整分类的是由两个指定实际算子 $A,L$ 的**有限变量收敛解析芽分式**产生的闭算子。R62 已证明解析芽算子值在 $\mathcal A$ 中稠密却为第一纲真子集，所以这里的有界性忠实及谱三分不能自动推广到任意 $X,Y\in\mathcal A$，也不证明每个非零 $H$ 向量循环。

同样，没有把全平面谱或空谱当作有界 $A$ 的不变子空间存在或不存在的结论。新的无条件内容是：非全纯分式必产生真实无界最大实现，且所有这类分式实现的谱已由 (7.2) 完整决定。
