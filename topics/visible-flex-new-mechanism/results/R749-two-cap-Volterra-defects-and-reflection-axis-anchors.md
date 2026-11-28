# R749　两端径向发展、两条真实反射轴和整带三项 Gram 的连续界

本条消费 [R748](R748-single-height-periodic-development-and-complete-two-cap-geometry.md) 的同一个材料高度 $u$ 和固定 $g=E(r)dr^2+r^2d\varphi^2$。$a=.075,\ b=.22,\ \sin\vartheta=.27,\ \cos\vartheta>0$。假设全周材料角 $\varphi$ 上的 $u$ 周期并对 $0$ 偶对称，$s^2=1-u_r^2/E-u_\varphi^2/r^2>0$。初始外帽和目标内帽的真姿、中心 $(C_x,0,C_z)$ 及同一 $E$ 都固定。下文的导数按 R748 的角向与径向正则假设，跨真实结有相应共同迹。若有可数胞积聚于帽，须给 $W,H$ 的绝对连续延拓、实际端迹和下述全尾可积界，或以有限截面真迹收敛及可积余量推出这些条件。

## 两个方向各自的真实 Volterra 核

记 $A=\sqrt{E-u_r^2}$，$Z_o=(c+id)e^{i\beta_o}$，其中 $c=-u_ru_\varphi/A,\ d=r\sqrt E\,s/A$。R748 的 $B=\beta_r,\ G=(d_r+cB)/A,\ W_o=(\beta_o)_\varphi-G,\ H_o=(U_o)_\varphi-Z_o$ 满足

$$
 (W_o)_r=-\mathcal D/(r\sqrt E\,s^3),\qquad
 (H_o)_r=i A e^{i\beta_o}W_o .
$$

内帽的真实水平点和单位径向为 $P_a,T_a$。以复乘 $R=T_a e^{-i\beta_o(a)}$ 和 $U_i=P_a+R[U_o-U_o(a)]$ 取内支。任一局部角提升满足 $\beta_i=\beta_o+\arg R$。因此

$$
 \partial_\varphi\arg R=W_i(a)-W_o(a),\qquad
 W_i(r)-W_o(r)=W_i(a)-W_o(a).
$$

$R$ 和全部水平位置在全圈单值，角提升只用于求导。两组真实微分式皆成立，内支的 $H_i$ 使用 $Z_i=RZ_o$。$u$ 的两端平帽迹与 $E(a)=E(b)=1,\ E'(a)=E'(b)=0$ 准确时，$W_i(a),H_i(a),W_o(b),H_o(b)$ 均为零。

令 $Q\ge|\mathcal D|/(r\sqrt E\,s^3)$，$A_*\ge A$，$\ell(x,y)=\int_x^y A_*(t)\,dt$。每个角标均可先独立积分，取全角共同上界也成立。以 $w_b,h_b,w_a,h_a$ 分别界外、内起点 $|W_o(b)|,|H_o(b)|,|W_i(a)|,|H_i(a)|$，则

$$
\begin{aligned}
 w_o(r)&=w_b+\int_r^b Q,&
 h_o(r)&=h_b+\ell(r,b)w_b+\int_r^b\ell(r,t)Q(t)\,dt,\\
 w_i(r)&=w_a+\int_a^r Q,&
 h_i(r)&=h_a+\ell(a,r)w_a+\int_a^r\ell(t,r)Q(t)\,dt .
\end{aligned}
$$

这些函数分别界两支真实 $|W|,|H|$。单侧三维理想归一微分的两列正交，把实际水平第二列的 $H/r$ 加入后，相对 Gram 算子误差至多 $2h/r+(h/r)^2$。

## 角错、两轴与真实水平平移

轴 $\varphi=0,\pi$ 上 $u_\varphi=B=0$，$\beta_o$ 分别恒为 $0,\pi$。两处 $T_a$ 正好等于原单位径向，故 $R=1$。令

$$
 L_\pm=\int_a^b A(r,0\ \text{或}\ \pi)\,dr,\quad
 J=P_a-U_o(a),\quad
 J_+=C_x+L_+-(b-a\cos\vartheta),\quad
 J_-=C_x+(b-a\cos\vartheta)-L_- .
$$

$J_\pm$ 是同一实际内圈的两端锚偏，每个均实。R748 的轴和、中心偏差分别为 $J_+-J_-$ 与 $(J_++J_-)/2$。令 $j=\max(|J_+|,|J_-|)$，$\omega=w_i(a)+w_o(a)$，$\nu=h_i(a)+h_o(a)$。到最近反射轴的真角距为 $t\le\pi/2$。因为 $J_\varphi=(R-1)Z_o(a)+H_i(a)-H_o(a)$，且 $|Z_o(a)|\le a$，直接沿此段积分得

$$
 |R-1|\le m(t)=\min(2,t\omega),\quad
 |J|\le j+t\nu+a\min(2t,t^2\omega/2),\quad
 |V|\le j+t\nu+a\min(2t,t^2\omega/2)+m(t)\ell(a,r)
$$

其中 $V=U_i-U_o=J+(R-1)(U_o(r)-U_o(a))$。另有真实全胞的 $|V|$ 或 $|R-1|$ 更小界时可取交。仅给 $\mathcal D=0$ 而两轴有水平平移偏差，仍会在拼合窗出现 $\chi'V$。

## 实际混合后每项 Gram

以实际固定 $\chi=1-S((r-.105)/.07)$，$S(x)=10x^3-15x^4+6x^5$，在 $[0,1]$ 外作常值延拓。从 $F=(\Re(U_o+\chi V),\Im(U_o+\chi V),u)$ 直接求导。置 $L=1-\chi+\chi R$，则

$$
 (U_o+\chi V)_r=L A e^{i\beta_o}+\chi'V,\qquad
 (U_o+\chi V)_\varphi=L Z_o+(1-\chi)H_o+\chi H_i.
$$

角依赖 $R_\varphi$ 已进入真实 $H_i$。令 $Q_h$ 为理想三维正交归一微分的水平两行，$z=(u_r/\sqrt E,u_\varphi/r)$，则 $Q_h^TQ_h=I-zz^T$。只将水平行乘 $L$ 时，Gram 变化恰为 $-qQ_h^TQ_h$，$q=\chi(1-\chi)|R-1|^2\le1$。余下两列范数界

$$
 e_r=|\chi'||V|/\sqrt E,\qquad
 e_\varphi=((1-\chi)h_o+\chi h_i)/r,\qquad e=\sqrt{e_r^2+e_\varphi^2}.
$$

实物的归一径、混、角三项绝对缺陷上界依次为
$q+2e_r+e_r^2,\ q/2+e_r+e_\varphi+e_re_\varphi,\ q+2e_\varphi+e_\varphi^2$，因为 $|z_rz_\varphi|\le1/2$（此处两下标表示向量 $z$ 的两个分量）。由最小和最大奇异值的扰动界，整张的相对度量算子范数可逐胞用更强的

$$
 \eta\le\max\left(2e+e^2,\ 1-\max(0,\sqrt{1-q}-e)^2\right).
$$

若某个实际 $C^2$ 代表与此数学径积分发展的归一微分两列还有已验证一致误差，就分别加进 $e_r,e_\varphi$。未经验证的 Gauss 节点、不同精化间的最大差和单次 ODE 运行不能提供这个量。

例如 R738 真实源有 $A_*\le1.69,\ E\ge1$。若两帽六迹准确、$s\ge\sigma>0$ 遍及全段，记 $d_*=\sup|\mathcal D|/\sigma^3$，则 $\omega<1.934d_*$（零残差时取等于零），$h_o(a)\le.237d_*$，两侧 $h/r\le3.16d_*$。真实过渡 $r\le.175$，因此 $|V|\le j+1.07d_*$，$q\le2.32d_*^2$，且 $|\chi'|\le1.875/.07$。这些是同一实际源上的粗全段预算；下面的单胞 $L^1$ 核允许首尾有不同尺度。

## 两帽六迹与实数误差

在任一端圈以 $T_*$ 表示真实平帽水平单位径向，$A_*=|P_r^*|$ 在本段专指该帽的水平径速。由构造，$U=P^*,\ U_r=A T_*$。相对给定帽的水平六迹差在缩放前逐项是

$$
 0,\quad(A-A_*)T_*,\quad0,\quad
 (A_r+iAB)T_*,\quad ((A-A_*)T_*)_\varphi,\quad0 .
$$

对应垂直项为 $\Delta u,\Delta u_r,\Delta u_\varphi,\Delta u_{rr},\Delta u_{r\varphi},\Delta u_{\varphi\varphi}$。真实端圈 $|T_{*,\varphi}|\le1/\cos\vartheta_*$；外帽取 $\vartheta_*=0$。将六向依次按 $1,1,r^{-1},1,r^{-1},r^{-2}$ 缩放得 R748 同一物理比较。若所有高度端迹精确，则 $A=A_*$、$A_r=B=0$，两组三维六迹确实一致。积分 $H,W$ 的半正余量不能修补非零接缝；正的六迹上界仅记录有界误差，不能单独证明闭壳在缝上属于 $C^2$。

当端迹仅有绝对误差时，程序也从这**同一组**数据支付 $h_a,w_a,h_b,w_b$。具体设 $p=u_r,\ v=u_\varphi,\ c_0=\cos\vartheta_*$。真端帽有 $s_*=c_0,\ u_{r\varphi}^*=v_*/r$，$|p_*|\le\sin\vartheta_*$。使用 $A\ge s>0$ 及
$$
 A_r=-pu_{rr}/A,\quad B=-v u_{rr}/(A^2rs),\quad
 ss_r=-pu_{rr}-v(u_{r\varphi}-v/r)/r^2 .
$$
则 $|H|$ 由 $|-pv/A+p_*v_*/A_*|$ 与 $r|s/A-c_0/A_*|$ 的平方和开根界出，$|W|$ 由 $|G-c_0/A_*^2|$ 界出，$G=(d_r+cB)/A$。另可采用已有的同端严格较小界。二阶误差只在有相应全点包围时支付，度量界本身不控制主曲率或 reach。

## 向外舍入接口

[双端传播程序](../scripts/r749_two_cap_volterra_bound.py) 复用 R734 的 84 位向外区间。输入包含完整材料端点 $.075,.22$、严格分开的径区间端点、各胞的 $A$ 上界、$E,s$ 正下界，以及同一场 $\mathcal D$ 的全点绝对上界或 $Q$ 的连续积分上界。若胞宽 $l$、质量 $m=\int Q$、左右一阶矩 $m_L=\int(t-r_L)Q,\ m_R=\int(r_R-t)Q$，从各自近端更新
$$
 (W_*,H_*)\longmapsto
 (W_*+m,\ H_*+A_*(lW_*+m_L\ {\rm 或}\ m_R)).
$$
缺少加权矩时用 $lm$，若有 $Q\le Q_*$ 还可用 $l^2Q_*/2$。允许一个已包围的胞覆盖整条可数真尾。左右各扫一遍，保存每一胞的两侧 $W,H$、三 Gram 及 $\eta$，另报两个真实锚点和两帽各六迹。命令行输入 JSON 使用原生十进制字符串或两端点字符串数组，明确关联连续证据的 SHA-256；可校验所附证据文件的实际字节。该关联本身不验证外部证明。若声明一份经验证的 $C^2$ 实现，还须提供各胞的两列实现余量和两帽各六项实现余量。没有这种输入时，只处理数学上的真实径向发展。调用键为 `edges,cells,boundary,proof_sha256`，可传 `eta_target`。每胞必传 `A_upper,E_lower,normal_s_lower` 和 `D_absolute_upper` 或 `Q_L1_upper`，可传 `Q_left_first_moment_upper,Q_right_first_moment_upper`。边界传 `C_x,L_plus,L_minus` 的真实区间和 `inner_height_errors,outer_height_errors`，每组包含 `u,u_r,u_phi,u_rr,u_rphi,u_phiphi` 的全圈绝对误差上界。取 `representation=validated_C2_representative` 时另传每胞 `relative_implementation_r_upper,relative_implementation_phi_upper` 和边界 `inner_implementation_six_upper,outer_implementation_six_upper`。完整输出可指定 `--output` 留给下游，标准输出记录输入、结果文件散列与总门。当前尚无本条对 R738 或 R745 的全域数值资格。
