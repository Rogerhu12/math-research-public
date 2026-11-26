# R239：完整 Cartesian 目标的精确径向块结构与同一 LM 方程的预条件

**可信度：下文的局部支撑、带结构和变量代换是已证明的有限维代数结论；新的预条件器尚未实现或实际求解，不声称改善数值、连续 metric、曲率或 reach。**

这条结论专用于当前固定真实源、固定 $g$、固定 $A/Z$ 的 additive Cartesian 空间。它不把旧 phase/primitive 供应器的全局依赖误删为局部依赖。现行 CI 的源与目标均不修改。

## 1. 当前完整目标和局部支撑

实际实现入口是 `scripts/6a65-cartesian-complete-stream.py`（SHA-256 `b8cfd595b535cc33d47e2c0bc3e2b8d6a79c8163a235415115ca42c53416e4a9`）与 `scripts/6a65-cartesian-complete-point-operator.py`（SHA-256 `cf475476fb2b5e3a91d4438dd9dd67e54652bfd9594cc577b038ee2fd5e6f08f`）。每个训练点保留 3 个 full-Gram metric 行、3 个 R191 实际谱曲率行和 7 个 R219 几何 guide 行，共 13 行；所有权重已包含在 point JVP/JT 中。

令 $B_i$ 为当前物理径向坐标上的 quintic B 样条，内部结严格递增，已删除左右各三个端点列以保全部端口两 jet。令 $\psi_m$ 为一个允许的实角模，$c_m\in\{0,1,2\}$ 为它对应的 Cartesian 分量。变化为

$$
\delta X(s,u)=\sum_{i,m}x_{im}B_i(s)\psi_m(u)e_{c_m}.
$$

实际 weighted point residual 只依赖 $X,X_s,X_u,X_{ss},X_{su},X_{uu}$。其每一列在径向上的支撑都包含于相应 $B_i$ 的支撑。任一内部点至多有 6 个连续径向索引同时活跃。若 $|i-j|>5$，这两个列族没有共同的非零两 jet；支撑只在简单结相接时，相关两 jet 也为零。被删除的端点列不增大支撑。

这里 $J$ 指对物理 Cartesian 系数 $x$ 的 Jacobian，尚未乘 Sobolev 逆三角因子；现行 `linear.operator` 对应变坐标后的算子，其 normal 不应被误称为同一窄带矩阵。因此物理系数上的完整 Gauss--Newton 矩阵 $H=J^T J$ 满足

$$
H_{(i,m),(j,n)}=0\qquad (|i-j|>5),
$$

这里 $m,n$ 可任意不同，所有原行和列均在 $J$ 中。这个结论不是把小的 off-band 项阈值化为零，而是该 additive 基的精确支撑恒等式。冻结源本身在某点可以依赖全体旧参数；在当前 Cartesian 线性化中它是固定背景，这不会制造额外 Cartesian 列依赖。

当前 $J=80$、97 个角通道共 7760 列。按 `(radial index, channel)` 排序，完整标量下半带宽至多 $6\cdot97-1=581$。只计 float64 下带数组，7760×582×8 = 36,130,560 字节。形成它所需计算与条件数仍须评估；本条没有形成新的完整 normal，也没有运行一次新 LM。

## 2. 更小的精确角通道径向子块

先不形成所有角通道的交叉块。固定角通道 $m$，记 $L_{r,k,c}$ 为当前点第 $r$ 个 weighted residual 对第 $k$ 个 jet 的第 $c$ 分量的导数，jet 顺序为

$$
(k=0,1,2,3,4,5)=(X,X_s,X_u,X_{ss},X_{su},X_{uu}).
$$

定义三个实际 13 维列向量

$$
\begin{aligned}
h_{m,0}&=L_{:,0,c_m}\psi_m+L_{:,2,c_m}\psi'_m+L_{:,5,c_m}\psi''_m,\\
h_{m,1}&=L_{:,1,c_m}\psi_m+L_{:,4,c_m}\psi'_m,\\
h_{m,2}&=L_{:,3,c_m}\psi_m.
\end{aligned}
$$

于是完整该列为

$$
J_{:,im}(s,u)=\sum_{d=0}^{2}B_i^{(d)}(s)h_{m,d}(s,u).
$$

对实际全部角节点和全部 13 行求和，置

$$
Q_{m,de}(s)=\sum_u h_{m,d}(s,u)^T h_{m,e}(s,u).
$$

径向节点上的 $B^{(d)}$ 评价矩阵记为 $D_d$。该角通道的精确 normal 主子块是

$$
H_m=\sum_{d,e=0}^{2}D_d^T\operatorname{diag}(Q_{m,de})D_e.
$$

因为 $L$ 已用真实 point weights 加权，不能再额外乘一遍径向或角 quadrature weight。全部 13 行都进入 $Q$；非活跃 hinge 导数为零仅来自原 point 算式，不是删行。各 $H_m$ 对称半正定且径向带宽 5，可逐 radial block 累积。97 个 80×80 的 float64 下带只需 97×80×6×8 = 372,480 字节；无需保存完整 $J$ 或完整 $H$。实际实现可用 local JVP/JT 形成小的 13×18 点 Jacobian 后收缩，不需要为每个全局列调用一次完整算子。

这只是预条件所需的主子块。它**不能**代替真实求解中的全部跨角通道耦合；完整 $J$、$J^T$ 必须原样用于每次迭代。

## 3. 保留原 LM 正则而非暗换方程

现行 `BandedSobolev` 使用一个已由带状 Cholesky 验证正定的矩阵 $S=L_S L_S^T$，并用 $\delta=L_S^{-T}y$。当前有限步的 LM 二次问题是

$$
\min_\delta\;\|J\delta+r\|_2^2+\lambda\delta^T S\delta.
\tag{1}
$$

若改用实际块 $P=\operatorname{diag}_m(H_m+\eta S_m)$，$\eta>0$、$S_m$ 为同一旧 Sobolev 的相应正定主块，则 $P$ 正定。记 $P=L_P L_P^T$、$T=L_P^{-T}$。为了**保持式 (1)**，应对 $\delta=Tz$ 解下面的增广最小二乘，且设求解器附加 `damp=0`：

$$
\mathcal A z=
\begin{bmatrix}JT\\ \sqrt\lambda L_S^T T\end{bmatrix}z,
\qquad
b=\begin{bmatrix}-r\\0\end{bmatrix}.
\tag{2}
$$

其伴随必须是

$$
\mathcal A^T\begin{bmatrix}v\\w\end{bmatrix}
=T^T\bigl(J^Tv+\sqrt\lambda L_S w\bigr).
$$

直接在新坐标调用 `lsmr(JT,-r,damp=sqrt(lambda))` 会把正则改为 $\lambda\delta^T P\delta$，一般不等于 (1)。保持全残差零集不能掩盖这个有限步算法变化。

证明式 (2) 的 squared residual 正好是 (1)，只需代入 $\delta=Tz$ 并用 $\|L_S^T\delta\|^2=\delta^TS\delta$。因此新的预条件可改变迭代速度及有限迭代返回的方向，却不改精确线性化方程。以后若实施，应同时记录原坐标法方程残差

$$
\|(J^TJ+\lambda S)\delta+J^Tr\|_2
$$

以及完整非线性 Armijo 试步、实际退出和新的同场密观察；求解器迭代上限退出仍不得记为线性收敛。

## 4. 使用边界与下一实际证据

这条推导没有证明条件数一定改善，也没有证明当前差初值可收敛。高度集中的近退化曲率可能造成强跨角耦合，单通道块仍可能不足。新实现可独立准备并做非零有限算子核验；真实大模型实验须绑定其当时实际输入并记录自身基线，不得热改已运行 job 的冻结入口。

现有 [cold 首 Cartesian 步](../notes/2026-11-26-6a65-cartesian-cold-first-actual-acceptance.md) `run 45812620369` 的真实标量报告已有 7760 列/4,206,592 行、LSMR 80 次后 `istop=7`、随后真实 Armijo 接受。这里只引用已发表记录作为提出预条件方向的动机，不把该旧接受重新登记为新计算。原 M12 旁支的共同 H1 带状预条件不等于这里的 actual 13-row channel blocks；两者构造矩阵和消费的点残差不同，不能互相冒用实际运行结论。

任何基/角规则/source/g/guide 变化仍要登记自己的 baseline；改变预条件也要记录新的入口身份。对每个非线性 trial，原 13 行和全部 Cartesian 列保持，曲率、归一化 Gram 行列式、held 和其它几何指标继续真实计算。有限下降不是课题完成。
