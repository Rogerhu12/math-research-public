# δ₄ 的 shared1032 完成；δ₅ 为准确系数 predictor

2026-11-12。δ₄ 两腿各 550 个 accepted steps，全部 1032 个初始角共用一套时间网格。
实际运行 21540 次 RHS、2829.55 秒，未复用 δ₃ 的 endpoint 值。

## 1. 原 δ₄ 的真实浮点结果与限制

准确对象为 `−7789866024620307/4611686018427387904`，H 为旧已证明的 H258。
完整报告 `2026-11-12-D5-exact-affine-step4-shared-knot-Hnodes1032.json`
SHA256 为 `4ef35b2a2eb3320a67b9a777859feeffb8448057c97c5e5e2053fbf86e156d01`。

| 实际采样量 | 值 |
|---|---:|
| 最大共轭残差 | 2.517275277114095×10⁻¹¹ |
| 最大残差一阶角导 | 2.104084240173165×10⁻⁹ |
| 加权平均残差 | −1.146525052454648×10⁻¹¹ |
| 加权平均参数列 | 0.002307171417490598 |
| 采样最大 N | −0.40801472573335423 |
| 径向归一化 Q 的最小浮点值 | 0.5993172837143316 |

这些是同图浮点结果，仍欠连续真流误差，不能代入 R31 当作已证 ε 或 σ。

另有明确不相容诊断：此 runner 的浮点根导数为
`6.110799498156206e−5`，而同一准确对象的新严格点区间为
`[6.110799499427786e−5,6.110799499501956e−5]`。
前者在区间之外约 `1.27e−14`，R62 的普通浮点 mixed-jet 计算
`6.110799498157194e−5` 也没有解决这一差异。
这显示浮点 spline/曲率高导数评价不能自动充当真实参数输入；不以重采样
或减少求解器 rtol 掩盖它。严格工作继续采用同族有向区间结果。

全部原始 70 个压缩分片与两份 trace manifest 共 234661599 字节，单件最大
3421031 字节。完整哈希表为 `2026-11-12-D5-step4-shared1032-raw-trace-hashes.json`，
SHA256 `e0e7dabea437b05a0b22bff5140935de1f6f798ebcd8bf25c2bd57bdf563aec4`。
这些大型中间数据留作复现，不自动整包提交。

原图重跑入口：

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python scripts/fourfold_phase_shared_grid_adaptive_chunks.py --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_object.json --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_root_tight.json --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_dyadic_H.json --out notes/2026-11-12-D5-exact-affine-step4-shared-knot-Hnodes1032.json --trace-dir data/phase_ring_continuation/exact_affine_step4_shared_knot_dense1032 --progress notes/2026-11-12-D5-exact-affine-step4-shared-knot-Hnodes1032-progress.json --rays 1032 --block-size 1032 --tolerance 2e-12 --resume

## 2. 一次便宜的有限 predictor

使用上述同一 1032 组实际 Y、J、参数列运行冻结的有限 circle Newton，
得到 δ₅ 的准确对象定义：

\[
 \delta_5=-7789843107295549/4611686018427387904,
 \quad \delta_5-\delta_4=11458662379/2305843009213693952.
\]

浮点求出的参数修正为 `4.969402658081083e−9`。将参数加到旧 dyadic 参数
并舍入成所选新 binary64 后，准确加法差为
`−27319/604462909807314587353088`，已完整记录，未修改控制点数组。

有限矩阵条件数约 2023.3543、线性残差约 `3.3766e−24`；H 修正采样最大
`1.71033854e−11`、导数修正 `4.573983e−9`。线性方程仍是普通浮点射线的
有限方程，不能由其小残差推出新真实返回的非线性残差。

对象文件 `type_fixed_step02_d5_exact_affine_step5_object.json` 的 SHA256 为
`91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`。
新 tight root 由数值代理对这个准确参数独立重跑，未转授 δ₄ 的根。

## 3. 新 H516 的准确整数证明

每个有限 Fourier 修正先视为准确 binary64 Fraction，与旧 H258 准确相加，
再一次取到分母 `2^120`；没有用采样 FFT 重新定义 H。
这次 C0/C1/C2 的系数舍入误差分子全部为零。
实际 H516 SHA256 为
`0439d88f10f46d367e44a984db661ac3806a7bd052f46eca14e71594fa8eb2c2`，
辅助 `_H_float_export.npz` 不是后续 H 的定义。

新 q1024 通过完整准确整数卷积、R48 有理指数 majorant 及 Neumann 逆：
宽度 1/512、1/256、1/128、1/64、1/32 均通过；实圆 H'>0 全部已证。
在 R63 使用的宽度 1/128，`||H'||<2.446326526`、
`||1/H'||<3.520010337`。另用原生 192-bit Arb 重算局部逆门，
扩大半径 1/1000 时 `κ<0.057574443`。
这证明有限 H 的输入条件，没有支付 δ₅ 的真实 E。

有限 predictor 的重跑：

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python scripts/fourfold_circle_exact_affine_newton.py --actual-nodes notes/2026-11-12-D5-exact-affine-step4-shared-knot-Hnodes1032.json --base-object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_object.json --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_dyadic_H.json --out notes/2026-11-12-D5-exact-affine-Newton1032-step5.json --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_H_float_export.npz --new-object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json

随后用 `fourfold_circle_exact_correction_budget.py`，指定 base 为 step4 dyadic H、
newton-report 为 Newton1032-step5，`--bits 120 --inverse-degree 1024`，
得到 step5 dyadic H 与其 Wiener budget；再用冻结的
`fourfold_circle_local_inverse_budget.py` 单独计算 step5 local-inverse budget。

## 4. 下一项的准确对象区别

δ₄ 原 trace、δ₅ 目标场、H516 新初值必须同时保留各自身份。
可以从原 trace 定义 δ₅ 的新参考函数，但它不是 δ₅ 的真实轨迹；
新参考的初值与时间接缝可准确检查，真正 δ₅ 的 e0/e1 仍须重新验证。
本次没有启动另一次长时间浮点射线，也没有修改旧 manifest 使它冒充同一对象。
