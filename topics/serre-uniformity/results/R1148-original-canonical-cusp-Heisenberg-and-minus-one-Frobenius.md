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


## 10. 固定权 Soulé 输入：充分大 p 时去掉两个非零门

本节改用已发表的固定权定理，去掉 §7–8 在充分大 $p$ 时的附加条件。它不以数值窗口或 Vandiver 猜想代替证明。

### 10.1 一个明确绝对常数与准确角色

Soulé 的 *Perfect forms and the Vandiver conjecture*（1999），§§3.2–3.3 证明：对固定奇数 $n\ge5$，存在 $v(n)$，满足
$$
\log v(n)\le n^{224n^4},
$$
使得所有 $p>v(n)$ 都有
$$
\operatorname{Cl}(\mathbb Q(\zeta_p))[p^\infty]_{\omega^{p-n}}=0;
$$
该角色的单位模 $p$ 由相应圆单位生成。原文同时明确给出
$H^2(\mathbb Z[1/p],\mathbb Z_p(n))=0$ 及原 cyclotomic element 对 $H^1$ 的生成性。这里只使用这一固定权范围，不声称所有 even class-group 角色都零。

取明确的绝对实常数
$$
\boxed{C_{\rm cyc}=\exp\!\left(9^{224\cdot9^4}\right).}
\tag{1148.21}
$$
它大于 $691,v(5),v(9)$。对 $p>C_{\rm cyc}$，$n=5,9$ 的准确角色分别是
$$
\omega^{p-5}=\omega^{-4},\qquad
\omega^{p-9}=\omega^{-8}.
\tag{1148.22}
$$
这正是 (1148.1) 的两个原单位角色，不是把 $B_5,B_9$ 或某个相反角色替换进来。这个界极大，但本节目标是一个明确的绝对“充分大”范围，不把它当有效小辅助素界。

### 10.2 原 ε₄、ε₈ 本身是生成元

为排除定标漏洞，在完整 $E=\mathcal O_K^\times$ 中写
$\chi=\omega^{-d}$，$d=4$ 或 $8$。取原来生成
$\mathbb F_p^\times/\{\pm1\}$ 的奇整数 $a$，并使用原圆单位
$$
\eta_a=\zeta_p^{(1-a)/2}\frac{1-\zeta_p^a}{1-\zeta_p}.
$$
$\chi$ 非平凡且为偶，故 root-of-unity 项投影为零。由同一个 group-ring projector，
$$
e_\chi\kappa(\eta_a)
 =(a^{-d}-1)e_\chi\kappa(1-\zeta_p)
 =\frac{a^{-d}-1}{p-1}\epsilon_d.
$$
在 $\mathbb F_p$ 中 $p-1=-1$，所以准确为
$$
\boxed{e_\chi\kappa(\eta_a)
       =(1-a^{-d})\epsilon_d.}
\tag{1148.23}
$$
这个因子为单位，且正是 R1144 已用的原 factor，不新增一个未知比例。

所有圆单位的 $\chi$ 分量都由同一个
$e_\chi(1-\zeta_p)$ 方向生成；(1148.23) 中的 $\eta_a$ 已给单位系数。Soulé §3.3(ii) 因而明确迫
$$
\epsilon_4\ne0,\qquad\epsilon_8\ne0.
\tag{1148.24}
$$
它们在 $S$-unit 群与普通 unit 群的非平凡角色相同，因为唯一 $p$ 位的 valuation 是平凡角色。Kummer 注入与 degree $p-1$ 的 restriction 单射遂给
$$
\boxed{\gamma_5\ne0,\quad\gamma_9\ne0
 \quad\text{对每个 }p>C_{\rm cyc}.}
\tag{1148.25}
$$
因此 §7–8 的准确密度、纯中心权 $14$ 与全部 cusp 同时排除，在这个明确绝对范围内均为无条件结论。并不要求
$p\nmid B_{p-5}B_{p-9}$；两个大指标 Bernoulli 的局部条件不再是这些全局结论的前提。

### 10.3 原全局标签的维数，以及仍不能取消的局部门

Soulé 的 class-group 消失结合 Kummer sequence，还给
$$
H^1(S_0,L_5)=\mathbb F_p\gamma_5,\qquad
H^1(S_0,L_9)=\mathbb F_p\gamma_9
 \quad(p>C_{\rm cyc}).
\tag{1148.26}
$$
单位的相应非平凡 even 角色秩为一，roots of unity 不在该角色；class-group 项由 (1148.22) 全部消失。因此不是只找到一个非零向量，而是付清整个 global H¹。

对权三，Kurihara 的 *Some remarks on conjectures about cyclotomic fields and K-groups of Z*（1992），Corollary 3.8 给
$A^{[p-3]}=0$；Remark 4.3 明确给标准 cyclotomic element 生成
$H^1(\mathbb Z[1/p],\mathbb Z_p(3))$。用同一有限 corestriction/系数约化及 (1148.23)（改取 $d=2$），记
$$
\gamma_3|_S=
\left(\sum_{b\ne0}b^2\kappa(1-\zeta_p^b)\right)
 \otimes\zeta_p^{\otimes2},
$$
则对当前 $p>C_{\rm cyc}$，
$$
\boxed{H^1(S_0,L_3)=\mathbb F_p\gamma_3.}
\tag{1148.27}
$$
此处也可以由 Kurihara 的 $A^{[p-3]}=0$ 和 Soulé §3.3 证明中所写的 Mazur–Wiles 角色单位指数等式得出：同一 $\chi=\omega^{-2}$ 圆单位分量已是全 unit lattice，(1148.23) 保原非零因子。

所以 R1146/R1148 中的全部 global abelian pairs 在充分大范围内恰为
$$
(\alpha,\beta)=(a\gamma_3,b\gamma_5),
 \qquad(a,b)\in\mathbb F_p^2.
\tag{1148.28}
$$
这里的 $a,b$ 是两槽标量，不是每个高角色或全部原候选的坐标数。式 (1148.18) 用于 $ab\ne0$，式 (1148.19) 用于 $ab=0$；§8 同时排除的对象准确包括这全部 $p^2$ 个 global lifts。

**全局生成性不等于局部生成性。** 以上论证没有证明
$\operatorname{loc}_p(\gamma_3)$、$\operatorname{loc}_p(\gamma_5)$
或 $\operatorname{loc}_p(\gamma_9)$ 为单位，甚至没有据此断言它们模 $p$ 非零。R1069 中由 $B_{p-3},B_{p-5},B_{p-9}$ 控制的实际 localization 门仍必须照原条件使用。这里消掉的是 (1148.17) 的全局非零门，不是原 $p$-local 盘内论证的门。

新增 primary 来源与精确使用位置：

- C. Soulé, *Perfect forms and the Vandiver conjecture*, **Journal für die reine und angewandte Mathematik 517 (1999), 209–221**；[作者全文](https://arxiv.org/pdf/math/9812171)。亲读 §§3.2–3.3：固定权 class-group 消失、显示界及单位生成性。arXiv 版在 §3.3 重复印为“Theorem 4”；这里用节号和 (ii)/(iv) 定位，避免把两个不同陈述混为同一编号。该文引用的 Mazur–Wiles 角色指数在 §3.3 的证明中明确写出。
- M. Kurihara, *Some remarks on conjectures about cyclotomic fields and K-groups of Z*, **Compositio Mathematica 81 (1992), 223–236**；[期刊全文](https://numdam.org/item/CM_1992__81_2_223_0.pdf)，Corollary 3.8（印刷230页）、Remark 4.3（231页）及 §5 的标准 cyclotomic element。
- 本节的 (1148.22)–(1148.28) 是对原角色、原 $\eta_a$、Kummer/corestriction 和有限系数的明确接入；未执行任何数学程序，也未重跑已有 Vandiver 或 Bernoulli 数值窗口。

主目标仍未完成：现在充分大的负一分支已具有无条件的真实中心限制，仍需付所有 affine 点或足够强的全局高度/局部排除。


## 11. 全部标签由一个五维群控制，且共同尖点排除密度恰 1/p²

本节仍取 $p>C_{\rm cyc}$，所以没有 §7 的额外非零门。记
$$
\Theta=\eta(\gamma_3,\gamma_5)
 \in H^1(S_0,\mathcal H_{3,5}).
$$
对 $a,b\in\mathbb F_p$，真实群同态
$$
D_{a,b}(x,y,z)=(ax,by,abz)
$$
连同 R1146 的唯一性给
$$
\boxed{\eta(a\gamma_3,b\gamma_5)=D_{a,b,*}\Theta.}
\tag{1148.29}
$$
所以不必取 $p^2$ 个互不相关的 splitting fields；全部 global lifts 已由同一个 $\Theta$ 控制。

把 $\Theta$ 与 $\Xi$ 放在一起。它们共享同一个 $\gamma_5$ 槽；可同时选择这个 cocycle 的同一代表。共同群是明确的 fibre product
$$
\mathcal J=
\mathcal H_{3,5}\times_{L_5}\mathcal H_{5,9}.
$$
写成五槽 $(x_3,x_5,x_9,z_8,z_{14})$，其群律是
$$
\begin{aligned}
&(x_3,x_5,x_9,z_8,z_{14})
 (x'_3,x'_5,x'_9,z'_8,z'_{14})\\
&\quad=(x_3+x'_3,x_5+x'_5,x_9+x'_9,\
 z_8+z'_8+x_3x'_5,\
 z_{14}+z'_{14}+x_5x'_9).
\end{aligned}
\tag{1148.30}
$$
$\gamma_3,\gamma_5,\gamma_9$ 非零且有不同角色，故实际 $G_K$ 像向这三个 abelian 槽满射；§7 的纯中心括号又给整个 $L_8\oplus L_{14}$。所以其实际像是全部 $\mathcal J$，几何阶准确为 $p^5$。

若 $M$ 是含 $K$ 且同时劈裂 $\Theta,\Xi$ 的最小有限 Galois 扩张，则
$$
\boxed{[M:K]=p^5,\qquad[M:\mathbb Q]=(p-1)p^5.}
\tag{1148.31}
$$
它仍仅在 $p$ 分歧。该式是实际共同场的次数，不是未验证的上界，也没有把共享 $\gamma_5$ 算两次。

对 $\ell\equiv-1\pmod p$，记
$$
t_\ell=\kappa_\ell(\Theta),\qquad s_\ell=\kappa_\ell(\Xi).
$$
式 (1148.12)、(1148.29) 精确给
$$
t_{a\gamma_3,b\gamma_5,\ell}=ab\,t_\ell.
\tag{1148.32}
$$
若 $t_\ell\ne0$，则 $ab$ 遍历整个 $\mathbb F_p$，所以对任意指定 cusp，总有某个 global pair 满足 (1148.15)。若 $t_\ell=0$，全部 pairs 的中心读数都是零；它们与某个 cusp 相容恰当 $s_\ell=0$。因此
$$
\boxed{\begin{split}
&\text{没有任何 global pair 与任何原 cusp 相容}\\
&\qquad\Longleftrightarrow\quad
 t_\ell=0,\quad s_\ell\ne0 .
\end{split}}
\tag{1148.33}
$$
这是对全部 global pairs 的精确判据；实际 $p$-local 候选可能只占其中一部分，但本节未借这种缩小来增加结论。

在 $\omega=-1$ coset 内，两个独立中心坐标均匀遍历 $\mathbb F_p^2$，满足 (1148.33) 的 pair 数准确为 $p-1$；其余三个 abelian 坐标任意。结合 $1/(p-1)$ 的同余密度，Chebotarev 给
$$
\boxed{\delta\{\ell:\text{(1148.33) 成立}\}
 =\frac1{p-1}\frac{p-1}{p^2}
 =\frac1{p^2}.}
\tag{1148.34}
$$
因此 §8 的正密度在充分大范围内已经确定为 $1/p^2$，且由同一个 degree $(p-1)p^5$ 的真实场检测。不声称每个负一素数都排掉 cusps；事实上 (1148.33) 也明确给出不能这样说的原因。

式 (1148.34) 不给最小这样的 $\ell$，仍不排其余 affine 点。全部论证为原两 Heisenberg lifts 的显示群律、已付 Galois 像和 Chebotarev 计数；无数学程序执行。


## 12. 同一规范覆盖的原 affine 中央值与明确大素数界限

本节仍使用 (1147.21) 的同一个 proper cover。计数部分只需 $p>37$；涉及 §11 的全部全局标签时再取 $p>C_{\rm cyc}$。记
$$
X=X_{\rm ns}^{+}(p),\quad g=g(X),\quad
m=(p-1)/2,\quad
D_p=g+p(p-1)(g-1).
$$
固定素数 $\ell\equiv-1\pmod p$。所有以下点数均在同一个好约化 $X_{\mathbb F_\ell}$ 上，不把 cusp 计数替代 affine 计数。

### 12.1 原中央值是一个准确的 p 维 character

固定 $\zeta_p$ frame，$L_8$ 在 $\mathbb F_\ell$ 上平凡；在两个奇权槽上 Frobenius 为 $-1$。对每个
$x\in X(\mathbb F_\ell)$，记原规范 torsor 的实际读数为
$$
c_\ell(x)=\kappa_\ell(Y_{{\rm mom},x})\in\mathbb F_p.
$$
它就是 (1148.12)，没有另选 central twist。取一个非平凡 additive character
$\psi:\mathbb F_p\to\overline{\mathbb Q}_r^\times$，
其中辅助系数素数 $r\ne p,\ell$。在 $p$ 维函数空间上定义
$$
(\rho_\psi(a,b,z)f)(u)=\psi(z+bu)f(u+a),
\qquad
(Rf)(u)=f(-u).
\tag{1148.35}
$$
直接复合得到原群律中的 $ab'$，并且
$$
R\rho_\psi(a,b,z)R=\rho_\psi(-a,-b,z),\qquad R^2=1.
$$
所以它是实际半直积 $H_p\rtimes\langle\tau\rangle$ 的表示，其中
$\tau(a,b,z)=(-a,-b,z)$。这正是本好素位上原群 sheaf 的 Frobenius 作用。

在标准 delta-function 基中，$\rho_\psi(a,b,z)R$ 只有
$u=-a/2$ 一个对角贡献。因此
$$
\boxed{\operatorname{Tr}(\rho_\psi(a,b,z)R)
 =\psi(z-ab/2)=\psi(\kappa_\ell).}
\tag{1148.36}
$$
中心作用为非平凡标量 $\psi(z)$。此外，$b$ 的全部对角算子把函数空间分成互异的一维特征线，而 $a$ 的平移传递置换这些线，所以 $\rho_\psi|_{H_p}$ 不可约，且维数确为 $p$。

由原 cover 的 torsor cocycle 得到
$\pi_1(X_{\mathbb F_\ell})\to H_p\rtimes C_2$。
使用 $\rho_\psi^\vee$ 的 associated sheaf $\mathcal L_\psi$，以便支付 arithmetic/geometric Frobenius 的逆号：
geometric Frobenius 是 arithmetic $(a,b,z)\tau$ 的逆，在 dual 表示中的 trace 正好仍为 (1148.36)。故
$$
\operatorname{Tr}(\operatorname{Frob}^{\rm geom}_x
 \mid\mathcal L_{\psi,x})=\psi(c_\ell(x)).
\tag{1148.37}
$$
$\mathcal L_\psi$ 在整个 proper $X_{\mathbb F_\ell}$ 上 lisse，秩为 $p$，有限 monodromy。没有在 cusp 添加 Swan 项或漏掉它们。

### 12.2 完整 H¹ 维数与 Weil 界

R1147 已付原 cover 的全部几何 monodromy 为 $H_p$，并且在这个好素位仍几何连通。因此 $\mathcal L_\psi$ 没有几何不变量；其 dual 亦然，故
$H^0(X_{\overline{\mathbb F}_\ell},\mathcal L_\psi)
=H^2(X_{\overline{\mathbb F}_\ell},\mathcal L_\psi)=0$。

这里可直接在原 cover 上付清中间维数。对任意非恒等 deck element $h\in H_p$，finite étale 性使它无 fixed point；Lefschetz 公式给
$\operatorname{Tr}(h|H^1(Y_{\overline{\mathbb F}_\ell}))=2$。
恒等元的 trace 为
$2g_Y=2+2p^3(g-1)$。所以作为 characteristic-zero $H_p$ 表示，
$$
H^1(Y_{\overline{\mathbb F}_\ell},\overline{\mathbb Q}_r)
 \simeq
 \mathbf1^{\oplus2}\oplus
 \overline{\mathbb Q}_r[H_p]^{\oplus(2g-2)}.
$$
由于 $|H_p|$ 在系数域中可逆，finite-cover descent 是取不变量的 exact 运算。取上节的非平凡 $p$ 维 irreducible multiplicity 后，准确得到
$$
\boxed{\dim H^1(X_{\overline{\mathbb F}_\ell},\mathcal L_\psi)
 =2p(g-1).}
\tag{1148.38}
$$
这没有用 genus $g_Y$ 粗暴地代替目标 character 的维数。

在 $\mathbb F_{\ell^2}$ 上 $H_p$ 已为常值群，
$\mathcal L_\psi$ 被同一个 $Y$ 平凡化；相应 $H^1$ 是
$H^1(Y_{\overline{\mathbb F}_\ell})$ 的 isotypic multiplicity。
曲线的 Weil 定理使 $\operatorname{Frob}_{\ell^2}$ 的每个此类特征根复绝对值为 $\ell$。故 $\operatorname{Frob}_{\ell}$ 的每个特征根绝对值为 $\sqrt\ell$。这个论证只用实际 finite cover 和已知的曲线 Weil 界，不假设另一个未构造的 weight-zero sheaf。

结合 (1148.37)、非恒定系数 Lefschetz 公式和 (1148.38)，得到
$$
\boxed{\left|
 \sum_{x\in X(\mathbb F_\ell)}\psi(c_\ell(x))
 \right|\le 2p(g-1)\sqrt\ell.}
\tag{1148.39}
$$
对全部非平凡 $\psi$ 同时成立。

### 12.3 每个实际中央纤维的原点数

令
$$
N_t=\#\{x\in X(\mathbb F_\ell):c_\ell(x)=t\}.
$$
有限 Fourier 正交关系是准确等式
$$
N_t=\frac1p\left(
 \#X(\mathbb F_\ell)
 +\sum_{a\in\mathbb F_p^\times}
 \psi(-at)\sum_{x\in X(\mathbb F_\ell)}
                  \psi(a c_\ell(x))\right).
$$
逐项使用 (1148.39)，得
$$
\boxed{\left|N_t-\frac{\#X(\mathbb F_\ell)}p\right|
 \le 2(p-1)(g-1)\sqrt\ell.}
\tag{1148.40}
$$
再用原 $X$ 的 Weil 界，即
$$
\boxed{N_t\ge
 \frac{\ell+1-2D_p\sqrt\ell}{p}.}
\tag{1148.41}
$$

$\ell\equiv-1\pmod p$ 在原 cusp field $K^+$ 中完全分裂，所以全部 $m$ 个原 cusps 均在 $\mathbb F_\ell$ 有理且互异。若
$C_t=\#\{c\text{ 为 cusp}:c_\ell(c)=t\}$，则
$$
N_t^{\rm aff}=N_t-C_t,\qquad 0\le C_t\le m.
\tag{1148.42}
$$
对 $p>691$，(1148.14) 还准确算出 $C_t$：
若 $s_\ell=0$，则 $C_0=m$、其它 $C_t=0$；
若 $s_\ell\ne0$，则 $C_0=0$，且每个出现的非零 cusp 值恰出现
$\gcd(6,p-1)/2$ 次。
最后一个数来自原映射
$h\in\mathbb F_p^\times/\{\pm1\}\mapsto h^{-6}$，
并未把正负两 cusp 标签重复计数。

特别地，只要
$$
\ell+1-2D_p\sqrt\ell>pm,
\tag{1148.43}
$$
每个中央值都在原 affine locus 上出现。
这还给一个只依赖 $p$ 的简单充分界 $\ell>p^8$。为支付该界而不借未经核准的精确 genus 表，原 congruence subgroup 的 index 为
$\mu=p(p-1)/2$，cusp 数为 $m$；Riemann–Hurwitz 的 elliptic-point 两项非负，因此
$$
g\le 1+\frac{\mu}{12}-\frac m2
 =\frac{p^2-7p+30}{24}<\frac{p^2}{24}.
$$
于是 $D_p<p^4/24$。若 $\ell>p^8$，则
$2D_p\sqrt\ell<\ell/12$，故 (1148.43) 由
$11\ell/12+1>p(p-1)/2$ 立即成立。

### 12.4 第 11 节的尖点排除素数，在大范围内仍有 affine 局部点

现取 $p>C_{\rm cyc}$，并令同一个辅助素满足 §11 的准确条件
$$
\ell\equiv-1\pmod p,\qquad
t_\ell=0,\quad s_\ell\ne0.
$$
全部 global lifts 在该位的完整 Heisenberg 类都为零：
两奇权槽的 finite-field $H^1$ 为零，而 (1148.32) 给全部中心 $ab\,t_\ell=0$。与此同时 $C_0=0$。因此
$$
N_0^{\rm aff}=N_0
 \ge \frac{\ell+1-2D_p\sqrt\ell}{p}.
$$
从而
$$
\boxed{\ell>4D_p^2
 \ \Longrightarrow\
 \text{存在同一个原 affine }\mathbb F_\ell\text{ 点，
 与全部 }p^2\text{ 个 global lifts 相容}.}
\tag{1148.44}
$$
由于 $4D_p^2<p^8/144$，$\ell>p^8/144$ 是一个明确的充分界。

这也是真正的 $\mathbb Q_\ell$ 局部非空结论。取 (1148.44) 的点，$c_\ell=0$ 意味原 torsor fibre 平凡，故有 $\mathbb F_\ell$-lift 到 $Y_{\rm mom}$。原 cover smooth proper 且 finite étale，Hensel 提升给对应的 $\mathbb Z_\ell$ 点；因 reduction 非 cusp，其 $j$ 为整。全部 global target 在 $\mathbb Z_\ell$ 的 unramified 类均平凡，故这个局部点满足所有 target 的原 fibre 相容条件。

因此 §11 的密度 $1/p^2$ 不能单凭“任选足够大的该类素数”升级为 affine 排除：超过 (1148.44) 的每个这样的素数，都已有原 affine 局部点。若沿这一个 cover 寻找完全为空的 affine residue 筛，必须在 $\ell\le4D_p^2$ 的范围另付实际点值；该必要范围本身并不保证有这样的素数。继续方向是原小辅助素处的真实中央函数，或原 $p$-local 相对连接，而非重复大素数 Chebotarev 存在性。

本节新增引用：J. S. Milne, *Lectures on Étale Cohomology*, v2.21 (2013)，[作者全文](https://www.jmilne.org/math/CourseNotes/LEC.pdf)，§25 的 fixed-point formula、§26 的曲线 Weil 特征根结论与 Theorem 29.4 的非恒定系数 trace formula。原 $H_p$ 表示、Frobenius 逆号、各 multiplicity、Fourier 常数、cusp 扣除和数值幂界均在本节逐式给出。无数学程序执行，未增加或重跑辅助素扫描。
