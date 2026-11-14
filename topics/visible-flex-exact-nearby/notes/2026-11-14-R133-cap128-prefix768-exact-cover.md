# 前 768 条完整帽行的准确覆盖消费

2026-11-14。原四个正常退出的 native 现在按原字节保存并消费：

| 原范围 | 行数 | 原 producer |
| --- | ---: | --- |
| `[0,256)` | 256 | v3 |
| `[256,512)` | 256 | v3 |
| `[512,513)` | 1 | v4 |
| `[513,768)` | 255 | packed v5，内含它明确消费的原 v4 前缀 |

全部输入文件、原 producer SHA256、真实进程记录及检查结果在
`2026-11-14-R133-cap128-prefix768-exact-cover.json`。该消费逐一确认
原 `selected_cells_complete=true`、`failure=null`、实际返回码 0，
每份文件的实际行数等于原声明范围长度；768 个 `index` 恰依次为
`0,1,…,767`，每个真实闭片的有理右端等于下一片的有理左端。

四份原科学 identity 仅 producer 版本字段不同；依照
[packed Fourier 与原算法的已证等价](../results/R133-supplement-packed-cap-Fourier-residual-and-prefix-continuation.md)
及原 `packed_v5.same_row_identity` 的明确规则比较后，其余每个字段
完全相等。原 v3/v4/v5 字段、数组 SHA、全部 97 个输入、257 个物理
状态、独立 mean、ordinary/divergence 及全部无限尾均保持原值。
此处没有重算任何数学行，也没有把原行重标成另一版本。

因此四份实际 native 的无重复并集严格覆盖原 1977 格中的 `[0,768)`，
真实径向并集为
`[9/10,286601144255265/281474976710656]`。这是一条完整的前缀覆盖
事实，不能据此给出尚未覆盖的剩余 1209 格、整帽图误差或完整主体逆。
