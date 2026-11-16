# R464：非零三次母矩与剩余九行的同周期光滑规范支付

日期：2026-11-16。**完整纸面存在证明；没有执行新的 profile、积分、符号程序、矩阵秩、开发检查或科学作业。**

本稿在 R455/R450 的同一次初选中增加一个严格开条件：每个最终母包的
$M_3(u)=\int(u'')^3$ 非零。它不增加必须保持的纤维方程，也不假设原已经冻结的母库具有这个值。原四个完整自然矩、共同 $F^\star=(F_{\rm rat},D,E_5)$、二十个真实目标、唯一共同退化镜对以及原合法窗口，仍在同一个最终对象上满足。

在这个加强的真实库上，若同一个完整成本的两个 period 已经有真紧特解，且最高 $P_2$ 的两个特解类值为零，则原其余九行可以由同一个光滑 period 齐次规范准确支付。三条第三合法矩随后用 R461 的原右逆支付而不动任一端口行。因此，本稿处理的是全部十三行与已有真 range 的相容性，不以十三这个行数授秩。

证明含两个不能省略的步骤。先对两个完整源各选一次统一的多项式紧逆；原十二复制外的八宏块使这个所选特解的九行残差全部 odd 相位系数为零。再对原九行构造明确右逆：前三行用同一实际母的六个真平移副本，后六行用两种原编码角色及其 $g$ 翻号平台。种子处后一个矩阵本身降秩；我们使用已证明的右端消失因子构造光滑解，不把点态满秩偷延到种子。

直接来源：[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)、[R312](R312-quadratic-height-ports-and-rational-arctangent-logarithmic-ruling.md)、[R326](R326-one-global-second-gauge-pays-the-complete-rational-port-and-preserves-joint-cost.md)、[R327](R327-analytic-packet-period-kernels-and-a-finite-same-gauge-joint-system.md)、[R389](R389-ordered-total-fluxes-and-complete-flat-end-germs-for-the-rational-port.md)、[R410](R410-zero-fifth-moment-mothers-with-one-degenerate-pair-and-nineteen-exact-targets.md)、[R431](R431-common-exterior-degeneracies-in-the-complete-four-constraint-nineteen-target-library.md)、[R450](R450-seventeen-degree-true-inverse-and-exact-second-period-macro-cancellation.md)、[R455](R455-four-natural-moments-with-one-common-degenerate-pair-and-twenty-targets.md)、[R460](R460-automatic-simple-critical-point-residues-and-complete-smooth-period-gluing.md)与 [R461](R461-complete-hook-blindness-and-the-nine-row-same-gauge-interface.md)。下面只新增所列纸面接口，不重复原二十秩或实际成本计算。

## 1. 固定原几何、原九行与所需条件

沿原二次高度端芽，记
$$
h=H(1+\varepsilon\sigma^2),\qquad
K=1+\kappa^2,\qquad H>0,\quad\varepsilon>0,\quad\kappa\ne0 .
$$
除原安装条件外，从起点选
$$
\boxed{1-\kappa^4-4\varepsilon\ne0.}
\tag{1}
$$
R312 的小正 $\varepsilon$ 安装区间中至多排除一个值，所以这是允许的初选，不是在旧冻结度量上改参。

采用原 E8 名称
$$
P=r_0,\ R=r_1,\ S=s_0,\ L=p_0,\ U=s_1,\ V=p_1,\ T=t_1,\ Y=p_2,
$$
并写
$$
B=aR-2eL+eU+\beta T,\qquad
a=\frac{K(\varepsilon-2K)}{32H^2},\quad
e=\frac{\kappa K}{4H},\quad \beta=-\frac{\varepsilon}{4}.
\tag{2}
$$
这里 $e,\beta$ 均非零。

原实际圆为 $\phi_\theta=f\cos\theta+g\sin\theta$，
$D_\theta=f^2-\phi_\theta^2$，$\Delta=f^2-g^2$。全部最细包、原八复制、十二复制、五块及 R450 外八宏块都从起点纳入。每个完整 base 自己满足
$$
\mathbf I(F,F)=\mathbf I(G,G),\qquad \mathbf I(F,G)=0 .
\tag{3}
$$
其逐布局依据是 R280(3),(11),(17) 的 $\sum R_i t_i^q=\sum T_i t_i^q=0$；不是以八复制的三次幅权冒充二次闭合。

原剩余九行按次序分为
$$
\mathcal B_\theta=
\bigl(P_{-4},P_{-3},H_{B,0}\ ;\
P_{-2},P_{-1},P_0,P_1,H_{B,1},H_{B,2}\bigr)_\theta.
\tag{4}
$$
$P_2$ 单列，三条合法矩记 $\mathcal L_\theta(k)=\mathbf I(\phi_\theta,k)$。

本稿的规范定理假设同一个最终完整成本 $V$ 满足原 $M=0$、$T=\tau\mathfrak H$、$\tau\ne0$ 的背景读法，以及
$$
\pi V=0,\qquad \mathcal Q_{\rm all}(V)=0 ,
\tag{5}
$$
并且其两个实际 incoming 修正后的 period 源 $G_d^c,G_e^c$ 确有同 collar 光滑紧逆。可以继续要求已有整个 $J^+(V)=0$；证明不把这些已付条件从实际联合目标中删除。真 range 必须由原全部 partial、端 germ、平台和 R460 的拼接支付，不由(5)推得。

## 2. 在原 cap 内同时看第三矩和第五矩

先使用 R410/R455 的实际正偶半 cap $\bar u$。它在中心准确为
$M-x^2/2$，正半轴严格下降，$M_5(\bar u)=\int(\bar u'')^5=0$，且仅有一对外部简单 $A_{\bar u}$ 零点。令
$$
p=\bar u',\quad r=\bar u'',\quad
A_{\bar u}=6pr'-2r^2.
$$
R410 峰窗内 $r$ 由负穿到正。取一个穿零点 $x_0>0$；这里 $p(x_0)<0$、$A_{\bar u}(x_0)<0$，所以
$$
r'(x_0)>0.
$$
先用连续性缩成一个固定小窗 $J_0$，使 $p<0,r'>0,A_{\bar u}<0$ 于该窗，且其闭包避开中心、两外退化根和最终解析平端。不能从任意 $A<0$ 区间直接推出 $r'>0$。

对支持于 $J_0\cup(-J_0)$ 的偶光滑紧变化 $v$，
$$
DM_3(\bar u)[v]=3\int(r^2)''v,\qquad
DM_5(\bar u)[v]=5\int(r^4)''v.
\tag{6}
$$
两次 IBP 的全部边项由紧变化方向清零，不改原函数锚。

这两行线性无关。若存在相关关系而 $DM_3$ 的系数非零，就有
$(r^2-cr^4)''=0$ 于 $J_0$。在 $x_0$，该函数及其一导都零，所以整个窗内 $r^2-cr^4=0$；这与 $r$ 严格穿零矛盾。若该系数为零，则 $(r^4)''=0$，同一论证也矛盾。偶延拓只使两侧积分乘同一个非零因子。因此
$$
\boxed{\operatorname{rank}D(M_3,M_5)|_{C^\infty_{c,\rm even}(J_0\cup-J_0)}=2.}
\tag{7}
$$
特别 $DM_5$ 在这个限制空间非零。

选择实现(7)的两个固定方向，用有限二维 IFT 沿 $M_5=0$ 作任意小的 $C^4$ 改动，使
$$
\boxed{M_3(\bar u)\ne0,\qquad M_5(\bar u)=0.}
\tag{8}
$$
若原第三矩已非零，则不必改变。变化完全内支撑，故中心二次 germ、两个外根及全部外 cap 都准确不动；窗内的正性、下降和严格 $A<0$ 有余量保持。其余区间未改，所以没有新增 $p$ 或 $A$ 根。这一步发生在 R455 固定半 cap 之前，不声称改动旧冻结母还保持旧 $F^\star$ 数据。

## 3. 周期四正常修正不会吃掉第三矩

把(8)的 cap 代入 R455 的原周期核构造。原
$\zeta(y+\pi)=-\zeta(y)$ 使 $\phi''$ 也反周期，所以
$(\phi'')^3$ 每周期平均为零。半 cell 的结论还同时使用原偶性：在核坐标中，$\rho=(\zeta'')^3$ 为偶函数且反周期，故 $\rho(\pi-y)=-\rho(y)$，原偶端相位上的半周期积分为零；这里没有仅由反周期性推出半周期零。因此未纠正母 $u_N$ 准确满足
$$
M_3(u_N)=M_3(\bar u)\ne0.
\tag{9}
$$
没有把单独半 cap 当紧输入；这里只对无显式 $x$ 的局部密度直接换元。

R455 四正常方向在 $O(N)$ 个不交 cell 中分别加同一个固定紧函数的平移。其真四根满足
$\|\theta^{(N)}\|=O(N^{-2})$。在固定小参数盒内，每 cell 的第三矩改变量为
$$
\int\{(\phi''+\theta h'')^3-(\phi'')^3\}
=O(|\theta|),
$$
常数只依已经冻结的 $\phi,h$，不依 cell 位置或 $N$。故
$$
\left|M_3(u_{N,\theta^{(N)}})-M_3(\bar u)\right|
\le C N\|\theta^{(N)}\|=O(N^{-1}).
\tag{10}
$$
先固定(8)的非零值，再选一个充分大的有限 $N$，使(10)小于其绝对值的四分之一。于是四个完整 $q$ 准确为零时，$M_3$ 仍非零且有固定余量。原 $D-E_5>0$、唯一外根和全部匹配，仍由 R455 原统一估计成立。

一次共同正支撑归一只给 $M_3$ 乘一个非零实因子，不能使其变零。此后这个有限周期数、外 cap、几何窗口需求和非零余量全部冻结。

## 4. 同一个 F★ 图册和二十根保留这一开条件

在 R455 的四约束图册中选真实限制最大 $F^\star$ minor 和全部二十 principal minor时，可以在任意小的有限维 $C^4$ 邻域内完成。把邻域缩小到同时满足
$$
|M_3(u)-M_3(u_*)|<|M_3(u_*)|/4
\tag{11}
$$
即可。这里没有把 $M_3$ 加入必须保持的 $F^\star$，也不改最大秩的定义；非零只是一个开条件。

最终有号集中与 $q/F^\star$ 纠正，在一个先固定的正幅盒上满足原统一
$$
\|U_{i,K,z}-u_0\|_{C^2}=O(K^{-1/2}).
\tag{12}
$$
$M_3$ 是固定支撑上的连续三次 $C^2$ 多项式。有限多个形状与整个固定幅盒可以共用一个阈值，使(12)导致的第三矩误差小于已留余量。再用同一个有限 $K$ 的真实二十维根，便得到
$$
q(U_i)=0,\quad F^\star(U_i)=F^\star(u_0),\quad
(\mathcal V_{19},d_P)=(0,\eta),\quad
\boxed{M_3(U_i)\ne0\ \text{对全部最终母}.}
\tag{13}
$$
原最高三阶脉冲只在单调窗，$A<0$ 的符号控制仍逐式按 R455(38)使用；不把(12)误说为三阶小。其它内区只有原光滑低阶小纠正，外 cap 一字不动。

全部真实副本同步使用这些最终母。物理宽度正缩放给 $M_3$ 一个非零幂因子；非零实幅可吸入实际 $a_i,b_i$。因此以下选出的任何真实编码角色都有非零第三母矩。本稿只证明这个从起点加强的库，不断言先前冻结的每个库已有(13)。

## 5. 两个完整源都能按真实 base 拆分

对一个固定完整 base $F=\sum a_i u_i,G=\sum b_i u_i$，令
$R_i=a_i^2-b_i^2,T_i=a_ib_i$。R389 的原 whole-pure-zero 极化给
$$
\begin{aligned}
V_d&=\sum_i a_i^2\left\{R_iS_i+\sum_{j>i}R_jU_{ij}\right\},\\
V_e&=-\sum_i a_i^2\left\{T_iS_i+\sum_{j>i}T_jU_{ij}\right\}.
\end{aligned}
\tag{14}
$$
$S_i=\Sigma_V(u_i)$，$U_{ij}$ 是完整 ordered $2+2$ 输出；两式都不是自然积分或只取左尾。

不同完整 base 的右方输入按原三矩线性。式(3)分别给
$\sum R_j\mu_j=\sum T_j\mu_j=0$，所以(14)的两条跨 base 输出均准确为零。由 whole $\mathcal Q_{\rm all}=0$，保留的各输出左尾至多 affine。

R450 §5 的拆分证明于是同时适用于 $d,e$：从全局真实紧逆截取每个 base 上的 $k'$，在两侧空隙补一个积分以使 $\int k'=0$，最后按原右锚恢复 $k$。局部式
$$
(L_fk)''=(A_fk'')'-6(f''f''')'k'
$$
保全部活动包上的方程；两个输出的右零值和零一导使剩余 affine 差为零。反向相加也成立。gap 修正改变平台值，但这些值包含在下面一次选定的真实逆里，不被删除。

因此两个总源已有真 range 时，每种完整 base 的每个真实副本都已有对应紧逆。不是从一个 base 当前可逆擅推其它位置可逆。

## 6. 一次选择两条真正的多项式紧逆

R450 使用的完整来源是
$$
\Sigma(N^{12}U)=0.
$$
它来自原真权 $[-9,3]$ 和 $\Sigma(U_{-9})=0$，不使用错误的
$\Sigma(U_{-8})=0$。因此把同一 base 的整个输出拉回固定坐标，
(14)的两个 canonical 源都是实际中心 $t$ 的次数至多十一多项式。

对每种固定 base，在原十二真实不同中心取已经存在的紧逆。用同一个逆 Vandermonde 作线性组合，分别得到
$$
k_d(t)=\sum_{m=0}^{11}t^m k_{d,m},\qquad
k_e(t)=\sum_{m=0}^{11}t^m k_{e,m},
\tag{15}
$$
其系数均为同一固定包络内的真正紧函数，并准确解各自的源多项式。这里 canonical 源始终指原 period 方程归一后的 $G_d(t)=-V_d^{\rm pull}(t)/(2\tau)$、$G_e(t)=-V_e^{\rm pull}(t)/(2\tau)$，其中 $V_e$ 保留(14)的原负号；式(15)已解 $L_Fk_{d,e}(t)=G_{d,e}(t)$，所以(16)只加入原 incoming 项，没有遗漏或再次施加这个 $-1/(2\tau)$ 因子。这里既不要求无限维闭像，也不假设存在一个全局连续逆算子。

原实际 incoming $X_*=\Phi_{m_*}$ 仍保留：
$$
k_d^c(t)=k_d(t)+T_{-t}X_*(T_t\Delta),\qquad
k_e^c(t)=k_e(t)-T_{-t}X_*(T_t(F,G)).
\tag{16}
$$
$\Delta$ 与 $(F,G)$ 的三个真矩均零，所以两项真紧。原 E8 公式在同步平移下次数至多四，故(16)仍至多十一。它们使用同一个实际 $X_*$，没有把 incoming 当作可自由选择的数。

对幅度 $\gamma$、$g$ 翻号 $\epsilon=\pm1$ 和中心 $t$ 的副本，按原 $L_{\gamma T_tF}=\gamma^2T_tL_FT_{-t}$，取对应特解
$$
k_{\theta,t}^{\,0}
=\gamma^2T_t\left\{\sin^2\theta\,k_d^c(t)
+2\epsilon\sin\theta\cos\theta\,k_e^c(t)\right\}.
\tag{17}
$$
把各真紧 base 特解相加即得整个实际圆的一个固定选择。九行不杀全部 $\ker L_f$，所以后文消去只针对这个明确选择；没有声称任意 particular 的九行值相同。

## 7. 全九行的十七次界与 odd 相位消去

对固定紧三槽 $k,F,G$ 同步平移，R326 的完整局部
$\mathcal T_h^\#(k;D)$ 显式位置次数至多五；最高来自
$Q_{\rm g}^2x\,k'''a''b''$。原 E8 二次公式的同步位置次数至多四，三个 $I_j$ 至多再加二，故全部十个端口系数对固定三槽的平移次数至多六。

原 J 的上端始终在同一右零 collar，所有平移展开都是原函数身份。不同完整 base 的端口交叉也消失：$XD$ 的三矩为零使其真实二次尾为零，mixed $X(\phi,k)$ 的非零输入在同一 base；遇到来自另块的二次尾时，紧 outer 与全部 $I_j$ 精确正交。$I_2$ 的 $2a'b'$ 项保留。gap 延拓支持在该 base 的预留包络，未跨入其它活动 base。

把(15)—(17)代入，所选完整残差
$$
\mathscr R_\theta(t)=\mathcal B_\theta(k_{\theta,t}^{\,0})
$$
的各相位系数均是 $t$ 的次数至多 $11+6=17$ 的真实多项式。整体是四次 profile 齐次量：源乘 $\gamma^4$、逆乘 $\gamma^2$、端口的其余两槽再乘 $\gamma^2$，所以权准确为 $\gamma^4$。

$G\mapsto-G$ 把整个式子送到 $\theta\mapsto-\theta$，包括(17)中的 $k_e^c$。因此两个 odd 相位系数准确乘
$\epsilon\gamma^4$。原十二包装与外八宏块于是给
$$
\sum_{k=0}^7\sum_{j=0}^{11}
(-1)^{k+j}\binom7k\binom{11}j
P(c+kH_c+t_0+jh_c)=0
\quad(\deg P\le17).
\tag{18}
$$
这是两次实际有限差分，步长各自保留；不是对一个已算的数值另取 signed 线性组合。

种子处 $k^0_\theta=0$，故残差没有 $\cos^4\theta$ 项。由(18)，两个 odd 项也零，得到
$$
\boxed{
\mathcal B_\theta(k_\theta^0)
=\sin^2\theta\{\cos^2\theta\,r_{22}
+\sin^2\theta\,r_{04}\}.
}
\tag{19}
$$
这是九个完整函数值的恒等式。它没有删除非local 的 period 逆、平台常数或 actual 原型基准；全部在(15)的真实系数中。

最高 $P_2$ 仍按 R437/R450 处理。其第二系数由同一包装为零，第一系数假设已支付。于是当前特解的 $P_2$ 全为零。

## 8. 前三行的真实母列：度数零、一、二

令 $F_{X,j}(u)=I_j(u,X(u,u))$。R259 完整 cubic 表与 R326(30)给
$$
\mathcal T_h^\#(u;u,u)
=-\frac{K^2F_{R,0}}{32h^4}
-\frac{\kappa K F_{R,1}}{16h^3}
+\frac{K(F_{R,2}-F_{S,2})}{32h^2}
-\frac{\kappa F_{T,1}}{16h}
-\frac{F_{Y,1}}{16}.
\tag{20}
$$
可直接核(20)：令 $p=u',r=u'',Q=K-2\kappa hx+h^2x^2$，
取原降阶 primitive
$\Psi=Q^2pr^2-xQ^2r^3/3-2he_{\rm g}Qp^2r$，
先计算 $(\partial_x+r\partial_p)\Psi$，再对 $p^2r$ 作一次紧 IBP。
全部边项含紧 profile jets，不假 $Xu^2$ 左紧。

只需其中前两幂。R327 的原母列因而为
$$
\begin{aligned}
J_{-4}(u)&=-K^2H\varepsilon F_{R,0}(u)/24,\\
J_{-3}(u)&=-\kappa KH\varepsilon F_{R,1}(u)/6
-K^2\varepsilon F_{R,0}(u)/192 .
\end{aligned}
\tag{21}
$$
而
$$
F_{R,0}(u)=-M_3(u)/3,\qquad
F_{R,1}(T_tu)=F_{R,1}(u)+tM_3(u)/3.
$$
原完整 $B$ 对角又给
$$
F_{B,0}(T_tu)
=\int\left\{
\left(-\frac a3-e(x+t)-\beta(x+t)^2\right)r^3
+\left(2e+2\beta(x+t)\right)pr^2
\right\}.
\tag{22}
$$
因此三向量
$$
v(t)=\bigl(J_{-4}(T_tu),J_{-3}(T_tu),-F_{B,0}(T_tu)\bigr)
\tag{23}
$$
的三个分量次数依次为 $0,1,2$，其最高系数分别是
$$
\frac{K^2H\varepsilon M_3}{72},\qquad
-\frac{\kappa KH\varepsilon M_3}{18},\qquad
\beta M_3 .
\tag{24}
$$
(13)与(2)使它们均非零。任意三个真实不同中心的三列遂可逆。这是逐系数三角/Vandermonde 证明，不执行新秩。

## 9. 两组 g 翻号给全相位光滑的前三行右逆

固定一个原编码角色，令 $\lambda=|b_i/a_i|$。原 high、low 角色分别有
$$
\lambda^2=1/9,\qquad \lambda^2=2,
\tag{25}
$$
均不等于 $1/3$，且 $a_i\ne0$。准确来源是 R280/R295 的 high 数据
$(R_i,T_i)=(8B_0,\pm3B_0)$、low 数据
$(-B_0/2,\pm B_0/\sqrt2)$：相应
$(a_i^2,b_i^2)=(9B_0,B_0)$ 或 $(B_0/2,B_0)$。
原完整副本共同幅度不改这个比值。

在同一十二副本族中，从两种 $g$ 符号各取三个真实不同中心。其母是同一个最终形状的平移，实际正幅平方和 $a_i^2$ 全吸入两个固定可逆矩阵 $M_+,M_-$。前三行的相位矩阵是
$$
\bigl(\zeta_+(\theta)M_+,\ \zeta_-(\theta)M_-\bigr),\qquad
\zeta_\pm=1-3(\cos\theta\pm\lambda\sin\theta)^2 .
\tag{26}
$$
$\zeta_+,\zeta_-$ 没有共同零。若同时零，二者平方之差先给
$\sin\theta\cos\theta=0$；$\sin\theta=0$ 时两者为 $-2$，
$\cos\theta=0$ 则需 $\lambda^2=1/3$，与(25)矛盾。

对任何三维右端 $y_\theta$，取这六个母列的系数
$$
\eta_\pm(\theta)=
\frac{\zeta_\pm(\theta)}
{\zeta_+(\theta)^2+\zeta_-(\theta)^2}
\,M_\pm^{-1}y_\theta .
\tag{27}
$$
它们光滑、周期并准确支付前三行。若 $y_\theta$ 含一个
$\sin\theta$ 因子，(27)也含此因子。全部支持、母形、中心和幅度已经实际存在；没有逐相位换成本或移动包。

## 10. 六个平台行的完整表与唯一几何因子

对任意最细包平台 $\chi_i$，记
$$
D_j=d_i(\theta)\mu_{i,j},\qquad
C_j=c_i(\theta)^2\mu_{i,j},\qquad
d_i=a_i^2-c_i^2,\quad c_i=a_i\cos\theta+b_i\sin\theta .
$$
R327(14)—(17)的真尾代入给
$$
P_{-4}(\chi_i)=P_{-3}(\chi_i)=H_{B,0}(\chi_i)=0.
\tag{28}
$$
其余六行准确为
$$
\begin{aligned}
P_{-2}&=\frac{K\varepsilon H}{6}D_0,\\
P_{-1}&=-\frac{K\varepsilon}{96}D_0
+\frac{K\kappa^2}{8}C_0-\frac{K\kappa H}{12}C_1,\\
P_0&=-\frac{Ha}{2}D_0+\frac{\kappa^3}{4}D_1
-\frac{K\kappa}{24}C_1
+H\left\{-\left(\frac{\varepsilon}{4}+\frac{\kappa^2}{12}\right)D_2
+\frac{\kappa^2}{12}C_2\right\},\\
P_1&=\frac{3+\kappa^2}{48}D_2-\frac{\kappa^2}{12}C_2,\\
H_{B,1}&=e(D_0+C_0),\\
H_{B,2}&=-2aD_0+2e(C_1-D_1)-2\beta D_2 .
\end{aligned}
\tag{29}
$$
这不是把 $\chi_i$ 当 gap 函数。原 $X D$ 的左右多项式差、local $T$ 的平台项以及 $X(u,1)$ 的原 sl2 作用都在(29)内。

记该常六乘六映射为 $A_6$。齐次消元依次给
$D_0=C_0=C_1=0$，再给
$$
D_1=-\frac{\beta}{e}D_2,\qquad
C_2=\frac{3+\kappa^2}{4\kappa^2}D_2 .
$$
余 $P_0$ 恰为
$$
\frac{H(1-\kappa^4-4\varepsilon)}{16K}D_2 .
\tag{30}
$$
所以(1)准确保证 $A_6$ 可逆。这里没有略去原平台尾来取得可逆性。

## 11. 两类真实角色支付因子化后的六个矩

分别选原 high、low 两个角色，并各用两种 $g$ 翻号。每组仍从原十二复制取三个真实不同中心。该角色的原 $a_i^2\mu_i$ 三列是真实三矩的可逆平移 Vandermonde；宽度只需在同角色复制内相同，high 与 low 可有不同实际宽度或最终母。

因此每组平台系数可以实现任意三向量 $w_\alpha$，其中
$\alpha=(\lambda,\epsilon)$，
$\lambda\in\{1/3,\sqrt2\}$、$\epsilon=\pm1$。对应
$$
D=\sum_\alpha d_\alpha(\theta)w_\alpha,\qquad
C=\sum_\alpha(1-d_\alpha(\theta))w_\alpha ,
$$
$$
d_\alpha(\theta)
=\sin\theta\,b_\alpha(\theta),\qquad
b_\alpha=(1-\lambda^2)\sin\theta-2\epsilon\lambda\cos\theta .
\tag{31}
$$
在 $2\times4$ 矩阵
$$
T_\theta=
\begin{pmatrix}
1&1&1&1\\
b_1(\theta)&b_2(\theta)&b_3(\theta)&b_4(\theta)
\end{pmatrix}
\tag{32}
$$
中，两行对每个相位独立。若 $\cos\theta\ne0$，同一 $\lambda$ 的两符号给不同 $b$；若 $\cos\theta=0$，两种不同的 $\lambda^2$ 给不同 $b$。故
$T_\theta^T(T_\theta T_\theta^T)^{-1}$ 是全相位光滑右逆。

现在给定含 $\sin\theta$ 因子的六行目标
$y_\theta=\sin\theta\,\bar y_\theta$。由(30)，先令
$$
(D,C)=A_6^{-1}y_\theta
=\sin\theta\,(\bar D,\bar C).
$$
用(32)逐矩分量解
$$
\sum_\alpha w_\alpha=D+C,\qquad
\sum_\alpha b_\alpha w_\alpha=\bar D .
\tag{33}
$$
(31)随即给所需真实 $(D,C)$。在种子处，$w_\alpha$ 可以非零但其总和为零；整个六行目标仍准确零。我们没有对一个任意非零右端非法除以 $\sin\theta$，而是使用(19)已付的光滑因子。

把各 $w_\alpha$ 经三矩 Vandermonde 还原为真实平台系数，就得到一个光滑周期平台组合。它属于 $\ker L_f$，且(28)保证不改已经支付的前三行。

## 12. 同一个光滑补偿支付九行及三个合法矩

由(19)，定义
$$
b_\theta=-\frac{\mathcal B_\theta(k_\theta^0)}{\sin\theta}
=-\sin\theta\{\cos^2\theta\,r_{22}+\sin^2\theta\,r_{04}\},
\tag{34}
$$
右边就是在种子处的光滑延拓。先用(27)支付 $b_\theta$ 的前三分量。该母组合的全部九行读出仍含 $\sin\theta$，因为其系数含这个因子、原行本身平滑。扣除后，后六行右端仍含 $\sin\theta$，再用(29)—(33)支付。

所得固定原核组合记为 $h_\theta$，满足
$$
L_fh_\theta=0,\qquad
\mathcal B_\theta(h_\theta)=b_\theta .
$$
于是
$$
\widetilde k_\theta=k_\theta^0+\sin\theta\,h_\theta
\tag{35}
$$
准确解同一个完整 period，并使九行全零。$h_\theta$ 光滑、周期，故(35)在 $0,\pi$ 为零。没有要求 $h_\theta$ 本身在种子零，也没有因平台组合的原间隙插值增加极点。

最高行在原整个 $\ker L_f$ 上零，所以(35)保 $P_2=0$。最后用 R461 的明确合法性投影
$$
k_\theta=\widetilde k_\theta
-\mathscr R_\theta\mathbf I(\phi_\theta,\widetilde k_\theta)
\tag{36}
$$
支付三条合法矩。原 $\mathscr R_\theta$ 同时属于 period 核及全部十端口行的核；因此(36)不改变刚支付的任何项。它也保种子和全相位光滑性。原第三 Gram 规范最后吸收 $\mathcal W_e$ 中的平方、交叉与常数，使用的是同一个 $k_\theta$。

式(35)—(36)给出真正同 collar、至少 $C^2$ 且事实上 $C^\infty$ 的相位族。所有 $x$ 函数均为原真实紧逆、母函数或固定平台的有限和；没有在任何 $p=0$ 或 $A_f=0$ 处除以 profile 导数。

## 13. 最高行、hook 与全部实际基准的范围

前述定理把最高两个特解类值设为零。对本从起点包装，R450 给第二值自动为零；原同点二十目标给
$d_f(P)=\eta\ne0$。因此在固定 signed 响应层，可用一个固定实倍
$\mathcal B_P\mathfrak H$ 改第一值，同时同步改 period 特解。这一响应保持已存在的真 range、全部内部 partial、whole $J^+$；完整成本仍属于同一个 $U$，所以 §§5—7 可对改变后的整个成本重新选取一次统一特解。不是继续沿用另一成本的十二份 range 收据。

由此，在 R459 的同宽 signed 见证上，先付最高第一值，再按本稿构造规范，可同时保 $\lambda_+=1$、$J^+=0$、全部两条真 period 与指定端口十三行。这里的 signed cost 与规范都使用同一真实母库；这仍不是 actual 增强成本截面。

对一条实际最终路径，本稿结论是条件性的规范支付定理：若其整个成本已经满足(5)、全 range 及最高第一值，那么原型自成本、M0 桥、真倒行、整数重复、后置商校正及 incoming 的全部基准都已经包含在 $V,G_d^c,G_e^c$ 中。次数界、有限差分和九行右逆作用于这些完整目标，没有把任何基准当小误差或设为零。

本稿没有证明 actual 路径可以在同时保 $J^+$、全部 partial 的前提下任意改变最高第一值；R459 固定宽度的 signed 核见证，也未因此变成一个正仿射稳定的 actual quotient。其它几何段的 ruling 仍须对(36)这同一个规范核验。

## 14. 有限选择次序与完成结论

本稿的从起点顺序为：

1. 在原 R410 cap 的固定穿零小窗内，以(7)选 $M_5=0,M_3\ne0$，冻结中心与外 cap。
2. 采用原 R455 周期核、四正常方向与一个足够大的有限周期数，精确付四 $q$ 并保(10)的非零余量。
3. 从起点固定原十二/外八宏复制、全部真实位置、幅度、宽度与共同合法窗口；选择原小安装参数并避开(1)的单一例外。
4. 在同一个四约束图册的适当小邻域内完成受限最大 $F^\star$ minor、二十 principal minor及一个有限集中根，保所有最终母第三矩非零。
5. 对同一个最终完整成本另行支付实际全 range 和最高第一值。此后才选(15)的统一真特解，作(18)的完整 odd 消去及(27)、(33)、(36)的同一个规范。

没有把极限、旧母数据或别的实际成本拼到当前结论中。新支付的是：在原明确的真 range 与最高值条件之后，全部剩余九个端口行和三个合法矩均可由一个全相位光滑的二阶规范准确完成。只需原 high/low 角色、原复制位置及一个已从起点保障的非零三次母矩；不再留下未知九行 rank 或种子 Smith 整除条件。

实际全成本增强、其余闭路径段、高阶收敛与主课题的最终几何目标仍按原范围保留。