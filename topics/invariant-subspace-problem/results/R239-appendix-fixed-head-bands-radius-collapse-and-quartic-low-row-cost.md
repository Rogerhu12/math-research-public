# R239 附录：真实头的固定带多项式界、解析半径坍缩与固定物理行的四次费用

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明。** 本文只讨论负整数边界表示中的真实有限头，沿用[真实 Jordan 成本与纯分级形式像](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md) §§1–3。证明三个结论：任意固定宽度的上三角带在按本列对角元归一后只有多项式费用；无限稳定头级数没有正解析半径；实际固定物理行 $1$ 的远列归一系数确实达到 $\exp(cD^4+O(D^3))$。最后一条同时适用于两个实际慢符号。

这些结论排除了把整个头变换费用统一降成 $\exp(O(D\log D))$ 的估计目标。它们没有排除原 $\Gamma$ Schur、共同源消去或第二下降桥产生的实际抵消，也没有解决边界 $N=M$。

## 1. 原有限头与准确矩阵位置

令
$$B e_n=\alpha_{v_2(n)}e_{n-1},\quad
W_n=\prod_{\ell=1}^n\alpha_{v_2(\ell)},\quad
d_i=W_{2^i},\quad d_0=e^{-20},\quad a_i=(i+1)^{-2}.$$
原权满足
$$W_n=\prod_{i\in\operatorname{bits}(n)}d_i,$$
$$\Lambda_i=-\log d_i
=100\,16^i-105\,8^i+(150i+25)2^i.\tag{1.1}$$
取 $m\ge3,D=2^m$。分别令
$$F_{N,m}(z)=\sum_{i<m}a_i z^{2^i}/d_i,\qquad
F_{Y,m}(z)=\sum_{i<m}a_i\frac{z^{2^i}}{d_i+z^{2^i}}.$$
在零点取逆芽 $\psi_m=F_m^{-1}$，并定义
$$g_m(z)=d_0F_m(z)/z,\qquad g_m(0)=1.$$
这是有限真实头 $H_m=F_m(B_m)$ 的原 Jordan 变换
$H_m=V_mJ_DV_m^{-1}$。所引稿的准确矩阵位置给
$$V_{n,j}=\frac{[w^j]\psi_m(w)^n}{W_n},\qquad
V_{j,j}=d_0^j/W_j.$$
所有系数实，故转置与伴随在此没有额外共轭。由 Lagrange 反演，对 $1\le n\le j<D$，
$$\boxed{\frac{V_{n,j}}{V_{j,j}}
=\frac{W_j}{W_n}\frac nj
[z^{j-n}]g_m(z)^{-j}.}\tag{1.2}$$
$n=0<j$ 时 $V_{0,j}=0$。因此以下估计始终针对原物理矩阵的真实行列，而非任意替代链基。

## 2. 固定宽度的上三角带

固定整数 $L\ge1$。$[z^r]g_m$ 对每个 $r\le L$ 在 $2^m>L+1$ 后稳定。将有限个较小头一并取最大，存在有限常数
$$a_L=\max\left(1,\sup_m\max_{1\le r\le L}
|[z^r]g_m|^{1/r}\right)<\infty.$$
分别对两个模型取该常数即可；也可取两者最大。

对 $1\le\ell\le L$，由于 $g_m-1$ 无常数项，
$$|[z^\ell](g_m-1)^k|
\le\binom{\ell-1}{k-1}a_L^\ell\qquad(1\le k\le\ell).$$
展开 $g_m^{-j}$，用
$\binom{j+k-1}{k}\le\binom{j+\ell-1}{\ell}$ 及
$\sum_{k=1}^{\ell}\binom{\ell-1}{k-1}=2^{\ell-1}$，得到
$$|[z^\ell]g_m^{-j}|
\le a_L^\ell 2^{\ell-1}\binom{j+\ell-1}{\ell}.$$
原单步权满足 $\alpha_k\le d_0$。例如由 (1.1) 精确求和，
$$-\log\alpha_k=\Lambda_k-\sum_{r<k}\Lambda_r
=\frac{280}{3}16^k-90\,8^k+300\,2^k-\frac{850}{3}\ge20.$$
因此 $W_j/W_{j-\ell}\le d_0^\ell$。结合 (1.2)，对 $j>\ell$，
$$\boxed{\frac{|V_{j-\ell,j}|}{|V_{j,j}|}
\le(d_0a_L)^\ell2^{\ell-1}
\binom{j+\ell-1}{\ell}=O_L(D^L).}\tag{2.1}$$
$j=\ell$ 时行零的系数为零，也满足相同上界。这里固定的是 $L$；没有给出随 $L$ 增长时的免费统一常数。

## 3. 稳定级数没有共同正解析半径

令 $\ell_i=2^i-1$。在 $\mathsf N$ 模型的稳定 $g$ 级数中，
$$[z^{\ell_i}]g=d_0a_i/d_i=:b_i.$$
于是
$$\log b_i^{1/\ell_i}
=\frac{\Lambda_i-20-2\log(i+1)}{2^i-1}
\sim100\,8^i\longrightarrow\infty.$$
故稳定形式级数的收敛半径为零。

对 $\mathsf Y$ 模型，相同次数的准确稳定系数为
$$d_0\left\{\frac{a_i}{d_i}
-\sum_{k<i}a_kd_k^{-2^{i-k}}\right\}.\tag{3.1}$$
负号来自 $2^{i-k}$ 为偶数，不能忽略。令
$$r_i=\Lambda_i/2^i=100\,8^i-105\,4^i+150i+25.$$
此序列严格递增，故旧项之和至多
$2\exp(2\Lambda_{i-1})$。又
$$\Lambda_i-2\Lambda_{i-1}
=\frac{175}{2}16^i-\frac{315}{4}8^i+150\,2^i
\ge770\,16^{i-1}\quad(i\ge1).$$
旧项相对于新主项的比例不超过
$$2(i+1)^2\exp(-770\,16^{i-1})<1/2.$$
所以 (3.1) 介于 $b_i/2$ 与 $b_i$ 之间，同样有无界的 $\ell_i$ 次方根，稳定级数半径为零。

有限 $\mathsf Y$ 头的最近极点模为
$$d_{m-1}^{1/2^{m-1}}=e^{-r_{m-1}}\longrightarrow0.$$
不同层的极点模不同，所以该最近极点不会被别的有理项抵消。有限 $\mathsf N$ 头虽是多项式，但稳定系数的无界根说明它们不可能在同一个正半径圆上有统一界。

以上区分有限真实解析芽与无限形式级数；只对有限芽使用下节的 Cauchy 估计。

## 4. 固定物理行的真实四次费用

令 $i=m-1\ge3$，记
$$D=2^{i+1},\qquad j=D-1,\qquad L=2^i-1,\qquad b=b_i.$$
这里 $L$ 随头长增长，与 §2 的固定带宽不同。令
$$g_< =d_0F_i/z.$$
两个实际模型都满足
$$g_m=g_<+bz^L\pmod {z^{2L+1}}.\tag{4.1}$$
$\mathsf Y$ 新项的第二个 Taylor 次数为 $2^{i+1}-1=2L+1$，因此不会影响所需的 $2L$ 次系数。

所引 Jordan 稿 §2 已支付真实有限圆盘
$$\rho_i=e^{-110\,8^{i-1}},\qquad
|g_<-1|<d_0\quad(|z|\le\rho_i).$$
于是对所有 $r,s\ge0$，
$$|[z^r]g_<^{-s}|\le\rho_i^{-r}(1-d_0)^{-s}.\tag{4.2}$$
由 (4.1) 的精确有限次数展开，
$$\boxed{[z^{2L}]g_m^{-j}
=\binom{j+1}{2}b^2-jb[z^L]g_<^{-j-1}
+[z^{2L}]g_<^{-j}.}\tag{4.3}$$
定义
$$\zeta_i=\rho_i^{-L}b^{-1}(1-d_0)^{-j-1}.$$
代入所有原常数，恰得
$$\begin{aligned}
\log\zeta_i={}&-\frac{345}{4}16^i+\frac{365}{4}8^i
-(150i+25)2^i+20+2\log(i+1)\\
&+2^{i+1}[-\log(1-d_0)]
\le-74\,16^i\qquad(i\ge3).
\end{aligned}\tag{4.4}$$
为核最后一步，可用 $8^i\le16^i/8$、$-\log(1-d_0)<1$ 和
$20+2\log(i+1)+2^{i+1}\le16^i/4$；被省去的另一项为负。

由 (4.2)，(4.3) 的两项相对误差至多
$$\frac{2\zeta_i}{j+1}+\frac{2\zeta_i^2}{j(j+1)}
\le\zeta_i\qquad(j\ge15).$$
结合 (1.2)、$W_j=\prod_{k\le i}d_k$、$W_1=d_0$，得到真实物理行 $n=1$ 的准确渐近式
$$\boxed{\frac{V_{1,D-1}}{V_{D-1,D-1}}
=2^i d_0a_i^2\,\frac{\prod_{k<i}d_k}{d_i}
(1+\varepsilon_i),\qquad
|\varepsilon_i|\le e^{-74\,16^i}.}\tag{4.5}$$
特别它对充分大的每个实际头均为正，且没有依赖形式级数的解析性。

对原 $\Lambda_i$ 求有限几何和及其导数，
$$\Lambda_i-\sum_{k<i}\Lambda_k
=\frac{280}{3}16^i-90\,8^i+300\,2^i-\frac{850}{3}.$$
因此 (4.5) 等价于
$$\boxed{\begin{aligned}
\log\left|\frac{V_{1,D-1}}{V_{D-1,D-1}}\right|
={}&\frac{35}{6}D^4-\frac{45}{4}D^3+150D-\frac{910}{3}\\
&+i\log2-4\log(i+1)+\log(1+\varepsilon_i).
\end{aligned}}\tag{4.6}$$
这给出实际单个固定行、按实际本列对角元归一后的四次指数增长；不是一般相似条件数上界留下的可能损失。

## 5. 对原边界研究的意义与未付项

§2 的固定带估计可以用于只损失有限个头次数的真实项，并且保留原权比 $W_j/W_{j-\ell}$。§4 则说明当损失随 $D$ 增长时，即使目标是固定低物理行，也不能把本列归一矩阵统一估成 $\exp(O(D\log D))$，更不能借一个并不存在的共同正解析半径得到这种结论。

[首物理头的实际商 Gram](R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)和[Boolean 两带、商边界及 $\Gamma$ 收缩](R239-appendix-boolean-two-band-quotient-commutator-boundaries-and-gram-contraction.md)仍保留完整共同源及 Schur 条件。本文的单列费用没有否定这些条件造成的抵消，也没有证明原自由坐标在坏列方向可任意实现。

继续需要支付的是实际 $\Gamma$ Schur 中的低侧反馈、第二下降跨 birth 桥以及原三种 Gram 的同源费用。不能把真实最高层加权能量趋零乘上 (4.6) 的增长常数后宣布低侧反馈趋零。
