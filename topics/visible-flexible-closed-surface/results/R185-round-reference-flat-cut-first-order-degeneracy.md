# R185：固定平坦切口旁圆基准的有界一阶退化

2026-11-12，Astra-visible-flex-fd2d / constructive_geometry。

**状态：以下限域命题已证明。** 它适用于 R181 的 B32 圆基准，也适用于具有同一种正二次末相位制动的圆基准。它不证明有限幅非圆解不存在，不排除边界层或不在闭域连续二基本形式拓扑中可微的分支，也不停止实际 gap $.05$ 的有限幅求解。本文没有运行新的 BVP。

## 1. 对象、假设与结论

采用实际材料角 $u\in\mathbb R/(2\pi\mathbb Z)$，物理子午弧长 $s\in[0,S]$，三场顺序为 $(n,m,l)$。基准度量和基准第二基本形式为

$$
g_0=ds^2+a(s)^2du^2,\qquad
S_0=(n_0,0,l_0)=\left(\frac{\cos\phi}{a},0,-\phi_s\right),
\qquad a_s=\sin\phi .
\tag{1}
$$

R181 已证明 $a\ge a_c=4/5$，且 $n_0>0$ 在 $s<S$。中央是准确圆柱，半径固定为 $a_0$；切口满足 $(a,a_s,a_{ss})=(a_c,-1,0)$，$S_0(S,u)=0$。完整圆参考和不除未知 $n$ 的增量方程见 [R166](R166-exact-round-prefix-and-complete-increment-equations.md)，新物理 B32 定义见 [R181](R181-shorter-phase-prefixes-and-an-explicit-variable-cut-budget.md)。

记 $\tau=S-s$。末段是准确 cubic smoothstep 相位桥，长度 $L>0$，起相位 $-p_d$，$0<p_d<\pi/2$，两端相位导数均为零。B32 的 $L$ 是候选记录的准确 binary64 $.026$，$p_d$ 是准确 binary64 $1.45$。令 $d=\pi/2-p_d>0$，则

$$
\phi(S-\tau)=-\frac{\pi}{2}
 +d\left(3\frac{\tau^2}{L^2}-2\frac{\tau^3}{L^3}\right).
\tag{2}
$$

考虑一侧或两侧参数族 $t\mapsto (a_t,S_t)$，满足：

1. 每个 $g_t=ds^2+a_t(s)^2du^2$ 仍为轴对称度量，中央 $a_0$ 与物理端点 $S$ 固定；在某个固定末邻域内 $a_t=a$。这包含七个紧支径向 bump 的当前外设计。
2. $a_t$ 在 $t=0$ 对参数可微，足以微分 $a_t,a_t',a_t''$；$S_t$ 在闭前缀的 $C^0$ 范数中可微。记其导数为 $(\dot n,\dot m,\dot l)$，因此它们在闭域有界、连续。
3. 每个 $S_t$ 满足完整 Gauss–Codazzi。若第二基本形式仅连续，Codazzi 可按分布意义理解；下文 Fourier 系数的连续右端会在每个内部紧区间给出通常的常微分方程，不额外要求曲面为 $C^3$。
4. 中央为闭合、定向一致的凸平面曲线沿准确圆柱方向挤出，材料周长固定为 $2\pi a_0$；实际 gap 是其中心对齐的两轴支持差。固定刚体规范不是额外几何约束。
5. 切口的完整三场等于 R128/R132/R170 实际 flat-tail 端口，且基准尾控制为零。特别地，对实际曲率函数 $\kappa_t$，切口三场为

$$
(n_t,m_t,l_t)(S,u)=
\kappa_t(a_c\sin u)
(\cos^2u,-\sin u\cos u,\sin^2u).
\tag{3}
$$

固定初始相位的刚体旋转只改变角原点；在零曲率基准上，一阶结论不受其可微变化影响。

**定理。** 在这些明确假设下：

- 实际尾的一阶曲率 $\dot\kappa$ 恒零；若用固定有限 Bernstein 多项式参数化，全部尾控制的一阶导数也为零。
- $(\dot n,\dot m,\dot l)$ 的每个非零材料角 Fourier 模在整个前缀恒零。轴对称 $\dot a$ 可以强迫零模，但不能强迫这些非零模。
- 中央曲率的一阶变化恒零，中央曲线的一阶变化至多是刚体运动，故

$$
\frac{d}{dt}\operatorname{gap}(t)\bigg|_{t=0}=0.
\tag{4}
$$

所以不能在圆点直接假设一条以 gap 本身为参数、且在闭前缀 $C^0$ 第二基本形式中可微的精确分支。这个结论只排除该可微参数化，不给局部或全局非圆解的不存在定理。

## 2. 准确末段因子，及真正有界的剩余系数

令 $A=3d/L^2$、$B=2d/L^3$。由 (2) 准确有

$$
l_0=2A\tau-3B\tau^2,\qquad
n_0=\frac{\sin(A\tau^2-B\tau^3)}{a(S-\tau)}.
\tag{5}
$$

同时 $a_\tau=\cos(A\tau^2-B\tau^3)$，$a(0)=a_c$。在足够小但固定的 $0\le\tau\le\tau_0<L/2$ 上，全部这些函数实解析，$a\ge a_c$，$l_0>0$。定义

$$
q(\tau)=\frac{n_0}{l_0}=\tau Q(\tau),\qquad
c(\tau)=\frac{a_s}{a}.
\tag{6}
$$

式 (5) 中相消 $\tau$ 后，$Q$ 在闭区间实解析且正，并准确满足

$$
Q(0)=\frac1{2a_c},\qquad c(0)=-\frac1{a_c}.
\tag{7}
$$

这里后续不用形式渐近余项作为证明。取 $Q_*=\min_{[0,\tau_0]}Q>0$。对任意固定整数波数 $\nu>0$，定义以下闭区间连续函数：

$$
r(\tau)=
\frac{(c(\tau)+2Q(\tau))/\tau+c(\tau)Q(\tau)-Q'(\tau)}{Q(\tau)},
\tag{8}
$$

$$
h_\nu(\tau)=
\nu\,\frac{1/(a(\tau)Q(\tau))-2}{\tau}.
\tag{9}
$$

$\tau=0$ 的值按连续延拓定义。(7) 使两个商的分子在零点准确为零；例如
$(c+2Q)/\tau=\int_0^1(c'+2Q')(\theta\tau)d\theta$。因此这些确为有界系数，且可取可消费上界

$$
|r|\le
\frac{\|c'+2Q'\|_\infty+\|cQ-Q'\|_\infty}{Q_*}
=:C_r,
\qquad
|h_\nu|\le |\nu|\left\|\left(\frac1{aQ}\right)'\right\|_\infty
=:C_{h,\nu}.
\tag{10}
$$

没有假定所有波数共用一个正的唯一性区间；下面逐个固定模式证明，这已足够。

## 3. 线性 Gauss 先确定真实尾迹

在固定末邻域 $\dot a=0$，线性化完整 Gauss 得

$$
n_0\dot l+l_0\dot n=0.
\tag{11}
$$

对每个 $\tau>0$ 用 (6) 写成 $\dot n=-q\dot l$。因为 $\dot l$ 在闭域有界，而 $q(0)=0$，连续切口迹必有

$$
\dot n(S,u)=0\qquad\text{对全部 }u.
\tag{12}
$$

微分准确尾端口 (3)，得到
$\dot n(S,u)=\dot\kappa(a_c\sin u)\cos^2u$。
在 $\cos u\ne0$ 上这迫使 $\dot\kappa(a_c\sin u)=0$；连续性补足两个轴点。因此 $\dot\kappa=0$ 在完整切口取到的 $y$ 区间，进而 (3) 给

$$
(\dot n,\dot m,\dot l)(S,u)=0.
\tag{13}
$$

这一推理没有把尾的非负控制盒当作微分方程条件，也没有在 $n_0(S)=0$ 处相除。即便允许带符号的一阶尾曲率，只要仍使用准确端口 (3)，结论相同。对于 R170 的固定 degree-15 多项式域，曲率是严格正的窗口因子乘多项式，在 $17/50<|y|<4/5$ 的开区间窗口因子为正。于是零一阶曲率使一阶多项式在开区间恒零，线性独立的 Bernstein 系数也全为零。

## 4. 每个非零模式的终端 Volterra 唯一性

先写实际 D2 奇偶模式
$\dot n=N(s)\cos(\nu u)$、
$\dot m=M(s)\sin(\nu u)$、
$\dot l=L(s)\cos(\nu u)$；当前表示的 $\nu=2j$，$j\ge1$。一般复 Fourier 模作相同计算，只在系数中出现 $\mathrm i\nu$，绝对值估计不变。

在末邻域线性化 Codazzi，转用 $\tau$ 得

$$
N_\tau=-\frac{\nu}{a}M-c(L-N),\qquad
M_\tau=\frac{\nu}{a}L+2cM,\qquad N=-qL.
\tag{14}
$$

代入 $q=\tau Q$ 并用 (8)–(9)，准确整理为

$$
L_\tau=\left(-\frac3\tau+r(\tau)\right)L+
\left(\frac{2\nu}{\tau}+h_\nu(\tau)\right)M,
\qquad
M_\tau=\frac{\nu}{a}L+2cM.
\tag{15}
$$

这不是仅保留首项的近似方程。所有剩余系数由 (10) 真实有界。

设 $R(\tau)=\int_0^\tau r(t)\,dt$。因 $L$ 有界，
$\tau^3e^{-R(\tau)}L(\tau)\to0$。积分 (15) 第一式给准确关系

$$
L(\tau)=\frac{e^{R(\tau)}}{\tau^3}
\int_0^\tau t^3e^{-R(t)}
\left(\frac{2\nu}{t}+h_\nu(t)\right)M(t)\,dt.
\tag{16}
$$

令 $L_\epsilon=\sup_{[0,\epsilon]}|L|$、$M_\epsilon=\sup_{[0,\epsilon]}|M|$。对 $0<\epsilon\le\tau_0$，(10)–(16) 给

$$
L_\epsilon\le
e^{2C_r\tau_0}
\left(\frac{2|\nu|}{3}+\frac{C_{h,\nu}\tau_0}{4}\right)
M_\epsilon
=:B_\nu M_\epsilon.
\tag{17}
$$

(13) 给 $M(0)=0$；$a\ge a_c$、$|c|\le1/a_c$ 以及 (15) 第二式给

$$
M_\epsilon\le
\epsilon\left(\frac{|\nu|}{a_c}L_\epsilon+
\frac2{a_c}M_\epsilon\right).
\tag{18}
$$

选择任意
$\epsilon< a_c/(|\nu|B_\nu+2)$，联立 (17)–(18) 得 $M_\epsilon=L_\epsilon=0$，从而 $N=0$。这完整排除了具有零尾迹的非零有界模式，不诉诸未经证明的 Fuchs 展开。

## 5. 轴对称外设计不会给非零模式强迫

对整个前缀线性化 Gauss–Codazzi，$\dot a,\dot c,\dot K$ 都只依赖 $s$。基准三场也无角依赖，故所有这些外设计强迫只落在零角模。非零模仍满足

$$
n_0L+l_0N=0,\qquad
N_s=\frac{\nu}{a}M+c(L-N),\qquad
M_s=-\frac{\nu}{a}L-2cM.
\tag{19}
$$

在任意内部闭区间 $n_0>0$，可用 $L=-l_0N/n_0$ 将其化为连续系数的二元线性 ODE。第四节给出的真实末邻域零解，通过通常的初值唯一性反向延拓至中央；每个内部共享两 jet 分界处系数连续，逐片延拓一致。这样每个非零角模在全前缀为零。

注意这里仅在远离切口的内部正分母域作代数消元。不能以 (19) 的内部形式把切口当作普通的非奇异初值点；真正的切口唯一性已经由 (16)–(18) 单独支付。

## 6. 中央曲线与 gap

中央曲率是 $n_t(0,u)$。第五节使其一阶变化与 $u$ 无关。每条中央凸曲线材料速度为 $a_0$，闭合转角为 $2\pi$，因此准确

$$
a_0\int_0^{2\pi}n_t(0,u)\,du=2\pi.
\tag{20}
$$

微分 (20) 后，其常数一阶变化也为零。若 $\theta_t$ 是中央单位切线的角，$\partial_u\theta_t=a_0n_t$；于是 $\dot\theta$ 为常数。再次积分曲线的位置一阶导数，得到它只是固定的平面转动与平移。中心对齐的轴支持差在圆上的导数为零，得到 (4)。这没有把另一个不依赖曲率的“幅度等式”偷偷加入系统。

## 7. 可用于计算的含义及明确不适用范围

准确圆参考仍是全部 GC 和零尾/零 gap 边界的真实解。本文说明的是：在该点直接线性化、同时强制一个非零线性 gap 步，不能把其有限求积最小二乘方向解释成已经构造出的可微精确分支。离散表示可能用非常窄的末端变化容纳该方向，必须在实际有限幅场上重新核 full Gauss/Codazzi，而不能靠形式的圆点 Jacobian 宣称存在。

实际 gap $.05$ 求解继续。一个明确的非零初猜可先在准确中央曲率族里求有限正 gap，选一组严格非零且满足 R170 的尾控制，再用圆参考与真实尾的完整函数拼成字段；这只是初值，完整残差必须实际计算。末正 $K$ 区还可用 R156 的 $d=n-l,m$ 正迹公式生成有限幅参考，再投影到当前 raw 空间；投影改变的误差不得隐去。

本文没有声称：

- 任意小 gap 的解都必须在本定理的 $C^0$ 第二基本形式拓扑中可微；
- 存在一个对所有高角模一致的有界线性逆；
- 非圆强目标不存在，或当前 R114 基础族受到此定理排除；
- 任意非零尾都不能在有限幅下接合；
- 当前尚未运行的 B32 有限目标、初猜或求解已经通过。

当前 B32 的独立全角物理点目标源已另名保存；它与本命题的数学连续极限明确分开。完整图的真实共同度量误差、配准高度、C² seam、held、全部法球和强目标仍须由实际最终非圆候选支付。
