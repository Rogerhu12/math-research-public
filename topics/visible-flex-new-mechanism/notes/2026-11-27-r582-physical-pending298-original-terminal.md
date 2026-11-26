# R582 normal298 自然终态：实际 f60 材料上的 59a4 完整有限资格

日期：2026-11-26 UTC；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

新公开运行自然结束。实际保留97q的完整 finite eta 降到 `3.838285782595128e-05`，但本次构造出的材料场 SHA 是 `f60be03b0af36d5d182f21860fe69cef80439c12bb23562d63dc2b57648bf52c`，不是上一段 `0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991`。本次初始和每次接受均在同一实际 f60 对象上支付完整 fine 资格，不能把 q 或旧连续证书跨场贴标签。

## 原执行与唯一日志

run [45901312947](https://github.com/Rogerhu12/math-research-public/actions/runs/45901312947)，job `140187488430`，触发提交 `98ded25f6b56ef1899efec271406361453217575`。job `21:54:44Z` 至 `22:34:47Z`，自然 `completed/success`。runner 子进程 `21:55:13.130857Z` 至 `22:34:44.763500Z`，returncode0；原新科学 `2370.257524993` 秒。
实际 public pull `f32fbfcb5884ab2d866f08641fe60b84ea45a38d`，根/课题 README 空差异，blob `282e86b03385d3b6245ce7100ae2e2af7b103c2d` / `d0432faff569c8e9af7ed4809847e12880976c11`；private 实际 pull `b4c273575d272827ad3581d46994612fb0e54292`，根规则 blob `5ba164843b1f5802184178a82d786264404873a3`，QUEUE 本会话。Python3.12.14、NumPy2.3.5、SciPy1.17.0。

| 原字节对象 | 字节 | SHA-256 |
|---|---:|---|
| 完整 stdout | 6455101 | `bde7498af6ab06b89d32d4657ce79458ee70aa839f705869cc7a266ad0c401dd` |
| 逐字 FINAL JSON | 479059 | `8b6f57b0a4d0f212fe378c10ec563e350efa7ca2b0e7d958912715e25ce42e15` |
| 逐字 FIELD JSON（含观察节点身份） | 116334 | `ec601fb7caa9285acf8e5b7a611b20d994afcea561ef8bbfbf32d9a8dd9451d9` |
| 原 wrapper | 11812 | `695104e5f0c664a06efac69bb461d6e1065c2d000cd99c591d8cf5c661ca5394` |
| 已发布 request | 399393 | `dcf95705842e8dc00b5cca4b8f1ff7fa4733462a840833bbe410affc57ff582a` |

有1个FIELD、1个START、1个BACKEND_START、14个PROGRESS、1个OUTER、1个CHECKPOINT和唯一FINAL。无自然OptimizeResult，无新方向检查，无旧七点诊断回放。

## 新材料身份与首次完整资格

本次和 R623 首次 K-only 的实际重建都观察到 f60：62878 个 endpoint，DOP853 tail RHS 960932，160 段；旧0d的62878个endpoint/RHS960944不能据相同数量认成同一场。这里不猜测硬件原因。原recipe未保存真正全部端点/分段dense状态，只有精确recipe和小口数据，不能用未存产物声称原0d可以按字节还原。
`START.initial_scan_reused_at_identical_p_q_and_complete_fine_grid=false`。在同一新 f60 对象，原14d1q重新支付 **16149×3072** 完整扫描，原uniform eta `4.262265974823864e-05`、physical violation0、working violation `9.778231549115168e-10`，scan `47.239016649000035` 秒。新coarse cover eta `4.2622659748445396e-05` 与之不同，不混为同一量。
原所有11100 fine点、原2个pending的实际float位置、新材料2956个活跃endpoint及必要midpoints等精确并集保留。endpoint threshold `1e-12`、最大未选endpoint jet `7.838692722655e-13` 只是原选点观察，不是连续误差证书；全62878 endpoint定义仍在对象中，没有删去。
原始未合格warm raw6f82仅作为后端初始点。本段第一接受是quarter-step f444，而不是把原0d上的14d1或raw6f82报告直接移交新场。全部新模型共享这一个 actual material 对象，未另造一个近似场用于fine。

## 全部14次真实callback结果

下表每行完整fine都是16149×3072；work-V为完整fine工作几何违反，原物理/工作门按原容差执行。raw backend、独立物理assessment和保留best分轨。

| callback | 接受 | fraction | 实际fine eta | fine work-V | assessment q SHA-256 |
|---:|---|---:|---:|---:|---|
| 1 | 是 | `0.25` | `4.259381122671913e-05` | `6.714147007466642e-10` | `f4442aceaa4baa67e3e93947c6c45b9cf6760907c0d979fa72ff1bd68e9e7729` |
| 2 | 是 | `0.5` | `4.253957428886674e-05` | `3.909298431845065e-10` | `b784e4440050781febfe75bf6b101457c77472c4a43396694ba91a8cd8fe2366` |
| 3 | 是 | `0.5` | `4.2500676824255126e-05` | `1.4333533492061346e-11` | `6abf1e12481aa0b689476296b08b79ae8939e89fbf03c20519e1c51b3bbce156` |
| 4 | 否 | `0.5` | `4.2501549680773465e-05` | `0.0` | `6f71ed570c59e296503288a260970c4ce183c38b01547d5b62cb00479b5d72af` |
| 5 | 是 | `0.5` | `4.244246828699616e-05` | `2.773062223425382e-09` | `5797ebd860ee18257bb8b794df3ddbdabd904d81f7795fbc9edd9fdb709619ad` |
| 6 | 是 | `0.5` | `4.1996103130577086e-05` | `1.9081219928759885e-09` | `0064dd13641dd0e91d5209aecc6461e54fdd5ccb69c3557473041ff5db8357dc` |
| 7 | 是 | `0.5` | `4.122390011116777e-05` | `0.0` | `1311ecb666096761ac56a25a39f0eafa7b0b64f0027fc12502e0bc490257c9f5` |
| 8 | 是 | `0.125` | `4.122210449778854e-05` | `0.0` | `ef9a74fb81154d25c360a45e1094c003a1338c1135ad8c002caa72f3037eb8b0` |
| 9 | 是 | `1.0` | `4.033460391194072e-05` | `0.0` | `94bd300aba98211b4cd6cde6f8d8e763527c6c59091ce16db9a68e01803d48fd` |
| 10 | 是 | `0.5` | `3.9488851756268136e-05` | `0.0` | `3d6865d4b3a6a6feaa37034031630fa4491b0b399c6adba49454ca7513bd2324` |
| 11 | 是 | `0.5` | `3.9359170127088544e-05` | `0.0` | `be9085fbb3cce114ee00ac6440e087957e69ca643beedeff92fd056d6c7ec11f` |
| 12 | 是 | `0.5` | `3.893695887544919e-05` | `0.0` | `7eb5d214ea95d3469ac02b3293dac35dac6353b4d1190789688447b9f3429810` |
| 13 | 是 | `0.5` | `3.838285782595128e-05` | `0.0` | `59a4ba766a9450509bcbd539639503e8a67d9dc0a98c6c3b63f59879c29a7b45` |
| 14 | 否 | `1.0` | `3.776290107081685e-05` | `2.6502573901020753e-05` | `d613ff403c21de80b2f4366214728467b9d1316b8695ecf96d17fb8e6d3e70ba` |

12次真实 metric 接受，0恢复接受。raw backend违反范围 `2.5490653467393507e-7` 至 `3.238036566965887e-5`；真实fraction有1/8、1/4、1/2和1。14次独立e抬升范围 `5.200315045174753e-8` 至 `1.489128617812146e-6`，全部先满足原完整coarse物理组，再付全fine门；e的下降或抬升不当作物理进展。
callback4 虽工作物理可行但eta未严格下降，未接受。callback14 actual fine eta `3.776290107081685e-05` 比保留值更小，但 working violation `2.6502573901020753e-05`，正确拒绝并交换全部13个新径向证据。

## 真正保留场、网格和观察

实际97q SHA-256：`59a4ba766a9450509bcbd539639503e8a67d9dc0a98c6c3b63f59879c29a7b45`；`p=.181`、epsilon`.0010000000000000009`、实际/计划/下一trust均2。该q明确属于本次f60；资格fine16149，当前下一requiredfine16167。FINAL的布尔 `qualified_on_this_fine_grid=true` 只在保留记录自身 scan 的 grid identity 上读取，不把它扩展到之后新构造的16167。

| 对象 | 个数 | binary64 SHA-256 |
|---|---:|---|
| 已付资格 fine | 16149 | `2bfc3537692283311887978a96fba44fc95dfd6bb2fea6cdaae80440d1cd2e31` |
| 当前 adopted coarse | 311 | `f9346fa13311a0fd0fc8bc17bfde0d3f30c08b93aeffb618bc037c2de7916736` |
| 当前 required fine | 16167 | `4240c3ba1d2959ea4c5f81139ead8a1a6e1f218f6b903df1eca94156361c71fd` |

coarse角1536、fine角3072；最后13个pending已采用为311 coarse，当前pending空、proposed=current311，角升级false。第二outer已进入网格构造，clock在其完整资格前结束，没有第二次backend start；原已付资格只到16149。

| 原保留scan量 | 值 |
|---|---:|
| `eta_max` | `3.838285782595128e-05` |
| `geometry_violation_max` | `0.0` |
| `working_geometry_violation_max` | `0.0` |
| `mean_E_min` | `0.6183984941320411` |
| `mean_E_max` | `1.173935286634088` |
| `det_min` | `0.6183856130301781` |
| `ball_radius_max` | `0.7750457629579252` |
| `abs_y_max` | `0.39255675238317717` |
| `z_min` | `0.02` |
| `area_min` | `0.21999999999999997` |

eta attainer `s=.7171875,theta=2.56072526191043`；曲率观察 `16.452569169073723`，attainer `s=.8715482369363079,theta=4.71238898038469`。该fine观察没有全径向/全角/reach认证。
同一次已付几何块累积的旧冻结圆参考范数观察为 C0`.0279108848014526`、C1`.2030308608394088`、一阶norm`1.1906353931957538`、法向投影差`.07623702187505288`、帽平移差`.022091312964010013`；这是对旧原始圆参考的采样结果，不是新同mean圆的连续界。没有为这些观察新增几何或AD求值。

## 最新mean改变与后继连续几何的身份

与旧a237相比，mean q64:72、q72:80和h96改变；另外首个新增tail-u坐标q80也改变，q80不属于mean。literal参数差的最大绝对值依次为 `.004476159711271022`、`.022919795585600533`，q80变化`+.004234700307509973`，h96从`.6942718843124706`变成`.6967930185437883`（差`+.002521134231317723`）。这些只是已存JSON坐标的比较，不是局部科学求值。
因此后继应固定最新59a4，按同q重新认证完整mean圆参考，再计算自身全C0/C1和R623K；旧a237 meanρ/D和旧0d δ/α均不消费。如果一次实际重建仍为f60，只有相同59a4的原16149物理观察可以复用；若再次异场，必须同一构造对象付全原fine和连续几何，不能另造材料或仅换SHA。

## 末后端与全部费用

末raw/assessment q是 `d613ff403c21de80b2f4366214728467b9d1316b8695ecf96d17fb8e6d3e70ba`。raw e `3.705887630822819e-05`、raw完整coarse violation `4.596590863705126e-07`；独立抬e至 `3.7518535398151414e-05` 后coarse物理可行，fine仍失败，不能替换59a4。无自然OptimizeResult、无后端内部数组恢复。

以下原终态成本逐项保留；各模型/field/观察计数有重叠，不能相加冒充互不相交的科学工作。

```json
{
  "R604_observation_counts": {
    "observed_radial_angular_points": 749650944,
    "reference_radial_nodes_evaluated": 244027,
    "reused_geometry_blocks": 1919
  },
  "counts": {
    "accepted_metric": 12,
    "backend_callback_invocations_including_explicit_terminal_read": 14,
    "coarse_feasible_assessments_without_metric_promise": 14,
    "complete_fine_radial_blocks": 1919,
    "complete_fine_scans": 15,
    "completed_backend_Jacobians": 13,
    "completed_backend_direction_blocks": 169,
    "completed_backend_value_evaluations": 70,
    "completed_callback_current_complete_row_checks": 14,
    "completed_optimizer_callback_scans": 14,
    "completed_outers": 1,
    "exact_epigraph_lifted_physical_candidates": 14,
    "fine_radial_points_evaluated": 244027,
    "natural_backend_returns": 0,
    "new_physical_backtrack_row_assessments": 29,
    "physical_backtrack_halvings_taken": 15,
    "source_unqualified_warm_trial_entries": 1
  },
  "final_resonant_field_counts": {
    "continuous_profile_radial_values": 3166,
    "dense_tail_radial_queries": 62443,
    "height_QUADPACK_RHS": 235893,
    "height_cache_hits": 375,
    "height_queries": 3166,
    "material_Hermite_radial_queries": 32925,
    "material_raw_knot_candidates": 63045,
    "new_dense_tail_RHS": 960932,
    "new_dense_tail_segments": 160,
    "new_dense_tail_transfers": 1,
    "new_exact_core_forward_RHS": 2510,
    "new_exact_core_forward_calls": 1,
    "new_material_Hermite_endpoints": 62878,
    "new_short_tail_backward_RHS": 206,
    "new_short_tail_backward_calls": 1,
    "radius_only_reference_queries": 32925,
    "resonant_field_queries": 436,
    "uncomputed_inner_tail_query_points": 0,
    "underflowed_nonzero_jet_components": 274689
  },
  "final_stable_evaluator_counts": {
    "residual_preparation_cells": 62877,
    "stable_material_radial_queries": 32925
  },
  "new_model_counts": {
    "attempted_geometry_AD_blocks": 169,
    "attempted_geometry_value_calls": 1961,
    "attempted_model_grid_constructions": 4,
    "geometry_cache_hits": 43,
    "geometry_parameter_direction_points_requested": 577195008,
    "geometry_spatial_points_requested": 846231552,
    "model_radial_points_prepared": 32925
  },
  "original_model_new_counts": {
    "actual_weight_calls": 1023374,
    "background_grid_constructions": 0,
    "background_radial_points": 0,
    "inner_RHS": 0,
    "linear_least_squares": 0,
    "mean_control_candidates": 0,
    "outer_RHS": 960932
  }
}
```

本段共15个完整fine=1个新场baseline+14个callback，244027个径向点/1919个块；13完整Jac/169方向块/70值求值，current backend未折叠计数null。4次model-grid构造、最后未闭新网格/资格的工作仍在2370.257524993秒及实际模型计数中。没有把它虚报成第二个完整outer或免费续算。
prior_cost_ledger 的全部历史条目保持，包括上一normal279 2375.001235837秒、12完整Jac和额外6个方向块；本段新科学单列，不用新字段覆盖旧账。所有未知较早工作保持未知。

本地只解析唯一原日志、JSON、字节哈希、原源码；没有导入科学程序或重复原诊断。完整FINAL作为下一次继续的必要输入保存，原大stdout及可重建端点数组不进入仓库。
