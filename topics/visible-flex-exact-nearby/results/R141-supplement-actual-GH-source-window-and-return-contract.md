# R141 补篇：真实高逆的五个源率与完整低高返回合同

2026-11-20，visible-exact-astra-ac637-20261120 / positive_inverse。

**已证明：** 在同一 full-real-delta 对象上，有限 head 源可直接使用已成 base-order 高逆的 $H^{1/3}$ ordinary-source 窗，得到完整 raw-$L^2$ 高响应；下文给出五个新可计算源率、未来 R141 低逆的完整消费公式、193原子和真实外端方块的准确位置。**尚未计算：** 五个源率、完整内部反馈门及实际有限端点矩阵。本篇不授任何尚未通过的数值门。

新 owner 只算五个 whole source scalars。它不重算已成 $L$、任何 high inverse、endpoint、atoms或原 small-$K$ 配方。真正 $G_H$ 与有限 WJK $F$ 的合同严格分开；同旧 $F$ 的源率另见 [完整 receiver-free 比较](R141-supplement-receiver-free-complete-FBc-comparison.md)。

## H1. 两份已成高图是同一实际算子

沿用原 repair 定义
$440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47$、
direction 定义
$6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04$，
真实族 $Q_\delta=Q_{\rm repair}+\delta Z$、$|\delta|\le10^{-8}$、固定物理 $\eta_0$。正区 compact $\nu$ bump 为零。反射奇偶、物理频率 $4j$、归一化角测度、普通 $dr$、真正 root 至 $R=25/8$ 和原 cut 都不改变。

完整只读输入是：

- [base-order 全正区图](R133-supplement-full-real-delta-positive-high-root-to-regular-graph.md)及 public run43617150971/1 的完整 summary/process；
- [negative-one 全正区图](R133-supplement-full-delta-negative-one-positive-source-and-regular-ports.md)及 public run43627228225/1 的完整 summary/process。

两个 summary 的 collar/body/outer native SHA、区间、cut、repair、direction完全相同。每份原 process 与当前 whole summary 的 bytes/SHA及 native、source receipts逐项相接；全部7源列、全部 response rows、独立 exterior mean/affine rows均保留为 whole-object reference。

把七个独立高端口设为零后的真实高逆记为 $G_H$。第一份证书给 ordinary-source 列

$$
\|G_H(f_c+f_b)\|_{L^2_rL^2_\phi}
\le C_c^{(0)}\|f_c\|_{L^2_rH^{1/3}_\phi}
 +C_b^{(0)}\|f_b\|_{L^2_rH^{1/3}_\phi}.
\tag{H.1}
$$

这里 $C_c^{(0)},C_b^{(0)}$ 就是完整 `entire_positive_raw_L2` 行的 collar/body 两列，不是单段局部解。第二份证书对同 $G_H$ 给 $L^2H^{-2/3}\to L^2H^{-1}$ 的原粗窗及完整实际 exterior graph。强源窗嵌入粗源窗、强输出嵌入粗输出；真实齐次端口相同，粗窗唯一性故将两份解识别为同一个 $G_H$。这没有重做原 Riccati/reference 或 source sweep。

当外部 stable-root、jumps、outer/mean/height数据仅在原粗单位时，仍用第二份原七列。不能据有限 head 源的强窗，把那些任意外部数据一律升级到 raw $L^2$。

## H2. 五个新目标的精确定义

令 $E_L$ 的原 normalized real order 为 odd $1,\ldots,96$、even mean、even $1,\ldots,96$。令

$$
\mathscr X=L^2(I;E_L),\quad
B_c=B_{HL,c}S^{-1},\quad
\Delta B=(B_{HL}-B_{HL,c})S^{-1},\quad
\Delta C_0=B_{LH}-B_{LH,c}.
\tag{H.2}
$$

$S$ 与原 WVC 完全相同：odd 权1、even及mean权 $q$。$A_{L,c}$ 保同实际 $\eta$ 的 principal，lower centre仍是原 repaired degree32 hybrid。真实 full-family 差不因这个选择而删除。

记 $I_c$ 为原真正 root collar，$I_b$ 为其余正区。五个新上界分别满足

$$
\begin{aligned}
b_{c,c}&\ge\mathop{\rm ess\,sup}_{r\in I_c}
 \|\langle4D\rangle^{1/3}B_c(r)\|_{\ell^2_L\to\ell^2_H},\\
b_{c,b}&\ge\mathop{\rm ess\,sup}_{r\in I_b}
 \|\langle4D\rangle^{1/3}B_c(r)\|_{\ell^2_L\to\ell^2_H},\\
b_{\Delta,c}&\ge\mathop{\rm ess\,sup}_{r\in I_c}
 \|\langle4D\rangle^{1/3}\Delta B(r)\|_{\ell^2_L\to\ell^2_H},\\
b_{\Delta,b}&\ge\mathop{\rm ess\,sup}_{r\in I_b}
 \|\langle4D\rangle^{1/3}\Delta B(r)\|_{\ell^2_L\to\ell^2_H},\\
d_C&\ge\mathop{\rm ess\,sup}_{r\in I}
 \|\Delta C_0(r)\|_{\ell^2_H\to\ell^2_L}.
\end{aligned}
\tag{H.3}
$$

其中 $\langle4D\rangle^{1/3}$ 在频率 $j$ 上乘
$(1+16j^2)^{1/6}$。$B_c$、$\Delta B$ 右侧各含一次 $S^{-1}$；
$\Delta C_0$ 是 raw 输出源，所以第五目标不添左 $S$，后继由低 Green 自己承担观察的 $S$。

具体保存名按同一顺序为

1. `complete_centre_BHL_Hthird_collar_upper`；
2. `complete_centre_BHL_Hthird_body_upper`；
3. `complete_family_BHL_Hthird_collar_upper`；
4. `complete_family_BHL_Hthird_body_upper`；
5. `complete_family_BLH_raw_L2_upper`。

原中心 $B_c$ 的输出仅 $97\le j\le160$，完整 full-family $\Delta B$ 的输出至288，$\Delta C_0$ 的高输入也仅至288。原因分别是 degree32/degree96 的 local quadratic带宽64/192以及两个有序 primitive因子的总带宽；未知高解始终无限维。中心 pure mean输入的高输出精确为零，源码逐155格核这一个 exact zero列；它没有将实际 $\Delta B$ 的 mean输入设零。

## H3. 整155格的实际实现

新纯模块 `fourfold_codazzi_actual_GH_source_fees_math.py` 仅有原证据的 metadata admission及 `complete_source_fees`。后者对同原153 parents、4650 closed rows、4801 intersections构成的155个完整 comparison panels执行：

1. 从 `context.centre_matrix(HIGH0,HEAD,whole_box)` 取得真实 signed $128\times193$ 矩阵；左乘逐模 $(1+16j^2)^{1/6}$，右按原 $q^{-1}$ 缩放even/mean列，最后取全矩阵 Schur norm；
2. 对全 family `HL` raw fee乘 $\|S^{-1}\|$ 与 $(1+16\cdot288^2)^{1/6}$，得到第三、四项的保守完整界；
3. 对全 family `LH` raw fee取整个正区最大值，得到第五项。

每个 sup 都覆盖整真实 panel 与全部实际族参数。按照原 parent是否为0区分 collar/body；没有将 collar source coefficient设零，也没有给 cut 两侧免费延拓。两处 comparison切分仅用于正确包围cutoff，不能把切格解释为缩窄原actual coefficient balls。

matrix Schur norm保留所有signed coefficient相加后才取绝对值。family fee则是此前同 context定义的完整真差包围，包括主部与drift的有界低输入角导、primitive与独立mean项。它的构造不是重新计算某个已经保存的科学 bound；本次五个新的whole组合此前未算。

owner完全不调用 `_complete_modal_norm_comparison`、高或低 Green action、旧 $L$ producer、`complete_positive_residual_base` 或原50图。它也不额外计算 $\|\Delta A_LS^{-1}\|$；原低族误差的已成完整 $L$ 按 H5 的资格只读消费。

所有5目标在全部155格完成后各自保存一个 whole directed upper，完整75位ball写入后再读回并检验 `saved.contains(original_upper)`；后继只消费读回upper。失败保完整prefix且不自动重复已成目标。固定公共 Python3.12.14、python-flint0.9.0、320bits与单线程；数学wall cap1800秒，无新大数组或Release。

## H4. 真正高响应，不经负一阶重构

记 $b_c=b_{c,c}+b_{\Delta,c}$、$b_b=b_{c,b}+b_{\Delta,b}$。因为 $B=B_c+\Delta B$ 是 pointwise低到高源，$P_cx$ 与 $P_bx$ 是其输入的正交分块。由 (H.1)，对 $\|x\|_{\mathscr X}=1$，

$$
\begin{split}
\|G_HBx\|_{L^2L^2}
&\le C_c^{(0)}b_c\|P_cx\|+C_b^{(0)}b_b\|P_bx\|\\
&\le H_B,\qquad
H_B=\sqrt{(C_c^{(0)}b_c)^2+(C_b^{(0)}b_b)^2}.
\end{split}
\tag{H.4}
$$

完整旧 `body_Z_sup` 与 `full_root_outgoing_unstable_port` 两行的同两列可用相同公式分别给 $H_Z,H_{\rm root}$。在外端，原
$h_j=M^{-1/6}T_MZ_j$、$M=|4j|\ge388$，
$p\in(1/8,1/5)$、$0<g<2$ 给 $\|T_M\|<5$。例如 Frobenius平方为
$(p^2+g^2+2)/(p+g)\le p+g+2/p<25$。
故实际外even迹满足

$$
\|P_Hh_2(R)\|_{H^{-5/6}}\le \frac5{388}\,H_Z\|x\|.
\tag{H.5}
$$

这里使用已付的 state sup与真实frame恢复；没有从 raw体 $L^2$ 免费取端点。完整 $G_H$ 已包括全部 actual高系数族，内部返回不再附加一个重复的 $\Delta A_{HH}$ 费用。与此同时 low与cross的差仍在下一节全部支付。

与之不同，WJK 的 $R_c$、$\Delta APB_c+\Delta B$ 是非局部源算子；它们的 collar/body输出掩码不将同一个head输入分成正交域。对那条路线必须保留
$C_c^{(0)}\rho_c+C_b^{(0)}\rho_b$ 的三角式，不能无证明套用 (H.4) 的平方和。

## H5. 同一低逆与旧 $L$ 的连续资格

令 $G_D$ 为原WVC低reference逆，$O$ 为原变换body加全部root97/outer96观察。已经保存的三个 $L$ records来自 run44724797559/1；其norm记为 $L_0$。

可消费的准确资格是

$$
\|OG_D\,\Delta A_LS^{-1}\|_{\mathscr X\to\mathscr Z}
\le L_0,\qquad
\mathscr Z=\mathscr X\oplus\mathbb R^{97}\oplus\mathbb R^{96}.
\tag{H.6}
$$

这不是从有限投影 $P_f$ 的范数反推出连续范数。直接检查该次已保存算法：
`_complete_modal_norm_comparison(...,low=True,...)` 的body callback在每个完整 $(r,s)$ cell包围连续低Green核；mean分支、两三角均在内。其 atom callback把全部193端点row作为一个完整Hilbert块。随后 `CompleteBlockEnvelope.forward/reverse` 只用普通真长度积分和该完整atom块；没有 $P_f$ 或cell-average norm出现在这一计算。与pointwise $\Delta A_LS^{-1}$ 的实际完整费用复合后，保存的row/column及其Schur乘积因此直接证明 (H.6)。保存结果原有有限receiver资格仍保留，但这里的连续资格来自算法本身的逐核证明。

若未来 R141 的同对象真正 $G_L$ 已认证，记

$$
c_B\ge\|\operatorname{pr}_B(T_L-I)\iota_B\|,\quad
c_A\ge\|\operatorname{pr}_A(T_L-I)\iota_B\|,\quad
T_L=I+OG_L(A_{L,c}-D_f)S^{-1}\operatorname{pr}_B .
\tag{H.7}
$$

$OG_L=T_LOG_D$；$T_L-I$ 只读body输入但向全部193atoms输出。由完整联合界 (H.6)，有

$$
\ell_B=(1+c_B)L_0,\qquad
\ell_A=\sqrt{1+c_A^2}\,L_0.
\tag{H.8}
$$

第二式对 $OG_D\Delta A_LS^{-1}$ 的body/atoms两个正交输出用 row norm $\|(c_A,1)\|$，并非将两块分别都取 $L_0$ 再声称关联。旧 $L$ 三量保持whole只读；本次五目标不重新计算 (H.6)–(H.8)。

## H6. 193原子的完整实际内部收缩

未来 R141 的源角色 `centre_high0_return_source` 与 `ordinary_raw_low_source` 分别提供

$$
g_{C,B/A}\ge\|\operatorname{pr}_{B/A}OG_LB_{LH,c}\|,\qquad
g_{0,B/A}\ge\|\operatorname{pr}_{B/A}OG_L\|.
\tag{H.9}
$$

结合新的第五率及 (H.4)，真实内部反馈

$$
\mathcal K=
OG_L[\Delta A_LS^{-1}+
(B_{LH,c}+\Delta C_0)G_H(B_c+\Delta B)]\operatorname{pr}_B
=\begin{pmatrix}K_B&0\\K_A&0\end{pmatrix}
\tag{H.10}
$$

满足

$$
\kappa_B\le\ell_B+(g_{C,B}+g_{0,B}d_C)H_B,\qquad
\kappa_A\le\ell_A+(g_{C,A}+g_{0,A}d_C)H_B.
\tag{H.11}
$$

假如完整新上界给 $\kappa_B<1$，就得到真正 actual interior/high feedback 在原reference低边界下的增广逆，且

$$
(I-\mathcal K)^{-1}
=\begin{pmatrix}(I-K_B)^{-1}&0\\K_A(I-K_B)^{-1}&I\end{pmatrix}.
\tag{H.12}
$$

令 $t=(1-\kappa_B)^{-1}$、$s=\kappa_A t$，完整范数可取

$$
\|(I-\mathcal K)^{-1}\|
\le\frac{\sqrt{(t+1)^2+s^2}+\sqrt{(t-1)^2+s^2}}2 .
\tag{H.13}
$$

只对body环要求小于一；大atom接收器不能被删除，也不必强行小于一。所有原子输入通过右下identity进入同一空间，故没有读取任意 $L^2$ 输入端点的非法操作。

任一完整已换坐标 RHS/port 的body、atoms上界为 $(u,v)$ 时，其响应界为

$$
(u,v)\longmapsto\left(\frac u{1-\kappa_B},
v+\frac{\kappa_Au}{1-\kappa_B}\right).
\tag{H.14}
$$

原WPN有限行 $f_f$ 与径向mean-zero tail行 $g_t$ 必须各自完整变换后使用 (H.14)；第二行不设零、不用两个moments替换。已付 $\kappa=3$ 是原径向tail逆，不是 (H.1) 的angular高逆，也不免除其实际Schur余项。

## H7. 原七端口和真实外193行的位置

对任意原粗端口，第二份高图仅给 $L^2H^{-1}$。接收到finite centre shell时可付
$\sqrt{1+16\cdot160^2}$，接收到family shell时付
$\sqrt{1+16\cdot288^2}$；再乘 (H.9) 的对应完整低source界。该转换只在实际有限接收壳进行，不声称整个外部高场属于raw $L^2$。高even外迹另由该图的body-$Y$ sup和even frame row norm $\le4$ 控制。七个原source/affine/stable/jump列仍各自保留，direct low、density两mean、外height、Robin及mean残差另按其原单位加入。

即使 (H.12) 通过，实际physical外行仍需一个真实有限块。为说明它不会被当作免费boundary perturbation，写原moving外图

$$
-J_\phi h_1-p_\delta y=\mathcal E_\delta y+\rho_B,\qquad
z=\mathcal M_\delta y+\rho_C,\quad
y=P_{\ne0}h_2,\ z=\langle h_2\rangle_\phi .
\tag{H.15}
$$

$\mathcal E_\delta,\mathcal M_\delta,\rho_B,\rho_C$ 必须是完整真physical-angle/DN/mean chart；$\rho_C$ 包括实际chart解后的mean/height源，不能直接把原未变换mean残差改名为它。

设 $b=\Theta y_L\in\mathbb R^{96}$，参考right97数据为
$r=(\Theta(h_{1,L}+p_0y_L),z)$，$p_0=13/80$。在原odd/even real基中 $J_\phi$ 把odd sine坐标送到even cosine坐标。于是 (H.15) 准确给

$$
r=A_bb+A_hy_H+g,\qquad
A_b=\binom{\Theta[(p_0-p_\delta)I-P_L\mathcal E_\delta\iota_L]\Theta^{-1}}
{\mathcal M_\delta\iota_L\Theta^{-1}},
\quad
A_h=\binom{-\Theta P_L\mathcal E_\delta\iota_H}{\mathcal M_\delta\iota_H}.
\tag{H.16}
$$

这里 $g=(-\Theta P_L\rho_B,\rho_C)$，$\Theta$ 是原outer $H^{-5/6}$权。actual高图的原outer-low源给
$h_H=G_HBx+P_bb+h_d$，
$y_H=T_xx+T_bb+t_d$；
所有独立source/height/mean和rootstable项在 $h_d,t_d$。$P_b$ 不是直接删去的零项。

经过 (H.12) 的实际内部逆，写
$x=x_0+\mathcal P r+\mathcal J_b b$；
$\mathcal P$ 是全部right97实际Poisson列，$\mathcal J_b$ 包含真实 $P_b b$ 的低返回，$x_0$ 保指定root96、ordinary与全部affine源。令 $O_bx=\Theta h_{2,L}(R)$，则两组真实有限条件构成

$$
\begin{pmatrix}I-U&-V\\-W&I-Z\end{pmatrix}
\binom r b
=\binom{g+A_h(t_d+T_xx_0)}{O_bx_0},
\tag{H.17}
$$

$$
U=A_hT_x\mathcal P,\quad
V=A_b+A_hT_b+A_hT_x\mathcal J_b,\quad
W=O_b\mathcal P,\quad Z=O_b\mathcal J_b .
\tag{H.18}
$$

这些块的形状为 $97^2,97\times96,96\times97,96^2$；完整mean在right97中。root97补输出仍由同一个 $O_a(x_0+\mathcal Pr+\mathcal J_bb)$ 取得。所有列必须是真signed finite action，不能从norm表构造伪矩阵或据小维度宣称det非零。独立physical-density两mean的行、$\nu$与其他系统的联立也没有被moving mean这一坐标取代。

## H8. 与旧有限 $F$ 桥的严格区别

(H.10) 使用真正 $G_H$，包含全部actual高族；WJK $F=P+Q^*-Q^*L_cP$ 是有限trial。原 R137 连续到finite桥和原 $\rho$ normalizer首先绑定旧 $F$ 的完整centre，故不能把 (H.12) 的逆直接标成该旧centre逆。

若要消费旧 $F$ 桥，使用另一新目标 $\|\Pi_0FB_c\|$ 与 R141 source界先闭同 $F$ 的CFB环；actual correction再由 W2H完整双侧恒等式支付
$\Delta A,\Delta B,\Delta C,R_c-\Delta APB_c-\Delta B$，保288/416支持与真正 $G_H$的全残差。或者为actual $G_H$ 重新建立完整source、finite factor、projection/normalizer和两RHS；不能只换一个符号。

本次5目标完成时，owner仅将完整five-source-rates旗标设true。actual low/high inverse、true low97+outer96行、全7ports、原finite $\rho$和任一RHS均继续为false，直到各自完整新证书实际通过。最终精确可见闭族及非线性、负侧、腰帽匹配仍按课题README执行。
