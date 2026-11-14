# 自动分离双池：不规则平方可和主行与双幂辅助夹界

日期：2026-11-13（UTC）。作者：central_review。
状态：完整短证明，供主会话独立核验后登记。
本文使用已证的全阶二位 Bézout 提升，只补齐产生其真实双池的新排序机制。
一般 Hilbert 不变子空间问题仍未完成。

## 1. 沿用的全阶目标与实际双池准则

取任意复序列
$$
a,b\in\ell^2,\qquad c\in\ell^1,
$$
以及任意标量常数，定义
$$
u=a_*+\sum_j a_j\chi_j,\qquad
w=b_*+\sum_j b_j\chi_j,\qquad
v_c=\sum_j c_j(\chi_j-1).
$$
对每个固定整数 $k\ge0$，沿用准确共振族
$$
F_k=k![t^k]\exp\left(
tu+\sum_{n=2}^k\frac{2^{n-1}}n t^n
\sum_j a_j^n(\chi_j-1)
\right).
\tag{1.1}
$$
特别地，
$$
F_0=1,\qquad F_1=u,\qquad
F_2=u^2+2\sum_j a_j^2(\chi_j-1).
$$
固定任意非恒定标量多项式
$$
q(z)=\sum_{k=0}^p q_kz^k,\qquad p\ge1,\quad q_p\ne0,
$$
并记
$$
F_q=\sum_{k=0}^p q_kF_k.
$$

已证的全阶二位 Bézout 准则如下。
若沿无穷整数子序列 $N$，存在不交的真实物理位池
$I_N,J_N$，各有 $N$ 位，满足
$$
\min(I_N\cup J_N)\ge\mu N,\qquad
\max_{j\in I_N\cup J_N}|a_j|\le C_aN^{-1/2},
\tag{1.2}
$$
且
$$
d_N:=\min_{j\in I_N,k\in J_N}|a_kc_j-a_jc_k|>0,
\qquad
1+\log^+d_N^{-1}=O(N^{3/2}),
\tag{1.3}
$$
则对于每个固定 $q$ 和每个 $\lambda\in\mathbb C$，
$$
\boxed{[F_q+v_c-\lambda]e^w\text{ 非零且对原 }A\text{ 循环}.}
\tag{1.4}
$$

该准则已在真实自然域上支付全部 $G_n$ 系数的反射 jets、
输入多项式绝对系数、重复位 carry、两池各自的阶乘平均、
以及任意固定局部测试的四次成本。
以下仅验证 (1.2)–(1.3)，不改变这些已经证明的算子步骤。

假设 $a$ 有无穷多个非零项。
令
$$
\rho_1\ge\rho_2\ge\cdots>0
$$
为其非零幅度的递减重排，重幅度处任意固定排序。
所有排序位置均保留其原真实物理位标签；
本稿不以排序位置取代物理位。

## 2. 平方可和行自动出现固定比例降幅

**引理 1。**
给定任意 $0<\delta<1$，取整数 $L>\delta^{-2}$ 并置 $K=3L$。
对于任意非零无限平方可和递减行 $\rho$，
有无穷多个整数 $N$ 满足
$$
\boxed{\rho_{KN}\le\delta\rho_{3N}.}
\tag{2.1}
$$

证明。平方可和及单调性给
$$
n\rho_n^2\longrightarrow0.
\tag{2.2}
$$
例如，
$$
\frac n2\rho_n^2
\le \sum_{\lfloor n/2\rfloor\le k\le n}\rho_k^2
\longrightarrow0.
$$
如果 (2.1) 只有有限多个解，则存在 $N_0$，使它对所有
$N\ge N_0$ 都失败。
沿整数列 $N_j=L^jN_0$，这给
$$
\rho_{3N_{j+1}}>\delta\rho_{3N_j},
\qquad
N_j\rho_{3N_j}^2>
N_0\rho_{3N_0}^2(L\delta^2)^j.
$$
右边趋于无穷，而左边由 (2.2) 趋零，矛盾。
证毕。

这个结论不要求点态幂律、正则变化、相邻幅度比的下界或平台长度的上界。

## 3. 只有一个排序对数下界的不规则全阶定理

**定理 2。**
设某个实数 $\kappa>1$ 和常数 $c_-,c_+>0$ 满足：
对全部充分高的非零主物理位，
$$
c_-|a_j|^\kappa\le |c_j|\le c_+|a_j|^\kappa.
\tag{3.1}
$$
仍单独假设 $c\in\ell^1$。
主行零位上的辅助只须可和，不要求为零。
若
$$
\boxed{\log^+\rho_n^{-1}=O(n^{3/2})\quad(n\longrightarrow\infty),}
\tag{3.2}
$$
则 (1.4) 对全部固定非恒定 $q$、全部 $\lambda$ 成立。
所有复相位、主行的任意物理排列及有限物理头例外均允许。

证明。取
$$
0<\delta\le
\min\left\{\frac12,
\left(\frac{c_-}{2c_+}\right)^{1/(\kappa-1)}\right\},
$$
再固定整数 $L>\delta^{-2}$ 和 $K=3L$。
由引理 1，沿无穷子序列 $N$ 有 (2.1)。

在非零幅度排序中取两个秩带
$$
(N,3N],\qquad (KN,(K+2)N].
\tag{3.3}
$$
每个秩带都有 $2N$ 项。
从每个秩带删除原物理位小于 $N$ 的项，最多各删 $N$ 项，
然后各取恰好 $N$ 项为 $I_N,J_N$。
充分大的 $N$ 同时删除了 (3.1) 的全部有限物理例外。
两个池不交，而且
$$
\min(I_N\cup J_N)\ge N,\qquad
\max_{I_N\cup J_N}|a_j|
\le\rho_{N+1}\le\|a\|_2N^{-1/2}.
\tag{3.4}
$$

对 $j\in I_N,k\in J_N$，有
$$
|a_j|\ge\rho_{3N},\qquad
\rho_{(K+2)N}\le|a_k|\le\rho_{KN}\le\delta\rho_{3N}\le\delta|a_j|.
$$
于是
$$
\left|\frac{c_k}{a_k}\right|
\le c_+|a_k|^{\kappa-1}
\le c_+\delta^{\kappa-1}|a_j|^{\kappa-1}
\le\frac12c_-|a_j|^{\kappa-1}
\le\frac12\left|\frac{c_j}{a_j}\right|.
\tag{3.5}
$$
无论两个比值具有何种复相位，反三角不等式均给
$$
\begin{aligned}
|a_kc_j-a_jc_k|
&=|a_ja_k|
\left|\frac{c_j}{a_j}-\frac{c_k}{a_k}\right|\\
&\ge\frac{c_-}{2}|a_j|^\kappa|a_k|\\
&\ge\frac{c_-}{2}\rho_{3N}^{\kappa}\rho_{(K+2)N}.
\end{aligned}
\tag{3.6}
$$
因此
$$
1+\log^+d_N^{-1}
\le C+\kappa\log^+\rho_{3N}^{-1}
+\log^+\rho_{(K+2)N}^{-1}
=O(N^{3/2})
$$
由 (3.2) 成立。
(3.4)、(3.6) 正是实际双池准则的全部输入，故得 (1.4)。
证毕。

常数 $K$ 可以很大，但在整个无穷子序列中固定。
它只改变双池准则的固定成本及最终选取的平均参数，
不改变 $N^{3/2}$ 的阶数。

### 3.1 适用范围与准确限制

条件 (3.2) 允许任意不规则平台与跳跃，
只要求幅度在每个排序位置不小于某个 $\exp(-C n^{3/2})$。
因此不必有两侧相同幂律，也不必有两侧伸缩指数模型。

这一条件是对所有充分大排序位置的下界。
不能仅凭某个无穷子序列上的 (3.2)，
就把 (3.6) 中同时出现的 $3N$ 与 $(K+2)N$ 两处下界补出来。

$\kappa>1$ 足以分离两个比值；$\kappa>2$ 不是本定理所需。
若 $\kappa\le2$，辅助可和性仍须作为独立假设保留。
即使 $\kappa>2$，主行零位上的任意辅助也须另行可和。

## 4. 两种不同幂次夹住辅助的定理

本节不要求辅助与同一个幂次上下比较。

**定理 3。**
设主行非零幅度满足
$$
A_-n^{-\sigma}\le\rho_n\le A_+n^{-\sigma},
\qquad \sigma>\frac12,\quad A_-,A_+>0.
\tag{4.1}
$$
若对全部充分高的非零主物理位有
$$
c_-|a_j|^{\kappa_+}\le|c_j|\le c_+|a_j|^{\kappa_-},
\qquad
1<\kappa_-\le\kappa_+,
\tag{4.2}
$$
并且 $c\in\ell^1$，则全部 (1.4) 成立。
有限例外与主行零位辅助的规定同定理 2。

证明。固定实数
$$
\tau>\frac{\kappa_+-1}{\kappa_--1}\ge1,
\qquad M_N=\lceil N^\tau\rceil.
\tag{4.3}
$$
取两个排序带
$$
(N,3N],\qquad(M_N,M_N+2N].
\tag{4.4}
$$
充分大时它们不交。
每带都有 $2N$ 项，分别删除原物理位小于 $N$ 的项后，
各取 $N$ 项。
仍得到 (3.4)，不需要第二带具有长度与其起点成比例。

第一池中的比值有下界
$$
\left|\frac{c_j}{a_j}\right|
\ge c_-|a_j|^{\kappa_+-1}
\ge C_1N^{-\sigma(\kappa_+-1)}.
$$
第二池中则有上界
$$
\left|\frac{c_k}{a_k}\right|
\le c_+|a_k|^{\kappa_--1}
\le C_2N^{-\tau\sigma(\kappa_--1)}.
$$
由 (4.3)，第二个上界最终小于第一个下界的一半。
所以与 (3.6) 相同的反三角估计给
$$
\begin{aligned}
|a_kc_j-a_jc_k|
&\ge\frac{c_-}{2}|a_j|^{\kappa_+}|a_k|\\
&\ge C N^{-\sigma\kappa_+}(M_N+2N)^{-\sigma}\\
&\ge C' N^{-\sigma(\kappa_++\tau)}.
\end{aligned}
\tag{4.5}
$$
故 $1+\log^+d_N^{-1}=O(\log N)$。
实际物理双池准则立即适用。
证毕。

(4.2) 允许辅助的有效幂次随物理位变化，
也允许处于两种幂之间的任意振荡幅度和任意相位。
这里没有额外要求 $\sigma\kappa_->1$：
如果它成立，(4.2) 的上界本身保证主支撑上的可和性；
如果它不成立，单独的 $c\in\ell^1$ 假设仍可能成立，并须保留。

## 5. 来源与后续边界

- [全阶二位 Bézout 完整源](2026-11-13-all-order-resonant-two-site-bezout-and-derivation-budgets-central-review.md)：
  实际自然域、全阶反射 jets、标量行列式输入及全部局部配对成本。
- [二位二次完整源](2026-11-13-two-site-scalar-bezout-lifts-and-late-support-quadratic-cyclicity-central-review.md)：
  物理位双池、绝对系数预算、两次阶乘的精确归一化。
- [R176](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)：
  所使用的自然闭多项式与核内有界 first。
- [R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)：
  任意跨度的真实导子与最高位壳估计。

本文仅给产生可用双池的新充分条件。
没有把所有平方可和行都宣称满足 (3.2)，
也没有把任意慢辅助归入 $\mathcal G$。
对不满足 (3.2) 的非可和主行，
可以进一步研究“可用第二带 / 实际辅助尾极小”的二分；
该路线需要真实全阶联合逆的另一个完整证明。
