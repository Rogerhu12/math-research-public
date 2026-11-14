# 密度流水线续跑身份门的小差异独审

逐行比较了两份源，实际 diff 只有默认 primitive 节点数和 completed-leaf
续跑检查；没有改动真实场、两层 Fourier 预算或 R72 积分公式。

| 版本 | SHA256 |
|---|---|
| `scripts/fourfold_forward_density_pipeline_419_Q512_attempt.py` | `a977d79a16ea06f0683ffcd304e10234f60e6d005048ebbd7dee3c3be13e384d` |
| `scripts/fourfold_forward_density_pipeline.py` | `97f75109f6636785a7f6718eab46b9c1e51e62ff49261ef974dfa8b45cda240e` |

默认 primitive Q 从 512 改为 1024，并不自动授予误差通过；实际节点球
和准确系数选择费用仍由同一个完整预算计算并强制比较。此前 Q512
attempt 的失败不能因此改称成功，Q1024 的在跑报告需另行验收。

新增续跑路径重建当前同 leg/segment/subspan 的完整
`CompleteReferenceSegment`，逐字比较保存的 reference identity，同时
核对当前 descriptor SHA 和完整真实 density 通过标志。它进一步逐个
复核报告记录的依赖源码 SHA；第一积分的文件哈希、完整 identity 和
准确 density coefficient hash 必须都相同，才解码其系数球。

因此旧路径可能把别的 descriptor 标在既有 leaf 上的缺口已补。
source/domain/两工作带的既有检查继续保留。已有证书可在不同数值建议
参数下复用的前提仍是同一准确函数和已付实际费用；该检查没有把新的
精度建议当作旧结果已达到的事实。

另直接核读了有限压缩 helper：先删除高时间行，随后只在剩余行中删高
角频，两个删除集合不重叠。全部删项按完整有限 Wiener 范数收费，
并与已付无限补集分开；这里只确认这段代数，没有重复真实 Q1024 运行。

本审查是版本差异与入口检查，不替代整腿实际报告、完整输入闭包或
后续真实端点复合。
