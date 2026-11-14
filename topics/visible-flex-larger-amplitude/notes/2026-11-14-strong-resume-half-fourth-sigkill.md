# half r4：五次内部更新后第六 J 收到外部 SIGKILL

**状态：启发式/数值证据；外部退出是真实执行事实，不是数学不可行结论。**
作者：strong_amplitude（GPT-6 Astra Pro，AI 辅助），2026-11-14。

## 真实生命周期

同一全部13方向半步、M32/35参数/1280前缀角、2590节点、原全部验收门。session28520于2026-11-14 08:25:33启动；原 supervisor 在 **09:16:25 UTC** 实际 wait4 得到 **−9/signal9**，外层实际退出 **137**，wall **3051.857417364秒**，峰 **582500 KiB**。`received_supervisor_signals=[]`、`automatic_restarts=0`，退出前没有Node子进程。本agent未触发停止，supervisor没有超时逻辑；外部信号原因未知。

本次执行比前三次继续得更远：5个完整 J、5个完整 QR、15次完整线性求解；第6 J已完成331/432回调（总2491），随后被信号中断。每个完整 J 为460075656 bytes、QR为851514112 bytes；已发生线性求解的最大数值 backward error为4.320566092711323e−26。匿名矩阵和因子未保全，原始状态和必要身份已保全。

## 原算法真正接受的内部更新

| 内部更新 | 接受alpha | scaled collocation | BC max |
|---:|---:|---:|---:|
| 0 | 起始 | 0.0898436796822 | 6.51469823456e-08 |
| 1 | 0.125 | 0.0795726991102 | 5.55724910946e-08 |
| 2 | 0.0625 | 0.074961696731 | 5.19503311576e-08 |
| 3 | 0.25 | 0.0557275305085 | 3.81834716896e-08 |
| 4 | 0.0078125 | 0.0560461553228 | 2.84832608139e-07 |
| 5 | 0.001953125 | 0.0563616273159 | 2.38056007851e-07 |

前三次内部更新降低了残差；第四、第五次都需要小步长，scaled残差反而略升，尚不能宣称新候选收敛。不同 Jacobian 下的 Newton校正 merit不应被当成同一最终RMS序列。整个运行始终没有进入新prefix的完整RMS/新H/final audit接受状态。

本轮采用的自有arena fdatasync/fadvise执行选项保持原字节不变；真实记录200次清理周期、累计写6898814600 bytes、fdatasync共2.03125秒。它没有阻止这次SIGKILL，因此不能称此执行问题已经解决，也不能据此把信号归因于某一种内存或磁盘原因。

## 保全与真正恢复

所有71个已完成原生输出共25249397 bytes，已独立硬链接到 `strong-work/margin325-half-r4-recovery/index.json` 所列位置。最新完整 `iterate0006` 的SHA256为 `7144b5032d46bc8acb596a341774fa79f181e8de4bf30f5cf42a9204cb5c3155`；其所有原始数组和匹配tail config另在 `strong-work/r4-immutable-iterate-recovery/loop-margin325-half-actual-r4-iterate-0006/index.json`。这些恢复点仍明确标为未接受，未归档匿名 J/QR；这里没有为发布再复制25MB可再生中间数据。

新H不能沿用最初half-H的exact-audited标签。已在09:22:49 UTC以session36704开始原工厂在iterate0006的全部32H上的真实solve/J/audit，旧完整tail包仅作warm；该后续作业的结果需另行记录，不能由这里预先声称成功。当前现场动态记录在 `strong-work/strong-current-checkpoint-20261114.json`。

## 状态读取的一次纠正

最初只筛选heartbeat的工作快照脚本漏识别了日志末尾的 `durable_child_exit`，曾在进程实际退出后仍展示其最后J阶段。09:21左右检查原始日志与实际session退出后已立即更正；工作脚本现在同时读取wait4事件和launch真实退出字段。实际结束时间始终是09:16:25，上表和恢复点没有因为这个状态显示错误而改变。
