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
