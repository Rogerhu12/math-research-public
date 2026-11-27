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
