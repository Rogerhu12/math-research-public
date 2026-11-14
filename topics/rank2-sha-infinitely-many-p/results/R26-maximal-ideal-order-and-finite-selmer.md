# R26：特征级数的极大理想阶控制有限 Selmer

**可信度：已证明。** 本结果统一局部深度、Iwasawa $\lambda$ 和 R24 的双权判据，不证明无穷多个素数满足所需上界。固定
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\qquad
p\ge13,\quad p\equiv1\pmod4,\quad p\ne17.
$$
沿用 R24–R25：
$$
\mathcal A=\mathbb Z_p[[T]],\quad \mathfrak m=(p,T),\quad
M=X_\infty^\chi,\quad
\operatorname{char}_{\mathcal A}M=(H_p),
$$
$$
H_p(T)=(T-p)^2G_p(T),\qquad G_p=\sum_{j\ge0}g_jT^j.
$$
对非零 $F\in\mathcal A$，定义
$\operatorname{ord}_{\mathfrak m}F=\max\{n:F\in\mathfrak m^n\}$。
这是二维局部环中的阶，不是中心 $T=p$ 的零点重数。

## 1. 结论

有无条件不等式
$$
\boxed{\quad
\dim_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q)
\le\operatorname{ord}_{\mathfrak m}H_p
=2+\min_{j\ge0}\{v_p(g_j)+j\}.
\quad}
\tag{1}
$$
其中 $v_p(0)=+\infty$。若 $d_p=\operatorname{ord}_{\mathfrak m}G_p$，则
$$
\boxed{\quad
\dim_{\mathbb F_p}\Sha(E/\mathbb Q)[p]
\le2\left\lfloor d_p/2\right\rfloor.
\quad}
\tag{2}
$$
所以 $G_p\notin\mathfrak m^2$ 足以给整个 $\Sha[p^\infty]=0$，且该条件准确等于
$$
g_0\notin p^2\mathbb Z_p
\quad\text{或}\quad g_1\notin p\mathbb Z_p.
\tag{3}
$$

## 2. 原始 Galois 模的准确矩阵表示

R25 已根据 Schneps Theorem IV 与 Rubin Proposition 11.3(ii) 证明
$$
M\simeq\mathbb Z_p^\ell,\qquad \ell=\lambda_p^{\mathrm{Iw}}.
\tag{4}
$$
这是原始 Galois 模的实际同构。选一个 $\mathbb Z_p$ 基，记 $T$ 的作用矩阵为 $A\in M_\ell(\mathbb Z_p)$。

$A$ 为拓扑幂零矩阵。确实，$\Gamma$ 的连续作用在有限群 $\operatorname{GL}_\ell(\mathbb F_p)$ 中的像为 $p$ 群，故 $\gamma=1+T$ 的像有 $p$ 幂阶；于是 $A\bmod p$ 幂零。存在 $b$ 使 $A^b\in pM_\ell(\mathbb Z_p)$，因此 $A^n\to0$。

对 $f(T)=\sum v_nT^n\in\mathcal A^\ell$，令
$$
f(A)=\sum_{n\ge0}A^nv_n,\qquad
q_j=\sum_{n\ge j+1}A^{n-1-j}v_n.
$$
这些和都收敛。逐项比较得到
$$
f(T)-f(A)=(TI_\ell-A)\sum_{j\ge0}q_jT^j.
$$
故以 $f\mapsto f(A)$ 为满射，有准确表示
$$
0\longrightarrow\mathcal A^\ell
\xrightarrow{\,TI_\ell-A\,}\mathcal A^\ell
\longrightarrow M\longrightarrow0.
\tag{5}
$$
左侧单射由 $\det(TI_\ell-A)$ 为非零首一多项式得到。

令 $D(T)=\det(TI_\ell-A)$。因 $A\bmod p$ 幂零，
$D\bmod p=T^\ell$，所以 $D$ 是次数 $\ell$ 的 distinguished polynomial。在每个高度一素理想处局部化，$\mathcal A$ 成为离散赋值环；对 (5) 作 Smith 分解，余核长度正是 $D$ 的赋值。特征理想按这些长度定义，所以
$$
(D)=(H_p).
\tag{6}
$$
$H_p$ 与 $D$ 仅差 $\mathcal A$ 单位。没有对可能带有限子模的任意伪同构替代物使用此结论。

## 3. 余核维数控制行列式的阶

令
$$
r=\dim_{\mathbb F_p}M/\mathfrak mM
=\dim_{\mathbb F_p}\operatorname{coker}(\overline A).
$$
$TI_\ell-A$ 模 $\mathfrak m$ 的秩为 $\ell-r$。左右各乘一个常数 $\operatorname{GL}_\ell(\mathbb Z_p)$ 矩阵，可使其约化成为
$\operatorname{diag}(I_{\ell-r},0_r)$。变换后的矩阵写为
$$
\begin{pmatrix}B&C\\D_1&E_1\end{pmatrix},
$$
其中 $B$ 在 $\mathcal A$ 上可逆，$C,D_1,E_1$ 的全部元素属于 $\mathfrak m$。准确的 Schur 补公式为
$$
\det\begin{pmatrix}B&C\\D_1&E_1\end{pmatrix}
=\det(B)\det(E_1-D_1B^{-1}C).
$$
第二个行列式有大小 $r$，所有元素都在 $\mathfrak m$，因此属于 $\mathfrak m^r$。基变换和 $\det B$ 都是单位，故
$$
\operatorname{ord}_{\mathfrak m}H_p\ge r.
\tag{7}
$$
若 $r=\ell$，原矩阵已全部在 $\mathfrak m$ 中，无须作 Schur 补。

R25 的有限 Selmer 注入给
$$
\operatorname{Sel}_p(E/\mathbb Q)
\hookrightarrow
\operatorname{Hom}_{\mathbb F_p}(M/\mathfrak mM,E[\mathfrak p]).
$$
右侧维数为 $r$，因为 $E[\mathfrak p]$ 为一维空间。于是
$$
\dim_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q)
\le r\le\operatorname{ord}_{\mathfrak m}H_p.
\tag{8}
$$
这只是不等式。比如 $\mathcal A/(T^2+p^2)$ 无非零有限子模、作为 $\mathbb Z_p$ 模自由秩二，但其模 $\mathfrak m$ 的维数为一，特征级数的 $\mathfrak m$ 阶为二。

## 4. 正规化系数及两个旧界

对非零 $F=\sum a_jT^j$，极大理想幂的生成元直接给出
$$
F\in\mathfrak m^n
\Longleftrightarrow
v_p(a_j)+j\ge n\quad\text{对所有 }j.
\tag{9}
$$
确实，$\mathfrak m^n$ 由 $p^{n-j}T^j$（$0\le j\le n$）生成，而所有次数至少 $n$ 的尾项都属于 $(T^n)$。所以
$\operatorname{ord}_{\mathfrak m}F=\min_j(v_p(a_j)+j)$。

又有
$$
\operatorname{gr}_{\mathfrak m}\mathcal A
\simeq\mathbb F_p[P,U],
$$
其中 $P,U$ 分别为 $p,T$ 的首项。此环为整环，故非零乘积的 $\mathfrak m$ 阶相加。$T-p$ 的首项为一次非零式 $U-P$，因此
$$
\operatorname{ord}_{\mathfrak m}H_p
=2+\operatorname{ord}_{\mathfrak m}G_p.
\tag{10}
$$
(8)–(10) 证明 (1)。

R4 的秩恰二、$E(\mathbb Q)[p]=0$ 与有限 Kummer 列给
$$
\dim\Sha(E/\mathbb Q)[p]
=\dim\operatorname{Sel}_p(E/\mathbb Q)-2.
$$
R7 已证明该数为非负偶数，所以由 (1) 得到 (2)。当 $d_p\le1$，$p$ 挠为零；非零 $p$ 初级挠元总有某个非零倍数的阶为 $p$，故整个初级部分为零。式 (9) 准确给出 (3)。

同时有
$$
\operatorname{ord}_{\mathfrak m}H_p
\le v_pH_p(0)=\nu_p,\qquad
\operatorname{ord}_{\mathfrak m}H_p
\le\lambda_p^{\mathrm{Iw}}.
\tag{11}
$$
第一式使用常数项；第二式使用 $H_p\bmod p$ 的首个非零项，其次数正是 $\lambda_p^{\mathrm{Iw}}$。中间系数可能给出比这两个数都小的 $\mathfrak m$ 阶，所以 (8) 比仅取这两个界的最小值更强。

## 5. 有限个权精确检测极大理想幂

取 $1\le n\le p-1$，定义
$$
k_j=1+j(p-1),\quad x_j=(1+p)^{k_j}-1,\quad z_j=x_j/p,
\qquad1\le j\le n.
$$
二项式展开和提升指数引理给
$$
z_j\equiv1-j\pmod p,\qquad v_p(x_j-p)=1.
\tag{12}
$$
各 $z_j$ 模 $p$ 两两不同。

**有限权判别。** 有准确等价
$$
\boxed{\quad
G_p\in\mathfrak m^n
\Longleftrightarrow
v_p\bigl(\delta^{k_j}\log\Phi(O)\bigr)\ge n+2
\quad(1\le j\le n).
\quad}
\tag{13}
$$

**证明。** R24 的全权单位矩比较与 (12) 给
$$
v_p\bigl(\delta^{k_j}\log\Phi(O)\bigr)
=2+v_pG_p(pz_j).
$$
模 $p^n$ 时，所有次数至少 $n$ 的尾项消失，故
$$
G_p(pz_j)\equiv\sum_{i=0}^{n-1}p^ig_i z_j^i\pmod{p^n}.
$$
关于未知量 $p^ig_i$ 的系数矩阵是 Vandermonde 矩阵，其行列式
$\prod_{j>i}(z_j-z_i)$ 为 $\mathbb Z_p$ 单位。因此全部
$G_p(pz_j)\in p^n$ 当且仅当全部 $p^ig_i\in p^n$；依 (9)，正等价于 $G_p\in\mathfrak m^n$。$\square$

$n=2$ 时，(13) 就是 R24 的双权失败条件；其否定通过 (1) 直接给初级部分为零。更高 $n$ 提供准确的系数过滤与有限 Selmer 维数上界，不能自动代替这里需要的无穷性。

## 6. 尚缺的算术输入

$\mu=0$ 和无有限子模保证上述比较严格成立，却不保证
$G_p\notin\mathfrak m^2$。抽象模块 $(\mathcal A/(T-p))^4$ 满足这两个结构条件，但有 $H=(T-p)^4$、$G=(T-p)^2\in\mathfrak m^2$。这不是 E17 的算术实现。

当前任务仍是证明原固定 $\Phi$ 的 $G_p\notin(p,T)^2$ 对无穷多个分裂素数成立，或找到更弱而足以证明初级有限的跨素数条件。两个指定对数矩与第二权的有限整系数公式使该条件可明确计算，没有消除跨素数非消失缺口。

## 引用与依赖

- R25：Schneps Theorem IV、Rubin Proposition 11.3(ii) 给出的实际 $\mathbb Z_p$ 自由性，以及有限 Selmer 的准确注入。
- K. Rubin, *Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，§11 的特征理想、Proposition 12.2、Theorem 12.9；[原文](https://swc-math.github.io/notes/files/99RubinCM.pdf)。
- R24：严格 LT 基的全权单位矩比较；R4、R7：秩、挠子与有限 Selmer 奇偶性。
- 本文已给出矩阵表示、Schur 补、极大理想阶及 Vandermonde 步骤的完整证明。
