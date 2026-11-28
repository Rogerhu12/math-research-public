# TC2677：从已结束运行的完整并集继续真正试探列

2026-11-28，`visible-exact-astra-b0d5a16-20261128`。

这是执行状态与续接说明，不是完整逆或闭曲面存在性结论。

原 run [45928452441/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45928452441)
于 2026-11-27 07:08:54 UTC 结束。整个原 signed matrix 成功保留；
negative/positive 全源目标仍未完成。完整回执如下（路径前缀
`notes/true_root_trial_residual_ci/run-45928452441-1/`）：

| 文件 | bytes | SHA-256 |
|---|---:|---|
| actual-trial-state.json | 45856 | f43017eb8eb66657bcfb6c743609867e4009e5534d4979bc02fd1c8bb44b9205 |
| complete-radial-integration-prefix.json | 9552 | e49d9c118655b78e9ac2335b1fab45c0c231dd004cee6675207b8c3d9b3bafd1 |
| complete-signed-trial-matrices.json | 13137 | f2cc92916a9d39e9f8f418861029de00b7b973aef09384a00c339edfad1cd247 |
| execution.json | 26901 | 3f8a8ee767b93f530d47332b5814073347082e1fe9e8ea0164db49f6bd6439ee |

原 seed 为前 992 格。三个固定互斥分片及实际游标是：

| 原分片（左闭右开） | 已接受终点 | 本片完整格数 |
|---|---:|---:|
| [992,3236) | 1605 | 613 |
| [3236,5480) | 3788 | 552 |
| [5480,7724) | 6000 | 520 |

因此完整并集为 $992+613+552+520=2677$ 格，连续前缀为 1605 格。
新入口保留原 seed、原分片、每格全部 96 列和五个源窗口，以及整份
精确 hexadecimal upper sums；仅继续 [1605,3236)、[3788,5480)、
[6000,7724) 的共 5047 个未接受单元。不会把并集误作连续前缀。

`make_true_root_saved_union_continuation.py` 只生成新输入清单和唯一
push 工作流。原 TCXV owner、vector scheduler、所有科学源码、四个
完整试探数组的身份、真实根、物理单位、原两 mean、原运行参数、
SkylakeX 必要输入恢复和 Haswell 试探选择都不变。它调用原 owner
的完整前驱准入，确认整并集及旧 matrix 可直接消费。原 manifest
与全部 current/historical descriptors 保留；只从新 roles 表删除
五个仅旧 generator 使用的冗余 original992 别名，原别名仍完整
保存在作为输入的旧 manifest 中。

新增 `.github/workflows/fourfold-codazzi-true-root-trials-complete2677-public.yml`
用于该唯一续接，仍使用原 concurrency group；不 dispatch 或重跑旧
工作流。其新 consumed marker 防止重复启动同一入口。每次完成后的
实际新格数、源范数和终态以该次完整输出为准。

SL 的低逆、真正 PDE 列误差、有限/无限反馈、两 mean、真实参数
Schur 和最终固定度量闭曲面族依然是独立未付条件。
