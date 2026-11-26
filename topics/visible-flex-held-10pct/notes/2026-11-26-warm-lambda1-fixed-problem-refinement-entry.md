# 仅由真实 λ1 暖场触发的固定问题精化入口

会话：Astra-held10-06bbeb39-20261126 / fixed_metric。状态：**新可执行入口已保存，尚无 λ1 accepted 暖场，因此没有执行任何本入口的 BVP 或场比较。** 已做语法、命令行入口检查；两个仅内存的拒绝检查确认较小 λ 和旧 design 身份在任何子进程之前被拒绝，没有伪造求解输出。没有修改已就绪的 warm step/model/factory/compare 源。

新增 `scripts/resume_20261126/warm_lambda1_refinement_pipeline.py`：

```sh
python scripts/resume_20261126/warm_lambda1_refinement_pipeline.py \
  --repo /path/to/math-research-public \
  --work /path/to/current-runner-work \
  --source-run /path/to/current-runner-work/accepted-lambda1/run.json \
  --outdir /path/to/current-runner-work/lambda1-refinement
```

## 触发条件与固定数据

必须是 `model_kind=warm-supported-material-phase-fixed-metric`，run 和 warm_definition 两处 homotopy 都字面为 1；原 solver/raw success、完整 finite_linear_candidate_pass、physical C2 导出、实际 RMS、normalized/physical BC、实际 component/operator metric 全部通过。角审计不能低于原 `16*(3M+1)`。真实 run/raw/physical/port/origin 的 SHA 核对后才启动子进程；较小 λ、旧 design 参数、错误或中断审计都不触发任何 BVP 或 port export。

完整 warm_definition（含冻结 support b*、源定义、当前 λ=1、相位尺度）、actual frozen_profile、物理尾背景/切口、材料角图、gauge、mean1168、BC normalization=.02 逐项相等。p0 仍为 log(q_aux/gauge)，未把 q_aux 改回支撑幅度。三个子入口都会把此次动作记为同 λ refinement，design_continuation 为 false。

## 默认三档

设实际 λ1 源的频率数为 M，默认档为 M、M+8、M+16；`--mode-levels` 可明确给三个数，但首档必须为源 M，后两档必须严格增加。没有硬写源必须 M24，较高 M 源也沿用同一模型。默认 max_nodes=6000、Jacobian batch=8，不在此入口改变原域门。

| 档 | 模式数 | RHS 角节点下限 | 初始物理径向加密 | tol | bc_tol | physical_bc_tol |
|---|---:|---:|---:|---:|---:|---:|
| 1 | M | 64M | 2 | 1e-8 | 1e-9 | 约2e-11 |
| 2 | M+8 | 64(M+8) | 1 | 1e-9 | 1e-10 | 约2e-12 |
| 3 | M+16 | 96(M+16) | 1 | 1e-10 | 1e-11 | 约2e-13 |

如果源已经有更紧的 tol/BC 门，继续保留更紧值，不放宽。每档角 metric 审计使用本档原 floor 和二倍 floor，mean 仍为 1168；新模式的线性端口由原 exporter 生成，只允许 modes/quadrature 的数值分辨率改变，其实际物理 parameters/cut 必须与源相同。任何一档真实求解或审计不过，就以该真实结果结束本 pipeline；不把失败场登记为 accepted，也不在本固定问题精化入口切换 λ 或物理参数。

## 实际场比较与输出

每个 accepted 返回都与紧邻前场调用已就绪的 `warm_fixed_m3_compare_c2.py`：第一个比较是源 M 的数值精化，后两个是两个真正的 modal increment。三个比较使用同一组角节点，默认是最终 M+16 的原 floor 及其二倍；径向使用各真实网格、全部中点、结点左极限和共同均匀点。输出完整六个 Cartesian jet 的有限采样差、真实 mean1168 primitive 的两种正 Gauss 阶数差，以及零扩展 phase d 的 exact rational 加权 l1 差。

末尾报告两个 modal difference 是否出现数值下降，逐 jet 给比值，保留各档实际 metric 值。不能将同 M 的数值改进与第一条模态差混作两次谱收敛，也不能把三个有限档或两个下降比值写成 C2 Cauchy 定理。所有 continuous_C2_bound / same_limit_core / complete_surface 标记仍 false。

`pipeline.json` 保存完整小记录；`summary.json` 给 worker 的 status/stages/progress/result/error，主动去掉 raw 参数向量、长 source signature 和有理数分子分母，只留实际节点/RMS/门/差值与文件 hash。这样不会再因把大诊断塞进 worker 请求而整段超过输出预算。

## 与实际 nonlinear DN 的边界

此入口仍是当前暖 **linear DN** 问题的固定 λ 精化，明确不能当作完整闭面验收。`actual_tail_requested` 或 `original_actual_nonlinear_tail` 的输入在入口处拒绝，避免静默把真实尾换回线性端口。

将来暖真 DN 须另建入口：先用 `warm_fixed_m3_model.load_model` 恢复 fixed=True 的暖 Base，再接原 TailMixin/真实尾 worker 和原外迭代。H、slope、BC_J 使用原 gauge·Y；p0 不能送进旧 portable design 的 δ 增量槽。原 TailMixin.seam_audit 用 n=max(512,64M) 计算均值；这对 M24 是1536，不能冒称本图固定 mean1168。新入口应保原非零模角审计，并另用 basis(1168)+velocity_s 计算实际 mean/mean_s、相应接缝差。该接口点已同步 actual_tail 与 seam_geometry；尚未写成一个不存在的暖 trueDN 接受结果。

最终全时族必须依 R23/R54 对同一完整基准 Cartesian 图施加材料角平移与旋转，保持其同一 mean1168 primitive；不能在每个相位重新对固定节点求均值，有限节点求积不具有任意相位平移不变性。这里的比较都在同一基准图上。
