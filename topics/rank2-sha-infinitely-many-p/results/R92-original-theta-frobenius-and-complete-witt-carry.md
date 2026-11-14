# R92：原双变量 theta 的完整 Frobenius 与 Witt 进位

日期：2026-11-12。状态：公共参考、全部迭代、求和交叉项及唯一性已根端独审。
证明见[原 theta 的平方 Frobenius](../notes/2026-11-12-original-theta-square-frobenius-and-witt-trace.md)。

固定原 $E_{17}$、$N=68$、原轨道 $\mathcal S$ 和 $T=(0,0)$。
惰性 $p\ge7$ 时令 $\Phi=[-p]\times[-p]$、$q=p^2$、
$a_r=(-p)^r$，$\mathcal F(f)=f^{\sigma^2}\circ\Phi$。
这是真实平方 Frobenius lift，且 $\sigma^{2r}P=a_rP$。

## 1. 公共参考与原 theta 一起保留

令 $U_P=Z(w)\Theta_P(z,w)$，
$$
J_a=\frac{Z([a]w)}{Z(w)^{a^2}\Psi_a(w)},\qquad
D_{a,P}=J_a\frac{\Psi_a(P+z+w)}{\Psi_a(P+z)}.
$$
sigma 乘法准确给
$$
\mathcal F^r(U_P)=U_P^{q^r}D_{a_r,P}.
$$
完整除子计算消去 $J_a$ 的全部形式挠点零极点，只余非零二挠点支撑。
原点值一消去竖直因子；另由
$\Psi_a(T)=17^{(a^2-1)/4}\equiv1\pmod p$，得到
$J_a,D_{a,P},D_{a,T}\equiv1\pmod p$，在整形式群参数中均整。
没有假设公共 $U_T$ 本身整。
所有层准确有
$$
D_{a_r,P}=\prod_{j=0}^{r-1}\mathcal F^j(D_{-p,P})^{q^{r-1-j}}.
$$
末项幂为一，不能由层数宣称额外的 $p^r$ 整除。

## 2. 原和的交叉项不能换成范数

整比值 $\mathcal R_P=U_P/U_T$ 在固定 $[68]\times[68]$ 覆盖上有理。
令 $\mathcal A=\sum\mathcal R_P$、
$C_{r,P}=D_{a_r,P}/D_{a_r,T}=1+pE_{r,P}$，以及
$$
\mathfrak C_Q(X)=\bigl((\sum X_j)^Q-\sum X_j^Q\bigr)/p\in\mathbb Z[X].
$$
原来 $256$ 项相加后的完整关系为
$$
\frac{\mathcal A\circ\Phi^r-\mathcal A^{q^r}}p
=\sum_P\mathcal R_P^{q^r}E_{r,P}
-\mathfrak C_{q^r}((\mathcal R_P)_P).
$$
第二层准确保留
$$
\mathfrak C_{p^2}(X)\equiv\mathfrak C_p(X_1^p,\ldots)
+p(\sum X_j^p)^{p-1}\mathfrak C_p(X)\pmod{p^2}.
$$
模 $p$ 的指数限制不能沿用到模 $p^2$，更不能不计形式对数换元
就转成加法变量的中央对角。
恢复原对象时须乘回 $U_T^{q^r}D_{a_r,T}$，并保留
$\sum U_P=Z(w)(256/w+\mathscr K)$。

## 3. 同一方程的歧义仅为准确二次项

同一局部系数域中，两个常数一的正式解之比满足
$\mathcal F(V)=V^{p^2}$。取正式对数并逐系数比较赋值，得
$$
V=\exp(c_{20}z^2+c_{11}zw+c_{02}w^2),\qquad \sigma^2c_{ij}=c_{ij}.
$$
$U_P(z,0)=1$ 及实际二阶 jet
$[\log U_P]_2=-x(P)(zw+w^2/2)$ 消去全部歧义；
参考 $T$ 的二阶 jet 为零。
故准确初值与 $D_{-p,P}$ 唯一重建原正式解。
但 division correction 随 $p$ 增长，这并未成为固定维线性 Frobenius 矩阵，
也没有证明指定中央行对无穷多个 $p$ 非零。
