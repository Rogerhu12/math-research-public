# 原 no-J 轨道一致的 current576 完整原生续解接口

作者：geometry；日期：2026-11-15。分类：独立可执行组件、完整来源合同；本文件不是续解成功报告。

## 1. 目的和实际对象

第 61 轮失败末状态仍是一组完整、有限的 577×224 原坐标 binary64 数。第 69 轮在这组完全相同的数上，实际重放了原 `evaluate(false)`，与第 61 轮保存的 `evaluate(true)` 返回值存在差异。新组件从这组失败末状态重新启动一个原生请求，以独立的 `flowStateWithJacobian` 实现沿原 no-J 的完整 226 维轨道形成新 Jacobian，再在每次真实 correction 中调用 R273 的 current576 QR 子进程。

原 no-J 的 root、RHS、`rk4` 和原 `evaluate`/十次试探/严格 norm 下降/guard/容差/迭代上限保持。新对象明确不是旧 with-J 字节表示。条件性的完整 primal 字节恒等与理想实数正则分支链式法则见 [R275](../results/R275-original-noJ-primal-identity-and-complete-variational-chain.md)；不由该证明推出舍入程序的精确导数、Jacobian 精度、Newton 收敛或最终几何结论。

第 71 轮的独立 stage11/stage12 探针不作为这个入口的新数值阈值。是否执行续解由已经取得的实际证据决定；入口本身完整保留原科学验收。旧失败响应不进入新 worker 的 `last` 或 `tangentPredictor`，首个 `predicted=true` 只防止原 worker 再次修改明确的初猜。

## 2. 冻结源

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `geometry_20261114_noj_primal_current576_damped_solve.py` | 20279 | `938fbec22f0733fff6ceb22e6e9b7a9e12942c12d1eae31c608d8f517702df8c` |
| `geometry_20261114_noj_primal_current576_damped_solve_hook.mjs` | 53665 | `099798e9c57f09b82f7532ea184d124446aeeb2cdbafe452390cb794b8db405d` |
| `geometry_20261114_noj_matched_variational_engine.mjs` | 8624 | `f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9` |
| `exact_20261114_noj_primal_current576_damped_system.py` | 27150 | `48297483617c56179fdd4d6b80e9aeeb1151bf89c90fd816ca41d2e3ccc0bcb3` |
| `exact_20261114_noj_primal_current576_damped_chain_qr.py` | 27750 | `70bc10dfb31717b662265485d10a15028365dbba5db85ccf9c8f592226e33955` |

后两源的逐字段及 exact 读回合同见 [新 adapter/QR 接口](2026-11-15-noJ-primal-current576-adapter-and-QR-interface.md)。它们实际调用原 `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33` QR 类、原 `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f` 整数核，来源分别保留。

launcher 还硬绑定：69 的输入 reader `fc2c61d35e6eb3b1e8d836f46b75c7dc5ec2f2f69bcd483410a289434637099b`、原 raw byte helper `b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390`、原 true TailClient `1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09`、原 identity helper `a8de071c0667b342dfc7a2731c9a47ce3d071e03496875637f80424864114776`、原 frozen worker `3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054` 和 resumable engine `1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8`。

原 78 源恢复保持原 worker 入口。新流函数另核原 product-J 源 `205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25` 和原 local cusp splitter `b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f`。这些数学依赖不由新文件替代。

## 3. 唯一父件与 CLI

只需同 69/71 已定义的实际 61 选择取件。完整原 artifact 为 run `43645948199` / artifact `14136633570`，ZIP 2335870174 字节，SHA256 `7b17d1b0c11bfe14329a1d8715c8451498d0dedb6821859deb8485e5b1c1b469`。选择取件器核完整 ZIP 身份后，只提取下面必要原件；本入口不重新下载 artifact。

```bash
python topics/visible-flex-larger-amplitude/computations/geometry_20261114_noj_primal_current576_damped_solve.py \
  --native-directory "$ACTUAL61/native-current576-damped" \
  --native-result-sha256 b8754cc3c6f9635bd2f37da56d39811c2c8ef5442aa7947df89078cb416715ef \
  --snapshot-directory "$ACTUAL61/native-current576-damped/iteration-003/snapshot" \
  --snapshot-result-sha256 5e801fe00f206b4dec50c64ac0fcfb8e1fe9225a7d37280e4da9bd4875709286 \
  --source-topic "$SOURCE_TOPIC" \
  --eta 1 --node-heap 6144 --exact-workers 2 \
  --max-factor-bytes 2147483648 \
  --out "$VISIBLE_OUT/native-noj-primal-current576-damped"
```

`SOURCE_TOPIC` 是完整原 78 源所恢复的 `topics/visible-flexible-closed-surface`；输出必须是独立空目录。所有科学执行只允许在本公开仓库的 Actions。

父 native 目录 12 件为：`result.json`、`current-correction-summary.json`、`current-input-config.json`、`native_runtime-config.json`、`native_intent.json`、`native_ready.json.gz`、`native_capacity.json`、`original-live-identity-before-selected-seed.json`、`actual-current-method-identities.json`、`core-instrumentation.json`、`native_trace.jsonl`、`native_trials.jsonl`。

父 iteration003 snapshot 需要 5 件 metadata：`result.json`、`array-manifest.json`、`context.json.gz`、`core-instrumentation.json`、`flow-return-metadata.json.gz`。另外按 manifest 完整取入 9 阵的所有 raw chunks：

| 原阵 | 形状 | 用途 |
|---|---|---|
| `base-states` | 577×224 | 唯一初猜，完整原字节恢复 |
| `physical-height` | 1×112 | 本次真实同 H 请求 |
| `cut-target` | 1×112 | 原 target 身份 |
| `original-scales` | 1×577 | 原 σ 身份 |
| `original-far-graph` | 1×112 | 原远端 Robin 身份 |
| `stage-residuals` | 576×224 | 父现场完整来源；不作新基态 |
| `stage-out` | 576×224 | 父现场完整来源；不作新输出 |
| `cut-residual` | 1×112 | 父现场来源；不清零 |
| `end-residual` | 1×112 | 父现场来源；不清零 |

父 `stage-jacobians` 仅保 manifest 描述身份，不读取其 payload；父 QR/factor 不需取入。没有 actual28/41/54/59 数值输入，也没有把它们改标签为本次基态。

父 raw 状态 SHA 为 `b34daaf8ad1841b452707c669236ba38731d1f97506af4bbfe1a22e39d814013`。原 H / target / σ / far 分别锁定 `c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f`、`e2ea4563e7afc7d993db2ebc29ef63a1d853355c9d1ceeaf10f296b84391a14d`、`ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc`、`395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54`。

## 4. 首个真实请求和新流安装

launcher 用冻结的 69 reader 逐 metadata/数组 SHA 核父结果确实是失败，4 次原 freshwithJ/4 次 QR 后停止于 iteration3。`parent_failed61` 明确保存 native result、summary、snapshot result/context/manifest 五个原 receipt、raw 状态 SHA、call1/it3/seq3 与 `native_accepted=false`。

原 TailClient 构造时仍使用原 numerical configuration，ready/capacity/source identity 逐项比对；构造没有 native solve，cache 为空。hook 只在原 request loop 首次 `let initial,predicted=false` 后插入初始化。所有 577×224 raw words 由 LE64 直接恢复，逐行 raw byte 对照，负零计数和实际 raw SHA 保留。此处不通过 JSON 状态重建，不调用 `initialCheckpoint` 几何映射，不清 cut/far 残差，不把非零 H 改零或缩放。

之后对原 worker 中每个唯一 `cell.engine`：只赋值其 `flowStateWithJacobian`。原 `root`/`rhs`/`rk4`/`rhsWithJacobian` 引用和源码 hash 保存，安装前后引用必须相同。原工厂参数逐字段来自同 worker：modes/spacing/quadrature 来自 cfg，mu 来自该实例首次 cell，orientation 和 projectionFloor 来自 `dn.tail.parameters`，cuspAwareFlow 保原布尔。共享 engine 的 stage 映射完整记录，未复制出新的不同数学引擎。

`primal-flow-installation.json` 保完整新模块、原两个依赖 SHA、所有唯一实例的原函数 hash/新 flow hash、实例到全部 576 stage 的映射和工厂参数。原 ready 的旧 backend 标签只记原构造来源；它不是新 with-J 实现的身份。新实现身份单独保存到每个 snapshot 的 `primal_flow_implementation`。

flow 工厂及 source 层范围是新组件的真实变更。整个程序不能称作“只有 correction 变化”。因此顶层 `only_nonlinear_correction_call_replaced=false`；另明确 `only_core_nonlinear_correction_call_replaced=true` 和 `independently_identified_withJ_flow_replaced=true`。仅在原 core 源码内，唯一替换仍是原 `correction(ev,states,target)` 调用。

## 5. 完整原循环与同步桥

保留原单请求 `jacobian=true,audit=true`，原 `maxIterations=32`、原 `solveTolerance=2e-9`、原 10 个 alpha、完整 D/S/A/root guard、严格原 σ norm 下降和原失败语义。原 solve 内部每轮实际 `evaluate(...,true,...)` 经新 flow 返回；若进入 correction，hook 立即保存该轮当前全部阵，再以 `spawnSync`、`shell=false` 调用新 Python QR CLI。stdout/stderr 是本轮独立文件，不进入 worker 协议。

每个 child 的 CLI 为：

```bash
python exact_20261114_noj_primal_current576_damped_chain_qr.py \
  --snapshot-directory ITERATION/snapshot \
  --snapshot-result-sha256 ACTUAL_THIS_RESULT_SHA \
  --eta 1 --out ITERATION/qr \
  --max-factor-bytes 2147483648 --exact-workers 2
```

子进程完整保存原 current576 模型、577 节点罚项/常数能量、完整 δ/checkpoint、原未缩放有限阵的全行 exact σ 读回和诊断。hook 逐来源/矩阵/current state/call/iteration/sequence、manifest、577×224 raw δ、JSON 负零 sidecar 核回。全部原坐标 δ 直接返回原试探，不把 soft cut/far 方向投影掉。

R273 L2、gradient、exact 线性缺陷以及额外单行 ULP 报告均不是新 nonlinear 验收门。子进程没有产生另一 RHS/J/ODE；它消费的是父 JS 当轮已经完成的真实数组。

## 6. 新 snapshot 与方向 schema

每次真正进入 correction 的 iteration 单独目录保存：

- snapshot result：`noj-primal-current-native576-withJ-snapshot-result-v1`。
- context：`noj-primal-current-native576-current-point-context-v1`。
- array manifest：`noj-primal-current-native576-snapshot-arrays-v1`。
- current model binding：`noj-primal-current-native576-complete-linear-system-binding-v1`。
- QR result：`complete-native-noj-primal-current576-damped-square-root-direction-v1`。
- δ checkpoint：`complete-native-noj-primal-current576-damped-direction-v1`。
- QR array manifest：`complete-native-noj-primal-current576-damped-direction-arrays-v1`。

snapshot 保存上述 9 原阵加当轮完整 `[576,224,224] stage-jacobians`，原 9 项 physical `rawNode=[0,72,144,216,288,360,432,504,576]`、576 stage profiles/ports/mu、graphs/gains/far、当前 norm/minA/minD 和全部原返回 meanHeight/guard scalar。minA/minD 的真实 NaN/±Infinity 数值记录不额外成为 finite 门；当前完成 norm 与输入求解数组仍须符合既有有限契约。

`primal-flow-installation.json` 以原 bytes 复制到每轮 snapshot 根，receipt 仅是相对 `{file,bytes,sha256}`。因此 child 不借父目录逃逸，也不重新安装流。context 明确 `original_evaluate_and_flow_source_not_instrumented=false`、`original_evaluate_source_not_instrumented=true`、`same_original_noJ_primal_contract=true`。

首轮 base raw 必须为真实失败61的 b34…，后轮只绑定其本轮实际状态。每个方向返回前后都核当前 states/target/σ raw 和原数学对象及新 flow 引用未变。不存在把父 norm 或父 J 作为新缓存的分支。

## 7. 完成范围、失败保全与资源

这次入口执行完整原循环，没有一轮后计划 STOP。仅真正原 TailClient 完整响应返回、worker 正常退出且无实际错误时，顶层 `native_accepted=true`。这仍不是完整 prefix 联解接受、同 g 精化完成或闭曲面几何通过，`task_completed` 保持 false。

最终 endpoint sensitivity/heightJetJacobian/audit 仍是原函数与原方程，不用 eta 正则化。它们可使用新 primal-matched flow 形成的 tangent；这是新实现身份的真实范围。源码中 audit 不再调用第二次 native solve，heightJetJacobian/actualSlopeJacobian 也不调用 core nonlinear correction；所以当前单协议请求 `native_call=1` 合同准确。如果最终这些原阶段失败，原 worker catch/trace/last progress 和 launcher 原响应留存，不把之前下降或小 residual 误报完整成功。

每次进入 correction 的 freshwithJ 完整快照和 QR 输出均保留在 `iteration-NNN/snapshot/large-arrays`、`iteration-NNN/qr/large-arrays`，artifact-only。这里不声称每次内部 withJ 调用都导出一份；例如已达容差的最终 evaluate 不进入 correction。每个 noJ 试探沿原 retainTrial/trace/progress 保存，未新增全 noJ residual 阵观察器，不能把未导出的逐试探数组冒作已核。

保留原 32 轮上限。单请求各轮完整 J/factor/ledger 会占大量空间，工作流须保原 32GiB 级资源规划及实际 df/RSS/elapsed。资源失败保留 partial，不截断模式、stage 或原迭代数来冒科学成功。这是本单请求的预算，不能外推为 19 个 live fullDN 请求的总预算。

## 8. 本地静态检查与相对 61 的差异

本地只做 Python AST、Node syntax、源码字符串往返、普通 JSON/字节/SHA；没有导入数学模块、构造 native engine、调用 root/RHS/J/ODE/QR 或跑试探。

`pure-source-roundtrip.json` 对原 core ac2fc999…、原 worker 36cf8235…实文本核：原 evaluate 和十次试探正文逐字保持；core 恰一个 correction 调用替换；engine loader 与 worker seed 插入可逆；生成的 worker 仅做 Node syntax。未修改 `Function.toString` 来伪造方法来源。

完整相对 frozen61 diff 随组件保存：

- `launcher-relative-to-frozen61.diff`：26373B，SHA `905445902e2b4e3f676a2e9a3e85cf35e8ca457d1a2facf192d7831402da462a`。
- `hook-relative-to-frozen61.diff`：42719B，SHA `6869d141ef1d525a29b7a6f50e3010739957e64a224025298761c7228d7a68ab`。

变更只有：实际失败61原件/原始种子替代59首接受种子；新 flow 安装及诚实来源；新 current adapter/QR schemas/pins；每轮新实现 receipt；其余原循环、原矩阵 shape/σ/cut/far/H、同步桥保全和最终函数结构保持。所有新科学事实由后续本仓 Actions 产生，不在这份源码接口中预写。
