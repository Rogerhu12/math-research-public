# 椭圆单位字符对数的一个显式估值上界

**可信度：已证明。** 本文把 Gaudron 的代数系数 $p$ 进对数线性形式定理实际代入本题，得到随 $p$ 明确变化的上界，而不只援引 Baker–Brumer 的非零性。该上界很大，不能给出 R16 所需的 $\nu_p\le3$。它精确显示：固定有理函数的有界高度，并没有使此处的数域次数、对数个数及定理的收敛参数固定。

## 1. 数据与已知非零性

沿用 R16、R19：
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
p\ge13,\quad p\equiv1\pmod4,\quad p\ne17,
$$
$$
L=K(E[\mathfrak p]),\quad G=\operatorname{Gal}(L/K),\quad
n=|G|=p-1,\quad F=L_{\mathfrak P},\quad [F:\mathbb Q_p]=p-1.
$$
令 $\rho=t(P_\pi)$、$\varepsilon=\Phi(P_\pi)$，其中 $\Phi$ 是 R19 的固定有理函数。R19 已证 $\varepsilon$ 是全局单位，且在本地属于 $1+\rho\mathcal O_F$。字符 $\chi$ 的 Teichmüller 提升记为 $\widetilde\chi$。

已完成的 [单位字符非零性笔记](2026-11-12-unit-character-nonvanishing.md) 与 R19 给
$$
e_\chi\log_p\varepsilon\ne0.
\tag{1}
$$
R16 的标准单位格生成元对数赋值为 $1/(p-1)$，而 R19 的比较系数为 $p$ 进单位，故
$$
v_p(e_\chi\log_p\varepsilon)=\nu_p+\frac1{p-1}.
\tag{2}
$$
这里 $v_p(p)=1$。

存在只依赖于固定 $E,\Phi$ 的常数 $H\ge1$，使
$$
h(g\varepsilon)\le H\quad(g\in G)
\tag{3}
$$
对全部目标素数成立。理由是挠点的 Néron–Tate 高度为零，固定曲线的坐标高度因此有统一上界；再应用固定有理函数的高度上界。所有求值点避开 $\Phi$ 的零极点，见 R19。共轭不改变绝对对数 Weil 高度。

## 2. 为什么必须同时记录数域和收敛半径

为容纳代数系数 $\widetilde\chi(g)^{-1}$，取
$$
k=L\,\mathbb Q(\mu_{p-1})\subset\mathbb C_p,\qquad D=[k:\mathbb Q].
$$
于是
$$
D\le2(p-1)\varphi(p-1)\le2p^2.
\tag{4}
$$
不能只写 $[L:\mathbb Q]=2(p-1)$ 后忽略字符系数的全局代数域。局部 $\mu_{p-1}\subset\mathbb Q_p$ 不表示这些系数属于全局 $L$。

对 $x\in\rho\mathcal O_F$，逐项估计给
$$
v_p\!\left(\frac{x^m}{m}\right)
\ge\frac{m-(p-1)v_p(m)}{p-1}\ge\frac1{p-1}.
$$
最后一步可令 $m=p^a b$、$p\nmid b$，用 $p^a-(p-1)a\ge1$。因此
$$
v_p\bigl(\log_p(g\varepsilon)\bigr)\ge\frac1{p-1}.
\tag{5}
$$
这并不足以直接满足下述定理的强收敛半径条件。合法的统一选择是
$$
u_g=p\log_p(g\varepsilon),\qquad
\alpha_g=(g\varepsilon)^p.
\tag{6}
$$
它满足
$$
\exp(u_g)=\alpha_g,\quad
h(\alpha_g)\le pH,\quad
v_p(u_g)\ge1+\frac1{p-1}.
\tag{7}
$$
指数等式可先注意 $v_p((g\varepsilon)^p-1)>1/(p-1)$，再在指数与对数互逆的圆盘中应用恒等式。对于 $p\ge13$，
$$
|u_g|_p\le p^{-1-1/(p-1)}
\le e^{-1}p^{-2/(p-1)}.
\tag{8}
$$
所以把对数乘以 $p$ 确实解决收敛条件，但它同时把代数数的高度上界变成了 $pH$。

## 3. Gaudron 定理的实际代入

一手来源为 É. Gaudron, *Minorations simultanées de formes linéaires de logarithmes de nombres algébriques*, Bull. Soc. Math. France **142** (2014), 1–62，[作者原文](https://lmbp.uca.fr/~gaudron/art12.pdf)，[期刊页面](https://www.numdam.org/articles/10.24033/bsmf.2658/)。以下核对的是 Théorème 2.1（印页 5），并使用 §2.2(3) 对隐藏的 $p$ 依赖的说明。该定理允许代数系数，也不要求输入对数全部 $\mathbb Q$ 线性无关。

取唯一的线性形式
$$
\mathcal L_p=\sum_{g\in G}\widetilde\chi(g)^{-1}u_g
=p(p-1)e_\chi\log_p\varepsilon\ne0.
\tag{9}
$$
系数都是单位根，高度为零，常数项取零。定理中的 $t=1$，且 $s=1$：最小有理子空间 $T_u$ 不包含于该形式的核，因为 (9) 非零；一个超平面与 $T_u\otimes k$ 相交的余维于是恰为一。设 $J$ 是输入对数的任意极大 $\mathbb Q$ 线性无关子集，只需 $|J|\le n$。

定理中的实参数 $\mathfrak e$ 可由 (8) 取为 Euler 常数 $e$。统一选
$$
\log a_g=pH,\qquad \log b=D,
$$
并定义
$$
A_p=\left\lfloor D\log(e+D+npH)\right\rfloor+1.
\tag{10}
$$
这些选择满足原定理的每一项假设。它给出
$$
\log|\mathcal L_p|_p\ge-B_p,
\tag{11}
$$
其中可以明确取
$$
\boxed{
B_p=(10n)^{59n^2}\,A_p\,
\bigl(D+A_p+D\log D\bigr)\,(1+DpH)^n.
}
\tag{12}
$$
从原定理到 (12) 只把乘积 $\prod_{g\in J}(1+DpH)$ 放大为 $n$ 次幂。没有把系数当作普通整数，也没有假设存在固定次数域容纳全部 $p$。

由 (2)、(9)，
$$
v_p(\mathcal L_p)=1+\nu_p+\frac1{p-1}.
$$
因此得到本题一个无条件、明确依赖 $p$ 的上界
$$
\boxed{
\nu_p\le\frac{B_p}{\log p}-1-\frac1{p-1}.
}
\tag{13}
$$
若不想保留实际域次数 $D$，可在 (10)、(12) 中统一以 $2p^2$ 代替它；所有右侧因子均随 $D\ge1$ 单调增加。

### 3.1 量级

固定 $H$ 后，$n=p-1$、$D\le2p^2$、$A_p=O_H(p^2\log p)$，从而
$$
B_p\le\exp(C_Hp^2\log p)
\tag{14}
$$
对某个固定有效常数 $C_H$ 成立。这是已经证明的估值控制，但 (12) 的数值对所有目标 $p$ 都远大于 $4\log p$。因而 (13) 不排除 $\nu_p\ge4$ 对全部大素数成立。不能从这个上界推出哪怕一个新增的 $\nu_p\le3$ 素数，更不能推出无穷多个。

## 4. 多字符和有限候选不能直接改进成目标阈值

Gaudron 的同时版本控制多个线性形式绝对值的 **最大值**，等价于只保证其中某个形式的赋值受控。把本题指定的 $\chi$ 与其他字符一起放入时，所得非小值可能全部来自其他字符，不能转给指定的 $\chi$。即便通过非零字符的已知结构保证维数参数 $s$ 增大，仍须证明目标字符本身落在受控的分量中。

若使用一个预先固定、有限的曲线集合，并只把每条曲线各自的目标字符放入同时定理，则可以获得“至少一条曲线”的赋值上界。这一量词形式确实适合有限候选覆盖方法。然而，对 $m$ 条固定候选，输入对数数目仍随 $p$ 增长，而 $s\le m$ 固定；更大的公共数域还会增加 $D$。原定理的 $(10n)^{59n^2/s}$ 因子本身已经增长，远不能给出固定门槛 $3$。

这里的结论仅针对上述一手定理及其直接代入，不声称所有可能的超越论估计均不可能改进。若要推进主问题，需要针对这族椭圆单位获得远强于 (13) 的估值控制，或者证明某个有限候选族的目标字符深度不能同时达到 $4$。

## 与现有结果的关系

- R19、单位字符非零性笔记给出固定函数、有界高度及每个 $p$ 的非零性。
- 本文新增 (12)–(14) 的完整参数代入，区分 $L$ 的次数、字符系数扩域、输入对数数目及强收敛半径。
- R20、R21 提供的有限精度判据仍然有效；本文的通用定量对数界未达到它们要求的固定小阈值。
