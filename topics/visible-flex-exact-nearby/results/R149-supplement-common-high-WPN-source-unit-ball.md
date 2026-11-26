# R149 补篇：真实 common 高输入的完整 WPN 源对

2026-11-26，visible-exact-astra-198c63d-20261126 / low_inverse。

本篇把 PN.13 的同一个 frozen common 输入变成原 physical-source 接口的真实完整数据包，并给出不重新物化原大系数载体的 weighted-body 与原 radial-tail 界。数据包描述一个已确定线性算子在单位球上的源，不是尚未知的某个解，也不是为了凑接口而设的零向量。新四个标量可以在 actual58/224/32 之前独立计算；它们不授予尚未完成的正侧或 incoming 逆。

## CX1. 唯一同输入、两行和全部 mean

采用 [WOB.2、WOB.24–31](R133-supplement-complete-outer-rows-and-signed-root96-inverse-certificate.md)、
[完整源对 S.2–S.4](R141-supplement-actual-physical-source-pairs-and-reusable-bounds.md)、
[精确 lifting L.24](R141-supplement-both-WPN-rows-by-exact-WOB-source-lifting.md) 和
[PN.13](R149-supplement-complete-positive-inverse-to-true-negative-and-incoming.md)。
固定原 selected member、固定 physical $\eta_0$、原真实 $r_*$ 和
$$
x\in X^{\rm fr}_{-4/3},\qquad \|x\|_{X^{\rm fr}_{-4/3}}\le1.
\tag{CX.1}
$$
原 $N_i$、$D_+$、自然反射子空间与真实 selected chart 已经在 $\Phi,\Upsilon$ 的右端完整支付一次。下面没有第二个 $N_i$。

取原共同高输入这一列，所有独立资料为零，准确源对为
$$
F_x=V_0\Phi x,\qquad
e_x=-(V_{0,R}\Phi-B_R^H\Upsilon)x.
\tag{CX.2}
$$
这个零独立资料条件定义所研究的线性列；不是从某个尚未知 RHS 缺字段推测零。完整 18 槽原接口恰为：

| 原 source 槽 | 此列的完整 norm record | 原因 |
|---|---:|---|
| frozen_common_high_Hminus4over3 | $1$ | (CX.1) 的实际 operator unit-ball 输入。 |
| root_even96_raw | $0$ | 此列的独立 prescribed physical $c_*$ 准确为零。 |
| rough_stable_Hminus3over2 | $0$ | 不把同一 common cause 重复作为另一 rough stable cause。 |
| low_ordinary_raw_L2 与 low_exactly_S_inverse_transformed_L2 | 各 $0$ | 没有另一个独立 low ordinary source；$\Phi x$ 已在 (CX.2)。 |
| 三个 independent physical height / Robin / mean 槽 | 各 $0$ | 齐次真实 exterior 数据；状态引起的完整外图仍在 (CX.2)。 |
| 原七个 high particular / source / jump 槽 | 各 $0$ | 同一 genuine common 高列已由 $\Phi,\Upsilon$ 表示；没有额外 particular cause。 |
| 三个 raw low jump 总量槽 | 各 $0$ | $V_0\Phi x$ 是原 ordinary 积分，绝无独立 low value jump。 |

17 个零逐一绑定上述精确源身份。原 seven-port stable 槽为零并不声称 genuine common 高基线的 stable trace 为零；后者已经在同一 $\Phi,\Upsilon$ 中，不能重复注入。

尤其 $B_R^H$ 的物理 mean 不为零。由 WOB.4，
$$
\Pi_{\rm even}e_x
 =-\Pi_{\rm even}V_{0,R}\Phi x+\mu_R\Upsilon x.
\tag{CX.3}
$$
独立 exterior mean datum 为零不删除 (CX.3)。另外，lifting 的辅助 $c=E_c^*e_x$ 一般不为零；它与 prescribed $c_*=0$ 不同。准确有 $F_x(r_*)=0$，由 PN.3–PN.5 的抵消，返回解的实际 even96 根仍为零。

## CX2. 只读原完整 WOBSA 球

[WOBSA actual](R133-supplement-actual-complete-outer-rows-and-rough-positive-observations.md) 的唯一 run43844596176/1 已完整保存 37 球和原42球；原 six-source 资格及所有 mean、反射、selected-member 限制保持不变。读取同一 whole actual、execution、manifest 与其 whole 原 small inputs，不调用原 producer。

| 记号 | 完整记录路径，起于 WOBSA scientific |
|---|---|
| $K_\Phi$ | complete_new_graphs.complete_genuine_and_rough_observations.complete_new_records.complete_Phi_upper |
| $B_x$ | complete_new_graphs.complete_zero_IVP_rows.complete_new_records.complete_B0_high_body_row_upper |
| $D_x$ | complete_new_graphs.complete_zero_IVP_rows.complete_new_records.complete_D0_high_endpoint_row_upper |
| $t_0$ | copied_original_scalar_records.C_R0 |

这些分别界 $\Phi$、$V_0\Phi$、$V_{0,R}\Phi-B_R^H\Upsilon$ 和 $\sqrt{R-r_*}$。$D_x$ 已包括整个 raw endpoint193 及 (CX.3)，不由两个 scalar 上界相减恢复 signed 差。

另读原 D-lift run44745017016/1 的完整
reference_weighted_right97_body_upper，记为 $d_B$。
[L.18](R141-supplement-both-WPN-rows-by-exact-WOB-source-lifting.md) 已证明
$$
\|q\|_{L^2(I_+)}\le d_B,\qquad S(r)=\operatorname{diag}(1,q(r))
\tag{CX.4}
$$
作用于完整 odd96 与 even97，包括 independent mean。证明用真实 reference mean 的单位右输入，其 raw 解恒为1；同一 $q$ 是原 WVC/WPN 精确 piecewise-constant weight。这里不以 D 的边界 inverse 替代真实正侧 inverse。

## CX3. 由已付 $L^2$ 权控制 weighted body

写 $\Phi x=(g_1,g_2)$。第一分量未加权，故
$$
\|V_0g_1\|_{L^2}\le B_x\|x\|.
$$
对第二分量，普通 $dr$ 的 Cauchy–Schwarz 逐 $r$ 给
$$
|V_0g_2(r)|\le t_0\|g_2\|_{L^2}
             \le t_0K_\Phi\|x\|.
$$
结合 (CX.4)，并只使用输出 odd/even 的真实正交分块，得
$$
\boxed{\quad
 \|SF_x\|_{L^2}\le
 B:=\sqrt{B_x^2+(t_0d_BK_\Phi)^2}.
 \quad}
\tag{CX.5}
$$
这不假设两个 $\Phi$ 分量或两个物理 cause 独立。它是一个保守的完整界，不声称优于未来可能直接获得的 $\|S\|B_x$；现有输入已经足够实际计算它。没有新 q 最大值目标，也没有把原 physical $S$ 换成别的权。

## CX4. 原24480径向尾的完整界

原153个 parent 各自160等分。设
$$
r_-=\frac{1191984371497}{5000000000000},\quad
R=\frac{25}{8},\quad
h_*=\frac{R-r_-}{160}.
\tag{CX.6}
$$
每个原 fine cell 的真实长 $h_i$ 均满足 $0<h_i\le h_*$。这由同一真根和原细分定义直接得到，不把155 comparison panels或1424 certification cells当作原投影。

在第 $i$ 格，$q=q_i$ 精确为常数，故
$$
(h_iq_i)^2=h_i\int_{I_i}q^2
 \le h_*\int_{I_+}q^2
 \le h_*d_B^2.
$$
因此
$$
\|\Lambda_hS\|_\infty
 \le M_h:=\frac{\max(h_*,\sqrt{h_*}\,d_B)}{\pi},
\qquad \Lambda_h|_{I_i}=h_i/\pi.
\tag{CX.7}
$$
原 S.6 对 $g=\Phi x$ 给
$$
\boxed{\quad
 \|Q_NSF_x\|_{L^2}\le T:=M_hK_\Phi,\qquad N=24480.
 \quad}
\tag{CX.8}
$$
(CX.7) 只以已付 $L^2$ 权作上界，不声称已取得 $\|S\|_\infty$，也不制造 generic source interface 所要求的未有 S-max descriptor。普通源不被求导；没有独立 jump，所以没有漏付 S.7 的阶跃尾。

## CX5. 四个实际新 source 记录与原接口

完整 endpoint bound 为 $E=D_x$。按原正交 finite/tail 分解，
$$
\begin{aligned}
 f_f&=(E_N^*SF_x,e_x),&g_t&=Q_NSF_x,\\
 \|f_f\|^2+\|g_t\|^2
  &=\|SF_x\|^2+|e_x|^2
  \le P^2,&P&=\sqrt{B^2+E^2}.
\end{aligned}
\tag{CX.9}
$$
新 owner 保存以下四条实际记录：

1. actual_source_weighted_body_rhs_upper：$B$；
2. actual_source_raw_endpoint193_rhs_upper：同一完整旧 $D_x$ 对本准确源列的 bound；
3. actual_source_complete_WPN_pair_rhs_upper：$P$；
4. actual_source_original_radial_tail_rhs_upper：$T$。

$P$ 可直接控制 finite RHS；不用两个上界相减，也不再把 $P$ 与 $T$ 平方相加称为准确 pair norm。四条记录采用原 complete_actual_physical_WPN_source_pair_bounds_v1 结果接口，原18槽 DATA_KIND 完整保留，并另标明它们是 (CX.1) 单位球上同一个真实线性列的 operator bounds。

配套新 math/owner 只对这个准确 common-input packet 使用 (CX.5)–(CX.8)，不调用要求 S-max descriptor 的 generic S.11 分支，也不为该分支设置假的 admission flag。既有 generic physical_WPN_source_pair_math 保持原样。所有源表与 selected-member 身份来自已成 whole 输入；无需等待 actual224/32，也不假设它们存在。

每个新记录先写候选、整球读回并核包含原上端，之后才进入正式 completed 前缀。$P$ 使用正式保存的 $B,E$ 上端。旧 $D_x$ 仅应用和复制，不重算其原图。

## CX6. 未来实际32表如何立即消费

这一步只有真实58/224/32及 SP/PW/WTA/WX 完整成功后才执行。本篇不给那些未来结果填值。用原32表两行的真实 root97 与 high-root-mixed receiver，
$$
 d_x\le U_{f,d}P+U_{t,d}T,\qquad
 z_x\le U_{f,z}P+U_{t,z}T.
\tag{CX.10}
$$
返回解为零独立 high stable 的 additional response。由 $c_*=0$，
$$
 K_+\le C_R\sqrt{d_x^2+z_x^2}
 :X^{\rm fr}_{-4/3}\longrightarrow\mathcal Y_0.
\tag{CX.11}
$$
它包含完整 low root、high mixed trace、负区传播、primitive pair 和两个 physical mean。原两左规范分支联合界是 $B_{H,0}K_{W,0}K_+$，WPL primitive 行界是 $B_{H,0}\sqrt{1/2}K_+$；不另乘 $N_i$。

真正 rough genuine baseline 仍保其原自然观察域。不能把它加到 mixed-root 向量再凭本返回的资格授予更强范数。完整 incoming 仍要将 (CX.11) 的实际新 strong addition 与原 baseline、transported finite factors、独立 mean、true phase/nu 和 signed Schur 一起支付。本篇不预称该完整上界足够小。
