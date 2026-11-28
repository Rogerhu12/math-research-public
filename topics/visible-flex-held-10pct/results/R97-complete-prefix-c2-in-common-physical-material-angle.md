# R97：同一物理材料角的完整 Cartesian 前缀与切口 C² 差界

**可信度：已证明的条件命题。** 对下述相同完整固定问题的两个真实积分场，完整系数及核心/角图的给定严格界推出六个空间二jet的全域差界；没有证明当前已经算出一个真实fixed pair、Cauchy序列或精确等距极限。

本结果保留全部Cartesian模式、有限mean、真实核心lift、中心与切口修补，并比较相同物理材料角而非相同计算角。各场的原actual-DN和完整metric/geometry责任不被此条件命题替代。

## 1. 比较对象、坐标与未支付范围

比较两场 $i\in\{L,R\}$ 的**同一个完整固定问题**，允许它们的径向网格、
全部有限 Fourier 模式数和 support 系数不同。冻结的量包括完整物理 $g$、
$\lambda,S,b,k$、gauge $q$、原角图、真实物理径向端点、有限 mean 的节点数及
GL6 规则。两场各自的 actual-DN/full-height 接受和最终 physical-H 绑定仍用原门。
参数 $p_0$ 改变的是实际 support 幅度，不能把它与冻结的 gauge $q$ 混同。

精确 Cartesian 表示写成

$$
X_i(s,\psi)=C_i(s,\psi)+h_i(s)L_i(\psi)
 +\sum_{j=0}^2W_j(s)D_{i,j}(\psi)
 +\sum_{j=0}^2U_j(s)A_{i,j}(\psi). \tag{1}
$$

$C_i$ 是保存的完整 Cartesian/Fourier 共享二 jet quintic；它包含完整有限 mean。
$h_i$ 是完整核心 lift 的共享 quintic。$W_j$ 是原中心修补权，$U_j$ 是原切口修补权。
$L_i,D_{i,j}$ 用下文的同一个真实积分核心。$A_{i,j}$ 保留完整尾的全部 planar、
height 和零模式，不能只保留原前缀的低模。

源 `angular_chart` 相同并不推出有限共享 quintic $e_L(s)=e_R(s)$。
`PhaseAngleChart` 在各自真实 `prefix.rep.x` 上重建 $e_i$，因此比较必须使用

$$
\theta=\psi_i-\frac{e_i(s)}3\sin(3\psi_i),\qquad
F_i(s,\theta)=X_i(s,\psi_i(s,\theta)). \tag{2}
$$

所求是同一 $(s,\theta)$ 下的六个差
$\Delta F,\Delta F_s,\Delta F_\theta,\Delta F_{ss},
\Delta F_{s\theta},\Delta F_{\theta\theta}$，不是同一计算角 $\psi$ 下的差。
本条不做自由刚体、相位、高度或核心中心配准。

这一有限对上界不等于 Cauchy 性或到无穷维精确等距解的误差；完整尾、柱和帽的
比较仍有各自责任。已有独立各场完整 metric/geometry 证书不因本条而失效。

## 2. 真实积分核心与有限 Gauss 查询必须区分

[`actual_cartesian_prefix.py`](../scripts/resume_20261128/tail/actual_cartesian_prefix.py)
的 `ActualR53CartesianPrefix` 类说明已经明确：数学核心是 R53 的真实 phase/position
积分；`core.evaluate` 是原有限数值积分查询。两个事实不能混用：

1. 有限 Gauss 位置公式的导数，不会仅凭另外返回的 `Ft,Ftt` 就等于后者。
2. 连续证书确实没有这样假定。

第二点的直接源码链是
`cartesian_prefix_interval_geometry.AngularRanges`
$\to$ `warm_phase_validated_core.build_oracle` 的零 phase 专化。
`cartesian_prefix_metric_tables.MetricAngularRanges.data` 用同一个真实
$\Gamma,\Gamma_u,\Gamma_{uu},\Gamma_{uuu},\Gamma_{uuuu}$ 同时组成完整 lift
和中心修补。其 `anchor_support_exact`、$S,b,k,\lambda$ 都是实际源的字面有理数；
完整 `phase_controls_exact` 为零。它没有把旧 phase 控制加入原 support 族。

保存的 `rep.jets`、mean 系数和 `source_initial` 均作为字面有限系数处理。
特别是 `source_initial` 只定义一个有限三角多项式 $P_i$，不假定它等于真实核心的
精确 Fourier 投影。因此连续核验直接作用于式 (1) 的真实积分场：
真实 $\Gamma$ 与有限 $P_i$ 之间的差已经出现在被围住的 $L_i$ 和 $D_{i,j}$ 中。
从有限 BVP 残差到真实核心的未经证明误差传递没有被使用。

尚须区别的是数值 `evaluate`/mesh 点查询到式 (1) 的误差，见第 9 节。
下文所有 $C^2$ 上界先针对真实积分定义的式 (1)，不冒称对浮点点查询函数已证
同样的导数恒等。

## 3. 同一材料 $u$ 的 support 逆映射差

把较短系数表补精确零，令 $m_j=3j$，

$$
b_{i,j}=(1-m_j^2)a_{i,j},\quad
\rho_i(\varphi)=1+\sum_jb_{i,j}\cos(m_j\varphi),\quad
U_i(\varphi)=\varphi+\sum_j\frac{b_{i,j}}{m_j}\sin(m_j\varphi).
$$

$\Phi_i=U_i^{-1}$ 是原核心的 normal-angle inverse。
目前已绑定的真核心 oracle 本来就要求 $A_i=\sum_j|b_{i,j}|<1$。
取

$$
r=1-\max_i A_i>0,\quad
B_\ell=\max_i\sum_jm_j^\ell|b_{i,j}|,\quad
D_\ell=\sum_jm_j^\ell|b_{R,j}-b_{L,j}|.
$$

由 $U_i'\ge r$ 的全实轴单调性，

$$
\|\Phi_R-\Phi_L\|_\infty
\le d_\varphi:=\frac1r\sum_j\frac{|b_{R,j}-b_{L,j}|}{m_j}. \tag{3}
$$

该式是在相同材料 $u$ 比较，而不是把相同 normal angle 当成相同材料点。
在各自的 $\Phi_i(u)$ 处，令

$$
d_\ell=D_\ell+B_{\ell+1}d_\varphi\qquad(\ell=0,1,2).
$$

于是 $|\Delta\rho|\le d_0$，$|\Delta\rho_\varphi|\le d_1$，
$|\Delta\rho_{\varphi\varphi}|\le d_2$。
由原恒等式

$$
\kappa_0=\rho^{-1},\quad
(\kappa_0)_u=-\rho_\varphi\rho^{-3},\quad
(\kappa_0)_{uu}=-\rho_{\varphi\varphi}\rho^{-4}
 +3\rho_\varphi^2\rho^{-5}
$$

得到完整差界

$$
\begin{aligned}
\delta K_0&=d_0/r^2,\\
\delta K_{0,1}&=d_1/r^3+3B_1d_0/r^4,\\
\delta K_{0,2}&=d_2/r^4+4B_2d_0/r^5
 +6B_1d_1/r^5+15B_1^2d_0/r^6. \tag{4}
\end{aligned}
$$

式 (4) 的 $4,6,15$ 项来自完整乘积差；不得漏掉同材料逆角变化的 $B_{j+1}d_\varphi$。

## 4. 同参数真实 flattening 的 $\beta$ 与 phase 差

取 $L=\pi/3$、$z\in[0,L]$，并记

$$
v_i(z)=\Phi_i(L+z)-L,\quad
C(z)=\int_0^z(1-W(t))\,dt,\quad c=S+b/2,\quad D=L-c.
$$

原 window 满足 $W(0)=0,W(L)=1,W'\ge0$，而
$C(L)=c$、$\int_0^LW'=1$。
真实归一化为

$$
\beta_i=\frac{\int_0^LW'(z)v_i(z)\,dz-kc}{D}. \tag{5}
$$

这就是 R95 已使用的正权积分恒等式，这里只用它比较两场，不重新求其数值证书。
固定 $S,b,k$ 后，

$$
|\Delta\beta|\le d_\varphi/D.
$$

代码用 R94 已证的有理 $\pi_->0$ 取 $D_-=\pi_-/3-S-b/2>0$，
以 $d_\varphi/D_-$ 替代；没有把 finite GL12/24 的浮点 `beta` 当成真实积分。

令 $q(z)=(z-C(z))/D$。因为 $q'=W/D\ge0$ 且 $q(0)=0,q(L)=1$，
有 $0\le q\le1$。对原 $\omega$ 分部积分，把归一化项和部分积分**一起**比较：

$$
\begin{aligned}
\Delta\phi_\lambda(L+z)
={}&(1-\lambda+\lambda W(z))\Delta v(z)\\
&+\lambda\left[q(z)\int_z^LW'\Delta v
 -(1-q(z))\int_0^zW'\Delta v\right]. \tag{6}
\end{aligned}
$$

右边对 $\Delta v$ 的总绝对质量不超过

$$
1-\lambda+\lambda W
 +\lambda[q(1-W)+(1-q)W]
=1-\lambda+\lambda q+2\lambda(1-q)W\le1+\lambda.
$$

原反射和三重周期将此界延伸到全实轴。因此

$$
\|\Delta\phi_\lambda\|_\infty
 \le d_\phi:=(1+\lambda)d_\varphi\le2d_\varphi. \tag{7}
$$

这是共同真实 $\beta$ 定义产生的抵消，不能把两个独立有限求积的浮点 `beta`
代入后继续引用。两场同 $\lambda,S,b,k$、`curvature_blend=1`、同材料原点是必要条件。

令 $W_1=630/(256b)$、$W_2=2520/(64b^2)$。原曲率公式给

$$
\begin{aligned}
\delta K&=\delta K_0+\lambda\delta\beta,\\
\delta K_1&=\delta K_{0,1}+\lambda W_1(\delta K_0+\delta\beta),\\
\delta K_2&=\delta K_{0,2}+2\lambda W_1\delta K_{0,1}
 +\lambda W_2(\delta K_0+\delta\beta). \tag{8}
\end{aligned}
$$

不另用采样取 $K, K_1$：可由 $r,R=1+\max A_i$ 取

$$
\begin{gathered}
B_\beta=\frac{c\max(|r^{-1}-k|,|R^{-1}-k|)}{D_-},\\
K=\max(k,r^{-1})+\lambda B_\beta,\qquad
K_1=B_1/r^3+\lambda W_1(r^{-1}+k+B_\beta).
\end{gathered}
$$

这些是便于复算的保守全域界，不冒充 R91 的更紧曲率预算。

## 5. 真核心位置、三 jet 与入口角图

真实核心固定在原三重旋转中心，不能另加未知平移。
对 $T=2\pi/3$，

$$
(e^{iT}-1)\Gamma_i(u)=\int_u^{u+T}i e^{i\phi_{\lambda,i}(v)}\,dv.
$$

因 $|e^{iT}-1|=\sqrt3$，并用 $\pi<22/7,\sqrt3>5/3$，

$$
\delta G_0=\frac{44}{35}d_\phi,\quad
\delta G_1=d_\phi,\quad
\delta G_2=\delta K+Kd_\phi,\quad
\delta G_3=\delta K_1+2K\delta K+(K_1+K^2)d_\phi \tag{9}
$$

分别围住同 $u$ 的 $\Gamma,\Gamma_u,\Gamma_{uu},\Gamma_{uuu}$ 差。
式 (9) 最后一项由 $\Gamma_{uuu}=-\kappa_u n-\kappa^2t$ 得出。

入口图 $\theta_0(\psi)=\psi-E_0\sin(3\psi)/3$ 在同固定问题中相同。
取 $r_0=1+|E_0|,r_1=3|E_0|$，则组合后的前三项差界为

$$
\delta\widetilde G_0=\delta G_0,\quad
\delta\widetilde G_1=r_0\delta G_1,\quad
\delta\widetilde G_2=r_0^2\delta G_2+r_1\delta G_1. \tag{10}
$$

组合 $\Gamma_u\circ\theta_0$ 的 $0,1,2$ 阶差则依次为
$\delta G_1,r_0\delta G_2,r_0^2\delta G_3+r_1\delta G_2$。
足够组成中心第二径向 jet 的完整角二 jet。

## 6. 所有有限系数、核心 lift、中心和切口一起比较

对每场的字面 nodal 二 jet 用原精确 `hermite` 公式，合并两场全部实际径向节点，
另加入两处修补的精确边界。每个共同小区间先把两个原 quintic 限制到同一单位区间，
再**相减后**转 Bernstein；不先取绝对值，不改网格，也不把浮点 PPoly 系数重新称为
精确共享二 jet。

所有 planar/height 模式并集均保留；缺少的模式补精确零。对角阶 $b$，
每个系数的 Bernstein 上界乘 $|m|^b$，再对全部模式相加，给 Cartesian 向量欧氏范数
的上界。零模式在 $b=0$ 时仍保留。这里包括全部 finite mean，而不是另行平移对齐高度。

入口有限投影可精确写成

$$
P_i(\psi):\quad
c_1=q r_{0,i},\qquad c_{1+3j}=q(r_{j,i}+t_{j,i})/2,\qquad
c_{1-3j}=q(r_{j,i}-t_{j,i})/2,\qquad z_{3j}=qz_{j,i}.
$$

$q$ 和保存向量的乘积按实有理乘法处理，不把一次浮点乘积重新冻结为另一个定义。
因为入口 circle 项相同，

$$
\delta L_b\le\delta\widetilde G_b+\delta P_b\qquad (b=0,1,2). \tag{11}
$$

原中心目标为
$T_0=\Gamma\circ\theta_0,T_1=e_z,T_2=b_0(\psi)\Gamma_u\circ\theta_0$，
其中 $b_0=-E_{pp}\sin(3\psi)/3$。
它的角二 jet 用式 (10) 和 Leibniz 法则，系数界为
$|E_{pp}|/3,|E_{pp}|,3|E_{pp}|$。
由

$$
D_{i,j}=T_{i,j}-C_{i,s^j}(0,\psi)-h_i^{(j)}(0)L_i
$$

得到 $\delta D_{j,b}$，其中 $h_i^{(j)}(0)$ 的实际差必须保留。
不假设 lift 的入口三项恰好是某个理想数组。

切口使用每场真实 `complete_cut_coefficients` 的完整 outward coefficient intervals。
它们来自各自最终 physical-H、同 $R,w,w_R$ 的实表达式、真实尾全模和完整 mean。
对区间 $[l_-,l_+]$、$[r_-,r_+]$，差严格落在
$[r_- -l_+,r_+-l_-]$；再按完整模式及角导数求和得到 $\delta A_{j,b}$。
独立区间相减会留下算术宽度底，本条如实保留，不能仅因区间数组接近就将其抹掉。
切口 height 零模的第零项在原公式中**代数上精确为零**，一、二阶 mean 项照常保留。

同一 $\psi$ 的完整差界于是是

$$
d_{a,b}\le\delta C_{a,b}
 +H_a\delta L_b+\delta h_a\,\mathcal L_b
 +\sum_j|W_j^{(a)}|\delta D_{j,b}
 +\sum_j|U_j^{(a)}|\delta A_{j,b},\quad a+b\le2. \tag{12}
$$

$H_a$ 是两场 $|h_i^{(a)}|$ 的共同上界；$\delta h_a$ 来自完整共享 quintic 差。
$\mathcal L_b$ 和各场中心角三 jet 的绝对上界直接取自各自已完成的真核心角区间表。
这些是**全部闭角盒**的向量界；欧氏范数在三重旋转下不变，所以一个完整扇区的界
覆盖全圆。不是 sampled maximum。

同理直接从式 (1) 给各场绝对 $M_{a,b}$，除六个二 jet 外只需
$M_{2,1},M_{1,2},M_{0,3}$。不要求径向三阶导数跨 Hermite 接点连续。

## 7. 完整逆角图二 jet：不能漏掉 $\Delta e$ 和混合项

在一个共同径向区间上，令

$$
E_j\ge\max_i\sup|e_i^{(j)}|,\quad
\delta e_j\ge\sup|e_R^{(j)}-e_L^{(j)}|,\qquad r_e=1-E_0>0.
$$

这些量都从字面共享 quintic 的精确 Bernstein 界取得。
全实轴单调逆映射保证同一个 $\theta$ 的连续 lift 满足

$$
|\psi_R-\psi_L|\le d_\psi=\delta e_0/(3r_e). \tag{13}
$$

没有使用模 $2\pi$ 的不连续减法。
令 $s_3=\sin(3\psi),c_3=\cos(3\psi),\rho=1-e c_3$，则

$$
\begin{aligned}
u:=\psi_s&=e' s_3/(3\rho),&v:=\psi_\theta&=1/\rho,\\
a:=\psi_{ss}&=(e''s_3/3+2e'c_3u-3e s_3u^2)/\rho,\\
b:=\psi_{s\theta}&=(e'c_3-3e s_3u)/\rho^2,&
c:=\psi_{\theta\theta}&=-3e s_3/\rho^3. \tag{14}
\end{aligned}
$$

式 (14) 由对式 (2) 做隐式微分得到；是同一 chart 的全部二 jet。
对两场相应角点，取
$d_t=\min(2,3d_\psi)$，则 $|\Delta s_3|,|\Delta c_3|\le d_t$，
$|\Delta\rho|\le\delta e_0+E_0d_t$，并有

$$
|\Delta(1/\rho)|\le(\delta e_0+E_0d_t)/r_e^2.
$$

代码的 `Pair(A,d)` 表示两边的绝对值不超过 $A$、差不超过 $d$。
乘法规则

$$
(A,d)\cdot(B,e)=(AB,Ae+Bd) \tag{15}
$$

由 $xy-\widetilde x\widetilde y=(x-\widetilde x)y+
\widetilde x(y-\widetilde y)$ 直接成立。
按式 (14) 保留全部项后使用式 (15)，得到 $u,v,a,b,c$ 的绝对界与差界。
代码为求上界把符号取绝对值，并未改变式 (14) 的数学定义。

## 8. 六个物理二 jet 的完整传递

先把两场在不同 $\psi_i$ 处的 Cartesian jet 对齐。由角向中值定理，

$$
\|X_{R,s^a\psi^b}(s,\psi_R)-X_{L,s^a\psi^b}(s,\psi_L)\|
\le d_{a,b}+M_{a,b+1}d_\psi. \tag{16}
$$

所需角向下一阶全部来自本条第 6 节的完整绝对三 jet，包含真实核心、中心与切口。
随后对

$$
\begin{aligned}
F_s&=X_s+X_\psi u,&F_\theta&=X_\psi v,\\
F_{ss}&=X_{ss}+2X_{s\psi}u+X_{\psi\psi}u^2+X_\psi a,\\
F_{s\theta}&=X_{s\psi}v+X_{\psi\psi}uv+X_\psi b,\\
F_{\theta\theta}&=X_{\psi\psi}v^2+X_\psi c \tag{17}
\end{aligned}
$$

逐项用式 (15)，即得六个同物理角差界。式 (17) 中每个 mixed/chart 项都保留。
逐共同区间取最大，得到全 $[0,s_{\rm end}]\times\mathbb R/(2\pi\mathbb Z)$ 的界。
共享两 jet 和修补端点恒等把各闭区间连成完整 $C^2$ 场，反射侧有相同范数界。

若六项界依次为 $d_{00},d_{10},d_{01},d_{20},d_{11},d_{02}$，可以不做浮点开方而保存

$$
\|D\Delta F\|_F^2\le d_{10}^2+d_{01}^2,\qquad
\|D^2\Delta F\|_F^2\le d_{20}^2+2d_{11}^2+d_{02}^2. \tag{18}
$$

所有这些端点均是精确 Fraction；显示小数不是新证书端点。

一个只涉及规定相位框架的直接推论是：若对两场都采用真实圆片中心
$O_i=\Gamma_i(\pi/3)-n(\pi/3)/k$ 及原 held-frame 公式，则

$$
\widetilde F_{i,\alpha}(s,\theta)
 =R_{k\alpha}F_i(s,\theta-\alpha)+(I-R_{k\alpha})O_i.
$$

同 $\alpha$ 下，空间一、二阶差界不变，位置差额外至多 $2\delta G_0$，
对全部允许相位统一成立。这是规定的真实 held frame，不是优化所得刚体配准。
当前有限对 CLI 的主六项仍明确为未附加该框架的式 (2)；不暗中扩大输出范围。

## 9. 有限 Gauss 点查询到真实场的最小支付式

假设同一已保存 $C,h,P,W,U,A$ 按其实表达式评价，仅核心查询换为有限 Gauss 提供的
$\widehat\Gamma,\widehat\Gamma_u$。在共同真实入口角 $\theta_0(\psi)$ 定义点值差
$e_0=\widehat\Gamma-\Gamma$、$e_1=\widehat\Gamma_u-\Gamma_u$。
这里**没有**先宣称 $\widehat\Gamma_u$ 是有限点函数 $\widehat\Gamma$ 的导数。

由式 (1) 的完整中心修补，直接代数消去相同有限项可得

$$
\widehat X-X=
\left[h+W_0(1-h(0))-W_1h'(0)-W_2h''(0)\right]e_0
 +W_2b_0e_1. \tag{19}
$$

所以每个实际 mesh 角点只要用已有真实 oracle 围住对应的
$\Gamma,\Gamma_u$，就能对保存的数值查询值支付式 (19)。真实角
$\theta_0=\psi-E_0\sin(3\psi)/3$ 的三角舍入和后续有限 Fourier/多项式运算也须
分别围住；可以直接让点 oracle 吃真实 $\theta_0$ 的区间，而不是把数值角默认为
精确角。

数值 held-frame 的原实现使用已知 normal $n(\pi/3)$：
其中心查询误差是核心位置误差加该明确 normal/角运算的舍入。
若另一个诚实实现从查询切向恢复 normal，保守界可再加 $|e_1|/k$。
不能把两种实现的误差来源混在一起。

式 (19) 只支付点查询；若要给有限 Gauss **位置函数自身**的 $C^2$ 误差，仍须对
该实际求积表达式微分并围住，不能借其独立返回的 jet 值跳过。
本条的主 $C^2$ 比较不需要这一偷换，因为从一开始就在比较真实积分定义的式 (1)。
在切口端 $h,h',h''$ 严格为零，且中心修补已消失；完整切口系数不另依赖数值核心
position 积分。最终 physical-H 的尾误差、全尾几何及实际 mesh 全部舍入仍各自明确。

## 10. 来源与结论边界

完整推导、源码对照、真实符号检查与待执行数据合同见[同物理角完整记录](../notes/2026-11-28-analytic-common-material-angle-c2-transfer.md)和[小回执](../notes/2026-11-28-analytic-common-material-angle-c2-transfer.json)。独立精确界实现为[prefix_physical_theta_c2_bounds.py](../scripts/resume_20261128/analytic/prefix_physical_theta_c2_bounds.py)。八个关键恒等式已由SymPy实际准确化简为零；这不是一次对尚不存在的真实固定场的数值验收。

本文给有限对的严格传递与数值点查询的误差表达式。完整尾、柱、帽及全局同一g精化仍须自行完成；有限对小差不自动推出可求和性、Cauchy性、无限维逆界或精确等距族存在。
