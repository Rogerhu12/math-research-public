# R13：固定 CM 同余曲线的导子、分母与高度下界

日期：2026-11-12；会话：`serre-uniformity-astra/2026-11-12`。

**状态：已证明。** 这是 [R2 的精确 Tate 局部条件](R2-exact-tate-local-criterion.md) 和 [R11 的固定 CM 整 j 同余刚性](R11-integral-j-fixed-cm-congruence.md) 的推论，结合标准复乘理论与 Frobenius 计算；不声称新颖性。它为实际满足全局同余的曲线给出必要条件，没有证明这种非 CM 曲线存在，也没有证明它们不存在。

## 1. 陈述

以下结论以实际的全局挠点同构为假设。固定
$$A:y^2=x^3-x,\qquad K=\mathbb Q(i),\qquad p>37,\quad p\equiv3\pmod4.$$
若 $E[p]\simeq A[p]$，则 $A$ 在 $p$ 好且超奇异，从而二者模 $p$ 像都是完整 $N_{\rm ns}(p)$。由自同态 $(x,y)\mapsto(-x,iy)$ 可知二次商为 $\chi_{-4}$，见 R7 §6。

记
$$T=\{q:v_q(j(E))<0\}.$$

**命题 R13。** 在上述条件下：

1. 存在互素整数 $a,b$，$b\ge1$，使 $j(E)=a/b^p$，且 $T$ 正是 $b$ 的素因子集；
2. $E$ 在 $p$ 好约化，在 $2$ 处的导子指数为 $5$，并且
   $$N_E=32\prod_{q\in T}q;\tag{13.1}$$
3. 对每个 $q\in T$，有
   $$q\equiv\chi_{-4}(q)\pmod p,\qquad q\equiv\pm1\pmod{4p};\tag{13.2}$$
   其中两个同余式中的符号一致；
4. 若 $q\in T$ 在 $K$ 分裂，则
   $$q\ge4p^2+1.\tag{13.3}$$

特别地，若 $E$ 非 CM，则由 R11 有 $T\ne\varnothing$，因而
$$h(j(E))\ge p\log(4p-1).\tag{13.4}$$
若 $T$ 含一个在 $K$ 分裂的素数，则更有
$$h(j(E))\ge p\log(4p^2+1).\tag{13.5}$$

## 2. 完整非分裂 Cartan 像及其二次商

为把陈述中的二次商说清，记 $\iota(x,y)=(-x,iy)$ 为 $A$ 的 CM 自同态。它在 $A[p]$ 上诱导矩阵 $J$，满足 $J^2=-I$。因为 $p\equiv3\pmod4$，$X^2+1$ 在 $\mathbb F_p$ 上不可约，所以 $\mathbb F_p[J]\simeq\mathbb F_{p^2}$，而 $J$ 的中心化子就是相应的非分裂 Cartan $C$。

对 $g\in G_{\mathbb Q}$，有
$$\rho_{A,p}(g)J\rho_{A,p}(g)^{-1}=\chi_{-4}(g)J.$$
因此表示像落在 $N(C)$ 中，且 $\rho_{A,p}(g)\in C$ 当且仅当 $\chi_{-4}(g)=1$；这就识别了二次商。

还需确认像不是 $N(C)$ 的真子群。$A$ 的判别式为 $64$，故在 $p$ 好约化。对 $\mathbb F_p$ 上的二次特征，把 $x$ 与 $-x$ 配对；因 $(-x)^3-(-x)=-(x^3-x)$ 且 $-1$ 为非平方，得到 $a_p(A)=0$，故 $A$ 在 $p>3$ 超奇异。好超奇异椭圆曲线在不分歧基域 $\mathbb Q_p$ 上的模 $p$ 惯性像为完整非分裂 Cartan，这是 Serre 1972, §1.11, Proposition 12 的标准结论；所用形式及来源见 [R7 §6、§9](R7-simultaneous-local-frobenius-approximation.md)。它与全局的 $C$ 相同：局部完整 Cartan 是 $N(C)$ 内的循环子群，阶为 $p^2-1$，而外陪集元素的阶至多 $2(p-1)<p^2-1$，所以该循环子群必包含于 $C$，进而相等。

复共轭满足 $\chi_{-4}(c)=-1$，因此像还含外陪集元素，故完整全局像正是 $N(C)$。全局同构 $E[p]\simeq A[p]$ 把这些结论一并传给 $E[p]$。

## 3. 导子、分母及高度界的完整证明

**证明。** R2 对每个 $q\in T$ 给出 $q\ne p$、$p\mid-v_q(j(E))$ 及 $q\equiv\pm1\pmod p$。因此分母是 $p$ 次幂，证明第 1 项。特别地 $2\notin T$，因为 $p>37$。

在 $p$ 处，R2 排除负 $j$ 赋值，所以 $E$ 潜在好约化。$A$ 在 $p$ 好约化且二者 $p$ 挠点同构，R11 引理 11.2 推出 $E$ 在 $p$ 好约化。在 $2$ 处，二者潜在好约化，R11 引理 11.3 使导子指数相等，均为 $5$。

对 $q\ne2,p$ 且 $q\notin T$，$E$ 潜在好约化，而 $A$ 好约化；同样由引理 11.3 得 $E$ 好约化。若 $q\in T$，$E$ 潜在乘性，而 $E[p]\simeq A[p]$ 在 $q$ 不分歧。Tate 二次扭曲特征不能在惯性上取 $-1$，否则模 $p$ 惯性矩阵的迹为 $-2$ 而非 $2$。所以该扭曲不分歧，$E$ 已为乘性约化，导子指数为 $1$。这证明 (13.1)。

在这样的 $q\in T$，R2 还给出 Tate 参数为 $\mathbb Q_q$ 中的 $p$ 次幂，因此模 $p$ Frobenius 共轭于
$$s_q\begin{pmatrix}q&0\\0&1\end{pmatrix},\qquad s_q\in\{\pm1\}.$$
若 $q\equiv1\pmod p$，这是标量矩阵，Cartan 商为 $+1$；若 $q\equiv-1\pmod p$，它有不同的 $\mathbb F_p$ 特征值，不能在非分裂 Cartan 中，商为 $-1$。该商等于 $\chi_{-4}(q)$，所以得到 (13.2) 的第一个同余。又 $\chi_{-4}(q)=+1$ 恰当 $q\equiv1\pmod4$，为 $-1$ 恰当 $q\equiv-1\pmod4$；中国剩余定理即给出第二个同余。

现设 $q\in T$ 在 $K$ 分裂，所以 $q\equiv1\pmod4$ 且 $q\equiv1\pmod p$。$A/\mathbb F_q$ 的 Frobenius 为某个
$$\alpha=u+vi\in\mathbb Z[i],\qquad u^2+v^2=q,\qquad a_q(A)=2u.$$
为说明这里没有隐含选择：自同态 $i$ 在 $\mathbb F_q$ 上定义，所以 Frobenius 与它交换；在椭圆曲线自同态代数中，非实二次子域的中心化子就是该子域。因此 Frobenius 属于 $\mathbb Q(i)$，又是代数整数，故属于最大整环 $\mathbb Z[i]$。其范数和迹分别为次数 $q$ 和 $a_q(A)$。

比较全局同余和 Tate Frobenius，得到 $2u\equiv\pm2\pmod p$，即 $u\equiv\pm1\pmod p$。结合 $u^2+v^2=q\equiv1\pmod p$，得到 $p\mid v$。曲线 $A$ 在每个奇素数处都有全有理 $2$ 挠点，所以
$$q+1-2u\equiv0\pmod4.$$
由于 $q\equiv1\pmod4$，$u$ 为奇数，进而 $v$ 为偶数。$q$ 为素数，故 $v\ne0$；于是 $|v|\ge2p$、$|u|\ge1$，从而 $q=u^2+v^2\ge4p^2+1$，证明 (13.3)。

若 $E$ 非 CM，R11 强迫 $b>1$。每个 $q\mid b$ 都满足 $q\equiv\pm1\pmod{4p}$，因此 $q\ge4p-1$。约分形式下的有理数高度为
$$h(j(E))=\log\max\{|a|,b^p\}\ge p\log b,$$
即得 (13.4)；若某个 $q\mid b$ 分裂，则用 (13.3) 得 (13.5)。证毕。

## 4. 范围与未解决步骤

这些都是必要条件和高度下界。没有得到一个对真实同余曲线统一、且增长更慢的高度上界，所以它们不构成矛盾。

固定参考曲线的最终整性问题、Anni–Siksek 定理中固定加性素数支集的作用，以及 Ribet 升层只给出新形式而不保证其系数域为 $\mathbb Q$，见 [CM 同余全局路线笔记](../notes/2026-11-12-cm-congruence-global-route.md)。这些边界不属于 R13 的结论。
