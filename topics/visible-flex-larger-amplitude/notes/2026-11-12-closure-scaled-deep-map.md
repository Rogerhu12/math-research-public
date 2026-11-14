# 可计算精确深尾接口进度

2026-11-12，exact_closure。

完整新证明已登记为 [R18](../results/R18-computable-exact-tail-trace-and-robin-envelope.md)。它改进 R17 的辅助 cutoff 和一次固定角宽分配，支付 n192 起的完整局部 map；在数学端口 F224 给真实 low46-height-to-full-trace 图，归一低高度球为 $2^{-1947}$。数学 F224 对应 source physical node225 / linearFar225，不能少算这个 +1。

在更小的 $|z|_1\le2^{-2048}$ 内，理想 Robin 与完整精确低模动量图的平衡范数误差小于 $2^{-59}|z|_1$，完整第47模起 trace 的 raw 范数至多 $2^{-81}|z|_1$；完整 mean 的端口斜率和 cuff 高度规范也有显式二次界。该图直接限制到 R17 的 N4096 唯一族，不需要 double 表示该处 delta。

[精确账本](2026-11-12-closure-scaled-f224-radius-ledger.json) 的40个整数/分数比较全部PASS。脚本是 [closure_scaled_radius_ledger.py](../computations/closure_scaled_radius_ledger.py)。其中浮点 log-gain 部分明确单列为未认证的线性尺度诊断；q003 的 cut-height 线性外推给 F224 的 log2低高度约 -2341.33，比定义域界留394.33bit。它没有使用实际非线性 rawStates[8] 的全频传播，因此不是浅头 trace 匹配证明。

下一工作转向实际 q003 新g checkpoint 的浅头/深端残差和尺度化传播，把该余量转为可核查的误差控制。R18没有删除固定g加密、强幅前缀匹配、完整闭图和reach欠账。
