# R239 附录：矩形最高次数给出的全局一阶约束

- 日期：2026-11-13。
- 作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。
- 状态：以下均值界和联立线性约束已证明。它们是同一个实际矩形的必要条件，不单独宣称异常位四次式正性。
- 输入：[实际 Pearson 双对角身份](R239-appendix-actual-binomial-pearson-bidiagonal-and-full-shear-elimination.md)以及[固定矩形 Turán 端点曲率上界及自足单调性证明](R239-appendix-rectangular-turan-endpoints-and-sharp-curvature-caps.md)。后者使用 Suvrit Sra, *Monotonicity of Turán-ratios of symmetric polynomials* (2026), §2 的单调性；仓库已有完整证明。

## 1. 单点曲率上界的正确积分

固定 $N\ge2$、$1\le D<N$、$t\ge1$，令
$$
S_j(z)=s_{(t^D)}(z^{[j]},1^{[N-j]}),\quad
f_j(\theta)=\log S_j(e^\theta),\quad 0\le j\le N.
$$
本文只写 $z>1$；倒数权对偶给 $0<z<1$。记
$$
\ell_j=t\min(j,D),\qquad
C_j=\frac{t\min(j,D)[N-\max(j,D)]}{t+|j-D|}.
$$
真实最高项给 $f_j'(+\infty)=\ell_j$。已证曲率上界为
$$
0\le f_j''(\theta)\le C_j\frac{e^\theta}{(e^\theta-1)^2}.
$$
因此直接积分得到
$$
0\le\ell_j-f_j'(\theta)
=\int_\theta^\infty f_j''(u)\,du
\le\frac{C_j}{z-1}.
\tag{1.1}
$$
积分无发散问题，因为下限 $\theta>0$，而被积上界在无穷处可积。另一方面，所有 Schur 单项式的总次数为 $tD$，变量对称性在 $z=1$ 给
$$
f_j'(0)=jtD/N.
$$
曲率非负使 $f_j'(\theta)\ge jtD/N$。合并得到同一矩形的点态均值区间
$$
\boxed{L_j\le f_j'(\theta)\le U_j,\qquad
L_j=\max\{jtD/N,\ \ell_j-C_j/(z-1)\},\quad U_j=\ell_j.}
\tag{1.2}
$$
$j=0,N$ 的端点亦准确成立，其中 $f_0'=0,f_N'=tD$。

## 2. Pearson 均值差与局部范数比

在真实异常位模型里，$N=h+1$、$D=\delta+1$，旧范数满足
$$
\boxed{e_j:=(z-1)\frac{a_{j+1}}{b_{j-1}}
=(j+1)f_j'-jf_{j+1}',\qquad1\le j<N.}
\tag{2.1}
$$
这里所有范数是原首一范数；$b_{-1}=\infty$ 只编码零逆项，故另有 $e_0=0$。式 (2.1) 并不允许为不同位置独立选择 $f_j'$。

例如逐项用 (1.2) 已给
$$
\boxed{(j+1)L_j-jU_{j+1}\le e_j
\le(j+1)U_j-jL_{j+1}.}
\tag{2.2}
$$
特别是 $j\ge D$ 时
$$
\boxed{e_j\ge tD-\frac{(j+1)C_j}{z-1}.}
\tag{2.3}
$$
这与单个曲率上界不同：它同时联系矩形宽 $t$、曲率累积和相邻层的范数比。

## 3. 同一均值序列的全部局部兼容约束

对 $1\le j<k\le N$，将 (2.1) 除以 $j(j+1)$ 后求和，准确得到
$$
\boxed{\frac{f_j'}j-\frac{f_k'}k
=\sum_{i=j}^{k-1}\frac{e_i}{i(i+1)}.}
\tag{3.1}
$$
因此必须有
$$
\boxed{
\frac{L_j}j-\frac{U_k}k
\le\sum_{i=j}^{k-1}\frac{e_i}{i(i+1)}
\le\frac{U_j}j-\frac{L_k}k.
}
\tag{3.2}
$$
这些不等式不限于相邻两层。

给定连续下标集合 $J=\{r,\ldots,s\}$ 及其内部 $e_i$，它们还等价于一个可复查的区间相交条件。令
$$
E_r=0,\qquad E_j=\sum_{i=r}^{j-1}\frac{e_i}{i(i+1)}\quad(j>r).
$$
由 (3.1)，全部 $f_j'/j$ 必写成一个共同实数 $v$ 减去 $E_j$。因此存在满足 (1.2)、(2.1) 的局部均值，当且仅当
$$
\boxed{\max_{j\in J}\left(\frac{L_j}j+E_j\right)
\le\min_{j\in J}\left(\frac{U_j}j+E_j\right).}
\tag{3.3}
$$
这只是均值层面的精确可行性条件，仍不保证给定范数来自实际矩形。特别不能据此省略下矩形的联立关系。

## 4. 四次式的四个曲率位置

设 $2\le n\le h-2$，沿用局部范数
$$
a=a_{n-1},\ b=a_n,\ c=a_{n+1},\ d=a_{n+2},\quad
p=b_{n-2},\ q=b_{n-1},\ r=b_n,\ s=b_{n+1}.
$$
在 $J=\{n-1,n,n+1,n+2\}$ 上，三个可见差量是
$$
e_{n-1}=(z-1)b/p,\qquad
e_n=(z-1)c/q,\qquad
e_{n+1}=(z-1)d/r.
\tag{4.1}
$$
将它们代入 (3.3) 才保留四个位置共同来源的一阶约束。低端 $n=1$ 时单独保留 $f_0\prime=0$，只在 $J=\{1,2,3\}$ 上使用含 $1/j$ 的区间公式，绝不令 $j=0$ 进入分母；高端可含 $j=N$，其均值已固定。其余不存在的范数项按真实零空间去掉。

例如曾出现满足四个有限宽曲率 cap 的松弛参数
$$
n=7,\ m=2,\ D=5,\ t=744,\ z=1.05915584,\quad
c/b=1.3670754,\ b/q=4523.3009.
$$
这里 $N=10$。用所写十进制作为准确有理数，(4.1) 的 $e_7$ 约为 $365.802$，而 (2.3) 要求 $e_7\ge1696.898$。故该松弛点并非实际矩形参数。这个排除只说明单点曲率界漏掉了全局均值联系；不构成完整相邻比较的证明。
