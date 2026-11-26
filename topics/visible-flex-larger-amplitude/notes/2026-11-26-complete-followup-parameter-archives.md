# 已返回步骤的完整参数归档与活动待办

类型：执行与来源记录，不是新科学结果。2026-11-26，公开02的29–44与03b的2–13均已真实返回（含失败），root逐个将活动队列的id与公开实际记录核对，无未返回id被移出。

为继续加入完整科学命令并保留原95000字节准入守卫，将这两个已返回队列的完整原始字节作为参数归档保留；没有拆分科学source或单个step，没有丢弃任何argv、summary、scope、来源或失败。活动文件继续同一parent_request_id且finish_when_done=false，仅保留未执行的新步骤。控制器的attempted_ids、完整实际journal、runwork与全部已有产物不变，旧id不会重放。

| 队列 | 完整原字节 | SHA256 | 已返回step数 | 完整参数 |
|---|---|---|---|---|
| 02 | 80236 | `472d101271fcc3c2fd53a1921b67bdfc22e8aa482a84f5f302dba3972cfbbddc` | 16 | [resume-20261126-followups-02-completed-archive-001.json](../computations/resume-20261126-followups-02-completed-archive-001.json) |
| 03b | 94917 | `5a48586c89b2821aa0f6bdba43d051ecdd94e59e7046e485deaaf85f791690ca` | 12 | [resume-20261126-followups-03b-completed-archive-001.json](../computations/resume-20261126-followups-03b-completed-archive-001.json) |

实际来源：[02至44](2026-11-26-public-actions-45800076687-1.md)、[03b至13](2026-11-26-public-actions-45820592817-1-part-003.md)。完整controller源码3cb1的`run`从当前steps过滤持久attempted_ids；移出已经返回的id不取消任何子进程，也不删除其科学结论。原02控制器的同一逻辑亦保留。所有raw数组和工作报告仍只在runner，以上仅是完整可复现参数。
