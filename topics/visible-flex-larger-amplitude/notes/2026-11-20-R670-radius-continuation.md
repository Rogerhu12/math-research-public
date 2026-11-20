# R670 同场半径专项续化：复用完整已付界，只读直径障碍胞

日期：2026-11-20。会话：Astra-resume-public-20261120 / geometry_path。

**状态：续化消费者源码已写成，只完成 AST/编译语法与接口文本核对；没有执行新的科学计算。** 本条消费 [R670](../results/R670-direct-same-angle-first-geometry-with-complete-tails.md) 已证明的完整同角包围算法，不增加数学定理，不重新运行完整旧覆盖或非平面判据。

源码：[actions_refine_closed_radius.py](../scripts/resume_20261120/actions_refine_closed_radius.py)，22,411 bytes，SHA256 `0faa98e102a5c3ef9c121911313e83f5831474b8be091a161615f000bcbf5369`。它调用字节冻结的 `actions_closed_postprocess.py`，SHA256 `eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599`，只用其原 `make_direct_reader`、`reader.cell` 和 `combine_cell`。新报告的 `source_sha256` 写本续化源，不能写成原 eaa 源。

## 1. 本轮明确输入与目标

当前供本消费者使用的主会话已登记输入来自公开 Actions run `44748103105`：

- 实际 bundle：`geometry_path/curvature-qp-spectral-hessian-r22-union-next-four.npz`。
- bundle SHA256：`c4a3f010691c8e9d1a1d9a8b26bfe4bc9b136efecf8fc3a9426ecddf28289080`。
- 原完整 R670 报告：`postprocess/continue-direct-first-geometry.json`。
- 报告 SHA256：`6e8deaaaeb9aa7304eee86d0540ba35143c6a25ad6d7793444186b3a03d6bbe7`。

该原报告已经覆盖全部922胞和帽，主会话登记的支持下界为 `0.28948189498677`，body 直径上界为 `4.119227849736666`，固定见证距离下界为 `0.9393681054734059`。这些是**原报告的既有结果**，不是本续化程序的新计算。新消费者逐一核实际 bundle/node report SHA；不能把链名称当作上述 SHA。

本轮目标明确取 body 直径 $D\le4.1=41/10$，不把 marked-body 直径与 body 直径混用。由于 $D\le2\sqrt{B}$，每个原胞的当前半径平方上界只需满足

$$
B_i\le \left(\frac{41}{20}\right)^2=\frac{1681}{400}.
$$

选择 pending 胞时，把已存的 binary 上界视为准确有理数，与该准确阈值比较。两个帽的既有半径上界也要通过同一目标；若帽界本身阻碍目标，报告据实保留此状态，不把继续细化活动胞冒成已支付直径目标。

## 2. 只对 pending 胞继续完整覆盖

默认计划为

```text
Q2048 / radial2 → Q4096 / radial4 → Q8192 / radial8
```

每层开始重新按**当前已付半径上界**选胞。目标已经满足的胞不读取；某胞如果已付同等或在 Q/r 两坐标上都更密的层，也不重复该预算。这个跳过策略不宣称浮点包围质量必然单调，只是明确不再花费已经付过的分辨率预算。

每个新调用仍是原 `reader.cell(cell, radial)` 的完整 R670 计算：相同准确径向重建、同角闭弧、全部 $M$ 模、完整 Laurent/Taylor 余项和未保留角模尾。没有为了压直径删除高模，也没有把样点范数当连续范数。

同一原胞的新旧记录按已证的 R670 规则合并：

| 量 | 同胞有效界的合并 |
|---|---|
| 半径平方上界 | 取较小值 |
| 见证距离平方下界 | 取较大值 |
| 支持下界 | 在已有效的下界中取较大值 |
| $E$ 与法向平方下界 | 分别取较大值 |

未选择的胞记录原样保留。两个帽、原准确 scalar/core 身份、原非平面结果全部复用，不重新运行其科学计算。完整报告重新汇总 body D、固定见证、marked D、held 比例和支持，但不宣称 metric 或 reach 已付。

## 3. 完整报告与来源

输出保持 R670 的 `fullclosed-direct-lowmode-first-geometry-actions-v1` schema、全部有序 `records`、`covered_cells`、`cap_bounds`、`nonplanar` 和原完整几何字段，便于同场几何合并器读取。新增来源字段为：

```text
source_sha256                   = 本续化源码 SHA
continuation_source_sha256      = 本续化源码 SHA
continuation_schema             = R670-same-member-radius-continuation-v1
original_first_geometry         = 最初 eaa 报告的 path / 实际 SHA / eaa source SHA
input_first_geometry            = 本次直接输入报告的 path / 实际 SHA / producer SHA
```

`source_inputs` 继续记录实际 bundle、node report、geometry、interval、difference、transfer 六个输入的路径和 SHA。允许再次消费同一字节版本的续化报告，但必须能追到实际原 eaa 报告，并核原报告与直接父均属于相同 bundle/node。

每个新层记录实际 Q/r、pending、真正读取胞、已经付过而跳过的胞、每胞与每层耗时。每胞新 pass 记录本源码和直接父报告 SHA。`seconds` 为本次真实 wall time，另存当前新增 cell-cover 时间和 lineage 累计已付时间，不把复用的旧工作记为新零成本证明。

每16个新胞及每层末写原子 checkpoint。由于旧报告本来已完整覆盖所有胞，checkpoint 中保留的各界仍全部有来源；`radius_continuation_state` 分别记录运行中、失败/中断、目标已付或计划结束但目标未付。程序正常返回但目标未付时，不把预算结束写成研究完成。

本消费者明确拒绝任何非零 R671 lambda 的 bundle：检查 `reference_tail_lambda`、`exact_tail_lambda` 和 `reference_tail_model_json.lambda_value`。本条的 eaa 径向 lift 证明不能用于新的解析参考尾表示。只有字面 $\lambda=0$ 与原模型相同时可复用旧公式。

## 4. 同一 Actions job 的完整命令

`REPO` 为本步固定源码 checkout，`WORK` 为保留真实 raw 的工作根。原 node report 与 candidate 同时来自该 job 已刊重建链。新增 raw 完整报告留在 work，仓库只登记紧凑结论、复现参数与实际 SHA。

```bash
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/actions_refine_closed_radius.py" \
  --repo "$REPO" \
  --bundle "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four.npz" \
  --node-report "$WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --first-geometry "$WORK/postprocess/continue-direct-first-geometry.json" \
  --diameter-target 4.1 \
  --plan 2048:2,4096:4,8192:8 \
  --checkpoint-every 16 \
  --out "$WORK/postprocess/continue-direct-radius-refined.json"
```

本程序沿用原 Actions-only 执行约束，没有本地科学试算、fixture 或额外审计门。本条没有新的半径、直径、支持、held 或 reach 数值；后续结论必须引用该次公开运行真正返回的报告。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
