# R116：快尾第一阶乘子的标准闭主理想

日期：2026-11-12（UTC）。独占稿：critical_kernel。
状态：**已证明；根与 l2_moments 已全文独立核验通过。** 本文件于执行器重置后由完整证明上下文重建；结论及常数保持不变。

## 1. 主定理与准确范围

令 𝓐=closure(C[I,A])，沿用实际归一化幂
N_j=A^{2^j}/d_j、Y_j=N_j(I+N_j)^{-1}。设

$$
S=\sum_{j\ge0}a_jY_j,\qquad a\in\ell^1,\quad a\ne0,
$$
$$
k_0=\min\{j:a_j\ne0\},\qquad h=2^{k_0}.
$$

记 I_S=closure(S𝓐)、I_h=closure(A^h𝓐)，闭包均取算子范数。

若无限个 a_j 非零，令 a_\ell^* 为其模长非增重排，并记

$$
\Gamma(a)=\liminf_{\ell\to\infty}
\frac{-\log a_\ell^*}{\ell^3}.
$$

**定理。** 若 a 有限支持，或

$$
\boxed{\Gamma(a)>400h^4,}
\tag{1}
$$

则

$$
\boxed{I_S=I_h.}
\tag{2}
$$

特别包括 Γ(a)=+∞ 的全部 R106 超三次重排尾，以及 R103 的
a_j≤Ce^{-c8^j} 类。条件 (1) 本身保证 a∈ℓ¹；在定义级数时先列 ℓ¹ 只为固定范数收敛。

400h⁴ 是本稿 Banach 商代数逆芽论证的充分阈值。R111 在更弱条件
Γ(a)>(80/3)h⁴ 下证明 Hilbert 空间单射，依赖实际不变限制的四次型；不能把那一结论自动搬到任意 Banach 商代数。

## 2. 标准理想与有限形式系数

R32 给连续线性形式系数 λ_n:𝓐→C，满足 λ_n(A^m)=1_{n=m}。于是

$$
I_h=\bigcap_{n<h}\ker\lambda_n.
\tag{3}
$$

包含 I_h⊂右端来自连续性。反之，若 X 的前 h 个系数均为零，取多项式 P_\nu(A)→X，减去

$$
\sum_{n<h}\lambda_n(P_\nu(A))A^n.
$$

该有限和趋零，余下多项式均被 A^h 整除且仍趋 X，故 X∈I_h。此处不要求在未知理想内部进行 Fejér 平均。特别地 dim(𝓐/I_h)=h。

对本题的 S，反向包含还可直接用实际有限项：

$$
Y_j=A^h
\left[\frac{A^{2^j-h}}{d_j}(I+N_j)^{-1}\right]
\in A^h\mathcal A
\qquad(j\ge k_0).
\tag{4}
$$

括号是真正的有界 𝓐 元素，但其范数可随 j 很大。因为
∥Y_j∥<3、a∈ℓ¹，S 是这些有限和的范数极限。因此

$$
S\in I_h,\qquad I_S\subseteq I_h.
\tag{5}
$$

没有声称 (4) 中商的无穷和收敛。

## 3. 有限前缀的一次解析坐标

对 k>k_0，写

$$
S=G_k(A^h)+B_k,\qquad
B_k=\sum_{j\ge k}a_jY_j,
$$
$$
G_k(z)=\sum_{k_0\le j<k}
\frac{a_jz^{m_j}}{d_j+z^{m_j}},
\qquad m_j=2^{j-k_0}.
\tag{6}
$$

每个 G_k 是零点邻域真正解析的标量函数，且

$$
G_k(0)=0,\qquad
G_k'(0)=g_1=a_{k_0}/d_{k_0}\ne0,
\tag{7}
$$

不依赖 k。

精确权满足

$$
\Lambda_j=-\log d_j
=100\,16^j-105\,8^j+(150j+25)2^j
\le100\,16^j.
\tag{8}
$$

最后一个不等式等价于 150j+25≤105·4^j。j=0 成立，两边差的相邻增量为 315·4^j−150>0。

若 G_k(z)=∑g_{n,k}z^n，只有 m_j|n 的项贡献。因此

$$
|g_{n,k}|\le\|a\|_1e^{100h^4n^4}
\qquad(k>k_0,\ n\ge1).
\tag{9}
$$

因为 (n/m_j)Λ_j≤100h⁴n m_j³≤100h⁴n⁴。

## 4. 逆芽系数的统一四次型

由 (7)，每个 G_k 有局部解析逆芽

$$
\psi_k(w)=\sum_{n\ge1}\beta_{n,k}w^n.
$$

**引理。** 存在 C<∞，独立 k,n，使

$$
\boxed{|\beta_{n,k}|\le C^n e^{100h^4n^4}.}
\tag{10}
$$

证明：写 G_k=g_1z(1+U_k)，则由 (9)，

$$
|[z^\ell]U_k|
\le\frac{\|a\|_1}{|g_1|}
e^{100h^4(\ell+1)^4}.
$$

Lagrange 反演为

$$
\beta_{n,k}
=\frac{g_1^{-n}}n[z^{n-1}](1+U_k)^{-n}.
\tag{11}
$$

相关每项来自正整数组成 ℓ_1+⋯+ℓ_s=n−1，满足

$$
\sum_{i=1}^s(\ell_i+1)^4\le n^4.
\tag{12}
$$

逐次合并即可证明 (12)：对 x,y≥2，
x⁴+y⁴≤(x+y−1)⁴，差函数在两个变量上递增且在 x=y=2 为正。
组成数、负二项式系数、(∥a∥₁/|g_1|)^s 及 |g_1|^{-n}
合计被固定 C^n 控制，故得 (10)。n=1 通过增大 C 处理。

每个 ψ_k 单独是解析芽，但其半径允许随 k 趋零。(10) 仅是跨 k 的系数估计，不声称一般四次型形式级数有正解析半径。

## 5. 与真实尾幂匹配

由 R111 的优化占据估计，条件 (1) 允许选

$$
400h^4<c<\Gamma(a),\qquad 0<\varepsilon<1,
$$
$$
D=(1-\varepsilon)c/4>100h^4.
$$

令

$$
\sigma_k=3\sum_{j\ge k}|a_j|^\varepsilon\longrightarrow0,
$$
$$
A_k=\frac{(1-16^{-1/3})^3}{4}\,16^k,\qquad
b_k=(A_k^{-1/3}+D^{-1/3})^{-3}\longrightarrow D.
$$

对充分大 k 和全部 n≥1，

$$
\boxed{\|B_k^n\|\le\sigma_k^n e^{-b_kn^4}.}
\tag{13}
$$

这里不是纯平方零模型的估计。实际局部幂满足
∥N_j^s∥≤exp[−16^j(s−1)^4/4]。对一次 n 元组，若 d 为不同指标数，重复占据付 A_k(n−d)⁴，(1−ε) 部分系数付 Dd⁴；Hölder 给二者之和≥b_kn⁴，剩下 ε 系数绝对求和给 σ_k^n。这就是 (13) 的完整接口。

于是存在固定 δ>0，使充分大 k 有

$$
\|B_k^n\|\le
\sigma_k^n e^{-(100h^4+\delta)n^4}.
\tag{14}
$$

若 Γ(a)=+∞，也可直接用 R106 的 b_k→∞ 界。

## 6. Banach 商代数中的真实解析演算

令

$$
\mathcal Q=\mathcal A/I_S,\qquad
\pi:\mathcal A\to\mathcal Q.
$$

π 为收缩同态。I_S 包含在常数特征核中，故商保有单位。设

$$
T=\pi(A^h),\qquad D_k=\pi(B_k).
$$

A^h 与 B_k 在 𝓐 中均拟幂零，因此 T、D_k 在商中亦拟幂零。由 (6) 和 π(S)=0，

$$
G_k(T)=-D_k.
\tag{15}
$$

在任意 Banach 代数中，零点邻域解析芽都可在拟幂零元上按 Taylor 级数求值：系数至多指数增长，元的幂范数根趋零，故级数绝对范数收敛；通常的解析复合恒等式成立。因此

$$
\boxed{T=\psi_k(-D_k).}
\tag{16}
$$

不要求 ∥D_k∥ 小于 ψ_k 的标量半径，也不依赖任何 Hilbert 表示或核。

由 (10)、(14) 和 π 收缩，

$$
\|T\|
\le\sum_{n\ge1}|\beta_{n,k}|\|D_k^n\|
\le\sum_{n\ge1}(C\sigma_k)^n e^{-\delta n^4}
\longrightarrow0.
\tag{17}
$$

T 不随 k 改变，故 T=0，即 A^h∈I_S。于是 I_h⊂I_S；结合 (5) 得 (2)。

有限支持时，有限有理函数直接给 S=A^hU、U∈𝓐 可逆，同样得到 (2)。

## 7. 闭理想、幂与有限乘积的后果

若闭理想 J 含 S，则 J 含 A^h 及 I_h，因此余维至多为 h。

对每个正整数 q，

$$
\overline{S^q\mathcal A}=I_{hq}.
\tag{18}
$$

取 SQ_\nu→A^h，则 S^qQ_\nu^q→A^{hq}，得到一个方向。
反方向由 S∈I_h，先在 A^h𝓐 中逼近 S，再作 q 次幂。
对有限个本定理的 S_i 及正整数 q_i，同理有

$$
\overline{\left(\prod_iS_i^{q_i}\right)\mathcal A}
=I_{\sum_iq_ih_i}.
\tag{19}
$$

R95 中某些这里的 S 不能由 A 有界整除，不与本稿冲突：
(2) 只给 SQ_\nu→A^h，未声称 Q_\nu 一致有界，更未声称存在精确有界商 SQ=A^h。

本稿不证明一般非零 𝓐 元素的闭主理想标准。也不把 R111 较低的 Hilbert 核阈值自动扩大为商代数结论。实际普通不变格与完整 Hilbert ISP 仍未解决。

内部依赖：
R32 形式系数连续与单点谱；
[R103 逆芽原稿](../notes/2026-11-12-first-chaos-quartic-tail-inverse-germ-0c-agent.md)；
[R106 超三次尾](../notes/2026-11-12-first-chaos-supercubic-rearranged-tail-0c-agent.md)；
[R111 有限三次型](../notes/2026-11-12-first-chaos-finite-cubic-type-0c-agent.md)。
