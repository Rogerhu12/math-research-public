# 固定 CM 秩 2 曲线的超奇异路线：signed 二次项、向量高度及超越性边界

日期：2026-11-12。会话：Astra-rank2-Sha / literature_scope。

**状态：主目标未完成。** 本文的模论推论和秩 2 线性代数引理有完整证明；引用的经典定理已对照原文的具体陈述。没有证明任何固定曲线在无穷多个超奇异素数处的二次项非零。新近稿件仅作范围核查，不作为未补证明的输入。

研究对象固定为 R4 的
$$
E=E_{17}:y^2=x^3-17x,
\qquad P=(-1,4),\quad Q=(9,24).
$$
R4 已证明 $\operatorname{rank}E(\mathbb Q)=2$，并证明 $P,Q$ 独立。本笔记检验：限制到 $p\equiv3\pmod4$，能否利用两个 signed 分量、CM 对称性或 $p$-adic 解析子群定理，消除 ordinary 路线里的二次非零缺口。

## 1. 所有惰性素数处已有适用的主猜想

曲线判别式为 $64\cdot17^3$，故每个 $p\equiv3\pmod4$ 都是奇数好约化素数。CM 环为 $\mathbb Z[i]$，这些素数在 $K=\mathbb Q(i)$ 中惰性。也可以直接算出 $a_p=0$：若 $\chi$ 为模 $p$ 二次特征，
$$
a_p=-\sum_{x\in\mathbb F_p}\chi(x^3-17x).
$$
将 $x$ 与 $-x$ 配对；由于 $\chi(-1)=-1$，每对贡献相消。$x=0$ 的贡献为零。所以 $a_p=0$，即为超奇异约化；Frobenius 多项式为 $X^2+p$。

以下 $\mathbb Q_\infty/\mathbb Q$ 是 cyclotomic $\mathbb Z_p$-扩张，$\Gamma=\operatorname{Gal}(\mathbb Q_\infty/\mathbb Q)$，$\Lambda=\mathbb Z_p[[\Gamma]]=\mathbb Z_p[[T]]$。**不要与反 cyclotomic 扩张混淆。**

Pollack–Rubin，*The main conjecture for CM elliptic curves at supersingular primes*，Annals of Mathematics 159 (2004), 447–464，Theorem 7.3 和 Lemma 8.3，分别给出
$$
\operatorname{char}_\Lambda X_p^\pm=(L_p^\pm(E,T)),
\qquad
\operatorname{Sel}_{p^\infty}(E/\mathbb Q)
\simeq
\operatorname{Sel}_{p^\infty}^\pm(E/\mathbb Q_\infty)^\Gamma,
\tag{1.1}
$$
其中 $X_p^\pm$ 是 signed Selmer 群的 Pontryagin 对偶，属于有限生成 torsion $\Lambda$-模。原文假设是 $E/\mathbb Q$ 有全整数环 CM、$p$ 为奇数好超奇异素数；$E_{17}$ 满足这些假设。这里没有以 $\Sha[p^\infty]$ 有限为输入。

原文：[arXiv 的已发表文本](https://arxiv.org/pdf/math/0509604)，[Annals 出版页面](https://annals.math.princeton.edu/2004/159-1/p11)。已独立核对上述两个陈述及 Lemma 8.3 的限制映射证明。

### 已证明推论 1：任一 signed 二次项非零足以得到该素数的有限性

记
$$
s_p=\operatorname{corank}_{\mathbb Z_p}
\operatorname{Sel}_{p^\infty}(E/\mathbb Q).
$$
对每个 $p\equiv3\pmod4$ 及任一符号，都有
$$
2\le s_p\le\operatorname{ord}_{T=0}L_p^\pm(E,T).
\tag{1.2}
$$
因此，若
$$
\bigl([T^2]L_p^+(E,T),[T^2]L_p^-(E,T)\bigr)\ne(0,0),
\tag{1.3}
$$
则 $s_p=2$，从而 $\Sha(E/\mathbb Q)[p^\infty]$ 有限。

**证明。** Kummer 正合列及 R4 给 $s_p\ge2$。取 (1.1) 的 Pontryagin 对偶，得
$$
s_p=\dim_{\mathbb Q_p}\bigl((X_p^\pm/TX_p^\pm)\otimes_{\mathbb Z_p}\mathbb Q_p\bigr).
$$
对任意有限生成 torsion $\Lambda$-模 $M$，在高度一素理想 $(T)$ 处局部化。$R=\Lambda_{(T)}$ 是 DVR，剩余域为 $\mathbb Q_p$，且
$$
M_{(T)}\simeq\bigoplus_{j=1}^m R/(T^{e_j}),\quad e_j\ge1.
$$
于是
$$
\dim_{\mathbb Q_p}((M/TM)\otimes\mathbb Q_p)=m
\le\sum_{j=1}^m e_j
=\operatorname{ord}_{T=0}\operatorname{char}_\Lambda(M).
$$
代入 $M=X_p^\pm$ 及 (1.1) 得 (1.2)。若任一二次系数非零，(1.2) 已排除常数项和一次项，该符号的消失阶就是 $2$，故 $s_p=2$。由 Kummer 正合列，$\Sha[p^\infty]$ 的余秩为零；它是余有限生成 $\mathbb Z_p$-模，所以有限，详见 R1。证毕。

**缺口的精确形式：** 证明 (1.3) 对无穷多个 $p\equiv3\pmod4$ 成立。本推论并未证明该条件必要；仅知 $\Sha[p^\infty]$ 有限，不能无条件代入一个预期的高度非退化结论来反推二次项非零。

## 2. 两个分量不是自动的二次非零来源

取 $\alpha^2=-p$、$\beta=-\alpha$。Pollack 的分解在 $a_p=0$ 时具有形式
$$
\begin{pmatrix}L_{p,\alpha}\\L_{p,\beta}\end{pmatrix}
=
\begin{pmatrix}
\log_p^+(T)&\alpha\log_p^-(T)\\
\log_p^+(T)&\beta\log_p^-(T)
\end{pmatrix}
\begin{pmatrix}L_p^+\\L_p^-\end{pmatrix}.
\tag{2.1}
$$
这些 $\log_p^\pm$ 是 Pollack 的 cyclotomic 对数幂级数，**不是点 $P,Q$ 的形式群对数**。它们在 $T=0$ 取非零值。可直接从乘积定义验证：每个 cyclotomic 多项式在 $1$ 处的值为 $p$，除以 $p$ 后常数项为 $1$，只剩非零的整体规范因子。参见 Lei，*Iwasawa theory for modular forms at supersingular primes*，Compositio Mathematica 147 (2011), 803–838，§3.4，公式 (5)、(6) 和其前的乘积定义：[作者文本](https://antoniolei.com/wp-content/uploads/2014/09/ap0compositio.pdf)。

矩阵在零点的行列式为
$$
(\beta-\alpha)\log_p^+(0)\log_p^-(0)\ne0.
$$
故此矩阵在 $\mathbb Q_p(\alpha)[[T]]$ 上可逆，得到
$$
\min\{\operatorname{ord}_T L_{p,\alpha},\operatorname{ord}_T L_{p,\beta}\}
=
\min\{\operatorname{ord}_T L_p^+,\operatorname{ord}_T L_p^-\}.
\tag{2.2}
$$
证明只需观察：可逆幂级数矩阵保持向量所属的 $T^n$ 倍子模。特别地，两端的常数项和一次项都为零后，二次系数向量之间由 (2.1) 在 $T=0$ 的可逆矩阵联系。

因此，从 signed 坐标换成 Frobenius 特征坐标，或者写成 Dieudonné 模值 $p$-adic $L$ 函数，都没有免去同一个二次非零条件。$\alpha\leftrightarrow\beta$ 的共轭把两个特征分量互换，但两个同时在二阶消失完全符合这种对称性。形式上，一对 $T^4$ 的倍数即可说明“幂级数非零 + 共轭关系 + 消失阶至少为 $2$”不蕴含二次项非零；这只是这些抽象输入的逻辑模型，并非声称实际 $L$ 函数等于此模型。

Lei 的 Theorem 7.9 也证明适当 CM 高权情形的 signed 主猜想。其作用仍是特征理想与 $L$ 函数的比较，不是固定权重在零点的阶数等式。对本曲线的权重 $2$ 问题，2004 年的主猜想已经足够；缺少的是增广点处的非零信息。

## 3. 秩 2 的向量 regulator 可以显式化简

取 $\omega=dx/(2y)$、$\eta=x\omega$，并以 $[\omega,\eta]=1$ 规范 de Rham 交替配对。设
$$
\ell=\begin{pmatrix}a\\b\end{pmatrix}
=\begin{pmatrix}\log_\omega(P)\\\log_\omega(Q)\end{pmatrix}\in\mathbb Q_p^2.
$$
这里 $a,b$ 均非零：$E(\mathbb Q_p)$ 上形式群对数延拓的核是 torsion。证明是先用一个整数倍把点送入对数单射的充分小开子群，再利用对数为零。R4 的两个点都非 torsion。

Bernardi–Perrin-Riou 的高度族 $h_\nu$ 对 $\nu$ 线性，且
$$
h_\omega(R)=-\log_\omega(R)^2.
$$
在本节统一使用
$$
B_h(R,S)=\frac{h(R+S)-h(R)-h(S)}2.
$$
令 $H=(B_{h_\eta}(P_i,P_j))_{i,j}$，其中 $(P_1,P_2)=(P,Q)$。这样 $h_\omega$ 的矩阵就是 $-\ell\ell^t$。部分文献的双线性配对省略 $1/2$，或整体除以 $\log_p\kappa(\gamma)$；它们及有限指数基的修正只乘非零因子，不影响以下零性判断。

### 已证明引理 2：两个向量坐标及同时为零的分类

定义
$$
d=\det H,\qquad q=\ell^t\operatorname{adj}(H)\ell.
$$
若 $\nu=s\omega+t\eta$，则
$$
G_\nu=tH-s\ell\ell^t,\qquad
\det G_\nu=t^2d-stq.
\tag{3.1}
$$
在上述配对与基的规范下，秩 $2$ 的向量 regulator 为
$$
\mathcal R_p=d\omega+q\eta.
\tag{3.2}
$$
特别地，
$$
\mathcal R_p=0
\Longleftrightarrow d=q=0
\Longleftrightarrow H=c\ell\ell^t\quad\text{对某个 }c\in\mathbb Q_p.
\tag{3.3}
$$
**证明。** 写 $H=\left(\begin{smallmatrix}u&v\\v&w\end{smallmatrix}\right)$，直接展开行列式：
$$
\det(tH-s\ell\ell^t)
=t^2(uw-v^2)-st(wa^2-2vab+ub^2).
$$
系数 $s^2$ 消失，因为 $\ell\ell^t$ 的秩为 $1$。BPR 向量 regulator 的定义在秩 $2$ 时为
$$
[\mathcal R_p,\nu]=\frac{\det G_\nu}{[\omega,\nu]}
\qquad(t\ne0).
$$
右边等于 $td-sq$，而 $[d\omega+q\eta,s\omega+t\eta]=dt-qs$，故 (3.2) 成立。关于这个定义，参见 Sprung §4.1、公式 (1)；另见 Castella 的 Lemma 2.3.2，下节列明版本。

为证明 (3.3)，对二维空间换基使非零线性泛函 $\ell$ 的坐标为 $(1,0)^t$。零性不随此换基改变。此时 $q=H_{22}$，而 $d=H_{11}H_{22}-H_{12}^2$。若 $d=q=0$，先得 $H_{22}=0$，再得 $H_{12}=0$，故 $H=c\ell\ell^t$。反向显然。证毕。

### strict Mordell–Weil 高度的实际输入

局部对数映射
$$
E(\mathbb Q)\otimes\mathbb Q_p\longrightarrow\mathbb Q_p,
\qquad xP+yQ\longmapsto ax+by
$$
的核为一维，由
$$
v=bP-aQ
\tag{3.4}
$$
生成。这是张量积里的向量，通常不是某个实际有理点。其 $h_\eta$ 高度为
$$
B_{h_\eta}(v,v)=b^2H_{11}-2abH_{12}+a^2H_{22}=q.
\tag{3.5}
$$
在核上 $h_\omega=0$，故对任意 $t\ne0$，规范高度 $h_{s\omega+t\eta}/[\omega,s\omega+t\eta]$ 的限制都等于 $h_\eta$ 的限制。于是 strict regulator 非零等价于 $q\ne0$，不计格基的非零平方因子。

注意：本引理只给出
$$
\operatorname{Reg}^{\rm str}_p\ne0\ \Longrightarrow\ \mathcal R_p\ne0.
$$
不能在没有其他算术结构的证明时反写等价；在线性代数上 $q=0,d\ne0$ 完全可能。

## 4. 已有高度公式仍要求额外输入

Francesc Castella，*A formula of Perrin-Riou and characteristic power series of signed Selmer groups*，2025-03-01 作者版本：[Coates.pdf](https://web.math.ucsb.edu/~castella/Coates.pdf)。已核对 Theorem A、Definitions 2.3.1–2.3.3、Theorem 2.4.1、Proposition 4.2.4 和 Theorem 5.1.1。

对奇数超奇异 $p$、$a_p=0$，其 Theorem A 的阶数是
$$
\rho=\min\{\operatorname{ord}_T\xi_p^+,\operatorname{ord}_T\xi_p^-\}\ge r.
$$
若 $\Sha[p^\infty]$ 有限且 strict regulator 非零，才得到 $\rho=r$ 与相应的 leading coefficient 公式。**结论是两个阶数的最小值等于 $r$；不要照抄旧版本或第三方摘录为每个符号都等于 $r$。**

Theorem 2.4.1 对 arithmetic Dieudonné 模值函数给出的也是上述类型的有条件阶数结论，其来源为 Perrin-Riou 1993 的 Propositions 3.4.5–3.4.6 及 2003 的 Theorem 3.1。以 Pollack–Rubin 主猜想把 arithmetic 与 analytic 对象连接，并没有消去公式中关于 $\Sha$ 或 strict 高度的条件。不能用这条公式循环证明它自己的有限性前提。

Florian Sprung，*A formulation of p-adic versions of the Birch and Swinnerton-Dyer conjectures in the supersingular case*，Research in Number Theory 1 (2015), Article 17：[原文](https://arxiv.org/pdf/1512.09362)。Conjecture 1.2 / 4.17 为两分量版本的 BSD；Theorem 1.3 / 4.19 证明它与 BPR 猜想等价，并未证明猜想成立。Theorem 4.22 给 Kato 的阶数下界。Theorem 1.4 / 3.1 的商值判据另有有限性与局部化非零假设，不能作为本题所需的无条件二次项结论。

Perrin-Riou 原文：*Fonctions L p-adiques d'une courbe elliptique et points rationnels*，Annales de l'Institut Fourier 43 (1993), 945–995，[原文](https://www.numdam.org/item/10.5802/aif.1362.pdf)。本轮打开原文并核对其目标，具体 leading-term 假设通过 Castella 对精确命题的重述核对；没有声称逐行复核这篇长文的全部证明。Bernardi–Perrin-Riou 1993 的 C. R. 短文原版未获取全文，其 formulation 由 Sprung 的精确定义和等价定理交叉核查。

## 5. 为什么单点非零、CM 对称与解析子群定理还不够

### 5.1 一个同时保留单点非零的退化模型

取 $c\in\mathbb Q_p^\times$，令
$$
H=c\ell\ell^t.
$$
则对任何非零 $(x,y)\in\mathbb Q^2$，只要 $a,b$ 在 $\mathbb Q$ 上线性无关，就有
$$
h_\eta(xP+yQ)=c(ax+by)^2\ne0.
$$
然而引理 2 给 $\mathcal R_p=0$；strict 向量 (3.4) 的高度也为零。因此，“每个非 torsion 有理点的高度非零”并不蕴含秩 $2$ regulator 非零。

这不是实际曲线高度的反例，也不反驳 BSD。它说明单点结论提供的逻辑信息不足以推出行列式结论。恰是完成后的 $\mathbb Q_p$-线性空间中存在不能用有理点逐点检验的方向。

CM 的单位对称同样没有在这一步排除退化。令 $F=\mathbb Q_p(i)$，$\sigma$ 为非平凡共轭。在 $F^2$ 上考虑 Hermitian 型
$$
\mathfrak h(z,w)=c\ell(z)\,\sigma(\ell(w)),\qquad \ell(z)=az_1+bz_2.
$$
它具有 $\mathfrak h(iz,iw)=\mathfrak h(z,w)$，并与共轭相容；更一般地，对所有 $\alpha\in\mathbb Q(i)$ 都满足 $\mathfrak h(\alpha z,\alpha w)=N(\alpha)\mathfrak h(z,w)$。在固定子空间 $\mathbb Q_p^2$ 上，其矩阵仍为 $c\ell\ell^t$。即使 $a,b$ 在 $\mathbb Q(i)$ 上线性无关，每个非零 $\mathbb Q(i)$-向量的自配对都可非零，而该型在 $F^2$ 上的秩仍为 $1$。这是 CM 标量等变性层面的模型；未声称它满足实际全局高度的每一条额外公理。

### 5.2 解析子群定理确实给什么

Clemens Fuchs、Duc Hiep Pham，*Some applications of the p-adic analytic subgroup theorem* (2016)，[原文](https://arxiv.org/pdf/1412.1248)，Theorems 1.1、2.1、2.2。已核对陈述和应用的证明结构。

Theorem 1.1 的输入是定义在 $\overline{\mathbb Q}$ 上的交换代数群、其 Lie 代数的 **$\overline{\mathbb Q}$-线性子空间**，以及非零对数落入该空间的 **代数点**。Theorem 2.2 推出：简单阿贝尔簇的代数点对数若在端同态环上独立，则在 Lie 代数的代数端同态系数上仍独立。

对本曲线，$P,Q$ 在 $\mathbb Z[i]$ 上也独立（模 torsion）。事实上，若
$$
(m+ni)P+(u+vi)Q
$$
为 torsion，对复共轭取和与差，得 $mP+uQ$ 及 $nP+vQ$ 都为 torsion；R4 的有理独立性迫使四个整数全为零。将 $P,Q$ 同乘足够大的整数即可放进局部指数映射的定义域。若其对数有 $\mathbb Z[i]$ 线性关系，对数核为 torsion，又与上述独立性矛盾。因此 Theorem 2.2 确实给
$$
a,b\text{ 在所选嵌入的 }\overline{\mathbb Q}\text{ 上线性无关}.
\tag{5.1}
$$
特别地 $b/a$ 不是代数数。这比排除有理系数关系强得多；但它没有使 (3.4) 变成一个代数点。

将解析子群定理用到 (3.4) 会在两个具体位置失效：其系数为 $p$-adic 数 $a,b$，一般不是代数数；$v$ 是 $E(\mathbb Q)\otimes\mathbb Q_p$ 的元素，不是已给出的 $E(\overline{\mathbb Q})$ 点。其对数为零来自构造，不能被该定理禁止。等式 $d=q=0$ 还涉及高度的二次关系，亦不是代数系数的对数线性关系。

同理，一个广义或导出 Kato 类首先是 Galois 上同调类。把它识别为已知代数点，或识别为 Mordell–Weil 子空间中的指定非零向量，需要独立证明；不能把待证的 Kummer 归属作为调用超越性定理的前提。即便已经进入 $E(\mathbb Q)\otimes\mathbb Q_p$，任意 $p$-adic 系数的向量仍不自动是代数点。

### 5.3 已知单点高度定理的适用范围

Agboola–Howard，*Anticyclotomic Iwasawa theory of CM elliptic curves*，附 Karl Rubin 的 appendix，[作者原文](https://web.math.ucsb.edu/~agboola/papers/cm1-final.pdf)，Theorem A.1 引述 Bertrand 的 CM 单点高度非零定理。该文处于 split ordinary $\mathfrak p$-adic 高度设置；appendix 明确区别单点非零与配对非退化。既不能直接换成 inert 高度，也不能把该定理施于 (3.4) 的 $p$-adic 张量向量。

Burungale–Disegni，*On the non-vanishing of p-adic heights on CM abelian varieties, and arithmetic of Katz p-adic L-functions*，AIF 70 (2020), 2077–2101，[原文](https://www.numdam.org/item/10.5802/aif.3381.pdf)。其 fixed-prime ordinary、反 cyclotomic 特征变化的非零结果，没有提供固定 $E$ 而 $p$ 变化的秩 $2$ strict regulator 非零性。

## 6. 近年 supersingular 文献的具体边界

下表只记录已从 primary source 核对的范围。没有用第三方标题或摘要的较强说法替换定理假设。

| 文献 | 已核对的位置与结果 | 对本问题仍缺什么 |
|---|---|---|
| Kobayashi，*p-adic Gross–Zagier formula for elliptic curves at supersingular primes*，Invent. Math. 191 (2013), 527–629，[出版页面](https://link.springer.com/article/10.1007/s00222-012-0400-9) | 出版摘要说明第一导数与 Heegner 点高度，应用为 rank $1$ 情形 | 没有从两个独立点推出 rank $2$ 二次项。原文全文本轮未取得，不声称核查全部证明 |
| Kobayashi，*p-Adic Height Pairing on Abelian Varieties at Non-ordinary Primes* (2014)，[出版页面](https://link.springer.com/chapter/10.1007/978-3-642-55245-8_9) | 摘要为非 ordinary 高度的构造、与 Zarhin/Nekovář 高度比较及 Gross–Zagier 的推广 | 构造高度不等于证明其 rank $2$ 非退化；只核对了出版摘要 |
| Burungale–Kobayashi–Ota，*p-adic L-functions and rational points on CM elliptic curves at inert primes*，JIMJ 23 (2024), 1417–1460，[全文](https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/padic-lfunctions-and-rational-points-on-cm-elliptic-curves-at-inert-primes/7F847A218FE1F6DBB390CC0279089C34) | Theorem 1.1 在 root number $-1$ 设置构造点，非 torsion 当且仅当解析秩 $1$；Theorems 4.3–4.4、Proposition 4.16 保留 rank $1$ 的非零条件 | 惰性 Euler 系统及特征插值没有自动给固定 rank $2$ 曲线在无穷多个 $p$ 的二次项非零 |
| Castella–Wan，*Perrin-Riou's main conjecture for elliptic curves at supersingular primes*，Math. Ann. 389 (2024), 2595–2636，[作者文本](https://web.math.ucsb.edu/~castella/Perrin-Riou.pdf) | Theorem A 对 semistable $E$、$p>3$ 给 Selmer 余秩 $1$ 的 $p$-converse；Theorem C 在其广义 Heegner、局部与平方自由导子条件下给 signed 反 cyclotomic 主猜想 | $E_{17}$ 不满足 semistable / squarefree 条件；即使推广，余秩 $1$ 输入不适用于本题，非 torsion 的 Iwasawa 类也可在增广点消失 |
| Katharina Müller，*An asymptotic formula for Tate–Shafarevich groups of CM elliptic curves at supersingular primes*，CMB，2025-11-13 在线，[出版全文](https://doi.org/10.4153/S0008439525101446)，[arXiv](https://arxiv.org/abs/2504.05734) | §2 全文约定每层 $\Sha(E/K_n)$ 有限；Theorems 1–2 另假设相应 fine Selmer 因子有限，研究固定 $p$ 的反 cyclotomic 层数渐近 | 不能反用该渐近式证明它已经假定的有限性；Theorem 3 也受全文约定约束 |
| Foivos Chnaras，*On the cyclotomic Iwasawa invariants of Elliptic Curves of rank one*，2025 稿，[原文](https://arxiv.org/pdf/2502.16910) | Theorem 1.3 是 rank $1$ 数值判据，假设 $p\nmid C_E\#\Sha$ 及其 Conjecture 1.1；§7 的跨素数断言标为猜想/启发式 | 不可把条件数值判据当成 rank $2$ 或无条件的无穷素数结果；本文不以该稿为证明输入 |
| Castella–Liu–Wan，*Kato's main conjecture for nonordinary modular forms*，2026-09-21 作者稿，[原文](https://web.math.ucsb.edu/~castella/CLW2.pdf) | Theorem A 受大剩余像及额外局部条件约束；Theorem B / Corollary C 的中心值应用假设 $L(f,k/2)\ne0$ | $E_{17}$ 的 CM 像不满足相关大像设置，且中心值非零应用不涵盖 rank $2$；未以这篇新稿作为输入 |

另核查 Banwait 2026 稿 *Second derivatives of $p$-adic $L$-functions and the Shafarevich–Tate group of rank-two CM elliptic curves*，[arXiv:2609.08431](https://arxiv.org/abs/2609.08431)，§§14–15。其 inert 讨论仍把 signed leading term 的比较、必要的高度控制和适用的生成函数刚性分开；没有证明本笔记的 (1.3) 对无穷多个 inert $p$ 成立。这里仅用它帮助定位问题，所有实质性推论使用上文经典定理和完整证明。

## 7. 该支线留下的可精确继续攻克的问题

1. **直接的解析目标：** 对固定 $E_{17}$，证明无穷多个 $p\equiv3\pmod4$ 满足 (1.3)。一旦得到，§1 已给不依赖高度猜想的完整结论链。
2. **高度目标：** 对无穷多个这些 $p$，排除实际 Bernardi 高度矩阵的特殊形状 $H=c\ell\ell^t$。这会给向量 regulator 非零，但单靠它仍不能忽略 leading-term 定理中的有限性或其他比较假设。若能直接证明 strict 高度 $q\ne0$，也必须说明该信息怎样非循环地约束全 Selmer 群。
3. **导出类目标：** 证明一个适当的 rank $2$ 导出类确实非零且与 strict Mordell–Weil 方向有已证明的比较。不能把 Iwasawa 模上的非零、在某个特征处的非零、或单点对数非零，直接换成其在增广点的导数非零。

这些目标保留固定曲线与无穷素数两个量词。到目前为止，这条超奇异路线提供了另一组可用的单素数证书和明确的线性代数障碍，没有消去课题完成标准中的核心缺口。
