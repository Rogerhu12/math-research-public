# R1014 — 原 full9 曲面的充分大约化 Tate 定理、惰性新增截面格与54图的真实有限域交

日期：2026-11-27。会话：`Astra-rank2-Sha-0b097461-20261127`。

**状态：充分大素数的结论已证明。** §7–8直接构造经过原曲面的光滑
射影变形族，完整支付周期非恒与全局同时解消，再用已发表的
Hamacher–Yang–Zhao Theorem B 得到固定整数 $q_0$，使所有
$q>q_0$ 满足除子 Tate。惰性时进一步得到完整 MW 格 $(q/3)A_2$、
两 Frobenius 方向及两个常数域的 Brauer 群零；§5给原54图的真实
整系数交公式。这里 $q$ 是辅助约化素数，不替代原普通 $p$。

§2保留此前核对的 Guo–Yang v2 路线，但它目前仍为预印本：
[作者主页](https://sites.google.com/umich.edu/hyg)与
[arXiv记录](https://arxiv.org/abs/2501.18541)，检查日期2026-11-27。
该路线不能直接作为本题已认可输入。本篇的充分大素数结论完全由
§7–8独立支付；$5\le q\le q_0$ 的全范围仍只是§2的条件推导。

尚未算出两个新截面的原54点评值，亦未声称原全局 AJ 或指定普通
位的 Coleman 值已非零。有限域交保留整系数，不能先张量
$\mathbf Q$ 后仍把有限域点称为非零 shadow。

## 1. 同一原模型和全部好约化

保持 R991(27) 的实际群
$$
\Gamma=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}
\in\Gamma_1(3):b-c/3\equiv0\pmod3\right\},
\tag{1}
$$
及其实际相对极小模曲面
$$
B:\ v^3=t(1-27t),\qquad
S:\ y^2+xy+t y=x^3\quad\text{over }B.
\tag{2}
$$
源 $A=E_{27}:y^2+y=x^3$、R1011 的 full9 基、全部54个 degree34 商
和 $P_-$ 不改变。$B$ 经 R991(29) 的有理同构就是 $E_{27}$。

以下 $S_q\to B_q$ 总指(2)的光滑、射影、相对极小模型。
在 $\mathbf Z[1/6]$ 上，$B$ 光滑。有限处的 Weierstrass 判别式和
$c_4$ 是
$$
\Delta=t^3(1-27t),\qquad c_4=1-24t.
\tag{3}
$$
$t=0,1/27$ 在 $B$ 上的分歧指数都是3；相应判别式阶为9、3，
$c_4$ 分别是1、$1/9$。所以在所有 $q\ge5$，两纤维准确为
$I_9,I_3$，没有小特征的附加纤维。

无穷处可直接核查，而不依靠特征零的纤维表。置
$$
r=t^{-1},\qquad z=v/t,\qquad z^3=r^2-27r,
\qquad x=z^{-2}X,\ y=z^{-3}Y.
$$
则实际好模型是
$$
Y^2+zXY+(r-27)Y=X^3,
\qquad\Delta_\infty=(r-27)^5.
\tag{4}
$$
在 $r=z=0$，判别式是 $(-27)^5$，故对所有 $q\ge5$ 都是好纤维。
有限两处 Weierstrass 模型只有 $A_8,A_2$ 有理双点；对节点局部模型
的逐次解消给上述相对极小光滑模型。这些分支点互异，所需2、3均
可逆，解消与这些好素数的约化相容。因而可对同一 $S$ 使用光滑
适当基变换的纯实现；没有把另一个同纯表示的曲面代入。

两纤维 Euler 数之和是12。基本线丛 $\mathcal L$ 的次数为1，
零截面给无多重纤维，且
$$
\chi(\mathcal O_{S_q})=1,\quad g(B_q)=1,\quad
K_{S_q}\equiv F,\quad O^2=-1,
\tag{5}
$$
其中 $F$ 是一个纤维类。实际二形式也保留无穷处的一阶零：
$$
\Omega=\frac{dt}{v^2}\wedge\omega_{\rm old}
=-\frac{dr}{z}\wedge\omega_{\rm new}
=-\frac{3z}{2r-27}\,dz\wedge\omega_{\rm new}.
\tag{6}
$$
故这里的 canonical fiber 正是(4)的光滑纤维。

两纤维的分裂型也在原模型中固定。$t=0$ 的节点切锥为 $y(y+x)$，
所以 $I_9$ 在 $\mathbf F_q$ 已裂。$t=1/27$ 的节点是
$(-1/9,1/27)$；平移后的二次项是
$$
Y^2+XY+\tfrac13X^2.
\tag{7}
$$
它的判别式平方类为 $-3$。因此 $I_3$ 在 $q\equiv1\pmod3$ 时裂，
在 $q\equiv2\pmod3$ 时非裂、到 $\mathbf F_{q^2}$ 才裂。

## 2. 仅作条件记录的 Guo–Yang 全好素数路线

本节只核对 Guo–Yang **v2** 的假设，不以其预印本定理作为§8的
无条件输入。它的陈述不含所有奇异纤维不可约的条件：

- H. Guo–Z. Yang，*The Tate conjecture for surfaces of geometric genus one
  — embracing singularities*，[arXiv:2501.18541v2](https://arxiv.org/pdf/2501.18541v2)，
  2025-06-11，Theorem2.22、Theorem4.33。

Theorem4.33 的条件是：$k/\mathbf F_q$ 有限生成、$q\ge5$，光滑
适当极小曲面有带截面的椭圆纤维化到 genus1 曲线，基本线丛次数1；
另外要求曲面非 supersingular，或有预期 Hodge 数。其结论是该
曲面的除子 Tate 猜想。这里没有不可约奇异纤维条件。

其所需的实际可分性可以直接检验。原 $j$ 函数为
$$
j(t)=\frac{(1-24t)^3}{t^3(1-27t)},\qquad
\frac{j'(t)}{j(t)}
=\frac{-3(1-36t+216t^2)}{t(1-27t)(1-24t)}.
\tag{8}
$$
对每个 $q\ge5$，右侧非零；$t:B_q\to\mathbf P^1$ 也是次数3的
可分映射。因此 $j:B_q\to\mathbf P^1$ 有限且可分。
Theorem2.22 于是给
$$
h^{0,1}=h^{1,0}=1,\quad h^{0,2}=h^{2,0}=1,
\quad h^{1,1}=12,
\tag{9}
$$
Hodge–de Rham 在 $E_1$ 退化，并给每阶晶体上同调无扭。
这逐项满足 Theorem4.33；在采用该预印本定理的前提下，所以
$$
\boxed{\text{在采用上述预印本定理的条件下，所有 }q\ge5\text{ 满足 Tate。}}
\tag{10}
$$
特别，摘要中便于统一陈述的 $q\ge11$ 并非本模型的限制；5、7
均由实际可分式(8)支付。这里明确依赖该文所述定理；既没有从纯
Frobenius 特征值推测 Tate，也尚未把这份预印本的完整证明搬入本仓库。

## 3. 实际 Frobenius、NS 秩和截面的常数域

本节及§4在所用约化的除子 Tate 成立时推导。§8已无条件支付
所有 $q>q_0$（含惰性的 $\mathbf F_{q^2}$）；有限剩余素数仅保条件范围。

令 $\Phi_q$ 为作用于未 Tate 扭曲 $H^2_{\rm et}$ 的**几何**
Frobenius。其 Weil 特征值绝对值为 $q$。令 $\sigma_q$ 为几何点和
NS 上的**算术** Frobenius $x\mapsto x^q$；在 $H^2(1)$ 上，它
与 $q^{-1}\Phi_q$ 互逆。以下 NS 的 $\pm1$ 符号在取逆后不变。

R991(32)已固定完整纯实现为 $\theta(\psi_{27}^2)$，包括3处有限
角色和原有理下降。在好素数处，其 weight3 特征多项式是
$$
X^2-A_qX+\chi_K(q)q^2,
\qquad K=\mathbf Q(\sqrt{-3}).
\tag{11}
$$
若 $q$ 惰性，则 $A_q=0$、$\chi_K(q)=-1$，故该原秩二部分的
几何 Frobenius 特征值恰为 $q,-q$。若 $q=\mathfrak q\bar{\mathfrak q}$
分裂，则二根为 $\pi^2,\bar\pi^2$，其中
$\pi=\psi_{27}(\mathfrak q)$、$\pi\bar\pi=q$。
比值 $\pi/\bar\pi$ 不是单位根：它的分式理想是
$\mathfrak q/\bar{\mathfrak q}$，非单位理想。因此这两个根除以
$q$ 后，在任何有限常数扩张都不成为1。

旧平凡格由 $O,F$、$I_9$ 的8个非恒等分量、$I_3$ 的2个非恒等
分量生成，秩12。惰性时，前10个类由 $\sigma_q$ 固定，$I_3$ 的
两个分量交换，故旧格的固定秩11、反固定秩1。结合所用 Tate 输入与(11)得
$$
\begin{array}{c|ccc}
 &\rho(S_q/\mathbf F_q)&\rho(S_q/\mathbf F_{q^2})
 &\rho(S_q/\overline{\mathbf F}_q)\\ \hline
q\equiv1\pmod3&12&12&12\\
q\equiv2\pmod3&12&14&14.
\end{array}
\tag{12}
$$
非恒定 $j$ 使常数 trace 为零。Shioda–Tate 的 Galois 等变分解
于是给实际 generic elliptic curve $E_q/\mathbf F_q(B_q)$ 的秩
$$
\boxed{\begin{array}{c|ccc}
 &\operatorname{rank}E_q(\mathbf F_q(B_q))
 &\operatorname{rank}E_q(\mathbf F_{q^2}(B_q))
 &\operatorname{rank}E_q(\overline{\mathbf F}_q(B_q))\\ \hline
q\equiv1\pmod3&0&0&0\\
q\equiv2\pmod3&1&2&2.
\end{array}}
\tag{13}
$$
可引用的原始表述是 T. Shioda，*Some remarks on elliptic curves over
function fields*，[Astérisque209(1992),99–114](https://www.numdam.org/article/AST_1992__209__99_0.pdf)，
§1(1.1)–(1.8)、§2 Theorem7；这些命题允许任意特征，且这里有
奇异纤维，满足其全篇条件(*)。

在惰性情形，$\Phi_q^2=q^2$ 在整个 $H^2$ 上成立；旧分量与新两线
均没有 Jordan 块。Tate 使所有 NS 类在 $\mathbf F_{q^2}$ 不变。
NS 无扭，故这是整 NS 上的不变性，不只在张量 $\mathbf Q_\ell$ 后
成立。有限域的 Lang 定理和 $\operatorname{Br}(\mathbf F_{q^2})=0$
使这些类由该域的除子表示。再用 Galois 等变的
$$
\mathrm{NS}(S_{\overline q})/T\simeq
E_q(\overline{\mathbf F}_q(B_q)),
\tag{14}
$$
得到整个几何 Mordell–Weil 群已在 $\mathbf F_{q^2}(B_q)$ 定义。
奇数次常数扩张保持秩1，偶数次保持秩2。这里没有只从有理秩
推断整截面常数域。

## 4. 所有特征的 torsion，以及惰性时准确的格

采用 Shioda 的高度规范 $\langle P,P\rangle=-\varphi(P)^2$。
对非零 torsion 截面 $P$，其高度式为
$$
0=2+2(P\cdot O)
-\frac{i(9-i)}9-\frac{j(3-j)}3,
\quad0\le i<9,\quad0\le j<3.
\tag{15}
$$
两项局部贡献之和不超过 $26/9<4$，所以 $P\cdot O=0$。
若 $j\ne0$，则必须 $i(9-i)=12$，无整数解；若 $j=0$，则
$i=3,6$。故 torsion 到 $I_9$ 分量群的映射在非零点上只取3、6，
其核为零。这同时排除非3 torsion 和9 torsion；论证没有排除
特征 $q$ 的 torsion 作为例外。原截面 $(0,0)$ 恰为 order3，因而
$$
E_q(\overline{\mathbf F}_q(B_q))_{\rm tors}
=\mathbf Z/3\mathbf Z.
\tag{16}
$$
它已经定义在 $\mathbf F_q$。

现在设 $q\equiv2\pmod3$。在 $k=\mathbf F_{q^2}$，全部14个
Frobenius 根均是 $q^2$。由(5)，Artin–Tate 指数
$\alpha=\chi(\mathcal O)-1+\dim\operatorname{Pic}^0=1$。
因此 Artin–Tate 公式给
$$
\#\operatorname{Br}(S_q/k)\,
|\det\mathrm{NS}(S_q/k)|=q^2.
\tag{17}
$$
这里 NS 无扭，见 Shioda 前引文 §1 及 §2 Theorem8 前的明确说明；
Tate 推出完整 Artin–Tate 公式，采用 J. S. Milne，
[*On a conjecture of Artin and Tate*, Ann. Math.102(1975),517–533](https://math.stanford.edu/~conrad/BSDseminar/refs/MilneAT.pdf)。
有限 Brauer 群的阶为平方，采用 Liu–Lorenzini–Raynaud，
[*On the Brauer group of a surface*, Invent. Math.159(2005),673–676](https://dinolorenzini.franklinresearch.uga.edu/sites/default/files/inline-files/papers/LLR2InventionesPublished.pdf)，
Theorem1；[2018 corrigendum](https://arxiv.org/pdf/1804.11158v2)
§2 Corrected Corollary3 明确保留这个平方结论。

式(17)只留下 $|\det\mathrm{NS}|=1$ 或 $q^2$。前者不可能：
$\langle O,F\rangle$ 的矩阵
$\left(\begin{smallmatrix}-1&1\\1&0\end{smallmatrix}\right)$ 幺模，
故 NS 整直和分解为这个格与负定秩12格 $N$。
由 Riemann–Roch，$D^2\equiv D\cdot K\pmod2$；(5)使 $N$ 为偶格。
若 NS 幺模，则 $N$ 为负定偶幺模秩12格，与偶幺模格的 signature
必须被8整除矛盾。因此
$$
\boxed{\det\mathrm{NS}(S_q/\mathbf F_{q^2})=-q^2,
\qquad\operatorname{Br}(S_q/\mathbf F_{q^2})=0.}
\tag{18}
$$

几何平凡格的判别式绝对值为 $9\cdot3=27$。
Shioda 的完整判别式公式与(16)、(18)给
$$
\det MW_{\rm free}=q^2/3.
\tag{19}
$$
真实甲板变换 $\tau:(t,v,x,y)\mapsto(t,\omega v,x,y)$ 是阶3
自同构。它在原二形式上的值为 $\omega$，故在原秩二纯部分上
特征多项式为 $X^2+X+1$。约化后，在新增 MW 格上也准确满足
该式。于是 $MW_{\rm free}$ 是 $\mathbf Z[\omega]$ 的无扭秩一模。
该环为 PID，故可取整生成元 $Q_q$；$\tau$ 保持高度，给
$$
\operatorname{Gram}(Q_q,\tau Q_q)
=a\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad a>0.
$$
式(19)迫 $3a^2=q^2/3$，即
$$
\boxed{MW_{\rm free}\simeq (q/3)A_2,
\quad\langle Q_q,Q_q\rangle=2q/3.}
\tag{20}
$$
这是完整整格身份；未把一个有限指数的两截面子格冒称整 MW。

还可固定算术 Frobenius 的反线性类型。因
$\sigma_q\tau\sigma_q^{-1}=\tau^2$，在 $\mathbf Z[\omega]$
坐标中 $\sigma_q(x)=u\bar x$，$u\in\mu_6$。变换整生成元后，只
有 $u=1,-1$ 两类。固定线的最小高度分别为 $2q/3,2q$。

实际 $\mathbf F_q$ 的 NS 固定格用下面的整列，而非删掉 $I_3$。
$T$ 是一个排列 Galois 格，$H^1(\langle\sigma_q\rangle,T)=0$；
因此(14)取不变量仍右正合。固定平凡格的判别式绝对值是
$9\cdot2=18$，其中非裂 $I_3$ 的固定类是两个非恒等分量之和，
自交 $-2$。设固定 MW 的最小高度为 $h$，则
$$
|\det\mathrm{NS}(S_q/\mathbf F_q)|=18h/3^2=2h.
$$
未扭曲的全 $H^2$ 多项式为
$(1-qT)^{12}(1+qT)^2$。直接应用 Artin–Tate 得
$$
4=\frac{\#\operatorname{Br}(S_q/\mathbf F_q)\,2h}{q}.
\tag{21}
$$
若 $h=2q/3$，右式要求 Brauer 群阶为3，与平方性矛盾。
所以 $u=-1$，且
$$
\boxed{\begin{aligned}
&\sigma_q(x)=-\bar x\quad\text{在一个整 }\mathbf Z[\omega]
\text{ 生成元规范中},\\
&h_{+}=2q,\qquad h_{-}=2q/3,\qquad
\operatorname{Br}(S_q/\mathbf F_q)=0.
\end{aligned}}
\tag{22}
$$
固定线由 $\delta Q_q$ 生成、反固定线由 $Q_q$ 生成；两线直和在
全 MW 格中指数2。因 torsion 为固定的 $\mathbf Z/3$，且
$H^1(C_2,\mathbf Z/3)=0$，自由固定生成元可提升为真实
$\mathbf F_q(B_q)$ 截面。这里 $h_+$ 是函数域 Néron–Tate 高度，
不代替数域原题的任何 $p$-adic regulator。

## 5. 新除子如何真正作用到原54图

此节同时记录一个不能省略的系数区别。先在特征零的固定有限图表达
中统一清分母，取一个固定整数 $d>0$，令
$$
R=\mathcal O_E[1/d],\qquad E=\mathbf Q(\zeta_9).
$$
使 R1011 的所有 $c_i$、$P_-$、$e_{\eta_j}$ 和 Chow 对应表达的
系数属于 $R$。保留这个**指定的有限循环表达** $Y_{j,0,R}$。
本节取 $q\nmid d$ 且避开该有限图表达的坏约化素数；这些排除固定。
选择 $k=\mathbf F_{q^{2e}}$，包含全部原 full9 点、54图、有限
Galois 共轭及模型同构的约化。没有删除或合并某些图。

对 $D\in\operatorname{Pic}(S_k)$ 且 $D\cdot F=0$，定义
$$
\mathcal S_D(Z)
=(\operatorname{pr}_A)_*
\bigl(\operatorname{pr}_S^*D\cdot Z\bigr)
\in CH_0(A_k)^0\otimes R=A(k)\otimes R.
\tag{23}
$$
对一张实际同源图 $\varphi:A\to S_b$，记
$r_b(D)\in\operatorname{Pic}^0(S_b)=S_b(k)$ 为 $D$ 在纤维上的
限制。则原修正图的交准确为
$$
\boxed{\mathcal S_D(\Delta_\varphi)
=\widehat\varphi\bigl(r_b(D)\bigr).}
\tag{24}
$$
证明：图项的交是 $\varphi^*(D|_{S_b})$，在 Picard 群中恰为
对偶同源 $\widehat\varphi$；$34(S_b\times O_A)$ 项的推出是
$34(D\cdot S_b)[O_A]=0$；$(O_b\times A)$ 项的积在 $S$ 上为
余维3，故为零。这是交理论等式，包含重数，不是只看闭点集合。

若 $D=[Q]-[O]$，其中 $Q$ 是本篇新增的截面，则
$r_b(D)=Q(b)$。Shioda 的垂直修正和从 $B$ 拉回的 Picard 类在
每个光滑纤维上限制平凡，所以不会改变(24)的点。

完整最高投影要保留转置。设
$$
D^+=(e_S^+)_{*}D,
\qquad (e_S^-)^t=e_S^+,
\qquad P_-=e_S^-\otimes e_A^-.
\tag{25}
$$
所有算子均是 R995 的实际有限 Chow 对应；不能把这里的 $e_S^+$
换成同号的 $e_S^-$。取固定 Galois 域 $L/K$ 如 R1011，
$H/K$ 的次数为18，Galois 只作用几何而固定系数 $R$。
由(24)与对应的投影公式，得到全54图的准确有限域公式
$$
\boxed{\mathcal S_D(Y_{j,0,R})
=(e_A^-)_*\frac1{18}
\sum_{\gamma\in\operatorname{Gal}(L/K)}
\eta_j(\gamma|_H)^{-1}
\sum_{i=1}^{54}c_i\,
\widehat{\gamma\varphi_i}
\left(r_{\gamma b_i}(D^+)\right).}
\tag{26}
$$
在(26)中先取实际 Galois 共轭再在固定素位约化；它并未假设所有
$\gamma$ 都属于一个分解群。对 $\operatorname{Cor}_{L/H}$ 的
全部项都求和，故没有丢掉 $[L:H]$ 的真实重数。每个
$\gamma\varphi_i$ 仍携带 R1011 的完整 full9 级结构及原 degree34。
式(26)保留 $e_A^-$ 的实际对应作用，因而也保留 Picard 拉回中
$[\delta]^*$ 对应于对偶同源 $[-\delta]$ 的方向。

最后明确有限域值能给出的信息。惰性 $q$ 时，$A=E_{27}$ 的
$q^2$-Frobenius 是 $[-q]$，所以
$$
A(\mathbf F_{q^{2e}})
=\ker\bigl([( -q)^e-1]\bigr),
\qquad
\bigl(q^e-(-1)^e\bigr)\mathcal S_D(Y_{j,0,R})=0.
\tag{27}
$$
若进一步张量 $E$，这些有限点全部变零；故必须用(23)的整
$R$ 版本或指定的 $\ell^n$ 商读取。新方向的存在、格(20)和
高度(22)本身不使(26)非零，更不直接推出 R1011 的普通局部
$J^0_{j,p}\ne0$。后续实际工作是构造(20)的截面方程、完整消费
(26)，再支付相应的全局与指定普通局部比较；不得把(10)的除子
Tate 定理扩成混合 AJ 的保真定理。

## 6. 本篇实际增加的输入

§7–8完整支付所有充分大 $q$ 的实际除子 Tate。(12)–(14)给准确
常数域；(18)、(20)、(22)给惰性新增截面的完整整格与 Frobenius
方向；(26)保原54图、$\eta_j^{-1}$、完整 trace 与 $P_-$。
小特征的全范围只保§2的条件陈述。没有预记任何未执行的交点值或
跨素数的混合 AJ 非零。

## 7. 原曲面所在具体族的非恒 period：完整短证明

本节独立证明后继已发表 Tate 定理所需的 period 条件。论证与
Greer–Zhang Lemma7.1 的短证明相容，但以下给出全部推导，不把该
预印本或有缺口的 Saito 普遍 infinitesimal Torelli 陈述作为黑盒。
真正的光滑射影同时解消在下一节另行构造；本节不先行假设它自动存在。

### 7.1 一个可直接检验的局部判据

设 $X/\mathbf C$ 是非等型椭圆曲面，基曲线 genus1，基本线丛次数1，
有零截面，且唯一 canonical divisor $K_X=C$ 是光滑纤维。
设该纤维的 Kodaira–Spencer 映射
$$
\kappa_C:H^0(C,N_{C/X})\longrightarrow H^1(C,T_C)
\tag{28}
$$
非零。则完整 weight2 period 的 infinitesimal 映射
$$
d\mathcal P_X:H^1(X,T_X)\longrightarrow
\operatorname{Hom}\bigl(H^0(X,K_X),H^1(X,\Omega_X^1)\bigr)
\tag{29}
$$
是单射。

先证明这里需要的 $H^0(X,T_X)=0$。连通自同构保持 Iitaka 纤维化，
所以一个全局向量场在基曲线上给平移向量场。它必须保持有限非空
奇异纤维集合，因而基向量场为零。于是它是垂直向量场；在零截面
求值给基本线丛对偶 $\mathcal L^{-1}$ 的截面。由于次数为 $-1$，
这个截面为零。椭圆纤维的向量场都是平移不变的，故原向量场处处
为零。

取生成 $H^0(X,K_X)$ 的二形式 $s$，其零除子是 $C$。由 Serre 对偶
及 $H^1(\Omega_X^1)$ 的 cup-product 自对偶，(29)的对偶是乘法
$$
\mu_s:H^1(X,\Omega_X^1)\longrightarrow
H^1(X,K_X\otimes\Omega_X^1).
\tag{30}
$$
故只须证明(30)满射。乘以 $s$ 给短正合列
$$
0\longrightarrow\Omega_X^1\xrightarrow{s}
K_X\otimes\Omega_X^1\longrightarrow
(K_X\otimes\Omega_X^1)|_C\longrightarrow0.
\tag{31}
$$
纤维的法线丛为平凡，adjunction 给 $K_X|_C\simeq\mathcal O_C$。
其 conormal 列是
$$
0\longrightarrow\mathcal O_C\longrightarrow
\Omega_X^1|_C\longrightarrow\mathcal O_C\longrightarrow0.
\tag{32}
$$
这个扩张的连接映射
$H^0(\mathcal O_C)\to H^1(\mathcal O_C)$ 是(28)的对偶。
两个空间都是一维，(28)非零使该连接映射为同构。对(32)取上同调
于是给
$$
\dim H^1(C,\Omega_X^1|_C)=1.
\tag{33}
$$
另一方面，Hodge 对称给
$\dim H^2(X,\Omega_X^1)=h^{1,2}=1$，而 Serre 对偶给
$$
H^2(X,K_X\otimes\Omega_X^1)=H^0(X,T_X)^\vee=0.
$$
因此(31)的长正合列中
$$
H^1(C,\Omega_X^1|_C)\longrightarrow H^2(X,\Omega_X^1)
$$
是两个一维空间之间的满射，遂为同构。由正合性，(30)的余核为零，
证明了(29)的单射。全部使用的几何假设已在本段逐项写出。

### 7.2 原 cyclic 三次基变换族的 canonical fiber

取参数 $a\ne1/27$，考虑具体族
$$
B_a:\ v^3=(t-a)(1-27t),\qquad
S_a:\ y^2+xy+ty=x^3\quad\text{over }B_a.
\tag{34}
$$
三个分支点是 $a,1/27,\infty$，均全分歧，故 $B_a$ 是光滑 genus1
曲线。$a=0$ 正是(2)，并非另一个纯实现相同的替代对象。
对一般 $a$，$t=0$ 有三个不分歧原像，各为 $I_3$；$t=1/27$ 的
纤维也为 $I_3$。在 $a=0$，前三个合为原 $I_9$。

令 $r=1/t,z=v/t$，则
$$
z^3=r(1-ar)(r-27),\quad
Y^2+zXY+(1-ar)(r-27)Y=X^3,
\tag{35}
$$
$$
\Delta_\infty=(1-ar)^4(r-27)^5.
$$
所以无穷纤维始终光滑，且其 $j=0$。与(6)相同的二形式是
$\Omega_a=-dr/z\wedge\omega_{\rm new}$。由(35)，在 $z=0$ 有
$r=-z^3/27+O(z^6)$，所以该二形式恰有一阶零。
各 $S_a$ 的基本线丛次数是1，canonical divisor 为一次纤维；
因此这一光滑无穷纤维就是全部 canonical divisor。

原 $j$ 函数不随 $a$ 变，且其在这个局部参数中的展开为
$$
j(t)=512r+O(r^2)
=-\frac{512}{27}z^3+O(z^6).
\tag{36}
$$
这里系数非零，故 $j$ 恰有三阶零，而不是只知道该纤维有 $j=0$。

在特征零的 $\mathcal M_{1,1}$，$j=0$ 的 elliptic stabilizer 除去
所有点共有的 $\{\pm1\}$ 后为 $\mu_3$。局部 versal 变形参数 $u$
受其忠实作用，粗模参数为 $u^3$；等价地，$j=u^3$ 乘一个可逆函数。
把(35)的实际光滑椭圆族拉到该局部变形盘，(36)使 $u$ 在 $z=0$
恰为一阶。因此纤维化 $S_a\to B_a$ 在 canonical fiber 的 KS 映射
非零。适用7.1，得到
$$
d\mathcal P_{S_a}\text{ 单射，}
\tag{37}
$$
特别也适用于原 $a=0$ 的 $S$。这一步没有使用“光滑 canonical
fiber 自动给 Torelli”的错误捷径；所需非零由(36)实际支付。

### 7.3 参数变化确实改变曲面

尽管所有 $B_a$ 本身的 $j$ 都为0，$S_a$ 的曲面模量并非常数。
这里给出可直接区分它们的内在数据。

相对极小非等型椭圆曲面的 Kodaira 维数为1，Iitaka 纤维化唯一。
所以曲面的同构必诱导基曲线的同构，并保持“给每个纤维取 elliptic
$j$”的有限映射
$$
j_a:B_a\longrightarrow\mathbf P^1_j.
$$
原 $j(t)$ 的临界值只在 $0,1728,\infty$；这一点也可由(8)及
Weierstrass 恒等式 $c_4^3-c_6^2=1728\Delta$ 直接核查。
在排除有限多个 $a$ 后，$t=a$ 不是原 $j(t)$ 的临界点，也不在
上述三个值的原像。式(34)在 $t=a$ 三重分歧，故 $j_a$ 有恰一个
位于 $\{0,1728,\infty\}$ 外的临界值
$$
j(a)=\frac{(1-24a)^3}{a^3(1-27a)}.
\tag{38}
$$
另两个三次分支点 $1/27,\infty$ 仍映到 $\infty,0$，不产生新的
可变临界值。因此(38)是曲面同构必须保持的内在值。
它是非恒的有理函数；对一个一般给定值，只有有限多个 $a$。
所以 $S_a$ 的同构类不是常数。

对任何包含这条族的真正光滑射影代数实现，特征零下非恒模量使
generic KS 类非零；否则模映射的微分恒零，进而在可分的一维参数
上局部常数，与(38)矛盾。组合(37)，它的 weight2 period 微分
在一般点非零，因而 period map 非恒。有限基变换 $a=w^3$ 在
$w\ne0$ 可分，保留这一结论。下一节只需真正构造这种光滑射影
实现，并应用已发表的 cofinite Tate 定理；不得再补一个未经证明的
simultaneous-resolution projectivity 假设。


## 8. 真实射影同时解消与已发表的 cofinite Tate 定理

本节补齐7.3要求的代数族，并只调用已发表的定理。最终得到一个固定
整数 $q_0$，使本篇的 Tate、惰性整格与 Brauer 结论对所有
$q>q_0$ 无条件成立；不声称这个 $q_0$ 已有效计算，也不把小特征的
条件结论暗中升级。

### 8.1 全局射影起点和需要解消的准确位置

在 $K=\mathbf Q(\omega)$ 上取
$$
U=\operatorname{Spec}K[w,(1-27w^3)^{-1}],\qquad a=w^3.
\tag{39}
$$
令 $\mathcal B\to U$ 为下列平面三次曲线族：
$$
V^3=(T-w^3R)(R-27T)R\subset\mathbf P^2_{[T:V:R]}\times U.
\tag{40}
$$
三个分支点始终互异，所以这是光滑射影 genus1 族，带固定无穷截面
$[1:0:0]$。记该截面为 $\infty$，并取
$\mathcal L=\mathcal O_{\mathcal B}(\infty)$。
在 $\mathbf P(\mathcal O\oplus\mathcal L^2\oplus\mathcal L^3)$ 中
取有零截面的 Weierstrass 模型
$$
\mathcal W:\quad y^2+xy+ty=x^3.
\tag{41}
$$
这是一个全局射影模型：$1$ 是 $\mathcal L$ 的截面，$t$ 是
$\mathcal L^3$ 的截面；后者在无穷的极恰为3阶。
式(35)就是(41)在无穷的实际另一张图，其判别式在无穷为
$(-27)^5$。故那一带已是光滑椭圆族，不需一个未付的 IV* 收缩。

以下修改全部支撑在 $t=0$ 或 $t=1/27$，与无穷图不相交。
对应理想在其余部分等于结构层，故可按这个规定延拓为全局相干
理想；各次吹起均是全局射影态射。

先在有限 $t$ 图考察原有理 Weierstrass 曲面
$y^2+xy+ty=x^3$。其 $t=0$ 的 $A_2$ 点由吹起
$(x,y,t)$ 解消，产生 split $I_3$ 三角形
$C_0\cup C_1\cup C_2$。这一说法也可直接核：$t$ 图的严格变换为
$$
Y^2+XY+Y=tX^3,
$$
其两条例外直线交于 $(X,Y,t)=(-1,0,0)$，在那里对 $t$ 的偏导
非零；另两图光滑。三角形的三个节点均有 étale 局部方程
$xy=t$。

$\mathcal B\setminus\{\infty\}\to\mathbf A^1_t\times U$ 由一个
首一三次方程定义，是有限平坦态射。因此这个原吹起与该基变换
交换。对(41)施行其拉回，得到在 $t=0$ 与原已解消曲面基变换
一致的全局射影模型。

$t=1/27$ 的原有理曲面只有一个 nodal $I_1$ 纤维，且总空间光滑。
在(40)中它的逆像总有三重分歧；因为 $1/27-a$ 为单位，局部方程
经乘一个单位成为 $xy=v^3$，沿 $w$ 等奇异。吹起其节点截面
$(x,y,v)$ 解消这个 transversal $A_2$：$v$ 图为 $XY=v$，另两图
也光滑。所有纤维均得到原 $I_3$，这次修改与 $t=0$ 的修改互不相交。

记所得模型为 $\mathcal N\to U$。在 $w\ne0$ 时，$t=0$ 的覆盖
不分歧，所以该模型的曲面纤维已光滑。$w=0$ 时唯一还需处理的是
原 $I_3$ 三角形的三个节点。其局部方程准确化为
$$
xy=v^3+w^3=\prod_{j=0}^2(v+\omega^jw).
\tag{42}
$$
这里从 $xy=t$ 到(42)没有忽略单位：原基方程给
$v^3+w^3=t(1+27w^3-27t)$，括号在这些节点是单位，把它吸收到
$y$ 中即可。故 $\mathcal N$ 是正规三维模型，只在中央的这三个
点有上述奇点；光滑性是 étale 局部性质，这个检验足够。

### 8.2 全局 Weil 除子的四次吹起支付 projectivity

对 $i,j\in\{0,1,2\}$，取在 $t=0$、$v=-\omega^jw$ 上、对应原
$I_3$ 分量 $C_i$ 的全局 Weil 除子 $D_{i,j}\subset\mathcal N$。
它们是相应分量在全族中的闭包，故有确定的相干理想。
在(42)的相邻节点，若 $C_i$ 是 $x=0$ 支，它的理想就是
$(x,v+\omega^jw)$；另一端可交换 $x,y$。在三个奇点之外
$\mathcal N$ 正则，因而这些 Weil 除子均 Cartier，吹起在那里为同构。

现按次序吹起
$$
D_{0,0},\quad \widetilde D_{0,1},\quad
\widetilde D_{1,0},\quad\widetilde D_{1,1},
\tag{43}
$$
其中波浪号指严格变换。这给全局射影态射，不是只选择局部 analytic
small resolution。下面把每个局部图算完。

在一个相邻节点，第一次吹起 $(x,v+w)$。其两张严格变换图为
$$
\begin{array}{ll}
v+w=xs:&y=s(v+\omega w)(v+\omega^2w),\\
x=(v+w)r:&ry=(v+\omega w)(v+\omega^2w).
\end{array}
\tag{44}
$$
第一图用 $(x,s,w)$ 作光滑坐标；第二图只剩一个 $A_1$ 型的
同时解消问题。$D_{0,1}$ 在第二图的严格变换理想是
$(r,v+\omega w)$。再次吹起后的两图分别是
$$
\begin{array}{ll}
v+\omega w=rs:&y=s(v+\omega^2w),\\
r=(v+\omega w)r_2:&r_2y=v+\omega^2w.
\end{array}
\tag{45}
$$
前者有坐标 $(r,s,w)$，后者有坐标 $(r_2,y,w)$。因此这三张图均
对 $w$ 光滑。$w=0$ 的曲面上它们给 $A_2$ 的两条 $(-2)$ 曲线，
而 $w\ne0$ 时各中心原为 Cartier，完全不改变该曲面。

$C_0$ 在三角形中邻接两个节点，所以(43)的前两次吹起同时解决
这两个节点；两端交换 $x,y$ 不改变上述检验。第三个节点属于
$C_1\cap C_2$，前两次中心不经过它。后两次按同样的(44)–(45)
解决它。在已光滑的位置，后续严格变换仍是 Cartier 除子，故不
另造例外曲线。

综上得到真正的光滑射影族
$$
f:\mathcal X\longrightarrow U.
\tag{46}
$$
一般纤维正是(34)的相对极小曲面，有四个 $I_3$；中央纤维把原
$I_3$ 的每个节点插入两条曲线，准确成为 $I_9$，另一个 $I_3$
及无穷好纤维不变。因此
$$
\mathcal X_0\simeq S\otimes_{\mathbf Q}K
\tag{47}
$$
是实际模型同构。没有额外吹起光滑点，也没有靠纯 cohomology
识别中央纤维。式(44)–(45)同时证明整个态射在中央光滑；其余
位置由前述局部模型已核。

每条纤维都有 $p_g=q=1$。§7给这条族的 generic KS 和 weight2
period 微分非零；故它是下面定理要求的实际 $\hbar$-family。

### 8.3 扩散、已发表定理和原有理模型的下降

采用已发表原文：P. Hamacher、Z. Yang、X. Zhao，
*On the Tate conjecture for divisors on varieties with $h^{2,0}=1$ in
positive characteristics*，J. reine angew. Math.827(2025),1–58，
[DOI:10.1515/crelle-2025-0042](https://doi.org/10.1515/crelle-2025-0042)，
Theorem B。该定理的输入是一个光滑连通有限型整数基及其光滑
射影、几何连通纤维族；特征零部分须 $h^{2,0}=1$ 且所指
Kodaira–Spencer 映射非平凡。结论对该固定族所有充分大的剩余特征
及其所有点给除子 Tate 猜想。它不要求本篇各椭圆纤维不可约。

(39)–(46)只有有限个定义方程、相干理想和射影吹起。将它们扩散到
$\mathcal O_K[1/d]$，并增大固定 $d$，可使基 $\mathcal U$ 光滑于
$\mathbf Z[1/d]$、族仍光滑射影且纤维几何连通。理由分别是：
$K/\mathbf Q$ 在3外 étale；有限表现的光滑性为开条件；特征零
验证的有限开覆盖和射影结构只需排除有限多个分母。中央截面
$w=0$ 和(47)的模型同构一并扩散，故保留的是原曲面的好约化。
基可取连通部分，包含这条中央截面和上面的非恒族。

§7实际证明的 period 非恒也等价于 Theorem B 中
$T_{U/K}\to\operatorname{Hom}(R^1f_*\Omega^1,R^2f_*\mathcal O)$
非零：它是(29)的 Serre 对偶。所有定理假设现已逐项支付。
因此存在固定 $q_0$，使每个素数 $q>q_0$、每个位
$\mathfrak q\mid q$，$\mathcal X_{0,\mathfrak q}$ 满足 Tate。

若 $q$ 在 $K$ 中惰性，该结论先在 $\mathbf F_{q^2}$ 上取得，
这里完全没有用“$q^2\equiv1$ 可替代素数 $q\equiv1$”的错误步骤。
它可下降到原 $\mathbf F_q$ 模型：任给 $\mathbf F_q$ 固定的
有理 $\ell$-adic 除子类，先在 $\mathbf F_{q^2}$ 用 Tate 写成除子
的有理线性组合，再取 $(D+\sigma_qD)/2$；由除子 norm，结果在
$\mathbf F_q$ 定义且原 cohomology 类不变。$\ell=2$ 时也在
$\mathbf Q_2$ 中合法。分裂情形已直接得到 $\mathbf F_q$ 结论。

由此无条件得到
$$
\boxed{\exists q_0\quad\forall\text{ 素数 }q>q_0:\
S_q/\mathbf F_q\text{ 满足除子 Tate 猜想。}}
\tag{48}
$$
惰性时同样已在 $\mathbf F_{q^2}$ 满足 Tate，故§3–4的全部后继
推导适用：几何 MW 秩2、整格 $(q/3)A_2$、准确两 Frobenius 方向、
两常数域的 Brauer 群零，以及原54图的整交公式均保持。
对 $5\le q\le q_0$，本篇仍仅保§2的条件推导，不冒称已付。
这项 cofinite 结论完全不以 Guo–Yang 预印本的正面定理为输入。

(48)仍只是这张辅助曲面的除子定理。它没有把原 $Y_{j,0}$ 的混合
Abel–Jacobi 类变成除子，也没有给出(26)的实际非零值或原普通
$p$ 位的局部非零；这些仍由同一原完整54图继续处理。
