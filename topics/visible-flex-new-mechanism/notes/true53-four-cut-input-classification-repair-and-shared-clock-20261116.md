# true53 四cut任务：原支持分类修复与同一科学钟延续

日期：2026-11-16。本说明是[原增广任务设计](true53-four-cut-exchange-master-design-20261116.md)在[首输入失败](true53-four-cut-first-input-failure-and-carried-account-20261116.md)后的明确修复，仍是同一个尚未开始求解的9662行问题。没有重新给一份600秒，也没有重跑任何旧finite/旧方向或源ordinary。

## 1. 根因与准确原语义

原 `frame_entry_body_subspace.py` 的 `RationalRowGrid.classify` 用原有理径向节点与 `EntryTailHeight159Subspace` 的准确支撑端点，判定
`left < t < right` 的variable行。原 `frame_entry_tail_height_blocks.py` 的 `_collect` 只将variable行写入primary的active_values/J/groups/tags；支撑外的metric行记为 `outside-soft-aggregated`，进入原外部常值约束和完整网格。其物理159导数按原支撑证明恒零，不是按浮点小量猜零。

原MODEL的 `_original_domain_record` 只序列化这些active行中的metric部分，即5743行。新oracle原先却把所有pool metric IDs都要求在此5743行加5加4梯度表内，故误把按原设计省去的恒零外部行当成丢失梯度。

修复准确复用原子空间与原classify，并要求：

1. 由两个原ordered pool按原顺序读出的**每一可变metric行**，逐项严格等于MODEL的5743个原tag；缺一、额外或乱序都拒绝。
2. 所有原installed rows仍逐gradient SHA对应；5个既付新增与4个新cuts仍完整安装。
3. 原subset硬门保留，只对真正需要梯度的可变行和installed行应用。
4. 支撑外metric ID及准确开区间写入metadata回执；其值仍参与完整e/f扫描和原constant外部预算，不删除约束。
5. de/df、完整双谱扫描、新点梯度、scalar及actual公式均未改变。

`EntryTailHeight159Subspace` 的这次构造仅恢复原坐标/支撑metadata，直接复用原M与basis，不调用geometry或J。根阅读了补丁和原分类来源；没有新增开发测试、compile或旧观察重跑。

## 2. 同600秒的可追溯延续

原失败run43825241350/research133157415075/source5189a1a78eac6215db75bf5c7d851a8913c6db0f已经花费 **36.79963991600005秒**，所有有限problem/JVP/新gradient/scalar/actual计数均0。此次继续前，额外只读其原stdout一次，绑定：

- 原log3741178 B / SHA997e9b9ddaa0ec6ae72f27a94f66895bfe6a1cc51be5850ae204cc4d70566944；
- 原FINAL_CLOCK字面JSON+LF6015 B / SHAa9648db960caa66e4f2562bbd4af2e32c9cd72cb34cdd69a58625fafafd4ffe9；
- 原失败状态、全部计数、无已尝试finite binding，以及累计1695.779430607秒/128值。

当前进程在数值imports前起钟，owner始终使用

$$
T_{\rm same\ task}
=36.79963991600005+T_{\rm current\ process}.
$$

全部有限子问题的elapsed也引用这个owner，不显示一个另起的较短钟。原600秒上限和32finite/3072迭代/6144系统/32双网/128新gradient/64scalar/3实际pair全部不变。

首失败的 `first_jet_input_restores=1` 已消耗计数与事件原样继承。因为当时构造器未返回，已恢复context只有hash而无可读取数组，明确增加一个 **`first_jet_input_restore_repairs=1`** 修复槽；新恢复按这个独立名记账，不把旧计数归零。必要的重建仅为未导出的scalar fields和变分frame系数；U/T/e/f、旧J和旧方向仍只读，不再生成。

总历史账户仍以1658.9797906909998为任务前祖先，再加**含首失败**的同任务elapsed。原36.7996秒不漏、不加两遍。原3.7MB失败log只是来源读取，没有重算其任何科学内容。

## 3. 输入、算法和终止仍按原设计

原MODEL、原U/T/e/f、5752梯度和所有物理/guard/池/bank/reference身份不变；四cuts在首次求解前已加入，首矩阵9662行从未求解。之后每次必须真新增原行，才能解下一有限矩阵。每个matrix binding只尝试一次，旧9658行问题不重解。

完整gain合格后才进入原guard区间/64scalar/最多3实际pair及全部14门。失败、有限task上限或没有新行不构成主课题停止条件。数学原stdout、末partial数组、严格原行来源和无重复ordinary的规则不变。

最终FINAL_CLOCK继续在全部大输出之后采样；只读report继续不导入科学运行时。此修复的全部输入、读失败log、context恢复、失败和输出都进入同600秒。

## 4. 修改源码

以下只改源文本，没有执行科学函数。其余6个新模块仍用原任务源码。

| 文件 | UTF8 B | SHA256 |
|---|---:|---|
| frame_metric_true53_augmented_scope.py | 9312 | 345fe5cab8b5dc8ef28057879b4110a2f063824a3b27c3faf4bf01dcd4e29a0b |
| frame_metric_true53_augmented_core.py | 17140 | 43b56558492724015976b9c21b6c9ac36fc3a02c314aa5fe88d3f9cb3a8a9dea |
| frame_metric_true53_augmented_transfer.py | 15315 | 2e63e473c8e37fe2f5b8ca327efb2e4a194da1a1b8cf055d681cd3e2f8862520 |
| frame_metric_true53_augmented_audit.py | 34218 | 54305ee3e4bebde07bb66ccca1c4657f6bdf888e5477f069f1e5227d9a6474cd |
| frame_metric_true53_augmented_first_jets.py | 64913 | 2067e12bf8cc7e84b52b5a79558a142ee37293293ca4dffb6c66b3c0b2d5988e |

workflow仅将两行科学钟说明改成同任务carry，执行步骤和公开Actions双pull规则不变；新workflow **9093 B / a29f2ffc3e79561e27068c1b58be95d14b1c0384edea09a39080805f0d57a150**。这次改动位于共享`.github/workflows/`，目的是准确记录延续账户；已在本题log说明。

request保留原method_design，同时绑定本修复说明、5个新源码SHA和新workflowSHA。推送该小request触发唯一修复继续run；不使用Actions rerun重启旧源。run/job/source在观察发生后立即登记。

## 5. 当前状态

物理点仍53，原metric辅助η与曲率未改变。这个补丁修复输入清单语义，没有提供新的下降结论。原完整metric、C²连续族、全时嵌入/reach、握持幅度与精化门均未满足。继续实际求解和纸面剩余任务。
