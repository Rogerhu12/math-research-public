# R150：W/b0 的 delta 正估值边界中整个 u 剩余二分之一支排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / r150_open_geometry。日期：2026-11-29（Asia/Taipei）。

**结论。** 在当前正确 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 原图中，剩余特征1009的赋值不存在
$$
v(e)=v(k)=0,\qquad v(\delta)>0,\qquad \bar u=\frac12,
\quad u=e+1,\quad Q=ek,\quad\delta=1-Q
\tag{1}
$$
的原解。这里自动有 $\bar k=-2$、$\bar\ell=1/2$、$\bar m=0$。本稿允许 mu 的任意极点、零值和单位，允许 $M=\ell^2\delta-m^2$ 任意深相消；没有将物理非零量当成赋值环单位。

证明只用已经成立的同点原 $b_0,q_2,R_6,N_5$，作新的完整纸面估值分层；**没有执行新门或重新执行旧门。** 一般 delta 边界的其他 u 剩余值，特别 $4u^2+2u-3=0$ 的首项退化及一般有限 mu 支，仍保留。本稿不宣整个 delta 边界或整个 W 排空。

## 1. 原来源、范围与准确恒等式

完整同点定义见 [原 b0/N5 源](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob **47281af16fdd0ad7500ecda377c3cb9f9d65e725**，SHA-256 **e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8**。这里只引用其原定义及已经付清的必要性，不重建或重跑该源的两个标量、QQ gcd、任何初始理想或局部 jet。

记
$$
\begin{gathered}
\ell=\frac{u((k+2)^2-2ek)}{k(uk+2)},\qquad m=u-\ell,\qquad
M=\ell^2\delta-m^2,\qquad bc=\frac{M}{4\delta},\\
J=2u(1-u)+\ell Q,\qquad A_*=4uQ-J,\qquad
C_*=A_*m^2+J\delta\ell^2,\\
\mu=2\lambda-3,\qquad
A_2=(\mu^2+4\mu+5)/2,\qquad
B_3=(\mu^3+6\mu^2+12\mu+7)/2 .
\end{gathered}
\tag{2}
$$
在本稿整个 b0 图，原关系给
$$
T=\kappa\mu,\qquad \kappa=\frac{uQ\ell}{A_*},
\quad D=\ell A_2-T^2,\quad
K=\ell^2B_3-3\ell A_2T+2T^3 .
\tag{3}
$$
准确原必要式为
$$
q_2=2C_*A_2+2M\ell Q(3-4\lambda)-8uQ\delta\ell T^2=0,
\qquad
R_6=MK^2-4m^2D^3=0 .
\tag{4}
$$
由 $MA_*+C_*=4uQ\delta\ell^2$，
$$
q_2=8uQ\delta\ell D
 -2M\{A_*A_2-\ell Q(3-4\lambda)\}.
$$
因此所有原点还满足
$$
D=MS,\qquad
S=\frac{A_*A_2-\ell Q(3-4\lambda)}{4uQ\delta\ell}.
\tag{5}
$$
(5) 是准确原式，不依赖任何首项不相消的假设。

下面使用的完整 N5 是原 N4 的 f 常数系数；这不施加物理 $f=0$。定义
$$
\begin{gathered}
T_0=2u-\ell Q-2u^2,\quad
\Phi=T_0+4u-4+Q,\\
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3,\\
G=\lambda P_{02}-(1-u)T_0,\qquad
P_c=QP_{02}(\ell+T)-GT_0,\\
t_s=-\frac{P_c}{bcQ\Phi},\qquad
V_s=-\frac GQ-\frac{P_c}{Q\Phi},\qquad
W_s=T_0/2,\qquad
y_s=\frac{\ell W_s-uV_s}{M},\\
w=\lambda-1-T,\qquad c_\lambda=-\mu,\\
z_1=-2(\ell c_\lambda+2T)y_s-2\ell w
                  +\frac{mTt_s}{\delta},\qquad
z_2=-\frac{2G}{Q}-4my_s,\\
Z_0=2(\ell c_\lambda+T)(\ell u w+V_sT)+2bc\,t_sT^2 .
\end{gathered}
\tag{6}
$$
最后一式由原 $A_{1,s}=-2V_s+2bc\,t_s$ 将完整 Z0 中三项 ell 平方部分精确相消得到，不是删去低阶或选取物理 f。原必要式是
$$
N_5=2mD(Z_0+Dz_2)+MKz_1=0 .
\tag{7}
$$
其完整来源为
$$
N_5=2mD\ell^2 NV+Mz_{1,\rm full}H
 -2mDz_{2,\rm full}q-\frac{2f}{MQ}C_4 .
\tag{8}
$$
当前 b0、q2 下原 C4 为零，所以 (7) 在同一个原点成立。(8) 只正乘 D，不反演 D，也不把数个不同范数的零点拼成同一点。

在 (1) 中 $u,Q,\ell,A_*,\Phi$ 的剩余分别为 $1/2,1,1/2,1,-1$，均为赋值环单位；m、delta、M 可以有任意正阶。它们在原物理图是非零量，故 (6) 作为赋值域中的准确恢复合法。D 在当前 W 物理图非零，R6 随之保证 K 非零。

## 2. 两个统一的局部参数与余项控制

置
$$
a=v(m)>0,\qquad d=v(\delta)>0,\qquad \varepsilon=\mu+2=2\lambda-1.
$$
用 $Q=1-\delta$ 写 W 权关系，
$$
m=\frac{u(u-1)(Q-2)(Q+2u-2)}
        {Q(uQ+2u-2)} .
\tag{9}
$$
在 $(u,\delta)=(1/2,0)$，右端对 u 的导数是 -1。因此可在 $\mathbb Z_{(1009)}$ 的完成局部环内，唯一地把 u 写成 (m,delta) 的整形式幂级数。必要时先取赋值环的完备化，不改变任何非零首项或原等式。

以下 $O_j$ 表示所列局部参数的 j 次幂理想，系数均在该整局部环；它们不是未经控制的数值近似。权恢复首先给
$$
\begin{aligned}
u&=\tfrac12+\tfrac\delta2-m+O_2(m,\delta),&
\ell&=\tfrac12+\tfrac\delta2-2m+O_2(m,\delta),\\
A_*&=1-2m+O_2(m,\delta),&
\kappa&=\tfrac14+\tfrac\delta4-m+O_2(m,\delta).
\end{aligned}
\tag{10}
$$
另有准确身份
$$
2\kappa-\ell
=\frac{\ell(J-2uQ)}{A_*},\qquad
J-2uQ=-\frac{mQ^2(2u-1)}{(u-1)(Q-2)} .
\tag{11}
$$
所以 $2\kappa-\ell\in(m,\delta)^2$。这一点在 $y_s$ 有极点时仍控制完整 z1，不可只用 $\bar\kappa=\bar\ell/2$ 代替。

q2 对 mu 的次数至多二，且准确属于 $(\delta,m^2)$。其两项最低系数为
$$
q_2=\delta\left\{\frac{(\mu+2)^2}{8}
                 +(m,\delta)\,\mathbb Z_{(1009)}[[m,\delta]][\mu]_{\le2}\right\}
 +m^2\left\{(\mu+2)(\mu+4)
                 +(m,\delta)\,\mathbb Z_{(1009)}[[m,\delta]][\mu]_{\le2}\right\}.
\tag{12}
$$
在 $\bar\mu=-2$ 的图，进一步准确有
$$
q_2=\frac32\delta m-\frac12\delta^2+2m^3+2m^2\varepsilon+\mathcal R,
\tag{13}
$$
其中
$$
\mathcal R\in
(\delta\varepsilon^2,\delta m\varepsilon,\delta^2\varepsilon,
 \delta m^2,\delta^2m,\delta^3,
 m^3\varepsilon,m^2\varepsilon^2,m^4).
\tag{14}
$$
(12) 可直接从 delta=0 时 $M=-m^2$ 及 (5) 读取；(13) 的二阶部分来自
$8uQ\delta\ell D-2M\{A_*A_2-\ell Q(3-4\lambda)\}$，
而 delta=0 时其三阶部分为 $2m^2(m+\varepsilon)$。所以 (14) 控制了所有后续相对阶，不假设 a 与 d 是整数或互为倍数。

当 epsilon 正阶时，完整恢复的必要初项是
$$
\begin{aligned}
D&=m-\delta/4+\varepsilon/4+O_2(m,\delta,\varepsilon),\\
K&=m-\delta/4+3\varepsilon/16+O_2(m,\delta,\varepsilon),\\
T_0&=2m+O_2(m,\delta),&
P_{02}&=m+\delta/2+O_2(m,\delta),\\
G&=-m/2+\delta/4+O_2(m,\delta,\varepsilon),\\
P_c&=m^2-m\delta/2+m\varepsilon/4+\delta\varepsilon/8
                         +O_3(m,\delta,\varepsilon).
\end{aligned}
\tag{15}
$$
epsilon 恰为零也保留：需要时以 $v(\varepsilon)=+\infty$ 理解。

## 3. mu 的所有极点及非负二剩余

### 3.1 mu 极点全部排除

若 $d<2a$，(12) 的 mu 平方头由 delta/8 独占；若 $d>2a$，由 m 平方独占。故 mu 有极点时 q2 在这两种情况下不可能为零。

若 $d=2a$，记 $z=\overline{\delta/m^2}\ne0$。mu 极点只能在 z=-8 时使该头相消。然而此时
$$
M/m^2\longrightarrow-3,\qquad
D/\mu^2\longrightarrow3/16,\qquad
K/\mu^3\longrightarrow-1/32,
$$
从而
$$
R_6/(m^2\mu^6)\longrightarrow-30/1024\ne0
\quad\text{于剩余特征1009。}
\tag{16}
$$
所以所有 mu 极点均排除。

### 3.2 d 不等于二倍 a

mu 整后，若 $d<2a$，(12) 强迫 $\bar\mu=-2$；若 $d>2a$，只可能 $\bar\mu=-2,-4$。后者在 $\bar\mu=-4$ 时
$$
D\longrightarrow1/4,\quad K\longrightarrow5/8,\quad
R_6/m^2\longrightarrow-29/64\ne0.
$$
因此这些图都只需继续 $\bar\mu=-2$。

### 3.3 d 等于二倍 a、mu 剩余不等于负二

由 (12)，
$$
z=-\frac{8(\bar\mu+4)}{\bar\mu+2}.
\tag{17}
$$
本小节在剩余域中省略 mu 上的横线，记
$$
J_1=3\mu+10,\qquad H_1=-\mu^2+2\mu+14.
$$
准确剩余为
$$
D_0=\frac{(\mu+2)J_1}{16},\qquad
K_0=\frac{(\mu+2)H_1}{32},\qquad
z-4=-\frac{4J_1}{\mu+2}.
\tag{18}
$$

先保 z=4 的整深 M 支。此时 $\mu=-10/3$，$K_0=17/108$ 非零；令 $\gamma=v(M)>2a$。(5) 的分子剩余是 $-4/9$，分母阶为 $2a$，故 $v(D)=\gamma-2a$。R6 两项阶为 gamma 与 $3\gamma-4a$，只能在 gamma=2a 时相等，矛盾。这里没有把深 M 当作一般支。

余下 z 不等于4，D0 非零。由完整 (6) 逐项取初项，得
$$
\begin{gathered}
G/m\to(\mu+1)/2,\quad P_c/m\to(\mu+2)/4,\quad
V_s/m\to-\mu/4,\quad
t_s/m\to\frac{4z(\mu+2)}{z-4},\\
my_s\to\frac{\mu+4}{2(z-4)},\qquad
z_2\to-\frac{2(\mu+4)}{z-4},\\
z_1\to\frac{(\mu+2)(4\mu-z+4)}{4(z-4)},\qquad
Z_0\to-\frac{\mu(\mu+2)}{32}.
\end{gathered}
\tag{19}
$$
(11) 保证 z1 第一项即使 $y_s$ 有极点也不产生漏掉的常数项。代 (17) 后，
$$
Z_0+D_0z_2=\frac{(\mu+2)(\mu^2+5\mu+8)}{32}.
\tag{20}
$$
N5 的第一项阶至少 a，第二项阶至少 2a；D0 非零且 mu+2 非零，所以原 N5 必迫
$$
\mu^2+5\mu+8=0 .
\tag{21}
$$
同一个 R6 剩余则迫
$$
H_1^2+(\mu+2)^2J_1^2=0.
\tag{22}
$$
在 (21) 下 $H_1=7\mu+22$、$(\mu+2)J_1=\mu-4$，(22) 左侧恰为 $50(\mu+2)$，非零。这一整支排除。它保所有剩余域嵌入，不挑选 (21) 的一个根。

此后全局只余 $\bar\mu=-2$。

## 4. d 小于二倍 a：三个完整区间

此时 $M/\delta\to1/4$。由原 R6，
$$
2v(K)=2a-d+3v(D),\qquad v(K)>v(D)>0.
\tag{23}
$$
若 epsilon 的阶严格小于 a、d，两项 D、K 都由 epsilon 独占而同阶，与 (23) 冲突。因此 $v(\varepsilon)\ge\min(a,d)$；后续的 K 首项相消均由 (23) 强迫，不是额外假设。

若 d<a，(15) 迫
$$
\varepsilon/\delta\to4/3,\qquad D/\delta\to1/12.
$$
但 (13) 的唯一最低项是 $-\delta^2/2$，矛盾。

若 $a<d<2a$，同理
$$
\varepsilon/m\to-16/3,\qquad D/m\to-1/3.
$$
(13) 的唯一最低项是 $3\delta m/2$，仍矛盾。余项 (14) 在这两个区间均严格更高。

现在 d=a。置 $z=\overline{\delta/m}\ne0$，(13) 的二阶部分给 $z(3-z)=0$，故
$$
\delta/m\to3.
$$
由 (15)、(23)，
$$
\varepsilon/m\to-4/3,\qquad D/m\to-1/12,\qquad v(K)=2a.
\tag{24}
$$
这一比例必须用完整 N5，不能只凭 q/R 声称排空。完整 (6) 给
$$
\begin{gathered}
bc\to1/16,\quad T_0/m\to2,\quad P_{02}/m\to5/2,\quad G/m\to1/4,\\
P_c/m^2\to-4/3,\quad t_s/m^2\to-64/3,\quad
V_s/m\to-1/4,\quad y_s\to5/6,\quad w/m\to-5/6,\\
v(z_1)\ge a,\qquad v(z_2)\ge a,\qquad Z_0/m\to-1/12 .
\end{gathered}
\tag{25}
$$
特别 $Dz_2$ 比 Z0 高阶，而 $MKz_1$ 阶至少4a。于是
$$
N_5/m^3\longrightarrow
2(-1/12)(-1/12)=1/72\ne0.
\tag{26}
$$
d=a 的全部更深首项修正也因这个非零剩余而排除。

## 5. d 大于二倍 a

此时 $M/m^2\to-1$，R6 给
$$
v(K)=3v(D)/2>v(D).
$$
由 (15) 必有
$$
v(\varepsilon)=a,\qquad
\varepsilon/m\to-16/3,\qquad D/m\to-1/3.
$$
(13)、(14) 的最低三阶项给
$$
q_2/m^3\longrightarrow2+2(-16/3)=-26/3\ne0.
\tag{27}
$$
故本区间全部排除。

## 6. d 等于二倍 a：非深 M 与整深 M

记 $z=\overline{\delta/m^2}\ne0$。

### 6.1 z 不等于四

这时 $M/m^2\to(z-4)/4\ne0$。和上节一样，
$$
\varepsilon/m\to-16/3,\quad D/m\to-1/3,\quad v(K)=3a/2 .
$$
由 (13) 的三阶系数，
$$
\frac32z-\frac{26}{3}=0,\qquad
z=\frac{52}{9}.
\tag{28}
$$
在这个比例，完整原 N5 的各必要初项是
$$
\begin{gathered}
M/m^2\to4/9,\qquad bc\to1/52,\qquad
T_0/m\to2,\quad P_{02}/m\to1,\quad G/m\to-1/2,\\
P_c/m^2\to-1/3,\quad t_s/m^2\to-52/3,\quad
V_s/m\to1/2,\quad my_s\to9/16,\quad w/m\to-10/3,\\
z_2\to-9/4,\qquad v(z_1)\ge a,\qquad
Z_0/m\to-13/12,\qquad (Z_0+Dz_2)/m\to-1/3.
\end{gathered}
\tag{29}
$$
z1 的阶界再次使用准确 (11)，而非只看其表面上含极点的 y_s。第二项 $MKz_1$ 的阶至少 $9a/2$，因此
$$
N_5/m^3\longrightarrow2(-1/3)(-1/3)=2/9\ne0.
\tag{30}
$$
该比例的所有后续修正均排除。

### 6.2 z 等于四：M 任意深相消

令 $\gamma=v(M)>2a$，不设任何上界。若 $v(\varepsilon)<a$，(5) 的原 q2 形式中第一项阶为 $2a+v(\varepsilon)$，第二项至少 $\gamma+v(\varepsilon)$，不可能相消。故 epsilon 阶至少 a。

若 D 在 (15) 的一阶部分不相消，q2 第一项阶3a，第二项至少 gamma+a，仍不可能。因此
$$
\varepsilon/m\to-4,\qquad K/m\to1/4 .
$$
此时 (5) 的分子除 m 趋于 $1-4=-3$，分母除 delta 趋于1，所以
$$
v(S)=-a,\qquad v(D)=\gamma-a .
\tag{31}
$$
R6 两项阶分别为 gamma+2a 与 $3\gamma-a$。相等会迫 $\gamma=3a/2$，和 gamma>2a 矛盾。整深 M 支排除，不曾把 M 的首项强加为单位。

## 7. 完整覆盖与结论边界

第3节覆盖 mu 全部极点及所有非负二剩余；第4至6节覆盖 mu 剩余负二时
$$
d<a,\quad d=a,\quad a<d<2a,\quad d=2a,\quad d>2a,
$$
并在 d=2a 中明确覆盖 M 首项相消的所有深度。每个最终非零常数在特征1009下仍非零。所有分歧及剩余域扩张均保，epsilon=0、mu=0 也未被先行删除。

因此 (1) 的整个原 DVR 边界为空。证明使用的是同一个物理原点上的准确 b0、q2、R6 和完整 N5；(25)、(29) 中的 f 常数恢复只提供原 N5 的已刊表达，没有令原物理 f 为零。本结论与先前 u 正估值、正负权射线以及其他内部边界分别成立；它只关闭当前 delta 正估值图的 u 剩余二分之一分支。

**执行说明。** 本稿是新纸面分层及原式推导，没有新脚本、Actions run、重放、增限、因式计算或证书载荷。来源仍是第1节既有完整原定义；后续其他 delta 剩余分支须另给完整原输入或纸面证明。
