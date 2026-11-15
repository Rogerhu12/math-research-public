# SC 首次实际运行：旧 finish 身份字段的 schema 失败与完整保存范围

**状态：实际运行失败已完整保存；尚未得到任何新 signed functional 分组或最终 affine 界。** 本篇记录公开 Actions 的真实返回，不把输入恢复通过写成新数学结论，也不撤销任何原已成功的 Gram、RW、Green 或 CPA 结论。

## 1. 唯一首次运行及原文件身份

部署提交为 `6994dc1e463ca927a67f60e7f92f7c3f430f5c91`。唯一自动 push 运行是 [43752221411/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43752221411)，job 为 `132928465565`，未另作 dispatch。运行于 2026-11-15 19:24:11 UTC 启动；worker 于 19:24:42.214173 UTC 进入，科学阶段于 19:25:31.813509 UTC 结束，job 最终为 failure。

下列三个小文件由该次 worker 实际发布，内容均已逐字读取并核对 SHA256：

| 原文件 | Git blob | bytes | SHA256 |
|---|---|---:|---|
| [完整科学失败收据](../notes/signed_cap_affine_functional_ci/run-43752221411-1/actual-scientific-conclusion.json) | `4afe582031fae70f9c6f1f03093cb7a80cd5293f` | 3937 | `2e152b087c6686508ec139ef8a766b8176df2e770d995e6fde05b9b640a39fc0` |
| [完整执行记录](../notes/signed_cap_affine_functional_ci/run-43752221411-1/execution.json) | `55c57ae650962c50c7d55c1b3a471f4fa4a93fe4` | 38229 | `649670d89e5b5ab182a901b518b7707805d4f3682c9d0bf3b9576a958ee62972` |
| [实际 worker 报告](../notes/signed_cap_affine_functional_ci/run-43752221411-1/actual-result.md) | `0c824360f024ba2f2d2ed0c6a2f439d4ea42deba` | 4492 | `30b4548e34ac419cba367ceb8b9099bb9d17114a25bb19c586a5cc631a5a596f` |

原新科学源码为 `92ec4392bd5d3e56d5acb10fc616a3a7e0e5718a` / 41640 B / SHA256 `d5f91e7a3b2d981366f659b2777f60b525df5bf3c2d40077e4419477a2c0989b`。manifest 为 `121ced6311ac0cfc57358b931f21e7b8eaf31842` / 38672 B / SHA256 `7b0f87b98ae75a3418c6d4468164b37888c485f0b2f00a6617758a97e43be2c9`。worker 为 `eb2b1c99c31ffe339cdb7eeb6333684cee884229` / 59315 B / SHA256 `414e55cb40c516ad02cbba8ae45ac4772f18545dbbfaab8adae5f2ef2abcf6ce`。

## 2. 实际完成与实际失败

实际科学子进程返回码为 **1**，`complete=false`。它到达了预定 20 门中的前 6 门，其中 5 门通过、第 6 门失败；未到达的其余 14 门没有判定，不计作通过或数学反例。

已通过的五门是：

1. 新源码、运行环境与完整 SC 参数身份相符。
2. 已发表 SA7a、SC18a 与全部原小证书身份相符。
3. 原 7908 个闭区间及完整 32 组 slice plan 覆盖相符。
4. 四个原省略 pilot 的原 midpoint jets 身份相符。
5. 五个原 candidate shards 与完整 canonical centre 相符。

失败发生在 `checked_inputs` 第 193 行调用的门：

`old complete formal field endpoint and value certificates have the same object`。

完整 traceback 已保存在科学收据中。这是输入证书 schema 检验失败；不能把它解释为新的 affine 范数过大、未知解不存在，或原 Gram 证书失败。

执行记录确认已恢复 **36 个原 artifact archive**，合计 912764217 bytes，逐 archive 的原 run、artifact id、原 bytes/SHA 和成员收据都完整保留。另有 32 个 Git 输入身份核验、8 个不可变 Python 文件的 AST 闭包核验；实际运行环境为 Python 3.12.14、python-flint 0.9.0、NumPy 2.3.5、256 bits。原 QR、target、residual norm、Gram、RW 和 Green 数学没有重做；新数组 artifact 与 Release 均为 0。

这是一次真实启动过的科学子进程，不能称为“没有运行”。但源码调用顺序与 traceback 同时证明：本次在 `run → checked_inputs` 中退出，尚未调用新的 `body_run`。因此 **新 signed 分组 0 个，完整 known parameter model 0 个**；不能授予任何新径向矩、97 维 signed affine 向量、posterior 误差或低迹界。

## 3. 已查明的具体 schema 原因

原 [body finish summary](../notes/complete_cap_adjoint_Grams_ci/run-43665656138-1-complete-adjoint-Grams-finish/evidence/complete-adjoint-Grams-finish-summary.json) 是已成功的原完整 7908 union 证书。其固定身份为 7982 B / SHA256 `ca1411120265fac503eba147289da621634cc98304766aa56dfb6da80b5180df`。它的实际字段为：

- `phase="finish"`，`complete=true`，两门均通过，`complete_quarter_count=7908`。
- `object_identity_sha256=null`。
- `plan_native_sha256` 与 `actual_input_sha256.plan` 均为原 plan 的 `93e9b52054d9af86b9f238fb13a4183ec23b90f2e0017676aef4773fa28dce32`。
- 原 finish native 的 SHA256 为 `4e505e025870904f35a160fefb637c72b67b846843d69d07f3ec2d8b2b183b43`。

新 SC 的错误条件要求该 summary 顶层 `object_identity_sha256` 等于原 plan/range 的 object hash `df9844506e25bdd207472fd8f5f7e9fbfaf90514c2e1a3629be2e5594eb25ca0`。原 finish summary 的实际 schema 没有这个非空值，所以该条件必为假。

这与原源码一致。[原 complete-cap Gram producer](../scripts/fourfold_codazzi_complete_cap_adjoint_Grams.py) 的已锁 SHA256 为 `6b3a47a54386171b2c659c776bbfeff52ae0ebe4456ced5b67350f7eabf48a8d`。其 `plan_run` 明写顶层 object hash；其 `finish_run` 核对 32 个真实成功 range、各自 plan 身份和全 7908 来源后，写入 `exact_object_identity=plan[...]` 与 `plan_native_sha256`，没有写该顶层 hash。不能把 plan/range 的字段形状套到 finish summary。

原 [finish process](../notes/complete_cap_adjoint_Grams_ci/run-43665656138-1-complete-adjoint-Grams-finish/process.json) 的固定 SHA256 为 `d28959027cc8a3692a7747fdf333a4d1d47a975dd35f26b850ddd78114a64ea5`。它实际保有同一 plan SHA、同一 finish native SHA、上述 summary 的 7982 B/SHA receipt、child 0 和完整覆盖声明。后续修复应沿这条准确原身份链读取，并保持新 reader 对原 plan 内部 object hash 的严格检查；**不能简单删除对象一致性门或把 null 当通配符**。

原 boundary、RW 和 cut 的完整证书仍须各自保留原 proposal、centre、mean、端点及参数门。本篇没有修改任何旧证书，也未改变旧数学数字。

## 4. 保存与丢失范围

原 child stdout 是 5503 B，SHA256 `ee7c32ab22a10e3cc5b0c751612e5585eb2e8eaafe7f0c476e4686dbe3771b45`。完整 job 日志经 GitHub job-log 工具解码取得 90275 B，SHA256 `b662253890bd9bc3026e7e4f2b25e5cef89730355195bcb045b5502f04b74282`；该身份对应工具返回的完整 UTF-8 文本，不冒称原下载 ZIP 的 SHA。

从日志中去掉 GitHub 的逐行时间戳，原 `SC_COMPLETE_SCIENTIFIC_RESULT_BEGIN/END` 标记之间的 JSON 加末尾 LF，逐字复原得到 3937 B / `2e152b087c6686508ec139ef8a766b8176df2e770d995e6fde05b9b640a39fc0`，与实际发布的小科学文件完全一致。预 Git payload 为 8647 B，封装失败字段为 null；因此本次没有丢失已完成的新科学结论。

runner 的原恢复文件已随作业结束清理，它们只可按原身份再恢复。不存在已成功的新 signed 分组需要重算；也不存在可以假定成功而未保存的 known model。任何后续运行必须先完成上述 schema 修正的独立核对，保留本次失败记录，只执行尚未完成的新目标。

## 5. 数学范围不变

[SC 合同](R133-supplement-exact-radial-subtraction-and-complete-known-cap-affine-moments.md) 与 [SA 完整配对公式](R133-supplement-signed-physical-cap-affine-and-complete-adjoint-receivers.md) 的解析证明不因该字段错误改变。未知量始终是 actual cap 减 repaired centre；radial subtraction 只改变已知配对组织，不能缩小未知 $y$ 的先验。

本次没有支付 selected affine 小门、CPA 五输入的实际 nonlinear/source 负荷、NG 的 low/shell/cut 门、core 自映像或闭曲面结论。全部真实均值、外端、height 与 waist 义务继续保留。
