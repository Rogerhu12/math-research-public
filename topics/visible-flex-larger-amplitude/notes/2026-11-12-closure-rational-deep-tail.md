# 固定有理深尾的恢复与实现记录

2026-11-12，exact_closure。

完整证明已经按主代理分配登记为 [R15](../results/R15-rational-deep-tail-and-46-parameter-trace.md)。该结果只构造充分深处的受限精确尾，不是整个闭曲面或强幅匹配的完成声明。

线性谱/Green精确有理核算为 [计算脚本](../computations/closure_rational_tail_linear.py) 和 [结果](2026-11-12-closure-rational-linear.json)。结果给46维受限族、CG<2^27、CE<2^61；N192仅支付线性扰动门，N224另支付低频高度坐标的线性门。

## 显式非线性深度已支付

[R17](../results/R17-explicit-rational-tail-nonlinear-depth.md) 逐项给出局部 $c_*=2^{-256}$、$C_*=2^{320}$；局部全频流从 n512（加真实 slope≤1）成立，当前固定参数的共同非线性起点可以明确取 N4096。36项整数/分数比较全部 PASS，见 [脚本](../computations/closure_rational_nonlinear_constants.py) 与 [账本](2026-11-12-closure-rational-nonlinear-constants.json)。

归一不是把 wCut 当 epsilon：原 epsilonScale 精确存数除以原 rCuff 存数的七次幂，严格给 $2^{14}<\epsilon<2^{15}$，近似16572.1331147941。N4096以后为未 warp 的有理深源；原浅部 warp 161.27721826272244 的传播/导数预算仍待单独计算。N4096 的 delta 不能用普通 double 直接表示。

## 新固定度量的数值 adapter 与线性诊断

实现只在 protectCell=160 及以后使用 alpha=65/64，保留原0…159的全部源profile、warp与全宽系数。它是新 g，不接续旧 g_stored 的加密链。源 delta0=.006、etaRatio=.05 按各自 IEEE-754 存数的精确 dyadic 值解释，不偷换为3/500或1/20。模型在全160胞元每段5个点的物理数据上保存前后 SHA256 指纹，端点相容的精确依据仍是 quintic profile 的符号定义；浮点 logw 端值差约5.68e-14不冒充精确等式。

已完成的46模浅 cut 线性诊断：

- [s256](2026-11-12-closure-rational-trace-m46-s256.json) 与 [s512](2026-11-12-closure-rational-trace-m46-s512.json)；
- 两次的 far176→192 全46模斜率/射影列在浮点上相同；
- s256→s512 仍有径向积分误差：m2斜率差7.49e-6，m16差9.73e-3，最差相对差约1.48%在m76；最大预条件射影差2.73e-6在m40；
- 这些旧诊断使用均匀 RK4，不能把深度饱和叫作径向收敛，更不能叫作精确非线性 trace。

供真实有限 DN 使用的新共享 cusp 网格与96点有界缓存已经通过 [小型等值检查](2026-11-12-closure-stage-graph-equivalence.json)：相对固定950f源程序，435个 graphs、432个 gains 逐值 bitwise 相等，全部160胞元×9段×7点的物理指纹前后相同；peak RSS143432KiB。通用模块为 [closure_bounded_point_cache.mjs](../computations/closure_bounded_point_cache.mjs) 和 [closure_linear_stage_graphs.mjs](../computations/closure_linear_stage_graphs.mjs)，它们不依赖新有理度量，tail_refinement 已在自己的旧 g adapter 中单独复用并做端到端逐值检查。

## 第一次真实新 g 有限非线性响应

[结果摘要](2026-11-12-closure-rational-q003-m8-d8-s16-l1024-summary.json) 与 [完整响应](2026-11-12-closure-rational-q003-m8-d8-s16-l1024-response.json.gz) 由旧 q003 checkpoint 仅作 warm start，在新 g 上重新解实际方程：

- M8、physicalDepth8、每stage16步、shootingParts4、quadrature256、linearSteps1024；新 linearFar192。
- 原 solveTolerance2e-9 和全部实际审计保持；真实 residual 从4.1387e-9经一步 Newton 到2.1826e-11。
- audit actualMetric4.4478e-15、holonomy3.3608e-21、minLeading0.99378268、minD0.999996689。
- 完整输入config、ready模型/源码hash、trace、gzip状态均保存；浅头指纹保持；elapsed512.2秒，peak child RSS387676KiB，gzip56028B。

这只是新 g 上有限 Fourier/有限 nonlinearDepth 的收敛响应。far Robin 仍是线性图，不是 R17 的完整非线性深图；该结果没有将任意浅高度提升为可闭合数据。下一工作是从可算深度向 N4096 的尺度化传播/严格余项接口，以及强前缀与真实图的匹配。完整闭图、reach和强幅度仍未完成。
