# R1148：原规范 Heisenberg 覆盖的尖点纤维与负一 Frobenius 分支

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面。** 以下先取 $p>691$。R1147 的同一个规范覆盖在每个原 cusp 的算术纤维，可由两个原圆单位类 $\gamma_5,\gamma_9$ 的唯一全局 Heisenberg 提升准确给出。没有另选曲线上的中心 twist，也不以无分歧代替纤维分裂。

当 $\ell\equiv-1\pmod p$，原 abelian 标签确实全灭，但这个覆盖的中心读数仍可见。本文给出完整的同 cusp 判据。在 $\gamma_5,\gamma_9$ 均非零的明确条件下，得到每个全局标签的准确允许素数密度，并得到正密度素数，同时排掉全部全局标签的全部 cusp 圆盘。这些结论只约束非整 $j$ 分支，不排 affine 点，不给足够小的辅助素，也不证明分母为空。

## 1. 同一圆单位及所有需要的低偶权消失

保持
$$
S_0=\operatorname{Spec}\mathbb Z[1/p],\quad
K=\mathbb Q(\zeta_p),\quad F=K^+,\quad
S=\operatorname{Spec}\mathcal O_K[1/p],\quad
L_r=\mu_p^{\otimes r}.
$$
对 $d=4,8$ 使用 R1144 的原类
$$
\epsilon_d=\sum_{b\in\mathbb F_p^\times}
 b^d\kappa(1-\zeta_p^b),\qquad
\gamma_{d+1}|_S=\epsilon_d\otimes\zeta_p^{\otimes d}.
\tag{1148.1}
$$
$\epsilon_d$ 的角色为 $\omega^{-d}$；$\Delta$ 的阶 $p-1$ 可逆，故
$\gamma_5\in H^1(S_0,L_5)$、$\gamma_9\in H^1(S_0,L_9)$
都唯一下降。这些是原 $p$-unit 类，不在此预设非零。

R1146 §4 的 Kummer/奇单位/Herbrand 证明逐个适用于
$$
r\in\{2,4,6,8,10,12,14\}.
$$
准确地，所需 class-group 角色是 $\omega^{1-r}$，奇 $S$-unit 项除 $\omega$ 外全零，且 $\operatorname{Br}(S)=0$。相应 Bernoulli 数为
$$
B_2=\frac16,\ B_4=-\frac1{30},\ B_6=\frac1{42},\
B_8=-\frac1{30},\ B_{10}=\frac5{66},\
B_{12}=-\frac{691}{2730},\ B_{14}=\frac76.
$$
$p>691$ 使全部这些分子、分母为单位。Herbrand 杀掉所需整个 $p$-primary class-group 分量，Kummer 两段遂给
$$
\boxed{H^1(S_0,L_r)=H^2(S_0,L_r)=0
 \quad(r=2,4,6,8,10,12,14).}
\tag{1148.2}
$$
所有这些角色的 $H^0$ 也为零。没有假设其它偶角色、Vandiver 或 regularity。有限界 $691$ 只用于一次清楚地排除低偶权中的 Bernoulli 例外；未声称小素数的新结论。

令 $\mathcal H_{5,9}$ 的三槽为 $L_5,L_9,L_{14}$，群律仍为
$$
(x,y,z)(x',y',z')=(x+x',y+y',z+z'+xy').
$$
由 (1148.2) 的 $r=14$，同 R1146 §5 的完整 obstruction/stabilizer 论证，存在唯一的全局 torsor
$$
\boxed{\Xi\in H^1(S_0,\mathcal H_{5,9}),\qquad
 \Xi_{\rm ab}=(\gamma_5,\gamma_9).}
\tag{1148.3}
$$
这里“唯一”是 torsor 同构类；下文 cochains 可以选择代表，最终读数不依赖这种选择。

## 2. 原 Tate tangential 纤维确在 S₀ 上

取原 Tate 参数 $q$，固定相容的 $q$ 的 $p$ 次幂根，并令算术 Galois 只作用于系数。这个 tangential section 上
$$
\mathcal H_{\rm Tate}=L_0 e_1\oplus L_1 e_2,
\tag{1148.4}
$$
其中 $e_1$ 是 $q$ 根方向，$e_2$ 是真正的 $\mu_p$ 方向。式中 $e_2$ 表示该线的自然包含；用 $\zeta_p$ 写坐标时才把它平凡化。

必须先保证 R1147 的整 $\mathscr P$ 在这个 section 上仍只在 $p$ 支撑。将它拉回
$\mathbb Z[1/p][[q]][1/q]$ 上的同一 Tate curve。先加 $\zeta_p$，再加入 $q^{1/p}$，系数 $\mathcal H$ 即平凡；剩下的 torsor 群是有限 $p$-群。因此泛点的几何 $q$-惯性像为有限循环 $p$-群。取足够大的固定 $A$，作 $q=t^{p^A}$，杀掉这个惯性像。

这个 Kummer base change 在 $p$ 已可逆的底上 tame。对
$\mathcal O_K[1/p][[t]]$ 的所有 vertical generic points，原 cover 仍 étale；对 $t=0$ 的 generic point，惯性已被杀；其它 height-one points 在原 punctured open 中。该底正则且 excellent，有限正规化由 branch purity 在全部点 étale。因此 $t=0$ 的纤维是真正的 $S$ 上 finite étale torsor。

相容根上的算术 section 给出原 $\Delta$ 下降，且有限 étale 下降沿 $S/S_0$ 有效，故得到 $S_0$ 上的实际 tangential 纤维。等价地，在每个 $\ell\ne p$ 的严格局部 trait 上作上述证明，即见该 Galois 类在 $\ell$ 无分歧；不是从一个仅在 $\mathbb Q$ 上的同构擅自填整支撑。进一步换更高 $p$ 次根只拉回已 étale 的 cover，其同一 tangential 算术 restriction 不变。

R1144 的完整 Tate transfer 已付
$$
\mathsf M_4|_{\rm ar}=\iota_4\gamma_5,\qquad
\mathsf M_8|_{\rm ar}=\iota_8\gamma_9.
\tag{1148.5}
$$
这里 $\iota_d:L_{d+1}\to\operatorname{Sym}^d\mathcal H_{\rm Tate}(1)$ 是全 $e_2$ 单项式的自然包含。该结果包括非零 $q$ 轨道的算术 transfer、共同 $q$ 阶与 phase 的消去；不重新把它们设零。原第三槽仍为 $\gamma_5$。先在 $K$ 上的 full cochain 计算给 (1148.5)，再由 degree $p-1$ 的 restriction 单射下降到 $\mathbb Q$；本节的无分歧性使它成为 $S_0$ 上的等式。

## 3. 显式算术 lift 与原来源之差

R1147 的中心在 (1148.4) 下分解为
$$
\mathcal Z_{\rm Tate}=
 \bigoplus_{i=0}^{12}L_{2+i}
 \ \oplus\!
 \bigoplus_{i=0}^{8}L_{4+i}
 \ \oplus\!
 \bigoplus_{i=0}^{4}L_{6+i}.
\tag{1148.6}
$$
每个分量的 $i$ 就是 $e_2$ 的次数。不是只保留最高单项式来替代整个中心。

从 $\mathcal H_{5,9}$ 到 R1147 的 $\mathcal G_{\rm Tate}$ 定义
$$
(x,y,z)\longmapsto
\left(
 \iota_4x,\ \iota_8y,\ x;\
 \iota_{12}z,\ 0,\ \frac{21}{22}\iota_4(x^2)
\right).
\tag{1148.7}
$$
中心中的自然包含分别把 $L_{14}$ 放入
$\operatorname{Sym}^{12}\mathcal H(2)$，把 $L_{10}$ 放入
$\operatorname{Sym}^{4}\mathcal H(6)$；所以所有 twists 吻合。

完整群律可直接核：
全 $e_2$ 的 $\Pi_0$ 是普通乘积，而 $\Pi_2,\Pi_4$ 的原 contraction 含 $e_2\wedge e_2$，故为零。剩下的中心补项为
$(21/11)xx'$；它恰等于
$$
\frac{21}{22}\big((x+x')^2-x^2-(x')^2\big).
$$
因此 (1148.7) 是群同态。将 $\Xi$ 沿它推前，得到一个明确的整 arithmetic lift，其 quotient 正是 (1148.5) 与第三槽 $\gamma_5$。

R1147 的实际 $\mathscr P_{\rm ar}$ 和这个 lift 具有相同 quotient。两者之差因而属于 $H^1(S_0,\mathcal Z_{\rm Tate})$。这里 quotient 的 $H^0$ 全零：其权为 $1,\ldots,9$ 和额外 $5$，都非平凡，所以没有遗漏的 quotient automorphism 作用。

该差的所有偶 $i$ 分量恰为 (1148.2) 的低偶权，故全零。奇 $i$ 分量未设零，也无需设零；下节原 Cartan 二次型会逐项杀掉它们。这一步同时保留原 lift 可能具有的全部算术修正，而不是只挑一个好看的局部零化 cochain。

## 4. 每个原 cusp 的完整纤维公式

令 $c_h=\sigma_hc_1$，$h\in\mathbb F_p^\times/\{\pm1\}$。在同一个 Tate fixed-Weil frame 中，原 trace-zero Cartan 的 norm 型为
$$
q_h=h x^2-\delta h^{-1}y^2,
\tag{1148.8}
$$
并带有 R1147 的 $L_1$ 值域。特别它的全部偶次幂只含偶 $y$ 次数。故原中心 map
$$
z\longmapsto
 \tfrac14q_h^6z_0-\tfrac{4\delta}{11}q_h^4z_2
       +\tfrac{4\delta^2}{21}q_h^2z_4
$$
把 §3 留下的所有奇 $i$ 分量杀掉。偶分量在 cohomology 中又已经为零。因此实际规范来源与 (1148.7) 在 cusp 的推前完全相同。

写
$$
u_h=\delta^2h^{-2}\zeta_p^{\otimes(-2)}
 \in H^0(\operatorname{Spec}\mathcal O_F[1/p],L_{-2}),
\qquad k_0=\frac{8\delta^2}{11}.
\tag{1148.9}
$$
$\pm h$ 给同一个 $u_h$。其尺度也可由原 R1064/R1115 cusp 标签直接核准：
$$
A_1(c_h)=\frac{\delta^2h^{-2}}2\epsilon_4,\qquad
A_2(c_h)=\frac{\delta^4h^{-4}}2\epsilon_8 .
$$
这里用 $\xi_j=\epsilon_{4j}/m$ 及 $m=(p-1)/2$，没有新平均因子。

准确的 cusp 群同态为
$$
\boxed{\quad
\phi_h(x,y,z)=
\left(
 \frac{u_h}2x,\
 \frac{u_h^2}2y+k_0x,\
 \frac{u_h^3}4z+\frac{k_0u_h}4x^2
\right):
\mathcal H_{5,9}|_F\longrightarrow
\mathcal H_{3,5}|_F .
\quad}
\tag{1148.10}
$$
所有三槽分别落在 $L_3,L_5,L_8$。双线性项和平方项给完整群同态；第一、第二对角系数非零，中心系数也非零，所以它是群同构。原 $k_0\gamma_5$ 常数修正仍在第二槽与第三槽中，未被删掉。

因为 R1147 的 cover 在 cusp 已无分歧，tangential 纤维与其真正的 cusp residue 纤维相同。故得到
$$
\boxed{
 [Y_{{\rm mom},c_h}]
   =\phi_{h,*}(\Xi|_F)
 \quad\text{in }H^1(\mathcal O_F[1/p],\mathcal H_{3,5}).
}
\tag{1148.11}
$$
这就是原规范 cover 的实际算术纤维式。没有声称这个纤维分裂，也没有将曲线上的其它中心 twists 设零。

## 5. 负一 Frobenius 下的准确中心坐标

一般设 $\mathcal H_{a,b}$ 的两权 $a,b$ 为奇数、中心权 $a+b$ 为偶数。对 $\ell\equiv-1\pmod p$，Frobenius 在两 abelian 槽上为 $-1$、中心上为 $+1$。

若某个 unramified torsor 的 Frobenius cocycle 为 $(x,y,z)$，置
$$
\boxed{\kappa_\ell=z-\frac12xy.}
\tag{1148.12}
$$
这是选择无关的 $L_{a+b}$-值读数。证明可换用坐标
$(x,y,w=z-xy/2)$，此时群律的中心项为
$(xy'-x'y)/2$。Frobenius-twisted conjugation 可唯一清掉前两坐标，而不改变 $w$。反过来，相同 $w$ 的两 cocycles 可如此共轭。因此
$$
H^1(\mathbb F_\ell,\mathcal H_{a,b})
 \simeq L_{a+b}(\mathbb F_\ell)
\tag{1148.13}
$$
准确由 (1148.12) 给出，而两个 abelian $H^1$ 都为零。不同 $\mu_p$ frame 只按已指定 Tate weight 变换读数。

对 $\Xi$ 的该读数记为 $s_\ell\in L_{14}(\mathbb F_\ell)$。将 (1148.10) 代入 (1148.12)，平方项恰好全部抵消：
$$
\begin{aligned}
\kappa_\ell(\phi_h(x,y,z))
&=\frac{u_h^3}4z+\frac{k_0u_h}4x^2
 -\frac12\frac{u_hx}2
      \left(\frac{u_h^2y}2+k_0x\right)\\
&=\frac{u_h^3}4\left(z-\frac12xy\right).
\end{aligned}
$$
故实际 cusp 的中心读数为
$$
\boxed{\kappa_\ell(Y_{{\rm mom},c_h})
       =\frac{u_h^3}{4}s_\ell.}
\tag{1148.14}
$$
这里没有把任意 Frobenius 当作 order-two 的复共轭；一般 $s_\ell$ 可非零。

## 6. 同一全局标签、同一 cusp 的完整判据

取任意
$$
\alpha\in H^1(S_0,L_3),\qquad
\beta\in H^1(S_0,L_5),
$$
并令 $\eta(\alpha,\beta)$ 为 R1146 的唯一 global Heisenberg 提升。其在 $\ell\equiv-1\pmod p$ 的中心读数记为
$t_{\alpha,\beta,\ell}\in L_8(\mathbb F_\ell)$。

R1115 已付非整 $j$ 恰为原 cusp 圆盘，原参数有
$j=t_h^{-p}+744+\cdots$，并且有限 étale cover 的类在整个 residue disc 恒定。结合 (1148.11)–(1148.14)，得到准确等价：
$$
\boxed{\begin{split}
&\exists x_\ell\in(X\setminus\Sigma)(\mathbb Q_\ell):
 \bar x_\ell=c_h,\ v_\ell(j(x_\ell))<0,\\
&\hspace{20mm}
[Y_{{\rm mom},x_\ell}]
 =\operatorname{loc}_\ell\eta(\alpha,\beta)\\
&\quad\Longleftrightarrow\quad
t_{\alpha,\beta,\ell}=\frac{u_h^3}{4}s_\ell .
\end{split}}
\tag{1148.15}
$$
右侧成立时整个原 cusp disc 满足这个 Heisenberg 条件；否则整个 disc 被排除。若还使用 R1115 的其它 forced abelian 角色，它们在这些素数处原本全相容，故不会改变这一新增条件。其它尚未构造的更高非阿贝尔条件不在本等价范围内。

选择 $\zeta_p$ 坐标将两读数平凡化。令
$$
g_p=\gcd(6,p-1),\qquad d_p=(p-1)/g_p .
$$
$\{h^{-6}:h\in\mathbb F_p^\times/\{\pm1\}\}$ 正是非零六次幂子群，大小 $d_p$。因此存在某一个相容 cusp，恰等价于
$$
\begin{cases}
t_{\alpha,\beta,\ell}=0,&s_\ell=0,\\
4t_{\alpha,\beta,\ell}/(\delta^6s_\ell)
 \in(\mathbb F_p^\times)^6,&s_\ell\ne0,
\end{cases}
\tag{1148.16}
$$
第二行明确要求分子非零。此处分式是在同一个 frame 下的 scalar；其 frame 变化由 $h$ 的同步重标吸收，所以判据为 Galois 共轭不变量。

这是对 R1115 负一整支的新限制，不是撤销该篇关于 abelian torsors 的结论。

## 7. 非零条件下的完整 Galois 像与精确密度

本节明确增加
$$
\gamma_5\ne0,\qquad\gamma_9\ne0.
\tag{1148.17}
$$
例如原 forced-good 条件
$p\nmid B_{p-5}B_{p-9}$ 足够：分别使用 R1069/R1112 的 $j=2,4$ 原圆单位及 (1148.1) 的非零因子。公式 (1148.11)–(1148.16) 本身不需要这个门。

在 $G_K$ 上，(1148.17) 是两个非零且不同 $\Delta$-角色 $5,9$ 的 homomorphisms。因此 abelian 像满 $\mathbb F_p^2$，交换子给整个中心，$\Xi$ 的实际 $G_K$ 像为全部 $H_p$。

固定 $(\alpha,\beta)$，取其 global lift 和 $\Xi$ 的共同有限 splitting field。若 $\alpha,\beta$ 都非零，前者同理满 Heisenberg，三条 graded 角色为 $3,5,8$；后者为 $5,9,14$。共同像中，两个中心方向 $8,14$ 实际独立。

可以直接支付这一独立性。所有群均 class two、exponent $p$，换用 $w=z-xy/2$ 的 BCH 坐标后成为 $\mathbb F_p$ Lie 代数，括号即交换子。$|\Delta|=p-1$ 为单位，故可在共同像中取 $\Delta$-角色投影。权 $9$ 方向在前一个群的像必为零；它与一个权 $5$ lift 的括号给纯权 $14$ 中心。权 $3$ 方向在后一个群的像必为零；与权 $5$ 的括号给纯权 $8$ 中心。$p>691$ 保这些角色确实不同。没有假设两个全部扩张线性无交；它们可以共享权 $5$ 的 abelian 扩张。

于是，在 Frobenius 的 $\omega=-1$ coset 内，两个读数
$(t_{\alpha,\beta,\ell},s_\ell)$ 对每个固定的其它坐标均独立均匀遍历 $\mathbb F_p^2$。满足 (1148.16) 的 pairs 恰为
$$
1+(p-1)d_p.
$$
Chebotarev 因而给“存在非整 $j$ cusp disc 满足这个 Heisenberg 条件”的素集合准确 Dirichlet 密度
$$
\boxed{
\delta^-_{\alpha,\beta}
 =\frac{1+(p-1)d_p}{(p-1)p^2}
 \qquad(\alpha\ne0,\ \beta\ne0).
}
\tag{1148.18}
$$
这包括同余条件 $\ell\equiv-1\pmod p$ 本身的因子 $1/(p-1)$。

若 $\alpha=0$ 或 $\beta=0$，该 global lift 可取中心 cocycle 为零，且始终 $t_{\alpha,\beta,\ell}=0$；唯一性保证这是实际 lift 的读数。此时 (1148.16) 仅要求 $s_\ell=0$，而纯权 $14$ 中心仍均匀，所以
$$
\boxed{
\delta^-_{\alpha,\beta}
 =\frac1{p(p-1)}
 \qquad(\alpha=0\text{ 或 }\beta=0).
}
\tag{1148.19}
$$
两式尤其均不超过 $1/(g_pp)$，严格小于旧 abelian 的 $1/(p-1)$。这些是允许分母素集合的密度，不是一个固定有理数的有限分母支撑的密度。

## 8. 同时排除全部全局标签的正密度负一素数

$H^1(S_0,L_3)$、$H^1(S_0,L_5)$ 都有限：由 $S$ 上 Kummer 序列，单位模 $p$ 与 class-group $p$-torsion 均有限，再取 $\Delta$ 分量即可。允许保留全部 irregular 项。因此可以把所有 $\eta(\alpha,\beta)$ 及 $\Xi$ 放入一个有限 Galois 扩张 $M/\mathbb Q$，其中 $K\subset M$，且 $M$ 仅在 $p$ 分歧。

所有 target lifts 的共同 $p$-群仍嵌在若干 $\mathcal H_{3,5}$ 的乘积中；其 Lie 代数的角色只有 $3,5,8$。与 $\Xi$ 合成后，同 §7 的权 $9$ 与 $5$ 括号，得到一个真正元素
$$
z\in\operatorname{Gal}(M/K)
$$
其 $\Xi$ 中心坐标非零、而在全部 target lifts 上的像为恒等。并非逐候选选取不同的 Frobenius。

取 $M$ 中同一个实际复共轭 $c$。它的阶为二、$\omega(c)=-1$；(1148.12) 的中心读数为零，因为在 BCH 坐标中 $(v,w)c$ 的平方中心是 $2w$。权 $14$ 为偶数，故 $c$ 与 $z$ 交换。元素 $zc$ 因而满足
$$
s(zc)\ne0,\qquad
t_{\alpha,\beta}(zc)=0
 \quad\text{对全部 }(\alpha,\beta).
$$
按 (1148.14)，全部 cusps 的读数都非零。因此 (1148.15) 对每个全局标签、每个 cusp 都失败。

这些性质在 $\operatorname{Gal}(M/\mathbb Q)$ 共轭下不变，故 $zc$ 的共轭类由 Chebotarev 给出正密度素数。得到
$$
\boxed{\begin{gathered}
\text{在 (1148.17) 下，存在正密度 }\ell\equiv-1\pmod p,\\
\text{全部原 cusp 圆盘均不容许任何全局 Heisenberg 标签。}
\end{gathered}}
\tag{1148.20}
$$
这是同一个辅助素、同一个实际规范 cover 上的同时排除。未使用候选数很小、Bernoulli regularity 或不同条件独立的假设。

对任意实际 $x\in X(\mathbb Q)$，R1146 的 properness 使其纤维必来自某个 $\eta(\alpha,\beta)$。所以这些特定素数处 $j(x)$ 必为整。仍不能据此推断 $j(x)$ 在每个素数整，或推出一般 $p$ 的非 CM 有理点不存在。

## 9. 来源、验证与继续范围

- [R1144](R1144-original-finite-moments-and-exact-proper-cup.md)：同一有限矩、完整 Tate arithmetic cochains、原 $\epsilon_d$ 规范与 contraction。
- [R1146](R1146-original-proper-arithmetic-Heisenberg-cover.md)：底算术 $H^1/H^2$、真实全局 lift 唯一性、proper rational-section 纤维；本文只按明确低 Bernoulli 数重复其一般论证，不重算已登记窗口。
- [R1147](R1147-original-canonical-moment-Heisenberg-lift.md)：同一个整 universal lift、三中心与 norm-polar 群同态、全部 cusp 无分歧及好素位。
- [R1115](R1115-original-cuspidal-nonintegral-j-branches-and-denominator-Frobenius.md)：原 cusp 标签、宽度 $p$、整 residue discs、负一分支的全部 abelian 条件及共轭稳定 Chebotarev 判别。
- NIST DLMF，[Table 24.2.1](https://dlmf.nist.gov/24.2#T1)：本文 §1 亲读的七个准确 Bernoulli 数。
- [Stacks Project, Tag 0BMB](https://stacks.math.columbia.edu/tag/0BMB)，即 SGA 1, Exposé X, Theorem 3.1 的 branch-purity 结论；§2 明确检查正则底与所有 height-one points，不从 characteristic-zero 无分歧略过 vertical 交点。
- 原圆单位的非零充分门由 R1069/R1112 已证局部式给出；(1148.17) 未被隐去。

全文无数学程序执行。仍需处理 (1148.17) 失效的分支、有效足够小辅助素、affine 同点像、原 $p$-local 读数及完整一般素数目标；本文不把其中任一个列为已完成。
