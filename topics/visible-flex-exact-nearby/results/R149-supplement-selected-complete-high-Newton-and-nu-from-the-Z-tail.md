# 同一 selected 成员的整域真实已知高频 Newton 与 ν 源

**已证明。** 在完整 $[0,25/8]$ 上，固定原物理 $\eta_0$、同一 $Q_\delta=Q_0+\delta Z,\nu=\nu_0+\delta$ 和实际 $\delta_*$，取 $P_H=P_{|j|\ge97}$、物理频率 $4j$。记 $f_\delta=(Q_\delta)_r-F(Q_\delta,\nu_\delta)$，$s_\delta=F_\nu+D_QF\,Z-Z_r$。下文给出普通径向测度下的界
$$
 \|P_Hs_{\delta_*}\|_{L^2_rH^{1/3}_\phi}<1.254870\,10^{-9},\qquad
 \|P_H(-f_{\delta_*})\|_{L^2_rH^{1/3}_\phi}<1.17560\,10^{-19}.     \tag{NHT.1}
$$
这两个源对应同一隐式选择和一个连续 physical proposal。只在已知源上利用有限支集；传播的未知解仍含全部高频。负区内的显式 metric 导数在 (NHT.6) 中出现。

## 原记录实际控制的正量

直接采用 [43628921664/1 的完整数学结果](R133-supplement-actual-complete-known-high-source-from-Z-tail.md) 和 [43630093667/1 的成功数学收据](R133-supplement-actual-known-high-success-receipt.md)。原前者 child 0、7721 行八门成功，外层因可选诊断过大失败；后者只核原整件。选择同一行的旧上界 $A\ge\|Q_0\|_{A^0,\rm pair}$、$A'\ge\|(Q_0)_\phi\|_{A^0,\rm pair}$、$H_0\ge\|P_{33\le|j|\le96}Z\|_{A^0,\rm pair}$、$H_1\ge\|\partial_\phi P_{33\le|j|\le96}Z\|_{A^0,\rm pair}$，包括原两列的连续修补。令 $B\ge|\beta|,k\ge\max(1,|K_0|)$ 为原行费用，其中 $K_0$ 表示 $\nu=\nu_0$ 的真实径向曲率。原逐格正预算是
$$
 T=Bk\{A^2H_1/4+3A^2H_0+AA'H_0/2\}.                      \tag{NHT.2}
$$
原摘要的 **new_tail_only_L2_radial** 直接按整行 $T$ 的平方和积分，给 $\|T\|_{L^2(0,25/8)}<1.456147\,10^{-10}$。这个字段尚未对另一个旧源候选取 min，故可在新式中逐项支配正量。另取原 **selected_known_high_H_one_third_L2_radial**，它给 $\|P_H s_0\|_{L^2_rH^{1/3}}<1.254869143346\,10^{-9}$，此时支集至 160。

原 [SC 全域 mean gap](R144-supplement-selected-metric-compact-residual-and-full-operator-fees.md) 的 raw $|m|>1.068$，整 centre repair 的 $A^0$ 费用 $<3.861\,10^{-18}$，故 $A\ge|\Pi(Q_0)_2|>1$。原 [Cδ.2](R133-supplement-selected-parameter-cap-row-transfer-with-unknown-high-input.md) 给完整 $H=19>\|Z\|_{A^0,\rm pair}, H'=83>\|Z_\phi\|_{A^0,\rm pair}$。坐标中独立 even mean 属于低头，亦属于这两个 complete state 的范数。

## 先在高投影内精确消项

记三线性函数
$$
 C_K(a,b;z)=-\beta\{I(a_1b_1+Ka_2b_2)z_\phi+(a_1b_1+Ka_2b_2)z\},
 \qquad C_v=\partial_K C_K .
$$
完整 moving 场除 $C_K(Q,Q;Q)$ 外仅有常角矩阵乘 $Q$、$\gamma mJ_KQ_\phi$ 两类项。其值、它们沿 $Q_\delta$ 的全导数以及 $(Q_\delta)_r,Z_r$ 均至 $|j|=96$。因此高投影后只余三线性项。这包括 $m,\partial_\nu m$ 本身和全部 compact metric 导数；只是角常数乘 $Z_\phi$ 或 $(Q_\delta)_\phi$ 无法产生第 97 模。原态低方程的相同项仍存在。

把 $C_K(Q_0+\delta Z,Q_0+\delta Z;Q_0+\delta Z)$ 依显式状态幂展开，记经 $P_H$ 后次数 $i$ 的系数为 $V_i(K)$，相应纯 $C_v$ 的系数为 $V_{i,v}$。因为 $Q_0$ 至 32，$V_0=V_{0,v}=0$。令 $z=P_{\le32}Z$。将某个余下 $V_i$ 中全部 $Z$ 换成 $z$，结果的高投影也严格为零。因此每个 $V_i$ 是原项与全低项的**有符号差**，逐个 $Z$ 作多线性差分，每次只插入一个 $Z-z$，其它槽取 $Z$ 或 $z$。投影在 Fourier $A^0$ 中收缩，所有列保原物理单位。

在 $K=K_0$，每个 $C$ 项由 $Bk\|a\|\|b\|(\|z_\phi\|/4+\|z\|)$ 控制，因原 $I$ 的 $A^0$ 范数为 $1/4$。对 $C_v$ 同式中的 $k$ 改为1。一次项恰有两个 $C(Q_0,Z;Q_0)$ 和一个 $C(Q_0,Q_0;Z)$。其一次 tail 差分即 (NHT.2)，所以 $\|V_{1,v}\|_2\le T/k$。对另两次幂，相同展开给如下整行上界，所列为除以 $Bk$ 后的正量表达式（即使 $B=0$ 也直接作乘法式理解）。
$$
\begin{array}{c|l}
i& \|V_i(K_0)\|_2\text{ 的 }Bk\text{ 因子以外的费用}\\ \hline
2 & HA'H_0/2+(6H+H'/2)AH_0+AHH_1/2\\
3 & (3H^2+HH'/2)H_0+H^2H_1/4 .
\end{array}
$$
二次项来自 $C(Z,Z;Q_0)+2C(Q_0,Z;Z)$，三次项来自 $C(Z,Z;Z)$。因 $A>1$，$2H<52$，$(6H+H'/2)/3<52$，$H^2<624$，$H^2+HH'/6<624$，得
$$
 \|V_2(K_0)\|_2\le52T,\quad \|V_3(K_0)\|_2\le624T,\quad
 \|V_{2,v}\|_2\le52T/k,\quad \|V_{3,v}\|_2\le624T/k.          \tag{NHT.3}
$$
以上各小球也控制逐点 angular $L^2$；源与 $V_i$ 的完整支集至 288。所有数均依赖准确原 $Q_0,Z$，未用 signed 原件中某个近零值替代未知量。

## 补上真实紧支参数

$0\le w\le1$，记 $L= T_{\rm met}w'$。原真实 intrinsic 给 $K_\delta=e^{-\delta w}(K_0+\delta L)$。在 support $[1/20,9/50]\subset[0,c]$，原 SP 的逐格曲率差正预算（$d_8=10^{-8}$）含 $d_8 e^{d_8}T_+ W_1$ 的正项，其中 $T_+\ge|T_{\rm met}|$，$W_1=2400/13\ge|w'|$。[完整 SP 实际结果](R133-supplement-actual-complete-primitive-and-mean-strict-propagation-to-the-waist.md) 的该预算最大值 $<1.048\,10^{-7}$，故 $|L|<10.48$；同时同一族包含 $\delta=0$，$|K_0|<1.03^2$。于是 $|\delta|\le d=10^{-10}$ 时
$$
 |K'_\delta|\le e^d((1+d)10.48+1.03^2)<12,\qquad
 |K_\delta-K_0|\le12|\delta|.                               \tag{NHT.4}
$$
prime 在此仅为参数导。support 外两量准确为零。$V_i$ 对 $K$ 仿射，所以二、三次项相对 (NHT.3) 可付 $1+12|\delta|$，一次项变化至多 $12|\delta|T$。特别 $V_1(K_0)=P_Hs_0$：在 $\delta=0$ 对 $V_0(K_\delta)\equiv0$ 的导数也为零。

设 $x=|\delta_*|<9.36826\,10^{-11}$。令 $D_1,D_0$ 为以下对整行 $T$ 的无量纲费用：
$$
 \begin{aligned}
 D_0&=12x^2+(1+12x)(52x^2+624x^3),\\
 D_1&=12x+(1+12x)(104x+1872x^2)+12(x+52x^2+624x^3).
 \end{aligned}                                               \tag{NHT.5}
$$
直接微分准确 signed identity $P_H(-f_\delta)=\delta V_1(K_\delta)+\delta^2 V_2(K_\delta)+\delta^3 V_3(K_\delta)$。用 $V_{i,v}$ 支配 $K'_\delta$ 的**全部**三项，得到
$$
 \|P_Hs_{\delta_*}-P_Hs_0\|_2\le D_1T,\qquad
 \|P_H(-f_{\delta_*})-\delta_*P_Hs_0\|_2\le D_0T.              \tag{NHT.6}
$$
结合 (NHT.2)、$\langle1152\rangle^{1/3}<10.484$ 和上列原 $s_0$ 强源，(NHT.1) 即得。整个改变后的误差先在真实高投影上估计，再按其自己完整 288 支集转换。此处没有对两个旧 norm 上界相减，也没有重算 7721 行。

## 与全负窗普通态的实际组合

在 [NRO](R149-supplement-ordinary-negative-response-from-the-strong-positive-root.md) 中记 $U_0=8.22,A=25.943,F=1.307204\,10^{-6},R_0=1/200$。严格段普通输入仍用完整 $F$；根段低头现在只需 $W_L=(1+384^2)^{1/6}<7.269$ 的 angular 成本，所有 $|j|\ge97$ 的原体源独立用 (NHT.1)。因此零根、零跳的已知负体源对 $[0,r_*]$ 普通 $L^2$ 实际贡献小于
$$
 \sqrt{(cU_0)^2/2+A^2R_0W_L^2}\,F
       +A\sqrt{R_0}(1.254870\,10^{-9})<1.754\,10^{-5}.             \tag{NHT.7}
$$
成立原因是原低根与完整严格源分别位于不交径向子区间。没有删去任一未知高响应。

再将已知正侧高 ordinary 源与 head-to-high、所有边界/跳及根稳定输入在强图中按线性分解。两个已知 ordinary 源列在 collar/body 上的输入平方和由 (NHT.1) 控制。实际 43617150971/1 的根补支行和 collar-sup 行，在这两个输入上的欧氏行范数均小于 $.182$。故已知 $\nu$ 高 ordinary 源对这两行各小于 $2.284\,10^{-10}$，对 (NRO.6) 的传入原根/正窄段预算总贡献小于 $5.34\,10^{-8}$；同单位 Newton 两行各小于 $2.140\,10^{-20}$。这里 true finite-root 与所有 head forcing 留在其独立的原输入，头部因高而改变的反馈亦仍须求解。对完整 $q_\nu-Z$，NRO.6 可保 $b$, 根 stable、两条完整 head-to-high 源、$B,J_c,J_s,J_u$ 和全部真实接口不动，去掉已单列的高 ordinary 源后，将已知费用 $2.523\,10^{-5}$ 更换为 $1.760\,10^{-5}$（含正窄段真实低 ordinary 费用）。本结论没有给未解端口赋值。
