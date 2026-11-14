# R2：潜在乘法约化处的精确局部判据

日期：2026-11-12。状态：**已证明**。这是标准 Tate 表示的展开与后续推论，不声称解决一致性或取得文献优先权。

## 1. 命题

设 $p\ge5$ 为素数，$q$ 为任意有理素数，$E/\mathbb Q_q$ 满足 $v_q(j(E))<0$。记 $t\in\mathbb Q_q$ 为具有相同 $j$ 的 Tate 曲线的参数，$v_q(t)=-v_q(j(E))>0$。则下列两条等价：

1. $\bar\rho_{E,p}(G_{\mathbb Q_q})$ 包含于某个非分裂 Cartan 正规化子；
2. $q\ne p$，$q\equiv\pm1\pmod p$，且 $t\in\mathbb Q_q^{\times p}$。

令 $e=-v_q(j(E))$。这又等价于：

- $q\equiv-1\pmod p$ 时，$p\mid e$；
- $q\equiv1\pmod p$ 时，$p\mid e$，且 $q^{-e}t\bmod q$ 在 $\mathbb F_q^\times$ 中是 $p$ 次幂。

两行均隐含 $q\ne p$，其他 $q$ 不可能。

## 2. Tate 输入和证明

Tate 一致化给出：$E$ 是 Tate 曲线 $T_t/\mathbb Q_q$ 的至多二次扭曲。在适当的 $p$-挠点基下，
$$
\bar\rho_{T_t,p}(g)=
\begin{pmatrix}\chi_p(g)&b_t(g)\\0&1\end{pmatrix},
$$
其中 $\chi_p$ 是模 $p$ 圆分特征，$b_t$ 描述 $g(t^{1/p})/t^{1/p}\in\mu_p$。扭曲只给矩阵乘一个 $\{\pm1\}$ 值标量；由于 $-I$ 在 Cartan 内，是否包含于某个正规化子不受影响。

假设 1。正规化子的阶为 $2(p^2-1)$，与 $p$ 互素。若 $\chi_p(g)=1$，上式是幺幂矩阵，所以只能是单位矩阵。于是 $b_t$ 在 $\ker\chi_p$ 上恒为零，整个表示经过 $\operatorname{Im}\chi_p$ 分解。该群阶与 $p$ 互素，由有限群表示的平均投影（Maschke）可对角化，得到
$$\bar\rho_{T_t,p}\simeq\chi_p\oplus1.$$

R1 的矩阵计算说明：正规化子中有两个不同 $\mathbb F_p$-特征值的元素，其特征值之比只能为 $-1$。因此 $\operatorname{Im}\chi_p\subseteq\{\pm1\}$。

若 $q=p$，$\mathbb Q_p(\mu_p)/\mathbb Q_p$ 的 Galois 群为 $\mathbb F_p^\times$，阶 $p-1>2$，矛盾。因此 $q\ne p$。此时 $\chi_p$ 非分歧，Frobenius 的值为 $q\bmod p$，故 $q\equiv\pm1\pmod p$。

令 $L=\mathbb Q_q(\mu_p)$。因为 $b_t$ 在 $G_L$ 上为零，$t$ 在 $L$ 中有 $p$ 次根。现在 $f=[L:\mathbb Q_q]\in\{1,2\}$。取 $z\in L$ 满足 $z^p=t$，则
$$N_{L/\mathbb Q_q}(z)^p=t^f.$$
取整数 $a,b$ 使 $af+bp=1$，则
$$\bigl(N_{L/\mathbb Q_q}(z)^a t^b\bigr)^p=t.$$
所以 $t\in\mathbb Q_q^{\times p}$，证明 2。

反之，若 2 成立，可选 $t^{1/p}\in\mathbb Q_q$，故 Tate 表示就是 $\chi_p\oplus1$。当 $q\equiv1$ 时它平凡；当 $q\equiv-1$ 时像由 $\operatorname{diag}(-1,1)$ 生成。后者是任意标准非分裂 Cartan 正规化子中的外陪集 involution。二次扭曲仍只乘标量，故满足 1。

最后，$p\ne q$ 时 $u\mapsto u^p$ 在 $1+q\mathbb Z_q$ 上是同构，Hensel 引理给出
$$t\in\mathbb Q_q^{\times p}
\iff p\mid v_q(t)\ \text{且}\ q^{-v_q(t)}t\bmod q\in(\mathbb F_q^\times)^p.$$
若 $q\equiv-1\pmod p$，$p\nmid q-1$，有限域上的 $p$ 次幂映射也是同构；若 $q\equiv1$，则必须保留剩余类条件。命题得证。

## 3. 与全局二次特征的相容性

若 $E/\mathbb Q$ 的像包含于一个固定 $N$，定义 $\varepsilon:G_{\mathbb Q}\to N/C=\{\pm1\}$。在所有负 $j$-赋值处 $q$，以上证明还给出
$$\varepsilon|_{I_q}=1,\qquad
\varepsilon(\operatorname{Frob}_q)=
\begin{cases}1,&q\equiv1\pmod p,\\-1,&q\equiv-1\pmod p.\end{cases}$$

理由是惯性上的 Tate 表示平凡，二次扭曲只产生 Cartan 内的标量；Frobenius 在 $q\equiv1$ 时为标量，在 $q\equiv-1$ 时有两个不同的有理特征值，故在外陪集。

## 4. 分母和高度推论

若无 CM 的 $E/\mathbb Q$ 在 $p>37$ 非满射，R1 允许应用本命题。将 $j$ 写成既约分数，则其正分母必须为 $B^p$，$B\in\mathbb Z_{>0}$。写
$$j=\frac{a}{B^p},\qquad \gcd(a,B)=1.$$
每个 $q\mid B$ 满足 $q\equiv\pm1\pmod p$。由 Tate 级数
$$j(t)=t^{-1}+744+196884t+\cdots$$
及其在 $v_q(j)<0$ 区域的反演，
$$t=j^{-1}\bigl(1+O_q(j^{-1})\bigr),$$
括号中的主单位是 $p$ 次幂。因此当 $q\equiv1\pmod p$ 时，还必须有
$$a\bmod q\in(\mathbb F_q^\times)^p.$$

若 $j\notin\mathbb Z$，取任一 $q\mid B$。此时 $q$ 为奇数且 $q\ne p$，$q\pm1$ 是正的偶数倍 $p$，故 $q\ge2p-1$。于是对绝对对数高度有
$$h(j)\ge\log(B^p)\ge p\log(2p-1).$$

这是**下界**；没有一个反向的、适用于全部异常曲线的统一高度估计，它不限制 $p$ 的绝对大小。

## 5. 文献与边界

Tate 表示是标准已证工具；可见 Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves* (1994), Chapter V, §3。直接针对本题的原文为：

- Zywina, *On the surjectivity of mod $\ell$ representations associated to elliptic curves*, Bull. London Math. Soc. (2022), Lemma 2.2、Theorem 1.5；[作者 PDF](https://pi.math.cornell.edu/~zywina/papers/EffectiveModl.pdf)。该引理已给出 $q\equiv\pm1$ 和 $p\mid v_q(j)$。
- Lemos, *Serre's uniformity conjecture for elliptic curves with rational cyclic isogenies*, Trans. AMS 371 (2019), Proposition 2.2；[原文](https://arxiv.org/pdf/1702.01985)。

本文补写的是完整局部等价条件及单位部分的具体形式；不把已有必要条件重新包装成一致性的证明。R3 构造同时满足本命题及 $p$ 处非分裂正规化子条件的曲线，说明这些局部限制仍可彼此相容。
