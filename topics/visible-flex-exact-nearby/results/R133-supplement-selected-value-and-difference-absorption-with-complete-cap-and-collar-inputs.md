# R133：同一 selected 态的体与切口非线性吸收，以及完整 collar 接收入口

2026-11-15，tail_connector。

**状态：条件解析推论；没有新增数值运行，也没有认定任何新的未知态输入已获界。** 本篇把 [SR 的统一割线接收式](R133-supplement-uniform-secant-cap-rows-and-complete-finite193-nonlinear-receivers.md) 化成一个明确的二阶正矩阵检验。其新内容是同时吸收 NF 的低频体非线性和 CH 的真实切口余项，并在同态条件下接入已成功 NG 的完整一行。原成功 Green、CPA、WL、NG 和原 SC 输入均不重算。

## VR1. 固定对象、范数和真实域

固定 SR.1 的同一个 $\eta_0,\nu_\delta,Q_\delta$、$|\delta|\le10^{-10}$、moving $\phi$、physical $\theta$、反射规范和真实 $L=9/10$。令
$$
 I_-=[0,L],\qquad \Pi=\Pi_{\le96},\quad H=1-\Pi,\quad
 h=Q-Q_\delta .
 \tag{VR.1}
$$
$\Pi$ 是原 odd96/even97 的完整正交投影，不再乘 $\alpha$，也不保留旧 weighted-state 的额外缩放。所有体 norm 使用 normalized-circle Euclidean pair 和真实 $dr$。定义
$$
 \begin{split}
 x_B&=\|\Pi h\|_{L^2(I_-;L^2_\phi)},&
 x_C&=\|\Pi h(L)\|_{L^2_\phi},\\
 y_B&=\|Hh\|_{L^2(I_-;L^2_\phi)},&
 y_C&=\|Hh(L)\|_{L^2_\phi},&
 t_H&=\|Hh(L)\|_{H^1_\phi}.
 \end{split}\tag{VR.2}
$$
这里 $t_H$ 是真实角一阶 norm，不能由已有 high-cut $L^2$ 列直接改名。两个分量、实际 even mean，以及由帽图输出的完整 physical Cmean 全部保留。physical $\gamma$ 的 nonmean 投影只用于帽的输入。

取 [CPA](R133-supplement-actual-weighted-cap-inner-difference-and-finite193-inverse.md) 的一个完整 case，其三窗四列记为 $g_Y,p_Y,a_Y,c_Y$，$Y=B,N,C$。原窗口 $N=[0,2383968743003/10^{13}]$。第五列 $w_Y$ 使用 SR.9 及已成 [WL 实际收据](../notes/complete_waist_lifting_ci/run-43749764738-1/execution.json) 的同 case。禁止从两个 case 拼取 entry，也不从已乘过腰源的 WL contribution 再乘一次 $\delta,\alpha$ 或 $1/\sqrt2$。

以下值推论要求：

- $Q$ 是这个背景下同一状态；全 $I_-$ 的 ordinary 方程和实际 value jumps 有明确意义。
- 整个 $I_-$ 有 NF.7 的同对象实值界 $M,\rho_{\rm core},k,b,g$。只在正 collar 有效的界不能代替它。
- 真 cut 满足 CH 的实角域，$r=\|h_2(L)\|_{H^1}\le2^{-10}$；所使用的总 cut 先验另写为
$$
                \|h(L)\|_{H^1_\phi\oplus_2 H^1_\phi}\le T .
 \tag{VR.3}
$$
- 实际 $\gamma_h=P_\perp(C_Q-\widehat C)$ 与基点 $\bar\gamma_\delta$ 均在所选 CPA case 的真实 physical $A^0$ 球；$f_h$ 在同一 normalized $\dot A^2$ 球，$s_B$ 固定。

$T$ 是该条件定理的真实前提。不能把待证的 W entry 半径填入 $T$，再将所得改善称为已经证明未知态进入该球。

## VR2. 单态 height 的正确量词与已知 affine

对这个给定 $Q$，在其**实际同一个** $f_h$ 上选基点帽
$\Gamma(\bar\gamma_\delta,f_h)$，沿 physical $\gamma$ 线段取 SR.10 的平均算子。于是完整边界值式准确为
$$
 \mathcal R_\partial^{f_h}(Q)
 =\mathcal R_\partial^{f_h}(Q_\delta)
       +\mathcal B_\delta^{\mathcal K_{h0}}h+\mathcal E_{h0}.
 \tag{VR.4}
$$
这里没有额外 height 差列，因为两项使用的就是同一个 $f_h$；没有假设 $f(\gamma)$ 可微或 Lipschitz。

记
$$
 b_\delta(f_h)=-\mathcal R_\partial^{f_h}(Q_\delta),\qquad
 \|b_\delta(f)\|_{97}\le b_{\rm aff}
 \quad\hbox{对所声明的整个 }f\hbox{ 域成立}.
 \tag{VR.5}
$$
若一个成功 [SC](R133-supplement-exact-radial-subtraction-and-complete-known-cap-affine-moments.md) 结论提供这个 uniform $b_{\rm aff}$，它必须包含完整 signed functional、数值尾、formal residual、完整左缺陷、outer affine 与 mean 费用，而不只是某个 RW prior uniform。SC.24 的 A.15 外端费和 SC.23 的先验须在该同一个 $f$ 域上有效。未成功的 SC 运行不给 (VR.5) 一个数值。

已知 $\bar\gamma_\delta$ 可使用 W 的已付
$\|\bar\gamma_\delta\|_{A^0}\le(13/200)|\delta|<10^{-9}/128$，
所以 SC 的 tail-$\gamma$ 已知基点 prior 可以控制 (VR.5)。
未知 $\gamma_h$ 及平均算子的整段若只满足 full-$\gamma$ 域，则 (VR.4) 和所有 $g,p,a,c,w$ 必须使用 CPA full case。已知基点较小不把未知割线的 $\kappa$ 改成 tail case。

若只得到某个固定 $f_{\rm ref}$ 的 affine 界，则 (VR.5) 右侧须增加 SR.17 的
$(7/25)\|f_h-f_{\rm ref}\|_{\dot H^2}$，不可删去。
若整 $f$ 球已在 (VR.5) 中包围，同一 height 改变也不可重复收费。
独立 meanheight、$\lambda$、span 和 high odd matching 均不因这个量词重排消失。

## VR3. 完整普通源与低角投影

使用 [NF.11](R133-supplement-divergence-nonlinear-core-source-and-complete-finite193-receivers.md) 的真实全内体量
$$
 \lambda_v=\operatorname*{ess\,sup}_{r\in I_-}
 k\rho_{\rm core}\left\{
 384\left[b\left(\frac{\pi}{8}(2M+\rho_{\rm core})+\frac M4\right)+g\right]
       +b(3M+\rho_{\rm core})\right\}.
 \tag{VR.6}
$$
则不索未知 $h_\phi$ 就有
$$
 \|\Pi\mathcal N_\delta(h)\|_{L^2(I_-;L^2_\phi)}
 \le\lambda_v\sqrt{x_B^2+y_B^2}
 \le\lambda_v(x_B+y_B).
 \tag{VR.7}
$$
原散度势的两个 mean reaction 仍包含在 (VR.6) 最后一项中。

令
$$
 f_\delta=(Q_\delta)_r-\mathcal F(Q_\delta,\nu_\delta),\qquad
 r_\delta\ge\|\Pi f_\delta\|_{L^2(I_-;L^2_\phi)} .
 \tag{VR.8}
$$
必须使用 R/MC 的 canonical 连续方向，含 raw response mean、真实 piece-constant offset 和 selected 参数项。MC 的两个 collar mean 费用不自动给整个 $I_-$ 的 (VR.8)，F.13 的额外 $\nu$ source 也不是它。本篇保持 $r_\delta$ 为独立的待付输入，不由现有局部收据猜值。

对近似态另记
$s_Q=\|\Pi(Q_r-\mathcal F(Q,\nu_\delta))\|_{L^2(I_-;L^2_\phi)}$；
其右行 residual norm 为 $r_\partial$，左腰 residual norm 为 $r_0$。
实际独立 value jumps 对输出 $Y$ 的完整贡献记为 $j_Y$。只有真方程、真97行、真腰和无 jump 时，这些额外量才为零。

## VR4. 同一个体与切口的二阶吸收

由真实频率 $|4j|\le384$，
$$
 \|\Pi h(L)\|_{H^1}\le\sqrt{1+384^2}\,x_C<385x_C.
$$
结合 (VR.3) 与 SR.15，定义 $\beta_v=128T$，得到
$$
 \|\mathcal E_{h0}\|_{97}
 \le128\|h(L)\|_{H^1}^{\,2}
 \le\beta_v(385x_C+t_H).
 \tag{VR.9}
$$
这一步的 pair 是 Euclidean pair；没有把 norm-sum 与 Euclidean norm 无费互换。

记 $b_{0,\delta}=-UQ_\delta(0)$，令
$\omega_Y\ge w_Y\|b_{0,\delta}\|_{96}$ 是同 CPA case 已成 WL contribution。
对真态定义
$$
 q_Y=
 g_Y(r_\delta+\lambda_v y_B)
 +p_Y(b_{\rm aff}+\beta_v t_H)
 +a_Yy_B+c_Yy_C+\omega_Y .
 \tag{VR.10}
$$
近似态则在同一 $q_Y$ 另加
$g_Ys_Q+p_Yr_\partial+w_Yr_0+j_Y$。
SR.19--21 给
$$
 \begin{pmatrix}x_B\\x_C\end{pmatrix}
 \le
 \begin{pmatrix}q_B\\q_C\end{pmatrix}
 +\mathsf M_v\begin{pmatrix}x_B\\x_C\end{pmatrix},
 \qquad
 \mathsf M_v=
 \begin{pmatrix}
 g_B\lambda_v&385p_B\beta_v\\
 g_C\lambda_v&385p_C\beta_v
 \end{pmatrix}.
 \tag{VR.11}
$$
$\Pi\mathcal A_\delta h_H$ 已由 $a_Y$ 消费；
完整 $\mathcal B_\delta^{\mathcal K}h_H(L)$ 已由 $c_Y$ 消费。
(VR.10) 中 $\lambda_v y_B$ 是非线性余项的另一个实际高输入，并非重复前两项。
帽线性差已在统一左边界行中吸收一次，不再加 $c_{\rm cap}\kappa$ 右源。

对任意非负矩阵 $\mathsf M=(m_{ij})$，若
$$
 A=1-m_{11}>0,\qquad D=1-m_{22}>0,\qquad
 \Delta=AD-m_{12}m_{21}>0,
 \tag{VR.12}
$$
则
$$
 (I-\mathsf M)^{-1}
  =\Delta^{-1}
      \begin{pmatrix}D&m_{12}\\m_{21}&A\end{pmatrix}\ge0 .
$$
因此 (VR.11) 准确给
$$
 \boxed{\quad
 x_B\le X_B=\frac{Dq_B+m_{12}q_C}{\Delta},\qquad
 x_C\le X_C=\frac{m_{21}q_B+Aq_C}{\Delta}.
 \quad}\tag{VR.13}
$$
负窗同时有
$$
 \|\Pi h\|_N
 \le q_N+g_N\lambda_v X_B+385p_N\beta_v X_C .
 \tag{VR.14}
$$
这些是同一个状态的有限正预算消元。它们不要求把未定义的 arbitrary $L^2$ trace 当成有界映射，也不把此条件后验估计说成 nonlinear existence。

## VR5. 真 wide collar 的同态高迹可替掉独立 $t_H$

本节仅针对同时进入 [NGA.4--7](R133-supplement-actual-adjustable-nested-collar-geometry-and-direct-angular-trace.md) 的同一个真态。要求整
$$
 I_{\rm w}=[17/20,19/20]
$$
上是同一个连续 $H^1$ 解，真实残差为零，selected $C^0$ 差满足原 $\rho=10^{-4}$ 域，全部 actual 系数、均值和 seam 条件成立。右帽的 $C^0$ 结论只付右半，不能替代这些前提。

令
$$
 P(r)=\operatorname{diag}(K(r)^{-1/4},K(r)^{1/4}),\qquad z=Ph,
$$
$$
 Z_L=\|\Pi_{\le96}z\|_{L^2(I_{\rm w};L^2_\phi)},\qquad
 Z_S=\|\Pi_{33\ldots96}z\|_{L^2(I_{\rm w};L^2_\phi)} .
 \tag{VR.15}
$$
$P$ 只出现一次。它径向且与 Fourier 投影交换，但不等于原 Green weighted-state 变换。

选择下列**一个完整** actual NG row：
$$
 (u,v)=(145,748)\quad\hbox{或}\quad(489,10),\qquad
 h_*=1.012\,10^{-11}.
$$
对应得到
$$
                  t_H<h_*+uZ_S+vZ_L .
 \tag{VR.16}
$$
$h_*$ 已包含该整行的完整 known source 和由真实 $C^0$ 域付出的 high-body 项，不能再把它当零。这里直接使用 H1 接收式，不使用另一个窄域 $H^{8193}$ 的插值。

记左、右半 $I_{\rm w}^-=[17/20,L]$、$I_{\rm w}^+=[L,19/20]$。
令 $p_-\ge\sup_{I_{\rm w}^-}\|P(r)\|$ 为已付系数界，
并保真正右半同态量
$$
 R_L\ge\|\Pi_{\le96}Ph\|_{L^2(I_{\rm w}^+;L^2_\phi)},\qquad
 R_S\ge\|\Pi_{33\ldots96}Ph\|_{L^2(I_{\rm w}^+;L^2_\phi)} .
 \tag{VR.17}
$$
原 $B$ 窗只能限制到左半。由正交性和随后三角不等式，
$$
 Z_L\le\sqrt{p_-^2x_B^2+R_L^2}\le p_-x_B+R_L,\qquad
 Z_S\le\sqrt{p_-^2x_B^2+R_S^2}\le p_-x_B+R_S .
 \tag{VR.18}
$$
这允许现有 whole-body scalar 给安全左上界，但没有制造一个更小的 output-shell Gram。若将来有真实左 shell receiver，可以完整替换这一左上界；旧 input-side Gram 不能投影成它。

置
$$
 \eta=p_-(u+v),\qquad d_H=h_*+uR_S+vR_L .
 \tag{VR.19}
$$
于是 $t_H<\eta x_B+d_H$。在 VR4 的同一先验 $T$ 下，(VR.11) 可以改为
$$
 \mathsf M_{\rm NG}=
 \begin{pmatrix}
 g_B\lambda_v+p_B\beta_v\eta&385p_B\beta_v\\
 g_C\lambda_v+p_C\beta_v\eta&385p_C\beta_v
 \end{pmatrix},
 \tag{VR.20}
$$
$$
 q_Y^{\rm NG}=
 g_Y(r_\delta+\lambda_vy_B)
 +p_Y(b_{\rm aff}+\beta_vd_H)
 +a_Yy_B+c_Yy_C+\omega_Y .
 \tag{VR.21}
$$
再按 (VR.12)--(VR.13) 消元，并对 $N$ 使用同一完整两系数行。
这样在明确的同态 wide 域内，不必另外把 $t_H$ 当作一个未经证明的输入。

(NC/BD) 两套 (VR.19)--(VR.21) 必须整套分别检验，不能先取较小 $u$ 再配另一行的较小 $v$，不能在矩阵与 $q$ 中使用不同 row。任何数值选择须消费最后保留有向上界，不从 rounded uppers 的比值反推 coefficient。

若得到 $X_B,X_C$，NGA 原具体充分门可直接写为
$$
 385X_C+
 \min\left\{
 145\sqrt{p_-^2X_B^2+R_S^2}
       +748\sqrt{p_-^2X_B^2+R_L^2},\
 489\sqrt{p_-^2X_B^2+R_S^2}
       +10\sqrt{p_-^2X_B^2+R_L^2}
 \right\}
 \le9.5\,10^{-12}.
 \tag{VR.22}
$$
每项仍是一个完整 row。门通过才给原 W 的低 physical-curvature entry；这里没有认定它已经通过。若用 (VR.3) 建立 bootstrap，自映像、连续选解或解的存在性必须另有实际证明，不能由 (VR.22) 自身倒推。

## VR6. 两态差分：值半径不能冒充 Lipschitz 常数

对同背景 $Q_\delta$ 的两态 $h,k$，令 $u=h-k$，并用 (VR.2) 对 $u$ 定义 $x_B,x_C,y_B,y_C,t_H$。全 core 的两个态都须在 NF 同一 $\rho_{\rm core}$ 域。真正的差分常数是
$$
 \lambda_d=\operatorname*{ess\,sup}_{I_-}
 k\rho_{\rm core}\left\{
 384\left[b\left(\frac{\pi}{8}(2M+\rho_{\rm core})
                         +M+\frac{\rho_{\rm core}}2\right)+2g\right]
       +b(6M+3\rho_{\rm core})\right\}.
 \tag{VR.23}
$$
它来自 NF.12--13，不用 $\lambda_v$ 改名。

另外，两个 cut 必须各自满足 CH 差分域
$$
 \|h_1(L)\|_{H^1}+\|h_2(L)\|_{H^1}\le\varrho,\qquad
 \|k_1(L)\|_{H^1}+\|k_2(L)\|_{H^1}\le\varrho,\qquad
 \varrho\le2^{-10}.
$$
两态 actual physical $\gamma$ 仍须位于同一个 CPA case，height 均合法。
由于 norm-sum 不大于 $\sqrt2$ 倍 Euclidean pair，
$$
 \|\mathcal E_{hk}\|_{97}
 \le\beta_d(385x_C+t_H),\qquad
                   \beta_d=2^{11}\sqrt2\,\varrho .
 \tag{VR.24}
$$
完整两均值和 $K_0+\mathcal K_{hk}$ 的 scalar 输出均包含在该 chart 费内。

令 $\Delta s$ 为两个 ordinary residual 的投影差 norm，
$\Delta r_\partial$ 为真实右97残差差 norm，$\Delta w$ 为真实96腰差；
令 $j_Y^\Delta$ 保留实际 jump 差。则
$$
 \begin{split}
 q_Y^d={}&
 g_Y(\Delta s+\lambda_dy_B)\\
 &+p_Y\left(\Delta r_\partial+\beta_dt_H
             +\frac7{25}\|f_h-f_k\|_{\dot H^2}\right)
 +a_Yy_B+c_Yy_C+w_Y\|\Delta w\|+j_Y^\Delta .
 \end{split}\tag{VR.25}
$$
以 $\lambda_d,\beta_d$ 替换 VR4 的矩阵并满足 (VR.12)，即得到同一对态的 (VR.13)--(VR.14)。
两个真解的 ordinary residual 和已匹配右行可以相消；非零 height 差不能删，也不能从 tail 仅连续选解推为 $\|\gamma_h-\gamma_k\|$ 的小线性费。

NGA 的 (VR.16) 是 selected 单态方程的已成条件结论；本篇不把它直接改名为 $u=h-k$ 的差分高迹界。差分若要吸收 $t_H$，须另付同一差分方程的真实高迹估计。把两个值上界相加最多得到新的非齐次上界，不自动给 contraction。

## VR7. 可消费字段与当前尚缺的真实输入

一个后续公开小 consumer 可以只读已成 CPA/WL/NG 与成功 SC 的小结，评价 (VR.12)、(VR.13) 和 (VR.22)，而不用重做 Green、Poisson、旧 signed Grams 或旧积分。它必须另有以下同对象输入：

| 输入 | 精确用途与不能替代的量 |
|---|---|
| uniform $b_{\rm aff}$ | 完整 SC.25 向量界；保 physical Cmean、非零 affine、原 $f$ 域和 selected 左 target |
| whole $r_\delta$ | canonical $Q_\delta$ 的全 $[0,L]$ ordinary $L^2dr$ 投影残差，含 raw mean 与 offset；不能用局部 MC 或 F.13 |
| $\lambda_v$ 或 $\lambda_d$ | 同一未知态球在全 core 的 NF 系数和半径；不是帽或 collar 系数 |
| $T$ 或差分 $\varrho$ | 真实 cut chart 前提；不是待证 low-entry 门 |
| $y_B,y_C$ | 独立 whole high-body 与实际 high-cut；不能混成一个 norm |
| $R_L,R_S,p_-$ | (VR.17) 的同态右半数据与一次径向 $P$；右帽 ordinary $L^2dr$ 不能变成 $\sum_k\sup_r$，也不能由 $\gamma$ 小省去 base mismatch |
| residuals、waist、jumps | 真零只能由真实方程/条件给；WL 已含的 known 腰 contribution 只使用一次 |

所有 determinant 与分母都须先验证严格正再求逆；失败保留完整输入和失败门，不输出假想上界。任何通过结论都只适用于列明的同态域。完整 high inverse、真正全部函数匹配、core 构造和最终几何任务仍须另付。
