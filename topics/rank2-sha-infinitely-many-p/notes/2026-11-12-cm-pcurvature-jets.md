# CM 导数递推：合法有限 jet 与除以 p 后的导子障碍

日期：2026-11-12。本文接续 R6、R9；未改变固定曲线或完成标准。

**状态。** §§1–3 的代数命题附完整证明。它们给出一个正确的有限商构造，并排除对 Hasse 不变量关系的一种错误提升；尚未得到 R6 的模 $\mathfrak p^4$ trace 非消失无穷性。有限 jet 的较小理想由主代理提出，本文核实其长度和应用。

## 1. 微分稳定的有限商：维数随 p 增长

设 $R=\mathbb Z_p[X]$，$G\in\mathbb Z_p[X]$ 为次数 $d$ 的首一多项式，令
$$
J=(p,G^p),\qquad R_k=R/J^k\quad(k\ge1).
$$

**命题 1。** $J^k$ 对 $\partial_X$ 稳定，因而对任意具有 $R$ 中系数的微分算子稳定。特别地，R6 的
$$
\mathcal L=4(X^3-17X)\partial_X^2
+6(3X^2-17)\partial_X+12X
$$
诱导 $R_k$ 上的算子。作为有限 $\mathbb Z_p$-模，
$$
\operatorname{length}_{\mathbb Z_p}R_k
=dp\frac{k(k+1)}2,\qquad
\dim_{\mathbb F_p}(R_k/pR_k)=dpk.
\tag{1}
$$

**证明。** $\partial_Xp=0$，而
$$
\partial_X(G^p)=pG^{p-1}G'\in J.
$$
由 Leibniz 法则，$J$ 微分稳定，进而每个幂 $J^k$ 也微分稳定。乘以多项式显然保持理想，因此任何有限阶的多项式系数微分算子均保持它。

由于 $G$ 首一，$R$ 作为 $\mathbb Z_p[G]$-模自由，基为 $1,X,\ldots,X^{d-1}$。可用逐次除法证明每个多项式唯一写成 $\sum_jr_j(X)G^j$，其中 $\deg r_j<d$。又
$$
J^k=(p^k,p^{k-1}G^p,\ldots,pG^{p(k-1)},G^{pk}).
$$
所以对 $0\le j<pk$，$G^j$ 层中的每个 $X^a$ 系数取值于
$$
\mathbb Z_p/p^{k-\lfloor j/p\rfloor}\mathbb Z_p,
$$
而 $j\ge pk$ 的层消失。将这些循环模的长度相加，得到
$$
d\sum_{j=0}^{pk-1}(k-\lfloor j/p\rfloor)
=dp\sum_{r=1}^kr=dp\frac{k(k+1)}2.
$$
每个存活循环模在模 $p$ 后都贡献一维，故模 $p$ 维数为 $dpk$。$\square$

**对 R6 的用法。** 在一个 split 位 $\mathfrak p\mid p$ 将 $G$ 的系数嵌入 $\mathbb Z_p$，对 $u$ 求值使 $G(u)=0$。$J^k$ 的任意元素在 $u$ 处取值均属于 $p^k\mathcal O_{F,\mathfrak p}$，因此可以在 $R_k$ 中重复应用递推，之后求值并取得 $B_n(u)$ 模 $p^k$ 的正确结果。由于 $v$ 为代数整数，乘以 $v$ 再求 trace 也保留这个精度。

对 $d=256,k=4$，模 $p$ 维数为 $1024p$，总 $\mathbb Z_p$ 长度为 $2560p$。这里应区分两个量，不能把总长度称作模 $p$ 的向量空间维数。

因此 R6 中无效的 $256$ 维固定商确实可以修复成合法有限商；但这个构造本身的大小随 $p$ 增长，不直接形成一个固定有限扩张上的 Frobenius 条件。它也不是对所有可能的更小模型的否定。

## 2. 模 p 的 Hasse 关系在本曲线上是什么

取 $p\ge5$、$p\nmid D$，在
$$
\mathcal A=\mathbb Z_{(p)}[x,y]/(y^2-x^3+Dx)
$$
上定义不变导子
$$
\delta x=2y,\qquad\delta y=3x^2-D.
$$
模 $p$ 的不变导子满足
$$
\bar\delta^{\,p}=H_p\bar\delta,
\tag{2}
$$
其中 $H_p$ 是微分 $dx/(2y)$ 对应的 Hasse 不变量。这是 Hasse 不变量的不变导子定义：$p$ 次迭代在特征 $p$ 下仍是导子，并仍平移不变，所以是该一维不变向量场空间中的一个常数倍。

原始标准出处为 N. Katz–B. Mazur，*Arithmetic Moduli of Elliptic Curves* (1985)，§12.3；可在线核查的逐式陈述见 S. Howe，*The spectral p-adic Jacquet–Langlands correspondence and a question of Serre*，Compositio Math. **158** (2022)，§3.2.2，[期刊原文](https://www.cambridge.org/core/journals/compositio-mathematica/article/spectral-padic-jacquetlanglands-correspondence-and-a-question-of-serre/7398F4C0CFA138C6C5CAA4C16ABD2415)。

用 Cartier 算子表示，$H_p$ 等于 $(x^3-Dx)^{(p-1)/2}$ 中 $x^{p-1}$ 的系数。这个公式也可从
$$
\frac{dx}{2y}=\frac{(x^3-Dx)^{(p-1)/2}}{2y^p}\,dx
$$
直接提取 Cartier 算子的 $x^{p-1}$ 项。该多项式次数小于 $2p-1$，所以没有别的 $ip-1$ 项贡献到一维全纯微分空间。特别地，当 $p\equiv1\pmod4$ 时，
$$
H_p=\binom{(p-1)/2}{(p-1)/4}(-D)^{(p-1)/4}\in\mathbb F_p^\times.
\tag{3}
$$
二项式系数的分子分母都由小于 $p$ 的非零整数构成，故非零；而 $D$ 也是单位。上述系数公式的标准算法表述见 A. Bostan–P. Gaudry–É. Schost，*Linear recurrences with polynomial coefficients and computation of the Cartier-Manin operator on hyperelliptic curves*，§4，[作者全文](https://cs.uwaterloo.ca/~eschost/publications/cartier.pdf)。

还有一条对递推直接可见的关系。令 $n=(p-3)/2$，并用 R6 的 $B_n$ 定义
$$
C_n(X)=2(3X^2-D)B_n(X)+4(X^3-DX)B_n'(X).
$$
则 $\delta^{p-1}x=C_n(x)$。在 $p\equiv1\pmod4$ 的情形，
$$
C_n(X)\equiv H_pX\pmod p.
\tag{4}
$$
**证明。** 由 (2)，$\delta(C_n(x))=\delta^px=H_p\delta x$，所以 $C_n'(X)=H_p$。$C_n$ 的次数至多 $(p+1)/2<p$，因此 $C_n-H_pX$ 是常数。递推 (2) 在每一步改变多项式的奇偶性，故 $B_n$ 的奇偶性与 $n$ 相同。这里 $n$ 为奇数，因而 $C_n$ 为奇多项式，该常数为零。$\square$

(4) 是有效的模 $p$ 简化，但 R6 的目标要求 trace 模 $\mathfrak p^4$，不能从 (4) 除以 $p^2$ 获取那两级新信息。

## 3. 除 p 后的误差算子严格地不是导子

下面把“还缺高精度”落实成一个明确的代数障碍。

**命题 2。** 设 $A$ 是无 $p$-挠的 $\mathbb Z_{(p)}$-代数，$p$ 为奇素数，$\delta$ 为 $\mathbb Z_{(p)}$-导子，且对某个 $H\in\mathbb Z_{(p)}$ 有
$$
\delta^p-H\delta\equiv0\pmod p.
$$
定义整的加法算子
$$
Q_p=\frac{\delta^p-H\delta}{p}:A\to A.
$$
则对任意 $a\in A$，
$$
\overline Q_p(\bar a^{\,p})=-(\bar\delta\bar a)^p.
\tag{5}
$$
因此，若 $A/pA$ 中存在 $\bar a$ 使 $(\bar\delta\bar a)^p\ne0$，则 $\overline Q_p$ 不是 $A/pA$ 上的导子。

**证明。** 对 $a^p$ 这个 $p$ 因子乘积连续使用 Leibniz 法则。按每个因子被求导的次数分组，得到
$$
\delta^p(a^p)\equiv
p a^{p-1}\delta^p(a)+p!(\delta a)^p\pmod{p^2A}.
\tag{6}
$$
为核实被省略项都含 $p^2$，设 $m_j$ 为恰被求导 $j$ 次的因子数。它们满足 $\sum m_j=p$、$\sum j m_j=p$，相应组合系数为
$$
\frac{p!}{\prod_jm_j!}\cdot
\frac{p!}{\prod_j(j!)^{m_j}}.
$$
除 $m_p=1,m_0=p-1$ 和 $m_1=p$ 两种情况外，所有出现的 $j$ 与所有 $m_j$ 都小于 $p$，故两个分子各贡献一个 $p$，分母都为 $p$-单位。这证明 (6)。

将 (6) 除以 $p$，再减去
$$
H\delta(a^p)/p=Ha^{p-1}\delta a,
$$
并用 $\delta^p a\equiv H\delta a\pmod p$，得到
$$
Q_p(a^p)\equiv(p-1)!(\delta a)^p\equiv-(\delta a)^p\pmod p.
$$
最后一步是 Wilson 定理。由于 $Q_p$ 为 $\mathbb Z_{(p)}$-线性算子，它模 $p$ 的作用与提升选择无关，所以得到 (5)。特征 $p$ 下的任意导子都消去 $p$ 次幂；若右侧非零，便与导子法则矛盾。$\square$

对第 2 节的椭圆曲线坐标环取 $a=x$，右侧为 $-(2y)^p\ne0$，故不论选择 (3) 的哪一个整数提升 $H$，得到的 $\overline Q_p$ 都不是导子。

同一障碍也体现在完整乘积公式中：
$$
Q_p(ab)=Q_p(a)b+aQ_p(b)
+\sum_{j=1}^{p-1}\frac1p\binom pj\delta^j(a)\delta^{p-j}(b).
\tag{7}
$$
中间二项式系数除以 $p$ 后通常在模 $p$ 非零。因而不能把 (2) 提升成“除以 $p$ 后仍是一个普通不变导子”的固定矩阵递推。

## 4. 对下一轮攻击的限制与可用数据

现在有一个可合法计算模 $p^4$ 的有限 jet 商，以及 (2)–(4) 的模 $p$ 关系和 (5)–(7) 的首个高阶误差恒等式。若继续沿此路，需要处理这个高阶误差算子及其 trace，而不是只保留 Hasse 不变量。

尚未证明的是：该额外数据能够由某个不随 $p$ 改变的对象控制，并在无穷多个 split $p$ 保证 R6 的 $a_{(p-3)/2}\notin\mathfrak p^4$。本文不把合法计算框架或模 $p$ 的 Hasse 单位性替代这个非消失断言。
