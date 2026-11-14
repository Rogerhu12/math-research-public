# α=.70 M128：完整低模块预条件器的两次真实 GMRES 拒绝

两次都使用原完整850节点 v9 输入，保留完整有限 FFT Jacobian 动作、参数列、
GMRES 后向残差门、全部非线性守门和原容差。预条件器准确保留前16个 Fourier
指标的完整块；更高指标分别采用 band0 与 band1。两次 LU 都完成，随后完整
GMRES 用满原12个 restart、768次内迭代而未过后向残差门。

| 项目 | core16 / band0 | core16 / band1 |
| --- | ---: | ---: |
| 稀疏预条件器非零数 | 2,518,096 | 4,039,502 |
| 实际 LU 非零数 | 3,482,387 | 49,895,130 |
| 构造时间（秒） | 21.1716 | 68.2998 |
| 完整 GMRES 相对残差 | 1.0019504382223456 | .8957101785032223 |
| GMRES info / 内迭代 | 12 / 768 | 12 / 768 |
| 完整作业时间（秒） | 280.7301 | 577.0138 |
| 峰值 RSS（KiB） | 369524 | 854984 |
| 新 accepted checkpoint | 0 | 0 |

两份原报告的 finite success 都为 false，进程正常 exit0。SciPy 随后的通用
“Singular Jacobian”消息仍不证明完整 Jacobian 奇异：本次明确是完整线性
GMRES 残差不合格，因而没有允许 Newton 采用这个方向。

最小实际记录为两组 `...v13-core16-floating.json`、
`...v13-core16-process.json` 与 `...v13-core16-b1-floating.json`、
`...v13-core16-b1-process.json`。小 candidate 索引保存所有完整重建块的 SHA。
本次零 accepted 状态，重复大数组仅在本地保留，可由已入库的 v9 全输入、
已保存静态源和各过程报告中的参数准确重建，不重复推送这些 shards。

后续不再继续同类稀疏 LU/GMRES 参数试探。root 已用保留全部相邻双块和参数列的
正交消元完成实际 α=.70 M128 求解；这两次失败只记录该已排除的预条件方向。
