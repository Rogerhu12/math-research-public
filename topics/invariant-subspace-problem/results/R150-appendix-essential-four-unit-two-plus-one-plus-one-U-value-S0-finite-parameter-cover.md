# R150 附录：unit 2+1+1 的 U 值图 S 线性退化层之有限参数覆盖

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-347c-20261126 / unit31_general。日期：2026-11-26。

状态：本附录的覆盖引理与全部所用有理恒等式、例外因子支付已经完成，并有实际执行的小证书。结论是有限参数覆盖，不是这些纤维空性的断言；原 mean、最高恒等式、第二梯度及物理实现条件仍须在保留的纤维上核验。

## 1. 范围与结论

沿用[原U值完整分层](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)的同一Frobenius代数及U值坐标：

$$
\tau(v)=av_0+v_1+bv_B+cv_C,\quad a=1-b-c,\quad
V=U/U_0=(1,w,h,k),\quad \lambda=m/U_0.
$$

作同一个原 Gram／$U$ 缩放令 $p=1$，本层保留

$$
\lambda q(q-1)(q+1)bcP_0\ne0.
$$

原 moment 为

$$
\tau(V)=\lambda,\quad \tau(V^2)=2\lambda^2,\quad
\tau(V^3)=4\lambda^3,\quad N(V)=0.
$$

设

$$
S=h+k+1-2\lambda.
$$

在原 $E_0=0,N_0=\lambda P_0$ 全局图内，$N(V)$ 对 $(f,t)$ 仿射；在 $S=0$ 上其 $t$ 系数为零。本附录处理该图的 $f$ 系数亦为零的层。首先只看三个不同的值 $1,h,k$，即

$$
(h-1)(k-1)(h-k)\ne0. \tag{1}
$$

下面定义的两个对称函数 $\mathcal I,\mathcal H$ 给出完整二分：

- 若 $(\mathcal I,\mathcal H)\ne(0,0)$，则 $q$ 有一个全局有理表达式；其新分母零例外精确落在第二支。
- 若 $\mathcal I=\mathcal H=0$，则 $\lambda$ 必为明确不可约六次多项式 $M_6$ 的根，$(h,k)$ 只有两种互换选择，$q$ 至多两个选择。因此所有 $(\lambda,h,k,b,c,w,q)$ 参数至多有 $24$ 个纤维。每个纤维仍保留原 $(f,t)$ 和全部原条件；没有把必要条件的解认作物理临界点。

## 2. 对称变量与原 f 系数

记

$$
x=h-1,\quad y=k-1,\quad s=x+y=2\lambda-3,\quad z=xy,
$$

$$
A=2\lambda^2-2\lambda+1,\quad
C=-4\lambda^2+5\lambda-2,\quad
R=3-4\lambda,\quad j=2\lambda-1.
$$

由原 moment，

$$
T=bx+cy=C/z,\qquad
l=b+c=\frac{sC-Az}{z^2},\qquad
w=\lambda-1-T. \tag{2}
$$

这些式子只除以 (1) 中已知非零的 $z$。全部权重是

$$
b=\frac{T-ly}{x-y},\qquad
c=\frac{lx-T}{x-y}. \tag{3}
$$

令 $u=b+cq,V_2=b+cq^2$。原 $N(V)$ 在 $S=0$ 上满足

$$
4N(V)=zA_1-2(h+k+hk)f
-2w\{by+cqx\}. \tag{4}
$$

原 $E_0/N_0$ 图给

$$
A_1=
2\left(1-l-\frac{u(q+1-2u)}q\right)f
+\frac{(2u-q-1)(V_2-2u^2)+4\lambda P_0}{q}.
$$

故 $f$ 系数零等价于

$$
R=z\left(l+\frac{u(q+1-2u)}q\right). \tag{5}
$$

不除新系数的原多项式版本是

$$
qR-z\{b(1-2b)+(2l-4bc)q+c(1-2c)q^2\}=0. \tag{6}
$$

## 3. 原常数式与完整 q 图

定义

$$
K_u=2(1-\lambda)R+4zjl-2\lambda z,\qquad
K_v=j(R-2zl),
$$

$$
\mathcal I=TK_u-2wlz+sK_v,
$$

$$
\mathcal H=-lK_u-2wT+2wsl-2K_v. \tag{7}
$$

在 (5) 下，将原 (4) 的常数项化简，精确得到

$$
4N(V)=K_u u+K_v(q+1)-2w(by+cqx). \tag{8}
$$

这里已在 $f$ 系数零面，所以右侧确为常数项。代入 (3)，以 $d=x-y\ne0$ 记两个 $q$ 系数：

$$
d\{b(K_u-2wy)+K_v\}=\mathcal I+\mathcal H y,
$$

$$
d\{c(K_u-2wx)+K_v\}=-\mathcal I-\mathcal H x.
$$

因此原 $N(V)=0$ 等价于

$$
(q-1)\mathcal I+(qx-y)\mathcal H=0. \tag{9}
$$

若 $(\mathcal I,\mathcal H)\ne(0,0)$，则

$$
q=\frac{\mathcal I+\mathcal H y}{\mathcal I+\mathcal H x}. \tag{10}
$$

没有遗漏分母零：若分母零，未除的 (9) 还要求 $\mathcal I+\mathcal H y=0$；两式之差及 $x-y\ne0$ 迫 $\mathcal H=0,\mathcal I=0$，恰为保留的第二支。又 $q\ne1$ 使本图 $\mathcal H\ne0$，$q\ne-1$ 使 $2\mathcal I+s\mathcal H\ne0$。

## 4. 同时零面的一条完整 QQ 结式

设 $D=sC-Az$。清掉已知非零的 $z$，定义

$$
I_2=z^2\mathcal I,\qquad H_3=z^3\mathcal H.
$$

以下是完整原多项式身份：

$$
\begin{aligned}
I_2={}&2(4\lambda-1)CD\\
&+z\{2C(1-\lambda)R-2(4\lambda^2-7\lambda+2)D\}\\
&+z^2(-2\lambda C+sjR),
\end{aligned}
$$

$$
\begin{aligned}
H_3={}&D\{[4\lambda(1-\lambda)+2\lambda z]z-4jD-2sC\}\\
&-2(\lambda-1)Cz^2+2C^2z-2jRz^3+4jDz^2.
\end{aligned}
$$

它们对 $z$ 的次数分别为 $2,3$。完整 $5\times5$ Sylvester 行列式在 $\mathbb Q[\lambda]$ 中给

$$
\operatorname{Res}_z(I_2,H_3)
\doteq
(2\lambda-1)^3(4\lambda-1)(2\lambda-3)
C^4(2\lambda^2-1)M_6(\lambda), \tag{11}
$$

其中 $\doteq$ 仅差非零有理常数，而

$$
\begin{aligned}
M_6(\lambda)={}&1280\lambda^6-1344\lambda^5-8496\lambda^4\\
&+21020\lambda^3-17150\lambda^2+5810\lambda-693.
\end{aligned} \tag{12}
$$

(11) 是真 QQ 身份，不是模素数零维探测或从数值样本猜出的因子。实际证书直接以 BigInt 计算 Sylvester 行列式，并比较完整本原整数多项式。

## 5. 全部非 M6 因子支付

逐一回到 $I_2,H_3$，而非把结式因子当作解：

| $\lambda$ 面 | 原 $\mathbb Q[z]$ 或数域中的 gcd | 与原图矛盾 |
|---|---|---|
| $\lambda=1/4$ | $z$ | $z\ne0$ |
| $\lambda=3/2$ | $z$ | $z\ne0$ |
| $\lambda=1/2$ | $z-1$ | 此时 $s=-2$，$z=1$ 迫 $x=y$ |
| $2\lambda^2=1$ | $z-11/4+3\lambda$ | 此时 $z=s^2/4$，仍迫 $x=y$ |

最后一行在 $\mathbb Q(\sqrt2)$ 精确计算，一次覆盖两个嵌入。对于 $C=0$，$I_2$ 化为 $z^2 I_{22}(\lambda)$；原 QQ 检查给

$$
\gcd(C,I_{22})=1.
$$

故 $C=0$ 也只可能给已排的 $z=0$。这支付了 (11) 的所有非 $M_6$ 因子，未丢任何系数降次纤维。

## 6. M6 面与最多 24 个参数纤维

模 $41$，$M_6$ 保持次数 $6$。精确 Rabin 检查给

$$
X^{41^6}\equiv X\pmod{M_6},
$$

以及

$$
\gcd(M_6,X^{41^2}-X)=
\gcd(M_6,X^{41^3}-X)=1
\quad\text{在 }\mathbb F_{41}[X]\text{ 中}.
$$

因此 $M_6$ 在 $\mathbb Q$ 上不可约。这只用于证明系数数域的不可约性，绝不把有限域判空当作原复数系统判空。

对 $H_3$ 除以 $I_2$ 作关于 $z$ 的伪除，除去两个余式系数的公共 $\mathbb Q[\lambda]$ 因子，写本原线性余式为

$$
R_1(\lambda)z+R_0(\lambda).
$$

实际 QQ 检查给

$$
\gcd(M_6,R_1)=\gcd(M_6,R_0)=1,
$$

$$
\gcd(M_6,I_{22})=1.
$$

故 $M_6$ 面上原公共 $z$ 值唯一，且

$$
z=-R_0/R_1\ne0. \tag{13}
$$

继续用完整 QQ gcd 支付全部值及权重分母：

$$
\gcd(M_6,s^2R_1+4R_0)=1,
$$

$$
\gcd\bigl(M_6,A^2R_0+(ACs-C^2)R_1\bigr)=1.
$$

第一式给 $s^2-4z\ne0$，所以 $x^2-sx+z=0$ 确有两个不同根。第二式给

$$
A^2z-ACs+C^2=(Ax-C)(Ay-C)\ne0,
$$

所以由原 moment 参数化得到的两权重均非零。

还实际检查

$$
\gcd\bigl(M_6,sCR_1^2+AR_0R_1-R_0^2\bigr)=1. \tag{14}
$$

其分子正是 $(l-1)z^2R_1^2$，故 $l\ne1$。因此 (6) 不会作为 $q$ 的多项式恒零：若恒零，常数与二次项及 $bc\ne0$ 迫 $b=c=1/2$，从而 $l=1$，与 (14) 矛盾。无论 (6) 在某纤维中是否降为一次，它始终至多有两个 $q$ 根；降次纤维全部保留，不需要除以二次项系数。

于是六个 $\lambda$ 共轭、两个 $x/y$ 值分配、至多两个 $q$ 值，给最多 $24$ 个参数纤维。每个仍须保留 $q(q-1)(q+1)uP_0\ne0$ 与原 $(f,t)$，并检验原

$$
E_1,E_B,E_C,\quad
P_1-3wP_0,\ P_B-h^3P_0,\ P_C-k^3P_0,
$$

$$
N_1-2\lambda wP_0,\ N_B-\lambda h^2P_0,\ N_C-\lambda k^2P_0.
$$

这一有限覆盖论断不利用 mean 分量的维数来排孤立交点，亦未把所有有限纤维宣为已经排除。

## 7. 非同时零图的同一齐次正规化

为说明 (10) 可直接用于原方程，设

$$
\theta=\frac{2\mathcal I+s\mathcal H}{2\mathcal H},\qquad
P=\mathcal I^2+s\mathcal I\mathcal H+z\mathcal H^2.
$$

使用已知非零的 $1+q$ 作同一个原 Gram／$U$ 缩放，使新的 $p+q=2$，写 $p=1-\kappa,q=1+\kappa$。则

$$
\kappa^2=
\frac{\mathcal H^2(s^2-4z)}{(2\mathcal I+s\mathcal H)^2},
\qquad
pq=\frac{4P}{(2\mathcal I+s\mathcal H)^2}.
$$

新的基点均值与原值参数为

$$
u=\frac{2(l\mathcal I+\mathcal H T)}{2\mathcal I+s\mathcal H},
$$

$$
h=\lambda-\tfrac12-\kappa\theta,\qquad
k=\lambda-\tfrac12+\kappa\theta,
$$

$$
b=\frac l2+\frac{l-u}{2\kappa},\qquad
c=\frac l2-\frac{l-u}{2\kappa}.
$$

两个 $\kappa$ 符号同时保留，对应完整的值交换。本图的所有对称参数均为 $(\lambda,z)$ 的有理函数；并未把不同的原 Gram 规范混在一起，也没有额外独立缩放 $U_0$。本节只提供同一原方程的坐标身份，未宣称该一般图为空。

## 8. 可复算小证书与实际执行身份

[完整独立源码](../notes/2026-11-26-unit211-U-value-S0-finite-cover-347c.js)可用Node.js直接执行。仅用 BigInt 和有界整数运算，没有软件代数库依赖，也不下载数据。

冻结 blob：e1b4bd0c77ae9b9c65356df21a372d4ddab062bb。

源码 SHA256：91aac492c15bb8813efcebd68ca439a960616a6b14f851b7e8c5beec698e4797；8282 bytes。

实际执行是在 functions.exec 的 V8 isolate 内对完全相同的 ASCII 源字节 eval(source)。执行结果为 all_exact_cover_identities_pass：QQ 21 次完整结式身份、每个低次因子的原 z-gcd、M6 的全部新分母 gcd，以及模 41 的保度不可约性全部通过。该执行不依赖失效的本地 shell 环境。

[实际小回执](../notes/2026-11-26-unit211-U-value-S0-finite-cover-execution-347c.json)对应blob26472ae3ffc10e06ed0efe4b3b66dccddfccead7。回执准确保留起始 UTC 与实际 eval 计时，并明确 claim_excluded=false、claim_lambda_layer_empty=false、ordinary_isp_claim=false；没有虚构文件 stdout。

独立的 Python M6 原式消元源仍须取得自己的实际执行结果后，才能对这些有限纤维的空性作任何结论。它和本覆盖证书的执行身份分开，不互相代替。
