# 第二档 critical 尾的精确数据接口审查

审查者：`/root/independent_geometry`，2026-11-09，未参与数值优化。

结论：**完整数据、精确径向锚和共享接口 PASS。** 这不替代该新有限图自身的 metric、曲率、闭图拼接或收敛认证。

manifest 为 `2026-11-09-db6f-tail-inc-flat17-m12-critical-r005-outer128-q512-manifest.json`，SHA256 `79e0ebcdca1654e4186eb245c02ce89d0fd6c88cd174a3317d30bbd798d47c69`。出口方法和冻结源码仍是先前已审的 critical increment exporter；本次只改变 raw0 网格工作设置。

新增独立脚本 `db6f-audit-increment-data.py` 不调用 `IntegratedTail` 或数值求解器，逐个读取 gzip 分片，仅保留一块数据，并以 Fraction 累加所存精确二进增量。报告为同名日期前缀 `audit-critical-r005-data.json`，绑定脚本、全部数据、全部声明源码和输入 checkpoint 的 hash。

完整检查如下：

- 26 个数据分片的实际文件字节数与 hash 全部符合 manifest；最大文件 4,419,822 字节，小于 5 MB。
- 所有数据均为有限双精度数；567 列的完整标签、141 个系数及四类节点/导数数据布局逐项核对。
- 25 个相邻分片的整行共享节点逐字节相同，检查包括所有位置、导数、中点数据和局部增量列。
- 20,953 个唯一节点、20,952 个所存精确增量全部严格为正；Fraction 总和等于声明的精确二进总和。
- 归一系数严格等于 $(r_{\rm outer}-r_{\rm inner})/\sum\ell_i$；精确累加后端点严格等于 $r_{\rm outer}=r_{\rm cut}$。
- $0<r_{\rm cuff}<r_{\rm inner}<r_{\rm cut}$，全部 Fourier 频率满足已审三重对称表示条件。
- 与第一档 critical manifest 比较，checkpoint、全部参数、源码 hash、格式、内外锚完全相同。变化仅在工作网格设置中；具体设置键记录于 JSON。

进程实际退出码 0，峰值 RSS 为 51,322,880 字节。首次开发运行在列布局 guard 处安全拒绝，因为新审计脚本把 manifest 的标签列表误当成整数列数；修正为核验列表长度及全部标签后完整重跑通过。没有修改输入数据或任何几何常数。

重放命令：

```bash
python scripts/db6f-audit-increment-data.py \
  notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r005-outer128-q512-manifest.json \
  notes/2026-11-09-db6f-audit-critical-r005-data.json \
  --same-checkpoint-reference \
  notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json
```

该有限图的值由精确积分定义，后续保存的位置列仍只作诊断。对近似 source 中点和有限差分的语义限制沿用已经独审的出口方法稿，没有由接口相等推断源 ODE 精确解或 G5。
