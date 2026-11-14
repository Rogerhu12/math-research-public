# R82：完整材料角下的相对角向度量输运及当前入口的严格有理点

日期：2026-11-10。作者：Astra-visible-flex-78718bd0 / geometric_closure。

**状态：已证明。** 本文证明一般 $C^2$ 曲面的恒等式、有限向量基投影的
准确源分解，以及当前指定 raw CP 入口的有理单点下界。对仅分段给出的 PP，
恒等式逐开放区间成立，跨节点必须保留实际 jump。本文不从浮点 Hermite
生成过程推断其 binary 系数在实数意义精确 $C^2$，也不增设全题光滑性门。
沿程 Gauss 积分、采样 FFT 和高模入口重投影均留在工作笔记，不是本定理
的严格连续数值结论。本文不产生新曲面或支付 README 的闭合/G5。

## 1. 设定与主结论

令 $I$ 为径向区间，$a:I\to(0,\infty)$ 为 $C^1$ 函数。令
$F:I\times S^1\to\mathbb R^3$ 和角图的 degree-one lift
$\Theta:I\times\mathbb R\to\mathbb R$ 为 $C^2$，且
$\Theta(s,\psi+2\pi)=\Theta(s,\psi)+2\pi$、
$\rho=\Theta_\psi>0$。定义材料角 $u=\Theta(s,\psi)$ 及
$$
b=\frac{\Theta_s}{\rho},\qquad
D_s=\partial_s-b\partial_\psi,\qquad
D_u=\rho^{-1}\partial_\psi.
\tag{1}
$$
假设每条角曲线满足 $F_\psi\ne0$、曲率 $\kappa>0$，并处在
$$
\left|\frac{a_s}{a}\right|<\kappa
\tag{2}
$$
的正根域。令 $\tau$ 为其单位切向，$\nu$ 为主法向，
$\eta=\tau\times\nu$，$\mu=a_s/a$。取与实际原流一致的物理速度
及固定角图速度
$$
V=-\frac{\mu}{\kappa}\nu+
\sqrt{1-\frac{\mu^2}{\kappa^2}}\,\eta,
\qquad W=V+bF_\psi.
\tag{3}
$$
定义
$$
T=D_uF,\quad G=|T|^2,\quad
e=D_sF-V=F_s-W,\quad \Gamma=G/a^2-1.
\tag{4}
$$

**定理1。** 在上述假设下，
$$
\boxed{D_s\Gamma=\frac2{a^2}T\cdot D_ue},
\tag{5}
$$
以及
$$
|D_sF|^2-1=2V\cdot e+|e|^2,
\qquad (D_sF)\cdot T=e\cdot T.
\tag{6}
$$
在仅 $C^2$ 情形，(5) 右侧使用乘积弱导数
$$
T\cdot D_ue:=D_u(T\cdot e)-(D_uT)\cdot e;
\tag{7}
$$
它有由左侧给出的连续代表。若 $e$ 额外为 $C^1$，(5) 就是通常的逐点
公式，不需要弱导数解释。若 $e=0$，则每条固定材料角射线上
$\Gamma(s,u)$ 恒定。

这最后一项保持的是相对误差 $G/a^2-1$，并非一般保持绝对差 $G-a^2$，
也不说明原流会消去非零入口误差。

## 2. 定理1的完整证明

由于 $\rho b=\Theta_s$，混合导数相等给
$$
[D_s,D_u]
=\frac{-\rho_s+b\rho_\psi+\rho b_\psi}{\rho^2}\partial_\psi=0.
\tag{8}
$$
因此 $D_sT=D_u(D_sF)$。这也可由 $C^2$ 坐标变换到 $(s,u)$ 后直接
看出。这里固定 $\psi$ 一般不是固定材料角，必须保留(1)中的平流项。

置 $\lambda=|F_\psi|$。Frenet 分解和 $\rho>0$ 给
$$
|V|=1,\qquad V\cdot T=0.
\tag{9}
$$
又
$$
D_uT=\rho^{-2}F_{\psi\psi}-\rho_\psi\rho^{-3}F_\psi.
$$
第二项与 $V$ 正交，第一项在 $\nu$ 方向的分量为
$\kappa\lambda^2/\rho^2=\kappa G$。故对任意满足正根域的状态，
$$
V\cdot D_uT=-\mu G.
\tag{10}
$$
它不要求 $G=a^2$；仅在已经等距的子集才可把右端改写为 $-aa_s$。

对光滑数据，(8)–(10) 给
$$
D_sG=2T\cdot D_u(V+e)
=2\mu G+2T\cdot D_ue.
\tag{11}
$$
因 $D_sa=a_s$，将(11)除以 $a^2$ 并减去分母导数即得(5)。
把 $D_sF=V+e$ 代入范数与内积，使用(9)，得到(6)。

现检查只具 $C^2$ 时没有隐藏的三阶要求。此时 $T$ 为 $C^1$，
$D_sF$ 为 $C^1$，$V$ 和 $e$ 至少连续。用(7)所定义的乘积弱导数，有
$$
T\cdot D_uV=D_u(T\cdot V)-(D_uT)\cdot V=\mu G.
\tag{12}
$$
右端连续；第一项准确为零，不需要单独存在 $D_uV$ 的经典导数。
同时 $D_u(D_sF)$ 是连续函数。因此(11)、(5)在分布意义成立，且右侧
由连续左侧代表。最后，$e=0$ 时在材料坐标中 $\partial_s\Gamma=0$，
故沿每条材料线恒定。证毕。

## 3. 原有限 Cartesian 投影的准确缺口

在原表示中，写
$$
F=X_0(s,\psi)+q\sum_iY_i(s)B_i(\psi)+\bar z(s)e_z,
\quad X_0=a(s)e_r(\Theta(s,\psi)),
\tag{13}
$$
其中 $q$ 为常数，$B_i$ 是完整 Cartesian 向量基。令 $\Pi_{M,N}$ 表示
在原 $N$ 个角点求出有限基系数后重建，并补入竖直均值的实际采样投影。
这里把采样及求和本身看成其准确有限数学算子；浮点求值若产生舍入，须
另计相应有限误差，不能借本代数式自动消去。

原系数 RHS $R=R_{M,N}(s,Y)$ 的定义等价于
$$
q\sum_iR_iB_i=\Pi_{M,N}(W-X_{0,s})-\langle W_z\rangle_Ne_z.
\tag{14}
$$
于是有准确恒等分解
$$
\begin{aligned}
e_{\rm proj}&=(\Pi_{M,N}-I)(W-X_{0,s}),\\
e_{\rm interp}&=q\sum_i(Y_i'-R_i)B_i,\\
e_{\rm mean}&=(\bar z'-\langle W_z\rangle_N)e_z,\\
e&=e_{\rm proj}+e_{\rm interp}+e_{\rm mean}.
\end{aligned}
\tag{15}
$$
**证明。** 将右侧相加，(14)中的有限投影和竖直均值两两消去，剩下
$X_{0,s}+q\sum_iY_i'B_i+\bar z'e_z-W=F_s-W=e$。证毕。

$e_{\rm mean}$ 不依赖角变量，故 $D_ue_{\rm mean}=0$，不进入(5)。
另外两项必须对实际投影重构后的函数求材料导数。例如
$$
D_ue_{\rm proj}=\rho^{-1}\partial_\psi
[(\Pi_{M,N}-I)(W-X_{0,s})].
\tag{16}
$$
这不是把 $D_u$ 先作用到 raw 速度再投影。$\rho^{-1}$ 随角变化，
$B_i$ 的 Cartesian 方向也随角转动；没有使用
$D_u\Pi_{M,N}=\Pi_{M,N}D_u$ 这种一般不成立的交换式。
故(15)将有限投影源、保存系数导数的 ODE 残差、纯径向均值重构误差
明确区分，而不要求当前状态已经满足任何 Galerkin ODE。

## 4. 三重对称材料轴上的完整标量公式

取当前使用的角图形式
$$
\Theta(s,\psi)=\psi-\frac{w(s)}3\sin3\psi,
\tag{17}
$$
其中 $w(s)$ 包含原 spline 与末端 cutoff 的全部因子。取
$\psi=0,\pi/3$，记 $\sigma=\cos3\psi=1,-1$。在这两轴上
$$
u=\psi,\quad b=0,\quad
\rho=1-\sigma w(s),\quad \rho_s=-\sigma w_s(s).
\tag{18}
$$
它们确为固定材料线，但 $\rho_s$ 通常非零。

把原有限向量基的水平扰动写为
$$
R_\theta=Y_0+\sum_{j=1}^M Y_{R,j}\cos(3j\psi),\qquad
T_\theta=\sum_{j=1}^M Y_{T,j}\sin(3j\psi),
$$
并令竖直扰动为余弦模之和。完整水平向量是
$R_\theta e_r(\psi)+T_\theta e_\theta(\psi)$。因
$e_r'=e_\theta$、$e_\theta'=-e_r$，
$$
\partial_\psi(R_\theta e_r+T_\theta e_\theta)
=((R_\theta)_\psi-T_\theta)e_r
+(R_\theta+(T_\theta)_\psi)e_\theta.
\tag{19}
$$
在两轴上，其径向分量和竖直导数均为零。定义线性泛函
$$
\mathcal B_\sigma(Y)=Y_0+\sum_{j=1}^M\sigma^j
(Y_{R,j}+3jY_{T,j}),\qquad B_\sigma=\mathcal B_\sigma(Y).
\tag{20}
$$
从(13)、(18)、(19)立即得到
$$
F_\psi=(a\rho+qB_\sigma)e_\theta,\quad
r_\sigma=\frac{qB_\sigma}{a\rho},\quad
\Gamma_\sigma=r_\sigma(2+r_\sigma).
\tag{21}
$$
这保留了旋转基导数给出的 $Y_0$ 和全部 $Y_{R,j}$。

对任意系数导数 $Z$，令
$$
\mathcal D_\sigma(Y,Z)=
\frac{2(1+r_\sigma)q}{a\rho}
\left[\mathcal B_\sigma(Z)-B_\sigma
\left(\frac{a_s}{a}+\frac{\rho_s}{\rho}\right)\right].
\tag{22}
$$
对(21)直接求导，并用(5)、(15)，得到
$$
\begin{aligned}
\partial_s\Gamma_\sigma&=\mathcal D_\sigma(Y,Y'),\\
\frac2{a^2}T\cdot D_ue_{\rm proj}
&=\mathcal D_\sigma(Y,R),\\
\frac2{a^2}T\cdot D_ue_{\rm interp}
&=\frac{2(1+r_\sigma)q}{a\rho}\mathcal B_\sigma(Y'-R).
\end{aligned}
\tag{23}
$$
第二式可在固定状态处暂取系数导数为 $R$、均值导数为
$\langle W_z\rangle_N$，再应用(5)证明；它是该状态的一阶代数恒等式，
不需要构造全程新 ODE 解。第三式则来自(19)对插值残差的同一线性操作。
在两轴上虽然 $b=0$，$b_\psi$ 仍可非零；(22)中的 $\rho_s/\rho$
正是不可省的相关材料坐标项。

## 5. 分段 PP 的节点项

若 $F,\Theta$ 仅在有限个开放径向区间上满足上述条件，每个区间有独立
的一侧迹，那么以上证明逐区间成立。若额外已经证明整张图为 $C^2$，
它们成为定理1的全局情形。若没有这项证明，不能把各 PP 系数由浮点
Hermite 公式生成当作准确的跨节点 jet 相等。

具体地，在一条固定材料轴上记分点为 $s_0<\cdots<s_N$，并以 PP 节点
取右块值。只要各块到端点有一侧迹，普通微积分逐块相加给
$$
\Gamma(s_N^+)-\Gamma(s_0^+)
=\sum_{k=0}^{N-1}\int_{s_k}^{s_{k+1}}
\partial_s\Gamma_k\,ds
+\sum_{k=1}^{N}[\Gamma]_k,
\quad [\Gamma]_k=\Gamma(s_k^+)-\Gamma(s_k^-).
\tag{24}
$$
若右端选左块值，就删去最后一个 jump。证明只需将每块积分写成
$\Gamma(s_{k+1}^-)-\Gamma(s_k^+)$ 后望远镜求和；它也就是分布导数的
原子部分。更一般的活动角分块须沿真实材料射线使用对应一侧迹。

本文没有把当前 raw CP 的潜在节点 jump 设成零。后续以 shared jets
重新定义的精确 $C^2$ 图是其自身明确对象，须有相应表示转移；不与 raw
PP 自动等同。这是对象范围的说明，不是附加机器精度光滑性门。

## 6. 当前指定 raw CP 入口的有理下界

指定输入为主 M14 成功 CP
`notes/2026-11-10-78718-numerical-m14-restart8000-02.json.gz`，SHA256
`4776c4c251c4bc6fdadda56aaed78f6fc02175483c5ad3a6fb3cf0359a49cd6a`。
其入口值取第一个 PP 块的常数系数，全部 binary 数按准确 dyadic 实数
解释；$a(0)=1$，chart 首值为1，因此 $w(0)=8q_{\rm ref}$。
实际 gauge 和 $q_{\rm ref}$ 都是所保存的 binary $0.1$，不替换为精确
十进 $1/10$。入口使用全部14组模式，(20)–(21)纯属有理运算。

**定理2。** 对这一指定有限表示，
$$
-\frac{134}{10^{10}}<\Gamma(0,0)<-\frac{133}{10^{10}},
\qquad |\Gamma(0,0)|>\frac1{500000000}.
\tag{25}
$$
另一轴满足
$$
0<\Gamma(0,\pi/3)<\frac{51}{10^{12}}.
\tag{26}
$$

**证明。** 代入(20)–(21)的准确有理求和分别给
$$
r_+=-\frac{927670661369091160064173922268431}
{139379657490816363686097257069545386934272},
\tag{27}
$$
$$
r_-=\frac{31911180015152273645848997881247}
{1254416917417347582659885134970977207189504}.
\tag{28}
$$
这些分数只用首块系数，不涉及任何跨节点导数。设 $r=N/D$、$D>0$，
则 $\Gamma=N(N+2D)/D^2$。把(27)代入后，直接整数比较得到
$$
10^{10}N(N+2D)+134D^2>0,\qquad
10^{10}N(N+2D)+133D^2<0.
$$
这证明(25)的两侧有理界，后一个绝对值门随即成立。对(28)，$N>0$，
且 $10^{12}N(N+2D)<51D^2$，给(26)。三角函数在两轴用精确的
$\sin(j\pi)=0$、$\cos(j\pi)=(-1)^j$ 消去；$e_\theta$ 的单位长度
也精确为1，不通过浮点 $\pi$ 或浮点 $\sqrt3$ 求范数。证毕。

式(27)–(28)可用
`scripts/78718-geometry-core-g-transport-v1.py` 的入口 Fraction 分支复算。
该脚本 SHA256 为
`9c4cba0e1b9f60a4d826a26ffc1d59ffaf19a54471abd17aee76cd909e3da77f`；
原端点执行780182自然退出0，其报告
`notes/2026-11-10-78718-geometry-core-g-endpoints-v1.json` 的 SHA256 为
`121b62724cbc3161e36d11f90eac873af7897b8a2c62d1d994aa16314a833d31`。
本文写作时也直接读取这两个已保存分数并以整数比较核对上述界
（实际 bafae2 退出0），未再求解或改变候选。

原脚本自动 `sys.modules` 清单并非未注册动态模块的完整来源列表。
此前已完成的明确21源重放与这一范围订正详见
`notes/2026-11-10-78718-geometry-core-source-and-pp-clarification-v1.md`；
本定理不把原遗漏表述沿用为“所有源都已被原自动清单记录”。

## 7. 对实际研究的范围

定理1说明未经投影的 raw 流保持已有相对角向误差，有限投影与插值残差
怎样给其源项，并完整保留实际 warp 和旋转基。定理2严格定位当前指定
raw CP 入口本身已有大于原 $2\cdot10^{-9}$ 门的误差；它不依赖
原沿程浮点积分或跨节点精确 $C^2$ 假设。

该单点暂不作最终 common map 的对象转移；当前最终图的严格否决已经由
R81另行支付。它也不否定未投影的 support core、其它频率/参数的入口或
正在重求的 M15 曲线。本文不给全域误差界、非线性存在、固定握持比例或
reach。完整浮点沿程分解见原工作笔记及其 PP 范围澄清；同 core 的更高模
入口重投影见 `notes/2026-11-10-78718-geometry-core-reprojection-analysis-v1.md`。

