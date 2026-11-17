# m3 q025首个初值失败的实际定位

会话 Astra-held10-f00f08c9-20261117。原接受的固定g细层q_actual=.020001546225852943作为暖数据，目标q=.025重新设计prefix δ；这不是跨幅同g加密。完整新带符号H送进原真实非线性尾，但第一个请求在momentum局部Newton停止，尚无完整shooting residual或prefix解。

附带脚本逐式复现原worker的重网格、整体幅度缩放、完整线性边界修正和首次坏状态，不改任何守卫。新H为旧H乘1.2499033683549081，各系数比例差≤1.1e−20；对多模输入原harmonic predictor未启用，因为其条件是所有高输入模严格为零。全部节点上的线性cut校正相对最大3.14e−12。因此本次失败不是新warp造成的大高频污染。

首坏映射是stage38、cell0/segment4、raw interval[.125,.25]，RK第12步b中点x=.78125，物理r=.2447882536、w=.00116526602。前38段均可评价。这个不一致缩放初值的单一中间状态，用上一局部root作下一次初猜的幅度同伦只能到λ=.9979912745，minA=.0500026714、minD=.9999970741；进一步步触原A floor .05。

没有达到完整该状态，没有证明A=0、几何奇性、真实非线性分支容量或q025不存在。不能把局部initializer守卫当本题的几何障碍。

同旧接受态的小步q021已进入原全局Newton，冻结时res683→164→9.49但仍运行，没有终态结论。另有针对性的独立试验：直接把完整旧accepted states作为原multiple-shooting初值，保留新cut Dirichlet残差及其Newton边界列，避免先将节点整体缩放并强制新cut；由原line search支付边界变化。该改进截至本条尚未有接受结果，原方程/门不变。

最小诊断源、完整命令、源/响应/hash及必要标量见 `../scripts/nonlinear_tail/m3_amplitude_initializer_deliverable/`；manifest SHA-256 `01ac30c2f38254275955f773d04b6cbcf90fe8484983c4a5c887c4f7f4461fa0`。40点局部trace与状态数组留在scratch，有hash和再生命令。
