# 新公共 Cartesian 前缀连续几何：实际执行与范围

日期：2026-11-28。会话：Astra-held10-7c4e33ee-20261128。

完整证明和准确有限对象见 [R73](../results/R73-new-common-cartesian-prefix-continuous-geometry.md)。本次不是旧 R62 重跑；输入为新 879 节点原接受场，最终 Cartesian 图有 945 个公共节点，并使用明确的新有限均值。

## 实际执行

在本会话统一工作目录恢复本次 `design-material-recovery-20261128/lambda002_m24/run.json` 后，从公共仓库根执行：

```bash
python topics/visible-flex-held-10pct/scripts/resume_20261128/geometry/cartesian_prefix_interval_geometry.py \
  --source-run /workspace/scratch/7c4e33ee17de/held10-design-work/design-material-recovery-20261128/lambda002_m24/run.json \
  --outdir /workspace/scratch/7c4e33ee17de/held10-geometry-work/new-prefix-interval-20261128-v2 \
  --angular 1024

python topics/visible-flex-held-10pct/scripts/resume_20261128/geometry/cartesian_prefix_curvature_rounding.py \
  --certificate /workspace/scratch/7c4e33ee17de/held10-geometry-work/new-prefix-interval-20261128-v2/summary.json \
  --out /workspace/scratch/7c4e33ee17de/held10-geometry-work/new-prefix-interval-20261128-v2/exact-curvature-budget.json
```

不同 workspace 只替换路径；核心、实际物理系数、所有原节点、mean1168/GL6、中心宽度、角盒数量及原门不因此改变。真实输出为 `continuous_new_prefix_geometry_certified`，966656 盒，未决0；严格阈值后处理为 `same_new_prefix_exact_rational_curvature_budget_certified`。

初版首次运行在核心初始化进度回调抛 `TypeError: dict() got multiple values for keyword argument 'seconds'`，发生在完成几何计算之前。修正为明确覆盖回调字段后在新目录执行；没有将这个日志工程错误当数学失败、也没有计入成功覆盖。

## 完整记录

- [原几何标量 JSON](2026-11-28-new-prefix-continuous-geometry.json) 是实际 `summary.json` 的逐字副本，含真实源、完整字段、所有脚本哈希和 oracle 参数；不含大数组。
- [精确有理曲率收紧](2026-11-28-new-prefix-exact-curvature.json) 保全部分数与证明关系，不将 binary64 的 `12.3` 误当准确 $123/10$。
- [独立点与定义数据核对](2026-11-28-new-prefix-map-point-check.json)重新由源构造图，全部公共定义数组逐位相同；首、中、末等六个实际闭盒的108个数值 Cartesian jet 分量均落在独立重组的包围中。这只是实现核对，不代替全盒证明。

所有大数组仍在对应 scratch 输出目录；定义数组 SHA 为 `02bba64a6afc45903b95ed159daa5d761d3f3d5121dbf980caac94d0e2b1fa10`，核心角盒数组 SHA 为 `3dbe52090953c556abcab1fffd93bb784a18fde185851ac45e23cade85fcab52`。不将可再生证书、网格或二进制加入 Git/Release。

## 继续项

本次几何界属于尚未附尾和 cut 修补的这张新图。前缀 metric 只有另记的实际采样值；连续 metric 需同一最终图和同一目标 $g$ 的区间验证。实际原全-H/native 尾和设计 $\lambda$ 推进同时继续；这项局部连续几何不满足课题完成标准。
