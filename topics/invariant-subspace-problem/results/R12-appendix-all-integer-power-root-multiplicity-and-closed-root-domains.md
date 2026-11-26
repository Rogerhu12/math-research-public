# 原尾全部整幂的有界根重数与闭根的真实域限制

作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127。日期：2026-11-27（台北）。

**状态：完整证明。** 对所有原尾 $B_m$、正整数 $k,p,q$（$q\ge2$）和 $\lambda\ne0$，有
$$
\boxed{
X^q=\lambda(I_k\otimes B_m^p)\text{ 存在全空间有界解 }
\quad\Longleftrightarrow\quad q\mid pk.
}
$$
根没有被预设与 $I_k\otimes B_m$ 交换。必要性使用真实奇幂恢复，先将根放进准确的有限放大尾交换子，再对深有限头的完整 Jordan 块计数。附带得到：不满足此整除的闭稳定域根，不能由任意有限整幂的整个像正则化。

本稿仍不构造普通不变子空间，也不把闭稳定域身份称作全域有界算子的通常意义下的平方根。

## 1. 已有输入及新范围

记 $K=L^2(\mathbb Z_2,\mu)$，$B_m$ 是原权 $\alpha_j=e^{-L_j}$ 的真实尾，$B_0=A$，并记
$$
\mathscr C_m=\{B_m\}',\qquad
\beta^{(m)}_n=\|B_m^n\|.
$$

[原尾有界根正文](R12-appendix-tail-root-multiplicity-and-all-invariant-projection-distances.md)已证明每个 $\mathscr C_m$ 是交换的含单位 Banach 代数，每个 $B_m$ 拟幂零，且 $I_k\otimes B_m$ 有有界 $q$ 次根当且仅当 $q\mid k$。

本稿用刚证明的[奇幂强恢复及全部幂交换子](R12-appendix-odd-power-strong-recovery-all-power-commutants-and-actual-subquotients.md)。若
$$
p=2^v s,\qquad s\text{ 奇数},\qquad d=2^v,\qquad
c=\beta^{(m)}_{d-1}>0,
$$
则
$$
B_m^p=c^s I_d\otimes B_{m+v}^{\,s},
\qquad
\{B_{m+v}^{\,s}\}'=\mathscr C_{m+v}.
\tag{1.1}
$$
此处第二式由原 Haar 空间上的一致有界强多项式恢复支付，不能仅从 $X^q=B_m^p$ 推断 $X$ 与 $B_m$ 交换。

## 2. 一个有限 Jordan 块计数

**引理 2.1。** 设复有限维 nilpotent 矩阵 $T$ 的 Jordan 块全部具有长度至少二，并且它恰有 $b$ 个 Jordan 块。若 $Z^q=T$，则 $q\mid b$。

**证明。** $Z^q$ nilpotent 意味着 $Z$ nilpotent。考虑 $Z$ 的一个长度为 $\ell$ 的 Jordan 块。

若 $\ell<q$，其 $q$ 次幂为 $\ell$ 个长度一的块，不可能出现在 $T$ 中。若 $q\le\ell<2q$，其 $q$ 次幂有恰 $q$ 个块，其中至少一个长度一，也不可能。因此每个 $Z$ 块都必须满足 $\ell\ge2q$。

对 $\ell\ge2q$，$J_\ell^q$ 的 $q$ 条余数链全部存在，每条至少长二，故它准确产生 $q$ 个 Jordan 块。把 $Z$ 的全部块加起来，$b$ 是 $q$ 的倍数。证毕。

这里不允许把长度一的剩余块丢掉；恰是其不出现迫使每个根块贡献完整的 $q$ 个块。

## 3. 全部整幂的必要整除

**定理 3.1。** 若
$$
X\in B(K^{\oplus k}),\qquad
X^q=\lambda(I_k\otimes B_m^p),\qquad \lambda\ne0,
\tag{3.1}
$$
则 $q\mid pk$。

**证明。** 根与自身的 $q$ 次幂交换，故 $X$ 与 $I_k\otimes B_m^p$ 交换。采用 (1.1) 的实际 $d$ 位头，将空间重排为 $K^{\oplus kd}$；现在 (3.1) 的目标为
$$
\lambda c^s I_{kd}\otimes B_{m+v}^{\,s}.
\tag{3.2}
$$
因 $\lambda c^s\ne0$，每个 $X$ 条目都与 $B_{m+v}^{\,s}$ 交换。奇幂恢复遂将它放进 $\mathscr C_{m+v}$。因此
$$
X\in M_{kd}(\mathscr C_{m+v}).
\tag{3.3}
$$

选 $\ell$ 使 $D=2^\ell\ge2s$，再把每个真实尾分成低 $\ell$ 位和其后尾。准确有
$$
B_{m+v}
=J_{m+v,\ell}\otimes I
+e_{0,D-1}\otimes B_{m+v+\ell},
\tag{3.4}
$$
其中 $J_{m+v,\ell}$ 是长度恰为 $D$、每条链权严格非零的加权 nilpotent Jordan 块。

每个 $\mathscr C_{m+v}$ 条目与
$$
B_{m+v}^{D}
=\beta^{(m+v)}_{D-1}I_D\otimes B_{m+v+\ell}
$$
交换，所以它的全部深尾条目均属于 $\mathscr C_{m+v+\ell}$。这个代数交换、含单位、非零，故存在一个复 Banach 代数字符 $\chi$。因 $B_{m+v+\ell}$ 拟幂零，
$$
\chi(B_{m+v+\ell})=0.
\tag{3.5}
$$

把 $\chi$ 逐条目施于 $X$，得到一个大小 $kdD$ 的复矩阵 $Z$。逐条目施字符是矩阵代数同态，所以原身份 (3.1) 准确下降为
$$
Z^q=\lambda c^s I_{kd}\otimes J_{m+v,\ell}^{\,s}.
\tag{3.6}
$$
没有对未知限制空间或未支付的商空间擅自施字符。

$J_{m+v,\ell}$ 与标准单块 $J_D$ 相似。$D\ge2s$ 保证 $J_D^s$ 恰有 $s$ 条余数链，且每条链长度至少二。因此 (3.6) 右侧准确有
$$
kd\,s=kp
$$
个 Jordan 块，每个长度至少二。非零标量 $\lambda c^s$ 不改变这些长度。引理 2.1 给 $q\mid kp$，证毕。

## 4. 全部整幂的充分构造

**定理 4.1。** 若 $q\mid pk$，则 (3.1) 有全空间有界解。

**证明。** 令
$$
g=\gcd(p,q),\qquad d_0=q/g.
$$
则 $q\mid pk$ 等价于 $d_0\mid k$。把 $K^{\oplus k}$ 分成 $k/d_0$ 个 $K^{\oplus d_0}$ 块。在每个块上取有界 companion 算子
$$
C_{d_0}(B_m)(x_0,\ldots,x_{d_0-1})
=(B_mx_{d_0-1},x_0,\ldots,x_{d_0-2}).
$$
当 $d_0=1$ 时它就是 $B_m$。令 $C$ 为这些 companion 的有限直和，则
$$
C^{d_0}=I_k\otimes B_m.
\tag{4.1}
$$
任取复标量 $\rho$ 满足 $\rho^q=\lambda$，定义
$$
X=\rho C^{p/g}.
\tag{4.2}
$$
它有界，且
$$
X^q
=\lambda C^{pq/g}
=\lambda(C^{q/g})^p
=\lambda(I_k\otimes B_m)^p
=\lambda(I_k\otimes B_m^p).
$$
这付清了所有标量、幂次及有限重数。证毕。

结合两定理，
$$
\boxed{
\exists X\in B(K^{\oplus k}):X^q=\lambda(I_k\otimes B_m^p)
\iff q\mid pk.
}
\tag{4.3}
$$
$p=1$ 恢复此前的根重数结论；$p>1$ 的必要性不含额外交换假设。

## 5. 闭稳定域根不能接受任何有限整幂的整个像

本节明确区分全空间有界根与一个可能无界的闭算子在其稳定域上的幂身份。

置 $\mathcal B=I_k\otimes B_m$。设 $T$ 为 $K^{\oplus k}$ 上稠密定义的闭算子，域记为 $\mathcal D$，满足
$$
T\mathcal D\subseteq\mathcal D,\qquad
\mathcal B\mathcal D\subseteq\mathcal D,\qquad
T\mathcal Bx=\mathcal BT x\quad(x\in\mathcal D),
\tag{5.1}
$$
并且
$$
T^q x=\lambda\mathcal B^p x\quad(x\in\mathcal D).
\tag{5.2}
$$
第一条使 $\operatorname{Dom}T^q=\mathcal D$，但一般 $\mathcal D\ne K^{\oplus k}$。

**推论 5.1。** 若 $q\nmid pk$，则对每个整数 $r\ge0$，
$$
\boxed{\operatorname{Ran}\mathcal B^r\not\subseteq\mathcal D.}
\tag{5.3}
$$

**证明。** 反设某个 $r$ 有范围包含。则
$$
Y=T\mathcal B^r
$$
定义于整个 $K^{\oplus k}$。它是闭算子：若 $x_n\to x$ 且 $Yx_n\to y$，则 $\mathcal B^rx_n\to\mathcal B^rx$；$T$ 的闭性给 $T\mathcal B^rx=y$。闭图定理遂给 $Y\in B(K^{\oplus k})$。

由 (5.1) 的域保持和交换，可逐次移动 $\mathcal B^r$，并且每次的中间向量仍在真实域内，得到
$$
Y^q=T^q\mathcal B^{qr}
=\lambda\mathcal B^{p+qr}.
\tag{5.4}
$$
(4.3) 迫使
$$
q\mid k(p+qr),
$$
也就是 $q\mid kp$，矛盾。证毕。

对于最直接的闭根问题 $k=p=1$，条件 (5.1) 中的 $\mathcal B$ 保持及交换无须另加：由域的 $T$-稳定性和 $T^q=\lambda B_m$，对 $x\in\mathcal D$ 有
$$
B_mx=\lambda^{-1}T^qx\in\mathcal D,
\qquad
TB_mx=\lambda^{-1}T^{q+1}x=B_mTx.
$$
因此任何稠密闭、稳定域、满足 $T^q=\lambda B_m|_{\mathcal D}$ 的根都必须满足 (5.3)。

更一般，当 $p$ 为奇数时，(5.2) 自动先给 $B_m^p$ 的域保持与交换；奇幂强多项式恢复及 $T$ 的闭性再给 (5.1)。有限放大完全同理。$p$ 为偶数时本节保留 (5.1)，不把已付的 $B_m^{2^{v_2(p)}}$ 交换擅自增强为 $B_m$ 交换。

## 6. 对真实平坦共同倍数接口的准确作用

[R267 的共同倍数](R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)及其原尾版本给出非零 quasiaffinity $P\in\mathscr C_m$，满足
$$
PH\subseteq\bigcap_{r\ge1}\operatorname{Ran}B_m^r,
$$
且 $P$ 有同一组收缩强单位。但这个像包含的方向，与 (5.3) 所排除的
$\operatorname{Ran}B_m^r\subseteq\mathcal D$ 不同。

因此：

- 任意有限幂 $B_m^r$ 都不可能成为上述闭根的全域正则化子；
- 若采用 $P$，仍须实际证明 $PH\subseteq\mathcal D$ 或等价地构造有界 $Y=TP$；
- “$P$ 是所有幂的共同倍数”不单独支付这个新域包含，也不与 (5.3) 矛盾。

这保留了真正可能超出有限幂的平坦来源，同时防止把有限次除法或一个静态负幂估计当成已经获得闭根图。
