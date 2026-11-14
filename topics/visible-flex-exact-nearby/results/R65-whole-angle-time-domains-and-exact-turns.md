# R65：全角复时间域、准确转向和域继承

**状态：已证明。** 本文给出完整的局部解析域判据及真实正弦时间、
径向反射、转向消根和圆盘继承证明。第 8 节只登记已实际支付的有限区间；
尚未完成两条参考腿的全区间覆盖，更没有真实流、共轭误差或 PDE 逆的结论。

对象始终是本题准确 affine 子族的显式径向对称、无限 R33 原函数图。
当前点为

$$
\delta _5=-\frac{7789843107295549}{4611686018427387904}.
$$

目标根 $t>0$ 是该点真实输出径向度量的根，不能换成 rounded 控制点图的根。
时间网格来自已保存的 $\delta _4$ 有限参考；使用这个网格不会改变实际场的
$\delta _5$ 身份。物理角为 $\theta$，归一角为 $x=4\theta$。

## 1. 同一完整主场的无分母不变量

写 $X=F_r$，在旋转柱坐标基中以相位 $\beta,\gamma$ 表示单位切向量。
令

$$
\begin{gathered}
c=\cos\gamma,\quad s=\sin\gamma,\quad
P=1+\beta_\theta,\quad u=\gamma_\theta,\quad
p=\beta_r,\quad q=\gamma_r,\\
h=-\sin\beta X_1+\cos\beta X_2,\quad
v=-\cos\beta X_1-\sin\beta X_2,\quad z=X_3,\\
Q=c z-s h,\qquad
D=P c Q-u v,\quad M=p c Q-q v,\quad W=Q^2+v^2.
\end{gathered}
\tag{65.1}
$$

这三个不变量都是实际图及其导数的整表达式；此处没有除以二型系数或
曲率平方根。R59 的移动 frame 恒等式给出

$$
D=-N_{\rm raw}/a^2,\quad M=-M_{\rm raw}/a^2,
\quad W=G_{\rm actual}/a^2.
\tag{65.2}
$$

在负曲率实区，R37 所选实际 modified 主场的两个速度，按本脚本的分支约定，是

$$
f_\sigma(\tau,\theta)
=-t\cos\tau\,
\frac{M+\sigma\sqrt{-K_0}\,W}{D},
\qquad r=t\sin\tau,\quad\sigma\in\{-1,1\}.
\tag{65.3}
$$

所有量取于同一 $(r,\theta)$。特别地，$W$ 包含实际面积平方，不能在有
度量残差时改成输出度量的行列式。

## 2. 准确正弦像与真实样条 germ

设一个准确时间子区间写成
$\tau=\tau_c+h u$，其中 $\tau_c,h$ 是准确的有理数与 $\pi$ 的有理线性组合，
$h\ne0$。实时间始终满足

$$-\pi/2\le\tau\le\pi/2.\tag{65.4}$$

若 $|u|\le R$，则同一个中心 $r_c=t\sin\tau_c$ 满足

$$
|t\sin(\tau_c+hu)-r_c|
\le t\{ |\sin\tau_c|(\cosh(|h|R)-1)
       +|\cos\tau_c|\sinh(|h|R)\}.
\tag{65.5}
$$

证明是准确恒等式
$\sin(a+z)-\sin a=\sin a(\cos z-1)+\cos a\sin z$，及两个幂级数的
三角不等式 $|\cos z-1|\le\cosh|z|-1$、
$|\sin z|\le\sinh|z|$。同一个 $t\sin\tau_c$ 必须用于系数展开和像界；
不能另取一个浮点中心后忽略其差。式 (65.5) 保留转向处的一阶速度消失。

实际径向标量是有共同精确 knots 的分段多项式。对实径向像相交的**每一个**
闭 common span，均选其真实多项式 germ 并独立支付以下域门。一个 germ 的
复延拓可以超出其实际 span，但只有实轨道位于该 span 的部分才代表实际场。
取全部 germ 的界的最大值可覆盖完整实际区间；不存在将一条离开 span 的
多项式延拓默认为实际样条的步骤。包含仅一个相邻浮点间距的 span 也须列入，
除非另有完整、带误差的 gluing 证明。

枚举所需 spans 时可进一步利用单调性：对准确的实端点
$\tau_-\le\tau_+$，分别计算 $t\sin\tau_-$ 的有向下界和
$t\sin\tau_+$ 的有向上界。由于 $t>0$ 且 (65.4) 上正弦单调，这两个端点
包住整个真实径向像，允许删去与这个**严格端点包络**不相交的 spans。
这与忽略短 span 不同：必须实际付清端点与 knot 的分离；把整条时间区间
先包成一个宽 Arb 球再取正弦通常更宽，只会多列 germ，不构成错误证书。

## 3. 同一真实锚点和无限角／时间尾

以下以正径向 span $I=[a,b]$ 为例。若 $r_c$ 的整个已证球位于 $I$，取
$u_a=0$；否则取靠近 $r_c$ 的准确端点 $r_a\in I$，令

$$
u_a=\frac{\arcsin(r_a/t)-\tau_c}{h}.
\tag{65.6}
$$

这里 $\arcsin$ 是对应 (65.4) 的主实支。
它满足准确恒等式 $t\sin(\tau_c+hu_a)=r_a$。在真实锚点应用 R59 同一控制盒
的全角 strip 下界 $|D(u_a,\theta)|\ge d_a>0$。必须实际检查准确 $\delta_5$
属于该盒，且所有覆盖锚点的径向 cells 都包含；不能在离开实际 span 的
$r_c$ 上套用 R59。

设在更大的真复域
$|u|\le S$、$|\operatorname{Im}\theta|\le w$ 上有实际整表达式的模界
$B_w$，在较窄角带 $s<w$ 上有模界 $B_s$，其中 $S>R>1$。
这里的 $D,M,W$ 都已在形成非线性乘积**之前**加入无限原函数的误差。
写

$$ D(u,\theta)=\sum_{i\ge0}\sum_{k\in\mathbb Z}d_{ik}u^i e^{4ik\theta}.$$

在 $N$ 个四分之一周期节点的带误差 DFT 上保留 $|k|\le K<N/2$。
令 $s_x=4s,w_x=4w$，则每个时间系数的保留模 alias 费用至多

$$
\frac{B_w}{S^i}
\sum_{k=-K}^K e^{s_x|k|}
\frac{e^{-w_x(N-|k|)}+e^{-w_x(N+|k|)}}{1-e^{-w_xN}},
\tag{65.7}
$$

未保留角频费用至多

$$
\frac{2B_w}{S^i}
\frac{e^{-(w_x-s_x)(K+1)}}{1-e^{-(w_x-s_x)}}.
\tag{65.8}
$$

证明：Cauchy 给 $|d_{ik}|\le B_w S^{-i}e^{-w_x|k|}$；逐一求和
所有 $k+\ell N$ 的 alias，再求和 $|k|>K$。因此若带误差 DFT 的有限
Wiener 和加上 (65.7)–(65.8) 为 $A_i$，则真实时间系数满足
$\|D_i\|_{A_{s_x}}\le A_i$。

设已算 $i=0,\ldots,m-1$，$\alpha\ge|u_a|$ 且 $\alpha<S$。由准确消去常数项，

$$
\begin{aligned}
|D(u,\theta)-D(u_a,\theta)|\le V_D:={}&
\sum_{i=1}^{m-1} A_i(R^i+\alpha^i)\\
&+B_s\left\{\frac{(R/S)^m}{1-R/S}
               +\frac{(\alpha/S)^m}{1-\alpha/S}\right\}.
\end{aligned}
\tag{65.9}
$$

故 $d=d_a-V_D>0$ 证明在整个目标域 $D\ne0$ 且 $|D|\ge d$。
式 (65.9) 是同一实际函数在两个点的差，不能改成两个各自含常数宽度的
区间结果相减。未知时间尾用 $B_s$，已保留时间层的未知角尾用 $B_w$；
这两个补集覆盖所有遗漏指标，没有漏掉同时高时间阶和高角频的区域。

同样的方法给 $M,W$ 的完整目标域模界。实际的 $a,E$ 在大复时间域须无零点，
从而 $K_0$ 真正解析；由其完整 Taylor 系数与 Cauchy 尾证明
$\operatorname{Re}(-K_0)>0$ 后，取在负曲率实轴为正的平方根支。
于是 (65.3) 真正解析。三角不等式及完整 $D_\theta,D_{\theta\theta}$ 等界
给出实际 $|f_\sigma|,|\partial_\theta f_\sigma|,
|\partial_\theta^2 f_\sigma|$；这些是完整场模界，绝不是已验证的流或 Jacobian。

## 4. 准确径向反射，包括时间方向

对本题显式对称对象令 $S=\operatorname{diag}(1,1,-1)$。有

$$
F(-r,\theta)=SF(r,\theta),\quad
F_r(-r,\theta)=-SF_r(r,\theta),\quad
F_\theta(-r,\theta)=SF_\theta(r,\theta).
\tag{65.10}
$$

按本题 $C=F_\theta\times F_r$ 的方向，$C(-r)=SC(r)$，故
$N_{\rm raw},G_{\rm actual},a,E,K_0$ 都为偶函数，$M_{\rm raw}$ 为奇函数。
由 (65.2)，$D,W,K_0$ 偶、$M$ 奇。负径向真实锚点因此可在对应正 span
应用 R59。变换必须同时使用

$$
I\mapsto-I,\quad r_c\mapsto-r_c,\quad
\tau_c\mapsto-\tau_c,\quad h\mapsto-h.
\tag{65.11}
$$

主支 $\arcsin$ 为奇函数，故式 (65.6) 给出的 $u_a$ **不变**。
不是只把径向坐标取绝对值而丢掉实际时间方向。负侧的 DFT／时间系数仍是
其自身真实 germ；仅锚点下界使用反射。
此外，准确主场满足

$$ f_\sigma(-\tau,\theta)=-f_{-\sigma}(\tau,\theta).\tag{65.12}$$

所有由 $|M|+|\sqrt{-K_0}W|$ 得到的域模界对两个分支均有效。
这允许按第 7 节继承模界，但不允许把一腿的数值射线终点当成另一腿终点。

## 5. 真根处的准确消根

令 $\varepsilon\in\{-1,1\}$ 是转向侧，
$\eta=\pi/2-\varepsilon\tau$，于是
$r=\varepsilon t\cos\eta$、$r_\tau=t\sin\eta$。
要求整个实际实区间位于含 $\varepsilon t$ 的同一个真实 common span，
否则本节不能替相邻 germ 消根。令

$$
\rho=t(1-\cos\eta),\qquad
J(\rho)=\frac{-K_0(t-\rho)}{\rho},\qquad
\mathcal Q(\eta)=\frac{tJ(\rho)}{1+\cos\eta}.
\tag{65.13}
$$

准确 $K_0(t)=0$ 使 $J$ 的奇点可去，且
$J(0)=K_0'(t)>0$。所以

$$ -K_0(t\cos\eta)=\sin^2\eta\,\mathcal Q(\eta).\tag{65.14}$$

若 $\operatorname{Re}\mathcal Q>0$ 在所付复域成立，则真实实内领口上的正根
延拓为 $\sin\eta\sqrt{\mathcal Q}$，并且完整正则场为

$$
f_\sigma=-t\sin\eta\,
\frac{M+\sigma\sin\eta\sqrt{\mathcal Q}\,W}{D}.
\tag{65.15}
$$

这在准确 $\tau=\pm\pi/2$ 解析，并在端点使 $f_\sigma$ 及其角导数准确为零。
此处没有要求 $-K_0$ 在跨转向的复圆盘仍处于右半平面。

为支付完整 $J$，在真实根周围半径 $R_K$ 的复径向盘上先证明 $a,E$ 无零点
及 $|K_0|\le B_K$。若已算 $J$ 的前 $L$ 个归一径向系数，
$|\rho|\le\rho_*<R_K$，则全部遗漏费用至多

$$
\epsilon_J\le\frac{B_K}{R_K}
\frac{(\rho_*/R_K)^L}{1-\rho_*/R_K}.
\tag{65.16}
$$

若 $|\eta|\le\eta_*$，取 $c_*:=\cosh\eta_*-1<2$，则
$\rho_*\le t c_*$、$|1+\cos\eta|\ge2-c_*$，所以
$\epsilon_{\mathcal Q}\le t\epsilon_J/(2-c_*)$。
时间展开的 $\rho(0)$ 通常非零：对**已知有限**径向多项式作完整 Horner
复合，然后加入 (65.16)，不能把截断解析级数移到非零中心而漏掉高阶回灌。
再用完整 $\mathcal Q$ 的时间 Cauchy 尾证明其右半平面门。

在 $|u|\le R$ 上还可直接使用

$$
|\sin\eta|\le |\sin\eta_c|\cosh(|h|R)
                 +|\cos\eta_c|\sinh(|h|R)
\tag{65.17}
$$

支付 (65.15) 的实际模界。R59 的 D 锚点和第 3 节双尾不因消根而改变。

## 6. 分段实际场与闭覆盖

真实标量在所有内部 knots 的连续阶数须至少为 $C^2$，保证 (65.3)／(65.15)
所用实际场连续。这由真实 B-spline 次数和准确内部重数检查，不能由采样代替。
对每个闭实时间子区间，给出其完整径向 common-span 列表，对每个列表项支付
一个有效域证书。多个 germ 可以在公共 knot 同时被列入；重复覆盖无害。
对实时间取相应实际 germ，其域／模界的最大值即为这个区间的完整实际界。

域验证失败时可以准确二分实区间，重新计算每个子区间的 common-span 列表。
不得删除失败 span、忽略极短区间或默认为某个 root 因式仍适用。
一个完整覆盖清单必须明确检查：准确首末端点为 $-\pi/2,\pi/2$，所有相邻
时间端点完全相同；每个子区间的全部 germ 有通过证书；两腿的对象、参考网格、
实际分支和时间方向各自对应。未完成这一清单就只有部分覆盖。

## 7. 已证复时间圆盘的继承

设同一真实 germ 的旧证书在
$|\tau-c_0|\le |h_0|R_0$、$|\operatorname{Im}\theta|\le s_0$
上给出 $D$ 下界、已选真实平方根支及完整场模界。一个新准确时间子区间
$\tau=c_1+h_1u$ 可直接继承这些界，只要

$$
|c_1-c_0|+|h_1|R_1\le |h_0|R_0,\qquad s_1\le s_0.
\tag{65.18}
$$

三角不等式证明复域包含，模界随域限制而保留。继承时必须绑定同一准确
affine 对象和同一个 common-span 多项式；跨 span 只因看起来相近而继承无效。
式 (65.18) 可用准确有理数／$\pi$ 表达式和有向球运算验证；完全相同的
端点与半径可先用精确恒等式处理。若先作 (65.11) 的反射，则同时反射
time center、time orientation 和 germ，再验证同一不等式。

普通平方根在相交的负曲率实段都取正值，故其解析支一致；真根版本由
(65.14)–(65.15) 规定。场模界对 $\sigma=\pm1$ 同时有效的事实由 (65.3)、
(65.15) 的三角不等式明确保证，不能从某一个带符号的采样最大值推断。
继承的费用仍是 $d\theta/d\tau$ 的模界；若改成 $d\theta/du$，须另乘 $h_1$。

## 8. 当前实际范围与程序入口

已完成并推送的普通域是 $\delta_5$、新共享网格 forward 第 419 段的全部
三个准确 common germs，物理角宽 $1/64$、复时间半径 $R=3$，外时间半径
$S=4$ 和较宽物理角带 $1/32$。其三个 D 下界分别大于
$0.1627344,0.1656428,0.2250061$，三个 $\operatorname{Re}(-K_0)$ 下界均大于
$0.5769445$。这是第二次执行器恢复后真正重跑的报告
`type_fixed_step02_d5_exact_affine_step5_reference419_whole_angle_time_domain.json`，
SHA256 为 `e1a2c3f327c3a36e33c412e76c70eebd185f224ea938dcdea93ee30ab9a05f90`。

新正弦／真转向入口是
`scripts/fourfold_phase_sine_time_geometry.py` 和
`scripts/fourfold_phase_full_angle_sine_domain.py`。
它们使用 `fourfold_phase_field_time_turn_collar.py` 的真实根消去，
以及冻结 uniform grid 两源形成完整 D/M/W 系数。准确端点由 `PiTime` 保存。
两腿各第 $0,1,2,548,549$ 段的十个真转向域及 forward 第 3 段的完整两个
普通 germs 已实际通过。十个真转向域仍为物理角宽 $1/64$、$R=3,S=4$，
使用 $R_K=3/1250$、64 个径向消根系数；共同下界
$|D|>0.37529$、$\operatorname{Re}\mathcal Q>6.62159$，共同场模界
$|f_\sigma|<0.22454$。这些下界仅限上述十个明确区间。
第 3 段先前被真转向入口拒绝，原因是其完整实际像离开单一 root span，
该拒绝记录保留，没有将相邻 germ 伪作可消根。

完成证书、准确参数和 SHA 见
`notes/2026-11-12-sine-turn-domain-frozen-manifest.json`。批处理的
`complete` 只表示已执行其明确请求列表；即使该列表全通过，也不表示两条腿
的全部 1100 个原始区间已经覆盖。正在推进的完整覆盖不属于本节已证数值范围。
所有数值界只为解析系数域：实际参考与真实场的连续残差、两腿误差传播、参数
Taylor、最终 KAM 和完整闭曲面族仍须各自支付。
