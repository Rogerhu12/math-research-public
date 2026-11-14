# R1：$p$-初级有限性的精确结构与量词

**可信度：已证明（标准结构的完整推导与逻辑校正）。** 不声称解决无穷素数问题。

设 $E/K$ 是数域上的椭圆曲线，$r=\operatorname{rank}E(K)$，$p$ 是素数。记
$$
S_p=\operatorname{Sel}_{p^\infty}(E/K),\qquad
A_p=\Sha(E/K)[p^\infty].
$$

## 1. 有限层与无限层

对 $n\ge1$，由乘 $p^n$ 的 Kummer 序列及各处局部化，得到短正合列
$$
0\longrightarrow E(K)/p^nE(K)
\longrightarrow \operatorname{Sel}_{p^n}(E/K)
\longrightarrow \Sha(E/K)[p^n]\longrightarrow0.                 \tag{1}
$$
这里 Selmer 群的定义就是 $H^1(K,E[p^n])$ 中在每个 $v$ 落入局部 Kummer 像的元素。因而右端像恰是每处局部平凡的 $p^n$ 扭子；这证明了 (1) 的满射性，未假设 $\Sha$ 有限。

有限层 Selmer 群是有限群。回顾标准证明的有限性步骤：取包含无穷处、坏约化处和 $p$ 上方各处的有限集合 $S$。在 $S$ 外，好约化与 $p$ 可逆保证局部 Kummer 类不分歧。因此 Selmer 群包含于 $H^1(G_{K,S},E[p^n])$。对固定有限 $G_{K,S}$-模 $M$，一个连续余循环连同 $G_{K,S}$ 在 $M$ 上的作用给出到有限群 $M\rtimes\operatorname{Aut}(M)$ 的同态；其核所定义的扩张次数有统一上界，且只在 $S$ 内分歧。有限次数局部扩张的判别式指数有上界，Hermite–Minkowski 定理遂保证这样的整体扩张只有有限多个；每个有限商上又只有有限多个余循环。因此所需 $H^1$ 有限。

在 (1) 上取直接极限，左端过渡映射是 $P\bmod p^n\mapsto pP\bmod p^{n+1}$，右端过渡映射是包含，得到
$$
0\longrightarrow E(K)\otimes\mathbb Q_p/\mathbb Z_p
\longrightarrow S_p\longrightarrow A_p\longrightarrow0.        \tag{2}
$$
Mordell–Weil 定理给出
$$
E(K)\otimes\mathbb Q_p/\mathbb Z_p\simeq
(\mathbb Q_p/\mathbb Z_p)^r.
$$
引用的经典背景是 J. H. Silverman, *The Arithmetic of Elliptic Curves*, second edition, Springer, 2009，Chapter VIII（Mordell–Weil）和 Chapter X, §4（Selmer 群与下降）。上面的有限性理由和正合列推导已单独列出。

## 2. 有限 $p$ 扭推出余有限生成，但不推出整个群有限

**群论引理。** 若离散 $p$-初级扭阿贝尔群 $A$ 的 $A[p]$ 有限，则存在整数 $d\ge0$ 和有限 $p$-群 $F$，使
$$
A\simeq(\mathbb Q_p/\mathbb Z_p)^d\oplus F.                    \tag{3}
$$

**证明。** 其 Pontryagin 对偶 $X=A^\vee$ 是紧 pro-$p$ 的 $\mathbb Z_p$-模。对偶给出 $X/pX\simeq A[p]^\vee$，故 $X/pX$ 有限。选择此商的一组生成元的提升 $x_1,\ldots,x_m$，令 $Y=\sum_i\mathbb Z_px_i$。$Y$ 是紧群的连续像，因此在 $X$ 中闭。于是紧 pro-$p$ 群 $B=X/Y$ 满足 $B=pB$。若 $B\ne0$，存在非零有限连续商 $C$；但 $C=pC$，与有限非零 $p$-群必有非零模 $p$ 商矛盾。因此 $B=0$，$X$ 是有限生成 $\mathbb Z_p$-模。离散赋值环上的结构定理给出 $X\simeq\mathbb Z_p^d\oplus F^\vee$，对偶即 (3)。$\square$

由 (1)，$A_p[p]$ 有限，故引理可用于 $A_p$。对 (2) 取对偶，得到
$$
0\longrightarrow A_p^\vee\longrightarrow S_p^\vee
\longrightarrow\mathbb Z_p^r\longrightarrow0.
$$
右端是自由模，故正合列分裂。若记 (3) 中的整数为 $d_p$，则
$$
\operatorname{corank}_{\mathbb Z_p}S_p=r+d_p,
\qquad
A_p\simeq(\mathbb Q_p/\mathbb Z_p)^{d_p}\oplus F_p.             \tag{4}
$$
因此有无条件等价
$$
\boxed{\quad A_p\text{ 有限}\quad\Longleftrightarrow\quad
\operatorname{corank}_{\mathbb Z_p}S_p=r.\quad}                 \tag{5}
$$
这是课题 README 主完成标准中所用的等价；它是正确的。

注意 $\Sha[p]$ 总是有限，因而“$\Sha[p]$ 有限”没有解决 (5)。真正需要排除的是 $d_p>0$ 时的无限可除部分。

## 3. 一个更强、但仅逐素数的有限层证书

由 (1) 的 $n=1$ 情形和 Mordell–Weil 结构定理，
$$
\dim_{\mathbb F_p}\operatorname{Sel}_p(E/K)
=r+\dim_{\mathbb F_p}E(K)[p]+\dim_{\mathbb F_p}\Sha(E/K)[p].
$$
所以
$$
\dim\operatorname{Sel}_p=r+\dim E(K)[p]
\quad\Longleftrightarrow\quad A_p=0.                          \tag{6}
$$
最后一步的理由是：任何非零 $p$-初级扭群都含非零 $p$ 阶元素。这里不能把 (6) 中的等号换为“有限”：有限层 Selmer 本来就是有限的。

若只知道 $r\ge r_0$，而某次下降证明
$$
\dim\operatorname{Sel}_p\le r_0+\dim E(K)[p],
$$
则同一公式同时证明 $r=r_0$ 以及 $A_p=0$。然而，完成有限多个这样的下降仍不推出无穷多个素数的结论。

## 4. “每个 $p$ 有限”与“整个 $\Sha$ 有限”之间还差有限支撑

任何扭阿贝尔群有初级分解
$$
A=\bigoplus_p A[p^\infty].
$$
故
$$
A\text{ 有限}\quad\Longleftrightarrow\quad
\begin{cases}
A[p^\infty]\text{ 对每个 }p\text{ 有限},\\
A[p^\infty]=0\text{ 对除有限多个以外的所有 }p\text{ 成立}.
\end{cases}                                                  \tag{7}
$$
两个方向都直接由初级分解得到：有限群只有有限个素因子；反之有限多个有限群的直和有限。

第一行单独不足。例子
$$
A=\bigoplus_p(\mathbb Z/p\mathbb Z)^2
$$
是无限扭群，每个初级部分却有限，且每个 $A[n]$ 也有限。甚至它还有值在 $\mathbb Q/\mathbb Z$ 中的零根基交错配对：不同初级部分正交，在第 $p$ 个部分取
$$
\langle(a,b),(c,d)\rangle=(ad-bc)/p\pmod{\mathbb Z}.
$$
每个非零元素可在其某个非零初级分量上找到非零配对对象，所以根基为零。由此可见，仅加上 Cassels–Tate 型“模可除子群非退化”的抽象性质，也不能补出有限支撑。这是群论反例，**不是实际椭圆曲线的 $\Sha$ 反例**。

因此，本课题更强目标里的“所有 $p$ 都有限，从而整个 $\Sha$ 有限”需要补上 (7) 的第二行；主目标的无穷素数要求不受此校正影响。

## 5. 背景中的秩假设

Gross–Zagier–Kolyvagin 的经典输入是
$$
\operatorname{ord}_{s=1}L(E,s)\le1,
$$
其结论才包括代数秩等于该解析秩及 $\Sha$ 有限。不能只把“代数秩 $\le1$”写成该定理的输入；也不能把低 **Selmer 余秩** 逆定理的输入换成低代数秩。式 (4) 精确显示二者的差别。

原始可核对出处：W. Stein, *The Birch and Swinnerton-Dyer Conjecture: A Computational Approach*, online 2007 version, §2，Theorem 2.14 与 Problem 2.16，<https://www.wstein.org/books/bsd/bsd/node24.html>。该处 Problem 2.16 正是本课题的固定曲线、无穷素数问题。
