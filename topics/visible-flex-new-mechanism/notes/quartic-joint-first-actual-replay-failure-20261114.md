# 首次四次高度与联合任务：数值多面体回放末位差

日期：2026-11-14。状态：完整输入身份已回放，实际原场已评价；**尚未执行四次高度优化或163维联合优化**。这次异常不是求解阴性，不能把它记成新的参数步。

[公开run43633105146](https://github.com/Rogerhu12/math-research-public/actions/runs/43633105146)，source `109cdd7f25927645ea6d33045c037cc920a8bc5f`，lane `quartic_joint_audit`。完整[summary](actions-43633105146-1-quartic_joint_audit/quartic-joint-audit-summary.json)与原始[报告](actions-43633105146-1-quartic_joint_audit/quartic-joint-audit.json)均已保留。全报告360168 B，SHA256 `8d3fdaaaebe8c9ee95403bfc6d04a6fe19a6023fb5053fd40ff5e9be67478989`。

运行145.153817049秒、峰RSS515952 KiB，停在 `original-fixed-T-polytope-numerical-replay`。原source、四份准确输入、原初态、已接受九高度末态、所有非height系数、完整g和共同sampling grid均已按原规则匹配；当前已接受物理态仍为 `f198ba74dcf3644569bf1ed78eecbc48a0f21ec421205d46a6b159cb00ff0f56`。

问题出在将重构数值多面体的全部JSON与原记录逐位相等作为gate。实际矩阵最大差为0，右端最大差为 `3.885780586188048e-16`。原数值多面体SHA为 `fca55130a2c176eb6e882a65f6c26b37c895a130b5d8d04149fb6e5ce4e6cc12`，重构数值SHA为 `57c5e61c5ec96a3a5f861e1cd2b882c53699fff2f5a26237e28de0db28a02c22`。该末位差不修改数学物理身份，但逐位dict检查在进入四次优化前抛出 `ValueError`。

下一修复保持**原先公开的A/b及其数值SHA**作为实际优化约束。源字节、完整物理/度量/参考身份、准确系数、节点和行定义仍须严核；重构数值的末位差只在明确记录的评价容差下作对照，不将新浮点A/b偷偷替换原约束。具体人工检查只覆盖这个新分支的末位接受和实际行改动拒绝，不重复既有全套开发作为前置门。

此处尚未据机器末位差推断唯一硬件/求值顺序原因，也没有宣称连续误差包围。原实算回执和失败日志保持；修复后继续原一次四次+联合设计，盒、目标g、最高步数与所有几何完成阈值保持。
