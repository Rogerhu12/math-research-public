# noJ-primal 多请求 current576：逐请求适配器与 R273 子求解接口

类型：源码实现及接口约定；本文件没有报告新科学计算或 native 接受。

作者：`exact_refinement`。日期：2026-11-15 UTC。

## 1. 已完成的源码范围

本次新建两个独立文件，将已冻结的多请求 current576 适配器与 R273 子求解，接到新的 noJ-primal live client。旧 live 四源、第 61 轮、第 73 轮单请求源码以及 R273 因子和整数核均不改。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `exact_20261114_noj_primal_live_current576_damped_system.py` | 33,197 | `e30e53e635f84ae4762ef045e6510c20d63524efd604ba617cec3a849bdfb3d3` |
| `exact_20261114_noj_primal_live_current576_damped_chain_qr.py` | 22,328 | `c3284d556e76f389d084bc612579c485697f15aeb4c5b7a5caa49567a9920909` |

直接源基线分别为：

- `exact_20261114_live_current576_damped_system.py`，`9346c0a7e7c7f562d20b02126b82c8819c687a7575aea38258e9796cabb8db4a`。
- `exact_20261114_live_current576_damped_chain_qr.py`，`ee174e8283f3b5454a8b3dbe751dbd4f41f4f0dba1bd9d240b627bd2748f889f`。

新的 flow 身份核函数逐字复用第 73 轮单请求 adapter `48297483617c56179fdd4d6b80e9aeeb1151bf89c90fd816ca41d2e3ccc0bcb3` 的 `primal_flow_identity`。完整差异和两个源码静态回执与本接口同批保存。

科学执行仍限定 `GITHUB_ACTIONS=true` 和本公开仓库。这里只执行了标准库源码读取、SHA、AST 和完整差异检查，没有导入两程序，没有构造系统、调用 RHS/J/ODE、执行 QR、范数、作用或有理残差计算。源码静态回执不是新科学通过条件。

## 2. 配套 client 与启动初猜

配套生产者为 geometry 的独立文件：

- `geometry_20261114_noj_primal_live_tail_client.py`；
- `geometry_20261114_noj_primal_live_tail_client_hook.mjs`。

配套总接口见 [noJ-primal live client 与 full-DN 接口](2026-11-15-noJ-primal-live-client-and-full-DN-interface.md)。两端按当前 checkout 的固定 basename 作双向源身份绑定：client 硬锁本次两个 SHA；adapter 对 snapshot 中 launcher/hook SHA 与实际文件逐字核对，避免双向硬编码造成哈希循环。

父锚必须是第 73 轮生产者的实际完成结果，schema 为 `completed-native73-noj-primal-literal-JSON-anchor-v1`。所绑定的生产者源为 `938fbec22f0733fff6ceb22e6e9b7a9e12942c12d1eae31c608d8f517702df8c`，hook 为 `099798e9c57f09b82f7532ea184d124446aeeb2cdbafe452390cb794b8db405d`。父结果和原响应的实际 SHA 由后续输入提供，本次没有填写未来结果 SHA，也没有宣称运行中的第 73 轮已接受。

父锚保留完整 `producer_result`、`original_response`、`parent_primal_flow_installation` 收据，以及 `native_accepted/full_J_returned/full_audit_returned=true` 的实际生产者声明。client 在启动前读取并核原件；每个 snapshot 保存这些完整收据，不在每轮重复装载父大文件。

种子明确使用 `original-response-JSON-decoded-binary64-v1`：原响应 JSON 解码后的完整 577×224 数组重新导出为 raw 和负零 sidecar。这不是对 JSON 序列化前未保存符号零的恢复，`pre_JSON_negative_zero_preservation_claimed=false`。同一 live worker 内仅 bootstrap 的 `native_call=1, iteration=0` 核当前 raw 状态等于这个 literal seed；后续请求不得重置为父状态。第 61 轮失败态固定 SHA `b34…` 不进入本次 adapter 的启动条件。

## 3. 每个请求和每个迭代的真实绑定

`native_call` 必须为正整数；`nonlinear_iteration` 与 `snapshot_sequence` 是该 call 内从零起的相同非负整数。目录由 client 按 `call-0001/iteration-000/{snapshot,qr}` 分离，所有子进程 stdout/stderr 留在对应迭代文件，不进入原 Node JSON 协议 stdout。

每个 snapshot 绑定本次 `current_request` 的完整 `request.json` 和 SHA。其 request 三字段仍为 `height`、`jacobian`、`audit`，高度保留全部 112 模式。`height_negative_zero_columns` 只恢复该次 JS 请求实际导出的负零位，先核排序、范围和每个零字，再与 `physical-height` 的全部 raw bytes 比较。

`bootstrap_request` 与 `seed_assigned` 仅在 call 1 为真。call 1 的 H 必须等于父锚实际 H；后续 call 使用自己的 H、target、σ、原 predictor/fallback 和 live 缓存状态，不强加父 H 相等或 seed 相等。每个请求的 context 还绑定新 `primal_flow_source_sha256`，避免把同一进程后续调用误标为旧 flow。

以下三种 snapshot schema 均为新身份：

| 文件 | schema |
|---|---|
| `result.json` | `noj-primal-live-current-native576-withJ-snapshot-result-v1` |
| `context.json.gz` | `noj-primal-live-current-native576-withJ-snapshot-context-v1` |
| `array-manifest.json` | `noj-primal-live-current-native576-withJ-snapshot-arrays-v1` |

完整当前数组合同保持：

| 数组 | 形状 |
|---|---|
| `base-states` | 577×224 |
| `stage-jacobians` | 576×224×224 |
| `stage-out`、`stage-residuals` | 各 576×224 |
| `original-scales` | 1×577 |
| `cut-residual`、`end-residual`、`original-far-graph`、`physical-height`、`cut-target` | 各 1×112 |

全部数学数组仍按有限 binary64 原词、完整形状、逐 chunk 与整体 SHA 核；σ 必须正。minA/minD 仅为原 numberRecord 元数据，允许按实际 IEEE 字和分类保存无穷/NaN，不另加有限门。原 norm 的既有有限合同保持。原 `rawNode=[0,72,144,216,288,360,432,504,576]` 为九个物理边界映射，不误认为 577 项。

cut/far 残差按当前真实值保存；不要求零，不投影或清零任何方向分量。全 576 个当前 J/r/out、577 个当前状态和尺度均进入本次身份，不借第 28/61/73 轮旧 J 改标签。

## 4. 新 flow 与原 evaluate 的明确范围

本次固定 flow 源：`geometry_20261114_noj_matched_variational_engine.mjs`，SHA `f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9`。原依赖固定为：

- `product_jacobian`：`205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25`；
- `local_cusp_grid`：`b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f`。

`primal_flow_implementation` 保原 noJ 226 维 primal 路径、224 维 shape 切向反馈、已捕获 root 的 feed-only 局部导数，以及只替换 `flowStateWithJacobian` 的范围。原 root/rhs/rk4 引用不变。adapter 逐字核 flow 源及依赖标识，读取该 snapshot 本地复制的完整安装 JSON，核其 schema `noj-primal-live-current576-live-flow-installation-v1`、launcher/hook 源、576 stages、implementation 全字典和安装未调用科学函数的范围。

这不等于旧 with-J flow 源未改。context 与输出显式保留：

```
original_evaluate_and_flow_source_not_instrumented = false
original_evaluate_source_not_instrumented = true
same_original_noJ_primal_contract = true
flowStateWithJacobian_is_a_new_identified_implementation = true
exact_DF_of_IEEE_map_not_claimed = true
```

原 core 唯一 correction 调用替换的源往返，与新 flow 安装是分别记录的两件事。原十 noJ 试步和原 evaluate 正文仍在父进程；最终灵敏度入口没有换成已保存矩阵，但其所调用的 with-J flow 是本次新实现。

新矩阵身份同时包含全部有限 J、原 r/base/边界/σ/H、本次 request、原数值源/配置/参数、cells/graphs/gains，以及完整 `primal_flow_implementation`。新 scope 为 `noj-primal-live-fresh-current-native576-finite-binary64-complete-J-r-sigma-chain`。不同 source/request 的哈希不能冒同一个原矩阵。

## 5. R273 数学、精确读回和验收

仍使用 [R273](../results/R273-complete-native-damped-square-root-chain.md) 的完整阻尼平方根块链，且实际导入的因子源与整数核不变：

| 源 | SHA256 |
|---|---|
| `exact_20261114_native_damped_chain_qr.py` | `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33` |
| `exact_20261114_native_allrows_dyadic_residual.py` | `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f` |
| `geometry_20261114_native_captured_band_correction.py` | `b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390` |

每个 577 节点的 η 惩罚恰一次，完整 cut/576 stage/far 行、Householder 两次局部 QR、全部纯常数余量和全方向回代保持。`MODEL_SCOPE` 仍为 `R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates`。η 是显式算法参数，不改变原方程或最终容差。

每次子求解保存当前未缩放有限 J/r/δ 的全部 129248 行精确整数账，再精确除原 σ。报告包括 base 与 direction 的完整最大值、578 块最大值、最坏见证原词。该精确账不包含 η 惩罚行，也不自动证明原数学 flow 的精确导数。形成时的 binary64 加权模型、原有限数组精确读回以及原非线性 noJ 验收仍是不同对象。

不以模型 L2 下降、梯度、精确线性缺陷或来源于它们的阈值阻止原试步。子程序只返回完整 577×224 δ；父仍执行原十试步、完整 guard、原 ∞ norm 比较、原收敛条件、final J 与 fresh audit。当前子程序 `native_accepted=false` 永远不代替父的真实结果。

本次没有复制单请求第 73 轮的首点 ULP 诊断到每个 live 请求；这不改变 R273 或其既有完整残差读回。将来对别的请求加该诊断须明确它属于哪个实际状态，不能把单次固定行解释成所有请求的瓶颈。

## 6. 子求解 CLI 与输出

由实际 live hook 同步启动，命令为：

```bash
python computations/exact_20261114_noj_primal_live_current576_damped_chain_qr.py \
  --snapshot-directory ACTUAL_CALL_ITERATION_SNAPSHOT \
  --snapshot-result-sha256 ACTUAL_COMPLETE_RESULT_SHA256 \
  --eta 1 \
  --exact-workers 2 \
  --max-factor-bytes 2147483648 \
  --out NEW_INDEPENDENT_QR_DIRECTORY
```

如显式传 `--factor-budget-seconds`，仍按冻结因子源的真实预算语义运行；此处不凭空加入数值停止阈值。CLI 必须使用不存在且不覆盖 snapshot 的独立目录。

| 输出 | schema 或内容 |
|---|---|
| `result.json.gz` | `complete-native-noj-primal-live-current576-damped-square-root-direction-v1` |
| `input-binding.json.gz` | `noj-primal-live-current-native576-complete-linear-system-binding-v1` |
| `native-direction-checkpoint.json.gz` | `complete-native-noj-primal-live-current576-damped-direction-v1` |
| `output-array-manifest.json.gz` | `complete-native-noj-primal-live-current576-damped-direction-arrays-v1` |
| `current576-exact-readback.json.gz` | `noj-primal-live-current-native576-complete-exact-direction-readback-v1` |
| `summary.json` | `native-noj-primal-live-current576-damped-chain-small-summary-v1`，保原小文件降级范围 |
| `factor-report.json.gz`、`factor-index.json.gz`、`formed-stage-inventory.json.gz` | 当前完整因子、形成模型身份及诊断 |
| `large-arrays/` | 全部因子、纯常数、当前输入副本、完整 δ/z 与全部 exact 行账 |

`native_delta` 与 `native_direction_checkpoint` 顶层字段保持。每个完整结果、checkpoint、manifest、factor index、精确行块和见证都继承实际 `snapshot_result/native_call/nonlinear_iteration/snapshot_sequence/current_state_sha256/request_height_float64le_sha256`。新增 flow 直接字段为 `primal_flow_source_sha256`；system binding 中相应字段名是 `new_variational_implementation_source_sha256`，并保完整 implementation 字典。

## 7. 存储与验证范围

一个完整当前 snapshot 的十数组 raw 总量沿原 576 维合同为 234318472 B；577 个因子及全部纯常数 raw 为 464891392 B。还需保存输入副本、z/δ/checkpoint、整数账、形成报告及原父协议产物。它们不能因为校正已返回而删掉常数或把 raw 完整性改成仅哈希声明。

原 32 GiB 单调用安排不能自动作为任意多个 live protocol requests 的磁盘上界。工作流应按实际请求/迭代预算记录容量；此两子源只保原每次 factor 存储上界，不擅改 native 的最大迭代或原试步数。大 payload 仅走 artifact 的 `large-arrays` 路径，Git 只出版源码和有界小报告。

本批静态回执 `unchanged-mathematical-source-check.json` 验证：原所有数组访问/完整 J streaming 的 AST 除来源文字相同；numberRecord 核完全同源；完整 exact/checkpoint 计算除新类/schema 相同；QR 的完整 `main` 除 adapter 类与声明身份元数据相同。该范围包括全部罚项、常数、精确行读回和原输出保全。它不冒 runtime 测试、原 RHS/J 重算或后续科学结果。
