# 新输入：正确 Phi 全第二 NV 头的五生成原交换差列与非零纯权支持

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**状态：未执行。** 目标是使用新显示五生成结构，首次构造一个覆盖全部当前第二头权图的原纯权必要式。没有预报该式非零或任何空性。源码不计算此前两个 sigma scalar 的 gcd，不重做旧六列、二十列、奇部八列、第一头冻结消元或 QQ[u] 幺模门。

源码：**2026-11-28-unit211-Phi-zero-corrected-second-NV-head-five-generator-original-commutator-weight-support-8542.py**。

Git blob：**d2de722a2e2dc270979676f3456876f9055b1b4e**。SHA256：**8b6155be7e54a2e84866869e9427a486731522583364f39aa2ccb7d8749dcb54**。字节：**16501**。

零依赖；固定 **120 秒 / 1 GiB**，外 135 秒。唯一预定有限域点
$$
p=1009,\qquad (u,Q)=(2,2).
\tag{1}
$$
输入不合格、秩不足或资源截止均保留已成定义和准确边界，不换点、换素数、恢复队列或增加预算。

## 1. 当前原图和新来源

范围是正确 Phi、物理 $D\ne0$ 的第二 NV 头
$$
B_2=\ell(3-2\lambda)+2T+2m\sigma=0.
$$
完整 [ell=3/2 交集排除](../results/R150-appendix-unit211-Phi-zero-corrected-second-NV-head-ell-three-halves-complete-original-exclusion.md)，唯一 actual run 46179464150，刚支付了本第二头上的 $3-2\ell$。它没有被外推到第一头。

本源的原结构来自新纸稿
[R150-appendix-unit211-Phi-zero-corrected-second-NV-head-global-four-head-unit-and-five-generator-algebra.md](../results/R150-appendix-unit211-Phi-zero-corrected-second-NV-head-global-four-head-unit-and-five-generator-algebra.md)，blob **684ebcc38efad5443caf22906b9b249e70e412f7**。记
$$
s=u-1,\quad \delta=1-Q,\quad L=Q-2s(u-2),\quad
\ell=L/Q,\quad m=u-\ell,\quad K_w=Q+4s,
$$
$$
T_0=-K_w,\quad J=Q-4s^2,\quad P_{02}=2sL,\quad
M_n=2uL-L^2-u^2Q .
$$
本次全部权分母只准含
$$
Q,\ \delta,\ s,\ K_w,\ L,\ M_n,\ uQ-L,\ 3Q-2L.
\tag{2}
$$
其中 $m$ 的正确原单位来源是已核整个等权原排除；其余均为当前纯权单位。物理 $D,t,f-u,\lambda,\sigma$ 不倒置。

## 2. 三条完整原式与四条普通三次规则

设
$$
a=\lambda-\frac32,\quad j=\ell\left(\lambda-\frac12\right)-m\sigma,
\quad E=P_{02}j/T_0,\quad
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q},
$$
$$
w=\lambda-1-j+\ell,\quad \theta=u-\ell Q.
$$
完整两个矩为
$$
E_2=\ell a^2-2ma\sigma+\ell\delta\sigma^2-A_\lambda,
$$
$$
E_3=\ell a^3-3ma^2\sigma+3\ell\delta a\sigma^2-m\delta\sigma^3-B_\lambda.
\tag{3}
$$
新纸稿从真正 dual germ Gram 给完整
$$
N^\sharp
=2\left[-\left(\lambda^2+\lambda-\frac34-\delta\sigma^2\right)f
 +(a^2-\delta\sigma^2)E-w(ua+\theta\sigma)\right],
$$
$$
NV=N^\sharp-2fE_2.
\tag{4}
$$
源码另以已经成立的幂等元极化紧凑定义回核 (4) 的全部普通系数；该部分只再生三个唯一原参数，不调用旧六列/两 cofactor 的驱动。

按基 $(\lambda^3,\lambda^2\sigma,\lambda\sigma^2,\sigma^3)$，四条
$$
\lambda E_2,\quad \sigma E_2,\quad E_3,\quad NV
$$
的头矩阵 $H$ 由实际原式逐系数构造。其显示行列式为
$$
\det H=2P_{02}m\delta(3-2\ell).
\tag{5}
$$
这是 (2) 的单位。源码只用这个原值和固定 $3\times3$ cofactors 构造 $H^{-1}$，并完整返回双向 32 坐标。没有选择几何主元或新的权头。

因此对四个三次单项式 $m_i$，得到普通原身份
$$
m_i=r_i+\sum_{k=1}^3\tau_{ik}F_k,\qquad
(F_1,F_2,F_3)=(E_2,E_3,NV),\quad \deg r_i\le2.
\tag{6}
$$
另有真正首一二次规则
$$
\sigma^2=r_2+\frac{E_2}{\ell\delta},
\tag{7}
$$
右侧 $r_2$ 不含 $\sigma^2$。四个三次头和这条二次规则都只使用 (2)。

## 3. 固定降次、五原动作与真正交换差来源

取
$$
\mathcal B=(1,\lambda,\sigma,\lambda^2,\lambda\sigma).
\tag{8}
$$
固定降次算法先处理最高总次数至少三的单项式，按次序选可整除它的
$\lambda^3,\lambda^2\sigma,\lambda\sigma^2,\sigma^3$，使用 (6) 降次。每次总次数严格下降。总次数至多二后，只用 (7) 消最后的 $\sigma^2$。

每次输出向量 $v(p)\in A^5$ 和三个普通原标签 $\tau(p)$，完整返回
$$
p=\mathcal B\,v(p)+\tau(p)\cdot F.
\tag{9}
$$
(8) 是真实商的生成集，不假定自由。对每个基元乘 $\lambda$、$\sigma$，用 (9) 得矩阵 $M_\lambda,M_\sigma$ 和十组标签：
$$
\lambda\mathcal B_j
 =\mathcal B(M_\lambda e_j)+\tau^\lambda_j\cdot F,
\qquad
\sigma\mathcal B_j
 =\mathcal B(M_\sigma e_j)+\tau^\sigma_j\cdot F .
\tag{10}
$$
每个普通多项式身份都实际回乘。

对每个 $j=0,\ldots,4$，固定新种子
$$
c_j=(M_\lambda M_\sigma-M_\sigma M_\lambda)e_j.
$$
它有真实原来源
$$
\mathcal Bc_j=
\left[
-\lambda\tau^\sigma_j
-\sum_i(M_\sigma)_{ij}\tau^\lambda_i
+\sigma\tau^\lambda_j
+\sum_i(M_\lambda)_{ij}\tau^\sigma_i
\right]\cdot F .
\tag{11}
$$
源码对全部五个 (11) 作普通系数返回。它不把两个裸矩阵的交换性当作假设：这些交换差本身就是新原理想列。

若 $\mathcal Bv=\Omega\cdot F$ 已由实际列给出，则新子列
$M_\lambda v$ 的普通原标签为
$$
\Omega^\lambda=\lambda\Omega-\sum_i v_i\tau^\lambda_i,
\tag{12}
$$
$\sigma$ 同理。每个新子列都完整回乘 (12)。因此任意本输入实际生成的 DAG 列始终有原 $E_2,E_3,NV$ 来源，不依赖一个自由五维结合代数。

## 4. 预定点只选择原列，不支付空性

只在 (1) 的唯一点进行一次有限域秩选择。在看秩之前，先核 (2) 的点值和全部实际动作/种子分母；有理常数通过分子分母的共同整数化准确处理。若这个点不合格，报告边界并停止，不选择另一个点。

队列初始恰为五个 (11)，按固定基顺序。每次以模点的 Gaussian 余向量判断是否独立，但保留的对象始终是**原 QQ 有理列及其普通原标签**。每选中一条原列，仅将其两个 (12) 子列按 lambda、sigma 次序入队；跳过的 Gaussian 余向量永不成为原输入。

达到秩五立即停止。若队列耗尽而秩不足五，只报告这个固定点和该原列队列的真实秩，不作新非零行列式或空性结论。本协议至多选择五条原列；最后一条不再扩展，故队列总量有限，不是无界搜索。

模点没有原几何 $\lambda,\sigma$ 的取值。这个固定权点只用于证明所定义纯权多项式非零；结论不扩展为整个第二头或其剩余纯权零纤维为空。

## 5. 实际整列清分母与普遍原 adjugate 身份

仅当选择了五条原列 $v_j$，对每列取五个**实际约消后系数**的权分母 LCM，记为 $d_j$。各 $d_j$ 只含 (2)。随后清有理整数分母并除共同非零整数内容，得到整数多项式列
$$
B_j=\gamma_j v_j\in\mathbb Z[u,Q]^5.
\tag{13}
$$
$\gamma_j$ 是 (2) 的权单位乘非零有理数。除整数内容没有移除任何纯权零面。源码逐五坐标返回 (13)，并将同一 $\gamma_j$ 乘到全部三个原标签，完整返回
$$
\mathcal BB_j=\Omega_{1j}E_2+\Omega_{2j}E_3+\Omega_{3j}NV.
\tag{14}
$$
这些标签的每个实际分母再次按 (2) 核对。设
$$
B=(B_1,\ldots,B_5),\qquad F_{\rm wt}(u,Q)=\det B.
\tag{15}
$$
本输入**不展开** (15) 的巨大 QQ 多项式。其定义已由全部实际整数矩阵条目唯一固定。

普遍恒等式
$$
B\,\operatorname{adj}(B)e_0=F_{\rm wt}e_0
$$
结合 (14)，由于 $\mathcal B e_0=1$，直接给
$$
\boxed{
F_{\rm wt}
=\sum_{r=1}^3
\left(\sum_{j=1}^5
 \operatorname{adj}(B)_{j0}\Omega_{rj}\right)F_r
\quad\text{于原已付系数环。}}
\tag{16}
$$
这是整个本第二头图的原必要纯权支持，包含所有矩阵秩降、临时选择关系退化及未付 $F_{\rm wt}=0$ 纤维。不存在从泛型满秩直接宣布整个图空的步骤。

最后只在同一个 (1) 点核整数列尺度非零，并以真实 $5\times5$ 模矩阵的完整双向逆返回 50 坐标。若 determinantModuloP 非零，才付 $F_{\rm wt}\ne0$ 这个 QQ 多项式命题。未检验另一点、另一素数或原几何值。

## 6. 次数只给已付上界

整数 $B$ 的每个非零条目已有准确 $u$、$Q$、总次数。对每个坐标，枚举固定五阶的 120 个置换，取非零匹配的最大次数和，得到
$$
\deg_u F_{\rm wt}\le d_u,\qquad
\deg_Q F_{\rm wt}\le d_Q,\qquad
\deg F_{\rm wt}\le d_{\rm tot}.
\tag{17}
$$
这是行列式展开的严格上界，不声称最高项没有相消，也不把模点的非零常数当成保度证据。条目整化、全部原来源、匹配上界与模双向逆都单独记录小 profiles。

源码没有计算 $F_{\rm wt}$ 的因式、paid 内容或与旧支持式的 gcd；不从旧模结果猜测删因子。若成功，新结论只是在整个当前第二头上得到一个定义明确、QQ 非零的纯权必要多项式及其上界。该多项式的完整零集仍需后续真正新输入。

## 7. 执行边界

这是五生成结构后第一次原交换差/DAG纯权目标。四阶头及十条动作是本次新矩阵定义的必要来源，不重跑旧 scalar 输出、旧失败中间态或已有同值门。没有完整系统充分性、自由模、模 D 幂零提升、有限点推空或整个 Phi 排除。

任何实现异常或固定预算截止都只登记最后完整原返回；不增加预算、不恢复队列、不改列次序或换点。输出只有原定义、profiles、真实返回计数及范围，不保存系数载荷或编码缓存。
