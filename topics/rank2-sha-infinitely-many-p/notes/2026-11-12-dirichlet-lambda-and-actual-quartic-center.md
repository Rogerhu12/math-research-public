# Dirichlet lambda 判据与实际四次扭曲中心的区别

日期：2026-11-12。状态：原始定理范围已核；下面角色比较和有限域去扭转论证已证明，尚未得到新的中心上界。

## 1. 新论文确实允许非平凡有限特征

Heiko Knospe，*Special values of p-adic L-functions and Iwasawa
$\lambda$-invariants of Dirichlet characters*，Research in Number Theory
**12** (2026)，article 76，
[出版 DOI](https://doi.org/10.1007/s40993-026-00762-x)；
[作者版本](https://arxiv.org/pdf/2401.06100)，v3，2026-08-29。
本次核读的是第 1 节及印刷页 7–8 的 Proposition 3.1、Theorem 3.2。

其输入为非平凡偶 Dirichlet 特征 $\chi=\theta\omega^i$，
$\theta$ 的导子与 $p$ 互素。因此不能将论文简单描述为“只处理平凡
特征”；导子含 $17$ 的有限 Dirichlet 特征也在范围内。

平凡零情形准确为
$$
\chi=\theta\omega,\qquad\theta(-1)=-1,\qquad\theta(p)=1.
$$
此时 Ferrero–Greenberg 给中心简单零。Theorem 3.2(i) 给
$$
\lambda_p(\chi)>1
\iff v_pL_p'(0,\chi)>1
\iff v_pL_p(1,\chi)>1
\iff v_pB_{p,\theta}>2.
\tag{1}
$$
第二部分是进一步判别 $\lambda_p(\chi)>2$ 的逐 $p$ 临界值公式。
它没有证明固定特征时这些估值对无穷 $p$ 有所需统一上界；
分布部分给预测与计算。原证明中的 Bernoulli 符号不影响 (1) 的估值陈述。

本题所需的下一步是把**实际** CM 角色、中心和局部条件映到这个
Dirichlet 对象。仅将符号 $\lambda$ 或“导子 $17$”对上不够。

## 2. 实际有限四次角色不是 Dirichlet 角色的限制

令 $K=\mathbb Q(i)$、$\alpha>0$ 满足 $\alpha^4=17$，并令
$$
L=K(\alpha),\qquad E_{17}:y^2=x^3-17x,\qquad E_0:y^2=x^3-x.
$$
固定与 CM 作用交换的同构
$$
\iota:E_{17,L}\longrightarrow E_{0,L},\qquad
(x,y)\longmapsto(x/\alpha^2,y/\alpha^3).
\tag{2}
$$
对 $\sigma\in G_K$，设 $u_\sigma=\sigma(\alpha)/\alpha\in\mu_4$。
椭圆曲线上的 CM 自同构为
$[u](x,y)=(u^2x,u^3y)$，因而
$$
{}^\sigma\iota=[u_\sigma]\iota.
$$
在 $\mathfrak p$-adic CM 直线上以 (2) 识别两表示，得到
$$
\rho_{17,\mathfrak p}
 =\epsilon_{17}\rho_{0,\mathfrak p},
\qquad
\epsilon_{17}(\sigma)=\frac{\alpha}{\sigma(\alpha)}.
\tag{3}
$$
这里的逆向可直接由
$\rho_{0,\mathfrak p}(\sigma)\iota
=[u_\sigma]\iota\rho_{17,\mathfrak p}(\sigma)$ 检验。

取 $\tau\in\operatorname{Gal}(L/K)$ 为 $\tau(\alpha)=i\alpha$。
复共轭 $c$ 固定 $\alpha$ 而送 $i$ 到 $-i$，所以
$$
c\tau c^{-1}=\tau^{-1},\qquad
\epsilon_{17}^{\,c}=\epsilon_{17}^{-1}\ne\epsilon_{17}.
\tag{4}
$$
反之，任何 $G_{\mathbb Q}$ 的一维特征 $\theta$ 的限制都满足
$$
(\theta|_{G_K})^c=\theta|_{G_K},
$$
因为一维表示中的共轭不改变其值。因此实际 $\epsilon_{17}$ 不是
任何 Dirichlet 特征限制到 $G_K$ 后的角色。
同样结论也可由 $L/\mathbb Q$ 的二面体 Galois 群看出。

尤其，模 $17$ 的四次 Dirichlet 特征与 (3) 不是同一对象。
二者在某个局部单位群上出现四次特征，不给全局角色的等同。
本节只排除这个直接识别；不排除另行构造的诱导表示、对应或比较定理。

## 3. 即使扩大有限角色范围，仍须保留 CM 的无限部分

本题中心商 $D_p$ 来自完整的 $\rho_{17,\mathfrak p}$。
它并不只取有限角色 $\epsilon_{17}$。采用
$\operatorname{HT}(\mathbb Q_p(1))=1$ 的约定，在 $p$ 的两个
$K$-嵌入上，CM 直线的 Hodge–Tate 权为
$$
(1,0)
$$
（交换 CM 型则为 $(0,1)$）。有限 Artin 角色乘同一个 Tate 扭曲
$\mathbb Q_p(r)$ 的权则为
$$
(r,r).
$$
有限扩域不改变这个差异；同时加 Tate 扭曲也不改变两权之差。
所以扩大 Knospe 定理中的有限角色集合，并不能自动把完整 CM 表示
或其中心 Selmer 条件变成 Dirichlet–Tate 情形。

这还解释了为何 R82 的权一 Eisenstein 分解不能直接调用 (1)：
R82 证明的是固定 cusp $q$-展开的有限 Dirichlet 分解；
实际中心系数还经过 CM 点的 Gauss–Manin 微分与周期规范。
未构造一个保留这些操作、完整 Galois 表示和局部条件的映射之前，
不能把所选中央理想认作某个 Kubota–Leopoldt 中心理想。

## 4. 对旧有限域点数判据的一个具体补充

Stokes，*On CM Elliptic Curves and the Cyclotomic
$\lambda$-Invariants of Imaginary Quadratic Fields*，
Journal of Number Theory **256** (2024)，160–169，
[作者版本](https://arxiv.org/pdf/2302.09594)，Theorems 1.4、1.6。
其 Gold 型判据已在
[局部饱和笔记 §5](2026-11-12-elliptic-unit-local-saturation.md)
核定；这里不重复旧审计，只补准确的去扭转计算。

设 $p\equiv1\pmod4$，$q=p^{p-1}$。则
$$
\frac{q-1}{p-1}=1+p+\cdots+p^{p-2}\equiv p-1\equiv0\pmod4.
\tag{5}
$$
对于任意 $D\in\mathbb F_p^\times$，因为 $4(p-1)\mid q-1$，有
$D^{(q-1)/4}=1$。循环群 $\mathbb F_q^\times$ 中这准确等价于
$D$ 是四次方。因此
$$
E_D:y^2=x^3-Dx
\quad\text{与}\quad E_0:y^2=x^3-x
$$
在 $\mathbb F_q$ 上同构，所有这些四次扭曲在这个域上的点数相同。
这里扩域次数确为 $p-1$，不能换成 $\mathbb F_p$ 后使用 Hasse 界。

所以同一个 $\mathbb F_{p^{p-1}}$ 点数判据不能自行辨认 (3) 的
非平凡四次角色中心。它即便给某个平凡角色分支的信息，也没有给
实际 $D_p$ 的剩余核上界。

## 5. 此来源分支的结论

已发表 Dirichlet 论文的范围比“平凡角色”广，但上述两处实际差别仍在：
有限四次角色反共轭，而完整 CM 表示还具有非平行 Hodge–Tate 权。
本文没有得到 $N_p$ 对无穷 $p$ 有限，也不把来源未提供一个比较定理
解释为不存在任何这样的比较。此来源的直接应用已核清；后续应回到
实际 $17$-特征中心核或真正的固定候选覆盖。
