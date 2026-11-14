# 同一 exact-affine 对象的完整258射线与第三次有限共轭校正

2026-11-12。**浮点预测与有限多项式证书；没有接受为精确共轭。**
本笔记只记录已实际完成的258射线和由它定义的下一个候选。
第三点的516射线验证另存，冻结本笔记时仍在进行。

## 1. 第二点的完整实际射线

明确的 exact-affine 参数为
$\delta_2=-15291006546051/9007199254740992$，来源、对称化及无限
R33 定义见 recovered-exact-affine-evaluator 笔记。整组258节点都由
同一新对象、新 evaluator、新 root reference 重新积分；每个节点
同时保存实际 R、J 与解析参数列，包含移动两端点修正。

完整输出 `notes/2026-11-12-D5-exact-affine-step2-Hnodes258.json`，SHA
`7850b8382f131b630d0fa0f334243a470318b8526201c5e421b156853ba53c6f`。

| 量 | 浮点值 |
|---|---:|
| 最大实际共轭误差 | 7.895395647095071e-5 |
| 最大误差角导数 | .005103413076144481 |
| 加权误差均值 | -5.290989994468871e-10 |
| 加权实际参数 twist | .002307176314574598 |
| twist 被积函数采样范围 | [.0003104506877877996,.004413077210363075] |
| root 参数导数 | 6.110800296749722e-5 |

采样误差与 twist 不是 Wiener 范数或严格下界。完整 dense trace 的
目录为 `data/phase_ring_continuation/exact_affine_step2_dense258/`，
每个节点块的 accepted times、参考多项式及文件 SHA 均已保留。

## 2. 全258列的有限 Newton

新源 `scripts/fourfold_circle_exact_affine_newton.py` 直接使用这一
完整网格的 R/J/G。状态方程没有 circle-map 插值，参数列也没有
子集插值。初始 H 使用原 dyadic Fourier 系数，频率64严格低于
258格的 Nyquist；只把浮点求值差作为诊断记账。

对 $x=4\theta$、$\alpha=2\pi\rho_5$ 解有限系统
$$
J_i\Delta h(x_i)-\Delta h(x_i+\alpha)
 4R_\delta(H(x_i)/4)\,\Delta\delta=-E_i.
$$
常数规范通过参数圆预旋转处理。所得新 H 次数129，具体浮点
预测如下：

- $\Delta\delta=-8.400106236694943\times10^{-7}$；
- 保存的新准确参数为 binary64 `−.0016984827643356504`，即
  $\delta_3=-7832869216826619/4611686018427387904$；
- 线性剩余 $1.90\times10^{-19}$，矩阵条件数约1993.58；
- H 修正采样最大 $5.48908\times10^{-5}$，H′修正最大约 .00330712；
- 新 H′采样范围 [.3577276888,1.7751000175]。

参数加法最后一次 binary64 舍入的准确差已单独记入报告；新对象
仍按准确 $S_0+\delta_3V$ 定义，不预先舍入所有控制点。
这一步留在 R57 的准确参数管内，不需要另把 rounded 图当成子族。

报告 `2026-11-12-D5-exact-affine-Newton258-step3.json`，SHA
`98bf61c4411e6a15a7e5f3977ade67ac77fbbf51e97e5e05924983d759b9c48c`。
新对象 JSON SHA 为
`e6ff2d46ed2d321c1b287e6c9d8e44ead7b9a70523350d145d703b4edd6def0f`。

## 3. 新 H 的严格有限多项式输入与自身 root

新 H 的 dyadic 整数定义为
`type_fixed_step02_d5_exact_affine_step3_dyadic_H.json`，SHA
`028a95679f5c6e6ff6438b539c9c427f745f976a4dbc70b46c0bb01dd0f4fb49`。
按 R48 的准确整数卷积与有理指数预算重新认证，得到

| 归一化 x 角带 | $\|H'\|$ 上界 | $\|1/H'\|$ 上界 | reciprocal 乘积缺陷上界 |
|---|---:|---:|---:|
| 1/512 | 2.359262 | 3.424212 | 1.462e-14 |
| 1/128 | 2.446317 | 3.520125 | 1.102e-13 |
| 1/32 | 2.972412 | 4.028465 | 5.116e-9 |

这是整个实圆上的正导数证明和有限 H 的解析输入，不能替代共轭
方程的残差证明。实际物理角为 $\theta=x/4$，物理 H 为
$H_\theta(\theta)=H(4\theta)/4$；导数及其倒数界不变，角带宽度
除以4。

numerical 已在这个准确 $\delta_3$ 上独立重跑 interval Newton：
`type_fixed_step02_d5_exact_affine_step3_root_tight.json`，SHA
`afdc964a11682f9c54ceb1e6a165950f007ea26ab917f8dbde8b38c9fe78629f`。
根位于 [.2383968737297366,.23839687372974327]，reference center 为
.23839687372973994。此根属于 exact-affine 新点，不是旧 rounded 图。

## 4. 重做和继续入口

所有命令在课题目录。有限 Newton：

    OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
    python scripts/fourfold_circle_exact_affine_newton.py \
      --actual-nodes notes/2026-11-12-D5-exact-affine-step2-Hnodes258.json \
      --base-object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_object.json \
      --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_dyadic_H.json \
      --out notes/2026-11-12-D5-exact-affine-Newton258-step3.json \
      --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_H.npz \
      --new-object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json

新 H：

    OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
    python scripts/fourfold_circle_conjugacy_budget.py \
      --conjugacy data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_H.npz \
      --polynomials data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_dyadic_H.json \
      --out notes/2026-11-12-D5-exact-affine-step3-H-Wiener-budget.json \
      --inverse-degree 512 --width-denominators 512 256 128 64 32

独立的新516射线：

    OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
    python scripts/fourfold_phase_exact_affine_nodes.py \
      --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json \
      --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json \
      --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_dyadic_H.json \
      --out notes/2026-11-12-D5-exact-affine-step3-Hnodes516.json \
      --trace-dir data/phase_ring_continuation/exact_affine_step3_dense516 \
      --progress notes/2026-11-12-D5-exact-affine-step3-Hnodes516-progress.json \
      --rays 516 --block-size 43 --tolerance 2e-10 --resume

后续必须检查新实际节点的误差，继续付 R60/R61 的参考残差、复角
管、真实参数 Taylor 与 Wiener 费用。有限线性系统的微小剩余不能
被称为非线性接受，H 的正性也不是精确闭曲面等距族的证明。
