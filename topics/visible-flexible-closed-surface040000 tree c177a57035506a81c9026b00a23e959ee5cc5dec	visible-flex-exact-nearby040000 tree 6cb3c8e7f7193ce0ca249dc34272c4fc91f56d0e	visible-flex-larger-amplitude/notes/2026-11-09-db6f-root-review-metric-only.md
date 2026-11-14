# 仅计算 metric 的连续后端：独立审查与完整回归

审查者：Astra-visible-flex-db6f0b0e（root）；实现者：independent_geometry。

**结论：静态数学范围审查及完整 M8 独立重跑 PASS。** 新脚本
`scripts/db6f-audit-tail-metric-only.py` 的 SHA256 为
`178d7b7b62deeff93d8e198f271736ac41f258c07b3d8b7a9bc111c909d5ebd6`。
精确依赖、报告与数据哈希在同名 JSON 中保存。

## 数学和实现审查

`first_fields` 使用已审 streaming 几何类的同一个 `span_polys` 或 R6
collar，只取前两个多项式。对局部区间的精确有理坐标、向外仿射限制、
Fourier 展开，表达式与已审 `fields` 对应两项逐式相同。冻结的
`metric_residuals` 只读取位置和一阶径向字段；其全部残差、归一因子和
算子范数公式保持不变。因此省去第三个字段的展开不改变 metric 包含性。

同一个冻结 `load_packet` 仍检查 manifest/data 哈希及从 collar 到最后
一个 span 的完整分区。即使只计算选定区间，也不省略这项全分区检查。
局部范围、pilot 限制与“全尾已覆盖”分别记录。输出明确写
`curvature_evaluated=false` 与 `curvature_certified=false`，没有把未算的
曲率填成零，也不据此作 reach 结论。独立的、绑定于同一图和同一背景
定义的旧曲率证书可以与新 metric 证书并用。

## 独立完整回归

root 用 R18 的同一 M8 manifest 和最终背景包运行新脚本，实际进程退出码
为 0。5237 个包行、collar 和全部 4637 个有限跨均覆盖。运行 132.49 秒，
峰值 RSS 为 75,988,992 字节。

`scripts/db6f-root-review-metric-only.py` 对全部 5237 行逐一比较包行号、
span 号与 metric 上界，并对全局坐标残差、算子上界、最坏位置、全部
覆盖字段及输入哈希进行精确比较，全部相同。完整上界仍为
$9.968938237875866\cdot10^{-7}$。

复跑命令（本题目录）：

```bash
python scripts/db6f-audit-tail-metric-only.py \
  --manifest notes/2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json \
  --packet notes/2026-11-09-db6f-audit-tail-tight-final-packet.json \
  --out notes/2026-11-09-db6f-root-metric-only-m8-replay.json --progress 1000
python scripts/db6f-root-review-metric-only.py
```

这里没有改变有限图、目标度量或任何数学界。新的背景包仍须另行证明
其点态包含性；本审查不支付源方程收敛、无限尾存在或 README 第 5 项。
