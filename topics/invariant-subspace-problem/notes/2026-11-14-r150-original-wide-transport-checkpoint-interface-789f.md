# R150：原始全多项式运输的 u16 trace 与真实数组检查点

日期：2026-11-14。实现文件建议：
`2026-11-14-r150-original-wide-transport-checkpoint-789f.cpp`。

本件只实现已有原始 DAG 运输的格式扩展和恢复协议；没有执行
197 个第三相关像或任何新的数学计算。本文也不声称代码已经编译。
真实模数乘回、CRT 和原 17 行来源核验仍由连续主 runner 完成。

## 1. 原实现与不变的数学操作

以 `2026-11-14-r150-ninth-first-transport-789f.cpp`
的实际 blob `2f6efa7911d854c487dc86d5757e441bbbf27ee8`
为基线；依赖文件
`2026-11-14-r150-ninth-first-common-789f.hpp`
实际 blob `37c69d325fa302b50634bea67a0836a320e5fa9c`
不作修改。其 bitplane 依赖实际 blob
`92d6e52a3fd6ce0ff953c66ca8ca3c036d1e6b9c`。

输入原 2195 源首先按完整 normal trace 累加
`-H C`；全部实际 RHS mixture trace 再累加
`J_rhs`。之后依原 backward DAG 和 forward DAG
还原真实 6188 原始来源。保留原完整计数：

- normal 源 trace：2204 行、25,305,683 项；
- backward DAG：3333 行、1,010,703 项；
- forward DAG：3333 行、782,976 项；
- 原 2195 非 prebasis 行与 3333 prebasis 行互不重合，
  共 5528 个选中原始来源；其余 660 行输出零。

本件不更换任何 source 字典、scale、符号、原始行代价
`model.delta(raw)` 或操作顺序。全过程仍在
\(\mathbf F_{31}\) 的 5 个 bitplane 中进行。

## 2. 两种 trace 精确格式

读取每个 normal / RHS trace 时单独识别 8 字节 magic。

| Magic | 指数 | 每项其余字段 |
|---|---:|---|
| `R150NR31` | little-endian u8 | basis u16、系数 u8 |
| `R150NW31` | little-endian u16 | basis u16、系数 u8 |

每行的 raw u32、label u16、operation-count u32 不变；wide
不是将已有 u8 文件重新解释。实际有非零乘子的每项仍检查运输后
多项式次数不超过 `P=B-10`。零乘子的 trace 行完整读过，
但不凭该无效乘子的指数额外限制来源代价。

仍要求 `B=N+96<=796`、`N=mix.bound`。
旧 mixture 输入和完成源 `R150SC31` 格式不变。

## 3. CLI

```text
PROGRAM completed-source model normal forward backward mix out-prefix \
        checkpoint-dir runner-sha256 remaining-seconds
```

前三至第七个输入参数及输出前缀与原程序一致；新增三个末尾参数。
`runner-sha256` 必须为 64 位小写 SHA256。runner 应令它绑定本次
源码、依赖及真实输入 manifest；程序进一步重新计算源、model、
normal、forward、backward 以及每族实际 NF / quotient / remainder / trace 文件的 SHA256。
mixture 绑定使用解析后的 count、bound、目标 labels、按原次序的每族 count、labels
和所有已模 31 规范化的多项式长度/系数；用固定整数文本语法生成 canonical-mix SHA256。
这些实际字节 SHA、canonical-mix SHA 与版本、实际尺寸和 runner SHA 合成 effective binding。

实际文件路径和 raw mixture 字节均不加入 effective binding；因此恢复目录改变、
mixture 内绝对路径重写但各实际文件 SHA、标签和系数不变时，可以恢复同一数组。
raw mixture SHA 另写入 metadata 的 `rawMixAuditSHA256`，只作审计，不改变绑定。
任何实际来源文件或规范化多项式改变，都会拒绝恢复，不会悄悄清空旧数组后继续。
本修订版本标识为 v3-portable；与之前把 raw mix 字节绑定的 v2 初稿不混用。

`remaining-seconds` 是本次 invocation 从启动计时的剩余预算，
必须为有限正数；不另要求 60 秒的 invocation 最小预算。
预留 `min(30, remaining-seconds/4)` 秒保存，在完整行边界保存后以 exit code 75 返回。
SIGTERM / SIGINT 处理器只设置保存标记，下一完整行边界执行同一检查点流程；
不在信号处理器中执行 I/O。若 runner 的硬超时先中断保存，旧活动槽仍保持完整。
普通失败以 1 返回；完整原始运输输出完成才返回 0。
周期检查点约每 120 秒一次，阶段结束也保存。
初始化输入散列及一次完整原始源读取发生在首次数组检查点之前；
它们未形成可复用的部分数学来源。

## 4. 检查点内容与原子性

检查点目录采用互斥文件锁，避免两次进程共同写同一状态。
`active.txt` 只指向两个轮换槽中的一个，并附 manifest SHA256。
一次保存先写不活动槽的临时目录，完成所有真实数组分片和 manifest 后，
才原子更换 active 指针。之前的活动槽在此之前保持可读。
不依赖仅打印在日志中的进度。

manifest 含：

- 版本、runner SHA、effective binding、目标数、\(B,PW\)；
- 实际 phase、下一行、当前 family、准确 trace 字节偏移；
- normal / active-normal / RHS / backward / forward 操作累计数；
- 完整 raw \(6188\times5PW\) 与 beta \(3333\times5PW\) 数组；
- 每片对应数组、连续 word 偏移、真实 word 数及 SHA256。

阶段 1 是源 trace，2 是 RHS mixture，3 是反向 DAG，4 是正向 DAG，
5 是两次 DAG 均完成且可重写输出。每个游标只在一整行的全部 bitplane
累加完成之后更新；所以恢复时不重复应用已提交的某一行。
trace 阶段使用保存的实际字节偏移；DAG 阶段重新读取完整不变 DAG，
只继续未完成的逆序行。

恢复同时检查每个 bitplane 的 padding、非法系数 31、尺寸、全部分片连续
覆盖以及 operation counts。缺片、旧 source 或旧 runner SHA 均被拒绝。

分片采用本件自含的 RLE32，小端 token：高位 1 是 repeated-word run，
高位 0 是 literal words，低 31 位为长度。每片最多 1,000,000 个
decoded words，即 4,000,000 字节；literal run 最多 16,384 words，
因此最坏编码长度仍严格小于十进制 4,500,000 字节。
所有分片都编码，包括不足十进制 1,000,000 字节者；不引入额外压缩库。
SHA256 实现含空串和 `abc` 的已知值启动检查。

## 5. 输出及验证边界

输出仍是完整旧格式
`out-prefix-primitive-source-mod31.bin`（magic `R150PS31`），
先写临时文件，完成后原子更名；metadata 保留
`higherModulusProductVerified=false`。
metadata 新增 input SHA、raw mix 审计 SHA、runner/effective binding、输出 SHA256/字节数、
实际 checkpoint phase/generation。恢复 phase 5 会按已保存 raw 数组重写输出，
不将不存在的输出假记为已完成。

该完整 primitive 文件作为后继乘回的临时本地输入可较大；
总 runner 在仓库持久化时应 gzip / 分片至每件不超过 4,500,000 字节，
保存重建 SHA256。此程序不另写一套同义大输出。

实现未启动任何新的数学运行，也没有用 checkpoint 的存在替代完整
全原始行乘回。它仅使下一次真实正分支可在上述精确状态继续。
