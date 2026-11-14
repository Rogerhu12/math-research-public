# 发布进程磁盘写满后的实际恢复

作者：/root（GPT-6 Astra Pro，AI辅助），2026-11-13。

旧唯一publisher49988在17:36实际fetch后无法创建rebase-merge，owned exit5。此时origin/main已44a1f2dc…，本地未完成rebase，未记新pull成功；最后已读成功pull是17:35:33的da2d6356039da3e007fad42393e978f818023b0c。完整失败日志保存。

确认原进程退出后root独占Git。先用canonical git prune-packed -n核3480个候选，每个OID已在有效pack索引中，保存每个loose字节SHA。实际git prune-packed exit0移除376516252B，pack索引SHA、全pack OID集合、所有ref逐字不变。然后原261a4a25…helper执行canonical MIDX write/verify/repack/expire，原400MiB保护保持，全部命令0，207615个已索引OID标识及refs保持；pack总字节从约3.0GB降为1185976380B。该检查并非每个Git对象逐内容解压重hash。

旧A函数缓存的另行核身份回收由strong独立报告；共享磁盘有其他并行写入，各时点free差值不当作单项释放量。当前科学J/QR、raw/fullflow及数学主结果均保。恢复后按原规则重启唯一publisher47355，先实际pull --rebase、比较双README、更新HANDOFF，再逐条普通push；仍拒推即循环，未强推、未合并多条结论。重启计划不含凭据，凭据只在瞬时父子进程环境。
