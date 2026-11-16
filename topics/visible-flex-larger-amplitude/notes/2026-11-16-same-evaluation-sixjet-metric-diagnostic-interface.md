# R519：同次六 jet 局部缺陷诊断的完整调用接口

作者：ChatGPT（AI 协作）。日期：2026-11-16。

本文对应 [R519 条件包含证明](../results/R519-same-evaluation-sixjet-local-defects-and-metric-consumption.md)，并使用已经发表的 [R514](../results/R514-complete-field-defect-transport-and-literal-residual-transfer.md)。这是独立、requestless 的 source 组合，没有新 workflow、run、数值完成或 source-ref 修改。新 consumer 实际在原 R459 measure 的同一次 target / field 求值后调用 helper；不是未调用函数清单。

## 1. 完整发表件与生成件

| 种类 | 相对 computations 的文件 | 字节数 | SHA256 |
|---|---|---:|---|
| 发表的纯局部 helper | geometry_20261116_same_evaluation_sixjet_defects.py | 15385 | f70474b3857b3decc0542ae50b5c32b107532cc739e529e818ec7264dfe1f2b4 |
| 发表的字面 generator | root_20261116_same_evaluation_sixjet_source_view.py | 9950 | 4ebd9c6a387bce5e4d0c377c17f0a6895f3b6bbc6acfff58b3dff72b4c80d18a |
| 发表的完整一 view 计划 | R519-same-evaluation-sixjet-source-view-plan.json | 18003 | e600977365ec57e527886065fc00823b26c1b75aee92f206ab2e0532187a8d32 |
| Actions 生成，不另入 Git | geometry_20261116_same_evaluation_sixjet_metric_evidence.py | 69439 | 8159e9f2e2d28fb31d27c719b54581d1db32b14935edefefec5b1730eda14781 |

基线是 geometry_20261116_fixed_target_complete_metric_evidence.py，62091 字节/494fea70b97404af2be8ef0f3d685fadc2f59c6a30ea3af771de98a56b868b05，正式来源提交 1f8213c7bd64ed064f959eca10c0ab5d4c973a0c。所有 source 固定完整 bytes/SHA；不能用 label 接受另一实现。完整计划列 17 条按序 literal 替换及各自唯一计数，最终输出全文件身份也固定。

证明发表在 results/R519-same-evaluation-sixjet-local-defects-and-metric-consumption.md，12851 字节/9df3edb40c02d1c92ebf0aef75f840527852c29033b869e701d07414feb649e3。当前仅三运行件和两篇文稿入库；完整 expanded source 与 full diff 是交接用源码文本，不能作为额外科学数据、归档或假旧源发表。五发表件总量约 75KB；单件均小于 100KB。

## 2. 真实 source HERE 与生成边界

Generator CLI 为 --computations、--namespace、--plan、--plan-sha256、--out，五项都必填。它要求真实公开 Actions、正确 repository、实际 computations 同时等于 generator 自身 HERE 与当前 GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations。不改 GITHUB_WORKSPACE、不复制私有 transitive closure、不伪造 source 根。

Namespace 必须已存在于真实 RUNNER_TEMP 下，out 必须是其中一个全新的子目录。它不创建或重开科学钟。原公开 R459/helper/plan 必须是实际 computations 中的普通文件；完整 SHA/bytes、17 个 literal occurrence count 和输出全 SHA 均实际核对。只对新 consumer basename 作 exclusive create，任何旧 source 或旧 view 已存在都会明确失败，不覆盖。

成功后该新 .py 就在真实 computations 中，后续输入的 computations 仍必须给这个同一实际目录。原 field/target/material loaders 因而仍从真实原路径按其固有完整 pins 读取。一个新文件存在或 source 数量匹配不构成任意未知动态 import 的一般闭包证明；原 R459 所需全部真实 closure 仍由原 caller/source 合同供应。

例如，未来同 job caller 已持有真实 namespace 和 source 环境时，可以实际调用：

~~~bash
python "$VISIBLE_COMPUTATIONS/root_20261116_same_evaluation_sixjet_source_view.py" \
  --computations "$VISIBLE_COMPUTATIONS" \
  --namespace "$VISIBLE_BASE" \
  --plan "$VISIBLE_COMPUTATIONS/R519-same-evaluation-sixjet-source-view-plan.json" \
  --plan-sha256 "e600977365ec57e527886065fc00823b26c1b75aee92f206ab2e0532187a8d32" \
  --out "$VISIBLE_BASE/sixjet519-source"
~~~

这是具体 CLI 示例，不表示现在已执行，也不填任何尚不存在的 field/accepted/first-material 文件。

生成元数据 schema 为 R519-same-evaluation-sixjet-source-generation-v1。out/result.json 记真实 run/source、generator/plan/baseline/helper/output 完整身份、每条 replacement 的原/新字节和 SHA、计数、实际 computations、阶段错误和 elapsed；它不记录数学成功。单份 frame 为 BEGIN/END_R519_SAME_EVALUATION_SOURCE_PREPARATION，成功 GITHUB_OUTPUT 为：

- sixjet_metric_view：生成文件真实路径；
- sixjet_metric_view_sha256：生成文件真实 SHA；
- sixjet_source_preparation：out/result.json 的实际路径；
- sixjet_source_preparation_sha256：该实际 receipt 的 SHA。

进入 out 创建前的环境/路径错误可能只有原 stderr，并没有 receipt；不得补造一个成功 receipt。创建之后的错误写 execution_error，complete=false，return 2，已生成部分也不能冒完整成功。必要元数据超过 90000 字节时只报告超限和已有原件身份，return 70，不分块、不输出伪完成 frame。Generator 不删除任何 source 或 raw，不操作 Git/ref，不 import/AST/compile/执行科学。

## 3. 新 consumer 的真实 CLI / schema

生成后 consumer 保原三种 mode：

~~~bash
python "$VISIBLE_COMPUTATIONS/geometry_20261116_same_evaluation_sixjet_metric_evidence.py" \
  measure --input "$R519_INPUT" --input-sha256 "$R519_INPUT_SHA"

python "$VISIBLE_COMPUTATIONS/geometry_20261116_same_evaluation_sixjet_metric_evidence.py" \
  compare --input "$R519_SERIES_INPUT" --input-sha256 "$R519_SERIES_INPUT_SHA"

python "$VISIBLE_COMPUTATIONS/geometry_20261116_same_evaluation_sixjet_metric_evidence.py" \
  readback --directory "$R519_OUT" --result-sha256 "$R519_RESULT_SHA" \
  --out "$R519_READBACK_OUT"
~~~

这些变量须由实际同 job owner 填真实已存在的原件和新输出地址，不能从旧 hash 恢复或伪填 accepted/checkpoint。

| 身份 | 当前新字面值 |
|---|---|
| 主 schema | R519-same-evaluation-sixjet-complete-relative-metric-evidence-v1 |
| measure input | R519-same-evaluation-sixjet-complete-relative-metric-evidence-v1-measure-input-v1 |
| series result | R519-same-evaluation-sixjet-complete-relative-metric-evidence-v1-actual-series-v1 |
| compare input | R519-same-evaluation-sixjet-complete-relative-metric-evidence-v1-compare-input-v1 |
| helper result | R519-same-evaluation-sixjet-local-defect-v1 |
| same-call target context | R519-same-evaluation-target-context-v1 |
| 小诊断摘要 | R519-same-evaluation-sixjet-local-diagnostic-summary-v1 |
| 必要 frame | BEGIN/END_R519_SAME_EVALUATION_SIXJET_METRIC_EVIDENCE |

Measure 顶层是原完整 14 字段加一个 bool，共 15 字段：

~~~json
{
  "schema": "R519-same-evaluation-sixjet-complete-relative-metric-evidence-v1-measure-input-v1",
  "label": "caller-supplied actual label",
  "namespace": "actual existing owned namespace",
  "computations": "actual computations directory",
  "proof_directory": "actual proof directory",
  "job_deadline": {"file": "actual file", "bytes": 0, "sha256": "actual complete SHA"},
  "first_material_transport": {"file": "actual file", "bytes": 0, "sha256": "actual complete SHA"},
  "first_plan": {"file": "actual file", "bytes": 0, "sha256": "actual complete SHA"},
  "first_assembly": {"file": "actual file", "bytes": 0, "sha256": "actual complete SHA"},
  "field": {},
  "work": {},
  "c_queries": {},
  "time_grid": {},
  "out": "fresh actual owned output directory",
  "sixjet_diagnostic_enabled": true
}
~~~

上例只是**字段形状**，其中 bytes=0 和文字占位不是可执行实际参数、原件或 receipt；真正 caller 必须以原实际 descriptor 逐字段替换。新 source 严格校验完整键集合和 schema，不能将原 R459 输入原字节和原 SHA 重标。新 flag 必须为 JSON bool；false 禁用旁诊断，true 只启用它，不增加原科学接受门。

原 field 完整六键保持：

- family：original112、resolution112 或 completeM；
- directory / result_sha256：实际 shared 原件；
- checkpoint_directory：实际完整 accepted checkpoint；
- cuff_atlas 与 continuous_e_result：真实 file/bytes/sha256 descriptor。

所有 identity 仍要求同实际 immutable GITHUB_SHA/run，保第一真实 construction、完整准确 C/root family、十词/DAG、第一材料图及原 clock。旧 C 中点、旧 Gauss 场、旧 source 标签或匹配十词不足以替代这些绑定。

原 work 十一个键完全不变：budget_seconds、free_bytes_reserve、interval_bits、sqrt_bits、initial_angular_depth、max_depth、max_cells、measurement_width_goal、metric_reference_eta、max_inverse_steps、max_phase_query_cells。原各参数合法范围、门和意义均沿基线；旁诊断复用 sqrt_bits，没有另给放宽精度、误差门或附加科学预算。

原 c_queries 十一个键完全不变：precision_bits、integral_absolute_bits、integral_relative_bits、analytic_guard_bits、integral_evaluation_limit、value_width_bits、integral_max_depth、inverse_max_depth、max_panels、max_nodes、budget_seconds。

原 time_grid 仍是 subdivisions 与 witnesses；每 witness 为 kind/coordinate/q/lower，真实完整 $k=0,\ldots,n$、各 piece membership 和闭端点不变。新旁诊断没有另取任何 $t$ 或任意缩小时间区间。

## 4. 真正 source 依赖与当前只覆盖三族

生成文件使用原 R459 的完整 FAMILIES，不重新命名/修改原数学源：

| 实际 family | 原 metric 源 | 完整 SHA |
|---|---|---|
| original112 | geometry_20261115_current_C_ten_live_query_complete_metric.py | 77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892 |
| resolution112 | geometry_20261116_current_C_resolution_live_query_complete_metric.py | fd263af28a7d55a7246a49283d367e420786f48f16556dd5a7d61406b1c8459b |
| completeM | geometry_20261116_current_C_M_live_query_complete_metric.py | fc35c6408aacbf2131a89fbac37ca4ae98c1665d9fbdc4ba78a50a43ca7f3a47 |

Material 仍是 geometry_20261116_current_C_actual202_M_common_material_phase.py，38151 字节/059d0df3ab5957b8ba5adf69e305ee4663ba06378242fe4c5f2116bab437af41，schema R457-current-C-actual202-capable-complete-M-common-material-phase-v1。它的真实 evaluate_active_cell 返回 value,u,q,uu,uq,qq；prefix 的 u 是公共坐标，radial 的 u slot 表示原 r 导数。当前新 helper 的通用 x slot 只按这次实际 API 映射，不将其误称所有族都是数值 s。

原 metric 的 CUT/PREFIX/KERNEL/C/CUFF/CAP/LIVE closure 仍逐件按原 tuple 加载。新 helper 被 load_source 明确以自己的固定 SHA 加载，其真实 receipt 进入 input binding 的 direct_sources。Generated consumer 的 source receipt 是真实新文件，不能冒原494fea source。

**未接** R504 的新同 C leaf/query source、R464/R463 incrementalM、R495 其他 views 或当前 217 全链。若后继需要这些族，必须独立登记真实 source/schema 和 generated-view 来源；本次不把一个 R459 view 的完成称为全部后继已覆盖。

## 5. 同一次 target 与六 jet 如何接

### 5.1 Base closed-cell

原顺序仍为 budget.check → target → current.evaluate → Gram → relative_norm。只在原值返回后，按 value,x,q,xx,xq,qq 取同一个 values 对象的六 slot，每 slot 保三个 Cartesian 分量的原区间端点。

Prefix target context 保实际准确 a 与 a_s、原 g11、原 Phi_q；A_x 由 a_s 乘 positive sqrt(g11) 向外包围。Base 时 g11=(Ltrue/Lnum)^2。不重算 closed_range，不换原 piece/support，不从圆整 a 倒推参数。

Tail/collar context 保 A=r、A_x=1、原同 C g11=E(r) 和实际 Phi_q；不调用新 query、不把 Bprime 换成 E。原 target 未返回时只写原 reason，根本不补做 field 求值。

### 5.2 Common-material 的原 t-grid

原 common.evaluate_active_cell 已返回准确共轭后的 value,u,q,uu,uq,qq。新 helper 直接吃这六向量；同次 target 已将 prefix g11 乘 Lnum²，因此此时 mu=Ltrue、A_u=Ltrue a_s。原第一材料 Phi_q、首图/当前图 inverse、实际旋转和 lower 反射都不另求一次。

所有诊断都发生在原 query 的计算过程中。原 common.encode_active_cell 或下一预算检查尚未完成时，一个已写入的局部 observation 并不意味着该原 phase transaction 已提交；实际 phase_cursor/count/pending 仍保持原算法定义。

### 5.3 可用与未付分列

Helper 可分别返回 angular_ratio_available、radial_angular_defect_available、algebraic_reference_velocities_available。任何正性不足仅令相应范围未付，原 direct Gram.available/norm_interval 保原值。真实 helper 输入/算术错误作为 diagnostic_error 保存原 type/message；不伪造有限 bound，也不将它重分类为 native 或 BVP 数学拒绝。

新常规源码字节/字段检查仍是原式工程绑定，不是新增数值接受门。Source view 缺原输入、同源不合或未完成 accepted loader 时，沿原 measurement 的原 setup/error 责任退出；不会用旁诊断绕过它。

## 6. 真实返回内容

局部完整记录只写已有 Actions 临时 cell/phase ledger，type=same_evaluation_sixjet_diagnostic。保：

- 唯一 observation_index 与完整原 cell 或原 time/witness/piece 地址；
- 实际坐标类型、同次目标 A/g11/Phi_q 与 A_x 的外包；
- h、h−1、局部 |h−1| 上界和可用时 tau 及其绝对上界；
- 可用时两 sigma 的归一化代数速度缺陷上界及 R514 局部 Gram majorant；
- W/P/当前角 norm 未隔正的真实必要区间与 reason；
- 原错误，或原 target 未返回的原因；
- “局部 observation 不代表原 cover/phase transaction 完成”的明确字段。

不复制原18个科学 jet 大数组，不返回原 root tape，不写新全域扫描或不被调用的审计 ledger。原 direct relative_norm 三个 Gram 分量、原参考 eta、DFS、继承 bound 和最终 global_relative_operator_error 完全不取新诊断值。

Result 新字段 same_evaluation_sixjet_diagnostics 包含：

| 必要域 | 含义 |
|---|---|
| counts / evaluation_kinds | 实际开始/返回及可用分项；重复 live-C 求值也实际计数 |
| unpaid_reason_counts | 原局部未付种类的出现次数，不替代完整未付地址 |
| largest_observed_local_upper_bounds | 仅已观察局部量的最大上界及实际地址；不是全域最大值 |
| last_started / last_completed | 实际最新观察及其 index/address |
| first_unpaid / last_unpaid | 首末真实未付对象，不冒完整中间列表已运输 |
| every_completed_observation_in_original_temporary_ledgers | 原 cell/phase ledger 的 bytes/SHA/rows |
| original_complete_coverage_and_pending | 原完整 coverage/pending 原件身份 |
| 明确 scope 布尔 | 没有积分、BC锚、solver稳定界、原分支或metric floor声明 |

原必要摘要还完整保有 R459 的 planned roots、实际 DFS stack、untouched root suffix、已退休无 bound 计数、原 resource/error 和全量原件身份。不能用局部诊断计数抹掉这些未付范围；已退休未付的完整原行仍只在实际 Actions ledger，必要摘要明说未全部重传。

Common t-grid、base 两侧及原反射的观察分开在实际原地址。两准确帽仍由原直接 target/graph 恒等式处理；诊断摘要声明没有为它们支付或要求 Frenet 条件。

## 7. 必要读回、比较与原 quiet/cleanup

Measure/readback 都使用新 R519 frame，每个独立完整语义 body 仍 ≤90000 字节。超过上限返回原明确 70，只保超限原件身份，不拆包、不将大科学树换字典编码、不截断成功。GITHUB_OUTPUT 名称继续是 metric_evidence_summary、metric_evidence_summary_bytes、metric_evidence_summary_sha256。它们是实际路径/身份，不能把原 R459 schema/frame 当当前记录。

Compare 必须消费**同一个新生成 source**的实际 measure results；原同目标/同 clock/真实父/分辨率/t-grid 比较完整保持。每 level 只另保该实际 result 身份、诊断启用标记和完整 pending 身份的引用；series 不复制全部局部诊断或把局部值用于 strict decrease。真 sup 下降、上界改善与 overlap/unpaid 仍按原 complete metric bounds 区分。

新代码不 spawn、不发 signal、不创建 owner、不删除 raw，不构造 quiet/cleanup marker。原 owner 必须持续拥有该测量进程；actual returned source/result/necessary 与原进程静止后才能照其既有合同清理。没有修改原第一 material、准确 C/raw、accepted field 的生命周期；它们必须在调用时真实在同 job 原 namespace 中。

原 handler 只记 signal，下一原 check 停止；新增局部运算/写账均消耗既有 clock allowance。不可为诊断再开一次18900秒或另一次 work budget。实际 overhead、完成 cell 数和数值改善均未测，不给必完成保证。缺第一B或其他原输入时仍只是本测量输入未付；不能用这个可选 role 卡住原 solver/refinement/held。

## 8. 明确尚未完成的责任

R519 不把两个代数 V 中任一个选成原 worker root/平方根分支，不是 IEEE RHS 或 noJ 求值误差。没有 BC-anchor、完整径向 tau 积分、原 ODE/RK/Hermite 重构稳定常数、全域 residual-to-Gram 传递或机器/solver tolerance floor。

局部观察和原完整 direct Gram 可以并存；前者不能覆盖原 pending 域，后者也不会把未付局部诊断伪填为合法 Frenet。没有新 science run，所以没有数值成功、非零原接受、全域收敛、性能或 raw 清理的实际声明。

后续 source 组合若把这项真正接进某个完整入口，须新增明确 runtime/source tuple、真实新 input/schema/frame 和原 clock/owner 关联。这个 requestless 交付已经提供实际可执行 measure caller，不要求额外 fixture、独立审计、预检数值对拍或先重跑一次旧数据。
