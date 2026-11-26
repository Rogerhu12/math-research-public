# 已返回步骤的完整参数归档与活动待办

类型：执行与来源记录，不是新科学结果。2026-11-26，公开02的29–44与03b的2–13均已真实返回（含失败），root逐个将活动队列的id与公开实际记录核对，无未返回id被移出。

为继续加入完整科学命令并保留原95000字节准入守卫，将这两个已返回队列的完整原始字节作为参数归档保留；没有拆分科学source或单个step，没有丢弃任何argv、summary、scope、来源或失败。活动文件继续同一parent_request_id且finish_when_done=false，仅保留未执行的新步骤。控制器的attempted_ids、完整实际journal、runwork与全部已有产物不变，旧id不会重放。

| 队列 | 完整原字节 | SHA256 | 已返回step数 | 完整参数 |
|---|---|---|---|---|
| 02 | 80236 | `472d101271fcc3c2fd53a1921b67bdfc22e8aa482a84f5f302dba3972cfbbddc` | 16 | [resume-20261126-followups-02-completed-archive-001.json](../computations/resume-20261126-followups-02-completed-archive-001.json) |
| 03b | 94917 | `5a48586c89b2821aa0f6bdba43d051ecdd94e59e7046e485deaaf85f791690ca` | 12 | [resume-20261126-followups-03b-completed-archive-001.json](../computations/resume-20261126-followups-03b-completed-archive-001.json) |

实际来源：[02至44](2026-11-26-public-actions-45800076687-1.md)、[03b至13](2026-11-26-public-actions-45820592817-1-part-003.md)。完整controller源码3cb1的`run`从当前steps过滤持久attempted_ids；移出已经返回的id不取消任何子进程，也不删除其科学结论。原02控制器的同一逻辑亦保留。所有raw数组和工作报告仍只在runner，以上仅是完整可复现参数。

## 2026-11-26 16:43:49 UTC — 03b第二完整参数归档

原活动65711B/SHA3d856854bb1dc8721166bb63b1c88945769c2604f466195e80dc2ef7323ac9d1逐byte保[archive002](../computations/resume-20261126-followups-03b-completed-archive-002.json)，含全旧step对象及archive001指针。仅已实际返14–20移出活动（19仍失败）；21–24全对象不变，后来实际返回由attempted跳过。新加原3d9完整R696纯读取、原606 integral全方向/6d54归因，全部明确参数见[说明](2026-11-26-direct-axisymmetric-integral-norm-full-direction.md)及[完整ledger](../computations/resume-20261126-followups-03b-archive002-ledger.json)。

## 2026-11-26：03b完整archive003

[实际26/27与后继](2026-11-26-actual-integral-SO3-first-direction-26-27.md)登记已返21–29的完整92518B/cabb队列逐字归档（包括28、29真实失败），全部9对象/argv及archive002指针保。完整来源/每条实际状态见computations/resume-20261126-followups-03b-archive003-ledger.json。新655d同范数续方向为全新完整对象，不改旧对象或实际journal。

## 2026-11-26：04完整archive002

[实际48/49](2026-11-26-run04-actual48-49-third-backtracked-SOC-accepted.md)返回后，仅已返46/47两个完整原step及其两条完整公开实际记录保[archive002](../computations/resume-20261126-run04-returned-steps-archive-002.json)，32181B/SHA8a4cd8d580e5be9eae3e1d9f9adc5064716dae3b03457e6358cd9587972bf88c。原活动93272B/86c0bfbf全文header及来源身份均在归档；其余16完整对象不变，48/49仍在活动，新加一个完整789f pair后91220B，全部argv、summary、output及cleanup保留。没有移出未返对象、没有删除地点或raw输入；持久attempted IDs原语义不变。
