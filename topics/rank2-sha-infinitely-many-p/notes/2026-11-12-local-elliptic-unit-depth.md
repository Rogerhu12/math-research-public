# 2026-11-12：固定椭圆单位的局部深度至多三判据

**状态：逐素数判据已证明；无穷多个素数上的深度上界未证明。** 固定 $E:y^2=x^3-17x$、$K=\mathbb Q(i)$，以及 $p=\pi\bar\pi\ge13$、$p\ne17$。本笔记把上一份 `relative-classgroup-reflection` 笔记中的全局单位格条件改成局部单位格条件，并给出一个具体的局部生成元。所用外部输入均来自 Rubin 的已证有限层下降与椭圆单位定理。

## 1. 选定的是经过导子范数的单位

令 $L=K(E[\pi])$、$G=\operatorname{Gal}(L/K)$、$\chi:G\to\mathbb F_p^\times$ 为在 $E[\pi]$ 上的作用字符，$\widetilde\chi$ 为其 Teichmüller 提升。$L$ 在 $\mathfrak p=(\pi)$ 上全分歧，唯一素点记为 $\mathfrak P$；$[L_\mathfrak P:K_\mathfrak p]=p-1$。

沿用上一份笔记已经逐项核对的单位
$$
\eta_p=\Lambda(P_\pi)
=N_{K(\mathfrak f\mathfrak p)/L}
\Theta_{E,(7)}(S+P_\pi),
\qquad\mathfrak f=2(1+i)17\mathcal O_K.
$$
其中 $S$ 为固定导子挠点，$P_\pi=\xi(\Omega/\psi(\mathfrak p))$ 为非零 $\pi$-挠点；$\Theta_{E,(7)}=\Delta^{48}/\Psi_7^{12}$。范数群阶为 $256$，范数本身只取一次。这里每个原始值的精确零化理想为 $\mathfrak f\mathfrak p$，不是素理想幂，因而所得 $\eta_p$ 在所有有限素点（包括 $2,17$）都是单位。

## 2. 局部单位目标格的秩与一个具体生成元

令
$$
\mathscr U_p=
\left(\widehat{\mathcal O_{L_\mathfrak P}^{\times}}{}^{\,(p)}
\right)^{\widetilde\chi},
\qquad
\mathscr E_p=
\left((\mathcal O_L^\times/\mu_L)\otimes\mathbb Z_p\right)^{\widetilde\chi}.
$$
帽号表示取 pro-$p$ 完备化。R7 的非 anomalous 性给出 $p\nmid\#E(\mathbb F_p)$。Rubin Lemma 10.9 因此适用，说明 $L_\mathfrak P$ 不含 $\mu_p$，且 $\mathscr U_p$ 为自由秩一 $\mathbb Z_p$-模。Dirichlet 单位定理则给出 $\mathscr E_p$ 也为自由秩一；后者不依赖任何 $p$-进调节子非退化假设。

用形式参数 $t=-x/y$，置 $t_\pi=t(P_\pi)$。它在 $L_\mathfrak P$ 中为均匀化参数。Rubin Lemma 10.4 给出 $G$-等变同构
$$
E[\pi]\xrightarrow{\sim}
(1+\mathfrak P)/(1+\mathfrak P^2),
\qquad P\longmapsto1+t(P).
$$
因此
$$
u_p=e_{\widetilde\chi}(1+t_\pi)
\in\mathscr U_p,
\qquad
e_{\widetilde\chi}=\frac1{p-1}\sum_{g\in G}\widetilde\chi(g)^{-1}g,
$$
在这个一维模的模 $p$ 商中非零。这里在单位群的 pro-$p$ 完备化中把指数投影写作加法作用。

具体解释最后一步：向 $(1+\mathfrak P)/(1+\mathfrak P^2)$ 的 $\chi$ 投影是一个非零的 $\mathbb Z_p$-线性映射 $\mathscr U_p\to\mathbb F_p(\chi)$。自由秩一模到 $\mathbb F_p$ 的任意非零映射的核都是 $p\mathscr U_p$；而 $u_p$ 的像就是 $P_\pi\ne0$。故 $u_p$ 为 $\mathscr U_p$ 的生成元。

记 $\eta_p$ 的局部 $\chi$ 投影为 $z_p^{\rm loc}$，则存在唯一
$$
b_p\in\mathbb Z_p,
\qquad z_p^{\rm loc}=b_pu_p.
$$
定义其局部深度
$$
\nu_p=v_p(b_p)\in\mathbb Z_{\ge0}\cup\{\infty\},\qquad v_p(0)=\infty.\tag{2.1}
$$
这也给出一个直接的局部对数表达式：
$$
b_p=
\frac{\sum_{g\in G}\widetilde\chi(g)^{-1}
\log_p(g\eta_p)}
{\sum_{g\in G}\widetilde\chi(g)^{-1}
\log_p(1+g t_\pi)}.\tag{2.2}
$$
分母非零：它是 $p-1$ 倍的 $\log_p(u_p)$，而该局部域不含 $p$-幂单位根，局部对数在其 pro-$p$ 单位群上没有挠核。两者属于同一一维 $\mathbb Q_p$ 特征子空间，所以比值在 $\mathbb Q_p$ 中；格的定义进一步保证它在 $\mathbb Z_p$ 中。

这里的 $\nu_p$ 是局部字符格的深度，不是原始代数单位 $\eta_p$ 的全局 $p$ 次幂深度，也不是式 (2.2) 分子在未归一化局部域中的普通赋值。

## 3. 全局格与局部格的差项

记 $z_p\in\mathscr E_p$ 为同一个单位的全局投影，深度为上一份笔记的 $m_p$。若 $\nu_p<\infty$，则局部化
$$
\lambda_p:\mathscr E_p\longrightarrow\mathscr U_p
$$
是两个自由秩一模之间的非零映射，故单射，且存在唯一 $a_p\ge0$ 使
$$
\lambda_p(\mathscr E_p)=p^{a_p}\mathscr U_p.
$$
选择各自生成元，$\lambda_p$ 为乘一个赋值 $a_p$ 的标量，于是
$$
\nu_p=m_p+a_p.\tag{3.1}
$$
这只是非零秩一格映射的指数计算。论证不先假设单一素点的 Leopoldt 性；在要证明的有限深度情形中，该非零性已由 $z_p^{\rm loc}\ne0$ 保证。若局部化恰为零，则 $\nu_p=\infty$，不会满足本文的充分条件。

令
$$
c_p=\dim\operatorname{Cl}(L)[p]^\chi,
\qquad s_p=\dim\operatorname{Sel}_p(E/\mathbb Q).
$$
R12 与 R7 给出
$$
c_p\ge1,\qquad s_p=2\left\lceil\frac{c_p}{2}\right\rceil,
$$
而上一份笔记已核对的 Rubin 椭圆单位指数界给出
$$
c_p\le m_p\quad\text{当 }m_p<\infty.\tag{3.2}
$$

## 4. 局部化指数为零时，Selmer 群没有额外的一维

**引理。** 若 $a_p=0$，则 $s_p=c_p$；特别地 $c_p$ 为偶数。

**证明。** Rubin §6 的局部下降映射
$$
\delta_1:\mathcal O_{L_\mathfrak P}^{\times}\longrightarrow E[\pi]
$$
在 $\chi$ 分量上满射（Lemma 6.8）。因此它在 $\mathscr U_p$ 上的核为 $p\mathscr U_p$。若 $a_p=0$，全局单位的局部像包含一个该格生成元，故 $\delta_1$ 的全局单位像为整个 $E[\pi]$。

更明确地，Theorem 6.9 及 Corollary 6.10 证明中的 idèle 正合列为
$$
0\longrightarrow
\mathcal O_{L_\mathfrak P}^{\times}/
\bigl(\overline{\mathcal O_L^\times}\,
(\ker\delta_1\cap\mathcal O_{L_\mathfrak P}^{\times})\bigr)
\longrightarrow J_L/W_1\longrightarrow A_0\longrightarrow0.
$$
其中第一项在上述满射性下为零；$A_0$ 是 $\operatorname{Cl}(L)$ 除以由 $\mathfrak P$ 的类生成的一个子群。由于 $L/K$ 在 $\mathfrak p$ 全分歧，
$$
\mathfrak P^{p-1}=\mathfrak p\mathcal O_L
$$
为主理想，所以这个被除掉的子群没有 $p$-初等部分。因此 Theorem 6.9 给出
$$
\operatorname{Sel}_\pi(E/K)
\simeq\operatorname{Hom}_G(\operatorname{Cl}(L),E[\pi]).
$$
R7 的有限层同构与 R12 再给出 $s_p=c_p$。R7 已无条件证明 $s_p$ 偶，所以 $c_p$ 也偶。$\square$

只使用了这个方向。没有声称 $c_p$ 为偶数就能反推出 $a_p=0$；当 idèle 列的左项非零时，取模 $p$ 同态还可能遇到非平凡扩张。

## 5. 深度判据

**命题。** 对所有本笔记的素数，$\nu_p\ge2$（包括 $\nu_p=\infty$ 的情形）。而且
$$
\boxed{\quad
\nu_p\le3
\quad\Longrightarrow\quad
\Sha(E/\mathbb Q)[p^\infty]=0.
\quad}\tag{5.1}
$$

**证明。** 若 $\nu_p=\infty$，第一结论自动成立。以下设其有限，使用 (3.1)–(3.2)。

若 $a_p\ge1$，则 $m_p\ge c_p\ge1$，故 $\nu_p\ge2$；若再有 $\nu_p\le3$，则 $c_p\le m_p=\nu_p-a_p\le2$。

若 $a_p=0$，第 4 节给出 $c_p$ 为正偶数，故 $c_p\ge2$。于是 $\nu_p=m_p\ge c_p\ge2$；若 $\nu_p\le3$，则正偶数 $c_p\le3$ 只能为 $2$。

两种情况下，有限深度至多 $3$ 都给出 $c_p\in\{1,2\}$。R7/R12 的有限层 Kummer 判据由此给出 $\Sha(E/\mathbb Q)[p^\infty]=0$。$\square$

该证明说明允许深度 $3$ 的原因：全局到局部单位格若已损失一层 $p$，它减少可用于类群的指数；若没有损失，则 Selmer 奇偶性排除类群维数 $3$。不能只从粗略上界 $c_p\le\nu_p$ 得到同样结论。

## 6. 固定函数还满足的精确分配关系

令 $\pi_E=\psi(\mathfrak p)$。Rubin 的 $\Theta$ 分配公式逐个应用到导子平移，得到
$$
\prod_{T\in E[\mathfrak p]}\Lambda(R+T)
=\prod_\sigma\Theta_{E,(7)}([\pi_E]R+[\pi_E]S^\sigma)
=\Lambda([\pi_E]R).\tag{6.1}
$$
最后一个等号使用 $[\pi_E]$ 在导子挠点轨道上等于 $\mathfrak p$ 的 Frobenius，因此置换乘积中的 $S^\sigma$。在 $R=O$ 时，$\Lambda(O)$ 非零且有限，约去两侧这一因子便得到
$$
\prod_{T\in E[\mathfrak p]\setminus\{O\}}\Lambda(T)=1,
\qquad N_{L/K}(\eta_p)=1.\tag{6.2}
$$
这些是精确代数恒等式，但 (6.1) 左边仍含随 $p$ 增长的 $p$ 个平移。现阶段没有证明它能把 (2.2) 的变化字符深度压缩成固定个代数数的低阶 Frobenius 差商。

## 7. 尚未闭合的命题

主目标现在有一个完全局部、显式且不需要求全局单位基的充分接口：对无穷多个分裂 $p$，证明 (2.2) 定义的 $b_p$ 满足 $v_p(b_p)\le3$。

本笔记已经证明统一下界 $v_p(b_p)\ge2$，没有证明所需的无穷次上界。也没有把 $b_p$ 与 CLS 的临界 Hecke 特殊值直接认作同一个数；两者若要逐式比较，仍需核对 Coleman 映射、归一化与高阶项。不能在 $\pi$-挠点上未经收敛核查就把 $\Lambda$ 的复均匀化 Taylor 级数代入形式对数：$\log_E(P_\pi)=0$，正好提醒这里可能位于形式指数的收敛边界。

## 来源

- K. Rubin, *Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，[讲义全文](https://swc-math.github.io/notes/files/99RubinCM.pdf)：Lemma 6.8，Theorem 6.9 / Corollary 6.10 的 idèle 列，Theorem 7.6，Proposition 7.8，Definition 8.1，Corollary 9.6，Lemmas 10.4、10.9。
- 本地 R4、R7、R12 及 `2026-11-12-relative-classgroup-reflection.md` 中已核对的曲线、局部条件、相对类群和全局单位输入。
