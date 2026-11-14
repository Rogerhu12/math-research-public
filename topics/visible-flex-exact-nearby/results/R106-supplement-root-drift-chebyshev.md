# R106 补充：由实径向界收紧整个复根领口的漂移

2026-11-13，constructive-route。

**已证明，20 个准确 BigInt 门已实际通过：** 对同一
$\delta_5\pm10^{-9}$、物理角带 $|\operatorname{Im}\theta|\le1/320$，
真实 root-germ 漂移 $q$ 在下述整个 Bernstein 椭圆满足

$$
|q|<
\frac{15094192482356543796294422702397}
     {545259520000000000000000000000}
<27.682585<28.
\tag{106CE.1}
$$

该椭圆覆盖完整实际根到 fixed cut 的实领口，并包含其中每一点的
复径向半径 $7\times10^{-6}$ 圆盘。这是实际完整系数的复域界，
不是一张角节点图。它不计算 $b-\beta$，不支付 R104 的有效 cutoff。

## 1. 当前根只随实参数移动

本篇使用 R37 修改算子的真实**径向 target**
$K_0(r,p)$ 及其正根 $t(p)$；$t$ 完全不依赖 $\theta$。
$p$ 在本文始终为实数。故

$$
\rho=t(p)-r,\qquad \rho\in\mathbb R
\quad\Longrightarrow\quad r\in\mathbb R
\tag{106CE.2}
$$

即使 $\theta$ 已复化也成立。这里没有使用早期实际二型行列式的
非径向根图 $t(\theta)$；若改用后者，本篇实轴输入不能直接转授。

准确根包、共同 scalar span 和实参数包含来自已支付的原件：

- notes/2026-11-12-beta-step3-true-derivative-collar-h1e5-domain500.json；
- data/phase_ring_continuation/type_fixed_step02_d5_step5_real_parameter_return_existence.json；
- notes/2026-11-13-R106-coarse-root-finite-part.json。

全部文件及 SHA256 由配套脚本逐字核验。requested 参数盒严格落在前两个
原件的共同实参数域。令

$$
h=\frac3{10000},\qquad R=\frac1{2000}.
$$

实际 $t(p)\pm R$ 全部落在同一准确 root scalar span 内；
$t(p)\pm h$ 也落在 R75 已付的真实 $|r|<\operatorname{binary64}(.24)$ 内。
因此对每个固定的复角 $\theta$，R75 的真实闭实径向界给出

$$
|q(\rho,\theta)|<9
\quad(-h\le\rho\le h,\ |\operatorname{Im}\theta|\le1/320).
\tag{106CE.3}
$$

正根向内的 mixed 系数与原物理 $r$ 系数差一个负号，
两个模长估计不受影响。

## 2. 同一真实复径向外盘

原 H collar 的整个 $|\rho|\le R$、同一物理角带上，
真实双线性面积平方与 $a_0$ 分别有实部下界 $9/5$、$1/5$。
R106 前一完整几何预算给在半径 $R_0=1/400$ 上

$$
|F_i|<25,\qquad |F_{\theta,i}|<81/10.
$$

这里 $F$ 是无限 R33 原函数，含全部角尾。Cauchy 在 $R$ 上给
$|F_{r,i}|\le25/(R_0-R)$、
$|F_{r\theta,i}|\le(81/10)/(R_0-R)$。
六项 triple-product 估计得到

$$
|q|=\left|\frac{(F_\theta\times F_r)\cdot F_{r\theta}}{G a_0}\right|
\le
\frac{6\cdot25\cdot(81/10)^2}
     {(R_0-R)^2(9/5)(1/5)}
=6834375000<7\times10^9=:M .
\tag{106CE.4}
$$

$q$ 在这个整个盘内全纯；两个真实复分母的非零性早已支付。
原 H collar 的根因子门也给 $|k_*|<50$，但下述收紧只使用 $q$。

## 3. 一个有限 Chebyshev–Joukowski 估计

令外椭圆参数 $\chi=3$，椭圆写为

$$
\rho=\frac h2(w+w^{-1}),\qquad |w|=\chi .
$$

它的半长轴准确是
$h(\chi+\chi^{-1})/2=R$，所以整个外椭圆包含于第 2 节的实际复盘。
对每个固定复角和实参数，写完整 Chebyshev 展开

$$
q(\rho,\theta)=\sum_{n\ge0}a_n(\theta)T_n(\rho/h).
$$

Joukowski 拉回在环域 $\chi^{-1}<|w|<\chi$ 全纯，且在外圆模长不超过 $M$。
Laurent 系数 Cauchy 估计因此给
$|a_n|\le2M\chi^{-n}$（$n\ge1$）。

取 $P_N=\sum_{n=0}^N a_nT_n$。实段上 $|T_n|\le1$，故

$$
\|q-P_N\|_{[-h,h]}\le
e_{\rm real}:=\frac{2M}{\chi^N(\chi-1)}.
\tag{106CE.5}
$$

结合 (106CE.3)，$|P_N|\le9+e_{\rm real}$。
对任意次数不超过 $N$ 的复系数多项式 $P$，
函数 $w^{-N}P(h(w+w^{-1})/2)$ 在 $|w|\ge1$ 全纯且在无穷远有有限值；
其单位圆边界模长不超过 $\sup_{[-h,h]}|P|$。
外域最大模原理给

$$
|P_N(\rho)|\le(9+e_{\rm real})\lambda^N
\quad\text{在内椭圆 }|w|\le\lambda,\quad1<\lambda<\chi .
$$

内椭圆的剩余级数由 $|T_n|\le\lambda^n$ 得

$$
\boxed{
|q|\le
(9+e_{\rm real})\lambda^N
+\frac{2M(\lambda/\chi)^{N+1}}{1-\lambda/\chi}.}
\tag{106CE.6}
$$

这个证明允许复角下的复杂系数，不要求 $q(\rho,\theta)$ 对实 $\rho$ 为实数。
$9$ 的实轴界已经对整个复角带成立，故没有在此遗漏角复化费用。

代入 $N=22$、$\lambda=21/20$，得到 (106CE.1)。
全部幂、几何级数和比较均为准确有理数；这里没有以浮点近似决定通过。

## 4. 完整实际领口的复厚度

内椭圆的准确半轴为

$$
a=\frac{841}{2800000},\qquad b=\frac{41}{2800000}.
$$

同一真 root 包和 fixed cut 给
$0<\rho_c(p)<1/4000$。若
$\rho_0\in[0,\rho_c(p)]$、$|z-\rho_0|\le7/10^6$，则

$$
\frac{(\operatorname{Re}z)^2}{a^2}
+\frac{(\operatorname{Im}z)^2}{b^2}
\le
\frac{(1/4000+7/10^6)^2}{a^2}
+\frac{(7/10^6)^2}{b^2}
=\frac{28554287048}{29723484025}<1.
$$

故每一个这样的复圆盘都包含在内椭圆中，(106CE.1) 同时控制它们。
这给 regular-source 分段径向 Cauchy 预算一个真实、均匀的几何输入，
无需把根处低 jet 外推到未支付的径向范围。

配套准确核：
scripts/fourfold_subprincipal_root_drift_chebyshev_exact.mjs；
真实执行报告：
notes/2026-11-13-R106-root-drift-chebyshev.json。

重放：

    node scripts/fourfold_subprincipal_root_drift_chebyshev_exact.mjs . \
      notes/2026-11-13-R106-root-drift-chebyshev.json

该界不提供有符号的 $q$ Fourier 系数，亦不代付完整根相位或强余项。
它用于下一实际有限 Fourier 正则源的域、alias 和截断预算；
主课题仍须完成真正闭曲面族。
