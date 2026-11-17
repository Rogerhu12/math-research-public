# 接续 m3 全闭表示

本包恢复前会话已经算完但尚未登记的 M8/M16 全闭比较，不重跑求解器。结论和范围见 `../../notes/2026-11-18-m3-recovered-closed-refinement.md`。已有数据仅在运行时生成；本包只保存源码和必要执行哈希。

## 依赖与输入

共享定义直接导入相邻 `../finite_closure/m3_m8_closed_map`，圆领来自 `../finite_closure/m3_m8_collar_disk/finite_closed_tail.py`。按该 R21 包的74源清单恢复 SOURCE；SHORT 指恢复的 `root_short_bridge.py`。

- M8 pair：`../nonlinear_tail/m3_coupled_seed_deliverable` 的 `m3_smallcut_fast45_q02_fixed_m8_breaks`，prefix SHA-256 `2efcc8e2f3edd765760266e9d1b83f0ee2cba1bc0b2fdb04e8b5427d645525a5`，tail SHA-256 `12754098ba6cffc0abb5f0c327c7a376cac826ea8ab820b793ec5ad9b958c4f2`。
- M16 pair：`../nonlinear_tail/m3_radial_refinement_deliverable` 的 `m3_smallcut_fast45_q02_fixed_m16_radial2`，prefix SHA-256 `7bab356153195aed714bcdd68c893755891bda8235c88cbc4cf065354ee30a6f`，tail SHA-256 `7d29ca238ddcd623659ccdae7814432a615ef85a89faae82970c93402add0c06`。
- 物理g描述必须匹配；比较器逐项检查6个字段，幅度是同g未知量。

先用 R21 的 `prepare_finite_tail.py` 导出各自尾部，参数均为 `--steps 32 --angular 256 --degree 96 --audit-angular 256 --background-curvature 8.001`。相同物理深度8，源差分步 .00005。得到两层 `tail-manifest.json`。原M8 manifest hash `1d3e5ccca3e409f49a3677d1f29b38f233c0482ae971f13a23d62a37f646fd21`，原M16 hash `2393fb7321f873563f586771d98666d84d140cbb50bd674d71c7e6090df42bcc`；路径元数据变化可改变manifest字节hash，须连同输入和参数记录。

## 共同材料坐标的全闭比较

下列大写名字均指上一步已有的真实路径，不是新设计参数。

```bash
python compare_closed_layers.py \
  --source-topic SOURCE --short-bridge SHORT \
  --coarse-checkpoint M8_PREFIX --fine-checkpoint M16_PREFIX \
  --coarse-port M8_PORT --fine-port M16_PORT \
  --coarse-manifest M8_MANIFEST --fine-manifest M16_MANIFEST \
  --tail-reader SOURCE/scripts/db6f_tail_integrated.py \
  --cap-source ../finite_closure/m3_m8_collar_disk/finite_closed_tail.py \
  --angular 512 --batch 16 --out SCRATCH/comparison.json
```

该脚本不求解BVP；它重新构造两层共享Cartesian二jet、显式C²材料角、同一cut函数和唯一mean，再比较完整图。经向样本由两层节点及中点联合生成。尾比较用共同背景的精确抵消，不重新拟合高度。

细层prefix的独立采样报告及可再生 `prefix-shared-cartesian.npz`：

```bash
python audit_refined_prefix.py \
  --source-topic SOURCE --short-bridge SHORT \
  --checkpoint M16_PREFIX --port M16_PORT \
  --tail-manifest M16_MANIFEST \
  --tail-reader SOURCE/scripts/db6f_tail_integrated.py \
  --cap-source ../finite_closure/m3_m8_collar_disk/finite_closed_tail.py \
  --angular 512 --radial 1025 --outdir SCRATCH/new-prefix-audit
```

随后原R23 `bound_cut_lift.py` 和 `certify_finite_tail_geometry.py` 可消费新细层文件；原R21背景积分证书可复用，因为物理背景未变。M16圆领审核使用本包 `audit_collar_and_disk_refined.py`：入口只要求prefix与tail模数相同，不再写死M8；所有有理式不变，输出模数标签取实际数据。原始/当前脚本hash差异及理由在 `recovered_execution.json`。

## 已知限制

完整prefix与tail的两层六jet差不为零；两层比较不是C²极限证明。源背景点查询仍是数值求值，精确背景由真积分定义。已有M16连续证书仅覆盖尾和圆领/盘，尚未把M8的全prefix界转成M16整面界。低幅候选不是10%解。
