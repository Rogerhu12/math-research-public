# 精确 affine 第三点的 516 实际射线与节点分段残差试验

状态：**浮点数值证据**。这里固定明确的精确输入函数，计算本身仍不是有向 ODE 证明，也不是完成的 KAM 或曲面构造。

## 1. 对象及已完成的整圈图

对象是 `type_fixed_step02_d5_exact_affine_step3_object.json`（SHA256
`e6ff2d46ed2d321c1b287e6c9d8e44ead7b9a70523350d145d703b4edd6def0f`）。
它沿 R57 的同一实际 affine 控制点方向取

$$
\delta_3=-\frac{7832869216826619}{4611686018427387904}.
$$

先作精确 affine 加法，再施加明确的径向偶奇对称化，采用无限 R33 单位切向原函数；同步目标是此图自己的径向输出 $g_0(\delta)$。有限 FFT、浮点三角函数和近根积分商是本次数值评价的近似，不能因此改称精确曲面或精确返回图。

实际参数根证书 `type_fixed_step02_d5_exact_affine_step3_root_tight.json`
（SHA256 `afdc964a11682f9c54ceb1e6a165950f007ea26ab917f8dbde8b38c9fe78629f`）给出

$$
t\in[0.2383968737297366,0.23839687372974327].
$$

射线计算用其中的保存中心 `0.23839687372973994`，本节未支付中心与真实根的差。归一角坐标为 $x=4\theta$，精确 dyadic $H$ 的 SHA256 是
`028a95679f5c6e6ff6438b539c9c427f745f976a4dbc70b46c0bb01dd0f4fb49`。

`2026-11-12-D5-exact-affine-step3-Hnodes516.json` 的全部 516 节点和 24 个分支已完成；SHA256 为
`ffbf2e273a64ca5aa018fc189661d6e25d2c776978f63c0771024deb5445978a`。
采用 Q=256 四分之一周期节点、每组 43 条射线、DOP853 `rtol=2e-10`。记录：

| 量 | 浮点结果 |
|---|---:|
| $\max|R\circ H-H\circ T_\alpha|$ | $1.9977607301768785\cdot10^{-7}$ |
| $\max|(R\circ H-H\circ T_\alpha)'|$ | $1.8454208482898693\cdot10^{-5}$ |
| 平均 $E/H'_\alpha$ | $-2.5600689280094392\cdot10^{-8}$ |
| 平均实际参数列 $\partial_\delta R(H)/H'_\alpha$ | $0.0023071722119627535$ |
| RHS 调用 | 77088 |

这一步的参数列由真实 affine 方向和两端根移动的链式法则得到，不是把径向作用量导数替代旋转数导数；但有限节点的均值仍不是严谨的连续平均。上一精确 $\delta_2$ 点的 258 节点最大误差为 $7.895395647095071\cdot10^{-5}$。当前误差降低约 395 倍，仍需改善参考轨道的残差后才适合再作高精度 Newton。

完整重做入口（在本课题目录运行）：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_exact_affine_nodes.py \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json \
  --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_dyadic_H.json \
  --out notes/2026-11-12-D5-exact-affine-step3-Hnodes516.json \
  --trace-dir data/phase_ring_continuation/exact_affine_step3_dense516 \
  --rays 516 --block-size 43 --tolerance 2e-10 --resume
```

## 2. 浮点连续残差探针

`fourfold_dense_residual_probe.py` 对保存的每个 DOP853 多项式直接微分。
写参考角为 $Y$，参考对数权为 $L$，$q=e^L$，真实目标特征场为 $f$。它评价

$$
e_0=Y_\tau-f(\tau,Y),\qquad e_1=L_\tau-f_\theta(\tau,Y).
$$

每段使用两端和 8 点 Gauss 节点；下表中的积分都是逐射线绝对值 Gauss 求和再取最大值，**不是积分的有向上界**。$q$ 是保存多项式定义的参考权，不是已验证的真变分流。

| 首 43 条 forward | 段数 | $\max|e_0|$ 采样 | $\int |e_0|/q$ 估计 | $\int|e_1|$ 估计 |
|---|---:|---:|---:|---:|
| $\delta_2$, rtol $2\cdot10^{-9}$ | 141 | $1.5001383\cdot10^{-6}$ | $7.1403913\cdot10^{-8}$ | $1.6983561\cdot10^{-6}$ |
| $\delta_3$, rtol $2\cdot10^{-10}$ | 168 | $4.9514463\cdot10^{-7}$ | $1.9237399\cdot10^{-8}$ | $3.4695572\cdot10^{-7}$ |
| 同一 $\delta_3$、同容差、按径向节点重启 | 302 | $2.2308880\cdot10^{-9}$ | $4.6717092\cdot10^{-11}$ | $8.4230906\cdot10^{-9}$ |

同对象同容差的第三行比第二行降低了约 412 倍的 $e_0$ 积分估计、约 41 倍的 $e_1$ 积分估计。RHS 从 2978 增至 4950。两种积分的最终角最大差 $1.3766036088824762\cdot10^{-9}$，最终 $J$ 最大差 $2.9820616642695086\cdot10^{-8}$，最终实际参数列最大差 $1.7064711704253485\cdot10^{-11}$。这表明保存的多项式残差费用对时间分区敏感；不能仅凭解算器的 `rtol` 给出连续误差。

探针的输入可为一个 NPZ/GZ，也可为包含所有 accepted-step 小块的 `.trace.json`；后一种输入先核对 SHA、精确共享端点再拼接有限数组。重做当前改善例：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_knot_aligned_probe.py \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json \
  --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_dyadic_H.json \
  --trace-stem data/phase_ring_continuation/exact_affine_step3_knot_probe/block_0000_forward \
  --out notes/2026-11-12-D5-exact-affine-step3-knot-forward.json \
  --comparison-trace data/phase_ring_continuation/exact_affine_step3_dense516/block_0000_forward.npz.gz \
  --total-nodes 516 --first-node 0 --count 43 --tolerance 2e-10

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_dense_residual_probe.py \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json \
  --trace data/phase_ring_continuation/exact_affine_step3_knot_probe/block_0000_forward.trace.json \
  --out notes/2026-11-12-D5-exact-affine-step3-knot-forward-residual-probe.json \
  --quadrature-order 8
```

另两份探针把 trace 换成对应普通积分的首 forward NPZ.GZ；$\delta_2$ 一份还需同时换成其自己的 object 和 root certificate。三份已经完成的探针 JSON 保留源 SHA、输入 SHA、逐段结果以及采样/积分口径。

## 3. 为什么改变积分分区

相位和背景的真实样条节点都进入特征场。跨过节点的高次时间多项式可能遇到较高导数的接缝；按积分器自己的误差指标接受一个时间步，不会自动给出足够小的整个多项式微分残差。新 helper 收集 `phase_knots`、`base_knots`、`shift_knots`、`mean*_knots`、`height*_slope_knots`，把正侧 166 个 binary64 节点按 $10^{-13}$ 聚成 143 组，取每组首节点作积分网格代表。最大被合并宽度为 $1.3877787807814457\cdot10^{-16}$。

这只改变数值积分分区，完全不改变精确输入函数。每个代表映为 $\tau=\arcsin(r/t)$，加入反射节点和零点；每段独立 DOP853，保留全部 accepted steps、原始 dense 系数和共享状态。被合并的其他实际节点仍可能被跨过，故本试验**不宣称**各时间段都处在一个解析样条片内。后续有向残差证明必须使用真实源分区，或对剩下的极窄接缝另付误差。

全圈 `fourfold_phase_knot_aligned_nodes.py` 已启动同对象 516 点、rtol $2\cdot10^{-12}$，其 live 输出不属于本次冻结包。下一精确点宜使用全部射线共享的时间网格，并按 accepted steps 分块保存，减小 R61 全初值参考的分区并集与重复径向 FFT。

仍欠：连续复域残差、真实根误差、无限原函数与 FFT/三角函数舍入、完整参数 Taylor 预算及最终 PDE 逆。上述任一浮点改善都不授予这些结论。
