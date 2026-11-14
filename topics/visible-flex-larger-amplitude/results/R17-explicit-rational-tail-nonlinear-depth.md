# R17：固定有理深尾的显式非线性常数与 $N=4096$

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

**结论。** 在 [R15](R15-rational-deep-tail-and-46-parameter-trace.md) 的固定有理深源和角差 $h=(\log2)/4$ 下，可以取

$$
\boxed{c_*=2^{-256},\qquad C_*=2^{320}.}
\tag{0.1}
$$

局部全频胞元引理在 $n\ge512$、$64\epsilon\delta_n^{7/4}\le1$ 上成立。对当前冻结参数，归一后的 $\epsilon$ 严格位于 $2^{14}$ 与 $2^{15}$ 之间；R15 的全部线性、局部存在、非线性收缩和低46高度坐标门可统一取

$$
\boxed{N=4096.}
\tag{0.2}
$$

这是一个**具体定义的全频精确深尾**，包括完整 mean、真实胞元转接和 $C^2$ 平端点。它没有支付从可浮点计算的浅 cut 到该图的非线性匹配，没有认证任何当前大幅闭曲面，也没有把远截断的浮点一致当成连接证明。

## 1. 固定参数、实际 $\epsilon$ 与 warp 的适用边界

沿用 R15 的

$$
\delta_n=d_0 2^{-n},\quad
\eta_n=c_\eta\delta_n^{3/2},\quad
R=64,\quad a=11/4,\quad\alpha=65/64,
$$

$$
3/500\le d_0<1/128,\quad
3/5\le c_\eta\le2/3,\quad c_0=c_\eta\sqrt{d_0}\le1/16.
$$

其中 adapter 的 $d_0,c_0$ 是 R15 §1 已列明的精确 dyadic 存数。九段 profile 用实指数、实对数和 quintic $10t^3-15t^4+6t^5$ 定义。

保存的物理参数为

$$
\epsilon_{\rm phys}
=\frac{3821273729050667}{295147905179352825856},
\qquad
r_c=\frac{900719925474099}{18014398509481984}.
$$

把 $r=r_c\rho$、$z=r_c\widetilde z$ 后，slope $w=z_r$ 不变，但绝对 profile 系数变为

$$
\epsilon=\epsilon_{\rm phys}/r_c^7.
\tag{1.1}
$$

精确分数比较给

$$
2^{14}<\epsilon<2^{15},\qquad
\epsilon\approx16572.1331147941.
\tag{1.2}
$$

这里没有把 $w_{\rm cut}=.08$ 当成 $\epsilon$，也没有丢掉 $\delta_0^{11/4}$ 或 $r_c^7$ 的归一因子。附属脚本从保存报告读取原两个 IEEE-754 数，取它们的精确分数，进行 (1.2) 的交叉相乘比较。

本证明只作用于 $n\ge160=\texttt{protectCell}$ 的**未作径向 warp** 的有理深源。它满足

$$
\rho_s=\rho/\sqrt{12},\qquad
P=\epsilon\delta^{11/4}p_*,\qquad w=P/\rho^7.
$$

深处所有剩余 log 长度是收敛的正几何级数，故 $1\le\rho\le2$；例如单个胞元及其更深部分的总长度小于 $8\delta_n$，于是
$\rho\le\exp(8\delta_n/\sqrt{12})<2$。
原浅头的全宽 warp 系数仍为 $161.27721826272244$。它不出现在这个未改造深域的 $\rho_s$ 中，因而无需也不能在下列深域常数里偷偷省去一个 warp 因子。对 $0\le n<160$ 的真实半径、$r_s,r_{ss}$、角宽和传播常数，R15 §9 仍要求独立计算。

## 2. 引用的完整方程与逐项数字化的范围

固定来源仍为提交 869436630c99aa5a68afb55bd8877c826034d117：

- Q：general-exact-mild-tail-quadratic-material.md §§2–7，完整 mean、压缩逆、精确二次源恒等式；
- L：general-geometry-mild-tail-huge-r-cell-estimates.md §§1–3，实际九段传播、Lipschitz 64、mean 小根；
- F：general-geometry-mild-tail-forced-shadowing-lemma.md §§1–5，强时空范数及真正全频强迫校正；
- A：general-exact-mild-tail-full-analytic-map.md §§3–9，Galerkin 近解加全频校正的共同复球流程。

F 的已恢复文件 SHA256 为 9da80e91c7500bf4ca198e0f03765ed6a98c251b7c63471493cee3327076463f。本文采用它们已经写出的完整方程和 Volterra 收缩，不另要求独立审查。下面逐项给出这次固定参数可用的常数，不以“同一证明适用”替代预算。

固定

$$
\gamma=h/32,\qquad
M=2\left\lceil\frac{10016}{2\gamma}(1+|\log\delta|)\right\rceil,
\qquad \mu_0=\epsilon\delta^{11/4}.
$$

对 $n\ge512$，由 $\log2>2/3$、$|\log\delta_n|<n+6$ 得

$$
1+M\le2^{21}(n+8)\le\delta_n^{-1/16}.
\tag{2.1}
$$

第二个不等式在 $n=512$ 由整数比较验证，此后其右侧每步乘 $2^{1/16}$，左侧至多乘 $521/520$，仍保持。$M$ 是证明 cutoff，不是最终尾的角频截断。

## 3. 全部低模真实内部传播：$K_M\le2^{16}(1+M)^{12}$

令 $m\ge2$ 为偶角频、$\nu=m^2(m^2-1)/12$、$k=(m^2-4)/\sqrt{12}$。一个平台的部分传播矩阵及其逆满足

$$
\|e^{tB}\|_1,\ \|e^{-tB}\|_1
\le1+|k|\delta+\max(\nu p_*\delta,\delta/p_*)
\le8(1+m)^4,\qquad 0\le t\le\delta.
\tag{3.1}
$$

第一步来自 $B^2=-(7m^2-16)I/12$ 的实际三角函数公式。三个平台的乘积至多 $2^9(1+m)^{12}$。

每个短段（四转接和两个端口）有

$$
\int\|B(s)\|_1\,ds
\le c_\eta\delta^{1/2}\{m^2\delta/3+2+(16/3)m^4\}
\le4(1+m)^4\delta^{1/2}.
$$

在 $m\le M\le\delta^{-1/16}$ 上，六段总和至多 $384\delta^{1/4}<\log2$。其任意子段组合及逆的总增益至多2。端口 raw/canonical 转换只含 $1$ 和 $2^{11/4}<7$。因此所有完整或部分内部传播均可统一放宽到

$$
K_M\le K_0(1+M)^{12},\qquad K_0=2^{16}.
\tag{3.2}
$$

这里使用真实 profile 和传播矩阵范数，未用谱半径取代非正规增益。

## 4. 完整二次源与低 Galerkin 复球

在 Q 的变量中记

$$
X=\|Q\|_{\tau,3}+\|\pi\|_{\tau,1},\qquad
\mathsf P=v_\theta/(\rho w),\quad K=v_\rho/w,\quad
L=K+\mathsf P_\theta,\quad U=K_\theta-\mathsf P.
$$

由 Q 的精确系数恒等式、$1\le\rho\le2$、$\sqrt{12}<4$，nonmean 部分满足

$$
Y_\perp:=
\|\mathsf P\|_{\tau,1}+\|K_\perp\|_\tau+
\|L_\perp\|_\tau+\|U\|_\tau
\le2^{14}\mu_0^{-1}(p_*^{-1}+p_*^{-2})X.
\tag{4.1}
$$

在 $Y_\perp\le10^{-4}$ 的小球内，L 的完整 mean 根估计
$|K_0|\le40(\|K_\perp\|+\|\mathsf P\|_1)^2$ 把全部相对量放大至多2倍。压缩 leading inverse 和 $\rho_{\rm dens}=D^{-3/2}$ 的范数各至多2。Q 的精确二次恒等式于是给

$$
\|H\|_\tau\le20(1+|\lambda|)(2Y_\perp)^2,
$$

$$
\|\mathcal N\|_\tau
\le\frac{2^{36}}{\mu_0}(1+|\lambda|)(1+p_*^{-2})X^2.
\tag{4.2}
$$

第二式使用精确因子
$\mathcal N=(wp_*/(\sqrt{12}\rho^3))H$ 和
$p_*^2(p_*^{-1}+p_*^{-2})^2\le2(1+p_*^{-2})$。
特别地，没有把压缩逆换成先取点态倒数再截断。

实际材料积分有一个简单的数字上界。总长小于 $4\delta$、$p_*\ge\delta/2$，给无导数部分至多 $20\delta^{-1}$；四个 log 单调转接给

$$
\int|\partial_s\log p_*|\,ds\le20\delta^{-2},\qquad
\int|\partial_s\log p_*|p_*^{-2}\,ds\le6\delta^{-2}.
$$

再用 $|\lambda|\le|\partial_s\log p_*|+7/\sqrt{12}$，得到

$$
\int(1+|\lambda|)(1+p_*^{-2})\,ds
\le106\delta^{-2}<2^7\delta^{-2}.
\tag{4.3}
$$

故在有限频率窗口内，连同规范的固定等价常数，可安全采用

$$
\int\|\mathcal N_M\|_\tau\,ds
\le\frac{C_{\rm mat}(1+M)^6}{\mu_0\delta^2}
\sup_s\|Z_M(s)\|_\tau^2,\qquad C_{\rm mat}=2^{52}.
\tag{4.4}
$$

原逐项预算只需 $2^{43}$；这里保留九个二进制位的余量。所有不等式均在复 Wiener 球成立，包括完整 mean 分支。

取较大的辅助输入球

$$
I:=\|U_{\rm in}\|_{\tau+h}
\le R_0:=c_0\mu_0\delta^2(1+M)^{-60},
\qquad c_0=2^{-240}.
\tag{4.5}
$$

bootstrap $\sup_s\|Z_M\|\le2K_0(1+M)^{12}I$ 下，Duhamel 非线性校正与 $K_0(1+M)^{12}I$ 之比至多

$$
4C_{\rm mat}K_0^2c_0(1+M)^{-30}
\le2^{-154}<1/2.
\tag{4.6}
$$

与此同时 $p_*^{-1}+p_*^{-2}\le6\delta^{-2}$，所以 (4.1) 连同 mean 不超过
$2^{36}c_0(1+M)^{-45}\ll10^{-4}$。
因此正分支、复 leading inverse 及上述 bootstrap 都严格改善；有限维继续到整个胞元。这里没有以尚未证明的流存在性作为小量假设。

## 5. 全频校正的全部常数

### 5.1 全局物理球与强时空范数

物理变量是 $W=(p,\kappa)$。精确换算

$$
p=\rho^3Q_\theta,\qquad
\kappa_\perp=\rho^3(\sqrt{12}\pi/p_*+|D_\theta|^2Q)
$$

和 (3.2)、完整 mean 根给

$$
\sup_s\|W_M\|_{\tau+h,1}
\le2^{25}\delta^{-1}(1+M)^{15}I.
$$

花去一次 $h/8$ 将 $\sup_s\sum_m$ 转为 $\sum_m\sup_s$。因为

$$
\sum_{m\in\mathbb Z}e^{-(h/8)|m|}
\le1+16/h<2^7,
$$

得到

$$
Y_{\rm app}:=\|W_M\|_{\tau+7h/8,1}^{\#}
\le2^{32}\delta^{-1}(1+M)^{15}I.
\tag{5.1}
$$

由 $w_{\min}\ge\mu_0\delta/256$，在 (4.5) 上

$$
Y_{\rm app}/w_{\min}\le2^{40}c_0(1+M)^{-45}
\le2^{-200}<10^{-6}/8.
\tag{5.2}
$$

这是 F 要求的统一 $w_{\min}$ 物理球，不是仅逐点相对当前 $w(s)$ 小。

### 5.2 完整残差和初值差

有限 Galerkin 解满足压缩密度方程。置
$H_{\rm res}=B\kappa_y^M-\rho_{\rm dens}\mathscr G$，则
$\Pi_MH_{\rm res}=0$，完整残差严格是

$$
e=B^{-1}(I-\Pi_M)H_{\rm res}.
$$

在 (5.2) 的复球上，L 的逐项物理估计给
$\|H_{\rm res}\|^\#\le64m_{\max}Y_{\rm app}$、$\|B^{-1}\|\le2$。
此外

$$
m_{\max}\le C_M\delta^{-5/2},\qquad
C_M=1+\frac{15}{8c_\eta}(2+\log128)<23.
$$

花去另一次 $h/8$，以 $\gamma=h/32$ 保守地记录指数尾，得到

$$
S:=\|e\|_{\tau+3h/4,0}^{\#}
\le2^{44}e^{-\gamma M}(1+M)^{15}\delta^{-7/2}I.
\tag{5.3}
$$

乘 $B^{-1}$ 可以重新产生低模；(5.3) 界定的是**完整**残差，不假定其低模消失。

完整输入与投影输入各自求其 complete mean 小根。从 raw 到物理 $\mathcal W^1$ 至多使用三阶角导数。在
$h/4-\gamma=7h/32>7/192$ 上，

$$
\sup_{m\ge0}(1+m)^3e^{-(7h/32)m}
\le(1+576/7)^3<2^{20}.
$$

物理换算和 mean 根在该小球的 Lipschitz 因子至多 $2^{10}$，故初值差满足

$$
I_0\le2^{30}e^{-\gamma M}I,\qquad
I_0+9S\le2^{48}e^{-\gamma M}(1+M)^{15}\delta^{-7/2}I.
\tag{5.4}
$$

### 5.3 真实九段 Volterra 增益与允许球

L/F 的明确粗常数在当前参数为

$$
K_R=2^9C_M^4\exp[256(3d_0+6\eta_0)]128^{960}.
$$

利用 $d_0<1/128$、$\eta_0=c_0^{\rm source}d_0\le1/2048$，
$256(3d_0+6\eta_0)\le27/4$。因此

$$
\boxed{K_R<2^{6764}.}
\tag{5.5}
$$

这里 $c_0^{\rm source}\le1/16$ 是 profile 宽度参数，区别于 (4.5) 的小球常数 $2^{-240}$。
Lipschitz 64、固定 $L=256$ 的真正 Volterra 校正给

$$
\|V\|_{\mathcal W^1}^{\#}
\le K_R\delta^{-2890}(I_0+9S)
\le2^{6812}(1+M)^{15}\delta^{7122.5}I.
\tag{5.6}
$$

最后一步用 $e^{-\gamma M}\le\delta^{10016}$。在 $n=512$ 上，$M<2^{31}$、$\delta<2^{-519}$，故 (5.6) 的 $I$ 系数的二进制对数小于

$$
6812+15\cdot31-\frac{14245}{2}\cdot519
=-3689300.5.
\tag{5.7}
$$

此后多项式因子的每步比值至多 $(521/520)^{15}$，被 $2^{-7122.5}$ 严格压倒。所以 (5.6) 对全部 $n\ge512$ 都小于 $I$；代入最大输入 (4.5) 后，更小于 $10^{-6}w_{\min}/4$。这实际支付了每个子段的强迫允许球，不能仅以残差小为由省略。

连更强的粗原点球也成立。对当前 $h$，L 的
$B_h=64(1+12/h)^3<2^{25}$，粗半径系数
$c_\rho=10^{-6}/(8192B_hK_R)>2^{-6822}$。
由 (5.4)、(4.5)，初值加九倍强迫至多

$$
2^{-192}\mu_0(1+M)^{-45}\delta^{10014.5}
<c_\rho\mu_0\delta^{2891}.
$$

该不等式在 $n=512$ 已有远超所需的指数余量，之后继续改善。全过程只使用固定的移动角宽；$h/8+h/8+h/4=h/2$ 后仍余至少 $\tau+h/2$，没有在迭代中反复花角宽。

## 6. Cauchy 余项、全部两 jet 与局部常数 (0.1)

低 Galerkin 部分满足 (3.2)；全频校正由 (5.6) 至多 $I$。端口 physical/raw 转换范数至多4。因此完整胞元 map 在共同复球 $B(R_0)$ 满足

$$
\|\Phi_n(U)\|_\tau\le2^{20}(1+M)^{12}\|U\|_{\tau+h}.
\tag{6.1}
$$

所有有限流、mean 根和强迫固定点在同一个复参数球全纯。线性化严格是实际 $T_n$；mean 根一阶为0。
在 $R_0/16$ 内用 Banach 空间的 Cauchy 估计，可将二次余项和其二次 Lipschitz 系数均放宽到

$$
\frac{2^{268}(1+M)^{72}}{\mu_0\delta^2}.
\tag{6.2}
$$

为避免半径约定差异，最终只使用更小的
$2^{-256}\mu_0\delta^2(1+M)^{-60}=2^{-16}R_0$，并将 (6.2) 放宽至 $2^{320}$。

两 jet 同样显式。低 Galerkin 物理 $\mathcal W^1$ 界至多
$2^{25}\delta^{-1}(1+M)^{15}I$；完整压缩方程给径向导数至多
$32m_{\max}$ 倍此量，物理 $d/d\rho$ 再至多乘4。因此其所有高度两阶以内 jets（包括 mean 的一二阶）可取

$$
2^{40}(1+M)^{15}\delta^{-7/2}I.
$$

差量完整方程在同一物理球上逐项相减，leading inverse 的 $w_{\min}^{-1}$ 与原右侧 $O(m_{\max}10^{-6}w_{\min})$ 配对。可用
$\|\delta\mathcal F_2\|\le64m_{\max}\|V\|_{\mathcal W^1}$，所以差量两 jet 至多 $2^{14}\delta^{-5/2}\|V\|$。
(5.7) 使该量远小于前述 $2^{40}$ 上界。
因此同一个 $C_*=2^{320}$ 支付 R15 (2.3)。

mean 高度只沿真实 $\kappa_0$ 积分一次；单胞元积分长度至多 $4\delta$。没有在两个端口另加相互独立的 mean 高度条件。由此 (0.1) 对存在、二次 Lipschitz、完整 mean 和全部胞元两 jet 同时有效。

## 7. 逐个支付 $N=4096$ 的全部门

对 $n\ge512$，函数
$(n+8)^{60}2^{-3n/4}$ 和 $(n+8)^{72}2^{-3n/8}$ 均递减；这由相邻比值或
$60/(n+8)<(3/4)\log2$、$72/(n+8)<(3/8)\log2$ 直接得到。
在 $N=4096$ 上，

$$
M_N\le2^{21}(4096+8)<2^{34},\qquad
\delta_N<2^{-4103}.
$$

于是 R15 的两个上确界满足

$$
c_*^{-1}A_N
<2^{256+60\cdot34-(3/4)4103}
=2^{-781.25}<1/4,
\tag{7.1}
$$

$$
2C_GC_1\delta_N^{3/8}B_N
<2^{1+27+320-11/2+72\cdot34-(3/4)4103}
=2^{-286.75}<1/4.
\tag{7.2}
$$

线性扰动门由 R15 已得

$$
\eta_N<2^{85-N/2}=2^{-1963}<1/4.
\tag{7.3}
$$

局部角宽门从 $n\ge128$ 即成立；真实低模传播与局部全频流从 $n\ge512$ 成立；$N=4096\ge224$ 也支付低46高度 chart 的线性逆。
归一 slope 满足

$$
w\le64\epsilon\delta_N^{7/4}
<2^{6+15-(7/4)4103}<1
$$

而且全部更深胞元继续改善。故当前 $\epsilon$ 下全部假设均由固定 $N=4096$ 支付。
更一般地，此 $N$ 同时覆盖 $0<\epsilon\le2^{7000}$；若 $\epsilon$ 更大，只须再增加一次固定 $N$ 使 $6+\log_2\epsilon-(7/4)(N+7)\le0$。

令 R15 §8 的 $r=C_GC_1\delta_N^{3/8}B_N$。上式给 $r<2^{-287.75}$，所以其半径可具体取

$$
r_b=1/4,\qquad r_z=1/16000000.
\tag{7.4}
$$

这是 $N$ 处**归一低46高度坐标**的半径，绝不是物理浅 cut 高度或用户要求的直径比例。

## 8. 重现和剩余的精确接口

精确分数账本从仓库根运行：

    python topics/visible-flex-larger-amplitude/computations/closure_rational_nonlinear_constants.py \
      --source-report topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-rational-trace-m46-s512.json \
      --out topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-rational-nonlinear-constants.json

该脚本只核算本文明确常数之间的整数/分数比较；全频流存在性的推导在 §§3–6。它不把浮点 PDE 迭代的成功作为证明。

$d_0 2^{-4096}$ 在实数定义中非零，普通 double 不能直接保存。当前 far192/256 的数值图还需要**尺度化传播和严格余项界**才能接到本文的完整非线性图。本文也没有给出任意有限角截断可以把高模高度设0的许可：R15 的第47模以后从二阶起被强迫。

已支付的只有 R15 所留的具体局部常数和共同非线性深起点。保留的工作是：真实有限头的解析/余项预算、浅 cut 的大幅 trace 匹配、固定新 $g$ 的加密，以及完整闭曲面的连续空间嵌入、reach 和强幅度。它们仍须继续计算。
