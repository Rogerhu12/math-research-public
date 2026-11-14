# 真实场的准确 Fourier／时间多项式保存

## 对象与恢复范围

本实现 `scripts/fourfold_phase_actual_field_fourier_package.py` 的 SHA-256 为
`c5198dcc172d4c2ef271370d4fc9b1bf39c749f20e04835e4c39cccf7498734a`。
它是在执行器恢复后新增准确系数保存合同的版本；中断前的摘要包只观测到几何与有限节点求值阶段，没有观测到完成，也没有保存可复用多项式。这里不沿用那个未完成作业的任何数值结论。

默认真实图为准确仿射参数
\[
\delta_5=-7789843107295549/4611686018427387904.
\]
默认时间是 δ4 shared1032 网格提供的 segment 419 的两个准确有理端点，但场、根和解析域全部使用 δ5。域报告必须同时确认对象／根哈希、准确参数、真实共同 span 列表、全角与复时间域完成。新恢复后域报告的 SHA-256 为
`e1a2c3f327c3a36e33c412e76c70eebd185f224ea938dcdea93ee30ab9a05f90`。

每次实际作业是否完成，以它自己写出的 JSON 中 `complete` 与其输入／源码哈希为准。本文给出保存定义和误差证明，不提前宣告正在运行的作业完成。

## 1. 保存的准确对象

令 \(\tau=\tau_c+hu\)，物理角周期为 \(\pi/2\)。所保存的有限对象为
\[
P(u,\theta)=
 \sum_{j=0}^{m-1}\sum_{k=-K}^{K}c_{j,k}u^j e^{4ik\theta}.
\]
其中所有 \(c_{j,k}\) 的实虚部都是**准确 dyadic 数**，不是显示成十进制后的近似，不是二进制浮点 64 位截断，也不是带误差的球。

JSON 分片将每个实数写成 \([M,e]\)，其数学意义是 \(M2^e\)，\(M\) 是任意精度有符号整数的字符串。复系数使用
\[
[M_{\mathrm{re}},e_{\mathrm{re}},M_{\mathrm{im}},e_{\mathrm{im}}].
\]
`arb.man_exp()` 提取准确值；`arb((M,e))` 重新构造后必须满足准确性和数值相等检查。每四个时间阶写一个 gzip 分片，`mtime=0`，manifest 记录字节数、SHA-256、阶数区间和对象身份。保存后重新读取**全部**分片和系数，验证哈希、形状、完整时间覆盖和准确解码。

只保存 \(0\le k\le K\)。负模按定义取
\(c_{j,-k}=\overline{c_{j,k}}\)，零模取准确实数。因此 \(P\) 在真实 \(u,\theta\) 上准确为实。该定义没有用数值近似冒充一个准确共轭恒等式。

## 2. 节点与 DFT 选择误差

真实场 \(f(u,\theta)=d\theta/d\tau\) 具有实性：准确输入的实系数、实根、真实时间以及所选平方根分支保证它在真实 \(u,\theta\) 上为实。因此对固定实角 \(\theta_\ell=\pi\ell/(2N)\)，第 \(j\) 个真实时间系数也是实数。

冻结的 time evaluator 给出包含该真实系数的复球 \(B_{j,\ell}\)。程序确认其虚部含零，然后选择
\[
y_{j,\ell}=\operatorname{mid}(\operatorname{Re}B_{j,\ell})
\]
为准确实 dyadic 数。其真实节点误差不超过实部半径
\(\epsilon_{j,\ell}\)。取平均
\[
\bar\epsilon_j=N^{-1}\sum_\ell\epsilon_{j,\ell}.
\]
DFT 对每个系数的算子权重绝对值均为 \(1/N\)，故真实节点 DFT 与准确中点节点 DFT 的差不超过 \(\bar\epsilon_j\)。

NativeFFT 有向计算准确中点节点的 DFT，并返回包住准确 DFT 的球 \(A_{j,k}\)。对正模选择准确复中点，零模选择准确实中点，记为 \(c_{j,k}\)。令
\[
\eta_j=\max_{0\le k\le K}|A_{j,k}-c_{j,k}|,
\qquad e_j=\bar\epsilon_j+\eta_j .
\]
这里 \(|A-c|\) 是整球的模上界，**包括**零模虚部置零可能产生的距离；没有只取半径而忽略选择移动。

准确中点节点全部为实，真实节点也全部为实，所以两种准确 DFT 均满足严格共轭。负模由正模准确共轭定义后，同一 \(e_j\) 自动覆盖全部 \(-K\le k\le K\)。无需把定向 FFT 的负模球中点也当成准确共轭数。

节点误差中已经包含了真实无穷角原函数、目标 \(E\)、真实根及全部有向运算的误差；\(\eta_j\) 只负责此后准确节点 DFT 与所选准确系数之间的距离。

## 3. 连续角与时间误差

独立域证书给出
\[
|f(u,\theta)|\le M
 \quad (|u|\le R,\ |\operatorname{Im}\theta|\le S_o).
\]
实际默认输入为 \(R=3,\ S_o=1/64\)。Cauchy 公式给出第 \(j\) 个时间系数的整角带模数 \(M/R^j\)。

每个保留时间阶调用已独立审查的 `fourfold_boundary_fourier_budget.py`，取实轴采样宽度零、频率尺度四、节点误差 \(e_j\)。它分别支付：

- 全部真实 Fourier 混叠 \(k+\ell N\)，\(\ell\ne0\)；
- 保留模中由 \(e_j\) 产生的 Wiener 权重误差；
- 所有被丢弃的 \(|k|>K\) 真角模。

对物理角导数 \(q=0,1,2\)，权重为
\((4|k|)^q e^{4|k|s}\)。有限时间阶的这些误差逐项乘 \(|u|^j\) 后累加。遗漏的全部时间阶另付
\[
M\,\frac{(|u|/R)^m}{1-|u|/R}
\sum_{k\in\mathbb Z}(4|k|)^q e^{-4|k|(S_o-s)}.
\]
这覆盖整个时间／角频矩形补集，包括高时间阶与高角频的角落。代码不以有限 DFT 的小高频系数代替真实解析尾界。

得到的是 \(\partial_\theta^q(f-P)\) 在 \(|u|\le1\)、内角带上的统一界。系数 \(P\) 本身已经按准确字节独立保存，后续有限复合计算可复用同一对象。

## 4. 已执行的小型验证

恢复后对一个已知的准确模型
\[
(2+u-u^2)\left(1+\tfrac13\cos4\theta-\tfrac17\sin8\theta\right)
\]
执行了 16 个角节点、三个时间阶的保存与重读。检查了：

- 任意精度 dyadic 的 `man_exp` 完整往返；
- 全部分片的字节哈希、形状、时间覆盖和准确读回；
- 正负 Fourier 模的准确共轭与正弦模的符号；
- 重建系数对已知解析系数的误差被所付费用覆盖。

此测试验证保存与符号接口，不授予实际 δ5 图的数值结果。实际图仍必须运行下面的完整命令并保存自己的报告。

## 5. 精确重跑入口

在课题目录执行：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python -u scripts/fourfold_phase_actual_field_fourier_package.py \
  --germ-index 2 --angles 4096 --degree 1800 --time-order 52 \
  --quarter-nodes 1024 --bits 320 \
  --inner-physical-theta-strip 81/10000 \
  --polynomial-dir data/phase_ring_continuation/step5_reference419_main_field_polynomial \
  --out data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_main_actual_field_fourier.json
```

读取保存对象使用
`load_polynomial(manifest_path)`，返回 manifest 与按 \(-K,\ldots,K\) 排列的准确复系数矩阵。应先设置足够的 Arb 精度；任何无法准确重建的系数都被拒绝，不能静默降为机器浮点。

## 6. 尚未授予的结论

此包只处理选定解析 germ 的外延。真实径向轨迹跨多个 spline span 时，必须为全部活动 germ 付出相应残差或取并集上界。完整全角解析域证书包含三个 germ，并不自动把一个 germ 的有限 \(P\) 变成整段真实 piecewise 场。

本包没有计算非均匀参考的 \(f(Y)\) 复合，没有支付整条流的误差，也没有完成 Wiener 返回映射验证或非线性 PDE 的存在证明。

