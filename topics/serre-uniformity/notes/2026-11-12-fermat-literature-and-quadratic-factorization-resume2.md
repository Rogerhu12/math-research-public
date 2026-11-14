# O6：广义 Fermat 文献接口、导子阈值与二次分解的真实范围

日期：2026-11-12；会话：serre-uniformity-astra-resume2。

**状态：文献假设核验与完整推导。** 本文得到两个可直接使用的子范围排除：所有 R19 解都有 $\operatorname{rad}(|Z|)>15625$；族 I、III 中 $W$ 不能为整数立方。随后完整检查一般二次范数分解和固定二次域的平方子族。一般分解恰是 R46 已有的三同源 Kummer 类，并未提供独立的统一消失定理。本文不完成 O6，也不把有界导子、固定支撑或一部分整数形状的排除当作完成标准。

## 1. 所核验的实际问题

保留 [R19](../results/R19-converse-fermat-fixed-cm.md) 的全部原始性、互素性和二进条件。具体地，
$$
p>37,\qquad |Z|>1,\qquad (Z,6p)=1,\qquad 3\nmid X,
$$
且 $X,W,Z$ 两两互素，并有
$$
X^3-27W^2=cZ^p,\qquad
c=1\ \text{（族 I、III）},\quad c=8\ \text{（族 II）}.
\tag{1}
$$
对应的非 CM Frey 曲线记为 $E$，参考曲线为
$$
A:y^2=x^3-x.
$$
R19 已证明
$$
E[p]\simeq A[p],\qquad N_E=32R,\qquad
R=\operatorname{rad}(|Z|),
\tag{2}
$$
并已排除 $p\equiv1\pmod4$。本文因而主要关心 $p\equiv3\pmod4$ 的实际解。特别地，这些实际解的最小可能指数为 $43$。

这里需要的是同时处理变化的 $p$ 和 $Z$ 的全局定理。固定某个签名 $(2,3,p)$ 的有限性、一个固定 $Z$ 的 Mordell–Weil 计算，以及假设 Frey–Mazur 或 abc 后的结论，都不能代替这个量词。

## 2. Cremona–Freitas 给出的无条件导子范围

### 2.1 已发表定理及证明性质

Cremona–Freitas，*Global methods for the symplectic type of congruences between elliptic curves*，Rev. Mat. Iberoam. **38** (2022), 1–32，**Theorem 1.3** 的精确量词是：
$$
\begin{gathered}
p>17\text{ 为任意素数},\quad E_1,E_2/\mathbb Q,\\
N_{E_1}\le500000,\quad N_{E_2}\le500000,\quad
E_1[p]\simeq E_2[p]\\
\Longrightarrow E_1,E_2\text{ 在 }\mathbb Q\text{ 上同源}.
\end{gathered}
\tag{3}
$$
两条曲线都受导子上界约束；定理没有排除 CM 曲线，也没有 GRH 假设。

[刊本原文](https://ems.press/content/serial-article-files/38965)，
[DOI 10.4171/RMI/1269](https://doi.org/10.4171/RMI/1269)。

这是文中第 4 节证明的计算定理。相同导子的不同同源类由 Frobenius 迹差的精确最大公因数排除。导子不同的同余由 Serre 层和权的比较，迫使 $p$ 整除某个乘性素数处的极小判别式赋值。完整导子数据库中这类 $p$ 最大为 $97$，其余有限检查在第 3 节完成。因此不能把 (3) 弱化成“只枚举检查了 $p\le97$”，也不能把它扩张为导子无界的 Frey–Mazur 定理。本轮使用已发表定理，没有声称重新执行其整个数据库证明。

### 2.2 对三个整数族的直接推论

**推论。** 任意 R19 实际解满足
$$
\boxed{R>15625.}
\tag{4}
$$

**证明。** 假设 $R\le15625$。由 (2)，
$$
N_E=32R\le500000,\qquad N_A=32.
$$
因为 $p>37>17$，(3) 给出 $E$ 与 $A$ 在 $\mathbb Q$ 上同源。同源保留 CM 性质：在 $\overline{\mathbb Q}$ 上用同源共轭即可得到两曲线有理自同态代数的同构。因此 $E$ 有 CM，违反 R19 已证明的非整 $j(E)$。证毕。

(4) 限制的是不同分母素数的**乘积**，不是说每个分母素数都大于 $15625$。若 $|Z|=q^m$ 只有一个素因子，则它才化为 $q>15625$。所有指数 $m\ge1$ 和三个族，包括 III 偶 $X$ 的射线分支，都包含在这个推论中。

### 2.3 与 R13、R37 的准确比较

[R13](../results/R13-denominators-for-fixed-cm-congruence.md) 已给出
$$
q\mid Z\Longrightarrow q\equiv\pm1\pmod{4p},
\qquad q\ge4p-1;
\tag{5}
$$
若 $q$ 在 $\mathbb Q(i)$ 中分裂，还有 $q\ge4p^2+1$。

因此若 $Z$ 有两个不同素因子，则
$$
R\ge(4p-1)^2\ge171^2=29241>15625.
$$
所以 (4) 相对于 R13 的新增适用范围，已经只剩单素数支撑的小导子部分。

[R37](../results/R37-cubic-descent-and-class-group-obstruction.md) 在普通分支给出
$$
R\ge\frac{\gamma}{s}p^4,\qquad
s=
\begin{cases}
1,&\mathrm I,\\
8,&\mathrm {II},\\
4,&\mathrm {III},\ X\text{ 奇},
\end{cases}
\quad
\gamma=
\begin{cases}
1/64,&Z>0,\\
\pi^2/1024,&Z<0.
\end{cases}
\tag{6}
$$
可统一用 $R\ge\pi^2p^4/8192$。当 $p\ge67$ 时这个较弱的统一下界已经大于 $15625$；用 $\pi^2>9$ 即可严格验证，不依赖小数近似。于是普通分支只有 $p=43,47,59$ 还可能从 (4) 获得超出这个统一版本的信息，具体某支的 (6) 可能更早就已更强。

在 III 偶 $X$ 的射线分支，R37 给
$$
|d-1|\ge p^2/4,\qquad d=\operatorname{sf}(Z),\qquad |d|\le R,
$$
从而 $R\ge p^2/4-1$。在 $p\ge251$ 时该界也已经强于 (4)。

以上比较说明 (4) 是可用的精确导子阈值，并非控制变化分母的新渐近上界。

## 3. 已发表广义 Fermat 定理的接口

### 3.1 Darmon–Merel：缺失的是辅助有理同源

Darmon–Merel，*Winding quotients and some variants of Fermat's Last Theorem*，J. reine angew. Math. **490** (1997), 81–100，Main Theorem 分别处理
$$
x^n+y^n=2z^n,\qquad x^n+y^n=z^2,\qquad x^n+y^n=z^3
$$
的非平凡原始整数解，门槛依次为 $n\ge3,4,3$；第三项原先附加的 $\mathbb Q$ 上椭圆曲线模性现已成立。

其 **Theorem 8.1** 要求：实际曲线有一个有理循环 $r$ 同源，$r=2$ 或 $3$；$p\ge5$；模 $p$ 像为非分裂 Cartan 正规化子。结论是 $j\in\mathbb Z[1/p]$。

[作者原文](https://www.math.mcgill.ca/darmon/pub/Articles/Research/18.Merel/paper.pdf)，
[作者发表目录](https://www.math.mcgill.ca/darmon/pub/pub.html)。

R19 的曲线 $E$ 没有这种辅助有理同源：Lemos 的有理循环同源统一性定理与 (2) 矛盾时即排除它；R37 已用此排除了有理 $2$ 挠点。$A$ 的有理 $2$ 挠点不会经 $E[p]\simeq A[p]$ 自动转移到 $E$。因此把 Theorem 8.1 用于 $A$ 只会重获 $j(A)=1728$ 的整性，用于 $E$ 则缺失假设。

方程 (1) 也不是 $(p,p,2)$ 或 $(p,p,3)$ 签名。没有证明额外完美幂条件之前，不能靠重新命名变量进入 Main Theorem。

### 3.2 Freitas–Naskręcki–Stoll：系数 27 与原始性不能删除

Freitas–Naskręcki–Stoll，*The generalized Fermat equation with exponents 2, 3, n*，Compositio Math. **156** (2020), 77–113，研究互素整数的 $u^2+v^3=w^p$。**Theorem 5.1** 给按 $p\bmod24$ 分类的局部可允许模曲线扭曲；**Lemma 6.1** 排除 CM 参考曲线 27a1 的 $p\equiv1\pmod3$ 分支和 288a1 的 $p\equiv1\pmod4$ 分支。后者是分裂 Cartan 排除，不包含本题剩余的 $p\equiv3\pmod4$ 情形。

[作者刊本版本](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf)，
[DOI 10.1112/S0010437X19007693](https://doi.org/10.1112/S0010437X19007693)。

本题能直接写成
$$
(27W)^2+(-3X)^3=-27cZ^p,
\tag{7}
$$
但这不是系数为 $1$ 的原始问题。以 $c=1$ 为例，令
$$
u=3^{(3p+3)/2}W,\qquad v=-3^pX,\qquad w=-27Z
$$
确实得到 $u^2+v^3=w^p$；三个坐标却都被 $3$ 整除，所以不能代入该论文的原始解定理。此障碍正对应其降层参考导子列表与本题层 $32$ 的差别。没有一个保留所需原始性的变量替换证明，就不能借用该论文的有限小指数分类或 CM 子分支排除。

### 3.3 一个确实可用的整数形状排除：I、III 中 W 不是立方

Freitas，*On the Fermat-type equation $x^3+y^3=z^p$*，Comment. Math. Helv. **91** (2016), 295–304，**Theorem 1（Kraus, 1998）** 明确给出：$p\ge17$ 的非平凡原始解 $a^3+b^3=c_0^p$ 必有 $3\mid c_0$。同一必要条件亦见 Bennett–Chen–Dahmen–Yazdani (2015), **Proposition 7**。本轮核验的是这两篇原始研究论文中的定理陈述；没有把未能直接访问的 Kraus 原 PDF 当作已读。

[Freitas 刊本](https://ems.press/content/serial-article-files/43415?nt=1)，
[DOI 10.4171/CMH/386](https://doi.org/10.4171/CMH/386)；
[Bennett 等作者刊本](https://personal.math.ubc.ca/~bennett/BeChDaYa-IJNT-2015.pdf)，
[DOI 10.1142/S179304211530001X](https://doi.org/10.1142/S179304211530001X)。

**推论。** 族 I、III 的实际解都满足 $W\notin\mathbb Z^3$。

**证明。** 若 $W=w^3$，则 (1) 化为
$$
X^3+(-3w^2)^3=Z^p.
\tag{8}
$$
三个坐标非零，因为原条件 $|Z|>1$ 及两两互素排除了 $X=0$ 或 $W=0$。又 $3\nmid XZ$，且 $(X,w)=(w,Z)=(X,Z)=1$，所以 (8) 是原始解。上述必要条件给 $3\mid Z$，矛盾。证毕。

这排除的是一个全指数的额外整数子族，不是任何整个 $p\equiv3\pmod4$ 的子同余类。族 II 同样代入只得到
$$
X^3+(-3w^2)^3=8Z^p;
$$
不能除以 $8$ 后声称得到三个互素整数。Freitas 的 **Theorem 3** 另排除系数 $1$ 方程的 $p\equiv2\pmod3$，也不能删除这个系数问题。

### 3.4 扭曲两立方和：辅助素数与指数的量词相反

Bennett–Bruni–Freitas，*Sums of two cubes as twisted perfect powers, revisited*，Algebra Number Theory **12** (2018), 959–999，**Theorem 1.4** 对素数 $p,q\ge5$、$p\ge q^{2q}$ 和
$$
a^3+b^3=q^\alpha c_0^p,\quad \alpha>0
$$
的非零互素解，要求 $q$ 属于明确的异常集合 $S_0$。$S_0$ 由导子 $18q,36q,72q$、有理 $2$ 挠点及指定判别式平方类的曲线刻画。**Theorem 1.7** 的结论只覆盖一部分指数；不是全部指数的排除。

[刊本原文](https://msp.org/ant/2018/12-4/ant-v12-n4-p06-s.pdf)，
[DOI 10.2140/ant.2018.12.959](https://doi.org/10.2140/ant.2018.12.959)。

它不覆盖族 II 的系数素数 $q=2$，也不能把 $q$ 换成本题一个变化的分母素数而保持结论。除首先必须把 $27W^2$ 变成立方之外，这种替换还会要求
$$
p\ge q^{2q},
$$
而本题 $q\mid Z$ 已有 $q\ge4p-1>p$，两不相容。文献中“多数辅助素数”或“一部分指数”的密度陈述也没有全称量词。

## 4. CM 同余刚性：Studnia 的小惯性条件在此失效

Studnia，*Congruences modulo 23 to $y^2=x^3-23$ are trivial*，arXiv:2507.20801v2（2025-09-30），**Theorem A** 固定参考曲线 $y^2=x^3-23$ 和素数 $23$。**Theorem B** 要求特征素数处的惯性像严格小于非分裂 Cartan $C$，再在一个 Rankin–Selberg 中心值非零的条件下构造秩零商。引言 **Theorems C、D** 的整性接口继续处于这个小惯性设定。**Theorem E** 的参考族是 $y^2=x^3+p^2$（$p\equiv2\pmod9$）或 $y^2=x^3+p$（$p\equiv5\pmod9$）的二次扭曲，不能换成固定 $A$。

[作者原文与精确定理](https://arxiv.org/html/2507.20801v2)，
[版本记录](https://arxiv.org/abs/2507.20801)。

对本题 $A$，$p>37$、$p\equiv3\pmod4$ 时在 $p$ 处好超奇异。其惯性作用在 $\mathbb F_{p^2}$ 上由二级基本特征 $\omega_2$ 给出：
$$
\left.\bar\rho_{A,p}\right|_{I_p}\otimes\mathbb F_{p^2}
\simeq
\begin{pmatrix}
\omega_2&0\\0&\omega_2^p
\end{pmatrix}.
$$
$\omega_2(I_p)=\mathbb F_{p^2}^{\times}$，故惯性像就是整个 $C$，指数为 $1$。残余模同构使 $E$ 的惯性像同样大。因此即使 $p$ 落在 $2$ 或 $5\bmod9$，仍不满足该论文用于整性的关键假设。

该文引言还解释了参考曲线在 $p$ 好约化时相关 $L$ 函数中心强制消失的障碍；将其解释成正秩需要 BSD，不能在本文升级为无条件的“所有商均无秩零”定理。本轮没有取得一个可用于固定 $A$、所有足够大 $p\equiv3\pmod4$ 的新 CM 同余刚性定理。

## 5. 一般二次范数分解：域随 Z 变化，立方类就是 R46

以下完全展开代数，不把形式因式分解视为独立下降。

记
$$
a=cZ^p,\qquad d=\operatorname{sf}(cZ),\qquad
K=\mathbb Q(\sqrt d),\qquad
L=\mathbb Q(\sqrt{-3d})=\mathbb Q(\sqrt{-3cZ}),
$$
并令
$$
\alpha=27W+\sqrt{-27a}
=27W+3Z^{(p-1)/2}\sqrt{-3cZ}.
\tag{9}
$$
选择平方根的相反号只会交换 $\alpha$ 与 $\bar\alpha$。
由 (1)，
$$
\boxed{\alpha\bar\alpha=(3X)^3.}
\tag{10}
$$
因此 $\bar\alpha$ 与 $\alpha^{-1}$ 在 $L^\times/L^{\times3}$ 中相同。

### 5.1 反射域的判别式仍由变化的分母控制

因为 $d$ 平方自由且 $3\nmid d$，$-3d$ 也平方自由，并且 $-3d\equiv d\pmod4$。二次域判别式公式给出精确关系
$$
\boxed{D_L=-3D_K.}
\tag{11}
$$
所以这并没有把 R37 的变化域 $K$ 换成固定判别式的域。

R37 已排除 $Z$ 为正、负平方。对于 $c=1$，$L=\mathbb Q(\sqrt{-3})$ 或 $\mathbb Q(\sqrt3)$ 分别要求 $d=1$ 或 $-1$，都被排除。对于 $c=8$，$d=2\operatorname{sf}(Z)$ 为偶平方自由数，更不可能为 $\pm1$。所以**一般实际解的 (9) 从来不是在这两个固定二次域内进行的分解**。

### 5.2 立方性与三次式有理根的严格等价

令
$$
g(T)=T^3-XT-2W.
$$
则
$$
\boxed{\alpha\in L^{\times3}
\quad\Longleftrightarrow\quad
g\text{ 有有理根}.}
\tag{12}
$$

**证明正向。** 写 $\alpha=s^3$、$s\in L$。由 (10) 和有理数中立方映射的单射性，
$$
s\bar s=3X.
$$
令 $S=s+\bar s\in\mathbb Q$。则
$$
S^3-9XS=s^3+\bar s^3=54W.
$$
所以 $t=S/3$ 满足 $t^3-Xt-2W=0$。

**证明反向。** 设 $t\in\mathbb Q$ 为根。由分解
$$
g(T)=(T-t)(T^2+tT+t^2-X)
$$
及判别式公式，
$$
4a=(3t^2-X)^2(4X-3t^2).
\tag{13}
$$
$a\ne0$，所以 $3t^2-X\ne0$。置
$$
r=\frac{2\sqrt{-3a}}{3t^2-X}\in L,
\qquad s=\frac{3t+r}{2}.
$$
式 (13) 给 $r^2=9t^2-12X$，故 $s\bar s=3X$。再计算
$$
s^3+\bar s^3=54W,\qquad
s^3-\bar s^3=r(9t^2-3X)=6\sqrt{-3a}.
$$
因此 $s^3=27W+3\sqrt{-3a}=\alpha$。证毕。

R37 已证明 $g$ 不可约；所以所有实际解都给出非零类
$$
\boxed{[\alpha]\ne0\ \text{于 }L^\times/L^{\times3}.}
\tag{14}
$$
不能因为 (10) 的范数为立方，就把 $\alpha$ 本身当作立方。

### 5.3 与 R46 的同一性是显式的

写 $p=6k+e$、$e\in\{1,5\}$，并置
$$
a_e=cZ^e,\qquad
P_e=\left(\frac{3X}{Z^{2k}},\frac{27W}{Z^{3k}}\right)
\in D_{a_e}(\mathbb Q),\qquad
D_{a_e}:V^2=U^3-27a_e.
$$
[R46](../results/R46-cubic-selmer-and-mordell-weil-sieve.md) 使用
$$
\phi:B_{a_e}\longrightarrow D_{a_e},\qquad
B_{a_e}:y^2=x^3+a_e.
$$
其实际 Kummer 类的三点 torsor 由
$$
T^3-\frac{U}{3}T-\frac{2V}{27}
=Z^{-3k}g(Z^kT)
\tag{15}
$$
给出。而二次域中的通常立方坐标为
$$
V+\sqrt{-27a_e}
=\frac{\alpha}{Z^{3k}},
\tag{16}
$$
与 $\alpha$ 相差一个立方。

这里也可以不援引任何坐标公式来检查同一性。在 $L$ 上，$s^3=\alpha$ 的三个根经
$$
s\longmapsto\frac{s+3X/s}{3}
\tag{17}
$$
给出 $g$ 的三个根。代入即可验证；两根重合会迫使 $a=0$，所以这是三点集合的 Galois 等变双射。R46 的核模为 $\mathbb F_3(\chi_d)$；在 $L$ 上 $\chi_d=\chi_{-3}$，故它成为 $\mu_3$，与 (17) 的立方 torsor 一致。限制到次数 $2$ 的扩张对三阶上同调类是单射，因为限制再核限制是乘 $2$。

所以 (9)–(16) 是 R46 同一个 Kummer 类的二次 Kummer 坐标。改变平方根或核生成元至多把类取逆，不会改变非零性、有理点存在性或该路线的全局缺口。

## 6. 理想赋值：普通分支与射线分支不能混淆

这些赋值给可核查的类群条件，但不消灭 (14)。

### 6.1 奇素数

$\alpha$ 是 $L$ 中的代数整数。若奇素数 $q\ne3$ 整除 $X$，则 $q\nmid WZ$。因此 $q$ 在 $L$ 中不分歧，而且任何同时整除 $\alpha$ 与 $\bar\alpha$ 的素理想都会整除
$$
\alpha+\bar\alpha=54W,
$$
与 $q\mid X$ 矛盾。该 $q$ 不能惰性，因为惰性素理想被共轭固定。所以 $q$ 分裂，并且位于 $q$ 之上的非零赋值恰为
$$
3v_q(X).
$$
若 $q\nmid3X$，(10) 使全部对应赋值为零。

在 $3$ 处，$3\nmid cZX$，而 $3$ 在 $L$ 中分歧。以 $v_{\mathfrak p_3}(3)=2$ 归一化，则
$$
v_{\mathfrak p_3}(\sqrt{-27a})=3,\qquad
v_{\mathfrak p_3}(27W)\ge6.
$$
所以
$$
v_{\mathfrak p_3}(\alpha)=3.
\tag{18}
$$
所有奇素理想处的赋值均被 $3$ 整除。

### 6.2 普通分支

普通分支 I、II、III 奇 $X$ 中，$X$ 奇，所以 (10) 的范数为奇数。结合上节，
$$
\boxed{(\alpha)=\mathfrak a^3}
\tag{19}
$$
对某个整理想 $\mathfrak a$ 成立。

若还有 $Z>0$，则 $L$ 为虚二次域。$3$ 在 $L$ 中分歧，故 $L\ne\mathbb Q(i)$；第 5.1 节又排除 $L=\mathbb Q(\sqrt{-3})$，所以其单位只有 $\pm1$，全都是立方。若 $\mathfrak a$ 主，则 (19) 使 $\alpha$ 为单位乘立方，即为立方，违反 (14)。因此
$$
\boxed{Z>0,\ X\text{ 奇}\Longrightarrow
[\mathfrak a]\text{ 的阶恰为 }3,\quad 3\mid h(L).}
\tag{20}
$$
这是同一下降类的理想类表达，不是一个证明所有这些虚二次类群三部分都为零的新定理。

若 $Z<0$，$L$ 为实二次域。即使 $\mathfrak a$ 主，也只能写
$$
\alpha=\varepsilon\beta^3,
$$
其中单位 $\varepsilon$ 可能不是立方。不能在这一分支从 (14)、(19) 推出 $3\mid h(L)$。

### 6.3 III 偶 X 的射线分支

这里 $c=1$，R19/R25 给 $v_2(X)=1$、$W$ 奇、$Z\equiv5\pmod8$。于是
$$
-3Z\equiv1\pmod8,
$$
$2$ 在 $L$ 中分裂。写 $(2)=\mathfrak p\bar{\mathfrak p}$。两个二进嵌入下 $\alpha$ 都是奇数加奇数，所以赋值至少为 $1$；(10) 的范数赋值为 $3$，故两赋值恰为 $1,2$。交换名字后，
$$
\boxed{(\alpha)=\mathfrak p\bar{\mathfrak p}^{\,2}\mathfrak a^3.}
\tag{21}
$$
特别地
$$
0=[\mathfrak p]+2[\bar{\mathfrak p}]+3[\mathfrak a]
=-[\mathfrak p]+3[\mathfrak a],
$$
从而
$$
\boxed{[\mathfrak p]\in3\operatorname{Cl}(L).}
\tag{22}
$$
这对两种 $Z$ 符号都成立；取共轭不改变三可除性。若 $3\nmid h(L)$，(22) 自动成立，因而不能一律视作排除。也不能把 (21) 误写成 (19)，从而错误地把普通类群论证移到射线分支。

(20)、(22) 都来自 R46 的实际类的同一坐标。它们可用于核对固定参数计算，本文没有证明其总与 R37/R46 的条件冲突。

## 7. 固定二次域只出现在 X 为正、负平方的子族

一般 $X^3$ 不是有理平方。因而
$$
(X^{3/2}+3\sqrt3\,W)(X^{3/2}-3\sqrt3\,W)
$$
不是一个在固定 $\mathbb Q(\sqrt3)$ 中的合法通用分解。下面检查真正能这样做的子族。

族 II 有 $X\equiv3\pmod8$，所以 $X$ 既不是正平方，也不是负平方。III 偶 $X$ 的 $v_2(X)=1$ 也排除这两种情况。余下只有：

| 额外形状 | 可能的 R19 分支 | 固定域与范数分解 |
|---|---|---|
| $X=s^2$ | I，$s$ 奇 | $N_{\mathbb Q(\sqrt3)/\mathbb Q}(s^3+3W\sqrt3)=Z^p$ |
| $X=-s^2$ | III 奇 $X$，$s$ 奇，且 $Z<0$ | $N_{\mathbb Q(\sqrt{-3})/\mathbb Q}(s^3+3W\sqrt{-3})=|Z|^p$ |

两行都有 $sW\ne0$、$(s,W)=1$、$3\nmid s$、$W$ 偶、范数与 $6$ 互素。记表中元素为 $\beta$。若素理想同时整除 $\beta,\bar\beta$，其下方素数在 $2,3$ 之外就要同时整除 $s,W$；而 $2,3$ 已由范数排除。因此两主理想互素。

两个固定二次域均有类数 $1$：Minkowski 的理想类代表范数界分别为 $\sqrt{12}/2<2$ 和 $2\sqrt3/\pi<2$。由互素性及范数为 $p$ 次幂，每个主理想中全部素理想赋值都被 $p$ 整除，遂有
$$
\beta=\varepsilon\gamma^p
\tag{23}
$$
其中 $\gamma$ 是该二次域的代数整数，$\varepsilon$ 为单位。

### 7.1 实二次域的单位参数不能丢掉

在 $\mathbb Q(\sqrt3)$ 中，
$$
\mathcal O^\times=\{\pm(2+\sqrt3)^n:n\in\mathbb Z\}.
$$
这里 $\mathcal O=\mathbb Z[\sqrt3]$；范数 $-1$ 被模 $3$ 排除，而最小的大于 $1$ 的正单位是 $2+\sqrt3$，故它生成去掉符号后的单位群。
因为 $p$ 奇，可以吸收符号；把单位指数按 $p$ 约化，只能得到
$$
s^3+3W\sqrt3=(2+\sqrt3)^r\gamma^p,
\qquad 0\le r<p,\qquad N\gamma=Z.
\tag{24}
$$
不能不经证明把 $r$ 设为 $0$。单位群的 $p$ 次幂商有阶 $p$，并未被类数 $1$ 消除。即便固定 $r$，$\gamma$ 仍随 $Z$ 变化，其迹的立方条件还没有得到统一排除。

### 7.2 虚二次域消除单位后，移动的种子仍然存在

在 $\mathbb Q(\sqrt{-3})$ 中，单位群阶为 $6$；$p>37$ 与 $6$ 互素，所以可把单位完全吸收到 $\gamma$，得到
$$
s^3+3W\sqrt{-3}=\gamma^p,\qquad N\gamma=|Z|.
\tag{25}
$$
这一步确实比 (24) 没有单位参数。但它留下
$$
\gamma^p+\bar\gamma^p=2s^3
\tag{26}
$$
这个变化代数整数 $\gamma$ 的迹为立方问题。$\gamma$ 不可能有理，否则 (25) 强迫 $W=0$。因此不能把 (26) 当作 Darmon–Merel 在有理整数上的 $(p,p,3)$ 方程。

两行的互素范数还要求每个 $q\mid Z$ 都在相应固定二次域中分裂。这也能直接从方程模 $q$ 的二次剩余条件读出；它没有限制这些分裂素数的大小或个数。固定数域并不等于固定分母支撑。对于 (25)，即使用 Lucas 序列语言，底数 $\gamma$ 随解变化，出现新的素因子也不与允许变化的 $s,W,Z$ 矛盾；本文没有借用一个不存在的统一原始除子矛盾。

## 8. 留下的精确缺口

本轮可核验的文献没有给出覆盖 R19 三族全部实际解的一个新的 $p\equiv3\pmod4$ 子同余类排除。可直接使用的是 (4)、(8) 的立方形状排除，以及 (19)–(25) 的精确分解接口。

一般二次分解需要控制的仍是 R46 的
$$
V\cap\delta\bigl(D_{cZ^e}(\mathbb Q)/\phi B_{cZ^e}(\mathbb Q)\bigr),
\qquad e\in\{1,5\},
$$
及通过这个交空间后 R42 要求的原始整数指标点。既没有证明这个交空间对所有变化 $Z$ 为零，也没有证明它的非零类无法在所有足够大的 $p$ 达到规定指标。

固定支撑的有效上界仍可用 [R34](../results/R34-primitive-depth-and-effective-support-bounds.md)，但其参数 $R=\operatorname{rad}(|Z|)$ 不受上述分解的绝对上界约束。把 (4)、(6) 等下界与一个依赖 $R$ 的上界放在一起，并不封闭成绝对指数界。要解决本接口，仍须对变化的 Kummer/Mordell–Weil 类或原始指标施加一个真正的统一全局限制。

