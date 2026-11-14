# 准确仿射族的全核心标量门（恢复后重跑）

状态：执行器更换后从同一准确输入完整重跑，源码 SHA 与原版相同，
完整 JSON 的 SHA256 亦与丢失前完全一致。不是从历史汇总数字补造证书。

对 R57 准确仿射族的全部 $|\delta|\le\operatorname{binary64}(.01)$、
$|x|\le\operatorname{binary64}(.24)$ 及全部实角，同时有

$$
Q=F_z/x>.94482899,\qquad F_{x,z}>.94266632,
\qquad |F_\theta\times F_x|>.85549055.
$$

$Q$ 在腰圈取准确连续延拓。此结论属于该族，不借用其他候选的常数。

## 1. 准确对象和全域界

原点 `type_fixed_step02_d5_jet_interval_inputs.npz` SHA256：

`0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`。

方向 `type_fixed_step02_d5_actual_parameter_direction.npz` SHA256：

`8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab`。

原始 phase 控制与 mean 系数准确取 $c_0+\delta v$、$\alpha_0+\delta w$，
然后施加固定 base 物理权重。$a,\beta$ 显式取偶部，$Z,\gamma$ 取奇部；
$Z$ 为准确 slope 积分，角向为真实无限 R33 原函数，未作 Gaussian 卷积。

原相位和方向的样条导数控制凸包分别计算，再使用
$|S_0^{(j)}+\delta V^{(j)}|\le\sup|S_0^{(j)}|+\delta_{\max}\sup|V^{(j)}|$。
物理权重后在整个对称核心取逐模最大值，显式平均不增加这些全局界。
mean/height knots 的准确反射与相等性由程序检查；相位原 knots 不必准确
反射。控制盒相关性损失仅使界变宽，不改变实际仿射对象的定义。

| 连续量 | 全参数 / 核心安全界 |
|---|---:|
| $Q$ | $>.94482899$ |
| $F_{x,z}$ | $.94266632<F_{x,z}<1.36028720$ |
| 面积因子 | $.85549055<\mathrm{area}<8.12409566$ |
| $|Q_x|$ | $<5.98296281$ |
| $|Q_\theta|$ | $<.41699773$ |
| $\|\gamma\|_\infty$ | $<.02353495$ |
| $\|\gamma_x\|_\infty$ | $<.37935966$ |

## 2. 无角采样的解析证明

四重垂直零均值原函数范数为 $\pi/8<11/28$，全向量范数为
$\pi/2<11/7$。由准确径向奇性，

$$
\frac{P_\theta\sin\gamma(x)}x
=\int_0^1P_\theta(\cos\gamma\,\gamma_x)(tx)\,dt.
$$

因此 $Q\ge\inf Z'-(11/28)a_+g_1$，其中 $g_j$ 为 $\gamma$ 的
第 $j$ 阶径向导数上界。另有

$$
|F_{x,z}-Z'|\le(11/28)(|a'|g_0+a_+g_1),
$$

$$
\|F_{x,h}\|\le(11/7)\{|a'|+a_+(\|\beta_x\|+g_0g_1)\}.
$$

因 $\|T_h\|=|\cos\gamma|\ge1-g_0^2/2$，叉积三角不等式给

$$
\|T\times F_x\|
\ge (F_{x,z})_-(1-g_0^2/2)-g_0\|F_{x,h}\|_+.
$$

先验证所有正乘积因子，再逐次向下舍入，并乘正半径下界，得到面积门。
没有用上界乘法代替下界。$Q=\int_0^1F_{x,z}(tx)dt$ 给
$|Q_x|\le\|F_{xx,z}\|/2$；实现保留全部 $a''$、$2a'\gamma_x$
和 $\gamma_{xx},\gamma_x^2$ 项。$Q_\theta=a\sin\gamma/x$ 给
$|Q_\theta|\le a_+g_1$。上述式子同时覆盖腰圈的可去奇点。

整个证明只用样条凸包和向外算术，不使用角节点值或有限 Fourier
原函数，所以此门不存在另欠的角截断尾。

## 3. 冻结与重放

源码 `scripts/fourfold_phase_affine_scalar_gate.py` SHA256：

`2b1fc7dd1ac47da22669ecf46f1dd1f75d3b8f372560eca4c00ddd68e12a0e65`。

报告 `data/phase_ring_continuation/type_fixed_step02_d5_affine_core_scalar_gate.json`
重跑 SHA256：

`d59cddb24b41f0d3862472785ad14da428b07b91944b065349c107486afb6c8c`。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_affine_scalar_gate.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --frozen-direction topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz \
  --parameter-left -.01 --parameter-right .01 --core .24 \
  --out /tmp/visible-D5-affine-core-scalar-gate.json
```

此门不单独证明 $N<0$、支持函数/$\zeta$ 正性、复管、目标型别或真实
返回，不向 rounded predictor 或更大独立控制盒转移结论，也不是精确
等距方程、正帽或闭合族的完成声明。
