# R245：完整 block 的第四阶加法、十次平移张量与四 Gaussian history 的精确有限化

日期：2026-11-15。**完整纸面证明；没有新增研究计算、profile 积分、符号目标、函数秩或参数采样。**

本稿补充 [R243](R243-finite-jet-criterion-for-the-complete-even-exceptional-ruling.md) 的完整偶部判据，给两个可直接使用的有限结构：

1. 对真正完整的二、三阶 profile block，第四 forcing、ruling 与 period 准确相加；整个 ruling 的平移次数至多十。
2. 在例外端芽中，全部几何 history 可以用四个 Gaussian 原函数、十个二次乘积和六个面积原函数，加有限 Laurent 多项式系数表示。

有限结构不提供任意有符号成本。本稿最后证明一个具体限制：即使把平移张量精确匹配，均匀正相位平均也会重开严格非零的领先 ruling 门，不能用作完整消去方案。

来源：[R46](R46-eight-packet-complete-third-order-circle.md)、[R52](R52-overlapping-profile-plane-complete-third-order-circle.md)、[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R183](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R229](R229-p2-energy-boundary-identity-for-exceptional-germs.md)、[R231](R231-complete-mixed-leading-gate-for-the-exceptional-even-port.md)、[R237](R237-complete-next-mixed-layer-after-exceptional-leading-cancellation.md)、[R239](R239-nonseparable-third-order-circles-paying-four-exceptional-energy-gates.md)、[R241](R241-complete-sigma-four-layer-and-resonant-exceptional-germs.md)及 R243。

## 1. 什么才是本稿允许相加的完整 block

固定同一条真实几何、同一目标构造规则、同一全路径 s 起点及同一个 profile 右锚。一个 pair $(f_b,g_b)$ 的支撑包络为 $J_b\Subset I$。要求它的 canonical 第一、第二、第三场

$$
Y_{b,\theta},\qquad Z_{b,\theta},\qquad W_{b,\theta}
$$

及其所需导数在 $I\setminus J_b$ 的开放部分全部为零，且二、三阶完整 range 已成立。这里包括完整 $\theta$ 四槽，而不是只一条对角或一个 leading 原式。

R183/R239 的整个八复制组可以作为这种 block。理由逐层如下。

- Y 由紧 profiles 直接局域。
- 每个基本 pair 的两个二次槽 $f^2-g^2$、$2fg$ 都有零三矩。R46/R52 的完整恢复使其 P、B、$\eta_0$、真实 $W_2$ 和恢复场在基本 pair 包络外全部为零，保留全 s history。
- 第三 forcing 因 Y、Z 局域而支撑于整个八复制包络。八复制准确消掉每个 s 的四条第三 ruling，故第三 P 的左尾也为零。R56 原式在包络外随之给 $\mathcal R_3=0$；用同一 canonical 初值，$W_3$、$\eta_3$ 及全部恢复分子亦在包络外为零。第三 period 另由已付 hook 身份保证周期性。

这里只把**完成的整个八复制组**当成一个 block。单个微包或尚未完成第三 ruling 的基本 pair 一般带第三尾，不能利用本节擅自删去它与其他包的交叉项。

## 2. 完整第四 forcing 的准确加法

取有限个这样的 block，包络 $J_b$ 两两不交。对实数 $a_b$ 定义

$$
f=\sum_ba_bf_b,\qquad
g=\sum_ba_bg_b.
\tag{1}
$$

由 R52/R56 的线性恢复及同一个 canonical 初值，

$$
Y_\theta=\sum_ba_bY_{b,\theta},\qquad
Z_\theta=\sum_ba_b^2Z_{b,\theta},\qquad
W_\theta=\sum_ba_b^3W_{b,\theta}.
\tag{2}
$$

证明不能只用幅度次数：第一 forcing 的跨 block 乘积逐点为零；因此二阶 forcing 是各包二次 forcing 之和，线性恢复给 Z 的式子。Y 与这些完整 Z 的跨包乘积仍逐点为零，故第三 forcing 和 W 的式子随后成立。导数保持各包支撑；固定 u 的 s 导数也只增加同一 profile 的 x 导数，不会移出其包络。

第四原 forcing 为

$$
H_{4,\theta}
=-\{(dZ_\theta)^2+\mathcal S(Y_\theta,W_\theta)\}.
$$

所有跨 block 配对因完整支持条件消失，准确得到

$$
\boxed{
H_{4,\theta}=\sum_ba_b^4H_{4,b,\theta}.
}
\tag{3}
$$

R56 的 ruling 积分及 characteristic range 对 H 线性。因此

$$
\boxed{
\mathscr K_{4,\theta}=\sum_ba_b^4\mathscr K_{4,b,\theta},\qquad
\mathscr P_{4,\theta}=\sum_ba_b^4\mathscr P_{4,b,\theta}.
}
\tag{4}
$$

第二式是完整 profile 周期函数的线性和。即使单个第四恢复尚有左尾，(4) 仍成立：这里先对完整 forcing 作准确加法，再应用线性 range；没有假定第四场也局域。

这些式子不把任意新增全局二阶或第三 gauge 也自动局域化。若采用那种 gauge，必须重新保留其真实交叉项。式 (1) 改变第一向量 f 时，目标度量也按新的 f 重新定义；不能把不同的 block 组合称为同一既定目标的自由变换。

## 3. 固定完整 block 的 ruling 平移次数至多十

令

$$
f_t(x)=f_*(x-t),\qquad g_t(x)=g_*(x-t),
$$

并把输出改用 $y=x-t$ 表示。t 是常数参数，所有选用平移均保持包络在同一合法 I 内。沿同一真实几何，

$$
z=y+t+\omega,\qquad e=h(y+t)+d,\qquad
\lambda=\frac{\gamma(y+t)+d_s}{h^2}
$$

对 t 的次数至多一；$K_0$ 至多二，$K_0/z$ 至多一。frame 及其协变矩阵 $\Omega(k)$ 与 t 无关。因此 s 导数、y 导数和协变导数均不增加已有的 t 次数。

每次 profile 右积分换元后的上端虽写成 $r-t$，但 integrand 在固定基本包右侧为零，所以可换为一个共同的右零 collar；不产生 t 依赖的未知常数。完整 s history 使用同一个全路径起点；如果随后只取某个 germ，段首值是全路径已经真实积出的多项式，不在该段另置零。

### 3.1 R56 的通用逐槽界

若一个已知二次 forcing 的全部原分子配对 $J,T_x,T_s,T_{sx}$ 对 t 的次数至多 d，则 R56(2)、(5)、(6)、(7) 给：

| 对象 | t 次数上界 | 原式来源 |
|---|---:|---|
| $B=J/(2h)$、$P=J_{\rm right}(T_x)/(2h)$ | d | 同右锚线性积分 |
| $\eta_0$ | $d+1$ | $e_sP_x$ 至多多一个 t |
| $\mathcal R_H$、真实 W | $d+2$ | $K_0P$ 至多多两个 t，s 积分保次数 |
| $A=W_x/2+\eta_0/h$ | $d+2$ | 完整 characteristic 分量 |
| 新分子 $V=(A,zP+B,eA-hW)$ | $d+3$ | B 方向还须乘 e |

最后一行不能被“局部第一分量次数较低”代替。特别第二局部恢复的 B 分量还乘 e，不能无原式取消就把整个局部分子说成次数至多三。

### 3.2 从第一场到完整第四 ruling

第一分子是

$$
V_f=(-f'/2,\ 0,\ hf-ef'/2),
$$

其次数至多一。于是二阶 forcing 的 d 至多二，给

$$
\deg_t W_2\le4,\qquad \deg_t V_2\le5.
\tag{5}
$$

第三 forcing 配对第一场与完整第二场，故 d 至多六。通用界给

$$
\deg_t W_3\le8,\qquad \deg_t V_3\le9.
\tag{6}
$$

这已包含全部真实二重 Volterra history、局部恢复和变化 profile 的链式项。

第四 ruling 直接使用 R56(4) 的原 $T_x/h$。其两种配对的次数分别满足

$$
\deg_t(V_{2,x}\cdot V_{2,x})\le10,\qquad
\deg_t(V_{1,x}\cdot V_{3,x})\le10.
$$

最终 x 积分可在固定基本包坐标 y 上进行；完整下阶支持保证没有移动端项。因此

$$
\boxed{
\mathscr K_{t,\theta}(s)=\sum_{j=0}^{10}t^j K_{j,\theta}(s).
}
\tag{7}
$$

这些 $K_j$ 是保留真实 geometry history 的整函数或光滑函数，取决于所用几何；(7) 不只对例外解析 germ 成立。

本证明针对原 canonical 初值规范。额外任意 homogeneous 输入若没有同阶平移多项式界，不由 (7) 自动覆盖。已在同一全路径上按原递推产生的段首历史则已经包含，不能据此另行删除。

## 4. 全旋转张量只有五个角系数，但幅度仍是正四次权

对一个完整 block 作常数正交换基

$$
f_\alpha=\cos\alpha f+\sin\alpha g,
\qquad
g_\alpha=-\sin\alpha f+\cos\alpha g.
$$

完整二、三阶四槽在该换基下保持零。第四 forcing 对原输入是四次，且 $\alpha\mapsto\alpha+\pi$ 同时翻转两个输入，不改变第四输出。因此 (7) 可细写为

$$
\begin{aligned}
\mathscr K_{t,\alpha}(s,\theta)
=\sum_{j=0}^{10}t^j\{&
K_{j,0}(s,\theta)
+K_{j,c2}(s,\theta)\cos2\alpha
+K_{j,s2}(s,\theta)\sin2\alpha\\
&+K_{j,c4}(s,\theta)\cos4\alpha
+K_{j,s4}(s,\theta)\sin4\alpha\}.
\end{aligned}
\tag{8}
$$

这里每个系数仍是完整 ruling 函数；未声称这 55 个生成元独立。对于若干同形 block 的合法不交放置，式 (4) 说明整个 ruling 由有限矩

$$
\sum_b a_b^4 t_b^j
\{1,\cos2\alpha_b,\sin2\alpha_b,\cos4\alpha_b,\sin4\alpha_b\},
\quad 0\le j\le10,
\tag{9}
$$

准确决定。相同的矩数组足以给相同的完整 ruling；反向必要性仍须取这些函数生成元的真实关系。

特别 $a_b^4\ge0$。负幅度也不能把第四成本的符号翻转。包络不交、最终 I、真实三矩和第三 range 还限制允许的参数；(9) 不是把所有形式正锥点直接授予实际路径或 profile 构造。

## 5. 例外端芽只需四个 Gaussian 原函数

现在专取 R243 的例外 germ，令

$$
H=e^{\varepsilon\sigma^2},\qquad
h=h_eH,\quad k=k_e(1-2\varepsilon\sigma^2),\quad
\omega=k_e/h,\qquad\varepsilon>0.
$$

记 $\mathcal A=\mathbb R[\sigma,H,H^{-1}]$，其中系数可依赖固定几何参数。R237(12) 已逐点证明

$$
r_\sigma
=hk\,\mathcal G-kj\,\mathcal P
+\frac{k_e^2-j^2-1-v^2}{8}\mathcal T
+\sum_{m=1}^3h^{-m}\mathcal Q_m(\sigma),
$$

$$
j=2\varepsilon k_e\sigma^2,\qquad v=2\varepsilon\sigma.
\tag{10}
$$

所以原八个 $M_{\rm raw}$ 坐标都是偶多项式乘 $H^r$ 的有限和，而且指数只在

$$
\{1,0,-1,-2,-3\}.
\tag{11}
$$

令

$$
S=\{1,-1,-2,-3\},\qquad
E_r(\sigma)=\int_0^\sigma H(t)^r\,dt\quad(r\in S).
\tag{12}
$$

它们是四个真实、奇的整函数，始终采用同一个中心初值。

### 5.1 一重 history 的准确归约

对 $r\ne0$，任何偶多项式 $P(\sigma)$ 都可唯一写成

$$
P=Q'+2r\varepsilon\sigma Q+b,
\qquad Q\text{ 为奇多项式},\quad b\in\mathbb R.
\tag{13}
$$

从最高次开始向下消元即可：次数 $2d$ 的项由 Q 的 $2d-1$ 项产生，最后只余常数 b；因 $r\varepsilon\ne0$ 不会失去主系数。故

$$
\int_0^\sigma P(t)H(t)^r\,dt
=Q(\sigma)H(\sigma)^r+bE_r(\sigma).
\tag{14}
$$

Q 为奇多项式，原下端值确为零。r=0 时直接积分偶多项式，得到奇多项式，不另引入 $E_0$。

因此每个中心二阶 history 都准确具有

$$
m_i=q_i+\sum_{r\in S}b_{ir}E_r,\qquad
q_i\in\mathcal A\text{ 为奇函数},
\tag{15}
$$

且 $q_i$ 仅用 (11) 的指数。所有 $b_{ir}$ 是完整原系数确定的常数，不是可自由挑选的控制参数。

### 5.2 第三局部源是奇 Laurent 多项式

这一点需要原恢复，不只援引总奇偶。第一分子具有
$(\text{偶},0,\text{偶})$ 奇偶型，协变导数是
$(\text{奇},\text{偶},\text{奇})$。第二局部恢复中 P、B 偶，$\eta_0$ 奇，故其分子是
$(\text{奇},\text{偶},\text{奇})$，协变导数是
$(\text{偶},\text{奇},\text{偶})$。

于是第一场与第二局部场的 $J,T_x,T_s$ 均为奇；R56(5) 每项仍为奇。R73 的 $\Psi(\phi,r_\sigma D_\theta)$ 同样为奇：其局部系数含 $\gamma$ 或 $e_s$，而 $r_\sigma$ 为偶。因此完整第三式

$$
W_3'
=-2\ell+2r_\sigma(\phi,\Phi_mD_\theta)
+2\Psi(\phi,r_\sigma D_\theta)
\tag{16}
$$

中不含 m 的部分是奇 Laurent 多项式，包含全部局部恢复和真实链式项。

任意奇多项式乘 $H^r$ 的中心积分是一个偶 Laurent 多项式减去其真实中心值。r=0 直接积分；r非零按最高次消元。特别没有把该常数设为零，也没有因指数相加为零而除以零。

## 6. 二重 history 只增加六个面积

记

$$
K_{r,s}(\sigma)=\int_0^\sigma H(t)^rE_s(t)\,dt,\qquad
A_{r,s}=K_{r,s}-K_{s,r}.
\tag{17}
$$

对 r、s 在四元集合 S 中，原积分恒等式给

$$
K_{r,s}+K_{s,r}=E_rE_s,\qquad
K_{r,r}=E_r^2/2.
\tag{18}
$$

因此只需十个对称乘积 $E_rE_s$ 和六个 $A_{r,s}$，r、s 取不重复无序对。面积为偶整函数，$A_{r,s}(0)=0$；它们不是另选的积分常数。

由 (16)，真正非局部第三 history 只需

$$
\int_0^\sigma m_i'(t)m_j(t)\,dt.
\tag{19}
$$

将 (15) 代入，逐类处理：

- $q_i'q_j$ 为奇 Laurent 多项式，其积分初等；
- $\int q_i'E_s=q_iE_s-\int q_iH^s$，最后一个 integrand 仍为奇 Laurent 多项式；
- $\int H^rq_j$ 同样初等；
- 最后剩下的恰为 $b_{ir}b_{js}K_{r,s}$。

所有端点都是同一个 0，$q_i(0)=E_s(0)=0$；没有丢掉由初等原函数产生的中心常数。若 r+s=0，所剩项按普通多项式积分处理，不误用 $1/(r+s)$。

结合 (18) 及完整恢复，得到：

**二十一生成元结论。** 整个中心化第四 ruling 的全部几何系数属于

$$
\boxed{
\mathcal A\cdot
\operatorname{span}_{\mathbb R}
\{1,\ E_r,\ E_rE_s,\ A_{r,s}:r,s\in S,\ r\le s
\text{ 对乘积},\ r<s\text{ 对面积}\}.
}
\tag{20}
$$

即 1 个常元、4 个一层、10 个乘积、6 个面积。它是**二十一生成元的 $\mathcal A$ 模呈示**，不是宣称真实函数空间维数为二十一，也没有证明这组函数独立。

恢复中只会乘几何 Laurent 系数；第四 ruling 对第二 history 二次、第三 history 线性，所以不需要三重乘积或更长面积。R243 的原相位五项仍全部保留。

实际二阶中心常数只增加常元或一层项，第三中心常数只增加常元；它们不迫使新超越函数出现。但实际偶部比较依然必须按 R224/R227 的完整组合处理，不能据此单独扔掉这些项。

特别，负指数的 $E_r$ 及与它们配对的面积必须原样保留。即使 $E_r$ 在正无穷有有限极限，也不能把它在整条 germ 上替成该常数；有限精确化与只保渐近首项不同。

## 7. 小呈示的显式 ODE 状态界

式 (20) 的 core 导数准确为

$$
E_r'=H^r,\qquad
(E_rE_s)'=H^rE_s+H^sE_r,\qquad
A_{r,s}'=H^rE_s-H^sE_r.
\tag{21}
$$

设某次完整原式输出在 (20) 中的系数，$\sigma$ 次数不超过 a，H 指数位于 $[m,M]\cap\mathbb Z$。先把 $\mathcal W_e$ 的三列也收入，使

$$
a\ge4,\qquad m\le-1,\qquad M\ge1.
$$

一个显式微分闭包可以取：

| core 层 | core 数 | H 指数区间 | $\sigma$ 次数 |
|---|---:|---|---|
| $E_rE_s,A_{r,s}$ | 16 | $[m,M]$ | $0,\ldots,a$ |
| $E_r$ | 4 | $[m-3,M+1]$ | $0,\ldots,a$ |
| 1 | 1 | $[m-6,M+2]$ | $0,\ldots,a$ |

式 (21) 每次下降一层，只把 H 指数加上 S 中一个值；两次下降最多减六或加二。多项式微分降低次数，$H^r$ 的微分给 $2r\varepsilon\sigma$ 乘原状态，由 ODE 系数承担，不增加该清单的多项式次数。

因此得到 R243 同型系统

$$
X'=(N+2\varepsilon\sigma D)X,
$$

其中 N 常数且按层数、多项式次数严格三角，D 为整数对角。状态数有可直接使用的保守界

$$
\boxed{
n\le(a+1)\{21(M-m)+45\}.
}
\tag{22}
$$

这是一个按真实有限清单计算的公式；本稿没有填入尚未编译的 a、m、M 或宣称任何新秩。原冗余仍由 R243 的有限 jet 判零处理，不能改为把二十一族的所有系数各自置零。

共振 $\varepsilon=k_e^2/4>0$ 可直接代入全部式子；(13) 的分母在每个所选非零 $k_e$ 上合法。本稿不声称该有理归约在 $(k_e,\varepsilon)=(0,0)$ 一致有界；真实端芽安装的联合 IFT 已由 R241 另行支付。

## 8. 均匀正相位平均必重开领先门

有限结构不提供一个自动消去策略。下面准确检验一个看似可能的策略，并给其严格限制。

在固定正 x 区间上，令

$$
A_f=\mathcal G(f,f),\qquad A_g=\mathcal G(g,g),\qquad
\overline A=(A_f+A_g)/2,
$$

$$
U=(A_f-A_g)/2,\qquad V=\mathcal G(f,g).
\tag{23}
$$

由同一三矩，U、V 都真正紧支撑；$\overline A$ 一般仍有共同左二次尾。对基准角旋转，

$$
A_\alpha=\overline A+U\cos2\alpha+V\sin2\alpha.
$$

R231 已证明原领先项准确为

$$
C_{\alpha,\theta}
=-E(A_\alpha,A_\alpha-A_{\alpha+\theta}),
\qquad
E(X,Y)=\frac14\int(x^2X''Y''+2X'Y').
\tag{24}
$$

$A_\alpha-A_{\alpha+\theta}$ 紧。对 $\alpha$ 平均时，背景 $\overline A$ 的贡献因差的平均为零而消失；没有把该非紧背景错误放进紧槽分部积分。正交三角积分直接给

$$
\boxed{
\frac1\pi\int_0^\pi C_{\alpha,\theta}\,d\alpha
=-\sin^2\theta\,\{E(U,U)+E(V,V)\}.
}
\tag{25}
$$

括号对每个非退化紧三矩圆严格正。若它为零，E 在紧函数上的正定性迫 U=V=0。R229 的真实同锚身份是

$$
\mathcal G(u,v)
=\frac{x^2}{8}J\{x^4(u/x)''(v/x)''\}.
\tag{26}
$$

对 $U=V=0$ 的原右积分微分，得到

$$
r_f^2=r_g^2,\qquad r_fr_g=0,\qquad r_u=(u/x)''.
$$

于是 $r_f=r_g=0$。正 x 区间上 f、g 各为 $ax+bx^2$；双零 collar 迫二者全零，矛盾。故

$$
\boxed{E(U,U)+E(V,V)>0.}
\tag{27}
$$

式 (24) 的 $\alpha$ 频率只有 0、2、4，所以四个等距射影角已经准确给出同一平均：

$$
\frac14\sum_{\ell=0}^3
C_{\alpha_0+\ell\pi/4,\theta}
=-\sin^2\theta\,\{E(U,U)+E(V,V)\}.
\tag{28}
$$

因此，均匀正角平均的领先 d 系数严格负，e 系数为零。它不能保留 R239 的 leading 双零。此结论**不排除非均匀正角组合**；尤其不能据此撤销 R239 已构造的两互补角方案。

## 9. 有限真实平移匹配也不能挽救这种均匀平均

式 (28) 本身只是同一个 block 上的有限角平均；不能把四份放在同一支撑就使用第 2 节的加法。为精确区分，可把平移张量也支付，得到一个实际有限构造。

取 $N_*=4^{11}$，将 $j=0,\ldots,N_*-1$ 写为十一位四进制数。令 $\chi(j)$ 为其数字和模四。在相邻间距 L 的合法完整 block 上选角

$$
\alpha_j=\alpha_0+\chi(j)\pi/4.
$$

对 $\zeta=i$、$m=1,2$，形式有限生成式为

$$
\sum_{j=0}^{4^{11}-1}\zeta^{m\chi(j)}e^{jt}
=\prod_{q=0}^{10}
\left(\sum_{b=0}^3\zeta^{mb}e^{b4^qt}\right).
\tag{29}
$$

每个因子在 t=0 为零，故左侧的 0 至 10 阶导数都为零。于是对任意等距平移 $t_j=t_0+jL$，

$$
\sum_j t_j^d e^{2mi\alpha_j}=0,
\qquad m=1,2,\quad 0\le d\le10.
\tag{30}
$$

实际 block 数很大但有限。可先选择足够小的完整基本 block，再取大于其包络宽度的正 L，使全部放入任意已选合法 I。R183/R239 的完整 block 可在任意正开区间中构造；这里不要求统一幅度或导数盒。最后共同正归一化保持全部低阶零条件。

由 (8)、(30)，这个实际不交组合的完整 ruling 准确等于各放置点的均匀角平均之和。没有仅匹配 leading 层。可是每个放置点在 (27) 中的能量都严格正，所以式 (4)、(25) 给其领先系数

$$
L_c^{\rm total}
=-a^4\sum_j\{E(U_{t_j},U_{t_j})+E(V_{t_j},V_{t_j})\}<0,
\qquad L_s^{\rm total}=0
\tag{31}
$$

（a 为共同的非零实幅度）。故这条完全准确的平均构造仍被原 R231 门排除。没有为此运行任何实际求积或制造一个待测试候选。

式 (31) 的用途是明确剩余建设性任务：需要对真实有限系数或不同 block 类型找到非均匀的正平衡，不能用形式带符号矩消去或均匀 O2 平均代替。

## 10. 对完整 joint 问题的范围

第 2–4 节是同一真实几何上的完整 forcing/ruling 加法与有限平移张量，不要求例外 germ。第 5–7 节是指定例外 germ 上完整几何 history 的精确压缩，不删除任何负指数原函数或面积。两者可合并为一个有限、准确的 whole-even-ruling 目标，再由 R243 检验真实函数关系。

尚未证明的是：R239 的参数、更多非同构完整 block 或允许的全局二阶 gauge 能同时支付这些全部有限条件。正四次幅度、包络放置、同一个固定目标与全部低阶 range 必须继续保留。即使整个偶 germ 的条件付清，其他 s 段、奇部、完整 period、同一 w 的 joint ruling 及最终有限等距族也仍须另付。

