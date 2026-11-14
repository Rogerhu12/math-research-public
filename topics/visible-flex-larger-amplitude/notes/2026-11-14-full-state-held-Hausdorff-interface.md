# 2026-11-14：新完整闭面的 held Hausdorff 消费接口

独立入口：[`geometry_20261114_full_state_held_hausdorff.py`](../computations/geometry_20261114_full_state_held_hausdorff.py)。它复用冻结的原 [`geometry_20261114_held_hausdorff_cover.py`](../computations/geometry_20261114_held_hausdorff_cover.py) 的全部距离公式、误差扣除、整面直径分母与 `0.2` 判据，只替换旧 A 文件名派发并加强同一实际输入的绑定。没有运行旧 A，也没有产生新数值结论。

## 输入与最小 CLI

先由新 [`geometry_20261114_full_state_continuous_cover.py`](../computations/geometry_20261114_full_state_continuous_cover.py) 完成一次真实新场的覆盖消费。若其主输出为

```
$OUT/full-state-cover.json
```

原 writer 会自动产生

```
$OUT/full-state-cover-position-cover.json
$OUT/full-state-cover-position-cover-centers-000.npz
...
```

没有另外的 `--position-cover-out` 参数。主 cover 报告的 `position_cover_packet` 记录 packet 的真实文件名、SHA 与完整活动中心数。

held 消费命令为：

```bash
python -u "$COMP/geometry_20261114_full_state_held_hausdorff.py" \
  --directory "$CLOSED" \
  --coverage "$OUT/full-state-cover.json" \
  --cover "$OUT/full-state-cover-position-cover.json" \
  --checkpoint "$ACTUAL" \
  --port "$PORT" \
  --config "$CONFIG" \
  --tail-response "$RESPONSE" \
  --complete "$COMPLETE" \
  --out "$OUT/full-state-held.json"
```

`CLOSED` 是该新场的闭包目录，通常含 `surface-plan.json`、`surface-assembly.json`、`surface-phase0.ply.gz`、`surface-heights.json`、`surface-normal-samples.npz`。实际文件名从 packet 的 `closed_bundle_files` 取得，没有新的旧 A 名称假设。五份 actual 原件必须与 cover 绑定的原件逐 SHA 相同；它们可以在当前 Actions 的其他路径，只要字节相同即可。

原有可选项继续有效：`--phase`（默认 `pi/2`）、`--witness-source-index`、`--rotation-position-error`。默认源点仍是规范 mirrored mesh 中的零角核心活动顶点；实际成员身份、标签、相位范围和旋转误差由原消费者检查。该值是一个真实整像距离见证的下界，不是把核心轴向差直接当作最终幅度。

## 强绑定与保留的证据

新 adapter 先核对：

- 新完整场 producer 的源码 SHA、原 held 数学消费者的源码 SHA；
- 主 cover 与 position packet 的互指 SHA、全部活动块数、中心数及 supplied envelopes；
- packet 和 producer 中完全相同的 `complete_field_binding`；
- plan、assembly、phase0 mesh、background、normal packet 五个实际文件的 SHA；
- assembly 对 plan/background/mesh/normal 的原绑定，background 对 plan/config 的原绑定；
- actual checkpoint、原 port、实际 config、最终响应、complete radial readout 的实际文件 SHA，与 plan 及 producer 均相同；
- plan/assembly/producer 的完整 `large_core_prefix` 字典相同，包括节点定义、源哈希和原输入哈希；
- `inlet_normalization` 的选择与原/新节点哈希完全相同；若启用 R249，还核当前对应规范形及 v3/v4 reader 源 SHA；
- 同一记录 SE2、完整材料均值、完整帽盘中心/半径与 marker 高度预算；
- 所有 position chunks 的顺序、数量及大小。随后原数学消费者仍逐个核 chunk SHA 和数组，并使用全部活动块。

该过程不重构 `SavedPrefix`，不再做 SE2 拟合，不运行尾、BVP、Frenet 或空间 pair 检查。原 cover 已核过的完整数值源、节点定义和连续封套前提被明确标为来自这份已绑定 producer，未被冒称在 held 阶段重新证明。

## 数学门保持原样

对活动覆盖块 \(C_i\)，原消费者使用

\[
\operatorname{dist}(x,F(C_i))
\ge |\widetilde x-c_i|-e_i-\varepsilon_x-\varepsilon_{\rm dist}.
\]

两片固定帽使用整个圆盘的解析距离，再扣完整 marker 高度上界和相同位置/距离求值误差。对**全部**活动块及两片完整帽取最小值，给出源点到整个目标闭面的距离下界。源点在实际相位像上的成员身份提供真实 Hausdorff 下界。

分母仍是 producer 给出的整个 marked 闭族的直径上界；固定 \(H\) 的直径见证仍来自两片完整固定帽的对应边界点。没有使用材料点位移替换像距离，没有使用 core-only 直径，没有删掉近对或尚未通过 reach 门的块。

**reach 覆盖全过不是运行 held 消费者的前提。** position cover 仍包含全部活动块；即使主 cover 留有 reach 余项，也可以读取这个独立的距离见证。原 `supplied_envelopes_contain_saved_samples` 对 held/fixed-H 通过旗的限制保持原样。数值中心与连续包络假设之间的差距也保持原样，不能因为包名换成新场就自动继承旧 A 的界。

输出保留原距离、分母、比率和判据字段，另加 `full_state_input_binding`、adapter SHA、规范形身份及原 reach 状态。`euclidean_registration_distance_certified`、`exact_continuous_envelopes_certified_here`、`task_completed` 仍不被升级为真。

## 冻结数学源

| 来源 | SHA256 |
|---|---|
| 原 whole-image held 消费者 | `3ba8a0d02266d2b057862c0741dc0a6f65c1276514adab8e403852d69a55809c` |
| 新完整场 position producer | `c39012655f36f652bacdbc39087c6934f03e6fde721830785fb0636930ceabe6` |

本次验证只做静态 AST 和接口/字段检查。该接口等待实际新闭面及对应 position packet，不为旧 A 再开一次计算。
