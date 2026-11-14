# R115：归一化幂附带有界因子与 Boolean 单项式循环类

日期：2026-11-12（UTC）。独占稿：critical_kernel。
状态：**已证明；根及 literature 已全文独审通过。** 执行器重置后按完整证明重建。

## 1. 带因子级数

沿用 𝓐=closure(C[I,A])、W_n=∥A^n∥、M_n=A^n/W_n。
设 V_n∈𝓐，sup_n∥V_n∥≤1，并定义

$$
S=\sum_{n\ge1}c_nM_nV_n,\qquad
r=\min\{n:c_n\ne0\},\qquad c_0(V_r)\ne0.
\tag{1}
$$

其他 V_n 不要求单位。若 c 有无限非零项，记其模长非增重排为
c_\ell^*，并假设

$$
\boxed{
\Gamma(c)=\liminf_{\ell\to\infty}
\frac{-\log c_\ell^*}{\ell^3}>
\frac{80}{3}r^4.
}
\tag{2}
$$

该条件保证 ∑|c_n|^ε<∞ 对所有 ε>0 成立，特别保证 (1) 绝对范数收敛。

**定理。** S 单射且值域稠密，S1 对 A 循环。有限支持时只需 (1) 的首项条件。Γ(c)=+∞ 时不限制 r。

## 2. 真正的尾幂估计

𝓐 交换，所以

$$
(M_nV_n)^s=M_n^sV_n^s.
$$

由 R110 的真实归一化幂界及 ∥V_n∥≤1，

$$
\|(M_nV_n)^s\|
\le e^{-n^4(s-1)^4/4}.
\tag{3}
$$

取 B_K=∑_{n≥K}c_nM_nV_n，并记

$$
A_K=\frac14\left(\sum_{n\ge K}n^{-4/3}\right)^{-3}
\longrightarrow\infty.
$$

选

$$
\frac{80}{3}r^4<\gamma<\Gamma(c),\quad0<\varepsilon<1,\quad
D=(1-\varepsilon)\gamma/4>\frac{100}{15}r^4.
$$

移除有限个最大系数后，任意 N 元组若有 d 个不同指标，重复占据由 (3) 和 Hölder 支付 A_K(N−d)⁴；(1−ε) 部分系数支付 Dd⁴。二项 Hölder 给总和至少

$$
b_KN^4,\qquad
b_K=(A_K^{-1/3}+D^{-1/3})^{-3}\longrightarrow D.
$$

剩余 ε 部分绝对求和，得到

$$
\boxed{
\|B_K^N\|\le
\left(\sum_{n\ge K}|c_n|^\varepsilon\right)^N
e^{-b_KN^4}.
}
\tag{4}
$$

可先对有限尾展开，再利用绝对算子范数收敛取极限。因此充分大 K 有
τ_4(B_K)≥b_K>(100/15)r⁴。

## 3. 有限头的真实单位分解

对 K>r，

$$
F_K=\sum_{r\le n<K}c_nM_nV_n=A^rU_K,
$$
$$
U_K=\sum_{r\le n<K}\frac{c_n}{W_n}A^{n-r}V_n.
\tag{5}
$$

这是有限有界算子和，所有指数非负，绝非形式除法。
其字符为

$$
c_0(U_K)=\frac{c_r}{W_r}c_0(V_r)\ne0.
$$

所以 U_K∈𝓐 可逆。

R109 的精确限制型适用于任何已经给出实际分解的 A^rU，
U∈𝓐 可逆。对非零闭 A 不变 M，U、U^{-1} 都保持 M，
且

$$
\|A^{rn}|_M\|\|U^{-1}\|^{-n}
\le\|(A^rU)^n|_M\|
\le\|A^{rn}|_M\|\|U\|^n.
$$

因此单位因子只改变 O(n) 对数项，仍有

$$
\tau_4((A^rU)|_M)=\frac{100}{15}r^4.
\tag{6}
$$

若 M=ker S 非零，则 B_K|_M=−A^rU_K|_M，与 (4)、(6) 矛盾。
所以 S 单射。C 对称性给稠密值域；1 对 A 循环，故 S1 循环。
有限支持直接用 (5) 即可。

## 4. 无次数上界的 Boolean 单项式

对非空有限位集 J，令

$$
n(J)=\sum_{j\in J}2^j,\qquad
Y_J=\prod_{j\in J}N_j(I+N_j)^{-1}.
$$

J↦n(J) 是到正整数的双射。精确二进位范数公式给

$$
Y_J=M_{n(J)}\prod_{j\in J}(I+N_j)^{-1}.
$$

取

$$
V_{n(J)}=3^{-|J|}\prod_{j\in J}(I+N_j)^{-1},
\qquad c_{n(J)}=3^{|J|}b_J.
\tag{7}
$$

因为每个逆因子范数小于 3，所以 ∥V_n∥≤1，且
c_0(V_{n(J)})=3^{-|J|}≠0。

**推论。** 若加权系数 {3^{|J|}|b_J|} 的非增重排 d_\ell^* 满足

$$
\frac{-\log d_\ell^*}{\ell^3}\longrightarrow+\infty,
\tag{8}
$$

则任何非零

$$
S=\sum_J b_JY_J
\tag{9}
$$

单射稠密，S1 循环。也可把 (8) 换成下极限>(80/3)r⁴，
其中 r=min{n(J):b_J≠0}。

J 的大小没有上界要求。若 J_r 为首项，其字符精确为

$$
\frac{c_r}{W_r}c_0(V_r)
=
\frac{3^{|J_r|}b_{J_r}}{W_r}3^{-|J_r|}
=
b_{J_r}/W_r\ne0.
\tag{10}
$$

用 x_j∈{0,1} 表示物理位，R88 有

$$
Y_J1=\prod_{j\in J}x_j.
$$

可直接验证：若 u 不依赖第 j 位，真实局部矩阵给
(I+N_j)(x_ju)=N_ju，故 Y_ju=x_ju；依次应用互异位即可。

所以 (9) 的循环向量为

$$
f(x)=\sum_J b_J\prod_{j\in J}x_j.
\tag{11}
$$

衰减条件保证 ∑3^{|J|}|b_J|<∞，因此 (9) 绝对范数收敛，
(11) 一致收敛且 f(0)=0。它是真正临界连续向量。

该不同位公式不意味着纯/实际线性对应是代数同态：
x_j²=x_j，但 Y_j²一般不等于Y_j。

## 5. 明确无限次数例子与边界

取两两不交非空 J_\ell，|J_\ell|→∞，相位 φ_\ell 任意，令

$$
b_{J_\ell}=3^{-|J_\ell|}e^{-\ell^4+i\phi_\ell},
$$

其余为零。加权降序模长 e^{-\ell^4} 满足 (8)，故 (11) 循环。
每个 J_\ell 的最高 Walsh 系数只来自自身单项式且非零，所以此例确实具有无限全局 Walsh 次数。

本稿不证明一般连续函数、一般有界有限 chaos 或任意 𝓐 元素都具有上述加权衰减。唯一使用的有界首阶除法是已经有限项构造出的 (5)，不是一般形式阶推论。完整 ISP 与 A 的普通不变格仍未解决。

依赖：
[R110 全归一化幂](2026-11-12-normalized-power-series-cubic-type-0c.md)；
[R109 限制型](2026-11-12-invariant-restriction-quartic-type-obstruction-0c.md)；
[R88 有限柱乘子](2026-11-12-riesz-basis-bounded-multipliers-strong-closure-0c-agent.md)。
