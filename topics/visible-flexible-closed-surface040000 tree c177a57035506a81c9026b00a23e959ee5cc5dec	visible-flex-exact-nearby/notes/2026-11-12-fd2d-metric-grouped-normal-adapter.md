# R165 新有限目标的 stream／partition 薄接入

**状态：** 可执行接口已闭；仅完成源码数学部分的 AST 对照和三个小诊断元数据 case。没有构造 problem、没有求值新的 F/J、没有装配 normal、没有运行 BVP 或 body。旧25仍使用自己的旧目标与实体，不能用这里的准备工作冒充新目标已求解。

## 1. 具体接口缺口

旧 `fd2d_gc_positive_trace_stream_normal_consumer.py` 在每个 cell packet 后强取
`known_lifting_full_change_maximum` 和 `selected_coast_local_cells`。R165 完整 actual 场同点细积分中，已知 lifting 与 raw 和非线性修正共同求积；它没有再次单独计算 known-lifting 差。这项未求值量不能造一个0，也不能借用完整 Codazzi 的值冒名。

新源明确另名：

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `scripts/fd2d_gc_grouped_coast_stream_normal.py` | 12952 | `ad127ceab9a5b592d2784806abbb730f4d1996a5d3110e1b3620dfc6160f219d` |
| `scripts/fd2d_gc_grouped_coast_partitioned_normal.py` | 19628 | `23c79f05e6a54a32164fe445d3639335e3a014535aef38007667e5a90df16367` |

冻结原 stream `db7377ae…`、原 partition `5802e1c2…` 和 R165 consumer `a0a8b934…` 均未改。

## 2. API 与选定目标

新 stream 保留原同名函数与签名：

```python
from fd2d_gc_grouped_coast_stream_normal import stream_positive_trace_normal

normal, info = stream_positive_trace_normal(
    problem, vector, curvature_cap=7.2, curvature_weight=1.,
    high_gauss_weight=1., high_codazzi_weight=1.,
    order=2, block_cells=2,
    node_indices=None, cell_indices=None, include_boundary=True,
    observer=None, progress=None,
)
```

默认 `cell_consumer` 为已闭 `gauss_cell_positive_trace_grouped_coast`，其已声明默认 fine order 为8、point batch为2。`order=2` 保留原接口及 G2 诊断网格；它不表示 R165 coast 只用了两个实际积分点。外 coast 的原规则与 terminal 修正由 R165 顶层 consumer 原样保留。

新 partition 导入上面的新 stream，公开同样的 `make_normal_partition`、`assemble_normal_tile`、`merge_normal_tiles`；所有参数、descriptor键、保存／回读原类型、逐片覆盖与消元规则同已闭原 helper。其 source SHA 和默认 consumer 身份不同，因此必须生成新的 actual plan/common binding，不把旧25的片移作新目标。

这是一项 **新有限目标的接入**：R165 coast 的实际残差与原25不同。本文的“assembly 不改数学”仅指给定所选 consumer 后，节点／边界／局部 J 拉回、`normal.add`、缩放前分片与求和本身不改变该所选目标；绝不声称两个 consumer 的残差相等。新 CLI 还须有相应新 baseline 及真实方向／trial。

## 3. 数学路径保持的范围

源副本保留以下完整计算：节点原实际 R153/R155 字段链和 Gauss／曲率行；局部 cell `retained/high` 的两节点列抽取；中央／cut／gap 边界行；R159 的全部 `normal.add` 调用、原参数映射、平台删除和 trace gauge；每片全部未缩放数组、列平方范数及残差平方和的合并。

仅 cell consumer 的选择和其后诊断聚合改变。设新 consumer 给出的实际加权行与 J 为 $r_b^{165},J_b^{165}$，原方向映射为 $E$。新 stream 累加的仍严格是

$$
\sum_b (J_b^{165}E)^T(J_b^{165}E),\qquad
\sum_b (J_b^{165}E)^T r_b^{165},\qquad
\sum_b\|r_b^{165}\|^2,
$$

并保留逐列平方和。新 partition 只是按旧 R159 证明把同一组有限和分组后相加。R165 已证明其完整同点求积保 actual raw-l／known-l 相消、相邻两节点局部性和各个真实参数导数；本薄层没有添加或删除这些行。

## 4. 诊断字段的明确语义

| 字段 | 含义 |
|---|---|
| `finite_maxima.full_gauss` 等原节点项 | 沿用原 stream 的节点观察范围 |
| `finite_maxima.G2_sampled_interior_Gauss` | 本 subset 真返回的原 `point_gauss` G2 点峰值；没有 cell 时为 `None` |
| `finite_maxima.fine_sampled_interior_Gauss` / `fine_sampled_interior_Gauss_maximum` | 仅 `grouped_coast_rules` 明确包含的 fine 点峰；无此点时为 `None` |
| `fine_sampled_minimum_active_n` | 已返回 fine 观察中非空的 active-n 最小值；无观察时为 `None` |
| `grouped_coast_global_cells` / `grouped_coast_cell_count` | 由局部 cell 编号加当前 chunk 的全局起点得到 |
| `grouped_coast_rules` | 保留原 fine 点／平均权／分片／位置资料，另添 `global_cell` 和 `stream_chunk_first_cell` |
| `known_lifting_full_change_maximum`、`finite_maxima.known_lifting_change`、`known_fine_coast_cells` | 明确 `None`；本层没有给出独立 known-only 比较 |
| `known_lifting_change_maximum_not_separately_evaluated` | `True` |

零与未求值严格区分。即便某个 outside-only packet 恰由旧 consumer 附带一个 known-only 数字，本新 stream 也不据此声称整个混合目标的该项已单独求值。调用方不能对上述 `None` 字段做未检查的数值 `max`，也不能把 fine 观察拼进原 G2 数据形状。

fine 节点、权与原 packet 不修改。新增记录是字典浅复制后添加全局标签；局部标签仍标明其原 chunk 范围。所有这些仍是有限点观察，不是全角或全径向连续包围。

## 5. 仅静态与 metadata 的真实小核

检查器不导入或构造物理 provider。它解析新旧源并实际比较：

- `radial_view` 和 locality assertion 的 AST；
- 全节点行循环、cell 数学构造及释放部分、完整边界块；
- 所有 `normal.add` 调用；
- 所有 partition 函数，唯一准许的函数内 AST 差异为默认 consumer 名。

之后从新源提取 **仅诊断聚合语句**，对人为构造的 outside-only、单coast、混合chunk三个小 metadata packet 执行。这里不存在物理字段求值，观察值只是测试诊断语义的小数。

首轮 `27013 / b50697 → 2e31c6` 真 exit1：检查器把 for target 的 AST `Store` 上下文与普通表达式的 `Load` 上下文直接比较，未找到统计块位置。已保留原检查器、console和退出收据；没有产生报告，不补写成功。

仅另名 `fd2d-metric-grouped-normal-adapter-check-v2.py`，按明确循环变量名匹配修复该检查器。两适配源保持。第二轮 `62603 / 6359f4 → 077ddf` 真 exit0：wrapper 2.718527062 s、内部1.006594654 s，所有列出的 AST 对照和诊断 case 为真。三 case 实际说明：

- outside-only 后 fine 和 known-only 均为 `None`；
- 最终 G2峰为0.7、fine峰为0.8，独立记录；
- 全局 coast cell 为 `[20,31]`，fine active-n最小观察为0.2；
- 原 packet 的 `info` 未改变，known-only 始终 `None`。

以上数值均为合成 metadata，**不是当前曲面的测量**。真实报告为 `notes/2026-11-12-fd2d-metric-grouped-normal-adapter-02-report.json`。

可重做这个无物理计算的小核：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python scripts/fd2d-metric-grouped-normal-adapter-check-v2.py \
  --out-prefix notes/2026-11-12-fd2d-metric-grouped-normal-adapter-repeat
```

## 6. 主线衔接

numerical 代理独占后续 newContext value objective、131节点实际初值和 staged CLI；这两个薄接口不主动运行它们。当前25的48片仍按原25目标闭存、合并、求真实阻尼方向及 Armijo；只有其后明确切换时，才使用新 R165 目标自己的完整 source/baseline/plan/partial normal 身份。既有数学闭组和已接受场一律保留，不以本接口准备工作替代下一实际求解。
