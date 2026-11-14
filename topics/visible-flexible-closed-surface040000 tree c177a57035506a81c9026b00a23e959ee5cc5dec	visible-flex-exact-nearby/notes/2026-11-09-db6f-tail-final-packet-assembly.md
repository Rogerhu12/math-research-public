# M8 全域背景包的有限分段组装

2026-11-09，`/root/independent_geometry`。本稿记录同一个精确背景、同一个有限扰动图上的区间包组装。工作容差和分段深度只是认证计算设置；没有调整物理参数、有限 source calibration 或目标 g。

## 1. 区间包的语义

有限图 manifest 是 `2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json`，SHA256 `da0795deed1303dac7a38b68ea168ffd2883d8a84559df77c10ed3e91498e1da`。背景的精确定义、紧 α 和全部 source 参数绑定沿用已审证书。

每一行的 w、w_r 幂系数加余项分别包围真实的两个函数；二者不要求互为所保存近似多项式的导数。后台从来不对供应的 w 多项式求 r 导数。由此，可以在保持全部 w 行不变时，用另一个已经证明有效的 w_r 包围替换较差的 w_r 包围，前提是它们指向同一个精确背景和同一个物理区间。

原全域 producer 在外侧个别盒中为满足统一 w_r 工作宽度而过度细分。已完成的合法数据没有丢弃，也没有把未完成的全域运行改称完成。`db6f-tail-retain-packet-prefix.py` 只在保存 shard 内每个 span 都完整覆盖 u∈[0,1] 时保留它，新的 `finished` 仅表示显式选区已完成；字段 `parent_full_run_finished=false` 保留中断事实。

该 retainer 已独立审读和复跑，全部 JSON 字段同值，原数据一字节未改。其 5000 行完整覆盖 collar 与 spans 0–4422，下一未覆盖 span 为 4423。见 `2026-11-09-db6f-audit-retained-prefix.json`。

## 2. 用实际门判断需要的精度

对 spans 4561–4576，先以同一冻结 supplier、max-depth=0 产生合法宽包。16 行全部给实际曲率界不超过 6.203250756567895，即使部分 w_r 包的总宽度为 48，仍然满足当前 reach 曲率预算 $1250/147\approx8.50340136$。

这些宽包的 metric 只有 spans 4567–4571 超过 $10^{-6}$，最坏为 $8.169161123473551\cdot10^{-6}$。只将这 5 个 span 的 source 包细分至 depth 2 后，4567、4569、4570 已通过，只有 4568 和 4571 需要 depth 3。两个 depth 3 修包完成后，该困难区域的全部连续 metric 界均小于 $10^{-6}$。这些都是实际后台输出，工作容差未达标本身不代表包失去包含性。

此外，原完整 coarse 运行已经证明**整个** suffix [4423,4637) 的实际曲率不超过 7.16173506642038；其最大值位于 span 4509。该证明使用 $w\in[0,16/15]$ 和 $w_r\in[-24,24]$。全 raw 0 的较大粗曲率位于 span 4308，属于保留的精细 prefix。因此 suffix 无需继续追求极窄的 w_r 多项式余项。

相关实际门输出为 `2026-11-09-db6f-audit-tail-wide-critical-consumer.json`、`2026-11-09-db6f-audit-tail-critical-depth2-consumer.json` 与 `2026-11-09-db6f-audit-tail-critical-depth3-consumer.json`。完整旧 coarse 曲率数据保持原 hash，未因后续选择而更改。

## 3. 最终选择顺序

以下每一步只覆盖完整的原始 geometry span；表中区间采用左闭右开整数索引，−1 是 collar。

| 顺序 | 物理 span 范围 | 供应包 |
|---|---|---|
| 1 | 全部 | 已审 `tail-background-coarse-int2` |
| 2 | [−1,4423) | 保留的 `tail-background-tight-int2-prefix`，5000 行 |
| 3 | [4423,4637) | `tail-background-tight-int2-suffix-wide`，214 行，depth 0 |
| 4 | [4567,4572) | `audit-tail-critical-depth2`，20 行 |
| 5 | [4568,4569) | `audit-tail-critical-4568-depth3`，8 行 |
| 6 | [4571,4572) | `audit-tail-critical-4571-depth3`，8 行 |
| 7 | [4423,4637) 的全部子盒 | 只将 w_r 重新继承为已审 coarse 的常数包；w 不动 |

所有文件名均带 `2026-11-09-db6f-` 前缀，位于本题 notes。最终文件为 `2026-11-09-db6f-audit-tail-tight-final-packet.json`，元数据 SHA256 `6655b639db57bd2635aa012d460dcfa5f77b4ebdea750568d23f6dac5e7a3c5f`。它有 5237 行，数据约 313KB。

`scripts/db6f-audit-overlay-tail-packet.py`（SHA256 `87218edf0b73b6e67dae3c58a618841601dc64b093b24519820bcfd63efca839`）只核对共同输入 hash，检查所覆盖 span 的完整无缝分割，给较低次数的数组添加精确零，再选择、排序原行。没有插值或改变任何原系数。

`scripts/db6f-audit-tail-inherit-coarse-wr.py`（SHA256 `718ae3b47154083cf0c5a17fd65cea6dad25b4440fd8e31d1dbcad1ba9748f1e`）要求 coarse 的 w_r 是整个原 span 上的常数区间；每个被替换的 fine 子盒都在该原 span 内。它只替换 w_r 系数及其余项，并保持全部 w 和物理坐标数组不变。共同 exact source 的 checkpoint、calibration、A/B 证书 hash 均必须相同。

这两个 helper 的独立代码审查另交 root。解析 supplier 的包含性与该逐行组装是两个分开的证明责任。

## 4. 完整后台运行

```sh
python scripts/db6f-audit-tail-metric-curvature.py \
  --manifest notes/2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json \
  --packet notes/2026-11-09-db6f-audit-tail-tight-final-packet.json \
  --out notes/2026-11-09-db6f-audit-tail-tight-full.json \
  --angular 128 --direct-threshold 8.5 --progress 500
```

后台仍为已交叉审查的 `ed175aacdb2ba3e84d7c397d121e90c2a6a1492d05f5efdb646690481d302670`，没有因这次包组装修改。其全域 partition 检查会重新验证 collar 和所有有限 span 的每个局部 u 区间，无缺失或重叠。

本次完整运行已经完成，5237 盒全部覆盖，给

$$
\epsilon_{tail}\le9.968938237875866\cdot10^{-7},\qquad
K_{tail}\le8.46544537300005.
$$

精确 Fraction 比较确认两者严格小于 $10^{-6}$ 和 $1250/147$。共 10 个盒调用直接曲率路线，其余采用已证明的背景联络扰动界。最坏 metric 盒在 span 4570；最坏曲率盒在 span 4301，后者的扰动上界刚低于工作 trigger=8.5，所以没有触发可选的直接路线。

完整报告为 `2026-11-09-db6f-audit-tail-tight-full.json`，精确门比较和依赖记录为 `2026-11-09-db6f-audit-tail-tight-full-thresholds.json`。这里只认证完整尾组件与 collar；全闭图的 support、前缀和标记帽曲率仍由相应证书组合。数值 $1/(K_{tail}\cdot3.92)>0.03013450912222017$ 是组合 reach 定理所需的曲率比例下界，单独不是一个闭曲面 reach 声明。

解析 supplier、组装 helper 的独审与 root 全量重放继续按各自记录执行。固定 g 加密收敛以及 README 的其它剩余要求不由本次尾部运行自动推出。
