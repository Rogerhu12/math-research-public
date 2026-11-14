# R11：固定 CM 曲线的整 j 同余具有显式刚性

日期：2026-11-12；会话：`serre-uniformity-astra/2026-11-12`。

**状态：已证明。** 这是 Raynaud 的有限平坦群全忠实性、椭圆曲线约化理论、模性和 Sturm 界的一个完整推论，不声称新颖性。它只排除与一条固定 CM 曲线同余、且 $j$ 整的非 CM 曲线；**没有证明所有同余曲线的 $j$ 必整，也没有解决 Serre 一致性。**

## 1. 主命题及显式常数

固定一条 CM 椭圆曲线 $A/\mathbb Q$，记其导子为 $N$。定义
$$
\mu_N=[\mathrm{SL}_2(\mathbb Z):\Gamma_0(N)]
=N\prod_{q\mid N}(1+q^{-1}),\qquad
B_N=\left\lfloor\frac{\mu_N}{6}\right\rfloor.
$$
令 $P(N)$ 为 $N$ 的最大素因子，并置
$$
C_A=\max\{37,\,P(N),\,4B_N\}.
\tag{11.1}
$$

**命题 R11。** 设 $p>C_A$ 是素数，$E/\mathbb Q$ 是椭圆曲线，且
$$
E[p]\simeq A[p]
\quad\text{作为 }G_{\mathbb Q}\text{-模},\qquad j(E)\in\mathbb Z.
\tag{11.2}
$$
则 $E$ 与 $A$ 在 $\mathbb Q$ 上同源。特别地，$E$ 有 CM。

证明还给出较早一步的精确结论：只要 $p>37$、$p\nmid N$ 且 (11.2) 成立，就有
$$N_E=N.\tag{11.3}$$

**具体例子。** 对
$$A:y^2=x^3-x,$$
有 $N=32$、$\mu_N=48$、$B_N=8$，所以 $C_A=37$。因此对每个 $p>37$，若 $E[p]\simeq A[p]$ 且 $j(E)$ 整，则 $E$ 与 $A$ 有理同源。这个结论不要求 $p\equiv3\pmod4$；该同余类限制只在将它应用于非分裂 Cartan 情形时出现。

## 2. 使用的标准定理

下面把较深的既有输入明确列出；后续组合论证全部给出。

1. **潜在好约化与惯性。** 椭圆曲线在局部域上有潜在好约化，当且仅当 $j$ 局部整。此时素于剩余特征的 Tate 模上的惯性像有限，且可通过好约化后特殊纤维的保原点自同构群实现，其阶至多 $24$。好约化等价于该 Tate 模惯性作用平凡，即 Néron–Ogg–Shafarevich 判据。见 Serre–Tate, *Good reduction of abelian varieties*, Ann. of Math. 88 (1968), 492–517，Theorems 1–2 及其推论；[原始论文](https://annals.math.princeton.edu/1968/88-3/p05)。椭圆曲线形式也见 Silverman, *The Arithmetic of Elliptic Curves*, VII §5、VII §7。
2. **Raynaud 的全忠实性。** 设 $R$ 为混合特征 $(0,p)$ 的离散赋值环，绝对分歧指数 $e=v_R(p)<p-1$。两个有限平坦交换 $R$-群概形若均被 $p$ 的某次幂杀掉，则其泛纤维间的每个同态都唯一延拓为 $R$ 上的同态。见 Raynaud, *Schémas en groupes de type $(p,\ldots,p)$*, Bull. SMF 102 (1974), 241–280，**Corollaire 3.3.6(1), p. 268**；[原文](https://www.numdam.org/article/BSMF_1974__102__241_0.pdf)。这里需要严格不等式 $e<p-1$，不能换成 $e\le p-1$。
3. **模性、系数和同源性。** 每条 $\mathbb Q$ 上椭圆曲线对应导子为层的归一化权二新形式；好素数系数等于 Frobenius 迹，坏处系数由约化型给出。两条曲线对应同一新形式时在 $\mathbb Q$ 上同源。这使用模性定理及 Faltings 同源定理。模性完整证明见 Breuil–Conrad–Diamond–Taylor, *On the modularity of elliptic curves over $\mathbb Q$: wild 3-adic exercises*, JAMS 14 (2001), 843–939，Theorem A，DOI [10.1090/S0894-0347-01-00370-8](https://doi.org/10.1090/S0894-0347-01-00370-8)。
4. **权二 Sturm 界。** $\Gamma_0(N)$ 上两个权二模形式，若从常数项到 $q^{B_N}$ 的系数相同，则二者相同。见 Sturm, *On the congruence of modular forms*, LNM 1240 (1987), 275–280；[原文出处](https://doi.org/10.1007/BFb0072985)。本处只用特征零的消失阶版本，也直接由价公式得到。
5. **CM 的潜在好约化。** CM $j$ 是代数整数，所以 $A/\mathbb Q$ 的 $j$ 是整数；因此 $A$ 在每个有限处有潜在好约化。此为标准复乘理论。

例子中的导子亦可由 Tate 算法直接计算：模型 $y^2=x^3-x$ 的最小判别式为 $2^6$，在 $2$ 处为 III 型，导子指数为 $5$；其余处好约化。可与 [LMFDB 32.a3](https://www.lmfdb.org/EllipticCurve/Q/32/a/3) 的精确局部数据交叉核对。

## 3. 一个初等矩阵事实

**引理 11.1。** 对任意奇素数 $r$，群
$$1+rM_2(\mathbb Z_r)$$
没有非平凡有限阶元素。

**证明。** 若 $U\ne I$，写 $U=I+r^sV$，其中 $s\ge1$ 且 $V\not\equiv0\pmod r$。二项展开给出
$$U^r=I+r^{s+1}V',\qquad V'\equiv V\pmod r.$$
因为 $r$ 为奇数，中间二项项和末项的赋值都严格大于 $s+1$；矩阵只涉及同一矩阵 $V$ 的幂，故通常二项公式适用。归纳可得 $U^{r^m}\ne I$ 对每个 $m\ge0$ 成立。另一方面 $1+rM_2(\mathbb Z_r)$ 是 pro-$r$ 群，任意有限子群都是 $r$-群。因此 $U$ 不可能有有限阶。证毕。

## 4. 表示素数 p 处：从同余下降到好约化

**引理 11.2。** 设 $p>37$，$A_0/\mathbb Q_p$ 有好约化，$E_0/\mathbb Q_p$ 有潜在好约化，且
$$E_0[p]\simeq A_0[p]$$
作为 $G_{\mathbb Q_p}$-模。则 $E_0$ 已在 $\mathbb Q_p$ 上有好约化。

**证明。** 先说明能选择一个有限 **Galois** 好约化扩张，其绝对分歧指数仍不超过 $24$；不能不加说明地取 Galois 闭包。

因为 $p\ne3$，考虑 $T_3(E_0)$。其惯性像 $H$ 有限且 $|H|\le24$。由引理 11.1，$H$ 在约化到 $E_0[3]$ 后仍被忠实表示。取
$$L=\mathbb Q_p(E_0[3]).$$
这是有限 Galois 扩张。其分歧指数等于惯性在 $E_0[3]$ 上的像的阶，故
$$e(L/\mathbb Q_p)=|H|\le24.$$
$I_L$ 在 $T_3(E_0)$ 上的像既有限又落在 $1+3M_2(\mathbb Z_3)$ 中，故为平凡群。由 NOS，$E_0/L$ 有好约化。

令 $\mathcal E,\mathcal A$ 为 $E_0/L,A_0/L$ 的椭圆曲线模型，定义在 $\mathcal O_L$ 上。因为 $\mathbb Q_p$ 绝对不分歧，$\mathcal O_L$ 的绝对分歧指数即上面的 $e$，满足
$$e\le24<p-1.$$
给定的泛纤维同构及其逆，分别由 Raynaud 全忠实性唯一延拓。因此得到有限平坦群概形的同构
$$\Phi:\mathcal E[p]\xrightarrow{\sim}\mathcal A[p].\tag{11.4}$$

$E_0,A_0$ 均定义于 $\mathbb Q_p$。对每个 $\sigma\in\operatorname{Gal}(L/\mathbb Q_p)$，泛纤维上的下降同构延拓到椭圆曲线模型；这来自好约化模型的唯一性或 Néron 映射性质。(11.4) 的泛纤维与这些下降同构相容，所以 **唯一性** 保证 (11.4) 在整模型上也相容。

现取 $\sigma$ 属于 $\operatorname{Gal}(L/\mathbb Q_p)$ 的惯性子群。它在剩余域上平凡，因而给出几何特殊纤维 $\widetilde E_0$ 的保原点自同构 $u_\sigma$。$\mathcal A$ 是 $\mathbb Z_p$ 上好约化模型的基变换，所以它的特殊纤维下降作用为恒等。由 (11.4) 的相容性，
$$u_\sigma|_{\widetilde E_0[p]}=1$$
是**群概形意义**下的恒等；这里不能只考察可能很少的几何 $p$ 挠点。

在特征 $p$ 下，$d[p]=0$，于是
$$\operatorname{Lie}(\widetilde E_0[p])=\operatorname{Lie}(\widetilde E_0).$$
所以 $u_\sigma$ 的切空间作用为恒等。特征 $p>3$ 时，椭圆曲线的保原点自同构在切空间上的作用忠实：对短 Weierstrass 模型，它具有 $(x,y)\mapsto(\zeta^2x,\zeta^3y)$ 的形式，在切空间上乘以 $\zeta^{-1}$；该数为 $1$ 时自同构即为恒等。因此 $u_\sigma=1$。

最后，$E_0/L$ 已好约化，故 $I_L$ 在 $T_3(E_0)$ 上平凡；商惯性群在特殊纤维上亦作用平凡，因而在素于 $p$ 的 $3$ 进 Tate 模上平凡。于是整个 $I_{\mathbb Q_p}$ 的作用平凡，再由 NOS 得 $E_0/\mathbb Q_p$ 好约化。证毕。

## 5. q≠p 处：导子在同余下保持

**引理 11.3。** 设 $q\ne p$，$p>3$，且 $E_1,E_2/\mathbb Q_q$ 均有潜在好约化。若 $E_1[p]\simeq E_2[p]$，则两曲线在 $q$ 处的导子指数相等。

**证明。** 对 $i=1,2$，$T_p(E_i)$ 上的惯性像是阶至多 $24$ 的有限群，其阶只含素因子 $2,3$，所以素于 $p$。对惯性的每个高阶分歧子群 $J$，记它在该 Tate 模上的有限像为 $H_{i,J}$。平均算子
$$e_{i,J}=\frac1{|H_{i,J}|}\sum_{h\in H_{i,J}}h$$
是定义在 $\mathbb Z_p$ 上的幂等算子。因此其像是自由直和因子，秩在模 $p$ 约化下不变。于是
$$
\dim_{\mathbb Q_p}(T_p(E_i)\otimes\mathbb Q_p)^J
=\dim_{\mathbb F_p}E_i[p]^J.
$$
给定的同余使右边对 $i=1,2$ 相同。因此两表示对每个高阶分歧子群都有相同的不变量余维；Artin 导子的惯性项和 Swan 项均相同。椭圆曲线导子就是这里的 Artin 导子，所以结论成立。证毕。

特别地，若 $E_1$ 好约化，则 $E_2$ 也好约化。若只需这一特例，也可直接使用引理 11.1：$E_2$ 的有限惯性像在模 $p$ 上平凡，因此落在无有限挠元的 $1+pM_2(\mathbb Z_p)$ 中，故整个惯性像平凡。

这里有限惯性阶的限制来自椭圆曲线特殊纤维的自同构群；其可能阶的素因子仅为 $2,3$。单独写“阶至多 $24$”并不能逻辑上推出素于每个 $p>3$，所以这一限制必须一并使用。

## 6. 主命题的证明

由 CM 理论和 $j(E)\in\mathbb Z$，$A,E$ 在所有有限处均有潜在好约化。

先假定 $p>37$ 且 $p\nmid N$。$A$ 在 $p$ 处好约化；由引理 11.2，$E$ 在 $p$ 处也好约化。对所有 $q\ne p$，引理 11.3 给出导子指数相等，故 $N_E=N_A=N$，证明了 (11.3)。

现在再假定 $p>4B_N$。由模性，取对应的归一化权二新形式
$$
f_E=\sum_{n\ge1}a_n(E)q^n,\qquad
f_A=\sum_{n\ge1}a_n(A)q^n
\in S_2(\Gamma_0(N)).
$$
对素数 $q\nmid Np$，挠点表示的同构给出
$$a_q(E)\equiv a_q(A)\pmod p.$$
对 $q\mid N$，两曲线都坏约化而又潜在好约化，故均为加性约化，其局部 Euler 因子为 $1$，从而
$$a_{q^m}(E)=a_{q^m}(A)=0\qquad(m\ge1).$$
在好素数处使用 Hecke 递推
$$a_{q^m}=a_q a_{q^{m-1}}-q a_{q^{m-2}},$$
再使用互素指标的乘法性。因为 $p>B_N$，所有 $1\le n\le B_N$ 都不被 $p$ 整除，故
$$a_n(E)\equiv a_n(A)\pmod p
\qquad(1\le n\le B_N).\tag{11.5}$$

Hasse 界说每个好素数 $q$ 的两个 Hecke 根均有复绝对值 $\sqrt q$。因此
$$|a_{q^m}|\le(m+1)q^{m/2}.$$
结合乘法性，以及坏素数幂系数为零，得到
$$|a_n|\le d(n)\sqrt n\le2n.$$
最后一个不等式来自因数配对给出的 $d(n)\le2\sqrt n$。因此
$$|a_n(E)-a_n(A)|\le4n\le4B_N<p.$$
结合整数同余 (11.5)，这些差只能全部为零。常数项亦均为零，故 Sturm 界给出 $f_E=f_A$，从而 $E$ 与 $A$ 在 $\mathbb Q$ 上同源。复乘性在几何同源下保持，故 $E$ 有 CM。证毕。

## 7. 精确归约：固定 CM 参考曲线仍缺哪一步

对固定 CM 曲线 $A$，下列两个最终性陈述等价：

1. 存在常数 $D_A$，使每个素数 $p>D_A$ 和每条满足 $E[p]\simeq A[p]$ 的 $E/\mathbb Q$ 都与 $A$ 有理同源；
2. 存在常数 $D'_A$，使每个素数 $p>D'_A$ 和每条满足 $E[p]\simeq A[p]$ 的 $E/\mathbb Q$ 都满足 $j(E)\in\mathbb Z$。

**证明。** 1 推出 2，因为与 CM 曲线同源的曲线也是 CM，故 $j$ 整。2 推出 1 由 R11，取阈值 $\max\{D'_A,C_A\}$。证毕。

因此，固定 CM 参考曲线的 curve-wise Frey–Mazur 问题可以明确压缩成一个 **最终整性问题**。R11 本身没有证明第 2 项。只给有限平坦同构、有限个 CM 参考曲线或固定二次商域，都不能把第 2 项当作已得结论。

若完全不用模性和 Sturm 界，也有非显式的短证明：前面的局部论证把整 $j$ 的同余曲线限制到固定坏素数集合；Shafarevich 定理给出有限多个有理同构类。对其中每条非 CM 曲线分别应用 Serre 开像定理，再取有限个阈值的最大值，就排除全部非 CM 曲线。显式证明另外还得到与 $A$ 的有理同源性和 (11.1)。

## 8. 非整 j 的实际缺口

当 $p$ 在 $A$ 的 CM 域中惰性并避开其有限坏素数时，$A[p]$ 落在相应非分裂 Cartan 正规化子中。因此同余曲线 $E$ 的每个负 $j$ 赋值素数 $q$ 都受 R2 的 Tate 约束：$q\ne p$、$q\equiv\pm1\pmod p$，而 Tate 参数是 $\mathbb Q_q$ 中的 $p$ 次幂。

若此外 $A$ 在 $q$ 好约化，则 $E[p]$ 在 $q$ 不分歧；潜在乘性曲线 $E$ 此时只能是乘性约化，其分裂符号记为 $s_q\in\{\pm1\}$。比较 Frobenius 特征多项式得到
$$a_q(A)\equiv s_q(q+1)\pmod p.\tag{11.6}$$
R11 未排除满足 (11.6) 的新乘性素数；没有这些素数时的固定导子论证，不能直接用于存在这些素数的曲线。

关于固定二次域、Anni–Siksek 的有限 CM 参考曲线定理、以及 (11.6) 对 $A:y^2=x^3-x$ 的进一步定量后果，见 `../notes/2026-11-12-cm-congruence-global-route.md`。
