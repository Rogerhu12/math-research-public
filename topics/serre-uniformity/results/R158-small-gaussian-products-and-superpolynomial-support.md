# R158：小高斯主理想的乘积放大与超多项式分母支撑

日期：2026-11-12；会话：serre-uniformity-astra-resume2；负责：cm_denominators；乘积放大及渐近参数由 root 提出，本篇完整展开。

**状态：已证明。** 保持 R157 的实际曲线、首次伴随反循环角色及最小 Tate 指数支撑：
$$
E[p]\simeq A[p],\qquad A:y^2=x^3-x,\qquad p>37,
$$
$$
g=\gcd_{q\mid Z}v_q(Z),\qquad M=pg,\qquad n=v_p(M),
$$
$$
R=\prod_{\substack{q\mid Z\\v_p(p\,v_q(Z))=n}}q,\qquad
C_R=\prod_{q\mid R}(q-\chi_{-4}(q)).
$$
这里 $E$ 是 R19 的实际非 CM 曲线。所有结论同时覆盖三个原始整数族、两种乘法符号以及任意变化的分母支撑。

## 1. 结论及量词

**定理 158.1。** 对每个固定实数 $B>0$，存在常数 $P_B$，使全部实际解满足
$$
p>P_B\quad\Longrightarrow\quad R>p^B.
\tag{158.1}
$$
更准确地，对每个 $\varepsilon\in(0,1)$，存在 $P_\varepsilon$，使全部实际解满足
$$
p>P_\varepsilon\quad\Longrightarrow\quad
\boxed{\log R>
(1-\varepsilon)\frac{(\log p)^2}{\log\log p}.}
\tag{158.2}
$$
所以沿任一实际解序列 $p\to\infty$，
$$
\liminf\frac{\log R\,\log\log p}{(\log p)^2}\ge1.
\tag{158.3}
$$
式 (158.2) 是不预设存在这种无穷序列的准确量词表述。

作为推论，同样的下界适用于 $\operatorname{rad}|Z|$，并有
$$
h(j(E))>
(1-\varepsilon)M\frac{(\log p)^2}{\log\log p}
\quad(p>P_\varepsilon).
\tag{158.4}
$$
证明使用已发表的显式素数计数下界和初等不等式，因此 $P_B,P_\varepsilon$ 均可有效选择；本文不宣称已计算其最小数值。

这些仍是实际分母和高度的**下界**。它们没有给 $R$ 的上界，也没有排除 $R$ 随 $p$ 超多项式增长。因此本篇不完成 O6 或主问题。

## 2. 唯一的新文献输入与已证角色接口

### 2.1 固定模四的显式素数下界

记
$$
\pi_1(Y)=\#\{t\le Y:t\text{ 为素数},\ t\equiv1\pmod4\}.
$$
Bennett–Martin–O'Bryant–Rechnitzer [BMOR] 的已发表 Corollary 1.6，取 $q=4,a=1$，直接给出
$$
\boxed{\pi_1(Y)>\frac{Y}{2\log Y}\qquad(Y\ge800).}
\tag{158.5}
$$
准确阈值来自 $50q^2=800$。这是无条件结论；本文不假设 GRH，也不需要模数随 $p$ 变化的素数分布定理。

### 2.2 R157 的实际全局输入

令
$$
U_R=
\frac{(\mathbb Z[i]/R\mathbb Z[i])^\times}
{(\mathbb Z/R)^\times\langle[i]\rangle}.
$$
R157 给出一个满射
$$
\theta:U_R\longrightarrow(\mathbb F_p,+),
\qquad
|U_R|=\frac{C_R}{2},\qquad
|\ker\theta|=\frac{C_R}{2p}.
\tag{158.6}
$$
对每个非零 $\alpha\in\mathbb Z[i]$，
$$
N(\alpha)<p^2/16
\quad\Longrightarrow\quad
(\alpha,Z)=1,\quad [\alpha]\in\ker\theta.
\tag{158.7}
$$
此外，
$$
R>p^3/50,\qquad
q\mid R\Longrightarrow q\ge4p-1.
\tag{158.8}
$$
如果 $q\mid R$ 在 $\mathbb Q(i)$ 分裂，实际上还有更强的 $q\ge4M^2+1$；本篇的群阶估计只需 (158.8)。

(158.7) 是由实际小 Frobenius 迹完全相等和首次伴随差异推出的全称命题。以下利用其乘法闭包，不把需要验证的素数逐个增加后再外推。

## 3. 一个有限参数的精确核容量不等式

取整数 $s\ge1$，置
$$
Y=(R/4)^{1/s},\qquad N=\pi_1(Y).
$$
暂假设
$$
Y\le p^2/16,\qquad N\ge s.
\tag{158.9}
$$
若 $Y=p^2/16$，也不影响 (158.7) 的严格不等号：$p$ 为奇数，$p^2/16$ 不是整数，所以任意素数 $t\le Y$ 仍严格小于 $p^2/16$。

### 3.1 乘积是原始高斯整数

对每个 $t\equiv1\pmod4$、$t\le Y$，固定其一侧高斯素元
$$
\pi_t=a_t+b_ti,\qquad
t=a_t^2+b_t^2,\qquad a_t>0\text{ 奇},\quad b_t>0\text{ 偶}.
$$
这规定了一个明确选择；不同时使用同一个 $t$ 的共轭素元。由 (158.7)，全部 $\pi_t$ 都与 $R$ 互素，且属于角色核。

对任意由 $s$ 个不同素数组成的集合 $S$，定义
$$
\beta_S=\prod_{t\in S}\pi_t.
$$
则
$$
[\beta_S]\in\ker\theta,\qquad
N(\beta_S)=\prod_{t\in S}t\le Y^s=R/4.
\tag{158.10}
$$
这个范数是平方自由整数。因此 $\beta_S$ 的两个整数坐标互素：若某个有理素数同时整除两个坐标，其平方将整除范数，矛盾。这里原始性来自平方自由范数，不是只假定每个单独因子原始便断言乘积原始。

按全局单位 $\{\pm1,\pm i\}$，将每个 $\beta_S$ 唯一旋转到半开扇区
$$
\{a+bi:a>0,\ -a<b\le a\}.
\tag{158.11}
$$
范数、原始性和角色核性质均不变。

### 3.2 模全局 $\pm i$ 的全部碰撞

若两个这样的扇区代表 $\beta=a+bi$、$\gamma=c+di$ 在 $U_R$ 中同类，则模 $R$，$\beta$ 是 $\gamma$ 或 $i\gamma$ 的有理单位标量倍。各素数分量的有理标量可不同，但所用 $i$ 是同一个全局单位。于是分别有
$$
R\mid ad-bc\quad\text{或}\quad R\mid ac+bd.
\tag{158.12}
$$
由 Cauchy–Schwarz 及 (158.10)，
$$
|ad-bc|,\ |ac+bd|
\le\sqrt{N(\beta)N(\gamma)}
\le R/4<R.
$$
故相应整数准确为零。

在 determinant 为零的情形，两个原始整数向量是相同或反号；扇区实部正，故准确相同。在 dot product 为零的情形，两个向量正交，而半开扇区恰排掉一对可能的相反对角端点，因此不可能发生。这个论证与 R157 的单位规范一致，没有遗漏额外的 $i$ 倍碰撞。

最后，不同素数集合 $S$ 的平方自由范数不同，故它们不可能给出相同高斯整数。因此
$$
\boxed{\binom{\pi_1(Y)}s\le\frac{C_R}{2p}.}
\tag{158.13}
$$
这是对每个满足 (158.9) 的有限参数组都成立的准确不等式。

### 3.3 显式的对数形式

若再有 $Y\ge800$，由 (158.5) 及
$$
\binom Ns
=\prod_{j=0}^{s-1}\frac{N-j}{s-j}
\ge(N/s)^s\qquad(N\ge s),
$$
得到
$$
\binom Ns>
\left(\frac{Y}{2s\log Y}\right)^s
=\frac{R}{4\{2\log(R/4)\}^s}.
\tag{158.14}
$$
与 (158.13) 合并：
$$
p<2\frac{C_R}{R}\{2\log(R/4)\}^s.
\tag{158.15}
$$

令
$$L=\log p,\qquad u=\log R,\qquad Q=4p-1.$$
由 (158.8)，
$$
\begin{aligned}
\log\frac{C_R}{R}
&=\sum_{q\mid R}\log\left(1-\frac{\chi_{-4}(q)}q\right)\\
&\le\sum_{q\mid R}\frac1q
\le\frac{\omega(R)}Q
\le\frac{u}{Q\log Q}.
\end{aligned}
\tag{158.16}
$$
分裂素数的对应对数为负，故也满足所写上界。于是得一个保留完整参数的有效必要条件：
$$
\boxed{
L<
\log2+\frac{u}{(4p-1)\log(4p-1)}
+s\log\{2(u-\log4)\}.
}
\tag{158.17}
$$
它仅要求 (158.9)、$Y\ge800$；未在此处预设 $s$ 固定或 $R$ 为 $p$ 的多项式。

## 4. 每个固定多项式分母支撑都被排除

固定 $B>0$。若 $B<3$，(158.1) 已由 (158.8) 对充分大 $p$ 直接成立。因此可设 $B\ge3$。

反设有一列实际解 $p\to\infty$ 满足 $R\le p^B$。选定一个**固定整数**
$$s>B/2.$$
由 (158.8)，
$$
(p^3/200)^{1/s}<Y=(R/4)^{1/s}
\le(p^B/4)^{1/s}.
$$
因此 $Y\to\infty$；又因 $B/s<2$，对充分大 $p$ 有 $Y<p^2/16$。式 (158.5) 同时保证 $\pi_1(Y)\ge s$。故 (158.13)–(158.17) 全部适用。

由 $u\le BL$，式 (158.16) 的右端趋于零，特别 $C_R/R\le2$ 对充分大 $p$ 成立。于是 (158.15) 给
$$p<4(2B\log p)^s,$$
与固定 $B,s$ 时 $p/(\log p)^s\to\infty$ 矛盾。

这严格证明 (158.1)。常数依赖固定 $B$；没有把任意增长的 $B=B(p)$ 代入刚得到的结论。

## 5. 随 $p$ 优化乘积长度

下面独立处理增长的 $s$，证明 (158.2)，而不把第 4 节的固定参数结论错误地作均匀使用。

固定 $\varepsilon\in(0,1)$。反设有实际解序列 $p\to\infty$，满足
$$
u\le(1-\varepsilon)\frac{L^2}{\log L}.
\tag{158.18}
$$
记
$$
w=u-\log4,\qquad v=2L-\log16,
$$
并取
$$
s=\left\lceil\frac wv\right\rceil,\qquad
Y=e^{w/s}.
\tag{158.19}
$$
由 (158.8)，$u>3L-\log50$，所以当 $p$ 充分大时 $w,v>0$。于是
$$
s\ge w/v,\qquad
s\le w/v+1,\qquad
Y\le e^v=p^2/16.
\tag{158.20}
$$

### 5.1 素数数量条件在增长参数下仍有效

取整不能使 $Y$ 太小。由 (158.20)，
$$
\log Y=\frac ws
\ge\frac{wv}{w+v}.
$$
函数 $w\mapsto wv/(w+v)$ 对 $w>0$ 递增。利用
$w>3L-\log200$，得到均匀下界
$$
\log Y\ge
\frac{(3L-\log200)(2L-\log16)}
{5L-\log3200}
=\left(\frac65+o(1)\right)L.
\tag{158.21}
$$
因此对充分大 $p$ 有 $Y\ge p$，特别 $Y\ge800$。

另一方面，由 (158.18)–(158.20)，
$$s=O_\varepsilon(L/\log L).$$
而由 (158.5)，
$$
\pi_1(Y)>
\frac{Y}{2\log Y}
\ge\frac{p}{4L}
$$
对充分大 $p$ 成立；最后使用 $Y\ge p$ 及 $\log Y\le2L-\log16<2L$。所以 $\pi_1(Y)\ge s$。这完整验证了增长参数下 (158.9) 和全部显式素数计数条件。

### 5.2 主不等式产生矛盾

在 (158.18) 下，
$$
\frac{u}{(4p-1)\log(4p-1)}=o(1).
$$
由 (158.17)、$w<u$ 及 $s\le u/v+1$，
$$
L<
\log2+o(1)+
\left(\frac{u}{2L-\log16}+1\right)\log(2u).
\tag{158.22}
$$
对 $u>1/2$，右侧最后一项关于 $u$ 递增。将 (158.18) 的上界代入，得到
$$
\begin{aligned}
\left(\frac{u}{2L-\log16}+1\right)\log(2u)
&\le
\left(
\frac{(1-\varepsilon)L^2}
{(2L-\log16)\log L}+1
\right)
\log\left(
\frac{2(1-\varepsilon)L^2}{\log L}
\right)\\
&=(1-\varepsilon+o(1))L.
\end{aligned}
\tag{158.23}
$$
这里 $+1$ 造成的误差只有 $O(\log L)$；对数中的 $-\log\log L$ 和固定常数也已包含在 $o(L)$ 中。没有用未控制的增长参数隐常数。

(158.22) 因而要求 $L<(1-\varepsilon+o(1))L$，矛盾。这证明 (158.2)、(158.3)。

## 6. 高度、有效性及仍然开放的量词

因为 $R\mid\operatorname{rad}|Z|$ 且每个 $v_q(Z)\ge g$，R19 的精确分母给
$$
h(j(E))
\ge p\log|Z|
\ge M\log\operatorname{rad}|Z|
\ge M\log R.
$$
代入 (158.2) 即得 (158.4)。

本篇可以有效指定阈值：唯一素数分布输入已在 $Y\ge800$ 显式有效；其余条件只是 (158.20)、(158.21)、$\pi_1(Y)\ge s$ 和 (158.22)–(158.23) 中的初等实函数不等式。给定 $B$ 或 $\varepsilon$ 后，可选一个充分大的明确实数阈值保证这些不等式同时成立。本文没有以无效的 Siegel 常数或变化模数的 PNT 作为隐藏输入。

需要保持的边界是：
$$
\forall B>0\;\exists P_B\;
\forall\text{实际解 }p>P_B:\ R>p^B
$$
并不等价于不存在任意大的 $p$。例如本结论仍允许
$R=\exp\{2(\log p)^2/\log\log p\}$ 这一数量级的增长。这里的例子仅说明量词边界，不宣称该数量级已实现为实际曲线。

新的完整算术约束是：实际首次伴随角色的核必须容纳大量互不相同的原始小主理想乘积；其指数为 $p$ 的全局射线类群无法在多项式支撑中提供足够容量。这比单次小迹筛或单个素数的线性/二次下界更强，但仍须与一个适当的独立全局上界结合才能关闭主缺口。

## 来源

- [R157：首次伴随角色与三次支撑界](R157-first-adjoint-character-and-cubic-denominator-support.md)：实际反循环角色、准确导子、所有小高斯整数的核条件及最初的 $R>p^3/50$。
- [R132：最大同余层支持素数界](R132-maximal-congruence-level-and-split-multiplicative-prime-bound.md)：全部 $q\mid Z$ 的 $q\ge4M-1$，以及分裂素数的更强下界。
- **[BMOR]** Michael A. Bennett, Greg Martin, Kevin O'Bryant, Andrew Rechnitzer, *Explicit bounds for primes in arithmetic progressions*, Illinois J. Math. **62** (2018), nos.1–4, 427–532, DOI [10.1215/ijm/1552442669](https://doi.org/10.1215/ijm/1552442669)。[作者托管的原刊 PDF](https://personal.math.ubc.ca/~bennett/BeMaObRe-IJM-2018.pdf)，Corollary 1.6，印刷 p.433（PDF 第7页）。只用其 $q=4,a=1$、$Y\ge800$ 的下界 (158.5)；其余推导均在本文展开。

