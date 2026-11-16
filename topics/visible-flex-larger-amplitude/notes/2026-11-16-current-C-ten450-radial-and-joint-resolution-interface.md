# R448：真实 frozen450 的径向与联合分辨率细化接口

作者：geometry agent（AI），2026-11-16。

本包是 requestless 的六源实现与完整条件证明。没有选择实际父场、mesh 因子、`max_nodes`、各阶段资源、request、run 或未来结果；没有修改已经冻结的 R441、203 helper、R437、原 193 / joint203 或 root 工作流。所有科学导入、计算、AST、编译、测试仍仅 Actions，本地只做源文本、原调用合同、字节哈希与完整 diff 的处理。

## 1　交付与确切身份

数学责任见 [R448](../results/R448-fixed-target-radial-mesh-and-joint-resolution-refinement.md)。本文与六个独立运行文件提交；builder、diff、静态身份回执与本地 manifest 只供交接，不作为新科学输入或新的验证门。

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| [geometry_20261116_continuous_ten_frozen450_radial_resolution_refinement.py](../computations/geometry_20261116_continuous_ten_frozen450_radial_resolution_refinement.py) | 49228 | `137d42cb27bb1aef227d42445adf07a6d11f7bba57315abdf151cc3b0086c7e8` |
| [geometry_20261116_current_C_frozen450_radial_resolution_owned_launch.py](../computations/geometry_20261116_current_C_frozen450_radial_resolution_owned_launch.py) | 49098 | `f3a2abf626fbb7f636315e40608b55170748a779e7bdf1287ebc362e04b73cf2` |
| [geometry_20261116_current_C_radial_resolution450_postsolve_geometry.py](../computations/geometry_20261116_current_C_radial_resolution450_postsolve_geometry.py) | 57405 | `64086e8dc283507442ab519f7fa139b748259948d2e9c5a419227363b33c67b8` |
| [geometry_20261116_current_C_radial_resolution450_postsolve_held.py](../computations/geometry_20261116_current_C_radial_resolution450_postsolve_held.py) | 43989 | `8ffa2e6fe2f9e30f5c4aada0f9adcbb9af2e28152e0ce019291bda5bffffbbcb` |
| [root_20261116_current_C_frozen450_radial_resolution_necessary_readout.py](../computations/root_20261116_current_C_frozen450_radial_resolution_necessary_readout.py) | 30056 | `965b07a1a996e9812cd91abf90254e3236323e9a2343e288ad699e675a2d75bb` |
| [root_20261116_current_C_radial_resolution450_postsolve_necessary.py](../computations/root_20261116_current_C_radial_resolution450_postsolve_necessary.py) | 27246 | `a087f6b4fe1ace727c2867eab5d34a8915fec1a007996bb96ced8392d289c71f` |

每个运行文件旁有相对于已冻结 R441 对应真实源码的完整 `.diff`。本包没有复制原十八源：完整 checkpoint writer、phase metadata API 及其余 resolution 几何 / scalar 数学源按原字节复用，合计下表十二个文件。实际新 checkpoint 仍是该真实 writer 的格式，新 driver 的源码、全数组、父身份和所有原末门进入新记录。

## 2　精确适用范围

当前实现固定 $M=112$、完整物理 338、完整 core 112、frozen450、活动标量数 0、固定 core targets 0；十个已接受参数按原 LE64 字值保持。新的 core 112 分量属于原边值问题未知量，可以在 fresh solve 中改变。没有用删去 453 三行代替真正 450 求解。

真正允许的 origin 是：

| origin | 原 launcher | 原 driver | 原实际 deadline schema |
|---|---|---|---|
| original193 | `geometry_20261115_continuous_ten_full453_frozen450_launch.py`，`6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66` | `geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py`，`11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8` | `request193-owned-job-science-deadline-v1` |
| joint203 | `geometry_20261116_continuous_ten_joint_full453_frozen450_launch.py`，`cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7` | `geometry_20261116_continuous_ten_joint_full453_frozen450_physical_dn.py`，`5400aa4a724b0403e6a89db2ea056f489dc336e685fa85e2ef1ef0fc51569592` | `request203-owned-job-science-deadline-v1` |

输入的 `origin_launch_directory` 总指真实原始两阶段 launcher。`parent_launch_directory` 可以是同一目录，也可以是真实 R431、R441 或本 R448 的后继输出。R431 只接受它原本实现的 original193 来源；不会以 compatible schema 冒 joint203 实现。后继必须保同 origin result 字节、同 deadline 字节、同准确 target / finite compiler 身份、同十字值，并确实完成自己的原 450 门。

R431 来源严格为 `4375375b343bc2e3b359a2e1ca566bb6648e08b691d7208cced348f185272868` owner 与 `70a5709d6bca4bf124a029ebcc33fae31407c3214c5164a867a8de9f37d53928` driver。R441 来源严格为 `2247aa97c4ed63c9065d1e326fb78b84500ee7b834f0970905e977773bcea8df` owner 与 `bf1f8d2dda15584791147f97dc6f313435c16d080acaa49ef418c2df06d503b3` driver；这里是已修正异常 `code=2` 的版本，不使用 superseded 旧 owner。

本 R448 后继则按本文独立 owner 的当前实际 SHA 与本文 driver 绑定，不把旧结果重新命名。当前没有任何一个实际可用的 accepted 父被本文预填。

## 3　五个因子与实际网格算法

`refinement_factors` 必须恰含五个正整数键：

| 键 | 实际改变 |
|---|---|
| `radial_mesh` | 每个父闭区间的准确有理 $j/f$ 候选，然后单次 RN64 |
| `field_and_native_angles` | 同时乘父 `field_angular_quadrature` 与 `native_quadrature` |
| `native_steps` | 乘父 `native_steps_per_stage`，重新生产完整实际样本 schedule |
| `material_angles` | 乘父完整 MaterialTrace 角数 |
| `physical_angles` | 乘父完整物理 Galerkin 角数 |

五因子至少一项大于 1。纯径向允许后四项全部为 1；本包没有调用原 R441 的四因子拒绝条件。实际 mesh 仍须出现新机器点；若因舍入没有新增节点且后四项均不变，driver 以明确资源 partial 返回 75。若后四项实际增加，则相应联合运行可以继续，同时诚实记录径向未增加。

实际七字段保持原 R441 writer 合同：`field_modes`、`field_angular_quadrature`、`native_quadrature`、`native_steps_per_stage`、`material_angles`、`physical_angles`、`native_stage_count`。径向节点数来自新实际数组，因子与完整 seed 来源来自新 recipe / plan，不能塞一个静态“mesh 已加密”布尔代替原网格。

对父 $x_i<x_{i+1}$，全部 $j=1,\ldots,f_r-1$ 使用

$$
\operatorname{RN}_{64}\left(Q(x_i)+\frac j{f_r}\bigl(Q(x_{i+1})-Q(x_i)\bigr)\right).
$$

不是逐步相加已舍入步长。随后保全部父节点、全部 literal knots 和所有不同候选。父节点重写原字值，包括符号零；profile 的原 knots 本体不改，mesh 同值去重。候选地址、准确有理值、舍入词、端点塌缩与去重原因写 `radial-grid-candidates.jsonl`。

`max_nodes` 是显式资源：必需父节点与所有 knots 若已超限，或者枚举时首次新增导致超限，保完整未访地址后停止；不删点、不抽样、不假设原 1200 容得下。完整枚举的 machine-no-new-point 也仅是资源停止。

父 450 状态与 mesh 字值的逐 bytes 保持只在初猜 / preflight。父 DY 仅是 Hermite 初猜系数；全新 450 行 RHS 重算，原完整 preflight 重跑。真正 fullDN 后状态可变、mesh 可按原算法调整；以实际末输出为准。

## 4　运行 owner：确切 CLI 与输入 JSON

公开 Actions 内命令为：

```bash
python -u "$COMPUTATIONS/geometry_20261116_current_C_frozen450_radial_resolution_owned_launch.py" \
  --input "$R448_INPUT" \
  --input-sha256 "$R448_INPUT_SHA256"
```

上例变量仅表示实际 caller 生成的路径与 SHA，不是已存在的配方或新运行。输入 schema：

`R448-current-C-frozen450-radial-resolution-owned-launch-v1-input-v1`

必需字段如下；源码可读入其他来源说明，但这些字段不能由标签或旧 SHA 补造。

| 字段 | 实际来源 / 约束 |
|---|---|
| `namespace` | `RUNNER_TEMP` 下现有真实 namespace |
| `origin_launch_directory` | 原始 193 或 joint203 的真实 launcher 目录 |
| `parent_launch_directory` | 真正已接受 450 的明确来源目录 |
| `job_deadline`, `job_deadline_sha256` | 原 origin launcher 实际消费的 deadline，逐 bytes/SHA 同一 |
| `computations` | 包含实际已 pin 源码的目录 |
| `accepted`, `accepted_sha256` | 原真实 96 构造 / source geometry 输入；保持原 same-target source |
| `tail_config`, `tail_config_sha256` | origin 的 `actual_input_files.current_native_config` 原件，不是后继重新命名的 config |
| `tail_source_root` | origin 实际命令唯一 `--tail-source-root` 路径 |
| `out` | namespace 内全新 sibling；不得包含输入、旧父或源码 |
| `max_nodes` | 正式声明的完整 seed / solver 容量，整数至少 2 |
| `refinement_factors` | 第 3 节五个完整正整数，至少一个请求增加 |
| `sampling` | 下述完整 fresh sampler 输入与资源 |
| `resources` | 下述五项完整 owner 资源 |

`resources` 必须恰含：

- `sampling_process_budget_seconds`
- `refinement_process_budget_seconds`
- `child_shutdown_reserve_seconds`
- `minimum_free_bytes_at_start`
- `free_bytes_resource_stop`

前三者为实际有限正数，后两者为正整数且停止储备小于启动所需空间。这些是工作资源，不是新的目标、残差或 acceptance 条件。没有默认替未来 caller 选择数值。

`sampling` 必须有实际 `cover_directory`、`cover_result_sha256`、`far_directory`、`far_result_sha256`、`proof`、`unit_row_proof`，以及完整 `parameters`。其资源键来自原 sampler：

`precision_bits`, `linear_budget_seconds`, `sampling_budget_seconds`, `max_panels`, `free_bytes_reserve`, `max_depth`, `local_defect_bits`, `panel_norm_limit`, `taylor_terms`, `max_geometry_cache_records`, `sample_max_nodes`, `sample_inverse_depth`, `sample_value_bits`。

joint203 还必须显式提供第十四项 `representative_max_precision_bits`，其值由实际 caller 写入；本包不替 caller 填默认值。original193 仍只取上述十三项，不能加入被忽略的参数。

owner 对原 sampler 完整 C/root 输入、实际源、真实原有限 cut/far 字值逐项绑定；新的 `steps` 来自实际父配置乘显式因子。即便纯径向且 steps 不变，当前实现仍真实重生该 sampler，再完整重求；没有复用旧响应、J、factor 或假称某个新样本已生成。

原 source family 决定实际 sampler/client：original193 使用 `965c277c5aad5a3b5c8c817600d4c435186d9ce1b267b0b59f6e7a8fa69de390` 与 `acb8b67b8e44dbfae9b0d166bfc75910f2c48a6aca238571db44d20520a0a1f9`；joint203 使用 `32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4` 与 `02e1645248ef01ffff10a50c2198194fafd40709254816408e1b9944e1cd0ae1`。本次没有修改四个原源。

## 5　真实 driver argv、recipe 与原求解

owner 真正生成 `actual-resolution-recipe.json` 和 `actual-refined-native-config.json`；不会预先把未来参数写死。driver 的完整 argv 为：

```bash
python -u "$COMPUTATIONS/geometry_20261116_continuous_ten_frozen450_radial_resolution_refinement.py" \
  --recipe "$OWNER_OUT/actual-resolution-recipe.json" --recipe-sha256 "$ACTUAL_RECIPE_SHA256" \
  --accepted "$ACTUAL_ORIGINAL_ACCEPTED" --accepted-sha256 "$ACTUAL_ORIGINAL_ACCEPTED_SHA256" \
  --parent-directory "$ACTUAL_PARENT_CHECKPOINT_DIRECTORY" \
  --parent-manifest-sha256 "$ACTUAL_PARENT_CHECKPOINT_SHA256" \
  --tail-config "$OWNER_OUT/actual-refined-native-config.json" \
  --tail-config-sha256 "$ACTUAL_REFINED_CONFIG_SHA256" \
  --tail-source-root "$ACTUAL_ORIGINAL_SOURCE_TOPIC" \
  --tail-client "$COMPUTATIONS/$ACTUAL_PARENT_CLIENT" \
  --jac-workers 2 --node-heap 6144 \
  --out "$OWNER_OUT/refined-BVP" --work "$OWNER_OUT/banded-work"
```

直接 driver CLI 是底层实际 API。为保原时钟和 quiet，应由本文 owner 调用，不把裸命令当已完成的 workflow。driver 不重启内部科学钟。

生成 recipe schema 是

`R448-explicit-current-C-ten-frozen450-radial-resolution-refinement-v1`，

operation 是 `same-job-genuine-frozen450-radial-resolution-fresh-original-solve`；`radial_seed_policy` 是 `all-parent-nodes-all-factor-subdivision-nodes-and-all-literal-knots`。它保原 parameter_order、真实 parent manifest SHA、原 accepted SHA、原 height_sign、十参数全取父、五因子、实际七 resolution 字段与下列原合同：

- `field_modes=tail_modes=112`，`physical_state_dimension=338`，`state_dimension=450`，`active_parameter_count=fixed_core_targets=0`。
- `outer_iterations=8`，`original_inner_trial_count=17`，`collocation_tolerance=1e-6`，`boundary_tolerance=1e-11`，`original_boundary_FD_threshold=5e-5`。
- `native_stage_count=576`；实际 steps 及其原 schedule 由新 sampler/config 读回。
- 原 native 32 / 10、容差 `2e-9`、方向 `eta=1`、全敏感度 `eta=0` 均保原源。

真实 `run_phase` 继续完整 current H、全 $338\times112$ J、FD、原 fullDN、末 current response / J、独立 fresh audit 与全数组 writer。parent DY、prepared 旧数组、旧零响应与旧 native factor 不作新原件替代。

输出布局包括：

| 位置 | 内容 |
|---|---|
| `OWNER_OUT/result.json` | owner 原实际状态、子进程、绝对钟、来源、错误与 quiet |
| `OWNER_OUT/native-sampling/` | 实际新完整 sampler 输出 |
| `OWNER_OUT/actual-resolution-recipe.json` | 真实父词、五因子、实际 resolution 的小配方 |
| `OWNER_OUT/actual-refined-native-config.json` | 仅允许的 geometry / N / steps / 来源更改 |
| `OWNER_OUT/refined-BVP/adapter-status.json` | 真正 R448 科学阶段 / 原门 / 未访 / 错误 |
| `OWNER_OUT/refined-BVP/refined450/initial-guess/radial-resolution-plan.json` | 完整候选计划、进度、未访地址与资源原因 |
| 同目录 `radial-grid-candidates.jsonl` | 全部实际候选原 temporary 账本 |
| 同目录 `complete-nested-seed-binding.json` | 完整 fresh RHS / preflight 真返回后才生成 |
| `OWNER_OUT/refined-BVP/refined450/accepted-checkpoint/` | 只有实际原末门成功后才由原 writer 产生 |

最后一个目录以实际 `actual_final_checkpoint_directory` 为准，不凭表格存在假设恢复。

## 6　复用 writer 与所有数学消费者

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| [geometry_20261116_continuous_ten_resolution_checkpoint.py](../computations/geometry_20261116_continuous_ten_resolution_checkpoint.py) | 43561 | `bf7dedd2135e3f6b54bc806a17064428111b502b6ddb8572ec66a883b1ce34ad` |
| [geometry_20261116_continuous_ten_resolution_saved_prefix.py](../computations/geometry_20261116_continuous_ten_resolution_saved_prefix.py) | 19180 | `fb6e181cd0ddfb34cc70c874c119ceb149850ce8756d1f2f0dd775175e99cffb` |
| [geometry_20261116_current_C_ten450_resolution_radial_readout.mjs](../computations/geometry_20261116_current_C_ten450_resolution_radial_readout.mjs) | 23527 | `3d711d395693cdf8ad222e0838bb29b99ffb5043defb8a66c992dc854df018f4` |
| [geometry_20261116_current_C_ten450_resolution_shared_field.py](../computations/geometry_20261116_current_C_ten450_resolution_shared_field.py) | 49116 | `1ceda9d32cfcf50e28e737cd0aee981cb8dc2329027aa2967d08532a1ea6e935` |
| [geometry_20261116_current_C_resolution_original_cuff_atlas.py](../computations/geometry_20261116_current_C_resolution_original_cuff_atlas.py) | 29116 | `d0b03a367f3ece13b06949d5218a992e6ee3e9a41364499070d3f5f475a150a0` |
| [geometry_20261116_current_C_resolution_accurate_cut_patch.py](../computations/geometry_20261116_current_C_resolution_accurate_cut_patch.py) | 26070 | `8811f89c7395bb4aed1adabe6c6825c801e1e41a9d80d416b0a4746596ae9a52` |
| [geometry_20261116_current_C_resolution_fixed_cap_balls.py](../computations/geometry_20261116_current_C_resolution_fixed_cap_balls.py) | 23665 | `ca53bdc5c0cdd5764065301f0edb1259d083fdffa9f3d767a5a38b4a7cafe364` |
| [geometry_20261116_current_C_resolution_live_query_complete_metric.py](../computations/geometry_20261116_current_C_resolution_live_query_complete_metric.py) | 55053 | `fd263af28a7d55a7246a49283d367e420786f48f16556dd5a7d61406b1c8459b` |
| [geometry_20261116_current_C_resolution_complete_reach_cover.py](../computations/geometry_20261116_current_C_resolution_complete_reach_cover.py) | 60452 | `745b245eddd27c10522012756a33bd842b3883d918845de49cc2cdacbeed1a05` |
| [geometry_20261116_current_C_resolution_complete_block_reach_cover.py](../computations/geometry_20261116_current_C_resolution_complete_block_reach_cover.py) | 45582 | `f27556bcfbeb72ac3ad7142bbc5089e1168fdc7966fe91757e1a201b7dbfe957` |
| [geometry_20261116_current_C_resolution_held_and_rigidity_inputs.py](../computations/geometry_20261116_current_C_resolution_held_and_rigidity_inputs.py) | 53737 | `144da57a9d55547fa3b85ccb43c0f4261db2e2dcb41e91094c8d3a16c9b7d7b1` |
| [root_20261116_continuous_ten_resolution_phase_readout.py](../computations/root_20261116_continuous_ten_resolution_phase_readout.py) | 18700 | `448c35c390abd78d169db8bad0c292d89b18cb0109fe5216420b5133479132bf` |

这些数学源不会改成 R448 schema。bf7d writer 使用 `R441-current-continuous-ten-resolution450-physical-DN-checkpoint-v1`，并实际记录 R448 driver、完整 runtime source closure、新数组、新 native config、实际 parent、FD/final/audit。这个格式本来支持真实 driver 来源；保留它避免无必要复制 writer。

original193 / R431 父用原 43f writer；R441 / R448 父用 bf7d writer。无论哪个分支，都加载完整数组与原 current profile，核实际父 450 成功及同十词 target；不是只读一个 `success=true` 标签。所有旧源的递归 pin 仍由其原 loader 和新实际 closure 核，运行 manifest 不是把动态来源责任截成一个短静态列表。

元数据依赖另包括：原 lifecycle `geometry_20261115_current_C_ten450_postsolve_geometry.py` / `84d0450f2f362138045c222f5a47162e030fd0be8b6c7a99c5d66c0e41da425a`；原必要 reader `root_20261115_current_C_pruefer_positive_full453_necessary_readout.py` / `34b49f026338b90b691cbd170d6d6303c7ec3549f2329ba0f4457a2cfeab75c9`；joint 必要 reader `root_20261115_current_C_pruefer_joint_full453_necessary_readout.py` / `19878e48ed25dec8bdcbd36c3d7ea7168796a08fb60675ad7455dbb296a0918c`。它们只作原受控 lifecycle 或必要 metadata API，不加载科学源来重算结果。

## 7　同一原绝对钟、资源与 partial

owner 必须实际读取 origin 已消费的 `actual_job_deadline`，核 bytes/SHA、schema、run/source 和原 recipe。其 `namespace_created_unix_seconds + 18900` 是同一原科学截止，原 readback reserve 为 2700；不由新 owner 的启动时刻重新计算一轮 18900。

每个子进程启动时按显式工作上限与实际原剩余时间减关闭预留裁剪。过程中继续检查截止、外部信号和临时盘空间；所有 children 使用自有 `start_new_session=True`、原 PID/start-ticks 观察与 TERM→KILL/wait。原 parent Python 可能共享 runner PGID，因此只按其真实 PID 身份观察，不要求共享公共组清空。

原已修 R441 的 `except BaseException` 首行 `code=2` 保留，避免 sampler 先返回 0、随后 BVP setup 异常却让 owner 返回 0。完整 driver 节点容量资源 stop 为 75；owner 时间 / 存储 stop 为 124，外部信号按原真实 signal 状态，程序异常为错误，不填数学拒绝。

这里不承诺所有工作资源之和能装进剩余原钟。bind/setup 也耗原真实剩余时间，子进程启动时不能重新获得这些时间。最终 step/job 硬限、规则 runner、总 readback 安排和清理由后继具体 caller 正式接线；本包有 owned process 和必要 API，但没有新增 workflow 或声称该外层编排已经发生。

## 8　owner 必要读回：完整剩余地址与原范围

科学子进程停止并实际 quiet 后：

```bash
python -u "$COMPUTATIONS/root_20261116_current_C_frozen450_radial_resolution_necessary_readout.py" \
  --namespace "$ACTUAL_NAMESPACE" --launch-directory "$OWNER_OUT" \
  --computations "$COMPUTATIONS" --out "$FRESH_OWNER_READBACK_DIRECTORY" \
  --entry-stdout "$ACTUAL_OUTER_STDOUT" --entry-stderr "$ACTUAL_OUTER_STDERR"
```

最后两项可省略，其他四项必需；若提供必须是真实同 namespace 日志。输出 `scalar-summary.json`，schema 为 `R448-current-C-radial-resolution450-one-necessary-readback-v1`，frame 是 `BEGIN_R448_FROZEN450_RESOLUTION_NECESSARY` / `END_R448_FROZEN450_RESOLUTION_NECESSARY`。

step outputs 继续原 `resolution_summary`、`resolution_summary_bytes`、`resolution_summary_sha256`，不是自动声明 job/report outputs 已接好。只有 `complete_necessary_readback=true` 才写 `readback-complete.json`；其 marker schema 是上述 schema 加 `-complete-marker`，带 actual namespace、launch result、原 necessary identity 与真实 quiet。

新增必要选择保：完整候选数、处理数、实际新不同点数、端点塌缩 / 重复数、首末塌缩见证、完整未访区间和 $j$ 后缀、容量原因、真实完整 seed / preflight 标志和实际五项增加标志。当前 interval 与其后整个区间闭范围不截断；无实际求解时所有 H/FD/fullDN 后继保持未访。

完整 literal knot 数组被读取但正文只返回身份。完整候选 JSONL 通过原 inventory 保 bytes/SHA，正文不搬运全部候选或此前所有塌缩行；plan 的计数和首末见证仍是科学 producer 原字段。异常强停时 plan 的保守 pending 可以覆盖已写账本的部分前缀，该重叠明确保留，不能据 ledger SHA 认定责任已完成。

原 phase reader完整选择每个实际已生成 FD error level / contraction / flags，以及原 RMS、BC、末 J、audit、cut 与 checkpoint；新 sampler 所有实际 mode / pending 仍由实际 source-family selector 读取。native 每 call 原标量行、全部失败/未完成 call scope 与最后 call 细节保留；此前巨大 native trial 状态、J、成功 factor/RHS 表仅身份，不宣称全部传回。

每份必要记录仍限 90000 字节。超限明确 70，不提高限制、不编码分包、不静默删失败或未访；必要不完整不写 marker。全部 raw 留同 job，本 reader 不删除数据。

## 9　新 450 后的五阶段完整几何

命令：

```bash
python -u "$COMPUTATIONS/geometry_20261116_current_C_radial_resolution450_postsolve_geometry.py" \
  --input "$R448_POSTSOLVE_INPUT" --input-sha256 "$R448_POSTSOLVE_INPUT_SHA256"
```

其 schema 为 `R448-current-C-radial-resolution450-same-job-live-query-block-geometry-v1-input-v1`，`upstream_kind` 必须是 `R448-radial-resolution450`。它只注册本包实际新 owner/driver；五个数学角色仍是未改的 R441 源。

输入必须有 namespace、实际 `upstream_launch_directory`、原 `job_deadline`/SHA、实际新 `geometry_directory`、同一 `continuous_e_directory`/resultSHA、computations、proof_directory、source_topic、fresh out，以及 `first_shared_directory`/resultSHA。actual geometry result 必须同时等于新 owner sampler receipt 和新 CP 的 native binding；同一个实际 C result / 根族原件不能换成 cut 三盒或旧 fingerprint。

`construction` 恰含 `cut_correction_width`、`cap_height`、`fixed_cap`。完整 marker 列表和顺序、每个数的字值、真实 cuff、准确 target 和全十词必须与实际首次 shared result 的 plan/CP 对应。首次 shared 可以是原 R409 `6a5f949a...` 或原 R441 `1ceda9d3...` 真结果；本 R448 调用同一 R441 shared 时输出后者真实 schema。因此可沿真实已产生的首次构造，不重新选 H。

`resources` 保原 `free_bytes_reserve`、`node_heap_mib`、`child_shutdown_reserve_seconds` 及五项 `stage_budgets_seconds`：`radial_replay`、`original_cuff_atlas`、`shared_field`、`metric`、`reach`。`metric` 参数完整为 eta / interval_bits / sqrt_bits / initial_angular_depth / max_depth / max_visited_cells；`reach` 参数完整为 curvature_upper / target_reach / active_depth / curvature_max_depth / pair_max_depth / interval_bits / sqrt_bits / max_cells / max_pair_nodes / max_pairs / cache_entries / max_constant_levels，以及三个 block 资源 max_block_nodes / max_union_cells / block_cache_entries。eta/K/tau 原准确有理文本由未来 caller 指定，本文没有选数。

`c_queries` 必须保原十一项：precision_bits、integral_absolute_bits、integral_relative_bits、analytic_guard_bits、integral_evaluation_limit、value_width_bits、integral_max_depth、inverse_max_depth、max_panels、max_nodes、budget_seconds。继续按原 R426 完整实际 source/radial ledgers进行同 C 精化，不用固定 cut box 冒全域 E。

每个 stage 都受同一原绝对截止与独立显式 stage cap；原 source/complete field 前置仍保，reach 不以 metric 成功为门。任何资源 stop、异常或未起均原样记。`procedure.json` 的“程序返回”不是 metric/reach 已过。

新场的 core→Phi、SE2、R249 重新计算。R443 的正密度与正确方向 `Theta_current_inverse composed with Theta_first`、公共 prefix u、tail 物理 r、帽 Cartesian 恒等/gluing继续作为同一抽象闭 target 的条件责任；不能把相同十参数/构造词当成相同材料系数表。本包没有执行已发表 R447 的准确材料 pullback consumer。

## 10　后闭必要与独立 held

五阶段必要命令：

```bash
python -u "$COMPUTATIONS/root_20261116_current_C_radial_resolution450_postsolve_necessary.py" \
  --directory "$R448_POSTSOLVE_OUT" --out "$FRESH_POSTSOLVE_NECESSARY_JSON"
```

该 source只把原 R441 necessary 的 procedure 名称/schema/SHA 注册为本文实际 producer；数学选择范围完全保留。完整 curvature/pair/block frontier、当前 single-rank、未付/错误、各 stage 原身份与 quiet均按原 reader；巨大成功账只完整身份与原范围，不能因多个块成功就认为全 root-pair universe 已付。单份 90000 字节规则保持，step outputs 为原 `postsolve_summary`、bytes、sha256、`postsolve_readback_complete`。

held 使用独立 wrapper：

```bash
python -u "$COMPUTATIONS/geometry_20261116_current_C_radial_resolution450_postsolve_held.py" run \
  --input "$R448_HELD_INPUT" --input-sha256 "$R448_HELD_INPUT_SHA256"

python -u "$COMPUTATIONS/geometry_20261116_current_C_radial_resolution450_postsolve_held.py" readback \
  --directory "$R448_HELD_OUT" --computations "$COMPUTATIONS" \
  --out "$FRESH_HELD_NECESSARY_JSON"
```

run input schema 是 `R448-current-C-radial-resolution450-same-job-held-after-shared-v1-input-v1`；必要 schema 去掉 input 后加 `-necessary-v1`。完整输入字段继续原 wrapper，且恰为：schema、postsolve_directory、postsolve_procedure_sha256、postsolve_input、postsolve_input_sha256、witness_plan、witness_plan_sha256、held、resources、out。namespace 与 computations 从实际被绑定的 postsolve input 读取，不重复供一个可不一致的字段。具体 `held` 参数为 active_depth、position_max_depth、position_radius_goal、interval_bits、sqrt_bits、max_position_cells、max_prefix_points、max_tail_witnesses；`resources` 恰为 held_budget_seconds、child_shutdown_reserve_seconds、free_bytes_reserve。全部真实 witness/完整同场/预算必须由未来明确来源给出，不从首末材料点位移代替全像 held。

wrapper 的 supported source/schema/input 三元只有本包新 postsolve；内部实际 R425 数学消费者仍为 `144da57a...`，不改 R441 几何 schema。只有 radial、atlas、shared 三前置的实际完成与同原时钟需要成立，metric/reach 结果不构成前门。step outputs继续原 postsolve_held_summary / bytes / sha256 / postsolve_held_readback_complete；frame 现明确为 `BEGIN_R448_CURRENT_C_RADIAL_RESOLUTION_HELD_NECESSARY` / 对应 END，避免冒旧 R441 wrapper。

## 11　清理、未执行与严格未付范围

本包所有 run/readback 都不删除、上传或归档 raw。成功 owner reader的 marker只证明自己的必要范围已读和真实 quiet，不能代替原 C/deep/来源/规则、后闭和 held 的必要读回。后继实际 caller必须把全部实际阶段、未起原因、原剩余 scope、各90KB状态和完整 quiet纳入其清理合同；没有整体 caller 就不能称已接完整工作流。

当前六源没有新增数学接受门，也没有把资料来源核验作为另一个必须先做的科学实验。必要读取失败和科学失败是不同记录；原父不成立、时间耗尽、容量不足、机器点不增加、native/FD/fullDN失败或未知输出各保本身范围。

本包没有扩 M，没有改变准确 C/DAG、十词、原有限 cut/far 或576 stages，没有证明有限 sampler 代表等于某个唯一准确 C 选择，也没有证明任一细化序列收敛。末场的准确 metric、reach、全像 held、含反射 deltaE、全相位/反射/帽/seam责任仍由真实新场的完整消费者分别给出；没有 actual450 数值、阈值通过或最终课题完成声明。

本次唯一允许的本地操作是纯文本读写、对应源全文差异与字节身份；未执行任何生成的科学源、metadata reader 或 loader，未做 import、AST、compile、fixture。所有后继 argv只是实际 API 合同，不是已经派发的命令。
