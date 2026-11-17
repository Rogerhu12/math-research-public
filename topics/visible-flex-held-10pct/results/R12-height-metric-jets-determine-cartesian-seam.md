# R12. 高度二jet与度量一jet决定完整 Cartesian 接缝

构造会话：`true_a_analysis`；主会话 `Astra-held10-f00f08c9-20261117` 已逐式独立复核有向曲率符号、Gram分解、C²正则性及全周期ODE唯一性。这是一个完整的局部接缝定理；不假设已经完成本课题的全局曲面。

## 精确命题

设两张 C2 参数曲面在同一个参数环带的边界 `r=r0` 上写成

\[
X_j(r,u)=(Y_j(r,u),z_j(r,u)),\qquad Y_j\in\mathbb R^2,
\quad u\in\mathbb R/L\mathbb Z,\quad j=1,2.
\]

两边的参数 `r` 都取同一方向；必要时先将任意原前缀的 `s` 换成相同的 `r` 坐标。假设沿整条参数边界：

1. `z1` 与 `z2` 的二jet相同，允许先作一次固定竖直平移；
2. 两个第一基本形式 `g1,g2` 的一jet相同；
3. 水平投影的 Gram 矩阵 `h=g-dz⊗dz` 正定。

则存在一个固定平面欧氏等距变换，将第二张曲面的水平分量作用后，两个 `X` 沿整条边界的 Cartesian 二jet相同。若两水平投影具有同样的取向，这个等距变换可取平面旋转加平移；取向相反时再允许一个平面反射。

这里正定保证 `Y_r,Y_u` 线性独立，故其取向在连通的边界上恒定。结论不要求水平投影的整条闭曲线无自交。

## 证明

写

\[
h=E\,dr^2+2F\,dr\,du+G\,du^2,
\qquad d=EG-F^2>0.
\]

由前两条假设，`h` 的一jet也完全相同，因为

\[
h_{ab}=g_{ab}-z_a z_b,
\qquad \partial_c h_{ab}=\partial_c g_{ab}-z_{ac}z_b-z_a z_{bc}.
\]

令 `ε=sign det(Y_r,Y_u)`；若需要先作反射使两侧 ε 相同。沿边界曲线 `u↦Y(r0,u)`，速度为 `v=√G`。令 `T=Y_u/v`，`J` 为平面逆时针九十度旋转，则

\[
Y_u=\sqrt G\,T,
\qquad
Y_r=\frac{F}{\sqrt G}T-\varepsilon\frac{\sqrt d}{\sqrt G}JT.
\tag{1}
\]

由于 `Y_r,Y_u` 构成平面的基，直接对 `Y_a·Y_b=h_ab` 求导并解出分量，得到

\[
Y_{ab}=\Gamma^r_{ab}(h)Y_r+\Gamma^u_{ab}(h)Y_u,
\quad
\Gamma^c_{ab}=\tfrac12h^{cd}(\partial_a h_{bd}+\partial_b h_{ad}-\partial_d h_{ab}).
\tag{2}
\]

这一恒等式只用 C2 的 `Y`；无需调用更强正则性的平面局部等距延拓定理。特别地

\[
\Gamma^r_{uu}=\frac{G(2F_u-G_r)-F G_u}{2d}.
\]

采用平面有向曲率约定 `κ=det(Y_u,Y_uu)/|Y_u|³`，便有

\[
\kappa=\varepsilon\,
\frac{G G_r-2G F_u+F G_u}{2\sqrt d\,G^{3/2}}.
\tag{3}
\]

因此两条边界曲线有相同的速度 `v(u)` 及有向曲率 `κ(u)`。选取一个 `u0`，用平面旋转和平移令位置与单位切向量在 `u0` 一致。两条曲线都满足线性常微分方程

\[
T_u=v\kappa\,JT,\qquad Y_u=vT.
\]

这些方程的系数连续，解的唯一性给出整个参数周期上 `Y1=Y2`、`T1=T2`。公式 (1) 再给出相同的 `Y_r`，公式 (2) 给出相同的全部 `Y_rr,Y_ru,Y_uu`。结合已相同的高度二jet，所需 Cartesian 二jet相同。证毕。

## 可执行的有限误差桥接

上述精确命题不能把当前 FFT 采样误差自动变成连续 C2 接缝证书。但它指出了需要量化的全部项，也说明在 `h` 正定时无须额外引入独立的 Cartesian 边界方程。

对两个数值候选，取相同取向并在 `u0=0` 对齐初始位置及切向量。由测得的 `h` 一jet计算

\[
v_j=\sqrt{G_j},\qquad
\omega_j=v_j\kappa_j
=\varepsilon\frac{G_j(G_j)_r-2G_j(F_j)_u+F_j(G_j)_u}{2\sqrt{d_j}\,G_j}.
\]

若整个周期有连续上界 `|v1-v2|≤δv`、`|ω1-ω2|≤δω`，且 `v_j≤V`，则将切向角连续提升到实数后，

\[
|T_1(u)-T_2(u)|\le u\,\delta\omega,
\quad
|Y_1(u)-Y_2(u)|\le u\,\delta v+\tfrac12V u^2\,\delta\omega,
\]

\[
|(Y_1)_u-(Y_2)_u|\le\delta v+Vu\,\delta\omega.
\]

公式 (1) 的两个标量系数差再界住 `Y_r` 的误差。最后用公式 (2) 及两侧已量化的 `Γ(h)` 差界住全部二阶误差。只要 `G`、`d` 的共同正下界和 `h` 的一jet共同上界已支付，这些显式表达的误差传播常数均有限，可用区间运算计算。

在本题反射尾接口，必须先使用正确坐标链式法则：`r_s=σ/√E_tail`，`r_ss=−(E_tail)_r/(2E_tail²)`，物理高度为 `σ z_worker+constant`。均值与全部非均值 Fourier 模都一起变换；只核首模或者只核非均值不满足命题。

该引理只在接口附近水平投影正定时适用。它没有给出全局 reach、无自交、完整参数族或无限尾存在性，也没有把一个未精化的有限离散解升级为精确等距曲面。


更明确地，令 `a_j=F_j/√G_j`、`b_j=−ε√d_j/√G_j`，分别给连续差上界δa、δb，且 `|a_j|+|b_j|≤B`，则

\[
|(Y_1)_r-(Y_2)_r|\le\delta a+\delta b+Bu\,\delta\omega.
\]

令所有一阶向量范数不超过V₁，一阶向量差不超过δ₁，且对任意a,b有 `sum_c |Γ^c_ab(h1)|≤CΓ`、`sum_c |Γ^c_ab(h1)−Γ^c_ab(h2)|≤δΓ`，则由(2)

\[
|(Y_1)_{ab}-(Y_2)_{ab}|\le C_\Gamma\delta_1+V_1\delta_\Gamma.
\]

所有量均是两侧g一jet与z二jet的显式表达式。这给后续区间实现直接可用的误差链；当前低幅联立的有限采样数值并未被自动转换为这些连续上界。

实际有限联立的已完成记录见[前缀—尾联立笔记](../notes/2026-11-17-actual-prefix-tail-coupling.md)；相同参数方向和均值符号见[符号审计](../scripts/coupling/coupling_sign_audit.md)。
