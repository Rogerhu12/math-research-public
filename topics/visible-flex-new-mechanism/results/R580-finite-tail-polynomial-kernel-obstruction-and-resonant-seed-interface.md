# R580：当前末段有限基缺少真实全平线性核及准确换基入口

2026-11-26，Astra-new-mechanism-0105020f-20261126。

本稿针对实际圆核背景与已运行的有限维表示，给出新的精确线性结论，并据此规定下一输入。它不把有限空间的限制解释成强非圆曲面不存在，也不改判或撤回正在执行的 theta-peak 探索。原圆核收据见[完整原收据](../notes/2026-11-26-circular-entry-and-small-core-continuation-receipt.md)；其 stage 0 是 run `45778418134` / job `139767648038` 的实际 17 维径向末态，stage JSON SHA256 `a78102463e4a816d00e000c969372af423a41ee93ab4996574b16048265b9324`。

## 1. 所用真实圆背景与精确末段表达

在圆核 p=q=.18、rounding=.2，且全部 64 个角系数为零时，实际连续位置式为

\[
X_0(s,\theta)=a(s)e_r(\theta)+z(s)e_z.
\tag{1}
\]

这里 a,z 是该实际 q 的径向函数，不能用零径向系数的参考背景代替。设

\[
L=.9,\quad s_\ell=.036,\quad \ell=.2,\quad r_c=.22,
\quad \delta=(L-s)/\ell,\quad \kappa=(L-s_\ell)/\ell=4.32.
\]

背景过渡在 s_b=L−.08=.82 结束，故在 `.82<s<.9` 准确有

\[
r_0=r_c+\ell\delta,\qquad
w(\delta)=.1\exp\!\left[-\frac{2-\sin(\delta^{-2})}{\delta}\right],
\]

\[
a=r_0\exp(\beta P_a),\qquad
z=h+H+\beta P_z,\qquad H_s=w(\delta).
\tag{2}
\]

P_a、P_z 是末段 B 样条多项式。原 free envelope 是

\[
x=\frac{s-s_\ell}{L-s_\ell}=1-\delta/\kappa,\quad
\lambda=-1/x+1/(1-x),\quad \chi=\frac1{1+e^{-\lambda}},
\quad\beta=4\chi(1-\chi).
\tag{3}
\]

8 个五次样条的最后结点区间为 `x∈(2/3,1)`，即 `s∈(.612,.9)`。在该区间每个 B_j 及其任意固定系数组合都是五次以下多项式。特别 (2) 覆盖的整个准确振荡尾都落在这一个多项式区间中。

由 (3)，在 delta→0+ 时

\[
\beta=4e\,e^{-\kappa/\delta}(1+O(\delta)),\qquad
\frac{\beta_s}{\beta}=-\frac{\kappa}{\ell\delta^2}+O(1).
\tag{4}
\]

对任意固定有限 P_a,P_z，(2)–(4) 给

\[
a_s=-1+O(\beta\delta^{-2}),\qquad
z_s=w+O(\beta\delta^{-2}).
\tag{5}
\]

关键是实际 z_s **不是**整尾都准确等于 w；已有径向 z 系数也会贡献。可是

\[
w\ge .1e^{-3/\delta},\qquad
\frac{|z_s-w|}{w}
 \le C\delta^{-2}e^{-(\kappa-3)/\delta}\longrightarrow0.
\tag{6}
\]

因此存在一个严格正的 delta_*，在 `0<delta<delta_*` 整个开尾区都有 z_s>0，且 a_s→−1。所有固定幂次 delta^{-N}z_s 都趋零。这里不宣称整条 `.036<s<.9` 连接的 z_s 无零；所需的端部正性由真实扰动后的函数 (6) 支付。

## 2. 完整非零角模线性度量行

对任意 j≥2，写一个角频 j 的向量变化为

\[
V=A(s)\cos(j\theta)e_r
   -\frac{A(s)}j\sin(j\theta)e_\theta
   +C(s)\cos(j\theta)e_z.
\tag{7}
\]

这一形式已经使第一变分的 G 非零角系数为零。直接微分给

\[
\delta E=2(a_sA_s+z_sC_s)\cos(j\theta),
\]

\[
\delta F_{\rm coordinate}
 =-\frac{aA_s+(j^2-1)a_sA+j^2z_sC}{j}\sin(j\theta),
\qquad\delta G=0.
\tag{8}
\]

所以要求度量在一阶仍 theta 不变，准确等价于

\[
\boxed{a_sA_s+z_sC_s=0,\qquad
aA_s+(j^2-1)a_sA+j^2z_sC=0.}
\tag{9}
\]

这只针对非零角系数，允许 E、F、G 的均值随设计改变，因而没有把固定 g 这一更强条件偷加到当前逆设计问题。径向均值变化属于 j=0，不能与 (8) 中的 j≥2 项抵消。

当前 frame 变量在圆点的切向变化为

\[
\delta T=-u_j(s)\sin(j\theta)e_r+v_j(s)\sin(j\theta)e_z.
\]

用原准确周期 primitive，(7) 的参数正好是

\[
A=\frac{ja}{j^2-1}u_j,\qquad C=-\frac aj v_j.
\tag{10}
\]

原模式 j=2,4,6,8 分别满足同样结论，且线性角 Fourier 正交使它们互不抵消。j=2 时即 A=(2a/3)u_2、C=−(a/2)v_2。

## 3. 末段同 envelope 有限多项式不能含非零真实核

**命题。** 在上述真实圆背景上，假设当前有限角基在帽端写成

\[
u_j=\beta P(\delta),\qquad v_j=\beta Q(\delta),
\tag{11}
\]

其中 P,Q 是有限次数多项式，且 (9) 在足够靠近帽的整个开区间准确成立。则 P=Q=0，因而该角模在末段恒为零。

**证明。** 若 P 非零，写 P(delta)=p_k delta^k+O(delta^{k+1})，其中 p_k≠0，k 为最小非零次数。由 a→r_c>0、(4)、(10)，

\[
A_s=-\frac{j r_c\kappa p_k}{(j^2-1)\ell}
       \beta\delta^{k-2}(1+o(1)).
\tag{12}
\]

若 Q 非零且最小次数为 m，则同理 C_s=O(beta delta^{m−2})；Q=0 时 C_s=0。由 z_s 比任一 delta 正幂衰减更快，且 a_s→−1，

\[
\frac{z_sC_s}{a_sA_s}\longrightarrow0.
\tag{13}
\]

于是 (9) 第一式不可能恒为零，矛盾。因此 P 是零多项式，A=0。再代 (9) 第二式，得 j² z_s C=0。由 (6) 在整个充分短开尾区 z_s>0，故 C=0，Q 在该开区间为零，遂也是零多项式。证毕。

这个结论直接适用于实际 stage0 的任意有限径向 a,z 系数，也适用于在同一表示中先重新调这些圆背景系数。改变圆背景会改变某个有限区间上的线性传递，但不会消除端部 (12)–(13) 的相对衰减矛盾。

[R569](R569-fixed-oscillatory-tail-and-flat-infinitesimal-bending.md) 已证明真实振荡尾有非零全平模式。这与本命题没有矛盾：它给出的 f 及各阶导数衰减为 `exp(−c/delta³)`；除以 beta 仍全平，但一个非零全平函数不是固定末端多项式。允许任意全平函数的空间或逐次加密的闭包，与当前固定 8 个径向样条不是同一实际线性空间。

## 4. 当前 8 基 p-forcing 的更具体局部缺口

本节仍只断言当前有限表示在圆点的 C1 一阶入口，不断言远处强非圆点不存在。

固定 q=.18、rounding=.2，R=q+rounding=.38，令 p=q+epsilon。核心支持函数对真实法向角 psi 的一阶展开为

\[
h(\psi)=R+\epsilon/2+(\epsilon/2)\cos2\psi+O(\epsilon^2).
\]

弧长密度为 h+h''，而平均密度为 R+epsilon/2，因此归一弧长角满足

\[
\theta=\psi-\frac{3\epsilon}{4R}\sin2\psi+O(\epsilon^2).
\]

故原核心相位 u_c=psi−theta 的单位 p 一阶 forcing 为 `3 sin(2theta)/(4R)`，即核心 A=1/2、C=0。把它代入当前背景 carrier 后，完整 j=2 相位变化是

\[
u_2=\frac{3}{4R}\,\mathrm{bg\_wm}(s)+\beta P(\delta),
\qquad v_2=\beta Q(\delta).
\tag{14}
\]

`bg_wm` 在 s≥s_b=.82 准确为零，在 s<s_b 的背景过渡内部严格为正。第3节首先迫使 P,Q 为零多项式；由于当前最后结点区间 `.612<s<.9` 是同一个多项式片，它们在该整个片上都为零。因此 s_b 左侧足够近处必有

\[
A=\frac{a}{2R}\,\mathrm{bg\_wm}>0,\qquad C=0.
\tag{15}
\]

下面直接核 a_s 在 s_b 附近非零，不借用未付清的全连接 z_s 正性。原全局 log-radius 系数界为 |c_i|≤3/2。由 B 样条非负分割统一性，|P_a|≤3/2。五次导数控制系数为 `5(c_i−c_{i−1})/(t_{i+5}−t_i)`；最小非零分母为 1/3，故在 x 坐标 |(P_a)_x|≤45，在 s 坐标

\[
|(P_a)_s|\le 45/(.864)=625/12.
\]

在 s_b，x=49/54，lambda=54/5−54/49>9。因此由 e>2，

\[
0<\beta<4e^{-9}<1/128,
\qquad |\beta_s|/\beta\le\lambda_s<138.
\]

于是 alpha=beta P_a 满足

\[
|\alpha_s|<\frac{207+625/12}{128}<\frac{21}{10}.
\]

背景 carrier 在 s_b 全平结束，r_0(s_b)=.3，故

\[
a_s(s_b)=e^{\alpha(s_b)}\{-1+.3\alpha_s(s_b)\}<0.
\tag{16}
\]

连续性使 a_s 在 s_b 左侧某个开区间仍严格负。若 (9) 成立，C=0 与第一式给 A_s=0，第二式随后给 3a_s A=0，即 A=0，与 (15) 矛盾。

**因此：**对当前 8 基、固定两种 envelope/端点位置、原 log-radius 参数盒，任何通过圆点且 `p'(0)≠0` 的 C1 参数路径，都不能使全部非零角度量行的一阶变化为零。任意径向均值参数的一阶变化都无法修复它，因为它们只在 j=0。其他角模也不能抵消 j=2。

本结论不排除远离圆点的某个孤立强非圆解、不排除更大函数空间的分支、不排除不同幅度参数化的非线性分岔，也不把有限数值 eta 当成严格误差下界。当前 theta-peak 强非圆范围仍自然运行并按原身份结算。

## 5. 实际换基和共振预测的完整接口

下一输入必须首先加入真实尾口线性场，不能只反复减 p−q 或只调圆背景后再使用相同末段多项式空间。具体应从已取得的 stage0 实际 a,z 出发，执行下列连续问题。

**实际尾种子。** 用 (2) 的真实曲线，不能直接挪用零径向参数 R569 或另一 R571 profile 的端值。在充分短尾部 a_s<0、z_s>0，可用真实半径 r=a(s)，定义 `w_eff=−z_s/a_s>0`。准确 j=2 方程是

\[
(w_{\rm eff}f_r)' -4\frac{(w_{\rm eff})_r}{r}f=0,
\quad A=\frac{w_{\rm eff}(4f-rf_r)}3,\quad C=f.
\tag{17}
\]

它须有真实非零全平端解及带误差控制的有限口数据。由 (5)–(6)，w_eff 与原 w 近端的相对扰动指数小，但“同一类渐近式”不是已经支付的原 DtN 数值；需把此实际权代入 R569 的 cell/递推控制，或另严证扰动稳定并明确常数。不得在有限内圈同时设置 f=f_r=0 后声称得到非零种子。

**核心共振。** 在 z_s≠0 的中段，(9) 是真实二维系统

\[
\frac d{ds}\binom A C
=\begin{pmatrix}
-3a_s/a&-4z_s/a\\
3a_s^2/(az_s)&4a_s/a
\end{pmatrix}\binom A C.
\tag{18}
\]

不把真实 z_s 的零点隐藏在除法中。若连接内有 z_s=0，必须回到未除法的 (9) 并支付该奇点的匹配。当前圆核细网几何可行没有证明 z_s 全程正。

在开核心圆柱 a_s=0、z_s=1，所需核心值是 A_core=1/2、C_core=0。因而对一个真实尾种子延伸到核心后，要先解 `C_core=0`，且必须有 `A_core≠0`，才可按 `1/(2A_core)` 缩放。由另一背景已知的 R571 负相位 holonomy 不能自动代付这份实际 a,z 的射击值。

**调背景但不冻角尾。** 可在核心和已定义实际尾种子口之间选明确的径向 profile 控制 mu，其支持避开开核心和那个尾口。这样尾种子的实际初值对 mu 固定，射击导数可用

\[
(\partial_\mu Y)'=M\partial_\mu Y+(\partial_\mu M)Y
\]

准确求得，外层以真实 `C_core(mu)=0` 及几何硬门调谐。只限制这些平均 profile 控制的支持，不冻结非径向自由在整个尾部的活动。若当前可行控制没有付出横截性或根，就换明确的背景/相位范围继续；不从一次有限扫描宣不存在。

**加入实际角列并预测。** 共振后将完整真实解转换为 `u_2=3A/(2a)`、`v_2=−2C/a`，作为一个独立已识别角基列。它在末端的非多项式行为及准确全平端必须保留；其余自由可继续覆盖每个内部尾点。核心单位 forcing 已由这列支付，然后以 `X_0+epsilon V` 和核心平均半径的对应变化作非圆预测，再解全部非线性 metric 行。二阶剩余为真实 `<dV,dV>` 及同步核心/均值二阶项，仍需连续估计与实际修正，不能把线性 seed 当有限等距族。

圆点的 17 个径向参数对所有非零角 metric 行的 Jacobian 列严格为零，因为任意圆 a,z 都有 theta 不变度量。这解释了为何“同时放开径向变量再做一次小 epsilon Newton”不会自动选择共振背景。正确实施顺序是先解决依赖背景的完整线性端问题，再用其真实向量预测有限非圆。所有后继科学均需独立 source/request 身份及完整原收据。
