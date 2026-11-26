# R238：任意非正交端切向的空间曲线长度必要界

日期：2026-11-26。会话：Astra-visible-flex-6a65e705。

本条扩展 [R212](R212-spatial-meridian-length-bound-without-reflection.md) 的正交端切向情形，支付任意非正交端切向下的空间曲线投影积分界。曲线可离开端切向平面或绕行；不假设单调转角。准确同一度量曲面的测地经线可以消费已经证明的曲率界，有限度量误差场不能直接套用。

## 1. 不要求空间曲线平面的端切向式

令 $\gamma:[0,L]\to\mathbb R^3$ 为单位速 $C^{1,1}$ 曲线，$T=\gamma'$，并假设

$$
 |T'|\le R^{-1}\quad\text{几乎处处},\qquad
 d=\gamma(L)-\gamma(0),\quad T(0)=T_0,\quad T(L)=T_1 .
$$

对任意单位向量 $v$，记

$$
 \alpha_i=\arccos(v\cdot T_i)\in[0,\pi].
$$

若 $L\ge R(\alpha_0+\alpha_1)$，则

$$
 \boxed{\quad L\ge v\cdot d+
 R\bigl(\alpha_0+\alpha_1-\sin\alpha_0-\sin\alpha_1\bigr).\quad} \tag{1}
$$

**证明。** 球面切向路径的长度不小于球面距离，所以

$$
 \operatorname{dist}_{S^2}(T(s),T_0)\le s/R,\qquad
 \operatorname{dist}_{S^2}(T(s),T_1)\le(L-s)/R.
$$

球面三角不等式给

$$
 \angle(v,T(s))\ge\max(0,\alpha_0-s/R),\qquad
 \angle(v,T(s))\ge\max(0,\alpha_1-(L-s)/R).
$$

因此在 $0\le s\le R\alpha_0$ 上，
$v\cdot T(s)\le\cos(\alpha_0-s/R)$；在
$L-R\alpha_1\le s\le L$ 上有对应的末端式；其他地方用
$v\cdot T\le1$。两段在所声明条件下不重叠，积分得到

$$
 v\cdot d
 \le R\sin\alpha_0+L-R(\alpha_0+\alpha_1)+R\sin\alpha_1,
$$

即 (1)。证明对任意空间切向路径成立，允许离开端切向张成的平面，也允许绕行；没有假设单调转角。证毕。

对任意 $v$ 使用 (1) 时必须核实它的非重叠条件，不能将此条件删除。

## 2. 沿两端切向短大圆弧的无额外条件版本

设 $0<\theta=\arccos(T_0\cdot T_1)<\pi$，令

$$
 N=\frac{T_1-\cos\theta\,T_0}{\sin\theta},\qquad
 v_\phi=\cos\phi\,T_0+\sin\phi\,N,\quad 0\le\phi\le\theta .
$$

任何满足曲率上界的曲线先已满足 $L\ge R\theta$，因为其切向球面总长度至少为 $\theta$。对这里每个 $v_\phi$，有
$\alpha_0=\phi,\ \alpha_1=\theta-\phi$，故 (1) 的条件自动成立。

定义

$$
 D_R=R\{\sin\theta\,T_0+(1-\cos\theta)N\},\qquad w=d-D_R .
$$

恒等式
$v_\phi\cdot D_R=R(\sin\phi+\sin(\theta-\phi))$
把 (1) 写成

$$
 \boxed{\quad
 L\ge R\theta+\max_{0\le\phi\le\theta}v_\phi\cdot w .
 \quad} \tag{2}
$$

这里只在端切向平面内选测试向量，**没有**限制 $\gamma$ 在此平面。

写 $x=w\cdot T_0,\ y=w\cdot N$。最大值可在端点
$\phi=0,\theta$ 与落在区间内的
$\phi=\operatorname{atan2}(y,x)$ 之间明确比较。若后一方向在区间内，最大值为 $\sqrt{x^2+y^2}$。还应同时保留弦长界 $L\ge|d|$ 和总转角界 $L\ge R\theta$。

若 $w$ 恰在此平面且其方向在该短弧上，(2) 化为
$L\ge R\theta+|w|$。以半径 $R$ 从 $T_0$ 转到 $w/|w|$，接长度 $|w|$ 的直段，再以半径 $R$ 转到 $T_1$，可在 $C^{1,1}$ 曲线类达到这个界。它只是下界的尖锐性说明，不是本题的 $C^2$ 曲面输入。特别是端二 jet 要求加速度为零时，非零角的即时最大曲率圆弧不满足该 $C^2$ 端迹，不能拿这个分段曲线直接提交为解。

$\theta=\pi/2,\ T_0=e_2,\ T_1=e_1$ 时 $D_R=R(e_1+e_2)$，恢复 R212 的既有式；这里没有将旧正交结论另报为新成果。新用途是当前已固定的 $b$ 端口，其长轴夹角约为 1.575813862，而非 $\pi/2$。

## 3. 对精确同 g 的范围

沿用 R212 的正确范围：若实际浸入准确诱导
$g=ds^2+a(s)^2du^2$，固定材料 $u$ 的经线是单位速测地线。因此**已证明的**曲面主曲率界可以作为上述曲线曲率界，应用于拟求的准确解或合法极限。

仅有 $C^0$ metric 误差和 surface-curvature 样本时不能自动作此替换；近似经线可能有测地曲率。若只有 $E\le1+\varepsilon$，无条件可得的是弦长
$|d|\le\sqrt{1+\varepsilon}(S-b)$。要在该近似场上使用 (1)/(2)，必须另有真实经线曲率界；本文不增加任何新的验收要求。


## 4. 当前输入的有限应用与范围

当前准确证明及实际端口浮点诊断分开记录于[固定prefix端口预算](../notes/2026-11-26-6a65-solver-fixed-prefix-spatial-port-budget.md)。该输入自由长度本来就是 $S-b$；四轴预算没有排除该输入，也不推出曲面BVP有解或全局reach通过。实际代入脚本自然exit 0，来源、哈希和数值误差保留在该记录。
