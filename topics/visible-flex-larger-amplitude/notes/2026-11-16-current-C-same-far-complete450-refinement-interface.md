# R456：同一完整 far 来源下的真实 450 细化调用链

作者：geometry agent（AI）。日期：2026-11-16。

## 1. 交付与范围

本交付是独立九运行源、[R456 条件证明](../results/R456-same-far-complete450-refinement-and-explicit-origin-composition.md) 及本接口。它把已发表 R450 的完整 far 复用接到 R448 的原径向/角/steps 细化算法，同时明确登记 actual202205 的最终 R449/205 来源和 R452 首构造 A/B。

没有新增 request、workflow、实际父场、因子、预算值、接受记录或 run。旧 R441、R448、R450、R452 和所有运行中的实验都保持原字节。当前没有执行新源码的 import、AST、compile、科学或 fixture；本地只读写源码文本、做字节身份与完整文本差异。真正执行仍限 `GITHUB_ACTIONS=true` 且 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。

原准确 C 根族/连续十族目标、有限数值 geometry 和有限 native 程序保持不同对象。复用的原 far 行和误差不能推出某个数值代表是统一准确 C 实现，也不能替代无限 DN 或几何结论。固定 $M=112$，保 $338+112=450$、全部双 mean 和所有 $338\times112$ 响应。M 扩展与其 postsolve 注册不包含在本九件中。

## 2. 九个独立入口

| 角色 | 文件 | 作用 |
|---|---|---|
| sampler | `geometry_20261116_current_C_same_far_registered_resampling.py` | 原 R450 完整 far binder、fresh-grid、配置生成和可选必要读回；新增实际205 clock 来源 |
| worker | `geometry_20261116_current_C_same_far_registered_native_worker.mjs` | 只接新 sampler 身份，原 full112 live native、敏感度及独立 audit 算法保持 |
| client | `geometry_20261116_current_C_same_far_registered_tail_client.py` | 原四参 TailClient，接独立 worker/sampler 来源 |
| driver | `geometry_20261116_continuous_ten_frozen450_same_far_refinement.py` | 原 R448 全细分 seed、fresh450、当前H/FD/fullDN/final/audit 与 bf7 writer |
| owner | `geometry_20261116_current_C_frozen450_same_far_owned_launch.py` | 原绝对钟下 sampler→配置→450，来源、父链、进程和资源完整绑定 |
| solve reader | `root_20261116_current_C_frozen450_same_far_necessary_readout.py` | 同far范围及真正450的单份必要读回，原 FD/native 选择器复用 |
| postsolve | `geometry_20261116_current_C_same_far450_postsolve_geometry.py` | 真新 checkpoint 的五个原 R441 几何角色，205分支绑定R452首A/B |
| postsolve reader | `root_20261116_current_C_same_far450_postsolve_necessary.py` | 原闭覆盖/frontier/错误加第一A/B来源的单份必要读回 |
| held wrapper | `geometry_20261116_current_C_same_far450_postsolve_held.py` | 在真 shared/atlas 后独立调用原 R441 held 源及其必要读回 |

worker/client 的派生只含来源、文件和 schema 字面变化。sampler 的原 `bind_original_far`、`fresh_grid` 和完整停止责任不改科学。driver 的 `resolution_seed`、原真正 `run_phase` 和末门保持；独立变化位于当前 native family/配置/原 far 来源绑定。owner、postsolve 和 reader 的变化是本接口逐条列出的真实调用责任。

## 3. 精确 schema

| 入口或原件 | schema |
|---|---|
| 新 sampler result | `R456-current-C-same-complete-far-family-fresh-radial-sampling-v1` |
| 新 sampler standalone necessary | `R456-same-far-fresh-grid-one-necessary-readback-v1` |
| 新 native worker | `R456-current-C-complete112-live-native-worker-v1` |
| 新 TailClient | `R456-current-C-complete112-live-tail-client-v1` |
| 新 450 driver | `R456-current-C-continuous-ten-frozen450-same-far-resolution-original-full-DN-v1` |
| 新实际 recipe | `R456-explicit-current-C-ten-frozen450-same-far-resolution-refinement-v1` |
| 新 owner | `R456-current-C-frozen450-same-far-resolution-owned-launch-v1` |
| 新 owner input | owner schema 加 `-input-v1` |
| solve necessary | `R456-current-C-same-far-resolution450-one-necessary-readback-v1` |
| 新 postsolve | `R456-current-C-same-far-resolution450-same-job-live-query-block-geometry-v1` |
| 新 postsolve input | postsolve schema 加 `-input-v1` |
| postsolve necessary | `R456-current-C-same-far-resolution450-block-postsolve-one-necessary-conclusion-v1` |
| held wrapper | `R456-current-C-same-far-resolution450-same-job-held-after-shared-v1` |
| held input / necessary | held schema 分别加 `-input-v1` / `-necessary-v1` |

新 native config 仍是原 `current-C-complete112-client-config-v1`，完整 geometry 仍是 `current-C-native-radial-geometry-bundle-v1`。它们保持原字段数学意义，但明确指向新 sampler/worker/client 的真实完整 source map；这不是把旧科学结果改 schema。

新 checkpoint 使用已发表 writer `geometry_20261116_continuous_ten_resolution_checkpoint.py`，SHA `bf7dedd2135e3f6b54bc806a17064428111b502b6ddb8572ec66a883b1ce34ad`，schema `R441-current-continuous-ten-resolution450-physical-DN-checkpoint-v1`。新 manifest 的 `actual_driver_source` 和 runtime closure 是实际新 driver，不会改名旧父 manifest。

## 4. 原始来源与允许的父

### 4.1 三个原始来源

owner 的 `origin_launch_directory/result.json` 必须是以下三者之一，且为同一实际 run/source。新 sampler 的 `ORIGINS` 也独立列同三个 launcher/clock；不会修改已发表 R450 的全局常量。

| kind | launcher 文件及完整SHA | driver 文件及完整SHA |
|---|---|---|
| `original193` | `geometry_20261115_continuous_ten_full453_frozen450_launch.py` / `6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66` | `geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py` / `11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8` |
| `joint203` | `geometry_20261116_continuous_ten_joint_full453_frozen450_launch.py` / `cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7` | `geometry_20261116_continuous_ten_joint_full453_frozen450_physical_dn.py` / `5400aa4a724b0403e6a89db2ea056f489dc336e685fa85e2ef1ef0fc51569592` |
| `actual202205` | `geometry_20261116_actual202_accurate_ten_full453_frozen450_launch.py` / `227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7` | `geometry_20261116_actual202_accurate_ten_full453_frozen450.py` / `56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615` |

三者原 clock schema 分别为 `request193-owned-job-science-deadline-v1`、`request203-owned-job-science-deadline-v1`、`request205-owned-job-science-deadline-v1`。实际 deadline 文件必须正是该 launcher 的 `actual_job_deadline`，并与其 recipe SHA 和原18900/2700字段一致。

原 positive 数值族为 sampler `965c277c5aad5a3b5c8c817600d4c435186d9ce1b267b0b59f6e7a8fa69de390`、client `acb8b67b8e44dbfae9b0d166bfc75910f2c48a6aca238571db44d20520a0a1f9`；joint203 和 actual202205 的原 joint 族为 sampler `32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4`、client `02e1645248ef01ffff10a50c2198194fafd40709254816408e1b9944e1cd0ae1`。更换来源不能只给一个相似 schema。

### 4.2 父字段的真实合同

`parent_launch_directory` 可以等于 origin 的实际目录，或是下面的真实成功 owner。每个 successor 均需保 `origin_launch` 和相同 `actual_job_deadline`，真实 adapter、完整 accepted450 checkpoint、原所有末门和实际 quiet；没有普通 partial 或伪造父状态的分支。

- R431，仅 original193：owner `4375375b343bc2e3b359a2e1ca566bb6648e08b691d7208cced348f185272868`，driver `70a5709d6bca4bf124a029ebcc33fae31407c3214c5164a867a8de9f37d53928`。
- R441：owner `2247aa97c4ed63c9065d1e326fb78b84500ee7b834f0970905e977773bcea8df`，driver `bf1f8d2dda15584791147f97dc6f313435c16d080acaa49ef418c2df06d503b3`。
- R448：owner `f3a2abf626fbb7f636315e40608b55170748a779e7bdf1287ebc362e04b73cf2`，driver `137d42cb27bb1aef227d42445adf07a6d11f7bba57315abdf151cc3b0086c7e8`。
- 本 R456 实际 owner/driver；其完整身份见末表。

旧 R441/R448 自身未注册 actual202205。因此上面保留的是它们真实已实现的父合同，不声称现在可以伪造一个“205 旧 R448 父”。actual202205 可以从其真正原450直接进入 R456，再由真实 R456 后继继续。

所有父必须完整保十词、准确 target identity 和真实 finite compiler。父的 Y/DY 只作为新初猜，不能把453删三行当450，也不能把父状态/接受当此次接受。

## 5. owner 的完整 CLI 和输入

入口：

```text
python geometry_20261116_current_C_frozen450_same_far_owned_launch.py \
  --input ACTUAL_RUNTIME_INPUT.json \
  --input-sha256 ACTUAL_INPUT_SHA256
```

`ACTUAL_*` 在本文仅表示调用位置，不是已经存在的运行数据。输入 JSON 必须由未来同job调用者基于真实文件生成并绑定。必须有以下字段：

| 字段 | 合同 |
|---|---|
| `schema` | 本 owner schema 加 `-input-v1` |
| `namespace` | 实际 RUNNER_TEMP 下的原 owned namespace，不创建新科学起点 |
| `origin_launch_directory` | 4.1中实际原两阶段 launcher 目录 |
| `parent_launch_directory` | 4.2中真实父；可等于 origin |
| `job_deadline`, `job_deadline_sha256` | origin 真正消费的原绝对钟原件 |
| `computations` | 当前真实源码目录 |
| `accepted`, `accepted_sha256` | origin原 `actual_input_files.accepted` 构造来源，不是给它改成新的场结果 |
| `tail_config`, `tail_config_sha256` | origin原 `actual_input_files.current_native_config` 原件；与下面originalfar配置用途不同 |
| `tail_source_root` | origin真command中的唯一 `--tail-source-root` 原目录 |
| `out` | 新鲜 owned sibling，不能包含任何父/源码/输入，也不能在旧父树中 |
| `max_nodes` | 显式完整seed/solver容量，整数≥2，不自动沿用1200 |
| `refinement_factors` | 下列5键，正整数且至少一个>1 |
| `resources` | 下列5个明确资源键 |
| `sampling` | 完整同far/fresh-grid来源与工作参数 |

`refinement_factors` 恰含：`radial_mesh`、`field_and_native_angles`、`native_steps`、`material_angles`、`physical_angles`。field/native angular quadrature 共用第二个因子；material 与 physical 角网格分别用各自因子。M=112、stage576保持。纯mesh时其它四因子允许1。没有推断未来合适因子或误差结果。

`resources` 恰含：

- `sampling_process_budget_seconds`：sampling与configure共同使用的process allowance；
- `refinement_process_budget_seconds`：真正450 child的最大process allowance；
- `child_shutdown_reserve_seconds`：原停止/回收预留；
- `minimum_free_bytes_at_start`：每次启动前明确容量；
- `free_bytes_resource_stop`：实际运行中空间停止，必须小于startup容量。

以上均需未来调用者实际给定。前3个为有限正数，后2个为正整数；不是数学接受阈值。

`sampling` 的路径/identity 字段：

```text
cover_directory, cover_result_sha256
far_directory, far_result_sha256
proof, unit_row_proof
original_sampling_directory, original_sampling_result_sha256
original_config, original_config_sha256
parameters
```

`cover` 和 `far` 是实际同C原完整结果，不能仅给cut三个盒。`proof` 和 `unit_row_proof` 保原生产器的 R380/R357 身份。

`original_sampling_directory` 是**真正原 full-far** positive/joint生产器目录。首个R456必须等于实际父geometry目录；后继R456必须沿父保留的 `same_original_far_family_reuse.original_directory/original_result` 回到原件。它不是上次新网格的目录，也不能重标schema。

`original_config` 是消费该原完整far的真实完整配置。首个R456取父checkpoint内实际 native配置member（或同bytes/SHA原件）；后继取父配置 `R456_same_far_fresh_grid_origin.original_config` 原receipt。它与顶层 `tail_config` 的原origin来源检查分工不同。两者都必须真实存在，不可由旧hash恢复。

`sampling.parameters` 恰含7键：

| 键 | 类型/范围 |
|---|---|
| `precision_bits` | 正整数，原sampler继续核其实际资源域 |
| `budget_seconds` | 显式有限正数，原fresh-grid内部合作式预算；仍受外部owner裁剪 |
| `free_bytes_reserve` | 正整数 |
| `max_geometry_cache_records` | 正整数 |
| `sample_max_nodes` | 正整数，原fresh sampling工作容量 |
| `sample_inverse_depth` | 正整数 |
| `sample_value_bits` | 正整数 |

本次不再接受原fullfar专用的 `linear_budget_seconds/max_panels/max_depth/local_defect_bits/panel_norm_limit/taylor_terms/representative_max_precision_bits` 作为假装会执行的参数。原已完成far的完整误差和工作来源仍保在原对象；没有重新生产代表行，故不追加一次代表精化。

## 6. owner 实际生命周期与输出

### 6.1 采样与配置

owner先核真实父完整450、目标、来源、原far/config及原钟，再真正运行新 sampler `sample`。该 child保留原完整far一处sample和实际$\mu$，其余新需要点/steps网格均由原算法重新生成。它保原完整unused/pending scope和异常；不启动native。

sample返回且实际quiet后，owner读其完整result，核原far identity/$\mu$、同C输入、完整新geometry以及同物理far/cut。此刻立即记录 `actual_sampling_completed=True`。之后才运行独立 owned `configure` child。configure只是元数据动作，仍是受同一原绝对钟约束的独占子进程，不能用无钟的裸 `subprocess.run`。

configure的process allowance是原 `sampling_process_budget_seconds` 减去sampling开始以来实际时间，非重开全额。两次 child都保原shutdown预算；最终shutdown和父元数据操作有实际成本，不承诺所有阶段在理想加总时间内完成。原绝对截止和真实外层规则/硬限仍需未来工作流接好。

configure生成 `actual-refined-native-config.json`。它只更新geometry身份、N、steps、独立3source和公开 `R456_same_far_fresh_grid_origin`。全部原阈值/算法/runtime/source未知键仍完整比较。若配置失败，采样已完成的事实不会被抹掉，BVP保持未开始。

### 6.2 真正450

配置和采样均完成且quiet后，owner运行新driver。driver CLI为：

```text
python geometry_20261116_continuous_ten_frozen450_same_far_refinement.py \
  --recipe ACTUAL_RESOLUTION_RECIPE --recipe-sha256 ACTUAL_SHA \
  --accepted ORIGINAL_ACCEPTED --accepted-sha256 ORIGINAL_SHA \
  --parent-directory ACTUAL_PARENT_CHECKPOINT \
  --parent-manifest-sha256 ACTUAL_PARENT_MANIFEST_SHA \
  --tail-config ACTUAL_NEW_CONFIG --tail-config-sha256 ACTUAL_NEW_CONFIG_SHA \
  --tail-source-root ACTUAL_ORIGINAL_SOURCE_ROOT \
  --tail-client CURRENT_NEW_CLIENT --jac-workers 2 --node-heap 6144 \
  --out OWNED_REFINED_BVP --work OWNED_BANDED_WORK
```

正常调用必须由owner组织；直接调用driver本身不能冒已有异步总钟。driver原真正算法保 $8$ outer、$17$ inner、RMS $10^{-6}$、BC $10^{-11}$、FD $5\times10^{-5}$、full native32/10/$2\times10^{-9}$ 及完整末消费者。没有改acceptance或选择新父。

owner实际输出主要为：

- `result.json`：原来源/父、deadline、全部 observed_children、三角色实际状态、资源/错误/quiet；
- `actual-resolution-recipe.json`：真实父十词和显式因子生成的新recipe；
- `native-sampling/`：新sample所有原result/geometry/完整ledger/临时数组；
- `actual-refined-native-config.json`：owned configure真实输出；
- `refined-BVP/adapter-status.json` 与 `refined-BVP/refined450/`：真正新科学；
- `banded-work/`：原完整带状求解临时数据；
- `sampling.*.log`、`configure.*.log`、`refinement.*.log`：独立完整原stdout/stderr。

每个实际child保PID/start_ticks/独占PGID、停止/回收/identity conflict及stdout/stderr身份。中断或存储不足只记对应scope，不据job红推数学。新原parent状态逐词保留只适用于seed，末状态与末mesh由真实solver输出决定。

## 7. sampler 自身CLI

正常由owner生成；独立接口完整保留，便于真实同job调用者复用而不猴补模块。

`sample` 必需路径参数：

```text
--cover-directory --far-directory --original-sampling-directory
--code-directory --proof --unit-row-proof --origin-launch-directory
--job-deadline --out
```

必需SHA参数：`--cover-result-sha256`、`--far-result-sha256`、`--original-sampling-result-sha256`、`--origin-launch-result-sha256`、`--job-deadline-sha256`。`--original-family`仅`positive`或`joint`；actual202205对应joint原族，但其clock来源仍实际205。

必需整数参数：`--steps`、`--precision-bits`、`--sample-max-nodes`、`--sample-inverse-depth`、`--sample-value-bits`、`--max-geometry-cache-records`、`--free-bytes-reserve`。必需浮点预算参数为`--budget-seconds`。`steps`由owner准确父值乘因子，不是另猜的采样网格。

`configure`参数：`--directory`、`--result-sha256`、`--original-config`、`--original-config-sha256`、`--computations`、`--quadrature`、`--out`。原配置的geometry必须确为保留原far。新配置生成没有native调用，也不变阈值。

`readback`参数：`--directory`、`--result-sha256`、`--out`。这是原R450选择范围的独立单90KB元数据读回。正常完整R456调用由下节新solve reader覆盖相同必要范围，避免重复运行两份读回。不要把standalone readback成功当成全部450或quiet完成。

## 8. solve必要读回

```text
python root_20261116_current_C_frozen450_same_far_necessary_readout.py \
  --namespace ACTUAL_NAMESPACE --launch-directory ACTUAL_NEW_OWNER_OUT \
  --computations ACTUAL_COMPUTATIONS --out FRESH_READBACK_DIRECTORY \
  [--entry-stdout ACTUAL_OUTER_STDOUT] [--entry-stderr ACTUAL_OUTER_STDERR]
```

reader只导入已钉住的标准库元数据helper。positive来源用原34b49必要selector；joint203与actual202205用原19878e joint selector。这里的“19878e”是reader源码SHA前缀，不是request198；没有把有限Gauss父搬进连续C。

新 sampler 的必要选择独立写在 `same_far_sampling_view`，不尝试把其result交给只认旧fullfar schema的原selector。它保：

- 实际原完整far/配置/输入、全部112 mode scope、far点/$\mu$词和成功矩阵身份；
- 全部新 `complete-unpaid-scope` 原行正文，以及每个生成ledger的原bytes/rows/SHA；
- binding-progress、完整当前地址、资源、错误、未返范围；
- 新完整geometry及每个数组身份，成功大点值/候选/factor正文只身份；
- 实际configure状态和公开provenance；
- 全部原mesh地址/后缀、FD各层、原末门、每native call原标量、末call细节及所有失败scope。

reader不重算科学数值。旧完整far的大streams由原sampler实际绑定，其成功正文不在这份必要返回中逐值重审。新solver成功也不代表闭面完成。

输出：`scalar-summary.json`、`necessary-readback-index.json`，以及仅完整scope+实际quiet时才有的 `readback-complete.json`。stdout frame为 `BEGIN_R456_FROZEN450_RESOLUTION_NECESSARY` / `END_R456_FROZEN450_RESOLUTION_NECESSARY`。step outputs仍为`resolution_summary`、`resolution_summary_bytes`、`resolution_summary_sha256`。

超过90000B返回70，不分包/编码；原read error或unknownquiet返回2，不写完成marker。若child已开始但result未返回，不凭缺件填scope。没有任何自动删除。外层caller仍必须结合origin/readback、第一A/B、原far、规则和当前quiet完成所有清理条件。

## 9. 新checkpoint后的五角色几何

入口：

```text
python geometry_20261116_current_C_same_far450_postsolve_geometry.py \
  --input ACTUAL_POSTSOLVE_INPUT --input-sha256 ACTUAL_SHA
```

input schema见第3节；`upstream_kind`为`R456-same-far-resolution450`，`upstream_launch_directory`指本new owner。需要原R448全部输入：

```text
namespace, upstream_launch_directory, upstream_result_sha256
job_deadline, job_deadline_sha256
geometry_directory
continuous_e_directory, continuous_e_result_sha256
computations, proof_directory, source_topic, out
first_shared_directory, first_shared_result_sha256
construction, resources, metric, reach, c_queries
```

`geometry_directory`必须是该真实新checkpoint绑定的新sampler目录；C必须是同一个完整实际cover/root对象，保四原小文件和现场原ledger/index。新的live-query角色继续消费R441绑定的R426，不把固定旧盒自动视为任意收紧。

`construction`只含`cut_correction_width`、`cap_height`、`fixed_cap`，其中完整markers列表显式给出。它必须逐有理整数/LE64词匹配actualfirst plan，含负零和列表顺序。新的atlas仍只用原当前C cuff，不换域外环。

`resources`包含`free_bytes_reserve`、`node_heap_mib`、`child_shutdown_reserve_seconds`和`stage_budgets_seconds`。后者恰含五个角色：`radial_replay`、`original_cuff_atlas`、`shared_field`、`metric`、`reach`。每个预算裁剪到同一原绝对截止，不重启科学钟。

`metric`恰含：`eta`、`interval_bits`、`sqrt_bits`、`initial_angular_depth`、`max_depth`、`max_visited_cells`。

`reach`恰含原12项：`curvature_upper`、`target_reach`、`active_depth`、`curvature_max_depth`、`pair_max_depth`、`interval_bits`、`sqrt_bits`、`max_cells`、`max_pair_nodes`、`max_pairs`、`cache_entries`、`max_constant_levels`；再加原block3项：`max_block_nodes`、`max_union_cells`、`block_cache_entries`。K/τ和所有门由原消费者真实执行，不由本来源组合选择。

`c_queries`恰含原11项：`precision_bits`、`integral_absolute_bits`、`integral_relative_bits`、`analytic_guard_bits`、`integral_evaluation_limit`、`value_width_bits`、`integral_max_depth`、`inverse_max_depth`、`max_panels`、`max_nodes`、`budget_seconds`。原合法资源范围保留。

五个科学CLI、数学参数、R441独立field/atlas/caps/四Loewner/闭DFS/block universe和wholephase合同均原样复用。真正新checkpoint会产生新的radial/shared/geometry结果。原父metric/reach证书不转用。reach不以metric成功为门；仅依实际前置radial/cuff/shared的完整性和quiet。

## 10. actual202205额外第一A/B来源

只有origin确为actual202205时，新postsolve要求输入`first_parameter_procedure`，其值恰是实际R452 `procedure.json` 的`{file,bytes,sha256}`。原193/203保既有first_shared合同，不要求新增来源；也不接收一个将被忽略的205字段。

注册的R452源：

- runner `geometry_20261116_actual202_ten450_parameter_block_postsolve.py`，`89a90b2d5d762510c228c5d3a4f6fe27a573c890b760268aecace2a44ab9e010`；
- policy `geometry_20261116_actual202_ten450_closed_parameter_policy.py`，`b49769f13f69bf30b82988b1ca57382c602d4b74bc3ae8a6c2b5d1e0ee3df7a8`。

`bind_first_parameter_source`实际读取该procedure及原input，并核其schema/source、`actual202205`、`initial-construction`、同launch/deadline、真实shared stage的`original_result`和原genuine checkpoint。随后读取`actual_selected_construction.outputs.first_construction_freeze`，核原policy、A、target canonical identity、全十词、完整construction words和首112材料定义。

若`actual_material_transport`存在，完整读取其`original_record`并核同source/A/clock/first checkpoint/target/词/`initial_capture`/`definition_capture_complete`。原大registration、normalization等不塞必要summary；只返真正读取的完整identity和范围。没有B则明确`actual_common_material_pullback_unpaid`，不把它或原metric/reach/held失败作新几何成功门。

本实现没有调用R447，也没有把首core的Φ换进当前场。当前Φ/SE2/R249由当前checkpoint重求。公开固定闭目标的共同材料解释仍沿R443条件；不把A/B的保存等同实际共轭或统一C²收敛。

## 11. postsolve必要读回与held

五角色reader：

```text
python root_20261116_current_C_same_far450_postsolve_necessary.py \
  --directory ACTUAL_POSTSOLVE_DIRECTORY --out FRESH_NECESSARY_JSON
```

保原完整block frontier、single-rank空间/相位stack、union待工、curvature和live-query未付/错误；已退ledger大正文仅原identity/address范围，不声称完整工具回传。增加实际A/B来源摘要。每份仍≤90000B，否则70；不清理。原step outputs保`postsolve_summary`、`postsolve_summary_bytes`、`postsolve_summary_sha256`、`postsolve_readback_complete`。

held调用：

```text
python geometry_20261116_current_C_same_far450_postsolve_held.py run \
  --input ACTUAL_HELD_INPUT --input-sha256 ACTUAL_SHA
python geometry_20261116_current_C_same_far450_postsolve_held.py readback \
  --directory ACTUAL_HELD_DIRECTORY --computations ACTUAL_COMPUTATIONS \
  --out FRESH_HELD_NECESSARY_JSON
```

held input恰含：`schema`、`postsolve_directory`、`postsolve_procedure_sha256`、`postsolve_input`、`postsolve_input_sha256`、`witness_plan`、`witness_plan_sha256`、`held`、`resources`、`out`。postsolve source/schema/input三元只认本冻结新post；不把不明新版本当原R448。

`held`恰含原8项：`active_depth`、`position_max_depth`、`position_radius_goal`、`interval_bits`、`sqrt_bits`、`max_position_cells`、`max_prefix_points`、`max_tail_witnesses`。`resources`恰含`held_budget_seconds`、`child_shutdown_reserve_seconds`、`free_bytes_reserve`。witness仍须实际当前场原plan；本文没有从首旧场复制一个点就称新场完成。

held仅依实际radial/cuff/shared来源，不依metric/reach通过。它再次用新post binder读取同一来源和绝对钟；实际R441 held数学源不变。其necessary全文保原必要范围、失败/当前/后缀，成功大记录只身份；单90KB，no cleanup，超限70。

## 12. 已复用数学源码与直接来源

本九源不复制新的native数学核。它们继续绑定：

| 原角色 | 完整SHA |
|---|---|
| full112 general Robin native | `fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349` |
| synchronous bridge | `67e3b23c9e5306764db3d6b8e0392eb8f59d4b63bfb671a0703fe33b2146c286` |
| complete general Robin QR | `946251656306a6cbe137513e12bac305c7758e5ec7306995a63314bd0f400bb5` |
| original capacity loader | `07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395` |
| joint numeric row representation | `24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97` |
| metadata lifecycle / OwnedChild | `84d0450f2f362138045c222f5a47162e030fd0be8b6c7a99c5d66c0e41da425a` |
| R441 checkpoint | `bf7dedd2135e3f6b54bc806a17064428111b502b6ddb8572ec66a883b1ce34ad` |
| R441 SavedPrefix | `fb6e181cd0ddfb34cc70c874c119ceb149850ce8756d1f2f0dd775175e99cffb` |
| R441 radial | `3d711d395693cdf8ad222e0838bb29b99ffb5043defb8a66c992dc854df018f4` |
| R441 shared | `1ceda9d32cfcf50e28e737cd0aee981cb8dc2329027aa2967d08532a1ea6e935` |
| R441 cuff atlas | `d0b03a367f3ece13b06949d5218a992e6ee3e9a41364499070d3f5f475a150a0` |
| R441 accurate cut | `8811f89c7395bb4aed1adabe6c6825c801e1e41a9d80d416b0a4746596ae9a52` |
| R441 caps | `ca53bdc5c0cdd5764065301f0edb1259d083fdffa9f3d767a5a38b4a7cafe364` |
| R441 live-query metric | `fd263af28a7d55a7246a49283d367e420786f48f16556dd5a7d61406b1c8459b` |
| R441 original reach | `745b245eddd27c10522012756a33bd842b3883d918845de49cc2cdacbeed1a05` |
| R441 block reach | `f27556bcfbeb72ac3ad7142bbc5089e1168fdc7966fe91757e1a201b7dbfe957` |
| R441 held/rigidity | `144da57a9d55547fa3b85ccb43c0f4261db2e2dcb41e91094c8d3a16c9b7d7b1` |
| R441 phase necessary API | `448c35c390abd78d169db8bad0c292d89b18cb0109fe5216420b5133479132bf` |
| original positive necessary | `34b49f026338b90b691cbd170d6d6303c7ec3549f2329ba0f4457a2cfeab75c9` |
| original joint necessary | `19878e48ed25dec8bdcbd36c3d7ea7168796a08fb60675ad7455dbb296a0918c` |

这些数学源继续各自读取原完整依赖，不能把上表当删减后的唯一运行闭包。真实配置的全部source map、原runtime pin、writer完整closure和每个下游consumer自身pin都必须可用。R441 radial实际按最终response checkpoint source唯一选择worker、按result source唯一选择sampler，因此新worker/newresult可真实接入；它不是固定导入旧worker后试图骗过schema。

原positive和joint legacy full453 utility分别为`ff66783d6491d56fd3b5b64f7be00849f744f08441811bf764608ae79619e248`、`c71d616936cf33e43965906c7cc99face01d06a12433420474b688b8d76b946d`。新driver只复用其完整runtime和原solver调用体，不改变其全局常量或冒其source执行新逻辑。

## 13. 仍待真实调用者完成

本包没有future request/run；完整workflow仍需真实来源的恢复、原2700秒规则同步、原namespace/硬限、step日志、所有独立必要读回以及全部quiet后清理条件。此处没有清理任何raw，原第一A/B、完整far、C/head/deep、父checkpoint和新临时结果必须留至依赖/读回全部完成。

同一准确target不等于同一有限离散程序，也不等于已经执行共同材料图。真实450、无限DN/共同C实现、最终metric/reach/held/δE、收敛与M路线仍按真实结果分别支付。本来源组合没有任何性能或终止保证；同far省去重复传播也不证明剩余时间足够。

## 14. 冻结身份与差异范围

以下运行源身份由当前实际文件字节生成。九个单源完整diff分别对应已发表R450或R448，均只作临时review材料；`publication-files.json`、builder和diff不提交为科学产物。实际发表仅九运行源、R456证明和本接口。全文差异不会被一个schema摘要代替。

| 运行源 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261116_current_C_same_far_registered_native_worker.mjs` | 18780 | `43ab8159593c240a68e399ab739c56c6681ac1cbf6b3cc0fae0f5309ef8a7e8c` |
| `geometry_20261116_current_C_same_far_registered_tail_client.py` | 23250 | `b778a3e15ec16a1f9f6cfcda2f75dc520a94a26d12fb50046e2dd5b22684fbd7` |
| `geometry_20261116_current_C_same_far_registered_resampling.py` | 50459 | `5f14be90b0e5ae36ee624ece930d46fa1205eee0efcc6e2a97decca15e7011d5` |
| `geometry_20261116_continuous_ten_frozen450_same_far_refinement.py` | 53190 | `9d76552d2a7b1dfc9e80ae9a3236fbb0d961007ca5052f702ffa6e18c3ac4a35` |
| `geometry_20261116_current_C_frozen450_same_far_owned_launch.py` | 58629 | `1a1df5136492abe5066a91139bd22554f8e83db21d13c981439532911f4b3c8d` |
| `geometry_20261116_current_C_same_far450_postsolve_geometry.py` | 65588 | `4770c16a51da7c384354c2999a8c97c76b7a8c315dbfedd304f7c9ff622614f2` |
| `geometry_20261116_current_C_same_far450_postsolve_held.py` | 43986 | `4f1e8a9d396a741934c50ebdf413f2d825ad99a53848e633881174899cf172e1` |
| `root_20261116_current_C_frozen450_same_far_necessary_readout.py` | 36696 | `59ed4273ca45c93931c6e6786adc87b4bd4fabf94f036e97e230a73687f7b596` |
| `root_20261116_current_C_same_far450_postsolve_necessary.py` | 27343 | `21e61e28c867cad82bff012f453f41a2c08d069669f470c6dc5d088b3ff14fd8` |
