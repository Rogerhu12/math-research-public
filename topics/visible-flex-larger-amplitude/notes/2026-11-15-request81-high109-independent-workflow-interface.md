# 第 81 轮：完整高 109 核两端诊断的独立工作流

类型：计算接口与源静态核对；不是新的数值结果。  
作者：exact_refinement。日期：2026-11-15。

## 1. 文件与调度范围

本稿仅在 `/tmp` 准备，未写仓库、未提交、未 dispatch。建议目标为：

- `.github/workflows/visible-larger-public-high-core-two-end.yml`；
- `topics/visible-flex-larger-amplitude/computations/public-high-core-two-end-request.json`。

触发器仅监听后一请求文件；独立 `high109` job、独立 concurrency group 不改第 80 轮的 small-core 工作流。请求固定第 81 轮，`lanes=["high109"]`。发布复用已存在的 `smallcoreresonance` lane，只是沿用原件发布目录，不把高模结果冒作低三参数求根结果。

| 文件 | 字节数 | SHA-256 |
| --- | ---: | --- |
| `visible-larger-public-high-core-two-end.yml` | 14124 | `fa8b7fe51f3f4a12a0dd826874310bcb943bdac8c45fa2dab58e9124a81be641` |
| `public-high-core-two-end-request.json` | 13808 | `4fdfe80c8140707d627ab22ba33971ea593c81060478e32d7ea1c37ad88f479e` |

上表与随稿静态收据逐字对应。

## 2. 唯一输入点与完整原件

父计算固定实际第 78 轮 run `43662193286`、source `11b5d25c436d84d734a73d4609092bde749daea5`。工作流读取实际四件：

| 相对父目录文件 | 字节数 | SHA-256 |
| --- | ---: | --- |
| `request78-input-and-source-identity.json` | 28516 | `57a5d443b0f13193a385a40a13c5dc038dae768e97095074e08a6edca5fc5b58` |
| `resonance/resonance-status.json` | 50438 | `09031496410951afc018b223b921db111a43b3e0852592b87aafd5351b4f0c40` |
| `resonance/circle-reference.json.gz` | 139996 | `6c56f190c6e07538582bc6271caa6abe9d8eb5c59362579b8f87ee6d13f8afb1` |
| `resonance/complete-scalar-domain.json.gz` | 79207 | `8efa0be35549651bf8f8369cf7587c0b7cda240cebad67569686a9be9242be71` |

父目录是公开仓库 `notes/public-actions-43662193286-1-smallcoreresonance/`。四件在新科学启动前逐字复制到新 artifact 的 `parent78-original/`，保持压缩文件原字节。固定参数仅从实际保存状态读取并交叉核对，不再优化：

`[0.09365081258727412, -0.13201200770909496, -0.12389206129693811]`。

原 M96 accepted、T112 prepared、真实 zero-tail full-J anchor、T112 config 四数学输入与原 78 请求的路径、字节数、SHA 完全相同；完整描述在请求 JSON。新工作流仍恢复原 78 个公开数值源，并设置 `VISIBLE_SOURCE_TOPIC`，不创建新尾求解或新 J。原 68 文件保守来源闭包逐项保持，加新消费者成为 69 项。

第 78 轮低三缺陷仍大，父点不是已得共振根；本诊断不把低三根或先前求根成功设为启动条件，也不将其结果作为任何 native/prefix 计算的验收条件。

## 3. 冻结消费者、运行时与预算

消费者：`exact_20261115_r259_high_core_two_end.py`，49546 B，SHA `f60db29ef0c235cc4d5d2fa2ffecd480dccc4d54b46aafe655a60ba88af7013f`。

原 `geometry_20261114_small_core_resonance.py` 的 SHA `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5` 不变。新消费者的算法、完整 CLI、双模型界限、输出矩阵定义见 [完整接口](2026-11-15-R259-complete-high109-two-end-diagnostic-interface.md)，两端行列式证明见 [R277](../results/R277-complete-two-end-chain-determinant-and-high-core-elimination.md)。

运行时沿原 78：Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0、python-flint 0.9.0，三个 BLAS 线程环境均为 1。工作流传 `--arb-bits 160 --arb-max-bits 640 --budget-seconds 1800 --maximum-integer-bits 4000000`；消费者精度序列为 160、320、640。job 60 分钟、科学 step 45 分钟，给取源、保存和上传留时间；科学预算仍 1800 秒，没有扫描参数。

完整 112 模、699 节点、698 cell 每模均保留。对保存 binary64 L/R 的精确 dyadic 两端行列式，及对声明实离散模型的 Arb 包围，分别保存、分别解释。两者不能互称误差外包；真实尾导数误差、连续 ODE 非共振、低三根与横截性均未据此自动证明。

本次具体最小修复只处理区间循环恰在 while 边界耗尽预算时的状态：若尚有 `pending` 且时间已尽，先在已有 partial 对象标记，再抛 `BudgetExhausted`，最终状态为 `resource-budget-exhausted-with-partial-evidence`。精度上限导致正常 unresolved 仍完成有界诊断。没有改科学公式、模式数或判据。

## 4. 输出、失败保全与发布

根目录为 `$RUNNER_TEMP/visible-high-core-two-end/high109`。新结果在 `high109-diagnostic/`，父四件在 `parent78-original/`，根级另存实际源码身份、准确 argv、源恢复 log、完整科学 log。原 `summary.json` 再作一次只读摘要；没有原 summary 时只记实际缺失，不能制造成功。

完整 artifact 名为 `visible-mainline-high109-${run_id}-${run_attempt}`。`always()` 上传在发布前，保留全部已完成模式/精度、原浮点阵、精确整数、Arb 文本、完整 `result.json.gz` 和 partial；没有按失败状态删大阵。

发布仍调用 SHA `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca` 的原 publisher，仅该步骤提供 `GH_TOKEN`。任何路径分量为 `large-arrays` 的完整文件只在 artifact，不入 Git；原 bounded 小件照现有规则发布。没有 PAT、force push 或新 lane 改动。

## 5. 已完成的本地静态核对

本地只做 AST、Bash 语法、JSON 描述与原文件哈希核对。69 个来源 SHA 均匹配；父四件与实际 78 原件逐字匹配；四数学输入描述与原请求一致；7 段 shell 经 `bash -n`、4 段内嵌 Python 经 AST。四个 B 元素 RHS 与原源 AST 相同；L/R 形成 RHS 与原源 AST 相同。没有 import 或运行科学模块、Arb、整数算子或 toy 计算。

独特源收据为 `2026-11-15-R259-high109-static-source-check.json`，避免覆盖 R276 的 `static-source-check.json`。工作流收据为 `2026-11-15-request81-high109-workflow-static-check.json`；相对原 78 的两份 `.diff` 同目录保留。静态核对仅排查具体接线问题，不构成额外数值门。
