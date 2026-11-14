# 当前domain拒绝的可见信息与下一入口的最小诊断

当前physical-merit-r4/session98541保持原运行源不动。第二次真实Newton方向在α=1、1/2、1/4、1/8、1/16时被原定义域捕获拒绝，α=1/32实际接受。原owned Newton仅捕获FloatingPointError并记录outside-domain，没有保存异常repr，因此现有日志不能确定具体触发项。不能据此称某个标量控制触边、core失凸、实际reach失败、分支折点或不存在。

只读源码显示的候选检查为：

- augmented.flow检查0.002<δ<1、LB>0、vu<vp<1。
- 实际frame检查Fθ长度、其法向二阶分量长度，以及margin=1−(a′/(a κ))²严格为正；材料角图也有可逆性检查。
- 边界入口另检查actual c2的搜索区间、完整支撑core凸性数值下界与弧长反演。
- 原evaluate先求完整collocation残差，再求BC；没有异常来源和失败块数据时，不能根据一次reject的表面时间推断发生位置。

这些是源码中的检查范围，不是本轮已经定位的失败原因。此项没有加载Flow、复算RHS或任何新Jac/Node/BVP。

下一次fresh入口的最小改动应仅增加观测：保留原FloatingPointError捕获和原continue，在outside-domain事件里附repr；在独立径向小块调用失败时记录该块的完整s、y、p输入及dtype/shape/hash、物理profile和参考/chart来源身份，再原样重抛同一异常。只记最先失败的小块，避免另起全网格审计或大临时包。不得用日志改写接受结果，不修改原线性系统、Armijo、最终RMS/BC或真实尾部门。若采用新的独立入口，应记录明确源码变换和新SHA；本活动运行不热改。

下面记录本次只读来源SHA，供之后核对实际执行路径，而非新增数学结论。

- `computations/root_domain_newton.py`：`fd0f63fed7d74115c6e482bf47560230409ce2c20880aaa91e4e4ea1fbda0c83`。

- `computations/strong_actual_augmented_core.py`：`74c64ab558953c6d0378948dd4affb5d354d1faaecab7922b83cfdf76041bad7`。

- `computations/geometric-fixed-dual-prefix.py`：`f189c8f94880ff5455a140a686219a1805399e1d45a3809e176630bb92772280`。

- `/workspace/scratch/c0de65fac774/visible-flex-source/topics/visible-flexible-closed-surface/scripts/950f-prefix-adaptive-chart-bvp-v2.py`：`958a9e2e428f8d64dfc786bed515bad77a208433fa16af7cbbe6f03b1bcc7ebe`。

- `/workspace/scratch/c0de65fac774/visible-flex-source/topics/visible-flexible-closed-surface/notes/fixed_metric_mode3_core.py`：`a529904e265ddc95635c6c6601ea173eb0e1383a75e458d3eaee024fe7078ead`。
