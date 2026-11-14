# R25：μ=0 与无有限子模控制有限 Selmer，双权判据加强为初级零

**可信度：已证明。** 固定 $E:y^2=x^3-17x$、$K=\mathbb Q(i)$，设
$$
p\ge13,\qquad p\equiv1\pmod4,\qquad p\ne17.
$$
使用 R20、R24 的单个 $\mathfrak p$ 除法塔及参数
$$
L_\infty=K(E[\mathfrak p^\infty]),\quad
G_\infty=\Delta\times\Gamma,\quad
\rho_E(\gamma)=1+p,\quad T=\gamma-1,
$$
以及 $\chi=\rho_E|_\Delta$。设 $X_\infty$ 是 $L_\infty$ 上仅在 $\mathfrak p$ 以上允许分歧的极大阿贝尔 pro-$p$ 扩张的 Galois 群，令
$$
M_p=X_\infty^\chi,
\qquad \operatorname{char}_{\mathbb Z_p[[T]]}(M_p)=(H_p(T)).
$$
R24 的 $H_p$ 正可这样取，记它的 Iwasawa $\lambda$ 不变量为 $\lambda_p^{\mathrm{Iw}}$。

## 0. 结论

对全部所列素数，无须预设 $\Sha$ 有限，有
$$
\boxed{\quad
\dim_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q)
\le\lambda_p^{\mathrm{Iw}}.
\quad}\tag{0.1}
$$
因此
$$
\lambda_p^{\mathrm{Iw}}\le3
\quad\Longrightarrow\quad
\Sha(E/\mathbb Q)[p^\infty]=0.\tag{0.2}
$$
这比仅使用 $p^\infty$-Selmer 余秩所得的“有限”更强。

结合 R24，双权充分条件也升级为零：
$$
\boxed{\quad
\min\{v_{\mathfrak p}(a_{(p-3)/2}),v_{\mathfrak p}(a_{p-2})\}\le3
\quad\Longrightarrow\quad
\Sha(E/\mathbb Q)[p^\infty]=0.
\quad}\tag{0.3}
$$
等价地，$v_p(c_p^+)\le3$ 或 $v_p(c_{2p-1}^+)\le2$ 均足够。没有证明这些条件在无穷多个 $p$ 上成立。

## 1. 把 μ=0 与“无有限子模”同时用上

以下代数事实是关键，不能仅凭特征理想忽略有限误差。

**引理 1。** 设 $\mathcal A=\mathbb Z_p[[T]]$，$M$ 是有限生成 torsion $\mathcal A$-模，$\mu(M)=0$，且 $M$ 没有非零有限 $\mathcal A$-子模。那么 $M$ 是秩 $\lambda(M)$ 的自由 $\mathbb Z_p$-模。因此
$$
\dim_{\mathbb F_p}M/(p,T)M\le\lambda(M).\tag{1.1}
$$

**证明。** Iwasawa 模结构定理给出一个有限核、有限余核的伪同构，将 $M$ 与有限个 $\mathcal A/(F_i)$ 的直和比较。因为 $\mu(M)=0$，所有 $F_i$ 都可取为 distinguished polynomial，且没有 $\mathcal A/(p^a)$ 因子。

每个 $\mathcal A/(F_i)$ 都是秩 $\deg F_i$ 的自由 $\mathbb Z_p$-模；伪同构的核、余核有限，故 $M$ 本身是有限生成的 $\mathbb Z_p$-模，且
$$
\operatorname{rank}_{\mathbb Z_p}M
=\sum_i\deg F_i=\lambda(M).
$$
$M$ 的 $\mathbb Z_p$-挠子群于是有限。它在 $T$ 作用下稳定，是一个有限 $\mathcal A$-子模；由假设必须为零。故 $M$ 为所述自由模。最后 $M/(p,T)M$ 是 $M/pM$ 的商，而后者维数为 $\lambda(M)$，得到 (1.1)。$\square$

对本题的 $M_p$，引理的两个算术输入均已成立：

- Schneps 1987，Theorem IV，直接对 $K(E[\mathfrak p^\infty])$ 的上述 $X_\infty$ 证明 $\mu(X_\infty)=0$；其条件为类数一 CM、分裂好素数 $p>3$。整字符分解于是给 $\mu(M_p)=0$，见 [μ/λ 笔记](../notes/2026-11-12-coleman-mu-lambda-attempt.md) 第 1 节。
- Rubin，Proposition 11.3(ii)，给出 $X_\infty$ 没有非零 pseudo-null 子模。在这里的单变量 Iwasawa 代数中，pseudo-null 与有限等价；该性质传给直和因子 $M_p$。

故无条件得到
$$
M_p\simeq\mathbb Z_p^{\lambda_p^{\mathrm{Iw}}}
\quad\text{作为 }\mathbb Z_p\text{-模}.\tag{1.2}
$$
这里特意使用 $\mathfrak p$-分歧 Galois 模 $X_\infty$。不能对其他只有相同特征理想、却可能带有限子模的模直接使用 (1.2)。例如
$$
\mathcal A/(T-p)^2\oplus\bigl(\mathcal A/(p,T)\bigr)^N
$$
的 $\mu=0,\lambda=2$ 与 $N$ 无关，而模 $(p,T)$ 的维数为 $N+1$。排除有限子模正是消除这个误差的必要步骤。

## 2. 有限 Selmer 到无穷层的注入

记 $V=E[\mathfrak p]$、$W=E[\mathfrak p^\infty]$。R7 已证明
$$
W(K)=0.\tag{2.1}
$$
直接证书是：$E$ 在 $K$ 中位于 $3$ 上方的素点好约化，剩余域为 $\mathbb F_9$，且 $\#E(\mathbb F_9)=16$。任何奇分裂 $p$ 的有理挠点都必须注入此群，所以没有 $p$ 挠；任何非零 $p$-幂挠点又会产生非零 $p$ 挠。

对短正合列
$$
0\longrightarrow V\longrightarrow W
\xrightarrow{\pi}W\longrightarrow0
$$
取全局上同调。由 (2.1)，得到单射（事实上在目标 $\pi$-挠中为同构）
$$
H^1(K,V)\hookrightarrow H^1(K,W)[\pi].\tag{2.2}
$$
有限与无穷 Kummer 映射相容。因此局部 Kummer 像经 (2.2) 落入无穷层的局部 Kummer 像，给出
$$
\operatorname{Sel}_{\pi}(E/K)
\hookrightarrow\operatorname{Sel}_{\mathfrak p^\infty}(E/K)[\pi].
\tag{2.3}
$$
这里仅需要注入，不要求任何控制定理的余核为零。

Rubin Proposition 12.2(i) 将 extended Selmer 群识别为
$$
\operatorname{Sel}'_{\mathfrak p^\infty}(E/K)
=\operatorname{Hom}_{\mathrm{cont}}(X_\infty,W)^{G_\infty}
=\operatorname{Hom}_{\mathrm{cont}}(M_p,W)^\Gamma.
\tag{2.4}
$$
通常 Selmer 是该群的子群；本文不把二者混同。对 (2.4) 取 $[\pi]$，再与 (2.3) 复合，得到
$$
\operatorname{Sel}_\pi(E/K)
\hookrightarrow\operatorname{Hom}_{\mathrm{cont}}(M_p,V)^\Gamma.
\tag{2.5}
$$
这是因为一个取值于 $W$ 的同态被 $\pi$ 消灭，恰当且仅当其像包含于 $V$。

### 2.1 限制映射的核没有额外字符项

为检查 (2.4) 的下降方向，$G_\infty=\Delta\times\Gamma$ 是阿贝尔群，$\Delta$ 通过非平凡的 $\chi$ 作用在 $V$、$W$ 上。可以选 $\delta\in\Delta$，使 $\chi(\delta)-1\in\mathbb Z_p^\times$。$\Delta$ 对 $\Gamma$ 的共轭作用平凡，故在 $H^b(\Gamma,V)$ 与 $H^b(\Gamma,W)$ 上也通过该标量作用。

有限群 $\Delta$ 的阶 $p-1$ 在这些 $p$ 初级模上可逆。Hochschild–Serre 谱序列的 $\Delta$ 不变部分因上述非平凡单位标量而为零，其更高上同调也由平均算子为零。因此
$$
H^i(G_\infty,V)=H^i(G_\infty,W)=0
\qquad(i\ge0).
$$
全局限制到 $L_\infty$ 的 inflation–restriction 列遂没有核项；不存在必须另加的 $H^1(G_\infty,V)$ 维数。放宽 $\mathfrak p$ 处局部条件并在其他位置保留非分歧条件，正给出 (2.4) 的极大 $\mathfrak p$-分歧阿贝尔 pro-$p$ 商，这也是 Rubin 的 Proposition 12.2 所识别的对象。

## 3. 有限 Selmer 维数至多 λ

$\Gamma$ 在 $V$ 上作用平凡，因为 $\rho_E(\Gamma)=1+p\mathbb Z_p$。因此
$$
\operatorname{Hom}_{\mathrm{cont}}(M_p,V)^\Gamma
=\operatorname{Hom}_{\mathbb F_p}
\bigl(M_p/(p,T)M_p,V\bigr).
\tag{3.1}
$$
$V$ 是一维 $\mathbb F_p$ 空间。由 (2.5)、(3.1) 和引理 1，
$$
\dim_{\mathbb F_p}\operatorname{Sel}_\pi(E/K)
\le\dim_{\mathbb F_p}M_p/(p,T)M_p
\le\lambda_p^{\mathrm{Iw}}.
$$
R7 的有限层限制、复共轭和 CRT 投影给出
$$
\operatorname{Sel}_p(E/\mathbb Q)
\simeq\operatorname{Sel}_\pi(E/K).
$$
于是得到 (0.1)。没有预设 $\Sha$ 有限，也没有将伪同构当成模 $p$ 后的同构。

R4 给出 $\operatorname{rank}E(\mathbb Q)=2$、$E(\mathbb Q)[p]=0$。R7 §9.5 利用 $p$-parity 及 Cassels–Tate 在有限商上的交错性，无条件证明
$$
s_p^{\mathrm{fin}}:=\dim_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q)
\text{ 为偶数，且 }s_p^{\mathrm{fin}}\ge2.
$$
所以 $\lambda_p^{\mathrm{Iw}}\le3$ 强迫 $s_p^{\mathrm{fin}}=2$。有限 Kummer 列给出 $\Sha(E/\mathbb Q)[p]=0$；任意非零 $p$ 初级挠群都会含有非零 $p$ 挠，故整个 $\Sha[p^\infty]$ 为零。这证明 (0.2)。

更一般地，(0.1) 和奇偶性还给出
$$
\dim_{\mathbb F_p}\Sha(E/\mathbb Q)[p]
\le2\left\lfloor\frac{\lambda_p^{\mathrm{Iw}}}{2}\right\rfloor-2.
\tag{3.2}
$$
此式约束 $p$-挠维数，不是有限群阶的上界。

## 4. 双权判据的加强

R24 写 $H_p=(T-p)^2G_p$、$G_p=g_0+g_1T+\cdots$，并证明
$$
v_p\lambda_p=v_pH_p((1+p)^p-1),
\qquad
v_p\lambda_{2p-1}=v_pH_p((1+p)^{2p-1}-1),
$$
其中仍以 $\lambda_k=\delta^k\log\Phi(O)$ 表示对数矩。

若 $v_p\lambda_p\le3$，R20 已证明 $\Sha[p^\infty]=0$。余下只需考虑
$$
v_p\lambda_p\ge4,
\qquad v_p\lambda_{2p-1}\le3.
$$
R24 §6 的精确两点展开证明，此时
$$
g_0\in p^2\mathbb Z_p,
\qquad g_1\in\mathbb Z_p^\times.
$$
故 $G_p\bmod p$ 的第一个非零系数恰在一次项，
$$
\mu(G_p)=0,
\qquad\lambda(G_p)=1,
\qquad\lambda_p^{\mathrm{Iw}}=3.
$$
使用 (0.2)，再次得到 $\Sha[p^\infty]=0$。结合 R24 的
$$
\lambda_p=4a_{(p-3)/2},\qquad
\lambda_{2p-1}=4a_{p-2},
$$
以及 $(2p-2)!$ 的 $p$-赋值为一，便得到 (0.3) 和它的临界值版本。

因此 R24 对第二权保留的“有限”现在已被加强为“零”。加强用到的是 $X_\infty$ 的无有限子模及有限 Selmer 注入，而非仅仅中心零点阶或局部深度。特别地，$\nu_p\ge4$ 本身仍不决定初级部分；第二权提供了 $g_1$ 的额外信息。

## 5. 留下的跨素数问题

本结果使原来的两条充分路线准确接合：对无穷多个 $p$ 证明 $\lambda(H_p)\le3$，或者证明两个指定对数矩不同时被 $p^4$ 整除，都足以给初级部分为零。但 $\mu=0$ 没有给出所需 $\lambda$ 上界，R24 的两个低次系数也尚未得到无穷次非消失。完成标准仍未达到。

## 引用

- L. Schneps, *On the μ-invariant of p-adic L-functions attached to elliptic curves with complex multiplication*, J. Number Theory **25** (1987), 20–33，Theorem IV；[作者全文](https://webusers.imj-prg.fr/~leila.schneps/Schnepsmu.pdf)，[DOI](https://doi.org/10.1016/0022-314X(87)90013-8)。
- K. Rubin, *Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，§11 的结构定理、Proposition 11.3(ii)、Proposition 12.2；[讲义全文](https://swc-math.github.io/notes/files/99RubinCM.pdf)。Proposition 11.3 引用 Greenberg 的无 pseudo-null 子模结果；本文使用讲义给出的原始 Galois 模版本，不对任意类群模外推。
- 本仓库 R4、R7、R20、R24，以及 `notes/2026-11-12-coleman-mu-lambda-attempt.md`。
