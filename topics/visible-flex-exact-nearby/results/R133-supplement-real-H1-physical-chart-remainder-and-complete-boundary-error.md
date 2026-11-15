# R133：真实 H1 角图余项、完整 mean 与一次帽差后的非线性边界费

2026-11-15。状态：下面实角值估计与差分估计已由明确原域推得；没有新增数值运行。只要求未知方向的一阶角导，不在未知函数上取复角，也不从 whole C0 小球推导裸 composition 算子小量。

引用 [AR 一次帽图消元](R133-supplement-actual-cap-affine-height-and-single-integral-boundary-elimination.md)、[W 已知 cut 与 scalar 准入](R133-supplement-known-finite-cut-Wiener-angle-and-sharp-low-curvature-entry.md)、[RB 原真实角与两 mean](R133-supplement-actual-right-cap-body-and-nonlinear-moving-L2-comparison.md)、[NF 固定 97 残差](R133-supplement-divergence-nonlinear-core-source-and-complete-finite193-receivers.md)、[CPA 实际 inner 差](R133-supplement-actual-weighted-cap-inner-difference-and-finite193-inverse.md)。

## CH1. 同一个已知 selected cut；未知 H1 门明确列出

在真 cut $L=9/10$ 固定
$$
 \bar Q=Q_\delta(L)=(\bar u,\bar v),\qquad
 \bar m=\langle\bar v\rangle_\phi,\quad
 \bar j=\bar v/\bar m,\qquad |\delta|\le10^{-10}.
$$
W.25、RB.5 和准确 finite96 身份给
$$
 \begin{gathered}
 |\bar m|>25/8,\quad |\bar m|<6,\quad
 63/64<\bar j<65/64,\quad
 \|\bar j-1\|_\infty<1/64,\quad
 \|\bar j'\|_\infty<1/16,\\
 |\bar u|<1/50,\qquad
 \|\bar u'\|_\infty+\|\bar v'\|_\infty<1/2 .
 \end{gathered}\tag{CH.1}
$$
这里两分量导数取各自完整 supremum 后相加。
$\bar u,\bar v$ 的 physical 频率属于 $|4j|\le384$；mean 与 canonical 连续 offset 都在原 finite96 内。
标量三角多项式 Bernstein 不等式逐分量给
$$
             \|\bar u''\|_\infty+\|\bar v''\|_\infty<192 .
 \tag{CH.2}
$$
(CH.2) 只用于这个已知有限函数，绝不用于未知 high。

设未知方向 $h=(\xi,\eta)$ 为实反射同类的 $H^1_\phi$ 函数，置
$$
 r=\|\eta\|_{H^1},\quad s=\|\xi\|_{H^1},\quad
 e=\|\eta\|_2,\quad \mu=\langle\eta\rangle_\phi,
 \qquad r\le2^{-10}.
 \tag{CH.3}
$$
本节至 CH5 不要求 $s$ 小。所有 $H^1$ 和 $L^2$ 用周期 $\pi/2$ 的 normalized measure 与实际物理导数 $\partial_\phi$。
Cauchy--Schwarz 对完整 signed $4\mathbb Z$ 给
$\|a\|_\infty\le2\|a\|_{H^1}$；
原 primitive $I=\partial_\phi^{-1}P_\perp$ 满足
$\|I:L^2\to L^\infty\|=\pi/(4\sqrt3)<1/2$。

## CH2. 真实路径上的正 Jacobian 与完整 mean

置 $v_t=\bar v+t\eta$、$m_t=\bar m+t\mu$、$j_t=v_t/m_t$。
由 (CH.1)--(CH.3)，对 $0\le t\le1$，
$$
 |m_t|>3,\quad |v_t|>3,\quad m_t,v_t<0,\qquad
                    31/32<j_t<33/32.
 \tag{CH.4}
$$
例如 $|\bar v|>(25/8)(63/64)$ 且 $\|\eta\|_\infty\le2^{-9}$，
所以第一组有正余量。另一方面
$$
 j_t-\bar j=\frac{t(\eta-\bar j\mu)}{\bar m+t\mu},
 \qquad \|j_t-\bar j\|_\infty<2r\le1/512,
$$
足以把 W.25 的条带留在 (CH.4) 中。

定义同一反射 phase 下的真实 lifts
$$
 \Theta_t=\mathrm{id}+I(j_t-1),\qquad \Phi_t=\Theta_t^{-1}.
$$
所有 $j_t$ 的 mean 都准确为1，故这些是同一圈上的 lifts；$C$ 的 changing mean 没有冻结。
对任意 $a\in L^2$，
$$
 \|a\circ\Phi_t\|_{L^2_\theta}
       \le\sqrt{33/32}\|a\|_{L^2_\phi}<2\|a\|_2 .
 \tag{CH.5}
$$
而 $\Phi_t'\ge32/33$。任意两端 inverse lifts 的凸组合也有该 lower bound，因此对 $a\in H^1$，
$$
 \|a\circ\Phi-a\circ\widetilde\Phi\|_2
       \le2\|\Phi-\widetilde\Phi\|_\infty\|a'\|_2 .
 \tag{CH.6}
$$
这是沿真实一维 maps 的 FTC 与真测度变换，不是 $L^2$ composition-minus-identity 的无导数界。对 $H^1$ 函数先作平滑逼近再用 (CH.6) 即可，常数不变。

## CH3. 逆角的一阶项与真实二次值余项

写
$$
 A=I(\eta-\bar j\mu),\qquad
 \ell=A/\bar m,\qquad
 \Theta_1-\Theta_0=A/(\bar m+\mu).
 \tag{CH.7}
$$
由于 $\eta-\bar j\mu=P_\perp\eta-(\bar j-1)\mu$，
$$
 \|A\|_\infty\le\frac{65}{128}e,\quad
 \|\ell'\|_\infty\le\frac{193}{200}r<r,\quad
 \|\Theta_1-\Theta_0-\ell\|_\infty\le e^2/16 .
 \tag{CH.8}
$$
最后一项使用准确差
$-\mu A/[\bar m(\bar m+\mu)]$，保留全部 $\mu$。

令
$$
 \Delta=\Phi_1-\Phi_0,\qquad
 L_\eta=-\left(\frac{\ell}{\bar j}\right)\circ\Phi_0 .
$$
已知 $\Theta_0'\ge63/64$ 给
$$
 \|\Delta\|_\infty\le(65/378)e<e/5 .
 \tag{CH.9}
$$
用 $\Theta_1(\Phi_1)=\Theta_0(\Phi_0)$ 在固定 $\Phi_0$ 展开，准确得到
$$
 \begin{split}
 \bar j(\Phi_0)(\Delta-L_\eta)
 ={}&-\{\Theta_0(\Phi_0+\Delta)-\Theta_0(\Phi_0)
                          -\bar j(\Phi_0)\Delta\}\\
 &-(\Theta_1-\Theta_0-\ell)(\Phi_1)
       -\{\ell(\Phi_1)-\ell(\Phi_0)\}.
 \end{split}\tag{CH.10}
$$
三项上界依次为 $e^2/800$、$e^2/16$、$re/5$。
再用 $\bar j^{-1}<2$ 及 $e\le r$，有
$$
             \boxed{\ \|\Delta-L_\eta\|_\infty\le re.\ }
 \tag{CH.11}
$$
只出现未知 $\eta$ 的 $H^1$；没有未知二阶导。

## CH4. 先 ratio 后真实 composition 的完整余项

对 $Q=(u,v)$，
$$
 \Psi(Q)=(B_Q,C_Q)
       =\left(\frac uv,\frac1v\right)\circ\Phi_v .
 \tag{CH.12}
$$
设 $a_0=(\bar u/\bar v,1/\bar v)$，直接 ratio 的线性项为
$$
 L_B=\xi/\bar v-\bar u\eta/\bar v^2,\qquad
 L_C=-\eta/\bar v^2 .
$$
准确 ratio 余项为
$$
 R_B^{\rm rat}=-\frac{\xi\eta}{\bar v(\bar v+\eta)}
                  +\frac{\bar u\eta^2}{\bar v^2(\bar v+\eta)},
 \qquad
 R_C^{\rm rat}=\frac{\eta^2}{\bar v^2(\bar v+\eta)} .
 \tag{CH.13}
$$
因此 physical chart 的线性项确为
$$
 D\Psi(\bar Q)h=(L_B,L_C)\circ\Phi_0
                           +(a_0'\circ\Phi_0)L_\eta .
$$
这与 NF 的同 mean、同 phase 真实微分一致。其余项
$R_\Psi=(R_B,R_C)$ 准确拆成
$$
 \begin{split}
 R_\Psi(h)={}&R^{\rm rat}\circ\Phi_1
       +L(h)\circ\Phi_1-L(h)\circ\Phi_0\\
 &+\{a_0\circ\Phi_1-a_0\circ\Phi_0
                         -(a_0'\circ\Phi_0)\Delta\}\\
 &+(a_0'\circ\Phi_0)(\Delta-L_\eta).
 \end{split}\tag{CH.14}
$$
所有乘法与 composition 在取 norm 前保持原次序；两个 mean 都在原式中。

由 (CH.1)--(CH.4) 逐项得
$$
 \|L_C'\|_2\le4r/27,\qquad
 \|L_B'\|_2\le s/2+r/16 ,
 \tag{CH.15}
$$
以及已知函数的
$$
 \|(a_{0,C})'\|_\infty<1/18,\quad
 \|(a_{0,C})''\|_\infty<22,\qquad
 \|(a_{0,B})'\|_\infty<1/6,\quad
 \|(a_{0,B})''\|_\infty<65 .
 \tag{CH.16}
$$
例如 $C$ 二导费为 $192/9+1/54<22$；$B$ 的 second-order ratio 逐项为
$|\bar u''|/3+|\bar u||\bar v''|/9+
2|\bar u'||\bar v'|/9+2|\bar u||\bar v'|^2/27<65$。
没有从未知函数的 finite support 获得这些数。

## CH5. 两分量各自的 H1 二次界

由 (CH.5)--(CH.16)，$C$ 的四项完整费用不超过
$$
 \left(\frac4{27}+\frac8{135}+\frac{11}{25}+\frac1{18}\right)re
                         =\frac{949}{1350}re<re .
$$
$B$ 的费用不超过
$$
 \left(\frac49+\frac15\right)rs
 +\left(\frac2{675}+\frac1{40}+\frac{13}{10}+\frac16\right)re
                <rs+2re .
$$
所以
$$
 \boxed{\quad
 \|R_C(h)\|_{L^2_\theta}\le r\|\eta\|_2,\qquad
 \|R_B(h)\|_{L^2_\theta}\le rs+2r\|\eta\|_2 .
 \quad}\tag{CH.17}
$$
特别地，physical C 的 remainder 不依赖 $\xi$。
$P_{\perp,\theta}$ 是同 physical normalized $L^2$ 的正交投影，故其 nonmean remainder 不增大。

完整 Cmean 仍有更准确的 signed 恒等
$$
 \langle R_C(h)\rangle_\theta
 =\frac{\mu^2}{\bar m^2(\bar m+\mu)},\qquad
 |\langle R_C(h)\rangle_\theta|\le\mu^2/27 .
 \tag{CH.18}
$$
这是 $d\theta=j_1d\phi$ 下 $\langle C_Q\rangle_\theta=1/m_1$ 的结果，不把 moving mean 与 physical mean 直接等同。

## CH6. 同一个 H1 球上的真实差分；不假设全图 C2

为明确付收缩所需的差分，令
$$
 \|h_1\|_{H^1}+\|h_2\|_{H^1}\le\varrho,\qquad
 \|k_1\|_{H^1}+\|k_2\|_{H^1}\le\varrho,\qquad
 \varrho\le2^{-10},
$$
并记 $d_i=\|h_i-k_i\|_{H^1}$、$d=d_1+d_2$。
对两个第二分量重复 (CH.7)，由真 inverse 的 lower Jacobian 得
$$
 \|\Phi_h-\Phi_k\|_\infty\le d_2/4 .
 \tag{CH.19}
$$
(CH.10) 逐项相减可用
$$
 \|(\Delta_h-L_{h_2})-(\Delta_k-L_{k_2})\|_\infty
                                      \le4\varrho d_2 .
 \tag{CH.20}
$$
这里是准确差式的直接估计：
已知 $\Theta_0$ 二次 Taylor 差至多 $\varrho d_2/320$；
$-\mu A/[\bar m(\bar m+\mu)]$ 及其 composition 的差至多 $\varrho d_2/3$；
$\ell(\Phi)-\ell(\Phi_0)$ 的两差至多
$(1/5+1/4)\varrho d_2$；
最后只乘 $\bar j^{-1}<2$。显示常数4还有余量。
这一步没有微分未知 $\eta'$。

对 (CH.14) 的三个组合部分，可以保留以下完整上界：

| 完整部分 | 差分的 $L^2_\theta$ 两分量 norm-sum |
|---|---|
| ratio remainder 后 composition | $2\varrho d$ |
| linear ratio 的 composition 差 | $\varrho d$ |
| 已知 ratio 的 Taylor 余项加 inverse-angle 余项 | $6\varrho d$ |

第一行可由
$A_\eta=\eta/[\bar v(\bar v+\eta)]$、
$\|\partial_\eta A_\eta\|_\infty\le1/9$ 直接相减：
$\|R^{\rm rat}(h)-R^{\rm rat}(k)\|_{L^2\oplus_1L^2}\le\varrho d/2$，
且 $\|(R^{\rm rat}(k))'\|_{L^2\oplus_1L^2}\le\varrho^2$。
再用 (CH.5)、(CH.6)、(CH.19) 即得该行。
第二行先分出 $L(h-k)$ 与 $L(k)$，用 (CH.15)、(CH.9)、(CH.19)。
第三行使用 (CH.16) 的 second-derivative norm-sum $<87$、
$\max(\|\Delta_h\|_\infty,\|\Delta_k\|_\infty)\le\varrho/5$，
及 (CH.19)--(CH.20)；first-derivative norm-sum $<1/4$。
于是
$$
 \boxed{\quad
 \|R_\Psi(h)-R_\Psi(k)\|_{L^2_\theta\oplus_1L^2_\theta}
 \le16\varrho\,\|h-k\|_{H^1_\phi\oplus_1H^1_\phi}.
 \quad}\tag{CH.21}
$$
该差分界只在固定已知基点的 remainder 上成立；不声称 rough $H^1$ 上整个 composition map 具有统一二阶 Banach 微分。

scalar mean 可继续单独保留 (CH.18)，其差有
$$
 |\langle R_C(h)-R_C(k)\rangle_\theta|
                    \le(2/27)\varrho\,|\langle h_2-k_2\rangle_\phi|.
 \tag{CH.22}
$$
为核这个常数，令 $M(\mu)=1/(\bar m+\mu)-1/\bar m+\mu/\bar m^2$。
准确有 $M'(\mu)=\bar m^{-2}-(\bar m+\mu)^{-2}$。
(CH.1) 的 $|\bar m|>25/8$ 与 $\varrho\le2^{-10}$ 使整个实均值线段同为负且绝对值大于3；对 $x^{-2}$ 的一维 FTC 给
$|M'(\mu)|\le2|\mu|/27$，再沿两均值之间积分得 (CH.22)。

## CH7. 到实际 full 97 行的明确 nonlinear source

现在另要求两个真实 physical gamma 输入和固定 normalized height 位于 AR.1 的同一个帽 product。仅 (CH.3) 或 (CH.21) 并不支付这个条件。
W.30--32 的独立 scalar 门可给具体入口，亦可消费另一条已经证明的同对象准入。

取 CPA 对应域内的实际 $\kappa$；其有向上端已严格小于 $1/5$。
AR.12--15 对完整
$\mathscr E(h)=\mathcal N_{\partial,\delta}(h)+\Delta\mathcal B_\delta h$
给
$$
 \begin{split}
 \|\mathscr E(h)\|_{97}
 &\le c_{\rm cap}\kappa\|h\|_{L^2_\phi\oplus_2L^2_\phi}
                           +7rs+114r\|\eta\|_2\\
 &\le c_{\rm cap}\kappa\|h\|_{L^2_\phi\oplus_2L^2_\phi}
               +128\|h\|_{H^1_\phi\oplus_2H^1_\phi}^2 .
 \end{split}\tag{CH.23}
$$
第一行使用 $7(16+\kappa)+1/27<114$；第二行用
$2rs\le r^2+s^2$。帽差 $\kappa$ 只出现一次，chart 的所有 mean 仍完整收费。

对 (CH.21) 同一球中的两态，若两 physical gamma 都在同一凸帽域，沿它们的 physical 直线段定义 AR 的平均线性算子 $\mathcal K_{hk}$。其 norm 至多 $\kappa$；因此同一个原 $c_{\rm cap}$ 给
$$
 \boxed{\quad
 \|\mathscr E(h)-\mathscr E(k)\|_{97}
 \le c_{\rm cap}\kappa\|h-k\|_{L^2_\phi\oplus_2L^2_\phi}
 +2^{11}\varrho\|h-k\|_{H^1_\phi\oplus_1H^1_\phi}.
 \quad}\tag{CH.24}
$$
确切组合费是 $7(14+\kappa)16\varrho d$ 加 (CH.22)，小于显示的 $2^{11}\varrho d$。
这里的第二项使用 norm-sum H1 球；不能不付范数转换就改称同半径 Euclidean pair 球。

## CH8. 真实使用范围

(CH.17)、(CH.21)、(CH.23)、(CH.24) 为此前保留的非mean chart remainder 提供具体可消费的值与差分费用。未知函数只在真实角上出现，最多使用其一阶角导；完整原 moving mean、physical Cmean、反射 phase 与固定 $S_\delta$ 均保持。

这些式子是条件接收界，尚未证明 unknown cut 满足相应 H1 半径或 physical gamma 的 A0 准入。实际 affine 源仍是 AR.19 或更尖同 source signed 证据；帽差变小并不使它消失。
若改变 normalized height，AR.16--17 的独立完整 source 另保；若是实际 tail 选择 $f(\gamma)$，本篇不授其 Lipschitz 或 C1 性。
原 waist、meanheight、$\lambda$、high matching 与 infinite high inverse 均不是本篇的图余项。
