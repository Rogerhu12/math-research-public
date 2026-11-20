# R137 补篇：同一主部提升的连续逆到原有限核心之桥

2026-11-20，`visible-exact-astra-ac637-20261120 / joint_kernel`。

**已证明的条件性定理。** 对 R137 的完整连续中心算子，若已经取得其真正的有界逆，原有 4,724,833 维有限中心核心还需一个明确的径向投影缺陷。本篇证明该缺陷有一个原细胞长度因子，给出直接 signed 目标及保留全部 source 的充分上界。它不要求连续中心的范数小于一，也不把连续可逆自动转授给有限压缩。

本篇没有执行任何新的数值目标，没有宣告下文的连续逆或有限严格门已成立。已有 WVC normalizer 的完整成功记录只读引用；已有 mean-floor 结论对旧 small-centre 配方的排除不被改写为算子奇异。

## 1. 固定原来的两个空间、投影和 193 个原子

采用 [R137 主篇](R137-continuous-signed-centre-and-exact-endpoint-system.md) (S.16a) 的准确 Hilbert 空间
$$
\mathscr Z=\mathscr H\oplus\mathbb R^{97}_d
                    \oplus\mathbb R^{96}_{\widehat b},
\qquad
\mathscr H=L^2(I;E_L)_{\widetilde a=Sa},\quad I=[r_*,25/8].
\tag{F.1}
$$
这里 $E_L$ 是原 normalized real odd96、独立 even mean1、even96 的 193 维空间；径向测度是普通 $dr$，角测度与原式相同。外端坐标仍是
$\widehat b_j=(1+16j^2)^{-5/12}b_j$。原子输入不是对任意 $L^2$ 函数取端点值。

原 WIC/WVC 网格有 $N=24480=153\cdot160$ 个细胞。令其真长度为 $h_i>0$，$S_i$ 是原继承的细胞常量变换，含完整 even mean 的缩放。$E_N$ 是 normalized cell-constant isometry，$\Pi=E_NE_N^*$ 是普通细胞平均。准确的有限投影为
$$
P_f(\widetilde a,d,\widehat b)
       =(E_N^*\widetilde a,d,\widehat b),\qquad \|P_f\|=1.
\tag{F.2}
$$
因此
$$
X_f=\mathbb R^{193N}\oplus\mathbb R^{97}\oplus\mathbb R^{96},
\qquad \dim X_f=193N+193=4724833.
\tag{F.3}
$$
源计算中的 155 个 comparison panels，以及 R141 认证内部插入的 1424 个或更多节点，都不是这里的有限网格。不能把它们的长度代入本篇的 $h_i$。每个 $h_i$ 是原 parent 真长度除以 160；根 collar 的端点仍是实际 $r_*$ 的准确 affine 函数，绝不以根区间中点替换。

以下固定同一个参数成员。若所需系数与算子界在原参数域一致成立，逐成员的准确恒等式即给同域一致结论。

## 2. 原 $W_D$ 确实是保持细胞平均的齐次主部提升

用 $D_i$ 表示 WVC 已选的低频 tracefree reference generator；它包含原 clipped diagonal，reference mean 为零。原变换满足
$$
\widetilde D_i=S_iD_iS_i^{-1}=\widetilde D_i^*.
\tag{F.4}
$$
非零角模式的谱是 $\pm\Omega_{ij}$。这正是 [WVC](R133-supplement-continuous-repaired-centre-trials-and-clipped-tracefree-reference.md) (WVC.37)--(WVC.39) 所使用的 self-adjoint reference；并未改成实际 $A_{Lc}$。

[WIC](R133-supplement-analytic-inherited-tail-and-weighted-impedance-circuit.md) (WIC.31)--(WIC.34) 给
$$
Z=Z_D\operatorname{pr}_u,\qquad
W_D(u,d,\widehat b)=(E_Nu-Z_Du,d,\widehat b).
\tag{F.5}
$$
尤其 $Z$ 的 body 不依赖 $d,\widehat b$。这不是一个省略 boundary columns 的约定：主部 tail equation 对这两个有限输入的列本来就为零，(WIC.33) 已完整陈述此事实。

为核清其局部意义，在一个 $\widetilde D_i$ 的正交特征方向写特征值为 $\lambda$，细胞左端移到 $t=0$。由 (WIC.31)，
$$
\begin{split}
(W_Du)_i(t)&=\ell_{i,\lambda}(t)\frac{u_i}{\sqrt{h_i}},\\
\ell_{i,\lambda}(t)&=
\frac{h_i\lambda e^{\lambda t}}{e^{\lambda h_i}-1}
\quad(\lambda\ne0),
\qquad \ell_{i,0}(t)=1.
\end{split}
\tag{F.6}
$$
它满足 $\ell'=\lambda\ell$ 及 $h_i^{-1}\int_0^{h_i}\ell=1$。反过来，一个齐次解的平均唯一确定它，因为实数 $\lambda$ 的指数平均严格为正。用 (F.4) 的正交 spectral decomposition，即得整个 193 维细胞的同一结论，包括 $\lambda=0$ 的 mean 和 zero-reference collar 分支。

故 $W_D$ 的 body 在每个细胞内恰为具有指定 transformed mean 的齐次 $D_i$ 解，并且
$$
P_fW_D=I_{X_f}.
\tag{F.7}
$$
这些 cell profiles 一般在细胞边界有跳。$W_D$ 的两个原子块独立地等于输入 $d,\widehat b$，不被宣称等于这些 profiles 的裸端点值。$W_D$ 是原 Schur 提升，不是一个任意数据下自动拼成连续全局 reference solution 的操作。

由于 $E_Nu\perp Z_Du$，
$$
\|W_D\|^2=1+\|Z_D\|^2.
$$
WVC (WVC.38)--(WVC.39) 对**同一 reference、同一细胞和同一 $S$** 已证明
$$
\|Z_D\|^2<5/12,
\qquad \boxed{\ \|W_D\|<\sqrt{17/12}<6/5.\ }
\tag{F.8}
$$
完整 atom identity 不增加这里的上界，因为它与 body lift 作用于正交输入块。该 $6/5$ 是已有解析定理，不是本篇重新评估的数值对象。

## 3. 消去齐次提升后，普通 source 有真正的 $h_i/\pi$ 因子

定义有界斜投影
$$
Q_D=I_{\mathscr Z}-W_DP_f.
\tag{F.9}
$$
由 (F.7) 得 $Q_D^2=Q_D$、$P_fQ_D=0$，且其 range 正是 $\ker P_f$。这里没有假设 $Q_D$ 正交或 $\|Q_D\|\le1$。

令 $G_D$ 是原 reference 的完整 raw ordinary-source Green map，$\mathcal O_D$ 给出 $S$ 倍 body、97 个 root-complement 和 96 个带原 Riesz 权重的 outer observations。对任意普通 source $f\in L^2(I;E_L)$，置
$$
x=\mathcal O_DG_Df,\qquad y=Q_Dx.
\tag{F.10}
$$
因为 $W_D$ 原样保留两个 atom 块，$y$ 的 **193 个 atom entries 全部恰为零**。其 body 在每个细胞平均为零，且为 $H^1$。$G_Df$ 满足原 reference source equation；(F.6) 的减项是齐次解，所以细胞内部准确有
$$
y_i'=\widetilde D_i y_i+S_if,
\qquad \Pi_i y_i=0.
\tag{F.11}
$$
没有对任意 $L^2$ 输入求导，也没有在细胞拼接处丢弃一个 source impulse。这里使用的只是各细胞内部等式；$y$ 的人工 profile jumps 不被改写为全局齐次传递条件。

令 $V_if(t)=\int_0^t f(s)\,ds$、$Q_i=I-\Pi_i$，并沿用 [WPT](R133-supplement-cellwise-principal-inverses-and-dual-radial-head-tail.md) (WPT.5) 的
$\mathcal B_i=Q_iV_iQ_i$。对 (F.11) 积分并减去平均，因 $\widetilde D_i$ 为常量且 $y_i$ 平均为零，得到
$$
(I-\mathcal B_i\widetilde D_i)y_i=Q_iV_i(S_if),
\qquad
y_i=(I-\mathcal B_i\widetilde D_i)^{-1}Q_iV_i(S_if).
\tag{F.12}
$$
WPT (WPT.6)--(WPT.10) 的 skew-adjoint primitive 与 self-adjoint fiber matrix 相交换，故
$$
\|(I-\mathcal B_i\widetilde D_i)^{-1}\|\le1.
$$
同时 (WPT.7) 对**未经 input mean projection 的普通 source** 给
$$
\|Q_iV_i\|\le h_i/\pi.
$$
这里不能使用 $h_i/(2\pi)$：常数 source 会产生非零 centered ramp，而它已在 (F.12) 内完整保留。

定义实际接收细胞上的长度乘子
$$
(\Lambda_h v)|_{I_i}=\frac{h_i}{\pi}v|_{I_i}.
\tag{F.13}
$$
在正交细胞 direct sum 中求和，即证明所需的全部 source 不等式
$$
\boxed{\quad
\|Q_D\mathcal O_DG_Df\|_{\mathscr Z}^2
\le\sum_i(h_i/\pi)^2\|S_if\|_{L^2(I_i)}^2
=\|\Lambda_hSf\|_{\mathscr H}^2.
\quad}
\tag{F.14}
$$
这是一条对任意普通 $L^2$ source 的算子估计，没有只测 cell constants 或有限 source columns，也没有任何 $\sqrt N$ 费用。$G_D$ 的原 boundary conditions 保持不变；边界数据本身只在 (F.10) 的真实 $H^1$ Green 输出上读取。

## 4. 完整中心与真正尚未支付的连续逆

为免与 actual tail block 混淆，记完整 raw 中心 source operator 为
$$
\mathcal R_c=(A_{Lc}-D_f)+C\mathcal F B,
\qquad
H=H_c^{\rm cont}
=\mathcal O_DG_D\mathcal R_c S^{-1}\operatorname{pr}_{\rm body}.
\tag{F.15}
$$
$B=B_{HLc}$、$C=B_{LHc}$，$\mathcal F$ 是 R137 (S.4)--(S.11) / WJK 的**完整有符号 trial-and-dual composite**。它包括两次 reference $G$、两次左 primitive、两次右 primitive 的相应组合，以及全部 $\chi,\psi$、collar/body 交项、真实 $J^*$ 上限 $R$ 和原 cutoff derivatives。这里既不把它改成单个 $G$，也不丢掉 $C\mathcal F B$。

$A_{Lc}$ 仍是 WVC (WVC.3) 的 same-actual-$\eta$ hybrid：主部使用原 full-family 实际 $\eta$，下阶系数用 repaired centre。全部 mean、reaction 和有序 angular primitive 保留。没有把这个实现免费等同于 $DF(Q_{\rm repair})$。

假设已经证明
$$
T=(I_{\mathscr Z}-H)^{-1}\in\mathcal L(\mathscr Z),
\qquad C_T\ge\|T\|,\qquad M_C\ge\|T-I\|.
\tag{F.16}
$$
这是完整 (F.15) 的逆假设。R141 的 low193、未含完整 CFB 的逆单独不满足它；若从 low-only inverse 出发，必须另证完整反馈转授。R137 的 609 维 endpoint equivalence 可以作为 (F.16) 的入口，但 endpoint 非奇异和定量界仍需真正取得。

$H$ 将所有纯 atom inputs 映到零。因此 $T$ 在这些 inputs 上是原样的 identity，$T-I$ 则将其映到零。这个结构没有删除 atom outputs：body input 经过 $H$、$T-I$ 仍可产生全部 root97/outer96 outputs，且其范数仍在 (F.16) 内。

现在设一个**完整 ordinary-body** 算子界满足
$$
M_{\rm mesh}\ge
\|\Lambda_h S\mathcal R_c S^{-1}\|_{\mathscr H\to\mathscr H}.
\tag{F.17}
$$
$\Lambda_h$ 在 receiving cell 一侧，不能穿过非局部 $\mathcal F$ 移到 source 一侧。可先合并 $(A_{Lc}-D_f)+C\mathcal F B$ 的完整 signed kernel 再估计；也可以用对同一完整对象已经证明的上界。两个不相关 norm upper 的减法不合法。

由 (F.14)、(F.15)、(F.8)，
$$
\|Q_DHW_D\|
\le M_{\rm mesh}\|\operatorname{pr}_{\rm body}W_D\|
\le(6/5)M_{\rm mesh}.
\tag{F.18}
$$
即使 $\|H\|$ 很大，这个式子仍然成立。它使用了消去同平均齐次主部后的准确 source equation，而非直接粗估 $\|Q_D\|\|H\|$。

## 5. 原有限中心的严格门与逆界

定义和 R137 (S.18a) 完全一致的 finite centre 及 finite trial
$$
F_c=P_fHW_D:X_f\to X_f,
\qquad T_f=P_fTW_D:X_f\to X_f.
\tag{F.19}
$$
R137 (S.18c) 的恒等式可直接展开核对：
$$
\begin{split}
W_D(I-F_c)&=(I-H)W_D+Q_DHW_D,\\
T_f(I-F_c)&=I+P_fTQ_DHW_D.
\end{split}
$$
再利用 $P_fQ_D=0$，得到更有用的准确形式
$$
\boxed{\quad
T_f(I-F_c)=I+\mathcal E_f,
\qquad \mathcal E_f=P_f(T-I)Q_DHW_D.
\quad}
\tag{F.20}
$$
故较紧的直接 signed 新目标是
$$
\eta_f\ge\|P_f(T-I)Q_DHW_D\|.
\tag{F.21}
$$
它允许保留 $T-I$、细胞 remainder、完整 CFB 与有限输入提升之间的真实抵消。一个较容易分开计算、但可能较粗的充分选取为
$$
\boxed{\qquad \eta_f=(6/5)M_C M_{\rm mesh}.\qquad}
\tag{F.22}
$$
(F.21) 与 (F.22) 是同一算子的两种合法完整估计，不是挑选不同 reference/candidate 的有利标量。还可用 $\|P_f(T-I)\iota_{\rm body}\|$ 替代 (F.22) 的 $M_C$，因为 $Q_D$ 输出的 atoms 已准确为零；该替代仍必须给出其全部 finite body 与 193 atoms 输出。

若一个最后保存并读回的 directed upper 确实证明
$$
\eta_f<1,
\tag{F.23}
$$
则 $I+\mathcal E_f$ 可逆。由 (F.20)，$I-F_c$ 单射；(F.3) 的有限维方阵性给满射，且
$$
\begin{split}
(I-F_c)^{-1}&=(I+\mathcal E_f)^{-1}T_f,\\
\boxed{\quad
\|(I-F_c)^{-1}\|
\le\frac{(6/5)\,C_T}{1-\eta_f}.
\quad}
\end{split}
\tag{F.24}
$$
这只用原 finite space 的维数相等，并不分配一个巨大 dense matrix。假设 (F.16) 与严格门 (F.23) 各自仍是实际任务；本篇没有给它们虚构数值。

## 6. 原 rational normalizer 的完整球可合法只读转授

按 R137 (S.18a)--(S.18b)、WPS (WPS.11)，
$$
J_\rho=Q_f\Delta_\rho,
\quad E_c=J_\rho+(I-J_\rho)F_c,
\quad I-E_c=(I-J_\rho)(I-F_c).
\tag{F.25}
$$
这里 $Q_f$ 是原 rational-normalizer finite inverse；它不是本篇的 $Q_D$。两者的定义、源与陪域不同。

所需 $e_\rho\ge\|J_\rho\|$ 已在 **WVC run `43891414339/1`** 完成，准确位置是

`complete_new_graphs.complete_reference_receivers.new_records.complete_reference_rho_defect_upper`

完整记录原文为

```text
[0.0711946036559288564790863698434927839130869973587190328050667489299067566782 +/- 4.35e-77]
```

出处是 [完整 actual scientific conclusion](../notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json)，78627 bytes，SHA-256
`85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88`；原 [WVC 实际结论](R133-supplement-actual-continuous-centre-tracefree-candidate-and-false-finite-gate.md) 的 receiver 表也逐字列出了此球。

这个球的整个上端小于 $9/125$。这是所示两个有限十进有理数的直接比较，远大于原半径的正 margin；没有重跑原 normalizer graph，也没有改用 `prior_completed_candidate` 中另一 reference 的相近数值。因本篇的原 mesh、$D_f$、$S$、normalizer、Riesz factors 和有限 receiver 全部未变，故同一个 $J_\rho$ 合法满足
$$
\|(I-J_\rho)^{-1}\|<\frac{125}{116}.
\tag{F.26}
$$
结合 (F.24)--(F.26)，得到完整**有限中心加原 normalizer**的结论
$$
\boxed{\quad
\|(I-E_c)^{-1}\|
\le\frac{75}{58}\,\frac{C_T}{1-\eta_f}.
\quad}
\tag{F.27}
$$
准确乘积次序是 $(I-E_c)^{-1}=(I-F_c)^{-1}(I-J_\rho)^{-1}$；(F.27) 仅在取 norm 后才使用乘法上界。

## 7. 原 actual Schur 与两个右侧仍按原式接回

$I-E_c$ 是原 paired finite residual 中的中心因子。完整 actual operator 还包括 family-minus-centre、真实 high response 差、原外端 Robin/mean/high-trace/affine corrections，以及 true tail elimination 的完整 residual product。它们没有被归入一个未定义的“已付小误差”。

具体说，用 [WDS](R133-supplement-two-sided-tail-residuals-and-true-finite-Schur-certificate.md) (WDS.2)--(WDS.6) 的原 actual 四块，记
$$
M=A-BR_{\rm tail}^{-1}C,
\qquad
\mathcal U=(E_0-E_c)+D_{\rm res}^*R_{\rm tail}^{-1}T_{\rm res}.
$$
此处特意写 $T_{\rm res}$，以区别 (F.16) 的连续逆 $T$。原恒等式给
$$
Q_fM=(I-E_c)-\mathcal U
=(I-E_c)\{I-(I-E_c)^{-1}\mathcal U\}.
\tag{F.28}
$$
只有另一个对该**完整同对象**的严格上界
$\|(I-E_c)^{-1}\mathcal U\|<1$，才能进一步证明 actual finite Schur 可逆。原 actual tail 的 norm bound $3$ 仍来自未改变网格的 WIC (WIC.5)，不能用别的内部 refinement 偷换其 finite blocks。

当 actual finite inverse 确实取得后，原两行输入 $(f_f,g_t)$ 的准确恢复仍是
$$
x=M^{-1}(f_f-BR_{\rm tail}^{-1}g_t),
\qquad z=R_{\rm tail}^{-1}(g_t-Cx).
\tag{F.29}
$$
若使用主/对偶 tail trials 计算右侧，必须保留 WDS (WDS.10)--(WDS.11) 的完整 $r_g$ 和 $D_{\rm res}^*R_{\rm tail}^{-1}r_g$。本篇不把第二行设为零，不把 endpoint datum 无证明地移入 ordinary source。

原 prescribed root-even96 的真实成对输入、全部七个 high ports、独立 even mean、原外部函数、真实 jump/affine data、$\Theta$、$\nu$、负侧 radial head 和 nonlinear matching 均保留其原行列、norm 与交叉项。连续逆、(F.23)、(F.28) 的 actual remainder gate，以及原闭曲面族的最终完成条件都尚未由本篇数值支付。

本篇新增的可执行入口因此很明确：先取得完整 (F.16)，再计算 (F.21) 或完整的 (F.17)/(F.22)，原 $e_\rho$ 只读；全程只需给这几个完整算子的严格界，不需要分配原 4,724,833 维 dense matrix，也不需要重新计算已成功的旧 norm targets。
