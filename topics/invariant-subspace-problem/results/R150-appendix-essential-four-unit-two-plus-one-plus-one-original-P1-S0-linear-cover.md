# R150 附录：原 P1 的显式一次式与 S=A_f=0 的完整线性坐标覆盖

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-347c-20261126 / unit31_general。日期：2026-11-26。

状态：本附录给出原双点最高一阶 germ 在原 mean 图上的完整一次式，并证明三值互异 $S=A_f=0$ 层的每个原解至少有一个 f 或 t 的非零系数。因此该层由两个合法的一变量图完整覆盖。本附录不宣称这些图已排空。

## 1. 同一原系统的一次式

沿用[原 U 值图](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)。先保留一般的非零 p,q，记

$$
a=1-b-c,\quad l=b+c,\quad u=bp+cq,\quad
V_2=bp^2+cq^2,\quad Q=pq,\quad \sigma=p+q,
$$

$$
T_0=V_2-2u^2,\qquad
2P_0=bp^3+cq^3-3uV_2+2u^3.
$$

原 Frobenius 数据仍是

$$
\tau(v)=av_0+v_1+bv_B+cv_C,\quad
k_0=(0,0,p,q),\quad k_1=(0,A_1,r,s).
$$

这里 $P_1$ 为原双点最高一阶 germ：

$$
P_1=\frac32\tau\left((k_0-u\mathbf1)^2
(k_1-\tau(k_1)\mathbf1)\right).
$$

直接按原乘法展开，得到

$$
\frac23P_1
=-T_0A_1+b(p^2-2pu-T_0)r
+c(q^2-2qu-T_0)s. \tag{1}
$$

该式本来就在 $A_1,r,s$ 中一次；没有将双点第二行当作另一简单点。

原 $E_0=0,N_0=\lambda P_0$ 的 Cramer 图可以写为

$$
W_1=T_0/2+2fu,\quad
W_2=uT_0+f(V_2+2u^2)-bcpqt+2\lambda P_0,
$$

$$
X=\frac{qW_1-W_2}{bp(q-p)},\qquad
Y=\frac{W_2-pW_1}{cq(q-p)},
$$

$$
r=X-ap-ct,\quad s=Y-aq-bt,\quad
A_1=2f-2bX-2cY+2bct.
$$

以上除数都在已付 $bcpq(q-p)\ne0$ 图内。将其代入 (1)，原方程 $P_1=3wP_0$ 等价于

$$
L_f f+L_t t+L_0=0, \tag{2}
$$

其中

$$
L_f=T_0\left(l-1+\frac{u(\sigma-2u)}Q\right),
$$

$$
L_t=bc\left(T_0+2u\sigma-\sigma^2+Q\right),
$$

$$
L_0=\frac{T_0^2(\sigma/2-u)}Q
+2P_0\left[\lambda\left(1-\frac{T_0}Q\right)-a-w\right].
$$

由原一阶矩 $\lambda=a+w+bh+ck$，最后一个系数亦为

$$
L_0=\frac{T_0^2(\sigma/2-u)}Q
+2P_0\left(bh+ck-\frac{\lambda T_0}Q\right). \tag{3}
$$

源代码以公分母 $2bcpq(q-p)$ 核对 (1)--(3) 的精确多项式身份，不作大有理图展开。

## 2. S=A_f=0 的对称参数

以下处于已付 $p+q\ne0$ 的范围，按同一个允许的公共尺度取

$$
p+q=2.
$$

这不把 p、q 分别独立归一。记

$$
x=h-1,\quad y=k-1,\quad
s_0=x+y=2\lambda-3,\quad z=xy,
$$

并处于三值互异图

$$
xyz(x-y)\ne0.
$$

实际上此处只需 $z(x-y)\ne0$。为与既有值图一致，定义

$$
A=2\lambda^2-2\lambda+1,\quad
C=-4\lambda^2+5\lambda-2,\quad R=3-4\lambda,
$$

$$
T=bx+cy=\frac Cz,\qquad
l=\frac{s_0C-Az}{z^2}.
$$

这些来自原三个矩，没有把必要矩条件称为充分。原 $N(V)=0$ 的 f 系数 $A_f$ 为零等价于

$$
QR=z\left(lQ+2u(1-u)\right). \tag{4}
$$

仍有

$$
Q\ne0,\quad bcP_0\ne0,\quad
V_2=2u-lQ,\quad
T_0=2u-lQ-2u^2.
$$

因此 (2) 的系数化为

$$
L_f=\frac{T_0(R-z)}z,\qquad
L_t=bc(T_0+4u-4+Q), \tag{5}
$$

$$
L_0=\frac{(1-u)T_0^2}Q
+2P_0\left(l+T-\frac{\lambda T_0}Q\right). \tag{6}
$$

下面证明任何原解都不可能同时有 $L_f=L_t=0$。这必须使用仍保留的原常数项 (6)，不能仅因一次式形式就忽略全部系数为零的参数面。

## 3. z=R 的全部零系数边界

若 $L_f=0$ 且 $z=R$，(4) 因 z 非零给出

$$
2u(1-u)=Q(1-l).
$$

于是

$$
T_0=Q(1-2l),\qquad
L_t=2bc\left(Q(1-l)+2u-2\right).
$$

两式结合 $L_t=0$ 得

$$
-4(u-1)^2=0.
$$

所以 $u=1$，再由 $Q\ne0$ 得 $l=1$。但一般恒等式

$$
2P_0=(2-3u)(2u-lQ)-Qu+2u^3
$$

在 $u=l=1$ 上恒为零，违反 $P_0\ne0$。这一步已经完整排除此零系数面，无须另除 $u-1$ 或 $l-1$。

## 4. T0=0 的全部零系数边界

(5) 表明，除第 3 节外，$L_f=L_t=0$ 只能落在 $T_0=0$。此时

$$
Q=4(1-u).
$$

因 $Q\ne0$，$u\ne1$。代回 $T_0=0$ 得

$$
2(1-u)(u-2l)=0,\qquad u=2l.
$$

原 P1 常数项必须同时为零；由 (6) 与 $P_0\ne0$ 得

$$
T=-l.
$$

故 $C=-lz$，而 (4) 与 $T_0=0$ 又给

$$
R=2zl=-2C.
$$

这是完全未除的关系

$$
(4\lambda-1)(2\lambda-1)=0. \tag{7}
$$

不能丢弃其中任一个根。

若 $\lambda=1/2$，则

$$
s_0=-2,\quad A=1/2,\quad C=-1/2.
$$

将 $C=-lz$ 与 $lz^2=s_0C-Az$ 合并，得

$$
z(A-C)=s_0C,
$$

所以 $z=1$。这使 $s_0^2-4z=0$，即 $x=y$，与三值互异矛盾。

若 $\lambda=1/4$，同样的两个原关系给出唯一候选

$$
s_0=-5/2,\quad z=20/13,\quad
l=13/20,\quad T=-13/20,
$$

$$
u=13/10,\quad Q=-6/5.
$$

尚须返回真正的值与权重关系。令

$$
p=1-\kappa,\quad q=1+\kappa,\quad \kappa^2=1-Q.
$$

因为 $p\ne q$，$\kappa\ne0$，且 $u=l-\kappa(b-c)$。另一方面，

$$
2T-ls_0=(b-c)(x-y).
$$

所以任何原参数必满足未取平方根的判别身份

$$
(1-Q)(2T-ls_0)^2-(l-u)^2(s_0^2-4z)=0. \tag{8}
$$

将上述唯一候选代回，左端精确为

$$
\frac{9971}{52000}=\frac{767}{4000}\ne0.
$$

因此第二个根也不可能。若除以已显示非零的 $l^2$，同一个矛盾是 $59/130\ne0$；源码同时核对这两个有理值。没有借 (8) 的必要性声称其充分。

## 5. 完整覆盖结论与范围

第 3、4 节穷尽了 (5) 的全部同时零系数可能，故每个三值互异 $S=A_f=0$ 原解都满足

$$
(L_f,L_t)\ne(0,0).
$$

因此该层由以下两个合法图完整覆盖：

1. $L_f\ne0$，由原 P1 解出 $f=-(L_tt+L_0)/L_f$。
2. $L_f=0$，此时 $L_t\ne0$，由原 P1 解出 $t=-L_0/L_t$，保留 f。

这是真正的两个图覆盖，第二图没有被第一图的分母清除。已登记的值碰撞排除可另行与此覆盖合并；本附录既没有重复它，也没有假设 $\mathcal I=\mathcal H=0$ 或其相反条件。故该覆盖同时适用于已经另付有限参数例外之外的余图。

完整原 mean、其他最高式、第二梯度式及同一物理几何仍然需要在余图中处理。本附录只降低坐标数，未宣布 S 层或整个非零均值层为空。

## 6. 实际执行身份

[自含源](../notes/2026-11-26-unit211-original-P1-S0-line-347c.py)及[实际小回执](../notes/2026-11-26-original-P1-line-execution-347c.json)均已保留。

冻结 blob：93bf370376fb853b5995e19de729cc1ab5a6de85；3436 bytes。

源码 SHA256：

42363730f4a89823d5937865e0117d181ba3f88f6ff401fc2702ffdae003891d。

公开 Actions run 45809839217 / job 139874500382。冻结源提交 eed35f2fb51b2b4f48ee85adc0fab5249aeaa074；执行前实际 pull 至 45522b1cbfbb7019945a9bf0b88496c4de5b6d69，根 README 与课题 README 未变。依赖 Python 3.12.14、SymPy 1.14.0。

实际源内计时 0.176205 秒，驱动计时 0.465967965 秒；峰值 RSS 69784 KiB，退出码 0。输出状态 all_exact_original_line_and_exception_checks_pass；S0Af0LineNeverIdenticallyZeroOnOriginalSolutions=true。输出 quarterLambdaOriginalMomentDiscriminant 为已约分的 767/4000。

stdout SHA256：

5097e4af2b6d3144a73a4ca40a2143fc5b53d0b73d9793b0e37f5f257b2ee5d2。

claimS0LayerEmpty=false、claimLambdaLayerEmpty=false、ordinaryISPClaim=false。
