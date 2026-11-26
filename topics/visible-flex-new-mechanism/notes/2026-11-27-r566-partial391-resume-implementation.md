# B030 从真实 7371 保留状态续算：复用 391，补完 1128

日期：2026-11-26 UTC；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

**这是新的已声明公开 Actions 输入与纯源码，尚无本 scope 的科学结果。**
来源是 [physical epigraph 完整自然终态](2026-11-27-r566-physical-epigraph-original-terminal.md)，
不重放原 15 次 metric 接受、1 次恢复、33 个 Jacobian 或 27 次已完成定位。
原完整物理门与所有求解参数保持；本次唯一新的继续接口是保留原未完队列
已经完成的前缀，从真正剩余 bracket 接着处理。

## 唯一原来源

run [45892179085](https://github.com/Rogerhu12/math-research-public/actions/runs/45892179085)，
job `140157246913`，触发提交
`1530094182e7409efe4fd040b9daa843389fbe2c`，实际 public pull
`dc291b5037f5e6ab2bdc8b7b0b51a328be9fa588`。

| 原字节对象 | 字节 | SHA-256 |
|---|---:|---|
| 完整原 stdout | 24320183 | `fb0591bef629a409e8e720154ca19a93bc7559c308bbd6f08b79e5566aa5a674` |
| 逐字 FINAL JSON | 575651 | `fca44b01c14b3a220f6d9116615e97371c887c2f67082e538f55f6e5bdfd9bb7` |
| 逐字 PARTIAL JSON | 325628 | `f3727616140ad30c0c2f3556bbb75d8bb51d409212135b0f92f7d897615e64e4` |

真实保留 q 是
`7371a880eaa603c17191acc747847817dd1e846196ee0d4e74548a125c898513`，
完整 eta `0.2277496382670385`，在 **1298×3072** 和全部 **1515** 个
原观测角峰上合格。当前 full coarse 是 **660** 径向、**1473** 个
实际 peak orbit、**573** 条工作行、FFT **1536**；当前永久 fine 是 **1322**。
`best_fine_nodes` 从 FINAL 的 `retained_qualification_fine_radial_nodes`
载入 1298，而不是误标成当前 1322；若本次原未完成候选仍未闭合，旧 q
保留其真正通过的原 fine 资格。后续所有 fine 都继续取永久精确并集。

原 trust 与 next trust 都是 `0.3003387451171875`，没有未报告的 trust 决策。
原 BFGS 工作数组没有输出，不能恢复成“同一原进程”。现有物理 best 与
raw backend 双轨保持，真实库 / phase 变化仍按原算法交换。

## 先完成同一原 scope 的剩余队列

未接受候选 q 为
`55e30fac8df3438d4e5d627f2c8ac9f867c67357db524e99589009bb8ad6ef36`。
原 working 和 2,346,480 条完整 coarse 已通过，原 **1322×3072** 全 fine
已完成，nested 三项已通过；这些报告只在相同 q 和相同 scope 上复用。

其原 1519 个 candidate 中，**391 已完成、全部成功，1128 未处理**。
新 helper 把原 391 个准确峰记录放入已完成前缀，只对剩下 1128 个原
bracket 执行原 four-orbit objective / bounded 定位。
原 fine 数组 binary64 SHA-256 为
`e0c7a9f044046140cc9eff8ff235498f17f447126bab8fcf864ed35869c23a01`；
原 oracle identity 为
`5bfa207c65636be672ca7395c97fdb9f5752dc3caf986a1ed58a80b9108b9b4d`。
参数 `xatol=1e-10`、`maxiter=50`、batch 512、边界四轨和 sampled fallback
均保持原样。新必要 FFT / primitive 准备进入同一 OracleLedger。

391 个完成峰从唯一原 PARTIAL 的 `peaks` 逐项复制；新 request 仅保存这段
必要前缀，1128 个剩余队列和完整 fine 坐标从原逐字 FINAL 取得，避免再存
一份重复 PARTIAL。完成前缀规范 JSON 为 58,958 B，SHA-256
`346519692aba79f1e418b20620b15b22c4d79de71e639d19f2544f86ff672ea1`。
本地核对了 PARTIAL 与 FINAL 的 q、oracle、fine 数组、剩余队列完全相同；
运行时再核前缀长度、成功状态、有限记录、规范 hash，以及前缀按 field
计算的 maxima 与原 FINAL `maximum_observed_peak_by_field` 一致。
整个输入另受 runner 的完整 stdin hash 和全部源码绑定保护。

helper 的 `candidate_count=1519` 与 `completed_candidate_count` 包含原前缀，
所有实际最大值与接受门消费合并后的全部峰；`new_candidate_count=1128`、
`new_completed_candidate_count` 和新 objective 求值单列，只把新工作加到
本段 counters。原 1542 个 objective、5.813535579000018 秒局部化在
源 cost ledger 保持已付，既不遗漏，也不重记为本段新花费。

若时钟再次中断，完整 PARTIAL 输出原已付前缀、新完成峰和真正剩余队列；
最后一个未闭合 bracket 的已花 objective 留在 elapsed 和计数里，不假称
得到完整峰或免费回退。全部队列闭合后才可考虑接受。

## 原接受门、pending 与物理约束继续保持

原 source candidate 的固定物理 box 逐坐标核对。它在相同 q 的较小 e
通过的 working / full coarse 可以按原已证 metric 行 `e−value` 单调性
继承；所有物理行不依赖 e。完成全部旧 / 新观测峰后，仍要求原几何
margin、完整物理门、nested 容差、e 包含实际 eta、真实 eta 严格下降。
原 raw 数组不原位修改，e 抬升不是物理或 metric 进展。

原 pending **5 个 physical orbit + 5 条 working proposal** 保持原证据，
先完成原 1322 / FFT3072 队列后再采用，不能先换网格后借旧完整报告。
新正常 callback 保持原 working / full coarse / full fine / nested /
全部观测角峰 / box / margin 门；抬 e 后仍执行原必要 working 和完整
coarse recheck。新发现但被抬 e 覆盖的实际证据仍进入原 pending 与工作库。

球、条带、正高度、mean-E 与 det 下限、两曲率组、mirror 必要条件、
全部材料参数和参考度量设计均未删除。科学上限 2400 秒、预留 30 秒、
工作容量 1024、径向容量 1025、peak orbit 容量 2048 等参数全部沿用
原已执行 scope。本次不借 finite 值认证连续角峰、全 reach 或固定 g。

## 实现与执行绑定

| 新文件 | 字节 | SHA-256 |
|---|---:|---|
| `scripts/r566_saved_partial_queue_20261127.py` | 8407 | `79fb5b0433f77164481d4ba067ff44fdc4829cd95319b6ab0448cacc8c4bbc8d` |
| `scripts/r566_partial391_physical_resume_20261127.py` | 55640 | `8c0a1300f75261b703cfeafd636e9b659f6436f67942ccb4e14d623c86dd8f38` |
| `computations/request-r566-partial391-resume-20261127.json` | 778681 | `fcd3b1d1d43dc46c1f0ddf695218e08f884caf4e1543a8d84d9167d32edbda4a` |
| `.github/workflows/visible-r566-partial391-resume-20261127.yml` | 5124 | `ee324eb88ed2484b39a2a2e3a22452066d79d9852d598b67c34e69f0ba3f39e6` |

lane 为 `rounded-core-B030-partial391`，stdin **678,180 B**，SHA-256
`62011715e938db8335d5a0a97ea1c65e6c7add254a9622b2c4d458413d2241c7`。
30 个 source / predecessor request / workflow 字节绑定齐全；原参数和所有
物理门保留。新 runner 先实际 pull 双仓、比对两份 README 与本会话 QUEUE，
删除认证环境后才开始新科学。只输出 stdout，不提交科学数据 artifact。

本地仅进行原日志解析、文本、JSON、AST 和 hash；没有导入或运行科学源码。
较早未知费用保持未知，原科学链已知下界 `12359.003476909998` 秒继续继承。
