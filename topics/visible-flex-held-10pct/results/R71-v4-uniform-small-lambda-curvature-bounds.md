# R71. v4 小 λ 曲率列及同模投影的 M 一致双边界

维护：Astra-held10-06bbeb39-20261126。2026-11-26 UTC。

这是 [R70](R70-full-to-complementary-phase-homotopy.md) 新族的一个更强、可独立使用的结论。它证明小 λ 时，真实连续曲率列以及投影到同一组材料角余弦模态后的列，均有与截断阶数 M 无关的双边界。证明只用真窗口、真频率和积分正交性，不使用采样奇异值或实际 Newton 返回。

**该界不是完整 BVP、原 adaptive-chart 位置投影或边界 Schur 补的逆界。** 它没有给新接受场、λ 延续成功、真实尾或固定问题 C2 收敛。

## 1. 定义与命题

沿用 R68/R70 的真实数据

$$
P=2\pi/3,\quad c=P/2,\quad 0<S<c,\quad L=c-S,\quad 0<b<L,
\quad D_1=\frac{630}{256b},\quad \omega_j=\frac{j\pi}{L}.
$$

在完整材料周期上定义

$$
A_j(u)=\frac{\sin(3ju)}{3j},\qquad
B_j(u)=\frac{W(v(u))\sin(\omega_jv(u))}{\omega_j+D_1},
\qquad \Psi_j^\lambda=(1-\lambda)A_j+\lambda B_j.
$$

其中 v 折回 $[-c,c)$，W 在 $|v|\ge L$ 为零，在补弧内为 R68 的原平滑窗；特别有 $0\le W\le1$、$\|W'\|_\infty\le D_1$。全部 L2 范数使用完整周期的非归一化 Lebesgue 积分。改变积分起点不改变范数。

对任意有限指标集 $J\subset\{1,2,\ldots\}$ 和实系数 $d=(d_j)_{j\in J}$，置

$$
\mathcal A_Jd=\sum_{j\in J}d_j\cos(3ju),\quad
\mathcal B_Jd=\sum_{j\in J}d_j B_j'(u),\quad
\mathcal T_{\lambda,J}=(1-\lambda)\mathcal A_J+\lambda\mathcal B_J.
$$

令 $\Pi_J$ 为完整周期上到 $\operatorname{span}\{\cos(3ju):j\in J\}$ 的 L2 正交投影，并记

$$
K=\sqrt{\frac{2L}{c}},\qquad
\ell_\lambda=\sqrt c\{1-\lambda-\lambda K\},\qquad
u_\lambda=\sqrt c\{1-\lambda+\lambda K\}.
$$

**命题。** 对 $0\le\lambda\le1$，总有

$$
\|\mathcal B_Jd\|_2\le\sqrt{2L}\,\|d\|_2,
\qquad
\|\mathcal T_{\lambda,J}d\|_2\le u_\lambda\|d\|_2.
\tag{1}
$$

若

$$
0\le\lambda<\lambda_*:=\frac1{1+K},
\tag{2}
$$

则下述两个下界同时成立：

$$
\boxed{\quad
\|\mathcal T_{\lambda,J}d\|_2\ge\ell_\lambda\|d\|_2,
\qquad
\|\Pi_J\mathcal T_{\lambda,J}d\|_2\ge\ell_\lambda\|d\|_2.
\quad}
\tag{3}
$$

它们不依赖 $|J|$ 或最大模态。因此，对完整连续曲率列，或对同模投影后的有限列矩阵，欧氏系数范数到上述 L2 范数的条件数均至多

$$
\frac{u_\lambda}{\ell_\lambda}
=\frac{1-\lambda+\lambda K}{1-\lambda-\lambda K}.
\tag{4}
$$

## 2. 补弧算子的 M 一致上界

在真补弧 $[-L,L]$ 上写

$$
f(v)=\sum_{j\in J}\frac{d_j}{\omega_j+D_1}\sin(\omega_jv),
\qquad \mathcal B_Jd=(Wf)'=Wf'+W'f.
$$

由 $0\le W\le1$、$|W'|\le D_1$ 和 $(x+y)^2\le2x^2+2y^2$，

$$
\|\mathcal B_Jd\|_2^2
\le2\{\|f'\|_{L^2(-L,L)}^2+D_1^2\|f\|_{L^2(-L,L)}^2\}.
$$

真频率 $\omega_j=j\pi/L$ 的正弦与余弦分别正交，且每列的平方积分为 L。因此

$$
\|f'\|_2^2+D_1^2\|f\|_2^2
=L\sum_{j\in J}\frac{\omega_j^2+D_1^2}{(\omega_j+D_1)^2}d_j^2
\le L\sum_{j\in J}d_j^2.
$$

在补弧外 $Wf$ 及其一阶导数为零，故这个范数就是完整周期上的范数。于是得到式 (1) 的第一个界。这里分母中的 $D_1$ 很关键：未归一化的窗口乘正弦不能直接使用这个常数。

另一方面，完整周期余弦正交性给精确等式

$$
\|\mathcal A_Jd\|_2=\sqrt c\,\|d\|_2.
\tag{5}
$$

对混合算子使用三角不等式及反三角不等式，立即得到式 (1) 的上界及式 (3) 的第一个下界。

由于 $\Pi_J\mathcal A_J=\mathcal A_J$ 且正交投影范数不超过1，

$$
\|\Pi_J\mathcal T_{\lambda,J}d\|_2
\ge(1-\lambda)\|\mathcal A_Jd\|_2
 -\lambda\|\Pi_J\mathcal B_Jd\|_2
\ge\ell_\lambda\|d\|_2.
$$

同样的三角不等式给投影后的上界不超过 $u_\lambda$。证毕。

## 3. 当前 λ=.004 的严格范围

当前冻结窗口 $S=1/2$，所以

$$
K^2=\frac{2(c-S)}c=2-\frac3\pi.
$$

由经典有理上界 $\pi<22/7$，

$$
K^2<\frac{23}{22}<\left(\frac{41}{40}\right)^2,
\qquad
\lambda_*>\frac{40}{81}>.49.
$$

在真实 $\lambda=.004=1/250$，式 (4) 因而给

$$
\operatorname{cond}(\mathcal T_{\lambda,J}),\ 
\operatorname{cond}(\Pi_J\mathcal T_{\lambda,J})
<\frac{1+\lambda/40}{1-81\lambda/40}
=\frac{10001}{9919}<1.009.
\tag{6}
$$

这是解析有理比较，没有把浮点 SVD 当成严格界。它对任意有限 J 成立，包括 $J=\{1,\ldots,M\}$，以及固定第一 phase 控制后使用的 $J=\{2,\ldots,M\}$。后者仅说明这些曲率列对其相同高模投影不退化，尚未说明它们在传播到物理端口后仍独立。

R70 的有限列单射覆盖全部 λ；本条的定量好界只在式 (2) 的小 λ 范围内使用。不能将式 (6) 延用到 λ 接近1。

## 4. 与原核心切向空间的精确关系及边界

令 $\mathcal H$ 为完整周期上实、偶、零均值的 L2 函数空间。余弦合成算子
$\mathcal A:\ell^2\to\mathcal H$ 是乘以 $\sqrt c$ 的等距同构。式 (1) 使 $\mathcal B$ 从有限序列唯一延拓为有界算子，值仍在 $\mathcal H$：每列是奇周期相位的导数，其均值为零。

写 $Q=\mathcal A^{-1}\mathcal B$，则 $\|Q\|\le K$，并且

$$
\mathcal T_\lambda
=\mathcal A\{(1-\lambda)I+\lambda Q\}.
$$

在式 (2) 下，$\lambda\|Q\|/(1-\lambda)<1$，Neumann 级数给

$$
\mathcal T_\lambda^{-1}
=\frac1{1-\lambda}
 \sum_{n=0}^{\infty}\left(-\frac{\lambda}{1-\lambda}Q\right)^n
 \mathcal A^{-1},
\qquad
\|\mathcal T_\lambda^{-1}\|\le\ell_\lambda^{-1}.
\tag{7}
$$

因此 v4 无限列在这一 **L2 曲率切向空间** 上是满射。原完整 R53 核心在固定材料角、相位和中心规范下的任何光滑支撑参数变化，其曲率变化是偶函数，并因总转角固定而有零均值；故属于 $\mathcal H$，可在这个 L2 意义下由 v4 全部列表示。

这没有声称原有限支撑族的每个切向量恰好落在某个固定有限 M 的 v4 span；原支撑到材料角的反解一般产生无限 Fourier 谱。也没有证明式 (7) 的系数属于 R70 可选的四阶带权绝对可和空间，或有限截断在 C2 中以已知速率收敛。它只给已明确范数下的精确表示及有界逆。

对任一完整基准，核心二jet的参数变化还满足

$$
\delta\Gamma''=-e^{i\phi}\{\delta\kappa+i\kappa\,\delta\phi\},
\qquad
|\delta\Gamma''|^2=(\delta\kappa)^2+\kappa^2(\delta\phi)^2.
$$

所以完整材料角几何的二阶导数 L2 范数至少为曲率变化范数；本条下界并不依赖把基准近似成圆。但经过原状态 Fourier 截断、非线性材料图、径向 Frenet 传播和端口条件之后，还需实际计算其各自的响应，不能把本条的投影 $\Pi_J$ 换成另一投影。

## 5. 对当前求解能作出的判断

本条排除了一个特定解释：在真实连续材料角曲率范数、物理 phase 系数单位及同模曲率投影下，v4 的 λ=.004 列没有随 M 形成近核。它没有排除完整 BVP 的弱响应、径向传播的逆放大、非线性高阶余项、有限场缺陷或原域门造成的实际困难。

原 δ 设计改变完整物理 profile，产生径向方程的非齐次变化；这不属于本条的核心入口曲率变化。故式 (7) 不能用来推断 δ 方向必可由固定 g 的 phase 解方向吸收。该问题应看真实端口响应的伴随泛函，须与本条分开。

数学定义来源：[R68](R68-complement-interval-phase-controls.md)、[R70](R70-full-to-complementary-phase-homotopy.md)。数值评价实现为 `warm_homotopy_core_factory_v4.py`，SHA `f303897c231639b2dd68854d7bf37cc8862eea4e52b468d5be84c856e84fbcb5`。本条没有运行新的 BVP 或参数诊断，也没有改变任何部署源码与验收门。
