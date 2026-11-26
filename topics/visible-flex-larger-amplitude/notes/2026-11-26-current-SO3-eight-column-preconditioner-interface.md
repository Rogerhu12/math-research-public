# 同一当前 SO(3) 全空间 QP 的八列预条件入口

2026-11-26。会话 `Astra-larger-e4e2a2bf-20261126 / geometry`。

**状态：完整小源和来源接线说明；只完成源码、AST、编译和接口审查，没有科学执行、实际加速结果或新的连续证书。** 本说明直接使用 [R681](../results/R681-current-J-coarse-frame-preconditioning.md) 的固定 SPD 应用代数和 [R685](../results/R685-constrained-active-face-preconditioner.md) 的约束面逆。它不重证这两个结果，也不把 [R688](../results/R688-complete-mean-metric-coarse-Gram-and-face-PCG.md) 的旧布局及角矩专用实现迁给 SO(3)。目前运行中的旧入口不改。

## 1. 已读到的真实源码入口

原完整归一化入口 `fullclosed_so3_cached_interior_separation_soc.py` 的 SHA256 是
`892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8`。
其 metric 分支先建立同当前完整点的 `NativeLinearization`，再定义

$$
A=\gamma J_{\rm positive}T_N,\qquad
\gamma=\sqrt{\frac{k}{\mathrm{scale}^2C_0}},\qquad
C_0=N_{\rm full}\sum_s w_s.
$$

这里 $T_N$ 就是当前 `RotationH2Coordinates.lift`，反向用其真正 `transpose`。原输入保留全部观察位置、quarter 轨道倍数、正谱三行、固定标量目标、全部 core/rotation/H 变量。当前源的 `qp.solve` 直接调用完整 v3，来源为
`fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4`。
其历史保存方向能量、斜率、面变化等标量，没有保存可重新消费的完整 $V,HV$ 列。不能把这些标量或旧 checkpoint 冒成已有低秩 Hessian 数据。

本次选择的新增输入是少量**独立的完整当前列**，而不是在同一未重启 CG 面内重新包装已经访问过的 Krylov 空间。R681 §8 已说明后者在准确算术中没有自动增加搜索空间的保证，本说明沿用其边界。

## 2. 首版八列的完整定义

保持当前原模型的 $K=3$、$M>K$、$J$、$n=3M+2$，以及源码所声明的全部径向自由槽

$$
\mathcal F=\{0,\ldots,3J-1\}\setminus
 \{0,3(J-1),3(J-1)+1\}.
$$

这只是核对**已经存在**的固定端口，没有新增端口、删模或约束。粗列顺序固定如下。

| 列 | 当前完整坐标中的来源 |
|---|---|
| 0 | 原自由高度 $H$ 的单位坐标 |
| 1 | 第一个原自由 core 坐标；$K=3$ 时对应频率 $\nu=8$，前三个固定系数不动 |
| 2–3 | 原 $\omega_x\sin\phi$ 角槽中的下述两条全径向多项式 |
| 4–5 | 原 $\omega_y\cos\phi$ 角槽中的同两条多项式 |
| 6–7 | 原 $\omega_z\sin2\phi$ 角槽中的同两条多项式 |

令 $t=s/S$，两条物理径向模板是

$$
p_0(t)=t(1-t)^2=t-2t^2+t^3,
\qquad
p_1(t)=t^2(1-t)^2=t^2-2t^3+t^4.
$$

在全部原节点填入 **value、真正 $s$ 一阶、真正 $s$ 二阶**，即

$$
\begin{aligned}
p_0'&=1-4t+3t^2,&p_0''&=-4+6t,\\
p_1'&=2t-6t^2+4t^3,&p_1''&=2-12t+12t^2,
\end{aligned}
$$

然后分别除以 $S$ 和 $S^2$。它们的 core value 为零，cap value 和 cap first derivative 为零；其余原自由 jet 全部按模板填入。这里的工作模板在**实际当前数值 mesh/S** 上形成。它是有限 QP 内的明确列选择，不以 mesh 载体或求积的工作字冒准确符号域的连续包围。

每个角槽的两列经当前坐标映射的逆送入 QP 坐标，然后只对这两列作完整 reduced QR，统一正对角符号。core 和 H 的支撑与三个 rotation 槽分离。所得 $W$ 有八列，但全空间维数仍是原 `q.free_size`；所有其他方向留在正背景项中。

小 QR 不丢秩、不用阈值剪列、不加入 ridge 或 jitter。若分解数值不可用，明确不启用这一 optional 预条件器；继续原完整 QP，而不删原变量。

## 3. 当前两个 norm 分支的真实逆公式

本源码只接已声明的 234ac 或 7f 完整 SO(3) 场及它们自己的 `RotationH2Coordinates`。旧 DI/角矩 coarse 源没有被调用。

### 3.1 原 node-jet norm

当前实际 lift 的 rotation 部分为

$$
x_i=d_i\frac{z_i}{\sigma_m},
$$

其中 $d_i$ 是原 `diagonal_scale`。因此模板在原 QP 坐标中的唯一逆为

$$z_i=\sigma_m x_i/d_i.$$

实现按原源码重读 mesh、Voronoi mass、三种径向权与已声明 diagonal hash，核实际 `diagonal_scale`；没有用另一个 norm 的字重标原 norm identity。

### 3.2 原 integral norm

当前实际 lift 为

$$x=E U^{-1}(z/\sigma_m),$$

其中 $E$ 是原正 equilibration，$U=L^T$ 是原 band Cholesky 的上带因子。所以

$$z=\sigma_m U E^{-1}x.$$

该逆只是六条带的矩阵乘积，不求新的积分、不形成另一母范数，也不另做当前 norm 的 Cholesky。原 packed convention 是

$$U_{i,i+k}=\mathrm{upper}[5-k,i+k],\qquad 0\le k\le5.$$

实现逐项按此乘法，同时核实际 lower/equilibration 的原 hash 与 upper 的真正转置关系。原 norm 如果在其自己的构造阶段失败，本 helper 不会以 node-jet norm 替代；它尚未获得合法输入对象。

两个分支都保原自由 core 缩放与原 H 尺度。粗框架是原 QP 坐标中的映射，不是新增的冗余自由参数。

因此 R681 旧 DI 加附加 coarse 槽的 $\sqrt2$、$2G_c$ 因子不进入本框架：本次没有增加任何 QP 槽，直接压缩的是当前八列 $W$ 的 $W^THW$。复用的是其固定 SPD 代数，旧布局的构造函数与专用数据装配均不调用。

## 4. 完整当前粗 Hessian：八次 A 与八次 A*

本 helper 接受实际完整 `q, coordinates, bridge, x`，先核：

- `bridge.original is q`、`coordinates.problem is q`。
- 当前完整点与 `bridge.x` 的 dtype、shape、全部字及摘要相同。
- q 的 jvp/vjp/fields、coordinates 的 lift/transpose 都来自同一个明确的 234ac 或 7f 完整源码，模型 schema/source/canonical identity 一致。
- bridge 的实际 matvec/rmatvec/whiten 来自原 R664 源 `29e2cf8c...`，谱模块是原 `e83742c6...`。
- 当前 norm canonical identity、实际 norm 数组、mesh/自由槽、完整观察权及全部轨道相同。

随后使用原公式**自行构造返回的同一个完整 $A$ 和原虚拟右端**。因此调用者应使用本 helper 返回的 `A, residual`，不再另换一个未绑定算子来做该 QP。

对 $j=0,\ldots,7$，实际执行

$$
w_j=W e_j,\qquad a_j=A w_j,\qquad
y_j=A^T a_j,\qquad G_{\cdot j}=W^T y_j.
$$

每次都是当前完整 $A$ 和 $A^*$，包含当前 nonlinear SO(3)、全 core 隐式图、完整 $h'\Delta$、H 链、正谱块、所有原行和外尺度。没有使用旧父 Hessian、少角/少径向子采样、旧 mean-metric 角矩或单位场近似。每列报告实际 data energy、$W^TA^TAW$ 的对应对角、二者浮点差、完整方向 SHA、耗时；小矩阵的反对称缺陷单列。

记录实际 literal $K_W=W^TW$，然后以对称化后的当前 data 小矩阵形成

$$H_c=\frac{G+G^T}{2}+\mu^2 K_W.$$

这里的 $\mu$ 是当前原 QP 的正阻尼。**原完整罚项仍为 $\mu^2I$**；小矩阵加 $\mu^2W^TW$ 是该原罚项在 literal 八列上的压缩，不是把原罚项换成八维的。

小矩阵用真实 Cholesky；成功后应用实际保存的 $LL^T$ 的逆。其工作舍入误差不是向外证书。未用 jitter、负特征裁剪或删除任何列来强造通过。

## 5. 固定 SPD 应用和背景尺度

直接使用 R681 已证的形式

$$B=\beta(I-WW^T)^2+W(LL^T)^{-1}W^T.$$

保两次补空间映射，不把浮点 $W$ 直接当严格正交而少做一次。`w` 与 `wt` 使用同一紧凑数组及互转置运算。R681 的准确代数正定性不要求机器中的 $W^TW$ 恰好等于 I。

首版默认**明确声明**这一算法尺度：

$$\beta=\frac{\operatorname{trace}(W^TW)}{\operatorname{trace}(H_c)}>0.$$

它是当前八列的平均 Rayleigh 逆尺度，准备后在本次完整 QP 内固定。它不称为整个补空间的真实谱、最优尺度或性能保证。也可由独立新入口显式给一个正的 `background_inverse_scale`，实际字和策略进入 setup record。没有改原 $\mu$ 或以背景尺度重新归一化原 QP。

全部 B 应用不需要新的场、J 或 J*；其成本是少量完整向量、紧凑径向乘法和 8×8 解。构造它所需的 **8 次 A + 8 次 A*** 必须独立计入实际资源，不能只报告 PCG 内部 products。

## 6. 大输出与完整资源语义

必须区分逻辑完整圆周行数与实际 A 输出行数。当前报告的 45,324,288 是逻辑全圆周行数 $3P N_{\rm full}$；实际完整 quarter 算子已经准确承担轨道倍数，其输出行数是

$$3P(N_{\rm full}/4+1)=\mathrm{bridge.shape}[0].$$

本层实际持有的一列是后者，不是 45,324,288 行的全圆周数组。`full_A_column_bytes` 按 `8*A.shape[0]` 记录真实输出字节。源码不形成 `rows × 8` 矩阵，也不将八个 A 列同时放在内存或磁盘。

每列按 `W e_j → A → A* → W*` 顺序处理，用完即在 `finally` 释放该列大输出和完整 adjoint 向量，再进入下一列。W 自身只保存三个 `radial_free × 2` 的紧凑矩阵、core/H 两个固定位置和小 Gram；不保存 `full_variables × 8` 的 W。

这只给出**本层新增持有对象**的明确范围。原 J/J* 的中间张量、当前 bridge、字段缓存、原全 C 与 active-face 向量仍占实际内存。v5 还为真实当前活动基的每一行缓存一个完整 $BQ_i^T$ 向量，数量由实际活动面决定；它在原报告的 `maximum_cached_vector_bytes` 单独记录，不能从八列 frame 的紧凑存储推断这一项为零。不得由任何单列字节数推出整个进程峰值。实际 Actions 返回应保原峰值读数、构造总时间、逐列时间和 q 计数差。没有把 raw A/Y/控制数组加入 Git 或 artifact。

## 7. 与原 v5 的最小完整接口

完整小源的 API 是：

```python
A, residual, preconditioner, setup = current_coarse.prepare(
    q, coordinates, bridge, x,
    damping=used_damping,
    background_inverse_scale=None,
    callback=lambda value: event(**value),
)
```

只在原 **metric** 分支调用；Phase I 继续原完整 v3。

metric 的同一 QP 直接交已刊 v5：

```python
coordinate_step, qp_report = qp_v5.solve(
    A, residual, solve_C, solve_bounds,
    damping=used_damping,
    parameters=original_parameters,
    block_columns=args.active_block_columns,
    callback=original_callback,
    preconditioner=preconditioner,
    preconditioner_metadata=setup,
    v3_source=paths['qp_v3'],
)
```

v5 完整源 SHA 为
`76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8`，39,739 B。其 `Parameters` 属性与原 v3 参数合同相同，但完整新入口必须明示这两个来源，不能仅把旧 `qp` 模块改标签。特别，原外层仍调用 `qp.StreamedRows`；v5 不导出该类。应保留原 v3 模块供所有原行操作与 Phase I 使用，只把 metric 的 solve 交 v5。

v5 使用 R685 的

$$B_V=B-BQ^T(QBQ^T)^{-1}QB,$$

其中 Q 是同一次 QP 的真实活动行欧氏正交基。原所有非活动行仍参与可行步上限；活动面变动时按原规则重启，释放第一步保原 Euclidean inward starter。停止仍用原投影梯度及可行释放尺度，`iteration_limit` 不冒收敛。

**原 C、bounds、母范数、damping、全部自由变量、真实 Phi、最近 rejected ray、同父 SOC、永久位置与最后真实读回全部继续由原完整外层保留。** 本 helper 不读取或改动这些对象。driver/launcher/reader 必须是独立新源，保旧 892f 的可重建身份和完整来源检查；首新方向仍须重新读取实际当前父。

## 8. 数值失败的完整语义

来源、布局、模型、当前点、norm 或字节身份不符是输入错误，明确抛出，不作为“可忽略的预条件失败”。

在合法同场输入上，QR/当前列数值/小 Cholesky 等 optional 准备不可用，或该准备过程中收到可捕获的 Python `MemoryError` 时，返回 `preconditioner=None` 和完整已尝试列数、算子计数、异常、耗时。此时尚未开始任何 PCG 链；v5 的 `None` 分支逐字调用同一个原 v3。失败不会让某列悄悄消失，也不称数学几何不可行。已经付出的部分 probe 成本如实保留。这里不承诺系统杀进程或作业硬终止也能返回。

一旦 PCG 已开始，B 的实际应用失败由 v5 明确截断报告；不会在同一未重启链中换成 identity、另一个 beta 或旧父数据。具体而言，本 helper 的 `NumericPreparationUnavailable` 继承 `ArithmeticError`；v5 新面 `_prepare` 捕获其声明的算术异常，只在新面第一链前选择整面的原合法 PBP。若在随后实际应用中仍失败，外层 `projected_preconditioner` 的 `except Exception` 记录异常并返回不可用，主循环以 `fixed_preconditioner_application_failed` 截断。可捕获的 `MemoryError` 不属于新面算术回退列表，会由这个外层异常路径截断。原完整方向的最后诊断仍按 v5 控制流执行；若整个进程已被终止，则不存在这份正常返回。

本 helper 构造后也核当前点、模型和母范数未被改动。调用者负责在 solve 返回前固定这些对象；本层不重新优化 x。

## 9. 返回字段与审核范围

`setup` 包含实际 source SHA、field/model/current-point/norm/权的完整身份、8 列来源和紧凑 QR hash、完整小 G/Hc、实际阻尼/background 字、8 次 A/A* 计数和 q 计数差、逐列时间、总准备时间，以及是否启用、数值回退和内存责任。原 `qp_report` 另给 PCG 自身的面变化、全原可行性、投影梯度和实际时间。两组时间与 product 不合并伪装零成本。

控制器 summary 可只选标量：`setup.enabled/status/columns_completed/extra_A_calls/extra_Atranspose_calls/preparation_seconds/maximum_data_Gram_skew/full_A_column_bytes`、`fixed_background_inverse.value`，以及原 QP 的 `advances/final_face_projected_gradient_norm/seconds/status`。完整小记录仍留在 report，以便复核来源和失败归因。

当前静态审核没有在本地导入科学模块或运行任何数值。没有额外 fixture、没有新通过门、没有预填速度、没有假定本八列覆盖当前真实慢方向。若真实返回显示补空间仍慢，才据该返回发展下一独立预条件输入，不能把本层 SPD 当成条件数必降的证明。
