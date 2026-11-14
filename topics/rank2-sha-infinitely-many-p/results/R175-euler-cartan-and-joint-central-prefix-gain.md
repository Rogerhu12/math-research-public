# R175. 整 Euler 行及原双中央条件的真实饱和收益

日期：2026-11-12。**已证明；全阶严格预算仍未完成。**

在 R174 的同一整 Cartan 坐标中，
$$
 EU=1+O((U,V)^{p-1}),\qquad EV=O((U,V)^{p-1}),
$$
首个两项准确为
$U^{p-1}/(p-1)!$、$U^{p-2}V/(p-2)!$。
所以齐次度 $d$ 的原源满足
$$
 L_{h,j}=d^hL_{0,j}/h!\qquad(h+j\le p-1).
$$
这给全部混合列共同的有限精度 Hermite 谱行，
并保留每个高 $q$ 项的实际总次数条件。
第二带的完整轴比较进一步给全部 $h<p$ 的共同模 $p^2$ 行；
$h=p-1$ 的两个首 carry 及整常数
$\kappa_p=u_0-[w^{r+1}]b(w)$ 均明确保留。

完整轴比较进一步给：对齐次且 mass 为零的 $H$，
存在同一个整径向参数 $\mathfrak a(U)-1=U+\cdots$ 及整单位
$\mathfrak b(U)$，使
$$
 \sum_{h\ge0}L_{h,j}(H)U^h
 =[w^j]H(\gamma(w))\,\mathfrak a(U)^d\mathfrak b(U)^{-j}
                     \qquad(1\le j\le r).
$$
这不再截断 $h$，且保留原第一类周期。

令 $r=(p+1)/4$、$\tau_p=pu_0\bmod p\ne0$。
对真实原源
$H\in\mathbb Z_p[A_2,B]_{\le D}$、$1\le D<p$，
若其实际前缀在 $rD$ 之前全零，则
$$
 \boxed{\quad
 p^{D-1}[w^{rD}]H(\gamma(w))
   \equiv(-17\tau_p)^{D-1}[w^r]H_1(\gamma(w))\pmod p.
 \quad}
$$
其中 $H_1$ 是原源的线性齐次部分。
因此两条实际中央系数
$[w^r]A_2=[w^r]B=0\bmod p$
使整个该饱和行的赋值从已付的 $-D+1$ 改善为至少 $-D+2$。
这确实使用原双中央条件，没有假设乘积列的中央值也为零。

同一前缀加双零条件还杀掉全部原齐次分量的第一中央矩，
从而后续 $rh<pr$ 的 $j=0$ 行满足
$\Lambda_{h,0}\in p^2\mathbb Z_p$。
中央条件准确使此矩消去提前一个 normal step；
它尚不构成 R159 所需的全部 $k,D,p$ 严格预算。

[完整证明](../notes/2026-11-12-euler-cartan-rows-and-joint-central-prefix-gain.md)。
[独立准确前缀脚本](../scripts/check-euler-cartan-central-prefix-gain.py)
只用原有理列和整列消元核对有限校准，不用 Cartan 公式生成数据。

[真实二维平均与第二带端点校准](../scripts/check-euler-cartan-second-band.py)
在 $p=7$ 对 $A_2,B,A_2^2$ 共核 135 项。
