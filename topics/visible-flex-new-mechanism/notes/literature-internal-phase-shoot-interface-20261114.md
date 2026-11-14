# R13 局部相位入口的公开 Actions 验证接口

日期：2026-11-14。脚本：`scripts/literature_internal_phase_shoot.py`。状态：合成多项式接口检查通过；实际 profile 求解及射击须由公开仓库 Actions 执行，本地尚未运行。

## 输入范围

脚本固定使用 [R13](../results/R13-local-smooth-complex-phase-opening.md) 的精确抽象系数

`(p0,p1,p2,r0,r1,s0,s1,t0,t1)=(2,0,−4,1,0,0,−4,5/2,0)`。

它们满足实际周期算子的九系数恒等关系，但**未由任何真实闭曲线的几何积分实现**。脚本没有把前一轮几何优化结果换成这组系数后继续称为同一个几何基底。

## 局部 Picard 与冻结验证

使用 R13 的精确四维 normal form。ℓ 和 G 通过有限多项式系数直接求值，避免计算 L/x²、R/x 时的小数相消。三条 Euler 方程的积分算子用 Chebyshev 插值多项式上的 `(tD+mI)^{-1}` 实现；奇异一阶 Green 算子用固定线性系统实现。

正支施加 `v(δ)=i eta_imag δ`，负支使用 0 附近有界条件，不另捏造负端终值。两支均从零余项开始迭代；报告 Picard 变化量、迭代状态和 ℓ 的安全范围。没有收敛或违反局部门时，不继续射击。

解出节点值后冻结其 Chebyshev 系数，在 `2N+3` 和 `4N+3` 个均匀点上检查三条 Euler 残差、完整 fast normal form 残差、直接 Q 与因式 Q 的差、完整局部 O。这里密网不重新解方程。N 加密则另给一份独立结果，端点参数 ηδ 保持相同，便于比较。

J 始终从 R13 的局部常数 `(44/9,3/4,−14/9)` 在 0 点积分。q′、q″ 的 Chebyshev 多项式先精确相乘再积分，避免只在原节点上平方后发生别名。**这些 J 尚不是来自某个已存在全平右尾的积分。**

## 外延与未付端点条件

仅局部数值门通过时，才从最高 N 的 ±δ 端点向 `±outer_stop` 积分 Q 及 J 方程。使用 DOP853；实部与虚部分成 14 个实变量，虚部另缩放，并按其初值设绝对容差，避免 O(1) 实部的误差阈值吞没全平虚部。

遇到归一化 L 太小、前四个 jet 过大或积分器失败时停止该次射击并报告位置。这些事件是当前显式正常形的数值停止条件，不是不存在证据。不会跨过未知退化点继续除以 L。

输出记录局部 O 在外延中的漂移、实际终点、实/虚 jet、J、采样 L 余量，以及左右已计算段的积分差。默认终点为 ±0.995，仍在目标区间内部。即使射击走到该点，也不能把有限 jet 和矩残差当作 ±1 处全平性或三总矩的证书。

## 建议首轮命令

```bash
python topics/visible-flex-new-mechanism/scripts/literature_internal_phase_shoot.py \
  --n 96 192 --length 0.003 0.006 --eta-imag 0.001 0.1 \
  --outer-stop 0.995 --out path/to/internal-phase-shoot.json
```

脚本检查公开仓库 Actions 环境；结果 JSON 逐批写出。可用 `--skip-shoot` 单独检查局部求解，不改变任何已固定局部参数。

本地只执行 `--developer-check`：固定低阶多项式的微分矩阵误差 `1.06e−13`，两个合成复向量上的精确 normal form 恒等式误差最大 `7.11e−15`，Chebyshev 转换及积分锚点检查通过。没有运行局部 Picard、ODE 射击或几何优化。

积分器接口按 [SciPy 官方 solve_ivp 文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) 核对。完整状态始终保留 `global_compact_profile_constructed=false`、`three_complex_total_moments_solved=false` 和 `finite_isometric_family_proved=false`。
