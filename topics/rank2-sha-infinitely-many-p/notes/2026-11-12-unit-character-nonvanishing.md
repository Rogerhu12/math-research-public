# 有限除法层的单位字符非零性，以及高度方法实际控制的量

**可信度：§1–5 已证明；§6 记录已核查的方法边界。** 本文沿用 R16 的固定曲线、辅助理想及单位：
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
\mathfrak f=2(1+i)17\mathcal O_K,\quad\mathfrak a=(7).
$$
设 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$，选 $\mathfrak p\mid p$，令
$$
L=K(E[\mathfrak p]),\quad G=\operatorname{Gal}(L/K),\quad
\chi:G\longrightarrow\mathbb F_p^\times,
$$
其中 $\chi$ 是 $E[\mathfrak p]$ 上的作用字符，$\widetilde\chi$ 是其 Teichmüller 提升。R12 给出 $G\simeq\mathbb F_p^\times$。唯一位于 $\mathfrak p$ 上的素点记为 $\mathfrak P$，并令 $F=L_{\mathfrak P}$。

本文证明 R16 中的三个深度均为有限整数：
$$
m_p<\infty,\qquad a_p<\infty,\qquad
2\le\nu_p=m_p+a_p<\infty.\tag{0.1}
$$
这消除了“所定义的字符单位可能恒为零”这一退化，但没有给出 $\nu_p\le3$，也不单独推出任何新的 $\Sha[p^\infty]$ 有限性。

## 1. 模 $\mathfrak p$ 字符的精确导子

令 $\psi$ 为 $E/K$ 的 Hecke 字符。因为 $K$ 的类数为一，对于与 $\mathfrak f$ 互素的 $\alpha\in\mathcal O_K$ 有
$$
\psi((\alpha))=\epsilon(\alpha)\alpha,
\qquad \epsilon(\alpha)\in\mu_4.
$$
$\epsilon$ 的精确有限导子为 $\mathfrak f$；这是 Hecke 字符导子的定义在类数一情形的表达。该导子已经由 CLS Lemma 3.2 及本题 cm-local-inputs note 核实。

CM reciprocity 给出，在 $\mathfrak m=\mathfrak f\mathfrak p$ 的 ray class group 上，
$$
\chi(\operatorname{Art}((\alpha)))
=\epsilon(\alpha)\alpha\pmod{\mathfrak p}.\tag{1.1}
$$
此式与更换生成元 $\alpha$ 无关，因为 $\epsilon(u\alpha)=u^{-1}\epsilon(\alpha)$，$u\in\mu_4$。

**引理 1.** 把 $\chi$ 膨胀到 $\operatorname{Gal}(K(\mathfrak m)/K)$ 后，其精确导子为 $\mathfrak m$；$\widetilde\chi$ 及其所有复嵌入具有相同导子。

**证明。** (1.1) 首先说明导子整除 $\mathfrak f\mathfrak p$。用中国剩余定理让 $\alpha\equiv1\pmod{\mathfrak p}$、而 $\alpha\pmod{\mathfrak f}$ 任意，此时 (1.1) 只剩 $\epsilon(\alpha)$。由于 $p\ge5$，映射 $\mu_4\to(\mathcal O_K/\mathfrak p)^\times$ 单射，故 $\mathfrak f$ 的每个局部导子指数原样保留。反过来让 $\alpha\equiv1\pmod{\mathfrak f}$，其模 $\mathfrak p$ 值任意，则 (1.1) 给出完整的 $\mathbb F_p^\times$ 字符，故还必须保留 $\mathfrak p$ 因子。Teichmüller 提升及复嵌入都不改变有限字符的核。$\square$

特别地，$2$ 和 $17$ 的导子因子不会因模 $p$ 而消失。这里对每个所列 $p$ 都有精确结论。

## 2. 使用原始字符的 Kronecker 极限公式

以下只需第二 Kronecker 极限公式的一项标准非零性推论。

**原始字符单位引理。** 设 $\mathfrak m$ 不是素理想幂，$\mu_K\to(\mathcal O_K/\mathfrak m)^\times$ 单射，$T_0$ 为精确 $\mathfrak m$-阶点，$\mathfrak a$ 与 $6\mathfrak m$ 互素且 $N\mathfrak a>1$。则对 $H=\operatorname{Gal}(K(\mathfrak m)/K)$ 的任意精确导子为 $\mathfrak m$ 的复字符 $\vartheta$，有
$$
\sum_{h\in H}\vartheta(h)^{-1}
\log\left|h\Theta_{E,\mathfrak a}(T_0)\right|^2\ne0.\tag{2.1}
$$

该结论来自 Flach, *Iwasawa theory and motivic L-functions*, Lemma 2.2(e) 的第二极限公式。其归一化同 Rubin 函数的关系是
$$
\Psi(1;\mathfrak m,\mathfrak a^{-1}\mathfrak m)^{12}
=\Theta_{\Omega\mathcal O_K,\mathfrak a}(\Omega/m),
\qquad (m)=\mathfrak m,\tag{2.2}
$$
其中左边 $\Psi$ 表示 Robert 的函数，避免与本题 Hecke 字符 $\psi$ 混用。Schmitt 的作者预印本 §3、公式 (3.14) 前逐式给出这一十二次幂比较，并在 (3.14)–(3.15) 写出范数后的极限公式。本文只用这项一般的有限层公式，不使用该文要求 $\mathfrak f$ 为素理想幂的 Iwasawa 主定理。

说明 (2.1) 中为何没有可能的零因子：原始有限阶 Hecke 字符的 $L$ 函数在 $s=1$ 非零，由函数方程及唯一复无穷位的 Gamma 因子，其在 $s=0$ 的零恰为一阶。第二极限公式把相应 Fourier 对数同这一非零的一阶导数联系起来。辅助理想产生的因子为 $N\mathfrak a$ 减去一个有限阶字符值；其绝对值不可能为零，因为 $N\mathfrak a>1$，而字符值的复绝对值为一。精确导子等于 $\mathfrak m$ 保证没有删除未分歧 Euler 因子所引入的额外零。我们只采用同时对字符及其逆成立的非零性结论 (2.1)，不把不同 Artin 约定下的精确标量认作相同。

在本文的幂等元约定下，辅助理想的字符方向也可以直接检查。Rubin Lemma 7.10 的 theta 比值给出
$$
\Theta_{\mathfrak a}(T)^{N\mathfrak b}/
\Theta_{\mathfrak a}([b]T)
=
\Theta_{\mathfrak b}(T)^{N\mathfrak a}/
\Theta_{\mathfrak b}([a]T)
$$
（$\mathfrak a=(a),\mathfrak b=(b)$，两者均与点阶互素）。由 reciprocity，$[a]T$ 对应 $\sigma_{\mathfrak a}$ 的作用。因此取 $e_\vartheta$ 后的乘子是
$N\mathfrak a-\vartheta(\sigma_{\mathfrak a})$。在 $\mathfrak a=(7)$ 时它是 $49$ 减去一个单位根，始终非零。此处没有把这个复非零性因子替代为 R16 中的 $p$-进 Euler-system 单位条件。

## 3. 特定的 $\eta_p$ 确实有非零字符分量

沿用 R16 的
$$
\eta_p=\Lambda(P_\pi)
=N_{K(\mathfrak f\mathfrak p)/L}
\Theta_{E,(7)}(S+P_\pi).
$$
单位性、范数次数 $256$ 及固定函数 $\Lambda$ 的准确比较已经在 relative-classgroup-reflection note §4.1 证明。

取 $S=\xi(\Omega/f)$、$\pi_E=\psi(\mathfrak p)$、$P_\pi=\xi(\Omega/\pi_E)$，则
$$
S+P_\pi
=\xi\left(\frac{(f+\pi_E)\Omega}{f\pi_E}\right).
$$
因 $f+\pi_E$ 与 $f\pi_E$ 互素，该点是精确 $\mathfrak m$-阶点。它与标准点 $\xi(\Omega/(f\pi_E))$ 相差一次 ray class Galois 作用以及一个可能的 $\mu_4$ 自同构；Rubin Lemma 7.2 说明 $\Theta$ 在后者下不变。因此两个 $\Theta$ 值确为 Galois 共轭，对字符分量仅乘一个非零单位根。更换固定 $S$ 的生成元也一样。

令 $\vartheta$ 是 $\widetilde\chi$ 经某复嵌入所得的字符，仍写成 $H=\operatorname{Gal}(K(\mathfrak m)/K)$ 上的膨胀字符。若 $\beta=\Theta_{E,(7)}(S+P_\pi)$，范数与 Fourier 和满足精确恒等式
$$
\sum_{g\in G}\vartheta(g)^{-1}\log|g\eta_p|^2
=\sum_{h\in H}\vartheta(h)^{-1}\log|h\beta|^2.\tag{3.1}
$$
这是逐个陪集展开范数，没有额外的 $256$ 次幂。引理 1 及 (2.1) 说明右边非零。

定义
$$
e_\chi=\frac1{p-1}\sum_{g\in G}\widetilde\chi(g)^{-1}g,
\qquad
\mathscr E_p=
\left((\mathcal O_L^\times/\mu_L)\otimes\mathbb Z_p\right)^{\widetilde\chi}.
$$
(3.1) 证明 $e_\vartheta\eta_p$ 在全局单位模的复化中非零。幂等元系数属于 $\mathbb Q(\mu_{p-1})$，换到给定的 $p$-进嵌入保持非零，故
$$
z_p=e_\chi\eta_p\ne0\quad\text{于 }\mathscr E_p.\tag{3.2}
$$
Dirichlet 单位定理把该单位表示识别为正则表示去掉平凡字符，所以 $\mathscr E_p$ 自由秩一。这证明 $m_p<\infty$。论证针对 R16 的具体 $\eta_p$，没有从“全部椭圆单位有有限指数”直接跳到一个未核对的生成元。

## 4. Baker–Brumer 证明这个字符线的局部化非零

所需 Baker–Brumer 定理的形式为：代数 $p$-进单位的对数若在 $\mathbb Q$ 上线性无关，则在代数数系数上也线性无关。来源是 Brumer (1967)；Sharifi 作者讲义 Theorem 1.5.17 陈述这一形式，并在 Theorem 1.5.21 给出其对虚二次域阿贝尔扩张的应用。

为使需要的范围清楚，下面直接证明有限层的单个字符断言。

取 $\mathcal O_L^\times/\mu_L$ 的一个 $\mathbb Z$-基 $u_1,\ldots,u_{p-2}$，并固定由 $\mathfrak P$ 决定的嵌入 $L\hookrightarrow F\hookrightarrow\mathbb C_p$。其对数在 $\mathbb Q$ 上线性无关：有理关系清分母后给出 $\log_p\prod_j u_j^{n_j}=0$；局部单位的对数核是单位根，因此 $\prod_j u_j^{n_j}$ 在 $F$ 中是单位根，也就在 $L$ 中是单位根，迫使所有 $n_j=0$。

因为 $\mathscr E_p$ 非零，可以选一个普通全局单位 $u$，使 $e_\chi u\ne0$。把 $gu$ 写到上述整数基后，有
$$
e_\chi u=\sum_j A_j u_j,
\qquad A_j\in\mathbb Q(\mu_{p-1})\subset\mathbb Q_p,
$$
且不是所有 $A_j$ 都为零。这里只是单位模的加法记号；没有定义代数单位的任意代数数次幂。

若其局部化对数为零，则
$$
\sum_j A_j\log_p(u_j)=0
$$
为一条非平凡的代数系数关系，违反 Baker–Brumer。故局部化映射
$$
\lambda_p:\mathscr E_p\longrightarrow\mathscr U_p
$$
非零。R16 已证明两端均为自由秩一 $\mathbb Z_p$ 模，所以 $\lambda_p$ 单射且有有限余核。于是存在有限整数 $a_p\ge0$ 使
$$
\lambda_p(\mathscr E_p)=p^{a_p}\mathscr U_p.\tag{4.1}
$$

这里 $G$ 恰是 $\mathfrak P$ 的整个分解群，所以局部化与同一 $e_\chi$ 交换，落入 R16 的那个局部本征线。我们没有把所有数域的 Leopoldt 猜想当作已知，也没有从一个无穷层的假设推出上述断言；所用的是每一个有限阿贝尔层上的 Baker–Brumer 定理及重数一。

结合 (3.2)、(4.1) 与 R16，得到 (0.1)。特别地，R16 对 $\nu_p=\infty$ 所保留的约定在本文范围内不会出现。

## 5. 这个非零性究竟推进了什么

目前每个所列 $p$ 都有
$$
1\le c_p\le m_p\le\nu_p<\infty,
\qquad \nu_p=m_p+a_p,
$$
并且 R16 给出 $\nu_p\ge2$ 及 $\nu_p\le3\Rightarrow\Sha(E/\mathbb Q)[p^\infty]=0$。

有限的 $\nu_p$ 只界定一个有限层类群字符分量的阶；它没有把该类群的 $p$-秩压到 $1$ 或 $2$。例如这些已证不等式允许 $c_p=3,m_p=3,a_p=1,\nu_p=4$，此时 R7 的有限层 Selmer 维数公式给出 $s_p=4$。这不是声称存在这样的素数，而是指出现有结论在逻辑上没有排除该情形。

因此真正尚缺的是无穷多个 $p$ 的小深度上界，不能以逐个 $p$ 的非零性替代。

## 6. 固定函数的统一高度界为何没有给出所需上界

确实存在只依赖固定 $E,\Lambda$ 的常数 $C$，使
$$
h(\eta_p)=h(\Lambda(P_\pi))\le C\quad\text{对所有所列 }p.\tag{6.1}
$$
理由是挠点的 Néron–Tate 高度为零，固定曲线上的朴素坐标高度与它只差一个有界量；再用固定有理函数的高度上界即可。所有 $P_\pi$ 均避开 $\Lambda$ 的零极点，已由单位性保证。

但 $z_p=e_\chi\eta_p\in p^{m_p}\mathscr E_p$ 是完成后的字符格中的可除性。$e_\chi$ 的系数是 $p$-进 Teichmüller 单位根，而非普通整数，所以不能写成 $\eta_p=v^{p^{m_p}}$ 后对这个不存在的普通单位等式使用高度。

即使把投影改写成真正的整数指数乘积，损失也很具体。对每个 $g$ 取
$$
0\le A_g<p^m,
\qquad A_g\equiv\widetilde\chi(g)^{-1}\pmod{p^m},
$$
并设 $m=m_p$。由于
$\sum_g A_g g\eta_p\equiv(p-1)e_\chi\eta_p\pmod{p^m}$，整数单位格中坐标属于 $p^m\mathbb Z_p$ 的整数向量必属于 $p^m\mathbb Z^{p-2}$，故存在普通全局单位 $v$ 及单位根 $\zeta$ 使
$$
\prod_{g\in G}(g\eta_p)^{A_g}=\zeta v^{p^m}.
$$
(6.1) 只能给出
$$
p^m h(v)\le(p-1)(p^m-1)C,
\qquad h(v)<(p-1)C.\tag{6.2}
$$
右边在除以 $p^m$ 后没有随 $m$ 减小。因而直接使用小高度单位的下界不会限制 $m$。

定量对数工具也必须保留变化的参数：$[L:\mathbb Q]=2(p-1)$；容纳投影系数的数域可以取 $L\mathbb Q(\mu_{p-1})$，其次数至多
$$
2(p-1)\varphi(p-1)\le2(p-1)^2.
$$
Fourier 对数含 $p-1$ 项，或者改用 $p-2$ 个基本单位的对数。Baker–Brumer 的定性非零性本身没有给出在这些参数变化时仍足够强的赋值上界。本文未得到任何可推出阈值 $3$ 的定量估计。

## 来源与依赖

- A. Brumer, *On the units of algebraic number fields*, Mathematika 14 (1967), 121–124，[DOI](https://doi.org/10.1112/S0025579300003703)；所用定理形式及字符论证明另见 R. Sharifi [作者讲义 §1.5](https://math.ucla.edu/~sharifi/notes/iwasawa-ch01.html)，Theorems 1.5.17、1.5.21。
- M. Flach, *Iwasawa theory and motivic L-functions*, Pure Appl. Math. Q. 5 (2009), 255–294，[DOI](https://doi.org/10.4310/PAMQ.2009.v5.n1.a8)，Lemma 2.2(e)。
- U. Schmitt, *A Twist Conjecture For Certain CM Elliptic Curves*，[作者预印本](https://www.mathi.uni-heidelberg.de/fg-sga/Preprints/A%20Twist%20Conjecture%20for%20certain%20CM%20Elliptic%20Curves_%28Ulrich%20Schmitt%29_v160103.pdf)，§3，公式 (3.14)–(3.15) 及之前的十二次幂比较；仅用一般有限层 Kronecker 公式。
- K. Rubin, *Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，[作者讲义](https://swc-math.github.io/notes/files/99RubinCM.pdf)，Corollary 5.16、Theorem 7.4、Lemma 7.10；本题 R12、R16 及 reflection note §4.1。
- J. Coates, Z. Liang and R. Sujatha, [arXiv:0901.3832](https://arxiv.org/abs/0901.3832)，Lemma 3.2，固定导子输入。
