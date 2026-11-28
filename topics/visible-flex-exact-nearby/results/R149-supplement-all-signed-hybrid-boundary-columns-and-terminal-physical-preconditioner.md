# GBC：同一 hybrid 的全 193 个有符号边值列与真实外端有限预条件器

固定 [GG](R149-supplement-joint-Grassmann-true-low193-and-whole-source-maps.md) 的同一 selected-family、193 维变系数 hybrid、真根至 $R=25/8$、$1424$ 个原认证格。下文给独立的原边值解算子、有符号观测及 97+96 physical 门。新计算需原 GG 两个实际目标全部通过，直接使用同作业全模型，或由 [GRR](R149-supplement-whole-signed-response-graph-carrier-recovery.md) 按原 whole SHA 完整还原。没有新的实际列值或已通过的 physical 门。

**初端和末端的全部齐次解。** 将 $l=x^e(r_*)\in\mathbb R^{96}$ 保持 raw，$r=(\Theta(x^o+p_0x^e)(R),x^m(R))\in\mathbb R^{97}$，$p_0=13/80$。最后一行是 independent even mean。记 $B_a,B_b$ 为原未加权 left 和 right 算子，$T=\operatorname{diag}(\Theta^{-1},1)$。对 GG 的正交坐标图 $L_i,R_i$，其列不必各自为正交基；原图恒等式直接给出
$$
 E_0=(B_aR_0)^{-1},\quad E_{i+1}=D_iE_i,\qquad
 F_N=(B_bL_N)^{-1}T,\quad F_i=C_i F_{i+1},\qquad
 H_i=[R_iE_i,\ L_iF_i].
$$
两端矩阵逆必须有向验证。因 $B_aL_0=B_bR_N=0$ 且两个稳定传播恒等式成立，$x_i=H_i(l,r)$ 给原任意 193 个独立齐次边值的真实解。特别 $H_i$ 保留同一个 $\nu$ 列所作用的完整 left/right 相关数据。对任何两个有符号独立体源列，用它们的零边 particular $p_i$，实际 hybrid 解为 $p_i+H_i(l,r)$。此处零边仅是 exact affine 分解的常数项；完整 BVP 的 $l,r$ 仍由物理端、high、height、root 与全局方程决定。改变后的全算子还须支付它自己的体反馈。原四个 ordinary 源映射不提供这些 193 个边值列。

程序在根保存 $(\langle4j\rangle^{1/3}x^o_j,x^m,x^e)$ 的整 193×193 signed map 及原 raw root97，在末端保存 $\Theta x^e(R)$ 的 96×193 整图。在 $9/10$ 读 raw193 cut。对于 $17/20\le t\le19/20$，$Y(t)=\operatorname{diag}(K^{-1/4},K^{1/4})H(t)$。在普通 $dr$ 上分别积分 $Y^*Y$ 和 $(P_{33..96}Y)^*(P_{33..96}Y)$。两个 full Gram 都先保 joint 193×193，包括带符号的跨边界项，再就 left、right、joint 分块取 op norm 的平方根。low full 含全部 low 和 mean，shell 投影只含原 33–96 两行。整个 $K$ 区间按与该 physical box 相交的原有向 intrinsic 行取并包，包括两侧端值。

为在每个 shell 格内测量这些 **新解列**，就实际 $X=H_i$ 的物理共轭初值在 balance 坐标传播。对时长 $h$ 及含所有 $hA(t)$ 的 joint 谱球 $G$，$V_1=GX,V_k=GV_{k-1}/k$。每个球包含整盒中所有相应的有序乘积以及它们的凸组合。按时间有序单纯形的体积，端点列在 $X+\sum_{k=1}^{16}V_k$ 加一只谱球内，其半径
$$
 \|V_1\|\frac{\beta^{16}}{17!}(1-\beta/18)^{-1},\qquad \beta=\|G\|^+ .
$$
所有较早的时间只多出 $(t/h)^k\in[0,1]$ 因子；各阶另以 $V_k/2$ 为中心并付 $\|V_k\|^+/2$ 可包整个 span。用 true span 球形成 Gram，时长乘其区间包含真积分平均，全部 cut 及原整个时间窗逐格无隙。只二分实际尚未积分且分母未过的子盒；最细仍未过即原样失败。整个反向传播只在两端与 shell 起点留必要的 right basis；原 GG store 只读。新矩阵只在 fresh job-private store 保存和整件读回。随结果留下每个 observation 的 bytes/SHA、整个 write journal 和 live index，公开只含身份与小标量。

**原 97+96 真外方程的 signed 预条件。** 设已经在同一 actual [GTP](R149-supplement-Grassmann-source-maps-to-original-seven-ports.md) 的原 stage 证明 internal margin $1-\kappa_B>0$。保留 [B.18](R141-supplement-reference-boundary-lifts-and-physical-outer-block-gate.md) 原矩阵
$$
 M=\begin{pmatrix}I-U&-V\\-W&I-Z\end{pmatrix},\quad
 U=A_h T_x\mathcal P,\quad V=A_b+A_h(T_b+T_x\mathcal J_b),\quad
 W=O_b\mathcal P,\quad Z=O_b\mathcal J_b .
$$
$W_c$ 取上述新 signed outer96 的最后 97 列，准确是同一 $G_c$ 从 right97 到加权 outer96 的矩阵。由 internal 方程和 GTP 的逐接收器费用，
$\|W-W_c\|\le\kappa_O p_B$，其中 $p_B$ 为真实 internal 关闭后 right97 到 body 的已保存范数，已含全部 $\Delta A_L,C G_HB_{HL}$。这一步使用真实原体反馈与 Wc 的相同端条件，不用未经证明的两个 inverse 相减上界。

原正图 43615531666/1 的整球给 $p_-\le p_\delta\le p_+$。取一个明确 binary64 再原样视作有理的 $\hat p$，$d_p=\max_{u\in[p_-,p_+]}|u-\hat p|$。在真实加权单位令
$$
 K=\binom{(p_0-\hat p)I_{96}}0,\qquad
 M_0=\begin{pmatrix}I&-K\\-W_c&I\end{pmatrix}.
$$
$K$ 的号由 [H.16](R141-supplement-actual-GH-source-window-and-return-contract.md) 给。$M_0$ 是实际有限图给出的 signed 模型；$p_\delta-\hat p$ 的误差保留。用原 joint 定向逆得到 $M_0^{-1}$ 的四块实际范数矩阵 $P$（不要求 $I-KW_c$ 有 contraction）。H.16 中的全非均值 Robin 余项和 independent mean 一起有 $a_h$ 界，故 $M_0-M$ 的各块受
$$
 D=\begin{pmatrix}a_ht_Xp_B&d_p+a_h(1+t_b+t_Xj_B)\\
                   \kappa_O p_B& j_O\end{pmatrix}
$$
控制。$P$ 与 $D$ 均为标量比较矩阵；未假设原物理大矩阵元素正。取 $N=PD=(\begin{smallmatrix}u&v\\w&z\end{smallmatrix})$ 的真实 directed uppers。若实际 $1-u,1-z,(1-u)(1-z)-vw$ 都有严格正 lower，则 $(I-N)^{-1}P$ 逐块控制 $M^{-1}$。证明是 $M=M_0[I-M_0^{-1}(M_0-M)]$ 的分块 Neumann 级数。真实 right97 与 outer96 的两类 RHS 均经过 $P$，不漏其中一块。保留原各项 outer-high 与 body-return、height 输入和 mean 的两路。

这是独立的 signed physical gate。若实际成功可向同一真实方程交付 2×2 比较逆，其原 TP 输入输出及 future224/32 的资格应由新 provenance 明确接收；原 TP 成败历史不被改名。当前没有取得所需 GG signed $W_c$ 或该门的数值，原 finite waist/mean/height feedback、true nonlinear root、全局几何条件依旧另行成立后才可收口。公式、private 完整列、两 Gram 及 physical test 的代码在 [GBC reader](../scripts/fourfold_codazzi_grassmann_all_boundary_columns.py)。
