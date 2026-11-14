# D5 实际 ODE/J 共轭 Newton 检查点

2026-11-12，constructive-route。本文只记录浮点预测和实际射线检验；
严谨的连续 N 与参数根结论另见 R55、R57。冻结时，第二步的 uniform
129 和 staggered 129 射线仍在运行，以下没有提前记为成功。

## 为什么改用实际 ODE Jacobian

旧 48 节点插值和 112 节点局部插值给出的共轭残差，都曾被新实际射线
否定。特别是源 `0dcfb37f...` 的 degree256 dyadic H，在 uniform64 上
最大误差仅 $3.40664\times10^{-6}$，但同源、同 H 的错位64上达到
$5.07492056\times10^{-4}$。完整失败数据已在 R55 manifest 保存。

新脚本 `scripts/fourfold_circle_actual_newton.py` 不再用插值 circle map
生成状态残差或状态 Jacobian。输入是同一源、同一 H 的已完成真实射线
$R(H(x_i)),J_i=R'(H(x_i))$。将节点上的 H 值定义为一个有限三角多项式，
明确承认这个新有限 H 在节点外可以不同于之前高次数 H。然后解有限线性
系统
$$
J_i\,\Delta h(x_i)-\Delta h(x_i+\alpha)
+G_i\Delta p=-\bigl(4R(H(x_i)/4)-H(x_i+\alpha)\bigr).
$$
这里 $x=4\theta$，$\alpha=2\pi\rho_5$，$G=4\partial_pR$。参数列若缺少
节点才从同源实际参数列作 periodic cubic interpolation；第一步为
128 状态节点和64参数节点，第二步的129个状态与参数节点完全相同。
H 的均值通过准确的参数圆旋转重定标；新 H 随后必须重新给出 dyadic
Wiener 证书。有限线性剩余小不代表非线性接受。

## 第一步：实际128节点预测，新的实际129节点检验

输入是 uniform64 与 staggered64 合成的完整128格。有限模型初始
真实 collocation 残差为 `.000567849201477455`。解得

- 参数修正 `−.0016740102254668519`；全局数值标签
  `p=.4396774815837377`；
- 线性剩余 `3.903e−18`，矩阵条件数约 `2002.23`；
- H 修正最大 `.00173342`，H′修正最大 `.102973`；
- 新 H 次数64，保存为129个样本以保留原 Nyquist 旋转后的正弦分量。

新几何文件是
`data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton128_probe.npz`，
SHA256
`566c95612ee91f9fb04282873530dbb97a1450f4c01c8b1814b003bd0e06aee5`。
其 metric norm 采样约 $7.92242\times10^{-5}$，腰差/直径代理采样约
`.0515017498`。这些仍是有限图采样，不是精确等距或 reach 证明。

新 dyadic H 的严谨有限多项式证书在
`notes/2026-11-12-step02-d5-actual-Newton128-H-Wiener-budget.json`。
归一化角 strip $s_x=1/32$ 上
$\|H'\|<3.359160$、$\|1/H'\|<5.236025$，实圆正导数已证明。
这只认证 H，不认证共轭方程。

对该几何和该 H 重新积分129个均匀实际节点，得到：

| 指标 | 实际129节点浮点值 |
|---|---:|
| 最大共轭误差 | `.00014765649958814464` |
| 最大误差角导数 | `.02158444528822967` |
| 加权误差均值 | `−8.743892988655481e−7` |
| 实际加权参数 twist | `.0023091145308023497` |
| twist 被积函数范围 | `[.0003001191967158313,.004579882424018106]` |
| 正根标签 | `.23839687522496475` |
| 移动根参数导数 | `6.11079807111234e−5` |

源数据为
`notes/2026-11-12-step02-d5-actual-Newton128-Hnodes129.json`。
这次检验较此前错位64最大误差下降，但仍远未达到严格 KAM 门。

R57 另以逐控制点准确比较证明该 checkpoint 的**显式对称无限图**落入
N 的独立盒，因而全核心有 $N<-.30865$。这没有把上述近似镜像浮点
射线转换为该准确对称图的已认证返回映射。

## 第二步预测及运行中对象

以同一129节点的实际返回、J、参数列形成第二个有限 Newton 步：

- `delta p=−2.363252824508565e−5`；新标签
  `p=.4396538490554926`；
- 初始残差 `.0001476564995894769`，线性剩余
  `3.53551552183945e−18`；
- H 修正最大 `.00137172936`，H′修正最大 `.07953846`；
- 新 degree64 H 的 H′采样范围 `[.35738488,1.77729943]`。

新几何文件：
`data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_probe.npz`，
SHA256
`3453e5be05f8ada2dc333d3e2eab5bcbf58d668eea4817ec7cda85913ca77fa7`。

其新 dyadic H 在 $s_x=1/32$ 上有严谨界
$\|H'\|<2.937193$、$\|1/H'\|<4.047210$；有限 reciprocal 缺陷小于
$4.686\times10^{-9}$。全部整数卷积、正导数和有理 exp 预算在
`notes/2026-11-12-step02-d5-actual-Newton129-step2-H-Wiener-budget.json`。

该 H 的 uniform129（含实际参数列）与 staggered129（实际 R/J）同时
运行，分块43节点，容差 `2e−9`。每个完整块及半程 branch 都保存，可
准确从完成块继续。冻结清单排除这两个尚未完成的 JSON/branch/progress
文件。两组完成后可合并为258格，继续真实 ODE/J Newton或作非线性接受
判断；不能只依据 uniform 节点宣布成功。

## 精确重做入口

所有命令在课题目录执行。第一步：

```sh
OPENBLAS_NUM_THREADS=1 python scripts/fourfold_circle_actual_newton.py \
  --actual-nodes notes/2026-11-12-step02-d5-jet-actual-conjugacy-nodes64.json \
                 notes/2026-11-12-step02-d5-jet-staggered-Hnodes64.json \
  --parameter-nodes notes/2026-11-12-step02-d5-jet-actual-conjugacy-nodes64.json \
  --base-global-parameter .4413514918092046 --target D5 \
  --out notes/2026-11-12-step02-d5-actual-Newton128.json \
  --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton128_H.npz

OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_parameter_probe.py \
  --checkpoint data/phase_ring_continuation/type_fixed_step02.npz \
  --directions data/phase_ring_continuation/type_fixed_step02_schur_directions.npz \
  --parameter-map notes/2026-11-12-phase24-corrected-step02-parameter-map48.json \
  --trial-checkpoint data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton128_probe.npz \
  --out notes/2026-11-12-step02-d5-actual-Newton128-geometry.json \
  --eigen-parameters .0008793549631674754 .00008793549631674754 0

OPENBLAS_NUM_THREADS=1 python scripts/fourfold_circle_conjugacy_budget.py \
  --conjugacy data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton128_H.npz \
  --polynomials data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton128_dyadic_H.json \
  --out notes/2026-11-12-step02-d5-actual-Newton128-H-Wiener-budget.json \
  --inverse-degree 512 --width-denominators 128 64 32

OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_conjugacy_nodes.py \
  --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton128_probe.npz \
  --directions data/phase_ring_continuation/type_fixed_step02_schur_directions.npz \
  --parameter-map notes/2026-11-12-phase24-corrected-step02-parameter-map48.json \
  --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton128_dyadic_H.json \
  --out notes/2026-11-12-step02-d5-actual-Newton128-Hnodes129.json \
  --branch-checkpoint data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton128_Hnodes_branch.npz \
  --rays 129 --block-size 32 --tolerance 2e-9 --resume
```

第二步的 actual Newton 输入改为该完整129文件，`--base-global-parameter`
改为 `.4396774815837377`。新 predictor 的 eigen-parameters 是新报告
`proposed_global_parameter` 分别乘准确浮点常数 `.002,.0002,0` 的实际
binary64 结果；保存值为
`.0008793076981109852,.00008793076981109853,0`。不要把手抄的更短十进制
截断当作同一个输入。新 dyadic 证书使用同一预算源及同一宽度列表。

正在运行的两项可重启命令为：

```sh
OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_conjugacy_nodes.py \
  --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_probe.npz \
  --directions data/phase_ring_continuation/type_fixed_step02_schur_directions.npz \
  --parameter-map notes/2026-11-12-phase24-corrected-step02-parameter-map48.json \
  --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_dyadic_H.json \
  --out notes/2026-11-12-step02-d5-actual-Newton129-step2-Hnodes129.json \
  --branch-checkpoint data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_Hnodes_branch.npz \
  --rays 129 --block-size 43 --tolerance 2e-9 --resume

OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_conjugacy_validation.py \
  --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_probe.npz \
  --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_dyadic_H.json \
  --out notes/2026-11-12-step02-d5-actual-Newton129-step2-staggered129.json \
  --branch-checkpoint data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_staggered_branch.npz \
  --rays 129 --offset .5 --block-size 43 --tolerance 2e-9 --resume
```

所有射线仍欠 ODE/采样误差、反射误差和复域预算；已认证的 H 多项式
正性、N 控制点管不能替代这些未付的部分。
