# 每次 inner 返回后的未解 outer 快照

会话：Astra-visible-flex-78718bd0；作者：`/root/numerical_recovery`；2026-11-10。

## 实际改动

`scripts/78718-run-prefix-mode.py` 在原 `selected_solver` 返回后、原外循环发送下一次真 DN 前，调用新 `scripts/78718-prefix-inner-snapshot.py`。不改当前已经启动的 M15 程序。快照失败只记录其异常；原返回对象和原外循环继续原路径。

每次调用生成独立 `_inner_0001`、`_inner_0002` 等名称：

- `<stem>_inner_0001-collocation.json.gz` 与其 PP 分片：真正返回的未加权状态 cubic，独立变量是数值坐标 `t`；原 `x`、`p` 和 PPoly 系数不舍入。
- `<stem>_inner_0001-nodes-*.npy.gz`：原返回节点值，避免从最后一个 cubic 端点重新求值产生舍入。
- `<stem>_inner_0001.json.gz` 与其 PP 分片：以 `obj.chart(x,p[0])` 得到物理坐标 `s`，用与原最终出口相同的 `c2_interpolant` 公式生成 quintic。它是用于后端的具体 Hermite 图，不冒称为 cubic 的精确非线性重参数化。

物理 quintic 用新的、同参数 Flow 和新的 bridge 计算。只在固定 `g` 路径读取原 chart；不调用活跃对象的 `initial`、BC、tail、RHS 或 Jacobian，不修改它的初值缓存或计算次数。新增 Flow 的 RHS 次数单独记录。前一个实际真尾包只作为来源/后续 warm 信息，不当作新候选的已匹配 seam。

所有快照永久写 `status=UNSOLVED_OUTER_INNER_CANDIDATE`、`solver_success=false`、`finite_coupled_success=false`、`outer_true_boundary_checked=false`；真正 inner 的 success、状态、物理残差和谱加权记录另列。没有 `tail_seam`。这些文件允许立即研究入口与全前缀误差，也允许显式另给真尾 warm 后再重启；它们不通过成功后端计划器的入口。

PP 使用原无损 gzip 分片，节点也按每片不超过约 4.4 MB 原始字节分片，所有实际文件须小于 5 MB。`-mode-run.json` 和 JSONL 进度保留闭存文件路径、大小、SHA 与快照耗时。文件均为可重生中间件，是否提交按根 README 第 11 条处理。

## 实际有限检查

`78718-prefix-inner-snapshot-check.py` 从已有 M15 warm 取 64 个径向节点建立**明确标记为合成存储夹具**的 cubic。它没有跑 BVP、DN 或积分，也没有假造实际 inner 的正例。返回的标记 residual=1 只是夹具字段，不是数值研究结论。

实际工具 `3cf23f` 自然 exit 0，0.637 秒，11 项全部通过：cubic、原节点、物理 quintic 的字节保存；物理/数值网格与参数；普通 geometry source 对物理 PP 的无损消费；活跃夹具对象的 Flow/初值缓存/参数尺度/调用次数完全未变；未声明成功、未声明 seam；每件文件小于 5 MB。小报告为 `2026-11-10-78718-numerical-inner-snapshot-check-02.json`，SHA `7b487b231663595ad0ecf790770b316c30f24961d0d51e54232550d88f3b67bd`。

第一次夹具检查 `445854` 自然 exit 1：只读 geometry loader 不像生产 runner 那样补 `port['_sha256']`。只修改夹具以匹配已有生产对象；helper 没有用缺 SHA 的 fallback 掩盖问题。首次已经闭存的局部文件保留在 scratch，第二次使用新目录。

真实回执和完整命令见 `2026-11-10-78718-numerical-inner-snapshot-and-fft-observed.json`。夹具数据只留 scratch；提交源码和小报告即可。这些检查是实现验证，不是新增研究验收门。

## 可立即消费的命令

新物理快照可直接交 `78718-geometry-inlet-angular-bound-v1.py --checkpoint <stem>_inner_0001.json.gz --out <另名报告>`，报告会继续携带 `solver_success=false`。需要具体 Cartesian 图时，可用原 prefix producer 的 checkpoint 参数读取物理快照，随后交 `78718-geometry-base-inlet-angular-bound-v1.py`；其数学结论只属于该明确的未解候选图。

当前旧主 61908 的第一个 inner 在本功能实现前已返回，且没有可读快照；本改动不附着或修改该进程，也不声称恢复它的内存结果。
