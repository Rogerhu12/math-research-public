# R128：全部奇数层的同余深度与分裂素数幂分母排除

日期：2026-11-12；会话：serre-uniformity-astra-resume2。

**状态：已证明。** 本文始终讨论 R19 的实际原始解及其非 CM 曲线
$$E/\mathbb Q,\qquad E[p]\simeq A[p],\qquad
A:y^2=x^3-x,\qquad p>37.$$
令
$$g=g(Z)=\gcd_{q\mid Z}v_q(Z),\qquad |Z|>1.$$
这里对有限非空的分母素数集合取正整数最大公约数，保留 $Z$ 的符号。

得到三个结论：

1. $g$ 是奇数，且它的每个素因子都模四余三。特别，**不存在 $Z$ 为任意素数 $\ell\equiv1\pmod4$ 次幂的实际解**；这同时排除第五、十三、十七、二十九、三十七次幂等全部相应分支，不限制 $\ell$ 的大小，也不预先假设 $\ell\nmid Z$。
2. $\gcd(g,Z)=1$。
3. 对每个正奇数 $m$，有精确充要条件
   $$\boxed{E[m]\simeq A[m]\quad\Longleftrightarrow\quad m\mid pg.}\tag{128.1}$$

所有同构均为实际 Galois 模同构，不固定 Weil 配对乘数。第三条推广 R114 的 $3^n$、$p^n$ 深度，第一条则使用 Lemos 已发表的双 Cartan 定理产生新的全参数排除。本文没有排除 $g=1,3$ 或具有变化的模四余三素因子的分母，因而不是 O6 或主问题的完成。

## 1. 固定的完整二进型

R19 给出
$$
N_E=32\operatorname{rad}|Z|,\qquad
\Delta_{\min}(E)=2^\delta Z^p,\qquad
\delta\in\{6,9,12\},\qquad (Z,6p)=1.
\tag{128.2}
$$
$E$ 在每个 $q\mid Z$ 为乘性约化，在其余非二素数处好约化。

R114 §2 已从实际 $E[p]\simeq A[p]$ 证明以下与辅助奇素数无关的事实。$E,A$ 在二处潜在好约化，完整有限惯性商及惯性核相同，商为 $Q_8$。原因是潜在好约化椭圆曲线的有限惯性群阶整除 $24$，原 $p>37$，所以模 $p$ 约化在该有限群上忠实；好约化扩张的惯性核不依赖 Tate 素数。

对任意奇素数 $\ell$，模 $\ell$ 的惯性作用仍忠实。特征不为二时，$Q_8$ 的忠实二维表示绝对不可约：Maschke 分解若由一维特征组成，就会杀掉交换子 $-1$。因此
$$\bar\rho_{E,\ell}\text{ 绝对不可约，且奇。}\tag{128.3}$$
同一有限惯性商、同一分歧滤过及同一忠实二维角色还给出二处的 Artin 导子指数准确为五。这里不只比较两个整数导子，也没有假定所有残余特征的惯性自然相同而不证明。

## 2. 允许辅助素数本身除分母的初始降层

### 引理 128.2

若奇素数 $\ell$ 满足 $\ell\mid pg$，则
$$E[\ell]\simeq A[\ell].\tag{128.4}$$

当 $\ell=p$ 时这是已知实际同余。以下令 $\ell\ne p$，所以 $\ell\mid g$，即所有 $v_q(Z)$ 被 $\ell$ 整除。

### 2.1 非特征素数处

对 $q\mid Z$ 且 $q\ne\ell$，Tate 惯性公式为
$$
\bar\rho_{E,\ell}|_{I_q}\sim
\begin{pmatrix}1&p\,v_q(Z)\,t_\ell\\0&1\end{pmatrix}
\pmod\ell .
$$
因此该处不分歧。非分裂乘法只引入未分歧二次扭曲，不改变这项计算。结合第 1 节，$\bar\rho_{E,\ell}$ 的素于 $\ell$ 的 Artin 导子准确为
$$N(\bar\rho_{E,\ell})=32.\tag{128.5}$$

### 2.2 特征素数处：好约化和乘法两种情形

若 $\ell\nmid Z$，则 $E$ 在 $\ell$ 好约化，实际 $E[\ell]$ 是光滑整模型上有限平坦群概形的 generic fibre。

若 $\ell\mid Z$，则仍不能称 $E$ 好约化或称 $E[\ell]$ 在 $\ell$ 不分歧。此时先作未分歧二次扭曲，取分裂 Tate 参数 $t$。由
$$v_\ell(t)=p\,v_\ell(Z)\equiv0\pmod\ell$$
可写
$$t=\ell^{\ell a}u,\qquad u\in\mathbb Z_\ell^\times.$$
Tate 扩张
$$0\longrightarrow\mu_\ell\longrightarrow E[\ell]
\longrightarrow\mathbb Z/\ell\longrightarrow0$$
的 Kummer 类在 $\mathbb Q_\ell^\times/(\mathbb Q_\ell^\times)^\ell$ 中等于 $u$。该类有明确的有限平坦模型：
$$
\mathcal G_u=
\coprod_{i=0}^{\ell-1}
\operatorname{Spec}\mathbb Z_\ell[X]/(X^\ell-u^i).
\tag{128.6}
$$
每个分支自由秩 $\ell$，$u$ 为单位。两个分支的群律把 $(i,X),(j,Y)$ 送到
$$
\begin{cases}(i+j,XY),&i+j<\ell,\\
(i+j-\ell,XY/u),&i+j\ge\ell.
\end{cases}
$$
这正是 Kummer 扩张，核为 $\mu_\ell$，商为常值 $\mathbb Z/\ell$；结合律及逆元由进位规则直接验证。非分裂乘法的未分歧二次扭曲可作有限 étale 下降，仍为有限平坦群概形。

所以不论 $\ell$ 是否除 $Z$，实际局部表示均有限平坦。其行列式为 $\chi_\ell$，由 Serre 1987 §2.8 Proposition 4 得准确的 Serre 权
$$k(\bar\rho_{E,\ell})=2.\tag{128.7}$$
该文 §2.9 Proposition 5 也直接写出乘法情形的判据：$\ell\mid v_\ell(j)$ 时权二，否则权 $\ell+1$。这里没有把两种权混同，也没有误用只许在 $q\ne\ell$ 降层的版本。

### 2.3 最优级权与平凡特征

应用已发表的完整 Serre 模性定理，即 Khare–Wintenberger 的最优级权结论（含偶导子的 §9 Theorem 9.1，所需 H 由 Kisin 已证明）。由 (128.3)、(128.5)、(128.7)，$\bar\rho_{E,\ell}$ 来自
$$S_2(\Gamma_1(32)).$$
不能仅引用该文限奇导子的 Theorem 1.2(1) 来处理 $32$。

设所给特征零新形式的 nebentypus 为 $\varepsilon$。权二行列式公式及 $\det\bar\rho_{E,\ell}=\chi_\ell$ 给 $\bar\varepsilon=1$。模 $32$ 的 Dirichlet 字符阶为二的幂；在奇剩余特征中，这些单位根的约化是忠实的。因此 $\varepsilon=1$，实际形式属于
$$S_2(\Gamma_0(32)).$$
该空间维数恰为一，唯一归一化新形式是 $f_A$。于是得到 (128.4)；双方在 $\mathbb F_\ell$ 上定义且绝对不可约，同构下降到 $\mathbb F_\ell$。引理得证。

## 3. 全部模四余一素数幂排除

假设某个素数 $\ell\equiv1\pmod4$ 整除 $g$。第 2 节给 $E[\ell]\simeq A[\ell]$，没有留下 $\ell\mid Z$ 的例外。

$A$ 的几何端同态 $[i]$ 在 $\mathbb Q(i)$ 定义，并满足 $[i]^2=-1$。由于 $\ell\equiv1\pmod4$，$T^2+1$ 在 $\mathbb F_\ell$ 中有两个互异根；故 $A[\ell]$ 有 $[i]$ 的两条不同本征线。任意 $\sigma\in G_\mathbb Q$ 把 $[i]$ 共轭到 $[i]$ 或 $[-i]$，所以置换这两条线。这严格证明
$$\operatorname{im}\bar\rho_{A,\ell}\subseteq N_{\rm split}(\ell),$$
无需证明像等于完整正规化子，也不需要选择 Weil 配对乘数。

Lemos，*Some cases of Serre's uniformity problem*，Math. Z. **292** (2019)，Theorem 1.4 适用于任意这样的辅助素数：非 CM 的 $E/\mathbb Q$ 只要有一个模素数像包含于分裂 Cartan 正规化子，其每个模 $p>37$ 表示都满射。这与本题实际 $E[p]\simeq A[p]$ 矛盾。

因此
$$\boxed{\ell\equiv1\pmod4\Longrightarrow\ell\nmid g.}\tag{128.8}$$
R37 §6.5 已排 $Z$ 为正平方或负平方，故 $2\nmid g$。所以 $g$ 的全部素因子都模四余三。

特别，$Z=Y^5$ 的整个实际分支在每个 $p>37$ 均不存在。这里不是只有“存在一个足够大的 $p$ 界”，也不是把有限参数搜索写成全局排除。

## 4. 幂指数与底数互素

若素数 $\ell$ 同时整除 $g$ 与 $Z$，第 3 节迫 $\ell\equiv3\pmod4$，且 (128.4) 成立。$\ell=3$ 与原条件 $(Z,6p)=1$ 矛盾，故可取 $\ell\ge7$。

$A$ 在 $\ell$ 好超奇异约化：$\ell$ 在其 CM 域 $\mathbb Q(i)$ 惰性。在绝对分歧指数一的 $\mathbb Q_\ell$ 上，好超奇异曲线的模 $\ell$ 惯性半单化是第二层基本字符
$$\psi,\psi^\ell,\qquad \psi(I_\ell)=\mathbb F_{\ell^2}^\times.$$
该二维表示在 $\mathbb F_\ell$ 上不可约。相反，$E$ 在 $\ell\mid Z$ 乘性约化，Tate 表示有实际 $\mathbb F_\ell$ 不变直线；未分歧二次扭曲不改变这一点。因此两者的局部模 $\ell$ 表示不可能同构。

这与 (128.4) 矛盾，所以
$$\boxed{\gcd(g,Z)=1.}\tag{128.9}$$

这个推论并非在第 2 节降层前作的隐藏假设。必须先处理有限平坦的坏特征素数，才能推导出它。

## 5. 任意奇素数幂的准确深度

固定奇素数 $\ell$ 和 $n\ge1$。证明
$$
\boxed{E[\ell^n]\simeq A[\ell^n]
\quad\Longleftrightarrow\quad
\ell^n\mid pg.}
\tag{128.10}
$$

### 5.1 必要性

先说明如果 $E[\ell]\simeq A[\ell]$，就必有 $\ell\nmid Z$。当 $\ell\equiv1\pmod4$，第 3 节的 Lemos 论证已经排除该同构本身；当 $\ell\equiv3\pmod4$ 且 $\ell\mid Z$，第 4 节的超奇异/乘法惯性矛盾同样直接排除该同构，不需假设 $\ell\mid g$。$\ell=3,p$ 本来不除 $Z$。

于是实际同构 $E[\ell^n]\simeq A[\ell^n]$ 使所有 $q\mid Z$ 都满足 $q\ne\ell$。$A$ 在这些 $q$ 好约化，R114 的完整 Tate 惯性式给
$$
\ell^n\mid p\,v_q(Z)\quad\text{对每个 }q\mid Z.
$$
取最大公约数，即 $\ell^n\mid pg$。

### 5.2 充分性：逐项使用同一最小变形环

假设 $\ell^n\mid pg$。若 $\ell=p$，原条件 $p\nmid Z$；否则 $\ell\mid g$，(128.9) 给 $\ell\nmid Z$。所以此时 $E,A$ 在 $\ell$ 都好约化，且 (128.4) 已给初始残余同构。

实际 $E[\ell^n]$ 满足：

- 每个 $q\mid Z$ 的 Tate 惯性类为 $p\,v_q(Z)t_\ell$，被 $\ell^n$ 整除，故在所有新增乘法素数不分歧。
- 在二处，R114 §2.2 的严格局部刚性对任意奇 $\ell$ 同样适用：$8$ 可逆使 $Q_8$ 提升的 $H^1$ 为零；忠实表示的中心化子只有标量；行列式相同与残余同构把 Frobenius 的标量差从 $\{\pm1\}$ 固定为 $1$。所以完整局部型与 $A[\ell^n]$ 相同。
- 在 $\ell$，好约化整模型的 $[\ell^n]$ 核有限平坦，generic fibre 正是这个实际自由秩二模。
- 行列式为模 $\ell^n$ 圆分特征。

残余限制的绝对不可约性也逐项成立。令
$$L_\ell=\mathbb Q\bigl(\sqrt{(-1)^{(\ell-1)/2}\ell}\bigr).$$
其基本判别式为奇数，故在二处不分歧，$I_2\subset G_{L_\ell}$；忠实 $Q_8$ 已使限制绝对不可约。这包括 $\ell=3$，没有遗漏小特征条件。

故可以应用 R114 已核的 Dieulefait–Taixés i Ventosa 最小有限平坦变形定理。残余导子 $32$、权二、固定圆分行列式的 Hecke 代数只有唯一形式 $f_A$，因而
$$R^{\min}=\mathbb T^{\min}=\mathbb Z_\ell.$$
这是完整的环同构，非仅比较特征零新形式数目。到 $\mathbb Z/\ell^n$ 的结构映射唯一，得到 $E[\ell^n]\simeq A[\ell^n]$。充分性得证。

### 5.3 合成全部奇数层

对于任意正奇数 $m$，中国剩余分解把实际 $m$ 挠点 Galois 模分解为各 $\ell^{v_\ell(m)}$ 初等部分。各初等部分的同构可直接合成，不固定配对类型不引入额外相容条件。因此 (128.10) 等价于 (128.1)。

特别，全部奇素数的最大深度统一为
$$d_\ell(E,A)=v_\ell(pg),$$
而不仅是 $3$ 与原 $p$ 两个方向。

## 6. 与主目标的边界

对任意实际解可写唯一的有符号形式
$$Z=Z_0^g,\qquad \gcd_{q\mid Z_0}v_q(Z_0)=1.$$
本结果给 $g$ 奇、全部素因子模四余三、$\gcd(g,Z_0)=1$，并识别准确的最大奇数同余层 $pg$。

R126 先给九次幂支的绝对有限 $p$ 界，R127/R129 继而完整分类固定曲线的全部有理点，把该支加强为全部 $p>37$ 的明确排除。因此现在可无条件断言 $9\nmid g$。这不限制 $Z_0$ 的高度、支撑或类群，也不排除 $g=1$ 和 $g=3$；变化的更大模四余三素因子同样仍需全局论证。

本篇没有把“对每个固定额外层有有限多个有理点”变成“对所有变化层有统一有限集合”。下一项仍是这些真正存活的非九次幂分支。

## 7. 已核原始来源

- J.-P. Serre，*Sur les représentations modulaires de degré 2 de Gal(Q/Q)*，Duke Math. J. **54** (1987)，179–230；§2.8 Proposition 4、§2.9 Proposition 5（印刷页189–191）。[作者原文](https://www.college-de-france.fr/media/jean-pierre-serre/UPL5835292064138487263_Serre_Repr.modulaires_Galois.pdf)。这里只引用局部权与有限平坦的已证判据，不将该文当年的全局猜想当作当年已证定理。
- C. Khare、J.-P. Wintenberger，*Serre's modularity conjecture (I)*，Invent. Math. **178** (2009)，485–504；§1 最优级权定义、§9 Theorem 9.1、§10.1 完整依赖说明。[作者原文](https://www.math.ucla.edu/~shekhar/papers/results.pdf)。
- M. Kisin，*Modularity of 2-adic Barsotti–Tate representations*，Invent. Math. **178** (2009)，587–634；Theorem 0.1、Corollary 0.2，完成前项的 H。[出版原文](https://link.springer.com/article/10.1007/s00222-009-0207-5)。此处使用已经完成的完整 Serre 模性定理，不能只列限奇导子的 KW Theorem 1.2。
- P. Lemos，*Some cases of Serre's uniformity problem*，Math. Z. **292** (2019)，739–762；Theorem 1.4，及其整性接口 Proposition 1.5。[出版原文](https://link.springer.com/article/10.1007/s00209-018-2189-8)。定理中的辅助素数没有大小限制。
- L. Dieulefait、X. Taixés i Ventosa，*Congruences between modular forms and lowering the level mod \(\ell^n\)*，JTNB **21** (2009)，109–118；Theorem 3、Proposition 3、Lemma 1。[出版记录](https://www.numdam.org/item/JTNB_2009__21_1_109_0/)，[作者原文](https://arxiv.org/pdf/0801.0104)。准确最小条件及二处刚性详见 R114。
- 本题 R19、R37、R114、R126–R127、R129。本文的初始特征素数有限平坦模型、nebentypus 下降及精确全奇数层组合均已在正文给出。
