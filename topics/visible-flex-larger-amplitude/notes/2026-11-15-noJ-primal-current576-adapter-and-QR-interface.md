# 从实际61失败末状态继续：同原 noJ 主路径的新576快照与R273接口

作者：`/root/exact_refinement`，GPT-6 Astra Pro，AI辅助；2026-11-15 UTC。

**类型：实现接口与纯静态核对。以下新源码尚未执行科学计算。** 原61末状态是明确保存的初猜，不是已通过原生容差的锚、响应缓存或新接受结果。新变分流有独立源码和矩阵身份；这里不把原61的J、残差或norm换标签使用。

## 1. 具体目的和边界

实际61完整循环停在第3轮原十档试步全部拒绝。其最后577节点原始binary64状态已保存，首个新的fresh evaluation必须使用这份原始状态，而非原响应JSON的近似恢复。实际69在该同一状态上执行原noJ，确认它与61旧withJ的残差读数不同。后继由独立流实现沿原noJ的完整226维状态、原schedule和算术括号推进，再从每个已捕获的root/RHS字段取得局部变分。

本两文件只消费这个新流已经返回的快照，并同步返回一个完整R273方向。原native循环、32轮上限、每轮十档试步、原`solveTolerance`、cut/far/H、原guards和最终敏感度/audit仍由父launcher处理。最终敏感度经过新变分流的事实必须按新身份记录，不能标成旧withJ逐字未变。

同一已保存有限矩阵上的精确行账仍不是精确连续ODE导数或浮点程序真实导数的证明。阻尼模型的L2行为也不替代原native无穷范数接受条件。完整理论沿用[R273](../results/R273-complete-native-damped-square-root-chain.md)，不新增机器接受门。

## 2. 冻结源码及唯一改动范围

| 文件 | 字节 | SHA256 |
| --- | ---: | --- |
| `exact_20261114_noj_primal_current576_damped_system.py` | 27150 | `48297483617c56179fdd4d6b80e9aeeb1151bf89c90fd816ca41d2e3ccc0bcb3` |
| `exact_20261114_noj_primal_current576_damped_chain_qr.py` | 27750 | `70bc10dfb31717b662265485d10a15028365dbba5db85ccf9c8f592226e33955` |

它们分别从已公开的单call61 adapter `695c2a564ada2bfc3cac251dfb5bd46bf99f6d16b696c64b75d9f90703a6ed90` 和QR入口 `ac04842bb9c42b9f29c8209d0d5f523c83744aa548e5615267521d8bf2c3141f` 独立派生，未修改旧文件。完整相对diff随接口提供。

保留的数学组件：

- `exact_20261114_native_damped_chain_qr.py`，`9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33`。
- `exact_20261114_native_allrows_dyadic_residual.py`，`0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f`。
- 完整数组/输出helper `geometry_20261114_native_captured_band_correction.py`，`b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390`。

新flow固定为 `geometry_20261114_noj_matched_variational_engine.mjs`，8624字节，SHA `f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9`。它由父hook安装；adapter不运行该模块，只核该文件、安装收据及每轮实际矩阵。

新增入口依赖父文件名为 `geometry_20261114_noj_primal_current576_damped_solve.py` 和同名`_hook.mjs`。为避免两个方向的SHA循环，父launcher锁本两文件；本adapter把snapshot声明的launcher/hook SHA与同一checkout的固定basename实际文件逐字比较。workflow再独立固定全部来源。

## 3. 失败父场：完整raw初猜，不要求成功

父run固定为 `43645948199`。`parent_failed61.schema`是`actual61-failed-native-final-snapshot-anchor-v1`；其`native_accepted`明确为`false`，源call/iteration/sequence为`1/3/3`。五份收据如下；同名`result.json`各自相对其真实native目录或snapshot目录。

| 键 | 原文件名 | 字节 | SHA256 |
| --- | --- | ---: | --- |
| `native_result` | `result.json` | 6891 | `b8754cc3c6f9635bd2f37da56d39811c2c8ef5442aa7947df89078cb416715ef` |
| `summary` | `current-correction-summary.json` | 12691 | `f75e96707b7af6f191777145108c646c9aa863082b882dbdfc5b15e316bceeed` |
| `snapshot_result` | `result.json` | 1301 | `5e801fe00f206b4dec50c64ac0fcfb8e1fe9225a7d37280e4da9bd4875709286` |
| `snapshot_context` | `context.json.gz` | 8339 | `c42bd7ddc98489b2b22ddd7f641b05913d3a816f8ba43b640d1ae415ec1da4e7` |
| `snapshot_manifest` | `array-manifest.json` | 171205 | `a7525246aabfeab518e3f7f9cda6529da4f60b032c1834acc7b3686679ee24bc` |

首轮`base-states`的完整raw SHA必须是`b34daaf8ad1841b452707c669236ba38731d1f97506af4bbfe1a22e39d814013`。后续轮使用其各自真实状态；不再强制等于初猜。完整物理H固定为原`c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f`。

父launcher负责一次完整原件绑定及raw状态恢复。本adapter逐轮保留并核这五份收据的身份，不重复装载旧大J/因子，不要求原61成功，也不把61旧矩阵/旧norm当成本轮cache。cut/far残差不强制为零，方向的对应分量也不投影或归零。

原run身份由已冻结69取件器的完整run/artifact/size/SHA固定tuple及其API元数据核验提供；父launcher再消费该取件目录中的上述固定五份原件。`parent_failed61`合同没有另设`public_run`键，本adapter也不重查API；它把固定`PARENT_RUN`写入输出binding，并以全部五个原件SHA和首轮raw状态核同一来源。这里不把仅记录一个run标签冒作独立网络验证。

## 4. 新snapshot合同

目录仍为每轮独立`iteration-000/snapshot/`等，内含`result.json`、`context.json.gz`、`array-manifest.json`及`large-arrays/`。单协议call严格为1；本call的`nonlinear_iteration`和`snapshot_sequence`从0起且相等。

| 对象 | schema |
| --- | --- |
| result | `noj-primal-current-native576-withJ-snapshot-result-v1` |
| context | `noj-primal-current-native576-current-point-context-v1` |
| manifest | `noj-primal-current-native576-snapshot-arrays-v1` |
| 有限矩阵定义 | `noj-primal-current-native576-finite-matrix-definition-v1` |
| 完整输入binding | `noj-primal-current-native576-complete-linear-system-binding-v1` |

全部十个数组仍使用原`<f8`、C-order、完整chunk ledger；所有原始词均保留，包括负零。

| 数组 | 形状 |
| --- | --- |
| `base-states` | `[577,224]` |
| `stage-residuals`、`stage-out` | 各`[576,224]` |
| `stage-jacobians` | `[576,224,224]` |
| `original-scales` | `[1,577]` |
| `cut-residual`、`end-residual`、`original-far-graph`、`physical-height`、`cut-target` | 各`[1,112]` |

`rawNode`仍是九个物理边界索引`[0,72,144,216,288,360,432,504,576]`，不是577个状态索引。每个stage保留原`rawCell/rawSegment/portRatio/mu/profiles`。current source/config/parameters、graph/gain/far SHA、完整raw数组摘要以及core插入收据都进入binding。

新`primal_flow_implementation`明确：

- schema为`original-noJ-matched-primal-captured-variational-v1`，绑定上节新flow源码与实际安装收据。
- `only_flowStateWithJacobian_replaced=true`限定在engine实现；原core内部仍有已经声明的唯一correction调用替换。两种修改分开记录。
- `original_root_rhs_rk4_unchanged=true`、`complete_state_dimension=226`、`shape_dimension=224`、`captured_root_feed_only=true`。
- 局部Jacobian原源`205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25`及局部分割grid源`b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f`固定。

context必须诚实记录`original_evaluate_and_flow_source_not_instrumented=false`，同时`original_evaluate_source_not_instrumented=true`、`same_original_noJ_primal_contract=true`。不能继承旧“整个evaluate/flow未改”的标签。

每轮原evaluate的norm、minA、minD仍按原numberRecord绑定实际bits/class。minA/minD的Infinity/NaN元数据不增加finite门；norm与真正输入数组维持旧finite输入合同。所有当前cut误差均原样保留。

## 5. R273调用、输出和原完整行账

父hook在本轮fresh evaluation已经返回后同步运行：

```bash
python computations/exact_20261114_noj_primal_current576_damped_chain_qr.py \
  --snapshot-directory "$ITERATION/snapshot" \
  --snapshot-result-sha256 "$ACTUAL_SNAPSHOT_SHA256" \
  --eta 1 \
  --exact-workers 2 \
  --out "$ITERATION/qr"
```

可选的`--factor-budget-seconds`默认不设置；`--max-factor-bytes`保持原默认2 GiB单次完整因子预算。没有改任何原native迭代/试步/求解预算。父进程把子进程stdout/stderr写入独立本轮文件，不混进worker协议stdout。

API是`NoJPrimalCurrent576System(snapshot_directory, expected_result_sha256, B=None)`及`NoJPrimalCurrent576ExactContext(system,kernel)`。数组流、raw访问、全576个stage、原边界及sigmas的合同与冻61相同。

数值模型仍保全部cut112、stage576×224、far112行，以及577个完整节点罚块。所有带宽224的Householder QR、carry压缩、纯常数、回代和原坐标恢复仍由冻结R273类执行。形成模型的binary64加权/列缩放舍入，与随后对未缩放保存矩阵的整数读回分开报告。

后者逐行精确形成：

$$
e_0^Q=\delta_0^Q+r_{\mathrm{cut}},\qquad
e_n=J_n\delta_{n+1}-\delta_n+r_n,\qquad
e_D^\Pi=\delta_D^\Pi-G_D\delta_D^Q+r_{\mathrm{far}},
$$

再分别除以实际保存的$\sigma_0,\sigma_n,\sigma_D$。不先把$J/\sigma$或$r/\sigma$舍入成另一套数组。不把eta罚行加入原native残差，不据这些精确数设试步门。

主要文件名与577完整方向保持：`result.json.gz`、`summary.json`、`input-binding.json.gz`、`factor-index.json.gz`、`factor-report.json.gz`、`formed-stage-inventory.json.gz`、`output-array-manifest.json.gz`、`native-direction-checkpoint.json.gz`、`current576-exact-readback.json.gz`、`current576-worst-witness.json`和`large-arrays/current576-all-exact-rows.jsonl.gz`。

| 对象 | 新schema |
| --- | --- |
| QR result | `complete-native-noj-primal-current576-damped-square-root-direction-v1` |
| full checkpoint | `complete-native-noj-primal-current576-damped-direction-v1` |
| arrays manifest | `complete-native-noj-primal-current576-damped-direction-arrays-v1` |
| exact detail | `noj-primal-current-native576-complete-exact-direction-readback-v1` |
| small summary | `native-noj-primal-current576-damped-chain-small-summary-v1` |

顶层`native_delta`仍指完整`[577,224]`原坐标数组；`native_direction_checkpoint`仍逐node写224值及负零列。manifest和checkpoint绑定新矩阵、snapshot、call/it/sequence、current state及`primal_flow_source_sha256`。输入binding另外保完整`parent_failed61`与`primal_flow_implementation`。

全部129248行和578个typed block均保存；不丢恒定项、不只保存最坏一行、不转成1372限制方向。该子进程始终`native_accepted=false`；只有父原native流程能给最终接受结果。

## 6. 首轮浮点可表达性读数：只解释原件

若首轮需要QR，入口在同一次Actions里生成`current576-row-resolution.json`，查询actual61旧withJ与actual69原noJ各自的共同norm最坏行stage11/Pi75，即stage内零基row186、完整方程零基row2762。它不是两路径差异最大的Pi104行。它只从本轮已绑的`stage-out`、`base-states`、`stage-residuals`、`original-scales`读四个原词，原tol取本轮`numerical_configuration.solveTolerance`。

报告完整operand bits及来源SHA，两个方向的相邻可表示浮点词；以精确有理数保存邻距、邻距/原sigma、邻距/(原tol×sigma)，以及两个已存操作数的精确差、存储残差与该差的舍入差。普通float近似仅供阅读，明确不是区间包络。

这不会重算RHS/J/ODE，也不会形成第二个方向。该行可能不再是新点的最大值，报告不假称新argmax。尤其不能从两个当前operand的ULP就断言存在正的残差下界：两个operand都可变化，相等值可以恰好相减为零。报告不给真实flow前向误差或连续DF误差界。

诊断自身异常被记录并继续原QR；它没有数值阈值、没有新的通过门，也不改变原tol。后续轮不重复此固定行诊断。

## 7. 完整保全和资源

当前构造不减少raw保存。原61Actions字节读者已经记录每轮10快照数组、576完整J块、583chunks、234318472字节；本次维度和保存形式相同。冻结R273每轮577因子与全部纯常数仍为464891392字节；129248行完整exact ledger另存gzip。新flow身份与单行诊断只增加小元数据。

此前单轮固定项估计704385296字节、单call最多32轮的32 GiB资源安排可继续作为同维度计划；它不是压缩率保证或可变ledger的严格上界。执行端须保全部实际文件并记录真实用量。不能为省空间删原常数/罚块/完整J，不能把一call预算冒多请求总预算。大数组均置于`large-arrays`，由既有publisher仅保artifact；小报告单独发布。

## 8. 已做和未做

已做：两新源码AST解析；相对冻结61的完整diff；原数组访问方法逐AST相同；exact全行读回只按声明改context类名/schema后逐AST相同；完整checkpoint仅schema改名后逐AST相同；原R273/kernel来源和模型参数化常量保持。收据为`unchanged-mathematical-source-check.json`。

未做：本地导入任何目标数值模块、构造快照对象、RHS/J/ODE、QR、Fraction诊断、范数/方向计算或新native运行。实际候选primal/J和完整续解结果只由后继公开Actions生成；源码准备不等于数值成功。
