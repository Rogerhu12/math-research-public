# R149 补篇：完整负侧二源与 signed 有限列的全残差认证

2026-11-26，visible-exact-astra-198c63d-20261126 / correlated_energy。

本篇给出两个新的解析结论。第一，已经完成的负根 Cauchy 常数和原 N/SP/PW receiver 接受完整第二非均值 ordinary 源；原较窄的 constant-second 标签无需被伪改成新域。第二，真正 physical root96 列可以用有限 Fourier 的连续径向 trial、完整未截断方程残差及真实正侧逆认证其 signed 腰部矩阵。为第一批齐次 root96 列，令正侧 trial 在真外端精确为零，便不需要从旧 unsigned DN 范数重建 signed DN 矩阵。

这两个结论没有执行新的科学数值，没有把尚未完成的 R142/R149、physical58 或完整224表置为成功。它们给后继 public owner 一条完整残差算法。其未知真解始终是全 Fourier 解；有限支集只用于可任选的 trial 及其可完整算出的残差。旧32量 WPN 表不含 signed 列，不能生成下面的 signed entries。

## SC1. 原对象和本篇使用的已成结果

全部对象仍是同一固定 intrinsic $\eta_0$、原 selected member 或原声明的实参数族、真实 $r_*$、完整 $DF(Q_\delta)$、ordinary $dr$ 及 normalized circle measure。原 Fourier 频率为 $4j$。全文用
$$
\Lambda_j=(1+16j^2)^{1/2},\qquad
I=\partial_\phi^{-1}(1-\Pi),\qquad
P_H=P_{\{|j|\ge97\}} .
\tag{SC.1}
$$

本篇依次使用以下 primary。

- [E：完整实根 Cauchy](R133-supplement-full-real-large-root-Cauchy-two-source-windows.md)，E.2–E.12；实际完成于 run43621934843/1。
- [N：完整负源到 cut](R133-supplement-complete-negative-source-to-strict-density-cut-readout.md)，N.2–N.7；以及 [SP：完整 primitive 与两 mean 传播](R133-supplement-complete-primitive-and-mean-strict-propagation-to-the-waist.md)，SP.6、SP.18。
- [PW：原七端口及完整腰密度](R133-supplement-seven-positive-ports-and-mixed-root-to-waist-density.md)，PW.11–PW.21；原实际四常数见 [PW actual](R133-supplement-actual-seven-positive-ports-to-complete-waist-density.md)。
- [Q：完整 moving Jacobi 方程](R133-supplement-negative-quadratic-density-and-full-frequency-transport.md)，Q.2–Q.4；以及 R141 的实际 full-family/physical identification。未解背景的 mean 变分项仍在。
- [P224：真实 physical 门后14输入、16输出](R141-supplement-original-seven-ports-after-the-physical-gate.md)，P.2、P.10–P.16；[L：精确 WOB/WPN 提升](R141-supplement-both-WPN-rows-by-exact-WOB-source-lifting.md)，L.24–L.25。
- [WY：完整两波 receiver](R133-supplement-four-ordered-waist-receivers-and-complete-strong-error-assembly.md)，WY.5、WY.11、WY.34；本轮 [PN 接线](R149-supplement-complete-positive-inverse-to-true-negative-and-incoming.md)。

新纯模块是 [fourfold_codazzi_signed_finite_column_residual_math.py](../scripts/fourfold_codazzi_signed_finite_column_residual_math.py)。它只定义完整有限卷积、真径向导数、Parseval 残差费、真正输入注入、signed pairing 和完整有限逆残差，不进行 IO 或科学执行。

## SC2. 同一个已成常数接受完整 ordinary 第二源

令 $R_0=1/200$，使用原
$$
r_c=r_+-R_0,\qquad
0<r_*-r_c\le R_0 .
\tag{SC.2}
$$
保留原两个有理 root endpoints；不把 $r_*$ 换成 midpoint。E 的 multiplier 为
$$
M=\operatorname{diag}(\theta/w,\theta),\qquad
w\ge\Lambda^{-1/3},\quad 0<\theta\le1 .
$$
所以每个 $\rho$ 上，对任意完整二源 $f=(f_1,f_2)$，
$$
\|\Lambda^{-1}Mf\|_2^2
 \le \|f_1\|_{H^{-2/3}}^2+\|f_2\|_{H^{-1}}^2 .
\tag{SC.3}
$$
这逐频包含 $j=0$。第二源的非均值 Fourier 项没有被投影掉；两个 source 分量各有自己的 Sobolev 权。

E.10 的 complete growth 是同一齐次算子的估计，与 $f$ 的角向 constancy 无关。将 (SC.3) 放入原受迫能量不等式，按 E.11–E.12 的同一有序 Duhamel、ordinary $dr$ Cauchy–Schwarz 及全频 density 延拓，得到
$$
\|h(r_c)\|_{H^{-1}\oplus H^{-1}}
\le {\cal C}_{-1}\left[
 B_{\rm root}+J_-+
 \sqrt{R_0}\,
 \|f\|_{L^2_r(H^{-2/3}\oplus H^{-1})}\right].
\tag{SC.4}
$$
$\mathcal C_{-1}$ 正是已完成的原常数，不再计算 E.10 的积分。原 E.12 已经直接公布的 isotropic
$L^2_r(H^{-2/3}\oplus H^{-2/3})$ 是 (SC.4) 的子域；因此一个完整 raw $L^2$ pair 即使不使用新的 anisotropic 最强版本，也已经具有完整二源资格。

N.7 对任意完整 raw $H^{-1}$ pair 是相同的 $h\mapsto(Iw,\Pi w)$ map，含原 $T(q)$、$n_g$ 和两个 mean。SP.6 的 source 是整个 $(ITf,\Pi Tf)$，SP 的齐次传播和 source 接收也不要求第二分量为常数。因此把 (SC.4) 沿原 N/SP 相同复合送至腰部，**原已经保存的同一个** $C_O$ 给
$$
D_W\le C_R(B_{\rm root}+J_-)
       +C_O F_-+C_2F_{\rm st}+C_1J_{\rm st},
\tag{SC.5}
$$
其中
$$
F_-=\|f\|_{L^2([r_c,r_*];\,H^{-2/3}\oplus H^{-1})},
\quad
F_{\rm st}=\|f\|_{L^2([0,r_c];\,H^{-1}\oplus H^{-1})}.
\tag{SC.6}
$$
strict ordinary 也可按原 $C_1L^1$ 选择；不将两种 ordinary 选择重复相加。真正 root-window impulses 仍用 mixed norm 和 $C_R$，strict impulses 仍用 $H^{-1}$ pair norm 和 $C_1$。它们不取得 ordinary source 的 $\sqrt{\text{length}}$ 因子。

这里 $D_W$ 的完整输出是
$$
\mathfrak D_0h=(Iw(0),\Pi w(0)),\quad
w=n_gT(q)h,\quad
\mathcal Y_0=L^2_0(\mathbb T;\mathbb R^2)\oplus\mathbb R^2 .
\tag{SC.7}
$$
同一 raw $L^2$ 源在 root/strict 两段的限制互相正交；只有在这个输入身份成立时，
$$
C_OF_-+C_2F_{\rm st}
 \le (C_O^2+C_2^2)^{1/2}\|f\|_{L^2([0,r_*]\times\mathbb T)} .
\tag{SC.8}
$$
这没有宣称两个解输出正交。新乘积或平方根如果需要登记数值，只在一个明确新的 public scalar target 中读取原球后计算；本篇不重算任何旧科学。

后继应使用明确的完整二源 admission，保留旧 PW constant-second 标签原义。R147 的完整 selected negative ordinary proposal residual 可按 raw-$L^2$ 子域接入；这只支付该已知源的负侧腰部贡献，不会单独证明完整 $\nu$、phase 或 nonlinear inverse。

## SC3. 一个有限 trial 的完整 PDE 残差确实可算完

在原 moving coordinates，记 $Q=(u,v)$，$m=\Pi v$，
$$
S_0=u^2+Kv^2,\quad d=-\beta I S_0,\qquad
J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix}.
$$
完整系数作用为
$$
\begin{aligned}
A_Qh={}&d h_\phi+\gamma mJ(K)h_\phi+Lh
 -2\beta Q_\phi I(uh_1+Kv h_2)
 +\gamma(\Pi h_2)J(K)Q_\phi,\\
L={}&
\begin{pmatrix}
-\beta(1+3u^2+Kv^2)&-2\beta Kuv\\
-2\beta uv&\beta(1-u^2-3Kv^2)
\end{pmatrix}.
\end{aligned}
\tag{SC.9}
$$
特别是最后一项不能由“mean 已固定”而删掉。完整 parameter 源另在 $f$；原 residual-sensitive physical-angle bridge 仍按 R141 的同一 $DF$ 身份使用。

若 $Q$ 的角向 degree 为96，trial $h^{\rm app}$ 的 degree 为 $M$，则 (SC.9) 的完整输出 degree 至多 $M+192$。理由逐项为：$d,L$ degree 至多192；$Q_\phi$ degree96；$uh_1+Kv h_2$ degree 至多 $M+96$，而真正 primitive $I$ 只消去其零频；最后 mean rank 的输出 degree 至多96。因此对于 finite source $f$，
$$
r=\partial_rh^{\rm app}-A_Qh^{\rm app}-f
\tag{SC.10}
$$
的支集完整包含于 $|j|\le\max(M+192,\deg f)$。所有零频、两符号、卷积末端和 nonlocal 中间零频都必须真的形成；没有将未知真解截至这个支集。若 $f$ 非有限支集，应额外保留其完整原 tail norm，而不是使用这个支集结论删去它。

使用 normalized real basis
$\sqrt2\sin4j\phi,\sqrt2\cos4j\phi,1$ 时，其 complex coefficients 为
$$
\widehat h_1(j)=-ia_j/\sqrt2,\quad
\widehat h_1(-j)=ia_j/\sqrt2,\quad
\widehat h_2(\pm j)=b_j/\sqrt2,\quad
\widehat h_2(0)=m_h .
\tag{SC.11}
$$
纯模块按此精确转换，用完整 complex coefficient pair 做有符号卷积。只有完整残差形成以后才取绝对值。逐 whole radial box $I_\ell$，Parseval 给
$$
\|r\|_{L^2_r(H^{s_1}\oplus H^{s_2})}^2
 \le\sum_\ell |I_\ell|
  \sum_{j,k=1,2}\Lambda_j^{2s_k}
       \sup_{I_\ell}|\widehat r_k(j)|^2 .
\tag{SC.12}
$$
实际 $|I_\ell|$ 是整个 true length 的有向上界，不是 midpoint length。盒子须完整覆盖相应真区间；交叠只可增加非负积分，不能遗漏。全参数族时，box 系数必须围住同一完整 $\delta$ 区间。细化 trial 评估盒子不会自动缩小原旧 whole-parent 系数球。

正侧 compact bump 为零时，$Q_\delta$ 为 affine，(SC.9) 的系数在 $\delta$ 上至多 quadratic；可用 polynomial-in-$\delta$ trial 来消除依赖宽度，也可直接使用完整 interval 系数。负侧 compact metric 的参数依赖不按 quadratic 伪截断。

## SC4. 首批96个齐次物理列无需 signed 外图

第 $j$ 个真实列的 positive 数据为独立 physical root-even96 单位向量 $e_j$，原高 stable 数据为零，ordinary、height、Robin、mean、jump 数据均为零。L.24 证明这个完整 source pair 是 P224 的第9列；根 prescribed96 是输入，不是一般 $L^2$ lifting 的 $w$ 根迹。

令 $x=(r-r_*)/(R-r_*)$。任选有限 Fourier、径向 polynomial 的 $p_j(x,\phi)$，置
$$
h^+_{{\rm app},j}(r,\phi)=(1-x)p_j(x,\phi).
\tag{SC.13}
$$
则真外端 $h^+_{\rm app}(R)=0$ 精确成立，包括完整 low/high、mean 和所有外图线性输出。零独立 exterior 数据下，原完整 DN、height、physical mean、angle/Robin 图在零输入上精确为零。这里不是将图算子设零，而是使用其线性性；因此无需从旧 operator norms 恢复其 signed entries。trial 的 cutoff 导数完整留在
$$
\partial_rh^+_{\rm app}
 =\frac{-p+(1-x)\partial_xp}{R-r_*}.
\tag{SC.14}
$$
分母使用同一真长度。一个 piecewise version 也可用共同 endpoint 值保证真 $C^0$ continuity。系数的 PPoly 导数跳不会产生状态 jump；如果 trial 自己不连续，就必须另付其真正 jump，不能喂进 P224 的 ordinary low 源列。

选择 $P_{E_c}p_j(0)=e_j$ 可使 root-even residual 精确为零。odd96 和 moving mean 根值是自由 trial 值。高 root trial 若精确满足原 stable 条件，则其 stable residual 为零；若尚无 signed stable projector 的新计算，仍可用原已付 mixed-to-stable 输入 conversion
$$
s_j\le (153/16)\,
 \|P_Hh^+_{{\rm app},j}(r_*)\|_{H^{-2/3}\oplus H^{-1}} .
\tag{SC.15}
$$
这只是保守的合法输入界，不是反用输出 factor9。也可选择 trial 的高根值精确为零，直接使 stable residual 为零。后继若该费用过宽，应计算真正有限 root projection 的残差，而不是改标签宣称零。

对 (SC.10) 的完整正侧 residual，分成真实 low193 raw-$L^2$、high collar 和 high body ordinary $H^{-2/3}$ pair。于是14个 P224 input slots 中，首批连续齐次列只需要
$$
d_0=s_j,\quad d_1=F_{c,j},\quad d_2=F_{b,j},
\quad d_7=F_{L,j},\quad
d_9=\|e_j-P_{E_c}h^+_{\rm app}(r_*)\|;
\tag{SC.16}
$$
其余为由 (SC.13) 和真正 continuity 证明的零。第8列 transformed low 是不同 source 坐标，不再与第7列重复收费。collar/body 的真实 partition 和两 source 分量使用原 ordinary norm；不只算低头投影。

令 $P_{\alpha k}$ 为真正完整保存的224表，按原单位取
$$
\epsilon_d=\sum_{k=0}^{13}P_{{\rm low\_root97},k}d_k,\qquad
\epsilon_H=\sum_{k=0}^{13}P_{{\rm high\_root\_mixed},k}d_k .
$$
则真实正侧解与 trial 的**完整物理**根差满足
$$
\epsilon_* \le
 \sqrt{d_9^2+\epsilon_d^2+\epsilon_H^2}.
\tag{SC.17}
$$
low mixed weights 不超过 normalized Euclidean weights；三个块真正正交。已存 high-root-mixed 已包括 stable 与 returning 分量，不再乘9。此处没有从一个 body-$L^2$ 上界取 trace。

若 trial 的其他真实物理边界资料非零，则必须恢复相应完整 slots，包括 height/Robin/mean 的两条注入路径。非零外端 trial 也可合法使用已付完整外图范数估计其边界 residual，但不能据此捏造 signed DN entries。优先采用 (SC.13) 是一种具体可执行 trial 选择，不是完整 inverse 成功的数值保证。

## SC5. 连续负侧 trial 给实际腰列的完整误差

令 $t=r/r_*$，任选另一个有限 Fourier polynomial $q_j(t,\phi)$，置
$$
h^-_{{\rm app},j}(r,\phi)
 =h^+_{{\rm app},j}(r_*,\phi)+(1-t)q_j(t,\phi).
\tag{SC.18}
$$
它在真根和 positive trial 精确相接；使用真 $r_*$ 除 (SC.14) 的相同导数形式。也可用保持共同端值的连续 piecewise trial。无需将 trial 视为解。

计算完整负 residual
$r^-=\partial_rh^-_{\rm app}-A_Qh^-_{\rm app}$，在 root/strict 两区分别用 (SC.6)、(SC.12)。第二非均值 residual 由 SC2 接收，没有删掉。因纯 root96 列没有独立 physical impulses，且 trial 连续，真误差的完整 waist norm 满足
$$
D_j\le C_R\epsilon_*+
             C_OF_{-,j}+C_2F_{{\rm st},j}.
\tag{SC.19}
$$
如果真实资料或 trial 有 jumps，应在 (SC.19) 增加 (SC.5) 的完整相应项。一个独立 parameter 列还要加入其实际 ordinary、根、germ、外资料及所有独立 matching 行，不能把齐次列的零 identity 复制给 $\nu$。

在腰部 $q(0)>0$，直接计算
$$
Y_j^{\rm app}=\mathfrak D_0h^-_{{\rm app},j}.
\tag{SC.20}
$$
$T(q)$ 和 $n_g$ 是 radial，因此这一步仍为完整有限 Fourier 列，且两个 mean 可以精确从零频读出。真 $Y_j$ 的两 mean 可能非零，不能用 reflection 或一个 moving mean 代替它们。本步骤的 interval enclosures 进入 trial evaluation 误差；(SC.19) 使用的是同一真实 $\mathfrak D_0$。

## SC6. 从有符号列到有符号 rows：可执行的 adjoint 认证

设实际 finite row $\ell_a:\mathcal Y_0\to\mathbb R$ 的完整 norm 已有方向正确的界 $L_a$。对于 exact finite trial，完整 signed 配对给
$$
M_{aj}=\ell_a(Y_j),\qquad
|M_{aj}-\ell_a(Y_j^{\rm app})|\le L_aD_j.
\tag{SC.21}
$$
不能用 $\|\ell_a\|\|Y_j\|$ 代替配对中心。若 row 是 raw primitive/mean 的 normalized Fourier functional，(SC.21) 的 trial pairing 直接是完整 Fourier 系数和两个 mean 的有符号实内积。

真正 normalized incoming rows 则按 WY/PN 的原顺序。例如对 real normalized output mode $g_a$，
$$
\ell_a(Y)=
 \langle g_a,U_{\mathcal H^{-1}}\mathscr J_+
                   \widehat T_0^{-1}Y\rangle ,
\quad
z_a=\widehat T_0^{-*}\chi_a,\quad
\chi_a=\mathscr J_+^*U_{\mathcal H^{-1}}^*g_a .
\tag{SC.22}
$$
在原 density-pullback convention $U_Xf=X'(f\circ X)$ 下，
$U_{\mathcal H^{-1}}^*g_a=g_a\circ\mathcal H$。outgoing row 的 adjoint 按原相反乘法顺序保留旋转：
$\mathscr J_-^*U_{\mathcal H^{-1}}^*U_{R_\Omega^{-1}}^*g_a$。
两个 mean 由 $\mathscr J_\pm^*$ 的完整 decomposition 保留。

选一个实际有限 Fourier row trial $z_a^{\rm app}$，完整形成
$$
e_a=\chi_a-\widehat T_0^*z_a^{\rm app}.
$$
由已成 $\|\widehat T_0^{-1}\|\le K_{W,0}$，
$$
\|z_a-z_a^{\rm app}\|\le K_{W,0}\|e_a\|.
\tag{SC.23}
$$
这给可直接执行的 row-residual 路线，而不是要求一个未有的 signed inverse 矩阵。原 $\widehat T_0$ 的两个 factors 按 adjoint 反序形成；不以两个 scalar norms 生成其 entries。其完整已知 multipliers 必须用实际 whole Fourier/angle carrier 评估，真实 Fourier projections、$I$ 和两 mean identity 保持原次序。若这些 multipliers 用有限 Fourier 截断表达，所有尾项都进入 $e_a$ 的完整 $L^2$ 上界。finite row trial 本身不意味着 $\widehat T_0^*z_a^{\rm app}$ 有有限支集；包含 $1/v$、phase 或其他无限系数时不得沿用 (SC.9) 的有限 degree 结论。

$\chi_a$ 的完整 $L^2$ residual 可在整个 angle circle 作有向 cell 积分：对真实 selected $\mathcal H$ 的原完整 lift enclosure，求 $g_a\circ\mathcal H$，再减去同一 angle box 上的完整 $\widehat T_0^*z_a^{\rm app}$，最后才平方积分。若使用一个 explicit $\mathcal H_{\rm app}$ 和原 whole error $\|\mathcal H-\mathcal H_{\rm app}\|_2$，另加
$\|g_a'\|_\infty\|\mathcal H-\mathcal H_{\rm app}\|_2$。本轮已有一个具体的合法选择：[W 的同 selected 物理 Wiener actual](R133-supplement-actual-physical-Wiener-conjugacy-strip.md)，run43588332723/1、loss $1/250$，给出
$$
G=K_{48}\circ H_{\rm fin},\qquad
\|\mathcal H-G\|_{\mathcal A_{1/128}}\le E_H ,
\tag{SC.23a}
$$
其中 $E_H$ 必须读取 W.4 对应的完整旧误差球；其 identifying upper 为 $2.210026409642\,10^{-7}$。$H_{\rm fin}$ 只表示 W 中已固定的原有限 coordinate $H$，不是另一个 selected conjugacy。W 的完整 R31/K48 原件来自 run43586895661，其 source/native/完整 coefficient 身份必须与 W/NIF 使用的同一 $Q_0,Z,\eta_0$ 和 selected pair 一致。

因此可明确取 $\mathcal H_{\rm app}=G$，将完整 $K_{48}$ 与 $H_{\rm fin}$ 按原次序逐 angle box 复合评估，并另付 $\|g_a'\|_\infty E_H$；$\mathcal A_{1/128}$ 支配原 normalized $L^2$。这直接消费已成 KAM 误差，不再求一次 KAM conjugacy。有限定义的两个映射之复合仍可能有无限 Fourier 尾：采用 angle-box 整体复合，或将其完整尾一并认证，不能把复合截为一个无余项的有限 Fourier 多项式。$g_a$ 的常数部分以及 $\chi_a$ 在 $\mathscr J_\pm^*$ 中的完整 mean decomposition 继续保留。outgoing 仍先按 (SC.22) 的 adjoint 反序加入真实旋转，不将原 Maslov/sign 跨过角映射。

仅有 WX 的 angle operator norm 不能冒充 $G$ 的这些 signed coefficients。尚未物化其完整已成载体时，应读取 W 的原全件及 actual process，而不是从 unsigned32表或截短显示值反推。完整角 cell 积分无需假定 $\chi_a$ 有有限 Fourier 支集。

于是新的可计算中心和 radius 是
$$
\widehat M_{aj}=\langle z_a^{\rm app},Y_j^{\rm app}\rangle,
\quad
|M_{aj}-\widehat M_{aj}|
 \le L_aD_j+
       K_{W,0}\|e_a\|\,\|Y_j^{\rm app}\|
       +\epsilon_{{\rm eval},aj}.
\tag{SC.24}
$$
$L_a$ 可用同一实际左 receiver 的 $B_{H,0}K_{W,0}\|g_a\|$，不需要再乘一个 $N_i$ 或 $K_\Lambda$。有限 physical root96 输入只有自身的 source normalization；high common-input 的右 $W^{-1}A_{\rm src}$ 不移到这些独立列。若实际 rows 另有 mean、phase、border 或 $\nu$ 部分，其完整 signed 项按原定义追加。

(SC.24) 的第二项只补 row trial 的配对误差，第一项仍使用真 row norm，不把它改成 row trial norm。两个误差不能无根据抵消。对于已经有完整 signed row coefficients 的情形，可直接用 (SC.21)，不重复收费 (SC.23)。

## SC7. 完整有限矩阵 gate 与真正 Schur 的范围

对所有声明的 rows、columns 保存完整 signed interval matrix $\mathbb M$，包括 (SC.24) 的全部 radii。源坐标和目标坐标分别按原 positive diagonal $D_s,D_t$ 转换：
$$
\widetilde M=D_tMD_s^{-1}.
\tag{SC.25}
$$
$D_t$ 不能被复用为 $D_s$，也不能把原 $S$、$\Theta$ 任意施加于 root/waist rows。选一张完整 exact dyadic trial inverse $B$，先按真正矩阵乘法形成每个 signed entry
$$
\mathbb E=I-B(D_t\mathbb M D_s^{-1}),
\tag{SC.26}
$$
再计算所有 row/column absolute sums，
$$
\rho_\infty=\max_i\sum_j|\mathbb E_{ij}|,\quad
\rho_1=\max_j\sum_i|\mathbb E_{ij}|,\quad
\rho_2\le\sqrt{\rho_\infty\rho_1}.
$$
若整个保存/读回 upper 严格小于一，则完整 square matrix 可逆，且
$$
\|\widetilde M^{-1}\|_2
 \le\frac{\sqrt{\|B\|_1\|B\|_\infty}}{1-\rho_2}.
\tag{SC.27}
$$
失败只表示这个 trial/残差 gate 未闭合，不能据此证明 BVP 奇异。不可跳过某些 rows、只取 principal submatrix、从 absolute entry 表恢复符号，或把负 upper 截零通过门。

原物理96矩阵本身不自动等于 BF/FC 的完整 Schur。真正 high elimination 的 cross terms、transported finite factors、两个 mean、independent function input、true phase 和 $\nu$ rows 仍按原 complete incoming square 保留。若要认证其真正 bordered Schur，应先通过相应 high inverse，并对每个 Schur RHS 依上述同一残差方法认证实际解列；将所有 cross terms 的 signed pairing 纳入 (SC.26)。root96 的正侧可逆和 (SC.27) 的某个独立小块不能代替这一步。

## SC8. 后继执行的最小科学范围

首批新 target 可以精确声明为所有96个 homogeneous physical-root columns：完整正/负 trial、全 $M+192$ residual、真实区间 ordinary fees、完整 root error、两个腰 mean 和所有指定 signed finite rows。每个 completed column 的科学数据可作为声明前缀保存，但没有全部96列及全部 rows 就没有 complete matrix gate。若执行中发现旧 positive inverse 前置未成，不能运行科学部分或创建虚构 actual。

旧 E/N/SP/PW、58、224、32 等成功数值只读；trial residual、row residual 和新 signed matrix 是新的实际目标。未知 full-frequency inverse 的误差控制来自完整真实正侧逆和 SC2，不能由一个数值截断矩阵自身代替。所有实际 source/selected/root/angle/normalizer 身份及 true cover 与零 identities 必须随 whole input receipt 绑定。公共 owner 对每个新保存结果完整读回并重新核门；内部大型可重建数组不要求复制成永久结果，但科学 whole 输入、完整完成数量、目标与输出球不得截断或以摘要代替。

至此，新完整二源域和 signed finite-column 残差认证的解析链已闭合。未付的是明确的新实际输入、列与 gate，不是额外的假设性 root/body majorant；本篇没有继续已被 R146 排除的 CV/RA 费用路线。
