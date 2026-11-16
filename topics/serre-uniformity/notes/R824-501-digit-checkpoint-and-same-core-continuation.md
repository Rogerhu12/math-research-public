# R824：原 free1187 的 501 位完整断点与同核续算

日期：2026-11-16。状态：**真实预算断点；原 27 个新权五和 244 个权六准确生成元尚未全部完成。**

## 1. 实际结束状态

[run43762208712](https://github.com/Rogerhu12/math-research-public/actions/runs/43762208712)，job132959291421，
source a75fdaa7cd40e81dbf1026767025e58044b3befb，
于 2026-11-16 02:14:13.680397 UTC 结束，退出码 1。
run receipt 的 error=null；核心为 BudgetStop：
“Only complete source-bound stages and each latest lift need continuation.”

原权五 free1187 从旧 365 位续至第 **501 位完整 lift**，
history/current 均 complete=true；预算在下一次 correction 之前检查而止。
这不是原准确关系不存在的结论，也不是数学拒证。

冻结 core：
1ece3cf45f57fda2d1fe40f38efb3e225d2e05ce910a917eb38dbcd85fe3d1cb；
冻结 wrapper：
c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c。
原 requested_scopes、reconstruct_every_digits=8、budget_minutes=300 及全部八组 producer 不变。
原 free1186 留给 R787，本任务没有重算该目标。

## 2. 已读取的小型断点身份

本地仅执行原字节 Range 读取、SHA256、JSON/schema 身份比对。
13 次 Range 共 575116 字节，读取原 manifest、run/core/input、
current 与第 501 位 history；未下载整个 1.378 GB ZIP 或 70.79 MB lift。
API 所报 archive digest 与选定来源一致；
此次只重新摘要实际下载成员，不声称重新摘要完整 ZIP。

| 文件 | 字节 | SHA256 |
|---|---:|---|
| full-outputs-manifest.json | 215784 | d2d54554c7bd16750931c6073cd5a4ad597dff11c75d08d00fcff7985f5f02bb |
| run-receipt.json | 425 | fe338299087a86848f3cb602bd627b1994f724199c7f7ea33d6c6466f36d7784 |
| core-receipt.json | 362 | a7f49478d6fed8a00f5c8cc39e82e535396f603799eb568e91dc48942b5f210c |
| public-actions-input.json | 10059 | ee8df36910cecaf5f708b9dc63748833d4027ca5ae6dfcef5b5d3ea73daf3bbb |
| R824-power5-free-1187-current.json.gz | 5694 | cd8dcb116296db6c7725a2e112ea3a6d3743afcdfa4b512afb7d83f2e70f7aae |
| R824-power5-free-1187-history-00000501.json.gz | 5743 | 01f47338d38a0cf664db1aee26a10d486599f65265f3b4d851a207f39c8b8ed9 |

原 manifest 共 861 项。实际 current 与 history 的完整 configuration、
target_configuration 相等；current 的 history/lift 规格与 manifest 相等，
history 的 new_complete_lift 也是同一最新 lift。
实际 public-actions-input.job 与本次修改前请求的 job 完全相等。

最新 lift 为 R824-power5-free-1187-lift-00000501.json.gz，
70788183 字节，
SHA256 a2f5c38c6d5d4aabac95b9d9b88a157ea41eb11a9765c1e1731f5fb263240eb9。
前一第 500 位仅保历史规格，large_historical_vectors_retained=false。

仍为原 ell=1000000753、free1187、“该原 L 自由坐标为 1、其余为 0”归一化，
原 280 维有理域基、129/142 阶、原清分母算子与十四支 chart 不变。
原必要输入包仍为 612745716 字节，
71b16a02e29ecd682b23ab2cfa475194188acdb41c0380561eeb9af9580983ac；
retained-inputs-receipt.json 仍为 1098638 字节，
917d5a344a4dac6c457a857ec4382cd950139e6292a86a5268102269156f3cb2。
这些大成员只读取原 manifest 的身份，实际恢复与全 SHA 认证由冻结公开 wrapper 完成。

## 3. 只续接同一核心

本次仅替换 R824-public-original-global-polar-generators-request.json 的 job.resume：

- run43762208712 / source a75fdaa7cd40e81dbf1026767025e58044b3befb；
- artifact14192476595，serre-global-R824-original-global-polar-generators-43762208712-1；
- ZIP 1377996593 字节，SHA256 7f1c8d822df115d4c3f676d8fec6f0a10be63710fd7ac2af4920d8460f904c9f；
- manifest d2d54554c7bd16750931c6073cd5a4ad597dff11c75d08d00fcff7985f5f02bb，
  expected_conclusion=failure，到期 2026-11-17 02:14:14 UTC。

原 core、wrapper、proof、method、field core、输入顺序、prime 与搜索参数一律不改。
冻结 wrapper 恢复已完成阶段和最后完整 current，从第 502 位继续，
不重复旧 Schur 逆、初始 profile 或 501 个已完成 lift。
本条没有新增准确 A/B、极模生成元、eta 或高度结论。
