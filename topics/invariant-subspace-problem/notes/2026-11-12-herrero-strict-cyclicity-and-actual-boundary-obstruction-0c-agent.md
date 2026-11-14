# Herrero 严格循环路线与实际负整数边界的反证检查

日期：2026-11-12（UTC）。作者：l2_moments。状态：完整自含估计及原始文献核对；不另占正式结果号。

本文证明 R174 的实际边界前移 $S=B^*$ 及它的每个坐标尾限制都不是严格循环算子。这个结论只排除一条文献中的充分条件，不判定 $B$ 或 $S$ 是否 unicellular。

## 1. 原始论文及准确适用范围

Domingo A. Herrero, *A unicellular universal quasinilpotent weighted shift*, Proceedings of the American Mathematical Society **110** (3), 649–652, 1990.

- DOI：[10.1090/S0002-9939-1990-1023343-3](https://doi.org/10.1090/S0002-9939-1990-1023343-3)。
- [原论文四页扫描](https://scispace.com/pdf/a-unicellular-universal-quasinilpotent-weighted-shift-1e0ll2qhb4.pdf)。

论文第649页构造的是特殊拼接权列，并非本课题的二进位 ruler 权。第650页先证明该前移及每个坐标尾限制严格循环；第651页说明由这些条件推出 unicellularity 的论证来自 Gellar。原文也证明其各正次幂非紧，所以“幂非紧”本身不能否定 unicellularity。

本课题不能把特殊权的估计或严格循环假设直接移植过来。下面对实际权逐项检验，得到相反的严格循环结论。

## 2. 实际边界、尾空间与归一化幂

沿用 R174 的负整数边界表示。在 $\ell^2(\mathbb N_0)$ 上，

$$
Be_0=0,\qquad
Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1).
$$

令 $S=B^*$，则

$$
Se_n=\alpha_{v_2(n+1)}e_{n+1}.
$$

记

$$
W_n=\prod_{\ell=1}^n\alpha_{v_2(\ell)},\qquad
d_j=W_{2^j}.
$$

R174 给 $\|B^n\|=\|S^n\|=W_n$，而无进位乘积恒等式为

$$
W_n=\prod_{j:\,n_j=1}d_j.
\tag{2.1}
$$

固定 $r\ge0$，令

$$
H_r=\overline{\operatorname{span}}\{e_n:n\ge r\},\qquad
S_r=S|_{H_r}.
$$

这是前移的真实闭不变限制。$\|S_r^n\|\le W_n$，故 $S_r$ 拟幂零。向量 $e_r$ 普通循环，因为

$$
S_r^n e_r=\frac{W_{r+n}}{W_r}e_{r+n},
$$

且所有权严格正。

取 $j$ 满足 $2^j>r$，此时 $r+2^j$ 没有二进位进位。由 (2.1)，

$$
\boxed{
\frac{S_r^{2^j}}{d_j}e_r=e_{r+2^j}.
}
\tag{2.2}
$$

这是实际权的精确恒等式，不是纯模型近似。

## 3. 同一个多项式的向量范数与算子范数分离

在负整数表示中，二进制位 $1$ 表示相对于全物理 $1$ 真空的一个孔。令 $F_j$ 为第 $j$ 位的纯孔创建算子：

$$
F_je_n=
\begin{cases}
e_{n+2^j},&n_j=0,\\
0,&n_j=1.
\end{cases}
$$

R44/R174 的实际归一化幂估计，在这个忠实 UHF 表示及取伴随后给

$$
\boxed{
\left\|\frac{S^{2^j}}{d_j}-F_j\right\|
\le\eta_j.
}
\tag{3.1}
$$

由于 $F_j$ 只增加整数指标，它也保持每个 $H_r$。所以 (3.1) 可直接限制到 $H_r$，不需要压缩后交换任何未保持空间的算子。

取整数 $J_0$ 使 $2^{J_0}>r$，并令

$$
J_m=\{J_0,J_0+1,\ldots,J_0+m-1\},\qquad
Q_m=\frac1{\sqrt m}\sum_{j\in J_m}\frac{S_r^{2^j}}{d_j}.
\tag{3.2}
$$

由 (2.2)，这些像是不同正交基向量，因此

$$
\boxed{\|Q_m e_r\|=1.}
\tag{3.3}
$$

另一方面，取单位向量

$$
v_m=2^{-m/2}
\sum_{F\subseteq J_m}e_{\,r+\sum_{j\in F}2^j}\in H_r.
\tag{3.4}
$$

低位 $r$ 与 $J_m$ 不交，故没有进位。对每个 $j\in J_m$，恰有一半求和项的该位为空，因而

$$
\langle F_jv_m,v_m\rangle=\frac12.
$$

由 (3.1)，

$$
\begin{aligned}
\|Q_m\|
&\ge|\langle Q_mv_m,v_m\rangle|\\
&\ge\frac{\sqrt m}{2}
-\frac1{\sqrt m}\sum_{j\in J_m}\eta_j.
\end{aligned}
\tag{3.5}
$$

本课题 $\sum_j\eta_j<\infty$，于是

$$
\boxed{\|Q_m\|\longrightarrow\infty,\qquad \|Q_m e_r\|=1.}
\tag{3.6}
$$

这已经是本题真实算子的范数反证。它不仅是某个已知充分判据未能验证。

## 4. 首向量不是严格循环向量

记

$$
\mathcal A_r=\overline{\mathbb C[I,S_r]}^{\|\cdot\|}.
$$

严格循环的定义是存在 $h\in H_r$，使 $\mathcal A_rh=H_r$，其中没有再取向量闭包。

若 $e_r$ 严格循环，则有界评价映射

$$
\Phi_r:\mathcal A_r\to H_r,\qquad T\mapsto Te_r
$$

满射。它也单射：若 $Te_r=0$，交换性给 $TS_r^ne_r=0$ 对全部 $n$；这些向量张成稠密空间，故 $T=0$。

由有界逆定理，存在 $C_r<\infty$ 使

$$
\|T\|\le C_r\|Te_r\|\qquad(T\in\mathcal A_r).
$$

将 $T=Q_m$ 代入，与 (3.6) 矛盾。因此 $e_r$ 不严格循环。

## 5. 实际上不存在任何严格循环向量

还需排除别的 $h$；只证明 $e_r$ 失败不能省略这一步。

$\mathcal A_r$ 是由一个拟幂零算子生成的交换含幺 Banach 代数，因此它只有一个字符 $\chi_r$，满足

$$
\chi_r(p(S_r))=p(0).
$$

具体而言，任意字符都必须把 $S_r$ 送到其 Banach 代数谱 $\{0\}$；再由多项式范数稠密性，字符唯一。对每个 $T\in\mathcal A_r$，其第 $r$ 坐标为

$$
(Th)_r=\chi_r(T)h_r.
\tag{5.1}
$$

该式先对多项式成立，再由范数逼近传到 $\mathcal A_r$。且 $\chi_r(T)\ne0$ 当且仅当 $T$ 是 $\mathcal A_r$ 中的单位。

假设某个 $h$ 严格循环。则存在 $T\in\mathcal A_r$ 使 $Th=e_r$。式 (5.1) 给

$$
\chi_r(T)h_r=1.
$$

所以 $T$ 为单位，$h=T^{-1}e_r$。对任意 $x\in H_r$，严格循环性给 $D\in\mathcal A_r$ 使 $x=Dh$，于是

$$
x=DT^{-1}e_r.
$$

这会使 $e_r$ 严格循环，与 §4 矛盾。综上，

$$
\boxed{
S_r\text{ 对每个 }r\ge0\text{ 都不是严格循环算子。}
}
\tag{5.2}
$$

本证明不把一般拟幂零算子的“普通循环”与“严格循环”混淆；关键是实际多项式 (3.2) 与局部代数的单位判据。

## 6. 准确的研究结论

Herrero 原论文的“每个坐标尾限制严格循环”路线不能直接用于本边界前移：本题每个这样的限制都严格地违反该假设。

这没有证明 $S$ 或 $B$ 非 unicellular。充分条件失效不能反推结论为假。仍未判定：

1. $B$ 的任意无限支持向量是否循环；
2. $B$ 是否存在真无限维闭不变空间；
3. 任意 $T\in\mathcal A$ 在边界表示中的核是否总等于由其形式首阶确定的有限根旗。

R175 已解决第3项中的真实快尾符号类；一般范数代数元素仍保留。即使未来解决整个边界格，R174 的双向无有界交织结论也表明不能自动搬到原 $H$。完整 Hilbert 不变子空间问题没有在本文解决。
