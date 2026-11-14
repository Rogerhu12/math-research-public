# 显式对称图的连续核心标量与面积门

状态：**已付全区间 $|x|\le1/4$ 的 $F_z/x>0$、$F_{x,z}>0$ 与
面积元正下界；不以此宣称 $N<0$、支撑函数正或等距方程成立。**

## 1. 同一精确对象与结果

对象与 `2026-11-12-symmetric-root-interval.md` 完全一致：从
`type_fixed_step02_analytic_smoothing_inputs.npz` 的二进制实数系数定义
物理相位及半径，显式取 $a,\beta$ 偶部、$Z,\gamma$ 奇部；$Z$ 是
冻结 slope 的精确积分。曲面是无限角原函数
$F=aP_\theta T+Ze_z$。这里没有 Gaussian 平滑，也不把原始 NPZ 的
近似反射等同于精确反射。

对**所有** $|x|\le.25$ 和实角 $\theta$，有向计算给出：

| 连续量 | 已付界 |
|---|---:|
| $a$ | $1.0688508059201285\le a\le1.1016516225597952$ |
| $Z'$ | $1.1088993307098116\le Z'\le1.200467817424658$ |
| $F_z/x$（零点取连续延拓） | $>.9447694241408142$ |
| $F_{x,z}$ | $>.9425536531736881$ |
| $|T\times F_x|$ | $>.7948727797455405$ |
| $|F_\theta\times F_x|$ | $>.8496004112349936$ |
| $|F_\theta\times F_x|$ | $<8.156318417184573$ |
| $|\partial_x(F_z/x)|$ | $<5.955508933332260$ |
| $|\partial_\theta(F_z/x)|$ | $<.4177852167210838$ |

这些保守界覆盖已认证根 $t\in[.2383698,.2383701]$ 及其半径
$1/4096$ 的实 collar。它们不是离散径向或离散角节点的最小值。

## 2. 不用角采样的证明

对周期 $L$ 的零均值向量函数，零均值原函数算子的圆卷积核是
中心化锯齿，其 $L^1$ 范数为 $L/4$。所以本图的竖直分量（周期
$\pi/2$）及全笛卡尔向量（周期 $2\pi$）满足

$$
\|P_\theta f_z\|_\infty\le\frac\pi8\|f_z\|_\infty
 <\frac{11}{28}\|f_z\|_\infty,
\qquad
\|P_\theta f\|_\infty\le\frac\pi2\|f\|_\infty
 <\frac{11}{7}\|f\|_\infty.
$$

系数支撑凸包给出 $A_j\ge\|a^{(j)}\|_\infty$、
$B_j\ge\|\partial_x^j\beta\|_\infty$、
$G_j\ge\|\partial_x^j\gamma\|_\infty$。
物理相位的 $a_{\rm base}^3$、$a_{\rm base}^2$ 权在求导后逐项计费。
每个相位 spline 的原 knots 均进入正负两侧共同分割，共 300 个区间；
之后才使用全域上界说明显式偶奇平均不增加这些范数。

记 $z_-\le Z'\le z_+$、$p=11/28$、$q=11/7$。因为
$\gamma(0,\theta)=Z(0)=0$，对 $x\ne0$ 有

$$
\frac{F_z}{x}=\frac Zx+aP_\theta\frac{\sin\gamma}{x}
\ge z_--pA_0G_1.
$$

同一不等式在 $x=0$ 由连续性成立。进一步

$$
\begin{aligned}
v_-&=z_--p(A_1G_0+A_0G_1)\le F_{x,z},\\
|F_{x,h}|&\le H=q[A_1+A_0(B_1+G_0G_1)],\\
|T_h|&=\cos\gamma\ge c=1-G_0^2/2,\quad |T_z|\le G_0.
\end{aligned}
$$

认证 $v_-,c>0$ 后，水平叉积及反三角不等式给出

$$
|T\times F_x|\ge v_-c-G_0H>0,
\qquad |F_\theta\times F_x|=a|T\times F_x|.
$$

这里下界中的正乘积向下舍入；损失项向上舍入。面积上界使用
$a(|F_{x,h}|+|F_{x,z}|)$。

令 $Q=F_z/x=\int_0^1F_{x,z}(tx,\theta)dt$。利用

$$
\|F_{xx,z}\|\le\|Z''\|+
p[A_2G_0+2A_1G_1+A_0(G_2+G_1^2)]
$$

得到 $\|Q_x\|\le\frac12\|F_{xx,z}\|$。而
$\partial_\theta F_z=a\sin\gamma$，故 $\|Q_\theta\|\le A_0G_1$。
这也说明 $Q$ 的腰圈连续延拓不依赖除零数值技巧。

## 3. 重放与边界

从仓库根运行：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_core_scalar_gate.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz \
  --core .25 --out /tmp/visible-core-scalar-gates.json
```

永久报告为
`data/phase_ring_continuation/type_fixed_step02_core_scalar_gate.json`。
报告记录源、三依赖和原 snapshot 的 SHA256；输入 SHA256 是
`bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532`。
只假定 IEEE binary64 的基本四则正确舍入，下一浮点数向外包络；
没有用浮点三角、FFT 或样本最小值代替连续界。

下一项仍须独立验证同一图的 $N<0$ 与正支撑函数。上述面积门只提供
定义单位法向的分母下界，不将它偷换成这些额外几何符号条件。
本报告也不覆盖新 D5/D8 参数试图、全体 cap 或闭合等距族。
