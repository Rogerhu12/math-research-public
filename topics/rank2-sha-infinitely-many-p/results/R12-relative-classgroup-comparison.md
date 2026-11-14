# R12：全 $p$ 除法域类群与单 $\pi$ 相对类群的明确同构

**可信度：已证明。** 固定 R4、R7 的曲线与素数范围
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),\qquad
p\equiv1\pmod4,\quad p\ge13,\quad p\ne17,
$$
并固定 $p=\pi\bar\pi$。本文证明 R7 的全 $p$ 除法域类群维数 $c_p$，与 De–Majumdar–Mondal 的单 $\pi$ 除法域相对类群维数 $r_\pi(E)$ **完全相同，没有遗漏的核、余核或局部修正项**。同构可由理想范数、复共轭和理想扩张逐一写出。

## 1. 记号与结论

令
$$
M=K(E[p]),\qquad L=K(E[\pi]),\qquad\bar L=K(E[\bar\pi]),
$$
并记 $\Delta=\operatorname{Gal}(M/K)$。CM 作用使 $\Delta$ 嵌入
$\mathbb F_p^\times\times\mathbb F_p^\times$，所以 $p\nmid[M:K]$。
记在两条挠点直线上的 Galois 特征为
$$
\chi_\pi,\chi_{\bar\pi}:\Delta\longrightarrow\mathbb F_p^\times.
$$
它们分别通过 $\operatorname{Gal}(L/K)$ 与 $\operatorname{Gal}(\bar L/K)$ 因子化。对 $\mathbb F_p$-模用上标 $\chi$ 表示特征子空间。

设 $B\subset L$ 为唯一满足 $[L:B]=4$ 的中间域。取相对类群的 $p$-初等部分为
$$
A_{L/B}:=\ker\bigl(N_{L/B}:\operatorname{Cl}(L)[p^\infty]
\longrightarrow\operatorname{Cl}(B)[p^\infty]\bigr).
$$
若相对类群采用除以基域类群的定义，则第 4 节的投影给出与此定义相同的规范 $p$-初等分块。

结论是有明确同构
$$
\boxed{\quad
\operatorname{Cl}(M)[p]^{\chi_{\bar\pi}}
\xrightarrow{\sim}
A_{L/B}[p]^{\chi_\pi}.
\quad}\tag{1.1}
$$
因此
$$
c_p:=\dim_{\mathbb F_p}\operatorname{Cl}(M)[p]^{\chi_{\bar\pi}}
=\dim_{\mathbb F_p}A_{L/B}[p]^{\chi_\pi}
=r_\pi(E).\tag{1.2}
$$
除了把字符作 Teichmüller 提升外，同一论证也适用于整个 $p$-初等类群分量。

## 2. 与 $p$ 互素的扩张次数：有分歧时同样无核、无余核

设 $N/F$ 为次数 $n$ 的有限 Galois 扩张，群为 $H$，且 $p\nmid n$。理想扩张 $j$ 与理想范数 $N_{N/F}$ 在类群上满足
$$
N_{N/F}\circ j=[n],\qquad
j\circ N_{N/F}=\sum_{g\in H}g.\tag{2.1}
$$
这些恒等式**不要求无分歧**。具体地，若 $\mathfrak P$ 位于 $\mathfrak q$ 之上，分歧指数、剩余次数为 $e,f$，则
$$
N_{N/F}(\mathfrak P)=\mathfrak q^f,
\qquad
j(\mathfrak q)=\prod_{\mathfrak Q\mid\mathfrak q}\mathfrak Q^e.
$$
故 $jN(\mathfrak P)=\prod_{\mathfrak Q\mid\mathfrak q}\mathfrak Q^{ef}$。另一方面，$\mathfrak P$ 的分解群阶为 $ef$，所以 $\prod_{g\in H}g\mathfrak P$ 中每个共轭素理想也恰出现 $ef$ 次。这证明第二式；第一式则由 $efg=n$ 直接得到。主理想在两种映射下仍为主理想，故恒等式下降到类群。

乘 $n$ 在有限 $p$-群上可逆。因此 $j$ 在 $\operatorname{Cl}(F)[p^\infty]$ 上单射。若 $x\in\operatorname{Cl}(N)[p^\infty]^H$，则
$$
j\left(n^{-1}N_{N/F}x\right)
=n^{-1}\sum_{g\in H}gx=x.
$$
从而得到规范同构
$$
j:\operatorname{Cl}(F)[p^\infty]
\xrightarrow{\sim}\operatorname{Cl}(N)[p^\infty]^H,
\qquad j^{-1}=n^{-1}N_{N/F}.\tag{2.2}
$$
这里 $n^{-1}$ 表示 $\mathbb Z_p^\times$ 中的逆作用；限制到 $p$-挠时就是模 $p$ 逆。所谓 ramified ambiguous class 的额外因素不会产生反例，因为它们被扩张次数控制，而本式已在与次数互素的 $p$-初等部分上直接证明。

## 3. 先下降到 $\bar L$，再由复共轭交换字符

由除法域定义，
$$
H=\operatorname{Gal}(M/\bar L)=\ker\chi_{\bar\pi}.
$$
所以 $\operatorname{Cl}(M)[p]^{\chi_{\bar\pi}}$ 全部位于 $H$-不变部分。第 2 节同构与 $\Delta/H$ 作用交换，因而若 $d=[M:\bar L]$，则
$$
d^{-1}N_{M/\bar L}:
\operatorname{Cl}(M)[p]^{\chi_{\bar\pi}}
\xrightarrow{\sim}
\operatorname{Cl}(\bar L)[p]^{\chi_{\bar\pi}}.\tag{3.1}
$$
其逆为理想扩张。特别是从全 $p$ 除法域退到一条挠点直线的除法域，并不产生修正项；目标字符在被除去的 Galois 群上本来就是平凡的。

由于 $E$ 定义在 $\mathbb Q$ 上，复共轭 $c$ 保持 $M$，交换 $L$ 和 $\bar L$，并交换 $E[\pi]$ 与 $E[\bar\pi]$。对 $g\in\operatorname{Gal}(L/K)$，字符方向满足
$$
\chi_{\bar\pi}(cgc^{-1})=\chi_\pi(g).\tag{3.2}
$$
证明可在挠点上直接进行：若 $P\in E[\pi]$，则
$(cgc^{-1})(cP)=c(gP)=\chi_\pi(g)cP$。这里整数标量的模 $p$ 作用与 $c$ 交换，所以字符不取逆。

对理想类作复共轭也满足同样的半线性关系。故
$$
c_*:\operatorname{Cl}(\bar L)[p]^{\chi_{\bar\pi}}
\xrightarrow{\sim}\operatorname{Cl}(L)[p]^{\chi_\pi}.\tag{3.3}
$$
要点是“复共轭交换两个 CM 字符”，不是把目标字符随意改成其倒数。

## 4. 相对四次类群恰好包含整个目标块

先核实 $[L:K]=p-1$，从而 $B$ 确实存在。曲线在 $\pi$ 处有好约化；$[\pi]$ 的微分为 $\pi$，次数为 $p$。其模 $\pi$ 约化微分为零、次数为 $p$，故为纯不可分同源。因此在形式参数中
$$
[\pi](T)=\pi T+\cdots,
\qquad [\pi](T)\bmod\pi=uT^p+\text{更高次项},\quad u\ne0.
$$
$[\pi](T)/T$ 的 Weierstrass 多项式为次数 $p-1$ 的 Eisenstein 多项式。任一非零 $\pi$-挠点在 $K_\pi$ 上因此生成次数 $p-1$ 的全分歧扩张。另一方面，$\operatorname{Gal}(L/K)$ 通过其在一维 $E[\pi]$ 上的忠实作用嵌入 $\mathbb F_p^\times$。局部下界与全局上界合起来给出
$$
\operatorname{Gal}(L/K)\simeq\mathbb F_p^\times,
\qquad [L:K]=p-1.
$$
特别地，$J=\operatorname{Gal}(L/B)$ 对应唯一的四阶子群 $\mu_4$，且 $\chi_\pi|_J$ 非平凡。

在 $A=\operatorname{Cl}(L)[p^\infty]$ 上，$J$-不变投影为
$$
e_J=\frac14\sum_{g\in J}g
=\frac14\,j_{B\to L}N_{L/B}.
$$
第 2 节保证 $j_{B\to L}$ 在 $p$-初等部分单射，所以
$$
\ker N_{L/B}=\ker e_J=(1-e_J)A,
\qquad
A=e_JA\oplus(1-e_J)A.\tag{4.1}
$$
基域类群的扩张像正是 $e_JA$。因此相对群若定义为 $A/j\operatorname{Cl}(B)[p^\infty]$，则投影 $1-e_J$ 给出它到上述范数核的同构。

在 $\chi_\pi$ 特征分量上，
$$
\sum_{g\in J}\chi_\pi(g)=0,
$$
所以 $e_J$ 为零。即
$$
\operatorname{Cl}(L)[p]^{\chi_\pi}
=A_{L/B}[p]^{\chi_\pi}.\tag{4.2}
$$
从完整类群改成相对四次类群，在目标分量上仍然没有核或余核。

## 5. 复合映射及其逆

把第 3、4 节合起来，(1.1) 的映射就是
$$
\Phi(x)=c_*\left(d^{-1}N_{M/\bar L}x\right),
\qquad d=[M:\bar L].
$$
其逆为
$$
\Phi^{-1}(y)=j_{\bar L\to M}\bigl(c_*y\bigr),
$$
这里第二个 $c_*$ 是从 $L$ 回到 $\bar L$ 的共轭映射。两次复合为恒等式，分别由 $c_*^2=1$、$Nj=[d]$ 以及 $jN=\sum_{h\in H}h=[d]$ 在目标块上的作用得到。

这给出了实际的群同构，而非只有维数不等式。

## 6. 与 DMM 记号逐项核对及对 R7 的后果

De、Majumdar、Mondal 在 *Relative p-class groups and p-Selmer groups* 的 2024-12-17 预印本 Theorem 2.4 中，令 $L_{D,\mathfrak p}=K(E_D[\pi_D])$，取四次相对中间域 $F_{D,\mathfrak p}$，并定义
$$
r_\pi(E_D)=\dim_{\mathbb F_p}
\operatorname{Cl}(L_{D,\mathfrak p}/F_{D,\mathfrak p})[p]^{\chi_D}.
$$
其 $\chi_D$ 是在 $E_D[\pi_D]$ 上的作用字符。$\pi_D$ 是 $\pi$ 的一个单位倍数，所以对 $D=17$ 有 $E_D[\pi_D]=E[\pi]$，除法域与特征均与本文相同。该定理证明的第一段也明确把完整类群目标块与相对类群目标块等同。

本文 (1.1)–(1.2) 额外把 R7 使用的全 $p$ 除法域、共轭字符块，与该单 $\pi$ 相对类群块接起来；这一步只用理想范数恒等式，不借用 Rubin 的 Selmer 维数不等式。

因此 R7 已证明的所有结论可原样改写为
$$
r_\pi(E)=c_p\ge1,
\qquad
\dim_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q)
=2\left\lceil\frac{r_\pi(E)}2\right\rceil,
$$
以及
$$
\Sha(E/\mathbb Q)[p^\infty]=0
\quad\Longleftrightarrow\quad
r_\pi(E)\in\{1,2\}.
$$
本文解决了两种类群实现之间的比较子问题；**没有证明 $r_\pi(E)\le2$ 对无穷多个 $p$ 成立**。固定 $p$ 的反射公式或单位指数公式仍需额外的变化素数控制，才能完成主课题。

## 来源

- D. De, D. Majumdar and S. Mondal, *Relative p-class groups and p-Selmer groups*, [arXiv:2412.13022v1](https://arxiv.org/abs/2412.13022v1)，2024-12-17，Theorem 2.4 及其证明首段；正式版为 *Journal of Pure and Applied Algebra* **230** (2026), article 108222，[DOI](https://doi.org/10.1016/j.jpaa.2026.108222)。本文按明示的预印本版本给出定理编号。
- 本地 R7 的 Kummer、局部条件和 $p$-奇偶论证，以及 R4 的精确秩与挠群证书。
