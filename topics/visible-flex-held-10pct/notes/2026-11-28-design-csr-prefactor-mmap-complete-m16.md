# 完整 CSR 在 QR 前映射：真实 M16 完整矩阵逐位核

2026-11-28 UTC。这里只验证执行存储，没有新的 BVP 步或接受场。

`complete_csr_prefactor_mmap.py` 先把真实完整 CSR 的 data、indices、indptr 逐字节复制到真实预分配的 scratch backing，保存原全部显式零。原 `eliminate_zeros` 仍只执行一次；仅该 CSR 实例的 `prune` 存储策略改为保留完全相同的前缀 view，原验证及消零算术不动，随后恢复实例方法。消零后的三数组只读；原 BlockQR constructor 只在完整 edges 抽取完毕后插入一次 mapped 页面释放，全部递归 QR 数值语句以及原 `_apply`、`_solve`、完整 residual/refinement 算法不动。原完整 CSR 对象仍交给同一 factor。完整 QR 返回后，再复用已核 factor-only mapper 存全部持久因子。

首次 session 31963 在映射前的真实磁盘门拒绝：当时 free 570,363,904 B，不足完整 M16 CSR、全部因子与 512 MiB 外余量所需上界 700,832,991 B。没有分配 backing，也没有数学失败。之后实际磁盘窗口回到 1,113,649,152 B，独立新输出 session 5948 正常 exit 0；用已保存实际 M16 的 43,087 维原矩阵及原残差核验，无新 Jacobian 装配。

完整方向、每个 backward-error 分母、完整原 J 残差、matrix_inf、所有原 factor/solve stats 全部逐位相同；初始三数组 SHA、原消零后的三数组 SHA 和 nnz 也一致。保留同一 CSR 对象、全部 CSR/factor 数组只读、实例 prune 已恢复。绝对原 J 残差最大值仍为 1.066670079402443e-20。禁用 cyclic GC 后，factor、CSR backing、QR backing 的 weakref 全立即为空，两个独占映射目录与文件都立即移除。实耗 6.255603068 秒，整个对照进程峰 RSS 208,540 KiB。

这次 M16 中，CSR 逻辑字节数为 59,115,368 B，真实 backing 59,121,664 B。映射并 allocator trim 前后 RssAnon 从 116,191,232 降至 34,938,880 B；此值包括当时 allocator 中已可释放页，不能等同于 CSR 逻辑字节。完整 edge 抽取后，再释放映射页与 trim，RSS 从 152,842,240 降至 89,919,488 B。两套完整存储都就绪后 RssAnon 为 39,038,976 B。这些都是 M16 实测，未声称 M48 已释放任何固定字节，也不能把 mapped 逻辑大小作为 MemAvailable 信用。

旧 factor-only 子组件仍报告其原生字段 `complete_CSR_remains_anonymous=true`，这只描述该冻结子组件本身的职责；本组合的真实 CSR 位置由独立 CSR store、共享 mapping 检查和完整三数组 SHA 证明，组合不把该旧字段当作事实。原 CSR 装配峰依然需要付；完整 warm solve 仍按所有 matrix/factor 页面可能同时驻留预算。后继预算将保留至少 512 MiB 外余量及实际磁盘门，全部原数学门不变。

源 SHA、保存矩阵/残差来源、完整逐位检查及每次真实内存观察见同名 JSON；数组与临时证书未进仓库。
