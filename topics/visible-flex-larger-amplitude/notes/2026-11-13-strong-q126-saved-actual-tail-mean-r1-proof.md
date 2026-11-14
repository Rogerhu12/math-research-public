# 当前 A 真有限尾部均值的缓存恢复

本包针对已真正接受的 q≈0.126、M32、32 个完整 core 系数、2590 前缀节点、原固定 g 的 A。原 actual primary SHA 为 `917d859e8a73fa663db1839e354909ae4f174bad1895f8717c20705cdd702aaf`；final tail response SHA 为 `018d19c6ca8c27acc5cc1dde6d396ee783e34ae25e5b525158c5bb37086520d9`。实际尾部为原 8 个物理 cell、576 个 numerical stage、steps12/quadrature512；没有改变任何物理参数或原验收条件。

## 恢复而不重算

原 solver 的 `meanHeightToCut` 等于最后一次完整 variational evaluation 的全部 stage `meanHeight` 前向求和。标准 response 没有导出这个量，但原 exact-stage store 保存了它。本消费者按接受点的完整二进制 states（保留 signed zero）生成每个 stage 的原缓存键，检查全部 header/input/payload SHA，并把每块完整 J 与最终已归档 full-flow 的对应 J 逐 bit 比较。576 个 stage 全部吻合。

由原相同求和顺序得到实际有限尾 meanHeightToCut = **0.022683979296285784**。更稳定的 fsum 为 0.02268397929628579，所有 stage 增量均为正。原 factory 的同 8-cell 背景高度积分为 0.02268424606570169，两者相差 −2.667694159047551e−7。两种积分规则不同，所以这个差不能独称非线性修正，更不是严格积分误差界。已保存 factory 背景在 cell8 以后另有 6.509982702811914e−8，仍只是背景资料。

## 紧凑且可恢复的保存

每 stage 原 out[64] 和 meanHeight/minA/minD 共 67 个 Float64 按原 bit 保存；576×67 的原始 308736 字节压成 299695 字节。另存原完整 stage identity 和每个原 header。全部 576 个原缓存文件用本侧车和已有 full-flow J 块重建后，文件 SHA 与原缓存逐项相等；没有再复制 18,874,368 字节原 J。若临时 cache 丢失，独有 mean/out 字节仍在此包。

消费者真实 owned exit0，1.5103963 秒、RSS51236 KiB、3498 门。没有调用 factory、momentum root、ODE、Newton、variational solver 或 Git，也没有重新接受任何候选。

## 范围

这是当前真有限解上已经付过计算成本的离散积分值。它不能控制角向高度模、整个 Cartesian frame、无限尾、固定帽或连续径向误差，不能独自给闭面直径、Hausdorff 振幅或 reach。后续候选仍须走原真 H、完整 J、BC 和最终 audit。
