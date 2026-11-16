# R438 — 原始／细化 450 同场闭面流程的块 reach 与 held 来源接线

作者：OpenAI / ChatGPT（geometry agent，AI）。日期：2026-11-16。**独立源与条件接口；尚无 recipe、request、workflow、run 或实际接受父场。**

## 438.1　已实现的差异与结论边界

本次将 [R435 完整根对块](R435-complete-root-pair-blocks-and-closed-separation-cover.md) 作为一个明确的新 reach 角色接入 [R436](R436-original-or-refined450-same-job-complete-geometry-source-binding.md) 已有的原始／细化 450 五阶段流程。实现为三个独立文件，没有修改、重标或猴补任何冻结源码的全局变量。

| 新文件 | bytes | SHA-256 |
|---|---:|---|
| `geometry_20261116_current_C_ten450_original_or_refined_block_postsolve.py` | 66873 | `5bb2ee1d9526a10ec707d1106763e4ebe94599d7e5152f726864a6812ba8af95` |
| `root_20261116_current_C_ten450_original_or_refined_block_postsolve_necessary.py` | 26912 | `57413c73db29cb9f65451f631771c07c642edf162dfbe6cdbaa292b5fb451fe5` |
| `geometry_20261116_current_C_ten450_original_or_refined_block_postsolve_held.py` | 44769 | `119ec38cc9351a2d040ce8c7101b933e1e572d19deabb7baf62c4c1cec62eada` |

三个实际基础源分别仍为 R436 的 `43565f7c...` producer、`a565bc88...` reader、`ad492e57...` held。新 producer 仍读取真实原始 193 或真实 R431 细化入口，完整重做 radial、原 cuff atlas、shared field、R426 live-query metric 和 reach。只有 reach 可执行角色从冻结 R422 改为冻结 R435；R422 仍是 R435 真正调用的数学依赖，旧 pin 没有删除。

新 reader 返回完整当前块 frontier、原 single-rank 空间／相位栈、当前 union 工作和原曲率 frontier。新 held 增加一个严格匹配新 producer **SHA／procedure schema／input schema** 的分支，保原三个已注册分支与原 R425 入口。

没有自动选择 $K,\tau,\eta$、W、cap height、marker、预算、场或网格。块组织不保证提速，也不因为块数较少就宣布原 $N^2$ 责任已支付。未来完整同 job 入口可以显式调用这些文件；本次没有运行或预填其结论。

## 438.2　原始与细化两条真实来源

`upstream_kind` 仍只有两个准确值：

```text
original193-frozen450
R431-refined450
```

原始分支保持 R436 `Procedure.bind_original193` 全文：真实两阶段 launcher、原 design453/frozen450 顺序、两个原 full-DN exit、全部原接受 flags、native owner 关闭、真实 43f writer checkpoint、十词相同、真实当前 C/native geometry 和原 deadline。删去三行的 453、仅有初猜或小残差的状态都不是这个输入。

细化分支保持 `Procedure.bind_refined450` 全文：实际 R431 launcher 与 R427 driver、真实原始 193 origin、当前直接父、同一实际原 deadline、当前新 450 的原完整接受、真实新 writer/checkpoint、源闭包、十词／准确 target／原 C、完整 geometry 身份。新场的几何结果必须从**当前新 checkpoint**重算，旧父的 metric/reach/held 证书不转移。

`bound_frozen450_metadata`、`mesh_launch_quiet` 也保持原文。当前 writer 仍是 `43f217d1...`；M=112、N=2048、完整 450=338+112、零活动参数及真实分离边界责任不改。本组件只读取既有已接受记录，不重新求 BVP、重算 J 或降低门。

原绑定尚未返回时，五个 stage 全部保为 `not-started`，带原实际原因；不补造 accepted450 或给后继传一个假的 result。来源或元数据异常、真实资源停止和数学未付按原字段分开。

### 完整闭面“同 $g$”的额外固定范围

十词与原 C/DAG target 相同，首先固定的是相应标量目标和 BVP 来源。若要把不同网格后形成的整个闭面称为同一个完整闭目标，还必须冻结首次真实 construction 的 W、cap height、全部 marker 字词、材料坐标／transport 选择、尾与帽的定义及准确源解释。R436 已明确这一点，本次不缩减。

R438 每次真实读取并保存 `construction` 原词、实际生成 plan/atlas 和 source 身份；它**不**自动与某个先前 postsolve construction 比较，也不自行选择首次 W/H/marker。该首次冻结策略由独立调用者明确给出。本文不从“同十词”直接推断全闭 $g$ 相同，不把目标换成 $1+B'^2$ 或当前诱导 metric。

## 438.3　五阶段的实际角色

固定 stage 名、执行次序和三个来源前置不变：

| stage | 执行入口 | 原完整输入及责任 |
|---|---|---|
| `radial_replay` | 原 `5cc3134e` Node radial | 当前真实 checkpoint、真实 geometry、全形状／均值／两阶节点 |
| `original_cuff_atlas` | 原 `02bb0c70` R413 | 原 cuff、明确 W/H/全 marker construction、同 target |
| `shared_field` | 原 `6a5f949a` R409 `prepare` | 以上真实 radial/plan，完整当前 shared field |
| `metric` | 原 `77be1d98` R426 | 当前 shared field/atlas、同 C 和 `07fc4e41` live-query provider |
| `reach` | 新角色 `e3fcd9eb` R435 | 同一个 shared field/atlas/accepted450，完整原 R422 曲率与块/叶责任 |

前三个 producer 必须实际产生相应完整原件。R413 原 result/plan 已完成而仅 stdout 超限返回 70 的原合法分支仍保留；同 job 下游读取实际文件，不把传输超限冒几何失败。

metric 与 reach 不相互门控：原 metric 未决、负结果、partial 或执行错误，只要自有子进程已经停止、同一 deadline 尚有时间且前三原件存在，仍调用 reach。held 同样不以 metric 或 reach 成功为条件。资源耗尽或前一个子进程未静默可以阻止后继运行，但这被明确记作资源／生命周期未启动，不是新增科学门。

新 reach schema 为：

```text
R435-current-C-ten450-complete-hierarchical-root-pair-reach-v1
```

producer 的 `RESULT_SOURCES/RESULT_SCHEMAS` 同时改成该真实新 source/schema。旧 R422 没有改名，它仍以原 `3ea1ef9f...` 被 pin 并由 R435 加载。R435 内部完整 old root universe、原 rank、两反射片、两帽、全角与两闭 RP1、原四门 OR/R282、所有 pending 和原 $K\tau$ 合取责任均由已证明实现承担。

## 438.4　完整直接源闭包

原 R436 的 15 个 basename/SHA 对逐个保留，只新增 R435，因此新 producer 直接表为 16 件。各科学入口的原转递闭包继续由其自己的原 loader 实际核验；这里不以16个文件代替完整数学来源。

| 原／新直接源 | SHA-256 |
|---|---|
| `geometry_20261115_continuous_ten_full453_frozen450_launch.py` | `6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66` |
| `geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py` | `11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8` |
| `geometry_20261115_continuous_ten_frozen450_checkpoint.py` | `43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae` |
| `geometry_20261115_current_C_ten450_radial_readout.mjs` | `5cc3134ed58aed45efea012219aa2e889624c47b41d5ee9f558da231806ab568` |
| `geometry_20261115_current_C_original_cuff_target_atlas.py` | `02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2` |
| `geometry_20261115_current_C_ten450_shared_field.py` | `6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3` |
| `geometry_20261115_current_C_ten_complete_relative_metric.py` | `28b7245a134d3556085bc1884cd2edf6b0cdaf4976c58e3dc6d5327ce19a7590` |
| `geometry_20261115_current_C_ten_live_query_complete_metric.py` | `77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892` |
| `geometry_20261115_same_job_C_live_query_provider.py` | `07fc4e41a6318c43a6e03313356df4df7538ccd5ea110406434b2e420c09bcd9` |
| `geometry_20261115_current_C_ten_complete_reach_cover.py` | `3ea1ef9fb56ec10301defa18d832681d6061d8646e78893957ca160279b71834` |
| `geometry_20261116_current_C_ten_complete_block_reach_cover.py` | `e3fcd9eb7ed304cd502c7e03186d65a2d414366c8ad47313c5754aa43ded66ad` |
| `exact_20261114_tail_capacity_loader.mjs` | `07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395` |
| `geometry_20261115_current_C_accurate_cut_patch.py` | `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` |
| `geometry_20261115_current_C_ten450_fixed_cap_balls.py` | `0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae` |
| `geometry_20261116_current_C_frozen450_mesh_owned_launch.py` | `4375375b343bc2e3b359a2e1ca566bb6648e08b691d7208cced348f185272868` |
| `geometry_20261115_continuous_ten_frozen450_mesh_refinement.py` | `70a5709d6bca4bf124a029ebcc33fae31407c3214c5164a867a8de9f37d53928` |

新 held 仍固定原 `root_20261115_current_C_ten450_postsolve_necessary.py` 的 `79296f4f...`，只调用其通用 `process_quiet`；不会运行它的旧必要选择器。真正 held 数学入口仍是 `geometry_20261115_current_C_ten_held_and_rigidity_inputs.py`，完整 SHA `c87b3a9b9d17f74d8c4f4066f65318e50fed5a56143f620628049a86dcf77ef2`。R425 的全像位置覆盖、D、反射责任、真实 witness plan 和误差条件一项不改。

## 438.5　producer 的实际 input 与三个新增工作字段

新 producer schema 与 input schema：

```text
current-C-ten450-original-or-refined-same-job-live-query-block-reach-geometry-v1
current-C-ten450-original-or-refined-same-job-live-query-block-reach-geometry-v1-input-v1
```

保留 R436 全部字段：`upstream_kind`、真实 `namespace/upstream_launch_directory/job_deadline/geometry_directory/continuous_e_directory/computations/proof_directory/source_topic/out`，真实 `job_deadline_sha256/continuous_e_result_sha256`；细化分支另需 `origin_launch_directory`。可用实际 `upstream_result_sha256` 锁定原输入文件。

`construction` 仍恰由 `cut_correction_width/cap_height/fixed_cap` 组成，`fixed_cap.markers` 为显式完整列表；即使为空也必须真正声明，不自行补空表。`metric` 与 `c_queries` 完全沿原 R436/R426 schema，后者仍有11个显式精度／积分／inverse／node／panel／时间参数。

`reach` 的原12键逐个保留：

```text
curvature_upper, target_reach, active_depth, curvature_max_depth,
pair_max_depth, interval_bits, sqrt_bits, max_cells,
max_pair_nodes, max_pairs, cache_entries, max_constant_levels
```

新角色另要求恰好三个明确的正整数工作参数：

```text
max_block_nodes, max_union_cells, block_cache_entries
```

它们分别限制根对索引块尝试次数、实际原根位置包围请求次数和联合记录的 LRU 容量。原 `max_pairs` 仍是原 flat rank 的独占上界，不能把跨界块夹带支付；R435 的非顺序 DFS 在停止时给完整块集合，不给伪造的连续 rank 后缀。$K/\tau$ 原有理文字原样转为 CLI；旧空间／相位深度、原 cell/node/rank 预算没有自动扩大或重分配。

这三个计数上限没有数学阈值意义，不是新的接受门。所有资源和常数都需要未来真实 recipe 给出，本次没有预填值。

## 438.6　唯一原 deadline 与进程生命周期

`resources` 保原 `free_bytes_reserve/node_heap_mib/child_shutdown_reserve_seconds` 以及恰含五个 stage 的 `stage_budgets_seconds`。

原始分支核所读 deadline bytes/SHA 等于原始 launcher 的实际 `actual_job_deadline`。细化分支另核该同一文件同时等于真实 origin 与 refined launcher 的 receipt；不生成一个新的起点。设原文件给出的 namespace 创建时刻与 science 总时长为 $t_0,T$，则唯一 science deadline 仍为 $t_0+T$。

每个原 `invoke` 计算

$$
T_{\rm child}=\min\{T_{\rm declared,stage},\ t_0+T-t_{\rm now}-T_{\rm shutdown}\}.
$$

无正余量则保未启动，不偷偷增加 clock。真正启动时，原 `Popen(start_new_session=True)`、PID/start-ticks/独占 session 观察、TERM/KILL/wait、磁盘检查、外部中断与输出 fsync 全文保留。信号只发给实际观察且 start-ticks 仍相同的自有进程，不碰父 job 的共享 PGID。

原外部监测会在 child science 时限或原 absolute deadline 前的 shutdown 余量处停止自有子进程。内部 R435 仍使用自己的 cooperative Budget；新层没有把它冒成独立的绝对 kill clock。绑定和最后元数据／必要读回仍受调用者实际 job 总限与其原保留时段约束；本次没有 workflow，不宣称已保证所有阶段和读回都能在预算内完成。

原 `OwnedChild`、`mesh_launch_quiet`、两个 bind、`skip/shutdown_allowance/invoke`、`producer_completed/run` 的五阶段命令正文和 `finish` 均与冻结 R436 逐文本相同。新 role 及参数由独立文件自己的常量表选择，并没有把旧模块加载后改全局仍称旧 SHA。

## 438.7　必要 readback 的精确新范围

新 reader schema：

```text
current-C-ten450-original-or-refined-block-postsolve-one-necessary-conclusion-v1
```

它只读实际临时 JSON／文件身份和 `/proc` 元数据，不导入科学源码、不再算任何误差、曲率或 rank 算术。读取前，原 procedure 必须完成其 finally，所有自有组与原 procedure PID/start-ticks 已静默；原文件 receipt 在读前及必要读后仍核同。

在 `stage_rows` 中 `name=reach` 的 `necessary_original_values` 下，以下路径具有准确意义：

| 路径 | 返回范围 |
|---|---|
| `original_reach_fields.values` | 原阶段、绑定/全账身份、全 $D$、常数、unstarted、reach 和 README flags |
| `original_pair_fields.values` | 完整原 pair 计划／退休计数、块／singleton attempts、逐 family、原 gate flags、report error |
| `original_pair_pending.values.pending` | **完整**当前未退休块 frontier、当前原 single-rank 栈、未启动 RP1 根、当前 union frame、原未付计数及账地址范围 |
| `original_curvature_pending.values.pending` | **完整**当前闭曲率 DFS frontier、实际 root 与原未访 root 后缀 |
| `original_union_bounds` | 原联合状态全文，或与上述 `pending.current_union_work` 完全规范字节相同后的显式引用 |

引用去重必须先比较两个完整 `canonical(value)` byte string；不是只看数值近似、对象个数或 hash，也不会把 `1`、`true`、`1.0` 等不同 JSON 字面类型随意混同。摘要明示引用在同一个结果投影中的准确字段路径及 canonical identity。若不相同，就分别保原值。

原 reader 的 `selected` 继续带 `absent_keys`，缺键与显式 null 分开。R435 当前 pending 不再经过旧 flat-rank `pending_projection`；不能用一个 suffix、数量或 SHA 代替当前未退休块。R426 metric 的原必要投影、原 source-query 未付范围和其来源核保持不变。

已退休的成功／未付历史 leaf、完整 union 坐标、六 jet 与大 ledger 不全搬回；它们留原临时文件，保 bytes/SHA/行数和未读正文声明。**历史未付叶地址完整保存在原 ledger，不表示工具端已逐行回传。** 整个当前 frontier 则确实在必要正文中。

原结构化错误、资源／中断、未启动 stage、未返回 result、metadata 错误和所有原 flags 都保留。stderr 仍沿冻结 reader 的最多8192-byte尾摘录规则，给准确显示范围、遗漏前缀字节数和是否完整 UTF-8；它不是完整大日志或全部错误历史的保证。原 stdout 只核完整身份，不拆段或编码传输。

最终必要 JSON 仍一份、上限90000 bytes。极端 frontier／错误／多阶段字段导致超限时返回70，给 attempted bytes/SHA 和完整原 procedure 身份，`necessary_readback_complete=false`、清理条件false；不截断 frontier、不升限、不分包。正常 `necessary_readback_complete=true` 只是该明示必要选择范围完整，绝不是几何成功。

## 438.8　held 的精确新增来源分支

独立 held schema 为：

```text
R438-current-C-ten450-original-or-refined-block-same-job-held-after-shared-v1
```

input 追加 `-input-v1`，必要读回追加 `-necessary-v1`。注册表保留原 R429、R434、R436 三条准确分支，另增加：

```text
source:
  geometry_20261116_current_C_ten450_original_or_refined_block_postsolve.py
SHA:
  5bb2ee1d9526a10ec707d1106763e4ebe94599d7e5152f726864a6812ba8af95
procedure schema:
  current-C-ten450-original-or-refined-same-job-live-query-block-reach-geometry-v1
input schema:
  current-C-ten450-original-or-refined-same-job-live-query-block-reach-geometry-v1-input-v1
```

选择时三者必须全匹配；不存在“同类来源”通配、改个 schema 自称验证或从参数个数推断 producer。选定后导入的只是该准确 stdlib procedure 与原通用 quiet helper，调用原 `validate_spec`、`Procedure.bind` 和 `producer_completed` 做真实来源重核，不执行其五阶段 `run`。

R438 producer 的两个实际 bind 正文未改，所以原 `OriginalBindingView` 所需属性仍完整。held 重新核同真实 checkpoint、当前 C、原 deadline、三个真前置 producer 与 shared/atlas/witness plan；同一 actual deadline receipt 原封不动转入其剩余时间计算。三个前置仍恰为 `radial_replay/original_cuff_atlas/shared_field`，metric/reach 的真假不是条件。

R425 原八个参数和三个资源字段保留：位置／prefix／tail witness 计划、完整反射包围、全像 D、所有 marker、原错误／未访和单90K必要摘要都没有改动。`Procedure.bind/run/finish` 相对 R436 held 全文不变，只有独立来源、schema、module name 和 marker 身份发生明确变化。

五阶段 procedure 原字段 `actual_held_rigidity_and_deltaE_not_executed=true` 仍准确描述它自己的范围。后继 held 是另一个独立真实 producer，其实际结果另读；不能改写先前 procedure 记录，把一个未来 held 结果预填回五阶段原件。

## 438.9　完整调用形状和临时路径

以下只是入口形状，尖括号由后继实际同 job 文件替换；没有具体参数或未来 SHA：

```text
python geometry_20261116_current_C_ten450_original_or_refined_block_postsolve.py
  --input <actual-postsolve-input.json>
  --input-sha256 <actual-input-SHA>

python root_20261116_current_C_ten450_original_or_refined_block_postsolve_necessary.py
  --directory <actual-postsolve-owned-output>
  --out <fresh-necessary-summary.json>

python geometry_20261116_current_C_ten450_original_or_refined_block_postsolve_held.py run
  --input <actual-held-input.json>
  --input-sha256 <actual-held-input-SHA>

python geometry_20261116_current_C_ten450_original_or_refined_block_postsolve_held.py readback
  --directory <actual-held-owned-output>
  --computations <actual-complete-computations-directory>
  --out <fresh-held-necessary-summary.json>
```

所有目录仍在实际 `RUNNER_TEMP` 内的原自有 namespace；新输出须为原上游／geometry／input 的兄弟，而不能包含它们。R435 的 fresh out 子目录自然落在该真实 namespace 的 `reach` 中，符合其自身 resource ownership 护栏。原科学 stdout/stderr 在每个stage旁临时保存；五阶段子程环境移除 `GITHUB_OUTPUT`，只有必要 reader 写最终小输出。

五阶段必要 stdout marker：

```text
BEGIN_CURRENT_C_TEN450_ORIGINAL_OR_REFINED_BLOCK_POSTSOLVE_NECESSARY
END_CURRENT_C_TEN450_ORIGINAL_OR_REFINED_BLOCK_POSTSOLVE_NECESSARY
```

原输出键 `postsolve_summary/postsolve_summary_bytes/postsolve_summary_sha256/postsolve_readback_complete` 不变，内容 schema/source 已明确改为新身份。

held 必要 marker：

```text
BEGIN_R438_CURRENT_C_ORIGINAL_OR_REFINED_BLOCK_HELD_NECESSARY
END_R438_CURRENT_C_ORIGINAL_OR_REFINED_BLOCK_HELD_NECESSARY
```

原 `postsolve_held_summary` 及其 bytes/SHA/complete 键也保持。必须核内容的实际 source/schema/原文件身份，不能只凭输出键名字相同。

所有raw都保留，本组件不执行清理、artifact上传或 Git/Release存档。`postsolve_cleanup_readback_condition_paid` 只标这一次明确必要读回；原 BVP、mesh及其他实际 producer 的完整必要读回和进程静默仍分别需要支付。后继 caller 负责整体清理条件，不能仅因某阶段 exit 0 就删未读输出。

## 438.10　来源组合命题

**命题。** 假设未来实际输入通过未改变的 R436 原始或细化绑定，并且三个真实前置阶段返回相应完整原件。在同一个实际原 deadline 和原资源限制下，本 R438 调用的 R435 正是以该次真实 shared field、原 atlas、当前 accepted450、同 $K/\tau$ 及原全部科学参数执行的完整块 reach consumer。若它返回数学通过，则只能在 R435/R422 的原假设与全部 flags 范围内解释；若任一责任未付，其原完整当前地址按 §438.7保留。后继 held 则在同一来源与 deadline 上调用原 R425，不依赖 metric/reach 是否通过。

**证明。** 两个 bind 的源码正文与 R436相同，且 source pins保全原15项，因此所选实际父、十词、target、C、geometry、writer与原 deadline没有新增推断。`run` 的前三步和 metric 命令正文保持，三个原 output receipt再次逐bytes/SHA核同；到reach的 `base` 正是由这一真实shared result/atlas/checkpoint构成。独立常量 `REACH`、对应完整pin与expectedschema把实际child唯一指向R435；原12参数原样传递，新增三个只影响已证明组织和工作资源，不改变字段、原rank宇宙或原门。

R435 的整块距离证明、完整分裂、单rank原方法委托与全部pending语义由其原证明给出。新reader仅读该真实result/原source/schema和实际quiet记录，原当前pending对象原样选取；等值引用只发生于两个完整规范JSON字节相同之后，所以不损失任何当前union状态。旧历史大账的未逐值读回边界明确保留。整个必要输出若超限则报告未完整，不能推出通过。

最后，held选择完整SHA/schema/input元组，重新执行选定真实producer的原bind，仅以三个真实前置为来源。原R425数学入口、参数、deadline核与生命周期正文未变，故没有借metric或reach通过来替代held自己的科学责任。证毕。

该命题是接口与来源组合结论，不是新的 reach/metric/held 定理，也不产生实际场。全闭同 $g$ 的首次construction冻结条件仍如§438.2；有限数值父与准确几何/ODE误差、完整终门和后继精化仍各自保留。

## 438.11　文本核对与交付状态

三份独立源相对冻结R436的完整 unified diff一并提供临时阅读；source-text preservation 回执仅比较指定正文字符串，没有AST/导入/编译/fixture或科学执行。已逐字相同的段包括原两父bind、mesh身份helpers、OwnedChild、预算与调用、五阶段命令正文、finish、reader.process_quiet、held bind/run/finish。

这些临时diff与文本生成脚本可从已提交源重生，不作为数据加入Git。正式交付仅三份新源码及本文。后继 request203 若采用该入口，必须提供其自己的真实recipe、全部源闭包、原时钟和必要输出收尾；本次没有先派发、预写成功或暗改任何运行中的科学源。
