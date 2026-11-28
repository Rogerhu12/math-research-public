# R150：W/b0 正 k 射线的 e 剩余值负一中心完整原排除

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**结论。** 当前 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 原图不存在满足
$$
v(k)=a>0,\qquad v(e)=0,\qquad \bar e=-1
\tag{1}
$$
的 $1009$ 进原解。证明完整覆盖 $u=e+1$ 相对 $k$ 的全部正估值，以及 $\mu=2\lambda-3$ 的整值、零值和极点。没有新的数学运行，也没有重做原投影、初始理想或矩阵门。

[正 k 射线一般中心](R150-appendix-unit211-W-b0-positive-k-ray-only-e-plus-minus-one-original-centers.md)已将该射线限制到 $\bar e=\pm1$；本文只负责负一中心，正一中心由[原D/M身份纸证](R150-appendix-unit211-W-b0-positive-k-e-one-center-original-D-over-M-exclusion.md)处理。其它权射线不在本条范围内。

## 1. 同点原式与两个正参数

令
$$
u=e+1,\quad v(u)=b>0,\quad r=u/k,\quad d=v(r)=b-a,
$$
$$
Q=ek,\quad\delta=1-Q,\quad
\ell=\frac{u((k+2)^2-2ek)}{k(uk+2)},\quad
m=u-\ell,\quad M=\ell^2\delta-m^2.
\tag{2}
$$
原 $u,k$ 均非零；允许 $d$ 为负、零、正。

沿已刊完整原定义，记
$$
J=2u(1-u)+\ell Q,\quad A_*=4uQ-J,\quad
C_*=A_*m^2+J\delta\ell^2,
$$
$$
\mu=2\lambda-3,\quad
A_2=(\mu^2+4\mu+5)/2,\quad
B_3=(\mu^3+6\mu^2+12\mu+7)/2,
$$
$$
D=\ell A_2-T^2,\qquad K=\ell^2B_3-3\ell A_2T+2T^3.
\tag{3}
$$
本 $b_0$ 图的三个必要式是
$$
A_*T=uQ\ell\mu,
\tag{4}
$$
$$
q_2=2A_2C_*+2M\ell Q(3-4\lambda)
       -8uQ\delta\ell T^2=0,
\tag{5}
$$
$$
R_6=MK^2-4m^2D^3=0.
\tag{6}
$$
另保留完整 NV 给出的原 $N_5=0$。原 q2、R6、N5 的唯一同点定义来源为已刊小源
[2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob 47281af16fdd0ad7500ecda377c3cb9f9d65e725，SHA256 e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8。此处不执行它的任何旧标量或 gcd。

下文 $O(k^j)$ 指估值至少 $ja$ 的元素；不预设存在解析展开或平方根 $k^{1/2}$。所有剩余值均在对应元素已经证明整之后才使用。

## 2. 全部 b/a 的统一 q2 系数

令
$$
L=\ell/r=
\frac{4+6k-2uk+k^2}{2+uk},\qquad
g=\frac{A_*}{uQ}
=1+\frac{4u-k+3uk}{2+uk}.
\tag{7}
$$
二者是赋值环单位，$\bar L=2,\bar g=1$。原 (4) 精确给
$$
T=\kappa\mu,\qquad \kappa=\ell/g=rL/g.
\tag{8}
$$
此处 $g$ 的单位是由 (7) 实际算出的，不是假设 $A_*$ 本身估值为零。

再记
$$
B=\frac{kM}{u^2}=2L-k-eL^2,\qquad
C=\frac{kC_*}{u^3}.
\tag{9}
$$
它们都是整元素且
$$
\bar B=8,\qquad \bar C=-16,\qquad
\overline{eBL}=-16.
\tag{10}
$$
例如 $J/(uk)\to-3$、$A_* /(uk)\to-1$，所以
$C=(A_*/(uk))(m/r)^2+(J/(uk))\delta L^2\to-4-12=-16$。

将 (5) 除以非零 $u^2r=u^3/k$，得到准确二次式
$$
A_\mu\mu^2+B_\mu\mu+C_\mu=0,
\tag{11}
$$
$$
A_\mu=C+rU_\mu,\quad
U_\mu=-8e\delta L^3/g^2,\quad
B_\mu=4(C-eBL),\quad C_\mu=5C-6eBL.
$$
其中
$$
\bar U_\mu=64,\qquad
B_\mu\in\mathfrak m,\qquad
\bar C_\mu=16.
\tag{12}
$$
特别 $\mu=0$ 不满足 (11)。以下分层没有把它漏掉。

### 2.1 b<a

此时 $d<0$，故 $v(A_\mu)=d$。若 $s=v(\mu)\le0$，则 $A_\mu\mu^2$ 是 (11) 唯一最低项，矛盾。故 $s>0$，而 (11) 迫
$$
s=-d/2,\quad \overline{r\mu^2}=-1/4,\quad
v(T)=d/2,\quad \overline{T^2/r}=-1.
\tag{13}
$$
由 $\bar\lambda=3/2$ 和 (3)，
$$
\overline{\ell/r}=2,\quad\overline{m/r}=-2,\quad
\overline{D/r}=6,\quad\overline{K/r^2}=14,\quad
\overline{M/(ur)}=8.
$$
于是 (6) 两项的估值分别为
$$
v(MK^2)=b+5d,\qquad v(4m^2D^3)=5d.
\tag{14}
$$
因 $b>0$，第二项严格较低，不可能相消。整个 $b<a$ 排除。

### 2.2 b>a

此时 $d>0$，故 $A_\mu$ 是剩余值 $-16$ 的单位。(11) 首先迫 $v(\mu)=0$，再给
$$
\bar\mu=\pm1,\qquad \bar\lambda=1\ \text{或}\ 2.
$$
在两种情况下，$v(T)=d$，且
$$
\overline{D/r}=2\ \text{或}\ 10,\qquad
\overline{K/r^2}=12\ \text{或}\ -8.
\tag{15}
$$
这些均在特征1009下非零；再次得到 (14) 的严格不等估值，整个 $b>a$ 排除。

以下只需 $b=a$，此时 $r$ 是单位，记 $R=\bar r\ne0$。

## 3. b=a、mu 整：只用一个完整 N5 最低项

若 $\mu$ 整，(11)–(12) 迫 $\mu$ 为单位，且
$$
(1-4R)\bar\mu^2=1.
\tag{16}
$$
这里 $R=1/4$ 自动不可能。由 $M/k\to8R^2$，$v(M)=a$，而 $\ell,m,T,\lambda,K$ 全整。(6) 迫 $D$ 的剩余值为零。由 (3)、(8)、(16)，
$$
\bar D=2R(2\bar\mu+3).
$$
因此
$$
\bar\mu=-3/2,\quad
\bar\lambda=3/4,\quad
R=5/36,\quad
\bar\ell=5/18,\quad
\bar T=-5/12.
\tag{17}
$$
直接在 (3) 代入这些剩余值，得
$$
\bar K=25/648\ne0.
$$
(6) 于是给
$$
v(D)=a/3.
\tag{18}
$$
若 $D=0$，(6) 已与 $\bar K\ne0$ 冲突；所以 (18) 没有未处理的零值例外。

下面准确使用原 NV 的常数系数，**不施加物理 f=0**。沿已刊定义
$$
T_0=2u-\ell Q-2u^2,\quad \Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3,\quad
G=\lambda P_{02}-(1-u)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0,
$$
$$
t_s=-P_c/(bcQ\Phi),\quad V_s=-G/Q-P_c/(Q\Phi),
\quad W_s=T_0/2,\quad A_{1s}=2G/Q,
$$
$$
x_s=((u-\ell Q)V_s-mW_s)/M,\quad
y_s=(\ell W_s-uV_s)/M.
\tag{19}
$$
这是原恢复关于 $f$ 的系数定义；实际物理 $f$ 任意。完整恒等式
$$
A_{1s}=-2V_s+2bct_s
\tag{20}
$$
保留。

令 $c_\lambda=3-2\lambda$、$w=\lambda-1-T$。原三个系数可写成
$$
z_1=-2(\ell c_\lambda+2T)y_s-2\ell w
       +mTt_s/\delta,\quad
z_2=2(\ell x_s-my_s-bct_s),
$$
$$
Z_0=2(\ell c_\lambda+T)(\ell u w+V_sT)+2bct_sT^2.
\tag{21}
$$
最后一式由原完整 $Z_0$ 用 (20) 准确消掉裸 $\ell^2$ 项，而非只取主项。完整必要式为
$$
N_5=2mD(Z_0+Dz_2)+MKz_1=0.
\tag{22}
$$
它具有已刊原身份
$$
N_5=2mD\ell^2NV+Mz_{1,\rm full}H_{\rm val}
 -2mDz_{2,\rm full}q-\frac{2f}{MQ}C_4,
$$
其中 $q=M\sigma^2-D$、$H_{\rm val}=K-2mD\sigma$、
$C_4=2mDa_\Delta+MKb_0$；故原值条件与 $q_2=b_0=0$ 充分支付 (22) 的必要性，没有新 $D$ 逆。

对 $b=a$、整 $\mu$，(19) 全部给 $t_s,V_s,x_s,y_s\in\mathcal O$，且
$$
\bar t_s=2(4\bar\lambda-3),\quad
\bar V_s=4R(2\bar\lambda-1),\quad
\bar x_s=3\bar\lambda-1,\quad
\bar y_s=1-\bar\lambda.
\tag{23}
$$
因为 $g-1=O(k)$，有 $\kappa-\ell=O(k)$；所以
$\ell c_\lambda+T=(\kappa-\ell)\mu=O(k)$。又 $bc=O(k)$，(21) 给
$$
v(Z_0)\ge a,\quad z_1\in\mathcal O,\quad
\bar z_2=8R\bar\lambda=5/6\ne0
\tag{24}
$$
（最后代入 (17)）。

在 (22) 中，$2mD^2z_2$ 的估值是 $2a/3$，另外两项 $2mDZ_0$、$MKz_1$ 分别至少 $4a/3$、$a$。最低项唯一，矛盾。$b=a$ 的全部整 $\mu$ 情况排除。

## 4. b=a、mu 极点：一般估值与精确偏移

只剩 $s=v(\mu)<0$。由 (11) 可知
$$
R=1/4,\qquad
\bar\ell=\bar\kappa=1/2,\quad
\bar m=-1/2,\quad
\overline{M/k}=1/2.
\tag{25}
$$
原 (7) 还给准确公式
$$
g=1+\frac{(4r-1)k+3rk^2}{2+rk^2},
$$
$$
\ell=2r+3rk+
\frac{r(1-4r)k^2-3r^2k^3}{2+rk^2}.
\tag{26}
$$
因而 $\kappa-\ell=o(k)$，这里 $o(k)$ 表示估值严格大于 $a$。

为利用原 q2 而不倒任何新谱头，将 (5) 等价重写为
$$
D=M S,\qquad
S=\frac{g(\mu^2+4\mu+5)}{8\delta\ell}
 +\frac{3+2\mu}{4u\delta}.
\tag{27}
$$
只除已付的原纯权，不把 $S$ 或其首值当单位。

### 4.1 -a<s<0

在 (27) 中，第二项估值 $s-a$ 严格低于第一项 $2s$，所以
$$
v(D)=s.
\tag{28}
$$
令 $d_2=\ell/2-\kappa^2$。从 (3)、$T=\kappa\mu$ 直接展开，$K$ 的 $\mu^3$ 系数为
$$
k_3=\ell^2/2-3\ell\kappa/2+2\kappa^3
=-2\ell d_2+(\ell-\kappa)(3\ell/2-2\kappa^2).
$$
用 $D=d_2\mu^2+2\ell\mu+5\ell/2$，得到完整恒等式
$$
\begin{aligned}
K={}&-2\ell\mu D+\ell(7\ell-6\kappa)\mu^2
 +\ell(11\ell-15\kappa/2)\mu+7\ell^2/2\\
 &+(\ell-\kappa)(3\ell/2-2\kappa^2)\mu^3.
\end{aligned}
\tag{29}
$$
最后一项估值严格大于 $a+3s>2s$，其它项估值至少 $2s$。所以 $v(K)\ge2s$。原 R6 两项满足
$$
v(MK^2)\ge a+4s>3s=v(4m^2D^3),
$$
矛盾。此整个开区间排除。

### 4.2 s<=-a：先付准确权偏移

在 $b=a$ 时，(11) 的系数满足
$$
A_\mu=64(r-1/4)+O(k),\quad
B_\mu=O(k),\quad C_\mu\in\mathcal O^\times.
$$
由 $\mu$ 的极点和 (11)，
$$
A_\mu=-B_\mu/\mu-C_\mu/\mu^2=O(k^2)
\quad(s\le-a).
$$
因此 $r-1/4=O(k)$，(26) 进一步给
$$
\kappa-\ell=O(k^2).
\tag{30}
$$

记 $z=k\mu$。若 $s<-a$，$v(z)<0$；若 $s=-a$，$z$ 为单位，记 $Z=\bar z\ne0$。由 (27)，
$$
\overline{\frac{D}{k\mu^2}}
=\begin{cases}
1/8,&s<-a,\\
1/8+1/Z,&s=-a.
\end{cases}
\tag{31}
$$
在恒等式
$$
\frac{D}{k\mu^2}
=\frac{\ell/2-\kappa^2}{k}
 +\frac{2\ell}{k\mu}+\frac{5\ell}{2k\mu^2}
$$
中，中间项的剩余值分别为 $0$、$1/Z$，末项为零。结合 (30)，得到
$$
\overline{\frac{\ell/2-\kappa^2}{k}}=1/8,\qquad
\overline{\frac{\ell-1/2}{k}}=-1/4.
\tag{32}
$$
它们是在完整原 q2 上推出的，不预设权偏移。

$K$ 的 $\mu^3,\mu^2$ 系数分别满足
$$
k_3/k\longrightarrow-1/8,\qquad
k_2=3\ell^2-6\ell\kappa\longrightarrow-3/4.
$$
所以
$$
\overline{\frac{K}{k\mu^3}}
=\begin{cases}
-1/8,&s<-a,\\
-1/8-3/(4Z),&s=-a.
\end{cases}
\tag{33}
$$

若 $s<-a$，把原 R6 除以 $k^3\mu^6$，(25)、(31)、(33) 给
$$
0=\frac12\left(\frac18\right)^2-\left(\frac18\right)^3
=\frac3{512}\ne0.
\tag{34}
$$
故 $s<-a$ 整段排除。

## 5. 最后 s=-a 边界的完整 N5 首项

现在 $Z=\overline{k\mu}\ne0$，由 (31)、(33)，
$$
\overline{kD}=\frac{Z(Z+8)}8,\qquad
\overline{k^2K}=-\frac{Z^2(Z+6)}8.
\tag{35}
$$
R6 的同尺度必要式为
$$
3Z^3+24Z^2-48Z-512=0.
\tag{36}
$$
(35) 允许 $Z=-8$ 或 $Z=-6$ 使其中一个首值下降，没有为写 (36) 除这些因子。

为完整返回 N5，继续用 (19)–(22) 的同一系数定义。由 (25)、(30)、(32)，
$$
\bar\ell=1/2,\quad
\bar m=-1/2,\quad
\overline{M/k}=1/2,\quad
\overline{bc/k}=1/8,\quad
\overline{kT}=Z/2.
\tag{37}
$$
同时 $w=1/2+(1/2-\kappa)\mu$ 整。原定义逐项给
$$
\overline{k t_s}=4Z,\quad
\overline{kV_s}=Z,\quad
\overline{kx_s}=3Z/2,\quad
\overline{ky_s}=-Z/2.
\tag{38}
$$
例如 $\bar G=Z$、$\overline{P_c/k}=-2Z$、$\bar\Phi=-4$、
$\overline{bcQ\Phi/k^2}=1/2$；它们同时核定 (38) 中的尺度和符号，没有另选原值。

代入完整 (21)，得到
$$
\overline{kz_2}=Z,\qquad
\overline{k^2z_1}=-Z^2/2.
\tag{39}
$$
其中 $z_1$ 的第一、第三项贡献分别为 $Z^2/2$、$-Z^2$，$-2\ell w$ 在此尺度为零。

由于 (30)，$\ell c_\lambda+T=(\kappa-\ell)\mu=O(k)$。所以 (21) 中 $Z_0$ 的第一项只为 $O(k^{-1})$；第二项完整给
$$
\overline{k^2 Z_0}=Z^3/4.
\tag{40}
$$
这一步使用了原 (20) 的准确相消；若误把旧 $f$ 常数项当成物理 $f=0$，就没有这里的合法来源。

最后将整个原 (22) 乘 $k^3$，(35)、(37)、(39)、(40) 给
$$
\begin{aligned}
\overline{k^3N_5}
&=-\frac{Z^3(Z+8)(3Z+8)}{64}
 +\frac{Z^4(Z+6)}{32}\\
&=-\frac{Z^3(Z+4)(Z+16)}{64}.
\end{aligned}
\tag{41}
$$
因此 $N_5=0$ 必须有 $Z=-4$ 或 $Z=-16$。但 (36) 的左侧在这两个值分别为
$$
-128,\qquad -5888=166\pmod {1009},
\tag{42}
$$
都非零。最后边界排除。

## 6. 全分层覆盖及历史边界

(14) 排除 $b<a$，(15) 排除 $b>a$；当 $b=a$ 时，第3节排除全部整 $\mu$，第4.1节排除 $-a<v(\mu)<0$，第4.2节排除 $v(\mu)<-a$，第5节排除 $v(\mu)=-a$。$\mu=0$ 已由 (11) 的单位常数项直接排除。因此所有 $b>0$ 与全部原 $\lambda$ 均已覆盖，证明 (1) 不可能。

所有新除法都发生在已经明确非零的原参数或已证赋值环单位上；$A_*$、$M$、$D$ 的可能首值下降均在分层中保留。第3、5节使用的是完整 N5 原身份，同一个 $\lambda,T,\sigma$，没有把不同范数根合成充分性。

本文不执行任何已完成或冻结源，不保存大系数。它与正一中心论文以及一般正 k 中心论文可合成该射线完整排除，但不更改其它四条未闭权射线、全 W 空性或普通 ISP 的状态。
