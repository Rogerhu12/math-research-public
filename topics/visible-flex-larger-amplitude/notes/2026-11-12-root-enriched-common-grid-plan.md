# 已知峰保留的共同几何网格与完整流式LP

第一基准场正式完成，但629×192网格漏旧同状态κ峰；旧场与计划保持不变。新 `root-q095-five-direction-geometry-r2-plan.json` 已准备11条完整暖态诊断命令，尚未运行实际场：全部2004个raw节点、uniform257数值点、uniform241物理点、每物理knot区间33点及旧峰映回同一数值chart，共3178×384；逆图round-trip和已知角点都在准备时核对。全部raw/24模/production mean保留。

`root_actual_geometry_field_chunks.py` 与原场生成器的几何公式相同，只把输出改为连续径向块的无损gzip NPY，每块原始数据≤4MB，完整JSON清单仅在所有块完成后写。读取逐件核SHA/形状/连续行覆盖。已有baseline重复成两块的字节夹具，经普通与磁盘数组读取均逐位相同，遗漏行和内容改动均硬拒。

`root_geometry_streaming_lp.py` 的五个原不等式组（两主曲率各正负、twice-radius）全部保留；五个中心差分存临时磁盘数组，每轮LP后逐批扫描全部有限行，只把下一轮活动行保留在小矩阵。它不依赖最坏点固定或丢弃未活动行。随机11000原约束与直接完整矩阵LP比较，全部行核对通过；不可行例正确返回status2。session16038正式exit0，wall6.840422秒/峰89652KiB。

这些不支付连续径向/角向余量或任何新曲面存在门；所有场均为完整实际Jac方向的未解暖态。数值窗口当前归q105 disk4388，新的11个物理场和实际LP都未执行。完成实际场后，按同计划/全部源SHA用 `root_geometry_streaming_lp.py --plan notes/2026-11-12-root-q095-five-direction-geometry-r2-plan.json --out <fresh.json>` 执行有限局部设计，再对选出的联合方向做真BVP。
