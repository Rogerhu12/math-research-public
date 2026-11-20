# R681 的隐式 coarse frame 与完整 SPD 应用接口

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / fullclosed_solver。

## 状态与源码

本条实现 [R681](../results/R681-current-J-coarse-frame-preconditioning.md) 的第 3、4、7 节小模块。源码为 [full_phi_coarse_frame.py](../scripts/resume_20261120/full_phi_coarse_frame.py)，20075 bytes，SHA256：

`324513a115a61800e105f340bd070eb50931bbe16dd66d3a8643bfe11298f2da`。

本次只写源、读既有源码逐槽核对并用标准库 AST 解析；没有 import 本模块或运行科学代码，没有数值伴随检查、fixture、场读出、J/JT、粗 Hessian 组装或求解。本模块未接入任何已运行方向，没有预排公开 Actions。它不提供 PCG/full-QP driver，也不实现 R681 的角矩组装程序。

导入只加载依赖并定义函数/类。所有公开数值构造和应用均检查 `GITHUB_ACTIONS=true` 与 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。后继实际执行只属于本仓库公开 Actions；AST 通过不是数学/数值误差证书。

## 同一原坐标映射及其转置

输入为当前原 `DoubleIntegrated` 对象 `di`、用同一 `di` 构造的 `PhysicalHeight` 对象 `height`、当前 literal `ThreeJetSpace` 对象 `basis`，以及当前调用者已经使用的 `diagonal, chol`。不重新选尺度、白化、粗列或高度补偿。

记 $S$ 为 `di.scale` 的对角矩阵，$A_H=I+v_qe_H^T$，$D=\operatorname{diag}(\mathtt{diagonal})$，$L_N=\mathtt{chol}$。模块保留

$$R=D^{-1}L_N^{-T},\qquad U=BR,$$

$$Qa=S^{-1}\mathrm{DI.inverse}(A_H^{-1}BRa;\mathrm{affine=false}).$$

`integrated_inverse_transpose(di, w)` 是 `DI.inverse(..., affine=False)` 本身的准确声明转置，未混入 `scale` 或高度映射。它先展开全部 core/A/E/D/H 槽：E 对相邻 A 各减一半，对 U 作 $\pm1/h$ 差分；D 对 U 各减一半，对 Y 作 $\pm1/h$ 差分。最后按真实自由布局收回，保留所有自由 core 的 $g_{Y_0,R}-\nu g_{Y_0,T}$ 项、自由初始 A、内部三 jet 和 H。固定端口 covector 按原 unpack 的转置丢弃。它不是 `DI.raw_transpose` 或 `DI.pullback`。

`CoarseFrame.qt(u)` 依次应用 $S^{-1}$、上述局部差分转置、$A_H^{-T}$、原 `basis.transpose_free` 和 $R^T$。其中 $A_H^{-T}g$ 的 H 分量为 $g_H-v_q^Tg$；这个减号与正向使用 $A_H^{-1}$ 配对。Q/QT 都作用于同一声明的完整线性映射，不在一侧额外加端口投影。

原 literal basis 的 `free_direction/transpose_free` 是实数 QP 接口，因此 frame 与 SPD 应用明确只收实向量，避免向复数输入静默丢虚部。单独的 `integrated_inverse_transpose` 保持输入复 dtype，但本次没有据此新增检查。

## 实际母 Gram 与一般 K 修正

`literal_mother_gram(di, basis)` 按当前 basis 的径向三 jet 与 R/T/Z 系数分离，直接使用 **实际 `di.scale` 每个槽** 形成

$$G_N=(S^{-1}\mathrm{DI.inverse}(A_H^{-1}B))^T(S^{-1}\mathrm{DI.inverse}(A_H^{-1}B)).$$

它复现原 `free_direction/unpack` 的端口限制：所有粗列不改变自由 core-c，初始 Y/U 与末端全部三 jet 固定，A0 仅 R/T 自由。最后一列准确使用同一个 H=1 高度方向，故 $A_H^{-1}$ 后只余 H。构造器用原最后一列逐值绑定现有 `height.compensation`；没有用理想连续 $b$ 代替实际 nodal $b-h$。因此原 lift 与 R671 新 lift 可共用这一接口，但调用者必须传本次实际模型的同一 basis/height。

本接口的 basis 契约就是已刊 `ThreeJetSpace`：每列一个径向三 jet 与一个系数 channel，唯一最后一列改变 H，所有 leading free core-c 系数为零。`global_core_second_jet` 的 A0 列保留。接口不把未来任意含 core-c 的新粗列冒作这个分离公式。

随后用调用者原来的 R 计算

$$K=R^TG_NR,\qquad E=K+K^2=L_cL_c^T,$$

$$W=\begin{bmatrix}Q\\K\end{bmatrix}L_c^{-T},\qquad
W^T=L_c^{-1}\begin{bmatrix}Q^T&K^T\end{bmatrix}.$$

没有从原 Cholesky 反向定义必然白化的 $G_N$，没有把实际 K 强设为 I。浮点 K/E 只作对称化，并记录原最大反对称项、K 距 I 最大差和小 Cholesky 对角；不加 ridge、jitter、截断或删列。准确算术中的正交结论不被标成浮点向外证书。

Q 始终通过原 B 和 DI 的应用生成向量；不保存 `integrated_variables × coarse_variables` 大矩阵，也不扫描任何全变量单位向量。新增持久存储为若干原长度向量和 coarse 阶小矩阵。

## 小数据 Hessian 的输入单位

`frame.small_hessian(Gc, mu)` 的 `Gc` 必须是本轮实际完整正谱 Hessian 在 **当前 $U=BR$ 系数** 中的数据 Gram：

$$G_c=A_c^TA_c.$$

这里 $A_c$ 已包含本轮原全观测行、同角轨道权、径向权及完整 normalized-Phi 外侧比例；当前 p=8、scale=.05 的外侧平方比例为 $1600/C_0$。`Gc` 不含 damping，不是原 B 系数下的矩阵，也不是早先 Jw 的正规矩阵。当前 R664 Hessian 正块必须保留；不能拿梯度用正块或旧范数的 coarse 白化代替。

模块不自行组装或重新验证这一数据身份。调用者在 `data_provenance` 绑定实际父 bundle、完整 bridge、行/权、模型与当前 U 的源码/参数身份；返回 metadata 明示 `current_data_identity_checked_by_this_helper=False`，不会伪称读过这些数据。

返回的小矩阵准确声明为

$$H_c=\mu^2I+L_c^{-1}(I+K)G_c(I+K)L_c^{-T}.$$

mu 是当前原 QP 的实际正 damping，既不重标度，也不改变原 $\mu^2\|z\|^2$ 母范数。不能由此声称改进了现有实际方向或已测得条件数。

## 最小调用与失败语义

下面是后继公开 Actions 中的接口示意，尚未执行：

```python
frame = module.CoarseFrame(
    di, height, basis, diagonal, chol,
    provenance=actual_frame_source_and_model_records,
)
Q_a = frame.q(a)
QT_u = frame.qt(u)
W_a = frame.w(a)
WT_z = frame.wt(z)
preconditioner = module.FixedSPDPreconditioner(
    frame, Gc, actual_mu, explicit_positive_beta,
    data_provenance=actual_current_data_records,
)
direction = preconditioner.apply(original_augmented_covector)
```

其完整应用为

$$\mathcal B=\beta(I-WW^T)^2+WH_c^{-1}W^T,\qquad\beta>0.$$

两个 $(I-WW^T)$ 应用都保留，因而 R681 第 7 节的 SPD 证明不依赖机器中 W 逐项正交。正向/转置沿同一公式，Hc 用 Cholesky 解。beta 必须由调用者显式给定并在本轮固定；本模块没有自动 beta/mu 选择。

未来若接固定活动面，应在原 Euclidean QP 坐标使用 $P\mathcal BP$ 和正确 PCG 内积，保原真实步长限制、全部不等式及 R668 释放。这里不实现该驱动，也不改任何永久几何记忆或非线性回溯。

`try_prepare(...)` 提供可选构造：实际小矩阵非有限或 Cholesky 不可用时返回 `(None, failure_record)`，调用者可明确继续原 solver。它不加数值补丁、不把小解失败说成物理不可行，也不让一项新检查成为原科学入口的前置门。布局/来源接口误用仍明确报错。应用时若小解失效，会抛 `SmallSPDUnavailable`；不能在进行中的 PCG 链内静默替换为 identity，若决定回退则必须显式重启。

本次产物是一个可复用的小映射模块；是否使用、实际耗时、伴随误差、数据小 Gram 质量和求解收益都尚未运行，仍由后继真实返回及原六方向归因决定。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
