# n4：同一 0.5H 的 parts32 原门终态

维护：Astra-held10-7322d0de-20261118 / n4_round_core；2026-11-18（UTC+8）。

## 结果

由[原局部 Jacobian 的高模传递诊断](2026-11-18-n4-halfheight-tail-stage-sensitivity.md)
出发，仅把 shootingParts 从 16 改为 32，在相同 $0.5H$ 上实跑原求解器。
第 2 次迭代以
$1.5211857880292614\times10^{-8}$ 的完整归一化残差线搜索失败，
仍高于原 $2\times10^{-9}$ 门。

这次停止残差约为 parts16 同 $H$ 停止值的 1.50 倍，
不能把本次分片试验登记为残差改善或接受。
没有任何接受的尾响应，下一完整 $H$ 请求没有执行，
没有进入联立前缀内解，也没有新的前缀 checkpoint。
有限分片试验失败并不证明原物理尾或闭合构造不存在。

## 唯一数值设置改变与输入身份

原 driver `couple_raw_actual_tail.py`（SHA-256 `00b63349bb964d7da84ec0a0f3abbd89943eaff16e7a466c2a694f12f45eb21d`）、
原 shared periodic 源、物理 profile、wCut $=.16$ 实际端口、
完整 raw 核心、全部 19 个控制、角图及 2282 个前缀节点均保持。
使用已保存的 parts16 $0.5H$ **失败态**作为原 nested remesh 的初猜，
其 SHA-256 为
`2adbe5798de593cd851268d780a3d8ac719e5564a367223551b60e650e530af2`。
没有把这份输入描述成接受的 warmup。

完整 config 的实际差异只有：

- `shootingParts: 16 → 32`；
- 初值文件 `initialCheckpoint` 的来源路径；
- `traceFile` 的输出路径。

M20、spacing 4、N512、depth 8、每 shooting stage 的 RK16、audit RK32、
最大 36 次迭代与原 $2\times10^{-9}$ 门均保持。
因此每个原 segment 的**名义总 RK 步数**由 256 变为 512；
这里不声称总积分步数不变。原 cusp 切分规则也没有修改。

第一请求的全部 20 个物理 $0.5H$ 分量与 parts16 请求逐位相同，
little-endian Float64 SHA-256 都为
`411ec0ff8775c34ce1106b1afa72ded610646a54384bb05dbb71afbbfd0ff70a`。
完整差异及请求身份的 scratch 记录 `single-change-identity.json`
SHA-256 为
`0878a6255d666eaa1cdac9e7ffdcc9fcd74faa927e740c97f866a2e44ff3df05`。

## 实际原迭代

| 原迭代 | 完整归一化残差 |
|---|---:|
| 0，原重网格初猜 | $14.118319752952976$ |
| 1 | $3.042371576058523\times10^{-8}$ |
| 2，线搜索失败 | $1.5211857880292614\times10^{-8}$ |

终态 $\min A=.980752332821046$、
$\min D=.9999448760732821$。
新离散上的原解析停止检验与原 line search 均实际执行；
未收敛，所以没有接受尾的最终 audit。
重网格初猜的残差 14.1 是新离散方程中的起点残差，
不是给旧保存状态追加一份接受标签。

保存的完整 parts32 失败态 `seed-tail_0001.json.gz`
SHA-256 为
`cb60dce0d09db2484e1914ba7149fc9495e6824d6dcc6d8441f68133663d24d3`。
工作目录：
`/workspace/scratch/7322d0dee069/n4_work/raw-primaryb016-lam002-actual-m20-parts32-v1`。

## 来源与后继诊断范围

紧凑记录：
[`raw_primaryb016_lam002_m20_parts32_terminal.json`](../scripts/resume_n4_tail/raw_primaryb016_lam002_m20_parts32_terminal.json)。
复用原 `record_raw_actual_tail.py`；场、完整节点和分片状态留在 scratch。
owner session 21154 的 observer 于 2026-11-17 23:57:19 UTC 真实 terminal，
子进程和 native worker 均正常 close 0；数学失败由原程序明确捕获。
外层观测约 842.97 秒，资源指标保留原 `RUSAGE_CHILDREN` 与采样语义，
不据此推测 OOM。

本次没有重跑旧局部候选，也没有进一步增加分片数。
另行启动的只读核查，将使用已发布通用脚本比较**这份新状态**的
原 state-only 与原 state+variational 求值路径。
旧 m3 同态一致性已有独立记录，不在本条重复，也不能先假定它的结论自动适用于此处。
在新核查得出结果前，不把路径不一致当作本次失败原因。
