# R119 真根联合解析证明：原实解进入唯一性空间的完整衔接

2026-11-13，tail_connector。**状态：已证明的衔接说明。**

本说明补全
`results/R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md`
(J.8) 后的实解识别步骤。该 proof 原字节 SHA256 为
`6f12b6a6a79bdff8deb26e9092e46ab08463e19064912d518d50c981e592741a`，
与其77门 native 均保持不变。这里不预先假定原实解对径向解析。

## 1. 已有的是完整实 germ 上的角范数界

在第 $j$ 个胞元中，真实根到最近接缝的缩放距离大于13，
所以完整实段 $-1\le x\le1$ 都包含在该同一胞元内。
对 $j>8192$，强首剪切局部图 (T.23) 后的相对四态界是由完整
局部强解得到的全胞元界，而不是只在两个端口读取的值：在已付
输出角宽内，$P,K,P_\theta,K_\theta$ 的每个 Wiener norm
至多
$$
 B_j:=N_j\|X\|_{\mathcal X_{224}},\qquad
 N_j=2^{184}h_j^{-5}\zeta_j/(\mu_j\delta_j^2).
 \tag{C.1}
$$
对未改的 $129\le j\le8192$，
`R119-supplement-new-deep-profile-full-label-chart.md` §6 在
(L.21) 前给完整局部强解的更小费用
$2^{47}h_j^{-5}\zeta_j/(\mu_j\delta_j^2)$；整个旧前缀因此也
被 (C.1) 覆盖。新全标签篇 (U.24)--(U.25) 用的正是这一
共同全实段包络。真实 $K_0$ 已包含在这四态中。

这些界对局部 map 的任意绝对基宽成立。当前真实标签权是224，
所以共同物理角宽可取 $\sigma_j\ge\tau_{j-1}+224>5$；
这只是把同一个已付加权解限制到更小角域，没有额外增加标签权。

## 2. 非解析径向实空间中的强 norm

定义 $\mathcal B^k_{\mathbb R}$ 与主文 (J.6) 完全相同，但把
$\sup_{|x|\le1}$ 改为实段 $\sup_{-1\le x\le1}$，并只要求每个
Fourier 系数对实 $x$ 连续。这个空间不包含任何径向解析假设。

对每个非零 $m\in4\mathbb Z$，(C.1) 和准确恒等式
$U_m=imP_m,V_m=imK_m$ 给
$$
 \sup_{x\in[-1,1]}(1+|m|)(|P_m(x)|+|K_m(x)|)
       \le4B_j e^{-\sigma_j|m|}.
$$
在 $m=0$，两项之和至多 $2B_j$；也可以使用实际
$P_0=0$ 得到更小费用，但不需要它来证明这个门。
径向指数权小于等于1，故
$$
 \|(P,K)\|_{\mathcal B^1_{\mathbb R}}
 \le B_j\left[2+8\sum_{k\ge1}e^{-4k(\sigma_j-4)}\right]
 <B_j\left(2+\frac8{15}\right)
 =\frac{38}{15}B_j<4B_j=n_j.
 \tag{C.2}
$$
这里仅用了 $\sigma_j-4>1$ 和 $e^{-4}<1/16$。
所以即使 (C.1) 先给的是每个实截面的角范数，而非先逐模取
径向上确界的强范数，也已用真实余宽把后者明确支付。
特别原实解确实进入 $n_j<2^{-32}<r_0=2^{-16}$ 的完整小球。

## 3. 在实空间应用同一个唯一性收缩

主文 (J.7) 的乘法、完整 leading 分母和 Lipschitz 证明只用
绝对值和 Fourier 卷积，原样适用于 $\mathcal B^k_{\mathbb R}$。
沿正半段与负半段分别从0积分时，径向指数核仍准确给
$$
 \|\mathcal V f\|_{\mathcal B^1_{\mathbb R}}
             \le2^{-12}\|f\|_{\mathcal B^0_{\mathbb R}}.
$$
因此相同的 $1/64$ 收缩在实空间成立。
原全标签解是 $C^1$ 的相对场，满足完整未投影 PDE，故满足同一
实 Volterra 积分方程。由 (C.2) 它在收缩小球内。
联合解析 CK 解的实限制也在该球内并有同一初值。
两者的差遂满足
$$
 \|W_{\rm real}-W_{\rm CK}^{\mathbb R}\|_{
                       \mathcal B^1_{\mathbb R}}
 \le\frac1{64}
 \|W_{\rm real}-W_{\rm CK}^{\mathbb R}\|_{
                       \mathcal B^1_{\mathbb R}},
$$
所以差严格为0。
这才将已经构造的真实非线性尾识别为 CK 解的实限制；没有先把
它放进需要径向解析性的 $\mathcal B$ 再循环使用唯一性。
完整 mean、holonomy 和独立高度积分常数均沿该相同实解保留。
