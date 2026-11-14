# 旧段43原步11：四级实际局部 Jacobian 与有限数组作用接口

2026-11-14。本入口只重放 actual41 已经存在的旧段43、原流步11。它从已保存的完整226状态开始，执行恰四次原 rhsWithJacobian，并保全四个226×224局部矩阵、原 derivative、各级完整状态、完整一步 tangent 与两行 mean。它不重放前11步，不新增 ODE 步，不重建全尾 J，不求解零尾或新非零尾，不进行 correction、trial、endpoint J 或 fresh audit。

## 1. 真实小回执与选择依据

[request44](https://github.com/Rogerhu12/math-research-public/actions/runs/43627297724) 的 source 是 d07eeb32ec7e72f8982b0c8f3c9352e4a0e34e1f；job132545953652 实际全部成功，包括源码编译、取回固定 actual41、纯元数据摘取和发布。

公开 [stage43-step11-fields.json](public-actions-43627297724-1-receipts/stage43-step11-fields.json) 为26214字节，SHA256：

~~~text
d7d00de365b2118e1346e8f8630d5bad408957da91fdf51f38496f73b0e0c5f2
~~~

该文件只复制原件，没有新算 gamma、xi、谱、范数或任何根/RHS/J。其四级原记录如下；第二、三级的 geometry 相同但完整状态 SHA 不同，不能合并两个局部矩阵。

| 级索引 | 原 x | 原 r | 原 w | 原 dlogwdx |
|---:|---:|---:|---:|---:|
| 0 | 0.9166666666666666 | 0.23103771501074039 | 0.028151989854083202 | -1.4777906263761906 |
| 1 | 0.9583333333333333 | 0.23125319169184086 | 0.02647874198852758 | -1.4632935958199547 |
| 2 | 0.9583333333333333 | 0.23125319169184086 | 0.02647874198852758 | -1.4632935958199547 |
| 3 | 1 | 0.23145444223065165 | 0.024920457919589727 | -1.447920384241892 |

原 h 的 bits 是555555555555b53f；原 port 为1；原 sigma 的 bits 是27c23cdad1aab53c。原 w 明确变化，因此 R269 的常 w 特例不适用于这一步。这里没有另外计算这些数的比值、变化幅度或稳定参数。关于需要区分的误差层，见 [R271](../results/R271-discrete-RK-stage-gauge-covariance.md) 与 [R272](../results/R272-native-RK-reference-and-propagation-error-split.md)。

## 2. 冻结源码

| 文件 | 字节数 | SHA256 | Git blob |
|---|---:|---|---|
| [geometry_20261114_native_stage43_local_j_probe.py](../computations/geometry_20261114_native_stage43_local_j_probe.py) | 21416 | 1185bbda5390c7ef3a9043ac59139b9359fececc802146f4be64aa7639730b21 | d650412aafb0b26ce850435ff3fbcb72b7d4ba81 |
| [geometry_20261114_native_stage43_local_j_probe_hook.mjs](../computations/geometry_20261114_native_stage43_local_j_probe_hook.mjs) | 38399 | 8992f3920729b0f6eabf7a1e15520290fc47942c72c0c4d6433d8ac6cb291059 | 859cee4670526ad54fa79832e1c248a3b6da321f |
| [geometry_20261114_native_stage43_local_j_window.mjs](../computations/geometry_20261114_native_stage43_local_j_window.mjs) | 6224 | 966ddc4946cc63f69260dd1871c2ac31ad0383eb5593f6c3a0b45b0cfcdef5ec | 11072380370530c282be3b755ed8825675a12b2f |

文件均小于100KB，通过 GitHub 小文本接口保存；root负责分支与发布。三个文件独立于所有已冻结 native/41/43 源。当前新终端只用于纯源码 AST/语法和字符串往返验证，未导入数学模块或运行任何科学数值。

## 3. 输入与完整状态

原历史仍为17/19/21/22/23及其同一个完整非零 H。actual28 的完整原数组和 source/ready/config/capacity/graphs/gains/far/sigma 均沿已验证的冻结链读取。

新入口另要求完整 actual41 提取目录及上述 actual44 小回执。actual41 result SHA 固定为：

~~~text
6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf
~~~

Python 完整核 actual41 result、selected report/window、四级原 packet 的压缩/解压 SHA和 array manifest。它逐chunk核旧43的四种完整数组：full_states、shape_outputs、shape_jacobians、mean_tangent_rows。只把所需行复制到新输出 large-arrays；不读后声称已独立重核其他71段所有payload。

输入是 full_states[11] 的全部226字，包含已有两项 mean；输出参照是 full_states[12]。另复制 shape_outputs[11]、shape_jacobians[11] 和 mean_tangent_rows[11]。复制只搬原字节，没有插值或重构；完整初始状态的 SHA须等于原 field0 的 a26c6776bc3ab654a9e962fe32adefade8a1675d5be69836a214ee63e0b21489。

新 shooting 定位始终是：

~~~text
original_stage = 43
original_flow_step = 11
new_shooting_stage = 519
new_input_node = 520
~~~

这只是 actual41 已保存布局的身份，不新建1372段系统，也不导入 G 构造器。

## 4. 原 RK 算式如何保留

窗口读取冻结的原 product-flow 源717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f，然后复用 actual41 已冻结的 preparePerStepFlowSource。

actual41 prepared function 的 SHA为：

~~~text
447590785c402226adef6af880a44f8da6e2831786724d2762ab6c2c0addf5ab
~~~

新窗口只在该函数唯一的原 n循环开头插入：

~~~javascript
if(n!==11)continue;
~~~

其选定函数 SHA为31fbe3413b0c8d4e171edb4f06410ee531afe764e5ea4cafe321b6c98a2a3bf6。删除此行精确恢复 actual41 函数，再逆向删除 actual41 的已声明观察器/重置插入，精确恢复原函数177cf5f563aecdcab4431d842d8dfdd7f7915667b73fe956c87c48c1571c9fe4。

因此：

- 原 profile 与普通12步 schedule 保留，目标 h/x仍由原表达式产生。
- 只有原 n=11 被实际计算；前11个 n不调用任何 RHS/root/J。
- 原完整226 state 的四级 increment、最终 update 全文未改。
- 原 tangent 的四级乘加全文未改；本步初始仍为 shape 单位阵和两个零 mean行。
- 四次原 root/RHS/J 返回后才只读保存数组，不改变返回值。
- 原出口 Pi行及 shape tangent Pi行各按原表达式除一次 port；本例port=1。mean行不作 port缩放。
- 原 private no-J schedule 未调用，也未声称与 withJac schedule逐字一致。

完整 original seed 和 live函数/graph/gain/far/sigma 在运行前后均核字节不变。原 constructor/source链及 worker 的首次请求插入方式沿已成功的 actual41 模式；没有更改原 solve正文。

## 5. 输出合同

result.json 的 schema：

~~~text
original-native-stage43-local-j-capture-result-v1
~~~

它以 capture_summary_sha256 绑定 stage43-local-j-summary.json。summary的 schema为 original-native-stage43-local-j-capture-summary-v1。两者的 capture_completed、native_accepted 等均为实际 JSON bool。

array_manifest 是完整 {file,bytes,sha256} 描述器，指向 stage43-local-j-array-manifest.json；其schema为 original-native-stage43-local-j-arrays-v1，arrays是列表。每项至少含：

~~~text
name, file, bytes, sha256, dtype="<f8", order="C", shape, role
~~~

所有数值数组在 large-arrays/，保负零、原非有限位值及其实际来源，只进入完整artifact。复制的reference也列入同一manifest，不把它们冒称新计算。

summary/result均有：

- local_J_arrays：按field_index0至3排列的四个完整描述器，shape=[226,224]，均未port。
- field_reports：四项，每项带field_index、完整geometry_number_fields、原x/h、完整state SHA、原root标量、实际对应原记录，以及 arrays.state、arrays.derivative、arrays.local_jacobian 三个完整描述器。
- reference_arrays：键 full-input、full-output、shape-output、short-J、mean-tangent-rows，各值是完整描述器，不只是名字。
- observed_step_arrays：本次完整输出、shape输出、shortJ、两行mean及输入引用。
- original_h、original_port_ratio、original_sigma：原numberRecord，含value、float64le_hex、classification。
- same_state_path_as_actual41、all_four_geometry_records_equal及完整step比较，分别给出真实观察，不把scalar接近写成位相等。

新窗口的 cumulative guards只覆盖这一个步。原actual41的 cumulative guards覆盖旧stage之前已有各步，两者不混称同一个统计。每级 root_minA/root_minD/root_error/root_scale可按各自原记录直接比较。

计数区分四个pointwise局部A与一个短RK块：returned_pointwise_local_J_matrices=4 才是四份A，completed_local_J_evaluations沿actual41语义表示完成的短块数量1，并附明确role说明。

## 6. 精确 action 的数学边界

后继 [exact_20261114_single_step_rational_action.py](../computations/exact_20261114_single_step_rational_action.py) 是独立消费者，由其自身冻结来源定义。它只需本probe产物，不回调native。默认最高频Q/Pi两basis；可选读取具有完整原始来源的actual43方向在node520上的原224项。

四个局部数组分为上224行A_i和下两行C_i；完整线性扩展为

$$
\widetilde A_i=
\begin{pmatrix}A_i&0\\C_i&0\end{pmatrix},
\qquad \widetilde v=(v,0,0).
$$

shape控制后一级输入，两项mean输出仍保留。对每一个原数组位模式按精确有理数执行原RK4作用，最后只给Pi除原port，和保存shortJ/mean_rows的精确作用比较。单位basis只是线性代数输入，不创建同幅非线性状态或试步。

必须保留一个限制：actual41 当时没有保存四个局部A原bytes。这里取得的是**对同一冻结原函数的新调用**。相同state、geometry、root标量、函数及runtime来源是可复现证据；不能冒称已对当时未保存的A逐字节独立审计。故无条件比较的是“本次保存四A所定义的精确有理RK作用”与“原41保存shortJ的精确作用”；将差唯一归入旧tangent传播还要说明同A条件。它也不是完整真实DF误差证书。

原sigma可用于这项实际有限数组差的尺度读数，但不成为新的native验收门。不同basis或某一个实际方向的见证不能自动推广到所有列、所有段或整个闭面。

## 7. 失败、停止与Actions调用

任何原域/根/局部导数异常都保存已完成数组、实际field入口及原错误，计数如实保留。若四次调用和一步完成，则先保存完整summary，随后抛：

~~~text
VISIBLE_NATIVE_STAGE43_LOCAL_J_PROBE_COMPLETE_V1
~~~

原worker如实返回failed；launcher将这个单独标为计划诊断停止。完成仅表示限定探针完整；即使Actions退出0，native_accepted、task_completed、完整尾response、endpoint J/audit仍为false。

输入依赖沿actual41环境，包含原Python/Numpy/SciPy依赖与原native sourceTopic；不是仅stdlib的field摘取器。CAPTURE28、STEP41分别是已钉两个完整artifact的提取目录。本probe不用下载大G43产物；可选actual43方向仅供后续action消费者，并且绝不是执行该坏方向的trial。

~~~bash
python "$C/geometry_20261114_native_stage43_local_j_probe.py" \
  --failed-directory "$TOPIC/notes/public-actions-43598917532-1-coupling112trust/full-DN112" \
  --cold-probe-summary "$TOPIC/notes/public-actions-43602823170-1-coldtailprobe/cold-tail-residual/summary.json" \
  --first-candidate-summary "$TOPIC/notes/public-actions-43603818345-1-zerorkprobe/same-RK-candidate-native-probe/summary.json" \
  --v2-candidate-summary "$TOPIC/notes/public-actions-43604874829-1-zerorkprobev2/same-RK-candidate-native-probe-v2/summary.json" \
  --candidate-directory "$TOPIC/notes/public-actions-43605912092-1-zerorkprobev3/same-RK-candidate-native-probe-v3" \
  --capture-directory "$CAPTURE28" \
  --step-directory "$STEP41" \
  --field-receipt "$TOPIC/notes/public-actions-43627297724-1-receipts/stage43-step11-fields.json" \
  --source-topic "$PUBLIC_SOURCE_TOPIC" \
  --node-heap 6144 \
  --out "$OUT/native-stage43-local-j-probe"
~~~

输出必须是新独立目录。source、输出目录和真实后继result SHA由Actions实际确定，不预填尚未产生的科学结果。

## 8. 已做验证

最终三份源码已经在新终端显式workdir="/"下做纯Python AST和两份Node --check；生成的单步函数也单独Node --check。另做了纯字符串SHA、唯一插入及双层反向恢复。没有模块import、constructor、根/RHS/J、RK、norm或solve在本地运行。actual44元数据读取是既有原件的纯复制；新的四A科学探针尚待公开Actions真实回执。
