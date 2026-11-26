# R147 补篇：同一固定负窗的完整 selected ν 源与实际腰贡献

2026-11-26，visible-exact-astra-198c63d-20261126 / correlated_energy。

本篇规定一个可立即运行的独立小 scalar target：从完整已成的 $s_0$、D 的真实负窗差源和 SP/PW receiver，支付同 selected 成员的完整 ordinary $\nu$-proposal 源到原腰密度的贡献。它不等待 R142、positive58/224/32，也不重复这些目标。R147 本身是解析转授证明，没有被虚构成一个旧 actual/execution。

## NW1. 新输入比旧保守转授更具体

保持 [R147 NM.1–NM.5](R147-selected-negative-nu-source-and-complete-mean-row.md) 的
$$
s_\delta=F_\nu(Q_\delta,\nu_\delta)-(\partial_r-A_\delta)Z,\qquad
I_N=[0,R_N],\quad R_N=\frac{2383968743003}{10^{13}},
$$
$$
Q_\delta=Q_0+\delta Z,\quad \nu_\delta=\nu_0+\delta,\quad
\eta=\eta_0,\quad d=10^{-10}.
\tag{NW.1}
$$
所有源是 ordinary $L^2(dr;L^2_\phi)$ 的完整 moving pair，原 normalized measure、independent even mean、全部 repair 和 parameter bump 均保留。正参数源约定与 $q_\nu-Z$ 相同；本篇不宣称该完整 BVP 响应已经存在。

run43613560173/1 的完整 finish summary 和 process 同时保存
$$
S_G=\texttt{complete\_source\_bounds.full\_body.full\_through160.L2\_L2\_radial},
$$
$$
S_N=\texttt{complete\_source\_bounds.fixed\_negative\_phase\_window.full\_through160.L2\_L2\_radial}.
\tag{NW.2}
$$
它们分别支配 $\|s_0\|_{[0,25/8]}$ 和 $\|s_0\|_{I_N}$。这里第二条是原 Z 合同 Z.6–Z.7 已完成的独立积分，不是从 global upper 中减去另一个 upper。实际 identifying sizes 为约 $2.7258614\,10^{-6}$ 和 $3.1258755\,10^{-7}$，输入始终读取完整原球，而不是这些显示缩写。使用的是 full 列，不能改用 low193 或 known-high 列。

同原 run43713242980/1 的
$$
D_N=\texttt{complete\_scalar\_fee\_conclusions.fixed\_negative\_window.ordinary\_L2\_bounds.complete\_additional\_response\_source}
\tag{NW.3}
$$
对完全相同的 $I_N$ 控制 $\Delta F_\nu+\Delta A\,Z$。原完整实参数正预算给
$$
\|s_\delta-s_0\|_{I_N}\le (|\delta|/d)D_N,\qquad |\delta|\le d .
\tag{NW.4}
$$
这里微分/缩放的是 D 的原显式正项公式，继而径向积分；没有对一个已保存的 residual upper 求导。

同 selected pair 是原 run43588332723/1、loss $1/250$，由 W/NIF/R141 N.2，
$$
|\delta_*|/d<0.9368259853002<\tau:=936826/10^6<1.
\tag{NW.5}
$$
所以两个完整合法新组合为
$$
F_G=S_G+\tau D_N,\qquad F_N=S_N+\tau D_N,\qquad
\|s_{\delta_*}\|_{I_N}\le F_N.
\tag{NW.6}
$$
$F_G$ 保留 R147 原 global-to-window 转授并应仍严格小于
$3.720478\,10^{-6}$；$F_N$ 是本次新同窗加强。旧 R147 的严格有理结论不被抹掉。

原 Z 合同警告不能将 $\delta=0$ 的 phase-window 积分直接改称改变背景后的源。本篇没有这样做：同一个固定物理区间 $I_N$ 上使用 (NW.4) 的完整差源，再按 (NW.6) 三角相加。真实 root 与 SP/PW 的 fixed cut 仍由原全族 Cauchy 的两端 bracket 包含于 $I_N$；metric bump 在 root 邻域为零，原真 root 并未被替换为 numeric midpoint。若窗口、参数、centre、direction 或原 norm 任一身份不匹配，消费者停止并保留真实失败。

## NW2. 完整二源域到腰部的一条真实贡献

[R149 SC2](R149-supplement-signed-finite-columns-and-full-negative-residual-sources.md) 已证明：原 E.12 完整 isotropic ordinary pair（以及 E.6 的较强 anisotropic pair）经同 N/SP 组合，仍由原保存的 $C_O,C_2$ 接收。第二非均值源和两 physical-density means 都保留。原 PW 的 constant-second 字段不被修改。

将同一 $s_{\delta_*}$ 限制到两个不交区间
$$
[0,r_c]\quad\hbox{和}\quad[r_c,r_*],
\qquad r_c=r_+-1/200.
$$
两个 ordinary 输入 norm 的平方和不超过 $F_N^2$。因此对负侧零 root 数据、零独立 impulses 的这个 ordinary-source 部分，其真腰密度贡献满足
$$
\boxed{\quad
D_{\nu,N}^{\rm ordinary}
 \le G_NF_N,\qquad
G_N=\sqrt{C_O^2+C_2^2}.
\quad}
\tag{NW.7}
$$
角向 $H^{-2/3}$、$H^{-1}$ norm 均不超过 normalized $L^2$ pair norm。这里的平方和来自同一源的径向限制；没有假定两个输出解正交。

输出是原完整 $\mathcal Y_0=(Iw(0),\Pi w(0))$，$w=n_gT(q)h$，包含两个物理 mean。未应用 actual principal-angle 或 incoming normalization；这些另有原有序 receiver。独立 root trace、positive 回传、germ/interface/height/Robin/mean/phase 源和真正 incoming inverse 均不包含在 (NW.7)。零 root/impulse 只定义这一线性分量，不能传给整个实际 $\nu$ 修正。

## NW3. 一个新完整目标与不可重复的旧输入

新 kind 为
`R147_complete_selected_negative_nu_ordinary_to_waist_v1`。
唯一目标按顺序保存四条完整有向记录：

1. `selected_negative_source_from_original_whole_body_upper`，$F_G$；
2. `selected_negative_source_from_same_fixed_window_upper`，$F_N$；
3. `complete_negative_ordinary_L2_to_waist_density_gain_upper`，$G_N$；
4. `selected_negative_nu_ordinary_to_waist_density_upper`，使用第2和第3条已经完整写入/读回的 upper 的乘积。

新脚本逐字读取完整 S0 summary/process/manifest、D execution/manifest、SP execution/manifest、PW execution/manifest，以及全部相关解析资格。D、SP、PW 的 scientific object 本来嵌在其完整 execution 中，不另造一个不存在的 science 文件。每个旧 result 的全部门、真实 run/attempt/source、完整 family/interval/mean 和 scope 同时核对；SP 的四个原 gain record 与 PW 的 literal copies 必须相等。新 actual 以 whole file receipts 和明确 JSON 路径引用旧球，并保留输入 full-window 与 global-window 的区别。

科学 import 前完成完整 metadata admission。Arb 只运行上述新 selected-plus-receiver 标量；无旧径向积分、coefficient、Green、source producer、Cauchy growth 或 strict matrix product 调用。所有新记录先整球保存、完整读回并验证包含原 directed upper，再用于后续计算；没有用显示 midpoint 或前缀补零。

科学仅在本公开仓库 Actions，固定 Python3.12.14、python-flint0.9.0、320bits。独立 public worker 使用原 small scalar 的完整输入、README pull/diff、200MB容量与非FF立即 rebase/push 循环；不会由 marker 或未来定义冒充一次 actual success。公开输出保存四条完整球和资格，内部临时材料不上传为数组/Release/大 artifact。失败仍保存实际已成前缀、完整异常身份和真实 child return code。

本篇自身是新的证明与运行入口定义。只有真实公共执行全部四条完成以后，才能登记该 ordinary 负侧腰贡献实际已付；完整 $\nu$ 响应误差、负侧 incoming/phase Schur、非线性闭曲面均保持未完成。
