# 互逆 M256 长区间进程的实际 137 退出及完整接续

2026-11-13，visible-exact / root。**状态：实际过程记录；没有有限或无限维存在性结论。**

会话 82459 在 19:04 UTC 的 `write_stdin` 返回中明确显示 shell 的
`Killed` 和进程退出码 137。原过程文件仍是 `complete=false,status=started`，
没有最终 floating 报告。原因没有被确定；不把这个观察改写成内存不足、
方程奇异或求解收敛。尝试读取本次可见环境的 `/sys/fs/cgroup/memory.events`
得到文件不存在，亦不能据此判定实际终止原因。

## 已真实完成的部分

原计算是 M256、角网格2048、$\alpha=.75$、$[0,25/8]$、1379初始节点、
原 `tol=2e-6,max_nodes=2800`、地址空间限额3072 MiB。
完整 checkpoint QR 保留513个状态分量、全部 Fourier 耦合、非线性物理边界行、
均值与 $\nu$ 列。初次完整因子分解结束后，两次独立全 FFT 反代残差分别为
$1.686831\cdot10^{-12}$、$2.929939\cdot10^{-11}$，均小于原 $5\cdot10^{-8}$ 门。

其第一个完整 Newton 步实际被接受，步长为1；
$\nu$ 从 $-.03390114732831421$ 到 $-.03390978822374861$，
affine invariant cost 从 $.00015484304747438406$ 降到
$7.572948695564419\cdot10^{-9}$。
该步没有通过原完整 collocation 收敛门，因此没有授予有限 BVP 成功。
第二轮全因子分解也完成，但在退出前没有第二个已接受状态或最终报告。

唯一完整已接受检查点为

`/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints/2026-11-13-R133-reciprocal-m256-alpha075-checkpointed-QR-floating/accepted-000.npz`，

SHA256 `af0a3f5fabd4d8d1194f30ff942130040e62975c0963f127c9ae864f7bd9521a`，
10916086字节，包含全部1379节点的513状态分量及径向导数。

## 已实际完成的无损重建

新通用脚本 `scripts/fourfold_codazzi_preserve_accepted_checkpoint_v2.py` 消费该检查点，
使用原 SciPy `create_spline` 的全部 Hermite 状态和导数，重建完整
$4\times1378\times513$ 三次系数；没有截掉高频或接口。
重建索引位于

`/workspace/scratch/ac0d699811ad/reciprocal-m256-alpha075-accepted000-candidate.json`，

SHA256 `45923b3675d2789376361192c6e0841e82914e27605d362872d5ac1dcf7a628e`。
这是原已接受状态的接续输入，不是未观察到的最终状态。
完整过程记录为
`notes/2026-11-13-R133-reciprocal-m256-alpha075-accepted000-preservation.json`。

按根 README 第11条，这个可由原程序和参数重建的大中间候选不重复提交二进制；
提交源、准确参数、原日志、原进程记录、检查点和重建结果的哈希。
若本地中间数据丢失，按原 process 文件的 `producer_arguments` 运行原完整生产器，
恢复首个 `accepted-000.npz`，再运行上述无损重建脚本。原输入是已经提交的
完整 M128 $\alpha=.75$ 五 shard 候选；所有环境、依赖哈希和原严格数值门均有记录。
不得把缺失文件改成零状态，亦不得声称这次137退出已经重新完成。

## 当前实际接续

真实帽 $r=3/2$ 的逐模 $q_m$ 已独立支付全部663原闭盒、非零R74尾以及所有高频的
$53/50$ 上界。主体接续使用该向量，并明确保留 $q$ 的逐模近似误差、物理商的全部尾、
非线性帽另一迹及 mean 费用。

当前正在运行的新脚本
`fourfold_codazzi_reciprocal_cap_cut_refine_probe_v2.py` 从上面的完整 M256 已接受状态接到
$[0,3/2]$；新进程会话84317、地址空间限额2048 MiB、原容差仍为 $2\cdot10^{-6}$。
它允许在**一个已通过原完整接受门并保存全部数据的 Newton 步之后**主动写出接续候选。
这种暂停记录 `finite_BVP_success=false`，不把已接受一步当最终收敛。
接续后仍由原完整 collocation、边界和径向 RMS 门决定最终有限成功。

另一个 M128 真切口进程81525独立运行，从原 M128 候选重新支付边界；
它不是原137进程的同一个运行。两个进程的最终结果尚须分别读取，不能提前推断。
