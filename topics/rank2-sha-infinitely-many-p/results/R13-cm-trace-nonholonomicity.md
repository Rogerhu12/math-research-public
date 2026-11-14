# R13. 固定 CM trace 序列不满足多项式系数线性递推

**状态：已证明。** 日期：2026-11-12。会话：Astra-rank2-Sha / cm_iwasawa_routes。

本结论研究 R6 中的整条特征 $0$ 序列 $a_n$，并不证明其素数对角值模 $\mathfrak p^4$ 的无穷非消失性。

## 1. 陈述及外部输入

固定
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),\qquad
\Lambda=\Omega_\infty\mathbb Z[i],\qquad f=34(1+i).
$$
令
$$
z_f=\Omega_\infty/f,\qquad
u=\wp(z_f,\Lambda),\qquad
v=\wp'(z_f,\Lambda)/2,
$$
并令 $F=K(E_f)$。所用外部算术输入是
$$
F=K(u),\qquad v\in F.
\tag{1}
$$
其出处是 J. Coates–Z. Liang–R. Sujatha，*The Tate–Shafarevich group for elliptic curves with complex multiplication*（2009），§3，Lemmas 3.1–3.2 及其用于 $D=17$ 的构造，[arXiv:0901.3832](https://arxiv.org/abs/0901.3832)。这些输入及以下导数递推的完整计算已在 [R6](R6-cm-trace-recurrence.md) 列明。

取 $B_0(X)=1$ 及
$$
B_{n+1}=4(X^3-17X)B_n''+6(3X^2-17)B_n'+12XB_n,
$$
定义
$$
a_n=\operatorname{Tr}_{F/K}(vB_n(u))\in K.
\tag{2}
$$

**定理。** 不存在特征 $0$ 的扩域 $L\supset K$、整数 $r,N\ge0$ 以及不全为零的多项式 $q_0(X),\ldots,q_r(X)\in L[X]$，使
$$
\sum_{j=0}^r q_j(n)a_{n+j}=0
\qquad(n\ge N).
\tag{3}
$$
换言之，$a_n$ 即使允许扩张系数域、忽略有限个初始项，也不是 P-recursive 序列。

## 2. 奇部具有无穷多个不消去的二阶极点

群 $\operatorname{Gal}(F/K)$ 的各元素给出点
$$
P_\sigma=(u^\sigma,v^\sigma)\in E(\mathbb C).
$$
选取 $z_\sigma\in\mathbb C/\Lambda$ 表示这些点，定义
$$
g(z)=\sum_{\sigma\in\operatorname{Gal}(F/K)}\wp(z+z_\sigma,\Lambda),
\qquad
g_o(z)=\frac{g(z)-g(-z)}2.
\tag{4}
$$
点 $P_f$ 不是 $2$-torsion：否则 $2z_f\in\Lambda$，等价于 $2/f\in\mathbb Z[i]$，显然不成立。因此 $v\ne0$，所有 $P_\sigma$ 都不是无穷远点或 $2$-torsion 点。故 $g$ 及 $g_o$ 在原点正则。

由 $F=K(u)$，各 $P_\sigma$ 互异。更重要的是，该 orbit 与其负 orbit 不交。若 $P_\tau=-P_\sigma$，则 $u^\tau=u^\sigma$；由 $u$ 生成 $F/K$ 可知 $\tau=\sigma$，继而 $v^\sigma=-v^\sigma$，与 $v\ne0$ 矛盾。

在 $-z_\sigma+\Lambda$ 处，$g(z)$ 的对应项有首部
$$
\frac1{(z+z_\sigma)^2}.
$$
同 orbit 的其他项没有该极点；$g(-z)$ 的极点来自 $+z_\tau+\Lambda$，由上段也不与之重合。所以 $g_o$ 在每个 $-z_\sigma+\Lambda$ 处有不为零的首项系数 $1/2$，在 $+z_\sigma+\Lambda$ 处有系数 $-1/2$。这些都是恰为二阶的极点。

固定一个 $\sigma$ 后，$-z_\sigma+\Lambda$ 已是一个无限离散集。因此 $g_o$ 有无穷多个不消去的二阶极点；它不是零函数，也不是整函数。

另一方面，平移后的 $x$ 坐标是定义在 $F$ 上的有理函数，对各共轭取和后定义在 $K$ 上；向量场
$$
\delta x=2y,\qquad\delta y=3x^2-17
$$
亦定义在 $K$ 上。因此 $g$ 在 $0$ 的全部 Taylor 系数属于 $K$。R6 已证明
$$
\frac{d^{2n+1}}{dz^{2n+1}}\wp(z,\Lambda)
=\wp'(z,\Lambda)B_n(\wp(z,\Lambda)),
$$
于是
$$
g_o(z)=2\sum_{n\ge0}a_n\frac{z^{2n+1}}{(2n+1)!}
\tag{5}
$$
在原点的一个复邻域成立。

## 3. 假想递推产生一个非零线性微分方程

假设式 (3) 成立。所有 $q_j$ 的系数生成一个有限生成的特征 $0$ 子域 $L_0/K$。它可嵌入 $\mathbb C$ 并固定既定的 $K\hookrightarrow\mathbb C$：先嵌入一个有限超越基，再延拓到其上的有限代数扩张。嵌入保留式 (3) 的每个等式以及至少一个非零系数。由于 $a_n\in K$，其复数值仍与式 (5) 相同。故以下可直接在 $\mathbb C$ 中计算。

置
$$
b_n=\frac{2a_n}{(2n+1)!},\qquad B(w)=\sum_{n\ge0}b_nw^n.
$$
由式 (5)，$g_o(z)=zB(z^2)$，所以 $B$ 在原点附近收敛。将式 (3) 除以 $(2n+1)!/2$，得到
$$
\sum_{j=0}^r Q_j(n)b_{n+j}=0\quad(n\ge N),
\qquad
Q_j(X)=q_j(X)\prod_{h=2}^{2j+1}(2X+h).
\tag{6}
$$
当 $j=0$ 时乘积为 $1$；这些 $Q_j$ 仍不全为零。

令 $\theta=w\,d/dw$ 并考虑多项式系数微分算子
$$
\mathcal L=\sum_{j=0}^r w^{r-j}Q_j(\theta-j).
\tag{7}
$$
对每个 $n\ge0$，$\mathcal L B$ 的 $w^{n+r}$ 系数恰为式 (6) 左侧。因此
$$
\mathcal L B=R(w)
\tag{8}
$$
其中 $R$ 是多项式，次数小于 $N+r$。这一步明确容许递推只在充分大的 $n$ 上成立。

算子 $\mathcal L$ 非零。确切地，令 $d=\max_j\deg Q_j$；其 $d$ 阶导数系数是
$$
\sum_{\deg Q_j=d}\operatorname{lc}(Q_j)\,w^{r-j+d},
$$
其中各 $j$ 给出不同的单项式，故不能相消。若 $R\ne0$，对式 (8) 两边再作用 $(d/dw)^{1+\deg R}$；若 $R=0$，不作此步。如此得到
$$
\widetilde{\mathcal L}B=0,
\tag{9}
$$
其中 $\widetilde{\mathcal L}$ 仍为非零多项式系数线性微分算子：左乘微分算子只提高最高导数阶，不会消掉非零的最高阶系数。

写 $h(z)=B(z^2)$。在 $z\ne0$ 的原点邻域，将式 (9) 中的 $w$ 替成 $z^2$、$d/dw$ 替成 $(2z)^{-1}d/dz$，即得 $h$ 的有理函数系数线性微分方程。该算子仍非零；若式 (9) 的最高阶为 $s$、最高阶系数为 $A_s(w)$，新最高阶系数是 $A_s(z^2)/(2z)^s$。再代入 $h(z)=z^{-1}g_o(z)$ 并清除分母，得到
$$
\sum_{j=0}^s C_j(z)g_o^{(j)}(z)=0,
\qquad C_j\in\mathbb C[z],\quad C_s\ne0.
\tag{10}
$$
乘以 $z^{-1}$ 后最高阶系数仍非零，故清分母不会得到零算子。两边都是全平面上的亚纯函数；由原点附近的等式和恒等原理，式 (10) 在全平面成立。

## 4. 极点阶给出矛盾

取 $g_o$ 的任一极点 $\zeta$，其首部为 $c(z-\zeta)^{-2}$，$c\ne0$。若 $C_s(\zeta)\ne0$，则式 (10) 的最高阶项有非零首部
$$
C_s(\zeta)c(-1)^s(s+1)!(z-\zeta)^{-s-2}.
$$
其余项 $C_jg_o^{(j)}$ 的极点阶至多为 $j+2\le s+1$，不能抵消这个 $s+2$ 阶项。故 $C_s$ 必须在 $g_o$ 的每个极点消失。但这些极点有无穷多个，非零多项式 $C_s$ 不可能有这么多根。这与式 (10) 矛盾，定理得证。此论证也涵盖 $s=0$ 的情形。

## 5. 两个有限模型推论

### 推论 A：没有固定维数的有理矩阵递推

不存在固定整数 $d$、有理函数矩阵 $M(X)\in\operatorname{Mat}_d(L(X))$、有理行向量 $c(X)$ 及向量序列 $U_n$，使对所有充分大的整数 $n$，
$$
U_{n+1}=M(n)U_n,
\qquad a_n=c(n)U_n.
\tag{11}
$$
这里允许 $L/K$ 为任意特征 $0$ 扩域，允许有限个整数下标落在系数的极点上，也不要求 $M$ 可逆。

**证明。** 对 $j=0,\ldots,d$，定义有理行向量
$$
r_0(X)=c(X),\qquad
r_j(X)=c(X+j)M(X+j-1)\cdots M(X).
$$
$d+1$ 个行向量在 $L(X)^d$ 中线性相关，所以存在不全为零的有理函数 $h_j(X)$ 使 $\sum_jh_jr_j=0$。清分母后系数可取为多项式。每个非零分母多项式只有有限个整数零点，故对所有充分大的 $n$ 可代入，并得到
$$
\sum_{j=0}^d h_j(n)a_{n+j}=0.
$$
这与定理矛盾。证毕。

### 推论 B：没有整条序列的有限原子表示

特别地，不存在有限组常数 $d_j,\lambda_j$ 使 $a_n=\sum_jd_j\lambda_j^n$ 对所有充分大的 $n$ 成立；这是推论 A 的对角常矩阵情形。

还可将其用于式 (4) 的具体函数。若在某个 good ordinary $p$ 上取形式群同构 $\iota_p$，满足
$$
\log_E\iota_p(T)=\Omega_p\log(1+T),
$$
则 $\widehat g(\iota_p(T))$ 不能等于有限和 $\sum_j c_j(1+T)^{t_j}$。否则形式变量替换后 $g(z)=\sum_jc_j\exp(\beta_jz)$，其中 $\beta_j=t_j/\Omega_p$；比较奇阶导数即有
$$
a_n=\frac12\sum_jc_j\beta_j(\beta_j^2)^n,
$$
与上段矛盾。这里不将这个特定 trace 函数未经证明地识别为经过正规化或 $p$-depletion 的整个 CLS / Katz 测度。

## 6. 本结论没有排除什么

本定理不排除仅在下标 $n=(p-3)/2$、且只模 $\mathfrak p^4$ 成立的特殊公式；该公式未必延伸为特征 $0$ 的全序列递推。它也不排除非线性递推、随 $p$ 改变维数的矩阵、引入额外算子的形式、或其它算术方式给出的无穷素数证书。

因此，本结果关闭的是“整条 trace 序列有一个固定阶线性递推，进而可直接套固定有限矩阵的 Frobenius 分类”这一具体入口。R6 所列的素数对角非消失条件仍待证明。
