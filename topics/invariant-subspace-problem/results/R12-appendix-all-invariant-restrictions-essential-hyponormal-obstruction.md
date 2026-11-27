# R12 附录：全部普通不变限制的本质次正规障碍及任意有界相似后的双号本质自交换子

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

**状态。** 本文给出完整的算子论推论。新结论同时保任意未知普通不变限制、任意有界相似与全部非恒定解析函数；不假设这些未知空间由物理柱投影给出。普通 Hilbert ISP 与本题候选的普通不变格仍未解决。

## 1. 实际输入与本次新增范围

沿用原 Haar 算子 $A$。已有结果给出：$A$ 单射、拟幂零，且属于原 UHF 代数。
[R164](R164-invariant-projections-high-bit-essential-rigidity.md) 已证明
$$
\mathfrak E=\{B\in B(H):[B,J_j]\longrightarrow0\text{ 强*}\}
$$
是含单位的 $C^*$ 代数，包含 $A$ 和全部 $P_M$，其中 $M\in\operatorname{Lat}A$ 是任意闭普通不变空间。它在 Calkin 代数中忠实；对任意非零投影 $P\in\mathfrak E$，
$$
P\mathfrak E P\longrightarrow
\mathcal Q(PH)=B(PH)/\mathcal K(PH)
\tag{1.1}
$$
仍为忠实含单位的 $*$ 同态，故保持范数、谱与正性。特别非零 $P$ 的像空间无限维。

R164 已给出特定慢平方共振限制的不本质正规性。
[R107](R107-centered-order-and-compactness-obstructions.md) 已排除全 Haar 算子幂的指定谱次序判据。
本文不重计这些结论。新增的是：任意非零普通限制及其非恒定解析函数，经过任意有界相似后，仍不能在紧扰动意义下成为 hyponormal 或 cohyponormal；自交换子的两种符号都在本质谱中出现。这还适用于下述所有非零拟幂零投影角及实际非零不变子商算子。

以下称 $S$ 为 hyponormal，当 $S^*S-SS^*\ge0$；cohyponormal 指 $S^*$ 为 hyponormal。“本质 hyponormal”仅指此不等式在 Calkin 代数中成立，比预先写成 hyponormal 加紧算子更弱。

## 2. 自含的拟幂零正序引理

**引理 2.1。** 含单位 $C^*$ 代数中的 hyponormal 元若拟幂零，则为零；cohyponormal 情形同样成立。

**证明。** 先在 Hilbert 空间证明。若 $S^*S\ge SS^*$，则 $\|S^*x\|\le\|Sx\|$，从而
$$
\|Sx\|^2
=\langle S^*Sx,x\rangle
\le\|S^*Sx\|\,\|x\|
\le\|S^2x\|\,\|x\|.
\tag{2.1}
$$
对单位向量 $x$ 记 $a_n=\|S^nx\|$。把 (2.1) 用于 $S^{n-1}x$ 得
$$
a_n^2\le a_{n-1}a_{n+1}.
$$
若 $a_1>0$，该式先迫所有 $a_n>0$，然后使相邻比值递增，故 $a_n\ge a_1^n$。于是
$$
r(S)=\lim_n\|S^n\|^{1/n}\ge\|Sx\|.
$$
对单位 $x$ 取上确界，得到 $r(S)=\|S\|$。$a_1=0$ 的向量不影响此上确界。因此 $r(S)=0$ 迫 $S=0$。

对一般含单位 $C^*$ 代数取忠实含单位 Hilbert 表示。该表示保持正性、范数与谱，上述证明原样适用。cohyponormal 情形用于 $S^*$，其谱是原谱的复共轭。证毕。

所以一个非零拟幂零 $C^*$ 元的自交换子既非正也非负。这里不需要迹、有限维性或紧性。

## 3. 忠实投影角上的全相似结论

**定理 3.1。** 设 $0\ne P\in\mathfrak E$，$B\in P\mathfrak E P$ 在 $PH$ 上非零且拟幂零。取任意可逆 $L\in B(PH)$、任意 $\lambda\in\mathbb C$ 及任意紧算子 $K$，令
$$
T=\lambda I_{PH}+L^{-1}BL+K.
$$
则
$$
\boxed{
\sigma_{\rm ess}(T^*T-TT^*)\cap(0,\infty)\ne\varnothing,
\qquad
\sigma_{\rm ess}(T^*T-TT^*)\cap(-\infty,0)\ne\varnothing.
}
\tag{3.1}
$$
特别 $T$ 既非本质 hyponormal，也非本质 cohyponormal。

**证明。** 令 $q:B(PH)\to\mathcal Q(PH)$ 为商映射。
(1.1) 的忠实性和谱保持性给
$$
q(B)\ne0,\qquad \sigma(q(B))=\{0\}.
$$
$q(L)$ 可逆，所以
$$
b=q(L)^{-1}q(B)q(L)\ne0,\qquad \sigma(b)=\{0\}.
$$
没有要求 $L$ 属于 $\mathfrak E$；只使用其在完整 $B(PH)$ 中的实际可逆性。标量移位不改变自交换子，而 $q(K)=0$，故
$$
q(T^*T-TT^*)=b^*b-bb^*.
\tag{3.2}
$$
若 (3.2) 为正或为负，引理 2.1 分别应用于 $b$ 或 $b^*$ 将迫 $b=0$，矛盾。自伴元的谱全为实数；既非正也非负，恰意味着谱同时与两个开半轴相交。Calkin 谱即这里的 Fredholm 本质谱，得到 (3.1)。证毕。

由 (3.1)，可选依赖于 $B,L$ 的 $\varepsilon_+,\varepsilon_->0$，使实际自交换子的正谱投影
$\mathbf1_{[\varepsilon_+,\infty)}(T^*T-TT^*)$
和负谱投影
$\mathbf1_{(-\infty,-\varepsilon_-]}(T^*T-TT^*)$
都具有无限维像。这是本质谱结论的直接后果；不宣称存在对任意 $L$ 一致的数值下界。

若某个 $T$ 可写成 $S+C$，其中 $C$ 紧且 $S$ hyponormal，则 $q(T)$ hyponormal；cohyponormal 同理。因此定理也排除了这样的全部紧扰动分解。

## 4. 每个未知普通不变限制及全部非恒定解析函数

**推论 4.1。** 设 $0\ne M\in\operatorname{Lat}A$，令 $A_M=A|_M$。
设 $f$ 是 $0$ 的某个邻域上的全纯函数，且其在 $0$ 的函数芽不是常数。则
$$
B_f=f(A_M)-f(0)I_M
$$
非零、单射、拟幂零，并属于 R164 的实际角 $P_M\mathfrak E P_M$。故定理 3.1 对 $B_f$ 成立。

**证明。** $A$ 保持 $M$，所以
$$
A_M^n=A^n|_M,\qquad
\|A_M^n\|\le\|A^n\|.
$$
因此 $A_M$ 拟幂零；$A$ 单射使 $A_M$ 单射且非零。$P_MAP_M$ 是其零延拓，属于实际角；不需要 $M^\perp$ 在 $A$ 下不变。

将非恒定函数芽分解为
$$
f(z)-f(0)=z^m g(z),\qquad m\ge1,\quad g(0)\ne0.
$$
拟幂零性使所有这些局部全纯函数均能在 $A_M$ 上进行全纯演算。具体地，任意正的收敛半径内，$\|A_M^n\|^{1/n}\to0$ 保证其 Taylor 级数按范数收敛。角代数闭且含其单位，故
$$
B_f=A_M^m g(A_M)\in P_M\mathfrak E P_M.
$$
谱映射给 $g(A_M)$ 可逆，故 $B_f$ 单射而非零；再次谱映射给 $\sigma(B_f)=\{0\}$。证毕。

由此，对每个 $L\in GL(M)$ 与每个紧 $K$，
$$
\big(L^{-1}f(A_M)L+K\big)^*
 \big(L^{-1}f(A_M)L+K\big)
-
\big(L^{-1}f(A_M)L+K\big)
 \big(L^{-1}f(A_M)L+K\big)^*
$$
在本质谱中同时具有正、负值。特别包括全部正整数幂，以及所有在原零谱附近非恒定的解析单位化。这里真正处理每个未知 $M$，没有把全空间的点态权公式移入未知限制。

次正规算子一定 hyponormal。为明确使用的方向：若正规 $N$ 在更大 Hilbert 空间上保持原空间，写作
$$
N=\begin{pmatrix}S&C\\0&D\end{pmatrix},
$$
正规等式的左上角给 $S^*S-SS^*=CC^*\ge0$。
所以以上全部算子都不能经有界相似写成“次正规算子加紧算子”，更不能写成“次正规算子加迹类算子”。

## 5. 实际子商和慢平方共振

若 $N\subset M$ 均为闭 $A$ 不变空间，置 $P=P_M-P_N$、$K=M\ominus N$，实际诱导算子为
$$
A_{M/N}=PA|_K.
$$
R164 §4.5 已证明
$$
A_{M/N}^n=PA^n|_K.
$$
故它拟幂零并属于 $P\mathfrak E P$。**只要它非零**，定理 3.1 即适用。
这里不假定其单射；若该诱导算子为零，本定理的非零前提不满足，不能据此排除该子商。

另在 R164 §7 的实际慢平方共振设置中，
$M=\ker(X-Y)\ne0$、$\chi(Y)=a$。旧证明已付
$Y_M-aI_M$ 拟幂零且非零：否则 $M\subset\ker(X-aI)=0$。
又 $Y_M-aI_M\in P_M\mathfrak E P_M$。
因此定理 3.1 将旧“不本质正规”提高到任意有界相似后的两个本质符号都存在，且排除 hyponormal 或 cohyponormal 紧扰动。
这仍是未知非零核的必要条件，不从该条件直接判核为零。

## 6. 新预印本的具体适用性及剩余方向

本次实际读取 [Guo–Jiang–Wang–Zhu, arXiv:2611.28933v1](https://arxiv.org/abs/2611.28933v1)，提交日期为 2026-11-21；
其[原文 Theorem 1.2](https://arxiv.org/html/2611.28933v1)声称：复可分无限维 Hilbert 空间上，次正规算子加迹类算子具有非平凡闭不变子空间。
这里仅记录已读取的定理范围，不把本次读取当作对整篇预印本证明的独立认证。

本文自身证明不依赖该预印本结论。即使采用其 Theorem 1.2，当前原 $A$、所有非零普通 $A$ 不变限制，以及其全部非恒定解析函数，经任何有界相似都无法满足其“次正规加迹类”输入。障碍已经发生在更弱的“本质 hyponormal”层，故更换紧算子、迹类分解或有界度量不能解除。

此结论不排除经真正不同的扩大空间、非可逆交织、闭无界域或其它算子结构获得新来源。它也不证明 $A$ 没有普通不变子空间，不支付未知 $W$ 的真实来源费用。继续这些未被排除的原接口，而不重试上述已排除的有界相似紧扰动输入。
