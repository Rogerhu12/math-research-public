# 新 full-H 的首段完整有限谱连续几何已实核

## 同一实际新场的首段结果

在真正 full-H 包返回后，原 `seam_run_tail_geometry_v2.py --phase stage0` 已实际运行，13.7566 秒返回。原 M24/N512 的完整有限谱是 planar degree 254、170 个 planar 模和 25 个 height 模；没有把完整非线性图替换成只有 24 个输入 H 的几何截断。

首段连续 metric operator 上界为 **3.59999724518074e-8**，principal-curvature 上界为 **8.177308001953627**，原首段 metric 与 curvature 分配门均通过。几何数据绑定同一真 full-H 包、同一完整 fresh native J、原完整 mean-chain 和同一 R58 真积分背景。

此证书只覆盖 **stage 0**。当前 bundle 只有该段，不能送入要求全部 1,152 段的 `ActualFiniteTailV2`、complete-tail radius identity 或完整闭图验收，也不能据此声称全尾通过。后继原 `--phase all --resume` 复用此首段的全部二阶 jet 和证书字节，只导出剩余 1,151 段。

## 真实文件与容量

stage-0000 JSON gzip 为 **195,304 B**，解压 **485,821 B**；首段证书 **70,562 B**。全尾共同 native mean-chain 是一次性的 **1,363,861 B**，不按段复制。首段流水线全部输出为 **1,702,945 B**。

若其余段与首段体积相近，1,152 段 gzip 约 224,990,208 B，证书约 81,287,424 B，加完整索引、manifest、summary 后约 320–340 MB。这个数字是以实际首段作外推，**不是**所有段的严格容量上界，后续仍要看真实磁盘余量和其他写入。

资源记录中的 `getrusage(RUSAGE_CHILDREN).ru_maxrss` 实测为 **179,636 KiB**。独立 `/proc` descendant sampler 只看到约 11.8 MB，明显小于真 child 高水位，说明没有覆盖全部后代；其 `sampled_peak_summed_tree_RSS_bytes` 字段不能用于总峰或内存上界。原记录保留不改，这里明确纠正适用范围；真实 rusage 也只是被等待 child/descendant 的最大值，不是同时存活进程的 RSS 总和。

完整源/文件大小/哈希保存在同名 JSON。原 worker 的 normalizedFullDefect 与此处的连续 metric 是不同量，本结论没有用前者替代连续估计。
