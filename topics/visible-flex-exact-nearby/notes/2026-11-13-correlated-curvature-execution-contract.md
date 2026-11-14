# R113 曲率分子的完整 Fourier 实算合同

2026-11-13。源已写；执行器不可用，尚无本入口的数值结果。
保存源码不代表已认证曲率小量、连续全域或 Newton 收敛。

新入口 scripts/fourfold_phase_correlated_curvature.py 复用真实仿射族、
有向 FFT primitive 和完整 Aσ 余项。它不先独立估计三项绝对值再相加，
而在有向 Fourier 代数内形成
Δ=LN−M²−K0G²，最后才包络角函数。

每个标量 Polynomial 保存有限真多项式的系数区间、准确支撑界和真无限场
相对它的完整 A0 余项。若 A=A_N+e_A、B=B_N+e_B，乘积余项取
||A_N||A0 εB+||B_N||A0 εA+εAεB，加法取误差和。
几何的 dot/cross 按三个标量分量准确构成，不能漏分量因子。
目标 E、E' 从真实完整均值包络形成；K0的常数球包括这些完整余项。

N节点 primitive 的 Nyquist 被原构造准确置零，真实有限支撑至N/2−1。
F和其导数为一次，C二次，L/M/N三次，G四次，Δ最高八次，
故乘积网格8N满足8(N/2−1)<(8N)/2；每次乘法还检查支撑不触边界。
此网格足以容纳全部有限卷积，任意无限尾均单列传播。
大常数项先分离，避免把它们经FFT后再数值消掉。
区间系数包含的舍入半径不能冒作真实无限尾，也不能被删除。

在最终角网格Q≥8N上，有限多项式的连续小格费用为
π/(4Q)||∂θP_N||A0，再加完整εP。归一角x=4θ，
所以小格宽度为物理θ宽度；所有小格覆盖一个π/2周期，
D4旋转不变的几何标量由此覆盖整个角圆。
每个小格还与完整Wiener模的全局区间相交；两者都独立包含真函数，
因此交集仍严谨。不是对角样本做未付费插值。

逐格检查G,T,S>0及N<0，再按R113准确式计算
K_F−K0=Δ/G²、ω=−TΔ/(NS²)及弱修正费。
T的平方根逐binary64端点经Arb包络，不依赖未经控制的库函数舍入。
球面密度、X的实际长度和cap的log ground-state角导都显式保留。
core选择ℓ=0；cap选择仅在Fz>0的正帽，使用真ℓ=∂θlog(Fz/√T)。
两者之间的实际cutoff过渡必须另证，不能按较小数随意切换。

首批恢复命令：

~~~sh
python scripts/fourfold_phase_correlated_curvature.py --points 0 1/8 1/4 --ell core --out notes/2026-11-13-correlated-curvature-core-points.json
python scripts/fourfold_phase_correlated_curvature.py --points 1/4 1/2 1 --ell cap --out notes/2026-11-13-correlated-curvature-cap-points.json
~~~

每个点输出都含整个δ5±1e−9及全部角；它不覆盖未列径向位置。
连续区间只允许落在一个准确公共spline germ，用--left/--right明确指定。
参数单点诊断可用--half-width 0，不能将其授予wholeη。
全连续域/强导数/背景邻域及Newton门均保持未支付。

R111另有 scripts/fourfold_phase_cap_parameter_collect.py：消费真实逐盒body报告，
允许无pending/failed的已接受前缀及完整续算，检查同族/源/依赖和精确有理无缝覆盖，
再直接消费已远存的完整322段graft。它不从execution receipt重建任何缺失行。
由于wall/CPU时间本来写入原报告，重跑后的文件SHA可不同；应记录新的真实SHA，
而不是伪造旧字节或要求重跑时间相同。本collector也尚未执行。
