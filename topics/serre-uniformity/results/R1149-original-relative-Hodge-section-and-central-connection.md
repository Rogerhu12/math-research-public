# R1149：原整 moment tower 的相对 Hodge 截面与中央连接槽

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面，所有 $p>37$。** 本篇把 [R1147](R1147-original-canonical-moment-Heisenberg-lift.md) §§8–15 的同一个整 theta tower 实现为 $\mathcal M_{1,1,\mathbb Q_p}$ 上的相对 filtered algebraic connection。原 $43$ 维 affine representation 的 $\operatorname{Fil}^0$ 给一个唯一全局 Hodge 截面。在它确定的标架中，三个中央连接槽及常数 $L_5$ 槽严格为零；水平解的中央变化仍由原 bilinear 群律给出的迭代项控制。

这是有理相对连接的结论。不预设一个相对 strongly divisible lattice、Frobenius 矩阵或 supersingular coarse disk 的整首项；原 Cartan $I$ 仍只作用在模 $p$ quotient。

## 1. 固定同一原对象

令 $\mathcal M=\mathcal M_{1,1,\mathbb Q_p}$，$f:\mathcal E\to\mathcal M$ 为 universal elliptic curve，记
$$
\mathbb H=T_p\mathcal E\otimes\mathbb Q_p,\qquad
\mathbb V=\operatorname{Sym}^4\mathbb H(1)
 \oplus\operatorname{Sym}^8\mathbb H(1)\oplus\mathbb Q_p(5),
$$
$$
\mathbb Z=\mathbb Z_0\oplus\mathbb Z_2\oplus\mathbb Z_4
 =\operatorname{Sym}^{12}\mathbb H(2)
 \oplus\operatorname{Sym}^{8}\mathbb H(4)
 \oplus\operatorname{Sym}^{4}\mathbb H(6).
\tag{1149.1}
$$
$\mathbb V,\mathbb Z$ 的秩分别为 $15,27$。完全保持 R1147 的 contraction 规范，令
$$
\lambda_\infty=\frac{21}{11}(1+p^4),\qquad
\mathfrak b((x,y,t),(x',y',t'))
 =\bigl(\Pi_0(x,y'),\Pi_2(x,y'),
          \Pi_4(x,y')+\lambda_\infty x\otimes t'\bigr).
\tag{1149.2}
$$
原群 $\mathbb G=\mathbb V\oplus\mathbb Z$ 的乘法为
$$
(v,z)(v',z')=(v+v',z+z'+\mathfrak b(v,v')).
\tag{1149.3}
$$
取 R1147 (1147.41) 的实际 $\mathscr P_\infty$，并反除 $p$，得到它的 $\mathbb G$-torsor $\mathscr P_{\mathbb Q_p}$。其 abelian quotient 仍为
$(\mathsf M_{4,\infty},\mathsf M_{8,\infty},\gamma_{5,\infty})$，没有更换 rational lift 或其常数项。

原整格的有理化由
$$
\mathbb W=\mathbb Q_p\oplus\mathbb V\oplus\mathbb Z,\qquad
R(v,z)=
\begin{pmatrix}
1&0&0\\
v&I&0\\
z&\mathfrak b(v,-)&I
\end{pmatrix}
\tag{1149.4}
$$
给出。用原 cocycle $c_\sigma$ 左扭曲 $R(c_\sigma)\rho_{\rm coeff}(\sigma)$，所得 rank-$43$ 局部系记为 $\mathbb W_{\mathscr P}$。保留其原 flag
$$
0\subset\mathbb Z\subset\mathbb K\subset\mathbb W_{\mathscr P},
\qquad
\mathbb K/\mathbb Z=\mathbb V,\quad
\mathbb W_{\mathscr P}/\mathbb K=\mathbb Q_p.
\tag{1149.5}
$$
这里 $\mathbb K$ 是 quotient $s=0$ 的 kernel，通常不是事先分裂的 $\mathbb V\oplus\mathbb Z$。

### 左扭曲与右作用的约定

$R(g)$ 在 affine hyperplane $s=1$ 上是左乘。因而左 cocycle 扭曲后，原未扭群 $\mathbb G$ 在 $\mathscr P_{\mathbb Q_p}$ 上保留的是 **右作用**。在一个局部点平凡化下，
$$
(s,v_0,z_0)\cdot(v,z)
 =\bigl(s,v_0+s v,z_0+s z+\mathfrak b(v_0,v)\bigr).
\tag{1149.6}
$$
这个线性化的右作用与所有 $R(c_\sigma)$ 交换。特别，原 torsor 正是 $\mathbb W_{\mathscr P}$ 中的 hyperplane $s=1$，连同 (1149.6)；这不是仅比较 associated graded 后另造的 affine bundle。

## 2. 已刊相对实现与 fine-level 下降

先拉回 full level $3$ 的 fine moduli scheme $Y(3)$，保留全部 Weil components；在有限扩域包含 $\zeta_3$ 后逐个几何连通 component 讨论。每个 component 都含一个定义在有限 $p$-adic 扩张上的好约化 elliptic point：例如对好模型 $y^2=x^3-x$ 取一个完整 $3$-level basis，并按所需 Weil pairing 选取标记。$p>37$，故该 prime-to-$p$ level 可以在有限未分歧扩张上取得。

R1147 §13 已证明这个点上同一个 $\mathbb W_{\mathscr P}$ 的 fibre crystalline，故 de Rham。Liu–Zhu 的 Theorem 1.3 / Theorem 3.9(iii)–(v) 遂使每个 connected rigid component 上的原局部系成为 de Rham 局部系，并给出保持 tensor、pullback 和 filtration 的相对连接。随后 Diao–Lan–Liu–Zhu 的 Theorem 1.1 与 Lemma 4.1.2 给其相同的代数化：
$$
D=D^{\rm alg}_{\rm dR}:
 \{\text{本处 de Rham 局部系}\}
 \longrightarrow
 \{\text{filtered algebraic bundles with regular integrable connection}\}.
\tag{1149.7}
$$
regular 指在光滑紧化边界具有 regular singularities；本篇先在开 moduli 上使用这个 tensor functor。

### 2.1 这里所需的 exactness 和 strictness

对原 flag、action 和有限 tensor constructions 中的任何短正合列，三个项在每个 classical point 都是 de Rham representations。经典 $D_{\rm dR}$ 在这些 representations 上严格正合；Liu–Zhu Theorem 3.9(ii)–(iii) 保持该 fibre 和其 filtration。

因此相对像列及其各 filtration 列在每个 classical fibre 严格正合。所有 filtration pieces 都是 vector subbundles。逐 affinoid 用 Nakayama，相关 kernels、images 和 cokernels 具有预定秩，得到相对列严格正合；代数化保持这一性质。这是本篇所需的 exact tensor 输入，未把单纯“tensor”一词当作 strict exactness 的替代。

对 $\mathbb H=(R^1f_*\mathbb Q_p)^\vee$，Liu–Zhu Theorem 3.8(v) 的 smooth proper pushforward comparison 与原 dual pairing 给
$$
\mathcal H=D(\mathbb H)
 =\bigl(H^1_{\rm dR}(\mathcal E/\mathcal M)\bigr)^\vee
\tag{1149.8}
$$
及其原 Gauss–Manin connection 和 dual Hodge filtration。因此 (1149.1)–(1149.6) 中的所有 pairing、$\Pi_r$、$\mathfrak b$、flag 与右作用都经同一 functor 运输，Tate factors 亦保留。

### 2.2 下降到原 DM stack

在 $Y(3)\times_{\mathcal M}Y(3)$ 上，两次 pullback 的实际 étale objects 已有满足 cocycle 条件的原 descent isomorphisms。由 pullback/tensor 相容性，它们诱导相同的 filtered connection descent data。代数化的独立紧化性及 regular connection analytification 的 full faithfulness，保证这些仍是代数同构。

故 (1149.7) 的对象、flag 和右作用下降到 $\mathcal M$。这里是沿 fine-level cover 的 faithfully flat descent，不作一个未指定的平均。不同辅助 level 给出同一对象，因为它们在共同 refinement 上按同一 étale source 识别。我们只据此下降到 DM stack；不以此宣称全部 coefficient bundles 已经下降到 coarse $j$-line。

## 3. 唯一相对 Hodge 截面

以下用 $\mathcal V,\mathcal Z,\mathcal K,\mathcal W_{\mathscr P}$ 表示 (1149.1)、(1149.5) 的 $D$-像，用 $\mathbf 1(r)=D(\mathbb Q_p(r))$ 保留 Tate line。由 (1149.8)，$\mathcal H$ 的 filtration jumps 是 $0,-1$。各项最高 filtration jump 为
$$
\begin{array}{c|ccc}
 &\operatorname{Sym}^4\mathcal H(1)&
   \operatorname{Sym}^8\mathcal H(1)&\mathbf1(5)\\ \hline
 \text{最高 jump}&-1&-1&-5
\end{array}
$$
以及
$$
\begin{array}{c|ccc}
 &\mathcal Z_0&\mathcal Z_2&\mathcal Z_4\\ \hline
 \text{最高 jump}&-2&-4&-6.
\end{array}
\tag{1149.9}
$$
特别
$$
\operatorname{Fil}^0\mathcal V
 =\operatorname{Fil}^0\mathcal Z=0,\qquad
\operatorname{Fil}^{-1}\mathcal Z=0,\qquad
\operatorname{Fil}^{-1}\mathbf1(5)=0.
\tag{1149.10}
$$

对 (1149.5) 用 §2.1 的严格正合性，先得
$\operatorname{Fil}^0\mathcal K=0$，再得严格同构
$$
\boxed{\quad
s:\operatorname{Fil}^0\mathcal W_{\mathscr P}
       \xrightarrow{\ \sim\ }\mathcal O_{\mathcal M}.
\quad}
\tag{1149.11}
$$
令 $h_{\rm H}$ 为 $1$ 的唯一逆像。它是原 affine hyperplane $s=1$ 的一个全局代数截面，并按全部 base changes 和 descent data 相容。这个截面由原对象本身确定，不需要选 Coleman primitive、Frobenius point 或 ordinary splitting。

### 3.1 实际 filtered torsor 平凡化

还须证明这个 Hodge 截面给的 torsor 坐标确有原 coefficient filtration。令
$$
\ell_{h_{\rm H}}:\operatorname{Lie}\mathcal G
 =\mathcal V\oplus\mathcal Z\longrightarrow\mathcal K
$$
是 (1149.6) 的右作用在 $h_{\rm H}$ 处的微分。右作用是同一 tensor functor 运输来的 filtered map，而 $h_{\rm H}\in\operatorname{Fil}^0$，故 $\ell_{h_{\rm H}}$ 保持 filtration。

在任意未必 filtered 的局部点平凡化中，写
$h_{\rm H}=(1,v_h,z_h)$，则
$$
\ell_{h_{\rm H}}(v,z)
 =(0,v,z+\mathfrak b(v_h,v)).
\tag{1149.12}
$$
它是底层三角同构。由 (1149.5) 的 strictness，两边每一 filtration piece 的秩都相同；因此 (1149.12) 是严格 filtered 同构。这里第二槽是 $\mathfrak b(v_h,v)$，不能误用左作用的 $\mathfrak b(v,v_h)$。

由于原群律在 $(v,z)$ 中至多 affine-linear，整个 orbit map 正是
$$
h_{\rm H}\cdot(v,z)=h_{\rm H}+\ell_{h_{\rm H}}(v,z).
$$
所以
$$
(s,v,z)\longmapsto s h_{\rm H}+\ell_{h_{\rm H}}(v,z)
\tag{1149.13}
$$
是 $\mathcal O\oplus\mathcal V\oplus\mathcal Z
 \simeq\mathcal W_{\mathscr P}$ 的严格 filtered 同构，保持原 hyperplane 和右 $\mathcal G$-action。由此直接得到实际
$\operatorname{Fil}^0\mathscr P_{\rm dR}=\{h_{\rm H}\}$；
这已支付了 filtered torsor 的同一性，不只计算 filtration 的维数。

## 4. 原 Hodge frame 内的连接矩阵

以 (1149.13) 作为唯一 Hodge frame。令 $\nabla_{\rm coeff}$ 为
$\mathcal O\oplus\mathcal V\oplus\mathcal Z$ 上的原 direct-sum coefficient connection，即由 (1149.8) 的 Gauss–Manin 与 Tate connections 诱导者。设
$$
A=\nabla_{\mathcal W_{\mathscr P}}-\nabla_{\rm coeff}.
$$
这是 $\mathcal O$-linear 的 endomorphism-valued 一形式；两连接保持同一个右作用，所以其差与右作用相容，并且 $sA=0$。

写 $A(e_0)=(0,\alpha,\eta)$。对任意 $g=(v,z)$，右作用将
$e_0=(1,0,0)$ 送到 $(1,v,z)$，因而
$$
A(1,v,z)=(0,\alpha,\eta+\mathfrak b(\alpha,v)).
$$
homogeneity 给完整矩阵
$$
\boxed{\quad
\nabla_{\mathcal W_{\mathscr P}}
 =\nabla_{\rm coeff}+
 \begin{pmatrix}
 0&0&0\\
 \alpha&0&0\\
 \eta&\mathfrak b(\alpha,-)&0
 \end{pmatrix},
\qquad
\alpha\in\mathcal V\otimes\Omega^1_{\mathcal M},\
\eta\in\mathcal Z\otimes\Omega^1_{\mathcal M}.
\quad}
\tag{1149.14}
$$
这也直接核准了左右次序：与右作用相容的 vertical vector field 是右不变的，其矩阵是左 infinitesimal action，故这里是 $\mathfrak b(\alpha,-)$。

对 $h_{\rm H}=e_0\in\operatorname{Fil}^0$ 使用 Griffiths transversality：
$$
\nabla h_{\rm H}\in
 \operatorname{Fil}^{-1}\mathcal W_{\mathscr P}
       \otimes\Omega^1_{\mathcal M}.
$$
结合严格 filtered 同构 (1149.13) 和 (1149.10)，得到
$$
\boxed{\quad
\eta=0,\qquad
\alpha=(\alpha_4,\alpha_8,0).
\quad}
\tag{1149.15}
$$
令 $\mathcal F=\operatorname{Fil}^0\mathcal H$，则还准确有
$$
\alpha_4\in
 \mathcal F^{\otimes4}\otimes\mathbf1(1)\otimes\Omega^1_{\mathcal M},
\qquad
\alpha_8\in
 \mathcal F^{\otimes8}\otimes\mathbf1(1)\otimes\Omega^1_{\mathcal M}.
\tag{1149.16}
$$

(1149.15) 是 **同一实际相对 torsor 在唯一 Hodge frame 内** 的精确连接约束。这里 $\operatorname{Lie}\mathcal G=\mathcal V\oplus\mathcal Z$ 是原 coefficient category 中的真实直和；所以中央项为零并非一个 associated-graded 结论。

## 5. 中央变化仍有原迭代项

写 affine hyperplane 内一个水平局部解的坐标为
$(1,x,y,t,z_0,z_2,z_4)$。固定 (1149.14) 的加号 convention，则其水平方程为
$$
\begin{aligned}
\nabla x&=-\alpha_4,&
\nabla y&=-\alpha_8,&
\nabla t&=0,\\
\nabla z_0&=-\Pi_0(\alpha_4,y),&
\nabla z_2&=-\Pi_2(\alpha_4,y),\\
\nabla z_4&=-\Pi_4(\alpha_4,y)-\lambda_\infty\alpha_4\otimes t.
\end{aligned}
\tag{1149.17}
$$
$\nabla t=0$ 是相对 Tate coefficient connection 的方程；它不把原算术类 $\gamma_{5,\infty}$ 设为零。最后三式保留了真正 class-two 迭代项及高层常数 $\lambda_\infty$。

例如在统一记号 $v=(x,y,t)$、$z=(z_0,z_2,z_4)$ 下，换成对称中央坐标
$\widetilde z=z-\mathfrak b(v,v)/2$，则
$$
\nabla\widetilde z
 =\frac12\bigl(\mathfrak b(v,\alpha)-\mathfrak b(\alpha,v)\bigr).
\tag{1149.18}
$$
因此 (1149.15) 不表示中央函数恒定，也不表示在任意 flat/crystalline frame 中中央连接系数都为零。改变截面产生的 bilinear 项正是下一步实际比较必须保留的部分。

## 6. 同源性与使用范围

本篇的 $\mathcal W_{\mathscr P}$ 由 R1147 的原 stable lattice 有理化后，经已刊 tensor functor 得到；(1149.11)–(1149.18) 没有另选一个具有相同 graded pieces 的 extension。对好约化点 pullback，Liu–Zhu 的 fibre compatibility 恢复 R1147 §13 的同一 $D_{\rm dR}(W_E)$。在未分歧底上，R1147 §14 的 Fontaine–Laffaille 格和模 $p$ quotient 仍是原给定格与 quotient。

但这里尚未构造与 (1149.13) 同时整相容的相对 strongly divisible module，也未计算 Frobenius-invariant point 相对 $h_{\rm H}$ 的坐标。因此下一步须在同一来源中明确 $\alpha_4,\alpha_8$ 的实际归一、比较 Frobenius 与 Hodge 截面，并控制原 supersingular deformation 的整误差和 coarse 阶数。

最后的 Cartan map 仍按 R1147 §11 先约模 $p$ 再取 $q_I$。本篇没有把
$I\in\operatorname{End}(\mathcal E[p])$ 提升到
$\operatorname{End}(T_p\mathcal E)$，也没有把 (1149.17) 直接当作原三条 Tate 线 Heisenberg covering 的有理相对方程。上述限制不影响本篇已证的 canonical Hodge section 与中央连接槽约束。

## 7. 已刊 primary 与精确消费点

1. R. Liu、X. Zhu，*Rigidity and a Riemann–Hilbert correspondence for p-adic local systems*，**Inventiones Mathematicae 207 (2017), 291–343**，[作者全文](https://arxiv.org/pdf/1602.06282)，[DOI](https://doi.org/10.1007/s00222-016-0671-7)。Theorem 1.3 给 one-point de Rham rigidity；Theorem 3.8(v) 给 smooth proper pushforward compatibility；Theorem 3.9(ii)–(v) 给 pullback、subbundle filtration、Griffiths 与 tensor。作者版 Theorem 3.8 在第23页，Theorem 3.9 跨第24–25页。本篇在 §2.1 另证所需 strict exactness。
2. H. Diao、K.-W. Lan、R. Liu、X. Zhu，*Logarithmic Riemann–Hilbert correspondences for rigid varieties*，**Journal of the AMS 36 (2023), 483–562**，[作者全文](https://arxiv.org/pdf/1803.05786)，[DOI](https://doi.org/10.1090/jams/1002)。Theorem 1.1 与 §4.1、Lemma 4.1.2 给相同 filtered connection 的代数化、tensor 与独立紧化性；作者版第3、46–47页。这里使用开曲线上的 $D^{\rm alg}_{\rm dR}$，不把一般 log extension functor 误称 tensor。
3. [R1147](R1147-original-canonical-moment-Heisenberg-lift.md) §§8–15：原 theta 的全部有序 primitive 矩、精确兼容 tower、$\lambda_\infty$、同一 rank-$43$ affine lattice 与好点 crystalline 比较。它们是本篇的实际输入，未被有理 polylog substitute 替换。

无数学程序执行；未更改既成数值输入、Actions 请求或固定 $47$ 结论。一般 $p$ 的原 $p$-local 非交换标量仍须实际计算。


## 8. 同一 Hodge 截面延到 nilpotent log extension

令 $\overline{\mathcal M}=\overline{\mathcal M}_{1,1,\mathbb Q_p}$，$C$ 为 cusp divisor。本节只延伸同一有理 filtered connection。

在 fine level $3$ 的每个 cusp，原 $\mathbb H$ 的 geometric monodromy 为 Tate 的 unipotent matrix。$\mathbb W_{\mathscr P}$ 保留 (1149.5)，其 diagonal blocks 为 $\mathbb Q_p,\mathbb V,\mathbb Z$，故整个 geometric monodromy 的全部 eigenvalues 都为一。这个结论不要求中央 cocycle 的 cusp 值为零。

Diao–Lan–Liu–Zhu Theorem 3.2.12(2) 因而在这里给真正的 **tensor** log de Rham functor，原连接有 nilpotent residues。其 algebraization 与 §2 相同。不同 fine charts 的 extension 沿原 descent data 识别：nilpotent Deligne extension 唯一，且该文 Corollary 3.5.7 的 pullback compatibility 在本处全部 unipotent 的情形适用。由此得到 $\overline{\mathcal M}$ 上同一 flag 和右作用的 filtered log extension，记为
$\overline{\mathcal W}_{\mathscr P}$、$\overline{\mathcal H}$ 等。

还须付 boundary strictness。取 cusp 的一个 local parameter $z$。Theorem 4.3.2 / Corollary 4.3.4 将 log fibre 的 filtered nearby-cycle realization 与实际 tangential $G_{k(c)}$-representation 的 $D_{\rm dR}$ 同一。因为 residues 全 nilpotent，$\operatorname{gr}^0_V$ 就是该 log lattice 模 $z$ 的 fibre。此处 étale nearby cycle 是原 generic fibre representation 沿参数给出的 Galois section 作 restriction，因而对原 flag 正合。经典 $D_{\rm dR}$ 的严格正合性于是支付 boundary fibre 的严格正合；结合 §2.1 的 interior 结论和 subbundle 性质，整条 compact fine curve 上的 flag 都严格正合。

这些 boundary representations 的 graded Hodge weights 仍是 (1149.9)。故 (1149.11) 延为
$$
s:\operatorname{Fil}^0\overline{\mathcal W}_{\mathscr P}
 \xrightarrow{\ \sim\ }\mathcal O_{\overline{\mathcal M}}.
\tag{1149.19}
$$
其逆像 $\overline h_{\rm H}$ 延伸原 $h_{\rm H}$。§§3–4 的 right-action 证明逐字适用，只把 $\Omega^1$ 换为 $\Omega^1(\log C)$。特别
$$
\alpha_d\in
H^0\!\left(\overline{\mathcal M},
 \overline{\mathcal F}^{\otimes d}\otimes\mathbf1(1)
 \otimes\Omega^1_{\overline{\mathcal M}}(\log C)\right),
\qquad d=4,8.
\tag{1149.20}
$$
这一步排除了 Hodge frame 在 cusp 额外产生的 pole；不能仅从连接 regular singular 得出 (1149.20)。

## 9. 最高 Hodge 线、Tate 正号与原留数

### 9.1 固定所有微分与 Tate frame

记 $\omega_{\rm Hod}$ 为 Hodge line。固定 de Rham Tate generator
$\tau_1=\zeta_{p^\infty}/t_{\rm per}$，其中
$t_{\rm per}=\log[\zeta_{p^\infty}]$；同时改变 compatible roots 时两者按同一单位改变，故 $\tau_1$ 不变。principal polarization 与 de Rham cup pairing 将一个 invariant differential $\omega$ 线性送到
$$
\nu(\omega)\in\overline{\mathcal F}
 =\operatorname{Fil}^0\overline{\mathcal H}.
$$
具体是以 $\tau_1$ 收缩 $\omega\cup(-)$ 得到的 dual functional；它杀掉 $\omega$ 自身。按 Tate 正号取该识别，在原 cusp 的 coinvariant 中
$$
\nu(dv/v)\longmapsto e_1,\qquad
e_1=q^{1/p^\infty},\quad e_2=\zeta_{p^\infty}.
\tag{1149.21}
$$
这里的单位确为一：$dv/v$ 在 multiplicative cycle 上的 normalized period 是一，原 principal pairing 的两 Tate cycles determinant 也是一。若反用相反的 symplectic orientation，两边只差整体负号；本节 $d=4,8$，其 $d$ 次幂不变。没有其它 period 单位可吸收。

保持原 Kodaira–Spencer 规范。对短模型
$$
E:\ y^2=x^3+A x+B,\qquad \omega=dx/(2y),
$$
[R1091](R1091-original-Gaussian-CM-logarithm-as-one-algebraic-coefficient.md) §1 的通用 de Rham 计算给
$$
K_\omega:=\operatorname{KS}(\omega^{\otimes2})
 =\frac{9B\,dA-6A\,dB}{2(4A^3+27B^2)}.
\tag{1149.22}
$$
这是 universal identity，不使用 R1091 的固定 $47$ 或 $4513$ 数值输入。代原 Tate 模型
$$
A=-E_4(q)/48,\qquad B=E_6(q)/864,\qquad
\omega=dv/v
$$
恰得 $K_\omega=dq/q$。

因此
$\nu(\omega)^d\tau_1K_\omega$ 是 (1149.20) 的同一局部 frame，换 $\omega\mapsto u\omega$ 时乘 $u^{d+2}$。它把该空间准确识别为 weight-$d+2$ 模形式空间，常 Tate line 按上述 $\tau_1$ 固定。

### 9.2 原 cocycle 的 residue，没有阶乘或宽度遗漏

令 $u$ 是与 R1147 相同的 positive geometric generator：
$$
u(e_1)=e_1+e_2,\qquad u(e_2)=e_2.
$$
实际 $(\mathbb Q_p,\operatorname{Sym}^d\mathbb H(1))$ extension 的 cocycle 满足
$$
[c_d(u)]_{\rm coinv}
 =v_d^\infty e_1^d\otimes\zeta_{p^\infty},
\qquad
v_d^\infty=(1-p^d)\frac{B_{d+2}}{d+2}.
\tag{1149.23}
$$
这是 R1147 (1147.32)、(1147.35) 的原全部有序 primitive 点式；本篇没有重取 moment、改成 divided powers 或再除一个 factorial。

该文 log comparison 的 Lemma 3.4.7 给 **正号**
$$
\operatorname{Res}(\nabla)=t_{\rm per}^{-1}\log(u),
\tag{1149.24}
$$
其中作者的 geometric generator 同样将所选根乘 $\zeta$。在这个 extension 上，
$\log(u)e_0$ 的首项是 $c_d(u)$，其余各项都属于
$(u-1)\operatorname{Sym}^d\mathbb H(1)$，故在 coinvariant 中消失。将 $e_0$ 换为唯一 Hodge 截面也只增加 coefficient monodromy 的像，不改变这一 coinvariant。

(1149.20) 将 residue 放在
$\overline{\mathcal F}^{\otimes d}(1)$；由 (1149.21)，这条线到 coinvariant 是以一为尺度的同构。因此
$$
\operatorname{Res}_{q=0}\alpha_d
 =v_d^\infty\,\nu(dv/v)^d\tau_1.
\tag{1149.25}
$$
若先在 fine cusp 参数 $z$ 上读，$q=z^w$，其 monodromy 是 $u^w$，而 $dq/q=w\,dz/z$。两边同时乘 cusp width $w$，下降后仍为 (1149.25)；没有额外的 $3$ 或其它 level 因子。更换有相同一阶 tangent 的 local coordinate 也不改 residue。

## 10. 两条实际连接形式的完整归一

在 $\mathbb Q_p$ 上，compact moduli 的短 Weierstrass presentation 是 weighted stack
$[(\mathbb A^2-\{0\})/\mathbb G_m]$，$A,B$ 的 weights 为 $4,6$。regular homogeneous functions 从 $\mathbb A^2-\{0\}$ 延至 $\mathbb A^2$，因为后者正规且所删点 codimension 二。因此 weight $6$ 的全局空间只有 $B$ 一维，weight $10$ 的全局空间只有 $AB$ 一维。这是 characteristic-zero 线束截面的直接计算，没有将一个有理维数结论约模 $p$。

以同一 Tate frame 归一的 forms 为
$$
E_6(E,\omega)=864B,\qquad
E_{10}(E,\omega)=E_4E_6=-41472AB;
$$
二者在 $\omega=dv/v$ 的 Tate $q$-expansion 常数项都是一。由 (1149.20) 与 (1149.25)，得到同一实际 Hodge connection 的精确恒等式
$$
\boxed{\begin{aligned}
\alpha_4
 &=\frac{1-p^4}{252}\,
   E_6(E,\omega)\,\nu(\omega)^4\tau_1K_\omega,\\
\alpha_8
 &=\frac{1-p^8}{132}\,
   E_{10}(E,\omega)\,\nu(\omega)^8\tau_1K_\omega.
\end{aligned}}
\tag{1149.26}
$$
两边在 $\omega$ 的缩放下相同，故这是真正全局式。也可写成
$$
\begin{aligned}
\alpha_4
 &=\frac{24}{7}(1-p^4)B\,
       \nu(\omega)^4\tau_1K_\omega,\\
\alpha_8
 &=-\frac{3456}{11}(1-p^8)AB\,
       \nu(\omega)^8\tau_1K_\omega,
\end{aligned}
\tag{1149.27}
$$
以及保持全部 tensor factors 的相容式
$$
\alpha_8
 =\lambda_\infty E_4(E,\omega)\,
       \nu(\omega)^4\otimes\alpha_4.
\tag{1149.28}
$$
R1147 的高层修正 $(1+p^4)$ 正是 (1149.28) 的实际比例；并未在有理化时丢失。

将 (1149.26) 代入 (1149.14)、(1149.17)，现在得到原 rank-$43$ rational connection 的完整显式输入，包括原 $\Pi_0,\Pi_2,\Pi_4$ 和 $\lambda_\infty$。这里只用原局部系的 log/Hodge 实现、实际 residue 与低权 line-bundle 计算，没有以一个另选 Eisenstein extension 替换原 tower。

这些式子的係数在 $p>37$ 时都是 $p$ 整的。但“有一组 $p$ 整的有理连接公式”本身仍不等于已付的同源相对 strongly divisible lattice 或 Frobenius structure。特别在 $A=0$ 的 fine cubic point，$E_{10}$ 的零不能直接作为原 coarse $p$-Kummer 中央标量的首项；还须保原 $q_I$、comparison 与 coarse 三阶运输。

新增 primary 的确切位置均在上引已刊 DLLZ 论文：Theorem 3.2.12(2)（作者版第27页）、Lemma 3.4.7 / Remark 3.4.8（第35页）、Corollary 3.5.7（第39–40页）、Theorem 4.3.2 / Corollary 4.3.4（第51页）。它们分别支付这里特定 unipotent 情形的 tensor log extension、正 monodromy residue、pullback 和 filtered tangential fibre；原 $v_d^\infty$ 来源仍是 R1147 自证的全部 primitive theta 计算。
