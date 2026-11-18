# λ=.04：完整失败行的两个正邻数初值与原尾真实接受

## 新结论与范围

沿 [λ=.04 原内解已接受、改变 H 后原尾失败](2026-11-18-m3-trace-path-lam004-inner-accepted-tail-failed.md) 的实际失败态，先完整保留全部超原门分量，再一次同时修改两个内部自由分量。原 worker 在迭代 0 真实接受，完整归一化残差为 **$1.8339314423524552\times10^{-9}<2\times10^{-9}$**，返回全部 208 个有限参数 Jacobian 元素及完整有限尾审计。没有重跑前缀内解，也没有以局部候选分数代替原求解器的接受响应。

本条只完成实际新 H 的尾响应；完整物理前缀、均值高度与接缝由另一个精确 post-tail 接续承担。当前部分圆化状态不能据此记为本题完成。

## 为什么保存完整行

先前逐 stage 只保留一个最大分量的定位器会隐藏同一行上的并列峰。新只读入口 `retain_actual_tail_residual_rows.mjs` 对同一失败状态执行一次原 `evaluate(..., true, scales)`，要求整体残差与原失败末次读数逐位一致；它同时保留所有达到原停止门的分量及受影响、上游行的全部 16 个分量。它不调用 Newton，不修改状态。

本次 M8、spacing=3、N=128、steps=16、parts=16，共 1152 个 stage。重放整体残差仍为 $3.6678628847049105\times10^{-9}$，完整超门集恰有两个元素，均在 node/stage 86：

| 原分量 | 物理模态/类型 | 原 state | 原 flow | 指向 flow 的相邻数 |
|---|---|---:|---:|---|
| 8 | mode 3 momentum | −955.770089930836 | −955.7700899308359 | 向 $+\infty$ 一邻数 |
| 11 | mode 12 momentum | 636.0029318583507 | 636.0029318583508 | 向 $+\infty$ 一邻数 |

两者的残差都是 $+1.1368683772161603\times10^{-13}$，归一化尺度为 $3.099538922125287\times10^{-5}$。这里两个方向都为正，是本次实际完整行给出的结果；未照搬 λ=.02 的正、负方向。

所有其余分量的最大值是 $1.8339314423524552\times10^{-9}$。cut 行残差为 0，deep 行为约 $1.6500\times10^{-40}$。完整行、全 source manifest 和原失败状态都保存在执行记录绑定的 scratch 文件，不将可再生成的大表入 Git。

## 唯一组合候选与局部性

`propose_complete_row_neighbors.mjs` 只生成一次候选。它要求完整超门集的每个元素都位于自由内部节点，且原 flow 恰为指向残差方向的一个相邻 binary64；随后同时替换整个集合。本次完整 $1153\times16$ 状态只有上述两个标量改变。原 H、物理参数、cut/deep 约束不变，`rawStates` 仅按相同 `rawNode` 从候选状态一致重取。候选明确标记 `candidate_only=true`、`solver_success=false`。

原离散方程的 stage $n$ 只读取 `states[n+1]` 的 flow 并减去 `states[n]`。因此只改 node 86 时，只有 stage 85、86 会变化。候选计算对这两行各调用一次原完整变分 flow，保存全部 16 分量；其余行和两端的界取自刚完成的完整原重放：

| 行/量 | 候选读数 |
|---|---:|
| stage 85 全行归一化残差 | $6.111685245795528\times10^{-10}$ |
| stage 86 全行归一化残差 | $1.8339314423524552\times10^{-9}$ |
| 未改变分量的已保存界 | $1.8339314423524552\times10^{-9}$ |
| 合并后的候选整体上界 | $1.8339314423524552\times10^{-9}$ |

最后一行是依赖局部性的有限上界，**不是重新执行的一次全状态残差读数**。它只决定是否提交这个初值，原 native 随后完整重算停止门。

## 原 native 接受

`solve_complete_row_neighbor_original_tail.py` 独立用 Python `math.nextafter` 验证两个邻数、整个状态差集、完整超门集合、全部输入 SHA 和原 H/config/source。配置只改变 `initialCheckpoint` 与 `traceFile`。原重新加载算术给出 ratio=1、零边界修补；cut/deep 及其余内部态均保留。请求仍是原实际 H、`jacobian=true`、`audit=true`，原严格 $2\times10^{-9}$ 门不变。

真实原响应为：

- `converged=true`；迭代 0，残差 $1.8339314423524552\times10^{-9}$。
- 返回 208 个有限 Jacobian 元素和完整有限 audit。
- 最终所有状态与候选逐位一致；没有另一次 Newton 修正或自动重试。
- 原停止路径 minA=$0.5218915639820443$、minD=$0.9991195358652001$。
- 有限 audit 的 actualMetric=$4.624395355534716\times10^{-8}$、formalCurvature=$8.409064765815549$；它们是原审计读数，不是新增的独立接受门或连续证书。
- worker、父进程与 observer 均有真实 return code 0。

接受文件为 `m3_work/trace-path-lam004-native-neighbors-v1/seed_tail_0001.json.gz`，SHA-256：

`7c3af1e8d95445cacfc82fbb27f138c9c46d560d9eee5bedd401cb84b87e1e93`

已将该真实同 H 响应交给原内解返回点的恢复器。它可复用此响应，未知 H 仍必须调用原实际尾；本批未执行新的前缀求解。

## 执行与复现来源

| 阶段 | 实际 session | 终态 UTC | 实际工具终态块 | child/observer |
|---|---:|---|---|---|
| 完整失败行重放 | 38300 | 2026-11-18 04:02:56 | `6de2f3` | 0/0 |
| 唯一组合候选 | 12179 | 2026-11-18 04:05:45 | `0143f6` | 0/0 |
| 原 native DN/Jac/audit | 12075 | 2026-11-18 04:07:42 | `3fc436` | 0/0 |

源码与紧凑记录：

- [完整行重放](../scripts/resume_m3/retain_actual_tail_residual_rows.mjs)
- [唯一组合初值](../scripts/resume_m3/propose_complete_row_neighbors.mjs)
- [原 native 请求](../scripts/resume_m3/solve_complete_row_neighbor_original_tail.py)
- [执行记录](../scripts/resume_m3/trace_path_lam004_complete_row_neighbors_execution.json)

紧凑记录绑定原失败 `a94402…`、完整行 `e40e68…`、候选 `de8479…`、原接受 `7c3af1…` 以及全部三次真实命令、资源终态和源 SHA。复现按记录中的三条命令依次执行，输出改为新的空路径；源会拒绝覆盖或输入来源不符。此处没有扫物理参数、连续逐坐标试错或更改 residual 公式，也没有将这两个实际邻数现象推广成一般机器误差下界。
