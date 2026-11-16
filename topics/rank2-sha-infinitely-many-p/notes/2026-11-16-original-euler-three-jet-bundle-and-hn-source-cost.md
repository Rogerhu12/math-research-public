# 原三 Euler 值束的完整来源成本与六倍次数方案的边界

日期：2026-11-16。**状态：下述完整二阶 jet 分离、原三值像束的行列式下界及其对所述 HN 方案的排除已证明。它不排除原首核，也不判定指定 forcing。**

本注核查一种可能的捷径：将三阶正常厚化的关联分次
$N^3,N^2,N$ 当作承载全部原来源的 rank $3$ 束，进而期待最大斜率不超过 $2\kappa$。完整原来源的 Euler 三值并不免费落入这个次数为 $6\kappa$ 的格。下面在原十九角曲面、全部原 $\mathcal H_3$ 上计算必要的来源成本。

## 1. 原几何、线性化和所计算的束

保留 R495/R815/R833 的实际数据
$$
C=(F),\quad
N=\mathcal O_C(C),\quad
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\quad
\kappa=C^2,\quad\chi=-K_XC,\quad b=C.f.
\tag{1}
$$
$C$ 是原光滑有理曲面 $X$ 上的几何整 Cartier 曲线，且不等于任何原边界。它可以有奇点。本注采用
$$
\boxed{\kappa\ge3,\qquad \chi>1,\qquad p>101.}
\tag{2}
$$
当前原 $r=2$、$b\ge5$ 强窗满足这些小界；本注不据此认定其它 profile 或候选存在。

原 $\mathbf G_m$ 作用是 $Y$ 的缩放，$\mathcal E$ 是它在各 $\mathcal O_X(jC)$ 上已经支付的线性化一阶算子。它保持整个原 $\mathcal H_j$，不是在固定角处忽略框项的裸导数。

令 $\nu:\widetilde C\to C$ 为正规化，置 $\widetilde N=\nu^*N$。考虑**同一个全局来源**的三个实际值
$$
j_{\mathcal E}^2:
\mathcal H_3\otimes_k\mathcal O_{\widetilde C}
\longrightarrow
\widetilde N^3\oplus\widetilde N^3\oplus\widetilde N^3,
\quad
G\longmapsto(G,\mathcal EG,\mathcal E^2G)|_{\widetilde C}.
\tag{3}
$$
定义
$$
\boxed{\mathscr E_{\rm act}=\operatorname{im}j_{\mathcal E}^2.}
\tag{4}
$$
下面证明它泛点 rank 为 $3$。在光滑曲线 $\widetilde C$ 上，(4) 是满 rank 子模，故是向量束。若先在奇曲线 $C$ 上取像，不能先称其局部自由；(4) 直接在正规化上定义，避免这项错误。

(4) **没有**在环境束内先作饱和。其饱和是整个环境束；二者的有限长度商正是必须记账的行列式缺陷。因为 $\deg\widetilde N=\kappa$，
$$
\deg\mathscr E_{\rm act}=9\kappa-\operatorname{length}\mathscr T,
\quad
\mathscr T=(\widetilde N^3)^{\oplus3}/\mathscr E_{\rm act}.
\tag{5}
$$

## 2. 全部原 $\mathcal H_3$ 确实分离二阶完整 jet

**引理 1。** 对任一几何点 $Q\in C$，原限制
$$
\boxed{
\mathcal H_3\longrightarrow
\mathcal O_X(3C)\otimes(\mathcal O_{X,Q}/\mathfrak m_Q^3)
}
\tag{6}
$$
满射。右边长度是 $6$，并非只沿一条光滑分支读三项。

**证明。** R495 已付 $H^1(X,\mathcal O_X(jC))=0$，$j\ge0$。对包含于原 $C$ 的长度 $n$ 的有限概形 $D$，其理想在 $C$ 上为 $\mathscr I_D$。由于 $C$ 为 Gorenstein 整曲线，
$$
H^1(C,N^j\mathscr I_D)^\vee
=\operatorname{Hom}_C(\mathscr I_D,\omega_C N^{-j}).
$$
右端对应 rank $1$ 无挠层的次数为
$$
(1-j)\kappa-\chi+n.
\tag{7}
$$
这在奇点也成立：将
$0\to\mathscr I_D\to\mathcal O_C\to\mathcal O_D\to0$
对偶，额外的 $\operatorname{Ext}^1(\mathcal O_D,\omega_C N^{-j})$
长度正是 $n$。次数为负的 rank $1$ 无挠层没有非零全局截面。因此下列三个范围都无 $H^1$：
$$
(j,n)=(3,\ n\le6),\quad
(2,\ n\le3),\quad
(1,\ n\le1).
\tag{8}
$$
所需严格不等式分别是
$2\kappa+\chi>6$、$\kappa+\chi>3$、$\chi>1$，由 (2) 保证。

现在对曲面上的 $D_3=V(\mathfrak m_Q^3)$ 使用实际剩余序列
$$
0\to
\mathscr I_{\operatorname{Res}_C D_3}(2C)
\xrightarrow{\ F\ }
\mathscr I_{D_3}(3C)
\to
\mathscr I_{D_3\cap C,C}N^3
\to0.
\tag{9}
$$
若 $m=\operatorname{ord}_QF$，则在曲面正则局部环内
$$
(\mathfrak m_Q^a:F)
=\mathfrak m_Q^{\max(a-m,0)}
\qquad (a=1,2,3).
\tag{10}
$$
这是由该局部环的关联分次环为多项式整环、乘积阶相加得到的，不要求 $C$ 光滑。

所以 (9) 的剩余概形至多是 $\mathfrak m_Q^2$ 所定义的长度 $3$ 概形；下一步至多是一个点。各次在 $C$ 上的交长度依次至多 $6,3,1$。逐次用 (8)、(9) 和最后的原 $H^1(\mathcal O_X(jC))=0$，得到
$H^1(X,\mathscr I_{D_3}(3C))=0$，即 (6)。证毕。

这一步用的是整个已付 $\mathcal H_3$。它不把某个较小 profile 或任意三个局部向量认成来源。

## 3. 原线束 charge 项不能从局部矩阵遗漏

在任一实际原框内，将一个截面写为函数 $g$，则线性化为
$$
\mathcal E g=Dg+a g,
$$
其中 $D$ 是原 $\mathbf G_m$ 向量场，$a$ 是该框的真实线束项。于是完整三值是
$$
\begin{pmatrix}
g\\ Dg+a g\\ D^2g+2aDg+(Da+a^2)g
\end{pmatrix}.
\tag{11}
$$
用行变换
$$
V_1\mapsto V_1-aV_0,\qquad
V_2\mapsto V_2-2aV_1+(a^2-Da)V_0
\tag{12}
$$
准确化为 $(g,Dg,D^2g)$。其行列式为 $1$；没有要求 $a$ 为单位，也没有删去 $Da$。因此 (12) 保全部原 charge 和十九角框，却不改变行列式缺陷。

在非固定轨道点，$D$ 至少有一个单位方向。用引理 1 取与 $1,x,x^2$ 同二阶 jet 的三个原全局截面，其中 $Dx(Q)$ 为单位。相应三值行列式在 $Q$ 等于
$$
2(Dx(Q))^3,
$$
是单位。因此
$$
\boxed{\mathscr T\text{ 只支撑在原 }\mathbf G_m\text{ 固定集与 }C\text{ 的交上。}}
\tag{13}
$$
特别 (3) 泛点 rank 为 $3$。一般 $t|_C$ 的分歧点并不属于此例外集：只要曲面上的 $\mathbf G_m$ 轨道非固定，原全来源仍分离这三个值。

## 4. 固定图中的真实行列式成本

原十九次吹起均在原不变边界的节点进行。每个固定图有实际单项坐标，使
$$
D=\alpha x\partial_x+\beta y\partial_y.
\tag{14}
$$
初始权是 $0,\pm1$；各链至多四次吹起，后续权由两权相减得到。因此所有需要的非零权、权差以及倍数 $2$ 在 (2) 中均为单位。这里只除这些固定曲面权，不除某个随 $C$ 增长的 charge。

在孤立固定点，$\alpha\beta\ne0$。取正规化上过该点的一支，记
$$
u=\operatorname{ord}x,\qquad v=\operatorname{ord}y.
$$
它们为正整数。对局部单项来源 $1,x,x^2$，三值行列式是
$2\alpha^3x^3$；相应的 $1,y,y^2$ 给 $2\beta^3y^3$。引理 1 允许用原全局截面代替这些单项，误差在 $\mathfrak m_Q^3$ 中。选择阶较小的坐标时，误差项的行列式阶严格较高。因此该支的实际缺陷满足
$$
\operatorname{length}\mathscr T_{\widetilde Q}
\le3\min(u,v).
\tag{15}
$$
若同时用 $1,x,y$，还得到 $\alpha\beta(\beta-\alpha)xy$；在权差为单位的原孤立固定图上可加强为
$$
\operatorname{length}\mathscr T_{\widetilde Q}
\le\min(u+v,3u,3v).
\tag{16}
$$
本注的全局界只需 (15)，不依赖更强的 (16)。

在固定水平曲线上，可取 $\alpha=0,\beta\ne0$，该固定曲线为 $y=0$。这里不能只用 $\mathfrak m_Q^3$ 的总阶估计误差，因为沿某支可能 $\operatorname{ord}y\gg\operatorname{ord}x$。应取与 $1,y,y^2$ 同二阶 jet 的三个原全局截面；首截面是单位，先除以它。其余两个函数写成
$$
r_i=\sum_{n\ge0}a_{i,n}(x)y^n.
$$
$D=\beta y\partial_y$ 杀全部 $n=0$ 项，且
$$
a_{1,1}(Q)=a_{2,2}(Q)=1,\qquad
a_{1,2}(Q)=a_{2,1}(Q)=0.
$$
行列式是 $Dr_1D^2r_2-D^2r_1Dr_2$；它被 $y^3$ 整除，$y^3$ 的系数在 $Q$ 为 $2\beta^3$。因此它准确是 $y^3$ 乘单位，给
$$
\operatorname{length}\mathscr T_{\widetilde Q}
\le3\operatorname{ord}_{\widetilde Q}y.
\tag{17}
$$
若它同时通过另一个边界分量，也保该分量，不把它约化掉。

这里利用了 DVR 上满 rank 像的余长度等于全部最大子式赋值的最小值；展示一个达到上述阶的真实子式已经足够，并未假设只有这三列。

上述估计直接在每个正规化分支的 DVR 上计算。它们不需要 $t|_C$ 的 tame 分歧假设，也不将奇点的多支当成一个光滑参数；最后对全部分支及剩余域次数求和。

## 5. 全十九角的总次数

令 $\mathscr B$ 是原完整约化不变边界：
两个严格水平截面、六个严格底纤维及十九个例外曲线。它有 $27$ 个分量；R815 的 $26$ 条负极射线之外，另保正水平分量。

原 $\mathbf F_4$ 上有
$$
K_{\mathbf F_4}=-2S_0-6f,\qquad
\mathscr B_0=2S_0+10f,
$$
所以 $K_{\mathbf F_4}+\mathscr B_0=4f$。每次在边界节点的吹起都是这一完整 log 对的 crepant 吹起：
$$
K_X+\mathscr B=\pi^*(K_{\mathbf F_4}+\mathscr B_0)=4f.
$$
因此
$$
\boxed{C.\mathscr B=\chi+4b.}
\tag{18}
$$
$C$ 不等于边界分量，故所有这些实际交数非负，并包含奇点的全部分支重数。

在孤立固定图，$\mathscr B$ 至少含 $xy=0$，所以 (15) 至多为该支与 $\mathscr B$ 交数的三倍。在固定水平图，(17) 也至多为其完整边界交数的三倍。结合 (13)，得到
$$
\boxed{
\operatorname{length}\mathscr T
\le3C.\mathscr B=3\chi+12b.
}
\tag{19}
$$
代入 (5)：
$$
\boxed{
\deg\mathscr E_{\rm act}\ge9\kappa-3\chi-12b,
\qquad
\mu(\mathscr E_{\rm act})
\ge3\kappa-\chi-4b.
}
\tag{20}
$$
这不是把像先饱和后得到的 $9\kappa$；全部原固定边界修改已在 (19) 扣除。

## 6. 为什么 $6\kappa$ 的正常分次不能承载全原三值

在原 $C$ 上，以 $e=\mathcal EF$、$f_2=\mathcal E^2F$ 写出的一个常见 $F$-normal 候选格由
$$
N^3\oplus N^2\oplus N
\longrightarrow (N^3)^{\oplus3},
\qquad
(v,a_1,a_2)\longmapsto
(v,e a_1,f_2a_1+2e^2a_2)
\tag{21}
$$
给出。其行列式为 $2e^3$，次数是 $6\kappa$。这只是一个确定的正常系数格，并不等于全原来源的三值像。

具体而言，R836 已证明全部原来源的第一法向值在 $Z=(e|_C)$ 上覆盖
$$
\ker[H^0(Z,N^3|_Z)\to H^0(Z_-,N^3|_{Z_-})],
$$
维数为 $\kappa-z_-$。若 $\kappa>z_-$，其中存在不被 $e$ 整除的真实值；(21) 的第二坐标却总被 $e$ 整除。

更直观地，在一个非固定简单分歧点，若 $f_2$ 为单位，则 R550 的原限制满射允许取实际 $H\in\mathcal H_2$ 在该点为单位。真实列 $eH$ 满足
$$
\frac{\mathcal E(eH)|_C}{e}
=\frac{f_2H|_C}{e}+(\mathcal EH)|_C,
$$
有真实极点。这一局部例不被当成所有原曲线必有简单分歧的假设；前一段的完整有限像已经给出一般范围。

更一般地，假设某 rank $3$ 向量束 $\mathscr V$ 真正接收全部原 $G$，并在泛点与同一三 Euler 值通过一个固定可逆变换识别。全部来源诱导一个泛点可逆的束映射
$$
\mathscr E_{\rm act}\longrightarrow\mathscr V.
$$
因为 $\mathscr E_{\rm act}$ 由这些全局来源生成，该映射在每一点都必须保持相同的 $\mathcal O_{\widetilde C}$ 线性关系；它是正则映射，不是只在去掉分歧点后的一张形式表。故其行列式给
$$
\deg\mathscr V\ge\deg\mathscr E_{\rm act}.
\tag{22}
$$
于是当
$$
\boxed{\kappa>\chi+4b}
\tag{23}
$$
时，(20)、(22) 迫
$$
\deg\mathscr V>6\kappa,\qquad
\mu_{\max}(\mathscr V)\ge\mu(\mathscr V)>2\kappa.
\tag{24}
$$
因此，保全部原来源及同一泛点三值的 rank $3$ 束，在 (23) 范围内不能具有“总次数 $6\kappa$、最大 HN 斜率不超过 $2\kappa$”这组性质。不能从厚化的形式关联分次直接引入该半稳定性结论。

(23) 是明确条件，不预认所有原 profile 都满足它。它适用于二次 $\kappa$ 主导线性 $b,\chi$ 的区域；小自交数的原面仍须按自己的准确数据读取。本注也不排除付清新来源限制后采用别的束、非线性结构或真实受限像方法。

## 7. 与实际首核的边界

(6) 是源端完整二阶 jet 分离，(20) 是承载这些实际 Euler 值的束次数下界。它们没有证明任意 $G$ 的高前缀可自由分配，没有证明 $W_T$ 满射，也没有让两块分别单射的原单位像相加。

原三长长度仍是 $T=s-r-13$，同一个 $G$ 的第四短行、三个十三行 carry、$q_{\rm src}$ 全 Euler 导数和下一位修正都保留。特别，本注只排除了上述未付修改成本的 HN 捷径，不把 (24) 当成原三长核非零或主目标的反证。

后续仍回到 R836/R840 的实际受限值、同一个镜轴解和指定 forcing。没有新增数学执行或数值扫描。

依赖：[R495](../results/R495-fixed-angular-surface-and-full-triple-source-joint-image.md)、[R815](../results/R815-complete-original-mori-nef-cones-and-s-fibration.md)、[R833](../results/R833-original-euler-image-and-negative-horizontal-cokernel.md)、[R836](../results/R836-original-restricted-euler-values-and-three-long-kernel-presentation.md)。
