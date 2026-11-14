# R131 续篇：完整正权分片生产者名称的独立保留

2026-11-13，visible-exact root。

本次修复消费报告中的一个来源名称字段，不改变任何数学包围或传播。
此前显式兼容旧生产者与小批次生产者的 v2 消费程序正确核验了
`kind`、源码 SHA、输入依赖、完整状态及精确连续分区；但局部变量
`name` 随后被输入和依赖的遍历覆盖，导致逐片输出
`complete_parts[].original_producer` 写成最后一个依赖的名称。
原源码 SHA 的核验和保存值一直正确，全部误差传播也不依赖此名称字段。

为保留已有证据，原 v2 源码、首盒报告和恢复 manifest 均保持原字节。
新独立程序为
[scripts/fourfold_codazzi_positive_weight_batched_piece_C0_v3.py](../scripts/fourfold_codazzi_positive_weight_batched_piece_C0_v3.py)。
它把生产者名称保存在专用 `producer_name` 中，报告采用独立 v3 kind，
并将原 v2 源加入依赖。除这三个来源记录变更外，源差异没有改动原合同。
特别是每片仍必须原本 `complete=true`、`failure=null`，且请求区间
等于完整覆盖；不接受中断检查点，不修改原报告，不重置连续误差。

新程序已分别实际消费两个原始完整首盒：旧生产者的4096角网格首盒，
以及小批次生产者的8192角网格首盒。每次均通过原有五个误差管。
与各自原消费结果逐字段比较，完整 `tube_results`、实际腰初值导数、
通过管、最优管、准确区间及完整候选 SHA 全部相同。逐片名称现分别
准确指向旧生产者和小批次生产者，其实际源码 SHA 与保存字段一致。

[完整独立比较记录](../notes/2026-11-13-R131-piece-v3-producer-identity-review.json)
保留两个真实输入/输出身份和完整源差异；两份新原生报告分别为
[旧生产者首盒](../notes/2026-11-13-R131-batched-piece-v3-original-first-C0-native.json.gz)
和[小批次首盒](../notes/2026-11-13-R131-batched-piece-v3-batch-first-C0-native.json.gz)。
以后完整四片的接续使用该 v3 消费程序。此修复不新增径向存在区间、
几何嵌入、闭面或共同度量族结论。
