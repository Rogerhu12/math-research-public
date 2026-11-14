# R78：任意有限模式多项式的全矩分离

日期：2026-11-12（UTC）。经主会话逐段核验。

**状态：主定理已证明。** 两个端点可以分别由任意有限多个平方可和复 Rademacher 级数构成，取任意次数多项式，并允许任意有限前缀柱函数作为系数。两个端点的模式、维数和高位方向均可完全不同。任意非零两端都不可能对实际算子 $A$ 全部矩消失；通常复 Hilbert 内积版本也成立。

证明按两端总次数归纳，归纳范围同时包括所有有限模式维数和所有有限前缀。先商去共同的无效平移方向。对于每个有效单位方向，取两端沿该方向的最高导数；它们的配对已由低总次数归纳分离。使用恰好相应数量的不同高位，将这个非零导数配对变成联合首项。单位球紧性给有限种测试，再由统一尾计数迫使有效系数绝对可和，与 R40 矛盾。

关键是使用多个高位对应的乘积 $\prod(2N_j-I)$，而不是只使用一个高位的翻译残差。相对误差在每个因子中先提出该位系数的模，最后保留完整的 $\prod_j\|a_j\|$ 因子。此前单个位的多变量曲率障碍和抽象单曲线反例因此不适用。

依赖：R9/R12 的高位矩阵单位近似；R11 的有限柱循环性；R24 的复双线性形式；R40 的连续对矩分离。稳定尾空间评价引理已在 R63 证明，本稿为完整性重写；多位翻译公式与 R76 一致，也在本稿重写。主证明不依赖 R76 的二元零线分类。

## 1. 完整定理

设

$$
B(u,v)=\int u(y)v(-1-y)\,d\mu(y),\qquad
\chi_j(y)=(-1)^{b_j(y)}.
$$

取任意有限维复 Rademacher 模式

$$
X=x_*+\sum_{j\ge0}a_j\chi_j\in\mathbb C^s,\qquad
Y=y_*+\sum_{j\ge0}b_j\chi_j\in\mathbb C^t,
\tag{1.1}
$$

满足

$$
\sum_j\|a_j\|^2+\sum_j\|b_j\|^2<\infty.
\tag{1.2}
$$

设 $\mathscr C_M$ 为低 $M$ 位柱函数空间，取

$$
F\in\mathscr C_M[x_1,\ldots,x_s],\qquad
G\in\mathscr C_M[y_1,\ldots,y_t].
\tag{1.3}
$$

令 $f=F(X)$、$g=G(Y)$。有限阶 Rademacher 矩估计保证这些向量及其全部形式导数代入均在 $L^2$ 中。

**定理 1.1。**

$$
B(A^nf,g)=0\quad(n\ge0)
\quad\Longrightarrow\quad f=0\ \text{或}\ g=0.
\tag{1.4}
$$

同样，

$$
\langle A^nf,g\rangle=0\quad(n\ge0)
\quad\Longrightarrow\quad f=0\ \text{或}\ g=0.
\tag{1.5}
$$

为证明 (1.4)，把 $(X,Y)$ 拼接成一个共同有限维模式 $Z$，并把 $F,G$ 看作共同变量中的多项式即可。因此主证明只处理

$$
Z=z_*+\sum_j c_j\chi_j\in V,\qquad
f=F(Z),\quad g=G(Z),
\tag{1.6}
$$

其中 $V$ 是任意有限维复向量空间。两端不必实际使用全部共同变量。

该向量类对反射共轭 $Ch(y)=\overline{h(-1-y)}$ 保持不变：$Cg$ 的柱系数仍是有限柱，模式系数变为 $-\overline b_j$，仍平方可和。由于

$$
\langle A^nf,g\rangle=B(A^nf,Cg),
$$

(1.5) 由 (1.4) 直接得到。这一步允许扩大共同模式维数，所以没有 R72/R76 限定共同二维时的复共轭范围问题。

## 2. 稳定尾空间中的评价忠实性

以下归纳始终同时涵盖任意有限维数、任意前缀长度。所有线性坐标变换、有限前缀加长及仿射限制均不增加形式总次数。

把模式的低位部分和常数项吸收进柱系数，写成

$$
Z=\sum_{j\ge M}c_j\chi_j.
$$

子空间

$$
W_m=\operatorname{span}_{\mathbb C}\{c_j:j\ge m\}
$$

下降且有限维，所以加长前缀后可假定 $W_m=W$ 对全部 $m\ge M$ 成立。把每个前缀上的多项式限制到实际的仿射尾空间，再使用 $W$ 的线性坐标。于是可假定

$$
Z=\sum_{j\ge M}c_j\chi_j\in W,\qquad
\operatorname{span}\{c_j:j\ge m\}=W
\quad(m\ge M).
\tag{2.1}
$$

**引理 2.1。** 尾级数 $Z$ 的分布在 $W$ 上 Zariski 稠密。因此

$$
P(Z)=0\text{ 几乎处处},\quad P\in\mathbb C[W]
\quad\Longrightarrow\quad P=0.
\tag{2.2}
$$

**证明。** 反设 $P$ 的非零最高齐次部分次数为 $d\ge1$，将其写成 $T(w,\ldots,w)$，$T$ 为对称 $d$ 线性型。对任意不同的 $j_1,\ldots,j_d$，条件于其余位，并将这 $d$ 位的全部符号赋值等式乘以符号乘积后求和。低次数项消失，得到

$$
T(c_{j_1},\ldots,c_{j_d})=0.
\tag{2.3}
$$

由每个尾仍张成 $W$，任意给定的 $w_1,\ldots,w_d\in W$ 可以分别写成互不相交有限高位块中系数向量的线性组合。将 (2.3) 多线性展开，得 $T(w_1,\ldots,w_d)=0$，与最高齐次部分非零矛盾。非零常数情形显然不可能。证毕。

对有限柱系数多项式，在每个前缀分量上应用此引理，得到评价忠实性：

$$
F(Z)=0
\quad\Longleftrightarrow\quad
F=0\text{ 作为 }\mathscr C_M[W]\text{ 中的形式多项式}.
\tag{2.4}
$$

尤其任何形式非零的最高方向导数，代入后仍是非零 $L^2$ 向量。这里不把一般多变量整函数的零集问题与多项式评价混同。

## 3. 共同平移稳定子的商

在 (2.1) 的坐标中，定义共同平移稳定子

$$
K=\{u\in W:D_uF=0\ \text{且}\ D_uG=0\}.
\tag{3.1}
$$

所有等式均是柱系数形式多项式等式。$K$ 是复线性子空间。对 $u\in K$，形式 Taylor 展开给

$$
F(z+\lambda u)=F(z),\qquad
G(z+\lambda u)=G(z)
\quad(\lambda\in\mathbb C).
$$

所以两多项式下降到商空间

$$
V=W/K.
$$

选择 $V$ 的任意 Hermitian 范数，将共同模式替换为商模式

$$
\widehat Z=\pi Z=\sum_{j\ge M}\widehat c_j\chi_j,\qquad
\widehat c_j=\pi c_j.
\tag{3.2}
$$

每个尾的像仍张成 $V$，所以引理 2.1 仍适用，评价仍忠实。多项式次数不增加。

如果 $V=\{0\}$，两端都是有限柱，R11 已排除非零零矩配对。因此只需考虑 $\dim V\ge1$。此后为简化符号，把商后的模式和系数仍记为 $Z,c_j$，把下降后的多项式仍记为 $F,G$。此时

$$
u\ne0
\quad\Longrightarrow\quad
D_uF\ne0\ \text{或}\ D_uG\ne0.
\tag{3.3}
$$

后面只需证明商后的有效系数绝对可和。原来被 $K$ 消去的系数可以不可和，但它们不影响 $f,g$。

## 4. 对所有有限维数统一作总次数归纳

按

$$
N=\deg F+\deg G
$$

归纳，命题同时量化所有有限模式维数、所有前缀长度和所有平方可和系数列。若某端次数为零，则该非零端是有限柱，R11 及 $B$-对称性直接排除任意非零另一端；特别地给出归纳基例。

假设结论对总次数小于 $N$ 的所有此类向量成立，反设当前 $f,g$ 非零且全部矩消失。完成 §2–§3 的预处理。若限制或商操作降低总次数，则低次数归纳已经给出矛盾；否则仍记总次数为 $N$，且共同有效空间 $V$ 满足 (3.3)。

取任意单位向量 $u\in V$。定义

$$
p_u=\max\{k:D_u^kF\ne0\},\qquad
q_u=\max\{k:D_u^kG\ne0\}.
\tag{4.1}
$$

$D_u^0F=F$，所以这些整数存在且非负。由 (3.3)，

$$
k_u:=p_u+q_u\ge1,\qquad k_u\le N.
\tag{4.2}
$$

由评价忠实性，

$$
f_u=(D_u^{p_u}F)(Z)\ne0,\qquad
g_u=(D_u^{q_u}G)(Z)\ne0.
\tag{4.3}
$$

两端总次数至多 $N-k_u<N$。归纳假设给某个矩指标 $n_u\ge0$，使

$$
B(A^{n_u}f_u,g_u)\ne0.
\tag{4.4}
$$

令

$$
\xi=F\otimes G,\qquad
L_u=D_u^{(1)}+D_u^{(2)},
$$

其中两个方向导数作用于不同张量因子。二项式展开中，若 $i>p_u$，第一端导数为零；若 $i<p_u$，则 $k_u-i>q_u$，第二端导数为零。因此只有一个纯张量存活：

$$
L_u^{k_u}\xi
={k_u\choose p_u}
(D_u^{p_u}F)\otimes(D_u^{q_u}G).
\tag{4.5}
$$

把

$$
\mathcal M_n(P\otimes Q)=B(A^nP(Z),Q(Z))
$$

记为固定有限导数张量空间上的线性泛函，便有

$$
\mathcal M_{n_u}(L_u^{k_u}\xi)\ne0.
\tag{4.6}
$$

这不是假定任意曲线张成空间自动包含低次纯张量；这里的唯一存活项来自两个端点各自沿同一固定方向的最高导数阶，公式 (4.5) 是精确二项式恒等式。

## 5. 单位球的有限覆盖，保留每片的联合首项

对固定 $u$，考虑 $k_u$ 个彼此独立方向变量上的连续多项式

$$
\Phi_u(v_1,\ldots,v_{k_u})
=\mathcal M_{n_u}
\left(L_{v_1}\cdots L_{v_{k_u}}\xi\right).
\tag{5.1}
$$

其在 $(u,\ldots,u)$ 处不为零。故存在单位球面上的邻域 $\mathcal U_u$ 和 $c_u>0$，使

$$
|\Phi_u(v_1,\ldots,v_{k_u})|
\ge3c_u
\quad\text{只要 }v_1,\ldots,v_{k_u}\in\mathcal U_u.
\tag{5.2}
$$

单位球面有限维且紧。取有限子覆盖

$$
\mathcal U_1,\ldots,\mathcal U_L,
$$

每片对应固定整数与常数

$$
1\le k_\ell\le N,\qquad n_\ell\ge0,\qquad c_\ell>0.
\tag{5.3}
$$

于是 (5.2) 对每片及该片内任意 $k_\ell$ 个方向成立。不同方向可以随高位任意变化；本步骤没有把它们固定为相同方向。

有限维性在这里以紧单位球的形式出现。一般无限秩有限 chaos 不自动具有此性质，不能直接照搬本节。

## 6. 多位翻译公式及逐因子的相对误差

### 6.1 精确公式

实际算子权记为

$$
\alpha_j=a_j^{\mathrm{op}}=e^{-L_j},\qquad
\eta_j=\frac{\alpha_{j+1}}{\alpha_j},
$$

并使用

$$
N_j=\frac{A^{2^j}}{W_{2^j}},\qquad
\|N_j-E_j\|=\eta_j,\qquad E_j=e_{10}.
\tag{6.1}
$$

对不同高位 $j$，$E_j$ 作用于不同位；$N_j$ 都是 $A$ 的幂的标量倍。设

$$
U_j=D_{c_j}^{(1)},\qquad V_j=D_{c_j}^{(2)},\qquad
\mathcal H_j=e^{U_j+V_j}
\bigl(\cosh(U_j-V_j)\bigr)^{-1}.
\tag{6.2}
$$

方向导数矩阵作用在由 $F,G$ 全部偏导生成的固定有限维张量空间中，彼此交换且幂零；$\mathcal H_j$ 是幺幂矩阵。双曲余弦的逆矩阵存在。

若有界算子 $T$ 不作用于有限位集 $J$ 中的任何位，则精确地

$$
B\left(\prod_{j\in J}(2E_j-I)\,Tf,g\right)
=\mathcal M_T
\left[\prod_{j\in J}(\mathcal H_j-I)\xi\right].
\tag{6.3}
$$

证明与 R76 相同：去掉这些位后的双线性积分为 $\Lambda$；每个恒等因子贡献 $\cosh(U_j-V_j)$，$2E_j$ 贡献 $e^{U_j+V_j}$，所以 $2E_j-I$ 贡献二者之差。相乘并消去可逆双曲余弦即得 (6.3)。本公式适用于有限前缀系数，只需 $J$ 高于该前缀并且 $T$ 不作用于 $J$。

### 6.2 必须逐因子提出系数模长

对 $c_j\ne0$，写

$$
\rho_j=\|c_j\|,\qquad v_j=c_j/\rho_j.
$$

定义

$$
\widehat{\mathcal H}(\rho,v)=
\begin{cases}
\displaystyle
\frac{
e^{\rho(D_v^{(1)}+D_v^{(2)})}
[\cosh(\rho(D_v^{(1)}-D_v^{(2)}))]^{-1}-I
}{\rho},&\rho\ne0,\\[6pt]
L_v,&\rho=0.
\end{cases}
\tag{6.4}
$$

由于形式导数幂零，分子是有限矩阵多项式且常数项为零；所以 (6.4) 在 $\rho=0$ 正则。对所有单位 $v$ 及 $0\le\rho\le\rho_0$，存在统一常数 $C$，使

$$
\|\widehat{\mathcal H}(\rho,v)-L_v\|\le C\rho,\qquad
\|\widehat{\mathcal H}(\rho,v)\|+\|L_v\|\le C.
\tag{6.5}
$$

特别地，若 $J=\{j_1,\ldots,j_k\}$，则

$$
\prod_{i=1}^k(\mathcal H_{j_i}-I)
=\left(\prod_{i=1}^k\rho_{j_i}\right)
\prod_{i=1}^k\widehat{\mathcal H}(\rho_{j_i},v_{j_i}),
\tag{6.6}
$$

并由乘积差的逐项展开得到

$$
\left\|
\prod_{i=1}^k\widehat{\mathcal H}(\rho_{j_i},v_{j_i})
-\prod_{i=1}^kL_{v_{j_i}}
\right\|
\le C_k\sum_{i=1}^k\rho_{j_i}.
\tag{6.7}
$$

因此未归一化乘积的误差是

$$
O\left[
\left(\prod_{i=1}^k\rho_{j_i}\right)
\sum_{i=1}^k\rho_{j_i}
\right].
\tag{6.8}
$$

这里的 $\prod_i\rho_{j_i}$ 完整保留；不能把它丢掉而只写绝对 $O(\max_i\rho_{j_i})$。

### 6.3 在同一覆盖片内获得模长下界

令 $A_m$ 是低 $m$ 位有限链，则

$$
\|A^n-A_m^n\|\le n\alpha_m.
\tag{6.9}
$$

在固定有限导数张量空间上，

$$
\|\mathcal M_{A_m^n}-\mathcal M_n\|
\le C_n\alpha_m.
\tag{6.10}
$$

取覆盖片 $\ell$，并选 $k=k_\ell$ 个不同的 $j_i\ge m$，其方向均在 $\mathcal U_\ell$ 中。$A_m$ 不作用于这些位。由 (6.3)、(6.6)，除以正数 $\prod_i\rho_{j_i}$ 后，左端精确等于

$$
\mathcal M_{A_m^{n_\ell}}
\left[
\prod_{i=1}^{k_\ell}
\widehat{\mathcal H}(\rho_{j_i},v_{j_i})\xi
\right].
\tag{6.11}
$$

由 (6.7)、(6.10)，它与

$$
\mathcal M_{n_\ell}
\left(L_{v_{j_1}}\cdots L_{v_{j_{k_\ell}}}\xi\right)
$$

的差至多

$$
C_\ell\left(\alpha_m+\sum_i\rho_{j_i}\right).
\tag{6.12}
$$

因为 $\rho_j\to0$，并且覆盖片只有有限个，可以选择共同阈值 $m_0$，使 (6.12) 对所有 $m\ge m_0$、所有相关高位元组均不超过 $c_\ell$。由 (5.2)，得到

$$
\boxed{
\left|
B\left(
\prod_{i=1}^{k_\ell}(2E_{j_i}-I)
A_m^{n_\ell}f,g
\right)
\right|
\ge c_\ell\prod_{i=1}^{k_\ell}\rho_{j_i}.}
\tag{6.13}
$$

该下界允许各 $\rho_{j_i}$ 差异任意大，也允许各方向在覆盖片中任意变化。

## 7. 实际归一化幂给统一尾上界

全部矩消失且 $N_j$ 是 $A$ 的幂，故

$$
B\left(
\prod_{i=1}^{k_\ell}(2N_{j_i}-I)
A^{n_\ell}f,g
\right)=0.
\tag{7.1}
$$

由 $\|2N_j-I\|,\|2E_j-I\|\le3$，

$$
\left\|
\prod_{i=1}^{k_\ell}(2N_{j_i}-I)
-\prod_{i=1}^{k_\ell}(2E_{j_i}-I)
\right\|
\le2\,3^{k_\ell-1}\sum_i\eta_{j_i}.
\tag{7.2}
$$

结合 (6.9)，对全部 $j_i\ge m$ 有

$$
\left|
B\left(
\prod_{i=1}^{k_\ell}(2E_{j_i}-I)
A_m^{n_\ell}f,g
\right)
\right|
\le C_\ell'\left(\alpha_m+\sum_i\eta_{j_i}\right)
\le C_\ell''\alpha_m.
\tag{7.3}
$$

最后一步使用实际 $\eta_j$ 递减且 $\eta_m=o(\alpha_m)$。常数只依赖固定端点、覆盖片、测试阶数，不随 $m$ 或高位元组变化。

将 (7.3) 与 (6.13) 合并，

$$
\boxed{
\prod_{i=1}^{k_\ell}\rho_{j_i}\le C_\ell'''\alpha_m
\quad
\left(
j_i\ge m,\ j_i\text{ 不同},\ v_{j_i}\in\mathcal U_\ell
\right).}
\tag{7.4}
$$

这里全部被测试位均随尾起点 $m$ 移动；没有留下固定锚位误差。对于 $n_\ell=0$，$A_m^0=I$，同一估计当然成立。

## 8. 有限覆盖的尾计数迫使有效系数绝对可和

为每个 $c_j\ne0$ 选择一个包含 $v_j$ 的覆盖片，形成有限划分。对片 $\ell$，若尾 $j\ge m$ 中有 $k_\ell$ 个系数同时满足

$$
\rho_j>(C_\ell'''\alpha_m)^{1/k_\ell},
$$

它们的乘积违背 (7.4)。故该片尾部超过此阈值的项至多 $k_\ell-1$。

因为 $1\le k_\ell\le N$、$\alpha_m\le1$，存在共同常数 $C_0$，使各片阈值均不超过

$$
T_m=C_0\alpha_m^{1/N}.
\tag{8.1}
$$

令

$$
K_0=\sum_{\ell=1}^L(k_\ell-1).
$$

于是整个尾中超过 $T_m$ 的有效系数范数至多 $K_0$ 项。将全部 $\rho_j$ 非增重排为 $\rho_1^*,\rho_2^*,\ldots$，头部 $j<m$ 至多 $m$ 项，所以

$$
\rho_{m+K_0+1}^*\le C_0\alpha_m^{1/N}
\quad(m\ge m_0).
\tag{8.2}
$$

也即对全部充分大 $n$，

$$
\rho_n^*
\le C_0\alpha_{n-K_0-1}^{1/N}
\le C_0\alpha_{\lfloor n/2\rfloor}^{1/N}.
\tag{8.3}
$$

实际权满足 $\sum_m\alpha_m^\gamma<\infty$ 对每个 $\gamma>0$ 成立。因此

$$
\sum_j\|c_j\|^s<\infty
\quad\text{对每个 }s>0,
\qquad\text{特别地}\qquad
\sum_j\|c_j\|<\infty.
\tag{8.4}
$$

这是商后的有效系数列。相应模式绝对一致收敛，故有连续代表。有限前缀柱系数连续，因此 $f,g$ 也连续。

R40 的连续对矩分离与非零零矩反设矛盾。总次数归纳完成，定理 1.1 得证。

## 9. 对此前障碍的准确回应

单高位公式给

$$
\mathcal H_j-I=L_{c_j}+\text{二阶及更高阶项}.
$$

如果只用这一个残差，在多个变化方向下，二阶项可能被方向的二阶变化吸收；此前有限前缀曲率反例已经说明，不能直接宣称所有混合二阶矩都独立于全部一阶矩。

本证明使用 $k$ 个不同高位的乘积。每个因子都减去了恒等项，因此每个被选位至少贡献一次方向导数。逐因子提出 $\rho_j$ 后，联合首项是

$$
L_{v_1}\cdots L_{v_k}\xi.
$$

沿一个方向取各端最高导数阶，使对角联合首项由 (4.5) 精确等于一个低总次数非零纯张量。低次数归纳保证其某个实际矩非零，再用联合连续性扩展到独立方向邻域。方向的高阶横向变化只进入 (6.8) 的相对小余项，无法取消已经有统一正下界的联合首项。

抽象单曲线反例只让某一条曲线上的单个 $\mathcal H$ 作用落入核；它没有给出所有不同高位乘积的约束。实际 $N_j$ 均为同一 $A$ 的幂，确保了本证明需要的全部乘积零矩 (7.1)。因此该反例没有否定本定理。

## 10. 尚未覆盖的真正无限秩问题

本定理取消了此前有限方向、共同二维、固定代数曲线以及平方根可和横向误差等限制，覆盖任意有限多个 Rademacher 模式的多项式配对，并允许两端模式完全不同。

一般有限 Walsh chaos 未必能用有限多个第一 chaos 模式和有限前缀多项式表示。例如二阶 Walsh 系数可以具有无限秩，归一化的行方向可能包含正交列。此时导数生成空间不再有限维，其单位方向集合不紧；§5 无法自动抽取有限覆盖，测试矩指标和下界也可能随移动方向失控。

因此，本定理没有仅凭稠密性扩展到全部有限 chaos，更没有扩展到任意 $L^2$。下一缺口明确是：能否替代 §5 的紧性，以定量方式控制无限多个有效行方向，而同时保留 §6 的逐因子相对误差及 §8 的全尾计数。
