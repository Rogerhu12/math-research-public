# R1017 — 原曲面在特征5的真正新截面、完整 MW 格与54图交的零值

日期：2026-11-27。会话：`Astra-rank2-Sha-0b097461-20261127`。

**状态：完整证明；实际公开计算已成功。** 本篇给出 R991 原曲面上
一条有明确有理函数坐标的新截面；其高度是 $10/3$，与 deck 共轭
一起生成整个几何 Mordell–Weil 自由部。因此特征5的 Tate 结论
不依赖 R1014 的未知充分大界，也不依赖尚未准入的 Guo–Yang 预印本。
本篇同时完整计算这条几何输入对原54图的作用范围：在5处所有相关
交点均为6挠，故倒6后全部 shadow 为零。这是一个准确的零值，
不把已经构造了新除子当成原最高 AJ 的新非零证明。

## 1. 同一个原曲面与真正截面的坐标

在 $k=\mathbf F_{25}$ 中固定 $\delta^2=-3=2$，令
$\omega=(-1+\delta)/2$。保持 R991(28)–(29) 的原同构和有序坏点：
$$
B:\ v^3=t(1-27t),\qquad
X=-3v,\quad Y=-27t,\quad Y^2+Y=X^3,
\tag{1}
$$
$$
S:\quad y^2+xy+t y=x^3\quad\text{over }B.
\tag{2}
$$
特别 $t=-Y/27$。这里没有再对基曲线作 $[-1]$；$I_9$ 的基点
是 $(X,Y)=(0,0)$，$I_3$ 的基点是 $(0,-1)$。

取基上的有理点和函数
$$
P=(3,1)\in B(\mathbf F_5),\qquad
h=\frac{Y+2}{X-3}.
\tag{3}
$$
以下所有整数系数均按模5理解。定义
$$
x_Q=X+h+2h^2,
\qquad
W_Q=1+3h+3h^2+4h^3+2X+2hX,
\tag{4}
$$
$$
\boxed{\quad y_Q=\frac{\delta W_Q-x_Q-t}{2}.\quad}
\tag{5}
$$
这给出(2)在 $k(B)$ 上的实际点 $Q$。

**原方程的精确验证。** 由(3)，
$Y=h(X-3)-2$。把它代入(1)并除去非零函数 $X-3$，得到
$$
X^2+(3-h^2)X+4+3h+3h^2=0,
\qquad t=2hX+4h+1.
\tag{6}
$$
在 $\mathbf F_5[h,X]$ 模(6)的二次关系中，直接展开(4)给
$$
-3W_Q^2-4x_Q^3-(x_Q+t)^2=0.
\tag{7}
$$
代入(5)即为(2)。这是有理函数恒等式，不是若干基点上的采样。
公开程序还把(4)返回到(1)，以如下分子分母独立作清分母约简：
$$
x_Q=
\frac{2+X+4X^2+3X^3+(3+X)Y}{(X-3)^2},
\tag{8}
$$
$$
W_Q=
\frac{3+2X^2+3X^3+(3+4X+X^2+X^3)Y}{(X-3)^3}.
\tag{9}
$$
实际约简环是 $\mathbf F_5[X,Y]/(Y^2+Y-X^3)$；分母没有被当作
独立变量或在零点处直接求值。

算术 Frobenius $\sigma=\operatorname{Frob}_5$ 只作用系数，固定
基模型的 $X,Y,t$。由于 $\delta^5=-\delta$，(5)给
$$
\sigma(Q)=(x_Q,-y_Q-x_Q-t)=-Q.
\tag{10}
$$
这是实际群法的负点，不只是纯实现上的一个负特征值。

## 2. 极点、两个坏纤维与准确高度

$h$ 在 $P=(3,1)$ 有一阶极点，在基的无穷点 $\infty$ 也有
一阶极点。另一个 $X=3$ 点是 $-P=(3,3)$；在那里 $Y+2$ 同时
为零，商可去。因而(4)在有限处只有 $P$ 可能成为 $Q$ 与零截面
的交点。

在 $P$ 取 $u=X-3$。因为 $2Y(P)+1=3\ne0$，$u$ 是一致化参数，
$h=3u^{-1}+O(1)$。于是
$$
\operatorname{ord}_P(x_Q)=-2,\qquad
\operatorname{ord}_P(y_Q)=-3.
\tag{11}
$$
在无穷处取 $z=-X/Y$，有 $X=z^{-2}+O(z)$、
$Y=-z^{-3}+O(1)$、$h=-z^{-1}+O(1)$。原极小好模型的坐标是
$$
x_{\rm good}=(v/t)^2x_Q,\qquad
y_{\rm good}=(v/t)^3y_Q,
$$
其中 $v/t$ 在无穷处恰有一阶零。式(4)–(5)给
$\operatorname{ord}_\infty(x_Q)\ge-2$、
$\operatorname{ord}_\infty(y_Q)\ge-3$，所以好模型中无极点。
没有把原 Weierstrass 坐标在无穷处的尺度忽略。由(11)，
$$
Q\cdot O=1.
\tag{12}
$$

在 $I_9$ 基点 $(X,Y)=(0,0)$，有
$$
h=1,\qquad x_Q=3,\qquad W_Q=1.
\tag{13}
$$
原节点是 $(x,y)=(0,0)$；(13)不是节点，故截面在 $I_9$ 的恒等
分量，局部高度贡献为0。

在 $I_3$ 基点 $(X,Y)=(0,-1)=(0,4)$，有
$$
h=3,\qquad x_Q=1=-1/9,\qquad W_Q=0,\qquad y_Q=3=1/27.
\tag{14}
$$
这是原 Weierstrass 节点。更精确地，以基参数 $X$ 展开，
$$
x_Q-1=4X+O(X^2),\qquad
W_Q=2X+O(X^2),\qquad
t-3=3X^3+O(X^6).
\tag{15}
$$
节点两切线的斜率是 $2\pm\delta$；(5)、(15)使一条节点分支
参数的阶为1。局部原节点平滑方程经三次基变换成为
$ab=\text{unit}\cdot X^3$，所以另一条分支参数阶为2。
在 $A_2$ 解消后，$Q$ 落在 $I_3$ 的一个非恒等分量；两种
分量编号分别为1、2，均贡献 $2/3$。本篇不人为固定未指定的两
切线编号。

Shioda 高度规范为 $\langle Q,Q\rangle=-\varphi(Q)^2$。
R1014§1已在所有 $q\ge5$ 的同一模型证明 $\chi(\mathcal O_S)=1$，
故高度公式现在给
$$
\boxed{\langle Q,Q\rangle
=2+2(Q\cdot O)-0-\frac23=\frac{10}{3}>0.}
\tag{16}
$$
因此 $Q$ 确实非挠；这一结论不使用 Tate 猜想。

## 3. 两独立截面、特征5 Tate 与完整整格

令 $\tau$ 是原 deck 自同构 $v\mapsto\omega v$，即
$(X,Y)\mapsto(\omega X,Y)$。$Q,\tau Q$ 均由(4)–(5)的明确
函数给出。

先证明它们独立，而不使用 R1014 的充分大界。$\tau$-固定的自由
Mordell–Weil 部分在乘以 torsion 阶后成为真正固定点，下降到原有理椭圆曲面
$$
R:\ y^2+xy+t y=x^3\quad\text{over }\mathbf P^1_t.
$$
它在特征5仍有 $I_3,I_1,IV^*$。该曲面有 $b_2=10$，其零截面、
纤维、$A_2$ 和 $E_6$ 分量已经给10个独立类，故由
Shioda–Tate 及 $\rho\le b_2$，几何 MW 秩为0。这里也可直接用
$x=-ab,y=a^2b,t=ab(1-a-b)$ 看它是有理曲面。

因此 $1+\tau+\tau^2$ 在自由部为零。若 $Q,\tau Q$ 有理线性
相关，$\tau$ 在它们的一维有理张成空间上的特征值只能是1，
与固定自由部为零矛盾。结合(16)得两条独立新截面。

原平凡格秩12，$S$ 的 $b_2=14$；故 $\rho=14$，所有
$H^2_{\rm et}(1)$ 都由除子张成。这直接证明
$$
\boxed{S_5\text{ 满足除子 Tate 猜想，几何 MW 秩为2。}}
\tag{17}
$$
它是 R1014 未知有限删集之外额外支付的一个明确小素数。

R1014§4中不依赖 Tate 的高度论证已证明：在每个 $q\ge5$，
几何 torsion 恰为原 $\mathbf Z/3\mathbf Z$，并在 $\mathbf F_q$
定义。因此 $Q+\tau Q+\tau^2Q$ 是该3挠群中的点。由(10)和
$\sigma\tau\sigma^{-1}=\tau^{-1}$，其 Frobenius 像又等于它的
负点；它同时被固定，所以它为零。于是这里有真正群法等式
$$
Q+\tau Q+\tau^2Q=O.
\tag{18}
$$
高度的 deck 不变性和(18)给
$$
\bigl(\langle\tau^iQ,\tau^jQ\rangle\bigr)_{i,j=0,1}
=\frac53\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\tag{19}
$$

这两点还生成整个自由格。若其指数为 $n$，平凡格判别式绝对值
27、torsion 阶3及 Shioda 判别式公式给
$$
|\operatorname{disc}\mathrm{NS}(S_{\overline5})|
=\frac{27}{3^2}\frac{25}{3n^2}=\frac{25}{n^2}.
\tag{20}
$$
NS 无扭且整，所以 $n=1$ 或5。若 $n=5$，NS 将为 unimodular。
$O,F$ 的交阵 $\left(\begin{smallmatrix}-1&1\\1&0\end{smallmatrix}\right)$
已是 unimodular；它的正交补是负定秩12。Riemann–Roch 给
$D^2\equiv D\cdot K_S\equiv D\cdot F=0\pmod2$，所以该正交补
还是 even。偶 unimodular 格的 signature 被8整除，不能是 $-12$。
因此 $n=1$，并且
$$
\boxed{\begin{aligned}
E(k(B))&=\mathbf Z/3\mathbf Z\oplus\mathbf Z Q\oplus\mathbf Z\tau Q,\\
\mathrm{MW}_{\rm free}&=\tfrac53A_2,\qquad
\operatorname{disc}\mathrm{NS}(S_{\overline5})=-25.
\end{aligned}}
\tag{21}
$$
此处 $k=\mathbf F_{25}$ 已包含整个几何 MW 群，因为给出的两个
生成元及原3挠点都在 $k(B)$。

由(10)、(18)，$\sigma(\tau Q)=Q+\tau Q$。所以固定自由部由
$Q+2\tau Q$ 生成，反固定自由部由 $Q$ 生成，准确为
$$
E(\mathbf F_5(B))=\mathbf Z/3\mathbf Z\oplus
\mathbf Z(Q+2\tau Q),\qquad
\langle Q+2\tau Q,Q+2\tau Q\rangle=10.
\tag{22}
$$
同 R1014§4 的整固定格/Artin–Tate 推导，(17)、(21)也给
$\operatorname{Br}(S_5/\mathbf F_5)=
\operatorname{Br}(S_5/\mathbf F_{25})=0$。这里的 Tate 前提已由
真正坐标(4)支付，不由未发表结论代替。

## 4. 全六个极点位置的完整公开计算

计算只在 [公开 run45929764445](https://github.com/Rogerhu12/math-research-public/actions/runs/45929764445)
的 [job140279423830](https://github.com/Rogerhu12/math-research-public/actions/runs/45929764445/job/140279423830)
执行。源提交是
`72b66100a3bd20ae115ba77a4d0c4b025232d3b9`。实际 PASS 输出时间为
2026-11-27 02:41:06 UTC，数学程序耗时2.461874秒，exit0。

源程序是
[check-r1017-q5-original-new-section.py](../scripts/check-r1017-q5-original-new-section.py)，
SHA256
`7abf40a8234b056d14c0aa26192de2c140e1151da19f67cbf6aa995869340e99`。
完整 stdout 为2444字节，SHA256
`27af604e540d5c10e57c04616d36f683ea85f05a264cfa67419a2dd3e97b423d`；
完整解序列的规范摘要为
`af21464c7307e17f10f940f0d43fa2cb1ab0a4e71ea83d0933caa9881a919a85`。
只保留必要的新坐标、来源和摘要，没有把可重算枚举表写入仓库。

以下说明计算的完备性。若反 Frobenius 点与 $O$ 的交除子是一个
$\mathbf F_5$ 有理点 $P'$，则
$$
x\in L(2\infty+2P'),\qquad
W\in L(3\infty+3P').
\tag{23}
$$
$B(\mathbf F_5)$ 完整为
$$
\infty,(0,0),(0,4),(1,2),(3,1),(3,3).
\tag{24}
$$
对有限 $P'=(a,b)$，取
$h_{P'}=(Y+b+1)/(X-a)$。它恰在 $P',\infty$ 各有一阶极点；
二挠情形也成立，因为分子一阶、分母二阶。相应完整基是
$$
\begin{aligned}
L(2\infty+2P')&=\langle1,h_{P'},h_{P'}^2,X\rangle,\\
L(3\infty+3P')&=\langle1,h_{P'},h_{P'}^2,h_{P'}^3,X,h_{P'}X\rangle.
\end{aligned}
\tag{25}
$$
这些元素线性独立：$h_{P'}$ 定义次数2映射，$X$ 不在
$\mathbf F_5(h_{P'})$，而其余项是对应多项式幂。由 genus1
Riemann–Roch 的维数4、6，(25)确为基。实际闭合乘法关系为
$$
X^2+(a-h_{P'}^2)X+a^2+a h_{P'}^2+(2b+1)h_{P'}=0.
\tag{26}
$$
在 $P'=\infty$，完整基改用
$\{1,X,Y,X^2\}$ 和 $\{1,X,Y,X^2,XY,X^3\}$。

每个 $P'$ 全部枚举 $5^4=625$ 个 $x$ 与 $5^6=15625$ 个 $W$。
后者的 $-3W^2$ 表有7813个不同元素；程序保留每个元素的准确
重数，零与两个符号均计入。对每个 $x$ 检查
$4x^3+(x+t)^2$ 是否在该表中，等价于全体625乘15625对的检验，
没有概率 hash 碰撞或系数截断。全部六个 $P'$ 都处理；结果恰为
(3)–(5)及其负点，其余五个位置没有解。最后逐候选清分母核
原方程，再在原两坏点和极点作局部验证；不是用枚举存在性代替
高度或分量证明。

源文件在任何实际代数构造之前检查
`GITHUB_ACTIONS=true` 和
`GITHUB_REPOSITORY=Rogerhu12/math-research-public`。本地仅作
AST/来源摘要检查，未执行数学搜索。

## 5. 原54图在5处的完整 shadow 确实为零

保 R1011 的固定未 depletion 循环：同一个 $A=E_{27}$、全部54个
degree34 商、原 full9 结构、$\eta_j$ 投影、全部
$\operatorname{Cor}_{L/H}$ 分支及原 $P_-$。取固定系数环
$$
\mathcal R=\mathcal O_{\mathbf Q(\zeta_9)}[1/d],\qquad 6\mid d,
\tag{27}
$$
包含这些实际对应和系数的全部固定分母。倒6不是新丢弃：
$\eta_j$ 的 $1/18$ 平均及 $P_-$ 的 $1/2$、$1/\delta$ 已要求
这些分母。若先用整倍数清分母，则以下结论等价于：所有
$\ell>3$ 的原整局部 shadow 均为零；不声称2、3-primary 原始
整点自动消失。

### 5.1 所有实际图的目标基点只有四种约化

$A$ 在5处好约化且 supersingular。一个直接检验是：在
$\mathbf F_5$ 的短 Weierstrass 形式 $y^2=x^3+a x+b$ 中，
Hasse 不变量是 $(x^3+a x+b)^2$ 的 $x^4$ 系数 $2a$；因此
特征5的 supersingular $j$ 恰为0。$A$ 的 $a=0$。

全部54个商的次数是34，与5互素；有限域中的约化仍为真实可分
同源，所以目标仍 supersingular。原 full9 结构的级也与5互素，
其有限模型与这些同源一同约化。目标不能是 $I_9$ 或 $I_3$
乘法纤维：源是好约化椭圆曲线，与之同源的目标也好约化。
故对每个原图及其每个 Galois 共轭，其目标 $b$ 都在 $S$ 的好
纤维，且满足 $j(b)=0$。

原 $j$ 函数在特征5仍是 R1014(8)。它的全部零点是
$$
t=1/24=4,\quad v^3=2\qquad\text{以及 }\infty.
\tag{28}
$$
立方根 $v$ 的三种选择都在 $\mathbf F_{25}$：$2$ 的阶是4，
而 $\mathbf F_{25}^\times$ 中立方子群的阶是8。
所以(28)是四个真正的 $\mathbf F_{25}$ 基点。这里允许54个图
在约化后有相同基点；没有合并或省掉它们的重数与有限角色权。

### 5.2 每个截面评值均为6挠

三个有限点的纤维都由 $t=4$ 的原方程(2)给出，故在
$\mathbf F_5$ 定义且 $j=0$。无穷处必须用 R1014(4)的好模型，
其纤维是
$$
Y_1^2-27Y_1=X_1^3,
\tag{29}
$$
同样在 $\mathbf F_5$ 定义且 $j=0$。对于任意这样的曲线，变成
$y^2=x^3+b$ 后，立方映射在 $\mathbf F_5$ 上为双射，所以其
点数为6，Frobenius迹为0。Frobenius 的特征多项式恒等式给
$$
\operatorname{Frob}_5^2=[-5],\qquad
E_b(\mathbf F_{25})=E_b[6].
\tag{30}
$$
$Q,\tau Q$ 都在 $\mathbf F_{25}(B)$ 定义；它们作为光滑适当
椭圆纤维化的截面，在(28)的每个点均有实际值。由(30)，这些
值全为6挠。若截面在该点与 $O$ 相交，其值就是0，也包含在该
断言中。

结合(21)，任意几何 MW 截面的四点评值都为6挠。R1014 的
$e_S^+$、最高投影和 Shioda 校正给的对应依旧由真实同源、零
截面与纤维/分量组成；其 Picard 收缩在好纤维上由同源及双同源
作用。群同态保持6挠，固定分母由(27)支付，所以这些校正不
产生一个新的非6-primary 值。

### 5.3 保全 trace 的交公式

R1014(27)中每一个实际项都是
$$
\widehat{\gamma\phi_i}\bigl(r_{\gamma b_i}(D^+)\bigr),
\qquad 1\le i\le54,
\tag{31}
$$
然后施原 $e_A^-$、$\eta_j(\gamma)^{-1}/18$ 权及全部
$\gamma\in\operatorname{Gal}(L/K)$ 的和。式(28)–(30)逐项适用
于每个 $\gamma b_i$；双同源无论在哪个有限常数扩域定义，都
保持点的6挠性质。因此所有(31)先在各自实际有限域中为6挠，
再进入(27)便为零。完整结果是
$$
\boxed{\mathcal S_D(Y_{j,0,\mathcal R}\bmod5)=0
\quad\text{对原 }j\in\{4,10,16\}\text{ 及全部新增除子方向。}}
\tag{32}
$$
此证明保留全部54图、所有 Galois 分支和有限 character；没有
把一个抽样 trace 或未投影点集当成原最高投影。

## 6. 对后继原问题的准确含义

(4)是原曲面上的新几何输入，(17)–(22)完整支付特征5的 Tate、
两实际截面及整 MW 格。与此相容，(32)证明5处的这条最高交值
路线不给任何允许的 $\ell>3$ 非零检测。继续研究一般惰性辅助
$q$ 时，需要其真正截面及原54带权评值；不能由秩2、
$\tfrac q3A_2$ 或正高度推断带权评值非零。

即使另一个 $q$ 给出某个 $\ell$ 的非零整 shadow，仍须沿已付
的 specialization/Kummer 图判定全局最高 AJ，并继续支付该
普通 $\ell$ 位的指定 Bloch–Kato/Coleman 配对非零；全局扩张
非平凡和原 $J^0_{j,\ell}\ne0$ 的量词不能互换。

本篇使用的标准高度、整 MW/NS 及判别式依据与 R1014 相同：
T. Shioda, *Some remarks on elliptic curves over function fields*,
[Astérisque209(1992),99–114](https://www.numdam.org/article/AST_1992__209__99_0.pdf)，
§1、Theorem7；原模型、projector 及全部54图分别见 R991、R995、
R1006、R1011。本篇新的方程恒等式、局部阶、独立性和(32)均已
在正文逐项证明。
