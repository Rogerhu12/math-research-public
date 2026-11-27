# R147 BFP：同一 strict ν 的完整 B forward 列、全圆 pullback 残差与 Θ 消费

2026-11-27，`visible-exact-astra-fb31ed6-20261127 / trial_restore`。

**新增完整可执行证书。** [BNC](R147-supplement-target-normalized-strict-parameter-column.md)
的96个低坐标不足以恢复整个 $\mathcal B^{-1}F_\nu$。
本条明确所缺的新输入：同一真 strict-$\nu$ particular 的一个
degree512 finite **forward** trial，及其完整全圆 $L^2$ residual。
该证书可从已成 NP/PO/ASB/JC、DBRA 的原 w carrier 和原全 G
载体实际构造，不需先有 homogeneous96、positive58/224 或完整 Schur。

新的 residual 在原 physical circle 的完整 pullback 中直接认证；
不重跑 BNC 的192 observations，不重算旧 NP pairings、
DWT2/BR7、IR、ASR、OT、UDRC21 或 CYA gap。所有无限 tail、真 H/G
区别、cohomological w error 和原两 mean 仍在下面的完整公式中。
本条没有新 BFP actual 或预报其误差足以闭合某个 Schur 门。

## BFP1. 同一真实列和已成输入

保持 BNC.2–5 的同一隐式 selected member、原 physical period
$\pi/2$、归一测度、物理频率4：

$
 f=f^a=\tfrac12(y_+^a+y_-^a),\quad \deg f=96,\quad
 \Pi f=0,\qquad
 F^a=U_{\mathcal H^{-1}}f,\qquad
 x_\nu=\mathcal B^{-1}F_\nu\in Y_a^0 .
 \tag{BFP.1}
$

这里 $f$ 由 NP 原193维 waist vector 和完整 true selected
$q,n_g$ 定义，不选择一个 numerical selected state。
原已成完整 PO、ASB、JC 与 W 输入给

$
 \|f\|_2\le N_0,\qquad
 \|F_\nu-F^a\|_2\le E_{\rm PDE}:=B_HD_b/\sqrt2 ,
 \tag{BFP.2}
$

以及整个

$
 \|\mathcal H-G\|_{\mathcal A_\sigma}\le E_H,\quad
 \|G-Id\|_{\mathcal A_\sigma}\le G_0,\quad
 \|G'\|_{\mathcal A_\sigma}\le G_1,\quad
 \|\mathcal H'\|_{\mathcal A_\sigma}\le H_1,\quad
 \sigma=1/128 .
 \tag{BFP.3}
$

$G=K_{48}\circ H_{24}$ 是原 full finite compound lift，
保完整常数相位。两 derivative 的 mean 都是1。JC/BNC.7 已给
整个 homotopy $X_t=(1-t)G+t\mathcal H$ 的真下界 $X_t'\ge m>0$；
这条既成 lower 直接复用。以下只使用这些全频 Fourier/Wiener
输入，不能以 scalar row error 反推 (BFP.3)。

[DBRA](R149-supplement-actual-direct-target-w-and-complete-B-inverse-rows.md)
给原完整2048-mode $\widehat w$ 和两个全误差
$e_{w,\infty},e_{w,2}$。仍使用同一个
$\mathcal B=Id+\mathcal T_w I$；
$\mathcal T_w=\Pi_+M_w\Pi_++\Pi_-M_w\Pi_-$。
$\widehat w$ 全 SHA 为
`c28d74dd27eda8cd0f7f3479afee06f67d36156df679ed43e0ddd62f006f5fb3`。
原 true $R_aw=-w$ 保证真正 $\mathcal B$ 与 $Q_a=P(Id+R_a)/2$ 交换；
finite $\widehat w$ 或下面的 trial 不被免费假设具有精确未知 $a$ parity。

## BFP2. 真 H 与 full G 的整个 density 差

令 $N_1\ge\|f'\|_2$。degree96 的 Bernstein 可使用
$N_1=384N_0$，不重算旧 $N_0$。
完整 Wiener derivative 与 degree-one mean 给

$
 \|(\mathcal H-G)'\|_\infty\le E_H/\sigma,\qquad
 \|X_t''\|_\infty\le
 B_2:=\frac{\max(G_1,H_1)-1}{\sigma}.
 \tag{BFP.4}
$

令 $u_t=U_{X_t^{-1}}f$、$d=\mathcal H-G$。
完整密度变分准确是

$
 \partial_tu_t=-\partial_x U_{X_t^{-1}}(df).
 \tag{BFP.5}
$

证明直接对
$u_t(x)=f(\phi)/X_t'(\phi)$、$\phi=X_t^{-1}(x)$ 求导；
$\partial_t\phi=-d(\phi)/X_t'(\phi)$。因此右边在 $\phi$ 中等于

$
 -\frac{d'f+df'}{(X_t')^2}
       +\frac{dfX_t''}{(X_t')^3}.
$

用真实变量替换 $dx=X_t'(\phi)d\phi$，而非免费 unitary
composition，可得

$
 \|\partial_tu_t\|_2
 \le m^{-3/2}(\|d'\|_\infty N_0+\|d\|_\infty N_1)
        +m^{-5/2}\|d\|_\infty B_2N_0 .
$

沿完整 $t\in[0,1]$ 积分后得到新可计算的 whole bound

$
 \boxed{\quad
 \|U_{\mathcal H^{-1}}f-U_{G^{-1}}f\|_2
 \le E_{\rm flow}:=
 \frac{E_H}{m^{3/2}}
       \left(N_1+\frac{N_0}{\sigma}+\frac{B_2N_0}{m}\right).
 \quad}
 \tag{BFP.6}
$

完整 first/second derivative 费用均已付，原常数相位 $d$ 也保留。
这是 whole density $L^2$ bound，不是有限 row 上的 estimate；
不通过假设真 $\mathcal H$ 具有 finite support 取得。

## BFP3. 新的 finite forward trial 与完整 same-sign 输出

任选一组完整 exact dyadic/rational coefficients，
定义实 mean-zero degree $M=512$ trial

$
 \widehat x(\phi)=\sum_{0<|n|\le M}z_ne^{4in\phi},
 \quad z_{-n}=\overline z_n,\quad z_0=0 .
 \tag{BFP.7}
$

浮点选择只给一个 trial；可用原 full G grid 的 inverse resampling
和同一 $\widehat w$ 的 finite solve 选取，但该选择不证明任何
residual、inverse 或 Galerkin tail。它不能调用已成 BNC192 的
旧 certified quadrature/pairing 目标。

令 $K=2048$，准确的完整 finite forward image 为

$
 r=\widehat x+\mathcal T_{\widehat w}I\widehat x,\qquad
 r_n=z_n+\sum_{\ell=1}^{M}
          \widehat w_{n-\ell}\frac{z_\ell}{4i\ell},
 \quad1\le n\le K+M=2560 .
 \tag{BFP.8}
$

$z_n=0$ 于 $n>M$，
$\widehat w_0=0$，
$\widehat w_{-k}=\overline{\widehat w_k}$。
正输出只接正输入，负 block 是整个 conjugate；
(BFP.8) 的符号是 forward $\mathcal B$ 的正号，
不是 BR 中 $\mathcal B^\dagger$ 的负号。
全部1–2560 signed outputs 都必须形成并保存，不能只核512块。
其后精确为零的只是这个 finite $r$，不是真正 residual。

## BFP4. 完整 pullback 范数与无限 alias

写 $F^G=U_{G^{-1}}f$。因为 $G$ 是原 orientation-preserving
degree-one lift，准确恒等式为

$
 \|r-F^G\|_2^2
   =\int_{\mathbb T}
       \frac{(r(G(\phi))G'(\phi)-f(\phi))^2}{G'(\phi)}
             \,\frac{d\phi}{\pi/2}.
 \tag{BFP.9}
$

它只需要完整 $G,G'$ 和 $f$ 的值，不需要旧192 Fourier observations，
也不需要在选择的 finite Fourier box 外假设真 $F^G$ 为零。

令 $\phi_j=j\pi/(2N)$、$N=8192$。所有新 point records 必须包含
同一原 G 的完整值球、其真实解析 derivative 的完整球以及全部 f。
$G'$ 由原 $K_{48}'(H_{24})H_{24}'$ 全 chain 形成，不以
相邻 grid 差分代替。设其整点有向 sum 为

$
 Q_N\ge\frac1N\sum_{j=0}^{N-1}
       \frac{(r(G(\phi_j))G'(\phi_j)-f(\phi_j))^2}{G'(\phi_j)} .
 \tag{BFP.10}
$

所有8192项保留，且每个 denominator lower 严格正。
$r(G(\phi_j))$ 使用相应整个复合 polynomial；迭代单位圆
disk residual 支付每一次幂与求和误差，不能再使用会指数包裹的
未经控制 rectangular power recurrence。

原整个 $G_1<2$ 给
$\|G'-1\|_{\mathcal A_\sigma}\le G_1-1<1$。Wiener algebra
Neumann 级数因此准确给

$
 \|(G')^{-1}\|_{\mathcal A_\sigma}\le(2-G_1)^{-1}.
 \tag{BFP.11}
$

以下新 finite weighted sums 必须使用所有2560和96 coefficients：

$
 A_r=2\sum_{n=1}^{2560}|r_n|e^{4n(\sigma+G_0)},\qquad
 A_f=2\sum_{n=1}^{96}|f_n|e^{4n\sigma}.
 \tag{BFP.12}
$

完整 composition 满足
$\|r\circ G\|_{\mathcal A_\sigma}\le A_r$，故 (BFP.9)
的 integrand（在实轴上等于其平方模表达式）之整个
$\mathcal A_\sigma$ norm 不超过
$(G_1A_r+A_f)^2/(2-G_1)$。
全 trapezoidal alias 只有非零 frequencies $kN$，所以

$
 E_{\rm alias}^{(2)}
   =e^{-4N\sigma}\frac{(G_1A_r+A_f)^2}{2-G_1}
 \tag{BFP.13}
$

覆盖其**整个** infinite alias series，而非一个首 omitted mode。
实轴 $r,G,f$ 全为实，故这里的 analytic square 与实平方模准确相同。
于是

$
 \boxed{\quad
 \|r-F^G\|_2\le\rho_{\rm fin}
          :=\operatorname{up}\sqrt{Q_N+E_{\rm alias}^{(2)}}.
 \quad}
 \tag{BFP.14}
$

$Q_N$ 与 (BFP.13) 均须整个保存读回后再形成 (BFP.14)。
即使粗 weighted sum 使 bound 大，也必须诚实保存整结果，
不能丢弃2560尾或预报门通过。

## BFP5. 真 w、PDE 与 full forward inverse error

由新 trial 定义形成完整

$
 I_2=\left(2\sum_{\ell=1}^{512}
                   \frac{|z_\ell|^2}{(4\ell)^2}\right)^{1/2},
 \qquad I_W=\sum_{\ell=1}^{512}\frac{|z_\ell|}{4\ell}.
$

same-sign orthogonality 给两个完整产品

$
 P_\infty=e_{w,\infty}I_2,\qquad
 P_2=\sqrt2 e_{w,2}I_W,\qquad
 \|\mathcal T_{w-\widehat w}I\widehat x\|_2
     \le P_*:=\min(P_\infty,P_2).
 \tag{BFP.15}
$

两候选均须先完整保存读回；负频和 infinite coefficient error
保留，不能从中挑选不一致的 mode 子项。

令 $W_{\rm tr}=2\sum_{n=1}^{2048}|\widehat w_n|$，
原 zero mean 精确为0，因而完整
$W_0=W_{\rm tr}+e_{w,\infty}\ge\|w\|_\infty$。
这是首次计算该 finite w 的整个 Wiener norm，旧 DWT2/BR7 没有
运行该 target。由 WBP.9 的同一个真正 onto inverse，

$
 \|\mathcal B^{-1}\|_{L^2_0\to L^2_0}\le K_{B,0}=1+W_0/4 .
 \tag{BFP.16}
$

准确分解完整 residual 给

$
 \|\mathcal B\widehat x-F_\nu\|_2
 \le \rho_B:=
 \rho_{\rm fin}+P_*+E_{\rm flow}+E_{\rm PDE}.
 \tag{BFP.17}
$

定义 $\widehat X=Q_a\widehat x$。真正 $F_\nu$ 和 $x_\nu$
均在 $Y_a^0$，而真 $\mathcal B$ 与 $Q_a$ 交换，$Q_a$ 是
正交投影，故

$
 \boxed{\quad
 \|x_\nu-\widehat X\|_2\le
 \delta_X:=K_{B,0}\rho_B .
 \quad}
 \tag{BFP.18}
$

此投影无需 finite $\widehat w$ 与 $Q_a$ 交换。
$\widehat X$ 的正交 target coordinates 准确为

$
 \beta_n=\langle\widehat x,v_n^a\rangle
       =\sqrt2\operatorname{Re}(z_ne^{2ina}),\quad1\le n\le512;
 \qquad \beta_n=0\quad(n>512).
 \tag{BFP.19}
$

必须使用整个真 $a$ ball；$\widehat X$ 是同一 true target 空间中的
finite reference，真实 $x_\nu$ 的高频从未被设零。
两 independent physical means 从 NP 原 whole 结果复制，仍在原
外部 slots，不由 (BFP.18) 变成 mean-height matching。

## BFP6. Whole Θ 对这整列的可执行消费

[UACT](R149-supplement-actual-original-finite-Theta-coordinate-inverse.md)
已提供新的全频

$
 \|V_Q-\widehat V_Q\|_{X_b^0\to\ell^2_{96}}\le E_V
$

以及原 entire OT dyadic $\widehat\Theta$ 与 full model rounding
upper $E_M$。原全局 error
$\|\Theta-\widehat\Theta\|_{Y_a^0\to\ell^2_{96}}\le E_\Theta$
也完整保留。分别消费对应整球，不能将 low96 error 冒充全频
$E_\Theta$。

按 [TM.2](R149-supplement-original-model-adjoint-on-complete-finite-Theta-rows.md)
的原 low reference 和所有 true signed Cayley multipliers，
$
 \overline Gv_n^a=\gamma_nu_n^b,\qquad
 \gamma_n=1\ (n\le96).
$
97–512 的 $\gamma_n$ 必须从原 entire2240 multiplier carrier
恢复并核原 SHA，不重跑7416项旧 gap。于是新 finite whole norm

$
 B_{\rm model}
  =\operatorname{up}\left(
       \sum_{n=1}^{512}|\gamma_n\beta_n|^2\right)^{1/2}
  \ge\|\overline G\widehat X\|_2
 \tag{BFP.20}
$

含全部512模式及 true mean/phase。另取新 trial 的完整
$B_x\ge\|\widehat x\|_2\ge\|\widehat X\|_2$。

整个96×2240 exact dyadic $\widehat\Theta$ 可形成一个此前未计算的
完整 trial operator upper $B_{\widehat\Theta}$，例如全
Frobenius bound；不把旧 GY norm 当成它。保存全部 entries 的 whole
SHA 后才求此 norm。故
$B_\Theta:=B_{\widehat\Theta}+E_\Theta\ge\|\Theta\|$。

新 signed vector 是所有96条完整配对
$
 d_j=\sum_{n=1}^{512}\widehat\tau_{jn}\beta_n.
 \tag{BFP.21}
$
取 exact signed centers $\widehat d_j$，把真 $a$ 和所有有向
rounding 的全96球半径作联合 $E_{\rm pair}$，则准确分解

$
 \begin{aligned}
 \Theta x_\nu-\widehat d={}&
 \Theta(x_\nu-\widehat X)
 +(V_Q-\widehat V_Q)\overline G\widehat X\\
 &+(\widehat V_Q\overline G-\widehat\Theta)\widehat X
 +(\widehat\Theta\widehat X-\widehat d)
 \end{aligned}
$

给完整真正 source/root $\Theta$-$\nu$ 列证书

$
 \boxed{\quad
 \|\Theta x_\nu-\widehat d\|_{\ell^2}
 \le B_\Theta\delta_X+E_VB_{\rm model}+E_MB_x+E_{\rm pair}.
 \quad}
 \tag{BFP.22}
$

完整 finite $B_{\rm model}$ 替代的是这条准确分解中的 finite
preimage norm，未减少任何真无限 error 项。
尤其不能以 BNC 的96低坐标补零后形成 (BFP.21)，也不能把 UACT
的12.588坐标逆代作原 full $\Theta$ norm。

## BFP7. 原输入、自然新目标和仍未付的接口

配套纯模块
[fourfold_codazzi_full_target_nu_forward_residual_math.py](../scripts/fourfold_codazzi_full_target_nu_forward_residual_math.py)
实现上述新 whole formulas。
actual owner 应首先准入整个 NP/PO/ASB/JC/DWTB9/UACT、
原 OT/CYA whole objects、同一个隐式 selected member 和全部 parent
bindings。必要恢复只核原 whole SHA；旧所有 norm/residual/gap/192
observations 目标调用数必须为0。

一次自然目标包括：新 w finite Wiener bound、新 forward trial
norms、全 pullback square/alias/finite residual、两 whole w products、
完整 flow/PDE payments、同一 full B residual/inverse error，以及
完整 finite model preimage、whole Θ trial norm和真正96维 signed列。
每个 whole scalar 先保存读回；所有2560 finite residual coefficients、
8192完整 grid records、512目标坐标和96配对也先完整保存。
大数组留 private，公开完整 receipts 与新 whole结论。

本条证明**如何实际认证缺失的完整列**，没有宣称这些新算术目标已完成。
BGR 的另一个完整 Gram 可在同次必要原 row restoration 后执行，
但现正在运行的 BNC7 完全不变。真实 homogeneous96、高逆/反馈、
两 physical mean、非局部 phase/height、regular defect 以及 full
physical Schur 继续分别存在；(BFP.18) 和 (BFP.22) 不替代它们。
