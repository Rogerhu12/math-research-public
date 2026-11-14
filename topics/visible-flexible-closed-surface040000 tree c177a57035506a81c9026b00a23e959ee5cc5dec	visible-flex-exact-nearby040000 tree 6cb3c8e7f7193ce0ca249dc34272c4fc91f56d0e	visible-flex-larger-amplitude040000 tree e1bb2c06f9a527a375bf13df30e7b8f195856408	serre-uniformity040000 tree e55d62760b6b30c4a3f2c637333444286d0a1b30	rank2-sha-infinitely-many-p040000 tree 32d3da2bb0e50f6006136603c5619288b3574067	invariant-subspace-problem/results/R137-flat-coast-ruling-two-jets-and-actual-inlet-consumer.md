# R137：平坦 coast 的直母线两 jet、实际入口及几何消费

## 1. 来源、用途与准确假设

本稿把 [2026-11-09 的完整平坦出口母线构造](../notes/2026-11-09-db6f-flat-outlet-ruling-continuation-v1.md) 改写到当前正交 $l,m,n$ 约定，并实际消费 R136 新前缀的 outward coast。直母线机制及共同材料圆周回收在该旧稿中已经存在；本结果不把它称为新机制。这里的新交付是明确的 Cartesian 两 jet 接口、入口缺陷传播公式和这次真实保存数据上的完整 coast 实体。

先给准确命题。设 $t\in\mathbb R/(2\pi\mathbb Z)$ 是固定材料角，$a_c>0,v>0$ 为常数。入口具有实际周期位置 $X_0(t)$、同向正交标架 $(e_1,e_2,N)$ 和足够光滑的周期函数 $n>0,m$，满足

$$
X_{0,t}=a_c e_2,
$$

$$
e_{1,t}=v e_2+a_c mN,\qquad
e_{2,t}=-v e_1+a_c nN,\qquad
N_t=-a_c m e_1-a_c n e_2.
\tag{1}
$$

入口的 Gauss 曲率为 $0$，所以要接的正交分量为 $l=m^2/n$。这些是假设于实际位置及标架的等式，不能由一组周期 $l,m,n$ 系数自动代替。数值输入未准确满足时，后文明确计算其缺陷。

定义

$$
k=\frac mn,\qquad G=e_1-ke_2,\qquad
B=v(1+k^2)-k_t,
$$

并考虑实际空间直母线

$$
F(t,w)=X_0(t)+wG(t),\qquad w\ge0.
\tag{2}
$$

以下统一要求使用的区域满足

$$
D(t,w)=a_c+wB(t)>0.
\tag{3}
$$

该条件给浸入和共同坐标，不单独给全局嵌入或 reach。

## 2. 母线的实际一、二基本形式

由 (1)，法向项 $a_c(m-kn)N$ 抵消，得到

$$
G_t=vk e_1+(v-k_t)e_2.
\tag{4}
$$

因此

$$
F_w=e_1-ke_2,\qquad
F_t=wvk e_1+\{a_c+w(v-k_t)\}e_2,
$$

$$
F_w\times F_t=DN.
\tag{5}
$$

法向量沿每根母线不变，且 $D>0$ 时为同一个 $N(t)$。由于 $F_{ww}=0$、$G_t\perp N$，

$$
II_{ww}=II_{wt}=0.
$$

再用 $N_t=-a_c n(ke_1+e_2)$，得

$$
II_{tt}=-F_t\cdot N_t=a_c nD.
\tag{6}
$$

一基本形式的行列式为 $D^2$，$I_{ww}=1+k^2$。所以唯一非零主曲率为

$$
\boxed{\kappa(t,w)=\frac{a_c n(t)(1+k(t)^2)}{D(t,w)}.}
\tag{7}
$$

这里保留了 $k_t$；丢掉它会漏掉真实焦点位置。若 $B<0$，正方向的焦点为 $w=a_c/(-B)$；本命题不越过该点。若 $B\ge0$，此母线在正方向没有该种焦点。

## 3. 完整共同材料圆周与准确度量

令 $\rho_c=a_c/v$。在材料角的通用覆盖上作平面展开

$$
P(t,w)=(\rho_c+w)e_r(vt)-wk(t)e_\theta(vt).
\tag{8}
$$

其两个切向量在 $(e_r,e_\theta)$ 中的分量与 (5) 相同，因此 (8) 和 (2) 有相同的一基本形式。展开平面不必在 $t\mapsto t+2\pi$ 后逐点闭合；其旋转单值障碍正是锥角，而真实空间位置 (2) 按输入的周期性闭合。

给定物理经线距离 $\sigma\ge0$，设 $\rho=\rho_c+\sigma$。由 $|P|=\rho$，唯一非负的母线参数为

$$
w(\sigma,t)=
\frac{\rho^2-\rho_c^2}
{\rho_c+\sqrt{\rho_c^2+(1+k^2)(\rho^2-\rho_c^2)}}.
\tag{9}
$$

此式没有小 $\sigma$ 时的平方根相消。因为 $\rho_c+w>0$，可用单一连续角 lift 定义

$$
U(\sigma,t)=t-\frac1v\arctan\!\frac{wk}{\rho_c+w}.
\tag{10}
$$

于是 $P=\rho e_r(vU)$。记 $A=\rho_c+(1+k^2)w$，直接微分或比较有向面积得

$$
\left.\frac{\partial U}{\partial t}\right|_\sigma
=\frac{D}{vA}>0.
\tag{11}
$$

又有 $U(\sigma,t+2\pi)=U(\sigma,t)+2\pi$，因此它不是仅局部可逆：它是整个圆周上的度数一微分同胚。令 $t=t(\sigma,u)$ 为其唯一逆，再在 (2) 中代入 (9)，便得到真正共同材料表达式

$$
\widehat F(\sigma,u)=F\bigl(t(\sigma,u),w(\sigma,t(\sigma,u))\bigr),
$$

$$
\boxed{\widehat F^*e=d\sigma^2+(a_c+v\sigma)^2du^2.}
\tag{12}
$$

各时间若共用 $a_c,v$，同一公式逐时给同一个 $g$。材料对称性也随之传递：例如 $k$ 在镜面反射下为奇函数，而其余实际标架按原镜面对称变换，则 (9)–(10) 与反射相容。上述陈述需要真正的输入对称等式，不把样本误差强制归零。

## 4. 入口全部两 jet 与可调用实现

在 $\sigma=0$，有 $w=0,U=t$。保持新材料 $u$ 不变时，

$$
t_\sigma=\frac{k}{a_c},\qquad t_u=1,
\qquad w_\sigma=1,\quad w_u=0.
$$

因此

$$
\widehat F=X_0,\qquad \widehat F_\sigma=e_1,
\qquad \widehat F_u=a_c e_2.
\tag{13}
$$

把 (6) 变换到该坐标，入口正交二基本形式准确为

$$
(l,m,n)=(nk^2,nk,n)=(m^2/n,m,n).
\tag{14}
$$

结合 (12) 的 Christoffel 符号，完整 Cartesian 两 jet 为

$$
\widehat F_{\sigma\sigma}=lN,\qquad
\widehat F_{\sigma u}=v e_2+a_c mN,\qquad
\widehat F_{uu}=-a_c v e_1+a_c^2nN.
\tag{15}
$$

所以与具有相同实际边界位置、标架和 $K=0$ 二基本形式的 $C^2$ 前片准确接合。不能只匹配抽象 $n,m$ 而忽略位置、标架或角向 monodromy。

实现 [fd2d_k0_ruling_coast.py](../scripts/fd2d_k0_ruling_coast.py) 给出：

- `ruling_coordinates(a,v,sigma,k,k_u,k_uu)`：共同坐标映射与二阶导数，包含 $D$ 及 (11) 的直接交叉核对；
- `propagate(a,v,sigma,inlet)`：从入口材料两 jet 直接计算实际 $X,X_\sigma,X_u,X_{\sigma\sigma},X_{\sigma u},X_{uu}$，再由实际位置导数计算自己的法向、度量和二基本形式；
- `at_material(...)`：带全局角 lift 括号的 Newton 求逆，返回指定固定材料圈上的同一张曲面；
- `inlet_defects(...)`：保留 (1)、位置切向和正交性的实际输入缺陷。

实现使用 (9) 的二次方程隐微分和 (10) 的二阶链式法则，不依赖 $l=(m^2+K)/n$ 去补一个未知末端曲率。当前选定入口仍要求 $n>0$；这与 R128 flat tail 零曲率角区的另一接口无关。

## 5. 沿整个 coast 的一维几何归约

设目标长度为 $L$，并记 $W(t)=w(L,t)$。对每个入口标签，$w$ 随 $\sigma$ 从 $0$ 单调增加到 $W(t)$。因 $D$ 对 $w$ 仿射，

$$
\min_{0\le\sigma\le L}D=\min\{a_c,D(t,W)\},
$$

$$
\max_{0\le\sigma\le L}\kappa
=\max\left\{n(1+k^2),\frac{a_c n(1+k^2)}{D(t,W)}\right\}.
\tag{16}
$$

只要角变量上的这些界已严格支付，就不需要为焦点或准确 rank-one 曲率再加一层径向网格。一个简单充分条件是 $B\ge-\beta$ 且 $a_c-L\beta>0$，因为 (9) 给 $0\le w\le\sigma$。

位置始终是线段 $X_0+wG$，所以对任何固定球心 $q$，全段的 $|X-q|$ 上界只需两个端点。固定方向的板宽和高度极值也只需端点。对 held 标记点 $p$，距离平方的最小值在

$$
w_* = \operatorname{clip}_{[0,W]}
\left(-\frac{(X_0-p)\cdot G}{|G|^2}\right)
\tag{17}
$$

达到；这是整个物理 coast 的准确一维最小值，不能仅取两个端点的距离下界。

在准确输入条件下，法向不随 $w$ 变化，且 $G\cdot N=0$，因此支持函数

$$
-F\cdot N=-X_0\cdot N
\tag{18}
$$

在每根母线上恒定。它可能为负；此时不能凭曲率小和 $D>0$ 自动套用要求正支持函数的法球充分条件。

即使输入只是近似兼容，位置线段性质及 (17) 仍然对定义出的实际曲面成立。令 $C_0=G\times X_{0,t}$、$C_1=G\times G_t$，其真实法向为 $(C_0+wC_1)/|C_0+wC_1|$。实际支持函数等于

$$
\frac{A_0+B_0w}{\sqrt{C+2Dw+Ew^2}},
$$

其中 $A_0=-X_0\cdot C_0$、$B_0=-X_0\cdot C_1$、$C=|C_0|^2$、$D=C_0\cdot C_1$、$E=|C_1|^2$（本式的 $D$ 仅为二次式系数）。其导数分子的非零因子为

$$
B_0C-A_0D+(B_0D-A_0E)w.
$$

所以最小值也只需端点及至多一个区间内驻点。实际法球、非局部自交和全闭核 reach 仍须另付；这些一维归约本身不是 reach 定理。

## 6. 近似入口的缺陷不会被公式抹掉

记实际近似入口的缺陷为

$$
C_X=X_{0,t}-a_c e_2,
$$

$$
A_1=e_{1,t}-v e_2-a_c mN,\qquad
A_2=e_{2,t}+v e_1-a_c nN.
$$

仍定义 $k=m/n$、$F=X_0+w(e_1-ke_2)$，则是一个具体实际曲面，并且准确恒等式为

$$
F_w=M z,\qquad F_t=M y+d,
$$

$$
M=(e_1,e_2),\quad z=(1,-k)^T,\quad
y=(wvk,a_c+w(v-k_t))^T,
$$

$$
d=C_X+w(A_1-kA_2).
\tag{19}
$$

设 $H=M^TM-I$。相对于展开平面的目标第一形式，实际缺陷准确为

$$
\Delta I_{ww}=z^THz,
$$

$$
\Delta I_{wt}=z^THy+(Mz)\cdot d,
$$

$$
\Delta I_{tt}=y^THy+2(My)\cdot d+|d|^2.
\tag{20}
$$

共同材料下的缺陷再以准确坐标 Jac 作合同变换。因此精确输入恢复 (12)，有限输入则保留可计算的有限缺陷。仅把辅助标架正交化、仅检查 Gauss 或仅沿母线绘图，都不能让 (20) 消失。

实际 consumer 对所有二阶 Cartesian 导数重新计算 $E,F,G$、法向和主曲率；其结果没有用辅助 $N$ 代替真实叉乘法向。有限输出的 $l,m,n$ 是实际二形式按目标尺度 $1,a$ 归一的分量；度量有缺陷时，不把这套目标归一切向量称为已经准确正交。对任意这样的 ruled surface，$II_{ww}=0$，所以其实际 $K\le0$；输入稍有不兼容时不应擅自把该实际 $K$ 置零。

## 7. 两 jet 实现的必要核对

[实现核对脚本](../scripts/fd2d_k0_ruling_coast_check.py) 使用两个准确已知曲面：圆锥给 $k=0$ 分支，平面经圆柱弯曲后沿非轴向入口取值给 $k=\tan t\ne0$ 分支。后一例同时检查非平凡材料求逆及全部二阶链式导数。

[核对报告](../notes/2026-11-12-fd2d-k0-ruling-twojet-check-01.json) 的 SHA256 为 `0e04c2aba60cee7a6690f08929a3fbd5407fbe35bfe037195b58916607f15153`。实际调用 `aa3ce7` 退出 $0$，报告内部耗时 $.031055237000146008$ 秒；所有检查中的最大有限误差约 $2.8122\times10^{-13}$。这些是实现检查，不是研究核的连续证书。

## 8. 新34的真实入口、被动重建与完整 coast 实体

物理输入是 R136 的 `7c3f31de…` cyl032 候选。其 outward coast 从

$$
s_c\approx.5919999999999992
$$

开始，具有

$$
a_c\approx1.029181699754392,\quad
v\approx.2587478542495509,\quad
L\approx.2755434451024161.
$$

原真实 IVP 轨道的 $307$ 号保存节点正是该共享入口。原报告在这里记录 metric 约 $3.07\times10^{-12}$、$n_{\min}\approx.20887846$；但原 trajectory 只逐节点保存 $n,m$ 及其径向 RHS，位置/标架只保存最后状态。因此不能把后来的 $s=.719$ 状态或 guard 状态冒充该入口。

[实际消费脚本](../scripts/fd2d_peak_spacer_ruling_consumer.py) 使用以下明示新表示：从中央准确 seed 的实际位置及标架出发，把已保存 $n,m$ 和其第一径向导数定义为共享 $C^1$ 三次 Hermite 字段，只被动积分

$$
X_s=e_1,\quad (e_1)_s=lN,\quad(e_2)_s=mN,\quad
N_s=-le_1-me_2,
$$

其中 $l=(m^2+K)/n$、$K$ 来自同一冻结标量输入。没有重求 $n,m$ PDE。得到的入口再冻结为实际 Fourier 位置/标架字段；它是新的有限表示，不是声称找回了原中间 DOP853 字节。

随后只用 (2)、(9)–(10) 传播完整 coast，并真正求逆到固定 seed-normal $\phi$ 所对应的材料 $u$。以下实体已保存：

- [inlet.npz](../notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz)：冻结入口及精确来源身份；
- [endpoint.npz](../notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-endpoint.npz)：末端固定材料圈上的完整 Cartesian 两 jet、实际 $l,m,n$、位置和标架；
- [overview.npz](../notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-overview.npz)：带真实材料角的全段小位置表；
- [完整报告](../notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-report.json)，SHA256 `3f45f937132e0614b642b29822030cb719de4d300aa1e67179dcff9debef85ab`。

运行 `61552 / 30050b` 自然退出 $0$，耗时 $140.55613315699975$ 秒。入口重建后的实际缺陷包括：位置切向约 $1.3777\times10^{-9}$，角向标架约 $3.7614\times10^{-8}$，正交 Gram 约 $3.73\times10^{-15}$。报告保留这些值，没有借用旧入口更小的数值代替。

对 $65$ 个径向位置、$768$ 个入口角，实际结果如下。

| 量 | 有限计算值 |
| --- | --- |
| $D$ 最小值 | $.21726361773588812$ |
| 实际相对 metric 缺陷最大值 | $1.09111070269619\times10^{-9}$ |
| 实际主曲率绝对值峰 | $4.24891605393483$ |
| 到实际标记点 $(0,A_q,0)$ 的样本最小距离 | $.9603513518153031$ |
| $|y|$ 最大值 | $.790439737666351$ |
| 到原点的半径最大值 | $1.66971588694323$ |
| 实际外向支持函数最小值 | $-.10045924307261947$ |

固定材料末端的求逆残差约 $1.794\times10^{-13}$，其实际 metric 缺陷约 $1.08466\times10^{-9}$，实际曲率峰约 $3.97364$。它可作为随后主回转段的真实位置/两 jet 初猜；本稿未继续重复主线 BVP 或非线性 IVP。

这些数值仍是有限诊断，特别没有用样本 $D>0$ 冒充全角区间证明。负支持函数也明确保留：本次不能自动沿用要求正支持函数的旧法球充分条件。强目标仍需实际非圆核的其余段、完整接尾、全时嵌入与 reach；本结果完成的是这条长 $K=0$ coast 的可消费传播方案。

