# 五个实际 Hermite 查询的完整角域算子接口

日期：2026-11-14。状态：独立消费者已实现，只有本地源码读取、SHA 与 AST 检查；本文件不报告新的数值通过、优化步或完整曲面。计算只在本公开仓库自己的 GitHub Actions。

源文件：

- computations/geometry_20261114_full_angle_domain_operator.py
- 38319 bytes
- SHA256: af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7

本接口承接 R262 的完整局部链与 R265 的有限不等式模型。实际 request24 已说明为什么下一步需要五处完整角网格；新模型仍须在其自己的实际基点重新构造。调用者计划使用 request22 已保存的新 warm，SHA 03ca9477cbb759cdbf07117f2540aa51dbe07545985c957289d0f0a3079f4be8。不得把 request24 在更早 base20 上的导数移给这个新基点。

## 1. 固定模型与原 Jacobian 捕获

调用顺序是：

    capture = EndpointJacobianCapture(problem, state, intervals=INTERVALS)
    with capture:
        linear = CompleteLinearization(problem, state)
    domain = FullAngleDomainOperator(
        problem, state, capture, fraction=FRACTION,
        input_identity=actual_input_sha_dictionary)

其中 INTERVALS=(473,475,477,479,480)，FRACTION=0.17267316464601146；区间编号从零开始。构造者是原 CompleteLinearization，所有原物理行、完整右边界、core 与 scalar 自由度仍留在 A 中。

capture 只临时包住该实例的 flow.jac。它先调用原函数，再从原返回值保存需要的 J/P，最后返回原对象，不修改数值。退出时恢复原实例属性状态；若 jac 原来是继承方法，会删除临时实例属性。它要求捕获调用确实来自已锁源的 CompleteLinearization.__init__，同一次构造、同一个 state，以及实际节点和状态的逐字节身份。没有第二次全 699 节点 Jacobian 计算。

每个区间的两端必须在同一次原 node-Jacobian 调用中出现。原 chunk 在节点 480 相接，区间 479 与 480 因此各绑定其实际批次的节点 480。两个批次若产生相同 J/P 字节才合并保存；若不同则保留两个实际版本，不用第一个覆盖第二个。实际存储是九个节点，至多十个端点版本。

捕获保留全部 n×n 物理块和 n×k scalar 块，核原显式 physical-core 列及全部常值 RHS 行为零。所有数组保持原 float64，不把其他 dtype 静默转换。mesh、完整 augmented y/f、原 S、函数与依赖源码均有身份记录。

## 2. 完整 Gamma/Pi 与缓存行

每个查询先用原 CubicHermiteSpline 及实际两端 y/f 求原 augmented query。基线 beta_squared 使用原 normal-vector 公式。独立 cross-product 公式只用于 R262 的代数梯度及两表达式的差异记录，不代换原试探域值。

令 d=F_phi、e=F_phiphi、Q=d·d、v=d×e、W=v·v，a 和 nu 为原 scalar_jets 返回的半径和一阶字段。这里不假定有限 Gauss 半径的真实导数就是 nu。完整梯度是

$$
g_d=-\frac{6\nu^2Q^2}{a^2W}d
+\frac{2\nu^2Q^3}{a^2W^2}(e\times v),\qquad
g_e=\frac{2\nu^2Q^3}{a^2W^2}(v\times d),
$$

$$
g_a=\frac{2\nu^2Q^3}{a^3W},\qquad
g_\nu=-\frac{2\nu Q^3}{a^2W}.
$$

使用原 q.jet 对全部 n 个单位系数逐一求 D1/D2，同时编成五个完整 Gamma=g_d D1+g_e D2；不另造舍入不同的三角表、不把 q.project 误作 Euclidean 转置。Pi 同时包含控制对 a 与原 returned_ap 的直接贡献。没有除以 nu 的步骤。

对每个实际 cell，原 Hermite 权重为 h00,h10,h01,h11，原两端物理/参数 Jacobian 为 JL/JR、PL/PR。编译

$$
B_L^{\rm coeff}=h_{00}\Gamma+h h_{10}\Gamma J_L,\qquad
B_R^{\rm coeff}=h_{01}\Gamma+h h_{11}\Gamma J_R,
$$

$$
B_p^{\rm coeff}=h(h_{10}\Gamma P_L+h_{11}\Gamma P_R)+\Pi.
$$

同一个全局 p 的两端及直接项先合并，然后按全坐标 S 的相应列除一次。B 的输入为原 scaled direction z=S·delta_coordinates。所有 B_left/B_right/B_p 都已除过 S，调用者不能再除一次。

当前五个 cell 均远离 inlet，局部显式 core 列严格为零；完整 core 的优化作用仍在全 A。通用 cell 0 分支也显式保留 left×ExactCoordinates.inlet 的全部 free-core 链。

每个实际物理角索引都保留。N=2048、n=338、k=3 时，每组 rows 为 2048×679，五组共 55,623,680 bytes。全局坐标是 236036 维，局部列并集只有九个物理节点及三个全局 p，共 3045 列。不分配 10240×236036 的稠密矩阵。

## 3. 明确的调用 API

domain.beta_squared 是按声明区间顺序、每区间原 phi index 0..N-1 排列的 flat 10240 向量。原 beta 与 B 的行没有额外缩放。

domain.local_indices 是排序后的全局 scaled-z 列索引。domain.local_blocks 是 tuple(dict)，每项提供：

- rows：该查询的 N×679 只读实际 float64 矩阵。
- B_left、B_right、B_p：同一 rows 的已缩放只读视图。
- global_columns：该 rows 的全局 z 列。
- local_columns：对应 local_indices 的位置。
- row_slice：该组在 flat 10240 行中的 slice。
- interval、left_kind、left_column_count 和 Gamma/Pi 身份。

正向及转置接口：

    domain.matvec(full_scaled_z)
    domain.rmatvec(full_angular_dual)
    domain.local_matvec(local_scaled_z)
    domain.local_rmatvec(full_angular_dual)

正向和转置都只读同一份已冻结 rows。共享节点和全局 p 的转置贡献逐组累加，不发生覆盖。局部投影可一次计算 rows/C_local；后续每行或每 sweep 不再执行 Gamma@J。C 是调用者从完整原 A 得到的算法预条件对角，与 S 不同。

domain.operator(local=False|True) 提供相应 LinearOperator；当前调用使用一维实向量。description() 返回固定模型身份、全部 source/array hash、区间/行序/变量尺度、捕获端点版本和明确范围。

## 4. 实际实现核验与保全

    report = domain.verify(state, direction=actual_scaled_LSMR_direction)
    exported = domain.export(directory, row_chunk=256)

verify 对三组实际 B/B^T dot-product、local/full action 一致性做复核。它还对新实际 LSMR 方向及一条固定种子的局部物理/core/p 方向，从完整 ExactCoordinates 链提升为 augmented 方向，再在九个唯一实际端点调用原 complex RHS、原 Hermite 和原 normal beta_squared，独立对照完整 Bz。它不把 complex 输入送入会转实数的 chart.expand，也不重新构建全 Jacobian。

沿用已有实现阈值：转置/局部一致 5e-12，原 complex 完整链相对误差 5e-5。这是实现接线核验，未新增科学接受门，也不能替代原残差或原全部真实域判据。

export 把每组 rows、实际 Gamma/Pi、全局/局部索引和基线按最多 256 个角分块写 NPZ；另保存实际捕获的全部端点 J/P、原完整 y/f/mesh/S、identity manifest 和逐件 SHA。Gamma/Pi 实际字节保全后释放内存，后续只用缓存 rows。没有以 Git 单文件 5 MB 限制否决数学计算；最终发布/压缩/外部 artifact 保全由调用 workflow 负责。

## 5. 适用范围

这个新模块定义的是一次实际基点、原模型、原浮点数组所编译的有限 B。不同 BLAS/FFT 求和顺序的浮点方向作用不宣称逐位相同，实际 complex 核验记录其差异。

五处 N2048 行不等于所有 cell、两侧 RMS 点、连续角或连续曲面的域证书。原 node/midpoint/两组 RMS/rho 域检查、实际全方程残差和回溯继续执行。该模块不调用 native tail、不删高模、不截断实际 H，也不产生 accepted full parent。优化器即使找到这 10240 行的可行方向，仍须用完整原非线性函数检查实际步；它不因有限不等式通过就成为 R265 全 QP 的精确最优解。

