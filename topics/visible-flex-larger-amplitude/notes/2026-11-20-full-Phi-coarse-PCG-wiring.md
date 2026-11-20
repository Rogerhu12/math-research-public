# 当前完整 Phi 方向的可选粗空间 PCG 接线

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / geometry_path。

本文件记录一个独立源派生器的实际接口。没有在本地构造矩阵、求解 QP、读取候选几何或运行数值 fixture；它也不是任何候选的收敛、等距或 reach 结论。

## 1. 完整源与接入位置

新源 [augment_full_phi_coarse_pcg.py](../scripts/resume_20261120/augment_full_phi_coarse_pcg.py)，16,827 字节，SHA256：

`f96cb48933d1356b97b5a687d25cc05cd33188b08c14cd0b439f170b027fce18`。

唯一公开源编辑接口为：

```python
derived_text, metadata = augmenter.augment_driver_text(validated_text)
```

`validated_text` 必须来自调用方已经严格绑定的完整 driver 与已声明的前置变换。此函数没有替代父源绑定器，也不把“几个锚点能匹配”当作科学源真实性证明。当前组合次序为冻结原场或 R671 driver、冻结 exact-location 变换、冻结 SOC 变换，最后本 PCG 变换。下一父的消费者必须从同一冻结链重新生成完整 AST，并核实际源文件与报告 SHA；不能把新复合源送入只接受旧 SOC 的绑定分支。

输出使用常量 header，没有 scratch 路径。运行报告中的 `coarse_preconditioner_derivation.authenticated_input_body_sha256` 绑定输入的 canonical AST 文本；函数返回的 metadata 另记本次输入原 UTF-8 文本 SHA、输出文本和 AST SHA。这使前置源注释里的路径不影响数学 body 身份，同时不丢失实际文本来源。

对两个冻结完整 driver 与两个 SOC 完整派生 body，已完成源编辑、AST 解析和 `compile`，每个预定锚点各匹配一次。没有导入 NumPy/SciPy 科学模块或执行任何生成的 driver。匹配锚点为参数、两个运行 helper、源设置、总报告、唯一 QP 调用及方向报告；没有修改残差、模型、约束行、线搜索、SOC 修正或阻尼更新公式。

## 2. 显式参数与冻结依赖

新 driver 参数只有：

```text
--enable-coarse-preconditioner
--coarse-frame-source PATH
--coarse-moments-source PATH
```

启用开关缺省为 false。启用时必须显式提供两个组件源，目标必须为原完整 spectral Phi；现有 `--qp-source` 必须选择下表 v4。v4 同目录的冻结 v3 也会在求解前核实，并通过 `v3_source` 显式传入。没有新 beta 调参选项，也没有新方向、迭代或时间预算。

| 角色 | 完整文件名 | SHA256 |
|---|---|---|
| 粗坐标框架与 FixedSPD | `full_phi_coarse_frame.py` | `324513a115a61800e105f340bd070eb50931bbe16dd66d3a8643bfe11298f2da` |
| 当前完整 Phi 粗 Gram | `full_phi_coarse_moments.py` | `da083ae9b20674a29121c25d5b57ef867fba442559a50791b7fc0b43d4db5719` |
| 可选固定预条件 PCG | `fullspace_feasible_active_pcg_v4.py` | `dd59510599334843cf79159cafe5d2548818ab8b7fdf6813f164ee811247ad3b` |
| 无预条件直接委派对象 | `fullspace_feasible_active_cg_v3.py` | `fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4` |

这些实际路径和 SHA 写入总报告的 `source_paths`、`source_sha256_by_role` 与 `coarse_preconditioner_setup`。关闭时不加载两粗空间组件，向原 `qp_module.solve` 传入空增量关键字，保留原 QP 调用；若调用方选择 v4，v4 的 None 路径直接委派冻结 v3。

## 3. 每个方向确切使用什么

构造位置在当前 `problem.set_base(x)`、完整 R664 bridge 和原 `A` 已建立之后、唯一 `qp_module.solve` 之前。使用当前实际的：

```python
frame = frame_module.CoarseFrame(
    coordinates, height_map, basis, coarse_diagonal, coarse_chol,
    provenance=provenance)
Gc, data_report = moments_module.assemble_current_coarse_gram(
    bridge, frame, stage_block=8,
    provenance=provenance, progress=progress)
preconditioner = frame_module.FixedSPDPreconditioner(
    frame, Gc, damping, 1. / damping**2,
    data_provenance=data_report)
```

这里 `damping` 是本方向实际的可变局部变量，已包含先前方向的真实阻尼更新；不是重新使用 `args.damping`。第一实现明确固定

$$
\beta=\mu^{-2}.
$$

这只选预条件器的背景逆尺度。原完整 QP 的 $\mu^2\lVert z\rVert^2$、所有原自由变量、原 $B$、原 $R$、原物理高度坐标及母范数均不变。构造期间及整次 QP 内，不更换此方向的 frame、$G_c$、小矩阵因子或 beta。

`Gc` 已由 da083 组件包含原完整归一化 Phi 的因子

$$
\gamma=\frac{k}{c^2\left(\sum_s w_s\right)N}.
$$

接线器不再乘一次 gamma、不另加 Frobenius 因子、不改变正径向权或角轨道重数，也不以旧 Jw 矩阵替代它。真实当前 $x$、全部行、完整 q/core、模型定义、实际高度 lift、当前 $B/R$ 及权的绑定由冻结 moment 组件执行并记入 `data_report`。R671 的固定 $k'$ 已在当前 first-jet cache 中；高度列仍是当前 Hermite$(b-h)+h$，接线器不另写一个近似高度列。

总报告记录输入 bundle 身份，每方向记录最近实际接受的 bundle SHA；同方向完整场的精确浮点数组身份与模型身份由 `data_report.actual_x_sha256` 和 `data_report.model` 分别给出。新表示迁移初猜不能凭旧输入 bundle 名称继承原场证书。

## 4. 失败与成本的真实记录

源码、方法身份、shape、布局或误用条件的 `ValueError` 直接传播。接线器不把它们伪装成可选组件的数值失败。

在求解之前，声明的 `SmallSPDUnavailable`，或粗矩阵构造的 `ArithmeticError` / `MemoryError`，会写入 `construction_unavailable_frozen_v3_selected` 及具体原因，再明确传 `preconditioner=None` 给 v4，委派原冻结 v3。没有加 jitter、裁剪谱值、改 damping 或为此另开一个 QP。操作系统直接终止进程时不会进入该分支，不能据此宣称已有成功 fallback。

若构造成功但 v4 在求解过程中应用预条件器失败，保留 v4 的 `fixed_preconditioner_application_failed` 和实际截断 $z$。不在同一 Krylov 链内换单位算子，不自动重试。这一截断步后续仍付原真实 Phi、全点几何和已声明 SOC 规则，不能称 QP 已收敛。

每方向 `coarse_preconditioner` 记录实际构造秒数、frame 记录、全行 moment 记录、小矩阵构造和源尺度 metadata、实际 QP schema/status。v4 自身另记预条件器应用次数、秒数及失败。原 `inner_counts` 仍属于真实 `A`/转置调用；粗构造前后也保存该计数器的实际差。

额外 field/residual/J/JT 调用均为 0。这里“没有单位列 probe”指没有单位 J 列或全 Jacobian 扫描；frame 内已有的字面高度列绑定与矩阵运算仍属真实构造成本，并由其 setup 时间计入。角矩、径向块和小矩阵分解当然有成本，不能因 J 调用为零而记作零工作。

`Gc` 和构造临时量在进入 QP 前释放；成功对象只保其 frame 与小因子。无论 solve 正常返回还是异常退出，`finally` 都移除临时 keyword 中的对象引用并释放本方向预条件器。原 `A` 不在这里删除，SOC 在需要时仍可读取同一个父模型。没有把新的高维数组加进公开报告。

## 5. 实际接入责任

此小模块只准备源，不包含完整 launcher、调度、父身份豁免或新的科学预算。复合 launcher 须先支付已有完整父报告/模型/永久位置绑定，重建 frozen-base → manifest → SOC → 本增强的源，显式转发上述源参数及 v4，然后在公开 Actions 执行。第一次真实方向是否改进、是否因可选构造退回 v3，以及实际构造/应用成本，均等待该真实执行报告；本说明不提前填写结果。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
