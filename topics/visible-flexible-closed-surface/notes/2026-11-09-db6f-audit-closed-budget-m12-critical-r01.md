# critical 第一档闭图账本的独立复核

审查者：`/root/independent_geometry`，2026-11-09，未参与数值优化。

结论：**同一实际对象的输入绑定与完整标量账本独立重放 PASS。** 这里不挪用 M12 uniform 的尾端值，也不宣布当前仍在运行的完整 critical 尾 metric/曲率证书已经完成。

## 1. 作用域

`db6f-root-common-cut-v2.py` 与 `db6f-root-closed-budget-v2.py` 的数学和实现已经分别通过此前全文审查。本次未修改它们；前者 SHA256 为 `317e519fda8d78fb70b53f8a8c80d51599dec1ac46e92741cd9b2576a3f4fa7d`，后者为 `0d68b718a43a69b24a865b1932e2700a47190724a3be4ea3f1202b56d1a59641`。

root 为 critical 第一档重新实际完成 common-cut 构建、前缀几何 256 角区间、连续 metric 和体积矩 512 角区间。此审查按要求核验这些新输出的输入绑定，并独立重跑轻量闭图账本；没有重复全部前缀数值计算。

实际闭图元数据为 `2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json`，SHA256 `253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2`。其尾 manifest SHA256 为 `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104`，正是当前完整尾验证器的输入。

## 2. 复核项目

- 作者账本七个输入文件的实际 hash 全部核对。
- 前缀 geometry、metric、moment 报告都绑定这个 critical common-cut 元数据及同一基底 NPZ 数据。
- 主几何的 base geometry、checkpoint、精确 bridge 参数证书、尾 manifest 和 reader 实现 hash 全部核对。
- 新一阶尾证书绑定 critical 第一档自身，未复用 uniform 一阶数值。
- 同背景 transfer 的新 manifest hash 与该尾一致，旧 checkpoint 与已审高度、正 alpha 证明相接；原账本执行时重新核验全部物理参数及全径向域。
- 所有保存的有理数上下显示方向均以 Fraction 重新核验。
- $D=98/25$、握持变化严格超过 $D/20$、握持区直径严格超过 $D/5$、完整第三体积矩和帽矩增量严格为正、精确目标前缀 metric 小于 $10^{-6}$ 均作精确有理数比较。

## 3. 独立重放结果

独立进程实际退出码为 0。`2026-11-09-db6f-audit-closed-budget-m12-critical-r01-replay.json` 与作者账本 **全部 JSON 字段相同**。绑定及比较报告为 `2026-11-09-db6f-audit-closed-budget-m12-critical-r01.json`，SHA256 `08f6c10d7c353377d5c710105ea934b61ea38c24ab336347fe76d3afa6b2d49c`。

向外界给出：

| 项目 | 已支付的界 |
| --- | ---: |
| 完整曲面支撑函数 | $>0.7370435198982139$ |
| 直径 | $\le98/25=3.92$ |
| $\delta_{\rm hold}/D$ | $>0.0509926386289832$ |
| 无帽完整第三体积矩实部 | $>0.4401644538270966$ |
| 修正后前缀对精确目标的 metric 上界 | $<2.57211883244924\cdot10^{-8}$ |

这些结论的全相位、嵌入和非全等含义沿用已审闭图组装、正支撑和帽矩证明。当前账本的 `whole_tail_metric_certified=false`、`whole_tail_curvature_certified=false`、`README_complete=false` 均已保留；不会从标量账本推断尚未完成的全尾计算或 G5。
