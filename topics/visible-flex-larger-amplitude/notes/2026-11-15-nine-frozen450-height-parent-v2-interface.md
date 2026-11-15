# 九控制同一 g 的450重构 v2：显式绑定原九设计及 H(s) 两类真实父场

类型：独立源码与完整接线合同，尚未执行科学计算；没有未来接受场、参数、λ或run。
作者：ChatGPT / exact_refinement（AI-assisted）。日期：2026-11-15。

## 1. 本次唯一变化

公开的 [九冻结450接口](2026-11-15-nine-control-frozen-same-metric450-interface.md) 中，070b profile只允许原00e4九设计producer或自身1610接受场。新的九控制 H(s) producer有独立schema、source及完整来源闭包，不能把其接受场改标签为00e4。因此本次另建两个 v2 文件，公开070b/1610一字不改。

新profile明确接受两种实际453设计父：原00e4直接当前H入口，或0433九控制 H(s)入口。二者都必须真正经过原完整 fullDN 接受；中间 H(s) 收敛、prepared、pending、driver摘要、低三候选和失败响应均不能作接受父。新的450仍是原全部九末系数冻结、K=k=0、物理338+自由core112、左338/右112，没有三个固定低核目标。

这是**来源兼容**，不把 H(s) 成功继承成450成功，也不在新450入口中自动执行 H(s) 路径。原450的当前H真实solve/J、原FD、同owner完整band/fullDN、finalJ和fresh audit全部保留。是否以后为450显式接 H(s) 是另一个算法接线问题，本次没有偷加。

## 2. 独立文件和不可变基线

| 角色 | 文件 | 字节数 | SHA256 |
|---|---|---:|---|
| v2完整标量与父绑定 | `geometry_20261115_nine_control_same_metric_profile_v2.py` | 26005 | `5e95afdb82f83a276003e6a4846e20893b7eb7f2b44b309d56950f11dbfaa0d3` |
| v2完整450入口 | `geometry_20261115_nine_control_same_metric_full112_v2.py` | 42405 | `92cfb0701824df770dfcd009a623e84695e72fe9c489d70537d8983415adc7e8` |
| 原profile基线，不改 | `geometry_20261115_nine_control_same_metric_profile.py` | 22140 | `070b9b35c3d31c5073cd7da5b7afbdaa1150a38a94861c70eea60a39f0c85647` |
| 原450基线，不改 | `geometry_20261115_nine_control_same_metric_full112.py` | 40951 | `1610d6fb4b8bbc953585b91d86e235a524ec25551de0df3c633552312cdab00d` |
| 新九H设计父定义 | `geometry_20261115_nine_control_height_continuation_full112.py` | 46089 | `0433e1014a4d55ca52554ec5b17e9afa1d01a3b8e376d2afda890b26c35aa924` |
| 原完整H路径helper | `geometry_20261115_original_tail_height_path.py` | 23078 | `e830a1679908cdc0cdd8c1ecd5663bbf6b82b24a3d52e44cf678aedc227eee48` |

原两个450基线见公开commit `0a7a0c88e20b3f7b69bf4dedf6cf347e4c6cdf81`。原九设计00e4为 `00e4d2c3413cfa6c1df915b9d85050bf375ab88c04e8756149d4ea0533ef3bd8`；九family为 `086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629`。0433的实际冻结源码、完整PINS及原e830政策均按原文本绑定，不引用未来数值。

## 3. schema与协议

| 对象 | 明确schema |
|---|---|
| 原00e4设计父 | `nine-control-three-active-nonzero112-complete-physical-DN-v1` |
| 新0433 H(s)设计父 | `nine-control-height-path-three-active-nonzero112-complete-physical-DN-v1` |
| 新冻结标量 | `frozen-nine-control-complete-same-metric-scalar-v2` |
| 新450场 | `nine-control-all-frozen-same-metric450-complete-physical-DN-v2` |
| 新450请求recipe | `explicit-nine-control-frozen-same-metric450-recipe-v2` |

`DESIGN_NAMES` 是上述两个设计schema到各真实basename的显式映射。源SHA按实际basename绑定，不用宽泛schema前缀、旧v3/v4回退或producer重命名。

`nine_control_full112_implementation` 仍是两个真实设计producer已导出的原键。新helper同时检查父顶层与binding的source、binding.schema、完整四数学输入、active `[0,1,2]`、frozen `[3,4,5,6,7,8]`、fixed_modes=3，以及**全部** `consumed_source_sha256` 字典。该闭包按原00e4 runtime已经绑定的实际source集合及0433原PINS构成；原height producer的PINS包含00e4基线，因此没有漏掉旧三active数学来源。

新入口只调用一次原00e4 runtime建立科学环境；随后读取0433模块的原PINS及源码身份，构成它真实声明的来源闭包。不会调用0433 runtime/main、其prepare/solve或H路径。v2自身闭包再包含新helper、两设计source及e830，并由实际v2入口SHA闭合。不能把父的闭包改成新consumer闭包。

v2自己的后继接受父仍使用 `nine_control_same_metric450_implementation` 键，但要求顶层精确v2 schema、v2入口SHA、空active、九冻结、fixed_modes=0、450维及自身完整闭包。原v1 own-schema不是v2的隐式回退路径；它的冻结源码仍可独立使用，本次没有实际v1父被遗弃或改标签。

## 4. H(s)父回执如何保留

0433的 `original_full_solve/write` 与00e4整函数AST相同，仅全局SCHEMA/source实际变化。真实fullDN的 `actual.json.gz` 仍保原 `success=true`、`status=0`、全部原RMS/BC判据、`actual_tail.final_response_sha256`、完整physical/core/mean、material/cut及实际终态数组。本v2继续调用原 `original_acceptance_receipt`，该函数与070b完全相同，不放宽门也不添新数值门。

0433父还必须具有其实际成功端点后才写入的以下原binding字段：

- `original_00e4_adapter_baseline_sha256`：真实00e4。
- `height_path_helper_sha256`：真实e830。
- `height_path_policy`：e830完整原 `POLICY`。
- `same_original_tail_worker_for_height_path_FD_fullDN_and_final_audit=true`。
- `intermediate_height_convergence_not_full_DN_acceptance=true`。
- `completed_height_path_status={file,bytes,sha256}`：原相对文件 `height-path/height-path-status.json`、实际正bytes与完整SHA。

这些字段逐原值复制到 `origin_design_field.height_path_provenance`，并同时保 `origin_design_field.schema/source_sha256/file_sha256/file_bytes` 与 `producer_source_binding` 中原完整source闭包、原四输入SHA。原00e4父的origin不允许冒加H路径标签。

本次只从实际父文件中核对并保存回执身份，**不声称已另读或复算该临时status原payload**；其真实性由明确冻结producer的原写入路径和完整父bytes绑定。没有把路径receipt当成当前450的native cache、成功响应或新验收。以后自身450继续时原origin及该回执原样保留，不重新选九系数或重造历史状态。

## 5. 完整九标量及有限求值路径保持

参数固定顺序为 `[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]`。所有九末值、原支撑、原stored width、完整port、原accepted96来源和嵌套三参数基定义必须重新构造并与实际完整九scalar spec一致；active空向量不能冒成冻结系数为空。

`FrozenNineProfile`、`reconstruct_nine_design`、`frozen_flow_class`、`serialize`、`finite_assembly_contract`、`scalar_identity_payload` 与070b逐AST相同：

- 点求值仍调用原00e4 `ThreeActiveView.profile(s, fixed_p[:3])`。
- 批求值仍调用原 `AugmentedFlow.scalar_jets`，把相同前三末系数按原布局重复到各节点。
- 六shape的原加法顺序、原zero-skip、stored宽度、点路径矩阵乘法和批路径einsum均未重排；未用低三search的另一种求和路径替换。

新scalar外层schema与重构source身份变为v2；其内层标识同一九函数及有限求值责任的 `canonical_scalar_identity_sha256` 仍由原 `scalar_identity_payload` 定义。来源版本变化不能据此误断物理g变化，反之只有系数相同也不能忽略实际有限求值路径。未承诺不同运行时、批布局或平台逐位相等。

全父physical338/core112字节保留，三个active末系数只转成完整冻结scalar事实，不把父节点残余漂移当成变化的g。保父所有节点、全部中点及literal knots；原父RHS不重标成冻结g的新RHS。原fresh RHS、Hermite初猜及节点/中点/两RMS预检、完整mean/material/尾的责任不变。

## 6. 原450运行入口及全部未付门

实际用户/后继请求须提供一个完整接受父文件及其SHA；本接口没有构造这样的文件或选择参数。调用示意：

```text
python -u topics/visible-flex-larger-amplitude/computations/geometry_20261115_nine_control_same_metric_full112_v2.py
  --recipe ACTUAL_RECIPE.json --expected-recipe-sha256 ACTUAL_RECIPE_SHA
  --accepted ORIGINAL_ACCEPTED96.json.gz --parent ACTUAL_ACCEPTED_PARENT.json.gz
  --tail-config ORIGINAL_T112_CONFIG.json
  --tail-client ACTUAL_ORIGINAL_CLIENT.py --expected-tail-client-sha256 ACTUAL_CLIENT_SHA
  --tail-source-root RESTORED_ORIGINAL_SOURCES
  --jac-workers 2 --max-nodes EXPLICIT_REAL_RESOURCE_LIMIT
  --material-angles 4096 --physical-angles 4096 --node-heap 1536
  --outer-iterations 8 --out RUNNER_TEMP/NEW_RESULT --work RUNNER_TEMP/NEW_FACTORS
```

Recipe只改明确v2 schema，其余原字段与检查完全沿1610：`parameter_order`完整九项、active空、frozen0..8、M112/N2048、实际 `parent_sha256`，`initial_guess_kind=complete-accepted-parent-physical338-core112`，`mesh_refinement=all-parent-nodes-plus-one-bisection-and-all-scalar-knots`，原accepted/config输入身份。不得传新的λ、九初参数、三个固定target来偷偷改变同g问题。

`--max-nodes` 仍必填；真实699节点二分为1397还可能加knots，资源不足明确返回resource状态，不能留旧1200上限而声称完整精化。`--prepare-only` 仍只产生未接受初猜。

原450 entry的 `prepare_problem`、`actual_boundary_fd`、`original_full_solve`、`main`、live owner、原临时生命周期均逐AST不变。当前H仍真实全112原词求完整J；原三方向/三步FD、17回溯、RMS/BC、全112右行、最终原native fullJ与fresh audit都实际执行。全九固定后只有450方形问题；不重新施加原三固定core目标，不把九维search冒平方BVP。

这两个源码不产生连续标量域/C²/seam/全t/reach/held/完整g算子证书。真正SavedPrefix/closed消费者仍需显式接受新450/v2身份及新九scalar；旧v3/v4 reader不能改标签调用。将来接完整连续E/Arb时也要完整九形状表达，而不是只通过旧 `ScalarExpression`。

## 7. 静态范围与交付

仅解析Python AST、比较源文本/字节与生成完整diff；没有导入科学模块、运行constructor、重建场、执行任何RHS/J/ODE/QR或建立数值fixture。

Profile旧函数中仅 `make_frozen_spec`、`freeze_parent` 有来源接线变化；新增两个纯身份函数 `checked_height_provenance`、`height_provenance`。入口旧函数仅 `runtime` 改变；全部科学函数和main原AST保持。没有新增workflow/request/阈值、没有修改0433或任何旧冻件。

完整相对diff和source-only回执置临时交付目录，均可由新旧源码重得；不作为新的审批、发布或科学通过门，也不提交可重算证书/大数据。后继只有真实接受父出现后才选择运行参数并在公开Actions执行。
