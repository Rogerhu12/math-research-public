# 新实际 reference 的十八字固定 Q：独立完整输入合同

## 结论范围

新完整纯源 `new_reference_literal_zero_moment_input.py` 允许把已经公开的十八个精确 binary64 Q 字作为新的固定控制参数，绑定到新 runner 实际构造出的完整参考输入。旧 `05dc5ed7...` 定义及 `26b094fe...` 真实 trace 只说明这十八个数从哪里来。它们不替代当前 reference、base、初点、材料坐标或固定标量度量的身份；不声称这些数仍是新初点的工作矩逆或真连续端点右逆。

这是新的输入类型，不修改旧 `4dc3e1a8...` binder 或 `44ac53f1...` 的严格同 reference 守卫。Gamma 算子和 driver 必须显式选择新模式并钉住本新完整源码，而旧模式仍走原 validator。

这项结论是完整输入/来源合同的源码结果，不是新场存在性、数值根成功、连续误差证书或题目完成。源只使用标准库，既不读科学数组，也不计算矩、逆、端点根、F、J 或 J*。

## 两种诚实输入类型

旧输入类型是 `frozen-zero-endpoint-moment-Q-input-v1`，它要求原 definition `05dc...` 中的 base、reference、scalar 与实际当前构造完全一致。新 runner 如果未逐字再生这些实际身份，原模式诚实拒绝，不能通过假造旧摘要、修改路径/时长、把旧参数 provenance 伪装成当前 model 来绕过。

新输入类型是 `new-reference-literal-zero-endpoint-Q-input-v1`，其 definition schema 是 `new-reference-literal-two-bubble-endpoint-Q-v1`。完整数学输入精确包含以下十项：

| 项 | 内容 |
|---|---|
| `schema` | 新独立 definition 类型 |
| `Q0_binary64_hex` | 原样全部十八个字，形状 2×3×3 |
| `exact_relative_bubble_nodes` | 两组完整宽支持有理节点 |
| `fixed_scalar_metric_identity_sha256` | 当前完整固定标量定义的 canonical SHA256 |
| `fixed_scalar_profile_definition` | 当前完整固定标量定义正文 |
| `initial_reference_bundle_sha256` | 当前实际 reference bundle 字节摘要 |
| `initial_reference_model_identity_sha256` | 当前完整 reference model 的 canonical 摘要 |
| `base_model_identity_sha256` | 当前完整 7f base model 的 canonical 摘要 |
| `initial_full_point_sha256` | 调用方从当前完整 base.initial 真数组得到的摘要 |
| `fixed_chart_core_sha256` | 当前固定材料坐标的全 core 摘要 |

新 definition 不含旧 trace report、旧 source、旧 base、旧 reference 或旧初点身份。这些都保留在 `provenance.complete_origin_definition` 等明确来源字段中。调用方把新 definition 及其 canonical identity 纳入模型；provenance 中的绝对读取路径不改变模型。

十八个 Q 字及六个支持字符串逐项保留。每个浮点词都必须 finite 且严格满足 `float.fromhex(word).hex() == word`；五个禁位准确为零，保持完整 reflection parity，不把小数静默抹成零。本源还逐项要求十八字与已公开的选择完全相同，因此没有隐含重拟合或新逆矩阵。

## 当前输入的完整检查

`_current_binding` 不接受只给一个摘要的替代 model，而是读取调用方已经构造的整个 base JSON。它要求实际来源为完整 7f meridian / 4e reference / e091 scalar，核验各 schema、两个完整 canonical model、完整 scalar definition 和摘要、当前 reference bundle、材料 chart、mesh、M160/J923、前三个 core 字、固定 R 字与全部 free core/H 标志。

当前 reference 内的 scalar input、全 warm、symbolic node、observation carrier 和全部目标 a 数组摘要都保留；它们必须是真实格式的完整 SHA256。固定 scalar 正文与 reference/base 中的两份正文必须完全一致。初点摘要由完整实际 operator 构造之后提供；纯 binder 不假称自己打开或重新验证了这个科学数组。完整 caller 仍负责它原本已有的实际 reference/数组/源字节检查。

`_validate_outer` 还要求 `provenance.binding_source_sha256 == sha(__file__)`，从而新输入不能自报另一个 producer 而冒充当前完整 binder 的产品。来源标记明确为：

- `same_mathematical_g_claimed = false`；
- `current_working_moment_inverse_claimed = false`；
- `current_exact_endpoint_right_inverse_claimed = false`；
- `origin_current_model_or_reference_identity_inherited = false`；
- `original_root_or_field_success_inherited = false`；
- `true_moment_error_or_uniform_IFT_certified = false`。

第一项表示没有建立“与旧度量相同”的结论；它也不是“两个数学度量一定不同”的证明。字节摘要中含真实文件来源或数值载体，不能仅因摘要变化而认定数学度量改变。

## 完整 API

`bind_new_input(origin_value, *, base_model, initial_reference_bundle_sha256, fixed_scalar_metric_identity_sha256, initial_full_point_sha256, bubble_nodes)` 返回新 outer。`origin_value` 可以由已锁旧 4dc `from_parameter_file` 以真实 df11 文件字节和明确 05dc definition 取得；该旧函数只读输入来源，随后不调用旧 same-base binder。

`bind_to_base(value, *, base_model, initial_reference_bundle_sha256, fixed_scalar_metric_identity_sha256, initial_full_point_sha256, bubble_nodes)` 严格复核整个新 outer 和当前十项绑定，返回新 definition identity。算子与纯 reader 都使用这一个合同，不各自猜测 keys。

`parse_literal_Q(value)` 返回两个 fresh list：完整 2×3×3 hex 字及对应的 2×3×3 binary64 数。它只解码固定数，不计算任何场或矩。

`from_parameter_file(path, *, input_sha256, ...同组当前参数...)` 是完整的小文件入口：它要求原公开 3618-byte 文件的真实 SHA 为 `df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c`，读取前后摘要一致，明确记录本次是否真的读取文件。它产生的 definition 与 `bind_new_input` 相同，路径仅进入 provenance。

源码还提供纯 CLI，接受完整 origin 文件和一个实际 current-binding JSON 及两者的字节 SHA。它不创建 current base，不把 JSON 声明冒作数值构造；科学 driver 直接传自己已经真构造的完整 base 即可，不需要新增 CLI 前置关卡。

## 05 bootstrap 与历史责任边界

根 README 第 8、13、15 条约束执行位置与可再生数据保存；题 README 明确允许换机制，同时最终精化必须固定同一个 g、参数和 t 范围。当前完整 4e reference 的 model 明确写 `old_optimized_q_field_required=false`、`old_nonlinear_directions_required=false`。其输入是全 warm、准确 scalar、全部 symbolic nodes、正权 observation 与明确提供的历史 manifest；它不读取旧 606/359f/R696/integral 的优化场。因此新 run 的完整 warm + 4e bootstrap 是 A（严格原定义再生）与 B（新独立实际输入）的共同真实必要输入，可以立即执行，并保留 `finish_when_done=false` 后续队列。

从科学数值依赖看，gamma 的 `base.initial()` 不需要先运行 3、17、21、26 的优化；这些旧方向在新完整队列里只可能承担额外永久位置来源。是否省去它们必须与历史责任分开判断：

1. 若只是报告路径、用时、压缩归档或其他 provenance 导致 identity 改变，而实际固定标量法则和材料坐标还是同一输入，就不能以新 schema 或 `same_mathematical_g_claimed=false` 为由丢掉已要求保留的同目标永久地点。完整十字段 binder 没有授权这种删减。
2. 若明确选择一个新的数学输入/研究分支，并从该分支真实 reference 的完整初始历史开始，旧算法场不是必需父；可以直接开始新 gamma 机制。报告须只声称自己确实提供并读取的历史完整，不能声称旧同目标后继地点已继承。本分支此后发现的每个位置仍进入它自己的永久集合，所有 full variables、mean/cross、原 C、真筛和最终完成标准都保留。
3. 当前 4e 同命令重建尚未返回新的实际标量/材料 chart，因此现阶段不能用未知新字节摘要证明已满足上一项的“新数学输入”。直接允许 bootstrap 并不预先裁定历史省略，也不需要为了该判断重跑无数值依赖的纯归因/旧失败。

这份源完全不读写位置集合，其 provenance 明写 `permanent_location_or_constraint_history_removed_by_this_binder=false`。caller 必须按实际选择明确提供全部应继承 manifest；新 binder 不替 caller 默默删行、不重标旧 C、不继承旧场值或证书。

## 完整源与实际检查

最终完整源为 `new_reference_literal_zero_moment_input.py`，22763 bytes，SHA256 `ea94cff11a975b44a6f91d46d3d08423ce386225b6eb8154bfb3f834706c9e39`。本地实际运行了标准库 AST、`compile`、字面重复 dict key、尾空白及 import 白名单检查；只含 argparse/fractions/hashlib/json/math/pathlib。两位同伴按当前 7f/4e/e091 全字段独立文字核对，未发现接口阻断。这些检查不构成新的科学执行门，也不宣称实际新输入已产生。尚未在 Actions 执行，无新场、Phi 或连续认证结果。
