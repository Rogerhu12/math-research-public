# R150：W/b0 的负 e、正 k 对角射线完整原排除

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**结论。** 当前 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 原图不存在满足
$$
v(e)=-a<0,\qquad v(k)=a,\qquad v(Q)=v(ek)=0
\tag{1}
$$
的 $1009$ 进原解。证明使用原 $b_0,q_2,R_6$ 与完整 NV 的纯 $N_5$ 必要式，保留 $\bar Q=\pm2$ 的全部分母或首项退化、$M$ 的任意高阶下降以及 $\lambda$ 的全部极点。没有新的运行，没有再算旧初始理想、投影或矩阵。

本条只关闭 (1)，不声明其它权射线或整个 W 已排空。

## 1. 原式与同点 N5

沿当前原图记
$$
u=e+1,\quad Q=ek,\quad \delta=1-Q,\quad
\ell=\frac{u((k+2)^2-2ek)}{k(uk+2)},\quad m=u-\ell,
$$
$$
M=\ell^2\delta-m^2,\quad bc=\frac M{4\delta},\quad
J=2u(1-u)+\ell Q,\quad A_*=4uQ-J,\quad
C_*=A_*m^2+J\delta\ell^2 .
$$
取
$$
\mu=2\lambda-3,\quad
A_2=\frac{\mu^2+4\mu+5}{2},\quad
B_3=\frac{\mu^3+6\mu^2+12\mu+7}{2},
$$
$$
D=\ell A_2-T^2,\qquad K=\ell^2B_3-3\ell A_2T+2T^3.
$$
原必要关系完整为
$$
A_*T=uQ\ell\mu,
\tag{2}
$$
$$
q_2=2C_*A_2+2M\ell Q(3-4\lambda)
       -8uQ\delta\ell T^2=0,
\tag{3}
$$
$$
R_6=MK^2-4m^2D^3=0.
\tag{4}
$$
由 $MA_*+C_*=4uQ\delta\ell^2$，(3) 还有准确形式
$$
q_2=8uQ\delta\ell D
      +2M\{\ell Q(3-4\lambda)-A_*A_2\}.
$$
因此在原图上
$$
D=M S,\qquad
S=\frac{A_*A_2-\ell Q(3-4\lambda)}
        {4uQ\delta\ell}.
\tag{5}
$$
(5) 的分母只含旧已付权；不倒 $D,S$ 或其首值。

全部来源为已刊
[2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob 47281af16fdd0ad7500ecda377c3cb9f9d65e725，SHA256 e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8。本条只用原定义，不执行该源任何旧目标。

为保全原 N5，记
$$
T_0=2u-\ell Q-2u^2,\quad \Phi=T_0+4u-4+Q,
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
x_s=\frac{(u-\ell Q)V_s-mW_s}{M},\quad
y_s=\frac{\ell W_s-uV_s}{M},\quad
w=\lambda-1-T,\quad c_\lambda=3-2\lambda=-\mu,
$$
$$
z_1=-2(\ell c_\lambda+2T)y_s-2\ell w+\frac{mTt_s}{\delta},
$$
$$
z_2=2(\ell x_s-my_s-bct_s)=-2G/Q-4my_s,
$$
$$
Z_0=2(\ell c_\lambda+T)(\ell u w+V_sT)+2bc\,t_sT^2 .
\tag{6}
$$
于是完整必要式为
$$
\boxed{\ N_5=2mD(Z_0+Dz_2)+MKz_1=0.\ }
\tag{7}
$$
这沿原 $f$ 常数系数身份，不是施加物理 $f=0$。其完整来源为
$$
N_5=2mD\ell^2NV+M z_{1,\rm full}H_{\rm val}
       -2mD z_{2,\rm full}q-\frac{2f}{MQ}C_4,
$$
$$
q=M\sigma^2-D,\quad H_{\rm val}=K-2mD\sigma,
$$
而 $C_4=0$ 在当前原 $b_0,q_2$ 图已付。没有把 NV 某分量或独立范数零集替代同点完整值。

令
$$
r=e^{-1},\quad v(r)=a,\quad k=Qr,\quad
V=Q+2+Qr,\quad
\mathcal A=4-2Q+4Qr+Q^2r^2.
$$
权恢复的准确形式是
$$
\ell=\frac{(1+r)\mathcal A}{Qr^2V},\qquad u/e\to1.
\tag{8}
$$
下面在包含原解的赋值环及其特征 $1009$ 剩余域中推导；所有剩余商都先由相应尺度证明整。记 $q=\bar Q\ne0$。

## 2. 一般 Q 剩余：只有两个原三矩根，随后皆被排除

先设 $q\ne2,-2$。由 (8)，
$$
\ell/e^2\to L=\frac{2(2-q)}{q(q+2)},\quad
m/e^2\to-L,\quad M/e^4\to-qL^2,
$$
$$
J/e^2\to-\frac{4q}{q+2},\quad
A_*/e^2\to\frac{4q}{q+2}.
\tag{9}
$$
特别两个最后的系数非零，(2) 给
$$
\frac{T}{e\mu}\to c=\frac{2-q}{2q}
\tag{10}
$$
（当 $\mu=0$ 时保留对应不除 $\mu$ 的原关系）。
又
$$
C_*/e^6\to\frac{16(2-q)^2}{(q+2)^3},\quad
M\ell Q/e^6\to-\frac{8(2-q)^3}{q(q+2)^3}.
\tag{11}
$$
(3) 的 $T^2$ 系数乘 (10) 后比 $C_*\mu^2$ 高至少 $a$。所以若 $\mu$ 有极点，$C_*\mu^2$ 是唯一最低项。故 $\mu,\lambda$ 整，$v(T)\ge-a$。

如果 $B_3$ 的剩余值非零，(4) 第一项估值为 $-12a$，第二项至少 $-10a$，矛盾。因此
$$
\bar B_3=0.
$$
将 (3) 除以 $e^6$，得到
$$
2qA_2+(q-2)(3-4\lambda)=0
\tag{12}
$$
的剩余身份。以下同节的 $\lambda,\mu,A_2$ 都指剩余值。

令 $n=2\lambda-1=\mu+2$。因为 $B_3=(n^3-1)/2$，
$$
n^3=1,\qquad q(n^2-2n+2)+4n-2=0.
$$
$n=1$ 会迫 $q=-2$，已在本节排除。所以
$$
n^2+n+1=0,\qquad
q=\frac{2(1-2n)}{1-3n}=\frac{2(10+n)}{13}.
\tag{13}
$$
这些根没有使 $q=0,1,2,-2$，也没有使 $\mu=n-2=0$。因此 $\delta$ 在此时才确认为赋值环单位。

记
$$
\tau=\overline{T/e}=c\mu,\qquad d=\overline{D/e^2}=LA_2-\tau^2.
$$
利用 (12)–(13)，
$$
\frac dL=\frac{(2-q)(55n-48)}{52q}.
\tag{14}
$$
$55n-48$ 在 $n^2+n+1=0$ 的两根上均非零：其准确范数为
$$
48^2+48\cdot55+55^2=7969\equiv906\pmod{1009}.
$$
所以 $d\ne0$，(4) 进一步强制 $v(K)=-3a$。令 $h=\overline{K/e^3}$，则
$$
qh^2+4d^3=0.
\tag{15}
$$

### 2.1 完整 N5 与同 K 首值

由 (6)、(9)，
$$
T_0/e^2,\ \Phi/e^2\ \to h_0=-2-qL=-8/(q+2),
$$
$$
P_{02}/e^3\to P=2+3qL,\qquad
G/e^3\to g=\lambda P+h_0,
$$
$$
P_c/e^5\to qPL-gh_0,\qquad
V_s/e^3\to v_0=-PL/h_0=\frac{4-q}{2}L.
\tag{16}
$$
原 $y_s$ 整，$z_2=O(e^3)$；由于 $w/e\to-\tau$，完整 $z_1$ 的唯一 $e^3$ 项是 $-2\ell w$：
$$
z_1/e^3\to2L\tau.
$$
完整 $Z_0$ 的 $e^6$ 项为
$$
Z_0/e^6\to2L\mu\tau(L-v_0),\qquad
L-v_0=-qLc.
\tag{17}
$$
因此 (7) 除以 $e^{10}$ 给
$$
2d\mu(L-v_0)+qLh=0,
$$
即
$$
h=2d\tau.
\tag{18}
$$
结合同一个 $h$ 的 (15)，因 $d\ne0$，
$$
d+q\tau^2=0,\qquad LA_2=(1-q)\tau^2.
\tag{19}
$$
这里不是把两个独立范数的根拼接，而是同一原 K 的两条实际首项身份。

把 (13) 代入 (19)，等价的准确一次条件是
$$
1070-1063n=0.
$$
模 $1009$ 它为 $61-54n=0$。但
$$
54^2\{(61/54)^2+61/54+1\}=9931\equiv850\pmod{1009}.
$$
矛盾。整个 $q\ne\pm2$ 分支已被排除。

## 3. Q 剩余负二：保 V 的全部高阶相消

设 $q=-2$。令
$$
d=v(V)>0.
$$
在 (8) 中 $\mathcal A\to8$ 是单位，故
$$
v(\ell)=-2a-d,\qquad
\beta=u/\ell,\quad v(\beta)=a+d.
$$
定义
$$
g=4\beta-1+\frac{2\beta e}{Q},\qquad
B=\delta-(\beta-1)^2.
$$
由原式严格有
$$
A_*=\ell Qg,\quad
T=(u/g)\mu,\quad m=\ell(\beta-1),\quad M=\ell^2B,
$$
$$
\bar g=-1,\qquad\bar B=2.
\tag{20}
$$
从而 $g$ 是在本支证明的赋值环单位，无需假设 $V/r$ 的首值非零。

令
$$
\varepsilon=\frac{C_*}{M\ell Q}-1
=\frac{4\beta(\beta-1)^2}{B}-\frac{2\beta e}{Q},\qquad
F=\frac{4u\beta^2\delta}{Bg^2}.
$$
有准确估值
$$
v(\varepsilon)=d,\qquad v(F)=a+2d,
$$
且原 (3) 正好化为
$$
\mu^2-1+\varepsilon(\mu^2+4\mu+5)-2F\mu^2=0.
\tag{21}
$$
因此 $\mu$ 是单位，剩余值只能是 $\pm1$。

若 $\bar\mu=1$，则 $A_2\to5,B_3\to13$。由 (20)，
$D/\ell\to5,K/\ell^2\to13$。原 (4) 的两项分别具有 $\ell^6$ 与 $\ell^5$ 的非零首项，因 $\ell$ 有极点，第一项唯一最低，矛盾。

若 $\bar\mu=-1$，则 (21) 给
$$
\mu+1\sim\varepsilon\sim-2\beta e/Q.
$$
因此
$$
T/u\to1,\quad D/\ell\to1,\quad
K/(\ell ue)\to-3/q=3/2.
\tag{22}
$$
这里 $K$ 的主项是 $\ell^2B_3$；另外两项至少高 $a$。原 (4) 只可能在
$$
d=2a,\qquad \ell/e^4\to9/8
\tag{23}
$$
成立。

### 3.1 N5 在唯一剩余中心有唯一最低项

在 (23)，由完整 (6)，
$$
T_0/\ell,\ \Phi/\ell\to2,\qquad
P_{02}/(e\ell)\to-6,\qquad G/(e\ell)\to-4,
$$
$$
P_c/(e\ell^2)\to20,\quad
t_s\ell/e\to30,\quad
V_s/(e\ell)\to3,\quad y_s\to1/2,
$$
$$
z_1/(\ell e)\to2,\qquad z_2/(\ell e)\to-4,\qquad
Z_0/(\ell^2e^2)\to4.
\tag{24}
$$
因此 (7) 第一项的估值为 $-18a$，而第二项为 $-19a$，其准确主项是
$$
MKz_1\sim6\ell^4e^3.
$$
特征 $1009$ 下系数非零，故这是唯一最低项，矛盾。整个 $q=-2$ 中心，包括 $V$ 的全部任意高阶相消，都被排除。

## 4. Q 剩余正二：先保 ell/u 的全部估值

现在设 $q=2$。由 (8)，$V\to4$ 是单位，$\mathcal A$ 有正估值。令
$$
L=\ell/u,\qquad l=v(L)>-a,\qquad
B=M/u^2=-QL^2+2L-1.
\tag{25}
$$
注意此节 L 是原量，不是第2节的剩余常数。由原 (2)，
$$
A_*=u\{2e+Q(4-L)\},\qquad A_*/u^2\to2,
$$
$$
T=\kappa\mu,\qquad
\kappa=\frac{uQL}{2e+Q(4-L)},\qquad \kappa/L\to1.
\tag{26}
$$
这同时保留 $L$ 的零、单位和极点。利用原
$$
C_*=4uQ\delta\ell^2-A_*M
\tag{27}
$$
可直接比较 (3) 的全部二次头。

### 4.1 L 不是单位，或 B 剩余非零

若 $l<0$，则 $B/L^2\to-2$、$m/\ell\to-1$，并且
$$
v(C_*)=-4a+2l,\quad
v(M\ell Q)=-3a+3l,\quad
v(8uQ\delta\ell\kappa^2)=-2a+3l.
$$
因 $l>-a$，(3) 先排除 $\mu$ 极点，再迫 $\bar A_2=0$。其后
$$
v(A_2)\ge a+l,\quad v(D)\ge2l,\quad v(K)=-2a+2l.
$$
这里 $A_2=0$ 的两个剩余根均有 $B_3\ne0$ 和 $3-4\lambda\ne0$。原 (4) 左项估值 $-6a+6l$，右项至少 $-2a+8l$；后者严格高，矛盾。

若 $l>0$，则 $B\to-1,m/u\to1$。同样由 (3) 得 $\mu$ 整、$\bar A_2=0$，
$$
v(A_2)\ge a+l,\quad v(D)\ge2l,\quad v(K)=-2a+2l.
$$
原 (4) 左项估值 $-6a+4l$，右项至少 $-2a+6l$，仍矛盾。

若 $l=0$ 但 $\bar B\ne0$，相同论证给 $\bar A_2=0$、$v(D)\ge0$、$v(K)=-2a$。左项估值 $-6a$，右项至少 $-2a$，矛盾；允许 $m/u$ 的首值为零只会提高右项。

故唯一可能为
$$
l=0,\qquad 2\bar L^2-2\bar L+1=0.
\tag{28}
$$
特别 $\bar L,1-\bar L,\bar L-1/2$ 均非零。

### 4.2 M 的所有下降阶及 C* 的全部相消

设
$$
w_B=v(B)>0.
$$
在 (28)，$v(M)=-2a+w_B$、$v(m)=-a$，且
$$
v(4uQ\delta\ell^2)=-3a,\qquad v(A_*M)=-4a+w_B.
$$

若 $w_B<a$，则 $v(C_*)=-4a+w_B$。由 (3)，$\mu$ 整、$\bar A_2=0$、$v(A_2)\ge a$，故 $v(D)\ge0$、$v(K)=-2a$。原 (4) 左项为 $-6a+w_B$，右项至少 $-2a$，矛盾。

若 $w_B>a$，则 $v(C_*)=-3a$。原 (3) 的实际 $T^2$ 项给 $\mu$ 整、$\bar A_2=0$、$v(A_2)=a$。在准确身份 (5) 中，分子两项估值都至少 $-a$，分母估值 $-2a$，因此
$$
v(S)\ge a,\qquad v(D)\ge w_B-a .
$$
而 $v(K)=-2a$。于是原 (4) 左项为 $-6a+w_B$，右项至少 $3w_B-5a$，又是左项唯一最低。

只余 $w_B=a$，此时 $v(C_*)\ge-3a$。若 $v(C_*)<-2a$，原 (3) 仍排除 $\mu$ 极点并迫 $\bar A_2=0$。因 $v(A_2)>0$，有 $v(D)>-a$、$v(K)=-2a$。原 (4) 左项为 $-5a$、右项严格高于 $-5a$，矛盾。

因此所有剩余可能必须满足
$$
w_B=a,\qquad v(C_*)\ge-2a .
$$
这没有把 $C_*$ 的新首项当单位。相反，(27) 的完整相消给出确定的原权比率
$$
\boxed{\ M/u\to-4L_0^2,\qquad L_0=\bar L,\quad
2L_0^2-2L_0+1=0.\ }
\tag{29}
$$

## 5. 深中心：R6 排全部 mu 极点

若 $s=v(\mu)<0$，由 (26)、(29)，
$$
\frac D{u\mu^2}\to\frac{L_0}{2},\qquad
\frac K{u^2\mu^3}\to\frac{L_0^2}{2}.
$$
因此
$$
\frac{R_6}{u^5\mu^6}\longrightarrow
-L_0^6-\frac{(1-L_0)^2L_0^3}{2}
=L_0^5(1/2-L_0).
\tag{30}
$$
由 (28) 右端非零，矛盾。故此深中心的 $\mu,\lambda,T$ 全部整。

## 6. 深中心的完整 N5 与 R6 两原余式

本节把剩余的 $L_0,\mu,\lambda,A_2,B_3$ 简记为 $L,\mu,\lambda,A_2,B_3$。由 (29)、(26)，
$$
D/u\to LA_2,\qquad K/u^2\to L^2B_3,\qquad
m/u\to1-L .
$$
原 (4) 除以 $u^5$，因 $(1-L)^2=-L^2$，得到
$$
\boxed{\ A_2^3=L B_3^2.\ }
\tag{31}
$$
$A_2,B_3$ 没有共同根：若 $n=2\lambda-1$ 同时满足 $n^2=-1,n^3=1$，则 $n=-1$ 又给 $1=-1$。所以在 (31) 中二者均非零。

现在逐项使用完整 (6)。有
$$
T_0/u^2,\ \Phi/u^2\to-2,\quad P_{02}/u^3\to2,\quad
G/u^3\to\mu+1,\quad bc/u\to L^2,
$$
$$
bct_s/u^3\to(\mu+1)/2,\quad
V_s/u^2\to\mu+1+L,\quad
y_s/u^2\to\frac{\mu+1+2L}{4L^2}.
\tag{32}
$$
$V_s$ 的 $u^3$ 项在这里准确相消，因为
$$
V_s=-\frac{G(\Phi-T_0)+QP_{02}(\ell+T)}{Q\Phi}.
$$
它不是省略某个原项。

由 $L^2=L-1/2$、$L(1-L)=1/2$，
$$
z_2/u^3\to-\frac{\mu+3}{2L^2},\qquad
z_1/u^3\to\frac{\mu(\mu+3)}2,\qquad Z_0=O(u^3).
\tag{33}
$$
这些式子保留 $\mu=0,-1,-3$ 的所有首项下降；并未预先除这些因子。

于是完整原 (7) 除以 $u^6$，其 $2mDZ_0$ 项趋零，余下准确为
$$
\boxed{\ 
(\mu+3)\left\{(1-L)A_2^2-\frac{\mu B_3}{2}\right\}=0.
\ }
\tag{34}
$$
若 $\mu=-3$，即 $\bar\lambda=0$，则 $A_2=1,B_3=-1$，(31) 迫 $L=1$，与 (28) 矛盾。这覆盖原 lambda 的正估值中心。

在余支 $\mu+3\ne0$，由 (31)、(34) 相乘消去同一个 $B_3$，
$$
\mu^2=2(1-L)A_2.
\tag{35}
$$
这里用 $(1-L)^2=-L^2$ 和 $L^3=(L-1)/2$；未另选某个范数根。(35) 排 $\mu=0$，再代 (34) 得
$$
\mu A_2=B_3,\qquad 2\mu^2+7\mu+7=0.
\tag{36}
$$
又
$$
L=\frac{4\mu+5}{\mu^2+4\mu+5}
  =\frac{2(4\mu+5)}{\mu+3}.
$$
代入 (28)，得到
$$
113\mu^2+258\mu+149=0.
$$
它与 (36) 的准确线性组合给 $275\mu+493=0$。但
$$
275^2\{2(-493/275)^2+7(-493/275)+7\}
=66448\equiv863\pmod{1009},
$$
矛盾。这排除 (29) 的全部整 $\mu$ 情形。

## 7. 完整覆盖与范围

$q=\bar Q$ 非零，由第2节，除 $q=\pm2$ 外全被排除。第3节保留并排除了 $q=-2$ 时 $V=Q+2+Qr$ 的任意下降阶。第4–6节覆盖了 $q=2$ 时 $L=\ell/u$ 的全部估值、$M/u^2$ 的全部下降阶、$C_*$ 的全部相消和 $\mu$ 的整值、零值及极点。因此 (1) 不存在原解。

整个证明只在明确分支里使用已证明非零的剩余量；没有将未知权首项、$M$ 首值、$C_*$ 首值、$D$ 首值或原 NV 的某个线性头提前设为单位。完整 N5 的每次首项来自 (6)–(7)，其与原矩/NV 的必要性由同点身份保留。没有改变旧计算成功、失败或冻结的范围，也没有新的系数缓存或执行回执。
