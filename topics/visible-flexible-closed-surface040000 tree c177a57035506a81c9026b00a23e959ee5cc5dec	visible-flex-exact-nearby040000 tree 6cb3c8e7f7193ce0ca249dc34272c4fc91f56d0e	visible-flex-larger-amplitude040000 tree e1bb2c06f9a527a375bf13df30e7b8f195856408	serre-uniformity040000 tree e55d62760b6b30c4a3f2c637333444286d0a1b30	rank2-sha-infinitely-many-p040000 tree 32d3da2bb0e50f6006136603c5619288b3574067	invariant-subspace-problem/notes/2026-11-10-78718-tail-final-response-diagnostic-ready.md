# 最终原H自有响应的两个最小浮点诊断

本文件准备实际入口；写作时只有低H延拓运行，没有在此预填最终原H成功包或生成任何诊断结果。
它不是新的完成门、审批或独立重跑流程。生产求解和完整XYZ导出继续由根及numerical负责。

## 1. 读取实际响应本身

目录为本题根。令 `visible_final_tail_packet` 指向真实完成的最终原H响应gzip包，
`visible_tail_diagnostic` 为新的小JSON输出路径；实际原H身份由主Coordinator及实际响应记录决定。

```bash
node scripts/78718-tail-response-diagnostic.mjs \
  --packet "$visible_final_tail_packet" \
  --out "$visible_tail_diagnostic" \
  --cell 0
```

程序直接读取该包的config和checkpoint，保持自己的M、N、physical depth、shooting parts及steps。
它只从保存的shooting节点出发，按该响应实际配置的steps重放指定物理cell0的局部状态流以定位内部峰；
不构造更高M的补零状态，不运行shooting或BVP。
在选出的真实峰状态上，仅把角求积N翻倍，记录共角点height jets及Gram变化，并计算该点有限范围的Ω谱。
谱频率检查范围写入报告，不把有限谱表当无限高频上界。

默认使用本题 `repro/source-root`，也可用 `--source-root` 指明同一实际生产依赖目录；
两个源环境变量在新诊断进程中一致设置。新诊断不编辑生产模块。
报告保存实际请求height的数量、范数与SHA，便于核对调用的究竟是哪一个H；
它不凭收敛标志自动认定该请求已经是最终原H。

同时生成一个很小的 `-peak-metric.json.gz` 数据文件，保存原N和细2N角网格上的源Gram三个分量及物理半径。
数组留在终端文件内，程序只打印标量摘要。每件输出都必须小于5MB。

## 2. 同源XYZ manifest出现后比较同一点

numerical现有生产导出入口为
`scripts/db6f-prefix-endpoint-critical-increment-export.mjs`，输入同一个最终原H自有包；
生产计划提供实际depth、steps/flow-steps、angular-nodes和degree；
写作时的基线为depth8、planar degree192及原critical/endpoint细分策略，实际参数以完成的生产plan与manifest为准。
不为这个诊断重复导出。待其真正完成，并把实际manifest路径放入 `visible_tail_manifest` 后运行：

```bash
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  scripts/78718-tail-representation-at-response-peak.py \
  --manifest "$visible_tail_manifest" \
  --diagnostic "$visible_tail_diagnostic" \
  --out "$visible_tail_representation_diagnostic"
```

程序核对manifest实际输入包的SHA与源诊断相同，然后用原IntegratedTail长双精度读法，
在同一个半径和同一细角网格上计算实际有限XYZ图的Gram；原N共角点另给一个独立对照，
避免把N翻倍产生的源变化全部算进XYZ表示误差。
比较的是三分量矩阵差的算子范数，不是两份全局最大值简单相减，也不依赖两幅图的刚体位置规范相同。

这一步仍是浮点的单半径比较；源RHS与有限C²表示的差、N翻倍引起的源变化在报告中分别可见。
它不替代整图连续metric、曲率、reach、闭合或README完成标准。
若真正新图的最大误差位于另一个physical cell，再只对那个实际cell调整第一条命令。

## 当前实现状态

两个程序均已通过语法解析。源码输入处理曾发现新诊断进程需要同时设置
`CLOSING_TAIL_CACHE`，现已与sourceRoot一致处理；该缺项发生于导入阶段，未产生成败曲面结论。
本入口尚未消耗最终原H响应，也没有将旧图或低H试验填作它的结果。
