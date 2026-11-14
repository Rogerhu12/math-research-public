# CM、Iwasawa 与广义 Kato 类路线（2026-11-12）

负责：Astra-rank2-Sha 的 cm_iwasawa_routes 子代理。

**状态：** 原始文献范围核查及下列逻辑推论已经完成；没有证明任何固定秩二曲线满足无穷多个 $p$ 的目标。本文不以未经核查的新稿替代缺失证明。未进行 git 操作。

## 1. 可直接使用的 CM 判据：有限性只需估值至多 3

J. Coates, Z. Liang, R. Sujatha, *The Tate–Shafarevich group for elliptic curves with complex multiplication*, J. Algebra **322** (2009), 657–674，作者预印本 [arXiv:0901.3832](https://arxiv.org/pdf/0901.3832)，Theorems 2.1–2.2，PDF 第 4–5 页（以正文印刷页码计）。

设 $E/\mathbb Q$ 有 CM，$K$ 为其 CM 域，$g=\operatorname{rank}E(\mathbb Q)$；按该文正规化，令
$$c_p^+(E)=(\Omega_\infty^+)^{-p}L(\overline\psi_E^{\,p},p)\in\mathbb Q.$$
对好约化、在 $K$ 分裂、排除定理中 $w$ 和 $\alpha(E)$ 的素数 $p$，若解析秩与 $g$ 同奇偶，则
$$v_p(c_p^+)<g+2\quad\Longrightarrow\quad\Sha(E/K)(p)\ \text{有限}.$$
这是 Theorem 2.2 的有限性部分。估值等于 $g$，再加非 anomalous 及 $p\nmid6$，给出该 $p$-primary 部分为零。

**对本题的精确目标。** 固定一条代数秩恰为二、根数为 $+1$ 的 CM 曲线。由函数方程解析秩为偶数，故满足所需同奇偶条件。在固定有限排除集之外，只要证明
$$\#\{p\text{ split}:v_p(c_p^+(E))\le3\}=\infty,$$
即足以完成本题。这里不必强行证明 $v_p(c_p^+)=2$；估值 3 仍然够用。这是**充分条件**，不声称它是有限性的必要条件。

从 $K$ 回到 $\mathbb Q$ 不损失此结论：对奇素数 $p$，restriction/corestriction 的复合是乘以 $[K:\mathbb Q]=2$，所以 $\Sha(E/\mathbb Q)[p^\infty]\to\Sha(E/K)[p^\infty]$ 单射。$p$-primary 意义下 2 是可逆的。

## 2. 已有同时控制所有大 $p$ 的结果为何仍不够

Coates–Liang–Sujatha, *The Tate-Shafarevich group for elliptic curves with complex multiplication II*, Milan J. Math. **78** (2010), 395–416，[arXiv:1005.4206](https://arxiv.org/pdf/1005.4206)，Theorems 1.1、1.3、3.2。

记 $t_p=\operatorname{corank}_{\mathbb Z_p}\Sha(E/\mathbb Q)[p^\infty]$。Theorem 1.1 证明：每个 $\varepsilon>0$ 都有有效阈值，所有充分大的好 ordinary $p$ 满足
$$t_p\le(1/2+\varepsilon)p-g.$$
Theorem 1.3 对 $y^2=x^3-Dx$、$D=-14,17,-33,-34,-39$ 五条秩二曲线，证明所有好分裂 $p<30000$ 的 $p$-primary 部分有限。除四个列明的 $(D,p)$ 外为零；其中三例经 Wuthrich 的计算另行解决。

**逻辑检查。** 即使再用 $t_p$ 为非负偶数，上述线性上界对所有大 $p$ 仍允许 $t_p=2$。不能让 $\varepsilon$ 随 $p$ 任意变化而忽略阈值 $c(E,\varepsilon)$；即使这样做，$p/2$ 主项也不会消失。

**对其乘积公式路线的继续尝试。** 该文 §3 先用惰性素数强制整除，去掉 $\prod_{q\mathrm{\ inert}}q^{\nu_q}$；剩余非零代数整数的复大小仍是 $C^p p^{p/2}$ 级别。这只允许得到 $v_p=O(p)$。为了由同奇偶性强制 $t_p=0$，需要把有关总估值压到小于 $g+2=4$。把线性系数改善为任何固定正数，均不足以跨越这个差距。

尝试把“所有分裂 $q$ 的额外 Selmer 余秩”代入同一个权重 $n$ 的特值时，还有一道算术障碍：有关插值分支要求 $n\equiv1\pmod{q-1}$。因此不能把关于不同权重 $q$ 的整除断言乘成同一个代数数上的整除断言。取 $n-1$ 为多个 $q-1$ 的公倍数虽可满足这些条件，却使权重和阶乘增长；当前估计没有导出矛盾。这是已尝试路线的明确未闭合处。

## 3. 广义 Kato 类给出另一条精确的等价路线

F. Castella, *Generalised Kato classes on CM elliptic curves of rank 2*, final version, to appear in American J. Math.; [arXiv:2204.09608v3](https://arxiv.org/html/2204.09608v3)，Theorem B / Theorem 6.3.1。

在该文 CM、好 ordinary $p\ge5$、$L(E,1)=0$、根数 $+1$ 和辅助 Hecke 角色条件下，存在 $\kappa_p\in\operatorname{Sel}(\mathbb Q,V_pE)$，并有
$$\kappa_p\ne0\Longrightarrow\dim_{\mathbb Q_p}\operatorname{Sel}(\mathbb Q,V_pE)=2.$$
反向在 Selmer 维数已为 2 时，$\kappa_p\ne0$ 等价于局部 restriction 非零。

### 命题：在固定代数秩二曲线上，上述 $\kappa_p\ne0$ 等价于 $\Sha[p^\infty]$ 有限

此命题是使用已发表/最终稿定理的逻辑推论；它没有消除所需的非消失问题。

**证明。** Kummer 理论给出
$$0\to E(\mathbb Q)\otimes\mathbb Q_p\to\operatorname{Sel}(\mathbb Q,V_pE)
\to T_p\Sha(E/\mathbb Q)\otimes\mathbb Q_p\to0.$$
若 $\kappa_p\ne0$，引用定理令中间项维数为 2。左项也为 2，故右项为零。$\Sha[p^\infty]$ 是 cofinitely generated 的 $\mathbb Z_p$-模，因此 Tate 模为零等价于这个 $p$-primary 群有限。

反之，若 $\Sha[p^\infty]$ 有限，则中间项维数为 2。取任一非扭点 $P\in E(\mathbb Q)$。其局部像在 $E(\mathbb Q_p)\widehat\otimes\mathbb Q_p$ 非零：先以非零整数 $N$ 乘 $P$，使 $NP$ 进入足够小的形式群；形式对数在该邻域是单射。如果局部像为零，其对数为零，故某个非零整数倍的 $P$ 是单位元，与非扭性矛盾。因此 restriction 非零。定理反向给出 $\kappa_p\ne0$。证毕。

**结论。** 对这样固定的 $E$，本题可改写为在无穷多个合适的 $p$ 证明 $\kappa_p\ne0$。这一改写不需要先假设 $p$-adic 高度非退化。

### 不能省去的特化步骤

Castella 的 Theorem A 证明 big diagonal class 在两变量系数环上非扭。$\kappa_p$ 却是一个特定权重的特化。非扭元素可以落在特化理想内；例如 $R=\mathbb Q_p[[U,V]]$、自由秩一模 $M=R$、$z=U$，则 $z$ 非扭但 $z|_{U=0}=0$。

由此排除以下推理：辅助 Hecke $L$-值可选成非零 $\Rightarrow$ big class 非零 $\Rightarrow\kappa_p\ne0$。最后一箭头没有成立。辅助角色的非消失仅去除了其他因子的障碍；目标 $E$ 对应的特化阶数仍保留原来的 Selmer 问题。

## 4. 高度非零不能代替二维行列式非零

D. Bertrand, *Propriétés arithmétiques de fonctions thêta à plusieurs variables*, in Number theory (Noordwijkerhout 1983), LNM **1068** (1984), 17–22。可核查的精确转述见 K. Rubin 的附录 Theorem A.1，附于 A. Agboola–B. Howard, *Anticyclotomic Iwasawa theory of CM elliptic curves*, AIF **56** (2006), 1001–1048，[作者全文](https://web.math.ucsb.edu/~agboola/papers/cm1-final.pdf)。该结论涉及单个非扭点的 $\mathfrak p$-adic 自高度。

即使一个对称双线性形式对每个非零有理向量 $v$ 都满足 $h(v,v)\ne0$，它扩张到 $\mathbb Q_p$ 后也未必非退化。这里有完整反例。

取 $\alpha\in\mathbb Q_p\setminus\mathbb Q$，定义
$$h((x,y),(x',y'))=(x+\alpha y)(x'+\alpha y').$$
对 $(x,y)\in\mathbb Q^2\setminus\{0\}$，$x+\alpha y\ne0$，所以自配对非零；但矩阵
$$\begin{pmatrix}1&\alpha\\\alpha&\alpha^2\end{pmatrix}$$
行列式为零，并以 $(-\alpha,1)$ 为核向量。这一反例只作线性代数说明，不声称它来自某条椭圆曲线的高度。

A. Burungale–D. Disegni, *On the non-vanishing of p-adic heights on CM abelian varieties, and the arithmetic of Katz p-adic L-functions*, AIF **70** (2020), 2077–2101，Theorem 1.1，[期刊](https://numdam.org/articles/10.5802/aif.3381/)、[作者稿](https://disegni-daniel.perso.math.cnrs.fr/height1.pdf)。其非消失结论在固定 $p$ 后沿 anticyclotomic 有限阶角色变化，且有根数 $-1$ 等假设。不能交换成固定 $E$、角色为 1、让 $p$ 变化的结论。

最后，就算某人另行证明了某个或无穷多个 $p$ 的二维高度非退化，也不能单靠这件事推出 $\Sha[p^\infty]$ 有限。Schneider–Perrin-Riou 的特殊值等式把“高度非退化且 $\Sha[p^\infty]$ 有限”与特征幂级数的最小零阶联系起来；其中第二个条件不可删除。

## 5. $\mu=0$、主猜想、余秩与零阶是不同数据

以下均为直接的模论检查。

1. 对 $\Lambda=\mathbb Z_p[[T]]$，$M=(\Lambda/(T))^4$ 是有限生成 torsion 模，$\mu(M)=0$；其 coinvariants 为 $\mathbb Z_p^4$。所以 torsion 和 $\mu=0$ 不给出 coinvariant 维数等于 2。
2. $N=\Lambda/(T^2)$ 的特征幂级数在零点阶为 2，但 $N/TN\cong\mathbb Z_p$，只有余秩 1。特征零阶算的是带长度的广义零特征空间；coinvariant 维数只数 Jordan 块。
3. 为每个 $p$ 取形式模型 $X_p=(\Lambda_p/(T))^4$、$L_p(T)=T^4$，同时满足 torsion、$\mu=0$、形式的特征理想等式以及偶余秩。它仍允许全部 $p$ 比两个有理点贡献多出余秩 2。此模型不是算术反例；它证明这些抽象性质不足以逻辑推出本题。

这也解释为什么 Rubin 的主猜想即使在全部好分裂素数都可使用，也还需要控制中心点的特化。

## 6. 超奇异素数也没有自动绕开中心点问题

R. Pollack–K. Rubin, *The main conjecture for CM elliptic curves at supersingular primes*, Ann. of Math. **159** (2004), 447–464，Theorem 7.3，[期刊](https://annals.math.princeton.edu/2004/159-1/p11)、[作者稿](https://www.math.uci.edu/~krubin/preprints/pollack-rubin.pdf)。其结论识别 signed Selmer 的特征理想与 $L_p^\pm$。

F. Castella, *A formula of Perrin-Riou and characteristic power series of signed Selmer groups*, [arXiv:2502.19618v2](https://arxiv.org/html/2502.19618v2)，Theorem A：在 $a_p=0$ 的好超奇异情形，两个 signed 特征幂级数最小零阶至少为代数秩；其等号和首项公式的假设包括 $\Sha[p^\infty]$ 有限及 strict regulator 非零。

故不能用这个首项公式反过来“证明”假设中的 $\Sha$ 有限。若另行证明某个 signed $L$-函数在中心恰好二阶，配合控制与主猜想有望给界；但本次未找到保证无穷多个惰性 $p$ 满足该二阶非消失的定理。

## 7. 2026 新稿的作用和不应引用过界之处

B. S. Banwait, *Second derivatives of p-adic L-functions and the Shafarevich–Tate group of rank-two CM elliptic curves*, [arXiv:2609.08431v1](https://arxiv.org/html/2609.08431v1)，2026-09-08，Theorems A/B，§§13–16。这里只将它用作最新路线索引，没有把其中新论证作为本仓库的已证输入。

该稿给逐 $p$ 的二阶系数单位判据，转成权重 $2p-1$ 的三个 Hecke 特值组合的估值条件；计算仍在有限素数范围。原文明确留下随 $p$ 非消失的问题。其约化只在模 $p^3$ 精度比较该组合与所需二阶 moment，所以组合在复数意义下非零，不足以保证其除以 $p^2$ 后模 $p$ 非零。

**独立的推理检查。** 设 $A_p$ 是随 $p$ 变化的非零代数数；每个 $A_p$ 有有限多个素因子，并不能推出存在无穷多个 $p$ 不整除 $A_p$，因为简单模型 $A_p=p$ 已否定这种量词交换。同理，权重 $2p-1$ 的对象不能被当作一个固定代数数来取有限坏素数集合。

## 8. 本次留下的具体研究接口

优先接口是 §1：固定 $E:y^2=x^3-17x$（其精确秩证书由另一子代理处理），尝试对无穷多个 $p\equiv1\pmod4$ 证明 $v_p(c_p^+(E))\le3$。需要一个真正的变化素数论证；继续增加计算上界不能替代它。

第二接口是 §3：证明固定 $E$ 的 $\kappa_p$ 在无穷多个 $p$ 非零。若企图将这些类统一为某个固定的代数/几何对象，必须给出跨 $p$ 的比较映射并证明其特化没有消失，不能把 Hida 家族（已固定 $p$）直接视为跨 $p$ 家族。

目前上述两个接口均未闭合；本笔记没有宣称主任务完成。


## 9. 实际跨 $p$ 攻击：把 E17 的目标写成明确的导数递推

这里不再只说“某个 $p$-adic $L$-值未知”。把必要计算化成一条固定 CM 数域中的整数序列，并检验可能的统一办法。

固定
$$E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad f=34(1+i).$$
课题 R4 给出精确代数秩二；`notes/2026-11-12-cm-local-inputs.md` 给出根数 $+1$ 和 $\alpha(E)=1$。设 $\Lambda_E=\Omega_\infty\mathbb Z[i]$，
$$z_0=\Omega_\infty/f,\quad u=\wp(z_0),\quad v=\wp'(z_0)/2,\quad F=K(E_f).$$
这些对象均不随后续素数 $p$ 改变。CLS2009 Lemma 3.1、§3 式(49)–(53) 给出 $F=K(u)$、$[F:K]=256$、$v\in F$；$u,v$ 为代数整数。

定义 $B_0(X)=1$，并递推
$$\boxed{B_{n+1}(X)=4(X^3-17X)B_n''(X)+6(3X^2-17)B_n'(X)+12XB_n(X).}$$

### 导数恒等式的完整证明

对一般 $D$，写 $x(z)=\wp(z)$、$y(z)=\wp'(z)/2$，则
$$x'=2y,\qquad y'=3x^2-D,\qquad y^2=x^3-Dx.$$
归纳证明 $x^{(2n+1)}=2yB_n(x)$。$n=0$ 是定义。若对 $n$ 成立，先求导：
$$\frac{d}{dz}(2yB_n(x))=2(3x^2-D)B_n(x)+4(x^3-Dx)B_n'(x).$$
再求导并提取 $2y$，得到
$$2y\{12xB_n(x)+6(3x^2-D)B_n'(x)+4(x^3-Dx)B_n''(x)\},$$
恰好给出递推。故恒等式对一切 $n$ 成立。证毕。

特别地，$B_n\in\mathbb Z[X]$，$\deg B_n=n$。其最高次项系数 $b_n$ 满足
$$b_{n+1}=(2n+3)(2n+4)b_n,\quad b_0=1,$$
所以 $b_n=(2n+2)!/2$。前几项为
$$B_0=1,\qquad B_1=12X,\qquad B_2=360X^2-72D.$$
若写 $B_n=\sum_k b_{n,k}X^k$，可用完全整数的系数更新
$$b_{n+1,k+1}\mathrel{+}=(2k+3)(2k+4)b_{n,k},\qquad
b_{n+1,k-1}\mathrel{+}=-2Dk(2k+1)b_{n,k}.$$

令
$$a_n=\operatorname{Tr}_{F/K}(vB_n(u))\in\mathbb Z[i].$$
CLS2009 的 Eisenstein 特值公式（Theorem 2.3、式(53)），按 CLS2010 §4 式(77)后的勘误去掉原式多余的单位数因子 $w=4$，现在成为
$$\boxed{c_p^+(E)=-\frac{2a_{(p-3)/2}}{f^p(p-1)!}.}$$
CLS2010 明确要求把 2009 年表中的值乘以 $4$；这个修正不改变奇素数处的赋值，但精确恒等式必须采用修正版。见 `results/R6-cm-trace-recurrence.md`。
这里 $p\equiv1\pmod4$，$p\ne17$，因此所有分母因子在两个 $p$-adic 位都可逆。对任一 $\mathfrak p\mid p$，
$$v_p(c_p^+(E))=v_{\mathfrak p}\bigl(a_{(p-3)/2}\bigr).$$
两个 $\mathfrak p$ 的估值相同，因为左边是有理数的估值。于是本路线的精确未解命题为
$$\boxed{\#\{p\equiv1\pmod4,\ p\ne17:\ a_{(p-3)/2}\not\equiv0\pmod{\mathfrak p^4}\}=\infty.}$$

这已经是可复算的明确算术命题，而不是一个没有指定对象的“非消失假设”。目前没有证明这个集合无穷。

### 9.1 为何固定数域本身没有给出 Chebotarev 条件

$F$、$u$、$v$ 固定，但是被检验的整数为第 $(p-3)/2$ 项；模数还要求 $\mathfrak p^4$。Chebotarev 可给出 $\operatorname{Frob}_{\mathfrak p}$ 在一个固定有限扩张中的分布，但当前没有证明上述高精度余数由某个固定扩张里的 Frobenius 共轭类决定。不能从“都在同一个数域里”推断该决定性。

即使先限制 $p$ 在一个完全分裂的 Chebotarev 集合，信息也只直接给出各固定代数数的模 $\mathfrak p$ Frobenius 行为。除以必有的 $p^2$ 后的下两级余数，仍是不同的算术数据。作为量词检查，固定数域 $\mathbb Q$ 中的序列 $d_n=(2n+3)^4$ 在相同索引上满足 $d_{(p-3)/2}=p^4$；它说明“固定数域 + 非零项 + 变化素数索引”不能提供所需结论。这个简单序列不模拟 CM 递推，只排除无依据的量词交换。

### 9.2 不能把导数递推直接压成固定 256 维矩阵

一个诱人的办法是先把每个 $B_n$ 对 $u$ 的最小多项式 $G(X)$ 取余，然后把上述递推当作 $K[X]/(G)$ 上的固定线性算子。这个操作不合法，下面给出完整证明。

对一般 $D$，令
$$\mathcal L=4(X^3-DX)\partial_X^2+6(3X^2-D)\partial_X+12X.$$
设 $G$ 可分且 $G(u)=0$，并且 $u^3-Du=v^2\ne0$。若 $\mathcal L$ 保持理想 $(G)$，由于乘以 $X$ 和任意多项式均保持该理想，交换子
$$[\mathcal L,X]-6(3X^2-D)=8(X^3-DX)\partial_X$$
也保持 $(G)$。作用到 $G$ 后在 $u$ 处求值，应得到零；但实际为
$$8(u^3-Du)G'(u)=8v^2G'(u)\ne0,$$
矛盾。故 $\mathcal L$ 不下降到 $K[X]/(G)$。

本例的 $G$ 在特征零可分，$z_0$ 的 $f$-阶大于 2，故 $v\ne0$，满足全部假设。因此，虽然算完 $B_n$ 后可以对 $G$ 取余再求 trace，却不能每个导数步骤都丢掉 $G$ 的倍数；丢掉的部分的导数还会贡献。这排除了一个具体的“固定有限矩阵 + Frobenius”伪简化，并未排除另造正确的更丰富有限模型。

### 9.3 模 $p$ 的微分简化为何还差两个 $p$-adic 层级

在好约化下，椭圆曲线的不变导子在特征 $p$ 满足 restricted-Lie 的 $p$ 次幂关系；因此高阶导数常有模 $p$ 简化。即便利用这一步，目标仍需要比较 $a_{(p-3)/2}/p^2$ 模 $p^2$。一个只在模 $p$ 成立的关系，经两次除以 $p$ 后没有任何可保留的精度。要使用该想法，需要明确构造并证明一个模 $p^4$ 的 Frobenius 提升关系，且证明它的剩余项在无穷多个 $p$ 非零。当前递推没有给出后一个结论。

## 10. 两个明确点与广义 Kato 类：缺失的比较式在哪里

对 $E17$ 取 $P=(-1,4)$、$Q=(9,24)$；R4 证明二者独立。令
$$\ell_p(P)=\log_{E,p}(P),\qquad \ell_p(Q)=\log_{E,p}(Q),$$
形式对数先通过乘以局部有限指数进入形式群再除回去，因此给出 $E(\mathbb Q_p)\widehat\otimes\mathbb Q_p\simeq\mathbb Q_p$。两个对数均非零：否则对应点是扭点。

在 $E(\mathbb Q)\otimes\mathbb Q_p$ 中定义
$$v_p=\ell_p(Q)P-\ell_p(P)Q.$$
由于 $P,Q$ 独立且两个系数不同时为零，$v_p\ne0$。同时
$$\log_{E,p}(v_p)=\ell_p(Q)\ell_p(P)-\ell_p(P)\ell_p(Q)=0.$$
因此我们对**每个**好 $p$ 已经有了一个明确非零 strict Kummer 类。它本身不控制 $\Sha$；一般 $r\ge2$ 时总能这样做。

为了与 Castella 的 $\kappa_p$ 比较，精确问题如下。令
$$S_p=\operatorname{Sel}(\mathbb Q,V_pE),\qquad
S_p^0=\ker(S_p\to E(\mathbb Q_p)\widehat\otimes\mathbb Q_p),\qquad
W_p=E(\mathbb Q)\otimes\mathbb Q_p.$$
因为局部 restriction 非零且目标一维，设 $t_p=\operatorname{corank}\Sha[p^\infty]$，便有
$$\dim S_p^0=1+t_p,\qquad W_p\cap S_p^0=\mathbb Q_pv_p.$$
而且严格地有短正合列
$$0\to\mathbb Q_pv_p\to S_p^0\to T_p\Sha(E/\mathbb Q)\otimes\mathbb Q_p\to0.$$
证明最后的满射：任取 $S_p/W_p$ 中的类，用 $W_p$ 中某向量减掉其局部 restriction（$W_p$ 的局部像已经是一维全空间），即可取到 $S_p^0$ 中代表。核恰是 $W_p\cap S_p^0$。

Castella 的构造给出 $\kappa_p\in S_p^0$；其 §1.3 指出，**当它非零时**它生成 $S_p^0$。于是若有人想从这两个显式点直接得出 $\kappa_p\ne0$，必须另证一条非循环的比较公式，例如
$$\boxed{\kappa_p=A_p\bigl(\ell_p(Q)P-\ell_p(P)Q\bigr),\qquad A_p\ne0.}$$
这里有两个不能省略的内容：

- 先证明 $\kappa_p$ 落在 $W_p$，而不仅仅是落在 $S_p^0$；后者可能含有 $\Sha$ 的 Tate 模方向。
- 给出 $A_p$ 的已证明表达式，并在所需的无穷多个 $p$ 证明其非零。即使已知它在有理点直线上，$A_p=0$ 仍然允许。

若先用 $\Sha[p^\infty]$ 有限证明 $S_p^0=\mathbb Q_pv_p$，再获得上述比较，那只是已知结论下的解释。不能用它反过来证明同一个有限性。类似地，若 $A_p$ 的表达式含有所需二阶 $p$-adic $L$ 系数并预设该系数非零，瓶颈只是换了记号。

当前我们已无条件构造了 $v_p$，但没有无条件得到上述 $\kappa_p$ 比较与 $A_p\ne0$。这是使用显式点攻击 Castella 路线所缺少的精确一步。
