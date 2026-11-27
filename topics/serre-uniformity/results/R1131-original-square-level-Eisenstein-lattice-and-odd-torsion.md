# R1131：原平方层 Eisenstein 整格、奇圆分扭点与实际圆单位扩张

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126。

**状态：下述两个 Bernoulli 单位条件内的实际整格定理。** 本文把 Calegari 的同素数平方层定理接到原 $J_{\rm ns}^+(p)$ 的实际 cuspidal 偶直线。结论消去指定 Hecke 块的全部奇圆分 $p$ 次幂扭点，并确定该块的真实模 $p$ 扭点扩张域。没有使用“把整个非分裂表示取 Hecke socle 后仍单射”的论证，也没有假定所有奇扭点都来自 Shimura 子群。

## 1. 定理、两个正指标与原模块

固定 $p>37$，
$$
K=\mathbb Q(\zeta_p),\qquad F=K^+,\qquad
\Delta=\operatorname{Gal}(K/\mathbb Q),\qquad
m=(p-1)/2,\qquad h=\lfloor p/4\rfloor-1.
$$
$\omega$ 是模 $p$ 圆分角色，亦用其 Teichmüller 提升定义整角色幂等元。记
$$
J=J_0(p^2),\qquad J_{\rm ns}=\operatorname{Jac}(X_{\rm ns}^+(p)).
$$
对 $1\le j\le h$，置
$$
r=p-1-2j,\qquad k=2j+1=p-r,\qquad
b=4j+2=2k,\qquad b'=p-1-4j=p+1-2k.                 \tag{1131.1}
$$
这些指标满足
$$
3\le k<m,\quad r>m+1,\quad
4\le b,b'\le p-3,\quad b,b'\text{ 均为偶数}.
$$
特别，本文只应用 Calegari 印刷定理中两个**正** Bernoulli 指标：
$$
B_b,\ B_{b'}\in\mathbb Z_p^\times.                   \tag{1131.2}
$$
角色对
$\{\omega^k,\omega^{1-k}\}=\{\omega^{1-r},\omega^r\}$
相同；我们不需要解释高代表 $r$ 代入原文时可能出现的负 Bernoulli 指标。

令 $\mathbb T$ 为 $J$ 上 prime-to-$p$ Hecke 算子生成的整代数，
$\mathfrak m_j$ 为
$$
p,\quad T_\ell-\ell^r-\ell^{1-r}\pmod p
\qquad(\ell\ne p\text{ 为素数})                       \tag{1131.3}
$$
规定的极大理想。本文 $\mathbb T_{\mathfrak m_j}$ 指 $(\mathbb T\otimes\mathbb Z_p)$ 的对应完成局部因子。负指数在 (1131.3) 中只表示 $\mathbb F_p^\times$ 的逆；可用正整数 $\ell^{p-r}$ 代替第二项。它就是 Calegari 的 $(p,k)$-Eisenstein 极大理想。

**定理。** 在 (1131.2) 下：

1. $\mathcal O=\mathbb T_{\mathfrak m_j}$ 是剩余域为 $\mathbb F_p$ 的 DVR；原 $M=e_{\mathfrak m_j}T_pJ$ 是自由秩二的 $\mathcal O$ 格。
2. 原 $J[\mathfrak m_j]$ 是准确的非分裂扩张
   $$
   0\longrightarrow\mathbb F_p(\omega^r)
   \longrightarrow J[\mathfrak m_j]
   \longrightarrow\mathbb F_p(\omega^{1-r})
   \longrightarrow0.                                \tag{1131.4}
   $$
   它的偶子直线由原 cuspidal 群运输而来，而非任意选择一个同半单化的抽象表示。
3. 原 Fricke 正块、原 Cartan 块与这个平方层块在整 $p$ 上相同，且
   $$
   J(K)[p^\infty]_{\mathfrak m_j}^{-}
   =J_{\rm ns}(K)[p^\infty]_{\mathfrak m_j}^{-}=0.
                                                               \tag{1131.5}
   $$
4. 令 $\beta_b=e_{\omega^b}[\eta_a]$ 为 R1069 的同一原圆单位类，其中 $a$ 为固定奇整数、其剩余类生成 $\operatorname{Gal}(F/\mathbb Q)$，且
   $$
   \eta_a=\zeta_p^{(1-a)/2}
          \frac{1-\zeta_p^a}{1-\zeta_p}.
   $$
   不要求 $V_{\omega^b}$ 在原 cuspidal 模块中出现。若 $\widetilde\beta_b\in F^\times$ 表示此非零 Kummer 类，则
   $$
   K\bigl(J[\mathfrak m_j]\bigr)
    =K\bigl(\sqrt[p]{\widetilde\beta_b}\bigr).          \tag{1131.6}
   $$
   这确定原扩张的 radical 直线和域，不指定 (1131.4) 的某个 cocycle 所对应的非零标量。

[R1062](R1062-original-full-nonsplit-cuspidal-kummer-descent.md)
给出本文每个 $r$ 的实际直线
$$
C_r\simeq\mathbb F_p(\omega^r)
 \subset C_\Sigma[p]\subset J_{\rm ns}(F)[p].         \tag{1131.7}
$$
因此 (1131.7) 不是定理中的额外猜测。条件 (1131.2) 与 $B_r$ 是否为单位是不同的两个条件。

## 2. 原偶直线确实落在同一个 Hecke 极大理想

[整 $p$ Chen 与 Ohta 笔记](../notes/2026-11-27-original-prime-p-Chen-isogeny-and-odd-torsion-reduction.md)
§§1–3 已给 $\mathbb Q$ 上 prime-to-$p$ 同源
$$
J_2^+\longrightarrow J_{\rm ns}\times J_0(p),
\qquad
J_2^+=\operatorname{Jac}(X_0(p^2)/w_{p^2}),           \tag{1131.8}
$$
并证明它在真实 $p$ 次幂扭点上是同构，保全部 away-$p$ Hecke。
商曲线拉回 $J_2^+[p^\infty]\to J[p^\infty]$ 的核被 $2$ 杀，故在此亦单射。将 (1131.7) 经 (1131.8) 的逆及这个拉回运输，得到
$$
0\ne C_r\subset J[p]^+.                              \tag{1131.9}
$$

对 $\ell\ne p$，$J$ 在 $\ell$ 良约化，$p$ 挠点的 specialization 单射。令 $\operatorname{Frob}_\ell$ 采用点坐标升至 $\ell$ 次幂的算术约定；其在 $\mu_p$ 上为乘 $\ell$。原 Eichler–Shimura 关系在点上为
$$
T_\ell=\operatorname{Frob}_\ell+
       \ell\operatorname{Frob}_\ell^{-1}.
$$
在 (1131.9) 上两个项分别为 $\ell^r$ 和 $\ell^{1-r}$，所以
$$
T_\ell|_{C_r}=\ell^r+\ell^{1-r}\pmod p.               \tag{1131.10}
$$
因此该直线属于准确的 $\mathfrak m_j$ 部分。这里没有从一个抽象 residual 角色对猜原 Hecke 层，也没有改原 cusp 的 Galois 方向。

若采用含 $U_p$ 的完整 Hecke 代数，则下一节排除 old 后，本块上 $U_p=0$。所以其局部代数与本文由 traces 生成的 away-$p$ 代数相同，不需另给 (1131.8) 一个未经证明的 $U_p$ 相容性。

## 3. Calegari 的同素数定理与实际秩二格

### 3.1 所消费的原定理比“DVR”更精确

在 [Ca, Definition 2.5、Theorem 2.6] 取 (1131.1) 的低代表 $k$。所有排除值
$0,1,(p-1)/2,(p+1)/2$ 都已避开，两个 Bernoulli 前提恰是 (1131.2)。
得到自然同构
$$
R\simeq\mathbb T_{\mathfrak m_j}=\mathcal O,
\qquad \mathcal O\text{ 为 DVR}.                     \tag{1131.11}
$$
本篇还使用原证明 §4.2 的 Lemmas 4.12–4.13 及紧随其后的结论：通用表示的 **trace reducibility ideal 正好是极大理想**
$$
I_{\rm red}=\mathfrak m_{\mathcal O}.                 \tag{1131.12}
$$
这是排除实际 residual split 的关键；单独“$\mathcal O$ 是 DVR”不够。

原同构把通用 $\operatorname{tr}\rho(\operatorname{Frob}_\ell)$ 送到实际 $T_\ell$。本文不需要把 Gross–Lubin 的某个整二维表示嵌入额外搬到 $J[\mathfrak m_j]$；只消费 Calegari 已发表的 (1131.11)–(1131.12)。

### 3.2 此极大理想没有 old 部分

level $p$ 的 $J_0(p)$ 在 $p$ 为纯 toric 半稳定约化。其 Tate 表示经未分歧扩张具有 toric uniformization 的两步过滤；在惯性上两类 Jordan–Hölder 角色为 $\chi_p$ 与 $1$。约化后只能为 $\omega$ 与 $1$。这也可从 level-$p$ 新形式在 $p$ 的 Steinberg 型和对应普通过滤直接得到。

若一个 level-$p$ old 特征落在 $\mathfrak m_j$，由其所有良素 Hecke traces、行列式及 Chebotarev，其模 $p$ 半单化必须为
$\omega^r\oplus\omega^{1-r}$。
限制到惯性便与前段矛盾：$r$ 及 $1-r$ 都不等于 $0,1\bmod p-1$。level $1$ 的权二 cusp 空间为零。因此本块全部是 exact level $p^2$ new，原 $J_0(p)$ 的 $\mathfrak m_j$ 部分为零。

### 3.3 从特征零到真实整格

在特征零，exact-level 新形式在微分中重数为一；Betti 一阶同调、或等价的 Tate 表示，在其系数域上重数为二。可用 Hodge 分解逐个新系统看见这两个维度。于是
$$
M\otimes_{\mathcal O}\operatorname{Frac}(\mathcal O)
 \simeq \operatorname{Frac}(\mathcal O)^2.             \tag{1131.13}
$$
[Em, §4，Theorem A 证明末段] 也给出了这个特征零 rank-two 论证；这里只用其有理结论，不借一个尚未证明的 residual multiplicity-one 定理。

$M=e_{\mathfrak m_j}T_pJ$ 是实际 $\mathbb Z_p$ 自由模的直因子。若 $a\in\mathcal O$ 非零，则某个 $p^n$ 被 $a$ 整除，因而 $aM$ 的核被 $p^n$ 杀，只能为零。故 $M$ 为有限无挠 $\mathcal O$ 模。由 (1131.11) 与 (1131.13)，
$$
M\simeq\mathcal O^2.                                  \tag{1131.14}
$$
没有先假定 $J[\mathfrak m_j]$ 二维；它将从 (1131.14) 推出。

## 4. 同一个 trace 迫实际 residual 非分裂

令 $\varpi$ 为 $\mathcal O$ 的均匀元，$\tau$ 为复共轭。
因为 $2$ 是单位且该权二表示为 odd，$M$ 的两个整幂等元
$(1\pm\tau)/2$ 各给秩一自由直因子。取基使
$$
\rho_M(\tau)=
 \begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
\rho_M(g)=
 \begin{pmatrix}a_g&b_g\\c_g&d_g\end{pmatrix}.
$$
写 $t(g)=\operatorname{tr}\rho_M(g)$。有完整整恒等式
$$
a_g=\frac{t(g)+t(\tau g)}2,\qquad
d_g=\frac{t(g)-t(\tau g)}2,\qquad
b_gc_h=a_{gh}-a_ga_h.                                \tag{1131.15}
$$
所以若 $B=(b_g:g\in G_{\mathbb Q})$、$C=(c_g:g\in G_{\mathbb Q})$，
则理想 $BC$ **只由同一 trace 决定**。

实际 $t$ 与 (1131.11) 的通用 trace 在全部 $\operatorname{Frob}_\ell$、
$\ell\ne p$ 上都等于 $T_\ell$，故由 Chebotarev 与连续性在全
$G_{\mathbb Q}$ 相等。将 (1131.15) 同样用于通用表示，并用
[Ca, §3 的 $I_{\rm red}=BC$ 及 §4.2 的 (1131.12)]，得到
$$
BC=(\varpi).                                         \tag{1131.16}
$$
这一步显式支付了 trace 理想与格选择无关；没有仅从“同半单化”
推出同扩张。

由 (1131.14)，
$$
J[\mathfrak m_j]\simeq\varpi^{-1}M/M\simeq M/\varpi M
$$
为二维。若它 split，则在上述复共轭的两个不同特征基中所有
$b_g,c_g$ 都被 $\varpi$ 整除，强迫 $BC\subset(\varpi^2)$，
与 (1131.16) 矛盾。因此它是非分裂的一个方向。

现在只用 (1131.9) 的**简单偶直线**来锁方向：它在同一个
$\mathfrak m_j$-primary 部分；取其最高非零 $\varpi$ 倍，就在
$J[\mathfrak m_j]$ 中得到非零 $\omega^r$ 直线。
乘 $\varpi$ 与 Galois 作用交换，故非零像仍为同一一维角色。
若用 (1131.10) 的全部 away-$p$ 生成元，则这条线本身已经被
$\mathfrak m_j$ 杀，亦可直接使用。
非分裂、异角色的二维表示只有一个简单子模，遂准确得到 (1131.4)。

这里不能把“取简单直线的非零像”替换成“取整个二维非分裂表示
的 socle 仍单射”。后者可能杀掉其中一个组成因子；本证明不作这种替换。

## 5. 原 Fricke 正块与全部奇圆分扭点

在本 exact-level new 的特征零块上，$w_{p^2}$ 按新形式的 Fricke
特征为标量 $\pm1$。$\mathcal O$ 是域整环的整序，故该块不能同时
含两个 Fricke 符号。式 (1131.9) 的非零直线在正部分，而且 $p\ne2$，
迫这个整个块的符号为 $+1$。

因此 (1131.8) 在本块给
$$
e_{\mathfrak m_j}T_pJ
 \simeq e_{\mathfrak m_j}T_pJ_2^+
 \simeq e_{\mathfrak m_j}T_pJ_{\rm ns},               \tag{1131.17}
$$
最后用了 §3.2 的 old 部分为零。此处是已付 prime-to-$p$ 同源的
真正整同构，不是只比较维数。

在 (1131.4) 上限制到 $G_K$，两个对角角色都为一。
若 $G_K$ 作用平凡，则 (1131.4) 通过阶 $p-1$ 的 $\Delta$，
Maschke 定理会迫它 split，矛盾。
故 $G_K$ 的像为非平凡阶 $p$ unipotent 群，
$$
J[\mathfrak m_j]^{G_K}=\mathbb F_p(\omega^r).          \tag{1131.18}
$$
尤其其奇部为零。

若 $P\ne0$ 属于 $J(K)[p^\infty]_{\mathfrak m_j}^{-}$，
取最高非零 $\varpi$ 倍得到非零
$P'\in J[\mathfrak m_j](K)^-$，违背 (1131.18)。
这证明 (1131.5)，并经 (1131.17) 保持原 Cartan 的同一结论。
该论证不只排除阶 $p$ 点。

## 6. 真实扩张域是原圆单位的指定角色

令 $L=K(J[\mathfrak m_j])$。由 (1131.18)，
$\operatorname{Gal}(L/K)\simeq\mathbb F_p$。
在 (1131.4) 的 upper-right 坐标上，$\Delta$ 的共轭作用为
$\omega^{r-(1-r)}=\omega^{2r-1}$。
于是 $\Delta$-等变 Kummer pairing 给准确的 radical 角色
$$
\omega\bigl(\omega^{2r-1}\bigr)^{-1}
  =\omega^{2-2r}
  =\omega^{4j+2}=\omega^b.                            \tag{1131.19}
$$

$J$ 在 $p$ 外良约化，故 $L/K$ 在 $p$ 外不分歧。
它的 radical 在 $K(\{p\},p)$ 中。
因 $b$ 偶，restriction 与 norm、合成为 $2$，给出
$$
K(\{p\},p)_{\omega^b}
 \simeq F(\{p\},p)_{\omega^b}.                         \tag{1131.20}
$$
这也可直接由 Kummer 的 restriction–corestriction 和
$|\operatorname{Gal}(K/F)|=2$ 核对；沒有擅自忽略 $S$-class-group 项。

条件 $B_b\in\mathbb Z_p^\times$ 允许直接使用
[R1069](R1069-all-prime-good-cuspidal-characters-and-unique-global-labels.md)
§§2–3：该角色的 real class group 为零，
$F(\{p\},p)_{\omega^b}$ 是一维，且同一原
$\beta_b=e_{\omega^b}[\eta_a]$ 的局部 leading 非零，故生成此空间。
这个单位与类群定理对任意非平凡偶角色成立，不要求它首先是 $V$ 的角色。
(1131.19) 的非零 radical 因而正是 $\mathbb F_p\beta_b$，证明 (1131.6)。

指定扩张的非零 cocycle 标量还取决于 (1131.4) 的基。
本文确定的是这条原 radical 直线及其域，不将标量置为 $1$，
也不把 $\beta_b$ 改成 $\beta_r$。

若需要局部分歧尺度，
[R1112](R1112-original-simultaneous-cuspidal-Frobenius-selection.md)
§9 的 Kummer filtration 证明可直接应用：
$\beta_b$ 在 $K_p$ 的精确单位深度为 $b<p$，所以 (1131.6) 在 $p$ 全分歧，
upper ramification break 为 $p-b$，Artin conductor 指数为 $p-b+1$。
这一读法保留原圆单位的实际局部归一化。

## 7. 对归一化 integral K2 残余的准确消去

沿用
[原 $K_2$ 笔记](../notes/2026-11-27-original-cuspidal-K2-torsion-and-odd-Jacobian-obstruction.md)
的 integral $p$-torsion 范围。Suslin 的正合列和全 cusp 平均给
$\Delta$-等变识别
$$
\mathcal R:=
 K_{2,\mathrm{nr}}(K(X_{\rm ns}^+(p)))[p]/K_2(K)[p]
 \simeq \mu_p\otimes_{\mathbb F_p}J_{\rm ns}(K)[p].     \tag{1131.21}
$$
因此 $\mathcal R_{\omega^\alpha}$ 对应
$J_{\rm ns}(K)[p]_{\omega^{\alpha-1}}$。

取 $\alpha=2-r\equiv2j+2\bmod p-1$。
任何此处的 Jacobian 角色直线，按同一个 Eichler–Shimura 论证，
都落在 (1131.3) 的 $\mathfrak m_j$，而它的角色为 $\omega^{1-r}$，是奇角色。
故 (1131.5) 给
$$
\boxed{\qquad
\mathcal R_{\omega^{\,2j+2}}=0
\quad\text{若 }p\nmid B_{4j+2}B_{p-1-4j}.
\qquad}                                               \tag{1131.22}
$$
亦即，全 cusp 平均为零的该角色 integral $K_2[p]$ 类本身为零。
这不是 $K_2/p$ 的 Brauer 消失命题，也不由一个抽象 cup 的零
直接生成中央覆盖。

本篇没有处理 (1131.21) 的全部偶角色，尤其没有据 (1131.22) 宣称其平凡角色
$\alpha=0$ 已消失。四阶实际 Siegel cochain／cover 的其余接口仍须分别完成。
后续 [R1132](R1132-original-full-Cartan-odd-cusp-and-constant-K2-torsion.md)
另用完整 Cartan 的奇尖点线，在 $p\nmid B_{p-3}$ 下消去规范残余的平凡角色；这不由本文 (1131.22) 推出。

## 8. 无条件的实际应用

### 8.1 p 等于 1 模 4 时至少五个真实块

设 $p=4a+1$，则 $h=a-1$。
当 $1\le j\le h$ 时，两组指标
$$
4j+2\in\{6,10,\ldots,p-3\},\qquad
p-1-4j\in\{4,8,\ldots,p-5\}
$$
互不相交，且它们合起来正是 $4,6,\ldots,p-3$。
所以每个 irregular Bernoulli 指标至多使一个 $j$ 失去 (1131.2)。
若 $i(p)$ 为普通 irregular index，至少有
$$
h-i(p)\ge5                                             \tag{1131.23}
$$
个实际 forced 块满足本文结论；最后一步正是
[R1128](R1128-all-prime-linear-good-cuspidal-rank.md)
(1128.16) 的已证不等式。
两个不同 $j$ 给不同无序 Galois 角色对，因为它们各自的偶成员
$\omega^r$ 不同，故 (1131.23) 没有重复计数同一个 Hecke 块。
相应 (1131.22) 也给至少五个不同的原 $K_2$ 角色分量消失。

沿用 R1069 的同一显式 $\mathcal H_p$，更精确地有
$$
\#\{j:\text{(1131.2)成立}\}\ge
h-\lfloor\log_p\mathcal H_p\rfloor
=\frac{\log24}{4}\frac p{\log p}-O(1).                 \tag{1131.24}
$$
这里只是这个已证明下界的渐近，不声称消失角色数等于右边。

### 8.2 p 等于 3 模 8 时一个指定块无条件成立

设 $p\equiv3\bmod8$。取
$$
j=(p-3)/8,\qquad r=(3p-1)/4,\qquad
k=(p+1)/4,\qquad b=b'=(p+1)/2.                        \tag{1131.25}
$$
$r$ 为偶数，$j$ 在 R1062 forced 范围内。
令 $\eta=\omega^{(p-1)/2}$ 为对应
$\mathbb Q(\sqrt{-p})$ 的奇二次角色。广义 Kummer 同余给
$$
\frac{B_{(p+1)/2}}{(p+1)/2}
 \equiv B_{1,\eta}
 =-h(\mathbb Q(\sqrt{-p}))\pmod p.                    \tag{1131.26}
$$
类数公式的最后一个等式因 $p>3$ 时根单位只有 $\{\pm1\}$ 而没有额外因子。

为明确支付非零，令 $N=\lfloor\sqrt{p/3}\rfloor$。
判别式 $-p$ 的每个约化正定 primitive binary quadratic form
$[a,b,c]$ 满足 $1\le a\le N$、$|b|\le a$；
固定 $a,b$ 后 $c=(b^2+p)/(4a)$ 唯一。
因此
$$
0<h(\mathbb Q(\sqrt{-p}))
 \le\sum_{a=1}^N(2a+1)=N(N+2)
 \le p/3+2\sqrt{p/3}<p.                              \tag{1131.27}
$$
故 (1131.26) 为单位，(1131.2) 在 (1131.25) 上无条件成立。
从而该原块的奇圆分 $p^\infty$ 为零，且
$$
\mathcal R_{\omega^{(p+5)/4}}=0.                      \tag{1131.28}
$$
其真实残余扭点域为
$K(\sqrt[p]{\widetilde\beta_{(p+1)/2}})$。
本段不使用有限 prime scan，也不使用 regular 或 Vandiver 假设。

## 9. 原始来源、整规范与尚未完成的部分

- [Ca] Frank Calegari，*Eisenstein deformation rings*，Compositio Math. 142 (2006), 63–83，DOI [10.1112/S0010437X05001661](https://doi.org/10.1112/S0010437X05001661)。实读 [作者 PDF](https://www.math.uchicago.edu/~fcale/papers/Eisenstein.pdf)：印刷第 64–65 页的 Bernoulli 约定、Definition 2.5、Theorem 2.6；第 66–67 页的整 trace/$BC$ 论证；第 72–73 页的 Lemmas 4.12–4.13 及 reducibility ideal 为极大理想的结论。本文只用 (1131.1) 的低代表，不扩张其 Bernoulli 范围。
- [Em] Matthew Emerton，*Optimal quotients of modular Jacobians*，[作者 PDF](https://www.math.uchicago.edu/~emerton/pdffiles/optimal.pdf)，§4，Lemma 4.1 与 Theorem A 证明，PDF 第 16–18 页。所消费的是特征零 Hecke/Hodge/Tate 秩二及 new 系统的重数；整自由性在本文由实际 DVR 和无挠性另证。
- Brian Conrad、William Stein，*Component groups of purely toric quotients*，[作者版本 §7](https://www.wstein.org/papers/compgrp/compgrp/node11.html) 与 [Appendix §8](https://www.wstein.org/papers/compgrp/compgrp/node20.html)：prime-level 纯 toric 来源及包括系数素数在内的 toric $p$-divisible／对偶过滤。本文 no-old 只消费其惯性两个组成角色。
- Daniel Kriz、Chao Li，*Goldfeld's conjecture and congruences between Heegner points*，Forum Math. Sigma 7 (2019), e15，DOI [10.1017/fms.2019.9](https://doi.org/10.1017/fms.2019.9)，[正式 PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/05E581EF286E02A8B4D681096E24E709/S2050509419000094a.pdf/goldfelds-conjecture-and-congruences-between-heegner-points.pdf)，§8，式 (35)，印刷第 52 页：奇二次角色的准确 $B_{1,\eta}$ 类数因子。
- R1062、R1069、R1128、整 $p$ Chen 笔记及 integral $K_2$ 笔记，按正文各处的原范围消费。没有运输未经证明的指定 polarization 或 cusp generator 尺度。

本文对指定块同时付清了实际 Hecke 极大理想、格的秩二、同一 trace 的整约化理想、偶子线方向及真实 Kummer radical。它不把单个或多个已消失角色升级成全 $J_{\rm ns}(K)[p]^{-}=0$，不宣称原四阶 cover 已构成，也不改一般 $p$ 的同点排除仍开放的状态。全文没有数学程序执行。
