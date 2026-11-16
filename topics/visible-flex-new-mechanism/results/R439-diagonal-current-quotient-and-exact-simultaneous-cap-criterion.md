# R439：完整退化点 current 的六次对角剩余与真实全点补偿判据

日期：2026-11-16。**纸面原式推导，并消费 R434 已完成的唯一联合像；本稿没有执行新的符号消元、profile 求值、退化点秩、人工测试或研究运行。**

[R434](R434-complete-self-kernel-and-three-tail-current-image-on-144-original-responses.md) 已确定同一 144 个原响应的 whole-self 核在三个尾矩、全部十三 current 坐标中的像为 32 维。本稿把其七条关系合为一个有明确原几何来源的六次多项式，给出七个完整剩余代表，以及固定实际圆上全部退化点的准确补偿判据。

结论只使用这一已付原响应模块。它不声称七条关系对整个响应空间成立，也不声称 actual whole-$E$、universal ordered 零已使这个多项式为零。原路径的全部 history、真实 suffix、原型基准和同一个二阶规范继续保留。

直接来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R292](R292-zero-platform-periods-and-ordered-second-history-matrix.md)、[R405](R405-common-exterior-packets-and-local-ordered-currents-at-all-internal-degeneracies.md)、[R408](R408-independent-second-gauge-invariant-fluxes-and-natural-character-extension.md)、[R431](R431-common-exterior-degeneracies-in-the-complete-four-constraint-nineteen-target-library.md)、[R433](R433-actual-universal-ordered-flux-zero-and-explicit-local-cap-currents.md)、R434 及 [R437](R437-highest-rational-gauge-row-vanishes-on-the-complete-period-kernel.md)。R405/R408 的原式由本文逐处重列；同一实际母库采用 R431 的任意有限共同退化点，不限于旧特殊的一对。

## 1. 固定原 current，而非只保含 profile 的单项

记
$$
p=u',\qquad r=u'',\qquad t=u''',\qquad
\mathcal A(u)=6pt-2r^2.
$$
固定原路径满足 $M=0,\ T=\tau_{\rm hook}\mathfrak H$，并取 R433 已实际可构成的
$$
E(V)=(\pi V,\mathcal QV)=0,\qquad O_{\rm all}(V)=0.
\tag{1}
$$
这里 $O_{\rm all}$ 是 universal ordered $3+2$ 自然读出；没有要求所有 universal self 自然通量为零。

对右包的原三矩 $n=(n_0,n_1,n_2)$，整个有序输出为
$$
\mathcal U_{V,n}(u)=4Q_{V,n}(u),
\qquad
Q_{V,n}=L_{V,n}+\sum_{j=0}^2m_j(x,n)J_j(u),
$$
$$
J_j(u)=\int_x^{r_*}
\{y^j(u''(y))^2+2\mathbf1_{j=2}(u'(y))^2\}\,dy.
\tag{2}
$$
全部 $n$ 依赖线性；先对真实右包成立，再由三个真实矩基线性延拓。whole $\mathcal Q=0$ 只给 $m_j''=0$，并没有删去 $m_j$ 的仿射部分。

写
$$
L=a u^2+bup+cur+dp^2+epr+fr^2,
\quad m_j=\alpha_jx+\beta_j,
$$
$$
M=m_0+xm_1+x^2m_2,\qquad
A_m=\alpha_0+\alpha_1x+\alpha_2x^2 .
\tag{3}
$$
为避免混淆，(3)中的 $e$ 是局部二次式系数；第6节几何坐标另写 $e_{\rm g}=hx+d_{\rm g}$。

原 ordered 恒等给 R433 六条 ODE，特别
$$
a'''=0,\qquad b''=-6a',\qquad c'=-2b.
\tag{4}
$$
故
$$
\begin{aligned}
a(x,n)&=A_0(n)+A_1(n)x+A_2(n)x^2,\\
b(x,n)&=B_0(n)+B_1(n)x-3A_1(n)x^2-2A_2(n)x^3,\\
c(x,n)&=C_0(n)-2B_0(n)x-B_1(n)x^2
       +2A_1(n)x^3+A_2(n)x^4.
\end{aligned}
\tag{5}
$$
所有六个参数仍对 $n$ 线性。

真实左平端的累计 current 定义为
$$
\mathcal K_{V,n}(x;u)
=\int_{\ell_u}^{x}u'(y)\mathcal U_{V,n}(u)''(y)\,dy .
\tag{6}
$$
在 $\mathcal A(u)(x)=0,\ p(x)\ne0$ 处，原式准确给
$$
\begin{aligned}
\frac{\mathcal K_{V,n}}4={}&
\frac{a''}{3}u^3+\left(a+\frac{b'}2\right)up^2
-bupr-\frac c6ur^2\\
&+\frac23(d'+b-2m_2)p^3
-2(d+A_m)p^2r+\left(2M-\frac{2e}3\right)pr^2.
\end{aligned}
\tag{7}
$$
这里仅代入该点 $t=r^2/(3p)$，不微分这个单点关系。式(6)全部原尾和左常数已由 R433 支付；(7)不是任意选取的 primitive。

六参数的 canonical representatives 取
$$
m=0,\qquad d(0)=d'(0)=e(0)=0.
$$
它们包含固定的 p-only 项。减去这六个完整代表后，余七基为
$$
p^3,\ p^2r,\ xp^2r,\ pr^2,\ xpr^2,\ x^2pr^2,\
S_7=2xp^3-5x^2p^2r+3x^3pr^2 .
\tag{8}
$$
因此三个矩共同给一个实 39 维形式空间 $\mathscr F$。本文所有关于 $\mathscr F$ 的等式都是完整退化点 current 的等式，不把只在 $\mathcal A=0$ 成立的式子扩成一般 $x$ 上的输出身份。

## 2. 七条已付关系恰是一个对角多项式

以 $A_\nu^{[j]},B_\nu^{[j]},C_0^{[j]}$ 表示(5)中 $n_j$ 的系数。定义线性映射
$$
\boxed{\mathfrak D:\mathscr F\longrightarrow\operatorname{Pol}_{\le6},
\qquad
\mathfrak D(F)(x)=c_F\bigl(x;(1,x,x^2)\bigr).}
\tag{9}
$$
这里 $(1,x,x^2)$ 是三矩线性式中的**代数代入**。没有声称它是一个非零紧包的三矩；尤其没有引入零宽度点质量作为实际包。

写 $\mathfrak D(F)=\sum_{\nu=0}^6d_\nu x^\nu$。直接展开(5)，得到
$$
\begin{array}{ll}
d_0=C_0^{[0]},&
d_1=C_0^{[1]}-2B_0^{[0]},\\
d_2=C_0^{[2]}-2B_0^{[1]}-B_1^{[0]},&
d_3=2A_1^{[0]}-B_1^{[1]}-2B_0^{[2]},\\
d_4=A_2^{[0]}+2A_1^{[1]}-B_1^{[2]},&
d_5=A_2^{[1]}+2A_1^{[2]},\\
d_6=A_2^{[2]}.&
\end{array}
\tag{10}
$$
它们恰是 R434 七条 annihilator 的重新排序及非零常数倍。注意 $A_0^{[j]}$ 全部不出现，p-only 七基也全部不出现。

令 $\mathscr R_{144,0}$ 表示 R434 同一 144 标签空间中的完整 $\mathcal Q$ 核，并令
$\mathcal C:\mathscr R_{144,0}\to\mathscr F$ 为三个真实尾矩的共同 current 映射。所有原标签的 pure 已为零。R434 的 32 维像及七条完整关系遂等价于
$$
\boxed{\mathcal C(\mathscr R_{144,0})=\ker\mathfrak D.}
\tag{11}
$$
这是一个共同原成本提升，不是对三个矩分别选择成本。R434 已从同一原 source 重构 whole $\mathcal Q$ 和三个 current；这里不重复该计算，也没有新增任何源列。

(11)立即说明：一个完整形式目标可以由该模块准确抵消，当且仅当它的对角多项式为零。此处“完整”指(7)—(8)全部 39 坐标，而非只选一个点、一个尾矩或六个含 $u$ 主单项。

## 3. 七个显式剩余代表

映射(9)满射，并可给一个完全显式的右逆。定义下列五个完整退化点多项式：
$$
\begin{aligned}
\Theta_0={}&-\frac16ur^2+\frac23xpr^2,\\
\Theta_1={}&\frac12upr-\frac16xur^2-\frac13p^3
+\frac13x^2pr^2,\\
\Theta_2={}&-\frac12up^2+xupr-\frac16x^2ur^2
+xp^3-\frac52x^2p^2r+\frac43x^3pr^2,\\
\Theta_3={}&-xup^2+\frac32x^2upr-\frac16x^3ur^2
+x^2p^3-2x^3p^2r+\frac56x^4pr^2,\\
\Theta_4={}&\frac23u^3-2x^2up^2+2x^3upr-\frac16x^4ur^2
+\frac43x^3p^3-2x^4p^2r+\frac23x^5pr^2.
\end{aligned}
\tag{12}
$$
这些依次是 R433 的完整 $C_0,-B_0/2,-B_1,A_1/2,A_2$ 代表。故其相应 $c$ 系数依次为 $1,x,x^2,x^3,x^4$。例如 $\Theta_1$ 中的 $-p^3/3+x^2pr^2/3$ 必须保留；删除它们会改变原坐标映射。

对 $D(x)=\sum_{\nu=0}^6d_\nu x^\nu$，定义
$$
\boxed{
\mathfrak S(D)
=(d_0n_0+d_1n_1+d_2n_2)\Theta_0
+n_2(d_3\Theta_1+d_4\Theta_2+d_5\Theta_3+d_6\Theta_4).
}
\tag{13}
$$
$\mathfrak S(D)$ 的规范是 $\mathcal K/4$。由(12)，
$$
\mathfrak D\mathfrak S(D)=D.
\tag{14}
$$
于是任何 $F\in\mathscr F$ 有精确分解
$$
F=\underbrace{F-\mathfrak S(\mathfrak D F)}_{\in\ker\mathfrak D}
+\mathfrak S(\mathfrak D F).
\tag{15}
$$
结合(11)，存在同一个原响应组合 $R_F\in\mathscr R_{144,0}$，使
$$
F+\mathcal C(R_F)=\mathfrak S(\mathfrak D F).
\tag{16}
$$
因此 R434 的完整 32 维像把任意形式目标缩成(13)这七个明确剩余。右逆不是唯一的；不同选择相差一个已有共同响应像。本文不把(13)的七个形式代表称为实际原成本。

## 4. 固定实际母库上，全点像的准确充要条件

现在冻结 R431 的同一最终母库与全部真实复制。写
$$
f=\sum_i a_i u_i,\quad g=\sum_i b_i u_i,\quad
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i,
$$
$$
u_i(x)=U_i((x-\xi_i)/w_i),\qquad w_i>0.
\tag{17}
$$
各实际 $U_i$ 的全部外退化点都是共同参考母 $U_0$ 的
$\pm b_\alpha$，$\alpha=1,\ldots,m$；这里 $m$ 是原构造给出的有限数，本文不固定为一、三或其他数目。于是
$$
x_{i,\alpha,\pm}=\xi_i\pm w_i b_\alpha,\qquad
u_i^{(k)}(x_{i,\alpha,\pm})
=w_i^{-k}U_0^{(k)}(\pm b_\alpha).
\tag{18}
$$
右方的真实 suffix 为
$$
n_i=\sum_{j>i}(T_iR_j-R_iT_j)\mu(u_j).
\tag{19}
$$
保持当前排序、全部幅度及实际宽度；不得把(19)当成每个点独立可选的三维参数。

用(18)—(19)定义一个固定实线性求值映射
$$
\boxed{
\mathcal E_*:\mathscr F\longrightarrow\mathbb R^{N_*},
\quad
(\mathcal E_*F)_{i,\alpha,\pm}
=4a_i^3F(x_{i,\alpha,\pm},u_i,u_i',u_i'';n_i).
}
\tag{20}
$$
$N_*$ 只是所有被纳入的真实根数，可把零外幅或零 suffix 的零行原样留在其中。按 R389/R433 归一，真实两个内部通量的 self 消去组合恰为
$$
C_{i,\alpha,\pm}
=R_iH_{e,i}(x_{i,\alpha,\pm})+
T_iH_{d,i}(x_{i,\alpha,\pm})
=(\mathcal E_*F_V)_{i,\alpha,\pm}.
\tag{21}
$$
(20)中的因子四来自 $F_V=\mathcal K/4$，不能与实际 $a_i^3$ 合并丢失。

当前实际组合(21)能否由 R434 模块的**同一个有符号成本**同时消去，准确等价于
$$
-\mathcal E_*F_V\in\mathcal E_*(\ker\mathfrak D).
\tag{22}
$$
利用(15)，也等价于
$$
\mathcal E_*\mathfrak S(\mathfrak D F_V)
\in\mathcal E_*(\ker\mathfrak D).
\tag{23}
$$
更内在的写法是
$$
\boxed{
[\mathfrak D F_V]=0
\quad\text{于}\quad
\operatorname{Pol}_{\le6}/\mathfrak D(\ker\mathcal E_*).
}
\tag{24}
$$

**证明。** 若 $F_V+G$ 在 $\ker\mathcal E_*$ 中且
$G\in\ker\mathfrak D$，则 $\mathfrak D F_V$ 属于
$\mathfrak D(\ker\mathcal E_*)$。反之，若存在
$H\in\ker\mathcal E_*$ 满足 $\mathfrak D H=\mathfrak D F_V$，
则 $H-F_V\in\ker\mathfrak D$，由(11)得到一个共同原响应提升。
这同时给出自然同构
$$
\frac{\operatorname{im}\mathcal E_*}
     {\mathcal E_*(\ker\mathfrak D)}
\simeq
\frac{\operatorname{Pol}_{\le6}}
     {\mathfrak D(\ker\mathcal E_*)}.
\tag{25}
$$

因此整个实际 ordered-channel 商的维数在此模块下**至多七**，但本稿没有计算它等于多少。特别：

- $\mathfrak D F_V=0$ 是全点可补偿的充分条件，且是整个形式 current 可补偿的必要充分条件。
- $\mathfrak D F_V\ne0$ 不是当前有限根无解的证据；它可能落在 $\mathfrak D(\ker\mathcal E_*)$ 中。
- 七条形式关系不是七条已经证明独立的实际点约束；真实 suffix、镜点、宽度和零行均可降低求值商。

若选 R434 已付的任意 32 个共同像基组成矩阵 $B$，则实际矩阵为
$\mathcal E_*B$。不作新的秩假设时，(22)亦等价于：对每一个满足
$\lambda^{\mathsf T}\mathcal E_*B=0$ 的真实有限行向量，
$$
\lambda^{\mathsf T}\mathcal E_*
\mathfrak S(\mathfrak D F_V)=0.
\tag{26}
$$
它是准确的目标判据；没有把不同点、不同尾矩分别控制后再拼接。

## 5. 代数像不等于附零成本的实际插入

原 144 标签属于响应空间，故其 whole-$E$ 核还保持全部自然读出以及 universal ordered 读出。因而(16)、(22)的有符号改动保原 $J^+=(E,A,O_{\rm all})$。

但实际路径不能仅凭这句把某个有符号成本免费插入。R101/R392 的真实复制词含原型基准成本；若原型被复制 $n$ 次，其基准也乘 $n$。后置全 $J^+$ 截面的成本和新的 partial 值必须作为同一个有限参数映射保留，不能从投影为零推出整个新增成本为零。

本稿没有提供这个新增实际映射的正锥或截面。完成项是精确识别它应保留的七维形式剩余与实际求值商(24)。任何实际增强须沿同一有限构造同时处理原基准和该商；不得把(11)的 signed span 改称 actual control。

此外，(21)只消掉两个 period 中的同包 self 通道。另一个独立组合仍含真实 $S_{u_i}$ 部分通量。R435/R436 及后继的 self 核方向可消费此分解，但本稿不据此授所有 self 点已支付。

## 6. 对角多项式的原几何/history 表达

现在把(9)中的 $c$ 直接回接 R292/R405 原恢复，避免只给抽象坐标。

记
$$
z=x+\omega,\quad e_{\rm g}=hz-k,\quad Q=1+e_{\rm g}^2,\quad
\gamma=h_s,\quad
K_0=kz^2-\frac{k^2+1}{h}z.
$$
对固定三矩 $n$，R292 的真实二阶左尾为
$$
\Pi_n=(\mathfrak a_nz+t_n,\ p_nz,\ \eta_nz+q_n),
\qquad
\tau_n=(t_n)_s-\frac{\gamma}{h}t_n .
\tag{27}
$$
所有这些量由同一个累计第二矩阵和原初值恢复；不能独立指定。

第三交叉场满足
$$
W_C=\beta_np-\partial_x\beta_n\,u,
\qquad
\beta_n(s_0,x)=0,
$$
$$
(\beta_n)_s=\frac14\left[
\left(t_n-kq_n-\frac{\gamma\tau_n}{h}\right)\frac Q{h^2}
-\tau_n\partial_s\!\left(\frac Q{h^2}\right)\right].
\tag{28}
$$
$\beta_n$ 是二次 $x$ 多项式，$\tau_n$ 不依赖 outer $x$。二者对固定 $n$ 线性。

设
$$
A_C=\alpha_n r+\alpha_{1,n}p+\alpha_{0,n}u,
\qquad
\boxed{\alpha_n=\frac{\beta_n}{2}+\frac{\tau_nQ}{8h^2}.}
\tag{29}
$$
完整分子是 $(A_C,N_C,e_{\rm g}A_C-hW_C)$，其中
$$
N_C=\frac{q_n}{2}u-\frac{t_n+e_{\rm g}q_n}{4h}p.
\tag{30}
$$
于是 $N_C,W_C$ 只含 $u,p$，没有 $r$ 项。

原初阶协变导数为
$$
\nabla_sV_Y=
\left(0,h\left(u-\frac z2p\right),
       \gamma u-\frac{(e_{\rm g})_s}{2}p\right).
\tag{31}
$$
用 R73 的原框架方向，第三交叉场协变导数的后两分量是
$$
(\nabla_sV_C)_2=hzA_C+(N_C)_s-hW_C,
$$
$$
(\nabla_sV_C)_3=(e_{\rm g})_sA_C+
e_{\rm g}(A_C)_s-\gamma W_C-h(W_C)_s-N_C.
\tag{32}
$$
因此原 $T_s/(2h^2)$ 的 $ur$ 系数准确为
$$
\frac z2\alpha_n+
\frac{\gamma}{2h^2}
\bigl((e_{\rm g})_s\alpha_n+e_{\rm g}(\alpha_n)_s\bigr).
\tag{33}
$$
原 $B=V_Y\cdot V_C/(2h)$ 的 $ur$ 系数为 $e_{\rm g}\alpha_n/2$。

R405 的完整右锚 $P_n$ 局部项是
$$
-\frac{B_\beta}{8h}-\frac{\tau_nB_\tau}{32h^3},
$$
$$
\begin{aligned}
B_\beta={}&he_{\rm g}\beta_npr-\frac{Q\beta_n}{2}r^2
+\frac{Q\beta_n''-2h^2\beta_n}{2}p^2\\
&-he_{\rm g}\beta_n''up+h^2\beta_n''u^2,\\
B_\tau={}&he_{\rm g}Qpr-\frac{Q^2}{2}r^2
-2h^3e_{\rm g}up+2h^4u^2 .
\end{aligned}
\tag{34}
$$
两式都没有 $ur$ 项；剩下的三 primitive 属于(2)中的 $m_jJ_j$，不能挪到局部 $c$ 中。因此原完整周期
$$
\int\left\{\frac{T_s}{2h^2}
+\left(\frac{K_0}{z}+\left(\frac\gamma{h^2}\right)_s\right)B
+(K_0+\lambda_s)P_n\right\}ds
$$
的 $ur$ 系数，仅需合并(33)和原 $B$ 项。其被积式为
$$
\frac12\left(z+e_{\rm g}\frac{K_0}{z}\right)\alpha_n
+\partial_s\left(\frac{\gamma e_{\rm g}\alpha_n}{2h^2}\right).
\tag{35}
$$
直接用 $hz=e_{\rm g}+k$ 得
$z+e_{\rm g}K_0/z=kQ/h$。故保端项的一般式是
$$
c_V(x,n)=
\int\frac{kQ}{2h}\alpha_n\,ds+
\left[\frac{\gamma e_{\rm g}\alpha_n}{2h^2}\right]_{s_0}^{s_1}.
\tag{36}
$$
在本文固定的实际闭路径上，$M=0,\ T=\tau_{\rm hook}\mathfrak H$ 使不同紧包的二阶、第三交叉场都真正周期；由三个真实右矩基，(27)—(29)对任意 $n$ 线性周期。几何端 jets 同样周期。因此显示端项准确相消，而非把其每个端值置零。得到
$$
\boxed{
c_V(x,n)=
\int_{\rm path}\left[
\frac{kQ}{4h}\beta_n+
\frac{kQ^2}{16h^3}\tau_n
\right]ds .
}
\tag{37}
$$
最后，在积分后或等价地逐线性槽代入 $n=(1,x,x^2)$，
$$
\boxed{
\mathfrak D F_V(x)=
\int_{\rm path}\left[
\frac{kQ}{4h}\beta_{(1,x,x^2)}(s,x)+
\frac{kQ^2}{16h^3}\tau_{(1,x,x^2)}(s)
\right]ds .
}
\tag{38}
$$
固定 $n$ 时 $Q\beta_n,Q^2\tau_n$ 的位置次数至多四；代入三矩抛物线至多再加二，所以(38)确为六次多项式。这一直接次数证明没有假设任何原系数独立。

式(37)—(38)保留全部真实 $s$ history 和连接段，特别保(28)原初值。本文没有证明它恒零、恒正或可独立调节。whole $E/O_{\rm all}=0$ 已用于建立(7)，不能未经新原式身份再次把(38)删掉。

## 7. 与同一个二阶规范、十三行及原 period 的关系

对原允许的任意光滑 $w_\theta$，R408 的完整周期改变量为
$$
\Delta V_\theta=2\tau_{\rm hook}L_f(w_\theta).
$$
原平端与原局部通量身份给
$$
\int_{\ell_i}^{x}f'(\Delta V_\theta)''
=2\tau_{\rm hook}A_f(x)
\{f'w_\theta''-f''w_\theta'\}.
\tag{39}
$$
故在每个实际 $A_f=0$ 点，两个原通量及(21)组合都不变。这包括已经安装的 incoming 清理规范
$w_\theta^c=-\Phi_{\mathsf m_*}D_\theta$；不要求该规范在单包左端为零。

所以若(24)对当前 canonical 目标和所选响应模块不成立，不能用另选一个允许 $w_\theta$ 来改变这批实际点目标。这个说法仍只排该响应模块加原规范的补偿，不排整个 $\mathcal R$、其他母库或新的真实路径机制。

反之，(24)成立只付 ordered-channel 的有符号点条件；并不提供原方程 $L_fk_d=-V_d^c/(2\tau_{\rm hook})$、
$L_fk_e=-V_e^c/(2\tau_{\rm hook})$ 的完整紧解。平台仿射、各点逆 germ、端 gluing、同包通道和其它 period 条件仍要由同一真实目标支付。

即使这两个特解已经存在，R437 的最高规范行仍准确为
$$
P_{2,\theta}(k)=\frac\kappa{24}I_2(Y(f,f),k),
\qquad Y=\Phi_{p_2},
\tag{40}
$$
并在完整 $\ker L_f$ 上为零。故同一十三行系统还要求
$$
I_2(Y(f,f),k_d)=I_2(Y(f,f),k_e)=0.
\tag{41}
$$
(41)保原 incoming 矩阵的真实改变。本文没有从(38)或(24)推出它；七维 current 商和这个固定正交条件属于不同原线性映射，不能按维数互相抵消。

对其余十二行仍须使用 R327 原有限矩阵、同一个相位光滑 kernel 系数、秩降匹配和两个 seed，不能限制允许系数只剩两个谐波。

## 8. 已完成与下一实际入口

本稿完成：

- 将 R434 的七条准确关系合成(9)，并证明同一 144 原模块的完整 current 像恰为其核；
- 给七个含全部 p-only 部分的剩余代表(12)—(16)；
- 给当前所有真实根、宽度、幅度、suffix 的联合补偿充要条件(24)，不新增任何实际点秩；
- 从 R56/R292/R405 原完整 forcing 收出(37)—(38)，保所有 history 与真实端项；
- 说明该有限点商受允许 $w_\theta$ 保护，同时保 R437 独立的同规范正交门。

下一具体问题是原实际背景的(38)与实际求值商
$\mathfrak D(\ker\mathcal E_*)$，以及可能位于本 144 模块外的原响应。它们现在都有明确公式；没有从 formal 32、符号代表或单个坐标失败跳到 actual 全 period 的解或无解。
