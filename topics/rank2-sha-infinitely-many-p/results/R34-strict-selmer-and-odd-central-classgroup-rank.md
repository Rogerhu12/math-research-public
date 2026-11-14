# R34：严格 Selmer 的准确控制与中心类群秩的奇性

**可信度：已证明。** 日期：2026-11-12。固定
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),\qquad
p\ge13,\quad p\equiv1\pmod4,\quad p\ne17.
$$
本文证明 R30 中两个相邻的可能值实际只有一个发生：
$$
\boxed{\quad s_{\infty,p}=q_p+1,\qquad q_p\text{ 是正奇数}.\quad}
\tag{0.1}
$$
因此，初级有限性等价于 $q_p=1$，并可用**第一个**高阶 Fitting 理想及一个辅助素数的 rank $2$ Rubin–Stark 元素检测。证明使用固定非挠点的局部 Kummer 像；不假设 $\Sha[p^\infty]$ 有限、$p$-adic 高度非退化或中心零点只有二阶。

## 1. 对象和严格局部条件

沿用 R27、R30、R32 的记号：
$$
\pi=\psi_E(\mathfrak p),\quad
K_n=K(E[\pi^n]),\quad K_\infty=\bigcup_nK_n,
$$
$$
G=\operatorname{Gal}(K_\infty/K)=\Delta\times\Gamma,
\quad \rho_E(\gamma)=1+p,\quad
\Lambda=\mathbb Z_p[[T]],\quad T=\gamma-1,
\quad\mathfrak P=(T-p).
$$
写 $\widetilde\chi=\rho_E|_\Delta$，其阶为 $p-1$；以下 $\chi$ 分量总是 $\Delta$ 以这个字符作用的分量，不取逆字符。令
$$
W=E[\pi^\infty],\qquad
M_p=X_\infty^{\widetilde\chi},\qquad
\mathcal A_p=
\left(\varprojlim_n\operatorname{Cl}(K_n)\otimes\mathbb Z_p\right)^{\widetilde\chi},
$$
以及
$$
C_p=M_p/\mathfrak P M_p,\qquad
D_p=\mathcal A_p/\mathfrak P\mathcal A_p,\qquad
q_p=\operatorname{rank}_{\mathbb Z_p}D_p.
\tag{1.1}
$$
这里 $X_\infty$ 只允许在 $\mathfrak p$ 处分歧，$\mathcal A_p$ 则是处处无分歧类群模。R25、R30 保证 $C_p,D_p$ 是有限生成 $\mathbb Z_p$-模。

令
$$
S_p=\operatorname{Sel}_{\pi^\infty}(E/K),\qquad
S_p^{\rm str}
=\ker\left(S_p\longrightarrow H^1(K_{\mathfrak p},W)\right).
\tag{1.2}
$$
只在 $\mathfrak p$ 处把 usual Kummer 条件收紧为零，其他地方保持 usual Selmer 条件。R27 已证明
$$
S_p=\operatorname{Sel}'_{\pi^\infty}(E/K)
\simeq\operatorname{Hom}_{\rm cont}(C_p,W).
\tag{1.3}
$$
R7 的限制及共轭比较又将 $S_p$ 与 $\operatorname{Sel}_{p^\infty}(E/\mathbb Q)$ 识别。因此
$s_{\infty,p}=\operatorname{corank}_{\mathbb Z_p}S_p$。

本文首先证明不带有限误差的同构
$$
\boxed{\quad
S_p^{\rm str}\simeq\operatorname{Hom}_{\rm cont}(D_p,W).
\quad}\tag{1.4}
$$

## 2. 局部限制没有核，未分歧部分不贡献目标字符

置 $k=K_{\mathfrak p}=\mathbb Q_p$、$k_n=k(E[\pi^n])$ 和 $k_\infty=\bigcup_nk_n$。Lubin–Tate 理论给 $k_n/k$ 全分歧，且局部扩张次数等于 $[K_n:K]$。故 $\mathfrak p$ 在每层只有一个上方素位，并且
$$
\operatorname{Gal}(k_\infty/k)=G=\Delta\times\Gamma.
\tag{2.1}
$$
$W$ 在 $k_\infty$ 上为平凡模，在 $G$ 上通过 $\rho_E$ 作用。

### 2.1 无穷塔的 inflation 核为零

因为 $|\Delta|=p-1$ 在 $\mathbb Z_p$ 中可逆，$H^j(\Delta,W)=0$ 对所有 $j>0$ 成立。又因 $\widetilde\chi$ 非平凡，可以取 $\delta\in\Delta$ 使 $\widetilde\chi(\delta)-1$ 为单位，故 $W^\Delta=0$。对正规子群 $\Delta\subset G$ 使用 Hochschild–Serre 序列，得到
$$
H^j(G,W)=0\qquad(j\ge0).
\tag{2.2}
$$
特别地，inflation–restriction 给出
$$
H^1(k,W)\xrightarrow{\ \sim\ }
H^1(k_\infty,W)^G.
\tag{2.3}
$$
也可直接检查 $\Gamma$ 的一阶项：
$H^1(\Gamma,W)=W/(\gamma-1)W=W/pW=0$；$\Delta$ 再消去不变量。这里用的是可除群 $W$，不是以 $W[p]$ 替代它。

### 2.2 局部惯性与单位

令 $\mathcal L_\infty$ 为 $k_\infty$ 上最大交换 pro-$p$ 扩张的 Galois 群，$\mathcal I_\infty$ 为其惯性子群。剩余域仍是 $\mathbb F_p$，所以
$$
0\longrightarrow\mathcal I_\infty
\longrightarrow\mathcal L_\infty
\longrightarrow\mathbb Z_p\longrightarrow0.
\tag{2.4}
$$
$G$ 在右端的作用平凡：它在剩余域上平凡，而未分歧 pro-$p$ Galois 群的 Frobenius 商是交换的。因此
$$
\operatorname{Hom}_{G,\rm cont}(\mathbb Z_p,W)=0.
\tag{2.5}
$$
一个 $G$-等变的局部类在惯性上为零，当且仅当整个局部类为零。

局部互反律的范数相容性将 $\mathcal I_\infty^{\widetilde\chi}$ 与局部主单位的范数极限 $U_\infty^{\widetilde\chi}$ 识别。这里的字符检查可在有限层完成：局部乘法群的 pro-$p$ 完备化商去主单位后，只有赋值群 $\mathbb Z_p$，$\Delta$ 在赋值上平凡；剩余域单位的阶为 $p-1$，其 pro-$p$ 完备化为零。全分歧扩张的范数在赋值群上是恒等映射，故取范数极限仍不增加非平凡 $\chi$ 分量。

所用无限层局部互反律也可由有限层直接得到：一个有限交换 $p$ 扩张在某个有限层下降；将该层继续提高，使开子群 $\Gamma_n$ 在其有限 Galois 群上的作用平凡。因为 $\Gamma_n\simeq\mathbb Z_p$ 的 $p$-上同调维数为一，有限交换商的字符可以扩张到该有限层，再应用有限层局部互反律。由此得到所需的范数极限识别，不引入额外的分歧或赋值修正。

结合 (2.3)–(2.5)，局部类是否为零可以准确地在 $U_\infty^{\widetilde\chi}$ 上检测。

## 3. 严格 Selmer 恰好由处处无分歧中心商给出

Rubin §11.2 的类域论正合列在目标字符上为
$$
0\longrightarrow B_p\longrightarrow M_p
\longrightarrow\mathcal A_p\longrightarrow0,
\qquad
B_p=(U_\infty/E_\infty)^{\widetilde\chi}.
\tag{3.1}
$$
其中 $B_p$ 正是局部惯性在全局 $X_\infty^{\widetilde\chi}$ 中的像。

取 $s\in S_p$，令 $f_s:M_p\to W$ 为 (1.3) 对应的同态。这个同构来自全局限制映射及互反律，因而与局部限制相容；这是 Rubin Proposition 12.2 以及其有限层来源 Theorem 6.9 所用的相容性。

若 $s$ 在 $k$ 处为零，则其在 $k_\infty$ 的局部惯性上为零，所以 $f_s(B_p)=0$。反过来，若 $f_s(B_p)=0$，则限制到 $k_\infty$ 的局部类在惯性上为零。它通过 (2.4) 的未分歧 $\mathbb Z_p$ 商因子化，再由 (2.5) 为零；(2.3) 的单射性于是给出 $\operatorname{loc}_{\mathfrak p}(s)=0$。因此
$$
S_p^{\rm str}
=\operatorname{Hom}_{G,\rm cont}(\mathcal A_p,W).
\tag{3.2}
$$
在右端，$\Delta$ 已通过投影 $e_{\widetilde\chi}$ 处理，而 $\Gamma$-等变性正是
$f((T-p)a)=0$。这就得到 (1.4)。

值得区分两个局部条件：usual Selmer 只要求消去 $\ker\delta_\infty$ 的 Artin 像，R27 证明这个要求在本分量自动满足；strict Selmer 则要求消去**整个** $U_\infty^{\widetilde\chi}$ 的像。式 (2.5) 保证后一个条件没有漏掉未分歧局部类。

## 4. 固定非挠点强迫局部像恰有余秩一

令 $H_{f,p}$ 为局部 Kummer 像：
$$
H_{f,p}
=\operatorname{im}\left(
E(k)\otimes_{\mathcal O_K}(K_{\mathfrak p}/\mathcal O_{K,\mathfrak p})
\longrightarrow H^1(k,W)\right).
\tag{4.1}
$$
该映射单射。椭圆形式群对数把 $E(k)$ 的一个有限指数开子群识别为 $\mathbb Z_p$ 中的一个非零格，故
$$
H_{f,p}\simeq\mathbb Q_p/\mathbb Z_p.
\tag{4.2}
$$
也可直接应用 Rubin Lemma 6.6；本素数范围的非异常性已在 R7、R24 核查。

取 R4 中的固定非挠点
$$
P=(-1,4)\in E(\mathbb Q)\subset E(K).
$$
选一个正整数 $N$，使 $NP$ 落在形式群对数为单射的开子群中。必须有 $\log_E(NP)\ne0$：否则 $NP=O$ 已在 $E(k)$ 中成立，从而在 $E(K)$ 中成立，与 $P$ 非挠矛盾。因此 $\log_E(NP)$ 在局部对数格中生成一个有限指数 $\mathbb Z_p$ 子模。

将这个非零格的包含张量 $\mathbb Q_p/\mathbb Z_p$，所得映射是该可除群上的非零 $\mathbb Z_p$ 标量乘法，故为满射。因此 $P$ 所生成的全局 Mordell–Weil 子模的 Kummer 像，局部化后已经满射到 $H_{f,p}$。全局 Mordell–Weil Kummer 像包含于 $S_p$，而 usual Selmer 的局部像包含于 $H_{f,p}$。于是
$$
\boxed{\quad
0\longrightarrow S_p^{\rm str}
\longrightarrow S_p
\xrightarrow{\operatorname{loc}_{\mathfrak p}}H_{f,p}
\longrightarrow0.
\quad}\tag{4.3}
$$
不需要先证明整个 $H^1(k,W)$ 等于 Kummer 像；(4.3) 只使用被 Selmer 条件指定的 $H_{f,p}$。

由 (1.4)、(4.2)、(4.3) 取余秩，得到
$$
s_{\infty,p}=q_p+1.
\tag{4.4}
$$
R7 的 $p$-parity 给 $s_{\infty,p}$ 为偶数，R4 的秩二又给它至少为二，所以 $q_p$ 为正奇数。这证明 (0.1)。

### 4.1 中心模上的整正合列

R27 已证明
$$
(\ker\delta_\infty)^{\widetilde\chi}
=\mathfrak P U_\infty^{\widetilde\chi},\qquad
\delta_\infty:
U_\infty^{\widetilde\chi}/\mathfrak P U_\infty^{\widetilde\chi}
\xrightarrow{\sim}T_\pi E.
$$
Rubin Lemma 6.8 的局部 Kummer 配对因而将 $H_{f,p}$ 识别为
$$
\operatorname{Hom}_{\rm cont}
\left(U_\infty^{\widetilde\chi}/\mathfrak P U_\infty^{\widetilde\chi},W\right).
$$
对 (4.3) 取 Pontryagin 对偶，并使用上述配对及 (1.3)–(1.4)，可得自然的整正合列
$$
\boxed{\quad
0\longrightarrow
U_\infty^{\widetilde\chi}/\mathfrak P U_\infty^{\widetilde\chi}
\longrightarrow C_p\longrightarrow D_p\longrightarrow0.
\quad}\tag{4.5}
$$
左端为自由秩一 $\mathbb Z_p$-模。这说明 R30 在中心商处留下的可能 Tor 退化，不能使局部惯性像消失。式 (4.5) 不声称该嵌入在 $C_p$ 的自由部分中原始，也不把 $D_p$ 的有限挠子直接认作 $\Sha$ 的有限部分。

## 5. 第一高阶 Fitting 理想与一个辅助素数

由秩二的无穷 Kummer 列和 (4.4)，
$$
\boxed{\quad
\operatorname{corank}_{\mathbb Z_p}\Sha(E/\mathbb Q)[p^\infty]
=q_p-1.
\quad}\tag{5.1}
$$
有限生成对偶保证余秩零等价于初级群有限，故
$$
\boxed{\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\iff q_p=1
\iff\operatorname{Fitt}_{\Lambda,1}(\mathcal A_p)
\not\subset(T-p).
\quad}\tag{5.2}
$$
最后一个等价由 R30 §4 的局部生成元数判据得到：
$(\mathcal A_p)_{\mathfrak P}$ 在 DVR $\Lambda_{\mathfrak P}$ 上恰需 $q_p$ 个生成元。仍然只要求中心评价**非零**，不要求为单位。

R32 已对每个 $i\ge0$ 证明有限层完整理想的相等
$$
\Theta^{\rm RS}_{i,n}
=\operatorname{Fitt}_{R_n,i}(A_n),\qquad
e_n(\Theta^{\rm RS}_{i,n})
=\operatorname{ev}_{T=p}
\bigl(\operatorname{Fitt}_{\Lambda,i}(\mathcal A_p)\bigr)
\pmod{p^n},
\tag{5.3}
$$
其中 $R_n=\mathbb Z_p[\Gamma/\Gamma^{p^{n-1}}]$、
$e_n(T)=p\pmod{p^n}$，并使用固定 $T$-修正素数 $(67)$。
取 $i=1$ 得到新的等价判据
$$
\boxed{\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\iff\exists n\ge1:
e_n(\Theta^{\rm RS}_{1,n})\ne0.
\quad}\tag{5.4}
$$
这里的生成元来自一个完全分裂于 $K_n/K$ 的辅助素数 $\mathfrak q$、一个 rank $2$ Rubin–Stark 元素，以及两个 $R_n$-线性单位泛函的外积值。若 (5.4) 成立，理想的生成元中至少有一个具有非零评价，所以一个这样的辅助素数及一个值就给有限证书。

R32 的 rank $3$ / 第二维 Fitting 判据仍然成立：在本算术对象上，$q_p\le2$ 与 $q_p=1$ 等价。单辅助素数降低外积秩，但不保证所需 $p$-adic 精度更低。

## 6. 有限类群增长和两种证书的精度

采用 R33 的有限群
$$
C_{p,n}=A_n/(\gamma_n-(1+p))A_n
\simeq D_p/p^nD_p,
$$
以及
$$
d_{p,n}=\log_p|C_{p,n}|-\log_p|C_{p,n-1}|.
$$
R33 已证明它单调不增并最终等于 $q_p$。本结果进一步给出
$$
\boxed{\quad
\lim_{n\to\infty}d_{p,n}\text{ 是正奇数},\qquad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\iff\exists n:\ d_{p,n}=1.
\quad}\tag{6.1}
$$
原有条件 $\exists n:d_{p,n}\le2$ 仍然是准确且可能更早出现的证书，不能用 (6.1) 抹去这一优势。

具体地，当 $q_p=1$ 时写
$$
D_p\simeq\mathbb Z_p\oplus
\bigoplus_{j=1}^{t}\mathbb Z/p^{a_j}\mathbb Z,
\qquad 1\le a_1\le\cdots\le a_t.
$$
则 $d_{p,n}=1$ 首次发生于 $n=1+\max_j a_j$；空集最大值取零。另一方面，Fitting 理想基变换给
$$
\operatorname{ev}_{T=p}\operatorname{Fitt}_{\Lambda,1}(\mathcal A_p)
=\operatorname{Fitt}_{\mathbb Z_p,1}(D_p)
=(p^{a_1+\cdots+a_t}).
\tag{6.2}
$$
故 rank $2$ Rubin–Stark **值理想**的模 $p^n$ 证书首次非零于
$$
n=1+\sum_j a_j.
\tag{6.3}
$$
相比之下，R33 的第一处 $d_{p,n}\le2$ 只需越过第二大的有限挠子指数；第二维 Fitting 的精度指数也只用除最大指数以外的总和。这些都是给定模的精度比较，不预设类群或 Rubin–Stark 元素已经算出。

## 7. 当前新增的算术内容和未闭合步骤

新增的输入是固定非挠点 $P$ 在局部有非零椭圆对数，故它的可除 Kummer 子群在局部满射。这排除了 R30 中 $s_{\infty,p}=q_p$ 的分支，并把中心类群的必需生成元数从“至多二”收紧为“恰一”。它没有把中心零点的代数重数收紧为一，也没有给任何素数间的类群比较。

现在可针对一个辅助素数研究 (5.4) 的 rank $2$ 行列式；仍须证明这一非零性对无穷多个目标 $p$ 发生。Chebotarev 为每个固定 $p,n$ 提供无穷多个可选辅助素数，本身不保证它们的 Rubin–Stark 评价非零。本文尚未解决这个跨素数步骤，因此课题主目标仍未完成。

## 来源

- K. Rubin，*Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，SWC 讲义，Lemmas 6.6、6.8，Theorem 6.9，§11.2 式 (13)，Proposition 12.2 和 Theorem 12.3：[原文](https://swc-math.github.io/notes/files/99RubinCM.pdf)。这些结果分别提供局部对数/Kummer 配对、局部与全局互反律的相容性和 Selmer 控制。
- 本仓库 R4、R7、R24、R25、R27：固定秩二曲线、非异常性、Selmer 比较与 parity、局部单位自由性以及中心处的准确 Selmer 同构。
- 本仓库 R30、R32、R33：处处无分歧模、已出版 ETNC–Rubin–Stark 输入的完整有限层 Fitting 理想、有限中心类群商的准确增长公式。
