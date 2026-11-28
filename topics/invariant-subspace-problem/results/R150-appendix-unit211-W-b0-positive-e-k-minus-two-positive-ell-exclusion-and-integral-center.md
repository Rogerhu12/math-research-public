# R150：W/b0 正 e、k 首值负二中心的正 ell 子支排除与原坐标整性

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**结论。** 在当前正确 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 原图上，取 $1009$ 上方赋值并设
$$
v(e)=a>0,\quad v(k)=0,\quad \bar k=-2.
$$
则不存在 $v(\ell)>0$ 的原解。特别每个可能的原解都必须满足
$$
\boxed{\quad v(k+2)\ge v(e),\qquad (k+2)/e\in\mathcal O.\quad}
\tag{1}
$$
证明使用同一点原 $b_0,q_2,R_6$，完整包含 lambda 极点、零值、正估值与单位值。不需要完整 N5，不反演新的谱头或物理 D。

这是一项新的纸面原估值结论。此前[正 e 的原 lambda 限制](R150-appendix-unit211-W-b0-positive-e-ray-original-lambda-valuation-and-two-pole-centers.md)留下的 $\bar k=-2$ 中心仍未全部关闭；本条只排其正 ell 子支并给出 (1)。没有新数学运行。

## 1. 同点原定义及三个必要式

沿已刊[完整 b0/N5 原定义源码](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob 47281af16fdd0ad7500ecda377c3cb9f9d65e725，源 SHA256 e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8，取
$$
u=e+1,\quad Q=ek,\quad \delta=1-Q,\quad V_b=uk+2,
$$
$$
\ell=\frac{u((k+2)^2-2ek)}{kV_b},\quad
m=u-\ell,\quad M=\ell^2\delta-m^2,
$$
$$
J=2u(1-u)+\ell Q,\quad
A_*=4uQ-J,\quad C_*=A_*m^2+J\delta\ell^2.
\tag{2}
$$
设
$$
\mu=2\lambda-3,\quad
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell A_2T+2T^3.
$$
完整原必要身份为
$$
A_*T=uQ\ell\mu,
\tag{3}
$$
$$
q_2=2A_2C_*+2M\ell Q(3-4\lambda)
       -8uQ\delta\ell T^2=0,
\tag{4}
$$
$$
R_6=MK^2-4m^2D^3=0.
\tag{5}
$$
(4) 来自完整 $2a_\Delta/\ell$、(3) 及整恒等式
$MA_*+C_*=4uQ\delta\ell^2$，并非某个投影的替代方程。必要性的原物理范围不扩大。

令 $\mathcal O$ 为赋值环，$\mathfrak m$ 为其极大理想。赋值允许在代数扩张中取值；所有剩余值都在同一剩余域中。原代数点选取 $1009$ 上方赋值的理由仍沿先前全权 Artin 必要模型，不从裸模空性作特征零提升。

## 2. 正 ell 假设下的全部权首项

反设
$$
d=v(\ell)>0.
\tag{6}
$$
此时 $u,\delta,k$ 都为赋值环单位，
$$
\bar u=\bar\delta=1,\quad
\bar m=1,\quad \bar M=-1.
\tag{7}
$$
不需要预设 $V_b$ 为赋值环单位；(6) 已给 ell 自身的整性。

由 $J/Q=-2u/k+\ell$，得到
$$
\overline{J/Q}=1,\qquad
\overline{A_*/Q}=3,\qquad
\overline{C_*/Q}=3.
\tag{8}
$$
因此 (3) 可按已证明的赋值环单位重写为
$$
T=\ell c\mu,\qquad
c=\frac{u}{A_*/Q}\in\mathcal O^\times,\qquad \bar c=1/3.
\tag{9}
$$
这里反演的仅是 (8) 已核的单位，不是新假设的头。

## 3. 先排 lambda 极点，再确定两个原矩的阶数

若 $v(\lambda)<0$，由 (9)
$$
T/\lambda=\ell c(2-3/\lambda)\in\mathfrak m.
$$
将 (4) 除以 $Q\lambda^2$，每一项都在 $\mathcal O$，且其剩余值依次为
$$
4\cdot3,\qquad 0,\qquad 0.
$$
故原 $q_2=0$ 迫 $12=0$，与特征 $1009$ 矛盾。于是 lambda 必整；$\lambda=0$ 也暂保在内。

此时由 (9)，$T/\ell$ 整，且 $T\in\mathfrak m$。将 (4) 除 $2Q$ 并取剩余值，得到
$$
\bar A_2=0.
\tag{10}
$$
记 $l=\bar\lambda$。由于 $A_2(0)=1$，有 $l\ne0$。同一原式精确解给
$$
\frac{A_2}{\ell}
=\frac{-M(3-4\lambda)+4u\delta T^2}{C_*/Q}
\in\mathcal O,
\qquad
\overline{A_2/\ell}=\frac{3-4l}{3}.
\tag{11}
$$
这使用 (8) 的单位，不以 (10) 直接假定某个更高阶消失。

由 (9)、(11)，
$$
\begin{aligned}
\overline{D/\ell^2}
&=\frac{3-4l}{3}-\frac{(2l-3)^2}{9}\\
&=-\frac{4l^2}{9}\ne0.
\end{aligned}
\tag{12}
$$
所以 $v(D)=2d$。特别这里没有剥掉 D 为零的可能；原式本身在当前假设下证明其所列首值非零。

又有完整一元恒等式
$$
B_3=(2\lambda-1)A_2-\lambda.
$$
因此 $\bar B_3=-l\ne0$。按 (9)、(11)，
$$
K/\ell^2
=B_3-3A_2(T/\ell)+2\ell(T/\ell)^3
\in\mathcal O^\times,
$$
$$
\overline{K/\ell^2}=-l,\qquad v(K)=2d.
\tag{13}
$$

## 4. 原 R6 的两项不能相消

由 (7)、(12)、(13)，
$$
v(MK^2)=4d,\qquad
v(4m^2D^3)=6d.
$$
$d>0$，两项估值严格不同，故 (5) 不可能为零。于是 (6) 排除。这一步保留所有原剩余参数，既不需要原 N5，也不需要按 lambda 的有限剩余根逐个选取。

## 5. 原 k 加二坐标的整性后果

令 $z=k+2$，故 $v(z)>0$；若 $z=0$，直接采用 $v(z)=+\infty$，(1) 已成立。对于非零 z，假设
$$
b=v(z)<a=v(e).
$$
原分母满足
$$
V_b=(1+e)z-2e,\qquad v(V_b)=b.
$$
原分子内的量为
$$
z^2-2ek=z^2+4e-2ez,
$$
其估值至少 $\min(2b,a)>b$，即使两个最低项相消也只会更高。因为 $u,k$ 均为单位，(2) 因而给
$$
v(\ell)>0.
$$
这与第4节矛盾，证明 (1)。

因此在整个余下 $\bar k=-2$ 中心，可以使用一个确实整的原坐标
$$
Z=(k+2)/e,\qquad k=-2+eZ.
$$
准确的恢复是
$$
\ell=
\frac{u(eZ^2+4-2eZ)}{(-2+eZ)(uZ-2)}.
\tag{14}
$$
(14) 的分子首值为4，$k$ 的首值为负二。因此：

- 若 $\bar Z\ne2$，则 ell 为单位，且 $\bar\ell=-2/(\bar Z-2)$；
- 若 $\bar Z=2$，则 ell 有极点，其全部深度仍保留。

这只是原参数在剩余中心的准确分类。两个情况的原均值、完整值、DVR 分母与原空性尚未支付。本文不排除这两个剩余中心，不宣称正 e 射线整体关闭，也不改变旧有限维计算或资源边界。
