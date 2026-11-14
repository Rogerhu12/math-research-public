# R376：实际 CM 的 Drinfeld 约化点与六层 CM 商的分量收缩

**现行范围更正（R575）**：本文指定模型之间的局部约化点及分量收缩论证按其实际局部表示假设保留。R348 的实际 CM 秩零商及随后实际有理点零像不再是可用前提，不能把本地分量收缩升级为全局排除。完整证明见 [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md)。

## 更正前正文（保留供复核，受上述范围更正约束）

**状态：已证明。** 本篇识别 R315 实际同构分支的特征 $p$ 约化点，并证明 R348 构造的所有 CM 商在该分量上均为常值。后一结论针对 (376.2) 底环上的半稳定源模型与好约化目标模型之间的形式浸入；它不排除将微分除去共同的 $p$ 进因子后研究高阶局部零点，也不排除其他模形式商。

## 1. 范围与结论

固定

$$
p\ge41,\qquad p\equiv2\pmod3,\qquad
Z_p=\operatorname{Norm}
\left(X_{\mathrm{ns}}^+(p)\times_{\mathbf P^1_j}\mathbf P^1_a\right),
\quad j=6912a^3(1-a^3).
\tag{376.1}
$$

令 $c_1$ 为 $j=0,a=1$ 处带 $\mathbb Z[\zeta_3]$ 的标准非分裂 Cartan 结构的有理 CM 点，见 R348。

令 $K_0$ 为 $\mathbb Q_p$ 最大未分歧扩张的完备化，剩余域
$k=\overline{\mathbb F}_p$。取

$$
\pi=(1-\zeta_p)^{1/(p+1)},\qquad
L=K_0(\pi),\qquad R=\mathcal O_L.
\tag{376.2}
$$

其分歧指数为 $p^2-1$。可以在 $R$ 上选取 $Z_p$ 的半稳定模型
$\mathcal Z$，它含有上方 $a=1,j=0$ 的 Drinfeld 分量 $D_1$，具有模型

$$
D_1:\quad y^2=x\left(x^{(p+1)/6}+A\right),
\qquad A\in k^\times.
\tag{376.3}
$$

在此模型上，

$$
\overline{c_1}=(x,y)=(0,0)\in D_1(k)
\tag{376.4}
$$

是整个半稳定特殊纤维的光滑点。

第一项结论涉及 R315 的实际分支。设 $P\in Z_p(\mathbb Q_p)$ 的参数
$a\in\mathbb Z_p$ 满足

$$
r=1-a^3\ne0,\qquad v_p(r)>0,\qquad 3\nmid v_p(r),
\tag{376.5}
$$

且在实际标记下，存在把 $P$ 的非分裂 Cartan 正规化子结构送到 CM 结构的局部同构

$$
H_a[p]\simeq D_r[p],\qquad
H_a:y^2=x^3+3arx-r(2a^3-1),\quad
D_r:y^2=x^3-r.
\tag{376.6}
$$

于是

$$
\overline P=\overline{c_1}=(0,0)
\quad\text{在 }\mathcal Z_k\text{ 上}.
\tag{376.7}
$$

这里要求同构运输实际水平结构。只知道两个未经标记的局部表示同构时，不能擅自指定 $P$ 的水平结构。R315 的全局同构以及其中两个 CM 参考之间的 CM 同源满足这个运输要求。

第二项结论适用于所有 R348 的 CM 因子。令

$$
\theta(\zeta_3)=\zeta_3^{-1},\quad
\theta(\sqrt{-3})=-1,\quad
g_\theta=f_{\Psi_\theta\kappa_4^{-1}}.
\tag{376.8}
$$

令 $B/\mathbb Q_p$ 是这些 $A_{g_\theta}$ 的任意有限乘积之同源商。
设

$$
q:J_{Z_p}\longrightarrow B,\qquad
f(P)=q([P-c_1])
\tag{376.9}
$$

为 $\mathbb Q_p$ 上的实际同态及相应曲线映射。则 $B_L$ 有好约化。对
$\mathcal B/R$ 的 abelian scheme 模型，$f$ 在 $\mathcal Z$ 的光滑部分唯一延拓，并满足

$$
\overline f\bigm|_{D_1^\circ}=0,
\tag{376.10}
$$

其中 $D_1^\circ$ 去掉与其他分量的交点。因此对每个整不变微分
$\omega\in H^0(\mathcal B,\Omega^1_{\mathcal B/R})$，

$$
\left.\overline{f^*\omega}\right|_{D_1^\circ}=0.
\tag{376.11}
$$

特别是这个实际模型映射在 $\overline{c_1}$ **不是形式浸入**。结论对任意同源格和任意倍乘后的投影仍成立；换一个同源代表不能恢复缺失的特殊纤维余切满射。

## 2. 附加六层在 $a=1$ 的稳定子

R348 已识别规范六层及其实际三次扭曲。规范六层由

$$
H_6=\{(\vartheta(g),g):g\in\mathrm{GL}_2(\mathbb F_3)\}
\subset
\mathrm{GL}_2(\mathbb F_2)\times\mathrm{GL}_2(\mathbb F_3)
\tag{376.12}
$$

给出，其中 $\ker\vartheta=Q_8$。规范参数 $u$ 与实际参数的关系是
$a=\sqrt[3]4\,u$。因 $p\equiv2\pmod3$，剩余域 $\mathbb F_p$ 的立方映射为双射，且三在 $\mathbb Z_p$ 为单位；Hensel 引理给

$$
\sqrt[3]4\in\mathbb Q_p.
\tag{376.13}
$$

故实际扭曲在 $\mathbb Q_p$ 已经平凡，不会再给以下惯性作用附加一个辅助层角色。

在 $p>3$ 时，全级六结构是椭圆模叠上的有限 étale 刚性化结构。可先加全级六，再取 $H_6$ 商，构造实际曲线的模型。所有辅助商的阶只含素数二和三。

在 $j=0$ 的椭圆曲线 $E_0:y^2=x^3-1$ 上，自同构群为 $\mu_6$。除去处处的 $[-1]$ 后，有效稳定子为 $\mu_3$。其通用变形可以写成
$y^2=x^3+t x-1$，粗 $j$ 参数在 $t=0$ 的分歧阶为三。另一方面，

$$
\left.\frac{d}{da}\bigl(6912a^3(1-a^3)\bigr)\right|_{a=1}
 =-20736\in\mathbb Z_p^\times.
\tag{376.14}
$$

因此 $a=1$ 这个辅助层支对粗 $j$ 参数不分歧。它保留全部有效
$\mu_3$ 稳定子：若标记的稳定子阶为 $e\mid3$，通用变形的商参数为
$t^e$，到 $j$ 线的分歧阶为 $3/e$；(376.14) 强迫 $e=3$。
相同论证在特殊纤维成立，因为这些群阶与 $p$ 互素，且全六标记的延拓为 étale。

这一点区分了 $a=1$ 支与 $a=0$ 支。后者到 $j$ 线的分歧阶为三，并不保留这个有效 $\mu_3$ 稳定子。

## 3. 全 $p$ 层坐标与两个不同的群作用

使用 Edixhoven–Parent (2021) 的半稳定模型构造，并取辅助问题为全级六。其 Theorem 2.3 与 §2.2.1 给如下坐标。设 $T$ 是通用椭圆形式群的参数，$(P_0,Q_0)$ 是完整 $p$ 水平基，写

$$
x_0=T(P_0),\qquad y_0=T(Q_0).
\tag{376.15}
$$

固定 Weil 配对分量后，超奇异处的局部方程的最低项为
$x_0^p y_0-x_0 y_0^p+(1-\zeta_p)\cdot\text{单位}$。
经吹起和 (376.2) 的基变换，在 Drinfeld 分量的仿射部分得到

$$
\alpha=\overline{x_0/\pi},\qquad
\beta=\overline{y_0/\pi},\qquad
\alpha^p\beta-\alpha\beta^p=C,\quad C\in k^\times.
\tag{376.16}
$$

这里 $\alpha,\beta$ 是约化后的坐标，不是原先坍缩为零的几何 $p$ 挠点。这个区别使以下比较能够识别吹起后的点。

现明确分开两个作用。

1. **几何自同构。** 若 $z\in\mu_6=\operatorname{Aut}(E_0)$ 按其对形式参数切线的作用规范，则

$$
(\alpha,\beta)\longmapsto(z\alpha,z\beta).
\tag{376.17}
$$

这是辅助层稳定子的作用，保持基环 $R$。它来自 $T\mapsto zT$。

2. **基域的惯性下降。** 对 $u\in\mu_{p+1}\subset k^\times$，取固定
$\zeta_p$ 且将 $\pi$ 送到 $[u]\pi$ 的 tame 惯性元素
$\sigma_u$；$[u]$ 是其 Teichmüller 提升。惯性在剩余域平凡，它在所固定的 Weil 配对分量上给

$$
(\alpha,\beta)\longmapsto(u^{-1}\alpha,u^{-1}\beta).
\tag{376.18}
$$

这是由分母 $\pi$ 引起的作用，见该文 §2.2.4、式 (13)。
它不是 (376.17) 的定义，也不是因为某一个点固定而推得。

现在取 $u$ 为一个原始三次单位根。由于辅助 $a=1$ 结构保留整个
$\mu_3$，(376.18) 在该 Drinfeld 分量上的作用，字面上等于 (376.17) 中已经被商掉的几何自同构 $z=u^{-1}$。因此该三阶惯性在商后的**整条分量上逐点平凡**。

下面还用商坐标重新核对这一事实。

## 4. 正规化子与辅助 $\mu_3$ 的显式商坐标

在 $\mathbb F_{p^2}$ 上将非分裂 Cartan 对角化。对
$(\alpha,\beta)$ 作相应可逆线性变换，得到
$(\widetilde\alpha,\widetilde\beta)$，其中 Cartan 作用为两个共轭特征。
(376.16) 成为

$$
\widetilde\alpha^{p+1}-\widetilde\beta^{p+1}=c,
\qquad c\in k^\times.
\tag{376.19}
$$

可以直接取
$\widetilde\alpha=\lambda\alpha+\lambda^p\beta$、
$\widetilde\beta=\lambda^p\alpha+\lambda\beta$，
其中 $\lambda$ 是范数一群的生成元；$p\ge41$ 保证这两个向量独立。
这是 Edixhoven–Parent 的式 (16)–(18)。

对范数一 Cartan 取不变量，令

$$
U=\widetilde\alpha^{p+1}-c/2,\qquad
V=\widetilde\alpha\widetilde\beta.
\tag{376.20}
$$

于是 $U^2=V^{p+1}+A$，其中 $A=c^2/4\ne0$。
正规化子相对 Cartan 的非平凡元素将 $(U,V)$ 送到 $(-U,-V)$，
故可取

$$
X=V^2,\qquad Y=UV,\qquad
Y^2=X\left(X^{(p+1)/2}+A\right).
\tag{376.21}
$$

在 (376.18) 的惯性作用下，

$$
U\longmapsto U,\quad V\longmapsto u^{-2}V,\quad
X\longmapsto u^{-4}X,\quad Y\longmapsto u^{-2}Y.
\tag{376.22}
$$

这里用到了 $u^{p+1}=1$，没有将所有惯性元素都当成固定配对分量的元素。

辅助层在 $a=1$ 的有效几何 $\mu_3$ 将
$(X,Y)$ 按 $(z^4X,z^2Y)$ 缩放。其不变量为

$$
x=X^3,\qquad y=XY,
\quad y^2=x\left(x^{(p+1)/6}+A\right).
\tag{376.23}
$$

由 (376.22) 得

$$
\sigma_u^*(x)=u^{-12}x,\qquad
\sigma_u^*(y)=u^{-6}y.
\tag{376.24}
$$

当 $u^3=1$ 时两个乘子都为一。这独立核准了 §3 的逐点平凡断言。

所用商都是 tame 商。式 (376.23) 是该实际辅助支的分量方程，而不只是未加六层的曲线方程：§2 已证明此支的剩余稳定子正好是产生 (376.23) 的 $\mu_3$。

## 5. 实际有限平坦同构识别吹起后的点

先证明 $c_1$ 的位置。对 $D'=E_0$ 及 $T=-x/y$，每个非零
$p$ 挠点 $S$ 都满足

$$
v_p(T(S))=\frac1{p^2-1}=v_p(\pi).
\tag{376.25}
$$

这是高度二形式群的 Newton 多边形计算，R374 §4 已给出完整证明。
因此

$$
\ell:E_0[p](\overline{\mathbb Q}_p)\longrightarrow k,\qquad
S\longmapsto\overline{T(S)/\pi}
\tag{376.26}
$$

是 $\mathbb F_p$ 线性单射。CM 的 $\zeta_3$ 在形式参数上的作用是一个原始三次单位根，故 $\ell$ 对相应的
$\mathbb F_p[\zeta_3]=\mathbb F_{p^2}$ 作用是线性的。扩标量到 $k$ 后，$\ell$ 在 Cartan 的两个共轭特征线之一上为零，在另一个上非零。

所以对 CM 标准 Cartan 基，(376.19) 的两个特征坐标恰有一个为零。
从而 $V=0$、$U=\pm c/2$；正规化子商再给

$$
(X,Y)=(0,0),\qquad (x,y)=(0,0).
\tag{376.27}
$$

方程 (376.23) 在此点对 $x$ 的偏导数为 $-A\ne0$，故分量光滑。模型中与 Igusa 分量的交点在此仿射图之外，见该文 §3.1–3.4 的构造。因此该点也是整个半稳定纤维的光滑点。辅助 $\mu_3$ 在一个光滑形式圆盘上的商仍是光滑圆盘：其阶与 $p$ 互素，可以线性化参数并取三次方不变量。这也直接核准了商模型的相对光滑性。

再考虑 (376.5)–(376.6)。取 $v^6=r$，并令
$L_0=\mathbb Q_p(\mu_6,v)$。其分歧指数
$e=6/\gcd(6,v_p(r))\in\{3,6\}$，小于 $p-1$。
把两条曲线同时改为好模型：

$$
H':Y^2=X^3+3av^2X-(1-2r),\qquad
D':Y^2=X^3-1.
\tag{376.28}
$$

它们的特殊纤维字面相同。R315 已证明：给定同构经 Raynaud 的完全忠实性延拓到有限平坦 $p$ 群后，其特殊纤维是某个
$[b]$，$b\in\mathbb F_p^\times$，且 Weil 乘子为 $b^2$。
将目标同构再乘 $[b^{-1}]$，可使它同时满足

$$
\phi\bmod\mathfrak m_{L_0}=\operatorname{id},
\qquad \phi\text{ 严格保持 Weil 配对}.
\tag{376.29}
$$

这一标量更改在 Cartan 中，故不改变水平结构。

以下说明群概形的约化相同如何控制 (376.16)，而不是仅比较坍缩后的点。超奇异好模型的 $p$ 挠点全部在形式群中，$T_H,T_D$ 给有限平坦坐标代数上的整函数。由 (376.29)，在源的坐标代数 $\mathcal A=\mathcal O(H'[p])$ 中有

$$
\phi^*T_D-T_H\in\mathfrak m_{L_0}\mathcal A,\qquad
\frac1e>\frac1{p^2-1}.
\tag{376.30}
$$

对任意非零 $S\in H'[p]$，整函数在该整点的值仍为整，故
$v_p(T_D(\phi S)-T_H(S))\ge1/e$。
参考曲线的 (376.25) 与严格不等式 (376.30) 于是给出
$v_p(T_H(S))=1/(p^2-1)$，并且

$$
\overline{T_D(\phi S)/\pi}
 =\overline{T_H(S)/\pi}.
\tag{376.31}
$$

因 $e\mid6\mid p^2-1$，$L_0$ 可在未分歧基变换后嵌入 $L$；再作有限扩张来写出全部挠点不会改变这些几何约化等式。

为 $P$ 选一个实际完整 $p$ 基，沿 $\phi$ 运输到 CM 参考。由 (376.29)，两者在同一 Weil 配对分量内；由 (376.31)，它们的 $\alpha,\beta$ 坐标相同。因此它们经过全部 Cartan、正规化子和辅助层商后仍是同一点。

最后核辅助六标记。$p\equiv2\pmod3$ 与 $a^3\equiv1\bmod p$ 给
$a\equiv1\bmod p$。选择 $H'$ 的一个全六标记提升，并将其剩余标记在 $D'=E_0$ 上唯一 étale 提升。所得到的粗辅助点必是 $a=1$：$j=0$ 上三个简单的 $a^3=1$ 支具有不同剩余值，而所选支剩余值为一。因而参考点正是 $c_1$，而非 $a=0$ 或另一个三次单位根支。这证明 (376.7)。

## 6. 目标 CM 因子的三阶惯性固定部分

令 $\sigma=\sigma_u$，其中 $u$ 是 §3 的原始三次单位根。取任意
$\ell\ne p$。R374 §2–3 已用同一个好约化参考
$E_0:y^2=x^3-1$ 写出 CM Tate 角色

$$
\psi_{\theta,\ell}
 =\psi_{0,\ell}\eta_{\theta,\ell},
\qquad
\eta_\theta=
\frac{\Psi_\theta\kappa_4^{-1}}{\Psi_0}.
\tag{376.32}
$$

参考在 $p$ 处不分歧，有限角色在 $p$ 的单位群上为
$\theta^{-1}$，而 $\kappa_{4,p}$ 平凡。
本地互反律把所用 tame 商与 $\mathbb F_{p^2}^\times$ 识别；若将互反律规范取反，则角色同时取逆。无论此规范如何，
(376.8) 都给出 $\eta_\theta(\sigma)$ 为原始三次单位根。
CM 共轭角色给其逆，系数域的任何嵌入也只能交换这两个原始根。
所以在每个 R348 因子以及它们任意同源商的有理 Tate 空间上，

$$
1+\sigma+\sigma^2=0.
\tag{376.33}
$$

这里是一个单一惯性元素在全部系数嵌入上的多项式恒等式，不依赖选取整 CM idempotent。

全部这些有限惯性角色的阶整除 $p+1$。它们在 $L$ 上平凡；
Néron–Ogg–Shafarevich 因此给 $B_L$ 好约化。对其 abelian scheme
$\mathcal B/R$，$\sigma$ 的下降在特殊纤维给自同构
$\iota:\mathcal B_k\to\mathcal B_k$。由于 $\sigma$ 对剩余域恒等，
这是 $k$ 上的群自同构。好约化时的有限 étale $\ell^n$ 挠点专门化与下降相容，故 (376.33) 变成

$$
1+\iota+\iota^2=0
\quad\text{于 }\operatorname{End}(\mathcal B_k).
\tag{376.34}
$$

从 Tate 空间到端同态的这一步只用端同态在全部
$\ell$ 次幂挠点上的作用忠实。特别得到整端同态恒等式

$$
(1-\iota)(2+\iota)=[3].
\tag{376.35}
$$

因此 $1-\iota$ 是次数与 $p$ 互素的同源：其核包含于
$\mathcal B_k[3]$，是有限 étale 群概形；对切空间的作用为同构。
不应把这句话扩大为 $\ker(1-\iota)=0$；固定的三次挠点可以存在，然而固定部分没有任何正维分量，也没有非零切方向。

由于 (376.33) 在有理 Tate 表示上成立，对任何实际同源代表都成立；
随后 (376.34)–(376.35) 在该代表的实际特殊纤维端环中成立。
故此论证不假设任何模形式投影在 $p$ 处整饱和。

## 7. 收缩整条分量与余切映射为零

令 $\mathcal U=\mathcal Z^{\mathrm{sm}}$。Néron 映射性质把 (376.9)
唯一延拓为

$$
\mathfrak f:\mathcal U\longrightarrow\mathcal B.
\tag{376.36}
$$

基点 $c_1$ 在 $\mathbb Q_p$ 定义，且 §5 证明其截面落在
$\mathcal U$。泛纤维有 $f(c_1)=0$，故
$\mathfrak f(\overline{c_1})=0$。

映射 $f$ 与基域 Galois 下降相容；延拓的唯一性保持这个相容性。
由 (376.24)，$\sigma$ 在 $D_1$ 上逐点为恒等。所以

$$
\iota\circ\overline{\mathfrak f}|_{D_1^\circ}
 =\overline{\mathfrak f}|_{D_1^\circ}.
\tag{376.37}
$$

该映射因此因子化经过有限 étale 群
$\ker(1-\iota)$。$D_1^\circ$ 几何连通，而有限 étale 群的几何分量是离散点；像必为常值。它包含基点的零像，所以常值准确为零。这证明 (376.10)，不需要先证明任何投影次数与 $p$ 互素。

将整不变微分拉回再约化，所得微分就是常值映射
$\overline{\mathfrak f}|_{D_1^\circ}$ 的拉回，因此为零。
在 $\overline{c_1}$，相对源余切空间是一维，目标余切到它的映射为零，不可能满射。形式浸入必然诱导余切满射，故该处不是形式浸入。

若 $q$ 先经任意同源或倍乘，§6 对新目标仍成立，(376.37) 也不变。因此障碍不能仅靠调整同源投影分母解除。

## 8. 对实际全局路线的后果与保留问题

R348 与 R374 已给出某个非零商 $B$，满足
$B(\mathbb Q)=0$ 和 $q([P-c_1])=0$。本篇进一步证明实际同 CM 分支中的
$P$ 与 $c_1$ 落在同一光滑约化点。这关闭了该分支的“同一约化点”缺口。

但这些具体 CM 商收缩包含该点的整个 Drinfeld 分量；在上述半稳定模型与目标好约化模型之间，它们不能直接提供形式浸入。障碍来自明确的三阶惯性作用，而非尚未核定的投影分母。

这也不等于在原 $\mathbb Q_p$ 底域的所有模型上均不存在形式浸入。原 Néron 模型到好约化基变换模型的映射，本身可能将微分乘上正赋值的因子；缩小源圆盘后，除去这些因子可能得到新的整方向。本篇没有把这种归一化排除。

尚可继续的严格问题包括：除去拉回微分的共同正赋值后，计算其第一个非零局部系数及全部余项界，借 R290 的实际深度估计隔离零点；或者寻找在该分量上有非零约化微分的其他模形式商。不能由本篇的收缩结论断言规范化后的解析函数恒零，也不能由秩零商的存在断言前一问题已经解决。原 Serre 一致性目标仍 OPEN。

## 9. 本篇使用的原文

- B. Edixhoven, P. Parent, *Semistable Reduction of Modular Curves Associated with Maximal Subgroups in Prime Level*, Documenta Mathematica **26** (2021), 231–269, DOI 10.4171/DM/814。所用位置是 Theorem 2.3（印刷第 238 页）；§2.2.1、式 (2)–(5)（240 页）；§2.2.2（241–242 页）；§2.2.4、式 (13)（243–244 页）；Theorems 3.1、3.3 及式 (16)–(23)（244–248 页）；Theorem 3.5 的证明与式 (26)（250–251 页）。原文给全层模型、两种作用及商坐标；本篇分别核出实际六层 $a=1$ 的稳定子、有限平坦同构的坐标比较，以及该具体 CM 商的收缩。
  [作者原刊 PDF](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf)
- 有限平坦同构的延拓及特殊纤维标量结论使用 R315 的完整证明，其原文输入为 Raynaud (1974), Corollaire 3.3.6(1)。R374 §4 的形式群 Newton 计算提供 (376.25)。CM Tate 角色与好约化使用 R374 已核的 Serre–Tate (1968), Theorems 1、11。

本篇为纯证明，无数值扫描、数据证书或新软件依赖。

