# R1041 — 原四点谱盖、完整 Pell 范数与真实半 Norm 类

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**已证明。** 本篇直接使用 R1031 原两 quadric 的 $s_0=0$
四点谱盖，给其固定亏格二模型、真实 S4 incidence 对应，
并消费 R1039 的无穷惰性超奇异输入。
所得 Pell 单位的 Norm 精确返回原 B，连常数平方也完全确定。
对一个真正的最短反 Frobenius 截面，再将 R1039 的
$F_Q$ 零除子分成原两个三挠交，构造保两半的
$E_L(\mathbf F_q)$ 类，而不将已算为零的完整 Norm 类当作非零。

Pell 单位的存在和平方 Norm 尚不等于原 $s_0=1$ 点；
以下保持这个区别，也未给原27对或原最高局部 AJ 非零。

## 1. 原四点不是新选的四次覆盖

设 $a^3=4$，特征零先在 $\mathbf Q(a)$ 上工作。
惰性 q≥5 时取 $a\in\mathbf F_q$ 的唯一该根。
原三次谱域为
$$
 k=\mathbf F_q(B),\quad B:Y^2+Y=X^3,\quad
 z^3+cz-4=0,\qquad c=3/X,
$$
$$
 g=z^2+az+a^2.
\tag{1}
$$
在其分裂域中记三个根为 $z_i$、相应 $g_i=g(z_i)$，
并按 R1039 固定
$$
 r_i^2=g_i,\qquad r_1r_2r_3=3a/X=ac.
\tag{2}
$$
它们的四个偶符号选择是原 S4 的四字母集合。

R1031(19)在 $s_0=0$ 时准确为
$$
 G_0=4X^2G_2,\qquad G_1=-4XG_2,
$$
亦即
$$
 gR^2=G_2(z-2X)^2.
\tag{3}
$$
在分裂域中，一个射影解由
$$
 R(z_i)/(z_i-2X)=\kappa/r_i
\tag{4}
$$
给出，允许三个 r 的符号改变并将总乘积规范为(2)。
公共负号可吸收到射影比例 κ，故恰有四个射影解。
反向由三个值唯一插值出次数≤2的 R；
(3)立即成立。因而这个四点集合就是原 $s_0=0$ 集合，
不是一个无关的同源曲线或另造的 Selmer 类。

令
$$
 \vartheta=r_1+r_2+r_3.
$$
其四个共轭为三个偶符号和。由原三次方程，
$$
 \sum g_i=3a^2-2c,\quad
 \sum_{i<j}g_ig_j=c^2-3a^2c,\quad
 \prod r_i=ac.
$$
直接展开四个和的多项式，得到
$$
 \boxed{
 (\vartheta^2-3a^2)^2+4c\vartheta(\vartheta-2a)=0.
 }
\tag{5}
$$
四字母的稳定子是 S3，故由 R1039 的真实全 S4 群，
(5)定义连通四度谱域。

## 2. 四点谱盖的固定亏格二模型

置
$$
 v=\vartheta/a-1,\qquad D(v)=v^2+2v-2.
$$
由(5)，原 B 坐标准确为
$$
 \boxed{X=-3a\frac{v^2-1}{D(v)^2}.}
\tag{6}
$$
不是仅比较模数。一个直接整系数恒等式是
$$
 D(v)^6-432(v^2-1)^3=(v^3-2)^2Q_6(v),
\tag{7}
$$
$$
 \boxed{
 Q_6(v)=v^6+12v^5+48v^4+44v^3-132v^2-96v+124.
 }
\tag{8}
$$
于是实际四谱盖的光滑射影正规化为
$$
 \boxed{\mathcal C_4:H^2=Q_6(v),}
\tag{9}
$$
且真正映射 $f_4:\mathcal C_4\to B$ 给为
$$
 \boxed{
 X=-3a\frac{v^2-1}{D(v)^2},\qquad
 2Y+1=\frac{(v^3-2)H}{D(v)^3}.
 }
\tag{10}
$$
反向在原四次域中为
$$
 v=\vartheta/a-1,\qquad
 H=\frac{(2Y+1)D(v)^3}{v^3-2}.
\tag{11}
$$
所有分母处按光滑射影模型延拓。(7)表明这是同一函数域；
不把去掉的平方因子当成新的分歧。

(8)在每个 q≥5 平方自由。可不靠判别式数表证明：
(6)的有限导数为
$$
 dX/dv=6a(v^3-2)/D(v)^3.
\tag{12}
$$
原 B 到 X 线的有限分歧在 $4X^3+1=0$。
拉回的分子正是(7)。
三个临界点 $v^3=2$ 都是简单临界点，
且
$$
 Q_6(v)\equiv108(2-v^2)\pmod{v^3-2},
$$
所以它们在(7)中恰被去掉二重因子。
$D=0$ 处不同时有 $v^2-1=0$ 或 $v^3-2=0$，
故没有额外零。其余零由(12)均为简单。
无穷处首项为1。因此(9)是每个 q≥5 的真正亏格二好模型。

两个无穷点记为 $I_+,I_-$，以 $H/v^3\to\pm1$ 标记。
它们在基域上有理，且
$$
 f_4(I_+)=T=(0,0),\qquad
 f_4(I_-)=-T=(0,-1).
\tag{13}
$$
这里两点均为 $f_4$ 的二重分歧点。
其余有限点不增加 $f_4$ 分歧；这也与
S4 的 transposition 在四字母集合上的循环型相符。
超椭圆 involution $\jmath_4:H\mapsto-H$
在原 B 上覆盖 $[-1]$。

## 3. 原 S4 incidence 给严格对应

把 S4 的四字母视为四面体顶点，
六个 $(i,\pm r_i)$ 视为它的六条边：
边 $(i,+)$ 连接第 i 个符号同为正的两个顶点，
边 $(i,-)$ 是其对边。
原 $\widetilde C/B$ 正是这六边覆盖；
原 $\iota$ 交换对边。

定义实际 incidence 对应
$$
 \Gamma:\ J_{\mathcal C_4}\longrightarrow J_{\widetilde C}
\tag{14}
$$
为一个顶点送到其三条邻边的和。
其反对应 $\Gamma^t$ 将一条边送到其两个端点。
在一般纤维上，两个不同顶点恰有一条共同边，
同一顶点有三条邻边，故准确有
$$
 \boxed{
 \Gamma^t\Gamma=[2]+f_4^*f_{4*},
 \qquad
 \pi_*\Gamma=f_3^*f_{4*}.
 }
\tag{15}
$$
这些是曲线对应及 Jacobian 同态的等式。
取实际正规化的 incidence 图并闭包后，
分歧点保原重数；支撑在一个 B 点上的集合是零维，
不能给对应另添一维“坏点修正”。
所以一般纤维的矩阵计数确实确定完整的一维对应。

(15)说明去掉 B 的平凡部分后，四字母标准表示
准确落到原六边表示的 $\iota=-1$ 部分。
由 R1039 的真正 $r^*:E_L\simeq\operatorname{Prym}(\widetilde C/C)$，
这给 $J_{\mathcal C_4}$ 的另一椭圆因子到同一个 E_L 的实际同源。
这里只需(15)，不将一个 ℓ 实现的投影当作未构造的 Chow 逆。

对 R1039 §§7–8 已付的无穷惰性超奇异 q，
原 $B$、$J_{\widetilde C}$ 都有真同态
$\mathrm F_q^2=[-q]$。Γ 和 $f_4$ 定义于 $\mathbf F_q$，
与 Frobenius 交换。
令 $u=\mathrm F_q^2+[q]$ 在 $J_{\mathcal C_4}$ 上。
则 $\Gamma u=0$、$f_{4*}u=0$，由(15)得 $[2]u=0$。
Hom 群无挠，故
$$
 \boxed{\mathrm F_q^2=[-q]\quad\text{在 }J_{\mathcal C_4}.}
\tag{16}
$$
这是真正的原四点谱盖的 Frobenius 输入。

## 4. Pell 单位及其原 B 范数的准确常数

由(16)及 $I_\pm\in\mathcal C_4(\mathbf F_q)$，
$$
 (q+1)(I_+-I_-)\sim0.
\tag{17}
$$
取在 $\mathbf F_q$ 上的函数 U，满足
$$
 \operatorname{div}(U)=(q+1)(I_+-I_-).
\tag{18}
$$
其一维函数空间由有限域 Hilbert 90 下降，
故不需扩常数域。
(9)的仿射坐标环是完整光滑仿射曲线的整闭环
$\mathbf F_q[v,H]/(H^2-Q_6)$。
U 与 $U^{-1}$ 都只可能在两个无穷点有极，
所以
$$
 U=A(v)+B(v)H,\qquad A,B\in\mathbf F_q[v],
$$
$$
 \boxed{A^2-Q_6B^2=c_U,\qquad c_U\in\mathbf F_q^\times.}
\tag{19}
$$
这是原四谱域中的实际单位，不是形式展开。
由(18)和两个无穷点的相反首项，
$$
 \deg A=q+1,\qquad \deg B=q-2,
 \qquad \operatorname{lc}(A)=-\operatorname{lc}(B).
\tag{20}
$$
U 唯一到一个非零常数；例如规定 $\operatorname{lc}(B)=1$
即完全固定 U。这里不假设 $I_+-I_-$ 的精确阶是 q+1；
即使其阶为真因子，取相应幂仍得到(18)及(20)。

现在取真正四度范数到原 B。
由(13)、(18)，其除子是
$(q+1)(T-(-T))$。
原 B 上
$$
 \operatorname{div}(Y)=3T-3O_B,\qquad
 \operatorname{div}(Y+1)=3(-T)-3O_B.
$$
置 $d=(q+1)/3$，先得范数等于常数乘
$(Y/(Y+1))^d$。该常数可以完全确定：
在 $O_B$ 上方，$D(v)=0$ 的两个不同 v 各有两个 H 符号，
共四点；(10)表明它们均不分歧。
每个 H 符号对的 U 值乘积恰为 $c_U$，
所以范数在该纤维的值为 $c_U^2$。
而 $Y/(Y+1)$ 在 $O_B$ 的值为1。
因此
$$
 \boxed{
 \operatorname{Nm}_{\mathcal C_4/B}(U)
 =c_U^2\left(\frac Y{Y+1}\right)^d.
 }
\tag{21}
$$
所有正负号、原点及常数都由原图确定。
特别 q 惰性且奇，d 为偶数，故
$$
 \operatorname{Nm}_{\mathcal C_4/B}(U)
 =\left[c_U\left(\frac Y{Y+1}\right)^{d/2}\right]^2.
\tag{22}
$$
这是原 $s_0=0$ 四谱域中的一个完整平方 Norm 输入；
(22)本身尚未给原 $s_0=1$ 两 quadric 点。

## 5. 原 Pell 单位的非零固定迹微分

还可把(18)–(21)压成低次数的精确微分关系。
因为 $\jmath_4U=c_U/U$，
$d\log U$ 是超椭圆反不变微分，
在有限处全正则，在 $I_\pm$ 仅有简单极。
因此存在次数≤2的 $F_q(v)$，使
$$
 d\log U=F_q(v)\frac{dv}{H}.
$$
在 $I_+$ 取局部参数 $1/v$，(18)的留数为 q+1，
在特征 q 中等于1。
在局部参数 $\rho=1/v$ 下，$dv/H$ 的首项为 $-\rho\,d\rho$，
所以二次首项准确为 −1。写为
$$
 \boxed{F_q(v)=-v^2+b_qv+c_q.}
\tag{23}
$$
这一微分非零，不能因为 Jac 的 Frobenius 特征值而删去。

比较 $dU=(d\log U)U$ 的两个函数域系数，得到
$$
 \boxed{
 A'=F_qB,\qquad
 Q_6B'+\frac{Q_6'}2B=F_qA.
 }
\tag{24}
$$
这保留实际 A、B 和所有低项，非一个仅在顶阶成立的近似 ODE。

有限可分对应的对数微分迹与 Norm 交换。
由(21)，且 $d=(q+1)/3=1/3$ 在 $\mathbf F_q$ 中，
$$
 \begin{aligned}
 \operatorname{Tr}_{\mathcal C_4/B}(d\log U)
 &=\frac13\,d\log\left(\frac Y{Y+1}\right)\\
 &=\frac{dX}{X(2Y+1)}.
 \end{aligned}
\tag{25}
$$
最后一步使用 $Y(Y+1)=X^3$ 和
$(2Y+1)dY=3X^2dX$。
(25)是同一个原 B 上固定、非零的第三类微分；
它在 T、−T 的留数分别为1、−1。
但此处的“非零”属于这个完整迹微分，
不能直接替代原最高 $P_-$、全 eta/Cor 或27对有权迹的非零。
特别在去掉 B 因子的投影下，仍须计算真正余下的部分。

## 6. 原两 quadric 点的两个真实半 Norm

现在令 q 为已付 Tate 范围内的惰性素数，
Q 为 R1027§8 的最短反 Frobenius 截面；
q=11 的实际 Q 亦满足同一已逐式证明的条件。
令原极除子 D 的度为 $e=(q-2)/3$，并保持
$$
 \operatorname{div}_\infty(x)=2D+2O_B,\qquad
 \deg(D+O_B)=d=(q+1)/3.
\tag{26}
$$
D 避开 $T,-T,O_B$。
原两个三挠截面为 $P_3=(0,0)$、$-P_3=(0,-t)$。
R1027 的实际端点保证 x 在两坏纤维都不为零；
在 canonical 好模型上 Q 亦不与这两个三挠截面重合。
因此 x 的零除子准确分成
$$
 D_+=(Q\cdot P_3),\qquad D_-=(Q\cdot(-P_3)),
$$
$$
 \operatorname{div}(x)=D_++D_--2D-2O_B.
\tag{27}
$$
它们在有限好纤维上，支撑互不相交。
反 Frobenius 性将两者交换，故各自次数为 d。
在原规范
$$
 y=(\delta W-x-t)/2,\qquad\delta^2=-3,
$$
两者分别由 $\delta W=t$、$\delta W=-t$ 识别。
这里只在 x=0 上使用这两式。

保持原 $F_Q=sR/(z-2X)+\delta u$，
其中 R1039 已证明
$$
 \operatorname{Nm}_{\widetilde C/C}(F_Q)=3x,\qquad
 u=\frac{1-w/(z^3-4)}6.
\tag{28}
$$
它的极除子准确为
$$
 \operatorname{div}_\infty(F_Q)
   =\pi^*f_3^*(D+O_B).
\tag{29}
$$
完整局部理由是：在 D 上，u 正则而 x 有偶数极阶，
所以由(28)和平方关系，两个 π 支都具有 D 的原重数。
在 $O_B$ 上方，f3 不分歧，u 只有简单极，
$sR/(z-2X)$ 至多简单极。
(28)的 x 具有二阶极，因此两个 π 支都必须恰为简单极，
不可能有一个支相消。其余点由平方关系均正则。
这证明(29)保全部厚点，未只比总次数。

按(27)将零除子也分成
$$
 \operatorname{div}_0(F_Q)=Z_++Z_-,
 \qquad \deg Z_+=\deg Z_-=3d=q+1,
\tag{30}
$$
其中 $Z_\pm$ 位于原 $D_\pm$ 上方。
每个三谱点恰选一个 π 支，
其重数是原交数，因为 $t\ne0$ 时 u 非零，
(28)的另一个 π 因子非零。

## 7. 两半由原四字母顶点准确标号

在一般三谱纤维上置
$$
 \nu_i=\frac{r_iR(z_i)}{z_i-2X}.
$$
定义 $u_i$ 为 u 的三个共轭。
由原方程可直接算得
$$
 2u_i^3-u_i^2+t=0,\qquad\prod_i u_i=-t/2.
\tag{31}
$$
另一方面，已付的两个 Norm 常数和原 W 方向给
$$
 \prod_i\nu_i
 =\frac{(3a/X)\operatorname{Nm}(R)}
         {\operatorname{Nm}(z-2X)}
 =\frac92W.
\tag{32}
$$
在 x=0 时，$\nu_i^2=(\delta u_i)^2$，置
$\epsilon_i=\nu_i/(\delta u_i)\in\{1,-1\}$。
由(31)–(32)，准确有
$$
 \boxed{\epsilon_1\epsilon_2\epsilon_3=-\delta W/t.}
\tag{33}
$$
这里正是原 W 的整体符号进入半 Norm 的位置。

在 $D_+$，右端为 −1，故四个偶符号顶点中
恰有一个使三个 $\epsilon_i$ 全为 −1。
该顶点的三个 incident 边正是 $F_Q$ 的三个零支。
在 $D_-$，右端为 +1，恰有一个顶点使三个
$\epsilon_i$ 全为 +1；它的三条邻边都不是零支，
三个对边才是零支。

因此原两个三挠交各自有唯一的四谱提升
$E_+,E_-$，次数均为 d，且准确有
$$
 \boxed{
 Z_+=\Gamma E_+,\qquad
 Z_-=\iota\Gamma E_-.
 }
\tag{34}
$$
这是原点到原两 quadric 的真实 incidence 接口。
$z-2X$ 在个别好点为零时，
其与 R 的比例按原函数域恒等式取正规化极限；
不能把那个完整点删去。
以上等式先在稠密开集证明，随后取有限闭包和原交重数，
所以也保留所有厚交。

因 $\delta^q=-\delta$，原 q-Frobenius 将
$D_+$ 送到 $D_-$，同时将“全负”的顶点条件送到“全正”。
故
$$
 \mathrm F_q(E_+)=E_-.
\tag{35}
$$
这里没有把 $\iota$、超椭圆 involution 与常数共轭混为一谈。

## 8. 保两半得到实际 $E_L(\mathbf F_q)$ 类

定义
$$
 \boxed{
 A_Q=[\,r_*\Gamma E_+-(q+1)O_{E_L}\,]\in E_L(\overline{\mathbf F}_q).
 }
\tag{36}
$$
这是原完整零除子的指定一半，不能从仅有的
$\operatorname{div}(N_Q)$ 中任意选一半来代替。

π 的两个点在 r 下互为负点。
所以对 C 的任意完整有效除子 A，
$r_*\pi^*A$ 相对 $2\deg(A)O_{E_L}$ 的类严格为0；
每个几何点对的和为0，厚重数也同样保留。
对(28)的完整主除子取 $r_*$，
再用(29)、(34)、$r\iota=[-1]r$，
得到
$$
 [\,r_*\Gamma E_+-(q+1)O_{E_L}\,]
 =
 [\,r_*\Gamma E_--(q+1)O_{E_L}\,].
\tag{37}
$$
结合(35)以及 r、Γ 的 $\mathbf F_q$ 定义，遂得
$$
 \boxed{A_Q\in E_L(\mathbf F_q).}
\tag{38}
$$
这为任意上述原最短反 Frobenius Q 成立，
不要求 $E_L$ 在 q 超奇异。
整体取 $(Q,R)\mapsto(-Q,-R)$ 交换两个指定提升，
由(37)可知不会改变 $A_Q$。

若再取 R1039 的无穷惰性超奇异 q，
则由真正 $\mathrm F_q^2=[-q]$ 得
$$
 \boxed{[q+1]A_Q=0.}
\tag{39}
$$
这一步是由原两三挠交、原 W 方向及全部 Norm 所构造的
真实类的限制，不是对一个另选常点给群阶估计。

(36)没有证明 $A_Q\ne0$，也没有把它预设为
R1039 固定边界 $(1,3)$ 的某个倍数。
q=11 的已执行“完整 N_Q 的有效除子类为 O”
仅是两半相减的结果，与(37)相容；
仍必须在原 $D_+,D_-$ 的方向下实际分离两半，才得到(36)。

## 9. 当前已经支付的接口与尚未支付的量词

(5)、(9)–(11)识别的是原两 quadric 的四点谱盖。
(15)给真正曲线对应，(16)给该同一个盖的无穷 Frobenius 输入。
(19)–(25)保 Pell 单位的全部系数、平方 Norm、准确常数
及固定非零迹微分。
(34)–(39)把实际 Q 的两个三挠交接回该四谱盖和原 Prym，
没有用完整 Norm 的零类代替指定半类。

后继须继续将 Pell 输入或真实半类返回原 $s_0=1$ 方程、
原27对有权交和最高投影。
平方 Norm 不自动产生两 quadric 的点；
固定非零第三类迹也不自动存活于最高 eta/Cor 投影。
无穷 q 以及(39)均不自动证明 q+1 有无穷多个不同素因子，
更不自动证明无穷目标普通 p 的局部 AJ 非零。

内部依据：R1027§8 的完整最短截面端点和极帽；
R1029 的原三谱域及纯 CM Frobenius；
R1031(19)–(24)的全部两式、Norm 常数和 W 方向；
R1039 的原 g 二盖、S4、准确 Prym 及 §§7–8 无穷输入。


## 10. 原 incidence 边界准确送到固定非挠点 P

本节保持 §§1–5 的同一四点谱盖和全部符号。
记
$$
 \Delta_\infty=[I_+]-[I_-],\quad
 T=(0,0),\quad
 R_0=(4,6),\quad P=(1,3)\in E_L,
$$
$$
 E_L:y_L^2=x_L^3-12x_L+20.
\tag{40}
$$
实际群律的倍点斜率为 $(3\cdot4^2-12)/(2\cdot6)=3$，故 $[2]R_0=P$。
R1039 已证明这个固定有理点 P 在特征零非挠。
这里计算的是真正曲线对应，不只比较两个椭圆因子的 j。

在 $I_+$ 上，原 $X\to0$、$Y\to0$，且
$\vartheta=a(v+1)$ 有极。
令 $c=3/X$，三谱根中一个趋于0，另外两个分别趋于
$L,-L$，其中 $L^2\sim-c$。
为使三个平方根之和 $\vartheta$ 有极，
后两个 $r_i$ 的首项必须相同，故其乘积首项为 $-c$。
由固定的 $r_1r_2r_3=ac$，趋于 $z=0$ 的那一根必须满足
$$
 s=r_1\longrightarrow-a.
\tag{41}
$$
相反的 $s=+a$ 不能给这个无穷顶点。
这一步同时付清了 incidence 边的正负方向。

因此 $\Gamma I_+$ 是原 $\widetilde C$ 上的以下三个点：
有限点 $(z,w,s)=(0,8,-a)$，
以及 $w/z^3\to+1$ 的原 C 无穷点上方两个 $s/z\to\pm1$ 支。
它们在 R1039 的准确映射
$$
 x_L=\frac{z-4a}{z-a},\qquad
 y_L=-\frac{3w}{s(z-a)^2}
\tag{42}
$$
下，分别是
$$
 R_0=(4,6),\qquad (1,-3),\qquad(1,3).
\tag{43}
$$
例如有限点的第二坐标为 $24/a^3=6$，
所以不是 $-R_0$。
超椭圆反演 $\jmath_4:(v,H)\mapsto(v,-H)$
交换 $I_\pm$；它在原六边盖上提升为
$\jmath:(z,w,s)\mapsto(z,-w,s)$，
并满足 $r\jmath=[-1]r$。
故另一个边界的三个像全部取负。
两对 $(1,\pm3)$ 在差中逐点抵消，得到**有效点除子的精确等式**
$$
 \boxed{
 r_*\Gamma\Delta_\infty=[R_0]-[-R_0].
 }
\tag{44}
$$
在 Jacobian 上，右端的类为 $[2]R_0=P$。
这一结论既没有丢三条边，也没有把分歧重数改成点集计数。

还能把这个固定点完整拉回。
令 $J=f_4^*f_{4*}$。
在四字母一般纤维上，$\Gamma^t\iota\Gamma$
的对角系数为0，非对角系数为2：
一条 incident 边的对边不含原顶点，
而其余任一顶点恰出现两次。因此与(15)合并，
$$
 \Gamma^t(1-\iota)\Gamma=4-J.
\tag{45}
$$
同 §3，有限正规化 incidence 的闭包保全分歧重数，
故这是实际曲线对应的等式。

又因 $r$ 的甲板 involution 是 $\kappa=\iota\jmath$，
而 $\jmath\Gamma\Delta_\infty=-\Gamma\Delta_\infty$
在除子层面就成立，
对(44)应用 $r^*$、再应用 $\Gamma^t$，得
$$
 \boxed{
 \Gamma^t r^*([R_0]-[-R_0])
   =4\Delta_\infty-f_4^*([T]-[-T]).
 }
\tag{46}
$$
这里 $f_{4*}\Delta_\infty=[T]-[-T]$。
所以真正去 B 的边界
$$
 \Delta_{\rm prim}
  =\Delta_\infty-\frac14 f_4^*([T]-[-T])
\tag{47}
$$
满足 $4\Delta_{\rm prim}=\Gamma^t r^*P$，
且 $r_*\Gamma\Delta_{\rm prim}=P$；
最后一步还使用
$\Gamma f_4^*=2(f_3\pi)^*$ 和 $r_*\pi^*=0$
在 Jacobian 上的原始等式。
于是特征零的 $\Delta_{\rm prim}$ 严格非挠。
这不是只因原 B 的边界非挠而作出的推断。

## 11. 全部范数将原 Pell 单位送成规范 Miller 函数

现在取 R1039 已付的无穷惰性超奇异 q，
置 $n=q+1$，并保持(18)–(21)的同一 U 和 $c_U$。
写
$$
 f=\frac Y{Y+1},\qquad d=n/3.
$$
令 $\mathscr I$ 为原 incidence 曲线的正规化，
$p:\mathscr I\to\mathcal C_4$ 为三度映射，
$q_{\mathscr I}:\mathscr I\to\widetilde C$ 为二度映射。
定义**整个** incidence 范数
$$
 U_\Gamma
  =\operatorname{Nm}_{q_{\mathscr I}}(p^*U)
       \in\mathbf F_q(\widetilde C)^\times.
\tag{48}
$$
在一个分裂的一般四字母纤维上，
若 $U_1,\ldots,U_4$ 是四个顶点的值，
则边 $\{i,j\}$ 上的值准确为 $U_iU_j$。

由 $\jmath_4U=c_U/U$，以及 $\iota$ 交换一对对边，
$$
 \jmath U_\Gamma=\frac{c_U^2}{U_\Gamma}.
$$
再取实际二度映射 $r$ 的全部范数
$$
 V=\operatorname{Nm}_r(U_\Gamma)\in\mathbf F_q(E_L)^\times.
$$
若 $\{k,l\}$ 是 $\{i,j\}$ 的对边，
$\kappa=\iota\jmath$ 给出完全确定的等式
$$
 \boxed{
 r^*V=c_U^2\,\frac{U_iU_j}{U_kU_l}.
 }
\tag{49}
$$
因此不是只按除子猜到 V 到一个常数：
两个规范范数已经固定了 V 的常数。

由(18)、(44)及 Norm 与除子的相容性，
$$
 \operatorname{div}(V)=n([R_0]-[-R_0]).
$$
而 $r\jmath=[-1]r$ 给
$$
 V\cdot[-1]^*V=c_U^4.
\tag{50}
$$
尚可在同一个好模型的 $O_{E_L}$ 处确定规范。
其两个原像为
$$
 P_0=(a,0,a\sqrt3),\qquad
 \iota P_0=(a,0,-a\sqrt3).
$$
这两点允许在二次常数扩域上读取；取完整 Norm 后仍回
$\mathbf F_q$。
在各点，原三谱根为 $a,a\omega,a\omega^2$，
后两根上的 g 值为0。
相应的一条边的两个端点恰是
$$
 v=-1+\sqrt3\quad\hbox{或}\quad v=-1-\sqrt3
$$
上的两个相反 H 支。
它们是 $D(v)=0$ 的真实四个好点；
每一对的 U 值乘积由(19)严格等于 $c_U$。
因此
$$
 U_\Gamma(P_0)=U_\Gamma(\iota P_0)=c_U,
 \qquad V(O_{E_L})=c_U^2.
\tag{51}
$$
这里没有额外的符号选择，也不依赖 $\sqrt3$ 是否已在基域。

置 $M=V/c_U^2$。遂得
$$
 \boxed{
 \operatorname{div}(M)=n([R_0]-[-R_0]),\quad
 M(O_{E_L})=1,\quad M\cdot[-1]^*M=1.
 }
\tag{52}
$$
对同一固定 $R_0$ 作真实平移，
$$
 m_{P,q}(Q)=M(Q-R_0),
$$
利用 $[2]R_0=P$，可写成
$$
 \boxed{
 \operatorname{div}(m_{P,q})=(q+1)([P]-[O_{E_L}]),
 \qquad m_{P,q}(R_0)=1.
 }
\tag{53}
$$
这就是原 Pell 单位经完整 incidence 和 Prym 范数所得、
在固定点规范的 Miller 函数。
此外 $m_{P,q}(P-Q)=m_{P,q}(Q)^{-1}$。
(53)并非另在 E_L 上选一个具有相同除子的函数：
(48)–(52)支付了其与原四点谱域的完整函数恒等式。

反向也有精确的乘法关系。
对四点谱盖上固定顶点 i，其三个 incident 边的
$r^*M$ 值乘积由(49)为
$$
 \prod_{j\ne i}\frac{U_iU_j}{U_kU_l}
       =\frac{U_i^4}{U_1U_2U_3U_4}.
$$
因此沿转置 incidence 的整个 Norm 满足
$$
 \boxed{
 \operatorname{Nm}_{\Gamma^t}(r^*M)
   =\frac{U^4}{\operatorname{Nm}_{\mathcal C_4/B}U}
   =\frac{U^4}{c_U^2 f^d}.
 }
\tag{54}
$$
左边定义为先沿 $\mathscr I\to\widetilde C$ 拉回，
再沿 $\mathscr I\to\mathcal C_4$ 取三度范数；
右边的 B 函数均按 $f_4$ 拉回。
一般纤维上的函数域等式自动保全正规化上的所有零极重数。
这付清了原 B 因子如何被去掉，而非只记录某个纯实现的同源关系。

## 12. 去 B 后的第三类部分确实非零

令 $\eta=d\log U$，并定义
$$
 \eta_{\rm prim}
   =\eta-\frac14f_4^*
         \left(\operatorname{Tr}_{\mathcal C_4/B}\eta\right).
\tag{55}
$$
其 B 迹为0。
由(25)，原迹微分在 $T,-T$ 的留数是 $1,-1$。
$f_4$ 在 $I_\pm$ 的分歧指数是2；
$\eta$ 在它们的留数分别为 $1,-1$。
故
$$
 \operatorname{res}_{I_+}\eta_{\rm prim}=\frac12,\qquad
 \operatorname{res}_{I_-}\eta_{\rm prim}=-\frac12.
\tag{56}
$$
其余两个位于 T 上方的不分歧点各有留数 $-1/4$，
另两个位于 $-T$ 上方的点各有留数 $1/4$。
这些就是(46)–(47)的完整原边界。
所以 $\eta_{\rm prim}\ne0$，不能因去掉 B 因子而删掉它。

进一步，Norm 与对数微分的准确相容性给
$$
 r_*\Gamma\eta=d\log V=d\log M.
$$
要将这里的 $\eta$ 换成 $\eta_{\rm prim}$，
还必须在第三类微分层面检查 B 项；
单独引用 Jacobian 的 $r_*\pi^*=0$ 不够。
置 $\beta=dX/[X(2Y+1)]$。
原 B 的 $[-1]:(X,Y)\mapsto(X,-1-Y)$ 满足
$[-1]^*\beta=-\beta$。
又 $\Gamma f_4^*=2(f_3\pi)^*$，
且 $f_3\pi\kappa=[-1]f_3\pi$。
因此 $(f_3\pi)^*\beta$ 在 r 的甲板 involution κ 下反不变，
其真正的二度微分迹为0。
这直接证明
$$
 \boxed{r_*\Gamma\eta_{\rm prim}=d\log M.}
\tag{57}
$$
右边在 $R_0,-R_0$ 的留数分别为
$q+1,-(q+1)$，在特征 q 中为 $1,-1$，因而严格非零。
这比只证明(25)非零更强：非零部分实际进入原 Prym 椭圆因子，
并由(52)–(54)的全部函数范数控制。

## 13. 这条固定边界尚须怎样被原最高投影消费

(44)、(46)、(53)、(54)、(57)均是原四谱盖、原六边 g 盖、
原 r 和固定 $P=(1,3)$ 之间的完整等式。
P 在特征零非挠，去 B 的边界在特征零非挠，
以及上述第三类微分在所选 q 中非零，都已得到证明。

这些对象属于原谱盖的 Prym 与其有标记点的扩张。
本节仍未将它等同于原 $H^3(2)$ 的最高 CM 线，
也未计算它对原全部27对、有限 eta 权及 Cor 的实际贡献。
后继必须保(48)–(54)的范数方向和指定边界，
在原有权交与最高投影中作真正的比较；
不能由这个低维非挠点或非零留数替代那一步。
同样，无穷 q 的(53)并未证明 q+1 具有无穷多个不同素因子。


## 14. 原四谱盖是实际 Q 的完整二分点盖

本节仍取 §6 的同一个实际最短反 Frobenius 截面 Q。
令原纤维的短坐标为
$$
 Y_Q=y_Q+(x_Q+t)/2=\delta W_Q/2.
$$
其三次多项式的根是 R1031 的 $\beta_i=-u_i^2$。
沿同一四字母顶点，置
$$
 \rho_i=\frac{\nu_i}{\delta}
 =\frac{r_iR(z_i)}{\delta(z_i-2X)},\quad
 A=\rho_1+\rho_2+\rho_3,\quad
 B_2=\rho_1\rho_2+\rho_1\rho_3+\rho_2\rho_3.
$$
原两 quadric 与原 Norm 符号准确给
$$
 \rho_i^2=x_Q-\beta_i,\qquad
 \rho_1\rho_2\rho_3=\delta W_Q/2=Y_Q.
\tag{58}
$$
后一个正号由(32)除以 $\delta^3=-3\delta$ 得到，
不允许将 R 的整体符号在此重新选择。
A 和 $B_2$ 是原顶点稳定子的不变量，
所以属于 $\mathbf F_{q^2}(\mathcal C_4)$，
而不需要取全 S4 分裂域作为新的基曲线。

定义同一个原椭圆纤维上的点 h：
$$
 \boxed{
 x_h=x_Q+B_2,\qquad Y_h=A B_2-Y_Q.
 }
\tag{59}
$$
它满足 $[2]h=Q$，可直接证明而不引用抽象二下降：
对 $\{i,j,k\}=\{1,2,3\}$，
$$
 x_h-\beta_i=(\rho_i+\rho_j)(\rho_i+\rho_k),
$$
$$
 Y_h=(\rho_1+\rho_2)(\rho_1+\rho_3)(\rho_2+\rho_3).
$$
因此 $Y_h^2=\prod_i(x_h-\beta_i)$。
该三次在 $x_h$ 的导数等于 $2A Y_h$，
故一般点的切线斜率为 A。
又 $\sum\rho_i^2=3x_Q+1/4$，
原短模型的二次系数是 $1/4$，于是倍点公式给
$$
 x([2]h)=A^2-\frac14-2x_h=x_Q,\qquad
 Y([2]h)=-Y_h+A(x_h-x_Q)=Y_Q.
\tag{60}
$$
这是函数域恒等式，分母或切线退化处由正规模型延拓，
不能删除这些点。
四个偶符号顶点恰给 Q 的全部四个二分点，
故不是只在某一分支上构造了一个点。

在 $D_+$ 的指定顶点，(33)–(34)给 $\rho_i=-u_i$。
由 $\sum u_i=1/2$、$\sum_{i<j}u_i u_j=0$，
这里 $(x_h,Y_h)=(0,-t/2)$，即 $h=-P_3$。
在 $D_-$ 的指定顶点则 $\rho_i=u_i$，故 $h=P_3$。
特别
$$
 E_+=(h\cdot(-P_3)).
\tag{61}
$$
在有限好纤维，倍点映射 étale，(61)保原交的全部重数。
下面还会检查坏纤维和 canonical fiber 没有额外的零截面交。

## 15. 完整二倍点除子给出 [4]A_Q=-P

置 $Z=h+P_3$，则
$$
 [2]Z=Q-P_3.
\tag{62}
$$
采用原 Weierstrass 坐标，令
$$
 \psi_2(Z)=2y(Z)+x(Z)+t.
$$
这是 $\mathcal C_4$ 上的真实有理函数；
可以在 $\mathbf F_{q^2}$ 上计算其除子，结果保原几何重数。

先在所有有限好纤维上计算。
$\psi_2$ 在非零二挠点有简单零，在零点有三阶极。
当 $[2]Z$ 与零截面相交时，
其原交数就是 $f_4^*D_+$ 的重数；
其中 $Z=O$ 的分支准确是 $E_+$。
因此这些好点的整个贡献为
$$
 f_4^*D_+-4E_+.
\tag{63}
$$
系数4不是只由次数猜出：
在 $Z=O$ 的支上，(63)的系数是 $1-4=-3$；
在另外三个非零二挠支上则是1。
倍点 étale 保所有厚交的交数。

现在逐点付两个乘法纤维。用
$\alpha=\operatorname{comp}_{I_3}(Q)\in\{1,-1\}$
表示 R1027§8 的定向分量，避免与 $a^3=4$ 混淆。
该节已证明
$\operatorname{comp}_{I_9}(Q)=0$、
$\operatorname{comp}_{I_9}(P_3)=3$，
而 $P_3$ 在 $I_3$ 的恒等分量。
四谱映射在 T 上有一个二重分歧点 $I_+$
和两个不分歧点，在 $-T$ 上同样为 $I_-$
和两个不分歧点。

在一个 $I_N$ 的 Tate 模型中，
若点的 Tate 参数阶为 $m$、$0<m<N$，
其正规化二除多项式的首项是非零单位乘
$u-\mathfrak q/u$。
所以只要 $m\ne N/2$，
$$
 \operatorname{ord}(\psi_2)=\min(m,N-m).
\tag{64}
$$
原模型和 Tate 模型的允许坐标变换只乘单位的三次方，
不改变这个阶。以下所有 m 均避开 $N/2$，
故没有未处理的首项抵消。

在 T，Q 的 Tate 参数是单位。
两个不分歧二分点 h 仍在分量0；
另两个二分点含 $\sqrt{\mathfrak q}$，
在二次分歧基变的 $I_{18}$ 上合成分量9。
加上原 $P_3$ 后，Z 的分量分别为3及 $9+6=15$。
在 $-T$，Q 的有符号 Tate 阶为 $\alpha=\pm1$。
含 $\sqrt{u_Q}$ 的两点在二次分歧基变后有分量
$\alpha\bmod6$，它们是 $I_-$；
另两点含 $\sqrt{u_Q\mathfrak q}$，不分歧且分量
$(\alpha+3)/2\bmod3$。
加上在恒等分量的 $P_3$ 不改变分量。
全部阶因此是
$$
 \begin{array}{c|c|c|c}
 \text{原基点}&\text{四盖上的支}&
       \text{Z 的分量}&\operatorname{ord}(\psi_2(Z))\\ \hline
 T&\text{两个不分歧支 }I_9&3&3\\
 T&I_+\text{，纤维 }I_{18}&15&3\\
 -T&\text{两个不分歧支 }I_3&1\text{ 或 }2&1\\
 -T&I_-\text{，纤维 }I_6&1\text{ 或 }5&1 .
 \end{array}
\tag{65}
$$
这些分量都非零，所以在这里 $Z\ne O$，
$[2]Z=Q-P_3$ 也不在零截面；(63)没有遗漏坏点交。

由 $f_4^*T=2I_+$ 加两个不分歧点，
T 的贡献准确为 $3f_4^*T-3I_+$；
同理 $-T$ 的贡献为 $f_4^*(-T)-I_-$。
最后在 $O_B$ 上的四个好点，
原 $\psi_2$ 与 minimal 好坐标相差基参数的三次负幂。
其 minimal 值是单位：若 $Z=O$ 或 Z 是非零二挠点，
由(62)都会有 $Q(O_B)=P_3(O_B)$；
但 Q 的值反 Frobenius、原三挠点的值 Frobenius 固定，
这会迫一个非零三挠点等于其负点，矛盾。
故这里的贡献**恰**为 $-3f_4^*O_B$。
也同样证明(61)没有 canonical 额外交。

合并得到完整主除子等式
$$
 \boxed{
 \begin{aligned}
 \operatorname{div}(\psi_2(Z))
  ={}&f_4^*D_+-4E_+
     +3f_4^*T+f_4^*(-T)\\
    &-3I_+-I_--3f_4^*O_B .
 \end{aligned}}
\tag{66}
$$
所有次数也吻合，但(66)已经逐点证明，不依靠次数补未知支。

同一函数的整个 Norm 常数也可准确核定。四个 $Z$ 是 $Q-P_3$
的全部二分点，所以
$$
 \boxed{\operatorname{Nm}_{\mathcal C_4/B}\psi_2(Z)
       =\Delta(t)=t^3(1-27t).}
\tag{66a}
$$
为确定常数，在一般短模型 $y^2=f(x)=\prod_i(x-e_i)$ 上，
$\operatorname{div}(\psi_2)=\sum_i[(e_i,0)]-3[O]$，
由 $[2]$ 推前得零，故全二分点乘积是常数。
令目标点趋 O，取其参数 $T=-x/y$。
O 支有 $\psi_2\sim-16/T^3$；各二挠支由不变微分
$dy/f'(e_i)$ 给 $\psi_2\sim f'(e_i)T$。
整个乘积为
$-16\prod_i f'(e_i)=16\operatorname{disc}(f)=\Delta$。
原 $\psi_2=2y+x+t$ 与判别式分别为权3、12，
故回到原 Tate 方程仍为(66a)，不增尺度。
(66)的完整推前同时给 $9T+3(-T)-12O_B$；
由 $t=-Y/27$，它正是这个 $\Delta(t)$ 的除子。
单一 Norm 条件不反推原两 quadric 已解。


对任意 $\mathcal C_4$ 除子 A，写
$$
 \Phi(A)=[r_*\Gamma A-3\deg(A)O_{E_L}].
$$
原等式 $\Gamma f_4^*=2(f_3\pi)^*$，
以及 r 下每个完整 π 对互为负点，给
$\Phi(f_4^*D)=0$，对任意次数的 B 除子 D 都成立。
由(43)–(44)，
$$
 \Phi(I_+)=R_0,\qquad \Phi(I_-)=-R_0,\qquad
 \Phi(E_+)=A_Q .
$$
在(66)上应用 $\Phi$，遂得
$$
 0=-[4]A_Q-[3]R_0+R_0,
 \qquad
 \boxed{[4]A_Q=-[2]R_0=-P.}
\tag{67}
$$
这是原指定半 Norm 的一般关系，保留整个群中的2幂信息。
它不要求 E_L 在 q 超奇异；
只要求本节实际 Q 满足已证明的反 Frobenius 与端点条件，
所以也直接适用于 q=11 的真实新截面。

## 16. 固定点关系的实际含义及最高投影边界

取实际有理点
$$
 G=(-2,-6),\qquad [2]G=R_0,\qquad[4]G=P
$$
把(67)进一步写成
$$
 \boxed{A_Q+G\in E_L(\mathbf F_q)[4].}
\tag{68}
$$
因此在倒2后的原群中，
$$
 \boxed{A_Q=-G\quad\text{于 }E_L(\mathbf F_q)\otimes\mathbf Z[1/2].}
\tag{69}
$$
这个固定低维部分已完全确定，不能再把它的非零误报为
Q 的未知有权变化。对于 q=11，公开指定半类消费的实际
$A_Q=-G$、阶16与(67)吻合；
这里没有根据那个单点输出猜测或执行一般公式。

在 R1039 的无穷惰性超奇异 q 上，
原 $[q+1]A_Q=0$ 仍成立，
与固定非挠 G 的模 q 约化相容。
这仍不产生 q+1 的无穷不同素因子量词。
同时，(66)给出了为何这个半类主要记录固定边界的
完整几何原因：去 B 后仅剩两个原分歧点的校正，
它们由(44)送到固定 P。

原最高 $\lambda$、有限 eta 权、Cor 与27对交仍须作用于
它们真正的对象。不能将(69)的固定常点直接代原 shadow；
尤其在 q=11，半类的阶16与原 shadow 的 $q+1=12$ 消去条件
本来不同。后继应保留原交函数及有标记除子，而非只取
已经由(67)–(69)确定的低维 Picard 类。


## 17. 第二个四度椭圆图的原坐标公式

本节将 $r_*\Gamma$ 的 Abel 和写成真实曲线映射，
并在特征零先相认，避免仅凭正特征微分相同而漏掉不可分同态。
对 $P'\in\mathcal C_4$，令
$$
 \Phi(P')=\sum_{E\in\Gamma P'}r(E)\in E_L
$$
取全部三条边及原重数的群和。加法映射
$\operatorname{Sym}^3(E_L)\to E_L$ 是正则的，
故这是完整光滑曲线上的映射，并且
$\Phi(I_\pm)=\pm R_0$。

记
$$
 K(v)=(v-2)(v+4),\quad
 N(v)=(v+1)(v+4),\quad
 L(v)=(v+4)^3-54 .
$$
准确公式为
$$
 \boxed{
 x_\Phi=\frac{4(N(v)^2-81)}{K(v)^2},\qquad
 y_\Phi=\frac{6H\,L(v)}{K(v)^3}.
 }
\tag{70}
$$
令 $R(v)=N(v)^2-81$。
直接展开有完整多项式恒等式
$$
 64R^3-48RK^4+20K^6=36Q_6L^2,
\tag{71}
$$
所以(70)确实落在原 $E_L$，没有改变其二次扭曲。
在 $v=2,-4$，分子分别为非零的 $2^2 3^5,-2^2 3^4$；
这两个 v 各有两个不同 H 支，
给 $O_{E_L}$ 的四个真实原像。
故(70)延拓为四度映射，对全部好特征 $q\ge5$ 保持四度。

还须证明它就是上述 incidence 的 Abel 和。
采用
$\omega_B=dX/(2Y+1)$、$\omega_L=dx_L/(2y_L)$。
由原 f3、r 的有理式，
$$
 f_3^*\omega_B=6\,dz/w,\qquad
 r^*\omega_L=-\frac a2\,s\,dz/w
             =-\frac{as}{12}(f_3\pi)^*\omega_B .
$$
沿三条 incident 边相加时 $\sum s=\vartheta=a(v+1)$，
而 $f_4^*\omega_B=6a\,dv/H$。
于是实际 Abel 和准确满足
$$
 \Phi^*\omega_L=-2(v+1)\frac{dv}{H}.
\tag{72}
$$
对(70)直接微分也给(72)，且 $I_+$ 的值是 $(4,6)$。
在特征零，两映射之差若非恒定，其拉回不变微分必非零；
故它们之差恒定，再由 $I_+$ 的值相同，知差为零。
这证明了(70)与原对应的完整相认。
随后约化同一函数恒等式；这里没有在特征 q 中以微分相同
推断两个映射相同。

(72)还确定全部分歧。
它的两个零恰为
$$
 v=-1,\quad H=\pm9.
$$
把它们代入(70)，得到
$$
 \boxed{\Phi(-1,\pm9)=(-4,\pm2)=\pm[3]R_0.}
\tag{73}
$$
$[3]R_0=(-4,2)$ 可直接用 $[2]R_0=P$ 及斜率1求出。
因此这个第二四度盖的真实分歧值是固定非挠点
$\pm[6]G$；它不是另选的 CM 椭圆商。

## 18. 非不变微分的固定 Miller 修正可以全部写出

(72)只描述不变微分；对 $d\log M$，
$\Gamma^t r^*$ 一般不等于 $\Phi^*$。
现在将其完整差项付清。

定义三个固定多项式
$$
 A_3(v)=v^3+5v^2+4v-9,\qquad
 J_3(v)=2v^3+15v^2+24v-43,
$$
$$
 B_3(v)=v^3+4v^2+8v+14,
$$
以及固定函数
$$
 \boxed{J(v,H)=\frac{H-A_3(v)}{H+A_3(v)}.}
\tag{74}
$$
逐项展开给
$$
 \boxed{
 Q_6-A_3(v)^2=(v^2-1)J_3(v),\quad
 x_\Phi-4=\frac{12J_3(v)}{K(v)^2},\quad
 A_3(v)L(v)+K(v)^3=J_3(v)B_3(v).
 }
\tag{75}
$$
这些等式保留常数与符号。

先在特征零比较全部除子。
在 $I_+$，$J\sim1/(2v)$；在 $I_-$，$J\sim2v$，
故它们的阶分别为1、−1。
在 $v=-1$ 的原 T 支，$H=9$、$A_3(v)=-9$；
在 $v=1$ 的原 T 支，$H=-1$、$A_3(v)=1$；
两点都是 J 的简单极，另两个 $-T$ 支是简单零。
在 $J_3(v)=0$ 的三个有限支，
(75)给 $H=-A_3(v)$ 时 $\Phi=R_0$，
$H=A_3(v)$ 时 $\Phi=-R_0$。
它们分别为 J 的简单极与简单零。
没有其它零极。因此
$$
 \boxed{
 \operatorname{div}(J)
  =4\Delta_\infty-f_4^*([T]-[-T])
      -\Phi^*([R_0]-[-R_0]).
 }
\tag{76}
$$
这也精确说明为什么不能把非不变第三类微分直接按(72)运输。
在特征 q 的重合或厚点上，继续使用(74)–(75)的函数恒等式，
不把这些点删去。

为确定函数级常数，取一般顶点对应的原三点除子
$D_E=E_1+E_2+E_3$ 在 $E_L$ 上，
其群和就是 $\Phi$。
用唯一的次数至多2多项式 $\ell(x)$ 插值这三个点的 y 坐标。
一般位置时
$$
 h_D(x,y)=\frac{y-\ell(x)}{x-x_\Phi}
$$
满足
$$
 \operatorname{div}(h_D)=D_E-[\Phi]-2[O_{E_L}].
\tag{77}
$$
理由是二次曲线 $y=\ell(x)$ 的第四个交点为 $-\Phi$；
分母准确消掉这一点并留下(77)。
在退化位置采用同一个有理函数族和原重数。

令
$$
 J_D=\frac{h_D(R_0)}{h_D(-R_0)}.
$$
在 $\mathcal C_4$ 上比较(77)在两个固定点的限制，
公共的竖直因子相消，得到
$$
 \operatorname{div}(J_D)
 =\Gamma^t r^*([R_0]-[-R_0])
       -\Phi^*([R_0]-[-R_0]).
$$
由(46)、(76)，$J_D/J$ 是常数。
超椭圆反演把三个 E 点全取负，
所以 $\ell\mapsto-\ell$，并给
$J_D\mapsto J_D^{-1}$；
(74)也满足 $\jmath_4J=J^{-1}$。
因此这个常数的平方为1。
本篇 $n=q+1$ 为偶数，故准确有 $J_D^n=J^n$；
这里没有遗留可能依 q 或顶点变化的比例。

现在对 §11 同一个规范 M 使用 Weil reciprocity。
其除子是 $n([R_0]-[-R_0])$，且 $M(O_{E_L})=1$。
由(77)，在一般位置上
$$
 \frac{\prod_{i=1}^3M(E_i)}{M(\Phi)}
  =\left(\frac{h_D(R_0)}{h_D(-R_0)}\right)^n
  =J^n .
$$
两边均是同一个函数域元素，所以延拓保所有厚点。
再将(54)代入，得到**带全部常数的原函数恒等式**
$$
 \boxed{
 \frac{U^4}{c_U^2f^d}
   =(\Phi^*M)\,J^{q+1}.
 }
\tag{78}
$$
其中 $f=Y/(Y+1)$，$d=(q+1)/3$，
U、M 分别是原四谱 Pell 单位与其完整范数所得的同一个函数，
并非只具有相同除子的另选函数。

对(78)取对数微分，在特征 q 中 $q+1=1$，遂得
$$
 \boxed{
 4\eta-f_4^*\operatorname{Tr}_{\mathcal C_4/B}\eta
     =\Phi^*(d\log M)+d\log J.
 }
\tag{79}
$$
左侧为 $4\eta_{\rm prim}$。
固定项 $d\log J$ 是实际 Miller 加法修正，
在本篇任何最高或有权运输中都不能免费删去。

## 19. 两条完整 holomorphic 线及其 Cartier 输入

(70)–(72)还给原四谱曲线的完整 holomorphic 分解。
对任意惰性好素数 q，写
$$
 \omega_0=dv/H,\qquad \omega_1=(v+1)\,dv/H,
$$
并令 $a_q(E_L)=q+1-\#E_L(\mathbf F_q)$。
原 B 在 q 超奇异，故其 Cartier 为0。
Cartier 与实际可分映射的拉回交换，
在一条椭圆曲线上的系数为 $a_q$ 的模 q 值。
于是
$$
 \boxed{
 \mathcal C(\omega_0)=0,\qquad
 \mathcal C(\omega_1)=a_q(E_L)\omega_1.
 }
\tag{80}
$$
这里的系数可用通常的 Hasse 公式直接核定：
对 $y^2=F(x)$，
$[x^{q-1}]F^{(q-1)/2}$ 同时是 Cartier 系数和
$a_q\bmod q$；后一等式将有限域点数和按幂次求和即得。
没有用未知的 EL 超奇异性替代原 B 的超奇异性。

更明确地，记
$$
 Q_6(v)^{(q-1)/2}=\sum_m \kappa_m v^m.
$$
Cartier 在显示模型中的系数公式与(80)给
$$
 \boxed{
 \kappa_{q-1}=\kappa_{2q-1}=0,\qquad
 \kappa_{q-2}=\kappa_{2q-2}=a_q(E_L)\pmod q.
 }
\tag{81}
$$
所以这四个原多项式系数由同一个实际非 CM 椭圆商控制；
无需扫描或重算已有有限 q。

对 §4 的无穷惰性超奇异 q，$a_q(E_L)=0$。
由于对数微分满足 $\mathcal C(d\log U)=d\log U$，
对(23)应用(80)后，两个低次系数也准确固定为
$$
 \boxed{
 b_q=-\kappa_{2q-3},\qquad c_q=-\kappa_{q-3}.
 }
\tag{82}
$$
其中 $\kappa_m$ 是刚定义的多项式系数，$c_q$ 保持(23)的常数项记号。
(82)保持整个原 Pell 对数微分，
但没有把这两条 weight1 线改名为原最高 weight3 线。
(78)–(79)所含的固定修正与原有限 eta/Cor 权
仍须在原标记交函数上一起消费。

