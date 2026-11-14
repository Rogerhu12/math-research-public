# R106 草稿：真实进位与不同占据数——超三次对数衰减的全空间循环性

日期：2026-11-12（UTC）。独占稿：critical_kernel。
状态：**已证明。** 本稿将 R103 的 e^{-c8^j} 尾大幅扩充到原索引或降序系数的超三次对数衰减。全部复相位、有限前缀和允许条件下的稀疏排列均任意。结论直接排除原 Haar Hilbert 空间上的核，不是有限 chaos 配对结论。

## 1. 主定理及更一般的尾乘积条件

沿用实际径向 odometer A、归一化幂

$$
N_j=\frac{A^{2^j}}{d_j},\qquad d_j=\|A^{2^j}\|,
\qquad
Y_j=N_j(I+N_j)^{-1}.
\tag{1.1}
$$

设

$$
f=a_*+\sum_{j\ge0}a_j\chi_j
\tag{1.2}
$$

非零。以下两种条件中的任一种足够：

1. **按原索引的超三次对数衰减：**

$$
\boxed{
\frac{-\log |a_j|}{(j+1)^3}\longrightarrow+\infty.
}
\tag{1.3}
$$

零系数的负对数约定为 +∞。

2. **按大小降序后的超三次对数衰减：** 若非零系数有无限项，令 a_r^* 是 {|a_j|} 的非增重排，则

$$
\boxed{
\frac{-\log a_r^*}{r^3}\longrightarrow+\infty.
}
\tag{1.4}
$$

有限支持另按有限柱结论处理。

**定理 1.1。** 满足 (1.3) 或 (1.4) 的每个非零 f 都对实际 A 循环。

两个条件都保证

$$
\sum_j\sqrt{|a_j|}<\infty,
\tag{1.5}
$$

因此也保证 a∈ℓ¹ 及 f 连续。相位不进入任何假设。

更一般地，设 a∈ℓ¹ 且满足 (1.5)。对充分大 k，所有 |a_j|（j≥k）均小于 1。将该尾的模长非增排列为 a_r^{*(k)}，定义

$$
\Omega_k(d)
=
-\log\prod_{r=1}^d a_r^{*(k)},
\qquad
\omega_k=\inf_{d\ge1}\frac{\Omega_k(d)}{d^4}.
\tag{1.6}
$$

若尾部少于 d 个非零系数，令 Ω_k(d)=+∞。空尾时全部 Ω_k(d)=+∞。

**定理 1.2。** 若

$$
\boxed{\omega_k\longrightarrow+\infty,}
\tag{1.7}
$$

则每个非零 (1.2) 循环。

后文先证明定理 1.2，再从两个具体条件推出它。条件 (1.5) 在多重和的求和步骤中明确使用；不能仅依据 a∈ℓ¹ 默认它成立。事实上 (1.7) 一旦在某个非空尾给出正的 ω_k，已可推出该尾的平方根可和；本稿把 (1.5) 保留为接口的显式假设，避免误用只有有限 d 控制的版本。

## 2. 真实局部幂的四次罚项

模型已有精确关系

$$
N_j^2=\eta_jN_{j+1},\qquad
\|N_j\|=1,\qquad
\eta_j\le e^{-770\,16^j}.
\tag{2.1}
$$

令 W_n=∥A^n∥、Λ_j=−log d_j。实际权给

$$
-\log W_n\ge\frac54n^4,\qquad
\Lambda_j\le125\,16^j.
\tag{2.2}
$$

这些是实际幂范数，不把 N_j 换成平方为零的独立位 E_j。

**引理 2.1。** 对全部 j≥0、整数 r≥1，

$$
\boxed{
\|N_j^r\|
\le
\exp\!\left[-\frac14\,16^j(r-1)^4\right].
}
\tag{2.3}
$$

**证明。** r=1 时为等号。r=2、3 时，(2.1) 给 ∥N_j^r∥≤η_j；r=4 时给 ∥N_j^4∥≤η_j²。这些界分别强于 (2.3)。

r≥5 时，由 N_j^r=A^{r2^j}/d_j^r 及 (2.2)，

$$
-\log\|N_j^r\|
\ge
16^j\left(\frac54r^4-125r\right).
\tag{2.4}
$$

而

$$
\frac54r^4-\frac14(r-1)^4
\ge r^4\ge125r
\qquad(r\ge5).
$$

所以 (2.4) 不小于 16^j(r−1)^4/4。证毕。

由平方关系，

$$
\|(I+N_j)^{-1}\|
\le\frac{2}{1-\eta_j}<3.
\tag{2.5}
$$

故对任意有限占据数组 (r_j)、r_j≥0、∑r_j=n，

$$
\begin{aligned}
\left\|\prod_jY_j^{r_j}\right\|
&\le
3^n\prod_{r_j>0}\|N_j^{r_j}\|\\
&\le
3^n
\exp\!\left[
-\frac14\sum_j16^j(r_j-1)_+^4
\right].
\end{aligned}
\tag{2.6}
$$

全部 Y_j 是同一个 A 的范数函数，故彼此交换；乘积和占据数组的改写合法。这里并不需要乘积范数等于各因子范数之积，上界的次乘性足够。

## 3. 两种占据情形支付整个 n 次幂

记

$$
B_k=\sum_{j\ge k}a_jY_j,\qquad
\sigma_k=3\sum_{j\ge k}\sqrt{|a_j|}.
\tag{3.1}
$$

由 (1.5)，σ_k→0。取 k 大，使全部尾系数模长小于 1。

对一个长度 n 的有序指标组 (j_1,…,j_n)，令 r_j 为指标 j 的出现次数，并令

$$
d=\#\{j:r_j>0\}.
$$

将系数积平均分成两半：

$$
\prod_j|a_j|^{r_j}
=
\left(\prod_j|a_j|^{r_j/2}\right)
\left(\prod_j|a_j|^{r_j/2}\right).
\tag{3.2}
$$

第一半与真实进位罚项一起支付四次衰减，第二半留到最后求和。

### 3.1 不同指标至多 n/2 个

若 d≤n/2，令 q_j=(r_j−1)_+，则

$$
\sum_{j\ge k}q_j=n-d\ge n/2.
$$

加权 Hölder 不等式给

$$
\begin{aligned}
\sum_jq_j
&=
\sum_j
(16^{j/4}q_j)\,16^{-j/4}\\
&\le
\left(\sum_j16^jq_j^4\right)^{1/4}
\left(\sum_{j\ge k}16^{-j/3}\right)^{3/4}.
\end{aligned}
$$

于是

$$
\begin{aligned}
\sum_j16^jq_j^4
&\ge
(1-16^{-1/3})^3\,16^k(n-d)^4\\
&\ge
\frac{(1-16^{-1/3})^3}{16}\,16^kn^4.
\end{aligned}
\tag{3.3}
$$

令

$$
c_{\mathrm{car}}
=\frac{(1-16^{-1/3})^3}{64}>0.
\tag{3.4}
$$

由 (2.6)，进位本身已支付
c_car16^kn⁴。第一半系数积不超过 1，可丢去。因此该有序组的贡献至多

$$
3^n e^{-c_{\mathrm{car}}16^kn^4}
\prod_j|a_j|^{r_j/2}.
\tag{3.5}
$$

### 3.2 不同指标多于 n/2 个

若 d>n/2，所有尾模长小于 1，故第一半系数的负对数至少为其不同指标的负对数和的一半。按 (1.6)，任意 d 个不同尾指标的模长积不超过前 d 个最大尾模长的积。因此

$$
\frac12\sum_jr_j(-\log|a_j|)
\ge
\frac12\Omega_k(d)
\ge
\frac12\omega_kd^4
>
\frac{\omega_k}{32}n^4.
\tag{3.6}
$$

这时即使丢去全部进位罚项，每个有序组的贡献仍至多

$$
3^n e^{-\omega_kn^4/32}
\prod_j|a_j|^{r_j/2}.
\tag{3.7}
$$

零系数产生的有序组贡献为零；无需在这些组上计算有限负对数。

### 3.3 对所有有序组求和

设

$$
\tau_k=
\min\left\{
c_{\mathrm{car}}16^k,\,
\frac{\omega_k}{32}
\right\}.
\tag{3.8}
$$

由 (3.5)–(3.7)，展开 B_k^n 并按范数求和得到

$$
\boxed{
\|B_k^n\|
\le
\sigma_k^n e^{-\tau_kn^4}
\qquad(n\ge1).
}
\tag{3.9}
$$

严格地说，先对有限尾和展开；其有序组的剩余系数和等于
(∑√|a_j|)^n。然后令有限尾截断趋无穷。由 (1.5) 及
∥Y_j∥<3，一次和及全部固定 n 次幂均按算子范数收敛，故可取极限得到 (3.9)。

由 (1.7)，τ_k→∞。又因 σ_k→0，充分大 k 有 σ_k≤1，所以

$$
\boxed{
\|B_k^n\|\le e^{-\tau_kn^4},
\qquad \tau_k\longrightarrow\infty.
}
\tag{3.10}
$$

(3.9) 中保留的 σ_k 因子可能对临界有限型有用；本定理只需 (3.10)。

## 4. 与有限前缀逆芽的实际匹配

本节给出排核步骤，明确统一常数及解析演算。所用逆芽估计也是 R103 §§4–6 的可复用结论，并不依赖 R103 的 e^{-c8^j} 特定尾假设。

若 f(0)=a_*+∑a_j≠0，则实际乘子

$$
X_f=f(0)I-2\sum_ja_jY_j
\tag{4.1}
$$

在 𝓐 中常数特征非零，因此可逆，f=X_f1 循环。

以下设 f(0)=0。若所有 a_j=0，则 f=0，与假设冲突。因此可令

$$
k_0=\min\{j:a_j\ne0\},\qquad h=2^{k_0}.
$$

定义 S=∑a_jY_j，所以 X_f=−2S。对 k>k_0，

$$
S=G_k(A^h)+B_k,\qquad
G_k(z)=
\sum_{k_0\le j<k}
\frac{a_jz^{m_j}}{d_j+z^{m_j}},
\quad m_j=2^{j-k_0}.
\tag{4.2}
$$

每个 G_k 是在零点附近解析的真正标量函数，且

$$
G_k(0)=0,\qquad
G_k'(0)=a_{k_0}/d_{k_0}\ne0
\tag{4.3}
$$

不随 k 改变。写 G_k(z)=∑g_{n,k}z^n。只有 m_j|n 的项有贡献，由 Λ_j≤12516^j，

$$
|g_{n,k}|
\le
\|a\|_1e^{125h^4n^4}.
\tag{4.4}
$$

由 Lagrange 反演，每个局部解析逆
ψ_k(w)=∑_{n≥1}b_{n,k}w^n 满足一个独立 k 的界

$$
\boxed{|b_{n,k}|\le e^{C_{\mathrm{inv}}n^4}.}
\tag{4.5}
$$

为完整起见，写 G_k=g_1z(1+U_k)。由 (4.4)，
|[z^ℓ]U_k|≤e^{C(ℓ+1)^4}。反演公式

$$
b_{n,k}
=
\frac{g_1^{-n}}n[z^{n-1}](1+U_k)^{-n}
$$

中的每项来自正整数组成 ℓ_1+⋯+ℓ_s=n−1，其系数乘积至多
exp(C∑(ℓ_i+1)^4)≤exp(16Cn⁴)；组成数、二项式数及
|g_1|^{-n} 合计只有 e^{O(n)}。这给 (4.5)。所有常数只依赖固定 a、h，不依赖 k。

反设 M=ker S 非零。M 对 A 及 B_k 不变，令

$$
T=A^h|_M.
$$

A 拟幂零，所以 T 拟幂零。在 M 上，(4.2) 给真实等式

$$
G_k(T)=-B_k|_M.
$$

对每个固定 k，通常解析芽演算的复合恒等式因此给

$$
T=\psi_k(-B_k|_M).
\tag{4.6}
$$

不要求 ∥B_k∥ 小于 ψ_k 的标量收敛半径：拟幂零算子上的任何零点邻域解析芽均有通常范数收敛的 Taylor 演算。式 (4.5) 仅用于跨 k 统一估计，并非声称一个一般四次型形式级数本身解析。

由 (3.10)、(4.5)，

$$
\|T\|
\le
\sum_{n\ge1}e^{-(\tau_k-C_{\mathrm{inv}})n^4}
\longrightarrow0.
\tag{4.7}
$$

T 不随 k 改变，故 T=0。A^h 单射，迫 M=0，矛盾。因此 S 单射。

S∈𝓐 对模型共轭 C 为复对称，故
ker S*=C ker S=0，S 值域稠密。1 对 A 循环，故

$$
\overline{\{p(A)f:p\in\mathbb C[z]\}}
=
\overline{S H}
=H.
$$

定理 1.2 得证。

## 5. 两个易检查的充分条件

### 5.1 按原索引的超三次衰减

假设 (1.3)，令

$$
\theta_k=
\inf_{j\ge k}
\frac{-\log|a_j|}{(j+1)^3}
\longrightarrow\infty.
\tag{5.1}
$$

任取 d 个不同尾指标并递增列为 j_1<⋯<j_d，有
j_r+1≥r。因此

$$
-\log\prod_{r=1}^d|a_{j_r}|
\ge
\theta_k\sum_{r=1}^d r^3
=
\theta_k\frac{d^2(d+1)^2}{4}
\ge
\frac{\theta_k}{4}d^4.
$$

对最优 d 个模长也成立，故

$$
\omega_k\ge\theta_k/4\to\infty.
\tag{5.2}
$$

同时 (1.3) 显然保证 (1.5)。定理 1.2 适用。此时 (3.8) 可取

$$
\tau_k=
\min\{c_{\mathrm{car}}16^k,\theta_k/128\}.
\tag{5.3}
$$

### 5.2 按大小降序的超三次衰减

假设 (1.4)。对正整数 R，取 K_R 足够大，使前 R 个最大非零系数对应的原始指标都小于 K_R。k≥K_R 时，

$$
a_r^{*(k)}\le a_{R+r}^*
\qquad(r\ge1).
\tag{5.4}
$$

定义

$$
\gamma_R=
\inf_{s\ge R+1}\frac{-\log a_s^*}{s^3}
\longrightarrow\infty.
$$

于是对 k≥K_R、任意 d≥1，

$$
\begin{aligned}
\Omega_k(d)
&\ge\gamma_R\sum_{r=1}^d(R+r)^3\\
&\ge\frac{\gamma_R}{4}d^4.
\end{aligned}
\tag{5.5}
$$

R 任意，故 ω_k→∞。此外
∑√|a_j|=∑√a_r^*<∞。定理 1.2 再次适用。

这一步只使用“给定有限个最大系数最终都离开尾部”，因此原始索引可以极度稀疏，也无需模长沿 j 单调。

## 6. 新例子、范围与实际未解点

以下全部允许任意实相位 φ_j、任意有限前缀，且通过
a_* = −∑a_j 形成真正的临界向量：

- a_j=exp(−c b^j+iφ_j)，任何 b>1、c>0；
- a_j=exp(−c(j+1)^{3+ε}+iφ_j)，任何 c,ε>0；
- a_j=exp(−(j+1)^3 log(j+2)+iφ_j)。

更稀疏的例子：只在任意互异指标 j_n 上取
a_{j_n}=exp(−n^4+iφ_n)，其余为零。无论 j_n 增长多快或如何排列，降序条件 (1.4) 都成立。例如 j_n=2^{2^n} 时，非零系数按原始 j 的衰减远慢于任何 exp(−c j^ε)，但本定理仍给全 H 循环性。

有限支持时，S 是 A 的非零标量解析函数，首非零阶可直接因式分解为 A^h 乘解析单位，故结论也成立。所有证明都不需要 f 本身有非零原点值。

本稿严格保留如下边界：

1. 一般 ℓ¹ 系数不自动满足平方根可和，更不自动满足 (1.7)。
2. 对 |a_j|=e^{-c(j+1)^3}，当前论证只给有限的四次型常数，不能仅由 (4.7) 宣称所有 c>0 都成立；需要进一步匹配 k 相关逆芽界与剩余 σ_k 因子。
3. 比三次更慢的任意相位尾、一般可和临界第一 chaos 以及一般 𝓐 元素的实际核仍未由本定理解决。
4. 本文仅关闭新的向量循环类；实际 A 的完整普通不变子空间问题及一般 Hilbert ISP 均未完成。

依赖原始证明位置：
[R103 完整逆芽稿](2026-11-12-first-chaos-quartic-tail-inverse-germ-0c-agent.md)；
[R88 实际乘子](2026-11-12-riesz-basis-bounded-multipliers-strong-closure-0c-agent.md)；
[R74 精确幂尺度](2026-11-12-all-power-gevrey-by-exact-norms-0c.md)。
