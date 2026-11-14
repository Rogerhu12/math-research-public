# R252. 完整物理角测试的 DN 边界、全 Jacobian 与有限投影缺项

2026-11-14，geometry，AI 辅助。

**状态：已证明的条件性有限维公式与一致性定理；尚未实施或数值验证的新测试方式。** 本文定义一个保留全部 $M$ 个物理角非均值测试的 DN 边界，给出其物理状态、完整核心、scalar 参数的导数，以及它和当前材料角测试之间的精确差恒等式。两种测试在有限截断下一般不同。本文不宣称新方法可解、条件数改善、原边界容差已经满足，也不替代真实全角接缝或整面度量检查。

当前源码采用 $M=T=112$、完整物理状态维数 $3M+2$、三个上游 scalar 控制。本文不改变这些场、尾部或标量函数的定义，仅推导一个尚未采用的边界测试备选。是否采用，应由原投影和完整边界线性化的实际诊断决定。

## 1. 坐标、符号和原边界的准确对象

记 $\omega_j=2j$、$b_j=1-\omega_j^2$，并用**全部**核心系数定义

$$
\Phi_c(\varphi)=\varphi+\sum_{j=1}^{M}\frac{b_j}{\omega_j}c_j\sin(\omega_j\varphi),\qquad
\rho_c(\varphi)=\Phi_c'(\varphi)=1+\sum_{j=1}^{M}b_jc_j\cos(\omega_j\varphi).
\tag{252.1}
$$

假设全角 $\rho_c>0$，记逆映射 $\psi_c=\Phi_c^{-1}$。这正是 [R240](R240-canonical-material-metric-and-refinement.md) 的固定原点材料角 $\theta=\Phi_c(\varphi)$。映射奇对称，且与平移 $\pi$ 交换，所以偶、$\pi$ 周期函数在换角后仍属于同一对称类。下文只在这一类中使用全部 cosine 模；没有把可能存在的非对称场直接删成 cosine 场。

切口处完整物理状态为

$$
y=(r_0,\ldots,r_M,t_1,\ldots,t_M,z_0,\ldots,z_M),\qquad n=3M+2.
$$

写

$$
z(\varphi)=z_0+\sum_{j=1}^{M}z_j\cos(\omega_j\varphi),\qquad
v(\varphi)=v_0+\sum_{j=1}^{M}v_j\cos(\omega_j\varphi),\qquad
(v_0,v_+) = Z f(s_*,y,p).
\tag{252.2}
$$

这里 $f$ 是原完整有限 Frenet RHS；$Z$ 取全部 $M+1$ 个高度行，$Z_+$ 只取高度的 $1,\ldots,M$ 行。因此 $z_+=Z_+y$、$v_+=Z_+f$。$v$ 是该有限 RHS 的真实物理 $s$ 导数，不是由新边界另行构造的斜率。核心在 $s$ 上为常数，故固定材料角与固定物理角的 $\partial_s$ 在换角后相容；若改成 $c=c(s)$，本文公式不能直接沿用。

高度符号与径向符号分别记 $e_h,e_r\in\{-1,1\}$。固定切口 $E_*>0$ 给出

$$
a_s(s_*)=\frac{e_r}{\sqrt{E_*}},\qquad
\gamma:=\mathrm{cut\_scale}=\frac{e_he_r}{\sqrt{E_*}}.
\tag{252.3}
$$

现有上半片采用 $e_h=e_r=-1$，故 $\gamma>0$；native 非均值切口高度仍须乘 $e_h$。不能因为 $\gamma$ 为正就漏掉高度输入中的负号。

在一个实际有效的尾部解分支上，设完整有限 native DN 映射为

$$
D:\mathcal U\subset\mathbb R^M\longrightarrow\mathbb R^M,
\qquad d=D(H),\qquad J=D'(H).
\tag{252.4}
$$

$d$ 的所有 $M$ 行是 native 的非均值 $\partial_r$ 高度系数，$J$ 是对所有 $M$ 个 native 高度输入的完整 Jacobian。另记该同一尾解的物理径向均值为 $\beta(H)$，即 `jets.meanSlope`。本文要求 $D$ 在所用分支上可微；原真实尾求解或其明确标注的仿射内层映射必须提供这些对象。不得换成主符号、低模块、WKB 斜率或从均值猜出的 DN。

这些定义对应现有源码的 [`MaterialTrace` 和 `FullDNBoundary`](../computations/geometry_20261114_full_dn_boundary.py)、[`AugmentedFlow` 和 `SeparatedBoundary`](../computations/geometry_20261114_full_dn_augmented.py) 以及 [`AffineTail`、`true_height`、`final_height_seam`](../computations/geometry_20261114_full_dn_solve.py)。尤其是 current `cut_scale` 与 (252.3) 一致。

## 2. 两个方向的投影，以及新的完整测试

为清楚区分函数与系数，定义

$$
U_cf=f\circ\psi_c,\qquad V_cg=g\circ\Phi_c,
$$

以及非均值 cosine 合成 $\mathcal C_\varphi u=\sum_{j=1}^M u_j\cos(\omega_j\varphi)$，材料角合成 $\mathcal C_\theta$ 同理。连续非均值系数算子是

$$
(Q_\theta g)_k=\frac1\pi\int_0^{2\pi}g(\theta)\cos(\omega_k\theta)\,d\theta,
\qquad
(Q_\varphi f)_i=\frac1\pi\int_0^{2\pi}f(\varphi)\cos(\omega_i\varphi)\,d\varphi.
\tag{252.5}
$$

定义完整方块

$$
\begin{aligned}
P(c)&=Q_\theta U_c\mathcal C_\varphi,&
P_{kj}&=\frac1\pi\int\cos(\omega_k\theta)\cos(\omega_j\psi_c(\theta))\,d\theta,\\
S(c)&=Q_\varphi V_c\mathcal C_\theta,&
S_{ik}&=\frac1\pi\int\cos(\omega_i\varphi)\cos(\omega_k\Phi_c(\varphi))\,d\varphi.
\end{aligned}
\tag{252.6}
$$

原实现的 `trace.projection` 有 $M+1$ 列，第一列被明确设为零；本文 $P$ 是其后面的完整 $M\times M$ 非均值块。这样写不丢高度均值：常数高度在任一角度下仍是常数，对非均值测试严格没有贡献。

原、备选边界都使用**同一个** native 高度输入

$$
H=e_hP(c)z_+.
\tag{252.7}
$$

备选边界的定义是

$$
\boxed{R_\varphi(c,y,p)=v_+-\gamma S(c)D\bigl(e_hP(c)z_+\bigr).}
\tag{252.8}
$$

这是把真实有限材料角尾斜率先按 $\theta=\Phi_c(\varphi)$ 拉回，再对**全部** $1,\ldots,M$ 个物理角 cosine 投影。更具体地，令

$$
w_\varphi(\varphi)=v(\varphi)-\gamma\left[\beta(H)+\sum_{k=1}^M d_k\cos(\omega_k\Phi_c(\varphi))\right].
\tag{252.9}
$$

由于常数项对非均值 cosine 正交，且 $v$ 本来就在物理角的完整有限空间中，$Q_\varphi w_\varphi=R_\varphi$。这证明 (252.8) 是明确的 $L^2(d\varphi)$ Galerkin 测试。它没有忽略 native 斜率均值对完整函数的贡献；该贡献恰好不会进入这些非均值行，均值另见 §6。

换元也给出

$$
P_{ki}=\frac1\pi\int_0^{2\pi}
\rho_c(\varphi)\cos(\omega_i\varphi)\cos(\omega_k\Phi_c(\varphi))\,d\varphi.
\tag{252.10}
$$

因此通常 $S\ne P^{\mathsf T}$，更不能令 $S=P^{-1}$。把 $\rho_c$ 加到新测试的积分权中会变成另一个测试，不能与 (252.8) 混用。[R250](R250-material-angle-square-projection-invertibility.md) 在连续积分下分别适用于 $P$、$S$ 的单调换角，给出各自可逆性，但没有给出条件数界或 $SP\approx I$。

## 3. 原有限角规则下的明确版本

原材料角规则在固定均匀节点 $\theta_a=2\pi a/N_\theta$ 上使用精确算术解释的

$$
P^{N_\theta}_{kj}=
\frac2{N_\theta}\sum_{a=0}^{N_\theta-1}
\cos(\omega_k\theta_a)\cos(\omega_j\psi_c(\theta_a)).
\tag{252.11}
$$

独立固定均匀物理角节点 $\varphi_b=2\pi b/N_\varphi$ 给出备选

$$
S^{N_\varphi}_{ik}=
\frac2{N_\varphi}\sum_{b=0}^{N_\varphi-1}
\cos(\omega_i\varphi_b)\cos(\omega_k\Phi_c(\varphi_b)).
\tag{252.12}
$$

要求两个节点数均为偶数且大于 $4M$。于是常数列严格为零，物理有限三角多项式 $v$ 的前 $M$ 个系数由该物理网格精确恢复；实现可直接取 $v_+$，避免重复投影舍入。这个节点数条件**不**保证复合函数的 Fourier 尾为零，也不保证上述有限求和已经足够接近积分。

用 $P^{N_\theta},S^{N_\varphi}$ 代入 (252.7)–(252.8)，就是一个完全指定的有限新边界。原材料角高度输入、native 尾模数以及全部尾响应仍保留。$N_\theta$ 和 $N_\varphi$ 是边界求积参数，与物理 ODE 自身的角网格分开记录；不能只因后者为 2048 就宣称前两者的非线性复合求积没有误差。

§4、§5 的矩阵和微分公式对连续积分、或固定节点有限和分别成立。有限和中的逆映射必须按同一个数学逆函数解释；当前 `material_angles` 是有容差的 Newton/二分求逆，实际逆角误差、舍入误差和有限求积误差都属于数值实现误差。特别地，本文的隐函数导数不是“对停止在某一次迭代的程序分支求导”的恒等式。

## 4. 核心、物理状态和 scalar 的完整 Jacobian

### 4.1 两个投影的所有核心导数

记

$$
A_j(\varphi)=\frac{b_j}{\omega_j}\sin(\omega_j\varphi).
$$

由 $\Phi_c(\psi_c(\theta))=\theta$ 得

$$
\partial_{c_j}\Phi_c=A_j,
\qquad
\partial_{c_j}\psi_c(\theta)
=-\frac{A_j(\psi_c(\theta))}{\rho_c(\psi_c(\theta))}.
\tag{252.13}
$$

积分区间紧且 $\rho_c$ 有严格正下界；在当前核心的充分小邻域内仍有一致正下界，故可逐项微分。写 $P_j=\partial_{c_j}P$、$S_j=\partial_{c_j}S$，得到

$$
\begin{aligned}
(P_j)_{ki}
&=\frac1\pi\int
\cos(\omega_k\theta)\,
\frac{\omega_i\sin(\omega_i\psi_c(\theta))A_j(\psi_c(\theta))}
{\rho_c(\psi_c(\theta))}\,d\theta,\\
(S_j)_{ik}
&=-\frac{\omega_k}{\pi}\int
\cos(\omega_i\varphi)\sin(\omega_k\Phi_c(\varphi))A_j(\varphi)\,d\varphi.
\end{aligned}
\tag{252.14}
$$

固定节点有限和只需把积分替换成同一规则的求和。$S_j$ 使用固定物理节点，因此没有逆映射因子 $1/\rho$，也没有额外权重导数。$P_jz_+$ 正是原 `MaterialTrace.height_core_jacobian` 的对应列；高度常数列及其核心导数均严格为零。

### 4.2 新右边界的导数

原局部 RHS 在把 $y,c,p$ 当独立未知量时为 $f(s_*,y,p)$：完整核心常数列只控制材料换角及 inlet 识别，不显式进入该局部 RHS。记原真实局部 Jacobian 为

$$f_y=\partial_yf(s_*,y,p),\qquad f_p=\partial_pf(s_*,y,p).$$

固定切口、固定尾公式和固定方向符号下，直接微分 (252.8) 得

$$
\delta H=e_h\left[PZ_+\delta y+\sum_{j=1}^M(P_jz_+)\delta c_j\right],
$$

$$
\delta R_\varphi
=Z_+(f_y\delta y+f_p\delta p)
-\gamma\sum_{j=1}^M(S_jd)\delta c_j
-\gamma S J\,\delta H.
\tag{252.15}
$$

所以完整三个块为

$$
\boxed{\begin{aligned}
J_y^\varphi
&=Z_+f_y-\gamma e_hSJPZ_+,\\
(J_c^\varphi)_{\cdot j}
&=-\gamma\left[S_jd+e_hSJ(P_jz_+)\right],\qquad 1\le j\le M,\\
J_p^\varphi
&=Z_+f_p.
\end{aligned}}
\tag{252.16}
$$

这里 $J_y^\varphi$ 有全部 $n$ 个物理列，$J_c^\varphi$ 有全部 $M$ 个核心列，$J_p^\varphi$ 有全部 scalar 列。$S_jd$ 是不能遗漏的项；只替换原右边界数值而仍沿用原 Jacobian，会得到另一个线性化。

当前三个 bump 的完整 $0/1/2$ jet 在 $s_*$ 邻域恒为零，区间端点、$E_*$、方向和 native 尾配置也独立于 $p$，见 [`PrefixControlsProfile`](../computations/geometry_20261114_prefix_controls_profile.py) 与 [`CompleteProfile`](../computations/geometry_20261114_full_scalar_profile.py)。因此当前右端局部 $f_p(s_*,y,p)=0$，从而 (252.16) 的显式 $J_p^\varphi=0$。这不意味着全 BVP 的 scalar 响应为零：上游 $f_p$ 非零，参数改变末端 $y$，还经实际求解改变核心，全部影响由变分 ODE 和其它 Jacobian 块传递。不能删除这三列或三条常值状态。

若将来改变端点、切口 metric 或尾参数，这个零块便不再自动成立。一般一阶变分还应有 $-\delta\gamma\,Sd$、$-\gamma S\,D_{\rm explicit}\delta p$，以及移动端点和额外换角参数带来的链式项；它们在本文当前明确设置中为零，而非通用地可以省略。

### 4.3 完整非局部与分离增广边界

不增广时 $c=(y_a)_{r[1:M]}$。左条件仍为

$$
r_0(0)-1=0,\quad r_j(0)-c_j^{\rm target}=0\ (1\le j\le K),
\quad t_j(0)+\omega_jr_j(0)=0\ (1\le j\le M),
\quad z_j(0)=0\ (0\le j\le M).
\tag{252.17}
$$

左 Jacobian 的各行分别是 $e_{r_0}^{\mathsf T}$、$e_{r_j}^{\mathsf T}$、$e_{t_j}^{\mathsf T}+\omega_je_{r_j}^{\mathsf T}$、$e_{z_j}^{\mathsf T}$；对右端和 $p$ 的左块为零。右边对 $y_a$ 的非零列恰把 $J_c^\varphi$ 填到全部 $r_1,\ldots,r_M$ 列，对 $y_b$ 填 $J_y^\varphi$，对 $p$ 填 $J_p^\varphi$。这给出所有端点列，没有把固定低核心条件当作可以删去其链式导数的理由。

分离增广时使用 $(y,c,p)'=(f,0,0)$，左边在 (252.17) 后再加 $c_j-r_j(0)=0$，其导数为物理 $r_j$ 列 $-1$、增广 $c_j$ 列 $+1$；右边直接使用

$$[\,J_y^\varphi\quad J_c^\varphi\quad J_p^\varphi\,].\tag{252.18}$$

增广 ODE 的全部 Jacobian 为

$$
\begin{pmatrix}f_y&0&f_p\\0&0&0\\0&0&0\end{pmatrix}.
\tag{252.19}
$$

当 $M=T$ 时右边仍是 $M$ 行，故 [R240](R240-canonical-material-metric-and-refinement.md) 的配平仍为 scalar 数 $k=K$。当前 $M=112,K=3$ 的物理维数为 338，增广维数为 453，左/右行数为 341/112；冻结 scalar 后 $K=k=0$ 的相应维数为 450，左/右为 338/112。该计数不证明 Jacobian 满秩。

### 4.4 真实与仿射内层尾的区别

若内层使用 $D_*(H)=D(H_*)+J_*(H-H_*)$，则 (252.16) 对该仿射映射仍精确成立，只需用 $d=D_*(H)$、$J=J_*$。核心变化仍改变 $P,S$，两个核心链式项都必须保留。内层新残差为零，不代表真实非线性 $D$ 的新残差为零；最终须重新调用同一完整 native 尾并使用其实际 $d,J,\beta$。

## 5. 与当前材料角残差的精确有限投影差

原非均值残差是

$$R_\theta=Pv_+-\gamma d.\tag{252.20}$$

**定理 252-A。** 对任意同一输入下的矩阵 $P,S$、真实或明确仿射的同一个 $d$，都有

$$
\boxed{\begin{aligned}
R_\varphi-SR_\theta&=(I-SP)v_+,\\
R_\theta-PR_\varphi&=\gamma(PS-I)d.
\end{aligned}}
\tag{252.21}
$$

**证明。** 分别把 $R_\theta=Pv_+-\gamma d$ 和 $R_\varphi=v_+-\gamma Sd$ 代入左边，两个 $\gamma Sd$ 或两个 $Pv_+$ 直接相消，余项正是右边。证毕。

该定理是纯有限矩阵恒等式：连续积分、两套固定均匀求和，乃至给定的实际舍入矩阵，都服从其精确实数解释；实际浮点相减仍有运算舍入。它不需要 $P$、$S$ 可逆。

特别地，新边界恰为零时原边界仍为 $\gamma(PS-I)d$。因此，即使 [R250](R250-material-angle-square-projection-invertibility.md) 保证 $P$ 数学可逆，新的零点也一般不等于旧零点。真正等价的左预条件化应是 $P^{-1}R_\theta=v_+-\gamma P^{-1}d$；(252.8) 刻意使用实际拉回投影 $S$，不是这个逆矩阵。

### 5.1 缺项就是未保留的换角后谱，而非未处理的常数

令 $\Pi_\theta,\Pi_\varphi$ 为包含常数和 $1,\ldots,M$ 模的连续正交投影。由于 $V_cU_c=U_cV_c=I$，且非均值测试消去常数，

$$
\begin{aligned}
(I-SP)v_+
&=Q_\varphi V_c(I-\Pi_\theta)U_cv,\\
(PS-I)d
&=-Q_\theta U_c(I-\Pi_\varphi)V_c\mathcal C_\theta d.
\end{aligned}
\tag{252.22}
$$

**证明。** 例如 $Q_\varphi V_cU_cv=v_+$，而 $Q_\varphi V_c\Pi_\theta U_cv=SPv_+$，中间的常数被 $Q_\varphi$ 消去。第二式同理从 $Q_\theta U_cV_c\mathcal C_\theta d=d$ 减去 $Q_\theta U_c\Pi_\varphi V_c\mathcal C_\theta d=PSd$。证毕。

固定有限和也有同一形式：将 $Q,\Pi$ 全部换成各自有限采样的系数提取与常数加有限模重建，前提是使用精确逆映射且两个网格精确恢复原有限三角多项式。此时 $I-\Pi_N$ 同时包含截断和求积 alias，不能称作单纯连续 Fourier 高模。若逆角有误差，(252.21) 的矩阵身份仍在，而 (252.22) 的函数解释另有对应逆角误差。

### 5.2 残差与全角误差的定量分离

连续积分时，以 $\|f\|_2^2=(2\pi)^{-1}\int|f|^2$ 归一化。记 $r_{\varphi0}=\langle w_\varphi\rangle_\varphi$，则由正交性和 $v\in\operatorname{range}\Pi_\varphi$ 有

$$
\boxed{\|w_\varphi\|_2^2
=|r_{\varphi0}|^2+\tfrac12\|R_\varphi\|_{\ell^2}^2
+\gamma^2\left\|(I-\Pi_\varphi)V_c\mathcal C_\theta d\right\|_2^2.}
\tag{252.23}
$$

因此全 $M$ 行的小残差仍不支付均值和换角后的剩余谱。有限求积时还必须加入其实际误差，不能把 (252.23) 当成离散采样的无误差 Parseval 等式。

若把连续 $P,S$ 分别近似为 $\widetilde P=P+E_P$、$\widetilde S=S+E_S$，且 $D$ 在两个输入间的线段上有 Lipschitz 常数 $L_D$，则令 $\widetilde H=e_h\widetilde Pz_+$，直接加减 $S D(\widetilde H)$ 给出

$$
\|\widetilde R_\varphi-R_\varphi\|
\le |\gamma|\left[
\|E_S\|\,\|D(\widetilde H)\|
+\|S\|L_D\|E_P\|\,\|z_+\|\right].
\tag{252.24}
$$

所用向量/算子范数须一致。真实尾数值误差还须另加；本式没有假定其为零。特别是新方程仍用 $Pz_+$ 产生 native 高度，故没有消除所有与病态 $P$ 有关的有限精度风险。

## 6. 均值的准确处理与导数

### 6.1 高度平移与物理斜率均值是两件不同的事

由于 $d\theta=\rho_c\,d\varphi$，完整有限核心给出精确连续材料均值

$$
\langle U_cz\rangle_\theta=z_0+\lambda(c)^{\mathsf T}z_+,
\qquad \lambda_j(c)=\tfrac12b_jc_j.
\tag{252.25}
$$

证明只需将 $z\rho_c$ 展开，利用不同 cosine 正交、相同非零模的平方平均为 $1/2$。因此 native 高度均值为 $e_h(z_0+\lambda^{\mathsf T}z_+)$。它可由一个共同高度平移对齐，不进入 $H$ 或 $D$；这不允许把完整物理 $z_0$ 从状态或读出中删去。

令

$$
\mu_k(c)=\left\langle\cos(\omega_k\Phi_c(\varphi))\right\rangle_\varphi.
\tag{252.26}
$$

材料角无均值的尾斜率，拉回到物理角一般产生非零物理均值 $\mu^{\mathsf T}d$。所以正确的两个均值 audit 分别是

$$
\boxed{\begin{aligned}
r_{\varphi0}&=v_0-\gamma\bigl[\beta(H)+\mu(c)^{\mathsf T}d\bigr],\\
r_{\theta0}&=v_0+\lambda(c)^{\mathsf T}v_+-\gamma\beta(H).
\end{aligned}}
\tag{252.27}
$$

不能以 $v_0-\gamma\beta$ 代替第一式。共同高度平移不改变任何 $v$、$\beta$ 或这些均值残差。

### 6.2 完整核心带宽给出的均值恒等式

**定理 252-B。** 连续积分下，若 $\rho_c$ 的全部非零频率均已包含在物理测试 $1,\ldots,M$ 内，则

$$
\mu^{\mathsf T}+\lambda^{\mathsf T}S=0,
\qquad
\boxed{r_{\theta0}-r_{\varphi0}=\lambda^{\mathsf T}R_\varphi.}
\tag{252.28}
$$

**证明。** 对每个 $k$，换元给出

$$
0=\langle\cos(\omega_k\theta)\rangle_\theta
=\left\langle\rho_c(\varphi)\cos(\omega_k\Phi_c(\varphi))\right\rangle_\varphi
=\mu_k+\sum_{j=1}^M\tfrac12b_jc_jS_{jk}.
$$

最后一步是完整 $\rho_c$ 的有限展开，未丢高核心项。得到第一式后，把 (252.27) 相减并代入 $R_\varphi=v_+-\gamma Sd$，即得第二式。证毕。

这说明在**连续投影的**新右边界满足时，两个准确均值 audit 相同，不能说明该共同值为零。若精确等距切口还满足 [R239](R239-material-cut-mean-and-planar-matching.md) 的完整高度、完整非均值斜率、共同方向、正分支与实际平面投影 turning number 等假设，其均值唯一性可另行支付这一值；有限 $M$ 行本身不支付这些连续假设。

若均值也按原有限角节点测量，定义 $\lambda^{N_\theta}_j=\langle\cos(\omega_j\psi_c(\theta))\rangle_{N_\theta}$，并用物理均匀和定义 $\mu^{N_\varphi}$。则纯代数给出精确有限身份

$$
r^{N_\theta}_{\theta0}-r^{N_\varphi}_{\varphi0}
=(\lambda^{N_\theta})^{\mathsf T}R^{N_\varphi}_\varphi
+\gamma\left[(\mu^{N_\varphi})^{\mathsf T}
+(\lambda^{N_\theta})^{\mathsf T}S^{N_\varphi}\right]d.
\tag{252.29}
$$

两个均匀网格不能按连续换元直接互换；方括号必须保留为实际求积缺项。使用解析 $\lambda$ 和有限 $S,\mu$ 时，同样保留 $\mu^{\mathsf T}+\lambda^{\mathsf T}S$ 的有限求积缺项。

### 6.3 均值 audit 的完整微分

若同一真实尾提供 $B=\partial_H\beta$，则

$$
\partial_{c_j}\mu_k
=-\omega_k\left\langle\sin(\omega_k\Phi_c)A_j\right\rangle_\varphi.
\tag{252.30}
$$

令 $Z_0$ 取物理高度常数行，$\mu_j=\partial_{c_j}\mu$。从 (252.27) 可得物理均值 audit 的全部块

$$
\begin{aligned}
\partial_y r_{\varphi0}
&=Z_0f_y-\gamma e_h(B+\mu^{\mathsf T}J)PZ_+,\\
\partial_{c_j}r_{\varphi0}
&=-\gamma\left[\mu_j^{\mathsf T}d
+e_h(B+\mu^{\mathsf T}J)P_jz_+\right],\\
\partial_p r_{\varphi0}&=Z_0f_p.
\end{aligned}
\tag{252.31}
$$

材料均值 audit 的对应块为

$$
\begin{aligned}
\partial_y r_{\theta0}
&=(Z_0+\lambda^{\mathsf T}Z_+)f_y-\gamma e_hBPZ_+,\\
\partial_{c_j}r_{\theta0}
&=\tfrac12b_jv_j-\gamma e_hBP_jz_+,\\
\partial_p r_{\theta0}
&=(Z_0+\lambda^{\mathsf T}Z_+)f_p.
\end{aligned}
\tag{252.32}
$$

有限规则若用 $\lambda^{N_\theta}$，其核心导数须用该有限规则和 (252.13)，而不是偷换成解析 $b_j/2$。$B$ 必须来自真实均值输出的导数；不能从非均值 $J$ 任取一行充当它。

这些均值行是完整读出与误差检查的公式。本文没有把它们追加到原方阵 BC 中；在不调整未知量/条件的情况下擅加一行会改变维数配平。

## 7. 连续极限一致性的充分条件与证明

下面说明“改变有限测试但保持连续目标”究竟需要什么，不推测实际计算会自动满足。

**定理 252-C。** 设 $M_\nu\to\infty$。所有函数属于上述偶、$\pi$ 周期类，方向和同一切口 metric 固定。假设：

1. $\Phi_\nu\to\Phi$ 于 $C^1$，且 $0<\rho_*\le\Phi_\nu'\le\rho^*<\infty$；所有映射保留同一个角原点和周期。
2. 完整物理高度 $z_\nu$、真实物理斜率 $v_\nu$ 分别于 $L^2$ 收敛到 $z,v$。这里包括高度常数项，不把 $z_0$ 置零来制造收敛。
3. native 输入为同一个材料高度的非均值投影 $H_\nu=e_hQ_{\theta,M_\nu}U_\nu z_\nu$。同一原尾问题的有限真实解满足
   $\mathcal C_\theta D_{M_\nu}(H_\nu)\to d_\infty$ 于 $L^2$，$\beta_{M_\nu}(H_\nu)\to\beta_\infty$，而 $\beta_\infty+d_\infty$ 是极限完整高度 $e_hU z$（允许共同高度平移）的真实连续 DN 斜率。
4. 新残差 $\|R_{\varphi,\nu}\|_{\ell^2}\to0$。如使用有限角求积，则这些**实际应用到当前输入和斜率上的**系数误差也趋于零，足以使连续投影残差同样趋零。

那么极限残差

$$w=v-\gamma V(\beta_\infty+d_\infty)$$

是常数函数。若再有正确均值 audit $r_{\varphi0,\nu}\to0$，或者极限本身满足能排除该常数的完整均值唯一性假设，则 $w=0$，即完整连续 DN 边界成立。此时原材料角测试也在该极限下得到零残差。

**证明。** 由换元，对任意 $L^2$ 函数有一致界

$$
\|U_\nu f\|_2\le\sqrt{\rho^*}\,\|f\|_2,
\qquad
\|V_\nu g\|_2\le\rho_*^{-1/2}\|g\|_2.
\tag{252.33}
$$

映射一致收敛和正下界给出逆映射一致收敛。对连续函数，复合随之于一致范数收敛；对一般 $L^2$ 函数，先以连续函数逼近，再用 (252.33) 控制逼近误差，得到 $U_\nu f\to Uf$ 和 $V_\nu g\to Vg$ 于 $L^2$。再结合假设 2，得 $U_\nu z_\nu\to Uz$。

包含均值的正交 Fourier 投影是 $L^2$ 收缩，且对每个固定 $L^2$ 函数强收敛到恒等算子。因此

$$
\|\Pi_{M_\nu}U_\nu z_\nu-Uz\|_2
\le\|U_\nu z_\nu-Uz\|_2+\|\Pi_{M_\nu}Uz-Uz\|_2\longrightarrow0.
$$

去掉均值并乘 $e_h$ 后也是如此，所以假设 3 的输入确实趋向同一个完整材料高度，而不是另一个由截断偷偷修改的目标。假设 3 及 (252.33) 进一步给出整个 $w_\nu\to w$ 于 $L^2$。

固定任意 $k\ge1$。充分大时 $k\le M_\nu$，$w_\nu$ 的第 $k$ 个 cosine 系数就是 $(R_{\varphi,\nu})_k$，它由假设 4 趋零；同时 $L^2$ 收敛使该系数趋向 $w$ 的第 $k$ 个系数。故 $w$ 的全部非均值 cosine 系数为零。由于函数始终处于偶、$\pi$ 周期类，Fourier 完备性说明 $w$ 是常数。

均值 audit 趋零时 $\langle w\rangle=0$，所以该常数为零；若使用均值唯一性，则按其真实假设得到同一结论。此时 $U_\nu w_\nu\to Uw=0$；材料角有限正交投影为收缩，因此其非均值系数的 $\ell^2$ 范数也趋零。证毕。

假设 3 是实际尾数值方案对原连续尾的收敛要求，本文没有证明它。仅有新边界某一次退出成功、或者 $P,S$ 都可逆，不足以得到上述极限。

一个有用的充分谱尾估计是：若 $f$ 的 $r$ 阶角导数在 $L^2$ 中，$r$ 为正整数，则 Parseval 逐项给出

$$
\|(I-\Pi_M)f\|_2
\le [2(M+1)]^{-r}\,\|\partial_\theta^rf\|_2.
\tag{252.34}
$$

证明是在每个 $k>M$ 项用 $(2k)^{2r}\ge[2(M+1)]^{2r}$，再求和。对换角后的高度和尾斜率若能取得一致导数界，这提供具体尾项消失的条件；没有这个或其它实际误差控制，不能只据 $M$ 增大就称有限投影缺项已经消失。有限求积及逆角误差还须随精化一起控制。

## 8. 本结论对当前研究的准确用途

本结果给出了一套可以独立实现和检验的备选边界，而不是一条新的接受记录。若实际投影诊断支持采用它，需要明确记录有限测试从 $d\theta$ 改为 $d\varphi$、两套投影参数和完整源身份；同一个真实尾与同一个完整 scalar 仍必须保留。

新的直接导数项是 $v_+$，所以没有在这一项左乘 $P$；但 $H=e_hPz_+$、$SJD(H)$ 的链式作用、核心响应及全段传播仍可能病态。本文不给完整 BVP 的稳定性、可解性或收敛保证，不把数学可逆性当成浮点可解性。

对实际新候选，至少应同时如实读出新残差、原 $R_\theta$、(252.21) 的投影缺项、正确均值和全角谱尾。这是判断同一有限场是否已接到原尾的问题本身，不是把旧 BC 成功旗沿用到新测试上。未实际计算前，本题原材料角门仍未因此核销。

最后，非均值一阶高度 DN 条件只是一项边界条件。完整 cut 的九 jet（$\partial_s^i\partial_\theta^jF$，$0\le i,j\le2$）、单一平面配准、完整高度均值、反射接缝、整个闭面的同 $g$ 度量及曲率/reach/真实像 Hausdorff 幅度，仍按实际有限场支付。本文不要求另加所有九 jet 差达到机器精度的完成门，也不把本条件性一致性证明代替课题 README 原来的同度量精化和整面检查。
