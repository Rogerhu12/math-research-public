# R122：有限 dyadic gauge 差、解析 cocycle 与实际核

日期：2026-11-12（UTC）。独占稿：critical_kernel。
状态：**已证明。** 根、l2_moments、literature 已独立核对核心链条；本稿写出完整证明。整个论证作用在原 Haar 表示及真实 A 上，不使用纯模型核的连续性。

## 1. 实际模型与主结论

沿用

$$
H=L^2(\mathbb Z_2,\mu),\qquad
(Af)(y)=w(y)f(y-1),
$$

其中 Haar 测度 μ，w(y)>0 几乎处处，A 单射、拟幂零，且

$$
N_j=A^{2^j}/d_j,\qquad
N_j=E_j+\eta_jE_j^*N_{j+1},\quad
\|N_j-E_j\|\le\eta_j\to0,\quad\|N_j\|=1.
$$

𝓐 为 A 的含单位多项式范数闭包。反线性对合为
(Cf)(y)=overline{f(−1−y)}，相应连续双线性形式为

$$
B(f,g)=\langle f,Cg\rangle
=\int_{\mathbb Z_2}f(y)g(-1-y)\,d\mu(y).
\tag{1}
$$

每个与 A 交换的有界算子 X∈{A}' 都 B 对称：

$$
B(Xf,g)=B(f,Xg).
\tag{2}
$$

这里不把范围限于𝓐。其直接证明只需 1 对 A 循环：在稠密的多项式轨道上，对任意 p、q，利用 A 的 B 对称性及 B 自身对称性，

$$
B(Xp(A)1,q(A)1)
=B(X1,p(A)q(A)1)
=B(p(A)q(A)1,X1)
=B(p(A)1,Xq(A)1).
$$

再由有界性延拓到全部 H。

**主定理。** 对任意非零可和复系数列 a，

$$
\boxed{
S=\sum_{j\ge0}a_jN_j(I+N_j)^{-1}
}
\tag{3}
$$

单射且值域稠密。没有相位、单调性、尾速度或支撑规则假设。

因此每个非零有界第一 Walsh chaos 向量

$$
f=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^1,
\tag{4}
$$

都对 A 循环。特别地，R103–R111 中尚未覆盖的小三次型及任意慢可和复尾，在第一 chaos 类内全部被本定理覆盖。

证明先给出一个适用于整个有界交换子的 gauge 差判据。§4.2 还证明：若非标量 X∈{A}' 的每个 dyadic gauge 增量都是某个真正解析芽作用于 A，则对每个复数 λ，X−λI 都单射稠密。§7 将此机制应用于 R112 的连续二阶块例子。

## 2. 每个非零闭不变限制都具有稠密的幂值域

**引理 2.1。** 对任意闭 A 不变子空间 M，以及每个整数 r≥1，

$$
\boxed{\overline{A^rM}=M.}
\tag{5}
$$

**证明。** 取

$$
Z_m=\frac2m\sum_{j=m}^{2m-1}N_j.
$$

有 ∥Z_m∥≤2。若 u 是有限柱向量，m 大于其全部位指标，则

$$
\frac2m\sum_{j=m}^{2m-1}E_ju
=u\,\frac2m\sum_{j=m}^{2m-1}b_j,
$$

其中 b_j 为物理 0–1 位。独立 Haar 位的方差给右侧在 L² 中趋 u。
又 N_j−E_j 的平均范数趋零。因此 Z_mu→u。用有限柱稠密性及
∥Z_m∥≤2，推广到全部 H：

$$
Z_m\longrightarrow I\quad\text{强收敛}.
\tag{6}
$$

固定 r，充分大 m 有每个 2^j≥r；于是

$$
Z_m=A^rQ_m(A)
$$

其中 Q_m 是一个有限多项式。故 Z_mM⊂A^rM。由 (6)，M⊂closure(A^rM)；反向来自闭不变性。证毕。

若 U∈𝓐 可逆，则 U、U^{-1} 均保持 M，所以 UM=M。因此任何已经具有真正分解

$$
F=A^rU,\qquad U\in\mathcal A\text{ 可逆}
\tag{7}
$$

的算子都满足 closure(FM)=M。非零零点解析芽 F(A) 是这种情况，包括首阶为0的可逆芽。

## 3. dyadic 字符与共轭核

对任意 dyadic 单位根 ζ（某个 ζ^{2^m}=1），令

$$
\vartheta_\zeta(y)=\zeta^{\,y\bmod2^m},
\qquad
(U_\zeta f)(y)=\vartheta_\zeta(y)f(y).
$$

定义与所选更大 m 无关。U_ζ 酉，且

$$
U_\zeta A U_\zeta^*=\zeta A,
\qquad
\gamma_\zeta(X)=U_\zeta XU_\zeta^*.
\tag{8}
$$

γ_ζ 同时保持𝓐及整个交换子 {A}'。

若 M=ker X，则

$$
M_\zeta:=U_\zeta M=\ker\gamma_\zeta(X).
\tag{9}
$$

**引理 3.1。** 假设 D_ζ=γ_ζ(X)−X 在 M 上具有稠密值域。
则

$$
\boxed{B(M,U_\zeta M)=0.}
\tag{10}
$$

**证明。** 对 v∈M、z∈M_ζ，由 (2) 及各自的核关系，

$$
B(D_\zeta v,z)
=
B(\gamma_\zeta(X)v,z)-B(Xv,z)
=
B(v,\gamma_\zeta(X)z)-0=0.
$$

用 D_ζM 在 M 中稠密及 B 连续，即得 (10)。这里使用的是
γ_ζ(X)∈{A}' 的 B 对称性，不要求 U_ζ 本身 B 对称。证毕。

## 4. 只剩有限个 Fourier 模式会迫核有限维

**定理 4.1（gauge 差排核判据）。** 设 0≠X∈{A}'。若存在 2 的幂 h，
使对每个 dyadic ζ 满足 ζ^h≠1，D_ζ=γ_ζ(X)−X 具有分解

$$
D_\zeta=A^{r_\zeta}U_\zeta',
\qquad r_\zeta\ge0,\quad U_\zeta'\in\mathcal A\text{ 可逆},
\tag{11}
$$

则 X 单射、值域稠密，X1 循环。

**证明。** 反设 M=ker X≠0。M 闭且 A 不变。由引理2.1及 (11)，
D_ζM 在 M 中稠密，所以引理3.1给 (10)。

固定 v,w∈M，定义 L¹ 函数

$$
F_{v,w}(y)=v(y)w(-1-y).
$$

由字符性质，

$$
B(v,U_\zeta w)
=
\zeta^{-1}\int F_{v,w}(y)\,
\overline{\vartheta_\zeta(y)}\,d\mu(y).
\tag{12}
$$

因此 F_{v,w} 的 Fourier 系数在所有 ζ^h≠1 处为零。它只剩
h 个字符，也就是

$$
\boxed{F_{v,w}\text{ 只依赖 }y\bmod h.}
\tag{13}
$$

这里的 Fourier 唯一性可以直接通过有限条件期望验证：令 h=2^s，
对 m≥s，前 m 位条件期望的有限 Fourier 展开只剩这 h 项，所以等于前 s 位条件期望。条件期望在 L¹ 中趋原函数，故得到 (13)。没有对 L² 向量取未定义点值。

下面证明 M 在每个 h 柱上的限制至多一维。

取 M 的可数稠密族 (v_n)，并定义其总本质支撑

$$
E=\bigcup_n\{y:v_n(y)\ne0\},
$$

按可测代表理解，忽略零测集合。每个 M 中的向量在 E 外都为零，
因为这一性质在 L² 中闭。由 A 不变及 w>0 几乎处处，

$$
E+1\subseteq E\quad\text{模零集}.
$$

Haar 平移保持测度，故 E+1=E 模零集。odometer 平移遍历，所以 E 为零测或全测；M≠0 排除零测，故

$$
\mu(E)=1.
\tag{14}
$$

反射 R(y)=−1−y 同样保测，所以 E∩R(E) 全测。
对每个柱 Q_t={y:y≡t mod h}，有

$$
Q_t\subseteq
\bigcup_{n,\ell}
\{y:v_n(y)v_\ell(-1-y)\ne0\}
\quad\text{模零集}.
$$

这是可数并；Q_t 正测，故存在一对 v_t,w_t∈M，其乘积在 Q_t 的正测子集上非零。由 (13)，该乘积在整个 Q_t 上为同一个常数，所以此常数 c_t≠0：

$$
v_t(y)w_t(-1-y)=c_t
\quad\text{几乎处处于 }Q_t.
\tag{15}
$$

对任意 u∈M，(13) 同样使 u(y)w_t(−1−y) 在 Q_t 上等于某常数 d_t(u)。由 (15)，

$$
u|_{Q_t}=\frac{d_t(u)}{c_t}\,v_t|_{Q_t}.
\tag{16}
$$

因此 M 在每个柱的限制只有一维。把 h 个柱的标量合在一起，
M 线性嵌入 C^h，得到

$$
\dim M\le h.
\tag{17}
$$

但 A 单射、拟幂零，故没有非零有限维不变子空间：在非零有限维
M 上，A|_M 必有特征值；其谱包含于{0}（幂范数根仍趋零），因此必有非零零特征向量，违背单射性。矛盾，故 ker X=0。

X 的 C 对称性给 ker X*=C ker X=0，所以值域稠密。
1 对 A 循环，X 与 A 交换，故 X1 也循环。证毕。

### 4.2 全交换子的解析加性 cocycle

**定理 4.2。** 设 X∈{A}' 非标量，并且对每个 dyadic 单位根 ζ，存在一个在0邻域真正解析的标量芽 F_ζ，使

$$
\gamma_\zeta(X)-X=F_\zeta(A).
\tag{A1}
$$

允许 F_ζ=0，也不要求不同 ζ 的芽具有统一收敛半径。则对每个 λ∈C，

$$
\boxed{\ker(X-\lambda I)=0,\qquad
\overline{\operatorname{Ran}(X-\lambda I)}=H.}
\tag{A2}
$$

相应地，每个 (X−λI)1 都对 A 循环。

**证明。** 令 G=∪_{m≥0}μ_{2^m} 为全部 dyadic 单位根，并定义

$$
H_X=\{\zeta\in G:\gamma_\zeta(X)=X\}.
$$

因为 γ 为群作用，H_X 是 G 的子群。G 的每个真子群都等于某个有限群 μ_h，其中 h 是2的幂：若子群内元素的阶无界，它对每个 m 都含一个阶至少2^m的元素，因而含整个 μ_{2^m}，于是等于 G；阶有界时则是某个循环2群的子群。

下面排除 H_X=G。若全部 gauge 都固定 X，X 就与所有有限柱字符乘法算子交换，因有限 Fourier 展开也与所有有限柱指示函数乘法算子交换。置 φ=X1。对每个有限柱函数 f 有 Xf=φf。由

$$
\|\phi1_E\|_2\le\|X\|\,\mu(E)^{1/2}
$$

对所有有限柱集合 E 成立，有限条件期望给
E(|φ|² | 前 m 位)≤∥X∥²；令 m→∞，得 |φ|≤∥X∥ 几乎处处。因此 φ∈L∞，柱函数稠密性给 X=M_φ。由 XA=AX 并作用于1，

$$
w(y)\phi(y)=w(y)\phi(y-1).
$$

w>0 几乎处处，所以 φ 为 odometer 不变函数。遍历性迫 φ 为常数，与 X 非标量矛盾。因此 H_X=μ_h 有限。

对 ζ∉μ_h，F_ζ(A)≠0。真正解析芽的演算在本题为忠实：非零芽 F=z^r u、u(0)≠0，给 F(A)=A^r u(A)≠0，其中 u(A) 是𝓐单位，A 单射。因此 F_ζ 本身非零，且

$$
F_\zeta(A)=A^{r_\zeta}u_\zeta(A),
\qquad u_\zeta(0)\ne0.
$$

这正满足定理4.1。X−λI 的全部 gauge 增量与 X 完全相同，而且 X 非标量保证 X−λI≠0。将定理4.1逐一用于 X−λI，即得 (A2)。证毕。

该结论明确排除点谱，并排除因非稠密值域造成的残余谱；它不声称 X−λI 对全部 λ 都有有界逆。

## 5. 全部可和第一 chaos 的实际核

取 (3) 的非零 a，令 k_0=min{j:a_j≠0}、h=2^{k_0}。
级数按算子范数绝对收敛，因为 ∥N_j(I+N_j)^{-1}∥<3。

若 ζ^{2^m}=1，则对全部 j≥m，

$$
\gamma_\zeta(N_j)=\zeta^{2^j}N_j=N_j.
$$

因此

$$
\gamma_\zeta(S)-S
=
\sum_{k_0\le j<m}
a_j
\left[
\frac{\zeta^{2^j}N_j}{I+\zeta^{2^j}N_j}
-\frac{N_j}{I+N_j}
\right].
\tag{18}
$$

它是一个有限和，每项都为某个零点附近真正解析的标量函数作用于 A。若 ζ^h≠1，其首阶为 h，首系数为

$$
a_{k_0}(\zeta^h-1)/d_{k_0}\ne0.
\tag{19}
$$

故 (18) 精确写成 A^h 乘一个解析单位。定理4.1适用，S 单射稠密。

对 (4)，R88 给

$$
X_f=f(0)I-2S,\qquad X_f1=f.
$$

若 f(0)≠0，X_f 在𝓐中可逆。若 f(0)=0，f≠0迫 a≠0，上述结论适用−2S。因此全部非零有界第一 chaos 向量都循环。

这里的“有界第一 chaos”恰对应 a∈ℓ¹；不把结论自动扩大到一般
a∈ℓ² 的无界第一 chaos 输入。

## 6. 一个直接的无限次数推广

取非空有限位集 J 的族，令

$$
Y_J=\prod_{j\in J}N_j(I+N_j)^{-1}.
$$

假设系数 b_J 满足

$$
\sum_J3^{|J|}|b_J|<\infty,
\tag{20}
$$

并且支撑局部有限：每个固定物理位只属于有限个 b_J≠0 的 J。
令 X=∑_J b_JY_J，不全为零。

对给定 ζ^{2^m}=1，所有 J⊂{m,m+1,…} 的项被 γ_ζ 固定。
剩下与前 m 位相交的 J 只有有限个。因此 γ_ζ(X)−X 是有限个
真正解析函数的和。

非零 X 有唯一有限形式首阶 r（R32）。对 ζ^r≠1，差的首阶仍为 r，
所以它是 A^r 乘解析单位。dyadic 根中 ζ^r=1 的集合恰为
μ_{2^{v_2(r)}}，是有限群。定理4.1给 X 单射稠密、X1 循环。

这里不全为零的系数确使 X≠0：令 r=min{∑_{j∈J}2^j:b_J≠0}，
二进位唯一性给唯一首项，其首系数 b_J/W_r≠0。

由有限柱公式 Y_J1=∏_{j∈J}b_j^{phys}，
得到一个无需任何尾速度、可具有无限次数的明确连续循环类。
(20) 保证其函数级数一致收敛。此推广只是方便直接核验的充分类；
不声称任意连续函数都具有这个展开和局部有限性。

## 7. R112 的 Hadamard 块例子现在具有全 H 循环性

R112 原构造的完整细节见
[独占原稿](2026-11-12-bounded-quadratic-no-l1-power-series-0c-agent.md)。
这里只重列本证明需要的精确性质。

第 n 块取 N_n=2^{4n}、t_n=2^{-n}，使用两个各含 N_n 个物理位的有限集合 I_n、J_n；所有块的位互不相交。用 Sylvester Hadamard 矩阵
H_{xy}=(-1)^{x·y}，令

$$
q_n=\sum_{x,y\in\mathbb F_2^{4n}}
t_nN_n^{-3/2}H_{xy}\chi_{i_x}\chi_{j_y},
\qquad
f_n=q_n-q_n(0)1.
\tag{B1}
$$

由 HH*=N_nI，有

$$
\|q_n\|_\infty\le t_n,\quad
q_n(0)=t_n/\sqrt{N_n},\quad
\|f_n\|_\infty\le2t_n.
$$

所以 f=∑_n f_n 一致收敛，非零且属于连续二阶 Walsh chaos，f(0)=0。
R92 的次数为2的维数统一乘子界给

$$
S=\sum_n S_n,\qquad S_n=X_{f_n},\qquad
\|S_n\|\le2C_2t_n,\qquad S1=f.
\tag{B2}
$$

故级数按算子范数绝对收敛，S∈𝓐。每个 S_n 都是有限柱乘子，精确公式为

$$
S_n=-2\sum_i\beta_iY_i+
4\sum_{i,j}u_{ij}Y_iY_j,\qquad
Y_i=N_i(I+N_i)^{-1},
\tag{B3}
$$

其中 u_{ij} 是 (B1) 的系数，β_i 为该块相应行和或列和。因此每个 S_n 来自一个真正有理解析芽。

固定 ζ 的阶2^m。凡块的全部位都≥m，其 S_n 被 γ_ζ 固定。因为块位互不相交，最多 m 个块与前 m 位相交；这些块各自有限。因此

$$
\gamma_\zeta(S)-S
=\sum_{\substack{n:\ (I_n\cup J_n)\cap[0,m)\ne\varnothing}}
\bigl(\gamma_\zeta(S_n)-S_n\bigr)
\tag{B4}
$$

是**有限个真正解析芽的和**。这里没有把按块绝对收敛误写成按全部二阶系数绝对收敛。

由 f≠0 得 S≠0，且 c₀(S)=0，所以 S 非标量。定理4.2直接给

$$
\boxed{\ker S=0,\qquad\overline{\operatorname{Ran}S}=H,
\qquad f=S1\text{ 对 }A\text{ 循环}.}
\tag{B5}
$$

因此 R112 的方法边界例子并非本题的非循环向量。其仍然有效的两条结论是：

- S 的唯一归一化幂系数不在ℓ¹，故不能归入绝对可和归一化幂表示；
- 在 R112 递归远移块的位置选择下，对任意真正解析头 F 及任意 s>1，
  liminf_N −log∥(S−F(A))^N∥/N^s=0。

(B5) 与这两点同时成立：gauge 论证提供了这些幂型判据之外的真实排核机制。R112 原稿末节的任意 H 核“尚未判定”状态已由本节解决；本稿不改动该冻结历史稿。

## 8. 仍然未解决的范围

- 一般无界第一 chaos（a∈ℓ²而不在ℓ¹）尚未从本稿推出循环；
- 一般有界有限 chaos，若其低位参与无限多个非零高位单项式，其 gauge 差不一定为有限解析和，仍需新论证；
- 任意 X∈𝓐 的所有非零核、任意 L² 端点以及 A 的完整普通不变格均未解决；
- 完整 Hilbert ISP 的完成标准没有改变。

本文没有把已知稠密循环类取极限，也没有从纯模型核角度转移；决定性额外结构是实际有限 dyadic gauge 差、在每个闭不变限制中稠密的 A 幂值域，以及跨核的 B 对称配对。

依赖：R9/R13 的实际模型，R23 的强单位近似（§2已重证），
R24 的 B 对称性（§1已推广性重证），R32 的形式系数，R88 的第一 chaos 乘子，以及 R92/R112 的 Hadamard 块乘子界。
