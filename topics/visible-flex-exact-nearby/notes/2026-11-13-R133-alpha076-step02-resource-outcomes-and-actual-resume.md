# R133：.76第二步的两次原过程结局与真正续算

**过程事实，不是数学证书。** 同一672节点、M256、2048角、全ν列及完整物理边界的step02，原所有数学方程和门保持不变。

## 已知ENOSPC的原80604

原v5完整671块分解用213.19秒，第一完整右端的原相对残差为2.4690315138973143e−11。随后在建立第二右端目录时得到真实OSError `[Errno 28] No space left on device`，进程正常报告异常后exit71。原report中的complete仅表示过程结局已记录，certified=false、没有accepted、没有最终finite输出；不能把它改成成功或与137混同。原resource report和精确原log压缩件分别是同prefix step02-process.json及step02-original-exit71.log.gz。

实际清理前核完整step01的候选SHA及保存结果，仅删除自己已完成、可由原输入重新计算的临时QR case9bd7786...，释放106699278字节。其完整候选、原accepted数组、输入及正在用的step02 case e61134c...均保留。随后使用Git支持的MIDX write/verify/expire/verify四命令，全部exit0且refs不变，但没有pack过期；不能把全局磁盘随后恢复的空间归因于这项操作。两份完整过程记录随本文保存。

## 实际137的恢复98052

恢复读取同一完整factor e61134c251b7912d84a69beae4cb6ed69bc67fd63ebe8a5b0e867401338a124e，第一右端从complete状态重读后再次独立检验原完整残差2.4690315138973143e−11，用时.9267秒。第二右端前向到128块后该真实session返回exit137，原报告仍started/complete=false，原因未知。原report、原log及独立观察记录保留；没有凭退出码宣称OOM、奇异或数学门失败。

新的76282采用独立resume2报告和日志、相同原输入/源/全门；实际重读完整factor、重检第一右端残差，并从第二右端forward next_index128继续。这证明实际大规模恢复已经消费了保存进度，并不表示第二步已接受或有限问题已收敛。当前过程继续，结局须以其新的原报告另记。

所有大临时因素仍在scratch，原Newton门、tol2e−6及完整线性5e−8门未放宽。只运行一项大型主体求解；每个真正接受状态都完整保存后立即进入下一步。
