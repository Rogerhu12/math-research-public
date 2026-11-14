# R5. 约化扭点不可能由固定有限代数点集统一抬升

**状态：已证明。** 日期：2026-11-12（UTC+8）。

本结果否定一个候选来源的中间引理；不否定该来源最终的 Sha 消失主张，更不构成本课题主目标的反例或解答。

## 1. 定理

设 $E/\mathbb Q$ 为椭圆曲线，$\ell$ 为素数，$S\subset E(\overline{\mathbb Q})$ 为有限集合。给定任意有限素数集 $B$，存在素数 $p\notin B$，满足 $p\ne\ell$ 且 $E$ 在 $p$ 处好约化，并有
$$
\widetilde E(\mathbb F_p)[\ell^\infty]\setminus\{O\}
\not\subseteq \operatorname{red}_p(S).
$$
这里约化映射由一个嵌入 $\overline{\mathbb Q}\hookrightarrow\overline{\mathbb Q}_p$ 确定，右边允许落在 $\widetilde E(\overline{\mathbb F}_p)$。事实上，可使此结论对所有这种嵌入同时成立，也可令左边所取点具有任意指定的充分大精确 $\ell$-幂阶。

## 2. 证明

先把 $S$ 替换成其全部 Galois 共轭的并集。这仍是有限集；扩大右边只会使待证不包含关系更强。令 $M=|S|$。

取整数 $n\ge1$，使
$$
\ell^{2n}-\ell^{2n-2}>M.
\tag{1}
$$
特征零下 $E[\ell^n]\simeq(\mathbb Z/\ell^n\mathbb Z)^2$，因此精确阶为 $\ell^n$ 的点数是式 (1) 左边。

考虑有限 Galois 扩张
$$
L_n=\mathbb Q(E[\ell^n])/\mathbb Q.
$$
由 Chebotarev 密度定理，完全分裂于 $L_n$ 的有理素数有正密度 $1/[L_n:\mathbb Q]$，特别地有无穷多个。删除 $B$、素数 $\ell$、曲线坏约化素数以及 $S$ 的仿射坐标在固定 Weierstrass 模型中涉及的有限多个分母素数，仍留下无穷多个可选 $p$。

固定其中任一素数 $p$。因为 $p\ne\ell$ 且好约化，约化映射
$$
E[\ell^n](\overline{\mathbb Q}_p)
\longrightarrow \widetilde E[\ell^n](\overline{\mathbb F}_p)
$$
是双射，并保持点的精确阶。可由良好整模型上的乘 $\ell^n$ 映射为有限 étale 映射得到；等价地，形式群约化核在 $\ell\ne p$ 时没有非零 $\ell$-幂扭点，而两边均有 $\ell^{2n}$ 个点。又因为 $p$ 在 $L_n$ 中完全分裂，分解群在所有 $\ell^n$-扭点上作用平凡，所以它们全部约化为 $\mathbb F_p$-有理点。

于是 $\widetilde E(\mathbb F_p)$ 中精确阶为 $\ell^n$ 的点至少有
$$
\ell^{2n}-\ell^{2n-2}>M
$$
个，而任一固定约化映射下 $S$ 的像至多有 $M$ 个。必有一个所需阶数的点不在该像中。

因为 $S$ 已取所有 Galois 共轭，改变嵌入只改变这一有限集合的排列，因此允许所有嵌入也不会增加可供约化的代数点总数。结论成立。证毕。

## 3. 推论：有限个 $y^2$ 值不可能统一抬升

设 $E$ 的短 Weierstrass 方程为
$$
y^2=x^3+Ax+B,\qquad A,B\in\mathbb Q,
$$
并设 $U\subset\mathbb Q$ 为有限集。则满足 $y(P)^2\in U$ 的仿射代数点集合 $S_U$ 有限：每个 $u\in U$ 至多对应两个 $y$ 和三个 $x$，故 $|S_U|\le6|U|$。由上节定理，不能对除有限个例外以外的所有好素数 $p$，利用 $S_U$ 抬升所有非零 $\ell$-primary 约化点。

特别地，不存在只依赖 $E,\ell$ 的常数 $C$，使这种统一抬升总可以满足
$$
y(P)^2=a/b,\qquad
a,b\in\mathbb Z,\qquad1\le|a|,|b|\le C.
$$
因为这时允许的有理数 $a/b$ 构成有限集合，直接适用上面的推论。增加任意有限多个例外素数也无济于事。

## 4. 对来源的精确影响

François Destrempes、Dmitry Malinin，*On the vanishing of almost all primary components of the Shafarevich-Tate group of elliptic curves over the rationals*，arXiv:1703.02215v2（2018 年修订）：<https://arxiv.org/abs/1703.02215v2>；核对 PDF：<https://arxiv.org/pdf/1703.02215>。

该稿 Theorem 6（式 (132)）、Remark 4 及 §3.5 构造有限域 $K'$ 的步骤，使用了上一节所排除的统一有界 $y^2$ 抬升断言。原稿另假设 $E$ 非 CM、$\ell>3$、$\ell\nmid(4A^3+27B^2)$ 和 $\ell$-进像满；这些附加假设不影响本定理的计数矛盾。

若将 Theorem 6 的常数重新解释为可以随 $p$ 增长，本定理不反驳这种较弱断言，但原稿后续固定有限 $K'$ 的步骤便不再成立。于是它仍不能推出其 Theorem 5，也不能作为本课题的完成证明。

更多局部错误的核查见 `notes/2026-11-12-destrempes-malinin-audit.md`；本文件的结论只依赖上面完整的计数论证。
