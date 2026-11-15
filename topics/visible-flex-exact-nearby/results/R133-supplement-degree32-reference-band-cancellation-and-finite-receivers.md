# R133 续篇：原 degree32 背景的精确频带消去与新的有限 receiver

2026-11-15，visible-exact / tail_connector。

**已证明的解析拆分，供独立核对。** 本篇改写同一个实际 collar 上高频方程的参考背景，不改变实际状态、metric、参数选择、Fourier 投影或旧成功数值。其用途是将通往 $|j|>96$ 的主要有限线性输入限制到 $33\le|j|\le96$。没有声称这个新频带的未知范数已经很小。

依赖 [E 完整 collar 方程](R133-supplement-positive-collar-energy-and-residual-sensitive-first-angular-cut-trace.md)、[PE 投影主部能量](R133-supplement-projected-principal-collar-energy-and-sharper-three-band-trace.md)、[WC 同态双域](R133-supplement-wide-collar-half-trace-and-independent-narrow-high-domain.md)、[MC 原 response mean 身份](R133-supplement-raw-response-mean-identity-and-corrected-collar-source.md)及[实际 MA 窄域](R133-supplement-actual-raw-mean-fee-and-restored-high-collar-domain.md)。所有角测度均为原 normalized moving 圆周，实际物理频率为 $4j$，径向测度为 $dr$。

## 1. 同一个状态和两个有限参考

在真实正 collar $I\subset[17/20,19/20]$ 上取原连续修补 M32 背景 $Q_0$，以及原 canonical 连续方向 $Z_{\rm can}$。在每个真实径向片上，
$$
 \operatorname{supp}_\phi Q_0\subset\{|j|\le32\},
 \qquad
 \operatorname{supp}_\phi Z_{\rm can}\subset\{|j|\le96\}.
 \tag{DB.1}
$$
这里包括全部 mean。连续修补是原有限系数的明确修补，没有产生新的角频率。径向 intrinsic 系数是角常数。

选中的 affine reference 仍为
$$
 Q_\delta=Q_0+\delta Z_{\rm can},\qquad |\delta|\le10^{-10}.
 \tag{DB.2}
$$
$Z_{\rm can}$ 不是 MC 中由 scalar mean-flow 替换 raw trial mean 得到的 $q^\sharp$。本篇不进行这样的替换。

实际未知状态记为 $Q$，其普通残差为
$f=Q_r-\mathcal F(Q)$。在本 collar 上原 $\nu$ bump 准确为0，所以 $Q,Q_0,Q_\delta$ 使用同一组 $\beta,G,K$。这个事实只在当前正 collar 使用，不能推广到 bump 支撑内。

保持 E 的径向矩阵
$$
 P=\operatorname{diag}(K^{-1/4},K^{1/4}),\qquad
 W_0=PQ_0,\quad
 z_0=P(Q-Q_0),\quad z_\delta=P(Q-Q_\delta).
$$
由于 $P$ 与角投影交换，
$$
 z_0=z_\delta+\delta PZ_{\rm can},\qquad
 H_{96}z_0=H_{96}z_\delta,\quad H_{288}z_0=H_{288}z_\delta .
 \tag{DB.3}
$$
同样在 raw moving 单位中，
$H_{96}(Q-Q_0)=H_{96}(Q-Q_\delta)$。这是真正的函数恒等式，不是两个独立上界相减。

## 2. 低参考的完整 residual 支撑

原方程 E.2 的局部非线性是三次，primitive 作用于完整二次 $S$ 后才与 $Q_\phi$ 相乘。$GmJ(K)Q_\phi$ 的 $m$ 是径向完整 mean。故
$$
 f_0=Q_{0,r}-\mathcal F(Q_0),\qquad
 \operatorname{supp}_\phi f_0\subset\{|j|\le96\}.
 \tag{DB.4}
$$
全部 radial model remainder 都是角常数，完整 mean 和 continuous-repair 导数也不提高 (DB.4) 的角支撑。原数据接口准确保留真实 one-sided 径向量；$Q_0$ 的连续性使这里不另生状态跳的分布原子。

因此 E 的差分源 $F_0=P(f-f_0)$ 满足
$$
 H_JF_0=H_JPf\quad(J\ge96). \tag{DB.5}
$$
对同一个真实解 $f=0$，所有这些高投影源准确为0。对近似态仍须保留其完整 $H_JPf$；原背景 degree32 不能删去未知近似残差的高频部分。

这不改变 selected-centre 的准确多项式
$f_\delta=f_0-\delta b_0+\delta r_0e_2-\delta^2T_2-\delta^3T_3$。
MC 的 raw mean 费用在该恒等式中继续存在。本篇只是对同一个高频未知量改用 $Q_0$ 作参考，故不需要把上述四种 selected 源分别送入高方程。它没有把 $b_0$ 与 canonical $s_0$ 混同。

## 3. 完整线性参考算子及非线性差

仍用 E.5 的实际 $b=\beta\sqrt K$、$g=GK^{1/4}$、$\alpha=\beta+K_r/(4K)$，
以及实际状态的 $a=-G\langle v\rangle\sqrt K$ 和 $d$。令
$$
 d_0=-bI_\phi(|W_0|^2).
$$
完整 reference 零阶算子为
$$
 \begin{split}
 \mathcal A_*u={}&\alpha Du
 -b\{|W_0|^2u+2W_0(W_0\cdot u)\}\\
 &-2bW_{0,\phi}I_\phi(W_0\cdot u)
       +g\langle u_2\rangle J_0W_{0,\phi}.
 \end{split}\tag{DB.6}
$$
最后一项是完整 principal mean 变分；不因使用高输出而在定义中删除。

由 E.13，存在准确算子 $\mathcal A(z_0)$ 使
$$
 (\partial_r-d\partial_\phi+aJ_0\partial_\phi)z_0
              =\mathcal A(z_0)z_0+P(f-f_0).
 \tag{DB.7}
$$
对任意测试输入 $u$，其差准确为
$$
 \begin{split}
 [\mathcal A(z_0)-\mathcal A_*]u
 ={}&-b\{(2W_0\cdot z_0+|z_0|^2)u+W_0(z_0\cdot u)\}\\
 &-bW_{0,\phi}I_\phi(z_0\cdot u),\\
 d-d_0={}&-bI_\phi(2W_0\cdot z_0+|z_0|^2).
 \end{split}\tag{DB.8}
$$
取真界 $|W_0|\le M_0$、$|W_{0,\phi}|\le M_1$、
$\|z_0\|_\infty\le\eta_0$。则可用
$$
 A_*=\alpha_++3b_+M_0^2+(b_+M_0/2+g_+)M_1,
$$
$$
 a_{\Delta,0}
  =b_+\eta_0(3M_0+\eta_0+M_1/4),\qquad
 d_{\Delta,0}
  =\frac{\pi}{8}b_+\eta_0(2M_0+\eta_0). \tag{DB.9}
$$
这里 $I:L^2\to L^2$ 的范数为 $1/4$；在 drift 的 $C^0$ 项用
$I=\partial_\phi^{-1}P_{\ne0}$ 的完整 sawtooth 卷积范数 $\pi/8$。
可将后一个常数安全宽为 $b_+\eta_0(2M_0+\eta_0)/2$。
所有范数在相同真径向窗上取值。

若已知的实际条件仍以 $Q_\delta$ 给出，
$\|Q-Q_\delta\|_{C^0,\oplus_1}\le\rho_w$，则只能使用
$$
 \eta_0\le p_+(\rho_w+19|\delta|),\qquad
 p_+=\sup_I\|P(r)\|. \tag{DB.10}
$$
或更尖的同一方向真界。不能把 $\eta_0$ 默认为 $p_+\rho_w$。
原已成 uniform-$\delta$ reference 标量包在 $\delta=0$ 也界住 $M_0,M_1$；
新的 (DB.9) 是正向费用公式，未在本篇登记新数值。

实际 principal $a,d$ 没有随参考改变。因此已经支付的同态
$a_-,d_+,L,c_p,c_r$ 可以保持；它们所依据的宽 $C^0$、完整负 mean 和普通残差 mean 假设仍必须成立。

## 4. 精确的 64 模作用范围

对任意完整 Fourier 输入 $u$，(DB.6) 各项的角支撑分别为：

| 项 | 输出支撑的增加 |
|---|---:|
| $\alpha Du$ | 0 |
| $|W_0|^2u$ 和 $W_0(W_0\cdot u)$ | 至多64 |
| $W_{0,\phi}I_\phi(W_0\cdot u)$ | 至多64 |
| $\langle u_2\rangle J_0W_{0,\phi}$ | 输出止于32 |
| $d_0\partial_\phi u$ | 至多64 |

primitive 先作用于完整积，保全部 signed modes；它既不增加频率，也不删除最终乘积产生的 mean。由此对每个整数 $J\ge64$，
$$
 H_J\mathcal A_*\Pi_{J-64}=0,\qquad
 H_Jd_0\partial_\phi\Pi_{J-64}=0. \tag{DB.11}
$$
在两个目标输出上特别得到
$$
 H_{96}\mathcal A_*\Pi_{32}
 =H_{96}d_0\partial_\phi\Pi_{32}=0,
$$
$$
 H_{288}\mathcal A_*\Pi_{224}
 =H_{288}d_0\partial_\phi\Pi_{224}=0. \tag{DB.12}
$$
这些是有限支撑恒等式，没有将未知状态截断。mean 属于被保留的低输入；它对 (DB.8) 的真实非线性差仍有作用。

## 5. 完整投影能量和两种新输入频带

对 $J\ge96$ 定义
$$
 z_A=\Pi_{J-64}z_0,\qquad
 z_S=(\Pi_J-\Pi_{J-64})z_0,\qquad
 z_H=H_Jz_0,
$$
$$
 Z_A=\|z_A\|_2,\quad Z_S=\|z_S\|_2,\quad Z_H=\|z_H\|_2,\quad
 Z_{\le J}=(Z_A^2+Z_S^2)^{1/2},\quad
 Z_0=(Z_A^2+Z_S^2+Z_H^2)^{1/2}. \tag{DB.13}
$$
每个范数都是完整 ordinary $L^2(dr\,d\phi)$，两个分量用同一个正交投影。

用 WC 的真实 triangular cutoff $\chi$，令
$C_{\chi,J}=\|\chi'H_Jz_0\|_2$，可宽为
$\kappa_\chi Z_H$，在原宽窗上 $\kappa_\chi=20$。
由 PE 的投影主部和 (DB.11) 精确得到
$$
 \begin{split}
 \mathcal L_{H_J}H_Jz_0={}&
 H_J\mathcal A_*(z_S+z_H)
 +H_J(\mathcal A(z_0)-\mathcal A_*)z_0\\
 &+H_J(d_0\partial_\phi z_S)
 +H_J((d-d_0)\partial_\phi\Pi_Jz_0)
 +H_JPf .
 \end{split}\tag{DB.14}
$$
实际高输入的 principal drift 保在 $\mathcal L_{H_J}$ 中，不另加已经由 PE 处理的 high-to-low 自交换子。

所以一个完整正预算是
$$
 \begin{split}
 E_J^{32}={}&\|H_JPf\|_2
       +(A_*+4Jd_{0,+})Z_S
       +(A_*+L)Z_H+C_{\chi,J}\\
 &+a_{\Delta,0}Z_0+4Jd_{\Delta,0}Z_{\le J}.
 \end{split}\tag{DB.15}
$$
$d_{0,+}$ 是同一完整 $d_0$ 的真界，也可在保留差费后使用已付更宽界。所有系数均为非负上界；这里没有相减两个独立数值预算。

将两个低量合并，合法但较宽的形式为
$$
 E_J^{32}\le\|H_JPf\|_2+
 (A_*+4Jd_{0,+})Z_S
 +(a_{\Delta,0}+4Jd_{\Delta,0})Z_{\le J}
 +(A_*+a_{\Delta,0}+L+\kappa_\chi)Z_H. \tag{DB.16}
$$
因此主要线性有限输入：

- 对 $J=96$ 只为 $33\le|j|\le96$；
- 对 $J=288$ 只为 $225\le|j|\le288$。

余下全部低频，包括 mean，只以 (DB.8) 的真实非线性系数继续进入；它们没有被删出问题。

## 6. 回到同一个 selected cut 和原 MA 高界

令 $p_c=\|P(c)^{-1}\|$，
$\kappa_J^{\rm ang}=\sqrt{1+[4(J+1)]^{-2}}$。
同 PE/WC 的完整两端 FTC 及实际能量给
$$
 V_J^{32}=p_c\sqrt{\kappa_J^{\rm ang}c_pc_r}\,E_J^{32},
 \qquad
 \|H_J(Q-Q_0)(c)\|_{H^{1/2}}\le V_J^{32}.
 \tag{DB.17}
$$
径向矩阵只付一次；cutoff 两侧属于同一状态。若两侧没有匹配，原 E.23 的 interface form 仍须保留。

由 (DB.3)，(DB.17) 同时界住 selected 差 $Q-Q_\delta$ 的两个高投影。若同一个状态在同一个 cut 满足 MA 五窄域之一，则
$$
 \|H_{288}(Q-Q_0)(c)\|_{H^{8193}}
 =\|H_{288}(Q-Q_\delta)(c)\|_{H^{8193}}
 \le2^{377903}. \tag{DB.18}
$$
不需要把整个 $Q-Q_0$ 强行放入一个更大的高阶球，也不额外增加 $Z_{\rm can}$ 的高范数。

这里精确引用 MA.7 的 selected-reference 差 $2^{377903}$，而非 MA.8 的完整 base-centre 差 $2^{377904}$。成功 receipt 的五个 `corrected_retained_cases` 中，`high_trace_conclusion.selected_reference_difference_bound_2_power_377903` 与 `base_centre_difference_bound_2_power_377904` 均保留；(DB.3) 使当前高投影直接消费前者。

设 $c_L=\|\Pi_{96}(Q-Q_\delta)(c)\|_{L^2}$，包含 full even mean。
于是
$$
 \begin{split}
 \|(Q-Q_\delta)(c)\|_{H^1}^2
 \le{}&\Lambda_{96}^2c_L^2+
       \Lambda_{288}(V_{96}^{32})^2\\
 &+2^{48}(V_{288}^{32})^{32768/16385},
 \qquad \Lambda_J=\sqrt{1+16J^2}.
 \end{split}\tag{DB.19}
$$
中间带只付 $\Lambda_{288}$，$2^{24}$ 仅在 far-band 插值中出现。
这是新的条件型三带迹公式；没有改写旧 LT/NR/WA 的成功科学数据。

## 7. 新 receiver 需要什么，现有 scalar 不能提供什么

要从原 finite193 Green 获取 (DB.16) 在左半
$I_-=[17/20,9/10]$ 的新输入，需要一个真正的新输出
$$
 {\cal R}_{33:96}h
   ={\bf1}_{I_-}(r)P(r)(\Pi_{96}-\Pi_{32})h(r)
       \in L^2_{r,\phi}. \tag{DB.20}
$$
$h$ 是原 unscaled moving 两分量；不能再次除原 even weight、乘 amplitude $\alpha$，或把物理角 curvature 的97维输入直接当此输出。

普通 body-source Green、真正97维右 Poisson，以及 specialized high-to-low 源的输入空间不同。若分别记为
$\mathcal G,\mathcal P,\mathcal A_{\rm HL}$，所需的是
${\cal R}_{33:96}\mathcal G$、
${\cal R}_{33:96}\mathcal P$、
${\cal R}_{33:96}\mathcal A_{\rm HL}$ 的各自完整证书。
普通输入仍在原完整 $[0,9/10]$，只有输出被 restriction；
不能把特殊 $a_Y$ 当普通 $g_Y$。

新输出可以使用同一次 Green 运行中仍在临时区的完整因子。抽象地，若原 native 状态为 $y$，准确 raw 恢复为 $h=N_{\rm raw}(r)y$，则应使用正矩阵
$$
 J_{33:96}(r)=
 N_{\rm raw}(r)^*P(r)^*
       (\Pi_{96}-\Pi_{32})P(r)N_{\rm raw}(r). \tag{DB.21}
$$
将这个矩阵放在原真实 $dr$ 积分和同一个完整误差证明中，是一个新的 receiver。它不要求重新计算 target 或原 Riccati/Green 动力学，但必须保原 selected-product/roundoff/defect 和 posterior 转授费用。

当前 active Green 的原 producer 只保存既定三类输出的 input-side Gram，未保存局部 $F(r)$ 的完整系数；传播矩阵虽保留，也不足以重建新的局部输出 Gram。原运行没有 receiver hook，本篇不修改该 frozen child。因此当前资料尚缺一个独立合法的局部 $J_{I,\mathrm{band}}$；不能称本轮已经具备或能够直接提取 (DB.20) 的新分带输出。

若只留下已经收缩成输入矩阵的 $\int Y^*J_{\rm full}Y\,dr$ 或最终 scalar norm，一般不能从中恢复
$\int Y^*J_{33:96}Y\,dr$。必须仍有原未丢输出坐标的 $Y$ 因子，或此前已经保存相应带内 covariance。至多可沿有界投影给旧 whole norm 乘 $p_+$ 的保守界；不能因此声称获得了更小中带 norm。

对于 (DB.13) 中的原参考差，应在这个新 receiver 之后保准确 affine 项
$$
 (\Pi_{96}-\Pi_{32})z_0
 =(\Pi_{96}-\Pi_{32})z_\delta
       +\delta P(\Pi_{96}-\Pi_{32})Z_{\rm can}. \tag{DB.22}
$$
它若使用标量 triangle，就必须另有同一径向窗的完整 canonical 方向界。仅有 cut 系数并不给 body 界。全角 coarse $\|Z_{\rm can}\|_{A_0}<19$ 可作合法 fallback，但不能假装它已是尖的 shell 积分。

右半 $[9/10,19/20]$ 依然需要同一个真正匹配帽状态的 receiver。原 Green 的 body 区间只到 $9/10$，不能无费延长。$225\le|j|\le288$ 也不是原 finite193 的输出，须由真正 high 方程/帽 receiver 另付。本文没有把这两个缺项留在符号外后宣布完整闭合。

## 8. 数值及全局 scope

本文只证明 (DB.3)--(DB.19) 和新 receiver 的准确类型。原 source 支撑、canonical 连续方向、完整 mean、实际 metric 及角规范保持不变。没有新数学数值运行，也没有覆写原91例、MA五例、NR/WA表或其 actual verdict。

一个后继公共消费者可只读取旧已成 coefficient 包，按 (DB.9)、(DB.15) 正向组合新系数；另一个新的 Green receiver 必须由 (DB.21) 所述完整因子支付真实数据。两者都不能把未知带内范数设为0。近似态必须保 (DB.5) 的 ordinary high residual 和 E.7 的 residual mean；真解才可使用它们为0的专门化。

core 存在、两侧同态匹配、选中参数与完整 mean 行、窄 MA 条件及最终低物理 $\gamma$ 自映像仍按原合同逐项关闭。
