# 原完整 native 行账的十 α 仿射∞诊断接口

类型：独立计算接口；新增精确科学算术只在公开 Actions 执行。

作者：`exact_refinement`（公开课题协作）；日期：2026-11-15。

## 1. 已交付对象与冻结身份

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `exact_20261115_native_affine_infinity_prediction.py` | 65,266 | `bd4ff360cb27750a98bb9966981949f89d6b6dcf607fd820c34bb71adee9cde4` |
| `R276-native-affine-infinity-descent-interval.md` | 12,288 | `0e052e088407f31d464ce176df10a6cbc5917a4e22df6b0b4e1e0c4eda3a50af` |
| `static-source-check.json` | 4,100 | `2a120dedbd0716e138eb5fd97f2451bb983867e4131df9ddf020b498c7b9f167` |

程序是标准库独立文件；没有导入 NumPy、SciPy、任何原 solver/adapter、或任何科学模块。源码只在本地做了 AST、冻结源字节和源码字符串核。没有导入或运行新程序，没有本地数值测试，也没有实际 73 数值结论。

数学结论见 [R276](../results/R276-native-affine-infinity-descent-interval.md)。本文不改已有 61/73、QR、kernel、workflow、接受门或源身份。

## 2. 诊断计算什么

固定当前完整 576 段、577 节点、224 维状态的有限矩阵。已有 exact ledger 是在原未缩放 $J,r$ 和恢复后实际 binary64 $\delta$ 上精确形成的 $e=A\delta+r$。新程序只对已保存的 signed $e_i$、原 binary64 $r_i$ 和实际正 $\sigma_i$ 做整数算术：

$$
\rho=\max_i\frac{|r_i|}{\sigma_i},\qquad
F(2^{-k})=\max_i\frac{|(2^k-1)r_i+e_i|}{2^k\sigma_i},\quad k=0,\ldots,9.
$$

完整顺序固定为 cut112、576×stage224、far112，共 129248 行；不把 η 罚行混进原规范。每个原候选同时报告 cut/stage/far 最大值、完整全局最大值、精确分数和坐标。

按 R276 输出正步长严格下降集合：ρ=0 时为空；ρ>0 但任一活跃行 $r_i(e_i-r_i)\ge0$ 时为空；否则对**全部**非零斜率行计算首个触界值的最小值 α*，集合恰为 $(0,\alpha_*)$。等号不是严格下降。全部活跃行另存完整 gzip JSONL，首个阻断/触界见证在完整报告中保留。十个原候选是否下降既逐行计算，也与区间结论核对。

已有完整 exact 报告的端点值 ε=$\|e/\sigma\|_\infty$ 若严格小于 ρ，已足以证明原十个候选都在仿射模型中下降；新报告明确标识这个充分条件。ε≥ρ 时不先否定小步，改用完整行/α* 判断。

没有新的 Jδ、RHS、root、ODE、QR、优化、方向恢复或 trial。现有 `formed_model_diagnostic` 只原样保留，不用它替代这个原坐标、原 σ 的精确模型。

## 3. 运行环境、来源 profile 与最小源闭包

启动强制 `GITHUB_ACTIONS=true` 且 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。程序不读取 token，不联网、不下载、不修改输入；使用上游已按真实 run/artifact/ZIP tuple 核验并解包的目录。科学算术不能借“只是读回”之名在本地运行。

支持两个明确 profile，不能把新 run 自动套成其中之一：

| profile | 实际原 run / source commit | 原目录 basename |
|---|---|---|
| `native73` | `43657001633` / `9515d5aaf7c68f8efd366438d6bd81ce73c3486f` | `native-noj-primal-current576-damped` |
| `native61` | `43645948199` / `cf6b51193255dfc713610d2919598451ccdd49e2` | `native-current576-damped` |

`native73` 需要本程序同目录存在以下八个冻结源，只读其文件 SHA，不导入执行：

| 文件 | SHA256 |
|---|---|
| `geometry_20261114_noj_primal_current576_damped_solve.py` | `938fbec22f0733fff6ceb22e6e9b7a9e12942c12d1eae31c608d8f517702df8c` |
| `geometry_20261114_noj_primal_current576_damped_solve_hook.mjs` | `099798e9c57f09b82f7532ea184d124446aeeb2cdbafe452390cb794b8db405d` |
| `exact_20261114_noj_primal_current576_damped_system.py` | `48297483617c56179fdd4d6b80e9aeeb1151bf89c90fd816ca41d2e3ccc0bcb3` |
| `exact_20261114_noj_primal_current576_damped_chain_qr.py` | `70bc10dfb31717b662265485d10a15028365dbba5db85ccf9c8f592226e33955` |
| `exact_20261114_native_damped_chain_qr.py` | `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33` |
| `exact_20261114_native_allrows_dyadic_residual.py` | `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f` |
| `geometry_20261114_native_captured_band_correction.py` | `b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390` |
| `geometry_20261114_noj_matched_variational_engine.mjs` | `f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9` |

61 只将前四个换成已有 `geometry_20261114_native_current576_damped_solve.py` / `_hook.mjs` 与 `exact_20261114_current576_damped_system.py` / `_chain_qr.py`，精确 SHA 已写入 profile，且不要求新 flow 文件。通用 factor/kernel/byte源仍为同三件。

新诊断无需恢复 78 个 RHS 源，无 `VISIBLE_SOURCE_TOPIC` 或 source-root 参数，无 Node/BLAS 调用；已核原 source/config/cell/gain/graph 身份由保存的完整 context、binding、source ledger 和实际 core instrumentation 保留。它不会冒称重新逐文件核了未取入的 78 源。

静态核重新由原 core 文件的两处已冻结 loader 文本替换生成 runtime 字符串，核到了 runtime `f29dc9…` 和原十试步正文 `603924…`。这里保留已有 accepted-trial progress 回调；原磁盘 core 的未经 loader 处理 trial 子串 SHA 是另一个对象，未把两者混写。

## 4. CLI 与工作流接线

完整 producer result 模式：

```sh
python computations/exact_20261115_native_affine_infinity_prediction.py \
  --native-kind native73 \
  --native-directory "$VERIFIED_EXTRACT/native-noj-primal-current576-damped" \
  --original-run-id 43657001633 \
  --original-source-commit 9515d5aaf7c68f8efd366438d6bd81ce73c3486f \
  --native-result-sha256 "$ACTUAL_NATIVE_RESULT_SHA256" \
  --out "$VISIBLE_OUT/native-affine-infinity"
```

变量 `ACTUAL_NATIVE_RESULT_SHA256` 必须来自那份实际已核 artifact 的 `result.json`；本接口不填未来 result/artifact SHA。默认处理 journal 的全部原迭代；可重复 `--iteration 0 --iteration 3`，只挑已存在的原迭代。不能创造第 33 轮、换方向、换 η 或改变原十 α。

若进程终止导致无最终 outer result，但留下完整的 per-correction journal，可以显式改用：

```sh
  --partial-records-sha256 "$ACTUAL_CORRECTIONS_JSONL_SHA256" \
  --partial-trials-sha256 "$ACTUAL_TRIALS_JSONL_SHA256"
```

它与 `--native-result-sha256` 互斥；profile/run/source 参数仍必需。有 `native_trials.jsonl` 就必须提供其实际 SHA；没有该文件才可省略 `--partial-trials-sha256`。此模式只接受完整可解析的已保存 journal 行，明确不宣称原 native 已有完整终态。没有返回完整方向的原记录只注明未计算，不虚构 e 或 trial。

程序只使用已有解包根。适合与原 73 Actions reader 共用同一次完整 artifact 下载/解包，单独一步执行。原 science 结局、byte audit、新仿射诊断是三个不同对象；新步骤失败可以记录其实际错误，不能反写原接受状态，也不能把它设成继续原科学所需的新数值门。原 large-array 发布策略已经跳过路径中的 `large-arrays`，无需为本程序修改共享 publisher。

## 5. 输入精确范围

每个已返回方向的迭代读取并绑定：

| 对象 | 实际路径/用途 |
|---|---|
| 原 native metadata | `result.json`、`current-correction-summary.json`、`current-corrections.jsonl`、`native_trials.jsonl`，或显式 partial journal |
| 当前 snapshot | `iteration-NNN/snapshot/result.json`、其 context/manifest/core 收据；73 另核本地 primal-flow installation 收据 |
| 当前方向 | `iteration-NNN/qr/result.json.gz`、input binding、output manifest、完整恢复后 `native_delta` 原字节 |
| 原方程输入 | QR 导出的九个 non-J 原数组，完整 shape/文件 SHA 与 snapshot 的整数组 raw SHA 一致；所有 σ 保原 bits |
| 原精确结果 | `current576-exact-readback.json.gz` 和完整 `large-arrays/current576-all-exact-rows.jsonl.gz` |

九个 non-J 数组是 base-states、stage-residuals、stage-out、original-scales、cut-residual、end-residual、original-far-graph、physical-height、cut-target。新数学只用其中 r 和 σ；其余完整小原件也哈希以保当前输入身份。方向完整 577×224 raw 文件再次哈希；不按 checkpoint JSON 重建一遍方向。

原 J 的完整 shape、全部 576 block SHA、完整 J raw SHA、原 source/config/cells/H/边界/σ 与 canonical matrix definition 都核其元数据和交叉绑定。**本程序没有重读 231MB 的 J payload，也没有重读 577 个 factor/constant payload。** 这些原件的完整字节审计仍属于专用 reader。保存的 signed exact ledger 每行都读；与其声称的方向和原 J block SHA 逐块交叉。

每行 E 用原 kernel 的 canonical signed odd-hex/power-of-two 结构读取，零采用 `['0x0',0]`，对应共同单位 $2^{-2148}$；没有通过 float 转换精确 E。原二进制 r/σ 也按 IEEE 字段解成整数；signed zero 原字节身份保留，作为精确实数参与比较时两种零都为零。positive σ 要求是本定理的输入条件，不是新 native 验收门。

61 的旧 canonical matrix definition 未重复 call/iteration/sequence 三键，新程序仅在其外层 binding、snapshot、ledger 核这些真实字段；不向旧 definition 添键再冒旧 hash。73 的新 definition 含这些键，按实际内容核。

## 6. 输出与信息限度

主目录：

- `original-native-outcome.json`：先保存原 native 状态/错误的读取范围，早于新算术。
- `large-arrays/original-native-readout.json.gz`：完整原 outer/journal/trial 原值与 descriptor。
- `summary.json` 与 `large-arrays/diagnostic-result.json.gz`：总体科学诊断状态、每轮输出、实际错误及完整输入引用。

每轮 `iteration-NNN/`：

- `summary.json`：ρ、α*或明确空集分支、全部十个原候选精确范数/行坐标、原 trial scalar 对照。
- `large-arrays/result.json.gz`：完整三类行最大值、精确分数、首触界/阻断见证、全部来源、原 formed-model 与 exact 报告。
- `large-arrays/active-original-rows.jsonl.gz`：全部 exact-baseline-active 行及其真实 r/e/σ bits、向内符号；不是只选一个当前最大行。
- `large-arrays/input-files.json.gz`、`status.json`：本程序实际读到的 metadata/non-J/direction/ledger 文件 SHA 范围，未读 J/factor 的事实及每轮错误。

小 summary 超 95KB 时保完整大件并输出明确 compact fallback。完整精确记录不会删除。十进制 64 位显示只是舍入显示，既不参与比较，也不称区间外包；精确 numerator/denominator 才是判定数据。失败时 `scientific_arithmetic_started` 与 `scientific_arithmetic_performed` 区分进入/完成/不确定部分执行，不把输入校验失败写成已完成科学结果。

实际 trial 按 call/iteration/trial 关联，核 α 的原 binary64 bits 和 `baseNorm` 的原 bits。只有存在的有限实际 `trialNorm` 才比较其保存值；guard/root 失败不伪造范数。报告可以给“实际标量范数减精确仿射范数”的精确数值，但显式注明它不是完整残差向量余项。

当前 61/73 的原 client 删除 `trialStatePrefix`，73 hook 只在 correction 前保存 fresh-withJ 全量 snapshot。没有完整每次 no-J trial 的 r 或原始 state；接受态只可能在随后进入 correction 时再有 raw snapshot。新诊断不重建 `base+αδ`，不算状态舍入项 A h，不额外重跑 no-J。它因此不能单独归因 state 加法舍入、J 表示误差与非线性余项各占多少。

## 7. 规模与后续使用

每轮一次完整 r/σ 扫描、一次 578-record signed exact ledger 流读，以及 129248×10 个精确 affine 分子和比较；不是 129248×224 的新 J 乘法。内存主要是约 3.1MB 的九个 non-J 原件、约 1MB 的方向以及每次一个 ledger block/少量整数最大值；不展开全 J 或 factor。完整 active 输出按行流式 gzip 写入。运行时间、输出大小只能由真实 Actions 回执给出，本地没有预造测量。

已有 ε<ρ 的精确充分结论、十 α 曲线或 α* 都只解释保存的有限模型。它们不会替代实际严格原 norm 比较、guards、最终 J/audit，也不会使已失败的 native 或其初猜自动成为“成功锚”。后续是否继续、改变方向算法或增加观察入口，由真实原结果和既有授权决定。
