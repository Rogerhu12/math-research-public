# R464 — 增量 M 同作业 owner、显式源码视图、几何与材料接口

作者：OpenAI ChatGPT（amplitude 子代理，AI）。日期：2026-11-16。

**状态：源码与来源组合已冻结；仅做源码文本、JSON、字节、哈希、完整差异和纸面分析。没有本地科学、项目模块导入、AST、编译、测试或 benchmark；没有创建 run、workflow、commit 或 ref。所有实际科学仅能在后续公开 Actions 内执行。** 条件证明见 [R464](../results/R464-incremental-M-owned-chain-and-explicit-source-view-composition.md)。

`publication-files.json`、`publication-sources.json`、`source-view-map.json`、各 `*.complete.diff` 和本地 `expanded-source-views/` 是交 root 的临时源代码清单/复核材料，不是科学 raw，也不需要另刊整份展开副本。本次拟发表只有七个独立源码、本接口与一篇条件结论。十五份完整视图由已发表基线和生成器的透明表在 Actions 产生；其源码身份公开，不冒旧文件标签。

## 1. 七个独立源码及冻结身份

路径均为 `topics/visible-flex-larger-amplitude/computations/` 下的 basename。

| role | basename | bytes | SHA256 | Git blob |
|---|---|---:|---|---|
| owner | geometry_20261116_current_C_incremental_M_owned_launch.py | 77960 | f372081797276ed3bc6c061f91febd97dfad70b742c34d10a9df5ae642a04078 | 9c44883dc7a536d0caaa70aa558986fefe29cf8a |
| reader | root_20261116_current_C_incremental_M_necessary_readout.py | 33447 | 602c9abd38a3fa7a7fc590a964139a4f4bf8186403da208583e4472d712bae8e | 812327dbc99948ca613f53cae23252a740f64d71 |
| material | geometry_20261116_current_C_incremental_M_common_material_phase.py | 38717 | 50bf2d04e5e4e505fad6f0ece5a896364bb94c25c9530d6a1e7c2ceef3aec923 | dfea5408a13f7efe02f4cf8c34b5084ded83a315 |
| post | geometry_20261116_current_C_incremental_M_postsolve_geometry.py | 71729 | 480ed1ebc76e00bef781c309946773a5e03b3cea6fa9f000c81c462849c72563 | 549d1b3e3944b1a8d175a28ef5af4643925f83e9 |
| postreader | root_20261116_current_C_incremental_M_postsolve_necessary.py | 27287 | 5d7bc6bfc7b057458a4b998f55d4bdd5592fb11d1cd10d50a76d33a350d39313 | 309440252b522800e13c12086f4b960e3f6a9f85 |
| held | geometry_20261116_current_C_incremental_M_postsolve_held.py | 44030 | 07876025cad4b3548eb4593431f609db95a4c288b6d0a37dcfeeec24fb986951 | 53e8b4af37828e7d201da5988489d5adf0b414e1 |
| generator | geometry_20261116_incremental_M_source_views.py | 42983 | 68ae7071a4e41beedc1dbaea65f14f60e5e0fe0793a1b7f2daaacfd73f9b7bf7 | 935569a5a0a0fe19de18b0103aa546d49d68b418 |

条件证明的当前身份：15635 B / SHA256 `ae50023b7c29dc0f94afb8c34eecebddec1ae81684b80109b9b1b05a07f21b58`。接口本身的最终身份由 publication manifest 给出，不在自身正文循环嵌入。

原 R463 两件保持已发表字节：

| 角色 | basename | bytes | SHA256 |
|---|---|---:|---|
| driver | geometry_20261116_continuous_ten_incremental_M_refinement.py | 51265 | cf86639189e98e7fe5c99f6dfba566fac6dbfd3b142c17ea8b22df6bb039ce28 |
| checkpoint | geometry_20261116_continuous_ten_incremental_M_checkpoint.py | 55236 | 7545962063692edc34bbbce9893b038a9f408383208f72ad28a5608440781e39 |

原 R462 三件保持已发表字节：

| 角色 | basename | bytes | SHA256 |
|---|---|---:|---|
| union | geometry_20261116_current_C_incremental_M_far_union.py | 52848 | 5da13c5f94c59be9f002f906a373d5320ed64d0ac0254af1746a1e5c8ce13c46 |
| worker | geometry_20261116_current_C_incremental_M_native_worker.mjs | 18663 | b536850a32fb8c26f7bc7a06483a4d3823662ea2fd2a9235e77dbdca069b6b08 |
| client | geometry_20261116_current_C_incremental_M_tail_client.py | 23746 | d9db5098b8dbf8ebabb83fb25c060faaa0acf28dd9075654b550bdf07ac5a710 |

完整 source closure 沿各真实 `PINS`/`SOURCE_PINS` 与 R463 原递归 loader；不能仅下载这十二个可见 basename 就声称所有 runtime 已齐。原 R457、R442、R451、R456、R437/R452、原 78 源及真正 C/runtime 来源按实际调用保留。没有删除旧 pin 换成新同名 pin。

## 2. 十五份有自己身份的源码视图

下面全部是**新 basename**，不是待覆盖的旧文件。生成器包含每份完整基线 basename/bytes/SHA、所有有序字面替换及精确出现次数、新 bytes/SHA。完整替换表就是公开生成源码的正文；`source-view-map.json` 是同表的交接形式。

| role | 新 basename | bytes | 新 SHA256 |
|---|---|---:|---|
| saved | geometry_20261116_continuous_ten_incremental_M_saved_prefix.py | 19270 | 959b1a2b54fd0da8be14c2228d91ca1d1ef312966d6f4ba40be4bbeff4247ce9 |
| radial | geometry_20261116_current_C_incremental_M_radial_readout.mjs | 24141 | 513494eb4569905d45e02326e388fec65e2e42b211ce8e30de31522618295bb9 |
| shared | geometry_20261116_current_C_incremental_M_shared_field.py | 49511 | 55a1fb95b574651bac6458034b5f85c46180172189d7a8010758e786087a4c04 |
| prefix | geometry_20261116_continuous_ten_incremental_M_prefix_metric.py | 32810 | fd74b6ad9dc1b6069b016dd7fce14e0c35215bc76b045682172e3e10522a7402 |
| atlas | geometry_20261116_current_C_incremental_M_original_cuff_atlas.py | 29440 | 14f79dcc67488e9bda3c654ca308a59c3d8142eaaf6d350cc3c9277f8bc7b2e5 |
| cut | geometry_20261116_current_C_incremental_M_accurate_cut_patch.py | 26131 | 8105c8148d221b5ba10bc332631c88764d620dc59d30936bbe1067b6a54228e2 |
| caps | geometry_20261116_current_C_incremental_M_fixed_cap_balls.py | 23668 | 3f43b4bf5e3d4e3134904a772abbf36483e1470174a1df9a3657edf03fbfe811 |
| metric | geometry_20261116_current_C_incremental_M_live_query_complete_metric.py | 55099 | 2592d09e9dc471679d4e6d8588a409c3a180132b3b478fc47fbeb1a9d91886f8 |
| reach | geometry_20261116_current_C_incremental_M_complete_reach_cover.py | 60498 | 710719dca6ff474c3c73f378b9bba04fad3c5621c86487147d4fe715a47f6f61 |
| block | geometry_20261116_current_C_incremental_M_complete_block_reach_cover.py | 45633 | afa18a5d303806e1a644186ce326644110f0e6a262b878d988b07b5712606ebe |
| heldconsumer | geometry_20261116_current_C_incremental_M_held_and_rigidity_inputs.py | 53822 | 6d3e56b2f8ab636d03d829c7d9bd244cfd7bbf1db0e4cdda6c9329b064440cba |
| nativeapi | root_20261116_current_C_incremental_M_native_necessary_api.py | 52328 | 4f1c2861a63ba50b6cc6bf3eed4ab2cc1b5fc0a3b7c7de6197b00fd0a810fdf4 |
| phaseapi | root_20261116_continuous_ten_incremental_M_phase_readout.py | 19706 | dfda82d609716948994fae95089e8915027a1b0bb1ea59eb1290c213ec9480e6 |
| evidence | geometry_20261116_incremental_M_fixed_target_metric_evidence.py | 62333 | 0eb5d8171664db099824698a8319e91a0324344b8d915032ebab932c29707f2b |
| display | geometry_20261116_current_C_incremental_M_multitime_display.py | 41727 | e0b47bbfd355032bb433302425d09a4e6be0413107e20ac3d96e7c52586e88cf |

前十一份原科学函数、数值式、循环与接受门保持原源，改变实际 CP/loader/source/schema 绑定及必要说明；native API/phase API 另加 union metadata 来源；最后 evidence/display 只加实际新 family 和材料来源，旧 family 保留。它们仍是新源码身份，不声称原 source byte 相同。

生成器按依赖顺序形成 SavedPrefix→radial/shared→prefix/atlas→cut/caps→metric/reach/held 及必要 API、evidence/display。实际科学执行时，各模块按自己的精确依赖 pin 再加载真实文件；生成器不执行这些模块。

### 2.1 两阶段来源绑定顺序

后续 outer 必须：先核已发表生成器及完整旧基线/published sources；在真实 computations 创建新视图；然后核全部生成全文身份；最后才启动会 import 它们的 owner/post/readers/evidence/display。不能在尚未生成前将十五份 view 当作 Git 已下载源核收，也不能绕开它们真实新身份。

```bash
python -u "$COMP/geometry_20261116_incremental_M_source_views.py" \
  --computations "$COMP" \
  --out "$NS/source-views"
```

这里 `COMP` 必须是生成器真实所在目录、R463 driver 的 `HERE`，也是 cfg.computations、profile/CP 和下游 loader 的实际 code_directory。源视图不写到另一个目录后仍标旧 computations。`NS/source-views` 是 RUNNER_TEMP 内的新鲜独占**收据**目录，与代码目录分开。

每个新源码目标事先须不存在；生成器全部只读核收完成后才 `xb` 写。已有目标明确失败，不覆盖旧源，不把先前生成结果悄然当缓存。实际 partial 文件不删除、不重新贴身份；结果记录 `current_target` 和 `unconfirmed_view_roles`，未知写回状态不冒“完全未写”。

输出 `source-view-result.json`，schema `R464-incremental-M-explicit-source-views-v1`；含同 run/source、actual computations、原 sources、每份生成身份、全部未确认后缀、error。stdout 用 `BEGIN_R464_SOURCE_VIEW_RESULT` / `END_R464_SOURCE_VIEW_RESULT`。0 表示来源生成完成，2 表示工程错误，70 表示单份来源报告超 90000 字节；这些都不是科学接受。没有原 raw 读取或编码。

## 3. owned launcher 的准确输入

```bash
python -u "$COMP/geometry_20261116_current_C_incremental_M_owned_launch.py" \
  --input "$NS/incremental-M-input.json" \
  --input-sha256 "$ACTUAL_INPUT_SHA"
```

输入 schema `R464-current-C-incremental-M-owned-launch-v1-input-v1`。下列是字段合同，不是预填实际 run 的 recipe：

| 字段 | 实际来源/含义 |
|---|---|
| namespace | 本新作业实际 RUNNER_TEMP 独占 namespace |
| origin_launch_directory | original193、joint203 或 actual202205 的本作业真实 origin result 目录 |
| parent_launch_directory | origin 本身，或真实 R431/R441/R456/旧 R442/R457/本 R464 accepted owner 目录 |
| job_deadline / job_deadline_sha256 | origin 真正消费的同一原 deadline；逐 bytes/SHA 核同 |
| computations | 同生成器/R463 HERE 的真实完整源码目录 |
| accepted / accepted_sha256 | origin 真正消费的原构造输入，不是旧 accepted 数值状态的偷换 |
| tail_config / tail_config_sha256 | origin 的**原 112 配置**；不能传当前 M 父配置替代 |
| tail_source_root | origin command 的真实 `--tail-source-root` |
| field_modes | 整数 M>112 且严格大于实际 parent.M |
| max_nodes | 显式原初猜完整节点容量，至少 2；不是删除父节点的许可 |
| refinement_factors | 恰四键，见下一节 |
| deep | 恰十字段，原 C/deep 输入和显式精度 |
| sampling | 原 cover/far/sampling 实件、两 proof、显式十四工作参数 |
| resources | 恰六资源字段，均为原钟内上限 |
| out | namespace 内新鲜 sibling，不能包含 origin/parent/input 或重用旧输出 |

四因子恰为 `field_and_native_angles`、`native_steps`、`material_angles`、`physical_angles`，均整数且至少 1。owner 先读取真实 parent 的 N/native quadrature/steps/material/physical，再乘因子。M128 接 R456×2 后 factor=1 的含义是保留 R456 的真实加密值，不是取旧原 112 的数值。

### 3.1 deep 十字段

`config`、`config_sha256`、`ledger_ready`、`ledger_ready_sha256`、`stored_ready`、`stored_ready_sha256`、`proof`、`tail_proof`、`mode_extension_proof`、`precision_bits`。

前三件来自原完整 C 输入，分别匹配 config/calibration_ledger/stored_reference；proof 与 tail_proof 匹配真实原 C/deep 记录；mode_extension_proof 是原 R442 有限 M 条件结论。precision_bits 使用原支持范围 128…8192。owner 仍真实产生**全部**新 M deep，不把原 112 deep 填成全 M。

### 3.2 sampling 字段

路径/身份字段：`cover_directory`、`cover_result_sha256`、`original_far_directory`、`original_far_result_sha256`、`original_sampling_directory`、`original_sampling_result_sha256`、`proof`、`unit_row_proof`。

`parameters` 恰十四键：

```text
precision_bits
linear_budget_seconds
sampling_budget_seconds
max_panels
free_bytes_reserve
max_depth
local_defect_bits
panel_norm_limit
taylor_terms
max_geometry_cache_records
sample_max_nodes
sample_inverse_depth
sample_value_bits
representative_max_precision_bits
```

这些是实际新工作的参数，不能只因和旧来源名称相同就宣称旧精度策略逐值相等。`steps` 不在此字典里；它由真实 parent resolution 和显式 native_steps 因子产生，避免重复 `--steps`。`budget_seconds` 也不在十四键中；它来自该角色声明资源上限并受原绝对钟裁剪。

R462 sample 收实际新 deep 的 `--far-directory/--far-result-sha256`，同时收原 `--original-far-*`、`--original-sampling-*`、原 family（original193 为 positive，203/205 为 joint）、真实 origin/deadline、M、actual steps 和全十四工作参数。结果仍保 R462 自己的 schema/source，不改标签。

### 3.3 resources 六字段和总钟

`deep_process_budget_seconds`、`sampling_process_budget_seconds`、`refinement_process_budget_seconds`、`child_shutdown_reserve_seconds` 为正有限数；`minimum_free_bytes_at_start`、`free_bytes_resource_stop` 为正整数，后者小于前者。

每子过程在原实际 `namespace_created_unix_seconds+18900` 截止内裁剪，原 2700 readback reserve 不成为新增 science。configure 从 sampling 上限减实际已用耗时取得剩余；不是额外一整份采样预算。所有 cap 是上限，不作完成承诺。未分配 M=128 或某时长的默认实际请求；这些由后续显式 outer recipe 选定。

## 4. R463 的真实调用与来源登记

owner 顺序运行 `deep`、`sampling`、`union-configuration`、`refinement` 四个实际子过程。第三个调用原 R462 `configure`，其 CLI：

```bash
python -u "$COMP/geometry_20261116_current_C_incremental_M_far_union.py" configure \
  --directory "$ACTUAL_UNION_DIRECTORY" --result-sha256 "$ACTUAL_UNION_SHA" \
  --original-config "$ACTUAL_ORIGINAL112_CONFIG" \
  --original-config-sha256 "$ACTUAL_ORIGINAL112_CONFIG_SHA" \
  --computations "$COMP" --quadrature "$ACTUAL_NEW_NATIVE_QUADRATURE" \
  --out "$OUT/actual-R462-configure-configuration.json"
```

该文件原字节保留。新文件 `actual-refined-native-config.json` 从其真实内容复制，仅在 `modes` 存在时改为新 M，并增加 `R464_incremental_M_owner_origin` 恰六真实收据/对象：

```text
actual_parent_checkpoint
original112_config
actual_R462_configure_configuration
actual_new_M_deep_result
actual_union_sampling_result
actual_resolution
```

没有凭 SHA 恢复不存在的原配置。原配置正文的读取属于实际 configure 和本 owner；R463 根据真正 receipts 和 union 数据核来源，不额外声称自己再次读了没有绝对路径的旧 descriptor。原 R462_actual_union_origin 完整保留。

最后调用真实 R463 driver：`--recipe/--recipe-sha256` 为新 `actual-resolution-recipe.json`，`--parent-directory/--parent-manifest-sha256` 为真实 parent CP，`--tail-config/--tail-config-sha256` 为上述实际新配置，`--tail-client` 为原 R462 d9db client。原 `--jac-workers 2 --node-heap 6144`、原完整 phase 流程和原最终门保持。

新 R463 recipe schema `R463-explicit-current-C-ten-incremental-M-refinement-v1`；operation `same-job-genuine-incremental-M-fresh-original-solve`；driver schema `R463-current-C-continuous-ten-incremental-M-original-full-DN-v1`；CP schema `R463-current-continuous-ten-incremental-M-physical-DN-checkpoint-v1`。原 profile 的 R442 schema/cc70 来源是实际未改 profile，不能一并替换成假 R464 profile。

完整 recipe 保 k=0、physical=3M+2、state=4M+2、全部 M far、全部原 native/current H/FD/fullDN/末 J/audit。原八轮/十七档/1e−6/1e−11/5e−5 与 576 stages 不变。新增 M 与分辨率是明确新求解问题，不是已被旧接受支付的状态。

## 5. owner 输出和允许读取的阶段

owner 主输出 `$OUT/result.json`，schema `R464-current-C-incremental-M-owned-launch-v1`。重要真实字段：`actual_parent_checkpoint`、`actual_parent_checkpoint_directory`、`actual_resolution`、`actual_deep_result`、`actual_sampling_result`、`actual_union_input_binding`、`actual_R462_configure_configuration`、`actual_new_native_configuration`、`actual_adapter_status`、`actual_refined_checkpoint`、`actual_refined_checkpoint_directory`、`current_refined_M_accepted`、`owned_group_quiescent_before_readback`、`resource_stop`、`external_interruption`、`error`。

实际子目录：`complete-M-deep/`、`native-sampling/`、`refined-BVP/`、`banded-work/`；真实 driver 状态为 `refined-BVP/adapter-status.json`，完整 phase 在 `refined-BVP/refined-M/`。最终 CP 路径只从实际状态的 `actual_final_checkpoint_directory` 与 receipt 取得，不能根据期待成功拼造。

`actual_BVP_child_started` 只反映 refinement 子过程，不包括前面真实 deep/far/configure；`stage_started=false` 也不自动表示 seed/preflight 无求值。原返回码、资源124、外部信号及每个未启动后缀按实际输出，不能以 workflow SUCCESS 代数学接受。

## 6. 单份 owned 必要读回

```bash
python -u "$COMP/root_20261116_current_C_incremental_M_necessary_readout.py" \
  --namespace "$NS" --launch-directory "$OUT" --computations "$COMP" \
  --out "$NS/M-necessary" \
  --entry-stdout "$ACTUAL_OWNER_STDOUT" --entry-stderr "$ACTUAL_OWNER_STDERR"
```

最后两个 entry log 参数可省略。必须实际 quiet 后才读取可能变化的 science tree；reader 自己再次观测所有已登记 child 及嵌套 owner。unknown/live 保现场，必要结论写未读，不造某阶段数学结果。

schema `R464-current-C-incremental-M-one-necessary-readback-v1`，frame `BEGIN_R464_INCREMENTAL_M_NECESSARY` / `END_R464_INCREMENTAL_M_NECESSARY`，正文输出 `scalar-summary.json`，并保 `necessary-readback-index.json`。完成时才写 `readback-complete.json`。

union 通过原 R462 `readback` 的标准库路径选择：新 reader 不调用旧 full-M `sampler_view` 来解释它。原 R462 必要正文临时写在 `actual-union-necessary/summary.json`，stdout 在 `actual-union-necessary-local-stdout.log`，暂移并恢复 GITHUB_OUTPUT，使其完整正文只纳入外层一次。实际 R462 原 error/未付/行计数/identity scope 保留；没有 sample/configure/科学 evaluator 调用。

一般字符串沿原 `short(...,1800)` 的 UTF8 字节限制；日志匹配 literal traceback/error/signal/storage 文本，仅返首二/末一匹配行，每行 `short(...,1200)` 并附原行和整文件身份；一般长度>16列表用原 identity 摘录。FD 走原专用逐方向/逐层字段选择，不受该泛用列表规则删成十六条。早期 native 成功大 trial、完整状态/J/factor/区间表通常仅 identity，末真实 native/所有失败 scope 按原规则选择，不宣称全部原文逐值已返回。

完整必要正文>90000B 时返回70，保原正文bytes/SHA、section sizes、errors count、quiet和未写完成标记的事实；不增上限、不拆包、不编码raw、不把最终science flag改写为运输成功。当前 source-only 没有实测任何未来输出大小。

## 7. 新场五阶段 postsolve

```bash
python -u "$COMP/geometry_20261116_current_C_incremental_M_postsolve_geometry.py" \
  --input "$NS/M-postsolve-input.json" --input-sha256 "$ACTUAL_POST_INPUT_SHA"
```

input schema `R464-current-C-incremental-M-live-query-block-geometry-v1-input-v1`，`upstream_kind` 必须是 **`R464-incremental-M`**。`upstream_launch_directory` 是本 owner 的实际输出；它的 `actual_refined_checkpoint/directory` 必须对应真正 R463 driver 的 `actual_final_checkpoint/directory`。

其余路径/身份：`namespace`、`job_deadline`、`job_deadline_sha256`、`geometry_directory`、`continuous_e_directory`、`continuous_e_result_sha256`、`computations`、`proof_directory`、`source_topic`、`first_shared_directory`、`first_shared_result_sha256`、`out`。`geometry_directory` 来自当前真实 R462 sampling，不是原 112 geometry；完整 C 四件与 source-panel/index 保留到 live metric 结束。

实际 origin 为205时，还必填 `first_parameter_procedure={file,bytes,sha256}`，指真正 R452 首次程序的 `procedure.json`。程序读取该原输入/上游/原钟、真实 first shared stage、first CP、A 和可有 B；不是自行重选 W/H/markers。旧193/203分支保持旧来源合同，不接一个会被忽略的205字段。

`construction` 恰三键：`cut_correction_width`、`cap_height`、`fixed_cap`（含完整 `markers` 列表及原顺序、upper/center/radius/height 原词）。必须等真实 first shared plan 与 A；不得按新 M 解重新选 H。B 缺失记材料责任未付，不是几何/held或 BVP 的新增通过门。

`resources` 必须显式含 `free_bytes_reserve`、`node_heap_mib`、`child_shutdown_reserve_seconds`、`stage_budgets_seconds`；后者恰五键：`radial_replay`、`original_cuff_atlas`、`shared_field`、`metric`、`reach`。全部由同一原 deadline 剩余时间裁剪。

`metric` 恰六参数：`eta`、`interval_bits`、`sqrt_bits`、`initial_angular_depth`、`max_depth`、`max_visited_cells`。`eta` 保原准确有理字符串。

`c_queries` 恰十一参数：`precision_bits`、`integral_absolute_bits`、`integral_relative_bits`、`analytic_guard_bits`、`integral_evaluation_limit`、`value_width_bits`、`integral_max_depth`、`inverse_max_depth`、`max_panels`、`max_nodes`、`budget_seconds`。全部沿原 R426支持范围，不新增 query 审核门；失败精化保原已证粗界。

`reach` 恰十五参数：`curvature_upper`、`target_reach`、`active_depth`、`curvature_max_depth`、`pair_max_depth`、`interval_bits`、`sqrt_bits`、`max_cells`、`max_pair_nodes`、`max_pairs`、`cache_entries`、`max_constant_levels`、`max_block_nodes`、`max_union_cells`、`block_cache_entries`。前两个保持准确有理字符串；原完整 AA/CC/AC 与 block/leaf 数学照旧。没有预填 K、tau 或比例已达结论。

主输出 `procedure.json`，schema `R464-current-C-incremental-M-live-query-block-geometry-v1`；每个 stage 的实际输出 schema 对应上面的生成视图。`stages[*].original_result` 与 `inputs` 保真实返回；`unstarted_stage_names`、资源、原错误与 quiet 保全部实际范围。reach 独立于 metric 成功。五阶段结束仍明确 held 未执行；held须后续独立调用。

必要读回：

```bash
python -u "$COMP/root_20261116_current_C_incremental_M_postsolve_necessary.py" \
  --directory "$ACTUAL_POST_DIRECTORY" --out "$NS/M-postsolve-necessary.json"
```

schema `R464-current-C-incremental-M-postsolve-necessary-readback-v1`，frame `BEGIN_R464_INCREMENTAL_M_POSTSOLVE_NECESSARY` / `END_R464_INCREMENTAL_M_POSTSOLVE_NECESSARY`。单90K，保原失败/未访和必要 scope，未知/超限不给 cleanup 条件。

## 8. 独立 held：只接匹配的新 R464 场

```bash
python -u "$COMP/geometry_20261116_current_C_incremental_M_postsolve_held.py" run \
  --input "$NS/M-held-input.json" --input-sha256 "$ACTUAL_HELD_INPUT_SHA"
python -u "$COMP/geometry_20261116_current_C_incremental_M_postsolve_held.py" readback \
  --directory "$ACTUAL_HELD_DIRECTORY" --computations "$COMP" \
  --out "$NS/M-held-necessary.json"
```

runtime schema `R464-current-C-incremental-M-held-after-shared-v1`；input 加 `-input-v1`，necessary 加 `-necessary-v1`。必要 frame `BEGIN_R464_INCREMENTAL_M_HELD_NECESSARY` / `END_R464_INCREMENTAL_M_HELD_NECESSARY`，event `R464_held_necessary_readback_identity`。

input 恰 `schema, postsolve_directory, postsolve_procedure_sha256, postsolve_input, postsolve_input_sha256, witness_plan, witness_plan_sha256, held, resources, out`。post 的source/schema/input三件必须是真正新 R464 tuple；不接受旧 R451 post 后又硬用新 shared/cut consumer。原旧wrapper全部保留在旧来源。

`held` 恰八键：`active_depth, position_max_depth, position_radius_goal, interval_bits, sqrt_bits, max_position_cells, max_prefix_points, max_tail_witnesses`，其中position_radius_goal保有理字符串；resources恰 `held_budget_seconds, child_shutdown_reserve_seconds, free_bytes_reserve`。witness_plan必须是真实同场计划/实际字节SHA，不预设四点一定给正距离。

完整全像、反射、两帽和 marker 以及非平面输入仍由原科学consumer真付；metric/reach不通过不阻本独立held。单必要90KB；没有raw分包/上传/删除。

## 9. 公共材料、新 evidence 与显示的 family 映射

公共材料源 schema `R464-current-C-incremental-M-common-material-phase-v1`；真实 API 保 `bind_loaded_common_material`、`evaluate_active_cell(index, radial, angular, (t,t), lower, interval_bits=..., max_inverse_steps=...)`、`encode_active_cell`。新增键 **`R464-incremental-M`**；全部旧 family 仍按其原真实 tuple解释。

| level 的真实来源 | evidence view 的 family | display view 的 family | 公共材料 family |
|---|---|---|---|
| 首原112准确场 | original112 | current112 | R416-original-resolution |
| R456真实112加密场 | resolution112 | resolution112 | R441-current-resolution |
| 原完整M场 | completeM | completeM | R451-current-M |
| 真R463增量M场 | incrementalM | incrementalM | R464-incremental-M |

每行的实际cut/shared/checkpoint仍由代码表精确绑定；family只是选择显式已注册来源，不是改数据schema。首B仍R437或R452真实完整112记录；不造首M材料record。

evidence CLI沿原 R459不变，自己的新schema为 `R464-same-accurate-closed-target-incremental-M-metric-evidence-v1`。未来联合序列的所有level和compare统一用这个view，旧三个family可直接使用，不能混合旧R459 schema记录作新compare。它仍实际消费公共目标、全域误差与真实t网格，不把相同eta的两个pass当作改善证据。

display CLI沿原 R461不变，自己的新schema为 `R464-current-accurate-incremental-M-multitime-display-v1`。physical-angle-image是同图像的有限显示抽样；不需要B但不声明固定首q顶点对应。first-material模式要真实B和原准确逆/完整lift接口。默认或outer选定的多个t、所有网格/precision/max_inverse/budget都要显式记录；本接口不把geometry准备的某一3/5/9显示计划预写为本源已执行。

显示逐顶点原区间与最终投影误差仍在必要读回；没有把其半径当连续面内误差或BVP误差。每压缩/未压缩文件原<5MB，临时到读回/quiet后清，不Git存raw。未访frame/vertex保原后缀。evidence/display均不隐含在post五阶段，outer需独立真实调用。

## 10. 生命周期、资源和只读边界

原 owner PID/PGID/SID/startticks、独立nested sessions、原关停/reap和实际quiet保留。所有输入/输出限制在真正namespace和source目录，已有结果不重写；unknown不当静止。本组件没有清理函数代outer删science。

原 C 的 `result.json, input-binding.json, query-plan.json, query-results.json, large-arrays/complete-source-radial-panels.jsonl, large-arrays/source-piece-index.json` 必须实际留到live metric消费结束。原112完整far/sampling/raw必须留到R462真正union消费与必要读回结束。当前和首次CP、radial/shared/A/B必须留到实际geometry/material/evidence/display/held结束；有SHA不代表删后仍可消费。

outer只在原完整读回与所有本轮必要读回成功、全部owner真的quiet后清理本作业自有raw。各resource cap不相加成新钟。工程返回70与科学原返回/资源/异常分别保存；任何tuple/source/bytes不符是来源错误，不编写数学拒绝。

## 11. 完整差异和出版范围

| role | 完整基线 | 完整 diff bytes | diff SHA256 |
|---|---|---:|---|
| owner | geometry_20261116_current_C_actual202_frozen_M_owned_launch.py | 40774 | 39e100277047a08ec7828e915a65821cf15f6c95cd135ec1ab3223255f1ea155 |
| reader | root_20261116_current_C_actual202_frozen_M_necessary_readout.py | 11086 | f2085a3fc31433dc9c2765298b35c7a0da0e4dff52a5ddfc078538d704f953e3 |
| material | geometry_20261116_current_C_actual202_M_common_material_phase.py | 1853 | 2d0fafe210c634df880cf6890856a3eae22b788f514cf8b454fa709f0db4898e |
| post | geometry_20261116_current_C_actual202_M_postsolve_geometry.py | 12901 | 685f599146460d185d5501d4b8e3e3abf8816b1cf963821b87914f2ced9acebc |
| postreader | root_20261116_current_C_actual202_M_postsolve_necessary.py | 3281 | 6a9b9379e642eb1bf867b9a9eff1e1eebdbbad4b9516b0de3d2e3c085a0072e3 |
| held | geometry_20261116_current_C_actual202_M_postsolve_held.py | 8070 | 714bad04eb0c13d033b2cd5cda62ec963657f42e434851a4309760ce6b9db058 |
| generator | /dev/null（新增生成器） | 43712 | 3009784bc88b102d0083008760ac6ae64c85c37e1b97f8d37fac96e8d973512c |

七源complete diff中，generator是独立新增完整源码；其15份视图的完整baseline diffs也提供在 `expanded-source-views/`。`final-current-labels.delta.diff` 单独说明最终当前R463/R464事件/文字及级联identity，与全部baseline diff一致。新held移除实际错配旧R451tuple是来源选择修复，未改held数学。

原R442/R457 owner、原R451科学源、原R463/R462和原193/203/205运行源均未改。当前没有新的accepted父参数、科学结果或性能结论；后续入口不能以本条件证明冒原运行已完成。Root独占发表/refs/request/dispatch，任何真实run另行绑定并按唯一责任完整必要读回。
