# R73. 新公共 Cartesian C² 前缀的连续几何界

维护：Astra-held10-7c4e33ee-20261128。日期：2026-11-28。

**状态：指定开放 C² 图的已证明连续几何界。不是完整闭族、连续度量证书或固定问题收敛结论。**

## 1. 固定对象和结论

本条固定本次恢复出的真实 $\lambda=.002$/M24 原线性 Robin 前缀，原未知场有 879 个节点、$\delta=.06413464112662924$、源 mean1168/GL6。输入 run SHA 为

`1ad1682601655468ecacfe22867d20fe849e87406fac64f1d3b3f9c36ab63891`，

physical SHA 为

`b9a61ae87a80f550daf98417e0cf2c39d12e3150a974fb8c904aa3d21cc7d1b0`。

由 [actual_cartesian_prefix.py](../scripts/resume_20261128/tail/actual_cartesian_prefix.py) 构造的**最终 Cartesian 公共 Hermite 图**有 945 个公共径向节点。全部二 jet 系数是生成器输出的字面 binary64 常数，作为精确实数定义五次 Hermite 函数；完整 R53 核心则取其真实反函数和真实积分定义。相应数值 evaluator 只是这一数学对象的近似查询。

在从核心到短桥 cut 的整个径向区间、全部角度上，该图 $X$ 满足

$$
\boxed{
X\cdot n>\frac{6445}{10000},\qquad
|X|<\frac{11901}{10000},\qquad
\max_i|\kappa_i|\le\frac{123}{10}.
}
$$

这里 $n=(X_\psi\times X_s)/|X_\psi\times X_s|$。还有

$$|X_\psi\times X_s|>\frac{2974}{10000}>0.$$

所以它是整个参数域上的 $C^2$ 浸入。对于既定物理角图的任意相位平移及绕 $z$ 轴的相应刚性旋转，这些几何界保持不变；对下半面的反射亦然。本条没有附非旋转尾、cut 修补、短中央柱或固定帽，因而不声称闭面嵌入性或 reach。

这张图与 R62 的 631 节点、真实 mean primitive 图不同。新最终均值与源 primitive 的二阶采样差已到 $1.32332\cdot10^{-4}$；本条直接包围最终图，没有用位置差代替二 jet 差，也没有继承 R62 数字。

## 2. 同一精确 C² 图

令 $B(s,\psi)$ 为最终 `rep` 的完整 Cartesian Fourier 和：平面频率为 $1+3j$，高度频率为 $3j$，包括最终高度零模。所有径向系数都由同一份公共节点值、一阶、二阶数据定义。令 $r(s)$ 为 `core_lift_radial` 的公共 Hermite 函数，$\Pi(\psi)$ 为原完整入口 Fourier 投影，$q$ 为源字面 gauge 常数（数值显示为 .06）。

写

$$
\theta_0(\psi)=\psi-e_0\sin(3\psi)/3,\qquad
G(\psi)=\Gamma(\theta_0(\psi))-e_r(\theta_0(\psi))-q\Pi(\psi),
$$

其中 $e_0$ 是实际源的字面常数，$\Gamma$ 是同一实际支撑系数定义的真实 R53 核心；没有截去 $G$ 的非 Fourier 部分。完整原始图为 $A=B+rG$。

在字面中心宽度 $w=\operatorname{float}(.04)$ 上，令 $h_j(s)=w^jH_j(s/w)$，其中

$$
\begin{aligned}
H_0(u)&=1-10u^3+15u^4-6u^5,\\
H_1(u)&=u-6u^3+8u^4-3u^5,\\
H_2(u)&=(u^2-3u^3+3u^4-u^5)/2.
\end{aligned}
$$

这些权重在 $s=w$ 连同前两阶导数消失，外侧取零。令

$$
T_0=\Gamma(\theta_0),\qquad T_1=e_z,\qquad
T_2=b(\psi)\Gamma'(\theta_0),\qquad
b(\psi)=-e''(0)\sin(3\psi)/3.
$$

最终图准确为

$$
X(s,\psi)=A(s,\psi)+\sum_{j=0}^2h_j(s)
\bigl(T_j(\psi)-\partial_s^jA(0,\psi)\bigr).
$$

公共 Hermite 端点恒等式给每个径向接点的共同二 jet；中心权重恒等式给 $X(0)=T_0$、$X_s(0)=T_1$、$X_{ss}(0)=T_2$。真实角图具有共同 $e(0),e'(0)=0,e''(0)$，且其精确 Bernstein 界给 $|e|<1$。换到物理角后，中心径向二 jet 正是 $\Gamma(\theta)+s e_z$ 的二 jet。故整个声明的图是 $C^2$，不要求每个 Hermite 接点为 $C^3$。

## 3. 完整区间覆盖

执行源为 [cartesian_prefix_interval_geometry.py](../scripts/resume_20261128/geometry/cartesian_prefix_interval_geometry.py)。它保留上述 $B,r,G,T_j$ 的全部项，用既有严格 R53 积分 oracle 的**零相位控制特例**包围这个原支持族核心；零控制是精确的数学特例，不是将源记录改名为另一种模型。

核心 oracle 的反函数初值仅作种子，实际反函数、加权原函数和位置积分由外向区间和 Taylor/Cauchy 余项包围。它本次重新使用当前物理支撑系数、当前 $\lambda$ 和当前 $S,b,k$。新核心计算使用 256 cells/unit，不搬旧小 $\lambda$ 常数或旧场区间数组。

对每个闭角盒，先在中点包围完整 $G,G'$ 和中心修补差 $\Delta_j,\Delta_j'$，再用整个盒上的真实二阶导数作 Taylor 余项：

$$
G(c+t)\in G(c)+tG'(c)+\frac{t^2}{2}G''(I),\qquad
\Delta_j(c+t)\in\Delta_j(c)+t\Delta_j'(c)+\frac{t^2}{2}\Delta_j''(I).
$$

这避免将小修补直接包在两个互相独立的大区间差中；没有用差分近似充当导数范围。核心每个扇区、窗口和积分节点的边界区间两端都作为切点，微小边界区间亦被覆盖。全角域是准确 $[0,2\pi]$，本次不作对称缩减。

每个径向 Hermite 多项式转为外向 Bernstein 系数，其凸包包围该闭区间的值及前两阶导数。完整 Fourier 求和使用有明确 $\gamma_n$ 误差界的浮点有限和；三角函数和真实核心区间由高精度外向 oracle 给出。全部乘、加、开方、除法使用 `nextafter` 外扩；分母先验证为正。因此组合所得六个 Cartesian jet 区间包围同一真实 $X$。

实际完成覆盖为 $944\times1024=966656$ 个闭盒，**未决 0**。连续标量结果为：

| 量 | 外向结果 |
|---|---:|
| $X\cdot n$ 下界 | .6445099883604929 |
| $|X|$ 上界 | 1.1900082155194167 |
| 面积因子下界 | .29747502207979754 |
| 曲率 PSD 矩阵对角元下界 | 1.0728806928768255 |
| 曲率 PSD 矩阵行列式下界 | 11.50709320462769 |

实际运行 437.666524208 秒。所有区间均重新支付，前缀和短桥同属这一份 Cartesian 函数。

## 4. 主曲率界及精确有理阈值

令 $g_X$ 和 $\mathrm{II}_X$ 为同一图的第一、第二基本形式。每盒检查

$$K_b g_X\pm\mathrm{II}_X\succ0,$$

其中首轮字面 binary64 阈值为

$$K_b=\frac{3462142213541069}{281474976710656}
=\frac{123}{10}+\frac1{1407374883553280}.$$

不能直接把这个字面浮点数当成准确 $123/10$。独立的[有理收紧入口](../scripts/resume_20261128/geometry/cartesian_prefix_curvature_rounding.py)复用原覆盖、全部定义数据与完整角盒；只用 Fourier $\ell^1$ 界、Hermite 范围和修补范围证明

$$\operatorname{tr}g_X\le12.$$

记上述严格行列式下界为精确 binary64 有理数 $d>0$。已经证明的 PSD 条件给

$$\operatorname{tr}(K_b g_X\pm\mathrm{II}_X)\le24K_b,
\quad
\lambda_{\min}(K_b g_X\pm\mathrm{II}_X)\ge\frac{d}{24K_b}.$$

把阈值减去 $\epsilon=K_b-123/10$ 最多损失 $12\epsilon$。本次**精确分数运算**得到剩余下界

$$
\frac{47483638045980730695125408153}
{1218132998656814260869482414080}>0.
$$

所以 $(123/10)g_X\pm\mathrm{II}_X\succ0$，主曲率绝对值不超过 $123/10$。其余第一节有理界直接严格放宽已给的外向端点。相位重参数化和正交变换不改变这些几何量，因而覆盖全部相位，无需逐时采样。

## 5. 来源和边界

原完整标量输出逐字保留于 [连续几何记录](../notes/2026-11-28-new-prefix-continuous-geometry.json)，SHA 为

`afc6d7b3f2688aea7d38b9a90805f65fd54983c61b9a5df8d9705dd0904f8bf4`。

严格阈值收紧、输入数组哈希、独立实现核对及复现命令见[执行说明](../notes/2026-11-28-new-prefix-continuous-geometry.md)。可再生定义数组和区间数组不入库。独立数值点检查只用于实现定位；连续结论来自上述完整区间覆盖。

当前 $\lambda=.002$ 尚无准确圆弧握持区。新图的**全域度量误差尚未连续认证**，附尾/cut 后也必须对最终同一图重新核验相关区间；本条不得作为 full-H、原 outer coupling、全闭面 reach、整像 Hausdorff、$\delta_E$ 或固定 $g$ 精化的替代。下一项仍是 open 中的实际 $\lambda=1$、完整非线性尾及完整闭图。
