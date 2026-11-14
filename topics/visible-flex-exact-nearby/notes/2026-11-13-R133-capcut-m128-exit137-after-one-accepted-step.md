# 真帽切口 M128：一个完整接受步后实际退出137

2026-11-13，visible-exact / root。**状态：实际数值过程及无损保全；未证明有限收敛。**

原会话81525从完整新互逆 M128 $\alpha=.75$ 候选接到真实 $r=3/2$ 切口，
使用已保存的实际逐模 $q_m$ 浮点向量；原门仍为 `tol=2e-6`、
`bc_tol=tol/100`、完整独立线性反代门 $5\cdot10^{-8}$，最多2400节点。
地址空间限额2048 MiB。首网格1343节点的完整 checkpoint QR 和全耦合线性解实际完成，
独立全相对残差 $2.0121549579511132\cdot10^{-13}$。

第一个完整 Newton 步以步长1接受，且这次试值确实通过原完整 collocation/边界门：
最大 collocation 残差 $1.1011428314305904\cdot10^{-16}$，
最大有限边界残差 $3.3306690738754696\cdot10^{-16}$。
准确候选参数是保存浮点值 $\nu=-.03390114729979629$ 所代表的 dyadic 数。

但原连续径向估计随后要求细化到1854节点。下一轮完整 QR 只在原日志中保存到
896/1853块；19:11 UTC 的工具返回明确显示 `Killed`、退出码137。
没有最终 floating 报告，原 process 仍为 `complete=false,status=started`。
因此不能从首网格 collocation 门已过推断整个有限 BVP 成功。
终止原因未知，不称为内存不足、方程奇异或已确认的容差拒绝。

唯一完整已接受检查点
`accepted-000.npz` 位于原 process 所用的 checkpoint 目录，SHA256 为
`e8abd66e63c6aba8f6174461cde62837c03e5903dce259370c670f8fd670514b`，
5319103字节。已用原 Hermite 插值无损转成全部 $4\times1342\times257$ 系数，
索引位于
`/workspace/scratch/ac0d699811ad/reciprocal-capcut-m128-alpha075-accepted000-candidate.json`，
SHA256 为 `ef57dce9a2cd2d478baa52ce7f4ba9b409555b581c46ad5a09788de1968bd223`。

原 process、原完整部分日志、v2保全源和本次 preservation JSON 一起保留。
按根规则11不重复提交这个可重建的大中间二进制。若本地文件丢失，按原 process
全部 `producer_arguments` 恢复首个完整已接受步，再用已提交的
`fourfold_codazzi_preserve_accepted_checkpoint_v2.py` 重建；不得推断未观察到的1854节点结果。

当前继续的是更高角分辨率的 M256 真切口进程84317，从另一份已保全的完整 M256 状态开始，
每个完整接受步后保存接续结果。现在只保留一个大型求解进程。
同时对本地 Git 设置可恢复的单线程/64MiB窗口和缓存资源界，
记录见 `notes/2026-11-13-git-pack-allocation-settings.json`。
这些工程措施不证明两次137的原因，也不改变任何数学方程、输入或验收门。
