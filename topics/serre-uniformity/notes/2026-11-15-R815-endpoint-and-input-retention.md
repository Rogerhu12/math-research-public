# 2026-11-15 17:15 UTC：R815 端点与必要输入保留期限核对

这是纯 IO 跟踪笔记，不新增数学结论。所有到期时间均读取公开仓库 Actions
artifact API；没有改变保留期限、复制 raw 到 Git 或重算旧数据。

## R815 当前实际状态

run `43719622321`，job `132828560965`，
source `2a3300a9edec73c23e72f23127a0ae7d8222d13e`，
13:33:32 UTC 启动；17:10 UTC 仍在运行第 6 步。
一次完成日志请求返回 BlobNotFound，随后没有对仍运行日志重复请求。
尚不能消费其未发布输出。

原 core / wrapper / framework SHA 分别为：

- `80516ff9598fdb6251628c00794dc3529b998a7c563fe80fd9c31406e3896c7d`；
- `ab725da038ec458493f461088ceee0fd105e0dc90cbfb4ad6f3047cbec90b454`；
- `849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3`。

核心自然 BudgetStop 写 core receipt 后重抛，故自然预算结束可以是退出码 1；
外层等待预算加 120 秒后才 SIGTERM，10 秒宽限后必要时 kill，记 124。
必须读真实 error / receipt 区分，不能把 workflow failure 自动当数学失败。
工作流在最终 verify 之前 always 上传一日 artifact。

## 保留期限与真实覆盖

| 原输入 / 已成功载体 | 原 artifact | 实际 expires_at UTC | 必要覆盖与边界 |
|---|---:|---|---|
| R806 | 14161637987 | 2026-11-16 12:25:28 | 原 34 组准确 $M_w$ 坐标、cyclic/index/metadata |
| R813 | 14162633303 | 2026-11-16 12:58:33 | 原两列 g/h 的准确坐标及 normal interface |
| R824 首 scope 成功 | 14168007461 | 2026-11-16 15:28:05 | 已核 7741 成员 carrier，含 R786 原五次 index、旧 R787 1234 real 行与 14 branch、R781 至 142 的 Laurent、必要 V6/V7 行 |
| R809 C-only 成功 | 14168728276 | 2026-11-16 15:52:48 | 已成 1234 条 S5 原行及其输入；A/B 尚未完成 |
| R820 | 14164872449 | 2026-11-16 13:58:47 | 两图原 cusp 272 列，实际各 colength 20 |
| R786 原早期产物 | 14148389754 | 2026-11-16 05:41:45 | β 所需五次 index 已有较晚 R824/R809 载体；不能据此声称全部旧行均在任意 carrier |
| R775 | 14148883593 | 2026-11-16 05:52:45 | β 所需 M2 与 power 2–5 已逐原 SHA 纳入 R790 的续传输入 |
| R791 | 14149997458 | 2026-11-16 06:37:55 | β 必需原 CM tangent；R794 没有续传这个 tangent 文件 |
| R790 | 14151827531 | 2026-11-16 07:22:12 | 原 146 个 CM value/first-jet 行；同时 carrier 保 R735 model 与 R775 M2/power 2–5 |
| R794 | 14152074788 | 2026-11-16 07:44:33 | carrier 保 R791 Hom / real-descent；不能代替未含的 CM tangent |
| R735 旧历史产物 | 14118747540 | 2026-12-14 15:08:07 | 原 model / torsion；这是已有历史保留期，本会话未修改 |

R809 原 input bundle 为 279,221,663 字节，
SHA `13a9486fff42b5150a5177c49aaee8a1c6790776df886a0f9ed9f865ea46827f`。
R824 首 scope input bundle 为 612,745,716 字节，
SHA `71b16a02e29ecd682b23ab2cfa475194188acdb41c0380561eeb9af9580983ac`。
这些成功产物的原全 manifest / carrier 审核已登记；此处没有重新下载大 carrier。

## R815 自身的最小闭包

frozen `prepare_inputs` 的消费集合是 R806 的 45 个原文件与
R813 的 8 个原文件，合计 53 个。它先逐 SHA 验证选择集合，
写并核 `R815-retained-producer-inputs.tar.gz`，
再启动数学进程。因此一个完成端点的实际
`retained-inputs-receipt.json` 会给出这 53 项的具体 bytes/SHA。

目前仅知道工作流数学步仍在运行；这个 step 还包含准备 IO，
所以不能仅凭 step 状态登记 carrier 已经公开保全。
结束后须读真实 receipt / manifest / bundle spec，再登记覆盖。
R815 carrier 不需要且不含 R790 CM 行、R791 tangent 或旧 S5 的全部 q 行。

## 结束后的最小读取

约 18:35 UTC 预算边界后，先核真实 run/job 结束状态与 artifact metadata。
只 Range 读取 reference、全 manifest、run/core/input receipt、原 core log，
以及已经存在的 g / Gamma 完整 index、最新小 CRT-step receipt。
从小 receipt 与 manifest 的 current spec 相等核实际 prime count；
若原子写入边界使两者不相等，只报告未知，不猜 current 的位数。

整个大 CRT 和矩阵行不用为状态检查重新下载。
同核续算本身仍由原 wrapper 完整流式核前次 ZIP、
全部 manifest 成员及自己的 53 文件 carrier。
所有原数学 core / source identity 保持不变。

未来 12 小时没有新保活的必要。
若 β 尚未消费而接近明晨期限，优先仅 IO 携带
R790 的 146 行和 R791 tangent / 所需原 metadata；
不能重算这些已成数据，也不能以 R815 carrier 已有其他输入代替它们。
