# R17：固定 CM 同余中新乘法素数的精确 Selmer 局部条件

日期：2026-11-12。会话：serre-uniformity-astra-cont。

**状态：已证明的结构定理；中间进展。** 在 R13 的实际全局同余假设下，非分裂乘法素数不改变通常的 $p$-Selmer 局部条件；每个分裂乘法素数只造成一个维度的局部差异。本结果明确了通过 Selmer 群排除分母的路线需要什么额外输入，不证明非 CM 同余曲线存在或不存在。

## 1. 全局陈述

固定
$$
A:y^2=x^3-x,\qquad p>37,\quad p\equiv3\pmod4,
\qquad \phi:E[p]\xrightarrow{\sim}A[p].
$$
这里 $\phi$ 是实际的 $G_{\mathbb Q}$-模同构。用它把两条曲线的模 $p$ 表示都识别为 $V$，并记
$$
T=\{q:v_q(j(E))<0\},\qquad
S=\{q\in T:E/\mathbb Q_q\text{ 为分裂乘法约化}\}.
$$
必须区分“$q$ 在 CM 域 $\mathbb Q(i)$ 中分裂”和“$E$ 在 $q$ 有分裂乘法约化”；以下 $S$ 指后者。

对每个位置 $v$，定义 Kummer 局部条件
$$
\mathcal L_v(B)=\operatorname{im}\left(B(\mathbb Q_v)/pB(\mathbb Q_v)
\longrightarrow H^1(\mathbb Q_v,B[p])\right),\quad B=E,A.
$$
通过 $\phi$ 将它们都视为 $H^1(\mathbb Q_v,V)$ 的子空间。

**定理 R17。**

1. 对每个 $v\notin S$，有 $\mathcal L_v(E)=\mathcal L_v(A)$。
2. 对每个 $q\in S$，有
   $$
   \dim\frac{\mathcal L_q(E)}{\mathcal L_q(E)\cap\mathcal L_q(A)}
   =\dim\frac{\mathcal L_q(A)}{\mathcal L_q(E)\cap\mathcal L_q(A)}=1.
   \tag{17.1}
   $$
3. 令 $W_E=\operatorname{Sel}_p(E/\mathbb Q)$、$W_A=\operatorname{Sel}_p(A/\mathbb Q)$，均嵌入 $H^1(\mathbb Q,V)$。则
   $$
   \dim(W_E/(W_E\cap W_A))\le |S|,
   \qquad \dim(W_A/(W_E\cap W_A))\le |S|,
   \tag{17.2}
   $$
   特别地 $|\dim W_E-\dim W_A|\le |S|$。
4. 若所有新增乘法素数都为非分裂乘法约化，即 $S=\varnothing$，则 $\phi$ 诱导实际子空间的等式
   $$\operatorname{Sel}_p(E/\mathbb Q)=\operatorname{Sel}_p(A/\mathbb Q).
   \tag{17.3}$$

这里没有假设 $\phi$ 保 Weil 配对。结论只比较 Kummer 子空间；任何给定的 Galois 同构都适用。

## 2. 新乘法素数处的完整表

R13 给出：$T$ 不含 $2,3,p$，$E$ 在每个 $q\in T$ 有乘法约化，$V$ 不分歧，$q\equiv\pm1\pmod p$，而对应 Tate 参数 $t_E\in\mathbb Q_q^{\times p}$。令 $s_q=1$ 表示分裂、$s_q=-1$ 表示非分裂，记 $F$ 为算术 Frobenius。

Tate 描述及其分裂给出
$$
V\simeq C_q\oplus Q_q,\qquad
C_q=\mu_p\otimes\nu_q,\quad Q_q=\mathbb F_p\otimes\nu_q,
\quad \nu_q(F)=s_q.
\tag{17.4}
$$
所以 $F$ 在两条线上的特征值分别为 $s_q q,s_q$。$C_q$ 是曲线 $E$ 的 Tate 规范子群，不仅是任意选择的特征线。

下表中 $H^1_{\rm ur}$ 表示不分歧上同调；“交”是两条曲线的 Kummer 条件之交。

| $q\bmod p$ | $E$ 的乘法型 | $F$ 在 $V$ 上的像 | $\dim\mathcal L_q(A)$ | $\dim\mathcal L_q(E)$ | 交的维数 |
|---|---|---|---|---|---|
| $-1$ | 非分裂 | 特征值 $1,-1$ | $1$ | $1$，同一不分歧直线 | $1$ |
| $-1$ | 分裂 | 特征值 $-1,1$ | $1$ | $1$，另一条有分歧直线 | $0$ |
| $1$ | 非分裂 | $-I$ | $0$ | $0$ | $0$ |
| $1$ | 分裂 | $I$ | $2$ | $2$ | $1$ |

最后一行的 $C_q$ 不能从标量 Frobenius 的特征值单独恢复，但交的维数仍恒为 $1$。

## 3. 一个局部上同调计算

令 $K$ 为剩余特征 $q\ne p$ 的局部域，剩余域大小为 $Q$，$M$ 为不分歧的有限维 $\mathbb F_p$-表示，Frobenius 算子为 $F$。温和惯性的最大 pro-$p$ 商是 $\mathbb Z_p(1)$，野惯性无正次数的 $p$-上同调。由惯性正合列的 Hochschild–Serre 序列及不分歧 Galois 群的 $p$-上同调维数为 $1$，得到
$$
0\longrightarrow M/(F-1)M
\longrightarrow H^1(K,M)
\longrightarrow \{m\in M:Fm=Qm\}
\longrightarrow0.
\tag{17.5}
$$
左边的像正是 $H^1_{\rm ur}(K,M)$。右端的条件来自算术 Frobenius 对温和惯性生成元作用为 $Q$ 次幂：一个惯性同态由其生成元值 $m$ 决定，Frobenius 不变性恰为 $Fm=Qm$。

因此对一维不分歧表示，$F$ 以 $\lambda\in\mathbb F_p^\times$ 作用时，
$$
\dim H^1_{\rm ur}(K,M)=\mathbf1_{\lambda=1},\qquad
\dim H^1(K,M)=\mathbf1_{\lambda=1}+\mathbf1_{\lambda=Q}.
\tag{17.6}
$$
这只给正合列，不声称一般存在规范的“不分歧加温和”直和分解。在 $Q=-1$ 且 $V$ 的两个 Frobenius 特征值不同的情形，表示本身的直和分解会给出所需的两条规范上同调直线。

## 4. Tate 曲线的 Kummer 像等于规范子群的上同调像

在 (17.4) 的条件下，有
$$
\mathcal L_q(E)=\operatorname{im}\left(H^1(\mathbb Q_q,C_q)
\longrightarrow H^1(\mathbb Q_q,V)\right).
\tag{17.7}
$$
由于 (17.4) 分裂，右侧映射单射。

### 4.1 分裂乘法型

Tate 一致化给出 $E(K)=K^\times/t_E^{\mathbb Z}$。乘 $p$ 的 Kummer 映射由 $K^\times$ 上的通常 Kummer 映射及 $\mu_p\hookrightarrow E[p]$ 诱导。通常 Kummer 映射满射到 $H^1(K,\mu_p)$。又 $t_E\in K^{\times p}$，所以其商不会损失这个上同调像，直接得到 (17.7)。

### 4.2 非分裂乘法型

令 $L/K$ 为非分歧二次分裂扩张，$T_0=\ker(\operatorname{Res}_{L/K}\mathbb G_m\to\mathbb G_m)$ 为范数一环面。扭曲的 Tate 一致化在几何点上为
$$0\longrightarrow\mathbb Z(\nu_q)
\longrightarrow T_0(\bar K)
\longrightarrow E(\bar K)\longrightarrow0.
\tag{17.8}$$
格子生成元映为 $t_E$；在 Galois 作用下同时按 $\nu_q$ 反转。

因为非平凡符号作用下 $\mathbb Z(\nu_q)^{G_K}=0$ 且
$H^1(K,\mathbb Z(\nu_q))\simeq\mathbb Z/2\mathbb Z$，(17.8) 说明 $T_0(K)\hookrightarrow E(K)$ 的余核被 $2$ 杀掉。这里 $H^1$ 的计算可先对分裂扩张的核取上同调：连续同态从紧群到离散无挠群 $\mathbb Z$ 为零，再计算阶 $2$ 群的符号模。由于 $p$ 为奇数，该嵌入诱导
$$T_0(K)/p\xrightarrow{\sim}E(K)/p.$$

另一方面，$H^1(K,T_0)=K^\times/N_{L/K}L^\times$ 被 $2$ 杀掉：对 $x\in K^\times$，$x^2=N_{L/K}(x)$。乘 $p$ 的环面 Kummer 正合列因此给出
$$T_0(K)/p\xrightarrow{\sim}H^1(K,T_0[p]),
\qquad T_0[p]=\mu_p\otimes\nu_q=C_q.$$
Kummer 映射关于 (17.8) 的一致化同态相容，证明 (17.7)。

这个证明明确使用 $p$ 为奇数；不能原样用于 $2$-Selmer 群。

## 5. 表的逐项证明

$A$ 在 $q\in T$ 好约化，故 $\mathcal L_q(A)=H^1_{\rm ur}(K,V)$。好约化的这一事实也可从光滑模型上的 Kummer 正合列和有限域上的 Lang 定理直接得出。

- 若 $q=-1\pmod p$ 且 $s_q=1$，则 $C_q$ 的 Frobenius 特征值为 $-1$。由 (17.6)，其 $H^1$ 一维且不分歧部分为零。另一特征线的 Frobenius 为 $1$，它的 $H^1$ 一维且全部不分歧。由表示的特征线直和，二者在 $H^1(K,V)$ 中相交为零。结合 (17.7)，得到第二行。
- 若 $q=-1\pmod p$ 且 $s_q=-1$，则 $C_q$ 的 Frobenius 为 $1$，其 $H^1$ 一维且全部不分歧；这正是 $V$ 的整个不分歧上同调。得到第一行。
- 若 $q=1\pmod p$ 且 $s_q=-1$，$F=-I$；(17.5) 的两端都为零。因此 $H^1(K,V)=0$，得到第三行。
- 若 $q=1\pmod p$ 且 $s_q=1$，$V$ 为二维平凡表示，$C_q$ 是其中一条直线。其 $H^1$ 二维，不分歧部分一维；$V$ 的不分歧上同调二维。由 $V=C_q\oplus Q_q$ 的任一 Galois 分裂及 (17.5) 的函子性，
  $$H^1(K,C_q)\cap H^1_{\rm ur}(K,V)=H^1_{\rm ur}(K,C_q),$$
  故交的维数为 $1$，得到第四行。

这也证明每个 $q\in S$ 的 (17.1)，以及每个 $q\in T\setminus S$ 的局部条件相同。

## 6. 其余位置的条件全部相同

R13 已证明 $N_E=32\prod_{q\in T}q$，并且 $E,A$ 在 $p$ 都好约化。

若 $v$ 为有限素数且 $v\notin T\cup\{2,p\}$，两曲线都好约化，局部条件都由 $V$ 的不分歧上同调给出，故相同。

在 $2$ 处，两曲线均为加性且潜在好约化。形式群是 pro-$2$ 群；约化单位分支是加法群；椭圆曲线加性约化的几何分支群阶只含素因子 $2,3$。于是对 $p>3$，乘 $p$ 在 $E(\mathbb Q_2)$ 和 $A(\mathbb Q_2)$ 上均为自同构，两者 Kummer 像均为零。

在 $p$ 处，令 $\mathcal E,\mathcal A$ 是 $\mathbb Z_p$ 上的好约化模型。由于绝对分歧指数 $1<p-1$，Raynaud 全忠实性使 $\phi$ 及其逆唯一延拓为有限平坦群概形同构
$$\mathcal E[p]\xrightarrow{\sim}\mathcal A[p].$$
对好约化阿贝尔概形 $\mathcal B/\mathbb Z_p$，有限域 Lang 定理及光滑 Hensel 提升给出 $H^1(\mathbb Z_p,\mathcal B)=0$。乘 $p$ 的 fppf Kummer 正合列因而将 $B(\mathbb Q_p)/p$ 识别为 $H^1_{\rm fppf}(\mathbb Z_p,\mathcal B[p])$，它在泛纤维上的像正是局部条件。延拓的同构保持此像，故 $\mathcal L_p(E)=\mathcal L_p(A)$。

实位置上，Galois 群阶为 $2$，与 $p$ 互素，故 $H^1(\mathbb R,V)=0$。至此定理第 1 项得证。

## 7. 全局 Selmer 比较

Selmer 群定义为全局上同调中满足所有上述局部条件的子空间。因此局部限制给出单射
$$
\frac{W_E}{W_E\cap W_A}\hookrightarrow
\bigoplus_{q\in S}\frac{\mathcal L_q(E)}{\mathcal L_q(E)\cap\mathcal L_q(A)}.
$$
核为零的理由是：若类在每个 $q\in S$ 的像也满足 $A$ 的局部条件，则在其余位置两条件已相同，它就在 $W_A$ 中。每个右端加项由 (17.1) 一维，因此得到 (17.2) 的第一式；交换 $E,A$ 得第二式。$S=\varnothing$ 时两子空间相等，证明全部结论。

## 8. 对整性路线的精确意义

R13 的非 CM 同余曲线必须有 $T\ne\varnothing$。R17 说明，单凭出现新的分母素数，不能断言 $p$-Selmer 群必须与 CM 参考曲线不同：如果这些素数全为非分裂乘法型，通常的 $p$-Selmer 群在给定同余下完全相同。

这是一条在实际同余假设下的蕴含；没有构造满足该假设且 $T\ne\varnothing$ 的曲线。要从 Selmer 理论证明最终整性，仍需排除这样的同余曲线，或找到超出通常的 $p$-Selmer 条件的全局约束。即使另有方法算出 $\operatorname{Sel}_p(A)=0$，也只能在 $S=\varnothing$ 时推出 $\operatorname{Sel}_p(E)=0$，这与一条非 CM 曲线的秩为零并不矛盾。

此外，(17.3) 只比较这两条曲线本身；没有声称它们的所有二次扭曲均为 Selmer companions，也没有声称 Mordell–Weil 群或 Tate–Shafarevich 群整体同构。

## 9. 来源与标准输入

- B. Mazur, K. Rubin, *Selmer companion curves*, Transactions of the AMS **367** (2015), 401–421，DOI [10.1090/S0002-9947-2014-06114-X](https://doi.org/10.1090/S0002-9947-2014-06114-X)；[作者全文](https://bpb-us-e1.wpmucdn.com/sites.harvard.edu/dist/a/189/files/2023/01/SELMER-COMPANION-CURVES.pdf)，§2，Lemmas 5.1、5.4、5.6，Proposition 5.8。本文给出所需奇素数情形的 Tate/Kummer 计算和全局比较，不直接套用要求两曲线潜在乘法素数集合相同的 companion 定理。
- M. Raynaud, *Schémas en groupes de type $(p,\ldots,p)$*, Bulletin SMF **102** (1974), 241–280，Corollaire 3.3.6(1)；[原文](https://www.numdam.org/article/BSMF_1974__102__241_0.pdf)。小分歧全忠实性在此仅用于两条已有好约化曲线的 $p$ 挠点，假设由 R13 给出。
- Tate 一致化、椭圆曲线约化群及分支群：J. H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves* (1994), Chapter V；*The Arithmetic of Elliptic Curves*, 2nd ed. (2009), Chapter VII。局部上同调维数在 §3 已由温和惯性关系展开。
