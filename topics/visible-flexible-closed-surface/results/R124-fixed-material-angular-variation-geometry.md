# R124：固定材料角变分直接给实际度量、曲率及稳定求值后验

2026-11-12，Astra-visible-flex-fd2d / root，接 R119、R122。

**状态：以下准确恒等式及条件求值后验已证明。** 给定一份实际有限 l,m,n 场，
沿 R119 唯一指定的固定材料 u 标架 ODE 重建，再积分少量三维角变分，
可以直接得到实际位置图的第一、第二基本形式。
这保留离散 Codazzi 残差在径向积分中的相消，不将形式输入 II 当成实际曲率。
它与 R119 的完整残差绝对值界是两条可选的认证途径，不增加完成标准。

## 1. 实际图及准确角变分

固定 $g=ds^2+a(s)^2du^2$，使用

$$
F_s=FA,\quad X_s=Fe_1,\quad
A=\begin{pmatrix}0&0&-l\\0&0&-m\\l&m&0\end{pmatrix}
=[\alpha]_\times,\qquad \alpha=(m,-l,0)^T.
\tag{1}
$$

这里 e1 是体坐标的第一个标准基向量，$[v]_\times w=v\times w$。
初始准确正交标架使 $F\in SO(3)$。
本方法用于当前角向光滑的有限 Fourier/exponential 场，要求 $\alpha_u,\alpha_{uu}$ 连续，
并具有以下初始角变分；径向仍只要求 A 连续。
这是所给有限场已有的角向正则性，不要求目标 a 为 C³ 或一般曲面额外径向 C³。

定义反对称矩阵 $R=F^TF_u=[r]_\times$，以及

$$
b=F^TX_u,\qquad v=r_u,\qquad c=b_u.
$$

全部角导是在**物理材料 u** 固定定义下求得。准确系统是

$$
\boxed{\begin{aligned}
r_s&=r\times\alpha+\alpha_u,\\
b_s&=-\alpha\times b+r\times e_1,\\
v_s&=v\times\alpha+r\times\alpha_u+\alpha_{uu},\\
c_s&=-\alpha\times c-\alpha_u\times b+v\times e_1.
\end{aligned}}
\tag{2}
$$

**证明。** 由 $F^TF=I$，R 反对称。对其径向求导，

$$
R_s=-AR+RA+A_u=[R,A]+A_u.
$$

叉积矩阵恒等式 $[[r]_\times,[\alpha]_\times]=[r\times\alpha]_\times$
给第一式。由 $X_{su}=F_u e_1$，
$b_s=-Ab+F^TF_ue_1=-Ab+Re_1$，给第二式。
分别对这两式求 u 导数即给后两式。
连续系数的线性 ODE 唯一性，保证从准确初值出发的 (2) 正是 (1) 的角变分，
不是另一张声称相容的位置图。证毕。

对当前中央平面单位速闭曲线、$e_{1,0}$ 竖直、$e_{2,0}$ 为曲线单位切向、N0 为内法向，
令其准确曲率为 n0。初始数据准确为

$$
r_0=(a_0n_0,0,0),\quad b_0=(0,a_0,0),\quad
v_0=(a_0(n_0)_u,0,0),\quad c_0=0.
\tag{3}
$$

最后一个零指体坐标 b 的角导为零，不指真实空间 $X_{uu}$ 为零。
若另用中央几何，必须代入其真实四个初值，不能仍沿用 (3)。

## 2. 直接读取真实第一基本形式

准确位置导数为

$$
X_s=Fe_1,\quad X_u=Fb,\quad
X_{ss}=F(0,0,l)^T,\quad X_{su}=F(r\times e_1),\quad
X_{uu}=F(r\times b+c).
\tag{4}
$$

前三式由 (1) 得到，第四式已在上节证明；最后一式来自 $\partial_u(Fb)$。
因此在目标正交坐标 $(\partial_s,a^{-1}\partial_u)$ 中，实际诱导度量矩阵是

$$
G=\begin{pmatrix}1&b_1/a\\b_1/a&|b|^2/a^2\end{pmatrix}.
\tag{5}
$$

记 $f=b_1/a$、$g_*=|b|^2/a^2$，其相对度量误差准确等于

$$
\boxed{\|G-I\|_{op}=\frac{|g_*-1|}{2}
+\sqrt{\left(\frac{g_*-1}{2}\right)^2+f^2}.}
\tag{6}
$$

这是对称矩阵 $\left(\begin{smallmatrix}0&f\\f&g_*-1\end{smallmatrix}\right)$ 的
两个特征值直接求解所得。若 $b_2^2+b_3^2>0$，实际图浸入，且

$$
\det G=(b_2^2+b_3^2)/a^2>0.
$$

相容时 b=ae2；非零 Codazzi 残差下则由真实系统 (2) 求 b，不能预设该等式。
这个实际 b 也给 R119 的 $C$：$F^TC=b-ae_2$。

## 3. 直接读取真实法向与主曲率

取任一个保持连续的定向符号 $\varepsilon\in\{1,-1\}$，设体法向

$$
\nu=\varepsilon\frac{e_1\times b}{|e_1\times b|}.
\tag{7}
$$

实际空间法向为 $F\nu$。对本题上半图外法向，中央 N 指向内侧，所以取 $\varepsilon=-1$。
在 (5) 的同一目标基中，实际第二基本形式为

$$
H=\begin{pmatrix}
l\nu_3&\nu\cdot(r\times e_1)/a\\
\nu\cdot(r\times e_1)/a&\nu\cdot(r\times b+c)/a^2
\end{pmatrix}.
\tag{8}
$$

由 (4) 与实际法向取点积即得，无需用 Gauss 方程预设相容。
真实主曲率是广义特征值 $\det(H-\kappa G)=0$。
例如可准确取

$$
T=\frac{H_{11}g_*+H_{22}-2H_{12}f}{\det G},
\qquad P=\frac{\det H}{\det G},
\qquad \kappa_\pm=\frac{T\pm\sqrt{T^2-4P}}2.
\tag{9}
$$

因为 G 正定、H 对称，判别式非负。数值显示时将极小负舍入截为0仅属求值处理，
不能在严格计算中以此掩盖不含真实判别式的区间。

若同时求 R122 的 $q_0=F^TX$，则真实径向支撑直接等于 $q_0\cdot\nu$。
因此 (5)、(8) 和支撑属于同一个实际 X，不必把新的形状误差迁移给另一个图。

## 4. 角变分有限求值的稳定后验

给定连续、分段 C1 的实际有限表示 $\widehat r,\widehat b,\widehat v,\widehat c$。
定义完整残差

$$
\begin{aligned}
R_r&=\widehat r_s-\widehat r\times\alpha-\alpha_u,\\
R_b&=\widehat b_s+\alpha\times\widehat b-\widehat r\times e_1,\\
R_v&=\widehat v_s-\widehat v\times\alpha-\widehat r\times\alpha_u-\alpha_{uu},\\
R_c&=\widehat c_s+\alpha\times\widehat c+
       \alpha_u\times\widehat b-\widehat v\times e_1.
\end{aligned}
\tag{10}
$$

令 $\rho_j(s)$ 包住各残差的全角范数，$A_1(s)\ge\sup_u|\alpha_u|$。
若准确初值与有限初值的距离分别不超过 $e_{r,0},e_{b,0},e_{v,0},e_{c,0}$，置

$$
\begin{aligned}
e_r(s)&=e_{r,0}+\int_0^s\rho_r,\\
e_b(s)&=e_{b,0}+\int_0^s(e_r+\rho_b),\\
e_v(s)&=e_{v,0}+\int_0^s(A_1e_r+\rho_v),\\
e_c(s)&=e_{c,0}+\int_0^s(A_1e_b+e_v+\rho_c).
\end{aligned}
\tag{11}
$$

则逐点 $|r-\widehat r|\le e_r$，其余三项同理。

**证明。** 令 $E_j=j-\widehat j$。准确减去 (10)，得到

$$
\begin{aligned}
(E_r)_s&=E_r\times\alpha-R_r,\\
(E_b)_s&=-\alpha\times E_b+E_r\times e_1-R_b,\\
(E_v)_s&=E_v\times\alpha+E_r\times\alpha_u-R_v,\\
(E_c)_s&=-\alpha\times E_c-\alpha_u\times E_b+E_v\times e_1-R_c.
\end{aligned}
$$

每行自身的齐次算子都是反对称矩阵，因此其传播矩阵正交。
按四行的三角顺序应用变常数公式、$|x\times y|\le|x||y|$，即依次得到 (11)。
无一行需要把 $|\alpha|$ 放进 Gronwall 指数，也无须径向的 $\alpha_s$。
若表示有接口跳跃，将该跳跃范数加入对应误差累计；共享值使此项为零。证毕。

系数 $\alpha,\alpha_u,\alpha_{uu}$ 的浮点评价误差必须包含在 (10) 的连续残差内。
ODE solver 的 rtol/atol 和有限点比较本身不等于这些残差上界。

## 5. 从有限变分值到严格 metric 与曲率

令 $\widehat B=(e_1,\widehat b/a)$，$d_b=e_b/a$。
实际目标基微分 $B=(e_1,b/a)$ 与其算子距离不超过 $d_b$，故

$$
\boxed{\|G-I\|\le\|\widehat B^T\widehat B-I\|
+2\|\widehat B\|d_b+d_b^2.}
\tag{12}
$$

这是展开 $B^TB-\widehat B^T\widehat B$ 的乘积界。
若 $\sigma_{min}(\widehat B)>d_b$，则实际最小度量特征值至少

$$
\mu=(\sigma_{min}(\widehat B)-d_b)^2>0.
\tag{13}
$$

也可用 $\widehat t=|e_1\times\widehat b|>e_b$ 直接保证浸入。
对由 $\widehat b$ 得到的同向单位法向 $\widehat\nu$，
单位向量归一化的三角不等式给

$$
|\nu-\widehat\nu|\le d_\nu:=2e_b/\widehat t.
\tag{14}
$$

证明时令 $z=e_1\times b$、$\widehat z=e_1\times\widehat b$，使用
$|z/|z|-\widehat z/|\widehat z||\le2|z-\widehat z|/|\widehat z|$；
$e_b<\widehat t$ 保证实际法向存在且定向一致。

令 $\widehat H$ 按 (8) 使用 $\widehat r,\widehat b,\widehat c,\widehat\nu$ 定义，
仍使用同一个准确 l、a。逐项误差可取

$$
E_{11}=|l|d_\nu,\qquad
E_{12}=\frac{d_\nu|\widehat r\times e_1|+e_r}{a},
$$
$$
E_{22}=\frac{d_\nu|\widehat r\times\widehat b+\widehat c|
+e_r(|\widehat b|+e_b)+|\widehat r|e_b+e_c}{a^2}.
\tag{15}
$$

例如二阶角项用
$r\times b-\widehat r\times\widehat b
=(r-\widehat r)\times b+\widehat r\times(b-\widehat b)$；
其余均为相同的乘积展开。对称误差矩阵满足
$\|H-\widehat H\|\le\max(E_{11},E_{22})+E_{12}$。
结合 (13)，真实正常曲率的 Rayleigh 商给

$$
\boxed{\max_i|\kappa_i|
\le\frac{\|\widehat H\|+\max(E_{11},E_{22})+E_{12}}{\mu}.}
\tag{16}
$$

各式可逐盒计算而非强行取全域单一最坏常数。
支撑还可用 R122 的 $q_0$ 求值界与 (14)；完整闭核再接 R10/R121。
非零 cut 接合误差和固定帽共同二 jet 仍须单独支付。

## 6. 移动计算角与真实程序

若保存场在 $(x,\xi)$ 中，物理变量是 $s=S(x)$、$u=U(x,\xi)$，
必须在每个 x 上先反解 $\xi(x,u)$，并使用

$$
\alpha_u=\alpha_\xi/U_\xi,\qquad
\alpha_{uu}=\alpha_{\xi\xi}/U_\xi^2
-\alpha_\xi U_{\xi\xi}/U_\xi^3.
\tag{17}
$$

随后 (1)–(2) 每个径向 RHS 都乘 $S_x$，即可按 x 积分。
由于材料 u 固定，这里不再加入移动连接或角对流项。
若直接沿固定 ξ 积分却省略对流，那会定义另一张近似图，不是本结果的 X。

实现 `scripts/fd2d-gc-body-actual-prefix.py` 消费已经保存的实际 native Hermite 场，
完整保留 n=nref·expη，使用 (17) 及 (2)。它同时积分 R122 的到原点/见证点体坐标
及固定 y/z 方向；状态名 r,z,w,p 在代码中分别对应正文 r,b,v,c。
每个径向接口用真实保存场连续求值，初值按其准确中央曲线定义求值。
它只做真实几何的线性后处理，不重新解 Codazzi PDE、不修正既有 BVP、不更改 g。

当前有限程序的 extrema 仍标 `finite_evaluation_only=true`、`continuous_certificate=false`。
只有补齐 (10)–(17) 的全域区间、实际接缝和尾/帽后，才能把有限读数提升为完整闭族结论。


## 7. 首个真实前缀的完整有限后处理

2026-11-12 实际 session16717 自然 exit0（最终工具 chunk `e467f2`），826.285秒。
消费 small01 原生场，固定32个材料角，逐个完成全部237径向span，每span取4个新观测点及初点；
不是只检查配点，也没有重新求解 Codazzi BVP。所有观测使用真实 (1)–(3) 中的位置角变分。

| 量 | 全部实际观测的极值 |
|---|---:|
| 归一化 metric 算子误差 | ≤1.6712261825875115e−8 |
| 真实主曲率绝对值 | ≤7.17143548796942 |
| 原点到图的距离 | ≤1.3452395404996786 |
| 真实外法向支持值 | ≥.8110746856665044 |
| 框架角兼容缺陷 | ≤6.597405490081822e−8 |
| 位置角兼容缺陷 | ≤8.535999018691826e−9 |

表中不等式只针对已观测有限集合。积分求解器容差并非严格ODE误差证书，32角采样也不覆盖角间上确界。
实际metric明显小于对残差绝对值积分的诊断surrogate，与径向相消一致；不能反过来把采样数字升级为连续上界。
该分支中央轴差仅8e−5，尾仍为linear starter，故没有达到强幅度、完整接缝或闭核要求。

闭存报告 `notes/2026-11-12-fd2d-small01-actual-body-01-report.json`，SHA
`259096cfc450fe6eed142e38d1c0d608bf0ca37ce13c14f1f4bf0b1be2ceaca2`；
完整节点状态 `...small01-actual-body-01-nodes.npz`，759622B，SHA
`2201a183559bc9220c82d6ab511fad13ca8d9e2740b1ab3013de399ada681365`。
源SHA `5a6f3cfd282a880a3cbd7de0f5694c6d8d339bee82df5492497747fbb626fd4b`，
真实退出及其他实体见同stem `completion-receipt.json`。
