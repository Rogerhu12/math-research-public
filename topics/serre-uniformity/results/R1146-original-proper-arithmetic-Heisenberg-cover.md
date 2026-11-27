# R1146 — 原修正角色对的 proper 算术 Heisenberg 覆盖及唯一全局中心提升

会话：Astra-serre-24b8836b-20261126。范围：所有素数 $p>37$。本文仅消费 R1144 已证明的原 proper 算术杯积，不加 regular、Vandiver、$B_{p-5}$ 或 F33 门。

## 1. 原对象、准确常数与三条下降线

记
$$
S_0=\operatorname{Spec}\mathbf Z[1/p],\qquad
K=\mathbf Q(\zeta_p),\qquad
S=\operatorname{Spec}\mathcal O_K[1/p],\qquad
\Delta=\operatorname{Gal}(K/\mathbf Q).
$$
$\mathscr X_0/S_0$ 是原完整 $X=X_{\rm ns}^+(p)$ 的 smooth proper 模型，$\mathscr X=\mathscr X_0\times_{S_0}S$。其存在及包括 $2,3$ 的光滑性、全部 finite étale cusps，已由 R1067 §§2–3 证明。

取原 R1070 的 leading-normalized 函数 $F_1,F_2$，以及 R1144 的原常数
$$
\epsilon_4=\sum_{b\in\mathbf F_p^\times}b^4\kappa(1-\zeta_p^b)
 =\frac{\beta_{\chi_2}}{1-a^{-4}},\qquad
k=\frac{8\delta^2}{11}\in\mathbf F_p^\times.
\tag{1146.1}
$$
这里 $\epsilon_4$ 是 Kummer 类的加法记号；$\delta$ 是原非平方参数，$a$ 是既定奇生成元。置
$$
A=\kappa(F_1),\qquad B=\kappa(F_2)+k\epsilon_4
 \quad\text{于 }H^1(\mathscr X,\mu_p).
\tag{1146.2}
$$
若写实际函数，第二槽为 $F_2e_4^{\tilde k}$，其中 $\kappa(e_4)=\epsilon_4$，$\tilde k$ 是 $k$ 的整数提升。不同提升只改一个 $p$ 次幂。本文没有把这个常数 twist 暗中改称原 $F_2$。

R1067、R1144 已付两槽全 $S$ 延拓及
$$
A\in H^1(\mathscr X,\mu_p)_{\omega^{-2}},\qquad
B\in H^1(\mathscr X,\mu_p)_{\omega^{-4}},\qquad
A\cup B=0\quad\text{于 }H^2(\mathscr X,\mu_p^{\otimes2}).
\tag{1146.3}
$$
这是指定 proper 算术类的零，故无需从一个 field 符号另猜 Picard lift。

在 $S_0$ 上令 $L_r=\mathbf F_p(r)=\mu_p^{\otimes r}$，视为秩一有限 étale $\mathbf F_p$-sheaf。$S/S_0$ 为次数 $p-1$ 的 finite étale Galois cover，故任意有限 $\mathbf F_p$ 系数的 restriction 精确识别为 $\Delta$-不变量。于是
$$
a_0|_{\mathscr X}=A\otimes\zeta_p^{\otimes2},\qquad
b_0|_{\mathscr X}=B\otimes\zeta_p^{\otimes4}
\tag{1146.4}
$$
唯一确定
$$
a_0\in H^1(\mathscr X_0,L_3),\qquad
b_0\in H^1(\mathscr X_0,L_5).
$$
两个右侧的角色分别是 $\omega^{-2}\omega^2=1$、$\omega^{-4}\omega^4=1$。同理 restriction 在 $H^2(\mathscr X_0,L_8)$ 单射，因而
$$
\boxed{a_0\cup b_0=0\quad\text{于 }H^2(\mathscr X_0,L_8).}
\tag{1146.5}
$$

## 2. 实际有限 étale 群及 cochain 构造

定义 $S_0$ 上的有限 étale 群 scheme $\mathcal H$：底层 sheaf 是 $L_3\times L_5\times L_8$，群律为
$$
(x,y,z)(x',y',z')
 =(x+x',\,y+y',\,z+z'+x\otimes y').
\tag{1146.6}
$$
双线性使结合律成立；逆元为 $(-x,-y,-z+x\otimes y)$。它有中心扩张
$$
1\longrightarrow L_8\longrightarrow\mathcal H
 \longrightarrow L_3\oplus L_5\longrightarrow1.
\tag{1146.7}
$$
在 $S$ 上用同一 $\zeta_p$ 平凡化后，它是阶 $p^3$ 的 Heisenberg 群，交换子为
$$
[(x,y,z),(x',y',z')]
 =(0,0,x\otimes y'-x'\otimes y).
\tag{1146.8}
$$
$p$ 为奇数，(1146.6) 的 $p$ 次幂为单位。三条算术角色严格为 $\omega^3,\omega^5,\omega^8$；中心不是常值 $\mathbf F_p$。

为了从 (1146.5) 得到真正覆盖，说明 étale $H^2$ 到连续 cochain 的接口。对任意连通 locally noetherian scheme $T$ 和有限 locally constant abelian sheaf $M$，有
$$
H^2_{\rm cts}(\pi_1^{\rm et}(T),M_{\bar t})
 \hookrightarrow H^2_{\rm et}(T,M).
\tag{1146.9}
$$
证明取全部 pointed finite étale Galois covers 的逆系。每个有限 locally constant $H^1$ 类是一个有限 étale torsor，在进一步有限 étale cover 上变零；取 Galois closure 仍变零。因此 universal pro-cover 上 $H^1$ 的直极限为零。Cartan–Leray spectral sequence 的五项正合列便给 (1146.9)。这里只用低阶单射，不宣称 $T$ 是 $K(\pi,1)$。

令 $\Pi=\pi_1^{\rm et}(\mathscr X_0)$。选代表 $a_0,b_0$ 的连续 crossed homomorphisms $a,b$。杯积的连续二余链为
$$
c(\sigma,\tau)=a(\sigma)\otimes\sigma b(\tau).
$$
由 (1146.5)、(1146.9) 及其 cup 相容性，存在连续 $L_8$-值一余链 $z$，使
$$
dz(\sigma,\tau)
 =\sigma z(\tau)-z(\sigma\tau)+z(\sigma)
 =-a(\sigma)\otimes\sigma b(\tau).
\tag{1146.10}
$$
于是
$$
\rho(\sigma)=(a(\sigma),b(\sigma),z(\sigma))
\tag{1146.11}
$$
满足 $\rho(\sigma\tau)=\rho(\sigma)\,\sigma\rho(\tau)$，恰是 $\mathcal H$ 的连续非阿贝尔一余循环。有限 étale covers 与有限连续 $\Pi$-sets 的等价，将它给为实际 torsor
$$
\boxed{\quad \mathscr Y\longrightarrow\mathscr X_0
 \quad\text{under }\mathcal H,\quad\deg(\mathscr Y/\mathscr X_0)=p^3.\quad}
\tag{1146.12}
$$
这付出了 cochain 的存在、连续性、正确负号、算术作用与有限覆盖的 representability。没有把只在函数域上的 norm witness 自动延到所有 cusps。

$\mathscr Y$ 的选择通常有歧义：固定 quotient torsor 后，中心 twists 由 $H^1(\mathscr X_0,L_8)$ 控制。后文的唯一性是底算术 scheme $S_0$ 上的唯一性，不能误改为此曲线上所有 $\mathscr Y$ 唯一。

## 3. 几何连通、全尖点与好素位

R1062 (1062.7)、(1062.9) 对 $j=1,2$ 无条件给出原非零 cuspidal $p$-torsion。原 leading 归一只乘一个 base 常数并把 divisor 乘单位 $m=(p-1)/2$，故
$$
A|_{X_{\overline{\mathbf Q}}}\ne0,\qquad
\kappa(F_2)|_{X_{\overline{\mathbf Q}}}\ne0.
$$
它们对应不同 $\Delta$-角色 $\omega^{-2},\omega^{-4}$，因此线性独立。常数 $\epsilon_4$ 的几何 restriction 为零，所以 $A,B$ 的几何 restrictions 仍独立。

在几何基本群上三个 $L_r$ 都常值。故 (1146.11) 的几何像 $G\subset H_p$ 向
$H_p/[H_p,H_p]\simeq\mathbf F_p^2$ 满射。选 $G$ 中分别映到 $(1,0),(0,1)$ 的元素；其交换子由 (1146.8) 是中心生成元。因此 $G$ 包含整个中心，且 $G=H_p$。所以
$$
\boxed{\mathscr Y_{\overline{\mathbf Q}}\text{ 几何连通}.}
\tag{1146.13}
$$

$\mathscr Y\to\mathscr X_0$ 已是 finite étale；复合 $\mathscr Y\to S_0$ smooth proper。所有几何纤维的连通分量数局部常数，因 $S_0$ 连通，所有好素位的几何纤维也连通。其泛纤维 $Y$ 满足
$$
g_Y=1+p^3(g_X-1).
\tag{1146.14}
$$
覆盖在全部 cusps 及所有 $\ell\ne p$ 处均无分歧，包括 $2,3$。无分歧不要求 cusp 纤维分裂；本文没有宣称任意 cusp 上有 rational lift。覆盖为 class $2$，不称为原需要的 class $4$ 塔。

## 4. 底算术中心的 H¹、H² 同时为零

这一步只用固定小 Bernoulli 数 $B_8=-1/30$。以 $\zeta_p^{\otimes7}$ 平凡化多出的七个 twists，restriction 给
$$
H^i(S_0,L_8)
 \simeq H^i(S,\mu_p)_{\omega^{-7}}.
\tag{1146.15}
$$
Kummer sequence 为
$$
0\longrightarrow
\mathcal O_K[1/p]^\times/
  \bigl(\mathcal O_K[1/p]^\times\bigr)^p
\longrightarrow H^1(S,\mu_p)
\longrightarrow\operatorname{Pic}(S)[p]\longrightarrow0.
\tag{1146.16}
$$
奇角色的 $S$-unit 部分除 roots of unity 的 $\omega$ 线外为零。具体地，对任意 $S$-unit $u$，$u/\bar u$ 在全部有限位的 valuation 都为零：离 $p$ 两项各为零，在唯一 $p$ 位二者相同；每个复嵌入的绝对值又为 $1$。由 Kronecker 定理它是 root of unity。因此奇投影 $(1-c)/2$ 的像只来自 roots of unity，其中模 $p$ 唯一非零线是 $\mu_p$ 的 $\omega$ 角色。$\omega^{-7}\ne\omega$，所以所需单位项为零。

Herbrand 定理的准确角色是
$\omega^{1-8}=\omega^{-7}$。$p>37$ 时 $B_8=-1/30$ 是 $p$ 单位，因此 $\operatorname{Cl}(\mathcal O_K)[p]_{\omega^{-7}}=0$。$\operatorname{Pic}(S)$ 是该 class group 的商；其相应整个 $p$-primary 部分也为零，于是 (1146.16) 给
$$
H^1(S_0,L_8)=0.
\tag{1146.17}
$$
此外，$K$ totally imaginary 且 $S$ 只去掉一个有限位，global Brauer invariant sum 的单个位和条件给 $\operatorname{Br}(S)=0$。Kummer 的下一段及同一 class group 消失给
$$
H^2(S_0,L_8)
 \simeq(\operatorname{Pic}(S)/p)_{\omega^{-7}}=0.
\tag{1146.18}
$$
这与 R1142 §4 的同一 $B_8$ base 消失相容，但 (1146.17) 还付了中心 $H^1$。未用 $B_{p-5}$，也未删任何其它 class-group 角色。

## 5. 每个全局 abelian 标签的提升唯一

对 (1146.7)，任一 $L_3\oplus L_5$-torsor 的 lifting obstruction 是两槽 cup 于 $H^2(S_0,L_8)$；可按 §2 的同一 cochain 直接计算。因此 (1146.18) 保证每对全局标签都可提升。

固定 quotient cocycle 后，任意两个提升的第三余链之差为 $L_8$-值一余循环。由 (1146.17) 此差为 coboundary，故两个提升同构。还须保 quotient torsor 的 automorphisms：因为 $L_3\oplus L_5$ 为 abelian，其 twisted automorphism sheaf 仍是自身，且
$$
H^0(S_0,L_3\oplus L_5)=0
\tag{1146.19}
$$
（$\omega^3,\omega^5$ 均非平凡）。所以没有未处理的 stabilizer quotient，准确得到 pointed sets 的双射
$$
\boxed{
H^1(S_0,\mathcal H)
 \xrightarrow{\sim}
H^1(S_0,L_3)\times H^1(S_0,L_5).
}
\tag{1146.20}
$$
这不是群同构的声明；左侧一般只作非阿贝尔 cohomology 集。

若 $x\in X(\mathbf Q)$，由 properness 它延拓为 $S_0$-section。任意固定 (1146.12) 在 $x$ 上的纤维因此给 $H^1(S_0,\mathcal H)$ 的类，且完全由原两槽 $(a_0(x),b_0(x))$ 唯一决定。曲线上的不同中心 twists 在 rational points 的全局纤维上均无差异，因为其 pullback 落入零群 (1146.17)。

这里全局 abelian 标签自身的维数、localization 像不被改写；可能的其它 irregular class-group 项仍在各自的 $H^1(S_0,L_3),H^1(S_0,L_5)$ 中。

## 6. p-local 中心恰一维及准确约束形式

在 $\mathbf Q_p$，$\omega$ 的像仍是 $\mathbf F_p^\times$，故
$$
H^0(\mathbf Q_p,L_8)=0,\qquad
H^0(\mathbf Q_p,L_{-7})=0.
$$
local Tate duality 中 $L_8^\vee(1)=L_{-7}$，所以
$$
H^2(\mathbf Q_p,L_8)=0.
$$
local Euler characteristic 为
$\#H^0\,\#H^2/\#H^1=p^{-1}$，从而
$$
\boxed{\dim_{\mathbf F_p}H^1(\mathbf Q_p,L_8)=1.}
\tag{1146.21}
$$
同样 $H^0(\mathbf Q_p,L_3\oplus L_5)=0$。因此对每个固定的 local abelian pair，非阿贝尔 lifting fiber 是一个恰有 $p$ 个元素的 $H^1(\mathbf Q_p,L_8)$-torsor，未再被 quotient automorphisms 合并。

取一对指定全局标签 $(u,v)$，令 $\eta(u,v)$ 为 (1146.20) 的唯一全局提升。在 (1146.12) 中固定一个 $\mathscr Y$。对任何满足
$$
(a_0(x_p),b_0(x_p))=(\operatorname{loc}_p u,\operatorname{loc}_p v)
$$
的 $x_p\in X(\mathbf Q_p)$，定义两 local lifting 类之间的唯一差
$$
\operatorname{ob}_{\mathscr Y,p}(x_p;u,v)
 =[Y_{x_p}]-\operatorname{loc}_p\eta(u,v)
 \in H^1(\mathbf Q_p,L_8).
\tag{1146.22}
$$
右边是 affine torsor 中的差，不是擅自在非阿贝尔 $H^1$ 中作加法。因为两个类的 quotient 相同且 $H^0$ 为零，该差定义准确。

每个原 rational point 必须满足
$$
\boxed{\operatorname{ob}_{\mathscr Y,p}(x;u,v)=0.}
\tag{1146.23}
$$
选中心线的一组基才可把它写成 $\mathbf F_p$ 标量；零条件与此选择无关。

(1146.22) 为实际覆盖的必要条件，但本文未证明它在任何原 $p$-disk 上非零、非恒定或独立于旧 abelian 标签。改变曲线上的中心 twist 可改变一般 local 点的函数；只有 rational point 的必要零条件及全局纤维唯一性不受影响。下一步须从同一 $\mathscr Y$ 的具体 cochains/原 theta 数据计算这个函数，不能由“一维 local 中心而全局零维”直接宣布排点。

## 7. 原 I₈ 门内，曲线上的覆盖选择也唯一

无条件地，$f_0:\mathscr X_0\to S_0$ 的 Leray 五项列及 (1146.17)–(1146.18) 给
$
H^1(\mathscr X_0,L_8)
 \simeq H^0(S_0,R^1f_{0*}L_8)
 \simeq J(K)[p]_{\omega^{-7}},
\tag{1146.24}
$
其中 $R^1f_{0*}L_8=J[p]\otimes L_7$。右侧只取确为 $K$-有理的奇扭点，不是整个几何 $J[p]$ 的 $\Delta$ 半单化。

任一右侧非零直线，按 R1131 §2 的同一良约化 Eichler–Shimura 论证，其实际 Hecke 系统为
$
T_\ell=\ell^8+\ell^{-7}\pmod p.
$
因此它属于原 $I_8$-块。R1132 对低偶 $r=8$ 的定理在
$
p\nmid B_{16}B_{p-15}
\tag{1146.25}
$
时消去整个原 plus Jacobian 的这个块。$p>37$ 保证 $8<(p-1)/2$ 及原定理的指标范围，故
$
\boxed{H^1(\mathscr X_0,L_8)=0\quad\text{在 (1146.25) 下}.}
\tag{1146.26}
$
$\mathscr X_0$ 的几何纤维连通，$H^0(\mathscr X_0,L_3\oplus L_5)=H^0(S_0,L_3\oplus L_5)=0$。因此固定原 quotient $(a_0,b_0)$ 后，中心 twisting action 的 stabilizer 为零；所有提升在 (1146.25) 下只有一个同构类。

所以旧 F33/$I_8$ 门在这里可支付**覆盖选择的唯一性**；R1144 已经无条件支付的杯积零及本文的覆盖存在并不需要它。门外 (1146.24) 保留真实奇扭点歧义，不擅自删去。即使门内覆盖唯一，也仍需实际计算 (1146.22) 才能排除点。

## 8. 来源、核查及未关闭主门

- [R1144](R1144-original-finite-moments-and-exact-proper-cup.md)：同一原 $F_1,F_2,\epsilon_4$ 的准确 proper 算术零杯积，是本文唯一几何 obstruction 输入。
- [R1062](R1062-original-full-nonsplit-cuspidal-kummer-descent.md) (1062.7)、(1062.9)：原非零几何角色及实际函数/divisor 接口。
- [R1067](R1067-original-cuspidal-labels-supported-only-at-p.md) §§2–3、7：原全 $S_0$ 模型、$2,3$ 及 cusps 的延拓；[R1142](R1142-original-proper-Eisenstein-cohomology-and-Picard-dichotomy.md) §4：同一 $B_8$ base 消失与原 proper 对象。
- [R1132](R1132-original-full-Cartan-odd-cusp-and-constant-K2-torsion.md)：低偶 $r=8$ 的完整 Fricke 负块消失，严格在 (1146.25) 范围内用于曲线上提升的唯一性。
- J. S. Milne, *Lectures on Étale Cohomology*, [作者全文](https://www.jmilne.org/math/CourseNotes/LEC.pdf)，Theorem 14.9、Remark 14.10 与 Proposition 14.13：finite Galois covers 的 Cartan–Leray 序列、逆塔与低阶 locally constant cohomology。本文 (1146.9) 给所需五项列单射的完整推导；§3 的 finite étale covers/基本群等价支付 (1146.12)。
- J. S. Milne, *Arithmetic Duality Theorems*, second edition (2006), [作者全文](https://www.jmilne.org/math/Books/ADTnot.pdf)，I Corollary 2.3 与 Theorem 2.8：local duality 与 Euler characteristic。本文将实际中心代入为 (1146.21)，未以维数代实际局部函数。

全文为纸面证明，无数学程序执行。proper 非阿贝尔覆盖、几何连通、真实 $\mathbf Q$ 下降及底算术中心的唯一性已付；原 class $4$、一般角色对、同点辅助排除与 Serre 一致性的完整主标准仍继续。
