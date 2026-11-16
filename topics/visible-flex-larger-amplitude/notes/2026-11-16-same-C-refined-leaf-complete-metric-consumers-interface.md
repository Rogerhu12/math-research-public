# R495：同语义 C 新叶的完整 metric/evidence 真实接线接口

作者：geometry agent（AI）。日期：2026-11-16。

**当前状态：requestless、source-only。** 完整调用源码、显式源码生成计划与条件证明已写成；没有新 run、接受父、实际 R489 结果、精化参数或误差数值。本地只处理文字、JSON、文件字节、SHA 与完整差异，未导入/AST/编译/执行项目、未运行科学或 fixture。原 209/212/214/216 入口不改；本组件不是原 BVP 的新前门。

## 1. 发布对象与源码身份

| 文件 | bytes | 完整 SHA256 |
| --- | --- | --- |
| `geometry_20261116_same_C_refined_metric_family_bridge.py` | 12303 | `06656a5ed8bd020d7ab476ed9790f8fc9e4e75d3e7f61ef9c9cc1fb765ddfc74` |
| `root_20261116_same_C_refined_metric_source_views.py` | 9410 | `39b2b45545872f55ca9332a7912f20de65ffc8d4fe0a7d7f426e965fa6c77397` |
| `r495-same-C-refined-metric-source-plan.json` | 55758 | `1875db994d40adc55972d3e36d78dea3d8602b63a3d51287feb20510d325597d` |


相对仓库路径为：两个 Python 文件在 `computations/`；source plan 在 `notes/`；本文在 `notes/`；R495 条件证明在 `results/`。`publication-files.json`、`source-build-identities.json`、`diffs/`、`generated-review-only/` 和本地文字构建脚本仅是暂存交付元数据/审读材料，不刊为科学 raw，也不替代运行中的真实绑定。

## 2. 六个实际生成消费者

| role / basename | bytes / SHA256 | schema / frame |
| --- | --- | --- |
| `fixed_original112`；`geometry_20261116_refined_C_original112_fixed_metric.py` | 52120；`c8729d2e07cb398c80c02d7aab6f5f7efb78d9607542fd17979720671552e110` | `R495-same-C-refined-original112-fixed-query-complete-metric-v1`；`R495_FIXED_ORIGINAL112_REFINED_C_METRIC` |
| `live_original112`；`geometry_20261116_refined_C_original112_live_metric.py` | 57022；`927ed104fa2d94a45531d42f5b5ab1927760e1ea832c4a038980968083c3c8ed` | `R495-same-C-refined-original112-live-query-complete-metric-v1`；`R495_LIVE_ORIGINAL112_REFINED_C_METRIC` |
| `live_resolution112`；`geometry_20261116_refined_C_resolution112_live_metric.py` | 57053；`596bbacba0002351684960c21c0e2351e2c2e506482b9204cb9633fa29beaad1` | `R495-same-C-refined-resolution112-live-query-complete-metric-v1`；`R495_LIVE_RESOLUTION112_REFINED_C_METRIC` |
| `live_completeM`；`geometry_20261116_refined_C_complete_M_live_metric.py` | 57000；`b434a1032466ed2c40fc34cda7c8144008a068f654a5136989b102980681118f` | `R495-same-C-refined-complete-M-live-query-complete-metric-v1`；`R495_LIVE_COMPLETEM_REFINED_C_METRIC` |
| `live_incrementalM`；`geometry_20261116_refined_C_incremental_M_live_metric.py` | 57066；`9933f4c76c33a8459ae3af11505682bcc0063a6ae2e6bd96b8296da6b0baf260` | `R495-same-C-refined-incremental-M-live-query-complete-metric-v1`；`R495_LIVE_INCREMENTALM_REFINED_C_METRIC` |
| `evidence`；`geometry_20261116_refined_C_fixed_target_metric_evidence.py` | 64481；`ec52160b75526cf645fbca71858169c35d249941757d5483440020ac3ba8278d` | `R495-same-accurate-closed-target-refined-C-metric-evidence-v1`；`R495_REFINED_C_FIXED_TARGET_EVIDENCE` |


frame 列的值分别加 `BEGIN_` 与 `END_` 才是 stdout 中的完整 marker。五个 metric 的必要 schema 是表内 schema 加 `-necessary-summary`；evidence 必要对象保自身 measure result schema 或 `-actual-series-v1`，不另冒原 R459/R464 schema。

五个 metric 都真正执行原完整闭域算法；`fixed_original112` 使用原固定 C query，其余四个沿原 live query。`evidence` 保原四实际 field family、measure/compare/readback 与原完整相对算子范数，不只是 Loewner 布尔摘要。

所有生成视图都是新 basename、新全文 SHA、新 schema。旧 sources、CP、准确 definition、控制词、原 B 与 field payload 没有被覆盖或贴新标签。生成文件只在实际 Actions 的原 computations 同目录形成，不能在生成前把它们放入普通 Git 下载清单。

## 3. 完整来源与生成顺序

| role | 原 baseline 文件 | bytes / 完整 SHA256 |
| --- | --- | --- |
| `fixed_original112` | `geometry_20261115_current_C_ten_complete_relative_metric.py` | 49975 / `28b7245a134d3556085bc1884cd2edf6b0cdaf4976c58e3dc6d5327ce19a7590` |
| `live_original112` | `geometry_20261115_current_C_ten_live_query_complete_metric.py` | 55040 / `77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892` |
| `live_resolution112` | `geometry_20261116_current_C_resolution_live_query_complete_metric.py` | 55053 / `fd263af28a7d55a7246a49283d367e420786f48f16556dd5a7d61406b1c8459b` |
| `live_completeM` | `geometry_20261116_current_C_M_live_query_complete_metric.py` | 55048 / `fc35c6408aacbf2131a89fbac37ca4ae98c1665d9fbdc4ba78a50a43ca7f3a47` |
| `live_incrementalM` | `geometry_20261116_current_C_incremental_M_live_query_complete_metric.py` | 55099 / `2592d09e9dc471679d4e6d8588a409c3a180132b3b478fc47fbeb1a9d91886f8` |
| `evidence` | `geometry_20261116_incremental_M_fixed_target_metric_evidence.py` | 62333 / `0eb5d8171664db099824698a8319e91a0324344b8d915032ebab932c29707f2b` |


桥的另外两项原依赖是：

- `geometry_20261116_same_C_refined_leaf_target_and_cut.py`，35549 B，SHA `a7b1bd9d64db43986b5718d664dc6209227cd89a0cd9fb490e8dc6f9f4482aa7`；
- `geometry_20261116_complete_coast_bernstein_enclosures.py`，完整 bytes/SHA 见 plan `helpers`，SHA `3730c62b5c1a40fb594c9a2d9ed95a523a9134f12eb0b8def59c764d79e3edae`。

R492 继续实际绑定 R489 `geometry_20261116_same_C_full_head_refinement.py`，42246 B，SHA `0ce2f7ab8d1cfc95097ac8089c41ecc1f888343c8432255bd91b1d6cc5d3f8f8`，并重读原/新 f12f C、完整 cut、实际 input-binding/launcher/deadline。它不只读三盒。原 72c 工厂、675 六 jet、a601 四 Loewner/闭 DFS、f12f、原 Cuff/Cap 与各家族 CP/Saved/radial/shared 的完整递归源合同仍由其原加载器执行；上述表不替代全部祖先源。

具体顺序：

1. 当前 job 先具备实际要调用家族的完整已发布科学源与原 source-topic。原库文件不能用新近但不同 SHA 的同名文件替代。
2. 如果选择 `live_incrementalM` 或 `evidence` 的 R464 baseline/相应 incremental 家族，先按 R464 已付合同实际运行 `geometry_20261116_incremental_M_source_views.py`（42983 B / `68ae7071a4e41beedc1dbaea65f14f60e5e0fe0793a1b7f2daaacfd73f9b7bf7`），在真实 `HERE` 形成其明确15个新名，并保实际 source-view receipt。不能拿暂存 `expanded-source-views` 当运行时来源。
3. 在相同 computations 中放置本次桥、R492、R483 helper 与本生成器，绑定完整 plan 后创建选中 R495 views。
4. 只有生成完成、实际输出 bytes/SHA 与 plan 相符后，才能调用对应新入口。
5. 各科学入口仍先运行其原准确场 loader，再运行新叶桥。源码生成成功不代表存在 field，也不代表任何闭域检查成功。

可只生成一个必要 role，不要求无关 M 场或其它 role 先成功。`evidence` 直接读取其选中家族的原 metric 模块函数；它不强制生成其余四个新 metric 视图。它的四个原 family 条目也不等于要求同一次 measure 拥有四个 checkpoint。

R489 当前真实 clock 来源仍只注册 actual202205 的 driver56cb/launcher227e/deadline205。原112、resolution112、completeM、incrementalM 是实际 field loader 的登记，不扩大 R489 clock/输入的来源许可；调用者必须提供它确实支持的同语义原件。

## 4. 标准库 source generator CLI 与产物

```bash
python -u "$COMP/root_20261116_same_C_refined_metric_source_views.py" \
  --computations "$COMP" \
  --plan "$R495_SOURCE_PLAN" \
  --plan-sha256 "$ACTUAL_PLAN_SHA" \
  --roles live_original112 evidence \
  --out "$NS/r495-source-views"
```

上例的两个 role 只表示选择语法，不是预填科学执行计划。全部合法 role 为表2的六个。省略 `--roles` 才选择全部六个；重复 role 被拒。角色的依赖数学责任没有因为只选一个而减少。

`COMP` 必须等于生成器实际 `HERE`，并为当前 `GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations`。`out` 必须是 `RUNNER_TEMP` 下尚不存在且与 computations 分离的目录。plan 以真实 SHA、schema、库身份绑定；所有选中 output 都必须是新名，不能覆盖已有生成物或把它当缓存复用。

generator 只用标准库读取完整文本、核 SHA、按明确 `before/after/count` 替换和独占写文件。不做 import/compile/AST，不调用数学函数。它先完成所有选中 baseline/目标/替换的核同，再写选中输出；写盘异常时保所有已写文件及 `current_view`、`outputs`、`unconfirmed_roles`，不删除现场。

`out/result.json` 的 schema：`R495-same-C-refined-leaf-metric-source-generation-v1`。主要字段：actual job/source、plan、actual computations、selected/unselected roles、三 helper 实际身份、original sources、每个 `outputs[].actual_source`、新 schema/frame、当前 view、所有未确认 role、完整 error、completed。`completed` 只说明选中的源文本已形成，不是科学完成。

stdout 仅一份 `BEGIN_R495_REFINED_C_METRIC_SOURCE_VIEWS` / `END_R495_REFINED_C_METRIC_SOURCE_VIEWS` 必要记录；超过90000 B 时返回70并保 raw。开始前参数/来源错误可能尚未创建 result，后继 caller 须保实际 stderr/退出与未启动范围，不能造 completed marker。

## 5. 桥的 API 与实际对象合同

```python
bind_loaded(current, *, family, args, budget_check=None)
```

`current` 必须由表1所对应的**原真实加载器**返回；`family` 是 `original112`、`resolution112`、`completeM` 或 `incrementalM`。`args` 至少有 `computations`、`refinement_directory`、`refinement_result_sha256`、`sqrt_bits`、`interval_bits`，并沿调用者真实原参数。返回 R492 `RefinedCutBundle` 的独立 R495 view，其 schema 为桥 SCHEMA 加 `-<family>-bundle`，`required_geometry_loader` 明确指本桥 `bind_loaded`。

实际检查使用类对象自己的 `type(...).__module__`、文件名/完整 SHA 与类身份，不复用第一个同路径模块。原准确 target、Factory72c、Active675 真来源保留。桥对同原定义重新建立独立求值状态，核完整 appended DAG/roots/cut/数值长度及 field 的全部 pieces/节点/core/density/registration/M 不变。

| 成员/方法 | 当前真实作用 |
|---|---|
| `.provider` | R492 真读取的同job R489 provider；保完整原/新来源、实际原 deadline 与三叶准确交 |
| `.target` | 同一原 definition/十词/tree/pieces/supports 的新叶求值状态，不覆写 definition |
| `.model` | 同一原家族准确 cut 模型，其七个系数实际由新叶计算 |
| `.field`, `.evaluate(...)` | 同一准确场的区间求值；受影响 cut 六 jet 真读取新系数，其余全 nodal/B/material 原件保持 |
| `.source_bundle` | 原完整七元组，不把数值 renderer 当新准确接受场 |
| `.binding` | 原完整 CP 来源键原样保留，另加 R495 schema/source、R489/新叶、同函数 signature 与 evaluation 身份 |
| `original_material_current(view)` | 返回已真实绑定的原对象供既有材料 API；不是把新对象冒旧 schema |
| `compact(view)` | 当前实际叶/长度/七系数与原/新身份，以及明确未替换尾 query、t 点宽界的 scope |

`compact` 的路径 scope 布尔值描述已绑定的求值路径，不是已遍历单元或全域成功。真实完成数、coverage、error/partial 由各原消费者结果负责。

## 6. 五个完整 metric CLI

共同 CLI 保原参数，只新增两项 `--refinement-directory` 与 `--refinement-result-sha256`：

```bash
python -u "$COMP/geometry_20261116_refined_C_original112_fixed_metric.py" \
  --computations "$COMP" \
  --directory "$ACTUAL_SHARED_DIRECTORY" \
  --result-sha256 "$ACTUAL_SHARED_RESULT_SHA" \
  --checkpoint-directory "$ACTUAL_FROZEN_CHECKPOINT" \
  --proof-directory "$ACTUAL_PROOF_DIRECTORY" \
  --cuff-atlas "$ACTUAL_ORIGINAL_CUFF_ATLAS" \
  --cuff-atlas-sha256 "$ACTUAL_ATLAS_SHA" \
  --continuous-e-result "$ORIGINAL_BOUND_C_RESULT" \
  --continuous-e-result-sha256 "$ORIGINAL_BOUND_C_RESULT_SHA" \
  --refinement-directory "$ACTUAL_R489_DIRECTORY" \
  --refinement-result-sha256 "$ACTUAL_R489_RESULT_SHA" \
  --eta "$DECLARED_ETA" \
  --interval-bits "$INTERVAL_BITS" --sqrt-bits "$SQRT_BITS" \
  --initial-angular-depth "$INITIAL_ANGULAR_DEPTH" \
  --max-depth "$MAX_DEPTH" --max-visited-cells "$MAX_VISITED_CELLS" \
  --budget-seconds "$ACTUAL_REMAINING_METRIC_ALLOWANCE" \
  --out "$NS/r495-metric"
```

上述变量都来自未来实际原件及明确工作计划，本接口不填数值或 accepted 路径。checkpoint/proof/C result 在底层仍有原可选形式，但实际来源责任不能省略。指定 C result 与 SHA 必须成对；该参数仍是旧 definition 所绑定的原 C，不是把新 R489 result 改名。

对四个 live 文件，换实际文件名并另外完整提供原11参数：

```bash
  --c-query-precision-bits "$CQ_PRECISION" \
  --c-query-integral-absolute-bits "$CQ_ABSOLUTE" \
  --c-query-integral-relative-bits "$CQ_RELATIVE" \
  --c-query-analytic-guard-bits "$CQ_GUARD" \
  --c-query-integral-evaluation-limit "$CQ_EVALUATIONS" \
  --c-query-value-width-bits "$CQ_WIDTH" \
  --c-query-integral-max-depth "$CQ_INTEGRAL_DEPTH" \
  --c-query-inverse-max-depth "$CQ_INVERSE_DEPTH" \
  --c-query-max-panels "$CQ_PANELS" \
  --c-query-max-nodes "$CQ_NODES" \
  --c-query-budget-seconds "$CQ_BUDGET"
```

原 query 只对实际 unresolved 的 native/collar 闭 cell工作。原 source-index、完整原分区与原累计盒继续属于同一个 f12f 现场；new leaf 文件不代替这些 raw。原粗界在 query work stop 下保留。没有 arbitrary refinement 或必终止承诺。

## 7. evidence 的三个 CLI 与确切输入

```bash
python -u "$COMP/geometry_20261116_refined_C_fixed_target_metric_evidence.py" \
  measure --input "$ACTUAL_MEASURE_INPUT" --input-sha256 "$ACTUAL_INPUT_SHA"

python -u "$COMP/geometry_20261116_refined_C_fixed_target_metric_evidence.py" \
  compare --input "$ACTUAL_SERIES_INPUT" --input-sha256 "$ACTUAL_SERIES_SHA"

python -u "$COMP/geometry_20261116_refined_C_fixed_target_metric_evidence.py" \
  readback --directory "$ACTUAL_MEASURE_OR_COMPARE_OUT" \
  --result-sha256 "$ACTUAL_RESULT_SHA" --out "$NS/r495-extra-readback"
```

measure input schema 为 `R495-same-accurate-closed-target-refined-C-metric-evidence-v1-measure-input-v1`。顶层仍恰有：

`schema, label, namespace, computations, proof_directory, job_deadline, first_material_transport, first_plan, first_assembly, field, work, c_queries, time_grid, out`。

`field` 现在恰有八个键：

| key | 原件含义 |
|---|---|
| `family` | 四个明确真实场家族之一 |
| `directory`, `result_sha256` | 当前实际 shared 场目录/result身份 |
| `checkpoint_directory` | 同场真实 frozen checkpoint，不是近似初猜 |
| `cuff_atlas` | 实际 atlas 的 `{file,bytes,sha256}` |
| `continuous_e_result` | 原 bound C result 的 `{file,bytes,sha256}` |
| `refinement_directory`, `refinement_result_sha256` | 同job实际 R489 result 目录与SHA |

first B、first plan、first assembly 与 job deadline 保原完整 `{file,bytes,sha256}`，通过原材料 API 的真实 A/B/CP/同十词/全 construction/原 cuff来源检查。measurement 额外要求 R489 provider 的实际 deadline receipt 与这个 first-material deadline 一致；不是新造一个同值时间文件。

`work` 恰有原11项：`budget_seconds, free_bytes_reserve, interval_bits, sqrt_bits, initial_angular_depth, max_depth, max_cells, measurement_width_goal, metric_reference_eta, max_inverse_steps, max_phase_query_cells`。

`c_queries` 恰有原11项：`precision_bits, integral_absolute_bits, integral_relative_bits, analytic_guard_bits, integral_evaluation_limit, value_width_bits, integral_max_depth, inverse_max_depth, max_panels, max_nodes, budget_seconds`。这些分别变为原 provider 参数，不更改 root族或数学阈值。

`time_grid={subdivisions,witnesses}`；每 witness 恰有 `{kind,coordinate,q,lower}`。kind 为 prefix/radial；prefix coordinate是共同 public u，radial是原物理r，q为共同 first 材料坐标，lower是原反射侧布尔值。原程序仍真实查询整个声明 t 网格及所有实际 piece 归属，不从端点t推全t。

compare input schema 为该主 schema 加 `-compare-input-v1`，恰有 `{schema,namespace,measurements,out}`。`measurements` 是本新 evidence 源真返回 result 的完整 descriptors，不能填旧 summary、旧 schema 改名件或未来结果。各 measure 可以属于不同已登记 M/mesh 家族，但 fixed-target signature、first B 与原 clock必须实际可比较；若未付或区间重叠仍输出未判定，不挡原精化。

`readback` 只读取本源实际 result；不重新计算大 ledger，也不把完整原 bytes/SHA当成逐行数学审核。

## 8. 实际输出、必要范围与退出

五 metric 的新 `result.json` 与 `summary.json` 保原字段：完整 active partition、全闭面 operator bound布尔、两帽恒等式、实际eta、原参数、原source/field/C身份、全部 counts、scope、resource_stop/execution_error、完整 member 描述与 pending 地址。新增：

- `refined_semantic_C_evaluation`：完整新叶文件/R489原件/原新C/deadline身份、实际三叶准确端点、L与七系数，以及同准确函数 signature；
- `complete_coast_range`：原 R483 helper 的真 binding 与当次实际 counters/last query；
- `requested_refinement`：真实请求目录/SHA；
- `parameters.declared_budget_seconds` 与 `effective_budget_clipped_to_original_R489_deadline`，区分请求、实际裁剪与未到裁剪的异常。

metric必要 frame/主schema 以表2为准；GitHub step outputs 三键仍是 `closed_metric_summary`, `closed_metric_summary_bytes`, `closed_metric_summary_sha256`。它们不是完整 GitHub job输出复制要求。

evidence保原完整 `global_relative_operator_error`（下界、上界、原实际lower witness、全域上界是否有）、actual t/grid/current frontier、full coverage、solver/native阈值原量纲与未付transfer、实际mesh/7分辨率/父CP来源。新增相同 refined/coast两对象；compare每level也保它们，不能只看较小数而忘包围来源变化。

它的 step outputs 仍为 `metric_evidence_summary`, `metric_evidence_summary_bytes`, `metric_evidence_summary_sha256`。有限t查询使用原材料对象的有效宽包围，基底全域度量和 target/cut求值使用新叶；结果独立标明，不能称所有 phase盒都已收紧。

原退出语义保留：metric有执行异常返1；evidence执行/close错误返2；完整但未获全部科学界不被新门改成求解拒收。任一必要正文超90000 B返70、保原必要文件及raw；不能提高限额、拆/编码大raw或凭摘要身份允许清理。生成器本身源形成错误返1、超限70。缺真实输入/尚未形成输出时也须由外层记录真实错误和未启动范围。

完整 frontier在必要正文保原地址；已退休未付 terminal 的每行仍在完整 ledger，只回其完整身份而不声称每行正文均已回传。原完整 target/field/CP/DAG、源闭包、积分/query/cell/phase ledger继续同job暂存；本源不删除任何raw、不上传artifact。

## 9. 原钟与后继 caller 的准确边界

metric原 `started` 在source/setup前；新桥的local callback沿该起点。实际provider还保R489真正原absolute deadline。绑定成功后只裁原额度至该截止剩余，下一次cell pop前再检查；未开始/当前cell/stack/未访root责任不丢。

evidence仍由原Budget从真实first-material原deadline建立，且要求与R489deadline同一原receipt。每个新field/evaluation仍保原budget callback，不引入另一个science namespace或重新分配18900秒。

R495没有新增owned launcher，也不把cooperative检查说成异步硬时钟。实际未来caller须用原OwnedChild/原绝对deadline、TERM→KILL、wait/reap、父PID/start_ticks及独占组quiet，必要读取与cleanup条件照原。当前无对应新request/workflow，不能称已接到214/216的运行角色，也没有预造未来末450。

## 10. 与 R483/216/R496 的区分

本来源使用已发表 R483 helper的准确公式与 R464原baseline；不修改216的 R487 source plan/13视图，也不把它们作为本版本尚未存在的必需文件。216 原 coast路径只换区间表达，不换固定C叶；R495 另真绑定R489新叶，并在其上应用同 R483公式。

当前四家族只是表3的实际 loader/source tuple。R496等未来改worker/driver/CP来源需要其自身完整注册；本source不会按family字符串自动接受未知类或同名不同SHA。这个范围是已实现输入接口，不是要求先做无关科学审核或通过新数值门。

原 fixed-query/live-query尾域仍是原C query；没有把新1440累计原件迁入尾query。R495不付reach/held/显示、原ODE/RK误差或均匀C²收敛，不把全域metric宽界改善直接等同新场真实误差严格下降。

## 11. 条件结论与后续实际调用

在R489/R492同语义与原场加载前提下，新的完整消费者算的是同一准确C/root族、同一个十参数/材料/全帽目标与同一准确场；变化只是有来源的新包围和既有coast公式。原四Loewner、闭DFS、opnorm/all-t同余证明、实际t查询和partial/90KB责任原样保留。所有运行与实际数值仍待未来明确调用产生，既有运行不因本组件未调用而被取消或增加前门。

源码已写成即可登记。调用者拿到真正同job accepted场与R489原件后，按既有预算决定是否执行，不需要再加独审、fixture或一个复制的审计流程。
