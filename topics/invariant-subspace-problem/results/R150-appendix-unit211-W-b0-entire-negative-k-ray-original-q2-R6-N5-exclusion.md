# R150：W/b0 的整个负 k 射线由原 q2、R6 与完整 N5 排除

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**结论。** 当前 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 原图不存在满足
$$
v(e)=0,\qquad v(k)=-a<0
\tag{1}
$$
的 $1009$ 进原解。证明保留 $\lambda,T$ 的所有极点，以及 $u=e+1$、$u+2/k$ 的全部首项相消；只用同点原 $b_0,q_2,R_6,N_5$。没有新的数学运行，没有重放旧首项、投影、gcd 或矩阵门。此条只关闭 (1)，不把其它权射线、整个 W 或普通 ISP 宣布为空。

## 1. 原来源、逆 k 坐标与完整 N5

设 $F$ 是包含假想原解的 $1009$ 进代数扩张，允许进一步代数扩张；$\mathcal O$ 是赋值环、$\mathfrak m$ 是极大理想，剩余域特征为 $1009$。所有写出剩余值的商，均先由相应估值说明为整。

取
$$
j=k^{-1},\quad v(j)=a>0,\quad u=e+1,\quad Q=e/j,\quad \delta=1-Q,
$$
$$
N=1+(4-2e)j+4j^2,\qquad H=u+2j,\qquad
\ell=\frac{uN}{H},\quad m=u-\ell,\quad
M=\ell^2\delta-m^2,\quad bc=\frac{M}{4\delta}.
\tag{2}
$$
$u,\ell,H$ 在当前原图都非零，但它们未被预设为赋值环单位。记
$$
J=2u(1-u)+\ell Q,\quad A_*=4uQ-J,\quad
C_*=A_*m^2+J\delta\ell^2,
$$
$$
\mu=2\lambda-3,\qquad
A_2=\frac{\mu^2+4\mu+5}{2},\qquad
B_3=\frac{\mu^3+6\mu^2+12\mu+7}{2},
$$
$$
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell A_2T+2T^3.
\tag{3}
$$
原必要式为
$$
A_*T=uQ\ell\mu,
\tag{4}
$$
$$
q_2=2C_*A_2+2M\ell Q(3-4\lambda)
        -8uQ\delta\ell T^2=0,
\tag{5}
$$
$$
R_6=MK^2-4m^2D^3=0.
\tag{6}
$$
(5) 使用的整式重写是
$$
MA_*+C_*=4uQ\delta\ell^2.
$$
没有除 $A_*$ 的未知首值。

这些原式及以下完整 $N_5$ 的同点来源，是已刊源
[2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob 47281af16fdd0ad7500ecda377c3cb9f9d65e725，SHA256 e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8。这里只用其原定义和已付身份，不执行原源。

为使后面的 N5 首项可逐项追溯，完整列出原 $f$ 常数系数定义。它们不是额外施加的物理 $f=0$：
$$
T_0=2u-\ell Q-2u^2,\qquad
\Phi=T_0+4u-4+Q=-\frac{2e^2(1+4j)}{H},
$$
$$
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3,\quad
G=\lambda P_{02}-(1-u)T_0,
$$
$$
P_c=QP_{02}(\ell+T)-GT_0,
$$
$$
t_s=-\frac{P_c}{bc\,Q\Phi},\qquad
V_s=-\frac GQ-\frac{P_c}{Q\Phi},\qquad W_s=T_0/2,
$$
$$
x_s=\frac{(u-\ell Q)V_s-mW_s}{M},\qquad
y_s=\frac{\ell W_s-uV_s}{M},\qquad
w=\lambda-1-T,\quad c_\lambda=3-2\lambda=-\mu,
$$
$$
z_1=-2(\ell c_\lambda+2T)y_s-2\ell w+\frac{mTt_s}{\delta},
$$
$$
z_2=2(\ell x_s-my_s-bct_s)
    =-\frac{2G}{Q}-4my_s,
\tag{7}
$$
$$
Z_0=2(\ell c_\lambda+T)(\ell u w+V_sT)+2bc\,t_sT^2,
$$
$$
\boxed{\ N_5=2mD(Z_0+Dz_2)+MKz_1=0.\ }
\tag{8}
$$
这里 $V_s-bct_s=-G/Q$、$\ell x_s+my_s=V_s$ 是准确原身份。故还可无损改写
$$
Z_0=2(\ell c_\lambda+T)\ell u w
       +2V_sT(2T-\ell\mu)+2(G/Q)T^2.
\tag{9}
$$
(8) 的原来源保完整 NV 和原矩误差：
$$
N_5=2mD\ell^2NV+M z_{1,\rm full}H_{\rm val}
       -2mD z_{2,\rm full}q-\frac{2f}{MQ}C_4,
$$
$$
q=M\sigma^2-D,\qquad H_{\rm val}=K-2mD\sigma.
\tag{10}
$$
在当前原 $b_0,q_2$ 图上 $C_4=0$，所以 (8) 是原必要式；全过程没有倒 $D$。下面用 $Z_0,z_1,z_2$ 的首项时，始终是 (7)–(9) 的完整定义，不把某一 NV 分量当完整原值。

## 2. u 剩余非零时的共同尺度

先设
$$
E=\bar e\ne0,-1,\qquad U=\bar u=E+1\ne0.
\tag{11}
$$
则 $H$ 是赋值环单位，由 (2) 得
$$
\bar\ell=1,\quad \bar m=E,\quad
\overline{M/k}=-E,\quad \overline{bc}=1/4,\quad
\bar\Phi=-2E^2/U,
$$
$$
\overline{T_0/k}=-E,\quad
\overline{P_{02}/k}=2E^2,\quad
\overline{C_*/k^2}=-E^2,\quad
\overline{M\ell Q/k^2}=-E^2.
\tag{12}
$$
又
$$
\overline{A_*/(ek)}=4U-1,\qquad
\overline{8uQ\delta\ell/k^2}=-8UE^2.
\tag{13}
$$
允许 $4U-1=0$；不在本节反演它。

### 2.1 整 mu 必有整 T

若 $v(\mu)\ge0$（含 $\mu=0$）而 $v(T)<0$，(5) 的最后一项是唯一最低项，矛盾。因此 $\mu,T$ 均整。记其剩余值仍为 $\mu,T$，并在本小节把 $A_2,B_3,D,K$ 解释为 $\ell=1$ 的剩余表达式。

(4)–(5) 直接给
$$
(4U-1)T=U\mu,\qquad
\mu^2-8UT^2=1.
\tag{14}
$$
从而 $T\ne0$；否则第一式给 $\mu=0$，与第二式矛盾。原 (6) 中 $v(M)=-a$，而其它量整，故
$$
K=B_3-3A_2T+2T^3=0
\tag{15}
$$
在剩余域成立。

令
$$
S=\mu+4+2T.
$$
将 (7) 的完整原定义按 (12) 取首项，有
$$
\overline{t_s/k}=2US,\quad
\overline{V_s/k}=US/2,\quad
\bar y_s=\frac12+\frac{U^2S}{2E}.
\tag{16}
$$
特别 $z_1,z_2$ 都整，由 (9)
$$
\overline{Z_0/k}=UST(2T-\mu).
$$
因此 (8) 除 $k$ 后，第二项的剩余值因 (15) 为零，得到
$$
2EU\,D\,S\,T(2T-\mu)=0.
\tag{17}
$$
$E,U,T$ 均非零。若 $2T=\mu$，(14) 先给 $U=1/2$，再给 $0=1$。所以 (17) 只可能有 $S=0$ 或 $D=0$。下面在剩余域完整排除这两种可能；没有剥任何新权因子。

### 2.2 S=0 的两小三次不相容

由 $S=0$ 得 $T=-(\mu+4)/2$。从 (14)，$4T-\mu=T/U\ne0$，于是
$$
(\mu^2-1)(4T-\mu)-8T^3=0.
$$
与 (15) 分别给
$$
A=-2\mu^3+4\mu^2+51\mu+72=0,
$$
$$
B=4\mu^3+24\mu^2+39\mu+10=0.
\tag{18}
$$
但
$$
B+2A=(\mu+2)(32\mu+77).
$$
两根上的准确值为
$$
A(-2)=2,\qquad A(-77/32)=5013/16384.
$$
它们在特征 $1009$ 都非零。因此不存在同根，整个 $S=0$ 剩余支被排除。

### 2.3 D=0 的完整降阶矛盾

令 $n=\mu+2=2\lambda-1$。由 $D=K=0$ 和 $T\ne0$，
$$
T^2=(n^2+1)/2,\qquad T^3=(n^3-1)/2.
$$
所以
$$
(n+1)^2Q_4(n)=0,\qquad Q_4=n^4-2n^3-2n+1.
\tag{19}
$$
若 $n=-1$，则 $T=-1$，(14) 给 $U=1$、$E=0$，与 $v(e)=0$ 矛盾。这一步保留了 $\bar\lambda=0$，未预先把它剥去。

在余支 $n+1\ne0$，(14) 给
$$
8T(1-2n)=(n-2)(n-1)(n-3).
$$
代入 $T=(n^3-1)/(n^2+1)$，其中分母 $2T^2\ne0$，并除非零 $n+1$，得到
$$
R_4=n^4+9n^3-5n^2-7n+2=0.
$$
于是
$$
C_3=R_4-Q_4=11n^3-5n^2-5n+1=0.
$$
由 $11(11Q_4-nC_3)+17C_3=-2C_2$，
$$
C_2=15n^2+169n-69=0.
\tag{20}
$$
将 $225C_3$ 除以 $C_2$ 的完整余式为
$$
337106n-133221.
$$
模 $1009$ 它等于 $100n-33$。在 $n=33/100$ 上，
$$
10000C_2(33/100)=-115965\equiv70\pmod{1009},
$$
矛盾。故 (19) 的全部剩余根都不可能。结合 2.2，所有整 $\mu,T$ 情形已排除。

## 3. u 剩余非零、mu 有极点时只有一个中心

设 $s=v(\mu)<0$。由 (5) 的三个实际系数估值，必有
$$
v(T)=s.
$$
否则 $\mu^2$ 项或 $T^2$ 项成为唯一最低项。由 (4) 可知 $A_*/(ek)$ 是赋值环单位，所以 $4U-1\ne0$，且
$$
\kappa=T/\mu=\frac{u\ell}{4u-\ell+2uj},
\qquad \bar\kappa=\frac{U}{4U-1}.
\tag{21}
$$
(5) 的最高项给
$$
8U\bar\kappa^2=1.
$$
而
$$
K/\mu^3\longrightarrow
\frac{4\bar\kappa^3-3\bar\kappa+1}{2}
=\frac{(\bar\kappa+1)(2\bar\kappa-1)^2}{2}.
$$
若此值非零，(6) 第一项比第二项低至少 $a$，矛盾。因此 $\bar\kappa=-1$ 或 $1/2$。前者由 (21) 给 $U=1/5$，与 $8U\bar\kappa^2=1$ 不合。唯一可能为
$$
U=1/2,\quad E=-1/2,\quad
\bar\ell=1,\quad \bar m=-1/2,\quad
\bar\kappa=1/2,\quad \overline{M/k}=1/2.
\tag{22}
$$

### 3.1 q2 对 u 偏移的完整控制

令 $x=\mu^{-1}\in\mathfrak m$。在 (22) 附近，(5) 除以 $-e^2k^2\mu^2$ 后是分母为赋值环单位的有理式。在 $j=0$ 上准确等于
$$
c(u)-x^2,\qquad
c(u)=1-\frac{8u^3}{(4u-1)^2}
=-\frac{(2u-1)(4u^2-6u+1)}{(4u-1)^2}.
\tag{23}
$$
其余项是 $j$ 乘一个整元素。$c'(1/2)=2$ 为单位，因此
$$
u-\tfrac12=O(j,x^2).
\tag{24}
$$
这里 $O(j,x^2)$ 仅指属于赋值环理想 $(j,x^2)$；不调用解析收敛或选取平方根。

若 $s\le-a/2$，则 (24) 给 $u-1/2=O(j)$，从而 $\ell-1,\kappa-1/2=O(j)$。完整展开
$$
\begin{aligned}
K={}&\tfrac12(\ell^2-3\ell\kappa+4\kappa^3)\mu^3\\
&+3\ell(\ell-2\kappa)\mu^2
+\tfrac32\ell(4\ell-5\kappa)\mu+\tfrac72\ell^2
\end{aligned}
\tag{25}
$$
得到 $v(K)\ge a+3s$。又 $D/\mu^2\to1/4$，所以 (6) 两项估值分别至少 $a+6s$ 和准确 $6s$，不可能相等。

只余 $-a/2<s<0$。此时 (23)–(24) 给更精确的剩余比率
$$
\frac{u-1/2}{x^2}\to\frac12,\qquad
\frac{\kappa-1/2}{x^2}\to-\frac12,\qquad
\frac{2\kappa-\ell}{x^2}\to-1.
\tag{26}
$$
(25) 的三次系数属于 $(j,x^4)$，二次项整，而一次项给
$$
K/\mu\to9/4,\qquad D/\mu^2\to1/4.
$$
(6) 因而准确迫
$$
s=-a/4,\qquad \mu^4/k\to162.
\tag{27}
$$

### 3.2 完整 N5 在唯一 pole 中心的余值为负一

在 (27) 下，按 (7) 逐项有
$$
\frac{G}{Q\mu}\to-\frac12,\quad
\frac{t_s}{k\mu}\to2,\quad
\frac{V_s}{k\mu}\to\frac12,\quad
\frac{y_s}{\mu}\to-\frac12,\quad w\to\frac12.
\tag{28}
$$
例如 $P_{02}/k\to1/2$、$T_0/k\to1/2$、$\Phi\to-1$，
故 $P_c/(k^2\mu)\to-1/4$，直接给前四式。

由 (26)，$(2T-\ell\mu)\mu\to-1$。在 (9) 中，第一项除以 $k\mu$ 趋零，第三项也趋零，因为 $\mu^2/k\in\mathfrak m$。第二项给
$$
Z_0/(k\mu)\to-1/2.
$$
在 $z_1$ 的完整定义中，前两项除以 $\mu^2$ 趋零，第三项给
$$
z_1/\mu^2\to-1.
$$
此外 $z_2=O(\mu)$。所以 $2mD^2z_2/(k\mu^3)\to0$，而完整 (8) 给
$$
\frac{N_5}{k\mu^3}\longrightarrow
(-1)\frac14\left(-\frac12\right)
+\frac12\frac94(-1)
=-1.
\tag{29}
$$
这是特征 $1009$ 的非零元，与原 $N_5=0$ 矛盾。因此 $U\ne0$ 的全部极点情形也被排除。

## 4. u 剩余为零的统一 q2：保 u+2j 的全部相消

现在设 $\bar e=-1$、$b=v(u)>0$。令
$$
\beta=\frac u\ell=\frac{u+2j}{N},\qquad c=v(\beta)>0.
\tag{30}
$$
这保留 $u+2j$ 的任意高阶相消；$\ell$ 可以为单位、趋零或有极点。记
$$
d=4\beta-1+2\beta j,\qquad
B=\delta-(\beta-1)^2.
$$
由原定义精确有
$$
A_*=\ell Qd,\qquad
T=\frac u d\mu,\qquad
m=\ell(\beta-1),\qquad
M=\ell^2B,\qquad B/k\to1,\quad d\to-1.
\tag{31}
$$
这里只反演已证明的单位 $d$，没有假设 $H/j$ 的首值非零。

再令
$$
\varepsilon=\frac{C_*}{M\ell Q}-1
=\frac{2\beta\{(2+j)\beta(\beta-2)+u+1\}}B,
$$
$$
F=\frac{4u\beta^2\delta}{Bd^2}.
\tag{32}
$$
则
$$
v(\varepsilon)=c+a>0,\qquad v(F)=b+2c>0,
$$
而完整原 (5) 正好等价于
$$
(1+\varepsilon-2F)\mu^2+4\varepsilon\mu-1+5\varepsilon=0.
\tag{33}
$$
其二次及常数系数都是单位，中间系数在 $\mathfrak m$。所以 $\mu$ 必为单位且
$$
\bar\mu=-1\quad\text{或}\quad\bar\mu=1.
\tag{34}
$$
特别所有 $\mu$ 极点、正估值及零值在这里都已由原式排除。

### 4.1 mu 剩余负一：仅一个缩放中心

若 $\bar\mu=-1$，(33) 还给
$$
v(\mu+1)\ge\min(c+a,b+2c)>c.
$$
因此 $A_2\to1$、$v(B_3)>c$，由 (3)、(31)
$$
D/\ell\to1,\qquad T/u\to1,\qquad
K/(\ell u)\to-3,\qquad m/\ell\to-1.
\tag{35}
$$
(6) 除以 $\ell^5$，两项相等只可能在
$$
b+c=a,\qquad ku\beta\to4/9.
\tag{36}
$$
若 $b<a$，则 $c=b$；若 $b>a$，则 $c=a$；若 $b=a$，则 $c\ge a$，包括全部相消。故 (36) 唯一允许
$$
b=c=a/2,\qquad \ell\to1,\qquad ku^2\to4/9.
\tag{37}
$$

在 (37) 的完整原 $f$ 常数项中，
$$
T_0/k\to1,\quad P_{02}/k\to2,\quad G/k\to1,\quad
u\Phi\to-2,\quad P_c/k^2\to-3,
$$
$$
t_s/(uk)\to6,\quad V_s/(uk)\to3/2,\quad
y_s\to1/2,\quad z_1\to-1,\quad z_2\to4.
\tag{38}
$$
由 (7)，$Z_0\to4/3$，故 $Z_0$ 整；$D\to1,m\to-1$。于是 (8) 第一项整，第二项 $MKz_1$ 的估值准确为
$$
-a+b=-a/2<0.
$$
这是唯一最低项，矛盾。

### 4.2 mu 剩余正一：两个线性余式不相容

若 $\bar\mu=1$，则 $\bar\lambda=2$、$A_2\to5$、$B_3\to13$。由 (31)
$$
D/\ell\to5,\qquad K/\ell^2\to13,\qquad m/\ell\to-1.
\tag{39}
$$
(6) 除以 $\ell^5$ 必迫
$$
v(k\ell)=0,\qquad k\ell\to500/169.
$$
用 (30) 的三种估值情形可知，这唯一可能在
$$
b=2a,\quad c=a,\quad R=\overline{k^2u}=1000/169\ne0.
\tag{40}
$$
特别 $u+2j$ 在这里没有首项相消。

以 $j$ 表示完整原量的首项：
$$
\ell/j\to R/2,\quad m/j\to-R/2,\quad
M/j\to R^2/4,\quad bc/j^2\to R^2/16,\quad T/j^2\to-R,
$$
$$
D/j\to5R/2,\qquad K/j^2\to13R^2/4.
\tag{41}
$$
逐项代 (7)，得到
$$
T_0\to R/2,\quad P_{02}\to R,\quad G\to3R/2,\quad
j\Phi\to-1,\quad P_c\to-5R^2/4,
$$
$$
t_s\to20,\quad V_s/j\to3R/2,\quad
x_s\to7/2,\quad y_s\to1/2,
$$
$$
z_1/j\to-R/2,\quad z_2/j\to4R,\quad Z_0=O(j^4).
\tag{42}
$$
因此完整 (8) 的 $j^4$ 首项为
$$
N_5/j^4\longrightarrow
-25R^4-\frac{13R^5}{32}
=-\frac{R^4}{32}(800+13R).
\tag{43}
$$
原式迫 $13R+800=0$。另一方面 (40) 给 $169R-1000=0$。这两式的准确组合
$$
13(13R+800)-(169R-1000)=11400
\equiv301\pmod{1009}
$$
非零，矛盾。于是 $\bar u=0$ 的整个分支也被排除。

## 5. 覆盖完整性与结论边界

$u$ 的剩余非零或为零覆盖全部可能。在前者，整 $\mu$ 自动给整 $T$，由 (14)–(20) 排除；有极点的 $\mu$ 只能落 (22)，再由 (24)–(29) 排除。在后者，(30)–(33) 同时包含 $u+2j$ 的全部相消，$\mu$ 的全部估值只余两个简单剩余值，各由 (35)–(43) 排除。因此 (1) 没有原解。

本条没有把 $D$、$u$、$H$、$4u-1$、$2u-1$ 的未知剩余值先行支付为单位。出现的单位都是当前原图已经支付的非零量，或在相应分支中由准确首项证明的赋值环单位。$N_5$ 的使用保留完整 (7)–(10)，不把原 $f$ 常数系数当作物理 $f=0$，不从独立范数的零集推同根充分性。

这是独立的原估值纸证，未新增执行回执；先前任何首项运行的成功、未返、资源边界及保留纤维均不改写。其余权射线和所有未完成的原图仍按各自已刊范围保留。
