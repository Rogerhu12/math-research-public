# R1147：原有限矩的唯一 universal lift 与规范 proper Heisenberg 来源

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面，所有 $p>37$。** R1146 给出原修正角色对的 proper 算术 Heisenberg 覆盖，并准确保留曲线上的中心 twist 歧义。本篇从 R1144 的三个实际有限矩恒等式出发，在 universal elliptic moduli 上先构造唯一提升，再沿原 Cartan 二次型作实际群同态。这样无须 F33，也能指定一个规范的原 proper 算术覆盖。这里的“规范”指本篇明确来源所选出的同构类，不断言曲线上其他中心 twists 消失。

本篇仍不证明其 $p$-local 标量非零或非恒定。它固定下一步实际读取所用的同一个覆盖。

## 1. 原有限矩的 H¹ 与辅助 c 的独立性

记
$$
S_0=\operatorname{Spec}\mathbb Z[1/p],\qquad
\mathcal M=\mathcal M_{1,1,S_0},\qquad
\mathcal H=\mathcal E[p],\qquad L_r=\mu_p^{\otimes r}.
$$
$\mathcal M$ 是光滑的 Deligne–Mumford stack；$\mathcal E$ 是 universal elliptic curve。以下 $L_r$ 均沿结构映射拉回。

在泛纤维 $\mathcal M_{\mathbb Q}$，保持 R1144 的原有限矩
$$
\mathsf M_d=
 \frac1{k_d(c)}
 \operatorname{Cor}_{\mathcal E[p]\setminus O\,/\,\mathcal M}
 \left(P^d\otimes\kappa(\theta_c(P))\right),
\quad
k_d(c)=c^2-c^{-d},
\quad d=4,8,12.
\tag{1147.1}
$$
$c>3$ 是 primitive mod $p$ 的辅助素数，故三个 $k_d(c)$ 都非零。仍使用全部有序非零 $p$-点；不增加平均因子。

R1144 §4 给
$$
H^0(\overline{\mathcal M},\operatorname{Sym}^d\mathcal H)=0,\qquad
H^1(\overline{\mathcal M},\operatorname{Sym}^d\mathcal H(t))
 \simeq L_{t-1}.
\tag{1147.2}
$$
Hochschild–Serre 的总次数一因而给
$$
H^1(\mathcal M_{\mathbb Q},
      \operatorname{Sym}^d\mathcal H(1))
 \simeq H^0(\mathbb Q,\mathbb F_p)
 =\mathbb F_p.
\tag{1147.3}
$$
同构由原 Tate residue 固定。原三个矩的 residue 分别为
$1/252,1/132,1/12$，不依赖 $c$。因此 (1147.1) 在泛纤维上真实地不依赖所选 $c$。这是整个 H¹ 类的独立性，而非仅两个 leading coefficients 相等。

## 2. 全 S₀ 整延拓，包括 2、3 和辅助素位

### 2.1 同一原 theta 的 vertical 阶逐项消去

固定 $\ell\ne p$。在 (1147.1) 中改选 $c\ne\ell$；由 (1147.3)，所得泛纤维类不变。逐 $\ell$ 使用 prime-to-$\ell$ 的辅助 fine level：$\ell=2$ 时用 level $3$，$\ell=3$ 时用 level $4$，其它 $\ell$ 可用二者之一。其 Galois degree 的素因子仅为 $2,3$，均为 $p$ 单位。于是局部问题可在正则 scheme chart 上检查，再用 trace 下降。

在同一个正则 Hodge frame chart $U$ 上，原 theta 是 universal elliptic curve 的 rational $K_1\otimes\mathbb Z_{(p)}$ 类，其水平 divisor 为
$c^2[O]-\mathcal E[c]$。若先乘原 $30$ 的幂使它为实际函数，则 divisor 与下列 valuation 也同步乘该幂；该幂是模 $p$ 单位，最后同步除回。相同的 frame 必须用于全部 $P$。

对 $U$ 的任一 vertical prime divisor $D$，$\mathcal E_D$ 在相应几何分支上不可约。原 theta 在它上的 vertical valuation 因此是一个共同数 $a_D$。由于 $p,c$ 互素且二者在这里均可逆，非零 $\mathcal E[p]$ 与 $O,\mathcal E[c]$ 在整模型上不相交。故每个非零 $p$-点处的 theta 值沿 $D$ 的 valuation 都是同一 $a_D$，没有另外的水平交数。改变正则 Hodge frame只产生另一个共同的 base 阶。

对有限 étale $p$-点 cover 求 corestriction 后，(1147.1) 在 $D$ 的 residue 为
$$
\frac{a_D}{k_d(c)}
 \operatorname{Tr}_{\mathcal E[p]\setminus O}
 (P^d)
 =\frac{a_D}{k_d(c)}
       \sum_{v\in\mathbb F_p^2\setminus0}v^d
 =0.
\tag{1147.4}
$$
最后一步逐单项式求和，使用 $0<d<p-1$。这是同一原 theta 在同一 frame 上的 vertical 消去；未假定每个 $\theta_c(P)$ 已经是整单位。

原类在 characteristic zero 的所有 noncusp 点本来无分歧；(1147.4) 又杀掉所有 vertical primes。因此有限 étale torsor 的正规化及纯度给出唯一整延拓
$$
\mathsf M_d\in
H^1(\mathcal M,\operatorname{Sym}^d\mathcal H(1)).
\tag{1147.5}
$$
不同 $\ell$ 使用的辅助 $c$ 在泛纤维相同。有限 étale torsor 的泛点平凡化在正规底上唯一延拓，所以这些局部类唯一粘合。

此论证未要求处理 characteristic $c$ 的单个 division polynomial：在那个位使用另一合法 $c$ 即可。它也没有删掉 $2,3,5$；在这些位系数中的 $30$ 仍是 $\mathbb F_p$ 的单位，vertical 同阶照 (1147.4) 消去。

### 2.2 中心 H² 的泛点单射

置
$$
\mathcal Z_0=\operatorname{Sym}^{12}\mathcal H(2),\quad
\mathcal Z_2=\operatorname{Sym}^{8}\mathcal H(4),\quad
\mathcal Z_4=\operatorname{Sym}^{4}\mathcal H(6),\quad
\mathcal Z=\mathcal Z_0\oplus\mathcal Z_2\oplus\mathcal Z_4.
\tag{1147.6}
$$
对每个 $\ell\ne p$，其几何特殊纤维的 $\mathcal H$-monodromy 是
$\mathrm{SL}_2(\mathbb F_p)$。可在上述 fine level $r=3$ 或 $4$ 上验证：加入完整 $p$-level 后，固定 Weil component 的 $X(pr)$ 在 $\ell\nmid pr$ 的 smooth proper 几何纤维连通，移去 cusps 后仍连通；CRT 给原 degree-$p$ 标记的 full $\mathrm{SL}_2(\mathbb F_p)$ monodromy。这使用完整 full-level 好模型，不把某个特殊椭圆曲线的 Galois 像当作 universal monodromy。

次数 $4,8,12$ 均正且小于 $p-1$，所以这些 symmetric powers 无几何不变量。因此
$$
H^0(\mathcal M_{\mathbb F_\ell},\mathcal Z(-1))=0.
\tag{1147.7}
$$
本处的 codimension-one cohomological purity 可直接在 smooth model 上核准：严格 henselian trait 的 prime-to-$\ell$ tame inertia 的 $p$-cohomological dimension 为一，故闭点的 $Ri^!\mathbf F_p$ 为 $\mathbf F_p(-1)[-2]$。在 fine-level chart 上 étale-locally 平凡化 $\mathcal Z$，由 smooth base change 将这一式拉到 vertical fibre，得到 $Ri^!\mathcal Z=\mathcal Z|_{\mathbb F_\ell}(-1)[-2]$。因此 localization 序列中删除该 fibre 的 H² kernel 是 (1147.7) 的像，故为零。逐个删有限多个素位，再取泛点极限，得到
$$
H^2(\mathcal M,\mathcal Z)
 \hookrightarrow H^2(\mathcal M_{\mathbb Q},\mathcal Z).
\tag{1147.8}
$$
DM stack 上的这一步可逐 $\ell$ 用上述 fine level、étale-local purity 与 prime-to-$p$ trace 检查；特别在 $2,3$ 不使用一个错误的 étale coarse quotient。

同样，有限 locally constant torsor 在正规底上的泛点单射给
$$
H^1(\mathcal M,\mathcal Z)
 \hookrightarrow H^1(\mathcal M_{\mathbb Q},\mathcal Z).
\tag{1147.9}
$$
由 (1147.2)，右侧的三个分量分别是
$H^0(\mathbb Q,L_1)$、$H^0(\mathbb Q,L_3)$、$H^0(\mathbb Q,L_5)$，全为零。因此
$$
\boxed{H^0(\mathcal M,\mathcal Z)
       =H^1(\mathcal M,\mathcal Z)=0.}
\tag{1147.10}
$$
H⁰ 的消失也直接来自几何无不变量。

## 3. 唯一的 universal class-two lift

令
$$
\mathcal V=
 \operatorname{Sym}^{4}\mathcal H(1)
 \oplus\operatorname{Sym}^{8}\mathcal H(1)
 \oplus L_5.
$$
写其元素为 $(x,y,t)$。$\gamma_5\in H^1(S_0,L_5)$ 是 R1144 的同一圆单位下降类：
$$
\gamma_5|_S=\epsilon_4\otimes\zeta_p^{\otimes4}.
$$
它在 $S_0$ 整，因为 $\epsilon_4$ 是原 $p$-unit 类。

使用 R1144 (1144.21) 的原 contractions $\Pi_0,\Pi_2,\Pi_4$，定义
$\mathcal V\times\mathcal V\to\mathcal Z$ 的双线性项
$$
\mathfrak b((x,y,t),(x',y',t'))=
\left(
 \Pi_0(x,y'),\
 \Pi_2(x,y'),\
 \Pi_4(x,y')+\frac{21}{11}x\otimes t'
\right).
\tag{1147.11}
$$
最后一槽的系数为
$\operatorname{Sym}^4\mathcal H(1)\otimes L_5
 =\mathcal Z_4$，所以各 Tate twists 准确吻合。

令 $\mathcal G$ 的底层为 $\mathcal V\oplus\mathcal Z$，群律
$$
(v,z)(v',z')=(v+v',\,z+z'+\mathfrak b(v,v')).
\tag{1147.12}
$$
双线性直接给结合律；$p$ 奇时 exponent 为 $p$。这是实际 finite étale class-two group sheaf，
$$
1\to\mathcal Z\to\mathcal G\to\mathcal V\to1.
$$
$\mathcal V$ 的秩为 $15$、$\mathcal Z$ 的秩为 $27$，故几何阶为 $p^{42}$。这里只用这一明确群，不称 free nilpotent group。

原 quotient torsor 是
$$
\eta=(\mathsf M_4,\mathsf M_8,\gamma_5)\in H^1(\mathcal M,\mathcal V).
$$
其 lifting obstruction 的三个分量正是
$$
C_0,\qquad C_2,\qquad
C_4+\frac{21}{11}\mathsf M_4\cup\gamma_5.
\tag{1147.13}
$$
R1144 证明它们在 $\mathcal M_{\mathbb Q}$ 的完整 H² 中全为零。
由 (1147.8)，整 $\mathcal M$ 上也全为零。因此 $\eta$ 有实际 $\mathcal G$-torsor 提升。

由 (1147.10)，固定 quotient 后的中心 twists 全为零。又
$H^0(\mathcal M,\mathcal V)=0$：前两项几何无不变量，第三项是非平凡算术角色 $L_5$。所以 quotient automorphisms 没有再改变这个 fiber。提升的 automorphism 也为零，因为其投影及中心 H⁰ 都为零。得到
$$
\boxed{\text{原 }\eta\text{ 有唯一到唯一同构的整 }
       \mathcal G\text{-torsor 提升 }\mathscr P.}
\tag{1147.14}
$$
存在性可用 R1146 §2 的连续 cochain 论证：所需
$H^2(\pi_1,\mathcal Z)\hookrightarrow H^2_{\rm et}(\mathcal M,\mathcal Z)$
仍由有限 étale covers 的五项列给出；同一论证适用于此 DM stack。也可直接使用 central lifting gerbe。没有假设一个未付的 $p$-adic unipotent lift。

(1147.14) 特别给出所需原来源的选择规范。这里没有将
$H^1(\mathscr X_0,L_8)$ 设为零；消失发生在较大的 universal coefficient sheaf $\mathcal Z$ 上。

## 4. 原 Cartan 上的 determinant twists 与实际群同态

令 $\mathcal Y_{\rm ns}^{+}(p)$ 为非尖点 Cartan moduli stack。其 elliptic curve 的实际 Cartan 中有唯一的一对 trace-zero endomorphisms
$$
\{I,-I\}\subset\operatorname{End}(\mathcal H),\qquad I^2=\delta.
$$
用原 Weil pairing $\langle\ ,\ \rangle:\bigwedge^2\mathcal H\to L_1$ 定义
$$
q_I(v)=\langle v,Iv\rangle\in L_1.
\tag{1147.15}
$$
$I\mapsto-I$ 使 $q_I$ 变号，但 $q_I^2,q_I^4,q_I^6$ 都真下降到 normalizer 商。在原 fixed-Weil frame
$$
I=\begin{pmatrix}0&\delta\\1&0\end{pmatrix}
$$
时，$q_I(x,y)=x^2-\delta y^2=N(x,y)$。这准确识别原 norm，不另作一个未付的 determinant-one 化。

因此
$$
q^2:\operatorname{Sym}^4\mathcal H\to L_2,\quad
q^4:\operatorname{Sym}^8\mathcal H\to L_4,\quad
q^6:\operatorname{Sym}^{12}\mathcal H\to L_6
$$
是算术上真实的 maps。每次 determinant twist 已在 (1147.15) 的 $L_1$ 值域中保留。

设 $\mathcal H_{\rm Heis}$ 是 R1146 的三线群 $L_3,L_5,L_8$。定义
$$
\begin{aligned}
a(v)&=\tfrac12 q^2x,\\
b(v)&=\tfrac12 q^4y+\frac{8\delta^2}{11}t,\\
h(z)&=\tfrac14 q^6z_0-\frac{4\delta}{11}q^4z_2
                 +\frac{4\delta^2}{21}q^2z_4 .
\end{aligned}
\tag{1147.16}
$$
前两式分别在 $L_3,L_5$，第三式在 $L_8$。R1144 的完整 polar identity 给
$$
h(\mathfrak b(v,v'))=a(v)\otimes b(v').
\tag{1147.17}
$$
确切地，前三 contraction 项是
$(q^2x)(q^4y')/4$；(1147.11) 的最后补项是
$(4\delta^2/11)(q^2x)t'$，恰为
$(q^2x/2)(8\delta^2t'/11)$。

所以
$$
(v,z)\longmapsto(a(v),b(v),h(z))
\tag{1147.18}
$$
是实际群同态。$q^{2j}$ 非零、$8\delta^2/11$ 为单位，中心 map 也非零，故该 map 在几何 fibre 上满射。把 (1147.14) 拉回 Cartan stack，再沿 (1147.18) 作 torsor pushout，给一个指定的
$\mathcal H_{\rm Heis}$-torsor。

由 R1144 (1144.8)，其原 quotient classes 正是
$$
a_0|_S=A_1\otimes\zeta_p^{\otimes2},\qquad
b_0|_S=\left(A_2+\frac{8\delta^2}{11}\epsilon_4\right)
                    \otimes\zeta_p^{\otimes4}.
\tag{1147.19}
$$
因此它与 R1146 使用完全相同的两槽、常数和三条下降线。不新增半 Cartan trace、$m$ 或 $2$ 的因子。

## 5. coarse 下降、全部 cusps 与算术纯度

### 5.1 非尖点 coarse 下降包括特征 2、3

非尖点几何 elliptic automorphisms 在 $L_3,L_5,L_8$ 上均平凡作用，因为它们保持 Weil pairing。它们在 torsor fibre 上因而只能通过 Heisenberg 平移作用。其阶的素因子仅为 $2,3$，而该 Heisenberg 群是 $p$-群，所以这个作用必为零。

这里在特征 $2,3$ 不把稳定子误写成仅阶 $2$ 或 $3$；可能的更大 elliptic automorphism groups 仍只有这些素因子。也不要求 wild coarse quotient 本身是 étale。可在一个 strict-henselian 局部 quotient chart 上把有限 étale torsor 平凡化为若干 copies；稳定子固定每一 copy，取商后每一 copy 的局部环就是原 coarse 局部环。因此覆盖真实下降为原 coarse open $Y/S_0$ 上的 finite étale $\mathcal H_{\rm Heis}$-torsor。

### 5.2 generic cusp 的中心惯性由原 real 下降杀掉

在原 compact $X_{\mathbb Q}$ 的任一 cusp $c$，两槽 (1147.19) 已经 proper，所以 cusp inertia 的像只能在中心 $L_8$。内部共轭在中心平凡，故惯性 map 必须是
$G_{k(c)}$-等变的
$$
I_c\longrightarrow L_8.
$$
其可能的 tame residue 属于
$$
\operatorname{Hom}(I_c,L_8)=L_8(-1)=L_7
\quad\text{的 }G_{k(c)}\text{-不变量}.
\tag{1147.20}
$$
全部原 cusp fields 是实域。复共轭在 $L_7$ 上为 $-1$，所以这个 invariant 为零。因 $p$ 奇，中央惯性全部消失，覆盖在 generic 的每个 cusp 无分歧。

本步使用原实际 cusp 定义域，不凭空指定一个 rational base cusp；也未将无分歧说成 residue extension 分裂。

### 5.3 全 S₀ proper 延拓

在 R1067 的原正则 smooth proper 模型 $\mathscr X_0/S_0$ 上取上述覆盖的正规化。每个 vertical prime 的 generic point 已在 noncusp open 中，故无分歧；全部 horizontal cusp primes 又由 (1147.20) 无分歧。其余 horizontal primes 本来在 open 中。所有 codimension-one ramification 因而为零。

Zariski–Nagata purity 排除 cusp 与特殊 fibre 交点处可能的 codimension-two branch。于是正规化给
$$
\boxed{\quad
\mathscr Y_{\rm mom}\longrightarrow\mathscr X_0
\quad\text{一个指定的 finite étale }
\mathcal H_{\rm Heis}\text{-torsor}.
\quad}
\tag{1147.21}
$$
正规化与群作用的延拓唯一，故这是原 universal moment 来源的规范 proper 算术覆盖，适用于每个 $p>37$，没有额外排除 $2,3,5,c$。

其几何连通直接消费 R1064 (1064.2)、(1064.5) 的原两角色注入：两个几何 Kummer 类独立，加入常数 $\epsilon_4$ 不改变它。因此几何 monodromy 满射到 $\mathbb F_p^2$；任取两个行列式非零的 lifts，它们的交换子生成全部中心，故 monodromy 就是 $H_p$。覆盖的实际几何 degree 为 $p^3$。Genus 以及 rational-point 的全局提升性质沿用 R1146。

## 6. 对实际 p-local 读取的意义及保留范围

(1147.21) 给 R1146 (1146.22) 一个明确且无门的 cover 选择：
$$
\operatorname{ob}_{{\rm mom},p}(x_p;u,v)
 =[Y_{{\rm mom},x_p}]-\operatorname{loc}_p\eta(u,v).
\tag{1147.22}
$$
它使用原 theta moments、原 $\gamma_5$ 和 (1147.16) 的具体 pushout；不是先任选中心 cochain 后把其值叫作规范读数。

这不意味着原曲线上所有 Heisenberg lifts 同构。一般的
$H^1(\mathscr X_0,L_8)$ 中央歧义仍如 R1146 §7；F33 门可杀全部该歧义，本篇则是在无门时选定一个实际来源。

同样，唯一来源不等于已经计算 (1147.22)。这里没有宣称这个 $\mathbb F_p$ 标量在某个 supersingular disk 非零或非恒定。下一步仍须用同一 $\mathscr P$ 的 finite cochains 或同一 theta 来源求它的实际首项；不能把有限 $\mathbb F_p$-Heisenberg torsor 未经证明地替换成一个 $\mathbb Q_p$-unipotent connection。

## 7. 来源和验证范围

- [R1144](R1144-original-finite-moments-and-exact-proper-cup.md)：三个有限矩、几何 cohomology 的完整模 $p$ 计算、$C_0,C_2$ 及 corrected $C_4$ 的实际零类、原 norm polar identity。
- [R1146](R1146-original-proper-arithmetic-Heisenberg-cover.md)：三条下降线、中心扩张的实际 cochain/finite étale 实现、全部原 cusp fields、曲线与底算术的中心歧义区别。
- [R1067](R1067-original-cuspidal-labels-supported-only-at-p.md)：原 full-level 及 Cartan quotient 的 good integral models，包括 $2,3$；本篇另写明 universal moment 的原 vertical 同阶消去。
- [R1138](R1138-original-integral-bare-cup-smoothing-comparison.md)：同一个 trace-fixed theta 的 divisor 与原 all-vector 规范。逐位换辅助 $c$ 只在 (1147.3) 已证明完整 H¹ 独立后使用。
- J. S. Milne, *Lectures on Étale Cohomology*, [作者全文](https://www.jmilne.org/math/CourseNotes/LEC.pdf)，Theorem 20.1 及其 scheme 适用说明（印刷127–128页）：smooth base change；本篇 §2.2 另写出严格局部 trait 的低阶 purity，以得到实际 vertical Gysin 项。
- A. Grothendieck 等，*Revêtements étales et groupe fondamental*（SGA 1），Exposé X, Theorem 3.1；同一 branch-purity 结论见 [Stacks Project, Lemma 58.21.4, Tag 0BMB](https://stacks.math.columbia.edu/tag/0BMB)。§5.3 的底为 R1067 已付的正则模型，有限正规化在所有 codimension-one 点无分歧，逐项满足该结论。
- 本篇的低阶 H¹、群律、pushout 及 cusp residue 全部在文中逐式证明。正规底上 finite étale torsor 的泛点单射、étale purity 与 Zariski–Nagata purity 按 fine level 的 scheme charts 使用，再由 prime-to-$p$ trace 与局部 quotient 描述下降，不将 characteristic $2,3$ 的 coarse map 冒作 étale。

无数学程序执行；未修改已有 Actions 请求或既成数值输入。


## 8. 同一 theta 的 primitive $p^n$ 矩及精确兼容箭头

以下是 §§1–7 的后继，仍只用原 theta，且不预设一个 $\mathbb Q_p$-connection。设
$$
R_n=\mathbb Z/p^n,\quad N=p^n,\quad
\mathcal H_n=\mathcal E[N],\quad
L_{r,n}=\mu_N^{\otimes r},\quad
U_n=\mathcal E[N]\setminus\mathcal E[N/p].
$$
$U_n$ 是 exact-order-$N$ 的有序点 cover。固定一个 $c>3$、$(c,p)=1$、primitive mod $p$ 的辅助素数，令
$$
k_d(c)=c^2-c^{-d}\in\mathbb Z_p^\times,\qquad d=4,8,12.
$$
在 $\mathcal M_{\mathbb Q}$ 定义实际类
$$
\mathsf M_{d,n}=
k_d(c)^{-1}\operatorname{Cor}_{U_n/\mathcal M}
 \bigl(P^d\otimes\kappa_N(\theta_c(P))\bigr)
 \in H^1(\mathcal M_{\mathbb Q},
              \operatorname{Sym}^d\mathcal H_n(1)).
\tag{1147.23}
$$
若原 trace-fixed $\theta_c$ 写在 $K_1\otimes\mathbb Z[1/6]$ 中，这里的 Kummer map 是按 $R_n$ 中可逆的同一分母解释；不反除 $p$。

使用同一 $\theta_c$ 的 exact distribution
$$
[p]_*\theta_c=\theta_c\qquad((p,c)=1).
\tag{1147.24}
$$
此式是原 theta 的 norm，而非一个相差未知 base 常数的 divisor 身份。Kato 的 theta 定理在 Kings §3.3, Theorem 3.3.1 中同时给出 divisor、distribution 与 base change；本篇使用其完整函数规范。也可沿 R1138 的 trace-fixed 规范证明：divisor 比较后的 base 常数由 prime-to-$pc$ 的全部 trace identities 固定，可能的 $24$-torsion 在 $R_n$ 中消失。

映射 $[p]:U_{n+1}\to U_n$ 的每个 fibre 含全部 $p^2$ 个原点，且它们全是 primitive。系数约化 $\mathcal H_{n+1}\to\mathcal H_n$ 是 $P\mapsto pP$。由 projection formula 和 (1147.24)，
$$
\mathsf M_{d,n+1}\pmod{p^n}=\mathsf M_{d,n}.
\tag{1147.25}
$$
没有额外 $p$、$p^d$ 或 degree 平均。$n=1$ 精确是 (1147.1)。

圆单位的兼容性须另定准确箭头。置 $K_n=\mathbb Q(\zeta_N)$，选择 $\zeta_{p^{n+1}}^p=\zeta_{p^n}$，定义
$$
\gamma_{5,n}
 =\operatorname{Cor}_{K_n/\mathbb Q}
   \bigl(\kappa_N(1-\zeta_N)\otimes\zeta_N^{\otimes4}\bigr)
 \in H^1(S_0,L_{5,n}).
\tag{1147.26}
$$
它在 $K_n$ 的 restriction 是
$$
\epsilon_{4,n}\otimes\zeta_N^{\otimes4},\qquad
\epsilon_{d,n}
 =\sum_{b\in(\mathbb Z/N)^\times}
       b^d\kappa_N(1-\zeta_N^b).
\tag{1147.27}
$$
由
$\operatorname{Norm}_{K_n/K_{n-1}}(1-\zeta_N)=1-\zeta_{N/p}$，
先约化系数再用 corestriction transitivity，得到
$$
\gamma_{5,n}\pmod{p^{n-1}}=\gamma_{5,n-1}.
\tag{1147.28}
$$
这是 **$\mathbb Q$ 上类的系数约化**。不把 $\epsilon_{4,n}$ 的 field norm 叫作同一兼容箭头：该加权全轨和的 field norm 是 $p\epsilon_{4,n-1}$。$n=1$ 的 (1147.26) 与原 $\gamma_5$ 相同。

## 9. 全 primitive 轨道的 Tate residue：非单位 $a$ 也保留

保持 R1144 的 Tate basis：
$$
e_1=q^{1/N},\qquad e_2=\zeta_N,\qquad
u(e_1)=e_1+e_2,\quad u(e_2)=e_2.
$$
$e_2$ 是惯性不变量，$e_1^d$ 是 symmetric-power coinvariant 的生成元。所有计算先在 $K_n$ 的 Tate punctured chart 作，arithmetical section 固定所选全部 $q$-roots。

### 9.1 实际 leading 的阶与相位

写 $0<a<N$，$ca=Nr+s$，$0<s<N$。原 theta 的 Tate product 给
$$
\begin{aligned}
k_N(a)
 &=ca r+\frac{c-c^2}{2}a
   -\frac N2(r^2+r)+\frac N{12}(c^2-1),\\
h_c(a)&=cr+\frac{c-c^2}{2},\\
k_N(a)&\equiv a h_c(a)\pmod N.
\end{aligned}
\tag{1147.29}
$$
这里 $k_N(a)=N\operatorname{ord}_q\theta_c(P)$。若 $P=a e_1+b e_2$，同一 product 的 leading 还包含真实相位
$\zeta_N^{b h_c(a)}$。符号因子是 $2$-primary，故其 $R_n$-Kummer 类为零；共同 Hodge frame 因子仍保留到加权总和才消去。

为逐项核 (1147.29)，可用
$$
\theta_c(v)=
q^{(c^2-1)/12}(-v)^{(c-c^2)/2}
\frac{(1-v)^{c^2}}{1-v^c}
\frac{\prod_{j\ge1}(1-q^jv)^{c^2}(1-q^j/v)^{c^2}}
     {\prod_{j\ge1}(1-q^jv^c)(1-q^j/v^c)} .
$$
代 $v=q^{a/N}\zeta_N^b$。分母中 $j=1,\ldots,r$ 的负 $q$ 阶因子准确贡献
$cbr$ 的 $\zeta_N$ 指数及
$ca r-Nr(r+1)/2$ 的阶；其余因子给 (1147.29) 的其余项。这里未以 Bernoulli 的 fractional-part 记号隐去相位。

令 $g=p^{v_p(a)}$，$h=N/g$。固定 $a$ 的惯性轨道长度是 $h$，代表由 $b\bmod g$ 给出。若 $g=1$，只有一个轨道；若 $g>1$，primitive 条件正是 $b\in(\mathbb Z/g)^\times$，所以共有 $\varphi(g)$ 个轨道。该点在参数 $q^{1/h}$ 上的实际 theta 阶为 $k_N(a)/g$。

于是每个轨道对 coinvariant residue 的贡献是
$a^d k_N(a)/g$。记
$$
S_N=\sum_{a=1}^{N-1}a^d k_N(a),\qquad S_1=0.
$$
又 $k_N(pa')=p k_{N/p}(a')$，合并全部 primitive 轨道得到
$$
v_{d,n}
 =\frac{S_N-p^dS_{N/p}}{k_d(c)}
 \pmod N.
\tag{1147.30}
$$
其中非单位 $a$ 的系数 $\varphi(g)/g=(p-1)/p$ 已完整计入。不把所有非零 $a$ 都误当长度 $N$ 的轨道。

### 9.2 幂和给精确 $\mathbb Z_p$ 值

令 $M=d+2$。$a\mapsto s=ca-Nr$ 置换 $1,\ldots,N-1$。比较
$\sum s^M=\sum a^M$ 模 $N^2$：
$$
M c^{M-1}\sum a^{M-1}r
 \equiv (c^M-1)\frac{\sum a^M}{N}\pmod N.
$$
这里 $M\le14<p-1$，所有涉及的小权 Bernoulli 分母都是 $p$ 单位。Faulhaber 恒等式给
$\sum a^M/N\equiv B_M\pmod N$。同时，$M-1$ 为奇数且大于一，
$\sum a^{M-1}$ 被 $N^2$ 整除。将这些式子代入 (1147.29)，得到
$$
S_N\equiv
(c^2-c^{-d})\,\frac{B_{d+2}}{d+2}\pmod N.
\tag{1147.31}
$$
(1147.30) 的低层误差乘 $p^d$ 后仍被 $N$ 整除。因此各层 residue 是同一精确整数的约化：
$$
\boxed{\quad
v_{d,n}=v_d^\infty\bmod p^n,\qquad
v_d^\infty=(1-p^d)\frac{B_{d+2}}{d+2}.
\quad}
\tag{1147.32}
$$
特别
$$
v_4^\infty=\frac{1-p^4}{252},\qquad
v_8^\infty=\frac{1-p^8}{132},\qquad
v_{12}^\infty=\frac{1-p^{12}}{12},\qquad
\frac{v_8^\infty}{v_4^\infty}
 =\frac{21}{11}(1+p^4).
\tag{1147.33}
$$
三个值均是 $\mathbb Z_p$ 单位。$n=1$ 恢复 §§1–3 的原 residue 和 $21/11$，不改变既成模 $p$ 常数。

### 9.3 非单位轨道的 arithmetic transfer 与相位共同消去

这一门不能只靠 residue 或一个非单位轨道的 norm 为零。

取 $\sigma\in G_{K_n}$，写
$s_\sigma=(\chi_{\mathrm{cyc}}(\sigma)-1)/N\bmod N$。固定上面一个 $a,b$ 轨道，用代表 $u^i$，$0\le i<h$。theta 的真实 leading phase 的 Kummer cocycle 是
$b h_c(a)s_\sigma$。ramified 参数的 transfer 同时给
$k_N(a)i s_\sigma$。二者由 (1147.29) 合成
$$
s_\sigma h_c(a)
 \sum_{i=0}^{h-1}(b+ia)
       \bigl(ae_1+(b+ia)e_2\bigr)^d .
\tag{1147.34}
$$
这是先合并实际 phase 与 ramified transfer 后的总式；不能分别删除两项。

再对 primitive 的 $b\bmod g$ 求和，$b'=b+ia$ 在 $a$ 为单位时遍历 $\mathbb Z/N$，在 $a$ 非单位时遍历 $(\mathbb Z/N)^\times$。每个坐标的 $b'$ 次数是 $j+1$，$1\le j+1\le d+1<p-1$。这两种集合的该次数幂和都为 $0\bmod N$：乘一个 Teichmüller unit，其 $j+1$ 次幂不等于一，即可逐式证明。因此 (1147.34) 的 **全 primitive 和** 为零。

共同 frame/leading 常数的总贡献也为零，因为
$\sum_{P\ {\rm primitive}}P^d=0$；同样用 scalar homothety 且 $c^d-1$ 可逆证明。在 $a=0$ 的 $\mu_N$ 轨道中，共同 $q$ 阶与 frame 乘
$\sum_{b\in R_n^\times}b^d=0$，相位乘
$\sum b^{d+1}=0$，准确只余 (1147.27)。

由惯性 coinvariant 的整自由性，可以减去一个在 $G_{K_n}$ 上为零的 coboundary，把完整 Tate cocycle 写成
$$
\mathsf M_{d,n}=R_{d,n}+U_{d,n},\qquad
\begin{array}{ll}
R_{d,n}(u)=v_{d,n}e_1^d,&R_{d,n}(G_{K_n})=0,\\
U_{d,n}(u)=0,&
U_{d,n}(\sigma)=\epsilon_{d,n}(\sigma)e_2^d .
\end{array}
\tag{1147.35}
$$
$R_{d,n}$ 真正经 $C_N$ inflation：其 norm 是各次数 $\le d$ 的完整幂和，所以为零。这里没有假设每个非单位 $a$ 的 orbit norm 都为零。

## 10. 完整 $R_n$-cohomology 与同源 cup 恒等式

### 10.1 几何 H¹ 的整自由性，不只模 p 维数

对 $d=4,8,12$，使用同一 $\mathrm{PSL}_2(\mathbb Z)=C_2*C_3$ 计算。因 $2,3$ 在 $R_n$ 中可逆，两个 cyclic invariants 都是自由直和项，其秩分别为
$(3,1),(5,3),(7,5)$。模 $p$ 时它们的交为零，且其和的秩为 $d$。故相应矩阵有一个模 $p$ 非零的 $d$ 阶 minor，亦即在 $R_n$ 上有 unit minor。因此其 cokernel 是自由秩一；不是仅凭模 $p$ 维数宣称无高层扭结。

同一 prime-to-$p$ 的 $\Gamma(4)$ free-group cover 给 geometric cohomological dimension 一；由模 $p$ 无不变量及逐 $p$ 降阶，也有所有 $R_n$ 层 H⁰ 为零。由 (1147.32) 的单位 residue，准确得到
$$
H^0(\overline{\mathcal M},\operatorname{Sym}^d\mathcal H_n)=0,\quad
H^1(\overline{\mathcal M},
       \operatorname{Sym}^d\mathcal H_n(t))
 \simeq R_n(t-1),\quad
H^{\ge2}(\overline{\mathcal M},-)=0.
\tag{1147.36}
$$
同构是原 cusp residue，保持完整 $G_{\mathbb Q}$ 作用。因此总次数一、二的 HS 给
$$
\begin{aligned}
H^1(\mathcal M_{\mathbb Q},
        \operatorname{Sym}^d\mathcal H_n(1))&\simeq R_n,\\
H^2(\mathcal M_{\mathbb Q},
        \operatorname{Sym}^d\mathcal H_n(t))&\simeq
             H^1(\mathbb Q,R_n(t-1)).
\end{aligned}
\tag{1147.37}
$$
这也证明 (1147.23) 的辅助 $c$ 独立性在完整 $R_n$-H¹ 中成立。

### 10.2 有限 cyclic cup 的实际零与算术下降

在 $C_N$ 的 cyclic resolution 上，$R_{4,n}\cup R_{8,n}$ 的 H² 代表是
$$
\sum_{i=0}^{N-1}
 R_{4,n}(u^i)\otimes u^i R_{8,n}(u).
$$
逐坐标为 $i$ 的多项式，次数至多 $13$，其分母只含 $\le13$ 的整数。对 $0\le j\le13<p-1$，$\sum_{i=0}^{N-1}i^j=0\bmod N$，故这个 **完整 H² 类** 为零。它不是仅有几何 residue 为零。

沿同一 $\Pi_0,\Pi_2,\Pi_4$ 投影 (1147.35) 的两 mixed terms，只有 $\Pi_4(U_{4,n}\cup R_{8,n})$ 在 coinvariant 中留下
$+v_{8,n}\gamma_{5,n}$；另一个 mixed term 及 $r=0,2$ 均仍含 $e_2$，在 coinvariant 为零。同一 cup 次序给
$$
\operatorname{res}(\mathsf M_{4,n}\cup\gamma_{5,n})
  =-v_{4,n}\gamma_{5,n}.
$$
这些是同一有序点、同一 Tate basis 下的符号，沿用 R1144 的 $\Pi_4$ 规范。

下降至 $\mathbb Q$ 不能用 $[K_n:\mathbb Q]$ 为 $p$ 单位，因为 $n>1$ 时它不成立。准确理由是
$$
\operatorname{Gal}(K_n/\mathbb Q)=\Delta\times P_n,\qquad
|\Delta|=p-1,\quad |P_n|=p^{n-1}.
$$
对 $k=1,3,5$，$\Delta$ 在
$H^i(P_n,R_n(k))$ 上的作用是非平凡 Teichmüller 角色 $\omega^k$；它在 $P_n$ 上的共轭平凡。因此这些群的 $\Delta$-invariants 为零。Lyndon–Hochschild–Serre 给
$H^1(\operatorname{Gal}(K_n/\mathbb Q),R_n(k))=
 H^2(\operatorname{Gal}(K_n/\mathbb Q),R_n(k))=0$。
特别所需的 global H¹ restriction 单射。

结合 (1147.37)，得到完整 universal cohomology 恒等式
$$
\boxed{
\begin{aligned}
\Pi_0(\mathsf M_{4,n}\cup\mathsf M_{8,n})&=0,\\
\Pi_2(\mathsf M_{4,n}\cup\mathsf M_{8,n})&=0,\\
\Pi_4(\mathsf M_{4,n}\cup\mathsf M_{8,n})
 &=-\frac{21}{11}(1+p^4)
       \mathsf M_{4,n}\cup\gamma_{5,n}.
\end{aligned}}
\tag{1147.38}
$$
系数按 $R_n$ 约化。这没有声称整个
$\operatorname{Sym}^4\otimes\operatorname{Sym}^8$ 的所有 odd contractions 都零；仍只使用原 norm polar identity 所需的 $r=0,2,4$。

## 11. 唯一兼容的整 class-two tower

以 $\mathcal H_n,L_{r,n}$ 替换 §3 的系数，记所得 $\mathcal V_n,\mathcal Z_n$。在原第三 bilinear 槽使用同一精确 $\mathbb Z_p$ 单位
$$
\lambda_\infty=\frac{21}{11}(1+p^4).
$$
也就是
$$
\mathfrak b_n(v,v')=
\bigl(\Pi_0(x,y'),\Pi_2(x,y'),
      \Pi_4(x,y')+\lambda_\infty x\otimes t'\bigr).
\tag{1147.39}
$$
群律仍为 (1147.12)，得到实际 finite étale group sheaf $\mathcal G_n$，几何阶 $p^{42n}$、exponent $p^n$。其 quotient 是
$$
\eta_n=(\mathsf M_{4,n},\mathsf M_{8,n},\gamma_{5,n}).
$$
(1147.38) 正是其三个 lifting obstructions 的零。

所有层在 $S_0$ 的整性按 §2 的同一论证付款。逐 $\ell\ne p$ 换辅助 $c\ne\ell$ 后，同一 Hodge frame 的 vertical valuation 仍是共同数；primitive 点总和
$\sum P^d=0$ 由 homothety 和 $c^d-1\in R_n^\times$ 给出。系数 $\operatorname{Sym}^d\mathcal H_n$ 在每个几何特殊纤维的 monodromy 是
$\mathrm{SL}_2(\mathbb Z/p^n)$：逐 fine level 用固定 Weil component 的 full-level good model 和 CRT。模 $p$ 无不变量，逐 $p$ 降阶即给
$$
H^0(\mathcal M_{\mathbb F_\ell},\mathcal Z_n(-1))=0.
$$
所以 §2.2 的 vertical Gysin 同样给
$H^2(\mathcal M,\mathcal Z_n)\hookrightarrow
H^2(\mathcal M_{\mathbb Q},\mathcal Z_n)$。
完整 (1147.38) 因而在整模型上成立。

由 (1147.36)–(1147.37)，
$$
H^0(\mathcal M,\mathcal V_n)=0,\qquad
H^0(\mathcal M,\mathcal Z_n)=H^1(\mathcal M,\mathcal Z_n)=0:
$$
中心三项只读 $R_n(1),R_n(3),R_n(5)$ 的算术 invariants，而它们的 Teichmüller 角色均非平凡。因此存在唯一到唯一同构的原整提升
$$
\mathscr P_n\in H^1(\mathcal M,\mathcal G_n).
\tag{1147.40}
$$
(1147.25)、(1147.28) 及群律 (1147.39) 与系数约化相容。唯一性强迫各 $\mathscr P_n$ 的约化同构也唯一相容。因此它们给一个真实 pro-finite étale torsor
$$
\mathscr P_\infty=\varprojlim_n\mathscr P_n
\quad\text{under}\quad
\mathcal G_\infty=\varprojlim_n\mathcal G_n.
\tag{1147.41}
$$
其 Lie lattices 是
$\operatorname{Sym}^4T_p\mathcal E(1)\oplus
 \operatorname{Sym}^8T_p\mathcal E(1)\oplus\mathbb Z_p(5)$
及原三个中心 symmetric powers；群律有整数系数，仍是明确 class two。反除 $p$ 后得到相同实际来源的 unipotent group torsor，而非另任选一个 rational substitute。

$n=1$ 时 $\lambda_\infty\equiv21/11\bmod p$，所以 (1147.40) 准确回到 §3 的 $\mathscr P$。**原 Cartan pushout 仍先约化到 $p$ 再用 §4 的 $q_I$。** 原 $I\in\operatorname{End}(E[p])$ 不因此获得一个未付的 $\operatorname{End}(T_pE)$ 提升；本篇不声称原 level-$p$ curve 上的三个常 Tate 线 Heisenberg 群本身已经提升为相同三线的 $\mathbb Z_p$ 群。

## 12. 新塔的范围、来源和下一接口

(1147.41) 支付了 §6 所要求的来源门：原有限覆盖确为同一 theta 的整 compatible tower 在第一层的实际 pushout。全部 primitive 点、所有非单位惯性轨道、相位、算术 corestriction 和高层修正 $(1+p^4)$ 均已保留。

这里仍没有从 ordinary de Rham 公式推断 supersingular disk 的中央首项，也没有把 Cartan coarse 参数的三阶变化简化为一个 fine 一阶变化。下一步若使用 crystalline 或 de Rham comparison，必须对 (1147.41) 的同一 fibre 或同一相对对象，并再按 §4 的原模 $p$ map 读取。

新增 primary 来源：

- G. Kings, *Eisenstein classes, elliptic Soulé elements and the $\ell$-adic elliptic polylogarithm*, [作者 arXiv 全文](https://arxiv.org/pdf/1304.7161)，§3.3, Theorem 3.3.1 及 Definitions 3.3.3–3.3.4：Kato 的原 theta、prime-to-$c$ exact norm、base change 及 finite Kummer/moment 来源。本篇的高层 primitive residue 与 arithmetic-phase 消去在 §§9–10 自证；不使用该文后段含 level 分母的有理比较来约模 $p$。
- R1138、R1144 与本篇 §§1–7：保持所有原 theta、full ordered vector、Tate basis 和 contraction 规范。新增 (1147.38) 是 $R_n$ 的完整 H² 身份，不只一个 rational identity 或 residue equality。

无数学程序执行；未更改既成输入、Actions 请求或结果。新塔仍未给出 $p$-local 首项的实际非零性。


## 13. 好约化点上同一 tower 的 crystalline fibre

本节是逐点比较，允许 supersingular reduction。先令 $F/\mathbb Q_p$ 为任意有限扩张，$\mathcal O_F$ 为其整数环，$E/\mathcal O_F$ 为光滑 proper elliptic curve。将 (1147.41) 拉回这个实际点，反除 $p$，记
$$
H=T_pE\otimes\mathbb Q_p,\quad
V=\operatorname{Sym}^4H(1)\oplus
  \operatorname{Sym}^8H(1)\oplus\mathbb Q_p(5),
$$
$$
Z=\operatorname{Sym}^{12}H(2)\oplus
  \operatorname{Sym}^{8}H(4)\oplus
  \operatorname{Sym}^{4}H(6),\qquad
G=V\oplus Z
$$
并保持 (1147.39) 的同一个 bilinear 群律。记实际 fibre 为 $P_E$。

### 13.1 线性 local 条件全部满足

$H$ 是原 good elliptic curve 的 crystalline Tate module。这里以 de Rham filtration 的跳跃记 Hodge weights，故 $H$ 的两个 weights 是 $0,-1$。各 graded pieces 的范围如下：

| piece | filtration weights | Frobenius Weil weight |
|---|---:|---:|
| $\operatorname{Sym}^4H(1)$ | $-5,\ldots,-1$ | $-6$ |
| $\operatorname{Sym}^8H(1)$ | $-9,\ldots,-1$ | $-10$ |
| $\mathbb Q_p(5)$ | $-5$ | $-10$ |
| $\operatorname{Sym}^{12}H(2)$ | $-14,\ldots,-2$ | $-16$ |
| $\operatorname{Sym}^{8}H(4)$ | $-12,\ldots,-4$ | $-16$ |
| $\operatorname{Sym}^{4}H(6)$ | $-10,\ldots,-6$ | $-16$ |

Weil weight 指 residue-field Frobenius 的复绝对值；对 $T_pE$ 使用 weight $-1$，并不把 arithmetic Frobenius 的点坐标约定混入此表。因而 $V,Z$ 以及 $V^*(1),Z^*(1)$ 均没有 Frobenius eigenvalue 一，特别
$$
H^0(F,V)=H^0(F,V^*(1))
 =H^0(F,Z)=H^0(F,Z^*(1))=0.
\tag{1147.42}
$$
这里 dual-twist pieces 的 Weil weights 分别是 $4,8,14$，全不为零。Local Tate duality 于是给 $H^2(F,V)=H^2(F,Z)=0$。

对 $W=V$ 或 $Z$，Bloch–Kato exact sequence 与 local Euler characteristic 给
$$
\begin{aligned}
\dim_{\mathbb Q_p}H^1_f(F,W)
 &=\dim_{\mathbb Q_p}D_{\rm dR}(W)/\operatorname{Fil}^0
     +\dim_{\mathbb Q_p}H^0(F,W)\\
 &=[F:\mathbb Q_p]\dim_{\mathbb Q_p}W
   =\dim_{\mathbb Q_p}H^1(F,W).
\end{aligned}
$$
因此
$$
\boxed{H^1(F,V)=H^1_f(F,V),\qquad
       H^1(F,Z)=H^1_f(F,Z).}
\tag{1147.43}
$$
这个论证不使用 ordinary unit-root splitting。

### 13.2 真实非交换 fibre 也是 crystalline

$G$ 是 crystalline representations 的 Tannakian category 中的 unipotent group：其 coordinate algebra 从 $V^*,Z^*$ 的 symmetric powers 构造，群律是原 crystalline bilinear map。令
$\mathcal D=D_{\rm cris}(G)$，$f$ 为 $F$ 的 residue degree。

Sakugawa 的两个条件在这里可逐项核：

1. **Non-neg。** Lie algebra 的 filtration weights 全负，所以 coordinate algebra 的 weights 全非负；
$\operatorname{Fil}^0\mathcal O(\mathcal D_F)=\mathcal O(\mathcal D_F)$。
而 $\operatorname{Fil}^0\mathcal D_F=1$。
2. **Bij。** Lang map $x\mapsto\varphi^f(x)x^{-1}$ 是 polynomial isomorphism。先在 $V$ 解 $(\varphi^f-1)v$，再在 $Z$ 解 $(\varphi^f-1)z$ 加已知的二次项；两线性算子都由上表无 eigenvalue 一而可逆。

此外，$G$ 及其 filtered-$\varphi$ 实现作为底域上的代数群都是 split unipotent；沿中心向量群逐次用 $H^1(k,\mathbb G_a)=0$，它们的普通代数 torsors 都有底域点。因此 Theorem 3.9 所需的 $\omega_{\mathbb Q_p}$-trivial 和 $\omega_F$-trivial 也满足（亦见原文 Lemma 3.1、Remark 6）。

使用其 Theorem 3.9 的 **unipotent** 分支（Proposition 3.3(b)，不使用 ordinary 分支），有自然参数化
$$
H^1_f(F,G)\simeq \mathcal D_F(F).
\tag{1147.44}
$$
Theorem 3.10 保持 central pushout 及中心作用。投影
$\mathcal D_F\to D_{\rm dR}(V)$ 是满射，所以每个 $V$ 的 crystalline torsor 都有一个 crystalline $G$-lift。

现在取实际 $P_E$。它的 abelian quotient 由 (1147.43) 是 crystalline。选上述 crystalline lift $P'_E$。两个 lift 的差来自 $H^1(F,Z)$；由于该群也等于 $H^1_f(F,Z)$，中心 twisting 保持 crystalline。故
$$
\boxed{\ P_E\text{ 是同一原 tower 的 crystalline }
        G\text{-torsor。}\ }
\tag{1147.45}
$$
这并未计算 $P_E$ 在 (1147.44) 中的坐标。它证明可以对这个实际 fibre 使用 crystalline comparison，且没有先换成另一个 rational torsor。

## 14. 未分歧基域上的原整格与模 p Heisenberg quotient

本节另假设 $F/\mathbb Q_p$ **未分歧**。不能在取得全 $p$-level 标记所需的 ramified field 上照用此假设。

### 14.1 一个携带原 torsor 的有限维格

令 $V_{\mathbb Z_p},Z_{\mathbb Z_p}$ 为 (1147.41) 的原格。定义
$$
W_{\mathbb Z_p}=\mathbb Z_p\oplus V_{\mathbb Z_p}\oplus Z_{\mathbb Z_p}.
$$
其秩为 $43$。$G_\infty$ 的 faithful affine representation 是
$$
R(v,z)=
\begin{pmatrix}
1&0&0\\
v&I_V&0\\
z&\mathfrak b_\infty(v,-)&I_Z
\end{pmatrix}.
\tag{1147.46}
$$
直接相乘给
$R(v,z)R(v',z')=
 R(v+v',z+z'+\mathfrak b_\infty(v,v'))$。
因此这不是只在 associated graded 上的表示。

选择 (1147.41) 的一个 fibre point，把实际 cocycle 记为 $c_\sigma\in G_\infty$。以
$R(c_\sigma)$ 复合原 $V,Z$ 的 coefficient action，得到同一个
$G_F$-stable $\mathbb Z_p$ lattice $W_{E,\mathbb Z_p}$。改变 point 只给由原 $R(G_\infty)$ 诱导的同构；原 affine hyperplane、flag 和 quotient maps 一并保留。

由 (1147.45)，$W_E=W_{E,\mathbb Z_p}\otimes\mathbb Q_p$ 是 crystalline。它的 filtration graded pieces 是 $\mathbb Q_p,V,Z$，所以全部 weights 在 $[-14,0]$。这只是 **幅度 $14$**，不随 $p$ 或 $E$ 增长。

### 14.2 Fontaine–Laffaille 恢复的是这个格

对未分歧 $F$，Fontaine–Laffaille 的整比较在长度 $\le p-2$ 的区间内给出 crystalline stable lattices 与 strongly divisible filtered modules 的等价，并与 quotient mod $p^n$ 相容。以对偶约定将上述 filtration 区间改写为 $[0,14]$；因 $p>37$，它严格落在该范围内。于是 **实际**
$W_{E,\mathbb Z_p}$ 对应一个 strongly divisible lattice，约模 $p^n$ 后恢复的正是原 $W_{E,\mathbb Z_p}/p^n$，而非任意选取的 isogenous lattice。

精确格这一点可按原文的 finite-level 与 lattice 两步读：有限扭部分的 exactness/full faithfulness 见 Theorems 3.3、6.1，整格及其有限 quotients 见 §§7.14–7.15；Proposition 7.8 与 Theorem 8.4 接 crystalline rational realization。在短区间内，simple objects 的表示是 simple，故 exact fully faithful image 对 subobjects、quotients 关闭；由此在一个 strongly divisible lattice 的有界 $p$-power sandwich 中恢复任意同一 rational representation 的 stable lattice。这里保留原给定的格，不用一句 rational crystallinity 代替整比较。

若原点还带有实际 $N_{\rm ns}(p)$-structure，§4 的 $q_I$ 及 $(a,b,h)$ 在模 $p$ 上是原 $G_F$-equivariant maps。它们给 (1147.46) 的真实 quotient
$$
(s,v,z)\longmapsto (s,a(v),b(v),h(z))
 \in \mathbb F_p\oplus L_3\oplus L_5\oplus L_8.
\tag{1147.47}
$$
(1147.17) 准确保证此线性 map intertwines 实际 twisted affine actions。它满射，且连同 affine hyperplane $s=1$、flag 及三个指定 graded lines，恢复的就是原
$\mathscr Y_{\rm mom,E}$ 的 Heisenberg cocycle。

因此 (1147.47) 可在 Fontaine–Laffaille 的有限扭范畴中读取同一个 quotient。它没有制造一个
$I\in\operatorname{End}(T_pE)$：$q_I$ 只在最后的模 $p$ quotient 使用。所需的 bilinear structure 也保持在 short-weight 范围；(1147.46) 的至多二次 tensor relations 幅度至多 $28<p-2$，没有偷偷调用任意高 tensor power 的无界整比较。

## 15. 此局部桥支付的范围与 primary

现在已有三个严格分开的对象，并已支付它们的对应：

- 同一 theta 的 compatible integral $\mathscr P_\infty$；
- 每个 good elliptic point 上其 actual crystalline rational fibre；
- 在未分歧基域上携带该 fibre 的原 stable lattice、它的有限 reduction 和 (1147.47) 的实际 Heisenberg quotient。

这一步仍不声称已写出相对 strongly divisible module 的 Gauss–Manin/Frobenius 矩阵，也不声称某个 supersingular coarse disk 的中央首项是单位。逐点晶体性与实际相对 jet 是两项不同输入。特别，$\mu_3$ 特殊点的 coarse 三阶变化仍须在原全 coefficient system 中计算，不能由 ordinary $E_{10}=E_4E_6$ 的 fine 简单零直接替代。

本节使用的已刊 primary：

- S. Bloch、K. Kato，*L-functions and Tamagawa numbers of motives*，1990，[全文](https://virtualmath1.stanford.edu/~conrad/BSDseminar/refs/BKTamagawa.pdf)，Corollary 3.8.4、其后 (3.8.5) 与 local Euler characteristic（印刷355–356页）。本篇在 (1147.42) 逐项排除 H⁰ 和 dual-twist H⁰ 后使用其完整维数式。
- K. Sakugawa，*On a non-abelian generalization of the Bloch–Kato exponential map*，*Math. J. Okayama Univ.* 59 (2017), 41–70，[全文](https://www.math.okayama-u.ac.jp/mjou/mjou59/_04_Sakugawa.pdf)，Definition 8、Proposition 3.3(b)、Theorems 3.9–3.10（印刷49、52、57–58页）。Non-neg、Bij 与 unipotent 条件在 §13.2 明确验证；特别不借 ordinary 条件。
- J.-M. Fontaine、G. Laffaille，*Construction de représentations $p$-adiques*，*Ann. Sci. ÉNS* 15 (1982), 547–608，[正式全文](https://www.numdam.org/item/10.24033/asens.1437.pdf)，Theorems 3.3、6.1、§§7.7–7.15、Theorem 8.4：有限层、整格和 crystalline realization 的同一比较。§14 始终保未分歧底和幅度 $14$，不使用 ramified full-level field 的虚假 Fontaine–Laffaille 假设。

本节没有数学程序执行，也没有给出一个未经计算的 local obstruction 值。


## 16. 完整整塔从函数域唯一补回全部 noncusp 点

本节给实际 four-line / Manin filling 的一个补点准则。它不从有限层 cup 消失制造一座塔，而是说明：**一旦在原函数域上构造了同一个兼容整塔，所有额外的水平删点自动补回。** 各层构造时删掉的有限集合可以随层数增长，不需要它们有有限的共同并集。

### 16.1 精确输入与中央惯性

先在一个光滑几何连通的 fine modular curve $Y$ 上论证；其底域 $k$ 是数域，universal elliptic curve $E/Y$ 在全部 $Y$ 上光滑 proper，故这里尚未加入 cusps。令 $F=k(Y)$，并以本篇的同一个
$$
\mathbb H_\infty=T_pE,\qquad
Z_\infty=
 \operatorname{Sym}^{12}\mathbb H_\infty(2)
 \oplus\operatorname{Sym}^{8}\mathbb H_\infty(4)
 \oplus\operatorname{Sym}^{4}\mathbb H_\infty(6)
\tag{1147.48}
$$
及 (1147.39) 构造 $G_n,V_n,Z_n$；特别 $Z_n=Z_\infty/p^n$，群律中的 $\lambda_\infty$ 仍为 $21(1+p^4)/11$。

假设已经给出以下实际对象：

1. $F$ 上的 $G_n$-torsors $Q_n$，以及与原群约化相容的、满足 cocycle 条件的同构
   $Q_{n+1}\times^{G_{n+1}}G_n\simeq Q_n$；
2. 它们的 $V_n$-quotients 与原 $\eta_n|_F$ 的相容识别，其中 $\eta_n$ 是 (1147.40) 的原 quotient，已在 $Y$ 延伸。

这不是“对每个 $n$ 存在某个 lift”的量词，也不是只给一个 $\mathbb Q_p$-rational lift。各 $Q_n$ 的几何 fibres 是非空有限集合，约化映射满射；选一个兼容 fibre point 后，实际得到连续 cocycle
$$
c:G_F\longrightarrow G_\infty=\varprojlim_nG_n.
$$
改变这个 point 只作同一个整塔中的 coboundary。

固定任一 closed point $x\in Y$，在 $G_F$ 内选其 decomposition group $D_x$ 与 inertia $I_x$。因为原系数和 $\eta_\infty$ 都沿 $x$ 无分歧，$I_x$ 对 $G_\infty$ 的 coefficient action 平凡，而 $c(I_x)$ 落在 $Z_\infty$。cocycle 规则因此给一个真正连续群同态
$$
\rho_x:I_x\longrightarrow Z_\infty.
\tag{1147.49}
$$
对 $d\in D_x$，一般 torsor 的共轭还含 $c(d)$；这里 $\rho_x(I_x)$ 在中心，这个内共轭完全消失。因此
$$
\rho_x(d\tau d^{-1})=d\,\rho_x(\tau).
$$
它是 $G_{k(x)}$-equivariant 的同态，不能只忽略算术 decomposition action。

此处 DVR 的 residue characteristic 是零，所以几何惯性的 pro-$p$ quotient 为 $\mathbb Z_p(1)$。于是
$$
\rho_x\in
\operatorname{Hom}_{G_{k(x)}}(\mathbb Z_p(1),Z_\infty)
 =H^0(k(x),Z_\infty(-1)).
\tag{1147.50}
$$

### 16.2 权重在整塔上迫惯性为零

$E_x/k(x)$ 是一条实际椭圆曲线。选 $k(x)$ 任一不在 $p$ 上、且 $E_x$ 好约化的有限位 $v$，记 residue-field 大小为 $Q_v>1$。这种位存在，因为这里只删掉有限多个坏位。

沿 §13 的同一 geometric-Frobenius 规范，$T_pE_x\otimes\mathbb Q_p$ 的 eigenvalues 的复绝对值为 $Q_v^{-1/2}$，而 $\mathbb Q_p(t)$ 的 eigenvalue 为 $Q_v^{-t}$。因此 (1147.48) 三项都纯 weight $-16$，$Z_\infty(-1)\otimes\mathbb Q_p$ 的三个分量都纯 weight $-14$。它的每个 eigenvalue 的复绝对值都是
$$
Q_v^{-7}\ne1.
$$
所以
$$
H^0(k(x),Z_\infty(-1)\otimes\mathbb Q_p)=0.
$$
$Z_\infty(-1)$ 是无挠的 $\mathbb Z_p$ 格，嵌入其 rationalization，故
$$
\boxed{H^0(k(x),Z_\infty(-1))=0,\qquad \rho_x=0.}
\tag{1147.51}
$$
若使用 arithmetic Frobenius，所有 eigenvalues 同时取逆，仍然没有一；不能混用两种 weight 记号。

这是关于整个 $\mathbb Z_p$ 同态 (1147.49) 的结论。单独的
$H^0(k(x),Z_n(-1))$ 可以非零；不能对一个任意有限层据复绝对值直接断言无惯性。

### 16.3 逐层正规化、唯一延伸和相容性

由 (1147.51)，每个 $Q_n$ 在每个 $x\in Y$ 的 inertia 都平凡。对 $Y$ 在 $Q_n$ 的各有限 separable function fields 中取正规化；每个分量都支配 $Y$，所以没有附加的孤立 vertical 分量。$Y$ 是正则曲线，有限扩张在每个 closed-point DVR 无分歧，故这个正规化是 finite étale。

原 $G_n$-action、torsor identity、quotient map 和各层 transition maps 都在泛点已给定。正规底上 finite étale covers 的 restriction fully faithful，所以这些 maps 唯一延伸；其等式在泛点相同便在整底相同。于是得到唯一的相容塔
$$
\overline Q_n/Y,\qquad
\overline Q_\infty=\varprojlim_n\overline Q_n,
\quad
\overline Q_n\times^{G_n}V_n=\eta_n.
\tag{1147.52}
$$
这一步也可以用 Zariski–Nagata purity 的一维情形；准确 primary 是
[Stacks Project, Tag 0BMB, Lemma 58.21.4](https://stacks.math.columbia.edu/tag/0BMB)。
这里使用实际有限正规化、正则底与全部 codimension-one 无分歧，未以“normal”单独替代 étaleness。

这个证明逐个 $x$ 进行。即使第 $n$ 层最初只在 $Y\setminus D_n$ 上显示，其 $D_n$ 随 $n$ 改变，也无妨；在函数域中已经给定的兼容塔保证 (1147.49) 对每个固定 $x$ 都有同一个 inverse limit。相反，若只是对各 $n$ 分别选一个不相容的解，就没有 (1147.49)，不能使用本结论。

### 16.4 原 stack 的识别与后续计算的范围

若构造起初是在 $\mathcal M_{\mathbb Q}$ 的 generic point 上，保留原 stack 的 generic descent data，再拉到 level $3$ 或 $4$ 的 fine cover 作上述论证。fine cover 及其 overlap 都正规，generic descent isomorphisms 因 (1147.52) 唯一延伸，故塔下降回整个 $\mathcal M_{\mathbb Q}$。这里未把 generic residual gerbe 或 elliptic automorphisms 丢掉，也没有声称 fine cover 上的 $H^1(Y,Z_n)$ 都为零。

回到原 universal stack 后，(1147.36)–(1147.40) 给
$$
H^0(\mathcal M_{\mathbb Q},V_n)
 =H^0(\mathcal M_{\mathbb Q},Z_n)
 =H^1(\mathcal M_{\mathbb Q},Z_n)=0.
$$
所以固定原 quotient 的延伸在每一层唯一到唯一同构，准确为
$\mathscr P_n|_{\mathbb Q}$；这些同构因唯一性相容。因而
$$
\boxed{\overline Q_\infty\simeq
       \mathscr P_\infty|_{\mathcal M_{\mathbb Q}}
       \quad\text{保持原 quotient、群律和全部层约化。}}
\tag{1147.53}
$$
这给指定 filling 的具体后续接口：需要构造的是真正的原
$G_\infty$-torsor（或同一连续 integral cocycle），并支付实际 theta roots、算术 paths、五项式和 corestriction 的相容性。一旦这些在原 generic point 支付，人工加入的 noncusp lines 不再需要逐点另选中心规范。

本节不从形式 Manin relation、单个 $K_2/p$ 消失、有限层解或 rational regulator 自动得到该输入；也不计算 $F_0$ 的 $z_{12}$。它没有证明一个任意 generic construction 的 arithmetic vertical 无分歧或 cusp 无分歧。只有先由 (1147.53) 识别为已成的原塔后，才可消费本篇先前已付的 $S_0$ 整来源，以及 R1147 §4 的原模 $p$ Cartan pushout；不能跳过这个识别直接把 ramified full-level coordinates 当未分歧 FL frame。

本节是纸面证明，没有数学程序执行。


## 17. 全部非零点的真实分布与连续 moment

本节仍取 $p>37$，并在 $\mathcal M_{\mathbb Q}$ 上工作。
为避免混淆，用 $r$ 表示标记及系数层数，$N=p^r$；
后文的 $\ell\in\{2,5\}$ 只是 prime-to-$p$ 的 cyclic
Hecke 辅助数。原辅助 $c$、trace-fixed theta、Tate basis
及 Kummer 次序均保持 §§8–11 的规范。

### 17.1 去掉零点 Dirac 向量的系数模

设
$$
\mathcal A_r=\mathcal E[p^r]\setminus0,\qquad
\Lambda_r^\circ=
R_r[\mathcal E[p^r]]/R_r[0],\qquad R_r=\mathbb Z/p^r.
\tag{1147.54}
$$
这里是**系数模商**，不是群环的环商：
$[0]$ 是零点的 Dirac 向量，不能把它生成的环理想拿来作商。
过渡为系数约化与
$$
[P]\longmapsto[pP],\qquad[0]=0.
$$
因此 $\Lambda_r^\circ$ 也可写成以全部非零 $p^r$-点
为基的 permutation module；当 $pP=0$ 时过渡确为零。

定义同一原 theta 的实际 Kummer 类
$$
\boldsymbol\mu_{c,r}=
\operatorname{Cor}_{\mathcal A_r/\mathcal M}
  \bigl([P]\otimes\kappa_{p^r}(\theta_c(P))\bigr)
\in H^1(\mathcal M_{\mathbb Q},\Lambda_r^\circ(1)).
\tag{1147.55}
$$
这不反除标记 cover 的 degree。
$K_1\otimes\mathbb Z_{(p)}$ 的有限分母按 §8 的
$p$ 单位幂解释。

兼容性可以在实际根 torsor 上指定，而非只写 H¹ 相等。
清除同一个 $p$ 单位分母后，若高层各槽的根为
$x_P^{p^{r+1}}=\theta_c(P)$，则对每个 $Q\ne0$ 定义
$$
y_Q=\prod_{pP=Q}x_P^p,\qquad
y_Q^{p^r}=\prod_{pP=Q}\theta_c(P)=\theta_c(Q).
\tag{1147.56}
$$
最后一式正是 (1147.24) 的原 norm。
乘积在未分裂 cover 上就是同一 finite-étale norm；
它与所有基变换、Galois 重指标及实际 Weil components 相容。
若先用了 $p$ 单位幂来表示 theta 类，再沿该幂的
Kummer-group 自同构除回。trace-fixed 等式中被清除的
prime-to-$p$ torsion 也用其唯一相容的 $p$ 次根处理，
不留下一个任选的 $\mu_{p^r}$ 相位。

落到 $Q=0$ 的 fibre 只因其系数为 $[0]=0$ 而被删除；
没有断言该 fibre 的各 theta 值或其 norm 为零。
也从不读取 $\theta_c(0)$。
两次 (1147.56) 的合成就是全部 $p^2P=Q$ 根的乘积，
所以这些 quotient-torsor 过渡严格相容。
这些过渡的群映射满射，有限几何纤维非空，
故可选兼容几何纤维点并得到严格兼容的 cocycles；
若与另一套既定根比较，仍须保留相应零次 gauge。

于是存在实际连续系数及根塔
$$
\Lambda^\circ=\varprojlim_r\Lambda_r^\circ,\qquad
\boldsymbol\mu_{c,\infty}.
\tag{1147.57}
$$
在一个几何 Tate-module frame 中，
$\Lambda^\circ$ 是 completed measure module
$\mathbb Z_p[[T_pE]]/\mathbb Z_p[0]$。
此处仍只用其系数模结构。
它表示原 norm-compatible Kummer torsors 的逆极限，
不是在每层另挑一个相容性未付的 cohomology 类。

### 17.2 连续 moment 不需要提升有限标签

对 $d\ge1$，有限系数 map
$$
\operatorname{mom}_{d,r}:\Lambda_r^\circ
 \longrightarrow\operatorname{Sym}^d\mathcal H_r,\qquad
[P]\longmapsto P^d
\tag{1147.58}
$$
因 $0^d=0$ 而有定义。
其与 $P\mapsto pP$ 的过渡严格相容，故给连续 map
$\operatorname{mom}_{d,\infty}:\Lambda^\circ
\to\operatorname{Sym}^dT_p\mathcal E$。
这里只在逆极限中得到真正的 Tate-module 权；
没有把某个有限 $P\in E[p^r]$ 任意提升为 $T_pE$ 向量。

对 $d=4,8,12$，置
$$
\widetilde{\mathsf M}_{d,r}
 =k_d(c)^{-1}\operatorname{mom}_{d,r*}
                         \boldsymbol\mu_{c,r}
 =k_d(c)^{-1}\operatorname{Cor}_{\mathcal A_r/\mathcal M}
          \bigl(P^d\otimes\kappa_{p^r}(\theta_c(P))\bigr).
\tag{1147.59}
$$
这些是全部非零点的矩，与原 primitive
$\mathsf M_{d,r}$ 暂作区分。
(1147.56) 给它们完整的层间过渡；
零像 fibre 的权在系数约化后是 $(pP)^d=0$。
因此不出现额外的 $p^2$ 平均或 $p^d$ norm 因子。

### 17.3 原 Tate residue 给精确比例

沿 §9 的同一 Tate chart，固定 $0<a<N$，记
$g=p^{v_p(a)}$。全部非零点现在允许每个
$b\bmod g$，所以固定 $a$ 的惯性轨道有 **$g$ 个**，
不再是 primitive 情形的 $\varphi(g)$ 个。
每个轨道仍贡献 $a^d k_N(a)/g$。
$a=0$ 的 $\mu_N$ 点在 $e_1^d$ coinvariant 中为零。
故
$$
\operatorname{res}\widetilde{\mathsf M}_{d,r}
 =k_d(c)^{-1}S_N
 =\frac{B_{d+2}}{d+2}\pmod{p^r}.
$$
这里逐项保留非单位 $a$ 的真实 orbit length；
最后一步直接消费 (1147.31)，不重新约化一个有理
Eisenstein 公式。

完整算术 H¹ 的原 residue 同构 (1147.37)，连同
(1147.32)，遂给
$$
\boxed{\quad
\mathsf M_{d,r}=(1-p^d)\widetilde{\mathsf M}_{d,r}
\quad(d=4,8,12),\quad\text{在每个 }R_r\text{ 上。}\quad}
\tag{1147.60}
$$
特别 all-vector residue 依次为 $1/252,1/132,1/12$。
它们也证明 (1147.59) 对合法辅助 $c$ 独立。
本式是原整 H¹ 中的等式；下一节另外支付实际根
representatives 的 gauge，不能在此先将该 gauge 设为零。


## 18. 与原 primitive 塔的实际群尺度及同根 gauge

### 18.1 三个中心同时保持的单位尺度

记
$$
a=1-p^4,\qquad b=1-p^8,\qquad
\lambda_0=\frac{21}{11},\qquad
\widetilde\gamma_{5,r}=a^{-1}\gamma_{5,r}.
\tag{1147.61}
$$
$\widetilde\gamma_5$ 的定义使用同一个原
$\gamma_5$-torsor 的单位倍，不改换圆单位来源。
由 (1147.38)、(1147.60)，全部非零点的矩满足
$$
\begin{aligned}
\Pi_0(\widetilde{\mathsf M}_{4,r}
                 \cup\widetilde{\mathsf M}_{8,r})&=0,\\
\Pi_2(\widetilde{\mathsf M}_{4,r}
                 \cup\widetilde{\mathsf M}_{8,r})&=0,\\
\Pi_4(\widetilde{\mathsf M}_{4,r}
                 \cup\widetilde{\mathsf M}_{8,r})
 +\lambda_0\widetilde{\mathsf M}_{4,r}
                 \cup\widetilde\gamma_{5,r}&=0.
\end{aligned}
\tag{1147.62}
$$
这里 $\lambda_\infty=(b/a)\lambda_0$，
并非在高层把原 $1+p^4$ 因子删掉。

令 $\widetilde{\mathcal G}_r$ 使用 (1147.39) 的相同
三个 coefficient modules，但第三 bilinear 系数取
$\lambda_0$。则
$$
\boxed{\quad
(x,y,t;z_0,z_2,z_4)\longmapsto
(ax,by,at;\,abz_0,abz_2,abz_4)
\quad}
\tag{1147.63}
$$
是 $\widetilde{\mathcal G}_r\to\mathcal G_r$ 的实际群同构。
前三 contraction 均乘 $ab$；
修正项准确满足
$a^2\lambda_\infty=ab\lambda_0$。
故它保持完整有序群律，不只保持其 associated graded。
这些同构与所有系数约化相容，且第一层就是恒等尺度。

### 18.2 从真实原根读取唯一零次修正

取 (1147.56) 的兼容纤维点，记其 moment cocycles 为
$\widetilde a_{d,r}$；原 primitive cocycles
$a_{d,r}$ 使用 R1160 §8 已固定的同一根规范。
令
$$
e_{d,r}=(1-p^d)\widetilde a_{d,r}-a_{d,r}.
$$
由 (1147.60)，这是一个实际 coboundary。
其零次原像不是新输入：对原几何群
$N=\pi_1(\overline{\mathcal M})$，使用 R1160 (1160.30)
的同一个明确反差分
$$
\rho_{d,r}=\mathcal I_d(e_{d,r}|_N),\qquad
d\rho_{d,r}=e_{d,r}.
\tag{1147.64}
$$
为明确其原数据，令
$f(Z)=e_{d,r}(T)(Z,1)$，
$T:(X,Y)\mapsto(X+Y,Y)$、
$T':(X,Y)\mapsto(X,Y+X)$，则
$$
\begin{aligned}
\rho_*&=Y^d\sum_{j=0}^{d-1}(\Delta^jf)(0)
                         \binom{X/Y}{j+1},\\
\rho_{d,r}&=\rho_*+
 [X^d]\{e_{d,r}(T')-(T'-1)\rho_*\}\,Y^d .
\end{aligned}
$$
所有分母仅为 $1!,\ldots,d!$，均是 $p$ 单位。
这只读取两条原路径上的实际 root cocycles。
已知 $[e_{d,r}]=0$ 保证它是全算术 coboundary；
$N$-invariants 为零使几何原像唯一，
所以由上式得到的同一个 $\rho_{d,r}$
也解全部算术群上的等式。
公式与约化交换，故 $\rho_{d,r}$ 自身严格兼容。

对 (1147.63) 后的代表，置
$\rho=(\rho_{4,r},\rho_{8,r},0)$。
第三坐标因为按 (1147.61) 取同一单位倍而无新相位。
若其 cocycle 是 $(v_\sigma,h_\sigma)$，用
$q=(-\rho,0)$ 作 $q^{-1}c_\sigma\sigma(q)$，
中央项必须同时改变为
$$
\begin{aligned}
v'_\sigma&=v_\sigma-d\rho(\sigma),\\
h'_\sigma&=h_\sigma+\mathfrak b_r(\rho,v_\sigma)
 -\mathfrak b_r(v_\sigma,\sigma\rho)
 -\mathfrak b_r(\rho,d\rho(\sigma)).
\end{aligned}
\tag{1147.65}
$$
这里 $\mathfrak b_r$ 正是原 (1147.39)，包括
$\lambda_\infty$；公式在三个中心同时成立。
这支付原 quotient 的实际同根运输，
没有由 H¹ 一维性忽略任何中央二次项。

(1147.62)–(1147.65) 也给全部非零点塔在 $S_0$
上的同源整延拓：先沿已证明的原 primitive torsors
及群同构运输，再消费 §11 的唯一性。
不由此宣称下节每个 auxiliary-$\ell$ subgroup cover
在整 $S_0$ 上也处处 étale。


## 19. 全层实际四线来源、兼容相关塔与未平滑最高子商

### 19.1 标记层与 raw 根层分别保留

固定一个标记层 $r$。在本小节中，raw Kummer 根的
层数另记为 $s$；先构造全部 $s\ge1$ 的固定函数整塔，
之后才取 $s=r$ 并加 $R_r$ 的 moment 权。

令
$$
\mathcal I_r=(\mathcal E[p^r]\setminus0)^2,\qquad
\mathcal J_r=\{(P,Q)\in\mathcal I_r:P\ne Q\}.
\tag{1147.66}
$$
对 $\mathcal J_r$ 上的三角形
$(P,-Q,Q-P)$，三个点都非零且阶为 $p$ 的幂。
R1157 §§2–8 的三函数构造只使用这三个条件：
三点和为零、非零、其阶与辅助 $\ell$ 互素。
所有 principal 化与分裂的分母来自 $\ell$、$2,3$；
未使用标记点恰好阶 $p$。
因此同一真实 triangle、原 $-\ell^{-8}$ 尺度和
同根/Cor 修正逐字适用于这些 $p^r$-点。
取 $\ell=2$ 时消费 R1157 §10 的同一实际函数；
取 $\ell=5$ 时用原 §§1–8。

相应 theta 值在标记曲线的全 noncusp 上是单位：
非零 $p$-power 点不落在 $\mathcal E[\ell]$。
每个 raw source 先保留完整无挠
$\mathbb Z_p(2)$ 中心及全部根层 $s$，
故 R1157 (1157.22) 的水平惯性证明仍适用。
这一步不把有限 $\mu_{p^r}$ 的不变量当成零。

随后按 R1158 §5，在实际 $\mathcal I_r,\mathcal J_r$
的每个连通 generic branch 上构造 raw source，
延伸后作 Weil restriction，再沿同一个实际 even-unit
quotient 作对角拉回。
这不反除标记 cover 的 degree；
在 $r>1$ 时也没有要求点对是自由基或 primitive。
保留全部 Weil components，算术作用由真实重指标给出。

### 19.2 同一个整多项式支付全部高层双线性项

R1158 (1158.7)–(1158.9) 的
$$
P(X,Y)=X^4Y^8=(1+S)A+(1+U+U^2)B
\tag{1147.67}
$$
是 $\mathbb Z[1/6]$ 上的多项式恒等式。
所以它可直接在
$\operatorname{Sym}^{12}\mathcal E[p^r]$ 中读取。
$B$ 的因子 $[XY(X-Y)]^3$
仍在 $X=0,Y=0,X=Y$ 时严格为零；
这不是 primitive indicator 的近似。
R1158 的 even-unit norm 同时保留，
moment 求和仍按 $P$ 和 $-P$ 各计一次，
故两槽的原 factor $2$ 都不改变。

对固定 $r$ 的 raw 根塔先取 $s=r$，
再用这些 **$R_r$ 中真实 tautological tensors**
作中心 pushout。
R1158 (1158.17) 的逐槽重指标因而原样给出
完整 ordered bilinear identity。
得到实际
$\mathcal G_{\ell,r}^{\rm corr}$-torsor
$\mathscr Q_{\ell,r}^{\rm corr}$，
其中心为 $\operatorname{Sym}^{12}\mathcal H_r(2)$，
群律仍是
$$
b_\ell(v,v')
 =\Pi_0(x,y')-\operatorname{Tr}_C\Pi_0(x_C,y_C').
$$
其 quotient 是
$$
X_{\ell,d,r}=\sum_{P\ne0}P^d\kappa_{p^r}(\theta_\ell(P)),
\qquad
X'_{\ell,C,d,r}
 =\sum_{P\ne0}P^d\kappa_{p^r}(\theta'_{\ell,C}(P)).
\tag{1147.68}
$$
所有求和、同子群乘积、根相位和 corestriction
保留 R1158 的原次序。
这里没有把有限权任意提为 Tate-module 权。

### 19.3 quotient 的 norm 过渡先付，中心才用唯一性

同一 trace-fixed 规范给
$[p]_*\theta_\ell=\theta_\ell$、
$[p]_*\theta'_{\ell,C}=\theta'_{\ell,C}$，
因为 $(p,\ell)=1$ 且 $[p]$ 置换原 $\ell$-division
及同一 $C$。
这也是 R1157 §2 的原 norm 条件；
可能的 $24$-torsion 按 (1147.56) 的规范处理。

因此 (1147.56) 的根乘积公式同时给 (1147.68)
的实际 quotient-torsor 过渡。
$\mathcal C_\ell/\mathcal M_{\mathbb Q}$ 在全部 $r$
保持同一个辅助 cover。
先固定这些 norm 过渡，才能比较
$\mathscr Q_{\ell,r+1}^{\rm corr}\bmod p^r$
与 $\mathscr Q_{\ell,r}^{\rm corr}$。

由 (1147.36)，在整个 $\mathcal M_{\mathbb Q}$ 上
$$
H^0(\mathcal M_{\mathbb Q},
       \operatorname{Sym}^{12}\mathcal H_r(2))
 =
H^1(\mathcal M_{\mathbb Q},
       \operatorname{Sym}^{12}\mathcal H_r(2))=0.
$$
两个已经实际构造的 lifts，固定其 quotient 及上述
norm 标识后，因 H¹ 消失有同构，因 H⁰ 消失只有一个同构。
三层过渡的两种合成都是同一 quotient 标识之上的同构，
故由唯一性相等。于是
$$
\boxed{\quad
\mathscr Q_{\ell,\infty}^{\rm corr}
 =\varprojlim_r\mathscr Q_{\ell,r}^{\rm corr}
\quad\text{是真正兼容的整相关 torsor。}
\quad}
\tag{1147.69}
$$
这不声称不同 $r$ 所选的任意四线分解或辅助根
在 raw 各槽上逐项相同。
实际兼容性发生在已完成全算术下降和完整
bilinear pushout 的对象上。
它也不从各层零 cohomology classes
直接抽取一个尚未构造的 inverse-limit lift。

### 19.4 接到原 primitive 最高整子商

R1158 (1158.21) 的同一 theta 函数等式，
在每个 $R_r$ 上都给
$$
X_{\ell,d,r}=(\ell^2-\ell^{-d})
                  \widetilde{\mathsf M}_{d,r},\qquad
X'_{\ell,C,d,r}
 =\ell\widetilde{\mathsf M}_{d,r}^{\,C}
       -\ell^{-d}\widetilde{\mathsf M}_{d,r}.
\tag{1147.70}
$$
$\psi_C^{-1}$ 在 $E[p^r]$ 上存在，故运输方向不变。
同一单位关系的兼容根给 R1158 (1158.23) 的实际
$\rho$，中央按 (1158.24) 同时运输。
该公式只反除 $k_d(c)$，从不反除可能为零的
$\ell^2-\ell^{-d}$。

先将各 $d=4$ 槽乘 $a$、各 $d=8$ 槽乘 $b$、
中心乘 $ab$，再用 §18 的同根 gauge，
即可把 (1147.70) 的 quotient 认到原 primitive
$a_{4,r},a_{8,r}$ 及其真实 isogeny pullbacks。
R1159 的全部 crossed projection-formula、
norm-root 相位及有序修正是实际整数 cochain 公式，
只用 $\ell$、$2$ 和 $k_d(c)$ 的单位逆；
故同样在每个 $R_r$ 成立，而不只在第一层。

写原
$\Omega_r=\Pi_0(a_{4,r}\cup a_{8,r})$，
则所得实际 source 满足
$$
dh_{\mathcal V_\ell,r}=-\mathcal V_\ell\Omega_r,\qquad
h_{\mathcal V_\ell,r}=h_{{\rm corr},r}+J_{\ell,r},
\qquad
\mathcal V_\ell=(\ell^4+\ell^{-11})-\ell^2T_\ell.
\tag{1147.71}
$$
每项 $J_{\ell,r}$ 保留 R1159 的原陪集及根规范。
原 $a_{12,r}$ 的同一 norm identity 和单位 residue
又给 $T_\ell$ 在几何 H¹ 上的精确标量
$\ell+\ell^{-12}$；
通过 (1147.37)，在对应算术 H² 上也是此标量。
所以
$$
v_\ell=\ell^{-11}(\ell-1)(\ell^{14}-1),\qquad
B_{\ell,r}=
 \mathcal B_{12,2,r}\bigl((\mathcal V_\ell-v_\ell)\Omega_r\bigr)
\tag{1147.72}
$$
是 R1160 §8 的同一个实际构造，
$dB_{\ell,r}=(\mathcal V_\ell-v_\ell)\Omega_r$。

$p\ne43,127$ 时取 $\ell=2$；
这两例取 $\ell=5$。
R1160 已核 $v_\ell$ 在相应情形为单位，故
$$
\boxed{\qquad
h_{0,r}=\frac{h_{\mathcal V_\ell,r}+B_{\ell,r}}{v_\ell},
\qquad dh_{0,r}=-\Omega_r.
\qquad}
\tag{1147.73}
$$
取 (1147.69) 的兼容纤维点并保相同的
norm-root gauges，R1159 的整数修正和
R1160 的约化自然性使本式逐层相容。
等价地，完成每层实际构造后，
同一原 quotient 上的 H⁰/H¹ 消失给唯一相容标识。
所以它确给原 $\mathscr P_\infty$ 的最高
$\operatorname{Sym}^{12}T_pE(2)$ 子商。
此处只认定这一实际四线来源的最高子商；
没有把未构造的其它 raw contractions 添入来源。

### 19.5 已付与仍须读取的准确边界

本节完成了三件此前分开的实际事情：
原 theta 的连续分布与 moment、全 $p^r$ 标记的
raw-to-correlation pushout、与原 primitive 最高整塔的
同根及未平滑比较。
全过程没有反除标记 degree，没有任意提升有限标签，
也没有将一个模 $p$ 的形式 filling 当成
$\mathbb Z_p$ 系数构造。

但这并不允许交换任意 period limit。
对每个有限标记层的原 primitive 作 rational
$B_{\rm st}$ 比较，与对 (1147.69) 的逆极限、
有限维 moment 及原 $43$ 维整格作相同比较，是不同的门。
实际求 $F_0$ 时仍须证明所使用的 period 表达式、
同根/中央 gauges、PD pullback 及极限在所需精度相容；
不能逐个约模后删掉 R1155 (1155.87) 的 normal carry。
本节也不提供 R1160 中一般 Frobenius
conjugating-path 的数值。

第一层的原 Cartan $q_I$ 仍按 §4 在模 $p$ 后使用。
本节没有把 $I\in\operatorname{End}(E[p])$
提升为 $T_pE$ 的算子，没有给新的 $z_{12}$ 数值或
中央单位，也不改变一般 $p$ 主目标的 OPEN 状态。

新增来源均为实际已成来源的明确延长：
R1147 (1147.24)、(1147.29)–(1147.37)；
R1157 的原 triangle、固定函数整根塔及水平延伸；
R1158 §§2–7 的共同 quotient、全算术 Weil restriction
和 ordered 双线性恒等式；
R1159 的全部实际 cochain 修正；
R1160 §§4、8 的整反差分、算术构造及约化自然性。
本节全部为纸面证明，无数学程序执行。
