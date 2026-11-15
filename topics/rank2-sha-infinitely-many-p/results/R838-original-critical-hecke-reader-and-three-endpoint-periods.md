# R838 — 原端点第四槽的完整临界 Hecke 系数读数

日期：2026-11-15。**状态：已证明。**

本篇给 R831 的三个真实端点来源同一个临界 Hecke 系数读取公式。
它保留完整临界广义特征空间的长度，不假设该空间只有二维；
保留原两个 Coleman 原函数项、全部坏处向量及 Frobenius 分母。
三条端点 Abel–Jacobi 值共用一个非零比较标量。

本篇不证明这些端点值非零，也不把它们相认 R814 的 canonical 类。
以下系数一律在完整临界谱投影之后读取；不是原未投影有限 q 卷积。

## 1. 同一原来源与原第四槽

固定 R826、R830、R831 的
$$
K=\mathbf Q(\omega),\qquad N=10404,\qquad M=2601,
\qquad f=\theta(\psi_{17}),
\qquad g_j=\theta(\eta_j^{-2}\psi_0).
\tag{1}
$$
$f$ 是 level $N$ 的平凡 nebentypus 新形式，$g_j$ 是 level $M$
的平凡 nebentypus 新形式。所有 $2,3,17$ 角色和 R830 的有限局部
test vectors 不变。用下表固定顺序：
$$
\begin{array}{c|ccc}
\nu&4&10&16\\ \hline
(j,k)&(10,16)&(16,4)&(4,10).
\end{array}
\tag{2}
$$
端点是共同目标上的 $Z_{02}^{(1)}$，第二、三因子分别使用
$q_0^{(1)}$、$q_2^{(1)}$；微分为 $g_j(Q)dQ/Q$ 和
$4g_k(Q^4)dQ/Q$，而非两个同一退化映射。

取原普通 ray 上的 $p>17$，保原嵌入及
$$
p=\pi\bar\pi,\qquad v_p(\pi)=1,\qquad
\alpha_f=-\bar\pi,\quad \beta_f=-\pi .
\tag{3}
$$
原 $g_j$ 的两个根是 $\bar\pi,\pi$。令零常数的实际原函数为
$$
\theta G_j=g_j-\bar\pi Vg_j,\qquad
\theta=Q\,d/dQ .
\tag{4}
$$
其完整 CM 整理想展开已在 R826 附录 A 支付。定义
$$
\boxed{
F_{\nu,p}(Q)
=4G_j(Q)g_k(Q^4)-\bar\pi G_k(Q^4)g_j(Q^p),\qquad
\Xi_{\nu,p}=F_{\nu,p}(Q)\frac{dQ}{Q}.
}
\tag{5}
$$
两个原函数均为 weight-zero 过收敛模形式，故 (5) 是 weight-two
过收敛尖点形式。乘积的第二因子为尖点形式，保证在所有 cusp
消失，不只是其 $\infty$ 展开常数为零。

记
$$
\mathcal A_{\nu,p}
=AJ_p(Z_{02,\nu}^{(1)})
  (\omega_f\otimes\omega_{g_j}\otimes\omega_{g_k}).
$$
R831(27) 给准确式
$$
\boxed{
\mathcal A_{\nu,p}
=\frac{\langle\omega_f,[\Xi_{\nu,p}]\rangle_{X_1(N)}}
 {1+\bar\pi/\pi^2}.
}
\tag{6}
$$
括号先使用 Besser 的 Frobenius 相容 proper-cohomology 投影，
再使用原杯积顺序。分母非零，赋值为 $-2$。
R831 中 $X_1/X_0$ 的 $1632,816$ 与 old projector 的 $12$
均已包含于 (6) 的原规范，本篇不再改变它们。

## 2. 完整的临界块及其谱投影

令 $E/\mathbf Q_p$ 足够大，包含原角色系数、$\pi$ 及下述有限块。
令
$$
f_\beta=f-\alpha_f Vf=f+\bar\pi Vf,
\qquad a_1(f_\beta)=1,\qquad Uf_\beta=-\pi f_\beta .
\tag{7}
$$
取 weight-two、原 tame level $N$、原 diamond-trivial 来源上的
完整广义 Hecke 特征空间
$$
\mathcal M_p
=S_2^\dagger(\Gamma_1(N),E)[I_{f_\beta}^{\,\infty}],
\qquad e_p=\dim_E\mathcal M_p .
\tag{8}
$$
这里 $I_{f_\beta}$ 使用所有素于 $Np$ 的 Hecke 特征及实际 $U$ 根
$-\pi$。$f$ 的 tame conductor 恰为 $N$，不添较低 tame level 的
旧副本。

用
$$
\mathsf P_p:S_2^\dagger\longrightarrow\mathcal M_p
\tag{9}
$$
表示**完整临界谱投影**：先在适当的 dagger Banach 模块上取包含
$-\pi$ 的有限 slope 部分，再取该 $U$ 广义特征与全部原 Hecke
特征的主分量。更换足够小的 dagger 邻域不改变此投影。
这是随 $p$ 改变的解析谱投影，不是 Jacobian 上固定的 tame
Chow 幂等元。

原杯积满足
$$
\langle\omega_f,Uv\rangle=-\pi\langle\omega_f,v\rangle
\tag{10}
$$
及良好 Hecke 的伴随公式。因此
$$
\langle\omega_f,[F\,dQ/Q]\rangle
=\langle\omega_f,[\mathsf P_pF\,dQ/Q]\rangle .
\tag{11}
$$
特别其所读的是 forms 的 $U$-critical 分量，而非 ordinary-forms
分量。对应 proper cohomology 的 $\varphi$ 根是 $-\bar\pi$。

### 2.1 权二的 exact 子空间

令
$$
\mathcal E_p
=\mathcal M_p\cap\theta M_0^\dagger .
$$
Coleman 的 quotient 定理和边界情形定理在权二给
$$
0\longrightarrow\mathcal E_p
 \longrightarrow\mathcal M_p
 \xrightarrow{\mathrm{KS}} H^1_{\mathrm{dR}}(X_1(N))_{f,\varphi=-\bar\pi}
 \longrightarrow0 .
\tag{12}
$$
右端一维。这里的 KS 包含 (6) 的同一 proper 投影。

权二有 $\ker(\theta:M_0^\dagger\to M_2^\dagger)=E$ 的常数项；
Coleman Corollary 7.2.2 在此明确先除去它。该常数是 Eisenstein
来源，在当前非 Eisenstein $f$ 块上没有贡献。
所以
$$
\dim_E\mathcal E_p=e_p-1 .
\tag{13}
$$
这一步使用 Coleman 原文的权二结论，不把 CG2 中要求 $k\ge3$
的整 $\Lambda$-adic control theorem直接用于 $k=2$。

## 3. 原临界 Hecke 环是一个完整长度的截断参数环

记 $A_p$ 为良好 Hecke 与 $U$ 在 $\mathcal M_p$ 上的像，
$\mathfrak m_p$ 为其极大理想。Hsu 的 CM 临界计算给
$$
\mathcal M_p[\mathfrak m_p]=E f_\beta,\qquad
\dim_E\mathcal M_p[\mathfrak m_p^2]=2 .
\tag{14}
$$
其假设中，选 $\psi_{17}$ 取 unit 值的素位 $\mathfrak u$，则
$$
\frac{\psi_{17}(\mathfrak u)}
     {\psi_{17}^{\,c}(\mathfrak u)}
=\frac{\bar\pi}{\pi}\ne p
$$
由赋值立即满足。这不使用残余大像或把 Hsu Proposition 4.3
的另一局部化非零当成已知。

以下小证明同时支付所需 q-duality 与整个长度。

**引理。** 映射
$$
A_p\longrightarrow\mathcal M_p^\vee,\qquad
a\longmapsto\big(H\longmapsto a_1(aH)\big)
\tag{15}
$$
为同构；并存在参数 $t$ 使
$$
A_p\simeq E[t]/(t^{e_p}),\qquad e_p\ge2 .
\tag{16}
$$

**证明。** $\mathcal M_p^\vee/\mathfrak m_p\mathcal M_p^\vee$
与 $\mathcal M_p[\mathfrak m_p]^\vee$ 对偶。因为
$a_1(f_\beta)=1$，$a_1$ 在该一维商中非零。
Nakayama 引理遂使 (15) 满射。$A_p$ 按其实际像定义，忠实作用于
$\mathcal M_p$ 及其对偶；若一个元素杀掉生成元 $a_1$，
便杀整个对偶，因此为零。这证明 (15)。

再由 (14)、(15)，
$$
\dim_E A_p/\mathfrak m_p^2=2,\qquad
\dim_E\mathfrak m_p/\mathfrak m_p^2=1.
$$
有限局部 $E$-代数有一个极大理想生成元，故是某
$E[t]/(t^e)$；其维数由 (15) 恰为 $e_p$。证毕。

这也与 CG2 Proposition 2.4.4（其范围为 $k\ge1$）的
$a_1(TH)$ perfect pairing一致。没有以 classical Hecke 环的
半单性替代这里实际的非半单环。

由 (16)，$\mathcal M_p$ 是 uniserial $A_p$-模。
(12) 的核是唯一的长度 $e_p-1$ 子模，所以
$$
\boxed{\mathcal E_p=\mathfrak m_p\mathcal M_p.}
\tag{17}
$$
特别 $f_\beta$ 本身 exact，并不代表 (12) 的非零商。

## 4. 可以选择一个真正惰性 Hecke 参数

对良好 split 素数 $\ell$，Hsu 的一阶广义特征公式给
$T_\ell-a_\ell(f)\in\mathfrak m_p^2$；
同时 $U-\beta_f\in\mathfrak m_p^2$。
因此必存在至少一个
$$
\ell_* \nmid Np,\qquad \ell_*\text{ 在 }K\text{ 中惰性},
\qquad T_{\ell_*}\notin\mathfrak m_p^2 .
\tag{18}
$$
否则所有生成元的 augmentation 均属于 $\mathfrak m_p^2$，
将与 $\dim\mathfrak m_p/\mathfrak m_p^2=1$ 矛盾。
对惰性 $\ell_*$，原 $a_{\ell_*}(f)=0$，所以没有遗漏标量减项。

更具体地，Hsu Theorem 1.1 的该一阶系数为
$$
a'_{\ell_*}
=\psi_{17}(c\,\mathrm{Frob}_{\ell_*})
\,\mathfrak e_p(\mathrm{Frob}_{\ell_*}^{\,2}),
\quad
\mathfrak e_p\in
H^1_{\mathfrak u}(K,\psi_{17}/\psi_{17}^{\,c}) .
\tag{19}
$$
选择 (18) 就是选择这个系数非零的良好素数。
本篇不把最小惰性素数、坏素数2或某个固定良好素数5
先行认作合格参数；$\ell_*$ 可以随 $p$ 变化。
这也不是原高权 $\lambda_j$ 的 canonical 类。

于是可以在 (16) 中准确取
$$
t=T_{\ell_*}.
\tag{20}
$$
不需要预先知道 $e_p=2$。Hsu Proposition 4.3 所刻画的
额外局部化门仅在想把完整 $e_p$ 降成2时才需要。

## 5. 最高 Hecke 系数恰读取上同调商

令 $r_p=e_p-1$。对任意 $\mathcal M_p$ 中的 $H$，定义
$$
d_{p,\ell_*}(H)=a_1(T_{\ell_*}^{\,r_p}H).
\tag{21}
$$
由 (16)、(17)，
$$
\boxed{
\ker d_{p,\ell_*}=\mathcal E_p,\qquad
d_{p,\ell_*}\ne0 .
}
\tag{22}
$$

这里还可固定唯一的完整归一代表 $H^{\mathrm{top}}_{p,\ell_*}$：
$$
a_1(T_{\ell_*}^{\,j}H^{\mathrm{top}}_{p,\ell_*})
=\begin{cases}0,&0\le j<r_p,\\1,&j=r_p.\end{cases}
\tag{23}
$$
因 $1,t,\ldots,t^{r_p}$ 是 $A_p$ 的基，(15) 保证存在唯一性。
并且
$$
T_{\ell_*}^{\,r_p}H^{\mathrm{top}}_{p,\ell_*}=f_\beta .
\tag{24}
$$
所有 $H$ 准确分解为
$$
H-d_{p,\ell_*}(H)H^{\mathrm{top}}_{p,\ell_*}
\in\theta M_0^\dagger .
\tag{25}
$$

定义本篇的单一比较标量
$$
\boxed{
\mathscr P_{f,p,\ell_*}
=\left\langle\omega_f,
 [H^{\mathrm{top}}_{p,\ell_*}\,dQ/Q]\right\rangle_{X_1(N)} .
}
\tag{26}
$$
它非零：$H^{\mathrm{top}}$ 在 (12) 中有非零像，而
$\varphi=-\bar\pi$ 线与全纯 $\varphi=-\pi$ 线的杯积非退化。
采用 R826 的 $\langle\eta_f^{\rm ur},\omega_f\rangle=1$ 规范时，
若 $[H^{\mathrm{top}}]=c\,\eta_f^{\rm ur}$，则
$\mathscr P_{f,p,\ell_*}=-c$。因此没有暗中调换杯积顺序。

于是对任意过收敛尖点形式 $F$，
$$
\boxed{
\langle\omega_f,[F\,dQ/Q]\rangle
=\mathscr P_{f,p,\ell_*}\,
 a_1(T_{\ell_*}^{\,e_p-1}\mathsf P_pF).
}
\tag{27}
$$
本式是同一个原形式的完整上同调恒等式；它不把 exact 向量
$f_\beta$ 与非 exact 的 $H^{\mathrm{top}}$ 混为一线。

(26)是一个实际非零 $p$-adic 比较标量。
本篇不证明它为代数数、$p$-单位或固定 $p$ 无关的复周期；
其 X1 规范也不被一个未说明的“period unit”吸收。
若全程改用原 X0 cup，其准确改变为 R831 的次数1632。

## 6. 完整有限 Fourier 读取式

令 $a_n(H)=[Q^n]H$。在平凡 nebentypus 的 weight-two 空间，
良好 Hecke 关系为
$$
T_{\ell_*}T_{\ell_*^a}
=T_{\ell_*^{a+1}}+\ell_*T_{\ell_*^{a-1}}\quad(a\ge1),
\qquad a_1(T_nH)=a_n(H).
$$
归纳给
$$
\boxed{
d_{p,\ell_*}(H)
=\sum_{j=0}^{\lfloor r_p/2\rfloor}
\left\{\binom{r_p}{j}-\binom{r_p}{j-1}\right\}
\ell_*^j\,a_{\ell_*^{\,r_p-2j}}(H),
}
\tag{28}
$$
其中 $\binom{r_p}{-1}=0$。证明只需把
$T_{\ell_*}^{\,r}$ 按 $T_{\ell_*^{r-2j}}$ 展开；
相邻项使用 Pascal 恒等式，初值 $r=0,1$ 直接成立。

定义原来源的读数
$$
\mathcal D_{\nu,p,\ell_*}
=d_{p,\ell_*}(\mathsf P_pF_{\nu,p}).
\tag{29}
$$
特别当已经另外知道 $e_p=2$ 时，
$\mathcal D_{\nu,p,\ell_*}=a_{\ell_*}(\mathsf P_pF_{\nu,p})$；
本篇主式 (28) 不依赖这个附加情形。

**投影不可删除。** (28) 只在 $\mathsf P_pF_{\nu,p}$ 上读取有限
个系数。$\mathsf P_p$ 本身来自完整过收敛谱分解，随 $p$ 变化，
并且可使用原输入的无限 Fourier 尾。
即使 $\ell_*^{r_p}<p$，也不能据此从 (5) 删除
$g_j(Q^p)$ 那一项，或将 (29) 改写为未投影的有限整理想卷积。
固定 tame Chow projector 只固定 proper 的 $f$ 因子，
没有给出 forms 上的 (9) 或其最高广义层。

## 7. 三条端点值共用同一个准确读数规范

把 (27) 代入 (6)，得到本篇主式：
$$
\boxed{
\mathcal A_{\nu,p}
=\frac{\mathscr P_{f,p,\ell_*}}{1+\bar\pi/\pi^2}
\,\mathcal D_{\nu,p,\ell_*},
\qquad \nu=4,10,16 .
}
\tag{30}
$$
这里 $e_p,\ell_*,\mathsf P_p,\mathscr P_{f,p,\ell_*}$ 全部只由同一个
$f$ 与普通地点决定；不随有序对 $(g_j,g_k)$ 重新选择。
因此三值向量准确是
$$
\begin{pmatrix}
\mathcal A_{4,p}\\
\mathcal A_{10,p}\\
\mathcal A_{16,p}
\end{pmatrix}
=
\frac{\mathscr P_{f,p,\ell_*}}{1+\bar\pi/\pi^2}
\begin{pmatrix}
\mathcal D_{4,p,\ell_*}\\
\mathcal D_{10,p,\ell_*}\\
\mathcal D_{16,p,\ell_*}
\end{pmatrix}.
\tag{31}
$$
这是同一非零标量，而不是三条任意归一的比例。
对任何给定有限系数组合，左侧关系恰等价于右侧同一组合。

此外，R831 的全部 old 测试矩阵逐项传为
$$
\big(d_{p,\ell_*}(\mathsf P_pF_{ab})\big)_{a,b=0}^2
=
\begin{pmatrix}
0&0&\mathcal D_{\nu,p,\ell_*}\\
0&0&0\\
-\mathcal D_{\nu,p,\ell_*}&0&0
\end{pmatrix},
\tag{32}
$$
其中 $F_{ab}$ 始终保 R831(26) 的 $2^a,2^b$ 和两个原函数项。
(32)是既有 Chow 恒等式在新读数中的准确运输，
不增加第三个独立对角来源。

R832 已证明这些端点类全在 $\lambda_\nu$ Chow 分量；
(30) 因而读取这个原纯分量的第四槽。
但它并不证明 $\mathcal D_{\nu,p,\ell_*}\ne0$，
也不把原 $e_p$、$\ell_*$ 或比较标量放入一个固定跨 $p$ 的有限表。

## 8. 与 canonical 原三值的准确分界

R826 附录 B 的另一个已付身份是：原 weight-four
$F_\nu^{(4)}=\theta(\lambda_\nu)$ 的 Kato 临界斜率函数在中心的
首导数，由同原 $I_{\nu,-2,p}^{\,2}$ 给出。
它的临界斜率是3；本篇 (9) 是 weight-two $f$ 的临界斜率1。

(30) 现在把需要比较的端点一侧固定为同一明确 functional
$a_1(T_{\ell_*}^{e_p-1}\mathsf P_p\,\cdot)$，并保留全部来源。
要把它等同 R814/R804 的 canonical 系数，仍须证明两份实际
全局来源的比较；相同 $\lambda_\nu$、相同 Frobenius 分母、
或三条 ordinary 槽已为零都不单独给这条比较。
本篇没有使用任何端点 AJ 非零假设，没有新增原中央零。

## 9. 原文依据及可复现范围

本篇无新增数值计算。局部环、最高系数和三条共同比例的证明在
第3–7节给出，所用已有定理的准确范围如下。

- R. F. Coleman, *Classical and overconvergent modular forms*,
  Invent. Math. **124** (1996), 215–241：
  Theorem 5.4、Theorem 7.2、Corollary 7.2.2；
  后者明确含 $k=2$ 的常数商。
  [已发表原文扫描](https://www.wstein.org/people/coleman/papers/classical_and_overconvergent_forms.pdf)。
- C.-Y. Hsu, *Fourier coefficients of the overconvergent generalized
  eigenform associated to a CM form*,
  Int. J. Number Theory **16** (2020), 1185–1197，
  DOI [10.1142/S1793042120500608](https://doi.org/10.1142/S1793042120500608)；
  [作者预印本](https://arxiv.org/pdf/2002.00324)：
  §1 的 $I^2$ 广义空间、Theorem 1.1、
  Proposition 2.2/2.4、Corollary 2.6、Lemma 4.1。
  Proposition 4.3 的额外局部化非零没有在本篇假定。
- F. Castella, C. Wang-Erickson,
  *Critical $\Lambda$-adic modular forms and bi-ordinary complexes*,
  Tunisian J. Math. **7** (2025), 677–754，
  DOI [10.2140/tunis.2025.7.677](https://doi.org/10.2140/tunis.2025.7.677)；
  [作者稿](https://web.math.ucsb.edu/~castella/CG2.pdf)：
  Proposition 2.4.4 的 $k\ge1$ perfect q-duality、
  Example 2.7.6/7.1.3。
  本篇未调用其 $k\ge3$ integral control 或带额外 conductor
  条件的 adjoint-unit 解释。
- [R826](R826-fixed-low-weight-cm-triple-and-fourth-de-rham-slot.md)、
  [R830](R830-distinct-degeneracy-test-vectors-and-fourth-slot.md)、
  [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)、
  [R832](R832-original-triple-chow-purity-and-rank-zero-contractions.md)：
  原有限角色、实际端点、完整两项杯积、次数与纯 $\lambda$ 来源。
