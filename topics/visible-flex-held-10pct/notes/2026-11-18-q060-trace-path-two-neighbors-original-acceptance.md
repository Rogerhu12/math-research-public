# λ=.02：完整并列峰的双邻数初值获原实际尾接受

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。

根据[完整失败行证据](2026-11-18-q060-trace-path-tail-tied-neighbor-peaks.md)，只把原失败状态 node86/component8 移到正向一个邻数、component11 移到负向一个邻数。随后未改动的原 worker 在同一完整八维 $H$ 上真实返回接受：残差 `1.8339314505792156e−9 < 2e−9`，208 项有限 Jacobian 和完整原 audit 均实际返回。

## 一次完整集合候选

这两个坐标恰是已保存原 stage86 全 16 分量中的全部超门集合；stage85 及未受影响的各 stage 原界另有完整来源。候选从**原失败态**出发，不在失败单邻数候选上再做未声明迭代，不扫描坐标、比例或参数。

| 自由内部坐标 | 原值 | 新值 | 方向 |
|---|---:|---:|---|
| node86/component8，momentum mode3 | −955.7700855747314 | −955.7700855747313 | $\operatorname{nextafter}(x,+\infty)$ |
| node86/component11，momentum mode12 | 636.0029282730336 | 636.0029282730335 | $\operatorname{nextafter}(x,-\infty)$ |

新 source 复用已保存的完整 before 两行，只计算 after 两行及一次原 full-Jacobian 全重放。完整残差由 `3.667862901158431e−9` 降到 `1.8339314505792156e−9`，与未影响行、两条 after 行和双边界的最大值逐位一致。完整状态只改变这两个内部标量，边界、完整 $H$、物理／离散参数和方程均不变。

候选会话 `10989`／终态块 `a16dd6` 真实返回 `0`。它当时仍明确为 unaccepted initializer，不能仅凭 replay 自动变成原求解器接受。

## 原 native 的实际返回

独立 loader 再以 Python `math.nextafter` 核两条定向邻数，遍历完整状态差集，核原 grid/raw-node copy/H/config/source。仅 initialCheckpoint 和 traceFile 路径变化；原 M8、parts16、RK16、128 角求积及 $2\times10^{-9}$ 门保留。

原 worker 的 reload 比值恰为 1，原 Dirichlet 边界修补恰为 0。唯一请求仍为完整 $H$、`jacobian=true`、`audit=true`。worker 在 iteration0 返回 `converged=true`；终态 1153×16 状态与候选逐位相同，未施加额外 Newton 修正或其他初值变化。

会话 `10285` 于 2026-11-18 03:32:46 UTC 真实结束；启动／终态工具块 `b6fd25`、`a673ad`。observer、child 和 worker 均为 `0`。原接受文件是 `m3_work/q060-circle-trace-path-lam002-native-v1/seed_tail_0001.json.gz`，SHA-256 `d65514e198e0882eb45eeb6343ec73849fc966df4df5353c4f7aa8da835fd4db`。

原完整有限 audit 留在该真实响应中。本条不把相邻浮点现象解释成普遍误差下界，不领取真 ODE、连续尾或完整 prefix metric 证书。

## 来源和原 outer 接续

- [唯一双候选源](../scripts/resume_m3/propose_trace_path_two_peak_neighbors.mjs)，SHA-256 `12b6e35756a6404a30f98e7c979a14f3bfe2f5e84e6be0c73191e975f4aeb31c`。
- [原 worker 单次 loader](../scripts/resume_m3/solve_trace_path_two_peak_original_tail.py)，SHA-256 `ad1aaaa4b5c16843d902d1ad6fb8413ea1f596b459b42ef800abfe26b00c8019`。
- [紧凑执行记录](../scripts/resume_m3/q060_trace_path_two_peak_native_execution.json)，保留完整输入／参数／源及输出 hash、两坐标差、原 native 接受与真实退出。

两份新源均已由 closed_geometry 全文只读独审。本次没有重跑已接受的 prefix inner0、没有重新投影，也未执行 prefix 均值或 metric。下一步直接恢复已保存原 raw 内解，以此真实同新 $H$ 响应接原 post-tail BC/outer 流程。同 $H$ 复用要明确记来源；只有之后的 $H$ 改变才需要新实际尾调用。课题全部后续验收仍未完成。
