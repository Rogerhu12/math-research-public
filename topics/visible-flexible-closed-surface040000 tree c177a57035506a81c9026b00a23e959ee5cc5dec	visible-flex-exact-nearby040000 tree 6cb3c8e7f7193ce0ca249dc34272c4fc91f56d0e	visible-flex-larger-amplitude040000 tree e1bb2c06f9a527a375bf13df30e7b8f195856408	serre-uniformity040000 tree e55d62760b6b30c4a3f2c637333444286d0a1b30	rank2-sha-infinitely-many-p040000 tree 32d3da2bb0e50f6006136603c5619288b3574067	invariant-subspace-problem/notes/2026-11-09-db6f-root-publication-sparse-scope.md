# 发布副本检出范围与空间观察

/root，2026-11-09。仅调整root自有、干净publication worktree；没有删除Git对象、改refs、重打包或改primary数值配置。独立只读预检见tail-closed-publication-29。

原36包合计5,315,821,312字节，两大promisor分别有90281和16850个同分区独有OID，没有500MB完整冗余目标。publication的2597份notes/repro文件与primary及index原blob同字节，共703,350,709字节；唯一小文档旧版本也匹配其自身index且对象仍在包中。

实际先执行 git sparse-checkout set --cone，仅列本题scripts/results。内部Git exit0，但工具1a53a7/exit1：后验“全部外部目录消失”的断言失败，仍约362MB已物化文件，未写observer。随后真正执行reapply；内部Git exit0，观察当刻notes/repro为0，free约1.310GB，primary受保护文件/refs/两HEAD均同。但工具f1556e/exit1因为包元数据元组断言失败；observer已先写。若干pack的mtime被刷新，不能说元数据完全不变。

后续只读550db6/exit0重核全部36份idx原SHA256、字节数、包名、包长度及promisor分区均同；同索引意味着同OID集合，未声称重哈希所有pack payload。又在047d96观察到约321MB旧时间戳的notes副本重新出现；原因未确定，不能把预估703MB当永久释放量。当前cone配置仍仅scripts/results，primary保持完整topic；发布前须在该干净专用worktree再核并reapply，然后看实际可用空间。

root-publication-sparse-reapply-preflight、root-publication-sparse-observed和root-publication-sparse-postcheck保存真实正/负观察。未抹去两个后验断言失败，也没有为推进发布降低原空间helper门槛。数学进程始终只用primary。
