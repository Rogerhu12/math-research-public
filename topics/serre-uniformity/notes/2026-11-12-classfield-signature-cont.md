# 精确惯性型后的全局 CM 比较，以及三次特征的明确障碍

日期：2026-11-12。会话：nonsplit_frobenius。状态：R21 已证明；本笔记 §2–§6 另给一个完整的模形式构造，说明全局模性不能替代有理系数条件。

## 1. 已完成的 R21

文件：`../results/R21-twelfth-power-signature-and-cm-twists.md`。

- $\lambda^{12}|_{I_p}=\omega_2^{12}$ 或 $\omega_2^{12p}$。证明通过 Raynaud 全忠实性在绝对分歧指数 $e\le6<p-1$ 下延拓 $\mathbb F_{p^2}$ 作用；其方程的余切模等于 $R/(p)$，强迫两个权为 $(0,e)$ 或 $(e,0)$。这是具体证明，不依赖 2026 年未发表的局部像分类。
- $\lambda^{12}$ 在 $p$ 以外不分歧，确实包括 $2,3$。对保原点自同构 $u$ 使用 $\deg(1\pm u)=2\pm\operatorname{tr}(u)$，可直接证明循环自同构阶只能为 $1,2,3,4,6$，故 $12$ 足够；并未假设整个惯性群阶整除 $12$。
- 若商域类数一，和固定 CM 参考特征比较，差特征的阶整除 $\gcd(p+1,12)$。
- 对 $K=\mathbb Q(i)$，$p\equiv7\pmod{12}$ 时真正得到某个有理四次 CM 扭曲的 $p$ 同余；$p\equiv11\pmod{12}$ 时留下可能非平凡的三次反圆分特征。
- 有界阶不能控制导子。$A_q:y^2=x^3-qx$ 的四次特征可在任意新素数 $q$ 处分歧，同时保留同一个 $K$、正确 $p$ 惯性型及满正规化子像。

## 2. 一个更强的全局障碍：非有理系数的 CM 模形式族

以下构造给出**实际的特征零新形式**，不是只拼接有限多个局部表示。

**命题。** 对每个素数 $q\equiv11\pmod{12}$，存在一个权 $2$、平凡 nebentype、水平 $32q^2$ 的正规化 CM newform $f_q$，其系数域恰为
$$
F=\mathbb Q(\sqrt3).
$$
对于每个素数 $p>37$、$p\equiv11\pmod{12}$、$p\ne q$，以及 $F$ 的任意 $p$ 上方次数一素理想 $\mathfrak p$，其残余表示可在 $\mathbb F_p$ 上实现，且
$$
\operatorname{Im}\bar\rho_{f_q,\mathfrak p}=N_{\rm ns}(p),
\qquad
\bar\rho_{f_q,\mathfrak p}|_{G_{\mathbb Q_p}}
\simeq A[p]|_{G_{\mathbb Q_p}},
$$
其中 $A:y^2=x^3-x$。商二次域固定为 $\mathbb Q(i)$。

因此，以下输入合在一起仍不能把一个模形式强迫为椭圆曲线新形式：权 $2$、平凡行列式扭曲、正确的有限平坦 $p$ 处局部类型、残余表示在 $\mathbb F_p$ 上定义、全局完整非分裂正规化子像。这里缺少的是**特征零系数为有理数**，而该族的系数域明确为二次域。

这些新形式有 CM，且不是 $\mathbb Q$ 上椭圆曲线的新形式；它们不构成 Serre 一致性的反例。

## 3. 三次环类特征的构造

令 $K=\mathbb Q(i)$，$\mathcal O_K=\mathbb Z[i]$。$q\equiv11\pmod{12}$ 保证 $q$ 在 $K$ 中惰性。导子为 $q$ 的序 $\mathcal O_q=\mathbb Z+q\mathbb Z[i]$ 的环类群为
$$
\operatorname{Pic}(\mathcal O_q)
\simeq\mathbb F_{q^2}^{\times}/
\bigl(\mathbb F_q^{\times}\mu_4\bigr).
\tag{3.1}
$$
原因是 $\mathbb Z[i]$ 的类数为一，而序的理想类群正由模 $q$ 单位商给出。此群循环，阶为 $(q+1)/2$；该阶被 $3$ 整除，所以选一个满射
$$
\nu_q:\operatorname{Pic}(\mathcal O_q)\longrightarrow\mu_3.
$$
将其视为有限阶 Hecke 特征，它的导子恰为 $q\mathcal O_K$：它不在 $q$ 以外分歧；若也在 $q$ 不分歧，则会经过平凡的普通类群，矛盾。

复共轭在 (3.1) 上为 $x\mapsto x^q$。模去 $\mathbb F_q^\times$ 后，它等于取逆，因为 $x^{q+1}\in\mathbb F_q^\times$。故
$$
\nu_q^c=\nu_q^{-1}.
\tag{3.2}
$$
而且 $\nu_q((n))=1$ 对每个与 $q$ 互素的有理整数 $n$ 成立：其模 $q$ 剩余类在被商去的 $\mathbb F_q^\times$ 中。

## 4. CM Hecke 特征与水平、nebentype

令 $\mathfrak f=(1+i)^3$。对与 $2$ 互素的理想 $\mathfrak a$，取唯一的生成元 $\alpha\equiv1\pmod{\mathfrak f}$，定义
$$
\Psi(\mathfrak a)=\alpha.
$$
唯一性来自四个单位 $\mu_4$ 恰好给出 $(\mathbb Z[i]/\mathfrak f)^\times$ 的四个剩余类。由生成元相乘可知 $\Psi$ 是无穷型 $(1,0)$ 的 Hecke 特征，其导子恰为 $\mathfrak f$。导子不能缩到 $(1+i)^2$，因为此时 $-1\equiv1$，与无穷型要求冲突。

这是 $A:y^2=x^3-x$ 的标准 CM Hecke 特征。对奇整数 $n$，
$$
\Psi((n))=\chi_{-4}(n)n.
\tag{4.1}
$$
现在令 $\Xi_q=\Psi\nu_q$。由于两个特征的分歧支集不交，$\Xi_q$ 的导子恰为 $\mathfrak f q\mathcal O_K$，无穷型仍为 $(1,0)$。

应用经典 Hecke theta-series 定理（例如 Miyake, *Modular Forms*, Theorem 4.8.2，采用非酉归一化），
$$
f_q(\tau)=\sum_{\substack{0\ne\mathfrak a\subseteq\mathcal O_K\\(\mathfrak a,\mathfrak f q)=1}}
\Xi_q(\mathfrak a)e^{2\pi iN\mathfrak a\tau}
$$
是正规化权 $2$ CM newform，水平为
$$
|D_K|N(\mathfrak f q\mathcal O_K)
=4\cdot8\cdot q^2=32q^2.
$$
其 nebentype 在与水平互素的整数 $n$ 上为
$$
\chi_{-4}(n)\frac{\Xi_q((n))}{n}
=\chi_{-4}(n)^2=1,
$$
其中用了 (4.1) 和 $\nu_q((n))=1$。无穷型的两个共轭不同，确保 theta 级数是尖点形式；特征原始性给出 newform 性。

## 5. 系数域恰为 $\mathbb Q(\sqrt3)$

$\Xi_q$ 的值在 $K(\mu_3)=\mathbb Q(i,\sqrt3)$ 内。对理想与其共轭配对，Fourier 系数为实数，故所有系数都在 $F=\mathbb Q(\sqrt3)$。

更具体地，对分裂于 $K$ 的有理素数 $r\nmid2q$，取 $r=\mathfrak r\bar{\mathfrak r}$，写
$$
\Psi(\mathfrak r)=a+bi,\qquad a,b\in\mathbb Z,\qquad a^2+b^2=r.
$$
若 $\nu_q(\mathfrak r)=1$，则 $a_r(f_q)=2a$。若其为 $\zeta_3$ 或 $\zeta_3^{-1}$，则分别有
$$
a_r(f_q)=-a-b\sqrt3
\quad\text{或}\quad
-a+b\sqrt3.
\tag{5.1}
$$

由类域论和 (3.2)，$\nu_q$ 给出 $K$ 上三次循环扩张，其在 $\mathbb Q$ 上的 Galois 群为 $D_6$。Chebotarev 定理给出分裂于 $K$、且 $\nu_q(\mathfrak r)\ne1$ 的有理素数 $r$。对这些素数，$b\ne0$，因为否则 $r=a^2$ 不是素数。故 (5.1) 中确实出现非有理系数。这证明系数域不是 $\mathbb Q$，而恰好为 $F$。

## 6. 残余表示的域、完整像与 $p$ 处有限平坦类型

现在取 $p>37$、$p\equiv11\pmod{12}$、$p\ne q$。由二次互反律，$(3/p)=1$，所以 $p$ 在 $F$ 中分裂，剩余次数为一；同时 $p$ 在 $K=\mathbb Q(i)$ 中惰性。选择 $K(\mu_3)$ 的一个 $p$ 上方素理想，剩余域为 $\mathbb F_{p^2}$。

记 $\bar\Psi$、$\bar\nu_q$ 为相应模 $p$ 特征，并令 $\Lambda=\bar\Psi\bar\nu_q$。因为 $p\equiv-1\pmod3$，有
$$
\bar\nu_q^c=\bar\nu_q^{-1}=\bar\nu_q^p,
$$
而 CM 特征满足 $\bar\Psi^c=\bar\Psi^p$，因此 $\Lambda^c=\Lambda^p$。将 $\mathbb F_{p^2}$ 当作二维 $\mathbb F_p$ 空间，让 $G_K$ 通过乘法 $\Lambda$ 作用，复共轭通过 $x\mapsto x^p$ 作用，就得到实际的 $\mathbb F_p$ 表示。它与 $f_q$ 的残余表示相同：二者都是 $\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}\Lambda$ 的下降，或等价地有相同的好素数 Frobenius 多项式。

其行列式为模 $p$ 圆分特征。对 $G_K$，$\bar\nu_q$ 的值具有范数一，而 $\bar\Psi$ 的范数为圆分特征；在复共轭上，Frobenius 半线性映射的行列式为 $-1$。

在 $p$ 处，$\nu_q$ 不分歧，且
$$
\nu_q((p))=1
$$
因为 $p$ 是与 $q$ 互素的有理整数。因此 $\nu_q$ 在整个 $G_{K_p}$ 上平凡。$\Lambda$ 在该局部群上与 $A[p]$ 的 CM 特征相同；对外陪集元素用 R21 §7 的范数一共轭计算，便得到
$$
\bar\rho_{f_q,\mathfrak p}|_{G_{\mathbb Q_p}}
\simeq A[p]|_{G_{\mathbb Q_p}}.
$$
所以这里确实是椭圆曲线的好超奇异有限平坦局部类型。

$A$ 在 $p$ 好超奇异且基域不分歧，R21 的 $e=1$ 证明给出惯性像为整个 $\mathbb F_{p^2}^\times$。再加行列式为 $-1$ 的复共轭，所得全球像恰为完整非分裂正规化子 $N_{\rm ns}(p)$。

## 7. 这个构造对研究路线的确切含义

第 2 节命题给出的不是椭圆曲线反例，而是一个明确的“有理系数缺口”模型：残余表示、权、det、$p$ 处有限平坦类型甚至实际特征零模性都可以同时满足，而特征零系数域仍为二次域。

对于实际非 CM 椭圆曲线 $E$，若它与某个这样的 $f_q$ 同余，椭圆曲线条件仍要求存在另一个系数域为 $\mathbb Q$ 的权 $2$ newform。构造 $f_q$ 没有证明这个有理 newform 存在，也没有证明它不存在。因此不可以把 Hecke theta 级数或模性定理本身当作 Serre 一致性的解答。

固定 $K=\mathbb Q(i)$ 也没有将参考曲线固定为有限集：四次部分可以在任意新素数处分歧，三次部分甚至可以迫使自然的 CM 参考对象具有非有理系数域。只有再控制差特征的具体导子或证明统一的有理同余刚性，才可能继续得到绝对素数界。

## 8. 参考

- M. Raynaud, *Schémas en groupes de type $(p,\ldots,p)$*, BSMF **102** (1974), 241–280，[原文](https://www.numdam.org/item/10.24033/bsmf.1779.pdf)；R21 已逐项注明所用编号。
- T. Miyake, *Modular Forms* (1989; English translation reprint 2006), Theorem 4.8.2：Hecke 特征的 theta 系列。其非酉归一化及水平公式亦见 Imin Chen, *Surjectivity of mod $\ell$ representations attached to elliptic curves and congruence primes*, Canadian Mathematical Bulletin **45** (2002), 337–348, Theorem 4.1，[已发表原文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/542D850BC192686BE60A77A63FE3E8B6/S0008439500016702a.pdf/surjectivity-of-mod-representations-attached-to-elliptic-curves-and-congruence-primes.pdf)。Chen 的 Theorems 1.6、1.7 已给出在 $p\nmid N_E$ 等假设下与 CM 新形式的同余；不能把一般“有 CM 模形式参考对象”声称为本轮新发现。
- $\mathbb Q(i)$、导子 $(1+i)^3$ 的上述 Hecke 特征与水平 $32$ 的 newform，可对照 F. Fité, K. S. Kedlaya, A. V. Sutherland, *Sato–Tate groups of some weight 3 motives*，[作者原文](https://math.mit.edu/~drew/conm13350.pdf) 中的显式 CM 例子。
- 二次序环类群正合列和类域论；本笔记已对所需的 $h_K=1$、惰性单素数导子情形给出显式有限域商与阶计算。
