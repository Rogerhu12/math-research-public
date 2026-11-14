# R133 补充：已知高频源成功数学的独立收据与原件恢复

公开 Actions [43630093667](https://github.com/Rogerhu12/math-research-public/actions/runs/43630093667) 已完成六项收据核验。**本次没有数学子进程，没有新源行，没有新 target 求值。** 原 run 43628921664 的数学子进程早已返回 0、7721 行及八门完整通过；随后仅因可选逐行诊断超过 60000 字节而发布失败。本次逐字复用其成功 native 与小摘要，不重跑已成数学，原失败过程继续保留。

## 1. 精确原件

本次目录：

`notes/known_high_Z_tail_receipt_ci/run-43630093667-1-known-high-math-success-receipt/`

| 原件 | SHA256 |
| --- | --- |
| 完整 native，7,508,940 字节，四个 lossless parts | `5ad8aaada967f4626a33e978b1c81adf640ee1abaf0876f54ffd22d6dbd107fd` |
| 原 14,387 字节主摘要 | `74e7b40d0eb4c79bf511a501467e73d80116d46990d1ab8e5b43f66f4fcd1b35` |
| 原 artifact 的成功数学/失败发布 process，20,712 字节 | `085a31c2f760df9076b0aa87672b05becaa1e699838bc14a71438c7592d38496` |
| 当前仓库本次 `process.json`，13,672 字节 | `cfa6bdfd47ce35bb191770d9ed237b86718de7127968f073f4eecf66822e8dae` |
| `evidence/known-high-original-success-receipt.json`，12,445 字节 | `cd7aa5f5c21509c629f8508bef21af4254e05716e2868e1804bce60e1ee583fa` |

原 artifact process 与原仓库 process 快照的 SHA 分别记录，不互相冒用。本次明示接受原 `complete=false`、精确发布错误及唯一数学 child 返回 0；同时核原 source、worker、147 件 manifest、native 全部行序和八门、精确 native 字节 SHA，以及主摘要同一数据身份。

原科学源为 `f9104cce14a3f04ebe3271ed19085d9bf4bdc7f9f7c215ed79dd99244e7034bf`，原 worker 为 `b11f7e85a555b3942d531ce120700c605d081a989abf320ff5758f70e8ee41cd`，原 manifest 为 `de4bd52b27daceb5b3ea85a79c2ba37dd01196143384ffc72d0946dc6826a759`。三者没有修改。新 receipt worker 为 `74a00ec426b897222424ca6a9241d7aa1f2d3b9763529fa2fd6be31671caecee`。

## 2. 数学范围没有扩大

原固定 repaired M32 中心、$\delta=0$、同一完整连续方向 $Z$ 的已知 $97\le |j|\le160$ 源仍满足：

| 径向窗口 | ordinary pair $L^2$ 严格上界 |
| --- | ---: |
| $[0,25/8]$ | $1.456146058343\,10^{-10}$ |
| $[0,9/10]$ | $1.455122185384\,10^{-10}$ |
| 原固定完整负区安全窗口 | $1.415385109261\,10^{-10}$ |

数值和证明的原实际记录见 [完整已知高频源验收](R133-supplement-actual-complete-known-high-source-from-Z-tail.md)。本收据只使成功原件完整出版，不授未知 high 反馈、非零 $\delta$ 背景、完整 PDE 逆或真正参数响应。

本次两次真实 pull/README 检查均为 `changed=false`、实际 diff 为空，最终已读提交
`807ccab534f10a80d53163f88411031656127527`。原大诊断没有再次生成，完整 native 和小主摘要按原字节保留。
