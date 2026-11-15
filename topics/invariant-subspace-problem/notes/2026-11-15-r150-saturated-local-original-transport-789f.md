# 完整饱和来源包的运行时 local source transport 接口

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

状态：冻结的实现接口，**尚未在本代理执行编译或数学计算**。
此文件不改变 204 个合法来源的证明，也不预填下一页计算结果。

代码：
[运行时 transport](2026-11-15-r150-saturated-local-original-transport-789f.cpp)，
blob `015e4fcd6cf8fdd829b6925c51b2e92a142df37e`。

它从原已使用的
`2026-11-14-r150-197-third-local-transport-789f.cpp`
（blob `8258b730f05698b8bc3c182809fac3f05670b8ed`）另存新文件；
旧文件不改。共同头固定为
`2026-11-15-r150-saturated-local-common-789f.hpp`，
blob `5ffd88b830ad58f9e8d10bfd291ceb7d3f2fb2fd`，
SHA-256
`1dc5005fd19003c77cce9620dd7f723b910db1c5ea3540e49a13fb93f440594f`。
其余 ninth-first common 与 F31 bitplane 算法保持原版本。

## 1. 命令行和作用域

```text
PROGRAM model oldK200 VQ normal RHS forward backward outPrefix \
        pipelineBinding mode old197TenOrDash spec checkpointDir remainingSeconds
```

参数顺序保留旧程序的前十一项，再追加 spec、checkpointDir、remainingSeconds。
程序名计入后 `argc=15`。

| 参数 | 实际内容 |
|---|---|
| model | 原 `R150_NATIVE_NF_V1` 模型和完整 6188 行来源字典 |
| oldK200 | q1 时的原 `R150KK31`；q2/3/4 不读取它 |
| VQ | 已完成的 2195 行 `R150SP31`，kind=1、done=1021 |
| normal | 完整原 2204 行 `R150NR31` H trace |
| RHS | q1 的完整 old200 trace，或 q2/3/4 的实际新 cochain |
| forward / backward | 原 `R150PB31` / `R150RJ31` 全 DAG |
| outPrefix | 仅输出路径，不参与 checkpoint 语义绑定 |
| pipelineBinding | 同一任务上游使用的 64 位小写 SHA-256 字符串 |
| mode | `q1`、`q2`、`q3` 或 `q4` |
| old197TenOrDash | q1 的已完成旧 197×10 原来源文件，或 `-` |
| spec | 运行时目标标签、长度和 ring |
| checkpointDir | 专用的真实数组 checkpoint 目录 |
| remainingSeconds | 总 runner **当前剩余**的正有限秒数，不是新分配一轮时钟 |

q1 仍限已付全局来源费用 177，对应原 cost≤81 的旧源。
若 spec 选入 old200 的 cost85 列，程序拒绝；
没有把运行时标签泛化误当已付更大的全局来源成本。
q2/3/4 的 bound=0 表示局部来源运输，不声明一个新的全局多项式次数界。

## 2. 运行时格式

spec 使用共同头提供的精确格式：

```text
R150_S2_LOCAL_JET_SPEC_V1
31 NT L ring
label_1
...
label_NT
```

共同头读取后设置 `jt::NT,L,W,S,RING\)，其中
\(W=\lceil NT/32\rceil\)、\(S=WL\)。
纯 root2 使用 ring=2；原 CRT 八槽使用 ring=12、L=8。
本轮的 197×20、198×15 及后续至多 229×10 均在共同头允许范围内。
`Co` 的物理长度为 20，但所有运算只遍历运行时 L。

VQ 和最终输出使用 `R150SP31`：

```text
magic[8]
u32: 31, count, NT, L, S, kind, done, bound
binding[64]
NT × u16 target-label
每行: u32 id, u32 raw-source, u16 delta, 5*S × u32 bitplanes
```

cochain 使用 `R150SN31`：

```text
magic[8]
u32: 31, 3333, NT, L
NT × u16 target-label
每行: u16 prebasis-id, 5*S × u32 bitplanes
```

全部 3333 个 prebasis-id 必须恰好出现一次。
cochain 恢复时会重新读取并核验原字典，但只对尚未执行的行做加法；
不会因重读输入而重加一个已经保存的数学阶段。

## 3. 保持不变的真实数学运输

原式仍为同一全局来源变换 \(B(J_\beta-HVQ)\) 的实际局部求值：

1. 将已完成的原 2195 行 VQ 放回其真实 raw-source 位置。
2. 按完整 H trace 的原符号扣除预基系数。
3. 加 q1 的原 old200 RHS trace，或 q2/3/4 的真实 cochain。
4. 逆序执行全部 backward DAG。
5. 逆序执行全部 forward DAG，回到原 6188 行来源。

原完整计数保持：

- normal H 操作数：25,305,683；
- backward 操作数：1,010,703；
- forward 操作数：782,976；
- 模型选定的原来源位置：5,528。

q1 不再硬编码第 \(j-1\) 个输出目标。
程序先从原 K200 元数据构造 `head-label → old-row` 字典，
再按 spec 的真实标签查对应的目标槽。
所有旧 trace 行仍全部读取、核验、计数；未选标签不写入输出。

纯 root2 的 Taylor 乘法与 CRT 两段乘法由共同头的原
`powers/muladd` 实现，不能把 CRT 八槽当一个长度八的 Taylor 环。

## 4. 可移目录的输入绑定

输出 packed 文件继续使用上游 `pipelineBinding\)，因此下一个原接口无需改成
另一种绑定格式。checkpoint 另有更细的 effective SHA-256，内容为：

- helper 版本、共同头 API blob、mode 和 runtime NT/L/S/ring；
- 同一个 pipelineBinding；
- model、VQ、normal、RHS、forward、backward 的实际文件字节 SHA；
- q1 使用的 oldK200 字节 SHA；
- 如使用，旧 197×10 比较文件的字节 SHA；
- spec 的规范化语义：质数、目标数、长度、ring、全部有序标签。

**不含任何输入路径、输出前缀或恢复目录字符串。**
spec 的原文件字节 SHA 另记为审计项，不放入有效绑定；
仅改变 spec 的空白排版不破坏相同语义的恢复。
上游 runner 还须按其既有 manifest 绑定本代码与共同头的实际编译输入。

输入、标签、环、精度或上游 binding 真正改变时，
旧 checkpoint 被拒绝；不能把不同页的已完成数组复用为本页数学进展。

## 5. 保存的是实际阶段与完整数组

五个阶段依次为：

| phase | 数组的准确状态 |
|---|---|
| 1 | 原 VQ 已放回，H trace 正在扣除 |
| 2 | H 全部完成，原 RHS / cochain 正在累加 |
| 3 | RHS 完成，backward DAG 正在运输 |
| 4 | backward 完成，forward DAG 正在回填 |
| 5 | 数学运输全部完成，等待或已经完成最终输出 |

每个 checkpoint 保存全部原 6188 行 raw 和 3333 行 beta 的 bitplanes，
以及 phase、下一行游标、实际流 offset、累计操作数和 generation。
不保存“预计已经做完”的假游标。

数组以双 slot 存储。每个分片至多 1,000,000 个 u32，
即 4,000,000 解码字节；RLE32 的最坏编码长度小于十进制 4,500,000 字节。
每片有 SHA-256，manifest 有 SHA-256，再以一个原子 active 指针发布。
恢复时要求全部片无缺口、无重叠，解码后的行宽、目标 padding 以及
所有 F31 值均正确；五个 bitplane 同时为一的非法值 31 亦被拒绝。

两个 slot 中只有 inactive slot 会被替换。
目录有排他文件锁，避免并行任务写同一份状态。
文件名只是 checkpoint 内部的受限相对名，不把任意 manifest 路径当作输出路径。

## 6. 单一剩余时钟、信号和完成回执

程序从入口开始计时，使用 runner 传来的剩余秒数；
保存预留为 \(\min(30,\mathrm{remainingSeconds}/4)\) 秒。
不要求另外至少 60 秒，不自行重置一个新的 300 秒预算。

SIGTERM / SIGINT 只设置信号安全标志；
在完成当前真实记录后保存完整数组。
定时 checkpoint 亦只在记录边界，阶段切换会强制保存。

退出码：

- 0：全部运输、必要的旧前缀比较和最终回执均完成；
- 75：实际数组已 checkpoint，因剩余时间或信号停止；
- 1：输入、scope、恢复状态或计算身份格式失败；
- 2：命令行参数数目不正确。

q1 若提供旧197×10文件，先按真实标签比较全部原 6188 行的前十项，
比较通过后才写新的原来源输出。
最后写 `outPrefix-original6188-q-jets.bin` 与原子
`outPrefix-transport.json`。
回执保 pipeline/effective 两个 binding、实际计数、是否恢复、
原 prefix 是否已比较及实际运行时维数。

本接口没有替下一层整数除 \(p\)、204 来源核、相关 primary 运输或
原十七式最终乘回作证明。它只保同一已经指定的原来源运输，
且必须由真实 runner 执行后才产生计算结论。
