# R10：固定 CM 曲线在超奇异素数处的二次系数判据

**可信度：已证明。** 本文证明一个不预设高度非退化的逐素数充分判据。它与 R3 的普通素数判据互补；没有证明所需二次系数对无穷多个素数非零。

固定 R4 的曲线
$$
E/\mathbb Q:\ y^2=x^3-17x,\qquad \operatorname{rank}E(\mathbb Q)=2.
$$
令 $p\equiv3\pmod4$。这样的 $p$ 都是奇数好约化素数；因 $E$ 的 CM 域为 $\mathbb Q(i)$，在这些惰性素数处 $a_p=0$，约化超奇异。也可直接证明 $a_p=0$：在计数式 $\sum_x(\frac{x^3-17x}{p})$ 中配对 $x$ 与 $-x$，利用 $(\frac{-1}{p})=-1$，各对相消。

记 $\mathbb Q_\infty/\mathbb Q$ 为 cyclotomic $\mathbb Z_p$-扩张，$\Gamma=\operatorname{Gal}(\mathbb Q_\infty/\mathbb Q)$，$\Lambda=\mathbb Z_p[[T]]$，$T=\gamma-1$。令 $L_p^\pm(E,T)$ 为 Pollack 的两个 signed $p$-adic $L$ 函数，$X_p^\pm$ 为 Kobayashi signed Selmer 群的 Pontryagin 对偶。

## 1. 使用的已发表定理及全部输入

Pollack–Rubin 的 Theorem 7.3 及 Lemma 8.3 分别给出
$$
\operatorname{char}_\Lambda(X_p^\pm)=(L_p^\pm(E,T)),
\qquad
\operatorname{Sel}_{p^\infty}(E/\mathbb Q)
\xrightarrow{\sim}
\operatorname{Sel}_{p^\infty}^\pm(E/\mathbb Q_\infty)^\Gamma.
\tag{1}
$$
$X_p^\pm$ 是有限生成 torsion $\Lambda$-模。原文的输入是定义在 $\mathbb Q$ 上且有全整数环 CM 的椭圆曲线、奇数好超奇异素数。上述曲线及素数满足这些条件；该定理不假设 $\Sha[p^\infty]$ 有限，也不假设其高度非退化。原文的 $\operatorname{Sel}_p$ 记号指无穷层 $p$-初等 Selmer 群，本文将其明确写成 $\operatorname{Sel}_{p^\infty}$。

出处：R. Pollack and K. Rubin, *The main conjecture for CM elliptic curves at supersingular primes*, **Annals of Mathematics 159** (2004), 447–464, Theorem 7.3 and Lemma 8.3；[原文](https://arxiv.org/pdf/math/0509604)，[期刊页面](https://annals.math.princeton.edu/2004/159-1/p11)。

## 2. 模论证明与有限性推论

**定理。** 对上述每个 $p$ 和每个符号，
$$
2\le s_p:=\operatorname{corank}_{\mathbb Z_p}
\operatorname{Sel}_{p^\infty}(E/\mathbb Q)
\le\operatorname{ord}_{T=0}L_p^\pm(E,T).
\tag{2}
$$
因此
$$
\bigl([T^2]L_p^+(E,T),[T^2]L_p^-(E,T)\bigr)\ne(0,0)
\quad\Longrightarrow\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}.
\tag{3}
$$

**证明。** Kummer 正合列与 R4 给出 $s_p\ge2$。将 (1) 的控制同构取 Pontryagin 对偶，得到
$$
s_p=\dim_{\mathbb Q_p}\bigl((X_p^\pm/TX_p^\pm)\otimes_{\mathbb Z_p}\mathbb Q_p\bigr).
$$
一般地，设 $M$ 为有限生成 torsion $\Lambda$-模。在高度一素理想 $(T)$ 处局部化，$R=\Lambda_{(T)}$ 是剩余域为 $\mathbb Q_p$ 的 DVR，且
$$
M_{(T)}\simeq\bigoplus_{j=1}^m R/(T^{e_j}),\qquad e_j\ge1.
$$
局部化并模 $T$ 与先模 $T$ 再张量 $\mathbb Q_p$ 相同，故
$$
\dim_{\mathbb Q_p}((M/TM)\otimes\mathbb Q_p)=m
\le\sum_j e_j
=\operatorname{ord}_{T=0}\operatorname{char}_\Lambda M.
$$
代入 $M=X_p^\pm$ 并使用 (1)，即得 (2)。若 (3) 左边成立，至少一个符号的二次系数非零；(2) 已排除该符号的常数项和一次项，故其消失阶恰为 $2$。于是 $s_p=2$。R1 的 Kummer/结构定理给
$$
s_p=\operatorname{rank}E(\mathbb Q)
+\operatorname{corank}_{\mathbb Z_p}\Sha(E/\mathbb Q)[p^\infty],
$$
所以后一个余秩为零。该群余有限生成，因而有限。$\square$

## 3. 换成两个 Frobenius 分量不会消除缺口

取 $\alpha^2=-p$、$\beta=-\alpha$。Pollack 分解具有形式
$$
\begin{pmatrix}L_{p,\alpha}\\L_{p,\beta}\end{pmatrix}
=
\begin{pmatrix}
\log_p^+(T)&\alpha\log_p^-(T)\\
\log_p^+(T)&\beta\log_p^-(T)
\end{pmatrix}
\begin{pmatrix}L_p^+\\L_p^-\end{pmatrix}.
\tag{4}
$$
这里的 $\log_p^\pm$ 是 cyclotomic 对数幂级数。其乘积定义中每个归一化 cyclotomic 因子在 $T=0$ 的值为 $1$，所以 $\log_p^\pm(0)\ne0$。参见 A. Lei, *Iwasawa theory for modular forms at supersingular primes*, **Compositio Mathematica 147** (2011), 803–838, §3.4, (5)–(6)；[作者原文](https://antoniolei.com/wp-content/uploads/2014/09/ap0compositio.pdf)。

(4) 的矩阵在零点行列式为
$$
(\beta-\alpha)\log_p^+(0)\log_p^-(0)\ne0,
$$
故在 $\mathbb Q_p(\alpha)[[T]]$ 中可逆。可逆幂级数矩阵保持子模 $T^n\mathbb Q_p(\alpha)[[T]]^2$，因此两个表示中系数向量的最低消失阶相同。由 (2) 得低于二阶的项全为零，二次向量正好通过 (4) 的常数矩阵互换。换坐标并没有证明任一二次系数非零。

## 4. 与主要完成标准的关系

只需证明 (3) 的非零条件对无穷多个 $p\equiv3\pmod4$ 成立，就可由同一条固定曲线完成主目标。但本结果没有证明此无穷性，也没有把它声称为有限性的必要条件。现有高度 leading-term 公式的额外假设、秩二向量 regulator 的退化分类以及解析子群定理的准确适用范围，已写入 `notes/2026-11-12-supersingular-attempt.md`；不能把那些公式的有限性前提倒过来作为证明。
