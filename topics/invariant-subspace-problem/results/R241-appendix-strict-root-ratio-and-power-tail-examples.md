# R241附录：严格根比与非调和幂尾的全多项式循环

日期：2026-11-12（UTC）。作者：kernel。状态：已证明。作为 [R241](R241-carry-head-powers-and-drifting-first-polynomial-cyclicity.md) 的量化附录。

## 1. 实际只需严格小于 1 的根比

沿用主稿
$$
s_m=a_*+\sum_{j<m}a_j,\quad
B_m=\sum_{j<m}|a_j|,\quad g_m=\|a_{\ge m}\|_2,
$$
$$
A_m=\max(1,6B_m),\quad
D_m=2C\sqrt m\,g_m,\quad
\delta_m=A_m e^{-\gamma(2m)^3},\quad
\gamma=770/16^4,
$$
以及
$$
\varepsilon_m=2\sqrt{A_mD_m}+3D_m+\delta_m.
\tag{1.1}
$$
主稿已在完整自然域上证明
$$
\|(X^*-\overline{s_m}I)^{4m}Q_m\|\le\varepsilon_m^{4m}.
\tag{1.2}
$$

**严格根比判据。** 如果
$$
|s_m|\to\infty,\qquad
\limsup_{m\to\infty}\frac{\varepsilon_m}{|s_m|}<1,
\tag{1.3}
$$
则不存在非零闭 $M\subseteq\operatorname{Dom}X$ 满足 $XM\subseteq M$。因而主稿的全部最高单位交换系数自然多项式，以及所有 $q(u)e^w$ 的单射／循环结论仍成立。

证明：若 $Y=X|_M$ 有界，主稿在同一个 $M$ 上的投影恒等式给
$$
\|P_MQ_m\|
\le\left(\frac{\varepsilon_m}{|s_m|-\|Y\|}\right)^{4m}
$$
对充分大 $m$ 成立。由 (1.3)，存在固定 $\rho<1$，使括号最终不超过 $\rho$。右端趋零，而 $Q_m\to I$ 强，故 $M=0$。后续 Bell 与指数权接口与主稿完全相同。

所以主稿较方便的条件
$(1+B_m)\sqrt m\,g_m/|s_m|^2\to0$
只是足够条件，不是本方法的准确边界。

## 2. 尾自然幂常数可统一取 17

R207 附录给
$$
C=16+C_K,\qquad
C_K=\frac{18e^2\|\eta\|_2}{1-e\eta_*}.
$$
实际模型满足 $\eta_j\le e^{-770\,16^j}$。因为 $16^j\ge j+1$，
$$
\|\eta\|_2^2
\le\sum_{j\ge0}e^{-1540(j+1)}
=\frac{e^{-1540}}{1-e^{-1540}},
$$
故 $\|\eta\|_2\le2e^{-770}$。又 $1-e\eta_*\ge1-e^{-769}>1/2$，所以
$$
C_K\le72e^{-768}<1.
$$
因此全部主稿尾幂估计可以取固定的
$$
\boxed{C=17.}
\tag{2.1}
$$
后续使用 17 是把已有常数增大后的合法统一选择。

## 3. 不等振幅交替幂尾

取
$$
\frac12<\sigma<1,\qquad
\kappa>0,\quad\kappa\ne1,\qquad
a_{2k}=(2k+1)^{-\sigma},\quad
a_{2k+1}=-\kappa(2k+2)^{-\sigma}.
\tag{3.1}
$$
允许任意固定常项 $a_*$。偶、奇整数的初等积分比较给
$$
s_m=\frac{1-\kappa}{2(1-\sigma)}m^{1-\sigma}
+o(m^{1-\sigma}),
\tag{3.2}
$$
$$
B_m=\frac{1+\kappa}{2(1-\sigma)}m^{1-\sigma}
+o(m^{1-\sigma}),
\tag{3.3}
$$
$$
g_m^2=\frac{1+\kappa^2}{2(2\sigma-1)}m^{1-2\sigma}
+o(m^{1-2\sigma}).
\tag{3.4}
$$
这些公式同样适用于奇数截断，因为单个端项相对相应主项趋零。

于是
$$
\frac{A_m}{|s_m|}\longrightarrow
h:=\frac{6(1+\kappa)}{|1-\kappa|},
$$
$$
\frac{D_m}{|s_m|}\longrightarrow
r:=\frac{4C(1-\sigma)}{|1-\kappa|}
\sqrt{\frac{1+\kappa^2}{2(2\sigma-1)}},
\tag{3.5}
$$
且 $\delta_m/|s_m|\to0$。所以 (1.3) 的明确充分条件是
$$
\boxed{2\sqrt{hr}+3r<1.}
\tag{3.6}
$$
在 (3.6) 下，(3.1) 的 first 不存在非零闭有界不变分支，任意非零 $q(u)e^w$ 都循环。

对每个固定 $\kappa>0$、$\kappa\ne1$，当 $\sigma\uparrow1$ 时 $h$ 固定、$r\to0$，故存在一个真实的开区间 $\sigma<1$ 满足 (3.6)。这严格增加了纯调和 $\sigma=1$ 的实例。

## 4. 一个无需隐含常数的具体区间

取
$$
\kappa=\frac12,\qquad
0.9999\le\sigma<1,\qquad C=17.
\tag{4.1}
$$
则 $h=18$。写 $\epsilon=1-\sigma\le10^{-4}$，由 (3.5)，
$$
r=136\epsilon\sqrt{\frac{0.625}{1-2\epsilon}}.
$$
因为 $0.625/(1-2\epsilon)<0.626<0.792^2$，
$$
r<136\cdot10^{-4}\cdot0.792<0.011.
$$
所以
$$
2\sqrt{hr}+3r
<2\sqrt{18\cdot0.011}+0.033
=2\sqrt{0.198}+0.033
<0.925<1.
\tag{4.2}
$$
因此整段 (4.1) 都满足严格根比判据。

(3.1) 在 $\sigma\le1$ 时正、负两相位各自不可和；没有可和相位缺陷方向。R138 给真实 first 的谱为整个复平面且全是连续谱。此处排除 Bell 碰撞使用的是新的高次投影估计，而不是空谱结论。

## 5. 复周期版本与边界

同一个计算适用于
$$
a_j=\omega_{j\bmod d}(j+1)^{-\sigma}.
$$
若
$$
\mu=\frac1d\sum_r\omega_r\ne0,\quad
\nu=\frac1d\sum_r|\omega_r|,\quad
\tau^2=\frac1d\sum_r|\omega_r|^2,
$$
则 (3.5) 替换为
$$
h=\frac{6\nu}{|\mu|},\qquad
r=\frac{2C(1-\sigma)\tau}{|\mu|\sqrt{2\sigma-1}}.
$$
同样，$2\sqrt{hr}+3r<1$ 即给全部 $q(u)e^w$ 循环。如果各非零周期系数不全在同一正射线上，这些例子也属于 R138 的全平面谱分支。

本附录不覆盖 $\kappa=1$，不声称 (3.6) 必要，也未证明这些 first 在任意未知闭不变限制中像稠密。

