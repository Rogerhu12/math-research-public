# 用两个真实 Airy 根值收紧已算出的完整无穷源

[GIC 公开作业 46144088993/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46144088993) 在原 $n\ge4194308$ 得完整 $L^2(dr;H^{-5/3})$ 数 $.09184711485636493$、原参考系数到腰 $.5259830156066113$、公共物理范数 $6.52218939352198$、ASQ16 高行 $.5354448409890977$ 为其输出的向上端点。原四个径向格、频率圆盘、每格 $m(w)$、矩阵文字 $K$ 与其导数的范数保持各自的原已付界。对同一整个无穷频率源，以下给更小上界
\[
 D<.0661300,\qquad D_{\rm nat}<.378708,\qquad
 C_{97,\mathrm{local},\infty}<4.6960,\qquad
 C_{\rm ASQ16,local,\infty}<.38553 .                           \tag{GIV.1}
\]
原完整小记录 1774 bytes，SHA256
\(\mathtt{d4be3220759ccfffa9dbe8f4d44d9dc51d74ebfbb18fb053884897b3b288fdd3}\)。
结论只覆盖同一根到截面的完整局部三项与以上自然频率。

沿 [GAF 两物理分支](R149-supplement-all-frequency-two-ray-physical-bound-for-both-genuine-Airy-rows.md) 记 $m=\operatorname{Ai}(-s)^2+\operatorname{Bi}(-s)^2$，$m_1$ 为两导数的平方和。正 Laplace 表示给 $m(s)\le m(0)$ 及 $0\le m''(s)\le m''(0)$。真实 Airy 方程给 $m_1(s)=sm(s)+m''(s)/2$，所以 $m''(0)/2=m_1(0)$。原两行在实负 $T$ 的解调幅遂满足
\[
 \sqrt{m(s)}<18/25,\qquad
 n^{-1/3}\sqrt{m_1(n^{2/3}u)}
 <(18/25)\sqrt{u+N^{-2/3}},\qquad u=-T,\ n\ge N.
\]
这里使用原根初值
\[
 m(0)=4/[3^{4/3}\Gamma(2/3)^2],\qquad
 m_1(0)=4/[3^{2/3}\Gamma(1/3)^2].
\]
为直接证明两个均小于 $(18/25)^2$，在 $[0,1]$ 把 $e^{-t}$ 用五次交错下多项式积分。在 $[1,\infty)$，条件指数分布的均值为 $2$，凸函数 $t^{-1/3}$ 用 Jensen。故
\[
 \Gamma(2/3)\ge 3/2-3/5+3/16-1/22+1/112-1/680+e^{-1}2^{-1/3}>107/80.
\]
最后不等式用 $2^{-1/3}>79/100$ 和 $e<68/25$；后者由指数级数前六项和后尾 $7/(6\cdot6!)$ 得到。$3^{1/3}>36/25$，且 $(18/25)^2(108/25)(107/80)^2>4$。另一初值用 $\Gamma(1/3)>\int_0^1t^{-2/3}(1-t)dt=9/4$、$3^{2/3}>2$ 即得。[AHD 中的原初值和 Laplace 表示](R149-supplement-full-Airy-matrix-correlation-and-integrated-Darboux-source.md)

这两个改进同时适用于 $s=0$ 和整个真实两分支。GAF 对解调幅导数的相对费 $1/2$、$5/8$ 仍直接乘各自已收紧的幅；真实 $Z_n$ 的幅和总变差两项也乘该公共因子。故 [GIC.1](R149-supplement-infinite-true-profile-tail-of-the-complete-genuine-collar-source.md) 的 $P_*$ 可整体乘 $18/25$，原加权导数行费仍为高度行的 $1/128$。插值两端都恰含一个 $P_*$，故 GIC.3 四个格的原正上界各乘 $18/25$，其逐格平方、径向求和开根也只乘一次。原物理腰读和 ASQ16 右因子为随后线性乘法，得到 (GIV.1)。这里是对原公式正上界的同一因子改进，未从未知算子之差作减法，亦未新算旧频率格。
