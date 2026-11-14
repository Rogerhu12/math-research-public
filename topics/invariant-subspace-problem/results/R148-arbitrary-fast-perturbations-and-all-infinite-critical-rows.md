# R148：任意快扰动的型预算与全行无限临界二阶例

主会话已全文核验；完整ISP仍未解决。研究原稿见[原稿](../notes/2026-11-12-arbitrary-fast-perturbations-and-all-infinite-critical-rows-0c-agent.md)。


日期：2026-11-12（UTC）。独占作者：critical_kernel。根代理预留 R148。
状态：以下定理、有限多扰动预算和全行无限二次例均已完整证明。
扰动 $E$ 不要求具有解析加性 cocycle；例子明确验证它不具有这一性质。

## 1. 任意单个快扰动

沿用 $\mathcal A=\overline{\mathbb C[I,A]}$、唯一常数特征 $\chi$，
真实 dyadic gauge $\gamma_\zeta(T)=U_\zeta T U_\zeta^*$，
以及

$$
\tau_4(T)=\liminf_{n\to\infty}
\frac{-\log\|T^n\|}{n^4}.
$$

设 $B\in\mathcal A$ 非零、$\chi(B)=0$，首形式阶为 $h\ge1$，
且每个 dyadic 增量 $\gamma_\zeta(B)-B$ 都是真正收敛标量解析芽
在 $A$ 上的演算。

令 $r(z)=z^qu(z)$ 为非零解析芽，$u(0)\ne0$，
允许

$$
0\le q<h.
\tag{1.1}
$$

取任意 $E\in\mathcal A$；**不假设其 gauge 差解析**。
假设

$$
\boxed{
\tau_4(E)>
8\,\frac{100}{15}(h-q)^4.
}
\tag{1.2}
$$

**定理1.1。** 实际有界算子

$$
S=B+r(A)E
\tag{1.3}
$$

非零，首形式阶为 $h$，单射且值域稠密；$S1$ 对 $A$ 循环。
所有 $\lambda\ne0$ 处 $S-\lambda I$ 都为 $\mathcal A$ 单位。

$q=0$ 包括直接的任意快扰动 $B+E$。
这一步不需要任何负次幂或未知有界除法。

## 2. 类型预算的两个基本事实

### 2.1 非零形式首阶限制全空间型

对 $T\in\mathcal A$ 的形式系数，真实物理头压缩给

$$
W_n|\gamma_n(T)|\le\|T\|,\qquad W_n=\|A^n\|.
\tag{2.1}
$$

若 $T$ 首阶为 $k$、首系数为 $\beta\ne0$，则 $T^n$ 的首系数
是位于 $kn$ 的 $\beta^n$，所以

$$
\|T^n\|\ge|\beta|^nW_{kn}.
$$

R109 的 $\tau_4(A^k)=100k^4/15$ 因此给

$$
\boxed{\tau_4(T)\le\frac{100}{15}k^4.}
\tag{2.2}
$$

特别地，正四次型迫使 $\chi(T)=0$。
非零 $\mathcal A$ 元素都有有限首阶，使用的是 R32 的形式系数忠实性。

若 $E\ne0$ 首阶为 $k$，由 (1.2)、(2.2)，

$$
k>8^{1/4}(h-q)>h-q.
\tag{2.3}
$$

于是 $q+k>h$，所以 (1.3) 的扰动不能取消 $B$ 的首项。
若 $E=0$，结论直接由加性 cocycle 定理 R122 得到。
这同时证明主定理中的非零性和首阶断言。

### 2.2 有限交换和的 harmonic 下界

若有限个有界交换算子 $T_1,\ldots,T_s$ 满足
$\tau_j=\tau_4(T_j)>0$，则

$$
\boxed{
\tau_4\!\left(\sum_{j=1}^sT_j\right)
\ge
\left(\sum_{j=1}^s\tau_j^{-1/3}\right)^{-3}.
}
\tag{2.4}
$$

证明：先取 $0<b_j<\tau_j$，由 $\liminf$ 定义吸收有限小次幂，
得到 $\|T_j^n\|\le C_j^ne^{-b_jn^4}$。
多项式展开及四次 Hölder 给

$$
\left\|\left(\sum_jT_j\right)^n\right\|
\le\left(\sum_jC_j\right)^n
\exp\!\left[-\left(\sum_jb_j^{-1/3}\right)^{-3}n^4\right].
$$

令 $b_j\uparrow\tau_j$ 即得。
零算子可省略；无穷型的逆三次根按0计。

乘以一个固定有界交换因子不会降低 $\tau_4$，
因为相应幂范数至多再乘该因子范数的 $n$ 次方。
同时 $\gamma_\zeta$ 是等距自同构，所以

$$
\tau_4(\gamma_\zeta(E))=\tau_4(E).
\tag{2.5}
$$

对 $E$ 和 $\gamma_\zeta(E)$ 的两个有界倍数使用 (2.4)，
下界正好是 $\tau_4(E)/2^3$。
主定理的常数8来自这个明确的两项损失。

## 3. 真正的 gauge 除法

记

$$
b_\zeta(A)=\gamma_\zeta(B)-B,
$$

其中 $b_\zeta(z)$ 为真解析芽。
只要 $\zeta^h\ne1$，其首阶恰为 $h$。
因此

$$
F_\zeta(z)=\frac{b_\zeta(z)}{z^q}
\tag{3.1}
$$

是真解析芽，首阶为 $h-q$。
$q=0$ 时只是原增量，没有除法。

直接使用 $r(z)=z^qu(z)$，在实际有界代数中展开：

$$
\begin{aligned}
\gamma_\zeta(S)-S
&=b_\zeta(A)
+r(\zeta A)\gamma_\zeta(E)-r(A)E\\
&=A^q\bigl[F_\zeta(A)+K_\zeta\bigr],
\end{aligned}
\tag{3.2}
$$

其中

$$
\boxed{
K_\zeta=
\zeta^q u(\zeta A)\gamma_\zeta(E)-u(A)E
\in\mathcal A.
}
\tag{3.3}
$$

这次提取 $A^q$ 是从两个已给出的真解析前因子中逐项完成的；
没有从 $E$ 或 $\gamma_\zeta(E)-E$ 的形式首阶推断有界整除。

由 §2，

$$
\tau_4(K_\zeta)\ge\frac{\tau_4(E)}8
>
\frac{100}{15}(h-q)^4.
\tag{3.4}
$$

此界对每个固定 $\zeta$ 成立；
因子范数可依赖 $\zeta$，它们只产生 $O(n)$ 的对数项。

## 4. 每个未知限制上的稠密像与排核

R140 的子商型定理说明：
若 $F$ 真解析、首阶为 $\ell\ge1$，
且 $\tau_4(K)>100\ell^4/15$，则对每个闭 $A$ 不变 $M$，

$$
\overline{(F(A)+K)M}=M.
\tag{4.1}
$$

为强调其逻辑来源，若右侧闭包 $L$ 真小于 $M$，
在非零商 $Q=M/L$ 上便有 $F(A_Q)=-K_Q$；
R140 给左边精确型 $100\ell^4/15$，
而压缩范数给右边型不小于 $\tau_4(K)$，矛盾。

因此 (3.4) 给

$$
\overline{(F_\zeta(A)+K_\zeta)M}=M
\qquad(\zeta^h\ne1).
$$

$A^q$ 在每个闭不变限制上的值域稠密（$q=0$ 时为恒等），
故 (3.2) 推出

$$
\boxed{
\overline{(\gamma_\zeta(S)-S)M}=M
\qquad(\zeta^h\ne1).
}
\tag{4.2}
$$

现在取 $M=\ker S$。由所有有界交换子的 $B$ 对称性，

$$
B((\gamma_\zeta(S)-S)M,U_\zeta M)=0.
$$

(4.2) 给 $B(M,U_\zeta M)=0$，
除外根仅为 dyadic 群中的有限子群
$\mu_{2^{v_2(h)}}$。
R122 的 Fourier 支撑、全本质支撑和逐柱秩证明遂给
$\dim M\le2^{v_2(h)}$；
$A$ 单射拟幂零不允许非零有限维不变空间，所以 $M=0$。

$C$ 对称性再给稠密值域，且 $1$ 循环给 $S1$ 循环。
由 §2 的 $\chi(E)=0$ 与 $\chi(B)=0$，有 $\chi(S)=0$；
非零谱参数处的可逆性由 R32 得到。定理1.1完成。

## 5. 任意有限个快扰动

更一般地，令

$$
S=B+\sum_{\nu=1}^s r_\nu(A)E_\nu,
\qquad
r_\nu(z)=z^{q_\nu}u_\nu(z),\quad u_\nu(0)\ne0,
$$

$$
q=\min_\nu q_\nu,\qquad 0\le q<h,\qquad
\tau_\nu=\tau_4(E_\nu)>0.
$$

所有 $E_\nu$ 只需属于 $\mathcal A$，不要求加性 cocycle。
若

$$
\boxed{
\frac18
\left(\sum_{\nu=1}^s\tau_\nu^{-1/3}\right)^{-3}
>
\frac{100}{15}(h-q)^4,
}
\tag{5.1}
$$

则同样有 $S$ 首阶 $h$、单射稠密及 $S1$ 循环。

证明中提取共同 $A^q$ 后，扰动成为 $2s$ 个交换项：

$$
\sum_{\nu=1}^s A^{q_\nu-q}
\left[
\zeta^{q_\nu}u_\nu(\zeta A)\gamma_\zeta(E_\nu)
-u_\nu(A)E_\nu
\right].
\tag{5.2}
$$

每个成对项的型至少为 $\tau_\nu$。
(2.4) 对全部 $2s$ 项给 (5.1) 左端。
其余证明与 §§3–4 相同。

此外 (5.1) 迫使每个非零 $E_\nu$ 的首阶 $k_\nu>h-q$，
故 $q_\nu+k_\nu>h$，保证没有未检查的低阶取消。

这是有限多扰动定理；没有将有限和界未经一致常数控制地搬到任意无限和。

## 6. 构造非加性扰动：真实的低位除法

下面给一个全行无限的**纯 Boolean 二次**实例。
它会用到一个明确构造出的有界商，先逐项检查其合法性。

令

$$
B=\sum_{j\ge2}(j+1)^{-2}Y_j,
\qquad
E_{\rm raw}=
\sum_{\substack{1\le i<j\\j\ge3}}
c_{ij}Y_iY_j,
$$

$$
c_{ij}=\alpha_i^2e^{-(i+j+4)^8}.
\tag{6.1}
$$

这里 $\alpha_i$ 是本题真实权值，正且不超过1。
两和均绝对范数收敛。
$B$ 是任意慢尾方向的一个明确选择，
其首形式阶为 $h=4$，每个 gauge 增量为有限解析和。

对每个 $i\ge1$，有限解析比值

$$
\frac{y_i(z)}{y_0(z)}
=\frac{d_0}{d_i}z^{2^i-1}
(1+z/d_0)(1+z^{2^i}/d_i)^{-1}
\tag{6.2}
$$

在零点解析。
记 $n(i,j)=2^i+2^j-1$。真实二进位范数给

$$
W_{n(i,j)}
=d_jW_{2^i-1}
=\frac{d_id_j}{\alpha_i}.
\tag{6.3}
$$

因此每一项实际为

$$
\frac{y_i(A)}{y_0(A)}Y_j
=
\frac{d_0}{\alpha_i}
\frac{A^{n(i,j)}}{W_{n(i,j)}}U_{ij},
$$

$$
U_{ij}=(I+N_0)(I+N_i)^{-1}(I+N_j)^{-1},
\qquad \|U_{ij}\|\le18,\quad\chi(U_{ij})=1.
\tag{6.4}
$$

从而以下级数真实绝对范数收敛：

$$
F:=
\sum_{\substack{1\le i<j\\j\ge3}}
c_{ij}\frac{y_i(A)}{y_0(A)}Y_j
\in\mathcal A,
\qquad
\boxed{Y_0F=E_{\rm raw}.}
\tag{6.5}
$$

因为其规范化系数绝对和受
$18d_0\sum_{i,j}\alpha_i e^{-(i+j+4)^8}<\infty$ 控制。
本稿没有先将无界 $Y_0^{-1}$ 作用到一个未知向量或算子上；
$F$ 是 (6.5) 的明确范数级数。

### 6.1 $F$ 的真实四次型

$n(i,j)$ 对这些有序对单射；
其最小值是 $n(1,3)=9$。
把 $U_{ij}/18$ 作为范数不超过1的因子，
相应归一化系数为

$$
\widetilde c_{ij}
=18d_0\alpha_i e^{-(i+j+4)^8}.
\tag{6.6}
$$

它们的非增重排满足超三次条件：
若 $\widetilde c_{ij}>18d_0e^{-R^8}$，则 $i+j+4<R$，
这样的对数至多 $R^2$。
所以对大 $\ell$，有某个绝对常数 $c>0$ 使

$$
-\log\widetilde c_\ell^*\ge c\ell^4-O(1),
\qquad
\frac{-\log\widetilde c_\ell^*}{\ell^3}\longrightarrow+\infty.
\tag{6.7}
$$

R110/R115 的真实重复占据估计因而给，
按 $n(i,j)\ge K$ 截断的尾 $F_{\ge K}$ 满足

$$
\tau_4(F_{\ge K})\longrightarrow+\infty.
\tag{6.8}
$$

每个有限头是真正解析函数，首阶稳定为9，且是 $A^9$ 乘实际单位。
于是 R146 引理5.1（或有限头、尾幂的二项 Hölder证明）给

$$
\boxed{\tau_4(F)=\frac{100}{15}9^4.}
\tag{6.9}
$$

为使这一步完全明确：
有限头的型为 $100\cdot9^4/15$；
尾型趋无穷时，二项 Hölder 的 harmonic 下界趋向该有限头型。
反向由第9阶首系数在每个 $F^n$ 中的唯一最低项和 (2.1) 给出。
这没有从 $F$ 的单射性推断幂型。

### 6.2 $F$ 确实不具有解析加性 cocycle

先证明 $E_{\rm raw}$ 不是一个标量解析芽的演算。
取 $\omega=i$，其阶为4。它只改变 (6.1) 中最低的 $Y_1$，
其他 $Y_j,j\ge2$ 都被固定。因此

$$
\gamma_\omega(E_{\rm raw})-E_{\rm raw}
=
(\gamma_\omega(Y_1)-Y_1)
\sum_{j\ge3}c_{1j}Y_j.
\tag{6.10}
$$

第一个因子是真解析非零函数，首阶为2。
第二个是无限非零第一阶尾。
R120 的解析第一阶乘子分类说明，后者不可能为真解析芽演算：
真解析的第一阶乘子只能有有限支撑。

如果 (6.10) 为真解析芽演算，连续形式系数先保证其标量芽
可被第一个解析因子整除，再取消已知单射的解析 $A^2$ 单位因子，
便会把第二个因子写成真解析演算，矛盾。
所以 (6.10) 不解析，特别 $E_{\rm raw}$ 不解析。

另一方面 $E_{\rm raw}\in\mathcal A_2$，故被 $\gamma_{-1}$ 固定。
由 (6.5) 及实际有限解析恒等式

$$
\gamma_{-1}(Y_0)(-V_0)=Y_0
$$

取消单射的 $\gamma_{-1}(Y_0)$，得

$$
\gamma_{-1}(F)=-V_0F,\qquad
\gamma_{-1}(F)-F=-(I+V_0)F.
\tag{6.11}
$$

$I+V_0=2(I+N_0)^{-1}$ 是真解析单位。
若 (6.11) 的差为真解析演算，则 $F$ 也为真解析演算，
从而 $E_{\rm raw}=Y_0F$ 解析，和上面矛盾。

因此

$$
\boxed{
\gamma_{-1}(F)-F\text{ 不是真解析演算；}
\quad F\text{ 不属于加性解析 cocycle 类。}
}
\tag{6.12}
$$

这直接验证了主定理对扰动不要求 additive 条件的实质使用。

## 7. 所有行无限且所有首行和为零的二阶循环例

现在对 $B+F$ 使用定理1.1，取 $q=0,r\equiv1$。
由 $h=4$ 和 (6.9)，

$$
\tau_4(F)=\frac{100}{15}9^4
>
8\,\frac{100}{15}4^4
$$

因为 $6561>2048$。
所以 $B+F$ 单射稠密。
再乘已知单射稠密的 $Y_0$，得到

$$
\boxed{
T=Y_0B+E_{\rm raw}
\text{ 单射稠密，且 }T1\text{ 循环}.
}
\tag{7.1}
$$

它是实际 Boolean 二次算子，对应向量

$$
f=
\sum_{j\ge2}(j+1)^{-2}
b_0^{\rm phys}b_j^{\rm phys}
+
\sum_{\substack{1\le i<j\\j\ge3}}
\alpha_i^2e^{-(i+j+4)^8}
b_i^{\rm phys}b_j^{\rm phys}.
\tag{7.2}
$$

有限不同位的实际乘法恒等式给
$Y_iY_j1=b_i^{\rm phys}b_j^{\rm phys}$；
绝对范数收敛保证 (7.2) 就是 (7.1) 的实际向量。
它非零、连续、有界、全局 Walsh 次数至多2。

每一物理位都有无限个非零二次邻边：
位0连接所有 $j\ge2$；
位1、位2及更高位都在第二个和中连接无穷多个更高位。
因此不能把任何包含最低位的整行收入一个有限解析头。

将 $f$ 写成

$$
f=a_*+\sum_i a_i\chi_i+\sum_{i<j}b_{ij}\chi_i\chi_j,
$$

每条 Boolean 边 $C_{ij}b_i^{\rm phys}b_j^{\rm phys}$
贡献 $b_{ij}=C_{ij}/4$ 和两个线性系数 $-C_{ij}/4$。
总绝对和有限，所以逐行可合法求和，并得到

$$
\boxed{
\tau_i=a_i+\sum_{j\ne i}b_{ij}=0
\quad\text{对所有 }i\ge0.
}
\tag{7.3}
$$

这不是 R133 的非零首行和情形，也不要求 R139 的最低各行有限。
慢行仍为 $(j+1)^{-2}$；
快行的实际低位除法、进位权与型预算已在 §6 逐项支付。

本例不代表任意全行无限临界二次都已解决。
两个或多个不满足本稿型预算的独立慢行仍开放。

## 8. 范围

主定理只控制扰动的实际算子幂；
它不要求扰动能写成同一个加性方向的解析函数，
也不要求其 gauge 差为解析芽。
常数8来自 $E$ 与 $\gamma_\zeta(E)$ 的两个交换项，未省略该损失。

有限多扰动必须满足 (5.1)；
无限和若没有另外的统一幂常数与可和预算，不由本稿自动覆盖。
§6 的无限构造是先用 R115 的真实归一化级数定理建立一个
已经满足型条件的单个有界算子 $F$，再使用主定理，
不是把有限和估计形式地写成无限和。

完整 ISP 与一般二阶核问题仍保持开放。

