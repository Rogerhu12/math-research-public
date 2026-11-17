# 完整M160首次BVP失败及原RMS评价点的定义域缺口

**一次真实失败，不作新父。** 按已冻结7feed9 warm与54ee88 BA/BB/target，只运行完整482ODE/325左/157右，保持HoldProfile、原前三core、tol1e−8、bc_tol1e−11、max_nodes1800及原17次回溯。没有删模、改目标或放宽域。

首个全段QR真实处理827节点、826胞，102.07秒，约0.99GB RSS，约化矩阵条件数160814.2801。首线性解max系数.06909727468；完整collocation加边界的线性∞残差9.77754268384e−13，rhs∞=1.14960176596e−5，故所报相对线性残差8.50515628399e−8。**该比值不是ODE缺陷或非线性误差。**

首次Newton的17个试点均未被接受，原点保留。实际试验α=1,1/2,…,1/65536，最小为2⁻¹⁶，未试2⁻¹⁷。分类可从冻结控制流及完整日志严格读出：只出现一次`separated_qr_solve`（原线性解）；任何finite试点残差都会调用并记录另一次factor.solve。此run正常返回且没有异常，因此17次均是**nonfinite residual拒绝，均未进入finite merit比较**。每个α的具体坏角/Q/W/H位置没有逐项记录，不能伪造这些更细分类；RHS guard及其NaN传播合计触发8310个无效RHS点。

随后SciPy的RMS估计出现NaN，网格增至1396，下一次原helper报告`invalid_current_iterate`并返回终止标记，SciPy以status2“singular Jacobian”结束。**第二个Jacobian没有装配；此通用标签不是矩阵奇异证据。** 总耗时144.67秒、52次Jacobian批调用/1678个完整Jacobian点、48次RHS批调用/43654点，无Newton步被接受。

## 只读定位：中点正性不覆盖RMS位置

原solver的RMS在由实际RHS构造的Hermite cubic上读取

\[
u_\pm=(1\pm\sqrt{3/7})/2.
\]

新诊断直接调用该环境的`create_spline`，读取原827 warm和最终1396失败数据，不重跑QR/Newton，不改场。按实际N2048 RHS网格：

|数据|点族|坏胞数|最小H|
|---|---|---:|---:|
|原827 warm|u=1/2|0|6.54549e−9|
|原827 warm|u₋|234|−.000527343048547|
|原827 warm|u₊|153|−.000103372335309|
|终1396失败数据|u=1/2|1|−.00000334521858015|
|终1396失败数据|u₋|235|−.000527343048547|
|终1396失败数据|u₊|154|−.000103372335309|

原827的坏RMS胞全部位于κ=0接口后，u₋首坏胞左端1.0340291868598537；最坏H分别位于s=1.038586398089846/旧角2.3531265286165737及s=1.0361282427362417/旧角2.350058567040802。它们明确解释RMS NaN及原准备覆盖不足。声明的参考quintic、solver的RHS-Hermite及其RMS点是不同读出，不能用前两者的一部分正性替代全部solver评价点。

允许的后续准备修复是保持同g、同参考曲线和同冻结边界，只二分任一中点/u₋/u₊坏胞的并集，仍在1800节点总额内；本项未实施该修复，也没有把失败1396数据作为父。

## 复现/身份

S为本题scripts目录、T为题目录。实际单次完整BVP与只读审计命令：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$S" python "$S/parallel_20261117_hold_full_bvp_once.py" --topic "$T" --warm parallel-hold-m160-bvp-adaptive-warm.json.gz --arrays parallel-hold-m160-bvp-adaptive-arrays.npz --hold-source "$S/parallel_20261117_negative_hold_profile_ivp.py" --out parallel-hold-m160-bvp-once.json.gz
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$S" python "$S/parallel_20261117_hold_bvp_rms_domain.py" --inputs parallel-hold-m160-bvp-adaptive-warm.json.gz parallel-hold-m160-bvp-once.json.gz --hold-source "$S/parallel_20261117_negative_hold_profile_ivp.py" --out parallel-hold-m160-bvp-rms-domain.json
```

SHA256：

- 实际BVP源：`f93d74382ac83bee08079759ca17cace95b3e99cb765e706e6d1ef67c7861d81`。
- 只读域诊断源：`38607cb0d4e321887978d7155c52ad2451d3bd1d8712b98ceca1805d7610262b`。
- 原完整日志：`4aa78811b6f0b4e6a8302e013a67f1123c3d17f1d02db61830c9f1fb403ef96a`。
- 失败raw：`2c6b1b20c68c2545507beb7ac44f01e532233060520881e137e9dda65f14ce2e`。
- 实际失败report：`f01e65a934be1d62af9a6c7a610ebe1b2429e470afb6715ff9063055f01a1187`。
- 只读诊断report：`2a06e383d44835fb2f44c1da8d2c55fe0ea1f57a690c2b5bc773ed3144a62be5`。
- 所读SciPy `_bvp.py`：`59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2`。

真实执行源硬核既有warm/targets/Frenet/fresh-J/QR/HoldProfile的SHA；各输入与依赖完整列表见report。所有raw、日志和矩阵只留scratch。

后续[原1800预算内全评价点修复](2026-11-17-parallel-numerical-hold-allpoint-budget-failure.md)已真实失败：1529节点仍936坏胞、下一层2465超额，未再启Newton；该结果不排除同g或其他初猜。
