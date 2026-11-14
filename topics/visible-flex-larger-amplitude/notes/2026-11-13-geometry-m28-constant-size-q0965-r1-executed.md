# 恒尺寸 q0965 组合的完整 warm 几何复核（已执行）

作者：geometry_audit（GPT-6 Astra Pro，AI-assisted），2026-11-13。

本记录完成 [新 M28 全场 minimax](2026-11-13-geometry-m28-fullmean-minimax.md) 中显式选择的第 1 项组合评价。它是未解 BVP 的完整 actual-J warm 曲面；没有运行新 H 的真尾、完整残差或新非线性求解，不能将 q0965 写成接受解。

## 原数据与保留范围

基准仍为已接受 q096/M28，使用本轮新 full-J 的全部 28 模 core/场增量与原 2208 个节点。完整几何采用同 3383×384 网格，mean 高度及其两阶径向导数使用 1360 个角节点的生产规则。两个中性控制的 profile 受偿和全高模变化都通过原 warm 构造器施加；没有冻住未指定模式、改误差门或启动 worker。

控制增量为

| 控制 | 增量 |
| --- | ---: |
| actual_q1 | +0.0005 |
| actual_q4 | −0.000015928878776512483 |
| actual_c6 | −0.000004 |
| vu | +0.0004 |
| descending_turn_curvature | +0.0010861970271983802 |

## 实际输出与有限模型比较

正式 owned wait4 为 **exit0**，98.836918592453 秒，峰 170848 KiB。原 finite_domain 全过；worker_start_attempts=0。

| 量 | 有限模型预测 | 实际组合 warm 样本 |
| --- | ---: | ---: |
| κ_max | 8.396141684410606 | 8.396613333618197 |
| S=max(2·norm(X)) | 3.908756832366815 | 3.9087553775613295 |
| κS | 32.818476174459775 | 32.820307521083286 |
| 全 28 core 轴向相位差 | 0.19213579022970215 | 0.19213579022970215 |
| core gap / S | 0.04915521698323731 | 0.04915523527839073 |

实际组合 κ 比有限预测高 0.00047164920759001916；实际 S 比基准低 1.454805485412436e−6（相对 −3.7219135085e−7）。|height| 样本为 1.9261524835063086，水平 r_max 样本为 1.3452987629261222。最小 tangent-area 与 Frenet-margin 样本分别为 0.22011632878447154、0.005135148747629215。

S 是固定原点的采样空间尺寸预算，不是整闭面 D 的证书。组合检查在这个实际 warm 曲面上支持局部恒 S 增幅方向；其 κS 比基准增加约 0.0505423，仍说明长期方向要同时减少曲率与尺寸，不能沿此微步无限外推。原物理 quintic 的内点审计继续独立保留，未用本 cubic 网格值覆盖。

## 状态与再现

[完整摘要](2026-11-13-geometry-m28-constant-size-q0965-r1-summary.json)列出实际数值、原预测、所有源 SHA 及六件小元数据路径。[计划](2026-11-13-geometry-m28-constant-size-q0965-r1-plan.json)、[完整 screen](2026-11-13-geometry-m28-constant-size-q0965-r1-screen.json)、[资源退出](2026-11-13-geometry-m28-constant-size-q0965-r1-resource.json)、[场 manifest](2026-11-13-geometry-m28-constant-size-q0965-r1-field-manifest.json)、[原 driver 执行记录](2026-11-13-geometry-m28-constant-size-q0965-r1-execution.json)及[账本](2026-11-13-geometry-m28-constant-size-q0965-r1-ledger.json)保持原字节。可复算 gzip 场块仅本地保留，其精确 SHA 与覆盖记录在 manifest 内。

`root_geometry_minimax_combined_plan.py` 已实际执行；它将选择项完整转换给原构造器。该新结果不改变正在独立求解的 q098 的接受标准，也不转移旧 g 的理论尾证书。下一新点要等待真实接受与新 full-J，再将 `start_acceleration` 作为第六个 core-held 控制评价。
