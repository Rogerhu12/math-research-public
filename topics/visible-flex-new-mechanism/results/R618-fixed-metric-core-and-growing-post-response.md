# R618 固定完整度量的核心均值链与逐级独立 post 响应

2026-11-27。状态：下述核心端式、有限新模的真实强迫内尾及嵌套表示已证明；
完整非线性内尾/主体的求解与无限角带一致逆尚未证明，主课题未完成。

本条接 [R587](R587-fixed-metric-mean-height-elimination-at-flat-cap-and-core.md)、
[R602](R602-exact-nonlinear-core-trace-elimination.md) 和
[R617](R617-finite-pre-tanh-poles-and-open-cap-rigidity.md)。
它不改正在运行的实际1130q完整位置目标，不重算已付低模内口，
也不把有限表示的准确零缺陷障碍改写成正误差下界。

## 1. 冻结的是函数，canonical mean 的分拆不改变旧高度

静态设计结束后选定并完整固定
\[
g_*=E_*(r)\,dr^2+r^2d\theta^2 .                                      \tag{1}
\]
完整身份包括原参数、原无限尾、全部径向基与从属核心函数、
连续 turning 根的分支及其真实导数。以后增加角频、径向点或精度时都调用同一函数。
不得用每一新网的 turning 根重新定义一个新 $E_*$。
原设计参数 $H$ 此后也不能作为改变 $E_*$ 的自由均值控制。

既有输入中 $Z_*=h_*+\sigma\tanh(V_*/\sigma)-A_{512}+P_*$。
这里 $A_{512}$ 是固定512材料角的原定义，与后来观察网无关。
若使用连续零均值参数化，只作准确的恒等分拆
\[
\bar h_*=h_*+A_\infty-A_{512},\qquad
f_* =\sigma\tanh(V_*/\sigma)-A_\infty+P_* ,\qquad
A_\infty=\langle\sigma\tanh(V_*/\sigma)\rangle .                  \tag{2}
\]
于是 $Z_*=\bar h_*+f_*$ 完全不变，$\langle f_*\rangle=0$。
这不准许把 $A_{512}$ 悄悄换成某个新离散均值；(2)中同一个标量同时加进均值、
从角部分减去。其求积误差仍须单独支付。
若原静态数值根只是有限角求积结果，不能声称它已经等于(1)的连续根。
从那个数值输入到完整连续定义的误差和可能修正必须明列。

固定 $E_*$ 后，令 $Z=h_0+f$、$\langle f\rangle=0$，用 R587 同一个标量方程
求 $p_0=h_0'$。记
\[
p=p_0+f_r,\quad q=f_\theta,\quad t=f_{\theta\theta},\quad
b=(r^2-q^2)^{1/2},\quad u=(E_*-r^2p^2/b^2)^{1/2},
\quad N=r/b+r^2pt/b^3,
\]
\[
\langle N/u\rangle=1,\qquad
C=E_*t+rp,\quad B=f_{r\theta}-q/r,\quad
M=r+pt-q^2/r,\quad \omega=r^2/(u^3b^3).                         \tag{3}
\]
在 $b,u,N>0$ 以及
\[
c_0:=\langle\omega C\rangle\ne0                                  \tag{4}
\]
的同一连续分支上，R587 给出真正的根导数
\[
p_0'=\frac{\langle\omega(E_*B^2+E_*'M/2-Cf_{rr})\rangle}{c_0},
\quad D=C(p_0'+f_{rr})-E_*B^2-E_*'M/2 .                         \tag{5}
\]
这些式子只除角平均 $c_0$，不点除可能变号的最高系数 $C$。
没有在任何一条响应方向中重新解一个可变化的 $E$。

### 一个允许 $C$ 变号的均值非退化充分界

若 $p_0<0$、$0<\omega_-\le\omega\le\omega_+$，则由
$\langle rf_r+E_*t\rangle=0$，
\[
c_0\le rp_0\omega_-+
\frac{\omega_+-\omega_-}{2}
\left\langle|rf_r+E_*t|\right\rangle .                           \tag{6}
\]
证明是从第二项减去常数 $(\omega_++\omega_-)/2$ 后取绝对值；
第一项因 $p_0<0$ 使用 $\langle\omega\rangle\ge\omega_-$。
右端严格负便足够，而不要求 $C$ 逐角同号。
(6)是可检查的充分界，本文没有宣称当前数值候选已经满足它。

## 2. 同一个固定 $g$ 的真实核心端式

设 $\delta=R-r$、$1/2<\alpha<1$，沿用 R597/R587 的逐阶可微核心展开
\[
W=k\delta^{-\alpha}(1+O(\delta^\sigma)),\qquad
\sigma>1-\alpha,\quad k>0,
\quad E_*=W^2+e_* ,\quad e_*\in C^1.
\]
假设 $f(R)=0$，$P=Wf_r$ 连同所需角 jets 有 $C^1$ 延伸，
$P_0=P(R)$、$P_1=P_r(R)$；它们均为连续角零均值。
由 R587 的非退化核心根，写
\[
p_0=-W+\zeta/W,\qquad \zeta\in C^1,
\quad u_R^2=e_{*,R}+2\zeta_R+2P_0,
\quad\langle u_R^{-1}\rangle=1 .                                \tag{7}
\]

置实际均值背景与对应的差量
\[
\widehat W=W-\zeta/W=-p_0,\qquad
\widehat e=E_*-\widehat W^2=e_*+2\zeta-\zeta^2/W^2,
\quad\widehat P=\widehat Wf_r=(1-\zeta/W^2)P .                  \tag{8}
\]
$W^{-2}=O(\delta^{2\alpha})$ 的一阶导数是
$O(\delta^{2\alpha-1})\to0$。因此准确有
\[
\widehat P_R=P_0,\quad\widehat P'_R=P_1,\quad
\widehat e_R=e_{*,R}+2\zeta_R,
\quad\widehat e'_R=e'_{*,R}+2\zeta'_R .                          \tag{9}
\]
而 $\widehat W/W=1+O(\delta^{2\alpha})$，连同其导数仍满足原核心假设；
因为 $\min(\sigma,2\alpha)>1-\alpha$。
这一步说明可以把已证 R597/R602 应用于真实均值 $\widehat W$，
不是将 $p_0=-W$ 继续硬塞进固定 $g$ 的方程。

记 $e(P_0)$ 是唯一连续根
\[
\left\langle(e(P_0)+2P_0)^{-1/2}\right\rangle=1,
\qquad e(P_0)+2P_0>0,
\quad c=\frac\alpha{1+\alpha},\quad
S=\langle(P_0)_\theta^2\rangle .                                 \tag{10}
\]
由(7)--(9)首先得到
\[
\boxed{\zeta_R=\frac{e(P_0)-e_{*,R}}2 .}                         \tag{11}
\]
在未施加核心零残差之前，同一个 turning 根的径向导数必须是
\[
e'_{*,R}+2\zeta'_R
=-2\frac{\langle P_1/u_R^3\rangle+
\langle(P_0)_{\theta\theta}/u_R\rangle/[R(1+\alpha)]}
{\langle u_R^{-3}\rangle}.                                      \tag{12}
\]
完整核心缺陷则为
\[
D_R=-RP_1+c\{e(P_0)+2P_0\}(P_0)_{\theta\theta}
 -(P_0)_\theta^2-\frac R2(e'_{*,R}+2\zeta'_R).                   \tag{13}
\]
利用 R602 已证的必要充分消元，(12)--(13)给
\[
\boxed{D_R\equiv0\ \Longleftrightarrow\
P_1=P_1^*(P_0):=
\frac{c\{e(P_0)+2P_0\}(P_0)_{\theta\theta}
-(P_0)_\theta^2+(2c+1)S}{R}.}                                   \tag{14}
\]
此时还有必须保留的固定 $g$ 均值端式
\[
\boxed{\zeta'_R=-\frac{2c+1}{R}S-\frac12e'_{*,R}.}             \tag{15}
\]
因此(14)在固定 $g$ 下仍可用，但不能再把 $e'_{*,R}$ 自由改成
$-2(2c+1)S/R$；承担差额的是同根给出的 $2\zeta'_R$。
(15)不是第二个独立自由条件，更不能在计算内点根之后另行覆盖它。

### 完整参数链

对零均值方向 $H=\delta P_0$，固定 $E_*$ 后
\[
\delta e=-2\frac{\langle H/u_R^3\rangle}{\langle u_R^{-3}\rangle},
\qquad \delta\zeta_R=\tfrac12\delta e,
\]
\[
\delta P_1^*=\frac{
c\{(\delta e+2H)(P_0)_{\theta\theta}
 +(e+2P_0)H_{\theta\theta}\}
-2(P_0)_\theta H_\theta
+2(2c+1)\langle(P_0)_\theta H_\theta\rangle}{R},                  \tag{16}
\]
\[
\boxed{\delta\zeta'_R=-\frac{2(2c+1)}R
\langle(P_0)_\theta H_\theta\rangle .}                          \tag{17}
\]
同一转向根、两个均值端量和全部从属非零角核心项都必须沿这条链微分。
不能只对固定的 $e$ 或固定的 $\zeta$ 求导。

## 3. 真正新增独立 post 频率，核心从属项不截断

取固定 $r_c<r_a<r_b<R$，令 $\chi_c$ 在 $r\le r_a$ 为0、
$r\ge r_b$ 为1，连接函数准确光滑。对任意当前 $f$，定义
\[
\mathcal C[f]=f+
\frac{\chi_c(r)\delta^{\alpha+2}}{k(\alpha+2)}
\{P_1^*(P_0[f])-P_1[f]\}.                                     \tag{18}
\]
由 R602 的准确自由阶，(18)保留 $P_0$、令 $P_1=P_1^*(P_0)$，
保留全部真实内尾，且保持角均值为零。
用固定 $E_*$ 重新求同一 $p_0$ 根后，(11)--(15)随之成立。
由(8)--(9)，不需要把(18)中的固定 $W,k$ 换成每次新定义的背景。

新增独立的核心 $P_0$ 控制也可以显式实现。令
\[
A_c(r)=-\int_r^R\frac{dt}{W(t)},\qquad
f_{Q}(r,\theta)=\chi_c(r)A_c(r)Q(\theta),\qquad\langle Q\rangle=0.
                                                                    \tag{19}
\]
在核心邻域 $(W(f_Q)_r)_R=Q$、$\partial_r(W(f_Q)_r)_R=0$。
所以先加(19)，再作(18)，即可独立改变新的正偶核心频率，
而无需把对应新模错误地借接到旧模式的内尾。
内尾方向与主体方向仍另外保留，不能只用核心控制代替全域解。

若裸 $P_0$ 的最高频率为 $J$，(14)的最高频率是 $2J$。
所有这些从属模必须完整形成；不能因为独立自由变量只到 $J$ 就把 $J$ 以上截掉。
其连续均值严格为零，乘积可按真实三角系数卷积形成；
标量根(10)仍是连续积分，不因 $P_0$ 有限带而成为有限精确求积。

对固定基场 $f_*$，逐级空间可采用
\[
f_J^{\rm bare}=f_*+
\sum_{2\le j\le J\atop j\ {
m even}}
\{\chi_{\rm in}g_j(r)+b_j(r)+\chi_c A_c Q_j\}\cos(j\theta),
\qquad f_J=\mathcal C[f_J^{\rm bare}].                          \tag{20}
\]
这里 $\chi_{\rm in}$ 在一个明确完整内尾恒为1，随后光滑降为0并在核心邻域恒零；
$b_j$ 是内尾/核心开邻域皆为零的独立径向函数。
$g_j$ 必须满足下一节的真实强迫口，不能用同一个齐次核替代一般强迫。
新增频率直接加在 tanh **之后**，不通过同一个有限 $V$ 的参数再间接生成。
保留基场当前幅度，新增系数从零开始；不以缩小振幅冒充精化。

在已有 $f_J$ 的全部独立系数不变、新系数为零时，
$J\to J'>J$ 的表示给出同一裸函数、同一连续核心根和同一(18)，故嵌入准确。
若最初基场只满足原有限512求积版核心条件，(18)在初次应用时可能非零；
这一实际变化必须记录，不能声称它是零系数的原场恒等嵌入。
同样，数学积分(19)的数值评价不是免费已付工作。

## 4. 任意新增有限角带的真实平尾，而非复制旧口

已有 $j\le32$ 继续引用 R583/R596/R600，数值口不重做。
这里支付新增任意**固定有限** $J\ge33$ 的尾存在范围。
取 $2\le j\le J$、$\mu=j^2$，仍用同一个实际温和尾
\[
W=\tfrac45e^{-u(2-\sin(u+\varphi))},\quad
r=\tfrac{11}{50}+\tfrac1{5u},\qquad
p=4u^2r^{2\mu}e^{-u(2-\sin(u+\varphi))},
\quad\varepsilon=\frac{\mu(\mu-1)\ell^2}{r^2u^4}.              \tag{21}
\]
只需在 $u\ge\max(100,4J)$ 开始新证明；相位先取模 $2\pi$ 的代表
$0\le\varphi<2\pi$ 并据此编号峰，则例如实际峰索引
$n_J=J+17$ 对全部相位都足够。
这不是删除原口与新口间的材料：新模必须沿自己的准确 ODE 外传到原主体公共边界，
原已有模仍保留各自原口。

R600 的 stationary-point 函数现满足
\[
0<\eta\le\frac{137}{44u}<.032,
\quad
|\eta'|\le\frac1u+\frac{147}{44u^2}
+\frac{4+25/242}{u^3}<.011 .                                  \tag{22}
\]
这由 $\mu\le u^2/16$ 直接代入原导数式得到；故原峰/谷的$.04$唯一窗口、
每 cell 长度 $6<\alpha_{n+1}-\alpha_n<7$ 和单谷结构继续成立。
对 cell 左端 $a\ge\max(100,4J)$，原权包络中的上侧常数可取
\[
B_a=\frac65\exp\!\left(\frac{20J^2}{11a}\right)
\le\frac65e^{5a/44},\qquad
C_a=4r_c^{2\mu}a^2 .                                           \tag{23}
\]
即 $e^{-21}C_a e^{-a(2-\sin)}\le p\le B_aC_a e^{-a(2-\sin)}$。
此外 $\varepsilon\le J^4/a^4\le1/256$，
所以准确 Dirichlet Green 小量至多 $49/512<1/4$。
原势下界 $\varepsilon\ge a^{-4}$ 仍成立：最小 $\mu=4$、
$r<.222$、$u<a+7$ 代入便有严格余量。

因此原 R600 的准确 DtN 比值证明给
\[
\frac{k_{n-1}}{V_n},\frac{k_n}{V_n}
\le\frac{1536}{5}e^{42}a^4e^{-61a/44}<\frac1{64},              \tag{24}
\]
其中相邻 cell 的 $B$ 也可用右端 $a$ 的上界(23)，因为前一左端小于 $a$。
在 $a=100$，右侧小于 $2^{9+27-96}=2^{-60}$，之后严格递减。
由此原 $[0,1/32]$ 上的 Riccati 收缩及截断界继续成立。
对足够大的 $a$（例如 $a\ge1000$ 再保留 $a\ge4J$），
比值还小于 $\tfrac12e^{-a}$，故实际 $\rho_n\le e^{-\alpha_n}$。
节点得到高斯衰减，cell 内固定阶 ODE 导数只损失线性指数和多项式，
所以每个新固定 $j$ 都有真实非零全平核及一维唯一性。
这不产生任何新数值 Cauchy 数据，也不声称 $j\to\infty$ 的一致 tame 界。

### 强迫尾的全平存在与准确仿射 DtN

记 $\mathcal G_\beta$ 为全部固定阶所需径向/角向 jets 均被
$C_{kl}e^{-\beta u^2}$ 控制的尾类。
对任意上述固定 $j$，若强迫 $S_j\in\mathcal G_{1/21}$，则
\[
L_jg_j:=r(Wg_j')'-j^2W'g_j=S_j                                  \tag{25}
\]
有真实 $g_j\in\mathcal G_{1/40}$ 的全平特解；全平解的全部自由度是再加本模齐次核。

证明沿 R591 的真实 cell 强迫法，只更新已声明的指数。
准确变换 $g_j=r^\mu y$ 后右端为
$H=|r_u|r^{\mu-1}S_j$。
准确含势的端值插值函数记为 $H_L,H_R$。
零端强迫解的两个外通量为
\[
\beta_{n,L}=\int_{\alpha_n}^{\alpha_{n+1}}H_LH\,du,
\qquad
\beta_{n,R}=\int_{\alpha_n}^{\alpha_{n+1}}H_RH\,du .             \tag{26}
\]
这是 Lagrange 恒等式，保留任意实符号强迫，不作同号假设。
由于 $|H_L|,|H_R|\le2$，通量至多 $14\sup|H|$。
$V_n$ 的倒数只增加固定 $j$ 的常数、线性指数和多项式，
故节点强迫在足够大的完整尾上至多 $C_j e^{-\alpha_n^2/22}$。
在节点范数 $\sup e^{\alpha_n^2/30}|y_n|$ 中，前邻项范数至多
$e^{-\alpha_n+14\alpha_n/30}$、后邻项至多 $e^{-\alpha_n}$，和小于1/2。
固定首节点的 particular 值为0，真实收缩给唯一衰减节点解。
各 cell 的准确零端 Green 解和插值，再加全部固定阶 ODE 导数估计，
把线性指数损失吸收进 $1/30-1/40$ 的余量，即得所称 $\mathcal G_{1/40}$ 解。
这是实际存在证明，不是口内置零。

为明确下一实现必须保留的仿射项，令
$\beta_n=\beta_{n-1,R}+\beta_{n,L}$。
节点方程准确为
\[
V_ny_n+k_{n-1}y_{n-1}+k_ny_{n+1}=\beta_n .                      \tag{27}
\]
写 $y_n=-\rho_n y_{n-1}+\tau_n$，则
\[
\rho_n=\frac{k_{n-1}}{V_n-k_n\rho_{n+1}},\qquad
\tau_n=\frac{\beta_n-k_n\tau_{n+1}}{V_n-k_n\rho_{n+1}} .         \tag{28}
\]
若完整尾起点为 $\alpha_N$，其准确左外通量为
\[
\boxed{q_{N,L}=(D_{N,LL}+k_N\rho_{N+1})y_N
              +\beta_{N,L}-k_N\tau_{N+1}.}                    \tag{29}
\]
旧齐次口只支付(29)的线性系数，**没有支付新的仿射强迫项**。
相同固定 $W$ 下对参数微分时 $\rho$ 不变，而
$\delta\tau_n=(\delta\beta_n-k_n\delta\tau_{n+1})/(V_n-k_n\rho_{n+1})$；
所有新强迫积分及其导数必须计算并收费。
真实二阶径向jet是
\[
g_j''=-\frac{W'}W(g_j'-j^2g_j/r)+\frac{S_j}{rW},                 \tag{30}
\]
更高口jets还含 $S_j$ 的导数；不得沿用齐次13jets而忽略它们。
上述式子没有认证浮点 ODE、有限尾截断的强迫余项或向共同主体口的传播误差。

## 5. 固定 $g$ 下真实非线性强迫必须包括什么

在内尾写固定 $E_*=1+W^2+e_*$、同根 $p_0=-W+s$。
对任意当前全角 $f$，(5)中的完整缺陷恒等分解为
\[
D=-\mathcal L_W f-r(Ws)'-\frac r2e_*'+\mathcal N,
\qquad\mathcal L_Wf=r(Wf_r)'+W'f_{\theta\theta},                 \tag{31}
\]
其中准确余项为
\[
\begin{aligned}
\mathcal N={}&E_*t(s'+f_{rr})-E_*B^2
+r(s+f_r)(s'+f_{rr})-e_*W't\\
&-WW'(s+f_r)t-\frac{e_*'}2(-W+s+f_r)t
+\left(WW'+\frac{e_*'}2\right)\frac{q^2}{r} .                  \tag{32}
\end{aligned}
\]
逐项展开 $C(-W'+s'+f_{rr})-E_*B^2-E_*'M/2$：
背景 $rWW'$ 与 $r(2WW')/2$ 相消；
$-E_*W't+W^2W't=-W't-e_*W't$，其余正是(31)--(32)。
这是完整非线性强迫，包含同一个固定度量差量和同一均值根导数。

故每个非零偶角模需要
\[
L_j f_j=2\langle\mathcal N\cos(j\theta)\rangle .                 \tag{33}
\]
若 $f=f_*+P$，独立 post 响应的真实右端是
$2\langle\mathcal N(f)\cos(j\theta)\rangle-L_j(f_*)_j$。
它通常随全部未知响应改变；只携带旧二阶 $j=4$ 的某个固定强迫，
或者只添加新齐次 $j$ 核，都不等于解(33)。
也不能点除某个角位置上失号的 $C$ 来生成径向加速度。

这些尾类与真实强迫相容：若 $f\in\mathcal G_{1/40}$，
固定 $e_*\in\mathcal G_{1/21}$，同根给
$s\in\mathcal G_{1/22}$。
这里还需用零均值的二次余量，不能仅从 R587 的定性全平类直接读取指数：
在 $(e_*,f,s)=(0,0,0)$ 处，turning 泛函对 $f$ 的一阶项是
$-W\langle f_{\theta\theta}/r+f_r\rangle=0$，
对 $s$ 的导数为 $-W$；对 $e_*$ 的导数为 $-1/2$。
故根差由 $e_*$、至少二次的 $f$ jets 及其高阶交叉项除有限次 $W$ 控制。
R587 的有理化非退化变量允许逐次对固定阶jets作相同估计；
除有限次 $W$ 仅损失线性指数，$1/21-1/22$ 的余量给上述结论。
(32)中的两 $f$ 因子至少有 $e^{-u^2/20}$，
其余项有更快的高斯因子，故 $\mathcal N\in\mathcal G_{1/21}$。
于是上一节真实线性强迫求解返回 $\mathcal G_{1/40}$。
这里说的是稳定的函数类别与每次真实线性强迫尾的存在，
尚未建立完整非线性映射在所有模式上的统一收缩常数。
若求的是相对任意基场的 post 修正，还必须检查
$L_j(f_*)_j$ 的相应强迫衰减；单独知道 $f_*\in\mathcal G_{1/40}$
不足以推出它属于 $\mathcal G_{1/21}$。
旧真实齐次项的这部分严格为零；已有 forced 项须保留其原真实源，
其余包络或非线性项按实际定义计入，不能省略。
尤其不能从这段指数余量直接宣称全角、全径向或宏观分支已经存在。

## 6. 角带极限中已排除的漏洞与仍须支付的量

对解析角类可用
\[
\|P\|_{\rho,s}=\sum_{m\in\mathbb Z}(1+|m|)^s e^{\rho|m|}|P_m|.
\]
若在同一固定 $g$、同一幅度/时间范围上，独立 post 的所需径向加权jets
在某个 $\rho>0$ 有统一可和界，则对任意 $0<\rho'<\rho$，
真 Fourier 截断在 $\rho'$ 范数中收敛，所需有限个角导数也收敛。
这只是绝对收敛级数的尾估计，不是假定未获得的统一界已经成立。

核心根映射有直接稳定性：
$|e(P)-e(Q)|\le2\|P-Q\|_\infty$，
可由(10)的严格单调性和逐点根比较证明。
在统一正域中，(16)及 Wiener 乘积不等式给(14)的连续依赖，
并只损失明示的两个角导数。
所以若独立 $P_0$ 及足够角jets真收敛，完整从属 $2J$ 核心项也收敛；
不能截去它们后再引用这一结论。

R617 的无限复极点论证针对有限 post Laurent 多项式。
逐级独立 post 的极限一般只在一个角解析带有定义，
不具有在整个复圆柱上对所有 tanh 极点均解析的有限多项式性质。
因此(20)给出必须保留的真正额外自由度；
它没有证明某个非平凡解必然落在此极限里。

后继真正求解必须共同完成：固定(1)的全函数身份及导数误差，
同根(3)--(5)的正域/非退化覆盖，新增(26)--(30)的真实强迫口和全成本，
完整(14)--(18)核心链，全部正文角残差及其未保留尾，
以及足以支持同一幅度/时间范围的收敛估计。
新的有限 scope 可以取得实际下降；只有这些量连同闭面几何、reach、
宏观握持和整像变化的 README 条件真正付清才是本课题完成。

## 7. 同固定 $E_*$ 的内点完整离解导数

这部分给下一实现直接使用，避免把 R613 中变化 $E$ 的导数原封不动套来。
设 $H=\delta f$，先暂取 $\delta p=H_r$、$\delta q=H_\theta$、
$\delta t=H_{\theta\theta}$，形成 $\delta_fN,\delta_f u$。
对(3)同根隐微分得
\[
\delta p_0=-\frac{\langle\delta_fN/u-N\delta_fu/u^2\rangle}{c_0},
\quad\delta p=\delta p_0+H_r,\quad\delta E_* =\delta E_*'=0 .  \tag{34}
\]
全部真实变化为
\[
\delta b=-q\delta q/b,\quad
\delta u=-\frac{r^2p\delta p}{ub^2}
-\frac{r^2p^2q\delta q}{ub^4},
\]
\[
\delta N=\frac{rq\delta q}{b^3}
+\frac{r^2(t\delta p+p\delta t)}{b^3}
+\frac{3r^2ptq\delta q}{b^5},\qquad
\delta\omega=-3\omega(\delta u/u+\delta b/b).                   \tag{35}
\]
记 $Q=E_*B^2+E_*'M/2-Cf_{rr}$，则
\[
\delta C=E_*\delta t+r\delta p,\quad
\delta B=H_{r\theta}-\delta q/r,
\quad\delta M=t\delta p+p\delta t-2q\delta q/r,
\]
\[
\delta c_0=\langle\delta\omega C+\omega\delta C\rangle,
\quad\delta Q=2E_*B\delta B+E_*'\delta M/2
-\delta C f_{rr}-CH_{rr},
\]
\[
\boxed{\delta p_0'=\frac{\langle\delta\omega Q+\omega\delta Q\rangle
-p_0'\delta c_0}{c_0}.}                                        \tag{36}
\]
最后
\[
\delta D=\delta C(p_0'+f_{rr})+C(\delta p_0'+H_{rr})
-2E_*B\delta B-E_*'\delta M/2,
\quad\delta R=\delta\omega D+\omega\delta D.                   \tag{37}
\]
这里未假定 $D=0$，所有离解项都保留；不需要三阶高度jets。
R613 的外层两次 primitive 链可直接用这个 $\delta R$、
$\delta a=\delta N/u-N\delta u/u^2$、$\delta b$，并取 $\delta E_*=0$。
这正是固定度量之后应该换入的新均值链。
