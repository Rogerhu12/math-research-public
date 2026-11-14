# R24：四次 CM 参数的奇素因子、精确导子与判别式刚性

日期：2026-11-12。状态：**已证明的必要条件；中间进展**。

本结果继续 R21 的实际四次 CM 同余归约。它把可变参数的全部奇素因子与 $j-1728$ 的实际约分分子联系起来，包含素数 $3$ 和残余特征 $p$；并给出精确导子。这里没有证明参数或分母的统一上界。

## 1. 陈述

设 $p>37$、$p\equiv7\pmod{12}$，$E/\mathbb Q$ 无 CM，且模 $p$ 像为完整非分裂 Cartan 正规化子，商二次域为 $K=\mathbb Q(i)$。则存在 $E$ 的一个有理二次扭曲 $E_0$ 和一个非零、有符号的平方自由整数 $d$，使
$$
E_0[p]\simeq A_d[p],\qquad A_d:y^2=x^3-dx.
\tag{24.1}
$$
写实际约分的 $j$ 不变量为
$$
j(E)=\frac{A^3}{B^p},\qquad
A\in\mathbb Z\setminus\{0\},\ B\in\mathbb Z_{>0},\quad (A,B)=1.
\tag{24.2}
$$
记
$$
n=A^3-1728B^p\ne0,
\qquad T=\{q:q\mid B\},
\qquad m=\prod_{\substack{q\mid d\\q\text{ 奇}}}q.
$$
$n$ 正是 $j-1728$ 的约分分子。以下结论成立。

**参数与整数方程。** 对每个奇素数 $q$，包括 $3,p$，
$$
\boxed{v_q(n)\equiv v_q(d)\pmod2.}
\tag{24.3}
$$
因此存在 $\epsilon\in\{\pm1\}$、$\alpha\in\{0,1\}$ 和非零整数 $Z$，使
$$
\boxed{A^3-1728B^p=\epsilon 2^\alpha dZ^2.}
\tag{24.4}
$$
还具有
$$
v_2(A)\in\{1,2,3\},\quad 3\mid A,\quad 6\mid Z,
\quad (B,6dp)=1,\quad p\nmid A,
\tag{24.5}
$$
以及每个 $q\ge5$、$q\mid d$ 都满足 $q\nmid A$。换言之，除 $2$ 和符号外，参考四次扭曲参数的平方类由 $j$ 本身决定。

**精确导子。** 令 $f_2(d)=v_2(N_{A_d})$，即这条明确的 CM 曲线在 $2$ 处的导子指数。则
$$
\boxed{N_{E_0}=N_{A_d}\prod_{q\in T}q
=2^{f_2(d)}m^2\prod_{q\in T}q.}
\tag{24.6}
$$
对奇素数，$E_0$ 在 $q\mid d$ 处为温和潜在好约化，惯性阶为 $4$、导子指数为 $2$；在 $q\in T$ 处为乘法约化；其余奇素数处好约化。特别地，在 $p$ 处
$$
v_p(\Delta_{E_0}^{\min})=
\begin{cases}0,&p\nmid d,\\3,&p\mid d.\end{cases}
\tag{24.7}
$$

**分母素数。** 每个 $q\in T$ 满足
$$
q\equiv\chi_{-4}(q)\pmod p,
\qquad q\equiv\pm1\pmod{4p},\qquad q\ge4p-1.
\tag{24.8}
$$
如果 $q\equiv1\pmod4$，则进一步有
$$
\boxed{q\ge 2p^2-2p+1.}
\tag{24.9}
$$
这里不能沿用固定 $A_1$ 时的 $4p^2+1$ 下界，因为一般 $A_d$ 没有全有理 $2$ 挠点。

**整 $j$ 情形的参数下界。** 令
$$
\mathcal B(N)=\left\lfloor
\frac{[\mathrm{SL}_2(\mathbb Z):\Gamma_0(N)]}{6}
\right\rfloor.
$$
如果 $B=1$，则实际非 CM 曲线必须满足
$$
\boxed{p^2\le16\mathcal B(N_{A_d}).}
\tag{24.10}
$$
这个结论也允许 $p\mid d$。因此有界的参考参数不能承载整 $j$、$p\to\infty$ 的非 CM 同余曲线；但 $d$ 未被统一控制，(24.10) 本身不排除全部曲线。

## 2. 一个独立的局部引理：$p$ 处的最小判别式完全一致

**引理 24.1。** 设 $p>13$，$U,V/\mathbb Q_p$ 均潜在好约化，且 $U[p]\simeq V[p]$。则
$$
v_p(\Delta_U^{\min})=v_p(\Delta_V^{\min}).
\tag{24.11}
$$
特别地，它们的 Kodaira 型相同。

**证明。** 因 $p>3$，两曲线在最大非分歧扩张之上的最小好约化分歧次数分别属于 $\{1,2,3,4,6\}$。在一个足够大的有限非分歧基扩张后，取共同的温和 Galois 好约化扩张 $L$。其绝对分歧指数可取为这两个次数的最小公倍数，故
$$
e(L/\mathbb Q_p)\le12<p-1.
$$
可进一步严格 Hensel 化；这不改变 $e$。

Raynaud 全忠实性使一般纤维同构唯一延拓为好约化模型上有限平坦群概形的同构
$$
\mathcal U[p]\simeq\mathcal V[p].
$$
唯一性保证该同构与惯性的下降作用相容。特殊纤维上 $[p]$ 的微分为零，故两边的 Lie 空间分别是好约化特殊纤维的一维 Lie 空间。于是惯性作用于这两个一维空间的特征相同。

设 $\delta_U=v_p(\Delta_U^{\min})$。取定义在基域上的极小不变微分 $\omega_U$，以及好约化模型上的极小不变微分 $\omega_{U,L}$。坐标变换公式给
$$
\omega_{U,L}=u_U\omega_U,
\qquad v_L(u_U)=\frac{e\delta_U}{12}.
$$
令温和惯性生成元 $\sigma$ 满足 $\sigma(\pi_L)=\zeta_e\pi_L$。单位的 $\sigma$ 比值约化为 $1$，所以在特殊纤维上，微分的下降特征为
$$
\overline\zeta_e^{\,e\delta_U/12}.
$$
对 $V$ 同理。Lie 特征相等等价于它们的对偶微分特征相等，故
$$
\frac{e(\delta_U-\delta_V)}{12}\equiv0\pmod e,
\qquad\text{即}\qquad \delta_U\equiv\delta_V\pmod{12}.
$$

最后，在剩余特征 $>3$ 的极小短 Weierstrass 模型上，潜在好约化意味着 $0\le\delta<12$：若 $\delta\ge12$，$j$、$j-1728$ 的整性分别给 $v(c_4)\ge4$、$v(c_6)\ge6$，因 $2,3$ 为单位便可用均匀化参数缩放，违反极小性。因此模 $12$ 同余已是相等；常规潜在好约化的判别式赋值表给相同 Kodaira 型。证毕。

这个论证比较的是有限平坦群概形及其下降 Lie 作用，不能用一般的模 $p$ 惯性半单化直接替代。

## 3. 温和惯性与判别式奇偶性

需要一个同时覆盖 $q=3$ 的事实。设 $W/\mathbb Q_q$ 潜在好约化，在最大非分歧扩张之上的最小好约化扩张温和、分歧次数为 $e$。与上节相同的微分计算表明，惯性对好约化特殊纤维微分的特征为
$$
\zeta_e^{e v_q(\Delta_W^{\min})/12}.
\tag{24.12}
$$
其阶恰为 $e$。理由是惯性在特殊纤维上的作用忠实，而阶与 $q$ 互素的保原点自同构若在切空间上平凡，则其本身平凡：在形式参数上取第一个非零高次项，迭代到自同构的阶后该系数被乘以一个非零整数，产生矛盾。因此
$$
\text{$v_q(\Delta_W^{\min})/12$ 的既约分母为 $e$。}
\tag{24.13}
$$
特别地，$e=4$ 时最小判别式赋值为奇数；$e=1,2$ 时为偶数。这里 $q=3$、$e=4$ 完全属于温和情形，没有遗漏野惯性项。

对 $q\ne p$ 的潜在好约化曲线，有限惯性像的阶至多 $24$。因 $p>37$，约化到 $\mathrm{GL}_2(\mathbb F_p)$ 在该像上忠实，且保留所有惯性固定空间的维数。因此模 $p$ 同构保持惯性核、惯性阶以及包含野部分的 Artin 导子。

## 4. 平方自由归一化及全部奇素数的比较

R21 先给 $E[p]\simeq A_{d'}[p]$，$d'\in\mathbb Q^\times$。写 $d'=dt^2$，其中 $d$ 为有符号平方自由整数、$t\in\mathbb Q^\times$。因为 $A_{d'}$ 是 $A_d$ 的二次扭曲，再对 $E$ 作相应二次扭曲便得 (24.1)。二次扭曲不改变 $j$ 或 Cartan 商域；由 R1 其异常像仍是完整正规化子。

对任意奇素数 $q$，$A_d$ 在 $q\nmid d$ 时好约化；在 $q\mid d$ 时，模型
$$
y^2=x^3-dx,
\qquad \Delta=64d^3
$$
极小，最小判别式赋值为 $3$，并在加入 $d$ 的四次根后取得好约化。其最小好约化惯性阶恰为 $4$，且在所有奇 $q$ 处均温和。

先取 $q\ne p$。若 $E_0$ 潜在好约化，上节的忠实性使它与 $A_d$ 的惯性阶相同：为 $1$ 或 $4$。故其最小判别式赋值的奇偶性正好为 $v_q(d)$。

若 $E_0$ 潜在乘法，R2 给模 $p$ 惯性像至多为标量 $\{\pm I\}$。因此不可能与 $q\mid d$ 时的四阶惯性同构，必有 $q\nmid d$。这时 $A_d[p]$ 不分歧，Tate 二次扭曲特征也不能在惯性上取 $-1$，所以 $E_0$ 已为乘法约化，且 $q\in T$。

再取 $q=p$。R2 保证 $E_0$ 潜在好约化。引理 24.1 直接给 (24.7)，从而在此处同样有
$$
v_p(\Delta_{E_0}^{\min})\equiv v_p(d)\pmod2.
$$

在所有潜在好约化的奇素数处，$B$ 为单位，而
$$
j-1728=\frac{c_6^2}{\Delta}
$$
给出 $v_q(n)\equiv v_q(\Delta)\pmod2$。在潜在乘法处，$q\mid B$，而 $n$ 为单位；刚才已经证明 $q\nmid d$。两种情况合并即证明 (24.3)，含 $q=3,p$。

若 $q\ge5$ 且 $q\mid d$，$E_0$ 的温和惯性阶为 $4$，其 Kodaira 型为 III 或 III$^*$，最小判别式赋值为 $3$ 或 $9$。由 $c_4^3-c_6^2=1728\Delta$ 且 $q\nmid1728$，$v_q(c_4)$ 分别为 $1$ 或 $3$，从而 $v_q(j)=0$，故 $q\nmid A$。

## 5. $2,3$ 的限制与整数方程

因 $p\equiv1\pmod3$，R15 给出 (24.2)，且 $p\nmid AB$。R2 又排除 $2,3$ 出现在 $B$ 中。

商域 $\mathbb Q(i)$ 在 $2$ 分歧。Zywina 的精确分歧支集引理（R20 §2 引用的 Lemma 2.3）因此强迫
$$
v_2(j)\in\{3,6,9\},
$$
即 $v_2(A)\in\{1,2,3\}$。另一方面，$3$ 在 $\mathbb Q(i)$ 惰性；若 $v_3(j)=0$，R20 的显式同 $j$ 好模型检验会强迫 $3$ 分裂，矛盾。既已排除负赋值，便有 $v_3(j)>0$，所以 $3\mid A$。

因此 $v_2(n)\ge3$、$v_3(n)\ge3$。利用 (24.3)，选 $\alpha\in\{0,1\}$ 使
$$
\alpha\equiv v_2(n)-v_2(d)\pmod2,
$$
再选符号 $\epsilon$。则 $n/(\epsilon 2^\alpha d)$ 的全部素数赋值均为非负偶数，故是一个整数平方 $Z^2$；在 $2,3$ 处上述下界还给 $6\mid Z$。这证明 (24.4)、(24.5)。

注意不能将 $d$ 与未经约分的 $j-1728$ 或直接与 $\Delta$ 的平方类混同。分母素数处 $v_q(\Delta)=p\,v_q(B)$ 可以为奇数，而 $q$ 不得整除 $d$。公式 (24.3) 使用实际约分分子正是为消除这个问题。

## 6. 精确导子与分母下界

第 4 节已经给出所有奇素数的约化类型：$q\mid d$ 的温和四阶惯性无非零固定向量，故导子指数为 $2$；$q\in T$ 为乘法约化、指数为 $1$；其余奇素数处好约化。$p$ 处由 (24.7) 分别为好约化或 III 型，导子指数也与 $A_d$ 一致。

$2$ 处两曲线都潜在好约化。模 $p$ 同构对其有限惯性和全部高阶分歧群忠实，因而固定空间维数相同、Artin 导子相同。于是得到 (24.6)，其中 $f_2(d)$ 保留为这条明确曲线的精确局部指数，没有把它错误地一律设为 $5$。

对 $q\in T$，Tate Frobenius 的两个特征值为 $\pm q,\pm1$。R2 迫使 $q\equiv\pm1\pmod p$。$q\equiv1\pmod p$ 时它为标量、商值为 $+1$；$q\equiv-1\pmod p$ 时它有两个不同的 $\mathbb F_p$ 特征值、位于 Cartan 外，商值为 $-1$。与 $\chi_{-4}(q)$ 比较即得 (24.8)。

如果 $q\equiv1\pmod4$，$A_d$ 的 CM Frobenius 是某个
$$
u+vi\in\mathbb Z[i],\qquad u^2+v^2=q,
$$
其迹为 $2u$。四次扭曲只会将标准 Gaussian Frobenius 乘以一个四次单位，所以仍是这个形式。全局同余与 Tate Frobenius 给
$$
u\equiv\pm1\pmod p,\qquad p\mid v.
$$
$v\ne0$，否则素数 $q$ 是平方。$u,v$ 一奇一偶：若 $v$ 为偶数，则 $|v|\ge2p$、$|u|\ge1$；若 $v$ 为奇数，则 $|v|\ge p$，而 $u$ 为偶数且 $u\equiv\pm1\pmod p$，故 $|u|\ge p-1$。两种情况都给 (24.9)。

## 7. 整 $j$ 时的 Sturm 约束

若 $B=1$，(24.6) 给 $N_{E_0}=N_{A_d}=:N$。两条曲线在全部坏素数处都是加性约化，故对应权 $2$、平凡 nebentype 新形式的这些素数系数都为零。对好素数 $q\ne p$，模 $p$ 同构给迹同余。

在 $p$ 处也有精确系数相等：若 $p\mid d$，两曲线均加性，系数为零；若 $p\nmid d$，$A_d$ 好超奇异，引理 24.1 使 $E_0$ 好约化，R15 的潜在超奇异结论使其同样超奇异，因此 $p>3$ 时两者的 $a_p$ 都为零。

假设 $p>4\sqrt{\mathcal B(N)}$。每个好素数 $q\le\mathcal B(N)$ 的 Hasse 界给
$$
|a_q(E_0)-a_q(A_d)|\le4\sqrt q<p.
$$
结合模 $p$ 同余，这些迹必相等。坏素数和 $p$ 处刚才已经处理。Hecke 递推与互素指标的乘法性于是给出全部 $n\le\mathcal B(N)$ 的 Fourier 系数相等。Sturm 界使两个新形式相同，两曲线有理同源，从而 $E_0$ 有 CM，与假设矛盾。取反即得 (24.10)。

这个阈值使用素数系数的 Hasse 界再以 Hecke 递推恢复合数系数，因而是 $4\sqrt{\mathcal B(N)}$，不必采用直接估计全部系数时的较粗阈值 $4\mathcal B(N)$。由于 $p$ 处已单独处理，也没有要求 $p\nmid N$。

## 8. 范围与来源

得到的是实际异常子族必须满足的参数平方类、导子和整数方程，而非可自由拼接的有限窗口条件。但 (24.4) 的 $d$ 仍随 $j$ 变化；(24.10) 只给整 $j$ 情形的参数下界；对 $B>1$ 也只有分母下界。因此没有证明 $p$ 的绝对上界。

- R2、R15、R20、R21：本文引用的全局归约、约分幂次和 $2,3$ 检验。
- M. Raynaud, *Schémas en groupes de type $(p,\ldots,p)$*, Bull. Soc. Math. France **102** (1974), 241–280，[原文](https://www.numdam.org/item/10.24033/bsmf.1779.pdf)，Théorème 3.3.3、Corollaire 3.3.6(1)。引理 24.1 的微分下降比较已完整写出。
- J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques* (1972)，潜在好约化的有限惯性及剩余特征 $>3$ 的温和次数分类；亦见 R15、R21 的已核查引用。
- D. Zywina, *On the surjectivity of mod $\ell$ representations associated to elliptic curves*, Bull. London Math. Soc. **54** (2022), 2404–2417，Lemma 2.3，[作者版](https://pi.math.cornell.edu/~zywina/papers/EffectiveModl.pdf)。这里只用其 $2$ 处商特征分歧的必要条件。
- J. Sturm, *On the congruence of modular forms*, Lecture Notes in Math. **1240** (1987), 275–280：权 $2$ 的消失阶界；相同输入见 R11。特征零模形式对应与有理同源的结论为模性及同源定理的标准应用。
