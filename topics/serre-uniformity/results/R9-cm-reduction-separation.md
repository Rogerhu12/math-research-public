# R9. 大素数层有理 CM 点在辅助素数处的约化分离

日期：2026-11-12。会话：`serre-uniformity-astra/2026-11-12`。

**状态：已证明。** 本结果只分离已经是 CM 的点。它不排除非 CM 有理点，不证明 quadratic Chabauty 函数的导数为单位，也不完成 Serre 一致性。

## 结论

令
$$
\mathcal D=\{-3,-4,-7,-8,-11,-12,-16,-19,-27,-28,-43,-67,-163\}.
$$
设 $p>163$ 为素数，$X=X_{\rm ns}^+(p)$。则：

1. $X(\mathbb Q)$ 中的 CM 点恰与满足 $\left(\frac{\Delta}{p}\right)=-1$ 的 $\Delta\in\mathcal D$ 一一对应。对应的 Cartan 子代数就是完整 CM 自同态环在 $p$-挠点上的像。特别地，即使 $j=0$ 或 $1728$，每个允许的 CM $j$ 也恰有一个有理点，不能另加未由 CM 环产生的有理 Cartan 结构。
2. 若 $\ell\ge5$ 是素数且 $\ell\ne p$，则约化映射
   $$
   X(\mathbb Q)_{\rm CM}\longrightarrow X(\mathbb F_\ell)
   $$
   是单射。这里使用 $X$ 在 $\ell$ 处的好约化模型。

取 $p>163$ 是为了同时避开所有 CM 判别式的素因子和选定模型的坏约化素数。本文不把 $p=67,163$ 等分歧情形默认为已处理。

## 1. 使用的经典事实与显式好约化模型

使用以下已确立的基础结果：

- 有理 CM $j$ 值的十三项分类，以及与 $\mathcal D$ 的对应。可见 Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves* (1994), Appendix A §3；便于在线核对的同一张表见 Zywina, *On the possible images of the mod $\ell$ representations associated to elliptic curves over $\mathbb Q$*, §1.9, Table 1，[作者原文](https://pi.math.cornell.edu/~zywina/papers/PossibleImages/PossibleImages.pdf)。这里仅使用该表转述的经典 CM 分类，不使用新的像分类猜想。
- Serre (1972), *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, §1.11, Proposition 11 及其推论（印刷页 273–274）、Proposition 12（页 275）：在 $\mathbb Q_p$ 上好普通约化的模 $p$ 惯性半单化为 $\chi_p\oplus1$；野惯性平凡时惯性像为 $\operatorname{diag}(\mathbb F_p^\times,1)$。好超奇异约化时惯性像为完整非分裂 Cartan，阶 $p^2-1$。[原文](https://www.college-de-france.fr/media/jean-pierre-serre/UPL5874918517843398173_Serre_proprie_te_s_galoisiennes_des_courbes_elliptiques.pdf)。
- 好约化下自同态约化的单射性、素于剩余特征的挠群保持性、同源通过其核的商分解；见 Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed. (2009), III §§4,6、VII §3。
- 自同态代数是 $\mathbb Q$、虚二次域或正定四元数代数，且对偶同源给出标准对合，约化范数等于次数；见 Voight, *Quaternion Algebras* (Springer, 2021), §42.1.3、Lemma 42.1.5。[开放原文](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42)。
- 对 $\ell\ge5$、$\ell\ne p$，非尖点模解释的几何点为椭圆曲线连同非分裂 Cartan 子代数的同构类；忘掉定向对应取正规化子。这是 $X_{\rm ns}^+(p)$ 的定义性模解释。固定椭圆曲线 $E$ 后，$j$ 纤维是 $\operatorname{Aut}(E)$ 在 Cartan 子代数集合上的轨道集合。

为避免用潜在好约化替代下面真正需要的 $p$ 处好约化，选用下表中的 $\mathbb Q$ 模型。五元组按
$$
y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6
$$
排列；$\Delta_E$ 表示方程判别式，区别于 CM 整环判别式 $\Delta$。

| CM 判别式 $\Delta$ | $(a_1,a_2,a_3,a_4,a_6)$ | $\Delta_E$ | $j$ |
|---|---|---|---|
| $-3$ | $(0,0,0,0,1)$ | $-2^4 3^3$ | $0$ |
| $-4$ | $(0,0,0,-1,0)$ | $2^6$ | $1728$ |
| $-7$ | $(1,-1,0,-2,-1)$ | $-7^3$ | $-3375$ |
| $-8$ | $(0,-4,0,2,0)$ | $2^9$ | $8000$ |
| $-11$ | $(0,-1,1,-7,10)$ | $-11^3$ | $-32768$ |
| $-12$ | $(0,0,0,-15,22)$ | $2^8 3^3$ | $54000$ |
| $-16$ | $(0,0,0,-11,14)$ | $2^9$ | $287496$ |
| $-19$ | $(0,0,1,-38,90)$ | $-19^3$ | $-884736$ |
| $-27$ | $(0,0,1,-30,63)$ | $-3^5$ | $-12288000$ |
| $-28$ | $(0,-42,0,-7,0)$ | $2^{12}7^3$ | $16581375$ |
| $-43$ | $(0,0,1,-860,9707)$ | $-43^3$ | $-884736000$ |
| $-67$ | $(0,0,1,-7370,243528)$ | $-67^3$ | $-147197952000$ |
| $-163$ | $(0,0,1,-2174420,1234136692)$ | $-163^3$ | $-262537412640768000$ |

这些数值由标准整式恒等式直接得到：
$$
\begin{aligned}
b_2&=a_1^2+4a_2,& b_4&=a_1a_3+2a_4,& b_6&=a_3^2+4a_6,\\
b_8&=a_1^2a_6+4a_2a_6-a_1a_3a_4+a_2a_3^2-a_4^2,\\
c_4&=b_2^2-24b_4,\qquad
\Delta_E=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6,\qquad
j=c_4^3/\Delta_E.
\end{aligned}
$$
所以每个模型在所有 $p>163$ 都有好约化。任一有理 CM $j$ 纤维都可使用本表的固定模型来描述其几何 Cartan 结构；不需要要求该纤维中每个可能的扭曲模型在 $p$ 处都有好约化。

## 2. CM 自同态的定义域及惯性中央化

令 $E/\mathbb Q$ 为表中模型，完整 CM 环为 $\mathcal O$，对应虚二次域为 $K$。取 $\mathbb Q$ 上非零不变微分 $\omega$。对每个几何自同态 $\alpha$，写
$$
\alpha^*\omega=c_\alpha\omega.
$$
映射 $\alpha\mapsto c_\alpha$ 是环同态。在特征零中，非零自同态是可分同源，微分不为零，故该映射单射；其分式域像实现了 $K\subset\overline{\mathbb Q}$。由于 $\omega$ 定义在 $\mathbb Q$ 上，
$$
c_{\sigma\alpha\sigma^{-1}}=\sigma(c_\alpha).
$$
因此，固定 $K$ 的每个 $\sigma$ 固定所有自同态。特别地，所有 CM 自同态定义于 $K$；这里包含 $j=0,1728$ 的情况。

因 $p>163$，$K/\mathbb Q$ 在 $p$ 不分歧，故 $I_p$ 固定 $K$。设 $V=E[p]$，则 $I_p$ 的像中央化
$$
A=\mathcal O/p\mathcal O\hookrightarrow\operatorname{End}_{\mathbb F_p}(V).
\tag{2.1}
$$
嵌入的单射性可直接说明：若 $\alpha$ 杀掉 $E[p]$，则它通过 $[p]$ 分解，所以 $\alpha\in p\mathcal O$。由于 $p\nmid\Delta$，$A$ 是二次 étale 代数：惰性时为 $\mathbb F_{p^2}$，分裂时为 $\mathbb F_p\times\mathbb F_p$。其在 $\operatorname{GL}(V)$ 中的中央化子恰为 $A^\times$。

### 惰性时

惯性像包含于非分裂 Cartan $C_0=A^\times$，故其阶素于 $p$，野惯性平凡。如果约化普通，Serre 的 Proposition 11 推论会给出惯性像 $\operatorname{diag}(\mathbb F_p^\times,1)$，其中有非标量的分裂半单元素；但 $C_0$ 的每个非标量元素的特征多项式不可约，矛盾。

所以约化超奇异，Proposition 12 给出惯性像阶 $p^2-1$，从而
$$
\bar\rho_{E,p}(I_p)=C_0.
\tag{2.2}
$$

### 分裂时

惯性像包含于分裂 Cartan $A^\times$。若约化超奇异，Proposition 12 所给的阶 $p^2-1$ 大于 $(p-1)^2=|A^\times|$，不可能。因此约化普通，野惯性同样平凡，Proposition 11 推论给出
$$
\bar\rho_{E,p}(I_p)\sim
\{\operatorname{diag}(a,1):a\in\mathbb F_p^\times\}.
\tag{2.3}
$$
这些论证只用了经典惯性定理和 CM 环作用，没有另外假定 CM 的分裂/超奇异约化判别定理。

## 3. 粗模空间的自同构轨道：排除额外有理 CM 结构

记 $\mathscr C$ 为 $\operatorname{End}(V)$ 中所有非分裂二次子代数的集合。为简化符号，也用 $C$ 表示相应的乘法群。共轭作用下，$C$ 的稳定子就是其正规化子 $N(C)$。

有两个初等群事实：

1. $C$ 的非标量元素特征多项式不可约，其中央化子就是 $C$。
2. $N(C)\setminus C$ 中每个元素在 $\operatorname{PGL}(V)$ 中的阶为 $2$：将 $V$ 识别为 $\mathbb F_{p^2}$，它形如 $z\mapsto az^p$，平方为标量 $a^{p+1}$。

固定 CM 曲线 $E$ 后，粗模 $j$ 纤维的几何点为 $\operatorname{Aut}(E)$ 在 $\mathscr C$ 上的轨道。标量 $\pm1$ 的共轭作用平凡，故每个轨道的长度不超过
$$
m=|\operatorname{Aut}(E)/\{\pm1\}|\le3.
\tag{3.1}
$$
$j=0$ 时 $m=3$，$j=1728$ 时 $m=2$，其他情况 $m=1$。这正是特殊自同构不能忽略的地方。

若一个轨道 $\mathscr O$ 对应有理点，则它整体 Galois 不变。对任意 $C\in\mathscr O$，设 $T=\bar\rho_{E,p}(I_p)$。于是 $T\cdot C\subseteq\mathscr O$，从而
$$
[T:T\cap N(C)]\le m.
\tag{3.2}
$$

### 3.1 惰性情形的唯一性

由 (2.2)，$T=C_0$，其射影像是阶 $p+1$ 的循环群。由 (3.2)，$T\cap N(C)$ 的射影像至少有 $(p+1)/m>2$ 个元素。它是循环群的子群，故有一个射影阶大于 $2$ 的元素 $h$。

群事实 2 表明 $h$ 必属于 $C$；它也是 $C_0$ 中的非标量元素。由群事实 1，其中央化子同时为 $C$ 和 $C_0$，所以 $C=C_0$。因此所有有理粗模点都来自唯一的 CM Cartan。

另一方面，Galois 作用正规化完整自同态环，故正规化其像 $A$，所以 $C_0$ 本身定义一个有理点。由此得到恰好一个有理点，连 $j=0,1728$ 也没有额外轨道。

### 3.2 分裂情形没有有理点

由 (2.3)，$T$ 的射影像为阶 $p-1$ 的循环群，每个非单位元素都有两个 $\mathbb F_p$ 特征线。若存在有理轨道，(3.2) 给出 $T\cap N(C)$ 中射影阶大于 $2$ 的元素 $h$。它不可能属于 $N(C)\setminus C$，于是属于 $C$。

但 $h$ 非标量且有两个 $\mathbb F_p$ 特征线，不能属于非分裂 Cartan。这是矛盾。

结合十三项 CM 分类，已证明结论第 1 项。也已说明后文每个真正的有理 CM 点，其 $p$-Cartan 代数确实由完整 CM 环给出；该前提不是从 $j$ 是 CM 直接跳过而来的。

## 4. 约化相交时的交换子障碍

以下论证对更一般的两个 CM 阶也成立。设 $p\ne\ell$，曲线 $E_1,E_2/\overline{\mathbb Q}_\ell$ 的完整 CM 环为 $\mathcal O_i$，判别式为 $\Delta_i<0$，且 $p\nmid\Delta_1\Delta_2$、$\left(\frac{\Delta_i}{p}\right)=-1$，即 $\mathcal O_i/p\mathcal O_i\simeq\mathbb F_{p^2}$。考虑由这些子代数给出的 Cartan 结构。

若这两个 CM 点在模 $\ell$ 相交，在一个共同有限扩张取得两曲线的好约化，并使用保持 Cartan 结构的几何约化同构，把约化都认作 $E_0$。记
$$
R=\operatorname{End}_{\overline{\mathbb F}_\ell}(E_0),
\qquad R_{\mathbb Q}=R\otimes\mathbb Q.
$$

**引理 4.1。** 若两个 CM 域在 $R_{\mathbb Q}$ 中的像不同，则存在整数 $t$，使
$$
\frac{\Delta_1\Delta_2-t^2}{4p^2}\in\mathbb Z_{>0}.
\tag{4.1}
$$

**证明。** 取 $a_i\in\{0,1\}$，$a_i\equiv\Delta_i\pmod2$，并取 CM 环生成元
$$
u_i=\frac{a_i+\sqrt{\Delta_i}}2.
$$
仍记它们在 $R$ 中的像为 $u_i$。约化同构保持 Cartan 结构，所以 $u_1,u_2$ 在 $E_0[p]$ 上都属于同一个交换二次代数。因此交换子
$$
w=[u_1,u_2]
$$
杀掉 $E_0[p]$。由商同源分解，$w=p\beta$，其中 $\beta\in R$。

若 $w=0$，$u_2$ 位于 $u_1$ 的中心化子中；虚二次或四元数代数中非实二次元素的中心化子就是它生成的二次域。这会使两个 CM 域的像相同。因此 $w\ne0$，且 $R_{\mathbb Q}$ 是正定四元数代数。

令 $x_i=2u_i-a_i$，则 $x_i$ 约化迹为零，$x_i^2=\Delta_i$。定义
$$
t=\frac12\operatorname{trd}(x_1x_2)
 =2\operatorname{trd}(u_1u_2)-a_1a_2\in\mathbb Z.
$$
自同态的迹是整数，故 $t$ 确为整数。又因 $x_i$ 为纯四元数，
$$
x_1x_2+x_2x_1=2t,\qquad
\operatorname{nrd}(x_1x_2)=\Delta_1\Delta_2,
\qquad w=\frac{x_1x_2-t}{2}.
$$
所以
$$
\operatorname{nrd}(w)=\frac{\Delta_1\Delta_2-t^2}{4}
 =p^2\operatorname{nrd}(\beta)=p^2\deg\beta.
$$
$\beta\ne0$，因而 $\deg\beta\in\mathbb Z_{>0}$，得到 (4.1)。证毕。

## 5. 素于 $\ell$ 的饱和性及同一 CM 域的退化情形

不能由“交换子为零”直接推出原先两 CM 点相同：不同导子的二次整环可能嵌入同一个约化 CM 域。下面保留并控制这一情形。

**引理 5.1。** 设 CM 椭圆曲线 $E/\overline{\mathbb Q}_\ell$ 有好约化 $E_0$，$\mathcal O=\operatorname{End}(E)$，$R=\operatorname{End}(E_0)$。在约化嵌入下，有限群
$$
(R\cap\mathcal O_{\mathbb Q})/\mathcal O
$$
的阶为 $\ell$ 的幂。

**证明。** 两个环是同一个二次域中的格，故商有限。只须证明它没有素于 $\ell$ 的挠元。

设 $n$ 与 $\ell$ 互素，$\alpha\in R\cap\mathcal O_{\mathbb Q}$ 且 $n\alpha$ 是某个 $\varphi\in\mathcal O$ 的约化。扩大好约化定义域，使所有相关映射定义良好。约化 $\bar\varphi=n\alpha$ 杀掉 $E_0[n]$。由于素于 $\ell$ 的挠群约化同构，$\varphi$ 也杀掉 $E[n]$。

所以 $\varphi=[n]\circ\psi$，$\psi\in\mathcal O$。约化后 $n\alpha=n\bar\psi$，自同态群无挠，故 $\alpha=\bar\psi\in\mathcal O$。这消灭了所有素于 $\ell$ 的挠元。证毕。

**推论 5.2。** 在 §4 的相交设定下，如果不存在满足 (4.1) 的整数 $t$，则
$$
\Delta_1/\Delta_2=\ell^{2r}
\quad\text{对某个 }r\in\mathbb Z.
\tag{5.1}
$$

**证明。** 由引理 4.1，两个 CM 域的像必为同一个 $K\subset R_{\mathbb Q}$。令 $\mathcal O_0=R\cap K$。对两条好约化曲线分别应用引理 5.1，得到
$$
[\mathcal O_0:\mathcal O_i]=\ell^{b_i}
\qquad(b_i\ge0).
$$
二次整环判别式在指数为 $d$ 的子环下乘以 $d^2$，于是
$$
\Delta_i=\ell^{2b_i}\operatorname{disc}(\mathcal O_0).
$$
相除即得 (5.1)。证毕。

## 6. 有理 CM 点的分离

现在恢复 $p>163$、$\ell\ge5$、$\ell\ne p$。由 §3，每个有理 CM 点均为某个 $\Delta\in\mathcal D$ 的标准 CM Cartan 点，且每个允许的判别式只有一个点。因此两个不同点对应不同判别式 $\Delta_1,\Delta_2$。

若它们约化相同，因其 CM $j$ 为整数，约化不是尖点。非尖点模解释给出 §4 使用的、保持 Cartan 代数的约化同构。两曲线都有潜在好约化，可在共同有限扩张实施 §4、§5 的证明。

不同判别式的乘积满足
$$
0<\Delta_1\Delta_2\le163\cdot67=10921<4p^2.
$$
因此 (4.1) 不可能，推论 5.2 强制 $\Delta_1/\Delta_2=\ell^{2r}$。交换下标后可设 $r>0$；$r=0$ 会使判别式相同。由列表范围，
$$
\ell^{2r}\le163/3<55.
$$
对 $\ell\ge5$，只剩 $\ell^{2r}=25$ 或 $49$。十三项列表中没有比为 $25$ 或 $49$ 的一对数，矛盾。结论第 2 项得证。

## 7. 结论的用途和边界

可以统一取辅助素数 $\ell=5$。对所有 $p>163$，已知有理 CM 点占据不同的第一层剩余圆盘。这为逐圆盘 QC 认证提供了确定的点分离。

它不能替代 QC 函数的简单零点判据。交换子只比较两 CM 环在同一约化曲线上的作用，不控制高度函数的导数或两个 QC 函数系数的行列式，也不排除不含 CM 点的剩余圆盘中出现非 CM 有理点。

$\ell\ge5$ 的限制也不能随意删去。同一虚二次域中不同导子的 CM 环可满足 (5.1)，例如判别式对 $(-3,-12)$、$(-3,-27)$、$(-4,-16)$、$(-7,-28)$ 在 $\ell=2$ 或 $3$。本证明保留了这些可能性。

### 与 2026 年交数论文的关系

Love–Studnia–Vonk, *Arithmetic intersections on non-split Cartan modular curves*, [arXiv:2604.06963](https://arxiv.org/abs/2604.06963)，2026 年预印本，Theorem B、Lemma 3.16、§4 给出更精确的算术交数信息。本结果的必要条件受其问题设置启发，但上述证明只使用 §1 列出的经典输入和显式计算，没有调用该预印本的结论。
