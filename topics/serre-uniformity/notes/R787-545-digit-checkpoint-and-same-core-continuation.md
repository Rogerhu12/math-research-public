# R787：545 位实际断点与同核心接续

日期：2026-11-16。状态：**原特征零关系尚未完成；本记录只登记已结束公开任务的真实断点和接续参数。**

## 已结束来源与实际终点

原公开 [run 43795851660](https://github.com/Rogerhu12/math-research-public/actions/runs/43795851660)，计算 job `133064488949`，source `9eeabe9c55d8ab6f8bea1e82d8ab7e1e2c60e8a0`。本轮从原 518 位继续，core receipt 明确为 `BudgetStop`，全部已成阶段保留；run receipt 于 `2026-11-16T05:05:18.530084+00:00` 结束，退出码 1、complete=false。完整关系证书不存在，不据此断言关系不存在、545 位不足或新的 q 排除。

| 原对象 | 字节数 | SHA256 |
|---|---:|---|
| 一日 artifact 14198754717 | 455011874 | a188db0f5b825e54412ef73926d92b6b29263db84216ae7447800106124758c6 |
| full-outputs-manifest.json（1262 项） | 430709 | 66c3fdb028cdfc6badb32e0115174338bd8f4152510a53972d00f6048799a4be |
| R787-prime-1000000753-dixon-00000545.json.gz | 76988028 | 2aa942595340b7c56b9747a9f9dd1eac690df812cb145222927aaacdbf53fdeb |
| dixon-checkpoint-history.json（545 条） | 127113 | 4fc18ea3efe09707fb29eb7c3c520ad6615c8aa61baa1eb885a505c0a4006e2c |
| dixon-output-compaction-receipt.json | 761 | 7a51ea65d93a7d46c7237229ba22dc87e4ac0ba82c0055629948833861cd0c77 |
| core-receipt.json | 308 | ec4673e2b51e4b3e47b2fbea4ac75c34c7923e90d47ab3f80110cf35f426e8f7 |

Artifact 名 `serre-global-R787-original-power5-function-relation-43795851660-1`，到期 `2026-11-17T05:05:48Z`。原 chart 为 `47ac1ce2a95781417a4e3b51f2128d2dd4836e5d1793cf2a50793911dcedce96`，selection 为 `a420d94a9a2f56fa449946bac6379f437e7e53120a651d7df95b5f9ef9b07adb`；保持同一辅助素数1000000753、free1186与14分支。

## 实际源读取范围

本次只有原源 IO：核真实 run/source/artifact/digest，逐 SHA 读完整 manifest 和九件小 metadata/history/chart/selection/log。12 次 HTTP Range 实际传输264566字节；manifest、545条历史与compaction中最新完整lift的身份一致。

本次没有下载或重新哈希全部 ZIP、大 lift 或旧分支向量。上表大对象的身份来自已哈希原manifest和GitHub artifact digest；后继冻结恢复器会流式核完整ZIP、manifest和所有恢复成员，再载入同一最新lift。没有本地数学或raw入Git/Release。

## 同一数学任务立即续接

[公开请求](R787-public-original-power5-relation-request.json)只修改job.resume为上述真实producer/artifact/manifest；预算保持120分钟。core `93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04`、wrapper `42157e0d95eb5d9aed28ef828a86dc5e7bec89e806e3e0a92aa0bcb1a36988b6`、原R781/R786、域核心/证明/方法、free1186与完整乘回条件不变。auxiliary_prime_start仍1000000007，每八位重建策略不变。

从实际545位向546位推进，1–545位不重求；只继续尚未完成的下一residual/correction或重建阶段。原518全格56个已闭结论直接继承，不因新lift重跑旧格。新run/job/source在推送触发后从实际Actions取得，记入HANDOFF。

原展开函数、A.1、β/η、原高度与全p一致性均未完成。
