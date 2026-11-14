# R31. Padé 分母在固定 torsion 点处是一个固定代数数的 Frobenius 商

**状态：已证明。** 日期：2026-11-12。会话：Astra-rank2-Sha / cm_iwasawa_routes；辅助理想规范由 explicit_curve 同步核对。

本结果找到一个固定的算术对象：R29 及 Padé 桥中的分母在固定 $\alpha$ 处的值，准确等于某个固定代数数的 Frobenius–Fermat 商的一个固定次主单位根。这不只是一阶同余，而是全部 $p$-进层的等式。它目前只控制固定 torsion 点处的值，尚未证明原 $\Phi$ 的全部目标矩可由这个值代替。

## 1. 记号与结论

沿用 R18、R29：
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
\mathfrak f=(34(1+i)),\quad P_f=(u,v),
$$
$$
F=K(E[\mathfrak f]),\quad
\alpha=v/u,\quad
M=K(\alpha)=F^{\langle\tau\rangle},\quad
\tau P_f=T-P_f,\quad T=(0,0).
$$
四次模型为
$$
X=y/x,\quad Z=x+17/x,\qquad Z^2=X^4+68.
$$
令 $Q_+,Q_-$ 为两个 $X=0$ 点；它们满足
$$
Q_++T=Q_-,\qquad [2]Q_\pm=O,
$$
且不同于 $O,T$。

对每个 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$，选择 $\mathfrak p\mid p$，令 $\pi=\psi_E(\mathfrak p)$，并将商上的 CM 同源规范化为
$$
X\circ[\pi]=\frac{N_p(X)}{D_p(X)},\quad
D_p(0)=1,\quad
\deg N_p=p,\quad\deg D_p=p-1,
$$
$$
N_p\equiv X^p\pmod p,\qquad D_p\equiv1\pmod p.
\tag{1}
$$
这些规范与 Padé 桥相同。令 $\sigma_{\mathfrak p}$ 为 $F/K$ 或 $M/K$ 中的算术 Frobenius。

选择固定辅助理想
$$
\mathfrak a=(67),\qquad \mathrm N\mathfrak a=4489,
\qquad \psi_E(\mathfrak a)=-67\equiv1\pmod{\mathfrak f}.
\tag{2}
$$
这里 $67\equiv3\pmod4$ 是惰性素数，$\mathfrak a$ 与 $6\mathfrak f$ 互素。其 Hecke 生成元为 $-67$，也可由惰性好素数处 $a_{67}=0$、平方 Frobenius 为 $[-67]$ 直接确定。

以下使用 §2 明确规范化的 Rubin 函数 $\Theta_{\mathfrak a}$。定义
$$
F_{\mathfrak b}(P)=
\Theta_{\mathfrak b}(P)\Theta_{\mathfrak b}(P+T),
$$
以及一个不依赖 $p$ 的数
$$
\boxed{\quad
w=\frac{F_{\mathfrak a}(P_f)}
{F_{\mathfrak a}(Q_+)}\in M^\times.
\quad}
\tag{3}
$$

**主结论。** 对全部上述素数及选择的素位，
$$
\boxed{\quad
D_p(\alpha)^{53856}
=\frac{\sigma_{\mathfrak p}(w)}{w^p},
\qquad
53856=12(4489-1)=2^5\cdot3^2\cdot11\cdot17.
\quad}
\tag{4}
$$
所有定义的值都有限非零；$w$ 在每个目标 $p$ 上方的素位都是单位，且
$$
D_p(\alpha)\in1+p\mathcal O_{M,\mathfrak p}.
\tag{5}
$$
式 (4) 的指数在整个目标素数集合中均为单位，不增加任何需要排除的素数。

这里 $\mathcal O_{M,\mathfrak p}$ 表示 $M$ 在所有 $\mathfrak p$ 上方素位的局部整数环之积。每个因子均不分歧；也可逐个上方素位阅读所有公式。

## 2. Theta 的规范与所需除子

设 $\mathfrak b=(\beta)$ 为与 $6$ 互素的 CM 理想，令
$\Delta=\Delta(E)=64\cdot17^3$。Rubin Definition 7.1 的规范是
$$
\Theta_{\mathfrak b}(P)
=\beta^{-12}\Delta^{\mathrm N\mathfrak b-1}
\prod_{0\ne R\in E[\mathfrak b]}
\bigl(x(P)-x(R)\bigr)^{-6}.
\tag{6}
$$
改变生成元所乘的四次单位根不改变 $\beta^{-12}$。函数定义在 $K$ 上，且由 $x(-P)=x(P)$ 可知它是偶函数。

若把非零核点按 $R,-R$ 配对，定义
$$
\psi_{\mathfrak b}(P)
=\beta\prod_{\{R,-R\}\subset E[\mathfrak b]\setminus\{O\}}
\bigl(x(P)-x(R)\bigr),
$$
则
$$
\Theta_{\mathfrak b}
=\Delta^{\mathrm N\mathfrak b-1}/\psi_{\mathfrak b}^{12}.
$$
这说明整数 division polynomial 公式如何准确推广到 $\mathfrak b=(\pi)$；没有省略 $\pi^{-12}$ 的首项常数。

由 (6) 直接计算除子：
$$
\operatorname{div}\Theta_{\mathfrak b}
=12\mathrm N\mathfrak b[O]
-12\sum_{R\in E[\mathfrak b]}[R].
\tag{7}
$$
在复不变参数 $z$（$\omega=dz$）下，$x=z^{-2}+O(z^2)$，所以在 $O$ 附近
$$
\Theta_{\mathfrak b}(P(z))
=\beta^{-12}\Delta^{\mathrm N\mathfrak b-1}
z^{12(\mathrm N\mathfrak b-1)}(1+O(z)).
\tag{8}
$$
这些除子和首项将同时固定以下两个恒等式的常数。

## 3. 分母的十二次幂及 X=0 常数

因为 $[\pi]$ 固定 $O,T$，且在特征零中无分歧，(1) 的分母在 $E$ 上的除子为
$$
\operatorname{div}D_p(X(P))
=[\pi]^*([O]+[T])-p([O]+[T]).
\tag{9}
$$
具体地，它的零点是非零 $\pi$-核及它们的 $T$ 平移；在 $O,T$ 各有一个 $p-1$ 阶极点。所有这些零点均为单点：它们不是 $P\mapsto T-P$ 的不动点，否则 $2P=T$ 与其在 $\pi$-核或核的 $T$ 平移中相矛盾。

另一方面，(7) 给
$$
\operatorname{div}F_{(\pi)}
=12p([O]+[T])-12[\pi]^*([O]+[T])
=-12\,\operatorname{div}D_p(X).
$$
所以 $D_p(X)^{12}F_{(\pi)}$ 是常数。在 $P=Q_+$ 处，$X=0$、$D_p(0)=1$，得到准确等式
$$
\boxed{\quad
D_p(X(P))^{12}
=\frac{\Theta_{(\pi)}(Q_+)\Theta_{(\pi)}(Q_-)}
{\Theta_{(\pi)}(P)\Theta_{(\pi)}(P+T)}.
\quad}
\tag{10}
$$
这里没有未定根单位常数。

所用点的值均有限非零。对于 $\mathfrak b=(\pi)$ 或 $\mathfrak a=(67)$，这些辅助理想都与 $\mathfrak f$ 及 $(2)$ 互素。$P_f,P_f+T,Q_\pm$ 均为非零 $\mathfrak f$-torsion 点，故不属于相应非零辅助核；它们也不等于 $O$。式 (7) 的零极点列表因此避开了全部这些点。

## 4. 辅助理想交换式及其常数的独立核对

Rubin Lemma 7.10 给出准确的辅助交换式
$$
\boxed{\quad
\frac{\Theta_{\mathfrak a}([\pi]P)}
{\Theta_{\mathfrak a}(P)^p}
=
\frac{\Theta_{(\pi)}([-67]P)}
{\Theta_{(\pi)}(P)^{4489}}.
\quad}
\tag{11}
$$
为使本文所用规范完全可核查，也可直接证明它。

更一般地，对 $\mathfrak a=(a)$、$\mathfrak b=(b)$，比较
$$
\Theta_{\mathfrak a}([b]P)/\Theta_{\mathfrak a}(P)^{\mathrm N\mathfrak b}
$$
与交换 $\mathfrak a,\mathfrak b$ 后的表达式。用 (7) 及
$[b]^{-1}E[\mathfrak a]=E[\mathfrak a\mathfrak b]$，可见两者除子相同。再由 (8)，第一项在 $O$ 的首系数为
$$
a^{12(\mathrm N\mathfrak b-1)}
b^{12(\mathrm N\mathfrak a-1)}
\Delta^{-(\mathrm N\mathfrak a-1)(\mathrm N\mathfrak b-1)}.
$$
交换两理想后完全相同。因此比值常数为一，得到 (11)。这一证明也显示没有依赖一个未说明的 division-function 首项。

因为 $-67-1=-68$ 被 $34(1+i)$ 整除，$[-67]$ 固定 $E[\mathfrak f]$ 的每一点。CM reciprocity 使 $[\pi]$ 在这些点上作用为 $\sigma_{\mathfrak p}$。所以 (11) 在任意上述非零 $\mathfrak f$-torsion 点 $P$ 处变成
$$
\Theta_{(\pi)}(P)^{1-4489}
=
\frac{\sigma_{\mathfrak p}(\Theta_{\mathfrak a}(P))}
{\Theta_{\mathfrak a}(P)^p}.
\tag{12}
$$
这同样适用于 $Q_\pm$；其较小的导子没有使交换式失效。

## 5. w 确实属于固定域 M，且主等式方向正确

所有值首先属于固定域 $F$。$\Theta_{\mathfrak a}$ 是偶函数，而 $T=-T$，因此
$$
F_{\mathfrak a}(T-P)
=\Theta_{\mathfrak a}(T-P)\Theta_{\mathfrak a}(-P)
=F_{\mathfrak a}(P).
$$
于是 $F_{\mathfrak a}(P_f)$ 被 $\tau$ 固定。另一方面，$Q_+,Q_-$ 被 $\operatorname{Gal}(F/K)$ 置换，且 $Q_++T=Q_-$，所以
$$
F_{\mathfrak a}(Q_+)
=\Theta_{\mathfrak a}(Q_+)\Theta_{\mathfrak a}(Q_-)\in K^\times.
$$
这证明 (3) 的 $w\in F^{\langle\tau\rangle}=M$。

将 (12) 分别用于 $P_f,P_f+T$ 后相乘，再除以用于 $Q_+,Q_-$ 后的乘积，得到
$$
\frac{\sigma_{\mathfrak p}(w)}{w^p}
=
\left(
\frac{F_{(\pi)}(P_f)}{F_{(\pi)}(Q_+)}
\right)^{1-4489}.
$$
由 (10)，括号中的量为 $D_p(\alpha)^{-12}$。因此
$$
\frac{\sigma_{\mathfrak p}(w)}{w^p}
=D_p(\alpha)^{12(4489-1)},
$$
正是 (4)。指数的符号也由这一步确定。

## 6. 所有目标素位的单位性，无须增加例外

由 R18，$\alpha$ 在每个目标素位为单位。式 (1) 的分母系数整且 $D_p\equiv1\bmod p$，故 (5) 成立。

现对 (4) 在任意上方素位 $\mathfrak P$ 取赋值：
$$
v_{\mathfrak P}(\sigma_{\mathfrak p}w)
=p\,v_{\mathfrak P}(w).
\tag{13}
$$
左边就是 $v_{\sigma_{\mathfrak p}^{-1}\mathfrak P}(w)$。沿这个有限素位轨道反复使用 (13)，最终得到
$$
v_{\mathfrak P}(w)=p^d v_{\mathfrak P}(w)
$$
其中 $d\ge1$，所以 $v_{\mathfrak P}(w)=0$。这证明 $w$ 在所有目标素位都是单位，没有预先假设其局部整性，也没有因辅助点的低导子引入新例外。

此外
$$
53856=2^5\cdot3^2\cdot11\cdot17.
$$
目标 $p$ 至少为 $13$，不等于 $17$；$11$ 又不是分裂素数。因此这个指数在整个目标集合中为单位。辅助理想的素数 $67$ 也是惰性的，不在目标集合中。

若需要全局单位支持的描述，Rubin Theorem 7.4 的单位性结论可用于 $P_f$ 的复合导子与 $Q_\pm$ 的 $2$-幂导子，给出固定的 $S$-unit 描述。本文的目标处单位性完全由 (4)、(5)、有限轨道证明，不依赖扩大或最小化这个 $S$ 的选择。

## 7. 固定底数的准确 Frobenius–Fermat quotient

设 $C=53856$。因为 $M/K$ 在目标素位不分歧且 $w$ 是单位，
$$
q_{\mathfrak p}(w)
=\frac{w^p/\sigma_{\mathfrak p}(w)-1}{p}
\in\mathcal O_{M,\mathfrak p}.
\tag{14}
$$
式 (4) 可改写为
$$
D_p(\alpha)^C=(1+p q_{\mathfrak p}(w))^{-1}.
$$
在主单位群中，取 $C$ 次幂是同构；由 (5) 唯一确定根，得到
$$
\boxed{\quad
D_p(\alpha)
=(1+p q_{\mathfrak p}(w))^{-1/C}.
\quad}
\tag{15}
$$
例如模 $p^4$ 有完整有限式
$$
\begin{aligned}
D_p(\alpha)\equiv{}&
1-\frac{p}{C}q_{\mathfrak p}(w)
+\frac{C+1}{2C^2}p^2q_{\mathfrak p}(w)^2\\
&-\frac{(C+1)(2C+1)}{6C^3}
p^3q_{\mathfrak p}(w)^3
\pmod{\mathfrak p^4}.
\end{aligned}
\tag{16}
$$
所有显示分母在目标素位都为单位。还有精确对数等式
$$
C\log_p D_p(\alpha)
=\log_p\sigma_{\mathfrak p}(w)-p\log_p w.
\tag{17}
$$
在固定域 $M$ 完全分裂的素数上，$\sigma_{\mathfrak p}=1$，于是
$q_{\mathfrak p}(w)=(w^{p-1}-1)/p$，成为通常的固定代数底数 Fermat quotient。没有把随 $p$ 改变的 $\pi$ 本身当成固定底数。

## 8. 与 Padé 三项式及目标矩的关系

Padé 桥已给出
$$
D_p(X)=1+\sum_{j=1}^r d_jX^{4j},\qquad
d\equiv-\frac p\ell b+\frac{p^2}{\ell^2}Ab
-\frac{p^3}{\ell^3}A^2b\pmod{p^4},
$$
其中 $A,b,\ell$ 都来自固定 $\mathscr L$ 的明确系数。将 $X=\alpha$ 代入后，整个有限 Toeplitz 组合现在等于 (16) 的固定数 $w$ 的 Frobenius 商。例如最低层为
$$
\frac1\ell\sum_{j=1}^r b_j\alpha^{4j}
\equiv\frac{q_{\mathfrak p}(w)}{C}\pmod{\mathfrak p}.
\tag{18}
$$
这里的 $b_j$ 是 Padé 向量的分量，不能与 R17 的四个系数 $b_j(p)$ 混同。

这确实消去了“在 $\alpha$ 处仍需一个随 $p$ 改变的未知单位”的问题。然而 (4)–(18) 只控制分母的特定求值及其 Galois 共轭；它们没有自动确定 $D_p$ 的全部系数，也没有自动给出其高阶导数。原 $\Phi$ 的 $\lambda_p,\lambda_{2p-1}$ 及 R24–R26 的 $g_0,g_1$ 仍涉及规定次数的系数或相应组合。若要仅以固定 $w$ 的 Fermat quotient 判定这些量，还必须证明这一额外比较，不能由一个点处的值径直推出。

本文也没有证明 $q_{\mathfrak p}(w)$ 对无穷多个 $p$ 具有指定的小赋值。即使获得这个独立的非 Wieferich 输入，仍须核对它确实控制目标组合中的相消。主问题的固定曲线与无穷素数两个量词均未改变。

## 来源与依赖

- K. Rubin, *Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，1999，
  [作者讲义](https://swc-math.github.io/notes/files/99RubinCM.pdf)：Definition 7.1、Lemma 7.5、Theorem 7.4、Lemma 7.10。本文已独立写出实际使用的除子、首项和辅助交换式的常数证明。
- R18：$F,M,\tau,\alpha$ 以及固定素位的 Frobenius 作用。
- R29 与 Padé 原点桥笔记：$D_p$ 的规范、整性、次数及三项展开。
- 所有新比较恒等式、固定域归属和目标处单位性均已在本文给出完整证明。
