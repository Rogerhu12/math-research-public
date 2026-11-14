# 相容表示系能否把单个 p 的 Sha 有限性传播出去？

日期：2026-11-12。会话：Astra-rank2-Sha / literature_scope。

**状态：得到 E17 的所有奇素数处 adjoint Selmer 消失这一可直接引用的正向结论；没有把它转移到标准 Tate 表示，也没有证明本题的跨 p 有限性。** 本笔记重点核对 Larsen–Pink 的 monodromy 独立性和 Newton–Thorne 的 adjoint 消失定理，另完整说明 Artin/Tate 的真正独立性例子。

记号固定为
$$
V_p(E)=T_pE\otimes_{\mathbb Z_p}\mathbb Q_p
\simeq H^1_{\mathrm{et}}(E_{\overline{\mathbb Q}},\mathbb Q_p)(1).
$$
本题对象是 $H^1_f(\mathbb Q,V_p(E))$，不是再把 $V_p(E)$ 扭曲一次。

## 1. 一个确实适用于 E17、且对所有奇 p 成立的定理

Newton–Thorne，*Adjoint Selmer groups of automorphic Galois representations of unitary type*，JEMS 25 (2023), 1919–1967，**Theorem 5.5**：设 $F$ 全实，$E/F$ 为椭圆曲线，$p$ 任意。若

- $E$ 非 CM；或
- $E$ 有 CM 域 $K/\mathbb Q$，且 $K\not\subset F(\zeta_{p^\infty})$，

则
$$
H^1_f(F,\operatorname{ad}V_p(E))=0.
\tag{1}
$$
这里 $\operatorname{ad}$ 是 $\operatorname{End}(V_p(E))$ 的共轭作用；在二维情形 $\mathfrak{gs}=\mathfrak{gl}_2$，见 Theorem 5.4 的证明。Theorem 5.5 的原文包括 CM 分支，不能只读摘要中的 non-CM 叙述。

对 E17，取 $F=\mathbb Q$、$K=\mathbb Q(i)$。对每个奇 $p$，所有 $\mathbb Q(\zeta_{p^n})/\mathbb Q$ 在 $2$ 不分歧，而 $\mathbb Q(i)/\mathbb Q$ 在 $2$ 分歧，所以
$$
\mathbb Q(i)\not\subset\mathbb Q(\zeta_{p^\infty}).
$$
由 (1) 得到明确结论
$$
\boxed{H^1_f(\mathbb Q,\operatorname{ad}V_p(E17))=0
\quad\text{对每个奇素数 }p.}
\tag{2}
$$
它不要求 $p$ 普通、好约化或满足额外的残余像条件。

[期刊原文](https://ems.press/content/serial-article-files/32858?nt=1)，已读取 Theorem A、Theorems 5.2–5.7 及其应用论证。总体证明输入是 Taylor–Wiles / pseudodeformation 技术，而非单靠 Frobenius 多项式相容性；本笔记没有独立重做全部技术证明。

### 1.1 最接近标准 CM 特征的正向结果仍然是另一权重

该文 **Theorem 5.7** 还证明：$F$ 为 CM 域，$\chi$ 是 unitary、type $A_0$ 的 Hecke 特征；若 $\chi\chi^c=1$，各无限型指数皆非零且同奇偶，并且 $F\not\subset F^+(\zeta_{p^\infty})$，则
$$
H^1_f(F,r_{\chi,p})=0.
\tag{3}
$$
对 E17 的 CM Tate 特征 $\psi_p,\psi_p^c$，有
$$
\psi_p\psi_p^c=\varepsilon_p,
$$
其中 $\varepsilon_p$ 是 cyclotomic 特征。比值 $\psi_p/\psi_p^c$ 的无限型为 $(1,-1)$ 或其相反（依 reciprocity 约定），是 (3) 可以处理的 weight-zero 对象。

但标准分量 $\psi_p$ 不满足反 cyclotomic 条件。任何整数 Tate 扭曲都满足
$$
(\psi_p\varepsilon_p^m)(\psi_p^c\varepsilon_p^m)
=\varepsilon_p^{2m+1}\ne1\qquad(m\in\mathbb Z).
\tag{4}
$$
有限阶 twist 也不能消掉右边的无限阶。形式上用半个 Tate 扭曲会变为半整数无限型，不是这里要求的 type $A_0$ 代数 Hecke 特征。因此 (3) 不能用于曲线原来的标准分量。

## 2. 尝试从 adjoint 转移：两种具体办法及其失败环节

### 2.1 直接因子、整数 Tate 扭曲与有限扩域

采用几何 Frobenius 的权重约定，$V_p(E)$ 的纯权重为 $-1$；纯表示 $W$ 的 $\operatorname{End}(W)$ 纯权重为 $0$，其整数 Tate 扭曲为偶权重 $-2m$。所以
$$
\operatorname{Hom}_{G_F}
\bigl(V_p(E),\operatorname{End}(W)(m)\bigr)=0
\tag{5}
$$
并且反向 Hom 也为零，只要 $W$ 为上述纯的几何/自守表示。

**证明。** 选一个两者都不分歧的好有限素点 $v\nmid p$。$V_p(E)$ 的所有 Frobenius 特征值的复绝对值为 $N(v)^{-1/2}$，而 $\operatorname{End}(W)(m)$ 的为 $N(v)^{-m}$；对整数 $m$ 两个谱不相交。任何 Galois 等变映射须与该 Frobenius 交换，故为零。有限扩域仅把相应特征值提升至固定正整数次幂，仍不相交。有限阶 Artin twists 的特征值绝对值为 $1$，也不改变论证。

相同证明适用于由纯 adjoint、Artin、整数 Tate 对象经有限直和、张量积、对偶及子商构成的对象：其纯组成因子的权重都是偶数，不能包含标准椭圆表示这个奇权重组成因子。这个断言只限制这些直接的表示操作，不排除额外几何对应、混合扩张或其他未构造的桥梁。

因此 (2) 不能经系数表示的一个投影或注入变成 $H^1_f(\mathbb Q,V_p(E17))$ 的维数上界。

### 2.2 用 $\mathbf1\oplus V$ 人为制造 adjoint 因子

一个看似更直接的办法是令 $W_p=\mathbb Q_p\oplus V_p(E)$。此时
$$
\operatorname{End}(W_p)
\simeq\mathbb Q_p\oplus\operatorname{End}(V_p(E))
\oplus V_p(E)\oplus V_p(E)^*.
\tag{6}
$$
若 Newton–Thorne 的消失定理能对这个 $W_p$ 使用，确实会强迫 $H^1_f(\mathbb Q,V_p(E))=0$。但定理假设此处全部不成立：$W_p$ 可约、混合两个不同权重，且其 Hodge–Tate 权重中 $0$ 重复，不能是所要求的 regular algebraic cuspidal 表示的纯 Galois realization。该文的一般定理要求的 enormous 像条件也排除了这个直接和。

这不是一个可以忽略的技术例外。R4 已给 E17 的两条独立有理点，Kummer 映射因而给所有 $p$ 都有
$$
\dim_{\mathbb Q_p}H^1_f(\mathbb Q,V_p(E17))\ge2.
$$
所以任何删除上述假设、把 adjoint 消失套到 (6) 的论证，都会与已知点矛盾。

相关更新也没有解除这个边界：Thorne，*On the vanishing of adjoint Bloch–Kato Selmer groups of irreducible automorphic Galois representations*，Theorem A / 6.1，将 enormous 条件减弱为限制到 cyclotomic 无限扩张后的不可约性，但仍要求 polarizable、cuspidal、regular algebraic，结论仍是 adjoint。
[作者版本](https://arxiv.org/pdf/2207.04925)；[发表信息](https://doi.org/10.4310/pamq.2022.v18.n5.a5)。已核对其引言与 Theorems 6.1–6.2，不依赖该更新来证明 (2)。

## 3. Larsen–Pink 的独立性究竟独立什么

Larsen–Pink，*On $\ell$-independence of Algebraic Monodromy Groups in Compatible Systems of Representations*，定义 (6.5) 用稠密 Frobenius 元素的特征多项式刻画相容性。对半单系统，其 Proposition (6.12) 给出连通 monodromy 群表示的 formal character 独立于 $\ell$，Proposition (6.14) 给出连通分量群的独立性；Theorems (9.1)、(9.4) 在文中附加条件及密度一素数集上进一步控制 Weyl 群、根数据和表示。

这些结论处理的是
$$
G_p=\overline{\rho_p(G_F)}^{\mathrm{Zar}},
$$
没有把带 Bloch–Kato 局部条件的全球 $H^1$ 纳入结论。文中引言还明确说明，特征多项式相容条件只约束半单化；其方法因而首先化到 reductive monodromy 群。

[作者原文](https://people.math.ethz.ch/~pink/ftp/LP2.pdf)。本次读取了定义 (6.5)、Propositions (6.12)、(6.14) 与主定理范围，没有把这些结论重新表述为 Selmer 独立性。

### 3.1 特征多项式看不见扩张类：一个完整的形式观察

给定 $\rho_p:G_F\to\mathrm{GL}(V_p)$ 与任意连续 $1$-cocycle $c_p\in Z^1(G_F,V_p)$，定义
$$
\widetilde\rho_{p,c_p}(g)=
\begin{pmatrix}\rho_p(g)&c_p(g)\\0&1\end{pmatrix}.
$$
cocycle 条件恰保证它是表示，而且对所有 $g$，
$$
\det(T-\widetilde\rho_{p,c_p}(g))
=(T-1)\det(T-\rho_p(g)),
\tag{7}
$$
与 $c_p$ 是否为 coboundary 完全无关。

因此从一组相容的 $\rho_p$ 出发，在不同 $p$ 任选零或非零的 Selmer 扩张类，(7) 的好素点 Frobenius 多项式仍相容。例如可在一个 $p_0$ 选择 E17 的非挠点 Kummer 类，在其余 $p$ 选择零类；所有半单化都为 $\mathbf1\oplus V_p(E17)$。这只是一个说明相容多项式不记录扩张类的例子，**不是**构造了来自同一个固定混合动机的实现系，更不是本题有限性传播的反例。

主问题需要的正是解释这些 $p$-adic 扩张中哪些来自共同全球几何对象。单纯的 monodromy 独立性没有提供这个信息。

## 4. Artin/Tate 的真独立性：为什么这些例子能够做

以下可直接由类域论和 Kummer 理论证明，不需要假设一般 Bloch–Kato 猜想。

令 $L/F$ 是固定有限 Galois 扩张，$G=\operatorname{Gal}(L/F)$。令 $A$ 是数域，$W_A$ 是一个通过 $G$ 作用的有限维 $A$ 表示。对 $A$ 的有限素点 $\lambda\mid p$，置 $W_\lambda=W_A\otimes_A A_\lambda$。则
$$
H^1_f(F,W_\lambda)=0,
\tag{8}
$$
以及
$$
H^1_f(F,W_\lambda(1))
\simeq
\left((\mathcal O_L^\times\otimes_{\mathbb Z}A)
\otimes_AW_A\right)^G\otimes_AA_\lambda.
\tag{9}
$$
右边来自一个固定的有限维 $A$ 向量空间，故 (9) 的维数确实独立于 $\lambda$。

**证明 (8)。** 限制到 $L$ 后表示平凡。Bloch–Kato 局部条件对 $\mathbb Q_p$ 是不分歧条件，包括 $v\mid p$，所以 $H^1_f(L,\mathbb Q_p)$ 是在所有有限处不分歧的 Abel 连续加法特征；它们经有限理想类群分解，故为零。限制映射在特征零系数上单射，因为 corestriction 与 restriction 的复合为非零整数 $[L:F]$。于是 (8) 成立。

**证明 (9)。** Kummer 理论给 $H^1_f(L,\mathbb Q_p(1))=\mathcal O_L^\times\otimes\mathbb Q_p$：先在 $p$ 之外不分歧的 Galois 群中得到 $p$-单位，$v\mid p$ 的 finite 条件再排除各 $p$-素点的赋值。有限群上特征零系数的高次上同调为零，所以 restriction、取 $G$ 不变量给出 (9)。局部条件也下降：它对 restriction/corestriction 稳定，且 $[L:F]$ 在 $A_\lambda$ 中可逆。这里不要求 $p\nmid[L:F]$，因为系数已经是域。

所用局部事实可核对 Bloch–Kato，*L-functions and Tamagawa Numbers of Motives*，Example 3.9：$H^1_f(L_v,\mathbb Q_p)$ 为不分歧特征，$H^1_f(L_v,\mathbb Q_p(1))$ 为单位对应的子空间；Example 3.11 给椭圆/Abelian variety 的局部 Kummer 比较。
[原文](https://math.stanford.edu/~conrad/BSDseminar/refs/BKTamagawa.pdf)。上面的全球推导已完整写出；没有把 Artin motives 的一般整系数 Tamagawa 猜想全部当成已知。

Artin 表示有限像，且在 (9) 中已经有显式的固定全球单位模。$V_p(E17)$ 有无限像和奇权重，不是有限表示的整数 Tate 扭曲。类域论的这个证明不能通过“同样属于相容系”推广到它。

## 5. 真正需要的传播命题，以及它会立刻给什么

R1 的 Kummer/Selmer 结构在有理系数上给出
$$
0\longrightarrow E(\mathbb Q)\otimes\mathbb Q_p
\longrightarrow H^1_f(\mathbb Q,V_p(E))
\longrightarrow T_p\Sha(E/\mathbb Q)\otimes\mathbb Q_p
\longrightarrow0.
\tag{10}
$$
因此对固定 E17，若记
$$
s_p=\dim_{\mathbb Q_p}H^1_f(\mathbb Q,V_p(E17)),
$$
则 $\Sha(E17)[p^\infty]$ 有限等价于 $s_p=2$。只要已知某个 $p_0$ 满足有限性，一个真正证明所有 $s_p$ 相同的定理就会给出所有 $p$ 的 primary 有限性；若只证明除有限多个外相同，还需要保证一个已知有限的素数落在该范围内，或另证明共同维数为 $2$。

同理，若一个独立性结果只针对密度一素数集，不能把该集合外的单个 $p_0$ 偷换成其中的基点。必须核对集合是否包含已认证素数，或直接识别共同维数。

一个充分而清楚的“共同对象”条件是：存在有限维 $\mathbb Q$ 向量空间 $M$，以及对所考虑全部 $p$ 的同构
$$
M\otimes\mathbb Q_p\simeq H^1_f(\mathbb Q,V_p(E)),
\tag{11}
$$
并与有理点 Kummer 映射相容。更强地，若整个 Selmer complex 是某个固定有限维有理复形的各个 base change，也会得到同样的维数独立性。维数论对此的推论是直接的；困难是证明 (11)。对椭圆曲线，已经构造的共同全球对象 $E(\mathbb Q)\otimes\mathbb Q$ 只给 (10) 的单射，满射的缺陷正是本题要消除的 $T_p\Sha$。

Thorne 上述论文引言式 (1.1) 对一般严格相容系把 Selmer 维数与共同 $L$ 函数零阶的等式列为 Fontaine–Mazur / Beilinson / Bloch–Kato 猜想的预期；随后证明的是特定 adjoint 情形。本文没有以其一般预期作为 (11) 的证明。

## 6. 本次分支的结论和可复用信息

可直接登记的正向事实是 (2)：**E17 在每个奇素数的 adjoint Bloch–Kato Selmer 群为零**。此外，(8)–(9) 给 Artin/Tate 情形真正的跨 $p$ 维数独立性。

本次尝试的两条实际转移路径已检查：直接因子/整数 twist 被权重奇偶排除；$\mathbf1\oplus V$ 的 adjoint 嵌入违反定理的纯性、regularity 与不可约像条件。Larsen–Pink 的 monodromy 独立性没有补上 Selmer 扩张类与共同全球几何对象之间的比较。

所以本轮没有将已有单个 $p$ 的标准 Selmer 有限性传播到无穷多个 $p$。继续使用 adjoint 技术时，所缺的是一个把标准表示的 Selmer 缺陷与某个已证消失的 adjoint 量联系起来的**新算术映射或不等式**；它不能只是系数表示的直接投影，也不能由 Frobenius 相容性自动产生。
