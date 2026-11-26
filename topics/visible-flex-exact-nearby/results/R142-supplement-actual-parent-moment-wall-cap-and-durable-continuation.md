# R142 actual：母格矩运行的真实预算终止与缺失完整 defect

会话：visible-exact-astra-198c63d-20261126。记录时间：2026-11-26 10:22:38 UTC。

## 1. 实际结果及其范围

[run45761859526/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45761859526) 已在 2026-11-26T10:09:58.393211+00:00 结束。child returncode=1，实际数学时长 16808.05140786 秒，原固定科学预算16800秒；worker未触发自身20100秒强杀，child_timeout=false。实际异常是 `fixed complete certificate wall cap; prefix retained`。

完整原件中的明确状态为：

~~~json
{
  "complete": false,
  "proved": false,
  "completed_targets": [],
  "current_target": "complete_parent_moment_true_hybrid_low_coefficient_defect",
  "defect": null,
  "sources": {},
  "strict_low_coefficient_gate_passed": null,
  "whole_interval_transversality": null
}
~~~

**本次没有保存完整 defect 六球，也没有 epsilon 门的true/false结论。** 不能把任务failure当作BVP奇异或充分界false；不能只看completed_targets来漏读全球。本次已整读certificate，确认defect确实为null，故适用无完整球的PS后继。

- [完整 scientific](../notes/low193_parent_moment_ci/run-45761859526-1/actual-scientific-conclusion.json)：56589 B，Git blob `0b2e8385af4ac842496b6403a580660c1cb2459e`，SHA256 `61bcbb6d98da372a2c073f0a0d58f0faafc86c3c8acd72303f2a948ad6cc44a1`。
- [完整 execution](../notes/low193_parent_moment_ci/run-45761859526-1/execution.json)：61663 B，Git blob `f5e356aaa8f10f02e2e4fa2cc720f69bb0ccb7d6`，SHA256 `734210f68e7d5138202050d18d0714250b1f16c6e255dcd1749dcbf7aa1fbb43`。
- 原 manifest SHA256 `50e5bbf2e55ee6fa7c24cd074cb2a7bd691101c3167004b840011710ac963b7e`；原事件提交 `b068d45008c3e58964bef3be9857b026d5a63be9`，实际science checkout `dba767eeee618d70f394831cc2e8cd21aa2a6885`。

原失败文件和source/parameter身份保持不变；本篇不改其complete、proved、failure或目标计数。

## 2. 已完成的准备及未保存的积分

77个当前输入、21个历史输入和完整原WVC/Green/mean-floor资格均已通过准入。原155 comparison panels细分为1424格、原5696个integration boxes及193全部输出原子不变；原comparison model chain为

~~~text
33fdf6eeba4d5904c961b2bedea43c5207d80fb66920017168f41f9106cc4d79
~~~

完整输出记录有153个原centre parent、4650行、4801交、1425 chart节点及1424双向carrier。当前defect source包计数为1424；四个其他source包计数0，point盒计数0。异常发生在 `complete_norms_with_shared_outputs` 的body/root97/outer96汇总流；原source第616–619行先完成shared A/B/K，再进入这个汇总流。公开作业日志也保留该阶段及原完整traceback。

这些计数和临时对象hash**不包含**可直接消费的全母格三积分前缀或完整六球。原private matrices没有被发布或恢复；不能从计数、日志checksum或只在进程内存在的sums虚构一个非空积分前缀。已经成立的旧Green和原comparison BVP成功仍保持原scope，不需要重新登记其数值目标。

## 3. 整件核验

root逐件读取scientific/execution，并核：

- 全scientific字段与原manifest一致；77个完整当前receipt、全部scientific module binding和参数逐项一致。
- 21件恢复对象的完整canonical bytes=15033、SHA256 `8213b004a48508c580440cb7a38239d796c7afc9eece83bbd3f5a02e5b2d7ed4` 与scientific整件引用一致；原WVC恢复子对象的完整hash也一致。
- 与已成Green actual的reference identity、完整model、1424细分count列表逐项相等，没有窄化原parent coefficient balls。
- execution准确绑定本次56589B scientific；21个已通过gate恰是原完整有序gate表的前缀；没有隐去未过门。
- 13次真实pull/README检查，记录的差异为空；完整链SHA256 `fb23f5ac6dfcd54c9d70eb76cc0de4c3affa50c89b0f791fe77d3aca563fdfda`。旧科学target、old producer/QR/SVD、数组/artifact/Release新发布次数均为0。

这些是本次真实计算的准入和终止证据，不是新的低逆证书。

## 4. 已实施后继规则

下一项是已经全审并保存的 [PS完整母格三积分接续](R142-supplement-durable-complete-parent-source-moment-prefixes.md) 与 [执行入口](../notes/2026-11-26-R142-streamed-defect-execution.md)。本次真实actual/execution/原manifest构成其首次合法输入。PS按每个完整source parent分别保存body/root97/outer96三个累计平方球，整件保存和contains读回通过后才推进游标；输出变量始终覆盖整个径向及193原子，两个same-cell有符号三角不删。

必要的同定义comparison表示和A/B/K/J可重物化；旧完整成功的数值结论不再作为新目标重算。此首次接续没有已保存的source积分，因此不伪造非空prefix。以后每个已经保存的完整source parent禁止重新积分；若全155个三积分已保存，则只由原球读回完成平方根，不再重物化Green。

实际完整六球一旦产生，必须立即消费：epsilon门true后接缺失的四源/whole point，完整false后走严格保原失败范围的R149 signed/coercive分支。两种情形都不得重新积分已有全球。本题的正侧58/224/32、negative incoming、完整Schur、精确非线性闭族及几何匹配仍保持原open的全部义务。
