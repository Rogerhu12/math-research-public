# n4：parts32 两原求值路径一致，另定位到一 ULP 主导行

维护：Astra-held10-7322d0de-20261118 / n4_round_core；2026-11-18（UTC+8）。

## 同一新失败态的两原路径

对[parts32、相同 $0.5H$ 的新失败态](2026-11-18-n4-halfheight-parts32-terminal.md)，
直接复用已发布的
`scripts/nonlinear_tail/m3_stage_amplification_deliverable/audit_failed_map_consistency.mjs`。
此源调用实际 split worker 工厂，无 mode 3 硬编码；
输入是本次 n4 状态，不是重跑已登记的旧 m3 一致性检查。

原 state+variational 停止路径与原 state-only 线搜索路径均得到
$1.5211857880292614\times10^{-8}$，与保存停止值相同。
2304 个 stage 中每个 40 个 shooting-state 输出的数值差全部为 0。
这里比较的是原残差使用的 $2M$ 个分量，未把额外 mean 积分分量也声称为已比较；
“数值差 0”也不扩大为 signed-zero 编码逐字节相同。

因此，这份状态上的已观察停滞不能归因于这两条原求值路径不一致，
不据该假说修改 line search。两个范数仍大于原 $2\times10^{-9}$ 门。

## 必须区分旧输出中的 component 字段

通用一致性脚本把最大残差行定位在 stage 175、cell 0、原 segment 3。
但其 `component` 字段追踪的是**两路径的差异分量**；当差异全为 0 时，
它保留默认值 0，不能把这个字段直接解释为最大残差的模式。

为此只对这一个已经由全重放确定的最大行及上游行重新读取原解析 flow，
没有再次重放全部 2304 行，没有改变任何状态，也没有求解新点。
实际主导分量为 component 20，即 mode 4 的**动量**分量：

| 项目 | stage 175 |
|---|---:|
| 原区间 | $[.5,.53125]$ |
| 保存节点值 | $-6.122429682261514$ |
| 原 flow 值 | $-6.122429682261515$ |
| 有符号残差 | $-8.881784197001252\times10^{-16}$ |
| 该分量 ULP | $8.881784197001252\times10^{-16}$ |
| 原归一化 scale | $5.8387241498672244\times10^{-8}$ |
| 归一化绝对残差 | $1.5211857880292614\times10^{-8}$ |

它恰为一个相邻 binary64 值之差。
上游 stage 174 当前最大行残差约 $4.71344\times10^{-10}$，
对应同一 mode 4 动量的 2 ULP，但其 scale 约为
$3.76871\times10^{-6}$，所以归一化后低于原门。
不能直接由此保证改变 node 175 后的上游行仍通过；任何候选都须重新计算。

这个新主导机制不同于 parts16 旧态的 mode 76/80 多行残差，
不追认已失败的单峰或多峰 screen 为成功。

## 来源、接口与后续范围

输入完整状态 SHA-256：
`cb60dce0d09db2484e1914ba7149fc9495e6824d6dcc6d8441f68133663d24d3`。
紧凑结果分别为
[`raw_primaryb016_lam002_m20_parts32_map_consistency.json`](../scripts/resume_n4_tail/raw_primaryb016_lam002_m20_parts32_map_consistency.json)
和
[`raw_primaryb016_lam002_m20_parts32_named_peak.json`](../scripts/resume_n4_tail/raw_primaryb016_lam002_m20_parts32_named_peak.json)。
新增单行读取源 `read_map_consistency_peak.mjs` 保留原 source/hash/配置绑定。
`adapt_consistency_peak_locator.py` 只把已完成的全重放和具名单行读数接到
既有单邻点工具的元数据接口；其 `largestResidual` 明确仅含一个已证明达到全局最大值的行，
不假装生成了完整排序表，也不生成数学状态。

只读全比较 session 80200 于 2026-11-18 00:00:52 UTC exit 0；
具名单行读取 session 5607 于 00:03:03 UTC exit 0。
它们都不是 nonlinear DN 接受。

后续允许明确尝试唯一的 node 175 / component 20 向原 flow 值移动 $-1$ ULP 初猜。
该动作仍须检查两条原邻行，并进入原完整 residual、DN 求解、解析 Jacobian 与 audit；
只有它们真正通过原门才是新接受的有限尾。
本条到此仅完成诊断，不预先宣称该候选、完整 $H$ 或联立前缀成功。
