# 完整尖点 jet 的满秩与三角形分母深度

日期：2026-11-12。状态：自含的条件性加强；保持真实秩零商及非零中心值谱前提。暂未分配 R 编号。

本篇接 R150。它不证明一般三色 Fourier 理想为单位，也不处理所有三次中心值同时为零的分支。新增的是：若同一个实际非零中心值谱在最初若干 Fourier 系数上满秩，可以在同一尖点作整的 adjugate 消元，得到分布在不同圆分素理想上的三角形深度。

## 1. 三阶结论

保留 R69、R72、R137、R150 的实际设定。设 $p>37$ 是真实小惯性完整非分裂正规化子分支的素数，$\mathcal F$ 是所有非零三次中心值的归一化水平 $p$、权二新形式，包含其完整 Galois 轨道。假设 $\mathcal F$ 非空，故已有同一完整层扭曲曲线的真实秩零商及饱和整微分接口。

记
$$
\operatorname{den}j(F)=D^p,
\qquad
J_p=(A_p(\theta),B_p(\theta))\subset\mathcal O_{\mathbb Q(\zeta_p)^+},
\qquad N_p=N(J_p).
$$

**命题。** 若
$$
\operatorname{rank}_{\overline{\mathbb Q}}
\begin{pmatrix}
1&a_2(f)&a_3(f)
\end{pmatrix}_{f\in\mathcal F}=3,
\tag{1.1}
$$
则
$$
\boxed{D^6\mid N_p.}
\tag{1.2}
$$
因此 R137 的同一个 Parseval 上界给
$$
\log\operatorname{den}j(F)
\le \frac{p(p-1)}{24}
\log\left(\frac{2p}{9}-\frac4{9(p-1)}\right).
\tag{1.3}
$$
条件 (1.1) 是实际非零谱的条件；不能只由存在三个归一化形式、或三个形式各自的系数不同来代替它。特别地，若全部 $a_3$ 是 $1,a_2$ 的同一线性组合，则该条件不成立。

## 2. Galois 稳定的 minor 与严格小于一的赋值

固定实际分母素数 $\ell$，令 $m=v_\ell(D)\ge1$。R137 给
$$
\ell\equiv\pm1\pmod p,\qquad \ell\ge2p-1>p+1.
\tag{2.1}
$$
选包含全部系数的有限 Galois 数域 $L$，固定 $\ell$ 上方嵌入，赋值归一化为 $v(\ell)=1$。

从三行 $f_1,f_2,f_3$ 得到的 minor 为
$$
\Delta=\det\begin{pmatrix}
1&a_2(f_1)&a_3(f_1)\\
1&a_2(f_2)&a_3(f_2)\\
1&a_2(f_3)&a_3(f_3)
\end{pmatrix}.
$$
它是代数整数。每个复嵌入下，三个列范数分别至多
$\sqrt3,\sqrt{24},6$，故 Hadamard 不等式给
$$
|\sigma\Delta|\le36\sqrt2<51.
\tag{2.2}
$$
这里用 Deligne 的 $|a_2|\le2\sqrt2$、$|a_3|\le2\sqrt3$。

由 (1.1) 至少一个 minor 非零。若所有非零 minor 在固定赋值处均有 $v\ge1$，则 Galois 稳定性保证这个非零 $\Delta$ 的每个 Galois 共轭都满足相同条件。等价地，$\Delta/\ell$ 在全部 $\ell$ 上方素理想整；在其余有限素理想也整。因此它是非零代数整数。但 (2.1)、(2.2) 使其所有复共轭绝对值小于一，与其非零整数范数矛盾。

所以可以对每个实际 $\ell$、每个需要的固定嵌入，选择三行使
$$
\boxed{\Delta\ne0,\qquad0\le\delta:=v(\Delta)<1.}
\tag{2.3}
$$
这一步不声称 minor 为单位；允许系数域在 $\ell$ 分歧，因而 $\delta$ 可以是严格介于零与一之间的有理数。

## 3. 同一真实整微分中的 adjugate 消元

R150 的实际尖点展开可对每个 $f\in\mathcal F$ 及两个标准三色差分方向 $j=1,2$ 写成
$$
\Omega_{f,j}
=\left(\sum_{1\le n<p}a_n(f)\kappa^nU_j(n)t^{n-1}
+O(t^{p-1})\right)dt,
\qquad
U_j(n)=\sigma_{an}(u_j-u_0)\quad(1\le n<p).
\tag{3.1}
$$
这里前 $p-1$ 项使用同一个实际尖点、同一个原始 $p$ 次根、同一个实际 $a\in\mathbb F_p^\times$ 及同一个 $\ell$ 进嵌入；$\kappa$ 为共同的 $p$ 次单位根。对 $n\ge p$ 不需要继续使用 $\sigma_n$ 记号，只需 R72 已证明的整系数展开。所有微分均来自同一真实秩零商。后面将固定的 $a$ 吸收入素理想 $\lambda$ 的选择，不独立更换它。

以 (2.3) 选择的三行为矩阵 $M$。利用 $\operatorname{adj}(M)M=\Delta I$，取整系数线性组合，得到三条微分 $\Omega_{i,j}$，其前三级系数准确为
$$
\Omega_{i,j}
=\kappa^i\Delta U_j(i)t^{i-1}dt
 +\sum_{n\ge4}c_{i,j,n}t^{n-1}dt,
\qquad c_{i,j,n}\text{ 整},\quad i=1,2,3.
\tag{3.2}
$$
没有除以 $\Delta$。它在所有相关系数域中的非整可逆性从未被假设。

同一实际点与尖点在秩零商中的差为零，故每条 (3.2) 的形式积分为零。R137 的实际参数满足 $v(t)=m$。对 $n\ge4$、$\ell>4$、$m\ge1$，
$$
nm-v_\ell(n)\ge4m.
\tag{3.3}
$$
确实 $n=4$ 时 $\ell\nmid n$；$n\ge5$ 时 $v_\ell(n)\le n-4$（例如 $\ell^r\ge5^r\ge r+4$ 对 $r\ge1$，而 $r=0$ 更直接）。
所以整个积分尾的赋值至少 $4m$。首项分母 $i\in\{1,2,3\}$ 为 $\ell$ 单位，从而
$$
\delta+v(U_j(i))+im\ge4m.
$$

各 $U_j(i)$ 位于未分歧圆分扩张中，因此其归一化赋值为整数。结合 $\delta<1$，得到
$$
\boxed{
v(U_j(1))\ge3m,\qquad
v(U_j(2))\ge2m,\qquad
v(U_j(3))\ge m,
\quad j=1,2.}
\tag{3.4}
$$
这里是对 $U_j(i)$ 的整数赋值取整，不是把 $\delta<1$ 错写成 $\delta=0$。

## 4. 不同圆分素理想的深度相加

三个颜色和为零，$3$ 为 $\ell$ 单位；又 $B_p$ 的分母因子 $\zeta_p-\zeta_p^{-1}$ 为 $\ell$ 单位。故 (3.4) 等价于
$$
v_{\lambda_1}(J_p)\ge3m,
\quad
v_{\lambda_2}(J_p)\ge2m,
\quad
v_{\lambda_3}(J_p)\ge m,
\tag{4.1}
$$
其中 $\lambda_i$ 是由同一个实际根及 $\sigma_i$ 得到的素理想。

$\ell\equiv\pm1\bmod p$ 使 $\ell$ 在 $\mathbb Q(\zeta_p)^+$ 完全分裂。由于 $p>37$，$1,2,3$ 在 $\mathbb F_p^\times/\{\pm1\}$ 中互异，因此三个 $\lambda_i$ 不同。相加即得
$$v_\ell(N_p)\ge6m.$$
逐个实际分母素数应用，完成 (1.2)。

## 5. 一般的完整初始 jet

同一证明给一个可复用的版本。设 $k<p/2$，最初 $k$ 个系数的行矩阵
$$
(a_1(f),\ldots,a_k(f))_{f\in\mathcal F}
$$
秩为 $k$。令
$$
H_k=k^{k/2}\prod_{n=1}^{k}d(n)\sqrt n,
$$
其中 $d(n)$ 为约数个数。Deligne 与 Hecke 递推给每个复嵌入下
$|a_n(f)|\le d(n)\sqrt n$，故任意 $k\times k$ minor 的 house 至多 $H_k$。

对满足 $\ell>\max(H_k,k+1)$ 的实际分母素数，Galois argument 给 $v(\Delta)<1$；adjugate 消去前 $k$ 项中的其余项，并以积分尾 $n\ge k+1$ 得
$$
v_{\lambda_i}(J_p)\ge(k+1-i)m\quad(1\le i\le k).
$$
由于 $k<p/2$，这些素理想互异，所以
$$
\boxed{v_\ell(N_p)\ge\frac{k(k+1)}2v_\ell(D).}
\tag{5.1}
$$
对所有实际分母都满足该数值条件时，得到整体整除
$D^{k(k+1)/2}\mid N_p$。$k=2$ 恰恢复 R150 的三次整除；$k=3$ 的更紧界 $H_3=36\sqrt2$ 与 $\ell\ge2p-1$ 自动相容。

一般 (5.1) 不对 $\ell\le H_k$ 作声明，也不从有限维谱本身推断最初 $k$ 个系数必满秩。它更不补足非零三次中心值的全局缺口。

## 接口来源

- R69、R72：真实秩零商及饱和整微分，而非仅形式上的 Hecke 特征向量。
- R137：同一实际尖点、参数深度、形式积分为零、共同三色理想与 Parseval 范数界。
- R150：完整 Galois 稳定非零谱与共同圆分根的 Fourier 展开规范。本篇在该规范上自含证明多行 minor 的 small-house 步骤及整 adjugate 消元。
- Deligne (1974), Theorem (8.2)，印刷页 302，已在 R156 精确核准：用于最初系数的复绝对值界。

