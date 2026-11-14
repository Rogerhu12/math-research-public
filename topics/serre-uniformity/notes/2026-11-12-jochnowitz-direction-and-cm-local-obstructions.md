# Jochnowitz 接口：方向、Kolyvagin 素数与本题尚缺的几何类

日期：2026-11-12。状态：已核文献适用边界；没有得到新的 Mordell–Weil 非挠点或统一排除。

## 1. 实际问题

沿用 R19、R146、R149。固定 $A:y^2=x^3-x$、$K=\mathbb Q(i)$，并设实际无 CM 曲线 $E$ 满足 $E[p]\simeq A[p]$，其中 $p>37$、$p\equiv3\pmod4$。R50 的一个 Selmer 方向不能直接作为有理点。尝试把 $L(A,1)/\Omega_A^+=1/4$ 接到 $E$ 的 Heegner 点，必须分别核对互反律的方向和所需整投影。

若 $q\mid Z$ 在 $K$ 中惰性，则 $q\equiv-1\pmod p$，而 $a_q(A)=0$；其在 $A[p]$ 上的 Frobenius 特征值为 $1,-1$。所以 $q$ 确是相对于 $(A,K,p)$ 的 Kolyvagin 素数。它不是下面 BD05 所用的 admissible 素数。这两个术语不能混用。

## 2. 经典 Jochnowitz 定理确允许 $q\equiv-1\pmod p$

Bertolini–Darmon，*Euler systems and Jochnowitz congruences*，American Journal of Mathematics **121** (1999), 259–281，作者稿 §1、Theorem 1.3；以及 Vigni，*Heegner points and Jochnowitz congruences on Shimura curves*，§1、Theorem 1.1、§3.1–3.2，采用的是 Kolyvagin 素数。

它们比较低层符号 $-1$ 的 Heegner 点与升层后符号 $+1$ 的中心值。Vigni 的条件还包括低层模参数化次数不被 $p$ 整除；其二次域判别式与导子互素，普通/推广 Heegner 分解也有指定的分裂类型。因此不能把它们反向读作本题所需的“低层 $A/K$ 的单位中心值推出高层 $E/K$ 的非挠点”。这里 $2$ 在 $K$ 中分歧也是一个独立的未覆盖条件。

文献原文：

- [BD99 作者稿](https://www.math.mcgill.ca/darmon/pub/Articles/Research/21.Jochnowitz/paper.pdf)，作者稿 pp. 3–5、§1；发表页码 259–281。
- [Vigni 作者稿](https://arxiv.org/pdf/1204.0496)，pp. 1–2、6；§3.1 只要求绝对不可约及 $p\nmid6N\deg\pi_E$，不应额外误报为要求残余满像。

还存在一个容易混淆的符号选择。BD99 在低层 $A/\mathbb Q$ 根数为 $+1$ 时，使用高层 $U_q=-1$ 的分支；这是高层非分裂乘法分支。更换辅助虚二次域，不能未经核对就把这条定理移到 $U_q=+1$ 的分裂乘法分支。

## 3. 方向合适的 BD05 第一互反律另有明确条件

Bertolini–Darmon，*Iwasawa's Main Conjecture for elliptic curves over anticyclotomic $\mathbb Z_p$-extensions*，Annals of Mathematics **162** (2005), 1–64，§2.2（印刷 p. 18）的 $n$-admissible 定义明确要求
$$
p\nmid q^2-1.
$$
Theorem 4.1（p. 29）的第一显式互反律采用这个定义。该文还以 ordinary 情形及判别式与导子互素为总体设置，Assumption 2.1（p. 14）另要求残余满像。故其定理不能原样用于本题。

[BD05 原刊全文](https://annals.math.princeton.edu/wp-content/uploads/annals-v162-n1-p01.pdf)。本记录不声称上述全部条件在证明第一互反律的有限层几何恒等式中都不可去掉；它们只是原文实际陈述中的条件。若要去掉，须给出相应的新证明。

## 4. 局部退化有具体内容

在惰性的 $q$ 处，$K_q/\mathbb Q_q$ 是未分歧二次扩张，且
$$
\operatorname{Frob}_{K_q}\mid A[p]
=\operatorname{Frob}_{\mathbb Q_q}^{\,2}
=-q=1\pmod p.
$$
又 $p\mid q^2-1$，故 $K_q$ 含 $\mu_p$。于是
$$
\dim_{\mathbb F_p}H^1_f(K_q,A[p])=2,
\qquad
\dim_{\mathbb F_p}H^1_s(K_q,A[p])=2.
$$
第一式是未分歧上同调 $A[p]/(\operatorname{Frob}-1)A[p]$；第二式由局部 Tate 对偶或惯性的 tame $p$-商得到。原定理的一维有限/奇异坐标因此不能直接照抄。

不过 $\operatorname{Gal}(K_q/\mathbb Q_q)$ 的两个本征空间可以再分开，而且 $\operatorname{Frob}_{\mathbb Q_q}$ 的 $\pm1$ 特征值互异。要把这项观察升级为实际 Heegner 点，需要证明同一符号上的整几何投影、组件群比较及与原始 toric 值的单位比例。这里只说明可能的补救接口，不把它当成已完成的互反律。

## 5. 真正尚缺的步骤

至少还须构造适合 $2$ 处真实局部型的 Shimura 曲线模参数化，证明其整组件群投影在所需 $p$ 分量上没有未计算的因子，并把实际 $E$ 上的 Heegner 类识别为 R50/R60 的非零 Selmer 方向。已存在的抽象唯一归一化类、已算出的椭圆单位类，均不能替代最后一个识别。

因此本次检查没有关闭 $s>0$ 的实际全局分支。R146 的 $s=0$ 结论和 R149 的整中心值同余保持不变；$s=1$ 的秩零加可除 $\Sha[p^\infty]$ 分支不能因此删去。
