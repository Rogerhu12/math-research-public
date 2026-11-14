# 固定差分逆像没有椭圆函数系数的线性微分方程

日期：2026-11-12。**状态：已证明。**

沿用 R28 及 `2026-11-12-difference-entire-uniformization.md`：
$a=69$，$\Phi\in K(E)^\times$ 的零极点支撑 $S$ 被 $[a]$ 逐点固定，
$\Phi(O)=1$，$\delta\log\Phi(O)=0$。令
$$
\mathcal F_{m,c}(z)=e^{cz}
\prod_{j\ge0}
\Phi\!\left(\exp_E\frac{z}{a^{m+j}}\right)^ {e_{m,j}},
\qquad
e_{m,j}=a^j\binom{m+j-1}{j},
\tag{1}
$$
其中 $m\ge1$。前一笔记已证明此乘积在全平面亚纯，
在原点给出固定差分方程的形式解 $F_{m,c}$。

## 1. 同一代数点上出现无界的分支消失阶

选 $\Phi$ 的一个零点 $s\in S$，记
$$
d_s=\operatorname{ord}_s\Phi>0.
$$
这样的点存在，因为 $\Phi$ 是射影曲线上的非常数有理函数。
取 $z_s\in\mathbb C$，使 $\exp_Ez_s=s$，并令
$$
z_n=a^{m+n}z_s\qquad(n\ge0).
$$
因为 $[a]s=s$，有 $\exp_Ez_n=s$。
对 $0\le j\le n$，第 $j$ 个因子的内部点为
$$
\exp_E\frac{z_n}{a^{m+j}}=[a]^{n-j}s=s,
$$
所以该因子在 $z_n$ 有零阶 $d_s e_{m,j}$。
通用覆盖及 $z\mapsto z/a^{m+j}$ 都局部无分歧，因此没有额外的分歧乘数。

若 $j>n$，记该内部点为 $u_j$，则
$[a]^{j-n}u_j=s$。
若 $u_j\in S$，由于 $[a]$ 逐点固定 $S$，必有 $u_j=s$。
因此后续因子若在 $z_n$ 有零极点，只能也是零点，不能有极点抵消。
对充分大的 $j$，内部参数趋于零，尾乘积全纯非零；
故实际只有有限个因子参与此处的零阶。
因 $e^{cz}$ 处处非零，得到
$$
\operatorname{ord}_{z_n}\mathcal F_{m,c}
\ge d_s\sum_{j=0}^{n}e_{m,j}\longrightarrow+\infty.
\tag{2}
$$

## 2. 线性微分方程的局部亚纯解不能有无界消失阶

**命题。** 不存在 $r\ge0$ 及不全为零的 $A_0,\ldots,A_r\in\mathbb C(E)$，
使
$$
\sum_{j=0}^{r}A_j\delta^jF_{m,c}=0
\tag{3}
$$
作为 $O$ 处形式恒等式成立。

**证明。** 可令 $A_r\ne0$。若 $r=0$，因 $F_{m,c}\ne0$，立即矛盾。
以下设 $r\ge1$。

在复通用覆盖上，$\delta$ 对应 $d/dz$，且每个
$A_j(\exp_E z)$ 是亚纯函数。式 (3) 在原点附近成立，
故由亚纯函数恒等定理在整个复平面成立。

在 $s$ 处取代数局部参数 $u$。对每个 $n$，通用覆盖在 $z_n$
附近给出局部同构，其逆把 $\mathcal F_{m,c}$ 变成一个非零亚纯 germ
$f_n\in\mathbb C((u))$。
所有这些 $f_n$ 都满足同一个局部线性微分方程 (3)，
而它们的消失阶由 (2) 趋于无穷。

设 $V\subset\mathbb C((u))$ 是这个方程的局部亚纯解空间。
有 $\dim_{\mathbb C}V\le r$：可在避开系数极点及最高系数零点的
一个小穿孔圆盘中选普通点，解由该点的前 $r$ 个初值唯一决定；
等价地，可用线性微分方程的 Wronskian 维数界。

对任意有限维子空间 $V\subset\mathbb C((u))$，其非零元素的
$u$-进阶数有统一上界。确实，令
$$
V_N=V\cap u^N\mathbb C[[u]].
$$
$V_N$ 是下降的有限维子空间链，最终稳定；而
$\bigcap_NV_N=0$，所以稳定值为零。
于是充分大的 $N$ 后，$V$ 中没有阶数至少 $N$ 的非零元素。
这与 $f_n$ 的无界消失阶矛盾。$\square$

## 3. 适用性边界

这个结论排除了把固定差分逆像直接识别为椭圆曲线上线性连接的一个
水平解；因此也排除了直接把它当作线性 Picard–Fuchs 系统的一个分量。
若分量来自有限秩线性系统，消元就会产生 (3)。
本命题没有声称排除所有非线性代数微分方程。

相关近期正向定理已核查：Y. H. J. Lam、D. Litt，
*Algebraicity and integrality of solutions to differential equations*，
[arXiv:2501.13175，2025](https://arxiv.org/abs/2501.13175)，
Theorem 1.3.4 对椭圆曲线族的 Picard–Fuchs 连接给出整形式水平解的
代数性；Theorem 1.2.4 处理具有指定 Picard–Fuchs 初值的 isomonodromy 叶。
一般非线性方程的相应断言仍列为 Conjecture 1.1.1 / 1.1.6。
当前 $F_{m,c}$ 没有被实现为该非线性定理中的对象，
而上面的完整证明已经排除直接使用线性 Picard–Fuchs 版本。

这不影响 Bost–Chambert-Loir 的一般形式曲线代数化判据：
该判据不要求线性微分方程，真正未解决的输入仍是固定图像的全部有限处大小。
