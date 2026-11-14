# 完整几何场基准与已知采样遗漏

原计划 `root-q095-five-direction-geometry-r1` 的 baseline，session69183 正式 exit0；wall48.951793909秒，wait4峰131540KiB。完整629×192×3 signed principal curvature / twice-radius 场已保存，无尾worker、新BVP或新Jac。插值仍用全部原始节点、24模和完整production mean；采样网格并未截断状态。八件清单见 `2026-11-12-root-q095-five-direction-geometry-r1-baseline-stable-files.json`。

当前样本max|κ|=8.42581873831104，max2|F|=3.900946460074288。它比同一q095全部状态的旧386×384诊断最大曲率8.439326192633953小；已知旧见证位于physical s=0.9566790776149228、chart ψ=1.1617347833587257。新网格未含这一径向/角向组合，因此不能把较小值解释为几何改进、曲率上界或reach。旧见证完整记录在 `2026-11-12-root-q095-actual-neutral-geometry-r1-baseline-screen.json`。

其它十个方向场未执行。下一计划保留原全部raw的physical-s C² cubic和所有模，在统一数值坐标中纳入旧峰、真实物理knots及短段细分，并使用384角点；必要时完整数组分块压缩，单件<5MB。有限行LP的预测仍须在真正联解及连续几何中核验，不能支付完成条5/6。当前主计算窗口用于disk4388实际q105，不为新诊断暂停生产。
