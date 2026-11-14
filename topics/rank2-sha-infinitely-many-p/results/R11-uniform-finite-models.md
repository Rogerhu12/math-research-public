# R11：统一分裂域和有理不变点的精确界限

**可信度：以下三个命题及其推论已证明。** 它们检查两种跨素数构造：以一个固定有限扩张统一平凡化 torsor，以及从全部代数点构造统一的有理向量空间。没有建立所需的新 Selmer 比较，也没有完成主目标。

设 $E/K$ 为数域上的椭圆曲线。使用 R1 的有限层结论：对每个正整数 $n$，$\Sha(E/K)[n]$ 有限。对合数 $n$，这也由 R1 的各素数幂情形取有限直和得到。

## 1. 一个固定有限扩张杀死全部 Sha，等价于全群有限

**命题 1。** 下列条件等价：

1. $\Sha(E/K)$ 有限；
2. 存在一个有限扩张 $L/K$，使限制映射
   $$\operatorname{res}_{L/K}:\Sha(E/K)\longrightarrow\Sha(E/L)$$
   为零。

对一个固定素数 $p$，同样有
$$
\Sha(E/K)[p^\infty]\text{ 有限}
\Longleftrightarrow
\text{存在有限 }L_p/K\text{ 杀死整个 }\Sha(E/K)[p^\infty].
\tag{1}
$$

**证明。** 若 $\Sha(E/K)$ 有限，给每个元素选择一个代表 torsor $C/K$。每个 $C$ 在代数闭包中有点，且一个这样的点只需有限多个代数坐标，所以在某个有限扩张 $L_C/K$ 中已有点。取有限多个 $L_C$ 的合成域，就同时杀死这些类。

反之，令 $d=[L:K]$。Galois 上同调的限制与余限制满足
$$
\operatorname{cor}_{L/K}\operatorname{res}_{L/K}=[d]
\quad\text{在 }H^1(K,E)\text{ 上}.
$$
因此若限制杀死全部 $\Sha$，则 $d\Sha=0$，即 $\Sha=\Sha[d]$，后者有限。这里不要求扩张 Galois；一般有限扩张的转移仍有同一恒等式，或先取 Galois 闭包。

对 $p$-初等部分，正向证明一样；反向令 $e=v_p(d)$，得到 $\Sha[p^\infty]=\Sha[p^e]$，仍有限。$\square$

**推论。** 若有常数 $B$，对某个素数集合 $\mathcal P$ 中每个 $p$ 都能以次数至多 $B$ 的扩张杀死 $\Sha(E/K)[p^\infty]$，则对所有 $p\in\mathcal P$、$p>B$，该初等部分为零。

**证明。** 此时 $p\nmid[L_p:K]$，乘 $[L_p:K]$ 在 $p$-初等群上可逆；由限制/余限制恒等式，该群只能为零。$\square$

所以“每个 torsor 分别在某个有限域中有点”虽然是无条件事实，却不提供一个对无限多个 torsor 统一的域或次数界。证明一个固定域对全部 Sha 都适用，本身已经证明全群有限；它比本题的无穷初级有限性更强，不能作为一个未经证明的便利替换。

## 2. 全部代数点模挠后的不变子空间没有新增方向

记
$$
V_E=E(\overline K)/E(\overline K)_{\rm tors},\qquad G_K=\operatorname{Gal}(\overline K/K).
$$
乘任意非零整数在 $E(\overline K)$ 上满射，其核由挠点组成；因此 $V_E$ 唯一可除，自然为 $\mathbb Q$-向量空间。

**命题 2。** 有自然同构
$$
E(K)\otimes_{\mathbb Z}\mathbb Q\xrightarrow{\sim}V_E^{G_K}.
\tag{2}
$$

**证明。** 对 $P\in E(K)$ 与正整数 $n$，选 $Q\in E(\overline K)$ 使 $nQ=P$。$Q$ 模挠类与选择无关，从而定义 $P/n\mapsto[Q]$。因为 $\sigma Q-Q\in E[n]$，其像 $G_K$-不变。若 $[Q]=0$，则 $P$ 为挠点，所以该映射单射。

为证满射，取不变类 $[Q]\in V_E^{G_K}$。对每个 $\sigma\in G_K$，$\sigma Q-Q$ 为挠点。点 $Q$ 定义在某个有限扩张中，所以它只有有限多个 Galois 共轭；这些差点构成有限集合。取其阶的公倍数 $N$，就有
$$
\sigma(NQ)=NQ\quad\text{对全部 }\sigma\in G_K,
$$
即 $NQ\in E(K)$。因此 $[Q]$ 是 $(NQ)/N$ 的像。$\square$

对 R4 的固定曲线及 $K=\mathbb Q$，(2) 的维数恰为 $2$。这个自然候选空间完全由 Mordell–Weil 点构成；从它出发尚不能得到一个包括未知可除 Sha 方向的统一 Selmer 实现。任何声称已有这种实现的论证，必须另行构造并证明与全 Selmer 群的比较。

## 3. 一个统一有理实现一旦存在，确实能传递维数

**命题 3（明确假设下的形式判据）。** 设 $\mathcal P$ 是素数集合，存在一个有限维 $\mathbb Q$-向量空间 $W$，并对每个 $p\in\mathcal P$ 给出已证明的同构
$$
W\otimes_{\mathbb Q}\mathbb Q_p
\simeq\operatorname{Sel}(K,V_pE).
\tag{3}
$$
若某个 $p_0\in\mathcal P$ 的 $\Sha(E/K)[p_0^\infty]$ 有限，则 $\mathcal P$ 中每个素数的初等部分都有限。

**证明。** 由 Kummer 的 Tate 模正合列，右边的维数为
$$
\operatorname{rank}E(K)+
\operatorname{corank}_{\mathbb Z_p}\Sha(E/K)[p^\infty].
$$
左边的维数恒为 $\dim_{\mathbb Q}W$。用 $p_0$ 得 $\dim W=\operatorname{rank}E(K)$，故其余 $p$ 的后一个余秩均为零；R1 给初级有限性。$\square$

本命题没有证明 (3)。命题 2 仅构造了已知的 Mordell–Weil 子空间，不能将它与全 Selmer 群的比较擅自标为同构。类似地，固定有限生成 $\mathbb Z$-模或有限自由整复形的有理上同调在各 $\mathbb Q_p$ 中维数相同，但把实际 Selmer 条件实现为这种对象仍是额外的算术断言。

## 来源与本题状态

- 限制/余限制和有限层 Kummer 背景：J. S. Milne, *Arithmetic Duality Theorems*, 2nd ed., 2006。所需有限性及与余秩的关系见 R1；上述量词与不变点论证均已完整给出。
- 对统一 ambient group 路线的动机：Y. Kezuka and D. Zagier, *A Birch–Swinnerton-Dyer dichotomy*, 作者预印本，检索于 2026-11-12，§§2、6；[作者原文](https://people.mpim-bonn.mpg.de/zagier/files/preprints/BSD_Dichotomy.pdf)。其中 $p$-余秩独立性明确作为猜想，而非现成定理；§6 已指出 (2) 的候选空间只给 Mordell–Weil 有理化，并归功于 Liang Xiao。本文不以该稿的未证明猜想作为输入。

统一域与统一有理空间两条路线均已落实为精确命题；尚无构造满足本题所需的额外条件。继续的问题是 R6 的跨 $p$ trace 非零、R7 的类群维数上界、R8 的导出类非零或 R10 的 signed 二次系数非零。
