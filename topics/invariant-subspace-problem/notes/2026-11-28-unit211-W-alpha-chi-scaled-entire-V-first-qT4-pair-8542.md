# 新输入：缩放完整原 V 向量，再作新的 qT4/Vlow 同点二列

日期：2026-11-28（Asia/Taipei）。Astra-ISP-8542378f-20261127；GPT-6 Astra Pro（AI-assisted）。

**尚未执行。** 固定180秒/4GiB。源 SHA256 为
c786f55735449210bddef16efc68b4a715f3b3a48e203f85e35bdce5509ea1ef，
14540 B。

## 1. 从实际失败处换原输入

17703 原源的唯一实际 run46119359308/job140900220947 在54.698322283秒以 exit1 结束，峰值201164 KiB。十二个原动作和 qT4、R6、Nlow、Plow 的六列已返回；进入三个完整 N4(V) 基底的循环时，旧 reduce_six 的纯权分母范围断言失败。失败调用先通过了完整原迹乘回，但日志未记录循环标签和实际分母，不能臆定是哪一个 Z 或哪个约化后因子。没有资源触界，也没有任何新 alpha、chi 原值行或 scalar。

旧 C9 reducer 的范围不含后来独立支付的 ell，而未缩放 V0、V1 的定义显含 ell 的逆。本次保留该旧 reducer、所有断言及其分母表，不为接受一个新分母改动旧程序。新原输入是多项式向量 ell*V0、ell*V1；完成旧范围内的原返回后，仅在外层纯权六行上使用已付 ell。

原成功 R6/Nlow/Plow 目标不重算。qT4 的六行只作为新 pair 的必要系数定义再生，并首次换入 alpha、chi 两列；不把它先前已成的六列另登记为新结论。唯一新 pair 为 (qT4,Vlow)，不是失败门尚未到达的两个旧 pair。

## 2. 准确原范围和已付单位

沿当前 W 的 D 非零、两个 singleton 原值互异的图。引用：

- [全原 alpha、chi 十行二列](../results/R150-appendix-unit211-W-alpha-chi-exact-original-ten-by-two-and-three-scalars.md)；
- [原低 D 次压缩](../results/R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)；
- [原两条四次](../results/R150-appendix-unit211-W-original-two-quartic-necessary-values.md)；
- [全图首一 T 四次](../results/R150-appendix-unit211-W-global-monic-T-four-F-two-and-finite-original-environments.md)。

记 delta=1-Q、m=u-ell、M=4bc delta。当前纯权环已付
u、Q、ell、m、M、delta、P02 和原 native 六规则的权分母。ell 和 m 使用本图已有的一般 ell=0 与等权整支排除，不向 h=k 或任何 D=0 图外推。新程序逐项调用现有 paid 支持检查；没有为新的 chi 多项式、D、K、值首项或范数求逆。

本次完整 N4(V) 来源不以某一分量、weighted 替代式或 Phi 倍数代替。其他完整原值仍需保留；两条新必要式不被宣称为充分系统。

## 3. 多项式缩放的全原身份

设

$$
A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$

$$
D=\ell A_\lambda-T^2,\qquad
K=\ell^2B_\lambda-3\ell A_\lambda T+2T^3.
$$

旧完整原值输入使用

$$
V_0=(1,\lambda-1-T,1+T/\ell,1+T/\ell),\qquad
V_1=(0,0,m/\ell-\rho,m/\ell+\rho).
$$

本次真正送入旧原 reducer 的向量为

$$
\widetilde V_0=(\ell,\ell(\lambda-1-T),\ell+T,\ell+T),
$$

$$
\widetilde V_1=(0,0,m-\ell\rho,m+\ell\rho),\qquad \rho^2=\delta.
\tag{1}
$$

源先逐个向量分量返回 $\widetilde V_i=\ell V_i$。原 N4 的每一项都对输入值向量齐次二次，因此恒等地

$$
N_4(\ell V)=\ell^2N_4(V).
\tag{2}
$$

以同一个真 Gram 的原 N4 直接计算

$$
\widetilde Z_0=N_4(\widetilde V_0),\quad
\widetilde Z_2=N_4(\widetilde V_1),\quad
\widetilde Z_1=N_4(\widetilde V_0+\widetilde V_1)-\widetilde Z_0-\widetilde Z_2.
\tag{3}
$$

三条的 rho 奇部必须实际为零。每条 (3) 在未改动的旧分母范围内完整返回六行和四个原均值来源。对每条基底先输出标签，再执行返回，避免失败时无法定位实际输入。

由 (2)，$\widetilde Z_i=\ell^2 Z_i$。因此原完整低 D 次条件恰为

$$
V_{\rm low}
=\frac{1}{\ell^2}
\left(D\widetilde Z_0+\frac{K}{2m}\widetilde Z_1+
\frac{D^2}{M}\widetilde Z_2\right).
\tag{4}
$$

括号内先在 native 六生成元中形成。仅最后的六个纯权系数乘 $\ell^{-2}$，并逐个核回 $\ell^2 r_i=\widetilde r_i$。这既保留全部原迹，也使旧 reducer 始终不接收新 ell 分母。

## 4. 原六生成动作与实际来源

native 基为

$$
b=(1,x,y,t,y^2,yt)^{\mathsf T},\qquad
F=(E_1,E_{B,e},E_{B,o},N_1,NS,PS).
$$

为新 (4) 只再生 lambda、T 的必要十二个原动作系数：

$$
M_\theta b-\theta b=E_\theta F,\qquad
\theta\in\{\lambda,T\}.
\tag{5}
$$

每列完整原乘回由旧 reducer 核出；其 NS、PS 两个误差分量实际为零。后继节点 $r_vb-P_v=\tau_vF$ 的真实动作是

$$
r_{\theta v}=r_vM_\theta,\qquad
\tau_{\theta v}=r_vE_\theta+\theta\tau_v.
\tag{6}
$$

每个二元单项式固定先 T 后 lambda，不假定六个原生成元自由，也不假定两个矩阵在整个自由六模上交换。源保留父节点、系数和原基底迹；(6) 是完整可再生原 DAG，不另外展开大乘子。

新末次纯权缩放也作为 DAG 节点保留。因此 (4) 的来源是四原均值加上完整 N4(V) 原条件的已刊低 D 次恒等式，没有把未知公共因子除出原方程。

## 5. 新 qT4/Vlow pair

为固定 qT4，置

$$
A_*=4uQ-J,\quad C_*=A_*m^2+J\delta\ell^2,\quad c=3-2\lambda,
$$

$$
a_*=M\ell^2Q(3-4\lambda)+MA_*T^2+
2MuQc\ell T+DC_*,
$$

$$
b_*=2Mm(A_*T+uQc\ell),\qquad
q_{T4}=\frac{2mDa_*+Kb_*}{8muQ\ell^2\delta}.
\tag{7}
$$

(7) 是已刊 C4 除已付的纯权 T 四次头，所有原首项零已由原图范围处理；不引入新几何逆。

分别把 (4)、(7) 的六行一次代入已刊 alpha、chi 坐标。因 x,y,t 对 alpha 一次，得到 alpha 至多二次多项式。对已成实际首一

$$
q_\alpha=\alpha^2+q_1\alpha+q_0
$$

作唯一短除，返回

$$
\widehat P-[\alpha^2]\widehat P\,q_\alpha=r_0+r_1\alpha.
\tag{8}
$$

源完整核 (8) 和两个纯权清分母缩放，未知 chi 内容不除。两条线性式的 alpha 倍由同一首一关系逻辑得到，本次不宣称展开其大系数。

取清分母两行 $(a,b)$、$(c,d)$。仅对两个实际乘子 $(d,-b)$ 求共同多项式因子 g，并在两乘子中精确除去：

$$
\mu_0=d/g,\qquad \mu_1=-b/g,\qquad
\mu_0(a+b\alpha)+\mu_1(c+d\alpha)=C.
\tag{9}
$$

源实际核两列与完整 (9)，故 g=0 的整纤维也被新原组合覆盖。最后只剥已付纯权因子，未付权曲线或 chi 首项全留。若 C 非恒定，仅是一条必要关系；若为零，如实保留，不据此声称排空。

## 6. 实际执行范围

只复用 a96d 源在 newfive 标记前9855 B的必要坐标和 q-alpha 定义；SHA256
c1436ea6bb67d4c720016091fb65f439be5bfcc7af131c00a0749321fcf45e43。

其完整文件为
2026-11-28-unit211-W-alpha-chi-full-original-ten-by-two-8542.py，
SHA256
18101a4af587253e1dad49cee60d188c60db401ed34b13cf73edeb4e09b6d42b。

唯一下一层依赖：
2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py，
SHA256
10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1；
只14656 B定义前缀，SHA256
88b8e2f49f925e51c0b940f929efb502ced9ed358228a605fea3755d9cdefff8。

不进入旧十行、三个 scalar、原 R6/Nlow/Plow 目标、旧参数 cofactor、旧范数或任何已冻尾段。各层 alarm 与 setitimer 同受最外层180秒绝对截止限制，地址硬界4GiB。阶段失败只保已完成范围；不提高预算或重复执行。

全部输出只保源、参数定义、次数/项数/字节数、SHA 与状态，不打印或保存可重算大系数/编码片/矩阵。
