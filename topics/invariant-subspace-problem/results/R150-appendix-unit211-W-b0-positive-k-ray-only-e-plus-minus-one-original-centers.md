# R150：W/b0 的正 k 射线只余 e 剩余值正负一

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**结论。** 在当前 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 原图上，设 $1009$ 进赋值满足
$$
v(e)=0,\qquad v(k)=a>0.
\tag{1}
$$
那么任何原解的剩余值只能满足
$$
\boxed{\ \bar e=-1\quad\text{或}\quad\bar e=1.\ }
\tag{2}
$$
本条不排除 (2) 的两个中心。证明使用同一点的原 $b_0$、$q_2$、$R_6$ 和完整 NV 的 $f$ 常数系数 $N_5$。没有新的数学运行、首项门、系数缓存或旧投影重放；尤其不把定义 $N_5$ 解释为施加物理 $f=0$。

## 1. 原定义和准确适用范围

沿[负 e 射线的原 q2/R6 估值证明](R150-appendix-unit211-W-b0-negative-e-ray-complete-q2-R6-valuation-exclusion.md)中的同一权定义：
$$
u=e+1,\ Q=ek,\ \delta=1-Q,\ \bar V=uk+2,
$$
$$
\ell=\frac{u((k+2)^2-2ek)}{k\bar V},\quad
m=u-\ell,\quad M=\ell^2\delta-m^2,\quad bc=\frac{M}{4\delta},
$$
$$
J=2u(1-u)+\ell Q,\quad A_*=4uQ-J,\quad
C_*=A_*m^2+J\delta\ell^2.
\tag{3}
$$
同点原谱量为
$$
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\qquad K=\ell^2B_3-3\ell A_2T+2T^3.
\tag{4}
$$
本 $b_0$ 图上的原一次关系和两个完整必要式为
$$
A_*T=uQ\ell\mu,\qquad \mu=2\lambda-3,
\tag{5}
$$
$$
q_2=2A_2C_*+2M\ell Q(3-4\lambda)-8uQ\delta\ell T^2=0,
\tag{6}
$$
$$
R_6=MK^2-4m^2D^3=0.
\tag{7}
$$
(6) 由 $MA_*+C_*=4uQ\delta\ell^2$ 直接原式重写，不除 $A_*$ 的首值。

完整 $N_5$ 定义和原来源来自已刊源
[2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob 47281af16fdd0ad7500ecda377c3cb9f9d65e725，SHA256 e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8。本文只用其中已刊原定义，不执行其两个权标量、因式、gcd 或任何初始理想。

原 q2/N5 的必要性仍限于上述原图，尤其不外推到一般 $D_{\rm phys}=0$ 碰撞图。新估值证明中不倒 $D$，允许其首值下降。

## 2. 非异常剩余权的完整尺度

反设 (1) 有一个原解，且
$$
E=\bar e\ne-1,1,\qquad U=E+1,\qquad H=1-E.
\tag{8}
$$
$v(e)=0$ 已给 $E\ne0$。因此 $E,U,H$ 都是剩余域中的非零元。

以赋值环 $\mathcal O$ 及其极大理想 $\mathfrak m$ 记约化。由原有理式在 $k=0$ 的展开，
$$
\ell=\frac{2u}{k}+u(1-2e)+k\,r,\qquad r\in\mathcal O.
\tag{9}
$$
这是因为 $\bar V=2+uk$ 为赋值环单位。以下各比率先属于 $\mathcal O$，然后取剩余值：
$$
\overline{k\ell}=2U,\quad
\overline{km}=-2U,\quad
\overline{kM}=4U^2H,\quad
\overline{kbc}=U^2H.
\tag{10}
$$
又由 (9) 及 $2u(1-u)=-2eu$，
$$
\overline{J/k}=EU(1-2E),\qquad
\overline{A_*/k}=EU(2E+3).
\tag{11}
$$
(11) 允许零首值，不要求 $2E+3\ne0$。

用 $C_*$ 的两个实际项计算，
$$
\overline{kC_*}
=4EU^3(2E+3)+4EU^3(1-2E)=16EU^3,
\tag{12}
$$
$$
\overline{kM\ell Q}=8EU^3H,\qquad
\overline{8uQ\delta\ell}=16EU^2.
\tag{13}
$$
特别 $v(C_*)=-a$，$v(M\ell Q)=-a$，而 $8uQ\delta\ell$ 是赋值环单位。

## 3. 原 b0/q2 付 lambda 中心与 T 的上界

先不对 $\lambda$ 的估值作假设。若 $\mu\ne0$ 且 $s=v(\mu)\le0$，则由 (5)、$v(uQ\ell)=0$ 和 $v(A_*)\ge a$ 得
$$
v(T)=s-v(A_*)\le s-a.
\tag{14}
$$
这里 $A_*,T$ 的非零由 (5) 右端非零自动推出，没有支付 $A_*/k$ 的首值。

由 $\lambda=(\mu+3)/2$ 得 $v(A_2)\ge2s$、$v(3-4\lambda)\ge s\ge2s$。因此 (6) 的非 $T$ 两项估值至少 $-a+2s$；$T^2$ 项估值却至多 $-2a+2s$，严格较低，不能相消。故
$$
\mu=0\quad\text{或}\quad v(\mu)>0,\qquad
\bar\lambda=3/2,\quad \bar A_2=5/2,\quad\bar B_3=7/2.
\tag{15}
$$
这一步覆盖 $\lambda$ 极点及 $\lambda=0$，没有借用先前的模 lambda 中心计算。

原 (6) 给
$$
kT^2=
\frac{k(2A_2C_*+2M\ell Q(3-4\lambda))}
     {8uQ\delta\ell}\in\mathcal O.
$$
由 (12)–(15)，
$$
v(T)\ge-a/2,\qquad
\overline{kT^2}
=\frac{80EU^3-48EU^3H}{16EU^2}
=U(2+3E).
\tag{16}
$$
(16) 暂允许 $2+3E=0$ 和 $T=0$，没有先把它们删除。

## 4. 原 R6 的二次剩余约束

由 (4)、(10)、(15)、(16)，
$$
\overline{kD}=5U-U(2+3E)=3UH\ne0.
\tag{17}
$$
所以 $v(D)=-a$。$K$ 中 $\ell^2B_3$ 的估值恰为 $-2a$，而 $\ell A_2T,T^3$ 的估值均至少 $-3a/2$。故
$$
\overline{k^2K}=14U^2,\qquad v(K)=-2a.
\tag{18}
$$
完整原 (7) 乘 $k^5$ 后取剩余值，得到
$$
0=784U^6H-432U^5H^3
 =16U^5H\{49U-27H^2\}.
$$
由 (8)，必须
$$
P(E):=27E^2-103E-22=0.
\tag{19}
$$
这是同一点原矩式的必要首值约束，不是独立选择一个谱根。

在特征 $1009$ 下，
$$
P(-2/3)=176/3\ne0,\qquad
P(-5)=1168=159\ne0.
\tag{20}
$$
第一条结合 (16) 现在才给
$$
kT^2\in\mathcal O^\times,\qquad v(T)=-a/2.
\tag{21}
$$
因而 $T\ne0$，且 $w=\lambda-1-T$ 满足 $\overline{w/T}=-1$。$E=-3/2$ 从未被当作异常：$A_*/k$ 首值可以为零，以上所有估值仍成立。

## 5. 完整 N5 的原定义：只取 f 常数系数

沿旧源定义
$$
T_0=2u-\ell Q-2u^2,\quad \Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3,
$$
$$
G=\lambda P_{02}-(1-u)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0.
\tag{22}
$$
这些只是原恢复的系数定义。记原关于 $f$ 的常数系数为
$$
t_s=-\frac{P_c}{bcQ\Phi},\quad
V_s=-\frac GQ-\frac{P_c}{Q\Phi},\quad
W_s=T_0/2,\quad A_{1s}=2G/Q,
$$
$$
\theta=u-\ell Q,\quad
x_s=\frac{\theta V_s-mW_s}{M},\qquad
y_s=\frac{\ell W_s-uV_s}{M}.
\tag{23}
$$
这里的下标 $s$ 仅标示系数；没有令原解的物理 $f$ 为零。原定义直接满足
$$
A_{1s}=-2V_s+2bc\,t_s.
\tag{24}
$$

三个完整 NV 系数在该常数项中的表达为
$$
z_1=-2\{\ell(3-2\lambda)+2T\}y_s-2\ell w
 +\frac{mTt_s}{\delta},
$$
$$
z_2=2(\ell x_s-my_s-bct_s),
$$
$$
Z_0=\ell^2A_{1s}
 +2\ell u w\{\ell(3-2\lambda)+T\}
 +2V_s\{\ell^2+\ell(3-2\lambda)T+T^2\}
 +2bct_s(T^2-\ell^2).
\tag{25}
$$
最后
$$
N_5=2mD(Z_0+Dz_2)+MKz_1.
\tag{26}
$$
其必要性由旧完整原身份支付：
$$
N_5=2mD\ell^2NV+Mz_{1,\rm full}H_{\rm val}
 -2mDz_{2,\rm full}q-\frac{2f}{MQ}C_4,
$$
$$
q=M\sigma^2-D,\quad H_{\rm val}=K-2mD\sigma,\quad
C_4=2mDa_\Delta+MKb_0.
\tag{27}
$$
原值条件、$b_0=q_2=0$ 因而确实给 $N_5=0$。不同原值条件始终共用同一个 $\sigma,\lambda,T$；本文不把 (26) 另行选根，也不除 $D$。

## 6. N5 的最低项与原二次约束冲突

由前面尺度和 (22)，
$$
\bar T_0=-4EU,\quad
\bar\Phi=-4E^2,\quad
\bar P_{02}=8E^2U,\quad
\bar G=8E^2U,\quad
\bar P_c=48E^3U^2.
\tag{28}
$$
$QT$ 的估值至少 $a/2>0$，所以没有遗漏 (22) 中 $T$ 的较低项。由 (10)、(23)、(28)，
$$
t_s,x_s,y_s\in\mathcal O,\qquad
\bar t_s=\frac{12}{H},\qquad
\overline{kV_s}=4U(E+3),\qquad
\bar W_s=-2EU,
$$
$$
\bar x_s=\frac{3-6E-2E^2}{H},\qquad
\bar y_s=-\frac{2E+3}{H}.
\tag{29}
$$
这些分母的剩余非零性只用 (8)；没有付新权头。

因为 $T\ne0$，原 (5) 给
$$
\frac{\ell(3-2\lambda)}{T}=-\frac{A_*}{uQ}\in\mathcal O.
\tag{30}
$$
所以 (25) 的第一项在乘 $k/T$ 后落入 $\mathfrak m$。利用 $\overline{w/T}=-1$，
$$
\overline{\frac{kz_1}{T}}
=4U-\frac{24U}{H}
=-\frac{4U(E+5)}H.
\tag{31}
$$
这个剩余值可以为零；不逆 $E+5$。

(24) 使 $Z_0$ 中全部裸 $\ell^2$ 项准确相消，故
$$
Z_0=
2\{\ell(3-2\lambda)+T\}(\ell u w+V_sT)
 +2bct_sT^2.
\tag{32}
$$
由 (21)、(29)、(30)，
$$
v(Z_0)\ge-2a,\quad v(z_2)\ge-a,\quad
v\{2mD(Z_0+Dz_2)\}\ge-4a.
\tag{33}
$$
因此将整个 (26) 乘 $k^4/T$ 后，其第一项估值至少 $a/2>0$；第二项的剩余值由 (10)、(18)、(31) 完整给出：
$$
\overline{\frac{k^4N_5}{T}}
=(4U^2H)(14U^2)\left(-\frac{4U(E+5)}H\right)
=-224U^5(E+5).
\tag{34}
$$
原 $N_5=0$ 于是迫 $E=-5$。这与 (19)–(20) 矛盾。

由此排除 (8) 下的所有原解，证明 (2)。$E=-1$ 使 $u$ 的首值消失，$E=1$ 使 $M$ 的本尺度首值消失；这两个中心没有被上述除法使用，必须保留另作新原分析。

## 7. 结论边界

本条是三条既有原必要式之间的新完整估值推论，不是旧首项计算的重演，没有新增 actual、因式分解、GB 或结果式。完整 N5 的来源 (27) 和准确常数系数身份 (24) 是关键；不能用未证明的“物理 f=0”代替它们。

负 e 射线已由独立论文关闭；本条只把正 k 射线收紧到 (2)。两个剩余中心、另外其它未闭射线、完整原方程与所有新首项零面继续保留。没有证明全 W 空性、完整整权模型、额外点数界或普通 ISP。
