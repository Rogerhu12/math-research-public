# R9：同步权重的整除量不能耗尽现有乘积公式预算

**可信度：已证明。** 本文证明一个关于现有 CM 插值及乘积公式方法的定量边界。它不证明目标不可能，也不排除更强的新算术输入；它说明把各素数处的固定额外中心零阶同步到同一个权重，所得整除量仍小于该方法留下的大小量级。

## 1. 固定对象及精确插值输入

沿用 R6 的
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),\qquad f=34(1+i),
\qquad C=N_{K/\mathbb Q}(f)=2312.
$$
对奇数 $n\ge3$，定义
$$
L_n=(n-1)!\,\Omega_\infty^{-n}L_f(\overline\psi_E^{\,n},n),
\qquad A_n=C^nL_n.
\tag{1}
$$
下标 $f$ 表示去掉导子 $f$ 处的 Euler 因子；这保证所有权重使用同一公式。

使用 Coates–Liang–Sujatha，*The Tate–Shafarevich group for elliptic curves with complex multiplication* (2009)，[原文](https://arxiv.org/pdf/0901.3832)，Proposition 2.4、Theorem 2.5 及式 (32)。对好分裂素数 $q$，在选定 $\mathfrak q\mid q$ 后，有系数整的幂级数 $H_{\mathfrak q}$ 和单位周期 $\Omega_{\mathfrak q}$，满足
$$
\Omega_{\mathfrak q}^{-n}
H_{\mathfrak q}\bigl((1+q)^n-1\bigr)
=L_n\left(1-\frac{\psi_E(\mathfrak q)^n}{q}\right)
\quad\text{当 } n\equiv1\pmod{q-1}.
\tag{2}
$$
在这个分支上，$\overline\psi_E^{\,n}$ 的导子仍是 $f$，所以 (2) 中没有 primitive/imprimitive 的额外差别。定义中心平移后的级数
$$
F_{\mathfrak q}(T)=H_{\mathfrak q}\bigl((1+q)(1+T)-1\bigr).
\tag{3}
$$
若 $E/K$ 的 $\mathfrak q^\infty$-Selmer 余秩至少为 $h$，则该输入给出
$$
F_{\mathfrak q}(T)\in T^h I_{\mathfrak q}[[T]],
\tag{4}
$$
其中 $I_{\mathfrak q}$ 是所用未分歧扩张完备化的整数环。这里只使用由 Selmer 余秩推出消失阶下界的方向，不把特征零阶等同于余不变量维数。

## 2. 同一个权重上的精确整除

**命题 1。** 固定整数 $h\ge1$ 及一个好分裂素数集合 $\mathcal B$。假设对每个 $q\in\mathcal B$，其选定 $\mathfrak q\mid q$ 满足 (4)。对奇数 $n\ge3$，令
$$
\mathcal B(n)=\{q\in\mathcal B:q-1\mid n-1\},
$$
$$
D_h(n)=\prod_{q\in\mathcal B(n)}q^{\,h(1+v_q(n-1))}.
\tag{5}
$$
则 $A_n$ 为非零有理整数，而且
$$
D_h(n)\mid A_n.
\tag{6}
$$

**证明。** 先说明整性。CLS 2009 式 (24) 的已勘误通式，结合 R6 的导数递推，对奇数 $n\ge3$ 给出
$$
f^nL_n=-2a_{(n-3)/2}\in\mathbb Z[i].
$$
这里使用 CLS 续篇对 2009 年式 (24)、(53) 的勘误，分母没有 $w$；精确出处见 R6。由于 $C/f=\bar f\in\mathbb Z[i]$，故 $A_n\in\mathbb Z[i]$。另一方面，$E/\mathbb Q$ 的 CM 角色满足共轭相容性，且 $\Omega_\infty$ 为实周期，因此 $L_n$ 为实数。于是 $A_n\in\mathbb Z[i]\cap\mathbb R=\mathbb Z$。临界值处的 Euler 乘积绝对收敛且非零，故 $A_n\ne0$。

现在取 $q\in\mathcal B(n)$，代入
$$
T_n=(1+q)^{n-1}-1.
$$
因 $q$ 是奇素数，二项展开（或提升指数引理）给出
$$
v_q(T_n)=1+v_q(n-1).
$$
从 (3)–(4) 得
$$
v_{\mathfrak q}\left(H_{\mathfrak q}((1+q)^n-1)\right)
\ge h(1+v_q(n-1)).
$$
$\Omega_{\mathfrak q}$ 为单位，且 $v_{\mathfrak q}(\psi_E(\mathfrak q))=1$，故当 $n\ge3$ 时 (2) 中的 Euler 因子是单位。因此
$$
v_{\mathfrak q}(L_n)\ge h(1+v_q(n-1)).
$$
$L_n$ 是有理数且 $q$ 分裂不分歧，故此即通常的 $q$-赋值下界。$q$ 为好素数，所以 $q\nmid C$。乘上 $C^n$ 不改变这个估值，最后对各个不同 $q$ 合并即得 (6)。$\square$

## 3. 同步条件给出的初等上界

**命题 2。** 对所有奇数 $n\ge3$，记 $m=n-1$，有
$$
\log D_h(n)
\le h\bigl(\tau(m)+1\bigr)\log n
\le h\bigl(2\sqrt m+1\bigr)\log n
=o(n\log n),
\tag{7}
$$
其中 $\tau(m)$ 是 $m$ 的正因数个数。该上界与集合 $\mathcal B$ 无关。

**证明。** 映射 $q\mapsto q-1$ 将 $\mathcal B(n)$ 单射到 $m$ 的正因数集合，并且每个这样的 $q\le n$。所以
$$
\sum_{q\in\mathcal B(n)}\log q\le\tau(m)\log n.
$$
又因为对不同素数只取一次，
$$
\sum_{q\in\mathcal B(n)}v_q(m)\log q\le\log m\le\log n.
$$
将两式相加并乘以 $h$，得到第一个不等式。把正因数按 $d$ 与 $m/d$ 配对，即得 $\tau(m)\le2\sqrt m$。最后 $\sqrt n\log n=o(n\log n)$，完成证明。$\square$

这个估计也覆盖了选择 $n-1$ 为许多 $q-1$ 的公倍数的办法；对所有如此选出的 $n$，上界 (7) 仍然成立。

## 4. 去掉惰性素数强制因子后的实际大小

所用另一个外部输入是 Coates–Liang–Sujatha，*The Tate–Shafarevich group for elliptic curves with complex multiplication II* (2010)，[原文](https://arxiv.org/pdf/1005.4206)，Theorem 2.1 及 §3。对好惰性素数 $\ell$，若 $n\not\equiv1+\ell\pmod{\ell^2-1}$，则
$$
v_\ell(L_n)\ge\left\lfloor\frac{n\ell}{\ell^2-1}\right\rfloor-1.
\tag{8}
$$
我们只取奇数 $n$，所以排除的同余类为偶数类，自动不会出现。定义
$$
P(n)=\prod_{\substack{\ell\le n\\ \ell\equiv3\ (4)}}
\ell^{\,\lfloor n\ell/(\ell^2-1)\rfloor-1},
\qquad \xi(n)=\frac{A_n}{P(n)}.
\tag{9}
$$
这些 $\ell$ 都是 $E17$ 的好素数；当 $\ell\le n$ 时指数非负。由 (8)，$\xi(n)$ 为非零有理整数。$P(n)$ 只含惰性素数，而 $D_h(n)$ 只含分裂素数，因此命题 1 进一步给出
$$
D_h(n)\mid\xi(n).
\tag{10}
$$

**命题 3。** 当奇数 $n\to\infty$ 时，
$$
\log|\xi(n)|=\frac12 n\log n+O(n).
\tag{11}
$$

**证明。** 因为 CM 角色在好素理想上的绝对值是范数的平方根，Euler 乘积一致给出
$$
L_f(\overline\psi_E^{\,n},n)=1+O(2^{-n/2}).
$$
例如取对数后，其绝对值被常数倍的 $\sum_{\mathfrak a\ne(1)}N\mathfrak a^{-n/2}$ 控制；对充分大的 $n$，用收敛于指数 $2$ 的和提取因子 $2^{-n/2}$ 即得到该界。由 (1) 和 Stirling 公式，
$$
\log|A_n|=n\log n+O(n).
\tag{12}
$$
另一方面，
$$
\left\lfloor\frac{n\ell}{\ell^2-1}\right\rfloor-1
=\frac n\ell+O\left(\frac n{\ell^3}+1\right).
$$
对 $\ell\equiv3\pmod4$ 求和并乘以 $\log\ell$，误差为 $O(n)$：$\sum_\ell(\log\ell)/\ell^3$ 收敛，且 Chebyshev 估计给出 $\sum_{\ell\le n}\log\ell=O(n)$。等差数列素数定理的标准推论（亦为 CLS II Lemma 3.1 使用的估计）为
$$
\sum_{\substack{\ell\le n\\\ell\equiv3\ (4)}}\frac{\log\ell}{\ell}
=\frac12\log n+O(1).
$$
所以
$$
\log P(n)=\frac12 n\log n+O(n).
$$
与 (12) 相减即得 (11)。$\square$

## 5. 对本题的准确含义

如果本题对 $E17$ 的主目标失败，则只有有限多个素数的初级部分有限。特别地，除有限多个好分裂 $q$ 外，$t_q>0$。由秩二与根数 $+1$ 的 $q$-parity 结论（CLS 2009 Theorem 2.2 证明中使用的已证输入），$t_q$ 为偶数，所以 $t_q\ge2$。同文式 (37) 及其后的 $n_{E/K}=g_{E/\mathbb Q}$ 把 $E/K$ 的 $\mathfrak q^\infty$-Selmer 余秩识别为 $2+t_q$，故至少为 $4$。从而可以对这个余有限素数集合取 $h=4$，应用上述全部结论。

然而，(7) 与 (11) 同时给出
$$
\log D_4(n)=o(n\log n),\qquad
\log|\xi(n)|=\frac12n\log n+O(n).
$$
因此这些强制整除与现有大小估计没有数值矛盾。把多个 $q$ 同步到一个共同权重，不会仅凭固定四阶中心零点的信息迫使非零整数 $\xi(n)$ 小于其已知因子。

这项结论只限定这一具体乘积公式尝试：新的同余关系、额外整除、远强的大小消去或跨 $p$ 比较仍可能推进问题。本文没有把这一路线的边界当作主问题的否定证明。
