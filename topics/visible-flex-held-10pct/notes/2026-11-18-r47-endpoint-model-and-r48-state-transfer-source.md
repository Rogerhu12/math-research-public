# R47 端点动态模式模型与 R48 连续状态转移：来源准备

本条只准备将来的升模接口，尚未构造新模型、核心、投影、初值或积分，也没有新的尾、BVP、度量或闭合结论。输入入口明确要求一份真正完成的 M8、$\lambda=1$ 物理 checkpoint；当前准备不把已经计算的中间同伦点充作端点。

## 1. 固定轮廓与自由参数分别记录

新模型复用原环境的实际 `build_classes`、完整 lift、全参数解析 Jacobian 及原 positivity 门。每个模式数重新构造 Flow/BVP 类并捕获不可变工厂，不修改已经存在的 M8 对象。核心调用 [R47 固定槽接口](../scripts/resume_closed/r47_fixed_slot_trace_core.py)，物理控制顺序为

$$
B_2,B_3,B_4,B_5,B_6,T,U,B_7,\ldots,B_{M-2}.
$$

$T,U$ 保持零起算物理控制槽 $5,6$，对应完整参数槽 $6,7$。新状态有 $3M+1$ 个分量，参数有 $M$ 项，控制有 $M-1$ 项。

原 M8 路径使用 `fixed=False`，其 $p_0$ 是轮廓的 $\delta$ 移动。新接口把实际 `frozen_profile` 原样用作轮廓，因此旧 $p_0$ 已计入一次；新模型 `fixed=True` 的初始 $p_0=0$，意义是

$$
q_{\rm actual}=q_{\rm seed}\exp(p_0).
$$

其中 $q_{\rm seed}$ 是真实端点的幅值。原 gauge、warp 仍为其已记录的 $.06$，两者不替代实际幅值。旧七个 $p_j$ 直接复制，首先检查前七个 `pscale` 逐字节相同，再检查所得完整物理七控制逐字节相同；不经“除以尺度再乘回”的重建，也不调用旧 `restart` 的幅值幂次规则。新控制补零。

**这没有固定原求解的全部参数。** 保留的原方程仍以 $p_0$ 和所有控制为自由未知量。初始化处的同核心身份，与后来求解可能产生的 $q$/控制变化分开记录；后者不能只凭 `fixed=True` 或冻结轮廓就称满足课题 README 第 5 条的固定全部参数精化。接口提供 `parameter_identity(actual_returned_p)`，供实际高层保存最终完整向量及幅值。

## 2. 完整端口与来源范围

`EndpointModeEnvironment(...).make(M, angular, linear_port_path)` 要求一份真正包含所需模式的完整线性端口文件。文件哈希单列，模式标签必须含 $3,6,\ldots,3M$，其全部物理参数及切口必须与原端点相同。原 short bridge 插入与旧 reader 一致，不能把一个较短端口列表补零充作新维度数据。

这个线性端口只用于原模型构造。新增的实际非线性 DN、完整高度向量、Jacobian 和 audit 都要由相应维度的原执行取得；本源不附着旧八维响应，也不把旧响应或其 Jacobian 补零。新的 `angular` 请求和原构造器产生的有效角点数分别记录。

当前准备核对新两源、既有 R47 固定槽源码、原完整 lift/参数导数、`tight_moment_interval_bounds` 及原环境的来源。此前 q060 绑定仅作为已登记源码哈希的只读注册表；它不是新 $\lambda=1$ 数值输入。未来实际入口仍需由真实端点 reader 逐项绑定自己的 checkpoint、参数、来源和尾。

## 3. R48 的实际状态分块

原 cylindrical basis 的状态布局为

$$
(R_0,R_1,\ldots,R_M,T_1,\ldots,T_M,Z_1,\ldots,Z_M),
$$

分别乘 $e_r$、$\cos(3j\psi)e_r$、$\sin(3j\psi)e_t$、$\cos(3j\psi)e_3$。故 $M\to N$ 的嵌入索引是：

| 旧块 | 新块位置，零起算 |
| --- | --- |
| $R_0,R_1,\ldots,R_M$ | $0,1,\ldots,M$ |
| $T_1,\ldots,T_M$ | $N+1,\ldots,N+M$ |
| $Z_1,\ldots,Z_M$ | $2N+1,\ldots,2N+M$ |

这逐列实现 [R48](../results/R48-exact-reference-compensation-for-mode-extension.md) 的 $\mathcal B_NE=\mathcal B_M$，不能用整条旧数组末尾补零代替。新接口从实际保存的 **physical quintic** 取值；旧 `raw.y`、求解器 cubic 与这个物理表示不混用。

设两个实际 inlet 投影为 $I_M,I_N$，取 $\Delta I=I_N-EI_M$。`EndpointStateTransfer` 提供连续函数及物理 $s$ 的前两阶 jet：

$$
\begin{aligned}
Z_N&=EZ_M+a\chi\,\Delta I,\\
(Z_N)_s&=E(Z_M)_s+(a_s\chi+a\chi_s)\Delta I,\\
(Z_N)_{ss}&=E(Z_M)_{ss}+(a_{ss}\chi+2a_s\chi_s+a\chi_{ss})\Delta I.
\end{aligned}
$$

代码逐式保留原 `exact_core_lift.py` 的 $a\chi$、窗 $.5,.9$ 和两个径向导数。$I_M,I_N$ 就是各实际模型已经计算并附着在 lift 上的有限浮点投影，不冒称精确 Fourier 积分。某个补偿因子字面为零时，直接复制相应嵌入状态 jet，避免额外的浮点加零；切口附近因此保留原块的字节，而新增维度的真正尾条件仍另付。

本接口不自动做 inlet repair，也不把连续补偿函数重新拟合成 quintic。若旧有限入口有残差，该残差仍按原实际条件处理；数学上标准入口相容的结论要求 R48 的原假设。补偿项一般不属于旧分段 quintic 空间，因此只取节点或另造插值不能宣称整域严格相同。

## 4. 物理坐标与归一化求解坐标

轮廓重基后，原 `fixed=True` 模型会重新建立归一化径向图。它的物理 $s$、轮廓和总长度保持，但不能直接假定旧 `fixed=False` 的 `raw.x` 就是新图的同一点。

`source_mesh_in_new_chart()` 只在未来显式调用时，把保存的物理 `PPoly.x` 交给新模型原 `inverse_chart`，继续使用该原函数自己的收敛门，然后报告有限 forward roundtrip。它不强制 roundtrip 为零，不用旧归一化数组伪装新图，也不调用残差或求解器。高层若加密径向网格，应在这一明确坐标关系上另作实际初始化。

## 5. 没有由源准备支付的结论

R47 保证补零后定义核心相同；不同模式数的实际反函数、积分和投影浮点结果未由此证明逐位相同。R48 的完整图恒等式还要求共同竖直均值；均值不在 $3M+1$ 状态里，本接口既不复制旧 primitive，也不新算 primitive。最终原 `height_integral`、全图 audit、接缝和额外尾方程必须由真实候选分别支付。

本次只运行 read/hash/AST 准备程序。没有 core/Flow/BVP 实例，没有入口投影、状态取值、chart 反函数、mean 积分、metric、Jacobian 数值探针或尾请求。因此它是可以供后续真实端点使用的来源接口，不是高模式数解、固定全参数收敛或新连续证书。

新源为 [动态模型](../scripts/resume_closed/r47_endpoint_refinement_model.py)、[逐块连续转移](../scripts/resume_closed/r48_reference_state_transfer.py)、[只读准备入口](../scripts/resume_closed/prepare_r47_endpoint_transfer_sources.py)，本次实际准备的完整哈希与紧凑字段见 [执行记录](../scripts/resume_closed/r47_endpoint_transfer_source_preparation.json)。
