# R434：同现场 C 查询精化接入完整十词 450 后几何编排

作者：AI（ChatGPT）；2026-11-16。

本接口交付两份独立、无请求号的源码：从已刊 R429 编排只替换 metric role，调用已刊 R426 的同现场 C 查询消费者，并接入其十一项显式工作参数。原始453→450接受责任、五阶段顺序、真实源／场绑定、绝对期限、进程所有权及单份必要读回均保留。本接口没有新的 actual run、接受场、查询参数取值、$\eta$、$K$ 或 $\tau$，也没有在本地运行科学、导入源码、做 AST／编译／fixture。

本项以 [R429 条件组合](R429-same-job-ten450-postsolve-geometric-responsibility-composition.md) 和 [R426 同现场完整 C 查询接口](R426-same-job-continuous-C-live-query-refinement-and-complete-metric-interface.md) 为依据。它完成实际调用连接，不另立数学验收条件。

## 1. 冻结文件与实际基线

| 独立文件 | Bytes | SHA256 |
|---|---:|---|
| [geometry_20261116_current_C_ten450_live_query_postsolve_geometry.py](../computations/geometry_20261116_current_C_ten450_live_query_postsolve_geometry.py) | 47084 | `88996287da8df21b997cd55835dbf40315766bfb4533e949e7091d7f642c32f8` |
| [root_20261116_current_C_ten450_live_query_postsolve_necessary.py](../computations/root_20261116_current_C_ten450_live_query_postsolve_necessary.py) | 24444 | `ebed189dfcc879a1d357b5595a2cf29d697d4cc92620f11b8cf0e5ed721e6fa0` |

两份直接基线均来自公开 commit `c13c165bb28b00256822ba9554707e86d6d543f7`：

- 原 producer `geometry_20261115_current_C_ten450_postsolve_geometry.py`，43042 B／`84d0450f2f362138045c222f5a47162e030fd0be8b6c7a99c5d66c0e41da425a`，blob `2f9199e4b9b0b954a08a7ed200d4cb3e5ac1ebe6`。
- 原 reader `root_20261115_current_C_ten450_postsolve_necessary.py`，23903 B／`79296f4ff205542cf99091ada7fd9a7055e68ffb04173bd242592769c8d4ca2f`，blob `d1c28fc78972d05fd3ab61d5493d332f7597b498`。
- R429 已刊总接口为16926 B／`98e61b34a6afcfe01a1bc29adf65c13485744023433b73be26a3e7f5d2ed65a3`；本地较早16916 B稿只在 R425 时态上不同，不能冒作该公开文件身份。

R426 三件公开于 `ba69b9b28be421ced147cc6aeb0da3371b95f4a9`：

| 角色 | 文件 | Bytes／SHA256 |
|---|---|---|
| 实际 metric entry | `geometry_20261115_current_C_ten_live_query_complete_metric.py` | 55040／`77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892` |
| 同现场查询 provider | `geometry_20261115_same_job_C_live_query_provider.py` | 31603／`07fc4e41a6318c43a6e03313356df4df7538ccd5ea110406434b2e420c09bcd9` |
| R426 完整接口 | `R426-same-job-continuous-C-live-query-refinement-and-complete-metric-interface.md` | 19556／`e26e2fd2945927b9092a2ba6d5b43a1c8678832fc98d834280125736441bc8b1` |

原 R429、R418、R426、R431 mesh、R433 held 以及正在运行的科学源均未被改写。

## 2. schema 与完整来源分支

新 producer：

```text
current-C-ten450-same-job-postsolve-live-query-complete-geometry-v1
```

新输入为上述字符串加 `-input-v1`。新 reader：

```text
current-C-ten450-live-query-postsolve-one-necessary-conclusion-v1
```

实际 metric 结果必须是：

```text
R426-current-C-accurate-ten-complete-closed-relative-metric-live-queries-v1
```

其 provider 状态来自：

```text
R426-same-job-original-C-live-closed-query-provider-v1
```

原 R429 input／procedure 不改标签后塞入新 reader。新 reader 核完整 procedure schema 与本次47084 B producer SHA，再核真实同 job 的 run／source。metric 结果仍由原 `invoke` 核实际结果来源 SHA与该 role 的准确 schema。

原 R429 producer 在新结果中只记 `original_R429_procedure_provenance`，明确 `source_provenance_only_not_executed=True`。原 R418 源继续保留于闭包、由 R426 核身份；本次不会另外启动一个 R418 metric 进程。

## 3. 原真实453→450输入责任逐项保留

新 producer 的命令行仍只有：

```text
python geometry_20261116_current_C_ten450_live_query_postsolve_geometry.py
  --input ACTUAL_INPUT_JSON
  --input-sha256 ACTUAL_INPUT_SHA256
```

这些大写名称说明调用方应提供的真实文件，不是已选输入或可执行示例值。输入对象保留下列原字段，并新增第4节的 `c_queries`：

| 字段 | 原实际含义 |
|---|---|
| `schema` | 本接口独立 input schema |
| `namespace` | 当前 job 的 RUNNER_TEMP 内已存在独占 namespace |
| `upstream_launch_directory` | 当前真实两阶段 launcher 输出目录 |
| `upstream_result_sha256` | 若提供，核真实上游 result；原可选语义不变 |
| `job_deadline`、`job_deadline_sha256` | 原 launcher 已消费的同一绝对期限文件与实际摘要 |
| `geometry_directory` | checkpoint 原 native binding 所指的实际 geometry 目录 |
| `continuous_e_directory`、`continuous_e_result_sha256` | 同一个实际当前 C 目录及 result |
| `computations`、`proof_directory`、`source_topic` | 当前固定科学 checkout 中的来源路径 |
| `out` | 同 namespace 内独立新 postsolve 目录，不覆盖上游树 |
| `construction` | 原 W、cap height及完整 fixed_cap.markers |
| `metric` | 原六项 metric 参数 |
| `reach` | 原十二项 reach 参数 |
| `resources` | 原五阶段预算、内存／磁盘／shutdown 配置 |
| `c_queries` | 新增、无默认值的十一项 R426 工作参数 |

原 `Procedure.bind` 的数学来源核保持：只接受真正的上游两阶段成功结果与 quiet；原 phases 必须依次是 design453、frozen450，维数453与450、两者原完整DN返回及各自实际接受标志均保。checkpoint 必须是原独立450 writer 所写，active parameter count与fixed core targets均为零，不是从453删除三行的伪450。

两个阶段的完整十个 float64le 词必须同一，当前目标、原全112／338、完整均值、material、cut、far、所有原 native／FD／RMS／BC／final audit 身份保持。新组件不重求上游450，也不从其残差小或进程绿色猜接受。

deadline 必须逐 bytes／SHA 匹配原 launcher 的 `actual_job_deadline`，并核原 repository、run、source、recipe。它不接受新建的“本阶段起钟”文件。上游未接受或未 quiet 时，原五阶段均留下明确未启动后缀，未发生的几何计算不填成功。

## 4. 十一项查询参数与实际 CLI

`c_queries` 必须恰含下表全部十一键。除 budget_seconds 是正有限 int／float 外，其余是明确整数；不接受 bool 冒整数。取值域与已刊 R426 parser／parameter_record 相同，只约束工作参数，不增加对结果的数学门。

| 输入 `c_queries` 键 | 传给 R426 的 CLI | 资源合法域 |
|---|---|---|
| `precision_bits` | `--c-query-precision-bits` | 128至8192 |
| `integral_absolute_bits` | `--c-query-integral-absolute-bits` | 1至precision_bits |
| `integral_relative_bits` | `--c-query-integral-relative-bits` | 1至precision_bits |
| `analytic_guard_bits` | `--c-query-analytic-guard-bits` | 0至64 |
| `integral_evaluation_limit` | `--c-query-integral-evaluation-limit` | 正整数 |
| `value_width_bits` | `--c-query-value-width-bits` | 1至precision_bits |
| `integral_max_depth` | `--c-query-integral-max-depth` | 0至80 |
| `inverse_max_depth` | `--c-query-inverse-max-depth` | 0至60 |
| `max_panels` | `--c-query-max-panels` | 正整数，查询间累计 |
| `max_nodes` | `--c-query-max-nodes` | 正整数，查询间累计 |
| `budget_seconds` | `--c-query-budget-seconds` | 正有限数，累计活跃查询时间 |

原 metric 六键仍为 `eta, interval_bits, sqrt_bits, initial_angular_depth, max_depth, max_visited_cells`。其中 `eta` 仍是明确准确有理文本。原 reach 十二键仍为 `curvature_upper, target_reach, active_depth, curvature_max_depth, pair_max_depth, interval_bits, sqrt_bits, max_cells, max_pair_nodes, max_pairs, cache_entries, max_constant_levels`；$K$ 与 $\tau$ 的准确文本不由本组件代选。

新十一参数逐值转为 CLI，没有另设 defaults、事后改精度或重选参数。R426 的原结果中 `parameters.same_job_C_queries` 采用其原字段名，其中 `integral_max_depth→max_depth`、`inverse_max_depth→query_depth`、`max_nodes→max_query_nodes` 是原 provider 的明确映射；本次输入本身则完整保留于新 reader 的 `explicit_original_parameter_inputs.c_queries`。

## 5. 五阶段与新增 metric 命令

阶段名、顺序和输出目录均保持：

| Stage | 实际执行 | 原依赖 |
|---|---|---|
| `radial_replay` | 原 R409 radial mjs | genuine450 + 原实际 geometry |
| `original_cuff_atlas` | 原 R413 atlas | genuine450 + 原 construction |
| `shared_field` | 原 R409 prepare | 上述两份真实完整输出 |
| `metric` | 本次固定 R426 entry／provider | 同一 shared field、checkpoint、atlas和当前 C |
| `reach` | 原 R422 | 同一 shared field、checkpoint、atlas；不以metric成功为前门 |

原 radial 与 atlas 的尝试顺序不改；只有其真实完成结果可产生后续 shared。原 R413 若已写完整 plan、结果 completed=true且无error，但只因stdout摘要过界返回70，仍沿 R429 已有分支读取实际文件，不添加科学门。

metric 命令保所有原 shared／checkpoint／proof／cuff CLI与原六参数，仅将 entry 换为 R426，并追加十一查询参数；`--continuous-e-result` 仍指同一个实际 C result，`--continuous-e-result-sha256` 仍为原 current binding。reach 的完整命令、参数、原失败／未决传播和实际终态 flags 均不改。

R426 调用的原 `QueryCover` 保同一准确 C、160浅层表、原冻结warp、完整深根族、自然域和全部可能逆像。一个新查询只有原完整闭域包围提交后才能与原已付粗包围求交；不以中点、旧SHA、任一数值代表或另一run的窄盒替换当前函数。R426 的工作分辨率未达不自动取消原完整合法粗界，原四项 Loewner检查不另设精化成功门。

因此 new metric=True 的含义仍是对该绑定准确目标、该完整 R416 场的原相对算子责任已付。new query完毕但metric未付，不推出目标不可能；metric成功也不推出R422／held／δE或完整任务完成。

## 6. 同现场 C 原件保留与未付边界

原四文件全部真实读取和绑定：

```text
result.json
input-binding.json
query-plan.json
query-results.json
```

实际查询另消费同目录保留的：

```text
large-arrays/complete-source-radial-panels.jsonl
large-arrays/source-piece-index.json
```

这两额外原件仍在 `inputs.continuous_E_files` 中记录原bytes／SHA或真实缺失；旧字段 `future_same_C_query_payloads_present` 在独立R434 schema中改为 `same_C_live_query_payloads_present`。没有用它增加启动／接受门：缺件由原R426报告精化未付，已完整的原粗界仍按原合同有效；原四件／当前场 binding 不匹配的实际错误也没有绕过。

R426 必须消费此 job 的原 C run／source与 RUNNER_TEMP 目录，读取源 ledger 完整身份、1440片索引／闭片覆盖及原累积量。没有重建已经删除的payload，没有跨run语义转移支路，也没有重做原1440片全部六primitive总和。原累积半径不确定性、深根族宽度、prefix语义叶及R416 cut系数宽度均可能继续限制结果；新空间划分不保证消掉这些源宽度。

新 producer／reader均不删除 C、shared、metric或其他raw；最后实际owner必须等全部已接消费者、对应必要读回及独立quiet确认后再清理。R433 held未来复用前三回执时也须位于同一次总清理前。源文件的digest不是可恢复这些实际原件的替代输入。

## 7. 原绝对期限与实际进程生命周期

原 `resources` 仍要求：

- `free_bytes_reserve`、`node_heap_mib`；
- `child_shutdown_reserve_seconds`；
- `stage_budgets_seconds`，恰包含五个 stage 的正有限预算。

每阶段在其实际启动时用原namespace绝对截止时刻，扣除原shutdown reserve，再将剩余时间与该stage显式预算取较小值。剩余不足则保留原未启动地址；磁盘reserve、信号和前一owner不静止也沿原路径记录，不被改成数学拒绝。

R426 仍得到已真实clip的 metric `--budget-seconds`。它的 `ActiveBudget` 从原metric开始计其绝对截止，并另累计查询活跃秒数；即使显式 `c_queries.budget_seconds` 大于本次metric剩余时间，也不能延长外层截止。这里没有新增第五阶段外的查询进程、重新起钟或额外预留时间。

原 `OwnedChild`、`proc_record`、同pid/start-time核对、TERM／KILL／wait、明确sid／pgid观察、parent signal处理、原disk检查及finally正文逐字保留。新source只在原metric结果返回之后记录它实际报告的query状态，再继续原reach尝试。两份源都不会借metric完成标志跳过实际quiet。

原runner的过程返回与科学完成分开：受控 procedure_returned 不代表五项均成功，父process绿色也不代表完整任务。外部中断保原signal退出，错误／nonquiet沿原返回语义。没有对正在运行的193／195／197／200或其他run改编译器、算法、预算或终检。

## 8. provider实际执行、请求和提交分开

R434 不再沿用原R429写死的“新C查询未执行”标志。

- metric从未启动时，`on_demand_C_refinement_provider_executed=False`；
- 实际R426结果带回 `same_actual_C_target.same_job_live_query` 原对象时，记录provider已执行及其原scope；这不要求发生新查询；
- metric已启动却没有可读的原provider状态时，该标志为null，明确不能据子退出或缺文件推为False或成功；
- 是否请求／提交／完成闭包围由原 `requested_query_count`、`committed_query_count`、`complete_new_query_bounds` 等分别给出，不能以provider=True替代。

`actual_C_live_query_provider_observation` 只摘录原schema/source/binding、state、source_prepared、原请求／提交／完成／工作分辨率／失败计数、disabled_reason及原error。它不是一个独立数学证明，也没有被用作reach前门。

完整必要metric投影保R426的原 `same_actual_C_target`，其中包含：

- 原完整源读取状态、尚未提交的source-row后缀；
- `active_uncommitted_query`，或cache已提交而地址尚未退休时的独立字段；
- 最后实际原integrator地址、所有累计预算计数与真实停止原因；
- 两份保留源原件和query journal的原身份、完整关闭标志；
- 原固定盒／全根族／prefix／cut仍未精化的明确范围。

旧combined标志 `actual_held_deltaE_and_new_C_query_provider_not_executed` 不存在于新schema，改为准确的 `actual_held_rigidity_and_deltaE_not_executed=True`。held／δE没有因接入R426而被执行或冒称完成。

## 9. 一份必要reader及完整未付语义

reader仍只用标准库读原JSON、文件身份和实际进程metadata，不调用科学源、C查询、ODE、FFT、Loewner或范数计算。其命令仍为：

```text
python root_20261116_current_C_ten450_live_query_postsolve_necessary.py
  --directory ACTUAL_CLOSED_POSTSOLVE_DIRECTORY
  --out NEW_NECESSARY_OUTPUT_JSON
```

它先核新producer完整来源及same-job身份、procedure finally已返回，再用原generic `process_quiet` 确认实际owner和所有原group均静止。五stage必须全部存在且顺序准确；未启动、无result、metadata错误、非零子退出、resource stop和真实source/schema都按原字段保留。

metric原结果／summary关联仍按实际result SHA核。R426整体 result 可以因自己的stdout摘要超界而子退出70；只要原文件存在且owner已静止，本reader读取该实际文件。子70仍是原事实，不改为科学成功。相反，缺result不造成功对象。

原R429必要字段投影保持：前三源的原计数／输入身份、完整field声明、metric完整活跃区／两帽／全闭算子flags、root计数、当前root和未触及rank后缀、reach曲率及pair的实际计数／pending责任。它不会把完整几何DFS或全部query包围表编码搬出；旧pending投影中未返回的完整对象仍只有原identity／数量与明确未读body范围。这种读回范围不能被表述为逐cell／逐数值独立核完。

新增provider状态是上述原必要metadata，不输出其全部query／primitive科学ledger。所有原raw、完整enclosures和全数组只保临时身份与所需未付地址。原stderr最多8192 bytes的明确末端excerpt合同不变，原完整bytes／SHA及省略范围明确，不冒全原文已读。

唯一必要JSON按原canonical ASCII序列化并含末LF，限90000 bytes。超界只输出一个真实小failure对象并返回70，`necessary_readback_complete=False`、cleanup条件False；不拆分、重编码、删原记录后谎称完整。原完整临时科学记录仍按owner责任保留，不能凭超界对象的SHA补未读值。

新stdout帧：

```text
BEGIN_CURRENT_C_TEN450_LIVE_QUERY_POSTSOLVE_NECESSARY
END_CURRENT_C_TEN450_LIVE_QUERY_POSTSOLVE_NECESSARY
```

GITHUB_OUTPUT沿原通用键 `postsolve_summary`、`postsolve_summary_bytes`、`postsolve_summary_sha256`、`postsolve_readback_complete`；它们只传这一份必要结论。原 `postsolve_cleanup_readback_condition_paid` 与 `original_upstream_BVP_readback_condition_must_also_be_paid` 分开，reader自身不执行清理。

## 10. R433 held 与其他薄层的兼容边界

R433 可显式白名单两套实际三元组：原R429 producer完整SHA／procedure schema／input schema，以及本R434 producer完整SHA／两个新schema。选择哪套，必须读取实际记录，不能只按文件后缀或未来参数猜。

R434 保留原 `Procedure.bind` 属性与前三stage路径／receipt、`producer_completed` 和 `OwnedChild` 接口。R433可复用相应真实producer的方法；只复用原79296 reader的标准库 `process_quiet` 时不需要错误调用其旧build／metric schema selector。R434不依赖R433，不等待held结果，也不增第六stage。

R431的mesh-refined上游身份、future完整十词输入及其他launcher分支没有被此修改默许。若未来调用方以另一个新driver/checkpoint source接入，必须明确自己的来源适配；本R434仍固定原R429接受的实际两阶段来源，不能把新mesh结果改标签后套用。

## 11. 源闭包、正文不变范围与未执行声明

新producer直接13个source pins＝原R429的11个逐basename／SHA保留＋R426 entry／provider两件。原R418 pin只是改常量名为 FIXED_METRIC，文件名与SHA不变；新METRIC指真正77be源，LIVE_QUERY指真正07fc源。R426自身继续核原六依赖及原R418来源，递归科学闭包没有被13这个直接计数替代。

原上游三个pin仍是6ff21118 launcher、11dd72f4 driver、43f217d1 checkpoint；radial5cc3134e、atlas02bb0c70、shared6a5f949a、reach3ea1ef9f、capacity07d45b95、cut28417b93、caps0ff1fa60及fixed metric28b7245a均沿原值。完整64位值都在新源码的PINS和交付manifest，不省略实际runtime核。

本地只做原文件全文阅读、准确文本replacement计数、SHA／bytes及正文比较：进程工具与OwnedChild的4451 B、invoke／shutdown的7698 B、producer_completed的1215 B、前三stage命令和控制的4136 B、reach及原终态flags的1372 B、reader generic quiet的1694 B和原stage／metric／pending投影的6083 B均逐字不变。这是代码差异记录，不是数学运行或新的发布门。

交付包含两份相对正式84d／79296的完整diff和publication manifest；它们是可从公开源重得的临时审读材料，不要求作为科学数据永久保存。源码未import、未AST、未编译、未运行，公开Actions实际执行尚未发生。没有新的workflow、请求、参数选择、伪checkpoint或accepted状态。

当前可执行责任是：真实同job完整450已存在且原来源责任成立时，以新独立输入显式给定原参数和十一查询资源，顺序运行原五stage，在原绝对deadline内把R426实际有限工作与完整未付状态交回一份必要结论。只有该未来实际输出才能报告新query是否发生、metric是否通过及其他几何责任是否已付。
