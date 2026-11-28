# R149 TP：真 low193 四个 whole maps 到原完整正侧与物理链

**解析转接与执行接口已证明；下面新的标量门尚未运行。**
2026-11-28。本条消费 [TF](R149-supplement-true-low193-local-flow-and-direct-response.md)
真正成功的两项结果，将其接入原完整正侧的58、224、32条记录，
继而接入 [PN](R149-supplement-complete-positive-inverse-to-true-negative-and-incoming.md)
的56条和 [CXN](R149-supplement-actual-common-high-negative-receiver-execution.md)
的6条。它不是又一个一般 Schur 引理，也不以一次 hybrid solve
冒充完整 $DF$。TF 尚未产生成功 whole actual 时，配套 generator
只给真实的 not-ready 结果，不造未来输入或可运行 manifest。

## 1. 真正相同的四个源、四个接收器

令 $G_c$ 为 TF 的实际原 WVC hybrid $A_{Lc}$ 边值逆。原低频193
坐标、独立 even mean、$S$、真实根端和普通 $dr$ 全保持；
右端 raw 条件仍为

$$
 B_bx=((u_j+\tfrac{13}{80}v_j)_{j=1}^{96},v_0),
 \qquad B_ax=(v_j)_{j=1}^{96}(r_*).
 \tag{TP.1}
$$

这里“193坐标”包含 mean，绝不把它删成192维。原四接收器是
$B=Sx$ 的普通 $L^2(dr)$、$R=(u_1,\ldots,u_{96},v_0)(r_*)$、
$O=(\Theta_jv_j(R))_{j=1}^{96}$ 和 $A=R\oplus O$。
$\Theta_j=(1+16j^2)^{-5/12}$。

TF 的四个完整 source roles 准确给下表；所有上界指同一个
$\mathcal O G_c$，其中 $\mathcal O=(B,R,O)$。

| TF role | 实际输入 multiplier | 列数 | 后继符号 |
|---|---:|---:|---|
| `ordinary_raw_low_source` | $Id$ | 193 | $g_{0J}$ |
| `transformed_low_source` | $S^{-1}$ | 193 | $g_{SJ}$ |
| `low_second_kind_correction` | $(A_{Lc}-D)S^{-1}$ | 193 | $c_J$ |
| `centre_high0_return_source` | 原完整 $C_*=B_{LH,c}$ | 128 | $g_{CJ}$ |

每项的 body、joint atoms 和完整 norm 直接复制 TF 的完整已保存
记录。原 root/outer 分开接收器的新上界准确是

$$
 g_{WR}=\sqrt{\operatorname{TF}_{W,R}^{HS2}},\qquad
 g_{WO}=\sqrt{\operatorname{TF}_{W,O}^{HS2}},
 \quad W\in\{0,S,\mathrm{correction},C\}.
 \tag{TP.2}
$$

这些是实际 Green 的平方范数；不加旧 comparison defect，
也不在旧数据里填一个虚假的 zero defect。旧
[B8](R141-supplement-reference-boundary-lifts-and-physical-outer-block-gate.md)
的 comparison-source 提升已经由 TF 实际逆取代，其余 B 的
原完整算子恒等式仍然适用。

TF 原128列 $C_*$ 不是全 $CFB$。同一原 selected-family 的
$\Delta A_L=A_L-A_{Lc}$、$\Delta C=C-C_*$、真实 $B_{HL}$、
$G_H$ 和物理 Robin/mean 图继续由下节的原 whole 结果支付。
这里没有换成 PA 的 compact mean-exact 背景。

## 2. 全 family、全 high 和全 CFB 的实际费用

完整输入是原 [GH5](R141-supplement-actual-five-GH-source-fees.md)
run44736533396/1、原 low-family run44724797559/1、
原 GH4 run44740105701/1、原
[有权 GH](R141-supplement-actual-radially-weighted-high-response.md)
run44746534556/1 和原 negative-one physical graph。
每份 actual、execution、源定义及完整 reference identity 逐项核对。
旧 GH4 原球保留，有权 GH 是一个显式的独立替换输入。
配套程序只读取下列整个记录：

$$
\begin{split}
 L_0&\ge\|\mathcal O G_D\Delta A_LS^{-1}\|,\quad
 d_C\ge\|\Delta C\|_{L^2\to L^2},\\
 H_B&\ge\|G_H B_{HL}S^{-1}:L^2(dr)\to L^2(dr)\|,\quad
 t_X\ge\|\text{原 high 外端 even trace}\|.
\end{split}\tag{TP.3}
$$

它们都是原完整空间的上界；没有从 $C_*$ 的128列中反推
$B_{HL}$ 或 unknown high operator，没有把旧上界相减或相除
还原任何未保存的系数。

TF correction role 给准确的原 second-kind 恒等式

$$
 T_L=Id+\mathcal O G_c(A_{Lc}-D)S^{-1}\operatorname{pr}_B.
 \tag{TP.4}
$$

其中193个独立 atom inputs 的 identity 全保留。于是原 low-family
费用与完整 internal feedback 逐接收器为

$$
 \ell_B=(1+c_B)L_0,\qquad
 \ell_J=\sqrt{1+c_J^2}\,L_0\quad(J=R,O,A),
 \qquad
 \kappa_J=\ell_J+(g_{CJ}+g_{0J}d_C)H_B.
 \tag{TP.5}
$$

最后一项明确是
$\mathcal O G_c(C_*+\Delta C)G_HB_{HL}S^{-1}$ 的完整支付，
加上第一项后才是实际 full-family internal loop。
只有新保存的 $\kappa_B<1$ 才继续，使用重新保存的
$\gamma=1-\kappa_B>0$。其余三个接收器按原 B 的
$u_J+\kappa_Ju_B/\gamma$ 提升，原指定的 root-even96
边界 lift 在此 closure 后加入，不另除一次 $\gamma$。

若第一门不通过，结果是完整 sufficient gate 未通过；不是
奇异性或无解结论，也不能继续生成224/32消费者。

## 3. 原 boundary、height、Robin 和 mean 没有少一条

原 run44745017016/1 的完整10条 reference boundary lift norms
分别处理 weighted right97 和 joint193 边界输入。对其中任一
完整 $X_D$，实际 lift 是 $\mathcal O X_c=T_L\mathcal O X_D$，
故原 B9 给

$$
 p_B=(1+c_B)d_B,\qquad p_J=d_J+c_Jd_B\quad(J=R,O,A),
 \tag{TP.6}
$$

再用 (TP.5) 关闭完整 internal loop。独立 outer low even 输入
到 high Poisson 的低频返回仍支付原160和288 support factors：

$$
 j_J^0=\big(\sqrt{1+16\cdot160^2}\,g_{CJ}
       +\sqrt{1+16\cdot288^2}\,g_{0J}d_C\big)
       C_{-,b}\beta_b,
 \qquad t_b=4C_{Y,b}\beta_b.
 \tag{TP.7}
$$

$C_{-,b}$ 是原 ordinary $dr$ 的整个 $L^2_rH^{-1}$ 输出，
$C_{Y,b}$ 是原真实 trace receiver。两个常数分别由原 negative
graph 完整行取得；不从一个 arbitrary $L^2$ 解取端点 trace。

原物理 right97 输入和 high coupling 仍为

$$
 a_b=\sqrt{(3/80+E)^2+m^2},\qquad
 a_h=\sqrt{E^2+m^2},
 \tag{TP.8}
$$

其中 $E$ 是整个 nonmean 空间上的原 Robin 算子上界，$m$ 是
独立 mean row；不是只对 high compression 的上界。
原 B18–21 的完整2-block门据 (TP.5–8) 产生同样58个有向记录。
先保存读回每个完整球，再使用它的正确方向 endpoint。
对 inverse numerator 仍使用 $1-z,1-u$ 的 upper，不能误用
正 lower margins 作为 numerator upper。

达到真正58条通过分支后，原
[P224](R141-supplement-original-seven-ports-after-the-physical-gate.md)
的14输入、16输出直接适用：原7个 high/source/jump ports、
raw low、$S^{-1}$ low、root-even96、charted right97、独立
height、Robin、mean 全保留。height/Robin/mean 各自同时进入
原 high affine 图和 low right97 图，不能只付其中一条路径。

接着原 [L](R141-supplement-both-WPN-rows-by-exact-WOB-source-lifting.md)
用相同24480径向投影、原 $q\ge1/8$ 和真正 lifted $w\in H^1$
给两条 WPN 行的32个完整输出。它们涵盖原完整 finite input
和整个 orthogonal tail，不需要旧未通过的 finite-$\rho$ 门。
只有这条实际链完成才得到 PN 所需的完整正侧逆；TF 本身仍
只证明 hybrid 逆。

## 4. 实际 owner 和原 PN56/CXN6 的兼容性

新增独立文件是：

- `fourfold_codazzi_true_low193_physical_consumer_math.py`：TF 的纯
  metadata admission、(TP.2–8) 的完整58记录和原 gate readback。
- `fourfold_codazzi_true_low193_physical_chain_owner.py`：只从真实
  TF actual/execution/manifest 与原 whole high inputs 运行一个
  gate、ports 或 wpn stage。
- `make_true_low193_physical_chain_manifest.py`：只在该 stage 的
  全部实际前驱成功且整个文件存在时生成 manifest/workflow。

TF admission 逐项检查完整两目标、原参数和5份 source/proof
定义、1424整 cells、所有4个 whole maps、原193观测以及每个
4273实际 pivot。pivot SHA 按真实顺序恢复：全部 left97，
node1424，随后 right1423/node1423 至 right0/node0；并非把
三个数组分别排好就假定是原顺序。它保留旧 comparison false
outcomes，不要求旧 whole-point gate，更不把它们改名为成功。

原 generic physical stage 的数学输出契约没有改变，因此仍使用
`complete_actual_positive_physical_scalar_stage_v1` 和原58、224、32
记录名；这不是给 TF 改 kind。TF actual 一直保留自己的
`complete_R149_true_low193_direct_flow_and_source_maps_v1`，新 gate
另保存明确的 `low_inverse_basis` 和 direct-source 标记。
原 public worker 按这套原 stage schema 验证，所有输出带实际
新 source SHA，不调用任何 prior producer。

[PN56 owner](../scripts/fourfold_codazzi_positive_inverse_negative_receivers_owner.py)
与 [CXN6 owner](../scripts/fourfold_codazzi_common_high_negative_receivers_owner.py)
检查原 generic stage 的实际 source SHA、全部记录、exact chain
receipts 和同一个完整 reference identity，没有绑定旧 low 的
comparison kind。因此这条新实际58→224→32链无须伪造一个旧
comparison certificate，就能进入它们现有的56/6目标。
它们依然须逐个实际运行；本文没有代填这些结果。

## 5. 若需要 signed response，原完整 RHS 的准确入口

TF 的四个 norm maps 没有保存任一具体 forcing column 的 signed
response。新 signed owner 必须向 TF 的
`certify_true_model(source_provider=...)` 提供真正的193×$k$
whole-cell forcing，每一列包含其原 mean；然后才调用
`solve_signed_response`。同定义 true flow 为新 forcing 所需的
materialization 不是重算旧范数目标；新 owner 不再调用四个
已完成 source norm reducers。

对原实际 low/high 方程，任何一次 signed 迭代或 residual
校正的真实 hybrid forcing 准确是

$$
 f_c=\Delta A_Lx+(C_*+\Delta C)h+f_L,\qquad
 L_Hh=B_{HL}x+f_H,
 \tag{TP.9}
$$

加上同一列的真实 high Poisson 和 affine jumps。若 $h$ 仍未知，
不能用 $\|G_H\|$ 或一个 saved upper 代替它的 signed values；
同样不能只送 $C_*$ 的128列然后称为完整 $CFB$。
norm-only (TP.5) 允许直接关闭整个无限维 loop；signed 路径则
必须实际供给 (TP.9) 的全载体及其完整误差。

对原 WPN pair $(F,e)$，准确 lifting 是

$$
 c=E_c^*e,\quad k=F+C_*^{\rm lift}E_cc,\quad a=k+w,
 \qquad B_aw=-c.
 \tag{TP.10}
$$

这里 $C_*^{\rm lift}$ 是原 L 的 root-even reference lift，
与 (TP.9) 的 high-return $C_*=B_{LH,c}$ 不混用。
应送入 TF 的完整 body forcing 为

$$
 f_c=\Delta A_Lw+(C_*+\Delta C)h+A_Lk,\qquad
 L_Hh=B_{HL}(w+k),
 \tag{TP.11}
$$

而原物理 right row 是
$r=A_bb+A_hy_H+g_e$，$g_e=(\Theta e_{odd},e_{mean})$。
它没有额外的 $(13/80)c$，因为 $e-E_cc$ 已经准确消去该 even
分量。$k$ 只要求 $L^2$；不能取它的 root trace。

原 right97 $r$ 的前96坐标已乘 $\Theta$，TF API 的
`right_data` 却是 (TP.1) 的 raw 值。因此实际调用必须且只须
做一次

$$
 r_{\rm TF}=(\Theta^{-1}r_{1:96},r_{97}).
 \tag{TP.12}
$$

配套纯函数 `solve_original_charted_signed_response` 已实现
(TP.12)，保完整 left96、独立 right mean 和 TF 返回的 root97、
outer96；它不重乘输出 $\Theta$。返回的节点值仍不足以代替
whole-cell body response，后者须继续使用 TF 的完整 local
prefix flow 与 signed affine increments。

本条给出了可实际运行的完整正侧入口，尚未支付 TF 当前数值门、
新的58/224/32/56/6数值结果、full finite physical Schur、两条
mean 与 height/phase matching 或最终非线性闭族。
