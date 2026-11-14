# 自由高模 cut-height 的仿射 prefix 初猜

状态：**辅助初猜方法，输出一律 UNSOLVED；不是真 DN 或本题新解。** 作者 `/root/coupled_prefix`，2026-11-09。实现 `scripts/db6f-prefix-affine-lift.py`。

M15 的初始嵌套流程在 prefix 有机会改变切口高度前，先求旧 M14 切口高度补零后的真 DN。这一特定 Dirichlet 子问题出现强阻尼，不排除允许切口高度共同变化的 joint 解。本辅助步骤只预测新切口，随后必须回到原 M15 非线性 DN 与原边界残差。

令 M14/N512 完整成功响应的物理切口高度、斜率和已存斜率 Jacobian 为 $H^{(0)}\in\mathbb R^{14}$、$S^{(0)}$、$J_{14}$。新增第15模的物理波数为 $m=3\cdot15=45$，其线性斜率系数 $d_{15}$ 读取同一冻结 `linear-port` 的 `linearSlope[14]`；使用的单位是物理 $dS_{15}/dH_{15}$，不再乘 Fourier 次数或 momentum 归一因子。

定义辅助切口斜率

$$
\widehat S(H)=
\begin{pmatrix}S^{(0)}\\0\end{pmatrix}
+\begin{pmatrix}J_{14}&0\\0&d_{15}\end{pmatrix}
\left(H-\begin{pmatrix}H^{(0)}\\0\end{pmatrix}\right).
$$

低模/新增模交叉块明确定义为零；这只是初猜的选择，不是关于真实 M15 DN 交叉导数为零的断言。旧低模锚点来自完整真 N512 校正响应，新模用同 g 的冻结线性 port。该 surrogate 只返回斜率及其 Jacobian，拒绝任何 audit 请求；其他两jet/均值行是未使用的占位，不是认证数据。

prefix 原未知量为 $Y$，切口物理高度 $H=\sigma qY_z$。保留原 boundary 形式

$$
q\,\partial_sY_z-\widehat S(H)/\sqrt{E_{\rm cut}}=0,
$$

并保持原 `bcweights`、$\sigma$、$q$ 标度和链式 Jacobian：在高度列减去 $\sigma q\widehat J/\sqrt E$。仍使用原 `TailMixin`，没有额外重新推导或更改实际边界的符号。

物理 profile、chart、`warp_reference_q`、无限尾定义和 phase 范围原样读取已完成 M14 CP；保存网格的有符号模 padding 仅用于 warm。前缀 Fourier 阶数增加到 M15，angular 512；原 BVP `tol=2e-9`、原边界容差不变。`projectionFloor=.05` 仅记录，不在辅助 BVP 中运行 tail root，也不修改未来真 DN 的该 guard。

保存的 CP 显式 `actual_nonlinear_tail=False`、`frozen_affine_dn=True`、`status=UNSOLVED`。`solver_success` 只指辅助仿射 BVP；不能将其称为完整联解。报告包括预测前后的全部物理 cut-height、新模幅度、仿射斜率、原 prefix metric 诊断和节点/RMS。即使这些指标良好，也必须以新切口为目标，从原同 g 状态初猜重新做真实 DN，最终按原方程校正并审计。

不可变 `-input-bindings.json` 在计算前只写一次；完整 `-reproduction.json` 在结束后写入，避免把活动 metadata 的旧 hash 当永久冻结输入。所有输出使用独立 stem，既有 source/FAILED CP 不改。
