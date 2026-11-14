# R37：三次下降、精确类群商与平方自由部分的增长

日期：2026-11-12；会话：serre-uniformity-astra-cont/2026-11-12。

**状态：已证明的全局必要条件与部分排除。** 本文从 R19 的实际解构造三次分裂域，给出它在二次预解式域上的完整分歧与指定分裂条件。除一个明确的二进分支外，所得循环三次扩张处处不分歧；特殊分支的导子恰为 $(2)$。这导出类群商、单位和射线类群的真实限制，以及平方自由部分的统一增长下界。本文没有证明这些类群商总为零，因而没有完成固定 CM 整性或主问题。

## 1. 记号与主结论

设 $p>37$，$(X,W,Z)$ 满足 R19 三族之一的全部条件。记相应 Frey 曲线为 $E$，并置
$$
c=
\begin{cases}
1,&\text{族 I、III},\\
8,&\text{族 II}.
\end{cases}
$$
所以
$$
X^3-27W^2=cZ^p,\qquad
g(T)=T^3-XT-2W,\qquad
\operatorname{disc}(g)=4cZ^p.
\tag{37.1}
$$
R19 给出 $E[p]\simeq A[p]$、$A:y^2=x^3-x$，且 $E$ 非 CM。对实际存在的解，R19 还强迫 $p\equiv3\pmod4$。

对非零整数 $n$，定义带符号平方自由部分
$$
\operatorname{sf}(n)=\operatorname{sgn}(n)
\prod_{v_\ell(n)\ {\rm odd}}\ell.
$$
令
$$d=\operatorname{sf}(cZ).$$

**定理 R37。**

1. $g$ 在 $\mathbb Q$ 上不可约，且 $d\ne1$。其分裂域 $H$ 满足
   $$
   \operatorname{Gal}(H/\mathbb Q)\simeq S_3,\qquad
   K=H^{A_3}=\mathbb Q(\sqrt d),\qquad
   \operatorname{Gal}(H/K)\simeq C_3.
   \tag{37.2}
   $$

2. 若为族 I、族 II、或族 III 且 $X$ 奇，则 $H/K$ 在全部有限及无限位都不分歧，而且每个位于 $2Z$ 之上的素理想都在 $H/K$ 中完全分裂。因此，写
   $$
   G_0=
   \operatorname{Cl}(K)/
   \big\langle[\mathfrak q]:\mathfrak q\mid 2Z\big\rangle,
   $$
   必有
   $$
   \boxed{G_0/3G_0\ne0.}
   \tag{37.3}
   $$
   特别地 $3\mid h(K)$。这里使用普通理想类群。

3. 若为族 III 且 $X$ 偶，则 $d\equiv5\pmod8$，素数 $2$ 在 $K$ 中惰性，$H/K$ 恰在唯一的素理想 $(2)$ 处温和全分歧，导子恰为 $(2)$。每个位于 $Z$ 之上的素理想完全分裂。令
   $$
   C=\operatorname{Cl}_{(2)}(K),\qquad
   G=C/\big\langle[\mathfrak q]:\mathfrak q\mid Z\big\rangle,
   \tag{37.4}
   $$
   其中射线模数不含无限位。设 $\overline I$ 为
   $$
   (\mathcal O_K/2\mathcal O_K)^\times\simeq\mathbb F_4^\times
   \longrightarrow C\longrightarrow G
   $$
   的像，则必有
   $$
   \boxed{\overline I\not\subseteq3G.}
   \tag{37.5}
   $$
   尤其每个全局单位都满足
   $$
   \boxed{\varepsilon\equiv1\pmod{2\mathcal O_K}.}
   \tag{37.6}
   $$
   若记 $r_3(B)=\dim_{\mathbb F_3}(B/3B)$，还必有
   $$
   \boxed{r_3(C)=r_3(\operatorname{Cl}(K))+1.}
   \tag{37.7}
   $$
   只要求 $3\mid|C|$ 比 (37.5) 弱，不能替代它。

4. 在第 2 项的处处不分歧分支，令 $D_K$ 为二次域的基本判别式，则
   $$
   \boxed{
   |D_K|\ge
   \begin{cases}
   p^4/64,&K\text{ 为实二次域},\\[2mm]
   \pi^2p^4/1024,&K\text{ 为虚二次域}.
   \end{cases}}
   \tag{37.8}
   $$
   该结论约束的是平方自由部分所定义的域，而不只是 $|Z|$。第 3 项的射线分支不直接使用这个 Minkowski 论证；它有另一个明确的素数见证，见第 7 节。

(37.3) 与 (37.5) 分别是存在具有上述指定分歧、分裂性质的抽象 $S_3$ 扩张的充要类群条件。但它们只是 R19 整数解的必要条件；存在这样的数域，不能反推具有指定系数和判别式的多项式 $g$，更不能反推 Fermat 解。

## 2. 不可约性、二次预解式与循环边界

族 I、II 中，$g$ 就是 $E$ 的 $2$ 除法三次式。族 III 中，实际短方程的三次式是
$$h(T)=T^3-4XT-16W,$$
而
$$h(2T)=8g(T).$$
故三个族中 $g$ 有有理根，当且仅当 $E$ 有非零有理 $2$ 挠点。

若有这样的点，就存在有理循环 $2$ 同源。Lemos 的已发表统一性定理（R8 使用的 Theorem 1.1）将给出 $\bar\rho_{E,p}$ 满射，与 $E[p]\simeq A[p]$ 的 CM 像矛盾。因此 $g$ 无有理根；三次式遂不可约。

不可约三次式的传递 Galois 群只能是 $C_3$ 或 $S_3$。判别式的平方根给出符号特征，所以若 $d\ne1$，便得到 (37.2)。以下排除判别式为有理平方、即 $d=1$ 的边界。

族 II 中 $v_2(cZ)=3$ 为奇数，不可能 $d=1$。族 III 偶 $X$ 时，第 4.2 节将直接给 $Z\equiv5\pmod8$，也不可能为平方。因此假设 $d=1$ 时必落在第 3 节处理的 $X$ 奇分支。

在该分支，第 3 节证明所有可能分歧的有理素数处，局部分解群均至多为 $C_2$。若全局群是 $C_3$，这些局部分解群便只能平凡；其他素数不分歧。因此会得到一个非平凡、处处有限不分歧的循环三次扩张 $H/\mathbb Q$。它不可能在实位分歧，因为复共轭的阶至多为 $2$。这违反 $\mathbb Q$ 的 Hilbert 类域为 $\mathbb Q$，或者直接违反 Minkowski 的无非平凡处处不分歧数域定理。故 $d\ne1$。

## 3. 奇素数、普通二进分支及无穷位

### 3.1 每个奇 q 整除 Z 的地方实际上完全分裂于 H/K

固定奇素数 $q\mid Z$。R19 给 $q\nmid6XW$。模 $q$ 有 $X^3=27W^2$，令
$$r=-3W/X\in\mathbb F_q^\times.$$
则
$$g(T)\equiv(T-r)^2(T+2r)\pmod q.$$
其中简单根 $-2r$ 与重根 $r$ 不同，因为 $q\ne3$。Hensel 引理给一个 $\mathbb Q_q$ 根。

因此 $g$ 的局部分裂域只须再分裂一个二次式，其局部 Galois 群、也就是 $H/\mathbb Q$ 的分解群 $D_q$，至多为阶 $2$。在 $S_3$ 中
$$D_q\cap A_3=1.$$
这不只排除 $3$ 分歧：它说明 $H/K$ 在每个位于 $q$ 之上的素理想处的整个分解群都是平凡的，即这些素理想完全分裂。

这个证明没有假定 $v_q(Z)$ 为奇数。若其为偶数，$q$ 可能不在二次域 $K$ 中分歧，但上述完全分裂仍成立。

### 3.2 X 奇时素数 2 的处理

当 $X$ 奇时，
$$g(0)\equiv0\pmod2,\qquad g'(0)=-X\not\equiv0\pmod2.$$
故 $g$ 在 $\mathbb Q_2$ 中有一个根。与上一节相同，$D_2$ 至多阶 $2$，所以每个位于 $2$ 之上的素理想均在 $H/K$ 中完全分裂。

这覆盖族 I、族 II、族 III 奇 $X$，无须把潜在好约化的惯性群错误地直接约化成 $2$ 挠点惯性群。这里直接处理三次多项式，避免了剩余特征为 $2$ 的这种混淆。

### 3.3 所有其他有限位

若 $\ell\nmid2Z$，则
$$\ell\nmid\operatorname{disc}(g)=4cZ^p.$$
因此 $g$ 的分裂域在 $\ell$ 处不分歧；例如 $\mathbb Z_\ell[T]/(g)$ 为有限 étale 代数，其所有根都落在最大非分歧扩张中。这也包括素数 $3$，因为 $\gcd(Z,3)=1$ 且 $c$ 无因子 $3$。

于是，当 $X$ 奇时，$H/K$ 在所有有限处不分歧。

### 3.4 无穷位与普通、窄类群

若 $Z>0$，则 $\operatorname{disc}(g)>0$，实三次式 $g$ 有三个不同的实根。因此 $H$ 全实，$K$ 的两个实位都在 $H$ 中保持实，亦即完全分裂。

若 $Z<0$，则 $K$ 为虚二次域，没有需要检查的实位。故本文得到的扩张在全部有限及无限位不分歧，对应普通类群。

也可从 $\operatorname{Gal}(H/K)=C_3$ 直接看出：实位若分歧，局部扩张只能为 $\mathbb C/\mathbb R$、其阶为 $2$，不可能出现于次数为 $3$ 的 Galois 扩张。普通与窄类群间的差别是 $2$ 群，虽不影响 $3$ 部分，本文仍已直接检查无穷位，未省略这一条件。

## 4. 唯一的二进分歧分支

### 4.1 对二次基本判别式的准确记录

写 $d_0=\operatorname{sf}(Z)$。由于 $Z$ 为奇数，去掉平方因子不改变其模 $4$ 或模 $8$ 剩余类。因而各分支有：

| 分支 | 二次域 $K$ | 基本判别式 $D_K$ |
|---|---|---|
| I | $\mathbb Q(\sqrt{d_0})$，$d_0\equiv1\pmod4$ | $d_0$ |
| II | $\mathbb Q(\sqrt{2d_0})$ | $8d_0$ |
| III，$X$ 奇 | $\mathbb Q(\sqrt{d_0})$，$d_0\equiv3\pmod4$ | $4d_0$ |
| III，$X$ 偶 | $\mathbb Q(\sqrt{d_0})$，$d_0\equiv5\pmod8$ | $d_0$ |

I、III 奇分支的模 $4$ 条件直接来自 R19 方程；II 中 $\operatorname{sf}(8Z)=2d_0$。这些都是带符号的等式，负 $Z$ 不作额外取正。表中已经排除了第 2 节的 $d=1$ 边界。

### 4.2 偶 X 时的局部分裂域

在族 III 偶 $X$ 中，$W$ 奇，故
$$g(T)=T^3-XT-2W$$
是 $2$-Eisenstein 多项式。它在 $\mathbb Q_2$ 上不可约，所定义的三次局部扩张完全分歧，分歧次数为 $3$，因而是温和分歧。

方程模 $8$ 给出
$$
Z^p\equiv -27W^2\equiv5\pmod8.
$$
所有奇数的平方模 $8$ 为 $1$，而 $p$ 奇，所以
$$Z\equiv5\pmod8,\qquad d=d_0\equiv5\pmod8.$$
因此 $K_2/\mathbb Q_2$ 为非分歧二次扩张，$2\mathcal O_K$ 是素理想，剩余域为 $\mathbb F_4$。

局部分裂域的群是传递子群；其判别式平方类 $d$ 在 $\mathbb Q_2$ 中非平方，所以群为 $S_3$。其二次子域是 $K_2$，而三次子扩张已经具有分歧次数 $3$。于是局部分裂域具有分歧次数 $3$、剩余次数 $2$，从而 $H/K$ 在 $(2)$ 处温和全分歧，次数恰为 $3$。

非平凡温和阿贝尔扩张的局部导子指数为 $1$；结合第 3.1、3.3、3.4 节，全球导子恰为
$$\mathfrak f(H/K)=2\mathcal O_K,$$
且在无限位不分歧。这证明第 1 节第 3 项关于域的全部断言。

## 5. 类群商、射线惯性和单位条件

### 5.1 处处不分歧分支

Artin 互反给满射
$$\operatorname{Cl}(K)\twoheadrightarrow\operatorname{Gal}(H/K)\simeq C_3.$$
第 3 节中完全分裂的素理想，其 Artin 符号都为零。因此此映射经过 $G_0$，得到 (37.3)。

反过来，如果某个二次域及指定素理想集合给出 $G_0/3G_0\ne0$，选一个非零线性泛函
$$G_0/3G_0\longrightarrow\mathbb F_3.$$
类域论产生一个处处不分歧且指定素理想完全分裂的循环三次扩张。

它自动在 $\mathbb Q$ 上 Galois，且群为 $S_3$。因为二次共轭 $\sigma$ 在普通类群上取逆：
$$[\mathfrak a][\sigma\mathfrak a]=[(N\mathfrak a)]=1.$$
故所选指数 $3$ 子群在 $\sigma$ 下稳定，类域在 $\mathbb Q$ 上正常；$\sigma$ 对 $C_3$ 的作用为非平凡的取逆作用，所得阶 $6$ 群是 $S_3$。这只证明所需数域存在的等价条件，不产生 Fermat 解。

### 5.2 射线分支：必须有一个仍看得见惯性的 C3 商

在偶 $X$ 分支，取有限模数 $\mathfrak m=(2)$。Artin 互反给
$$C=\operatorname{Cl}_{(2)}(K)\twoheadrightarrow C_3,$$
并且该映射在局部惯性像
$$I=\operatorname{im}\bigl((\mathcal O_K/(2))^\times\to C\bigr)$$
上非零，因为 $H/K$ 在 $(2)$ 确实分歧。它杀掉所有位于 $Z$ 之上的素理想类，故经过 $G$，并在 $\overline I$ 上非零。

任何映射 $G\to C_3$ 都经过 $G/3G$。所以这样一个映射存在，当且仅当 $\overline I$ 在 $G/3G$ 中有非零像，即 (37.5)。这是完整的有限阿贝尔群判据。

反方向同样由类域论成立：若 (37.5) 成立，选一个在 $\overline I$ 上非零的 $\mathbb F_3$ 线性泛函，所得循环三次层在 $(2)$ 真实分歧、在指定其他素理想处完全分裂，且导子恰为 $(2)$。它也在 $\mathbb Q$ 上给出 $S_3$ 扩张。理由是对与 $(2)$ 互素的理想 $\mathfrak a$，
$$\mathfrak a\,\sigma\mathfrak a=(N\mathfrak a),$$
而 $N\mathfrak a$ 是奇整数，所以 $N\mathfrak a\equiv1\pmod{2\mathcal O_K}$。故二次共轭在整个 $C$、继而在 $G$ 上仍取逆。

### 5.3 为什么单位必须全部模 2 为 1

射线类群的标准正合列在这里为
$$
\mathcal O_K^\times
\longrightarrow\mathbb F_4^\times
\longrightarrow C
\longrightarrow\operatorname{Cl}(K)
\longrightarrow0.
\tag{37.9}
$$
中间的 $\mathbb F_4^\times$ 是阶 $3$ 群。如果任何全局单位的模 $2$ 像不等于 $1$，该单位已经生成整个 $\mathbb F_4^\times$，那么 $I=0$。这与真实的三次惯性矛盾。因此所有单位必须模 $2$ 为 $1$，证明 (37.6)。

此条件**不需要**假设 $3\nmid h(K)$。它在类数含有 $3$ 因子时也同样必要。

在 (37.6) 成立时，(37.9) 化为
$$0\longrightarrow I\simeq C_3\longrightarrow C
\longrightarrow\operatorname{Cl}(K)\longrightarrow0.$$
一个在 $I$ 上非零的 $C_3$ 商存在，当且仅当 $I\not\subseteq3C$。取模 $3$ 后，核的维数为 $1$ 或 $0$，因而该条件等价于 (37.7)。实际扩张满足更强的 (37.5)，故必满足它。

例如若抽象正合列为
$$0\longrightarrow C_3\longrightarrow C_9\longrightarrow C_3\longrightarrow0,$$
则每个 $C_9\to C_3$ 都杀掉这个阶 $3$ 核。虽然射线类数被 $3$ 整除，却没有该核上非零的三次商。这说明为何“射线类群有 $3$ 部分”不够。

### 5.4 一个明确的实二次单位排除

若 $d>0$，取实二次域 $K$ 的基本单位 $\varepsilon$。因 $\mathcal O_K^\times=\{\pm\varepsilon^n\}$ 且 $-1\equiv1\pmod2$，(37.6) 等价于
$$\varepsilon\equiv1\pmod2.$$
在 $\mathbb F_4$ 上，共轭是平方映射。单位的剩余类 $u$ 满足
$$
\operatorname{Tr}_{K/\mathbb Q}(\varepsilon)\bmod2=u+u^2.
$$
对 $u\in\mathbb F_4^\times$，右侧为零当且仅当 $u=1$。所以 (37.6) 又等价于
$$\operatorname{Tr}_{K/\mathbb Q}(\varepsilon)\ \text{为偶数}.$$

特别地，若正平方自由数 $d$ 可写为
$$d=n^2+4\quad\text{或}\quad d=n^2-4,\qquad n\text{ 奇},
$$
其中第二种取 $n\ge3$，则
$$\eta=(n+\sqrt d)/2$$
是范数 $-1$ 或 $+1$ 的全局单位，且迹为奇数 $n$。故这些 $d$ 不可能出现在族 III 偶 $X$ 的实际解中。这里不需要证明 $\eta$ 本身就是基本单位。例如 $d=5,13,29,53$ 均被这个理由排除。

若 $d<0$，本题 $\gcd(Z,6)=1$ 排除 $K=\mathbb Q(\sqrt{-3})$，而 $d\equiv5\pmod8$ 排除 $K=\mathbb Q(i)$。所以只有单位 $\pm1$，(37.6) 自动成立；此时仍须检查 (37.5)，不能因为单位筛为空就断言射线层不存在。

## 6. 小素数全裂与 p 的四次方判别式下界

本节先对所有分支给一个 Frobenius 事实，随后只在处处不分歧分支使用 Minkowski。

### 6.1 好素数的小窗口

设 $\ell$ 为奇素数、$\ell\nmid Z$ 且 $\ell\ne p$。两条曲线 $E,A$ 在 $\ell$ 处均好约化，$p$ 挠点同构给
$$a_\ell(E)\equiv a_\ell(A)\pmod p.$$
若
$$\ell<p^2/16,$$
则 Hasse 界给
$$
|a_\ell(E)-a_\ell(A)|\le4\sqrt\ell<p,
$$
所以两迹作为整数相等。$A$ 有全部有理 $2$ 挠点，其奇素数好约化群的阶被 $4$ 整除，故 $a_\ell(A)$ 为偶数。于是 $a_\ell(E)$ 也为偶数。

在 $\mathrm{GL}_2(\mathbb F_2)\simeq S_3$ 中，阶 $3$ 元素的迹为 $1$，而单位元及阶 $2$ 元素的迹为 $0$。所以 $H/\mathbb Q$ 的 $\ell$-Frobenius 阶为 $1$ 或 $2$。限制到 $K$ 后，若阶为 $2$，该素数在 $K/\mathbb Q$ 中惰性，$H/K$ 的相对 Frobenius 是其平方；若阶为 $1$，本来已经平凡。两种情况都说明每个 $\mathfrak l\mid\ell$ 在 $H/K$ 中完全分裂。

### 6.2 残余特征 p 必须另行处理

上一步没有在 $\ell=p$ 使用“好约化迹同余”。R19 给 $p\nmid\Delta_E$，所以 $E$ 在 $p$ 处好约化；$A$ 因 $p\equiv3\pmod4$ 为好超奇异。

$E[p]\simeq A[p]$ 使 $E$ 也超奇异：若 $E$ 普通，其惯性模 $p$ 表示有一维分支，与 $A$ 的二级基本特征给出的不可约惯性模不相容。好超奇异曲线在 $\mathbb F_p$ 上有 $p\mid a_p(E)$，而 $p>3$ 的 Hasse 界使
$$a_p(E)=0.$$
因此模 $2$ 的 Frobenius 迹仍为零；与上一节相同，每个 $\mathfrak p\mid p$ 在 $H/K$ 中完全分裂。这个结论也直接包含在 R13 的好超奇异分析中。

素数 $2$ 和所有 $q\mid Z$ 则已由第 3、4 节独立处理：$q\mid Z$ 总是完全分裂，$2$ 在 $X$ 奇的分支完全分裂，在偶 $X$ 分支真实分歧。

### 6.3 Minkowski 只作用于处处不分歧分支

现在假设 $X$ 奇。因此上述结论合起来说明：所有有理素数
$$\ell<p^2/16$$
之上的素理想都在 $H/K$ 中完全分裂，此外全部位于 $2Zp$ 之上的素理想也完全分裂。

对二次域，Minkowski 定理给每个普通理想类一个整理想代表，范数至多
$$
B_K=
\begin{cases}
\tfrac12\sqrt{D_K},&K\text{ 实},\\[1mm]
\tfrac2\pi\sqrt{|D_K|},&K\text{ 虚}.
\end{cases}
$$
因而普通类群由范数至多 $B_K$ 的素理想生成：将每个上述代表分解成素理想即可。

若 $B_K<p^2/16$，则这些生成素理想下方的有理素数也小于 $p^2/16$。它们的 Artin 符号全部为零，所以整个
$$\operatorname{Cl}(K)\twoheadrightarrow C_3$$
都会是零映射，矛盾。故 $B_K\ge p^2/16$，分别平方即得 (37.8)。

这个证明不把射线类群当作普通类群，也不将 $2$ 处真实分歧的偶 $X$ 分支带入 Minkowski 结论。

### 6.4 分母根与 j 高度的直接推论

在本节的三个分支中，令 $s=1,8,4$ 分别对应族 I、族 II、族 III 奇 $X$。第 4.1 节的表给出
$$
|D_K|=s\,|\operatorname{sf}(Z)|,\qquad
|\operatorname{sf}(Z)|\le\operatorname{rad}(|Z|)\le|Z|.
$$
记 $\gamma=1/64$ 当 $Z>0$，$\gamma=\pi^2/1024$ 当 $Z<0$。于是 (37.8) 给
$$
\boxed{
|\operatorname{sf}(Z)|\ge\frac{\gamma}{s}p^4,\qquad
\operatorname{rad}(|Z|)\ge\frac{\gamma}{s}p^4,\qquad
|Z|\ge\frac{\gamma}{s}p^4.
}
\tag{37.8a}
$$
所以并非只通过把一个固定小素数的赋值变大，就能满足这条增长要求。

三个族的 $j$ 值分别为
$$
j(E)=\frac{1728X^3}{Z^p},\qquad
\frac{216X^3}{Z^p},\qquad
\frac{1728X^3}{Z^p}.
$$
R19 的互素性和 $\gcd(Z,6)=1$ 保证既约分母恰为 $|Z|^p$。因此绝对对数高度满足
$$
\boxed{
h(j(E))\ge p\log|Z|
\ge p\log\left(\frac{\gamma}{s}p^4\right).
}
\tag{37.8b}
$$
这些分支统一可取较弱的系数 $\gamma/s=\pi^2/8192$。它们仍然是下界；与 R34 的依赖 $\operatorname{rad}(|Z|)$ 的上界相容，不能合成为绝对指数界。

### 6.5 一个直接的整数形状排除

实际解的 $Z$ 不可能是正平方或负平方。

族 III 偶 $X$ 已有 $Z\equiv5\pmod8$，直接排除 $\pm$ 平方。族 I、III 奇 $X$ 的模 $4$ 条件分别只可能留下 $Z$ 为正平方、或负平方。前者使 $d=1$，已在第 2 节排除；后者使 $K=\mathbb Q(i)$，其类数为 $1$，违反 (37.3)。

族 II 若 $Z=\pm s^2$，则 $K=\mathbb Q(\sqrt{\pm2})$，类数也为 $1$。这些三个二次类数结论都可直接用 Minkowski：对应基本判别式 $-4,8,-8$ 的 $B_K$ 均小于 $2$，故每个理想类只能由范数 $1$ 的理想代表。于是族 II 同样不可能。

## 7. 射线分支的一个明确素数见证

在族 III 偶 $X$ 中，$d\equiv5\pmod8$，取
$$
\omega=(1+\sqrt d)/2\in\mathcal O_K,\qquad
N_{K/\mathbb Q}(\omega)=(1-d)/4.
$$
这个范数是非零奇整数，$\overline\omega\in\mathbb F_4^\times$ 为阶 $3$ 元素。实际 Artin 特征
$$\chi:C\longrightarrow C_3$$
在局部惯性上非零，故
$$\chi((\omega))\ne0.$$
这里正合列中是否采用相反的 Artin 符号约定只改变符号，不影响非零性。

将主理想 $(\omega)$ 分解成素理想，至少有一个素因子 $\mathfrak l$ 满足 $\chi(\mathfrak l)\ne0$。令 $\ell$ 为其下方有理素数。则：

- $\ell\mid |d-1|/4$，且 $\ell\ne2$；
- $\ell\nmid Z$，因为所有位于 $Z$ 之上的素理想完全分裂；
- $\ell\ne p$，由第 6.2 节；
- $\ell$ 在 $K$ 中分裂：若惰性，唯一素理想就是 $(\ell)$，而奇整数 $\ell\equiv1\pmod2$，其射线类为零；若分歧，则 $\ell\mid d$，却与 $\ell\mid d-1$ 矛盾；
- 第 6.1 节强迫 $\ell\ge p^2/16$。

因此每个此分支的实际解都给出一个满足
$$
\boxed{
\ell\mid\frac{|d-1|}{4},\quad
\ell\nmid2Zp,\quad
\ell\text{ 在 }K\text{ 中分裂},\quad
\ell\ge p^2/16
}
\tag{37.10}
$$
的素数。特别地
$$\boxed{|d-1|\ge p^2/4.}\tag{37.11}$$

若这个见证素数还满足 $\ell\equiv3\pmod4$，则 $a_\ell(A)=0$，只需 $2\sqrt\ell<p$ 就能由迹同余推出 $a_\ell(E)=0$。所以这种见证实际上满足更强的 $\ell\ge p^2/4$。

这是射线分支的独立论证；它没有把 (37.8) 的普通类群界移用于射线群。

## 8. 自然三同源的像恰好对应 Frey 有理 2 挠点

最后说明类群路线与 R32 的“同源放大”路线如何相接。

对任意 $a\in\mathbb Q^\times$，置
$$
B_a:y^2=x^3+a,\qquad D_a:V^2=U^3-27a.
$$
自然三同源为
$$
\phi:B_a\longrightarrow D_a,\qquad
(x,y)\longmapsto
\left(\frac{x^3+4a}{x^2},
\frac{y(x^3-8a)}{x^3}\right).
\tag{37.12}
$$
代入方程可验证该映射；它延拓到光滑射影曲线并把无穷点送到无穷点。第一坐标的极点总次数为 $6$，而 $U$ 在目标上的极点次数为 $2$，故映射次数为 $3$。它是椭圆曲线同源，核为 $O,(0,\pm\sqrt a)$。

**引理 37.1。** 对仿射点 $P=(U,V)\in D_a(\mathbb Q)$，以下等价：
$$
P\in\phi(B_a(\mathbb Q));
\qquad
f_P(T)=T^3-\frac U3T-\frac{2V}{27}
\text{ 有有理根}.
\tag{37.13}
$$

**证明。** 若 $P=\phi(x,y)$ 为仿射，则 $x\ne0$。置 $t=2y/(3x)$，计算
$$
27t^3-9Ut-2V
=\frac y{x^3}\left(8y^2-6(x^3+4a)-2(x^3-8a)\right)=0.
$$
所以 $t$ 是所需有理根。

反过来，给定 $t$，置
$$x=3t^2-U/3,\qquad y=3tx/2.$$
若 $x=0$，则 $U=9t^2$，而 $f_P(t)=0$ 给 $V=-27t^3$，进而 $U^3-V^2=0$，与 $27a\ne0$ 矛盾。因此 $x\ne0$。

暂记 $a'=y^2-x^3$。由定义有
$$
x+\frac{4a'}{x^2}=9t^2-3x=U.
$$
再计算 (37.12) 的第二坐标：
$$
\frac{y(x^3-8a')}{x^3}
=\frac{3t}{2}(3x-2U)
=\frac{27t^3-9Ut}{2}=V.
$$
(37.12) 的方程恒等式给 $V^2=U^3-27a'$。与 $P$ 的方程比较，得到 $a'=a$，所以 $(x,y)\in B_a(\mathbb Q)$ 且其像为 $P$。证毕。

对 R19 的实际解，写
$$p=6k+r,\qquad r\in\{1,5\},\qquad a=cZ^r,$$
并取
$$P=\left(\frac{3X}{Z^{2k}},\frac{27W}{Z^{3k}}\right)\in D_a(\mathbb Q).$$
则
$$f_P(T)=Z^{-3k}g(Z^kT).$$
第 2 节的不可约性和引理 37.1 因而给出
$$\boxed{P\notin\phi(B_a(\mathbb Q)).}\tag{37.14}$$

所以不能仅因为这些 Mordell 曲线有一个自然有理三同源，就把 R19 的实际点当成该同源的有理像，进而套用针对这种像点的更强 prime-power EDS 定理。本文只排除了这个明确的自然三同源像；没有声称任何其他同源或其他意义的放大均不可能。

## 9. 已证边界与来源

这条路线提供真正的全局类群条件，而非再增加一个位置的可解性筛。不过 $K=\mathbb Q(\sqrt{\operatorname{sf}(cZ)})$ 随分母变化，类群商可以非零，单位也可以满足所需条件。判别式下界随 $p$ 增长，与 R34 的依赖支撑上界相容；两者尚不封闭成绝对 $p$ 界。

外部输入及准确范围：

- P. Lemos, *Serre's uniformity conjecture for elliptic curves with rational cyclic isogenies*, Trans. Amer. Math. Soc. **371** (2019), Theorem 1.1，DOI [10.1090/tran/7198](https://doi.org/10.1090/tran/7198)，[作者版本](https://arxiv.org/abs/1702.01985)。这里只用“非 CM 且有有理循环同源时，所有 $p>37$ 的像满射”，不可约性的其余步骤已写出。
- J. S. Milne, *Class Field Theory*, v4.03 (2020)，[作者原文](https://www.jmilne.org/math/CourseNotes/CFT.pdf)，Chapter V, Theorem 1.7 为射线正合列，§3 的互反与存在定理、Example 3.9 为 Hilbert 类域及普通类群，Chapter I §1.9 给温和阿贝尔扩张导子指数。本文已展开所需商群、惯性存活、共轭作用与无限位的推论。
- J. S. Milne, *Algebraic Number Theory*, v3.08 (2020)，[作者原文](https://www.jmilne.org/math/CourseNotes/ANT.pdf)，Theorem 4.3 为 Minkowski 类群代表范数界，Theorem 4.9 为 $\mathbb Q$ 无非平凡处处不分歧扩张。
- V. Mahé, *Prime power terms in elliptic divisibility sequences*, Math. Comp. **83** (2014), 1951–1991，DOI [10.1090/S0025-5718-2013-02790-1](https://doi.org/10.1090/S0025-5718-2013-02790-1)，[机构保存的期刊原文](https://infoscience.epfl.ch/bitstreams/e22b05d1-f9ab-40f4-b4bf-dbd00e6e1d2d/download)。其 §1 明确要求相应点为非平凡有理同源之像，并区分无条件依赖曲线的指标界与依赖 Lang、Hall–Lang 的统一指标界。本文没有把后者当作无条件输入。
- 本仓库 R19、R13、R8、R32 分别提供精确方程与模表示、残余特征处的好超奇异性、有理同源孤立性、正规化 Mordell 点与局部深度背景。

所有新推论的代数、局部与类群论证均在本文件内给出。没有用尚未证明的变指数广义 Fermat 定理。
