# 同一材料坐标中的线性时间加密：一致 C² 误差与度量界

## 结论及适用范围

本条给出当前完整相位图的一个**条件明确、可计算常数的时间加密命题**。
它不把新 $\lambda=1$ 场、固定 $g$ 空间精化、全时嵌入或 reach 的尚未返回
结果记成已完成。它也不把已有若干时刻的 `CubicSpline` 诊断升级为连续证书。

设已经选定的完整图为 $X:[0,1]\to C^2(M,\mathbb R^3)$，所有时刻使用同一
材料曲面、同一空间图册、同一 $g$、同一帽及柱参数。若

$$
M_2\ \ge\ \sup_{t\in[0,1]}\|\partial_{tt}X_t\|_{C^2},
$$

则在最大步长为 $h_t$ 的任意时间网格上，逐材料点的**分段线性**插值 $L_hX$
满足

$$
\sup_t\|L_hX_t-X_t\|_{C^2}\le\frac{h_t^2}{8}M_2.                 \tag{1}
$$

此外，令 $A_t=DX_tg^{-1/2}$。若网格端点的相对度量误差至多 $\eta$，且

$$
V_{g,1}\ \ge\ \sup_{p,t}\|\partial_t A_t(p)\|_{\mathrm{op}},
$$

则整个线性插值族满足更直接的界

$$
\big\|(D L_hX)^T(D L_hX)-g\big\|_g
\le \eta+\frac{h_t^2V_{g,1}^2}{4}.                                \tag{2}
$$

这里 $\|B\|_g=\|g^{-1/2}Bg^{-1/2}\|_{\mathrm{op}}$。源中已经付出的
normalized Gram entrywise 上界若更强，可作为这里的 $\eta$；本条没有改变
原数字验收门。式 (2) 只需端点度量界与时间一阶空间一阶界；计算整个空间
$C^2$ 误差的式 (1) 才需要后文的五阶曲线导数。

## 一、Banach 空间插值余项

取固定有限空间图册，各图以固定紧子域覆盖 $M$，定义 $C^2$ 范数为这些子域
上位置、一阶和二阶坐标偏导的最大 Euclidean 范数。极点使用 Cartesian 图，
不用退化的极坐标范数。图册和图间转换在时间上固定。

令 $B=C^2(M,\mathbb R^3)$；假定 $X$ 对时间二次可微为 $B$ 值函数，二阶
导数连续或具有相同本质上界。对一个网格区间 $[a,b]$，记

$$
L_hX(t)=\frac{b-t}{b-a}X(a)+\frac{t-a}{b-a}X(b).
$$

两端为零的二阶边值 Green 核给出

$$
L_hX(t)-X(t)=\int_a^b K_{a,b}(t,s)\,X''(s)\,ds,
$$

其中非负标量核为

$$
K_{a,b}(t,s)=
\begin{cases}
\dfrac{(s-a)(b-t)}{b-a},&a\le s\le t,\\[4pt]
\dfrac{(t-a)(b-s)}{b-a},&t\le s\le b.
\end{cases}
$$

这是 Bochner 积分；同一公式分别适用于所有空间偏导。因此

$$
\|L_hX(t)-X(t)\|_B
\le M_2\int_a^b K_{a,b}(t,s)\,ds
=\frac{(t-a)(b-t)}2M_2\le\frac{(b-a)^2}{8}M_2.
$$

取全部区间的最大值即得 (1)。常数 $1/8$ 对二次标量函数已达到，不能只靠
一般二阶导数假设改小。非均匀网格同样成立。

线性组合保留每个固定空间接缝的完整位置、一阶和二阶共同 jet；它不要求
径向三阶导数存在。$L_hX$ 在时间节点上可以有速度折角，但在时间上连续取值于
$C^2$，正符合本题所需的时间连续性。若材料握持区 $H$ 上所有节点图都逐点
等于 $X_0$，线性插值也在整个 $H$ 上逐点固定。它不是重配准后的坐标比较。

## 二、两种显式相对度量界

### 2.1 从误差的一阶空间导数传递

若原连续族已满足 $\|A_t^TA_t-I\|_{\mathrm{op}}\le\eta$，定义

$$
M_{g,2}\ge\sup_{p,t}\|D\partial_{tt}X_t\,g^{-1/2}\|_{\mathrm{op}},
\qquad e=\frac{h_t^2}{8}M_{g,2}.
$$

由相同 Green 核，$E=D(L_hX-X)g^{-1/2}$ 满足 $\|E\|\le e$。所以

$$
\begin{aligned}
(A+E)^T(A+E)-I
 &=A^TA-I+A^TE+E^TA+E^TE,\\
\|(A+E)^T(A+E)-I\|
 &\le\eta+2\sqrt{1+\eta}\,e+e^2.                    \tag{3}
\end{aligned}
$$

因此对目标 $\tau>\eta$，一个充分条件为

$$
e\le\sqrt{1+\tau}-\sqrt{1+\eta}.
$$

根号须使用严格有理包围或向外区间。直接把近似根号相减的浮点结果当上界不够。

### 2.2 端点 Gram 恒等式

在一个时间区间，记 $u=(t-a)/(b-a)$、$A_0=A_a$、$A_1=A_b$。因 $g$ 不随
时间改变，线性插值的归一切向矩阵恰为

$$
A_h=(1-u)A_0+uA_1.
$$

展开得到精确矩阵恒等式

$$
A_h^TA_h=(1-u)A_0^TA_0+uA_1^TA_1
-u(1-u)(A_1-A_0)^T(A_1-A_0).                         \tag{4}
$$

最后一项负半定，不能遗漏。若两端满足
$(1-\eta)I\preceq A_i^TA_i\preceq(1+\eta)I$，由
$\|A_1-A_0\|\le(b-a)V_{g,1}$ 得

$$
\left(1-\eta-\frac{(b-a)^2V_{g,1}^2}{4}\right)I
\preceq A_h^TA_h\preceq(1+\eta)I.
$$

这证明 (2)。若只要求 $\tau=10^{-6}$，可选

$$
h_t\le\frac{2\sqrt{\tau-\eta}}{V_{g,1}}
\quad(V_{g,1}>0),                                      \tag{5}
$$

并取严格向下舍入的时间步长。$V_{g,1}=0$ 时两端切向矩阵相同，式 (4) 无附加
误差。这是对有限时间离散的可执行误差预算，不是假定时间采样越密就自动通过。

若 (2) 的右端小于 1，还得到每点微分满秩。该条件只给 immersion，不能单独
推出全局嵌入或所需 reach 比例。

## 三、当前完整相位图的时间生成元

下述参数为固定真实数，$\alpha(t)=\Omega t$ 严格仿射。
R87 的显式相位入口选择 $\Omega=4/5$。若以后改非仿射时间函数，必须增加
$\alpha''\partial_\alpha X$，不能照抄本节公式。

记 $Jv=e_z\times v$，$P_h=-J^2$ 是水平投影，$R_\alpha$ 是绕 $z$ 轴转动。
前缀、cut、柱及非平尾在**物理材料角** $\theta$ 中的未握持图为

$$
G_\alpha(r,\theta)=R_\alpha F(r,\theta-\alpha)+c(r)e_z.       \tag{6}
$$

这里 $c(r)e_z$ 代表该块固定竖移；在各内部块上为常量。上下全 $z$ 反射与 $J$
及 $R_\alpha$ 对易，给相同导数界。真实握持框架为

$$
Y_\alpha=R_{-(1-k)\alpha}G_\alpha+O-R_{k\alpha}O.
$$

圆弧中心 $O=\Gamma(L)-k^{-1}e(L)$ 是真实表达式；源码的浮点 `center` 只是其
数值求值。由 (6)，在 active 块上

$$
Y_\alpha=O+R_{k\alpha}\big(F(r,\theta-\alpha)-O\big)+c(r)e_z,
$$

故

$$
\partial_{tt}Y_t
=\Omega^2R_{k\alpha}
\left[k^2J^2(F-O)-2kJ F_\theta+F_{\theta\theta}\right].       \tag{7}
$$

对固定材料空间偏导 $D^\nu$、$|\nu|\le2$，式 (7) 给出

$$
\begin{aligned}
\|D^\nu\partial_{tt}Y_t\|
\le\Omega^2\big(&k^2\|P_hD^\nu F\|
 +2|k|\|P_hD^\nu F_\theta\|
 +\|D^\nu F_{\theta\theta}\|\\
 &+\mathbf1_{\nu=0}k^2|O_h|\big).                          \tag{8}
\end{aligned}
$$

各项取完整材料域和全部相位的严格上界，便得到 (1) 的 $M_2$。对应的一阶
生成元 $\Omega(kJ-\partial_\theta)$ 给 (2) 的 $V_{g,1}$。同一 $g^{-1/2}$ 必须在
真实材料坐标中使用，不能拿相同计算角 $\psi$ 的导数替代。

### 静态 Cartesian 帽无需帽的高阶空间导数

极盘未握持图是 $D(x,y)=(x,y,\pm(Z+f(x,y)))$，不随相位改变。握持后

$$
Y_t=R_{(k-1)\alpha}D+O-R_{k\alpha}O,
$$

于是

$$
Y_{tt}=\Omega^2\left[(k-1)^2R_{(k-1)\alpha}J^2D
-k^2R_{k\alpha}J^2O\right].                            \tag{9}
$$

但 $J^2D=-(x,y,0)$ 恰为仿射函数，因此

$$
D^2Y_{tt}=0.
$$

在半径 $a$ 的 Cartesian 盘上，位置上界为
$\Omega^2((k-1)^2a+k^2|O_h|)$，一阶导数上界为
$\Omega^2(k-1)^2$，二阶项为零。现有帽仅 $C^2$ 的边界正则性已经足够；
不能为了这个时间命题要求帽的四阶导数或偷换帽参数。未握持框架的静态盘
本来就有 $D_{tt}=0$。

## 四、真实材料 chart、所需曲线阶数与完整尾

当前 shared chart 定义

$$
\theta=\psi-\frac{e(s)}3\sin(3\psi),\qquad
\rho=1-e(s)\cos(3\psi)\ge\rho_*>0,
$$

其中 $e$ 是共同径向两 jet 的分段 quintic。物理偏导为

$$
\partial_\theta=\rho^{-1}\partial_\psi,
\qquad
\partial_s\big|_\theta=\partial_s-\frac{\theta_s}{\rho}\partial_\psi. \tag{10}
$$

它们作为同一坐标变换的坐标向量场对易。对 (7) 施加至多两次空间偏导时，
只使用 $e,e',e''$ 与它们的角向导数，不要求 $e'''$。径向 knot 的两侧使用
同一共享两 jet；piece 内可用原有限多项式和严格 Bernstein 上界。$\rho_*$
必须取真实共享 chart 的正有理下界，不能取采样最小值。

各块所需数据如下。

| 完整块 | (1) 所需最高材料角数据 | 现有来源与尚待的工作 |
|---|---|---|
| 基础 Fourier/Hermite 前缀 | 所有原模、径向阶数至多 2、角阶数至多 4 | 保存的完整系数可直接支付；禁止只取入口模 |
| exact-core lift | $\Gamma$ 至第 4 阶 | 现有真实 core oracle 已提供至第 4 阶 |
| 中心 Cartesian 两 jet 修补 | 一般需要 $\Gamma$ 第 5 阶 | 修补的角向系数含 $b(\psi)\Gamma'(\theta_0(\psi))$，四次角导数会出现 $\Gamma^{(5)}$ |
| cut Hermite 修补 | 完整 union Fourier 的角阶数至 4 | 当前 `cut_angular_tables` 只存阶数 0、1、2、3；可由原全模直接求阶数 4，不能称旧表已包含 |
| 正短柱 | $\Gamma$ 至第 4 阶 | 所有竖向参数导数显式；同一实际 core |
| 所有有限尾段及 deep collar | 原全部 Fourier 模、径向两 jet、角阶数至 4 | 同一全局 mean 与全部共享节点；只需有限系数，不需新 native 积分 |
| 静态帽与极点 | 帽现有 $C^2$，时间项用 (9) | 不需要帽四阶导数；必须使用 Cartesian 图 |

`MetricAngularRanges` 的现有 `range(4)` 是**阶数 0 至 3**，其真实 core
输入为 $\Gamma,\ldots,\Gamma^{(4)}$。这足以支持多种 $C^1$ 时间误差界，
却不等于已经付过 (1) 的完整 $M_2$。中心项一般非零，不能以只看中心端点的
消去关系把所需阶数降成 4。

尾的水平复 Fourier 模 $m$ 在握持框架有时间权重 $(k-m)^2$，高度模有权重
$m^2$；再施加空间角导数即可得到完整有限和上界。near-cut 的真实
$r=r(R)$ 只扰动有限系数时，要保留 $r',r''$ 链式因子。固定背景及其真实积分
本身不随相位改变，水平圆背景的转动和角平移按 (7) 精确合并。

原 `ActualFiniteTailV2.fourier` 的高度分支只供阶数 0、1、2 使用；它的其他
分支不能直接当作第 3、4 阶导数。原 cut 表已经显式绕开此限制。新的严格界
可直接用完整保存模的 $(im)^j$ 或正余弦四周期公式；不修改冻结的低阶求值器，
不截去全局 mean 或任何保存模。

## 五、不依赖新高阶反演积分的有理五阶曲线界

下面给出原 R53、无额外 supported-phase control 的完整粗界。它既证明所需
常数有限，也给实际场返回后可直接用有限字面输入计算的办法。

设原支撑函数曲率半径为

$$
\rho_0(\varphi)=1+\sum_j b_j\cos(m_j\varphi),
\quad b_j=(1-m_j^2)a_j,\quad
B_j=\sum_\ell |b_\ell|\,|m_\ell|^j,
\quad r=1-B_0>0.
$$

所有 $a_j$ 取冻结字面实数。以弧长材料变量 $u$ 表示的原曲率
$q_0=1/\rho_0(\varphi(u))$ 满足

$$
\begin{aligned}
q_0'&=-\frac{\rho_0'}{\rho_0^3},\\
q_0''&=-\frac{\rho_0''}{\rho_0^4}
       +\frac{3(\rho_0')^2}{\rho_0^5},\\
q_0'''&=-\frac{\rho_0'''}{\rho_0^5}
       +\frac{10\rho_0'\rho_0''}{\rho_0^6}
       -\frac{15(\rho_0')^3}{\rho_0^7}.
\end{aligned}                                                    \tag{11}
$$

右侧的 $\rho_0$ 导数均对 $\varphi$；式 (11) 每次使用
$\partial_u=\rho_0^{-1}\partial_\varphi$。因此可取

$$
\begin{aligned}
Q_0&=r^{-1}, & Q_1&=B_1r^{-3},\\
Q_2&=B_2r^{-4}+3B_1^2r^{-5},
&Q_3&=B_3r^{-5}+10B_1B_2r^{-6}+15B_1^3r^{-7}.
\end{aligned}                                                    \tag{12}
$$

记原 nonic 窗口为 $W$、过渡宽为 $b>0$。在窗口外导数为零；在过渡区，
由 $0\le t(1-t)\le1/4$ 直接得到全域有理界

$$
|W'|\le W_1=\frac{630}{256b},\quad
|W''|\le W_2=\frac{2520}{64b^2},\quad
|W'''|\le W_3=\frac{2205}{4b^3}.                         \tag{13}
$$

最后一式来自

$$
W'''=\frac{\pm\big[7560t^2(1-t)^2(1-2t)^2
-5040t^3(1-t)^3\big]}{b^3}.
$$

原窗口的端点导数匹配保证这些界跨 piece 成立。令 $|\beta|\le B_\beta$ 是
真实归一化常数的严格上界。原公式为

$$
\kappa=(1-\lambda(1-W))q_0+\lambda(1-W)k+\lambda\beta W,
\qquad 0\le\lambda\le1.
$$

取 $G=Q_0+k+B_\beta$，下式均为有理上界：

$$
\begin{aligned}
K_0&=\max(Q_0,k)+\lambda B_\beta,\\
K_1&=Q_1+\lambda W_1G,\\
K_2&=Q_2+2\lambda W_1Q_1+\lambda W_2G,\\
K_3&=Q_3+3\lambda W_1Q_2+3\lambda W_2Q_1+\lambda W_3G.
\end{aligned}                                                    \tag{14}
$$

例如 $D=S+b/2$、$L=\pi/3$，取已证明的有理 $L_*\le L$ 且 $D<L_*$。
原归一化积分给出一个无需数值积分的选择

$$
B_\beta=
\frac{D}{L_*-D}
\max\left(\left|k-\frac1{1+B_0}\right|,
          \left|k-\frac1{1-B_0}\right|\right).                  \tag{15}
$$

这里用了 $\int_0^L(1-W)\,du=D$ 以及 $q_0$ 的严格上下界。
当冻结输入满足 $D<1$ 时，可直接用 $L_*=1$，因为 $\pi>3$。更紧的已验证
beta 区间也可代替 (15)，但不得代入未经包围的浮点 beta。

令 $n=e(\varphi)$、$T=e_\perp(\varphi)$，有 $\Gamma'=T$、$n'=\kappa T$、
$T'=-\kappa n$。逐次微分得到

$$
\begin{aligned}
\Gamma^{(4)}&=(\kappa^3-\kappa'')n-3\kappa\kappa'T,\\
\Gamma^{(5)}&=(6\kappa^2\kappa'-\kappa''')n
 +(\kappa^4-4\kappa\kappa''-3(\kappa')^2)T.
\end{aligned}                                                    \tag{16}
$$

因 $|n|=|T|=1$，一个完整可计算界为

$$
\boxed{\quad
|\Gamma^{(5)}|\le
6K_0^2K_1+K_3+K_0^4+4K_0K_2+3K_1^2.
\quad}                                                          \tag{17}
$$

这里 $K_0^4$ 是四次幂，不是四阶曲率导数。更低各阶可取
$|\Gamma'|=1$、$|\Gamma''|\le K_0$、
$|\Gamma'''|\le K_1+K_0^2$、
$|\Gamma^{(4)}|\le K_0^3+K_2+3K_0K_1$。
位置与圆心仍沿真实 primitive／实际 normalization 的来源支付，不能从只给
导数的 (17) 擅自选取位置常数。

式 (11)–(17) 使用全部原支撑系数。若以后增加非零 supported-phase control，
必须另付其所需三阶曲率项；本条不覆盖那种变更。当前实际 R53 oracle 以零
control 包装原 core，这没有给源图添加控制。

## 六、怎样接入固定 g 的空间与时间联合加密

若某条已经真实建立的同 $g$ 空间精化序列 $X^{(n)}$ 满足

$$
\sup_t\|X^{(n+1)}_t-X^{(n)}_t\|_{C^2}\le d_n,
$$

且第 $n$ 个时间网格的 $\epsilon_n=h_n^2M_{2,n}/8$，则

$$
\sup_t\|L_{h_{n+1}}X^{(n+1)}_t-L_{h_n}X^{(n)}_t\|_{C^2}
\le d_n+\epsilon_n+\epsilon_{n+1}.                         \tag{18}
$$

若原空间序列已是 $C^2$ Cauchy 且 $\epsilon_n\to0$，插值序列收敛到同一个
极限。不能仅因为 $h_n\to0$ 就略过可能随 $n$ 增长的 $M_{2,n}$；应选择
$h_n^2M_{2,n}\to0$。对度量可独立用 (2)，在真实空间误差 $\eta_n$ 下降时选择
$h_n^2V_{g,1,n}^2\to0$。时间加密不会去掉一个固定有限场本身的空间误差底数。

实际节点求值若还有严格的 $C^2$ 误差 $\xi_n$，线性插值的凸权重只再增加
$\xi_n$；它也应另付，不得把导出的有限精度网格视为精确节点图。

固定空间接缝和握持区由线性组合保持，时间节点上的端点见证也原样保留。
全域嵌入、reach 的量化余量仍须由真实完整图证书或另一个严格扰动传递支付。
式 (1)–(18) 没有宣布这些未付门通过。

## 源码核对和执行状态

同名 JSON 逐文件绑定本次只读核对的来源和 SHA，核心来源为：

- `finite_closure/m3_m8_closed_map/closed_m3_map.py`：真实物理角相位、全尾和
  静态 Cartesian 盘的定义。
- 同目录 `phase_angle_chart.py`：共享两 jet chart、严格 $\rho_*$ 和物理角反演。
- `resume_20261128/tail/actual_cartesian_prefix.py`：完整 exact-core lift 及
  `center_delta` 的 $b\Gamma'$ 项。
- `resume_20261128/geometry/cartesian_prefix_metric_tables.py` 和
  `cartesian_prefix_cut_metric.py`：现有阶数 0–3 的真实角表及全部 cut 模。
- `resume_20261128/analytic/material_circle_phase_contract.py`：仿射相位、真实
  圆心表达式和握持刚体框架。
- `resume_20261128/analytic/qr_fixed_actual_closed_map.py`：实际 own-fixed 来源
  门后的原完整闭图构造；本条不改变其源门或帽参数。
- `resume_m3/r53_validated_material_core.py` 与
  `resume_20261126/warm_phase_validated_core.py`：原支撑半径、真实曲率与 nonic
  窗口；后者提供适用于完整 R53 参数范围的零 control 包装。

本条没有启动低 $\lambda$ 计算、积分、新 J、native 请求或数值插值探针。
五阶界、Green 核和 Gram 恒等式均由本页推导；尚未把任何真实新 $\lambda=1$
固定场代入取得 $M_2,V_{g,1}$ 的最终数值。

独立小源码 `resume_20261128/tail/verify_linear_time_c2_algebra.py` 实际执行了
20 项精确符号恒等式检查，全部返回通过：Peano 核积分与 $1/8$、完整 Gram
恒等式、支撑曲率至三阶材料导数、nonic 窗口及端点四 jet、完整混合曲率三阶
导数、曲线四／五阶导数、Cartesian 盘的仿射水平生成元。使用整数／有理
符号运算，没有加载一个几何场或构造假阳性样例。标量执行回执在
`held10-tail-preparation/linear-time-c2-lemma-20261128/algebra.json`，SHA256 为
`0cd5a13340e351dcc7e9abda106c642a20a740924413da2e630ea672ca56c6ec`。
重复检查可用一个新的 scratch 输出文件：

```bash
python topics/visible-flex-held-10pct/scripts/resume_20261128/tail/verify_linear_time_c2_algebra.py \
  --out "$NEW_ALGEBRA_RECEIPT"
```

符号检查核对本条等式；非负核、矩阵范数方向、窗口粗界及真实场范围仍由正文
的完整证明负责。该回执明确不宣称已支付实际时间常数、全图 metric、嵌入或 reach。
