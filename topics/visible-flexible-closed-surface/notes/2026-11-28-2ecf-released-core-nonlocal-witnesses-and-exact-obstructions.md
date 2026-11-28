# 完整释放闭核的实际近点对与准确非局部厚度反例

[R290](../results/R290-two-actual-released-core-nonlocal-reach-obstructions.md) 对两个完整保存位置给出了严格 reach 上界。第一场是[释放原 .8 切圈的首个实际场](2026-11-28-2ecf-actual-release-of-developed-cut-to-inner-flat-cuff.md)；第二场是[富集母场加真实双球 XYZ 修正](2026-11-28-2ecf-released-flat-cuff-simultaneous-held-and-local-curvature-physical-field.md)的第二态。两场均保持同一目标，反例涉及改变帽之前即已存在的两片上核区域。

## 实际有限搜索

完整原 R267 中央、全部真实 H65 径格及中点、准确短 coast、每个已保存连接单元及中点、右侧真平面环和闭合平盘均逐函数求位置和法向；下半由真实反射给出。角向为 96 个偏移 .271 的均匀角，另含两平盘圆心。初始原场共 69794 点，带双球修正的富集场共 82082 点。对空间距离不超过 .194 的全部取样点对，使用真正两端法向的最大绝对内积计算法球比。两组分别实际处理 20782374 和 26827422 个非退化近点对，进程自然退出 0。

| 完整实际场 | 取样最小法球比 | 见证材料径坐标 | 同角取样值 |
|---|---:|---|---:|
| 原释放场 | .0713522718855 | .324794275245、1.25891454858 | 4.73012588891 |
| 富集加双球修正 | .0686050491385 | .331021743734、1.26981261844 | 1.58853323532 |

后一对的空间距离 .13690238，两法向几乎相反。不是近邻材料的局部曲率见证，而是相隔约 .939 的材料径区间。两组的采样极角导数最小值约 .541765，尚未得到全局单射结论；已试常数斜率的斜投影径导也有负值。完整 R273 外凸帽没有在这个有限搜索中数值离散；R290 的反例对任何保留两个见证点的嵌入闭帽扩展都成立，因此不需用假帽网格补齐。

首个同参数搜索已完成计算，但最终创建 JSON 时遇到真实 `ENOSPC`，未保存结果，退出 1；未将其算成成功或发布结论。原脚本版本保留为 `2ecf-released-flat-core-normal-ball-search-v1.py`。之后保持完整原搜索参数，以支持实际修正和临时输出回退的新入口重新执行。源、原生数学输入和点对覆盖没有缩减；这次必要恢复和另一新场的结果分别保存。共享盘恢复期间，仅调整本会话的可恢复 Git 索引缓存；私库同一 HEAD、干净状态均核过，77460775 字节普通索引转换为 899 字节稀疏索引，完整原索引的 SHA 与备份保留。本条数学结论不依赖该工程处理。

## 准确两点消费者与重生

有限见证随后取成准确 \(u=\pi/2\) 和两组 dyadic 径坐标。源码逐项消费全部 Fourier–Hermite 模及第二态完整 216 系数，以 `Fraction` 计算位置、两切向、未归一法向和严格有理不等式。无需数值三角函数或浮点特征值。两个实际消费者自然退出 0，分别得到 reach 小于 .073 与 .070，从而归一化值分别小于 73/2800 与 1/40。

先按上引两份实际源记录生成完整场及状态。设 `S` 为公开 scripts，`W` 为再生目录，`O` 为一个新的结果目录：

```bash
python "$S/2ecf-released-cuff-exact-two-point-reach-obstruction.py" --state "$W/polar-released-cut-true-flat40.json" --field "$W/polar-released-cut-true-flat40.npz" --s1 83/256 --s2 323/256 --radius 73/1000 --output "$O/original-two-point.json"
python "$S/2ecf-released-cuff-exact-two-point-reach-obstruction.py" --state "$W/polar-released-cut-flat40-enriched.json" --field "$W/polar-released-cut-flat40-enriched.npz" --correction "$W/polar-released40-actual-cartesian-hardspheres.json" --s1 85/256 --s2 325/256 --radius 7/100 --output "$O/held-two-point.json"
```

完整近点搜索的 `--work` 是含这两份场和其已列所有依赖的工作目录；`--command-receipt` 消费原完整观察回执的 `command` 路径参数，`--state`、`--field` 给相应源，第二场另加 `--correction`。默认 96 角、.271 偏移和 .194 搜索半径就是本次实际值。若在新的再生目录使用该有限诊断，可将与原观察命令相同的九项路径参数放在一个仅含 `command` 数组的 JSON 中；它仅定义输入路径，不代表已执行回执。准确结论的上面两个命令不需要任何该类路径回执。

| 源码或实际报告 | SHA-256 |
|---|---|
| 2ecf-released-flat-core-normal-ball-search-v1.py | `d7a251529ab55d80c6d7da9991b64248068da757a80bfec226a4faed47a81906` |
| 2ecf-released-flat-core-normal-ball-search.py | `1e9b9fbbf56f56bc8fb2b9fba0870aeb1da350902bd76286162146178fdedbd6` |
| 2ecf-released-cuff-exact-two-point-reach-obstruction.py | `dbc0ff8ea0e393fce05b0463cbc13c35c1e3c341110a0b14af6a940bfabdc15d` |
| visible-flex-2ecf-released-flat40-complete-core-normal-pairs.json | `39f3cd1ab253b2a1d74105ab19bab8ca0d247e51bb97d51b38f1eee5aef59031` |
| visible-flex-2ecf-released-flat40-held-complete-core-normal-pairs.json | `7d547f83be90f025d66629084edc97f4503dbceec4dc90aff7ef8c18cefdb490` |
| released-flat40-original-exact-two-point-reach-obstruction.json | `2e2467979c809197b50d3f750342edac5ab17a765c05687a2da55dc5a49d7ae0` |
| released-flat40-held-exact-two-point-reach-obstruction.json | `cf3db294f5b0c6239938dded80481f502984ec0df3ca13344596dd73344f2e9a` |
