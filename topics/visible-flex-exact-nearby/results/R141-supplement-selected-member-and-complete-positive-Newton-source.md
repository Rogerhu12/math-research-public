# R141 补篇：同一选定成员与完整正区 Newton 普通源

2026-11-20，visible-exact-astra-ac637-20261120 / positive_inverse。

**已证明：** 下述同成员限制、完整旧核心源的复用以及新外尾源的逐格计算公式。配套纯数学模块可直接由独立公共消费者调用。**尚未执行：** 本篇七个新有向标量。没有重新计算任何已成功的旧残差、核心限制、方向源、系数、Green 或逆目标，也没有把一个导数范数改名为实际右端。

## N1. 要接的是哪个成员

固定同一物理内禀参数 $\eta_0$，以及

$$
Q_\delta=Q_0+\delta Z,\qquad
\nu_\delta=\nu_0+\delta,\qquad
\operatorname{SHA}(Q_0)=
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47,
$$

$$
\operatorname{SHA}(Z)=
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.
\tag{N.1}
$$

下表给出旧证明和实际输入清单的准确参数范围。

| 对象 | 已定义或已成的范围 | 与本篇的关系 |
|---|---|---|
| R141 low193 中心 | 同一 $|\delta|\le10^{-8}$ 上的 $A_L^c[\eta_\delta]$；其有向逆门须由自己的实际结果决定 | principal 保留 $\eta_\delta=-\gamma m_\delta$，lower coefficients 是 repaired degree32 centre |
| 已成低族差 $L$ 三量 | 同一 $|\delta|\le10^{-8}$，实际 $A_L(Q_\delta)-A_L^c[\eta_\delta]$，完整 mean 与193观察 | 加回此差才恢复真实低块；不能将 hybrid 本身当作 $DF(Q_0)$ |
| 真实 $G_H$ 与已成五源、加权响应 | 同 repair/direction、固定物理 $\eta_0$，$|\delta|\le10^{-8}$ | 原正区 bump 为零，故固定原 $\nu_0$ 的正区算子也正是 $\nu_\delta$ 的正区算子 |
| WOBSA run43844596176/1 | 原选定成员及其同一 frozen input normalization | 本篇不将它提升为全族 KAM 或全族观察定理 |
| CRA run43757468943/1 | 同一 $|\delta|\le10^{-10}$ 的整个 $[0,9/10]$ | 已付完整普通 $f_\delta$，包含 bump、独立 mean、centre/direction repair 与参数余项 |
| 完整7721方向源 run43613560173/1 | $\delta=0$ 时的 $s_0$，整个 $[0,25/8]$ | 它是精确参数展开的线性系数，单独不等于 $f_{\delta_*}$ |

前两行的实际清单均保留 exact real direction radius $1/100000000$，actual eta is the same full-family function in A and Ac；参见 [R141 主篇](R141-low193-directed-green-and-complete-observation-certification.md)、[已成低族差](R139-supplement-actual-complete-low-family-budget.md)及 [真实高源合同 H1–H5](R141-supplement-actual-GH-source-window-and-return-contract.md)。这里的 full real delta 不等于原内禀参数的整区间；原清单的 whole original intrinsic parameter family remains false。

[NIF.1–4](R133-supplement-uniform-frozen-selected-input-coordinates-for-the-real-reference-family.md) 指定的是 public run43588332723/1、loss $1/250$ 给出的同一对 $(\delta_*,\mathcal H_*)$，并已证明

$$
|\delta_*|<9.368259853002\,10^{-11}
       <d:=10^{-10}<10^{-8}.
\tag{N.2}
$$

因此最小同成员桥就是把所有上述 uniform bounds 限制到 $\delta_*$。没有把 $\delta_*$ 设为 $0$ 或 $10^{-10}$，也不需要另做一个 $A_0$ 到 $A_{\delta_*}$ 的逆运输。WOBSA 的 selected chart 仍是该选定对的原 chart。有关真正 $DF(Q_\delta)$ 的后继结论仍须完整消费低族差、高返回和实际物理外行，不能仅据范围相同宣布逆已经闭合。

本篇的七个新量统一覆盖 $|\delta|\le d$，因而可用于这个同一 $\delta_*$。物理角重建、实际 $\Theta$、物理 mean、height 和 $\nu$ 外行没有改名或消失。

## N2. 已成的整个核心源，直接限制到真根

记

$$
I=[r_*,R],\quad L=9/10,\quad R=25/8,\qquad
f_\delta=(Q_\delta)_r-\mathcal F(Q_\delta,\nu_\delta).
\tag{N.3}
$$

普通范数为 $L^2(dr;L^2_\phi)$，角测度是原归一化 moving circle。$\Pi_{96}$ 包含96 odd、96 nonmean even 与独立 even mean；$P_H=1-\Pi_{96}$。

[完整核心实际结果 CRA](R133-supplement-actual-complete-core-residual-restriction-and-selected-ordinary-source.md) 已经保存以下三个完整输入。下面字段都在其 actual scientific conclusion 中，逐球读回，不重新调用 RF 或 CRA producer：

| 记号 | 原完整字段 |
|---|---|
| $C_{\rm full}$ | complete_selected_source_conclusion.complete_background_choices.new_core_restriction.uniform_selected_full_L2_upper |
| $C_{\rm low}$ | 同一 choice 的 uniform_selected_low193_L2_upper |
| $C_{\rm quad}$ | complete_selected_source_conclusion.complete_quadratic_source_contribution |

其准确资格是

$$
\|f_\delta\|_{[0,L]}\le C_{\rm full},\qquad
\|\Pi_{96}f_\delta\|_{[0,L]}\le C_{\rm low},
\tag{N.4}
$$

$$
\|f_\delta-f_0+\delta s_0\|_{[0,L]}
\le C_{\rm quad},\qquad |\delta|\le d,
\tag{N.5}
$$

其中

$$
s_0=\mathcal F_\nu(Q_0,\nu_0)-(\partial_r-A_0)Z.
$$

(N.5) 是原 RF.14 的完整余项：$C_{\rm quad}$ 已实际计算为 $dD_{\rm core}/2$。它包含核心内的真实内禀参数变化，不能解释成一个仅在 bump 外成立的三次多项式近似。

已知 $0<r_*<L$，所以径向限制的范数不增。(N.4)–(N.5) 直接覆盖 $[r_*,L]$，包括真根 germ 与所有原核心分格；无需将下端改成 root midpoint，无需重新做任何 germ 源积分，也不从旧 global upper 减去 core upper。核心内 mean 和连续修补已全付，不再添加第二次 raw-mean 或 $384E_Z$ 费用。

## N3. 唯一新的原始残差限制在 $[L,R]$

原7296行完整残差 native 为
6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1。
其每行都保存整闭格的 complete_residual_A0.U 和 .V，完整 primitive 与 even mean 已保留，已成的旧全域积分和旧核心积分不重算。

对原格 $J_i$，取准确的 $J_i^+=J_i\cap[L,R]$。只在非空交段计算新的尾端量

$$
F_{\rm raw}^+
=|\alpha|\left[
\sum_i |J_i^+|\{(R_{U,i})^2+(R_{V,i})^2\}
\right]^{1/2},\qquad
\alpha=\frac{6890507429876859}{9007199254740992}.
\tag{N.6}
$$

完整的两分量上界先平方相加。振幅只乘一次；$Z$ 已是物理方向，不乘 $\alpha$。这里使用旧闭格 supremum 乘真实交段长度，没有按长度比缩放一个旧已积分球，也没有重算任何旧 row 的残差。

## N4. 新尾端完整 centre repair 费

只读原4650行完整 positive coefficient native
ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d。
一行给出原 raw physical moving centre 的
$U,V,U_1,V_1$ 与有符号 $\beta,\gamma,K$ 包围。$\nu$ bump 支持在 $[1/20,9/50]$，所以 $[L,R]$ 上所有内禀系数对于 $\nu_\delta$ 完全相同。

精确连续修补的完整 pair 界保留为

$$
E_{Q0}=3.861\,10^{-18},\qquad E_{Q1}=1.970\,10^{-17}.
\tag{N.7}
$$

第二个是 inhomogeneous $A^1$ 上界，故也控制角导。原修补在每原径向 piece 是常数，其径向导数几乎处处为零；全部6143值跳精确相消。ordinary residual 改变量因此是完整场差 $\mathcal F(Q+e)-\mathcal F(Q)$，没有遗漏一个 interface Dirac。

在整个 raw-to-repaired 仿射线段上取

$$
q_0=U+V+E_{Q0},\quad q_1=U_1+V_1+E_{Q1},\quad
b=|\beta|\max(1,|K|),\quad g=|\gamma|\max(1,|K|).
\tag{N.8}
$$

将原场逐项微分，使用已定 primitive 范数 $1/4$，得到

$$
c_0=b(1+3q_0^2+q_0q_1/2)+gq_1,\qquad
c_1=bq_0^2/4+gq_0,
\tag{N.9}
$$

$$
\|D\mathcal F(Q)h\|_{A^0,\mathrm{pair}}
\le c_0\|h\|_{A^0,\mathrm{pair}}
   +c_1\|h_\phi\|_{A^0,\mathrm{pair}}.
\tag{N.10}
$$

$gq_1$ 正是完整方向 mean-rank 的费用；$gq_0$ 控制 principal mean。$bq_0q_1/2$ 来自 primitive 系数的变化。它们都没有删除。

于是该行的修补残差上界是 $e_Q=c_0E_{Q0}+c_1E_{Q1}$。在每个 coefficient 闭格 $K_j$ 上保持整个旧 enclosure，只裁剪积分域，计算

$$
E_{\rm rep}^+
=\left[\sum_j |K_j\cap[L,R]|\,e_{Q,j}^{\,2}\right]^{1/2}.
\tag{N.11}
$$

这是一条新的尾端 scalar，未重新求原修补系数、whole primitive 或任何已成 RF 系数。两个原分格不必相同：(N.6) 和 (N.11) 分别覆盖同一个完整尾区，然后用三角不等式。

## N5. 用已成方向幅度界形成新二/三次尾余项

full-delta body run43615531666/1 已在完整 summary 保存
complete_delta_input_bounds.A0 与 .angular_A0。它们的原源码逐格准确使用

$$
e_0^{(8)}=10^{-8}(H_0+E_Z),\qquad
e_1^{(8)}=10^{-8}(H_1+E_{Z,\phi}),
\tag{N.12}
$$

然后对全4650格取最大值。原 $H_0$ 含非负 mean-completion 包络，因此控制 raw direction；完整 direction 的常值修补另外已在 $E_Z$ 中相加。centre repair 是原 large M32 部分，不在这两个缩放量中。

设 $M_k$ 是同一个 $Z$ 在完整 body 上的第 $k$ 个实际范数 supremum。原保存量 $E_k^{(8)}$ 满足 $E_k^{(8)}\ge10^{-8}M_k$；对每一个 $|\delta|\le d$ 都有 $|\delta|M_k\le(d/10^{-8})E_k^{(8)}$。这只使用方向对参数的线性齐次性，未假设 interval enclosure 是某个参数点的值。

所以两个已保存 global upper 可以**精确乘 $d/10^{-8}=1/100$**，得到同一 $|\delta|\le d$ 下

$$
\|\delta Z\|_{A^0,\mathrm{pair}}\le e_0,\qquad
\|(\delta Z)_\phi\|_{A^0,\mathrm{pair}}\le e_1
\quad\hbox{在整个 }[L,R].
\tag{N.13}
$$

这既不从任意 operator upper 反推出方向大小，也不缩放 centre repair。独立 mean 满足 $|\langle\delta\zeta\rangle|\le e_0$，不是零。

在 bump 外，原 [R.15–R.18](R133-supplement-selected-centre-complete-residual-and-collar-source-bounds.md) 是精确三次恒等式。用 (N.8) 的同一个 repaired-centre 包围，其完整非线性余项受

$$
\begin{split}
n_j={}&b\{e_0^2q_1/4+q_0e_0e_1/2+3q_0e_0^2
                      +e_0^2e_1/4+e_0^3\}
       +g e_0e_1 .
\end{split}
\tag{N.14}
$$

其中最后一项是 principal mean 的二次项。求和先保留同一行二次和三次项的相关性，再取

$$
N^+
=\left[\sum_j |K_j\cap[L,R]|\,n_j^2\right]^{1/2}.
\tag{N.15}
$$

因而

$$
\|f_\delta-f_0+\delta s_0\|_{[L,R]}\le N^+.
\tag{N.16}
$$

这里未将有限 known source 的 angular support 授给未知高解。没有对任一 forcing 求径向导数。

## N6. 七个新输出与原样保存规则

从原7721完整 finish summary 只读三球

$$
S_{\rm full}=\|s_0\|_{[0,R]}\ \hbox{的已存上界},\quad
S_{\rm low}=\|\Pi_{96}s_0\|_{[0,R]}\ \hbox{的已存上界},\quad
S_{\rm high}=\|P_Hs_0\|_{[0,R]}\ \hbox{的已存上界}.
\tag{N.17}
$$

其 fields 是 complete_source_bounds.full_body 下
full_through160、low193、high97_through160 的 L2_L2_radial。
三个都是已含 full raw mean 与两次连续修补的真实 ordinary source；可以径向限制，不能由 whole upper 减去 inner upper。

先定义

$$
F_{\rm tail}=F_{\rm raw}^++E_{\rm rep}^++dS_{\rm full}+N^+,\qquad
F_{\rm tail,low}=F_{\rm raw}^++E_{\rm rep}^++dS_{\rm low}+N^+.
\tag{N.18}
$$

完整正区 full、low 两界分别为

$$
F_+=\sqrt{C_{\rm full}^2+F_{\rm tail}^2},\qquad
F_{+,L}=\sqrt{C_{\rm low}^2+F_{\rm tail,low}^2}.
\tag{N.19}
$$

两个径向区间的输出正交，但每区间内不同来源只用了三角式，没有把同输入产生的输出说成独立。

完整 centre 和修补 degree32，所以其 ordinary $f_0$ 精确到 quarter-index96。由 (N.5)、(N.16) 和原 $s_0$ high 行，

$$
\boxed{\displaystyle
\|P_H f_\delta\|_{[r_*,R]}
\le F_{+,H}:=dS_{\rm high}+\sqrt{C_{\rm quad}^2+(N^+)^2}.}
\tag{N.20}
$$

这里线性项在全正区只计一次；核心与尾端的余项径向直和。$P_Hf_\delta$ 的 known source support 至288，完整 even mean 则留在 low193 中。不得把 (N.20) 改成零，也不得把大小约 $10^{-8}$ 的低背景 residual 当作实际 high source 的必要大小。

七条保存记录按下列顺序，全部都是新目标：

1. new_outer_tail_raw_physical_residual_L2_upper，(N.6)；
2. new_outer_tail_continuous_centre_repair_L2_upper，(N.11)；
3. new_outer_tail_selected_nonlinear_remainder_L2_upper，(N.15)；
4. complete_outer_tail_selected_Newton_full_L2_upper，(N.18)；
5. complete_positive_selected_Newton_full_L2_upper，(N.19) 第一式；
6. complete_positive_selected_Newton_low193_L2_upper，(N.19) 第二式；
7. complete_positive_selected_Newton_high97_through288_L2_upper，(N.20)。

每个结果先完整写入、读回并证明 saved interval contains original directed upper；后继只取读回 upper。尤其第五条使用已保存第四条，而不是未保存的内部临时值。第一到第三条也在后续组合前保存、读回。新平方根的非负对象使用已证明非负的 directed upper 点，不能因 Arb 区间的表示跨零而把失败隐藏成零。

程序准入保存 whole CRA actual/execution、whole7721 summary/process、whole full-delta body summary/process、WOBSA 和 NIF 的完整文件身份及 scope。原7296/4650行全部校验区间与原接口后，仅在新尾区求新标量；新交段计数从完整元数据生成并保存。没有原 producer 导入、旧目标运行、旧均值积分、重新插值或旧积分相减。

## N7. 真正得到的源与仍独立的边界行

若本消费者实际完整成功，七量给出同 $\delta_*$ 的 ordinary Newton 源 $-f_{\delta_*}$ 的完整 full/low/high 大小。符号对 norm 无影响；实际 source-pair 组装仍须采用 [完整物理两行合同](R141-supplement-actual-physical-source-pairs-and-reusable-bounds.md) 的 signed $F,e$。

特别是它没有自动提供 root-even input、negative/germ return 数据、独立 affine jumps、外端 height、真实 Robin residual 或 physical mean residual。已成 CRA core 只被用作 known source 的径向限制，不是一个负侧逆或 negative solution。修补的值连续性只消掉本 known reference 的 value jumps；任意未知 interface datum 仍单列。

S19 的实际 Newton 外端两残差依然是

$$
r_B=-[J_\theta B_\delta+Q_\theta\mathcal Z_\delta
-\mathfrak d(\mathcal Z_\delta,f_B)],\qquad
r_C=-[m_\delta(R)-1-C_{\rm ref}
-\mathfrak c_0(\mathcal Z_\delta,f_B)].
\tag{N.21}
$$

本篇不把 exterior derivative rows、背景半径、或 $\nu$ 的显式零方向当作 (N.21) 的实际值。所有 future224、future32、物理外门、两 WPN RHS、全逆和 nonlinear existence 标志仍保持未付。新的完整普通源只关闭它自己的 source-size 义务。
