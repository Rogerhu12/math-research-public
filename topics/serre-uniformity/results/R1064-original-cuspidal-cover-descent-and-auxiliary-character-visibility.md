# R1064：完整非分裂 Cartan 尖点覆盖的下降、规范纤维与辅助素可见性

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明。** R1062 的无基点 Kummer 标签确由一个定义在 $\mathbf Q$ 上、
在完整 $X_{\rm ns}^+(p)$ 上处处 étale 的有限覆盖给出。
对其无条件存在的 forced characters，规范尖点纤维可准确写成真实圆单位的
平方角色分量；同时完全确定每个辅助好素能看见哪些分量。

对 regular $p$，任意允许的全局 twist 在每个 $F$-rational cusp 上的
$p^r$ 个几何纤维点构成一个次数 $p^r$ 的闭点。因此这个具体覆盖在
$\mathbf Q$ 或 $F$ 上不自动增加 Runge 所需的 cusp 轨道盈余。
这不是所有覆盖或所有全局路线不可能的断言。

这些结论没有排除原非 CM 有理点。实际剩余是：用同一个全局标签，
同时满足不同辅助素处的真实有限点集条件，进而排点。
全文是纸面证明，没有数学程序执行。

## 1. 真实模块和统一覆盖的具体定义

沿用 R1062：
$$
X=X_{\rm ns}^+(p),\quad p>37,\quad
m=(p-1)/2,\quad F=\mathbf Q(\zeta_p)^+,\quad
G=\operatorname{Gal}(F/\mathbf Q).
\tag{1064.1}
$$
全部 $m$ 个 cusp 构成简单传递的 $G$-集合 $\Sigma$。
固定 $c_1$，令 $c_h=\sigma_hc_1$，这里
$\sigma_h(\zeta_p)=\zeta_p^h$ 的限制采用 R1062 已核定的实际方向。

记
$$
U=\{u\in F(X)^\times:\operatorname{supp}\operatorname{div}u\subset\Sigma\}/F^\times,
\quad
U_p=\{u\in U:\operatorname{div}u\in p\operatorname{Div}^0_\Sigma(X_F)\},
$$
$$
V=U_p/pU\simeq C_\Sigma[p]\subset J(F).
\tag{1064.2}
$$
对任意 $G$-stable 子空间 $W\subset V$，置 $n=\dim_{\mathbf F_p}W$，
并令
$$
H_W=\operatorname{Hom}_{\mathbf F_p}(W,\mu_p)
\tag{1064.3}
$$
带实际 Galois 作用。它是 $\mathbf Q$ 上的有限 étale 群概形；
到 $F$ 后，$W$ 成为常数，$H_{W,F}\simeq\mu_p^n$。

若 $u$ 代表 $W$ 中的一个元素，写
$\operatorname{ord}_c u=pn_c$，取 $F$-定义的局部参数 $t_c$，置
$$
a_c(u)=\left.(u/t_c^{pn_c})\right|_c,\qquad
A(u)=\prod_{c\in\Sigma}a_c(u),\qquad
f_u=u^m/A(u).
\tag{1064.4}
$$
在泛点的 $p$ 次幂商中，
$$
W\longrightarrow F(X)^\times/F(X)^{\times p},
\qquad u\longmapsto[f_u]
\tag{1064.5}
$$
是一个实际 $\mathbf F_p$-线性同态。

完整的选择核查如下。改变 $t_c$ 只使 $a_c(u)$ 乘一个 $p$ 次幂；
把 $u$ 乘常数 $a$ 时分子乘 $a^m$，$A(u)$ 也乘 $a^m$，严格抵消。
把 $u$ 换成 $uv^p$，其中 $v\in U$，则
$f_{uv^p}=f_u(v^m/A(v))^p$，此处对 $A(v)$ 使用 $v$ 的实际整数阶。
乘法的 leading coefficients 相乘，所以 (1064.5) 线性。
此外
$$
A(\sigma u)/\sigma A(u)\in F^{\times p}
\tag{1064.6}
$$
因为 $\sigma t_c$ 与 $t_{\sigma c}$ 的 leading ratio 只以 $pn_c$ 次幂出现。
故 (1064.5) 在函数域中已经 $G$-equivariant，
不是只在某些有理点取值后才 equivariant。

选择 $W$ 的一组基 $u_1,\ldots,u_n$，在 $F(X)$ 上写
$$
z_i^p=f_{u_i}.
\tag{1064.7}
$$
对所有点，$\operatorname{div}f_{u_i}$ 都是 $p$ 的倍数。
在局部把 $t^{pN}$ 去掉后，(1064.7) 是对局部单位取 $p$ 次根；
特征零中其导数为单位。因此规范化给出整个 $X_F$ 上的有限 étale
$H_{W,F}$-torsor $Y_W\to X_F$，没有漏掉 cusps。

这个覆盖几何连通且次数为 $p^n$。事实上，若在
$\overline{\mathbf Q}(X)^\times/\overline{\mathbf Q}(X)^{\times p}$ 中
存在关系 $\prod_i f_{u_i}^{a_i}=h^p$，写
$\operatorname{div}u_i=pD_i$，则
$m\sum_i a_iD_i=\operatorname{div}h$。
由 (1064.2) 中 $W\hookrightarrow J[p]$ 的注入和 $p\nmid m$，
所有 $a_i$ 都为零。Kummer 理论于是给出次数 $p^n$ 的域扩张。
这也说明不把独立的几何 $p$-torsion 换成 $\mathbf Q$-rational torsion。

## 2. 严格的 $\mathbf Q$ 下降与实际 twists

先证明存在 descent isomorphisms，再使用其唯一性。

在 $F$ 上，$H_{W,F}$-torsor 的类由
$$
\operatorname{Hom}_{\mathbf F_p}
  \bigl(W,H^1_{\mathrm{\acute et}}(X_F,\mu_p)\bigr)
\tag{1064.8}
$$
描述；任选基即是 $n$ 个 Kummer torsor，换基按线性组合运输。
泛点限制
$H^1(X_F,\mu_p)\to F(X)^\times/F(X)^{\times p}$
是单射：一个泛点平凡的有限 étale torsor 在正常曲线上已经平凡，
可在规范化上逐个延拓其泛点截面。
上一节已构造 (1064.8) 中的类，而 (1064.6) 使它在采用
$W$ 的实际 $G$ 作用后保持不变。

因此对每个 $\sigma\in G$，$\sigma Y_W$ 与 $Y_W$ 的
$H_{W,F}$-torsor 类相同，**确实存在一个在 $F$ 上定义的
equivariant isomorphism**。这里不是仅有几何同构。
任一这种 torsor 的 equivariant automorphism 群是
$$
H_W(X_F)=H_W(F)=\operatorname{Hom}(W,\mu_p(F))=0,
\tag{1064.9}
$$
因为 $X_F$ proper、几何连通且 $F$ totally real、$p$ 为奇数。
故上述 isomorphism 唯一；两种复合给出的 descent isomorphism
也必须相同，自动满足 cocycle condition。
有限 étale 代数的 Galois descent 遂给出唯一的
$\mathbf Q$-定义覆盖
$$
Y_W\longrightarrow X.
\tag{1064.10}
$$
(1064.9) 只用于已证明存在之后的唯一性，没有以它替代存在性。

同样论证应用于 $\operatorname{Spec}F$，给出准确的标签识别
$$
H^1(\mathbf Q,H_W)
 \simeq
\operatorname{Hom}_{\mathbf F_p[G]}(W,F^\times/F^{\times p}).
\tag{1064.11}
$$
也可由 $p\nmid|G|$ 的 Hochschild–Serre 序列得到，但这里直接证明了
torsor descent。给定右侧 $\phi$，以其相应常数 torsor twist (1064.10)，
记为 $Y_{W,\phi}$。对 $x\in X(\mathbf Q)$，其纤维的 $F$-标签正是
R1062 的
$$
\Phi_x(u)=
\left[u(x)^m/\prod_{c\in\Sigma}a_c(u)\right].
\tag{1064.12}
$$
因此 $x$ 在 $Y_{W,\phi}$ 上有一个有理提升，当且仅当
$\Phi_x|_W=\phi$。在 cusp 用本地去掉 $p$ 次幂参数后的 leading coefficient
作同一取值。

取 $S=\{\mathfrak q:\mathfrak q\mid6p\}$，R1062 已证明所有原有理点的标签属于
$$
\mathscr L_{p,W}
 =\operatorname{Hom}_{\mathbf F_p[G]}(W,F(S,p)).
\tag{1064.13}
$$
这是有限集合，含完整 $S$-class-group 项。
于是所有原有理点都在这个**同一个真实有限 twist 家族**的像中。
这不是断言每个 twist 有有理点，也不是用任何未经证明的 local–global 原理。

## 3. Forced character 的规范基和原 Siegel 前导项

令
$$
r=\lfloor p/4\rfloor-1,\quad
\chi_j=\omega^{-2j},\quad
W_{\mathrm{for}}=\bigoplus_{j=1}^r V_{\chi_j}.
\tag{1064.14}
$$
R1062 已无条件证明各 $V_{\chi_j}$ 准确一维。
以下对其中一个 $\chi$ 计算，并固定其基的尺度。

采用原非分裂 Cartan 模型
$\mathbf F_{p^2}=\mathbf F_p(\sqrt\delta)$，
$N(a+b\sqrt\delta)=a^2-\delta b^2$，$\delta$ 为非平方。
Carlucci 的原 Siegel products 是
$$
G_h=\prod_{\substack{z\in\mathbf F_{p^2}^\times/\{\pm1\}\\ [Nz]=h}}g_{[z]},
\quad h\in G.
\tag{1064.15}
$$
选择整数 $n_h$ 使
$$
n_h\equiv m^{-1}\chi(h)^{-1}\pmod p,\qquad
\sum_h n_h=0.
\tag{1064.16}
$$
非平凡性使模 $p$ 的和为零，所以可调整一个指数的 $p$ 倍达到整数和零。
Carlucci Theorem 6.5 中的 $d\mid\sum n_h$ 条件于是确实满足。
其 Theorem 4.3 和同一范数纤维的二次矩条件保证原 raw product
$$
f_\chi=\prod_hG_h^{n_h}\in K_0(X)^\times,
\qquad K_0=\mathbf Q(\zeta_p).
\tag{1064.17}
$$
具体地，范数为 $\pm h$ 的完整纤维上
$\sum a^2=\sum b^2=\sum ab=0\bmod p$，
且全部 Siegel 指数之和为 $(p+1)\sum n_h=0$。
二次矩的零可直接核：每个 $N(z)=h$ 的圆是阶 $p+1$ 群的陪集，
故 $\sum z^2=\sum\bar z^2=0$；合并 $h,-h$ 后 $\sum Nz=0$。
由 $a=(z+\bar z)/2$、$b=(z-\bar z)/(2\sqrt\delta)$ 得上述三个矩。
按 $\pm1$ 取商只除以二，不改变零。这样支付 full-level 函数的全部同余条件。
Theorem 6.5 再支付实际 normalizer 的几何不变性。

由 R1062 的 $\theta$ 作用，
$\operatorname{div}f_\chi\in p\operatorname{Div}^0_\Sigma$。
其 divisor 的 $F$-rational Riemann–Roch 一维空间给出同 divisor 的
$F$-函数；记其 $V$ 类为 $u_\chi$。这是 (1064.16) 所固定的非零基。
不把 raw product 自动宣称为实系数函数。
真正的 norm
$$
w_\chi=f_\chi\overline{f_\chi}\in F(X)^\times
\tag{1064.18}
$$
在 $V$ 中的类准确为 $2u_\chi$。

置
$$
\varpi_b=(1-\zeta_p^b)(1-\zeta_p^{-b})
 =\sigma_b(\varpi_1),\quad
e_\psi=\frac1m\sum_{b\in G}\psi(b)^{-1}\sigma_b.
\tag{1064.19}
$$
本节的 $F^\times/F^{\times p}$ 采用加法记号。
对 $\psi\ne1$，$e_\psi[\varpi_1]$ 实际是一个全局单位类；
$\varpi_1$ 在 $p$ 处的唯一 valuation 属于 trivial character，投影后消失。

Siegel q-product 的已发表精确式为
$$
g_{(a_1,a_2)}=
-q^{B_2(a_1)/2}e^{\pi i a_2(a_1-1)}
\prod_{n\ge0}(1-q^{n+a_1}e^{2\pi ia_2})
             (1-q^{n+1-a_1}e^{-2\pi ia_2}).
\tag{1064.20}
$$
因此前导常数除 root of unity 外，只有 $a_1=0$ 时多出
$1-\zeta_p^b$。原索引中这些恰是 $z=b\sqrt\delta$，
$[Nz]=[-\delta b^2]$。
Carlucci Proposition 5.2 末证明 cusp width 为 $p$，
所以原 $q^{1/p}$ 是参数，没有额外 cusp ramification 倍数。

用 $K_0/F$ norm 计算 (1064.17) 的 leading coefficient，
**所有 root-of-unity 相位与其复共轭严格相消**。
不需要假设某个单项的相位本来只有 $\mu_p$ 阶。
若所选解析参数与 $F$-参数相差一个 leading unit，
其指数是 $\operatorname{ord}f_\chi\in p\mathbf Z$，
norm 后只改变 $p$ 次幂类。
于是
$$
[N_{K_0/F}\operatorname{lc}_{c_1}(f_\chi)]
 =\sum_{b\in G}n_{[-\delta b^2]}[\varpi_b]
 =\chi(-\delta)^{-1}e_{\chi^2}[\varpi_1].
\tag{1064.21}
$$
这里没有把任意乘常数的 raw product 当成已固定函数：
(1064.17) 是原 product；另乘常数时其影响将在完整规范化中抵消。

## 4. 全部 cusp 上的精确平方角色公式

令
$L_h=[N_{K_0/F}\operatorname{lc}_{c_h}(f_\chi)]$。
必须同时运输参数和 residue-field 常数：
$$
\operatorname{lc}_{c_h}(f_\chi)
 =\sigma_h\!\left(
   \operatorname{lc}_{c_1}(\sigma_h^{-1}f_\chi)\right)
\tag{1064.22}
$$
在允许的参数选择下成立；其它参数仍只改 $p$ 次幂类。

Carlucci Remark 6.6、Proposition 4.2 给
$\sigma_h^{-1}G_a=G_{ah^{-1}}$，差一个在 $K_0$ 中的 root of unity。
故 (1064.16) 的指数在 $\sigma_h^{-1}f_\chi$ 中变成
$n_{ah}\equiv\chi(h)^{-1}n_a$。
差的指数向量为 $p$ 倍且 augmentation 仍零，
所以对应差函数是实际 modular unit 的 $p$ 次幂；
root-of-unity 的 norm 仍严格为一。
最后，(1064.21) 的常数由 $\sigma_h$ 乘 $\chi(h)^2$。
两项合起来准确为
$$
L_h=\chi(h)\chi(-\delta)^{-1}e_{\chi^2}[\varpi_1],
\qquad
\sum_{h\in G}L_h=0.
\tag{1064.23}
$$
只移 cusp 指标而漏掉 (1064.22) 外侧的 $\sigma_h$ 会错误地得到逆角色。

把 (1064.23) 代入完整的 (1064.4)，并用
$[w_\chi]=2u_\chi$，得到原切向 cusp 值
$$
\boxed{
\Phi_{c_h}(u_\chi)=
\frac m2\,\chi(h)\chi(-\delta)^{-1}
e_{\chi^2}[\varpi_1]\quad\text{in }F^\times/F^{\times p}.
}
\tag{1064.24}
$$
这里的 $\Phi_{c_h}$ 正是 étale torsor 的实际 cusp 纤维，
并非仅取了未归一化的一个 Siegel 常数。

对 forced 范围，$2j<m$，故 $\chi_j^2\ne1$ 且所有
$\chi_j^2=\chi_{2j}$ 互不相同。
若 $p$ regular，则 R1062 的圆单位局部对数计算还给
$$
e_{\chi_j^2}[\varpi_1]\ne0.
\tag{1064.25}
$$
为明确其来源，选 $G$ 的生成元 $a$，取奇整数代表并设
$\eta_a=\zeta_p^{(1-a)/2}(\zeta_p^a-1)/(\zeta_p-1)$。
有
$$
(\psi(a)-1)e_\psi[\varpi_1]=2e_\psi[\eta_a].
\tag{1064.26}
$$
R1062 已对每个非平凡偶 $\psi$ 证明 regular $p$ 时右侧在 $p$ 处非零；
$\psi(a)-1$ 为单位，所以 (1064.25) 成立。
没有假设 Vandiver，也没有把 irregular 情形的分量擅自删去。

## 5. 任意全局 twist 的 cusp 纤维与准确的 Runge 边界

本节只在 $p$ regular 时断言。
取 $W=W_{\mathrm{for}}$ 和任意
$$
\phi\in\operatorname{Hom}_{\mathbf F_p[G]}(W,F^\times/F^{\times p}).
$$
固定任一 cusp $c_h$，其 twisted fibre 的 $r$ 个 Kummer 类是
$$
\beta_j=\Phi_{c_h}(u_{\chi_j})-\phi(u_{\chi_j}),
\quad 1\le j\le r.
\tag{1064.27}
$$
第一项是非零 $\chi_{2j}$ 分量，第二项纯属 $\chi_j$。
这些类线性独立。若存在非零线性关系，取系数非零的最大指标 $j$，
投影到 $\chi_{2j}$：

- 所有 $2i$ 都在 $[2,2r]\subset[1,m-1]$，所以
  $\chi_{2i}=\chi_{2j}$ 只可能 $i=j$；
- 若某个第二项角色 $\chi_i=\chi_{2j}$，则因
  $1\le i\le r<m$ 且 $2j<m$，必须 $i=2j>j$，
  与 $j$ 的最大性矛盾。

故投影只剩第 $j$ 项的非零圆单位，矛盾。
此处完整检查了模 $m$ 的碰撞，没有把字符编号当作无界整数。

限制 $F^\times/F^{\times p}\to K_0^\times/K_0^{\times p}$ 是单射，
因为随后 norm 是乘二，$p$ 为奇数。
所以 (1064.27) 在含 $\mu_p$ 的 $K_0$ 上仍独立，
Kummer 纤维代数是次数 $p^r$ 的域。
原 $F$-纤维代数张量 $K_0$ 后是域，故其自身也是域、次数仍为 $p^r$。

因此在 $Y_{W,\phi}/F$ 上，每个原 cusp 只给一个闭点；
全部 cusp 闭点数是 $m$。在 $\mathbf Q$ 上，
原 cusps 构成一个 Galois 轨道，且每个纤维在 $G_F$ 下已传递，
所以整个 cusp 逆像仍是一个次数 $mp^r$ 的闭点。
分别与 $F$ 的 $m$ 个 archimedean places、$\mathbf Q$ 的一个
archimedean place 相比，都仍是相等，未产生 Runge 严格盈余。
若再加入有限 places，所需 Runge 不等式只会更严格。

该结论只检查这个明确的 forced-character twist 家族及这些基域；
不宣称任意其它覆盖、基域、height 方法或辅助局部组合都不可能。

## 6. 辅助好素的完整可见性

设 $\ell\nmid6p$ 为有理素数。R1062 的原 smooth proper 模型及
disjoint cusp sections 使 (1064.10) 和所有 (1064.13) 中的 twists
在 $\ell$ 处延拓为有限 étale covers。

具体地，允许先在该素使用整局部参数；这种更换在 Kummer 类中只改 $p$ 次幂。
在 $\mathfrak q\mid\ell$ 的模型上若
$\operatorname{div}u=p\sum n_c\mathscr C_c+nY$，
则每个 $a_c(u)$ 的 valuation 都是 $n$，所以
$\operatorname{div}(u^m/A(u))=mp\sum n_c\mathscr C_c$，
没有剩余 vertical divisor。常数 twist 的 valuation 又为 $p$ 倍。
有限 étale 延拓与无分歧的 $F/\mathbf Q$ descent 相容。

于是有真正的有限点集标签
$$
\delta_\ell:X(\mathbf F_\ell)\longrightarrow
H^1(\mathbf F_\ell,H_W).
\tag{1064.28}
$$
在 forced 分量上，
$$
H_{\chi_j}=\operatorname{Hom}(V_{\chi_j},\mu_p)
\quad\text{的 Galois 角色是}\quad
\omega\chi_j^{-1}=\omega^{2j+1}.
\tag{1064.29}
$$
有限域的 Galois 群为 procyclic，所以
$$
H^1(\mathbf F_\ell,H_{\chi_j})
 =H_{\chi_j}/(\operatorname{Frob}_\ell-1)H_{\chi_j}
 =
\begin{cases}
\mathbf F_p,&\ell^{2j+1}\equiv1\pmod p,\\
0,&\text{否则}.
\end{cases}
\tag{1064.30}
$$
这里采用 arithmetic Frobenius；换 geometric Frobenius 不改可见条件。

也可直接核原 $F$-标签而不用覆盖语言。
设 $d_\ell=\operatorname{ord}_p(\ell)$，$\mathfrak q\mid\ell$。
若 $d_\ell$ 为偶数，则 $F$ 的 residue degree 为 $d_\ell/2$，
$\ell^{d_\ell/2}=-1\bmod p$，故
$k_\mathfrak q^\times/k_\mathfrak q^{\times p}=0$。
若 $d_\ell$ 为奇数，则 residue degree 为 $d_\ell$，
分解群由 $\sigma_\ell$ 生成，它在非零 residue $p$-quotient 上作用为乘 $\ell$。
一个 $y\in X(\mathbf F_\ell)$ 的标签为分解群 equivariant，
所以 $V_\chi$ 的读数非零必须满足 $\chi(\ell)=\ell$；
对 $\chi_j$ 正是 (1064.30)。

由此得到：

1. $d_\ell$ 为偶数时，全部 cusp $p$-torsion 的 residue 标签都不可见，
   不只是所选 forced 分量；所有 dual characters 都是奇字符。
2. $d_\ell$ 为奇数时，第 $j$ 个 forced 分量只在
   $d_\ell\mid(2j+1)$ 时可见。
3. 若 $\gcd(2j+1,p-1)=1$，该分量只在
   $\ell\equiv1\bmod p$ 的辅助素可见。
   特别地，$p\equiv2\bmod3$ 时第一个 forced 分量只有这种辅助素能读。
4. 若 $p=2q+1$ 且 $q$ 为奇素数，则本 forced 范围满足
   $3\le2j+1<q$，每个 $\omega^{2j+1}$ 都 faithful；
   因而整个 forced 家族只有在 $\ell\equiv1\bmod p$ 才可见。

这些是必要的 exact visibility 条件。
可见不意味着 (1064.28) 满射，也不意味着其像已经算出。

## 7. 固定小素集合的角色覆盖界与真实后继条件

固定一个有限有理素集合 $T$，并令 $p\notin T$ 趋于无穷。
对每个可用 $\ell\in T$，
$$
d_\ell\ge\frac{\log(p+1)}{\log\ell}
\tag{1064.31}
$$
因为 $p\mid\ell^{d_\ell}-1$。
奇数 $d_\ell$ 可见的 forced 指标至多 $r/d_\ell+1$，
偶数 $d_\ell$ 一个也没有。因此全部 $T$ 能看见的 forced 角色数至多
$$
\sum_{\ell\in T,\ \ell\nmid6p}
 \left(\frac{r\log\ell}{\log(p+1)}+1\right)
 =O_T\!\left(\frac p{\log p}\right).
\tag{1064.32}
$$
而 forced 模块维数 $r\sim p/4$。
所以一个固定小素列表不能读取全部 forced 角色；
这不排除它读取的少数角色已经筛除某些标签或点。

对任意原有理点，实际条件仍必须使用**同一个**
$\phi=\Phi_x|_W\in\mathscr L_{p,W}$：
$$
\operatorname{loc}_\ell(\phi)\in
\delta_\ell\bigl(X(\mathbf F_\ell)\bigr)
\quad\text{对所有选定的 }\ell\nmid6p.
\tag{1064.33}
$$
在一个固定 $\ell$ 处也不能逐角色任意挑不同约化点；
(1064.28) 要由同一个 $y\in X(\mathbf F_\ell)$ 给出完整向量。
若一个点在该素约化到 cusp，(1064.24) 便给完整的实际 cusp 向量，
仍保同一 $h$、全部圆单位与所有可见角色。

下一项真正未付输入是 (1064.33) 对适当、可随 $p$ 变化的辅助素的
共同像排除。本文没有把可见性、cover degree 或 Runge 边界当成这个排除。

## 8. 可见商给出真实有限辅助范围

本节继续取 $W=W_{\mathrm{for}}$；全部维数 $r,s$ 均指这个明确子覆盖。

令 $s=s(\ell)$ 为 (1064.30) 的可见 forced 角色数。
在 $\mathbf F_\ell$ 上，Frobenius 的阶整除 $p-1$，
因此有限 étale 群准确分裂为
$$
H_W=H_{\rm vis}\oplus H_{\rm nv},
\qquad H_{\rm vis}\simeq(\mathbf Z/p\mathbf Z)^s,
\quad
H^0(\mathbf F_\ell,H_{\rm nv})
 =H^1(\mathbf F_\ell,H_{\rm nv})=0.
\tag{1064.34}
$$
对任意 $\phi\in\mathscr L_{p,W}$，上一节已支付其好约化。
取实际 quotient cover
$$
Z_{\phi,\ell}=Y_{W,\phi,\mathbf F_\ell}/H_{\rm nv}
 \longrightarrow X_{\mathbf F_\ell}.
\tag{1064.35}
$$
它几何连通、étale、次数 $p^s$，是 visible 常数群的 torsor。
几何连通性来自上一节的 proper smooth 好模型及几何连通泛纤维，
在未分歧特殊化下保持；不是另行假设每个模 $\ell$ cover 连通。
对每个 $z\in Z_{\phi,\ell}(\mathbf F_\ell)$，
其逆像是一个 $H_{\rm nv}$-torsor。
(1064.34) 的 $H^1=0$ 给出一个有理点，$H^0=0$ 给出唯一性。
所以实际上有双射
$$
Y_{W,\phi}(\mathbf F_\ell)
 \xrightarrow{\;\sim\;} Z_{\phi,\ell}(\mathbf F_\ell).
\tag{1064.36}
$$
特别地，$s=0$ 时右侧就是 $X(\mathbf F_\ell)$；
此时没有额外 Kummer 筛力。
这里不把 $X(\mathbf F_\ell)$ 本身的非空性无声略去。

令 $g_X$ 为原 $X$ 的 genus。Riemann–Hurwitz 给出
$$
g_{\rm vis}=1+p^s(g_X-1).
\tag{1064.37}
$$
对这个实际光滑、projective、几何连通的 quotient，
Weil 界是
$$
\#Z_{\phi,\ell}(\mathbf F_\ell)
 \ge\ell+1-2g_{\rm vis}\sqrt\ell.
\tag{1064.38}
$$
因此若
$$
\ell+1>2\bigl(1+p^{s(\ell)}(g_X-1)\bigr)\sqrt\ell,
\tag{1064.39}
$$
则**每个**允许的全局 twist 在该辅助素都有点；
(1064.33) 对整个 $\mathscr L_{p,W}$ 自动成立。
例如 $\ell>4g_{\rm vis}^2$ 是一个便于使用的充分条件。
因为 $s(\ell)\le r$，故所有
$$
\ell>4\bigl(1+p^r(g_X-1)\bigr)^2,\qquad \ell\nmid6p,
\tag{1064.40}
$$
都不能提供这个 Kummer 家族的额外有限域排除。

这个结论同时保留完整同标签条件和真正好约化，
不是把高 genus 原 cover 的虚构小 quotient 当作输入。
它给出了固定 $p$ 时实际辅助搜索的有限范围，
以及应优先查看的可见角色。
本文没有据此声称有限范围内的共同像已经为空，
也没有处理 $2,3,p$ 的未付局部条件。

## 来源与消费范围

- R1062：完整原 $V$、forced characters、无基点归一化、
  $\mathbf Z[1/6p]$ 模型、有限 $F(S,p)$ 标签和 regular $p$ 的圆单位局部计算。
- P. Carlucci, *Cuspidal divisor class groups of non-split Cartan modular curves*,
  Acta Arith. 187 (2019), 301–327, DOI 10.4064/aa8516-6-2018。
  作者全文 https://arxiv.org/pdf/1605.00375 ，
  Proposition 4.2、Theorem 4.3；PDF15–16页的 Proposition 5.2、原索引及 $G_h$；
  Theorem 6.5、Remark 6.6；Theorem 7.1、Remark 7.2。
  本文只消费这些已发表的 modular-unit、参数及 Galois 公式，
  新平方角色、下降、纤维独立和辅助素结论均在正文证明。
- Y. Bilu, P. Parent, M. Rebolledo,
  *Rational points on $X_0^+(p^r)$*, Ann. Inst. Fourier 63 (2013), 957–984，
  Eq. (3.3)，印刷第965页：
  https://www.numdam.org/item/10.5802/aif.2781.pdf 。
  这里只使用原 Siegel infinite-product 公式，没有移用 split-Cartan 排点结论。

- Weil 的标准曲线点数界；上述精确式可核于
  M. Perret, *Nombre maximum de points rationnels d'une courbe sur un corps fini*,
  JTNB 3 (1991), 261–274，§I.1，Theorem 2，印刷第262页：
  https://www.numdam.org/item/JTNB_1991__3_2_261_0.pdf 。
  本文只使用通常的双边 Weil 界，未使用任何更强的点数猜想。

全文由 global_route 给原 modular-unit/cusp 计算及严格下降，root 独核函数域注入、descent 的存在与唯一、完整 $\chi^2$ 常数和角色碰撞。§8 的实际可见商与点集双射由 root 提出、global_route 独核；root 实读 Carlucci 原索引/width、Bilu–Parent–Rebolledo (3.3) 及所引 Weil 界。无数学程序执行。


## 9. 后继补齐 $2,3$ 的原整模型

[R1067](R1067-original-cuspidal-labels-supported-only-at-p.md)
支付完整原曲线在所有 $\ell\ne p$ 的 smooth proper coarse 模型，
以及规范 Kummer 函数的全部水平、垂直 $p$ 倍 divisor。
因此本篇的 finite étale twists、可见角色、(1064.36) 点集双射及
(1064.37)–(1064.40) Weil 范围，在允许标签改为
$\operatorname{Hom}_G(W,F(\{p\},p))$ 后也适用于 $\ell=2,3$。
这补齐了本篇原先保留的两个好位接口；不声称其辅助点像已排除候选，
$p$ 处仍使用 R1065–1066 的真实模型。
