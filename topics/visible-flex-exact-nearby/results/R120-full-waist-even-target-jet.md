# R120 补篇：完整腰部偶对称对角目标二阶 jet

2026-11-13，newton_source。**准确恒等式及整个参数盒上的腰截面证书。**

本篇把 `R120-fixed-target-radial-sensitivity.md` 的单列检查扩为固定径向
对角目标在腰部的全部有效二阶自由度，保持实际嵌入不变。结论是：
即使允许任意改变角向目标分量的二阶径向导数，同时把两个目标值各改动
不超过 0.01，当前真实 source 在腰处仍严格大于 0.590232。
这缩小了可行下一步的选择：很小的固定目标调整本身不能消掉当前首轮源。
它不排除直接修正嵌入，更不表示课题中的精确族不存在。

## 1. 准确三列公式

固定当前 $F$、其真实球面拉回度量 $s$ 及 $a_s=\rho^2$。
为避免把材料半径和球面密度混淆，这里把材料半径记为 $a_0(r)$。
原目标是

$$
g_0=E(r)\,dr^2+G(r)\,d\theta^2,
\qquad G=a_0^2.
$$

考虑另一个预先选定的径向对角目标
$g_0+e(r)dr^2+g(r)d\theta^2$。腰反射要求 $e'(0)=g'(0)=0$。
记

$$
A=-\tfrac12\mathcal C_s(a_sdr^2),\qquad
B=-\tfrac12\mathcal C_s(a_sd\theta^2),\qquad
C=\frac{a_s}{2\det s}>0.
$$

则在 $r=0$ 上有**准确**恒等式

$$
\boxed{q_{\rm new}=q+A\,e(0)+B\,g(0)+C\,g''(0).}
\tag{120W.1}
$$

特别没有 $e''(0)$ 项。这是 source 对目标的线性关系，不是忽略了高次项
的扰动展开。保持正度量的改变任意大时，恒等式仍成立。

证明：使用 R120 径向敏感度篇中的张量乘法公式。在腰处一阶径向导数为零，
所以乘法产生的附加项只来自 $\nabla_s^2e=e''dr^2$ 和
$\nabla_s^2g=g''dr^2$。$e''$ 的系数为
$a_s((s^{rr})^2-(s^{rr})^2)=0$。$g''$ 在兼容算子中的系数为

$$
a_s\{(s^{r\theta})^2-s^{rr}s^{\theta\theta}\}
   =-\frac{a_s}{\det s}.
$$

乘上 $-1/2$ 即给 $C$。全部零阶密度、球面连接项已包含在 $A,B$ 中。
令 $\xi=dx$、$H=\nabla_s^2x$、$\tau=\operatorname{tr}_sH$、
$n=|dx|_s^2$、$Z=\tau dx-H(\nabla_sx,\cdot)$，其中 $x=r$ 或局部角坐标
$x=\theta$。两列分别用

$$
\mathcal C_s(a_sdx^2)
=a_s(\tau^2-|H|_s^2-2n)
 +2\langle da_s,Z\rangle
 +\nabla_s^2a_s:dx^2-(\Delta_sa_s)n
\tag{120W.2}
$$

直接计算，只需要当前二阶几何。角坐标只用于局部恒等式；$d\theta$ 和
全部系数在材料圆上周期匹配。

## 2. 两角严格消去任意二阶目标改变

令 $\widehat q=q/C$、$\widehat A=A/C$、$\widehat B=B/C$。
对任意两个材料角 $\theta_+,\theta_-$，(120W.1) 给

$$
\frac{q_{\rm new}(\theta_+)}{C(\theta_+)}
-\frac{q_{\rm new}(\theta_-)}{C(\theta_-)}
=\Delta\widehat q+e(0)\Delta\widehat A+g(0)\Delta\widehat B.
\tag{120W.3}
$$

任意大的 $g''(0)$ 在这里准确抵消。如果右边对所有允许改变均大于 $L>0$，
三角不等式立即给

$$
\|q_{\rm new}\|_\infty\ge
\frac{L}{C(\theta_+)^{-1}+C(\theta_-)^{-1}}.
\tag{120W.4}
$$

程序用完整角格的区间值选择格编号 0 与 262（共16384格），再对所有
$e(0),g(0)\in[-\varepsilon,\varepsilon]$ 作外向区间计算。
选择角格只影响证书强弱，不是额外假设。每个格内所有真实角、全部
$\eta=10^{-9}$ 参数都被包住，故选其格中心也可直接使用 (120W.4)。
结果如下；表中数值向下截短。

| $|e(0)|,|g(0)|\le\varepsilon$ | $g''(0)$ | 任意改变后的 $\|q_{\rm new}(0,\cdot)\|_\infty$ 下界 |
|---:|---|---:|
| $10^{-4}$ | 任意实数 | 0.6046464976 |
| $10^{-3}$ | 任意实数 | 0.6033361464 |
| $10^{-2}$ | 任意实数 | 0.5902326350 |

全部三列的完整角向 $C^0$ 上界分别小于

$$
\|A\|_\infty<7.019911,\qquad
\|B\|_\infty<2.016467,\qquad
\|C\|_\infty<0.472695.
$$

## 3. 实际候选选择及重新验证

程序还在512个角格中点的浮点数据上解三列 minimax 线性规划，
把选出的三个改变冻结为确切二进有理数，再使用16384个完整角格、
完整 Fourier 余项和整个参数盒重新计算。浮点 LP 仅选择候选，
不证明全局最优性。

| 选择范围 | 验证的实际候选 source 上界 |
|---|---:|
| 两个目标值各改变至多约 $10^{-3}$ | 0.613909 |
| 两个目标值各改变至多约 $10^{-2}$ | 0.601362 |
| 宽正性范围 | 0.570012 |

由于 `float(1/1000)` 等是二进有理数，前两行的确切候选极微小地越过
十进制端点；它们的精确分数以报告为准。上节的**所有改变下界**使用
确切有理预算 $1/1000$、$1/100$，不受候选选择的端点表示影响。
宽范围候选在腰处给新目标值约
$E_{\rm new}=1.201705472575$、$G_{\rm new}=0.946696870691$，都严格正。
原目标值为 $E\approx1.229138831253$、$G\approx1.142189864049$。

这里只评估可能目标的腰部二阶 jet，没有安装新的全局目标，
也没有迁移 R101/R111/低块等属于原目标的返回或强逆证书。

## 4. 输入、算术及重跑

源码：`scripts/fourfold_phase_newton_target_full_waist_jet.py`，SHA256
`4ce3f0dbf0c08f2c7825dd151ea1a6f5da2d33a14052459181b4cdbc9ce7934b`。

报告：`notes/2026-11-13-newton-target-full-waist-jet-native.json`，SHA256
`1216f0c5480615361591ab397352051f0eb6aa04b7894b05c00799b3073b7630`。

报告含实际对象、origin、direction、中心参数及 $\eta$ 的确切值和输入 SHA。
它调用 R120 已证明的 centered Fourier 完整误差算法（同一个冻结源码 SHA），
512个 primitive 节点、4096乘积网格、16384完整角格及192-bit Arb。
此次 native 运行228.83秒，包含三个浮点 LP；没有用 LP 的容差作任何严格证明。

```sh
python scripts/fourfold_phase_newton_target_full_waist_jet.py \
  --out notes/2026-11-13-newton-target-full-waist-jet-native.json
```

本篇只涉及腰截面。完成整个近似嵌入的实际修正、估计材料方向上的
$C^0/C^1$ 和分量 Hessian、控制更新后的 source，仍是后续任务。
