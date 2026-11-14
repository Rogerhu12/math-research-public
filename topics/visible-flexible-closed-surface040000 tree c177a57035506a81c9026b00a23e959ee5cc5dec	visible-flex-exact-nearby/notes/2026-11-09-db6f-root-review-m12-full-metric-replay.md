# M12 critical 第一档：完整 metric 后端的独立重跑

2026-11-09，root。状态：**实际退出 0，全部 30,971 数学行及报告数学字段逐值相同**。
本记录补齐新 M12 汇总稿独审时尚在运行的第二份完整后端计算。

在本题目录执行：

```bash
python scripts/db6f-audit-tail-metric-only.py \
  --manifest notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json \
  --packet notes/2026-11-09-db6f-audit-transfer-lowmetric-final-m12-critical-r01.json \
  --out notes/2026-11-09-db6f-root-tail-m12-critical-lowmetric-replay.json
```

进程实际退出码为 0。耗时约 1,657.16 秒，峰值进程 RSS 334,225,408 字节。
全部有限跨及圆领共 30,971 个包行均完成，相对算子误差上界的保存端点为精确二进有理数

$$\frac{7055251261315967}{302231454903657293676544}<2.334387\cdot10^{-8}.$$

独立报告与原 `db6f-audit-tail-m12-critical-lowmetric-full.json` 的 manifest、packet、
数据、源实现 hash 均相同。两个逐行 gzip 文件分别重新核 hash 后解压，在内存中逐项比较，
30,971 条记录全部完全相同；未把大数组或二进数据读入对话。
除输入/输出路径写法、逐行文件自身 hash、耗时和峰值内存这些非数学字段外，
全部报告字段也完全相同。原包分区的独立 Fraction 检查因数学行相同而适用。

同名 JSON 保存两个完整报告及两个逐行文件的实际 SHA256、逐值比较结论和源绑定；
比较报告 SHA256 为 `73f3678feb51c2d61ea3378c751311d0b2926ae68cc223ea974575daaa702fae`。
这次运行仅重算度量，曲率仍来自同一图此前独立审查的完整曲率证书。
完整后端复跑不等于重新求解源 BVP，不把一次真实误差下降升级为 G5，
也不替代最终冻结候选后的全流程 fresh 审查。
