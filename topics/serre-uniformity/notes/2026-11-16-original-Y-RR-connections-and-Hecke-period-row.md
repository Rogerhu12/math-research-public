# 原 Y 的 Picard 一次列：254度移动、有限主部与同源 Hecke period 行

日期：2026-11-16。状态：**本文给出原层41的一项有限准确构造和来源契约；没有执行新算术。** 新内容是把已经完成的原五个嵌入 Picard 理想及 c0 帧，接成可实际生成的代数连接、未拆闭点的主部线性图和同一原 Hecke 校准行。本文证明的128、634、508、507是空间维数与映射秩；没有声称已经求出任何新截面系数、连接系数、Hecke 对数矩阵或 Poincaré period 数值。

原 [R724](../results/R724-original-Chow-Heegner-height-matrices-and-canonical-jet-evaluation.md) 已给规范求值与原活跃 Hecke 部分；
[既有高度审计](2026-11-15-original-height-Poincare-linearization-and-period-determinant-audit.md) 的 UE.28i、UE.28p–r 已证明同一第二类修正的全部 jet 相消。
这些结论不重登。这里补它们尚未提供的**原代数微分和实际纤维来源**，并将结果逐项放回原组合
$$
\frac1{q_j}\tau_{Y,p}(v_j)-2\ell_{h_j}(\log P_Y).
\tag{YP.1}
$$
原 $\beta$、$\eta_{h_j}$、theta 二挠比较、$\chi$、非 $p$ 项及原 $c_0,c_1$ 均不改变。

## 1. 使用已经完成的原理想和两个指定帧

沿 [R849](../results/R849-certified-original-global-function-and-five-polar-ideal-DAGs.md)、
[R848](../results/R848-certified-original-c0-Hodge-jets-and-comparison-leading-coefficients.md)
及 [RF 的实际纤维构造](2026-11-16-original-c0-rigidified-Poincare-fibres-and-theta-section-DAG.md)，写
$$
Y/\mathbf Q,\quad g(Y)=127,\quad
P_0=\phi(c_0),\quad P_1=\phi(c_1),\quad t=a^3,
$$
$$
\mathscr L_j=\mathcal O_Y(-Z_j),\quad
\xi_j=[Z_j],\quad \eta_{h_j}=\xi_j/q_j,\quad
\operatorname{mult}_{P_0}Z_j=-7\delta_j.
\tag{YP.2}
$$
这里 $P_0,P_1$、$t$ 及原有理下降均为原来源的对象；
$t$ 不是 R805 铅笔的底变量。$P_1$ 不在 $Z_j$ 的支撑中。
原两个局部帧和纤维点是
$$
e_{0,j}=t^{-7\delta_j},\qquad e_{1,j}=1,\qquad
v_j=1(P_1)\otimes e_{0,j}(P_0)^{-1}
 \in\mathcal P_Y(P_Y,\lambda_Y\xi_j)^\times,
\quad P_Y=[P_1-P_0].
\tag{YP.3}
$$
仍用原符号 $i_Y^*\lambda_Y(\xi_j)=-\xi_j$。

(YP.2) 的线丛、帧和 norm 都是完整原对象的下降；
不能把原 M2 截面或 R820 的辅助 $\mathbf Q$-form 直接改称原扭曲曲线的有理截面。
算法可先在原 $K=\mathbf Q(\zeta)$ 的两图进行，再用 R802 的真实半线性作用作下降。
后文所有维数先对原 $\mathbf Q$ 对象成立，经 $K/\mathbf Q$ 基变换不变。

## 2. 一个128维 RR空间把任意大的原除子压到254度

置 $m=2g=254$，先固定一个 $j$，省去下标。
$$
V(\mathscr L)=H^0\!\left(Y,\mathscr L(mP_0)\right).
\tag{YP.4}
$$
因为 $\deg\mathscr L(mP_0)=254>2g-2=252$，
Riemann–Roch 给 $\dim V=128$。
基变换到代数闭包后，对任一几何点 $P$，$\deg\mathscr L(mP_0-P)=253>252$，
故该线丛无基点；这个推导也见 Stacks Project
[53.5，Riemann–Roch](https://stacks.math.columbia.edu/tag/0B5B)
及 [53.22.3](https://stacks.math.columbia.edu/tag/0E39)。

因此可以准确选
$$
a\in V,\qquad
c=\left(t^{m+7\delta}a\right)(P_0)\ne0,\qquad a(P_1)\ne0 .
\tag{YP.5}
$$
这里第一个值是线丛纤维坐标。它不是把一个有极点的函数直接代入 $P_0$。
选择不要求两个点的联合评价满秩：先取 $u$ 在 $P_0$ 非零；
若 $u(P_1)=0$，再取 $v$ 在 $P_1$ 非零，
则 $u+v,u+2v$ 中至少一个同时非零。
不得据度254自动宣称联合二点评价秩2。

定义
$$
T=\operatorname{div}(a)-Z+mP_0 .
\tag{YP.6}
$$
这是有效 Cartier 除子，$\deg T=254$，且 $P_0,P_1\notin T$。
不要求 $T$ 约化，也不分裂其闭点。令
$$
D_0=T-mP_0,\qquad \mathscr M=\mathcal O_Y(D_0).
$$
正乘 $a$ 是实际同构
$$
m_a:\mathscr M\longrightarrow\mathscr L.
\tag{YP.7}
$$
在 $P_0$，$\mathscr M$ 的帧为 $t^m$，而
$a\,t^m=c\,t^{-7\delta}(1+O(t))$；在 $P_1$ 的帧1中标量为 $a(P_1)$。
因此原刚性化纤维准确满足
$$
\boxed{\quad v_j=\frac{c_j}{a_j(P_1)}\,v_{D_{0,j}}.\quad}
\tag{YP.8}
$$
这里 $v_{D_0}=1(P_1)\otimes(t^m)(P_0)^{-1}$。
原标量 $c/a(P_1)$ 保存在来源中，不能因两个线丛的 Picard 类相同而删除。

这一步同样适用于任意已知整数张量幂 $\mathscr L_j^{\,N}$：
其次数仍为零，(YP.4) 的维数仍是128；
只把 (YP.5) 中 $7\delta$ 换成 $7N\delta$。
没有在 Jacobian 中求一个未知的 $N$-除点。

## 3. 从原两图理想生成有限 RR 线性图

这一节说明“求(YP.4)”所需的实际有限输入，不将128误称为整个输入矩阵的大小。

保持 R805 的两个正规环
$$
\mathcal R_\tau=\bigoplus_{a=0}^{271}K[z_\pi]\beta_a,\qquad
\mathcal R_\sigma=\bigoplus_{a=0}^{271}K[t_\pi]\gamma_a,
\quad t_\pi=z_\pi^{-1},
$$
$$
z_\pi=\sigma/\tau,\qquad
\gamma_a=t_\pi^{\epsilon_a}\beta_a,\qquad
\epsilon=(0,1^{144},2^{127}).
\tag{YP.9}
$$
R849 的理想式在这两个**完整正规环**中解释。
对乘积、逆、和与整理想商使用真嵌入分式理想；
可复用 R811 的完整多项式核/列格与两图运输，不把一个仅有包含关系的格当作理想。

例如 (YP.4) 的两图模为
$$
M_\tau=\mathscr L_\tau I_{P_0,\tau}^{-m},\qquad
M_\sigma=\mathscr L_\sigma I_{P_0,\sigma}^{-m}.
\tag{YP.10}
$$
原 $P_0$ 的点理想由实际评价的核给出；
若 $P_0$ 不在某图，该图的理想就是单位理想。
这一步不改用一个方便但不同的点。

每个非零分式理想作为 $K[z_\pi]$ 或 $K[t_\pi]$ 模有限自由秩272。
材料化并完整认证其基矩阵 $H_\tau,H_\sigma$ 后，令
$$
A_M(t_\pi)
 =H_\sigma(t_\pi)^{-1}
   \operatorname{diag}(t_\pi^{-\epsilon_a})
   H_\tau(t_\pi^{-1}).
\tag{YP.11}
$$
同一理想在重叠处相等恰给
$A_M\in\operatorname{GL}_{272}(K[t_\pi,t_\pi^{-1}])$；
两向 Laurent 恒等式须实际核验。

设 $r_M$ 是 $A_M^{-1}$ 全部非零项的最低 Laurent 次数，
$B_M=\max(0,-r_M)$。
任一全局截面的第一图坐标 $u(z_\pi)$ 满足
$$
\deg u_a\le B_M,\qquad
\bigl[A_M(t_\pi)u(t_\pi^{-1})\bigr]_{\text{负次}}=0.
\tag{YP.12}
$$
反之这些有限系数方程的每个解都是全局截面。
证明：第二图坐标 $v=A_Mu(1/t_\pi)$ 必须为多项式；
反向 $u(1/t_\pi)=A_M^{-1}v$ 的最低次数不小于 $r_M$，
所以任何非零 $u$ 的次数受所述界限制。
由此(YP.12)是完整的有限线性图，核恰为(YP.4)。

$B_M$ 来自实际基矩阵；它可能大，不能预称此次转换总成本为128阶。
全部中间理想运算及基变换也可能昂贵，应按需求、来源与断点保存，
不先求没有消费者的完整 Krylov 逆或 $272^3$ 乘法表。

若先在 $K$ 上求解，对所得有限全局空间施加原 R802 半线性下降。
真实 Galois 作用保持(YP.2)、$mP_0$及主部目标；
解空间按这个作用下降，不以系数共轭代替原扭曲曲线的 Galois 作用。
一组 $K$ 基的原共轭及其函数等式可给准确有限下降矩阵。

### 3.1 微分模只需原 g 与已成 cusp 理想

R813/R814 的原导子记为
$$
\delta_\tau=\tau^{-1}D_0,\qquad
g_\tau=\delta_\tau z_\pi,\qquad
\nu=\frac{dz_\pi}{g_\tau}.
\tag{YP.13}
$$
$\nu$ 是同一个原函数域中的有理微分。
R814 的
$\operatorname{div}\delta_\tau=\mathcal D_{\rm cusp}-H_\tau$
及 R820 的完整尖点理想 $\mathcal C_\tau,\mathcal C_\sigma$ 给
$$
\boxed{\quad
\Omega^1(\mathcal R_\tau/K)=\mathcal C_\tau\nu,\qquad
\Omega^1(\mathcal R_\sigma/K)
 =t_\pi^{-1}\mathcal C_\sigma\nu .
\quad}
\tag{YP.14}
$$
第二式用 $\delta_\sigma=t_\pi\delta_\tau$，
所以其对偶微分为 $\nu/t_\pi$。
这里两个图均包含全部尖点，且原 $\tau,\sigma$ 在那里非零。

对有效除子 $D$，$\Omega^1_Y(D)$ 的两图系数格因此只是
$$
\mathcal C_\tau I_{D,\tau}^{-1},
\qquad t_\pi^{-1}\mathcal C_\sigma I_{D,\sigma}^{-1}.
\tag{YP.15}
$$
可直接用(YP.11)–(YP.12)求其完整全局空间。
原 $g_\tau$ 已有准确 normal 向量；原函数域的导数也有 GP 的准确隐式表达。
本步骤不要求先完成一般 $\Gamma$ 或 $M_g$ 的全部矩阵 CRT。
若把 $\nu$ 写成 $dz_\pi/g_\tau$ 后在某点出现 $0/0$，
须在(YP.14)的正则微分模内求纤维，不能用未正则化的标量比代入。

## 4. 未拆闭点的508维主部方程

令
$$
D=T+mP_0,\qquad \deg D=508.
$$
则
$$
\dim H^0(Y,\Omega^1_Y(D))=634,\qquad
\dim H^0(Y,\Omega^1_Y(D)/\Omega^1_Y)=508.
\tag{YP.16}
$$
第一式由 $\deg\Omega(D)=760>252$ 得到。
定义完整主部图
$$
\mathrm{pp}:H^0(Y,\Omega(D))
 \longrightarrow H^0(Y,\Omega(D)/\Omega).
\tag{YP.17}
$$
其核为 $H^0(Y,\Omega)$，维127，所以秩507。
这是实际有限系数图；不能只把每个闭点的 residue 一个数作为全部主部条件。

指定目标 $\mathfrak p_T$ 如下：

* 在 $T$ 上，取有效 Cartier 除子的规范对数主部 $df_T/f_T$；
* 在 $mP_0$ 上，取 $-m\,dt/t$，其余高极阶主部均为零。

局部生成元更换 $f_T\mapsto uf_T$ 只增加正则 $du/u$，
故这个主部与生成元选择无关。
若 $T$ 在某几何点的重数为 $r$，其 residue 是 $r$；
这里没有把 $T$ 换成约化支撑。

全局 residue functional 在508维目标上非零。
$\mathfrak p_T$ 的 residue 总和为 $\deg T-m=0$。
所有全球有理微分的 residue 总和为零；
结合(YP.17)的秩507，其像恰为该 residue functional 的核。
因此完整仿射方程
$$
\boxed{\quad\mathrm{pp}(\alpha_0)=\mathfrak p_T\quad}
\tag{YP.18}
$$
有解，解空间维127。

这里 global residue theorem 也可直接沿原有限图 $\pi$ 证明：
对有理微分取函数域迹到 $\mathbf P^1$，局部微分迹保持 residue 的剩余域迹和，
而 $\mathbf P^1$ 上部分分式的 residue 总和为零。
没有要求实际算法拆闭点。

### 4.1 完整 jets/CRT 的具体有限模

在一个含相应支撑的仿射图 $U$ 上令
$R=\mathcal O(U)$、$I=I_{T\cap U}$。
有限代数 $A=R/I$ 可以非约化。
其 conormal 模 $I/I^2$ 是秩一可逆 $A$ 模，
因 $A$ 是 Artin 半局部环而为自由模。
选一个准确生成元 $\bar f\in I/I^2$，取 $f\in I$ 为其提升。

这一选择是有限线性代数：给定生成列 $f_1,\ldots,f_s$，
测试 $\sum_{\ell=1}^{s}n^{\ell-1}\bar f_\ell$ 是否生成 $I/I^2$，
即测试乘法 $A\to I/I^2$ 的完整 $k$-线性满秩。
每个几何支撑点至多排除 $s-1$ 个整数参数；
因支撑点数不超过 $\deg T$，
前 $\deg T(s-1)+1$ 个整数中必有可用者。
此计数只证明有限停止，不要求执行中拆分任何闭点。

在支撑附近 $f$ 是 $I$ 的生成元。
乘 $f$ 给准确有限模同构
$$
I^{-1}\Omega_R/\Omega_R
 \xrightarrow{\ \cdot f\ }\Omega_R/I\Omega_R .
\tag{YP.19}
$$
在右侧，对数主部恰由 $df\bmod I\Omega_R$ 表示。
所以目标和全局主部图均可由多项式格商、微分及完整有限矩阵写出；
不需要在函数域任取一个局部根，也不需要将 $f$ 的额外全局零点加入 $D$。
若 $f$ 改变一个 $I^2$ 元素，$df\bmod I\Omega_R$ 不变。

$mP_0$ 的部分使用原 $t$，
$$
\mathcal O_{mP_0}\simeq k[t]/(t^m),\qquad
t^m\!\left(-m\,\frac{dt}{t}\right)
 =-m\,t^{m-1}dt\bmod t^m\Omega .
\tag{YP.20}
$$
这保存全部 $m$ 个主部坐标，并非只核 residue $-m$。

为避免在两图重叠重复记支撑，可将有限 $T$ 分为第一图部分与
$H_\tau$ 上部分。用第二图有限代数中乘 $t_\pi$ 的稳定核/像作 Fitting 分解，
或用同一个有限模的 CRT 幂等元即可；这只分为两个开集部分，不分裂剩余域。
因 $P_0\notin T$，再与 $mP_0$ 的互素理想作 CRT。
各部分维数相加恰508，所有运输按(YP.14)保留。

## 5. 原帧上的代数连接和原切向评价

方程(YP.18)的任一解给 $\mathscr M=\mathcal O(T-mP_0)$ 上的正则代数连接：
在其有理截面1中令 $\nabla 1=\alpha_0\,1$。
正乘(YP.7)运输到 $\mathscr L$，在原有理截面1中恰为
$$
\boxed{\quad \alpha_{\rm alg}=\alpha_0-d\log a .\quad}
\tag{YP.21}
$$
其全部 residue 是 $-Z$。
在 $P_0$，写
$a=t^{-(m+7\delta)}u_a$、$u_a(P_0)=c$；
则
$$
\alpha_{\rm alg}
 =7\delta\,dt/t+\text{正则微分},
\qquad
\alpha_{\rm alg}-7\delta\,dt/t
$$
是原局部帧 $e_0=t^{-7\delta}$ 中的正则连接形式。
在 $P_1$，$a(P_1)\ne0$ 且 $T,P_0$ 均不经过该点，
所以 $\alpha_{\rm alg}$ 本身正则。

若原 $X$ 参数为 $s_X=a-1$，本次真正的一次代数量是
$$
A_{{\rm alg},j}
 =\left.\frac{\phi^*\alpha_{{\rm alg},j}}{ds_X}\right|_{c_1}.
\tag{YP.22}
$$
必须沿原 $\phi$ 和原切向求值，不把 $d/dz_\pi$ 或 $d/dt_\pi$ 当作它。
可使用正则微分模的纤维与原 R790/R796 的点/一阶来源；
如果后继表达式表面上有共同零，应先在模内消去再评价。

Abel 拉回在 Picard 零次线丛及其正则连接上给
$\operatorname{Pic}^{\nabla}(J_Y)\simeq\operatorname{Pic}^{\nabla}(Y)$。
在固定线丛纤维上，两边都是全局正则1形式的仿射空间，
且 $H^0(J_Y,\Omega^1)\to H^0(Y,\Omega^1)$ 是同构。
故(YP.21)和原刚性化唯一指定原 universal extension 的一个**代数**提升，
等价于固定扩张上的代数 Lie 投影 $t_{\rm alg}$。
它通常不是原 canonical 提升。这个差保留到第7节的同一校准行中。

在 $P_0$，有理截面1并非该线丛的非零局部帧。
不得把 $\int_{P_0}^{P_1}\alpha_{\rm alg}$ 的常数任设为0：
真实常数是(YP.8)及原半阿贝尔群的单位刚性化。
(YP.22)只求正阶，不靠这种未指定积分常数。

## 6. 原活跃投影的真整数化与连接幂等投影

这里的 $e=e_\eta$ **只能取 R724 §3 中由原全部 $\eta_{h_j}$ 确定的活跃中心投影**。
它属于原完整 adelic Hecke 代数，在 Rosati 下自伴；
R724 §2 的参考 splitting 按该实际等型分解相容。
不许为了本式另选一个有利投影。

取正整数 $d$ 清除这个实际 $e$ 的同态分母，使
$$
f=de\in\operatorname{End}_{\mathbf Q}(J_Y).
$$
因 $\operatorname{End}(J_Y)$ 无整数挠，有真同态恒等式
$$
f^2=df,\qquad f^\dagger=f .
\tag{YP.23}
$$
R724 只先给 $(f-d)\xi_j=0$ 于有理点的 $\mathbf Q$-张量中；
其实际差可能是非零挠点。
因此必须先选并记录一个真整数 $N>0$，杀掉五个实际差：
$$
N(f-d)\xi_j=0\quad\text{于 }J_Y(\mathbf Q).
\tag{YP.24}
$$
例如可使用 R724.10 的两好素数约化给出的准确挠阶上界，再以真群等式核验。
这里没有填一个尚未计算的 $N$，也没有以低精度零对数作挠判。

置 $Q_j=\lambda_Y(N\xi_j)$，$\mathscr L_{j,N}=\mathscr L_j^{\,N}$，
原纤维为 $v_j^{\otimes N}$，其第一 Picard 槽仍是 $P_Y$。
自伴性与(YP.24)准确给
$$
f^\vee Q_j=dQ_j.
\tag{YP.25}
$$
在原刚性化 Poincaré 线丛 $L_{Q_j}$ 上，(YP.25)给唯一保持零轴的实际同构
$$
\iota_j:f^*L_{Q_j}\xrightarrow{\sim}L_{Q_j}^{\otimes d}.
\tag{YP.26}
$$
需要的 tensor 同构和原 torsion 比较由这个真等式生成；
不把二挠帧或一般 torsion 帧设置为1。

先按第2–5节为 $\mathscr L_{j,N}$ 构造任意正则代数连接 $\nabla$。
在同一个固定线丛上定义
$$
\mathcal A_j(\nabla)
 =\frac1d\,\iota_{j,*}f^*\nabla .
\tag{YP.27}
$$
这里 $1/d$ 是从 $L_{Q_j}^{\otimes d}$ 的连接回到既定 $L_{Q_j}$ 的
唯一仿射除法：tensor 连接在局部形式上乘 $d$。
它不在 Jacobian 中选择 $d$-除点，不在代数纤维里选择 $d$ 次根。

(YP.27)的线性部分为 $f^*/d=e^*$。
(YP.23)与所有零轴刚性化同构的唯一性，
连同 Picard 零次连接的乘法相容性，给
$$
\mathcal A_j^2=\mathcal A_j .
\tag{YP.28}
$$
具体地，两次拉回的底同态是 $f^2=[d]\circ f$；
沿 $[d]$ 的真实 Picard tensor 同构把连接乘 $d$，
而两个 $1/d$ 恰归为一次 $1/d$。
因此 $\nabla_j^e=\mathcal A_j(\nabla)$ 是可准确构造的 $e$-相容连接。

这些操作可沿原 Hecke 对应在曲线上实施：
有限对应的两支使用连接的拉回与 norm，后者在局部形式上是有理微分的迹，
并保留行列式 norm 纤维及刚性化。
分歧处采用正则微分的 dualizing trace，不能只对一个有极点的系数取未校正迹。
正则性可在特征零完成 DVR 上核：写基参数为局部参数的 $r$ 次幂，
迹筛出的正则微分项仍是非负幂；同一式给
$\operatorname{Tr}(d\log u)=d\log\operatorname{Nm}u$。
这是有限代数操作，不要求算法拆闭点。
实际对应、$f,d,N,\iota_j$ 都是新消费者须记录的源，不宣称已完成。

原块相容 canonical connection 同样满足(YP.27)，因为其 Hodge splitting 与原 $e$ 交换。
因此，若
$$
\delta_j=t_{{\rm alg},j}^e-t_{{\rm can},j}
 \in\operatorname{Lie}(J_Y)^*,
$$
则
$$
\boxed{\quad \delta_j=\delta_j e.\quad}
\tag{YP.29}
$$
这是下面删除 inactive 分量的依据；对一个未经(YP.27)处理的任意连接，
不能直接写(YP.29)。

## 7. 同一 Hecke log 矩阵与实际 fibre period 行

保留 R724.9–12 的真实 $B_\eta=eJ_Y$、$b=\dim B_\eta$，
以及从原 $\eta_{h_j}$ 的有限实际 Hecke 轨道选出的有理点基
$P_1^{\rm H},\ldots,P_b^{\rm H}$。
用上标 H 与原曲线点 $P_1$ 区分。
$$
L=\bigl(\log P_1^{\rm H}\ \cdots\ \log P_b^{\rm H}\bigr)
 \in\operatorname{GL}_b(\mathbf Q_p).
\tag{YP.30}
$$
其非奇异性来自原 R724 的已证对数同构；
不假定一个任意点集的 log 矩阵满秩，不反演高度矩阵。

对每个 $j,r$，在真实有理纤维
$\mathcal P_Y(P_r^{\rm H},Q_j)$ 中选并记录一个有理非零向量 $w_{jr}$。
这可直接从原 divisor/ideal DAG 构造，不需要先展开全部标准 Jacobian 坐标。
若 $P_r^{\rm H}$ 由 $D_r=E_r-F_r$ 表示，使用
$$
\operatorname{Nm}_{E_r/\mathbf Q}
   (\mathscr L_{j,N}|_{E_r})
 \otimes
\operatorname{Nm}_{F_r/\mathbf Q}
   (\mathscr L_{j,N}|_{F_r})^{-1}.
\tag{YP.31}
$$
有效部分可非约化，支撑允许与 $Z_j$ 相交。
这里取的是线丛限制，不是把有极点的原有理截面1强行代值。
对有限代数 $A$ 上的秩一模 $M$，
$\operatorname{Nm}(M)=\det_{\mathbf Q}M\otimes(\det_{\mathbf Q}A)^{-1}$；
实际有理基即可给非零纤维向量，所有换基行列式保留。
主除子更换沿原 norm/Weil reciprocity 同构运输。
所以本构造不要求分裂闭点或把共同支撑移开。

原 $\chi_p=c_\chi\log_p$，$c_\chi\ne0$。
使用同一 $t_{{\rm alg},j}^e$ 和实际半阿贝尔群，定义
$$
\gamma_{{\rm alg},j}(w)
 =t_{{\rm alg},j}^e\log_{E_{Q_j}}w,
$$
$$
\boxed{\quad
U_{jr}=\gamma_{{\rm alg},j}(w_{jr})
       +c_\chi^{-1}\sum_{\ell\ne p}\tau_{Y,\ell}(w_{jr}).
\quad}
\tag{YP.32}
$$
群对数、torus 分支和非 $p$ 项都用 R724 的原规范。
尤其 (YP.32)不是只取一个扩域地方的局部对数。
如在有限扩域计算，先保持真实 $\mathbf Q$ 纤维，再按完整原 trace/norm 求值。

更换 $w_{jr}$ 为 $a\,w_{jr}$、$a\in\mathbf Q^\times$，
第一项增加 $\log_p a$，其余地方之和按同一全局角色恰减少该值。
所以 $U_{jr}$ 与这个有理纤维选择无关。
实际有限支撑可由对应、理想、帧、纤维点及群结构的整模型清分母取得；
非 $p$ 项不能因完整原 $\mathscr N_h(c_1)$ 的坏处值为零而逐项删除。

Poincaré 的全局因子2和(YP.29)给
$$
U_{jr}=\frac{2}{c_\chi}h_Y(P_r^{\rm H},N\xi_j)
          +\delta_j(\log P_r^{\rm H}).
\tag{YP.33}
$$
令 $U_j=(U_{j1},\ldots,U_{jb})$。
把 R724 的真正 $\ell_{h_j}$ 写在同一原基下，遂得到
$$
\boxed{
\frac1{q_j}\tau_{Y,p}(v_j(P))
 -2\ell_{h_j}(\log [P-P_0])
 =
 \frac{c_\chi}{Nq_j}
 \left\{
 \gamma_{{\rm alg},j}\bigl(v_j(P)^{\otimes N}\bigr)
 -U_jL^{-1}e\log[P-P_0]
 \right\}.
}
\tag{YP.34}
$$
这是在原 $P_1$ 盘上的来源级实现，不另声称一个新的抽象相消定理。
它与已登记 UE.28p 是同一式：本次给出其中的代数连接及 period 行具体来源。

若 $\alpha_j^e$ 是第6节投影后连接在原有理截面1中的形式，
对原 $s_X=a-1$ 求一次，准确有
$$
\boxed{
\frac1{q_j}
 \left.\frac d{ds_X}\tau_{Y,p}(v_j)\right|_{c_1}
 -2\ell_{h_j}(u_Y)
 =
 \frac{c_\chi}{Nq_j}
 \left\{
 \left.\frac{\phi^*\alpha_j^e}{ds_X}\right|_{c_1}
 -U_jL^{-1}eu_Y
 \right\},
}
\quad
u_Y=\left.\frac d{ds_X}\log P_Y\right|_{c_1}.
\tag{YP.35}
$$
同一个 $N$ 已进入 $\alpha_j^e$ 和第二变量 $Q_j$，不能再在左侧重复乘 $N$。

改变初始代数连接，使投影后增加一个 $e$-支持的正则1形式 $\theta$，
则(YP.35)的代数项增加 $\theta(eu_Y)$，
而 $U_j$ 增加 $\theta L$；两项准确相消。
这也核准了连接选择不会改变原高度。
若更换 Hecke 点基，$L$ 与 $U_j$ 同时右乘同一个可逆有理矩阵，结果亦不变。
$b=0$ 时空行项按0解释；(YP.24)仍保实际 torsion 平凡化和原帧，
不能仅以 $\eta=0$ 于有理张量中就删整个线丛。

这给每个原方向至多 $b\le127$ 个实际校准纤维；
五行的直接实现上界是 $5b$，没有要求计算或反演一个 $b\times b$ 高度矩阵。
已登记 UE.28d/R785 的同源块合并仍可进一步复用相同 period；
这里不把 $5b$ 宣称为不可再少的下界。

## 8. 回到原常数列、对称导数和指定一次列

原高度审计 UE.2 已证明的是完整修正线丛在 $c_1$ 的全部非 $p$ 值为零，
所以
$$
d_{h_j}=\Lambda_{h_j}(c_1)
       =\widehat h_{\mathcal L_{h_j}}(\beta).
\tag{YP.36}
$$
这条旧结论不重证。
RF/SP 的新增实际椭圆来源使常数列可用六个完整的全球 line-height 校准。
对 $h=f,g_1,\ldots,g_5$，取 RF 原七因子的三次 $\mathbf Q$ 下降，
并定义
$$
\mathcal H_h
 =\frac13\sum_v
   \log_{\Theta_h^{\,3},v}\bigl(u_h(\gamma)^{\otimes3}\bigr),
\qquad \gamma=[c_1-c_0].
\tag{YP.37}
$$
全部 origin 帧、三次 tensor 同构及原非 $p$ 项按 RF 保留。
RF 的 NS/完整 theta 比较给
$$
d_{h_j}=\mathcal H_{g_j}
             -\frac{p_j}{q_j}\mathcal H_f.
\tag{YP.38}
$$
这里只需六个完整全球标量，不需额外为五个 $d_{h_j}$ 各找一个高度 oracle。
但 $\mathcal H_h$ 的 $p$ 项由 SP 的原 sigma 公式计算后，
仍须加它自己的非 $p$ 项；不能由(YP.36)删掉六个因子的这些项。
三次帧下降和原 theta-square/二挠比较也没有因取全球和而被改写成任意椭圆 theta。

记 SP 的六个对称一次项为 $\mathcal B_h$，原比较函数为 $\mathcal R_j$。
结合 RF.31、SP.33 和(YP.35)，原实际一次列的第 $j$ 项为
$$
\boxed{
\Lambda_{h_j}'(c_1)
 =\mathcal B_{g_j}-\frac{p_j}{q_j}\mathcal B_f
 -\frac1{3q_j}
   \left.\frac d{ds_X}\chi_p(\mathcal R_j)\right|_{c_1}
 +\frac{c_\chi}{Nq_j}
  \left\{
   \left.\frac{\phi^*\alpha_j^e}{ds_X}\right|_{c_1}
   -U_jL^{-1}eu_Y
  \right\}.
}
\tag{YP.39}
$$
$\nu_j,\kappa_j$ 的零阶标量仍在 RF.31；
它们的导数为零，故未出现在(YP.39)。
不能把 $\mathcal R_j/(\kappa_jt^{14\delta_j})$ 代回此式。
R847 在辅助 $\ell=1000000753$ 的真单位证书也不等于这些原 $p=41$ 的 period 数值；
每个真实 $p$ 嵌入、精度和 trace 仍须来源认证。

(YP.35)提供原 Y 一次列的具体代数源与有限 period 行。
(YP.38)提供六个实际全球 line-height 的常数列来源。
两者没有证明原指定 $\mathscr T_p$ 非零，也没有将 Picard 修正或第二类周期设为零。

## 9. 最小可执行阶段及尚未输出的准确对象

后继可按下列顺序保存独立、来源绑定的原子阶段；这不是新增授权或独立测试门：

| 阶段 | 真输入和完整输出 | 纸面保证 |
|---|---|---|
| 原理想材料化 | R849五理想 DAG、原272整基/函数域、R848帧；完整两图格及过渡 | 仍是原 $\mathscr L_j$，不改类/尺度 |
| 254度移动 | (YP.12)全系数核、实际 $a_j,T_j,c_j,a_j(P_1)$、真两图同构 | RR维128，$P_0,P_1$均避开 $T_j$ |
| 主部连接 | R820原 $\mathcal C$、R813原 $g$；634维空间、508维目标及全映射、完整解 | 秩507，127维解的仿射空间 |
| 原 Hecke 投影 | 原 $e,d,f$、实际 torsion 差与 $N$、唯一刚性化同构 | $f^2=df$、$f^\vee Q=dQ$、(YP.28) |
| 校准纤维 | 原 Hecke 点基、未拆有限代数的 norm 纤维、完整非 $p$ 来源 | 与实际 $L$ 同一行，保持原角色 |
| period 求值 | 实际原 $p$ 嵌入、进入形式群整数、尾界与 trace 损失 | (YP.32)、(YP.35)、(YP.39)准确求值 |

前五行是有限代数来源的构造；其实际矩阵大小取决于已经材料化的格及 Hecke 对应，
不由128或634两个输出维数自动界定。
当前没有运行这些新阶段，也没有填未知 $a_j$、$T_j$、$N$、$L$ 或 $U_j$。
既成原曲线、函数、极理想、cusp理想、CM点和帧继续按其真实 producer 直接消费，
不重做已有算术。

本入口的新增实质是：(YP.10)–(YP.22)把原 GP 理想和指定帧接成一条真正可生成的代数微分；
(YP.23)–(YP.35)把它接入原同一个 Hecke 校准行，严格保留 inactive/torsion 边界。
原规范 splitting 的数值差无需单独计算，实际 period 与非 $p$ 校准仍按(YP.32)保留。
