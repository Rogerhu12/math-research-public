# R30：源切口到真实 Cartesian 边界迹与星形外延

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

状态：**已证明，条件坐标工具**。本结果给出完整切口两 jet 的坐标转换、半周对称下的精确位置闭合、凸性及 R27 所需的实际极角导数。存在一个实际尾部图、其径向方程与精确源度量相容、内 cuff 可填平盘，仍是独立条件。保存响应的有限角采样不因此成为精确闭合或整尾 reach 证书。

使用 [R19](R19-all-angle-cut-and-complete-jet-correction.md) 的完整角平均根可以支付本文的一个精确转角条件；使用 [R27](R27-explicit-star-shaped-graph-extension.md) 的外延和 [R25](R25-entire-graph-curvature-and-reach.md) 的整图定理时，还须逐项支付各自的输入。

## 1. 两种半径和完整输入

源坐标为 $(r,\theta)$，源度量为

$$
g=E(r)\,dr^2+r^2\,d\theta^2.
\tag{30.1}
$$

固定切口 $r=r_0>0$。以下公式中的 $r,E,E'$ 均表示切口处的值。完整高度数据写为

$$
H(\theta)=h(r_0,\theta),\qquad
P(\theta)=h_r(r_0,\theta),\qquad
Q(\theta)=h_{rr}(r_0,\theta).
\tag{30.2}
$$

$P,Q$ **包括完整均值项**。高度的常数项只改变垂直平移；$P,Q$ 的均值不能通过平移删除。本文使用 $\rho$ 表示水平 Cartesian 平面中的实际极径，$\varphi$ 表示实际极角。一般有 $r\ne\rho$、$\theta\ne\varphi$、$P\ne f_\rho$、$Q\ne f_{\rho\rho}$。

假设

$$
a^2:=r^2-H_\theta^2>0,\qquad
n_z^2:=1-\frac{P^2}{E}-\frac{H_\theta^2}{r^2}>0.
\tag{30.3}
$$

定义

$$
D:=\sqrt{Ea^2-r^2P^2}=\sqrt E\,r n_z,
\qquad b=-\frac{PH_\theta}{a},\qquad c=-\frac D a.
\tag{30.4}
$$

选择水平单位切向 $t=(\cos\gamma,\sin\gamma)$ 和左法向 $n=Jt$。该符号约定使圆的 $t=e_\theta,n=-e_r$；背景水平径向导数指向外侧。水平映射 $X$ 的一阶 jet 为

$$
X_\theta=at,\qquad X_r=bt+cn.
\tag{30.5}
$$

直接计算得到 $\langle X_i,X_j\rangle=g_{ij}-h_i h_j$，而

$$
\det(X_r,X_\theta)=-ac=D>0.
\tag{30.6}
$$

这也证明水平局部坐标非退化。对全体高度 jet 同时作垂直反射不会改变 $a,b,c,D$ 或水平曲线。它不同于只翻转某一个 Fourier 系数或额外改变相位。

## 2. 切向转角、精确闭合和严格凸性

由 $X_{r\theta}=X_{\theta r}$ 的切向分量，得

$$
\Gamma:=\gamma_\theta
=\frac{b_\theta-a_r}{c}
=\frac{1+PrH_{\theta\theta}/a^2}{\sqrt E\,n_z}.
\tag{30.7}
$$

这里

$$
a_r=\frac{r-H_\theta P_\theta}{a},\qquad
a_\theta=-\frac{H_\theta H_{\theta\theta}}a.
\tag{30.8}
$$

式 (30.7) 可逐项验证：

$$
b_\theta-a_r=-\frac ra-\frac{Pr^2H_{\theta\theta}}{a^3}.
$$

给定初始切向角和水平平移以后，

$$
\gamma(\theta)=\gamma(0)+\int_0^\theta\Gamma(s)\,ds,
\qquad
X(\theta)=X(0)+\int_0^\theta a(s)t(s)\,ds.
\tag{30.9}
$$

一般必须分别验证转角和位置周期：

$$
\int_0^{2\pi}\Gamma\,d\theta=2\pi,
\qquad
\int_0^{2\pi}at\,d\theta=0.
\tag{30.10}
$$

**半周闭合引理。** 若 $H,P$ 为 $\pi$ 周期函数，且 (30.10) 的第一个等式精确成立，则第二个等式精确成立。此时 $X$ 关于

$$
C=\frac{X(\theta)+X(\theta+\pi)}2
\tag{30.11}
$$

中心对称，右侧与 $\theta$ 无关。

**证明。** $a,\Gamma$ 均为 $\pi$ 周期。任意半周的转角积分均为 $\pi$，所以 $t(\theta+\pi)=-t(\theta)$、$X_\theta(\theta+\pi)=-X_\theta(\theta)$。积分给出位置闭合；对 (30.11) 求导即知其为常量。高度本身也周期，故完整空间切口同时闭合。$\square$

这说明偶物理 Fourier 模态允许省去一个独立的平移周期方程；它**不**允许把数值转角残差小于容差当作精确转角方程。

**凸性引理。** 再假设 $\Gamma>0$，则上述闭曲线是严格凸的正向简单曲线，$C$ 位于其内部，从 $C$ 出发的极角为严格递增坐标。

**证明。** 从任意 $\theta_0$ 起，令其切向和左法向为 $t_0,n_0$。沿一整周考察

$$
q(\theta)=(X(\theta)-X(\theta_0))\cdot n_0,
\qquad q'=a\sin(\gamma-\gamma(\theta_0)).
$$

由于切向角严格增大一整周，$q$ 在前半转角区间严格增加，在后半转角区间严格减少，且始末均为零；中间严格为正。因此每条切线均为严格支撑线。任意非同一参数的两个曲线点不可能重合，否则违反其中一条严格支撑线。每个方向的支撑点唯一，所以该简单闭曲线界定严格凸域。中心对称给出 $C$ 为任意一对对径点的中点；上述严格支撑关系说明它严格位于所有支撑线的内侧，故在域内。于是任意从 $C$ 出发的射线只交边界一次，且

$$
\det(X-C,X_\theta)>0.
\tag{30.12}
$$

这也直接证明实际极角严格递增。$\square$

### 2.1 完整 mean 根的接口

固定 $H$ 和 $P$ 的非均值项，只变动 $P\mapsto P+s$。令

$$
\Delta=E-P^2-EH_\theta^2/r^2.
$$

对 (30.7) 精确微分，得到

$$
\frac{\partial\Gamma}{\partial s}\bigg|_{s=0}
=\frac{P+EH_{\theta\theta}/r}{\Delta^{3/2}}.
\tag{30.13}
$$

若该分子在一个 $s$ 区间内有严格正下界，完整转角平均对 $s$ 严格递增。R19 的有理级数包络及根区间给出该区间中唯一的精确根。取该根以后才能使用半周闭合引理；R19 的完整 $Q$ 修正同时支付切口 Darboux 相容条件。这个单 cut 修正不证明径向轨道或深尾匹配。

## 3. 完整水平二阶 jet

除 (30.8) 外，定义

$$
\begin{aligned}
D_r&=\frac{E'a^2+E(2r-2H_\theta P_\theta)-2rP^2-2r^2PQ}{2D},\\
D_\theta&=-\frac{EH_\theta H_{\theta\theta}+r^2PP_\theta}{D},\\
b_r&=-\frac{QH_\theta+PP_\theta}{a}
       +\frac{PH_\theta a_r}{a^2},\\
c_r&=-\frac{D_r}{a}+\frac{Da_r}{a^2},\qquad
c_\theta=-\frac{D_\theta}{a}+\frac{Da_\theta}{a^2},\\
\gamma_r&=\frac{b\Gamma+c_\theta}{a}.
\end{aligned}
\tag{30.14}
$$

则

$$
\begin{aligned}
X_{\theta\theta}&=a_\theta t+a\Gamma n,\\
X_{r\theta}&=a_rt+a\gamma_r n,\\
X_{rr}&=(b_r-c\gamma_r)t+(b\gamma_r+c_r)n.
\end{aligned}
\tag{30.15}
$$

**证明。** (30.14) 的前四式是 (30.4) 的逐项微分，$a_r$ 使用 $h_{r\theta}=P_\theta$。对 (30.5) 求导并使用 $t_\theta=\Gamma n,n_\theta=-\Gamma t$。混合导数的法向分量给出最后一式，径向微分则给出 $X_{rr}$。这些公式也与平面度量 $g-dh^2$ 的 Christoffel 公式一致。$\square$

它们是一个实际等距图存在时必有的两 jet；对任意离散数据套入这些式子，并不产生已经解出的径向等距邻域。

## 4. 实际径向一、二阶高度迹

令 $Y=X-C$、$\rho=|Y|$、$e_\rho=Y/\rho$。记

$$
e_t=e_\rho\cdot t,\qquad e_n=e_\rho\cdot n,
\qquad
\xi=\frac{e_n}{c},\qquad
\eta=\frac{e_t-b\xi}{a}.
\tag{30.16}
$$

则 $e_\rho=\xi X_r+\eta X_\theta$。在实际 Cartesian 图 $z=f(x,y)$ 中，水平梯度的切法分量为

$$
q_t=\frac{H_\theta}{a},\qquad
q_n=\frac{P-bq_t}{c},\qquad q=q_tt+q_nn.
\tag{30.17}
$$

完整 Cartesian 径向迹为

$$
a_0=H,\qquad a_1=f_\rho=P\xi+H_\theta\eta.
\tag{30.18}
$$

定义对称矩阵

$$
K_{rr}=Q-q\cdot X_{rr},\quad
K_{r\theta}=P_\theta-q\cdot X_{r\theta},\quad
K_{\theta\theta}=H_{\theta\theta}-q\cdot X_{\theta\theta}.
\tag{30.19}
$$

则

$$
a_2=f_{\rho\rho}
=K_{rr}\xi^2+2K_{r\theta}\xi\eta+K_{\theta\theta}\eta^2.
\tag{30.20}
$$

**证明。** 由 $h=f\circ X$，一阶链式法则给出 (30.17) 和 (30.18)。再微分得

$$
h_{ij}=\operatorname{Hess}_{xy}f[X_i,X_j]+q\cdot X_{ij}.
$$

若 $J=(X_r,X_\theta)$，便有

$$
\operatorname{Hess}_{xy}f=J^{-T}KJ^{-1}.
\tag{30.21}
$$

沿固定实际极角的射线，$e_\rho$ 不变，二阶径向导数为该 Hessian 在 $e_\rho$ 上的二次型，得到 (30.20)。$\square$

## 5. 实际极角的全部链式导数

令

$$
k:=\varphi_\theta=\frac{\det(Y,X_\theta)}{\rho^2}>0.
\tag{30.22}
$$

直接微分得到

$$
\begin{aligned}
\rho_\theta&=\frac{Y\cdot X_\theta}{\rho},\\
\rho_{\theta\theta}&=
\frac{|X_\theta|^2+Y\cdot X_{\theta\theta}}{\rho}
-\frac{(Y\cdot X_\theta)^2}{\rho^3},\\
k_\theta&=
\frac{\det(Y,X_{\theta\theta})}{\rho^2}
-2\frac{\det(Y,X_\theta)(Y\cdot X_\theta)}{\rho^4}.
\end{aligned}
\tag{30.23}
$$

把星形边界写成 $\rho=R(\varphi)$，则

$$
R_\varphi=\frac{\rho_\theta}{k},\qquad
R_{\varphi\varphi}
=\frac{\rho_{\theta\theta}k-\rho_\theta k_\theta}{k^3}.
\tag{30.24}
$$

任一径向迹 $a_j$ 同样满足

$$
(a_j)_\varphi=\frac{(a_j)_\theta}{k},\qquad
(a_j)_{\varphi\varphi}
=\frac{(a_j)_{\theta\theta}k-(a_j)_\theta k_\theta}{k^3}.
\tag{30.25}
$$

例如，若已知连续界 $k\ge k_*>0$、$|k_\theta|\le k_1$，则

$$
\|(a_j)_\varphi\|_\infty
\le\frac{\|(a_j)_\theta\|_\infty}{k_*},\qquad
\|(a_j)_{\varphi\varphi}\|_\infty
\le\frac{\|(a_j)_{\theta\theta}\|_\infty}{k_*^2}
+\frac{\|(a_j)_\theta\|_\infty k_1}{k_*^3}.
\tag{30.26}
$$

这给出 R27 的 $U_j,V_j,W_j$，(30.24) 给出其中的 $\rho_1,\rho_2$。必须对实际中心 $C$ 的水平曲线给出 $R_*>0$，不能用源切口半径直接替换。

为使三个径向迹都属于 $C^2(S^1)$，足够假设 $H\in C^4$、$P\in C^3$、$Q\in C^2$，以及 (30.3)、(30.10)、$\Gamma>0$。因为 (30.9) 给出的边界至少 $C^4$，(30.14)–(30.20) 的分母有正下界，所得 $a_0,a_1,a_2$ 至少 $C^2$。一般 $C^2$ 曲面不能自动保证这些更高的切口正则性；R27 中的额外假设仍保留。

## 6. 无角网格的近圆位置包络

下面给出一个可以接入有理区间计算的连续位置界。假设第 2 节的精确闭合及半周对称成立，并已证明

$$
|a-r|\le\varepsilon_a,\qquad
|\Gamma-1|\le\varepsilon_\Gamma.
\tag{30.27}
$$

通过整体水平旋转取 $\gamma(0)=\pi/2$，置 $\delta(\theta)=\gamma(\theta)-\theta-\pi/2$。由于 $\delta$ 是 $\pi$ 周期且 $\delta(0)=\delta(\pi)=0$，

$$
|\delta|\le\varepsilon_\delta:=\frac\pi2\varepsilon_\Gamma.
\tag{30.28}
$$

由 (30.11) 得精确恒等式

$$
Y(\theta)=-\frac12\int_\theta^{\theta+\pi}a(s)t(s)\,ds.
\tag{30.29}
$$

和圆的同式比较，使用 $|t-e_\theta|\le|\delta|$，得

$$
|Y-re_r|\le\varepsilon_Y
:=\frac\pi2(\varepsilon_a+r\varepsilon_\delta).
\tag{30.30}
$$

因此在随切口转动的正交标架中，

$$
|Y\cdot t|\le\varepsilon_t:=\varepsilon_Y+r\varepsilon_\delta,
\qquad
|Y\cdot n+r|\le\varepsilon_n
:=\varepsilon_Y+\frac r2\varepsilon_\delta^2.
\tag{30.31}
$$

第二式使用 $1-\cos\delta\le\delta^2/2$。令 $Y_t=Y\cdot t,Y_n=Y\cdot n$，还有精确导数关系

$$
\begin{aligned}
Y_t'&=a+\Gamma Y_n,&Y_n'&=-\Gamma Y_t,\\
Y_t''&=a_\theta+\Gamma_\theta Y_n-\Gamma^2Y_t,
&Y_n''&=-\Gamma_\theta Y_t-\Gamma(a+\Gamma Y_n).
\end{aligned}
\tag{30.32}
$$

将 (30.31) 与这些关系、(30.14)–(30.25) 一起作有理外向区间运算，即可包围全部实际极角 trace；不需要以角网格代替连续界。若使用 $\pi<22/7$，(30.28)–(30.31) 的位置误差上界也全部可以取有理数。

## 7. 已存实际 M16 响应的诊断与范围

输入为已正式成功的

`notes/2026-11-12-root-vu032-q085-actual-resumable-m16-tail-response_0003.json.gz`，

SHA256 `671f4921924995e7c4ec4f2cc5807c127d6fc67364b7d79f8023a58ca84dfd7c`。完整尾残差为 $4.249050468400791\times10^{-11}$。工具 `computations/tail_cartesian_cut_traces.py` 只读取该已存包，不构建尾工厂、不重求 BVP、不修改 mean、不把转角或位置投影到闭合条件。

输出 `notes/2026-11-12-tail-r30-actual-m16-cartesian-cut.json` 保存 512/1024 两档诊断。下表是 1024 档的有限采样结果，**均不是连续几何界**：

| 量 | 数值 |
|---|---:|
| $\Gamma$ 范围 | $[0.9999973732964639,1.0000024939771943]$ |
| 水平位置周期误差 | $3.103\times10^{-16}$ 以下 |
| 实际水平半径范围 | $[0.2999997409606593,0.3000002530465354]$ |
| $\|R_\varphi\|,\|R_{\varphi\varphi}\|$ | $5.123\times10^{-7},1.048\times10^{-6}$ 以下 |
| $\|a_0\|,\|(a_0)_\varphi\|,\|(a_0)_{\varphi\varphi}\|$ | $2.169\times10^{-5},4.334\times10^{-5},8.695\times10^{-5}$ 以下 |
| $\|a_1-w\|,\|(a_1)_\varphi\|,\|(a_1)_{\varphi\varphi}\|$ | $2.592\times10^{-4},5.172\times10^{-4},1.041\times10^{-3}$ 以下 |
| $\|a_2-w_r\|,\|(a_2)_\varphi\|,\|(a_2)_{\varphi\varphi}\|$ | $8.748\times10^{-4},1.738\times10^{-3},3.713\times10^{-3}$ 以下 |
| 切口 $\max|\kappa|$ | $1.849640894137708$ |
| R27 外环界表达式，代入上述采样值 | $1.954423713$ 以下 |

这里 $w=0.08000000000000027$、$w_r=-1.866666666666673$，但求值始终使用完整 $P$ 均值 $0.08000019102494224$ 与完整 $Q$ 均值 $-1.8666594182889793$。两档浮点转角误差均舍入为零；这并未支付精确转角条件。

工具还用精确二进制有理 Fourier 系数的 $\ell^1$ 范数，证明该**表示数据模型**在所有角上的 $n_z^2>0.9935996764354$、$P+EH_{\theta\theta}/r>0.0794512256350$、转角分子 $>0.9999767403808$。这些正性界不认证源 profile 的实数求值误差，也不把有限频谱声明为精确全频解。

复算入口：

```bash
python computations/tail_cartesian_cut_traces.py \
  --response notes/2026-11-12-root-vu032-q085-actual-resumable-m16-tail-response_0003.json.gz \
  --out notes/2026-11-12-tail-r30-actual-m16-cartesian-cut.json \
  --angular 512 1024
```

## 8. 对整尾与 reach 的准确用途

若后续得到真实尾部 Cartesian 图、其精确闭合切口满足上面的连续 trace 盒，R27 即给出保持该边界全部两 jet 的外延。若内 cuff 的实际 Cartesian 高度、梯度、Hessian 也精确趋于平盘的 jet，则可连同平盘得到完整有限图，再接上述外延为整平面图。此时取内部主曲率界与外环曲率界的最大值，R25 才能给出全图 reach 以及图内所有点对的法向弦界。

当前仍须支付的输入是：精确源度量与全频径向尾、真实内 cuff、整尾投影为图及其连续主曲率界、与其余闭曲面部分的跨块点对。本文没有用切口的约 $1.85$ 曲率代替这些输入，也没有把局部 mean/second 修正宣称为已解出的全径向等距轨道。

## 9. 已证明的 M16 邻近闭合切口及外环支付

本节加强第 7 节的采样诊断：对同一个输入的 **direct_stored_jet 实数对象**，已经用无角采样的有理运算构造邻近的精确闭合切口，并支付一组真正 Cartesian 的 R27 数据盒。这里固定的 $r,E,E'$ 是保存字段的精确二进制有理值；不是未经包围的源函数精确值。原响应完全不修改。

### 9.1 完整 mean 根和实角二阶修正

R19 原工具的精确输出为
[全角 cut 包络](../notes/2026-11-12-tail-r30-actual-m16-exact-cut.json)。
对直接保存对象，完整转角平均误差满足

$$
4.079835803371566\times10^{-17}
<\Phi<
4.079859733472560\times10^{-17}.
\tag{30.33}
$$

上下十进制端点在此向外取整；判定依据是 JSON 中的准确分数。特别地，原始切口的完整转角误差**不是零**，虽然第 7 节浮点求积舍入为零。

R19 的单调根论证给出唯一完整 mean 根 $s_*$，满足

$$
|s_*|<4.081604\times10^{-15}.
\tag{30.34}
$$

保留 $H$ 和 $P$ 的非均值项，取 $P_{\rm ex}=P+s_*$。再按 R19 的全角 Darboux 公式定义完整 $Q_{\rm ex}$。为核销 R27 的 $C^2$ 正则性和导数界，不必支付宽度 $\log2$ 的解析条带。

具体地，沿用 R19 记号，令

$$
B=P+EH_{\theta\theta}/r,\qquad
J=Q-E'H_{\theta\theta}/(2r),\qquad
A=F+s_*J.
$$

则

$$
Q_{\rm ex}-Q=-\frac{A}{B+s_*}.
\tag{30.35}
$$

设 $|s_*|\le\eta$，已知 $B-\eta\ge b_*>0$，并用完整有限 Laurent 系数的 $\ell^1$ 范数取

$$
A_j=\|F^{(j)}\|_0+\eta\|J^{(j)}\|_0,\qquad
B_j=\|B^{(j)}\|_0,\quad j=0,1,2.
$$

商的两次微分和三角不等式严格给出

$$
\begin{aligned}
\|Q_{\rm ex}-Q\|_\infty
&\le A_0/b_*,\\
\|(Q_{\rm ex}-Q)_\theta\|_\infty
&\le A_1/b_*+A_0B_1/b_*^2,\\
\|(Q_{\rm ex}-Q)_{\theta\theta}\|_\infty
&\le A_2/b_*+2A_1B_1/b_*^2
+A_0B_2/b_*^2+2A_0B_1^2/b_*^3.
\end{aligned}
\tag{30.36}
$$

本输入的准确计算证明 $b_*>0.0799658210540$，并分别得到上界

$$
1.295809\times10^{-11},\qquad
4.374024\times10^{-10},\qquad
1.487446\times10^{-8}.
\tag{30.37}
$$

该修正保留其全部频率，没有把 $Q_{\rm ex}$ 截断为 16 模。因为实角分母严格为正，$Q_{\rm ex}$ 在实圆上光滑。旧 cut 工具的固定 $\log2$ 权分母在本输入上约为 $-0.6333$，所以其专用于该条带的 correction.exists 标志为 false；本节使用 (30.36) 的实角 $C^2$ 论证，不引用失败的条带门，也不据该门失败判断实角修正不存在。

### 9.2 连续 Cartesian 盒

计算工具为 [tail_cartesian_cut_interval.py](../computations/tail_cartesian_cut_interval.py)，输出为
[连续 Cartesian 包络](../notes/2026-11-12-tail-r30-actual-m16-cartesian-enclosure.json)。
它对每个输入导数使用有限 Fourier 的准确 $\ell^1$ 上界，把未知 $s_*$ 及 (30.37) 的全部修正纳入区间。第 6 节以 $\pi<22/7$ 包住中心化位置，而非数值积分位置。随后依 (30.14)–(30.25) 传播二阶 Taylor jet 的有理区间。

每次加减乘除均向外舍入到 $2^{-160}$ 的整数倍；平方根下端点由整数平方根向下取整，上端点再加一单位。对于 $\theta$ Taylor 系数，乘法用有限卷积，倒数和平方根用恒等式逐阶递推。其包含性由阶数归纳和区间四则运算直接成立。没有使用任何角网格、FFT 误差估计或浮点比较来决定下列不等式。

得到的连续几何界包括

$$
\begin{aligned}
0.9999561954405&<\Gamma<1.0000439035563,\\
n_z^2&>0.9935996764354,\\
0.9996746663339&<\varphi_\theta<1.0003254513215,\\
0.2999674602234&<\rho<0.3000325397756.
\end{aligned}
\tag{30.38}
$$

$\Gamma>0$ 与完整 mean 根使第 2 节的精确闭合、严格凸性和中心星形性全部适用。对真实 $\varphi$ 导数，得到如下向外显示的连续界：

| 迹或边界 | 零阶偏离 | 一阶实际极角导数 | 二阶实际极角导数 |
|---|---:|---:|---:|
| $a_0$，参考常数 $0$ | $2.168524\times10^{-5}$ | $4.341835\times10^{-5}$ | $8.708012\times10^{-5}$ |
| $a_1$，参考常数 $w$ | $2.765856\times10^{-4}$ | $5.475834\times10^{-4}$ | $1.067742\times10^{-3}$ |
| $a_2$，参考常数 $w_r$ | $1.721275\times10^{-3}$ | $3.171463\times10^{-3}$ | $4.978088\times10^{-3}$ |
| $R$ | 下界见 (30.38) | $5.327106\times10^{-5}$ | $4.585533\times10^{-5}$ |

因此以下更简单的**准确有理盒**已得到支付：

$$
\begin{gathered}
R_*=\frac{299}{1000},\qquad L=\frac1{10},\qquad
\rho_1=\frac{54}{10^6},\quad \rho_2=\frac{46}{10^6},\\
(U_0,U_1,U_2)=\frac1{10^6}(22,44,88),\\
(V_0,V_1,V_2)=\frac1{10^5}(28,55,107),\\
(W_0,W_1,W_2)=\frac1{10^5}(173,318,500).
\end{gathered}
\tag{30.39}
$$

参考常数严格取原保存的二进制 $c_0=0,c_1=w,c_2=w_r$；完整 $P,Q_{\rm ex}$ 的均值仍在实际迹中，未用 $w,w_r$ 替换。数据盒见
[certified-r27-box.json](../notes/2026-11-12-tail-r30-actual-m16-certified-r27-box.json)。

这些迹确实可作为完整 Cartesian 两 jet 使用。首先 $q\cdot X_\theta=H_\theta$ 及 $q\cdot e_\rho=a_1$ 唯一确定边界梯度。其次，对 $q\cdot X_r=P_{\rm ex}$ 和 $q\cdot X_\theta=H_\theta$ 求 $\theta$ 导数，由 (30.15) 得

$$
q_\theta=\bigl(J^{-T}KJ^{-1}\bigr)X_\theta.
$$

由边界 trace 构造的图具有相同梯度沿边界的导数；(30.20) 还指定其 Hessian 在 $e_\rho$ 方向的二次型。因为 $e_\rho$ 与 $X_\theta$ 线性独立，这些条件唯一决定对称 $2\times2$ Hessian，所以其完整两 jet 就是 (30.17)、(30.21)。这一步不假设尚未构造的径向等距邻域。

### 9.3 外环曲率结论及保留的缺口

R27 的显式 Hermite 外延可直接应用于上述闭合星形曲线及三个 $C^2$ 迹，构造其外侧环带的图，并在更外侧接为常值。准确有理计算为
[extension-bound.json](../notes/2026-11-12-tail-r30-actual-m16-extension-bound.json)，给出

$$
|\kappa_{\rm ext}|
\le
\frac{1233160395408603650737015639}
     {629103609822733926400000000}
<1.960186488<2.
\tag{30.40}
$$

这里已经支付的是**邻近精确闭合切口的实际 Cartesian 外环**。它是 reach 论证的辅助延拓，不是声称该外环满足原径向等距度量。

若将来实际内部尾图的边界两 jet 与此切口吻合，且内部主曲率 $\le33/4$、内 cuff 确实填为平盘，则 R25 给出的辅助整图 reach 为至少 $4/33$。JSON 中该内部界及 reach 字段始终标为条件量。本节没有支付这些内部条件，也不把单 cut 修正接回实际径向尾或 $g_{\rm root}$。

可复算的三个入口依次是：原 R19 cut 包络工具；本节 Cartesian 有理区间工具，输入上述 cut 报告及 (30.39) 的盒；R27 有理外延界工具。全部文件保存输入和脚本哈希。此次 R19 两种算术层合计约 48 秒、峰值 14 MB；Cartesian 区间计算约 0.5 秒、峰值 14 MB，均已正常结束，没有启动新的尾部求解。
