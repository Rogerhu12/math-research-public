# R149 补篇：真根端点连续的 96 个 PDE trial 与完整新残差

2026-11-26，visible-exact-astra-198c63d-20261126 / correlated_energy。

本篇把 SC 的有限列路线落实为可执行的第一批新数学目标：96 个真实 physical even-root 单位输入的连续有限 Fourier trial、全区间 selected moving 方程残差、以及与已完成 RW96 行的 signed 腰部配对。已完成的 RW96 行误差、7721 个旧 intrinsic Taylor 载体、原连续修复和已选参数资格均只读。有限 trial 的选择可以用浮点计算；所有新结论由随后完整的有向残差计算证明。

本次新增独立 kind 为 `R149_complete_true_root_finite_trial_residuals_v1`。旧 SC7 末段在 positive inverse 未完成时禁止运行的，是其 true-column error / 真矩阵认证科学入口；该入口仍保持禁运行。本次另立有限对象 algebra/residual 目标，不调用 P224 或未知逆。

本篇及第一轮只证明 trial、残差和 signed trial matrix；没有把它们登记为真 PDE 列、真有限矩阵可逆或全频逆。真正的列误差须在原 P224 完整实际表成立后按 SC.17--24 付清。完整双 mean、真根位置、完整 selected mean 和原 dr 均在下述定义内。

## TC1. 原件、空间与唯一选中对象

固定 normalized circle、物理频率 $4j$、ordinary 径向测度 $dr$，实反射坐标依次为

$$
(a^o_1,\ldots,a^o_{96},b^m,b^e_1,\ldots,b^e_{96})\in\mathbb R^{193},
\qquad
a=\sqrt2\sum_{j=1}^{96}a^o_j\sin(4j\phi),\quad
b=b^m+\sqrt2\sum_{j=1}^{96}b^e_j\cos(4j\phi).
\tag{TC.1}
$$

令 $E_c$ 是最后96维的等距注入；$E_d$ 是前97维的注入。试列最大角次数96，真 PDE 解不加 Fourier 截断。

完整背景始终是 $Q_\delta=Q_0+\delta Z_{\rm can}$。$Q_0$ 是原 base65 cubic 先乘原精确 $\alpha$、再逐结点精确连续修复、最后加原 scalar $s_0$ 所定义的场；$Z_{\rm can}$ 是原 physical193 cubic 的完整连续修复，**不再乘 $\alpha$**。两条完整 offset chain 分别由原定义哈希

- centre：440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47；
- direction：6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04

绑定。共同6144个原 cubic 及全部6143个接口使用精确 binary64 有理值与 Fraction 运算；不得用 offset sup 充当 signed offset。

本次只需原 run43588332723/1、loss $1/250$ 的同一 selected member。NW 已证明

$$
|\delta_*|<d_{\rm sel}:=
\frac{9368259853002}{100000000000000000000000}<10^{-10}.
\tag{TC.2}
$$

此处使用整件 NW manifest/proof 与其完整 selected 资格，不从显示小数抽取参数。RW96 的原 $|\delta|\le10^{-8}$ 行资格仍原样保留，因而包含这个同一 selected member。没有把未知 $\delta_*$ 设为浮点数。浮点 proposal 可在 $\delta=0$ 选择，误差证明使用整个 (TC.2)。

真根满足原完整区间

$$
r_-=\frac{1191984371497}{5000000000000}
\le r_*\le
r_+=\frac{2383968743003}{10000000000000},\qquad R=\frac{25}{8}.
\tag{TC.3}
$$

compact intrinsic 控制的支集为 $[1/20,9/50]$，严格位于 $r_-$ 左侧。因此正侧 intrinsic $\beta,K,\gamma$ 及真根均不因 $\delta$ 改变；selected mean 仍是 $m_0+\delta\Pi Z_{\rm can}$，不是另一个 rotational $s_\delta$。

## TC2. 只消费已经完成的 40 parts / 7721 个 intrinsic 载体

原 run43583838026/1 的40个自然分片给出全 $[0,R]$ 的7721个闭行。必须读取完整原 manifest、8个原 archive 的实际 process、全部40个原 compressed-payload SHA256、原成功汇总和精确 row 身份。单个分片的 `complete=false` 是原局部分片语义；它同时必须 `selected_cells_complete=true`、无 failure、具有正确选定指标。全 cover 由40件按原索引恰好拼成0..7720来证明，不伪改旧标记。

每行已有 $\beta,K,\gamma,s_0$ 的 midpoint 0..3 阶 derivatives、whole 0..3 阶 derivatives、原 $a_{\rm phys}$、真 scalar germ、原 cubic piece 身份以及完整原 $\eta$ half-width $10^{-9}$。这些是真原无限 intrinsic 对象的已付包围。**本次保留全部旧 $\eta$ 宽度**；选定 $\eta_0$ 属于它，不因此把旧半径缩为零。

对原行 $J=[c-h,c+h]$，取已保存的 midpoint derivatives $F_0,F_1,F_2$ 及 whole third derivative $F_3(J)$。逐系数选确定的 exact dyadic $p_k$，并保有向误差 $e_k$，使

$$
F_0\subset p_0+[-e_0,e_0],\quad
F_1\subset p_1+[-e_1,e_1],\quad
F_2/2\subset p_2+[-e_2,e_2],\quad
F_3(J)/6\subset p_3+[-e_3,e_3].
$$

则逐点 Taylor 公式给

$$
f(c+x)=p(x)+e_f(x),\quad
p(x)=\sum_{k=0}^3p_kx^k,\quad
|e_f(x)|\le E_f:=\sum_{k=0}^3e_k h^k,\qquad |x|\le h.
\tag{TC.4}
$$

third derivative 在余项中可随 $x$ 变化；(TC.4) 没有声称它是一个固定未知多项式系数。所有新子格只代入 $x=c_{\rm child}-c+h_{\rm child}t$，保留相同 $E_f$，或以同一式中合法的较小 $|x|$ 上界计算子格费用；**不得对 $E_f$ 求径向导数**，也不重算原 germ。真正 trial 的径向导数来自其精确多项式。

在 compact 支集内，完整 selected intrinsic 为

$$
\gamma_\delta=\gamma_0e^{\delta w/2},\qquad
K_\delta=e^{-\delta w}(K_0+\delta T w'),\qquad
T=\frac{\beta}{2(a_{\rm phys}\gamma_0)^2}.
\tag{TC.5}
$$

原精确 $w$ 满足 $|w|\le1,\ |w'|\le2400/13$。可以在原 Taylor carrier 上加入完整 uniform scalar fees

$$
E_{\gamma,\delta}\le \|\gamma_0\|_\infty(e^{d_{\rm sel}/2}-1),\qquad
E_{K,\delta}\le \|K_0\|_\infty(e^{d_{\rm sel}}-1)
+d_{\rm sel}\|T\|_\infty(2400/13)e^{d_{\rm sel}}.
\tag{TC.6}
$$

$\|T\|_\infty$ 直接用该原 whole 行的 $\beta,a_{\rm phys},\gamma_0$ 与严格正分母证明。支集外两项为精确零。完整 $\beta$ 不变，$s_0$ 不改成新的 rotational mean。这些费用只改变径向 scalar，不创造无限角尾。

## TC3. 精确共享节点，真根参数与齐次外端

选一个有限 proposal 网格，包含原所有需要的固定切点，以及唯一符号节点 $r_*$。根隔离区间内的固定点可以删除，避免把未知根与某个端点强行认同。浮点选择只使用一个明确 dyadic $\widehat r\in[r_-,r_+]$；最后的数学 trial 始终使用 $r_*$。

每个节点保存同一组 exact binary64 有理向量 $Y_i$，每侧保存 derivative vectors $D_i^{(k)}$，$k=1,2,3$。所有96列一次共同选择。根节点的 even96 子块**按定义精确设为 $I_{96}$**，其 odd96+mean 坐标取保存的 dyadic proposal。正负两侧引用同一整个根 $Y_*$，不各自四舍五入。

在一段真实长度 $h_i=r_{i+1}-r_i>0$ 上，令 $t=(r-r_i)/h_i$。用八个 Hermite 基函数定义次数7的多项式

$$
H_i(r)=\sum_{k=0}^3
\frac{h_i^k}{k!}
\bigl[D_i^{(k)}L_k(t)+D_{i+1}^{(k)}(-1)^kL_k(1-t)\bigr],
\qquad D_i^{(0)}=Y_i,
\tag{TC.7}
$$

其中

$$
\begin{aligned}
L_0(t)&=1-35t^4+84t^5-70t^6+20t^7,\\
L_1(t)&=t-20t^4+45t^5-36t^6+10t^7,\\
L_2(t)&=t^2-10t^4+20t^5-15t^6+4t^7,\\
L_3(t)&=t^3-4t^4+6t^5-4t^6+t^7 .
\end{aligned}\tag{TC.8}
$$

$L_k^{(\ell)}(0)=k!\delta_{k\ell}$ 且 $L_k^{(\ell)}(1)=0$，$0\le\ell\le3$，故 (TC.7) 的所有节点值恰等于同一 $Y_i$。尤其

$$
E_c^*H^+(r_*)=I_{96},\qquad H^-(r_*)=H^+(r_*).
\tag{TC.9}
$$

此处没有 root midpoint residual 被漏付。true $h_i$、$1/h_i$ 和每个径向积分质量均作为整球保留。只需节点值连续；即使左右高阶 derivative proposals 不同，也没有 distributional jump 源。

为使第一轮不需从 unsigned 外边界常数反造 signed DN 矩阵，定义

$$
\chi(r)=
\begin{cases}
1,&r\le3,\\
L_0(8(r-3)),&3\le r\le25/8 ,
\end{cases}
\qquad \widetilde H^+=\chi H^+,\quad \widetilde H^-=H^-.
\tag{TC.10}
$$

$\chi(3)=1,\chi(R)=0$ 且两端一至三阶导数为零；因此正侧 trial 在真外端完全为零，完整 exterior height、Robin、两 mean 及真 cap 对零变分的响应全部为零。$\chi'H+\chi H'$ 的两项均进入新 residual。最末 cap trial 的次数至多14，仍是有限径向多项式。

## TC4. 浮点 proposal 只选择 (TC.7)，不提供任何证明费用

一个具体实现可在 positive 半段从原近似 Robin96 frame 反向作 QR shooting，在 negative 半段从同一根向腰积分；共用原 selected centre 的完整193近似矩阵。用至少四阶步进并在每个节点保存完整值和三阶 physical radial derivatives。QR、线性求解、步长或近似端点图都只是有限 dyadic proposal 的选择规则。近似模型不是实际 full $DF(Q_\delta)$ 的替代物。

合法证书不依赖某个浮点局部误差估计：即便该 proposal 质量很差，后续全残差仍包围其真正误差。任何非有限 proposal、缺失列或 endpoint identity 失败必须停止该新 target 并保存实际失败，不能用插值补成功。

完整 trial 数组仅在 runner 私有保存，逐件写入后读回并校验 SHA256；所有后续残差与配对只读这份确定的 dyadic 数组。公开记录精确 source/runtime/parameters、完整 counts 和 whole hash。后继若需条目，按同一定义重新物化必要 carrier，并验证同一 whole hash；不得中途按一个新 midpoint 改 trial，也不重算本轮已经完成的 residual norm 目标。

## TC5. 完整 moving residual 的有向批量计算

逐个原 scalar 行、原 exact cubic pieces 与 trial piece 的共同交集，构造同一径向变量上的完整 $Q_\delta$、$\widetilde H$ 与真 $\partial_r\widetilde H$。角乘法使用完整 signed Fourier 卷积，或严格无 alias 的 directed FFT。最大 residual 支集为 $|j|\le96+2\cdot96=288$，故 $L=1024$ 足以保全部两符号和两个分量。

必须使用 SC.9 的完整算子：

$$
\begin{aligned}
(\mathcal A h)_1={}&d a_\phi+\gamma mK b_\phi
-\beta(1+3u^2+Kv^2)a-2\beta Kuvb\\
&-2\beta u_\phi I(ua+Kvb)+\gamma(\Pi b)K v_\phi,\\
(\mathcal A h)_2={}&d b_\phi-\gamma m a_\phi
-2\beta uva+\beta(1-u^2-3Kv^2)b\\
&-2\beta v_\phi I(ua+Kvb)-\gamma(\Pi b)u_\phi,\\
d={}&-\beta I(u^2+Kv^2),\qquad m=\Pi v .
\end{aligned}\tag{TC.11}
$$

这里没有假定背景已解方程；最后两个 mean-rank 项全部保留。新源为

$$
f_j^\pm=\partial_r\widetilde H_j^\pm-\mathcal A_{Q_{\delta_*}}\widetilde H_j^\pm .
\tag{TC.12}
$$

批量运算只是把独立列作为额外数组轴。每列有自己完整的 uniform Wiener error；不可把它误用作一个矩阵 operator error。对 $p+e$ 与 $q+d$，传播规则为

$$
E_{pq}\le N_pE_q+N_qE_p+E_pE_q.
\tag{TC.13}
$$

所有误差都具有明确有限角支集。故 angular derivative 的误差为 $4M E$，primitive 的误差至多 $E/4$，mean 与 nonmean 投影的 Wiener 误差均至多 $E$。未知无限 intrinsic primitive tails 已在原 scalar 球中完整支付。

径向 polynomial 使用 exact monomial-to-Legendre 转换。若

$$
p(t,\phi)=\sum_{\ell,k}c_{k\ell}P_\ell(t)e^{4ik\phi},
$$

则对真实长度 $\Delta r$，

$$
\|p\|_{L^2_rH^s_\phi}^2
=\Delta r\sum_{k,\ell}
\frac{(1+16k^2)^s|c_{k\ell}|^2}{2\ell+1}.
\tag{TC.14}
$$

先形成 signed residual，再对各 $c_{k\ell}$ 取有向平方上界。uniform error 的 $L^2_rH^s$ 费用为至多 $\sqrt{\Delta r}E$，因为本轮 source 窗口均有 $s\le0$。有限项与误差使用三角不等式；不同不交径向子格的最终 L2 平方相加。所有平方根用 Arb 有向计算。

若真根与原固定 scalar cut 的次序在隔离区间内不确定，可以将实际交集包围在同一原行内的固定闭区间上，并将精确 trial 多项式作代数延拓后积分这个较大区间。这样只会增加费用；全 cover 不允许空隙。旧 scalar 误差仍只在其原行内使用。重复包围的 tiny 根区间不能以“正交分区”去掉。

## TC6. 第一批每列的完整可消费 outputs

使用原固定 positive cut

$$
r_b=\frac{1192029371497}{5000000000000}
$$

和原 negative strict cut $r_c=r_+-1/200$。每列支付五个不同的完整 residual 费用：

$$
\begin{aligned}
F_{L,j}&=\|P_Lf_j^+\|_{L^2([r_*,R];L^2)},\\
F_{c,j}&=\|P_Hf_j^+\|_{L^2([r_*,r_b];H^{-2/3}\oplus H^{-2/3})},\\
F_{b,j}&=\|P_Hf_j^+\|_{L^2([r_b,R];H^{-2/3}\oplus H^{-2/3})},\\
F_{-,j}&=\|f_j^-\|_{L^2([r_c,r_*];H^{-2/3}\oplus H^{-1})},\\
F_{{\rm st},j}&=\|f_j^-\|_{L^2([0,r_c];H^{-1}\oplus H^{-1})}.
\end{aligned}\tag{TC.15}
$$

$P_L$ 保留全部193坐标，包括 even mean；$P_H$ 保留97..288全部本次 residual 输出。negative 两个分量无 constant-second 限制，使用已证明 SC2 的完整二源资格。continuous trial 的所有低跳跃、cut 仿射跳跃和 negative impulses 恰为零。

原 P224 的14输入向量因而只有 indices1、2、7（按从0计数）分别为 $F_{c,j},F_{b,j},F_{L,j}$，其余精确零。stable high 根值因 trial 支集96而为零；prescribed even96 根误差由 (TC.9) 为零；独立外 high/height/Robin/mean 和97条 right chart 缺陷由完整零外端构造为零。

在真腰 $r=0$ 用同一 selected 原件计算

$$
q_0=\sqrt{-K(0)}>0,\quad
n_g(0)=\frac{a_{\rm phys}(0)^2}{m_\delta(0)^2},\quad
w_\pm=\frac{n_g}{\sqrt{2q_0}}(a\pm q_0b).
\tag{TC.16}
$$

完整 trial density 为 $(Iw_+,Iw_-;\Pi w_+,\Pi w_-)$。两 mean 独立保留，即使 physical primitive96行本身对 mean 的系数为零。第六个每列 output 是这个整个 density 的 L2+两mean 范数。

## TC7. 只用原 RW 的同一个精确行做 signed 配对

RW run45787309600/1 已完成96行、480小球及98400私有 coefficient records。本轮读取其 whole actual/execution/manifest 与原定义；只为新配对重物化同一 exact DFT4096、cutoff1024 的 $p_i$ carrier，并校验原 private carrier hash。**原 $\epsilon_i$、trial norm、incoming/physical row error 不再求值。**

physical96 trial matrix 定义为

$$
M^{\rm tr}_{ij}=
\left\langle (Pp_i/2,Pp_i/2;0,0),
(Iw_{+,j},Iw_{-,j};\Pi w_{+,j},\Pi w_{-,j})\right\rangle_{\mathcal Y_0}.
\tag{TC.17}
$$

复实现必须取同一实 Hilbert pairing 的实部；在全部 signed 求和结束前不得取绝对值。若同时保存 declared incoming96 matrix，则其行严格为 $(Pp_i,0;\Pi p_i,0)$，其 old-angle mean 不能删除。两个矩阵是不同对象，各自有明确完整 hash；本轮不把它们或任意子块冒称全 bordered Schur。

所有96×96 entries 在私有文件整体保存读回后，才求其新的完整 row/column/Frobenius 范数。公开只保存完整矩阵 hash、尺寸、signed 输入定义和小范数球；不发布新可重建大数组。该 signed trial matrix 仍不是 true PDE matrix。按 SC.24 还须付真列误差与原完整 RW 行误差，且主空间上需原 T0、G、完整 mean、真正 receiver adjoint 顺序；不能从试算残差小或试算矩阵非奇异直接宣称完成。

## TC8. 证书顺序与旧目标隔离

一个列（或批内若干列）的五个 source norm、完整 waist norm、全部 signed entries 必须全部完成，再形成 candidate 记录；candidate 全件写入、读回、逐球检查包含后，才能进入 completed prefix。后继乘法只读正式保存 upper。任何失败保留实际 prefix 与未成 target，不能把未读回 candidate 算作完成。

新 public owner 只登记这里的96列和完整 signed trial matrices。原7721 scalar jets、原 repair chains 的已成结论、RW96误差、NW selected 参数与源预算、旧 R142 HS/Green 以及所有旧外图/receiver预算均不重算。必要的 signed exact repair 或 RW DFT carrier 物化明确记为新目标所需输入恢复；其已有规范或数值界不再作为新的科学 target。

执行范围严格分为两步：（一）本次独立 kind 只执行 (TC.12)--(TC.17) 的已定义有限 trial algebra、完整 residual norms 与 signed trial pairings，不需要也不读取未知正侧逆；（二）原 SC.17--24 的真 PDE 列误差与真矩阵门仍只允许在完整 P224 actual 成立之后执行。旧 SC true-column 入口的禁运行条件没有被删除或绕过。本篇不需要等待尚未完成的正侧全逆才执行第一步。一旦全 P224 实际表可用，仍必须按同一已定义 trial、同一 source units 和原 SC 完整误差公式继续认证真正 signed 列，不更换对象规避已付失败。

## 原件引用

- [SC：完整二源与 signed 有限列](R149-supplement-signed-finite-columns-and-full-negative-residual-sources.md)。
- [RW：反射有限行](R149-supplement-reflected-finite-waist-rows-from-complete-conjugacy.md)及 run45787309600/1 的完整 actual。
- [NW：同窗 selected 参数资格](R147-supplement-same-window-selected-nu-source-to-complete-waist.md)。
- [原40件/7721载体 manifest](../notes/2026-11-15-R133-selected-parameter-core-scalar-fees-CI-inputs.json)，原 producer 是 `fourfold_codazzi_correlated_head_residual_rows.py`，只读其完成的输出。
- [正侧完整14端口](R141-supplement-original-seven-ports-after-the-physical-gate.md)、[原 full-delta collar](R133-supplement-full-real-delta96-positive-root-collar.md)、[完整 primitive 与两 mean](R133-supplement-complete-primitive-and-mean-strict-propagation-to-the-waist.md)。
