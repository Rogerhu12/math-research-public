# R6：固定 CM 数域中的导数递推与高精度 trace 判据

**可信度：已证明。** 本文给出一个固定整数序列，把 E17 的逐素数有限性判据准确写成该序列的整除条件，并证明一个自然的有限维简化不成立。**尚未证明满足该条件的素数有无穷多个。**

## 1. 固定对象和外部已证输入

固定
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),\qquad f=34(1+i).
$$
令 $\Lambda_E=\Omega_\infty\mathbb Z[i]$ 为 Néron 微分 $dx/(2y)$ 的复周期格，选择 $\Omega_\infty$ 为正实基本周期，并设
$$
z_0=\Omega_\infty/f,\quad u=\wp(z_0,\Lambda_E),\quad
v=\wp'(z_0,\Lambda_E)/2,\quad F=K(E_f).
$$
这里 $E_f$ 是 CM 自同态 $[f]$ 的核；所有这些对象都固定，不随下文的素数 $p$ 变化。

使用的外部输入为 J. Coates–Z. Liang–R. Sujatha，*The Tate–Shafarevich group for elliptic curves with complex multiplication*，J. Algebra **322** (2009), 657–674，[作者预印本](https://arxiv.org/pdf/0901.3832)：

1. Lemmas 3.1–3.2 及 §3 式 (49)–(50)：$f\mathbb Z[i]$ 是 CM Grössencharacter $\psi_E$ 的导子，$F=K(u)$，$v\in F$，且 $u,v$ 都是代数整数；$[F:K]=\varphi(f)/4=256$。
2. §3 的周期正规化：$w=4$，$\alpha(E)=\Omega_\infty^+/\Omega_\infty=1$。式 (53) 必须采用作者在续篇中的勘误（见下），其正确版本对所考虑的素数为
   $$
   c_p^+(E):=(\Omega_\infty^+)^{-p}L(\overline\psi_E^{\,p},p)
   =-\frac{\operatorname{Tr}_{F/K}\wp^{(p-2)}(z_0,\Lambda_E)}{f^p(p-1)!}\in\mathbb Q.
   \tag{1}
   $$
3. Theorem 2.2：若 $g=\operatorname{rank}E(\mathbb Q)$ 与解析秩同奇偶，$p$ 好、分裂且不整除 $w\alpha(E)$，则 $v_p(c_p^+)<g+2$ 蕴含 $\Sha(E/K)[p^\infty]$ 有限。

**勘误依据。** 同三位作者的 *The Tate–Shafarevich group for elliptic curves with complex multiplication II*，Milan J. Math. **78** (2010), 395–416，[预印本](https://arxiv.org/pdf/1005.4206)，§4 式 (77) 后、印刷页 19，明确纠正：2009 年式 (24)、(53) 中的 $w$ 因子应删除，旧表中的数值应乘以 $4$。因此 (1) 的分母没有 $w$。该改正不影响任何奇素数处的赋值，但影响精确恒等式，必须保留。

所述数域次数也可直接核算：$(f)=(1+i)^3(17)$，$17$ 在 $\mathbb Z[i]$ 分裂，故 $\varphi(f)=4\cdot16^2=1024$。

R4 已独立证明 $\operatorname{rank}E(\mathbb Q)=2$。根数 $+1$ 的局部核算见 `notes/2026-11-12-cm-local-inputs.md`；因此函数方程给出解析秩为偶数，足以应用输入 3，不需要知道解析秩恰为二。

## 2. 完全整数的导数递推

先对任意非零整数 $D$ 定义
$$
B_0(X)=1,
$$
$$
B_{n+1}(X)=4(X^3-DX)B_n''(X)
             +6(3X^2-D)B_n'(X)+12XB_n(X).
\tag{2}
$$

**引理 1。** 若 $x(z)=\wp(z)$、$y(z)=\wp'(z)/2$ 满足 $y^2=x^3-Dx$，则对每个 $n\ge0$，
$$
x^{(2n+1)}(z)=2y(z)B_n(x(z)).
\tag{3}
$$
并且 $B_n\in\mathbb Z[X]$，$\deg B_n=n$，最高次项系数为 $(2n+2)!/2$。

**证明。** 由微分方程，
$$
x'=2y,\qquad y'=3x^2-D,\qquad y^2=x^3-Dx.
$$
当 $n=0$ 时，(3) 就是第一条等式。假设 (3) 对 $n$ 成立，对右侧连续求导两次。第一次得到
$$
\frac{d}{dz}\bigl(2yB_n(x)\bigr)
=2(3x^2-D)B_n(x)+4(x^3-Dx)B_n'(x).
$$
第二次求导，合并项并提取 $2y$，得到
$$
2y\left(12xB_n(x)+6(3x^2-D)B_n'(x)
                 +4(x^3-Dx)B_n''(x)\right).
$$
这正是 $2yB_{n+1}(x)$，完成归纳。

递推 (2) 保持整数系数。若 $B_n$ 的最高次项系数为 $b_n$，则 $X^{n+1}$ 的系数为
$$
\bigl(4n(n-1)+18n+12\bigr)b_n=(2n+3)(2n+4)b_n.
$$
从 $b_0=1$ 得到 $b_n=(2n+2)!/2\ne0$，并同时证明次数断言。$\square$

前几项为
$$
B_0=1,\qquad B_1=12X,\qquad B_2=360X^2-72D.
$$
具体计算可只用以下系数更新。每个单项式 $b_{n,k}X^k$ 对下一项的贡献是
$$
b_{n+1,k+1}\mathrel{+}=(2k+3)(2k+4)b_{n,k},\qquad
b_{n+1,k-1}\mathrel{+}=-2Dk(2k+1)b_{n,k}.
\tag{4}
$$
第二式在 $k=0$ 时贡献为零。该更新直接由 (2) 展开，因而无需数值近似或浮点计算。

## 3. 准确的 trace 归约

以下在 (2) 中取 $D=17$，定义固定序列
$$
a_n=\operatorname{Tr}_{F/K}\bigl(vB_n(u)\bigr),\qquad n\ge0.
\tag{5}
$$

**命题 2。** $a_n\in\mathbb Z[i]$。对每个 $p\equiv1\pmod4$、$p\ne17$，有
$$
c_p^+(E)=-\frac{2a_{(p-3)/2}}{f^p(p-1)!},
\tag{6}
$$
以及对任一 $\mathfrak p\mid p$，
$$
v_p(c_p^+(E))=v_{\mathfrak p}\bigl(a_{(p-3)/2}\bigr).
\tag{7}
$$
各赋值以 $v_p(p)=v_{\mathfrak p}(p)=1$ 正规化。

**证明。** $vB_n(u)$ 是 $F$ 的代数整数，故它到 $K$ 的 trace 为 $\mathbb Z[i]$ 中的元素。令 $n=(p-3)/2$，则 $2n+1=p-2$。将引理 1 在 $z_0$ 的值代入 (1)，得到 (6)。

由于 $p\equiv1\pmod4$，它在 $K$ 分裂且不分歧。又 $p\ne17$，所以 $2$、$f$、$(p-1)!$ 在两个 $\mathfrak p\mid p$ 处都是单位。对 (6) 取 $\mathfrak p$-赋值，得右侧为 $v_{\mathfrak p}(a_n)$。左侧 $c_p^+$ 是有理数，故其 $\mathfrak p$-赋值等于通常的 $v_p$，得到 (7)。$\square$

**推论 3。** 定义
$$
\mathcal P_{17}^{\rm tr}
=\left\{p\equiv1\pmod4,\ p\ne17:
a_{(p-3)/2}\notin\mathfrak p^4\right\}.
\tag{8}
$$
这个定义与两个 $\mathfrak p\mid p$ 中的选择无关。每个 $p\in\mathcal P_{17}^{\rm tr}$ 都满足 $\Sha(E/\mathbb Q)[p^\infty]$ 有限。因此，若另行证明 $\mathcal P_{17}^{\rm tr}$ 无穷，本课题即完成。

**证明。** 由 (7) 和整性，条件等价于 $v_p(c_p^+)\le3$，故不依赖 $\mathfrak p$ 的选择。曲线的坏素数仅为 $2,17$；R4 的秩二、根数 $+1$、$w=4$ 和 $\alpha=1$ 满足第 1 节输入 3 的全部假设。该输入给出 $\Sha(E/K)[p^\infty]$ 有限。

restriction 与 corestriction 在 $\Sha(E/\mathbb Q)[p^\infty]$ 上的复合是乘以 $[K:\mathbb Q]=2$。由于 $p$ 为奇数，此乘法可逆，所以 restriction 单射。它将所求群嵌入一个有限群，从而得到结论。$\square$

这里的条件是充分条件。本文没有证明它是初级有限性的必要条件，也没有把 (8) 的无穷性当成已证事实。

## 4. 为何不能逐步模最小多项式约化

**命题 4。** 设 $D\ne0$，$u$ 为特征零域上代数元，$G\in K[X]$ 是 $u$ 的最小多项式，并假定 $u^3-Du\ne0$。则微分算子
$$
\mathcal L=4(X^3-DX)\partial_X^2
            +6(3X^2-D)\partial_X+12X
\tag{9}
$$
不保持理想 $(G)$，因而不诱导商空间 $K[X]/(G)$ 上的线性算子。

**证明。** 记 $M_X$ 为乘以 $X$ 的算子。假设 $\mathcal L$ 保持 $(G)$。乘以任何多项式也保持 $(G)$，所以交换子 $[\mathcal L,M_X]$ 及其与乘以 $6(3X^2-D)$ 的算子的差都保持 $(G)$。直接对任意多项式求导得到
$$
[\mathcal L,M_X]-6(3X^2-D)=8(X^3-DX)\partial_X.
\tag{10}
$$
于是作用到 $G$ 后应仍属 $(G)$。但其在 $u$ 的值为
$$
8(u^3-Du)G'(u)\ne0,
$$
因为特征零下 $G$ 可分。与属于 $(G)$ 的多项式在 $u$ 处必须为零矛盾。$\square$

在本例中，$v^2=u^3-17u$；若 $v=0$，则 $(u,v)$ 是二扭点。而 $z_0=\Omega_\infty/f$ 在 $\mathbb C/\Lambda_E$ 的消去理想恰为 $(f)$，不被 $2$ 消去。因此 $v\ne0$，命题 4 适用。

所以，可以在完整计算 $B_n$ 之后对 $G$ 取余再求 trace；不能在每轮递推前先丢弃 $G$ 的倍数，再对余式应用 (9)。被丢弃项的导数仍可能有贡献。这个证明排除的是上述特定的固定 $256$ 维矩阵构造，并不排除另一个包含更丰富数据的有效构造。

## 5. 归约后仍需证明什么

固定 $F,u,v$ 并未把 (8) 化成一个固定代数数的素因子问题：待检验的项是 $a_{(p-3)/2}$，索引随 $p$ 变化，模数是 $\mathfrak p^4$。还需要真正的变化素数论证，证明该精确序列满足 (8) 的素数无穷。

本文只证明了递推、trace 恒等式、逐 $p$ 的充分判据，以及一个无效简化的障碍；没有声称已有的 Dirichlet 或 Chebotarev 定理能直接证明 (8)。
