# 实际 coast 修域点到完整 current-C BVP 的最小参数交接

作者：AI（ChatGPT）。状态：独立源码接口；尚未消费 request180 的实际成功输出，未生成新 BVP 配方，未运行科学。本文不修改已发表 request179，也不把区间修域、数值求解、连续目标及闭曲面责任合并。

## 当前接线边界（2026-11-15，root补记）

当前 request180 只恢复旧 actual165 的小结果、准确输入盒与历史 core；它没有 fresh-C 输入模式，也没有与下一次完整 BVP 连成同一工作流。这里交付的是可复用的输入组件，尚不是已执行或可直接派发的后继。本文第2节的步骤1–2是后继待实现合同：先取得新 C 的真实现场，再在该现场沿180修域算法重新选择或核实准确初点，真实调用原 factory 后才交本适配器。旧180选中参数可以作为明确候选，旧域通过不能直接转给新 run/包围对象。

本源码严格比较 continuous_tail、actual_enclosure_leaves、core_input 等完整对象；直接把旧180 definition 送给新C factory，会因来源或区间对象不同而不能完成交接。不能为通过此检查只改 provenance 标签。未来优先补最小 fresh-C 修域入口，再保持本组件的同现场比较；不为尚未发生的非精确投影扩展另一套算法。当前没有选中 beta、新BVP请求号、后继源码或成功结果被预填。

## 冻结源码与已读接口

本次独立源码 [geometry_20261115_accurate_coast_selected_bvp_inputs.py](../computations/geometry_20261115_accurate_coast_selected_bvp_inputs.py)：21,230 B，SHA256 `37ea635a6673e6cac3b41622ae3557075904184d6371c48385e335afaa43c6cf`，Git blob `7a7e7b7e76d1cf71ab63f3963c2fec2df835c48d`。独立读取原源码和 request180 producer 已明确字段后写成；没有本地 import、AST、编译、求解或实际运行。这次只创建小文本 blob，没有移动 branch/ref。

| 原直接依赖 | 字节 / SHA256 |
|---|---|
| `geometry_20261115_continuous_nine_scalar_factory_v3.py` | 42,270 / `0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e` |
| `geometry_20261115_continuous_nine_scalar_numeric_v3.py` | 22,469 / `7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60` |
| `geometry_20261115_continuous_C_full112_binding.py` | 42,658 / `c0bda3350b30b9659c326112eaf8f411d0bb6f825a7a3f81fcc6c7502ed3f952` |
| `geometry_20261115_current_C_riccati_full453_physical_dn.py` | 63,057 / `76c51a05c8ce40f78225aa3bfbd5db2b1ac39e0d6fb7f8b84f02e0dfaafd122f` |

原模板为 `current-C-riccati-full453-physical-DN179-recipe.json`，10,294 B / `d926cecf92f35cf4c7ae8cc86ad243287846d73df98c78e8ba1005c568ab8811`，已发布 source `ccf1b02341f365e4b6eff5d5eeeba9be2b0487ad`。实际 selection producer 的最终源码 SHA 由未来公开 request 与必需 CLI 参数同时绑定，不在这里预填未冻结或未来实际结果的身份。

已有目标结构与范围沿 [R300](../results/R300-continuous-nine-control-scalar-family-and-cut-calibration.md)、[R383](../results/R383-accurate-R323-target-identity-and-coast-control-necessary-band.md) 及 [request179 总接口](2026-11-15-request179-Riccati-far-and-current-profile-full453-interface.md)。本次没有重复建立新数学验收标准。

## 1. 唯一选用的直接路径

接收原 request180 producer 真实返回的 selected_profile。其准确九系数来自同一 R323/R300-v3 完整表达式，原 C 语义叶、core、长度、cut、全部控制支撑保留。先逐个读取 producer 的实际 binary64 原词，并以完整有理恒等式核该词恰表示对应准确系数。九项全部满足时，使用这些原词生成原 request179 三活动参数配方；初始准确九点完全一致。

本接口不实现一个尚未发生的非精确投影分支。若实际 selected_profile=null，或者任一准确系数与其实际词不同，报告直接交接未完成、保留原来源及投影差，不生成 BVP 配方。这个输入身份结果不是原 BVP 的新域门、容差、试步或数学失败。

共同 2 的负整数次幂缩放通常保留原 binary64 系数的准确表示，但本入口不预先据此宣布任何实际九点可表示；必须读取真实输出。

## 2. 原源码的准确接点

已有原 driver geometry_20261115_current_C_riccati_full453_physical_dn.py 的 read_recipe 接收九个有限数字，prepare_problem 依次创建 CurrentProfile、three-active view、完整338物理状态和112 core，保3个活动参数。因此当前问题仍453维，原 source seed 的全部物理/core分量仅作初猜，公共 u 重参数化后所有新 RHS 重新求值。

现有 CurrentProfile 来自 geometry_20261115_continuous_C_full112_binding.py。它的 bind_definition 要求真正原 factory result 与 definition 双向一致，包含原 producer SHA、原九系数、实际新 recipe、core、完整 C 输入及真实 cut 两jet。不能把 request180 自己的 selection result 改标签成原 factory result。

最小无需改原科学源的顺序为：

1. 同 job 生成原完整 C 及实际 cut 两jet，并按原 R323 产生原待修域表达式。
2. 执行 request180，保其真正选中的新 recipe、准确 definition 和完整必要摘要；没有选中便明确没有本接口的实际初点。
3. 用该新 recipe 及同一个实际 C、cut、core 文件，真实调用冻结的原0d893 factory。其结果可以继续报告域未决；不增加新的 factory 域通过要求。此步用于取得原 binder 要求的真正 producer 结果，不能伪造。
4. 独立薄参数适配器完整核三方数学定义、九个准确系数、实际词和原源，生成原179输入格式的新配方。
5. 原179 driver 消费这一真实新 factory 结果和新配方，经当前 profile 实际 H、同一 live native/J、原 FD、原完整 BVP、原末 fresh audit 继续。实际请求号由未来明确请求给定，本接口不预造。

第3步是新增真实原 factory 调用，必须计入未来资源计划；不是免费已付步骤。它仍使用现有完整两个域遍历实现和原预算。适配器不重新执行原域算术，更不把其成功作为另一个 BVP 门。

## 3. 输入及实际出处

适配器只接受真实文件和明确 SHA，不发网络请求。所有科学数据在同 job 的自有临时目录，读取完整原 bytes 后绑定；不从 Git/Release 拉取已删除的 raw。

| 输入 | 来源与用途 |
|---|---|
| selection summary及SHA | 原 request180 原摘要，含选中点及逐词投影；未出现真实结果不能填入 |
| selection source及SHA | 同 checkout 的准确原 producer，来源由未来明确请求 pin |
| selected recipe | request180 输出的真实新有理配方，原 bytes 不重序列化后冒原件 |
| selected definition | request180 用原 factory.definition 实际产生的新准确数学对象 |
| factory directory/result SHA | 用新 recipe 真实调用冻结原 factory 的结果 |
| 原179 BVP模板 | 已发布 ccf1b023… 的完整原配方，固定SHA d926cecf…，只取已明确算法/初猜合同 |
| 4个直接旧源 | 原 factory、numeric、CurrentProfile binding、完整179 driver，逐源码SHA核同 |
| 实际未来 BVP 请求号 | 显式 CLI 数值，不以179/180冒后继实际运行 |

其他完整源闭包仍由原 driver/request 的原检查承担，适配器不会把4个直接源核误称完整科学闭包已经执行。

## 4. 比较的准确数学对象

比较原 schema/source、完整参数顺序、九准确系数、表达式 DAG、所有 pieces、全部支撑、所有根节点、core_end、cut_radius、root_choice、连续尾完整身份、core来源、实际 E0/E1/E2 闭盒及构造条件。cut 控制的语义值保持原 C 中的值；区间中点从不写回准确目标。

同 job 原 factory 的操作性域遍历可能产生不同计时和报告文件 SHA，所以不能用一次新的 result SHA 强迫原 selected definition 原 bytes 完全相同。两件完整原字节身份各自保留，同时比较所有数学定义字段；不把未比较的操作日志宣称成数学恒等证据。准确九系数按有理值比较，零的数值表示符号由原 binary64 word 独立保留。

需要同一实际 C/cut/core 输入对象；不可将后来重算而包围不同的 cut 盒或其他根族悄悄替换。若这些身份/表达式不同，交接明确失败，不把“同一个模型名”视为同一实际目标。

## 5. 九词与有限搜索影子的区别

对第 i 项，实际 producer 给出准确有理数 c_i、binary64 原词 w_i、其文字值及投影差。适配器按原词解码 x_i，核文字值回到同一16位十六进制词，核 finite，核 Q(x_i)=c_i，核 producer 自己的 represented_exactly 与准确投影差。这是准确字词身份，不是科学重求解。

九词全匹配只说明初始参数点没有投影换目标。数值 profile 仍会用已披露的 semantic leaf 中点和有限多项式运算；原数值长度、有限接缝词和完整 RHS 不能因此被认作同一准确 C 的已认证求值。原 public u 下准确长度 L_true 和数值长度 L_numeric 的区别、R326 比较责任以及准确目标 metric 误差责任全部保留。

原 p1/p2/p3 仍可在 BVP 内活动，theta1..3/eta1..3 仍冻结为真实修域点词；不新增活动参数、不删控制。当原求解走到新 p 时，request180 对初点的准确域结论不自动覆盖后继 p。最终接受点需按其自己的准确系数支付连续域/metric责任。

## 6. 只允许更改的配方字段

生成配方继续使用原179输入 schema，因为原 driver 支持这一输入格式；它不是伪造一个179实际结果。原 source_commit/run_id 在真实科学执行中由原 driver 记录。

只改 request_number、initial_nine_parameters、initial_parameter_origin，并新增 actual_selected_coast_input_binding。其余模板键逐JSON值比较不变，包括：

- lambda=.001、完整699×453原初猜及历史8bd2671身份、原五数学输入；
- 完整112模态/338物理/112core/3活动，341左/112右边界；
- 原17内试探、outer8、max1200、RMS1e-6、BC1e-11、FD5e-5；
- native32轮、原10档、严格下降、tol2e-9、eta1修正、eta0全112敏感度；
- 当前 R375/R357 true-far、真实mu、完整候选取向单位行以及全部未付范围；
- 同一 live client、当前 H/J 和原 fresh audit；
- 原资源/信号/读回及条件清理策略。

新 factory 调用消耗未来实际资源；原 namespace 仅启动剩余裁剪的性质不改变。不能把工作计划的剩余时间说成全链必完成保证。

## 7. 输出与未付范围

正常适配器产生一个小 original179格式配方和独立自己的 result；生成配方有实际 bytes/SHA。报告保全部输入身份、9项准确系数/词/投影差、数学字段相同比较哈希、原 factory 域状态和允许的字段改动列表。没有 J、残差、全状态、数组、准确场或成功证书输出。

单份必要摘要≤90000B；超限不分块，只报原bytes/SHA和未完整返回。源身份/实际文件错误记录原错误，直接未选/非精确投影记录其真实原因。适配器本身没有 BVP/native调用；它不清理任何上游数据。后继 workflow 仍必须在真实原读回完成且进程停止后按所有权清理。

本接口不是新求解验收门，不宣称 request180 已有成功结果，不把原当前BVP或闭曲面问题当已完成。它准备的是实际修域点一旦生成后可以直接使用的、来源严格区分的输入接点。

## 8. 准确选中协议与 CLI

消费 schema 为 `request180-accurate-R323-coast-three-coefficient-repair-v1`。顶层必须来自实际 request180；`selected_profile` 非空时，原 `full_accurate_nine_domain_proved` 必须为 true。这个原布尔由完整418个不变片与 coast 片的已完成域遍历一起决定；本适配只引用被冻结 producer 的这个合同，不冒重新读取或重算全部域 ledger。

`selected_profile` 中实际读取：

- `parameter_order`、`nine_parameters_exact`、`beta_exact`；
- `recipe` 和 `accurate_definition` 的完整 bytes/SHA；
- `factory_source_sha256`、`new_selection_source_sha256`、`continuous_model_schema`；
- `semantic_C_remains_original_all_root_family`、`full_length_expression_unchanged`；
- `binary64_projection.all_nine_exactly_representable` 和全部9项 `parameters` 行：parameter、accurate_rational、binary64_value、binary64_word、represented_exactly、exact_projection_difference。

投影差的符号明确为 `Q.from_float(binary64_value) - Q(accurate_rational)`。原 word 是 little-endian 8字节、16个十六进制字符；负零也按实际词保留。准确零本身不编码符号，两层责任分别保存。

当前 producer 的原临时文件名为 `selected-accurate-nine-recipe.json` 和 `selected-accurate-nine-definition.json`。不要求这些 raw 将来常驻仓库；未来同 job 必须真实重新生成。只从历史必要 summary 拿一串参数而没有本次原准确对象和来源，不满足这个输入接口。

CLI 各身份均在实际文件生成后计算：

```text
python geometry_20261115_accurate_coast_selected_bvp_inputs.py
  --selection-summary ACTUAL_SELECTION_SUMMARY
  --selection-summary-sha256 ACTUAL_SELECTION_SUMMARY_SHA256
  --selection-source PINNED_ACTUAL_SELECTION_SOURCE
  --selection-source-sha256 PINNED_ACTUAL_SELECTION_SOURCE_SHA256
  --selected-recipe ACTUAL_SELECTED_RECIPE
  --selected-definition ACTUAL_SELECTED_DEFINITION
  --factory-directory ACTUAL_ORIGINAL_FACTORY_OUTPUT
  --factory-result-sha256 ACTUAL_ORIGINAL_FACTORY_RESULT_SHA256
  --template-bvp-recipe ORIGINAL179_TEMPLATE
  --code-directory CURRENT_PINNED_COMPUTATIONS
  --bvp-request-number EXPLICIT_ACTUAL_NEXT_REQUEST_NUMBER
  --out NEW_OWNED_TEMPORARY_DIRECTORY
```

上面的大写词只是参数位置，不是新请求或实际结果。入口强制 `GITHUB_ACTIONS=true` 与原 repository；真正 original factory result 的 run_id/source_commit 必须为当前同 job。原完整 mathematical keys 比较完成后，新配方输出名为 `current-coast-selected-BVP-recipe.json`，来源摘要为 `result.json`。

退出码0表示本次输入绑定和新配方生成完成；3表示没有实际选中对象或不能直接保准确点的投影；2表示完整原来源/字段不符或原读取异常；70表示单摘要超限未完整返回。任何码都不等于原 BVP 科学接受或拒绝。原科学调用、输入完整性和最后读回仍由实际未来工作流负责。没有当前场、没有实际 beta、没有新请求号、没有接受结论被预填。
