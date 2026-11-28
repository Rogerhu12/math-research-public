# R1187：原半秩目标上的有界实际商与极化比较

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明。** 本文在 R1011 的原同一个 $X_1,c_0,c_1,D_0$ 和原半秩目标 $C/\mathbf Q$ 上，选取一个新的、实际且有界的满射 $q_*:J_{X_1}\to C$，保持 $q_*N=0$ 及 $q_*(D_0)$ 非挠，并将 R1185 的极化比较常数 $K$ 替换为只依原 Belyi 次数和亏格的显示整数；§10 进一步控制同一目标的实际双向同源图及稳定 Faltings 高度。目标 $C$ 不作同源替换，原 CM 点不作替换。

这里选择的是有界新箭头，不给任意预先固定的旧 $q_C$ 的整数尺度一个统一界。新的 Abel jet 须以 $q_*$、原 $t=p^3w$ 及同一实际 Néron 格重新计算；模型坐标高度、倍二误差、微分基和局部倍数仍保留。本文没有执行数学程序。

## 1. 原对象、迹规范和显示常数

沿用 [R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md) 的范围及对象：

$$
X=X_1,\quad J=J_X,\quad g=\dim J,\quad
D=[c_1-c_0],\quad N=1+\delta+\delta^2,\quad E_0=3-N,
$$
$$
D_0=E_0D,\qquad q_0:J\twoheadrightarrow C,\qquad
q_0N=0,\qquad \beta_0=q_0(D_0)\ \text{非挠},
$$
$$
F_0=\operatorname{End}_{\mathbf Q}^0(C)\ \text{全实},\qquad
f=[F_0:\mathbf Q],\quad n=\dim C=2f,\quad
\operatorname{rank}C(\mathbf Q)=f,\quad
C(\mathbf Q)\otimes\mathbf Q=F_0\beta_0.
\tag{1187.1}
$$

$C$ 只须在 $\mathbf Q$ 上简单。本文不会将其当作几何简单。令 $\Theta$ 为 $J$ 的原主极化；用 $c_1$ 平移 $W_{g-1}$ 得到的有理 theta 线丛记为 $\Theta_0$。它代表 $\Theta$，但不要求对称。

全部范数采用 Gaudron–Rémond 的**完整 Tate 迹**：若 $A$ 维数为 $a$，则

$$
\operatorname{Tr}_A(u)
=-[T^{2a-1}]\deg(T\operatorname{id}_A-u),\qquad
\operatorname{Tr}_A([m])=2am.
\tag{1187.2}
$$

对于极化 $\lambda_A,\lambda_B$，置

$$
u^\dagger=\lambda_A^{-1}u^\vee\lambda_B,
\qquad
\|u\|^2=\operatorname{Tr}_A(u^\dagger u)
=\operatorname{Tr}_B(uu^\dagger).
\tag{1187.3}
$$

没有在 (1187.3) 中除以二。原文依据是 Gaudron–Rémond 2014，Definitions 2.1、2.4、2.6 及 Properties 2.2，印刷 pp.2063–2065。

取原覆盖次数的一个整数上界 $D_{\rm B}\ge\deg_{\rm B}(X)$；本原曲线可取

$$
D_{\rm B}=D_p=3p(p-1).
\tag{1187.4}
$$

以下常数都是显示正整数：

$$
H=1+13\cdot10^6gD_{\rm B}^5+2g,
\qquad
U=241(6g^2)^{4g^2}(2g^2)^5H,
$$
$$
\Gamma=(8g)^gU^{3g^2},\qquad
E=3^{2g}\Gamma^2,
$$
$$
R=(4g^2)^{2g^2}E^{2g^2}U^{16g^4},\qquad
K_*=9R^2+1.
\tag{1187.5}
$$

**定理 1187.1。** 在同一 $C/\mathbf Q$ 上存在有理对称 ample 线丛 $\mathcal L_0$，令 $\mathcal L=\mathcal L_0^{\otimes3}$，以及实际有理满射 $q_*:J\twoheadrightarrow C$，使

$$
h^0(C,\mathcal L_0)\le\Gamma,\qquad
h^0(C,\mathcal L)\le3^g\Gamma,\qquad
\deg\lambda_{\mathcal L}\le E,
$$
$$
q_*N=0,\qquad \beta_*=q_*(D_0)\ \text{非挠},\qquad
\|q_*\|\le3R,
\tag{1187.6}
$$

且 $\mathcal L$ 的完整线性系是射影正规闭嵌入，原有理线丛

$$
\boxed{\quad
\Theta_0^{\otimes K_*}\otimes(q_*^*\mathcal L)^{-1}
\quad\text{ample}.\quad}
\tag{1187.7}
$$

这些数据有 §7 的终止枚举和有限验证证书。相应原 Abel 映射

$$
f_*(x)=q_*[x-c_1]
$$

满足同一原点的精确关系

$$
\beta_*=3q_*D=-3f_*(c_0).
\tag{1187.8}
$$

## 2. 同一个 $J$ 所生成的类：有界极化与自同态协体积

使用 Gaudron–Rémond，*Nouveaux théorèmes d’isogénie*，Mémoires SMF 176 (2023)。该文 §1.2 明定全部同态、子簇、简单性均在给定底域上。这里底域是 $\mathbf Q$，该文的生成对象取为我们的 $J$，而不是未知高度的目标 $C$。

将 $J$ 在 $\mathbf Q$ 上分解到同源

$$
J\sim_{\mathbf Q}\prod_i S_i^{m_i},
$$

其中 $S_i$ 两两不同源且在 $\mathbf Q$ 上简单。该文参数 $\nu$（原文记为 $n$）满足

$$
\nu=\sum_i\frac{2(\dim S_i)^2}
 {\operatorname{rank}_{\mathbf Z}\operatorname{End}_{\mathbf Q}(S_i)}
\le2g^2.
\tag{1187.9}
$$

原 $C$ 是 $J$ 的实际商，故由 Poincaré 完全可约性与 $J\times C$ 一同属于该文由 $J$ 生成的类。该类的量 $\Upsilon,d_{\rm GR}$ 同时控制所有这些对象。

Javanpeykar，*Polynomial bounds for Arakelov invariants of Belyi curves*，Theorem 1.1.1、§2.3，给

$$
h_F(J)=h_{\rm Fal}(X)\le13\cdot10^6gD_{\rm B}^5.
\tag{1187.10}
$$

这里使用 Faltings 原规范。Javanpeykar 的曲线 $L^2$ 度量在行列式上正是 Jacobian 的 $2^{-g}\int|s\wedge\overline s|$ 度量；Gaudron–Rémond 2014 *Théorème des périodes...* §2.3 明确把它与含 $\pi$ 的另一规范区分。因此 (1187.10) 不漏 $g\log\pi/2$。

2023 年文 Theorem 1.8 和 §1.2 给

$$
\Upsilon\le241(\mathrm e\nu)^{2\nu}\nu^5
 \max\{1,h_F(J)+3g/2\}\le U,
\qquad
d_{\rm GR}\le\Upsilon^{2\nu}\le U^{4g^2}.
\tag{1187.11}
$$

此处 $\mathrm e<3$ 是自然对数的底数；显示系数 $241$ 是整数二百四十一。

对该类内维数为 $a$ 的对象，原文量 $e_{\rm GR}(A)$ 满足 $e_{\rm GR}(A)\le2a^2$。Theorem 1.3(2) 给同一 $C$ 上、**定义在 $\mathbf Q$ 上的对称 ample 线丛** $\mathcal L_0$，且

$$
h^0(C,\mathcal L_0)
\le(8n)^{n/4}\Upsilon^{3e_{\rm GR}(C)/2}
\le\Gamma.
\tag{1187.12}
$$

在特征零，ample 线丛的三次幂 very ample 且正规生成；后者也直接由 Sekiguchi Theorem 2.3 的乘法满射归纳得到。故 $\mathcal L=\mathcal L_0^3$ 具有定理要求的嵌入性质。阿贝尔簇 Riemann–Roch 给

$$
h^0(C,\mathcal L)=3^nh^0(C,\mathcal L_0)\le3^g\Gamma,
\qquad
e:=\deg\lambda_{\mathcal L}=h^0(C,\mathcal L)^2\le E.
\tag{1187.13}
$$

再对 $A=J\times C$ 使用 Theorem 1.3(3)。忠实的 Tate 表示给

$$
\operatorname{rank}_{\mathbf Z}\operatorname{End}_{\mathbf Q}(A)
\le4(\dim A)^2\le16g^2.
$$

原文的协体积与 (1187.2)–(1187.3) 相同，并满足

$$
\operatorname{vol}\operatorname{End}_{\mathbf Q}(A)^2
\mid d_{\rm GR}^{\operatorname{rank}\operatorname{End}_{\mathbf Q}(A)}.
$$

因而

$$
\boxed{\quad
\operatorname{vol}\operatorname{End}_{\mathbf Q}(J\times C)
\le U^{32g^4}.
\quad}
\tag{1187.14}
$$

这个界未把 $h_F(C)$ 当作一个额外输入。

## 3. 非主极化目标的整数性与 Hom 协体积

本节逐项说明整数性，不能由 $\lambda_{\mathcal L}$ 非主却默认 $\operatorname{End}(C)$ 被 Rosati 保持。

### 3.1 End 的下界来自迹配对的行列式

对任一阿贝尔簇 $A/\mathbf Q$，取 $\operatorname{End}_{\mathbf Q}(A)$ 的整数基 $u_1,\ldots,u_s$，置

$$
T_{ij}=\operatorname{Tr}_A(u_i u_j).
$$

每个 $T_{ij}$ 是整数。令 $D_\dagger$ 为 $\dagger$ 在此**有理向量空间**上的矩阵。它不必是整数矩阵，但 $D_\dagger^2=1$，故 $\det D_\dagger=\pm1$。Rosati Gram 矩阵是 $TD_\dagger$；它正定，故 $T$ 非退化，并且

$$
\operatorname{vol}\operatorname{End}_{\mathbf Q}(A)^2
=\det(TD_\dagger)=|\det T|\in\mathbf Z_{\ge1}.
\tag{1187.15}
$$

这正是 GR2014 Proposition 2.9 的行列式证明。因此 $\operatorname{vol}\operatorname{End}(J)$ 与 $\operatorname{vol}\operatorname{End}(C)$ 均至少一，无需 $C$ 的极化为主。对当前全实 $F_0$ 也可另核：正 Rosati 在 $F_0$ 上是恒等，完整 Tate 迹为 $4\operatorname{Tr}_{F_0/\mathbf Q}$，故平方协体积为 $4^f$ 乘原端环序的判别式绝对值。正文后续只需一般式 (1187.15)。

### 3.2 主极化源给 Hom 的最短向量下界

置

$$
H_C=\operatorname{Hom}_{\mathbf Q}(J,C),\qquad
H'_C=\operatorname{Hom}_{\mathbf Q}(C,J),\qquad
r=\operatorname{rank}_{\mathbf Z}H_C\le4gn\le4g^2.
$$

因 $\lambda_\Theta$ 是实际同构，$f\in H_C$ 时 $f^\dagger\in H'_C$，从而 $f^\dagger f$ 是 $J$ 的实际整数自同态。因此

$$
f\ne0\quad\Longrightarrow\quad
\|f\|^2=\operatorname{Tr}_J(f^\dagger f)\in\mathbf Z_{\ge1}.
\tag{1187.16}
$$

此外 $e=\deg\lambda_{\mathcal L}$ 杀掉 $\ker\lambda_{\mathcal L}$，故 $e\lambda_{\mathcal L}^{-1}$ 是实际同态。对 $u\in H'_C$ 有 $eu^\dagger\in H_C$，于是

$$
eH'_C\subset H_C^\dagger\subset H'_C,
\qquad [H'_C:H_C^\dagger]\le e^r.
\tag{1187.17}
$$

$\dagger$ 是两个 Hom 实向量空间间的等距同构，所以

$$
\frac{\operatorname{vol}(H_C)}{\operatorname{vol}(H'_C)}
=[H'_C:H_C^\dagger]\le e^r.
\tag{1187.18}
$$

### 3.3 必须保留两个交叉 block

在 $J\times C$ 上取乘积极化。GR2014 Proposition 2.5 给**实际整数格**的正交直和

$$
\operatorname{End}_{\mathbf Q}(J\times C)
=\operatorname{End}_{\mathbf Q}(J)\oplus H'_C
 \oplus H_C\oplus\operatorname{End}_{\mathbf Q}(C).
$$

故由 (1187.15)

$$
\operatorname{vol}(H_C)\operatorname{vol}(H'_C)
\le\operatorname{vol}\operatorname{End}_{\mathbf Q}(J\times C).
\tag{1187.19}
$$

将 (1187.18) 乘入 (1187.19)，再用 (1187.13)–(1187.14)，得到

$$
\boxed{\quad
\operatorname{vol}(H_C)
\le e^{r/2}\operatorname{vol}\operatorname{End}(J\times C)^{1/2}
\le E^{2g^2}U^{16g^4}.
\quad}
\tag{1187.20}
$$

这里没有把 $H_C$ 的协体积直接当作 End 协体积的某个未付因子，也没有把 $H_C$ 和 $H'_C$ 擅自认成同一个整数格。

## 4. 短同态生成族及原 $D_0$ 的非挠分量

令 $\lambda_1\le\cdots\le\lambda_r$ 为 $H_C$ 的欧氏连续最小值。由 (1187.16)，$\lambda_1\ge1$。Minkowski 第二定理的标准推论（GR2014 Lemma 3.1，p.2069）给

$$
\lambda_1^{r-1}\lambda_r
\le r^{r/2}\operatorname{vol}(H_C).
$$

因此有 $\mathbf Q$-线性无关的实际同态 $f_1,\ldots,f_r\in H_C$，生成 $H_C\otimes\mathbf Q$，且

$$
\|f_i\|\le\lambda_r
\le(4g^2)^{2g^2}E^{2g^2}U^{16g^4}=R.
\tag{1187.21}
$$

只需有理生成族，不声称这是一组整数基。

原曲线自同构 $\delta$ 保持 Jacobian 主极化，故

$$
N^\dagger=N,\quad N^2=3N,\quad
E_0^\dagger=E_0,\quad E_0^2=3E_0,\quad E_0N=0.
\tag{1187.22}
$$

$E_0$ 在对应 Hermitian 空间上只有特征值 $0,3$，其算子范数至多三。定义实际映射

$$
q_i=f_iE_0.
$$

则 $q_iN=0$ 且

$$
\|q_i\|^2
=\operatorname{Tr}(f_i^\dagger f_i E_0^2)
\le9\operatorname{Tr}(f_i^\dagger f_i)
\le9R^2.
\tag{1187.23}
$$

必须保留原点上的因子三：

$$
E_0D_0=E_0^2D=3D_0.
\tag{1187.24}
$$

若所有 $q_iD_0$ 都是挠点，写 $dq_0=\sum_i a_i f_i$，其中 $d\ge1,a_i\in\mathbf Z$，则

$$
\sum_i a_i q_iD_0
=dq_0E_0D_0
=3d\beta_0
$$

也是挠点，矛盾。因此某个 $q_iD_0$ 非挠。选择该 $q_i$ 为 $q_*$。其像是 $C$ 的非零有理阿贝尔子簇；$C/\mathbf Q$ 简单，故 $q_*$ 满射。由 $q_*N=0$ 得到 (1187.8)。这既保同一个原 $D_0$，也不通过替换 CM 点来寻找非挠点。

## 5. 从小范数得到有界极化比较

令

$$
T=q_*^\dagger q_*\in\operatorname{End}_{\mathbf Q}(J).
$$

它是 Rosati 自伴、半正的，且

$$
\operatorname{Tr}_J(T)=\|q_*\|^2\le9R^2.
\tag{1187.25}
$$

其每个分析特征值非负，且不超过完整 Tate 迹。因此 $K_*\operatorname{id}-T$ 正定。Appell–Humbert 的正定判据用于原线丛

$$
\Theta_0^{K_*}\otimes(q_*^*\mathcal L)^{-1}
$$

即得 (1187.7)：其相对 $\Theta$ 的 Riemann 形式正是 $K_*\operatorname{id}-T$。这不是只给一条数值高度不等式；它给该指定有理线丛的真实 ampleness。

有限证书可以直接由同态、线丛及完整迹构成。GR2014 Proposition 2.8 给精确整数

$$
\|q_*\|^2=
\frac{2g}{(\Theta_0^g)}
 (\Theta_0^{g-1}\cdot q_*^*\mathcal L),
\tag{1187.26}
$$

其中交数可由实际射影模型的 Hilbert 多项式有限求出。验证 (1187.25) 后，上述正定证明即是 (1187.7) 的证书。若坚持 R1185 的截面型证书，则对这个**已经固定的 $K_*$** 枚举 very ample 幂即可；终止由刚证明的 ampleness 保证。

二次规范高度的函子性与 ample 线丛非负性给

$$
\widehat h_{\mathcal L}(q_*P)
\le K_*\widehat h_J(P)
\qquad(P\in J(\overline{\mathbf Q})).
\tag{1187.27}
$$

$\Theta_0$ 不对称不妨碍这里的二次高度：对称化后除以二正好恢复原主极化规范，没有额外的二。

## 6. 同一原点高度及同一 Mordell–Weil 对数线的运输

### 6.1 将新 $K_*$ 代入原高度归约

令 $M$ 为 R1182 用同一目标 $C$ 的 Néron 模型取得的实际局部整数，置 $\beta_*'=M\beta_*$。由 R1185 的原两点高度及 (1187.8)、(1187.27)，

$$
\boxed{\quad
\widehat h_{\mathcal L}(\beta_*')
\le18M^2K_*\frac g{g-1}H_{\rm br}(D_p).
\quad}
\tag{1187.28}
$$

用 $\mathcal L$ 的完整基给射影嵌入 $\iota$，其实际倍二公式和齐次 Nullstellensatz 证书给 R1185 的 $E_{\mathcal L}$，所以

$$
\boxed{\quad
h_\iota(\beta_*')
\le18M^2K_*\frac g{g-1}H_{\rm br}(D_p)
+E_{\mathcal L}/3.
\quad}
\tag{1187.29}
$$

该步骤删除了一个独立未知的极化比较参数。它尚未把 $E_{\mathcal L}$、选定模型系数、微分基分母及 $M$ 同时换成只依 $p$ 的界。

### 6.2 不丢失原半秩和对数横截性

目标 $C$ 完全不变，故 $F_0$、维数、秩及半秩关系不变。由 (1187.1) 与 $\beta_*$ 非挠，有唯一 $\alpha\in F_0^\times$ 满足

$$
\beta_* = \alpha\beta_0
\quad\text{在 }C(\mathbf Q)\otimes\mathbf Q\text{ 中}.
\tag{1187.30}
$$

在任一有限素数 $q$，经整数进入形式邻域后取实际对数，函子性给

$$
\log_q\beta_*=d\alpha(\log_q\beta_0),
\qquad
(F_0\otimes\mathbf Q_q)\log_q\beta_*
=(F_0\otimes\mathbf Q_q)\log_q\beta_0.
\tag{1187.31}
$$

因此原 Mordell–Weil 对数空间及其 annihilator **完全相同**。对 R1182 的同一有理 $F_0$-平衡交错型 $\Omega$，有

$$
\Omega(d\alpha\,u,v)=\Omega(u,d\alpha\,v).
\tag{1187.32}
$$

这给新线性函数的准确运输，但不声称每一个选定的标量 Chabauty 函数数值相同。也不从 (1187.30) 推出 $\alpha$ 的高度已受控。

新 Abel 列是实际微分推送

$$
\log_q f_*(x)=dq_*\bigl(\log_q[x-c_1]\bigr).
\tag{1187.33}
$$

它的首个非零系数仍在 $\operatorname{Lie}(C)(\mathbf Q)$。R1011 的有理 Lie 空间与原 Mordell–Weil 对数线交零、以及 R1182 的有理超平面半稳定论证，均对同一 $C$ 和 (1187.31) 继续有效。首阶仍满足

$$
m_*\le2(g-n)+1.
\tag{1187.34}
$$

在 $q=p$ 的原 CM 支路，须消费 R1184 的 $t=b-1=p^3w$，按新 $q_*$ 重算 $U_m^*$、$\ell_m^*=\Omega(-,U_m^*)$、$\mathcal B$ 和 $e_m$；R1186 的实际代数 jet 高度界也须输入此新映射的数据。不能沿用旧商或旧参数缩放的系数高度。

## 7. 有效选择与有限证书

本节给终止程序，不声称本文已经运行它。输入是原 $J,C,q_0,N,D_0$ 的有限有理模型与群结构数据。

首先枚举定义在 $\mathbf Q$ 上的线丛及其有限 transition 数据、对称同构、截面和 ample 证书，检验 $h^0(C,\mathcal L_0)\le\Gamma$。一个 ample 证书可以是其某次幂的闭嵌入；所有数据在有限 affine cover 上由有理多项式给出，等式及闭嵌入可有限检验。§2 保证枚举遇到一个合格 $\mathcal L_0$。随后取实际三次幂及其完整截面基，得到 $\mathcal L$。

固定该 $\mathcal L$ 后，枚举有理映射图像及有限开覆盖公式，验证它们给出 $q:J\to C$ 的全局态射、$q(0)=0$ 及群律相容。对每个实际同态检验

$$
qN=0,\qquad \|q\|^2\le9R^2.
\tag{1187.35}
$$

范数用 (1187.26) 的有理交数计算，不用数值近似的复周期比较。无需先知道全部 Hom 格的基，也无需先证明已枚举到完整生成族。

非挠性也有有限证书。选择同一 $C$ 的两个不同的**好约化辅助素数** $\ell_1,\ell_2$，并计算

$$
B_{\rm tor}=\#C(\mathbf F_{\ell_1})\,
             \#C(\mathbf F_{\ell_2}).
\tag{1187.36}
$$

每个有理挠点的 $r$-primary 部，选择其中一个不等于 $r$ 的好约化素数后，由 prime-to-residue-characteristic 挠点的约化单射得其阶整除对应有限群阶。因此 $B_{\rm tor}$ 杀掉 $C(\mathbf Q)_{\rm tors}$。对枚举的 $q$ 精确检验

$$
[B_{\rm tor}]q(D_0)\ne0.
\tag{1187.37}
$$

通过者的点必非挠；§4 证明必有一个通过者，所以此搜索终止。这里的 $\ell_1,\ell_2$ 与 level $p$、局部素数 $q$ 无关，不假设 $C$ 在 $p$ 好约化。

最终证书包括实际 $\mathcal L_0,\mathcal L,q_*$、对称与群律图、(1187.35) 的精确迹或交数、(1187.37) 的有理非零点，以及 (1187.7) 的正定证书。射影坐标的任意整数放大不会伪造一个更小的 Rosati 范数；旧 $q_0$ 的任意尺度也不在这份证书的界内。

## 8. 已消成本及准确剩余接口

本篇取得的是同一原非 CM 半秩目标上的有界实际商，并且保持原 CM 点差非挠、原 Mordell–Weil 对数线和原局部支路。通过 (1187.5)、(1187.28)–(1187.29)，R1185 的 $K$ 可对这个明确的新选择改成 $K_*$。

尚须继续控制的是这个实际有界选择的有理坐标模型、倍二误差 $E_{\mathcal L}$、$F_0$-基及 $\Omega$ 的系数高度、局部 Néron 数据和新 Abel jet 的代数输入。小 Rosati 范数本身不等于任意射影表达式的系数高度小。本文也未证明 R1182 的隔离半径落在统一 $p^3$ 盘内；完整盘结论仍须把这些数据代入首项估值与全部余项比较。

## 9. 正式来源与适用位置

1. Éric Gaudron–Gaël Rémond, *Nouveaux théorèmes d’isogénie*, **Mémoires de la Société Mathématique de France 176 (2023), vi+123 pp.**, DOI [10.24033/msmf.484](https://doi.org/10.24033/msmf.484)。[正式全文 PDF](https://smf.emath.fr/system/files/filepdf/smf_mem_176_0.pdf)：§1.2 的底域与简单性约定、$\nu,d_{\rm GR},\Upsilon,e_{\rm GR}$ 在印刷 pp.2–4（PDF 第10–12页）；Theorem 1.3 在 p.4；Theorem 1.8 在 p.7（PDF 第15页）。本文以原 $J$ 为该文生成对象，未把目标 $C$ 的高度偷偷代入。
2. Éric Gaudron–Gaël Rémond, *Polarisations et isogénies*, **Duke Mathematical Journal 163 (2014), 2057–2108**, DOI [10.1215/00127094-2782528](https://doi.org/10.1215/00127094-2782528)。[作者正式版 PDF](https://lmbp.uca.fr/~gaudron/art13.pdf)：Definitions 2.1、2.4、2.6 及 Properties 2.2，pp.2063–2065；Propositions 2.5、2.8、2.9 与 Corollary 2.10，pp.2065–2068；Lemma 3.1，p.2069。全部使用完整 Tate 迹。
3. Ariyan Javanpeykar, *Polynomial bounds for Arakelov invariants of Belyi curves*, **Algebra & Number Theory 8 (2014), 89–140**, DOI [10.2140/ant.2014.8.89](https://doi.org/10.2140/ant.2014.8.89)。[正式 PDF](https://msp.org/ant/2014/8-1/ant-v8-n1-p04-s.pdf)：Theorem 1.1.1，p.90；§2.3 对稳定 Faltings 高度及 Jacobian 的规范，p.98。
4. Éric Gaudron–Gaël Rémond, *Théorème des périodes et degrés minimaux d’isogénies*, **Commentarii Mathematici Helvetici 89 (2014), 343–403**, DOI [10.4171/CMH/322](https://doi.org/10.4171/CMH/322)。[作者正式版 PDF](https://lmbp.uca.fr/~gaudron/art11.pdf)：§2.3，pp.351–352，核对 $h_F$ 的原度量；§2.4 的 Riemann 形式正定判据也与 §5 所用规范相同。
5. Tsutomu Sekiguchi, *On projective normality of abelian varieties*, **J. Math. Soc. Japan 28 (1976), 307–322**。[正式 PDF](https://www.jstage.jst.go.jp/article/jmath1948/28/2/28_2_307/_pdf/-char/ja)：引言 p.307 及 Theorem 2.3，p.321，取特征零及 ample 线丛三次幂。
6. [R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md)、[R1182](R1182-original-effective-Abel-jet-valuation-and-CM-disc-radius.md)、[R1184](R1184-original-uniform-cubic-CM-disc-and-Neron-integrality.md)、[R1185](R1185-original-CM-point-height-and-quotient-cost.md) 支付同一原点、半秩对数线、实际 $p^3$ 参数及高度常数。本文未更换任何 CM 点，也未借另一个曲线的有理点来完成非挠性选择。

## 10. 同一目标的有界实际同源图与 Faltings 高度

本节继续使用 §§1–9 已选定的同一个 $C,\mathcal L,q_*$，不再选择一个未经运输的抽象同源因子。置

$$
Q=9R^2,\qquad
B=\operatorname{im}(q_*^\dagger)\subset J,
\qquad
\iota=q_*^\dagger:C\longrightarrow B,
\qquad
\rho=q_*|_B:B\longrightarrow C.
\tag{1187.38}
$$

所有箭头定义在 $\mathbf Q$ 上。因 $J$ 主极化，$q_*^\dagger$ 是实际同态，而非只在 $\operatorname{Hom}\otimes\mathbf Q$ 中的分数箭头。$q_*$ 满射，故 $q_*^\dagger$ 的像维数为 $n=\dim C$；$\iota$ 是到其像的同源。另一方面

$$
T_C=\rho\iota=q_*q_*^\dagger\in\operatorname{End}_{\mathbf Q}(C)
\tag{1187.39}
$$

是相对于 $\mathcal L$ 的正定自伴端态，因此也为同源，$\rho$ 随之为同源。

完整 Tate 迹满足

$$
\operatorname{Tr}_C(T_C)=\|q_*\|^2\le Q.
$$

在复切空间上记其 $n$ 个正特征值为 $\lambda_i$；Tate 特征值将它们各计两次。故算术–几何平均不等式给

$$
\deg T_C=\prod_{i=1}^n\lambda_i^2
\le\left(\frac{\operatorname{Tr}_C(T_C)}{2n}\right)^{2n}
\le Q^{2n}.
$$

由实际复合 (1187.39)，

$$
\boxed{\quad
\deg\iota\,\deg\rho=\deg T_C\le Q^{2n},
\qquad \deg\iota,\deg\rho\le Q^{2g}.
\quad}
\tag{1187.40}
$$

这同时控制两个具体箭头，因而可以在后继模型比较中保留实际微分，而不只记录“存在某个小同源”。

令 $\Theta_B=\Theta_0|_B$。由 Rosati 的定义，$\lambda_{\iota^*\Theta_B}=\lambda_{\mathcal L}T_C$；Riemann–Roch 以及有限平坦拉回的 Euler 特征给

$$
\deg\iota\,h^0(B,\Theta_B)
=h^0(C,\iota^*\Theta_B)
=h^0(C,\mathcal L)\sqrt{\deg T_C}.
\tag{1187.41}
$$

特别地

$$
h^0(B,\Theta_B)\le3^g\Gamma Q^n.
\tag{1187.42}
$$

GR2014 *Théorème des périodes et degrés minimaux d’isogénies* §2.3，印刷 pp.351–352，在本篇原 $h_F$ 规范下给子簇界

$$
h_F(B)\le h_F(J)+\log h^0(B,\Theta_B)
                   +\frac32(g-n),
$$

以及同一页的 Raynaud 同源高度界

$$
h_F(C)\le h_F(B)+\frac12\log\deg\iota.
$$

保留 (1187.41) 中的分母后，$\deg\iota$ 的成本部分抵消：

$$
\begin{aligned}
h_F(C)
&\le h_F(J)+\log h^0(C,\mathcal L)
 +\frac12\log\frac{\deg T_C}{\deg\iota}
 +\frac32(g-n)\\
&=h_F(J)+\log h^0(C,\mathcal L)
 +\frac12\log\deg\rho+\frac32(g-n)\\
&\le h_F(J)+\log(3^g\Gamma)+n\log Q+\frac32(g-n).
\end{aligned}
\tag{1187.43}
$$

结合 (1187.10)，得到只依 $g,D_{\rm B}$ 的显示上界

$$
\boxed{\quad
h_F(C)\le
13\cdot10^6gD_{\rm B}^5
+\log(3^g\Gamma)+g\log(9R^2)+\frac32g.
\quad}
\tag{1187.44}
$$

本节没有改变原 $C$ 的 $\mathbf Q$-结构；故 §6.2 的半秩、同一 $\beta_*$ 和 Lie 对数空间的运输保持原样。新取得的是实际双向同源图的次数及同一目标的稳定 Faltings 高度。由这些模意义高度构造系数受控的有理模型、微分基和群律，仍须给具体模型比较；不能将 (1187.44) 直接当作任意已给坐标的系数高度。
