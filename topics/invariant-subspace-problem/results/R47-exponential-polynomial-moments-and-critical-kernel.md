# R47：指数多项式矩分离与原临界核的严格排除类

日期：2026-11-12（UTC+8）。会话：Astra-ISP-0c017065。

**状态：已证明的中间结论。** 本条将 R46 推广到有限指数多项式，允许两端使用任意两个不同的平方可和标量 Rademacher 级数及有限前缀系数。原临界向量 $f_*=D1$ 属于新类，因而可以排除 $\ker D$ 中整个新类的非零向量。没有证明一般核向量属于该类，没有决定 $\ker D$，也没有解决完整 Hilbert 不变子空间问题。

依赖：R9/R12 的有限链及高位估计；R16 的单个无限乘积和任意有限前缀循环性；R24 的复对称性；R40 的连续向量对矩分离；R43 的临界算子定义。本条给出全部新的反集中、有限维函数演算和归纳步骤。

## 1. 向量类与结论

仍令
$$
H=L^2(\mathbb Z_2,\mu),\qquad
(Af)(y)=w(y)f(y-1),\qquad
w(y)=a_{v_2(y)}\quad(y\ne0),\quad w(0)=0,
$$
$$
a_j=e^{-L_j},\qquad
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
$$
写 $\chi_j(y)=(-1)^{b_j(y)}$，$\mathscr C_m$ 为低 $m$ 位柱函数空间。使用复双线性型
$$
B(f,g)=\int f(y)g(-1-y)\,d\mu(y)
=\langle f,Cg\rangle,\qquad
Cg(y)=\overline{g(-1-y)}.
$$
内积在第一变量线性。R24 给出
$$B(Af,g)=B(f,Ag).\tag{1.1}$$

取任意
$$
X=x_*+\sum_{k\ge m}x_k\chi_k,\qquad
Y=y_*+\sum_{k\ge m}y_k\chi_k,\qquad x,y\in\ell^2,
\tag{1.2}
$$
及有限指数多项式
$$
F(s)=\sum_{\alpha\in\Lambda}P_\alpha(s)e^{\alpha s},\qquad
G(t)=\sum_{\beta\in\Gamma}Q_\beta(t)e^{\beta t},
\tag{1.3}
$$
其中 $\Lambda,\Gamma$ 有限，$P_\alpha,Q_\beta$ 的系数属于 $\mathscr C_m$。求导只针对形式标量变量。

**定理 1.1。** $F(X),G(Y)\in H$。如果
$$B(A^nF(X),G(Y))=0\qquad(n\ge0),\tag{1.4}$$
则 $F(X)=0$ 或 $G(Y)=0$。

取全部 $m,X,F$ 得到向量类 $\mathscr E$。有限个低位项可以吸收进柱函数系数，故两个成员总能使用共同的 $m$。反射共轭把 $F(X)$ 送成以 $\overline X$ 为变量的另一有限指数多项式，系数仍为有限柱函数。因此 $C\mathscr E=\mathscr E$，也有
$$
f,g\in\mathscr E,\quad
\langle A^nf,g\rangle=0\ (n\ge0)
\quad\Longrightarrow\quad f=0\text{ 或 }g=0.
\tag{1.5}
$$
这只分离两端同时在 $\mathscr E$ 中的配对，不声称每个非零成员对任意 $H$ 中向量均矩分离。

## 2. 可积性与无原子性

### 2.1 指数多项式可积

对有限实 Rademacher 和 $Z=\sum d_k\chi_k$，独立性和 $\cosh u\le e^{u^2/2}$ 给
$$
\mathbb E e^{tZ}\le
\exp\left(\frac{t^2}{2}\sum_kd_k^2\right).
\tag{2.1}
$$
Markov 不等式及尾积分公式遂给每个有限 $q\ge1$ 的估计
$$\|Z\|_q\le K_q\|d\|_2.\tag{2.2}$$
复系数分别处理实部、虚部。对尾项使用 (2.2)，有限和在每个有限 $L^q$ 中收敛。

$\operatorname{Re}(\lambda X)$ 是常数加实 Rademacher 级数，(2.1) 和 Fatou 引理保证其任意实指数矩有限。因此 $e^{\lambda X}\in L^q$ 对所有有限 $q$ 成立；Hölder 不等式再给
$$X^r e^{\lambda X}\in L^q\qquad(r\ge0,\ q<\infty).\tag{2.3}$$
有限和代入也在这些 $L^q$ 中收敛。对指数用
$$
|e^u-e^v|\le |u-v|
\bigl(e^{\operatorname{Re}u}+e^{\operatorname{Re}v}\bigr)
$$
和 Hölder，不同有限和的指数矩由 (2.1) 一致控制；多项式因子再用差分分解。这证明全部代入、导数代入和后文积分合法。

### 2.2 无限非零系数的分布没有原子

**引理 2.1。** 若 $(x_k)$ 有无限多个非零项，则 $X$ 的分布没有原子。

**证明。** 选任意 $N$ 个非零系数，选一个实投影方向使这 $N$ 个复系数的投影均非零。翻转 Rademacher 符号不改变分布，可以假定这些投影都正。

产生同一实和值的正号指标集合形成反链：严格包含会严格增大正权之和。一个 $N$ 元集合上的反链至多有 $\binom N{\lfloor N/2\rfloor}$ 个成员。所需 Sperner 界可自证：随机排列产生的完整子集链至多经过反链的一个成员，经过固定 $r$ 元集合的概率为 $\binom Nr^{-1}$，故
$$
\sum_{S\text{ 属于反链}}\binom N{|S|}^{-1}\le1.
$$
这推出上述基数界。

条件于其余位，事件 $X=z$ 的概率至多
$$2^{-N}\binom N{\lfloor N/2\rfloor},$$
并且这个界与余项及 $z$ 无关。积分后仍成立。该界趋零，因为
$$
4^{-r}\binom{2r}r
=\prod_{j=1}^r\left(1-\frac1{2j}\right)\longrightarrow0
$$
且奇数情形不大于相邻偶数情形。让 $N\to\infty$ 得证。

非零整函数的零集是可数离散集。因此，无原子性的直接推论是
$$
H\text{ 为非零标量整函数}
\quad\Longrightarrow\quad
\mathbb P\{H(X)=0\}=0.
\tag{2.4}
$$
尾级数与低 $m$ 位独立，所以 (2.4) 可逐个前缀使用。后文非零形式指数多项式的代入，不会因此变成零向量。

## 3. 复杂度与单指数基例

合并相同指数、删去零项，定义
$$
\kappa(F)=\sum_{\alpha\in\Lambda}(\deg P_\alpha+1).
\tag{3.1}
$$
次数指最高非零柱系数的次数。不同指数的指数多项式线性无关：施加消去其他指数的常系数微分算子后，可把任一非零指数项化为非零多项式乘指数。逐个前缀使用此事实即可。

若 $\alpha\in\Lambda$，则
$$
F_1=(\partial-\alpha)F,\qquad
\kappa(F_1)=\kappa(F)-1,
\tag{3.2}
$$
其中零函数的复杂度记零。对应 $\alpha$ 的次数降一或整项消失；其余项的最高系数乘非零数 $\lambda-\alpha$，次数保持。

若 $\kappa(F)\ge2$，则
$$
(\partial-\nu)F\ne0\qquad(\nu\in\mathbb C).
\tag{3.3}
$$
否则逐个前缀解一阶方程，会得到 $F(s)=h e^{\nu s}$，复杂度只有一。对无原子分布的 $X$，(2.4) 保证上述非零性在 $H$ 中同样成立。

当 $\kappa(F)=1$，$F(X)=h e^{\alpha X}$，其中 $0\ne h\in\mathscr C_m$。这是 R16 的循环向量。确切地说，
$$e^{\alpha X}=e^{\alpha x_*}\prod_{k\ge m}e^{\alpha x_k\chi_k}.\tag{3.4}$$
§2.1 给有限乘积的非零 $L^2$ 极限。局部平方范数为
$$\cosh(2\operatorname{Re}(\alpha x_k)),$$
所以局部范数乘积收敛到有限非零数。归一化局部因子形成 R16 的收敛无限乘积；任意非零有限前缀 $h$ 仍循环。因此
$$
\kappa(F)=1,\ F(X)\ne0
\quad\Longrightarrow\quad F(X)\text{ 对 }A\text{ 循环}.
\tag{3.5}
$$

若 $X$ 只有有限多个非零系数，则任意 $F(X)$ 都是有限柱函数，非零时由 R11 循环。这是另一直接基例，不必对离散分布使用 (2.4)。

## 4. 高位矩的有限维函数演算

令 $\mathcal V_F$ 为下列形式函数张成的有限维空间：
$$
h\,s^r e^{\alpha s},\qquad
h\in\mathscr C_m,\quad
\alpha\in\Lambda,\quad0\le r\le\deg P_\alpha.
$$
对 $G$ 类似定义 $\mathcal V_G$，取 $\mathcal V=\mathcal V_F\otimes\mathcal V_G$。求导 $\partial_s,\partial_t$ 在 $\mathcal V$ 上是交换的有限矩阵，不必幂零。对有界 $Q$，定义
$$
\mathscr B_Q(U\otimes V)=B(Q\,U(X),V(Y)).
\tag{4.1}
$$
它是有限维空间上的连续泛函，见 §2。

对充分小的复参数 $u,v$，定义
$$
\mathcal H_{u,v}
=\exp(u\partial_s+v\partial_t)
\bigl[\cosh(u\partial_s-v\partial_t)\bigr]^{-1}.
\tag{4.2}
$$
逆合法，因为 $\cosh$ 矩阵在原点为恒等。

记 $E_k=e_{10}$ 为第 $k$ 位矩阵单位。若 $Q$ 不作用第 $k$ 位，则充分大的 $k\ge m$ 满足
$$
2B(E_kQF(X),G(Y))
=\mathscr B_Q\bigl(\mathcal H_{x_k,y_k}(F\otimes G)\bigr).
\tag{4.3}
$$

**证明。** 写 $X_0=X-x_k\chi_k$、$Y_0=Y-y_k\chi_k$，把其余位上的双线性积分记为 $\Lambda$。在第 $k$ 位取 $\chi_k=\varepsilon$ 时，第一个位置增加 $\varepsilon x_k$，反射后的第二个位置增加 $-\varepsilon y_k$。因此
$$
\mathscr B_Q=\Lambda\cosh(x_k\partial_s-y_k\partial_t).
$$
$E_k$ 取第一个位置的输入位为零、输出位为一；反射后第二位置的位也为零，所以
$$
2B(E_kQF(X),G(Y))
=\Lambda\exp(x_k\partial_s+y_k\partial_t)(F\otimes G).
$$
两个矩阵函数交换，消去 $\Lambda$ 得 (4.3)。有限维翻译恒等式精确成立，§2 确保代入和积分合法。证毕。

在固定有限维空间中，解析展开给
$$
\mathcal H_{u,v}
=I+u\partial_s+v\partial_t
+2uv\partial_s\partial_t+O((|u|+|v|)^3).
\tag{4.4}
$$
纯平方项为零，因为
$$
\frac12(u\partial_s+v\partial_t)^2
-\frac12(u\partial_s-v\partial_t)^2
=2uv\partial_s\partial_t.
$$
余项是矩阵范数估计，常数不依赖高位指标 $k$。

## 5. 两个标量参数的约束

假设 $f=F(X),g=G(Y)$ 非零且满足 (1.4)。对固定 $r\ge0$，记
$$
C_r=B(A^rF'(X),g),\quad
D_r=B(A^rf,G'(Y)),\quad
E_r=B(A^rF'(X),G'(Y)).
\tag{5.1}
$$
令 $\rho_k=|x_k|+|y_k|$。R9/R12 的有限链 $A_k$ 和 $N_k=A^{2^k}/\|A^{2^k}\|$ 满足
$$
\|A^r-A_k^r\|\le r a_k,\qquad
\|N_k-E_k\|=\eta_k=\frac{a_{k+1}}{a_k},\qquad
\eta_k=o(a_k).
\tag{5.2}
$$
$A_k^r$ 不作用于第 $k$ 位。由零矩假设，$B(N_kA^rf,g)=0$。在 (4.3) 中取 $Q=A_k^r$，再用 (5.2) 换回 $A^r$。固定有限维空间所有基函数代入后的 $L^2$ 范数有限，$\mathcal H_{x_k,y_k}$ 最终一致有界，所以全部替换误差为 $O_r(a_k)$。零阶矩消失，(4.4) 给
$$
\boxed{x_kC_r+y_kD_r+2x_ky_kE_r
=O_r(\rho_k^3+a_k).}
\tag{5.3}
$$

## 6. 复杂度归纳排除二阶退化

对 $\kappa(F)+\kappa(G)$ 归纳。任一复杂度为一，或任一级数仅有有限多个非零系数时，§3 和 (1.1) 已排除非零零矩对。

因此假定两复杂度至少二，两个分布无原子，定理对更低总复杂度成立。选 $\alpha\in\Lambda,\beta\in\Gamma$，令
$$f_1=F'(X)-\alpha f,\qquad g_1=G'(Y)-\beta g.$$
它们非零，复杂度分别降低一。全部 $B(A^rf,g)$ 为零，故
$$C_r=B(A^rf_1,g),\qquad D_r=B(A^rf,g_1).\tag{6.1}$$
归纳假设使序列 $C,D$ 都非零。

若 $C,D$ 线性无关，取两个固定测试使其 $2\times2$ 矩阵可逆。(5.3) 给
$$\rho_k\le K(\rho_k^2+a_k).$$
由 $\rho_k\to0$ 吸收二次项，得到 $\rho_k=O(a_k)$。

若 $C=\lambda D$，则 $\lambda\ne0$。此时 $D,E$ 必线性无关。否则 $E=\mu D$，而
$$
B(A^rf_1,g_1)
=E_r-\alpha D_r-\beta C_r
=(\mu-\alpha-\beta\lambda)D_r.
$$
记 $\nu=\mu-\alpha-\beta\lambda$，得到
$$B(A^r(f_1-\nu f),g_1)=0\qquad(r\ge0).\tag{6.2}$$
$f_1-\nu f=(\partial-\alpha-\nu)F(X)$ 由 (3.3) 和无原子性非零；其复杂度至多 $\kappa(F)$，而 $g_1$ 的复杂度低一。这与归纳假设矛盾。

于是可取两个固定有限坐标线性组合 $\ell_0,\ell_1$，满足
$$\ell_0(D)=1,\qquad\ell_1(D)=0,\qquad\ell_1(E)=1.$$
对 (5.3) 应用它们，置 $e_0=\ell_0(E)$：
$$
\lambda x_k+y_k+2e_0x_ky_k=O(\rho_k^3+a_k),
\qquad
2x_ky_k=O(\rho_k^3+a_k).
\tag{6.3}
$$
第一式给 $y_k=-\lambda x_k+O(\rho_k^2+a_k)$，故最终
$$\rho_k\le K(|x_k|+a_k).$$
结合第二式和 $|x_k|\le\rho_k$，又有
$$|\lambda||x_k|^2\le K(\rho_k^3+a_k).$$
平方前式并代入后式，得到 $\rho_k^2\le K(\rho_k^3+a_k)$。再次吸收三次项：
$$\boxed{|x_k|+|y_k|=O(a_k^{1/2}).}\tag{6.4}$$

两种情形都推出 $x,y\in\ell^1$，所以 $X,Y$ 连续，进而 $f,g$ 连续。R40 排除非零连续对的全部矩消失，归纳完成。

本证明没有把非零多变量解析函数的零点擅自视为孤立；(6.3)–(6.4) 是两个实际测试给出的孤立性估计。

## 7. 原临界核的应用

沿用 R43 的
$$
r_j=\frac{1-(j+2)^{-2}}{1+(j+2)^{-2}},\quad
Q=\prod_j(I+r_jN_j)(I+N_j)^{-1},\quad D=I-Q,
$$
$$f_*=D1=1-\prod_jr_j^{b_j}.$$
由于 $\sum_j|\log r_j|<\infty$，置
$$
X_*=\sum_jb_j\log r_j
=\frac12\sum_j\log r_j-\frac12\sum_j(\log r_j)\chi_j.
\tag{7.1}
$$
它是平方可和（事实上绝对可和）的标量级数，且 $f_*=1-e^{X_*}\in\mathscr E$、$f_*\ne0$。

若 $v\in\ker D$，由 $D$ 的 $B$-对称性及与 $A$ 交换，
$$
B(A^nf_*,v)=B(A^nD1,v)=B(A^n1,Dv)=0\qquad(n\ge0).
$$
定理 1.1 因而给
$$\boxed{\ker D\cap\mathscr E=\{0\}.}\tag{7.2}$$

这排除了 R43 连续性结论未直接覆盖的非连续标量指数多项式。例如
$$
Y=\sum_{j\ge0}\frac{\chi_j}{j+1},\qquad
P(Y)e^{\lambda Y}+Q(Y)e^{\mu Y}
$$
的任意非零成员都不在 $\ker D$ 中，允许有限前缀柱函数系数。

尚未处理的是 $\mathscr E$ 外的一般 $L^2$ 向量。即使 $\mathscr E$ 含有稠密核心，也不能取闭包将 (7.2) 推成 $\ker D=0$；原临界核和完整 ISP 继续保持未解决状态。

