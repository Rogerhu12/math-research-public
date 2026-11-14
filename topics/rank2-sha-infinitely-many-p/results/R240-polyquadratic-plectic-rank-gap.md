# R240. 原有理秩至少二时，polyquadratic plectic 的平凡特征投影消失

**可信度：已证明。** 本文给出已发表 Fornea–Gehrmann 定理在本课题上的一个严格推论，并自证所需 norm 映射的单射性。结论针对其 polyquadratic 设置的平凡 anticyclotomic 特征和 minus 投影；不声称所有 plectic 类消失，也不证明原课题的 Sha 有限性。

## 1. 设置及全部适用假设

令 $E_0/\mathbb Q$ 为椭圆曲线，$K/\mathbb Q$ 为虚二次域，$F/\mathbb Q$ 为全实多二次 Galois 扩张，
$$
G=\operatorname{Gal}(F/\mathbb Q)\simeq(\mathbb Z/2\mathbb Z)^t,
\qquad r=[F:\mathbb Q]=2^t,\quad t\ge1.
$$
置 $L=FK$、$A=E_0\times_{\mathbb Q}F$。在下面的文献中，这些对象分别记作 $A_\circ,F_\circ=\mathbb Q,E_\circ,F,E$。

固定有理素数 $p$，令 $S$ 为 $F$ 中所有位于 $p$ 上方的素点。要求以下假设成立：

1. $p$ 在 $F$ 中完全分裂、在 $K$ 中惰性，且 $E_0$ 在 $p$ 处为乘法约化。因此 $|S|=r$，且 $A$ 在每个 $\mathfrak p\in S$ 为乘法约化。
2. $E_0$ 的导子 $N_0$ 与 $K/\mathbb Q$ 的分歧支撑不交；$N_0$ 的素因子在 $F/\mathbb Q$ 中均不分歧。
3. $F/\mathbb Q$ 每个非平凡中间扩张都分歧，且所有在 $F/\mathbb Q$ 中分歧的有限素数都在 $K$ 中分裂。
4. 写 $N_0=pN_0^\sharp N_0^\flat$，三个因子两两互素，$N_0^\sharp$ 包含且仅包含在 $K$ 中分裂的导子素因子及其全部指数。要求 $N_0^\flat$ 无平方因子，且其素因子个数为奇数。
5. $A/F$ 的导子在 $L/F$ 中不分歧。写成
   $$
   \mathfrak f_A=\Bigl(\prod_{\mathfrak p\in S}\mathfrak p\Bigr)
   \mathfrak n^\sharp\mathfrak n^\flat,
   $$
   其中各因子两两互素，$\mathfrak n^\sharp$ 包含且仅包含在 $L/F$ 中分裂的导子素因子及其全部指数。要求 $\mathfrak n^\flat$ 无平方因子，且其素因子个数与 $[F:\mathbb Q]$ 同奇偶。

这里保留第 5 条，而不把它误当成第 2–4 条的自动推论。椭圆曲线 $E_0/\mathbb Q$ 的模性及二次基变换给出所需 $A/F$ 的模性。

上述条件就是 Fornea–Gehrmann 的基本局部设置及 Assumptions 1.1、1.5、1.7 在 $F_\circ=\mathbb Q$ 下的形式。使用的**已发表来源**为：

M. Fornea–L. Gehrmann, *On the Algebraicity of Polyquadratic Plectic Points*, International Mathematics Research Notices **2023**, no. 22, 19237–19265, DOI [10.1093/imrn/rnad091](https://doi.org/10.1093/imrn/rnad091)。已核对[期刊正文](https://academic.oup.com/imrn/article/2023/22/19237/7159217?guestAccessKey=72c4670e-fac3-48db-8866-c57e26b9286c)的上述假设、Theorems A/C、Proposition 3.1、Corollary 4.4 以及 Remark 1.10；[作者预印本](https://arxiv.org/pdf/2203.15998)可辅助定位。

## 2. 命题

在第 1 节全部假设下，另假设
$$
\operatorname{rank}E_0(\mathbb Q)\ge2.
\tag{2.1}
$$
则
$$
\boxed{\operatorname{ord}_{s=1}L(E_0/L,s)\ge r+2.}
\tag{2.2}
$$

令 $\mathrm P_{A,S}$ 为上述论文中**平凡 anticyclotomic 特征**的 plectic Stark–Heegner 点。对每个 $\mathfrak p\in S$，令 $\sigma_{\mathfrak p}$ 为 $L_{\mathfrak p}/F_{\mathfrak p}$ 的非平凡自同构，并以 $a_p=+1$ 或 $-1$ 区分 $E_0/\mathbb Q_p$ 的分裂或非分裂乘法约化。所有 $a_{\mathfrak p}$ 都等于 $a_p$。置
$$
\operatorname{pr}^-_S=\prod_{\mathfrak p\in S}(1-a_p\sigma_{\mathfrak p}).
$$
则在有理化的局部完成张量积中有
$$
\boxed{\operatorname{pr}^-_S(\mathrm P_{A,S})=0.}
\tag{2.3}
$$

这里 (2.3) 比“暂时未验证非零定理的假设”更强：该具体投影确实为零。它没有说 $\mathrm P_{A,S}=0$，也没有讨论其他部分 Frobenius 符号投影或非平凡 anticyclotomic 特征。

## 3. Artin 因子的零阶至少多出二

令 $G^\vee=\operatorname{Hom}(G,\{\pm1\})$，$E_0^\eta$ 为对应的二次扭曲。因 $F$ 全实而 $K$ 为虚二次域，$F\cap K=\mathbb Q$，故 $\operatorname{Gal}(L/K)\simeq G$。

对平凡特征，Artin 分解给出
$$
L(E_0/L,s)=\prod_{\eta\in G^\vee}L(E_0^\eta/K,s).
\tag{3.1}
$$
可直接从有限群的正则表示分解证明：$\operatorname{Ind}_{G_L}^{G_K}\mathbf1$ 是各 $\eta|_{G_K}$ 的直和，将它与 $V_\ell(E_0)|_{G_K}$ 张量后，Artin formalism 给 (3.1)。只在共同好素点比较也足够：所有被删去的椭圆曲线局部 Euler 因子在 $s=1$ 非零，因此不改变零阶。论文 Corollary 4.4 和 §5 式 (17) 给出同一零阶分解。

第 1 节的假设确保每个 $\eta$ 的三元组 $(E_0^\eta,K,p)$ 均满足该论文的 generalized Heegner 假设；特别地，
$$
\varepsilon(E_0^\eta/K)=-1
\quad(\eta\in G^\vee).
\tag{3.2}
$$
这是该文 §1.2、Assumption 1.7 后的结论。由于各 $L$ 函数在中心全纯且不恒为零，(3.2) 使每个中心零阶为正奇数，因而至少为一。

平凡 $\eta=1$ 的因子不能恰为一。事实上，$E_0(\mathbb Q)\hookrightarrow E_0(K)$ 给
$$
\operatorname{rank}E_0(K)\ge2.
$$
Fornea–Gehrmann Proposition 3.1 在单素点集合 $\{p\}$、平凡特征下，使用已发表 Gross–Zagier–Kolyvagin 理论，给出
$$
\operatorname{ord}_{s=1}L(E_0/K,s)=1
\ \Longrightarrow\ \operatorname{rank}E_0(K)=1.
$$
因此该因子的零阶不为一；与其为正奇数结合，得到
$$
\operatorname{ord}_{s=1}L(E_0/K,s)\ge3.
\tag{3.3}
$$
注意这里没有使用“代数秩至少二就等于解析秩二”，也没有使用 Sha 有限性。由 (3.1)、(3.2)、(3.3)，
$$
\operatorname{ord}_{s=1}L(E_0/L,s)
\ge3+(r-1)=r+2,
$$
证明 (2.2)。

## 4. 先得到 norm 投影为零

在上述设置中，Fornea–Gehrmann Theorem A 的方向是
$$
\operatorname N_{S/p}\bigl(\operatorname{pr}^-_S\mathrm P_{A,S}\bigr)\ne0
\ \Longrightarrow\
r_{\rm alg}(A/L)=r_{\rm an}(A/L)=r.
\tag{4.1}
$$
其 Theorem C 给出更精确的等价
$$
\operatorname N_{S/p}\bigl(\operatorname{pr}^-_S\mathrm P_{A,S}\bigr)\ne0
\ \Longleftrightarrow\
\bigl(r_{\rm an}(A/L)=r\ \text{且}\ \varrho_A(S)=r\bigr),
\tag{4.2}
$$
其中 $A^+=A$、$A^-$ 是 $L/F$ 的二次扭曲，$S^+$、$S^-$ 按 $a_{\mathfrak p}=+1,-1$ 分拆，
$$
\varrho_A(S)=\max\{\operatorname{rank}A^+(F)+|S^+|,
                         \operatorname{rank}A^-(F)+|S^-|\}.
$$
式 (2.2) 使 (4.2) 右侧的第一个条件为假，所以
$$
\operatorname N_{S/p}\bigl(\operatorname{pr}^-_S\mathrm P_{A,S}\bigr)=0.
\tag{4.3}
$$
这是已证等价的直接应用；仅用 (4.1) 的正确逆否命题也足够。没有把“某个充分非零条件未验证”当成零的证明。

## 5. 单射性的域、完成及张量范畴

还不能在任意张量积上从 (4.3) 删除 norm。这里能删，是因为 $F_\circ=\mathbb Q$，故 $p$ 为底域的度一素点。

令 $K_p/\mathbb Q_p$ 为该惰性二次局部扩张。对局部点群取 pro-$p$ 完成，除去有限挠子，再有理化，记
$$
M=\widehat{E_0(K_p)}\otimes_{\mathbb Z_p}\mathbb Q_p.
$$
帽号在本文与原论文相同，指 pro-$p$ 完成的无挠部分；这里不是把抽象 $\mathbb Q$ 向量空间做未指定的无限张量完成。局部点群有有限指数的形式群开子群，形式对数在足够小的开子群上为解析同构。因此有 Galois 等变同构
$$
\log_{E_0}:M\xrightarrow{\ \sim\ }K_p
\tag{5.1}
$$
作为 $\mathbb Q_p$ 向量空间。等变性来自选用定义于 $\mathbb Q_p$ 的不变微分；有限指数和有限挠子在有理化后不影响 (5.1)。

记 $\sigma$ 为 $K_p/\mathbb Q_p$ 的非平凡自同构。其在 $K_p$ 上的正、负特征空间各为一维。因此
$$
M^-=M^{\sigma=-a_p}
$$
也是一维 $\mathbb Q_p$ 空间。由于 $p$ 在 $F$ 中完全分裂，每个 $\mathfrak p\in S$ 的局部域 $L_{\mathfrak p}$ 与 $K_p$ 相同，所有局部 minus 空间在这些自然同构下都是同一个 $M^-$。

原文 §1.3 的 norm，在有理化后正是
$$
\operatorname N_{S/p}:M^{\otimes_{\mathbb Q_p}r}
\longrightarrow\operatorname{Sym}^r_{\mathbb Q_p}M,
\tag{5.2}
$$
即局部识别后取对称商。等价地，可先在有限自由 $\mathbb Z_p$ 模上作普通张量积和对称幂，再张量 $\mathbb Q_p$。式 (5.2) 在整个空间一般不单射；例如 $x\otimes y-y\otimes x$ 属于二次对称商的核。

但它在
$$
(M^-)^{\otimes_{\mathbb Q_p}r}
\tag{5.3}
$$
上单射。证明：选非零 $e\in M^-$，该源为 $\mathbb Q_p e^{\otimes r}$；对称商把其生成元映为 $e^r$。将 $e$ 扩充为 $M$ 的基，对称代数为相应变量的多项式环，其中 $e^r\ne0$。故限制映射单射。这个证明对 $p=2$ 也成立，因为已经有理化；没有使用整系数投影算子 $\frac12(1\pm\sigma)$。

$\operatorname{pr}^-_S\mathrm P_{A,S}$ 正好位于 (5.3)，所以 (4.3) 推出 (2.3)。这同时完整解释了原文 Remark 1.10 的度一限制在此处的作用。若底域改为更大的全实域且局部次数大于一，局部特征空间未必一维，不能照搬这一步。

## 6. 对本课题的具体含义

上述已发表的高秩非零机制由多个解析秩一的 Artin 因子组成。若把一条已经有理秩至少二的曲线放在平凡因子，该因子在此根数设置中至少增加两个解析零，故其规范化 minus plectic 投影被迫消失。这一结论只排除这里明确写出的构造，未排除更高导数、其他特征或其他新类。

另外，此设置要求系数素数 $p$ 是固定 $E_0$ 的乘法坏约化素数，故即使另一个投影在某个 $p$ 非零，$p$ 也只来自一个有限集合。对本课题的 $E_{17}$ 与 $E_{34}$，还有更早的局部排除：两者 $j=1728$，在所有有限素点及其有限扩域中的赋值均非负，因而不存在乘法约化素点。理由是乘法约化经至多二次扩张成为 Tate 曲线，而 $j(q)=q^{-1}+744+\cdots$ 在 $v(q)>0$ 时满足 $v(j)=-v(q)<0$。这使用经典 Tate uniformization；可参见 J. H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, Springer, 1994, Chapter V, §3。

因此必须分清两层结论：CM 主曲线首先没有本构造所需的局部输入；对确实满足第 1 节全部假设的其他有理秩至少二曲线，(2.2)–(2.3) 进一步给出平凡特征 minus 投影的实际零结论。
