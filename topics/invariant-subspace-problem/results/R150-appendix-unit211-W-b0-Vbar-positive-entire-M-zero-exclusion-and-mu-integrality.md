# R150 补充：Vbar 正阶图的整个 M 深中心排除与 mu 整性

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127。日期：2026-11-29（Asia/Taipei）。

## 1. 结论及已付图

在当前正确 W、完整 b0=0、物理 D 非零的原图，取任意剩余特征1009的位置。沿[全 ell 整及 Vbar 有限权图](R150-appendix-unit211-W-b0-global-ell-integrality-and-Vbar-positive-finite-weight-chart.md)，e,k,u 已是单位，ell 整。若
$$
v(V_{\rm bar})=v(uk+2)>0,
$$
则原剩余权为
$$
u=1/2,\quad k=-4,\quad Q=2,\quad\delta=-1,\quad\ell=L,
$$
$$
m=1/2-L,\quad M=-2L^2+L-1/4,\quad
A_*=(7-4L)/2,\quad T_0=\Phi=1/2-2L.
$$
四个整个深中心 L=0,1/4,1/2,7/4 已排，不在本稿重做。

本稿的新结论是
$$
\boxed{v(M)=0,\qquad v(\mu)\ge0,\qquad\mu=2\lambda-3.}
$$
这里第一式排除 M 的两个剩余零值及其任意深相消，第二式覆盖 mu 的任意极点深度。一般有限 mu 的完整 q2/R6/N5 条件仍是后续目标；没有宣称 Vbar 整图或 W 为空。

## 2. 完整原式

在上述剩余权记
$$
H=7-4L,\quad F=8L^2-4L+1=-4M,\quad
T=2L\mu/H,\quad\lambda=(\mu+3)/2,
$$
$$
A_2=(\mu^2+4\mu+5)/2,\quad
B_3=(\mu^3+6\mu^2+12\mu+7)/2,
$$
$$
D=LA_2-T^2,\qquad
K=L^2B_3-3LA_2T+2T^3.
$$
完整原必要式为
$$
q_2=2C_*A_2+2MLQ(3-4\lambda)-8uQ\delta LT^2,
\qquad R_6=MK^2-4m^2D^3,
$$
其中 J=2u(1-u)+LQ、Astar=4uQ-J、Cstar=Astar m²+J delta L²。

完整 N5 保同一点、同一个物理 f，采用已经证明的 f 常数表达
$$
G=\lambda P_{02}-(1-u)T_0,\quad
P_c=QP_{02}(L+T)-GT_0,\quad bc=M/(4\delta),
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
\qquad N_5=2mD(Z_0+Dz_2)+MKz_1.
$$
这里 P02=-1/4-L。此表达不施加物理 f=0；原来源为
$$
N_5=2mD\ell^2NV+Mz_{1,\mathrm{full}}H_{\mathrm{val}}
 -2mDz_{2,\mathrm{full}}q-\frac{2f}{MQ}C_4.
$$
当前同点 b0/q2 使 C4=0。没有倒置 D 或将不同原范数的根拼接。

## 3. M 正阶必先给 mu 整及 D、K 零剩余

设 gamma=v(M)>0。由于 ell、m、Astar、delta 均单位，q2 的系数整。若 mu 有极点，其二次头必须零剩余；在 F=0 时该头等于
$$
-8L D_2,\qquad
D_2=[\mu^2]D
=\frac{L}{2H^2}(H^2-8L).
$$
但模 F 有 H²-8L=47-56L。两者若同时零，必须 L=47/56，而
$$
56^2F(47/56)=10280\equiv190\ne0\pmod{1009}.
$$
所以 mu 极点不可能，且没有对 M 或其首值取逆。

mu 整后，完整原 q2 的准确恒等式给
$$
D=MS,\qquad
S=\frac{A_*A_2-\ell Q(3-4\lambda)}{4uQ\delta\ell}.
$$
S 为整，故 v(D)≥gamma。若 K 的剩余非零，R6 两项的阶分别 gamma 与至少3gamma，矛盾。因此任何 M 正阶原解的剩余都满足
$$
F(L)=D(L,\mu)=K(L,\mu)=0.
\tag{1}
$$
这覆盖 gamma 任意大及所有分歧位置；没有将 M 当作一般单位图处理。

## 4. 固定五列返回排除整个 M 零剩余图

新源码对完整 D、K 的普通分子 pD,pK 构造容量(2,3)的固定矩阵，列为
$$
p_D,\ \mu p_D,\ \mu^2p_D,\ p_K,\ \mu p_K
$$
在 1,mu,...,mu⁴ 上的全部坐标。唯一第零列伴随返回给
$$
C(L)=\Omega_DD+\Omega_KK.
$$
五个矩阵坐标及两个原乘子全部实际返回；整个行列式 L 次数19，仅删除已付支持
$$
U_0=L(2L-1)(4L-1)(7-4L)
$$
的13次因子，得到 C 的 L 次数6。

随后对这一个新 C 与 F 做首次 $\mathbb F_{1009}[L]$ Bézout。实际结果是常数1，且乘子完整运输回
$$
\boxed{1=\omega_DD+\omega_KK+\omega_FF
\quad\text{于 }\mathbb F_{1009}[L,\mu,U_0^{-1}].}
\tag{2}
$$
全部有理数分母对1009为单位；各多项式分母只有 U0 支持。最后不是只核抽象 gcd：源码逐项核了 (2) 全部原系数。实际无需再乘 U0 的正幂，paidSupportPower=0。

(2) 与 (1) 冲突，故 gamma>0 不可能。M 原来整，因此 v(M)=0，整个 M 深中心排除。这个返回保 F 的全部剩余根，没有挑选其中一个根，也没有靠 F 在某域不可约。

## 5. M 单位图的全部 mu 极点排除

现在 M、Phi、Astar、delta、ell、m 均为单位，完整 q2/R6/N5 的全部恢复系数整，mu 次数分别至多2、6、5。若 mu 有极点，则下列三个最高系数必须同时具有零剩余：
$$
h_q=[\mu^2]q_2,\qquad
h_R=[\mu^6]R_6,\qquad
h_N=[\mu^5]N_5.
$$
源码从第2节完整原式提取它们，不用旧投影或某个不完整 N5 部分。

对三个新普通分子只删除已付
$$
U=U_0F
$$
支持，所得 L 次数分别5、9、10。一次固定 $\mathbb F_{1009}[L]$ 联合 Bézout 实际返回
$$
\boxed{1=\eta_qh_q+\eta_Rh_R+\eta_Nh_N
\quad\text{于 }\mathbb F_{1009}[L,U^{-1}].}
\tag{3}
$$
三个原头的全部坐标完整回乘；实际 etaN=0，q/R 两个乘子已足够给1。这个事实来自实际返回，不是事前丢掉完整 N5 或把一个因子误认为可逆。最高头中的零纤维均在 (3) 中保留，且没有 mu 头逆。

(3) 排除所有 mu 极点。所以 v(mu)≥0。原 lambda=(mu+3)/2 也整，允许 mu=0、lambda剩余0以及任何有限剩余。

## 6. 实际执行与可再生定义

冻结源码和执行前输入位于 notes：
- [源码](../notes/2026-11-29-unit211-W-Vbar-positive-M-zero-and-generic-mu-pole-original-input-8542.py)
- [执行前输入](../notes/2026-11-29-unit211-W-Vbar-positive-M-zero-and-generic-mu-pole-original-input-8542-input.md)
- [小执行回执](../notes/2026-11-29-unit211-W-Vbar-positive-M-zero-and-generic-mu-pole-original-input-8542-execution.json)

固定预算30秒/256 MiB、外45秒，零依赖。唯一数学启动为
[run 46180054993](https://github.com/Rogerhu12/math-research-public/actions/runs/46180054993)，job **141087354966**、attempt1。实际 **0.08535021399998755 秒 / 39484 KiB / exit0**；数学末记录0.015220415999976922秒。

源提交 **41d53fe1b3de06af0e4b6f5fdd484ac57df522a4**；真实 pull 到
**ad390edced8aa031e9081c3e0c7fb591c9e4e660**，于 **2026-11-28 19:13:51.291380 UTC** 检查两README，均无变。
源 blob **7fe1a0f64a101b1c980345d8f379d2ffdf1fe7cd**，
SHA256 **a8c1245ff75f96f6e0ad0ebe133af4f8de382ec9f5daf0a016350c978d3e9640**。

全文读取五条数学记录并重组 stdout：**9864 B**，
SHA256 **885a3105763557280a1e51f7925923b005a45b12d0567688fd8cc83c3b384d64**，与驱动回执一致。
完整返回统计为五个伴随坐标、九次原来源回乘、98次精确多项式整除、26次p整检查、16次有限域除法及七次Bézout返回。

| 新对象 | 真实次数 | SHA256 |
|---|---|---|
| D/K 原行列式 | L19 | 0878616820cb4940efc27b53441b0fdab1ab6c2425c18a251a98b495e69bdcd2 |
| 删除已付支持后的 C | L6 | c989c720b5cd9b9a8dbb9cfd438ec9767dde7f56ca21e6ebe0857048db29d584 |
| 模1009的 C | L6 | b5e954db2514b07c7db4ffd5c2958e88a4290272b3c4a49db07041f368b61fa8 |
| 模1009的三个 pole 标量 | L5/9/10 | b8785c3cff4e66244c55db8240b0ac75b8f3baeebc0223c821d0465c3b43e4b3 / c443481914e1a3402b0f95ff099cd70756e8e4a8e77fcd0f04fc6be78233d236 / 76fe4daac69bdde90b433966251fc3c491d04450bc4f1c5925ee8d1aa5f54f8d |
| 两个实际最终目标 | 均为1 | 080a9ed428559ef602668b4c00f114f1a11c3f6b02a435f0bdc154578e4d7f22 |

乘子由冻结源码的固定伴随、整除和有限域 Bézout 定义；只存源、参数、profiles与小回执，不保存可重算的系数载荷。先前发布工作流因名称含大写M而拒绝派发，已经在小回执记明；那次没有数学源启动。改用现有规则允许的小写名后才发生这里唯一的数学运行，未更改派发守卫。

## 7. 尚未覆盖的原图

本稿排整个 M 深中心，并使 Vbar 正阶图的 mu 为整；它没有检查一般有限 mu 的完整共同原点。后续用第2节全部 q2/R6/N5 构造新的固定原标量，不能重算本次已经成功的 M 或 pole 门。其他内部原分母、整体 W 空性及普通 Hilbert ISP 均继续保留。
