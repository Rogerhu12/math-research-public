# R150：整个当前 W 图的无 T³ 项的首一 T 四次、原均值 F 二次与固定有限环境

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。
AI-assisted GPT-6 Astra Pro。

**状态：完整原理想推导。** 当前原 Delta0/W0 余图上，新同值 C4 准确给出一条无 T³ 项的首一 T 四次；一个原均值组合给出首一 F 二次，其中 F=2f−uλ。两者首项都只含已付权单位。它们为同点 Gram 投影提供一个在 A[λ] 上明确自由八维的环境；若保原值 s 的首一二次，则得到十六维环境。原最终方程商不被称为自由，所有原物理非零条件继续单列保留。

## 1. 原域及已成身份

A 是当前原一般 LS、Delta=0、W=0 图的已付权局部环，沿用当前完整权排除定理的准确作用域。不将其中依赖原物理 D 非零的边界结论外推到一般 hU=kU 碰撞。

记

$$e=u-1,\quad Q=ek,\quad
d=1-Q,\quad m=u-\ell,\quad
M=\ell(2u-\ell Q)-u^2=\ell^2d-m^2.$$

A 中 e,u,Q,ell,m,d,M,Phi 均为已付单位。又有

$$T_0=2u-\ell Q-2u^2,\quad
J=2u(1-u)+\ell Q,\quad
P_f=T_0(J-Q),$$

$$\Phi=T_0+4e+Q,\qquad
\Phi(J-2uQ)=P_f.\tag{1}$$

因此 J−2uQ 也是 A 单位。由 J+T0=−4ue，(1) 还准确推出

$$2e(J-uQ)=uQ\Phi.\tag{2}$$

所有原量仍来自同一个 Gram。沿用[两个同值四次原必要式](R150-appendix-unit211-W-original-two-quartic-necessary-values.md)的

$$A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,$$

$$D=\ell A_\lambda-T^2,\quad
K=\ell^2B_\lambda-3\ell T A_\lambda+2T^3,$$

$$c=3-2\lambda,\quad A_*=4uQ-J,\quad
C_*=A_*m^2+Jd\ell^2,$$

$$
\begin{aligned}
a_\Delta={}&M\ell^2Q(3-4\lambda)+MA_*T^2
+2MuQc\ell T+C_*D,\\
b_\Delta={}&2Mm(A_*T+uQc\ell).
\end{aligned}
$$

两个已成原组合是

$$R_4=Ma_\Delta^2-Db_\Delta^2,\qquad
C_4=2mDa_\Delta+Kb_\Delta.\tag{3}$$

本文以该原组合为输入，不再证明一次原值的排除，也不依赖 D27 或 B239 的新首项逆。

## 2. C4 的全部系数与无 T³ 项首一四次

置

$$H_4=4uQ\ell^2d.$$

由 M+m²=ell²d，直接有

$$MA_*+C_*=(A_*+J)\ell^2d=H_4.\tag{4}$$

将 aDelta 写成 T 的二次：

$$a_\Delta=(MA_*-C_*)T^2+2MuQc\ell T
+M\ell^2Q(3-4\lambda)+C_*\ell A_\lambda.$$

在 C4/(2m)=D aDelta+M K(Astar T+uQc ell) 中，T³ 系数恰为

$$-2MuQc\ell+2MuQc\ell=0.$$

其完整系数为

$$\frac{C_4}{2m}
=H_4T^4+B_2T^2+B_1T+B_0,\tag{5}$$

其中

$$B_2=-2\ell A_\lambda H_4-M\ell^2Q(3-4\lambda),$$

$$B_1=M\ell^2\{A_*B_\lambda-uQcA_\lambda\},$$

$$B_0=M\ell^3Q(3-4\lambda)A_\lambda
+C_*\ell^2A_\lambda^2+MuQ\ell^3cB_\lambda.$$

所以

$$[T^4]C_4=8muQ\ell^2d\in A^\times.\tag{6}$$

没有新的几何或权首项零面。定义实际首一多项式

$$q_T=T^4+\alpha_2T^2+\alpha_1T+\alpha_0
=\frac{C_4}{8muQ\ell^2d}\in A[\lambda,T],\tag{7}$$

其三个明确系数为

$$\alpha_2=-2\ell A_\lambda-\frac{M(3-4\lambda)}{4ud},$$

$$\alpha_1=
\frac{M\{A_*B_\lambda-uQcA_\lambda\}}{4uQd},$$

$$\alpha_0=
\frac{C_*A_\lambda^2}{4uQd}
+\frac{M\ell\{(3-4\lambda)A_\lambda+ucB_\lambda\}}{4ud}.$$

它们对 λ 的次数分别不超过 2、3、4，所有分母均已付。式 (7) 继承 C4 对原 EDelta、E2、E3 的完整原组合；没有把 R4、C4 当作全部原值条件的等价替代。

## 3. R4 的真正三次余式与完整首项零纤维

设 r4=[T⁴]R4，并只作首一除法：

$$r_T=R_4-r_4q_T,\qquad \deg_T r_T\le3.\tag{8}$$

因为 qT 的 T³ 系数为零，原展开准确给

$$[T^3]r_T=
8M^2uQ\ell^3d(3-2\lambda)(2uQ-J).\tag{9}$$

(9) 中全部权因子已付，但 3−2λ 尚未支付。本结论在 λ=3/2 整纤维上继续保留原 qT、rT；不在那里除三次首项，也不把“次数下降”当作该支为空。后续可以在补图首一化 rT，或在零图直接保留其降次原式。

(8) 是完整原组合，只用 qT 的单位首项；没有取平方自由部分、删内容或选 T 根。

## 4. 原均值对 F 的全图首一二次

令 F=2f−uλ，并把 λ、T 当作另外两个同点几何坐标。已刊物理仿射坐标双侧逆只用 A 中的单位，允许把原 x,y,t 的完整式写成 A[F,λ,T] 多项式。

使用[完整原均值多项式身份](R150-appendix-unit211-W-global-polynomial-mean-coordinates-and-explicit-monic-w-six.md)中的

$$L=mE_{B,e}+\ell dE_{B,o},$$

$$
L=M(y-1)\left(t-\frac{2x}{u}+\frac{2dy}{u}-c_0\right)
-\frac{\ell N}{u}(x-x_*),\tag{10}
$$

其中

$$c_0=\frac{2e}{u}+\frac{T_0\ell d}{uM},\quad
N=u(2-2u-Q)+\ell Q(2u-1),\quad x_*=1+u-u/\ell.$$

为使 qF 的全部系数可直接再生，可使用以下完整逆式：

$$f=(F+u\lambda)/2,\quad G=\lambda P_{02}-(1-u)T_0,$$

$$t=\frac{T_0G-P_ff-QP_{02}(T+\ell)}{\Phi bcQ},$$

$$g_1=2uf+T_0/2,\quad
W_2=\lambda P_{02}+uT_0+(V_2+2u^2)f-bcQt,$$

$$V_2=2u-\ell Q,\quad
g_y=u-\ell Q,\quad C_y=2u-uQ-\ell Q,$$

$$x=\frac{C_yg_1-g_yW_2}{QM},\qquad
y=\frac{uW_2-V_2g_1}{QM}.\tag{11}$$

它们是已刊原 E0/N0/P1 的同一双侧恢复，不引入第二份 Gram。

固定 λ、T，(11) 的三个 F 最高系数为

$$x_F=\frac{u\ell d}{M},\quad
y_F=-\frac{um}{M},\quad
t_F=\frac{2uQ-J}{2bcQ}
=\frac{2d(2uQ-J)}{MQ}.\tag{12}$$

原 (10) 的 F² 系数遂为

$$
\begin{aligned}
h_F:=[F^2]L
&=My_F(t_F-2x_F/u+2dy_F/u)\\
&=\frac{2umd(J-uQ)}{MQ}
=\frac{u^2md\Phi}{eM}\in A^\times.
\end{aligned}\tag{13}
$$

最后一步正用 (2)。因此无需原 F² 头的另一个未付因子，可以直接定义

$$q_F=L/h_F=F^2+a_1(\lambda,T)F+a_0(\lambda,T),\tag{14}$$

其中 a1 总次数不超过 1，a0 总次数不超过 2。它们的完整精确定义是将 (11) 代入原 (10)，除以 (13)；所有原低次项均保留，不能仅从最高次式猜定 qF。

因为 ell d 与 hF 均已付，在 qF=0 的原商里

$$E_{B,o}=-mE_{B,e}/(\ell d).$$

原 qF 来源和反向恢复均为同一个实际原均值组合。

## 5. 八维投影环境与保 s 的十六维环境

先取

$$R=A[\lambda],\quad C_1=R[T]/(q_T),\quad
C_2=C_1[F]/(\overline q_F).\tag{15}$$

qT 首一四次，qF 首一二次。因此 C1 为 R 自由四维，C2 为 R 自由八维，一个明确基底为

$$1,T,T^2,T^3,\quad F,FT,FT^2,FT^3.$$

这不需要权环为域，不需要 qT 或 qF 不可约，也不要求任何根简单。每次乘法可先按 F² 规则，再按 T⁴ 规则完成，只有已付单位分母。

(15) 是完整原点的 Gram 投影所落入的明确环境。原其余三条二次、加权 NS/PS、rT 与原值的其余条件仍须施加；它们不是由首一环境自动成立的条件。

为在同一个环境中保留完整原值，而不以 norm 逆代替真实值，继续取

$$C_3=C_2[s]/(s^2-D/M).\tag{16}$$

这是第三条首一规则，C3 在 R 上自由十六维，基底为上列八元及其各自乘 s。再施加原 H3、EDelta、EC、个别两谱 N/P，以及其余原 Gram 行；它们的原矩和逐谱来源保持已刊完整十行定义。

只有 (15)、(16) 的环境被称为自由。加上原行后的方程商只由相应基元生成。原 λ、D、s、zeta、原值 S 等非零条件继续作为原点限制；本文没有加入其逆变量，不能在任意几何局部化后自动沿用同一有限自由模结论。尤其没有将 D 的范数倒置。

D27 已闭并不迫使 B239 或 3−2λ 为单位。本页整个构造无需这两个尚未付的首项；它们的全零纤维仍在 (15)、(16) 中。

## 6. 实际小证书及尚未执行的部分

配套 V8 源在十个独立形式变量的 BigInt 整系数多项式环上，实际展开验证 (5) 的全部系数、T³ 恒等消失、(9) 的完整权关系余项，以及 (13) 的原 W 关系清分母式。

在尚未施加 M+m²=ell²d 时，源码保留并准确核掉其完整倍数；对均值 F² 头，同样保留 m−u+ell 及 2e(J−uQ)−uQPhi 的完整倍数。没有数值特化或选模样本。

实际耗时 26 毫秒，源码 8111 字节，SHA256：

e53cc4c0d77264a8da2697758237914afb899e1f7aa31df5aa66218ea006ce33

这是 V8 精确多项式检查，没有外部进程，POSIX exit 与 RSS 不适用。源并未展开 (15)、(16) 在 e,k 上的全部原矩阵，也未执行其任何有限排除；后续新矩阵必须按这里的同点原式、单首一规则和完整乘回构造，不能把环境存在性记成某条矩阵已返回。
