# coupling112 首次实跑：真正零锚复用成功，尚未请求新 H

公开 Actions run **43590496434**、job **132434008353** 的 coupling112 实际产物，
源码提交 `eef66c977ee41bd1521cad61282301daeaea6e81`。本条只核尾 client、缓存和实际
worker 调用边界；前缀 QR/Newton/回溯的分析另列。失败产物完整保留，不能称为新非零尾失败。

## 原始记录给出的边界

`true-tail_imported-zero-uses.jsonl` 恰有一条
`completed_actual_zero_response_reused`。该请求的 **112 项 H 全部精确等于零**
（记录为 `-0.0`），`jacobian=true`、`audit=false`。没有把小非零系数截成零。
复用来源是已经完成的 T112/N2048 真非线性 solve/full-J/audit：

- 原 response SHA256：
  `6b4ff3e5bc11e23419242ee018b668c57f08b6dbdd791cd43d81883bf6f4960e`。
- 实际新 worker solve 数：**0**。
- worker 已启动并产生 ready；trace 只有 `2026-11-14T11:33:34.937Z` 的
  `tail_variational_backend` 一行，**没有 request、iteration 或 response**。
- stderr 为 **0 B**；没有新的 `true-tail_0001.json.gz` 或 trial diagnostic。
- 原服务器内部 tangent predictor 没有被导入或伪造；本次尚未触发其新的非零初始 solve。

`driver-status.json` 记录 `outer=0`、`phase=inner-newton-not-accepted`，
elapsed **299.57870137300006 s**，inner status **2**、消息为 singular collocation
Jacobian，输出 966 nodes、RMS 为 null、affine BC 为
`1.3378388679289559e-8`。这里只用这些状态定位停止边界，不由 singular 消息单独判断
前缀失败根因。完整非线性耦合尚未接受，未到产生新 H 后调用实际尾的阶段。

## 保存的 anchor 确实是原实际 J

对归档原字节做结构核对，`outer-00-anchor-tail.json.gz` 的整个 JSON 对象与
原 `tail_0001.json.gz.response` **完全相同**，包括：

- 全部 **37,856 = (3×112+2)×112** 个 J 项；
- 全部三个非均值 jet、四个 mean 字段及八项 audit；
- 完整 checkpoint、全部 states 和 rawStates。

这不是 ready 的线性参考代替真 J。输入 config 字节 SHA 仍为
`01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`。
import manifest 保留 89 项数学源码身份比较；input/runtime config 两项单独绑定，
仅排除声明的输出路径差异。原公开提交和本次提交可以不同，但数学源和数值配置仍相同。

原 T112 零锚的独立 Darboux J 审计和 ready/actual-J 差异见
[实际 T112 零锚记录](2026-11-14-actual-T112-zero-anchor-and-J-audit.md)。
本次没有重新计算该审计，也没有修改原 response。

## 实际文件的 SHA256

| 文件 | bytes | SHA256 |
|---|---:|---|
| `full-DN112/outer-00-anchor-tail.json.gz` | 6815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| `full-DN112/true-tail_imported-zero-uses.jsonl` | 1092 | `e3b877eff764e32d38a2a23d020aa6a2c49d15615c7f61b71e74fa5ecaaec58f` |
| `full-DN112/true-tail_imported-zero.json` | 23371 | `64567c40ffa38a73c7ea45da94b0a1fd9fc300f00d3308beb298ef6ad137adcb` |
| `full-DN112/true-tail_ready.json.gz` | 6843 | `6fcb2537cba10b51f5fbea8a322456c15f4dc25b2bcdf225c237a131dacf6894` |
| `full-DN112/true-tail_trace.jsonl` | 158 | `b615b1cc10b9bd2f96d9e64cbdff78b7a4d0cb8581e8e711d3ce18f03a10aaa0` |
| `full-DN112-tail-diagnostics.json.gz` | 2809 | `3a5b9915de2142e9591ca15e7d9753de379638ad5902f1de4e22f34c27ed6b5e` |
| `full-DN112/driver-status.json` | 80656 | `7e9ad939221a79e02cd52500319a788c3a2df1065d1168dac11c6cf6d8e6fca9` |

因此，若下一次仍用完全相同的 T112/N2048 数值配置和源码，并从精确 H=0 初始态开始，
可以继续按现有严格缓存规则复用已完成零锚，无须重复其 1351.74 s 求解。
任何新 H、任何 audited 请求仍须进入原真实 worker；这次失败没有提供其行为的新证据。
本条不修改门、尾源或接受状态，也不产生闭曲面/同 g 极限结论。
