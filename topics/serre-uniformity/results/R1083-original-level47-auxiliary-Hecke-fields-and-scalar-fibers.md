# R1083：原 level 47 的辅助系数域障碍与 4513 的完整标量分支

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明。** 原 $X=X_{\rm ns}^+(47)$ 在辅助素数 $283$
没有泛纤维为 $\mathbf Q_{283}$ 的 Hecke 因子，因此不能在该素数
选择一个实际等于 $\mathbf Z_{283}$ 的完整局部 Hecke 块。
这不影响 R1074 已完成的同点 Kummer 筛选。

本文另外付清辅助素数 $4513$ 的全部标量 Frobenius 情形：
它们准确来自 $j=1728$ 的两个 quartic twists，必须保留全部
$1081$ 个原 necklaces；原 coarse $j=1728$ 纤维有 $553$ 个点。
$4513$ 允许尖点型系数域的一次局部因子，并使八个剩余原 CM 类中的
六个普通约化。实际 $4513$ 的十六个一次块已由
[R1081](R1081-certified-original-level47-Cartan-trace-and-integral-Hecke-algebra.md)
认证；本文给其类型来源及完整几何覆盖，不断言 MW 不饱和、
局部高度赋值一或盘内唯一性。

全篇使用原 full $X_{\rm ns}^+(47)$，不搬用带额外 tame 六水平的
$X_1$ 格，也不搬用 level $41$ 的矩阵。本文没有运行数学程序。

## 1. 原正规化子所允许的全部有限类型

置 $G=\operatorname{GL}_2(\mathbf F_{47})$，
$C=\mathbf F_{47^2}^{\times}$，$N=C\rtimes\langle w\rangle$。
原模水平含中心，故只需中央角色平凡的有限表示。
记 $\epsilon$ 为 $\mathbf F_{47}^{\times}$ 的二次角色。

这里可直接使用已刊 Mercuri–Schoof 的原 full-level 实现：
其 Proposition 5.2 将 level $47^2$ 的每个实际 newform $f$
放进一个在原系数域 $F_f=\mathbf Q(a_n(f))$ 上定义、
绝对不可约的有限 $G$-表示 $V_f$。原非分裂正规化子微分正是
$V_f^N$；所用是同一 Hecke 谱，尚未声称任何同源在辅助素数处
保持整格。R1080 也在此同一个谱上认证原 $J$ 的全秩。

为保全遗漏检查，重写正规化子条件。
对主系列
$\operatorname{Ind}_B^G(\chi,\chi^{-1})$，$\chi^2\ne1$，
$C$-固定线一维；在 $Cw$ 的 split 半部 character 为
$2\chi(-1)$，另一半为零，所以 $w$ 在此线上作用为
$\chi(-1)$。因此只有偶角色 $\chi$ 保留。
$\mathbf F_{47}^{\times}$ 阶为 $46$；每个非平凡偶角色准确具有阶 $23$。

对尖点型 $V_\theta$，$\theta$ 是
$C/\mathbf F_{47}^{\times}$ 的非二次角色，
该商阶为 $48$。其 $C$-固定线一维；$Cw$ 的非分裂半部
character 为 $-2\theta(t_2)$，其中 $t_2$ 是商中的二阶元，
split 半部为零。因此保留条件为 $\theta(t_2)=-1$。
写 $\theta$ 的指数为奇数 $r$，模 $48$ 并商去 $r\leftrightarrow-r$。
它的阶只能是 $48$ 或 $16$。

Steinberg 是 $\mathbf P^1(\mathbf F_{47})$ 置换表示去掉常数，
$C$ 传递，故没有 $C$-固定向量。
$\operatorname{St}\otimes(\epsilon\circ\det)$ 的 $C$-固定线
上的 $w$ 特征值为 $\epsilon(-1)=-1$，也被排除。
一维非平凡 determinant 角色在 $C$ 上已非平凡；
一维平凡类型若产生全局尖点形式，就来自去掉 $47$ 水平后的
$S_2(\operatorname{SL}_2(\mathbf Z))=0$。
以上也处理了主系列的所有退化情形。没有遗漏二次 Steinberg 或
旧的 unramified 类型。

于是每个实际系数域 $F_f$ 至少包含下表中的一个子域：
$$
\begin{array}{c|c|c}
\text{原有限类型}&\text{角色阶}&\text{必含的子域}\\ \hline
\text{主系列}&23&
 K_{23}=\mathbf Q(\zeta_{23}+\zeta_{23}^{-1}),\ [K_{23}:\mathbf Q]=11\\
\text{尖点}&48&
 K_{48}=\mathbf Q(\zeta_{48}+\zeta_{48}^{-1}),\ [K_{48}:\mathbf Q]=8\\
\text{尖点}&16&
 K_{16}=\mathbf Q(\zeta_{16}+\zeta_{16}^{-1}),\ [K_{16}:\mathbf Q]=4.
\end{array}
\tag{1083.1}
$$

### 1.1 为什么这些是真正的系数子域

有限主系列在适当 split 元素上的 character 含
$\chi(a)+\chi(a)^{-1}$；尖点型在非分裂元上的 character 含
$-\theta(a)-\theta(a)^{-1}$。取角色的 primitive 值，分别生成
(1083.1) 的实 cyclotomic 域。

另一方面，$V_f$ 在 $F_f$ 上定义，所以每个实际有限群作用的
trace 都属于 $F_f$。这直接给出子域包含关系。
这是 Mercuri–Schoof §6 在 principal-series 与 cuspidal 两处
分别明确写出的结论，也可由上面的 trace 证明立即重得。
不需要把某个模辅助素数的有限表示的定义域，错误认成整个
特征零系数域。

对原 $N$-固定线读取 Hecke 特征值后，系数域仍是同一个 $F_f$：
有限群作用与 Hecke 作用交换，且 strong multiplicity one
锁定原 newform 的整套特征值。此处不把不同的二次 twist、
不同的 Galois 共轭或不同的局部有限类型合并成一个较小的域。

## 2. $283$ 没有实际一次泛纤维 Hecke 块

素数 $\ell\nmid n$ 在 $K_n=\mathbf Q(\zeta_n)^+$ 中的剩余次数，
是 $\ell$ 在 $(\mathbf Z/n\mathbf Z)^\times/\{\pm1\}$ 中的阶。
本例三个 cyclotomic 域在 $283$ 都无分歧。

模 $23$ 有
$$
283\equiv7,\qquad 7^2=3,\quad 7^4=9,\quad
7^8=12,\quad 7^{11}=-1 .
$$
商群阶为素数 $11$，而 $7\ne\pm1$，所以实剩余次数为 $11$。

模 $48$ 有
$$
283\equiv43,\qquad 43^2\equiv25,\qquad43^4\equiv1,
$$
且 $43,25$ 均不是 $\pm1$，所以实剩余次数为 $4$。
模 $16$ 同样有
$$
283\equiv11,\qquad11^2\equiv9,\qquad11^4\equiv1,
$$
实剩余次数也是 $4$。

因此，对任一实际原系数域 $F_f$ 及其上任一位 $\mathfrak q\mid283$，
$$
[F_{f,\mathfrak q}:\mathbf Q_{283}]
 \ \text{至少为 }11\text{ 或 }4,\qquad
\boxed{F_{f,\mathfrak q}\ne\mathbf Q_{283}.}
\tag{1083.2}
$$
更准确地，完成域内含相应的无分歧 $11$ 次或 $4$ 次子扩张。

令 $\mathbb T$ 是原 $J$ 上实际整 Hecke 代数。
若某个完整局部因子
$(\mathbb T\otimes\mathbf Z_{283})_{\mathfrak m}$
等于 $\mathbf Z_{283}$，反转 $283$ 后就给一个
$\mathbf Q_{283}$ 泛纤维因子，与 (1083.2) 矛盾。故
$$
\boxed{
(\mathbb T\otimes\mathbf Z_{283})_{\mathfrak m}
 \not\simeq\mathbf Z_{283}
\quad\text{对每个实际局部因子成立。}}
\tag{1083.3}
$$

**整序边界必须保留。**
(1083.2) 不意味着任意非极大 Hecke order 的每个剩余域次数
也至少为四。例如对一个无分歧扩张的整数环 $\mathcal O$，
order $\mathbf Z_\ell+\ell\mathcal O$ 的剩余域仍可能是
$\mathbf F_\ell$。本文排除的是完整泛纤维一次因子以及真正
等于 $\mathbf Z_{283}$ 的局部环，不由此排除一个非正规 order
出现 $\mathbf F_{283}$ 剩余角色。

R1074 在 $283$ 的完整同点标签结论不使用 (1083.3) 所排除的环，
所以完全保留。不能继续在 $283$ 搜索一个已被 (1083.3)
排除的 rank-one integral Hecke block 来付款新的高度判据。

## 3. $4513$ 的实际局部域与 CM 约化

取
$$
q=4513,\qquad q-1=96\cdot47,\qquad q\equiv1\pmod{48}.
\tag{1083.4}
$$
这是素数：$\sqrt{4513}<68$；按
$2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67$
试除，其余数分别为
$1,1,3,5,3,2,8,10,5,18,18,36,3,41,1,8,29,60,24$，
均非零。这里仅为纸面有限整除证明，没有执行素数测试。

因为 $q\equiv1\bmod48$，$K_{48}$ 与 $K_{16}$ 在 $q$ 完全分裂；
(1083.1) 对尖点型不再阻止一次完成域。
对主系列仍有阻碍：$q\equiv5\bmod23$，
$5^{11}\equiv-1\bmod23$、$5\ne\pm1$，
所以其 $K_{23}$ 子域的实剩余次数仍是 $11$。
因此若出现真正的 $\mathbf Q_q$ Hecke 因子，它一定来自尖点型，
但尖点型本身尚不保证这样的因子实际存在。
R1081 的实际 squarefree Hecke 证书另外付清存在性：
$16$ 维因子给六个、$24$ 维因子给十个一次块，$33$ 维因子没有一次块。

R1074 八个原 CM 点的虚二次域只有
$\mathbf Q(\sqrt{-3}),\mathbf Q(i),\mathbf Q(\sqrt{-7}),
\mathbf Q(\sqrt{-2})$。$q$ 不整除各 CM conductor，
而
$$
q\equiv1\pmod3,\quad q\equiv1\pmod4,\quad q\equiv1\pmod8,
\qquad q\equiv5\pmod7 .
$$
所以前、第二、第四个域在 $q$ 分裂，第三个惰性。
由原 CM 约化判据，以下六点在 $q$ 普通约化：
$$
J=0,\ 1728,\ -12288000,\ 54000,\ 287496,\ 8000;
\tag{1083.5}
$$
而 $J=-3375,16581375$ 在 $q$ 超奇异约化。
这是辅助 $4513$ 处的性质，没有改变原坏 $47$ 圆盘的约化类型。

普通约化允许后继从真正的 Serre–Tate 参数计算 CM 点差的
$B_q=q+1-T_q$ 对数；它不自动给所需对数、生成元或高度为单位。
特别不能把某个只针对 ordinary CM 的 jet 公式用于上述两个
supersingular CM 点。

## 4. $4513$ 的所有标量 Frobenius，及完整粗模覆盖

设 $E/\mathbf F_q$，$\pi$ 为其实际 $q$-Frobenius。
模 $47$ 的行列式为 $q\equiv1$。
如果 $\pi|E[47]$ 为标量，则只能是 $\pm I$。
必要时取二次 twist，将它变为 $+I$；于是
$E[47]\subset E(\mathbf F_q)$，从而
$47^2\mid\#E(\mathbf F_q)$。

Hasse 给出精确整数区间
$$
4380\le\#E(\mathbf F_q)\le4648.
$$
区间内唯一的 $47^2=2209$ 倍数为 $4418$。
所以在上述 twist 上
$$
\operatorname{tr}\pi=96,\qquad
\pi=48\pm47i,\qquad
(\operatorname{tr}\pi)^2-4q=-4\cdot47^2.
\tag{1083.6}
$$
该曲线普通，几何 endomorphism order 是 $\mathbf Q(i)$ 中
包含 $\mathbf Z[\pi]$ 的 order，故 conductor 只能是 $1$ 或 $47$。

对任何 $q\ne47$ 的椭圆曲线 endomorphism $\alpha$，
$\alpha$ 在 $E[47]$ 上为零，当且仅当
$\alpha\in47\operatorname{End}_{\overline{\mathbf F}_q}(E)$：
前向由 $\alpha$ 经商 $E/E[47]$ 因子化，再用原 $[47]$
识别该商，后向显然。因此在 (1083.6) 中
$$
\pi\equiv I\pmod{47}
\quad\Longleftrightarrow\quad
1\pm i\in\operatorname{End}(E)
\quad\Longleftrightarrow\quad
\operatorname{End}(E)=\mathbf Z[i].
\tag{1083.7}
$$
原曲线不 twist 时的 $\pi\equiv-I$ 完全相同。
最大 order 的 $j$ 正是 $1728$，故
$$
\boxed{\text{原 }q\text{-Frobenius mod }47\text{ 为标量，只可能在 }j=1728.}
\tag{1083.8}
$$
仅有 trace $\pm96$ 不够：conductor-$47$ order 的曲线模 $47$
为非标量重根，不能把它也当作全项链固定的标量分支。

### 4.1 $j=1728$ 的四个 twists 和 $553$ 个真实点

$q\equiv1\bmod4$，所以有四个 quartic twists。
最大 order 中范数 $q$ 的 Frobenius 为
$\pm(48+47i),\pm i(48+47i)$，允许同时复共轭。
因此四个 traces 为
$$
\pm96,\qquad\pm94.
$$
前两个模 $47$ 为 $\pm I$，固定全部
$47(47-1)/2=1081$ 个原 necklaces；
后两个模 $47$ 为 $\pm i$，其 projective class 是非分裂对合，
固定 $(47+3)/2=25$ 个 necklaces。

几何 effective automorphism group 是
$\operatorname{Aut}(E)/\{\pm1\}\simeq C_2$。
以一个 scalar twist 为参考，Frobenius 在 necklace 集上平凡，
而非平凡 automorphism 的 fixed count 为 $25$。
twisted Burnside 因而给真实 coarse 纤维
$$
\boxed{\#j^{-1}(1728)(\mathbf F_q)=(1081+25)/2=553.}
\tag{1083.9}
$$
枚举全部四 twists 得 $2\cdot1081+2\cdot25=2212$
个 raw necklace 表示；它们不是 $2212$ 个粗模点，
也不是仅有 $1081$ 个粗模点。后继评价仍须按原粗模相位及
automorphism 等价处理重复。

### 4.2 $j=0$ 及其余纤维

纸面等式 $4513=25^2+3\cdot36^2$ 给
$\mathbf Q(\sqrt{-3})$ 中范数 $q$ 的元 $25+36\sqrt{-3}$。
六个 sextic twists 的 traces 是
$$
\pm50,\quad\pm133,\quad\pm83.
\tag{1083.10}
$$
它们模 $47$ 均非 $0,\pm2$。
$47$ 在该 CM 域惰性，故每个 Frobenius 都属于实际非分裂
Cartan 且非标量、非对合，于是恰固定一个 necklace。
effective $C_3$ 的 twisted Burnside 给
$$
\#j^{-1}(0)(\mathbf F_q)=1.
\tag{1083.11}
$$

其它 $j$ 上没有 scalar 分支。
非标量重根的 projective 元有阶 $47$，而 $N_{\rm ns}$ 的
projective 阶为 $2(47+1)=96$，所以没有 fixed necklace。
split 非对合半单元素也不能在非分裂 Cartan 或其 reflection coset；
在 determinant 一的本例中，split projective 对合不可能发生，
因为 trace 零元素的特征多项式为 $T^2+1$，$-1$ 在
$\mathbf F_{47}$ 非平方。
剩下的非分裂半单元素按原 R1073 固定数一或二十五处理。

全部 $23$ 个 cusps 在 $\mathbf F_q$ 上有理，因为
$q\equiv1\bmod47$。它们仍必须使用原规范 cusp 标签计入，
不能由 affine 模型枚举省掉。

## 5. 原同点标签算法在新素数的准确改动

这里尚未执行 $4513$ 筛选，但其数学输入范围已经明确。

在非标量非分裂分支，原选择 $P,Q_0=\pi P$ 仍给独立
$47$-torsion 基。标量 $j=1728$ 分支必须另取独立 $P,Q_0$，
并由真实 Weil pairing 核准；这时 $Q_0=\pi P$ 会退化，
不能沿用。保原 nonsquare $\delta=5$，
全部 matrices
$$
J=\begin{pmatrix}a&b\\c&-a\end{pmatrix},
\qquad a^2+bc=5,\qquad J\sim-J
$$
给全部原 $1081$ 个 necklaces；$c\ne0$ 自动成立，
因为 $5$ 非平方。原坐标变换与 Weil pairing 均仍为
$$
(v_0,v_1)=(u-aw/c,w/c),\qquad
e_{47}(P,JP)=e_{47}(P,Q_0)^c.
\tag{1083.12}
$$

对于 scalar $\pi=\pm I$，每个半点 $\{\pm P_v\}$ 已由 Frobenius
固定；$\psi_5$ 是偶函数，所以它在这些半点上的值都属于
$\mathbf F_q$。原每个 norm/± 纤维仍有 $48$ 个半点，
其乘积、augmentation-zero 指数和完整 $\psi_5$ 评价公式不变。

实际 Kummer 读数现在取
$$
\log_\zeta(z^{(q-1)/47})=\log_\zeta(z^{96}),
\tag{1083.13}
$$
不能把 $283$ 的指数六照抄。
每个角色的 global circular-unit 读数也要按同一 $\zeta$、
同一个指数 $96$ 重新计算。
若某个读数为零，仍只能比较等式，不能除以它。
任何 root-of-unity 基变换必须对所有角色和同一粗模点同步，
沿用 R1073 §9 的 $a^{1-R}$ canonical-root 运输。

这些规则给完整覆盖方法，但不声称 $4513$ 的实际标签像
已经计算、像的基数等于点数，或新的局部条件已经排除某个原候选。

## 6. 一个可认证实际整 Hecke 块与 Hodge 自由性的有限准则

这一节给出独立于数值的完整准则；R1081 已在 $283$ 和 $4513$
实际执行并满足它。本节不另行运行或重算该证书。
令 $\mathbb T\subset\operatorname{End}_{\mathbf Q}(J)$
为原整数 Hecke 代数，$A=\mathbb T\otimes\mathbf Q$。
原 newform 重数一给
$\dim_{\mathbf Q}A=\dim J=73$。
取实际整数 Hecke 组合 $H\in\mathbb T$，令
$P_H(X)$ 为它在原 $73$ 维 Hodge 谱上的特征多项式。
Hecke 特征值为代数整数，故 $P_H\in\mathbf Z[X]$。

**准则。** 若 $P_H\bmod q$ 为 squarefree，
则
$$
\boxed{
\mathbb T\otimes\mathbf Z_q
 =\mathbf Z_q[H]
 \simeq\prod_i\mathcal O_i,}
\tag{1083.14}
$$
其中 $\mathcal O_i/\mathbf Z_q$ 是模 $q$ 各不可约因子次数所给的
无分歧整数扩张。特别，线性因子恰给真正的
$\mathbf Z_q$ 局部 Hecke 因子。

证明：squarefree 迫 $H$ 有 $73$ 个不同的特征值，
故其最小多项式就是 $P_H$，且
$\mathbf Q_q[H]=A\otimes\mathbf Q_q$。
$\mathbf Z_q[X]/P_H$ 是有限 étale 代数，因而已是此泛纤维的
最大整序。实际 $\mathbb T\otimes\mathbf Z_q$ 是同一代数中的
整序，包含 $\mathbf Z_q[H]$，只能相等。

此外 $q\ne47$ 时原 $J$ 良好，所有实际整数 Hecke endomorphisms
延伸到其阿贝尔模型。其 Hodge 格及 Lie 格都是
$\mathbb T\otimes\mathbf Z_q$ 模上的有限无挠模，
在每个泛纤维因子上秩一。
由 (1083.14) 逐个无分歧 DVR 因子应用无挠模结构，
得到
$$
\boxed{
\omega_{\mathcal J}\ \text{及 }\operatorname{Lie}\mathcal J
\text{ 均为 }\mathbb T\otimes\mathbf Z_q\text{ 上的自由秩一模。}}
\tag{1083.15}
$$
这里是真正原 Néron/阿贝尔模型的格，不通过未经检验的同源
运输整性。因而一次完整 squarefree 证书同时支付完整局部
Hecke 环及其 Hodge/Lie 自由性。
它不支付 $q\nmid\#J(\mathbf F_q)$、MW 饱和性、指定 CM jet、
迹零对应的剩余特征值为零或高度赋值一。

若 (1083.14) 在 $283$ 被认证，所有不可约因子的次数还必须
满足 §2 的真实子域限制，尤其不能出现线性因子。
这可作为独立来源核对，不以剩余 order 的偶然线性角色代替。

## 7. 来源、审核与接续范围

- P. Mercuri–R. Schoof,
  *Modular forms invariant under non-split Cartan subgroups*,
  Math. Comp. **89** (2020), 1969–1991，
  [作者正式 offprint](https://reneschoof.github.io/mcom3503.pdf)。
  本次亲读 Proposition 2.1、Proposition 5.2 及 §6：
  原 finite representation 在 $F_f$ 上定义见印刷1978页；
  principal-series 与 cuspidal character 子域分别见1979、1981页。
  §1 另直接核所有正规化子符号及退化类型。
- [R1029](R1029-original-lowest-inertia-type-integral-Hecke-splitting.md) §2
  已给相同有限群 character 的完整证明；本篇去掉 tame 六水平，
  用原 level-one 无形式来处理 unramified 来源，未引用其 $X_1$ 整格。
- [R1073](R1073-original-split-auxiliary-cuspidal-sieve.md)：
  真正 full-$47$ 同点标签、全部 norm/± 乘积与 coarse 相位。
- [R1074](R1074-certified-original-p47-eight-CM-disks.md)：
  原八个 CM 类、$283$ 同点筛选及坏 $47$ 高度；
  §4 的 Frobenius 与 coarse 计数在本文重新证明。
- [R1078](R1078-original-level47-Cartan-correspondences-and-fixed-cycles.md)：
  全原角与 fixed cycles，包含全部 $23$ cusps。
- [R1080](R1080-certified-full-level47-Jacobian-rank.md)：
  原 full Jacobian 的 $73$ 维 Hecke 谱及全 rank；
  本文不重跑其任何 $L'$ 计算。

root 已亲读 Mercuri–Schoof 原文并复核全部推导；
o2_high_coefficient 已独立纸核 §1–2 的类型/真系数域与所有剩余次数，
以及 §3–4 的 $4513$ Hasse 区间、实际 endomorphism order、
scalar 判据、四/六 twists、twisted Burnside 和六普通/二超奇异范围。

Serre 主目标及八个原 $47$ 圆盘的内部有理唯一性仍 OPEN。
实际辅助因子已由 R1081 付清；下一项是新 $4513$ 同点标签、
原 CM 对数与完整高度的共同输入，不得把有限 étale 整块当成
已经存在的 MW 非饱和性或高度单位。
