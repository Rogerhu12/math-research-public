# R119：同一完整径向网络的公共参数与有限阶多项式逆

2026-11-14，visible-exact-astra-ac0d。

**状态：已证明。** 本篇把[实际尺度的完整正定散射导数](R119-supplement-scale-correct-polynomial-middle-scattering-generator.md)直接接到[真实完整酉网络](R119-supplement-complete-radial-unitary-network-and-global-eigenphase.md)。存在原 fixed-stop 允许族中的一组公共参数，使每个实际保留频率同时满足

\[
 \boxed{\quad
 \|(I-U_M)^{-1}\|_{\ell^2\to\ell^2}
   \le 2^{2200007}d_M M^{30699}
   <2^{2200007}M^{30700}.
 \quad}                                                     \tag{P.1}
\]

这里的单位是原网络的全部 canonical incoming 端口。真实 high 前缀、无限 low 余尾、所有正段交叉及仿射源均已准确消元到该网络；不是把这些方程删掉。此结论把该网络的逆费用降为固定有限阶数，并保同一角解析宽度。原逐层标签源到端口、全物理重建、非径向混模和最终非线性方程还不能由 (P.1) 自动获得。

## 1. 同一允许族中的一次选择

沿用[带权公共选择](R119-supplement-weighted-spectral-selection-one-common-radial-profile.md)的原记号

\[
 \delta_j=(2/25)2^{-j},\quad J=j+5,\quad
 A_j=2^{-40}\delta_j^{-1/8},\quad
 T_j=2^{65536}J^{204}\delta_j^{-320},
\]
\[
 \mathcal I_M=\{j\ge8193:A_j\le M\le T_j\},\qquad
 n_M=|\mathcal I_M|,\quad d_M=2n_M,
 \quad M\in4\mathbb N, M\ge M_*:=A_{8193}.
                                                               \tag{P.2}
\]

原证明给 \(M_*>2^{984}\)、\(n_M<8\log_2M+321\)。每个 \(\mathcal I_M\) 非空且有限；每层实际保留的频率也有限。两端真实允许线可以竖直，反射的定义没有坐标极点。

在每层、每个原 dyadic band 中，现取尺度正确定理 (S.27)--(S.35) 的实际方向、完整半径和频率数：

\[
 \Xi_j=\sum_n\frac{r_{j,n}}{N_{j,n}}
       \sum_{M\text{ in band }n}\theta_M\psi_{j,M},
 \qquad -1\le\theta_M\le1.                              \tag{P.3}
\]

只对真正保留的四倍频率求和。同一个 \(\theta_M\) 同时作用于其所有 \(j\in\mathcal I_M\)。方向已按原 quartic 和实际频率固定；以后不随未知全局共振态调整。原两个补偿 bump 精确保两 phase，完整 \(C^4\) 总量仍小于 \(2^{-79}\)。固定接线、原 \(h_j,\zeta_j,b_M,\mathsf K\) 及标签定义均不变。

本篇在原允许族内部加强公共参数的存在选择，并未声称某个此前任意选定的数值参数点自动满足新间隙。下面同时保留以前的带权网络结论和原 good-\(t\) 条件。依赖具体参数点、而没有在整个允许族统一证明的其它证书，仍须在最终所选点验证。

## 2. 完整二维不等式直接组装

准确消元给

\[
 U_M=P_M\bigoplus_{j\in\mathcal I_M}S_{j,M},\qquad
 (I-U_M)x_M=g_M.                                      \tag{P.4}
\]

固定其它所有坐标及外 bump 参数 \(t\) 时，\(\theta_M\) 只改变 retained negative windows。两端线、正段、端口单位及其 normal shear 对这个坐标固定，所以 \(\partial_{\theta_M}P_M=0\)。故准确有

\[
 -iU_M^*\partial_{\theta_M}U_M
   =\bigoplus_{j\in\mathcal I_M}
         (-iS_{j,M}^*\partial_{\theta_M}S_{j,M})
   \ge D_M,                                           \tag{P.5}
\]
\[
 D_M=\operatorname{diag}_{j\in\mathcal I_M}(D_{j,M}I_2),
 \quad D_{j,M}>a_M^0:=2^{-2200000}M^{-30697}.
                                                               \tag{P.6}
\]

整个参数盒上的下界已包括方向幅度 \(r/N\)、全部 band 的同时变化和两补偿 bump 的 Hessian。原完整散射定理 (P.21)--(P.24) 同时给

\[
 \|-iU_M^*\partial_{\theta_M}U_M\|<2^{-33}<1/8.       \tag{P.7}
\]

这里直接使用完整 complex incoming 空间上的正定矩阵。没有再选一个 rank-one 共振向量，也没有再支付从该向量到两端口的 \(K_j^3\) 因子。

## 3. 谱平均保留一个明确的无权间隙

令 \(a_M=\min_jD_{j,M}>a_M^0\)，并取

\[
 \varepsilon_M=(128d_MM^2)^{-1},\qquad
 \xi_M=a_M\varepsilon_M,\qquad
 L_M=1+\log(512d_MM^2/a_M),\quad
 \mathcal T_M=128d_MM^2L_M.                            \tag{P.8}
\]

[已证谱平均引理](R119-supplement-weighted-spectral-selection-one-common-radial-profile.md)的 (W.6)--(W.10) 适用于整个真实酉路径。其好集同时满足

\[
 \operatorname{dist}(1,\sigma(U_M))\ge\xi_M,
 \qquad
 \|D_M^{1/2}(I-U_M)^{-1}D_M^{1/2}\|\le\mathcal T_M,
                                                               \tag{P.9}
\]

条件坏集概率小于 \(1/(32M^2)\)。特别地，间隙条件并没有在取得带权估计后丢弃。

为明确其量词：每条连续展开的 eigenphase 几乎处处满足
\(a_M\le\phi'_k\le1/8\)。穿越区间内总变化小于 \(1/4\)，所以一条分支只能遇到一个 \(2\pi\) 近邻弧。坏弧的参数长度至多 \(4\xi_M/a_M\)；重根的一阶分裂由相应 eigenspace 上的同一正定 generator 控制。这里不对单个 eigenphase 求需要其它谱间距的二阶导数。

酉矩阵正规性及 (P.8)--(P.9) 直接给

\[
 \|(I-U_M)^{-1}\|\le\xi_M^{-1}
    <128d_MM^2(a_M^0)^{-1}
    =2^{2200007}d_MM^{30699}.                         \tag{P.10}
\]

最后 \(d_M<M\) 是全范围的真实数值不等式。写
\(x=\log_2M\ge984\)、\(x=984+q+r\)、\(q\in\mathbb N\)、\(0\le r<1\)，则

\[
 d_M<16x+642\le16402+16q
     \le16402\,2^q<2^{15+q}<2^{984+q}\le M.          \tag{P.11}
\]

这证明 (P.1)，没有用“层数是对数”略掉实际有限常数。

## 4. 一组参数同时满足全部频率和原固定接线条件

对 \(t\in[0,1]\) 和全部 \(\theta_M\in[-1,1]\) 取产品概率。条件固定其它参数时 (P.5)--(P.9) 统一成立，故 Fubini 和真实可数频率求和给

\[
 \mathbb P(\text{至少一个 middle 频率失败})
 <\sum_{M\in4\mathbb N}\frac1{32M^2}<\frac1{256}.  \tag{P.12}
\]

这里 \(\sum_{k\ge1}k^{-2}<2\)，已足够得到严格上界，不需要特殊函数数值。对每个真实 \(\Xi\)，原 fixed-stop 定理还给新允许线的闭 good-\(t\) fibre，测度至少 \(1-83/16384\)。再次 Fubini 得联合好集测度大于

\[
 1-\frac1{256}-\frac{83}{16384}
       =1-\frac{147}{16384}>0.                       \tag{P.13}
\]

因而确有同一个完整径向 profile 及同一个 \(t\)，使 (P.1)、(P.9) 与原固定接线条件同时成立。原产品连续性、端线 reflection 和闭间隙条件给非空紧好集；若要单值指定，可沿 \(t,\theta_{M_1},\theta_{M_2},\ldots\) 逐个取该紧集的最小坐标。这是准确存在指定，不是已经算出无限参数数组的声明。

## 5. 原逐窗口角宽结论也保留

这不是以无权多项式估计换掉原局部权。对 active \(j\)，从 \(M\le T_j\)、\(\log2<1\)、\(\log(25/2)<3\)、\(\log J<J\) 得

\[
 \log M<66496+524J<1024J.                            \tag{P.14}
\]

由 (P.6) 及 \(J\ge8198\)，

\[
 -\log D_{j,M}<2200000+30697\cdot1024J<2^{25}J.    \tag{P.15}
\]

另一方面原 \(M\ge A_j\)、\(h_j=8\delta_j^{1/256}\) 给

\[
 2^{-800}Mh_j>2^{31j/256-837}.                       \tag{P.16}
\]

写 \(j=8193+512q+r\)、\(0\le r\le511\)。则
\(J\le8709+512q\le8709\,2^q<2^{14+q}\)，而
\(31\cdot8193/256-837>155\)。因此 (P.16) 大于
\(2^{155+62q}>2^{39+q}>2^{25}J\)，所以

\[
                  D_{j,M}>e^{-2^{-800}Mh_j}.         \tag{P.17}
\]

同一范围中，令 \(x=\log_2M=984+q+r\)，有
\(2200000+30697x\le(2200000+985\cdot30697)2^q<2^{25+q}\)，故 \(-\log a_M<M/4\)。又由 \(d_M<M\) 得

\[
 L_M<1+\log512+3\log M+M/4<2M,
 \qquad \mathcal T_M<256M^4.                         \tag{P.18}
\]

末个对数比较可用 \(\log M\le M/8\)（在1024成立且以后改进）。于是
\(\log\mathcal T_M<8+4096J<2^{13}J<2^{-803}Mh_j\)，最后一步用同一 (P.16) 再除8。定义原局部端口权

\[
 W_M=\operatorname{diag}_{j\in\mathcal I_M}
                           (e^{2^{-800}Mh_j}I_2).
\]

由于 \(1+1/8<2\)，上述两项指数费用给
\(W_M^2\ge\mathcal T_MD_M^{-1}\)。故同一个参数选择还满足

\[
             \|W_M^{-1}(I-U_M)^{-1}W_M^{-1}\|\le1.   \tag{P.19}
\]

全部原局部角宽仍在，未重新归一原标签或径向源权。

## 6. 同角宽、有限阶端口映射及明确的物理缺口

在上述完整 canonical 端口上定义

\[
 \|v\|_{\sigma,s}^{\rm port}
   =\sum_{M\in4\mathbb N,\,M\ge M_*}
       e^{\sigma M}M^s\|v_M\|_{\ell^2(\mathbb C^{d_M})}.
                                                               \tag{P.20}
\]

对任何右端 \(g\)，只要右侧有限，完整网络解唯一且

\[
 \boxed{\quad
 \|x\|_{\sigma,s}^{\rm port}
       \le2^{2200007}\|g\|_{\sigma,s+30700}^{\rm port}.
 \quad}                                                     \tag{P.21}
\]

负频率由真实方程的共轭同时处理，不另选度量；若把双号都写进范数，两侧同加相应项。这个定理是固定阶数的端口映射，\(\sigma\) 完全不变。它并非原 \(\mathcal X_\beta\) 空间的同阶有界逆。

原中性层已有 \(N_M<C_\zeta e^{-\tau_\infty M}M^{-30960}\)。与 (P.1) 比较，确切剩余次数为 \(30960-30700=260\)，而常数 \(2^{2200007}C_\zeta\) 必须保留。这一比较只能用于**确实已经**转成该 \(N_M\) 单位的完整端口列；不能把任意物理源或一条标签取值泛函直接冒作这种列。

具体而言，\(g_M=P_Mt_M+p_M\) 继续保所有 negative ordinary/weak 两态源、正段双端 affine、high 前缀和无限 low 余尾的源。total flux 与 bare flux 的端荷、材料密度、frame Jacobian 和 normal shear 均须在 source-to-port 及重建时支付。零模仍有其独立高度、完整通量与电阻积分；\(M<M_*\) 的巨大有限频段不在本篇定量结论中。

本篇没有证明非径向背景下同一参数 generator 对所有混频簇正定，也没有把绝对小扰动除以这个多项式间隙。最终全物理 Green、同对象全频补逆和非线性闭合继续保留在 open 中。

## 7. 可复现的精确有限预算

[有理预算源码](../scripts/fourfold_common_radial_polynomial_resolvent.py)核实上面实际使用的全部有限常数、维数块、概率余量、层号指数及规范次数，并绑定四篇输入证明的 SHA256。[原生运行记录](../notes/2026-11-14-R119-common-radial-polynomial-resolvent-rational.json)保存实际执行结果。无限维的量词、谱平均、产品选择和源单位来自正文完整证明，不以有限频率采样代替。
