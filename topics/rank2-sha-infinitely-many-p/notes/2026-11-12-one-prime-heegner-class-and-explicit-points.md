# 固定辅助二次域上的单素数 Heegner 类与显式点证书

日期：2026-11-12。状态：以下固定辅助域的存在、单素数等价判据、
实际导出点及其局部/P,Q 比较均已证明。
还没有证明该非零判据对无穷多个 $p$ 成立。

## 1. 固定一次辅助域，再让 $p$ 变化

固定本题曲线
$$
E:y^2=x^3-17x,\qquad P=(-1,4),\quad Q=(9,24),
$$
其秩恰为 $2$、根数为 $+1$（R4 和局部输入）。
记其导子为 $N_E$，素因子为 $2,17$。

Bump–Friedberg–Hoffstein（1990），Introduction 的主定理 (i)，
允许指定一个包含全部导子素因子的有限集合 $S$，并得到
一个基本判别式 $D$，满足
$$
D<0,\qquad \text{$S$ 中全部素数在 }F=\mathbb Q(\sqrt D)
\text{ 分裂},\qquad L'(E^D,1)\ne0.
\tag{1}
$$
原定理的符号条件是 $\epsilon D<0$，这里 $\epsilon=+1$；
它适用于平凡 nebentype 的任意偶权新形式，没有非 CM 限制。
取 $S=\{2,17\}$。以后固定这一 $F$，不随 $p$ 重新选择。
由于 $2$ 分裂，$D$ 为奇数、$D\equiv1\pmod8$，且
$F\ne\mathbb Q(i),\mathbb Q(\sqrt{-3})$。
Gross–Zagier–Kolyvagin 给
$$
\operatorname{rank}E^D(\mathbb Q)=1,
\qquad \Sha(E^D/\mathbb Q)\text{有限}.
\tag{2}
$$

考虑固定集合
$$
\mathcal P_F=\{p\ge5:p\nmid17D,
                 \ p\text{ 在 }\mathbb Q(i)\text{ 与 }F\text{ 均分裂}\}.
\tag{3}
$$
它为无穷集合；例如 $p\equiv1\pmod{4|D|}$ 的素数除去有限个
均属于它。这里得到的是无穷个可用的输入素数，
尚没有把它们全部认定为有限 Sha 的输出素数。

### 1.1 CM 情形满足 BCGS 的不可约输入

对每个 $p\in\mathcal P_F$，$E[p]$ 在 $G_{\mathbb Q(i)}$ 上
分解为两个 CM 特征线。在所选 $p$-进惯性群上，一个为模 $p$
cyclotomic 特征，另一个为平凡特征；二者在 $p\ge5$ 时不同。
因此任何 $G_\mathbb Q$ 稳定直线必是其中一条 CM 线。
复共轭交换这两条线，故不存在这样的稳定直线，即
$E[p]$ 是不可约的 $G_\mathbb Q$ 模。

也有 $E(F)[p]=0$。若存在一个非零 $G_F$ 不变向量，因 $G_F$
正规且 $E[p]$ 不可约，其 $G_\mathbb Q$ 轨道张成整个 $E[p]$，
于是全部 $p$-挠点在 $F$ 有理。Weil 配对给
$\mu_p\subset F$，与 $p-1>2$ 矛盾。

所以 BCGS（2026）Theorem A 的第二个无条件情形适用：
其要求的是不可约，不是满 $\mathrm{GL}_2(\mathbb F_p)$ 像。
相反，同文 Theorem B 的 refined primitivity 另要求 surjective，
不能用于本 CM 曲线；以下不使用 Theorem B。

## 2. 最小非零支撑恰为 $1+t_p$

令
$$
t_p=\operatorname{corank}_{\mathbb Z_p}\Sha(E/\mathbb Q)[p^\infty].
$$
由于 $p$ 为奇数，二次扩张的 restriction/corestriction 及
$\frac{1\pm c}{2}$ 分解给
$$
r_p^+(E/F)=2+t_p,\qquad r_p^-(E/F)=1,
\tag{4}
$$
其中第二式使用 (2)，两边分别为完整 $p^\infty$-Selmer 的
复共轭特征空间余秩。

BCGS Theorem A 给实际 Heegner Kolyvagin 系统
$\boldsymbol\kappa^{\rm Heeg}$ 非零。
其 Corollary A 给准确最小支撑式
$$
\operatorname{ord}(\boldsymbol\kappa^{\rm Heeg})
=\max\{r_p^+(E/F),r_p^-(E/F)\}-1=1+t_p.
\tag{5}
$$
这里 $\operatorname{ord}$ 是存在非零导出类的指标 $n$ 所含的
最少不同 Kolyvagin 素数数目，不是整个系统的整除指数。

因此得到一个单素数判据：
$$
\boxed{\quad
\Sha(E/\mathbb Q)[p^\infty]\text{有限}
\ \Longleftrightarrow\
\exists\text{ Kolyvagin 素数 }\ell:
                  \kappa^{\rm Heeg}_\ell\ne0.
\quad}
\tag{6}
$$
左边等价 $t_p=0$，由 (5) 等价最小支撑为 $1$。
反向若已有单素数非零类，则最小支撑至多 $1$，而 (5) 又给
至少 $1$，故 $t_p=0$。

特别地，不能用“整个系统非零”替换 (6)；它只保证最小支撑
是某个有限整数，不把 $1+t_p$ 强制成 $1$。

## 3. 这个类来自哪一个实际代数点

固定一个有理模参数化 $\pi:X_0(N_E)\to E$，取
$\pi(\infty)=O$。设 $F[n]$ 为 $F$ 的导子 $n$ 环类域，
$P[n]=\pi(x_n)\in E(F[n])$ 为标准 Heegner 点。

对素数 $\ell\nmid N_EpD$，要求
$$
\ell\text{ 在 }F\text{ 惰性},\qquad
M_\ell=\min\{v_p(\ell+1),v_p(a_\ell(E))\}>0.
\tag{7}
$$
约定 $v_p(0)=+\infty$。
记 $G_\ell=\operatorname{Gal}(F[\ell]/F[1])$，这是阶
$\ell+1$ 的循环群（$F$ 的单位只有 $\pm1$）。
选生成元 $\sigma_\ell$，置
$$
D_\ell=\sum_{j=1}^{\ell}j\sigma_\ell^j,
\qquad
Y_\ell=\sum_{\tau\in\mathcal C_\ell}
                   \tau D_\ell P[\ell]\in E(F[\ell]),
\tag{8}
$$
其中 $\mathcal C_\ell$ 为
$\operatorname{Gal}(F[\ell]/F)/G_\ell$ 的一组代表。
这是一个有限整数系数和，不是未指定的 Selmer 向量。

群环恒等式
$$
(\sigma_\ell-1)D_\ell
=(\ell+1)-\sum_{j=0}^{\ell}\sigma_\ell^j
\tag{9}
$$
配合 Heegner 点的范数关系，使 $Y_\ell\bmod p^{M_\ell}$
在 Galois 下不变。BCGS §1.1.2、式 (1.3)–(1.4) 及其后构造，
先将这个点的 Kummer 类唯一下降为原始导出类；本篇明确记为
$c^{\rm raw}_\ell$，以区别于满足规范化有限/奇异关系的系统分量。

在本题还可直接检查 $E(F[\ell])[p]=0$。
$F[\ell]/\mathbb Q$ 在 $p$ 和 $2$ 都不分歧；
所以 $p$-惯性仍把一个 CM 线作 cyclotomic 作用、另一个作平凡作用。
任何不变向量只能位于后者。但 $\mathbb Q(i)$ 在 $2$ 分歧，
不能包含于 $F[\ell]$，故 $G_{F[\ell]}$ 还有交换两条 CM 线的元素，
迫使该不变向量为零。
于是 inflation–restriction 给
$$
H^1(F,E[p^M])\xrightarrow{\sim}
H^1(F[\ell],E[p^M])^{\operatorname{Gal}(F[\ell]/F)}
\tag{10}
$$
对所有 $M\ge1$ 成立。

### 3.1 规范系统的修改是可逆映射

BCGS 印刷 p.8 在完成上述下降后还作一次 slight modification。
其准确来源是 Howard（2004）Proposition 1.7.4 与
Theorem 1.7.5（正式发表版 pp.1457–1458）：
若 $I_n=p^{M(n)}\mathbb Z_p$，则存在逐素数构造的可逆映射
$\chi_n$，规范系统为
$$
\kappa'_n=\chi_n^{-1}(c_n^{\rm raw})
             \otimes_{\ell\mid n}\sigma_\ell.
\tag{10a}
$$
$\chi_n$ 是对应全局上同调群的自动同构，不应未经证明把它简写成
乘一个标量单位。对 $n=\ell$，$\sigma_\ell$ 在
$G_\ell/p^{M_\ell}G_\ell$ 中为生成元；张量这一生成元也是同构。
所以准确有
$$
\kappa^{\rm Heeg}_\ell\ne0
\quad\Longleftrightarrow\quad c^{\rm raw}_\ell\ne0.
\tag{10b}
$$

这项构造不以 $\kappa_1$ 非零为前提，也不是将一个非零的
$\kappa_1$ 项加到 $c^{\rm raw}_\ell$ 上。Howard 的局部
$\chi_\ell$ 由约化、投影到 $p$-Sylow 群，再作用
$p^{-M_\ell}(a_\ell-(\ell+1)\operatorname{Fr}_\ell)$ 构成。
在两个 Frobenius 特征分量上它均诱导同构；
Theorem 1.7.5 将这些可逆映射组合成 (10a)。
该局部计算和非零保持不需要满 $\mathrm{GL}_2$ 像。
原文在此使用满像来保证的下降无挠条件，已由本题 (10) 前的
CM/不分歧论证直接给出；BCGS 的不可约版本正使用同一构造。

因此 (6) 成为以下完全等价的代数点问题：
$$
\boxed{\quad
\Sha(E/\mathbb Q)[p^\infty]\text{有限}
\ \Longleftrightarrow\
\exists\ell\text{ 满足 (7)}:
Y_\ell\notin p^{M_\ell}E(F[\ell]).
\quad}
\tag{11}
$$
没有将 $Y_\ell$ 的非扭性误当成 (11) 的不可整除性。
例如一个非扭点仍可能是 $p^{M_\ell}$ 倍点。

## 4. 单素数类的局部条件与下降到 $\mathbb Q$

由于 $\operatorname{ord}_{s=1}L(E,s)\ge2$，而
$\operatorname{ord}_{s=1}L(E^D,s)=1$，有 $L'(E/F,1)=0$。
第一个不等式也可只用已证秩二与 Gross–Zagier–Kolyvagin 的
解析秩至多一情形排除法得到，不需要秩二 BSD。
Gross–Zagier 使基底 Heegner 点
$\operatorname{Tr}_{F[1]/F}P[1]$ 为扭点。
它无 $p$-primary 部分，故整个基底类
$c^{\rm raw}_1=\kappa_1$ 为零。

这里直接在完整模 $p^M$ 层使用 Howard Proposition 1.7.4，
其中 $M=M_\ell$、$\lambda\mid\ell$：
$$
\chi_\ell\bigl(c^{\rm raw}_1(\operatorname{Fr}_\lambda)\bigr)
 =c^{\rm raw}_\ell(\sigma_\ell)=0
 \quad\text{于 }E[p^M].
\tag{12}
$$
Howard Lemma 1.7.3 给 $c^{\rm raw}_\ell$ 在 $\lambda$ 处属于
横截局部条件；其 Proposition 1.1.9 给横截条件到 singular
商的同构。对这里无分歧、模 $p^M$ 上 Frobenius 平凡的系数模，
singular 类由在惯性生成元 $\sigma_\ell$ 上的值确定，
见 Proposition 1.1.7 与 Definition 1.1.8。因此 (12) 推出
$\operatorname{loc}_\ell c^{\rm raw}_\ell=0$。
这是全 $p^M$ 层的关系，不是从模 $p$ 关系提升精度。

所以虽然一般 $n$ 指标类在 $n$ 处采用横截局部条件，
这个原始单素数类在 $\ell$ 处实际为零，其余地方满足通常 Selmer 条件。
复杂共轭的符号为
$$
\epsilon(E)(-1)^{\nu(n)+1};
$$
当 $n=\ell$ 时它为 $+1$。
所以 $c^{\rm raw}_\ell$ 是通常 Selmer 群的正特征类，并唯一下降为
$$
c_{\ell,p}\in\operatorname{Sel}_{p^{M_\ell}}(E/\mathbb Q).
\tag{13}
$$
局部关系和符号是 Heegner 系统的几何性质，不需要 mod $p$ 满像。
局部关系采用上述 Howard 的完整 $I_n$ 版本；
复杂共轭符号可见 Zhang（2014）式 (3.24)。
Zhang 同文式 (8.1) 的模 $p$ 写法没有用于证明全 $p^M$ 断言。

有一个计算上应注意的后果：(12) 说明在辅助素数 $\ell$ 自身
约化这个类不能给出非零证书。若使用局部证书，应选择别的地方。

## 5. 与已知 $P,Q$ 的准确比较及可验证的充分证书

令 $I=[E(\mathbb Q)/E(\mathbb Q)_{\rm tors}:\mathbb ZP+\mathbb ZQ]$。
它是一个固定有限正整数；本篇不需要预先知道它等于 $1$。
对 $p\nmid I$，$P,Q$ 是 $E(\mathbb Q)/p^ME(\mathbb Q)$ 的基。
由 (10) 和 Kummer 单射，(13) 落在有理 Mordell–Weil 子群中
当且仅当存在 $a,b\in\mathbb Z/p^M\mathbb Z$ 使
$$
Y_\ell-aP-bQ\in p^M E(F[\ell]),\qquad M=M_\ell.
\tag{14}
$$
若这样的 $a,b$ 不同时为零，则 $c_{\ell,p}\ne0$，由 (6)、(10b)
已经推出初级有限。
若不预先排除 $p\mid I$，只需把“$a,b$ 不同时为零”改为
“$aP+bQ\notin p^ME(\mathbb Q)$”，同一个充分证书仍成立。

(14) 是真实全局点归属条件。仅在若干有限域中找到同样的
$a,b$，不证明这个全局关系。若该关系失败，$c_{\ell,p}$ 可能
带有 $\Sha[p^M]$ 分量；不能因为它来自扩域中的代数点，就
宣布它来自 $E(\mathbb Q)$。

另有更直接的局部充分证书：取 $F[\ell]$ 的一个好约化有限位
$v\nmid p$，若
$$
\overline{Y_\ell}\notin p^M\widetilde E(k_v),
\tag{15}
$$
则 $Y_\ell$ 不可能在全局为 $p^M$ 倍点，故 (11) 成立。
这里有限群中检验的是实际乘 $p^M$ 的像；不能只检查
$\overline{Y_\ell}\ne O$。同理，任一 $p$-进位的实际局部
Kummer 类非零也足够。
这些首先给出充分证书。
[R104 的进一步比较](2026-11-12-cyclic-heegner-augmentation-and-complete-reduction.md)
使用 split CM 的完整 $H^1(E[p^M])$ 局部核为零，证明这里的好约化证书
实际完备，并可避开任何有限位集合。它不把 $H^1(E)[p^M]$ 中的
Sha 类与其 $E[p^M]$-系数提升的局部行为混同。

## 6. 一个简化的 CM 辅助素数族与剩余任务

若另取 $\ell$ 在 $\mathbb Q(i)$ 中惰性，则 $a_\ell(E)=0$，
于是 (7) 简化为 $\ell\equiv-1\pmod p$ 加两个二次域的惰性条件，
且 $M_\ell=v_p(\ell+1)$。对每个固定 $p\in\mathcal P_F$，
这样的素数由 Chebotarev/Dirichlet 给出无穷多个。
在这组素数上，原范数关系更强地是
$$
\operatorname{Tr}_{F[\ell]/F[1]}P[\ell]=0,
$$
所以 (9) 直接变为
$(\sigma_\ell-1)D_\ell P[\ell]=(\ell+1)P[\ell]$。

本篇只将这组额外受限的 $\ell$ 作为方便的充分证书候选；
没有未经证明把 (6) 中所有 $\ell$ 的存在性收窄到这个子集。
Chebotarev 给的是满足 Frobenius 条件的素数，
不保证真实点 $Y_\ell$ 的不可整除性。

现在 O4 有了可直接攻击的全局问题：固定本篇的 $F$，
对无穷多个 $p\in\mathcal P_F$，证明至少一个 (8) 的点满足
(11)，或构造 (14)/(15) 的证书。
已知 $P,Q$ 的独立性、整个 Kolyvagin 系统非零和辅助素数的
存在性都已经付清；尚缺的是这个单支撑的不可整除性。

## 来源

- D. Bump、S. Friedberg、J. Hoffstein（1990），
  *Nonvanishing theorems for L-functions of modular forms and their derivatives*，
  Inventiones Mathematicae **102**, 543–618；Introduction 主定理 (i)，
  [原论文](https://wstein.org/papers/bib/bump-friedberg-hoffstein-nonvanishing.pdf)。
- A. Burungale、F. Castella、G. Grossi、C. Skinner（2026），
  *Non-vanishing of Kolyvagin systems and Iwasawa theory*，
  [作者终稿，2026-01-02](https://web.math.ucsb.edu/~castella/Kolyvagin.pdf)：
  Theorem A、Corollary A（印刷 pp.2–3），§1.1.2（pp.7–8）。
  Theorem B 的 surjective 假设未用于本文。
- B. Howard（2004），*The Heegner point Kolyvagin system*，
  Compositio Mathematica **140**, 1439–1472，
  [正式发表全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1BF8414258216C1575963BBDA814CB2F/S0010437X04000569a.pdf/the-heegner-point-kolyvagin-system.pdf)，
  DOI 10.1112/S0010437X04000569；
  [作者预印本](https://arxiv.org/pdf/1202.6340)。
  Proposition 1.1.7、Definition 1.1.8、Proposition 1.1.9，
  Lemma 1.7.3、Proposition 1.7.4、Theorem 1.7.5。
  后两条在正式版 pp.1457–1458；它们直接处理 $T/I_nT$，
  给出原始导出类与规范 Kolyvagin 系统之间的可逆比较。
- W. Zhang（2014），*Selmer groups and the indivisibility of Heegner points*，
  Cambridge Journal of Mathematics **2**, 191–253；
  [作者全文](https://math.mit.edu/~wz2113/math/online/Kconj.pdf)，
  式 (3.24)。这里只引用 Heegner 系统的符号，
  不将其需要满像的非消失主定理套到 CM 曲线。
- 固定曲线与 strict Selmer 核：R4、
  [R8](../results/R8-strict-selmer-comparison.md)。
