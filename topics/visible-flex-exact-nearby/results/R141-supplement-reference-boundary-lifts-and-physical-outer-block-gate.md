# R141 补篇：原参考边界 lift 与真正物理外行的二块门

2026-11-20，visible-exact-astra-ac637-20261120 / positive_inverse。

本篇落实两个独立对象。第一部分给同一个 WVC 参考 $D$ 的完整右97和联合193边界 lift，其十个新标量可立即公共计算，不依赖尚在运行的 R141 有向低逆。第二部分给未来已成低逆和真实 $G_H$ 的消费公式，保留 root97、outer96和全部193观察，并把真正 physical 外行化为一个具体 $2\times2$ 正矩阵判据。数值门未过前不宣称实际内部逆或物理外边界逆。

## B1. 准确输入、边界和输出

沿用 [R141](R141-low193-directed-green-and-complete-observation-certification.md) (G.1)–(G.5) 的 normalized real坐标与 ordinary $dr$。低状态次序为 odd1..96、原 moving-even mean、even1..96。原参考边界是

\[
B_ax=x^e(a),\qquad B_Rx=(x^o(R)+p_0x^e(R),x^m(R)),\qquad p_0=13/80.
\tag{B.1}
\]

$S=\operatorname{diag}(I,q,qI)$ 与原153个 exact reference choices相同。令

\[
\Theta=\operatorname{diag}_{1\le j\le96}(1+16j^2)^{-5/12}.
\]

本次的两个输入空间是：右输入
$r=(\Theta\lambda,\mu)\in\mathbb R^{96}\oplus\mathbb R$，其中 $\lambda=x^o(R)+p_0x^e(R)$、$\mu=x^m(R)$；以及联合输入 $(l,r)\in\mathbb R^{96}\oplus\mathbb R^{97}$，其中 $l=x^e(a)$ 使用原 raw root单位。联合 norm 是这两个独立输入块的 Euclidean直和。

两者均输出

\[
\mathcal Ox=(Sx,R_ax(a),\Theta R_bx(R))
\in\mathscr X\oplus\mathbb R^{97}\oplus\mathbb R^{96},
\quad\mathscr X=L^2(I;\mathbb R^{193}).
\tag{B.2}
\]

root97为odd96加mean，outer96为even非均值。此处的 moving-even mean不是另外的physical density-mean行。输出评价只对真实齐次ODE解进行，不从任意 $L^2$ 函数读端点。

## B2. 原参考的两个精确齐次列

在模式 $j>0$，原 $D$ 的 raw $2\times2$ 生成器为

\[
D_j=\begin{pmatrix}a_j&c_jq^2\\c_j&-a_j\end{pmatrix},\qquad c_j=4j|\eta_D|.
\]

原 signed reference模块已定义同一个连续 raw状态的 $p_j,g_j,H_j,K_j$：
$g_j(a)=1$，$H_j(a)=0$，$p_j(R)=p_0$，$K_j=1-p_jH_j$。记

\[
d_j(r)=\exp\!\left(-\int_r^R(a_j+c_jp_j)\,ds\right)=g_j(R)/g_j(r).
\tag{B.3}
\]

实现用 `profiles.to_right(j,box)` 的有序衰减公式，不除以很小的全程 $g_j(r)$。原所有reference seam都保持raw identity transmission。

两个 raw解为

\[
X_{l,j}(r)=g_j(r)\binom{-p_j(r)}1\,l_j,
\quad
X_{r,j}(r)=d_j(r)\binom{K_j(r)}{H_j(r)}\,\theta_j^{-1}r_j.
\tag{B.4}
\]

第一列在root的even等于 $l_j$，在outer的Robin为零；第二列在root的even为零，在outer的Robin为 $\theta_j^{-1}r_j$。直接利用原 Riccati关系
$g'=-(a+cp)g$、$H'=c-2(a+cp)H$ 可验两列均解 $x'=D_jx$。在右端 $K+p_0H=1$ 保证准确Robin，未替换成浮点 $p_0$。

mean分量是 $x^m(r)=\mu$。其body观察为 $q(r)\mu$，root mean为 $\mu$，outer96中没有另添mean槽。因此独立mean贡献的平方Gram准确为
$\int_Iq^2dr$（body）、$1$（root和atoms）、$0$（outer96）、$\int_Iq^2dr+1$（complete）。

## B3. 完整 Gram 与十个新标量

对同一模式的两个输入列，写

\[
W_j(r)=
\begin{pmatrix}
-p_jg_j&d_jK_j\theta_j^{-1}\\
qg_j&qd_jH_j\theta_j^{-1}
\end{pmatrix},
\quad
A_j=
\begin{pmatrix}
-p_j(a)&g_j(R)\theta_j^{-1}\\
\theta_jg_j(R)&H_j(R)
\end{pmatrix}.
\tag{B.5}
\]

body、atoms、complete的模式Gram分别为

\[
G_{B,j}=\int_IW_j^TW_j\,dr,\quad
G_{A,j}=A_j^TA_j,\quad G_{Z,j}=G_{B,j}+G_{A,j}.
\tag{B.6}
\]

root或outer的Gram取 $A_j$ 的相应单行。**同一角模式的两个边界输入列在输出上不正交。** 实现先形成并积分完整signed交叉项，最后才取其绝对值。不同角模式以及独立mean则在所有输出槽正交，因此联合193输入的operator norm是各 $2\times2$ Gram最大特征值与独立mean项的最大值再开方。

右97输入单独的五个norm取各Gram的右下项，以及相应mean项。它们通常比联合输入界小，必须分别保留。

若 $\begin{psmallmatrix}a&b\\b&d\end{psmallmatrix}$ 是某个被包围的PSD Gram，令 $\bar a,\bar d$ 为非负有向upper，$\bar b\ge|b|$，则可用

\[
\lambda_{\max}\le
\frac{\bar a+\bar d+\sqrt{(\bar a-\bar d)^2+4\bar b^2}}2.
\tag{B.7}
\]

这来自逐项绝对值支配与非负对称 $2\times2$ 矩阵的Perron根，不要求把interval Gram当成精确矩阵求逆。

新纯模块 `fourfold_codazzi_reference_boundary_lift_math.py` 重新识别原153 definition chain与selected diagonal chain，使用原155 comparison cover。它只准备low1..96参考剖面；不构造 actual centre/family packets、高参考、Green核或旧norm目标。每原panel/mode分成16个精确归一化子格，在每个whole box包围 (B.5)，乘 **真实 $dr$ 长度** 后累加 (B.6)。首格左端仍是真root；切格不把root替换为中点。

计算保留96组三个signed Gram累积标量、原reference节点剖面及一个panel的whole-box缓存。每panel后清缓存，不保全历次大矩阵。总共 $155\cdot96\cdot16$ 个完整profile boxes；没有 $193\times193$ transfer/QR/Gram传播。

两个新目标分别保存以下五项：body、root97、outer96、完整atoms193、complete。字段前缀分别是 `reference_weighted_right97_` 与 `reference_joint193_boundary_`，共十个whole scalar records。全部75位保存球读回并检查包含原directed upper；后继只用读回upper。该计算只证明同一个 $D$ 的lift，不证明actual低逆或physical外边界。

## B4. 消费未来 R141 的已成分块观察

R141的每个 source comparison 及完整actual coefficient defect均保存
`body_norm_upper`、`root97_HS2_upper`、`outer96_HS2_upper`和完整193atoms norm。假如它实际完成7目标并通过严格body defect门，令 $b_W$ 为该source已保存的actual body upper，$e_R^2,e_O^2$为defect的两项HS平方界。则新增分块消费为

\[
g_{W,R}=\sqrt{G_{W,R}^2}+\sqrt{e_R^2}\,b_W,
\quad
g_{W,O}=\sqrt{G_{W,O}^2}+\sqrt{e_O^2}\,b_W.
\tag{B.8}
\]

这是R141 (G.29) 的同一实际解resolvent identity在两种真实端点receiver上的投影。不重新计算任何Green，亦不从body norm取trace。完整joint atom upper $g_{W,A}$ 仍直接读取原actual结果，不用较粗的两分块平方和覆盖它。

对 `low_second_kind_correction`，记相应界为 $c_B,c_R,c_O,c_A$，并记 $T_L=I+\mathcal OG_L(A_L^c-D)S^{-1}\operatorname{pr}_B$。若 (B.3)–(B.7) 给某一完整边界输入族的reference界 $d_B,d_R,d_O,d_A$，则其真正低解为

\[
\mathcal OX_L=T_L\mathcal OX_D,
\tag{B.9}
\]

因而可取

\[
l_B=(1+c_B)d_B,\quad l_R=d_R+c_Rd_B,\quad
l_O=d_O+c_Od_B,\quad l_A=d_A+c_Ad_B.
\tag{B.10}
\]

两种输入族分别转授。$T_L-I$ 只读取body槽而输出全部193原子，因此 (B.9)没有隐含原子输入回路或任意trace。

## B5. 内部实际反馈的三个receiver

沿用真实高源合同 (H.6)–(H.11)。已成完整连续 $L_0$ 来自原联合body+193atom kernel majorant；对两分块也有

\[
\ell_R=\sqrt{1+c_R^2}L_0,\quad
\ell_O=\sqrt{1+c_O^2}L_0,
\quad \ell_A=\sqrt{1+c_A^2}L_0,\quad
\ell_B=(1+c_B)L_0.
\tag{B.11}
\]

这里对完整 $\mathcal OG_D\Delta A_LS^{-1}$ 使用 row norm $(c_R,1,0)$ 等，保其共同输入；不是将两个各自 $L_0$ 的输出错误地声称正交独立。

对 $J=B,R,O,A$，用同一 actual $G_H$ 的已成 $H_B$ 和第五源率 $d_C$ 定义

\[
\kappa_J=\ell_J+(g_{C,J}+g_{0,J}d_C)H_B.
\tag{B.12}
\]

$g_C$、$g_0$ 分别是 `centre_high0_return_source` 与 `ordinary_raw_low_source`。只要求完整body门 $\kappa_B<1$。若通过，任一初始低response四块 $(u_B,u_R,u_O,u_A)$ 转为

\[
x_B=\frac{u_B}{1-\kappa_B},\quad
x_R=u_R+\kappa_Rx_B,\quad
x_O=u_O+\kappa_Ox_B,\quad
x_A=u_A+\kappa_Ax_B.
\tag{B.13}
\]

右下193原子input identity仍保留。这一步尚固定原低reference边界。令 (B.10)的右97输入再经(B.13)所得map为 $\mathcal P$，记录 $p_B,p_R,p_O,p_A$。联合边界输入同理保全，故原root low96输入未删除。

## B6. 原 physical Robin 与 mean 界作用于完整非均值空间

此处必须使用 [真实negative-window证明](R133-supplement-full-delta-negative-one-positive-source-and-regular-ports.md) §6，而不是仅high压缩的reflection常数。

其 (N.10) 的 $E$ 是 **full raw Robin operator** $\mathcal E_\delta$ 在完整 $H^{-5/6}$ mean-zero空间上的界。其 (N.11) 给同一chart的真实mean：

\[
|z|\le m\|y\|_{H^{-5/6}}+
m_+^2(1+C_-I_*B_2)(V_-F_B+|r_C|),
\quad m=m_+^2C_-I_*.
\tag{B.14}
\]

该文直到 (N.12) 才施 $P_H$ 并形成高reflection。因此 $E,m$ 都有资格接收完整低+高 $y$，不是仅 $P_H\mathcal E P_H$ 的norm。

完整已成summary中精确来源分别是
`actual_complete_negative_order_outer_constants.raw_Robin_bound` 与
`exterior_mean_output_coefficients[0]`。后者的原输入名是
`full_nonmean_y_Hminus5over6`。低向高的单独affine系数
$\beta_b$ 是 `exterior_affine_Y_output_coefficients[0]`，其输入名是
`low_nonmean_y_Hminus5over6`。这些literal输入次序在未来consumer中必须核定。

低 $\Theta$ 正是该Bessel norm的有限restriction；高输入保完整 $H^{-5/6}$，不使用有限带宽。$\rho_C$ 是物理chart消元后已含height/mean源的行，仍按(B.14)及原报告单位转授，不能直接把未变换 $r_C$ 改名为 $\rho_C$。原ordinary Robin residual同样保其独立 $H^{-5/6}$ 单位。

## B7. 高outer-low列与真实97+96有限方块

真实高图具有

\[
h_H=G_HBx+P_bb+h_d,\quad
y_H=T_xx+T_bb+t_d,\qquad b=\Theta y_L.
\tag{B.15}
\]

$P_b$ 由上节 $\beta_b$ 注入原negative high图的
`body_outer_mean_head_and_Y_weighted_jumps` 列（索引3）。此列原 raw输出只有 $L^2H^{-1}$。若该整列 raw norm 为 $C_{-,b}$，则对每个低receiver $J$，先取

\[
j^0_J=
\bigl(\sqrt{1+16\cdot160^2}\,g_{C,J}
 +\sqrt{1+16\cdot288^2}\,g_{0,J}d_C\bigr)
C_{-,b}\beta_b.
\tag{B.16}
\]

转换只发生在实际 finite $C$ 接收壳。原高场从未被授予 raw $L^2$。将四项 $j_J^0$ 经(B.13)得到 $\mathcal J_b$ 的 $j_B,j_R,j_O,j_A$。它与 $\mathcal P$ 一起给
$x=x_0+\mathcal P r+\mathcal J_b b$。

若原该列的body-$Y$ sup系数为 $C_{Y,b}$，原even frame row界4给
$t_b=4C_{Y,b}\beta_b\ge\|T_b\|$。
已成新head高response的第四量记为 $t_X\ge\|T_x\|$。两者均是实际trace资格，不从raw体norm推取。

原physical关系仍准确为真实高源合同 (H.15)–(H.16)。由 $p_\delta\in(1/8,1/5)$ 与 $p_0=13/80$，
$|p_\delta-p_0|\le3/80$。故完整两行receiver满足

\[
a_b=\sqrt{(3/80+E)^2+m^2}\ge\|A_b\|,
\quad a_h=\sqrt{E^2+m^2}\ge\|A_h\|.
\tag{B.17}
\]

未知数始终是 $r\in\mathbb R^{97}$、$b\in\mathbb R^{96}$，包括独立mean。四个真正有限map为

\[
U=A_hT_x\mathcal P,\quad
V=A_b+A_hT_b+A_hT_x\mathcal J_b,\quad
W=O_b\mathcal P,\quad Z=O_b\mathcal J_b.
\tag{B.18}
\]

其系数矩阵为 $\begin{psmallmatrix}I-U&-V\\-W&I-Z\end{psmallmatrix}$。从前述具体scalar receivers可取

\[
N=\begin{pmatrix}u&v\\w&z\end{pmatrix}
=\begin{pmatrix}
a_ht_Xp_B&a_b+a_h(t_b+t_Xj_B)\\
p_O&j_O
\end{pmatrix}.
\tag{B.19}
\]

这不是用norm伪造一个signed193矩阵。$N$ 是该准确 $97+96$ 方块的四个operator norm上界；所有mean、high Poisson和physical angle项在(B.18)中先保留。

若新的完整directed值证明

\[
u<1,\qquad z<1,\qquad
\Delta=(1-u)(1-z)-vw>0,
\tag{B.20}
\]

则 $\rho(N)<1$。按正矩阵加权的block norm得到真实193方块逆，且对任意完整两行RHS范数 $e_r,e_b$，

\[
\|r\|\le\frac{(1-z)e_r+ve_b}{\Delta},\qquad
\|b\|\le\frac{we_r+(1-u)e_b}{\Delta}.
\tag{B.21}
\]

这里允许 $w>1$，无需更强的 $\|N\|_2<1$。随后 root97输出仍为
$x_{0,R}+p_R\|r\|+j_R\|b\|$ 的界，完整193atom用自己的joint bound保留。失败只排除这一充分比较，不能宣称实际方块奇异。

## B8. 后继范围与公共执行

本次实际程序只执行 B1–B3 的两个参考边界目标。B4–B7需要未来R141完整成功、内部反馈小门与实际后继标量消费；本篇没有把它们登记成已经完成。原 seven ports 的direct low列、physical height/Robin/mean RHS 转换和两条原WPN RHS仍须逐完整对象组装。给定正区root incoming数据的外行逆也不自动完成负区连接、全局非线性或几何结论。

真正 $G_H$ 路线与旧 WJK 有限 $F$ 的有限-$\rho$ 桥不是同一个对象。若回到旧finite Schur，仍须支付 $C(F-G_H)B$ 或对准确新算子重建桥；原径向tail界3不能替代它。全部当前false scopes明确保留。

新 owner 使用原完整readonly admission和原公共worker的 `scientific_entry_role`，保全部旧已成结论、已成五源、全部七端口。唯一数值新工作是153个同reference定义的hash再识别、96个low scalar profiles及十个边界Gram标量；不调用 actual centre/family provider或任一旧norm目标。固定320bits，16 whole subboxes每panel/mode，science wall3600秒。完整小结果逐条保存、读回核包含，不产生大数组、Artifact或Release。运行结果另行如实登记。
