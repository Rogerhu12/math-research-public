# 非分裂 Cartan 的尖点、Runge 条件与覆盖提升障碍

日期：2026-11-12。会话：serre-uniformity-astra；子任务 geometric_route。

**状态：本文的有限群/尖点命题有完整证明；它们排除一类直接照搬 Runge 方法的路线，不证明 Serre 一致性，也不否定其它高度方法。** 已有文献中的标准模曲线尖点描述明确列为输入。没有将文献核查或路线障碍算作主问题完成。

## 1. 原始文献与精确适用范围

1. B. Mazur, *Rational isogenies of prime degree*（附 D. Goldfeld 的 appendix），Invent. Math. 44 (1978), 129–162，Theorem 1 与开篇有理点表：有理素数次同源的可能次数为 $2,3,5,7,11,13,17,19,37,43,67,163$；其中超过 $37$ 的条目来自 CM。原文：<https://www.math.columbia.edu/~goldfeld/Mazur-Goldfeld1978.pdf>。
2. Y. Bilu–P. Parent–M. Rebolledo, *Rational points on $X_0^+(p^r)$*, Ann. Inst. Fourier 63 (2013), 957–984，Theorem 1.1：$p\ge11$, $p\ne13$, $r>1$ 时有理点只有尖点和 CM 点。$X_0^+(p^2)\cong X_{\rm sp}^+(p)$，不应将此同构误用到非分裂曲线。正式条目：<https://aif.centre-mersenne.org/articles/10.5802/aif.2781/>；作者稿：<https://lmbp.uca.fr/~rebolledo/page-fichiers/12_bpr_rational_points.pdf>。
3. D. Zywina, *On the possible images of the mod $\ell$ representations associated to elliptic curves over $\mathbb Q$*, Proposition 1.13：排除明确的 $17,37$ 同源例外后，$\ell\ge17$ 的非满像只剩整个非分裂正规化子，或 $\ell\equiv2\pmod3$ 时的指数三子群。作者稿：<https://pi.math.cornell.edu/~zywina/papers/PossibleImages/PossibleImages.pdf>。其论证也由下一条 Appendix B 完整重述。
4. S. Le Fourn–P. Lemos, *Residual Galois representations of elliptic curves with image contained in the normaliser of a non-split Cartan*, Algebra Number Theory 15 (2021), 747–771。本文使用 Lemma 2.1、Corollaries 2.2–2.3 的尖点描述；Remark 1.6 说明非分裂正规化子 Jacobian 的有限 Mordell–Weil 商障碍是 **BSD 所预言的**，不能删去条件；Lemma 6.3 证明指数三子群曲线有两个有理 Galois 尖点轨道。原文：<https://arxiv.org/pdf/2002.02714>。
5. Y. Bilu–P. Parent, *Runge's method and modular curves*, IMRN 2011, 1997–2027，Theorem 1.2 的条件是 $c_K>|S|$，其中 $c_K$ 为尖点在 $K$ 上的 Galois 轨道数，$S$ 包含全部无穷位。原文：<https://arxiv.org/pdf/0907.3306>。
6. A. Bajolet–M. Sha, *Bounding the $j$-invariant of integral points on $X_{\rm ns}^+(p)$*, Proc. AMS 142 (2014)，§1 指出尖点全共轭、通常 Runge 条件失败。Theorem 1.2 给出整数点的上界
   $$\log|j(P)|<41993\cdot13^p p^{2p+7.5}(\log p)^2.$$
   该界增长极快，且只适用于整数 $j$；它与线性级别的同源下界并不矛盾。原文：<https://arxiv.org/pdf/1203.1187>。
7. D. Zywina, *Improved bounds for integral points on modular curves using Runge's method*, arXiv:2403.14904，Theorem 1.1 将一般界改到 $h(j)\le N^{12}\log N$，但仍明确保留相同的 $c_K>|S|$ 假设；不能因为界变好就将它套到不满足条件的非分裂情形。<https://arxiv.org/html/2403.14904v1>。

关于 Furio–Lombardo 排除指数三情形以及截至检索日的更近文献，见同日 literature-nonsplit 笔记；本笔记不重复该核查。

## 2. 记号与所用标准尖点事实

固定奇素数 $p$，把 $V=\mathbb F_p^2$ 识别为 $\mathbb F_{p^2}$。对 $a\in\mathbb F_{p^2}^{\times}$，令 $m_a(x)=ax$，令 $w(x)=x^p$。记
$$C=\{m_a:a\in\mathbb F_{p^2}^{\times}\},\qquad
N=C\rtimes\langle w\rangle.$$
于是 $C$ 是非分裂 Cartan，$N$ 是其正规化子，且
$$\det m_a=\operatorname N(a),\qquad \det w=-1.$$
令 $M=(V\setminus\{0\})/\{\pm1\}$。

对含 $-I$ 且行列式满的 $H\le N$，模曲线 $X_H$ 是定义在 $\mathbb Q$ 上的光滑射影几何连通曲线。上述文献 4 的 Lemma 2.1 与 Corollaries 2.2–2.3 给出：

- 几何尖点集合为 $(H\cap\mathrm{SL}_2)\backslash M$；
- 所有尖点都在 $\mathbb Q(\zeta_p)$ 上有定义；
- $\mathbb Q$ 上的 Galois 尖点轨道集合为 $H\backslash M$。

下面还要用其相对版本。设数域 $F$ 的模 $p$ 圆分特征像为
$$D_F=\chi_p(G_F)\le\mathbb F_p^\times,$$
并令 $H(D_F)=H\cap\det^{-1}(D_F)$。则
$$\boxed{c_F(X_H)=|H(D_F)\backslash M|.}\tag{2.1}$$
这不是另一个外部假设：从 Lemma 2.1 的作用公式直接得到。具体地，对 $\lambda\in D_F$ 选择 $\gamma_\lambda\in H$ 满足 $\det\gamma_\lambda=\lambda$。在上述几何尖点商集上，圆分作用由 $\lambda\gamma_\lambda^{-1}$ 作用于向量实现。不能仅凭行列式就断言这个矩阵在 $H$ 中。这里使用 $H\le N$：对乘法型元素 $m_a$，有 $\operatorname{adj}(m_a)=m_{a^p}=m_a^p\in H$；对半线性元素 $g$，有 $\operatorname{tr}(g)=0$，故 $\operatorname{adj}(g)=-g\in H$。因此对所有 $g\in H$ 都有 $\operatorname{adj}(g)\in H$，且 $\operatorname{adj}$ 是对合。于是 $\lambda\gamma_\lambda^{-1}=\operatorname{adj}(\gamma_\lambda)$ 确实在 $H$ 中，行列式是 $\lambda$；这些矩阵随 $\lambda\in D_F$ 恰好遍历 $H(D_F)/(H\cap\mathrm{SL}_2)$ 的陪集。再除以原有的 $H\cap\mathrm{SL}_2$ 作用，便是 (2.1)。这一推导只在已写明的非分裂正规化子子群范围内使用，不把它未经检查地推广到任意 $\mathrm{GL}_2$ 子群。

## 3. 非分裂正规化子的单一尖点轨道

### 命题 G1（尖点域与有理模单位）

$X_N=X_{\rm ns}^+(p)$ 有 $(p-1)/2$ 个几何尖点；每个尖点的剩余域都是
$$L_0=\mathbb Q(\zeta_p)^+,$$
且尖点在 $\mathbb Q$ 上形成一个 Galois 轨道。若 $u\in\mathbb Q(X_N)^\times$ 的零点和极点都仅在尖点，则 $u\in\mathbb Q^\times$。

**证明。** $C$ 在 $V\setminus\{0\}$ 上传递，所以 $N\backslash M$ 只有一个元素。为了同时确定几何尖点数和域，考察 $N\cap\mathrm{SL}_2$ 的作用。其乘法型元素满足 $\operatorname N(a)=1$，保持向量范数；其半线性元素 $m_aw$ 满足 $\operatorname N(a)=-1$，把范数 $t$ 变为 $-t$。反过来，同范数的非零向量由范数一的乘法型元素相连，范数相反的向量也由行列式一的半线性元素相连。因此几何尖点由
$$\mathbb F_p^\times/\{\pm1\}$$
标记。圆分元素 $\lambda$ 在这个标记上乘以 $\lambda$：可在 §2 的公式中取 $\gamma_\lambda=m_a$, $\operatorname N(a)=\lambda$，于是
$$\operatorname N(\lambda a^{-1}x)=\lambda\operatorname N(x).$$
任一尖点的稳定子是圆分 Galois 群中的 $\{\pm1\}$，故尖点域正是 $L_0$。

若 $u$ 如陈述所示，$\operatorname{div}(u)$ 是 Galois 不变的尖点除子。因为所有尖点共轭，每个几何尖点在除子中的系数相同，设为 $n$。主除子次数为零，所以 $n(p-1)/2=0$，从而 $n=0$。光滑射影几何连通曲线上无零极点的函数为常数，且 $u$ 在 $\mathbb Q$ 上有定义，故常数在 $\mathbb Q^\times$。证毕。

### 推论 G2（单纯基变换不能恢复通常 Runge 条件）

对每个数域 $F$，
$$c_F(X_N)=[F\cap L_0:\mathbb Q]\le r_1(F)+r_2(F).$$
因此对任何包含所有无穷位的 $S$，均有 $c_F(X_N)\le|S|$。

**证明。** 尖点是 $\operatorname{Gal}(L_0/\mathbb Q)$ 的正则集合；$F$ 上的轨道数即 $[F\cap L_0:\mathbb Q]$。令 $B=F\cap L_0$。$B$ 完全实，它的每个实嵌入至少延拓为 $F$ 的一个无穷位，所以 $[B:\mathbb Q]\le r_1(F)+r_2(F)$。证毕。

这里允许 $F$ 依赖 $p$。尤其，直接把全部尖点分裂到 $L_0$ 上，只会同时产生 $(p-1)/2$ 个无穷位；严格不等式仍然没有出现。

## 4. 覆盖提升同样不能直接创造 Runge 条件

这一节将上一障碍推广到“先把完整正规化子像降到一个已研究的真子群，再在相应扩域上用 Runge”的路线。命题只涉及当前这一类覆盖，不宣称所有替代方法不可行。

### 引理 G3（向量稳定子与复共轭）

1. $N$ 在 $M$ 上传递，$[1]\in M$ 的稳定子是
   $$J=\{I,-I,w,-w\}=\langle-I,w\rangle.$$
2. 若 $c\in N$ 的特征多项式为 $T^2-1$，则 $c$ 在 $N$ 中共轭于 $w$。
3. 对任意包含 $-I$ 的 $H\le N$，
   $$|H\backslash M|=|\langle w\rangle\backslash N/H|.$$

**证明。** 传递性来自乘法群。一个 $m_a$ 或 $m_aw$ 固定 $[1]$，当且仅当 $a=\pm1$，得到 1。$C$ 的非标量元素没有 $\mathbb F_p$ 特征直线，而 $c$ 有两个不同的 $\mathbb F_p$ 特征值，故 $c=m_aw\notin C$。条件 $c^2=I$ 等价于 $\operatorname N(a)=1$。有限域乘法群是循环群，映射 $b\mapsto b/b^p$ 的核为 $\mathbb F_p^\times$，其像恰是范数一群，所以存在 $b$ 使 $a=b/b^p$。于是 $c=m_bw m_b^{-1}$。最后 $M=N/J$，逆元映射把 $H\backslash N/J$ 变成 $J\backslash N/H$；中央的 $-I\in H$ 在 $N/H$ 上作用平凡，故可将 $J$ 换成 $\langle w\rangle$。证毕。

### 命题 G4（最小提升域上尖点轨道数等于无穷位数）

设无 CM 椭圆曲线 $E/\mathbb Q$ 的模 $p$ 像恰为 $N$，把挠点分裂域记为 $L=\mathbb Q(E[p])$，以所选基识别 $\operatorname{Gal}(L/\mathbb Q)=N$。设
$$H\le N,\qquad -I\in H,\qquad \det H=\mathbb F_p^\times,$$
并令 $K=L^H$。则 $E$ 的 $H$ 级结构给出 $X_H(K)$ 的点，并且
$$\boxed{c_K(X_H)=c_{\mathbb Q}(X_H)=r_1(K)+r_2(K).}\tag{4.1}$$

**证明。** 由定义，$G_K$ 在 $E[p]$ 上的像为 $H$，所以对应 $H$ 结构在 $K$ 上有定义。

Weil 配对给出 $\mathbb Q(\zeta_p)=L^{N\cap\mathrm{SL}_2}$。因为 $\det H$ 满，限制到 $H$ 的行列式仍满，所以 $G_K$ 的圆分像是全部 $\mathbb F_p^\times$。因此 §2 的公式给出
$$c_K(X_H)=|H\backslash M|=c_{\mathbb Q}(X_H).$$
同样可表述为 $K\cap\mathbb Q(\zeta_p)=\mathbb Q$，且所有尖点的 Galois 作用在基变换后不变。

固定一个嵌入 $L\hookrightarrow\mathbb C$。$K$ 的所有嵌入形成 $N/H$。复共轭的单点轨道对应实嵌入，双点轨道对应成对的复嵌入，所以其轨道数是 $r_1(K)+r_2(K)$。椭圆曲线的奇性及 Weil 配对给出复共轭矩阵的特征值 $1,-1$；由 G3，它在 $N$ 内共轭于 $w$。故
$$r_1(K)+r_2(K)=|\langle w\rangle\backslash N/H|=|H\backslash M|,$$
完成证明。

### 命题 G5（进一步扩域也不能恢复这类提升的 Runge 条件）

保留 G4 的 $E,N,H,L$。允许任意数域 $F$，只要求在当前选定的基下
$$\bar\rho_{E,p}(G_F)\subseteq H.$$
那么
$$\boxed{c_F(X_H)\le r_1(F)+r_2(F).}\tag{4.2}$$
因此对任何 $S\supseteq M_F^\infty$，通常 Runge 条件 $c_F(X_H)>|S|$ 都不成立。

**证明。** 令 $D=D_F$，$H_D=H\cap\det^{-1}(D)$，并令 $K_D=L^{H_D}$。因为 $\bar\rho_{E,p}(G_F)\subseteq H_D$，有 $K_D\subseteq F$。公式 (2.1) 和 G3 给出
$$c_F(X_H)=|H_D\backslash M|
=|\langle w\rangle\backslash N/H_D|.
$$
这里 $-I\in H_D$，因为 $\det(-I)=1$。与 G4 同样的复共轭—嵌入对应说明右侧恰为 $r_1(K_D)+r_2(K_D)$；这一句不需要 $\det H_D$ 满。数域每个无穷位在有限扩域中至少有一个延拓，所以
$$r_1(K_D)+r_2(K_D)\le r_1(F)+r_2(F).$$
证毕。

### 指数三例子

若 $p\equiv2\pmod3$，令 $H=C^3\rtimes\langle w\rangle$。此时 $-I\in C^3$，且 $\det H=\mathbb F_p^\times$：$p\equiv2\pmod3$ 使立方映射在 $\mathbb F_p^\times$ 上可逆。$[N:H]=3$，$N/C^3\cong S_3$，$H/C^3$ 是一个反射子群。复共轭在三个陪集上的循环型为 $(1)(2)$，故 $K=L^H$ 有签名 $(r_1,r_2)=(1,1)$。相应地，尖点有两个 $K$-Galois 轨道。

这解释了为何 Le Fourn–Lemos 对 **有理** 指数三像的 Runge 分析，不能经“把完整正规化子像提升到三次数域”直接解决当前剩余情形：有理指数三像有两个尖点轨道与一个无穷位，提升后的完整正规化子像有两个尖点轨道与两个无穷位。

### 命题 G6（去掉满行列式要求）

G4–G5 可扩展到任意包含 $-I$ 的 $H\le N$；此时将 $X_H$ 定义在其自然圆分基域
$$B_H=\mathbb Q(\zeta_p)^{\det H}$$
上，并选取与所固定的 Weil 配对相符的几何连通分支。若 $K=L^H$，则 $B_H\subseteq K$，且
$$c_K(X_H)=r_1(K)+r_2(K).$$
若任意数域 $F$ 满足 $\bar\rho_{E,p}(G_F)\subseteq H$，则自动有 $B_H\subseteq F$，从而 $X_H$ 可在 $F$ 上考虑，并仍然有
$$c_F(X_H)\le r_1(F)+r_2(F).$$

**证明。** 模曲线的自然基域描述见文献 5 开头，或文献 7 §1。Weil 配对及有限 Galois 对应给出
$$K\cap\mathbb Q(\zeta_p)=L^{\langle H,N\cap\mathrm{SL}_2\rangle}=L^{\det^{-1}(\det H)}=B_H,$$
所以 $K$ 包含所需基域。对任意上述 $F$，圆分像 $D_F\subseteq\det H$，故 $G_F$ 固定 $B_H$。

在这个选定分支上，几何尖点仍是 $(H\cap\mathrm{SL}_2)\backslash M$。对 $\lambda\in D_F$ 仍然可以选取 $\gamma_\lambda\in H$，而 §2 已验证伴随矩阵保持本题的 $H$。所以相对公式
$$c_F(X_H)=|(H\cap\det^{-1}(D_F))\backslash M|$$
依旧成立。其余证明就是 G4–G5 的双陪集计数及复共轭—嵌入对应；它们不使用行列式满。对 $F=K$，有 $D_K=\det H$，给出等式；对一般 $F$，取 $K_D=L^{H\cap\det^{-1}(D_F)}\subseteq F$，得到不等式。证毕。

这也覆盖了最极端的全级提升：若 $H=\{\pm I\}$，则 $K$ 含 $\mathbb Q(\zeta_p)$，所有 $(p^2-1)/2$ 个几何尖点在 $K$ 上有定义，但 $K$ 也恰有 $(p^2-1)/2$ 个无穷位；仍没有严格的 Runge 不等式。

## 5. 其它已经识别的几何/高度缺口

### 5.1 整数性不能从潜在好约化的部分结论中推出

Le Fourn–Lemos Proposition 5.2 只保证在 $q\not\equiv\pm1\pmod p$ 的素数处潜在好约化，不能据此声称 $j\in\mathbb Z$。在完整 $N$ 情形，仍可能存在 $q\equiv\pm1\pmod p$ 的分母。指数三情形获得整数性的 formal-immersion 论证用了该特殊曲线的 Jacobian 商；它不是完整 $N$ 情形已有的通用整数性定理。

即使另行证明了完整 $N$ 情形整数性，G1–G2 仍阻断通常 Runge 条件。需要另一个满足所需增长率的统一高度上界。

### 5.2 一条很大且有效的上界不等于统一排除

已有同源界给出形如 $h(j)\ge cp-O(1)$ 的必要条件。若某整数点算法只给 $h(j)\le B(p)$，而 $B(p)/p\to\infty$，上下界可同时满足，不会约束 $p$。Bajolet–Sha 的一般非分裂整数点界正处于这种状态。指数三或分裂情形成功的关键是更小的 $O(\sqrt p)$ 级上界，与线性下界不相容；该上界不能从别的模曲线转移过来。

### 5.3 Faltings 与 gonality 的量词问题

对每个固定 $p$ 得到 $X_{\rm ns}^+(p)(\mathbb Q)$ 有限，不会推出所有充分大 $p$ 都没有非 CM 点。不同素数对应不同曲线；“每条曲线有限”允许每个 $p$ 都有一个点。

同样，gonality 趋于无穷主要限制有界次数点形成的无限族，不禁止孤立有理点。此家族本身已有清楚的提醒：固定 $j=1728$ 的 CM 曲线，在 $p\equiv3\pmod4$ 的素数处给出非分裂正规化子上的有理点，尽管这些曲线的复杂度随 $p$ 增长。要排除 **非 CM** 有理点，仍须能辨别其算术来源的新论证。

## 6. 对继续研究的含义

可以排除的具体尝试是：

1. 在 $\mathbb Q(X_{\rm ns}^+(p))$ 中构造非恒定、零极点仅在尖点的模单位；G1 直接说明做不到。
2. 仅通过扩充常数域分裂尖点来恢复通常 Runge 条件；G2 对任意扩域给出反证。
3. 将完整 $N$ 像的点提升到 $X_H$，并希望其定义域上的尖点轨道数超过无穷位数；G4–G6 排除所有 $H\le N$、$-I\in H$ 的上述尝试，包括行列式非满、需在自然圆分基域定义的覆盖，以及指数三覆盖。

仍开放的是找到不受这一轨道计数约束的全局论证，例如利用非尖点除子且能控制其算术值的高度方法，或对高秩 Jacobian 的有理点使用足以统一排除非 CM 点的额外结构。这里没有为这些方法补出关键不等式，不能据此宣布有统一常数。
