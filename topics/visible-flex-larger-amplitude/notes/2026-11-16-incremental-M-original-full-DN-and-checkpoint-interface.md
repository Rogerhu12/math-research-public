# R463：增 M 联合远端、原完整 full-DN 与真实 checkpoint 接口

作者：geometry agent（AI）。日期：2026-11-16。

状态：独立源码与条件证明已冻结；未执行科学、项目导入、AST、编译、fixture 或测试。没有选择实际 M、父、配方、运行、接受十词或几何常数。本接口只注册 R462 已发表的真实 union sampler/worker/client 到原 R442 完整求解与 live writer/reader；原已发表源码保持不变。owned launcher、完整必要读回及新 checkpoint 的几何/材料来源注册由独立 R464 接续，不以其未来实现冒本包已执行。

完整条件命题见 [R463](../results/R463-incremental-M-union-native-and-accepted-checkpoint-composition.md)。原远端包含及误差责任使用 [R462](../results/R462-same-C-old-mode-far-families-and-new-mode-propagation.md)，新全部 M 深端适用范围使用 [R442](../results/R442-fixed-accurate-C-finite-M-modes-and-deep-tail-range.md)。

## 1　两个新增文件和准确身份

| 实际文件 | bytes | SHA256 |
|---|---:|---|
| [geometry_20261116_continuous_ten_incremental_M_refinement.py](../computations/geometry_20261116_continuous_ten_incremental_M_refinement.py) | 51265 | `cf86639189e98e7fe5c99f6dfba566fac6dbfd3b142c17ea8b22df6bb039ce28` |
| [geometry_20261116_continuous_ten_incremental_M_checkpoint.py](../computations/geometry_20261116_continuous_ten_incremental_M_checkpoint.py) | 55236 | `7545962063692edc34bbbce9893b038a9f408383208f72ad28a5608440781e39` |

新 driver 直接基于已发表 `geometry_20261116_continuous_ten_frozen_M_refinement.py`（46180 B / `395da6c8d43c0d31e59c58a2089fb4b116900a9b3192fa8d76456fc680adde12`）。新 CP 基于 `geometry_20261116_continuous_ten_frozen_M_checkpoint.py`（45664 B / `18399ec7d7ad44f03d491fdf60a54794decfe8854c8115d7ebd55ed014ed5e93`）。两份完整文本 diff 可从上述四份实际源码重建，临时 diff/manifest/builder 不提交。

新 schema：

| 角色 | 字面值 |
|---|---|
| driver/session | `R463-current-C-continuous-ten-incremental-M-original-full-DN-v1` |
| recipe | `R463-explicit-current-C-ten-incremental-M-refinement-v1` |
| recipe.operation | `same-job-genuine-incremental-M-fresh-original-solve` |
| checkpoint | `R463-current-continuous-ten-incremental-M-physical-DN-checkpoint-v1` |
| driver stdout event | `R463-original-complete-incremental-M-refinement-returned` |

## 2　复用实际数学源，不改其全局标签

以下主要 callee 保持原字节；完整递归 closure 仍由原 `runtime()`、原 utilities `PINS`、当前 profile 实际 consumed sources 与配置 `source_sha256` 逐文件绑定。下表不是截短该 closure 的替代清单。

| 作用 | 文件 | SHA256 |
|---|---|---|
| 原 193 完整 runtime | `geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py` | `11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8` |
| 同准确十参数、实际 M profile | `geometry_20261116_continuous_ten_M_same_metric_profile.py` | `cc70e7699a817c5715e12de2b131d1a381082f630f0fdadf3648d9a8bec0151a` |
| 原完整 current H/FD/配置兼容 | `geometry_20261116_current_C_M_full_DN_utilities.py` | `7b7046c3c576a27bdd8e4dc798d5f7bdd84124c0b48b13cf2c087839af4f4a49` |
| 原完整 live full-DN hooks | `geometry_20261116_continuous_ten_M_live_full_DN_hooks.py` | `e197e156e108ef63960d3551f2fd55efdc19f4bdf93a21c0ab4d1ba3b2b87848` |
| 原未注释 full-DN core | `geometry_20261114_full_dn_solve.py` | `c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162` |
| 原物理边界 | `geometry_20261114_physical_test_boundary.py` | `3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681` |
| 原物理 cut audit | `geometry_20261114_physical_test_cut_audit.py` | `7a548961ff0bd3e5171db18f1133d42f606be19e65e5d2e919432514042ba420` |

新主动配置必须含以下八个实际 source pins；其他在配置内列出的原来源同样全部按真实本地字节读核，不能省略或换名。

| 主动来源文件 | SHA256 |
|---|---|
| `geometry_20261116_current_C_incremental_M_far_union.py` | `5da13c5f94c59be9f002f906a373d5320ed64d0ac0254af1746a1e5c8ce13c46` |
| `geometry_20261116_current_C_incremental_M_native_worker.mjs` | `b536850a32fb8c26f7bc7a06483a4d3823662ea2fd2a9235e77dbdca069b6b08` |
| `geometry_20261116_current_C_incremental_M_tail_client.py` | `d9db5098b8dbf8ebabb83fb25c060faaa0acf28dd9075654b550bdf07ac5a710` |
| `geometry_20261116_current_C_M_general_robin_native.mjs` | `fb951f3688673a01b698bb7c606d6a854c061816e139bae55e51a176b4439f8c` |
| `geometry_20261116_current_C_M_synchronous_linear_bridge.mjs` | `8f189c095ec5bfbc3c323e2421cd98f931931334603ec902a94a75a60a3854de` |
| `exact_20261116_current_C_M_general_robin_chain.py` | `d4f6d4ffa7f54c38fb251ed72ef7d5bcdd8c5371c99506b0b8d98095506c3737` |
| `exact_20261114_tail_capacity_loader.mjs` | `07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395` |
| `geometry_20261115_pruefer_joint_row_representative.py` | `24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97` |

原 M sampler/worker/client 在 utilities 的原 `PINS` 中仍是被绑定的祖先源码；它们不是新 config 的主动角色。新 driver 不要求用它们替代这八个实际主动来源。完整实际配置的所有 source 同时合并进 driver 的 `consumed_source_sha256`，冲突保留为真实来源错误。

### 同一实际源码目录

`HERE` 是新 driver 自身所在目录。`cfg.computations` 必须解析为这个真实目录，profile/CP/各 loader 也使用同一实际 `code_directory`；`cfg.source_topic` 必须等于 CLI 的实际源目录。若未来调用层生成独立源码视图，必须把运行使用的整个依赖闭包放在相应真实目录，形成该目录的真实 config/身份，不能只把少量新 views 写入另一目录而仍标旧 `computations`。本包没有创建这样的 views，也没有更改任何原已发表全局。

## 3　三个输入来源及前置生成

### 3.1　接受父

父必须是同 job 的真实零活跃参数接受 checkpoint。`load_parent_checkpoint` 按以下四个**真实 reader 源**读取，而非统一改 schema：

| 父类型 | 实际 reader | 精确 SHA |
|---|---|---|
| R400，真实 450 | `geometry_20261115_continuous_ten_frozen450_checkpoint.py` | `43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae` |
| R441/R448/R456 使用的真实 resolution450 CP | `geometry_20261116_continuous_ten_resolution_checkpoint.py` | `bf7dedd2135e3f6b54bc806a17064428111b502b6ddb8572ec66a883b1ce34ad` |
| 原 R442 完整 M CP | `geometry_20261116_continuous_ten_frozen_M_checkpoint.py` | `18399ec7d7ad44f03d491fdf60a54794decfe8854c8115d7ebd55ed014ed5e93` |
| 本 R463 完整 M CP | 本包新 CP | `7545962063692edc34bbbce9893b038a9f408383208f72ad28a5608440781e39` |

检查实际 reader class/module、源码路径/SHA、manifest writer、维数、零活跃状态和实际分辨率。前两项调用原 `require_frozen450`，后两项调用各自 `require_frozen_M`。R449/actual202205 若使用真实 43f writer，它的实际 driver/source 仍保留在原 manifest/完整 closure，不能冒原 193/203。原 outer origin/deadline tuple 的明确注册仍是 R464 调用层职责。

### 3.2　原完整 112 远端与配置

R462 原 `sample` 必须读取同 job 原完整 112 输出、原 fullroot/误差/行/raw 与原 far/μ。R462 `configure` 必须真正读取与之对应的原 112 config，而不是拿某个后继父配置代替。父可以来自 R456 或原 M 精化，其 native 配置是**初猜和政策来源**；原 112 config 是**被复用族的来源**。

R462 `configure` 产生原配置文件 receipt 后，外层可另写新调用配置，添加明确 provenance，且只正规化已经存在的兼容 `modes` 为新 M。若 `modes` 缺失，原 full-DN utility 后续会添加；若 `spacing` 缺失，原 utility 后续会添加准确 2。已存在时 driver 要求分别等于新 M 与 2。由此不把纯兼容字段缺失误认为原数值策略改变，也不允许另一 spacing。

### 3.3　真实新 M union

新 config 的 schema 必须是 `R462-current-C-incremental-M-client-config-v1`；`geometry_directory/result.json` 必须是 `R462-current-C-old112-and-new-M-far-union-fresh-sampling-v1`，source 必须为 `5da13c5f…`；其 geometry 必须是 `R462-current-C-incremental-M-native-radial-geometry-bundle-v1`。完整新 M deep、全新增频率传播与全新 grid 必须已经真实完成。

新 CP helper `actual_union_native_binding(report, config, M)` 检查：

- 同 repository/run/source/model；真实 `completed/native_geometry_ready`，无原 error。
- 请求全频率 `2..2M`、保留旧频率 `2..224`、真实新增频率 `226..2M`；全部新 factorized/unit 列完成，未起后缀为空。
- `actual_original_input_binding` 是真正的新完整 M binding；内嵌 `new_complete_M_binding` 与它相等；`old112_complete_binding` 仍原样独立存在。
- 全部原 C 公共字段、准确 cut、原全根族和新完整 R442 proof identity 保留，原 112 `M_changed=false` 不被覆盖；union 顶层则明确 `M_changed=true`。
- 原 physical far/μ 字词相同；原 row 文档/矩阵身份保留；新 M 的第 i 行 Q/Pi 列为 `[i,M+i]`。
- 完整内嵌 union 对象按 R462 原 canonical JSON 编码，与真实 member 的 bytes/SHA 相等；live binder 再读该实际 member。
- 没有把数值代表宣称为共同准确 C 实现，没有使用旧响应/J/factor。

完整 row 文档/数组由实际 R462 worker/client 继续验证和消费。本 helper 保持实际原记录，不再求一次远端传播，也不在 CP summary 中塞入完整大数组。

## 4　新 driver 的 CLI

该命令必须由同一实际 owned deadline 的外层在公开 Actions 调用；以下符号路径和 SHA 是调用者实际对象的占位名称，不是现成配方或派发命令。

```text
python COMPUTATIONS/geometry_20261116_continuous_ten_incremental_M_refinement.py
  --recipe ACTUAL_RECIPE
  --recipe-sha256 ACTUAL_RECIPE_SHA256
  --accepted ORIGINAL_ACCEPTED96
  --accepted-sha256 ORIGINAL_ACCEPTED96_SHA256
  --parent-directory ACTUAL_PARENT_CHECKPOINT_DIRECTORY
  --parent-manifest-sha256 ACTUAL_PARENT_CHECKPOINT_SHA256
  --tail-config ACTUAL_UNION_BVP_CONFIG
  --tail-config-sha256 ACTUAL_UNION_BVP_CONFIG_SHA256
  --tail-source-root ACTUAL_ORIGINAL_SOURCE_TOPIC
  --tail-client COMPUTATIONS/geometry_20261116_current_C_incremental_M_tail_client.py
  --jac-workers 2
  --node-heap 6144
  --out FRESH_TEMP_RESULT_DIRECTORY
  --work FRESH_TEMP_FACTOR_DIRECTORY
```

`--tail-client` 可省略，此时 driver 仍选固定的新 R462 client；若给出则路径必须完全对应。`jac-workers=2`、`node-heap=6144` 是保留的原选择，不允许另值。`accepted` 是原 genuine96/1024 constructor/source 文件，仍核原完整 SHA、原 success/status、原 law 及 `/fixed_scalar_profile/geometry` 精确 pointer；它不是本次 accepted 父。

`out` 与 `work` 必须均在真实 `RUNNER_TEMP` 内、相互分离、都是空的新目录，而且不能包含原 recipe/accepted/parent/config/source/HERE。没有隐藏的临时输入恢复或默认父；没有 `--budget-seconds` 重起钟参数。本包只保留调用者负责原全局绝对钟的合同。

## 5　完整 recipe 字段

recipe 必须真实新写并按完整 bytes/SHA 绑定。它不得把父接受当新 M 接受；本接口不选其中任何未来参数。

| 字段 | 必须含义或原值 |
|---|---|
| `schema` | 本 R463 recipe schema |
| `operation` | `same-job-genuine-incremental-M-fresh-original-solve` |
| `parameter_order` | `p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3,xi` 的完整列表 |
| `all_ten_selected_from_actual_parent_without_changes` | `true`；实际仍从完整父读词 |
| `parent_checkpoint_sha256` | 实际父 manifest SHA，与 CLI 相等 |
| `accepted_source_sha256` | 原 accepted96 文件 SHA |
| `radial_seed_policy` | `all-parent-nodes-and-all-literal-knots` |
| `field_modes` | 显式新正整数 M，严格大于真实父 M |
| `physical_state_dimension` | `3*M+2` |
| `state_dimension` | `4*M+2` |
| `tail_modes` | M |
| `active_parameter_count`, `fixed_core_targets` | 均 0 |
| `outer_iterations`, `original_inner_trial_count` | 8、17 |
| `collocation_tolerance`, `boundary_tolerance` | `1e-6`、`1e-11` |
| `original_boundary_FD_threshold` | `5e-5` |
| `native_stage_count` | 576 |
| `height_sign` | 与实际父物理边界一致的原 ±1 |
| `max_nodes` | 显式整数容量，至少 2；不足完整 seed 就资源 partial |
| `refinement_factors` | 下一段四个键各为正整数 ≥1 |
| `actual_resolution` | 实际父 resolution 按该四因子和新 M 形成的完整七字段 |

四因子是 `field_and_native_angles`、`native_steps`、`material_angles`、`physical_angles`。前者同时乘原 `field_angular_quadrature` 与 `native_quadrature`；其他各乘对应字段。新七字段为 `field_modes`、`field_angular_quadrature`、`native_quadrature`、`native_steps_per_stage`、`material_angles`、`physical_angles`、`native_stage_count`。M 本身必须真实增加；四因子可以全为 1，但新 N 必须仍为偶数且 `N>8M`，两角数必须为偶数且各 `>4M`。不能为满足条件暗改 recipe。JS 整数接口容量不足产生明确资源 partial。

本 driver 没有径向倍增因子：它保留真实父的全部节点与全部 literal knots。父若已由 R456 真径向加密产生，这个更细 mesh 会进入本次完整 seed；未做过的径向加密不能由来源名字推定。求解后末 mesh 以原 solver 的实际输出为准。

## 6　配置比较和 R464 provenance

新主动配置必须完整保留原 runtime SHA 表和数值政策。`bind_current_native` 先核所有实际配置源，明确新 tuple，再核实际 N/steps、新 C/准确根族/cut/far/factory/union 数据；不是只检查一个 schema。

与接受父比较时，仅从数值政策比较中排除以下明确键：

```text
schema, field_modes, modes, spacing, source_sha256,
geometry_directory, geometry_result_sha256, quadrature, steps,
current_BVP_adapter_origin, resolution_refinement_origin,
mode_refinement_origin, R456_same_far_fresh_grid_origin,
R462_actual_union_origin, R464_incremental_M_owner_origin
```

这里 `spacing` 并非自由参数：若存在只能是 2；`modes` 若存在只能是真新 M。其余未列出的所有配置字段必须与父逐字段相等，包括原数值阈值、policy 和资源参数；来源元信息差异不放宽数值方法。

driver 对 `R462_actual_union_origin` 核实际 union sampling/geometry receipt、原 112 sampling receipt、原配置 descriptor 与原完整族/fresh 责任字段。它没有仅凭 descriptor 再读原 112 config 文件；真实该原件读取由冻结 R462 `configure` 与外层原配置绑定承担，完整 receipt 继续保留。

可选 `R464_incremental_M_owner_origin` 若存在，按以下六个真实字段核，而不是允许任意 opaque origin：

| 字段 | 对应实际来源 |
|---|---|
| `actual_parent_checkpoint` | 当前接受父完整 manifest 的 bytes/SHA |
| `original112_config` | R462 configure 真读取的原 112 config receipt |
| `actual_R462_configure_configuration` | 原 configure 生成文件 receipt；该原件由外层保留 |
| `actual_new_M_deep_result` | 新实际输入 binding 的完整 M deep result |
| `actual_union_sampling_result` | 本次实际 union result |
| `actual_resolution` | 本 recipe 的实际七字段 |

R464 独立配置只添加自己的 provenance、正规化可选 `modes`；不得改变原 root/RK、linear、native acceptance 等数学 policy。driver 进一步真实读取新 union member 和当前 geometry；原 112 binding 不用新 M 或 owner metadata 覆盖。若外层没有这个可选 provenance，合法原 R462 配置仍可直接作为该 driver 的输入，前提是已存在的兼容字段符合上面的实际值。

## 7　保留的完整求解次序与门

以下原数学函数/连续控制流未因 source 注册被删减：`selected_resolution`、`resolution_seed`、`prepare_refined`、`problem_binding`、`run_phase` 的求解正文以及 main 的原阶段处理。新身份/receipt 字段之外保持原方法。

完整节点并集超过 `max_nodes`，或者实际整数接口容量超限时，返回 75 并记录资源 partial，不截断完整并集。父全部 node 字和原状态块在初猜时按新 M 偏移保持；新增高模只作为初猜零词。所有 M RHS fresh，原 preflight fresh；父 DY/J 不作为当前方程求值。

随后从实际当前边界形成全 M 的 H，真实 native solve 及完整端点 J，然后执行原五项 cut 比较和两组原 FD。FD 使用原三个扰动、全部方向和两层 Richardson，完整阈值 `5e-5`。原 affine 扰动只锚定这个真实当前响应；它不是继承旧 J。

原 full-DN 仍求解完整 `4M+2`、零活跃参数、左 `3M+2` / 右 M 的系统。保原 8 outer / 17 inner、RMS `1e-6`、BC `1e-11`、原 frozen-control RMS、末实际 H/J/fresh audit 及物理 cut/两 mean 记录。native 仍原 32/10/`2e-9`/`eta=1` 和全 `eta=0` 敏感度。576 stage 与显式 steps 参数按原实际 schedule，不把配置数值另写成未核的原子步数保证。

完整新 far 行用于本次边界，所有旧/new 行的误差族保留；没有把它们转成“native tolerance 已经严格达到准确 C 误差”的结论。原数值末门与连续几何责任保持原分工。

## 8　live writer 与 own reader

实际 API：

```text
checkpoint.load_profile(code_directory)
checkpoint.load_parent_checkpoint(directory, manifest_sha256, code_directory)
checkpoint.require_parent_instance(parent, code_directory)
checkpoint.actual_union_native_binding(report, config, mode_count)

checkpoint.LiveCheckpointWriter(
    owner, flow, boundary, separated, original_core_module, raw_client,
    driver_source=ACTUAL_DRIVER_PATH,
    complete_source_sha256=ACTUAL_RUNTIME_CLOSURE,
    original_law=ACTUAL_ORIGINAL_LAW, parent=ACTUAL_PARENT)

writer.capture(
    original_result=ACTUAL_UNANNOTATED_FULL_DN_RESULT,
    fd_result=ACTUAL_FD,
    fd_anchor_response=ACTUAL_CURRENT_H_RESPONSE,
    final_native_response=ACTUAL_FINAL_J_AND_AUDIT,
    physical_cut_audit=ACTUAL_PHYSICAL_CUT_RECORD,
    out=FRESH_CHECKPOINT_DIRECTORY)

checkpoint.Checkpoint(directory, manifest_sha256, code_directory)
checkpoint_instance.require_frozen_M()
```

writer 核真实 profile/flow/boundary/separated 实例、原实际 core/augmented/boundary/cut audit 源、完整 runtime closure，且实际 writer/driver 自身都在 closure 内。它只在原未注释 full-DN 文件已经接受、原 FD 和末真实 native/audit 来源吻合后捕获；不把未执行的 response 补零。

原完整数组包括 mesh、physical states/RHS、augmented states/RHS、完整 core、原两 mean/常数行 drift 等；原十词固定。原物理 RHS 与 augmented RHS 有各自真正计算语义，原代码并未强迫它们逐词相同。末实际 H 仍按原 trace 重算，原 `1e-12` 同场绑定责任不变；没有新 seam 数值阈值。

新 `original_native_binding.complete_far_union_binding` 包含原/新 source tuple、原完整 union member、原112结果/geometry/row/matrix、新全 M 行、新深端、真实 far/μ 和完整频率范围。其 `all_native_responses_J_means_and_BVP_gates_must_be_fresh` 是责任标记；真正已完成状态由原实际接受/FD/末 audit 判断，不能在 driver 初次 bind 时提前写作已完成。

CP 把完整 R462 `result.json` 逐字复制为 `members.native_geometry_result`，于是原 112 完整 binding 与新完整 M binding 的原对象均保存。它不复制整个 external geometry/row/error ledger 目录；后继 radial/closed-field 消费必须在同 job 持有这些真实 raw，不能只凭 CP 的 SHA 恢复不存在的数组。

own reader 除原全部成员、数组、target、FD、末 response 与源闭包检查外，再调用同 `actual_union_native_binding` 核该实际复制结果，并与 manifest 的联合来源记录完全比较。它不能创建 accepted field。

## 9　CP 读取 CLI 与实际输出

```text
python COMPUTATIONS/geometry_20261116_continuous_ten_incremental_M_checkpoint.py
  --directory ACTUAL_CHECKPOINT_DIRECTORY
  --manifest-sha256 ACTUAL_CHECKPOINT_SHA256
  --code-directory COMPUTATIONS
  --require-frozen
  --out FRESH_TEMP_CHECKPOINT_READOUT
```

这条命令执行真实字段/数组比较，仍只允许公开 Actions。`--out` 必须是 RUNNER_TEMP 内尚不存在的新文件。stdout 只给 readout 文件 receipt、维数和实际 frozen 标志；完整 readout 写入原临时文件。本包没有声称它是已封装的单份 90KB workflow readback。

driver 主要原输出保留：

| 路径（相对 `out`） | 原范围 |
|---|---|
| `adapter-status.json` | 实际 phase、source/recipe/输入、当前维数、原 gates、异常/未起范围、native calls/关闭状态 |
| `refined-M/initial-guess/mode-seed-plan.json` | 原节点/knots 并集、字词身份、显式容量、旧/新维数、真初猜来源 |
| `refined-M/initial-guess/complete-nested-seed-binding.json` | 完整原 preflight 返回后的 seed/RHS 和固定 target 绑定 |
| `refined-M/initial-guess/phase-binding.json` | 完整当前 phase、原配置与全部 source closure |
| `refined-M/initial-guess/prepared.json.gz` | 真完整初猜/新 RHS，仅临时 |
| `refined-M/actual-H-response/actual-first-height-input.json` | 真当前 H 全字词与来源 |
| `refined-M/actual-H-response/initial-actual-H-tail.json.gz` | 真 current H 的完整 native/J |
| `refined-M/actual-H-response/original-five-cut-comparisons.json` | 原五字段实际双方值/字与原 `isclose` |
| `refined-M/actual-H-response/response-check.json` | 完整两组 FD、所有原层/方向与原接受字段 |
| `refined-M/full-DN/` | 原完整 solve、末 J/audit、物理 cut 与所有状态 |
| `refined-M/accepted-checkpoint/` | 仅真正末接受后写出的新 CP；未接受时不捏造 |

阶段名仍是 `refined-M`，方便外层明确保持原路径合同；schema/source 已为新 R463，不因目录名相同重标原 M 结果。

## 10　返回、绝对钟、必要读取和 raw

正常返回是否接受由原 `status==0`、真实 final checkpoint、零活跃维数决定。原 cut/FD 未过时保原状态；原 full-DN 失败保原 code/phase。显式容量/安全整数不足返回 75，`resource_partial=true`，不据此叫数学无解。普通异常保 repr/traceback 与原 phase/未起后缀，然后按原程序抛出。若 runtime/input 在 session 初始化前失败，外层仍须保原 stderr 和未起范围，不能假设 `adapter-status.json` 一定存在。

`finally` 对已经创建的 current owner 原样尝试关闭，保关闭异常、所有已返回 native calls、leases 状态。原程序的数值返回与实际 quiescence 是两件事；不能仅因 exit0 主动删 raw。

**本包没有 owned launcher、绝对钟执行器、最终 90KB necessary reader 或 cleanup marker。** R464 必须按原同 job 的 actual deadline 将完整新 M deep、R462 sample→configure、driver 的 setup/求解/末门一起安排在实际剩余资源内，不能启动时重新获得完整时长。科学 child 必须使用原受控 session/group、TERM→KILL、join/实际 quiet 合同；真正读取所有必要错误、partial/未起地址和成员身份之后才具备后继 cleanup 条件。

完整原成功大矩阵/全部 raw 不传 Git 或 artifacts；必要 reader 不编码分块搬运它们。reader 自身若不能完整支付必要范围或超过 90000 B，只能诚实 metadata partial/70并保 raw。这里没有给这些尚未接好的工作流责任一个提前“通过”的布尔值。

## 11　原 112 binding、材料与几何的后继责任

`same_original_far_family_reuse.M_changed=false` 是历史原 R456 冻结对象中的真实语义；本包绝不把它改成新 M。新 union 顶层的 `M_changed=true` 与实际新 M 深端/input/source 同时存在。旧原两系数进入新 M 的列位置由 R462 真 raw 给出，不通过本 driver 重算。原误差族包围的是完整候选集合；选择有限数值代表仍不证明它们来自同一个准确 C 根选择。

同准确 C/十词固定不等于同材料坐标分量：当前 M/core 的 Phi 可以变化。全闭合 target 需要真实首次 A/B construction、全部 marker 与物理/材料图绑定；R443/R447 的正确共轭、全部六jet、帽 chart/seam 仍独立负责。现 R442/R451/R457 等消费者若硬锁 18399，不能仅改 manifest writer/source 就读新 CP；R464 必须独立注册真实 R463 loader 及完整当前径向/atlas/shared/metric/reach/held/材料来源。

本包未执行这些几何，不继承旧 metric/reach/held/距离结果，不声称 README 所需的误差持续下降、严格连续解或机器精度。R459 的可比较全域误差证据须由真正新场另行计算，不能把两次 finite 接受或重复固定 eta pass 当下降。

## 12　本次交付边界

实际新增运行件只有两份；原 profile、M utilities、hooks、native、bridge、QR、deep、R462 三源均保持冻结。完整 source 差异只有独立 schema/source 选择、真实 union 输入/列布局/配置 provenance、四父 reader 注册和相应 receipts。原求解正文未新增 rank、误差、域或几何接受门。

本目录内的 `publication-files.json`、两份完整 baseline `.diff`、文首四来源小 `.diff`、`source-build-identities.json` 与文本构造脚本是临时可重建材料；正式刊出仅两源码、R463 条件证明与本接口。没有分配新 request，没有操作 Git refs，没有启动 Actions，也没有预填后继实际父或结果。
