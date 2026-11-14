# R133：同一完整方阵的三角端口、矩阵 source Gram 与方向 Green

## 1. 固定空间

本合同沿用完整 193 方阵合同 (M.1)–(M.13) 的真实反射类、固定物理
$\eta_0$、原 $\nu$、连续修补 M32 中心及全部 mean。低头状态仍为
$y=R h$，$R=\operatorname{diag}(I_{96},\rho I_{97})$。本文的 $p,q$
是 regular 与其完整补空间的坐标，**不是**频率低高分拆。
物理 source 方向 $E$ 则准确是 odd/even $33\ldots96$ 的 128 槽。

原四个实际 full193 多项式来自 run 43645186441。其原 native、数组
和 source 身份固定；本次不重新计算四格 $F$ 或任何原 target。
独立舍入的 backward 多项式不作为本条的真逆。以下所有端口、逆
source 与输出 Gram 都使用同一个新 patched forward $F$。

## 2. 完整坐标与有费用的三角化

在每个节点取
$$
 S_i=[Q_i,N_i]\in\mathbb R^{193\times193}.
 \tag{G.1}
$$
$Q_i$ 是原完整 dyadic 的 96 列 regular 锚；$N_i$ 是本次选取并
保存原字节的 97 列补空间。对准确 $S_i$ 验证完整
$\|S_i^*S_i-I\|_2<1$，并使用其真逆。不能将 $S_i^{-1}$ 免费替成
$S_i^*$，也不能从 $Q_i$ 自身推出完整传播。

设原 forward 多项式 $F_i^0(0)=I$，其 cell 参数为 $t\in[0,1]$。
先计算 $S_{i+1}^{-1}F_i^0(1)S_i$，选择并保存新的准确 dyadic
上三角块
$$
 T_i=\begin{pmatrix}A_i&B_i\\0&D_i\end{pmatrix},
 \qquad A_i:96\times96,\quad D_i:97\times97.
 \tag{G.2}
$$
被去掉的下块绝不当成精确零误差。定义准确矩阵
$$
 \Delta_i=S_{i+1}T_iS_i^{-1}-F_i^0(1),\qquad
 F_i(t)=F_i^0(t)+t\Delta_i.
 \tag{G.3}
$$
因此 $F_i(1)S_i=S_{i+1}T_i$ 是准确恒等式，且 $F_i(0)=I$。
$\Delta_i$ 的准确对象由所存 $S_i,S_{i+1},T_i$、旧 $F_i^0$ 和真
矩阵逆定义；其中间 Arb enclosure 不重新定义这个矩阵。

若旧整格下界为 $\ell_i^0$，则实际新门必须证明
$$
 \ell_i=\ell_i^0-\|\Delta_i\|_2>0.
 \tag{G.4}
$$
设 $d_i^0$ 是旧 $F_i^0$ 相对同一准确新 reference $A_*$ 的完整
微分残差，$M_i\ge\sup\|A_*\|$，$h_i$ 为真实格长。新费用为
$$
 d_i=d_i^0+(h_i^{-1}+M_i)\|\Delta_i\|_2,\quad
 \|F_i\|_\infty\le\|F_i^0\|_\infty+\|\Delta_i\|_2.
 \tag{G.5}
$$
沿用旧完整 $\epsilon_i$ 后，
$$
 \|\widetilde A_i-A_{\rm true}\|_\infty
 \le\epsilon_i+d_i/\ell_i,\qquad
 \widetilde A_i=(F_i)_xF_i^{-1}.
 \tag{G.6}
$$
所有 $\rho'$、全 mean 和原 128 个 primitive 中间模保留。
$A_i,D_i$ 的完整可逆性也分别验证。三角化只改变已明确付费的
辅助生成元，不宣称真实生成元天然上三角。

## 3. 固定 M32 的真实交叉 source

设 $\mathcal B=A_{LH}$，输入为物理高状态的 odd/even
$97\ldots160$，输出准确位于 $E$，其余 65 槽严格为零。固定 M32
系数总带宽为 64；mean-rank 输入为零，角常数的 principal 与
reaction 不跨此分拆。对于 primitive 的两次乘法，中间可能到
192，但最终回到 head $\le96$ 只读取 $|\ell|\le128$。因此仍须且
只须完整保留原 128 个中间模，不能删掉低中间槽的 signed 贡献。

原模型的 raw error 是明确的 Wiener/乘法算子门
$$
 E_{\rm raw}
 =384(E_d+\max(E_{a12},E_{a21}))
   +E_{\rm local}+E_{\rm primitive}+E_{\rm rank}.
 \tag{G.7}
$$
该定义见冻结的 regular_cut_interval_model.py 的 raw_generator。
其零阶和 primitive 项不依输入维数；这里只将最高物理角导从
384 升到 640。因此对新 raw cross reference，安全误差为
$(5/3)E_{\rm raw}$。这一步不得用有限矩阵 HS 误差代替 (G.7)。

从同一已存四阶径向系数定义重建 cross reference 后，左乘真实
$R(t)$。输入仍是普通物理高状态，不右乘 $R_H^{-1}$。本消费者完整
保留线性 $R$ 与三次 raw cross 的 degree 4 乘积，不将最高项
截掉。选取新准确 dyadic $\widehat{\mathcal B}_y(t)$ 时另付全部
矩阵舍入，得到
$$
 \|\mathcal B_y-\widehat{\mathcal B}_y\|_\infty
 \le\epsilon_{\mathcal B}
 :=\max(1,\rho_l,\rho_r)\frac53E_{\rm raw}
   +E_{\rm cross,round}.
 \tag{G.8}
$$
两者的像都仍在准确 128 槽 $E$。后继可把差写成
$\epsilon_{\mathcal B}E\,U(x)$，其中 $\|U(x)\|_2\le1$。
这条未知的方向差不得被悄悄置零。

同时保存两个独立测试 source：加权状态坐标中的 $E$，以及普通
物理 source 的 $R(t)E$。它们与
$\widehat{\mathcal B}_y$ 的单位清楚区分。

## 4. 同一 patched 逆与局部 source Gram

定义准确辅助多项式 $C(t)$，$C(0)=I$，以
$C_x=-C A_*$ 的 degree 24 **准确递推**确定其系数。该递推没有
新增未存浮点选择；其唯一对象由旧准确 dyadic generator、真实
格长及 degree 决定。Arb 仅包络这个准确对象。

完整反向作用残差为 $d_C\ge\|C_x+C A_*\|_\infty$，并保留
$C_\infty\ge\|C\|_\infty$。由
$$
 (CF_i)_x=(C_x+C A_*)F_i+C((F_i)_x-A_*F_i)
$$
与 $C(0)F_i(0)=I$ 得
$$
 \|CF_i-I\|_\infty
 \le h_i(d_C\|F_i\|_\infty+C_\infty d_i)=:\delta_i,
 \quad
 \|F_i^{-1}-C\|_\infty\le\delta_i/\ell_i.
 \tag{G.9}
$$
这里始终是真 $F_i^{-1}$，没有借用旧 independently rounded
backward $F$。

对每一准确 polynomial source $\mathcal C_y(t)$，定义
$$
 G_i(t)=S_i^{-1}F_i(t)^{-1}\mathcal C_y(t),\qquad
 P_i(t)=S_i^{-1}C(t)\mathcal C_y(t).
 \tag{G.10}
$$
完整误差为
$\eta_i=\|S_i^{-1}\|(\delta_i/\ell_i)
\sum_k\|[\mathcal C_y]_k\|$。
以真实 $dx=h_i\,dt$ 积分。若 $P_i=\sum_k L_kP_k(2t-1)$ 为移位
Legendre 展开，则
$$
 H_{P,i}=\int P_iP_i^*\,dx
 =h_i\sum_k\frac{L_kL_k^*}{2k+1}.
 \tag{G.11}
$$
幂到移位 Legendre 的准确系数为
$(2k+1)(n!)^2/((n-k)!(n+k+1)!)$，$0\le k\le n$。
各完整矩阵乘积内保留所有 signed entries 和 source 相关项。
由 Cauchy–Schwarz，
$$
 H_i:=\int G_iG_i^*\,dx
 \preceq H_{P,i}+
 \left(2\eta_i\sqrt{h_i\,\operatorname{tr}H_{P,i}}
       +h_i\eta_i^2\right)I.
 \tag{G.12}
$$
再选取准确对称 dyadic 矩阵中点，并将完整 matrix enclosure
误差作为额外非负对角 slack 保存，得到可直接复用的准确
Loewner 上界 $H_i^+$. 不能先把矩阵每项取 upper 再进行 signed
二次型。

输入误差 (G.8) 不混进主 cross-reference source。其独立 Gram
通道可直接使用 $\epsilon_{\mathcal B}^2 H_{E,i}^+$。
对同一个真实输入，主项与未知差项最终按合法三角上界合成，
不伪称这两个输入相互正交。

## 5. 真实输出 metric 的矩阵积分

令 $\Psi_i(t)=F_i(t)S_i$。保存两个完整输出矩阵上界：
$$
 J_{y,i}=\int\Psi_i^*\Psi_i\,dx,\qquad
 J_{h,i}\succeq\int\Psi_i^*R(x)^{-2}\Psi_i\,dx.
 \tag{G.13}
$$
将 $\Psi_i$ 的 odd 与 even 行分开作准确 Legendre 积分。
$J_{h,i}$ 使用真实闭格 $\rho_{\min}$，即
$J_{\rm odd}+\rho_{\min}^{-2}J_{\rm even}$。完整 even mean 与其
物理 Gram 保持原样。相同方法另算原固定负区上端
$2383968743003/10^{13}$ 截断的真实交段；格长只乘一次。

因此非酉 $S_i$ 与 $R$ 的 metric 全部显式存在。原物理输运的
skew-adjoint 性不能被免费搬到这些坐标，也没有据此转置帽图。

## 6. 全区间矩阵双扫的准确恒等式

以下为后继完整覆盖消费者的合同；四格 local pilot 不宣称已经
执行该全局双扫。设 cell source 积分为
$\eta_i=\int G_i(x)f(x)\,dx=(\eta_p,\eta_q)$。由 (G.3)，
$$
 \begin{aligned}
 q_i&=D_i^{-1}q_{i+1}-\eta_q,\\
 p_{i+1}&=A_i p_i+B_iD_i^{-1}q_{i+1}+A_i\eta_p .
 \end{aligned}\tag{G.14}
$$
准确消元中的 $B_i\eta_q$ 已抵消；不能重新加两次。
名义右条件为 $q_N=0$。真实帽 97 条约束尚未由此清零。
左 waist 96 条 odd 条件给
$$
 p_0=V_0q_0,\qquad
 V_0=-(\Pi_{\rm odd}Q_0)^{-1}\Pi_{\rm odd}N_0.
 \tag{G.15}
$$
如果将 $V_0$ 再选择为 dyadic proposal，则其真实左边界差也须另付。

写 $p_i=V_iq_i+w_i$，有
$$
 V_{i+1}=(A_iV_i+B_i)D_i^{-1},\qquad
 w_{i+1}=A_iw_i+A_i[I,-V_i]\eta_i.
 \tag{G.16}
$$
$q_i$ 只依当前及右侧 source，$w_i$ 只依严格左侧 source。
这两个输入支集正交，给出完整节点 Gram 递推
$$
 \begin{aligned}
 Q_i&=D_i^{-1}Q_{i+1}D_i^{-*}+(H_i)_{qq},\\
 W_{i+1}&=A_iW_iA_i^*
  +A_i[I,-V_i]H_i[I,-V_i]^*A_i^*,\\
 \Gamma_{z,i}&=
 \begin{pmatrix}
 W_i+V_iQ_iV_i^*&V_iQ_i\\ Q_iV_i^*&Q_i
 \end{pmatrix}.
 \end{aligned}\tag{G.17}
$$
$Q_N=W_0=0$。$H_i$ 的 $p/q$ 相关项与节点的 $V_iQ_i$ 全部保留。
实际计算可逐步保存准确 dyadic matrix 加非负对角 slack 的
Loewner 上界。每个局部 Loewner 不等式须完整验证；单独上舍入各
矩阵条目不能代替它。

若 (G.16) 的 $V_{i+1}$ 被独立 dyadic 舍入，则只把这些 $V_i$
作为明确的辅助 kernel 定义，记录
$$
 E_{V,i}=V_{i+1}-(A_iV_i+B_i)D_i^{-1}.
$$
相应真实 weighted-state jump 正好是
$Q_{i+1}E_{V,i}q_{i+1}$，符号为正。其完整 kernel Gram 可由
$Q_{i+1}^{\rm future}$ 消费，之后交已有真 Green 的接口源列。
不能把此跳与旧 projector 归一化跳混为一谈。

## 7. 格内相关结构与后验费用

置 $L=[V_i;I]$、$E_p=[I;0]$，
$\Pi_p^V=[I,-V_i;0,0]$、$\Pi_q^V=[0,V_i;0,I]$。
在格内 $t$，严格过去、严格未来、当前格左半 source、当前格右半
source 是四个互不相交的径向输入支集。故格内状态 Gram 为
$$
 \Psi_i(t)\left[
 E_pW_iE_p^*+L D_i^{-1}Q_{i+1}D_i^{-*}L^*
 +\Pi_p^V H_i(0,t)(\Pi_p^V)^*
 +\Pi_q^V H_i(t,1)(\Pi_q^V)^*
 \right]\Psi_i(t)^* .
 \tag{G.18}
$$
每个 partial Gram 可用完整 $H_i^+$ 上界，或在已有缓存上细分。
这可能增加上界，但不会虚构同一个 source 的独立性。
通过 $J_{h,i}$ 和真实 $dx$ 可获得全区及负区 output 核平方积分；
通过 $J_{y,i}$ 与 (G.6) 付真实 ordinary source 缺陷时，还须乘
$\max(1,\rho_{\min}^{-1})^2$。

右端仅满足名义 regular 图，其真实负荷仍为
$B_{\rm right}Q_Np_N$，包含完整 97 行与独立 mean。
用原真实帽误差与完整 even 输入 kernel Gram 支付它，不能删除
原 $D_L$ 或用 finite97 输入结论代任意未知 high 输入。

最后使用已有完整 finite193 真逆的后验恒等式 (M.13)，逐项消费：
ordinary-$L^2$ 连续缺陷、真实左边界差、真实右边界差、全部真实
接口跳及 (G.8) 的独立交叉 source 差。没有额外假定新的 Neumann
常数小于 1。任意给出的方向上界必须覆盖整个径向 $L^2$ source
空间，不能只验证有限个固定径向 load。

## 8. 本次可运行范围

本次新 public pilot 只复用四个既成方阵，新增同 $F$ patch、
完整 source Gram 和输出 metric 积分。三个实际 source 通道均保
完整 128 个输入方向。新 auxiliary $C$ 由明确准确递推定义；
旧独立 backward 多项式、原 5970 validator、原 target、原帽
residual 及已成 Green 全部不重算。所有数值门只有在公开 Actions
实际执行后才授予。

这不授 full5970 矩阵覆盖、全低高 Schur、负高 BVP、非零 $\delta$
或真正无限维 $\nu$ 响应。真实全频帽的独立 high trace 与 mean
端口始终保留。
