# 两个固定代数提升的 universal-extension 对数与高度的准确差别

后续 [R39](../results/R39-cm-height-linear-period-matrix.md) 已用新增 CM 行把实际三个 cyclotomic 高度和反对称高度同时化成线性 period，并证明其全部代数线性独立；剩余二次 regulator 尚未非零。

**可信度：§1–§6 的代数群、线性独立和提升改变公式已证明；§7–§8 在所列已证高度构造输入下逐式推导。** 日期：2026-11-12。固定
$$
E:y^2=x^3-17x,\qquad
P=(-1,4),\quad Q=(9,24),\qquad
\omega=\frac{dx}{2y}.
$$
R4 已证明 $P,Q$ 独立。本笔记核查一条具体方案：将 $P,Q$ 提升到 $E$ 的 universal vectorial extension，能否用两个对数的行列式取代 rank-two 高度或导出类的非零条件。

本笔记最初得到 §5 的二选一弱结论；后续
[R37](../results/R37-cm-period-reciprocity-nonvanishing.md)
已用广义 Jacobian 和 §7 的互易式证明：两个指定的代数提升在每个目标 $p$
都有非零对数行列式。它仍不是所需的 cyclotomic 高度行列式。
§7 保留两者之间不可省略的积分项。

## 1. 固定代数提升可以明确选取

令
$$
0\longrightarrow\mathbb G_a
\xrightarrow{\iota}G=E^\natural
\xrightarrow{\operatorname{pr}}E
\longrightarrow0
\tag{1}
$$
为 universal vectorial extension。其扩张类非零，并生成一维空间
$\operatorname{Ext}^1(E,\mathbb G_a)$。

在特征零中，$G$ 的代数点可由第三类微分表示：微分的留数除子给出其在 $E$ 上的像，两个代表相差 $d\log f$ 时等价；改变同一留数除子的代表相当于加全纯微分。这是 Coleman 的 *Vectorial extensions of Jacobians*，§1 的描述。

对于 $R=(x_R,y_R)\ne O$，且 $y_R\ne0$，可以取
$$
\eta_R=\frac{y+y_R}{x-x_R}\,\omega.
\tag{2}
$$
它在 $R$ 的留数为 $1$、在 $O$ 的留数为 $-1$，在 $-R$ 没有极点。所以 (2) 表示 $(R)-(O)$ 上的一个代数提升。特别地，
$$
\eta_P=\frac{y+4}{x+1}\,\omega,\qquad
\eta_Q=\frac{y+24}{x-9}\,\omega
\tag{3}
$$
定义两个固定的 $\mathbb Q$-有理提升 $g_P,g_Q$。

取系数使 $\iota(c)$ 对应加 $c\omega$。于是
$$
\eta_R\longmapsto\eta_R+c\omega,\quad c\in\mathbb Q,
\tag{4}
$$
是另一个固定代数提升，不改变其在 $E$ 上的像。

来源：[Coleman 1990 原文](https://www.numdam.org/article/AIF_1990__40_4_769_0.pdf)，§1，印刷第770页。式 (2) 的留数直接用局部参数计算，不需要引用新的高度结论。

## 2. 真子群及 CM 独立性

### 2.1 G 的连通真子群

$G$ 的正维连通真子群只能是式 (1) 的 $\mathbb G_a$。

证明：设一维连通子群 $H$ 的像在 $E$ 中非零，则该像为 $E$。$H$ 的线性部分映到 $E$ 为零，所以只能包含在有限核中；于是 $H$ 是椭圆曲线，$H\to E$ 是同源。这将使 (1) 沿该同源的 pullback 分裂。但特征零中同源在
$\operatorname{Ext}^1(-,\mathbb G_a)\simeq H^1(-,\mathcal O)$ 上诱导同构，所以不能杀掉非零扩张类，矛盾。

另一个所需性质为
$$
\operatorname{Hom}(G^n,\mathbb G_a)=0.
\tag{5}
$$
由 universal extension 的定义，应用 $\operatorname{Hom}(-,\mathbb G_a)$ 时的连接映射
$$
\operatorname{Hom}(\mathbb G_a^n,\mathbb G_a)
\longrightarrow\operatorname{Ext}^1(E^n,\mathbb G_a)
$$
是同构，因此得到 (5)。

由此还可见：若 $H\subset G^n$ 是连通代数子群且投射满 $E^n$，则 $H=G^n$。否则 $G^n/H$ 是由向量核满射得到的非零向量群，组合一个非零线性泛函将产生与 (5) 矛盾的同态。

### 2.2 P 与 Q 在 CM 上也独立

若
$$
(a+bi)P+(c+di)Q=0,\qquad a,b,c,d\in\mathbb Q,
$$
复共轭固定 $P,Q$ 并将 $i$ 变为 $-i$。将原式与共轭式相加、相减，得到
$$
aP+cQ=0,\qquad bP+dQ=0.
$$
R4 的有理独立性使四个系数都为零。因此 $P,Q$ 在
$\operatorname{End}^0_{\overline{\mathbb Q}}(E)=\mathbb Q(i)$ 上独立。

于是 $(P,Q)$ 在 $E^2$ 中的代数群包为整个 $E^2$：若有真连通子群包含某个非零整数倍，就会给出一个非零 CM 线性关系。结合 §2.1，$(g_P,g_Q)$ 在 $G^2$ 中的代数群包为 $G^2$。这些结论对任意代数提升都成立。

## 3. AST 的确给出四个坐标的代数线性独立

在目标 split 素位将系数嵌入 $\mathbb Q_p$。可取固定代数 Lie 坐标，使
$$
\log_G(g_P)=(a_{P,p},\ell_{P,p}),\qquad
\log_G(g_Q)=(a_{Q,p},\ell_{Q,p}),
\tag{6}
$$
第二坐标是椭圆对数
$$
\ell_{P,p}=\log_E(P),\qquad
\ell_{Q,p}=\log_E(Q).
$$
这两个数均非零，因为 $P,Q$ 非挠。

这些点属于可定义标准群对数的 $G(\mathbb Q_p)_f$。这里可直接验证整个 $G(\mathbb Q_p)$ 都在该集合内：取一个紧开子群 $U$，其在紧群 $E(\mathbb Q_p)$ 中的像是开子群，指数有限。任意 $g$ 的某个非零整数倍因而可写成 $u+v$，其中 $u\in U$、$v\in\mathbb G_a(\mathbb Q_p)$。加法群中的每个点位于一个紧加法子群中，所以 $u+v$ 位于一个紧子群中。再加上有限个 $g$ 的陪集，便得到包含 $g$ 的紧子群；其点的某个严格递增整数倍序列趋于零。

所用已证输入是 Fuchs–Pham 的 $p$-adic analytic subgroup theorem。Theorem 2.2 的假设是任意正维**交换代数群**，没有 semi-abelian 限制，因此确实涵盖非分裂向量扩张 $G^2$：
若代数点的非零对数位于一个**在 $\overline{\mathbb Q}$ 上定义的**真 Lie 子空间，则存在相应的正维代数子群包含该点。见 arXiv:1502.00768，Theorem 2.2。

假设 (6) 的四个坐标存在非零 $\overline{\mathbb Q}$-线性关系。它给出
$\operatorname{Lie}(G^2)$ 中一个代数超平面，包含 $\log(g_P,g_Q)$。上述定理便给出一个真代数子群包含 $(g_P,g_Q)$，与 §2.2 的代数群包矛盾。因此
$$
\boxed{\quad
a_{P,p},\ell_{P,p},a_{Q,p},\ell_{Q,p}
\text{ 在 }\overline{\mathbb Q}\text{ 上线性独立}.
\quad}
\tag{7}
$$

还可以加入常数 $1$。事实上 $(1,g_P,g_Q)$ 在
$\mathbb G_a\times G^2$ 中的代数群包也是整个群。为处理可能不连通的代数群包，先取其恒等分支 $H$；某个非零整数倍 $(N,Ng_P,Ng_Q)$ 在 $H$ 中，且 $H$ 投射满 $G^2$。若投射的核为零，则 $H\to G^2$ 为同源。其存在一个复合后等于乘整数的反向同源，故 (5) 也推出 $\operatorname{Hom}(H,\mathbb G_a)=0$。第一坐标同态因而为零，与 $N\ne0$ 矛盾。若核是整个第一因子 $\mathbb G_a$，则 $H$ 已是全群。再用同一 AST 得到
$$
1,a_{P,p},\ell_{P,p},a_{Q,p},\ell_{Q,p}
\quad\text{在 }\overline{\mathbb Q}\text{ 上线性独立}.
\tag{8}
$$
特别地，每个非零坐标都是超越数。

这是一个真实的线性独立结论，而不只是说 AST “似乎不适用”。

来源：[Fuchs–Pham 原文](https://arxiv.org/pdf/1502.00768)，Theorem 2.2；本文只用该定理，不使用一个系数在 $\mathbb Q_p$ 中的未知超平面。

## 4. 单独在 G² 中使用 AST 的不足及 R37 的实际加强

定义
$$
D_p^\natural=
a_{P,p}\ell_{Q,p}-a_{Q,p}\ell_{P,p}.
\tag{9}
$$
Poonen 对群对数和闭包的定义直接给
$$
\dim_{\mathbb Q_p}\overline{\langle g_P,g_Q\rangle}
=
\operatorname{rank}_{\mathbb Q_p}
\begin{pmatrix}
a_{P,p}&a_{Q,p}\\
\ell_{P,p}&\ell_{Q,p}
\end{pmatrix}.
\tag{10}
$$
因此闭包维数为 $2$ 等价于 $D_p^\natural\ne0$。

若只从 §3 的线性独立出发，假设 $D_p^\natural=0$ 将给出两列共线，以及
$$
\frac{a_{P,p}}{\ell_{P,p}}
=\frac{a_{Q,p}}{\ell_{Q,p}}.
\tag{11}
$$
由 (7)–(8)，这个公共斜率不是代数数；两列之间的比例
$\ell_{Q,p}/\ell_{P,p}$ 也不是代数数。故 (11) 所给的 $\mathbb Q_p$ 直线并非一个代数定义的 Lie 子空间。不能把它作为 §3 中 AST 的输入。

这说明单独的线性独立命题与矩阵秩命题不同。四个抽象数甚至连同 $1$
可以代数线性独立，同时满足一个二次行列式等式。例如以三个代数独立的符号 $u,v,w$ 代入
$$
\begin{pmatrix}
u&v\\ w&vw/u
\end{pmatrix}
$$
时，行列式为零而 $1,u,v,w,vw/u$ 线性独立。
这个例子只展示“直接升级”的逻辑缺口，**不再是本曲线实际行列式的障碍**。

R37 引入 $J_{O+P+Q}$，将 §7 的准确互易式
$D_p^\natural=\mathcal B_{PQ,p}-\mathcal B_{QP,p}$
识别为两个固定广义 Jacobian 提升的非零代数 Lie 线性形式。
两点的 CM 独立性以及该广义 Jacobian 没有 affine 商，
使提升点的群包满；AST 随即证明 $D_p^\natural\ne0$。
该证明还处理了不在紧子群中的小素数点和对数分支，
所以覆盖每个目标 $p$，并适用于任意代数提升。

最新的相关 primary 也明确保留这项区别。Burungale–Skinner–Wan，
arXiv:2603.20886v2，§5、Conjecture 5.2 将多点 logarithm matrix 的实际秩等于 structural rank 列为猜想；其已证单点非零结论与 §3 的 AST 相容。这篇论文针对 abelian varieties，而非声称证明本 universal extension 的 rank-two 特例。

来源：

- [Poonen 原文](https://math.mit.edu/~poonen/papers/leopoldt.pdf)，§1.2–§1.3。
- [Burungale–Skinner–Wan 原文](https://arxiv.org/pdf/2603.20886)，§5，Definition 5.1、Conjecture 5.2、Corollary 5.4；v2 日期为 2026-05-10。
- [Waldschmidt 原文](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/p-adicClosure.pdf)，Theorem 2 是较弱的闭包秩下界；§7.2 说明一般代数群还需处理真子群。不能将其 simple-abelian-variety 公式直接应用于 $G$。§7.3 还给出朴素最大维数猜测的反例，所以本文不把 Poonen 的一般问题当作已证定理。

## 5. 初始的二选一弱论证（现已由 R37 加强）

以下是发现广义 Jacobian 互易法以前的一个简单弱论证。
它仍然成立，但现在指定的 (3) 已由 R37 证明在每个目标 $p$ 都非零。

保持 $g_P$，取两种固定提升
$$
g_Q^{(0)}=g_Q,\qquad
g_Q^{(1)}=g_Q+\iota(1).
$$
对应微分为 $\eta_Q$ 和 $\eta_Q+\omega$。对所有目标 $p$，
$$
D_p^{(1)}=D_p^{(0)}-\ell_{P,p}.
\tag{12}
$$
因为 $\ell_{P,p}\ne0$，二者不可能同时为零。目标 split 素数集是无限集，所以至少一个固定选择
$c\in\{0,1\}$ 满足
$$
\boxed{\quad
D_p^{(c)}\ne0
\quad\text{对无穷多个目标 }p.
\quad}
\tag{13}
$$
这无需任何 period conjecture。它并不指定是哪一个 $c$ 有无限成功集合。

但 (13) 也说明为什么“任意代数提升的 log determinant 非零”不能直接替代原目标：改变提升的加法坐标，就能人为改变这个行列式，而 canonical 高度不应依赖这样的选择。下一节把这一点写成准确公式。

## 6. 本 CM 曲线的 unit-root 补空间可取为固定代数直线

$[i](x,y)=(-x,iy)$ 给
$$
[i]^*\omega=i\omega,\qquad
[i]^*(x\omega)=-i(x\omega).
\tag{14}
$$
在 $H^1_{\mathrm{dR}}(E)$ 中，$\omega,x\omega$ 构成代数基。在 split 素位，Frobenius 提升 $[\pi]$ 在这两条 CM 特征线上分别作用为 $\pi,\bar\pi$；前者赋值为 $1$、后者为 $0$。所以 canonical ordinary 补空间为
$$
W_p=\mathbb Q_p[x\omega].
\tag{15}
$$
将 $x\omega$ 乘一个固定非零有理数，得到 $\beta$，使
$H^1_{\mathrm{dR}}(E)/\mathbb Q\omega$ 的坐标与固定 $\omega$ 给出的椭圆对数坐标一致。于是仍有 $W_p=\mathbb Q_p\beta$，并可将 (6) 理解为
$$
\Psi_p(\eta_i)=a_{i,p}\omega+\ell_{i,p}\beta,
\qquad i=P,Q.
\tag{16}
$$
这里 $\Psi_p$ 正是 universal extension 的对数（使用主极化作标准识别）。

因此，不能把当前障碍只归咎于“unit-root 直线随 $p$ 变化”：对这条 CM 曲线，该直线可以固定。仍随 $p$ 改变且必须保留的是 (16) 的对数坐标 $a_{i,p}$。

## 7. 高度的正规化减去的是一个对数坐标，还需要第三类积分

外部已证输入为 Coleman–Gross 构造：

1. $\Psi_p$ 在全纯微分上是标准上同调类，并杀掉 $d\log f$。
2. 对留数除子 $A_i$，唯一正规化第三类微分 $\omega_{A_i,W_p}$ 满足
   $\Psi_p(\omega_{A_i,W_p})\in W_p$。
3. 在 $p$ 处的局部高度是该正规化微分沿另一个除子的 Coleman 积分；全局高度还须加入远离 $p$ 的局部项。

这些输入见 Besser arXiv:1711.06957，§2，式 (2.2)–(2.3)、Theorem 3.7；其与 Nekovář 高度的比较为 Theorem 1.1。对 elliptic curve 的 Mazur–Tate 高度比较也见 Balakrishnan–Besser arXiv:1201.6016。

令 $A_P=(P)-(O),A_Q=(Q)-(O)$，用 (3) 作第三类微分。为了所有矩阵元均有不交支集，可以为两个列分别选固定有理除子 $B_j$，使 $B_j\sim A_j$，并避开两个 $A_i$ 的支集；例如平移代表即可，而有限个禁止点可避开。记
$$
I_{ij,p}=\int_{B_j}\eta_i,\qquad
C_{ij,p}=\sum_{v\ne p}h_v(A_i,B_j),
\qquad
\mathcal B_{ij,p}=I_{ij,p}+C_{ij,p}.
$$
取局部分量为标准 $\log_p$ 的 cyclotomic 全局 log。由 (15)–(16)，
$$
\omega_{A_i,W_p}=\eta_i-a_{i,p}\omega.
$$
故全局高度矩阵恰为
$$
\boxed{\quad
H_p=\mathcal B_p-\mathbf a_p\boldsymbol\ell_p^t,
\quad
\mathbf a_p=\binom{a_{P,p}}{a_{Q,p}},
\quad
\boldsymbol\ell_p=\binom{\ell_{P,p}}{\ell_{Q,p}}.
\quad}
\tag{17}
$$

改变提升 $\eta_i\mapsto\eta_i+c_i\omega$ 时，
$$
\mathbf a_p\mapsto\mathbf a_p+\mathbf c,\qquad
\mathcal B_p\mapsto\mathcal B_p+\mathbf c\boldsymbol\ell_p^t.
$$
因此 $H_p$ 完全不变，而
$$
D_p^\natural\mapsto
D_p^\natural+c_P\ell_{Q,p}-c_Q\ell_{P,p}.
\tag{18}
$$
所以 §5 的无限非零结果不会给高度的无限非零。

对于 elliptic curve，一维补空间自动 isotropic，故 $H_p$ 对称。将 (17) 的非对角项相减，还得到准确比较
$$
\boxed{\quad
D_p^\natural=\mathcal B_{12,p}-\mathcal B_{21,p}.
\quad}
\tag{19}
$$
即原始提升的对数行列式只给未经正规化的积分矩阵的反对称部分；它不是对称高度矩阵的行列式。

若直接使用高度正规化后的提升，其对数为
$$
\Psi_p(\eta_i-a_{i,p}\omega)=\ell_{i,p}\beta.
$$
两者都在同一条 $W_p$ 直线上，所以其对数行列式恒为零。此外，由 (8)，$a_{i,p}$ 超越，故这些正规化微分并不是本来固定的代数提升，不能对其系数再次使用代数 AST。

高度行列式由 (17) 给出的准确公式为
$$
\det H_p=
\det\mathcal B_p-
\boldsymbol\ell_p^t\operatorname{adj}(\mathcal B_p)\mathbf a_p.
\tag{20}
$$
它包含第三类积分以及对数的乘积。本文未把它识别为一个固定 $1$-motive 的单个线性 period；单纯把 (20) 中的乘积重新命名，并不能提供这种识别。

来源：

- [Besser 原文](https://arxiv.org/pdf/1711.06957)，§2、Theorem 3.7。
- [Balakrishnan–Besser 原文](https://arxiv.org/pdf/1201.6016)，§2 Assumption 2.2 及随后的对称性说明；Theorem 4.1 给局部高度的二重积分表达，Corollary 4.2 给 ordinary unit-root 情形与 $\sigma_p$ 的比较，Corollary 4.3 给 Mazur–Tate 比较。
- Coleman 第三类微分描述见 §1 的来源。式 (17)–(20) 为本笔记直接代入并计算。

## 8. 严格 Mordell–Weil 核向量仍带 p-adic 系数

令
$$
\mathbf v_p=\binom{\ell_{Q,p}}{-\ell_{P,p}},
\qquad
\xi_p=\ell_{Q,p}P-\ell_{P,p}Q.
$$
这是 $E(\mathbb Q)\otimes\mathbb Q_p$ 中的严格局部核向量，不是已经证明存在的一个代数点。由
$\boldsymbol\ell_p^t\mathbf v_p=0$，(17) 给
$$
\boxed{\quad
h_p(\xi_p,\xi_p)
=\mathbf v_p^tH_p\mathbf v_p
=\mathbf v_p^t\mathcal B_p\mathbf v_p.
\quad}
\tag{21}
$$
这里正规化的 rank-one 修正准确消失，但第三类积分仍在。式 (21) 也是
$\boldsymbol\ell_p^t\operatorname{adj}(H_p)\boldsymbol\ell_p$。

由 (7)，$\ell_{Q,p}/\ell_{P,p}$ 超越，所以不能将 $\xi_p$ 当作代数点来使用单点非零定理；也不能把消去的修正项理解为高度已经线性化。

至此，本路线给出了：

- 固定 algebraic lifts 的五个数 (8) 的完整代数线性独立；
- 后续 R37 已将本笔记的二选一弱结论加强为：任意代数 lifts 在每个目标 $p$
  都有非零 logarithm determinant；
- 该 determinant 与实际高度的准确关系 (17)–(21)。

仍缺的是实际高度或导出对象的非零，而不是任意 lift 的一阶对数非零。本笔记没有从这些结论推出 $G_p(p)\ne0$ 或 Sha 的有限性。
