# R84：真实复时间参数源、转折消根、降阶小帽和有符号参数密度

**状态：已证明。** 本文给出同一个准确 affine 对象的实际参数源构造和全部误差接口，
并记录普通段 419、转折段 0 及跨芽段 4 已完成的计算。
这不是完整前腿、完整返回、非零 twist 或最终 KAM 的证明。
中心参数模数和实参数盒的一致模数始终分开。

## 1. 准确对象和导数的含义

取 R80 的准确 affine、显式偶奇对称、完整无限角原函数对象，中心参数为

$$
p_0=-\frac{7789843107295549}{4611686018427387904}.
\tag{84.1}
$$

对象、原点和方向由以下 SHA256 确定：

| 输入 | SHA256 |
|---|---|
| step5 object | 91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848 |
| 准确原点 | 0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b |
| 准确方向 | 8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab |
| 中心简单根证书 | 489268d254c2a9454ccbee32a4821d9bf577279490f76c9cc6f8d902a5e64e0b |
| 参数无关 retarget descriptor | 097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052 |

在一个明确选择的共同样条芽上，写

$$
F(r,\theta,p)=a(r,p)\mathcal P_\theta T(r,\theta,p)+Z(r,p)e_z,\qquad X=F_r,
\tag{84.2}
$$

其中 $\mathcal P_\theta$ 是固定零均值的完整 Cartesian 角原函数，不以有限 DFT 重定义。
所有 $a,Z,\beta,\gamma$ 的参数依赖来自同一 affine 控制点方向。置

$$
D=(X\times T)\cdot T_\theta,\quad M=(X\times T)\cdot T_r,\quad
W=(X\times T)\cdot(X\times T),\quad
K=\frac{a'E'-2a''E}{2aE^2},\quad E=\langle F_r\cdot F_r\rangle.
\tag{84.3}
$$

复延拓中点积为复双线性，不能换成 Hermitian 内积。
真实正简单根为 $t(p)$；固定物理时间 $\tau$ 时 $r=t(p)\sin\tau$，分支场为

$$
f_\varepsilon(\tau,\theta,p)
=-t(p)\cos\tau\,\frac{M+\varepsilon\sqrt{-K}\,W}{D},
\qquad \varepsilon\in\{-1,1\}.
\tag{84.4}
$$

普通芽用已付的 $\operatorname{Re}(-K)>0$ 分支，转折用第 4 节。
参考子段的准确时间为 $\tau=\tau_c+hu$，$-1\le u\le1$。
本文 $f_p,f_{pp}$ 均为**固定 $\tau,\theta$** 的真实导数，包含 $t',t''$。

## 2. 复径向输入中的真实均值

固定 $r,\theta$ 求导，因为 $a_{pp}=Z_{pp}=0$，

$$
F_p=a_p\mathcal P_\theta T+a\mathcal P_\theta T_p+Z_p e_z,\qquad
F_{pp}=2a_p\mathcal P_\theta T_p+a\mathcal P_\theta T_{pp}.
\tag{84.5}
$$

这是 affine 输入的准确链式，不是把 $F$ 线性化。由此

$$
E_p=2\langle F_r\cdot F_{rp}\rangle,\qquad
E_{pp}=2\langle F_{rp}\cdot F_{rp}+F_r\cdot F_{rpp}\rangle.
\tag{84.6}
$$

有限 Fourier 和、无限尾及舍入由 R80 的完整原函数参数预算支付。
在复 $r$ 上，$E,E_p,E_{pp}$ 都保持为复球；只在已证为实的根处取实部。
实际零频配对是 $\sum_kX_k\cdot X_{-k}$。

令 $C=a'E'-2a''E$、$B=2aE^2$、$\ell=a_p/a+2E_p/E$，则

$$
\begin{aligned}
C_p&=a_p'E'+a'E_p'-2a_p''E-2a''E_p,\\
C_{pp}&=2a_p'E_p'+a'E_{pp}'-4a_p''E_p-2a''E_{pp},\\
K_p&=C_p/B-K\ell,\\
K_{pp}&=C_{pp}/B-2K_p\ell-K(\ell^2+\ell_p),\\
\ell_p&=-(a_p/a)^2+2E_{pp}/E-2(E_p/E)^2.
\end{aligned}
\tag{84.7}
$$

每次除法要求同一复域的 $a,E$ 排零。无限原函数尾按 Cauchy 公式扩到所需径向阶。
归一化参数 jet $(A_0,A_1,A_2)$ 表示
$A(p+\epsilon)=A_0+\epsilon A_1+\epsilon^2A_2+o(\epsilon^2)$，
乘积用卷积，真实二阶导数输出为 $2A_2$。若 $r_p=b,r_{pp}=c$，复合为

$$
\dot A=A_p+bA_r,\qquad
\ddot A=A_{pp}+2bA_{rp}+b^2A_{rr}+cA_r.
\tag{84.8}
$$

全部源、平方根和有限参数矩形均用这个二阶规范。

## 3. 真实根导数和整个复角带的源模数

在 R58/R80 的实际简单根分支上，

$$
t'=-K_p/K_r,\qquad
t''=-\frac{K_{pp}+2t'K_{rp}+(t')^2K_{rr}}{K_r}.
\tag{84.9}
$$

实现以完整无限均值在精化真实中心根计算各项，检查 $K_r>0$、$0\in K(t)$，
再与已付实分支导数区间相交。没有使用旧 binary64 根中心。
中心实际得到

$$
\begin{aligned}
t'(p_0)&=6.110799498997630373224016\ldots\,10^{-5},
&\operatorname{rad}<3.593\,10^{-30},\\
t''(p_0)&=-9.40286391462846346793035\ldots\,10^{-7},
&\operatorname{rad}<7.650\,10^{-31}.
\end{aligned}
\tag{84.10}
$$

报告中的有向球是实际输入；这些窄中心球不替代较大参数盒上的区间。

对全角带 $|\operatorname{Im}\theta|\le S$，复径向相位系数可能不实，因此取

$$
I=S+\sum_k\left(
|\operatorname{Re}\beta_k|\sinh(4kS)+|\operatorname{Im}\beta_k|\cosh(4kS)
+|\operatorname{Re}\gamma_k|\sinh(4kS)+|\operatorname{Im}\gamma_k|\cosh(4kS)
\right).
\tag{84.11}
$$

复旋转算子模给 $\|T\|\le e^I$。零均值 Cartesian 原函数核的 $L^1$ 模为 $\pi/2$，
所以 $\|X\|\le(\pi/2)\|\partial_r(aT)\|+|Z_r|$。
用非负混合 jet 对这些公式逐项求导、乘法、复合，即给 $D,M,W$ 的完整模数。
这一步没有除以 $D$，可用于第 7 节而不循环。

若实际 $|D|\ge d>0$，$V=A/D$ 的归一化参数系数可按

$$
|V_0|\le |A_0|/d,\qquad
|V_j|\le\frac{|A_j|+\sum_{i=1}^j|D_i||V_{j-i}|}{d},
\quad j=1,2
\tag{84.12}
$$

估计。若 $\operatorname{Re}Q\ge\mu>0$，则平方根系数满足

$$
|\sqrt Q|_0\le\sqrt{|Q_0|},\quad
|\sqrt Q|_1\le\frac{|Q_1|}{2\sqrt\mu},\quad
|\sqrt Q|_2\le\frac{|Q_2|}{2\sqrt\mu}+\frac{|Q_1|^2}{8\mu^{3/2}}.
\tag{84.13}
$$

与 (84.8) 及完整 $t\cos\tau$ 二阶乘积结合，给全复时间盘、全角带的
$f,f_p,f_{pp}$ 模数。粗模数用于解析重建尾；小的节点值不替代该连续模数。

## 4. 转折的三个准确零常数和全部径向尾

在正根附近令 $\rho=t(p)-r$，
$\widehat K(\rho,p)=K(t(p)-\rho,p)$。固定 $\rho$ 有

$$
\widehat K_p=K_p+t'K_r,\qquad
\widehat K_{pp}=K_{pp}+2t'K_{rp}+(t')^2K_{rr}+t''K_r.
\tag{84.14}
$$

准确恒等式 $K(t(p),p)=0$ 证明这三种源在 $\rho=0$ 的常数都为零。因此

$$
J_j(\rho,p)=-\frac{\partial_p^j\widehat K(\rho,p)}{\rho},
\qquad j=0,1,2
\tag{84.15}
$$

解析。代码只删这三个已证明准确为零的项，不把一般含零球任意设零。

若 $|\partial_p^j\widehat K|\le M_j$ 于 $|\rho|\le R_K$，
保留 $J_j$ 的前 $L$ 项，$q=|\rho|/R_K<1$，其第 $d$ 个径向导数尾至多

$$
\frac{M_j}{R_K^{d+1}}\sum_{n=L}^\infty(n)_d q^{n-d}.
\tag{84.16}
$$

对 $d=0,1,2$，三个级数准确为

$$
\frac{q^L}{1-q},\quad
\frac{Lq^{L-1}}{1-q}+\frac{q^L}{(1-q)^2},\quad
\frac{L(L-1)q^{L-2}}{1-q}
+\frac{2Lq^{L-1}}{(1-q)^2}+\frac{2q^L}{(1-q)^3}.
\tag{84.17}
$$

证明是对真实外圆用 Cauchy 系数界后求几何级数；包括 $R_K^{-d}$ 导数费用。
实际 sine 支为 $\tau\in[-\pi/2,\pi/2]$。端点距离记 $\eta$，
$r=t\cos\eta$（负端使用已证反射），则

$$
\rho=t(1-\cos\eta),\qquad
-K=\sin^2\eta\,Q,\qquad
Q=\frac{tJ_0(t(1-\cos\eta),p)}{1+\cos\eta}.
\tag{84.18}
$$

固定 $\tau$ 时 $\eta$ 固定，$\rho_p=t'(1-\cos\eta)$、
$\rho_{pp}=t''(1-\cos\eta)$。把 (84.8) 用于 $J_0$，
其中固定 $\rho$ 参数导数为 $J_1,J_2$，再乘完整 $t$ jet。
二阶乘积特别包含 $t''J_0+2t'(J_1+\rho_pJ_{0,\rho})$。
最后用

$$
\sqrt{-K}\ \hbox{的解析转折表示}=\sin\eta\sqrt Q
\tag{84.19}
$$

及实际 $\operatorname{Re}Q>0$ 求导。
这给端点有限的 $f_p,f_{pp}$，没有对未消根方根反复除零。
合并后的根平移链式准确回到 $r_p=t'\cos\eta$、$r_{pp}=t''\cos\eta$，没有双计。

## 5. 原生参数源和无限原函数费用

ParameterTimeCircleField.sample 在每个复时间节点原生计算全部物理角节点的
$[f,f_p,f_{pp}]$ 球，使用同一个真实芽的 $F,F_p,F_{pp}$、
$T,T_r,T_\theta$，不是射线差商。
设三种原函数源统一尾为 $e_0,e_1,e_2$，局部 Cauchy 半径 $R_0$，
$b=r_p,c=r_{pp}$。$X$ 的归一化参数三项所加半径依次是

$$
\frac{e_0}{R_0},\quad
\frac{e_1}{R_0}+\frac{2|b|e_0}{R_0^2},\quad
\frac12\left(\frac{e_2}{R_0}+\frac{4|b|e_1}{R_0^2}
+\frac{6|b|^2e_0}{R_0^3}+\frac{2|c|e_0}{R_0^2}\right).
\tag{84.20}
$$

这些正是 (84.8) 用于 $F_r$ 的 Cauchy 导数费。
共同外预算同时将 $R_0,R_E$ 加上真实 sine 像半径，保持差值；
每个节点的原函数和均值导数仍用节点自身的 $R_0,R_E$。
相位有限不等于其指数或原函数有限。
实现每次除法均检查复球非零，并检查正确的 $-K$ 或 $Q$ 分支。
实际 $u=0,1,i$ 的零阶节点与独立 scalar 源球相交，是额外相容检查；
连续证明来自第 2–4 节及真实全域证书。

## 6. 参数 crossing 帽的阶数是二阶和一阶

取非转折共同物理 knot $k$。真实角原函数、半径和相位保持径向 $C^4$，
高度为 $C^5$；故 (84.3)–(84.4) 的左右普通芽在 $r=k$ 的 $0,1,2$ 阶
径向 jet 对每个实参数准确相同。此处用完整原函数的可微性，
没有把有限位置 Fourier 原函数当成完整图。
固定物理角，未乘 $r_\tau$ 的场差可写为

$$
\Delta V(r,\theta,p)=(r-k)^3B(r,\theta,p).
\tag{84.21}
$$

$r=t(p)\sin\tau$ 后固定 $\tau$ 求一次参数导数至多降低一阶零点，
求两次至多降低两阶。乘 $r_\tau$ 及其参数导数不再降低阶数。因此在真实 crossing
$u_*(p)$，$\Delta f_p$ 至少二阶消失，$\Delta f_{pp}$ 至少一阶消失。
它们不能沿用零阶的 cubic 帽费。

若左右 $\partial_p^jf$ 于同一 $|u|<R$、全物理角带的模数为 $M_L,M_R$，
置 $m=3-j$、$\rho_*=R-|u_*|$。帽长 $\ell<\rho_*$ 时，
在以 $u_*$ 为中心的盘使用 $m$ 重 Schwarz 引理得

$$
|\Delta\partial_p^jf(u,\theta)|
\le(M_L+M_R)\left(\frac{|u-u_*|}{\rho_*}\right)^m.
\tag{84.22}
$$

先在固定 $\theta$ 证明这个商界，再仅于实时间代入已付参考像 $\theta=Y(u,x)$。
若全实时间 $|q|=|Y_x|\ge q_*>0$，参数密度帽的 uniform 和积分费是

$$
\frac{|h|(M_L+M_R)\ell^m}{q_*\rho_*^m},\qquad
\frac{|h|(M_L+M_R)\ell^{m+1}}{(m+1)q_*\rho_*^m}.
\tag{84.23}
$$

不要求复时间 $Y$ 像落真实 field 域。多芽沿相邻 crossing 望远镜求和。
根芽不在普通 knot 帽引理的作用域内。

## 7. 一个真实实参数盒上的一致源

令 $I=[p_0-\epsilon,p_0+\epsilon]$ 包含在已付简单根分支范围内。
由真实全盒导数先得

$$
t(I)\subset t(p_0)+[-\epsilon\sup_I|t'|,\epsilon\sup_I|t'|].
\tag{84.24}
$$

在该根盒和同一参数盒上，用完整均值参数 jet 及 (84.9) 重算 $t',t''$，
再与已有分支见证相交。丢掉相关性只扩大球，不缩小真值集合。
第 3 节不除以 $D$ 的 majorant 在整个盒上给 $\sup|\partial_pD|$，
故中心实际复域 $|D(p_0)|\ge d_0$ 扩展为

$$
|D(p)|\ge d_0-\epsilon\sup_I|\partial_pD|>0.
\tag{84.25}
$$

普通芽有

$$
\operatorname{Re}(-K(p))
\ge\mu_0-\epsilon\sup_I|\partial_pK|>0,
\tag{84.26}
$$

转折芽同理用 $Q$。这里导数均包括真实 $t(p)$ 的固定 $\tau$ 复合，
均值定理只沿实参数线段，不假定复参数条带。
在扩展域上，真实 interval 参数 jet 和 (84.12)–(84.20) 包住所有 $p\in I$。
转折的三个准确零常数也对每个实参数分别成立。

覆盖实际分段前腿时还必须以 (84.24) 的根盒重查径向端点和共同 spans，
不能复制中心 crossing 列表。每个可能芽都须有同盒域，每个帽用第 6 节正确阶数。
419 的单芽端点余量远大于本次根位移，不自动授予其他段。

## 8. 连续有限重建、真实密度和 R82 接口

对 $j=1,2$，用实际全域模数和球节点作时间圆 DFT、物理角 Fourier 重建。
R67 的全部 alias、未留时间项、未留角模、节点球及 dyadic 选择误差分别支付，得到
有限 $P_j$ 和全实时间、目标物理角带上的

$$
|\partial_p^jf-P_j|\le e_j.
\tag{84.27}
$$

有限删尾另付完整有限 Wiener 和，不把小系数当零。
同一个参数无关参考 $Y,q=Y_x$ 下，

$$
g_0=(hf-Y_u)/q,\qquad g_1=hf_p/q,\qquad g_2=hf_{pp}/q.
\tag{84.28}
$$

没有额外因子 $4$；输出归一化返回 $4Y$ 时才引入它。
有限代理 $\widetilde g_j=hP_j(Y)/q$ 可在更宽的有限参考复时间/标签盘上支付
重建尾，因为 $P_j$ 是整函数。真实 (84.27) 只在全实时间已付像和 $q$ 上使用。
若有限密度重建及删尾 uniform 误差为 $\eta_j$，则真实积分误差

$$
E_j\le2\left(|h|e_j/q_*+\eta_j\right)+\sum_{\rm caps}E_{j,\rm cap}.
\tag{84.29}
$$

写 $\widehat g_j=\sum_i u^ic_{j,i}(x)$，则

$$
B_j=2\sum_i\frac{\|c_{j,i}\|_{A_S}}{i+1}+E_j,\qquad
G_j=\sum_{\text{$i$ even}}\frac{2c_{j,i}}{i+1}
\tag{84.30}
$$

分别是完整积分模数及保留所有频率的有符号首积分。
中心 $B_j$ 只在 $p_0$ 有效；全盒源所得 $B_{2,I}$ 才能供 uniform $T$。
真实均值定理也允许用中心 $g_1$ 的有限代理覆盖 $I$，
其积分误差增加至多 $\epsilon B_{2,I}$；不把中心 $g_2$ 当全盒源。

R82 的局部有序二次项为

$$
\begin{aligned}
J_0&=\int\widehat g_{0,x}G_0(u)\,du,\\
J_1&=\int(\widehat g_{1,x}G_0(u)+\widehat g_{0,x}G_1(u))\,du,\\
J_2&=\int(\widehat g_{2,x}G_0(u)+2\widehat g_{1,x}G_1(u)
                         +\widehat g_{0,x}G_2(u))\,du.
\end{aligned}
\tag{84.31}
$$

首个 419 报告用同一已完成 $g_0$ 的完整矩形支付这些范数。
后续若零阶叶只保存每个 time-row 的 $A_S$ 范数 $n_{0,i}$，
仍有

$$
\|\partial_xc_{0,i}\|_{A_\sigma}\le
\frac{n_{0,i}}{e(S-\sigma)},\qquad \sigma<S.
\tag{84.32}
$$

证明是逐模 $k e^{-k(S-\sigma)}\le1/[e(S-\sigma)]$。
结合同一完整 $G_0$ 的有限导数范数和 R82 的奇偶时间权，即可支付 (84.31)，
无需重造或改换 $g_0$。所有跨段二次项仍须准确相乘累积。

实际后续接口保留 $J_2$ 中最大的有限项
$2\int\widehat g_{1,x}\int_{-1}^u\widehat g_1$ 的全部系数。
若 $\widehat g_1=\sum_m u^m c_m$，其准确表达为

$$
2\sum_{m,n} w_{mn}\,c_m'c_n,\qquad
w_{mn}=\frac{\int_{-1}^1u^{m+n+1}\,du
                  -(-1)^{n+1}\int_{-1}^1u^m\,du}{n+1}.
\tag{84.36}
$$

每个单项积分是奇数次时零、偶数次时 $2/(j+1)$，故 $w_{mn}$ 是准确有理数。
有限 Fourier 乘法保留最高至两个输入次数之和及零频，球运算误差包含在输出系数内。
余下的 $g_0/g_2$ 两混合项用 (84.32) 和完整时间奇偶权付费；
$J_1$ 也只包含这类零阶混合。没有以完整 $J_2$ 范数重复收费。

## 9. 已完成的实际范围

主要源：

- scripts/fourfold_phase_parameter_time_circle.py：
  4552558eabe5f35bb9fe6bf4155ab869535e2aeb61c4087ef3eb1d60ffc46fc1；
- scripts/fourfold_phase_parameter_cap_budget.py；
- scripts/fourfold_phase_uniform_parameter_time_circle.py；
- scripts/fourfold_parameter_density_leaf.py：
  d4bafca758676dbbb4b55119c9786e943dae36248d09dcf82d5affd8f7442186。

普通 419 和转折 0 已付 $|u|\le3$、物理角带 $1/64$ 的中心参数源模数，
并完成 $u=0,1,i$ 的原生节点包含。以下均位于 data/phase_ring_continuation：

| 报告文件 | SHA256 |
|---|---|
| type_fixed_step02_d5_step5_parameter_time_circle419_pilot.json.gz | cdc8e747389144cc49ef54309169bc172c643f289d4519a65ccc17665353d36e |
| type_fixed_step02_d5_step5_parameter_time_circle_turn0_pilot.json.gz | 33ac451dce1d472daede485da311da931071e287668fb309973ac248c75cc1ea |
| type_fixed_step02_d5_step5_uniform_parameter_time_circle419_h1e12.json.gz | b41012a35560ebc2c896bcab9024a7c19d7798ae46bdf60044e5d4129b4737c0 |
| type_fixed_step02_d5_step5_uniform_parameter_time_circle_turn0_h1e12.json.gz | 835a3abb12b27576c4fd20a47f094762ab8c7da88e5fbd8392dfa81c453a1a43 |
| type_fixed_step02_d5_step5_parameter_caps4.json.gz | 7ed697420f1f64324a67c28da1c0fee64f3090994e21b62d7aa5ca4882e118b3 |
| type_fixed_step02_d5_step5_parameter_density419.json.gz | dd78e021c15430005cfbcd15de5909db56d34a5b684732066f32f2890a7a3d2b |
| type_fixed_step02_d5_step5_parameter_local_integrals419.json.gz | 608456edd77e9e23bf4ba94add65bd237bed03c76a042804baeea127f63adc0b |
| type_fixed_step02_d5_step5_uniform_parameter_density419_h1e12.json.gz | 31906f61f726168a541c387dfc7d5008a0fc1b0003a95238b4d9485ea40ddf12 |

419 的真实盒 $\epsilon=10^{-12}$：$D$ 扰动小于 $7.360\,10^{-13}$，
$-K$ 扰动小于 $5.980\,10^{-15}$，扩展下界仍分别大于 $.03120$、$.56772$。
源报告只给域和节点。随后独立的 uniform 密度报告已完成整个同一实盒的
有限重建及真实帽/参考费用，得到 $E_{2,I}<2.190\,10^{-9}$、
$B_{2,I}<2.172731\,10^{-6}$，并且 $E_{1,I}<4.650\,10^{-9}$。
其整个参数区间包含在输出 identity 中；该盒不能免费扩到 $10^{-9}$ 或更宽。

段 4 在 $S=1/256$ 的全部真实参数帽积分费用满足

$$
E_{1,\rm cap}<2.800\,10^{-28},\qquad E_{2,\rm cap}<2.009\,10^{-18}.
\tag{84.33}
$$

中心 419 的完整连续密度在 $S=1/256$、$\sigma=3/1024$ 上得到

$$
\begin{aligned}
E_1&<3.856\,10^{-12},& E_2&<1.679\,10^{-12},\\
B_1&<1.605145\,10^{-4},& B_2&<2.171691\,10^{-6},\\
\|J_0\|&<7.992\,10^{-21},&
\|J_1\|&<1.594\,10^{-13},&
\|J_2\|&<3.089\,10^{-7}.
\end{aligned}
\tag{84.34}
$$

完整有限首积分参数零频中心为

$$
(G_1)_0=-9.86741993405323066101913367\ldots\,10^{-6},\qquad
(G_2)_0=5.16058194162984103023368827\ldots\,10^{-8}.
\tag{84.35}
$$

实际报告保留完整球及全部正频数组（长度 799、309、248）。
真源误差 (84.29) 另加。局部零频不等于最终 twist；
$J_2$ 包含 $2\int g_{1,x}G_1$，没有因 $g_0$ 很小而省略。

由 scripts/fourfold_parameter_local_integrals.py 实际执行 (84.36) 后，
保留的完整局部二阶多项式在 $A_{3/1024}$ 的范数小于
$6.374890\,10^{-8}$，剩余 $g_0/g_2$ 混合费小于
$7.375\,10^{-15}$。CPU 约 $0.47$ 秒；没有重新求解场。
这份新报告还使用同一 $g_0$ 的 row-norm/Cauchy 接口，
并核对三个完整首积分与原 419 报告逐项相容。
原来全部省略 $J_2$ 的报告和其较大费用原样保留。

### 重放

从本课题目录使用 PYTHONDONTWRITEBYTECODE=1、OPENBLAS_NUM_THREADS=1、
OMP_NUM_THREADS=1。主要入口：

    python scripts/fourfold_phase_parameter_time_circle.py \
      --domain data/phase_ring_continuation/step5_sharp_time_domain_R6_order40/forward_0419_r.json.gz \
      --out data/phase_ring_continuation/type_fixed_step02_d5_step5_parameter_time_circle419_pilot.json.gz
    python scripts/fourfold_phase_parameter_time_circle.py \
      --domain data/phase_ring_continuation/step5_sharp_time_domain_full/forward_0000_r.json.gz \
      --out data/phase_ring_continuation/type_fixed_step02_d5_step5_parameter_time_circle_turn0_pilot.json.gz
    python scripts/fourfold_phase_uniform_parameter_time_circle.py \
      --domain data/phase_ring_continuation/step5_sharp_time_domain_R6_order40/forward_0419_r.json.gz \
      --out data/phase_ring_continuation/type_fixed_step02_d5_step5_uniform_parameter_time_circle419_h1e12.json.gz
    python scripts/fourfold_parameter_density_leaf.py \
      --directory data/phase_ring_continuation/step5_parameter_density419 \
      --out data/phase_ring_continuation/type_fixed_step02_d5_step5_parameter_density419.json.gz

准确依赖和已完成输出列入本批 manifest；大的可重建矩形只需保源、参数和哈希。
完整 550 段参数密度、全盒二阶模数、跨段累积和最终参数端点/KAM 门仍须继续支付。
