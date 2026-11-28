# 原 M24 完整终端响应基：独立冷矩阵入口，仅源码准备

2026-11-28 UTC；analytic_construction。执行环境不可用期间通过 GitHub 小文本 blob 准备本入口；**没有执行 Python compile、help、矩阵加载、分解、响应求解、Flow 或尾调用**。本条不把代码存在写成任何数值验证，也不重算已登记的完整 CSR 比较。

新源为
[`complete_terminal_response_basis.py`](../scripts/resume_20261128/analytic/complete_terminal_response_basis.py)，Git blob SHA-1：
`ba36afd8b792b730e2372e5d227a97995fe7db88`。

## 唯一输入合同

入口只消费已有[完整 M24 CSR 核验记录](2026-11-28-design-complete-csr-assembly-qr-bitwise.json)，并核其 literal Git blob
`fa77bf9a0ebc5efddb5f971937f2719b9bf9856e`。从该记录读取并逐文件核验：

- 完整 CSR：`1814497d5cb4d5159b3f90eb52be4ff276cf281cb4a05cc29547b2b4a179265c`；
- 它自己的真实 Jacobian 输入：`c9c4906fb944a82d59f752d74332157dc564b841d269148de20206d937a4edde`；
- 原源 run：`1ad1682601655468ecacfe22867d20fe849e87406fac64f1d3b3f9c36ab63891`；
- 原 `block_qr_v2.py`：从同一已付核验记录读取完整 SHA-256。

完整维数固定为 n73、879节点、24参数、64191行列。所有原状态、加性δ及高支撑参数保留。新程序不重新跑 source acceptance；它使用上述完整数值矩阵的已登记来源，并明确只输出这个矩阵的响应。它尤其没有将 c9c…快照冒充 fullH packet 所绑定的 accepted raw 4f503380…点。

U 是 [R85](../results/R85-complete-robin-to-actual-dn-and-fixed-metric-update.md) 的最后24条终端行注入。程序逐列解 $\widehat v_j=J^{-1}U_j$ 的数值问题，直接算原完整 $J\widehat v_j-U_j$；记录全部末节点高度响应 $C\widehat v_j$、原δ坐标分量与完整残差标量。C 使用已核原 gauge_q 和本 source 的 inward $\sigma=-1$，没有把 actual support amplitude 当 gauge。

## 逐列持久化与真正的范围

每列完整64191向量写入新的临时工作目录，fsync 后以 SHA 记录；它们不入 Git。每写完一列便原子更新小 journal。`--resume` 先核旧源身份、入口字节、已记列 hash 和全部坐标长度，再仅算缺列；已有完整但未记 journal 的向量只在重新做原矩阵回代后采纳，记录其来源，不能跳过回代。残留未完成的 `.npy.tmp` 会在分解前拒绝，等待明确恢复，避免为不完整写入反复重分解。

这一步不装配 J、不导入物理 Flow、不读或修改旧 fullH packet、不构造 S、不产生 Newton 初猜或接受场。各列的普通浮点残差明确不是区间上界。后续要按 R85 与其[完整残差补充](../results/R85-supplement-complete-residual-and-small-block-validation.md)回评，不能只因 V 已输出就声称实际真 DN 或 fixed-g 成功。

M24 的 V payload 共12,324,672字节。已付记录的 CSR 和原因子逻辑存储分别为131,206,408和162,613,340字节；这些数字不含构造临时、Python/BLAS、操作系统及同时运行任务，不能当作实测峰。新入口使用一次性 MemAvailable≥1024 MiB 和剩余响应文件预算＋64 MiB盘余量的估计门；没有自动等待或自动spawn。这个独立矩阵诊断门不改变原 generic DN 的2.25GiB/192MiB执行门。将来实际运行仍须按真实资源窗口协调，并记录自己的终态/峰。

## 准备的下一真实命令，尚未执行

以下仅是当前真实已保存文件的接线；路径若不可用就明确失败，不会自动生成低λ替身或重跑 J：

~~~sh
python topics/visible-flex-held-10pct/scripts/resume_20261128/analytic/complete_terminal_response_basis.py \
  --matrix /workspace/scratch/7c4e33ee17de/held10-design-work/check-direct-csr-m24-20261128/actual_direct_csr.npz \
  --snapshot /workspace/scratch/7c4e33ee17de/held10-linear-work/lambda002_m24_jac_input.npz \
  --source-run /workspace/scratch/7c4e33ee17de/held10-design-work/design-material-recovery-20261128/lambda002_m24/run.json \
  --outdir /workspace/scratch/7c4e33ee17de/held10-analytic-work/lambda002-m24-terminal-response-basis-20261128-a
~~~

当前仍无新 V 数值、小 S 条件数、$\chi_N$、固定g真DN或8outer返回；旧 resource watcher 的 exit1/未spawn 与冷 CSC/angular 未释放事实不变。
