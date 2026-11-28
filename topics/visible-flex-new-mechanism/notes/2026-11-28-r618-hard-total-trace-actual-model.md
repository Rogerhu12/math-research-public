# R618：从实际接受态接入的总核心 trace 模型

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。
**状态：已实现上述仿射表示的完整源码；尚未在 Actions 执行本新范围。**
这里的数学表示见同日 `r618-hard-total-trace-and-convex-core-path` 笔记。
当前 centered run46117718197/job140895158286/source19de4da31f4f6139a2547f2ada7949271a492a00
仍按原声明运行；不读取活动日志，不改变其输入，不预定新的大幅度核心。

## 真实函数，而非报告中的核心标签

`r618_hard_total_trace_model_20261128.py` 定义独立 `HardTotalTraceHeight`。
它拥有原 `FourierCenteredHeight`，但不冒充原类或修改原源码、实例方法、目标身份。
新模型的目标仍是同一个被冻结的 $E_*$。
旧 1129、额外 compact224、真实全平 tail96 共1449自由列全部保留。
原23个独立核心 lift 与 tau 按总 trace 约束消元；没有删位置行或小奇异方向。

给真实 tau1 接受响应 $z_*$，令 $x_*=z_*[0:1449]$，
$P_*=P_0[z_*]$。源码实际使用

$$
f_{P,x}=f[z_*]+L(x-x_*)
+A\{P-P_*-B_0(x-x_*)\}
+B\{\mathcal T(P)-\mathcal T(P_*)-B_1(x-x_*)\}.
$$

在首输入 $x=x_*,P=P_*$ 时，六 jets 直接返回原 source 的同一六 jets，
不通过大数相减再加回来制造“近似相同”的首态。
指定总 $P$ 同时覆盖全部24个模式，包含原模型没有独立 lift 的 j2。
核心径向目标始终用全部48个从属模式至96，不按输出网格截短。

固定 $P$ 的每一自由列均为 $L-A B_0-B B_1$，空间六 jets 完整。
完整1449列 Jacobian 继续经过同一隐式均值链和全部位置投影行。
外部 $P$ 方向另有 $A\dot P+B D\mathcal T(P)\dot P$；同根的 $\dot e$、
$\dot e_r$、全部从属模式、均值和位置方向均已实现，未把这个方向误作零。

## 三个实际消费者中的必要差别

1. **均值与积分**：1449自由参数全零一般不是冻结参考场。
   所有均值查询、位置额外查询、完整 cap 锚定积分都明确禁用旧 tau0 的零响应捷径。
   积分始终需要真实 tail anchor，并保存其尚未解决的 source/ODE 等误差。
2. **系数场**：原 pre-tanh 参考项与全部新 post-tanh 项在同一系数数组组合，
   包括 $A$ 的全部24模和 $B$ 的完整48模，随后才做后续范数消费者。
3. **真尾**：新模型在整个 cap-to-mouth 区间与一个显式原模型响应具有相同六 jets，
   因为这整个区间上 $A,B$ 及其空间导数准确为零。
   原 producer 对那个原模型计算。新 consumer 保存它的完整原身份/receipt，
   再用该支持恒等式推导新模型的 anchor，清楚说明区间以外两个场通常不同。
   原 source contract 必须针对这个原 producer 模型，不能直接换成新模型 hash。
   它的未付误差和条件结论原样保留，不由支持恒等式升级。

新 `r618_hard_total_trace_consumers_20261128.py` 的 direct readout
始终调用真实新模型的六 jets 和同一均值链，在原全部fine点及两套完整额外径向模板上重建位置。
尚未实际运行，不能声称得到了完整 direct 数值结果。

## 接入 current centered 的自然终态

`r618_hard_total_trace_from_centered_terminal_20261128.py`
只接受上述实际 run/job/source 的自然终态与 literal FINAL，
提取 `actual_response`，不取 `pending_trial_not_accepted`。
它从同一实际接受态求总 $P_*$，首输入不改变外部 $P$ 或 $\mu$。
原接受步、下一 damping、全部终态费用及未完成读数保留。
真实 source 的已付接受态不需另跑“资格确认”门；在新参数化中需要未存数组时仍如实计费。

本轮本地仅进行源码/AST、字段及调用链检查，没有运行科学数值。
尚未创建新计算请求或选择宏观 $\mu$；要先消费正在运行的真实 centered 终态，
再依据具体坐标限制 attainer、完整根进展及几何余量选择下一输入。
这套实现不证明连接段存在，也不证明任何完整闭面满足 README。
