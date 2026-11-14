# R138. 非 CM 普通、非异常大素因子的无条件选择

日期：2026-11-12。状态：**已证明；实际二次增广非零未证明。**

完整证明见
[非 CM 大素因子的例外删除](../notes/2026-11-12-noncm-large-factor-exception-deletion.md)。

若一个坏素数集合满足
\[
 A(y)\ll y(\log\log y)^2/(\log y)^2,
\]
则对每个固定 \(0<\theta<1\)，
\[
 \#\{\ell\le x:\ell\text{ 素},\
   \exists p\text{ 坏},\ p>x^\theta,\ p\mid\ell+1\}
 \ll_\theta x(\log\log x)^2/(\log x)^{3/2}
 =o(x/\log x).
\]
证明在 \(p=xe^{-\sqrt{\log x}}\) 分段：下段保留
Brun–Titchmarsh 的 \(\log(x/p)\)，上段对整数余因子
\(u\le2e^{\sqrt{\log x}}\) 求和。两段均付准确上界。

Thorner–Zaman（IMRN 2018）Theorem 1.4 给任意固定非 CM
椭圆曲线的坏集合 \(a_p\in\{0,\pm1\}\) 上述计数。
因此 R126 的固定进程 \(\ell\equiv-1\pmod B\) 中，仍有
\(\gg_B x/\log x\) 个 \(\ell\) 同时满足
\[
 \begin{gathered}
 p=P^+(\ell+1)>x^{667/1000},\quad
 a_p\not\equiv0,\pm1\pmod p,\quad a_\ell\not\equiv0\pmod p,\\
 v_p(\ell+1)=1,\qquad
 u=(\ell+1)/p\ll p^{333/667},\qquad u^2=o(p).
 \end{gathered}
\]
这里删去 \(a_\ell=0\) 也只需同一固定迹对数界，没有把
\(a_p=\pm1\) 错用超奇异素数的特殊幂次界。

应用于 R136 的固定 E389 与 \(F=\mathbb Q(\sqrt{-7})\)，
令 \(7\mid B\)。则 \(\ell\) 惰性，环类群有唯一次数 \(p\) 商
\(L/F\)，且
\[
 \#E(\mathbb F_{\ell^2})\equiv-a_\ell^2\not\equiv0\pmod p,
 \qquad H^1(F_\ell,E[p])=0.
\]
实际完整 Heegner 迹的范数是 \(a_\ell P_1=O\)。
高层 \(Y_n\) 的范数却仍可能为 \(a_\ell P_n\ne0\)，所以
norm-one Euler 首项的额外 \(\delta\) 必须保留。

已得到无穷个 ordinary/nonanomalous 的实际大因子输入；
尚未由此证明其完整 \(Q\) 非挠、二次增广非零或主目标。
