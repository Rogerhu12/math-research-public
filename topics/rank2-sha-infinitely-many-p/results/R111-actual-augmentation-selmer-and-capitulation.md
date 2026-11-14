# R111：实际增广 Selmer 类、strict 局部条件与 Sha 消失核

日期：2026-11-12。状态：已证明。

完整证明见
[研究笔记](../notes/2026-11-12-actual-augmentation-selmer-and-capitulation.md)。

## 命题

取 R103–R106 的 $E/F$ 与实际循环次数 $p$ 扩张 $L/F$，
其中 $F=\mathbb Q(\sqrt{-15})$。
写 $\Gamma=\langle\tau\rangle$、$N=\sum\tau^j$、
$\mathcal M=\ker(N:E(L)\to E(F))$、
$B=\mathcal M/(\tau-1)\mathcal M$。
R104 的单射 $\iota:B\hookrightarrow H^1(F,E[p])$ 将 $[Q]$
送到实际下降类 $c_Q$。

令 $B_{\mathrm{Sel}}=\iota^{-1}(\operatorname{Sel}_p(E/F))$。
则准确有
$$
0\longrightarrow\frac{NE(L)}{pE(F)}
\longrightarrow B_{\mathrm{Sel}}
\longrightarrow
\ker\bigl(\Sha(E/F)[p]\to\Sha(E/L)[p]\bigr)
\longrightarrow0.
$$
左箭头为 $NZ\mapsto[(\tau-1)Z]$，下降后为
$-\delta_p(NZ)$；右箭头为 R104 的负 inflation。
没有假设两边 Sha 有限。

对辅助位 $\lambda\mid\ell$，全部 $b\in B_{\mathrm{Sel}}$ 均满足
$$
\operatorname{loc}_{\lambda}\iota(b)=0.
$$
证明使用全分歧时
$\overline{DQ}=p(p-1)\bar Q/2=0$ 与形式群上的乘 $p$ 同构，
再用相同剩余群给出的有限局部条件限制单射。
该证明允许 $E(F_\lambda)[p]\ne0$，不在局部错误约去 $p$。

在所需复共轭特征中，上述正合列是
$$
0\to(NE(L)/pE(F))^+
\to B^-_{\mathrm{Sel}}
\to\ker(\Sha(E/F)[p]\to\Sha(E/L)[p])^+
\to0.
$$
若 $\rho_\ell:E(\mathbb Q)/p\to E(\mathbb F_\ell)/p$ 非零，
则范数正特征被包含于一维 $\ker\rho_\ell$。
全部 strict Selmer 消失核类与 $\iota(B^-_{\mathrm{Sel}})$ 的商
准确为 $\ker\rho_\ell/(NE(L)/pE(F))^+$。

## 对当前目标的作用

实际 Heegner 类 $[Q_{\ell,p}]$ 位于这个中项。
本结果区分基域范数点与真实 Sha 消失核，
并证明其辅助位为零是整个 Selmer 增广块的性质。
它不证明指定类非零。
通常 strict Selmer 群仍满射 $\Sha(E/\mathbb Q)[p]$，
所以指定局部核线并不消去未知 Sha 商。

已核 Morgan–Smith（2024），Corollary 4.9(2)，
给消失核与 corestriction 像的 Cassels–Tate 正交性；
本文没有把该伴随关系升级为满射性或非退化性。
