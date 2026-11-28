# 新输入：W/b0 内部 delta 正估值的一般有限 mu 同点三原剩余返回

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / r150_open_geometry。日期：2026-11-29（Asia/Taipei）。

**状态：未执行的新输入。** 当前正确 W、完整 $b_0=0$ 的内部赋值范围为
$$
v(e)=v(k)=v(u)=0,\qquad v(\delta)>0,\qquad
u=e+1,\ Q=ek,\ \delta=1-Q.
$$
本次只处理下面准确列出的剩余开图；不从原物理非零条件自动推其首值非零，不预报排空。

源码：**2026-11-29-unit211-W-b0-internal-delta-open-three-original-same-mu-residues-8542.py**。

Git blob：**b2a31315dc3eb95e969f6573adf29a3bd7072c84**。SHA-256：**b352d1055ddafd27be722b5d855b1bd1cbbd91c043745e07b99b8288c5d0a7c5**，12258 bytes。

零执行依赖，固定 **120 秒 / 1 GiB**，外层135秒。只有 Python 标准库；源内固定特征1009，不选点、不换素数、不枚举某个剩余域的根。全部系数和乘子以 $\mathbb F_{1009}[u]$ 及其有理函数域的精确普通算术实现。没有旧射线、初始理想、C74/C78、PRS 或同 mu 标量门的再次执行。

## 1. 准确剩余图及其全部补图

设
$$
S(u)=u(u-1)(3u-2)(2u^2-1)(2u-1)
                 (4u^2+2u-3)(4u-3).
\tag{1}
$$
本次仅在 $\overline{S(u)}\ne0$ 的原剩余点工作。代码中的 paid-support 检查只表示 (1) 这个**明示剩余开图**的单位，不表示这些原物理量在任意1009赋值下都已有非零首值。

当 $\bar Q=1$ 时，正确 W 权定义准确专门化为
$$
\begin{gathered}
\ell=\frac{u(2u^2-1)}{3u-2},\qquad
m=-\frac{u(u-1)(2u-1)}{3u-2},\qquad M=-m^2,\\
J=2u(1-u)+\ell,\qquad
A_*=4u-J=\frac{u(4u^2+2u-3)}{3u-2},\\
T_0=2u-\ell-2u^2,\qquad
\Phi=-\frac{2(u-1)^2(4u-3)}{3u-2},\\
P_{02}=2u(u-1)(2u-1).
\end{gathered}
\tag{2}
$$
源码在新算术环中完整核回四个显示权恒等式，且核每个实际分母只含 (1) 支持。

所有 S=0 剩余点在本输入之外保留。部分补图已有或正在独立成文的原排除：

- u 正阶是先前独立原边界；本输入本来假定 u 是赋值环单位。
- $3u-2=0$ 的 ell 极点由根的独立原分层处理，不在本输入删除一个未证明的深分量。
- $2u-1=0$ 的整个深 m 支见新 [delta/u 二分之一原纸证](../results/R150-appendix-unit211-W-b0-internal-delta-positive-u-half-entire-original-valuation-exclusion.md)。
- $4u^2+2u-3=0$ 的整个 Astar 正阶支见新 [delta/Astar 原纸证](../results/R150-appendix-unit211-W-b0-internal-delta-positive-Astar-entire-original-valuation-exclusion.md)。
- ell 剩余零与 Phi 剩余零的完整纸面分层将另行成文；本源不以尚未刊出的概述作为单位依据。

因此无论新返回如何，单次程序都只陈述 (1) 开图的结果。补图必须按各自准确原来源拼接。

## 2. 新输入来自完整原 q2、R6、N5

共同原定义为 [完整 b0/N5 源](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob **47281af16fdd0ad7500ecda377c3cb9f9d65e725**，SHA-256 **e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8**。本次不执行或导入其旧驱动；只在自含源内写出已经成立的原定义。

置
$$
\mu=2\lambda-3,\quad
A_2=(\mu^2+4\mu+5)/2,\quad
B_3=(\mu^3+6\mu^2+12\mu+7)/2,
$$
$$
T=\frac{u\ell}{A_*}\mu,\qquad
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell A_2T+2T^3.
\tag{3}
$$
三个新原剩余式为
$$
\mathcal Q=2A_*m^2A_2+2M\ell(-3-2\mu),\qquad
\mathcal R=MK^2-4m^2D^3,
\tag{4}
$$
和下面完整 N5 的正则剩余。

原 N5 虽显示 $t_s/\delta$，但在原权函数域内已有准确恒等式
$$
bc\,t_s=-\frac{P_c}{Q\Phi},\qquad
\frac{mTt_s}{\delta}=-\frac{4mTP_c}{MQ\Phi}.
\tag{5}
$$
先用 (5)，所有 delta 分母完全取消，然后才取 Q=1。定义
$$
\begin{gathered}
G=\lambda P_{02}+(u-1)T_0,\quad
P_c=P_{02}(\ell+T)-GT_0,\\
V_s=-G-P_c/\Phi,\quad
y_s=(\ell T_0/2-uV_s)/M,\quad w=\lambda-1-T,\\
z_1=-2(-\ell\mu+2T)y_s-2\ell w-\frac{4mTP_c}{M\Phi},\\
z_2=-2G-4my_s,\qquad
Z_0=2(T-\ell\mu)(\ell uw+V_sT)-\frac{2P_cT^2}{\Phi},\\
\mathcal N=2mD(Z_0+Dz_2)+MKz_1 .
\end{gathered}
\tag{6}
$$
全部实际分母只由 (1) 支付。这里的 f 常数定义来自完整原 N5，不施加物理 f=0。整个原来源仍是
$$
N_5=2mD\ell^2NV+Mz_{1,\rm full}H
       -2mDz_{2,\rm full}q-\frac{2f}{MQ}C_4.
\tag{7}
$$
当前同点 b0、q2 下 C4 为零，所以任何原点均给 (4)、(6) 为零；不倒 D，不把几项范数为零当成原值充分条件。

在本开图，原 q2 的 mu 二次头剩余是 $m^2A_*$，为赋值环单位。其其他系数也整，因此在取剩余前已经能将 q2 首一化，**mu 必整**。无需预先假定 lambda 或 mu 的首值非零。于是完整原等式都可在同一个剩余 mu 上合法化为 (4)、(6)。

## 3. 同一个首一二次及两条真实一次余式

在
$$
A=\mathbb F_{1009}[u,S(u)^{-1}]
$$
中，令
$$
q=\frac{\mathcal Q}{m^2A_*}
  =\mu^2+q_1\mu+q_0.
\tag{8}
$$
源实际核其 mu 头为1，并对同 q 作两次普通首一除法：
$$
r=\mathcal R-Q_Rq=a_R+b_R\mu,\qquad
n=\mathcal N-Q_Nq=a_N+b_N\mu .
\tag{9}
$$
q、r、n 的三原来源逐 mu 坐标返回；每个实际权分母重新核只含 (1)。这里没有反演 bR、bN、某个新头或任何几何条件。

这是真正同一点、同 mu 的两行。即使某行整式为零、某个一次头为零、两个头同时为零，下面的固定普通身份仍成立。

## 4. 一个交叉式及两个同 mu 范数

固定构造三个纯 u 标量：
$$
C_\times=b_Nr-b_Rn=a_Rb_N-a_Nb_R,
\tag{10}
$$
$$
C_R=(a_R-q_1b_R-b_R\mu)\,r+b_R^2q
       =a_R^2-q_1a_Rb_R+q_0b_R^2,
\tag{11}
$$
$$
C_N=(a_N-q_1b_N-b_N\mu)\,n+b_N^2q
       =a_N^2-q_1a_Nb_N+q_0b_N^2 .
\tag{12}
$$
源把 (9) 的完整原乘子复合回 $\mathcal Q,\mathcal R,\mathcal N$，逐 mu 坐标核回 (10)–(12)。这三式始终只是原必要条件；不宣三个范数/交叉为零就充分给原共根。

各标量的约消后纯 u 分母只含 S。乘自己的实际分母得到普通 $\mathbb F_{1009}[u]$ 多项式 $c_i$，并将该乘子同步乘到全部三个原来源后再次核回。代码中纯 u 分母通过 $MP(F(d))$ 嵌入常数 mu 系数，避免把 u 系数列表误当 mu 多项式。

随后只对这三个**新的原剩余标量**作一次完整 $\mathbb F_{1009}[u]$ 累积 Bézout：
$$
g(u)=s_\times(u)c_\times(u)+s_R(u)c_R(u)+s_N(u)c_N(u).
\tag{13}
$$
每个阶段不仅核单变量 Bézout，也再次把 (13) 复合返到三条原 mu 多项式。没有旧 char0 投影、旧同点 norm 或其他射线初项的复算。

## 5. 只按实际返回决定开图范围

若三标量全零，则保留整个开图，不称有新 u 覆盖。

否则 g 首一。只对 (1) 的明确剩余单位支持作反复 gcd 精除，全部商积返回。若留下非恒定因子，报告其完整必要剩余支持的定义、次数与 SHA，**全部零纤维保留**；不额外选择素数、点或次序去寻求空性。

只有实际 g 的全部不可留支持都在 S 上时，令 $B=\deg g$。普通单变量除法须完整返回
$$
S^B=g\,q_g.
$$
B=0 时这就是常数1。将 (13) 的三个实际来源乘 $q_g$，再清最后全部实际纯 u 分母 L，返回
$$
\boxed{\qquad
L(u)S(u)^B
 =\Omega_Q(u,\mu)\mathcal Q
  +\Omega_R(u,\mu)\mathcal R
  +\Omega_N(u,\mu)\mathcal N .
\qquad}
\tag{14}
$$
这里 Omega 为普通 $\mathbb F_{1009}[u,\mu]$ 多项式；L 的支持逐因子仅在 S 中。最终整个原 mu 多项式再次乘回，不仅比较首一二次的余类。

(14) 左侧在本剩余开图是单位，因此足以排全部原赋值点在这个图中的剩余，包括任意剩余域扩张。**这不是从一个任取模点推 QQ 泛型空性**：已经给出每个所考虑的原点的整性，且 (14) 是整个剩余开图的普通多项式矛盾。没有从模 D 幂零提升 char0 D 幂零，也没有选择某个 u 或 mu 根。

## 6. 首次执行和记录边界

固定 p=1009、固定三个原输入、固定一个 cross 和两个 norm、固定顺序。每项数学结果只有实际完整乘回后输出；若资源界或实现错误先到，就只记录最后完整 checkpoint。没有自动重试、扩限、换点、换素数或接续失败门。

输出只保参数定义、profiles、实际乘回计数、源 SHA 与完整范围；不缓存或传送大系数、编码参数或重放载荷。本输入不执行、重算或宣称已关闭 S=0 的补图，更不预记整个 delta 边界排除。
