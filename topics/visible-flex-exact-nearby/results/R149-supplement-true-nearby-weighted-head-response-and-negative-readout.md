# R149 补充：真邻域中的 weighted head 响应与全负窗读出

在 [SPN](R149-supplement-true-positive-seven-port-graph-around-the-selected-member.md) 的同一非线性邻域 $T=Q_{\delta_*}+p$ 上，令 $x=P_L(q_\nu-Z)$，$B=\|Sx\|_{L^2(I)}$，其中 $I=[r_*,25/8]$，每个真子格仍用原 $S_m$。令 $b=\|P_L(q_\nu-Z)(r_*^+)\|_{H^{1/3}\oplus L^2}$，$a=\|y_L(25/8)\|_{H^{-5/6}}$ 是外端 96 个非均值 even 坐标，$F_B=\||D_\theta|^2\dot f_B\|_{H^{1/6}}$ 为实际独立外 height 方向。真 high 解中单由 $x$ 的体耦合驱动的整段普通 $L^2$ 范数小于 $30 B$，其 root-outgoing、collar 与 body 三个 $Z$-sup 均小于 $11.9 B$，真实外端 high-even $H^{-5/6}$ 小于 $.154 B$。这是围绕实际选定成员、对无穷角支集扰动的整图。

## WHN.1 原始物理 low193 到完整 $H^{1/3}$ 高体源

写 $\mathcal W=A^{1/3}$，其权 $(1+|m|)^{1/3}$ 在 $H^{1/3}$ 上是乘子权，因为 $\langle n+m\rangle\le(1+|m|)\langle n\rangle$。对成对的场用系数向量模或分量和；因而实 Euclidean 输入的乘积估计不需改用独立两个头部的和。$W_{96}=\langle384\rangle^{1/3}<7.269$。沿 $I$ 有 $\|Q\|_\mathcal W\le A=33,\|Q_\phi\|_\mathcal W\le D=28$，$p,p_\phi$ 两范数均不超过 $\rho$。原 intrinsic 的 $b_K<6,g_K<14$ 覆盖整段。[SPN 的原 WLA/cap 接合和 NBE 状态界](R149-supplement-true-positive-seven-port-graph-around-the-selected-member.md)

用 SPN 的三线性式 $C(u,v;h)$。$P_H(A(T)-A(Q))x$ 的三线性部分恰为 $2C(Q,p;x)+C(p,p;x)+2C(p,x;Q)+2C(Q,x;p)+2C(p,x;p)$ 的高投影。$\gamma\langle p_2\rangle Jx_\phi$ 仍是低态，另一均值项 $\gamma\langle x_2\rangle Jp_\phi$ 付原 $g_K$，保留独立 even mean。第一对词的末槽给 $1+384/4$。其它三个词分别给 $2(A+D/4),2A(1+1/4),2\rho(1+1/4)$。原 WVC 全权的 $q_m\ge1/8$，$\|S_m^{-1}\|\le8$。逐径向点有

$$
 \|P_H(A(T)-A(Q))x\|_{H^{1/3}}
 \le8\rho\left[6W_{96}\left((2A+\rho)97+2(A+D/4)+\tfrac52 A+\tfrac52\rho\right)+14\right]\|S_mx\|_2
 <2.3\,10^6\rho\|S_mx\|_2 .                                      \tag{WHN.1}
$$

在平均泛函上用 $|\langle x_2\rangle|\le\|x\|_2$，故最后的 14 没有 $W_{96}$。$6W_{96}$ 只换有限输入的范数；高输出含全部频率。

## WHN.2 保留逐径向的原 functional

真实原加权积分 run 44746534556/1 在 4650 原闭行与 154 个 body 源段的 4802 个公共格上，已给未扰 functional $W_o<8.130665$。其每一个分支为 $K_{2g}(f^2c^2)$ 的上确界再开方，$c$ 是该段原 full-family $P_H A(Q)P_L S_m^{-1}$ 的正预算，$f$ 是相同 original frame；两个方向的输入半区在每个接收点不交，分支输出正交。$c$ 不依赖采用哪组光学帧。SPN 给出新阻尼 $g'\ge(1-\sigma)g$、新源框 $f'\le(1-\tau)^{-1/2} f$，$\tau=10^{-7}$、$\sigma=2\,10^{-7}$。对任意非负源 $F=f^2c^2$ 的两条 scalar 正核，PH.13 的 $\|K_{2g}2g\|_{\infty\to\infty}\le1$ 直接给

$$
 \sup K_{2g'}((f')^2c^2)
 \le {\sup K_{2g}(f^2c^2)\over(1-\tau)(1-2\sigma)} .
$$

逐分支其实只需 $1-\sigma$，采用上式也涵盖联合上确界的较宽比较。每个原 $c$ 均留在其原积分中。扰动部分另外用 (WHN.1) 与真正 QN.42 的 ordinary body 费用 $.126142$。原 GH5 两个 collar 源费及上式给新 $C_c<9.76$，$W<8.161$。令 $x_c,x_b$ 是 $Sx$ 在 collar/body 上的不交 $L^2$ 输入，$x_c^2+x_b^2=B^2$。在 QN.43 令 $z=.009C_c x_c$、$w=W x_b$，$q_c=750/749,r_c=1/749,q_b=100/69,r_b=31/69$，$\Sigma=(1-r_c r_b)^{-1}$。仅这个线性分量的独立边界/jump 输入为零，于是

$$
 X=\Sigma(q_c z+r_c q_b w),\qquad Y=r_bX+q_bw,\qquad
 U_a=S_c=q_c(Y+z),\qquad S_b=q_b(X+w).
$$

每行的两系数作 Euclidean 合成。两行均小于 $11.9B$。原态用 $\sqrt{9h S_c^2+2.518^2 S_b^2}$、$h\le9\,10^{-6}$；真实外端 high trace 用 $5S_b/388$。此处变化的是 $B_{HL}$ 和整个 high 逆，两者均已支付。在确切 $p=0$ 时直接保留原 $U_a=S_c\le11.693139B$ 的已成更紧行。

## WHN.3 全负窗的实际有限接收坐标

令 $p_e=(s,f_c,f_b,j_B,j_c,j_s,j_u)$ 保留强七端口中其余独立输入。$f_c,f_b$ 排除已列出的原已知普通源、(WHN.1) 的完整 head 路径；$j_B$ 含剩余 body jump 与额外 Robin/独立 physical mean。在真邻域中该项可取 $j_{B,\rm jump}+23\|r_{\rm extra}\|_{H^{1/6}}+28|m_{\rm extra}|$。$s$ 为真实根 stable；两个 cut jumps 以及 collar jump 分别保留。把 $p_e$ 代入 QN.43 的 $U_a,S_c$，记输出 $U_e,V_e$。定义

$$
 \mathcal E_T=25.95(9.00002)(s+U_e)+2.86\,10^{-6}V_e+
   25.944J_r+3.973J_s^{\rm raw}+9.54\,10^{-7}J_p .
$$

$J_r,J_s^{\rm raw},J_p$ 是 SPN 原三个普通/混合空间的负窗和窄段低跳。强边界真实输入 $\|y_L\|_{H^{1/6}}\le\langle384\rangle a$，此有限的转换只用于真正外 head 96；$\Theta$ 度量、独立 mean 及全部未知高态不截断。QN.39 的 $.001\langle384\rangle a+.004F_B$ 在纯 $B$ 输入的完整 strong root/collar 两行均乘至多 $1.453$。在 (SPN.1) 中分出 (WHN.2)、实际 $a,F_B$ 并用范数三角，给

$$
 \boxed{\|q_\nu(T)-Z\|_{L^2([0,r_+];L^2_\phi)}
 \le25.95 b+2780B+131a+1.36F_B+\mathcal E_T+1.774\,10^{-5}+5530\rho.}       \tag{WHN.3}
$$

所有测量用同一真实响应。例如 $b\le2\,10^{-5},B\le1.2\,10^{-6},a\le4\,10^{-6}$ 且 $F_B,\mathcal E_T=0$ 时，全邻域均达到 $.005$；这列明数值阈值需要的全部端口条件。固定选定 $p=0$ 的版本保 [OHR](R149-supplement-strong-physical-outer-residuals-and-complete-independent-right-hand-sides.md) 已算独立源 $1.769\,10^{-5}$、原真实两行 $U_e,V_e$ 与 NRO 原跳费用。真外低-to-high、独立 height 的 $H^{1/6}$ 输入系数充分采用 run 43615531666/1 的 $2.340052\,10^{-5},2.832692\,10^{-5}$。此时 $(2780,131,1.36)$ 对应可换成 $(2732,3.03,.0096)$。式中 $b,B,a,F_B$ 的实际物理匹配、额外端口的真实数值及非线性背景的存在仍由原方程决定。

[有理组合与整件准入](../scripts/fourfold_codazzi_true_nearby_weighted_head_saved_bounds.py) 直接读取原 GH5、weighted、WVC、strong 外端以及证明合同，不重做原积分、原 source fee 或 Riccati sweep。
