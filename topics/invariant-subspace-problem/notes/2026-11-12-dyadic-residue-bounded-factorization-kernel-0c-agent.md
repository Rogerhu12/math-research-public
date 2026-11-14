# Dyadic 余数分量的有界因式与首一次代数元素的核排除

日期：2026-11-12
作者：Astra-ISP-0c017065 / l2_moments
状态：R124 已证独占加强稿，供根独审。核的 Fourier 机制由 critical_kernel 首先提出；本稿给出真实余数分量的有界因式及由此新增的适用类。

## 1. 实际 dyadic 圆作用与余数分量

设 $N=2^m$。对 $\zeta^N=1$，定义酉乘法
$$
(U_\zeta f)(y)=\zeta^{\,y\bmod N}f(y).
$$
实际权移满足
$$
U_\zeta A U_\zeta^{-1}=\zeta A.
$$
故
$$
\gamma_\zeta(T)=U_\zeta T U_\zeta^{-1}
$$
在 $\mathcal A=\overline{\mathbb C[I,A]}$ 上为等距自同构。记
$$
\mathcal E_{s,N}(T)
=\frac1N\sum_{\zeta^N=1}\zeta^{-s}\gamma_\zeta(T),
\qquad0\le s<N.
\tag{1.1}
$$
每个 $\mathcal E_{s,N}$ 收缩，并且
$$
T=\sum_{s=0}^{N-1}\mathcal E_{s,N}(T).
$$
对多项式，它保留且仅保留幂指数模 $N$ 等于 $s$ 的项。

## 2. 每个非零余数的真实有界除法

**引理 2.1。** 对每个 $T\in\mathcal A$、$0\le s<N$，存在
$$
B_s\in\overline{\mathbb C[I,A^N]}
$$
使
$$
\boxed{\mathcal E_{s,N}(T)=A^sB_s,\qquad
\|B_s\|\le W_s^{-1}\|\mathcal E_{s,N}(T)\|.}
\tag{2.1}
$$
$s=0$ 时 $W_0=1$，即余数零分量属于 $A^N$ 的范数代数。

**证明。** 对多项式余数分量，写
$$
P_s(A)=A^sQ_s(A^N).
$$
真实归一化幂在低于 $m$ 的位上为恒等，因此
$$
A^N=d_m I_{\mathrm{head}}\otimes\widehat N_m.
\tag{2.2}
$$
这由长 $N$ 权积中只有唯一的 $N$ 倍数权重仍依赖尾变量得到，正是 R117 的精确尾分解。

取归一化物理头向量 $e_i=\sqrt N\,1_{\{\mathrm{head}=i\}}$。对任意尾向量 $v$，
$$
A^s(e_0\otimes v)=W_se_s\otimes v
\qquad(0\le s<N).
$$
由于 $Q_s(A^N)$ 在头上为恒等，故
$$
P_s(A)(e_0\otimes v)
=W_se_s\otimes Q_s(d_m\widehat N_m)v.
$$
所以
$$
\boxed{\|Q_s(A^N)\|\le W_s^{-1}\|P_s(A)\|.}
\tag{2.3}
$$

现在取多项式 $P^{(\nu)}(A)\to T$，并作固定余数投影。其余数分量在范数中趋于 $\mathcal E_{s,N}(T)$；(2.3) 对任意两个近似的差适用，故对应 $Q_s^{(\nu)}(A^N)$ 是范数 Cauchy。极限 $B_s$ 属于闭代数 $\overline{\mathbb C[I,A^N]}$，保持因式及范数界。证毕。

明确说，令 $\mathcal A_N=\overline{\mathbb C[I,A^N]}$，同一压缩论证经范数逼近对每个 $B\in\mathcal A_N$ 给
$$
W_s\|B\|\le\|A^sB\|\le W_s\|B\|.
$$
右边只是 $\|A^s\|=W_s$，所以实际上
$$
\boxed{\|A^sB\|=W_s\|B\|\qquad(B\in\mathcal A_N,\ 0\le s<N).}
\tag{2.5}
$$
因此乘以 $A^s$ 在这个特定尾代数上为缩放等距映射，其像闭；上述逼近证明该像恰为 $\mathcal E_{s,N}(\mathcal A)$。这给出完整的封闭像与有界逆解释。$s=0$ 的等式仅为恒等，不允许把零字符的 $B_0$ 再除一个 $A$。

这是有界除法的特殊情形，不能推广成任意零常数 $\mathcal A$ 元素都可被 $A$ 有界整除：余数零分量内部仍可能不能再除一个 $A$。

普通连续形式系数给
$$
\chi(B_s)=\gamma_s(T),
\tag{2.4}
$$
其中 $\chi$ 是 $\mathcal A$ 的唯一常数特征。

## 3. 首一次系数非零时的全部旋转差

若
$$
\chi(T)=0,\qquad \gamma_1(T)\ne0,
$$
则对任意非平凡 dyadic 根 $\zeta$，设其阶为 $N$，由 §2，
$$
\begin{aligned}
\gamma_\zeta(T)-T
&=\sum_{s=1}^{N-1}(\zeta^s-1)A^sB_s\\
&=A\,C_\zeta,
\end{aligned}
\tag{3.1}
$$
其中
$$
C_\zeta=\sum_{s=1}^{N-1}(\zeta^s-1)A^{s-1}B_s\in\mathcal A.
$$
其特征为
$$
\chi(C_\zeta)=(\zeta-1)\gamma_1(T)\ne0.
$$
所以 $C_\zeta$ 是 $\mathcal A$ 的单位。旋转差不必是标量解析芽，但精确为 $A$ 乘一个实际有界单位。

更一般地，令 $h=2^k$，若
$$
T\in\overline{\mathbb C[I,A^h]},\qquad
\chi(T)=0,\qquad \gamma_h(T)\ne0,
\tag{3.2}
$$
则对每个 dyadic $\zeta$ 满足 $\zeta^h\ne1$，其阶 $N$ 为 $h$ 的倍数且大于 $h$。只有余数 $h,2h,\dots,N-h$ 可以出现，故同样有
$$
\boxed{\gamma_\zeta(T)-T=A^hC_\zeta,\qquad C_\zeta\in\mathcal A^\times.}
\tag{3.3}
$$
单位特征为 $(\zeta^h-1)\gamma_h(T)$。

## 4. 核的 Fourier 有限维机制

为完整给出本稿新增类的结论，记录 critical_kernel 的机制在 (3.3) 下的自含证明。

设 $M=\ker T$ 非零。它闭且 $A$ 不变。对任意闭 $A$ 不变空间 $L$ 及整数 $r\ge1$，
$$
\overline{A^rL}=L.
\tag{4.1}
$$
事实上，$N_jx\in A^rL$ 对所有充分大 $j$ 成立；真实 $N_j$ 与局部 $E_j$ 的范数差趋零，而 $E_j\to I/2$ 于 WOT。因此 $N_jx\rightharpoonup x/2$。闭线性空间 $\overline{A^rL}$ 弱闭，故包含 $x$。

记 $M_\zeta=U_\zeta M=\ker\gamma_\zeta(T)$。$\mathcal A$ 中算子对
$$
B(v,w)=\int v(y)w(-1-y)\,d\mu(y)
$$
均对称。对 $v\in M,w_\zeta\in M_\zeta$，
$$
B((\gamma_\zeta(T)-T)v,w_\zeta)=0.
\tag{4.2}
$$
由 (3.3)，单位 $C_\zeta$ 及其逆都保持 $M$，而 (4.1) 给
$$
\overline{(\gamma_\zeta(T)-T)M}=M.
$$
所以
$$
B(M,U_\zeta M)=0
\qquad(\zeta^h\ne1).
\tag{4.3}
$$

固定 $v,w\in M$。函数 $v(y)w(-1-y)$ 属于 $L^1$。等式 (4.3) 正是它在所有不满足 $\zeta^h=1$ 的 dyadic 字符处 Fourier 系数为零。所有 dyadic 字符组成 $\mathbb Z_2$ 的对偶群，因此 Fourier 唯一性给
$$
v(y)w(-1-y)
\text{ 在每个低 }\log_2h\text{ 位物理柱上为常数。}
\tag{4.4}
$$
也可用有限柱条件期望的 Fourier 展开与 $L^1$ 收敛直接证明此结论。

### 总本质支撑与逐柱一维性

取 $M$ 的可数正交基，令 $\Omega$ 为其非零集合的本质并。该集合包含每个 $M$ 向量的本质支撑，且 $\mu(\Omega)>0$。权重 $w>0$ 几乎处处，$A$ 不变性给
$\Omega+1\subseteq\Omega$ 模零。平移保持 Haar 测度，故该包含实际为模零相等。odometer 的遍历性给 $\mu(\Omega)=1$。

因此每个物理柱上，总能从可数基向量对中选 $v_i,w_i\in M$，使
$v_i(y)w_i(-1-y)$ 在该柱的一个正测集上非零：其支持交的可数并覆盖该柱。由 (4.4)，该乘积在整个柱上为一个非零常数，故 $w_i(-1-y)$ 在柱上几乎处处非零。

对于任意 $u\in M$，$u(y)w_i(-1-y)$ 仍是柱常数。因此 $u$ 在该柱上的限制属于一个固定一维空间，例如由 $v_i$ 的该柱限制张成。共有 $h$ 个柱，故
$$
\dim M\le h.
$$
非零有限维 $A$ 不变空间会产生 $A$ 的特征向量，但 $A$ 拟幂零且单射，没有特征值。矛盾，故 $M=0$。

## 5. 新增结论与范围

由 §§3–4：

**定理 5.1。** 若 $T\in\mathcal A$ 满足 $\chi(T)=0$、$\gamma_1(T)\ne0$，则 $T$ 单射且值域稠密，$T1$ 循环。

**定理 5.2。** 若 $h=2^k$ 且 $T$ 满足 (3.2)，同样单射稠密，$T1$ 循环。

值域稠密来自实际 $C$ 对称性，循环性来自 $1$ 循环与交换关系。非零常数特征的情形本来就是单位，无需上述论证。

这包括全部非零临界有界第一 chaos 乘子：
$$
T=\sum_{j\ge k}a_jN_j(I+N_j)^{-1},
\qquad a\in\ell^1,\ a_k\ne0,
$$
因为它属于 $\overline{\mathbb C[I,A^{2^k}]}$，且在 $A^{2^k}$ 上的一次系数非零。不要求系数快尾、相位或排列条件。

本稿没有覆盖任意首形式阶 $r>1$ 的 $\mathcal A$ 元素：更低非零余数分量的商虽然常数项为零，却未必可再有界除法。也没有证明全部范数闭主理想标准或任意不变子空间不存在。完整 ISP 仍未解决。
