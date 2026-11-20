# R12 附录：Deddens 负幂域保持与等距共轭

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / literature；AI-assisted，GPT-6 Astra Pro。

**状态：以下域保持、负幂上界、共轭及真实原像递推均已证明。** 正幂的最优 Deddens 常数同时是全部负幂的一个统一上界；本文不未经证明把“只检查负幂”所定义的另一个最优常数与它等同。所有逆幂均在实际稠密定义域上使用，不宣称 $A^{-1}$ 是 $H$ 上的有界算子。

内部依赖是 [R12](R12-normalized-powers-and-compact-commutant.md) 的实际归一化幂与高位模型，及 [Deddens 完整边界](R12-appendix-deddens-algebra-localizing-and-uniform-cost-obstruction.md) 的定义。原权对象见 [R9](R9-radial-odometer-and-nilpotent-approximants.md)。除所列 R12 极限外，证明重写于下。

## 1. 原算子与所用极限

在 $H=L^2(\mathbb Z_2,\mu)$ 上，

$$
A=M_wU,\qquad Uf(y)=f(y-1),\qquad
w(0)=0,\quad w(y)=\alpha_{v_2(y)}>0\ (y\ne0),
$$

$$
\alpha_j=\exp\left(
-\frac{280}{3}16^j+90\,8^j-300\,2^j+\frac{850}{3}
\right).
\tag{1.1}
$$

$A$ 单射、值域稠密，且 $\|A\|=\alpha_0=e^{-20}<1$。记

$$
N_j=2^j,\qquad \beta_n=\|A^n\|,\qquad
F_j=A^{N_j}/\beta_{N_j}.
\tag{1.2}
$$

R12 给出作用于第 $j$ 位的 $E_j=e_{10}$，满足

$$
\|F_j-E_j\|\to0,\qquad
E_j\to\tfrac12 I\ {\rm WOT},\qquad
E_j^*E_j=P_j^0\to\tfrac12 I\ {\rm WOT}.
\tag{1.3}
$$

由于 $\|F_j\|=\|E_j\|=1$，(1.3) 也给

$$
F_j\to\tfrac12 I\ {\rm WOT},\qquad
F_j^*F_j\to\tfrac12 I\ {\rm WOT}.
\tag{1.4}
$$

第二个极限来自
$\|F_j^*F_j-E_j^*E_j\|\le2\|F_j-E_j\|$。特别，对每个固定 $u\in H$，

$$
\boxed{\|F_ju\|^2\longrightarrow\tfrac12\|u\|^2.}
\tag{1.5}
$$

定义

$$
\mathcal D_A=
\{X\in B(H):\exists C<\infty,\
\|A^nXf\|\le C\|A^nf\|\quad(n\ge1,\ f\in H)\},
$$

$$
c_A(X)=\inf\{C:\text{这些全部不等式成立}\}.
\tag{1.6}
$$

## 2. 正幂成本支配普通范数

若 $C$ 是 $X$ 的一个合法 Deddens 常数，取 $n=N_j$ 并除以 $\beta_{N_j}$，

$$
\|F_jXf\|\le C\|F_jf\|.
$$

对平方范数用 (1.5)，得到

$$
\tfrac12\|Xf\|^2\le\tfrac12 C^2\|f\|^2.
$$

故

$$
\boxed{\|X\|\le c_A(X).}
\tag{2.1}
$$

合法常数向其下确界递减时，不等式对每个固定 $n,f$ 保持，所以最优常数本身合法。以下可直接取 $C=c_A(X)$；也可始终用任意合法 $C$，最后取下确界。

## 3. 全部负幂的实际域保持

因 $A$ 单射，$A^{-k}$ 在 $\operatorname{Ran}A^k$ 上有唯一含义。它是闭算子；定义域稠密，但不等于声明其有界。

**定理 3.1。** 对任意 $X\in\mathcal D_A$ 和整数 $k\ge1$，

$$
\boxed{X(\operatorname{Ran}A^k)\subseteq\operatorname{Ran}A^k,}
\tag{3.1}
$$

并且

$$
\boxed{
\|A^{-k}Xf\|
\le c_A(X)\|A^{-k}f\|
\qquad(f\in\operatorname{Ran}A^k).}
\tag{3.2}
$$

**证明。** 固定 $f=A^ku$。只取 $N_j>k$，令

$$
g_j=\frac{A^{N_j-k}Xf}{\beta_{N_j}}.
\tag{3.3}
$$

正幂 Deddens 不等式给

$$
\|g_j\|\le c_A(X)
\frac{\|A^{N_j-k}f\|}{\beta_{N_j}}
=c_A(X)\|F_ju\|.
\tag{3.4}
$$

所以 $\{g_j\}$ 有界，在 Hilbert 空间中存在弱收敛子列，设其弱极限为 $v$。另一方面，

$$
A^kg_j=F_jXf\longrightarrow\tfrac12 Xf
\quad{\rm weakly}.
$$

有界算子 $A^k$ 弱连续，故 $A^kv=Xf/2$。这首先证明 $Xf\in\operatorname{Ran}A^k$，而非预先把 $A^{-k}Xf$ 当成已定义。

现在记 $v_0=A^{-k}Xf$。由单射性，(3.3) 对整个序列变成

$$
g_j=F_jv_0.
$$

将此式代回 (3.4)，对两边平方范数用 (1.5)，得到
$\|v_0\|^2/2\le c_A(X)^2\|u\|^2/2$，即 (3.2)。证毕。

该证明的第一步只使用有界弱聚点来支付域；支付域以后才使用准确的范数极限，因此没有丢失一个额外因子 $2$。

**常数范围。** 定理说的是正幂最优常数 $c_A(X)$ 控制全部负幂。若把正幂、普通范数和负幂全部放在一起定义联合最优常数，则因为包含原正幂条件，联合最优常数确实等于 $c_A(X)$。本文不从这个事实推出“仅负幂条件”的独立最优常数也相等。

## 4. 各实际算子值域上的 Hilbert 作用

给 $\operatorname{Ran}A^k$ 赋予范数

$$
\|f\|_{-k}=\|A^{-k}f\|.
\tag{4.1}
$$

映射 $u\mapsto A^ku$ 是 $H$ 到这一空间的满等距同构，所以它是 Hilbert 空间。到原 $H$ 的包含连续，范数至多 $\beta_k$，但其像在原范数中一般不闭。

定理 3.1 表示同一个 $X\in\mathcal D_A$ 在全部这些真实 Hilbert 空间上有界，且范数均不超过 $c_A(X)$。原像不是另行优化的替代向量：由于 $A$ 单射，它是唯一的 $A^{-k}f$。

特别，任意 $R_i\in\mathcal D_A$ 的递推

$$
f_i=R_iAf_{i-1}
\tag{4.2}
$$

满足

$$
f_n\in\operatorname{Ran}A^n.
\tag{4.3}
$$

这是归纳结论：$f_{n-1}\in\operatorname{Ran}A^{n-1}$ 使
$Af_{n-1}\in\operatorname{Ran}A^n$，再用域保持。它对非复制来源重排也成立。

## 5. 正负共轭都是有界的，且保持同一个成本

对 $X\in\mathcal D_A$，先在 $\operatorname{Ran}A$ 上定义

$$
\Phi(X)(Af)=AXf.
\tag{5.1}
$$

由正幂 $n=1$ 的不等式，它延为 $H$ 上的有界算子，范数不超过 $c_A(X)$。

由定理 3.1，另一个算子

$$
\Psi(X)=A^{-1}XA
\tag{5.2}
$$

已在整个 $H$ 上有定义，且范数不超过 $c_A(X)$。

证明它们仍在 $\mathcal D_A$。对于 $\Phi(X)$，先在稠密集合 $f=Ag$ 上计算：

$$
\|A^n\Phi(X)f\|
=\|A^{n+1}Xg\|
\le c_A(X)\|A^{n+1}g\|
=c_A(X)\|A^nf\|.
$$

由连续性扩展至所有 $f$，所以 $c_A(\Phi(X))\le c_A(X)$。

对于 $\Psi(X)$，当 $n\ge2$ 时，

$$
\|A^n\Psi(X)f\|
=\|A^{n-1}XAf\|
\le c_A(X)\|A^nf\|.
$$

当 $n=1$ 时，使用 (2.1)：

$$
\|A\Psi(X)f\|=\|XAf\|
\le\|X\|\|Af\|\le c_A(X)\|Af\|.
$$

故 $c_A(\Psi(X))\le c_A(X)$。

由 (5.1)–(5.2)，利用 $\operatorname{Ran}A$ 的稠密性和 $A$ 的单射性可得

$$
\Phi\Psi(X)=X,\qquad \Psi\Phi(X)=X.
$$

乘法恒等式也先在 $\operatorname{Ran}A$ 上成立，再由稠密性扩展。因此 $\Phi,\Psi$ 是互逆代数自同构，并且双向成本不等式给

$$
\boxed{c_A(\Phi(X))=c_A(\Psi(X))=c_A(X).}
\tag{5.3}
$$

记 $\Phi^{-1}=\Psi$。对全部 $n\in\mathbb Z$，

$$
\boxed{\|\Phi^n(X)\|\le c_A(X),\qquad
c_A(\Phi^n(X))=c_A(X).}
\tag{5.4}
$$

对正 $n$，$\Phi^n(X)$ 是 $A^nXA^{-n}$ 从实际稠密定义域的有界延拓；对负 $n=-k$，它是已支付域的 $A^{-k}XA^k$。这个记号不把裸 $A^{-k}$ 单独延为有界算子。

$\Phi(X)=X$ 当且仅当 $AX=XA$。交换子本身满足
$c_A(X)=\|X\|$，因为正幂可以交换，再结合 (2.1)。

应用于 (4.2)，令 $u_n=A^{-n}f_n$，可得保持同一原像的准确递推

$$
\boxed{
u_n=\Phi^{-n}(R_n)u_{n-1},\qquad
\|u_n\|\le c_A(R_n)\|u_{n-1}\|.}
\tag{5.5}
$$

因此 $u_n$ 是实际来源序列，不是仅由某个存在性定理另选的最小源。

## 6. 任意真实不变子空间都有稠密的无限可回溯核心

本节说明仅以值域或其交集取闭包，不会自动产生一个新的非零真闭不变量。

先设 $M$ 是 $A$-不变闭子空间。对 $f\in M$，每个 $F_jf$ 都在 $AM$ 中，而 $F_jf\to f/2$ 弱收敛。闭线性子空间弱闭，故

$$
\overline{AM}=M.
\tag{6.1}
$$

以下直接构造任意长后继原像的相容极限。给定 $v\in M$ 和 $\varepsilon>0$，令 $u_0=v$。由 (6.1)，逐次选 $u_{n+1}\in M$，使

$$
\|Au_{n+1}-u_n\|<\varepsilon2^{-n-1}.
\tag{6.2}
$$

对 $0\le k\le n$ 定义 $x_{k,n}=A^{n-k}u_n$。因为 $\|A\|<1$，

$$
\|x_{k,n+1}-x_{k,n}\|
\le\varepsilon2^{-n-1}.
$$

所以对固定 $k$，$x_{k,n}$ 在闭空间 $M$ 中收敛为 $x_k$。有
$Ax_{k+1}=x_k$，且 $\|x_0-v\|<\varepsilon$。因此
$x_0=A^kx_k\in A^kM$ 对全部 $k$ 成立，证明

$$
\boxed{\overline{\bigcap_{k\ge0}A^kM}=M.}
\tag{6.3}
$$

由于 $A$ 单射，这些后继原像唯一，正是 $A^{-k}x_0$。本构造不对 $\|x_k\|$ 给任何统一或增长预算；不能把存在全部原像误认为已支付原像费用。

取 $M=H$，得到

$$
\mathcal H_\infty:=\bigcap_{k\ge0}\operatorname{Ran}A^k
$$

稠密。由定理 3.1，它被整个 $\mathcal D_A$ 保持，但在原 Hilbert 范数下取闭包得到 $H$。因此其保持性与 $\mathcal D_A$ 单位球强稠密并不矛盾，也不单独给普通不变子空间。

## 7. 对非复制来源的可用接口与剩余门

负幂域保持可直接作用于任意真实 $R_n\in\mathcal D_A$，不依赖硬 cut、软 copy 或逐点正性。对有限头下三角 $R_n$，其最优正幂成本可用 [有限头成本附录](R12-appendix-contractive-deddens-core-and-exact-finite-head-cost.md) 的至多 $2N$ 个端点矩阵精确计算；同一个数同时上界 (5.5) 的负幂共轭作用。

这为非复制来源重排提供一个保持同一原像的预算接口。不过，(6.3) 只支付后继原像的存在与稠密性，未支付其增长率。全 $\mathcal D_A$ 的强稠密性也没有把它变成未知 $A$-不变子空间的保持代数。要完成普通问题，仍须对同一来源序列得到可用的实际费用上界或构造真正的非零真闭不变量；本文没有跨过这一门。
