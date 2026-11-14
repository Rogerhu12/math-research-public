# request17：真实极小非零 H 的原 native tail 冷启动失败

2026-11-14，exact_refinement，AI 辅助。

**实际结论：本次原 worker 确实收到非零的全部 112 项 H，并执行了原非线性 tail；第一轮 shooting 的全部 10 个回溯试验均被原动量分支门拒绝。没有新的已接受尾、没有新的完整 J 或 audit，也没有可复用的非零完成 anchor。** 这不同于此前在 prefix 域或线性方向上、尚未请求新尾便失败的情况。

## 1. 公开 Actions 的原回执

Run [43598917532](https://github.com/Rogerhu12/math-research-public/actions/runs/43598917532)，artifact `14116526155`，下载包 `visible-mainline-coupling112trust-43598917532-1`。数值环境来源记录的公开提交为 `4b8b2bfdd417f76574dcc2a8e2353c4c2dce3e21`。原 `full-DN112-tail-diagnostics.json.gz` 是只读汇总；完整 `true-tail_0001.json.gz` 和 `true-tail_iteration.json.gz` 均保留失败状态。

| 原字段 | 实际值 |
|---|---|
| 首请求时间 | `2026-11-14T13:28:33.638Z` |
| worker call | `1` |
| 请求 | `jacobian=true, audit=false` |
| H 第一项 | `4.1760413061806626e-17` |
| H 第二项 | `2.6552455799552836e-17` |
| H 第三项 | `1.5532555306562415e-17` |
| 第一次完整 stage pass | `13:43:22.412Z`，iteration `0` |
| 原 normalized norm | `13414069.96827908` |
| minA / minD | `0.999999999975931 / 0.9999999999999858` |
| correction chartCondition | `1.3312263223101865e+60` |
| 失败时间 | `13:44:50.600Z` |
| 原 request 耗时 | `977.033129609 s` |
| 原完整 shooting 状态 | `577 × 224` |
| actual shooting depth / physical depth | `576 / 8` |
| modes / quadrature / spacing | `112 / 2048 / 2` |
| steps / auditSteps / shootingParts | `12 / 12 / 8` |
| 原 solveTolerance | `2e-9` |

回溯步长为 `1, 1/2, …, 1/512`。前 5 次在 stage `13`，后 5 次在 stage `14` 被 `momentum branch D/S/A rejected` 拒绝；它们的原定位均为 `rawCell=0, rawSegment=7`。最终错误为

```text
multiple-shooting line search failed at 13414069.96827908
```

`outer_history=[]`，driver 的 `new_coupled_finite_acceptance=false`。尾失败响应的 `original_J_method`、`complete_J_entry_count`、`original_audit` 均为空；不能因为请求了 J 就说取得 J。

原文件字节身份：

| 文件 | SHA256 |
|---|---|
| `full-DN112/true-tail_0001.json.gz` | `ebe8932a7ba1a995f49b365344e795714bc0fdfccc606765cc69944b56a6b7a0` |
| `full-DN112/true-tail_trace.jsonl` | `62122d42b45a2f386a2c514e6434b317a144f06ebc402dc0b31c2d2367fd3d3e` |
| `full-DN112/true-tail_trials.jsonl` | `64a3fa166cb9baf4b948a784c49ed241f9afc73f1823dd6cb38f29551cd10533` |
| `full-DN112/true-tail_imported-zero.json` | `75c410e42eb7527686537cf4e15b69e26c4924e05d272fb3f8fd1b839afacb15` |
| `full-DN112/driver-status.json` | `2f951f3072922876281236fab6a003a51722a49789fdaa6f889f3fd7dc37d594` |

## 2. 这次没有复用首零响应，也没有恢复服务器 predictor

导入的是此前真正完成的 [T112 零锚](2026-11-14-actual-T112-zero-anchor-and-J-audit.md)。其完整 J 为 `338 × 112`、37856 项，原 residual 为 0。导入 manifest 仍明确记录：

```text
server_tangent_predictor_imported = false
nonzero_height_rounding = false
cache_discarded_before_first_actual_worker_request = true
```

本次没有 `true-tail_imported-zero-uses.jsonl`。原 strict client 仅在全部 H 严格等于 0 且 `audit=false` 时复用；此次 H 非零，因而原缓存正确清除并把完整 H 交给原 worker。不是在 Python 缓存里对一个真新 H 使用了旧零响应。

实际 runtime config 没有 `initialCheckpoint`。原 `78718-prefix-tail-tangent-fourier-worker.mjs` 在 ready 前设 `last=null`、`tangentPredictor=null`，只有一次真实完成的 solve 才创建 live tangent predictor。故这次首请求没有 tangent warm，也没有 amplitude warm，`opts.initial` 未设置，原 shooting 入口直接使用

```text
target = H / r_cut^4
states = tail.initial(target)
```

失败时保留的是这个初猜第一次完整评估及其尚未接受的 correction 诊断；不能把失败 checkpoint 当作已完成 DN 响应。

## 3. 极小 H 与很大归一化残差为何不构成矛盾

以下是直接从原源码得到的结构，不是一次新重算。

原 `initial(target)` 用 ready 的稳定 `graphs/gains` 逐模式传播：

\[
Q_{0,j}=\operatorname{target}_j,\quad
\Pi_{0,j}=G_{0,j}Q_{0,j},\quad
Q_{n+1,j}=Q_{n,j}/\operatorname{gain}_{n,j},\quad
\Pi_{n+1,j}=G_{n+1,j}Q_{n+1,j}.
\]

而 `scaleFor(target)` 使用首模的 gains：

\[
s_0=\max(10^{-250},\|\operatorname{target}\|_\infty),\qquad
s_{n+1}=s_n/|\operatorname{gain}_{n,0}|.
\]

报告的 norm 是各 stage 残差除以这些 $s_n$ 后的最大值，另含原两端条件。在线性极限且尚未触及 floor 时，同时把 H、states 和 residual 缩小，scales 也同比缩小，归一化残差并不必变小。因此 `1.34e7` 不能直接解读为具有同样量纲的大幅位置误差；它仍是真实且远未通过原容差的数值失败。

还有一个实际已知的离散差别。原 `closure_linear_stage_graphs.mjs` 对 stage 图使用

```text
max(8, ceil(linearSteps / shootingParts)) = 256
```

步的线性 RK4 传播，本次真实 state/variational residual 使用 `steps=12` 的原流。不同离散传播不因输入足够小就自动一致。此前 T112 真零 J 核对已经实际记录：真实 shooting slope J 与 ready 线性 slope 的最大绝对差为 `828.7132857724173`，最大相对条目/列差为 `0.035157884011777545`。该旧检查直接支持“两对象不同”，但尚不能定位本次 `1.34e7` 的全部来源。

本次实际初始最坏 stage、最坏模态和对应的未归一化 residual 尚未保存到摘要中。不能仅凭首个 guard 拒绝位置，声称它就是最初 normalized norm 的最大位置；更不能据此预先断言全部失败均由 RK12 精度造成。

动量 root 的原停止规则也已核过：它使用

\[
\mathrm{scale}=\max(10^{-300},\mathrm{maxQuad},\|\mathrm{target}_{\rm root}\|_\infty)
\]

以及 `err <= 8e-14*scale`，有原 `5e-12*scale` roundoff fallback；不是用一个固定绝对容差把所有 $10^{-17}$ 输入直接当零。这里没有更改这两个条件。

## 4. 最小下一诊断及不能作的替换

优先的最小诊断是：只在公开 Actions 中加载本失败 iteration0 的完整状态和同一原数值源，执行一次原**无 J stage evaluate**，不运行 solve、不作 Newton correction、不重算零锚。输出每个 stage/模态的未归一化 residual、原 scales 及归一化值，保原 rawCell/rawSegment 标签；核保存 states 是否逐项为原 cold initial，并保 graphs/gains 的完整身份。这样可定位当前真实 norm 的来源，而无需再付本次完整 J pass 的约 15 分钟成本。

只有拿到这条实际定位，才决定是否构造与同一个 RK12 离散流一致的线性 warm，或对原流做必要精化。任何新 warm 仍只是初猜，不能改变实际 H、原非线性残差、D/S/A、完整 J、最终 audit 或 fixed-g 要求。

不能据本次极小量级把 H 阈值化为 0，不把 ready 的线性数据替代实际 J，不用失败状态伪造可复用非零 anchor，也不重复此前已完成的耗时真零计算。前缀侧随后已核：warm 的实际末端非均值 z 与 fresh FD、native 请求一致，原 P 的常数列已精确置零；详见同日 [实际warm与native失败总记录](2026-11-14-actual-trust-warm-and-tiny-height-native-failure.md)。此身份核对不替代尚未执行的原无J残差定位。
