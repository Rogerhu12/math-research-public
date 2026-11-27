# R1132：完整 Cartan 的奇尖点线、原正商整块消失与常数 K2 扭点

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明的条件结论。** 取 $p>37$。若 $p\nmid B_{p-3}$，则原
$J_{\rm ns}^+(p)(\mathbb Q(\zeta_p))[p]_{\omega^{-1}}=0$；
因此按原全尖点平均规范的、平凡 Galois 角色的未分歧整 $K_2[p]$
残余为零。证明使用完整 Cartan 曲线的真实奇尖点线，先迫整个相关
Hecke 块在正规化子 involution 的负部分，再排除它在原正商中的存在。

本篇亦给同一论证的准确低偶指标推广。它不要求 $p$ regular，
但保留下文逐块的两个 Bernoulli 单位条件。没有将整 $K_2[p]$ 换成
$K_2/p$，也没有把本定理当成原杯积或四阶中央覆盖已构成。

## 1. 原曲线、角色与结论

令
$
K=\mathbb Q(\zeta_p),\qquad
\Delta=\operatorname{Gal}(K/\mathbb Q),\qquad
m=(p-1)/2,
$
$
Y=X_{\rm ns}(p),\qquad
X=X_{\rm ns}^+(p)=Y/\langle w\rangle,\qquad
J_Y=\operatorname{Jac}(Y),\quad J_X=\operatorname{Jac}(X).
\tag{1132.1}
$
$Y$ 是完整非分裂 Cartan 曲线，$X$ 是本课题原正规化子曲线。
$w$ 为 $\mathbb Q$ 上的正规化子 involution。
$\omega$ 同时表示模 $p$ 圆分角色及其 Teichmüller 提升。
符号 $+$、$-$ 在涉及 $w$ 时表示 $w$ 的符号；
下标 $\omega^a$ 始终表示实际 $\Delta$ 角色，不把两种作用混同。

设 $r$ 是偶数，满足
$
2\le r<m,\qquad
p\nmid B_{2r}B_{p+1-2r}.                              \tag{1132.2}
$
在 $J_0(p^2)$ 的 away-$p$ Hecke 代数上，令
$
\mathfrak m_r=
\bigl(p,\ T_\ell-\ell^r-\ell^{1-r}:\ell\ne p\bigr).
\tag{1132.3}
$
第二项的负幂只在模 $p$ 中使用。
利用下文的整 Chen 比较，在 $J_Y$ 及 $J_X$ 的 $p$-divisible
群上使用同一完成 Hecke 代数及其块幂等元 $e_r$。

**定理。** 条件 (1132.2) 下，
$
w=-1\quad\hbox{在 }e_rT_pJ_Y\hbox{ 上},\qquad
e_rT_pJ_X=0,\qquad e_rJ_X[p^\infty]=0.                \tag{1132.4}
$
最后一个等式是几何 $p$-divisible 群的整块消失。
特别，
$
J_X(K)[p]_{\omega^{1-r}}=0.                          \tag{1132.5}
$
当 $r=2$ 时，$B_4=-1/30$ 为单位，(1132.2) 恰只剩
$p\nmid B_{p-3}$。此时 (1132.5) 给所需的 $\omega^{-1}$ 部分消失。

## 2. 从 full level 到完整 Cartan 的实际尖点群

### 2.1 几何商与 Galois 作用分别固定

令 $Z=X(p)_K$ 为固定 Weil pairing 的几何连通 full-level 分支。
写
$
\mathbb F_{p^2}=\mathbb F_p(\sqrt d),\qquad
T(a+b\sqrt d)=a,\qquad N(a+b\sqrt d)=a^2-db^2,
$
其中 $d$ 是非平方。取
$
C=\mathbb F_{p^2}^{\times}/\{\pm1\},\qquad
H=\ker(N)/\{\pm1\},\qquad |H|=(p+1)/2.
\tag{1132.6}
$
$C$ 作用于完整模函数域；行列式等于 $N$，所以一般为
semilinear 作用。只有 $H$ 在固定 $K$ 分支上作几何作用。
实际商为 $Y_K=Z/H$，且 $C/H=\mathbb F_p^\times$。

full-level 的尖点由 $C$ 标记。商后 $Y$ 的 $p-1$ 个尖点
由范数 $h\in\mathbb F_p^\times$ 标记，全部在 $K$ 上有理。
行列式为 $a$ 的 Cartan 场自同构固定 $\mathbb Q(Y)$，
在常数上为 $\zeta_p\mapsto\zeta_p^a$，故在 $K(Y)$ 上就是实际
$\sigma_a$。取 $c_h=\sigma_h(c_1)$，则尖点格的左作用为
$\sigma_a c_h=c_{ah}$。

这里沿用 [R1062 §1](R1062-original-full-nonsplit-cuspidal-kummer-descent.md)
已经核定的函数/除子作用方向，但此处尚未再商掉 $h\mapsto-h$。
下面 Stickelberger 元中的逆已经负责角色的逆，不能把 Galois
作用再反转一次。[C, Proposition 4.5、Theorem 4.6] 在 full level
给出所需实际格及此方向。

### 2.2 尖点类群的整 $p$ transfer

令 $C_Z,C_Y$ 分别为全部尖点生成的几何次数零除子类群。
所有这些尖点在 $K$ 上有理；若尖点除子几何上 principal，
Riemann–Roch 的基变换给出 $K$ 上的函数，所以此群也是相应
$K$-rational 尖点除子模实际 principal 格。

[C, Theorem 4.6] 给
$
R=\mathbb Z[C],\quad
\theta=\frac p2\sum_{z\in C}
 B_2\!\left(\left\langle T(z)/p\right\rangle\right)[z]^{-1},
\quad
C_Z\simeq R_0/(R\cap R\theta).                        \tag{1132.7}
$
$B_2(t)=t^2-t+1/6$，$R_0$ 为 augmentation-zero 理想。
此处保留来源中的交 $R\cap R\theta$，不把含分母的
$\theta$ 任意当成整矩阵。

对商 $\pi:Z\to Y_K$，拉回与推前保尖点类，而且
$
\pi_*\pi^*=[|H|],\qquad
\pi^*\pi_*=\sum_{h\in H}h.                            \tag{1132.8}
$
由于 $p\nmid|H|$，由 (1132.8) 得到准确同构
$
C_Y\otimes\mathbb Z_p
 \simeq (C_Z\otimes\mathbb Z_p)^H.                    \tag{1132.9}
$
不需要假设所有非尖点处不分歧。具体地，一个 $H$-不变类等于
$|H|^{-1}\pi^*\pi_*$ 作用于自身；拉回的核被 $|H|$ 杀。

对 $\mathbb F_p^\times$ 的任意非平凡字符 $\chi$，
$\chi\circ N$ 在 $-1\in\mathbb F_{p^2}^\times$ 上平凡，
所以 **奇** $\chi$ 在 (1132.7) 中同样合法。取该整角色幂等元，
(1132.7)–(1132.9) 给
$
(C_Y\otimes\mathbb Z_p)_\chi
 \simeq\mathbb Z_p/
       \bigl(\mathbb Z_p\cap S_{\chi^{-1}}\mathbb Z_p\bigr),
$
$
S_\psi=\frac p4\sum_{z\in\mathbb F_{p^2}^\times}
 B_2\!\left(\left\langle T(z)/p\right\rangle\right)\psi(Nz).
\tag{1132.10}
$
当下文证明 $S_\psi\in p\mathbb Z_p$ 后，交即为
$S_\psi\mathbb Z_p$。本式没有从原正商臆造一条奇尖点线：
这条线属于尚未商去 $w$ 的真实 $Y$。

## 3. 低奇角色给一条真实的阶 $p$ 线

取满足 (1132.2) 的 $r$，令
$
s=r-1,\qquad\psi=\omega^s,\qquad
\chi=\psi^{-1}=\omega^{1-r},\qquad \eta=\omega^m .
$
于是 $s$ 为奇数、$1\le s<m$，而
$\psi,\psi^2,\psi\eta$ 均非平凡。
R1062 的范数纤维计算不要求 $\psi$ 偶，逐项仍给
$
S_\psi=-\frac14 J(\psi,\eta)B_{2,\psi^2},\qquad
J(\psi,\eta)=\sum_{z\in\mathbb F_p}\psi(z)\eta(1-z).
\tag{1132.11}
$
其中 $B_{2,\psi^2}=p\sum_{a=1}^{p-1}\psi(a)^2B_2(a/p)$。
说明如下：固定非零 $a=T(z)$，范数纤维数为
$1-\eta(a^2-n)$，故其 $\psi$-和为
$-\psi(a)^2J(\psi,\eta)$；$a=0$ 的和因 $\psi^2\ne1$ 为零。

模 $p$ 有
$
J(\psi,\eta)\equiv\sum_z z^s(1-z)^m=0,
\quad
J(\psi^{-1},\eta)
 \equiv-(-1)^s\binom ms=\binom ms\ne0.                \tag{1132.12}
$
第一式中全部幂严格小于 $p-1$；第二式仅 $p-1$ 次幂有贡献。
Gauss 和恒等式准确给
$J(\psi,\eta)J(\psi^{-1},\eta)=p$，故
$
v_p J(\psi,\eta)=1.                                  \tag{1132.13}
$

广义 Bernoulli 数的通常 Kummer 同余为
$
\frac{B_{2,\omega^{2r-2}}}{2}
 \equiv \frac{B_{2r}}{2r}\pmod p.                     \tag{1132.14}
$
所有指标 $4\le2r\le p-3$ 均为非异常正指标，分母为单位；
也可先由
$p^{-1}\sum a^2\omega(a)^{2r-2}-\sum a\omega(a)^{2r-2}$
直接核其整性。由 (1132.2)，(1132.14) 为单位。
因此 (1132.11) 的 valuation 恰为一，(1132.10) 给
$
(C_Y\otimes\mathbb Z_p)_{\omega^{1-r}}\simeq\mathbb Z/p,
\qquad
L_r:=C_Y[p]_{\omega^{1-r}}
 \simeq\mathbb F_p(\omega^{1-r})\subset J_Y(K)[p].
\tag{1132.15}
$
这是一条实际非零子线，且该尖点角色的整 $p$-primary 阶恰为 $p$。

在主应用 $r=2$ 中，
$J(\omega^{-1},\eta)\equiv m\ne0$，且
$
B_{2,\omega^2}\equiv B_4/2=-1/60\pmod p.
\tag{1132.16}
$
所以这条 $\omega^{-1}$ 尖点线本身对全部 $p>37$ 都存在；
$p\nmid B_{p-3}$ 只在后面的同素数 Hecke 环步骤使用。

## 4. 这条奇线在真实正规化子负部分

取 $\alpha\in\mathbb F_{p^2}^\times$ 使 $N(\alpha)=-1$。
线性 Frobenius $\iota:z\mapsto z^p$ 的行列式为 $-1$；
所以 $g=\alpha\iota$ 有行列式一，代表 $Y_K$ 上的正规化子 involution。
它满足 $g^2=-I$，而 $-I$ 在模曲线上作用平凡，故确为 involution。
不同 $\alpha$ 的选择仅相差 $H$，不改变 $Y_K$ 上的 $w$。

在尖点范数标记上，
$
N(gz)=N(\alpha)N(z^p)=-N(z),
\qquad w(c_h)=c_{-h}.                                \tag{1132.17}
$
此 involution 是原 $\mathbb Q$ 上 $Y\to X$ 的 deck involution。
于是 $w$ 在尖点的 $\chi$-部分按 $\chi(-1)$ 作用。
(1132.15) 的 $\chi=\omega^{1-r}$ 为奇，故
$
w|_{L_r}=-1.                                        \tag{1132.18}
$
这里没有把复共轭在所有 $J_Y$ 上的作用等同于 $w$；
只在已明确的尖点格上用 (1132.17) 算出了符号。

## 5. 完整 Cartan 的 Chen 比较也在整 $p$ 上成立

[dSE, Theorems 3–4] 的**第一条**关系要求辅助素数
$\ell\nmid p^2-1$。取 $\ell=p$ 合法，得到
$
\varphi:J_0(p^2)\longrightarrow J_Y\times J_0(p)^2,
\qquad p\nmid\deg\varphi,                            \tag{1132.19}
$
且 $\varphi$ 在 $\mathbb Q$ 上定义。

这与
[整 Chen 笔记](../notes/2026-11-27-original-prime-p-Chen-isogeny-and-odd-torsion-reduction.md)
的正规化子第二条关系不同。此处使用有序 split 商
$X(p)/T_s=X_0(p^2)$，并保留两个 level-$p$ 因子。
dSE 的原证明检查实际商 Jacobian 拉回核：
对 $T_s,B$ 为阶整除 $p-1$ 的群，对 $T_{\rm ns}$
为阶整除 $p+1$ 的群，均无 $p$。
因此 (1132.19) 不是仅有理同源，也不遗漏含 $p$ 的拉回核。

原置换模同构对带 $G=\mathrm{GL}_2(\mathbb F_p)$ 作用的对象函子性成立。
full-level 的 away-$p$ Hecke 与 $G$ 作用交换，
故在 $\mathbb Z_{(p)}$ 范畴内可取 Hecke 等变的同构，
再用 prime-to-$p$ 整数清分母。
因此 (1132.19) 保全部 $T_\ell$、$\ell\ne p$，并给
$
T_pJ_0(p^2)\simeq T_pJ_Y\oplus T_pJ_0(p)^2
\tag{1132.20}
$
以及全部真实 $p$-divisible 群的 Hecke/Galois 等变同构。
本文不要求 (1132.19) 事先保 $w$ 或 Fricke；
$w$ 的符号在原 $Y$ 上独立计算。

## 6. 同一个唯一 new 块整个属于 $w=-1$

### 6.1 实际线锁定 Hecke 极大理想

对 $\ell\ne p$，$J_Y$ 良约化，$p$-torsion specialization 单射。
算术 Frobenius 的 Eichler–Shimura 关系在 (1132.15) 上给
$
T_\ell|_{L_r}
 =\ell^{1-r}+\ell\ell^{r-1}
 =\ell^{1-r}+\ell^r\pmod p.
\tag{1132.21}
$
故 $L_r$ 确被 (1132.3) 的 $\mathfrak m_r$ 杀。
这里用的是原 $K$-rational 角色线，未另设同半单化的抽象表示。

### 6.2 真实 rank-two 整格及标量 involution

在 [Ca, Definition 2.5、Theorem 2.6] 取低代表 $k=r$。
$2\le r<m$ 避开原定理全部例外，
两 Bernoulli 前提恰为 (1132.2)。故
$
\mathcal O=\widehat{\mathbb T}_{\mathfrak m_r}
 \text{ 是 DVR，剩余域 }\mathbb F_p.                 \tag{1132.22}
$
本节只需该结论；不同于 R1131，尚无需调用 trace reducibility ideal。

该块没有 level-$p$ old 成分：
$J_0(p)$ 在 $p$ 纯 toric 半稳定，其 Tate 表示的惯性半单角色
只能为 $\chi_p$ 与 $1$；模 $p$ 后为 $\omega,1$。
(1132.21) 的全局半单角色为
$\omega^r,\omega^{1-r}$，两者均不是 $1,\omega$。
由 Chebotarev 与上述惯性过滤排除 old。
这正是 [R1131 §§3.2–3.3](R1131-original-square-level-Eisenstein-lattice-and-odd-torsion.md)
的同一完整论证，对当前 $r$ 范围仍逐项成立。

exact-level new 的特征零 multiplicity one 给
$
e_rV_pJ_0(p^2)\simeq\operatorname{Frac}(\mathcal O)^2.
$
实际 $T_p$ 无挠，DVR 上即自由。由 (1132.20) 的两个 old 块为零，
$
M=e_rT_pJ_Y\simeq\mathcal O^2.                       \tag{1132.23}
$
这是原整格，不是 residual multiplicity-one 的假定。

$w$ 在 $\mathbb Q$ 定义，且与全部 away-$p$ Hecke 交换。
此唯一 new 块的二维特征零 Galois 表示为绝对不可约；
所以 Schur 引理使 $w$ 为标量。
亦可不用这个表示表述而直接在特征零看：
每个 new Hecke 系统的 holomorphic eigenspace 一维；
$w^2=1$ 在它上给 $\pm1$，在复共轭的 antiholomorphic
直线上是同一个实符号。由于 $w$ 在 $\mathbb Q$ 定义，
所有系数嵌入的符号也相同。因此它在完整二维 Tate 块上为同一标量，
不是仅从“Hecke 交换”就跳到二维空间上的标量结论。

于是 $w=\pm1$ 在 $M\otimes\operatorname{Frac}(\mathcal O)$ 上，
亦在无挠格 $M$ 上。
非零 $L_r$ 被 $\mathfrak m_r$ 杀且 (1132.18) 的符号为 $-1$，
而 $2$ 为单位，迫
$
w=-1\quad\text{在整个 }M\text{ 及对应 }p\text{-divisible 块上}.
\tag{1132.24}
$

### 6.3 原正商整块消失

令 $q:Y\to X$。准确有
$
q_*q^*=[2],\qquad wq^*=q^* .
\tag{1132.25}
$
因此 $q^*:J_X[p^\infty]\to J_Y[p^\infty]$ 单射，
且像在 $w=+1$ 部分；它也与 away-$p$ Hecke 交换。
(1132.24) 使此像在 $e_r$ 块只能为零。
这证明 (1132.4)。

任一 $J_X(K)[p]$ 的 $\omega^{1-r}$ 子线，
仍由 (1132.21) 的 Eichler–Shimura 关系被 $\mathfrak m_r$ 杀；
它会落入已为零的整块，故 (1132.5) 成立。
不需要把原 $X$ 的奇扭点先认作尖点或 Shimura 子群。

## 7. 原常数角色的规范整 K2[p] 残余

令 $L=K(X)$，$\Sigma$ 为原 $X$ 的全部 $m=(p-1)/2$ 个尖点。
沿用
[原整 K2 笔记 §§1–4](../notes/2026-11-27-original-cuspidal-K2-torsion-and-odd-Jacobian-obstruction.md)
已经证明的 $\Delta$-等变正合列与全尖点 specialization 平均：
$
0\longrightarrow K_2(K)[p]\longrightarrow
K_{2,\mathrm{nr}}(L)[p]\longrightarrow
\mu_p\otimes_{\mathbb F_p}J_X(K)[p]\longrightarrow0,
$
$
s_\Sigma=\frac1m\sum_{c\in\Sigma}\operatorname{sp}_c,\qquad
W=\ker s_\Sigma
 \simeq\mu_p\otimes_{\mathbb F_p}J_X(K)[p].
\tag{1132.26}
$
$K_2$ 为整 Milnor/Quillen $K_2$；“nr” 表示每个闭点的 tame symbol
均为 $1$。$s_\Sigma$ 是对常数项的 retraction。

准确角色关系是
$
W_{\omega^\alpha}\simeq
\bigl(\mu_p\otimes J_X(K)[p]\bigr)_{\omega^\alpha},
\quad\text{其 Jacobian 角色为 }\omega^{\alpha-1}.
$
将 $\alpha=2-r$ 与 (1132.5) 配合，得到
$
\boxed{\quad W_{\omega^{\,2-r}}=0
 \quad\text{在 (1132.2) 下。}\quad}                  \tag{1132.27}
$
特别，
$
\boxed{\quad p\nmid B_{p-3}\quad\Longrightarrow\quad
 W^\Delta=0.\quad}                                  \tag{1132.28}
$
等价地，任何 $\Delta$-不变的未分歧整 $K_2[p]$ 类
若全尖点平均为零，就本身为零；若未规范，其类来自 $K_2(K)[p]$。
此处的“常数角色”指 $\Delta$ 的平凡角色，不自动等于一个已经算出的常数符号。

本篇没有假设某个正在构造的原 cup 已经属于 (1132.26)。
若仅知一个模 $p$ 的 Brauer 类、一个有理系数 Manin 关系，
或一组几何 Weil pairing 为零，均还不能直接代入 (1132.28)。
必须分别付实际整类、$p$-torsion、全 tame 与原规范。
更高 $p$-primary 的推广也须先在其实际群上定义 specialization；
不能因 $\mu_p\subset K$ 就假定 $\mu_{p^a}\subset K$。

## 8. 与已成分支的关系及来源

R1131 用原正商的高偶尖点线，锁定一个完整 Fricke 正块及其实际非分裂扩张；
本文用完整 Cartan 的低奇尖点线，锁定完整正规化子负块。
两条线各在真实曲线上构造，方向由各自 cusp 作用确定，互不替代。
本篇不以 $B_r$ good 替换 (1132.2) 的两个条件；
$p\mid B_{p-3}$ 的常数残余支仍须另行处理。
R1127 只在其指定 Gaussian 条件下给该 Bernoulli 分支的跨盘一次标签，
不能因此宣布一般 $p$ 的四阶问题已完成。

实际读取的原始来源：

- [C] Pierfrancesco Carlucci，*Cuspidal divisor class groups of non-split Cartan modular curves*，
  Acta Arith. 187 (2019), 301–327，
  [DOI 10.4064/aa8516-6-2018](https://doi.org/10.4064/aa8516-6-2018)；
  [作者全文 arXiv:1605.00375](https://arxiv.org/pdf/1605.00375)。
  本篇消费作者版本的 Proposition 4.5、Theorem 4.6（印刷第12–13页）、
  full-level 尖点标记及 determinant 对常数的实际作用。
  原正商 Galois 规范沿 R1062 的 Remark 6.6/7.2 核读记录。
- [dSE] Bart de Smit、Bas Edixhoven，*Sur un résultat d'Imin Chen*，
  Mathematical Research Letters 7 (2000)，
  [DOI 10.4310/MRL.2000.v7.n2.a1](https://doi.org/10.4310/MRL.2000.v7.n2.a1)；
  [作者 PDF](https://pub.math.leidenuniv.nl/~smitbde/papers/2000-de_Smit_Edixhoven.pdf)。
  本篇用 Theorem 3 的第一条 $\ell\nmid p^2-1$ 条件及
  Theorem 4 的第一条 prime-to-$\ell$ 同源和拉回核证明，
  不是只引用其有理关系或正规化子第二条。
- [Ca] Frank Calegari，*Eisenstein deformation rings*，Compositio Math. 142 (2006), 63–83，
  [DOI 10.1112/S0010437X05001661](https://doi.org/10.1112/S0010437X05001661)；
  [作者 PDF](https://www.math.uchicago.edu/~fcale/papers/Eisenstein.pdf)。
  原前提在印刷第65页，Definition 2.5 / Theorem 2.6 在第66页。
  仅取 $k=r\in[2,m)$ 的正指标范围。
- 特征零 rank-two/new multiplicity-one、纯 toric 惯性过滤、
  Kummer 同余以及 Suslin/Weibel 的精确 integral $K_2[p]$ 范围，
  按 R1131、R1062/R1069 与上述原 K2 笔记的已核 primary 和证明消费。

root 给出全文推导；o2_high_coefficient 独立核读三份主要来源，
并纸核完整 Cartan transfer、奇角色方向、Jacobi/Bernoulli valuation、
真实 $w$ 负号、rank-two/Schur 步骤、整商单射及 $\mu_p$ 扭曲。
本篇不含数学程序执行。


全文精确复核：root、global_route、o2_high_coefficient 对候选726c4ea6的全部八节及低偶指标推广独立纸核通过；发布版只将数学定界符机械转换为仓库规定的美元符号。
