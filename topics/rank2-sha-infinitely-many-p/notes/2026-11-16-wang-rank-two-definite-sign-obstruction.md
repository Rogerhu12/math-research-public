# 2026-11-16：一个新检索到的 rank-two 完成声称在辅助域条件处矛盾

**状态：以下符号障碍已证明。它排除所核文稿的这组参数与推论，不是否定本课题主问题。**

## 所核实际声称

Xiong Wang，*The Birch and Swinnerton-Dyer Conjecture for Analytic Rank Two: A Complete Proof via Definite Anticyclotomic Iwasawa Theory*，文稿日期 February 2026，作者于 March 1 上传，[DOI/作者全文](https://doi.org/10.13140/RG.2.2.14539.86569)。

已亲读其 Definition6.1、Proposition6.3（printed pp29–30）以及 Theorem10.1（pp42–43）的参数。它同时要求虚二次域 $K$ 满足：

- 所有 $\ell\mid N_E$ 在 $K$ 中分裂；
- $w(E/K)=+1$；
- 在原解析秩二的设定中，$L(E,\chi_K,1)\ne0$。

Proposition6.3 将前一条件推出第二条件，证明把虚二次域的两个复嵌入算作两个复 place。Theorem10.1 再声称可以同时满足上述非零条件。这不是仅根据标题或摘要作出的判断。

## 完整符号反证

设 $E/\mathbf Q$ 是任意椭圆曲线，$K$ 是虚二次域，且每个坏约化素数都在 $K$ 中分裂。

对于每个 $\ell\mid N_E$，两个完成域都是 $\mathbf Q_\ell$，两个局部曲线相同，故它们的局部根数乘积为

$$
w(E/\mathbf Q_\ell)^2=1.
$$

对于 $\ell\nmid N_E$，$E$ 的好约化在任意有限扩张后仍是好约化，因此 $K$ 中每个该有限位的局部根数都是1。这也覆盖在 $K/\mathbf Q$ 中分歧但不整除 $N_E$ 的素数。

最后，虚二次域有**一个**复 place：两个复嵌入属于同一共轭对。椭圆曲线在一个复 place 的局部根数是 $-1$。于是所有有限位的乘积为1，而

$$
\boxed{w(E/K)=-1.}
\tag{1}
$$

这里所用的标准局部根数规则，见 Tim Dokchitser，
*Notes on the Parity Conjecture*，2010/2012，
[arXiv:1009.5389v2](https://arxiv.org/pdf/1009.5389)，§3.4，Definition3.19与Example3.20，printed p22：所有 Archimedean 位贡献 $-1$，好约化有限位贡献 $+1$。
以上计算不依赖代数秩奇偶猜想、Sha有限或任何 $p$-adic 非零假设。

所以文稿中两条前提已经不相容。进一步，若原解析秩确为2，功能方程给 $w(E/\mathbf Q)=+1$。二次基变换的精确分解

$$
L(E/K,s)=L(E/\mathbf Q,s)L(E^{\chi_K}/\mathbf Q,s)
$$

及其完备功能方程给

$$
w(E^{\chi_K}/\mathbf Q)
=\frac{w(E/K)}{w(E/\mathbf Q)}=-1.
$$

椭圆曲线及其二次扭曲的模性给解析延拓和功能方程；在中心 $s=1$，后者因此强制

$$
\boxed{L(E,\chi_K,1)=0.}
\tag{2}
$$

故其 Theorem10.1 所请求的最后一个非零条件也不能与全部坏素数分裂共存。扩大普通素数 $p$、选取别的同类虚二次域或援引无穷多个扭曲的非零定理，都不消除(1)–(2)；该指定符号类中的中心值全部为零。

## 对本课题的范围

此处已经足以阻止把这份文稿作为 rank-two 完成定理输入。无需为此逐一核查其余 level-raising、主猜想或 $\lambda$ 比较声称；本注未声称完成了文稿的全篇评审。

本课题仍按原 README 要求给完整证明；R901/R893 的真实字符、Heegner比较与未闭非零门保持。此次也重新查看 Banwait 的 arXiv:2609.08431v1；其有限素数准则和三矩范围已在本题 2026-11-14 的 Banwait–Agboola 核查注登记，本次不重复登记为新推进。
