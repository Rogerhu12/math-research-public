# λ1 真实失败与 λ.82 实际启动记录

**状态：没有取得合格端点；后继中间步终态未知。** 本条保存执行服务失联以前已经取得的真实观察，不把未知状态写成数学失败。

## λ1 的真实终态

从完整 λ=.64 物理 checkpoint `f55b4fbb…` 出发的 session **38274**（启动块 `31bbd3`）于 **2026-11-18 05:49:56 UTC** 返回终态块 `ecbd46`。observer 记录 child=0、worker=0，历时 578.728274961999 秒。原主流程捕获后处理异常后正常返回，进程 0 因而不是数学接受。

| 原结果 | 保存值 |
|---|---:|
| solve_bvp success / status | false / 1 |
| 实际节点／网格轮次 | 4212 / 3 |
| 原节点门 | 6000 |
| 最大 RMS | 1.0682086532050248 |
| 接受步数 | 15 |
| domain / merit 拒绝 | 139 / 59 |
| 最小接受步长 | 9.5367431640625e-7 |
| 新实际尾请求 | 0 |

原消息为 `The maximum number of mesh nodes is exceeded.`，4212 是已使用的网格大小。原 raw/cubic/RMS、八个参数、七个物理控制及 affine 来源已保存，不能把这个失败 raw 作为接受锚。

物理 CP 在 audit 前先写入。随后 `adaptive.audit → height_integral → integrate_intervals → frame` 触发正根域异常，实际 Frenet margin 为 **−2.533498597578898e−7**。完整 prefix metric、Darboux、mean 和 seam 均未返回；这不是尾求解失败，也不是合格的 literal λ1 端点。

[独立观察记录](../scripts/resume_m3/trace_path_lam100_observed_terminal_record.json) 保存完整已知身份、参数和标量。只读 collector `595c08` 已实际 exit=0，核过 207 个来源、26 raw/26 sidecar 和唯一 returned raw；其完整 scratch 记录 SHA 是 `432340279106b60d8801c22df0a3933031c2fc7d4324b161709423ae4a7e0fb1`。root 没有在失联前取得该 JSON 全文，所以本条独立记录只转存已实际读取并上报的字段，不冒称重新读取了不可访问文件。

## 继续 λ=.82 的实际入口

上述真实终态以后，从最后完整 λ=.64 锚继续 **λ=.82**，种子主振幅为 **0.05336960976112643**。原 gauge/warp=.06、全部参数和尺度、base profile 加一次 p0、原门与 native provider 均保持。失败 λ1 状态没有被用作接受锚。

[run_m3_trace_path_native_partial_v2.py](../scripts/resume_m3/run_m3_trace_path_native_partial_v2.py) 的 SHA 为 `175e4aeb80c14bb3772ff38e35003521ede5a2763ba9eff1cc218114577baeed`。它由已发布 `018df4f4…` 源的六项字面修改得到，限于严格中间 λ 的入口范围及父源绑定，保留原初值、方程、全部门和观察流程。失联前 `d4596f` 已核 AST/逆向还原；失联后 root 从 GitHub 读取完整父源、应用相同修改，得到的完整源码 SHA 与实际启动源一致。该源码恢复没有运行任何数学模型。

准备 `c7f173` 实际 exit=0，绑定 208 个来源，计划 SHA 为 `cc5ea1d1f81f91f184cc58c956eb95c51c9dcc2031a21a083c67390afbc58fb9`。唯一 observer **91205** 已由块 **439498** 启动，工作目录 `m3_work/trace-path-lam082-native-coupled-v1`。没有失联后的初始化、inner 或终态观察。

## 执行环境中断

2026-11-18 05:53 UTC 时，共享环境已标 `unavailable`；新的只读进程不能启动，随后读取既存会话明确返回 `No usable execution environment is available`。这些服务错误不提供 91205 或并行 27744 的进程退出码，不能据此判断 OOM、数值失败或重复启动。

GitHub 通道仍可用，故先保存已观察状态和实际源码。最后一次真实终端 pull 是 13:51:10（UTC+8）至 `97da2bfe…`；之后远端 compare 确认根和课题 README 未变，本次 API 读取没有冒称实际 pull。

恢复执行环境后先真实 pull/rebase、检查双 README 差异，再读取既存 observer/resource/原始返回和真实尾，确认状态后接原控制流。课题全部完成标准仍未满足。
