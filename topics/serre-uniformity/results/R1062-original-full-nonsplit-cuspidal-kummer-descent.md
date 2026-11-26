# R1062：完整非分裂 Cartan 曲线的无基点 cuspidal Kummer 标签

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126；global_route，root 复核。

**已证明。** 对每个 $p>37$，完整原曲线 $X_{\rm ns}^+(p)$ 上的每个非 cusp 有理点，
都给出同一个真实 cuspidal $p$-torsion 模块上的、支撑固定在 $2,3,p$ 的有限全局
Kummer 标签。构造不用指定 CM 有理基点，覆盖非整 $j$、完整 $I_p$ 及变化二次域。
同时给出其真实 Galois 角色、无条件 $\lfloor p/4\rfloor-1$ 个一维分量，
以及辅助好素处的全部点约化条件。

这些是全局必要条件，**尚未排除非 CM 点**。还证明：对 regular $p$，
这个 ambient 全局标签空间向单独 $p$ 处的全部允许标签满射，
故单独这一局部比较不筛除任何 $p$-adic 点。
不把几何 $p$-torsion 当作 $\mathbf Q$-rational torsion，
不假设 Vandiver，不省略 $S$-class group，也不声称所有 Kummer twists 有局部点。

本文全部为纸面证明，无数学程序执行。

## 1. 原曲线、真实 cusp 格和 Galois 方向

设
$$
X=X_{\rm ns}^+(p),\qquad m=(p-1)/2,\qquad
F=\mathbf Q(\zeta_p)^+,\qquad
G=\operatorname{Gal}(F/\mathbf Q)=\mathbf F_p^\times/\{\pm1\}.
\tag{1062.1}
$$
$X$ 对应完整非分裂 Cartan 正规化子，定义在 $\mathbf Q$ 上。
令 $\Sigma$ 为它的全部 $m$ 个几何 cusps。它们全部定义在 $F$，
并形成一个简单传递的 $G$-轨道。置
$$
D_0=\operatorname{Div}^0_\Sigma(X_F),\qquad
U=\{u\in F(X)^\times:\operatorname{supp}\operatorname{div}u
       \subset\Sigma\}/F^\times,
$$
$$
C_\Sigma=D_0/\operatorname{div}(U)\subset J(F).
\tag{1062.2}
$$
$C_\Sigma$ 是几何 cusp-generated divisor class group，
不是预先限定为 $J(\mathbf Q)$ 中的挠群。

所用已发表来源是 Carlucci [C] 的 Theorem 6.5、Remark 6.6、
Theorem 7.1、Remark 7.2、Theorem 8.3。
作者全文的 PDF 第22–25页给单位与 Galois 格，第30页给定义域。
另一个预印本 [CP] 的 Theorem 3.2 只作发现线索；
下面所需的 $p$-torsion 下界完整重证，不直接引用它。

为固定方向，取 $\mathbf F_p^\times$ 的生成元 $g$。
[C, Remark 6.6] 中的行列式为 $g$ 的场自同构 $\rho$，
在常数上是 $\zeta_p\mapsto\zeta_p^g$，且固定 $X$ 的 $\mathbf Q$ 函数域。
它在 $F(X)$ 上正是实际 $\sigma_g$。选一个 cusp $c_1$，标记
$$
c_h=\sigma_h(c_1)\quad(h\in G).
$$
[C, Remark 7.2] 明确给出
$\operatorname{div}(\rho^j u)=w^j\operatorname{div}(u)$。
所以 $D_0=\mathbf Z[G]_0$ 上的左作用就是实际 Galois 作用。
下式中的逆号属于 Stickelberger 系数，不能再把整个 Galois 作用反转。

记
$$
R=\mathbf Z[G],\qquad d=\frac{12}{\gcd(12,p+1)},\qquad
R_d=\{a\in R:d\mid\operatorname{aug}(a)\}.
$$
在 $\mathbf F_{p^2}=\mathbf F_p(\sqrt\delta)$ 中取 $\delta$ 为非平方，
$T(a+b\sqrt\delta)=a$，$N(a+b\sqrt\delta)=a^2-\delta b^2$。
令 $B_2(t)=t^2-t+1/6$。来源给出
$$
\theta=\frac p2\sum_{z\in\mathbf F_{p^2}^\times/\{\pm1\}}
 B_2\!\left(\left\langle\frac{T(z)}p\right\rangle\right)
 [N(z)]^{-1},
\qquad C_\Sigma=R_0/(R_d\theta).
\tag{1062.3}
$$
其中 $[N(z)]$ 是 $G$ 中的类。
$d>1$ 时，单个 Siegel product $G_h$ 不必已经是 $X$ 上函数；
满足 $d\mid\sum_h n_h$ 的 power product 才是实际单位。
因此 (1062.3) 保留真正的 $R_d$。

全部 cusps 在 $F$ 上有理。若一个 $F$-rational cusp divisor
在 $\overline{\mathbf Q}$ 上 principal，其对应的一维
Riemann–Roch 空间由基变换在 $F$ 上已有非零函数。
所以 (1062.2) 的 $F$-unit 格确给完整几何 principal cusp 格，
没有因为定义域而遗漏主除子。

## 2. 实际 $p$-torsion 模块及无条件角色下界

令 $\omega:\mathbf F_p^\times\to\mathbf Z_p^\times$ 为 Teichmüller 字符。
因为 $p\nmid d$，张量 $\mathbf Z_p$ 后 $R_d=R$。
对非平凡偶字符 $\chi$，令
$$
e_\chi=\frac1m\sum_{h\in G}\chi(h)^{-1}h.
$$
(1062.3) 给出
$$
(C_\Sigma\otimes\mathbf Z_p)_\chi
  \simeq \mathbf Z_p/(S_{\chi^{-1}}),
\qquad
S_\psi=\frac p4\sum_{z\in\mathbf F_{p^2}^\times}
 B_2\!\left(\left\langle\frac{T(z)}p\right\rangle\right)\psi(Nz).
\tag{1062.4}
$$
整性由 $R_d\theta\subset R$ 和 $p\nmid d$ 得到；
$S_{\chi^{-1}}\ne0$ 由 Manin–Drinfeld 的有限性得到。
每个非平凡字符在 $C_\Sigma[p]$ 中至多一维。
$R_0$ 的 trivial 分量为零，故
$$
C_\Sigma[p]^G=0.
\tag{1062.5}
$$

下面直接证明一组无条件非零分量。置
$$
\eta=\omega^m,\qquad \psi=\omega^{2j},\qquad
1\le j\le\lfloor p/4\rfloor-1.
$$
$\psi,\eta,\psi\eta,\psi^2$ 都非平凡。
对 $a\ne0$，按范数纤维计数，
$$
\sum_{b\in\mathbf F_p}\psi(a^2-\delta b^2)
 =-\psi(a)^2J(\psi,\eta),\qquad
J(\psi,\eta)=\sum_{z\in\mathbf F_p}\psi(z)\eta(1-z).
$$
因为范数为 $n$ 的 $b$ 的数目是 $1-\eta(a^2-n)$，
且 $\sum_n\psi(n)=0$。$a=0$ 时的和也是零，因为 $\psi^2\ne1$。
于是
$$
S_\psi=-\frac14J(\psi,\eta)B_{2,\psi^2},
\qquad
B_{2,\psi^2}=p\sum_{a=1}^{p-1}\psi(a)^2B_2(a/p).
\tag{1062.6}
$$

模 $p$ 展开
$$
J(\psi,\eta)\equiv\sum_{z\in\mathbf F_p}z^{2j}(1-z)^m.
$$
因 $2j<m$，所有幂严格小于 $p-1$，故该和为零。
对 $\psi^{-1}=\omega^{2(m-j)}$，唯一 $p-1$ 次幂给出
$-\binom m{2j}\ne0\bmod p$，故反向 Jacobi 和是单位。
Gauss 和恒等式
$G(\alpha)G(\alpha^{-1})=\alpha(-1)p$，
应用于 $\psi,\eta,\psi\eta$，准确给
$$
J(\psi,\eta)J(\psi^{-1},\eta)=p.
$$
从而 $v_pJ(\psi,\eta)=1$。

另一方面
$$
B_{2,\psi^2}
 =\frac1p\sum_{a=1}^{p-1}a^2\psi(a)^2
  -\sum_{a=1}^{p-1}a\psi(a)^2
  +\frac p6\sum_{a=1}^{p-1}\psi(a)^2.
$$
首和模 $p$ 是 $\sum a^{4j+2}=0$，
因为所选范围保证 $0<4j+2<p-1$；其余项整。
因此 $S_\psi\in p\mathbf Z_p$，并由 (1062.4) 得
$$
\boxed{\quad
 \bigoplus_{j=1}^{\lfloor p/4\rfloor-1}
       \mathbf F_p(\omega^{-2j})\ \subset C_\Sigma[p].
 \quad}
\tag{1062.7}
$$
每个所列分量准确一维。
不排除其它 irregular 分量；它们仍由完整 $\theta$ 保留。

## 3. 从 divisor classes 到实际函数

定义
$$
U_p=\{u\in U:\operatorname{div}u\in pD_0\},
\qquad V=U_p/pU.
\tag{1062.8}
$$
有实际 $G$-同构
$$
V\xrightarrow{\sim}C_\Sigma[p],
\qquad [u]\longmapsto[\operatorname{div}u/p].
\tag{1062.9}
$$
满射是 cusp class 被 $p$ 杀的定义。
若 $\operatorname{div}u/p=\operatorname{div}v$，
则 $u/v^p$ 为常数，恰给核 $pU$。
所有函数均在 $F(X)$，Galois 作用仍按 §1。

这不是把 (1062.7) 中的非平凡几何角色宣布为 $\mathbf Q$ 上的函数：
事实上 (1062.5) 正说明没有非零的 rational cuspidal $p$-torsion。
下面使用整个实际 $G$-模块及 equivariant 标签。

## 4. 足够的整模型与互不相交 cusps

令 $S$ 为 $F$ 中全部位于 $2,3,p$ 上的有限素位。
$X$ 有 $\mathcal O_F[1/(6p)]$ 上 smooth proper、
几何连通的模型 $\mathscr X$，cusps 闭包为互不相交的 sections。

原始输入为 Deligne–Rapoport [DR]：

- IV Theorem 2.5：full-level proper smooth 与 finite étale cusps，
  PDF 第68页／印刷210页。
- IV Corollary 2.9：full-level 为 projective smooth scheme，
  PDF 第69页／印刷211页。
- IV Theorem 3.4：一般 $H$ 的 stack 为 proper smooth，cusps finite étale，
  PDF 第70页／印刷212页。
- VI §1.9–2：除 $2,3$ 的 elliptic automorphism 描述，
  PDF 第129页／印刷271页。

具体 coarse 结论可直接从 full level 取得。
在固定 Weil component 上取
$(N_{\rm ns}\cap\mathrm{SL}_2(\mathbf F_p))/\{\pm1\}$ 的商。
在 $\ell\nmid6p$ 处，非 cusp stabilizer 的阶为 $1,2,3$；
cusp stabilizer 是该群与 unipotent cusp stabilizer 的交，
因其群阶 $p+1$ 与 $p$ 互素而平凡。
在完成严格 henselian 局部环中，对 tame stabilizer 平均参数，
得到 $\mathcal O[[t]]^I=\mathcal O[[t^e]]$，
故 coarse 商仍 smooth。
full cusp finite étale scheme 的有限轨道商仍 finite étale。
$\det N_{\rm ns}=\mathbf F_p^\times$ 给出原 $\mathbf Q$ 下降。

泛纤维几何连通；proper smooth 的几何连通分量数局部常数，
所以各纤维几何连通，从而光滑曲线纤维几何不可约。
cusps 泛点全在 $F$ 上，finite étale 闭包于是分裂为互不相交的 sections。
本篇只消费 $\mathbf Z[1/(6p)]$，不擅自删除 $2,3$。

## 5. 无基点的 leading-coefficient 归一化

对 $[u]\in U_p$，写
$$
\operatorname{div}u=p\sum_{c\in\Sigma}n_c[c],
\qquad \sum_c n_c=0.
$$
在每个 $c$ 取任意 $F$-rational uniformizer $t_c$，定义
$$
\operatorname{lc}_c(u;t_c)
 =\left.(u/t_c^{pn_c})\right|_c\in F^\times.
$$
换 $t_c$ 为 $a_ct_c+O(t_c^2)$，该值乘 $a_c^{-pn_c}$，
所以其 $F^\times/F^{\times p}$ 类与参数无关。置
$$
\tau_\Sigma(u)=\prod_{c\in\Sigma}\operatorname{lc}_c(u)
       \quad\text{in }F^\times/F^{\times p}.
$$
对任意非 cusp $x\in X(\mathbf Q)$，定义
$$
\boxed{\quad
\Phi_x([u])=
 \left[\frac{u(x)^m}{\tau_\Sigma(u)}\right]
       \in F^\times/F^{\times p}.
\quad}
\tag{1062.10}
$$

这是实际 $G$-equivariant $\mathbf F_p$-linear 映射。

1. $u$ 乘常数 $a$ 时，分子和 $m$ 个 leading coefficients 的乘积
   都乘 $a^m$，准确抵消。
2. $u$ 乘 $v^p$ 时，分子和各 leading coefficient 的变化都是 $p$ 次幂，
   故降至 $V=U_p/pU$。
3. leading coefficient 对乘法相容，故映射线性。
4. 在 $\sigma c$ 处选 $\sigma t_c$，则
   $\operatorname{lc}_{\sigma c}(\sigma u)
   =\sigma\operatorname{lc}_c(u)$。
   $\Sigma$ 为 $G$-stable 且 $x$ 为 $\mathbf Q$ 点，
   所以 $\Phi_x(\sigma[u])=\sigma\Phi_x([u])$。

这个归一化没有选择任何 CM 有理基点。
$\Sigma_0=\sum_c[c]$ 是 $\mathbf Q$-rational degree $m$ divisor，
原点给出
$$
i_\Sigma(x)=[m[x]-\Sigma_0]\in J(\mathbf Q).
$$
(1062.10) 是此 divisor 的 regularized function evaluation；
$\operatorname{ord}_c u\in p\mathbf Z$ 使 tangent ambiguity 消失。
若另有非 cusp $y\in X(\mathbf Q)$，则
$$
\Phi_x([u])/\Phi_y([u])
       =[u(x)/u(y)]^m.
\tag{1062.11}
$$
$m$ 在 $\mathbf F_p$ 中可逆，故与通常有基点 descent 比较时没有丢失信息。

## 6. 固定支撑，不排除非整 $j$

固定 $\mathfrak q\notin S$，令 $\mathcal O=\mathcal O_{F,\mathfrak q}$，
$\pi$ 为 uniformizer，$Y=\mathscr X_{\mathfrak q}$ 为唯一几何不可约纤维。
在 regular smooth surface 上有准确 Cartier-divisor 等式
$$
\operatorname{div}_{\mathscr X}(u)
   =p\sum_c n_c\mathscr C_c+nY,\qquad n\in\mathbf Z.
\tag{1062.12}
$$
没有其它水平成分；只有一个垂直纤维成分。

在 cusp section $c$ 附近选整参数 $t_c$，其零除子正好是该 section。
因其它 cusp sections 不交，
$$
u=\pi^nt_c^{pn_c}\epsilon_c,\qquad
\epsilon_c\text{ 为局部单位}.
$$
所以
$$
v_{\mathfrak q}(\operatorname{lc}_c u)=n
       \quad\text{对所有 }c.
\tag{1062.13}
$$
properness 使 $x$ 延成 $\mathcal O$-section；拉回 (1062.12) 给
$$
v_{\mathfrak q}(u(x))=n+pI_x,\qquad
I_x=\sum_c n_c(\mathscr C_c,x)\in\mathbf Z.
$$
即使 $x$ 的约化是 cusp，或 $v_{\mathfrak q}(j(x))<0$，此式仍成立；
仅要求泛点 $x$ 不是 cusp。
由此
$$
v_{\mathfrak q}\!\left(\frac{u(x)^m}{\tau_\Sigma(u)}\right)
     =m(n+pI_x)-mn=mpI_x\in p\mathbf Z.
\tag{1062.14}
$$
每个好位可分别选整参数；§5 的参数独立性保证这些计算属于同一全局类。

置
$$
F(S,p)=
 \{a\in F^\times:v_{\mathfrak q}(a)\equiv0\pmod p
                    \text{ 对所有 }\mathfrak q\notin S\}/F^{\times p},
$$
$$
\mathscr L_p=\operatorname{Hom}_{\mathbf F_p[G]}(V,F(S,p)).
$$
因此
$$
\boxed{\quad \Phi_x\in\mathscr L_p
       \quad\text{对全部非 cusp }x\in X(\mathbf Q).\quad}
\tag{1062.15}
$$
$S$ 只含 $2,3,p$，与 $j(x)$ 的分母、对应椭圆曲线的坏素集合、
正规化子的二次域及 $I_p$ 大小无关。
所以这是 [R1003](R1003-global-scope-and-remaining-branches.md) 的完整 O0 输入，
不只覆盖旧 cubic family。

## 7. 有限全局标签及 class-group 项

有自然 $G$-equivariant exact sequence
$$
0\longrightarrow
 \mathcal O_{F,S}^\times/(\mathcal O_{F,S}^\times)^p
 \longrightarrow F(S,p)
 \longrightarrow\operatorname{Cl}(\mathcal O_{F,S})[p]
 \longrightarrow0.
\tag{1062.16}
$$
最后的映射把 $(a)=\mathfrak a^p$（忽略 $S$ 内素因子）送至
$[\mathfrak a]$。kernel 恰为 $S$-units；任一 $p$-torsion ideal class
选其 $p$ 次的 principal generator 给出 surjectivity。
$S$-unit 定理及 class group 有限性表明 $F(S,p)$ 和 $\mathscr L_p$ 都有限。

本文保留整个 $\operatorname{Cl}(\mathcal O_{F,S})[p]$。
没有 Vandiver 假设，也没有默认 circular units 的指数 prime to $p$。

## 8. 辅助好素处的实际全部点比较

设 $\mathfrak q\notin S$，剩余域为 $k_{\mathfrak q}$。
对 $[a]\in F(S,p)$，写 $v_{\mathfrak q}(a)=pe$，定义
$$
\operatorname{red}_{\mathfrak q}[a]
   =[\pi^{-pe}a\bmod\mathfrak q]
   \in k_{\mathfrak q}^\times/k_{\mathfrak q}^{\times p}.
\tag{1062.17}
$$
换 $\pi$ 只乘 $p$ 次幂，故此类 canonical。

对 $u$ 取 $u_0=\pi^{-n}u$，其中 $n$ 是 (1062.12) 的 vertical 系数。
它在 $Y$ 上约成有理函数 $\bar u$，满足
$$
\operatorname{div}_Y(\bar u)=p\sum_c n_c[\bar c].
$$
对 $y\in Y(k_{\mathfrak q})$，
若 $y$ 不是 cusp，令 $\operatorname{ev}_y(\bar u)=\bar u(y)$；
若 $y=\bar c$，则取同一整参数约化后的 leading coefficient。
定义
$$
\Psi_{\mathfrak q}(y)([u])
 =\left[\frac{\operatorname{ev}_y(\bar u)^m}
       {\prod_c\operatorname{lc}_{\bar c}(\bar u)}\right]
 \in k_{\mathfrak q}^\times/k_{\mathfrak q}^{\times p}.
\tag{1062.18}
$$
缩放 $u_0$ 的常数、换参数及 $u$ 乘 $v^p$，
均按 §5 抵消，所以这是 $V$ 上的实际 linear functional。
对 $x\in X(F)$ 非 cusp、约化为 $y$，准确有
$$
\operatorname{red}_{\mathfrak q}\Phi_x=\Psi_{\mathfrak q}(y).
\tag{1062.19}
$$
在非 cusp disk 直接约化；在 cusp disk 写
$u_0=t^{pn_c}\epsilon$，
$t(x)$ 的贡献为 $p$ 次幂，$\epsilon(x)$ 约为 leading coefficient。
因为剩余特征不为 $p$，$1+\mathfrak q\mathcal O$ 中单位皆为 $p$ 次幂，
没有漏掉 higher disk 条件。

对原 $x\in X(\mathbf Q)$，同一有理素数 $\ell\nmid6p$ 的全部
$\mathfrak q\mid\ell$ 上的约化来自同一个 $X(\mathbf F_\ell)$ 点。
所以对任意有限辅助素集 $\mathcal T$，同一全局标签属于
$$
\begin{aligned}
\mathscr L_p(\mathcal T)=
 \{\phi\in\mathscr L_p:\ &
 (\operatorname{red}_{\mathfrak q}\phi)_{\mathfrak q\mid\ell}
 \in
 \{(\Psi_{\mathfrak q}(y))_{\mathfrak q\mid\ell}:
                   y\in X(\mathbf F_\ell)\}\\
 &\text{对每个 }\ell\in\mathcal T\}.
\end{aligned}
\tag{1062.20}
$$
必须保全部 $\mathfrak q$ 之间的 Galois 关联及全部有限域点，包括 cusps。
选 $\ell\equiv1\bmod p$ 时全部 residue degree 为一，
且 $\mu_p\subset\mathbf F_\ell$，residue quotient 非平凡。
若 $p\nmid|k_{\mathfrak q}^\times|$，该位 quotient 为零，不给它虚假的筛选力。

还未证明 (1062.20) 为空、只由 CM 标签组成，
或存在对所有大 $p$ 可统一控制的辅助素集。

## 9. Regular $p$ 时，单独 $p$-local 比较完全满射

令 $\mathfrak p$ 为 $F$ 上唯一 $p$ 位，
$K=F_{\mathfrak p}$，$L=\mathbf Q_p(\zeta_p)$，$\lambda=\zeta_p-1$。
$K/\mathbf Q_p$ 的 ramification degree
$m=(p-1)/2<p-1$，所以 log/exp 在 $U_1(K)$ 与
$\mathfrak p\mathcal O_K$ 之间互逆，并给
$$
U_1(K)/U_1(K)^p
 \simeq\mathfrak p\mathcal O_K/p\mathfrak p\mathcal O_K.
\tag{1062.21}
$$
右侧按 $\lambda$ 的 $2,4,\ldots,p-1$ 阶过滤，
$\sigma_b$ 在 $\lambda^{2i}$ 级的作用为 $\omega(b)^{2i}\bmod p$。
由于 $p\nmid m$，每个偶字符恰出现一次。
$K^\times/K^{\times p}$ 另有 valuation 的 trivial 分量，
所以每个非 trivial 偶字符的部分恰为一维。

对每个非零模 $p$ 剩余类选一个奇整数代表 $a$，真正全局 real circular unit 为
$$
\eta_a=\zeta_p^{(1-a)/2}
       \frac{\zeta_p^a-1}{\zeta_p-1}\in\mathcal O_F^\times.
\tag{1062.22}
$$
此时 $(1-a)/2$ 是整数；每个非零剩余类都有这样的代表。该元素 real；
整比值的绝对 norm 为一，故确为 global unit。
仅为本地展开置 $u_a=\eta_a/a$。则
$u_a-1\in\lambda^2\mathcal O_L$。
$\log a$ 为 $G$ 不变量，所以非 trivial $\chi$ 上
$e_\chi\log\eta_a=e_\chi\log u_a$；
不把 $u_a$ 误叫 global unit，也不扩大 $S$。

只在 $\lambda^{p-1}$ 之前使用形式
$t=\log(1+\lambda)$ 的截断多项式，绝不把真正 $\log\zeta_p=0$
当作一个非零解析参数。
由于 $u_a-1\in\lambda^2$，log 展开第 $n\ge p$ 项的
$L$-valuation 至少
$$
2n-(p-1)v_p(n)\ge p+1.
$$
因此它们完全不影响 $\lambda^2,\ldots,\lambda^{p-3}$ 系数。
$n<p$ 时分母为单位；普通形式恒等式合法给出
$$
\log u_a\equiv
 \sum_{\substack{2\le r\le p-3\\r\ {\rm even}}}
 \frac{B_r(a^r-1)}{r\,r!}\,t^r
     \pmod{\lambda^{p-1}}.
\tag{1062.23}
$$
此处 $B_r$ 是通常 Bernoulli 数。
截断 $t$ 在 $\sigma_b$ 下模 $\lambda^{p-1}$ 变为 $bt$；
所有涉及的分母小于 $p$。
因此 $e_{\omega^r}$ 投影后的最低 $\lambda^r$ 系数为
$B_r(a^r-1)/(r\,r!)$，且 $t=\lambda+O(\lambda^2)$。

若 $p\nmid\operatorname{num}(B_r)$，选择 $a^r\ne1\bmod p$，
则真实 global unit $\eta_a$ 的该字符 localization 非零，
故射满唯一的一维 local 字符空间。
特别若 $p$ regular，即全部偶数 $2\le r\le p-3$ 的
$B_r$ 分子都不被 $p$ 整除，circular units 在每个非 trivial
字符上均满射。

由 (1062.5) 和 (1062.9)，$V^G=0$。
逐字符选上述单位，得到实际满射
$$
\boxed{\quad
 \operatorname{Hom}_{\mathbf F_p[G]}(V,F(S,p))
 \longrightarrow
 \operatorname{Hom}_{\mathbf F_p[G]}
       (V,K^\times/K^{\times p})
 \quad\text{在 regular }p\text{ 时满射}.
 \quad}
\tag{1062.24}
$$
所以任意非 cusp $x_p\in X(\mathbf Q_p)$ 的同一规范 local
$\Phi_{x_p}$，都能提升为某个 ambient global label。
只比较 $p$ 处这一必要条件，不会筛掉任何这样的 $p$-adic 点。

这不声称该标签来自 $\mathbf Q$ 点，不声称所有 twists 都有 $p$ 点。
本篇这一节只精确刻画 (1062.15) 的单 $p$ 处比较。
后继 [R1064](R1064-original-cuspidal-cover-descent-and-auxiliary-character-visibility.md)
§§1–2 已从同一规范函数完整构造统一 $\mathbf Q$-torsor；
其真实下降不改变本节满射和剩余共同标签条件。
真正剩余是辅助好素及同一全局标签的同时相容；
大量几何 torsion、固定 $S$ 或单 $p$-local descent 本身均不完成 Serre。

## 10. 来源与范围

- [C] P. Carlucci, *Cuspidal divisor class groups of non-split Cartan modular curves*,
  Acta Arith. 187 (2019), 301–327,
  [DOI](https://doi.org/10.4064/aa8516-6-2018)；
  [作者全文](https://arxiv.org/pdf/1605.00375)。
  使用已发表单位格及实际 Galois 作用；§2 的 forced $p$-torsion 自行证明。
- [CP] P. Carlucci, *Properties of cuspidal divisor class numbers of non-split Cartan modular curves*,
  2016，[作者预印本](https://arxiv.org/pdf/1605.09323)。
  只作发现线索，不引用其 Theorem 3.2 作为未付款输入。
- [DR] P. Deligne and M. Rapoport,
  *Les schémas de modules de courbes elliptiques*, LNM 349 (1973), 143–316，
  [作者全文](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/Lesschemas.pdf)。
  精确位置见 §4。
- M. Jaswal, *The rational points of the non-split Cartan modular curve of level 25*,
  2026，[作者全文](https://manvirjaswal.github.io/papers/xns-25/jaswal-xns-25.pdf)。
  Theorem 1.3、§3 的构造提供方法线索；
  本篇将需要的归一化、固定支撑与辅助约化完整证明。
  不引用其 level-$25$ 数值筛选、全局结论或其它未付款推论。

本文没有改变课题完成标准。全 O0 排除、统一 CM 标签浓缩及绝对常数仍开放。
