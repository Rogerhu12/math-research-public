# R95 草稿：临界第一 chaos 的精确有界除法判据与全空间循环类

日期：2026-11-12（UTC）。独占稿：critical_kernel。

**状态：本稿全部陈述的除法分类、值域分类及循环性结论均已证明。** 任意可和复系数均允许。结果用一个加权差分的 ℓ² 条件精确判断实际临界第一 chaos 乘子能否由任何 B(H) 算子除以 A；满足该条件时，首个非零 A 次幂后的商实际属于 𝓐 且可逆，因此排除整个 H 上的核。条件不满足时，本稿只证明有界除法失败，不证明存在核，也不把此前有限 chaos 的配对分离误作全 H 单射性。

本稿改进 R36 中绝对可和的加权充分条件：这里的条件是充要的，允许加权系数不趋零、甚至无界，并允许任意复相位。它与 R60–R75 的规则幂尾及 Newton 主面机制互补；例如规则幂尾通常不满足本稿的有界除法条件，而其单射性可能已由那些定理证明。

内部依赖：[R12](../results/R12-normalized-powers-and-compact-commutant.md) 的实际归一化幂，[R32](../results/R32-gauge-action-and-formal-coefficients.md) 的常数特征与单点谱，[R49](../results/R49-incomparable-critical-and-power-ranges.md) 的单边链表示及正算子序入口，R88 的第一 chaos 实际乘子公式。所需前缀 ℓ² 合成、实际误差、矩阵列与求和证明全部给出。

## 1. 记号与主定理

为避免向量系数与实际算子权混淆，将实际径向权记为

$$
\alpha_j=e^{-L_j},\qquad
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
\tag{1.1}
$$

记

$$
\eta_j=\frac{\alpha_{j+1}}{\alpha_j},\quad
d_j=\|A^{2^j}\|,\quad
N_j=\frac{A^{2^j}}{d_j},\quad
Y_j=N_j(I+N_j)^{-1}.
\tag{1.2}
$$

已有

$$
\|N_j\|=1,\quad N_j^2=\eta_jN_{j+1},\quad
\|N_j-E_j\|=\eta_j,\quad
\eta_j\le e^{-770\,16^j}.
\tag{1.3}
$$

特别地，

$$
\|(I+N_j)^{-1}\|
\le\frac{2}{1-\eta_j}<3,\qquad
\|Y_j\|<3.
\tag{1.4}
$$

设

$$
f=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
(a_j)\in\ell^1,\qquad
a_*+\sum_ja_j=0,\qquad f\ne0.
\tag{1.5}
$$

因此 f 是连续的临界第一 chaos 向量。R88 给出其唯一有界实际乘子

$$
X_f=-2S,\qquad
S=\sum_{j\ge0}a_jY_j\in\mathcal A,
\tag{1.6}
$$

级数按算子范数绝对收敛。取

$$
k_0=\min\{j:a_j\ne0\},\qquad s=2^{k_0},
\tag{1.7}
$$

并在 j≥k_0 定义

$$
b_j=\frac{a_j}{\alpha_j},\qquad
\Delta b_j=b_j-b_{j-1}\quad(j>k_0).
\tag{1.8}
$$

**定理 1.1：精确有界除法。** 下列条件等价：

1. (Δb_j)_{j>k_0}∈ℓ²；
2. 存在 B∈B(H)，使 S=AB；
3. 存在 B∈B(H)，使 S=BA；
4. Ran S⊂Ran A；
5. 存在 𝓐 中的可逆元 U，使 S=A^sU。

所有有界商在相应因子关系中均唯一。特别地，只要这些条件成立，

$$
\ker S=\{0\},\qquad
\operatorname{Ran}S=\operatorname{Ran}A^s,\qquad
\overline{\operatorname{Ran}S}=H,
\tag{1.9}
$$

而 f 对实际 A 循环，另一端允许任意 H 向量。

**定理 1.2：全部正整数次幂的值域分类。** 对任意整数 r≥1，

$$
\boxed{
\operatorname{Ran}S\subseteq\operatorname{Ran}A^r
\iff
r\le s\ \text{且}\ (\Delta b_j)_{j>k_0}\in\ell^2.}
\tag{1.10}
$$

此时唯一的有界商为 A^{s-r}U，属于 𝓐；左除与右除等价。特别地，若加权差分不在 ℓ²，则 S 不属于 AB(H) 或 B(H)A，即使原始系数 a_j 衰减得极快。

## 2. 一个独立位前缀的 ℓ² 算子合成引理

固定起点 k。对 j≥k 定义

$$
P_{k,j}=\prod_{\ell=k}^{j-1}E_\ell,\qquad P_{k,k}=I.
\tag{2.1}
$$

**引理 2.1。** 对任意有限标量族 c_j，

$$
\left\|\sum_{j\ge k}c_jP_{k,j}\right\|
\le2\left(\sum_{j\ge k}|c_j|^2\right)^{1/2}.
\tag{2.2}
$$

因此右端平方可和时，级数按算子范数收敛；不是仅对某个向量强收敛。

**证明。** 令 Q_{j,0}、Q_{j,1} 为第 j 位分别为物理 0、1 的正交投影，写

$$
P_{k,j}=P_{k,j}Q_{j,0}+P_{k,j}Q_{j,1}.
\tag{2.3}
$$

第一族算子的值域分别位于

$$
b_k=\cdots=b_{j-1}=1,\qquad b_j=0
$$

这些两两不交的柱集合，因此第一族具有两两正交的值域。每项范数至多一，故

$$
\left\|\sum_jc_jP_{k,j}Q_{j,0}\right\|\le\|c\|_2.
\tag{2.4}
$$

第二族算子的初始空间分别位于

$$
b_k=\cdots=b_{j-1}=0,\qquad b_j=1,
$$

同样两两正交。对伴随使用 (2.4) 得

$$
\left\|\sum_jc_jP_{k,j}Q_{j,1}\right\|\le\|c\|_2.
\tag{2.5}
$$

相加即得 (2.2)。j=k 的空前缀也符合这两个停止位描述。尾系数的同一估计给算子范数收敛。证毕。

这里的正交来自首个停止位，不要求系数同号，也没有将不同前缀的整个值域错误地当作正交。

## 3. 真实前缀保留同一 ℓ² 合成

定义实际前缀

$$
T_{k,j}=\prod_{\ell=k}^{j-1}N_\ell,\qquad T_{k,k}=I.
\tag{3.1}
$$

每个前缀范数至多一。固定 j 时，排序 telescoping 给

$$
T_{k,j}-P_{k,j}
=
\sum_{\ell=k}^{j-1}
T_{k,\ell}(N_\ell-E_\ell)P_{\ell+1,j}.
\tag{3.2}
$$

对有限 c_j 求和，并先固定错误位 ℓ：

$$
\sum_jc_j(T_{k,j}-P_{k,j})
=
\sum_{\ell\ge k}
T_{k,\ell}(N_\ell-E_\ell)
\left(\sum_{j>\ell}c_jP_{\ell+1,j}\right).
\tag{3.3}
$$

由引理 2.1，括号内的范数至多 2∥(c_j)_{j>ℓ}∥₂。因此

$$
\left\|\sum_jc_j(T_{k,j}-P_{k,j})\right\|
\le2\left(\sum_{\ell\ge k}\eta_\ell\right)\|c\|_2.
\tag{3.4}
$$

连同 (2.2)，得到

$$
\boxed{
\left\|\sum_{j\ge k}c_jT_{k,j}\right\|
\le C_k\|c\|_2,\qquad
C_k=2\left(1+\sum_{\ell\ge k}\eta_\ell\right).}
\tag{3.5}
$$

该界同样保证 ℓ² 系数时按算子范数收敛于 𝓐，因为各 T_{k,j} 都是 A 的多项式。没有把形式除法当作算子。

下面固定 k=k_0，简记 T_j=T_{k_0,j}。

## 4. Abel 恒等式与总是有界的真实进位误差

由 N_j²=η_jN_{j+1}，归纳得到

$$
N_{k_0}T_j=\frac{\alpha_j}{\alpha_{k_0}}N_j
\qquad(j\ge k_0).
\tag{4.1}
$$

定义

$$
Q_j=T_j(I+N_j)^{-1}.
$$

使用精确代数恒等式

$$
(I+N_j)^{-1}=I-N_j+N_j^2(I+N_j)^{-1}
$$

得

$$
Q_j=T_j-T_{j+1}+R_j,\qquad
R_j=T_jN_j^2(I+N_j)^{-1},
\tag{4.2}
$$

且

$$
\|R_j\|\le3\eta_j.
\tag{4.3}
$$

为方便与首个 N_{k_0} 相配，将加权系数缩放为

$$
\beta_j=\alpha_{k_0}b_j
=\frac{\alpha_{k_0}a_j}{\alpha_j}.
\tag{4.4}
$$

注意 β_{k_0}=a_{k_0}≠0。由 (4.1)，

$$
a_jY_j=N_{k_0}\beta_jQ_j.
\tag{4.5}
$$

一个对任意原始 ℓ¹ 系数都成立的估计是

$$
\sum_{j\ge k_0}|\beta_j|\eta_j<\infty.
\tag{4.6}
$$

确切地说，(1.1) 给

$$
L_{j+1}-2L_j
=\frac{3920}{3}16^j-540\,8^j+\frac{850}{3}
\ge1050.
\tag{4.7}
$$

故

$$
|\beta_j|\eta_j
=\alpha_{k_0}|a_j|
\frac{\alpha_{j+1}}{\alpha_j^2}
\le\alpha_{k_0}e^{-1050}|a_j|.
\tag{4.8}
$$

因此真实误差级数 ∑β_jR_j 总按范数绝对收敛，无需假设 β 有界或趋零。

对 J≥k_0 求和 (4.2)，精确得到

$$
\sum_{j=k_0}^J\beta_jQ_j
=
\beta_{k_0}I
+\sum_{j=k_0+1}^J(\beta_j-\beta_{j-1})T_j
-\beta_JT_{J+1}
+\sum_{j=k_0}^J\beta_jR_j.
\tag{4.9}
$$

关键是不能直接丢掉最后一个前缀边界项。将它乘回 N_{k_0} 后，由 (4.1) 得

$$
N_{k_0}\beta_JT_{J+1}
=a_J\eta_JN_{J+1}\longrightarrow0
\quad\text{于算子范数}.
\tag{4.10}
$$

(4.10) 只用 a∈ℓ¹ 及 η_J≤1。它不要求 β_JT_{J+1} 本身强趋零或范数趋零。

## 5. 充分性：真正的可逆首阶商

现在假设 (Δb_j)_{j>k_0}∈ℓ²。等价地 Δβ∈ℓ²。由 (3.5) 与 (4.6)，下式按算子范数定义一个 𝓐 元素：

$$
V=
a_{k_0}I
+\sum_{j>k_0}(\beta_j-\beta_{j-1})T_j
+\sum_{j\ge k_0}\beta_jR_j.
\tag{5.1}
$$

由 (4.5)、(4.9)、(4.10) 及原始 S 级数的范数收敛，

$$
S=N_{k_0}V.
\tag{5.2}
$$

这是实际有界算子等式。还可记录明确的范数界：

$$
\|V\|
\le |a_{k_0}|
+C_{k_0}\alpha_{k_0}\|\Delta b\|_2
+3\alpha_{k_0}e^{-1050}\|a\|_1.
\tag{5.3}
$$

所有 j>k_0 的 T_j 都具有正的 A 次数；每个 R_j 也具有正的 A 次数。所以 R32 的常数特征给

$$
c_0(V)=a_{k_0}\ne0.
\tag{5.4}
$$

由 𝓐 的单点谱结论，V 在 𝓐 中可逆。令 U=V/d_{k_0}，则

$$
\boxed{S=A^sU,\qquad U\in\mathcal A\text{ 可逆}.}
\tag{5.5}
$$

这证明定理 1.1 的 1⇒5，并同时给出全空间单射、稠密值域及准确实际值域等式。因 X_f=-2S 且 f=X_f1，而 1 对 A 循环，

$$
\overline{\{p(A)f:p\in\mathbb C[z]\}}
=\overline{X_fH}=H.
\tag{5.6}
$$

所以 f 对 A 循环；这里没有限制可能的正交向量具有有限 chaos。

## 6. 必要性的合法入口：只转移正算子序

假设存在任意 B∈B(H)，使

$$
S=AB.
\tag{6.1}
$$

不预设 B 属于 UHF 或 𝓐。由实际关系，

$$
SS^*\le\|B\|^2AA^*.
\tag{6.2}
$$

R49 的等距含单位 * 表示

$$
\pi:\mathcal U\longrightarrow B(\ell^2(\mathbb N_0))
$$

把 A 送为单边加权移位

$$
\pi(A)e_n=\alpha_{v_2(n+1)}e_{n+1},
\qquad
\pi(A)^re_n=\frac{W_{n+r}}{W_n}e_{n+r}.
\tag{6.3}
$$

这个表示可直接由有限局部矩阵在整数 n 的低位上作用构造，每个局部矩阵保持范数。这里只对 (6.2) 中的 S、A 施加 π，绝不对未知 B 施加 π。

由转移后的正序界，在 Ran π(A)* 上定义

$$
T_0(\pi(A)^*x)=\pi(S)^*x.
$$

它良定义且范数至多 ∥B∥。延至该值域闭包，并在正交补置零后取伴随，得到有界 T，满足

$$
\pi(A)T=\pi(S),\qquad \|T\|\le\|B\|.
\tag{6.4}
$$

这是所需有界因子的直接构造。它不转移原表示的核。

## 7. 商的第零列强制加权差分平方可和

由 (6.3)，π(N_k) 的幂在 e_0 上满足

$$
\pi(N_k)^r e_0
=\frac{W_{r2^k}}{d_k^r}e_{r2^k}.
\tag{7.1}
$$

在 π(Y_k)=π(N_k)(I+π(N_k))⁻¹ 的展开中，第 2^j 行只有 k≤j 能贡献，指数为 r=2^{j-k}。k=j 时符号为正；k<j 时 r 为偶数，符号为负。故

$$
\langle\pi(S)e_0,e_{2^j}\rangle
=W_{2^j}\left(
\frac{a_j}{d_j}
-\sum_{k=k_0}^{j-1}
\frac{a_k}{d_k^{2^{j-k}}}
\right).
\tag{7.2}
$$

由于 π(A) 从 e_{2^j-1} 到 e_{2^j} 的权恰为 α_j，(6.4) 给

$$
\langle Te_0,e_{2^j-1}\rangle
=b_j-\sum_{k=k_0}^{j-1}\mu_{k,j}b_k,
\tag{7.3}
$$

其中

$$
\mu_{k,j}
=\frac{W_{2^j-1}}{W_{2^k-1}d_k^{2^{j-k}-1}}
=\frac{\prod_{\ell=k}^{j-1}d_\ell}
{d_k^{2^{j-k}-1}}.
\tag{7.4}
$$

由 d_{\ell+1}=η_\ell d_\ell²，

$$
\mu_{j-1,j}=1,
\tag{7.5}
$$

而对 j≥k+2，

$$
\boxed{
\mu_{k,j}
=\prod_{\ell=k}^{j-2}
\eta_\ell^{\,2^{j-\ell-1}-1}.}
\tag{7.6}
$$

因此 (7.3) 精确写为

$$
\langle Te_0,e_{2^j-1}\rangle
=\Delta b_j-r_j,\qquad
r_j=\sum_{k=k_0}^{j-2}\mu_{k,j}b_k,
\tag{7.7}
$$

约定 b_{k_0-1}=0，故 j=k_0 时 Δb_j=b_j，空和为零。

接着证明误差数组 r 本身总在 ℓ¹。因为所有 η_\ell<1，(7.6) 给

$$
\mu_{k,j}\le
\eta_k^{\,2^{j-k-1}-1}
\le\eta_k^{j-k-1}.
$$

所以

$$
\sum_{j\ge k+2}\mu_{k,j}
\le\frac{\eta_k}{1-\eta_k}.
\tag{7.8}
$$

令 η_*=\sup_jη_j<1。由 Tonelli、(4.7)，

$$
\begin{aligned}
\sum_j|r_j|
&\le\sum_{k\ge k_0}
|b_k|\frac{\eta_k}{1-\eta_k}\\
&\le
\frac{e^{-1050}}{1-\eta_*}\sum_{k\ge k_0}|a_k|
<\infty.
\end{aligned}
\tag{7.9}
$$

另一方面，不同 j 的行索引 2^j-1 不同，而 Te_0∈ℓ²。因此 (7.7) 左端构成 ℓ² 数列。结合 r∈ℓ¹⊂ℓ²，得到

$$
\boxed{(\Delta b_j)_{j>k_0}\in\ell^2.}
\tag{7.10}
$$

这证明必要性 2⇒1。特别地，实质条件是整个商列的平方可和性，而不仅是单个系数有界。

## 8. 左右商、全部值域以及唯一性

若 S=BA，则

$$
[B,A]A=BA^2-ABA=SA-AS=0.
$$

A 的值域稠密，故 [B,A]=0，于是 S=AB。因此 3⇒2；反向显然由已构造的 𝓐 商给出。

若 Ran S⊂Ran A，则 A 单射使 A⁻¹S 成为定义在全 H 的算子。若 x_n→x 且 A⁻¹Sx_n→y，则 Ay=Sx，所以由单射性 A⁻¹Sx=y。其图闭；闭图定理给有界因子 S=AB。因此 4⇒2。反向由因子关系直接成立。这完成定理 1.1 的等价性。

所有左商唯一，因为 A 及其正幂单射；所有右商唯一，因为 A 及其正幂值域稠密。

对 r≥1，若 Ran S⊂Ran A^r，同样的闭图论证给 S=A^rB，因而 S=A(A^{r-1}B)。定理 1.1 已强制 Δb∈ℓ²。还必须 r≤s：将相应正序不等式转移到 π 后，Ran π(A)^r 的前 r 个坐标全部为零，而 π(S)e_0 的首个非零坐标恰在 s=2^{k_0}，系数 a_{k_0}≠0。因此 r>s 不可能。

反过来，若 Δb∈ℓ² 且 r≤s，(5.5) 直接给

$$
S=A^r(A^{s-r}U),
$$

其中括号内属于 𝓐。由唯一性，这就是任意 B(H) 中可能的商。定理 1.2 得证。

特别地，本类中的有界 A 商一旦存在，就自动属于 𝓐；没有隐藏在完整交换子较大的 SOT 闭包中。

## 9. 超出旧加权绝对可和条件的例子

以下均令 a_*=-∑a_j，使 f(0)=0。可从任意固定 k_0 开始，有限前缀取零；为简化记号从 j=0 开始。

### 9.1 加权系数不趋零

取

$$
a_j=\alpha_j,\qquad b_j=1.
$$

加权绝对和 ∑|a_j|/α_j 发散，但 Δb=0。故 f 对 A 循环，且 S=A 乘以实际可逆的 𝓐 元素。

### 9.2 加权系数无界

取任意实 γ<1/2，例如 γ=1/3，并令

$$
a_j=\alpha_j(j+1)^\gamma.
$$

则 b_j=(j+1)^γ，而 Δb_j=O(j^{γ-1})∈ℓ²。因此同样给全 H 循环性。原始 a_j 当然可和，因 α_j 超快衰减。也可取 b_j=√(j+2)/log(j+2)，其差分平方可和而 b_j 无界。

### 9.3 不收敛的复相位

取

$$
a_j=\alpha_j(j+1)^{it},\qquad t\in\mathbb R.
$$

当 t≠0 时加权相位不收敛，但 Δb_j=O_t(j⁻¹)∈ℓ²，结论仍成立。更一般地，任意复序列 b 满足 Δb∈ℓ² 都可用；该条件自动给 b_j=O(√(j+1))，从而 α_jb_j∈ℓ¹。

### 9.4 极快原始尾仍不能自动有界除法

取

$$
a_j=(-1)^j\alpha_j.
$$

这时 b_j=(-1)^j、|Δb_j|=2，因而 S 不属于 AB(H) 或 B(H)A，也不满足任何正整数次幂的值域包含。

此例的系数与前面例子具有相同的绝对值，说明有界除法不仅由衰减速度决定；相邻加权差分也参与。**本稿没有判定这个交替例的核，不能从不可有界除法推出非零核。**

## 10. 与既有核结论的关系及下一缺口

R36 的加权 ℓ¹ 条件蕴含本稿条件：若 ∑|b_j|<∞，则 b∈ℓ²，且 Δb∈ℓ²。但反向明显不成立，§9.1–9.3 给出实际循环的新例。新证明依赖停止位前缀的 ℓ² 合成及 Abel 边界项的真实消去，不是把绝对值求和粗估再重复一次。

规则幂尾 a_j∼c(j+2)⁻ᵖ 一般使 a_j/α_j 迅速增长，因而不能沿本条完成有界除法。它们的全空间单射性必须由 R60–R75 那类半群/Bernstein–Walsh 或 Newton 主面机制获得；本条并未取代这些机制。

R91 已证明任意第一 chaos 与任意有限 chaos 全矩分离。本稿在 Δ(a_j/α_j)∈ℓ² 的临界可和分支把另一端扩大到整个 H，并同时给出精确值域。而 Δ(a_j/α_j)∉ℓ² 的一般可和复尾仍可能需要新的真实核论证；即便原始尾比每个幂都快，也不能只凭形式首阶或一般解析局部函数直觉解决。

没有得到一般临界第一 chaos 的全 H 单射性，也没有构造非平凡普通闭不变子空间。本稿完成的是一个精确有界除法分类及相应实际循环类。
