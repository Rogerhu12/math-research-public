# R535：同一固定规范的负矩密度固定 d 支与统一正时长延续

日期：2026-11-16。**完整原式纸证；没有执行数值、求积、符号程序、profile、旧秩或开发检查。**

本稿接 [R534](R534-real-zero-history-entry-into-negative-matrix-density-and-fixed-gauge-continuation.md) 的真实零历史前缀，始终使用同一个 [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md) 正交母库、同一个右锚、$w=0$ 和已经固定的第三规范 $\chi^\delta$。它不借 R520/R533 的另一母库，不在接点重置 $A,T$，也不将任意负密度几何曲线视作 ruling 已付。

R534 在负极小点后已经给局部恒负 $\rho=M_{p_1}$ 分支，但没有统一其存在时长。本稿使用另一个真实输入 $d_{ss}$，其中
$$
d=h(\omega-\omega_c)-k,\qquad \rho=-kd .
$$
先用一段长度 $\delta^4$ 的平滑过渡使 $d_s=0$，随后保持 $d=d_\delta>0$。其完整 ruling 对 $h_{ss}$ 的系数在一个明确的无上界高度域内严格为负，而且只依赖 $h,d_\delta$。在本次实际入值处，大 Gram 只通过 $d_\delta\nu^\delta_1=O(\delta^3)$ 进入。因此包含全部八矩和第三历史的约化 ODE 有一个正规有限极限，给出与 $\delta$ 无关的真实正时长，以及不随 $\delta$ 缩小的高度增量。

这条延续的 $p_1$ 增量严格为负，量级为 $\delta^{10}$。进入它以前的累计仍是正的 $\pi\delta^7/4+O(\delta^9)$，所以本稿仍没有清掉总 $p_1$，更没有得到全 $M=0$。末节把沿此具体支下一步必须达到的高度尺度写明，而不把加速度系数无零误作流全局存在。

## 1. 固定原式、规范与真实入点

记
$$
y=x+\omega_c,\quad \eta=\omega-\omega_c,\quad
\gamma=h_s,\quad\upsilon=k_s,\quad
\eta_s=\frac{\upsilon}{2h},
$$
$$
d=h\eta-k,\qquad e=hy+d,\qquad Q=1+e^2.
\tag{1}
$$
物理 $x$、全部 profiles、各 copy 的真实宽度及振幅均为 R534 原值。取同一个 $S_c=(H,0,\omega_c)$，有
$$
y>0,\qquad H^2y^2>1
\tag{2}
$$
于整个固定物理区间，且有共同严格余量。

将 R521 的完整全相位式提出 $\sin^2\theta$ 后写为
$$
C_h(S)h_{ss}+C_k(S)k_{ss}
+\mathcal F(S,\gamma,\upsilon,A,T)
-\frac{1+d^2}{2h}\nu^\delta_0-d\nu^\delta_1=0.
\tag{3}
$$
这里 $\nu^\delta_2=0$，而 R534 的同一个选择是
$$
\nu^\delta_0
=2H\{\mathcal F(S_c,0,\delta^2,0,0)+c_h a_*\},
\qquad
\nu^\delta_1=\frac{2c_k}{\delta^2},
\quad a_*>0,
\tag{4}
$$
其中 $c_h=C_h(S_c)<0,c_k=C_k(S_c)>0$。
$\chi^\delta$ 只按(4)选择一次，整个新延续不再调整它。

$\mathcal F$ 是 R482 **未消第三历史**的完整余式：
$$
\mathcal F
=\mathcal R_0(S)+\mathcal R_2(S;\gamma,\upsilon)
+\mathcal L_S(AD)-\mathcal E_S(AD,AD)
-4\mathcal E_S\{\phi,T(\phi;D)\}.
\tag{5}
$$
$\mathcal R_2$ 对速度准确二次，$\mathcal L$ 对速度和 $A$ 各一次；所有项均已按 R521 的同一个正交库提出共同相位。没有在本稿用另一份库的第三外矩消去 $T$。

真实累计始终满足
$$
A_s=\Phi_{M_{\rm raw}},\qquad
T_s=-\Phi_{M_{\rm raw}}\circ A+\mathcal C_s.
\tag{6}
$$
R77/R79 的完整原式把 $\mathcal C_s$ 写成速度一次、速度乘加速度、速度三次三类，系数在合法 scalar 紧域中光滑且位于固定有限 profile 算子空间。这里保有序复合、全部原函数和左尾。

R534 给出一个实际负极小点 $s_m$。置
$$
\kappa_*=\frac{a_*\pi}{2H},\qquad
d_*=\frac{a_*\pi}{4H},\qquad
c_*=\frac{3a_*\pi}{4H^3}.
\tag{7}
$$
该点上的真实数据为
$$
\begin{aligned}
h_m&=H+O(\delta^2),&
\gamma_m&=a_*\pi\delta+O(\delta^3),\\
k_m&=\kappa_*\delta^5+O(\delta^7),&
\eta_m&=\frac{3a_*\pi}{4H^2}\delta^5+O(\delta^7),\\
\upsilon_m&=-\delta^2+O(\delta^4),&
A_m&=O(\delta),\qquad T_m=O(\delta^2).
\end{aligned}
\tag{8}
$$
因此
$$
d_m=d_*\delta^5+O(\delta^7)>0,\qquad
(d_s)_m=\eta_m\gamma_m-\upsilon_m/2
=\delta^2/2+O(\delta^4)>0.
\tag{9}
$$
所有估计在这一个固定母库的有限原算子空间中取范数。

## 2. 原加速度行给出的新全域行列式

为避免隐藏源因子，写 R521 两行中的同一个正权积分为
$$
\mathcal I_S[\psi]
=\sum_\nu w_\nu\rho_\nu^4
\int_I\psi(x)\frac{F_{u_\nu}(x;h,d)^4}{Q(x;h,d)^2}\,dx,
$$
$$
F_u=Q u''-2he u'+2h^2u,\qquad w_\nu>0 .
\tag{10}
$$
原有限正交群大小记为 $|\mathcal G|$。R521 的完整公式是
$$
C_k=\frac{|\mathcal G|}{3072h^5}\mathcal I_S[e],
\qquad
C_h=\frac{|\mathcal G|}{3072h^6}
\mathcal I_S[1+k^2-h^2(y+\eta)^2].
\tag{11}
$$
其非零性使用原非零紧母，不能将积分换成任意形式正权。

由(1)直接微分，
$$
d_s=\eta\gamma-\frac{\upsilon}{2},\qquad
d_{ss}=\eta h_{ss}-\frac{k_{ss}}2+\frac{\gamma\upsilon}{2h}.
\tag{12}
$$
联立(3)与规定的 $d_{ss}$，加速度矩阵是
$$
\begin{pmatrix}C_h&C_k\\ \eta&-1/2\end{pmatrix}.
$$
其完整行列式准确为
$$
\begin{aligned}
\mathfrak D_d
&=-C_h/2-\eta C_k\\
&=\frac{|\mathcal G|}{6144h^6}
\mathcal I_S[h^2y^2-(1+d^2)] .
\end{aligned}
\tag{13}
$$
第二等式只用 $h\eta=k+d$：
$$
h^2(y+\eta)^2-k^2-1-2h\eta(hy+d)
=h^2y^2-d^2-1.
$$
没有冻结 $\omega_s$，也没有丢掉 $k$ 的真实水平贡献。

于是，在明确域
$$
\boxed{h>0,\quad y>0,\quad
hy>\sqrt{1+d^2}\quad(x\in I)}
\tag{14}
$$
内，$\mathfrak D_d>0$。由于 $F_u\not\equiv0$，严格性成立。它是当前 scalar 的原系数结论，与 $A,T,\chi$ 的大小无关。

记
$$
\boxed{
B(h,d)=2\mathfrak D_d
=\frac{|\mathcal G|}{3072h^6}
\sum_\nu w_\nu\rho_\nu^4
\int_I\{h^2y^2-(1+d^2)\}
\frac{F_{u_\nu}^4}{Q^2}\,dx>0 .
}
\tag{15}
$$
$e,Q,F_u$ 只含 $h,d$，所以 $B$ 确不依赖另一个曲线参数，也不依赖累计历史。由(2)，在(8)附近有一个与 $\delta$ 无关的合法紧盒及 $B\ge b_0>0$。

## 3. 长度 $\delta^4$ 的实际平滑刹停

继续原 R534 真解一个足够短的区间，记其真实 $d$ 为 $d_{\rm old}$。取一个固定光滑 cutoff $\vartheta$，在 $0$ 附近为1、在1附近为0，且 $0\le\vartheta\le1$。令
$$
\ell_\delta=\delta^4,
$$
并定义一个真实目标导数及其积分：
$$
\widehat d_s(s_m+t)=\vartheta(t/\ell_\delta)
(d_{\rm old})_s(s_m+t),
$$
$$
\widehat d(s_m+t)
=d_m+\int_0^t\widehat d_s(s_m+\tau)\,d\tau,
\qquad 0\le t\le\ell_\delta .
\tag{16}
$$
原 rescaled 解在这个区间仍存在；$\ell_\delta$ 远小于 R534 已控制的末端 $\delta^3$ 尺度。其导数满足
$$
|(d_{\rm old})_s|\le C\delta^2,\qquad
|(d_{\rm old})_{ss}|\le C
$$
即可完成以下估计；不需要假定一个并未支付的全路径 $C^3$ 小量。

给输入 $u=\widehat d_{ss}$。则
$$
|u|\le C\delta^{-2}+C,\qquad
\int_{s_m}^{s_m+\ell_\delta}|u|\,ds\le C\delta^2.
\tag{17}
$$
这里明确允许加速度达到 $\delta^{-2}$。小的是积分效应，不是 $C^1$ 控制范数。

用(3)(12)(13)求实际 $h_{ss},k_{ss}$，并同时积分真实水平和(6)。实际 $d$ 与 $\widehat d$ 具有相同的值、一导和二导，故在解存在时准确相同。初段 cutoff 为1，唯一性使整条新解与原解逐 germ 相同；末段 cutoff 为0，则 $d$ 已经准确为常数且全部正阶导数为零。

还需实际支付存在及累计界。以下在固定(14)紧盒内作 bootstrap：
$$
|\gamma|+|\upsilon|\le C\delta,\quad
\|A\|\le C\delta,\quad \|T\|\le C\delta^2.
$$
由 $\widehat d=O(\delta^5)$，大 Gram 项满足
$$
|\widehat d\,\nu^\delta_1|=O(\delta^3).
\tag{18}
$$
(5)全部原项因而有一致有限界。两个加速度满足
$$
|h_{ss}|+|k_{ss}|\le C(1+|u|).
\tag{19}
$$
逐项积分得
$$
\Delta\gamma,\Delta\upsilon=O(\delta^2),\qquad
\Delta h=O(\delta^5),\quad
\Delta k,\Delta\eta=O(\delta^6).
\tag{20}
$$
原 $M_{\rm raw}$ 在这个盒内至多速度二次，故
$$
\|\Delta A\|=O(\ell_\delta)=O(\delta^4).
\tag{21}
$$

对完整第三累计，不能仅由(17)称它很小。逐类估计是
$$
\begin{array}{c|c}
\text{原完整来源}&\text{在此过渡段的积分界}\\ \hline
-\Phi_{M_{\rm raw}}\circ A&O(\delta^5)\\
\mathcal C^{[1]}\text{ 的速度一次项}&O(\delta^5)\\
\mathcal C^{[3]}\text{ 的速度三次项}&O(\delta^7)\\
\mathcal C^{[3]}\text{ 的速度乘加速度项}
&O\!\left(\delta\int(1+|u|)\,ds\right)=O(\delta^3).
\end{array}
\tag{22}
$$
所以
$$
\boxed{\Delta T=O(\delta^3).}
\tag{23}
$$
这些界关闭 bootstrap，给整个实际长度 $\ell_\delta$ 上的存在，并保持(14)的共同余量。高阶时间导数可以变大，但每个固定 $\delta>0$ 的解、规范和全部场都光滑；未把它们伪称一致 $C^\infty$ 小扰动。

因(8)(20)，$\gamma$ 保持严格正，$k$ 保持严格正；$\widehat d>0$。整个过渡段准确有 $\rho=-k\widehat d<0$。没有在切换中插入一段未经记账的正或负路径。

## 4. 实际末值与固定 d 曲线

将过渡末端作为新时间 $t=0$。以下下标0均为该真实末值，不是另选初值。由上节，
$$
\begin{aligned}
h_0&=H+O(\delta^2),&
\gamma_0&=a_*\pi\delta+O(\delta^2)>0,\\
k_0&=\kappa_*\delta^5+O(\delta^6)>0,&
d_\delta&=d_*\delta^5+O(\delta^6)>0,\\
A_0&=O(\delta),&
T_0&=O(\delta^2).
\end{aligned}
\tag{24}
$$
末 germ 中 $d_s=0$，所以 $\upsilon_0=2\eta_0\gamma_0$。定义一个实际正数
$$
c_\delta=\frac{k_0+d_\delta}{h_0^2}
=c_*\delta^5+O(\delta^6)>0 .
\tag{25}
$$
以后保持 $d=d_\delta$。由水平关系，
$$
\eta_s=\frac{k_s}{2h},\qquad
k=h\eta-d_\delta
$$
给 $h\eta_s=\eta h_s$。因此整条实际支准确满足
$$
\boxed{
\eta=c_\delta h,\qquad
k=c_\delta h^2-d_\delta,\qquad
\upsilon=2c_\delta h\gamma .
}
\tag{26}
$$
它不是任意重新指定的几何；(26)由真实入值、固定 $d$ 输入和原水平方程共同得到。

只要 $h\ge h_0$，就有 $k\ge k_0>0$，从而
$$
\boxed{\rho=-d_\delta k\le-d_\delta k_0<0.}
\tag{27}
$$
这个分支与 R534 的恒 $\rho$ 曲线不同：这里负密度随高度增加而变得更负。

## 5. 完整 ruling 的正规约化

由(26)，
$$
k_{ss}=2c_\delta h\,h_{ss}+2c_\delta\gamma^2 .
$$
将它代回原(3)，有
$$
C_h+2\eta C_k=-B(h,d_\delta).
$$
故真正的高度方程是
$$
\boxed{
h_{ss}=
\frac{
\mathcal F(S,\gamma,2c_\delta h\gamma,A,T)
-\nu^\delta_0(1+d_\delta^2)/(2h)
-g_\delta
+2c_\delta C_k(h,d_\delta)\gamma^2
}{B(h,d_\delta)},
}
\tag{28}
$$
$$
S=(h,c_\delta h^2-d_\delta,\omega_c+c_\delta h),
\qquad
g_\delta=d_\delta\nu^\delta_1=O(\delta^3).
\tag{29}
$$
$C_k$ 也由(11)只依赖 $h,d_\delta$。分母在(14)内不为零，全部历史仍在(28)中。

在(28)之后继续原完整演化：
$$
A_s=\Phi_{M_{\rm raw}(S,\gamma,2c_\delta h\gamma)},
$$
$$
T_s=-\Phi_{M_{\rm raw}}\circ A+
\mathcal C_s\!\left(
S,\gamma,2c_\delta h\gamma,
h_{ss},2c_\delta h h_{ss}+2c_\delta\gamma^2
\right).
\tag{30}
$$
因此状态 $(h,\gamma,A,T)$ 的闭合系统是原有限维光滑 ODE。这里没有要求 $T$ 在某个商里为零，也没有只保其端点势。

最关键的消奇异范围是明确的：$\chi^\delta$ 在完整 ruling 中只有(3)所列线性配对；沿固定 $d$ 支，$\nu^\delta_1$ 只通过 $g_\delta$ 出现。$\mathcal C_s$ 和原 $M_{\rm raw}$ 不依赖这一固定齐次第三规范。故以
$$
(d_\delta,c_\delta,\nu^\delta_0,g_\delta)
$$
为参数时，(28)(30)在一个固定合法紧盒附近是普通光滑系统，且
$$
(d_\delta,c_\delta,\nu^\delta_0,g_\delta)
\longrightarrow(0,0,\nu^0_0,0),
\quad
\nu^0_0=2H\{\mathcal F(S_c,0,0,0,0)+c_h a_*\}.
\tag{31}
$$

这不声称 $\chi^\delta$ 作为 profile 有有限极限。它只有在本次完整 ruling 配对中的作用已按原式写成有限参数。对每个固定 $\delta>0$，物理第三、第四字段的原规范幅度仍须完整保存。

## 6. 不随小参数缩短的真实负累计时间

(24)的约化初值趋于
$$
h=H,\qquad \gamma=0,\qquad A=T=0.
$$
在(31)的极限参数下，(28)在起点准确给
$$
h_{ss}(0)
=\frac{-c_h a_*}{-c_h}=a_*>0.
\tag{32}
$$
所以先取极限完整 ODE 的一个固定短解，再缩小一个固定 $T_*>0$，使其留在(14)的紧邻域，并有
$$
a_*/2<h_{ss}<2a_*
$$
于 $0\le t\le T_*$。普通 ODE 的参数连续依赖与(24)(31)于是给：对全部充分小的实际 $\delta>0$，同一个 $T_*$ 上都存在真实解，保同一合法域，并可取
$$
\boxed{a_*/2\le h_{ss}\le2a_* .}
\tag{33}
$$
完整 $A,T$ 同时在这个固定紧状态盒内；不是只证明 scalar 几何存在以后再假设历史可延拓。

由 $\gamma_0>0$，
$$
h(t)\ge h_0+\gamma_0t+\frac{a_*t^2}{4},\qquad
\gamma(t)\ge\gamma_0+\frac{a_*t}{2}.
\tag{34}
$$
特别 $h(T_*)-H$ 有一个严格正的、与 $\delta$ 无关的下界。该真实高度弧已经离开随 $\delta$ 收缩的中心邻域。

在整个固定时长上，(27)给
$$
\boxed{
\Delta m_{p_1}
=-d_\delta\int_0^{T_*}(c_\delta h(t)^2-d_\delta)\,dt
\le-c_1T_*\delta^{10}<0
}
\tag{35}
$$
其中可取某个固定 $c_1>0$。例如由
$\kappa_*d_*=a_*^2\pi^2/(8H^2)>0$，充分小 $\delta$ 下可取其一半。

若 $h_*(t)$ 表示(31)(32)的完整极限解，则还有准确的有限极限
$$
\delta^{-10}\Delta m_{p_1}
\longrightarrow
-d_*\int_0^{T_*}\{c_*h_*(t)^2-d_*\}\,dt<0.
\tag{36}
$$
因为 $h_*(t)\ge H$ 且 $c_*H^2-d_*=\kappa_*>0$，右端严格负。此式保留真实极限高度，而没有将它换成一个只在起点正确的二次近似。

原全相位 $K=0$ 在过渡和固定 $d$ 两段一直成立。frame、位置、第三场、第四场及全部成本按原恢复继续；没有新的实际验收或无限时间断言。

## 7. 哪些系数无退化，哪些全局问题仍在

对一个最终固定的 $\delta$，(15)表明固定 $d_\delta$ 支的完整加速度系数在
$$
h>\frac{\sqrt{1+d_\delta^2}}{\min_{x\in I}y}
\tag{37}
$$
的整个高度域不为零。这个域没有高度上界。并且(26)给 $e=hy+d_\delta>0$、$y+\eta>0$；当 $k,d_\delta>0$ 时，原强合法性也由
$$
h^2(y+\eta)^2-k^2-1
=h^2y^2-1+2hy(k+d_\delta)+2kd_\delta+d_\delta^2>0
$$
保持。

(37)只排除了“这一加速度行在大高度处必然退化”这一种故障。它不排除完整 ODE 的有限时间爆破、速度或历史增大，不能据此称任意长负累计已经存在。

R73 在固定 $d_\delta$ 曲线上另外给一个很具体的原矩公式：
$$
\boxed{
8M_{t_1}
=c_\delta^2h^4-(1+d_\delta^2)-(\gamma/h)^2 .
}
\tag{38}
$$
其来源是原
$8t_1=h\,a_1-\gamma^2/h^2$，
$a_1=2k\eta-(k^2+1)/h$，代(26)后
$h\,a_1=c_\delta^2h^4-(1+d_\delta^2)$。
因此本稿的固定有限高度段上，$t_1$ 仍严格负；全部八矩义务没有因为 $p_1$ 出现负增量而消失。

若以后仅沿此具体支希望取得非负的 $t_1$ 密度，至少必须真正达到
$$
h\ge c_\delta^{-1/2}(1+d_\delta^2)^{1/4},
\tag{39}
$$
并支付(38)里的真实速度项。由(25)，这个高度尺度为
$\delta^{-5/2}$。这给后继实际延续一个明确目标，不把单纯的系数非退化当成该目标已经可达。

## 8. 总账与下一步

R534 的完整正前缀、当前过渡和新固定 $d$ 段属于同一实际路径，使用同一个 $\chi^\delta$。把入点从原首零移到负极小点只改变更高阶小量；过渡的 $p_1$ 积分为 $O(\delta^{14})$。因此加入本稿统一时长段以后，整个累计仍有
$$
\boxed{
m_{p_1,\mathrm{total}}
=\frac{\pi}{4}\delta^7+O(\delta^9)>0 .
}
\tag{40}
$$
(35)是真实负增量，(40)同样是真实总值；二者不能互相替代。

本稿新增的是：负区的真实延续时长可以不随 $\delta$ 缩短，且在同一固定规范下可以取得有限幅的高度变化；完整第三历史跨越 $\delta^{-2}$ 加速度切换也有逐项可审计的界。它不是全矩阵返回。下一个具体问题是从(28)(30)继续，或在同一规范内改变已经获得的 $d$ 控制，取得足以抵消正前缀的负累计，并联立其余七矩、端 germs、pose 和完整 period。不得用无 ruling 桥、另一母库或另一段单独重选的规范填补这一步。

### 原来源与核验范围

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：原八矩、真实水平关系和有序第三累计；
- [R77](R77-weight-three-local-operator-actual-finite-controllability.md)、[R79](R79-closed-horizontal-C1-control-and-endpoint-potential.md)：完整第三密度的一／三导数权；这里只使用原式，不使用未受当前 ruling 限制的桥；
- [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md) 未消历史的原式：完整 $\mathcal F$、固定 $\chi$ 的唯一线性配对和真实加速度；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：两条完整加速度积分及同一正交库；
- [R534](R534-real-zero-history-entry-into-negative-matrix-density-and-fixed-gauge-continuation.md)：真实零历史前缀、负极小点及全部入值尺度。

本稿只作原式与普通有限维 ODE 的纸面推导；没有生成或执行任何新科学程序。

独立核验：root与mechanism已分别核对原加速度行列式、δ⁴切换的L¹界及υ改进、完整第三ΔT=O(δ³)、正规参数极限和t₁必要高度式；均为纸面推导，没有执行科学代码。δ⁶的Δk、Δη先用(19)积分将υ改进至O(δ²)，不只用最初O(δ) bootstrap。
