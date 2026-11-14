# 非零 quartic 根结构的实际几何设计接口

日期：2026-11-14。状态：实现完成及合成接口检查；**尚未运行本脚本的研究优化**。脚本为 `scripts/literature_quartic_codesign.py`，直接导入已冻结的 `literature_closed_codesign.py` 的真实几何、初值和诊断，不改动该模块。

目标来自 R8 的必要条件：非零 C∞ 紧支撑复 profile 的真实支撑端点为 C 的两个二重实根。本设计只寻找这个几何入口，没有把必要条件当作 profile 存在或有限弯曲。

## 方程和非退化门

从既有 11 项接口准确提取

\[
(c_0,c_1,c_2,c_3,c_4)=
(r_0,r_1+s_0,s_1+t_0-p_0/4,t_1-p_1/4,-p_2/4).
\]

若 `c4≠0`，令 `U=c3/(2c4)`、`V=(c2/c4−U²)/2`，则两条消元残差为

\[
c_1-2c_4UV,\qquad c_0-c_4V^2,
\]

还需 `U²−4V>0`。这些残差、判别式及导出的候选两根在输出中完整保留。

实际优化为避免除以接近零的 c4，另带两个真实根变量 `a<b`，比较

\[
C(\xi)\quad\text{与}\quad c_4(\xi-a)^2(\xi-b)^2
\]

的前四个系数。四条方程加两个根未知量，与上述两条形状方程等维；最高系数来自当前真实几何。c4 有固定非零幅度门，区间宽有严格正的参数下界，不能靠 c4→0 或两根合并宣称通过。多项式残差的单位尺度在初值时冻结，另输出相对于目标系数大小的误差，防止缩小整体幅度掩盖形状差。

## 物理区间和固定参数验证

令固定 ξ 单位为 `d=max(1,初值omega的采样极差)`，根变量是正 gap 和正 width 的对数。

- 正 u 分支令 `a=−min omega+gap`、`b=a+width`。
- 负 u 分支令 `b=−max omega−gap`、`a=b−width`。

训练节点上的整个根区间因而位于 `ξ+omega` 同号半带。这个构造只对训练所用的采样 extrema 有效，未宣称连续域证书。优化后冻结 a、b、c4、所有真实几何参数、闭合 tilt 与速度归一化；验证网格不再重选任何这些数值。每档验证比较**全部五个 C 系数**与同一个冻结目标，故最高系数的积分漂移也可见。

验证还记录原 quartic 的复根、候选二次式的实根、分母范围、实际采样 `u=h/(ξ+omega)` 范围、两端 u 范围和最窄 u 宽度。分母在某个采样角度的区间内部跨零时明确报告，不能以端点分母本身非零绕过检查。

两个端点的标准指数率始终作为条件性诊断输出；可用 `--enforce-exponential-signs` 加入该 ansatz 的正号筛。默认不加该筛，以免把标准指数形式以外的全平行为未经证明地排除。

端点率的分母用该验证网格得到的实际 c4，端点位置始终用冻结的 a、b；这是对当前积分值的候选诊断，不表示把端点率本身也冻结。与冻结完整目标的五系数差独立报告。

## 导数门

优化 Jacobian 使用共享 `closed.absolute_jacobian` 的逐坐标中央差分，步长固定为 `2e−5 max(1,|xj|)`。不能使用相对步长 `2e−5 |xj|`：初值中接近零的 Fourier 系数会把步长缩至浮点消差区。输出记录具体方法和步长，并在 Actions 内对最终设计记录另一步长的方向导数交叉检查；合成接口检查另以一个含 `1e−16` 坐标的二次函数比对精确 Jacobian，最大绝对误差 `1.3654e−11`，不调用真实几何。

## 接口与来源

例：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_quartic_codesign.py \
  --q 3 --sides positive negative --theta-n 768 \
  --validation-n 768 1536 3072 --max-nfev 150 \
  --warm-start path/to/public-closed-design.json \
  --out path/to/quartic-design.json
```

真实运行由公开仓库 Actions 执行。`--warm-start` 读取同 q、相同模式数的已存 `final_parameters`；输出保留输入路径、SHA-256 和来源 schema。默认种子为 q=3、2、4，均可单独选择；每个已完成的设计立即写入小报告。

本地仅运行 `--developer-check`：用 `2(ξ−3)²(ξ−5)²` 检查接口和两残差，拒绝零/极小 c4 和无实二次根，使用三个人工 omega/v 点检查正、负半带及跨极点失败，并核冻结目标能暴露最高系数改变。所有检查通过，没有调用真实 `geometry`，没有运行研究优化。

报告明确保持 `full_complex_period_equation_solved=false`、`three_complex_total_moments_solved=false`、`nonzero_profile_constructed=false`、`finite_isometric_path_proved=false`。即使形状残差很小，还要认证双根与整个物理区间，再求真实复 profile、完整二阶修正及高阶/有限路径；嵌入、握持和 reach 仍是独立未完成项。
