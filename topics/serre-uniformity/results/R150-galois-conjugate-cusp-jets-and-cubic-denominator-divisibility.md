# R150：共轭新形式的真实尖点展开与分母二、三次整除

日期：2026-11-12。

**状态：已证明。** 本文始终保留 R69、R72 的非零三次中心值假设。若提供该实际秩零商的新形式有非有理系数域，其整个 Galois 轨道在同一个商中给出真实整微分。比较这些微分，可以强迫第二个圆分频率具有分母深度。一般得到 $D^2\mid N(J_p)$；若 $a_2$ 已非有理，则得到 $D^3\mid N(J_p)$。

这没有证明一般三色理想为单位，没有排除全部实际分母，也没有消除变化三次中心值可能全零的分支。第 8.1 节还将结论推广到任意至少二维的非零中心值谱；唯一可用的归一化新形式为有理系数时，仍没有额外结论。

## 1. 设定与主定理

沿用 R69、R72、R137 的设定。设 $p>37$，实际曲线 $E/\mathbb Q$ 的模 $p$ 像为完整非分裂 Cartan 正规化子，并且其 $p$ 处惯性严格小于 Cartan。于是惯性为 $C^3$，且 $p\equiv2,5\pmod9$。令 $K$ 为实际二次商域，$\eta$ 为实际阶三角色。

**假设存在**水平 $p$、权二、平凡 nebentype 的归一化新形式
$$f=\sum_{n\ge1}a_n(f)Q^n$$
满足
$$L(1/2,\pi_{f,K}\otimes\eta)\ne0.\tag{150.1}$$
令 $K_f=\mathbb Q(a_n(f):n\ge1)$，并令 $G=g(X_0(p))$。R69、R72 给出实际完整水平扭曲曲线 $X=X_E^\alpha(p)$ 的连通核最优商
$$q:J_X\twoheadrightarrow A,\qquad A(\mathbb Q)\text{ 有限},\qquad \dim A=2[K_f:\mathbb Q].\tag{150.2}$$
其微分子空间包含 $f$ **整个 Galois 轨道**与两维三色增广空间的张量积，而不只是某一个系数嵌入。

取任意 $F/\mathbb Q$ 满足 $F[p]\simeq E[p]$，配对乘子由该实际同构确定。按 R137 写
$$\operatorname{den}(j(F))=D^p,\qquad D\in\mathbb Z_{\ge1}.\tag{150.3}$$
若 $D=1$，以下整除结论自动成立。对 $D>1$，每个 $\ell\mid D$ 满足
$$\ell\equiv\pm1\pmod p,\qquad\ell\ge2p-1>p+1.\tag{150.4}$$

沿用 R137、R142 的实圆分理想。令
$$L^+=\mathbb Q(\theta),\quad\theta=\zeta_p+\zeta_p^{-1},\quad\mathcal O^+=\mathbb Z[\theta],$$
$$A_p=u_0,\qquad B_p=\frac{u_1-u_2}{\zeta_p-\zeta_p^{-1}},\qquad J_p=(A_p,B_p)\subset\mathcal O^+,$$
$$N_p=\operatorname N_{L^+/\mathbb Q}(J_p),\qquad \sigma_r(\zeta_p)=\zeta_p^r.$$
这里 $u_i$ 是同一真实 Cartan 三色和，$u_0+u_1+u_2=0$。实圆分上的 $\sigma_r$ 只依赖 $r\bmod\{\pm1\}$。R137 已证明 $J_p\ne0$。

**定理 150.1。** 在 (150.1) 下：

1. 若 $K_f\ne\mathbb Q$，则
   $$\boxed{D^2\mid N_p.}\tag{150.5}$$
   更准确地，令 $r$ 是首个满足 $a_r(f)\notin\mathbb Q$ 的指标。则 $r$ 是素数，
   $$2\le r\le2G-1<p-1.\tag{150.6}$$
   对每个 $\ell\mid D$，写 $m=v_\ell(D)$。存在由实际尖点、实际原始 $p$ 次根所确定的同一个 $\lambda\mid\ell$，使
   $$v_\lambda(J_p)\ge m,\qquad v_\lambda(\sigma_r J_p)\ge m.\tag{150.7}$$
2. 若 $a_2(f)\notin\mathbb Q$，则同一个实际 $\lambda$ 满足
   $$\boxed{v_\lambda(J_p)\ge2m,\qquad v_\lambda(\sigma_2J_p)\ge m,}\tag{150.8}$$
   因而
   $$\boxed{D^3\mid N_p.}\tag{150.9}$$

这里每个 $\ell$ 可以选择不同的共轭新形式对。定理不要求某一固定共轭差在所有 $\ell$ 处都是单位；甚至允许所有这些差在系数域某个剩余素理想中为零。关键是其中某个差的**归一化 $\ell$ 赋值严格小于一**，再利用圆分理想在实际未分歧素数处的整数赋值。

## 2. 一个小 house 引理，包含分歧系数域

以下引理区分“模剩余素理想相同”和“模 $\ell\mathcal O$ 相同”。后一条件强得多。

**引理 150.2。** 设 $x$ 是非有理代数整数，次数 $e$，所有复共轭满足 $|x_i|\le H$。设 $\ell$ 是素数，
$$\ell\nmid e,\qquad H<(\ell+1)/2.$$
固定包含全部 $x_i$ 的正规数域在 $\ell$ 上方的一个赋值 $v$，归一化为 $v(\ell)=1$。则存在两个共轭 $x_i,x_j$，使
$$0\le v(x_i-x_j)<1.\tag{150.10}$$

**证明。** 否则所有共轭差的赋值至少一。置
$$t=\operatorname{Tr}_{\mathbb Q(x)/\mathbb Q}(x)\in\mathbb Z.$$
因为 $e$ 是 $\ell$ 单位，
$$v(x_i-t/e)\ge1\quad\text{对全部 }i.$$
选唯一的整数 $c$，满足
$$|c|\le(\ell-1)/2,\qquad c\equiv t/e\pmod\ell.$$
于是 $v(x_i-c)\ge1$。在正规闭包中把这组不等式同时作 Galois 共轭，得到在**每个** $\ell$ 上方素理想处，$x-c$ 的归一化赋值均至少一。因此
$$y=(x-c)/\ell$$
在 $\ell$ 上方整；在别的有限素数处，$\ell$ 为单位，所以它也整。故 $y$ 是代数整数。另一方面，每个复共轭满足
$$|y_i|\le\frac{H+(\ell-1)/2}{\ell}<1.$$
非零代数整数的范数是非零整数，不可能所有复绝对值都小于一。因此 $y=0$，即 $x=c\in\mathbb Q$，矛盾。证毕。

这个论证没有把系数域视为未分歧。若 $v(x_i-x_j)=1/e_\mu$ 等分数，仍可使用 (150.10)。

## 3. 首个非有理指标为何小且为素数

假设 $K_f\ne\mathbb Q$，令 $r$ 为首个非有理系数的指标。归一化给 $r\ge2$。对 $n$ 的 Hecke 乘法及素数幂递推说明：若所有素数指标 $q\le n$ 的系数都在 $\mathbb Q$，则 $a_n(f)\in\mathbb Q$。此外 $a_p(f)=\pm1$。所以这个最小 $r$ 必为素数，且 $r\ne p$。

选择一个使 $a_r(f^\sigma)\ne a_r(f)$ 的复嵌入。非零全纯微分
$$\omega_{f^\sigma}-\omega_f=(f^\sigma-f)\frac{dQ}{Q}$$
在 $X_0(p)$ 的 $\infty$ 尖点有阶数恰为 $r-1$ 的零。非零全纯微分的零因子次数为 $2G-2$，因此
$$r-1\le2G-2,\qquad r\le2G-1.$$
标准的 Riemann–Hurwitz 计算给
$$G=\frac{p+1}{12}-\frac{e_2}{4}-\frac{e_3}{3}\le\frac{p+1}{12},$$
其中 $e_2,e_3\ge0$ 是两个椭圆型的未分歧点数；两个尖点使常数项抵消。故
$$r\le2G-1\le(p+1)/6-1<p-1.\tag{150.11}$$

下面给足够的 house 界，不需要另加尖锐 Ramanujan 界。对 $r\ne p$，两个退化映射
$$X_0(pr)\rightrightarrows X_0(p)$$
均为度 $r+1$。全纯微分的 $L^2$ 范数满足拉回算子范数为 $\sqrt{r+1}$；迹映射为其伴随，算子范数也为 $\sqrt{r+1}$。权二 Hecke 算子是一次拉回与一次迹的复合，故其算子范数至多 $r+1$。将它作用在每个共轭新形式上，得到
$$|\sigma a_r(f)|\le r+1\le2G.\tag{150.12}$$
标准界 $2\sqrt r$ 更强，但这里不需要它。

又有
$$[\mathbb Q(a_r(f)):\mathbb Q]\le[K_f:\mathbb Q]\le G<\ell,$$
且由 (150.4)、(150.11)，
$$r+1\le2G\le(p+1)/6<(\ell+1)/2.$$
因此引理 150.2 可用于 $x=a_r(f)$。在任意预先固定的 $\ell$ 进系数嵌入下，存在两个完整共轭新形式 $f_1,f_2$，使
$$\delta:=v_\ell(a_r(f_1)-a_r(f_2))<1.\tag{150.13}$$
二者的全部前置系数均相同，因为这些系数本来就在 $\mathbb Q$。

## 4. 实际尖点处的全轨道整微分

固定 $\ell\mid D$。沿 R72、R137 取未分歧局部底环，使实际点 $P\in X$ 与实际尖点 $c$ 在同一个好约化形式圆盘中，取 Tate 参数
$$z=q_{\rm Tate}^{1/p},\qquad v_\ell(z(P))=m\ge1.$$
R137 的全尖点除子构造和形式群无挠证明给出：以 $c$ 为局部基点的实际最优商映射 $h$ 满足
$$h(c)=0,\qquad h(P)=0.\tag{150.14}$$
若使用乘以 $(p^2-1)/2$ 的无基点版本，这只是全部展开多一个 $\ell$ 单位，不影响下述推导。

随后可以加入全部新形式系数，所得环允许分歧。R72 的饱和格等式已在未分歧底环上证明，再平坦基变换。因此下文使用每个 $f_i$ 及其整系数线性组合，均为同一实际 $A$ 的真实整微分。

先保留实际频率 $a\in\mathbb F_p^\times$。令
$$v_a(n)=\begin{pmatrix}
\sigma_{an}(u_1-u_0)\\[2pt]
\sigma_{an}(u_2-u_0)
\end{pmatrix},\qquad 1\le n<p.$$
R72 的忘线 Tate 计算给，对于任意完整共轭新形式 $f_i$，同一个尖点处的两列实际微分满足
$$h^*\boldsymbol\Omega(f_i)=
\left(\sum_{1\le n<p}a_n(f_i)\kappa^n v_a(n)z^{n-1}+O(z^{p-1})\right)dz,\tag{150.15}$$
其中 $\kappa$ 为同一个 $p$ 次单位根。所有更高系数整；乘法线的贡献始于 $z^{p-1}dz$，故不改变本文使用的 $n=1,2,r$ 各项。

不能在 (150.15) 中独立选择 $a$ 或 $\kappa$。两个新形式是在**固定实际尖点和固定实际 Tate 基**下比较，所以它们具有完全相同的 $v_a(n)$ 和 $\kappa$。

由于 $u_0+u_1+u_2=0$，且 $2,3,\zeta_p-\zeta_p^{-1}$ 在 $\ell$ 处都是单位，
$$\min_jv_\ell(v_a(n)_j)
=v_\lambda(\sigma_nJ_p)\in\mathbb Z_{\ge0},\tag{150.16}$$
这里把实际 $a$ 吸收入同一个 $\lambda\mid\ell$ 的选择。式 (150.16) 中每个 $n$ 使用的是这个同一 $\lambda$。

### 形式积分的统一尾界

若 $1\le s\le\ell-1$，则对所有 $n\ge s$，
$$n-v_\ell(n)\ge s.$$
确实，$n<\ell$ 时显然；若 $v_\ell(n)=j\ge1$，则
$$n-j\ge\ell^j-j\ge\ell-1\ge s.$$
所以对 $m\ge1$，
$$nm-v_\ell(n)\ge(n-v_\ell(n))m\ge sm.\tag{150.17}$$
此外 $nm-v_\ell(n)\to\infty$，保证无限尾在 $m=1$ 时仍收敛。

对一个实际整不变微分，$h(P)=h(c)=0$ 给出积分恒等式
$$0=\sum_{n\ge1}\frac{c_n}{n}z(P)^n,$$
其中 $h^*\Omega=\sum c_nz^{n-1}dz$。若只保留一个低阶项，其余项从 $n=s$ 起，则 (150.17) 给出至少 $sm$ 的尾赋值。这不依赖系数扩张的分歧指数。

## 5. 一般非有理系数域给第二个真实频率

令 $r$ 如第 3 节，并在当前系数赋值下选择 (150.13) 的 $f_1,f_2$。对同一实际商中的整微分相减：
$$\boldsymbol\Omega(f_1)-\boldsymbol\Omega(f_2).$$
它在 (150.15) 中的前 $r-1$ 项全为零，第 $r$ 项为
$$d\kappa^r v_a(r)z^{r-1}dz,
\qquad d=a_r(f_1)-a_r(f_2),\quad v_\ell(d)=\delta<1.$$
积分到实际点 $P$，其余项由 $n=r+1$ 起。因为
$$r+1\le2G<\ell-1,$$
(150.17) 逐个坐标给
$$v_\ell(d)+v_\ell(v_a(r)_j)+rm\ge(r+1)m.$$
因此
$$v_\ell(v_a(r)_j)\ge m-\delta.$$
这两个圆分数的赋值为整数，故严格的 $\delta<1$ 迫
$$v_\lambda(\sigma_rJ_p)\ge m.\tag{150.18}$$
R137 对原来的 $n=1$ 项已经给出
$$v_\lambda(J_p)\ge m.$$
从而得到 (150.7)。这里的第二频率是由**两个实际整微分相减**强迫出来的，不是从 Galois 对称性假定原分母深度沿频率轨道传播。

## 6. $a_2$ 非有理时原频率也获得双倍深度

现在 $r=2$。写
$$x_i=a_2(f_i),\qquad d=x_1-x_2,\qquad v_\ell(d)<1.$$
第 5 节已得 $v_\lambda(\sigma_2J_p)\ge m$。

另取同一实际商上的整微分组合
$$x_2\boldsymbol\Omega(f_1)-x_1\boldsymbol\Omega(f_2).$$
因为 $a_1(f_i)=1$，其常数项为
$$-d\kappa v_a(1)dz.$$
其 $z\,dz$ 项严格为零：
$$x_2a_2(f_1)-x_1a_2(f_2)=x_2x_1-x_1x_2=0.$$
故形式积分中的尾从 $n=3$ 起。由 (150.17)，
$$v_\ell(d)+v_\ell(v_a(1)_j)+m\ge3m.$$
再用圆分整数赋值及 $v_\ell(d)<1$，得到
$$v_\lambda(J_p)\ge2m.\tag{150.19}$$
这证明 (150.8)。它并未假设 $a_2(f_i)$ 为单位，也未用它们的差去除微分，因此不会引入非整的 Hecke 投影或系数分母。

## 7. 两个不同圆分素理想的范数贡献

由 $\ell\equiv\pm1\pmod p$，$\ell$ 在 $L^+$ 中完全分裂。实圆分 Galois 群在 $\ell$ 上方的素理想上自由传递。因此当 $1<r<p-1$ 时，$\sigma_r\ne1$，且
$$\lambda'=\sigma_r^{-1}\lambda\ne\lambda.$$
按理想赋值的定义，
$$v_\lambda(\sigma_rJ_p)=v_{\lambda'}(J_p).$$

在一般情形，两处分别至少有 $m$，所以
$$v_\ell(N_p)=\sum_{\nu\mid\ell}v_\nu(J_p)\ge2m.$$
在 $a_2$ 非有理情形，它们分别至少有 $2m$、$m$，所以
$$v_\ell(N_p)\ge3m.$$
对所有 $\ell\mid D$ 合并，得到 (150.5)、(150.9)。不要求在每个 $\nu\mid\ell$ 都具有相同深度。

## 8. 全 $p$ 的显式分母上界及边界

R137 的 Parseval 界为
$$N_p\le Q_p^{(p-1)/4},\qquad Q_p=\frac{2p}{9}-\frac4{9(p-1)}.$$
设 $e=2$；在 $a_2(f)$ 非有理情形可取 $e=3$。则
$$\boxed{\log\operatorname{den}(j(F))
\le\frac{p(p-1)}{4e}\log Q_p.}\tag{150.20}$$
每个实际分母素数还满足
$$e\,v_\ell(D)\log\ell
\le\frac{p-1}{4}\log Q_p,$$
而 $Q_p<\ell$，故
$$\boxed{v_\ell(D)<\frac{p-1}{4e}.}\tag{150.21}$$

若存在多个满足 (150.1) 的新形式，可以任选其中一个满足本篇系数条件的因子。这里没有证明必然存在这样的非有理系数因子。下面说明多个有理系数因子也可共同使用，但唯一非零中心值新形式为有理系数的分支仍须保留。本文也没有证明 $D$ 与三次角色导子之间的足够上、下界，没有控制 $j$ 的分子，更没有把形式积分条件当作实际曲线存在的充分条件。

### 8.1 任意至少二维的非零中心值谱

令 $\mathcal F$ 是满足 (150.1) 的归一化新形式的一个非空 Galois 稳定集合，包括所选形式的完整轨道，不重复计数。因 $\dim S_2(\Gamma_0(p))=G$，有 $|\mathcal F|\le G$。

**推论 150.3。** 若 $|\mathcal F|\ge2$，则 $D^2\mid N_p$。如果集合
$$\{a_2(f):f\in\mathcal F\}$$
不全相同，则 $D^3\mid N_p$。两种情况下相应的局部深度和 (150.20)、(150.21) 也成立。

**证明。** 首先把每个轨道的 R69 商取乘积，再取 $J_X$ 在乘积中的像，最后以连通核最优化。像的有理点是有限集合的子群；最优化只给一个同源，因此仍得到实际 $A(\mathbb Q)$ 有限的商。其泛纤维微分空间包含全部 $\mathcal F$ 与三色增广空间的张量积。R72 的饱和格证明继续适用，完全不要求不同 Hecke 因子在 $\ell$ 处整直和。

引理 150.2 有如下直接推广。设一个有限的 Galois 稳定代数整数多重集 $\{x_i\}_{1\le i\le e}$ 不全相同，$\ell\nmid e$，且全部 house 至多 $H<(\ell+1)/2$。它的总和 $t$ 为整数。若在固定系数赋值处所有差的赋值至少一，仍可取 $c\equiv t/e\pmod\ell$、$|c|\le(\ell-1)/2$。Galois 稳定性使每个 $(x_i-c)/\ell$ 在所有有限素数处整，且所有复共轭绝对值小于一。于是全部 $x_i=c$，矛盾。因此总存在一个差的归一化赋值小于一。此推广也包括多个不同的有理整数值。

令 $r$ 为首个使 $\{a_r(f):f\in\mathcal F\}$ 不全相同的指标。因为 $\mathcal F$ Galois 稳定，所有前置的共同系数均为有理整数。Hecke 递推与两个形式之差的零点次数，照第 3 节证明
$$r\text{ 是素数},\qquad 2\le r\le2G-1<p-1.$$
对上述系数多重集应用推广的 house 引理，其大小 $e=|\mathcal F|<\ell$、house 至多 $r+1$。故可在每个实际 $\ell$ 处选择 $f_1,f_2\in\mathcal F$，使第一处系数差的赋值小于一。第 5 节与第 7 节遂给 $D^2\mid N_p$。若 $a_2$ 值不全相同，则 $r=2$，第 6 节再给 $D^3\mid N_p$。证毕。

因此，本篇二次整除加强的准确剩余谱分支是：满足 (150.1) 的归一化新形式总共只有一个；Galois 稳定性迫它具有有理系数。本文不声称这个分支不可能，也不把存在一个非零中心值提升为存在两个。

## 9. 依赖和核验接口

- R69：整个 Galois 轨道的非零中心值与实际有限有理点商；没有把单一共轭的解析非零直接当作全轨道秩零。
- R72 §§2–5：最优商的整微分格饱和、系数域可分歧的平坦基变换、全部共轭新形式的整性，以及同一实际尖点的精确忘线展开。
- R137：$\operatorname{den}(j(F))=D^p$、实际 $\ell\equiv\pm1\pmod p$、$h(P)=h(c)=0$、原频率深度和 Parseval 范数界。
- R142：二阶尖点与同一实际频率的规范。本文加强来自额外的共轭新形式微分；没有把 R142 中 $W_p\bmod\lambda=0$ 重新命名为新的排除条件。

本篇新输入是第 2 节的小 house 引理、第 3 节首个非有理指标的微分零点界，以及第 5、6 节同一实际商中的两种整微分组合。证明为全参数论证，没有扩大固定素数扫描或使用数值非零。
