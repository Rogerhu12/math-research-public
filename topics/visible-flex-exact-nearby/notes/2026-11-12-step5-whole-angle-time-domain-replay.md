# 第二次恢复后的 whole-angle 真重跑

2026-11-12，constructive_route。

执行器恢复后，已将完整源码、证明及两套 grid 依赖放回 canonical 目录，
然后按原完整参数实际执行了第 419 段的全角/复时间证书。没有从摘要重填报告。

新报告：
`data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_whole_angle_time_domain.json`，
SHA256 `e1a2c3f327c3a36e33c412e76c70eebd185f224ea938dcdea93ee30ab9a05f90`。

三个必需 common spans 均已重新计算，`complete=true`、
`complete_common_span_coverage=true`、
`proved_full_physical_angle_and_complex_time_domain=true`。
三项 D 下界分别为 .16273449952651292377、.16564287848765126234、
.22500614436846167096；三项 Re(−K) 下界分别为
.57694455233667687632、.57694477751884642191、.57694499909214098007。
这些已在中断前工具输出中明确保存的数值与新输出一致。
报告其余所有区间、输入哈希、根细化和完整费用都来自本次真实运行，
不以数值一致性代替重新计算。

核心源码 SHA256 仍为
`d681614326efacb0c256037d2c7e995eb895d8f77ce4281720f44c76a896548e`。
证明正文保留其历史运行报告 SHA；本 note 与新完成清单明确指定当前有效的
重跑报告。旧报告含运行时间，整个文件哈希本来就无需与新报告相等。

两份 grid 全文的恢复 SHA256 为：

- `fourfold_phase_uniform_field_time_grid.py`：
  `7c5b0f94aa4e4008b23c1e30443454ad21d3885206206dddcbb7a834e1451c32`；
- `fourfold_phase_uniform_field_time_grid_fast.py`：
  `30655319d9172b0ac8de857f24329d944f5ec9d87b08ee283ee0292f90159aa8`。

root 在自身压缩检查点中独立保留了旧两份哈希，已确认上述恢复值与旧值严格一致。
因此这两份恢复也不是另一个算法近似版本。

原证明的对象、完整时间端点、物理角条带 1/64、时间盘半径 3、所有 germ
以及结论边界保持不变。它仍不是全分支残差、累计流或 KAM 证书。
后续 sine 径向像及转折适配源码是另一项在研工作，不包含在本次通过结果中。
