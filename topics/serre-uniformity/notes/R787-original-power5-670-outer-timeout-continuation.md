# R787：原 670 位完整断点与缺 core receipt 的严格 IO 续接

## 1. 实际结束状态

原同核心计算 run `43846878233`、job `133229330888`、source
`fe3da6c73f0b1ea87a9b57f5f520eca8647ec1e9` 已结束。实际 run receipt
记 `complete=false`、`process_exit_code=124`、`core_receipt_sha256=null`，
错误为外层预算停止后的断点保留提示；其 `finished_at_utc` 是
`2026-11-16T15:16:16.224092+00:00`。原 archive 确无 `core-receipt.json`。
这不是特征零关系成功，也不补造 core receipt 或核心正常退出的声明。

实际公开纯 IO v23（run `43895402826`）读取原 manifest、reference、
public input、run receipt、history、compaction、chart、selection 和日志。
原日志最后完整阶段是 670 位；history 有 670 条已成 lift 身份。

| 对象 | 字节数 | SHA-256 |
|---|---:|---|
| 原 artifact `14237434353` | 472657363 | `85bb473206cad22c1b59a7cdf3ddd23373e9acd0f0818c110c3b62aadcf1c025` |
| `full-outputs-manifest.json`（1261 项） | 430387 | `f756e25445ff7916d16fad4e1a4b19c84ae18ba54b124ff8d59e26c53848ac1c` |
| `R787-prime-1000000753-dixon-00000670.json.gz` | 94621748 | `8c9052ec2df798620d6be59cc0aa27e34d3c3f30eab5883446d06c9021d7718b` |
| `dixon-checkpoint-history.json` | 157110 | `c1d693569ee04120eb11fddf2d63504b63acdf78e3c48f8d4a5f62d7f857c2c1` |
| `R787-retained-producer-inputs.tar.gz` | 123713383 | `2f4371c94e36372b2eeb9291d75479ccbe2432abe741dc9ecbebab78e9046e92` |

原 artifact 名是
`serre-global-R787-original-power5-function-relation-43846878233-1`，
平台到期时间 `2026-11-17T15:17:40Z`。669 位前驱摘要为
`5fc63ba102607e192aa96c60442e88281b8a8085eb37ab7599604c9508a1bbbc`。
原 compaction 记只移除 76 个被替代的完整 lift，身份仍在 history，
没有删除其他已成阶段，也没有改变数学 checkpoint 字节。

v23 运输只包含小 metadata，不包含 94.6 MB lift 或原 123.7 MB 输入包。
它不替代原 artifact。新续接请求直接绑定上述原 artifact 与完整 manifest。
此次小 IO 没有重哈希全部大文件；下一公开恢复沿原 wrapper 的流式整 ZIP
及全部 manifest 成员逐字节 SHA 核验，并实际读取完整 lift。

## 2. 唯一 IO 修复

冻结旧 wrapper SHA
`42157e0d95eb5d9aed28ef828a86dc5e7bec89e806e3e0a92aa0bcb1a36988b6`
在 `streamed_original_outputs` 无条件读取 core receipt，因此不能消费这个
真实外层 timeout 产物。新分支仅在以下条件同时成立时允许该文件缺失：

1. 来源被固定为实际失败 run，且原 run receipt 是 `complete=false`。
2. 原 `process_exit_code` 恰为 `124`，`core_receipt_sha256` 恰为 `null`。
3. 不存在 `complete=true` 的最终证书。
4. 原 public input 的结果、仓库、run/source 身份与核心 SHA 均照常核对。

有 core receipt 时保留原结果、摘要、核心和 complete 断言；缺失时不生成替代
receipt。新的 resume review 显式记真实 `source_core_receipt_present=false`
及外层 timeout 分支。全部 ZIP/成员 hash、1372 原输入、14 个已成 Schur 分支、
完整配置同一性、670 lift 的完整原模关系和前驱 history 乘接检查均保持原样。

## 3. 同核心续算请求

数学核心仍是
`93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04`。
原 field core、R786 证明、R787 方法、1372 输入、实际素数、原 free1186 方向、
14 分支、每 8 位重构规则及 300 分钟预算不变。请求仅更新 `resume` 为本次
真实 670 原 archive，以及本次严格 IO wrapper 的新 SHA。

新 wrapper：39571 B，
`dff10f4528eac7b8d5501e18d113aa7151c63d31ab236dc097b8de2ed4cd047c`。
新请求：3722 B，
`0ef37410cc917490bbdfde04764ce6b1700292a7bf093d672d388e720f94a95e`。

本次只作源码和源身份 IO；本地仅 AST 解析，没有导入数学核心，没有新算术，
没有启动重复 run。恢复从最新 670 完整阶段继续，不退回 594 祖先。
