# R326：完整全局同余整数与全部 p 次幂层的等价判别

**状态：已证明。** 本文对 R317 保留的实际整数族，构造一个可由有限个好素数精确计算的正整数。它判定同一对曲线的完整全局 $p^n$ 挠点同构，且判定所有 $n$，并非仅比较半单化或任意有限处的局部同构。Sturm 界使用两曲线的实际共同导子，允许 $p\mid N$；所有坏素数（包括 $p$）的 Fourier 系数在两边严格相同。

本条没有给这个整数的素因子以与 $d$ 无关的上界。其有限终止性不能替代本课题仍缺的统一界。

## 1. 实际整数族与同时扭曲

设

$$
a^3+db^3=1,\qquad
a,b\in\mathbb Z,\quad a\ne0,1,\quad b\ne0,
\quad d>0\text{ 为立方自由整数},
\qquad r=1-a^3=db^3.
\tag{326.1}
$$

取下列两种参数之一：

- 偶分支：$4\mid a$，$r\in\mathbb Q_3^{\times3}$，$\varepsilon=-1$；
- 奇分支：$a\equiv1\pmod {32}$，$\varepsilon=1$。

这些是 R317 已证明的必要局部约束；定义本条判别整数时，不预先假设全局模 $p$ 同构存在。令

$$
\begin{aligned}
E=E_{a,b}^{\varepsilon}&:
y^2=x^3+3abd\,x+\varepsilon d(2a^3-1),\\
A=A_d&:y^2=x^3+d.
\end{aligned}
\tag{326.2}
$$

假设 $E$ 无复乘。直接计算给

$$
\Delta(E)=\Delta(A)=-432d^2,\qquad
j(E)=6912a^3db^3\in\mathbb Z.
\tag{326.3}
$$

这里 $\Delta$ 是所写短模型的判别式；在二、三处不冒认它总是极小。对同一个二次扭曲参数 $\beta=-\varepsilon b$，模型恰为

$$
E^{(\beta)}=H_a:
y^2=x^3+3arx-r(2a^3-1),\qquad
A^{(\beta)}=B_a:
y^2=x^3-\varepsilon r.
\tag{326.4}
$$

因二次角色的平方为一，对每个奇素数 $p$ 和每个 $n\ge1$，

$$
E[p^n]\simeq A[p^n]\quad\Longleftrightarrow\quad
H_a[p^n]\simeq B_a[p^n]
\tag{326.5}
$$

都是同一个 $G_{\mathbb Q}$ 的实际模表示同构。后文不会在逐个素数处自由更换全局同构。

## 2. 共同导子与全部坏 Euler 因子

两条曲线在每个有限处潜在好约化，故坏约化只能是加性。若 $q\ge5$，模型判别式赋值为 $2v_q(d)\in\{0,2,4\}$。零赋值给好约化；赋值二、四时模型极小，约化为温和加性潜在好，导子指数为二。

在二、三处，R317 的显式好模型及同一下降给出：对任意辅助素数 $\ell>37$，$H_a[\ell]$ 与 $B_a[\ell]$ 在当地同构。偶分支在三处使用 $r\in\mathbb Q_3^{\times3}$，奇分支在二处使用 $a\equiv1\pmod {32}$。同时扭回 (326.4)，可比较 $E[\ell]$ 与 $A[\ell]$。

这足以比较完整野导子：潜在好约化的有限惯性群阶只含素数二、三，故与 $\ell$ 互素。对每个高阶分歧子群，平均投影的分母在 $\mathbb Z_\ell$ 中可逆，取不变量与模 $\ell$ 约化交换。因而 Artin 的惯性余维项及各 Swan 项全部相等。这里没有先假设实际全局 $p$ 同构来得出共同导子。

由 R258 的完整二、三处计算，设 $d=2^u w$，$u\in\{0,1,2\}$、$w$ 为奇数，记

$$
N=N(E)=N(A)
 =2^\alpha3^\gamma R_d^2,
\qquad R_d=\prod_{\substack{q\ge5\\q\mid d}}q,
\tag{326.6}
$$

则

$$
\alpha=
\begin{cases}
6,&u=1,\\
4,&u=0\text{ 或 }2,\ w\equiv3\pmod4,\\
2,&u=0\text{ 或 }2,\ w\equiv1\pmod4,
\end{cases}
\quad
\gamma=
\begin{cases}
2,&3\nmid d,\ d\equiv\pm1\pmod9,\\
3,&3\nmid d,\ d\not\equiv\pm1\pmod9,\\
5,&v_3(d)=1\text{ 或 }2.
\end{cases}
\tag{326.7}
$$

每个 $q\mid N$ 均是加性坏素数，所以两曲线的当地 Euler 因子均为一，标准系数均为

$$
a_q(E)=a_q(A)=0,\qquad
a_{q^j}(E)=a_{q^j}(A)=0\quad(j\ge1).
\tag{326.8}
$$

特别地，后面考虑的表示素数 $p\mid d$ 满足 $p^2\mid N$，在这里并没有被遗漏；其坏 Euler 因子在两边也严格等于一。

## 3. 原始 Sturm 定理与任意整数模数

由 Breuil–Conrad–Diamond–Taylor 的模性定理及标准的新形式对应，存在归一化新形式

$$
f_E=\sum_{m\ge1}A_m Q^m,\qquad
f_A=\sum_{m\ge1}B_m Q^m
\ \in S_2(\Gamma_0(N)),\qquad
A_m,B_m\in\mathbb Z,
\tag{326.9}
$$

其完整 $L$ 级数分别为两曲线的 $L$ 级数。此处 $Q=e^{2\pi iz}$ 只是展开变量，不是素数。特别地 $A_1=B_1=1$，好素数系数就是整数 Frobenius 迹，坏素数系数满足 (326.8)。

置

$$
\mu(N)=[\mathrm {SL}_2(\mathbb Z):\Gamma_0(N)]
       =N\prod_{q\mid N}\left(1+\frac1q\right),
\qquad
S(N)=\left\lfloor\frac{\mu(N)}6\right\rfloor.
\tag{326.10}
$$

Sturm 原文 Theorem 1（1987，印刷第 276 页）设任意包含主同余子群的 $\Gamma$、任意正整数权 $k$、数域整数环 $R$ 和其中的素理想 $\Lambda$。对 Fourier 系数在 $R$ 中的形式，其结论是

$$
\operatorname {ord}_\Lambda(f-g)>
\frac{k[\mathrm {SL}_2(\mathbb Z):\Gamma]}{12}
\quad\Longrightarrow\quad f\equiv g\pmod\Lambda.
\tag{326.11}
$$

第 275–276 页的定义只要求在无穷尖点的 Fourier 系数属于 $R$；定理没有 $\Lambda\nmid N$ 条件，也没有 $N$ 平方自由的条件。原文后续才研究平方自由新形式的额外改进。本文只用 Theorem 1，取 $\Gamma=\Gamma_0(N),k=2,R=\mathbb Z$，所以允许同余素数整除 $N$。

由此还得到本条需要的素数幂版本，而无需另引用一个未核对的加强：

**引理 326.1。** 对任意整数 $M\ge1$，

$$
A_m\equiv B_m\pmod M\ (1\le m\le S(N))
\quad\Longleftrightarrow\quad
A_m\equiv B_m\pmod M\ (m\ge1).
\tag{326.12}
$$

**证明。** 只需证明 $M=\ell^e$。$e=1$ 时，差形式的常数项为零，前 $S(N)$ 项为零模 $\ell$，故其首个非零模 $\ell$ 系数的位置大于 $\mu(N)/6$，适用 (326.11)。若已知前 $S(N)$ 项被 $\ell^e$ 整除，归纳先知全部系数被 $\ell^{e-1}$ 整除。于是

$$
g=\frac{f_E-f_A}{\ell^{e-1}}\in S_2(\Gamma_0(N))
$$

仍具有整数 Fourier 系数，其前 $S(N)$ 项均为零模 $\ell$。再用 (326.11)，所有系数均为零模 $\ell$，完成归纳。一般 $M$ 逐个素数幂处理。$\square$

## 4. 全部好素数迹差的精确整数 gcd

对好素数 $q\nmid N$ 定义

$$
\delta_q=a_q(E)-a_q(A)\in\mathbb Z,
\qquad
\mathcal D(a,b)=
\gcd_{\substack{q\le S(N)\\q\text{ 素数},\ q\nmid N}}|\delta_q|.
\tag{326.13}
$$

暂约定全为零或空集合的 gcd 为零；下面证明在本文非 CM 假设下不会出现该情形。

好素数的系数递推与互素乘法性为

$$
A_{q^{j+1}}=A_qA_{q^j}-qA_{q^{j-1}},
\qquad
A_{mn}=A_mA_n\quad((m,n)=1),
\tag{326.14}
$$

$B_m$ 同理；坏素数的全部正次幂系数已由 (326.8) 给出。递推表明，任意整数模数 $M$ 下，前 $S(N)$ 个所有系数相等，当且仅当 (326.13) 中各个好素数迹相等。素因子或素数幂不可能大于其乘积的指标，故递推没有超出此窗口。

结合引理 326.1，得到整数理想的严格相等

$$
\begin{aligned}
(\mathcal D)
&=(A_m-B_m:1\le m\le S(N))\\
&=(A_m-B_m:m\ge1)\\
&=(a_q(E)-a_q(A):q\nmid N,\ q\text{ 素数}).
\end{aligned}
\tag{326.15}
$$

这里不仅素因子集合相同，每个素因子的指数也完全相同；这正是引理 326.1 使用任意 $\ell^e$ 的原因。

若 (326.13) 全部为零，则对每个素数 $\ell$，引理 326.1 使所有 $A_m-B_m$ 被 $\ell$ 整除。因此所有系数在 $\mathbb Z$ 中相等。相同归一化新形式给出同一 $\mathbb Q$ 同源类，故 $E$ 与 CM 曲线 $A$ 同源，违背 $E$ 非 CM。于是至少一个窗口中的 $\delta_q$ 非零，且 Hasse 界给

$$
0<\mathcal D(a,b)\le4\sqrt{S(N)}.
\tag{326.16}
$$

本族还有一个无需实际模 $p$ 同构的二次整除。取 $\theta^3=d$，$\theta_i=\zeta_3^i\theta$。$A$ 的三个非零二挠点的横坐标为 $-\theta_i$；$E$ 的对应横坐标为

$$
\varepsilon(-a\theta_i+b\theta_i^2).
\tag{326.17}
$$

代入三次式并用 (326.1) 可直接验证。模型判别式非零，三个根互异；这个双射与 $G_{\mathbb Q}$ 作用交换，所以 $E[2]\simeq A[2]$。因 $2\mid N$，每个好素数均为奇数，两个整数 Frobenius 迹相等模二。故

$$
\mathcal C(a,b)=\mathcal D(a,b)/2\in\mathbb Z_{>0},
\qquad
0<\mathcal C(a,b)\le2\sqrt{S(N)}.
\tag{326.18}
$$

对奇素数 $p$，$v_p(\mathcal C)=v_p(\mathcal D)$。

## 5. 从整个迹系统到实际全部 p 次幂层

下面取本课题实际小惯性分支的素数

$$
p>37,\qquad
\begin{cases}
p\equiv5\pmod9,\quad v_p(d)=1,\\
\text{或 }p\equiv2\pmod9,\quad v_p(d)=2.
\end{cases}
\tag{326.19}
$$

原异常分支还满足 $v_p(b)\ge1$；下述整数判别及矩阵论证本身不需要增加这个条件。两曲线均在 $p$ 加性坏约化，由 (326.6) 有 $p^2\mid N$。

### 5.1 CM 剩余像的矩阵代数

R258 的实际 CM 惯性计算给

$$
\bar\rho_{A,p}(I_p)=C_{\mathrm {ns}}(p)^3.
\tag{326.20}
$$

此群的阶为 $(p^2-1)/3>p-1$，所以它不包含于标量群。在把底层二维空间认作 $\mathbb F_{p^2}$ 后，其 $\mathbb F_p$ 线性包等于乘法代数 $\mathbb F_{p^2}$：任取一个非标量元素，其最小多项式次数为二。

复共轭属于正规化子的外陪集，作用于该域的共轭为 $z\mapsto z^p$。乘法算子与乘法算子后复合 $z\mapsto z^p$ 线性无交，其总维数为四。故

$$
\mathbb F_p[\bar\rho_{A,p}(G_{\mathbb Q})]
=M_2(\mathbb F_p).
\tag{326.21}
$$

特别地，这是绝对不可约的剩余表示。这里不必把 (326.20) 加上复共轭冒认成完整正规化子；(326.21) 已足够。原始问题若另外要求完整正规化子像，该前提照旧保留。

### 5.2 精确等价定理

**定理 326.2。** 在 (326.1)–(326.2)、两种局部分支、非 CM 假设及 (326.19) 下，对每个整数 $n\ge1$，下列四件事等价：

$$
\begin{aligned}
\mathrm{(i)}\quad &p^n\mid\mathcal D(a,b)
                    \quad(\Longleftrightarrow p^n\mid\mathcal C(a,b));\\
\mathrm{(ii)}\quad&
a_q(E)\equiv a_q(A)\pmod {p^n}
\quad(q\le S(N),\ q\text{ 素数},\ q\nmid N);\\
\mathrm{(iii)}\quad&
f_E\equiv f_A\pmod {p^n}
\quad\text{逐个 Fourier 系数};\\
\mathrm{(iv)}\quad&
E[p^n]\simeq A[p^n]
\quad\text{作为实际 }G_{\mathbb Q}\text{-}\mathbb Z/p^n\mathbb Z
\text{ 模}.
\end{aligned}
\tag{326.22}
$$

同样可以把 (iv) 换为 $H_a[p^n]\simeq B_a[p^n]$。

**证明。** (i)、(ii)、(iii) 的等价性由 (326.12)–(326.15) 给出。

若 (iv) 成立，对任意好素数 $q$，因 $p\mid N$，必有 $q\ne p$。在未分歧的 $p^n$ 挠点上取 Frobenius 迹得到两条曲线整数迹的模 $p^n$ 同余。在所有坏素数，包括 $p$，(326.8) 给逐项严格相等。再用 (326.14) 即得 (iii)。

反过来，设 (iii) 成立，写 $R=\mathbb Z/p^n\mathbb Z$，以 $\rho_E,\rho_A$ 记两实际自由秩二 $R$ 模表示。在两条 $p^n$ 除法域的复合域中应用 Chebotarev：每个共轭类可由避开 $N$ 的好素数 Frobenius 实现。因此

$$
\operatorname {tr}\rho_E(g)=\operatorname {tr}\rho_A(g)
\quad(g\in G_{\mathbb Q}).
\tag{326.23}
$$

此时不能仅援引“半单化同构”就结束，尤其 $n>1$ 的系数环不是域。以下直接构造实际同构。

由 (326.21) 和 Nakayama 引理，

$$
\operatorname {span}_R\rho_A(G_{\mathbb Q})=M_2(R).
\tag{326.24}
$$

令 $\mathcal A=\operatorname {span}_R\rho_E(G_{\mathbb Q})$；因为群元素矩阵相乘仍是群元素矩阵，它是含一的 $R$ 子代数。若

$$
\sum_i c_i\rho_E(g_i)=0,\qquad c_i\in R,
$$

则对每个 $h\in G_{\mathbb Q}$，乘以 $\rho_E(h)$ 后取迹，再用 (326.23)，得到

$$
0=\sum_i c_i\operatorname {tr}\rho_E(g_i h)
=\operatorname {tr}\left(
\left(\sum_i c_i\rho_A(g_i)\right)\rho_A(h)\right).
\tag{326.25}
$$

$M_2(R)$ 上的双线性配对 $(X,Y)\mapsto\operatorname {tr}(XY)$ 是完美的；矩阵单位 $E_{ij}$ 与 $E_{ji}$ 为对偶基。由 (326.24)，(326.25) 强迫 $\sum_i c_i\rho_A(g_i)=0$。

因此

$$
T:\mathcal A\longrightarrow M_2(R),\qquad
\sum_i c_i\rho_E(g_i)\longmapsto\sum_i c_i\rho_A(g_i)
\tag{326.26}
$$

良定义，且是满的 $R$ 代数同态。作为有限集合，
$\mathcal A\subseteq M_2(R)$，而目标基数为 $p^{4n}$；满射迫源至少具有该基数。因此 $\mathcal A=M_2(R)$，$T$ 为 $R$ 代数自同构。

最后，此自同构为内自同构，可在本情形直接证明。令 $e_{ij}=T(E_{ij})$。$e_{11},e_{22}$ 是互补秩一幂等元，像和核是在局部环 $R$ 上的自由秩一模。取 $e_{11}$ 像的生成元 $v_1$，并令 $v_2=e_{21}v_1$。矩阵单位关系给 $e_{12}v_2=v_1$，所以 $v_2$ 生成 $e_{22}$ 的像，$(v_1,v_2)$ 为一组基。在此基下全部 $e_{ij}$ 恢复为标准矩阵单位。于是存在 $P\in\mathrm {GL}_2(R)$，使 $T(X)=PXP^{-1}$。应用于 $\rho_E(g)$ 得

$$
\rho_A(g)=P\rho_E(g)P^{-1}\quad(g\in G_{\mathbb Q}),
$$

这就是实际同构 (iv)。同时二次扭曲的等价性为 (326.5)。$\square$

### 5.3 最大同余层

因此这一对固定曲线的最大同余指数严格为

$$
n_{\max}(p)=v_p(\mathcal D(a,b))=v_p(\mathcal C(a,b)).
\tag{326.27}
$$

值零表示连模 $p$ 同构也没有。值有限是因为 $\mathcal D>0$。由 (326.18)，若有模 $p^n$ 同构，必有

$$
p^n\le\mathcal C(a,b)\le2\sqrt{S(N)}.
\tag{326.28}
$$

这是随共同导子变化的上界，不是绝对 $p$ 界。

## 6. 同一个全局同构的 Weil 辛型

在原实际分支中，R315 已证明每个 $H_a[p]\simeq B_a[p]$ 的全局同构之 Weil 乘子均为平方。其 $p$ 处证明使用同一潜在好模型、非约化底环上的 Raynaud 延拓、特殊纤维的 $\mu_3$ 中心化子和完整半线性 Frobenius 下降；没有逐处另选同构的自由。该局部证明事实上对 $3\nmid v_p(r)>0$ 都成立，(326.19) 正满足此条件。

同时二次扭曲由几何曲线同构实现，保持 Weil 配对，所以 $E[p]\simeq A[p]$ 的乘子同样是平方。设定理 326.2 给出某个
$\phi_n:E[p^n]\simeq A[p^n]$，其乘子为
$\mu_n\in(\mathbb Z/p^n\mathbb Z)^\times$。约化模 $p$ 后乘子为平方；因为 $p$ 为奇数，Hensel 引理给
$c\in(\mathbb Z/p^n\mathbb Z)^\times$ 使
$c^2\mu_n=1$。故 $[c]\circ\phi_n$ 保持 Weil 配对。

也可以追踪全部同构：由 (326.24)，$A[p^n]$ 的全局自同构必须与整个 $M_2(R)$ 交换，因而只是 $R^\times$ 标量，其乘子为平方。于是

$$
\max\bigl(\{0\}\cup
\{n\ge1:\text{存在保持 Weil 配对的全局 }p^n\text{ 同构}\}\bigr)
=v_p(\mathcal C(a,b)).
\tag{326.29}
$$

这不把 R301 的模 $p$ Kummer/Selmer 运输自动推广到模 $p^n$；更高层的当地整模型及 Kummer 条件仍须另证。

## 7. 与 R320 全局好素数约束的接口

记 $F=2a^3-1$。若 $q\ge5$ 且 $q\mid F$，则 $2r+F=1$ 保证 $q\nmid db$，故 $q$ 是 (326.2) 的共同好素数。由同时二次扭曲 (326.4)，两组整数迹差只差同一个二次单位符号：

$$
a_q(E)-a_q(A)
=\left(\frac{\beta}{q}\right)
\bigl(a_q(H_a)-a_q(B_a)\bigr).
\tag{326.30}
$$

R320 在此把右边两迹化为固定的 Gaussian/Eisenstein CM 迹，并记其差的四分之一为 $D_\varepsilon(q)$。因此

$$
\mathcal D\mid4D_\varepsilon(q).
\tag{326.31}
$$

特别地，对 R320 的三个 gcd（空集合约定为零），有

$$
\mathcal D\mid4G_1(a),\qquad
\mathcal D\mid4G_{57}(a),\qquad
\mathcal D\mid8G_a(a)\quad\text{在奇分支}.
\tag{326.32}
$$

最后一个式子来自 $q\equiv7\pmod {12}$、$q\mid a$ 时的迹差 $2a_q(y^2=x^3+1)$，而 R320 将该迹除以四后取 gcd。

R320 在 $p\equiv5\pmod {12}$、$q\equiv1\pmod {12}$、$q\mid F$ 上证明某些单独迹差额外被 $p^2$ 整除。这不能推出 $p^2\mid\mathcal D$：后者需要所有好素数的迹差都被 $p^2$ 整除。定理 326.2 准确刻画了这种额外全局提升所需的完整条件。

## 8. 有限终止算法、量词及剩余缺口

给定满足第一节条件的整数 $(a,b,d,\varepsilon)$，按 (326.6)–(326.10) 计算准确共同导子 $N$ 和整数 $S(N)$。枚举 $q\le S(N)$ 的好素数，用有限域点数求两条实际曲线的整数迹，计算 (326.13) 的 gcd。这是完全有限且有效的整数算法；本条无需先搜索全局同构，也无需假设 GRH、Frey–Mazur 或任何 Selmer 消失。

算法所得的同一个正整数 $\mathcal C$ 同时判定所有满足 (326.19) 的素数 $p$ 及所有 $p^n$ 层。如果额外保留原问题的完整正规化子像或指定三次角色，这些仍是原参数的额外条件，本算法不会凭空产生它们。

本条没有实际枚举某个巨大 $N$ 的完整窗口，也不提交虚构的数值证书。它是一条完整证明的算法及等价判别。它与 R293/R317 的有限局部比较族不冲突：这里的好素数窗口随参数的共同导子增长，并且比较的是同一对全局曲线；任意预先固定的有限集合不能替代它。

统一问题的剩余接口现在可以精确写成：须对本族证明，正整数 $\mathcal C(a,b)$ 不可能有任意大的满足实际全部前提的素因子。当前仅有

$$
\mathcal C(a,b)\le
2\sqrt{\frac{N(A_d)}6
\prod_{q\mid N(A_d)}\left(1+\frac1q\right)},
\tag{326.33}
$$

而 $N(A_d)$ 随 $d$ 无界。既有的导子或高度下界与此式不能给矛盾。所需的统一限制尚未证明，主目标仍为 OPEN。

## 9. 依赖与已核原文

- R258，§§5–9：实际 CM 惯性 $C_{\mathrm {ns}}(p)^3$、立方自由参数及二、三处准确导子表。
- R315：同一个全局同构在 $p$ 处的平方 Weil 乘子。
- R317，§§2–4：两种保留分支在二、三处的真实局部同构与完整下降；本文在这些处比较任意辅助 $\ell>37$。
- R320：$2a^3-1$ 的好素数上的两种固定 CM 迹、实际 gcd 和个别 $p^2$ 整除。
- Christophe Breuil, Brian Conrad, Fred Diamond, Richard Taylor, *On the modularity of elliptic curves over Q: wild 3-adic exercises*, J. Amer. Math. Soc. **14** (2001), 843–939，Theorem A，Introduction 的条件 (1)–(6)。已直接核作者原稿第 1–3 页：全部椭圆曲线模性及完整 $L$ 级数在准确导子上的权二形式对应。DOI：[10.1090/S0894-0347-01-00370-8](https://doi.org/10.1090/S0894-0347-01-00370-8)；[作者原稿](https://math.stanford.edu/~conrad/papers/tswfinal.pdf)。
- Jacob Sturm, *On the congruence of modular forms*, in D. V. Chudnovsky et al. (eds.), *Number Theory*, Lecture Notes in Math. **1240**, Springer (1987), 275–280，Theorem 1，印刷第 276 页；定义在第 275–276 页。已直接核出版社公开的两页原文 preview，特别核实没有同余素数与 $N$ 互素的假设。DOI：[10.1007/BFb0072985](https://doi.org/10.1007/BFb0072985)；[出版社原文 preview](https://page-one.springer.com/pdf/preview/10.1007/BFb0072985)。

Chebotarev 定理、椭圆曲线 Hasse 界、模性的新形式与有理同源类对应，以及有限环上的 Nakayama 引理是标准已发表输入。本文所需的全部素数幂 Sturm 推广、整数理想等式和实际矩阵同构已在正文完整证明；没有将迹相等只得到的半单化结论冒作高阶同构。
