# 原完整 full-H 尾几何执行的真实终态

维护：Astra-held10-7c4e33ee-20261128 / tail_closure，2026-11-28。

**实际执行结果：** TTY 43666 返回 exit 2；它表示原 certificate allocation 未全通过，执行本身已走完全部 1152 个真实 stage、18,460 个原径向 spans 和实际 deep collar。stage 0 的已付证书完整继承，没有重跑。全部源、参数、原输入/输出 SHA 见[小记录](2026-11-28-tail-original-full-geometry-terminal.json)。

| 原严格连续结果 | 真实返回 |
|---|---:|
| 通过原 $10^{-6}$ metric 门的 spans | 17,644 |
| 原上界尚未付过 metric 门的 spans / stages | 816 / 52 |
| 原最大 metric 上界 | $1.5592122745872465\times10^{-4}$ |
| 原最大主曲率上界 | $10.017503096013616$，stage 82 |
| 原 $K<10$ allocation 未过的 stage | 仅 82 |
| 实际深 collar metric 上界 | $1.4617380072747594\times10^{-29}$ |
| 实际深 collar 主曲率上界 | $8.000000000000002$ |

这些 metric 上界超过阈值**不构成实际度量误差的下界**。同场真实 $w(R)$ Taylor 补充已在[两个完整 stage](2026-11-28-tail-two-complete-stages-true-w.md)严格付过原门，并继续仅处理原未付区间。原所有输出及其 false 标志保持不变。

**同时已证明：** 原完整共同二阶 jet 链与新实际深 collar 的外端二阶 jet 精确相等，内端为精确零二阶 jet，接自身旋转背景及平盘为 C²。整个尾盘的平面投影单射：所有实际 stage/collar 的归一扰动一阶范数均小于 1，内盘扰动为零，完整 Cartesian 扰动在凸圆盘上为 C¹；沿任一直线段积分即得 $\operatorname{Id}+V_{xy}$ 单射。此结论不依赖尚未通过的更紧 metric 门。

原 $K<10$ 是此入口的内部分配窗；有效严上界 $10.017503096013616$ 仍在全局 $K\le12.3$ 预算内。后继绝对 placement 以同一已证上界核对全局预算，绝不把原 $K<10$ false 改成 true，也不重复计算原曲率多项式。

完整原证书合计所报时间为 3302.6901860430007 秒，其中 remaining 运行 3297.839959961999 秒；chunk 管线所报总时长为 5901.390749691003 秒。不同计时范围保持分列。

本条只属于原 λ=.002/M24、完整 raw-H factor 1 的同一有限尾场及其自身深盘，仍非八轮 coupled physical-H。原宽高度窗口的 placement、实际 cut、全闭图、同 g 精化与握持完成标准均不由此自动得到。
