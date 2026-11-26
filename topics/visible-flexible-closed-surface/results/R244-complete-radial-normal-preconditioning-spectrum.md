# R244：完整物理径向正规带与保原 LM 的精确预条件谱界

日期：2026-11-26。会话：Astra-visible-flex-6a65。

本条接 [R239](R239-complete-cartesian-radial-block-preconditioning.md)。R239 的每角通道主块预条件器保持了原物理方程；本条进一步使用**全部角通道交叉项**的完整物理正规矩阵。以下是有限维精确代数证明，数值实现与大模型的支付范围另列，不把预条件谱界当作曲面存在或物理目标过门。

## 1. 固定模型、全部物理行与带状结构

固定同一真实源、目标度量 $g$、全部离散点、权重、guide 和 Cartesian 修正基。设完整加权残差为 $r\in\mathbb R^q$，完整物理 Jacobian 为 $J\in\mathbb R^{q\times n}$，

$$
H=J^\mathsf{T}J\succeq0.
$$

这里的“完整”包括 metric、曲率和几何的全部原十三行，以及所有实际 Cartesian 系数。原 Cauchy 的 $\rho,A,Z$ 设计列已固定在源中，不属于这组 Cartesian 变量。不能把非局部附加设计列误套进下面的带宽结论。

写修正为

$$
\delta X(s,u)=\sum_{i,m}c_{im}B_i(s)p_m(u)e_{c_m},
$$

其中 $B_i$ 为端口两 jet 消失的五次 B 样条基，$p_m$ 是给定 Cartesian 分量的实 Fourier 通道。每条物理行只依赖同一点的 $X,X_s,X_u,X_{ss},X_{su},X_{uu}$。其导数因而可写成

$$
J_{(s,u,r),(i,m)}=\sum_{d=0}^2 B_i^{(d)}(s)h_{r,m,d}(s,u).
$$

若 $|i-j|>5$，两五次基及其二阶以内导数在所有点的共同支撑为空；故 $H$ 的 $(i,j)$ 径向块严格为零。这个结论不删除任何非零小项。带内对所有角通道 $m,n$ 求和，不能再以“主块”名义去掉 $m\ne n$ 项。

设每径向层有 $C$ 个角通道，按 $iC+m$ 排列物理系数。标量半带宽为

$$
w=\min(6C-1,n-1).
$$

同一物理基上的多个完整采样组只把各组的 $H$ 相加，因此保持此带宽。增加仅依赖同一点物理 jet 的残差行也保持带宽；这并不自动证明一个尚未接入的多组或新增行实现正确。

## 2. 完整离散角矩的准确表示

在原均匀离散网格 $u_j=2\pi j/N$，令 $L_{r,I}(s,u_j)$ 为完整加权点行对十八个物理 jet 分量的导数。令

$$
C_{I,J}(s,u_j)=\sum_r L_{r,I}(s,u_j)L_{r,J}(s,u_j).
$$

指标同时含 Cartesian 分量和 jet 序号，所以 $xy,xz,yz$ 协方差不能删除。每个实 Fourier 通道均写成两个准确复指数项，常数通道只有一个非零项；一、二阶角导数分别乘 $i\ell$ 与 $-\ell^2$。

于是完整角收缩只需要

$$
M_\omega(s)=\sum_j C(s,u_j)e^{i\omega u_j},
\qquad \omega=\ell_m+\ell_n.
$$

它是完整有限离散和。$C$ 无须是有限带限函数，也不需要连续 Fourier 尾估计来证明这个离散恒等式。rFFT 使用负指数；取正频率矩要取相应共轭，负频率及超过半网格的频率须模 $N$ 后按正确半区读取。若 $N>2M$，两个基通道产生的频率仍可能大于 $N/2$，不能截去。全部径向、角通道、Cartesian 分量和导数组合如此收缩后，得到原完整有限 $J^\mathsf{T}J$。

本条只证明离散目标的恒等表示；不声称该有限角和已经给出连续曲面的积分或最大值证书。

## 3. 保留原物理 Sobolev LM 二次项

令原预条件坐标对应的物理正则矩阵为

$$
S=L_S L_S^\mathsf{T}\succ0.
$$

实际模型的 LM 阻尼为 $\lambda>0$，原物理二次问题为

$$
\min_{\delta\in\mathbb R^n}
\|J\delta+r\|^2+\lambda\delta^\mathsf{T}S\delta.
\tag{1}
$$

独立选预条件参数 $\eta>0$，取

$$
P=H+\eta S\succ0.
\tag{2}
$$

取任意可逆 $T$ 满足 $T^\mathsf{T}PT=I$。例如 $P=L_P L_P^\mathsf{T}$ 时取 $T=L_P^{-\mathsf T}$。允许用正对角矩阵 $D$ 做合同缩放：若

$$
DPD=L L^\mathsf{T},
$$

则 $T=D L^{-\mathsf T}$ 仍满足同一白化关系。这个缩放没有改变物理 $P$。

令 $\delta=Tz$。因 $T$ 可逆，(1) 等价于

$$
\min_z\left\|
\begin{bmatrix}JT\\\sqrt\lambda L_S^\mathsf T T\end{bmatrix}z
-\begin{bmatrix}-r\\0\end{bmatrix}
\right\|^2.
\tag{3}
$$

定义增广算子 $\mathcal A$ 为 (3) 左矩阵。若用 LSMR 解 (3)，额外 `damp` 必须为零；不能在已增广的原 $\lambda S$ 之外再加一个坐标正则项，更不能用 $\lambda P$ 替换原 $\lambda S$。

完整伴随为

$$
\mathcal A^\mathsf T(v,w)
=T^\mathsf T\bigl(J^\mathsf T v+\sqrt\lambda L_S w\bigr).
$$

物理方向的原正规方程残差为

$$
J^\mathsf T(J\delta+r)+\lambda S\delta.
\tag{4}
$$

报告 (4) 可直接审查原方程，不用坐标变换后的停止指标冒充物理精度。

## 4. 完整 $H$ 给出的精确谱界

**命题。** 在 $H\succeq0,S\succ0,\lambda>0,\eta>0$ 及 $T^\mathsf{T}PT=I$ 的假设下，令

$$
\alpha=\min(1,\lambda/\eta),\qquad
\beta=\max(1,\lambda/\eta).
$$

则

$$
\alpha I\preceq\mathcal A^\mathsf{T}\mathcal A\preceq\beta I,
\tag{5}
$$

从而

$$
\kappa_2(\mathcal A^\mathsf{T}\mathcal A)
\le\max(\lambda/\eta,\eta/\lambda),
\qquad
\kappa_2(\mathcal A)
\le\sqrt{\max(\lambda/\eta,\eta/\lambda)}.
\tag{6}
$$

**证明。** 若 $\lambda\le\eta$，则

$$
(H+\lambda S)-(\lambda/\eta)(H+\eta S)
=(1-\lambda/\eta)H\succeq0,
$$

$$
(H+\eta S)-(H+\lambda S)=(\eta-\lambda)S\succeq0.
$$

所以 $(\lambda/\eta)P\preceq H+\lambda S\preceq P$。若 $\lambda\ge\eta$，同样有

$$
(H+\lambda S)-P=(\lambda-\eta)S\succeq0,
$$

$$
(\lambda/\eta)P-(H+\lambda S)
=(\lambda/\eta-1)H\succeq0.
$$

两种情形合并成 $\alpha P\preceq H+\lambda S\preceq\beta P$。对其作 $T$ 的合同变换，并用

$$
\mathcal A^\mathsf{T}\mathcal A
=T^\mathsf{T}(H+\lambda S)T,
$$

立即得到 (5)。因为 $\alpha>0$，其特征值比与 $\mathcal A$ 的奇异值比给出 (6)。证毕。

该界不含径向层数、角通道数或 Jacobian 的坐标单位。前提是**完整** $H$ 和同一个原 $S$；每角通道主块近似不满足这里的恒等式，不能借用此界。

### 阻尼和预条件参数相等

若 $\lambda=\eta>0$，则 $P=H+\lambda S$，故

$$
\mathcal A^\mathsf{T}\mathcal A=I.
$$

这是精确代数白化，原 LM 方向为

$$
z_*=-T^\mathsf{T}J^\mathsf{T}r,
\qquad
\delta_*=-TT^\mathsf{T}J^\mathsf{T}r
=-(H+\lambda S)^{-1}J^\mathsf{T}r.
$$

它不保证有限精度组装后的带因子也达到精确白化，更不免除真实非线性值与接受判据。

### 无正则问题 $\lambda=0$ 的边界

若 $\lambda=0$，即使 $\eta>0$、$P$ 可逆，也只能保证

$$
0\preceq T^\mathsf{T}HT\preceq I.
$$

一般没有严格正下界。例如 $H=\varepsilon S$ 时，全部特征值为 $\varepsilon/(\varepsilon+\eta)$，可随 $\varepsilon\downarrow0$ 趋于零；$H=0$ 时全部为零。若 $H$ 有核，可逆坐标变换不会消掉这个核。

因此本条不能把 (6) 借给原 M12 的无正则最小二乘路线。该路线可把带矩阵用作可逆右预条件器，但仍须保留原无正则目标并重新审查其真实算子和收敛；非唯一解下的坐标最小范数选择也不由本条固定。

## 5. 实现和支付边界

独立实现为 `scripts/6a65-cartesian-complete-radial-normal.py`，不改当前活动 v5。它以完整物理点协方差装配下带；使用正对角合同缩放、带 Cholesky 和保存因子的三角带求解，不形成稠密生产 Jacobian 或稠密生产正规矩阵。

一个新的 91 非零列完整有限核已真实运行，独立回执见 [实际小核](../notes/2026-11-26-6a65-solver-complete-radial-normal-actual-finite-check.md)。小核检验了全部跨角与跨 Cartesian 项、实际 FFT 别名、同一原 LM、伴随和原坐标正规残差。

精确代数论证与实际浮点验证必须区分：本文没有给完整装配舍入误差的区间证书；未支付生产 7760 列的大模型成本、真实 Cauchy 输入的数值稳定性或任何新非线性接受。两组采样和第十四面积行保持带状结构只是本节定理的适用形式，实际接口尚需另行接入和验证。连续 metric/reach、共同 $g$ 的曲面族、同场精化与课题其它完成门槛均未由本条解决。
