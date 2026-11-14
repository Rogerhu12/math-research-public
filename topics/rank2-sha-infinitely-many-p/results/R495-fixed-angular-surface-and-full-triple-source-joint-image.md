# R495 — 原固定角曲面、完整三倍来源与更强联合 jet 界

日期：2026-11-14。**状态：已证明。** 直接对实际因子 $F$ 的固定角点作十九次几何吹起，可以在同一原预算中使用整个 $H^0(X,\mathcal O_X(3C))$，其中 $C$ 是 $F=0$ 的严格变换。其规范交数满足 $K_XC\le-2b$，从而全部正倍数的所需一阶上同调消失。这给同一个修正的联合值/法向 jet 一个由准确 $C^2,K_XC$ 控制的新界。

对几何自交具有满主阶的高 $b$ 候选，定理覆盖一段真正维数临界的预算；低 $\ell/s$ 的临界区仍不由该界覆盖。新增的是一个真实包含来源和联合像定理，未证明整个 $J$ 首次提升或三原完整中央的跨 $p$ 非零。

## 1. 同一实际立方来源

保 R489/R491 的 $p=6s-1>83$、$f_D<p$，原 $\mathcal W_D$、$Y=\mathscr R$、$\mathcal E=Y\partial_Y$、$d=1+8t$。
取非零实际来源
$$
d^{C_D}\bar P=t^rF^3Q,\qquad
\bar P\in\overline{\mathcal W}_D,\quad r\ge1,
$$
$$
F\in k[t,Y]\text{ 不可约},\quad
F(0,1)=0,\quad F_Y(0,1)Q(0,1)\ne0.
\tag{1}
$$
写 $b=\deg_YF$、$F=\sum_{i=0}^b f_i(t)Y^i$、
$$
u=\max_i(\deg f_i-4i)\ge0.
\tag{2}
$$
$F$ 不是 $Y$ 或角多项式，故 $f_0\ne0$ 且各 $f_i$ 的公因子为 $1$。
剩余域 $k$ 完美，$F$ 不可约且 $P=(0,1)$ 是 $k$ 有理光滑点，故曲线几何整：若有多个共轭几何分支，Galois 传递性及 $P$ 的有理性会使它们都经过 $P$，与光滑矛盾。对几何计算可先扩到代数闭包，所用限制及矩阵秩随后下降。记正规分支为 $Y=\psi(t)$。

所有 Gauss 赋值继续使用 R491 (8) 的原定义，简记为
$v_a$（$a=0$ 或 $h_7$ 两根，权 $4,-1$）、
$v_1$（权 $3,-1$）、$v_d$（权 $2,1$）、
$v_\infty$（权 $-2,9$）。它们对乘积严格相加。

## 2. 固定的十九个吹起及准确交数

从 R489 的 $\mathbb F_4$ 开始。有限底坐标为 $t$、纤维仿射坐标为 $Y$；
负截面是 $Y=0$，另一截面为 $Y=\infty$。
在底无穷远用
$$
T=1/t,\qquad Z=t^4Y.
$$
因此原 $F$ 的局部方程为
$$
T^u F(T^{-1},T^4Z),
\tag{3}
$$
其系数正则。原曲线闭包 $C_0$ 的类、交数为
$$
C_0\sim bS_0+(u+4b)F_0,\qquad
C_0^2=4b^2+2bu,\qquad
K_{\mathbb F_4}C_0=-2u-6b.
\tag{4}
$$

现作以下固定链，所有中心均不在 $P=(0,1)$：

- 在 $t=0$ 及两个 $h_7$ 根处的 $Y=\infty$ 点，各作权 $(4,1)$ 的四步链；
- 在 $(t,Y)=(1,\infty)$ 作权 $(3,1)$ 的三步链；
- 在 $(t,Y)=(-1/8,0)$ 作权 $(2,1)$ 的两步链；
- 在 $(T,Z)=(0,0)$ 作权 $(2,1)$ 的两步链。

这里“权 $(e,1)$ 的链”是**普通吹起**：以局部坐标 $(z,x)$ 开始，依次在 $z=x^jz_j$ 的图中吹起 $x=z_j=0$，$1\le j\le e$。没有把奇异加权曲面当作光滑面。总数为 $3\cdot4+3+2+2=19$ 个几何中心；不分裂的 $h_7$ 点在原域按相应闭点吹起。

所得光滑有理曲面为 $X$，$C$ 为 $C_0$ 的严格变换。令每条链的累计值为 $V_j$、$V_0=0$：

$$
\begin{aligned}
V_j^{(a)}&=b+\min_i\{j\operatorname{ord}_{a}f_i-i\}
&& (a=0,h_7\text{ 两根};\ 1\le j\le4),\\
V_j^{(1)}&=b+\min_i\{j\operatorname{ord}_{1}f_i-i\}
&& (1\le j\le3),\\
V_j^{(d)}&=\min_i\{j\operatorname{ord}_{-1/8}f_i+i\}
&& (1\le j\le2),\\
V_j^{(\infty)}&=ju+\min_i\{-j\deg f_i+(4j+1)i\}
&& (1\le j\le2).
\end{aligned}
\tag{5}
$$
置 $\mu_j=V_j-V_{j-1}$。这些是各次吹起的真实重数，均非负。
证明是将局部方程代入 $z=x^jz_j$：总 $x$ 阶恰为 $V_j$，
减去前面已提取的阶，余下的中心重数就是 $\mu_j$。
(3) 给无穷远一行同样的计算；即使曲线在这些点奇异，公式仍准确。

记
$$
\boxed{\kappa=C^2=4b^2+2bu-\sum_{\text{全部链、全部 }j}\mu_j^2,\qquad
\chi=-K_XC.}
\tag{6}
$$
普通吹起的规范公式及 $\sum_j\mu_j=V_e$ 给
$$
\boxed{K_XC=-2b+
v_0(F)+v_{h_{7,1}}(F)+v_{h_{7,2}}(F)+v_1(F)+v_d(F)+v_\infty(F).}
\tag{7}
$$
这保留每个实际角点；不可仅以一个矩形次数替代 (5)。

## 3. 规范交数严格为负及全部所需 H¹ 消失

**定理 1。** 对每个 (1) 的不可约 $F$，准确有
$$
\boxed{\chi\ge2b,\qquad \kappa\ge2b-2\ge0,\qquad
H^1(X,\mathcal O_X(mC))=0\quad(m\ge0).}
\tag{8}
$$

**证明。** 各 $f_i$ 没有共同角因子。因此在每个负 $Y$ 权角点 $a$，
至少有某个 $f_i$ 在该点为单位，故 $v_a(F)\le-i\le0$；$t=1$ 同理。
另外用非零的常数 $Y$ 系数 $f_0$ 同时估计两个剩余角：
$$
v_d(F)+v_\infty(F)
\le2\operatorname{ord}_{-1/8}f_0-2\deg f_0\le0.
$$
代入 (7) 得 $\chi\ge2b$。$C$ 仍是整 Cartier 曲线，$P$ 光滑未动，
其算术亏格非负。伴随公式
$2p_a(C)-2=C^2+K_XC=\kappa-\chi$
遂给 $\kappa\ge\chi-2\ge2b-2$。

有理光滑面 $X$ 有 $H^1(\mathcal O_X)=H^2(\mathcal O_X)=0$。
对每个 $m\ge1$，
$$
\deg\bigl(\omega_C\otimes\mathcal O_C(-mC)\bigr)
=-\chi+(1-m)\kappa<0.
$$
因此 $H^1(C,\mathcal O_C(mC))=0$。将此用于
$0\to\mathcal O_X((m-1)C)\to\mathcal O_X(mC)\to\mathcal O_C(mC)\to0$
并由 $m=0$ 归纳，得全部 $H^1=0$。此证明没有在正特征使用未付的消失定理。
另有 $H^2(\mathcal O_X(mC))=0$，因为
$H^0(K_X-mC)\subset H^0(K_X)=0$。故
$$
h^0(X,\mathcal O_X(mC))
=1+\frac{m^2\kappa+m\chi}{2}.
\tag{9}
$$
$\square$

## 4. 完整三倍线性系确实在原同一格内

将 $\mathcal O_X(3C)$ 的截面按原 $F^3$ 的平凡化写成多项式 $G(t,Y)$。
吹起投影和 (4) 给
$$
\deg_YG\le3b,\qquad \deg_t G_i\le3u+4i.
$$
每条链的例外除子条件给所有累计值
$V_j(G)\ge3V_j(F)$；特别在最后一步，正是
$$
v_a(G)\ge3v_a(F),\quad v_1(G)\ge3v_1(F),\quad
v_d(G)\ge3v_d(F),\quad v_\infty(G)\ge3v_\infty(F).
\tag{10}
$$
例如有限 $Y=\infty$ 图的方程是 $x^{3b}G$，最后值为
$3b+v_a(G)$；原因子的三倍值为 $3b+3v_a(F)$。
无穷远则用 $T^{3u}G(T^{-1},T^4Z)$，完全同理。
所有中间例外条件也保留；(10) 只是足以回原格的必要子集。

由 (1)、Gauss 乘法及 R491 对原格的双向识别，
$$
\boxed{
d^{-C_D}t^rQ\cdot H^0(X,\mathcal O_X(3C))
\ \subset\ \overline{\mathcal W}_D.}
\tag{11}
$$
确实，乘积的每个原赋值不小于
$v(d^{C_D}\bar P)$，且 $Y$ 次数不超过
$3b+\deg_YQ=\deg_Y(d^{C_D}\bar P)\le D$。
这一步使用**整个**线性系，不要求其由三次乘积生成，也不增加 $D$。

由 (8)，限制到 $2C$ 的序列
$$
0\to\mathcal O_X(C)\to\mathcal O_X(3C)
\to\mathcal O_{2C}(3C)\to0
$$
在全局截面上满射。因此 (11) 支付完整 $F^2$ 厚化上的三倍来源。

## 5. 真实低 r 行也在原预算内

记原每条 charge 的最大 $t$ 阶
$$
\mathsf B_n=A_n+e_{n+1}.
$$
这是 R412 的同一数列，严格递增。由于 (1) 的最低 $t$ 层为
$F(0,Y)^3Q(0,Y)$ 的非零单位倍，且在 $Y=1$ 至少三重零，
它至少有四个非零 charge。理由是 $D<p$，任意不超过三条不同 charge 的
$1,\mathcal E,\mathcal E^2$ 值给单位 Vandermonde。
每条出现的原 charge 都须满足 $r\le\mathsf B_n$。所以
$$
\boxed{r\le\mathsf B_{D-3}.}
\tag{12}
$$

对每个 $0\le j<r$，取 $\mathsf B_n\ge j$ 的最小 $n$，
使用原两列 $Y^nq_nt^{j-A_n}$、$Y^{n+1}q_{n+1}t^{j-A_{n+1}}$。
R412 的原连续列条件在 (12) 内成立：两角指数非负、次数不超过原帽、
$n+1\le D$。首值/首 Euler 导数的 $2\times2$ 行列式仍是两个首单位的乘积。
具体地，$n=0$ 时 $A_0=A_1=0$；$n\ge1$ 时
$j>\mathsf B_{n-1}\ge n+2\ge A_{n+1}$，
而 $j\le\mathsf B_n\le\mathsf B_{n+1}$，正好给两条准确次数条件。
因此最初 $r$ 对行有实际块三角右逆，高尾全部保留。

这只使用已经付清的相邻两列，不把 $t^r$ 当可逆来源。

## 6. 新的同一修正联合界

在 $C$ 上令
$$
\eta(t)=d(t)^{-C_D}t^rQ(t,\psi(t))
=t^r\eta_0(t),\qquad\eta_0(0)\ne0.
\tag{13}
$$
对 (11) 的来源，规范化值与 Euler 导数为
$$
G|_C=\eta^{-1}R|_C,\qquad
(\mathcal EG)|_C
=\eta^{-1}(\mathcal ER)|_C-
\left.\frac{\mathcal EQ}{Q}\right|_C\eta^{-1}R|_C.
\tag{14}
$$
$t^r,d$ 都是角因子；$Q$ 的全部径向项在第二式保留。

**定理 2。** 对原联合映射
$$
R\mapsto(R|_C\bmod t^V,\;(\mathcal ER)|_C\bmod t^N),
$$
若
$$
\boxed{r<N\le V,\qquad
V\le r+2\kappa+\chi-1,\qquad
N\le r+\kappa+\chi-1,}
\tag{15}
$$
则同一 $\overline{\mathcal W}_D$ 中的映射满射。

**证明。** 先用第5节填齐低 $r$ 对行并保高尾；按 (13)–(14) 将剩余长度改为
$V''=V-r$、$N''=N-r$。在 $2C$ 上使用 $L=\mathcal O_C(3C)$。
其两层对偶度为
$$
\deg(\omega_C L^{-1})=-2\kappa-\chi,\qquad
\deg(\omega_C L(-C)^{-1})=-\kappa-\chi.
$$
(15) 恰使加入 $V''P$、$N''P$ 后都严格负度。
所以先实现值 jet，再用 $F$ 倍数的核截面修正法向 jet；
$\mathcal EF(P)$ 为单位，使后者准确满射。
第4节的完整限制把同一个截面返回 (11)，从而回原预算。$\square$

在 R459 的相对 $J$ 可读窗 $r>2k$ 中，
$$
V=2h+k+1,\qquad N=h+k+1.
$$
因此当
$$
\boxed{
2h+k\le r+2\kappa+\chi-2,\qquad
h+k\le r+\kappa+\chi-2,\qquad h+k\ge r}
\tag{16}
$$
时，原单位 $-2$ 与单位 $5$ 两条必要分支 jet 一起可由真格实现。
R491 已付其双 jet 余核仿射偏移为零，但 (16) 不需要挑选别的矩阵或别的修正。

## 7. 界外的真行仍保两最高极条件

本节只把 R489 的对偶接口应用于刚付出的更大实际来源。
在 $2C$ 上取 $\mathscr I=(t^{V''},F t^{N''})$，则显示子格的双 jet 余核对偶为
$$
H^0\!\left(2C,
\operatorname{Hom}(\mathscr I,\omega_{2C}\otimes\mathcal O_{2C}(-3C))\right).
\tag{17}
$$
其两层为
$\omega_C(-3C)(V''P)$ 和 $\omega_C(-2C)(N''P)$。
对原 $\mathcal W_D$ 的真正行，仍须减去第5节低行的全部原高尾，并测试 (11) 外的所有原列；不能将整个 (17) 当原真左核。

使用局部 $n=F$，行写为
$(A+nB)dt\wedge dn/n^2$。
对 R459 两指定目标，(14) 的 $Q$ 径向项乘较高的值 jet，
不进入法向首系数。故同一计算给齐次兼容条件
$$
\boxed{
a_{-N''}-\frac25u_0(-1)^h b_{-V''}=0}
\tag{18}
$$
对全部通过真实列测试的行成立，才可实现这两个必要目标。
R491 支付了右侧确为零；(17) 的全局正则和原列测试仍不可省。
(15) 范围内行空间为零；范围外 (18) 的实际非零尚待证明。

## 8. 高 b 真实来源的主阶及准确临界范围

下列族只用来说明实际来源及几何主阶，**不声称具有原 theta 深接触**。
令奇数 $b\ge5$，
$$
A_b=\lfloor(b+1)/4\rfloor,\quad
B_b=\lfloor(b+1)/3\rfloor,\quad c=\lfloor b/2\rfloor,\quad
E=e_{b+1}-4,
$$
$$
N_b=(th_7)^{A_b}(t-1)^{B_b}(1+t)^E,\qquad
F_b=d^c(Y-1)+N_bY^b.
\tag{19}
$$
有 $F_b(0,1)=0$、$(F_b)_Y(0,1)=1$。
在 $d=0$ 的离散赋值下，其 Newton 多边形是从 $(0,c)$ 到 $(b,0)$ 的单段，
且 $\gcd(c,b)=1$；中间 $Y$ 项在此段严格上方。因此任何有理因子所含根数须被 $b$ 整除，
证明 $F_b$ 在 $k(t)[Y]$ 上不可约。$p>83$ 保 $N_b(-1/8)$ 为单位。

取 $D=3b$，则
$$
\boxed{
P_b=\frac{t(t-1)h_7}{d^{3c}}F_b^3\in\mathcal W_{3b}.}
\tag{20}
$$
清原分母后是
$t(t-1)h_7d^{C_{3b}-3c}F_b^3$；
$C_{3b}-3c=1$。直接用 (8) 的赋值：四个负权角分别至少为 $-2,-2,-2,-1$，
$d$ 角准确达到 $2C_{3b}$，无穷远准确达到 $-2C_{3b}-8$。
故 (20) 保原所有列帽。没有把 $F_b$ 本身称为原来源。

本族 $u=2c=b-1$。三条四步链的累计值为
$\min(jA_b,b-1)$，三步链为 $\min(jB_b,b-1)$；
两条二步链各有重数 $(c,c)$。因此准确有
$$
\chi=2b+4,\qquad
\kappa=\frac{47}{12}b^2+\frac{13}{6}b-\frac{25}{12}
-9\mathbf1_{b\equiv3\ (4)}-\delta_{b\bmod3},
$$
$$
\delta_0=\frac23,\qquad\delta_1=0,\qquad\delta_2=\frac83.
\tag{21}
$$
固定十九步交数而非目标素数扫描给出此式。

例如 $b=13,D=39$ 时，
$\kappa=688,\chi=30,\dim\mathcal W_D=3250$。
$r=1$ 下 (15) 的联合界是 $V\le1406,N\le718$。
证书脚本只核原 Gauss 条件、实际十九次重数与这些整数，不预设深接触。

更一般地，对任何**实际**候选，若
$$
D=3b,\quad
\kappa=\frac{47}{12}b^2+O(b),\quad \chi=O(b),\quad r=O(b),
$$
$$
2s+\ell=\dim\mathcal W_D+o(b^2),\quad
\ell/s\longrightarrow\lambda,\quad
h=\lceil(s-r)/2\rceil,\quad k\in\{0,1\},\quad r+h\ge\ell,
\tag{22}
$$
并保 R459 可读窗，则
$$
\frac{h}{\kappa}\longrightarrow\frac9{8+4\lambda}.
\tag{23}
$$
这里使用原
$\dim\mathcal W_{3b}=141b^2/8+O(b)$。
所以在实际可能的 $1/4<\lambda\le1/2$ 范围，(16) 最终严格成立；
这是一段真正维数临界、$D$ 为 $\sqrt p$ 量级的同格联合像范围。
在边界 $\lambda=1/4$ 须看准确线性项，不能从主项判定。
当 $\lambda\to0$，比例是 $9/8$，当前充分界确实仍有缺口。

(19)–(21) 不证明有候选满足 (22) 的原 theta 接触。
(22) 是对每个已经存在的真候选的准确条件结论；不以人工选择接触阶来制造原首核。

## 9. 相对 J、原 M 与完整中央的界限

本篇联合像支付的是 R459 两必要分支条件。
原 $J$ 其他行、$J(P^{\rm fact})/p$ 的完整 forcing、以及 R481 的同一修正方程均保留。
原 $M$ 继续有
$$
M=c_*U_0m_{13}J,\qquad
K_2^{\rm red}(M)=\ker(\pi\beta_J),\qquad
G_2=C_2(J)/\overline H.
$$
$P_{134}/U_0$、十三自由行、两条十三行 carry 和第三精度没有被这些几何满射删掉。
若使用 R479 的 $B_0,B_1$，它们仍是同一个修正的原边界输出。

三条完整原中央也没有传播到 (11) 的任意截面。
主目标还需真实中央条件约束下的原剩余像/第二障碍或另一条跨 $p$ 非零输入。
固定证书为 [check-r495-fixed-surface-source.py](../scripts/check-r495-fixed-surface-source.py)。

