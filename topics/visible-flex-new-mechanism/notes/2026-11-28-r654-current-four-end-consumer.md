# R654 的当前四控制全导数接口

2026-11-28。输入为 R651 真正给出的正时长参数、准确有理 $C^3$ 接边宽度以及原固定归一粗网。资料在 [R654](../results/R654-released-rest-shapes-moving-time-four-end-implicit-chart.md)。目前尚未沿该源取得一次真实完整 ruling 接受，此接口不把候选时长或源 fine 当作新资格。

- `scripts/r654_released_rest_physical_base.py` 按真实先后次序从 R651 有理参数构造运动段、四个可变时段及实际往返。若有额外往返，固定停留在往、返之间，所选静止点的可变时长接在返回之后。按准确有理局部多项式实现接边升阶；各移动段的导数以 16 个子块上的精确 Bernstein 凸包给上界。原 h/k/η/γ/υ 资格用 R654 (7)、全部 256 个实际系数及真实时长计算。不足的充分界保为未闭记录。
- `scripts/r654_released_rest_four_end_chart.py` 的 `ReleasedChart.joint` 在原固定 $x$ 的 Gauss/读出点上取 $t=(Lx-S_j)/D_j$ 为实际 Jet。对 $h_{ss},k_{ss}$ 保留 $B'''_j\dot t$ 与 $-2B''_j\dot D_j/D_j^3$。原 $\eta$ 和八 A 均用同一网的 $Lk_s/(2h)$ 和 $LM$ 前缀积分，奇端扣除全部末积分。这是 R654 的固定 $x$ 公式：材料上限与宽度移动的作用已在 $t,L,C_s$ 中，不能另外重复加入一次材料导数。
- `solve_controls` 的每个 Newton 步均重新计算当前四时长列；接受用当前四行、正时长和实际 $\Delta\tau$ 的 Armijo。有限网四端达到容差时，在同一曲线计算 256+4 列，解实际 $E_\tau D_q\tau=-E_q$，再将所有几何、加速度、八 A、四个真实端读出和 $L$ 合成回 256 列。源静止矩阵 V 没有进入任何当前 Newton 或隐式导数计算。未闭范围及每一回溯保留，不能计为原问题无解。

所得 curve 可直接给原 `CountedInterruptedFullHistory.evaluate` 和 `project_true_ruling`，以原十八块、完整正势、六 $\rho$、实际中心势差及全程常 gauge 求同一物理读出。这里仍输出四个真实端的完整导数和原四偶归一组合。原固定 $x$ 的工作/精化网、完整 ruling 和 HS/feedback/end 绝对门均可沿用；旧多项式专名的物理资格标志改由这里的真实全场连续界提供。最终资格还需同一 $q$、四时长、接边宽度、A 中心、三 gauge 的固定 fine，并以原 history 门检查。该 fine 使用 `joint(..., mode="fixed",fixed_center=...)`，不能调用 `solve_controls` 重解另一条曲线。

正式连续 R654 根还要对**新接边过渡**的 $b_\epsilon$、严格正时长与原盒作同一对象的连续资格；本接口的浮点根本身只陈述固定网数值。R651 初始严格根若尚未取得，不运行以正时长源为前提的 full-BVP 续接。原 R641/R632/R636 各自的真实科学任务继续。
