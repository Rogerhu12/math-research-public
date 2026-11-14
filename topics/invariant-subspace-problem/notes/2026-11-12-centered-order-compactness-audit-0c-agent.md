# Centered 原文、正半交换子族与 Haar 表示中的紧化障碍

日期：2026-11-12。会话：0c0170654df7，独占代理 literature。拟登记 R107；编号由母会话最终决定。

**状态。** §§2、4–8 给出完整的模型内证明。§§1、3 是已取得原文的精确适用性审计。这些结论没有证明 $A$ 存在或不存在普通非平凡闭不变子空间。特别不能把 centered 的结构表示、不可约性或 Banach 格的闭理想结论等同于普通 Hilbert 空间 ISP。

本轮发现一处需要纠正的引用：2026 年预印本 [4] 引言把一般 centered 算子的不变子空间归因于 Morrel–Muhly 模型；但其所引原论文 [1] 第 262 页 §6.2 正将这个问题留下。本文不由此推断 1974 年以后不存在其他适用定理，只说明这条具体引用不能承担无条件结论。

## 1. 已实际取得的原文与编号

以下日期是版本页眉或出版信息；不以搜索引擎的抓取日期代替发表日期。所有本地第三方 PDF 和图像仅在临时目录，不进入仓库。

| 来源 | 已核正文位置 | 精确用途 |
|---|---|---|
| [1] Morrel–Muhly, *Centered operators*, Studia Math. 51 (1974), 251–263 | Theorem III，p.258；Theorem V，p.261；§6.2，p.262 | type IV 表示；不可约性；作者明确留下的普通不变子空间问题 |
| [2] Budzyński, arXiv:2510.19768v1，2025-10-22 | §5，Theorem 21 / Proposition 22，p.12；Theorem 27，p.14 | 弱 centered 加 hyponormal 次序条件 |
| [3] Budzyński, arXiv:2603.03594v2，2026-04-17 | §4，Proposition 11，p.11 | 单射且稠密像的有界加权复合算子是 type IV |
| [4] Budzyński, arXiv:2606.24550v1，2026-06-23 | 引言 p.1；§3，Proposition 2，p.7 | 新的幂相位谱次序判据及其实际附加假设 |
| [5] Anisca–Troitsky, Indiana Univ. Math. J. 54 (2005), 861–872 | 作者版本 Definition 2，p.2；Theorem 8，p.4；Corollary 13，p.8；Theorem 17，p.10；随后 $L^p$ 讨论，p.11 | 正算子族的条件 $(*)$；$C_0$ 与 $L^p$ 的差别 |
| [6] Flores–Tradacete–Troitsky, J. Math. Anal. Appl. 343 (2008), 743–751 | 作者版本 Theorem 3.8，pp.9–10；Theorem 3.10，p.10 | 正半交换子支配 AM-compact 算子的充分条件 |
| [7] Chalendar–Flattot–Partington, *The Method of Minimal Vectors Applied to Weighted Composition Operators* | 作者版本 Theorem 3.2，p.6；Corollary 4.4，pp.11–12；§4.4，pp.16–17 | 轨道严格比值判据及其遍历情形限制 |

### 1.1 Morrel–Muhly 原文实际说了什么

[1] 的 Theorem III 把 type IV 的固定谱重数部分表示成

$$
\Theta S M_{\Gamma(P)}.
$$

这里 $S$ 是带 Radon–Nikodym 因子的酉复合算子，$\Theta$ 是可分解酉算子。Theorem V 判断的是 reducing subspace 意义下的不可约性，条件为底空间测度遍历以及相应 cocycle 不可约。

原文 §6.2 先说明 hyponormal centered 的已知结果，然后提出：

> Which centered operators have proper invariant subspaces?

同页校样补注只报告 Davie 已处理一大类 Bishop 算子。故不能将该论文改述成“所有 centered 算子已知有普通不变子空间”。[4] p.1 的无条件概括不由这一引用得到支持。[3] p.1 对 type IV 为加权平移的描述与 [1] 的 Theorem III 一致。

### 1.2 合法获取位置

[1] [出版社记录](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/51/3/100346/centered-operators)明确标注 CC-BY 免费下载。正常 HTTP 下载跳转到 [ICM 原始扫描](https://matwbn.icm.edu.pl/ksiazki/sm/sm51/sm51122.pdf)。本地文件为 /tmp/isp_centered_sources/morrel-muhly-1974.pdf，共 7 张双页，2,871,364 bytes；关键原图为同目录 mm1974-page-5.png、mm1974-page-6.png、mm1974-last.png。

大学课程资料 CoifmanFefferman.pdf 只有该论文的第一页，不能把它当作全文。本轮的结论使用的是上面的完整期刊扫描。

[2]–[4] 原始 arXiv PDF 分别为 [2510.19768v1](https://arxiv.org/pdf/2510.19768v1)、[2603.03594v2](https://arxiv.org/pdf/2603.03594v2)、[2606.24550v1](https://arxiv.org/pdf/2606.24550v1)，本地名称分别是 /tmp/isp_centered_sources/budzynski-weak-2025.pdf、budzynski-centered-2026.pdf、budzynski-spectral-2026.pdf。

## 2. 当前算子恰是原模型的标量 type IV

沿用 R9 的实际算子

$$
H=L^2(\mathbb Z_2,\mu),\qquad
(Af)(y)=w(y)f(y-1),\qquad
w(y)=a_{v_2(y)},\quad w(0)=0,
$$

其中 $\mu$ 是 Haar 概率测度，$a_0>a_1>\cdots>0$ 且 $a_j\to0$。令

$$
(Uf)(y)=f(y-1),\qquad P=M_{w(\cdot+1)}.
$$

于是 $A=UP$，$U$ 酉，$P$ 单射且稠密像。注意在本文中，“正算子”若涉及半交换子或支配，均指 Banach 格意义的保正算子；不是仅指 Hilbert 空间自伴正半定算子。

**命题 2.1。** 记 [1] 使用的模的平移代数为

$$
\mathcal P_A=C^*(I,U^nPU^{-n}:n\in\mathbb Z).
$$

则

$$
\mathcal P_A=\{M_f:f\in C(\mathbb Z_2)\},\qquad
\mathcal P_A''=\{M_f:f\in L^\infty(\mu)\}.
$$

**证明。** 每个生成元都是连续函数的乘法算子，故第一式的左侧包含于右侧。对于 $m\ge1$，在

$$
\sigma(P)=\{0,a_0,a_1,\ldots\}
$$

上取一个连续函数，在 $\{0,a_m,a_{m+1},\ldots\}$ 上为 $1$，在其余有限个谱点上为 $0$。连续函数演算给出

$$
M_{\mathbf1_{-1+2^m\mathbb Z_2}}\in C^*(I,P).
$$

再用 $U$ 的整数平移，得到每个模 $2^m$ 柱集的指标乘法算子。局部常数函数在 $C(\mathbb Z_2)$ 中一致稠密，证明第一式。柱集生成 Borel $\sigma$-代数，其指标乘法算子的强闭包为全部 $L^\infty$ 乘法算子，证明第二式。$\square$

因此 [1] Theorem III 在这里可以直接取

$$
X=\mathbb Z_2,\quad \mu=\text{Haar},\quad
\mathcal E=\mathbb C,\quad S=U,\quad\Theta=I.
$$

谱重数为 $1$，且 odometer 遍历。这里不存在另一个隐藏的有限维纤维分解可从该模型自动提取普通不变子空间。R105 的 diffuse/atomic MASA 区分仍然必要：上述 $\Theta=I$ 是 diffuse 表示中的事实，不允许删除 PPP 的 atomic permutation 表示中的另一个酉因子。

## 3. 三篇 Budzyński 原文的实际附加假设

[2] Proposition 22 要求

$$
E_{\phi,w}(h_{\phi,w})=h_{\phi,w},\qquad
h_{\phi,w}\circ\phi\le h_{\phi,w}\quad\mu_w\text{-a.e.}
$$

Theorem 27 的相应无界版本保留这些条件。这里 $\phi(y)=y-1$ 可逆，所以第一个条件成立；第二个条件的失败已在旧 centered 文献笔记算出。

[3] Proposition 11 是 type IV 分类结论，没有从该命题额外得到普通不变子空间。

[4] Proposition 2 固定 $n\ge1$，令 $V_n$ 是 $T^n$ 的极分解相位，

$$
B=T^*T,\qquad C_n=V_nBV_n^*.
$$

它要求 $B$ 与 $|T^n|,C_n$ 交换，并要求

$$
B\ge C_n.
\tag{3.1}
$$

结论是一个由 $B$ 的谱子空间生成的有限轨道和对 $T$ 不变；命题本身不保证该和非零且真。原文 Example 1，p.6，明确展示有限轨道和可能等于全空间。不能只核对 centeredness 后删去 (3.1)，也不能把“某闭子空间不变”偷换成“得到真不变子空间”。

## 4. 所有正整数幂都不满足该谱次序判据

**定理 4.1。** 对任意 $s,n\ge1$，把 [4] Proposition 2 应用于 $T=A^s$ 时，其交换性条件成立，但 $B-C_n$ 同时有正、负方向。特别 (3.1) 和反向次序都不成立。

**证明。** 由真实加权复合公式，

$$
(A^s f)(y)=w_s(y)f(y-s),\qquad
w_s(y)=\prod_{j=0}^{s-1}w(y-j).
$$

$w_s$ 是连续函数，恰在 $\{0,\ldots,s-1\}$ 上为零，故几乎处处为正。于是 $A^s$ 的极分解相位为 $U^s$，而

$$
|A^s|^2=M_{h_s},\qquad
h_s(y)=\prod_{r=1}^s w(y+r)^2.
$$

同理 $V_n=U^{sn}$，所以

$$
B-C_n=M_{h_s(y)-h_s(y-sn)}.
\tag{4.1}
$$

所有待交换的算子都是乘法算子。另一方面，

$$
h_s(-s)=0,\qquad h_s(-s-sn)>0:
$$

后一个乘积中的参数全部是非零负整数。故 (4.1) 的乘子在 $y=-s$ 严格负。取 $y=sn-1$ 时，

$$
h_s(sn-1)>0,\qquad h_s(-1)=0,
$$

故乘子严格正。连续性和 Haar 测度满支集把这两个严格不等式扩展成正测度开集；在相应集合上取非零支持向量，即得到正、负二次型方向。$\square$

当 $s=1$、$r=v_2(n)$ 时还有显式下界。在

$$
D_-=-1+2^{r+1}\mathbb Z_2,\qquad
D_+=n-1+2^{r+1}\mathbb Z_2
$$

上，分别有

$$
h_1(y)-h_1(y-n)
\le -(a_r^2-a_{r+1}^2),\qquad
h_1(y)-h_1(y-n)
\ge a_r^2-a_{r+1}^2.
$$

两集测度都是 $2^{-r-1}$。因此这一失败不依赖测度零的特殊点。

更一般地，在保测概率空间上，若有界实函数 $h$ 满足 $h\circ\phi\le h$，则积分相等迫使两者几乎处处相等；若 $\phi$ 遍历，则 $h$ 常数。这个简单事实解释了 [2] 的 hyponormal 判据在非恒定 Haar 权上的限制；但偶数平移未必遍历，所以定理 4.1 使用的是实际零点与连续性，并未错误假定 odometer 的每个幂遍历。

## 5. 正的左、右半交换子有统一的真实高位角估计

设 $\mathcal S_-$ 和 $\mathcal S_+$ 分别是

$$
\mathcal S_-=\{B\ge0:BA\le AB\},\qquad
\mathcal S_+=\{B\ge0:BA\ge AB\}.
$$

这里所有不等号都是 Banach 格的算子次序。它们比正交换子集合更大。

采用已证明的真实进位恒等式

$$
N_j=\frac{A^{2^j}}{\|A^{2^j}\|}
=E_j+\eta_jE_j^*N_{j+1},
\qquad \|N_{j+1}\|=1,\quad \eta_j\longrightarrow0.
\tag{5.1}
$$

$E_j=e_{10}$ 只作用在第 $j$ 个物理位；$N_{j+1}$ 作用于更高位，并与该位的矩阵单位交换。所有式 (5.1) 中的算子都保正。令 $P_j^0=E_j^*E_j$、$P_j^1=E_jE_j^*$。

**引理 5.1。** 对每个 $B\in\mathcal S_-\cup\mathcal S_+$，

$$
\|P_j^0BP_j^1\|\le\eta_j\|B\|.
\tag{5.2}
$$

**证明。** 按第 $j$ 位的 $0,1$ 顺序写矩阵，

$$
N_j=
\begin{pmatrix}
0&\eta_jN_{j+1}\\
I&0
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
B_{00}&B_{01}\\
B_{10}&B_{11}
\end{pmatrix}.
$$

$B$ 保正意味着其四个角都是相应 $L^2$ 空间之间的保正算子。若 $BA\le AB$，保正性归纳给 $BA^k\le A^kB$，故 $BN_j\le N_jB$。比较 $00$ 角，

$$
0\le B_{01}\le \eta_jN_{j+1}B_{10}.
$$

若 $BA\ge AB$，同理 $BN_j\ge N_jB$；比较 $11$ 角，

$$
0\le B_{01}\le \eta_jB_{10}N_{j+1}.
$$

保正算子的范数对该次序单调，而 $\|B_{10}\|\le\|B\|$，故两种情形均得到 (5.2)。$\square$

**推论 5.2。** 对有限位集 $J$ 及其全零事件的指标投影

$$
P_J=\prod_{j\in J}P_j^0,
$$

有

$$
\|P_JB(I-P_J)\|
\le \|B\|\sum_{j\in J}\eta_j.
\tag{5.3}
$$

**证明。** 将 $J$ 排序为 $j_1,\ldots,j_\ell$，写

$$
I-P_J=\sum_{\nu=1}^{\ell}Q_\nu,\qquad
Q_\nu=\left(\prod_{\kappa<\nu}P_{j_\kappa}^0\right)P_{j_\nu}^1.
$$

这些正交投影的和恰为 $I-P_J$，并且 $P_J\le P_{j_\nu}^0$、$Q_\nu\le P_{j_\nu}^1$。故

$$
P_JBQ_\nu=P_J(P_{j_\nu}^0BP_{j_\nu}^1)Q_\nu,
$$

逐项用 (5.2) 后求和即可。$\square$

## 6. 全部一致有界正半交换子族都不满足 AT 条件 $(*)$

[5] Definition 2 的条件 $(*)$ 要求存在 $x_0\ge0$ 和 $0<r<\|x_0\|$，使每个序列

$$
x_m\in B(x_0,r)\cap[0,x_0]
$$

都能选出子列和族内算子 $B_m$，令 $B_mx_m$ 范数收敛到非零向量。[5] Corollary 13 对正的左半交换子中的全部收缩算子使用这个条件。

**定理 6.1。** 对任意有限 $C$，集合

$$
\mathcal F_C=
\{B\in\mathcal S_-\cup\mathcal S_+:\|B\|\le C\}
$$

不满足 $(*)$。更精确地，对每个上述球，都存在其中的序列 $x_m$，使任意子列及任意选择 $B_m\in\mathcal F_C$ 的范数收敛像只能收敛到零。

**证明。** 取整数 $\ell\ge1$，使

$$
p=2^{-\ell}<\frac{r^2}{\|x_0\|^2}.
$$

取位集 $J_m$，每个含 $\ell$ 个连续高位，且 $\min J_m\to\infty$；例如可令这些位块互不相交。记全零事件投影为 $P_m=P_{J_m}$。公平乘积测度给

$$
P_m\longrightarrow pI\quad\text{于 WOT}.
\tag{6.1}
$$

具体地，对任意依赖有限低位的 $L^1$ 函数 $h$，充分大的 $m$ 满足 $\int P_mh=p\int h$。用柱函数在 $L^1$ 中的稠密性及 $\|P_m\|_\infty\le1$，对一般 $h\in L^1$ 得到同一极限；取 $h=f\overline g$ 即为 (6.1)。

令

$$
x_m=(I-P_m)x_0.
$$

则 $0\le x_m\le x_0$，且

$$
\|x_0-x_m\|^2=\langle P_mx_0,x_0\rangle
\longrightarrow p\|x_0\|^2<r^2.
$$

去掉有限个初项后，整个序列在所需球内。推论 5.2 给出对任意 $B_m\in\mathcal F_C$ 的一致估计

$$
\|P_mB_mx_m\|
\le C\|x_0\|\sum_{j\in J_m}\eta_j
\longrightarrow0.
\tag{6.2}
$$

若某子列的 $B_mx_m$ 范数收敛到 $g$，则

$$
\|P_mg\|
\le\|g-B_mx_m\|+\|P_mB_mx_m\|\longrightarrow0.
$$

另一方面，(6.1) 应用于 $|g|^2$ 给

$$
\|P_mg\|^2\longrightarrow p\|g\|^2.
$$

于是 $g=0$。同一证明对任何子列成立，完成反证。$\square$

这里明确排除了 [5] Corollary 13 的整个正收缩算子族假设；结论不只是“尚未找到合适的算子”。对比 [5] p.11 的 $L^p$ 讨论，其独立事件构造针对加权复合算子的支配族；本定理额外使用真实的进位恒等式，处理全部左、右半交换子，不要求它们本身是加权复合算子。

### 6.1 同时明确排除 Theorem 8 的全部支配族

对每个 $s\ge1$，设

$$
\mathcal D_s=\{K\in B(H):|Kf|\le A^s|f|\ \text{对所有 }f\in H\}.
$$

这正是 [5] Theorem 8 涉及的那类支配族，而不只包含正算子。

**命题 6.2。** 每个 $\mathcal D_s$ 都不满足 $(*)$。

**证明。** 写 $A^s=M_{w_s}U^s$。对 $K\in\mathcal D_s$，令 $D=KU^{-s}$，则

$$
|Df|\le w_s|f|.
$$

因此 $D$ 保持每个可测支持子空间，进而与每个指标乘法算子交换。令 $b=D1$，先对简单函数、再由 $L^2$ 稠密性得到 $D=M_b$，且 $|b|\le w_s$。故 $K=M_bU^s$。

对任意球，取定理 6.1 的同一序列 $x_m=(I-P_m)x_0$。任何 $K_m\in\mathcal D_s$ 的像都在平移事件 $D_m+s$ 上为零，其中 $D_m$ 是 $P_m$ 对应的全零事件。记其指标投影为 $\widetilde P_m=U^sP_mU^{-s}$，则 $\widetilde P_m\to pI$ 于 WOT。若 $K_mx_m\to g$ 于范数，

$$
\|\widetilde P_mg\|\le\|g-K_mx_m\|\to0,
$$

而其平方趋于 $p\|g\|^2$。故 $g=0$，对子列同样成立。$\square$

## 7. 任意正半交换子都不能支配非零 AM-compact 算子

算子 $K$ 称为 AM-compact，是指它把每个序区间映成范数相对紧集。该条件比紧性弱。

**定理 7.1。** 设 $B\in\mathcal S_-\cup\mathcal S_+$。若 AM-compact 算子 $K$ 满足

$$
|Kf|\le B|f|\qquad(f\in H),
\tag{7.1}
$$

则 $K=0$。$K$ 不必保正。

**证明。** 由支配和 (5.2)，

$$
\|P_j^0KP_j^1\|\le\eta_j\|B\|.
\tag{7.2}
$$

固定 $f\ge0$。序列 $P_j^1f$ 属于序区间 $[0,f]$，且弱收敛到 $f/2$。AM-compact 性给出 $KP_j^1f$ 范数相对紧；其弱极限是 $Kf/2$，所以整个序列范数收敛到 $Kf/2$。

于是 (7.2) 给

$$
\|P_j^0Kf\|
\le2\|KP_j^1f-Kf/2\|+2\eta_j\|B\|\|f\|
\longrightarrow0.
$$

但公平乘积测度给

$$
\|P_j^0Kf\|^2\longrightarrow\frac12\|Kf\|^2.
$$

故 $Kf=0$。正函数的复线性张成是 $H$，所以 $K=0$。$\square$

因此 [6] Theorem 3.10 中“存在正右半交换子 $S$ 支配非零 AM-compact 算子”的条件在当前模型中严格不可能成立。这个结果把 R20 中对正交换子、正紧支配的结论扩大到两侧正半交换子、任意受支配的 AM-compact 算子。

## 8. $C(\mathbb Z_2)$ 不变闭理想为何不产生 Haar 闭子空间

[5] Theorem 17 确实适用于连续函数空间上的正拟幂零加权复合算子。这里 $A$ 同时作用于 $C(\mathbb Z_2)$，并且每个幂的 $C$ 算子范数与 $L^2$ 算子范数相同：连续乘子的上确界等于 Haar 本质上确界。因此 $A|_{C(\mathbb Z_2)}$ 也拟幂零。必须检查所得闭理想在 $L^2$ 中的闭包。

**定理 8.1。** $C(\mathbb Z_2)$ 中所有非零真闭理想里，对 $A$ 不变的恰为

$$
I_n=\{f\in C(\mathbb Z_2):f(0)=f(1)=\cdots=f(n)=0\},
\qquad n=0,1,2,\ldots.
\tag{8.1}
$$

每个 $I_n$ 在 Haar $L^2$ 中均稠密。

**证明。** 先回顾闭理想的一个自含事实。若 $I\subset C(X)$ 是闭理想，令 $F$ 为其公共零点集，则 $I=I(F)$。确实，对 $f|_F=0$ 和 $\varepsilon>0$，紧集 $\{|f|\ge\varepsilon\}$ 可以由有限多个 $g_i\in I$ 的非零集覆盖。令 $h=\sum_i|g_i|^2\in I$，则

$$
f\frac{h}{h+1/k}\in I
$$

在该紧集上一致趋于 $f$，而其余部分误差至多 $\varepsilon$。先令 $k\to\infty$，再令 $\varepsilon\to0$，得 $f\in I$。

对本题的非空真闭集 $F$，$I(F)$ 为 $A$ 不变，当且仅当

$$
y\in F\setminus\{0\}\quad\Longrightarrow\quad y-1\in F.
\tag{8.2}
$$

充分性由 $w(0)=0$ 直接得到。必要性：若 $y\in F\setminus\{0\}$ 且 $y-1\notin F$，可以选择在 $F$ 上为零、在 $y-1$ 不为零的连续函数 $f$；此时 $(Af)(y)\ne0$，矛盾。

若 $F$ 含有一个不属于嵌入的非负整数集 $\mathbb N_0$ 的点 $y$，那么它的后退轨道永远不会碰到 $0$。式 (8.2) 迫使整个 $\{y-k:k\ge0\}$ 属于 $F$。该轨道在每个模 $2^m$ 商中遍历全部余类，所以在 $\mathbb Z_2$ 中稠密，违背 $F\ne\mathbb Z_2$。故 $F\subset\mathbb N_0$。

如果 $F$ 无限，则它含有任意大的普通非负整数。式 (8.2) 于是迫使全部 $\mathbb N_0\subset F$，再次由稠密性矛盾。因此 $F$ 有限，(8.2) 恰给 $F=\{0,\ldots,n\}$。反向验证显然，证明 (8.1)。

最后，对 $F=\{0,\ldots,n\}$，令 $O_m$ 为这些点所在的模 $2^m$ 柱集之并，则 $O_m$ 是 clopen，且

$$
\mu(O_m)\le(n+1)2^{-m}\longrightarrow0.
$$

对任意连续 $f$，函数 $f\mathbf1_{O_m^c}\in I_n$ 且在 $L^2$ 中趋于 $f$。连续函数在 $H$ 中稠密，所以 $\overline{I_n}^{\,H}=H$。$\square$

这只分类连续函数空间中的闭理想，没有分类其所有不变闭线性子空间。它精确说明为什么此处的 $C_0$ 不变理想定理本身不能完成 Haar Hilbert 空间的任务。

## 9. 轨道严格比值判据的直接失败

[7] 的关系使用

$$
t\prec r\quad\Longleftrightarrow\quad
\limsup_{n\to\infty}
\frac{h(\gamma^n(t))}{h(\gamma^n(r))}<1.
\tag{9.1}
$$

Theorem 3.2 还要求左右正则性及几乎处处可比较性；Corollary 4.4 另要求一个吸引不动点及一致收敛的迭代。原文 §4.4 已指出其遍历情形不能如此应用。这里不把该文区间/圆盘上的微分假设直接搬到 $\mathbb Z_2$；仅检查欲移植的比值机制本身。

取 $h=w^2$、$\gamma(y)=y-1$。去掉普通整数的可数轨道后，所有分母均为正。对任意剩余的 $t$，$\gamma^n(t)$ 在无穷多个 $n$ 上为奇数；这些时刻

$$
h(\gamma^n(t))=a_0^2,\qquad
0<h(\gamma^n(r))\le a_0^2.
$$

故 (9.1) 左侧的 limsup 至少为 $1$，严格关系为空。把 $h$ 换成 $w(\cdot+1)^2$ 结论相同。这里连几乎处处可比较性都不成立。更强的实际 minimal-image 无范数收敛子列结论见 R14，不在此重复证明。

## 10. 适用范围与仍未完成的部分

当前已经严格排除：三篇新 centered 文献中已核的具体谱次序入口、AT 的支配族及正半交换子族 $(*)$ 条件、正半交换子支配非零 AM-compact 算子的入口，以及把连续函数不变理想直接闭包到 Haar $L^2$ 的做法。

没有排除全部不变子空间方法，也没有把这些排除结论组合成“$A$ 无普通不变子空间”。JKP 2019 的完整附加条件仍未取得，状态沿用 R105，不因其摘要提到 weak centered 就补写条件。普通 ISP 的主缺口仍须以一般非零 $L^2$ 向量的轨道/矩分析解决，或者找到一个确实适用、假设完整核对的一手定理。

## 参考资料

1. B. B. Morrel, P. S. Muhly, *Centered operators*, Studia Mathematica 51 (1974), 251–263，DOI [10.4064/sm-51-3-251-263](https://doi.org/10.4064/sm-51-3-251-263)。完整扫描与位置见 §1.2。
2. P. Budzyński, *Weakly centered weighted composition operators in $L^2$-spaces*, [arXiv:2510.19768v1](https://arxiv.org/abs/2510.19768v1)。
3. P. Budzyński, *Centered weighted composition operators on $L^2$-spaces revisited*, [arXiv:2603.03594v2](https://arxiv.org/abs/2603.03594v2)。
4. P. Budzyński, *Spectrally $n$-centered operators. I*, [arXiv:2606.24550v1](https://arxiv.org/abs/2606.24550v1)。
5. R. Anisca, V. G. Troitsky, *Minimal vectors of positive operators*, Indiana University Mathematics Journal 54(3) (2005), 861–872；[作者全文](https://www.math.ualberta.ca/~vtroitsky/papers/math/done/min_vec_positive/min_vec_positive-dated.pdf)，版本日期 2005-08-13；[期刊记录](https://iumj.org/article/767/)。
6. J. Flores, P. Tradacete, V. G. Troitsky, *Invariant subspaces of positive strictly singular operators on Banach lattices*, J. Math. Anal. Appl. 343(2) (2008), 743–751，DOI [10.1016/j.jmaa.2008.01.067](https://doi.org/10.1016/j.jmaa.2008.01.067)；[作者全文](https://www.icmat.es/miembros/ptradacete/assets/images/portfolio/2008jmaa.pdf)。
7. I. Chalendar, A. Flattot, J. R. Partington, *The Method of Minimal Vectors Applied to Weighted Composition Operators*, in *The Extended Field of Operator Theory*, Operator Theory: Advances and Applications 171 (2007), 89–105，DOI [10.1007/978-3-7643-7980-3_5](https://doi.org/10.1007/978-3-7643-7980-3_5)；[作者公开全文记录](https://www.researchgate.net/publication/227192023_The_Method_of_Minimal_Vectors_Applied_to_Weighted_Composition_Operators)。本文页码明确使用该处 18 页作者稿；不把 ResearchGate 的错误“1970”元数据当发表年。
