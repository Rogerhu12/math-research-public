# R5：有限阶预解式的单参数判据及阶数边界上的显式例子

**状态：已证明的条件性中间结论；不解决完整 ISP，不声称文献新颖性。**

日期：2026-11-12。会话：Astra-ISP-b382c564。

研究动机：Tcaciuc 的已知双参数判据把拟幂零算子的 ISP 化为“同一个秩一方向上有两个非零参数仍拟幂零”。本条在标量预解式有有限增长阶且低阶矩消失时，把两个参数降为一个；同时给出紧加权移位例子，说明不能省去增长阶的严格不等式。这只是判据，**没有为任意算子构造满足判据的扰动**。

以下内积对第一变量线性，$u\otimes v$ 表示 $x\mapsto\langle x,v\rangle u$。

## 1. 秩一扰动的全部非零谱由一个整函数决定

设 $T\in B(H)$ 拟幂零，$u,v\ne0$，$F=u\otimes v$。定义

$$h(z)=z\langle(I-zT)^{-1}u,v\rangle
=\sum_{n=0}^{\infty}\langle T^nu,v\rangle z^{n+1}.$$

因为 $r(T)=0$，右边的算子 Neumann 级数在每个有界 $z$ 集合上按范数一致收敛；因此 $h$ 是整函数且 $h(0)=0$。

对 $\lambda\ne0$ 记 $R=(\lambda I-T)^{-1}$，则

$$\lambda\in\sigma(T+\alpha F)
\quad\Longleftrightarrow\quad
1-\alpha h(1/\lambda)=0.\tag{1}$$

而右边成立时，$Ru$ 是相应的非零特征向量。

**证明。** 若 $c=1-\alpha\langle Ru,v\rangle\ne0$，直接相乘可验证逆为

$$
(\lambda I-T-\alpha F)^{-1}
=R+\frac{\alpha}{c}\,\bigl[x\mapsto\langle Rx,v\rangle Ru\bigr].
$$

若 $c=0$，则 $\alpha\ne0$，并由 $TRu=\lambda Ru-u$ 得

$$(T+\alpha F)Ru=\lambda Ru-u+\alpha\langle Ru,v\rangle u=\lambda Ru.$$

这同时证明 (1) 的两边，无需额外使用本质谱或 Fredholm 理论。证毕。

因此，对 $\alpha\ne0$，$T+\alpha F$ 拟幂零当且仅当整函数 $1-\alpha h$ 无零点。注意 $z=0$ 处的值为 $1$，不会在从 $z$ 到 $\lambda=1/z$ 的变换中漏掉零点。

若 $h\equiv0$，则

$$M=\overline{\operatorname{span}}\{T^nu:n\ge0\}\subset v^\perp$$

是非零真闭 $T$-不变子空间，且所有 $T+\alpha F$ 都拟幂零。

## 2. 单个非零参数的有限阶判据

**命题。** 设 $m\ge1$ 是整数。除以上假设外，再设：

1. $\langle T^nu,v\rangle=0$ 对 $0\le n\le m-2$ 成立（$m=1$ 时不要求任何低阶矩）；
2. 存在 $C>0$、$0\le\rho<m$，使

   $$|h(z)|\le C\exp(C|z|^\rho)\qquad(z\in\mathbb C);\tag{2}$$

3. 存在一个 $\alpha\ne0$，使 $T+\alpha F$ 拟幂零。

则 $h\equiv0$，所以 $T$ 有上面显式给出的非平凡闭不变子空间，而且 $T+\beta F$ 对所有 $\beta\in\mathbb C$ 都拟幂零。

**证明。** 由条件 1，$h(z)=O(z^m)$ 于 $z=0$。条件 3 及 (1) 说明 $q=1-\alpha h$ 是无零点整函数，$q(0)=1$。函数 $q'/q$ 是整函数，在单连通的复平面上取以零为起点的原函数 $g$，则

$$g(0)=0,\qquad q=e^g.$$

由 (2)，对某个只依赖 $C,\alpha$ 的 $C_1>0$，

$$\operatorname{Re}g(z)=\log|q(z)|\le C_1(1+|z|^\rho).\tag{3}$$

现完整证明 (3) 蕴含 $g$ 是次数小于 $m$ 的多项式。给定 $R\ge1$，令 $A=C_1(1+(2R)^\rho)>0$。在 $|z|<2R$ 上，$\operatorname{Re}g\le A$，因此

$$\psi(z)=\frac{g(z)}{2A-g(z)}$$

解析、$\psi(0)=0$ 且 $|\psi(z)|\le1$；最后一项来自

$$|2A-g|^2-|g|^2=4A(A-\operatorname{Re}g)\ge0.$$

对半径 $2R$ 的圆盘应用 Schwarz 引理，在 $|z|\le R$ 有 $|\psi(z)|\le1/2$，故

$$|g(z)|=\left|\frac{2A\psi(z)}{1+\psi(z)}\right|\le2A.$$

Cauchy 导数估计给出，对每个整数 $k\ge m>\rho$，

$$|g^{(k)}(0)|\le\frac{k!\,2C_1(1+(2R)^\rho)}{R^k}\xrightarrow[R\to\infty]{}0.$$

于是 $g$ 是次数至多 $m-1$ 的多项式。但 $q(z)=1+O(z^m)$，其归一化对数满足 $g(z)=O(z^m)$；这些条件只能使 $g\equiv0$。因此 $q\equiv1$，进而 $h\equiv0$。证毕。

特别地，$m=2$ 时，矩条件只是 $\langle u,v\rangle=0$，即 $F^2=0$。若对应标量预解式的增长阶严格小于 $2$，则一个非零的拟幂零秩一扰动已足以迫使全部矩消失。

可用的算子层面充分条件是

$$\sum_{n\ge0}\|T^n\|r^{n+1}\le C\exp(Cr^\rho),\qquad \rho<m;$$

它蕴含任意固定 $u,v$ 的 (2)，但本条不要求也不证明一般拟幂零算子有这种增长界。

## 3. 阶数恰为 $m$ 时的显式例子

对每个整数 $m\ge1$，在 $H=\ell^2(\{1,2,\ldots\})$ 上定义

$$T_me_n=\frac{2}{n^{1/m}}e_{n+1},\qquad u=e_1.$$

令 $v=v^{(m)}$ 的非零坐标为

$$v_{mk}=-\frac{((mk-1)!)^{1/m}}{2^{mk-1}k!}\quad(k\ge1),\qquad
v_j=0\quad(m\nmid j),\qquad F_m=u\otimes v.$$

有以下精确结论：

- $T_m$ 非零、紧且范数拟幂零；$F_m$ 为非零秩一算子。
- 对 $m\ge2$，$F_m^2=0$；所有 $0\le n\le m-2$ 的矩均为零。
- 标量函数为

  $$h_m(z)=1-e^{z^m},$$

  其增长阶恰为 $m$。
- $T_m+\alpha F_m$ 拟幂零当且仅当 $\alpha\in\{0,1\}$。当 $\alpha\notin\{0,1\}$ 时，它有无穷多个非零特征值。

**逐项证明。**

权趋零，故有限秩截断按算子范数趋于 $T_m$，它紧。因为正权 $2/n^{1/m}$ 随 $n$ 递减，

$$\|T_m^n\|=\frac{2^n}{(n!)^{1/m}},$$

所以其 $n$ 次根趋零，得到范数拟幂零性；例如 $n!\ge(n/2)^{n/2}$ 已足以验证此极限。

多项式 $(x_1+\cdots+x_m)^{mk}$ 中等多重指标项的系数不超过所有系数之和，因此

$$\frac{(mk)!}{(k!)^m}\le m^{mk}.$$

于是

$$|v_{mk}|\le2\left(\frac{m}{2^m}\right)^k.$$

由于 $m/2^m<1$ 对所有 $m\ge1$ 成立，$v\in\ell^2$，且显然 $v\ne0$。当 $m\ge2$ 时，$v_1=0$，故 $F_m^2=0$。

再由

$$T_m^ne_1=\frac{2^n}{(n!)^{1/m}}e_{n+1}$$

直接算得

$$\langle T_m^ne_1,v\rangle=
\begin{cases}-1/k!,&n=mk-1,\ k\ge1,\\0,&\text{其余 }n\ge0.
\end{cases}$$

因此 $h_m(z)=-\sum_{k\ge1}z^{mk}/k!=1-e^{z^m}$，增长阶恰为 $m$。这里低阶矩确实全部消失，但 $h_m$ 并不恒零。

由 (1)，$\alpha=1$ 时判别整函数等于 $e^{z^m}$，没有零点，所以 $T_m+F_m$ 拟幂零。$\alpha=0$ 时是 $T_m$。若 $\alpha\notin\{0,1\}$，非零谱条件等价于

$$e^{z^m}=1-\frac1\alpha\ne0.$$

选任意一个右边的复对数 $w$，每个方程 $z^m=w+2\pi i k$ 都给出根；随 $k\in\mathbb Z$ 变化有无穷多个不同的根。$z=0$ 不是根，因为右边不等于 $1$。于是由 (1) 得到无穷多个非零特征值 $\lambda=1/z$。证毕。

此族说明，§2 中 $\rho<m$ 不能在相同低阶矩假设下放宽为允许阶数 $m$。特别是“$F^2=0$、$T$ 和 $T+F$ 都拟幂零”并不能单独推出 $\langle T^nu,v\rangle=0$ 对全部 $n$ 成立。

例子中的 $T_m$ 与其秩一扰动都是紧算子，因此它们本来就有不变子空间。此处反驳的是**单参数迫使全部矩消失**这一更强断言，不是反驳 ISP。

## 4. 与已有结果及主目标的关系

Adi Tcaciuc, *On quasinilpotent operators and the invariant subspace problem*, J. Math. Anal. Appl. **477** (2019), 187–195，Lemma 2.1、Theorem 2.3、Proposition 2.4 及其后例子；[arXiv:1805.03277v2](https://arxiv.org/html/1805.03277v2)，[DOI](https://doi.org/10.1016/j.jmaa.2019.04.026)。该文给出：$T$ 拟幂零时，存在非平凡不变子空间当且仅当存在非零秩一 $F$ 和 $\alpha\notin\{0,1\}$，使 $T+F,T+\alpha F$ 均拟幂零。其后加权移位例子的标量函数为 $e^{1/\lambda}-1$；§3 是同类指数机制的高阶显式版本，不据此主张创新优先权。

**尚缺：** 即使知道 $h$ 增长阶小，也没有证明能找到非零 $u,v$，同时满足低阶矩条件及某个非零参数下的拟幂零性。单靠小范数或低阶矩消失不能保证后者。一般有界算子也尚未被无损地归约到本条的有限阶拟幂零情形；不得将本条当作完整答案。
