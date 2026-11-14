# 固定 1-motive 的全素数消失定理：准确适用范围与局部化障碍

**可信度：已证明。** 本文核对 Jossen 已发表原文，并对本题给出两个具体结论：一个固定的 $\mathbb G_m$ 扩张确实有无条件的二阶 Sha 消失；但其一阶 Sha 与原椭圆曲线的 Sha 同构。另一方面，整数 Tate 模的全局到所有局部的单射，不能在取 $\mathbb Q_p$ 系数后作同样推论。本题的秩二点直接产生这个非交换现象的算术实例。

## 1. 引用的定理及其局部条件

一手来源是 P. Jossen, *On the second Tate–Shafarevich group of a 1-motive*, Algebra & Number Theory **7** (2013), 2511–2544，[期刊原文](https://msp.org/ant/2013/7-10/ant-v7-n10-p05-p.pdf)，[DOI](https://doi.org/10.2140/ant.2013.7.2511)。以下均已对照发表版，不能把预印本检索摘要当作完整假设。

原文 §2.1（p.2520）对连续 Galois 模使用连续 cochain 上同调，并定义
$$
\Sha^i(k,C)=\ker\left(H^i(k,C)\longrightarrow
\prod_{v\text{ 全部处所}}H^i(k_v,C)\right).
\tag{1}
$$
无穷处采用 Tate 修正。特别地，$C=T_pM$ 时要求在每个局部的**整数 Tate 模上同调中为零**，不只是落在局部 Kummer 像，也不只是取 $\mathbb Q_p$ 后为零。

原文 Lemma 5.2（p.2534）的假设为：$M=[Y\to B]$，$B$ 是阿贝尔簇或环面，其几何有理自同态代数是除代数的乘积，且 $Y$ 的 Galois 作用平凡。结论是
$$
\Sha^1(k,T_pM)=0\qquad\text{对每个 }p.
\tag{2}
$$
原文 Theorem 3（p.2513）在相同的 $B$ 条件下给出有限群的完美配对
$$
\Sha^0(k,M)\times\Sha^2(k,M^\vee)\longrightarrow\mathbb Q/\mathbb Z.
\tag{3}
$$
本题 $E:y^2=x^3-17x$ 的 $\operatorname{End}_{\overline{\mathbb Q}}(E)\otimes\mathbb Q=\mathbb Q(i)$ 是域，因而满足条件。对于 $M=[0\to E]$ 以及任意常值格映射 $M=[\mathbb Z^r\to E]$，(2) 都适用。

## 2. 一个固定半阿贝尔群的二阶 Sha 确实为零

固定本题的独立点
$$
P=(-1,4),\qquad Q=(9,24),
$$
取 $M=[u:\mathbb Z^2\to E]$，其中 $u(1,0)=P$、$u(0,1)=Q$。其对偶为 $[0\to G]$，其中 $G$ 是固定扩张
$$
0\longrightarrow\mathbb G_m^2\longrightarrow G
\longrightarrow E^\vee\longrightarrow0.
\tag{4}
$$
用主极化识别 $E^\vee=E$。扩张由 Barsotti–Weil 公式中的有理点 $P,Q$ 决定；只使用 $P$ 同样得到固定的 $\mathbb G_m$ 扩张。

由于 $\mathbb Z^2$ 是常值离散格，连续同态从紧 Galois 群到 $\mathbb Z^2$ 必为零，故
$$
H^0(\mathbb Q,M)=E(\mathbb Q)/u(\mathbb Z^2),\qquad
H^0(\mathbb Q_\ell,M)=E(\mathbb Q_\ell)/u(\mathbb Z^2)
$$
对每个有限素数 $\ell$ 成立。若有理点 $R$ 的商类在某一个 $\mathbb Q_\ell$ 中为零，则 $R=u(a,b)$ 对某个 $(a,b)\in\mathbb Z^2$ 在 $E(\mathbb Q_\ell)$ 中成立。因两边都是有理点，该等式也在 $E(\mathbb Q)$ 中成立。因此
$$
\Sha^0(\mathbb Q,M)=0.
$$
由 (3) 得到真正无条件的结论
$$
\boxed{\Sha^2(\mathbb Q,G)=0.}
\tag{5}
$$
这不是固定 $p$ 后选择扩张：$G$ 已由固定的 $E,P,Q$ 定义，(5) 同时涵盖所有素数。

### 2.1 同一个 $G$ 的一阶 Sha 完全保留原题

更一般地，对任意数域 $k$ 上的分裂环面扩张
$$
0\longrightarrow\mathbb G_m^r\longrightarrow G\longrightarrow A\longrightarrow0
$$
有自然同构
$$
\boxed{\Sha^1(k,G)\simeq\Sha^1(k,A).}
\tag{6}
$$
**证明。** Hilbert 90 在全局和每个局部都给 $H^1(k,\mathbb G_m^r)=0$、$H^1(k_v,\mathbb G_m^r)=0$。因此 $H^1(k,G)\to H^1(k,A)$ 单射。若 $\xi\in\Sha^1(k,A)$，其连接像属于 $\operatorname{Br}(k)^r$，并在每个 $\operatorname{Br}(k_v)^r$ 中为零。Brauer–Hasse–Noether 单射迫使连接像为零，所以 $\xi$ 有唯一全局提升 $\widetilde\xi\in H^1(k,G)$。局部 Hilbert 90 又迫使其所有局部限制为零，故 $\widetilde\xi\in\Sha^1(k,G)$。$\square$

将 (6) 用于 (4)，得到
$$
\Sha^1(\mathbb Q,G)[p^\infty]
\simeq\Sha(E/\mathbb Q)[p^\infty]
\quad\text{对每个 }p.
\tag{7}
$$
所以 (5) 并没有经一个长正合列消去目标 Sha；(7) 精确表明目标仍留在同一个半阿贝尔群的一阶群中。

## 3. 每个单独的上同调群都允许有理化

设 $\mathcal G$ 为紧群，$T$ 为有限自由 $\mathbb Z_p$ 模，带连续作用，$V=T\otimes\mathbb Q_p$。则
$$
H^1_{\rm cont}(\mathcal G,T)\otimes\mathbb Q_p
\simeq H^1_{\rm cont}(\mathcal G,V).
\tag{8}
$$
**证明。** $\mathcal G^n$ 紧，所以每个连续 $V$ 值 cochain 的像有界，包含在某个 $p^{-a}T$ 中。因此对每个次数，连续 cochain 复形满足
$$
C^\bullet_{\rm cont}(\mathcal G,V)
=C^\bullet_{\rm cont}(\mathcal G,T)[1/p].
$$
局部化是正合函子，取上同调便得 (8)。$\square$

这适用于 $G_{\mathbb Q}$、每个 $G_{\mathbb Q_v}$，也适用于有限集合 $S$ 对应的 $G_{\mathbb Q,S}$。问题不在 (8)，而在自然映射
$$
\left(\prod_v H^1(\mathbb Q_v,T)\right)\otimes\mathbb Q_p
\longrightarrow
\prod_v\left(H^1(\mathbb Q_v,T)\otimes\mathbb Q_p\right).
\tag{9}
$$
这是无限乘积；(9) 一般不单射。下面证明本题确实出现这一现象。

## 4. 秩二直接给出非零的全局有理类，所有局部有理像均为零

固定本题一个 good split $p\ge13$、$p\ne17$，令 $T=T_pE$、$V=V_pE$。令 $\ell_p$ 为延拓到 $E(\mathbb Q_p)$ 的形式椭圆对数。非扭点 $P,Q$ 的对数均非零；其核为局部扭点群，而有理点若在 $E(\mathbb Q_p)$ 中为扭点，也是在 $E(\mathbb Q)$ 中的扭点。

取一个 $c\in\mathbb Q_p^\times$ 使
$$
A=c\ell_p(Q),\qquad B=-c\ell_p(P)
$$
都属于 $\mathbb Z_p$，且至少一个为单位。定义
$$
w=A P+B Q\in E(\mathbb Q)\otimes\mathbb Z_p.
\tag{10}
$$
$P,Q$ 在 $E(\mathbb Q)\otimes\mathbb Q_p$ 中线性无关，故 $w$ 非零且非挠。整数 Kummer 映射给出非挠类
$$
x=\kappa_p(w)\in H^1(\mathbb Q,T).
\tag{11}
$$
该映射的单射性来自有限层 Kummer 单射取逆极限；不需要假设 Sha 有限。

在 $p$ 处，$A\ell_p(P)+B\ell_p(Q)=0$。R7 的非异常性给 $E(\mathbb Q_p)[p]=0$，故形式对数在局部 pro-$p$ 完成上单射，得到
$$
\operatorname{res}_p x=0\quad\text{已经在 }H^1(\mathbb Q_p,T)\text{ 中成立。}
\tag{12}
$$
对于 $\ell\ne p$，$E(\mathbb Q_\ell)$ 有一个开 pro-$\ell$ 子群，因此
$$
E(\mathbb Q_\ell)^{\wedge}_p
\quad\text{是有限 }p\text{ 群。}
$$
由 Kummer 映射的自然性，$\operatorname{res}_\ell x$ 落在此有限群的像中，故为有限 $p$ 挠。取 $\mathbb Q_p$ 系数后该像为零。无穷处的高阶上同调在奇素数 $p$ 下为零。因此 (8)、(11)、(12) 给出
$$
0\ne x\otimes1\in
\ker\left(H^1(\mathbb Q,V)\to\prod_vH^1(\mathbb Q_v,V)\right).
\tag{13}
$$
这里仅使用了椭圆曲线局部 Kummer 像的性质；没有对任意 $p$ 进表示断言局部 $H^1$ 为零。若要得到更强的本例陈述，局部 Tate 对偶及 $E(\mathbb Q_\ell)$ 的上述结构还给 $H^1(\mathbb Q_\ell,T)$ 有限、从而 $H^1(\mathbb Q_\ell,V)=0$，但 (13) 不需要这个更强版本。

### 4.1 所构造的类只在固定有限集合可能分歧

可以取 $S=\{2,17,p,\infty\}$。对 $\ell\notin S$，曲线有好约化且 $p$ 可逆，乘 $p^n$ 映射在阿贝尔概形上有限 étale。将它拉回到有理点给出的整截面，得到的 Kummer 扭子在 $\ell$ 处不分歧。因此 (11) 来自
$$
H^1(G_{\mathbb Q,S},T).
\tag{14}
$$
以下出现的无穷多个辅助素数不代表新增分歧：那些整数局部类是不分歧但非零的类。好素数处的不分歧整数群
$T/(\operatorname{Frob}_\ell-1)T$ 可以非零，即使取 $\mathbb Q_p$ 后为零。

## 5. 辅助处的局部挠阶必定没有统一上界

对 $M=[0\to E]$，Jossen Lemma 5.2 给
$$
\Sha^1(\mathbb Q,T_pE)=0.
\tag{15}
$$
而第 4 节已经构造非挠的 $x$，其每个局部像都是有限 $p$ 挠，且 $p$ 处局部像为零。

**命题。** 对每个 $N\ge0$，存在一个有限素数 $\ell\ne p$，使
$$
p^N\operatorname{res}_\ell x\ne0.
\tag{16}
$$
而且去掉任意固定有限个处所后，局部像的阶仍然无界。

**证明。** 若某个 $p^N$ 杀死全部局部像，则 $p^Nx\in\Sha^1(\mathbb Q,T)$，由 (15) 得 $p^Nx=0$，与 $x$ 非挠矛盾。每个单独的局部像的阶有限；有限多个处所的阶有共同上界。因此无界性在去掉任意有限集合后仍成立。$\square$

令 $b=(\operatorname{res}_v x)_v$。每个坐标都是挠元，但 (16) 表明 $b$ 在整数局部乘积中不是挠元。因此
$$
b\otimes1\ne0
\quad\text{而它在 (9) 右边的像为零。}
$$
这给出 (9) 不单射的实际算术实例，并精确解释了
$$
\Sha^1(\mathbb Q,T_pE)=0
\quad\centernot\Longrightarrow\quad
\Sha^1(\mathbb Q,V_pE)=0.
\tag{17}
$$
同理，不能把要求所有处所整数局部像为零的 (15)，换成只在有限集合 $S$ 施加局部零条件。由 (12) 并再乘一个杀死 $2,17$ 处局部像的 $p$ 幂，已经得到有限 $S$ 局部零条件下的非零类。

本题 R8 中的显式 strict 直线正是 (13) 的 Mordell–Weil 来源。它存在于每个目标素数处，无论 $\Sha[p^\infty]$ 是否有限；因此 (15) 不能替代 R8 中尚缺的额外 Sha 方向控制。

## 6. 固定代数数的 rank-one 1-motive 也不控制 Fermat 深度

对任意固定数域 $F$ 和 $\alpha\in F^\times$，取
$$
M_\alpha=[\mathbb Z\xrightarrow{1\mapsto\alpha}\mathbb G_m].
$$
同样有 $\Sha^0(F,M_\alpha)=0$；$\mathbb G_m$ 满足 Jossen 的自同态条件，且这个 rank-one 1-motive 的对偶与自身同构。因此
$$
\Sha^2(F,M_\alpha)=0.
\tag{18}
$$
但是 (18) 不给固定 $\alpha$ 的局部对数深度上界。作为数值层面的区别，对任意预先选定的奇素数 $q$ 和 $N\ge1$，选定常数 $\alpha=1+q^N$ 后，(18) 仍对这个固定动机成立，而
$v_q(\log_q\alpha)=N$。故结构性二阶消失本身不能给出局部单位格的一个固定小指数。这里没有声称一个固定 $\alpha$ 在变化素数处的深度已经证明无界。

## 来源与适用边界

- Jossen 2013 已发表原文：§2.1、Theorem 3、Lemma 5.2；对偶构造见 §1.11–1.13。本文所用的几何简单性假设对 $E_{17}$ 成立。
- J. S. Milne, [*Arithmetic Duality Theorems*, second edition](https://www.jmilne.org/math/Books/ADTnot.pdf)：Chapter I §3 的局部阿贝尔簇对偶与 §4 的全局类域论输入。正文的 (13) 只需局部 Kummer 像有限，并未依赖任意表示的局部消失。
- 本题 R4、R7、R8。本文补充的是 (6) 的半阿贝尔 Sha 同构，以及 (10)–(17) 的整数/有理局部化非交换证明。没有得到 $\nu_p\le3$ 的无穷次发生，也没有取得 $\Sha(E/\mathbb Q)[p^\infty]$ 的跨 $p$ 有限性传播。
