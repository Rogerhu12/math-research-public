# R114：最小变形给出的固定 CM 同余精确深度

日期：2026-11-12；会话：serre-uniformity-astra-resume2。

**状态：已证明。** 设 $E$ 是 [R19](R19-converse-fermat-fixed-cm.md) 任一实际原始解给出的曲线，原指数为 $p>37$，并令 $A:y^2=x^3-x$。本文证明对每个整数 $n\ge1$，
$$
\boxed{E[3^n]\simeq A[3^n]\quad\Longleftrightarrow\quad
Z\in\mathbb Q^{\times 3^n},}
\tag{114.1}
$$
$$
\boxed{E[p^n]\simeq A[p^n]\quad\Longleftrightarrow\quad
Z\in\mathbb Q^{\times p^{n-1}}.}
\tag{114.2}
$$
所有同构都是相应 $\mathbb Z/\ell^n\mathbb Z[G_{\mathbb Q}]$-模的同构，未要求其 Weil 配对乘数为指定平方类。$Z$ 保留原有符号；由于所有幂指数都是奇数，负号不产生例外。式 (114.2) 在 $n=1$ 时恰为 R19 已证的实际同余，没有把该同余自动提升到 $p^2$。

所用全局输入是已发表的最小、有限平坦变形 $R=T$ 定理。以下逐项核对其条件，特别保留 $2$ 处的完整表示和残余限制不可约性；不是由“特征零只有一个新形式”直接推断任意有限层的唯一性。

## 1. 固定模型及 Tate 惯性的完整描述

R19 给出
$$
E[p]\simeq A[p],\qquad
N_E=32\operatorname{rad}(|Z|),\qquad
\Delta_{\min}(E)=2^\delta Z^p,
\tag{114.3}
$$
其中 $\delta\in\{6,9,12\}$、$|Z|>1$、$(Z,6p)=1$，而且 $E$ 在 $3,p$ 都好约化，在每个 $q\mid Z$ 为乘性约化。这些结论适用于 R19 的全部三族及其符号，不需要另选二次扭曲的全局模型。

固定 $q\mid Z$。若约化非分裂，记 $\eta_q$ 为对应的不分歧二次特征；若分裂，令 $\eta_q=1$。在不分歧二次扭曲成为分裂 Tate 曲线后，记 Tate 参数为 $t_q$。对任意奇素数 $\ell\ne q$，有完整的 Tate 模表示
$$
T_\ell(E)\simeq
\eta_q\otimes
\begin{pmatrix}\chi_\ell&c_{t_q}\\0&1\end{pmatrix}.
\tag{114.4}
$$
这里 $c_{t_q}$ 是 $t_q$ 的 Kummer 扩张类，
$$v_q(t_q)=v_q(\Delta_{\min}(E))=p\,v_q(Z).$$
在惯性群上，$\chi_\ell$ 和 $\eta_q$ 都平凡；选择兼容的根及 Tate 基后，
$$
c_{t_q}|_{I_q}=p\,v_q(Z)\,t_\ell,
\tag{114.5}
$$
其中 $t_\ell:I_q\twoheadrightarrow\mathbb Z_\ell(1)$ 是满射的 $\ell$ 分量 tame 特征。单位部分在最大不分歧扩张中可取所有 $\ell$ 次幂根，因此不影响 (114.5)。特别地，这是整个惯性扩张类的等式，不只是有限像阶的比较。

于是
$$
E[\ell^n]\text{ 在 }q\text{ 不分歧}
\quad\Longleftrightarrow\quad
\ell^n\mid p\,v_q(Z).
\tag{114.6}
$$
因为 $A$ 在所有这些 $q$ 好约化，任意实际同构 $E[\ell^n]\simeq A[\ell^n]$ 必使 (114.6) 成立。这已经证明 (114.1)、(114.2) 的必要方向。对整数 $Z\ne0$，全部素数赋值被一个奇数 $m$ 整除，当且仅当 $Z$ 是有符号的整数 $m$ 次幂；这与 $Z\in\mathbb Q^{\times m}$ 等价。

**扭曲规范。** 上述 $\eta_q$ 仅用于在 $\mathbb Q_q$ 上书写 Tate 模；它在惯性上平凡，且两次扭曲相消。本文后面始终使用原全局曲线 $E,A$ 的表示及共同的行列式 $\chi_\ell$，不把各个 $\eta_q$ 拼成一个未经证明存在的全局扭曲。

## 2. 素数 2 处：相同完整惯性核与局部刚性

### 2.1 任意奇特征中的绝对不可约性

[R22 §4](R22-good-supersingular-symplectic-type.md) 已核实 $A$ 在 $2$ 处的半稳定缺陷为 $8$，有限惯性群为 $Q_8$：可用与 $A$ 有有理 $2$ 同源的
$$B:y^2=x^3-6x^2+x$$
及其 $(c_4,c_6,\Delta)=(528,12096,512)$，直接落入 Freitas–Kraus 的完整惯性表。有理 $2$ 同源对每个奇数挠点层都是同构，故可据此识别 $A$ 的惯性核。

$E$ 在 $2$ 潜在好约化：R19 各模型的 $j$ 在 $2$ 整。其有限惯性群忠实作用在好约化特殊纤维上，阶只可能整除 $24$。由于 $p>37$，约化模 $p$ 在这个有限惯性群上忠实：$\operatorname{GL}_2(\mathbb Z_p)$ 的主同余核为 pro-$p$ 群。式 (114.3) 因而说明，作为 $I_2$ 的商，$E,A$ 的有限惯性核完全相同，商均为 $Q_8$。

这个核不依赖于所取的 Tate 素数：它是曲线在最大不分歧底域上取得好约化所需的惯性核，亦由 Néron–Ogg–Shafarevich 判据刻画。因此对任意奇数 $\ell$，$T_\ell(E),T_\ell(A)$ 的惯性作用均通过这个相同的 $Q_8$，且约化模 $\ell$ 仍忠实。

特征不为 $2$ 时，$Q_8$ 的忠实二维表示绝对不可约。确实，若它在代数闭包上可约，则由 Maschke 定理分解为两个一维特征，而每个一维特征均杀掉交换子 $-1\in Q_8$，与忠实性矛盾。所以 $E[3],A[3],A[p]$ 的全局表示都绝对不可约；这里得到的是实际线性表示的结论。

### 2.2 固定残余同构后，完整局部表示唯一

以下引理将用于 $\ell=3$ 和 $\ell=p$。假设已给定
$$E[\ell]\simeq A[\ell].$$
选择基使该同构为恒等。对每个 $n$，两个 $I_2$-表示的提升可由一个模 $\ell$ 为恒等的矩阵共轭成完全相同。

其证明是逐层的：从模 $\ell^k$ 的一致提升到模 $\ell^{k+1}$ 时，差为
$$H^1(Q_8,\operatorname{End}(\mathbb F_\ell^2))$$
中的一个类；由于 $8$ 可逆，对群作平均使此群为零。所以可逐层选择严格共轭，并得到在每个有限层上的一致惯性表示。

该惯性表示的中心化子只含标量，且此断言在 $\mathbb Z/\ell^n\mathbb Z$ 上成立。若 $R,S$ 分别为四元数生成元的矩阵，则
$$R^2=S^2=-1,\qquad RS=-SR.$$
矩阵 $1,R,S,RS$ 的迹配对对角元为 $2,-2,-2,-2$，非对角元为零；故它们生成整个二阶矩阵代数，中心化子恰为标量环。

对齐惯性后，两个算术 Frobenius 矩阵之比中心化惯性，因此为某个标量 $u$。两个表示的行列式都是圆分特征，故 $u^2=1$。所选残余同构给出 $u\equiv1\pmod\ell$；$\ell$ 为奇数，所以 $u=1$。商 $G_{\mathbb Q_2}/I_2$ 为 procyclic，遂得
$$
\boxed{E[\ell^n]|_{G_{\mathbb Q_2}}
\simeq A[\ell^n]|_{G_{\mathbb Q_2}}\quad(n\ge1).}
\tag{114.7}
$$
因此本文在 $2$ 处使用的有限层变形有固定的完整惯性型和完整不分歧作用。仅有导子指数同为 $5$ 并不足以推出 (114.7)；这里用到了实际残余同构和相同的惯性核。

## 3. 需要的已发表最小变形输入及残余限制

使用 Dieulefait–Taixés i Ventosa，*Congruences between modular forms and lowering the level mod $\ell^n$*，JTNB **21** (2009), 109–118，§3 Theorem 3、§4 Proposition 3 和 Lemma 1。其最小变形问题固定圆分行列式，要求在残余导子外不分歧、坏素数处最小、$\ell$ 处有限平坦，并要求残余表示在
$$L_\ell=\mathbb Q\bigl(\sqrt{(-1)^{(\ell-1)/2}\ell}\bigr)$$
上不可约；$\ell=3$ 的这一附加条件不能略掉。该文从 Diamond、de Shalit 所述的 Taylor–Wiles 定理取得实际环同构 $R^{\min}\simeq\mathbb T^{\min}$。

本题可直接验证更强的绝对不可约性。$L_\ell$ 的基本判别式为 $(-1)^{(\ell-1)/2}\ell$，故在 $2$ 不分歧，因此
$$I_2\subset G_{L_\ell}.$$
残余 $I_2$ 像为上一节的忠实 $Q_8$，在任意奇特征绝对不可约。于是
$$\bar\rho_{A,\ell}|_{G_{L_\ell}}\quad\text{绝对不可约}$$
对 $\ell=3,p$ 分别成立。这既核对了 $\ell=3$ 的特殊条件，也不需要把原 $p$ 的情形从 $3$ 的情形形式套用。

残余导子准确为 $32$。在 $2$，惯性像阶与 $\ell$ 互素，同一分歧滤过及其不变维数在约化前后保持，故 Artin 导子指数仍为 $5$；其余 $q\ne\ell$ 处 $A$ 好约化。因此该最小 Hecke 代数位于权 $2$、平凡特征、层 $32$ 的空间中。R19 的亏格计算给
$$\dim S_2(\Gamma_0(32))=1,$$
且其归一化新形式 $f_A$ 的全部系数在 $\mathbb Z$。所以
$$
\mathbb T^{\min}=\mathbb Z_\ell,\qquad
\boxed{R^{\min}=\mathbb Z_\ell.}
\tag{114.8}
$$
更具体地，$\mathbb T^{\min}$ 作为同余分量嵌入唯一系数环 $\mathbb Z_\ell$，并含有底环 $\mathbb Z_\ell$，故等号成立；随后使用完整 $R=T$，而非只比较两环的特征零点。故没有被遗漏的非平坦分量、幂零方向或 $\ell$ 挠元。

固定残余表示及其基后，任何满足这组变形条件、系数为 $\mathbb Z/\ell^n\mathbb Z$ 的提升都由一个 $\mathbb Z_\ell$-代数映射
$$R^{\min}\longrightarrow\mathbb Z/\ell^n\mathbb Z$$
给出。由 (114.8) 只有通常的约化映射，所以该有限层表示与 $A[\ell^n]$ 严格等价。这里环是 $\mathbb Z_\ell$，不需要对任意分歧系数环的自同态作额外唯一性断言。

## 4. $3^n$：初始降层、有限平坦与全部有限层

假设 $Z\in\mathbb Q^{\times3^n}$，其中 $n\ge1$。先证明真正的初始同构 $E[3]\simeq A[3]$。

第 2.1 节已给出 $E[3]$ 绝对不可约。$E$ 的模性及式 (114.6) 说明该表示来自权 $2$、平凡特征的模形式，并在所有 $q\mid Z$ 不分歧。Ribet (1990) Theorem 1.1 允许残余特征 $3$；删除 $q\parallel N_E$ 时，因 $3\nmid N_E$，即使 $q\equiv1\pmod3$ 也满足其另一分支。逐个降层到 $32$，唯一形式只能是 $f_A$，所以
$$E[3]\simeq A[3].$$
两边在 $\mathbb F_3$ 上定义并绝对不可约，故在代数闭包上得到的同构下降至 $\mathbb F_3$。这也独立补强了原[模三桥接笔记](../notes/2026-11-12-global-cube-and-three-congruence.md)。

现考虑实际 $E[3^n]$：

1. 由 (114.6) 和 $3^n\mid v_q(Z)$，它在每个 $q\mid Z$ 不分歧；其余 $q\notin\{2,3\}\cup\operatorname{Supp}(Z)$ 本来好约化。所以它仅在 $2,3$ 可能分歧。
2. 在 $2$，第 2.2 节给与 $A[3^n]$ 相同的完整局部表示，特别满足最小变形条件。
3. 在 $3$，R19 的原整模型判别式是 $3$-进单位，因此 $E$ 延拓为 $\mathbb Z_3$ 上的光滑椭圆概形。其 $[3^n]$ 核是有限平坦群概形，generic fibre 恰为实际 $E[3^n]$；其 $\mathbb Z/3^n\mathbb Z$ 模为自由秩二。故满足定理要求的 flat 条件，而非只声称模三的 Serre 权为 $2$。
4. 行列式是模 $3^n$ 圆分特征，残余限制不可约性由第 3 节给出。

因此 $E[3^n]$ 是 (114.8) 的最小有限平坦变形，必与 $A[3^n]$ 同构。这证明 (114.1) 的充分方向，对所有 $n$ 同时成立。

## 5. 原 $p^n$：独立核对特征素数处

现在假设 $Z\in\mathbb Q^{\times p^{n-1}}$。初始同构已经是 R19 的 $E[p]\simeq A[p]$。其残余导子准确为 $32$，绝对不可约且限制到 $G_{L_p}$ 仍绝对不可约，均已在第 2–3 节由惯性 $Q_8$ 逐项核清。

对每个新增乘法素数 $q\mid Z$，
$$p^n\mid p\,v_q(Z),$$
故 (114.6) 给出 $E[p^n]$ 在 $q$ 不分歧。其他非 $2,p$ 素数好约化；在 $2$ 由 (114.7) 得到完整最小局部型。

在这里的特征素数 $p$，使用的是 R19 的 $(Z,p)=1$ 和实际极小判别式，而不是从 $E[p]\simeq A[p]$ 推测 $E$ 的约化。式 (114.3) 直接给 $p\nmid\Delta_{\min}(E)$，所以 $E$ 在 $p$ 好约化，且其光滑模型的 $[p^n]$ 核为 $\mathbb Z_p$ 上有限平坦群概形。$A$ 在 $p$ 也好约化；对 $p\equiv3\pmod4$ 它是超奇异，但所用 flat 变形定理同时包含这一情形，不要求 ordinary。

因此，$E[p^n]$ 具有固定圆分行列式、仅 $2,p$ 分歧、$2$ 处最小和 $p$ 处有限平坦，满足第 3 节的完整条件。$R^{\min}=\mathbb Z_p$ 迫使 $E[p^n]\simeq A[p^n]$。结合第 1 节，(114.2) 得证。

## 6. 精确深度与边界

因为 $|Z|>1$，下列最小值都取自非空有限集合：
$$
d_3(E,A)=\min_{q\mid Z}v_3\bigl(v_q(Z)\bigr),\qquad
d_p(E,A)=1+\min_{q\mid Z}v_p\bigl(v_q(Z)\bigr).
\tag{114.9}
$$
其中 $d_\ell(E,A)$ 表示使 $E[\ell^n]\simeq A[\ell^n]$ 成立的最大 $n\ge0$，$n=0$ 为空条件。式 (114.1)–(114.2) 证明 (114.9) 是准确等式。因此第一个同余失效的有限层，恰由至少一个新增乘法素数处的实际 Tate 惯性首先出现检测出来；这不是对一个预选素数的经验观察。

这给出全局高次同构的充要算术条件，仍不提供变化 $Z,p$ 的绝对排除。具体地：

- $Z$ 为立方只给 $E[3]\simeq A[3]$；除非再证明 $Z$ 为九次幂，否则不能使用九级同构。
- $Z$ 为九次或二十七次幂时，确有对应的实际同构，可进入固定的九级或二十七级模曲线问题。本文没有将某个未解决的有理点问题当成已证的全局排除。
- RSZB 的已发表三进像分类保留“像包含于 $N_{\rm ns}(27)$”这一类；不能把它误读为只保留某一个精确开子群，再据此宣称 $N_{\rm ns}(81)$ 已被排除。
- R19 只保证 $d_p\ge1$。若某个 $q\mid Z$ 的指数 $v_q(Z)$ 不被 $p$ 整除，则准确有 $d_p=1$，所以此前任何模 $p$ Selmer 或局部计算都不能直接用于假定的全 $p$ 进 CM 同构。

## 7. 主来源

1. L. Dieulefait、X. Taixés i Ventosa，*Congruences between modular forms and lowering the level mod $\ell^n$*，Journal de Théorie des Nombres de Bordeaux **21** (2009), 109–118，§3 Theorem 3、§4 Proposition 3 和 Lemma 1。[出版记录及 DOI](https://www.numdam.org/item/JTNB_2009__21_1_109_0/)，[作者全文](https://arxiv.org/pdf/0801.0104)，PDF 第 7–8 页。本轮直接核读全部变形条件和 $\ell=3$ 的限制不可约条件。本文只用其已发表的最小变形环定理，不把只删一个素数的 Corollary 2 在未知唯一性的中间层上迭代。
2. K. A. Ribet，*On modular representations of $\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)$ arising from modular forms*，Inventiones Mathematicae **100** (1990), 431–476，Theorem 1.1。[作者全文](https://math.berkeley.edu/~ribet/Articles/invent_100.pdf)。初始模三降层与 R19 使用同一已核定理。
3. N. Freitas、A. Kraus，*On the symplectic type of isomorphisms of the $p$-torsion of elliptic curves*，Memoirs AMS **277**, no. 1361 (2022)，有关 $2$ 处半稳定缺陷及完整惯性表。[作者全文](https://arxiv.org/pdf/1607.01218)。$A$ 的 $Q_8$ 识别和具体表行已在 R22 §4 展开；本篇其余有限群及局部刚性步骤均给出了证明。

固定 CM 的最终同余排除和 Serre 一致性主目标仍未完成。
