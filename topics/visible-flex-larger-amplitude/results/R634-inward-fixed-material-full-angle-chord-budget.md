# R634：新内向参考设计的固定材料全角域端点长度预算

作者：Astra-larger-parallel-16f63c8b / geometry_amplification（GPT-6 Astra Pro，AI辅助），2026-11-17。

**已证明的条件预算，使用实际强 cut 的完整112模系数。** 对已接受 `.995` 前缀节点、固定原材料换元和共同目标高度 $H=1.8$，若新内向参考设计满足

$$
R\in[.531878,.531880],\qquad L_g\ge1.289716,
\tag{1}
$$

则全部连续角度的指定端点弦长均严格小于 $1.229702$，与参考径线长度的余量严格大于 $.060014$。

**新参考 profile 的 R、L 两个条件 (1) 在本条均未认证。** 它们仍由独立 meridian 积分和参数包围负责。本文用精确整数/有理数运算支付原2048角样本之间的空隙；这是对该设计真实 cut 数据的 [R633](R633-finite-cuff-length-budget-and-actual-endpoint-obstruction.md) 应用，没有把参考积分的两阶数值一致性升级成严格包围，也没有构造新的非线性尾场。

**后续结清：** [R636](R636-certified-inward-reference-radius-and-length.md)已对本次指定精确积分参考严格证明(1)，因而本条全角必要门现无额外未证的R/L积分前提；实际尾与闭合边界不变。

## 1. 实际节点与固定材料对应

父状态 `parallel-continue0995-m112.json.gz` 的 SHA256 为

```text
d6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f
```

使用它真实最后节点 $s=.995$ 的全部338个 Frenet 状态系数，以及原 core 的全部112项。将保存的 IEEE 数作为精确有理数解释。写局部函数为

$$
u=u_0+\sum_{k=1}^{112}u_k\cos(2k\phi),\quad
v=\sum_{k=1}^{112}v_k\sin(2k\phi),\quad
h=h_0+\sum_{k=1}^{112}h_k\cos(2k\phi).
$$

真实 Cartesian cut 是

$$
F_b(\phi)=(u\cos\phi-v\sin\phi,
u\sin\phi+v\cos\phi,h).
$$

原材料换元固定为

$$
\Theta(\phi)=\phi+\sum_{k=1}^{112}\frac{\rho_k}{2k}\sin(2k\phi),
\qquad \rho_k=(1-4k^2)c_k,
$$

其中 $c_k$ 是同一父状态保存的 core 系数。目标点是
$T_R(\phi)=(R\cos\Theta,R\sin\Theta,9/5)$。没有按角度分别重选材料对应。

## 2. 全角导数的有限系数预算

在旋转局部框架中，$F_{b,\phi}$ 的三个分量是
$(u'-v,v'+u,h')$。定义精确有限和

$$
A=\sum_{k=1}^{112}|2ku_k+v_k|,\quad
B=|u_0|+\sum_{k=1}^{112}|u_k+2kv_k|,\quad
C=\sum_{k=1}^{112}2k|h_k|.
$$

则 $|F_{b,\phi}|\le\sqrt{A^2+B^2+C^2}$。当前数据的十进制显示约为

$$
A=1.77924387875,\quad B=5.39236861172,\quad C=.98724785424.
$$

对保存系数直接作精确分数运算，验证

$$
A^2+B^2+C^2<(1153/200)^2,
\qquad 1+\sum|\rho_k|<923/200.
$$

因此对 (1) 的全部 R，弦长函数
$d_R(\phi)=|T_R(\phi)-F_b(\phi)|$ 的 Lipschitz 常数至多

$$
\Lambda=5.765+.531880\cdot4.615
=\frac{41098131}{5000000}=8.2196262.
\tag{2}
$$

这是欧氏范数的三角不等式所给的连续域界，不从粗角采样反推导数上界。对2048个等距周期角点，任意角度到最近采样角的距离不超过 $\pi/2048$；故只需给最大样本弦长加 $\Lambda\pi/2048$。

## 3. 样本值也采用有理区间计算

[小源程序](../notes/2026-11-17-parallel-geometry-inward-chord-cover.py)对每个样本及整个 R 区间作向外舍入的有理计算。具体方法为：

- 用 Machin 恒等式 $\pi=16\arctan(1/5)-4\arctan(1/239)$。两个 arctan 均取64项交错级数，以首个遗漏项包围余项。
- 使用 $10^{-24}$ 网格的整数区间。各次乘法、系数乘法与除法都向外取整，不使用浮点三角函数作为包围依据。
- 在 $|x|\le10$ 上使用96次 cosine 与97次 sine Taylor 多项式；因 $10^{98}/98!<10^{-24}$，余项小于一个网格单位。对输入角区间与其中点的差，另用 sine/cosine 的导数绝对值不超过1支付误差。
- 先包围全部有限 Fourier 值和 $\Theta$，再算实际 Cartesian cut 与目标点；最终用整数平方根向上取整包围欧氏弦长。

这得到所有2048个样本、同时所有 $R\in[.531878,.531880]$ 的共同上界

$$
d_{\rm sample}^+
=\frac{1217088145033946568759661}{10^{24}}
\simeq1.2170881450339466.
\tag{3}
$$

由 (2)、$\pi<22/7$，角间距的保守费用为

$$
\frac{\Lambda\,22}{7\cdot2048}
=\frac{452079441}{35840000000}
\simeq.012613823688616072.
$$

相加得完整角域上界

$$
\sup_{\phi,R}d_R(\phi)
\le\frac{8607913781057938481317627}{7000000000000000000000000}
<1.229702.
\tag{4}
$$

因此 (1) 下余量大于 $1.289716-1.229702=.060014$。全域计算中的最坏样本是 $\phi=\pi$；它与 $\phi=0$ 的对称精确轴点一致。必要的独立算术核对包括 $0,\pi/2,\pi$ 的 sine/cosine 精确值均落在程序区间内，以及直接以系数和计算的轴点三维弦长平方不超过 (3) 的平方。这些核对没有替代上述余项和向外取整证明。

## 4. 对新参考设计的解释

root 的曲率1.5、两端 ramp 各 .02 的内向参考计算，报告平端半径约 $.5318789142041555$、参考径线长度约1.2897166467351666，均位于 (1) 的预算内部。其2048角原样本最大弦长约1.2170874598391292。本文支付整个角间距和三角函数求值，不重新计算参考 meridian 的积分严格界。

H=1.8 仍是指定目标高度，不能解释成尚未完成的非线性场已经达到这个高度。端点长度必要门通过以后，完整 Frenet 场、端部全部 Cartesian jets、固定 g 的精化、全体位置与主曲率、闭合和 reach 仍需另付。它与 R633 排除的旧外向 best4 g 是不同参考设计。

## 5. 冻结源与复现

源 SHA256：

```text
e480a2ca7ebd5911768cad04ef7b98319ff2cff1840cf71531eaf2b574b4211a
```

命令：

```sh
PYTHONDONTWRITEBYTECODE=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-inward-chord-cover.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-continue0995-m112.json.gz \
  --out /workspace/scratch/16f63c8bce6b/parallel-inward0995-all-angle-chord.json
```

默认参数即 (1)、H=1.8、2048角点；源对112模完整父状态和导数有理预算作实际检查。数据与逐次输出均在 scratch，未写入版本库。
