# 已存 gamma-H KKT 矩阵的完整只读归因入口

本条新增一个小矩阵读取器，不重演求根，不改变任何数学输入或算法参数。它只在公开 Actions 中消费未来实际返回的同一个 gamma-H 科学报告：driver 8f37529deaa8e07d4561e00371b39b82cb641a4e52e0790d41555b2ae9e320a9、完整 operator b712a24a0c0223356b4a53e6aa1fa78ba9cea66e4be39c7ee39931be99cb782a。原报告、矩阵和控制向量留在 runner；这里只生成紧凑标量、真实来源和字节身份。尚无本读取器的科学返回，下面不填未来报告或矩阵 SHA。

## 1. 消费的实际证据与缺项

源码为 scripts/resume_20261126/read_actual_gamma_height_kkt_matrices.py，完整 SHA256 为 **b3d424b30563ad883b3dcbed8aa82537138243a1b7a12a93baf9045b2316347d**，28250 bytes。

先调用字节锁定的 c3fdd83c29dabeb00974899bb183360da01c57fcf364704759efcc1ac643b9ec 完整纯 reader，复核 driver、所有源角色、准确目标、原 reference、字面 Q、显式 H 初点、全部已存短快照和报告的成功/失败语义。前后报告 SHA 必须一致。这里不 import 实际物理算子，也不构造 F、J、参考积分、Q 或 checkpoint。

真正矩阵来源限于
latest_operator_metadata.endpoint_continuation_last_batch.stages[*].angle_records[*].last_evaluated_KKT_matrix。
b712 只在失败 stage 保存它已经计算过的最后一个矩阵。该记录自带 current_full_point_sha256、local_angle_index、continuation_parameter_target、newton_iteration、当时的九维 state、九维 shifted residual 和完整 9×9 matrix。读取器逐一把这些字段和外层 batch/angle/target 对上，再计算任何矩阵代数。

一个矩阵所在的状态可能早于该 failed stage 最后返回的状态。两者分别哈希并逐字比较；不把较早矩阵叫成较晚状态的 Jacobian，也不把两者残差混合。材料角只按原 canonical float.hex 字读取。

未保存矩阵的失败 stage 计数保留，明确没有矩阵可读。没有原报告、没有 actual operator metadata、没有 batch 或没有任何 saved failure matrix，各自返回明确 unread 状态，不造零矩阵，不重新调用科学算子补数据。只覆盖原报告保存的最后 batch，不宣称恢复了此前未保留的所有失败批次。成功 stage 没有 failure matrix 是该源的正常行为，不是一个隐含的非奇异结论。

## 2. K 的准确块意义

同一准确控制定义中 $u=(z/S,v)\in\mathbb R^6$，$f=C/S\in\mathbb R^3$，九维 KKT 方程为
$$
R(u,\ell)=
\begin{pmatrix}u+f_u^T\ell\\f\end{pmatrix}.
$$
所以其零阶 Jacobian 是
$$
K=\begin{pmatrix}L&A^T\\A&0\end{pmatrix},
\qquad
A=f_u,\quad
L=I+\sum_{k=1}^3\ell_k\,D^2 f_k.
$$
代码从原记录的 raw K 直接取 A=K[6:,:6]、L=K[:6,:6]，并分别报告 K、L 的不对称缺陷、右上块与 A 的转置差、右下零块缺陷。K 的奇异值始终使用完整 raw K，不把对称化替代原矩阵。

以下是解释诊断时使用的精确线性代数条件，不是当前候选的证书。假设 A 的行秩为3，Z 的列构成 ker A 的正交基，则
$$
K\text{ 可逆}\quad\Longleftrightarrow\quad Z^T L Z\text{ 可逆}.
$$
若 $K(x,\lambda)=0$，则 $Ax=0$，故 $x=Zv$；左乘 $Z^T$ 得 $Z^TLZv=0$。若此限制可逆，则 $x=0$，而 $A^T$ 单射给 $\lambda=0$。反之，若非零 $v$ 属于限制的核，则 $LZv$ 与 $\ker A$ 正交，故存在 $\lambda$ 使 $A^T\lambda=-LZv$，从而产生 K 的非零核。这证明等价。它只要求限制可逆，不要求正定。只有在完整可行驻点及其它相应假设下，正定限制才可用于二阶充分条件；一个辅助 stage 的值不证明 SOSC，更不证明全局最小。

因此 A 的样本仍有良好行秩，而限制 L 接近奇异，可以提示驻点选择机制的困难；A 本身退化则有不同含义。普通浮点样本、一个失败状态或这些标量不能独自给出故障因果或连续全域结论。法向选枝仍须支付自己的整条路径和有限步 Jacobian；本诊断不承诺它成功。

## 3. 实际浮点输出与范数

所有新数值运算仅为 runner 上的 9×9/3×6/至多6×6 SVD、对称特征分解和一次 K 的线性求解。没有新 field、closure、Hessian、J、root 或 integral 计算。对每个真实保存的矩阵：

- 取 A 的全部三个奇异值及条件数；数值秩惯例明确为 singular_value > max(shape)·eps64·largest_singular_value。此阈值只用于诊断，不成为 solver 接受门或精确秩声明。
- Z 使用完整 SVD 中低于此秩切分的全部右奇异方向；若数值秩低于3，不把多出来的核方向删掉。报告 A Z 残差及 Z 的正交缺陷。
- 计算 Z^T sym(L) Z 的最小、最大、最接近零的特征值与惯例下符号计数。L 的对称化改动单独报告，不能藏入“准确 Hessian”的说法。
- 取完整 raw K 的最小/最大奇异值、条件数与同惯例数值秩。
- 用同记录的 shifted residual 解 K d=r，报告线性残差、相对后向残差、d 的范数及 state−d 的控制/乘子范数和原域比较。它不评估该候选的非线性残差，也不声称该未截断 Newton 步会被接受。

SVD/eigen/solve 不可得或给非有限结果时，保留不可得状态，不补零或伪造分解。精确秩、SOSC、连续根分支、全题不存在性、metric/reach/嵌入证书标志均为 false。

矩阵状态记录的 r 是
$$
R(u,\ell)-(0_6,(1-\tau)f(0)).
$$
原源已核初始 stationarity 六分量为零，所以前六分量就是原 stationarity。末三分量在 tau<1 时仍是辅助方程的残差，绝不叫成原闭合残差；只有 tau=1 才输出同状态原物理端点残差。dimensionless 端点量乘源使用的同一 S carrier 才成为物理长度。该 carrier 只由已有 FullHold S 有理盒按 a1ed 的准确 midpoint 规则读取；4e context 已在构造时核其等于实际 mesh[-1]。不新增标量积分，也不把 carrier 当成已包围的精确 S。

## 4. 完整覆盖和紧凑发布

读取器处理该实际存储 batch 的全部已有矩阵，不按条件数筛选计算。输出记录完整保存/缺失/成功 stage 的计数、全部紧凑标量行的 SHA，以及全集合的极值。为保持发布小文本，只附至多五个原样标量代表：A 最小奇异值最小、K 最小奇异值最小、限制特征值最靠近零、限制特征值最小，以及记录顺序的最后矩阵。每个代表都含实际 source/report/model/current point/angle/target 所属关系或其已核全局身份，以及原矩阵、原 state 和 residual 的哈希；不输出原矩阵、控制、乘子或奇异向量。

所有可用矩阵均先处理，再选择发布代表。若没有真实矩阵，所有极值仍缺省/空，不把空集解释为零残差、正定或不存在故障。

## 5. 可运行入口和未返回边界

独立 ready 为 actual-gamma-height-saved-KKT-matrix-run05-ready.json。读取对象是实际科学步骤 complete-added-gamma-nine-KKT-explicit-H-full-history-first-20261126-05 的
{work}/zero-closure-added-gamma-KKT-explicit-H-first/report.json；
输出为
{work}/postprocess/zero-closure-added-gamma-KKT-explicit-H-saved-matrix-readout.json。
全部 summary selectors 都指向标量。parent_bundle 使用已经存在的 reference.npz，不依赖科学步骤是否产生 final。

命令只包含 repo、report、output；若实际报告 SHA 已知，还可显式给 --report-sha256。此请求排在该科学结果之后；它不是新的前置 fixture，不推迟完整新方向，也不修改已失败报告。未来实际 input report/batch 身份留空，不能预填。

本轮环境不可用，源经过完整文字/真实源身份比对，solver 独立读了矩阵分块、数值核空间、残差单位和 own-state 合同。没有声称执行了 AST、compile、fixture 或任何科学求值。
