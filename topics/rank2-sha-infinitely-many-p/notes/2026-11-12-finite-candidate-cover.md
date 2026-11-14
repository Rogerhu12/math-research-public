# 有限候选覆盖：充分条件、有限族恒等式与量词缺口

日期：2026-11-12。会话：Astra-rank2-Sha / literature_scope。

**状态：下述逻辑引理及多二次域分解已证明；尚未得到满足条件的固定有限曲线族。** 本文不把“每个素数可以另选一条曲线”替换成题目要求的固定曲线。

## 1. 真正足够的有限覆盖

设 $\mathcal F=\{E_1,\ldots,E_m\}$ 是**事先固定、与 $p$ 无关**的有限曲线集，每条都已证明秩至少为 $2$。记
$$
G_i=\{p:\Sha(E_i/\mathbb Q)[p^\infty]\text{ 有限}\}.
$$
若 $\bigcup_iG_i$ 无穷，则某个 $G_i$ 无穷。证明：有限个有限集的并有限，取逆否命题即可。若并集覆盖所有素数中正的自然下密度，则至少一个 $G_i$ 有正的自然上密度；在没有证明密度存在时，不能直接声称某项有自然密度。

可用的等价搜索目标是：存在**固定高度界 $H_0$**，使无穷多个 $p$ 各自有一个高度不超过 $H_0$ 的已证秩至少二的见证曲线。固定有理曲线的标准整模型在固定高度内只有有限多个。若高度界随 $p$ 无界增长，即使增长很慢，也不能据此使用有限鸽巢。

### 1.1 精确秩已知时的平均余秩判据

设每个 $r_i=\operatorname{rank}E_i(\mathbb Q)$ 都已精确确定，令
$$
s_{i,p}=\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E_i/\mathbb Q),
\qquad \delta_{i,p}=s_{i,p}-r_i.
$$
R1 给 $\delta_{i,p}\in\mathbb Z_{\ge0}$，且 $\delta_{i,p}=0$ 等价于所需的初级有限性。因此
$$
\sum_{i=1}^m\delta_{i,p}<m
\tag{1}
$$
就保证至少一条曲线在该素数处初级有限。

如果还分别证明 $(-1)^{r_i}=w(E_i/\mathbb Q)$，Dokchitser–Dokchitser 的 $p$-parity 定理给每个 $\delta_{i,p}$ 为偶数，此时可把 (1) 放宽为
$$
\sum_{i=1}^m\delta_{i,p}<2m.
\tag{2}
$$
证明：若每项非零，每项至少为 $2$，与 (2) 矛盾。来源：*On the Birch–Swinnerton-Dyer quotients modulo squares*，Annals of Mathematics 172 (2010), 567–596，Theorem 1.4 / 4.19，[原文](https://arxiv.org/pdf/math/0610290)，[出版页面](https://annals.math.princeton.edu/2010/172-1/p11)。已核对这一定理适用于所有 $E/\mathbb Q$ 和所有 $p$；它比较的是 Selmer 余秩与根数，不能直接把一般 Mordell–Weil 秩奇偶当作已知。

### 1.2 只有秩下界时仍有一个安全版本

若只有已证明的下界 $r_i\ge\ell_i\ge2$，不能把 $s_{i,p}-\ell_i$ 称为 Sha 的余秩。不过它仍是非负整数。若另已算出 $w(E_i)=(-1)^{\ell_i}$，则 $s_{i,p}-\ell_i$ 是非负偶数。因此
$$
\sum_{i=1}^m s_{i,p}<\sum_{i=1}^m\ell_i+2m
\tag{3}
$$
保证某个 $s_{i,p}=\ell_i$，继而
$$
\ell_i\le r_i\le s_{i,p}=\ell_i
$$
同时证明该候选的精确秩及初级有限性。特别地，如果每条只知道秩至少二，但都已算出根数 $+1$，充分上界为
$$
\sum_{i=1}^m s_{i,p}<4m.
\tag{4}
$$
这不依赖事先补齐每条候选的精确秩证明。若没有独立根数输入，使用 $\sum_i s_{i,p}<\sum_i\ell_i+m$ 即可。

### 1.3 有限层平均的另一充分条件

在精确秩 $r_i$ 已知时，设 $t_{i,p}=\dim_{\mathbb F_p}E_i(\mathbb Q)[p]$。有限层 Kummer 列给
$$
q_{i,p}:=\frac{\#\operatorname{Sel}_p(E_i/\mathbb Q)}{p^{r_i+t_{i,p}}}
=\#\Sha(E_i/\mathbb Q)[p]\in\{1,p,p^2,\ldots\}.
$$
所以
$$
\frac1m\sum_{i=1}^m q_{i,p}<p
\tag{5}
$$
迫使某个 $q_{i,p}=1$。该曲线的 $\Sha[p]$ 为零，从而整个 $\Sha[p^\infty]$ 为零：非零的 $p$-初级 torsion 元素适当乘 $p$ 的幂会给非零 $p$-挠元。

因此，一个对固定有限候选集的、独立于 $p$ 的规范化平均上界 $\frac1m\sum_iq_{i,p}\le C$，若在无穷多个 $p$ 成立，就足以完成主目标。现有全体曲线的平均定理并不是这条有限集上界。

## 2. 真正的有限族恒等式：多二次基变换

令 $F/\mathbb Q$ 是固定多二次 Galois 扩张，$G\simeq(\mathbb Z/2\mathbb Z)^d$，$m=|G|$，$\widehat G$ 为其全部二次特征，包括平凡特征。对固定 $E/\mathbb Q$，以 $E^\chi$ 表示相应二次扭转。

### 已证明命题

对每个奇素数 $p$，有
$$
\operatorname{Sel}_{p^\infty}(E/F)
\simeq\bigoplus_{\chi\in\widehat G}
\operatorname{Sel}_{p^\infty}(E^\chi/\mathbb Q),
\tag{6}
$$
以及
$$
\Sha(E/F)[p^\infty]
\simeq\bigoplus_{\chi\in\widehat G}
\Sha(E^\chi/\mathbb Q)[p^\infty].
\tag{7}
$$
Mordell–Weil 群张量 $\mathbb Q$ 后也有同样的特征分解。特别地，
$$
\delta_p(E/F)=\sum_{\chi\in\widehat G}\delta_p(E^\chi/\mathbb Q).
\tag{8}
$$

**证明。** 因为 $p\ne2$，$m$ 在每个 $p$-初级群上可逆，故
$$
e_\chi=\frac1m\sum_{g\in G}\chi(g)g
$$
是正交幂等元，且 $\sum_\chi e_\chi=1$。取一个定义在 $F$ 上的扭转同构 $\iota_\chi:E^\chi\to E$，满足 $g\iota_\chi=\chi(g)\iota_\chi$。它把来自 $E^\chi/\mathbb Q$ 的限制类送入 $E/F$ 上的 $\chi$-分量。

反过来，对 $E/F$ 的 $\chi$-分量施以 $\iota_\chi^{-1}$，便成为 $E^\chi/F$ 的 $G$-不变分量。限制映射到不变分量的逆为 $m^{-1}\operatorname{cor}$，因为
$$
\operatorname{cor}\operatorname{res}=m,
\qquad
\operatorname{res}\operatorname{cor}=\sum_{g\in G}g.
$$
这些映射与全局及局部 Kummer 映射相容；余限制在点的 Kummer 像上由范数给出，且限制、余限制均保持处处局部平凡条件。因此该构造分别在 Selmer 和 Sha 子群上给互逆同构，证明 (6)、(7)。对有理点张量 $\mathbb Q$ 同样用幂等元分解，即得秩相加。对 (6) 取余秩并减去秩等式，得到 (8)。证毕。

**可攻克的具体新门槛。** 若这些固定扭转均已证明秩至少二且根数 $+1$，则只要在无穷多个奇 $p$ 证明
$$
\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/F)<4m,
\tag{9}
$$
由 (4)、(6) 与有限鸽巢便完成本题。精确秩都已知时，可以改用
$$
\operatorname{corank}\operatorname{Sel}_{p^\infty}(E/F)
<\operatorname{rank}E(F)+2m
$$
及各扭转的秩/根数奇偶核查。此门槛比证明 $\Sha(E/F)[p^\infty]$ 整体有限弱，但本轮未得到满足它的无穷素数定理。

**已有候选不能虚增覆盖。** R4、R7 已证明 $E_{17}$ 及其二同源曲线 $y^2=x^3+68x$ 都精确秩二；但 R7 也给出它们在每个奇 $p$ 的初级 Sha 同构，所以这个二元候选集并未增加 good-prime 并集。取 $F=\mathbb Q(i)$ 时，$E_{17}$ 的 $-1$ 二次扭转又与原曲线相同；分解只是同一个未知项出现两遍。未在本笔记中把其他尚无本仓库精确秩证明的候选标成“已证秩二”。

## 3. 为什么逐个素数的平均结果不自动提供有限覆盖

以下抽象反例已经显示量词不能交换。列出曲线 $E_1,E_2,\ldots$ 和素数 $p_1,p_2,\ldots$，人为规定
$$
\mathcal G(E_n,p_j)\Longleftrightarrow n\ge j.
$$
每个固定 $p_j$ 下，满足性质的曲线在前 $N$ 条中密度趋于 $1$；但每个固定 $E_n$ 只满足有限多个 $p_j$。因此，即使将“每个 $p$ 有曲线”加强成“每个 $p$ 下密度 $1$ 的曲线满足”，仍不能推出固定曲线对应无穷多个 $p$。

还有一个针对有限候选的障碍：对固定 $p$，任意修改预先指定的有限集上的 Selmer 数值，都不改变全体曲线按高度排序的极限平均，因为有限项对趋于无穷的分母贡献趋于零。这一陈述纯属极限运算，不声称实际 Selmer 群可任意修改；它证明平均等式本身无法恢复预设有限集的数值。

若要用无限族平均补足这一步，一个足够的紧性条件是：在同一个已证秩至少二的可数族上，存在**与 $p$ 无关**的概率权重 $w_n$，使无穷多个 $p$ 满足
$$
\sum_{n\ge1}w_n\mathbf1_{\mathcal G(E_n,p)}\ge\varepsilon>0.
$$
取固定 $N$ 使 $\sum_{n>N}w_n<\varepsilon$，则每个这样的 $p$ 必有前 $N$ 条中的见证，归结为有限覆盖。通常按不断增大的高度截断取均匀平均，其质量会离开每个固定有限集，并不具有这条性质。

## 4. 最接近的文献输入具体缺哪一个量词

### 4.1 全体曲线或大同余族的平均 Selmer

Bhargava–Shankar，*The average size of the 5-Selmer group of elliptic curves is 6, and the average rank is less than 1*（2013 年稿），Theorems 1–2，[原文](https://arxiv.org/pdf/1312.7859)。已核对陈述：固定 Selmer 素数 $5$，对按高度排序的全部曲线，或满足固定有限个同余条件的无限族，平均 $\#\operatorname{Sel}_5=6$。这既没有变化的无穷 Selmer 素数，也没有固定有限候选集。即使假设每个 $p$ 的全体平均都为 $p+1$，第 3 节的有限集不可见性仍在。

Ross Paterson，*The Failure of Galois Descent for p-Selmer Groups of Elliptic Curves*，Math. Proc. Cambridge Philos. Soc. 177 (2024), 185–218，[出版全文](https://doi.org/10.1017/S0305004124000197)，Theorems 1.1、1.7、1.9 及 §1.4：其固定数域扩张上的平均界仍对**变化的曲线**取平均，无条件部分使用 $p\in\{2,3,5\}$。它不是对本节固定 $E/F$ 的逐曲线上界 (9)，不能把平均数值充当该固定曲线的 Selmer 余秩上界。

### 4.2 有限曲线组的 simultaneous 非零定理

Kriz–Nordentoft，*Horizontal p-adic L-functions*，2025-11-18 版本，Theorem 1.2，[原文](https://arxiv.org/pdf/2310.20678)。它固定 $E_1,\ldots,E_n$，但假设每个 $L(E_i,1)\ne0$；结论对**导子增长的 Dirichlet 特征 $\chi$**计数，给 $\prod_iL(E_i,\chi,1)\ne0$。这里固定组中的基曲线已经是解析秩零，变化的是扭转特征；不是固定若干已证秩二曲线、变化 $p$、二次 leading term 不同时消失。

Theorem 1.1 的单曲线扭转非零，也只选出新的中心值非零扭转；二次扭转情形这些曲线由 Gross–Zagier–Kolyvagin 为秩零。不能用它们占据本题要求秩至少二的候选位置。

### 4.3 CM twist 分布与 Euler 系统

Jie Shu，*Selmer ranks in twists of CM abelian varieties*，2025-07-31 v2，Theorem 1.4、Corollary 1.5，[原文](https://arxiv.org/pdf/2504.21274)。其密度沿固定 $p$ 的 character fan 取先 $X\to\infty$、再层数趋于无穷的极限；不是固定有限 twist 集。当 $\mu_p$ 不在 CM 环中时，原文 §1.2、§1.4 使用 $\mathcal O[\zeta_p]\otimes_{\mathcal O}A$ 的 Serre tensor，维数一般也随 $p$ 改变。Theorem 1.8 另显式假设所有相关 $\Sha[p^\infty]$ 有限。本轮只核对这些范围，不以新稿为证明输入。

已核查的 Kato、Pollack–Rubin 及 CM 广义 Kato 类结果也没有补上有限族门槛。以全部候选均处于可用 cyclotomic 条件为例，R3 及 supersingular note 给出的实际界是
$$
\sum_i s_{i,p}\le\sum_i\operatorname{ord}_{T=0}L_{p,i}(T),
\tag{10}
$$
超奇异时可逐条选择适用的 signed 分量。右边仍是未知的各条曲线增广点消失阶，不能据此报出小于 $4m$ 的固定数值。广义 Kato 类路线同样需要证明某条候选的相应类非零；有限个判据并置本身不证明这些类不同时为零。精确定理及假设见 `notes/2026-11-12-literature-scope.md` §5。

本轮没有找到能直接用于固定有限 CM 秩二 twist 集的 ordinary/signed 二次项非同时消失定理，也没有得到 (2)、(3)、(5) 或 (9) 的无穷素数上界。可继续攻克的目标现在是明确的**固定有限族平均缺陷界**；并非仅扩大一个随 $p$ 变化的可选曲线名单。
