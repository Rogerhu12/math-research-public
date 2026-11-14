# 同 RK12 候选初猜接原生尾方程：一次无 J 探针

## 实际动机与本次范围

原公开 Actions request17 的非零完整 $H$ 首次原生请求在第零次迭代失败。公开 request19（[run 43602823170](https://github.com/Rogerhu12/math-research-public/actions/runs/43602823170)）对同一失败状态完成了原 `evaluate(false)`：全部 576 个 stage 的原域检查通过，原归一化残差为 `13414069.968482966`；最大项在 stage 11、rawCell 0、rawSegment 7 的 Pi mode 104。所有 cut/far 的 112 行残差均为零；保留的 577×224 项状态与原 `initial` 逐实数相等。这个结果支持检验一个不同初猜，尚未证明所有失配都来自初始化。

本入口只将已冻结的[同 RK12 零态块初猜器](2026-11-14-same-native-RK-zero-stage-initializer.md)接到同一 live native worker。它既不求零解，也不运行 Newton、全 J、尾审计或 BVP。即使本次无 J 残差小于原 `2e-9`，也只记录一个未经原完整求解/审计接受的候选。是否随后调用原 `solve` 由真实输出决定，本入口没有自动 Newton 阈值。

## 独立文件及固定身份

| 文件 | SHA256 |
| --- | --- |
| `geometry_20261114_zero_rk_native_probe.py` | `c5b14f0a760ec36c47206e1024e7c53b0217488b13dcbf0a7a7040ef2db0521d` |
| `geometry_20261114_zero_rk_native_probe_hook.mjs` | `7273f97922059d7673f4354a972ffe20ca97fdccff9fb916d62d48d4f6b21ff2` |
| 原初猜器 `geometry_20261114_zero_rk_stage_initializer.mjs` | `aad7ca6ebddf91dee6b38a454543bc16a5308f5474428fb1add09763c0c56288` |
| 原 `f6tail_cusp_grid.mjs` | `b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f` |
| 原 `tail_frozen_worker.mjs` | `3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054` |
| 原 `exact_20261114_true_tail_client.py` | `1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09` |
| 实际 request19 `summary.json` | `5c9203ce46b44de31d187c3dce43f94f30524cb25c9beaf31b9d893f05d640b1` |

新 Python 还固定核对 request17 的失败 response、iteration0 recovery、ready、intent、capacity、runtime-config 和 request19 原冻结探针源。它剥离的配置项只有既有 I/O 路径；全部数学配置及容差逐项保持。原 seeded-zero helper 仅提供身份比较函数；实例化的是原 `TailClient`，不调用其 `solve`，不复用零响应冒充新 $H$。

## 运行接线

先沿现有 workflow 恢复公开源和固定校准文件，产生已有的 `VISIBLE_SOURCE_TOPIC`。本入口只允许在本公开仓库的 GitHub Actions 运行。原 H 来自以下真实失败包，不从显示值重建，也不对任何系数阈值化。

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_zero_rk_native_probe.py" \
  --failed-directory "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43598917532-1-coupling112trust/full-DN112" \
  --cold-probe-summary "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43602823170-1-coldtailprobe/cold-tail-residual/summary.json" \
  --source-topic "$VISIBLE_SOURCE_TOPIC" \
  --out "$VISIBLE_OUT/same-RK-candidate-native-probe" \
  --node-heap 1536
```

`--out` 必须为空。两个归档位置可换为同一原字节文件的解压位置；内容 SHA 不允许变化。节点数、全部 112 模、2048 求积、RK12、shootingParts8、原深侧 Robin 图、原 `linearSteps=2048`、原容差和所有 branch guards 均保留。

执行顺序如下：

1. Python 校验真实输入及全部冻结依赖，以原 client 构造 worker。其容量 hook、原 constructor、ready、源表和 calibration/physical manifest 原样执行；握手后再次核源、配置、ready 和 capacity。
2. 新 hook 只替换已锁 `tail_frozen_worker.mjs` 所构造内存 worker 的唯一请求循环，记录原/新编译文本、被替换循环、新 hook/initializer 的 SHA。原数值函数未改。无关只读 Git 子进程照常通过，不接 hook。
3. 请求携带 spec SHA 和握手验证文件 SHA。hook 核 live manifest 对当前 ready 的一致性，再从被锁原源实际导入 `integrationGrid`，没有手写替代版本。
4. 运行冻结 initializer，先将完整 factory identity 及所有 576×112 个 2×2 stage blocks 写出，再运行 `predict(H)`。原 graphs/gains/far 只读；候选图及传递分母保留在私有构造中。
5. 若候选完整有限，保全全部 577×224 个状态，并调用一次原 `dn.tail.evaluate(candidateStates, H/rCut^4, false, originalScales)`。原归一化为 $s_0=\max(10^{-250},\max|H/r^4|)$、$s_{n+1}=s_n/|\mathrm{originalGain}_{n,0}|$，没有使用候选分母替换尺度。

原 initializer 对非零传播下溢、非有限块或奇异 chart 的拒绝保持。若 `predict` 失败，已经完成的全部块及图的统计/哈希仍在，summary 保留精确错误及 node/stage/mode。若 factory 在返回前失败，原完整 graphs/gains/layout 和具体错误仍保留；冻结 API 没有暴露的私有部分数组明确标为未返回，不捏造完成记录，也不默改初猜器以绕过失败。

## 完整输出与解读

`verified-launch-intent.json`、`instrumentation.json`、原 constructor 的 intent/ready/runtime-config/capacity/日志记录实际消费的所有源与 hook 身份。`original-live-identity.json` 固定原数值方法文本、graphs/gains/far 的 binary64 哈希和 stage/cusp 布局，并在结束后再次核对。

候选完整构造时输出 `candidate-factory-identity.json`、全部零态 stage blocks、`candidate-initializer-identity.json`、完整 candidate-state 分块及 `candidate-checkpoint.json`。后者只是一份带分块索引的未经接受初猜，`success=false`、`converged=false`、`native_tail_response=false`；rawStates 由完整状态和原 rawNode 精确索引，不丢深侧/高模。

原无 J 检查完成时保留全部 stage 的 224 个非线性残差、原 scale、归一化绝对值、mean-height increment，以及全部 cut/far 112 行。由各项重构的最大值必须与原 `ev.norm` 相等。另存由候选 2×2 块计算的零态线性残差，它有单独身份，不冒充非线性残差。gzip 证据按行分块，每件小于 5 MB；不以删状态、删模式或只保最大值满足预算。

`summary.json` 的 `evaluation_completed=true` 只表示一次原无 J 遍历完整返回及身份核对通过。程序这时 exit0，即使残差仍很大；候选构造或原域失败时 exit2 并保全已产生证据。无 J API 不返回可靠的全 stage `minA/minD`，本入口明确不报告假造的域裕量。它不改变原求解/审计的任何门，也不增加本课题完成标准。

本次交付只做 Python AST 和 Node 语法检查。候选数值、与 request19 的改善比例以及能否进入原完整 Newton/J/audit，均待公共 Actions 实际结果。
