# R675 两种真实非平面证明接入同场几何合并器

日期：2026-11-20。会话：Astra-larger-resume-24b2ab87-20261120 / fullclosed_solver。

**状态：独立后继源码准备，只有 AST 与文本核对，未消费实际报告、未执行科学计算、未安排新任务。** 如果已有 b36 v1 报告已经付完全部活动胞，则继续使用原链即可；本接口不要求为同一已付结论再跑一次消费者。

新源：`scripts/resume_20261120/exact_reference_tail_geometry_combine_v2.py`，30568 bytes，SHA256 `521187ae2df4225ddbda6efd8326db760d2f1bd5bd184a74f3a816408ad19e6c`。冻结原合并器 `exact_reference_tail_geometry_combine.py` 的 SHA256 仍为 `9da689fa2d16ba878e7eac3caf7c33a8d17a2a9940f6d2d6466f8ed536a4ab8f`，其文件未改。

## 1. 新接口只扩展非平面证明的消费分支

新消费者接受以下两种准确 schema/source 配对，分别读取实际报告，不改写报告身份或证明标志：

| 分支 | 实际生产者 | SHA256 | 付费条件 |
|---|---|---|---|
| v1 | `exact_reference_tail_nonplanarity.py` | `b36d387fed072235e1aec8e77da130c9c9be095aed64be46485fc0890b21c09d` | 每个原胞都有准确非零高 Z Hermite 见证 |
| v2 | `exact_reference_tail_nonplanarity_v2.py` | `df8f3f1e876d3bc7f970de1748aa3e9f46a5b9d71193d0ea94d69aa1672036ea` | 每个原胞由准确高 Z 见证或已刊非零解析尾命题支付，两个集合互斥 |

两分支均保留原合并器的同场身份要求：实际 bundle SHA、准确节点报告 SHA、canonical model 身份与 lambda，以及非平面报告所使用的 **embedding-report SHA 必须等于本次实际 first 报告 SHA**。first/curvature 仍只接受冻结 f122 新尾区间核，全部 canonical 依赖和实际 scalar 身份保持原检查。没有借用旧 lift 的证书，也没有把 v2 伪装成 b36 生成的 v1。

共同前提仍是该实际场全域嵌入已付、准确正胞宽已付、两镜像活动片均覆盖、帽的已知平面内部排除。v1 分支保持原来的 `J-1` 个高 Z 见证及原充分条件，没有改其数学含义。

## 2. v2 按真实互斥胞集合消费

对 v2，消费者读取 `selected_witnesses` 与 `analytic_tail_zero_high_Z_cells`，核对：

- 高 Z 见证数等于真实列表长度，每胞恰有一个见证，胞序、端点、三 jet 阶数、正 Fourier 模号及准确 binary hex 非零值符合生产者格式。
- 解析尾胞序无重复，数量等于 `analytic_tail_cell_count`；使用此分支时 lambda 必须为正，准确 eta 节点与 canonical model 一致，所有解析胞都在 eta 起点之后，已刊 FullHold 源身份和准确 binary `.995` 分界一致。
- 高 Z 胞和解析尾胞互不相交，其并集准确等于 `0,...,J-2`，且 `paid_cell_count = selected_witness_count + analytic_tail_cell_count = J-1`。
- `all_cells_nonplanarity_alternatives_paid` 和实际活动非平面结论为真，没有未付胞。原 `all_cells_nonzero_height_mode_condition_paid` 必须准确等于“高 Z 见证数为 `J-1`”。使用解析胞时这个旧标志应为假，消费者保留该事实，绝不将它改成真。

解析尾分支使用已刊 R675 补充命题和 df8 生产者实际记录；这里不重读 q、不执行新的 scalar oracle、不重复区间或嵌入计算。未满足覆盖或身份时只报告未付，不反推存在平面开片。

## 3. 几何合并原文保持

新源码来自冻结 9da 原文的独立副本。`literal_bundle`、canonical identity、全部 first/curvature 身份函数以及从四 marker 到 R650 reach/held/grip 的 Fraction 运算均保持原文。源码文本核对确认整个 marker/几何公式块未变；没有新的几何阈值或新的证书门。

因此仍使用同一固定帽四图构造、同一有理 marker 常数、同场直径上界、支持下界、曲率上界与距离见证。非平面条件只用于原活动片和正 Euclidean 形状变化的既有推论。metric、固定 g 精化和课题完成状态不由此自动支付，输出中的相应标志继续为假。

新报告另记 `actual_nonplanarity_proof_consumption`：真实 schema/source、采用的证明分支、真实高 Z 数、解析尾数、总支付数和分区检查；并记录冻结 9da 来源 SHA。它不覆盖输入报告，不改变输入标志。

## 4. 相同 CLI 的独立输出

```bash
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/exact_reference_tail_geometry_combine_v2.py" \
  --repo "$REPO" \
  --bundle "$ACTUAL_R671_BUNDLE" \
  --node-report "$SAME_ACCURATE_NODE_REPORT" \
  --first-geometry "$ACTUAL_F122_FIRST_REPORT" \
  --curvature "$ACTUAL_F122_CURVATURE_REPORT" \
  --nonplanarity "$ACTUAL_B36_OR_DF8_REPORT" \
  --out "$WORK/postprocess/same-field-two-proof-geometry.json"
```

实际消费仍仅在本仓库公开 Actions。输入可为 v1 或 v2 的真实报告；二者无需都运行，更不需要为了本消费者新增 fixture。所有检查只消费已返回证明及实际 bundle 的字面 scalar/model 元数据，不调用场、导数、Fourier 或连续覆盖核。当前源码准备没有任何新的科学结果。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
