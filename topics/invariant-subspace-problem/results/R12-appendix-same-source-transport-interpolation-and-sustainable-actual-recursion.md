# 原同源运输插值与一条可持续的真实 Deddens 递推

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-27（Asia/Taipei）。

**状态：已证明的正向中间结论。** 本稿给原 Haar 模型上的实际输入运输矩阵、逐边真实成本、准确普通范数插值条件，以及一条始终留在固定非零球内的真实递推。该递推的累计对数 Deddens 成本有明确五次上界；没有将它冒称为低于原幂衰减的预算，也没有假定 Deddens 算子保持未知的 $A$-不变子空间。

## 1. 原对象与输入不变的约定

沿用 [R9](R9-radial-odometer-and-nilpotent-approximants.md)、[R12](R12-normalized-powers-and-compact-commutant.md)：
$$
H=L^2(\mathbb Z_2,\mu),\qquad
(Af)(y)=w(y)f(y-1),
$$
$$
w(0)=0,\quad w(y)=\alpha_{v_2(y)}\ (y\ne0),\quad
\alpha_j=e^{-L_j},
$$
$$
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3},
\qquad\alpha_0=e^{-20}.
$$
写
$$
\beta_0=1,\qquad
\beta_n=\|A^n\|=\prod_{a=1}^n\alpha_{v_2(a)},\qquad
\mathcal D=\mathcal D_A.
$$

固定 $N=2^m$，用原等距坐标
$$
f_r(z)=N^{-1/2}f(r+Nz),\quad 0\le r<N,
\qquad H=\mathbb C^N\otimes L^2(\mathbb Z_2).
\tag{1.1}
$$
本稿允许矩阵 $B(z)$ 依赖实际尾变量，但所有输入始终为给定的 $h_r(z)$，不先换成条件期望或另外挑选的便宜向量。具体递推 §6 中甚至可取 $B$ 不依赖 $z$。

## 2. 每条实际下三角边的准确成本

对 $0\le s\le r<N$，置
$$
\boxed{d_{rs}=\frac{\beta_{r-s}\beta_s}{\beta_r}.}
\tag{2.1}
$$
由 [有限头准确成本公式 §6](R12-appendix-contractive-deddens-core-and-exact-finite-head-cost.md)，它恰为真实矩阵单位 $e_{rs}\otimes I$ 的最佳 Deddens 成本。为便于后续直接应用，记
$$
h_\ell(y)=\prod_{a=1}^{\ell}w(y+a),\qquad
D_\ell(z)=\operatorname{diag}(h_\ell(r+Nz))_{r<N}.
$$
乘积相消给
$$
\frac{h_\ell(r+Nz)}{h_\ell(s+Nz)}
=\frac{\beta_s}{\beta_r}
\prod_{a=s+1}^{r}w(Nz+\ell+a)
\le d_{rs}\qquad(r\ge s).
\tag{2.2}
$$
正整数尾轨道稠密、$w$ 连续，使右侧最佳值达到上确界；相应单矩阵单位的算子范数就是唯一非零条目的绝对值。因此 (2.1) 是必要且充分的准确边费用，不是仅有的充分估计。

这个费用可完全用二进 carry 写出。令 $S_n=-\log\beta_n$，则
$$
S_n=nL_0+\sum_{k\ge1}(L_k-L_{k-1})\left\lfloor\frac n{2^k}\right\rfloor.
$$
所以
$$
\log d_{rs}=\sum_{k=1}^{m-1}(L_k-L_{k-1})\varepsilon_k(r,s),
\tag{2.3}
$$
$$
\varepsilon_k(r,s)=
\left\lfloor\frac r{2^k}\right\rfloor
-\left\lfloor\frac s{2^k}\right\rfloor
-\left\lfloor\frac{r-s}{2^k}\right\rfloor\in\{0,1\}.
$$
因 $L_k$ 严格增加，$d_{rs}\ge1$。每个 $\varepsilon_k\le1$，并且 $r=2^{m-1},s=1$ 同时令所有 $k=1,\ldots,m-1$ 的 $\varepsilon_k=1$。因此
$$
\boxed{D_m:=\max_{s\le r<N}d_{rs}
=\frac{\alpha_0}{\alpha_{m-1}}\quad(m\ge1),\qquad D_0=1.}
\tag{2.4}
$$
$m=1$ 时空乘积给 $D_1=1$，与上式一致。

## 3. 保同一实际输入的加权运输证书

给定原向量 $h,g\in H$，在 (1.1) 中写
$$
a_s(z)=|h_s(z)|,\qquad b_r(z)=|g_r(z)|.
$$
设存在有限常数 $K,C$ 及非负可测函数 $\pi_{rs}(z)$，满足 $\pi_{rs}=0$ 当 $r<s$，以及几乎处处的条件
$$
\sum_{s\le r}\pi_{rs}=b_r^2,
\tag{3.1}
$$
$$
\sum_{r\ge s}\pi_{rs}\le K^2a_s^2,
\tag{3.2}
$$
$$
\sum_{r\ge s}d_{rs}^{\,2}\pi_{rs}\le C^2a_s^2.
\tag{3.3}
$$
行质量 (3.1) 是指定输出；(3.2) 支付普通算子范数；(3.3) 支付每一个真实幂比较。没有将目标源任意归一化后再忘记其实际大小。

在 $a_sb_r>0$ 时定义
$$
B_{rs}(z)=
\frac{g_r}{b_r}\,
\frac{\pi_{rs}}{b_ra_s}\,
\overline{\frac{h_s}{a_s}},
\tag{3.4}
$$
其他位置置零。零行、零列与 (3.1)–(3.2) 相容。令 $X$ 为逐尾纤维作用的实际算子 $(Xf)(z)=B(z)f(z)$。

**定理 3.1。** 上述构造满足
$$
\boxed{Xh=g,\qquad\|X\|\le K,\qquad X\in\mathcal D,\qquad c_A(X)\le C.}
\tag{3.5}
$$

**证明。** (3.1) 直接给 $Bh=g$。对任意有限向量 $x$，逐行 Cauchy 不等式给
$$
|(Bx)_r|^2
\le\sum_s\pi_{rs}\frac{|x_s|^2}{a_s^2},
$$
其中零列略去；求和并用 (3.2) 得 $\|B(z)x\|^2\le K^2\|x\|^2$，故 $B$ 是可测且本质有界的算子场。

对 $D_\ell(z)BD_\ell(z)^{-1}$ 作同一个逐行估计，右侧每项多出
$h_\ell(r+Nz)^2/h_\ell(s+Nz)^2$。由 (2.2)、(3.3)，
$$
\|D_\ell(z)B(z)D_\ell(z)^{-1}x\|^2
\le\sum_s\frac{|x_s|^2}{a_s^2}
\sum_r d_{rs}^{\,2}\pi_{rs}
\le C^2\|x\|^2.
$$
各权几乎处处为正；固定 $\ell$ 的零测例外以及全部 $\ell$ 的可数并均可删除。对实际 $L^2$ 输入积分，便是全部 Deddens 不等式。证毕。

特别地，只要 (3.1)–(3.2) 成立，(3.3) 自动可取
$$
C=KD_m.
\tag{3.6}
$$
更细的 (3.3) 可在源列之间分配费用，通常不必让所有边都支付最坏值 $D_m$。这些是关于 $\pi$ 的有限线性约束，允许保留实际 $z$、实际源及目标后优化。

## 4. 准确普通范数插值与更便宜边的可行性

对固定 $m$，存在逐尾纤维下三角算子 $X$，满足 $\|X\|\le K$、$Xh=g$，当且仅当几乎处处对每个 $0\le q<N$ 有
$$
\boxed{\sum_{r=0}^{q}|g_r|^2
\le K^2\sum_{s=0}^{q}|h_s|^2.}
\tag{4.1}
$$
必要性来自 $P_{\le q}X=P_{\le q}XP_{\le q}$。充分性可以直接构造 (3.1)–(3.2)：从 $r=0$ 开始，将第 $r$ 行的需求 $b_r^2$ 分配给尚有容量的列 $s\le r$，每列容量为 $K^2a_s^2$。前面全部行的已用质量为 $\sum_{i<r}b_i^2$；(4.1) 保证当前前缀剩余容量足够。固定列的处理顺序后，每步只用加减和最小值，因此所得 $\pi$ 可测。

定理 3.1 同时说明这个普通范数最优插值可在 $\mathcal D$ 内实现，而且有 (3.6) 的真实成本上界。准确最小普通范数为
$$
K_*=\operatorname*{ess\,sup}_z\max_{0\le q<N}
\left(\frac{\sum_{r\le q}|g_r(z)|^2}
{\sum_{s\le q}|h_s(z)|^2}\right)^{1/2},
\tag{4.2}
$$
约定 $0/0=0$、正数除以零为无穷。若 $K_*<\infty$，上述构造以 $K=K_*$ 达到它，并付 $c_A(X)\le K_*D_m$。

若只允许较便宜的边
$$
\mathcal E_D=\{(r,s):s\le r,\ d_{rs}\le D\},
$$
同样的运输构造在以下有限 Hall 条件下可行：对每个输出指标集合 $J\subseteq\{0,\ldots,N-1\}$，
$$
\sum_{r\in J}b_r^2
\le K^2\sum_{s\in\mathcal N_D(J)}a_s^2,
\qquad
\mathcal N_D(J)=\{s:\exists r\in J,(r,s)\in\mathcal E_D\}.
\tag{4.3}
$$
此时得到 $\|X\|\le K$、$c_A(X)\le KD$。

为完整说明 (4.3)，把源列看成容量 $K^2a_s^2$ 的节点，输出行需求为 $b_r^2$，只沿允许边送非负质量。若最大总运输仍留未付需求，从一个未付输出逆向沿允许边、再沿正流量的反向边找可达集合；其中若有未耗尽的源列，就可沿有限交替路径增流，矛盾。若所有可达源列均已耗尽，其关联的输出集合 $J$ 的需求严格超过可达容量，正好违背 (4.3)。最优流存在，因为有限流多面体闭且有界。可测选取可通过固定所有可能的顶点基次序完成：每个候选顶点为容量和需求的线性函数，在有限个可行最优顶点中选第一个。

这里的 (4.3) 是该运输证书的准确可行性，不宣称它刻画全部可能带相位抵消的 Deddens 插值。

## 5. 对任意指定目标的实际前缀截取

给定同一个输入 $h$、目标 $u$ 及范数预算 $K$，可直接造出满足 (4.1) 的目标 $g$。在每个实际尾纤维上递推
$$
q_r=|u_r|^2,\qquad
b_r^2=\min\left(q_r,
\left[K^2\sum_{s\le r}|h_s|^2-\sum_{i<r}b_i^2\right]_+\right),
\tag{5.1}
$$
并令 $g_r$ 与 $u_r$ 同相位且模为 $b_r$。置
$$
L_m(z)=\max_{0\le q<N}
\left[\sum_{r\le q}|u_r(z)|^2-
K^2\sum_{s\le q}|h_s(z)|^2\right]_+.
\tag{5.2}
$$
逐次记已丢失质量，(5.1) 给准确递推
$$
\sum_{i\le r}(q_i-b_i^2)
=\max_{0\le q\le r}
\left[\sum_{i\le q}q_i-K^2\sum_{s\le q}|h_s|^2\right]_+.
$$
因 $(\sqrt q-\sqrt b)^2\le q-b$ 对 $0\le b\le q$ 成立，故
$$
\boxed{\|g-u\|_2^2\le\int L_m(z)\,d\mu(z),\qquad
g=Xh,\quad\|X\|\le K,\quad c_A(X)\le KD_m.}
\tag{5.3}
$$
这给实际输入上的可检验误差，而不是只用坏集合测度代替原向量质量。

当 $K\|h\|\ge\|u\|$ 时，右侧随 $m\to\infty$ 趋零。证明可直接用低 $p$ 位柱函数 $h^{(p)},u^{(p)}$ 在 $L^2$ 逼近 $h,u$。对 $m\ge p$，其能量序列以 $2^p$ 为周期；每个前缀由若干完整周期和一个不足一周期的尾段组成。因此其归一化前缀亏损最多为
$$
\big(\|u^{(p)}\|^2-K^2\|h^{(p)}\|^2\big)_+
+2^{p-m}\|u^{(p)}\|^2.
$$
换回实际输入和目标，多出的积分误差不超过
$$
\|\,|u|^2-|u^{(p)}|^2\,\|_1
+K^2\|\,|h|^2-|h^{(p)}|^2\,\|_1.
$$
先令 $m\to\infty$ 再令 $p\to\infty$ 即得结论。注意，柱函数仅用于证明误差趋零；实际构造 (5.1)–(5.3) 从始至终使用原 $h,u$。

## 6. 一条始终留在固定非零球内的真实递推

现在不用抽象的存在选择，直接指定全程输出。令 $f_0=\mathbf1$；对 $n\ge1$，令
$$
N_n=2^{m_n}=\min\{2^m:2^m\ge4n\},\qquad a_n=2n-1,
$$
$$
\boxed{f_n(y)=\mathbf1_{\{y\bmod N_n\ge a_n\}}.}
\tag{6.1}
$$
显然
$$
\|f_n-\mathbf1\|^2=\frac{2n-1}{N_n}<\frac12,
\qquad\|f_n\|^2>\frac12.
\tag{6.2}
$$

**定理 6.1。** 存在原模型上的真实有限头下三角算子 $R_n$，使
$$
\boxed{R_nAf_{n-1}=f_n,\qquad
\|R_n\|\le\frac2{\alpha_0},\qquad
c_A(R_n)\le\frac2{\alpha_{m_n-1}}.}
\tag{6.3}
$$
因此 (6.1) 是一条实际可持续递推，而不是逐步更换初始源后得到的一组互不关联的插值。

**证明。** 对真实输入 $h=Af_{n-1}$，每个奇数坐标满足
$$
h(s+N_nz)=\alpha_0 f_{n-1}(s-1+N_nz).
\tag{6.4}
$$
这些实际数值只可能为 $0$ 或 $\alpha_0$，且不依赖尾变量。偶数输入可以非零，也包含真实尾 carry；我们选择的 $R_n$ 将其列置零，因此无需用近似值替换它们。

每个值为 $\alpha_0$ 的奇数源格给予运输容量 $4$，每个目标格 $r\ge a_n$ 给予需求 $1$。这里用未乘 $N_n^{-1/2}$ 的格值；共同归一化因子对 (4.1) 两侧相消。普通范数预算取 $K=2/\alpha_0$。只需检查前缀供给大于等于前缀需求。

$n=1$ 时全部奇数源都可用，结论立即成立。对 $n\ge2$，置 $M=N_{n-1}$，则 $N_n\in\{M,2M\}$，且
$$
M\ge4(n-1).
\tag{6.5}
$$

若 $N_n=M$，可用奇数源恰为 $a_n,a_n+2,\ldots,M-1$。从 $a_n$ 起，任意长度 $d$ 的前缀至少有 $\lceil d/2\rceil$ 个源，容量 $4\lceil d/2\rceil\ge d$。

若 $N_n=2M$，两个旧块中的可用奇数源分别为
$$
a_n,a_n+2,\ldots,M-1,\qquad
M+a_n,M+a_n+2,\ldots,2M-1.
$$
第一段中供给仍足够。第一段之后、第二段首源出现之前的最紧前缀终点是 $q=M+a_n-1$；此时总需求为 $M$，已经获得的总容量为
$$
4\cdot\frac{M-a_n+1}{2}=2M-4n+4\ge M
$$
，最后一步正是 (6.5)。第二段开始后，每两个新输出格至少增加一个容量 $4$ 的源，所以前缀不等式继续成立。

用 §4 的实际运输构造得到有限头矩阵 $B_n$。它仅使用这些真实奇数源，给 $B_n h=f_n$；源和目标在所用坐标上均为常格值，所以 $B_n$ 可取与 $z$ 无关。定理 3.1、(2.4) 给
$$
\|B_n\otimes I\|\le2/\alpha_0,\qquad
c_A(B_n\otimes I)\le(2/\alpha_0)D_{m_n}
=2/\alpha_{m_n-1}.
$$
置 $R_n=B_n\otimes I$ 即得 (6.3)。证毕。

此构造在头翻倍时用第一旧块的真实富余源填补第二旧块前端的旧空洞。它不满足旧“每个保留奇数格只复制到自身及紧随偶数格”的递推公式，因而不能把旧硬复制存活集合公式直接套到这里。可以在满足同一容量约束的多个流之间取凸组合，使输出格混合多个实际源；(3.1)–(3.3) 仍成立。

## 7. 全程成本、已付内容与没有跨过的门

(6.3) 对同一条实际递推逐项给
$$
\sum_{i=1}^n\log c_A(R_i)
\le n\log2+\sum_{i=1}^n L_{m_i-1}.
\tag{7.1}
$$
由于 $2^{m_i-1}<4i$，以及
$L_j\le(280/3)16^j+300\,2^j$，有明确上界
$$
\boxed{\sum_{i=1}^n\log c_A(R_i)
\le n\log2+\frac{71680}{3}\sum_{i=1}^n i^4
+600n(n+1)=O(n^5).}
\tag{7.2}
$$
成本是原 $A$ 的成本；没有换权、换测度或舍弃原尾。普通算子范数统一有界，输出球也固定，与 $n$ 无关。

另一方面，[负幂域与等距共轭](R12-appendix-deddens-negative-domains-and-isometric-conjugation.md) 对任意实际递推给
$$
\|f_n\|\le\beta_n\left(\prod_{i=1}^nc_A(R_i)\right)\|f_0\|.
\tag{7.3}
$$
所以 (6.2) 本来就要求 $\beta_n\prod_i c_A(R_i)>1/\sqrt2$。本稿的五次上界不与此冲突，也没有支付一个低于原四次幂衰减的矛盾性预算。

真正新增的正向内容是：同一实际源上可实施的运输证书；准确最小普通范数及真实 carry 费用；可计算的前缀亏损误差；以及源持续变化时仍能严格实现、统一有界且全程非零的显式递推。便宜边条件 (4.3) 与逐列加权预算 (3.3) 保留了进一步优化真实费用的入口。未知 $A$-不变空间未被这些运输算子证明保持，因此这里没有得到普通不变子空间或完整 ISP 结论。
