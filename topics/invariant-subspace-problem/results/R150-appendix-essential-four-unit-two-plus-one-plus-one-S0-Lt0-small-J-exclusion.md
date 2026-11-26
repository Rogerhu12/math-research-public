# R150 附录：S=0、原 P1 的 t 系数为零时小 J 因子的完整排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-347c-20261126 / unit31_general。日期：2026-11-26。

状态：本附录将已经实际生成的 Lt0 参数结果式中的小 J 因子完整返回原系统并排除。全部四次 lambda 参数及原 q 二次方程的两个根同时保留；最终是一个真实 QQ 八维单位身份。未宣布 Lt0 的另一个大因子、整个 S 层或整个非零均值层为空。

## 1. 小 J 的原权重意义

使用已经登记的[原 U 值矩](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)和[原 P1 一次式](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-P1-S0-linear-cover.md)。在已付通用图中共同规范 $p+q=2$，保留

$$
bcpq(p-q)uP_0\lambda(u-1)\ne0.
$$

这里整个 $u=1$ 分支已另行关闭。设

$$
x=h-1,\quad y=k-1,\quad s=x+y=2\lambda-3,\quad
z=xy,\quad \Delta=s^2-4z,
$$

并保留三值互异条件 $z\Delta\ne0$。记

$$
A=2\lambda^2-2\lambda+1,\quad
C=-4\lambda^2+5\lambda-2,\quad
D=sC-Az,
$$

$$
l=b+c=D/z^2,\qquad T=bx+cy=C/z.
$$

已经实际执行的 Lt0 参数投影使用的小因子是

$$
\begin{aligned}
J(\lambda,z)={}&4z^3+(12\lambda^2-4\lambda-1)z^2\\
&+(96\lambda^3-236\lambda^2+196\lambda-62)z\\
&+192\lambda^4-624\lambda^3+776\lambda^2-442\lambda+100.
\end{aligned}
$$

它有精确身份

$$
J=-\left[\Delta z^2+D(4A-2\Delta)-4C^2\right]
=-z^2\Delta(1-2b)(1-2c). \tag{1}
$$

因此在本三值互异图，$J=0$ 等价于 $b=1/2$ 或 $c=1/2$。

原 P1 的 t 系数为

$$
L_t=bc\left[-2(u-1)(u-2)+(1-l)pq\right].
$$

若 $b=1/2$，用 $p+q=2$ 得

$$
u-1=(l-1)q,\qquad
\frac{L_t}{bc}=(l-1)(3-2l)q^2.
$$

$u-1$ 与 q 非零，故 $L_t=0$ 强制 $l=3/2,c=1$。另一情形交换 B、C 标签。原系统对这一重标记对称；随后以同一个公共尺度规范 $p=1$。所以完整保留代表

$$
b=1/2,\qquad c=1,\qquad l=3/2,\qquad a=-1/2. \tag{2}
$$

没有分别独立缩放 p 和 q，也没有丢弃交换后的值分配。

## 2. 全部 lambda 参数：一个四次式及已付 C=0

由原矩，(2) 等价于

$$
H_l=3z^2+2Az-2sC=0.
$$

完整 QQ 结果式为

$$
\operatorname{Res}_z(H_l,J)=16C^2M_J(\lambda), \tag{3}
$$

其中

$$
M_J(\lambda)
=420\lambda^4-1884\lambda^3+3663\lambda^2-3084\lambda+916.
$$

源码从两个原多项式重新计算 (3)，没有只取其某一个方便的因子。

必须单独支付 $C=0$。若 C 为零，$H_l=0,z\ne0$ 给 $z=-2A/3$。同时 $D=lz^2=3z^2/2$，由 (1) 与 $J=0$ 得

$$
\Delta=3A.
$$

于是 $s^2=A/3$，即 $A-3s^2=0$。但模

$$
C=-4\lambda^2+5\lambda-2
$$

有

$$
A-3s^2\equiv(43\lambda-42)/2,
$$

而这两个 QQ 多项式的 gcd 为 1。因此 C=0 不可能。所有原候选都满足 $M_J=0$。

取完整 QQ 商代数

$$
K_4=\mathbb Q[\lambda]/(M_J).
$$

在 $K_4[z]$ 中，源码对完整 $H_l,J$ 作 Euclidean 运算；每个被使用的最高系数先在整个四维 QQ 代数中求真逆并回乘。实际 gcd 为一次且首项为 1，所以每个 lambda 根都对应唯一的 z，并精确核对 $H_l(z)=J(z)=0$。

令 $T=C/z$。固定 (2) 后，值分配被原一阶矩确定为

$$
x=2(s-T),\qquad y=2T-s,\qquad
h=1+x,\quad k=1+y,\quad w=\lambda-1-T. \tag{4}
$$

源码实际检查 $x+y=s,xy=z$ 及

$$
x^2/2+y^2=A,\qquad x^3/2+y^3=4\lambda^3-6\lambda^2+3\lambda-1.
$$

因此没有在四次参数域中任取某个平方根或遗漏另一种权重标签。

## 3. 原 P1 全局确定 f

从现在起 $p=1$，仍保留两简单点基点配对 q。由 (2)，

$$
u=1/2+q,\qquad V_2=1/2+q^2,\qquad
P_0=3q^2/4,\qquad T_0=-q(q+2).
$$

原 P1 的 t 系数恒为零，其 f 系数为

$$
L_f=q^2(q+2).
$$

[整个三值互异 S0/P1 两变量系数零排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-P1-zero-coefficients-exclusion.md)支付了 $q+2=0$；这一步没有把该面静默移除。因此令

$$
H=3/2+T,
$$

原 P1 恰给

$$
f=\frac{q+2}{2}-\frac{3\lambda}{2}
-\frac{3H}{2(q+2)}. \tag{5}
$$

在同一原 $E_0=0,N_0=\lambda P_0$ 图上，另有

$$
A_1=2qf+q(3\lambda-q-2)
=-\frac{3qH}{q+2}. \tag{6}
$$

## 4. 原 N(V) 的真正二次 q 方程

记 $R=3-4\lambda$。S=0 上的原身份为

$$
4N(V)=zA_1-2(z-R)f-w(y+2qx).
$$

代入 (5)、(6)，乘唯一新增且已付的 $q+2$，得到

$$
\begin{aligned}
n(q)={}&-3H(zq-z+R)\\
&-(z-R)(q+2)(q+2-3\lambda)\\
&-w(q+2)(y+2qx)=0. \tag{7}
\end{aligned}
$$

即

$$
n(q)=n_2q^2+n_1q+n_0,
$$

$$
n_2=-(z-R)-2wx,
$$

$$
n_1=-3Hz-(z-R)(4-3\lambda)-w(y+4x),
$$

$$
n_0=(z-R)(3H-4+6\lambda)-2wy.
$$

源码明确保留降次及恒零可能；若原 q 兼容式恒零会输出未知并停止该计算，不会宣排空。本次实际 q 次数为 2，且 $n_2$ 在整个 $K_4$ 中求得真逆并回乘。因此所有四个 lambda 参数同时是真正的二次 q 图，没有未付的一次降次纤维。

建立

$$
\mathcal B_8
=K_4[q]/(q^2+n_2^{-1}n_1q+n_2^{-1}n_0).
$$

这里不需要任一商多项式不可约；整个代数同时保留所有根及所有原参数求值同态。

源码预备逐一剥离原已付的 q、q±1、u、q+2 和声明的 L 图因子，但实际 removedUnitFactors 是空列表。也就是说，在形成 $\mathcal B_8$ 前没有剥掉任何一个 q 因子。随后直接在整个未删的八维代数中求出并回乘

$$
q,\ q-1,\ q+1,\ u,\ P_0,\ q+2,\ L=qx-y
$$

的逆。因此这次计算还证明 (7) 覆盖的全部参数自动满足 $L\ne0$。虽然执行门标签写作 L≠0，本实际覆盖没有遗留一个被 L 饱和删除的点，L=0 也不可能满足这些原必要条件。未使用或除去 $A_f$；$A_f=0$ 及其相反情形均保留。

## 5. 同一原九式及真实 QQ 单位身份

按原 Frobenius 运算、原最高双点 germ 和原第二梯度，在上述参数代数与剩余 t 变量上重建原图：

$$
W_1=V_2/2-u^2+2fu,
$$

$$
W_2=uV_2-2u^3+f(V_2+2u^2)-bcqt+2\lambda P_0,
$$

$$
X=\frac{qW_1-W_2}{b(q-1)},\quad
Y=\frac{W_2-W_1}{cq(q-1)},
$$

$$
r=X-a-ct,\quad s_1=Y-aq-bt,\quad
A_1=2f-2bX-2cY+2bct.
$$

上述两个 Cramer 除数都求真实全局逆并回乘。随后核对

$$
f=\tau(D_K\mathbf1)/2,\quad E_0=0,\quad
P(k_0)=P_0,\quad N(k_0)=\lambda P_0,\quad P(V)=N(V)=0.
$$

完整九式为三条原 mean、三条原最高式及三条原第二梯度式：

$$
E_1,E_B,E_C,\quad
P_1-3wP_0,\quad P_B-h^3P_0,\quad P_C-k^3P_0,
$$

$$
N_1-2\lambda wP_0,\quad
N_B-\lambda h^2P_0,\quad N_C-\lambda k^2P_0.
$$

它们对 t 的次数依次为

$$
2,2,2,-1,3,3,2,3,3.
$$

原 P1 真实恒为零，原其余八式全部保留。参数阶段完成 45 次成功的全局逆及下层范数逆；原九式生成后共计 49 次。无失败的全局逆试探，无参数单位因子删除。

取两条原 mean 的完整 Sylvester 结果式

$$
\mathcal R=\operatorname{Res}_t(E_1,E_B)\in\mathcal B_8.
$$

没有除以任一 t 最高系数，因此它们在某个参数点降次时，原共同有限根仍使完整结果式为零。

在完整八维 QQ 基中，$\mathcal R$ 的乘法矩阵实际为 $8\times8$ 且 QQ 秩为 8。源码求得乘子 $g\in\mathcal B_8$，然后用原代数乘法重新检查

$$
g\mathcal R=1.
$$

乘子向量 SHA256：

b51d2f3ed69b3d68d00a8ca68a3c1a0701551caa2b466ba85c0bac693ec7d5cb。

任何原参数求值同态都将原共同 t 根送到 $\mathcal R=0$，与上述单位身份矛盾。这完整排除小 J 因子；不是模素数探测，也未把某个范数必要条件称为充分。

由 (1)--(7) 的完整覆盖和本次没有任何参数因子删除的实际身份，三值互异 S0 图中 $L_t=0,J=0$ 的原解不存在。Lt0 参数投影中的另一个 $(26,12)$ 大因子仍须另行处理。

## 6. 实际执行身份

[自含源](../notes/2026-11-26-unit211-S0-Lt0-small-J-original-QQ-347c.py)与[实际小回执](../notes/2026-11-26-S0-Lt0-small-J-execution-347c.json)保留完整执行身份。

冻结 blob：b919002dffb46db73817500ba7a88bcdf97bfaf9；14392 bytes。

源码 SHA256：

534a59d51814fa35db8b02ed5e536324e144bafc2a88a3edced548da529d3c6c。

公开 Actions run 45820227879 / job 139910286544。冻结源提交 ed27f68cd6a0d4d951542f1af6db2e24f0f34f3b；执行前实际 pull 后仍为同一提交，根 README 与课题 README 未变。依赖 Python 3.12.14、python-flint 0.9.0。

参数与单位核验 0.008210 秒；完整原九式核验 0.099075 秒；最终单位身份完成于 0.108022 秒。源内峰值 RSS 37500 KiB；驱动计时 0.184326977 秒、峰值 RSS 38396 KiB，退出码 0。

原九式输入 SHA256：

12ba9279a759842dddc9979cae8ec0dec5a1f5ac52bc02cca17479dacdc5758f。

stdout SHA256：

007f17b1ec1c153a87ce5d42524bf1853838621e3b332dbe3d31852a63510e5f。

实际只用 E1/EB 一个结果式就取得八维单位身份。最终状态 exact_original_small_J_fiber_excluded；qEquationDegree=2、removedUnitFactors=[]、P1IdenticallyZero=true、failedGlobalInverseTrials=0。输出保持 claimS0LayerEmpty=false、claimLambdaLayerEmpty=false、ordinaryISPClaim=false。
