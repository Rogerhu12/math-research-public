# 椭圆单位的全局指数、局部饱和与变素数 non-Wieferich 条件

日期：2026-11-12。会话：Astra-rank2-Sha / literature_scope。

**状态：证明了一个具体的局部饱和反例和一个系数表示障碍；核查的经典定理没有给出本课题所需的无穷多个 $p$。** 这里不重复一般 $abc$ 条件推论，重点核对椭圆单位文献中“指数”“无穷素数”和“Wieferich”的实际对象。

## 1. 三种条件不能混同

设 $F$ 是固定数域，$C_F\subset\mathcal O_F^\times$ 是有限指数的椭圆单位子群（$F$ 为虚二次域的有限 Abel 扩张时）。记指数为 $I$。对 $p\nmid I$，有
$$
C_F\otimes\mathbb Z_p=\mathcal O_F^\times\otimes\mathbb Z_p.
\tag{1}
$$
这确实对除有限多个以外的 $p$ 成立，但是**全局单位群中的饱和性**。

对 $p$ 的各个完成作对角嵌入，取主单位部分，再取闭包，得到
$$
\overline{C_F}\subset U_{F,p}:=\prod_{v\mid p}(1+p\mathcal O_{F_v})
$$
（下文只讨论 $p>2$ 在 $F$ 中不分歧的情形）。(1) 只说明 $\overline{C_F}$ 等于全局单位像的闭包；它不说明 $U_{F,p}/\overline{C_F}$ 没有 $p$-挠。

第三种条件是把相应局部指数/对数投影到椭圆曲线的 Hecke 特征后，其**指定阶导数非零**。它既不是 (1)，也不是任意一个普通单位的对数非零。

### 1.1 精确的局部阈值

令 $L/\mathbb Q_p$ 无分歧，剩余域有 $q=p^f$ 个元素。对 $u\in\mathcal O_L^\times$，用 Teichmüller 分解定义 $\log_p u$。若 $u$ 非挠，则
$$
v_p(\log_p u)=v_p(u^{q-1}-1).
\tag{2}
$$
这是因为 $q-1$ 是 $p$-adic 单位，而 $\log:1+p\mathcal O_L\to p\mathcal O_L$ 是保持赋值的同构。因此
$$
u\in(\mathcal O_L^\times)^p
\Longleftrightarrow\log_pu\in p^2\mathcal O_L
\Longleftrightarrow u^{q-1}\equiv1\pmod{p^2}.
\tag{3}
$$
有限剩余单位部分的 $p$ 次幂映射是自同构，故它不造成额外条件。局部 non-Wieferich 的阈值是 $v_p(\log_pu)=1$，不是仅仅 $\log_pu\ne0$。固定的非挠代数单位在每个这样的完成中对数都非零，但赋值仍可能大于一。

更一般地，设 $u_1,\ldots,u_r$ 的半局部对数在 $\mathbb Q_p$ 上独立。选定 $\prod_{v\mid p}\mathcal O_{F_v}$ 的 $\mathbb Z_p$ 基，将 $p^{-1}(\log_pu_i)_v$ 写成矩阵。闭包在半局部主单位群中饱和，当且仅当该矩阵模 $p$ 的秩仍为 $r$，也就是某个 $r\times r$ 子式为单位。证明直接用 $\log$ 同构和 Smith 标准形。这是矩阵的秩条件，逐个对数非零不足以代替它。

## 2. 一个真正的椭圆单位例子：全局 $13$-饱和而局部不饱和

取
$$
k=\mathbb Q(i),\quad F=\mathbb Q(\zeta_8)=\mathbb Q(i,\sqrt2),\quad
\epsilon=1+\sqrt2,\quad p=13.
$$
采用 Oukhaba–Viguié 的椭圆单位群 $C_F$。以下断言给出明确反例：

> $C_F\otimes\mathbb Z_{13}=\mathcal O_F^\times\otimes\mathbb Z_{13}$，但其半局部主单位闭包在自己的 $\mathbb Q_{13}$ 线性张成空间内的饱和指数恰为 $13$。

这只否定从全局指数直接推断局部饱和的论证，不是关于 $\Sha$ 的反例。

### 2.1 类数与全局单位

$F$ 的判别式为 $256$。Minkowski 界是
$$
\left(\frac4\pi\right)^2\frac{4!}{4^4}\sqrt{256}
=\frac{24}{\pi^2}<2.44.
$$
每个理想类都有范数至多 $2$ 的理想代表。$2$ 在 $F$ 中全分歧，唯一范数 $2$ 的素理想由 $1-\zeta_8$ 生成，因为 $N_{F/\mathbb Q}(1-\zeta_8)=\Phi_8(1)=2$。故 $h_F=1$。$\mathbb Z[i]$ 为 Euclidean 环，故 $h_k=1$。

$F^+=\mathbb Q(\sqrt2)$ 的单位为 $\{\pm\epsilon^m:m\in\mathbb Z\}$。一个简短证明是：对正的实单位 $u=a+b\sqrt2>1$，其共轭为 $\pm u^{-1}$，从而 $a,b$ 为正整数，故 $u\ge1+\sqrt2$；用 $\epsilon$ 的幂把任意正单位缩放到 $[1,\epsilon)$ 即得结论。

对任意 $u\in\mathcal O_F^\times$，所有复嵌入下 $u/\bar u$ 的绝对值均为 $1$，由 Kronecker 定理它为单位根。因此
$$
u^2=(u/\bar u)N_{F/F^+}(u)\in\mu_F\mathcal O_{F^+}^\times.
$$
所以 $\mathcal O_F^\times/(\mu_F\langle\epsilon\rangle)$ 被 $2$ 杀，特别地
$$
\mathcal O_F^\times\otimes\mathbb Z_{13}
=\mathbb Z_{13}\epsilon
$$
（乘法群在张量后用加法模记号）。

### 2.2 椭圆单位指数确实不含 $13$

Oukhaba–Viguié，*On the Gras Conjecture for Imaginary Quadratic Fields*，Canadian Mathematical Bulletin 56 (2013), 148–160，引言式 (1.2) 对 $g=[F:k]$ 给出
$$
[\mathbb Z[g^{-1}]\otimes\mathcal O_F^\times:
\mathbb Z[g^{-1}]\otimes C_F]
=\frac{\#(\mathbb Z[g^{-1}]\otimes\mathrm{Cl}(F))}
{\#(\mathbb Z[g^{-1}]\otimes\mathrm{Cl}(k))}.
\tag{4}
$$
此处 $g=2$ 且两类数都为 $1$，所以 $13$-adic 张量后指数为 $1$。这正是 (1) 在本例的结论。

[已读取的期刊原文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0148F81E2EC11C708E2769B9AF48720C/S000843950000062Xa.pdf/on-the-gras-conjecture-for-imaginary-quadratic-fields.pdf)。该文引言还精确说明 Rubin 原先结果要求 $p\nmid w_k[F:k]$；这里 $13\nmid8$。本笔记使用并直接核对的是 (4)，没有声称重新证明 Rubin 的 Euler-system 定理。

### 2.3 局部饱和缺陷的精确计算

$13\equiv1\pmod4$，但 $2$ 在 $\mathbb F_{13}$ 中不是平方。所以 $F$ 的两处 $13$ 完成都为 $\mathbb Q_{13}(\sqrt2)$，是无分歧二次扩张。直接计算
$$
\epsilon^7=239+169\sqrt2,
\qquad
\epsilon^{14}=114243+80782\sqrt2.
$$
于是
$$
\epsilon^{14}+1
=13^2(4\cdot13^2+478\sqrt2).
$$
括号模 $13$ 为 $10\sqrt2\ne0$。在两个完成中因此都有
$$
v_{13}(\epsilon^{14}+1)=2,
\qquad
v_{13}(\log_{13}\epsilon)=2,
\tag{5}
$$
后一个等式由 $-\epsilon^{14}\in1+13^2\mathcal O$、$\log(-1)=0$ 和 $13\nmid14$ 得到。

令 $x=(\log_{13}\epsilon)_v$。半局部闭包在对数下是 $M=\mathbb Z_{13}x\subset\prod_{v\mid13}13\mathcal O_{F_v}$。由 (5)，$x/13$ 属于右边，且在其中是一个 primitive 向量；它不属于 $M$，因为 $x\ne0$。于是
$$
\operatorname{Sat}(M)=\mathbb Z_{13}(x/13),
\qquad
\operatorname{Sat}(M)/M\simeq\mathbb Z/13\mathbb Z.
$$
这完成了反例的证明。算术恒等式另外用整数递推 $(a,b)\mapsto(a+2b,a+b)$ 核对；没有数值精度假设。

## 3. Coates–Wiles 1978 的“无穷多个素数”具体证明了什么

Coates–Wiles，*On $p$-adic $L$-functions and elliptic units*，J. Austral. Math. Soc. A 26 (1978), 1–25，Theorem 1 的条件是：$K$ 类数一、$E/K$ 有全 CM；$p$ 避开 $2,3$ 与坏约化，$p$ split，且 $p$ 对 $E$ non-anomalous。

固定这样的 $p$，在 $F_n=K(E[\mathfrak p^{n+1}])$ 的塔中，局部主单位模椭圆单位闭包的第 $i$ tame 分量逆极限同构于
$$
Y_\infty^{(i)}\simeq\Lambda/(G_i(T)),\qquad i\not\equiv0\pmod{p-1},
$$
其中 $G_i$ 由临界 Hecke 特值插值给出；还有有限层控制同构。Theorem 1 后确实说满足上述三个素数条件的 $p$ 有无穷多个。

但这没有说 $G_i$ 是单位，也没有说其在某个中心具有恰好指定阶的零。它给出商的结构和插值函数的对应。$F_n$ 与单位系统本身均依赖 $p$。

对本题 E17，$(0,0)$ 是非零有理 $2$-挠点，因此所有好奇素数处 $a_p$ 为偶数。对 $p\ge7$，Hasse 界与 $p-1>2\sqrt p$ 说明 $a_p\equiv1\pmod p$ 只能是 $a_p=1$，与偶数性矛盾。因此 E17 的这些 $p$ 自动 non-anomalous；这并没有解决 R9 所需的 $T^2$ 首项非零。

[已读取的原文，Theorem 1 及其后段落](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4469043119AAC5B6C5D298A18D059696/S1446788700011459a.pdf/on_padic_lfunctions_and_elliptic_units.pdf)。本次核对了引言、定理与插值对象；没有重新独立验证该文全部证明。

## 4. 最接近的 CM non-Wieferich 判据：基数与分量都要核对

Lozano–Robledo 2010，Theorem 1.3 / Corollary 6.9，设 $K$ 类数一、$D_K\ne-3,-4$，$p$ split。取 $\mathfrak p=(\pi_p)$，$\mathfrak p'=(\pi_p')$。该文的精确等价是
$$
v_{\mathfrak p}((\pi_p')^{p-1}-1)=1
\Longleftrightarrow BH_p^{\,p-2}\in\mathbb Z_p^\times
\Longleftrightarrow G_{(1,1)}\text{ 为单位幂级数}.
\tag{6}
$$
§6.2 中的 $M$ 是左边赋值减一。Theorem 6.7 的相关分支是 $(k,-j)\equiv(1,1)\pmod{p-1}$，在 (6) 中取 $(k,j)=(p,p-2)$。

这里有三个具体限制：

1. $\pi_p'$ 是随 $p$ 改变的素理想生成元，不是一个固定椭圆单位；固定基数的 non-Wieferich 结论不能直接套用。
2. 这是 $(1,1)$ 分量，不能改名为本题 $\psi$ 权重的 $(1,0)$ 分量；固定有限 twists 也不能任意改变其 infinity type。
3. 文中对 split 素数给出判据及有限计算，没有给出满足 (6) 的无穷素数定理；其 inert 的“除有限多个外”结果是另一种 deformation/adjoint 对象，已在 `2026-11-12-inert-deformation-scope.md` 审核。

[已核对的作者原文](https://production.wordpress.uconn.edu/alozano/wp-content/uploads/sites/490/2014/01/lozano_robledo_BH.pdf)。$D_K=-4$ 明确被排除，故 (6) 不能作为该文定理直接用于 E17。

Gold 的 cyclotomic $\lambda$ 判据将类似的变基数条件写成：当 $p>3$、$p\nmid h_K$、$p=\mathfrak p\bar{\mathfrak p}$ 且 $\mathfrak p^{h_K}=(\alpha_p)$ 时，
$$
\lambda_p(K)>1\Longleftrightarrow
\alpha_p^{p-1}\equiv1\pmod{\bar{\mathfrak p}^{2}}.
\tag{7}
$$
Stokes，*On CM Elliptic Curves and the Cyclotomic $\lambda$-Invariants of Imaginary Quadratic Fields*，Theorem 1.4 重述 (7)，Theorem 1.6 又把它写成某个约化 CM 曲线在 $\mathbb F_{p^{p-1}}$ 上的点数被 $p^2$ 整除。**这个有限域是 $\mathbb F_{p^{p-1}}$，不是 $\mathbb F_p$**，故不能以 Hasse 界直接排除 $p^2$ 整除。

[已读取的 Stokes 作者版本](https://arxiv.org/pdf/2302.09594)。这里只核对其定理范围；本次没有读取 Gold 原始证明，也没有由 Stokes 的“$\lambda>1$ 无穷性仍开放”反向推断“$\lambda=1$ 无穷性”的状态。所查论文未提供本题可用的后者定理。

## 5. 固定虚二次基域 $p$-rational 不会自动控制曲线特征

固定虚二次域 $K$ 的全局单位秩为零。对充分大的不分歧 $p$，局部主单位没有 $p$ 次单位根，且 $p\nmid h_K$；类域论因而使其最大 Abel pro-$p$ 的 $p$-分歧扩张 Galois 群为自由 $\mathbb Z_p$ 模。这是一种真正的“所有充分大 $p$”结论，但对象是未扭曲的基域 Abel 扩张。

进入固定正单位秩扩域 $F$ 后，即使 $p\nmid h_F$、椭圆单位指数也素于 $p$，仍有 §2 的局部 regulator 障碍。Gras 2019，§1 的 exact sequence 将局部商中的挠分解为局部单位根项及 normalized $p$-adic regulator；§7 / Conjecture 7.1 把其跨 $p$ 单位性视为猜想/启发式，而非由全局单位指数得到的定理。

[Gras 期刊原文](https://www.numdam.org/item/10.5802/pmb.35.pdf)。作为近期状态交叉核对，Hofmann–Johnston 2026 的算法稿 §3.1、Conjecture 3.5 和 §8 仍明确将固定数域对除有限多个外的 $p$ 为 $p$-rational 当作 Gras 猜想；其新内容是给定 $p$ 的算法，而非无穷素数非零定理。[原文](https://arxiv.org/html/2609.15190v1)。本笔记不依赖该新稿的未独立复核定理。

### 5.1 固定域普通单位不能直接投影成曲线的 Tate 特征

还存在一个简单的系数表示障碍。令 $p$ 是 E17 的好 split 素数，$V_{\mathfrak p}$ 为 $E[\mathfrak p^\infty]$ 对应的一维 $\mathbb Q_p$ 表示。对任意固定有限扩张 $F/K$，
$$
\operatorname{Hom}_{G_K}
\left(\operatorname{Ind}_{G_F}^{G_K}\mathbb Q_p(1),V_{\mathfrak p}\right)=0.
\tag{8}
$$
**证明。** 由 Frobenius reciprocity，左边等于 $\operatorname{Hom}_{G_F}(\mathbb Q_p(1),V_{\mathfrak p})$。在 $\mathfrak p'$ 上方的一处惯性上，$V_{\mathfrak p}$ 是 ordinary CM Tate 模的 étale 分量，故不分歧；$\mathbb Q_p(1)$ 的 cyclotomic 特征在任意有限局部扩张的惯性上仍有无限像。因此两一维特征不相等，Hom 为零。交换两个素理想，同理得到另一 CM 分量的版本。

普通单位的 Kummer 类属于 $H^1(F,\mathbb Q_p(1))$。有限 Galois 扩张中的角色投影本身不能消除 (8) 的 infinity-type / 惯性不匹配；需要依赖 $p$ 的无限塔、扭曲和 moment 映射。这解释了为什么“固定椭圆单位的对数永不为零”不能直接给出本题的 derived elliptic-unit 类非零。(8) 只排除这一直接的系数映射，不排除更深的对应或额外几何构造。

## 6. 到主目标仍缺少的具体命题

本次核对中真正无条件的跨 $p$ 结论，是固定有限指数带来的全局饱和、固定虚二次基域的低维类域论、以及 Coates–Wiles 的无穷多个好 split non-anomalous 素数。它们没有推出 E17 在无穷多个 $p$ 的二阶首项或 derived 类非零。

若继续这条路线，需要直接处理曲线的正确 Hecke 分量，并证明其派生椭圆单位类在无穷多个 $p$ 非零；若改求局部 $p$-单位性，则必须同时证明实际需要的归一化 regulator / 矩阵子式，而不能以全局椭圆单位指数素于 $p$ 代替。§2 的具体例子已经证明这种替代在相当小的 CM 扩域中也会失败。
