# R172：一阶闭乘子的自然幂、固定图核心与标量算子多项式谱

日期：2026-11-12（UTC）。作者：critical_kernel。根代理预留 R172。

状态：完整证明。本文的 $q(X)$ 是闭一阶算子的自然算子多项式；它一般不等于点态向量 $q(u)$ 的乘子，后者仍有 Bell 修正及未解共振。

## 1. 设置与结论

设

$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
0\ne a\in\ell^2,
$$

令 $X=X_u$ 为 R125 的实际闭一阶乘子。R161 已证明

$$
\operatorname{Dom}X=\operatorname{Dom}X^*
\tag{1.1}
$$

及某个有界自伴 $C_a$ 满足

$$
\|Xx\|^2-\|X^*x\|^2
=\langle C_ax,x\rangle
\qquad(x\in\operatorname{Dom}X).
\tag{1.2}
$$

这里只使用准确的共同域二次型式，不把两个无界二次乘积的定义域自动认作相同。记 $c=\|C_a\|$。

**主结论。**

1. 每个自然幂 $X^p$ 都是闭、稠密定义的算子。
2. 对任意次数 $p\ge1$ 的标量多项式 $q$，自然 $q(X)$ 在准确域 $\operatorname{Dom}X^p$ 上闭。其图范数与 $X^p$ 的图范数等价。
3. R128/R140 的每个固定共同正则器 $R(t)$ 满足：$R(t)^pH$ 是 $X^p$ 及 $q(X)$ 的图核心。该结论也适用于任意闭 $A$ 不变限制。
4. 每个 $q(X)-\lambda I$ 在全 $H$ 上单射且值域稠密。其谱由 R138 的第一阶三分精确决定：

$$
\boxed{
\sigma(q(X))=
\begin{cases}
\{q(a_*+\sum_ja_j)\},&a\in\ell^1,\\
\varnothing,&a\notin\ell^1\text{ 且存在可和相位缺陷方向},\\
\mathbb C,&a\notin\ell^1\text{ 且没有可和相位缺陷方向}.
\end{cases}}
\tag{1.3}
$$

非空谱全部是连续谱。限制上的谱满足多项式谱映射，但本稿不由全空间分类推断未知限制的第一阶谱。

## 2. 共同伴随域给离散插值不等式

先在任意满足 (1.1)—(1.2) 的闭算子上作计算。若 $x\in\operatorname{Dom}X^2$，则 $Xx\in\operatorname{Dom}X^*$，所以

$$
\|Xx\|^2=|\langle X^*Xx,x\rangle|.
$$

在向量 $Xx$ 上使用 (1.2)，得到

$$
\|X^*Xx\|^2
\le\|X^2x\|^2+c\|Xx\|^2.
$$

因此

$$
\|Xx\|^2
\le\|x\|\bigl(\|X^2x\|^2+c\|Xx\|^2\bigr)^{1/2}
\le\|x\|\|X^2x\|+\sqrt c\,\|x\|\|Xx\|.
\tag{2.1}
$$

对 $x\in\operatorname{Dom}X^p$，记

$$
a_k=\|X^kx\|,\qquad 0\le k\le p.
$$

将 (2.1) 用于 $X^{k-1}x$，再用 Young 不等式，给

$$
\boxed{
a_k^2\le2a_{k-1}a_{k+1}+c\,a_{k-1}^2
\qquad(1\le k\le p-1).
}
\tag{2.2}
$$

所有向量都属于所需的实际域，因为 $x$ 已在自然 $p$ 次幂域中。

### 2.1 一个自含的有限序列最大值论证

设 $p\ge2$，置

$$
\beta_k=2^{k(p-k)},\qquad
R\ge R_0:=\max\{1,2^{p+1}\sqrt c\}.
$$

考虑有限序列 $a_k/(R^k\beta_k)$ 的最大值。若一个正最大值在内部指标 $k$ 取得，则 (2.2) 给

$$
1\le
2\frac{\beta_{k-1}\beta_{k+1}}{\beta_k^2}
+\frac c{R^2}\left(\frac{\beta_{k-1}}{\beta_k}\right)^2.
\tag{2.3}
$$

但

$$
\frac{\beta_{k-1}\beta_{k+1}}{\beta_k^2}=\frac14,
\qquad
\left(\frac{\beta_{k-1}}{\beta_k}\right)^2
=2^{4k-2p-2}\le2^{2p}.
$$

所以右侧至多 $1/2+1/4<1$，矛盾。最大值必在端点取得。由 $\beta_0=\beta_p=1$，

$$
\boxed{
\|X^kx\|
\le\beta_k\bigl(R^k\|x\|+R^{k-p}\|X^px\|\bigr)
\quad(0\le k\le p).
}
\tag{2.4}
$$

当 $1\le k<p$，令 $R$ 足够大即可得到任意小的最高幂相对系数：对每个 $\varepsilon>0$，存在有限 $C_{\varepsilon,p,k}$，使

$$
\boxed{
\|X^kx\|
\le\varepsilon\|X^px\|
+C_{\varepsilon,p,k}\|x\|
\quad(x\in\operatorname{Dom}X^p).
}
\tag{2.5}
$$

$p=1$ 没有内部低阶需要处理。

## 3. 自然幂与标量多项式都闭

**命题3.1。** 每个自然幂 $X^p$ 闭。

证明：设 $x_n\to x$、$X^px_n\to y$，其中 $x_n\in\operatorname{Dom}X^p$。对 $x_n-x_m$ 使用 (2.4)，知每个 $X^kx_n$（$k<p$）都 Cauchy。依次使用 $X$ 的闭性，

$$
x\in\operatorname{Dom}X,\quad
Xx=\lim Xx_n,\quad\ldots,\quad
x\in\operatorname{Dom}X^p,\quad X^px=y.
$$

证毕。此闭性计算本身不预设 $\operatorname{Dom}X^p$ 稠密；稠密性将在 §4 由实际正则器给出。

令

$$
q(z)=q_pz^p+\cdots+q_0,\qquad q_p\ne0,
$$

并在 $\operatorname{Dom}X^p$ 上定义自然多项式

$$
q(X)x=\sum_{k=0}^pq_kX^kx.
\tag{3.1}
$$

由 (2.5)，所有低阶项之和相对 $X^p$ 的界可以任意小。于是存在 $C_1,C_2>0$，使

$$
C_1(\|x\|+\|X^px\|)
\le\|x\|+\|q(X)x\|
\le C_2(\|x\|+\|X^px\|).
\tag{3.2}
$$

因此

$$
\boxed{
q(X)\text{ 在 }\operatorname{Dom}X^p\text{ 上闭}.
}
\tag{3.3}
$$

同一论证适用于 $q(X)-\lambda I$，且其域仍严格等于 $\operatorname{Dom}X^p$。

这里没有假定高次自然幂本来已经闭，也没有把自然多项式的域擅自扩大为某个最大形式域。

## 4. 实际共同正则器的高次域

本节明确使用 [R128](../results/R128-first-chaos-invariant-parts-and-resolvent-regularization.md) §7 和 [R140](../results/R140-invariant-subquotient-type-and-fixed-first-regularization.md) §7 的具体结论。

把 $a$ 写成四个非负 $\ell^2$ 系数列的复线性组合。对它们的增生闭乘子取

$$
R_\nu(t)=(I+tX_{b_\nu})^{-1},\qquad
R(t)=\prod_{\nu=1}^4R_\nu(t),\qquad t>0.
\tag{4.1}
$$

零分量取恒等算子。这些算子均为收缩、单射、有稠密值域的有界交换子；其有限乘积也单射稠密。并有

$$
R(t)\to I\text{ 强},\qquad
\operatorname{Ran}R(t)\subseteq\operatorname{Dom}X,
\qquad
S(t):=XR(t)\in\{A\}'\subseteq B(H).
\tag{4.2}
$$

R125/R128 的完整域交换给

$$
R(t)\operatorname{Dom}X\subseteq\operatorname{Dom}X,\qquad
XR(t)x=R(t)Xx.
\tag{4.3}
$$

特别 $S(t)R(t)=R(t)S(t)$：对任意 $h$，在 $R(t)h\in\operatorname{Dom}X$ 上应用 (4.3)，即可得到该有界恒等式。

固定 $t$，简记 $R=R(t)$、$S=S(t)$。由 (4.2)—(4.3) 归纳，

$$
\boxed{
R^pH\subseteq\operatorname{Dom}X^p,\qquad
X^kR^p=S^kR^{p-k}\quad(0\le k\le p).
}
\tag{4.4}
$$

归纳中的域依据可直接写出：$XR^ph=R^{p-1}Sh$；右侧按前一步属于 $\operatorname{Dom}X^{p-1}$。因此左侧输入确在自然 $p$ 次幂域中。

$R^p$ 是稠密值域的有界算子，所以 (4.4) 同时证明

$$
\overline{\operatorname{Dom}X^p}=H.
\tag{4.5}
$$

## 5. 每个固定 $R(t)^pM$ 都是图核心

令 $M$ 是任意闭 $A$ 不变空间。R128 已给

$$
X(\operatorname{Dom}X\cap M)\subseteq M.
$$

因此自然限制的高次域准确为

$$
\operatorname{Dom}X_M^p=\operatorname{Dom}X^p\cap M,\qquad
X_M^p=X^p|_{\operatorname{Dom}X^p\cap M}.
\tag{5.1}
$$

R140 的实际预解比例恒等式为

$$
R(s)=R(t)U(s,t),
\tag{5.2}
$$

其中 $U(s,t)$ 是有界交换单位，且它及其逆保持每个 $M$。所有因子交换，所以

$$
\boxed{R(s)^pM=R(t)^pM\qquad(s,t>0).}
\tag{5.3}
$$

对 $x\in\operatorname{Dom}X_M^p$，有

$$
R(s)^px\longrightarrow x,
\qquad
X^pR(s)^px=R(s)^pX^px\longrightarrow X^px
\quad(s\downarrow0).
\tag{5.4}
$$

这里强收敛来自收缩 $R(s)\to I$；域交换可对自然幂逐次使用。每个逼近向量由 (5.3) 都在同一个固定 $R(t)^pM$ 中。

所以

$$
\boxed{
R(t)^pM\text{ 是 }X_M^p\text{ 的图核心},
}
\tag{5.5}
$$

再由 (3.2)，它也是 $q(X_M)$ 的图核心。自然幂和这些自然多项式在 $M$ 中均闭、稠密定义。

本节不宣称有限柱与未知 $M$ 有非零交，也不需要有限柱本身已经是高次幂的图核心。

## 6. 真算子多项式的单射与全空间稠密值域

固定 $\lambda\in\mathbb C$，在标量域中分解

$$
q(z)-\lambda=q_p\prod_{i=1}^p(z-\mu_i),
\tag{6.1}
$$

允许重根。由于 $a\ne0$，R125 给每个 $X-\mu_iI$ 单射且值域稠密。

自然有限乘积在 $\operatorname{Dom}X^p$ 上恰为 $q(X)-\lambda I$。若其值为零，从最左侧因子起逐次用单射性消去，便得到输入为零；每一步的输入都在该因子的域内。因此

$$
\ker(q(X)-\lambda I)=0.
\tag{6.2}
$$

证明稠密像时使用固定正则器，不以一个未经引用的 $q(X)1$ 循环结论替代。

令

$$
S_{\mu_i}=(X-\mu_iI)R=S-\mu_iR.
$$

它们有界且两两交换。R140 的固定 $RH$ 是 $X$ 的图核心，也当然是 $X-\mu_iI$ 的图核心；所以

$$
\overline{\operatorname{Ran}S_{\mu_i}}
=\overline{\operatorname{Ran}(X-\mu_iI)}=H.
\tag{6.3}
$$

每个 $S_{\mu_i}$ 还单射，因为 $R$ 和 $X-\mu_iI$ 都单射。

由 (4.4) 的真实高次域，

$$
\boxed{
(q(X)-\lambda I)R^p
=q_p\prod_{i=1}^pS_{\mu_i}.
}
\tag{6.4}
$$

有界稠密值域算子的有限乘积仍有稠密值域。于是 (6.4) 给

$$
\boxed{
\overline{\operatorname{Ran}(q(X)-\lambda I)}=H.
}
\tag{6.5}
$$

这是全空间结论；它没有把 R125 的全空间稠密性传到任意未知限制。

### 6.1 限制稠密性的准确等价

在任意非零 $M$ 上，(5.5) 和 (6.4) 给

$$
\overline{\operatorname{Ran}(q(X_M)-\lambda I)}
=\overline{\left(\prod_{i=1}^pS_{\mu_i}\right)M}.
\tag{6.6}
$$

由于有界 $S_{\mu_i}|_M$ 交换，该有限乘积在 $M$ 中稠密，当且仅当每个因子在 $M$ 中稠密。再用固定 $RM$ 图核心，

$$
\boxed{
\overline{\operatorname{Ran}(q(X_M)-\lambda I)}=M
\ \Longleftrightarrow\
\overline{\operatorname{Ran}(X_M-\mu_iI)}=M
\text{ 对全部根 }\mu_i.
}
\tag{6.7}
$$

反向的必要性使用乘积像包含于每个因子的像；充分性使用有界稠密像乘积的稠密性。一般复杂第一阶限制的右侧仍可能未知，本稿不将它写成无条件成立。

## 7. 多项式谱映射与真实预解域

对每个非零闭 $A$ 不变 $M$，

$$
\boxed{\sigma(q(X_M))=q(\sigma(X_M)).}
\tag{7.1}
$$

以下直接证明，避免对未核对定义域的无界多项式演算引用一般谱映射口号。

若 (6.1) 的全部 $\mu_i$ 都在 $\rho(X_M)$，其有界全域逆两两交换，并保持 $X_M$ 的域。逐个预解式使自然幂域增加一阶，所以它们的乘积把 $M$ 送入 $\operatorname{Dom}X_M^p$。逐因子验证得到

$$
(q(X_M)-\lambda I)^{-1}
=q_p^{-1}\prod_{i=1}^p(X_M-\mu_iI)^{-1}.
\tag{7.2}
$$

反向，假设 $\lambda\in\rho(q(X_M))$，令全域有界逆为 $G$。它的像在准确域 $\operatorname{Dom}X_M^p$ 中。取任一根 $\mu$，写

$$
q(z)-\lambda=(z-\mu)Q_\mu(z).
$$

$Q_\mu(X_M)$ 已由 §3、§5 证明闭（次数0时为有界常数）。因此复合

$$
Q_\mu(X_M)G
$$

全域且闭：若 $h_n\to h$、复合值趋于 $y$，则 $Gh_n\to Gh$，由 $Q_\mu(X_M)$ 闭性知复合值在 $h$ 处等于 $y$。闭图定理给它有界。

又因 $G(M)\subseteq\operatorname{Dom}X_M^p$，该复合的像包含于 $\operatorname{Dom}X_M$，且

$$
(X_M-\mu I)Q_\mu(X_M)G=I_M.
\tag{7.3}
$$

$X_M-\mu I$ 是全空间单射算子的限制，所以单射；(7.3) 给满射，故 $\mu\in\rho(X_M)$。这对全部根成立。

于是

$$
\lambda\in\rho(q(X_M))
\Longleftrightarrow
q^{-1}(\{\lambda\})\subseteq\rho(X_M),
$$

等价于 (7.1)。

这证明的是每个限制自身的谱映射。它没有说明 $\sigma(X_M)$ 与 $\sigma(X)$ 相等。

## 8. 全空间的完整三分

对 $Q=H$，R138 已给第一阶谱分类。写

$$
\mathcal D(a,\theta)
=\sum_j\bigl(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\bigr).
$$

### 8.1 $a\in\ell^1$

此时 $X\in\mathcal A$ 有界，且

$$
\sigma(X)=\{c_0\},\qquad c_0=a_*+\sum_ja_j.
$$

由 §7，

$$
\sigma(q(X))=\{q(c_0)\}.
$$

§6 给该点处单射、稠密而非满射，所以它是连续谱点。

### 8.2 $a\notin\ell^1$，存在 $\mathcal D(a,\theta)<\infty$

R138 给 $\sigma(X)=\varnothing$。§7 或逐根式 (7.2) 给

$$
\sigma(q(X))=\varnothing.
$$

这里空谱与自然高次域、闭性完全相容。预解算子由有限个真实一阶预解式的有界乘积构成。

### 8.3 $a\notin\ell^1$，所有相位缺陷均不可和

R138 给 $\sigma(X)=\mathbb C$。因为非恒定复多项式映满 $\mathbb C$，§7 给

$$
\sigma(q(X))=\mathbb C.
$$

由 §6，每个谱参数处仍单射、值域稠密；若满射，闭图定理会给有界逆，与谱点矛盾。因此全部为连续谱。

本节将自然算子多项式的谱完整化，并没有把它当成点态符号多项式的谱分类。

## 9. 与点态多项式及共振缺口的区分

R134/R144 的点态多项式 $q(u)$ 需要实际 Bell 修正。例如平方向量的实际乘子涉及

$$
X^2+B_2,\qquad
B_2=\sum_ja_j^2(I-V_j^2),
$$

而不是只含 $X^2$。本稿的 (1.3) 不删除这个有界修正。

因此以下推断均未作出：

- 没有从 $q(X)$ 的单射稠密推断所有点态 $q(u)$ 循环；
- 没有宣布慢平方共振 $u^2-a_{j_0}^2$ 已排核；
- 没有声明所有高次多项式都自动 $C$ 自伴；
- 没有把全空间连续谱传到任意未知限制。

R161 的共同伴随域及有界二次型给自然幂的实际闭性；R128/R140 的固定正则化给稠密域、图核心及有限因子像。两类输入分别承担不同工作，没有以形式域运算替代其中任一步。

完整 Hilbert 不变子空间问题仍未解决。
