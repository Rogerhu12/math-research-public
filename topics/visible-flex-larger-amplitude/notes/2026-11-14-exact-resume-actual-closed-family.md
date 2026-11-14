# 原 A 的背景保留尾已实际组装为有限闭族：三个网格与全相位样点检查

作者：exact_closure，GPT-6 Astra Pro，AI 辅助。2026-11-14。

本条实际执行前条准备的完整链：原物理 quintic prefix 的完整 mean → 背景保留 2305 节点有限尾与固定宽 `0.01` cut 修补 → 原固定 inner collar → R14 弱固定帽 → 三个闭网格、9 个 phase 的像样本、三类法向弦样点检查。公开旧 CI 已按更新后的根规则 14 停用；这里是在**本地独立普通文件快照**上完成，没有新增旧 CI 请求。

**当前 A 仍不是本题完成解。** 最大相位像距离样本约为 `0.0630D`，远低于 `0.2D`；空间嵌入/reach 检查仍是有限样本，严格准确等距极限的缺口也保留。新增的是已实际跑通、可供未来实际大幅候选复用的完整有限闭组装及其真实读数。

## 1. 已完成的可审查产物

完整目录为 `notes/2026-11-14-exact-resume-actual-closed-r2/`。其中：

- `refined-A-closed-phase0.ply.gz`、`-phase4.ply.gz`、`-phase8.ply.gz` 对应 $t=0,1/2,1$。
- `refined-A-closed-assembly.json` 保存完整组装、mean、接缝、metric/曲率和 phase 读数。
- `refined-A-closed-all-phase-finite-pairs.json` 保存三类法向弦检查的实际最坏对。
- `refined-A-closed-normal-samples.npz` 保存被检查的真实空间点、单位法向与源顶点索引。
- `actual-closed-summary.json` 从实际 mesh 重读全局顶点直径和固定帽并集直径，附完整 9-phase 表。
- plan、source background、启动源哈希、argv、逐步退出及最终 tool 结束记录均在同目录。

最终三个压缩网格大小分别为 `1,141,241`、`1,187,062`、`1,145,909` bytes；各自解压大小为 `3,745,773` bytes，均小于 5 MB。每个网格有 `73,442` 个顶点、`146,880` 个三角面、Euler characteristic `2`，每条边恰好邻接两面，零面积面数为 `0`，最小三角面积为 `9.967257147929602e-11`。这些拓扑和非退化读数不单独证明没有自交。

## 2. 完整 mean、接缝和表示保持

原 prefix mean 使用原 knots 上正权 Gauss6 积分和完整 `1552` 角规则，唯一 mean 锚仍在物理 $s=0$。得到

$$H_{\rm cut}=1.9614677525806448,$$

实际 upper cap 的平面高度为

$$H_{\rm cap}=1.984151796693749.$$

尾的 background 和 small mean 一起按原 `sigma=-1` 反射，下半片是完整上半片的 z 反射。接缝补丁只在尾的 $r\in[0.29,0.3]$ 上作用，原 prefix 没有被重插值或添加 s 方向补丁。cut 用保存 Fourier 系数直接定义完整共同二 jet。

| 实际完整 mean 框架下的 cut 差 | 最大向量范数 |
| --- | ---: |
| 位置 | `2.3055512673781017e-16` |
| $F_s$ | `2.2887833992611187e-16` |
| $F_{ss}$ | `2.2898349882893854e-16` |
| $F_\theta$ | `6.20633597500042e-17` |
| $F_{\theta\theta}$ | `1.1188630310358827e-16` |
| $F_{s\theta}$ | `2.482534390000168e-16` |

最终 mesh 显示取点上，prefix、finite tail、collar 的相对 metric **算子范数**最大值分别为

$$4.7040619844\cdot10^{-8},\qquad
4.3589094131\cdot10^{-8},\qquad
4.5462084062\cdot10^{-16}.$$

显示网格比此前完整 tail 的 `39168×1024` audit 稀疏，故不把较小显示读数当作新的全域最大值。此前更密的四级尾 metric 样本最大值 `7.2922816452e-8` 仍保留；原真实 prefix 更密曲率样本约 `8.34551434`，也不能被本次显示网格上的 `8.31766531` 取代。

原 fixed collar 的非零缺陷没有靠增深度或缩宽度隐藏。另条 `2026-11-14-exact-resume-fixed-finite-collar-bound.md` 已对实际 binary terminal Fourier jets 所定义的 finite collar 给出全 r、全角 metric 贡献上界 `1.0013852088236555e-18`。当前 mesh 读数约 `4.55e-16` 处在浮点计算量级；严格无限非轴尾存在性并不因此得到证明。

## 3. D、固定 H 与幅度的实际读数

实际 mesh 顶点点云的直径见证下界与原点球直径上界相同，为

$$D_{\rm mesh}=3.977459266677549.$$

这约束的是当前有限 mesh/点云，没有把它写成完整连续 C² 曲面的严格直径界。

固定握持区取两整个固定帽的并集，符合原定义允许 H 不连通的规定。其 `9602` 个固定顶点的实际直径为

$$\operatorname{diam}H_{\rm mesh}=3.9695633776641137,\qquad
\operatorname{diam}H_{\rm mesh}/D_{\rm mesh}=0.9980148410118023.$$

直径见证是两帽 cuff 上相对的点。对显式连续固定帽，简单几何还给出数值括区间

$$3.9695633776641137\ \le\ \operatorname{diam}H
\ \le\ 3.9695634386799,$$

其下端来自相对 cuff 点，计算式为 $2\sqrt{r_c^2+H_{\rm cap}^2}$；上端来自全帽包含在 $r\le r_c,\ |z|\le H_{\rm cap}+A$ 中，计算式为 $2\sqrt{r_c^2+(H_{\rm cap}+A)^2}$。展示的平方根是数值评价，完整 source/mean 的严格误差界没有在这里支付。

相位法则始终为

$$F_\alpha(s,\theta)=R_\alpha F_0(s,\theta-\alpha),
\qquad\alpha=\pi t/2.$$

固定帽和 cuff 的对应网格顶点在全部 9 个相位上逐位相同。点云 Hausdorff 读数如下；它们不是连续曲面 $\delta_{\rm hold}$ 的独立严格上下界。

| t | 点云 Hausdorff 距离 | 除以 $D_{\rm mesh}$ |
| --- | ---: | ---: |
| 0 | 0 | 0 |
| 0.125 | `0.05141204139` | `0.01292584988` |
| 0.25 | `0.10062696546` | `0.02529930760` |
| 0.375 | `0.14516780437` | `0.03649762188` |
| 0.5 | `0.18304330618` | `0.04602015857` |
| 0.625 | `0.21276098947` | `0.05349168281` |
| 0.75 | `0.23427942511` | `0.05890177860` |
| 0.875 | `0.24651106441` | `0.06197701796` |
| 1 | `0.25063813746` | `0.06301463338` |

相同 D 代表下，目标 `0.2D` 为 `0.7954918533355098`。当前有限读数仍约只有目标的三成，故不能收尾。

## 4. 全 phase 的有限空间法向弦检查

采用实际阈值

$$\tau=0.03D_{\rm mesh}=0.11932377800032647.$$

检查的判据是对两端单位法向同时控制

$$|q-p|^2-2\tau\max\{|n_p\cdot(q-p)|,|n_q\cdot(q-p)|\}\ge0.$$

moving/moving 对在共同刚体转动下不变，fixed/fixed 对不随 t 变化；moving/fixed 对直接调用 [R11](../results/R11-exact-all-phase-normal-chord-reduction.md) 的连续相位消元，覆盖全部实相位，强于所需的 $[0,\pi/2]$ 区间。空间点仍是输出 NPZ 中明确保存的有限样本。

| 对的类型 | 样点对总数 | 最小余量 | 负余量对数 |
| --- | ---: | ---: | ---: |
| moving/fixed，全部连续 phase | `19,196,784` | `5.1657408646e-10` | 0 |
| moving/moving | `31,932,036` | `1.4525134087e-14` | 0 |
| fixed/fixed | `2,883,601` | `4.1385065037e-8` | 0 |

同类远点对若弦长至少为 $2\tau$，由单位法向的 Cauchy–Schwarz 不等式自动有非负余量；其余对均实际评价。moving/moving 的最小绝对余量来自非常近的样点，弦长约 `1.20564e-7`。因此绝对余量小不应误读成 reach 只剩该数值的长度预算。

这些读数没有覆盖所有连续空间对，也没有认证全部相位中的连续嵌入。需要区分“相位已消去”和“空间已全部覆盖”。

## 5. 显示网格缺陷的实际修复

第一次完整执行已退出 0，但拓扑检查发现 16 个零面积面。原因是 cap 显示计划同时请求

`0.031249999999999993` 和 `0.031249999999999997`，相差 `3.469446951953614e-18`；部分 Cartesian 顶点舍入到同一点。

新入口 `computations/exact_20261114_closed_display_adapter.py` 仅合并这类机器量级的近重复**显示查询**，优先保留命名 marker/端点。没有移动任何物理 source node，没有改 g、实际函数、系数、cut 宽、inner collar 或 t 范围。原失败 mesh 的摘要和实际终态作为 `preceding-r1-*` 保存，最终交付的是 r2 三个无零面积面的 mesh。

后续应使用这个显示适配入口的 `plan` / `render`，不直接使用早期 driver 中尚指向未适配显示计划的默认入口。例如在 topic 目录中，给定原生成的 `$COMPLETE` 与接受 checkpoint：

```sh
python -u computations/exact_20261114_closed_display_adapter.py plan \
  --source-topic "$SOURCE_TOPIC" --checkpoint "$CHECKPOINT" \
  --port "$PORT" --config "$CONFIG" --complete "$COMPLETE" \
  --out-prefix "$OUT/refined-A-closed"
node --max-old-space-size=384 --expose-gc computations/exact_20261114_closed_background.mjs \
  --repo-root "$REPO" --source-topic "$SOURCE_TOPIC" --config "$CONFIG" \
  --plan "$OUT/refined-A-closed-plan.json" --out "$OUT/refined-A-closed-background.json"
python -u computations/exact_20261114_closed_display_adapter.py render \
  --source-topic "$SOURCE_TOPIC" --checkpoint "$CHECKPOINT" \
  --port "$PORT" --config "$CONFIG" --complete "$COMPLETE" \
  --plan "$OUT/refined-A-closed-plan.json" \
  --heights "$OUT/refined-A-closed-background.json" --out-prefix "$OUT/refined-A-closed"
```

原 full mean 和所有已交计算源都在独立快照中执行，未依赖主仓库 rebase 期间的文件状态。最终 plan、background、render 实际退出码全部为零，总用时 `64.73806` 秒；从 mesh 重读摘要再用 `0.68549` 秒，退出零。对应新摘要源为 `computations/exact_20261114_closed_mesh_summary.py`。

本条交付真实完整有限闭组装，继续等待/消费新实际大幅候选自己的 tail H、prefix 和 readout；旧 A 的小幅读数不得自动移植为新候选的结论。
