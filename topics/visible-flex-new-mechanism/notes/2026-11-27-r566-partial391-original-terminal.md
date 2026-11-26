# B030 partial391 自然终态：旧队列完整闭合，实际 56e8 保留

日期：2026-11-26 UTC；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

本收据只解析已自然结束的唯一原日志，不运行科学源码。新工作已完成原剩余 1128 个 bracket，复用原 391 个完成记录；随后有 8 次 metric 接受（含补完旧候选）与 2 次几何恢复接受。完整有限门上的实际 eta 从 `0.2277496382670385` 变为 `0.22244446600107332`。这不是固定度量等距族、全连续 reach 或课题完成声明。

## 原执行身份与规则

run [45900339926](https://github.com/Rogerhu12/math-research-public/actions/runs/45900339926)，job `140184283363`，触发提交 `b6343b326b0947772fc2635d679097dd718d374b`。API job 时间为 `2026-11-26T21:45:53Z` 至 `22:26:01Z`，自然 `completed/success`。
原 runner 实际 public pull 到 `f38d871291a53e583e862b10e5bddfc2ef8bc04d`，根 / 课题 README 差异都为空，blob 分别 `282e86b03385d3b6245ce7100ae2e2af7b103c2d` / `d0432faff569c8e9af7ed4809847e12880976c11`。private 实际 pull `8578f88879c33788bc66a79ef64cab56b2d36af0`，根规则 blob `5ba164843b1f5802184178a82d786264404873a3`，QUEUE 仍唯一属于本会话。
科学子进程 `21:46:26.200596Z` 至 `22:25:57.208902Z`，returncode 0；Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0。原科学累计新 elapsed `2370.2086491530004` 秒。

| 原对象 | 字节 | SHA-256 |
|---|---:|---|
| 完整 stdout | 18252593 | `fc574cd2d2e560fb983eb43165cf2311f4a330da22ff6d3d8787732383690b6c` |
| 逐字 FINAL JSON | 261842 | `5a78749c61c393f6d38443fa2f3eb8c8971d487bd5a046ce59c3832eb6a1d9a2` |
| 本次科学源码 | 55640 | `8c0a1300f75261b703cfeafd636e9b659f6436f67942ccb4e14d623c86dd8f38` |
| 已发布 request | 778681 | `fcd3b1d1d43dc46c1f0ddf695218e08f884caf4e1543a8d84d9167d32edbda4a` |

原输出有 23 个完整 checkpoint、22 次 backend start、21 个完整 Jacobian、21 个 outer complete、1 STOP、1 FINAL。没有 PARTIAL 记录；不能凭空继承上段已完成队列。

## 实际保留值与永久网格

实际 81q binary64 SHA-256：`56e8d87b39bf336a4cdb8c4106108396e735c498254a9e51c1a84c503904fb2f`。完整观测峰 eta 为 `0.22244446600107332`；uniform fine eta 是 `0.22244446047228628`，两者不能互换。物理盒、完整 working/coarse/fine/nested 和全部观测峰门均按原容差保留。

| 对象 | 个数 | binary64 SHA-256 |
|---|---:|---|
| 当前完整 coarse | 694 | `d5fe645dc40e3ac5136f553a609a1eb54e90507798a4cd23fa0a38713594c5b0` |
| 当前永久 required fine | 1390 | `345b946a64a98732feaa0936c97f79cacb470908c6cd6efeeb60eaf03aab6ec3` |
| 保留 q 真正已合格 fine | 1388 | `b387db869669487a4ad7b2c31d828afe7375d051d08826e1f479871d162c75f1` |

FFT coarse `1536`，fine `3072`；完整实际 peak orbit `1555`，工作行 `309`。physical pending 与 working pending 都是空列表。required fine 1390 与已合格 fine 1388 的身份严格分开，新网格必须支付自身资格；老 1388 报告不自动授予 1390。
实际 / 提议 trust 均 `0.3003387451171875`，最后 trust 决策未完成，未有新自然 OptimizeResult。工作 epigraph 是 `0.2224444760010733`，并非新的实际 eta。

保留 q 的原 finite 几何观察：

| 项 | 原值 |
|---|---:|
| `geometry_violation_max` | `0.0` |
| `mean_E_min` | `0.9986470520145753` |
| `mean_E_max` | `3.2211477158521453` |
| `det_min` | `0.8996910177755987` |
| `ball_radius_max` | `1.0114938734373362` |
| `abs_y_max` | `0.3926032549463192` |
| `z_min` | `0.02` |
| `curvature_max` | `16.38348926358271` |

曲率 attainer 为 `s=0.7593749999999999, theta=1.5707963267948966`。最后接受来自几何恢复：物理 violation 是 0，工作 violation `1.2355767450844546e-12`，完整几何 margin violation `1.2358994036509863e-12`，仍在原容差内；这不等于严格正 ball margin。
最后合格 eta 的 uniform attainer 为 `s=0.53203125, theta=5.939573610693202`；真实定位 metric-plus attainer 为相同 s、`theta=0.34366593739042184`。原 8886 个 candidate 全部完成、0 剩余 / unresolved，18 批，91422 次 objective，定位 elapsed `283.2560825640003` 秒。

## 全部真实接受与相位

| 来源/outer | phase | actual eta | q SHA-256 | working violation | geometry-margin violation |
|---|---|---:|---|---:|---:|
| 旧32的剩余队列 | metric | `0.22693934877011765` | `55e30fac8df3438d4e5d627f2c8ac9f867c67357db524e99589009bb8ad6ef36` | `0.0` | `0.0` |
| 0 | metric | `0.22616798763348003` | `c90811ad601aa097aeb61e6ede0e88c90d3e46729d4bd5574032a60c93563fab` | `0.0` | `0.0` |
| 1 | metric | `0.22546029550121888` | `a8050896ffcecf261601459e8654484d8a408fbbe86f3dcaa79d874949bd49bd` | `0.0` | `0.0` |
| 4 | metric | `0.22470127192027115` | `6be08ae39e1bd1283a46b0415cd653eaf28000540f9962495e5af8c656e28e52` | `0.0` | `0.0` |
| 5 | metric | `0.22401563845534614` | `af1da457170fdbec3ccab86056a5fdb8efdf998c1876d91f394a5b8b9f5b3c39` | `0.0` | `0.0` |
| 6 | metric | `0.2234315305612979` | `a0f540f780893e2bcf1eeb969718e49f9d533af519d2b18da51ec98202ac71be` | `0.0` | `0.0` |
| 7 | metric | `0.22274487760647815` | `878575807851bb0497159697895b283912392d67d206b4119463db413a64e433` | `0.0` | `0.0` |
| 12 | geometry_restoration | `0.2228412933032053` | `edd8ac63ceac395c2377d0fff4633289646a8f4d112027dbade8fd03f4a3e5fa` | `7.568381685252312e-13` | `7.563940793153812e-13` |
| 15 | metric | `0.22250223625979482` | `e1f870de24a19749e9c01d3c1f287011fecafa66e33a5f9b2c118981046f77a3` | `0.0` | `0.0` |
| 18 | geometry_restoration | `0.22244446600107332` | `56e8d87b39bf336a4cdb8c4106108396e735c498254a9e51c1a84c503904fb2f` | `1.2355767450844546e-12` | `1.2358994036509863e-12` |

原旧候选 `55e30…` 的 coarse/fine/nested 已在相同 q/原 scope 支付，只有原剩余 1128 个 bracket 是新定位。完整 1519 个峰闭合后，真实 eta `.22693934877011765` 才被接受。该接受计入本段 8 次 metric 中，不再回放整个队列。
outer12 为真实恢复接受，eta 从 `.22274487760647815` 上升到 `.2228412933032053`，不能伪记为 metric 下降。随后 outer15 的 metric 接受和 outer18 的恢复得到最后 q。全部接受选中实际 fraction 1；本段 0 次 shortened full acceptance、0 次后端自然返回。
21 个完成 outer 的 restart 原因：10 次 complete-fine-peak exchange preserved after epigraph lift、8 次 complete-fine actual-peak exchange、2 次 complete geometry restoration reached、1 次 required coarse-row exchange。工作库只控制局部矩阵，完整物理行没有删减；恢复相位移除的是当时不激活的 metric 工作行。

## 未接受末候选与未闭成本

最后完整候选 q `05f2636a42f37c3d1c19fe1845bbc510e8160a32388aa1082d99dfdb9679b38d`，actual eta `0.23759999314433572`，全 coarse/fine/localization 均完成，物理盒、working、geometry-margin violation 均为 0；因真实 eta 未下降而不接受。它不能覆盖实际 56e8 保留状态。
该候选原 fraction 1，working epigraph lift `.00023221547363572181`、coarse lift `.020391593265334712`、fine lift `5.589627959740051e-6`，complete coarse scalar rows `2464018`。e 抬升和原 raw SLSQP 数组分轨，不是物理改进。
最后 outer21 已建立 309 行的当前矩阵并开始下一次操作，STOP 为 `EndSegment: working-row scientific clock before next atomic operation`。21 个完整 Jacobian 共 `528.2540227650001` 秒、1164 个完整方向块，单次 15.11083738299999 至 37.30689301699999 秒；终态全成本方向块 1168，额外 4 个已付块来自未闭第22矩阵，不计成完整 Jacobian。全部未闭耗时仍在 elapsed / oracle counters 中，不能删除或免费复现。

## 完整本段费用

以下都是原 FINAL，本段 counters 与 prior ledger 分开，overlapping 子计时不相加冒充独立时间。

```json
{
  "accepted_metric_steps": 8,
  "accepted_restoration_steps": 2,
  "backend_histories_continued_after_shortened_full_acceptance": 0,
  "backend_natural_returns": 0,
  "backtrack_callback_proposals": 21,
  "backtrack_exhausted": 0,
  "backtrack_value_trials": 21,
  "backtrack_working_recoveries": 0,
  "backtracked_fully_qualified_acceptances": 0,
  "complete_coarse_epigraph_lifts": 15,
  "complete_coarse_scans": 65,
  "complete_fine_epigraph_lifts": 8,
  "complete_fine_scans": 20,
  "complete_localizations": 21,
  "fine_required_row_rejections": 8,
  "localizer_candidates": 53048,
  "localizer_completed_candidates": 53048,
  "localizer_point_objective_evaluations": 482651,
  "localizer_unresolved_returns": 0,
  "nested_quadrature_rejections": 0,
  "new_remaining_saved_brackets_completed": 1128,
  "new_restriction_observations": 0,
  "original_working_rechecks_after_lift": 40,
  "outer_completed": 21,
  "outer_started": 22,
  "paid_current_complete_selection_replays_avoided": 1,
  "physical_exchanges": 16,
  "required_row_rejections": 1,
  "source_completed_brackets_reused": 391,
  "source_paid_full_fine_and_nested_reports_reused": 1,
  "source_saved_localizations_completed": 1,
  "source_saved_trial_fully_qualified_acceptances": 1,
  "working_complete_jacobians": 21,
  "working_direction_blocks": 1168,
  "working_epigraph_lifts": 17,
  "working_exchanges": 20,
  "working_jacobian_seconds": 528.2540227650001,
  "working_value_keys": 83,
  "working_value_rejected_callbacks": 0
}
```

原 oracle ledger（每个 live/retired oracle 只合并一次）：

```json
{
  "FFT_states_prepared": 2028,
  "diagnostic_uniform_FFTs": 0,
  "exact_core_arclength_points_prepared": 2295207,
  "nonuniform_points_summed": 2361031,
  "oracle_constructor_seconds": 62.47960638200004,
  "oracle_constructors_completed": 245,
  "point_evaluations": 487120,
  "point_parameter_directions_evaluated": 3151220,
  "point_seconds": 1460.6308679570336,
  "point_set_seconds": 123.4931473530001,
  "point_sets_prepared": 482922,
  "point_subsets_created": 4870,
  "point_values_evaluated": 2746540,
  "prepare_seconds": 581.6017499519909,
  "primitive_Fourier_fields_prepared": 18252,
  "uniform_geometries_prepared": 2028,
  "uniform_points_gathered": 385509
}
```

本段之前原已知科学链下界 `12359.003476909998` 秒，加本段后下界 `14729.212126062998` 秒；较早被外部截断而未报告的科学工作仍未知，不冒充精确总成本。原 live counts 终态已经折入，`active_working_counts_not_yet_retired=null`。

## 具体继续输入

继续的唯一物理参数是上述实际 56e8，全部694 coarse /1555 orbit /309 working /1390 required fine和真正1388 qualified fine从逐字 FINAL载入。没有待续 PARTIAL、没有原391或1128队列再跑。新1390资格由新scope支付；原15+8等已完成接受和所有旧Jac费用只进入历史账。原未输出BFGS矩阵不能伪造恢复。

完整原 FINAL 是下一次继续所需状态；原 stdout 不作为仓库数据表重复提交。本地只做日志、JSON、字节哈希和源码解析，没有科学求值。
