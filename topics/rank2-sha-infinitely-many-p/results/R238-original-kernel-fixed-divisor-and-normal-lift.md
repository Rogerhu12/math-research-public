# R238 — 原低次核的共同重因子与同一前缀的首次提升

日期：2026-11-13。**状态：已证明。** 在 R236 的低次数范围，整个原核空间具有同一个依赖 $C$ 的重因子，而不是仅仅每个向量各有一个可能不同的重因子。该因子由对原图的高接触唯一确定；全部有关 Hasse 接触阶可准确计算，核条件压缩成两条整数不等式。由此得到全部深层方向的共同因子限制，并把第一次提升准确写在约去这个共同因子后的有限源上。没有构造所需的原深关系，没有证明任何跨素数非零。

本篇的固定因子由同一个原核空间确定；不更换原 theta 轴、原次数或原前缀。它不允许把模 $p$ 的共同因子当成整关系可直接约去的因子。

## 1. 原核与实际 Hasse 条件

取 $p=4r-1\ge19$，$\mathcal O=\mathbf Z_p$，并固定
$$
k=rq+s,\qquad 0\le s<r,\qquad 2\le q\le p-2.
\tag{1}
$$
仍用原 $A,C=B-A$、R233 的有限环 $L_k/pL_k$ 及原评价
$$
j_{k,1}:\mathbf F_p[A,C]\longrightarrow L_k/pL_k.
$$
固定 $d<p$，记
$$
V_d=\ker\bigl(j_{k,1}|_{\mathbf F_p[A,C]_{\le d}}\bigr).
\tag{2}
$$
原轴图为
$$
\phi(A)=c(f^{-1}(A))=-22A^2+O(A^3).
$$
R196 给出的完整第一带条件为
$$
\begin{aligned}
\operatorname{ord}_A(\partial_C^{[j]}P)(A,\phi(A))&\ge (r-2j)_+,
&&0\le j<q,\\
\operatorname{ord}_A(\partial_C^{[q]}P)(A,\phi(A))&\ge (s-2q)_+.
\end{aligned}
\tag{3}
$$
这些是同一个原 $P$ 的条件。因为 $d<p$，本文涉及的 Hasse 导数可以用通常导数除以相应单位阶乘表示。

当 $V_d\ne0$ 时，令
$$
G_d=\gcd\{P:P\in V_d\}\in\mathbf F_p[A,C],
\tag{4}
$$
取任一固定的首系数规范。计算 (4) 只需一组有限基，且不依赖该基。

## 2. 整个原核的共同重因子

**定理 1。** 假设
$$
V_d\ne0,\qquad r-2(q-1)>d(d-1).
\tag{5}
$$
则存在一个依赖 $C$ 的不可约多项式
$F\in\mathbf F_p[A,C]$，满足
$$
\boxed{\qquad F^q\mid G_d.\qquad}
\tag{6}
$$
特别，$q\deg F\le\deg G_d\le d$，并且每个原核向量都被同一个 $F^q$ 整除。

### 2.1. 所需的单向量引理

先回顾并核实 R236 的 resultant 论证可在任意系数域扩张上使用。设 $K/\mathbf F_p$ 为域扩张，$0\ne P\in K[A,C]$，$\deg P\le d$，且
$$
\operatorname{ord}_A(\partial_C^{[j]}P)(A,\phi(A))
\ge r-2j\quad(0\le j<q).
\tag{7}
$$
若关于 $C$ 的全部非恒定不可约因子重数都小于 $q$，则
$$
\gcd(P,\partial_C^{[1]}P,\ldots,\partial_C^{[q-1]}P)=1
\quad\text{在 }K(A)[C]\text{ 中}.
\tag{8}
$$
这里使用 $d<p$：每个依赖 $C$ 的不可约因子的 $C$ 次数小于 $p$，故关于 $C$ 可分。必要时扩张常数域，可以选常数组合
$$
Q=\sum_{j=1}^{q-1}\lambda_j\partial_C^{[j]}P
$$
使 $\gcd(P,Q)=1$ 在 $K(A)[C]$ 中。此时 $\deg Q\le d-1$，且由 (7)
$$
\operatorname{ord}_A Q(A,\phi(A))\ge r-2(q-1).
$$
非零 resultant $R(A)=\operatorname{Res}_C(P,Q)$ 满足
$$
\deg R\le d(d-1),\qquad R=UP+VQ
\tag{9}
$$
其中 $U,V$ 为多项式。代入原图后，(7) 和 (9) 迫使
$\operatorname{ord}_A R\ge r-2(q-1)>\deg R$，矛盾。
若 $P$ 只依赖 $A$，第零条已经给 $\operatorname{ord}_A P\ge r>d$，同样不可能。

因此 $P$ 有一个依赖 $C$ 的至少 $q$ 重因子。这个引理没有要求 $K$ 有限，也没有改变原图的系数。

### 2.2. 从单向量到共同因子

取 $V_d$ 的基 $P_1,\ldots,P_h$，引入代数独立参数 $t_1,\ldots,t_h$，并置
$$
K=\mathbf F_p(t_1,\ldots,t_h),\qquad
P_{\mathrm{gen}}=\sum_{i=1}^h t_iP_i.
\tag{10}
$$
(3) 是线性条件，所以 (7) 对这个同一原核中的通用线性组合成立。由单向量引理，某个依赖 $C$ 的不可约
$H\in K[A,C]$ 满足 $H^m\mid P_{\mathrm{gen}}$，$m\ge q\ge2$。

对任意 $t_i$ 求导。因 $m\ge2$，Leibniz 公式给
$$
H\mid\frac{\partial P_{\mathrm{gen}}}{\partial t_i}=P_i
\qquad(1\le i\le h).
\tag{11}
$$
这里对 $K$ 的有理函数系数求导即可；不需要在代数闭包上延拓导子，也不需要除以 $m$。
于是 $H$ 整除 $G_d$ 在 $K[A,C]$ 中的像。

纯超越域扩张保持 $\mathbf F_p[A,C]$ 中不可约多项式的不可约性。因此 $H$ 与某个固定的不可约因子
$F\mid G_d$ 伴随。该 $F$ 依赖 $C$。再由
$$
F^q\mid\sum_i t_iP_i
$$
以及参数 $t_i$ 的代数独立性，在
$(\mathbf F_p[A,C]/(F^q))\otimes_{\mathbf F_p}K$ 中比较参数系数，得到
$$
F^q\mid P_i\quad\text{对全部 }i.
$$
故 $F^q\mid G_d$，证明定理。$\square$

这个证明排除了“不同向量的重因子可以随意变动”的可能性。关键是对整个核的通用线性组合应用同一个实际 Hasse 条件，再对系数参数求导。

### 2.3. 非空的最后一块可以再增加一次重数

若更强地有
$$
s-2q>d(d-1),
\tag{12}
$$
则 (3) 的 $j=0,\ldots,q$ 全部具有大于 $d(d-1)$ 的消失阶。对上述论证使用 $q+1$ 个 Hasse 条件，得到某个依赖 $C$ 的不可约 $F$，使
$$
F^{q+1}\mid G_d.
\tag{13}
$$
(12) 自动保证 (5)；没有把最后一块当成完整长度 $r$。

## 2.4. 共同因子由实际高接触唯一确定

下面给定理 1 的一个定量加强，同时给出另一份不使用通用参数的证明。对非零多项式 $H$，记
$$
v_\phi(H)=\operatorname{ord}_A H(A,\phi(A))\in\mathbf Z_{\ge0}\cup\{+\infty\}.
$$
仍假设 (5)。则存在唯一的、在乘非零常数意义下确定的不可约 $F$，满足
$$
e:=\deg F\le\lfloor d/q\rfloor,\qquad
h:=v_\phi(F)>e(d-1),
\tag{14}
$$
且每个 $0\ne P\in V_d$ 的这个因子的重数至少为 $q$。
这里的唯一性只指满足 (14) 的低次数因子，不声称原核没有其他共同因子。

**证明。** 先对一个 $0\ne P\in V_d$ 分解为不可约因子的乘积。因为
$v_\phi(P)\ge r$ 且 $\deg P\le d$，至少一个因子 $F$ 满足
$$
\frac{v_\phi(F)}{\deg F}\ge\frac rd>d-1.
\tag{15}
$$
若某个因子的接触为无穷，直接选这样的因子。只依赖 $A$ 的不可约因子接触至多一次：唯一可能在原点为零的是 $A$ 本身。因此 (15) 的因子依赖 $C$。写
$$
P=F^mG,\qquad F\nmid G,\qquad e=\deg F,\quad g=\deg G\le d-me.
$$
因 $d<p$，$F$ 关于 $C$ 可分。对 $F,F_C$ 的非零 resultant 使用无分母的 Bézout 恒等式及总次数界，得到
$$
\min\{v_\phi(F),v_\phi(F_C)\}\le e(e-1).
$$
由于 (15) 的严格下界至少为 $e(e-1)$，可知
$$
\mu:=v_\phi(F_C)\le e(e-1)<+\infty.
\tag{16}
$$
同样，对 $F,G$ 使用 resultant；$G$ 为非零常数时直接处理。因为
$h>e(d-1)\ge eg$，得到
$$
z:=v_\phi(G)\le eg\le e(d-me).
\tag{17}
$$
这一步保留了 $F_C$ 和 $G$ 在原点可能有的正接触阶，没有把它们当成单位。

对每个 $0\le j\le m$，多项式 Hasse 乘法公式准确给
$$
\partial_C^{[j]}(F^mG)
=\binom mj F^{m-j}F_C^jG+F^{m-j+1}H_j
\tag{18}
$$
其中 $H_j\in\mathbf F_p[A,C]$；$j=0$ 时可取 $H_0=0$。
第一项之外的每个项，至少有 $m-j+1$ 个未求导的 $F$ 因子。又因为 $m\le d<p$，$\binom mj$ 是单位。
由 (16)—(17)，
$$
j\mu+z\le je(e-1)+e(d-me)
\le e(d-m)<h.
\tag{19}
$$
所以第一项严格低于余项的接触阶，不能与其相消，准确有
$$
\boxed{\quad
v_\phi(\partial_C^{[j]}P)
=(m-j)h+j\mu+z\quad(0\le j\le m).
\quad}
\tag{20}
$$
若 $h=+\infty$，约定 $0h=0$；$j<m$ 时两侧为无穷，$j=m$ 时仍由 (19) 给有限的准确值。

如果 $m<q$，则把 $j=m$ 代入 (20)，得到
$$
v_\phi(\partial_C^{[m]}P)=m\mu+z
\le e(d-m)\le d(d-1).
$$
这与 (3)、(5) 给出的
$v_\phi(\partial_C^{[m]}P)\ge r-2m>d(d-1)$ 矛盾。
故 $m\ge q$，从而 $e\le\lfloor d/q\rfloor$。

最后，若存在两个不同的不可约 $F_1,F_2$ 满足 (14)，次数分别为 $e_1,e_2$，则 $e_i\le d/2\le d-1$。其非零 resultant 的次数至多 $e_1e_2$，而 Bézout 恒等式给
$$
\operatorname{ord}_A\operatorname{Res}_C(F_1,F_2)
\ge\min\{v_\phi(F_1),v_\phi(F_2)\}>e_1e_2,
$$
矛盾。所以这个低次数高接触因子唯一，不随 $P$ 改变。$\square$

## 2.5. 原完整核的两条接触不等式

一旦找到满足 (14) 的因子 $F$，对任意
$$
P=F^mG,\quad F\nmid G,\quad \deg P\le d,\quad m\ge q
$$
都可以使用 (16)—(20)，不需要预先假设 $P\in V_d$。注意
$$
h-\mu\ge e(d-e)+1\ge2.
\tag{21}
$$
因此在全部完整块 $0\le j<q$ 中，(3) 的最强一条准确为 $j=q-1$。原核条件等价于
$$
\boxed{\begin{aligned}
(m-q+1)h+(q-1)\mu+z&\ge r-2(q-1),\\
(m-q)h+q\mu+z&\ge (s-2q)_+.
\end{aligned}}
\tag{22}
$$
反向直接将 (20)—(21) 代入所有原条件 (3) 即得。正向还用 §2.4 保证每个非零原核向量确实含这个 $F^q$。

所以，在 (5) 下可以先找一个次数至多 $d/q$、接触满足 (14) 的原曲线因子。找不到则 $V_d=0$；找到后，原 $q+1$ 组 Hasse 条件由 (22) 完整保留。这里 $z=v_\phi(G)$ 仍是实际余因子的接触，不能任意设为零。

### 更强的最后一块阈值

若 $m=q$，(16)—(17) 给
$$
q\mu+z\le e(d-q)\le\lfloor d/q\rfloor(d-q).
$$
因此在 (5) 下，只要
$$
\boxed{\quad
s-2q>\lfloor d/q\rfloor(d-q),
\quad}
\tag{23}
$$
就已经迫使所有原核向量的共同高接触因子重数至少为 $q+1$。
(23) 严格改进 §2.3 的充分阈值 (12)。它使用了同一因子真实的 $F_C$ 接触上界，而没有假定法向导数为单位。

例如在 $q=2$ 时，写 $h=v_\phi(F)$、$\mu=v_\phi(F_C)$、$z=v_\phi(G)$，原条件就是
$$
(m-1)h+\mu+z\ge r-2,
\qquad (m-2)h+2\mu+z\ge(s-4)_+.
$$
当 $s-4>\lfloor d/2\rfloor(d-2)$，共同因子至少为三重。这个结论仅涉及原模 $p$ 核，不自动提升为模 $p^2$ 关系。

## 3. 所有深层方向必须经过同一个因子

令 $J=J_{d,<k}:E_d(\mathcal O)\to L_k$ 为原完整归一矩阵，仍在同一个 $k$。定义 R233 的实际提升层
$$
\mathcal F_T(d)=\operatorname{im}\bigl(
\{P\in E_d:J(P)\in p^TL_k\}\to E_d/pE_d\bigr),
\quad T\ge1.
\tag{24}
$$
因为 $\mathcal F_T(d)\subset V_d$，定理 1 立即给
$$
\mathcal F_T(d)\subset G_d\,\mathbf F_p[A,C]_{\le d-g},
\qquad g=\deg G_d.
\tag{25}
$$
乘 $G_d$ 在抽象多项式环上单射。因此每个 $T$ 都有
$$
\boxed{\quad
\dim\mathcal F_T(d)\le\binom{d-g+2}{2}
\le\binom{d-q\deg F+2}{2}.
\quad}
\tag{26}
$$
若把特征零核的 Smith 指数记为 $+\infty$，则 (26) 同时是原矩阵中 Smith 指数至少 $T$ 的个数上界。对 $T=1,\ldots,N$ 求和，得到
$$
\boxed{\quad
B_N(d,k)\le N\binom{d-g+2}{2}.
\quad}
\tag{27}
$$
这些式子只针对满足 (5) 的这个次数 $d$。不得把在 $E_d$ 中求得的共同因子，直接推广为更大 $E_D$ 的全部核向量的共同因子。

对于 R223 的 primitive 深关系入口，(6) 说明：在 (5) 的主带子区间，任何候选关系的非零模 $p$ 约化都必须携带同一个 $q$ 重原因子。只提高精度不会绕过这个限制。

## 4. 共同因子后的首次提升是一个确定的有限线性问题

定义约去共同因子后的实际空间
$$
W_d=\{Q\in\mathbf F_p[A,C]_{\le d-g}:G_dQ\in V_d\}.
\tag{28}
$$
乘 $G_d$ 给 $W_d\simeq V_d$。任取同次数的整提升
$\widetilde G_d,\widetilde Q$，由 (28)
$$
J(\widetilde G_d\widetilde Q)\in pL_k.
$$
记 $S_d=j_{k,1}(\mathbf F_p[A,C]_{\le d})\subset L_k/pL_k$。定义
$$
\boxed{\quad
\omega_{G_d}(Q)=
\frac{J(\widetilde G_d\widetilde Q)}p
\pmod{pL_k+S_d}
\quad\in (L_k/pL_k)/S_d.
\quad}
\tag{29}
$$
式中先在整个实际输出中除以 $p$；$pL_k+S_d$ 表示其约化后再商去 $S_d$。

**定理 2。** (29) 是与提升选择无关的 $\mathbf F_p$ 线性映射，而且
$$
\boxed{\quad
\mathcal F_2(d)=G_d\ker\omega_{G_d}.
\quad}
\tag{30}
$$

**证明。** 改变两个提升，乘积的变化模 $p^2$ 为
$$
p(\widetilde G_d Q_1+G_1\widetilde Q),
$$
其中括号内仍是次数至多 $d$ 的原多项式。除以 $p$ 后的输出变化模 $p$ 属于 $S_d$，故 (29) 良定义。相同论证给线性。

任何约化为 $G_dQ$ 的原整多项式都可写成
$$
P=\widetilde G_d\widetilde Q+pR,
\qquad R\in E_d.
\tag{31}
$$
于是 $J(P)\in p^2L_k$ 准确等价于
$$
\frac{J(\widetilde G_d\widetilde Q)}p+J(R)=0
\quad\text{在 }L_k/pL_k\text{ 中}.
$$
可选这样的 $R$ 当且仅当 (29) 为零，得到 (30)。$\square$

### 4.1. 保留原加权乘法的实际计算式

令 $b_n=p^{-e_n}u^n$ 为 R233 的原目标基，写
$$
J_n(\widetilde G_d)=x_n,\qquad J_n(\widetilde Q)=y_n.
$$
在同一个完整前缀中，(29) 的未取商代表第 $n$ 坐标准确为
$$
\frac1p\sum_{a+b=n}
p^{e_n-e_a-e_b}x_ay_b\pmod p,
\qquad n<k.
\tag{32}
$$
超可加性使和中的所有项整；(28) 只保证整个和被 $p$ 整除，不允许逐项无条件除以 $p$。因此 (32) 保留实际 carry 与全部低次补偿，并只读取原前缀 $<k$。

如果只使用定理 1 找到的因子 $F^q$，也可完全同样地把
$G_d$ 替换为 $F^q$、把 (28) 的源换成其真实原像。使用完整 gcd 只会减小待计算的有限源。

## 5. 这给出的正向接口与仍缺的算术

在 (5) 中，寻找深关系可以先在原模 $p$ 核中求一个共同因子，再在较小空间 (28) 上计算准确的首次障碍 (29)。这是一个共同因子，而非对大量候选分别猜测不同因子。

但 (31) 的修正 $R$ 必须允许取遍原 $E_d$。把它限制为 $\widetilde G_d$ 的倍数，会加入未证明的因子提升假设，可能丢掉真实提升。相反，(30) 并不声称高精度关系在 $\mathcal O[A,C]$ 中也被 $\widetilde G_d$ 整除。

目前原双完整中央条件仍没有证明 $V_d\ne0$ 在所需的固定比例低次数发生，也没有证明 (29) 的实际核含所需 primitive 方向。原径向方程可以用于算这些原系数，但其存在本身不令 (29) 消失。这里没有从有限样本推断该结论。

依赖：R196 的原 graph–Hasse 等价、R233 的同一前缀环结构与提升层、R236 的单向量 resultant 引理。所有新增断言的证明均在本文给出。
