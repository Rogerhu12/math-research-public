# O6：全局立方分母与实际模 3 同余

日期：2026-11-12；会话：serre-uniformity-astra-resume2。

**状态：已证明的补充接口。** 本文的 $E$ 始终是 [R19](../results/R19-converse-fermat-fixed-cm.md) 某个实际原始解对应的曲线，不是单独满足有限个迹条件的参数。得到
$$
\boxed{Z\in\mathbb Q^{\times3}\quad\Longleftrightarrow\quad E[3]\simeq A[3],
\qquad A:y^2=x^3-x.}
\tag{1}
$$
由此加强立方分母支的素因子和 Tate 参数限制；这些是必要条件，没有排除全部变化的 $Z,p$。

## 1. 模 3 降层没有不可约性或权的缺口

R19 给出 $p>37$、$E$ 非 CM、$E[p]\simeq A[p]$，并且
$$
N_E=32\operatorname{rad}(|Z|),\qquad
\Delta_{\min}(E)=2^\delta Z^p,\qquad
(Z,6p)=1,\quad \delta\in\{6,9,12\}.
\tag{2}
$$
若 $E[3]$ 在 $\mathbb F_3$ 上可约，则 $E$ 有有理循环 $3$ 同源。Lemos 的 Theorem 1.1 对非 CM 且有非平凡有理循环同源的曲线给出：每个 $p>37$ 的模 $p$ 像为全部 $\operatorname{GL}_2(\mathbb F_p)$。这与 $E[p]\simeq A[p]$ 矛盾。因此 $E[3]$ 不可约。

这里不可约也蕴含绝对不可约。否则交换子域为 $\mathbb F_9$，二维像包含于 $\mathbb F_9^\times$；但奇表示中的复共轭有两个不同的 $\mathbb F_3$ 本征值 $1,-1$，不可能属于这个非分裂 Cartan。

假设 $Z$ 是立方。每个 $q\mid Z$ 都满足 $q\ne2,3$，$E$ 在 $q$ 为乘性约化，且
$$
3\mid v_q(\Delta_{\min}(E))=p\,v_q(Z).
$$
Tate 曲线的惯性描述说明 $E[3]$ 在 $q$ 不分歧。此处仅用惯性扩张类消失，尚未假设整个 Tate 参数为立方。

Ribet (1990) 的原始 **Theorem 1.1** 明确允许残余特征 $\ell\ge3$。其设定是绝对不可约、来自权 $2$ 和平凡特征的表示；删除 $q\parallel N$ 时，要求在 $q$ 有限，并满足以下二者之一：$q\not\equiv1\pmod\ell$，或者 $\ell\nmid N$。在这里取 $\ell=3$，模性定理给出起始形式，而且始终 $3\nmid N$。所以即使 $q\equiv1\pmod3$，也可以逐个删除所有 $q\mid Z$。不需要删特征素数或改变 Serre 权。

最终表示来自 $S_2(\Gamma_0(32))$。该空间维数为 $1$，由 $f_A$ 张成，故 $E[3]\simeq A[3]$。绝对不可约且双方在 $\mathbb F_3$ 上定义，保证同构下降到 $\mathbb F_3$。

反之，若 $E[3]\simeq A[3]$，则对每个 $q\mid Z$，$A[3]$ 在 $q$ 不分歧。乘性约化的 Tate 惯性公式给出
$$
3\mid p\,v_q(Z).
$$
因为 $p\ne3$，所有 $v_q(Z)$ 都被 $3$ 整除。有理整数的负号也是立方，故 $Z$ 为整数立方。这证明 (1)。

## 2. 全部局部扩张的消失及同余模 $12p$

$A$ 的 CM 自同态 $[i]$ 在 $\mathbb Q(i)$ 定义，且 $i^2+1$ 在 $\mathbb F_3$ 上不可约，所以 $A[3]$ 的像包含于阶 $16$ 的非分裂 Cartan 正规化子。事实上像等于它：直接数点得 $\#A(\mathbb F_5)=8$，故模 $3$ Frobenius 特征多项式是
$$t^2-t-1.$$
其根在 $\mathbb F_9^\times$ 中范数为 $-1$，因此阶为 $8$，给出完整 Cartan；复共轭在 Cartan 外，给出正规化子。

于是当 $Z=Y^3$ 时，$E[3]$ 的有限像的阶与 $3$ 互素。局部 Tate 表示中的两个一维特征的扩张必分裂：在 $q\equiv1\pmod3$ 时，剩余的不分歧非平凡扩张会产生阶 $3$ 的幺幂元；在 $q\not\equiv1\pmod3$ 时，不分歧扩张群本来就是零。设 $t_{E,q}$ 是在非分裂乘性情形先作不分歧二次扭曲后的 Tate 参数，则
$$
t_{E,q}\in\mathbb Q_q^{\times3}.
$$
[R13](../results/R13-denominators-for-fixed-cm-congruence.md) 已由实际模 $p$ 同余证明 $t_{E,q}\in\mathbb Q_q^{\times p}$。因 $(3,p)=1$，
$$
\boxed{t_{E,q}\in\mathbb Q_q^{\times3p}.}
\tag{3}
$$

记 $s_q=1$ 或 $-1$ 为实际曲线 $E$ 在 $q$ 的分裂或非分裂乘性符号。Tate 半单化的本征值为 $s_q q,s_q$。若 $q$ 在 $\mathbb Q(i)$ 中分裂，$A[3]$ 的 Frobenius 位于非分裂 Cartan 内；而一个在 $\mathbb F_3$ 上有本征值的 Cartan 元只能是标量，故 $q\equiv1\pmod3$。若 $q$ 在 $\mathbb Q(i)$ 中惰性，Frobenius 位于正规化子外侧，迹为零，故 $q\equiv-1\pmod3$。结合 R13 的同符号模 $4p$ 条件，得到
$$
\boxed{q\mid Y\Longrightarrow
q\equiv\chi_{-4}(q)\pmod{12p}.}
\tag{4}
$$
这里 $q$ 在 CM 域的分裂性，与 $E$ 的乘性约化是否分裂，是两个不同概念。

若 $q$ 在 CM 域分裂，写其 CM Frobenius 为 $u+vi\in\mathbb Z[i]$，$q=u^2+v^2$。实际 Tate 符号 $s_q$ 同时适用于模 $3$ 和模 $p$，所以两个同构给出
$$u\equiv s_q\pmod{3p},\qquad 3p\mid v.$$
又 $A$ 的全部 $2$ 挠点有理，故 $v$ 偶、$u$ 奇；$q$ 为素数使 $u,v$ 都非零。因此
$$
\boxed{q\text{ 在 }\mathbb Q(i)\text{ 分裂}\Longrightarrow q\ge36p^2+1.}
\tag{5}
$$

最后，R19 的 $j$ 分母恰为 $|Z|^p=|Y|^{3p}$。由 (4) 和 $|Y|>1$，
$$h(j(E))\ge3p\log(12p-1).$$
若 $Y$ 有 CM 分裂的素因子，则可加强为 $3p\log(36p^2+1)$。下界随 $p$ 增长本身不与任何已证上界矛盾。

## 3. 原始来源与后续接口

- P. Lemos, *Serre's uniformity conjecture for elliptic curves with rational cyclic isogenies*, Theorem 1.1；[作者预印本 arXiv:1702.01985](https://arxiv.org/pdf/1702.01985)。这里只用已经明列的有理循环同源定理，不把它扩展到仅在二次域上存在的同源。
- K. A. Ribet, *On modular representations of $\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)$ arising from modular forms*, Invent. Math. **100** (1990), 431–476，Theorem 1.1，印刷页 431–432；[作者原文](https://math.berkeley.edu/~ribet/Articles/invent_100.pdf)。本轮已直接查看原始扫描的这两页，确认 $\ell=3$ 及 $\ell\nmid N$ 分支。
- 全局模性、层 $32$ 维数和最小判别式的来源与详细证明见 R19。

实际的 $Z=Y^3$ 整数问题在[完整原始四次式参数化](2026-11-12-cube-denominator-primitive-quartics.md)中继续处理。(1) 不是固定 $A$ 的 Frey–Mazur 排除：同时具有模 $3$ 与模 $p$ 同构仍是需要进一步算术输入的子问题。
