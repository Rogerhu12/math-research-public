# R133 续篇：原完整实参数区间上的固定基点全频帽线性逆

2026-11-15，visible-exact-astra-0df9。

**结论：同一显式族在原整个实区间 $|\delta|\le10^{-8}$ 上，完整帽主体与真实改变外边界的合计反馈小于 $3/8$，对应固定基点解算子的 Neumann 放大因子小于 $8/5$。** 这一结论不缩小原参数区间。下面把已实际完成的两个系数消费结果，逐项接入原 P、O 合同。

这里的“线性逆”是完整原 moving 方程在显式 $Q_\delta$ 处的导数逆，限制到同一个实际奇/偶反射类，并保持原固定内端非mean $C$ 数据。$Q_\delta$ 本身仍是连续修补后的显式近似族；本条不把它称为精确 PDE 解，不把固定基点模块上的线性结论扩成未知非线性背景域。

## 1. 同一对象、区间和完整端口

令
$$
 I=[9/10,25/8],\qquad
 Q_\delta=Q_0+\delta Z,\qquad \nu_\delta=\nu_0+\delta ,
 \qquad |\delta|\le10^{-8},\quad \delta\in\mathbb R .
 \tag{V.1}
$$
物理本征参数始终固定为 $\eta_0$。完整连续中心和完整方向定义的 SHA256 分别为

- 440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47；
- 6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04。

原 $Z$ 连续修补 native 是 87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88。193个真实 sine/cosine 状态包括独立 even mean；它没有再乘 alpha，也没有减少到有限未知态。有限193只描述这个已给系数方向，下面的未知线性变分仍有全部 $4\mathbb Z$ 频率，处于实际反射子空间。

帽区上的原 compact $\nu$ bump 恒为零，故 (V.1) 不改变该区间的 $\beta,\gamma,K$。所有本征界只用同一个原本征对象。真实外端 $R=25/8$ 的 long graph、独立 mean、真实高度与仿射源，均保留 [O1–15](R133-supplement-true-full-delta-outer-rows-in-fixed-base-cap-inverse.md) 的完整约定，包括该图已有的外背景高度解析入口。内端是 $r=9/10$ 上固定 $D\Psi_0$ 坐标的非mean $C$ 行，不把它换成随 $\delta$ 移动的新行。

背景与变分的反射约定由 [R1–17](R133-supplement-exact-reflection-sector-and-original-moving-cap-tail-bridge.md) 给出。该类上角规范 $A$ 及相应导数准确为零，所以这里确为原 moving 方程的导数问题。径向 $\Gamma^*$ 返回条件不由这个事实消失。

## 2. 实际已完成的联合系数和本征界

[完整 $Z$ 联合消费](../notes/2026-11-15-R133-actual-complete-cap-Z-joint-coefficient-bounds.md) 对原660个帽区 cubic 片逐状态取径向 supremum，再加原193修补界并求和。公开 Actions 43674204314/1 的 child0 和10门完整通过，授予
$$
 \|Z\|_{\mathscr A_{1/128},\mathrm{pair}}
       <0.869975739133<7/8 .
 \tag{V.2}
$$
这里复 Fourier 范数的权是 $e^{|n|/128}$，真实物理频率为 $n=4j$。每个非零实振幅等于其两个复系数绝对值之和；mean 权为1。

[原完整闭行本征消费](../notes/2026-11-15-R133-actual-cached-complete-cap-intrinsic-bounds.md) 的公开 Actions 43674917925/1 child0、9门通过。原4650闭行身份与完整覆盖先核验，再取与 $I$ 相交的1346个真实交段，得到
$$
 b_*=\sup_I|\beta|<5.639200000174<6,\qquad
 g_*=\sup_I|\gamma|<5.639200000174<6,
$$
$$
 K_*=\sup_I|K|<0.254600000149<1,\qquad
 k_*=\max(1,K_*)=1 .
 \tag{V.3}
$$
原证书同时保有帽区正 $K,\gamma$。这里仅需它们的绝对值上界；没有用根 germ 的局部上界替代完整帽区。

两个实际 native 的 SHA256 分别为 dd236bb30e17ed457a45bd38a24ff3188d896562e5e2e4189d5f3a5579cdc39c 和 145d6e558f8348bf2b29febc8700aa43cba2a507b3ba2d7fc7da5ea1db22cd2d。原过程、summary、artifact 身份与复用范围见上述实际记录。以下仅对已证明的上界作符号估计，不生成新的数值数据，也不重算旧 target、ODE、FFT、修补或 intrinsic 网格。

## 3. 固定角复合的联合范数：逐系数支付

帽区上的联合 Wiener 范数为
$$
 \|f\|_{\mathscr A_\sigma}
   =\sum_{n\in4\mathbb Z}e^{\sigma|n|}
                 \sup_{r\in I}|f_n(r)| .
 \tag{V.4}
$$
pair norm 是两分量之和。该范数满足乘积不等式；证明直接使用每个 Fourier 卷积项的径向 supremum，再对项求和。这里没有交换径向 supremum 与一个未经控制的 Fourier 和。

把角映射固定在 $Q_0$。沿用 [完整规范篇](R133-supplement-complete-normalized-angle-gauge-and-residual-Hessian.md) 的有符号 $m=\langle v\rangle_\varphi$、$C$ 和 $\Phi_0$。G.2 与 G.23 给
$$
 \Phi_0(\theta)=\theta+I_\theta(mC-1),\qquad
 \|mC-1\|_{\mathscr A_0}<1/32 .
 \tag{V.5}
$$
第二个范数已明确是同一联合径向/系数范数。G.2 的角均值规范确保 (V.5) 没有另一个未知常相位。由于所有非零频率的绝对值至少为4，
$$
 \chi_0=\Phi_0-\mathrm{id},\qquad
 \|\chi_0\|_{\mathscr A_0}
 \le\frac14\|mC-1\|_{\mathscr A_0}<1/128 .
 \tag{V.6}
$$
这一步使用 $m(r)$ 原符号，不把负 $m,C$ 替换为绝对值后重定义映射。

对于任一有界联合解析系数列，
$$
 f(r,\Phi_0(r,\theta))
 =\sum_n f_n(r)e^{in\theta}\exp(in\chi_0(r,\theta)).
$$
由 (V.4) 的 Banach 代数乘积和指数级数绝对收敛，
$$
 \|\exp(in\chi_0)\|_{\mathscr A_0}
 \le\exp(|n|\|\chi_0\|_{\mathscr A_0}),
$$
从而
$$
 \|f\circ\Phi_0\|_{\mathscr A_0}
 \le\sum_n\sup_I|f_n|\exp(|n|\|\chi_0\|_{\mathscr A_0})
 \le\|f\|_{\mathscr A_{1/128}} .
 \tag{V.7}
$$
该证明保留 $f_n(r)$ 与 $\chi_0(r,\theta)$ 的真实径向依赖。组合后一般产生无限多个 Fourier 模，但完整级数已由 (V.7) 支付。常数模本身也保留。

在 [P1–21](R133-supplement-fixed-base-conservative-source-transport-and-nearby-cap-linearization.md) 中，帽号准确表示与同一个固定 $\Phi_0$ 复合。因此 (V.2)、(V.7) 给
$$
 \varepsilon
 =\|\widehat{Q_\delta-Q_0}\|_{\mathscr A_0,\mathrm{pair}}
 \le |\delta|\,\|Z\circ\Phi_0\|_{\mathscr A_0,\mathrm{pair}}
 <\frac78\,10^{-8}<2^{-26}.
 \tag{V.8}
$$
最后只用整数比较 $2^{26}=67108864<10^8$。没有估计随未知态变化的复合算子与恒等算子的同阶差。

## 4. 完整主体条件在原区间成立

P.19 要求
$$
 \varepsilon\le\frac{2^{-22}}{k_*(1+b_*+g_*)}.
 \tag{V.9}
$$
由 (V.3)，$k_*(1+b_*+g_*)<13<16$，所以
$$
 \frac{2^{-22}}{k_*(1+b_*+g_*)}>2^{-26}>\varepsilon .
 \tag{V.10}
$$
条件在整个 (V.1) 上严格成立。于是 P.17–P.19 在其原固定物理模块 $\mathfrak M$ 中给
$$
 \|\mathcal K_{\mathrm{body},\delta}\|_{\mathfrak M\to\mathfrak M}
 <1/4 .
 \tag{V.11}
$$

这包含原完整四个 primitive 项、两类 gamma mean 秩项及所有 ordinary 项。P.5–P.7 已准确把 moving 散度变成固定物理散度与 mean 项。原 $D\Psi_0$ 的径向导数、非解中心 $R_0$ 的完整 Hessian 和已付原 jump 始终留在同一个基逆内。故 (V.11) 不需要 $Y_r$、新的 $R_\delta$ Hessian 或重新计算一个 nearby residual。

未知变分的范数仍是原 $\mathfrak M$。这里只要求已给系数 $Y=\delta Z$ 具有 (V.8) 的联合代数界，没有从 $\mathfrak M$ 输出擅自推断任意未知非线性修正也属于 $\mathscr A_0$。

## 5. 与真实改变外边界合成

O.14 已在同一整个实区间、同一 fixed-base 模块证明
$$
 \|\mathcal K_{\mathrm{outer},\delta}\|
 <\frac{10824}{100000}<1/8 .
 \tag{V.12}
$$
其原证明包含真实外 Robin 行、独立 even mean、准确仿射 lift、端点反馈和正 $q_*$ 权；内端非mean $C$ 数据固定。该界没有把外界面冻结在 $\delta=0$，也没有把 $H^1$ 算子范数直接冒为 $L^2$ 范数。

将全部给定 ordinary/divergence 源、原 affine jump、固定内端数据和真实外两行源准确提升到基点，记这个已支付的完整基点响应为 $x_{\mathrm{aff},\delta}$。完整线性方程在原模块中准确写成
$$
 x=x_{\mathrm{aff},\delta}
     +(\mathcal K_{\mathrm{body},\delta}
                       +\mathcal K_{\mathrm{outer},\delta})x .
 \tag{V.13}
$$
因此
$$
 \|\mathcal K_{\mathrm{body},\delta}
                       +\mathcal K_{\mathrm{outer},\delta}\|<3/8 ,
 \qquad
 \|(I-\mathcal K_{\mathrm{body},\delta}
                       -\mathcal K_{\mathrm{outer},\delta})^{-1}\|<8/5 .
 \tag{V.14}
$$
(V.14) 是相对 O、P 已定义完整基点 lift 的放大因子，不是任意改单位后的绝对源范数常数。所有独立源列继续按原单位取值。给定兼容数据时解存在且唯一；不满足原 mean/通量兼容的数据仍保留其真实兼容荷，不改称齐次物理问题的解。

把 $x$ 经原完整 $(D\Psi_0)^{-1}$ 还原，得到原 moving 变分，包括 even mean 与真实相位规范。此还原、内端约束及真实外方程是同一个线性边值问题，而不是仅有限97或193态的矩阵逆。

## 6. 当前闭合的子项和后续接口

本条闭合了完整帽区上 P.19 尚缺的实际系数条件，并把它与 O.14 真实改变外边界相接。帽区同一显式族的全频线性逆在整个原 $|\delta|\le10^{-8}$ 上成立，不再留下“待取得完整帽区 beta/gamma/K”或“待支付固定角联合组合”的条件。

仍须保留以下后续量词：

1. 本条没有得到一般高阶或负阶 $\delta$ 一致 Sobolev 逆；那些阶数需各自支付乘子、端口与共轭费用。
2. $3/8$ 是完整可逆性上界，不是精细的 $\nu$ 方向误差。把该帽逆转授给原 signed97 Poisson/误差矩阵时，须保持原 physical 行单位和实际参数相关性。
3. 本条不改变内主体的完整 Green、强返回、修正 seam、高频截断充分性或参数 Schur 的待证事项。
4. 对未知非线性修正，必须另外证明同域系数球、真实改变边界及可重复的解图。线性可逆性不等于精确非线性族已经存在。
5. 全局 holonomy、材料 held 区、闭合与嵌入、reach、固定四点及可见非刚性仍按本课题 README 的同一族完成门处理。

原有限矩阵、Green、Poisson、几何证书及全部失败/成功原记录均保留。本结论没有产生或宣称最终闭等距族。
