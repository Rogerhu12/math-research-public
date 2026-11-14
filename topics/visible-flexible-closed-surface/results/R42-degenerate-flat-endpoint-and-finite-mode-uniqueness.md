# R42：退化平圆领极限与有限模圆柱端唯一性

状态：**已证明，全文独立审查通过。** 作者 `/root/independent_geometry_continued`；独审 `/root/tail_review_continued`；root于2026-11-09全文读取原证明与独审后正式采纳。

只支付文中精确定义的有限模正常端唯一性、完整径向Gauss–Codazzi/周期重构、假设已有周期浸入时的全Cartesian C²平圆领极限及近端局部点对门。实际出口高度由解决定，不存在已解非圆连接或全闭面结论。 本结论不支付G5。

原证明 [冻结稿](../notes/2026-11-09-db6f-audit-degenerate-flat-endpoint-interface-v2.md)，SHA256 `c289b4fda5cefbc679a6519a45fe37830cfa8229bfd09260865a20b99919beab`；[独立全文审稿](../notes/2026-11-09-db6f-tail-review-degenerate-flat-endpoint-v2.md)，SHA256 `68d1c25628d12c408a212e08b22bd0ad0c7e09bdcae1dd6fde10cac56924b06b`，含实际独立精确复跑和另一实现。

以下第1节起数学正文逐字保留；新前言只更新可信度和采用范围。

## 1. 固定有限 Fourier 系统在非退化圆柱端仍唯一

### 1.1 精确指定离散系统

令 $a\in C^2(I)$、$a>0$，$S\in I$，并满足

$$
a(S)=c>0,\qquad a'(S)=a''(S)=0.
\tag{1}
$$

记 $\mathcal T_K$ 为最高 Fourier 模数 $K<\infty$ 的实三角多项式空间，$P_K$ 为它的 $L^2(S^1)$ 正交投影。考虑未知 $M,N\in\mathcal T_K$，在 $N(\theta)>0$ 的开域上满足

$$
\begin{aligned}
L&=\frac{M^2-aa''}{N},\\
M_s&=P_K(L_\theta)-\frac{a'}aM,\\
N_s&=M_\theta+\frac{a'}aN+aa'P_KL,
\end{aligned}
\qquad
M(S)=0,\quad N(S)=c.
\tag{2}
$$

$L$ 不要求是有限三角多项式；投影出现在 (2) 指定的位置。不能把本节结论无条件套给另一个未写清投影或切割方式的离散算法。

### 1.2 局部唯一性只需有限维 Lipschitz 性

选包含初值的一个小系数球，使其上 $N\ge c/2$。在这个球内，系数到 $M,N$ 及其角导数是有限维线性映射；除以 $N$、角微分、积分投影均为系数的光滑运算。$a,a',a''$ 对 $s$ 连续，所以 (2) 是关于系数局部一致 Lipschitz 的有限维非自治 ODE。标准 Picard 迭代或对两个解差的 Grönwall 估计给局部唯一性；这里完全不需要 $a$ 解析。

由 $a'(S)=0$，可缩小区间使 $|a'|<1$。写

$$
\beta=\sqrt{1-a'^2},\qquad
M_{\rm rev}=0,\quad N_{\rm rev}=a\beta,\quad
L_{\rm rev}=-\frac{a''}{\beta}.
\tag{3}
$$

这些常角函数属于每个 $\mathcal T_K$。直接微分得

$$
(a\beta)'=a'\beta-\frac{aa'a''}{\beta}
=\frac{a'}aN_{\rm rev}+aa'L_{\rm rev},
\qquad L_{\rm rev}N_{\rm rev}=-aa''.
$$

故 (3) 是 (2) 的解并具有同一初值，局部唯一性迫使两个解相同。在包含 $S$、满足 $a>0$、$|a'|<1$ 的连通区间上，只要所研究解始终留在 $N>0$ 的开域内，逐点延拓唯一性便保持这个相同。若一个端点使 $\beta\to0$，则 $N_{\rm rev}\to0$，该端点不再属于上述开域。

这里先由有限维唯一性得到旋转系数 (3)，它们另经上面的直接代入满足完整、未投影的 Gauss–Codazzi 方程；然后给定相同圆柱位置和框架，径向框架重构的线性 ODE 唯一，得到的图才是旋转图。没有把一般的投影系数解自动当作真实浸入。

**结论范围。** 非解析 $a$ 本身不能让固定有限 Fourier 截断从精确圆柱末端数据产生非圆分支。真正退化的 $N=0$ 端、无界模数极限以及无限维低正则 PDE 的唯一性均不由本命题决定。本稿也不把有限 Galerkin 方程等同于完整未投影的 Gauss–Codazzi 方程。

## 2. 径向度量及定向：完整符号必须一致

现在研究另一种出口。令 $r\in(r_0,r_1]$，$r_0>0$，共同度量为

$$
g=E(r)\,dr^2+r^2d\theta^2,\qquad E>0.
\tag{4}
$$

内向经线弧长参数满足 $r_s=-1/\sqrt E$。对实际等距浸入 $F$ 定义

$$
e_1=-F_r/\sqrt E,\qquad e_2=F_\theta/r,\qquad n=e_1\times e_2,
$$

$$
A=F_{rr}\cdot n,\qquad B=F_{r\theta}\cdot n,\qquad
C=F_{\theta\theta}\cdot n.
\tag{5}
$$

若 $L,M,N$ 是弧长坐标下的第二基本形式，则坐标变换给

$$
\boxed{A=EL,\qquad B=-\sqrt E\,M,\qquad C=N.}
\tag{6}
$$

$B$ 的负号来自 $r_s<0$，不能从外向约定直接照搬。
度量 (4) 的非零 Christoffel 符号为

$$
\Gamma^r_{rr}=\frac{E'}{2E}=:\eta,\qquad
\Gamma^r_{\theta\theta}=-\frac rE,\qquad
\Gamma^\theta_{r\theta}=\Gamma^\theta_{\theta r}=\frac1r.
\tag{7}
$$

由 $R^r{}_{\theta r\theta}=rE'/(2E^2)$ 得
$K=E'/(2rE^2)$。因此 Gauss–Codazzi 方程恰为

$$
\boxed{AC-B^2=\frac{rE'}{2E},}
\tag{8}
$$

$$
\boxed{
B_r=A_\theta+\left(\frac{E'}{2E}-\frac1r\right)B,\qquad
C_r=B_\theta+\frac Cr+\frac rE A.}
\tag{9}
$$

例如第一条 Codazzi 恒等式来自
$\nabla_\theta h_{rr}=A_\theta-2B/r$ 与
$\nabla_r h_{r\theta}=B_r-(\eta+1/r)B$。
第二条来自
$\nabla_\theta h_{r\theta}=B_\theta-C/r+rA/E$ 与
$\nabla_r h_{\theta\theta}=C_r-2C/r$。

当 $C\ne0$ 时，(8) 可以代入为正常形

$$
A=\frac{B^2+rE'/(2E)}{C},\qquad
B_r=A_\theta+(\eta-1/r)B,\qquad
C_r=B_\theta+C/r+rA/E.
\tag{10}
$$

平面圆领处是 $C=0$，因此不能把 (10) 在端点当作普通的 Lipschitz 初值 ODE；也不能因这种写法退化便宣称非圆分支已经存在。

### 2.1 旋转背景的符号检查

若选一次固定的 $w(r)$，令

$$
E=1+w^2,\qquad F_{\rm rev}=r e_r+h(r)e_z,\qquad h_r=-w,
\tag{11}
$$

则按 (5) 的定向

$$
n=-\frac{w e_r+e_z}{\sqrt E},\qquad
A_0=\frac{w_r}{\sqrt E},\qquad B_0=0,\qquad
C_0=\frac{rw}{\sqrt E}.
\tag{12}
$$

于是 $A_0C_0=rww_r/E=rE'/(2E)$，且
$C_0'=C_0/r+rA_0/E$。如果取 $h_r=+w$，在相同内向定向下 $A_0,C_0$ 都变号。只有 $E=1+w^2$ 而没有高度导数的符号，不能确定背景第二基本形式。

## 3. 周期位置图的重构没有被 Gauss 方程一项代替

把正交框架写为列矩阵 $Q=(e_1,e_2,n)\in SO(3)$。由 (7) 得

$$
Q_r=QU,\qquad Q_\theta=QV,
\tag{13}
$$

$$
U=\begin{pmatrix}
0&0&A/\sqrt E\\
0&0&-B/r\\
-A/\sqrt E&B/r&0
\end{pmatrix},\qquad
V=\begin{pmatrix}
0&1/\sqrt E&B/\sqrt E\\
-1/\sqrt E&0&-C/r\\
-B/\sqrt E&C/r&0
\end{pmatrix}.
\tag{14}
$$

三个独立相容式
$U_\theta-V_r+VU-UV=0$ 恰是 (8)–(9)。这是实际框架的平坦性条件，不是另加的一组近似条件。

现假设 $E,A,B,C$ 在开带内足够光滑，$A,B,C$ 为 $2\pi$ 周期，并满足 (8)–(9)。在一个内切口 $r_1$ 给定真实、周期的初始位置和框架，满足

$$
Q_\theta(r_1)=Q(r_1)V(r_1),\qquad
F_\theta(r_1)=r_1e_2(r_1).
\tag{15}
$$

沿 $r$ 解 $Q_r=QU$、$F_r=-\sqrt E e_1$。因 $U$ 反对称，$Q$ 保持在 $SO(3)$。
令 $Z=Q_\theta-QV$。用相容式直接算得 $Z_r=ZU$；由 (15) 得 $Z=0$。
再令 $D=F_\theta-re_2$，由 $Q_\theta=QV$ 与 (14) 得

$$
D_r=-\sqrt E\left(-\frac1{\sqrt E}e_2-\frac B{\sqrt E}n\right)-e_2-Bn=0.
$$

故 $D=0$，(4) 的全部度量恒等式成立，第二基本形式恰为 (5)。周期性也从径向 ODE 的唯一性和周期初值继承：$Q(r,\theta+2\pi)$ 与 $Q(r,\theta)$ 解同一个初值问题，位置积分同理。

因此本节可从一个真实闭合的活动侧 Cauchy 切口出发。任意不带 (15)、不检验周期初值的 $(A,B,C)$ 数值表不能直接冒充闭合位置图；单独支付 (8) 也不够。

## 4. 平圆领极限定理：真正的全 Cartesian 两jet

### 4.1 假设与极限圆

设已存在上述周期等距浸入 $F$，并且在 $r\downarrow r_0>0$ 时

$$
E\longrightarrow1,\qquad E'\longrightarrow0,\qquad
a_*(r):=\|A(r,\cdot)\|_\infty\longrightarrow0,\qquad
b_*(r):=\|B(r,\cdot)\|_\infty\longrightarrow0,\qquad
c_*(r):=\|C(r,\cdot)\|_\infty\longrightarrow0.
\tag{16}
$$

这里 $E$ 与 $E'$ 在端点有相应连续延拓，第二基本形式在角度上统一趋零。
定义可实际估计的函数

$$
J(r)=\int_{r_0}^r\left(\frac{a_*(u)}{\sqrt{E(u)}}+\frac{b_*(u)}u\right)du.
\tag{17}
$$

由 (16)，被积函数在端点有界，$J(r)\to0$。从 (14) 可得 $e_1,e_2,n$ 在端点均有一致极限，并分别满足

$$
\|e_i(r)-e_i^0\|_\infty\le J(r),\qquad
\|n(r)-n^0\|_\infty\le J(r).
\tag{18}
$$

又因 $|F_r|=\sqrt E$ 在端点可积，$F$ 有一致位置极限 $F^0$。
角向框架方程在端点一致趋于

$$
(e_1^0)_\theta=-e_2^0,\qquad
(e_2^0)_\theta=e_1^0,\qquad
(n^0)_\theta=0,\qquad
(F^0)_\theta=r_0e_2^0.
\tag{19}
$$

一致收敛的导数确实是极限函数的导数：在任意固定角区间对 (14) 积分并取极限即可，未交换未经控制的高阶导数。
于是 $n^0$ 是常向量，$e_1^0,e_2^0$ 是这个平面中频率恰为一的正交旋转框架，并且

$$
F^0+r_0e_1^0=p_0
\tag{20}
$$

为常向量。极限因此是中心 $p_0$、半径 $r_0$ 的完整平面圆；不是一般闭曲线，也没有多重绕圈。

### 4.2 精确 C3 等变迫使圆同轴，并固定材料两jet

再假设原图具有与活动核心相同的精确等变性

$$
F(r,\theta+\omega)=R_\omega F(r,\theta),\qquad \omega=2\pi/3,
\tag{21}
$$

其中 $R_\omega$ 是绕固定竖轴的转动。微分与取极限使位置、框架继承 (21)。故 (20) 的 $p_0$ 在竖轴上，$n^0$ 是 $\pm e_z$。由 (19)，若 $n^0=+e_z$，框架的材料角转动方向是 $R_{-\theta}$，与 (21) 的 $R_{+\omega}$ 不相容，因为 $\sin\omega\ne0$。所以 $n^0=-e_z$，存在常数 $z_0,\phi_0$，使

$$
F^0(\theta)=r_0 e_r(\theta+\phi_0)+z_0e_z,\qquad
e_1^0=-e_r(\theta+\phi_0),\qquad e_2^0=e_\theta(\theta+\phi_0).
\tag{22}
$$

考虑固定平面模型
$F_{\rm flat}(r,\theta)=r e_r(\theta+\phi_0)+z_0e_z$。
在 $r=r_0$，实际图的全部两阶极限为

$$
\begin{aligned}
F&\to F_{\rm flat},& F_r&\to e_r,&F_{rr}&\to0,\\
F_\theta&\to r_0e_\theta,&F_{r\theta}&\to e_\theta,&
F_{\theta\theta}&\to-r_0e_r.
\end{aligned}
\tag{23}
$$

这里 $e_r,e_\theta$ 的角均为 $\theta+\phi_0$。证明不只依赖度量趋近：由真实 Gauss 公式

$$
F_{rr}=\eta F_r+An,\qquad
F_{r\theta}=e_2+Bn,\qquad
F_{\theta\theta}=\frac r{\sqrt E}e_1+Cn
\tag{24}
$$

和 (16)、(18) 逐项得到 (23)。以 $F_{\rm flat}$ 延拓到 $r\le r_0$ 后，各阶偏导连续接合，因而是 C² 浸入；端点的实际导数由积分的微积分基本定理给出。

对相位族 $F_\alpha(r,\theta)=R_\alpha F(r,\theta-\alpha)$，(22)–(23) 逐点不变。故整段固定平环上的材料图在所有相位确实相同；不只是其像集合不变。相位作用连续地作用于 C² 函数，因而该局部族在 C² 拓扑下连续。

若没有 (21)，(20) 仍给一个平面圆，但其中心与法向未必适配指定相位轴；不能略去这个区别。$z_0$ 也由实际解决定，不能由本定理任意设为几何模板要求的 $.094$。

### 4.3 可直接转成误差预算的估计

在 (22) 的坐标中，(18)、(24) 给以下全角上界：

$$
\begin{aligned}
\|F_r-e_r\|_\infty
&\le |\sqrt E-1|+\sqrt E\,J,\\
\|F_\theta-r e_\theta\|_\infty&\le rJ,\\
\|F-F_{\rm flat}\|_\infty
&\le\int_{r_0}^r\bigl(|\sqrt{E(u)}-1|+\sqrt{E(u)}J(u)\bigr)du,\\
\|F_{rr}\|_\infty&\le\frac{|E'|}{2\sqrt E}+a_*,\\
\|F_{r\theta}-e_\theta\|_\infty&\le J+b_*,\\
\|F_{\theta\theta}+r e_r\|_\infty
&\le \frac r{\sqrt E}J+r\left|\frac1{\sqrt E}-1\right|+c_*.
\end{aligned}
\tag{25}
$$

这些是位置图自身的估计，不把近似度量的 C0 误差当作二阶数据控制。所有相位有同一上界，因为刚体转动与角平移不改变各全角范数。

## 5. 平领附近的嵌入与自有点对门可以单独支付

本节只涉及已经存在的平圆领附近很小的活动尾段与固定平环，不覆盖活动核心或外桥。

固定 $0<d_0<r_0/4$，将图按第 4 节延拓为平面图到 $r\in[r_0-d_0,r_0]$。
对足够小的 $\epsilon>0$，整个参数环
$[r_0-d_0,r_0+\epsilon]\times S^1$ 的半径比小于二，并且在平面极坐标识别下

$$
\|D(F-F_{\rm flat})\|\le1/10.
\tag{26}
$$

这由 (25) 的一阶估计及左半段恒为零得到。给两个参数平面点，记其弦长为 $d$；沿较大半径转动较短角，再走径向段，得到位于参数环内的折线路径。它的长度 $L_0$ 满足

$$
L_0\le |r-r'|+\max(r,r')\,|\Delta\theta|
\le(1+\pi)d<5d.
\tag{27}
$$

第二步使用 $|\Delta\theta|\le\pi$、
$2\sqrt{rr'}\sin(|\Delta\theta|/2)\le d$，以及半径比小于二。
沿此路径对 (26) 积分得实际空间弦长至少 $d-L_0/10>d/2$。
所以不同参数点的像不同；联合 C² 与秩二已给嵌入。实际路径长度 $L$ 还满足

$$
L\le(11/10)L_0<11|F(P)-F(Q)|.
\tag{28}
$$

正交单位切向基下，形算子矩阵的元素是
$A/E$、$B/(r\sqrt E)$、$C/r^2$，因此可取主曲率绝对值上界

$$
\kappa\le\frac{a_*}{E}+\frac{2b_*}{r\sqrt E}+\frac{c_*}{r^2}.
\tag{29}
$$

右端在外侧尾段上随 $\epsilon\downarrow0$ 一致趋零，内侧平面段上为零。
若同一整段的上界为 $\kappa_*$，沿 (28) 的路径积分法向变化得

$$
|(F(Q)-F(P))\cdot n(P)|\le\frac12\kappa_*L^2.
$$

从而

$$
2|(F(Q)-F(P))\cdot n(P)|
\le121\kappa_*|F(Q)-F(P)|^2.
\tag{30}
$$

故任意预给有限 $\tau>0$，只要再缩小尾段，使
$\kappa_*\le1/(121\tau)$，这一平领局部的所有有向法向点对就有半径 $\tau$。这个结论仍没有给与远处活动核心、固定帽、未知桥的混合点对；也不把有边环片的 normal-pair 证书直接称为完整闭面的 reach。

## 6. 一个明确但尚未验证的加权端点类

若在 $(r_0,r_1]$ 中 $w>0$，$E=1+w^2$ 固定，且 $w,w_r\to0$，则可给 (16) 一组更直接的充分条件。假设存在固定 $0<k\le K_0<\infty$ 使

$$
k\frac{rw}{\sqrt E}\le C(r,\theta)\le
K_0\frac{rw}{\sqrt E},\qquad
\frac{b_*(r)^2}{w(r)}\longrightarrow0.
\tag{31}
$$

于是 $C\to0$、$B\to0$。由真实 Gauss 方程 (8) 得

$$
|A|\le
\frac{\sqrt E}{kr}\frac{b_*^2}{w}+
\frac{|w_r|}{k\sqrt E}\longrightarrow0.
\tag{32}
$$

又 $E'=2ww_r\to0$，所以 (16) 全部成立。这个推导允许 $w_r$ 变号，绝对值已写在 (32) 中。

(31) 不是必要条件，不是已经证明存在解的函数空间，也未宣称当前任何尾部满足它。它只是可以逐项核验的充分类。特别地，单独知道 $B,C\to0$ 不能控制商
$(B^2+rE'/(2E))/C$；若分母消失过快，$A$ 仍可能发散，无法 C² 贴平。

如 $w=(r-r_0)^p$、$p>1$，旋转背景确实满足所有平领条件；这仅提供平领接口非空的旋转例。它没有非圆活动核心，更没有给可见弯曲。用这个例子替换现有 flat17 的固定背景会改变物理度量，不能被记入原 G5 收敛序列。

## 7. 一个实际边值问题还必须提供什么

若要应用于 `audit-flat058-geometric-template` 的强比例模型，应在计算前固定一次完整共同度量与物理参数，然后完成以下真实任务：

1. 活动侧给来自非圆核心精确局部片的完整位置、框架、第二基本形式，满足周期闭合与精确 C3 等变；径向切口必须已进入真实 $a_s<0$ 的分支，不能将核心 $a_s=0$ 或经线转折点强行装进 (4) 的坐标。同一次完整度量还要允许 $r_0=.579$ 的退化出口。
2. 在同一固定 $E(r)$ 上求周期 (8)–(9)，而不是只拟合点上 Gauss 约束；需要来源明确的真正尾部或严格存在性方法。
3. 证明 (16)，或更强的 (31)，并用自己的误差界支付 (25)。有限截断 Robin 响应本身不是这些极限条件的证明。
4. 计算并控制真实出口高度 $z_0$。若不等于几何模板要求的 $.094$，必须重做完整位置和点对预算；不能靠独立移动出口圈保留原共同度量。
5. 将固定平环接到同一材料帽的固定外桥，支付全部未知连接上的包围、曲率与混合点对，再生成全闭面并执行 README 的加密和独立全流程。

本稿没有把这些任务完成，也不改变已有 flat17 主线、求解容差、源系数或 G5 判据。它给出的是一个精确端口、全部符号、一个可复用的 C² 极限定理和可操作的局部几何门。

## 8. 核验与出处边界

本稿的 Gauss–Codazzi、矩阵平坦性、坐标转换和旋转背景恒等式由附属符号脚本独立于任何实际候选作精确核验；算术输出只记录恒等式状态和源身份。有限维唯一性、框架极限、C3 对轴和局部点对证明均已在正文展开，不能由符号测试代替全文审查。

仓库来源包括 R6 的真实切口两jet原则、R27/R29 的核心与相位机制、R38 的合法一阶 Gauss–Codazzi及周期框架重构、`audit-cylindrical-cuff-and-analytic-endpoint` 的解析出口反例和 `audit-flat058-geometric-template` 的新平环位置。它们的具体 SHA 随来源清单记录。这里的有限维唯一性直接由局部 Lipschitz 差估计证明，未引用或扩张一个未核查的无限维唯一性定理。
