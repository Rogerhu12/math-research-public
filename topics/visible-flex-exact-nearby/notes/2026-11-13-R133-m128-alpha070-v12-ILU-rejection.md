# α=.70，M128：受限填充 ILU 预条件器拒绝

v12 在原完整850节点输入上实际运行68.03秒后正常返回；有限 BVP 成功旗标为 false。
唯一构造异常是 SuperLU ILU 的 `RuntimeError: Factor is exactly singular`，
发生于 drop tolerance $10^{-5}$、fill factor4、COLAMD 的预条件器分解。
它没有产生第一步 GMRES，也没有新 accepted checkpoint。峰值 RSS459908KiB，
明确 AS 上限1536MiB未触发。SciPy 随后显示的通用“Singular Jacobian”不能据此
变成完整 Jacobian 奇异性结论：被拒的是有丢弃的 ILU 预条件器。

完整850节点三次候选、全部128模式、参数 $\nu$、边界和加倍角网诊断仍原样保存于
`2026-11-13-R133-compact-metric-m128-alpha070-v12-b3-floating.json` 及对应
`candidate.json`、三份 `candidate-partNNN.npz.gz`。
其中三份大 shards 只在本地保留，不重复提交；小 `candidate.json` 保留其 SHA、
维数和片段范围。这个尝试没有任何 accepted Newton 状态，因而全部数组可由已经
入库的完整 v9 输入及 v12 源准确重建。原输入是
`2026-11-13-R133-compact-metric-m128-alpha070-v9-candidate.json`；其实际 SHA、
源身份、850节点、128模、1024角网、振幅 $.70$、band3、drop $10^{-13}$、
chunk8 和原收敛门完整保存在 floating/process 两份小报告中。
过程报告为 `2026-11-13-R133-m128-alpha070-v12-b3-process.json`。
完整有限残差为 $.000124226523472169$，未达到原收敛门。

下一版保留完整 FFT Jacobian 动作、GMRES 后向残差、全部非线性门和容差，
仅将预条件器改为前16个 Fourier 指标的完整低模块，以及高指标的逐模式块，
用准确稀疏 LU 分解这些块。这样避免把很小但必要的分岔参数/边界耦合由 ILU
drop 规则丢掉，同时减少高频带状耦合的填充。该改变只影响迭代算法，
不构成 PDE 或无限频率证明。α=.70 仍是继续增振幅的中间步骤。
