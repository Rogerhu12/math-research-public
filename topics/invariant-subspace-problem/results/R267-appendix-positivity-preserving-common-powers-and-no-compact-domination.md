# R267 附录：保持函数正锥的全部幂共同分母及其紧支配边界

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：实际来源的完整构造。** 本文在原 Haar 每个尾上构造保持函数正锥的非零共同分母 $P^+$，所有实际整数逆 $C^{-r}P^+$ 也保持正锥。它们保同一收缩强*单位、全部原旗上的单射稠值及闭域图核心。这里的“正”始终指 $f\ge0\Rightarrow Tf\ge0$，不指 Hilbert 空间正自伴；非零拟幂零算子不可能正自伴。没有构造 $Y^2=C(P^+)^2$ 的有界分子 $Y$。

## 1. 原块与实际误差

固定原 Haar 尾 $C=A^{(m_0)}$，在该尾按局部位编号。记

$$
N_j=C^{2^j}/d_j,\qquad d_j=\|C^{2^j}\|,\qquad
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad N_j^2=\eta_jN_{j+1},
\tag{1}
$$

$$
\|N_j\|=1,\qquad
0<\eta_j\le e^{-770\,16^j},\qquad
\sum_{j\ge m}\eta_j\le2e^{-770\,16^m}.
\tag{2}
$$

$N_j$ 是原正权平移，保持函数正锥。沿用
[原共同分母稿](R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)
的 $q_\nu=2^{\nu+6}$（$\nu\ge1$）和依次后移、互不交的连续位块
$F_\nu=[m_\nu,m_\nu+q_\nu)$。这些块满足旧稿的收缩预算；不改变原权或进位。

旧因子与新因子分别为

$$
T_\nu=\frac2{q_\nu+2}\sum_{j\in F_\nu}Y_j,\qquad
Y_j=N_j(I+N_j)^{-1},\qquad
T_\nu^+=\frac2{q_\nu+2}\sum_{j\in F_\nu}N_j.
\tag{3}
$$

全部因子属于原多项式范数闭包并互相交换。只有 $T_\nu^+$ 在此被断言保持正锥。

独立局部范数
$\|\sum_{j\in F_\nu}E_j\|\le(q_\nu+1)/2$
和 (1)–(2) 给

$$
\|T_\nu^+\|
\le\frac{q_\nu+1}{q_\nu+2}
+\frac2{q_\nu+2}\sum_{j\in F_\nu}\eta_j
\le\frac{q_\nu+1+4e^{-770\,16^{m_\nu}}}{q_\nu+2}<1.
\tag{4}
$$

这是真实 $N_j$ 的范数预算。又
$(I+N_j)^{-1}=(I-N_j)(I-N_j^2)^{-1}$，所以

$$
\|(I+N_j)^{-1}\|\le\frac2{1-\eta_j}<3,\qquad
\|N_j-Y_j\|\le3\eta_j.
$$

因此

$$
\delta_\nu:=\|T_\nu^+-T_\nu\|
\le\frac6{q_\nu+2}\sum_{j\in F_\nu}\eta_j,\qquad
\Delta:=\sum_{\nu\ge1}\delta_\nu<12e^{-770}<\frac1{64}.
\tag{5}
$$

## 2. 正乘积的非零强极限与尾强*单位

记旧稿已付的强乘积为

$$
P^Y=\operatorname*{SOT-lim}_{n\to\infty}\prod_{\nu=1}^nT_\nu,
\qquad
Q_n^Y=\operatorname*{SOT-lim}_{k\to\infty}\prod_{\nu=n+1}^kT_\nu.
$$

旧稿给它们收缩、$Q_n^Y\to I$ 强*，并且
$\langle P^Y\Omega,\Omega\rangle\ge31/32$。

有限乘积的准确恒等式为

$$
\prod_{\nu=1}^nT_\nu^+-\prod_{\nu=1}^nT_\nu
=
\sum_{\nu=1}^n
\left(\prod_{i<\nu}T_i^+\right)
(T_\nu^+-T_\nu)
\left(\prod_{\nu<i\le n}T_i\right).
\tag{6}
$$

对每个固定 $\nu$，最后一段有旧的强极限；第 $\nu$ 项范数不超过 $\delta_\nu$。由 (5) 的可和控制，(6) 证明新乘积真正在全 $H$ 强收敛，而不是仅真空列收敛：

$$
P^+=\operatorname*{SOT-lim}_{n\to\infty}P_n^+,\qquad
P_n^+=\prod_{\nu=1}^nT_\nu^+,\qquad
\|P^+\|\le1,\quad \|P^+-P^Y\|\le\Delta.
\tag{7}
$$

特别

$$
\langle P^+\Omega,\Omega\rangle\ge31/32-\Delta>61/64,
\tag{8}
$$

所以 $P^+\ne0$。正锥在 $L^2$ 中闭，而每个有限乘积保持它；故 $P^+$ 也保持函数正锥。

同样从第 $n+1$ 个因子开始，(6) 给实际尾积 $Q_n^+$，并给

$$
P^+=P_n^+Q_n^+,\qquad
\|Q_n^+\|\le1,\qquad
\|Q_n^+-Q_n^Y\|\le\sum_{\nu>n}\delta_\nu.
\tag{9}
$$

于是 $Q_n^+\to I$ 强。收缩的强恒等极限自动是强*极限，因
$\|(Q_n^{+*}-I)x\|^2\le2\|x\|^2-2\operatorname{Re}\langle Q_n^{+*}x,x\rangle$。
各 $Q_n^+$ 也保持正锥。

## 3. 同一分母的全部正整数逆与原旗

令 $k_n=\sum_{\nu\le n}2^{m_\nu}$。新因子具有精确正系数多项式分解

$$
T_\nu^+=C^{2^{m_\nu}}U_\nu(C),\qquad
U_\nu(z)=\frac2{q_\nu+2}\sum_{j\in F_\nu}
\frac{z^{\,2^j-2^{m_\nu}}}{d_j}.
\tag{10}
$$

$U_\nu(0)>0$，$C$ 拟幂零，故 $U_\nu(C)$ 是有界交换单位；它本身保持正锥，但不声称其逆保持正锥。置 $U^{[n]}=\prod_{\nu\le n}U_\nu(C)$。给定任意整数 $r\ge0$，选 $k_n\ge r$，定义

$$
P_r^+=C^{k_n-r}U^{[n]}Q_n^+.
\tag{11}
$$

它是实际有界正锥保持算子，且

$$
\boxed{P^+=C^rP_r^+,\qquad P_r^+=C^{-r}P^+\text{ 在全 }H\text{ 上有界}.}
\tag{12}
$$

原 $C$ 单射保证 (11) 与所选 $n$ 无关。再用更大的 $k_n$，得到每个 $P_r^+\in\mathfrak F_C=\bigcap_sC^sC'$。

使用 R23 的收缩强*多项式单位 $E_\ell=e_\ell(C)$，取 $\ell(n)\ge n$、最低次数至少 $k_n$，写 $E_{\ell(n)}=C^{k_n}B_n(C)$，并置

$$
W_n=(U^{[n]})^{-1}B_n(C)\in\mathcal A.
$$

则同一个 $P^+$ 满足

$$
\boxed{P^+W_n=Q_n^+E_{\ell(n)},\qquad
\|P^+W_n\|\le1,\qquad P^+W_n\longrightarrow I\text{ 强*}.}
\tag{13}
$$

对 $P_r^+$，同一单位可写为 $P_r^+(C^rW_n)$。这付每个 $P_r^+$ 在全部有限放大原不变旗子商上的单射稠值：所有系数保持旗；核被 (13) 的单位杀掉，像闭包包含其强极限。特别它们都是非零 quasiaffinity。

每个 $P_r^+$ 拟幂零且在 UHF 外，来自 (12) 的全部幂整除及旧稿 §7 的 $\mathfrak F_C\cap\mathfrak U=\{0\}$。同一收缩单位也保旧稿 §6.1 的闭交换域图核心：对 $x\in D(T)$，$P^+W_nx\to x$ 且 $TP^+W_nx=P^+W_nTx\to Tx$。仍不由此推 $P^+H\subset D(T)$。

此外 $P^+\Omega>0$ 几乎处处。若它在正测度集 $E$ 上为零，则
$\langle\Omega,P^{+*}\mathbf1_E\rangle=0$；$P^{+*}$ 保正锥使 $P^{+*}\mathbf1_E=0$，与其单射性矛盾。这里不声称 $P^+\Omega$ 有正的本质下界，也不声称 $P^+$ 把每个非零非负向量都送成几乎处处正。

## 4. 原高位乘法的范数交换预算

令 $Z_j=M_{\chi_j}$。它是自伴酉，且 $Z_j\to0$ 于 WOT。由 (1) 的真实逐位 carry，$k<j$ 时

$$
\|[N_k,Z_j]\|
\le2\prod_{\ell=k}^{j-1}\eta_\ell,
\tag{14}
$$

而 $k=j$ 时上界为 $2$，$k>j$ 时交换子为零。这里使用高位 $N_{k+1}$ 与第 $k$ 位矩阵交换，没有将所有 $N_k$ 换成独立 $E_k$。

对收缩有限乘积逐项展开交换子，随后对 (7) 取强极限，得到对 $j\ge1$

$$
\boxed{\|[P^+,Z_j]\|
\le b_j:=\frac4{q_{\nu(j)}+2}\mathbf1_{\{j\in\cup_\nu F_\nu\}}
+8e^{-770\,16^{j-1}}\longrightarrow0.}
\tag{15}
$$

$\nu(j)$ 只在 $j\in F_{\nu(j)}$ 时使用。证明余项时，
$\sum_{k<j}\prod_{\ell=k}^{j-1}\eta_\ell
\le\eta_{j-1}/(1-\eta_0)\le2e^{-77016^{j-1}}$；
每个 $k$ 至多出现一次，且 $4/(q_\nu+2)\le4$。
第一项趋零因为 $q_\nu\to\infty$，而块依次后移。

同一界适用于任何固定起点的正尾积。由 (11)，$P_r^+$ 是一个固定 UHF 多项式乘该尾积；UHF 元与 $Z_j$ 渐近范数交换。因此

$$
\|[P_r^+,Z_j]\|\longrightarrow0\qquad(r\ge0\text{ 固定}).
\tag{16}
$$

## 5. 这个新正来源不支配非零紧算子

固定 $r\ge0$。若紧算子 $K$ 满足真实 Banach lattice 支配

$$
|Kf|\le P_r^+|f|\qquad(f\in H),
\tag{17}
$$

则 $K=0$。特别不存在非零正紧算子 $0\le K\le P_r^+$。

证明取乘法投影 $Q_j^\pm=(I\pm Z_j)/2$。由 (17)，

$$
\|Q_j^+KQ_j^-\|\le\|Q_j^+P_r^+Q_j^-\|,
\qquad
\|Q_j^-KQ_j^+\|\le\|Q_j^-P_r^+Q_j^+\|.
$$

按两正交半空间写块矩阵，
$\|[L,Z_j]\|=2\max(\|Q_j^+LQ_j^-\|,\|Q_j^-LQ_j^+\|)$；
所以 (16) 给 $\|[K,Z_j]\|\to0$。
对固定 $x$，$Z_jx\rightharpoonup0$，紧性给 $KZ_jx\to0$；
交换子界又给 $Z_jKx\to0$ 于范数。$Z_j$ 酉，故 $Kx=0$，证毕。

旧[快衰减文献笔记 §6](../notes/2026-11-12-fast-decay-and-odometer-literature.md)只用单一 weighted composition 的局部性排 $C^r$ 的紧支配。本节针对新 UHF 外的无限正乘积；没有把保持正锥自动提升为正积分核或紧下界。

## 6. 继续保留的平方来源

新 $P^+$ 是可以直接代入最大商正向定理的实际非局部分母；它与所有原交换子交换，且 (13) 已付同一图核心所需单位。但

$$
Y\in C',\qquad Y^2=C(P^+)^2
$$

仍是未解决的真实有界二次方程。本文没有由正锥保持、整数逆全域有界、UHF 外性或全喷射平坦推出这个 $Y$，也没有用 §5 的紧支配排除代替普通 ISP。
