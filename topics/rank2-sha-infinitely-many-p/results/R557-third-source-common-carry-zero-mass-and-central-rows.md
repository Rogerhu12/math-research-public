# R557 — 同一 carry 的完整第三来源返回、双态零质量及中央首项

日期：2026-11-14。**状态：已证明。**
R536 的同一个测试 $\mathfrak q_{n,p}$ 现在对 R541 的第三来源
$\eta$ 及 R548 的正来源 $h=\eta+\rho_0/2$ 保持整个四输出，
无需改变七行右逆或另选系数。
在原五深、一单位网格上，两来源的加权质量和全部只依赖自由输入的
测试也严格为零。三条实际中央各有明确单位首项；
第三来源的未归一 $Y-W$ 差则准确取消第一项，获得 $2n$ 的下界。

本篇中的 $h$ 始终是 $\eta+\rho_0/2$，
不同于 R536 第9节曾记作 $h$ 的 $\omega^2\mathcal T_*\rho_0$。
不从旧来源的 $W$ 核给新 $h$ 赋核心。

## 1. 同一完整输入、观察和 carry

保 R531、R536、R541 的全部原 ray、固定坏集及 $D_*$ 条件，
特别 $p\ge71$。记
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\gamma=3+\omega,\quad\bar\gamma=2-\omega,
$$
$$
b=17,\quad\lambda=-\bar\pi_0^{-1},\quad
\beta=-\lambda,\quad\kappa=p\lambda^2,\quad d=p-1,\quad
\rho_0=-\nu_\sigma^{\otimes6}/84.
\tag{1}
$$
原六输入为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$，设
$$
\begin{aligned}
H_0&=(1,0,-1,1,0,0),&
H_1&=(-1,2,\omega,1+\omega,0,0),\\
C&=H_0/\delta,&
D&=(1,\omega^2,-2\omega,0,1,2+3\omega),\\
F&=D+C,&E&=F+13C,&
G&=13H_1+(3-2\omega)F.
\end{aligned}
\tag{2}
$$
保持原 $\pi_4=(Y,W,W',G)$；
$Y,W,W',W_2=-\omega^2W-\omega W'$ 均为 R531 的原观察。
特别
$$
Y=A+c+2d_0,\qquad W=A+3\delta c+4d_0,\quad
A=\delta\xi_1+2\delta\xi_2+\gamma\xi_3+\bar\gamma x.
\tag{3}
$$
$C,F,D,E$ 与整个 $\pi_4$ 正交，$C\perp F$、$D\perp E$。
这里 $G$ 是原隐藏行，不是 R541 的矩阵 $\mathcal G$。

令 $H$ 固定前四输入，后两输入矩阵为
$$
H=\frac12\begin{pmatrix}-1-\omega&-1-2\omega\\
2+\omega&-1-\omega\end{pmatrix},\qquad
\eta=\omega^2H_*\rho_0,\quad h=\eta+\rho_0/2.
\tag{4}
$$
写 $\zeta_j=\omega^{2j}$，
$$
D_j=F-\zeta_jC,\quad E_j=F+13\zeta_jC,\qquad
\Gamma_{n,j}=\{C,F\ {\rm unit},D_j\in p^n\}.
\tag{5}
$$
实际恒等式 $\Gamma_{n,j}=\{D_j\in p^n,E_j\ {\rm unit}\}$ 保持。

R536 的准确七行系数 $x_p$、六次 $Q_p$ 及其在 $(D,E,G)$ 中的
$P_p$ 全部不变。仍令
$$
u_j=(1+\lambda\kappa^j)^{-1},\qquad
\mathcal R_p\!\left(\sum a_{kj\ell}D^kE^jG^\ell\right)
=\sum a_{kj\ell}u_jD^kE^jG^\ell,
$$
$$
q_{n,p}^{(j)}
=\frac1{b\Omega^6}
(\mathcal R_pP_p)(D_j/\kappa^n,E_j,G)
\quad\hbox{于 }\Gamma_{n,j},
$$
$$
\boxed{\mathfrak q_{n,p}
=\frac13\sum_{j=0}^2\mathbf1_{\Gamma_{n,j}}q_{n,p}^{(j)}.}
\tag{6}
$$
本篇不以 $H$ 保持此函数为前提；一般 $\mathfrak q_{n,p}\circ H$
确实不同。

## 2. 第三来源的四个完整 scalar 核

后两输入只通过同一个
$$
M=c+(2+3\omega)d_0
$$
进入 $D,F,E,G$。实际矩阵乘法给
$$
\boxed{MH=2\omega(c-d_0),\qquad CH=C.}
\tag{7}
$$
这两条整性是扩展到第三来源的关键；
原 $YH$ 的半整数系数并未被忽略。

**定理1。** 对 $\mu=\rho_0,\eta,h$，所有 $n\ge0$，
$$
\boxed{
\mu|_{\{J\in p^n\}}=\beta^n(P_{J,\kappa^n})_*\mu,
\quad J=C,F,D_j,E_j,\quad j=0,1,2.
}
\tag{8}
$$
它们是保完整其余五方向的测度身份。

**证明。** R531 给以下 entire theta 空间的绝对 scalar 核，
其原 theta 群中心和非零锚均已支付：
$$
\begin{array}{c|c|c|c}
\text{物理方向}&\text{完整整覆盖}&g_\pi\bmod 2N&\text{绝对锚}\\ \hline
C&H_0,\ \text{odd }3&1\bmod6&\sigma(\delta z)\\
F&3F,\ \text{odd }117&1\bmod234&\sigma(3(4+\omega)z)\\
D_j&D_j,\ \text{even }14&15\bmod28&\Theta(\gamma z)\\
E_j&3E_j,\ \text{even }1638&1639\bmod3276&
 \Theta(3\gamma(4+\omega)z).
\end{array}
\tag{9}
$$
全部标量为 $\beta$，不是仅对原第一边际成立。

$H$ 酉且固定前四输入，故整个框架乘 $H$ 后的 Gram 完全不变。
(7) 使 (9) 各个整覆盖乘 $H$ 后仍为整数行。
$H_0$ 原样不变；$3F$ 的末两非零模二系数从两个变为零个，
总非零模二个数从五变为三。
$D_j$ 和 $3E_j$ 的总个数按 $j=0,1,2$ 分别从
$(4,6,6)$ 变为 $(2,4,4)$。
在 $\mathcal O_K/2$ 中每个非零乘子保原 sigma 奇半特征，
所以上述每条完整 odd/even 半特征均不变。

沿所选轴，与其余五轴的 Gaussian 交叉项仍为零；
若其余观察为清半整数而采用额外 $[2]$ 覆盖，这不改变本轴的
(9) 空间、半特征或物理缩放。
因此 $\eta$ 在每条轴上仍属于同一个 entire theta 空间张量
全部其余系数空间。已付 scalar 核遂逐系数适用，给 $\eta$ 的 (8)。
再线性组合得到 $h$。无新增 ray、未知相位或普通符号。证毕。

原 $C$ 的整个 odd3 空间也保持，所以对这些 $\mu$ 均有
$$
\boxed{
(\text{忘 }C)_*(C^2\mu)
=(\text{忘 }C)_*(C^4\mu)
=(\text{忘 }C)_*(C^5\mu)=0,
}
$$
$$
\boxed{
(\text{忘 }C)_*(C^6\mu)
=-8b\Omega^6(\text{忘 }C)_*\mu.
}
\tag{10}
$$
这保全部其余五变量测试，不是先把它们取质量。

## 3. 原测试现在保持整个两态四输出

**定理2。** 对 $\mu=\rho_0,\eta,h$，
$$
\boxed{
(\pi_4)_*(\mathbf1_{\Gamma_{n,j}}q_{n,p}^{(j)}\mu)
=\beta^n(\pi_4)_*\mu,\qquad j=0,1,2,
}
$$
$$
\boxed{
(\pi_4)_*(\mathfrak q_{n,p}\mu)
=\beta^n(\pi_4)_*\mu.
}
\tag{11}
$$

**证明。** 用 (8) 的真实 $D_j$ 核还原 $D_j/\kappa^n$，
保 $E_j,\pi_4$。再按 $E_j$ 次数用其真实单位因子
$1-\beta\kappa^m=1+\lambda\kappa^m$ 消去 (6) 中的 $u_m$。
最后 (10) 对同一个
$Q_p(\zeta_jC,F,G)$ 给完整来源返回；
$\zeta_j^6=1$ 保固定 $-C^6/8$，其余十个方向仍被 (10) 消掉。
这逐项是 R536 的原有限运算，系数 $x_p$ 无需改变。
三支不交且平均系数为 $1/3$，得到第二式。证毕。

(11) 允许任意原四输出的连续混合测试，包括
$L=(W-Y)/2$ 的单位条件和任何 $G$ 条件。
它不允许免费加入 $u_1,u_2$ 等不属于 $\pi_4$ 的 cut。
它给第三来源自身的中央乘 $\beta^n$，
不将该中央认作原 $S/T$ 的已知零。

## 4. 原五深网格上的质量自动同时消去

保持实际原域
$$
\mathcal D_n=
\{\xi_1,\xi_2,\xi_3,c,d_0\in p^n,\ x\ {\rm unit}\}.
\tag{12}
$$
$H$ 保此域且与五个深输入的共同缩放交换。
故 $\rho_0,\eta,h$ 在这同一域都以 $\beta^{5n}$ 返回，
并且几何上仍只有 $\Gamma_{n,0}$ 命中。
在 $\mathcal D_n$ 上 $\mathfrak q_{n,p}=q_{n,p}^{(0)}/3$。

缩放五深变量为 $T$，置
$$
\mathcal P_p(T;\boldsymbol t,x)=
(\mathcal R_pP_p)(D_f,e_0x+TE_f,g_0x+TG_f),
\tag{13}
$$
其中 $\boldsymbol t=(\xi_1,\xi_2,\xi_3,c,d_0)$，原准确行为
$$
\begin{aligned}
D_f&=(1,\omega^2,-2\omega,1,2+3\omega),\\
E_f&=((-11-28\omega)/3,-1-\omega,(14+22\omega)/3,1,2+3\omega),\\
G_f&=((-37-14\omega)/3,21-3\omega,(-5+17\omega)/3,
                                      3-2\omega,12+11\omega),\\
e_0&=(-14-28\omega)/3,\qquad g_0=(32+31\omega)/3.
\end{aligned}
\tag{14}
$$
仍是总次数六的原多项式。

**引理。** 对任何只经 $D_f,E_f,G_f$ 依赖最后两个深输入的
次数至多六的多项式，其五深变量积分在 $\eta$ 与 $\rho_0$ 之间
准确相差固定比
$$
\boxed{
r_\eta=-\frac{12+8\omega}{7},
\qquad r_h=r_\eta+\frac12=-\frac{17+16\omega}{14}.
}
\tag{15}
$$
自由输入 $x$ 的完整测度和任意测试保持。

**证明。** 三个原独立 sigma 的最小次数各为一；
末两输入在 $\rho_0$、$\eta$ 都是总型二、最小次数二的来源。
总次数至多六时，唯一可能的非零五输入总次数是五，
即前三输入各取第一矩，末两输入取二次矩。
(14) 的末两输入只经 $M=c+(2+3\omega)d_0$ 出现，
所以只有 $M^2$ 的二次矩需要比较。
原 $\sigma\otimes\sigma$ 给 $2(2+3\omega)\Omega^2$；
由 (7)，$\omega^2H_*$ 给
$\omega^2\cdot2(2\omega)(-2\omega)\Omega^2=-8\omega\Omega^2$。
其比为 (15) 的 $r_\eta$。无更高次数项可贡献，
所以这不是模 $p$ 或低阶近似。证毕。

R536 的六条准确质量方程使
$\rho_0$ 对 (13) 的条件积分作为 $T,x$ 的多项式恒为零。
(15) 立即给

**定理3。** 对 $\mu=\rho_0,\eta,h$、任意 $n\ge1$
和任意自由输入的连续函数 $a(x)$，
$$
\boxed{
\int_{\mathcal D_n}a(x)\,\mathfrak q_{n,p}\,d\mu=0.
}
\tag{16}
$$
特别全部常数 log、$\log\langle x\rangle$、固定尺度 log 都准确消失。
同一结论对未平均的 $q_{n,p}^{(0)}$ 成立。
这里没有增加七行矩阵的方程，也没有按参数样本重选测试。

## 5. 同一原网格的三个真实中央首项

先用未平均的 $q_{n,p}^{(0)}$ 定义
$$
C^\mu_{L,n}
=\int_{\mathcal D_n}d\log\langle L\rangle\,q_{n,p}^{(0)}\,d\mu,
\quad L=Y,W,W_2.
\tag{17}
$$
平均测试的值是其 $1/3$。
原 $L=a_Lx+TZ_L$ 的全部行保 R531：
$$
\begin{array}{c|c|c}
L&a_L&Z_L\\ \hline
Y&\bar\gamma&(\delta,2\delta,\gamma,1,2)\\
W&\bar\gamma&(\delta,2\delta,\gamma,3\delta,4)\\
W_2&3+2\omega&(\gamma,2\delta,6+3\omega,-1+\omega,4).
\end{array}
\tag{18}
$$
在整原来源上设
$$
\mathcal A^\mu_L(T)
=\frac{d}{b\Omega^6}
\int_{x\ {\rm unit}}\int
\log\langle a_Lx+TZ_L\rangle\,
\mathcal P_p(T;\boldsymbol t,x)\,d\mu.
$$
(12)–(16) 给
$$
C^\mu_{L,n}=\beta^{5n}\mathcal A^\mu_L(\kappa^n),
\qquad \mathcal A^\mu_L(0)=0.
\tag{19}
$$
第一项只有原 $D_f^4$ 的部分存活，原第七行
$\mathcal L=1$ 仍准确有效。因此
$$
\boxed{
[T]\mathcal A^\mu_L
=\frac db(1+\lambda\kappa)\alpha^\mu_L.
}
\tag{20}
$$

全部固定常数如下：
$$
\begin{array}{c|c|c|c}
L&\alpha^{\rho_0}_L&\alpha^\eta_L&\alpha^h_L\\ \hline
Y&(-36-54\omega)/49&(-36+72\omega)/49&(-54+45\omega)/49\\
W&(-180-102\omega)/49&(-36+72\omega)/49&(-18+3\omega)/7\\
W_2&(-60-6\omega)/49&(-12+24\omega)/49&(-6+3\omega)/7.
\end{array}
\tag{21}
$$

**完整系数证明。** 原列为
$$
\alpha^{\rho_0}_L=-\frac{
[\xi_1\xi_2\xi_3cd_0]D_f^4 Z_L}{84a_L}.
$$
$\eta$ 的正确列必须同时变换两个行并乘其源系数：
$$
\boxed{
\alpha^\eta_L=-\frac{\omega^2
[\xi_1\xi_2\xi_3cd_0](D_fH)^4(Z_LH)}{84a_L}.
}
\tag{22}
$$
这里 $H$ 只在最后两个位置作用。真实完整值为
$$
D_fH=(1,\omega^2,-2\omega,2\omega,-2\omega),
$$
$$
\begin{aligned}
Z_YH&=(\delta,2\delta,\gamma,(3+\omega)/2,-(3+4\omega)/2),\\
Z_WH&=(\delta,2\delta,\gamma,(11+\omega)/2,(5-4\omega)/2),\\
Z_{W_2}H&=(\gamma,2\delta,6+3\omega,5+5\omega/2,-(1+\omega)/2).
\end{aligned}
\tag{23}
$$
对任意五行 $a,z$，所需系数准确是
$4!\sum_i z_i\prod_{j\ne i}a_j$。
(22) 的含 $\omega^2$ 分子依次为
$-432\omega,-432\omega,144$；代入 (18) 得 $\eta$ 列。
再加原列的一半即 $h$ 列。
第4节已经消掉所有多项式首项所乘的常数 log，
所以 (20) 没有被遗漏的未知 $x\log x$ 项。证毕。

三条 $\eta$ 首项的范数为
$$
1296/343,\qquad1296/343,\qquad144/343;
$$
三条 $h$ 首项的范数为
$$
1053/343,\qquad387/49,\qquad9/7.
\tag{24}
$$
其分子素因子最多为 $2,3,13,43$，故在同一个 $p\ge71$ ray
都是单位，没有新增有限坏集。
所有系数整，原 log 的统一全尾界仍为
$$
v_p([T^r]\mathcal A^\mu_L)\ge-\lfloor\log_pr\rfloor.
\tag{25}
$$
于是
$$
\boxed{v_p(C^\eta_{L,n})=v_p(C^h_{L,n})=n
\quad(L=Y,W,W_2;\ n\ge1).}
\tag{26}
$$
平均测试除以 $3$ 后赋值不变。

## 6. 第三来源的实际 Y−W 差更深一阶

(21) 给准确的相等而不是剩余类相等：
$\alpha^\eta_Y=\alpha^\eta_W$。
因此 (19)–(25) 直接给
$$
\boxed{v_p(C^\eta_{Y,n}-C^\eta_{W,n})\ge2n.}
\tag{27}
$$
这里使用原未归一 $Y,W$，没有插入 $6\delta$。

相比之下，
$$
\alpha^h_Y-\alpha^h_W
=\frac{24(3+\omega)}{49},\qquad
N\!\left(\frac{24(3+\omega)}{49}\right)=\frac{576}{343}
$$
是同 ray 的单位，故
$$
\boxed{v_p(C^h_{Y,n}-C^h_{W,n})=n.}
\tag{28}
$$
这些都保实际共同 $\mathcal D_n$、同一原 $q_{n,p}^{(0)}$，
不是先独立改变两个 Mellin 变量。
对原 $\mathfrak q_{n,p}$ 同样成立。

## 7. 当前实际边界

(11) 现在让整个两态的原 $\pi_4$ 测试都严格返回，
(16) 则同时支付同一实际网格上的全部自由输入质量。
所以 R544/R548 的 $L$ 单位、$Y/W$ 混合权在没有额外
$u_j$ 条件时，可以直接用 (11)；不再需要凭边际或猜 $H$ 不变性。

剩余 native 条带却还含 $u_1,u_2$ 深条件，
这两个条件不属于 $\pi_4$，并且与 $D_j/E_j$ 核并不免费交换。
本篇的 (26)–(28) 只计算明确子域，未删除其真实补域。
尤其第三来源 $Y-W$ 的首项消失不是整个积分为零；
(11) 对其完整中央也不新增算术零假设。
继续必须在原实际条带中联立这些准确返回与 R548/R553 的全来源式。

## 依赖及精确计算

- [R531](R531-hidden-two-frame-native-central-carry.md)，四个 entire scalar 核、全框架及各原观察。
- [R536](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)，同一七行右逆、原 $D_*$、完整 carry 测试。
- [R541](R541-original-degree8-second-state-and-exact-sigma-transport.md)，真实 $H$ 与所有原输入域。
- [R548](R548-original-whole-third-source-cm-reflection-and-complete-positive-spectrum.md)，本篇所用新 $h$。
- [R553](R553-original-norm2-two-theta-source-and-mixed-unit-domain.md)，完整低度两态来源。
- [精确有理/CM 计算脚本](../scripts/check-r557-third-source-common-carry-moments.js)及[输出](../scripts/check-r557-third-source-common-carry-moments.json)记录 (15)、(22)–(24)。
  这些是特征零全系数计算，不用有限素数试验代替原单位性。
