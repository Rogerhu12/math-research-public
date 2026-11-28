# W：新纯 lambda,T 四次的原三行消元与首次固定四／五阶输入

日期：2026-11-28（Asia/Taipei）。
会话：Astra-ISP-8542378f-20261127。

本稿是尚未执行的首次输入定义，不预告新结式非零、任何因式或原排空。
源自含，没有文件依赖：
`2026-11-28-unit211-W-pure-lambda-T-quartics-new-four-five-T-resultants-8542.py`。
SHA256 6cd932dfacb355d84cbb47d8ff8d466637081d31218e0bb743fd50858a60c169。
首次预算 180 秒、4 GiB，驱动 195 秒。
只保存源、准确参数定义、次数／项数／SHA 和小回执，不保存系数载荷。

## 1. 完整原图与真正的新来源

范围仍是当前 W 的原互异两值、物理 $D\ne0$ 图。
新源取三个同点纯值多项式：
$$
q_4=\frac{\mathcal C_4}{8muQ\ell^2\delta},\qquad
\mathcal R_4,\qquad
\mathcal B(\lambda,T).
$$
这里 $q_4$ 是既有全图首一 $T$ 四次，
$\mathcal R_4$ 是原二次矩／Delta 的四次，
$\mathcal B$ 是新完整 N4 四次的准确 $f$ 常数系数。
来源分别为：

- [原两个四次](../results/R150-appendix-unit211-W-original-two-quartic-necessary-values.md)；
- [全图首一 T 四次](../results/R150-appendix-unit211-W-global-monic-T-four-F-two-and-finite-original-environments.md)；
- [完整 N4 的 f 消失与纯 lambda,T 四次](../results/R150-appendix-unit211-W-full-NV-f-independent-pure-lambda-T-quartic.md)。

第三行是真正新增输入。此次不重建 native，不重新执行四次大两列、
旧 qT4/R6、Nlow/Plow 投影或任何冻结的动作／范数门。
旧原 R4 和首一 q4 只作新 Bpure 消元所需的小定义。

源没有倒置 $b_0,A_*$、任一新 T 头或 lambda 头。
它同时覆盖整个 $b_0=0$ 分支和互补支；
[该支新 F78 曲线](../results/R150-appendix-unit211-W-entire-b0-zero-original-78-weight-curve.md)
只作范围记录，不作为此次分母或剥除支持。

## 2. 新纯四次的自含定义

沿已刊权参数 $u=e+1,Q=ek$、W 的 $\ell(e,k)$，置
$$
\delta=1-Q,\quad m=u-\ell,\quad
M=\ell^2\delta-m^2=4bc\delta,\quad
T_0=2u-\ell Q-2u^2,\quad J=2u(1-u)+\ell Q,
$$
$$
\Phi=T_0+4u-4+Q,\qquad P_f=T_0(J-Q).
$$
当前 W 权身份 $J\Phi-P_f=2uQ\Phi$ 保证完整 N4 四次不含 $f$。
源以
$$
G=\lambda P_{02}-(1-u)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0,
$$
$$
t_*=-P_c/(bcQ\Phi),\quad V_*=-G/Q-P_c/(Q\Phi),\quad
W_*=T_0/2,\quad A_{1*}=2G/Q
$$
和
$$
x_*=\{(u-\ell Q)V_*-mW_*\}/M,\qquad
y_*=(\ell W_*-uV_*)/M
$$
定义 $\mathcal B$。这只是准确系数提取，不给原解新增 $f=0$ 条件。

其余 $D,K,a_\Delta,b_0,z_{1*},z_{2*},Z_{0*}$
均逐式写在自含源中，最后
$$
\mathcal B=b_0(Z_{0*}+Dz_{2*})-a_\Delta z_{1*}.
$$
源也返回其定义所用的三个小系数身份：
$$
MQ[f]z_1=2b_0,\qquad
MQ[f](Z_0+Dz_2)=2a_\Delta,\qquad
[f]\overline B_4=0.
$$
这些检查是新小输入的定义返回，不再跑此前的完整 native N4 门。

## 3. 仅取消真实三个原乘子的共同内容

令基行为 $F=(q_4,\mathcal R_4,\mathcal B)$。
每个新多项式 $P$ 都同时保存三个实际乘子 $\tau_i$，使
$$
P=\sum_{i=0}^2\tau_iF_i.
$$
若清三个乘子的纯权分母后，共同多项式因子为 $g$，
只将这三个真实乘子分别精确除以 $g$。
新行重新定义为除后乘子与同一原三行的组合，并逐个 T 坐标核回。
因此新行仍在原理想中，包含 $g=0$ 的整个面；
这不是把原方程除以未付因子。

首先构造
$$
R_3=\mathcal R_4-[T^4]\mathcal R_4\,q_4,\qquad
B_3=\mathcal B-[T^4]\mathcal B\,q_4,
$$
并按上述合法方法压缩实际乘子。
其次数均不超过 3。
再取固定三次头 $r_3=[T^3]R_3,\ b_3=[T^3]B_3$，得到新行
$$
S_2=r_3B_3-b_3R_3,\qquad \deg_TS_2\le2.              \tag{1}
$$
两个头同时为零时 (1) 仍是准确原身份，不从该点选择一个新逆。
若实际 R3 次数更低，也保留固定三次头定义和原行。

为新 S2 的结式，另对 $q_4,R_3$ 使用伪除法：
$$
h^r q_4=Q_R R_3+Q_2,\qquad \deg_TQ_2<\deg_TR_3\le3. \tag{2}
$$
每一步仅正乘实际头 $h$，完全不倒它；
源逐步核回 (2) 并把新 Q2 运输回三个原行。
这不是重新执行旧 R4/C4 的参数目标；
Q2 只与新增 S2 配成下节的新目标。

## 4. 两个新的固定 T 标量

清上述三行实际乘子的已付权分母后，第一目标是固定
$(2,2)$ 的四阶结式，而不按某一特化点的实际次数换矩阵。
若
$$
A=aT^2+bT+c,\qquad B=dT^2+eT+f,
$$
令 $p=af-cd,\ q=ae-bd,\ r=bf-ce$，直接使用
$$
(qe-pd+qdT)A+(-qb+pa-qaT)B=p^2-qr.                 \tag{3}
$$
所有 $T^0,\ldots,T^3$ 系数完整返回。
只约掉这四个真实乘子的共同因子，然后再次返回全部四坐标，
并复合回本次三个原四次来源。
两个二次头、所有更低头以及该共同因子零面均保留。

若第一目标已完整返回已付单位，则目标已完成，第二个结式不再执行。
否则第二目标是固定 $(3,2)$ 的五阶矩阵，其原行为
$$
R_3,\ TR_3,\ S_2,\ TS_2,\ T^2S_2.
$$
每个共同有限 T 根都给非零 Vandermonde 核列，所以矩阵行列式必要为零，
即使一个或两个最高头退化。
Bareiss 的每个商积实际返回；中间主元不是原参数单位，
所有主元零面由完整多项式身份保留。

若某个固定目标恒零，只记录原组合和零事实，
不从零式得出新曲线或排空。
若 R3 恒零或只有 T 常数，源记录该准确退化而不启动不适用的伪除法目标。

## 5. 唯一合法终端剥除及实际范围

全部系数分母先按已付纯权支持支付。
源没有将 $A_*,b_0,r_3,b_3$ 或新 Q2/S2 的任意内容列入单位表。

最终仅可剥原权支持，以及当前 W 已付的 $\lambda$、
$2\lambda-3$：
前者来自原非零 mean/U0 图；
后者来自独立的整
[$\lambda=3/2$ 排除](../results/R150-appendix-unit211-W-lambda-three-halves-complete-original-exclusion.md)。
整 $2\ell-1$ 支持只引用
[完整 Lhalf 排除](../results/R150-appendix-unit211-W-entire-Lhalf-complete-original-exclusion.md)，
不引用此前仅 F101 覆盖。

每个实际非零标量随后作完整 QQ 因式和乘回，
全部未付参数因子、lambda 因子及其零面保留。
多变量 gcd、一个非零模特化或只一个因子都不构成排空。
除非本次完整原组合返回已付单位，
新输出只能登记为当前同点必要 lambda／权条件，
不宣称全 W 有限或原 ISP 完成。

此输入没有添加复现门；所有数学结果和资源状态以唯一首次实际日志为准。
