# 新输入：Vbar 正阶有限权图的 M 零中心及一般 mu 极点

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127。日期：2026-11-29（Asia/Taipei）。

**未执行的新原目标。** 固定源码
2026-11-29-unit211-W-Vbar-positive-M-zero-and-generic-mu-pole-original-input-8542.py，
Git blob **7fe1a0f64a101b1c980345d8f379d2ffdf1fe7cd**，
12100 B，SHA-256 **a8c1245ff75f96f6e0ad0ebe133af4f8de382ec9f5daf0a016350c978d3e9640**。
零依赖，固定 **30 秒 / 256 MiB**，外层45秒；不换素数、标量、算法或预算，不继续旧失败门。

## 1. 已证明的范围

沿[全 ell 整与 Vbar 有限图](../results/R150-appendix-unit211-W-b0-global-ell-integrality-and-Vbar-positive-finite-weight-chart.md)，当前正确 W/b0 原点的所有1009位置满足 e,k,u 单位、ell 整。若 r=uk+2 正阶，剩余权准确为
$$
u=1/2,\quad Q=2,\quad \delta=-1,\quad \ell=L,
$$
$$
m=1/2-L,\quad M=-2L^2+L-1/4,\quad
A_*=(7-4L)/2,\quad \Phi=T_0=1/2-2L,\quad P_{02}=-1/4-L.
$$
四个整个深中心 $L=0,1/4,1/2,7/4$ 已排除。本次不重复这些证明，也不把 P02 的零剩余值删除。记
$$
H=7-4L,\quad F=8L^2-4L+1=-4M,\qquad
T=2L\mu/H,\quad\lambda=(\mu+3)/2.
$$
完整剩余原定义是
$$
A_2=(\mu^2+4\mu+5)/2,\quad
B_3=(\mu^3+6\mu^2+12\mu+7)/2,
$$
$$
D=LA_2-T^2,\quad K=L^2B_3-3LA_2T+2T^3,
$$
$$
q_2=2C_*A_2+2MLQ(3-4\lambda)-8uQ\delta LT^2,\quad
R_6=MK^2-4m^2D^3 .
$$
源码从这些完整原式构造；没有以先前的某个投影代替原输入。

## 2. M 首值为零时，mu 整且原 D、K 首值全零

这里允许 M 任意正阶。若 mu 有极点，q2 的最高二次项必须在剩余域为零。在 F=0 时，该头是
$$
-8L D_2,\qquad
D_2=L/2-4L^2/H^2
=\frac{L}{2H^2}(H^2-8L).
$$
但模 F 有 $H^2-8L=47-56L$。假如两者共零，需 L=47/56，而
$$
56^2F(47/56)=10280\equiv190\ne0\pmod{1009}.
$$
所以该最高头必是单位，mu 极点不可能。这里没有将 M 当作单位或反演其首值。

mu 整后，完整 q2 的准确身份给
$$
D=MS,\qquad
S=\frac{A_*A_2-\ell Q(3-4\lambda)}{4uQ\delta\ell}.
$$
S 在本图为整，因为 u,Q,delta,ell,Astar 都是单位。若 gamma=v(M)>0，则 v(D)≥gamma。若 K 剩余非零，原 R6 的两项阶分别 gamma 与至少3gamma，矛盾。因此任何 M 正阶原点的剩余满足
$$
\boxed{F(L)=D(L,\mu)=K(L,\mu)=0.}
$$
这是下面目标A的完整原来源；不曾用 D 逆。

## 3. 固定目标 A：完整 D、K 的一个原标量与 F

先取完整 D、K 的普通 QQ 分子 pD,pK，保留各自原分母，固定 Sylvester 容量(2,3)，五列为
$$
p_D,\ \mu p_D,\ \mu^2p_D,\ p_K,\ \mu p_K.
$$
只做这个固定5乘5矩阵的第零坐标伴随返回。若该行列式非零，返回全部五坐标，并实际构造
$$
C(L)=\Omega_D(L,\mu)D+\Omega_K(L,\mu)K.
$$
没有反演 mu 的首项；首项零纤维及全部重数仍在普通组合内。若固定标量为零，保留整个 M 零支，不另选余子式。

只可去掉已付支持
$$
U_0(L)=L(2L-1)(4L-1)(7-4L).
$$
然后做这两个**新**标量 C、F 在 $\mathbb F_{1009}[L]$ 的首次联合 Bézout。每条乘子都返回到完整 D、K、F，模1009逐项核全部原系数；分母只有 U0 支持，且每个有理数分母都对1009为单位。
最终保留
$$
U_0(L)^a g(L)=\omega_DD+\omega_KK+\omega_FF
\quad\bmod1009.
$$
仅当实际 g 是非零常数，才排整个 M 正阶原支；若 g 非常数，保其全部可能剩余根，不作因子识别或另一个素数门。

## 4. 固定目标 B：M 为单位、mu 有极点的完整三头

这是与目标A分别注册的另一个新原目标；它只针对 M 为单位的图，不以目标A成功为执行前提。所有恢复系数的原分母在此图均已支付。

完整 N5 按已有同点原必要式定义。先取
$$
G=\lambda P_{02}-(1-u)T_0,\quad
P_c=QP_{02}(L+T)-GT_0,
$$
$$
t_s=-P_c/(bcQ\Phi),\quad
V_s=-G/Q-P_c/(Q\Phi),\quad
y_s=(LT_0/2-uV_s)/M,\quad w=\lambda-1-T,
$$
$$
z_1=-2(-L\mu+2T)y_s-2Lw+mTt_s/\delta,\quad
z_2=-2G/Q-4my_s,
$$
$$
Z_0=2(T-L\mu)(Luw+V_sT)+2bc\,t_sT^2,
\quad N_5=2mD(Z_0+Dz_2)+MKz_1.
$$
这些是原 N5 的 f 常数表达，不施加物理 f=0。原必要性来自已经证明的
$$
N_5=2mD\ell^2NV+Mz_{1,\mathrm{full}}H
 -2mDz_{2,\mathrm{full}}q-\frac{2f}{MQ}C_4.
$$

若 mu 有极点，完整 q2/R6/N5 的最高次分别至多2、6、5。由于全部系数整，三条最高系数必须同时具有零剩余：
$$
h_q=[\mu^2]q_2,\quad
h_R=[\mu^6]R_6,\quad
h_N=[\mu^5]N_5.
$$
本次从完整原式逐系数提取这三个头，再对其新普通分子做一次 $\mathbb F_{1009}[L]$ 联合 Bézout。原分母和全部乘子始终保留，最终真正返回
$$
U(L)^b g_{\rm pole}(L)=
\omega_q h_q+\omega_R h_R+\omega_N h_N\quad\bmod1009,
\qquad U=U_0F .
$$
这里只有本目标中已假定为单位的 M 支持 F 新增到 U0；目标A从未将 F 作为可删支持。
如果最高系数本来为零，零输入原样保留。只有 g_pole 真为非零常数，才排该图全部 mu 极点；不由 gcd 次数或某个有理系数看似非零声称排除。

## 5. 执行与后续范围

两个目标的次序、输入及返回范围均在首次执行前固定。源码只用普通精确多项式除法、固定 Bareiss 伴随及小一元有限域 Bézout，输出 profiles、SHA、实际返回状态与统计；不保存系数载荷、分块数据或缓存。

若目标A、B都实际返单位，可结合第2节推出整个 Vbar 正阶有限权图上 M 为单位且 mu 整。**一般有限 mu 的 q2/R6/N5 原图仍是另一个目标，本源码不执行它，也不预先称整个 Vbar 或 W 为空。** 无论本次结果如何，其他内部原分母与普通 ISP 仍须继续。
