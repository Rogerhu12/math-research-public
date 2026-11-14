# R212 — 负 Witt 行、Faber 正则尾与同一原源的完整前缀运输

日期：2026-11-12。**状态：下述 Grunsky 恒等式、负行读取、完整原源的整目标等价及归一行同余均已证明；不声称获得新的净范数收益。**

本篇继续 [R210](R210-full-first-band-faber-kernels-and-integral-witt-cost.md) 的负扭方向。它们不能无条件叫作“未来原行”；但在所需阶仍属于原已保留前缀时，确实给一个单位三角运输。更一般地，全部 Laurent 系数可共同作用于原多项式源 $E_D$，无需按齐次次数分别作 gauge。

## 1. 固定窗口与两种源版本

仍取原
$$
 E_0:y^2=x^3-x,\quad \omega=dz=\frac{dx}{2y},\quad
 s=x^{-2},\quad T=x^2=s^{-1},\quad w=z^4,
$$
以及
$$
 p=4r-1\ge7,\qquad R=\frac{p^2-1}{4},\qquad
 1\le n\le M\le R.
$$
设 $W(s)=sF(s)^4$ 为 R208/R210 的原严格换元。$W(s)$ 与其反函数
$s(w)$ 至所需第一带前缀均整。

本篇先允许任意 $g(w)\in\mathbf Q_p[[w]]$，定义其唯一有限代表
$$
 f_M(s)=[g(W(s))]_{\deg_s\le M}.
 \tag{1}
$$
于是
$$
 g_M(w):=f_M(s(w))\equiv g(w)\pmod{w^{M+1}}.
 \tag{2}
$$
这里不要求 $g$ 的原系数整。(1) 从 $w$ 系数到 $s$ 系数的有限矩阵是首对角为一的整下三角矩阵。

下面两种原 theta 源的应用均沿用 R199 的 $p\ne11$ 限制；纯几何 Faber 恒等式与任意形式级数的换元结论仍只要求 $p\ge7$。

应用有两种：

- 对 R210 的原两条 gauged 函数，$g=\widehat A,\widehat B$，其第一带系数已整且常数项为零。
- 对整个原源，取
  $g_{\mathcal P}(w)=\mathcal P(A(w),C(w))$，
  $\mathcal P\in E_D=\mathbf Z_p[A,C]_{\le D}$。
  此时保留全部原次数，允许常数列及原非整 Taylor 系数。第 6 节统一使用其真实归一行，不对不同齐次块另选 gauge。

R210 给
$$
 \mathcal H_n=-xy\,\mathcal D_n(T),\qquad
 \mathcal D_n\in\mathbf Z_p[T],\quad
 \deg\mathcal D_n=n-1,\quad \text{首系数}=1,
$$
以及
$$
 \mathcal H_n=z^{-4n-1}+O(z^3).
 \tag{3}
$$
置
$$
 \Omega=f_M(s)\mathcal H_n\omega
 =\pi_T^*\eta,\qquad
 \eta=-\frac14f_M(T^{-1})\mathcal D_n(T)dT.
 \tag{4}
$$
写
$$
 \eta=\sum_{h=1-M}^{n}\beta_hT^{h-1}dT.
 \tag{5}
$$
允许常数项后，最上面的指数是 $h=n$；若 $g(0)=0$，这一项为零。

## 2. 原 Faber 核的准确正则尾

写原 Weierstrass 函数
$$
 x(z)=z^{-2}+\sum_{t\ge1}a_tz^{4t-2}.
 \tag{6}
$$
以下恒等式在特征零中成立：
$$
 \boxed{\quad
 \mathcal H_n
 =-\frac1{(4n)!}\partial_z^{\,4n-1}x(z).
 \quad}
 \tag{7}
$$
证明：右边是只在原点有极点的奇椭圆函数，准确主部为
$z^{-4n-1}$；低于导数阶的正幂项被杀掉，其余项正则。
它与 (3) 的差是全局正则奇函数，故为零。

因此
$$
 \mathcal H_n
 =z^{-4n-1}-\sum_{m\ge1}\kappa_{n,m}z^{4m-1},
 \tag{8}
$$
其中
$$
 \kappa_{n,m}
 =a_{n+m}
   \frac{(4(n+m)-2)!}{(4m-1)!(4n)!}.
 \tag{9}
$$
若记
$$
 b_{n,m}
 =4a_{n+m}\frac{(4(n+m)-2)!}{(4m)!(4n)!},
$$
则
$$
 b_{n,m}=b_{m,n},\qquad \kappa_{n,m}=m\,b_{n,m}.
 \tag{10}
$$
这是所用的对称 Grunsky 系数规范；(8) 的负号和 (10) 的因子 $4$ 都已保留。

### 2.1. 需要的整性是 kappa，而不是 b

在所需范围中，
$$
 \boxed{\quad \kappa_{n,m}\in\mathbf Z_p
                  \qquad(n+m<R). \quad}
 \tag{11}
$$
不能从此把 $b_{n,m}$ 也宣布为整，尤其当 $p\mid m$ 时。

为证明 (11)，置 $U(w)=u(z)/z$。R202 的首坏阶给
$U\in1+w\mathbf Z_p[[w]]\pmod{w^R}$，且
$$
 x=z^{-2}U^{-2},\qquad
 y=-z^{-3}U^{-3}\sqrt{1-s(w)}.
$$
把这些式子代入 $\mathcal H_n=-xy\mathcal D_n(x^2)$，
得到 $z^{4n+1}\mathcal H_n$ 至 $w^{R-1}$ 的全部系数整。
而 (8) 给
$$
 z^{4n+1}\mathcal H_n
 =1-\sum_{m\ge1}\kappa_{n,m}w^{n+m},
$$
故得 (11)。这不要求把 (9) 中各阶乘的商逐个当成单位。

## 3. 负 Laurent 系数的原点公式

先设 $g(0)=0$。对整数 $k\ge1$，若
$$
 n+k\le M\le R,
 \tag{12}
$$
则准确有
$$
 \boxed{\quad
 \beta_{-k}
 =-\frac14[w^n]g(w)s(w)^{-k}
 +\frac14\sum_{m=1}^{k-1}
       \kappa_{n,m}[w^{-m}]g(w)s(w)^{-k}.
 \quad}
 \tag{13}
$$
这是特征零等式，保留任意精度；不是只在模 $p$ 下的读取。

证明：$T=x^2$ 在原点的分歧指数是 $4$，所以
$$
 -4\beta_{-k}
 =\operatorname{Res}_{O_E}g_M(w)s(w)^{-k}\mathcal H_n\,dz.
$$
将 (8) 代入。$g_M(w)s(w)^{-k}$ 最低阶为 $1-k$，
所以正则尾只有 $m\le k-1$ 可贡献留数。主项只读 $g_M$ 至
$w^{n+k}$，尾项只读至 $w^{k-m}\le w^{k-1}$。
条件 (12) 因而允许全部替成真实的 $g$，给出 (13)。
又因 $n+m\le n+k-1<R$，(11) 支付了每个实际尾系数的整性。

若 $g(0)\ne0$，负行仍可直接用 $g-g(0)$ 代替：
常数列在 (4) 中给一个 $T$ 的多项式微分，对所有 $\beta_{-k}$ 的贡献都为零。
这样避免把常数项引出的两个可能非整端点项分开读取。

由于 $s(w)^{-k}=w^{-k}(1+\cdots)$，(13) 特别给
$$
 \beta_{-k}
 =-\frac14\,g_{n+k}
       +\sum_{0\le i<n+k}c_{n,k,i}\,g_i,
 \qquad c_{n,k,i}\in\mathbf Z_p.
 \tag{14}
$$
主项其余系数只读 $g_{<n+k}$，尾最多只读 $g_{\le k-1}$。
所有参数系数的最高需要阶都小于 $R$，故 (14) 的整性也包括
$n+k=M=R$ 的合法端点。

若 $n+k>M$，(13) 不能继续把 $g_M$ 换成 $g$：
被截去的原系数可能已经贡献留数。这正是要保留的前缀边界。

## 4. 负 Witt 行的 Frobenius 形状

现在再设 $g$ 的有关原系数整，并取 $k=pq$。
写
$$
 \bar s(w)^{-q}=\sum_{\ell\ge-q}u_{q,\ell}w^\ell,
 \qquad u_{q,-q}=1.
$$
在特征 $p$ 中
$$
 \bar s(w)^{-pq}
 =\sum_{\ell\ge-q}u_{q,\ell}w^{p\ell}.
$$
所以 (13) 的主项为
$$
 -\frac14
 \sum_{\ell=-q}^{\lfloor(n-1)/p\rfloor}
       u_{q,\ell}\,\bar g_{n-p\ell}.
 \tag{15}
$$
其最高原行是 $g_{n+pq}$，系数为 $-1/4$；其后是
$g_{n+p(q-1)},\ldots$ 及同一余类的过去行。
正则尾准确为
$$
 \frac14\sum_{m=1}^{pq-1}\bar\kappa_{n,m}
       \sum_{\ell=-q}^{\lfloor(-m-1)/p\rfloor}
           u_{q,\ell}\,\bar g_{-m-p\ell}.
 \tag{16}
$$
它只读 $g_{\le pq-1}$。这必早于最高行 $n+pq$；
若 $pq>n$，则不应把这些行全部称为原来的第 $n$ 行以前。

式 (15)–(16) 只能在 $n+pq\le M$ 时读取真实原行。
同时，它们此处要求原 $g_i$ 整；不能先对任意含分母的
$\mathcal P(A,C)$ 逐项模 $p$。下一节用整目标矩阵支付整个原源的运输。

## 5. 全部 Laurent 系数就是同一完整前缀的整重表达

写
$$
 f_M(s)=\sum_{i=0}^Mf_i s^i,\qquad
 \mathcal D_n(T)=\sum_{a=0}^{n-1}d_aT^{n-1-a},\qquad d_0=1.
$$
直接从 (4) 得
$$
 \boxed{\quad
 \beta_{n-j}=-\frac14
       \sum_{\substack{0\le i\le M,\ 0\le a<n\\i+a=j}}
                   f_i d_a .
 \quad}
 \tag{17}
$$
因此对 $0\le j\le M$，
$$
 \beta_{n-j}=-\frac14f_j+\sum_{i<j}\lambda_{j,i}f_i,
 \qquad\lambda_{j,i}\in\mathbf Z_p.
 \tag{18}
$$
而 $f_0,\ldots,f_M$ 与 $g_0,\ldots,g_M$ 之间也是单位下三角整换元。
所以
$$
 (\beta_n,\beta_{n-1},\ldots,\beta_{n-M})
 \quad\text{与}\quad
 (g_0,g_1,\ldots,g_M)
 \tag{19}
$$
之间是同一个 $GL_{M+1}(\mathbf Z_p)$ 目标变换，对角为 $-1/4$。
它不依赖于 $g$，且每一个截到第 $j$ 行的变换仍是单位下三角。

剩余的 $n-1$ 条 Laurent 边界行对应
$j=M+1,\ldots,M+n-1$。由 (17)，它们都是原已保留
$g_0,\ldots,g_M$ 的整线性组合。
它们并不是原完整函数的第 $M+1,\ldots,M+n-1$ 行；
添加这些行不会增加当前前缀的信息。

## 6. 同一个原 E_D 和同一个真实归一 J

本节及第 7 节沿用 R199 的 $p\ne11$ 假设。现在对所有原 $\mathcal P\in E_D$ 同时取
$$
 g_{\mathcal P}(w)=\mathcal P(A(w),C(w)).
$$
不对 $\mathcal P$ 的不同齐次部分分别作 gauge。
令
$$
 h_j=\lfloor j/r\rfloor,\qquad
 J_j(\mathcal P)=p^{h_j}[w^j]g_{\mathcal P}(w),
 \quad 0\le j\le M,
$$
并对所选 Laurent 行使用完全相同的归一：
$$
 B_j(\mathcal P)=p^{h_j}\beta_{n-j}(\mathcal P).
 \tag{20}
$$
R199 保证这些 $J_j$ 在原整源上整。(18) 及严格换元共同给
$$
 B_j=-\frac14J_j+
      \sum_{i<j}p^{h_j-h_i}a_{j,i}J_i,
 \qquad a_{j,i}\in\mathbf Z_p.
$$
由于 $h_j\ge h_i$，准确有
$$
 \boxed{\quad
 B_{0,\ldots,M}=\mathsf T_{n,M}J_{0,\ldots,M},
 \qquad\mathsf T_{n,M}\in GL_{M+1}(\mathbf Z_p).
 \quad}
 \tag{21}
$$
这是对全部原源的同一个目标矩阵，不是不同齐次块各自的等价。

因此 (21) 同时保留：

- 每个真实连续前缀的源核及消失旗标；
- 任意 $p^N$ 精度下的原像格；
- 实际有限像、全部非零 Smith 指数及其长度；
- 对同一原源范数定义的逐行真实值理想。

剩余 Laurent 边界行可统一乘 $p^{h_M}$；由 (17)，它们也都是
原 $J_0,\ldots,J_M$ 的整组合。加入它们后，整个目标矩阵准确整等价于
$$
 \begin{pmatrix}J_{0,\ldots,M}\\0_{n-1}\end{pmatrix}.
 \tag{22}
$$
若给这些冗余行使用更大的 $p^{\lfloor j/r\rfloor}$，结论仍成立；
但那些编号不是原真实前缀的继续，不借此延长第一带范围。

(1) 的像虽然用次数 $M$ 的有理多项式表示，源始终是同一个 $E_D$。
不能把它扩大成所有次数 $M$ 的独立多项式，也不能删去原 theta 次数或原列的关系。

## 7. 归一负 Witt 行与原 J 的一层精度

对
$$
 k=pq\ge p,\qquad n\ge r,\qquad j=n+pq\le M
$$
还有一个在整个原源上成立的整行关系：
$$
 \boxed{\quad
 B_j+\frac14J_j
 \in p\,\langle J_0,\ldots,J_{j-1}\rangle_{\mathbf Z_p}.
 \quad}
 \tag{23}
$$
它不要求 raw 系数 $g_i$ 整。

证明时先减去常数列；负 Laurent 行与 $J_j$ 均不受影响。
写
$$
 s(w)^{-pq}=w^{-pq}V(w)^{-pq},\qquad V(w)=s(w)/w.
$$
所需 $V$ 系数均整。模 $p$，$V^{-pq}=(V^{-q})^p$：
若一个非首系数的次数 $\nu$ 不被 $p$ 整除，它本身就在 $pO$；
若 $\nu>0$ 被 $p$ 整除，则 $\nu\ge p>r$，归一化额外给
$p^{h_j-h_{j-\nu}}\in pO$。
所以 (13) 主项的所有非首行贡献，在归一后都属于右边的行模。

尾项最多读 $g_{pq-1}$。其与第 $j$ 行的距离至少 $n+1>r$，
故相应的归一幂差同样至少为一；(11) 保证没有隐藏的尾分母。
得到 (23)。此论证是在整系数目标矩阵上进行，没有对 raw 非整源作非法约化。

特别地，若所有较早真实行属于 $p^N$，则
$$
 B_j(\mathcal P)+\frac14J_j(\mathcal P)\in p^{N+1}.
 \tag{24}
$$
这支付了负 Witt 行在已观测窗口内的实际精度；它仍是同一原行的运输，不是额外独立约束。

## 8. 与 Cartier/原非零问题的边界

正 Witt 行在 R210 §5.3 已落实为真实过去行；本篇把范围内的负 Witt 行
落实为真实未来行及准确正则尾。选取的未来行必须仍在同一个保留的
$M$ 前缀内。最末 $n-1$ 条 Laurent 行始终是有限代表的冗余边界，
不能假称提供尚未读取的真实高行。

对原两条整 gauged 函数，可以直接使用 (15)–(16) 的模 $p$ Frobenius 形式。
对整个原多项式源，统一有效的是 (21)、(23) 的归一矩阵形式。
行归一是一个明确的系数算子，并不是原全局微分乘上一个共同标量；
若之后施加 Cartier、求原函数或拿 R207 的有理迹作比较，仍须保留这一区别。

本篇没有产生新的范数收益，因为 (21) 本来就是整单位目标变换。
它支付的是原源、原全部前缀、整目标格及未截断正则尾的比较，
使后续不能把正负扭项重复当成独立的中央信息。
原完整中央导数的跨素数非零和严格净预算依然未证。

依赖：[R208](R208-original-theta-single-pole-faber-and-integral-log-comparison.md)、
[R210](R210-full-first-band-faber-kernels-and-integral-witt-cost.md)、
原第一带矩阵 [R199](R199-exact-first-band-exponential-and-complete-divided-image.md)。

