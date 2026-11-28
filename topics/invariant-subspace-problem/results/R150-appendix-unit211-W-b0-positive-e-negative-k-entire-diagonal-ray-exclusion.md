# R150：W/b0 的正 e、负 k 对角射线完整原排除

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**结论。** 当前 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 原图不存在满足
$$
v(e)=a>0,\qquad v(k)=-a,\qquad v(Q)=v(ek)=0
\tag{1}
$$
的 $1009$ 进原解。证明保留 $\bar Q=1$ 时 $\delta=1-Q$、$M$ 的全部下降阶，保留 $\lambda$ 的极点、零剩余值和高阶相消；只用同点原 $b_0,q_2,R_6,N_5$。没有新的运行、旧初始理想重放或系数缓存。

本条仅关闭 (1)，不宣布其它未闭权射线或整个 W 排空。

## 1. 原定义和完整 NV 必要式

设 $F$ 是包含假想原解的 $1009$ 进代数扩张，$\mathcal O$ 为赋值环、$\mathfrak m$ 为极大理想。约化后特征为 $1009$。所有写出剩余值的商均先由相应尺度证明整。

令
$$
r=e,\quad v(r)=a>0,\quad k=Q/r,\quad u=1+r,\quad \delta=1-Q.
$$
原权恢复为
$$
\ell=\frac{(1+r)\{Q^2+4Qr+(4-2Q)r^2\}}
 {Q\{Q+(Q+2)r\}},\qquad m=u-\ell,\qquad
M=\ell^2\delta-m^2,\qquad bc=\frac M{4\delta}.
\tag{2}
$$
原 $Q,\delta,M$ 均非零，但没有假设它们的剩余值非零。

记
$$
J=2u(1-u)+\ell Q,\quad A_*=4uQ-J,\quad
C_*=A_*m^2+J\delta\ell^2,\qquad \mu=2\lambda-3,
$$
$$
A_2=(\mu^2+4\mu+5)/2,\quad
B_3=(\mu^3+6\mu^2+12\mu+7)/2,
$$
$$
D=\ell A_2-T^2,\qquad K=\ell^2B_3-3\ell A_2T+2T^3.
$$
本图原必要式是
$$
A_*T=uQ\ell\mu,
\tag{3}
$$
$$
q_2=2C_*A_2+2M\ell Q(3-4\lambda)
       -8uQ\delta\ell T^2=0,
\tag{4}
$$
$$
R_6=MK^2-4m^2D^3=0.
\tag{5}
$$
由 $MA_*+C_*=4uQ\delta\ell^2$，还保留准确原身份
$$
D=M S,\qquad
S=\frac{A_*A_2-\ell Q(3-4\lambda)}
        {4uQ\delta\ell}.
\tag{6}
$$
其分母都是旧已付权；没有倒 $D,S$ 或其首项。

完整原 $N_5$ 沿已刊源
[2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob 47281af16fdd0ad7500ecda377c3cb9f9d65e725，SHA256 e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8。这里仅使用原定义，不执行原源的任何旧目标。

为完整保留同点原值，记
$$
T_0=2u-\ell Q-2u^2,\quad
\Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3,\quad
G=\lambda P_{02}-(1-u)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0,
$$
$$
bct_s=-\frac{P_c}{Q\Phi},\quad
V_s=-\frac GQ-\frac{P_c}{Q\Phi},\quad W_s=T_0/2,
$$
$$
x_s=\frac{(u-\ell Q)V_s-mW_s}{M},\qquad
y_s=\frac{\ell W_s-uV_s}{M},\quad
w=\lambda-1-T,\quad c_\lambda=3-2\lambda,
$$
$$
z_1=-2(\ell c_\lambda+2T)y_s-2\ell w+\frac{mTt_s}{\delta},
\qquad z_2=-2G/Q-4my_s,
$$
$$
Z_0=2(\ell c_\lambda+T)(\ell u w+V_sT)+2bc\,t_sT^2.
\tag{7}
$$
完整必要式是
$$
\boxed{\ N_5=2mD(Z_0+Dz_2)+MKz_1=0.\ }
\tag{8}
$$
这些量是原 $f$ 常数系数，绝不是额外施加的物理 $f=0$。完整来源仍为
$$
N_5=2mD\ell^2NV+M z_{1,\rm full}H_{\rm val}
       -2mD z_{2,\rm full}q-\frac{2f}{MQ}C_4,
$$
$$
q=M\sigma^2-D,\qquad H_{\rm val}=K-2mD\sigma.
$$
当前原 $b_0,q_2$ 已使 $C_4=0$。所有后续首项均来自 (7)–(8)，不以个别 NV 分量或独立范数根替代完整值。

## 2. 全 Q 单位的基本展开

由 (2)，在 $Q$ 为单位的整个本图，
$$
\ell=1+\frac{2r}{Q}+O(r^2),\qquad
m=\frac{Q-2}{Q}r+O(r^2),\qquad J=Q+O(r^2),
$$
$$
A_*=3Q+4Qr+O(r^2),\qquad
\kappa=\frac{uQ\ell}{A_*}
=\frac13+\frac{6-Q}{9Q}r+O(r^2),\qquad T=\kappa\mu .
\tag{9}
$$
$A_*$ 的首项 $3\bar Q$ 在这里已经证明非零。没有选取新的头开图。

在 $\lambda\in\mathfrak m$ 的中心，直接展开 (9) 与原 D、K，得到
$$
D=-\frac23\lambda+\frac{2(Q-3)}{3Q}r
       +O((\lambda,r)^2),
$$
$$
K=-\lambda+\frac{Q-4}{Q}r
       +O((\lambda,r)^2).
\tag{10}
$$
这些是以整参数 Q 为系数的准确一阶式；$Q$ 变化不会引入与 $\lambda,r$ 无关的新常数项。

## 3. Q 剩余不等于一

设 $q=\bar Q\ne1$，故 $\delta$ 为赋值环单位。此时 $M\to1-q$。原 (4) 的最高系数在 $r=0$ 准确给
$$
q(1-q)(\mu^2/9-1)=0.
\tag{11}
$$
其二次头非零，所以 $\mu$ 没有极点，剩余值只可能是 $\pm3$。

若 $\bar\mu=3$，则 $\bar\lambda=3,\bar T=1$，
$$
\bar A_2=13,\quad\bar B_3=62,\quad\bar D=12,\quad\bar K=25.
$$
(5) 左项是单位，右项至少有正估值 $2a$，矛盾。

若 $\bar\mu=-3$，则 $\lambda\in\mathfrak m$。原 q2 在此简单根的一阶式为
$$
q_2=-\frac{4Q\delta}{3}\lambda
     -\frac{4\delta(2Q+3)}3r+O((\lambda,r)^2).
$$
故
$$
\lambda/r\to-\frac{2q+3}{q},\qquad
D/r\to2,\qquad K/r\to\frac{3q-1}{q}.
\tag{12}
$$
$\lambda/r$ 的首值允许为零。由 (5)，若最后一个首值非零，左项估值 $2a$、右项至少 $5a$，矛盾。唯一可能为
$$
q=1/3.
\tag{13}
$$

### 3.1 完整 N5 排除 q=1/3

在 (13)，有
$$
m/r\to-5,\quad D/r\to2,\quad M\to2/3,\quad
\lambda/r\to-11,\quad (T+1)/r\to-13,\quad w/r\to2.
$$
原 (5) 准确迫
$$
v(K)=5a/2.
\tag{14}
$$
由完整 (7)，
$$
P_{02}/r\to2/3,\quad G/r\to-1/3,\quad
\Phi/r^2\to-2,\quad P_c/r\to-1/9,
$$
$$
r\,bct_s,\ rV_s\to-1/6,\quad ry_s\to1/4,\quad
rz_1\to-1/2,\quad z_2\to5,\quad rZ_0\to1/3 .
\tag{15}
$$
因此 (8) 第一项的 $r$ 系数为 $-20/3$，第二项估值为
$5a/2-a=3a/2>a$。所以
$$
N_5/r\to-20/3\ne0.
$$
矛盾。整个 $q\ne1$ 分支已排除。

## 4. Q 剩余为一：delta 与 e² 的全部相对估值

现在设 $q=1$，令
$$
d=v(\delta)>0.
$$
由 (9)，$m/r\to-1$、$\kappa\to1/3$。在 $\mu$ 为整量时，原 (4) 的最低两组二次系数为
$$
r^2(\mu+3)(3\mu+7)+\delta(\mu^2/9-1).
\tag{16}
$$
这是由原式按 $\delta,m^2$ 分组得到，不先支付 $M$ 的首值。

### 4.1 delta 估值小于 2a

若 $d<2a$，则 $M/\delta\to1$。(16) 先排 $\mu$ 极点，再给 $\bar\mu=\pm3$。$\bar\mu=3$ 时 (5) 两项估值分别为 $d$ 与 $2a$，矛盾。

在 $\bar\mu=-3$ 中，把 q2 除以 $\delta$。其 lambda 一次系数趋 $-4/3$，原常数项除以 r 趋 $-20/3$；$m^2/\delta$ 的所有修正有正估值。故
$$
\lambda/r\to-5,\quad D/r\to2,\quad K/r\to2.
$$
(5) 两项估值是 $d+2a$ 与 $5a$，仍不相等。这里包括 $d$ 比 a 大或小的所有情形，不要求裸 Q 专门化保持某个多项式次数。

### 4.2 delta 估值大于 2a

若 $d>2a$，则 $M/r^2\to-1$。(16) 排除 $\mu$ 极点，整 lambda 的余根只可能为
$$
\bar\lambda=0\quad\text{或}\quad1/3.
$$
若 $\bar\lambda=1/3$，则
$$
\bar T=-7/9,\quad\bar D=-4/81,\quad\bar K=-119/729.
$$
(5) 除以 $r^2$ 的非零余值等价于
$$
K^2+4D^3=\frac{13905}{531441}\ne0
\quad\text{于特征 }1009,
$$
其中 $13905\equiv788$，矛盾。

若 $\bar\lambda=0$，原 q2 在该根上的一次系数及常数项给
$$
\lambda/r\to-1,\qquad D/r\to-2/3,\qquad K/r\to-2.
$$
于是 (5) 左项估值为 $4a$，右项为 $5a$，矛盾。

## 5. delta 估值等于 2a：先排全部 mu 极点

取
$$
h=\delta/r^2\in\mathcal O^\times,\qquad H=\bar h\ne0.
$$
$m^2/r^2\to1$，$M/r^2\to H-1$，后者允许零值。

若 $\mu$ 有极点，则由 (16) 的二次头必须有 $H=-27$。在这个值上
$$
D/\mu^2\to7/18,\quad K/\mu^3\to2/27,\quad M/r^2\to-28.
$$
所以
$$
\frac{R_6}{r^2\mu^6}\longrightarrow
-28\frac4{729}-4\left(\frac7{18}\right)^3
=-\frac7{18}\ne0,
$$
矛盾。故以下 $\mu,\lambda,T$ 都整。

(16) 的完整剩余方程是
$$
(\mu+3)\{3\mu+7+H(\mu-3)/9\}=0.
\tag{17}
$$
本节及第6节把整几何量的剩余值仍记为 $\mu,\lambda,T$。先处理 $\mu\ne-3$。由 (17)，$\mu\ne3$ 且
$$
H=-\frac{9(3\mu+7)}{\mu-3},\qquad
H-1=-\frac{4(7\mu+15)}{\mu-3}.
\tag{18}
$$
原 D、K 的准确剩余表达式为
$$
D_0=\frac{(\mu+3)(7\mu+15)}{18},\qquad
K_0=\frac{(\mu+3)(4\mu^2+42\mu+63)}{54}.
\tag{19}
$$
原 (5) 除以 $r^2$ 给
$$
(H-1)K_0^2=4D_0^3.
\tag{20}
$$

### 5.1 M 首项为零的支仍完整保留

若 $7\mu+15=0$，则
$$
\mu=-15/7,\quad H=1,\quad D_0=0,\quad K_0=-47/343\ne0.
$$
在 (6) 中，分子的剩余值为 $12/49$，所以
$$
r^2S\to3/49,\qquad v(D)=v(M)-2a,\qquad v(M)>2a.
$$
(5) 左项估值为 $v(M)$，右项为 $3v(M)-4a>v(M)$，矛盾。因此 (18) 的整个 $H=1$ 支在这里被原式排除，没有先倒 $M/r^2$。

在余支，$H-1,D_0,K_0$ 都非零。

### 5.2 同一个原 K 的 N5 关系

令 $A=5\mu+12$，暂不要求它非零。由完整 (7)，
$$
rV_s,\ r\,bct_s\to A/6,\qquad
r^3y_s\to-\frac{A}{6(H-1)},
$$
$$
r^2z_2\to-\frac{2A}{3(H-1)},\qquad
r^3z_1\to-\frac{\mu A}{9(H-1)},\qquad
rZ_0\to-\frac{\mu^2A}{27}.
\tag{21}
$$
特别 $2mDZ_0=O(1)$。原 (8) 乘 r 后给
$$
A\{12D_0^2-\mu(H-1)K_0\}=0.
\tag{22}
$$
这保留 $A=0$ 的全部首项下降。

若 $A=0$，则
$$
\mu=-12/5,\quad H=-1/3,\quad
D_0=-3/50,\quad K_0=-41/250.
$$
但是
$$
(H-1)K_0^2-4D_0^3=-\frac{3281}{93750}\ne0,
\qquad 3281\equiv254\pmod{1009},
$$
与 (20) 矛盾。

所以可在余支取消 $A$。结合 (20)、(22) 中同一 $D_0,K_0$，有
$$
3K_0=\mu D_0,\qquad \mu^2(H-1)=36D_0.
\tag{23}
$$
这里 $D_0,K_0$ 已由前述分支证明非零，不是新假设。

将 (18)–(19) 代入，第一式给
$$
\mu^2-9\mu-21=0,
$$
第二式给 $\mu^2=3$。它们迫 $\mu=-2$，又给 $4=3$，矛盾。于是 (17) 中 $\mu\ne-3$ 的整个分支被排除。

## 6. delta 估值等于 2a、lambda 剩余为零

只余 $\mu=-3$，即 $\lambda\in\mathfrak m$。以下 h 仍是原整参数 $\delta/r^2$，其剩余值为 H。

为保留双根 $H=-3$，先写出原 q2 的完整一阶展开：
$$
\begin{aligned}
q_2/r^2={}&(12+4h/9+O(r))\lambda^2\\
&+(-4-4h/3+O(r))\lambda\\
&-(4+20h/3)r+O(r^2).
\end{aligned}
\tag{24}
$$
每个 $O(r)$ 系数都是 h、r 的整有理式，分母在本支为单位。这里不是仅在固定 H 的数值点作展开。

为直接核 (24) 的常数系数，可将原式准确分组为
$$
q_2=2m^2R+2\delta\ell U,
$$
$$
R=A_*A_2-\ell Q(3-4\lambda),\quad
U=\ell J A_2+\ell^2Q(3-4\lambda)-4uQT^2.
$$
在 $\lambda=0$，
$$
R/r\to-2,\qquad U/r\to-10/3.
$$
在 $r=0$ 的 lambda 多项式中，$R=6\lambda^2-2\lambda$、
$U=2\lambda^2/9-2\lambda/3$，正给 (24)。

### 6.1 H 不等于负三

此时 (24) 的一次头为单位，故
$$
\lambda/r\to-\frac{3+5H}{3+H}.
$$
结合 (10)，
$$
D/r\to\frac{2(H-1)}{H+3},\qquad
K/r\to\frac{2(H-3)}{H+3}.
\tag{25}
$$
若 $H\ne1,3$，(5) 左项估值 $4a$，右项至少 $5a$，立即矛盾。$3+5H=0$ 所致的 lambda 进一步下降也在此论证中，不曾剥除。

若 $H=1$，则 $v(M)>2a$，由 (25) 有 $\lambda/r\to-2,K/r\to-1$。在 (6) 分子 R 上，
$$
R/r\to2,\qquad rS\to1/2.
$$
所以 $v(D)=v(M)-a$。原 (5) 左项估值 $v(M)+2a$，右项为
$3v(M)-a$，后者严格较高，因为 $v(M)>2a$。矛盾。

若 $H=3$，则
$$
M/r^2\to2,\quad D/r\to2/3,\quad m/r\to-1.
$$
原 (5) 迫 $v(K)=3a/2$。从 (7) 的完整原量直接有
$$
rV_s,\ r\,bct_s\to-1/2,\quad
r^3y_s\to1/4,\quad
r^3z_1\to-1/2,\quad z_2=O(r^{-2}),\quad Z_0=O(r^{-1}).
$$
因此 (8) 第一项估值至少 a，第二项估值准确为
$$
2a+3a/2-3a=a/2.
$$
其首系数非零，所以第二项唯一最低，矛盾。

### 6.2 双根 H=−3

这里 $M/r^2\to-4$。从 (10)，
$$
D=-2\lambda/3-4r/3+O((\lambda,r)^2),\qquad
K=-\lambda-3r+O((\lambda,r)^2).
$$
若 $0<v(\lambda)<a$，则 (5) 两项估值为 $2a+2v(\lambda)$ 与 $2a+3v(\lambda)$，不相等。若 $v(\lambda)>a$（包括 $\lambda=0$），则两项估值为 $4a$ 与 $5a$，仍矛盾。

若 $v(\lambda)=a$，而 $\overline{\lambda/r}\ne-3$，左项仍为 $4a$，右项至少 $5a$。所以唯一可能为
$$
\lambda/r\to-3 .
$$
但在 (24) 中，$\lambda=O(r)$，$h+3\in\mathfrak m$；二次项除以 r 趋零，一次项除以 r 也趋零，而常数项给
$$
q_2/r^3\to16\ne0.
$$
矛盾。这完整排除了双根的所有相对相消，没有将 $h+3$ 当单位或预定其估值。

## 7. 完整覆盖与边界

$\bar Q\ne1$ 在第3节全部排除。$\bar Q=1$ 的 $\delta$ 估值分别小于、大于、等于 $2a$，覆盖全部可能；等于时先排所有 $\mu$ 极点，再分别处理 $\mu\ne-3$ 和 lambda 零剩余中心，保留并排除 $H=1,3,-3$ 的全部退化。故 (1) 不存在原解。

证明没有从模 D 幂零推 QQ，没有只选一个代数根，也没有反演未知的 $\delta$、M、lambda 或值头的首系数。使用完整原身份作赋值矛盾只排本射线；当前物理图以外的碰撞结构、其它尚未关闭的射线以及旧执行边界都保持原范围。
