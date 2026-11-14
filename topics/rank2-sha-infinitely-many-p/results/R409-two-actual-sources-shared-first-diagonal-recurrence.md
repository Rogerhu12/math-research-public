# R409：两条真实来源的共享首权递推与有限联合证书

日期：2026-11-14。**状态：本篇的固定有理递推、全部指定素数处的无分母模 $p$ 算法和首层充分判据均已证明；末节另记录有限精确计算。没有证明递推的两个指定对角对无穷多个素数不同时为零，有限计算不改变主目标状态。**

本篇直接使用 R398/R404 已识别的两个真实六 sigma 来源。将它们共同缩放到 $E_1:y^2=x^3+1$，所得首项一函数分别记为 $A_{34}$、$A_{72}$。这和 R303、R402 的定义相同，而不是另选两个 theta 截面。

## 1. 不依赖 p 的三个固定递推

令 $q=z^6$，定义
$$
W(q)=z^2x(z)=\sum_{n\ge0}X_nq^n,
\qquad F(q)=\log(\sigma(z)/z)=\sum_{n\ge1}f_nq^n.
$$
则
$$
\boxed{X_0=1,\quad X_1=-\frac17,\qquad
X_n=\frac{\sum_{i=1}^{n-1}X_iX_{n-i}}{(6n+1)(n-1)}\quad(n\ge2),}
\tag{1}
$$
$$
\boxed{f_n=-\frac{X_n}{6n(6n-1)}.}\tag{2}
$$
再定义固定整数序列
$$
\boxed{t_0=2,\quad t_1=-286,\qquad
t_{n+2}=-286t_{n+1}-117649t_n.}\tag{3}
$$
置
$$
\begin{aligned}
d_n^{34}&=(-27)^n+(-1728)^n+t_n+1+64^n,\\
d_n^{72}&=(-27)^n+(-1728)^n+t_n+(-19683)^n+4096^n.
\end{aligned}\tag{4}
$$
两条目标递推的初值都是 $c_0^{34}=c_0^{72}=1$，并满足
$$
\boxed{
c_n^N=\frac1n\sum_{j=1}^{n}j f_jd_j^N c_{n-j}^N,
\qquad N\in\{34,72\},\quad n\ge1.
}\tag{5}
$$

**定理 1。** 以上所有序列都在 $\mathbf Q$ 中唯一确定，且准确有
$$
\boxed{A_N(z)=z^6\sum_{n\ge0}c_n^Nz^{6n}\qquad(N=34,72).}\tag{6}
$$
特别地，两个序列是同一固定 $F$ 的实际六因子指数卷积；没有把函数乘法换成 Mellin 乘法。

**证明。** 原微分给 $x'=2y$、$y'=3x^2$，故 $x''=6x^2$。比较 $z^{6n-4}$ 系数，$n\ge2$ 时有
$$
((6n-2)(6n-3)-12)X_n
=6\sum_{i=1}^{n-1}X_iX_{n-i}.
$$
左边括号等于 $6(6n+1)(n-1)$，给出 (1) 的递推。由 $(x')^2=4x^3+4$ 比较常数项，得到 $-16X_1=12X_1+4$，故 $X_1=-1/7$。再由 $(\log\sigma)''=-x$ 得 (2)。这些等式同时给实际 Weierstrass/sigma 级数的唯一性。

取 $\gamma=(5+\delta)/2$、$\delta^2=-3$。R404 的实际源为
$$
\begin{aligned}
A_{34}(z)&=-\frac1{84}\,
\sigma(\delta z)\sigma(2\delta z)\sigma(\gamma z)
\sigma(\bar\gamma z)\sigma(z)\sigma(2z),\\
A_{72}(z)&=-\frac1{504\delta}\,
\sigma(\delta z)\sigma(2\delta z)\sigma(\gamma z)
\sigma(\bar\gamma z)\sigma(3\delta z)\sigma(4z).
\end{aligned}\tag{7}
$$
每个 $\sigma(az)=az\exp(F(a^6q))$。六个 $a$ 的乘积准确抵消 (7) 的归一常数，保留下来的首项是 $z^6$。
又有 $\gamma+\bar\gamma=5$、$\gamma\bar\gamma=7$，直接六次幂计算给
$$
\gamma^6+\bar\gamma^6=-286,\qquad
\gamma^6\bar\gamma^6=7^6=117649.
$$
故 (3) 准确等于 $t_n=\gamma^{6n}+\bar\gamma^{6n}$，其余四个六次幂正是 (4) 所列整数。这给出全函数身份
$$
\frac{A_N(z)}{z^6}
=\exp\left(\sum_{n\ge1} f_nd_n^Nq^n\right).
\tag{8}
$$
对 (8) 作 $q$ 的对数微分并比较系数，便得到 (5)。因此 (6) 对全部系数成立。$\square$

例如准确的前两项为
$$
\begin{array}{c|cc}
&c_1&c_2\\\hline
34&-988/105&16594771/1576575\\
72&-2938/35&-230804229/175175
\end{array}\tag{9}
$$
两条一次项之差为 $-1118/15$，与 R403 的真实 $H_{38}-1$ 一致。这里的一致性是核对归一；(7)–(8) 已证明全部系数身份，不以这几个数识别来源。

## 2. 指定 prime diagonal 全程可以在 Fp 计算

取
$$
p\ge11,\qquad p\equiv5\pmod6,\qquad s=(p+1)/6.
\tag{10}
$$
只需在 (1)–(5) 中计算 $0\le n\le s-1$。所有出现的除数都是 $p$ 单位：
$$
1\le n<p,\quad 6n+1\le p-4,\quad
6n\le p-5,\quad 6n-1\le p-6,
$$
而初始固定除数为七；(1) 中 $n-1=0$ 的唯一位置 $n=1$ 已另给初值，不执行除法。
因此在此截断内所有 $X_n,f_n,c_n^N$ 都属于 $\mathbf Z_{(p)}$，逐步模 $p$ 递推与真实有理系数约化完全相同。

**定理 2。** 定义
$$
a_p^{34}=c_{s-1}^{34}\bmod p,\qquad
a_p^{72}=c_{s-1}^{72}\bmod p.
\tag{11}
$$
它们准确就是同一物理底曲线上的
$$
\boxed{a_p^N=[z^{p+1}]A_N\bmod p.}\tag{12}
$$
这对全部 (10) 的素数成立。算法只需两个相同长度的指数卷积及一个共享 $W$ 递推，使用 $O(s^2)$ 次域运算和 $O(s)$ 个域元素；不需要生成完整中央无限级数、近似周期或高阶 theta 矩阵。

证明已经包含在上述整性界和 (6) 中。算法没有在临界 $n=s$ 处尝试把 sigma 的真 $p$ 分母约去；由于目标来源从 $z^6$ 起，所需最高位置恰好是 $s-1$。

## 3. 回到两条真实中央的准确首层

本节共同使用两曲线时另取 $p\ne17$。令 $c=[z^{p+1}]\log(\sigma/z)$。R301/R303/R402 已给
$$
v_p(c)=-1,\qquad
pc\equiv-(-1)^s4^{-s}\binom{2s}{s}\pmod p.
\tag{13}
$$
因 $2s<p$，右端是单位。对同一实际 Gaussian/下降阶乘 Newton 变换，既有完整尾估计给
$$
\boxed{
\frac{J'_{N,p}(0)}p\equiv
\frac{a_p^N}{N\,pc}\pmod p,
\qquad N=34,72.
}\tag{14}
$$
在共同好范围还须排除 $p=17$；没有因为计算是在 $E_1$ 上进行就忘记物理 $E_{17}$ 的坏约化。

物理曲线 $y^2=x^3+17$ 的系数乘 $17^{(p+1)/6-1}$，物理 $E_{24}$ 的系数乘 R402 的 $C_{24}\theta^{p+1}$。在共同范围这些均是单位，并且 Gaussian 参数按同一缩放运输，故 (14) 的非零条件保留。
结合 R303、R402 中包含全部 Sha 的原 Selmer 比较，有
$$
\begin{aligned}
a_p^{34}\ne0&\Longrightarrow
\Sha(E_{17}/\mathbf Q)[p^\infty]\text{有限},\\
a_p^{72}\ne0&\Longrightarrow
\Sha(E_{24}/\mathbf Q)[p^\infty]\text{有限}.
\end{aligned}\tag{15}
$$
此处 $E_{17}$ 专指本篇的 $y^2=x^3+17$，并非旧四次 CM 曲线 $y^2=x^3-17x$。

于是两条完整中央同时失败的一个必要条件是
$$
\boxed{a_p^{34}=a_p^{72}=0.}\tag{16}
$$
(16) 不等价于完整失败：若首层为零，仍应继续 R303/R402 的更高有限 Newton 证书。
若今后能证明无穷多个共同好 $p$ 不满足 (16)，有限鸽巢原理才会给出一条固定曲线在无穷多个 $p$ 上初级有限。目前没有证明这个无穷性命题。

## 4. 有限精确计算记录，不作为无穷性输入

按上面的已证模 $p$ 递推，计算全部 $11\le p\le10000$、$p\equiv5\pmod6$ 的素数，得到：

| 范围或例外 | 精确结果 |
|---|---|
| 素数总数 | 615 |
| 两曲线共同好素数数目（排除17） | 614 |
| $a_p^{34}=0$ | $p=17,29$ |
| $a_p^{72}=0$ | $p=113,3623$ |
| 两个首层同时为零 | 此有限范围内没有 |

因此在这 614 个共同好素数处至少一条原首层证书命中。对每条曲线单独而言，这仍只是有限多个初级部分的结论；不能把没有搜到共同零点写成全素数定理。

复算源为 [check-r409-joint-first-diagonal.cpp](../scripts/check-r409-joint-first-diagonal.cpp)，参数和输出哈希为 [check-r409-joint-first-diagonal-summary.json](../scripts/check-r409-joint-first-diagonal-summary.json)。完整 CSV 可由脚本重新生成，不重复提交中间表。其 8566 字节输出的 SHA-256 为
`4d18bcb262d9e25862e4786988de655276c18cc641c5ade6feac4a676aaebbf3`。
另以 R398 的实际 $\sigma^Nx^j$ 多项式表达在有理数中展开到 $q^6$，核对了 $p=11,17,23,29,41$ 的两条结果；该核对未替代上面的全参数证明。

直接依赖：R398/R404 的原六 sigma 身份、R303/R402 的原中央首层和完整 Selmer 桥；(1)–(8) 和整性截断在本文直接证明。
