# R1150：原 class-two moment tower 的相对对数 Frobenius 与同源识别

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面，所有 $p>37$。** 本篇使用 [R1147](R1147-original-canonical-moment-Heisenberg-lift.md) 的同一整 tower 及 [R1149](R1149-original-relative-Hodge-section-and-central-connection.md) 的同一 Hodge connection。所有系数先反除 $p$，$p>37$。

目标是支付 R1149 §12 所明确保留的**相对 rational associatedness**。证明按实际 Frobenius 矩阵进行：先构造两条原 abelian Frobenius，用完整 Tate 算术常数计算中央微分的留数，再构造中央 Frobenius。随后在带全部尖点的 proper fine model 上作同源识别，才回到原开 moduli。不能以好约化 tube 的上同调代替原全曲线的上同调。

## 1. 固定原对象与 Frobenius 约定

沿用 R1149 的
$$
V=\operatorname{Sym}^4H(1)\oplus\operatorname{Sym}^8H(1)
  \oplus\mathbf1(5),\qquad
Z=\operatorname{Sym}^{12}H(2)\oplus
  \operatorname{Sym}^8H(4)\oplus\operatorname{Sym}^4H(6).
$$
$G=V\oplus Z$ 的原群律为
$$
(v,z)(v',z')=(v+v',z+z'+b(v,v')),
$$
$$
b((x,y,t),(x',y',t'))=
(\Pi_0(x,y'),\Pi_2(x,y'),\Pi_4(x,y')+\lambda_\infty x t'),
\quad
\lambda_\infty=\frac{21}{11}(1+p^4).
\tag{1150.1}
$$
所有 $\Pi_r$ 与 Tate factors 均保持 R1147 的原规范。

在唯一 Hodge frame 中，原 rank-$43$ connection 为
$$
\nabla=\nabla_{\rm coeff}+R_*(\alpha,0),\qquad
\alpha=(\alpha_4,\alpha_8,0),
$$
$$
\alpha_d=v_d^\infty E_{d+2}\nu^d\tau_1\,{\rm KS},
\quad
v_4^\infty=\frac{1-p^4}{252},\quad
v_8^\infty=\frac{1-p^8}{132},\quad
v_8^\infty=\lambda_\infty v_4^\infty .
\tag{1150.2}
$$
这些是 R1149 已付的完整代数 log forms，中央 Hodge connection 槽为零。

记原 geometric coefficient crystal 的 Frobenius 为 $\Phi_{\rm coeff}$。
在一个 Frobenius lift $\phi$ 上记
$$
\alpha'=\Phi_{\rm coeff}\phi^*\alpha.
$$
写待求完整 Frobenius 为
$$
\Phi=R(u_V,u_Z)\Phi_{\rm coeff}.
\tag{1150.3}
$$
由 R1149 的完整矩阵直接相乘，水平性等价于
$$
\boxed{\quad
\nabla_{\rm coeff}u_V=\alpha'-\alpha,\qquad
\nabla_{\rm coeff}u_Z
=b(u_V,\alpha')-b(\alpha,u_V)=:\delta .
\quad}
\tag{1150.4}
$$
次序由原左 cocycle/右 torsor 约定固定。第二式不是只取其反对称化；全部原 bilinear 项都保留。

## 2. 所消费的已刊相对比较及扩张方向

这里使用的比较输入是 Faltings 的已刊
*Crystalline cohomology and p-adic Galois-representations*，
§5、Lemma 5.5：在光滑 proper 模型及相对 normal-crossing 水平边界的 log 情形，associated crystalline 局部系到 filtered convergent $F$-isocrystals 的 functor 严格正合、全忠实，其**在 filtered $F$-isocrystal 一侧的 essential image 对严格扩张封闭**。系数为 $\mathbb Q_p$，并保留 log connection。使用的方向不是“两个 crystalline étale representations 的任意 étale 扩张仍 crystalline”。

为明确这个输入在本处支付什么，给出实际扩张论证。设 $E_1,E_2$ 已分别 associated 于 $L_1,L_2$，并有 filtered convergent $F$-isocrystals 的严格扩张 $E$。在一个 log chart 选 filtered splitting，其差由
$$
x\in{\rm Fil}^{-1}\operatorname{Hom}(E_2,E_1)\otimes\Omega^1(\log),
\quad
y\in\operatorname{Hom}(E_2,E_1)
$$
表示；水平性正是相应的
$\nabla y=(1-\Phi)x$，高维时另有 $\nabla x=0$。
不是先把这个扩张投影到某个尚未证明单射的 $H^2_{\rm syn}$。

对 $\operatorname{Hom}(E_2,E_1)$ 用已给的**水平** associatedness。为免混同两种文献记号，记有结构连接的 period algebra 为
$\mathcal O\mathbb B_{\log,\mathrm{cris}}$，其 horizontal 子环记为
$\mathbb B_{\log,\mathrm{cris}}$。内点即通常的 $\mathcal O\mathbb B_{\mathrm{cris}}$ 与 $\mathbb B_{\mathrm{cris}}$。
所用的是整个 filtered log de Rham mapping fiber
$$
\operatorname{Fib}\left(
 \operatorname{Fil}^0\bigl(
 \mathcal O\mathbb B_{\log,\mathrm{cris}}\otimes\Omega^\bullet(\log)\bigr)
 \xrightarrow{\,1-\varphi\,}
 \mathcal O\mathbb B_{\log,\mathrm{cris}}\otimes\Omega^\bullet(\log)
 \right),
\tag{1150.5}
$$
其中 $q$ 次项的 period filtration 是 $\operatorname{Fil}^{-q}$。
filtered log PD Poincaré resolution 与 horizontal period 的 fundamental sequence
$0\to\mathbb Q_p\to\operatorname{Fil}^0\mathbb B_{\log,\mathrm{cris}}
\xrightarrow{1-\varphi}\mathbb B_{\log,\mathrm{cris}}\to0$
使 (1150.5) resolution $\mathbb Q_p$。在 smooth 内点，这分别是 Tan–Tong Corollary 2.17 与 Theorem 3.18 证明中写出的两个输入；log chart 使用 Faltings 的同一 log PD construction。

tensor 上 $\operatorname{Hom}(L_2,L_1)$ 后，$(x,y)$ 在该复形中 locally 是
$(\nabla a,(1-\Phi)a)$，其中
$$
a\in\operatorname{Fil}^0\left(
 \mathcal O\mathbb B_{\log,\mathrm{cris}}\otimes
 \operatorname{Hom}(E_2,E_1)\right).
$$
于是 triangular change of splitting by $a$ 同时消去 connection 与 Frobenius 的 extension slots，并严格保持 filtration。换回后得到实际的
$$
\mathcal O\mathbb B_{\log,\mathrm{cris}}\otimes E
 \ \simeq\
\mathcal O\mathbb B_{\log,\mathrm{cris}}\otimes_{\mathbb Q_p}L
$$
**filtered、horizontal、Frobenius-compatible** 同构。其水平且 Frobenius-fixed 的 $\operatorname{Fil}^0$ 部分为同秩 $\mathbb Q_p$ 局部系；Galois cocycle 是 $g(a)-a$（符号随 splitting 同时改变）。它的连续性来自 period algebra 的连续作用及有限个 period coefficients。这个 triangular 同构也给所有 filtration graded 上的同构，不只是一个 fibrewise filtered vector-space identification。

log chart 的 PD 坐标使 $d\log q$ 的 primitive 成为相应对数 period，其 Galois 变化保留实际 Kummer 惯性。Faltings 的 proper-log realization 把这些局部 representations 下降为全部 $X_K\setminus D_K$ 上的 étale 局部系；这里只在完成的 good open 构造表示并不足够。内外 chart 的同构由同一 horizontal fixed-space construction 粘合，degree zero 给全忠实性。故 tensor contractions、flag、action 和 pullback 沿这一个比较运输。

特别，**不把 Tan–Tong Proposition 3.21 单独当作保持 connection 的结论**：它对 Faltings 弱 associatedness 的陈述只给 filtration/Frobenius 同构。这里的水平性由上面的显式方程 $\nabla a=x$ 及整个 $\mathcal O\mathbb B_{\log,\mathrm{cris}}$ gauge 另行支付。内点随后适用其 Definition 3.10 / Proposition 3.22，经 $\mathcal O\mathbb B_{\mathrm{cris}}\to\mathcal O\mathbb B_{\mathrm{dR}}$ 得到同一 filtered connection 的 de Rham comparison。

本处最初的 associated objects 是原 universal elliptic geometric coefficient 及 Tate lines：smooth 内点由 proper smooth $H^1$ 比较，cusp 由实际 Tate log basis 和 Kummer period 给出；dual、symmetric powers 与 tensor 均保持这个水平比较。本篇不借未刊的逐点 crystalline 判据，也不把 Bannai–Kings 定义中的“admissible”一词直接解释成 associatedness。

## 3. 三个小权的实际 rigid cohomology

令 $\mathcal M=\mathcal M_{1,1,\mathbb Q_p}$。
对于 $d=4,8,12$，同一 coefficient $H$ 有
$$
H^0_{\rm rig}(\mathcal M_{\mathbb F_p},\operatorname{Sym}^dH(t))=0,
$$
$$
\boxed{\quad
{\rm res}:H^1_{\rm rig}(\mathcal M_{\mathbb F_p},
        \operatorname{Sym}^dH(t))
 \xrightarrow{\sim}\mathbb Q_p(t-1).
\quad}
\tag{1150.6}
$$
右边的 Frobenius 是 $p^{1-t}$。

这些式子不需要待构造的 rank-$43$ comparison。只对原 geometric coefficient 使用 rigid/de Rham comparison。Bannai–Kings Remark 2.5 与 §2 的 residue maps 在 prime-to-$p$ fine level 给相同的比较；再取 full level-$3$ descent 的不变量。de Rham 维数则由 characteristic-zero 的同一
$\operatorname{PSL}_2(\mathbb Z)=C_2*C_3$
复形直接计算：三个正次数的 invariants 交为零，两个 cyclic invariant ranks 为 $(3,1),(5,3),(7,5)$，所以 $H^1$ 都是一维。R1147 的原 moment residue 非零，因而 residue map 在这条线是同构。这里也可用 $S_6=S_{10}=S_{14}=0$ 读取同一计算。

Frobenius 的尺度可在真正 Tate chart 核准。用 log de Rham basis $f_1,f_2$ 使
$$
Nf_1=f_2,\quad Nf_2=0,\quad
\Phi f_1=f_1,\quad \Phi f_2=p^{-1}f_2,\quad
\Phi\tau_1=p^{-1}\tau_1,\quad\phi(q)=q^p.
\tag{1150.7}
$$
$\nu(0)=f_1$，$f_2$ 是 multiplicative Tate line 的原 generator。
$\operatorname{Sym}^dH(t)$ 的 monodromy coinvariant 由
$f_1^d\tau_1^t$ 生成；$dq/q$ 的 pullback 乘 $p$，故 residue Frobenius 为 $p^{1-t}$。这里没有把 coefficient Frobenius 与一形式 Frobenius 混在一起。

在 affine tame stack 上，相关 coherent bundles 没有高次 coherent cohomology；可在 weighted Weierstrass presentation 中取 $\mathbb G_m$ 不变量，或经 tame coarse map 验证。因此 (1150.6) 中一个 exact 的全局一形式有全局 overconvergent primitive。其唯一性来自 $H^0=0$。

## 4. 两条实际 abelian Frobenius 的存在及 log 延拓

先处理 $d=4,8$。由 (1150.6)，twist $t=1$ 的 $H^1$ 上 Frobenius 是一。故
$$
[\alpha_d'-\alpha_d]=0,
$$
从而有唯一 overconvergent section $u_d$ 满足
$$
\nabla u_d=\alpha_d'-\alpha_d.
\tag{1150.8}
$$
可在 completed weighted affine chart 用
$A\mapsto A^p,\ B\mapsto B^p$；判别式的像模 $p$ 为原判别式的 $p$ 次幂，故在相应 weak completion 上可逆。更换 lift 时使用 coefficient connection 的 Taylor isomorphism，所写式子随之运输；唯一性使它们相容。

须另证尖点处的正则性。在与 Tate chart 相交的 overconvergent annulus 上，把 $u_d$ 写成 Laurent 级数。取 (1150.7) 的 log basis 后，右边 $\alpha_d'-\alpha_d$ 只有非负 $q$ 次项，且常数 residue 为零。若 $n<0$，则
$$
(n+N)(u_d)_n=0.
$$
$N$ 幂零，$n\ne0$，所以 $n+N$ 在 $\mathbb Q_p$ 上可逆，所有负次项都为零。剩余级数在整个 $|q|<1$ 上收敛，并满足
$$
Nu_d(0)=0,\qquad
u_d(0)=a_{d+1} f_2^d\tau_1
\tag{1150.9}
$$
对某个真正的常数 $a_{d+1}$。这证明 log regularity，不是仅从 regular-singular connection 猜测 Frobenius 无 pole。

于是 $(1\oplus\operatorname{Sym}^dH(1),\nabla,R(u_d)\Phi_{\rm coeff})$
成为 log filtered $F$-isocrystal。其 filtration 是同一 Hodge splitting，且扩张严格；Griffiths 由 $\alpha_d\in{\rm Fil}^{-1}$ 保证。
其 log convergence 也直接可核：连接的 Taylor 解先在某个正半径收敛；Frobenius 迭代把任意严格小于一的 diagonal tube 送进该半径，horizontal invertible Frobenius 再把 Taylor isomorphism 拉回。log chart 中对 ratio $1+z$ 使用 $(1+z)^p-1$ 的同一收缩；幂零 residue 的指数为有限矩阵指数。这给 convergent log stratification，而非只有一个形式微分方程。

在带全部 cusp 的 proper level-$3$ model 上用 §2，得到全开曲线上的 associated étale extension。其 descent data 由唯一性及全忠实性运输。回到原 level one，其 residue 是原 $v_d^\infty$。R1147 的完整 integral geometric cohomology 取极限、反除 $p$ 后，Hochschild–Serre 给
$$
H^1_{\rm et}(\mathcal M,\operatorname{Sym}^d\mathbb H(1))
 \xrightarrow{\ {\rm res}\ }\mathbb Q_p
\quad\text{为同构}.
\tag{1150.10}
$$
因此这个 associated extension 就是原
$\mathsf M_{d,\infty}\otimes\mathbb Q_p$。
这里只用 residue 唯一性于**全原 $\mathcal M$**；proper-log realization 已先支付。

## 5. 原 Tate arithmetic constant 使 $a_5=u_5$

令原 $\gamma_{5,\infty}$ 的 crystalline extension，在同一唯一 Hodge splitting 内写成
$$
\Phi_{\gamma_5}(e_0)=e_0+u_5\tau_1^5,\qquad
\Phi_{\gamma_5}(\tau_1^5)=p^{-5}\tau_1^5 .
\tag{1150.11}
$$
$u_5\in\mathbb Q_p$ 是原类的真实参数；不把它设为零或单位。
这个常数 extension crystalline 已由 R1147 §13 支付。

现在在 Tate tangent $q=0$ 取固定所有 $q$-roots 的原 arithmetic section。R1147 (1147.34)–(1147.35) 对全 primitive 轨道及真实 phase/transfer 的计算说明，原 $\mathsf M_{d,\infty}$ 的 tangential arithmetic class 精确为
$\gamma_{d+1,\infty} f_2^d$，保留原 Tate factor。

这里从有限层到 rational arithmetic class 的箭头可明确检查。限制到 cyclotomic kernel
$H=\ker\chi_{\rm cyc}$ 时，每个有限层都在 R1147 的 $G_{K_n}$ 范围内，所有已合并的 nonzero-$a$ 轨道和 phase 项逐层为零；故极限只留下同一圆单位类。另一方面 tangential coefficient 分解为
$\bigoplus_{j=0}^d\mathbb Q_p(j+1)$。
cyclotomic quotient 上这每条非零权线的 $H^1$ 都为零：一个开 procyclic generator 的 $\chi^{j+1}-1$ 在 $\mathbb Q_p$ 中可逆，有限部分可平均。因此 restriction 到 $H$ 在总次数一单射。所得 rational arithmetic 身份不是从变化有限域的 restriction 单独猜出的。

§4 已把 abelian crystal 与原 étale extension 识别。log comparison 对这个原 tangential fibre 的 pullback 保持 filtration、Frobenius 和 Tate generators；其对数 residue $N$ 另外保留，取 arithmetic section 时不把它当成额外 Galois cocycle。因为所有 coefficient filtration weights 都负，$\operatorname{Fil}^0$ 中映到一的 lift 唯一，双方没有可再吸收的 Hodge-frame 平移。$f_2^4\tau_1=\tau_1^5$ 的原 identification 给
$$
\boxed{\qquad a_5=u_5.\qquad}
\tag{1150.12}
$$
$a_9$ 则来自原 $\gamma_{9,\infty}$；下节的 residue 消去不需要假定其非零。

## 6. 三个中央 residue 的完整消去

取
$$
u_V=(u_4,u_8,u_5),\qquad
\delta=b(u_V,\alpha')-b(\alpha,u_V).
$$
它是原 $Z$-valued overconvergent log 一形式。曲线上的 closedness 自动成立。
由 §§4–5，在 cusp 有
$$
u_4(0)=a_5 f_2^4\tau_1,\quad
u_8(0)=a_9 f_2^8\tau_1,\quad
{\rm res}(\alpha_d')={\rm res}(\alpha_d)
=v_d^\infty f_1^d\tau_1.
$$
对 $\Pi_0$ 槽，两个 mixed monomials 都含 $f_2$，故在 monodromy coinvariant 中为零。
对 $\Pi_2$ 槽也一样：原 contractions 后分别仍含 $f_2^2$ 或 $f_2^6$。

最后 $\Pi_4(f_2^4,f_1^8)=f_1^4\tau_1^4$，尺度恰为一，因为原纯幂 contraction 是四次 Weil pairing；$\Pi_4(f_1^4,f_2^8)$ 则仍含 $f_2^4$，不贡献 coinvariant。
$\alpha_5=\alpha_5'=0$，但原 $+\lambda_\infty x t'$ 项贡献
$-\lambda_\infty v_4^\infty u_5$，不能删除。因此
$$
\boxed{\quad
{\rm res}_{\rm coinv}(\delta)
=\left(0,0,\,
 v_8^\infty a_5-\lambda_\infty v_4^\infty u_5\right)
=\left(0,0,v_8^\infty(a_5-u_5)\right)=0.
\quad}
\tag{1150.13}
$$
这一步同时用原高层比例 $1+p^4$ 与原 arithmetic circular-unit constant；只看 mod-$p$ 的 $21/11$ 不足以得到本篇 rational identity。

由 (1150.6)，$\delta$ 在 $H^1_{\rm rig}(Z)$ 中为零，于是存在唯一全局 overconvergent $u_Z$ 满足
$$
\nabla u_Z=\delta.
\tag{1150.14}
$$
在每个 cusp，负次 Laurent 项再次被 $(n+N)^{-1}$ 消去；常数 residue 已在 monodromy 像中，故 $u_Z$ 正则。由 (1150.4)，(1150.3) 是原整个 rank-$43$ connection 的 horizontal invertible Frobenius。

不同 Frobenius lifts 的结果经同一原 connection 的 Taylor map 识别：abelian 部分是 §§4–5 的同一对象，中央差是一个 horizontal $Z$ section，而 $H^0_{\rm rig}(Z)=0$。故这一 Frobenius structure 真正下降，并非只在一个选定 affine chart 上写了矩阵。
同样的 Frobenius 收缩论证给其 convergent log stratification。

## 7. 全原 tower 的识别及已支付范围

把 (1150.3) 与 R1149 的原 split Hodge filtration 合并。
完整 $\nabla$ 满足 Griffiths，原 flag
$$
0\subset Z\subset K\subset W,\qquad K/Z=V,\quad W/K=\mathbf1
$$
严格。首先 $K$ 是已 associated coefficient objects 的严格扩张；然后 $W$ 是 $\mathbf1$ by $K$ 的严格扩张。因此 §2 在 proper fine log model 上两次应用，得到同一全曲线上的 associated rational étale $G$-torsor。原 right action、$b,\Pi_r,\lambda_\infty$、hyperplane $s=1$ 与 flag 都由全忠实 tensor comparison 恢复，故这确是原群 $G$ 的 torsor，不仅是某个有相同 graded pieces 的 rank-$43$ representation。

其 abelian quotient 在 §§4–5 已锁定为
$(\mathsf M_{4,\infty},\mathsf M_{8,\infty},\gamma_{5,\infty})\otimes\mathbb Q_p$。
另一方面由同一 R1147 cohomology 及 Hochschild–Serre，
$$
H^0_{\rm et}(\mathcal M,Z)=H^1_{\rm et}(\mathcal M,Z)=0,
$$
因为三个 geometric $H^1$ 分别是
$\mathbb Q_p(1),\mathbb Q_p(3),\mathbb Q_p(5)$，均无 $G_{\mathbb Q_p}$ 不变量，而 geometric $H^0$ 全零。$H^0_{\rm et}(\mathcal M,V)$ 也为零。
固定 abelian quotient 的两个 class-two lifts 之差是 $H^1(\mathcal M,Z)$，其 automorphisms 由相应 $H^0$ 检测，故上述 associated torsor与原 $\mathscr P_\infty\otimes\mathbb Q_p$ 唯一相同。

于是得到本篇结论：
$$
\boxed{\begin{gathered}
\text{R1147 的原 rational rank-43 tower 在原 good model 上}\\
\text{有与 R1149 相同 Hodge connection 的 associated relative}\\
\text{crystalline realization，且延为全部 cusp 的 convergent log realization。}
\end{gathered}}
\tag{1150.15}
$$
强 associated comparison 经 $\mathcal O\mathbb B_{\rm cris}\to\mathcal O\mathbb B_{\rm dR}$ 给与原 étale source 相同的 filtered connection；R1149 的代数化与 regular connection analytification 的全忠实性把这个身份恢复为原代数连接。唯一 $\operatorname{Fil}^0$ lift 又锁定同一 Hodge frame。对好约化点 pullback，全忠实性与原 fibre comparison 恢复同一 $D_{\rm cris}(W_E)$，包括真实 Frobenius。
因此 R1149 §12 的相对 rational associatedness 前提已经由本篇支付；该文的短盘 lattice 恢复仍按其原未分歧、小权和实际 frame 条件使用，不扩到未付的 ramified integral 等价。

本篇没有计算 CM 参考点 $F_0$ 的未知中央条目，没有把 $I$ 提升到 $T_pE$，也没有删除原 global lift subtraction。
R1149 (1149.44) 的三槽公式现可在其声明的原短盘范围内无此附加前提地消费；原 supersingular 中央 unit、一般 $p$ 排点以及 full $N_{\rm ns}$ 全范围仍继续。

## 8. Primary 与精确依赖

- G. Faltings，*Crystalline cohomology and p-adic Galois-representations*，in J. I. Igusa (ed.), **Algebraic Analysis, Geometry, and Number Theory**, Johns Hopkins University Press, 1989, 25–80；§5、Lemma 5.5。消费的是 proper-log associated comparison、全忠实性及 **filtered $F$-isocrystal 一侧**的严格扩张封闭；§2 写出所用 period-cocycle 机制。Tsuji 的 [2001 讲义](https://swc-math.github.io/dls/DLSTsuji2.pdf) Theorem 3.3 指向这个已刊 lemma，但讲义不充当另一个未刊黑盒。
- G. Faltings，*Almost étale extensions*，**Astérisque 279** (2002), 185–270，[原文](https://www.numdam.org/item/AST_2002__279__185_0.pdf)，§5，特别 log PD 比较、水平边界、filtration 与 Frobenius 相容性。这里只消费本篇 smooth proper pair 的情形。
- F. Tan、J. Tong，*Crystalline comparison isomorphisms in p-adic Hodge theory: the absolutely unramified case*，**Algebra & Number Theory 13** (2019), 1509–1580，[正式全文](https://msp.org/ant/2019/13-7/ant-v13-n7-p01-s.pdf)，Corollary 2.17、Theorem 3.18 及其 fundamental exact sequence、Definition 3.10 / Proposition 3.22。消费内点的 horizontal period 输入及 de Rham compatibility；§2 明确不以 Proposition 3.21 的弱 associatedness 偷付 connection，也不以无边界表述代替 log 定理。
- K. Bannai、G. Kings，*p-adic elliptic polylogarithm, p-adic Eisenstein series and Katz measure*，**American Journal of Mathematics 132** (2010), 1609–1654，[作者全文](https://epub.uni-regensburg.de/13818/1/MP67.pdf)，Remark 2.5、Propositions 2.6、2.9、2.11。消费的是原 geometric symmetric powers 的全 modular-curve rigid/de Rham/residue comparison；不把 ordinary-locus 显式公式外推为本篇 Frobenius。
- R1147 §§8–15、R1149 §§1–15：全部原 primitive theta、phase/transfer、Tate normalization、Hodge/log source 与原 finite lattice。这里的中央 residue、Frobenius 矩阵和同源识别在正文逐项完成。

无数学程序执行；未改既成数值输入或重开固定 $47$ 窗口。
