# 同一冻结 g 的幅度保护求解与真实精化接口

2026-11-26，Astra-larger-e4e2a2bf-20261126 / construction。

这是 [固定均值 g 数值管线](2026-11-26-frozen-mean-target-numerical-pipeline.md) 与 [完整 D/L 幅度保护入口](2026-11-26-held-amplitude-protected-mean-design.md) 的独立完整组合实现。所有已有已刊源、已排 moving-mean 分支及其身份都不改。本入口只在选定实际可接受设计后使用同一个已经冻结的 R684 metric manifest；**当前并没有这条固定 g 幅度精化的实际运行或收敛结论**。

## 1. 两种“固定”不能混淆

$g_*=E_*(s)ds^2+C_*(s)d\theta^2$ 的原父场、N*、rho*、有限均值权、整个连续径向公式及帽自身诱导 metric 已固定；当前场的所有原角均值残差都必须恢复。仍使用 `FrozenMetricOperator` 的 $J_*=D_*(s)J$、$J_*^T=J^TD_*(s)$，没有 moving-mean 投影，也没有将 R688 的均值扣除挪过来。

幅度预算 Dmarked/L/Hmin 也在本分支固定，但相位见证 $p=(0,1+\sum c_j,0)$ 来自**当前**待求场，随全部自由 core 系数变化。冻结 g 不等于冻结 p。原完整幅度 helper 继续支付 $dp=\sum\delta c_j$ 到所有原自由 core 首块，随后过同一 $T^*$；每个 trial 重新从 prepared.current core 求 r0。这个依赖与冻结父 rho* 互不替代。

同一个源保留固定目标的全部原变量、正权 Gram 行、原 H² 母范数、完整固定 K00 coarse Gram 和 R685 v5/显式 v3 分支；原几何C逐条作prefix，额外幅度行与全已知真筛完全使用已核的两个共用小源。原 `.992/.025` 筛仍只是必要曲率筛，不替代 reach 证书。

## 2. 完整实现范围

`fullclosed_frozen_metric_amplitude_qp.py` 的完整来源是 fixed driver `2020d687…` 与完整 amplitude driver v2 `970f03ad…` 的声明组合。完整源独立发布，报告 schema 为 `complete-fixed-frozen-target-with-held-amplitude-budgets-v1`。原固定 target identity、target materialization、common-parent-measure 比较、目标五输入显式重绑定及源repo相对路径恢复全部保留。

原point/body读循环直接把同一实际 F 交幅度 Accumulator。完整stage bitset与expected/actual永久任意地址集合一起核通过；同一trial曲率和幅度都通过才可接受。所有新幅度极值与selected地点永久保存，reject后不删除。新增记忆后重新读当前父时，同时复查曲率和幅度才启动新的可行QP。非finite物理/曲率读数明确incomplete。没有增加自动梯度fixture，没有接SOC，也不伪称完成连续幅度/全域reach证明。

固定目标预条件仍调用 `prepare_current_frozen_preconditioner`：只用 $K_{00}$、fixed_scale与当前固定目标残差Hessian，全部原均值约束保留。共享的 amplitude rows只是追加C，不改变A、真梯度、Hessian、原μ单位或目标。每方向记录原/新增行数、两份row-cache实际bytes、真实J/J*计数及v5/v3状态。

## 3. 同网格继续求解

先按原 `frozen_mean_metric.py` 命令冻结选定的真实设计成员。将固定数值阈值显式赋给 `FLEX_FIXED_TARGET`；不能把设计5e-7筛选阈值改称README原求解容差。以下父必须与给出的当前carrier/node/eta匹配；已精化父要用其真实输出，不能继续照抄885。

```bash
python "$FLEX_REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_frozen_metric_amplitude_actions.py" \
  --repo "$FLEX_REPO" --work "$FLEX_WORK" \
  --parent-report "$FLEX_PARENT/report.json" --bundle "$FLEX_PARENT/final.npz" \
  --carrier "$FLEX_WORK/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
  --node-report "$FLEX_WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --scalar-input "$FLEX_WORK/fullclosed_solver/data/pulse-a5-complete-base.json.gz" \
  --manifest "$FLEX_WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four-witnesses-compact.json" \
  --frozen-target-manifest "$FLEX_WORK/frozen-mean-g/metric.json" \
  --eta-start-node 885 --lambda-value 1 --angles 2048 \
  --marked-diameter-budget 4.2 --witness-lower-budget .9 --amplitude-height-floor 1.01 \
  --damping "$FLEX_DAMPING" --directions 2 --maxiter 64 \
  --qp-atol 0 --qp-rtol 1e-6 --active-rows 192 \
  --reach-safety-factor .992 --active-band .025 \
  --spectral-p 4 --spectral-epsilon .001 --spectral-scale .05 \
  --target "$FLEX_FIXED_TARGET" \
  --outdir "$FLEX_WORK/fixed-mean-g-amplitude-first"
```

默认开启 R687 centered Phi−constant；这只是稳定scalar计算。全部 old Phi仍保存。`--coarse-preconditioner none` 显式走原完整fixed-target v3，不能将其状态冒充PCG加速。若父已有幅度预算，三个固定预算必须逐值相同；数值真筛自己读取当前父，不自动继承父连续证明。

## 4. R676 transfer-only 后对同一 g、同一预算求解

```bash
python "$FLEX_REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261126/refine_frozen_metric_amplitude_actions.py" \
  --repo "$FLEX_REPO" --work "$FLEX_WORK" \
  --parent-report "$FLEX_WORK/fixed-mean-g-amplitude-first/report.json" \
  --bundle "$FLEX_WORK/fixed-mean-g-amplitude-first/final.npz" \
  --carrier "$FLEX_WORK/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
  --node-report "$FLEX_WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --scalar-input "$FLEX_WORK/fullclosed_solver/data/pulse-a5-complete-base.json.gz" \
  --manifest "$FLEX_WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four-witnesses-compact.json" \
  --frozen-target-manifest "$FLEX_WORK/frozen-mean-g/metric.json" \
  --radial-factor 2 --directions 2 --maxiter 64 \
  --outdir "$FLEX_WORK/fixed-mean-g-amplitude-refine01"
```

这里继承真实父的固定 target threshold、p/epsilon/scale、qp atol/rtol、scalar evaluator、coarse选择和幅度工作集参数；默认μ来自其actual final_damping，若显式另给则记录。已有幅度父的三预算不许默改；首个原父尚无幅度字段时，必须通过CLI显式给三个预算，不能凭空填合格证。

完整父memory先收集再交 R676 **transfer-only**，不运行原g0/p8 readout。新完整求解取实际transferreport的refined_model.eta_start_node/lambda，所有原节点/角点/正权和exact永久地点保留。目标N*、rho*及公式不动。fine自己测度的Phi单列；只有从fine残差数组提取的同父literal测度Phi可与原父相减。新current carrier/node来源与原冻结target原始五输入角色分开。

raw目标输入在其他job需要重建相同bytes时，五个 `--target-*` override 与baseline相同，refiner继续转交；不能用fine/current数据冒充原被冻结的对象。若fine初始低于停止阈值、零方向退出，仍报告zero_direction_exit，不推断误差持续下降或达到原求解floor。

## 5. 独立严格报告归因

```bash
python "$FLEX_REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_frozen_amplitude_report.py" \
  --repo "$FLEX_REPO" \
  --report "$FLEX_WORK/fixed-mean-g-amplitude-refine01-solve/report.json" \
  --out "$FLEX_WORK/postprocess/fixed-mean-g-amplitude-refine01-summary.json"
```

专用reader绑定新完整body、固定wrapper9d644、fixed coarse a531与两幅度源，严格收新schema。它核每条实际方向的旧/新行数和完整true acceptance，不借旧R688 binder。摘要含 frozen target ID/manifest SHA、target N*、current J/M/N、同父测度读数、显式数值target和零步、实际amplitude/curvature筛、所有原位置计数、真实峰值内存。`sampled_minimum_witness_distance_squared` 仍不能当全域距离下界。

R689严格连续Gram核与同场完整first/K/far/marker/reach仍需实际执行。此源的存在不说明已有可冻结合格解，也不说明实际固定g精化已通过。

## 6. 完整源与静态验证

| 源 | Bytes | SHA256 |
|---|---:|---|
| fullclosed_frozen_metric_amplitude_qp.py | 73253 | 859ceb836378c3140a0d27877987f3d06546aae2baee0ef316403d3f332d911b |
| launch_frozen_metric_amplitude_actions.py | 19620 | d73ec177827fd420153dd95ceafbc3601eeb0af6e3b0c89b7b2d372c021e41e1 |
| refine_frozen_metric_amplitude_actions.py | 16270 | f5d2caaab5b73483c2f09cda8321854f9f39d06c7e28bcf4670f589438751fee |
| read_frozen_amplitude_report.py | 10920 | f119d9960a0e6de381b6a7ab93581a1dd785db258a6b7cd2a72546ea62c979af |

冻结 wrapper 与 fixed moments 身份不改；幅度 helper/screen 使用修复重复 `sign` 关键字的独立 v2 文件（旧 v1 保留）：frozen wrapper `9d6440ab9f86cfe5312b78643e704a3ec861f2c5b6fd45047461af92eca81d28`，fixed moments `a531818d75040ff571ad1249eecb3c18f7341284d1cdd86d2032b0f8f4ef9f63`，amplitude rows `d494f92a3d212c40c8b602588c8cfe74f01ff332f116992ffca6469b3978ad8e`，amplitude screen `e6be35e97702e4185f29fb8f9b7c326fd62083cb4027880956aacdf8b0ba296f`。

四完整源无尾空白，AST/compile通过；纯 `--print-command` 155argv、76flags全与新driver解析器匹配。geometry独立静态核固定target/J/J*/K00、全known地址真筛、起点/末态通过路径，无阻断问题；未科学执行或测定性能。

这份本次刊载的 fixed-amplitude 实现采用 `held_amplitude_inequalities_v2.py` 与 `held_amplitude_screen_v2.py` 默认路径，完整固定 g、预算和行公式均未因 v2 接口修复改变。具体来源见 [幅度行记录 v2 修复](2026-11-26-amplitude-row-record-v2-repair.md)。
