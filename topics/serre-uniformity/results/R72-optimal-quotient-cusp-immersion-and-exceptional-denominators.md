# R72：最优商的整微分与 exceptional 分母判据

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明。** 本文把 R69 的实际秩零商接到尖点的形式浸入。关键是先取连通核的最优商，再用已发表的 Raynaud–Mazur 正合性得到其微分格的饱和；不假设某个新形式的 Hecke 幂等元在 $\ell$ 整。忘线映射在 Tate 参数中的直接展开给出两个三次颜色和之差。

所得结论与 Studnia submitted 论文 Theorem D 在这里所需的分支一致，但证明只引用已发表的整模型输入及 R66、R69，并在下文重做全部尖点计算与有理点排除。它仍以非零 $L$ 值为条件；R66 的 $p>M$ 是一个已发表充分条件。本文既未证明 exceptional 集为空，也未控制变化的 $M$，没有完成主问题。

## 1. 设置与结论

设 $p>37$，$E/\mathbb Q$ 无 CM，实际模 $p$ 像为完整非分裂正规化子
$$
\rho_{E,p}(G_{\mathbb Q})=N=C\rtimes\langle c\rangle,
\qquad C\simeq\mathbb F_{p^2}^{\times}.
$$
假设
$$\rho_{E,p}(I_p)\subsetneq C.$$
按 R66，$p\equiv2,5\pmod9$，实际惯性为 $H=C^3$。取阶三字符 $\vartheta:C\to\mu_3$，置
$$
K=\overline{\mathbb Q}^{\,\rho_{E,p}^{-1}(C)},\qquad
\eta=\vartheta\circ\rho_{E,p}|_{G_K},\qquad
M=|D_K|\,c_\eta^2.
$$

设水平 $p$、权二、平凡 nebentype 的归一化新形式 $g$ 满足
$$L(\tfrac12,\pi_{g,K}\otimes\eta)\ne0.\tag{72.1}$$
对任意配对乘子 $\alpha$，写
$$X=X_E^\alpha(p),\qquad J=\operatorname{Jac}(X).$$
R69 给满射 $q_0:J\to B$，其中 $B$ 与 $B_g$ 同源，且 $B(\mathbb Q)$ 有限。令
$$
A=J/(\ker q_0)^0,\qquad q:J\twoheadrightarrow A.
\tag{72.2}
$$
于是 $q$ 有连通核，$A\to B$ 为同源，故 $A(\mathbb Q)$ 也有限。

用非平方 $z\in\mathbb F_p^\times$ 和 $\tau^2=z$ 定义三种颜色
$$
B_j=\{b\in\mathbb F_p:\chi(1+b\tau)=\zeta_3^j\},
\quad
u_j=\sum_{b\in B_j}\zeta_p^b,
\quad
I_p=(u_0,u_1,u_2)\subset\mathbb Z[\zeta_p].
\tag{72.3}
$$
这里 $\chi$ 阶三，颜色取向不影响 $I_p$；改变 $z$ 的选择只作变元缩放及圆分 Galois 共轭，不改变下述有理素数集。称 $\ell$ exceptional，若 $I_p$ 在某个 $\ell$ 上方素理想中。

**定理 72.1。** 设 (72.1) 成立。对于任何 $F/\mathbb Q$ 及模 $p$ 同余
$$F[p]\simeq E[p],$$
若 $\ell$ 整除 $j(F)$ 的分母，则
$$
\boxed{\ell\equiv\pm1\pmod p,\qquad \ell\text{ exceptional for }p.}
\tag{72.4}
$$
更准确地，$\ell\bmod p$ 是 $K/\mathbb Q$ 在 $\ell$ 的二次字符值。

**推论 72.2。** 若 $p>M$，则 R66 的 Feigon–Whitehouse 非消失提供满足 (72.1) 的 $g$，所以 (72.4) 对所有上述 $F$ 成立，特别对 $F=E$ 成立。

下面同时证明一个几何接口：只要 $\ell\nmid p(p^2-1)$、$X$ 在 $\ell$ 是未分歧的完整水平曲线扭曲且 $\ell$ 非 exceptional，最优商 $q$ 对应的尖点余切映射在每个几何尖点均满射。有限性只在最后排除有理点时使用。

## 2. 最优商的积分微分像

本节区分三个对象：有理 Hecke 投影、新形式的泛纤维微分子空间、最优商的整微分格。

设 $R$ 是 $\mathbb Q_\ell$ 的有限未分歧扩张的整数环，$\ell>2$，记 $L_0=\operatorname{Frac}(R)$。设 $J_R$ 为阿贝尔概形，且
$$0\longrightarrow K_0\longrightarrow J_{L_0}
\overset q\longrightarrow A_{L_0}\longrightarrow0$$
为连通核的阿贝尔簇正合列。Mazur (1978), Proposition 1.2 (Raynaud) 给出对应阿贝尔概形正合列
$$
0\longrightarrow\mathcal K_0\longrightarrow\mathcal J
\overset{\mathcal q}\longrightarrow\mathcal A\longrightarrow0,
\tag{72.5}
$$
因为绝对分歧指数 $e=1<\ell-1$。特别 $\mathcal q$ 光滑，沿单位截面取余切得到自由 $R$ 模正合列
$$
0\longrightarrow\omega_{\mathcal A/R}
\overset{q^*}\longrightarrow\omega_{\mathcal J/R}
\longrightarrow\omega_{\mathcal K_0/R}
\longrightarrow0.
\tag{72.6}
$$
这里 $\omega_{\mathcal A/R}=e_{\mathcal A}^*\Omega^1_{\mathcal A/R}$。

所以 $q^*\omega_{\mathcal A/R}$ 在 $\omega_{\mathcal J/R}$ 中饱和。若
$$V=q^*H^0(A_{L_0},\Omega^1_{A_{L_0}/L_0}),$$
则
$$
\boxed{q^*\omega_{\mathcal A/R}
       =V\cap\omega_{\mathcal J/R}.}
\tag{72.7}
$$
证明只需观察 (72.6) 的余核无挠：右边模左边是一个同时被某个非零 $R$ 元素杀掉、又嵌入自由模的模，故为零。

这些等式可以再沿任意有限扩张 $R\to R'$ 平坦基变换。我们只在未分歧 $R$ 上使用 Raynaud–Mazur；引入新形式系数域时，允许 $R'$ 分歧，不会重新假设其分歧指数仍小。

若 $\mathcal X/R$ 光滑、射影、几何连通，且 $\mathcal J=\operatorname{Pic}^0_{\mathcal X/R}$，则
$$\omega_{\mathcal J/R}=H^0(\mathcal X,\Omega^1_{\mathcal X/R}).$$
这是下面将一个**已知积分、且在泛纤维属于 $V$** 的曲线微分升为真实 $\mathcal A$ 微分的依据。

### 已发表输入的精确位置

Mazur 的 Proposition 1.2 在 pp.135–136，后续 Corollary 1.1 在 p.137 直接写出余切正合列。其小分歧基础是 Raynaud (1974), Théorème 3.3.3、Corollaire 3.3.6(1), p.268：有限平坦 $\ell$ 幂群的泛纤维同态在 $e<\ell-1$ 时唯一延拓，且核、余核平坦。故 (72.7) 不是“$\ell$ 不整除有限群阶”的推论。

## 3. R69 商的泛纤维微分子空间

令 $\Omega=\mathbb P(E[p])$。R69 的 $p+1$ 个忘线映射为
$$\pi_i:X_{\overline{\mathbb Q}}\to X_0(p)_{\overline{\mathbb Q}}.$$
写 $W_g\subset H^0(X_0(p)_{\overline{\mathbb Q}},\Omega^1)$ 为 $g$ 的整个 Galois 轨道张成的子空间。令
$$
\operatorname{Aug}(\Omega)
=\{(a_i)\in\overline{\mathbb Q}^{\,\Omega}:\sum_i a_i=0\}.
$$
由 R69 的构造以及其 Gram 恒等式，
$$
V_{\overline{\mathbb Q}}
=\left\{
\sum_{i\in\Omega}\pi_i^*\omega_i:
(\omega_i)\in
\operatorname{Aug}(\Omega)^H\otimes W_g
\right\}.
\tag{72.8}
$$
右边维数为 $2\dim A_g$；忘线映射的 Gram 标量 $(p^2-1)/2\ne0$ 保证没有多余核。

具体地，$H$ 在 $\Omega$ 有三个等长轨道 $O_0,O_1,O_2$，每个长度
$$m=(p+1)/3.$$
对任何 $\omega\in W_g$，两个微分
$$
\Omega_j(\omega)=
\sum_{i\in O_j}\pi_i^*\omega-
\sum_{i\in O_0}\pi_i^*\omega,\qquad j=1,2,
\tag{72.9}
$$
均属于 $V_{\overline{\mathbb Q}}$。

这里 $H$ 仍只是 R69 中置换 $\Omega$ 的 Galois 像子群。式 (72.9) 是真实忘线拉回的线性组合；没有把 $H$ 当作固定配对分支的几何甲板群。把 $q_0$ 最优化为 $q$ 只经过同源，不改变特征零中的 (72.8)。

## 4. 归一化新形式的积分性

取一个包含 $g$ 全部系数的有限扩张，并在 $\ell\ne p$ 上选整数环 $R'$。令
$$g(q)=\sum_{n\ge1}a_n(g)q^n,\qquad a_1(g)=1.$$
新形式的 $a_n(g)$ 是代数整数。标准模形式与微分对应给
$$\omega_g=g(q)\frac{dq}{q}.$$
它属于 $X_0(p)_{R'}$ 上的整微分格。

这里所需的 $q$ 展开原则也可直接由好约化证明。若某个泛纤维全纯微分的 $q$ 展开整，而它自身不整，取最小 $r>0$ 使 $\varpi^r\omega$ 整。其模 $\varpi$ 约化在尖点的完整形式邻域为零。特殊纤维光滑、几何连通，故不可约，一个正则微分的形式 germ 为零便迫使它全局为零。因此 $\varpi^r\omega$ 又可被 $\varpi$ 整除，矛盾。光滑射影曲线的上同调基变换保证这个除法仍在整微分格内。

令 $w_p:X_0(p)\to X_0(p)$ 为 Atkin–Lehner 对合，取
$$\omega=w_p^*\omega_g.\tag{72.10}$$
它在 $\ell\ne p$ 仍整，并仍位于 $W_g$：$w_p$ 保持每个水平 $p$ 新形式轨道。选择 (72.10) 是为了下面的 Tate 展开不带 Atkin–Lehner 符号；没有使用该符号的任何模 $\ell$ 性质。

## 5. 尖点处忘线映射的一次系数

在一个几何尖点，经过有限未分歧基变换及随后加入系数域，完整水平曲线的形式参数可取
$$t=q_{\rm Tate}^{1/p}.$$
先采用标准 Tate 基：
$$E_{t^p}=\mathbb G_m/(t^p)^{\mathbb Z},\qquad
E_{t^p}[p]=\langle\zeta_p,t\rangle.$$
其中唯一乘法线记为 $\infty$；另外 $p$ 条线是
$$L_b=\langle\zeta_p^b t\rangle,\qquad b\in\mathbb F_p.$$

忘掉线 $\infty=\mu_p$ 的映射 $\pi_\infty$ 将尖点送到 $X_0(p)$ 的 $\infty$，并在标准局部参数中满足 $q=t^p$。因此对任意尖点微分 $\omega$，
$$\pi_\infty^*\omega\text{ 的 }dt\text{ 常数项为 }0.\tag{72.11}$$

对于有限线，商 Tate 曲线为
$$E_{t^p}/\langle\zeta_p^b t\rangle=E_{\zeta_p^b t}.$$
所以 $w_p\circ\pi_b$ 在目标的 $\infty$ 参数中给 $q=\zeta_p^b t$。按 (72.10)，
$$
\pi_b^*\omega
  =(w_p\circ\pi_b)^*\omega_g
  =\sum_{n\ge1}a_n(g)\zeta_p^{bn}t^n\frac{dt}{t}.
\tag{72.12}
$$
其 $dt$ 常数项恰为 $\zeta_p^b$。

### 与实际 Cartan 颜色同时对齐

不能默认为标准 Tate 基已经把实际 $C$ 放在某个预先指定的矩阵形式中。可在二维空间中取一个迹零二次算子 $T$，使
$$\mathbb F_p[T]=C\cup\{0\},\qquad T^2=z,$$
并把乘法线的一个生成元记作 $\tau$、另一个基向量记作 $1$。于是
$$
\Omega=\{\infty=[\tau]\}\cup\{[1+b\tau]:b\in\mathbb F_p\}.
$$
由于 $3\nmid p-1$，$\chi$ 在 $\mathbb F_p^\times$ 平凡；又 $\tau^2=z$，故 $\chi(\tau)=1$。因此
$$O_0=\{\infty\}\cup B_0,\qquad O_1=B_1,\qquad O_2=B_2.\tag{72.13}$$

在 Tate 表示中，这样的两个基向量一般送到
$$\tau\mapsto\zeta_p^u,\qquad
1\mapsto\zeta_p^v t^w,\qquad u,w\in\mathbb F_p^\times.$$
有限线 $[1+b\tau]$ 的生成元为 $\zeta_p^{v+bu}t^w$。将其升到 $w^{-1}\bmod p$ 次幂不改变循环子群；在 Tate 商中可删去 $(t^p)^\mathbb Z$ 因子。故其标准参数为
$$q_0=\zeta_p^{d+ab}t,\qquad
a=u/w\in\mathbb F_p^\times,\quad d=v/w\in\mathbb F_p.$$
于是 (72.12) 的一次系数一般是
$$\kappa\,\zeta_p^{ab},\qquad \kappa=\zeta_p^d\in(R')^\times.\tag{72.14}$$
任意配对分支、任意尖点只改变 $a$ 和共同单位 $\kappa$，不会改变共同消失问题。

将 (72.14) 代入 (72.9)，得到
$$
\boxed{\Omega_j(\omega)|_{t=0}
 =\kappa\,\sigma_a(u_j-u_0)\,dt,\qquad j=1,2,}
\tag{72.15}
$$
其中 $\sigma_a(\zeta_p)=\zeta_p^a$。

## 6. 非 exceptional 给真实最优商的形式浸入

设 $\ell\nmid p(p^2-1)$，且曲线在 $\ell$ 的模型如上。若 $\ell$ 非 exceptional，则对每个 $\ell$ 上方素理想，三个 $u_j$ 不会同时为零。又
$$u_0+u_1+u_2=\sum_{b\in\mathbb F_p}\zeta_p^b=0.$$
由于 $\ell\ne3$，两个差 $u_1-u_0,u_2-u_0$ 不会同时为零：若都为零，则 $3u_0=0$，从而三个均为零。对其任意圆分共轭也成立。

因此 (72.15) 的两个一次系数中至少一个是 $R'$ 单位。相应的 $\Omega_j(\omega)$：

1. 是整微分，因为每个忘线映射及 $\omega$ 都在该好模型上整；
2. 在泛纤维属于 $V$，由 (72.8)–(72.9)；
3. 因而由 (72.7) 是一个真实 $\mathcal A_{R'}$ 微分的拉回。

所以在每个几何尖点，$\mathcal A$ 的微分拉回满射到该点的一维余切空间。这个满射可沿平坦基变换下降，故不是仅在特征零或仅在某个外加微分格中成立。

对曲线上的任意局部 Abel–Jacobi 映射后接 $q$，余切满射即给尖点的形式浸入。若改用次数 $\delta$ 的无基点映射
$$x\longmapsto q([\delta x-D]),$$
其微分只多乘 $\delta$；当 $\ell\nmid\delta$ 时结论保持。

这一步明确消除了 Hecke congruence 分母：我们既未对整模施加 $e_g$，也未要求模 $\ell$ 的不同 Hecke 因子直和。允许它们有同余，(72.7) 仍将所构造的整微分纳入正确的最优商。

## 7. 实际 Tate 分母给未分歧的好模型

设 $F[p]\simeq E[p]$，$\ell$ 整除 $j(F)$ 的分母。

首先 $\ell\ne p$。确实，$F$ 也有同一完整正规化子像及同一 $p$ 处惯性 $C^3$；R21 的局部分析给潜在好约化。亦可直接看出：$p$ 处潜在乘法表示可约，而 $C^3$ 在 $\mathbb F_p^2$ 上不可约。

由 R2 的准确 Tate 判据，
$$
\ell\equiv\varepsilon_K(\ell)\pmod p,\qquad
p\mid-v_\ell(j(F)),\qquad
\rho_{E,p}(I_\ell)\subset\{\pm I\}.
\tag{72.16}
$$
特别
$$\ell>p+1,\qquad \ell\nmid p(p^2-1).\tag{72.17}$$
$\varepsilon_K$ 在这里不分歧，因为商掉 $C$ 后 (72.16) 的惯性为零。

尽管 $E[p]$ 本身可能有一个标量二次惯性，$\pm I$ 在完整水平模曲线的粗曲线上作用平凡：基同构与其相反同构由椭圆曲线的 $[-1]$ 联系。因此 $X_E^\alpha(p)$ 的曲线扭曲在 $\ell$ 处未分歧。$\zeta_p$ 也在 $\ell\ne p$ 处未分歧。经过有限未分歧扩张，这个曲线及其尖点概形成为标准的光滑完整水平模型；有限 étale 下降给：

- $X$ 在 $\mathbb Z_\ell$ 上有光滑射影几何连通模型 $\mathcal X$；
- 尖点闭子概形 $\mathcal Z$ 有限 étale；
- $j$ 映射延拓，$j^{-1}(\infty)$ 的支撑恰为 $\mathcal Z$；
- $J$ 好约化，最优商 $A$ 也好约化，且 §2 的整格结论适用。

代表同余 $F[p]\simeq E[p]$ 的点 $P\in X(\mathbb Q)$ 延拓成 $\mathcal X(\mathbb Z_\ell)$ 的截面。因为 $v_\ell(j(F))<0$，其特殊点 $c_0$ 是 $\mathbb F_\ell$ 有理尖点。有限 étale 性和 Hensel 性给唯一
$$c\in\mathcal Z(\mathbb Z_\ell)$$
提升 $c_0$。所以 $P,c$ 落在同一个未分歧的剩余圆盘。

## 8. 无有理尖点的全局映射与尖点挠性

令 $D$ 为 $X_{\overline{\mathbb Q}}$ 上所有几何尖点之和。它 Galois 不变，定义于 $\mathbb Q$，次数为
$$\delta=(p^2-1)/2.\tag{72.18}$$
定义
$$
f:X\longrightarrow A,\qquad
f(x)=q([\delta x-D]).
\tag{72.19}
$$
这是真实 $\mathbb Q$ 态射，不要求一个有理尖点。由 (72.17)，$\delta$ 是 $\mathbb Z_\ell$ 单位；所以若 $\ell$ 非 exceptional，§6 给 $f$ 在 $c_0$ 形式浸入。

下面直接证明所需的 $f(c)$ 挠性，不需要假定一个未经控制的尖点分母。

对任何几何尖点 $c$，除子
$$Z_c=\delta[c]-D$$
为次数零的尖点除子。每个 $\pi_i$ 将尖点送到 $X_0(p)$ 的 $0$ 或 $\infty$，故
$$\pi_{i,*}[Z_c]=n_i([0]-[\infty])\in J_0(p)(\overline{\mathbb Q})$$
对某个整数 $n_i$ 成立。而
$$u(z)=\frac{\Delta(z)}{\Delta(pz)}$$
是 $X_0(p)$ 上的模单位，且
$$\operatorname{div}(u)=(p-1)([0]-[\infty]).\tag{72.20}$$
在 $\infty$，其阶为 $1-p$；利用 $w_p$ 可得在 $0$ 的阶为 $p-1$；上半平面无零极点。所以每个 $\pi_{i,*}[Z_c]$ 均为挠点。

R69 中 $\Theta=(\pi_{i,*})_i$，且 $q_0$ 由 $\Theta$ 后接整倍清分母的同态构造。因此 $q_0[Z_c]$ 为挠点。因 $A\to B$ 是同源，$q[Z_c]=f(c)$ 也为挠点：
$$f(c)\in A(\overline{\mathbb Q})_{\rm tors}.\tag{72.21}$$
此论证不要求同源次数素于 $\ell$。同源的有限核只用于从一个挠像推出原像挠。

另一方面，
$$f(P)\in A(\mathbb Q)$$
属于 R69 已证明有限的群，故也为挠点。

## 9. 形式浸入完成分母排除

反设 $\ell$ 非 exceptional。由 §§7–8，$P,c$ 约化到同一个 $c_0$，并且
$$f(P),f(c)\in A(\mathbb Q_\ell)_{\rm tors}.$$
它们的差在好约化的形式群
$$A_1(\mathbb Q_\ell)
=\ker\bigl(\mathcal A(\mathbb Z_\ell)\to\mathcal A(\mathbb F_\ell)\bigr)$$
中。$\ell>2$ 时这个群无挠：可用定义在 $\ell\mathbb Z_\ell^{\dim A}$ 上的形式对数，也正是 Mazur (1978), §1(c) 的 Specialization Lemma 在 $e=1<\ell-1$ 下的阿贝尔簇情形。因此
$$f(P)=f(c).\tag{72.22}$$

而 $f$ 在 $c_0$ 是形式浸入。其完整局部环映射满射，所以同一剩余圆盘内、具有相同 $f$ 像的两个 $\mathbb Z_\ell$ 截面相等。由 (72.22) 得 $P=c$，与 $P$ 非尖点、$j(P)=j(F)$ 有限矛盾。

所以 $\ell$ 必 exceptional。结合 (72.16)，定理 72.1 得证。R66 给 $p>M$ 时 (72.1) 成立，推论 72.2 随即成立。

## 10. 这一步解决和未解决的接口

R69 的有理分解不自动说明整微分非退化；本篇通过最优化、Raynaud–Mazur 正合性、Tate 展开和整个尖点除子，给出完整补充。对符合条件的实际 $F$，它把分母支撑严格限制到 exceptional 集。

仍然保留的条件是：

- 必须有 (72.1)，目前可由 $p>M$ 保证；本篇没有统一估计变化的 $M$。
- exceptional 的定义仍是三个和在同一剩余素理想共同消失；没有证明所有 $p$ 均无这种素数。
- 完整惯性分支不在本定理的设置中。
- 即使某个同余类由本篇得到整 $j$，也不能在没有额外刚性定理时把它推广成所有实际异常曲线不存在。

因此该结果关闭的是一个真实的整格与形式浸入接口，不是主问题的完成。

## 11. 已发表来源与证明归属

- B. Mazur, **Rational isogenies of prime degree**, with an appendix by D. Goldfeld, *Invent. Math.* **44** (1978), 129–162，DOI [10.1007/BF01390348](https://doi.org/10.1007/BF01390348)，[作者保存的原刊全文](https://www.math.columbia.edu/~goldfeld/Mazur-Goldfeld1978.pdf)。Proposition 1.2, pp.135–136；Corollary 1.1, p.137；§1(c) 的 Specialization Lemma, p.135。这里使用其一般好约化最优商输入，未把其关于 $X_0(N)$ 的 Corollary 4.3 直接套到扭曲完整水平曲线。
- M. Raynaud, **Schémas en groupes de type $(p,\ldots,p)$**, *Bull. Soc. Math. France* **102** (1974), 241–280，[原刊全文](https://www.numdam.org/article/BSMF_1974__102__241_0.pdf)，Théorème 3.3.3、Corollaire 3.3.6(1), p.268。严格小分歧条件在本篇为 $1<\ell-1$。
- P. Deligne and M. Rapoport, **Les schémas de modules de courbes elliptiques**, *Lecture Notes in Mathematics* **349** (1973), 143–316，[作者全文](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/Lesschemas.pdf)。IV 的水平结构与紧化、VII §2 的 Tate 尖点参数及 VII Théorèmes 3.9–3.10 的展开原则；本篇 §4 写出了好约化时所需的积分性论证，§5 直接计算忘线映射。
- A. Agashe, K. Ribet and W. Stein, **The Manin constant**, *Pure Appl. Math. Q.* **2** (2006), 617–636，[作者保存的发表版](https://wstein.org/papers/ars-manin/agashe-ribet-stein-the_manin_constant.pdf)，Theorem 3.5、§4.1。其任意维最优商结果也给 $\ell\nmid p$、$\ell$ 奇时的相应 Manin 格结论，和 §2 的推导一致。本篇不需要假设一般 Manin 常数猜想，也不使用只适用于椭圆商的结论替代高维商。
- [R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md)、[R69](R69-forgetful-maps-and-unconditional-rank-zero-quotient.md)：前者给实际惯性、$M$ 和已发表非消失，后者给实际 $\mathbb Q$ 商及有理点有限性。两者是本篇全局输入。
- Studnia，[arXiv:2507.20801v2](https://arxiv.org/html/2507.20801v2)，§3 提供同类 exceptional 定义和所欲结论；其 submitted 状态按作者页面核查。本篇没有把其 Theorem D 或 §3 的形式浸入断言作为输入，§§2–9 已给出本题所需的独立证明。
