# R119 续篇：同一径向 middle 逆的全频次指数界与可求和角宽

2026-11-14，visible-exact-astra-ac0d。

**状态：已证明。** 在[公共径向谱选择](R119-supplement-weighted-spectral-selection-one-common-radial-profile.md)
实际选出的同一个无限 profile 和同一个外参数 \(t\) 上，完整
middle 网络的物理散射逆满足
\[
 \|(I-U_M)^{-1}\|_2
 <\exp\!\left(2^{-795}M^{1-1/163840}\right),
 \qquad M\in4\mathbb N,\ M\ge M_* .                  \tag{B.1}
\]
这是该已付完整端口空间的界，不改变原两迹、源、mean 或标签权。
它给出任意固定角宽损失的连续线性逆，以及显式可求和的
频率截断角宽费用。本文没有据此宣称更新后的非径向逆、
任意原物理源到这些端口的提升、或非线性收敛已经完成。

## 1. 同一完整网络及原窗口

记
\[
 \delta_j=\frac2{25}2^{-j},\quad J=j+5,\quad
 h_j=8\delta_j^{1/256},
\]
\[
 A_j=2^{-40}\delta_j^{-1/8},\qquad
 T_j=2^{65536}J^{204}\delta_j^{-320},\qquad
 I_M=\{j\ge8193:A_j\le M\le T_j\}.                   \tag{B.2}
\]
全部 \(I_M\) 使用前篇已证明的同一个参数。
更浅的实际 high 前缀和真正无限 low 尾已准确消为允许线
及全部 affine 源；中间 positive cross 保留在 \(U_M\)。
本篇不重复选择 profile、不逐模改外端线，也不删掉任何一行。

前篇在这些真实归一物理端口上给
\[
 \|W_M^{-1}(I-U_M)^{-1}W_M^{-1}\|_2\le1,\qquad
 W_M=\operatorname{diag}_{j\in I_M}
                \left(e^{2^{-800}Mh_j}I_2\right).    \tag{B.3}
\]
维数为 \(2|I_M|\)。下述算子范数始终在同一完整有限维
Euclidean 端口空间，故乘两次 \(\|W_M\|_2\)
无需额外乘以维数或窗口数。

## 2. 实际 middle 的层宽随频率消失

置 \(x=\log_2 M\)。因 \(M\ge M_*=2^{984}25^{1/8}\)，
\(x>984\)。对每个 \(j\in I_M\)，\(A_j\le M\) 给
\[
                j<8x+320,\qquad J<8x+325<9x.        \tag{B.4}
\]
因此
\[
 \log_2(J^{204})<204(4+\log_2x)
                                      <4096+x/2.    \tag{B.5}
\]
最后一个不等式对整个 \(x\ge984\) 区间成立：
在984处，\(\log_2 984<10\)，
\(204(4+10)=2856<4096+984/2\)；
差函数的导数
\(204/(x\log2)-1/2<408/x-1/2<0\)。
这不是仅在有限层号上的抽查。

将
\[
                        J^{204}<2^{4096}M^{1/2}
\]
代入同一窗口的另一端 \(M\le T_j\)，准确得到
\[
 \delta_j^{320}
      \le 2^{65536}J^{204}/M
       <2^{69632}M^{-1/2}.                           \tag{B.6}
\]
取 \(1/(320\cdot256)\) 次方，且 \(69632<81920\)，给
\[
 \boxed{h_j<16 M^{-1/163840}\quad(j\in I_M).}         \tag{B.7}
\]
两个窗口端同时使用；没有把 \(M\le T_j\) 的方向倒置。

## 3. 完整物理 middle 逆与任意固定角宽

令
\[
       q=163840,\qquad \chi=1-\frac1q,\qquad c=2^{-795}.
\]
由 (B.3)、(B.7)，
\[
 \|W_M\|_2<\exp(2^{-796}M^\chi),
 \qquad
 \|(I-U_M)^{-1}\|_2
       \le\|W_M\|_2^2<\exp(cM^\chi).
\]
这就是 (B.1)。由于 \(0<\chi<1\)，它是真正次指数增长；
系数 \(c\)、指数 \(q\) 和频率范围均明定。

例如对这些完整端口向量定义
\[
 \|g\|_{\sigma,s}
   =\sum_{\substack{M\in4\mathbb N\\M\ge M_*}}
                      e^{\sigma M}M^s\|g_M\|_2 .
\]
对 \(0<\varepsilon<\sigma\)，完整径向解
\(x_M=(I-U_M)^{-1}g_M\) 满足
\[
 \|x\|_{\sigma-\varepsilon,s}
                  \le e^{K(\varepsilon)}\|g\|_{\sigma,s},
\]
其中可取明确常数
\[
 \boxed{
 K(\varepsilon)=\frac cq
       \left(\frac{c(q-1)}{q\varepsilon}\right)^{q-1}.
 }                                                   \tag{B.8}
\]
证明仅需最大化 \(cM^\chi-\varepsilon M\)：
其非负实轴上的极值点为
\(M=(c\chi/\varepsilon)^q\)，极值正是 (B.8)。
若极值不在当前离散频段，取全非负实轴的上界仍合法。
相同对角估计适用于相应的平方可和频率范数。
这里没有换成原逐层 \(\mathcal X_\beta\) 范数。

## 4. 完整高 middle 包络的可求和费用

置 \(B(N)=cN^\chi\)。对真实高 middle 频段，
\[
 \log\sup_{\substack{M_*\le M\le N\\M\in4\mathbb N}}
              \|(I-U_M)^{-1}\|_2\le B(N)
 \quad (N\ge M_*).                                  \tag{B.9}
\]
任取 \(N_0\ge M_*\)，则连续费用准确满足
\[
 \int_{N_0}^\infty\frac{B(N)}{N^2}\,dN
       =cqN_0^{-1/q}<2^{-777}.                       \tag{B.10}
\]
最后一步用 \(q<2^{18}\)；\(N_0^{-1/q}\) 没有被错误地
变成增长因子。

对二进制 cutoff \(N_n=2^nN_0\)，
\[
 \sum_{n=0}^\infty \frac{B(N_n)}{N_n}
   =\frac{cN_0^{-1/q}}{1-2^{-1/q}}<2^{-776}.          \tag{B.11}
\]
完整分母可以直接估计。令 \(a=\log2/q>1/(2q)\)，
指数级数给 \(e^a>1+a\)，于是
\(e^{-a}<1/(1+a)\)，进而
\[
 \frac1{1-2^{-1/q}}<1+\frac1a<2q+1<2^{19}.
\]
(B.11) 就保留了即使 \(q\) 很大也必须支付的整个几何和，
没有将每次任意小损失当作自动可求和。

## 5. 使用边界

本篇结论全部针对前篇实际选定的**径向完整 middle**。
它连同[原标签物理规范](R119-supplement-original-neutral-label-common-analytic-normalization.md)
给下一次接线提供两项准确输入：不同标签取值层具有同一指数宽度，
而完整 middle 谱分母的剩余对数增长是可求和的。

以下各项仍须在原方程中完成：

1. \(M<M_*\) 的完整低频段、另一 canonical 行和真正 mean/height；
2. ordinary/weak 物理源、prefix 与无限 low-tail affine 数据的
   完整提升费用，以及全部径向重建核；
3. 非径向更新的真实 principal 端图、混频簇和相同参数身份；
4. 包含这些输入及 nonlinear residual 的兼容迭代。

尤其，(B.10)--(B.11) 本身不是一个已实施的 Nash--Moser
或解析迭代，也不允许将径向谱隙与一个频率一致的绝对小扰动
直接作无限 Neumann 反演。完整非线性 \(\mathcal F=0\) 仍开放。

生产源：
\(\texttt{scripts/fourfold\_radial\_middle\_subexponential\_budget.mjs}\)。
实际有理报告：
\(\texttt{notes/2026-11-14-R119-radial-middle-subexponential-rational.json}\)。
全频单调性、实际窗口方向及无限和来自本文证明；原生报告只核
所列精确有理数和指数运算，不将有限测试当作全频谱证明。
