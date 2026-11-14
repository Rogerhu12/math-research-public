# 准确参数源有限节点接口：δ5、forward419

2026-11-12。全核心连续模界在 R80；本页保存与同一有限参考相接的实际
取值接口及一次完整运行。它保留参数源的符号，但尚不是连续积分或 twist。

## 对象与微分

中心为准确 -7789843107295549/4611686018427387904。使用 object SHA
91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848、
point-root SHA
489268d254c2a9454ccbee32a4821d9bf577279490f76c9cc6f8d902a5e64e0b，
完整参数方向和 R80 相同。节点计算的真实参数小管半径是准确
1/100000000000000；它是 R80 的大管的子集。

scripts/fourfold_phase_real_parameter_forcing.py 的 SHA256：
7c1d1393cf32b8d5e98f8f3cbb2963e2b04deeaa8cc7a19dedf41e607cc3b632。
RealParameterFamily.snapshot(tau,sign).sample(thetas) 返回真实
f、fp、fpp 的有限复角数组球值，固定真实物理时间 tau。没有差商。
全部保留的 Fourier primitive 模及三个实际无限误差分别支付；参数一、
二阶包括根的 t′、t″ 和半径 r=t sin(tau) 的完整链式。
普通点微分实际 K；近转折先使用 R58 的 Q、Qp、Qpp，精确两个端点的
三种源都为零。跨共同 knot 的不确定径向包取全部实际相邻 germ 的 hull。

同一参数无关参考是 descriptor SHA
097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052。
reference_parameter_forcing 对完整有限 Y、Yu、q=Yx 返回

\[
g_0=(h f(Y)-Y_u)/q,\qquad
g_1=h f_p(Y)/q,\qquad
g_2=h f_{pp}(Y)/q.
\]

所有原图、Q 与初始修正乘积完整保留，准确物理半段宽 h 只乘一次，
没有额外因子 4。物理角到归一 map 的尺度在最终 endpoint 合成时处理。

## 本次真实运行

输出
data/phase_ring_continuation/type_fixed_step02_d5_step5_real_parameter_forcing419_pilot.json.gz，
SHA256 fb5018fb1d6d24c8072062c4b49c852f3c3ee17c506ce452bb5742f2069001de，
complete=true。Q512、256 bit，在 forward419 的 u=-1/2,0,1/2
各取 64 个标签节点，标签上边界 Im x=1/512。运行 CPU 10.2981 秒、
wall 70.8065 秒；耗时不参与证明。

这些有限节点的实际模数满足 |fp|<0.002371622、|fpp|<0.000031882。
离散 g1 均值的实部依次约为
-4.94206464456e-6、-4.95650414714e-6、-4.97095413534e-6，
单个值的球半径小于 2.337e-13。
上边界离散均值仍有约 1.7e-9 至 2.1e-9 的非零虚部：这里只取 64 点，
没有支付 alias，绝不可把这些离散均值作为实际全圆平均或扭转量。

同一真实中心时间另用已付域的独立 scalar sampler，在 512 个完整
物理角节点比较 f0，所有 Acb 球均重合；精确两个转折端点也实际核为零。
这项一致性核查没有替代源本身的解析无限尾证明。

重放入口，在课题目录：

~~~bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_phase_real_parameter_forcing.py \
  --out data/phase_ring_continuation/type_fixed_step02_d5_step5_real_parameter_forcing419_pilot.json.gz
~~~

该实时间接口不宣称复杂时间域。下一步在同一固定 scalar germ 的完整
时间域中构造有符号有限参数密度，再把其连续误差交 R82 的有序参数积分。
R80 的 20、200 只付粗余项，不能单独推出非零平均。
