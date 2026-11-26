# 同一零闭合初值的端点失败重演、实际宽泡泡矩与候选输入

日期：2026-11-26。本文是独立诊断入口的完整说明，不新增课题完成结论或定理编号。原始实际失败见 [03b 第 3 卷](2026-11-26-public-actions-45820592817-1-part-003.md)，完整弦长读取见 [第 4 卷](2026-11-26-public-actions-45820592817-1-part-004.md)。

## 1. 这次读取的具体责任

实际 `45820592817/1` 阶段 11 在同一初自由点、宽泡泡支撑与数值分支搜索半径 $0.75$ 下失败。报告 SHA256 为 `4341323c805a3e4f38c20c6e5264e9875b8b717082793ece982c029f488ed744`；失败索引为 `[5]`，批次最大实际残差为 `0.034892231118679326`，批次最大修正范数为 `0.5022681264085023`。这些最大值是整个首批八角的值，不能擅自配给索引 5。该次没有初始场、终场或完整参数 $J/J^*$ 返回。

阶段 14 已对同一真实初值给出完整角域弦长盒，`all_chords_necessary_condition=true`、`no_closure_for_this_core_H=false`，全角最大弦长平方减 $S^2$ 的严格上界为负。故当前证据排除了“原高度违反一般单位速子午线弦长必要条件”这个解释。必要条件通过不证明有限泡泡族可达，也不证明 Newton 根存在；目前没有按该错误理由降低 $H$。

原 `5b4c3921...` 数值根源的失败记录保存失败原因、索引、策略、批次最大值与完整自由点身份，没有保存当时的 $z,C,C_z$、Newton 方向及最后实际回溯的各数组。其成功缓存要在整个角批完成后才建立。纯读原报告不能恢复这些未写出的值。

因此，新入口是一次明确的公开 Actions 科学重演：在与阶段 11 完全相同的初自由点和八个原角节点上，再执行原数值根方法，保留真正失败处的小数组。它不把新计算称为原日志读取，也不假定新浮点路径必与旧运行逐字相同。

## 2. 完整来源与原输入不变

源文件为 `scripts/resume_20261126/trace_zero_initial_endpoint_failure.py`，完整 SHA256 为 `73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54`，22440 字节。报告 schema 为 `actual-zero-first-eight-endpoint-replay-v1`。

它使用已刊 `diagnose_zero_initial_chord.py` 的完整 `ActualInitialInput`，精确源 SHA 为 `65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0`。该构造器绑定实际失败报告、全部物理源、reference/observations/nodes/scalar 四个输入字节、完整参考准备报告和 zero→base→reference 三层定义；重建原 `q.initial()`，再核完整自由点 SHA 与实际失败报告相同。

本次对应的原完整自由点为 `cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3`。当前 core 必须逐字等于固定参考 core，全部原 $\omega$ 系数为零，$H$ 为原 reference 字，完整 $x$ 不可写。原准确标量目标和全部原自由变量保持不变。读取的是实际 03b 的模型 `29f540c6fc265b977a388813dcd0d3faddfd48fd06d40c7f6c4bcae5c848281b`，不是旧运行 `383168...` 的来源标签。

宽泡泡两个精确相对三节点继续为

$$
(1/32,\ 1/4,\ 15/32),\qquad
(17/32,\ 3/4,\ 31/32).
$$

根策略仍从真实失败报告完整重建：残差容限 $2\cdot10^{-12}$，最多 24 次外迭代、每次最多 18 次回溯、Armijo 系数 $10^{-4}$、数值分支搜索半径 $0.75$。这不是新的 IFT 已验条件。程序不换初种子，不预装任何新的泡泡矩阵，不增加根迭代预算。

## 3. 原算法的只读观察位置

入口对实际对象 $\_C0,\_C0\_jacobian,\_solve\_roots,\_total,\_meridian\_data,\_bubble\_values,\_W,\_rotate$ 的代码来源逐一核 SHA：

`5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46`。

它解析这一完整源中的 `ZeroClosureOperator._solve_roots`，复制完整函数 AST，仅在两个类型的位置插入观察语句：

1. 每个原 `self._fail(...)` 之前，读取当前局部变量；
2. 原 `trial_norm = ...` 赋值之后、原 `good/accepted` 更新和 $\alpha$ 减半之前，读取真正被评价的最后候选与步长。

将所有且仅这些观察语句删除后，整个函数 AST 必须与原函数逐项相同。不是仅比较几个科学表达式，也不是用重写的 Newton 算法代替原方法。完整新生成函数另存为小源码 `observed-original-endpoint-root.py`，输出其 SHA 与原完整函数 AST 的 SHA。

实际 $q$ 的方法没有替换，物理方程和小端点 Jacobian 都仍调用原对象的原函数。新观察函数只读取并复制小数组，不写入原 $z$、方向、状态或张量图。

失败观察记录当时的 $z,C,C_z$、Newton 方向、active/accepted、候选范数、容许标志等小数组，各数组同时保存有限工作值及精确 binary64 十六进制字。最后实际回溯记录的 $\alpha$ 位于原减半之前，因而不会把失败后多减半一次的局部变量当作真实评价步长。

Armijo 右侧从这些原工作字重算并明确标为数值诊断；它不是向外区间证明。对当时 $C_z$ 的 SVD 同样只报告数值奇异值，不把较大的数值奇异值称为严格可逆性证书。

## 4. 同时返回的宽泡泡完整工作矩

令未修正单位切向场为 $T_y$，两泡泡为 $\beta_i$。其连续矩定义为

$$
v_i(\phi)=\int_0^S \beta_i(s)T_y(s,\phi)\,ds.
$$

本次诊断实际用原 $\_total$ 和原 $\_bubble\_values$，遍历全部原径向胞，保原 8 阶 Gauss 工作节点、权重与 literal mesh 宽度，读取两个矩在首八角的工作值。没有只读取几段支撑的采样点并冒作积分。

这些数值使用原工作规则，尚未支付准确符号节点、标量、积分或浮点误差。因此报告明确写 `moments_are_working_values_not_true_intervals=true`，`true_moment_integration_or_FloatingPoint_error_certified=false`。全工作胞积分和严格连续积分是不同责任。

原首零角下，真实轴对称输入使

$$
v_i(0)=B_i e_x+C_i e_z.
$$

程序保留实际返回矩的三个分量，包括其数值 $y$ 字。仅为提出后继可选输入，另显式定义

$$
\widehat v_i=(\widehat B_i,\ 0,\ \widehat C_i)
$$

为一组准确 literal binary64 字。这里的零是新候选输入的明确对称定义，不是把数值 $y$ 误差删去后宣称取得准确积分。

## 5. 为什么实际矩能指导下一输入

当前 5b4 的两 $Q_i$ 使用端点轴近似矩：第一段近似竖直、第二段近似径向。把支撑扩到大部分子午线后，积分方向可能与这些端点轴近似不同。这里的“可能”不是对当前失败原因的结论；新的实际 $C_z$ 和积分矩正用于判别这一点。

对任意两个真实非平行向量 $v_1,v_2$，记 $[v]_\times u=v\times u$，并定义

$$
G=\sum_{i=1}^2\bigl(|v_i|^2 I-v_i v_i^T\bigr),\qquad
Q_i=[v_i]_\times G^{-1}.
$$

对非零 $u$，

$$
u^TGu=\sum_i |v_i\times u|^2>0,
$$

所以 $G$ 正定。端点修正采用世界左乘旋转

$$
\widetilde T(s,\phi,z)
 =\exp\!\left(\left[\sum_i\beta_i(s)Q_i(\phi)z\right]_\times\right)T_y(s,\phi).
$$

在 $z=0$，对 $\delta z$ 的端点积分导数为

$$
C_z(0)\delta z
 =\sum_i (Q_i\delta z)\times v_i
 =-\sum_i[v_i]_\times Q_i\delta z.
$$

利用 $-[v]_\times^2=|v|^2I-vv^T$，上述选择给出

$$
C_z(0)
 =\sum_i\bigl(|v_i|^2I-v_iv_i^T\bigr)G^{-1}
 =I.
$$

这是以真实积分矩为前提的完整代数恒等式；不证明有限残差下存在非线性根，也不提供 IFT 球条件。

实际源码用工作矩生成可选 literal $Q_i$，如工作 Gram 不可数值求逆或矩阵非有限则如实不给候选。若可返回，候选矩阵三个维度的全部 binary64 字会列出。它以同一固定图的 $R_z(\theta_0)$ 共轭扩展到各角，并仅计算对应工作导数的数值奇异值与距离单位矩阵的数值误差。工作矩不是准确积分，因此不声称真实 $C_z(0)=I$。

以 literal 字冻结两个矩阵是一项明确的新表示输入选择；该输入不必先被认证为真实积分矩才有数学定义。如果以后采用，须独立发布完整源/模型并绑定这些准确矩阵字，重新读取同一准确目标下的新实际场。当前代码只报告 `candidate_Q_installed=false` 和 `actual_original_input_changed=false`。

对于这种轴对称 literal 输入，$G^{-1}$ 保留水平径向/竖直的二乘二块与独立切向块，因而 $Q_i=[v_i]_\times G^{-1}$ 具有与原端点轴公式相同的径向—切向、切向—竖直耦合位置。固定 $Q_i(0)$ 经 $R_z(\theta_0)$ 共轭后，其角一、二导仍由同一交换子公式给出。后继如采此输入，仍须在完整新源中写出这一绑定，不能只改原来源标签；不能在每个当前自由点重算 $Q_i$ 却遗漏其参数导数。

## 6. 返回成功的含义与可执行入口

诊断 schema 的 `complete=true` 表示本次完整原算法重演及小诊断正常结束。原 `EndpointRootFailure` 是预期可记录的返回，诊断可以因此退出 0；这不把根失败改为成功。另有 `original_method_replay_success` 单独报告原数值根是否返回。非预期异常给 `complete=false` 和退出 1。

所有情况下，本入口不写新的输入、候选场或 checkpoint，不调用完整场 residual/$J/J^*$，也不宣称连续根、度量、嵌入、reach 或等距结果。即使这次原方法数值成功，也只是一批工作根返回，仍不代表全角连续分支认证。

完整 ready 文件为 `zero-initial-endpoint-trace-ready-steps.json`，SHA256 `4b34574f87fdf4b449ba72147ac149cb69af752cf52ee1d81b5e1036a3eea794`，6184 字节。其阶段 ID 为 `actual-zero-same-initial-first-eight-endpoint-trace-and-moments-20261126-03b`，消费既存 `axisymmetric-R690-reference-v2-first/reference.npz` 与原阶段 11 失败报告，在新目录 `zero-initial-endpoint-trace-first` 输出报告及完整 observed 方法源。所有公共 summary 选择器均落在标量叶子；小根数组和积分矩工作数据留在 runner。

写源时执行环境 unavailable，完成了逐段静态阅读与来源/参数检查，未声称已经执行本地 AST/compile 或科学测试。实际入口在公开 Actions 启动时强制整函数 AST 还原等号。当前新报告身份和实际数值仍未返回，不能预填。

后续选择只根据真实返回的失败状态、最后真实回溯是否受球约束、当前 $C_z$ 工作条件与两个宽泡泡矩作出；不继续盲增半径，也不把阶段 14 已排除的一般弦长障碍重新当作降高依据。
