# R617：有限pre-tanh的复极点恒等与开帽刚性

2026-11-27，Astra-new-mechanism-1f4a61a4-20261127。**纸面证明：固定有限角带的pre-tanh加任意固定有限角带post项，虽然通常具有无限角谱，仍不能作为从正半径开帽长出的准确非圆Darboux高度。** 本结论没有执行科学/符号计算，不给当前数值输入的正残差下界，也不排角带增大后真正无限自由响应的收敛极限。

它补充[R610](R610-finite-angular-height-clamp-rigidity.md)：R610的最高Fourier模证明本来不适用于无限tanh谱；这里使用另一条必要恒等——tanh的无限个复极点。最后对剩下有限post高度直接消费R610，不重复其最高模证明。

## 1. 准确范围

固定 $0<a<b\le\infty$。对每个 $c\in(a,b)$，设 $E\in C^1([a,c])$、$E>0$，$h\in C^2([a,c])$。取常数 $\sigma>0$，以及固定有限整数 $J,K$。令
$$
V(r,\theta)=\sum_{1\le |j|\le J}v_j(r)e^{ij\theta},
\qquad v_{-j}=\overline{v_j},\quad v_j\in C^2([a,c]),       \tag{1}
$$
$$
P(r,\theta)=\sum_{|k|\le K}p_k(r)e^{ik\theta},
\qquad p_{-k}=\overline{p_k},\quad p_k\in C^2([a,c]).       \tag{2}
$$
因此 $V,P$ 在实角上实值，且 $V$ 的连续角均值为0。允许任意cos/sin混合、变号以及随 $r$ 变化的相位；不要求径向解析。

定义同一真实高度
$$
Z=h+\sigma\tanh(V/\sigma)+P.                              \tag{3}
$$
假设在 $(a,b)\times S^1$ 准确满足原必要Darboux方程
$$
\mathcal D(Z;E)=
E\{Z_{rr}Z_{\theta\theta}-(Z_{r\theta}-Z_\theta/r)^2\}
+rZ_rZ_{rr}
-\frac{E'}2\{r+Z_rZ_{\theta\theta}-Z_\theta^2/r\}=0.       \tag{4}
$$
没有除以 $EZ_{\theta\theta}+rZ_r$，不要求其有固定号。$E$ 是同一候选自己的径向度量，而非另选的背景；本证明不使用turning消元或某张有限角网。

**主定理。** 若 $V(a,\theta)=0$，则 $V\equiv0$ 于 $[a,b)\times S^1$。

**开帽推论。** 若(3)在包含 $a$ 左侧的一个非空开径向帽领上为轴对称高度，且同一表示C2延续至连接带，则整条连接带的高度也轴对称。对于本题固定水平开平帽，结合R610 §5，实际等距浸入的位置也只能是由该帽确定的旋转型位置。

下文分别证明主定理和开帽推论。径向角点或核心处即使 $E$ 发散，结论只逐个内部紧区间传播；不跨未正则端点使用统一常数。

## 2. 每个固定半径有无限个真实简单复极点

固定 $r_0\in(a,b)$，且 $V(r_0,\cdot)\not\equiv0$。因均值0，它是非恒定实三角多项式。写 $z=e^{i\theta}$，则
$$
\widetilde V(r_0,z)=\sum_{j=-d}^{d}v_j(r_0)z^j,
\qquad d\ge1,\quad v_dv_{-d}\ne0.                         \tag{5}
$$
此处 $d$ 是该半径的实际最高频，允许 $d<J$。对任意复数 $w$，方程 $\widetilde V=w$ 乘 $z^d$ 后是一个次数 $2d$、首项和常数项都非零的多项式方程，因而按重数有 $2d$ 个 $z\in\mathbb C^*$ 的根。

$V_\theta=iz\partial_z\widetilde V$ 是非零Laurent多项式，其在 $\mathbb C^*$ 内只有有限个零点，因而只有有限个临界值。取tanh的极点值
$$
w_n=i\pi\sigma(n+\tfrac12),\qquad n\in\mathbb Z.         \tag{6}
$$
除去至多有限个临界值后，每个方程 $V(r_0,\theta)=w_n$ 都产生简单根 $V_\theta\ne0$。不同 $w_n$ 的根集不交，故在 $z$ 平面得到无限多个互异的有限非零点。没有把它们当成单个周期内的重复副本，也不要求这些点在 $\mathbb C^*$ 内有有限聚点。

在任一这样的点附近选择一个局部复对数，得到角坐标 $\zeta(r_0)$。系数对真实参数 $r$ 为C2，且复角导数非零；实二维隐函数定理给一个局部C2复根分支
$$
V(r,\zeta(r))=w_n.                                       \tag{7}
$$
因为tanh在每个极点的留数为1，在 $x=\theta-\zeta(r)$ 附近
$$
Z(r,\theta)=\frac{A(r)}x+H(r,x),\qquad
A(r)=\frac{\sigma^2}{V_\theta(r,\zeta(r))}\ne0.            \tag{8}
$$
$H$ 对 $x$ 解析，对 $r$ 有所需C2导数。$h$ 和有限 $P$ 在此复点解析，全部进入 $H$；它们不能取消tanh的非零留数。对固定 $\theta$ 作 $r$ 导数时，$H_r-\zeta'H_x$ 等项仍解析，不产生新的负幂。

在实角上tanh没有极点；(4)在一条实角开弧上成立。其两边都是复角的亚纯函数，故由恒等原理，(4)作为亚纯恒等式成立于整个复角域。于是每个简单极点处的全部Laurent负幂系数都必须为0。

## 3. 六阶准确消去，五阶不含有限post或背景

下面只保足以确定 $x^{-5}$ 系数的项；撇表示沿根分支的 $r$ 导数。由(8)，
$$
\begin{aligned}
Z_\theta&=-Ax^{-2}+O(1),&
Z_{\theta\theta}&=2Ax^{-3}+O(1),\\
Z_r&=A\zeta'x^{-2}+A'x^{-1}+O(1),&
Z_{r\theta}&=-2A\zeta'x^{-3}-A'x^{-2}+O(1),\\
Z_{rr}&=2A\zeta'^2x^{-3}
 +(2A'\zeta'+A\zeta'')x^{-2}+A''x^{-1}+O(1).
\end{aligned}                                             \tag{9}
$$
因此
$$
\begin{aligned}
Z_{rr}Z_{\theta\theta}
 &=4A^2\zeta'^2x^{-6}
 +(4AA'\zeta'+2A^2\zeta'')x^{-5}+O(x^{-4}),\\
(Z_{r\theta}-Z_\theta/r)^2
 &=4A^2\zeta'^2x^{-6}
 +(4AA'\zeta'-4A^2\zeta'/r)x^{-5}+O(x^{-4}),\\
rZ_rZ_{rr}&=2rA^2\zeta'^3x^{-5}+O(x^{-4}),\\
r+Z_rZ_{\theta\theta}-Z_\theta^2/r
 &=2A^2\zeta'x^{-5}+O(x^{-4}).
\end{aligned}                                             \tag{10}
$$
六阶项准确相消。所有含 $A'$ 的五阶项也相消，$A''$ 只进入四阶或更低。代(4)，五阶系数为
$$
A^2\left[2E\zeta''+
 \left(\frac{4E}{r}-E'\right)\zeta'+2r\zeta'^3\right].    \tag{11}
$$
由于 $A\ne0$，每个简单根都满足
$$
2E\zeta''+\left(\frac{4E}{r}-E'\right)\zeta'
 +2r\zeta'^3=0.                                          \tag{12}
$$
这也覆盖 $\zeta'=0$；没有除以 $\zeta'$。有限post、$h'$、$h''$ 或解析余项与奇异项交叉，最高只到三阶，故不进入(11)。留数可随 $r$ 和极点编号任意变化，其导数不影响(12)。这就是此约束不能靠有限post修正消除的原因。

## 4. 无限极点迫一个有限Laurent恒等式

在(7)的简单根上，
$$
\zeta'=-\frac{V_r}{V_\theta},\qquad
\zeta''=-\frac{
 V_{rr}V_\theta^2-2V_{r\theta}V_rV_\theta
 +V_{\theta\theta}V_r^2}{V_\theta^3}.                    \tag{13}
$$
把(13)代(12)，乘 $-V_\theta^3/2$，得到
$$
\boxed{
\Phi:=E\big(V_{rr}V_\theta^2
 -2V_{r\theta}V_rV_\theta+V_{\theta\theta}V_r^2\big)
 +\left(\frac{2E}{r}-\frac{E'}2\right)V_rV_\theta^2
 +rV_r^3=0.
}                                                        \tag{14}
$$
此前(14)只是在那些简单复根上成立。现在固定 $r_0$：$V$ 及其所有出现的导数都是角带不超过 $J$ 的Laurent多项式，所以 $\Phi(r_0,z)$ 的角带不超过 $3J$。乘 $z^{3J}$ 后为次数至多 $6J$ 的普通多项式。

第2节给无限多个互异 $z\in\mathbb C^*$，在这些点 $\Phi=0$。有限次数非零多项式不可能有无限多个不同根，因此
$$
\Phi(r_0,\theta)\equiv0                                  \tag{15}
$$
对全部实角/复角成立。这个论证不把 $V$ 的其他极点当“最高Fourier模”，也不截去tanh的无限谱。

若某个半径 $V\equiv0$，则分两种情形。它若在零集的径向内部，$V_r=0$，直接有 $\Phi=0$；否则它是非零半径的极限，由全部系数及jets的连续性，(15)仍成立。故(14)事实上在整个 $[a,b)$ 成立（边界取连续延拓）。特别在 $V\equiv0$ 的半径，(14)化为 $rV_r^3=0$，所以 $V_r\equiv0$。

## 5. 任意实符号及非唯一最大点的Gronwall

设
$$
M(r)=\max_{\theta\in S^1}|V(r,\theta)|\ge0.               \tag{16}
$$
在任意紧径向区间，$V_r$连续且角域紧，故 $M$ 局部Lipschitz、绝对连续。为处理变号和非唯一最大点，使用紧索引集 $S^1\times\{+1,-1\}$，写
$$
M(r)=\max_{(\theta,s)}sV(r,\theta),\qquad
\Gamma(r)=\{(\theta,s):sV(r,\theta)=M(r)\}.               \tag{17}
$$
对每个 $h>0$ 取一个实现 $M(r+h)$ 的索引；沿收敛子列取极限，由连续性其极限属于 $\Gamma(r)$。用对紧角域一致的C1 Taylor展开即得
$$
D^+M(r)\le\max_{(\theta,s)\in\Gamma(r)}sV_r(r,\theta).   \tag{18}
$$
这不选取一个随 $r$ 可微的最大点，也不要求最大点唯一。

若 $M(r)>0$，每个最大索引都满足 $V_\theta=0$、$sV_{\theta\theta}\le0$。代(14)得到
$$
V_r^2(EV_{\theta\theta}+rV_r)=0.                          \tag{19}
$$
因此该点要么 $V_r=0$，要么 $rV_r=-EV_{\theta\theta}$；不论取哪一根，
$$
|V_r|\le\frac{E(r)}r\|V_{\theta\theta}(r,\cdot)\|_\infty.
                                                               \tag{20}
$$
若 $M=0$，上一节已得 $V_r=0$，所以同一上导数界成立。负的绝对最大值由 $s=-1$ 完全涵盖，不需要 $V$ 固定符号。

这里只需一个显式有限带范数常数。由(1)的准确连续Fourier系数公式，$|v_j(r)|\le M(r)$；故
$$
\|V_{\theta\theta}\|_\infty
\le\sum_{1\le|j|\le J}j^2|v_j|
\le C_JM,
\qquad C_J=2\sum_{j=1}^Jj^2<\infty.                      \tag{21}
$$
由(18)–(21)，
$$
D^+M(r)\le C_J\frac{E(r)}rM(r).                           \tag{22}
$$
在任意 $[a,c]$ 上，$a>0$ 且 $E$连续，所以系数可积。由于 $M$ 绝对连续，(22)给几乎处处相同导数不等式；乘积分因子并积分，得到
$$
M(r)\le M(a)\exp\left(C_J\int_a^r\frac{E(t)}t\,dt\right).
                                                               \tag{23}
$$
$V(a,\cdot)=0$ 给 $M(a)=0$，故 $M\equiv0$ 于任意 $[a,c]$。$c<b$ 任意，主定理证毕。

## 6. 从真实开帽到整个有限组合类

若在一个开径向帽领内 $Z$ 为角常数，固定该领中的任意半径。如果此处 $V$非恒定，第2节给tanh项在 $\mathbb C^*$ 内无限多个非零留数极点，而(3)中的 $h+P$ 为有限Laurent多项式，在这些点都解析。它们不能相消成角常数，矛盾。因此领内 $V$必须为角常数；由其均值0，$V=0$。

于是C2连接给 $V(a)=0$，主定理迫全连接区 $V=0$。同时在开帽领 $P$ 为角常数，所以其全部非零Fourier系数及一阶径向导数的Cauchy数据为0。剩下高度 $Z=h+P$ 是固定有限角带并仍满足同一(4)，直接由R610 §4迫所有非零post模式恒零。其实际位置结论照R610 §5消费原水平开平帽及完整度量假设，不另作范围推广。


### 6.1 当前实际路线的帽入口与可积性

当前R571/R583/R600输入的帽边是**内侧正半径**
$$
a=r_c=11/50=.22,
$$
从 $r\downarrow r_c$ 的全平尾向**增大的 $r$**进入正文；不是 $R=.85$ 的柱/反射核心接缝。R571 §1明确在 $r\le r_c$ 置 $w=0,h=h_c$，在右侧用同一全平公式；R583对pre-tanh的2、4、6、8模给向该帽的全平延拓，R596/R600给后增有限模的同入口结论。

对应源码的旧pre-tanh bulk包络为有限全平模平方和加
$\exp[-10^{-4}/(r-r_c)^4](R-r)^{2+2\alpha}$，所以也在 $r_c$ 全平。后增bulk在 $r\le.23$ 为零，compact响应在 $r\le.226$ 为零；强迫j4在尾中只是同一全平齐次模的倍数，完整core修正远离此帽入口才开启。这些只是指出同一已声明连续输入的入口；不是重新计算或认证有限口。

可积性还可以不依赖特定全平速率直接从R576 §2的原turning定义读出。为避免与pre-tanh $V$ 混淆，把那里动能记成
$$
\mathcal V=\frac{r^2p^2}{b^2},\qquad p=Z_r,\quad
b=(r^2-Z_\theta^2)^{1/2},\quad
N=r/b+r^2pZ_{\theta\theta}/b^3.
$$
真实水平开帽的C2拼合给，均匀于角变量，
$$
p,Z_\theta,Z_{\theta\theta}\longrightarrow0,
\qquad b\longrightarrow r_c>0,
\quad N\longrightarrow1,\quad\mathcal V\longrightarrow0.
$$
对连续根 $\langle N/\sqrt{E-\mathcal V}\rangle=1$，只要靠帽处 $N>0$，其单调性给
$$
(\min N)^2\le E\le\max\mathcal V+(\max N)^2.
$$
左界由 $\mathcal V\ge0$ 直接比较被积函数；右界把右端代入turning函数即可得到函数值≤1。因此 **$E\to1$**，$E/r$在这个实际入口有界、可积。声明的准确全平输入还使该根由 $\partial_E\mathcal T=-1/2$ 的帽值光滑延拓；若直接从真实C2浸入出发，诱导径向metric自身也有相应C1拼合。

所以(23)在当前路线从 $a=.22$ 启动的近帽积分确有依据，再接内部紧区间；不是从一个未知不可积端仅凭“内部局部有界”启动。有限运行的最小采样半径约 $.221845$ 以及有限 $\alpha_M$ 口都**不是**开帽边，不在那些截断点擅自放零数据。数值DtN/ODE是否逼近该真实全平连续输入仍需原误差账；R617只排其若被完成为同一有限组合类的准确clamped根。

### 6.2 若在外侧正半径给帽数据

当前入口无需反向传播，但可把方向问题说明完整。对(17)每个活跃索引，$sV_{\theta\theta}\le0$；由(19)及 $E>0$，准确有 $sV_r\ge0$。取任一活跃索引作为 $r+h$ 的试验值，又得到与(18)相反的下界；故右导数等于活跃导数的最大值，且
$$
0\le M'_+(r)\le C_J\frac{E(r)}rM(r).
$$
于是 $M$在每个内部紧区间非减，几乎处处也有 $|M'|\le C_J(E/r)M$。若 $r=b_0>0$ 是外侧帽入口且 $M$连续趋于 $M(b_0)=0$，单调性已经迫所有 $r<b_0$ 的 $M(r)=0$；若使用双向Gronwall，则仍须明示对应端的 $E/r$可积性。此反向事实不允许在**内侧**不可积端把零极限自动传播向外；本路线内侧启动使用的是上一小节已给的 $E\to1$。

## 7. 对当前输入及后继的准确含义

当前canonical高度的非线性项为
$$
(I-Q_{512})\{\sigma\tanh(V/\sigma)\}.
$$
$Q_{512}$减去的量只是一个径向函数，可以吸收到(3)的 $h$；它不是删去tanh的无限角尾。当前pre-tanh只有2、4、6、8四个实余弦频率，post包含已付各齐次模式、强迫j4、全部有限core修正以及新增compact响应，仍为一个固定有限角多项式。因此，在其数学输入有所声明C2开帽拼合、且要求完整Darboux准确0时，本定理覆盖这个固定表示类。改变有限post次数、有限径向样条数、目标权或Jac组织，都不单独解除准确根的这一障碍。

这句话**不等于一个正的有限精度误差下界**。证明用了准确亚纯恒等和所有复极点；实角上小残差并不能无额外复域范数条件传到那些极点，也不能据此给当前run的最小η或否定其数值改善。R613完整实际S目标仍可揭示/降低真实有限误差，R615仍支付相应连续角误差预算；当前compact原scope和它们的真实读数都不因本证明被改写。

同样，本定理不排一系列post角带 $K\to\infty$、pre带 $J\to\infty$ 或真正无限独立响应，在同一固定度量及正确空间中收敛为非有限组合的准确高度。前者的极点消去可能只有在完整无穷响应里发生，不能把“每一级有限post都没有准确根”偷换成“其无限极限没有根”。后继必须明确这个无限响应/误差闭合问题，不能再仅凭tanh具有无限谱，就称当前固定有限组合已逃过所有开帽刚性。存在、固定g精化、全时间宏观幅度和reach仍须继续完成。
