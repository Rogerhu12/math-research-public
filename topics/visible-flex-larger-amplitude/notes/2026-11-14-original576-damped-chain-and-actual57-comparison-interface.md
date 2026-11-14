# 原 576 段 R273 方向与实际 57 限制方向的同矩阵读回接口

- 分类：实现接口；源码已完成，仅做 AST 与静态检查，尚无本入口的科学运行结果。
- 作者：ChatGPT（exact_refinement）。
- 日期：2026-11-14。
- 范围：本公开仓库 Actions，完整 actual28 原 576 段有限矩阵；不改冻结求解器、不新增验收门。

## 1. 为什么这次使用原 576 段

[实际 57 的完整报告](2026-11-14-actual57-damped-chain-QR-and-original-exact-readback.md)记录了一个必须分开的事实：R273 在新的 1372 段有限矩阵上得到很小的完整原尺度线性缺陷，但将其方向限制回原 577 个节点后，原 576 段十次非线性试探的范数都没有下降。前一个矩阵的精确读回不等于后一个矩阵的精确读回。这里不把该差异预先宣布为唯一原因。

本入口直接借用 actual28 保存的全部原 576 个宏传播块、残差、基态、cut、far、原尺度和完整非零高度输入，按 [R273](../results/R273-complete-native-damped-square-root-chain.md) 的同一个平方根算法产生新方向。同时，把 actual57 已经保存的 577 节点限制方向原字节放到**这同一原 576 矩阵**中，独立读回全部行。两次精确读回共享 J 的解码，不共享结果，不调用新的 RHS、J、ODE、baseline 或原非线性试探。

这是有因的目标矩阵对照，不预言新方向能够被原非线性规则接受。actual57 方向的来源仍是其原 1372 目标，文件不会被重命名成新求解结果。

## 2. 独立源码及冻结身份

| 源码 | 字节数 | SHA-256 |
|---|---:|---|
| `computations/exact_20261114_original576_damped_system.py` | 10616 | `c78dfc6a5ef64a9de8bbbc857a927c6cd1078bbfb2281be62be4eb942014b207` |
| `computations/exact_20261114_original576_damped_chain_qr.py` | 27828 | `e1a35bd82433cfe6525047cb3ceb3d0c434c1ebaa62680cb0f1fdab0e76cfaec` |

必要冻结依赖如下。入口检查实际文件 SHA，并检查导入路径，不复制或修改其科学正文。

| 用途 | 源码 | SHA-256 |
|---|---|---|
| 原捕获字节绑定 | `geometry_20261114_native_captured_band_correction.py` | `b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390` |
| 动态完整平方根类 | `exact_20261114_native_damped_chain_qr.py` | `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33` |
| 原二进有理数行内核 | `exact_20261114_native_allrows_dyadic_residual.py` | `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f` |

借用的是 `NativeDampedChainQR` 类，**不调用**冻结文件中绑定 1372 目标的 `main` 或精确读回函数。因子报告自己的 `source_sha256` 真实保留 `9b951f…`；新总结果、因子索引、输入绑定另外记录当前入口和适配器身份，不冒称借用代码来自新源码。

## 3. 输入只需要 actual28 与 actual57 五件

### 3.1 原 576 目标

`--capture-directory` 指 actual28 的 `native-correction-capture/`。原 `result.json` SHA 为：

`ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7`。

完整 576 个 J 块的原始串接 SHA 为：

`394ca2cc7c28ead3ffb963502ad24df86126c32f6e4eef10079495a753320a19`。

原捕获 reader 检查全部来源、完整数组及 chunk。新适配器依原序再绑定全部 J 块，九个非 J 数组保持原始字节：`base-states`、`stage-residuals`、`stage-out`、`original-scales`、`cut-residual`、`end-residual`、`original-far-graph`、`physical-height`、`cut-target`。没有用更精细的状态或 residual 重建原矩阵。

`Original576System(capture_directory, B=None)` 的 `depth=original_depth=576`，`old_to_new=[0,...,576]`。它的 `binding.original_capture_binding` 保留原 reader 绑定；新 `matrix_identity_definition` 覆盖全部原 J/r/边界/尺度/H/基态及行列次序，并由此生成独立的 `new_matrix_identity_sha256`。新 SHA 由实际字节产生，本说明不虚填。它不继承 actual57 的 `76f30d…` 或旧 step 系统的矩阵身份。

### 3.2 actual57 的五个已完成原件

`--reference57-directory` 指选择性取入的 `native-damped-chain-qr/`。只需要以下五件，保原相对目录。

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| `result.json.gz` | 4712 | `c6feb54847e96778b076076ba17b4ccd666c2548c72f8c36414b2897d176cdc1` |
| `input-binding.json.gz` | 335715 | `32cb5a0b92ab4ce642b65c0b75ba010ff26dcab5cbf77b1b847b5b469ea5279f` |
| `output-array-manifest.json.gz` | 133187 | `8a77b6b6365562ae3d41b3ff4832576f0bd880f41f2b5ed0a8fdefa86a650401` |
| `large-arrays/complete-old-node-restricted-delta.f64le` | 1033984 | `5b6e7bb4205ce79c6d0f20b63e491def9747e95a3272e8add1712595ea1c4a85` |
| `restricted-original-node-direction.json.gz` | 1590751 | `691d2b98bbd767c7c524bc9e7d6dd287067a0e9283939401d8b80bf028d72d84` |

入口核 result、四个完整 descriptor、manifest 同名 alias、checkpoint 全行及负零，再核 actual57 的 `original1372_input_binding.original_capture_binding` 与当前 actual28 原绑定逐值相同。它记录 actual57 的原 1372 目标与原 producer，不把来源目标改为 576。

这次不重新读取 actual57 的 1373 节点完整方向或因子，不重新证明其限制过程；该过程已在实际 57 的完整字节审计中付过。这里严格消费已经保存的 577 节点原件。也不需要下载 actual41 或 actual54。

## 4. Actions CLI 与预算

在题目目录执行，输出必须为不存在的独立目录：

```bash
python computations/exact_20261114_original576_damped_chain_qr.py \
  --capture-directory "$CAP28/native-correction-capture" \
  --reference57-directory "$CAP57/native-damped-chain-qr" \
  --reference57-result-sha256 c6feb54847e96778b076076ba17b4ccd666c2548c72f8c36414b2897d176cdc1 \
  --eta 1 \
  --max-factor-bytes 2147483648 \
  --exact-workers 2 \
  --out "$VISIBLE_OUT/native-original576-damped-chain-qr"
```

运行必须满足 `GITHUB_ACTIONS=true` 及本公开仓库身份。环境沿现有 Actions 的 Python/NumPy/SciPy 版本及单线程 BLAS。`--eta` 是必填正有限模型参数；默认不设因子时间截止。可选 `--factor-budget-seconds` 只在原因子类规定的新 front 启动位置检查，已完成方向的读回与保全不会因为截止被悄悄丢掉。默认完整因子资源预算为 2 GiB，不通过删节点、丢常数或截秩来满足预算。精确读回允许 1–4 个 worker，默认 2。

本次指定 $\eta=1$ 的含义只是原 $\sigma$ 坐标中使用一个明确的无量纲阻尼尺度：$\delta_n=\sigma_n z_n$，目标为

$$
\frac12\|W(A\delta+r)\|_2^2+\frac12\eta^2\|z\|_2^2.
$$

cut 行用 $\sigma_0$，stage $n$ 行用 $\sigma_n$，far 行用 $\sigma_{576}$；每个 577 节点的 $\eta I$ 恰一次。cut/far 作为完整软残差保留，不把所得方向的这两部分投影或清零。该选择不是新容差，也没有最优参数或 $\ell_\infty$ 下降保证；R273 已明确 $\ell_2$ 模型下降不能替代原非线性无穷范数规则。

## 5. 形成模型、精确读回与输出范围

原有限系数经同一冻结平方根实现形成：$J_n\sigma_{n+1}/\sigma_n$ 及 $r_n/\sigma_n$ 用 `longdouble` 求值再转 binary64；该有限形成对象不被称为精确有理模型或正确舍入证明。两次局部 Householder QR 保存全部三角因子、下一节点耦合、仿射列和纯常数，未形成正规矩阵、未做 Riccati 求逆、没有额外 ridge 或删奇异值。

**之后的两条完整精确读回均直接使用原未缩放 binary64 J、r、cut、far、实际方向和原 $\sigma$：**先用二进有理数计算每条 $J_n\delta_{n+1}-\delta_n+r_n$，再精确除以该条原 $\sigma_n$。不先把 $J/\sigma$ 或 $r/\sigma$ 舍入成另一个矩阵。这两份原方程账均不含 $\eta$ 行。

两条方向分别保存全部 `112 + 576*224 + 112 = 129248` 行，两个独立 gzip ledger、逐块最大值、全局最大值及原 bits 最坏见证。J 只需在同一共享 pass 解码一次。由相同矩阵和完整原 row order 取得的这两个结果可以直接对照；不能拿 actual57 的原 1372 范数替代其中任意一个。

### 主要输出

| 文件或键 | 契约 |
|---|---|
| `result.json.gz` | schema `complete-native-original576-damped-square-root-direction-v1`，完整结果与新/借用源码身份 |
| `summary.json` | 小于 95 KB 的摘要；完整 result descriptor 保留，即使需要紧凑 fallback |
| `input-binding.json.gz` | schema `actual28-original576-complete-linear-system-binding-v1`，原 576 完整矩阵身份 |
| `reference57-binding.json` | 五件实际来源、新旧目标区分、577 原方向字节不变及不重审 1373 限制的范围 |
| `native_delta` | 原 Q/Pi 坐标 `[577,224]` 完整方向，`large-arrays/complete-original-coordinate-delta.f64le` |
| `native_direction_checkpoint` | `native-direction-checkpoint.json.gz`，schema `complete-native-original576-damped-direction-v1` |
| `factor-index.json.gz`、`factor-report.json.gz` | 全 577 个因子/纯常数；真实 borrowed factor source 为 `9b951f…` |
| `formed-stage-inventory.json.gz` | 同一形成模型的全部 576 组系数身份；不等于重新导出所有形成系数 |
| `formed_model_diagnostic` | 原冻结类的完整形成模型/因子能量、梯度及实际资源读数；不是精确有理证书 |
| `original_exact_readback` | 新方向在原 576 矩阵上的全部精确行账 |
| `reference57_original576_exact_readback` | actual57 原 577 限制方向在同一原 576 矩阵上的全部精确行账 |
| `output-array-manifest.json.gz` | schema `complete-native-original576-damped-direction-arrays-v1`；所有数组留 artifact |

新 checkpoint 含 `depth=original_depth=576`、恒等 `old_to_new`、完整输入绑定、eta bits、577 行全部 224 系数和负零列，**没有 `step_depth`**。`original576_full_direction=True`、`not_a_restriction_of_a1372_direction=True` 明确它是本次完整未知量。新的 result 用 `native_delta/native_direction_checkpoint`，不使用误导性的 `step_delta/restricted_old_node_delta` 别名。

正常完成时静态结构为 577 个节点罚块、1153 次局部 QR、129248 行纯常数；形成读回完成后总 formation 次数为 1152。各数值、耗时、内存、形成零化计数、因子与实际方向 SHA 均由 Actions 报告，不在此预填。两份精确 ledger 的矩阵身份必须相同，方向身份必须各自真实保留。

## 6. 失败保全与原十试探的接线

已开始的计算无论成功与否都写完整 result、摘要、现有数组 manifest、因子报告和已有部分索引。`linear_direction_computed` 与 `diagnostic_completed` 分开；部分因子不能被当成完整方向。入口不会伪造 fresh native 调用，顶层 `original_native_calls/new_RHS_calls/new_J_calls/new_ODE_steps/nonlinear_trials` 均为 0；`native_accepted=False`、`task_completed=False` 保持。

后继独立 trial 读取本次完整 `native_delta` 与 checkpoint，绑定原 actual28 同一基态、H 和来源。它必须保留全部原 cut/far 方向分量及原十个 alpha、原 `evaluate(false)`、guard、严格原范数下降规则。精确线性缺陷和形成模型 $\ell_2$ 读数只作诊断，不能增加“线性足够小才准试探”的门。

actual57 的同矩阵读回用于区分目标与方向，不能替代这次新方向的非线性读回。即使两个线性结果不同，也不单凭此断言其全部差异都来自浮点传播或某一个算法环节。

本接口的源码仅经过 AST 和静态对照；未导入或运行科学模块。实际请求、输入下载、完整计算、原十试探和结果发布由本公开仓库 Actions 执行，源的存在本身不代表得到新的 native 接受解。
