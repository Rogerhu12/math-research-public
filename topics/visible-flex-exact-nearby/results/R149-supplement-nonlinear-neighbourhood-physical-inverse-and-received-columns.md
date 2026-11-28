# R149 补充：真选定邻域的完整正侧物理逆及两列受迫解

仍用 SPN 全邻域 $\|p\|_{A^3}\le\rho\le10^{-7}$、外端 $\|p(R)\|_{A^3}\le9\,10^{-10}$ 及同一独立 height 背景。这里把 WHN 的无穷维 actual strong high 图、真正 GG 的四个原图、GBC 的 signed 边界提升、WSS 的两列 signed 源放进同一个**新邻域**低/高/物理边界系统。充分门的数值由实际 GG / GBC 输入决定；原 selected TP 的结果、失败分支和所有输入资格各自保留。

## NPG.1 三种 low 接收的真实无限频差分

令 $A=7.000001,D=6.000001$，它们在整个正区支配 $Q=Q_{\delta_*}$ 的 $A^0$ 状态和角导，因为原 degree32 部分为 $7,6$、方向为 $19,83$、$|\delta_*|<10^{-10}$。写
$L(A,D)=2(A+D/4)+(5/2)(A+\rho)$。WHN.1 的五个有序词在 raw 范数仍成立。有限 low 输入 $\|x_\phi\|\le384\|x\|$，两个均值主项各在自己的槽，故

$$
 \|P_L\Delta A P_L S^{-1}\|
 \le8\rho\{6[97(2A+\rho)+L(A,D)]+14(384+1)\}<112000\rho.
$$

对任意全部 high $h$，常角 $\langle p_2\rangle Jh_\phi$ 无 low 输出，$\langle h_2\rangle=0$。把漂移差写 $a=\mathcal I(2Q^tDp+p^tDp)$（这里的矩阵为 $\operatorname{diag}(1,K)$）。$P_L(ah_\phi)=\partial_\phi P_L(ah)-P_L(a_\phi h)$，$\partial_\phi\mathcal I=P_{\ne0}$ 在 Wiener 范数收缩。第一项只支付 384，第二项的正预算是 $(2A+\rho)\rho$。所以

$$
 \|P_L\Delta A P_H\|_{L^2\to L^2}
 \le 6\rho[98(2A+\rho)+L(A,D)]<8500\rho .
$$

同一恒等式按分布成立。$A^1$ 在 $H^{-1}$ 上的乘法界由 $H^1$ 对偶给出。原有限 $Q$ 有 $A^1$ 状态/角导界 $A_1=A+D,D_1=385D$；无穷支集的 $p,p_\phi$ 在 $A^1$ 仍各至多 $\rho$。最后仅对 low 输出从 $H^{-1}$ 换普通范数，于是第三个真 fees 为

$$
 \|P_L\Delta A P_H\|_{H^{-1}\to L^2}
 \le\langle384\rangle 6\rho[98(2A_1+\rho)+L(A_1,D_1)]<8.8\,10^6\rho . \tag{NPG.1}
$$

这一步使正侧外端可同时使用真正负一窗和强窗，未截断 $p$ 或 $h$。正区 $F_\nu=0$。对原方向 $Z$ 单独用 $19,83$ 和整个长度 $\sqrt{|I|}<1.768$，故 $\|P_L(s(T)-s(Q))\|_{L^2}<15500\rho$；完整正 high 由 SPN 给 $1.254870\,10^{-9}+9\rho$。

## NPG.2 body 与两物理端口

对 $Y=B,A,O$ 分别为 $S$-body、原 raw root97、charted outer96。GG 原完整 raw、centre-high0-return、second-kind correction 的真实范数分别为 $g_Y,c_Y,d_Y$；GH5 的原小余量为 $d_C$，同 family 旧 low comparison 为 $L$。若 $t_Y=(1+d_Y)L$ 对 $B$，$t_Y=\sqrt{1+d_Y^2}L$ 对两个端点（原 TP 的完整低差分接收），则在新邻域取

$$
 h^+_Y=c_Y+g_Y(d_C+8500\rho),\qquad
 h^-_Y=\langle640\rangle c_Y+g_Y(\langle1152\rangle d_C+8.8\,10^6\rho),
$$
$$
 \kappa_Y=t_Y+112000\rho\,g_Y+30 h^+_Y .                       \tag{NPG.2}
$$

两个 $\langle\cdot\rangle$ 只来自原 center 97–160 和原 selected 差 97–288 的准确支集。原始 $v_{high}$ 从真正 $H^{-1}$ 或 raw 空间接收，$\rho$ 项无有限频假设。若全域 $\kappa_B<1$，给定 seed $z$ 的内部解有 $B'=z_B/(1-\kappa_B)$，$Y'=z_Y+\kappa_Y B'$ 对两个端点。外端未知 $a=\|y_L(R)\|_{H^{-5/6}}$ 的内部 Poisson seed 各取
$\min(h^+_Y\cdot3.656366\cdot.001\langle384\rangle,h^-_Y\cdot12.912904\cdot.001)$；
其内部闭合为 $J_Y$。high even 直接外读数也取两个原窗真界之小者。右自由 datum 的同一内部提升为 $P_Y$，其初始 $S$-body 图是 $(1+d_B)D_B$，其两个端点直接由 GBC 的 signed 97 列给出。左侧是独立 96 列，未与 attached mean 合并。

QN.36–40 给 $E<.000283,\mu<.000219$。新 $p_T$ 的真实区间取原 $p_Q$ 区间两端分别除以 $1+\varepsilon/5.84$ 和 $1-\varepsilon/5.84$，$\varepsilon=\min(\rho,9\,10^{-10})$，逐件验证仍在 $(1/8,1/5)$。设 $a_h=(E^2+\mu^2)^{1/2}$ 的上述有向上界，$a_b=((3/80+E)^2+\mu^2)^{1/2}$ 的上界，$t_x=.154$ 为 WHN 完整 head-to-outer 真高行。两物理未知 $r,a$ 分别在原 charted-right97、charted-outer96 的单位中。operator 分块的正界为

$$
 \mathcal K=\begin{pmatrix}
 a_h t_x P_B & a_b+a_h(t_b+t_x J_B)\\
 P_O & J_O
 \end{pmatrix}.
$$

若两对角余量和行列式均正，两物理端口有真逆。否则 GBC 真 signed $W_c$ 给 $M_0=(I,-K;-W_c,I)$，$K=((13/80-\widehat p)I;0)$，$\widehat p$ 是上面真实区间中的 dyadic 中心。完整 $193\times193$ 实 directed 逆的 $2\times2$ 分块范数再乘残差

$$
 \begin{pmatrix}
 a_h t_x P_B&\sup|p_T-\widehat p|+a_h(1+t_b+t_x J_B)\\
 \kappa_O P_B & J_O
 \end{pmatrix}.
$$

重新验证这个真正物理算子的两余量及行列式。取出的最终 $2\times2$ 逆同时乘原右数据两项。两个充分门都未通过时保留真实结果。

## NPG.3 signed RHS、所有可移动界面、实际负窗

SAR 先给原 $z_i^0=G_c\pi_L f_i(Q)$ 的两列 signed 解。各 receiver 还可用其上界与同一旧 low 源全 ordinary 上界乘 GG 原 raw 图取小。新 $T$ 的完整两个 $A(T)$ 图和 QN 强外行给独立 $v_i(T)$、$d_i(T)$，其中 mean 是真实 attached row。原 WSS 的低 particular 保持原符号；其余已知和自由源在右端分开付。$\nu$ 低差由 NPG.1、高差及两外 residual 由 SPN 支付。Newton 在 $p=0$ 使用 OHR 的 high/Robin 与原 OA 的真实独立 mean；若 $p\ne0$，需收到实际 Newton 相对原 low 的 residual 差、完整 high ordinary 和两项真实外 residual。$\|p\|_{A^3}$ 独自不支配 $p_r$。

完整输入还包括 stable root、分开的两段 $H^{1/3}$ ordinary、其余两窗及两 cut jump、实际外 height、额外 Robin/mean、根左 96 与独立右 97。所有低点源也可收。确实，在任意严格内部的物理跳 $j$ 取一侧宽 $h=1/40000$ 的线性三角提升，方向选使整个支撑在 $I$ 内。低 raw 跳正好为 $j$，边界值为零，全 $S$-body 至多 $(\sup\|S\|)\sqrt{h/3}|j|$；原 ordinary 余力至多 $(h^{-1/2}+70000\sqrt{h/3})|j|$。在完整真状态 $T=Q_0+\delta_* Z+p$ 及其角导上，$7+19\,10^{-10}+10^{-7}<A_t=7.000002$，$6+83\,10^{-10}+10^{-7}<D_t=6.000002$。把这两个界代入 PA.4 的整张主部与零阶 DG 式，使用原整区 $b_K<6,g_K<14$ 和真实低角导 384，得到
$384(6 A_t^2/4+14A_t)+6(1+3 A_t^2+A_t D_t/2)+14 D_t<70000$。该界 含真实 scalar drift、旋转 principal、local reaction、primitive 与 mean rank。各跳按自身原始坐标，端点跳由对应的端口接收。

已知 seed 内部关闭为 $B_0,O_0$ 等后，剩下两条物理右数据为 $a_h t_xB_0,O_0$ 的上界；直接由独立 high/height/Robin/mean 引入的非齐次 $d_i(T)$ 此前已在 seed 中进入一次。用证明过的物理逆同时解出 $r,a$。真 $S$-body 为 $B_0+P_Br+J_Ba$ 的上界；true mixed 193 根同时可用 SAR 原 signed mixed 列或“raw97 加独立 even96”的正交界。强 outgoing 与 collar 再加 WHN 的 $11.9B$ 和物理外 head 项。由此真 $b,B,a$ 可直接代入 WHN.3。若还有负体源，严格段 ordinary $L^2$ 与根段 $L^2H^{1/3}$ 各以 2 倍保守接收，因为 $8.22001\,c<2$、$25.944/\sqrt{200}<2$；正窄段的额外低普通源另加 $1.005(9\,10^{-13})\|g\|$。各处真跳另按 WHN.3，不省略 collar 或两端原子。

[完整计算入口](../scripts/fourfold_codazzi_nearby_physical_received_response.py) 使已有真实 private 模型可依序试两个新充分门。收到同一个真实全局解的全部输入后才可对它检验 $.005$，并保每个独立实际 datum。此处未取得该全局解、实际门值或非线性几何族。
