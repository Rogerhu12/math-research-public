# D5 实际固定 $\tau$ 二阶参数源检查点

**浮点诊断；恒等式与变分方程的完整证明见 R62。** 当前准确参数对象是
`type_fixed_step02_d5_exact_affine_step3_object.json`，SHA256
`e6ff2d46ed2d321c1b287e6c9d8e44ead7b9a70523350d145d703b4edd6def0f`，
$\delta_3=-7832869216826619/4611686018427387904$。真实根证书 SHA256 为
`afdc964a11682f9c54ceb1e6a165950f007ea26ab917f8dbde8b38c9fe78629f`。

## 已完成的实际接口

`fourfold_phase_affine_second_variation.py` 固定 $\tau$、令 $x=t(\delta)\sin\tau$，
计算真实 $f,f_\theta,f_\delta,f_{\theta\theta},f_{\theta\delta},f_{\delta\delta}$。
参数导数来自 affine profile、非径向二型与目标曲率的有限 jet 代数；有限差分只用于诊断，未进入源项。

其中根导数的浮点评价值为

$$
t_\delta=6.110800376546802\cdot10^{-5},\qquad
t_{\delta\delta}=-9.402869185378746\cdot10^{-7}.
$$

这两个值落在 R58 的整管有向区间中。$|\sin\tau|\ge0.999$ 时使用根积分商，直接形成 $Q,Q_\delta,Q_{\delta\delta}$，没有将分别发散的项相减。所需共同 collar 与 R58 一致。

新脚本逐个 binary64 knot 检查实际输入：phase/base/shift/mean/height-slope 全为五次，$|x|\le.24$ 内最大节点重数为一，共同 root collar 无这些节点或其反射点。这是有限准确输入检查，而不是浮点估计某个导数的正则性。

## 独立一阶对比与二阶差分费用

在 $\tau=-.71,0,.71$ 和四个实际角上，把旧几何评价器提供的固定 $x$ 实际参数列加上 $x_\delta=t_\delta\sin\tau$ 的链式项，与新源比较：

- $f$ 最大差 $6.661338147750939\cdot10^{-16}$；
- $f_\delta$ 最大差 $5.6378512969246235\cdot10^{-18}$。

再对同族 $\delta_3\pm h$ 重新求目标根，不冻结旧根；采用两个端点和五个内部 $\tau$、四个角作中央差分。全部三次位移都在原 $|\delta|\le.01$ 管内。结果为：

| $h$ | 一阶 $f_\delta$ 最大差 | 二阶 $f_{\delta\delta}$ 最大差 | 混合 $f_{\theta\delta}$ 最大差 |
|---|---:|---:|---:|
| $10^{-4}$ | $2.6777640\cdot10^{-8}$ | $5.7587028\cdot10^{-4}$ | $1.6648983\cdot10^{-7}$ |
| $10^{-3}$ | $4.1743478\cdot10^{-10}$ | $4.8064450\cdot10^{-6}$ | $3.2130831\cdot10^{-9}$ |
| $4\cdot10^{-3}$ | $6.5653574\cdot10^{-10}$ | $5.4165145\cdot10^{-8}$ | $3.4515544\cdot10^{-9}$ |

小步长的二阶差分在这里明显放大函数评价/重新求根的舍入误差；不能把差分差值本身当作二阶导数的严格误差。三个结果都保存，未只挑较小的一个。实际源的二阶项由 R62 公式给出，连续有向界仍需另外支付。

从本课题目录重做，分别把 `--parameter-step` 取 `.0001`、`.001`、`.004`，输出尾名分别用 `second-source`、`second-source-h1e3`、`second-source-h4e3`：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_affine_second_variation.py \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json \
  --out notes/2026-11-12-D5-exact-affine-step3-second-source-h4e3.json \
  --parameter-step .004
```

## 共享网格入口

新 `fourfold_phase_shared_knot_nodes.py` 复用准确对象的一阶解析参数 runner，
一次对全部 516 条射线共同选时间步；强制 `--block-size` 等于 `--rays`。
每个 forward/backward 分支按最多 32 accepted steps 一片保存，不对初始角另分组。
每片 metadata 的 `first_accepted_segment`、`accepted_segment_stop`、
`branch_total_accepted_segments` 明确定位；只有第一片的 `initial_angles` 才是 $H$ 初始格，其余是该片的轨道边界状态。

已启动的 benchmark（输出尚未完成，不属于本次冻结报告）：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_shared_knot_nodes.py \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json \
  --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_dyadic_H.json \
  --out notes/2026-11-12-D5-exact-affine-step3-shared-knot-Hnodes516.json \
  --trace-dir data/phase_ring_continuation/exact_affine_step3_shared_knot_dense516 \
  --rays 516 --block-size 516 --tolerance 2e-12 --resume
```

共享积分网格是为了缩小 R61 全初值参考的时间分区并集；它本身不证明 ODE 残差、参数 Taylor 范数、共轭方程或 PDE 可逆性。
