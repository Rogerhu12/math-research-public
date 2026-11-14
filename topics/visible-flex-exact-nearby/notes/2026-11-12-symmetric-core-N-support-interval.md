# 原 step02 显式对称图：连续核心 N 与支撑区间

状态：**已完成 $|x|\le.25$、全部实角的有限有向证书：
$N_{\rm raw}<0$、$N<0$、正支撑 $h$ 与正归一化支撑 $\zeta$。**
对象是原 `type_fixed_step02.npz` 的显式对称无限角 R33 图，不是
D5/D8 参数点。174 个正侧闭 span 全部通过，未启用额外细分，
相邻端点逐位相等，左右反射覆盖整个核心。

| 连续量 | 全 $|x|\le.25$ 的已付界 |
|---|---:|
| $N_{\rm raw}$ | $<-.3916395581808441$ |
| $N=N_{\rm raw}/A$ | $<-.3186311822179974$ |
| $h=F\cdot\nu$ | $>.8068876494914060$ |
| $\zeta=h/|F|$ | $>.6886454097622460$ |
| $A=|F_\theta\times F_x|$ | $<1.412032504135112$ |
| $|F|$ | $<1.178935968710474$ |
| $|F_x|$ | $<1.289289077626495$ |

配合前一标量证书，同一区间还有 $A>.8496004112349936$ 和
$Q=F_z/x>.9447694241408142$。上表的 $h$ 下界也给出同样的
$|F|$ 正下界。因此 $\partial_\theta\log Q-
\partial_\theta\log|F|$ 在腰圈没有来自对数或除零的障碍；此结论
不假设原始二进制输入精确反射。

## 1. 四个符号分别定义

令 $X=F_x$、$F_\theta=aT$，选外向法向

$$
\nu=\frac{F_\theta\times F_x}{|F_\theta\times F_x|},\qquad
A=|F_\theta\times F_x|.
$$

本文分别认证

$$
\begin{aligned}
N_{\rm raw}&=F_{\theta\theta}\cdot(F_\theta\times F_x)
          =-a^2X\cdot(T\times T_\theta),\\
N&=F_{\theta\theta}\cdot\nu=N_{\rm raw}/A,\\
h&=F\cdot\nu,\\
\zeta&=\frac{F\cdot\nu}{|F|}=h/|F|.
\end{aligned}
$$

$h$ 是长度量，$\zeta$ 是无量纲正夹角因子；二者不共用同一个字段
或同一个下界。报告中分别使用 `raw_N_upper`、
`normalized_N_upper`、`support_lower`、`zeta_lower`。

输入 SHA256 为
`bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532`，
来自原 checkpoint SHA256
`05d3e59cf338c5d2a2bde13aad7bf1d4e5247c326efb46b3148793e75a7ea883`。
对物理加权相位和实际半径取 $a,\beta$ 偶部、$Z,\gamma$ 奇部。
$Z$ 由冻结 slope 精确积分；此实现重新用有向 B-spline 反导控制递推
构造积分，再取 $(P(x)-P(-x))/2$，所以任意积分常数精确消掉。
没有使用原浮点 primitive 与 slope 精确相等这一错误假设。
没有 Gaussian 卷积，也没有把约 $10^{-15}$ 的 knots 反射缺陷置零。

## 2. 径向闭区间覆盖

合并所有原始和精确反射 knots，并加入 $0$、$.25$，得到正侧
174 个闭区间；每对邻区间共用同一个二进制实数端点，没有遗漏 knots。
当前输入的核心内全部原始内 knots 都是简单 knots。标量 spline
本身至少 $C^4$，本证书使用的 $F,F_x$ 在这些端点具有唯一连续值。

对每一原 spline 和每一闭区间，程序用**有理数精确中点**定位其
多项式 span。即使相邻 knots 只差一个浮点单位，中点不是浮点数，
也不会误选到相邻 span。随后用有向 de Boor 包住该有理中点的全部
多项式 Taylor 系数，并以完整有限 Taylor 展开包住整个闭区间。
原 phase、反射 phase、base、mean、saved radius shift、高度 slope
全部纳入；物理权重 $a_{\rm base}^3$、$a_{\rm base}^2$ 在求 jet 时
也逐项计费。

正侧通过后，负侧由**所定义对象的精确偶奇性**推出。具体地
$F_h$ 偶、$F_z$ 奇，所以上述 $A,N_{\rm raw},h,\zeta$ 都是偶函数。
这不借用原 checkpoint 的近似反射。

## 3. 无限角原函数和有向节点值

每个径向闭区间先在 256 个 quarter-angle 节点上对真
$T,T_x$ 作有向三角求值，再用直接区间和计算 DCT/DST。
没有调用浮点 FFT。三角端点沿用 root 证书的 Machin $\pi$ 区间、
32 阶实 Taylor 及严格 Lagrange 余项。

保留柱坐标 $4j$、$j\le127$ 后，对应完整 1024 点笛卡尔 DFT 的
$|n|\le509$ 截断。R33 复角 strip 的真 $T,T_x$ 范数和几何级数
同时支付截断与 alias；这些上界在整个径向闭区间有效。$F,F_x$ 的
每个有限值在形成叉积、点积**之前**都加上无限原函数尾区间。

用于 $N_{\rm raw}$ 的 $T_\theta$ 直接来自真有限相位的三角组成，
而不是把截断 primitive 的二阶导数无误差地当成真 $aT_\theta$。
在柱坐标中它准确等于

$$
\begin{pmatrix}
\sin\gamma\,\gamma_\theta\sin\beta-
 \cos\gamma\cos\beta(1+\beta_\theta)\\
-\sin\gamma\,\gamma_\theta\cos\beta-
 \cos\gamma\sin\beta(1+\beta_\theta)\\
\cos\gamma\,\gamma_\theta
\end{pmatrix}.
$$

## 4. 4096 个角节点之间如何计费

每个 quarter-circle 有 4096 个有向节点，任何实角到最近节点的距离
不超过

$$
\delta_\theta=\frac\pi{4\cdot4096}
 < .0001917475984857052.
$$

设相位系数绝对和给出的界为 $M_{T_x}$、$M_{T_\theta}$、
$M_{T_{\theta\theta}}$。明确可取

$$
\begin{aligned}
M_{T_x}&=B_x+G_x,\\
M_{T_\theta}&=1+B_\theta+G_\theta,\\
M_{T_{\theta\theta}}&=B_{\theta\theta}+G_{\theta\theta}
 +(1+B_\theta+G_\theta)^2,
\end{aligned}
$$

其中角导数的系数权为 $4j$ 或 $(4j)^2$，每次正和、正乘法都向上
舍入。由真无限原函数恒等式 $F_\theta=aT$、
$F_{x\theta}=a'T+aT_x$，节点向量范数加
$a_+\delta_\theta$ 或 $(|a'|_++a_+M_{T_x})\delta_\theta$，
分别给出整角 $M_F,M_X$。

节点向量范数的平方逐项向上计算。平方根函数只提出候选端点，
程序随后将其平方与输入上界作**精确有理数比较**，必要时向上移动
一个浮点数，直到端点被证明是上界。因此平方根库值并非未经验证的
证书端点。

记 $W=T\times X$、$J=aF\cdot W$。由于 $T$ 是真单位向量，

$$
\begin{aligned}
|\partial_\theta N_{\rm raw}|
&\le a_+^2(a_+M_{T_x}M_{T_\theta}+M_XM_{T_{\theta\theta}}),\\
|\partial_\theta J|
&\le a_+M_F(M_{T_\theta}M_X+a_+M_{T_x}),\\
|\partial_\theta W|
&\le M_{T_\theta}M_X+a_+M_{T_x}.
\end{aligned}
$$

每个节点的有向 $N_{\rm raw}$ 上界、$J$ 下界再分别加、减这些
Lipschitz 上界乘 $\delta_\theta$，才成为全角界。面积上界用
$a_+\min(M_X,M_W)$，其中 $M_W$ 同样由节点叉积范数加上述 gap 预算
获得。最后逐个径向区间取

$$
N\le\frac{N_{{\rm raw},+}}{A_+}<0,
\qquad h\ge\frac{J_-}{A_+}>0,
\qquad\zeta\ge\frac{J_-}{A_+M_F}>0.
$$

面积的独立正下界 $.8496004112349936$ 已由
`2026-11-12-symmetric-core-scalar-gates.md` 对同一输入和同一核心支付；
$J_->0$ 自身也保证此处叉积与 $F$ 都不为零。

## 5. 精确重放入口与范围

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_core_interval.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz \
  --core .25 --quarter-nodes 256 --angular-nodes 4096 \
  --out /tmp/visible-core-N-support.json
```

每 10 个径向区间及每次未通过时写入可恢复 JSON；`--resume` 读取
原进度。恢复前应核对报告中全部依赖 hash，源和输入 hash 则由程序
直接检查。永久 JSON 同时保留全部已通过 cell 的区间值、无限尾、
Lipschitz 常数和节点间余量。重放时计时字段会不同，不作为数值证明
输入。

永久文件为
`data/phase_ring_continuation/type_fixed_step02_core_interval.json`
（202529 bytes），SHA256
`36a83e821e7ca2572fdc95378d688505c1fee788b633e7f0195ff61ecf35eeac`。
源 `scripts/fourfold_phase_core_interval.py` 的 SHA256 是
`f489e86dadf7d013d5044fa3b7588b9699268f2db3923d80419a811cb077b40b`。
完整跑174个span约198秒；报告记录所有依赖hash，不需要重做Newton。

全核心最大的无限原函数误差是
$\|\delta F\|<3.232\cdot10^{-16}$、
$\|\delta F_x\|<2.888\cdot10^{-14}$。最大的额外角 gap 补偿是
$N_{\rm raw}$ 的 .075178 和 $J$ 的 .002334；这些补偿已经从符号
余量中扣除，不能再把节点值的较好余量当成全角结果。
六个代表半径（含0、实际root附近、.25）另外用独立
`SymmetricFrozenGeometry` 浮点评估检查方向、积分高度和数值范围；
全部落入对应证书界。这只是实现交叉检查，连续结论来自上述有向
覆盖而非浮点样本。

范围是这个显式对称图的 $|x|\le.25$，包括已付 target 根
$t\in[.2383698,.2383701]$ 和半径 $1/4096$ 的实 collar。
它证明单个二型系数不退化和正支撑，不证明实际 Gaussian 曲率只有
两次变号，不覆盖外部 caps，不解径向等距残差，不构造闭合等距族。
所有 D5/D8 参数点都必须使用各自快照另算。
