# R374：实际六层 CM 商的惯性无扭点与准确零像

**状态：已证明。** R348 的每个实际 CM 因子，在 $\mathbb Q_p$ 的最大未分歧扩张上都没有非零扭点。这一性质对整个同源类成立，不要求所选投影、Hecke 阶或 Tate 格在 $p$ 处极大或整饱和。因此 R348 所选中心值非零的因子具有 $A(\mathbb Q)=0$，实际有理点的 Abel–Jacobi 像准确为零。结论尚不涉及模曲线整数模型上的余切满射或形式浸入。

## 1. 定理

沿用 R348：

$$
p\ge41,\quad p\equiv2\pmod3,\quad
K=\mathbb Q(\sqrt{-3}),\quad
T_p=\mathbb F_{p^2}^{\times}/\mathbb F_p^\times,
\tag{374.1}
$$

$$
\theta(\zeta_3)=\zeta_3^{-1},\qquad
\theta(\sqrt{-3})=-1,\qquad
g_\theta=f_{\Psi_\theta\kappa_4^{-1}},
\qquad N(g_\theta)=108p^2.
\tag{374.2}
$$

令 $A_\theta/\mathbb Q$ 为 $g_\theta$ 的模 abelian variety，
$F_\theta$ 为其 Hecke 系数域。令
$B/\mathbb Q_p$ 为任意与 $(A_\theta)_{\mathbb Q_p}$
$\mathbb Q_p$-同源的 abelian variety。则：

$$
F_\theta\subset\mathbb Q(\mu_{p+1})^+,
\qquad p\text{ 在 }F_\theta\text{ 中完全分裂},
\tag{374.3}
$$

并存在一个惯性元素 $\tau\in I_p$，使对每个素数 $\ell$，

$$
1-\tau:T_\ell(B)\longrightarrow T_\ell(B)
\quad\text{为同构}.
\tag{374.4}
$$

特别地，若 $\mathbb Q_p^{\mathrm{nr}}$ 表示代数闭包中的最大未分歧扩张，则

$$
B(\mathbb Q_p^{\mathrm{nr}})_{\mathrm{tors}}=0.
\tag{374.5}
$$

若 $B$ 在 $\mathbb Q$ 上定义且与 $A_\theta$ 在 $\mathbb Q$ 上同源，进一步有

$$
L(g_\theta,1)\ne0
\quad\Longrightarrow\quad
B(\mathbb Q)=0.
\tag{374.6}
$$

R348 对每个上述 $p$ 保证至少有一个这样的 $\theta$。因而可以选一个正维商

$$
q:J_{Z_p}\twoheadrightarrow B,\qquad
Z_p:\ j=6912a^3(1-a^3),
\tag{374.7}
$$

使

$$
q([P-c_1])=0
\quad\text{对所有 }P\in Z_p(\mathbb Q).
\tag{374.8}
$$

其中 $c_1$ 是 R348 中 $j=0,a=1$ 的实际有理 CM 点。这里的零是 abelian variety 群中的准确零，不只是模扭点或模同源的零。

## 2. 所有系数嵌入与固定 CM 参考

令

$$
M=p+1,\qquad L=\mathbb Q(\mu_M),\qquad r=\operatorname{ord}(\theta).
\tag{374.9}
$$

$6\mid M$，故 $K\subset L$。R348 的理想公式中，
$\Psi_\theta((\alpha))=\alpha\epsilon_3(\alpha)\theta(\alpha)$
的全部值在 $L$ 中，$\kappa_4$ 的值也在 $\mu_3\subset L$。
因此 $g_\theta$ 的 Fourier 系数在 $L$ 中。它们为实数，所以
$F_\theta\subset L^+$。

$p$ 不分歧于 $L$，其 Frobenius 把 $\mu_M$ 送到其 $p$ 次幂；由于
$p\equiv-1\pmod M$，该 Frobenius 正是复共轭。它在 $L^+$ 上平凡，证明 (374.3)。

(374.2) 的两个指定值还给出

$$
6\mid r,\qquad r\mid p+1.
\tag{374.10}
$$

故 $r$ 至少有两个不同素因子。对 $F_\theta$ 的任意系数嵌入，延拓到
$L$ 后作用于 $\mu_M$ 为取某个与 $M$ 互素的幂。若该嵌入同时共轭 $K$，将 Hecke 角色重新写成无穷型 $(1,0)$ 时还会将有限角色取逆。这两种操作都保持角色阶 $r$。所以每个系数嵌入下的 $p$ 惯性有限特征都仍有准确阶 $r$，不是某个可能变成素数幂阶的角色。

取固定参考曲线

$$
E_0:\ y^2=x^3-1.
\tag{374.11}
$$

它在 $p>3$ 有好约化，且有 $\mathcal O_K$-CM。以无穷型 $(1,0)$ 规范其代数 Hecke 角色 $\Psi_0$。则

$$
\eta_\theta=\frac{\Psi_\theta\kappa_4^{-1}}{\Psi_0}
\tag{374.12}
$$

为有限阶 Hecke 角色，因为分子分母具有相同的代数无穷型。其在 $p$ 处单位群上的限制准确是 $\theta^{-1}$：$\Psi_0$ 在此处未分歧，而 R348 已证明 $\kappa_{4,p}$ 在整个 $K_p^\times$ 上平凡。

对每个 $\ell$，包括 $\ell=p$，相应的一维 CM Galois 角色满足

$$
\psi_{\theta,\ell}
=\psi_{0,\ell}\,\eta_{\theta,\ell}
\quad\text{在 }G_{K_p}\text{ 上}.
\tag{374.13}
$$

在 $\ell=p$ 时不能把代数 Hecke 角色的有限局部分量直接当作整个 Tate 角色；(374.13) 的成立是因为两个角色的无穷型相同，故 $\ell$ 进实现中的代数修正项相消。Serre–Tate（1968）Theorem 11 的
$\rho_\ell(a)=\varepsilon(a)\psi_\ell(a_\ell^{-1})$
正好给出这一点。

$K_p/\mathbb Q_p$ 是未分歧二次扩张，所以
$I_{K_p}=I_p$。下文只在惯性上运算；不需要把有限阶角色延拓为 $\mathbb Q_p$ 的一维角色。

## 3. 异于 $p$ 的全部扭点

取 $\tau\in I_p$，使其在与
$(\mathcal O_K/p)^\times=\mathbb F_{p^2}^\times$
对应的 tame 惯性商中为生成元。由于 $E_0$ 在 $p$ 好约化，
对 $\ell\ne p$，$\psi_{0,\ell}$ 在惯性上平凡。因此
$\tau$ 在 $V_\ell(A_\theta)$ 的每个 CM 特征线上作用为一个原始
$r$ 次单位根，或其共轭。§2 已核准这对所有系数嵌入同时成立。

设 $\Phi_r(X)$ 为第 $r$ 个 cyclotomic 多项式。$r$ 不是素数幂，所以

$$
\Phi_r(1)=1.
\tag{374.14}
$$

可从
$\prod_{d\mid n,\ d>1}\Phi_d(1)=n$
按 $n$ 归纳得到：$\Phi_n(1)$ 在 $n=q^a$ 时为 $q$，在 $n>1$ 非素数幂时为一。这也就是 $1-\zeta_r$ 为代数单位的准确理由。

在 $V_\ell(A_\theta)$ 上，

$$
\Phi_r(\tau)=0.
\tag{374.15}
$$

写

$$
\Phi_r(X)-1=(X-1)Q_r(X),\qquad Q_r(X)\in\mathbb Z[X].
\tag{374.16}
$$

代入 (374.15) 得到

$$
(1-\tau)Q_r(\tau)=1.
\tag{374.17}
$$

同一个等式在任何 $\tau$-稳定的 $\mathbb Z_\ell$ 格上成立，因为
$Q_r$ 是整系数多项式。因此 (374.4) 对所有 $\ell\ne p$ 成立，且已同时覆盖
$\ell=2,3$、$\ell\mid p+1$ 以及所有其他素数。这里没有假设某个 CM 分解 idempotent 在 $\ell$ 处为整。

把同源 $\mathbb Q_\ell$ 表示识别后，(374.15)–(374.17) 也在
$V_\ell(B)$ 及其实际 Tate 格 $T_\ell(B)$ 上成立。因此异于 $p$ 的部分已经与同源代表的选择无关。

## 4. 参考曲线的 $p$ 次挠点惯性

为处理 $\ell=p$，先给 (374.11) 所需的完整局部计算。由于
$p\equiv2\pmod3$，多项式
$(x^3-1)^{(p-1)/2}$ 的 $x^{p-1}$ 系数为零。因此 $E_0$ 的好约化是超奇异的，其形式群高度为二。

取整数形式参数 $T=-x/y$。在 $\mathbb Z_p[[T]]$ 中，

$$
[p](T)=pT+\sum_{2\le i<p^2}c_iT^i+c_{p^2}T^{p^2}
+\sum_{i>p^2}c_iT^i,
\qquad
c_i\in p\mathbb Z_p\ (2\le i<p^2),\quad
c_{p^2}\in\mathbb Z_p^\times.
\tag{374.18}
$$

所有 $E_0[p]$ 点约化到单位元。Newton 多边形或 Weierstrass 准备定理给出对每个非零 $P\in E_0[p]$：

$$
v_p(T(P))=\frac1{p^2-1}.
\tag{374.19}
$$

确实，次数 $1$ 的系数赋值一、次数 $p^2$ 的系数赋值零，而所有中间点都严格位于这条线段上方。

取 $\varpi$ 满足 $\varpi^{p^2-1}=p$。首项映射

$$
P\longmapsto \overline{T(P)/\varpi}
\tag{374.20}
$$

是 $E_0[p]\to\overline{\mathbb F}_p$ 的 $\mathbb F_p$ 线性单射：形式群加法的高次项具有更高赋值，而 (374.19) 保证非零点的首项不为零。由 (374.18)，其像为某个
$a\mathbb F_{p^2}$，其中 $a\ne0$。

惯性在剩余域上平凡，故其在 (374.20) 上的作用为乘以

$$
\omega_2(\sigma)=\overline{\sigma(\varpi)/\varpi}.
\tag{374.21}
$$

这是满射到 $\mathbb F_{p^2}^\times$ 的 niveau-$2$ 基本角色。因此

$$
E_0[p]\otimes_{\mathbb F_p}\overline{\mathbb F}_p
\bigm|_{I_p}
\simeq\omega_2\oplus\omega_2^p.
\tag{374.22}
$$

这一计算在实际整数模型上给出参考格的残余特征，未从 Hodge–Tate 权的数值直接猜测有限层惯性。

## 5. $p$ 扭点、行列式单位与任意同源格

选择 §3 的同一 tame 元素 $\tau$，使
$\omega_2(\tau)$ 为 $\mathbb F_{p^2}^\times$ 的生成元。
在每个 $p$ 进系数嵌入下，$\eta_\theta|_{I_p}$ 的阶为
$r\mid p+1$，故其残余角色为

$$
\overline{\eta_\theta}|_{I_p}
=\omega_2^{(p-1)k}
\tag{374.23}
$$

中的某个 $k\in\mathbb Z/(p+1)\mathbb Z$。有限角色的阶与 $p$ 互素，所以其值是 $p$ 进单位，约化保留准确的阶。

由 (374.13) 与 (374.22)，相应的两个 CM Tate 特征值模 $p$ 为

$$
\omega_2^{\,1+(p-1)k},
\qquad
\omega_2^{\,p-(p-1)k}.
\tag{374.24}
$$

第二个也可写作第一指数的 $p$ 倍，模 $p^2-1$ 取值。若更换 CM 嵌入，则交换这两个角色；若更换系数嵌入，则只改变 $k$。

两个指数都满足

$$
b\equiv1\pmod{p-1}.
\tag{374.25}
$$

由于 $p>2$，它们均不为 $0\pmod{p^2-1}$。所以在所选同一
$\tau$ 上，没有一个残余特征值等于一。

(374.3) 说明 $p$ 在 $F_\theta$ 中全分裂；即使不选择整 idempotent，也可在有理 $p$ 进 Tate 空间扩标量后计算所有上述特征值。由 (374.24)–(374.25)，

$$
\det\!\left(1-\tau\mid V_p(A_\theta)\right)
\in\mathbb Z_p^\times.
\tag{374.26}
$$

该行列式只依赖有理表示。$B$ 与 $A_\theta$ 同源，所以在
$V_p(B)$ 上仍是同一个单位；$\tau$ 在实际 $T_p(B)$ 上为整矩阵。
其伴随矩阵公式于是给 $1-\tau$ 在 $T_p(B)$ 上的整逆，证明
(374.4) 的 $\ell=p$ 部分。

因此无需假定某个模形式商的 $p$ 进投影为整，也无需把残余半单化的描述未经证明地升级为 Tate 格的同构。所有同源格上的结论直接来自行列式单位。

## 6. 扭点消失与准确的全局零像

对每个 $\ell$，

$$
B[\ell^\infty](\overline{\mathbb Q}_p)
=V_\ell(B)/T_\ell(B).
\tag{374.27}
$$

(374.4) 的整逆也作用在此商上。若一个扭点被 $I_p$ 固定，特别地被
$\tau$ 固定，则它被 $1-\tau$ 杀掉，故必为零。这证明
(374.5)，并推出 $B(\mathbb Q_p)_{\mathrm{tors}}=0$。

对在 $\mathbb Q$ 上定义的 $B$，映射
$B(\mathbb Q)\hookrightarrow B(\mathbb Q_p)$ 为单射，所以

$$
B(\mathbb Q)_{\mathrm{tors}}=0.
\tag{374.28}
$$

若 $L(g_\theta,1)\ne0$，R348 已用 Kato 的 CM 适用版本证明
$\operatorname{rank}B(\mathbb Q)=0$。有限生成性与 (374.28)
给 (374.6)。这一步对任意有理同源代表均有效，包括为清除商映射分母而换取的代表。

最后，R348 给出至少一个这样的因子及非零满射
$q:J_{Z_p}\to B$。对每个有理点 $P$，其像
$q([P-c_1])$ 属于 $B(\mathbb Q)$，故 (374.8) 成立。

也可在 $p$ 进对数上准确表述。abelian variety 的局部对数先在充分小的形式邻域定义，再通过乘法延拓到 $B(\mathbb Q_p)$；其核为扭点。由 (374.5)，这里该对数为单射。于是

$$
\log_B q([P-c_1])=0
\quad\text{与}\quad q([P-c_1])=0
\quad\text{等价}.
\tag{374.29}
$$

## 7. 对下一步整数模型问题的准确边界

本稿已经消去 R348 的有理扭点像，不需要先证明 $P$ 与 $c_1$ 在某个模型上有相同约化。所有有理点都落在实际商映射的零纤维。

但若为了构造 $q$ 乘以含 $p$ 的整数，它的微分也会乘以该整数；(374.4) 不会使这一微分自动变为 primitive。即使已知
$v_p(a-1)$ 的高精度，仍须：

- 在实际非分裂 $p$ 水平的整数模型上识别 $P$ 与 $c_1$ 所在的支；
- 把选定商映射和相应微分延拓到该支，并控制可能的同源分母；
- 计算零纤维在该支的首个非零项，或证明所需的余切注入。

这些条件没有由 $A(\mathbb Q)=0$ 自动推出。主统一性目标仍未完成。

## 8. 原文输入

- R348，§§3、5、6、8：实际角色 $\Psi_\theta\kappa_4^{-1}$、其在 $p$ 的有限角色、CM 因子实际出现及非零中心值的秩零结论。
- J.-P. Serre–J. Tate, *Good reduction of abelian varieties*, Ann. of Math. 88 (1968), 492–517，§1 Theorem 1（好约化与异特征 Tate 模未分歧）；§7 Theorems 10–11，printed pp.511–513（CM Hecke 角色与每个 $\ell$ 进实现的代数修正项）。本稿用后一公式保证 $\ell=p$ 时 (374.13) 仍准确；参考形式群的残余惯性另在 §4 自行证明。[原刊记录](https://annals.math.princeton.edu/1968/88-3/p05)；[扫描 PDF](https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf)。
- K. A. Ribet, *Galois representations attached to eigenforms with Nebentypus*, Lecture Notes in Mathematics 601 (1977), 17–51，§4 Proposition (4.4)、Theorem (4.5)，printed pp.39–42：CM 模形式的各个系数位表示限制到同一虚二次域为一对共轭 Hecke 角色。用于明确所讨论的是所有系数嵌入；(374.4) 的格结论由本稿的整多项式逆和行列式直接证明。[作者文献目录](https://math.berkeley.edu/~ribet/Articles/)；DOI 10.1007/BFb0063943。

本文为纯证明；无数值扫描或附加数据文件。
