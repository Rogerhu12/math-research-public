# R461：原八 hook 的完整端口盲方向与九行同规范接口

日期：2026-11-16。**完整原式纸面证明；没有执行 profile、积分、符号程序、矩阵秩或新的科学作业。**

本稿在同一真实圆、指定二次高度端口与原 $L_f$ 周期算子上，推进已存在完整 period 特解之后的规范问题。它不以 signed 成本见证代替 actual 全 partial 支付。

新增两项明确结论。第一，原反正切方向 $B_\varepsilon$ 的整个 profile $B_\varepsilon D_\theta$ 落在原全部十三行的核，不只使最高 $P_2$ 行为零；其 hook 响应可由一个同步的二阶规范准确抵消 period，仍保指定端口。第二，原真实复制库本身给出三条第三合法矩的全相位右逆，且这个右逆同时杀全部十个端口系数并保持 period。因此三条合法矩可以最后支付，不改变其余任何门。

[R459](R459-one-common-signed-witness-for-all-internal-fluxes-of-the-equal-width-library.md) 已在从起点固定的同宽、一对退化点母库上给出同一个 signed $V_\#$，保持 $J^+=0$、全部角色的 $A_f$ partial 为零并有 $\lambda_+=1$。在原 $\tau$ 与 incoming 的固定读法下，[R460](R460-automatic-simple-critical-point-residues-and-complete-smooth-period-gluing.md) 已使其两条 period 具有真正双 collar 光滑特解。这里的 gap 积分修正和原右锚恢复仍须进入下文九行的真实右端；这个 signed 事实不是实际成本已能实现。

由此，完整同规范问题准确只需先保最高两个特解类值，再处理原九行。若用原 $d_f(P)=\eta\ne0$ 支路清第一最高值，八个固定 hook 参数在九行上的有效候选由六个明确方向生成；这里不声称它们的像有六维，更不允许对不同相位另选成本。原 finite-word 的所有基准和实际 incoming 仍留在目标内。

直接来源：[R312](R312-quadratic-height-ports-and-rational-arctangent-logarithmic-ruling.md)、[R321](R321-complete-single-arctangent-gates-and-ten-dimensional-joint-control.md)、[R326](R326-one-global-second-gauge-pays-the-complete-rational-port-and-preserves-joint-cost.md)、[R327](R327-analytic-packet-period-kernels-and-a-finite-same-gauge-joint-system.md)、[R394](R394-conditional-complete-period-and-finite-same-gauge-interface.md)、[R437](R437-highest-rational-gauge-row-vanishes-on-the-complete-period-kernel.md)、[R444](R444-original-hook-response-action-and-the-highest-second-period-blind-row.md)、[R445](R445-two-exact-highest-gauge-null-directions-and-the-complete-P-self-formula.md)、[R455](R455-four-natural-moments-with-one-common-degenerate-pair-and-twenty-targets.md)及 R460。

## 1. 固定原十三行和同一个 period 方程

保同一合法窗口、右锚、原有限母库与全部真实复制。原闭背景满足
$$
M=0,\qquad T=\tau\mathfrak H,\quad \tau\ne0.
$$
指定端口为
$$
h=H(1+\varepsilon\sigma^2),\qquad
H>0,\quad\varepsilon>0,\quad k=\kappa\ne0,\quad\omega=0.
$$
记
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f^2-\phi_\theta^2,\qquad \Delta=f^2-g^2.
$$
原 E8 名称取
$$
P=r_0,\ R=r_1,\ S=s_0,\ L=p_0,\ U=s_1,\ V=p_1,\ T=t_1,\ Y=p_2.
$$
本节 $T=t_1$ 是二次算子方向，不与整个第三量 $T_{\rm total}=\tau\mathfrak H$ 混用。

R326 的两个原 history 部分是
$$
\mathsf o=\mathsf Q+EB,\qquad
E=\frac{\arctan(\sqrt\varepsilon\,\sigma)}{\sqrt\varepsilon},
\qquad B=B_\varepsilon=aR-2eL+eU+\beta T,
$$
$$
a=\frac{(1+\kappa^2)(\varepsilon-2-2\kappa^2)}{32H^2},
\qquad e=\frac{\kappa(1+\kappa^2)}{4H},
\qquad \beta=-\frac{\varepsilon}{4}\ne0.
\tag{1}
$$
原三矩使每个 $XD_\theta$、$X\Delta$、$X(f,g)$ 真紧，$X\in E8$。单包 $X(u_i,u_i)$ 的真实左二次尾仍保留。

记
$$
\mathcal L_\theta(k)=\mathbf I(\phi_\theta,k)\in\mathbb R^3,
$$
$$
\mathcal T_\theta(k)
=\bigl((P_{\ell,\theta}(k))_{\ell=-4}^{2},
(H_{B,j,\theta}(k))_{j=0}^{2}\bigr)\in\mathbb R^{10}.
\tag{2}
$$
这些是 R326 原十三行，均对同一个紧 $k$ 线性。完整奇响应是
$$
\begin{aligned}
\widehat{\mathcal B}_\theta(k)
={}&2\mathcal T_\sigma(k;D_\theta)
-4\mathcal T_\sigma(\phi_\theta;\phi_\theta,k)\\
&-2\mathcal E_h(\mathsf oD_\theta,k)
+4\mathcal E_h\{\phi_\theta,\mathsf o(\phi_\theta,k)\}.
\end{aligned}
\tag{3}
$$
这里 $\mathcal T_\sigma$ 是原局部配对，不是(2)的十维向量。由原有理/反正切独立性，(3)恒零等价于(2)十行全零。额外平方与第三初值只在原 $\mathcal W_e=\operatorname{span}\{h^{-1},1,h\}$ 内，仍由一次真实第三 Gram 规范支付；并未从完整方程删掉。

本稿进入九行归约之前，明确假设两个原全函数特解已存在：
$$
L_fk_d=G_d,\qquad L_fk_e=G_e,\qquad
k_\theta^0=\sin^2\theta\,k_d+2\sin\theta\cos\theta\,k_e.
\tag{4}
$$
$G_d,G_e$ 保 R460(6)的实际 incoming、$2\tau$、原平台与右 collar。R460 给当前有限简单退化库的准确 range 条件；本稿不以一个有限矩阵反过来证明(4)。

## 2. B 方向的完整十三行恒零

R312(23)将整个 centered ruling 写成
$$
\widehat{\mathscr K}
=\mathscr R_{\rm rat}+E\mathscr R_E+E^2\mathscr R_2+L\mathscr R_L,
$$
其中
$$
\begin{aligned}
\mathscr R_E={}&
2\mathcal T_\sigma(BD;D)
-4\mathcal T_\sigma(\phi;\phi,BD)\\
&-2\mathcal E_h(\mathsf QD,BD)
+4\mathcal E_h\{\phi,\mathsf Q(\phi,BD)\},
\\
\mathscr R_2={}&-\mathcal E_h(BD,BD)
+2\mathcal E_h\{\phi,B(\phi,BD)\}.
\end{aligned}
\tag{5}
$$
这两式保原 local、chain、完整右锚和真实 self 尾；它们不是 principal 的定义。

在(3)直接代入真紧的 $k=BD_\theta$，再用 $\mathsf o=\mathsf Q+EB$，四个非 $E$ 项就是(5)第一式，剩下两项准确为 $2E\mathscr R_2$。因此
$$
\boxed{
\widehat{\mathcal B}_\theta(BD_\theta)
=\mathscr R_{E,\theta}+2E\,\mathscr R_{2,\theta}.
}
\tag{6}
$$
R321 及其后同一点构造已经支付完整七个 one-$E$ 与三个 square 值，故右侧逐相位为零。更逐行地，原定义给
$$
H_{B,j,\theta}(BD_\theta)=q_j(\theta),\qquad
P_{\ell,\theta}(BD_\theta)=\rho_\ell(\theta),
\tag{7}
$$
所以十行各自恒零。原八副本的完整 cubic 零式 R326(6)又给
$$
\mathbf I(\phi_\theta,BD_\theta)=0.
$$
于是
$$
\boxed{BD_\theta\in\ker\mathcal L_\theta\cap\ker\mathcal T_\theta
\quad\text{对全部 }\theta.}
\tag{8}
$$

原 hook 响应 $K_X=\mathcal B_X\mathfrak H$ 在当前固定圆上的完整成本为
$$
K_X(f^2,\phi_\theta)=2L_f(XD_\theta).
\tag{9}
$$
所以增加 signed 成本 $tK_B$ 时，同步改
$$
\delta k_\theta=-\frac t\tau BD_\theta
\tag{10}
$$
正好抵消全部 period 变化。由(8)，这个补偿不改变任何一条指定端口的十三行。它保原两个 seed、双 collar 和相位光滑。

(10)不要求 $L_f(BD_\theta)=0$。其作用是成本与同一 gauge 的准确配对。新的 $\mathcal W_e$ 平方/交叉仍按 R326 重新支付；其它路径段 ruling 和 actual prototype 基准不由(8)自动不变。

## 3. 三个第三合法矩可支付且不动全部端口行

### 3.1 使用的是完整 circle base

选原十二副本中的一个完整基本块 $(F,G)$。它已经包含完整编码圆及原八副本 cubic 包装，因而
$$
\mathbf I(F,F)=\mathbf I(G,G)=\mu,\qquad
\mathbf I(F,G)=0,\qquad \mu_0>0.
\tag{11}
$$
(11)的逐块来源是 R280(3)、(11)、(17)：每个正、负完整编码布局各自满足
$$
\sum_i R_i t_i^q=\sum_i T_i t_i^q=0
\qquad(0\le q\le10),
$$
而其真实微包三矩为 $\mu_i=m(1,t_i,t_i^2+\nu)$。取 $q=0,1,2$ 即在每个布局内分别给出 $\sum_iR_i\mu_i=\sum_iT_i\mu_i=0$，也就是 $\mathbf I(F,F)=\mathbf I(G,G)$ 与 $\mathbf I(F,G)=0$。后续八、十二包装及外五块只作原已固定的整块平移、幅度和 $g$ 翻号，逐块保留这个二次闭合。R412/R431/R455 的四个 $q$ 约束和 $F^\star$ 图册中的母形替换又保持各真实三矩 $\mu_i$，所以同一结论保留到当前最终母库。这一来源不把八副本的三次权 $\alpha_\ell^3$ 代替二次权。

原八复制还给
$$
I_j\{a,X(b,c)\}=0
\quad
(a,b,c\in\operatorname{span}(F,G),\ X\in E8,\ j=0,1,2).
\tag{12}
$$
其真实跨尾由 R326(7)支付：compact outer 与任何二次多项式的三个 $I_j$ 全部正交，$I_2$ 的 $2a'b'$ 项不能省。

同一个八复制还准确给
$$
\mathcal T_\sigma(a;b,c)=0
\quad(a,b,c\in\operatorname{span}(F,G)).
\tag{13}
$$
证明直接用 R326(30)的完整紧槽式。其 integrand 为 local 三次式，显式 $x$ 次数最多五：最高项来自 $Q_{\rm g}^2x\,a'''b''c''$；其余项次数不更高。共同平移后是次数至多五的多项式。原每个副本三次幅权为
$\alpha_\ell^3=(-1)^\ell\binom7\ell$，第七有限差分使其准确为零。不同副本的 local 三次乘积没有重叠；不需要给某个非紧槽偷用紧版公式。

### 3.2 完整 base 的 F/G 都杀十行

将实际最终圆拆成这些不交完整 base，记其中一块为 $(F_j,G_j)$。它们均为最细 $u_i$ 的固定线性组合，故 R327/R460 给
$$
F_j,G_j\in\ker L_f.
\tag{14}
$$
对(3)的任一 $k=F_j$ 或 $G_j$，local T 两项由(13)为零。history 项在本 base 内由(12)为零；其他 base 只留下真二次尾，与紧 outer 的三个矩精确正交。因而
$$
\boxed{
\mathcal T_\theta(F_j)=\mathcal T_\theta(G_j)=0
\quad\text{对全部 }\theta.
}
\tag{15}
$$
这里的(15)包括 $P_2$ 和全部其余九行，而不只是取一个最高系数。

### 3.3 三个实际中心给一个固定可逆矩阵

从同一个十二复制族取三个不同真实中心 $t_1,t_2,t_3$。吸收其外层固定幅度后，它们形如
$$
F_j=\gamma_j T_{t_j}F,\qquad
G_j=\epsilon_j\gamma_j T_{t_j}G,\qquad
\gamma_j\ne0,\quad\epsilon_j\in\{-1,1\}.
$$
每块仍满足(11)，其三矩是
$$
\mu_j=\gamma_j^2
(\mu_0,\ \mu_1+t_j\mu_0,\
\mu_2+2t_j\mu_1+t_j^2\mu_0).
\tag{16}
$$
所以
$$
\det(\mu_1,\mu_2,\mu_3)
=\gamma_1^2\gamma_2^2\gamma_3^2\mu_0^3
\prod_{i<j}(t_j-t_i)\ne0.
\tag{17}
$$
这里下标 $\mu_j$ 指列向量，原矩分量仍是(16)中 $\mu_0,\mu_1,\mu_2$。

令 $\mathsf M=(\mu_1,\mu_2,\mu_3)$，并定义
$$
z_{j,\theta}=F_j\cos\theta+G_j\sin\theta,\qquad
\mathscr R_\theta y
=\sum_{j=1}^3(\mathsf M^{-1}y)_j z_{j,\theta}.
\tag{18}
$$
不交支撑与(11)给
$$
\mathbf I(\phi_\theta,z_{j,\theta})=\mu_j.
$$
因此
$$
\boxed{
\mathcal L_\theta\mathscr R_\theta=\operatorname{Id}_{\mathbb R^3},
\qquad
L_f\mathscr R_\theta=0,\qquad
\mathcal T_\theta\mathscr R_\theta=0 .
}
\tag{19}
$$
这是同一实际库内、全相位光滑的明确右逆，没有按相位重新选三包或移动中心。只需三个完整 base 是同一固定 base 的真实平移复制；不要求所有最细包共用一个宽度。

对任意候选 $k_\theta$，置
$$
\Pi_\theta k_\theta
=k_\theta-\mathscr R_\theta\mathcal L_\theta(k_\theta).
\tag{20}
$$
它准确支付三个合法矩，同时不改变 period、任一端口行或种子。若 $k_\theta$ 光滑周期且在 $0,\pi$ 为零，(20)仍有这些性质。原第三 Gram 规范随后处理 $\mathcal W_e$，其对完整 period 的变化为零。

## 4. 先保最高两个特解类值，再保九行

R437 的完整恒等式是
$$
P_{2,\theta}(k)=\frac{\kappa}{24}\ell_f(k),\qquad
\ell_f(k)=I_2\{Y(f,f),k\},\qquad
\ell_f|_{\ker L_f}=0.
\tag{21}
$$
故(4)之后最高行的准确条件仍是
$$
b_d:=\ell_f(k_d)=0,\qquad b_e:=\ell_f(k_e)=0.
\tag{22}
$$
(19)不会改变这两个数。R450 的最高 e 消去只有在其实际宏复制及真实 period range 前提下才能使用；没有采用该包装时，仍保 $b_e$ 原值。

删去 $P_2$，记
$$
\mathcal B_\theta(k)
=\bigl((P_{\ell,\theta}(k))_{\ell=-4}^{1},
(H_{B,j,\theta}(k))_{j=0}^{2}\bigr)\in\mathbb R^9.
\tag{23}
$$
这只是原九行，不新定义 profile 观察。

令 $v_\nu$ 依次为原 $u_i,\chi_i$，定义
$$
D_\theta=(\mathcal B_\theta(v_1),\ldots,\mathcal B_\theta(v_{2n})).
\tag{24}
$$
间隙函数仍全盲。由(19)，
$$
\mathcal B_\theta(\ker L_f\cap\ker\mathcal L_\theta)
=\mathcal B_\theta(\ker L_f).
\tag{25}
$$
所以无需在(24)里删列或另作会改变九行的 Schur 补偿。任意九行解都可以最后用(20)合法化。

在(4)、(22)成立后，完整十三行与 period 同时可解，准确等价于：存在光滑周期的 $\eta_\theta\in\mathbb R^{2n}$，满足
$$
\boxed{
D_\theta\eta_\theta
=-\mathcal B_\theta(\sin\theta\,k_d+2\cos\theta\,k_e).
}
\tag{26}
$$
由其构造
$$
\widetilde k_\theta=
\sin\theta\left[
\sin\theta\,k_d+2\cos\theta\,k_e+
\sum_\nu\eta_\nu(\theta)v_\nu\right],
\qquad
k_\theta=\Pi_\theta\widetilde k_\theta.
\tag{27}
$$
这同时保原两个 seed。反向从任何完整解减去(4)，按 R327/R460 的核分解并作 seed 的 Hadamard 除法，即得(26)。没有在 $p=f'$ 的零点除一个不合法的 profile；此处只除相位 $\sin\theta$，两种子已真实为零。

(26)有九个显示行，不授其秩为九。特解的 gap 积分修正、原仿射尾及 actual incoming 全部已经进入右侧；不能把它们从这个原目标中删除。

## 5. 原八 hook 的固定六参数余作用

原每个 $K_X$ 都保持 signed whole $J^+$、全部内部 partial 与消 self 的 C 行；这由 R444 的完整(9)与原通量身份给出。这里消费的是原响应空间，不把一个实际 word 的全部基准也称为零。

令
$$
d_f(X)=\ell_f(X\Delta),\qquad
e_f(X)=\ell_f(X(f,g)).
$$
当前真实十二包装已给 $e_f(X)=0$ 对全部 $X\in E8$；R445又给
$d_f(B)=d_f(Y)=0$。R455 的同一点二十目标允许固定
$$
d_f(P)=\eta_P\ne0.
\tag{28}
$$
因此在 signed 响应层先取
$$
Z_0=\frac{\tau b_d}{\eta_P}P,
\qquad
k_d\longmapsto k_d-Z_0\Delta/\tau,\quad
k_e\longmapsto k_e+Z_0(f,g)/\tau.
\tag{29}
$$
它使第一最高值为零，第二最高值不变。若 $b_e\ne0$，这整个八 hook 支路仍不能支付最高行。

现在假设两个最高值均已通过。余 hook 必须取同一个固定
$Z\in\ker d_f\subset E8$。定义六个明确方向
$$
Z_X=X-\frac{d_f(X)}{\eta_P}P,
\qquad X\in\{R,S,L,U,V,Y\}.
\tag{30}
$$
其中 $Z_Y=Y$。因为(1)的 $\beta\ne0$，有
$$
Z_T=-\frac a\beta Z_R+\frac{2e}\beta Z_L
-\frac e\beta Z_U+\frac1\beta B.
\tag{31}
$$
故 $\ker d_f$ 由这六个方向和 B 生成。由(8)，B 的全部九行作用恒零。

对六个**固定实参数** $z_X$ 取 $Z=\sum_Xz_XZ_X$。原同步特解改变为
$$
\delta k_\theta=-\frac1\tau ZD_\theta
=-\frac{\sin\theta}{\tau}
 Z\{\sin\theta\,\Delta-2\cos\theta(f,g)\}.
\tag{32}
$$
它的三个合法矩已经由 R326 cubic 恒等式为零，最高行也因 $d_f(Z)=e_f(Z)=0$ 为零。九行的真实作用准确是
$$
\mathcal H_{\theta,X}
=\frac1\tau
\mathcal B_\theta\!
\left(Z_X\{\sin\theta\,\Delta-2\cos\theta(f,g)\}\right).
\tag{33}
$$
于是八 hook 支路与周期核共同支付原全部十三行的准确剩余方程为
$$
\boxed{
D_\theta\eta_\theta
=b_\theta+\sum_{X\in\{R,S,L,U,V,Y\}}z_X\mathcal H_{\theta,X},
\quad
b_\theta=-\mathcal B_\theta(\sin\theta\,k_d+2\cos\theta\,k_e).
}
\tag{34}
$$
$z_X$ 不依赖相位；$\eta_\theta$ 才是允许随相位变化的 period 核系数。不能把六个响应列逐相位自由赋值，也不能据有六个候选方向宣布其真正像维数为六。

## 6. 精确的有限相位检验，保全部秩降点

(24)的条目仍是原次数至多二的相位多项式。(33)与(34)右端次数至多三。第3节的合法化没有引入 Gram 分母，也没有改变这些原度数。

如需把(34)写成有限条件，沿 R394 令 $\zeta=e^{i\theta}$，
$$
M(\zeta)=\zeta^2D_\theta,\qquad
\mathfrak b(\zeta;z)=\zeta^3\left(b_\theta+\sum_Xz_X\mathcal H_{\theta,X}\right),
\qquad \xi=\zeta\eta .
$$
则
$$
M(\zeta)\xi(\zeta)=\mathfrak b(\zeta;z),\qquad |\zeta|=1,
\tag{35}
$$
$M$ 逐项次数至多4，$\mathfrak b$ 至多6。取原多项式 Smith 消元
$UMV=\operatorname{diag}(d_1,\ldots,d_r,0)$；这里只给准确纸面判据，不执行任何新消元。存在一个共同实向量 z 与光滑相位解，恰好当：

- $U\mathfrak b(\zeta;z)$ 的所有零行作为多项式恒零；
- 对每个非零 $d_j$ 的单位圆根，$U\mathfrak b$ 的对应分量按其全部重数准确消失。

这些都是同一个固定 z 的实线性或共轭成对线性条件。满足后按原商式恢复解析相位解，再取实部、使用(27)与(20)，得到原允许的同一个二阶规范。

若 $r>0$，原 determinantal-divisor 论证给
$$
\sum_{\substack{|\zeta_*|=1\\j\le r}}
\operatorname{ord}_{\zeta_*}d_j
\le4r\le36.
\tag{36}
$$
它只界非零行的局部整除重数；不把零行多项式条件算成独立36行。若 $r=0$，条件就是整个右端恒零。这里不重算旧十三行秩，也不把上界当实际秩。

## 7. 真实 incoming 与实际 prototype 的全部代价

(29)—(34)是固定 profiles 与端口参数下，原 signed 响应对两个真实 period 目标的准确作用。真实路径改动若还产生 $\delta X_*$，则 R437 的原公式必须同时计入
$$
\delta k_d=\delta X_*\Delta-Z\Delta/\tau,\qquad
\delta k_e=-\delta X_*(f,g)+Z(f,g)/\tau
\tag{37}
$$
以及改变后完整 canonical 基准的特解；不能把 $\delta X_*$ 当自由参数或直接置零。它由同一个实际词与其位置决定。

若实际实现写成
$$
V_{\rm base}(t,n)+\sum_Xt_XK_{Z_X},
$$
原 $V_{\rm base}$、桥、真倒行、重复 prototype 和后置商校正的
$J^+$、全部 partial、最高两个值、(34)九行及 incoming 代价必须在同一个目标里支付。某个原型的自成本可按重复次数线性增长，不能塞入与次数无关的误差。

因此本稿没有从 R459 的 signed $\lambda_+=1$ 核见证推出新增 partial 或九行的 actual 截面。它也没有证明(34)已经可解。新成果是原几何内明确可用的三矩右逆、一个完整十三行盲 hook、以及八 hook 在剩余原九行上的唯一正确固定参数接口。

当(4)、最高两值及(34)全部成立时，指定端口的完整 ruling 与整个第四 period 可用同一个二阶规范和一个第三 Gram 规范同时完成。其它路径段 ruling、与实际成本基准的共同实现、高阶收敛和最终几何目标仍需另付。
