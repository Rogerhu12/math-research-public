# R171：准确径向相位积分、物理 bumps 与单侧 Arb jet 的完整消费者

## 1. 结论和范围

本结果为 [R136](R136-peak-spacer-prefix-continuous-radius-and-outer-design-domain.md) 的准确标量度量定义提供完整、可重读的一维区间消费者。对冻结候选及实际保存的七个物理径向参数，消费者包围

$$
a_\delta,\quad (a_\delta)_s,\quad (a_\delta)_{ss},\quad
(a_\delta)_{sss},\quad
c_\delta=\frac{(a_\delta)_s}{a_\delta},\quad
K_\delta=-\frac{(a_\delta)_{ss}}{a_\delta},\quad (K_\delta)_s.
$$

前三项属于同一准确 $C^2$ 半径函数；第三径向导数及 $K_s$ 按显式分片取单侧值或所列单侧的并包。没有增加全局 $C^3$ 假设，也不把相位积分的近似多项式另立为目标度量。

准确输入是 [cyl032 candidate](../notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json)，SHA256

`7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1`。

本次实际外参数及保存网格来自第 27 轮不可变接受态 [grouped27 accepted](../notes/2026-11-12-fd2d-raw-bump-grouped27-trial-back00-a01-accepted.npz)，SHA256

`2b65810c5c09985d54544e6ca697ee609f066a17ecbce4b83e89adad0b52ae6f`。

该包有 131 个保存节点、31 个中央参数、16 个独立尾参数和 7 个径向参数。本消费者只读网格、七个径向参数及其支持、候选身份；不求解 F/J、BVP、标架、位置图或全局几何。有限场的其余列保持原字节。

主实现为 [fd2d_gc_r136_arb_profile.py](../scripts/fd2d_gc_r136_arb_profile.py)，SHA256

`7bcc33f75b3c3264934110c71c549e18d7ad92cb2681a317980e3844c72323c6`。

实际生成器为 [fd2d-metric-r136-profile-packet.py](../scripts/fd2d-metric-r136-profile-packet.py)，SHA256

`b4aea52fa04314064d37e6b1f556f38a4c8ab5c8ec947696281f1cdd0b7d83d5`。

## 2. 同一个目标准确定义

### 2.1 固定几何常数和共享 Hermite 片

中央尺度为 R136 所定义的椭圆周长尺度

$$
a_0=\frac{2(7/5)}{\pi}\,\mathrm E\!\left(1-\frac{(1/2)^2}{(7/5)^2}\right).
$$

使用 [已发布矩区间包](../notes/2026-11-12-fd2d-balanced-moments-taylor-01.json) 中的准确 dyadic 端点。R136 的 [半径证书 v2](../notes/2026-11-12-fd2d-peak-spacer34-radius-certificate-02.json) 绑定相同候选及该 $a_0$ 输入，并已证明基准全域 $a\ge4/5$。消费者核对这两个身份及证书的成功状态。矩包整体中一项未达到额外显示精度偏好的标志，不否定其中已经支付余项的 $a_0$ 区间。

除 $7/5,1/2,4/5,-\pi/2$ 和 R136 已明定的 ramp 比例 $2/25,23/25$ 外，raw 输入的有限数采用其 binary64 字节所代表的准确有理数。特别是冻结 outward spacer 不是重新优化出的长度。

每个正长度 $L$ 的 Hermite 片用同一组左右两 jet

$$
(d_0,v_0,b_0),\qquad(d_1,v_1,b_1)
$$

定义唯一五次多项式 $d(t)$，$t\in[0,1]$，满足 $d,d_t/L,d_{tt}/L^2$ 的这六个端值，半径为 $a_0+d$。相邻共享数据逐项相等。实现直接由这些有理数构造多项式，不把浮点重建系数当作另一套输入。命名端点的前两阶 jet 直接返回共享定义；第三导仍由实际多项式的单侧导数给出。

### 2.2 相位片和导出的深 coast 长度

每个相位片以准确物理起点 $S_i$、正长度 $L_i$ 及归一变量 $t=(s-S_i)/L_i$ 定义

$$
a(s)=a(S_i)+L_i\int_0^t\sin\phi_i(v)\,dv.
$$

第一相位是准确 $\arcsin v_*$。`start_from_previous` 采用前片的准确终相位；`start_second_from_previous` 采用前片准确加速度除以当前相位余弦。由 R136 的已验证相位域，该分母为正。

令 $\epsilon=2/25$，$A=23/25=1-\epsilon$。soft-turn 的归一累积轮廓明确为

$$
I(t)=\begin{cases}
t^3/\epsilon^2-t^4/(2\epsilon^3),&0\le t\le\epsilon,\\
t-\epsilon/2,&\epsilon\le t\le1-\epsilon,\\
A-(1-t)^3/\epsilon^2+(1-t)^4/(2\epsilon^3),&1-\epsilon\le t\le1.
\end{cases}
$$

相位为 $\phi=p_0+(p_1-p_0)I/A$；`length_from_turn_rate` 的长度是准确 $|p_1-p_0|/(K A)$。相位三次桥用其端相位及物理端导数定义；coast 相位常数。每个 turn 在准确的 $\epsilon,1-\epsilon$ 处分片后积分。

最终相位端值采用候选明示的准确 $-\pi/2$，不采用该数的浮点近似作为定义。令 $I_b$ 为最后 brake 的准确半径积分，$A_d$ 为进入深 coast 的准确半径，$p_d<0$ 为其准确常相位。深 coast 定义为

$$
L_d=\frac{4/5-I_b-A_d}{\sin p_d}.
$$

R136 已证明其正性；当前更紧的区间也直接得到严格正长。故最终准确满足 $a=4/5$。总物理长度 $S$ 是所有准确长度之和，而不是运行时 `Candidate.end` 的舍入数。

## 3. Taylor 积分及余项证明

考虑一片归一子区间 $[l,r]$。置

$$
t=c+h y,\qquad c=(l+r)/2,\quad h=(r-l)/2,\quad -1\le y\le1,
$$

并把准确相位写成

$$
\phi(c+h y)=\phi_c+\Delta(y),\qquad \Delta(0)=0.
$$

若 $\Delta(y)=\sum_{j\ge1}d_j y^j$，则

$$
|\Delta(y)|\le D:=\sum_{j\ge1}|d_j|.
$$

所有相位系数及 $\phi_c$ 都由包含准确值的 Arb 球包围。系数间依赖可以丢失而扩大包围，不能因此缩小真实范围。对任意实 $x$，正弦的各阶导数绝对值不超过 $1$，故 $N$ 阶 Taylor 多项式

$$
P_N(y)=\sum_{k=0}^{N}
\frac{\sin^{(k)}(\phi_c)}{k!}\,\Delta(y)^k
$$

满足完整连续余项界

$$
|\sin\phi(c+h y)-P_N(y)|
\le\varepsilon_N:=\frac{D^{N+1}}{(N+1)!},\qquad |y|\le1.
$$

这里四周期导数 $\sin,\cos,-\sin,-\cos$ 各自用区间值包围。积分多项式按每项准确原函数构造，再平移常数，使其在 $y=-1$ 准确为零。任意部分原函数的归一误差由

$$
\left|\int_l^t(\sin\phi-P_N)\,dv\right|
\le(r-l)\varepsilon_N
$$

包围；乘以物理长度 $L_i$ 就是半径误差。全子片积分可利用奇次幂在 $[-1,1]$ 上积分为零，但仍支付相同均匀余项。各片起始半径、后续深 coast 长度及其物理端点继承之前全部误差包。

因此保存的是“准确相位积分的多项式包围与显式余项”，不是把 $P_N$ 积分所得函数指定为 $a$。特别地，下一节的真导数没有通过对半径余项区间求导取得。

本次 $N=24$、Arb 中点精度 256 位，14 个相位分支的最大单分支物理半径余项严格小于

$$
1.299\times10^{-31}.
$$

其完整 dyadic 端点在报告中，显示小数不是定义数据。

## 4. 真导数、连续接缝和第三导的作用域

在一个相位解析分片内部，微积分基本定理给出

$$
a_s=\sin\phi,\qquad
a_{ss}=\cos\phi\,\phi_s,\qquad
a_{sss}=\cos\phi\,\phi_{ss}-\sin\phi\,(\phi_s)^2.
$$

这些是第 2 节同一个准确积分函数的导数。多项式 $\phi,\phi_s,\phi_{ss}$ 在所求区间用 Bernstein 系数包围；正弦余弦及四则运算继续外包。Hermite 片的各导数则来自同一个准确五次多项式。

相邻 Hermite 片共享两 jet；Hermite 末速度通过准确 asin 接入相位，且该末加速度为零；相位桥传递同一相位和物理相位导数。soft-turn 的端相位导数为零，coast 的相位导数恒零。因此所有 raw 接缝上的 $(a,a_s,a_{ss})$ 共同，构成准确 $C^2$ 函数。程序保存每个连接所用的具体恒等式，并检查左右包没有与该恒等式矛盾。

不要求左右 $a_{sss}$ 相等。`interface_jets(i)` 返回第 $i$ 个界面的左右值及明确的 `common_third_jet_claimed=false`。跨界面求盒时并包所有可能涉及的单侧。对 R119/R125 的分片积分和 R153 的实际需要，第三导只在其被消费的相位/Hermite片内部提供；没有把这一接口转成新的全局正则性门。

最终 brake 上 $\phi\to-\pi/2$ 且 $\phi_s\to0$，$\phi_{ss}$ 有限。因此准确 cut 左侧满足

$$
(a,a_s,a_{ss},a_{sss})=(4/5,-1,0,0).
$$

这是半径函数的结论。它**不**推出 R155 正 trace 修正的 $E_s=0$，也不赋予未知第二基本形式一个未定义的 cut 径向 jet。两种对象在报告中明确分开。

## 5. 当前七个物理 bumps 与同一固定度量

从输入 NPZ 的显式布局读取中央 $[0,31)$、尾 $[31,47)$、径向 $[47,54)$。支持端点与七个 $\delta_j$ 均按保存字节的准确 dyadic 值定义。在 $[L_j,R_j]$ 上令

$$
q_j=\frac{s-L_j}{R_j-L_j},\qquad
\psi_j(s)=1024q_j^5(1-q_j)^5,
$$

支持外为零。因两端有五重零点，$\psi_j\in C^4$。真实参数化是

$$
a_\delta(s)=a(s)+\sum_{j=1}^7\delta_j\psi_j(s).
$$

消费者用乘积法则计算前四项 jet，不改变支持、系数、物理坐标或目标度量。对零阶范围，直接用 $q(1-q)$ 的准确二次极值包围，保留 $0\le\psi_j\le1$；更高导数使用有限乘积公式。支持跨界面的部分显式并入零值。

由 R136 的准确全域下界，

$$
a_\delta(s)\ge\frac45+\sum_j\min(\delta_j,0).
$$

本次输入的右端是准确有理数

$$
\frac{8652411935637125253}{11529215046068469760}
=0.7504771054285823810199584915636705773067660629749298095703125>0.
$$

这是充分的全连续正下界，不是采样最小值。全部支持均避开准确中央柱和准确 cut 的邻域，故两处保护 jet 不变。对任何已经严格包住的局部盒，四则运算给出

$$
c_\delta=\frac{a_s}{a},\qquad
K_\delta=-\frac{a_{ss}}a,\qquad
(K_\delta)_s=-\frac{a_{sss}}a+\frac{a_{ss}a_s}{a^2}.
$$

宽盒的导数区间可能很粗；它们表示有效外包，不表示真实极值很大。后续可在实际残差盒所需宽度直接调用同一消费者，不需要重求候选或更改 $g$。

## 6. 准确物理点、命名分片和可重读包

`piece_box(i,t0,t1)` 的输入是第 $i$ 个准确物理片的归一闭区间。它自动支付准确长度和起点的不确定包；端点单侧由片名决定。

`physical_box(s0,s1,side=...)` 的输入是准确有理物理坐标区间，不能用浮点片编号假定其隶属关系。对每个可能相交的准确片，计算

$$
t\in\frac{[s_0,s_1]-S_i}{L_i}\cap[0,1],
$$

并并包全部可能的片。准确有理界面可按显式左右侧选择；超越端点仍未分开的盒保留两侧。固定物理区间必须被证明位于准确域内。`endpoint_jets()` 另以准确终点标签提供 cut，避免把 `Candidate.end` 的二进制数推广为准确 $S$。

每个区间的存储都是准确 dyadic 上下端点。读包先设置声明精度，再恢复区间。`from_packet(path,expected_sha256=...)` 核对实际包 SHA、原区间源 SHA、输入及物理参数的内容绑定。数学身份使用输入字节、源、精度和明确参数，不依赖搬迁后的绝对路径。

采用的 Arb 球语义、端点外取整和中点精度控制见 [python-flint 0.9.0 官方 arb 文档](https://python-flint.readthedocs.io/en/latest/arb.html)。包围半径的有限实现精度可能略扩大 hull；例如宽盒的显示下端会略低于已知 $4/5$，不会推翻独立准确下界或形成缩小包围。

## 7. 旧 runtime 的真实关系及未付项目

本轮绑定链是 `IndependentTailPositiveTraceNativeField` 的物理 profile、`RadialBumpProfile`、再到 `fd2d_frozen_ellipse_candidate.Candidate.profile`。源码中后者以每相位分支的 40 点浮点 Gauss 求半径，同时用 $\sin\phi,\cos\phi\,\phi_s$ 报导数。`Candidate.linear_piece` 的 ODE 求解是另一入口，本链没有调用；这里没有 profile ODE 的 dense 插值可供误差转移。

因此不能把“浮点积分程序对输入坐标的导数”与这些报告导数默认为同一函数。准确目标已由 R136 的积分定义确定，本消费者直接包围它。实际保存网格前 130 个节点上的旧输出被当作具体 binary64 数，在**同一准确物理点**减去上述包围。这支付这些有限值的实际误差，不声称为所有可能浮点调用建立了全程序舍入定理。

最后一个保存数另作 endpoint 标签，报告同时保留准确 $S$、标签差及成对 cut jet 差，明确不声称这是同一物理点。

由此，后续连续后验可以直接用本包的准确 $a,a_s,a_{ss},K$，不必先证明旧 Gauss 程序所有调用。但若要迁移既有浮点 frame/body 观测，仍须显式计入实际重建误差。准确 $S$ 与旧保存末点间的极小区间也需由明确有限场定义或显式端点坐标衔接覆盖；本结果没有暗改旧 P1 场、atlas 或 cut 标签，也没有把该缺口藏进零误差。

## 8. 精确删柱平移

设 $0\le d<C$，其中 $C$ 为准确初始常半径柱长。删去 $d$ 的柱段并以新物理坐标 $\tilde s$ 表示时，定义

$$
\widetilde a_\delta(\tilde s)=a_\delta(\tilde s+d),\qquad
0\le\tilde s\le S-d.
$$

这直接保留全部已有导数公式、正下界及片侧语义；每个 bump 的支持也随同一个复合平移。新的准确 cut 是父准确 cut 标签减 $d$，而不是旧浮点末点减去另一个舍入数。实现 `shifted(Fraction(7,50))` 已保存这一准确复合，并在少量实际有理点核实与父查询相同。

它是父定义域的限制再平移，不声称删柱后仍与未删柱的原定义域相同。R168 的几何预算仍对该新闭曲面支付。

## 9. 实际闭存结果

真实执行 `87589 / 3ee9be → f951e0` 自然退出 $0$，消费者自身计时 $1.933955775002687$ 秒、最大 RSS $90720$ KiB。见 [完整报告](../notes/2026-11-12-fd2d-metric-r136-arb-profile-01-report.json) 与 [完成回执](../notes/2026-11-12-fd2d-metric-r136-arb-profile-01-completion-receipt.json)。覆盖 61 个 raw 片、14 个相位积分分支和 60 个共享两 jet 界面。

准确总长的完整 dyadic 区间宽为 $2.617\times10^{-31}$ 以下，其包含值显示为

$$
S\approx1.4889731783581300000441758523227.
$$

它比本次旧保存末点标签大

$$
1.1873403225247744\times10^{-15}
\;<\; S-S_{\rm label}\;<\;
1.1873403225247747\times10^{-15}.
$$

130 个同物理点的实际有限误差外包为：

| 量 | 最大绝对误差的严格简洁外包 |
| --- | ---: |
| $a$ | $1.178\times10^{-15}$ |
| $a_s$ | $2.855\times10^{-15}$ |
| $a_{ss}$ | $7.814\times10^{-12}$ |
| $c$ | $2.545\times10^{-15}$ |
| $K$ | $6.964\times10^{-12}$ |

这些只是所列实际有限输出与准确目标之差；不从表推出连续曲面误差通过。

完整可重读标量包为 [profile packet](../notes/2026-11-12-fd2d-metric-r136-arb-profile-01-packet.json.gz)，381511 字节，SHA256

`7bedd394db9ab0fc3b1d3186c49225ae8f7765ca6d28a80560aeb8842a26ee7c`。

实际有限比较保存在 [queries packet](../notes/2026-11-12-fd2d-metric-r136-arb-profile-01-queries.json.gz)。可重做命令和准确接口见 [消费说明](../notes/2026-11-12-fd2d-metric-r136-arb-profile.md)。全部已闭文件及依赖以该说明所连 manifest 为准。

## 10. 接入 R119/R125 的实际剩余范围

本结果完整支付径向目标这一块。把返回的四个半径 jet 交给已闭 `ProfileBox`，可直接提供当前场的 $c,K,K_s$。R125 的零端 primitive 恒等式以及移动材料角的 $U_s/U_\xi$ 项保持原式；本结果没有删除它们。

完整当前 affine lifting、冻结参考函数及 ruling atlas 的连续值/角 jet 包仍须与同一个实际有限场绑定。R153 分母 $n$ 的连续正性、R155 cut 退化处的实际作用域、真正的初始相容缺陷、primitive 余项和完整闭曲面几何也不会由本一维报告自动获得。这些是原任务剩余构造数据；没有增加独立审核或更高正则性条件。
