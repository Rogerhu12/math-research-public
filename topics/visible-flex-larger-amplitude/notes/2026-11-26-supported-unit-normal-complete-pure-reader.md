# 新固定支撑单位种子的 normal-chain 完整纯读取器

本说明对应独立源码 `scripts/resume_20261126/read_supported_unit_normal_lift_so3_report.py`。它把新固定种子及其实际内部求解记录接入原完整 normal-chain 读取链；不计算场、积分、根、矩阵谱或新的数值科学结果，不替代 R707–R709 的条件与误差责任。新来源身份的改变也不删除原来的永久地点或约束历史。

## 1. 完整来源与具体变化

新读取器完整 SHA256 是 `d788f4f07559b9375247874abbd57ec7d493a1cb4f543b8ab9f31f8dab3d128b`，UTF-8 字节数 56534。它精确绑定实际完整 driver：

- `fullclosed_supported_unit_normal_lift_so3_qp.py`，SHA256 `e482428ee68aefa23da5b3b5c0a6b3363f047b0457f67a9193044ef151caec35`；
- report schema：`complete-supported-unit-reference-fixed-normal-plane-SO3-QP-v1`；
- normal model schema：`complete-supported-unit-reference-SO3-fixed-normal-plane-six-control-zero-layer-v1`；
- 新 pure readout schema：`actual-complete-supported-unit-fixed-normal-plane-SO3-scalar-readout-v1`。

原完整读取器 `read_zero_normal_lift_so3_report.py` 的 SHA256 为 `8381cd9e034fda5917cae5f221f0c3f5420953cab6ca8dd809c82f3de0f7e1e8`。新源码保留其全部正文，独立改变 driver/schema 路径与三处来源接线；新增两个完整种子绑定函数。

纯 AST 对照确认以下十个函数逐体相同：`sha`、`canonical`、`load_pins`、`normal_dimensions`、`endpoint_roots`、`bind_snapshots`、`statistic`、`geometric`、`direction`、`main`。只有 `bind_literal_input`、`endpoint_metadata`、`read_report` 接入了新来源，新增 `supported_seed_binding` 与 `supported_seed_metadata`。全部 34 个当前点 normal snapshot 键与新 driver 完全相同；没有只从末次 metadata 回填旧 trial 的根数据。

源码来源表仍由新 driver 的完整字面 `SOURCE_PINS` 解析得出，且逐项复读当前公开文件的 SHA256。新角色分别为：

| 角色 | 实际源码 | 完整 SHA256 |
|---|---|---|
| 原准确标量参考接口 | `so3_axisymmetric_reference.py` | `4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3` |
| 固定支撑种子 provider | `supported_unit_meridian_reference.py` | `30ea80ec0673f3bdff3e59b97dfb5f7166a296aeb4b989fbca18b2feb5e9544c` |
| 均值与两阶角 jet 核 | `supported_unit_seed_mean_jets.py` | `bd9c0761e101679b10ff52d50f27a3dfb964687130c59878d756389b304ee771` |
| 新完整 base | `so3_supported_unit_meridian_operator.py` | `e1bb7303540b1e807176ca5e71dcb2798b3f1e4e34909cd207cea300a9d4ebc0` |
| 新完整 normal layer | `so3_supported_unit_normal_lift_operator.py` | `5297192216356970140585eb9e56c521d9f35453211fb5a76086b713350eaa67` |
| 新全变量几何适配 | `so3_supported_unit_normal_lift_geometry.py` | `d84b540d21622d4d609efa5ea85fef432a2dcebb51bea0f3c7c24376294918f4` |
| 新 12 字段纯输入绑定 | `supported_unit_literal_zero_moment_input.py` | `9fecbe018442be23d0c36d139ebb6ba3574b550aed76ef89cdcadd279770b0d6` |

上表只列新接线的核心角色；读取器并未把 driver 中其余完整来源、原 Q 参数来源、完整 QP/谱目标/历史/几何选择器删除。

## 2. 新输入的完整闭包

本入口只接受显式模式 `supported-unit-reference`，外层类型为 `supported-unit-reference-literal-zero-endpoint-Q-input-v1`，定义类型为 `supported-unit-reference-literal-two-bubble-endpoint-Q-v1`。它不把旧 same-reference 或旧 ea94 new-reference 类型重贴成这一新类型。

读取器先核新纯 binder 的完整字节，再调用其 `bind_to_base`。完整 12 字段定义必须同时保持：十八个 literal Q 字、两个准确支撑、当前准确 scalar definition/identity、当前原 reference bundle/model、当前 base model、原始完整自由点、固定 chart core，以及整个新 supported seed definition/identity。历史 05dc/26b 的来源仍只在 provenance 中；它不证明当前矩阵是真积分逆、当前 root 存在或当前几何通过。

独立的 `supported_seed_binding` 再把同一个完整种子逐层核到：

1. 顶层实际 report 的 `supported_unit_seed_definition` 与 identity；
2. normal model 的完整固定种子；
3. base model 的完整固定种子、provider/mean SHA 与完整工作规则；
4. Q 输入定义中的完整固定种子；
5. 原 4e reference model、完整固定 scalar law、固定 chart 与原 reference bundle；
6. 实际 context 的五个原文件记录：reference bundle、carrier、node report、scalar input、preparation report。

原参考角色 `reference` 始终仍是 4e；新 provider 单独占 `seed_reference`。固定种子的 core 与 H 来自原始参考点，但外层当前 core、全部 omega、H 仍自由。新 driver 明确拒绝把旧 7f 或不同参考场 checkpoint 当作此种子；读取器也拒绝非空 `direct_base_seed`。真正同新来源的 restart 仍由完整 driver 校验后重新读初场、度量和几何。

这些逐项检查属于实际来源与字段一致性校验，不会在本地重新构造任何物理场，也没有为求解新增收缩、秩、几何或精度门。

## 3. 固定种子的实际返回与当前 normal 根分开

实际 provider 的记录路径是：

`latest_operator_metadata.base_complete_metadata.fixed_supported_unit_seed`。

这里必须仍匹配同一个 provider source、完整种子 model/identity、完整 binding、工作规则与原 scalar target。它的缓存只按原固定参考与 literal angle 工作，不能被解释成当前外层自由点的 normal 根。

纯读取器保留以下真实记录：

- 原 provider 的实际计数、完成 literal angle 数、实际成功 mean batch 数；
- 每个完整成功批次的 literal angle 字、bd9c 来源、原 core/H 与所有三分量、五段角向 profile、两阶角 jet；
- 实际完整 radial plan，含所有原 cell、正权 boundary/complement 节点及无限 scalar 尾；
- 最新真实 provider failure 的阶段、原因、原记录与 source/seed/scalar 身份；
- 原 scalar carrier 误差记录；它不会被改称 normalization、积分、根或完整场误差。

成功 mean batch 要显式完整；内部三分量不能丢，中央五段不能删。但成功 mean 的 Jacobian 不是当前 normal-control 的右逆证书。读取器保持 `seed_mean_inverse_is_not_normal_control_inverse_certificate=True`，并保持全部连续证书旗标为 false。

provider 的实际顺序是在保留缓存数组、增加完成计数之后，写 runner 缓存文件并追加完整 batch record。真实文件写入中断可能留下已经缓存的值而尚无该批完整记录。因此读取器把以下数量分列：

- `completed_literal_angle_count`：实际缓存记录；
- `complete_batch_recorded_angle_count`：完整批次记录中的角数；
- `complete_batch_records_match_cached_angle_count`：两种范围与实际计数是否一致。

它不把写缓存失败改称均值成功，也不因这个可能的真实中断而覆盖原失败报告；更不会用较大的一个数冒充已经完成当前整角 normal 证明。已经列为完整的不同 mean batch 不得重复同一个 literal angle。

## 4. 原完整数值归因保持

当前点 root snapshots、工作 root policy、共同准确分段、6 控制/3 增量/每段 9 维及全 $6m/9m$ 角向隐式维数继续使用原完整核验。每个 snapshot 必须绑定自己的当前自由点、模型、source 与 policy；旧 trial 不能用后面的根状态补填。

原 `statistic`、`geometric`、`direction` 逐 AST 不变，因此：

- 全部度量行与固定 scalar 身份继续核对，跨目标 Phi 不相减；
- 原选择器前缀、附加幅度行和全部真实 trial 保留；
- Phase I 公共 slack 继续与真实物理违约分开；
- metric 接受仍须同目标实际下降与完整真实几何通过；
- restoration 接受仍须真实正违约下降；
- 初读根/种子失败继续返回 incomplete，不产生初场、末场、已接受方向或闭合等距结论；
- 未实际产生 final bundle 的报告不因纯 reader setup 强行要求 final 文件而丢失归因。

新种子数学上采用单位切向与端点均值定义。这个准确定义的径向恒等式与工作浮点径向 Gram 残差始终分开，数值径向行没有删除。任何数值结果都仍须支付 R707/R709 所列实际根、完整尾、积分、角分支、normal 链及浮点费用后才可能进入连续证明。

## 5. 可执行读取入口与公开摘要

使用完整原 report 的实际路径；新输出必须不存在：

```text
python {repo}/topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_supported_unit_normal_lift_so3_report.py \
  --repo {repo} \
  --report {actual_supported_normal_outdir}/report.json \
  --output {fresh_pure_readout_path}
```

`--verify-final-bundle` 只有在报告自身 `complete=True` 且实际 final 文件存在时才触发完整字节复核；这不是记录初读失败的前提。Actions 控制器的纯读取 stage 可以保留实际存在的原 reference 作为 setup parent，而不要求可能未产生的 final。

可增加的 scalar-only 摘要选择器包括 `supported_unit_seed_identity_sha256`、`seed_diagnostics.completed_literal_angle_count`、`seed_diagnostics.mean_successful_batch_count`、`seed_diagnostics.complete_radial_plan_available`、`seed_diagnostics.last_seed_failure_phase`、`seed_diagnostics.last_seed_failure_reason`。不要把整个 `seed_diagnostics`、`mean_batch_records`、counts 对象或 normal batch 作为标量摘要。完整科学 raw 与缓存仍留 runner；公开只发布紧凑实际值、完整身份及失败归因。

## 6. 已做的验证与未做的工作

仅做了源码验证：完整 AST/compile、重复字典字面键、尾空白、新 driver SHA/schema、全部 34 snapshot 键、十个原函数逐体 AST 相等，以及仅 stdlib 的 `--help`。没有导入 scientific provider、构造场、运行 mean/normal 根、积分、F/J/J*、SVD 或人为 fixture。

本文件编写时，新种子的真实 report 尚未返回；没有预填种子、根、曲面、几何、完整相位或 refinement 成功。
