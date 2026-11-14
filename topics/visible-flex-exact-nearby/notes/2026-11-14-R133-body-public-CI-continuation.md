# 全 regular 主体相关残差的公开 Actions 接续

2026-11-14。本文件登记恢复的实际检查点及新执行计划。全 7721 行尚未
由本计划完成；精确 mean 误差传播、完整连续逆和真正 ν Schur 仍不能从
已有有限提案或这些局部行直接推出。

## 原进程的真实终点

旧 `correlated-chain-left-resume26` 实际命令直接调用原 row producer，
只有 `--first 1 --count 256`，没有继续至 4000 的外层 chain。现存过程
记录已经 `state=finished, actual_returncode=0`，其原 native 完整覆盖
`[1,257)`，共 256 行。与此前独立完成的第 0 行合起来，已完整覆盖
`[0,257)`。不能继续把旧计划写成正在跑到 4000。

旧右进程请求 `[4000,4256)`，实际退出码为 `-9`。原 native 保存了
第 4000–4058 行，共 59 行；`selected_cells_complete=false`、
`failure=null`。本次原字节保留该前缀和原进程记录，不把它改成正常
完成，也不猜测原进程被终止的原因。

两份恢复记录是：

- `2026-11-14-R133-body-CI-original-left1-257-native.json.gz`
  及同名前缀的 `process.json`；native SHA256
  `176ac5a3a78ed48fc5e12cf54f604e554138fed28a42b3b9fcead65c79d297e8`。
- `2026-11-14-R133-body-CI-original-right4000-4059-native.json.gz`
  及同名前缀的 `process.json`；native SHA256
  `2722467d9e18e9677106b9e1611d2ca30b7949dd1a491f7c32e382b254cac4a4`。

原先五个独立成功行 `0,477,1000,6000,7719`、新恢复的完整
`[1,257)` 及右 59 行的全部科学身份逐项相同，producer 仍为
`fourfold_codazzi_correlated_head_residual_rows.py`，SHA256
`1651f6cf73af9f3c16061767cc5acff0c452ada183422f7efb983ec8a6d4eb07`。

## 最小固定 trial 输入

不重新求解已经完成的 193 态、6145 节点响应及伴随 QR 问题。
新目录 `data/body_regular_nodal_resume_20261114/` 保存两份原
`answer-0.npy` 的完整、无损字节分片，以及两份原 finite native 和
四份原 full/nonmean trial index。13 件总计 18,566,442 字节；每个
大文件已经 gzip 压缩，单文件均小于 5 MB。没有保存可重算的 QR 因子、
完整 cubic 数组或四套约 146 MB 的完整 Hermite 分片。

每份完整 nodal answer 都有 9,488,016 字节。其原 SHA256 为：

| 角色 | 原 nodal answer SHA256 |
| --- | --- |
| response | `5d69eabc45757f91a4739c58114310c5534ac1a84e01e54233188dfffa567b1c` |
| adjoint | `536a6777217446b193fc1b44f3eb202825c356d6aa0b393fdf4a75de756402c5` |

新 `fourfold_codazzi_regular_trial_from_fixed_nodes.py` 恢复以上字节，
确认原 `FinalHead.identity`，调用未修改的原
`incremental_spline`，并要求生成的完整 `trial-cubic.npy` 与原 SHA256
相等。它随后按原 metadata 生成 full 和显式零 mean 的 nonmean 分片，
要求四份 index 及其每一份分片全部与原 SHA256 相等。新执行记录与原
finite native 分开；原 case 指向旧 nodal 求解，不冒称本次又执行了
原 QR 或原独立后向检查。

原两份完整 cubic SHA256 为：

| 角色 | 原完整 cubic SHA256 |
| --- | --- |
| response | `3484712c492440e15bfd15607b5e66aa317288bd0271710cca7cc5ec82ce9402` |
| adjoint | `f8ff095fb61e12ffeb2c8b1f6720857e8e42f5cb7ad8cc720a0b9f8106d61f04` |

这些相等检查包括全部单侧径向导数、全部 193 个状态和完整 finite
mean。若另一台机器的 BLAS、序列化或压缩结果不一致，记录实际失败，
保留实际产物，不改期望 SHA，不默默改为另一份近似解。

完整 ac1 背景直接复用已公开的
`data/phase_transport_resume127_20261114/candidate/` 六件原文件，
index SHA256 仍是
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`。
原完整 scalar mean native 从已公开的
`2026-11-14-R133-final-complete-scalar-mean-native-binary-parts.json`
及其五片恢复，要求原 gzip 容器 SHA256
`e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b`。

## 互斥完整覆盖

一次 prepare 重建原 trial，然后八个 worker 共用同一 Actions artifact。
四个左区间补上旧命令实际没有派发的部分；四个右区间继续原右前缀。

| worker 区间 | 已有行的处理 |
| --- | --- |
| `[257,1200)` | 跳过已成功的 477 和 1000 |
| `[1200,2133)` | 全部待算 |
| `[2133,3066)` | 全部待算 |
| `[3066,4000)` | 全部待算 |
| `[4000,5000)` | 首个 `[4000,4256)` 原子段恢复原 59 行 |
| `[5000,6000)` | 全部待算 |
| `[6001,6860)` | 第 6000 行由原独立 native 提供 |
| `[6860,7721)` | 跳过 7719，仍明确计算末行 7720 |

每个 worker 再按原节点编号分成不超过 256 行的原子段，共 34 段。
六份已完整 native 一共 261 行；加上原 59 行成功前缀，实际仍需
7,401 条新行。manifest 已对每一个整数行编号逐项检查：完整旧行与
本次原子段的并集恰是 `[0,7721)`，无遗漏、无重复。59 行前缀只作为
其原 `[4000,4256)` 段的 resume 输入，未另算一次。

`fourfold_codazzi_body_CI_worker.py` 调用原 producer 的真实命令，保留
它的全部源、完整输入路径身份、whole η 半宽 `1/1000000000`、512
个完整角节点、有限乘积高输出和完整原始 mean。原绝对路径只在全新
runner 上映射到已核 SHA 的 artifact；本地旧 scratch 不被写入。
每次 rerun 选择同身份、同原子段的最远成功前缀；已完整原子段直接
消费原字节，不重算。

## 执行及实际轻门

工作流是 `.github/workflows/visible-exact-correlated-body.yml`。
117 个固定文件（其中 77 个源）列在
`2026-11-14-R133-body-CI-pinned-inputs.json`；Python 3.12.14、
NumPy 2.3.5、SciPy 1.17.0、python-flint 0.9.0、SymPy 1.14.0、
mpmath 1.3.0 和单线程 BLAS 与原记录一致。

本地仅执行了 3.815 秒的实际轻门：两个 nodal answer 的完整 SHA
还原正确；新路径下 `model.identity` 与原值相等；两个角色各自首片
和末片的全部 `4 × 193` 个 cubic 浮点值逐位等于原片。该轻门没有
重新执行全部 6144 个 trial 片，也没有计算任何新的主体残差行。
所有固定源均通过语法解析，工作流 YAML 与八区间 manifest 一致。
完整 trial 重建及新主体残差只由公开仓库自己的 Actions 实际执行。

worker 先把已核 SHA 的源和输入复制到不可变计算目录，避免正在跑的
数学进程受 `git pull` 影响。每 10 分钟以及每个原子段结束都实际
`pull --rebase`，核两份 README 差异并发布小 native、stdout 和真实
进程记录；非快进立即 rebase 后重推。完整 trial 数组只通过 Actions
artifact 传递，native 超过单件限制时用原字节无损分片保存。实际失败
同样保存，不把检查点、预定范围或正常退出以外的状态改写为完成。

本次仍是原 ac1 算子的全主体相关残差任务。它不会自动把这些行转授
给连续修复后的中心。即使所有行完成，还须实际调用原精确 mean
误差消费者，保留全部原试函数 mean 跳跃和非 mean 跳跃，再支付真实
边界、连续主体逆、无限高模反馈、Schur 及非线性闭合的各项条件。
