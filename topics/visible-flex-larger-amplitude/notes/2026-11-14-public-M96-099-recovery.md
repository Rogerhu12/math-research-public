# 恢复大核心 M96 到 .99 的真实 Newton 检查点

2026-11-14，amplitude（GPT-6 Astra Pro，AI 辅助）。

**状态：实际计算的恢复记录，不是新收敛解。** 公开迁移前已经真实接受的放大核心 M96 前缀止于 $s=.984$；其数据和几何读出随本轮恢复的旧公开工作副本提交保存。随后到 $s=.99$ 的完整两端边值求解没有数学失败结论：它于 2026-11-14 09:08:19 UTC 在第 4 次全 Jacobian 的第 403/422 区间写入时因 `ENOSPC` 退出 1，实际用时 1251.63 秒。退出回执与原日志都仍在，不能把没有最终结果称为收敛。

## 已恢复的内容

目录 `2026-11-14-public-M96-099-recovery/` 保存完整 profile、原生 seed、固定的实际非轴法向 terminal projector、第四次全 Jacobian 开始前的完整 Newton 状态、原 argv、资源回执和日志，总计约 4.03 MB，每件小于 5 MB。`manifest.json` 给出逐件 SHA-256 和原数学源码 SHA-256。

检查点包含全部 423 个节点，每点全部 290 个实状态及其 RHS，$M=96$、$N=1024$，前 32 个核心 support 系数保持固定，所有高模仍是原问题的自由未知量。其 SHA-256 为 `e57dd148f64ce9e576227c478e0786e17d842726b84e9a251b0a6d3ba413ff39`。

在写盘失败前，三个内部 Newton 步已经实际接受：步长分别为 $1/4,1/2,1/64$。最后记录的 collocation 最大绝对残差为 $5.421661622152492\times10^{-8}$，边界最大绝对残差为 $2.686682629572234\times10^{-21}$。这些是内部迭代指标；没有最终 RMS 验收，不能据此推断完整 BVP 已经通过 $10^{-6}$ 容差。

## 公开 Actions 的下一步

新增入口 `computations/geometry_20261114_public_continuation.py` 只在本公开仓库 Actions 中执行数值工作；`--plan-only` 仅核文件和生成 argv。首轮使用恢复的完整检查点作为 warm，保留原 frozen profile、原 projector、全部 M96 状态、同一个有限 Fourier 方程、原 $10^{-6}$ RMS 容差与 $10^{-11}$ 边界门。不复用损坏或未写完的 QR 文件；在 runner 的独立 scratch 重建它们。

```bash
python -u topics/visible-flex-larger-amplitude/computations/geometry_20261114_public_continuation.py \
  --out "$RUNNER_TEMP/visible-larger-M96-results" \
  --work "$RUNNER_TEMP/visible-larger-M96-work" \
  --jac-workers 2 --budget-seconds 18000
```

可加 `--next-durations .006 .012 .024`，使一个确实完成、满足原 RMS/边界门的有限 BVP 继续准备下一个正 Gauss 转弯段。每一轮成功或失败都有自己的日志、完整结果、最新 Newton 检查点及 driver 状态。后续准备仅在前一轮真接受后发生；不会把初猜或内部迭代当作接受解递进。后续段延长 scalar profile 且可能改变自由高模，因此是新的设计问题，不能作为固定同一 $g$ 的收敛序列。

本次本地只完成语法检查、逐件字节核对和 `--plan-only`，没有启动 Jacobian 或重跑数值任务。完整闭合、全时刻嵌入/reach、握持区和最终直径仍待后续计算。
