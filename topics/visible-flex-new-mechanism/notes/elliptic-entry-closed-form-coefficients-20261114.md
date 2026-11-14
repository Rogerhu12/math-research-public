# 椭圆入口 u4/v7/b6 的准确回参公式

日期：2026-11-14。状态：纸面实现附录；没有候选计算或源码变更。

本稿服务于 [R64](../results/R64-convex-core-entry-seventh-tangent-and-sixth-center-jets.md) 和成套入口基场设计。它将其中的曲率比值化为准确椭圆弧长回参后的简单函数，避免实现时把必要的角函数误投影成已有有限模。

## 1. 约定与弧长换元

取 A≥B>0，

$$
\Gamma(\varphi)=(A\cos\varphi,B\sin\varphi,0),\quad
q(\varphi)=\sqrt{A^2\sin^2\varphi+B^2\cos^2\varphi},\quad
\Delta=A^2-B^2.
$$

定义准确周长半径和材料角

$$
a_0=\frac1{2\pi}\int_0^{2\pi}q(\varphi)\,d\varphi,
\qquad d\theta=\frac q{a_0}\,d\varphi.
$$

因此 `φθ=a0/q`，入口角转速 k 与其导数为

$$
k=\frac{a_0AB}{q^3},\qquad
q_\varphi=\frac{\Delta\sin\varphi\cos\varphi}{q},\qquad
k_\theta=-\frac{3a_0^2AB\Delta\sin\varphi\cos\varphi}{q^6}.
\tag{1}
$$

所有函数均沿同一个准确材料逆映射 φ(θ) 读取；a0 仍是准确周长积分的身份，不冻结为某次数值近似。

## 2. 不用高次曲率除法的系数

沿用 `a′=−Cx3+…`、C>0、side=σ。代入 R64 得

$$
\boxed{
U_4(\theta)=\frac{3C\Delta}{4a_0AB}
\sin\varphi\cos\varphi,
\qquad
(U_4)_\theta=\frac{3C\Delta}{4ABq}\cos2\varphi.
}\tag{2}
$$

特别地，U4 本身只是一个准确 `sin(2φ)` 模，不能因为它在材料 θ 的 Fourier 展开很长就认为需要近似定义。

竖直切向的必要第七阶为

$$
\boxed{
V_7(\theta)=-\frac{3\sigma C^2\Delta}{7a_0^2A^2B^2}
\sin\varphi\cos\varphi\,q^3.
}\tag{3}
$$

它的一阶材料角导数为

$$
\boxed{
(V_7)_\theta=-\frac{3\sigma C^2\Delta}{7a_0A^2B^2}
\left[q^2\cos2\varphi+
3\Delta\sin^2\varphi\cos^2\varphi\right].
}\tag{4}
$$

V7 含 q3 权函数，通常不是有限个 φ 正弦模；后续应直接使用 (3)—(4)，不能用旧角列的拟合系数冒充同一个准确入口。

准确均值为

$$
\boxed{
\langle k^{-2}\rangle
=\frac1{2\pi a_0^3A^2B^2}\int_0^{2\pi}q(\varphi)^7\,d\varphi,
\qquad
B_6=-\frac{\sigma C^2}{2}\langle k^{-2}\rangle.
}\tag{5}
$$

这里 q7 而非 q6 来自材料角测度。数值实现可在 φ 坐标对这个光滑正函数积分，但必须将积分误差及 a0 误差作为评价账保留；物理定义仍是 (5)。这不是逐圈优化中心速度，也不是随当前参数另选平均值。

## 3. 对称、圆极限和未评价的准确界

U4、V7 为 π 周期奇函数，保留当前闭角重构所用的二重周期与反射；B6 为一个径向系数。A=B 时 Δ=0，二者准确为零，且 k=1、`B6=−σC2/2`，正好与旋转圆柱的 `z′=σ sqrt(1−a′2)` 展开一致。

严格凸圈的总转角给 `〈k〉=1`。Jensen 不等式因此给

$$
\langle k^{-2}\rangle\ge1,
$$

非圆椭圆严格大于 1。这只比较必要入口高度系数的大小，不是完整连接或全局曲率判据。

若只需要对未来支持长度作解析预算，

$$
\|U_4\|_\infty=\frac{3C\Delta}{8a_0AB}.
\tag{6}
$$

当 Δ>0，令 `s=sin²φ`。因

$$
|\sin\varphi\cos\varphi\,q^3|^2
=s(1-s)(B^2+\Delta s)^3,
$$

内部唯一极大点 s* 是

$$
B^2+(4\Delta-2B^2)s_*-5\Delta s_*^2=0,
$$

即

$$
s_*=
\frac{4\Delta-2B^2+
\sqrt{(4\Delta-2B^2)^2+20\Delta B^2}}{10\Delta}
\in(0,1).
$$

因此 V7 的准确振幅由 (3) 的常数乘
`sqrt(s*(1−s*)) (B2+Δs*)^(3/2)` 给出，无需对候选角网格取样寻找最大值。它只控制新增必要首项；原锚低阶项的删除、cutoff 导数和更高未知项仍应分别核算。

## 4. 独立复核及使用范围

repo_sources 已独立复核 (1)—(5) 的符号、a0 因子、材料测度以及 U4 单 φ 模/V7 非有限 φ 模的区别。本稿没有评价 A=1、B=.28 的任何积分或最大值，没有选择新的入口支持长度，也没有改变当前公开 Actions 的输入或源码。
