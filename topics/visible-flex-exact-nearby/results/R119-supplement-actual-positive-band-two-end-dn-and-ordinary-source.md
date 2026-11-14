# R119 续篇：实际正型分量的完整两端弱 DN、普通源与 holonomy 通量

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 在同一个真实 $\ell^1_{224}$ 尾图上，每个实际
正型有限分量都具有完整两端 Dirichlet 解、弱 DN 和连续普通 scalar
source 解。真实角图先被准确共轭；在原径向两端能量迹空间上，更新
DN 的全频相对误差小于 $2^{-430}X_{224}$。所有频率、两端互相反馈
和 mean/平移均保留，包括型别零点作为端点的情形。

所用能量迹空间由同一真实径向 Sturm 传递矩阵明确给出，不是有限模
近似。这里证明的是这个具体能量空间中的弱边界算子；它与整个尾的
已安装 Airy/strong-source 范数之间的统一强比较、负型 return 相位及
全高输入逆仍须继续支付。
零标签时所有比较误差准确为0；下文以 $X_{224}>0$ 写严格预算，
其零标签极限按等式理解。

## 1. Raw 高度的准确 selfadjoint divergence

采用前几篇的原几何与相对变量
$$
 E=1+w^2,\quad J=1+K+EU,\quad
 D=1-w^2(2K+K^2+EP^2),\quad
 d=\frac{E(V-P)}J,\quad v=\frac{\sqrt D}{J},\quad \rho=D^{-3/2}.
$$
$h$ 在本篇表示正参考高度扰动的 Jacobi 变化，因此
$\dot P=h_\theta/(aw)$、$\dot K=h_t/(aw)$。
北侧实际垂直高度的变化是 $-h$，不能混淆这个共同号数。
source 仍按原合同 $\dot K_t-D F[\dot P,\dot K,\dot U,\dot V]=e$。

把上述两个导数代入真 Jacobi 方程，准确得到
$$
 h_{tt}-2d h_{t\theta}+(d^2+Av^2)h_{\theta\theta}
       -(A+1+F_K)h_t-F_Ph_\theta=aw\,e.
 \tag{P.1}
$$
定义真实正系数
$$
 \mu=\frac wa J\rho,\qquad
 \mathsf M_h=\mu\begin{pmatrix}1&-d\\-d&d^2+Av^2\end{pmatrix}.
 \tag{P.2}
$$
完整方程准确为
$$
 \boxed{\quad
 \operatorname{div}_{t,\theta}(\mathsf M_h\nabla h)
       =s_h,\qquad s_h=w^2J\rho\,e.
 \quad}                                                     \tag{P.3}
$$
它不是只有 principal 相同的模型。可直接核两个一阶系数：
$$
 (\log\mu)_t-d(\log\mu)_\theta-d_\theta=-(A+1+F_K),
$$
$$
 -d_t-d(\log\mu)_t+(d^2+Av^2)_\theta
          +(d^2+Av^2)(\log\mu)_\theta=-F_P.
 \tag{P.4}
$$
代入 $\log\mu=\log(w/a)+\log J-\tfrac32\log D$、
$w_t=Aw$ 和完整四态 PDE 后，两式逐项恒等。
相邻脚本使用独立 $U_\theta,V_\theta$ 验到余项为0。
常高度 $h=1$ 是此 raw 方程的准确平移解。

其沿正 $t$ 方向的真实 raw conormal 密度是
$$
 p_h=\mu(h_t-dh_\theta)
     =w^2\rho[J\dot K-E(V-P)\dot P].
 \tag{P.5}
$$
这个 raw 通量不直接等于 R37 grounded 通量；后者仍需完整
normal/shear 和水平变化转换。

## 2. Raw 通量的 mean 恰为完整 holonomy 变化

原 holonomy 被积式是
$$
 G=\left(1+\frac{w^2(1+K)U}{1-w^2P^2}\right)D^{-1/2},
 \qquad M=\langle G\rangle.
$$
其完整 Euler 导数准确满足
$$
 G_K=w^2\rho J,\qquad
 G_P-\partial_\theta G_U=-w^2\rho E(V-P).
 \tag{P.6}
$$
对 $\dot U=(\dot P)_\theta$ 积分分部，得到
$$
 \boxed{\quad \langle p_h\rangle=\dot M,\qquad
             \partial_t\langle p_h\rangle=\langle s_h\rangle. \quad}
 \tag{P.7}
$$
所以此 selfadjoint 表示没有另外制造或删除一个 mean 通量行。
任意普通 source 造成的 holonomy 负荷按 (P.7) 保留；真实标签列
$e=0,\dot M=0$ 的相同条件也保持。

## 3. 同一真角流消交叉项后的相对系数

使用
[一阶尾框架](R119-supplement-unscalarized-tail-frame-and-summable-remainder.md)
中已构造的真正漂移流
$\phi_t=-d(t,\phi)$、$j=\phi_\eta>0$。
这里需要高度函数与通量密度的不同变换：
$$
 \widetilde h=h\circ\phi,\quad
 \widetilde p=j(p_h\circ\phi),\quad
 \widetilde s=j(s_h\circ\phi).
 \tag{P.8}
$$
准确得到
$$
 \partial_t(\widetilde\mu\,\widetilde h_t)
 +\partial_\eta(\widetilde\beta\,\widetilde h_\eta)
       =\widetilde s,\qquad
 \widetilde p=\widetilde\mu\,\widetilde h_t,
 \tag{P.9}
$$
其中
$$
 \widetilde\mu=\frac wa\,j(JD^{-3/2})\circ\phi,\qquad
 \widetilde\beta=\frac wa\,A\,\frac{(D^{-1/2}/J)\circ\phi}{j}.
 \tag{P.10}
$$
原径向系数是 $\mu_0=w/a$、$\beta_0=A\mu_0$。

同一实际域的完整状态及真角 Jacobian 已满足
$$
 n_{\max}<2^{-447}X_{224},\qquad
 \|j-1\|_{\mathcal A_2}<2^{-435}X_{224},\qquad X_{224}<1.
$$
直接的 Banach 代数给
$$
 \|JD^{-3/2}-1\|_{\mathcal A_3}\le10n,\qquad
 \|D^{-1/2}/J-1\|_{\mathcal A_3}\le10n .
$$
真角复合已经有宽3到宽2的余量。故可统一取
$$
 \varepsilon_*=2^{-430}X_{224},\qquad
 \left|\frac{\widetilde\mu}{\mu_0}-1\right|<\varepsilon_*,
 \quad
 \widetilde\beta=A\mu_0(1+\epsilon_\beta),
 \quad|\epsilon_\beta|<\varepsilon_* .
 \tag{P.11}
$$
在 $A=0$ 端点第二式仍按因子形式成立，没有除以0。
本篇以下使用真实实背景，因而这些都是正实系数的相对比较。

完整两端数据必须是
$h(t_-,\cdot)\circ\phi(t_-,\cdot)$ 和
$h(t_+,\cdot)\circ\phi(t_+,\cdot)$；两端使用各自真实的角图。
不能把它们换回原角而同时忘掉 pullback。这个记录保留与相邻负型
段接合时真正的角相位。

## 4. 原径向的全部两端能量迹空间是明确的

取实际有限区间 $I=[t_-,t_+]$，要求 $A\ge0$，且在某个开子区间
严格为正。它可取任一真实正型分量的闭包，端点允许 $A=0$。
每个固定实际分量上 $\mu_0>0$ 连续；不把无限平尾端误当此有限
区间的正系数端点。

定义原径向能量
$$
 \mathscr E_0(u,z)=\int_I
    \left\langle\mu_0u_t\overline{z_t}
                      +A\mu_0u_\eta\overline{z_\eta}\right\rangle\,dt.
 \tag{P.12}
$$
对全部 $m\in4\mathbb Z$，真径向状态 $(u_m,p_m)$ 的传递系统为
$$
 \frac d{dt}\begin{pmatrix}u_m\\p_m\end{pmatrix}
 =\begin{pmatrix}0&\mu_0^{-1}\\m^2A\mu_0&0\end{pmatrix}
       \begin{pmatrix}u_m\\p_m\end{pmatrix},\qquad
 \Phi_m(t_+,t_-)=
     \begin{pmatrix}\alpha_m&\beta_m\\\gamma_m&\delta_m\end{pmatrix}.
 \tag{P.13}
$$
这是原安装 profile 的准确 Sturm 方程，不是另选势。
$\det\Phi_m=1$。从初值 $(0,1)$ 的解看，
$u'>0,p'\ge0$，所以 $\beta_m>0$，包括 $m=0$。

于是完整两端 outward DN 矩阵明确为
$$
 \boxed{\quad
 \mathsf S_m=\frac1{\beta_m}
       \begin{pmatrix}\alpha_m&-1\\-1&\delta_m\end{pmatrix}.
 \quad}                                                     \tag{P.14}
$$
它输出 $(-p_m(t_-),p_m(t_+))$，保留反射和两端互相耦合。
对 $m\ne0$，$\mathsf S_m$ 正定，因为能量为0会同时迫使
$u_t=0$ 和 $mu=0$。对 mean，
$$
 R_I=\int_I\mu_0^{-1}dt,\qquad
 \mathsf S_0=R_I^{-1}
       \begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
 \tag{P.15}
$$
唯一零方向是共同平移 $(1,1)$，没有删除 mean 高度差或 mean flux。

对平滑两端数据 $f=(f_-,f_+)$，定义
$$
 \|f\|_{\mathcal T_I^0}^2
 =\sum_{m\in4\mathbb Z}f_m^*\mathsf S_m f_m,\qquad
 \lambda(f)=\frac{(f_-)_0+(f_+)_0}{2},\qquad
 \|f\|_{\mathcal T_I}^2=
       \|f\|_{\mathcal T_I^0}^2+|\lambda(f)|^2.
 \tag{P.16}
$$
取其完备化；$\mathcal T_I^0$ 是除共同常数后的 Hilbert 空间。
由 (P.13) 的全部径向解，其真 harmonic lift $H_0f$ 的能量准确
等于 (P.16) 的第一项。这提供了明确的全频迹空间与范数，
不是用一个尚未证明的非线性逆来定义范数。
作为存在性检查，用两端数据的径向线性插值作竞争者即可把每模能量
上界写成同一有限区间常数乘 $(1+m^2)|f_m|^2$；故所有平滑两端
数据确实具有有限能量，不需对指数大的单个传递矩阵条目另作假设。

## 5. 实际完整弱 Dirichlet 解和相对 DN

令 $\mathcal V_0(I)$ 为两端高度为0的平滑函数在 (P.12) 中的
完备化。径向正系数和一维 Poincaré 控制其 $L^2$，所以该 norm
不退化。实际能量记为
$$
 \mathscr E_a(u,z)=\int_I
   \langle\widetilde\mu u_t\overline{z_t}
                 +\widetilde\beta u_\eta\overline{z_\eta}\rangle\,dt.
$$
(P.11) 给完整双边比较
$$
 (1-\varepsilon_*)\mathscr E_0(u,u)
 \le\mathscr E_a(u,u)
 \le(1+\varepsilon_*)\mathscr E_0(u,u).
 \tag{P.17}
$$
所有模式和型别零点都在同一 form 内，不需在零点先除以 $A$。

对每个 $f\in\mathcal T_I$，在 $H_0f+\mathcal V_0(I)$ 最小化
$\mathscr E_a$。实际 form 的强制性和 Hilbert 完备性给唯一修正，
故得到全部高输入的真弱解 $H_af$，独立平移常数按输入保留。
这个解满足 (P.9) 的齐次方程。其完整两端 DN 由
$$
 \langle\mathcal N_af,g\rangle
       =\mathscr E_a(H_af,H_ag)
 \tag{P.18}
$$
定义，是对全部 smooth 边界通量的唯一连续延伸。

对任意 $f$ 比较两个最小值，立即得到
$$
 (1-\varepsilon_*)\mathcal N_0
       \le\mathcal N_a\le(1+\varepsilon_*)\mathcal N_0,
 \qquad \mathcal N_0=\bigoplus_m\mathsf S_m .
 \tag{P.19}
$$
两者均在共同常数上为0。在 $\mathcal T_I^0$ 中用 Riesz 表示，
这是一个 selfadjoint 算子的区间界，因而完整相对 norm 满足
$$
 \boxed{\quad
 \|\mathcal N_a-\mathcal N_0\|_{\mathcal T_I^0\to
                                      (\mathcal T_I^0)^*}
 <2^{-430}X_{224}.
 \quad}                                                     \tag{P.20}
$$
这里是更新后真实所有角模的 DN 界，不是某些标签列的绝对小误差。
但它始终在 (P.8) 已明示的实际两端角图内。

## 6. 连续普通 source、两端通量及 mean 负荷

对零 Dirichlet 体空间的任意连续反线性泛函 $\mathcal F$，实际
有源解 $z_a\in\mathcal V_0$ 由
$$
 \mathscr E_a(z_a,\zeta)=-\mathcal F(\zeta),\qquad
                         \zeta\in\mathcal V_0
 \tag{P.21}
$$
唯一确定，并且
$$
 \|z_a\|_{\mathscr E_0}\le
       \frac{\|\mathcal F\|_{\mathcal V_0^*}}{1-\varepsilon_*}.
 \tag{P.22}
$$
若 $\mathcal G_a$ 表示这个带准确负号的 Green 解，则
$$
 \|\mathcal G_a-\mathcal G_0\|_{\mathcal V_0^*\to\mathcal V_0}
 \le\frac{\varepsilon_*}{1-\varepsilon_*}.
 \tag{P.23}
$$
由减去 (P.21)、再用 (P.17) 直接证明。

为给真正连续体源一个具体充分合同，定义两个原 profile 积分
$$
 R_I=\int_I\mu_0^{-1}dt,\qquad
 M_I=\int_I A\mu_0\,dt>0,\qquad
 C_I=1+2\sqrt{R_I}+\frac1{4\sqrt{M_I}}.
 \tag{P.24}
$$
它们是同一已安装有限区间的明确正数，没有换成未授权的常势。
对任何平滑 $u$，将非mean部分在径向作 $A\mu_0$ 加权平均，
并用全部非零四重频率的 Poincaré 常数 $1/4$；再对径向差用
Cauchy–Schwarz，即得
$$
 \sup_{t\in I}\|u(t)\|_{L^2_\eta}
 \le C_I\bigl(\mathscr E_0(u,u)+|\lambda(u)|^2\bigr)^{1/2}.
 \tag{P.25}
$$
具体地，非mean的加权平均 norm 至多
$\mathscr E_0^{1/2}/(4\sqrt{M_I})$，从任意径向点到该平均的差
至多 $\sqrt{R_I}\mathscr E_0^{1/2}$；mean 从其两端平均的差也
至多 $\sqrt{R_I}\mathscr E_0^{1/2}$。

因此对真实普通密度源
$\widetilde s=j(w^2J\rho e)\circ\phi$，一个完整充分源 norm 是
$$
 \mathcal S_I=C_I\int_I\|\widetilde s(t)\|_{L^2_\eta}\,dt.
 \tag{P.26}
$$
它使 $\mathcal F(u)=\int_I\langle\widetilde s\,\overline u\rangle dt$
在含独立常高度的能量空间上 norm 不超过 $\mathcal S_I$。
故 (P.22) 的右侧可取 $\mathcal S_I/(1-\varepsilon_*)$。

由完整 Green 恒等式，普通 source 造成的两端 outward flux 泛函为
$$
 \langle q_{\mathcal F},g\rangle
       =\mathcal F(H_ag),
 \qquad
 (-\widetilde p(t_-),\widetilde p(t_+))
                  =\mathcal N_af+q_{\mathcal F}.
 \tag{P.27}
$$
用 (P.17)–(P.19) 得
$$
 \|q_{\mathcal F}\|_{\mathcal T_I^*}
 \le\sqrt{\frac{1+\varepsilon_*}{1-\varepsilon_*}}\,\mathcal S_I
 <2\mathcal S_I .
 \tag{P.28}
$$
其共同平移测试方向准确给
$$
 \langle q_{\mathcal F},(1,1)\rangle
 =\int_I\langle\widetilde s\rangle\,dt
 =\dot M(t_+)-\dot M(t_-).
 \tag{P.29}
$$
这是保留的独立 mean 负荷，不属于被 quotient 掉的齐次 DN 核。
对整个无限尾若有各段 source，必须按实际 (P.26) 支付相应和；
本篇不宣称这些 $C_I$ 在所有层免费统一，也不将此合同改称 R37
任意 metric-source 的现成强 norm。

## 7. 与真实转向接口的范围

本篇给出了实际正型分量的完整弱两端解、普通源和更新 DN，系数比较
跨 $A=0$ 的端点仍合法。它不依赖“把负型振荡公式移到正型区”。
真实原径向两端矩阵 (P.14) 已指定全部输入、输出及平移方向；
两个端点的真角图和 raw/grounded 物理转换仍保留。

接下来需要将 (P.14)–(P.28) 的明确能量空间与安装的转向
height/flux 强范数作全频、全层比较，并把这些正型边界算子与实际
负型射线 return 联立。前篇的 Airy 能量门不能自动提供这一比较，
本篇的相对 DN 门也不能自动提供全尾高输入横截或最终相位选择。

[准确系数、mean 与预算程序](../scripts/fourfold_positive_band_two_end_dn_20261113.py)
和 [报告](../notes/2026-11-13-R119-positive-band-two-end-dn-budget.json)
核验 (P.3)–(P.7) 的完整恒等式及实际相对常数。
