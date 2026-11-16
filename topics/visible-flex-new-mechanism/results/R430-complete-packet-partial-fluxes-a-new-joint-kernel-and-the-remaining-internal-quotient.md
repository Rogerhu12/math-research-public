# R430：同包全部退化点的两维旧像、新完整核与真实内部 joint 的剩余商

日期：2026-11-16。**只读已发表原式并作手工证明；没有执行新的 profile、积分、符号程序、数值秩或人工检查。**

[R429](R429-complete-kk-minus4-values-and-actual-common-joint-sections.md) 已支付同一最终母库的 whole $E$ 和实际所需共同自然查询 $A$ 的真实联合截面。该结论支付整包通量，仍未支付每个内部 $A_f$ 零点的累计 partial。

本文先给出一个准确限制：对同一个微包的任意多个退化点，R399 的全部八条新核响应在两通道残差上只有两个共同系数；旧十一维局部轨道对此残差恒零。因此任意三个点给一个明确的线性行列式读出，旧两模块不能改变它。这个结论不是对整个响应空间的否定。

随后从原 $\delta\mathfrak H$ 和 $\chi_{30}$ 构造另一条完整第三核。它的 whole pure、whole self 和全部自然总通量都为零，但其内部 current 在 $A_f=0$ 时有新的 $f'f''$ 因子。它能打破上述三点读出。这是一条真实的新核，既不是点质量模型，也不借未付的全响应秩。

全稿保持同一个最终 profiles、实际位置、幅宽、右锚及 suffix；最后明确实际响应词的完整基准和同一个十三行规范仍如何进入全点问题。

直接来源：[R258](R258-self-adjoint-hook-green-operator-and-complete-period-interface.md)、[R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md)、[R297](R297-ordered-platform-matrix-surjective-pure-zero-responses-and-real-control.md)、[R345](R345-local-whole-E-kernel-orbit-and-eleven-corresponding-degenerate-fluxes.md)、[R389](R389-ordered-total-fluxes-and-complete-flat-end-germs-for-the-rational-port.md)、[R394](R394-conditional-complete-period-and-finite-same-gauge-interface.md)、[R399](R399-new-whole-E-natural-kernel-and-four-ordered-internal-period-controls.md)、[R401](R401-one-packet-mirror-degeneracies-and-four-complete-period-flux-controls.md)、[R408](R408-independent-second-gauge-invariant-fluxes-and-natural-character-extension.md)、[R412](R412-complete-weight-zero-natural-null-mothers-and-nineteen-common-targets.md)、R414、R429。文中若沿用原第三方向 $\mathfrak H$，它始终是完整 $C(P,S)-3C(P,R)$，不是某个简化的首项。

## 1. 需要同时支付的实际有限查询

固定 R412/R414/R429 的同一最终有限母库及其全部真实复制，写
$$
f=\sum_{i=1}^n a_i u_i,\qquad
g=\sum_{i=1}^n b_i u_i,\qquad a_i\ne0,
\qquad
u_i(x)=U_i((x-\xi_i)/w_i),\quad w_i>0.
\tag{1}
$$
所有幅度已放在 $a_i,b_i$；不将真实 $w_i$ 或中心另作自由控制。各支撑闭包不交，包界全平。设
$$
R_i=a_i^2-b_i^2,\qquad T_i=a_ib_i,\qquad
\mu_i=\left(\int u_i''{}^2,\int x u_i''{}^2,
\int\{x^2u_i''{}^2+2u_i'{}^2\}\right).
\tag{2}
$$
每个母的 $p_i=u_i'$ 内部零点简单且有限；其
$$
A_i=6p_i u_i'''-2(u_i'')^2
$$
的内部零点也简单且有限。在 $A_i(x)=0$ 处必有 $p_i(x)\ne0$。记这些实际点为 $x_{i,\alpha}$，总数为 $m$。本文不假设每包只有一对，也不把它们移动成任意插值点。

对一个原完整成本 $V$，采用原两个 period 系数
$$
V_d=V(f^2,g),\qquad
V_e=\frac12\partial_\theta
V(f^2,f\cos\theta+g\sin\theta)\big|_{\theta=0}.
\tag{3}
$$
需要的 raw 查询是
$$
H_{d,i,\alpha}(V)=\int_{\ell_i}^{x_{i,\alpha}}f'V_d'',\qquad
H_{e,i,\alpha}(V)=\int_{\ell_i}^{x_{i,\alpha}}f'V_e'',
\tag{4}
$$
其中 $\ell_i$ 是该包的真实左平端。没有先扣一个平台二次系数。

已有 full $J=(E,A)$ 截面中：

- $E=(\pi,\mathcal Q)$ 是 whole universal pure 与原完整 self 左二次尾；
- $A$ 是实际母的 self 自然查询、所需右矩基的有序 $3+2$ 查询及其共同正仿射闭包；
- $A=0$ 通过 R389/R407 的原分解支付所有整包 $d/e$ totals；
- $E=0$ 支付原平台二阶导数，但不将平台的仿射值重置为零。

在这些条件下，R394 的内部简单 $A_f$ 逆 germ 仍要求全部 $2m$ 个(4)为零。R408 的原式为
$$
\int_{\ell_i}^x f'\{2\tau L_f(w_\theta)\}''
=2\tau A_f(x)\{f'w_\theta''-f''w_\theta'\}.
\tag{5}
$$
因此任何实际允许的同一个全局二阶规范，在 $x=x_{i,\alpha}$ 处都不能改变(4)。式(5)只用原左平端，不要求 $w_\theta$ 在每包的左侧分别紧，也不准在包间重新选常数。

这里的固定使用清单是：同一组 $u_i,a_i,b_i,w_i,\xi_i$、全部实际 $A_i$ 根、原三矩和 suffix、同一个 full $J$，以及原同一右锚。辅助自然输入仅用于读出 totals，不是可以各自修改的 gauge。

## 2. 原 ordered 两通道残差

在包 $i$ 上定义
$$
C_{i,\alpha}(V)=
R_iH_{e,i,\alpha}(V)+T_iH_{d,i,\alpha}(V),
\tag{6}
$$
以及真实 suffix
$$
n_i=\sum_{j>i}(T_iR_j-R_iT_j)\mu_j.
\tag{7}
$$
(7)包含原八/十二副本、五块、所有最后幅权和位置。不能用裸 cell 的均值代替它。

自己的 self 在(6)中消去。R394/R397 的完整函数身份给
$$
C_{i,\alpha}(V)
=a_i^3\,\mathfrak a_{V,u_i}(x_{i,\alpha};n_i),
\tag{8}
$$
其中右边是同锚真实跨包累计 partial。有限 $A=0$ 只使这个表达的整个包积分为零，不使其在任一内部点自动为零，也不使原密度的 universal Euler 多项式为零。

若某个真实 $n_i=0$，式(8)已经使这个包的全部 $C_{i,\alpha}$ 对每个 whole-$E=0$ 成本自动为零；这不只是某个响应模块的盲点。因此实际需要保留的生成清单可减为：每个内部点一个 $D$，以及 $n_i\ne0$ 的包中每个内部点一个 $C$。若后者点数为 $m_*$，至多使用 $m+m_*$ 个生成查询；这仍不是秩声明。

一般 $R_i$ 可能为零；因此全点目标可用
$$
C_i=R_iH_{e,i}+T_iH_{d,i},\qquad
D_i=R_iH_{d,i}-T_iH_{e,i}
\tag{9}
$$
替换。因 $a_i\ne0$，$R_i^2+T_i^2>0$，这个变换可逆。当前 high/low 布局的 $R_i\ne0$ 时，也可沿旧稿使用 $(H_d,C)$。本文的三点读出只涉及 $C$，不会把它误当成两个 period 的全部条件。

## 3. 同一包上旧两模块的准确限制

沿 R399，
$$
\tau_*=64(\chi_{34}-3\chi_{32})-\mathfrak J_0/2,\qquad
\mathcal R_E^*=\mathcal B_E(\tau_*),\quad E\in E_8.
$$
其原局部算子为
$$
D^3K_u^*=D^2(2p^2D^2)-D\{(4r^2+2pt)D\},
\qquad p=u',\ r=u'',\ t=u'''.
\tag{10}
$$
整个右端三个常数由原 $K=-J^3\mathscr A$ 固定。R399 的完整 current 给
$$
C_{i,\alpha}(\mathcal R_E^*)
=4a_i^3 p_i(x_{i,\alpha})^2
\{p_i p_E(n_i)''-r_i p_E(n_i)'\}(x_{i,\alpha}).
\tag{11}
$$
原 $p_E(n)$ 是二次左尾，故对固定包 $i$、固定 $n_i$，
$$
p_E(n_i)'=\alpha_E+\beta_E x,\qquad
p_E(n_i)''=\beta_E .
$$
于是所有八条响应、以及它们的任意真实线性组合，在该包所有点上的值准确属于
$$
\boxed{
C_{i,\alpha}
=4a_i^3p_{i,\alpha}^2
\{-\alpha r_{i,\alpha}
-\beta(x_{i,\alpha}r_{i,\alpha}-p_{i,\alpha})\},
\qquad \alpha,\beta\in\mathbb R .
}
\tag{12}
$$
同一 $\alpha,\beta$ 必须用于这个包的所有点。此式不是把每一点的尾导数分别指定。

若 $n_i\ne0$，原八尾表使一次与二次尾的导数都能独立取得：对非零的 $(n_i)_j$，分别用 $R/U/T$ 和 $L/V/Y$ 的相应两列。常数尾全部保留，但在(11)中消去。因此(12)确为这两条 jet 列的像；若两列在所选点恰相关，实际秩还会降低。若 $n_i=0$，全模块对该包的 $C$ 均为零。

R345 的整个旧局部轨道
$$
\mathscr K=\operatorname{span}\{K_0,\ldots,K_{10}\}
$$
满足
$$
C_{i,\alpha}(K)=0\qquad(K\in\mathscr K)
\tag{13}
$$
于所有包、所有点。这来自完整局部输出在同包的 $a_i^2d_i$ 因子，不限旧选出的十一对应点。

对同包三个不同实际根 $x_1,x_2,x_3$，令
$$
\widehat C_j(V)=\frac{C_j(V)}{4a_i^3p_j^2}.
$$
于是
$$
\boxed{
\mathcal I_{i;123}(V)=
\det\begin{pmatrix}
-r_1&x_1r_1-p_1&\widehat C_1(V)\\
-r_2&x_2r_2-p_2&\widehat C_2(V)\\
-r_3&x_3r_3-p_3&\widehat C_3(V)
\end{pmatrix}
}
\tag{14}
$$
是成本 $V$ 的线性读出，且
$$
\mathcal I_{i;123}
\bigl(\mathscr K+\mathcal B(E_8,\mathbb R\tau_*)\bigr)=0.
\tag{15}
$$
若前两列独立，(14)就是一个非零的三点兼容条件。

原跨副本的 $\mathrm{Pol}_{\le3}$ 插值并不取消(15)：跨副本时 $n$ 的矩随中心输运；本节是在同一个实际包中固定同一个完整 suffix。正幅、平移和正伸缩也不能为同包的不同根另选 $\alpha,\beta$。所以从“至多四个对应 $C$ 点”直接推到一个多退化包的全部点是不成立的。

(15)只限制明确显示的两模块。下一节给出一条原响应内的新方向，说明不能把它扩大为整个 $\mathcal R$ 的障碍。

## 4. 一个新的完整第三核

记原
$$
\mathfrak H=C(P,S)-3C(P,R),\qquad
\mathscr D=x^2D-2x.
$$
$\delta\mathfrak H$ 是对完整三个槽和输出的真实导子；R258 已证明它属于原 $Z_{71}$。只使用这一已付方向，不假设额外八个 $\chi$ 或整个 $\mathcal R$ 在 $\delta$ 下闭合。

定义
$$
\boxed{\tau_\dagger=-\frac18\{\delta\mathfrak H+1024\chi_{30}\}.}
\tag{16}
$$
两项都属于原完整第三对角核 $Z$，故 $\Delta\tau_\dagger=0$。

写
$$
D^3K_u^\tau=\mathscr A_u^\tau
=D^2(a_\tau D^2)+D(b_\tau D)+c_\tau .
$$
原 $\mathfrak H$ 的三个系数为
$$
a_H=A=6pt-2r^2,\qquad b_H=-6(rt)',\qquad c_H=0.
\tag{17}
$$
R258(19)—(21)的完整导子递推给
$$
a_{\delta H}=-6xA+12ut-8pr,\qquad
b_{\delta H}=36x(rt)'+28rt,
$$
$$
c_{\delta H}=-12\{r u^{(5)}+3t u^{(4)}\}.
\tag{18}
$$
这里 $b$ 是自伴形式中的一阶夹心系数；不是原展开式的 $D^2$ 系数。

R261(3.1)有 $\bar a_{30}=256a_{30}$，并给
$$
1024a_{30}=-2xA-12ut-8pr,
$$
$$
1024b_{30}=12x(rt)'+52rt,\qquad
1024c_{30}=12\{r u^{(5)}+3t u^{(4)}\}.
\tag{19}
$$
例如第二式由其原 $\bar d_{30}-\bar a_{30}''$ 得
$\bar b_{30}=13rt+3x(rt)'$；没有只比较最高阶。

逐项相加后得到
$$
\boxed{
a_\dagger=xA+2pr,\qquad
b_\dagger=-6x(rt)'-10rt,\qquad c_\dagger=0.
}
\tag{20}
$$
所以
$$
\boxed{
\mathscr A_u^\dagger
=D^2\{(xA+2pr)D^2\}
-D\{(6x(rt)'+10rt)D\}.
}
\tag{21}
$$
这是完整原算子身份。特别 $(\mathscr A_u^\dagger)^*=\mathscr A_u^\dagger$，
$\mathscr A_u^\dagger u=0$，并非只在 $A=0$ 的点成立。

## 5. 完整同锚 current 与新响应的 whole 核

对任一原 $Z$ 算子，若 $c=0$，且
$$
\mathscr A_u=D^2(aD^2)+D(bD),\qquad \mathscr A_u u=0,
$$
则原右锚唯一性给
$$
K_u=-J^3\mathscr A_u,\qquad
(K_uw)''=(aw'')'+bw'.
\tag{22}
$$
允许 $w$ 有真实左二次尾。右端的局部系数全平，故(22)没有额外常数。

由 $\mathscr A_u u=0$，
$$
\{(ar)'+bp\}'=0.
$$
同一右 collar 给
$$
(ar)'+bp=0.
\tag{23}
$$
因此原部分通量有准确局部原函数
$$
\boxed{
\int_{\ell_u}^x p(K_uw)''
=a(x)\{p(x)w''(x)-r(x)w'(x)\}.
}
\tag{24}
$$
左端为零仅用 $u$ 的真平零 jets，不以 $w$ 左紧作前提。直接微分右边并用(23)即可核(24)。

令
$$
\mathcal R_E^\dagger=\mathcal B_E(\tau_\dagger).
\tag{25}
$$
其 universal pure 由 $\Delta\tau_\dagger=0$ 为零。R297 的原完整 self 式为
$$
\mathfrak q_u(\mathcal B_E\tau)
=-\frac14\int c_{\tau,u}\Phi_E(u,u),
$$
所以(20)给 whole $\mathcal Q=0$。自然总通量亦由同锚自伴交换准确为零：
$$
\begin{aligned}
\Lambda_u(\mathcal R_E^\dagger)
&=2\int u'''K_u^\dagger(\Phi_E(u,u))\\
&=-2\int u\,\mathscr A_u^\dagger\Phi_E(u,u)
=-2\int(\mathscr A_u^\dagger u)\Phi_E(u,u)=0.
\end{aligned}
\tag{26}
$$
三次分部和自伴交换由紧 $u$ 与紧局部系数支付；$\Phi_E(u,u)$ 的左尾从未删掉。于是
$$
\boxed{
\mathcal R_E^\dagger\in
\mathcal R\cap\ker E\cap\ker\Lambda_{\rm all}.
}
\tag{27}
$$
所以它保持 R429 的全部实际共同自然查询，而不只是两个固定读出。

对当前逐整包比例圆，完整 $K_f^\dagger(g)=0$ 仍由局部算子杀 $f_i$ 和原右三常数给出。原响应准确简化为
$$
\mathcal R_E^\dagger(f^2,\phi_\theta)
=2K_f^\dagger(\Phi_E D_\theta).
\tag{28}
$$
这一步同时支付另一条原 history 项，不能只凭不交支撑删去它。

在(6)中本包 self 相消，左包输出真右零，右包只留同一个 $p_E(n_i)$。由(24)、(28)，
$$
\boxed{
C_{i,\alpha}(\mathcal R_E^\dagger)
=2a_i^3 a_\dagger(x_{i,\alpha})
\{p_i p_E(n_i)''-r_i p_E(n_i)'\}(x_{i,\alpha}).
}
\tag{29}
$$
特别在实际 $A_i=0$ 点，
$$
\boxed{
C_{i,\alpha}(\mathcal R_E^\dagger)
=4a_i^3p_i r_i
\{p_i p_E(n_i)''-r_i p_E(n_i)'\}.
}
\tag{30}
$$
与(11)相比，$p_i^2$ 被 $p_ir_i$ 替换。这是原完整 partial 的变化，非某个 principal 的近似。

## 6. 新方向确可打破三点旧读出

固定 $n_i\ne0$，从原八尾取 $E_1,E_2$，使
$$
p_{E_1}(n_i)'=1,\quad p_{E_1}(n_i)''=0,\qquad
p_{E_2}(n_i)'=-x,\quad p_{E_2}(n_i)''=-1 .
\tag{31}
$$
它们的常数尾可以非零，不影响(24)。例如 $(n_i)_0\ne0$ 时用
$E_1=R/(n_i)_0$、$E_2=2L/(n_i)_0$；其它非零矩分量分别用 $U,V$ 或 $T,Y$。

在归一化(14)中，旧两列和一条新列分别为
$$
\mathcal R_{E_1}^*:\ -r_j,\qquad
\mathcal R_{E_2}^*:\ x_jr_j-p_j,\qquad
\mathcal R_{E_1}^\dagger:\ -r_j^2/p_j.
\tag{32}
$$
因此只要
$$
\boxed{
\det\begin{pmatrix}
-r_1&x_1r_1-p_1&-r_1^2/p_1\\
-r_2&x_2r_2-p_2&-r_2^2/p_2\\
-r_3&x_3r_3-p_3&-r_3^2/p_3
\end{pmatrix}\ne0,
}
\tag{33}
$$
这三个实际 $C$ 查询在上述原核方向上满行秩，且新列改变(14)。

(33)不是从三个点的数目推出。其 polynomial 条件并不恒零：取自由 jets
$x_j=j,\ p_j=1,\ r_j=j$，则三行是
$$
(-1,0,-1),\qquad(-2,3,-4),\qquad(-3,8,-9),
$$
行列式恰为 $2$。令 $u'''(x_j)=r_j^2/(3p_j)$ 使 $A=0$，再选第四 jets 使 $A'$ 非零；有限 Hermite 支持可以实现这些局部数据。这只证明条件不是一个 universal 零身份，不声称 R412 已冻结的某三根自动具有这些 jets，也不把这个例子替代同圆所有门的构造。

若某个真实根有 $r_j=0$，新列(30)在该点可能为零；所有公式仍准确。不能因一个泛性例子便忽略这些可能值。

## 7. 实际增强必须保留完整成本基准

(27)的三类原成本在 fixed $J$ 上为零，但它们的**实际 prototype 整词成本**并不因此为零。

必要的有限仿射闭包仍在已付核内。原平移给 $N\tau_\dagger=\mathfrak H$，正伸缩按其真实齐次权作用；$\tau_*$ 及原 $\mathscr K$ 也有既有仿射稳定模块。把 $\mathcal B(E_8,\mathbb R\mathfrak H)$ 一并纳入，便可按 R302/R429 的共同端口和合法窗口先安置一个固定有限响应库，不要求移动实际查询点。没有使用未付的全 $\delta$ 闭合。

设从上述或更大的真实核中选出有限响应 $r_\nu$，某个指定有限查询向量 $F$ 对它们有可逆矩阵 $M$。原 R101 响应词仍有
$$
E_0(t)+n\left(2\sum_\nu v_\nu+Mt\right)
\tag{34}
$$
型完整成本；这里 $v_\nu$ 是真实 prototype 的基准，不是 $r_\nu$ 本身。

消费 R429 的实际 full $J$ 截面时，可先对每个 prototype 加同端口、$M=T=0$ 的真实 $J$ 校正，得到 $\widehat v_\nu$ 且 $J(\widehat v_\nu)=0$。这个清零块自己的 $F$ 成本也进入
$2n\sum F(\widehat v_\nu)$，不能归入与 $n$ 无关的余项。

把该固定 leading 常量通过一个有限 $t_0$ 吸收入 $Mt$，固定参数盒和全部原型重复整数后，再加后置 full-$J$ 校正。响应列本来在 $\ker J$，故后置目标仅依赖同一个有界 $E_0(t)$，不含新的 $n$ 项。其全部 $F$ 成本必须保留为固定盒上的 $O_{C^1}(1)$ 余项。最后才选一个有限大 $n$，由 $M$ 的真实可逆性作一次收缩。Klein 的非零基准按原式先减后除以4。

这证明：**一旦固定的有限查询在真实 $\ker J$ 响应中确有满行秩，就可在原窗口/端口范围内与 whole $J$ 在同一实际路径联合支付。** 此处不是把 signed span 直接等同实际可达；(34)中的所有基准和后置代价都参与精确有限方程。

例如满足(33)的三个 $C$ 查询可使用该原接口。这个实例不同时宣称其余 $H_d$ 或其它根已经为零；新三列的这些值一般非零，并须进入下一真实联合矩阵。

## 8. 全部内部点的下一准确问题

令 $\mathcal P(V)$ 为(4)全部 $2m$ 个原 partial，且
$$
\mathcal R_0=\mathcal R\cap\ker E.
$$
R344/R389 给 $\Lambda_{\rm all}(\mathcal R_0)=0$，故
$\mathcal R_0\subset\ker J$。对固定 $J(V)=0$ 的 signed 成本，能否只加保 $J$ 响应支付所有内部点，准确等价于
$$
\boxed{-\mathcal P(V)\in\mathcal P(\mathcal R_0).}
\tag{35}
$$
等价地，每个湮没 $\mathcal P(\mathcal R_0)$ 的线性读出，都必须湮没当前 $\mathcal P(V)$。本稿没有算这个完整像的秩。

若后继证明
$$
\mathcal P(\ker J)\subseteq\mathcal P(\mathcal R_0),
\tag{36}
$$
则可以在其真实独立像坐标上使用第7节：prototype 和 full-$J$ 清零成本也在 $\ker J$，其全部 partial 基准由(36)落在同一响应像，故同一个有限构造能支付全点；不是忽略像外的 leading 常量。反之，仅证明某些列或某些投影满射，不支付(35)/(36)的其余分量。

现有两模块满足(15)，新完整核(16)在条件(33)下打破它。这已经说明：旧三点行列式不能用作全 $\mathcal R_0$ 的障碍；必须继续使用更大原核或证明一个对整个原核有效的新读出。

即使(35)在实际同一路径上已经支付，R394/R408 的同一个二阶规范仍须处理平台仿射 gluing、两个完整 period particular 和原十三行相位系统。成本变化可能改变 particular 与十三行右端，不能把多个点各自可解拼为不同的 $w_\theta$。本文不改该规范定义、不另设区间积分常数，也不宣布十三行 Smith 兼容已经解决。

最后，R412 的当前母库只保证有限简单退化点，没有 R405 的共同外 cap。若后继从起点证明同 $q$、同完整纤维、同十九根的共同 cap 版本，可再消费 R405/R407 的公共表；不能把另一母函数的 cap 身份移植进当前圆。上述(11)、(24)、(29)及全点准则(35)对是否共同 cap 均不作这种假设。

本稿完成的是同包旧像的真实限制(12)—(15)、新原核(16)—(27)、其完整内部响应(29)—(30)、及打破旧读出的明确条件(33)。全部内部点和同一个十三行规范仍按(35)及原 range 接口继续。
