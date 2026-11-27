# R1087. 原 full-47 的 principal 角理想与严格消去全部 cusp 块的整对应

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；global_route。

**状态：已证明，纯纸面；没有新数学执行。**
本文在原 $X=X_{\rm ns}^{+}(47)$、$J=\operatorname{Jac}(X)$ 上，
给出原角代数的完整有理分解及一个明确的整对应
$Z_{\rm ps}$。它非零、Rosati 自伴、degree 与 Hodge trace 都为零；
在全部 cuspidal 型上严格为零，在 principal 型上于 $283,4513$ 可逆。
其完整 fixed divisor 仍保留，不从这些谱性质臆断高度非零。

## 1. 完整原角代数

令
$$
G=\operatorname{PGL}_2(\mathbf F_{47}),\qquad
N=N_{\rm ns}/\mathbf F_{47}^{\times},\qquad
\mathscr N=G/N.
$$
$\mathscr N$ 是原 $1081$ 个无定向 necklaces。
[R1078](R1078-original-level47-Cartan-correspondences-and-fixed-cycles.md)
证明它的全部非恒等 orbitals 为
$$
R_C,\qquad C\in\mathbf F_{47}/\pm,\quad C\ne\pm1,
$$
共有 $23$ 个；degree 为 $d_0=24$、其余 $d_C=48$。
其完整 composition 是原对应的 cycle 恒等式，不只是抽象置换矩阵。

### 1.1 全部 spherical types 与三个域

[R1083](R1083-original-level47-auxiliary-Hecke-fields-and-scalar-fibers.md)
已经完整核准 finite character 与 normalizer parity：

- principal series $\pi_\chi$ 的 $N$-fixed 线存在且为一维，
  当且仅当 $\chi(-1)=1$。排掉 $\chi^2=1$ 后，全部 $\chi$ 恰为
  $\mathbf F_{47}^{\times}$ 的非平凡 order-$23$ characters，
  按 $\chi\sim\chi^{-1}$ 有 $11$ 个；$\dim\pi_\chi=48$。
- cuspidal $\pi_\theta$ 的 $N$-fixed 线存在且为一维，
  当且仅当 $\theta$ 是 order-$48$ nonsplit torus quotient 上的 odd character。
  按 $\theta\sim\theta^{-1}$，order-$48$ 有 $8$ 个、
  order-$16$ 有 $4$ 个；每个维数 $46$。
- Steinberg、quadratic-twisted Steinberg 及非平凡一维 determinant
  character 都不贡献。trivial representation 贡献一次。

由 Frobenius reciprocity，以上各项在 $\mathbf C[\mathscr N]$ 中的重数
就是相应 fixed-line 维数。因此
$$
\mathbf C[\mathscr N]
 =\mathbf1\ \oplus\!
   \bigoplus_{\chi}\pi_\chi\
   \oplus\!\bigoplus_{\theta,\ \operatorname{ord}\theta=48}\pi_\theta\
   \oplus\!\bigoplus_{\theta,\ \operatorname{ord}\theta=16}\pi_\theta,
\tag{1087.1}
$$
且完整维数检查为
$$
1+11\cdot48+8\cdot46+4\cdot46=1081.
$$
特别这是 multiplicity-free 分解，无漏掉的 spherical constituent。

记
$$
K_n=\mathbf Q(\zeta_n+\zeta_n^{-1}).
$$
principal 的完整 character field 是 $K_{23}$，
两类 cusp character fields 分别是 $K_{48},K_{16}$。
这可以由 split / nonsplit regular 元的原 character traces
$\chi(a)+\chi(a)^{-1}$、$-\theta(t)-\theta(t)^{-1}$ 直接读取。
三个 Galois orbits 的大小准确为 $11,8,4$。

于是完整有理 orbital 代数为
$$
\operatorname{End}_{\mathbf QG}\mathbf Q[\mathscr N]
 \simeq \mathbf Q\times K_{23}\times K_{48}\times K_{16}.
\tag{1087.2}
$$
这里无需另加一个可能的 Schur-index 矩阵块：
复数上每项的 $N$-fixed 维数为一，corner 本身是交换代数；
它的有理 primitive factors 正由上述 Galois orbits 决定。

### 1.2 在原 Jacobian 上没有再丢掉一个域

恒等 orbital 与全部非恒等 orbitals 的和为 all-ones operator，
是 trivial projector 的 $1081$ 倍。
原几何中它是 $j^*j_*$，经 genus-zero 的 $X(1)$ 因子，
所以在 $J$ 上为零。

[R1081](R1081-certified-original-level47-Cartan-trace-and-integral-Hecke-algebra.md)
已经用原 complete fixed cycles 和 Rosati trace pairing
准确认证实际 image rank 为 $23$，唯一核正是这一条关系。
因此不是仅凭 permutation representation 猜测 Jacobian 上的 image，
而是严格得到
$$
\boxed{\quad
\mathcal A_{\rm ang}:=\mathbf Q[R_C]\subseteq\operatorname{End}_{\mathbf Q}^{0}(J)
 \simeq K_{23}\times K_{48}\times K_{16}.
\quad}
\tag{1087.3}
$$
称其第一项为 principal 理想，其余两项之和为 cusp 理想。
这里“cusp 型”是 finite cuspidal representation，
不指曲线边界的 $23$ 个 cusp 点。

## 2. 从 split 共轭类直接得到原整对应

取 $a\in\mathbf F_{47}^{\times}$，假设 $a\ne\pm1$。
令 $\mathscr K_a$ 为 $G$ 中 $\operatorname{diag}(a,1)$ 的共轭类。
其 centralizer 是 split torus，order 为 $46$，所以
$$
|\mathscr K_a|=47\cdot48=2256.
\tag{1087.4}
$$
以下仅使用 $a=5,25$。因为 $(5/47)=-1$ 且 $46=2\cdot23$，
$5$ 的 order 为 $46$；$25=5^2$ 的 order 为 $23$。
两者都不是 projective involution。

### 2.1 精确整系数及真正的有理下降

固定原 necklace $x_0$。
对每个非恒等角 $C$，取角为 $C$ 的任意目标 $y_C$，定义
$$
k_C(a)=
 \#\{g\in\mathscr K_a:\ g x_0g^{-1}=y_C\}.
\tag{1087.5}
$$
共轭类和与 $G$ 作用交换，且 $N$ 在每个原角轨道上可迁，
故这个整数与 $y_C$ 的选择无关。

split regular、projective order 大于二的元素不能属于 $N$：
$N$ 的 rotation subgroup 是 nonsplit torus；
其外陪集的 projective 元素全是 involutions。
所以 $\mathscr K_5,\mathscr K_{25}$ 没有元素固定任何 necklace。
它们的 diagonal coefficient 都为零。

定义原 cycle
$$
K_a=\sum_C k_C(a)R_C\qquad(a=5,25).
\tag{1087.6}
$$
每个 coefficient 是非负整数，所有项都是 R1078 的实际有限对应，
因而 $K_a$ 定义在 $\mathbf Q$ 上、没有 diagonal component，
且
$$
\deg K_a=\sum_C k_C(a)d_C=2256.
\tag{1087.7}
$$

这也说明此处下降没有偷偷使用一个错误的 geometric group action：
没有把每个 $g\in G$ 声称为选定 full-level 连通分支上的
$\mathbf Q$-automorphism。
(1087.5) 只在原 finite moduli fiber 中计数；
(1087.6) 才是定义于 $\mathbf Q$ 的实际对应。
R1078 的完整 composition 恒等式把这个 finite orbital 计算
准确送入 $\operatorname{End}_{\mathbf Q}(J)$。

每个 $R_C$ 对称，所以 $K_a$ Rosati 自伴。
也可从 $\mathscr K_a^{-1}=\mathscr K_a$ 看出相同结论：
$\operatorname{diag}(a^{-1},1)$ 与 $\operatorname{diag}(a,1)$
在 $G$ 中共轭。

### 2.2 全部实际 eigenvalues

中心类和在不可约 $\pi$ 上的 scalar 是
$|\mathscr K_a|\operatorname{char}_\pi(a)/\dim\pi$。
对原 spherical types，split regular character 给
$$
K_a|_{\pi_\chi}=47\bigl(\chi(a)+\chi(a)^{-1}\bigr),
\qquad K_a|_{\pi_\theta}=0.
\tag{1087.8}
$$
后一式覆盖 order $48$ 和 $16$ 的全部 cusp 型，且是特征零的准确零。

令 $s=\zeta_{23}+\zeta_{23}^{-1}$，选择 $\chi(5)=\zeta_{23}$；
换该选择只是 $K_{23}$ 的 Galois conjugation。
由 (1087.3)，(1087.8) 在原角代数中给
$$
K_5=(47s,0,0),\qquad K_{25}=(47(s^2-2),0,0).
\tag{1087.9}
$$

## 3. 明确的非零、迹零、cusp-annihilating 对应

置
$$
\boxed{\quad Z_{\rm ps}=K_5-K_{25}.\quad}
\tag{1087.10}
$$
这是原整对应的 signed cycle；它仍不含 diagonal component。
由 §2，
$$
\deg Z_{\rm ps}=0,\qquad Z_{\rm ps}^{\dagger}=Z_{\rm ps},
\qquad
Z_{\rm ps}=(47(2+s-s^2),0,0).
\tag{1087.11}
$$
主分量
$$
2+s-s^2=(2-s)(1+s)
$$
非零：primitive $23$ 次根不可能给 $s=2$ 或 $s=-1$。
因此 R1081 的 actual faithfulness 保证 $Z_{\rm ps}$ 在 $J$ 上非零。

原 $H^0(X,\Omega^1)$ 的 principal 部分是某个有限维
$K_{23}$-vector space；其 rational trace 是相应整数重数乘域迹。
又
$$
\operatorname{Tr}_{K_{23}/\mathbf Q}(s)
 =\operatorname{Tr}_{K_{23}/\mathbf Q}(s^2-2)=-1,
$$
因为乘二置换全部非零 $23$ 次 characters 的 inverse pairs。
所以
$$
\boxed{\quad
\operatorname{Tr}(Z_{\rm ps}\mid H^0(X,\Omega^1))=0.
\quad}
\tag{1087.12}
$$
这不要求事先将每一个 actual Hecke factor 与某个角 eigenvalue 数值配对。

### 3.1 在所选辅助素处的严格整分裂

有
$$
\operatorname{Norm}_{K_{23}/\mathbf Q}(2-s)=23,\qquad
\operatorname{Norm}_{K_{23}/\mathbf Q}(1+s)=\pm1.
\tag{1087.13}
$$
第一式由 $(1-\zeta)(1-\zeta^{-1})=2-s$ 和 $\Phi_{23}(1)=23$。
第二式由
$$
1+s=\zeta^{-1}\frac{1-\zeta^3}{1-\zeta};
$$
在全 cyclotomic field 中 numerator 与 denominator 的 norm 都为 $23$，
所以 real norm 的平方为一。

因此 $Z_{\rm ps}$ 的非零 principal eigenvalue 的域 norm 仅含素数
$23,47$，并且
$$
\left|\operatorname{Norm}_{K_{23}/\mathbf Q}
 (47(2+s-s^2))\right|=23\cdot47^{11}.
\tag{1087.14}
$$
特别在 $q=283,4513$ 上它对 principal 部分为单位，
对 cusp 部分准确为零。

这个分裂也在实际整 Hodge/Lie 格上成立，而不只是泛纤维：
设 $m(T)\in\mathbf Z[T]$ 是其非零 principal 元的最小多项式。
其常数项在这两个素处为单位，且
$$
e_{\rm cusp}=\frac{m(Z_{\rm ps})}{m(0)},\qquad
e_{\rm ps}=1-e_{\rm cusp}
\tag{1087.15}
$$
在 $\mathcal A_{\rm ang}\otimes\mathbf Q_q$ 中分别为 cusp/principal projector。
它们是实际整 endomorphisms 的 $\mathbf Z_q$-线性组合，
故保持实际 good-model Hodge/Lie 格。
由 (1087.14)，$Z_{\rm ps}$ 在 $e_{\rm ps}$ 的整格上可逆；
在 $e_{\rm cusp}$ 的格上为零。
所以这两个素处的整 kernel 准确是 cusp 格，没有额外同阶 congruence kernel。

原 angles 与全部 away-$47$ Hecke operators 交换。
R1081 的完整 Hecke 有理代数在原 Hodge 空间上具有 multiplicity one；
其 centralizer 就是自身。因此这些角算子属于同一个有理 Hecke 代数，
且 R1081 的最大整序证书使上述整分裂与实际 Hecke 分块相容。

R1083 已证明 $283$ 的 principal completion degree 为 $11$，
$4513$ 同样如此；
故 R1081 在 $4513$ 认证的全部十六个 $\mathbf Z_{4513}$ 块都属于 cusp 部分。
对每个这样的真实 eigencharacter $\vartheta_{\mathfrak m}$，现在得到
$$
\boxed{\quad\vartheta_{\mathfrak m}(Z_{\rm ps})=0
       \quad\text{在 }\mathbf Z_{4513}\text{ 中准确成立。}\quad}
\tag{1087.16}
$$
这比仅仅模 $4513$ 为零更强，但没有给出其 Mordell–Weil 非饱和或高度值。

## 4. 完整 fixed divisor：不能与谱零一并删掉

沿用 R1078 的实际角变换
$\mathcal F_4^*,\mathcal F_3^*$，并对原非恒等角的有理线性组合线性延拓。
如果
$$
Z_{\rm ps}=\sum_C z_C R_C,\qquad
n_Z=\sum_C z_C n_C,
$$
则原 signed fixed cycle 准确为
$$
\operatorname{Fix}Z_{\rm ps}
 =\frac12(\mathcal F_4^*Z_{\rm ps})(y_4)
  +\frac23(\mathcal F_3^*Z_{\rm ps})(y_3)
  +n_Z C_\infty.
\tag{1087.17}
$$
所有 source/target 稳定子、二/三倍拉回重数、
两条 cubic branches 和全部 $23$ cusps 均沿用 R1078 的已证 cycle。
这里不将 $\mathcal F_i^*$ 当成角代数 homomorphism。

因 $\deg Z_{\rm ps}=\operatorname{Tr}Z_{\rm ps}=0$，
Lefschetz 公式给
$$
\deg\operatorname{Fix}Z_{\rm ps}=0.
\tag{1087.18}
$$
所以 (1087.17) 本身定义原 $\operatorname{Pic}^0$ 类。

令
$$
u_i=[23y_i-C_\infty]\quad(i=3,4),\qquad
u_y=[23y-C_\infty],
$$
并定义原 Chow–Heegner 型平移类
$$
d_Z(y)=[\operatorname{Fix}Z_{\rm ps}-2Z_{\rm ps}(y)]\in J(\mathbf Q).
\tag{1087.19}
$$
$Z_{\rm ps}(y)$ 已经 degree zero，所以没有隐含的基点调整。

每个原 $R_C$ 将全部 cusp 和送至 $d_C C_\infty$：
Galois 单轨道和 degree 的证明与 R1085 §2.4 相同。
因此 $Z_{\rm ps}C_\infty=0$，并由 (1087.17)–(1087.18) 得准确等式
$$
\boxed{\quad
23\,d_Z(y)=
 \frac12(\mathcal F_4^*Z_{\rm ps})u_4
 +\frac23(\mathcal F_3^*Z_{\rm ps})u_3
 -2Z_{\rm ps}u_y
 \quad\text{于 }J(\mathbf Q)\otimes\mathbf Q.
\quad}
\tag{1087.20}
$$
原 cycle 等式乘六给真正的整系数关系（不只是在模 torsion 的商中）：
$
138\,d_Z(y)=3(\mathcal F_4^*Z_{\rm ps})u_4
 +4(\mathcal F_3^*Z_{\rm ps})u_3-12Z_{\rm ps}u_y.
$

所有 cusp degree 项相消的系数恰为
$\frac12\deg\mathcal F_4^*Z+
 \frac23\deg\mathcal F_3^*Z+23n_Z=\deg\operatorname{Fix}Z=0$；
不是预先将 cusp 类删除。

将 (1087.20) 投至任一 cusp Hecke 部分，最后一项严格消失，得到
$$
23\,e_{\rm cusp}d_Z(y)=
 \frac12e_{\rm cusp}(\mathcal F_4^*Z_{\rm ps})u_4
 +\frac23e_{\rm cusp}(\mathcal F_3^*Z_{\rm ps})u_3.
\tag{1087.21}
$$
这个投影与 $y$ 无关，但不因此等于零。
右边保留两个**原有理 CM 点**以及两个真实角变换；
没有将 $R_Ay_i$ 冒称为一个尚未计算的 scalar 倍。

在 $q=4513$，$y_3,y_4$ 都是普通 CM 点。
[R1085](R1085-original-ordinary-CM-Hecke-logarithm-and-Serre-Tate-moment.md)
因此给右边两个原 $B_q u_i$ 的完整首对数读法。
由于 $B_q$ 与角算子交换，(1087.21) 可直接用于相同来源的
$B_qd_Z(y)$ 首层计算。
它仍不证明右边非零，更不证明所需全局高度 valuation one。

## 5. 原高度条件现在支付到哪里

本篇已经支付：

- 一个原 $\mathbf Q$ 定义、整、对称、无 diagonal component 的实际 $Z_{\rm ps}$；
- 其 Jacobian 非零、degree zero、Hodge trace zero；
- 所有 $4513$ 一次块上 $\vartheta_{\mathfrak m}(Z_{\rm ps})=0$ 的准确特征零条件；
- 两个所选好素上实际整 principal/cusp kernel 分裂；
- 全部 fixed cycle 与两个原 CM 点的准确 Picard 恒等式。

R1074 §9 已支付原八个坏 $47$ tubes 的全部非恒等角支撑避让。
因此本篇的 signed 原组合同样满足那里已证的同盘坏 $47$ Néron 项为零；
不需要另把 signed cycle 改成一个未识别的正对应。

真正剩余是：
$\mathcal F_3^*Z_{\rm ps},\mathcal F_4^*Z_{\rm ps}$ 的实际 cusp 作用、
(1087.21) 的原 CM 类与对数、所需 Mordell–Weil 格、
完整 good-prime 高度及其首项。
如果这些实际投影相消，本篇的谱消去不能挽救这个特定高度方向。
在给出上述数据前，不宣称本篇满足任何盘内排点定理的全部假设。

## 6. 来源与审查边界

- R1078：原角 moduli、composition、fixed divisor、cusps 和 trace 的完整纸证。
- R1081：原 Hodge trace pairing 的 rank-$23$ 证书及完整实际整 Hecke 代数；
  本篇只消费其已完成公开 CI，不重跑。
- R1083：全部 finite types、真实 character fields、$283/4513$ 的准确 local-field 范围。
- P. Mercuri–R. Schoof, *Modular forms invariant under non-split Cartan subgroups*,
  Math. Comp. **89** (2020), 1969–1991，
  [作者 offprint](https://reneschoof.github.io/mcom3503.pdf)，
  Proposition 2.1、Proposition 5.2 及 §6。
  已亲读原文。本文需要的 finite types 已在 R1083 逐类证明；
  中心类和、整下降、迹零、norm 和 fixed-class 关系在本篇给出完整证明。

root 与 o2 已全文独立纸审；root 在 R1083 阶段已亲读上述原文。
本篇没有执行 finite-group 程序，也没有把任何尚未付款的高度
或固定 $47$ 结论外推为 Serre 一致性完成。
