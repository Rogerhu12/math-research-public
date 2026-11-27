# 原非分裂 Cartan 的 prime-to-p Chen 同源与奇圆分扭点的平方层归约

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126。

复核：root、global_route、o2_high_coefficient 已各自核读原定理及全文推导。

**状态：已证明的整 $p$ 比较与范围说明。** 以下同源次数与 $p$ 互素，因而可用于真实 $p$ 挠点和 $\mathbb Z_p$ 格。另用 Ohta 的原定理消去比较中 level $p$ 因子的奇圆分扭点。本文不证明 level $p^2$ 的相应奇部消失，也不识别任何指定 Eisenstein 扩张为原圆单位类。

## 1. 固定原曲线与商的身份

设 $p>37$，$K=\mathbb Q(\zeta_p)$，$F=K^+$，$\Delta=\operatorname{Gal}(K/\mathbb Q)$，$c=\sigma_{-1}$。取 de Smit–Edixhoven 原文中的整个 naive full-level 模曲线 $X=X(p)_{\mathbb Q}$：其对象为 $(E,\phi)$，其中 $\phi:\mathbb F_p^2\simeq E[p]$，不事先选一个 Weil pairing 几何分支。$G=\mathrm{GL}_2(\mathbb F_p)$ 在它上作用。

记 $B$ 为 Borel，$T_s,T_{\mathrm{ns}}$ 为 split、nonsplit Cartan，$N_s,N_{\mathrm{ns}}$ 为其正规化子。原商为
$$
X/B=X_0(p),\qquad
X/N_{\mathrm{ns}}=X_{\mathrm{ns}}^+(p),\qquad
X/N_s=X_0(p^2)/\langle w_{p^2}\rangle.                 \tag{1}
$$
最后一个等式是 $\mathbb Q$ 上的实际模曲线身份，亦见 [dSE, Theorem 1 后的显示式，作者 PDF 第 2 页]。

可直接核 (1)：有序 split 结构是 $(E,L_1,L_2)$，两条 $p$ 阶线不同。若 $\phi_i:E\to E/L_i$，则
$$
\phi_2\circ\phi_1^\vee:E/L_1\longrightarrow E/L_2
$$
的次数为 $p^2$，核是循环群。反过来，循环 $p^2$ 同源的唯一中间 $p$ 商恢复 $E$ 及两条不同的线。交换 $L_1,L_2$ 将该同源换成对偶，即 $w_{p^2}$。所有构造都在基域上定义，并延伸到光滑射影紧化。

设
$$
J_{\mathrm{ns}}=\operatorname{Jac}(X_{\mathrm{ns}}^+(p)),\quad
J_1^{\mathrm{old}}=J_0(p),\quad
J_2^+=\operatorname{Jac}(X_0(p^2)/\langle w_{p^2}\rangle).
$$
这里 $J_2^+$ 首先表示**商曲线的 Jacobian**。它与 $J_0(p^2)$ 的 Fricke 正部分在 $p$ 挠点上相同，因为商映射的拉回、推前合成为 $[2]$，而 $2\in\mathbb Z_p^\times$。

## 2. de Smit–Edixhoven 的整定理允许取辅助素数为 $p$

[dSE, Theorem 3，作者 PDF 第 4 页] 将其函子性正规化子关系提升为 $\mathbb Z_{(\ell)}$ 关系，只要求 $\ell\nmid p-1$。特别是 $\ell=p$ **满足**这个条件；原证明还显式处理了 $\ell=\operatorname{char}\mathbb F_p$ 的情形，并不要求 $\ell\nmid|G|$。

在置换模层，所用关系是
$$
\mathbb Z_{(p)}[G/N_s]\oplus\mathbb Z_{(p)}
 \simeq
\mathbb Z_{(p)}[G/N_{\mathrm{ns}}]
 \oplus\mathbb Z_{(p)}[G/B].                            \tag{2}
$$
故不需要、也没有使用 $1/|G|$ 的平均。

[dSE, Theorem 4 及证明，作者 PDF 第 5–6 页] 将这个关系落实到实际 Jacobian，并给出 $\mathbb Q$ 同源
$$
\varphi:J_2^+\longrightarrow J_{\mathrm{ns}}\times J_0(p),
\qquad p\nmid\deg\varphi.                              \tag{3}
$$
实际商 Jacobian 的拉回核必须在这一步检查。原证明把它们识别为最大无分歧交换子覆盖群的 Cartier 对偶：对于 $N_s,N_{\mathrm{ns}}$，核为 $2$ 群；对于 $B$，核的阶整除 $p-1$。这正足以从 (2) 得到 (3)，没有遗漏一个可能含 $p$ 的商映射核。

关系 (2) 在带 $G$ 作用的对象上是函子性的。原 full-level 上次数与 $p$ 互素的 Hecke pull–push 与 $G$ 换标记作用交换，并下降成 (1) 各商的标准 Hecke 对应。因而可以选择 (3) 与全部 $T_n$、$(n,p)=1$ 交换：先取 $\mathbb Z_{(p)}$ 范畴中的函子性同构，再以一个与 $p$ 互素的整数清分母。上述 split 中间商解释也核实了这确是标准 level $p^2$ 的 prime-to-$p$ Hecke 作用。

## 3. 真实 $p$-divisible、整 Tate 和上同调接口

由 $p\nmid\deg\varphi$，对每个 $a\ge1$，(3) 诱导 $\mathbb Q$ 上有限群方案的同构
$$
J_2^+[p^a]\simeq
J_{\mathrm{ns}}[p^a]\oplus J_0(p)[p^a].                \tag{4}
$$
例如取同源的准逆 $\psi$，使 $\psi\varphi=[d]$、$\varphi\psi=[d]$，其中 $p\nmid d$；则在 $p^a$ 挠点上用 $d^{-1}\psi$ 即得逆映射。这也说明同构在改变 $a$ 时相容。

因此有 $G_{\mathbb Q}$ 等变同构
$$
J_2^+[p^\infty]\simeq
J_{\mathrm{ns}}[p^\infty]\oplus J_0(p)[p^\infty],
\qquad
T_pJ_2^+\simeq T_pJ_{\mathrm{ns}}\oplus T_pJ_0(p).
                                                               \tag{5}
$$
这里是特征零上的真实 $p$-divisible 群及其整 Tate 格。本文没有借 (5) 额外声称某个坏约化整模型上的连通部分已被指定。

对任意扩域 $L/\mathbb Q$，取 $G_L$ 不变量或连续 Galois 上同调，得到
$$
\begin{aligned}
J_2^+(L)[p^a]&\simeq
J_{\mathrm{ns}}(L)[p^a]\oplus J_0(p)(L)[p^a],\\
H^1(G_L,J_2^+[p^a])&\simeq
H^1(G_L,J_{\mathrm{ns}}[p^a])
 \oplus H^1(G_L,J_0(p)[p^a]).                          \tag{6}
\end{aligned}
$$
同样，(5) 的 $\mathbb Z_p$ 对偶给相应光滑射影曲线的整 $H^1_{\mathrm{et}}(-,\mathbb Z_p)$ 直和。式 (4)–(6) 均保 prime-to-$p$ Hecke 作用。对 $L=K$，因 (3) 在 $\mathbb Q$ 定义，还保 $\Delta$ 的每个角色；这不是只有半单化或张量 $\mathbb Q_p$ 后的比较。

这些同构依赖于同源的选择。它们不自动保原 cuspidal divisor 的指定生成元、全 cusp 平均的规范、Weil pairing／极化的指定尺度，亦不声明 $U_p$ 相容。若要运输这些额外结构，仍须分别证明。

## 4. Ohta 原定理消去 level $p$ 因子的全部奇圆分 $p$ 扭点

为忠实保原来源，令 $X_1^{\mathrm{arith}}(p)$ 表示 Ohta 使用的曲线：对象是 $(E,\alpha:\mu_p\hookrightarrow E[p])$；令 $J_1^{\mathrm{arith}}(p)$ 为其 Jacobian。下面只用它忘记 $\alpha$、保留其像的实际 $\mathbb Q$ 映射
$$
\pi:X_1^{\mathrm{arith}}(p)\longrightarrow X_0(p),
\qquad \deg\pi=(p-1)/2.                               \tag{7}
$$
所以无须在此隐含交换 arithmetic 与 naive 的 $X_1$ 规范。

考虑
$$
W=J_1^{\mathrm{arith}}(p)(K)[p]^-
 =\{P:cP=-P\}.
$$
$W$ 对 $G_F$ 稳定；$G_K$ 在其上平凡，而 $G_F/G_K$ 的非平凡元 $c$ 作用为 $-1$。在 $\mu_p$ 上也是同一作用，故 $W$ 对应的 $F$-有限群方案为若干个 $\mu_p$ 的直和。特别地，它的 Cartier 对偶是常值群方案，正是 [O, Introduction] 所用的 $\mu$-type。

在 [O, Theorem 5.1.4] 中取
$$
N=1,\qquad k_0=\mathbb Q,\qquad A=\{1,-1\},
\qquad k_A=F.                                        \tag{8}
$$
定理的 $p\nmid N\phi(N)$、$[k_0:\mathbb Q]$ 与 $p$ 互素、$k_0$ 在 $p$ 无分歧、$A\ne\{1\}$ 均满足。$\langle-1\rangle$ 在 $X_1^{\mathrm{arith}}(p)$ 上是恒等：$(E,\alpha)$ 与 $(E,-\alpha)$ 经 $[-1]_E$ 同构。于是其在 Jacobian 上也恒等，定理给
$$
J_1^{\mathrm{arith}}(p)(K)[p]^-=0.                    \tag{9}
$$
原定理允许 $N=1$；其证明在需要 fine moduli 时才引入与 $p$ 互素的辅助覆盖，将 $N$ 化到至少 $5$。这不是定理范围中的额外 $N\ge5$ 限制。

由 $\pi_*\pi^*=[(p-1)/2]$，(7) 在 $p$ 挠点上给 $\mathbb Q$ 定义的单射
$$
J_0(p)[p]\hookrightarrow J_1^{\mathrm{arith}}(p)[p].
$$
故
$$
J_0(p)(K)[p]^-=0.                                    \tag{10}
$$
同样没有非零奇 $p$ 次幂扭点：若有奇部中阶为 $p^a$ 的点，乘以 $p^{a-1}$ 会违背 (10)。因此
$$
J_0(p)(K)[p^\infty]^-=0.                             \tag{11}
$$
此处没有把一般 $p^a$ 阶子群直接称为 $F$ 上 $\mu_{p^a}$ 型；只先对阶 $p$ 应用 Ohta，再取阶 $p$ 子点。

## 5. 原奇扭点障碍的精确平方层归约

将 (11) 代入 (5)–(6)，得到真实 $\Delta$ 模及 prime-to-$p$ Hecke 模同构
$$
J_{\mathrm{ns}}(K)[p^\infty]^-
 \simeq J_2^+(K)[p^\infty]^-,
\qquad
J_{\mathrm{ns}}(K)[p]^-
 \simeq J_2^+(K)[p]^-.                               \tag{12}
$$
这准确定位了
[原 cuspidal $K_2$ 工作笔记](2026-11-27-original-cuspidal-K2-torsion-and-odd-Jacobian-obstruction.md)
中的奇 Jacobian 残余：它可在 Fricke 正平方层的实际整 $p$ 扭点中研究；level $p$ 因子对该残余无贡献。

式 (12) **没有**断言右侧为零。Ohta 的原定理仍要求 $p\nmid N$，不能令 $N=p$ 而把它直接用于 $J_1(p^2)$。特别是一个抽象半单角色对
$$
\mathbb F_p(\omega^r),\quad
\mathbb F_p(\omega^{1-r})
$$
尚不能给原整 Jacobian 中某一特定短正合列。若后来得到这一实际列，仍须按前述 $K_2$ 笔记 §7 区分扩张方向：偶在下、奇在上时，其 Kummer radical 是 $\omega^{2-2r}$；反向时是 $\omega^{2r}$。本文不把原 $\beta_r$ 未经角色识别地接入该列。

## 6. 原始来源与核读范围

- [dSE] Bart de Smit、Bas Edixhoven，*Sur un résultat d'Imin Chen*，Mathematical Research Letters 7 (2000)，DOI [10.4310/MRL.2000.v7.n2.a1](https://doi.org/10.4310/MRL.2000.v7.n2.a1)。实际核读 [作者 2000-02-09 PDF](https://pub.math.leidenuniv.nl/~smitbde/papers/2000-de_Smit_Edixhoven.pdf)：第 2 页的商曲线身份及 Theorem 2 的函子性，第 4 页 Theorem 3，第 5–6 页 Theorem 4 及其商映射核证明。尤其已核 $\ell=\operatorname{char}\mathbb F_p$ 的单列论证。
- [O] Masami Ohta，*$\mu$-type subgroups of $J_1(N)$ and application to cyclotomic fields*，J. Math. Soc. Japan 72 (2020), 333–412，DOI [10.2969/jmsj/78327832](https://doi.org/10.2969/jmsj/78327832)。核读 [正式 PDF](https://www.jstage.jst.go.jp/article/jmath/72/2/72_333/_pdf)：Introduction 的 $\mu$-type 定义；印刷第 399–400 页（PDF 第 67–68 页）Definition 5.1.3、Theorems 5.1.4/5.1.7、以及 $N=1$ 仍在范围内的辅助层说明。

本笔记无新数值计算。一般 $p$ 的实际 Eisenstein 整层、指定 Kummer 扩张类及后续非交换覆盖仍未完成。
