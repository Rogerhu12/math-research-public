# R520：原变形母库中的真实常态 ruling 与同一规范下的非恒局部离开

日期：2026-11-16。**完整原式纸面构造；没有执行符号程序、求积、profile 扫描、秩计算、开发检查或新的科学任务。**

本稿严格使用 [R459](R459-one-common-signed-witness-for-all-internal-fluxes-of-the-equal-width-library.md) 的母库类型：母形可以在共同严格内区不同，但四个自然约束、完整低阶纤维、共同宽度、真实三矩、共同外 cap 和二十个原目标在同一点保持。它不把 [R512](R512-fixed-compact-second-mother-and-complete-linear-path-gauge-obstruction.md) 的字面同形母库改名后套用。

新增结论是一条真实的正向入口。可以从起点在该类中选一个加强子库，并选一个合法常 scalar 状态，使原完整 history 平方系数准确为零，而二阶 history 本身和它的正能量均不为零。一次固定的第三规范使整个常态区间的第四 ruling 为零。在这条常态路径的一个具有真实非零累计矩阵的内部点，另一条完整速度导数严格非零；由此可用同一个第二、第三规范平滑离开常态区间，产生真正非恒的局部几何路径，完整保留原八矩和第三历史。

这不宣称已经得到返回桥。所得非恒段的末 scalar、frame、位置、总 $M,T,V$ 均是原方程的真实输出。没有将这条新局部规范与此前已锁定的有理保护芽十三行规范自动等同，也没有把 [R518](R518-fixed-width-complete-period-cost-cone-and-actual-finite-C1-sections.md) 的实际成本截面当成点态 ruling 已付。

## 1. 固定原母库与本次新增的两个完整目标

取 R455/R459 的共同物理宽度、严格不交 rank-one 圆
$$
f=\sum_i a_i u_i,\qquad
g=\sum_i b_i u_i,\qquad
\phi_\theta=f\cos\theta+g\sin\theta,
$$
$$
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta,\qquad
R_i=a_i^2-b_i^2,\qquad
\lambda_i=-a_i^2R_i .
\tag{1}
$$
全部实际平移、八副本、十二翻号副本、五个正权 block 和原八宏复制都包含在这个列表中。二次输入槽使用 $\odot$；不能把槽上的导数改成普通乘积求导。

共同右锚为
$$
Jv(x)=\int_x^{r_*}v(t)\,dt,\qquad (Jv)'=-v.
$$
所有真实 profiles 在两个固定 collars 为零。不同微包的原算子输出可以有左多项式尾；下文不删除这些尾。

原目标仍为
$$
\mathbf T_{20}=(\mathcal V_{19},d_f(P)),\qquad
\mathcal V_{19}=0,\quad d_f(P)=\eta_P\ne0.
\tag{2}
$$
四自然约束及原共同纤维是
$$
\mathbf q(u_i)=0,\qquad
F^\star(u_i)=F^\star(u_0),\qquad
F^\star=(\mathcal F_{\rm rat},D,E_5).
\tag{3}
$$
外 cap、两个简单 $A_u$ 根的整个邻域、有限简单 $u'$ 根，以及 R455 的原严格开条件一并保持。

在选母以前另固定一个合法状态
$$
S_c=(h_c,0,\omega_c),\qquad h_c>0,\quad
\omega_c\ne0,\quad x+\omega_c>0\quad(x\in I).
\tag{4}
$$
可直接取一个正 $\omega_c$ 使最后条件成立；它不是原有理保护芽的 $\omega=0$。记
$$
y=x+\omega_c,\qquad e_c=h_cy,\qquad Q_c=1+h_c^2y^2.
$$
以下 $Q_c$ 是几何多项式；完整 history 平方另记为 $\mathscr Q_c$。

令
$$
M_c=M_{\rm raw}(S_c,0,0),\qquad A_c=\Phi_{M_c}.
\tag{5}
$$
真实 physical 配对为
$$
\mathcal E_S(v,w)
=\frac1{4h}\int\{(1+(h(x+\omega)-k)^2)v''w''
                    +2h^2v'w'\}.
\tag{6}
$$
当一槽紧而另一槽有原左尾时，仍按原 physical 配对及其真端项使用该式；涉及两个非紧单包时先保原 Green 项。

本次两个新目标是
$$
\boxed{
\mathscr Q_c(\theta)
=-\mathcal E_{S_c}(A_cD_\theta,A_cD_\theta)
+2\mathcal E_{S_c}\{\phi_\theta,A_c(\phi_\theta,A_cD_\theta)\},
}
\tag{7}
$$
及
$$
\boxed{
\mathscr G_c(\theta)
=\mathcal L_{k,c}(A_cD_\theta).
}
\tag{8}
$$
其中
$$
\mathcal L_{k,c}(q)
=2\mathcal T_{k,c}(q;D_\theta)
 -4\mathcal T_{k,c}(\phi_\theta;\phi_\theta,q),
\tag{9}
$$
$\mathcal T_{k,c}$ 是 R221 原 physical 三线性式对真实速度 $k_s$ 的偏导，先使用 $\omega_s=k_s/(2h)$，再在 $S_c,h_s=k_s=0$ 取值。不是把 $\omega_s$ 当成独立控制。

我们将从起点同时取得
$$
\boxed{
\mathbf T_{20}=(0,\eta_P),\qquad
\mathscr Q_c(\pi/2)=0,\qquad
\mathscr G_c(\pi/2)=1.
}
\tag{10}
$$
数值 $1$ 只固定一个有限非零目标单位；不来自计算。

## 2. 常态矩阵与完整常态三阶密度

R73 的原八坐标在(4)准确给
$$
\boxed{
A_c=-\frac1{8h_c^2}R_y-\frac18T_y,
}
\tag{11}
$$
其中
$$
R_y(u,u)=(u')^2+yJ((u'')^2),
$$
$$
T_y(u,u)=y^2(u')^2+
yJ\{y^2(u'')^2+2(u')^2\}.
\tag{12}
$$
共同 $y=x+\omega_c$ 只是一次真实坐标重写；右锚同时变为 $r_*+\omega_c$，不改变积分常数。

若 $p=u',r=u'',t=u'''$，则
$$
(A_cu^2)''=\alpha_c\,t+\beta_c,\qquad
\boxed{\alpha_c=-\frac{Q_c(p-yr)}{4h_c^2},}
\tag{13}
$$
$\beta_c$ 保含所有原 $C^2$ jets 和右 primitives。直接由
$R_y''=2(p-yr)t$ 及完整
$
T_y''=4ypr-2y^2r^2-2p^2+2y^2(p-yr)t
$
得(13)：前三项属于已经保留的 $\beta_c$，只有最后一项进入 $\alpha_c$。此处的 $C^2$ 余项不能在完整等式中省略。

$M_c$ 非零。事实上在 $y$ 坐标中它只有 $r_1=-1/(8h_c^2)$、$t_1=-1/8$ 两个非零八坐标，故是真 rank-one、平方零矩阵。矩阵平方零不代表二次 profile 算子 $A_c\circ A_c$ 为零。

还需要核完整第三 local 密度，而非只观察矩阵。在常 $S_c$ 上，
$$
V_{Y_u}=\left(-p/2,0,h_cu-e_cp/2\right),\qquad
\nabla_sV_{Y_u}=\left(0,h_c(u-yp/2),0\right).
$$
原 second local 场 $K(v,w)$ 的 $\eta$ 为零，分子只有 $N$ 分量。其 $x$ 导仍只有 $N$ 分量，协变 $s$ 导只有 $T,B$ 分量。因此 forcing $H(Y_u,K(v,w))$ 的
$P,\mathcal B,T_s$ 三个分子配对均为零。R56 原 range 密度随之为零。R73 的变化-profile $\Psi_s$ 在常态也为零。于是完整三线性身份是
$$
\boxed{C_s(u;v,w)=0\quad\text{在常态区间上}.}
\tag{14}
$$
这里没有说第三 local 场本身为零；它的局部恢复仍进入第四常数项。

从真实 $A(0)=T(0)=0$ 开始，在一段常态区间上准确有
$$
A(t)=tA_c,\qquad
T(t)=-\frac{t^2}{2}A_c\circ A_c.
\tag{15}
$$
这是原 R73 累计式的精确积分。没有重锚，也没有用 $W$ 的外矩零代替(14)。

对任意固定全局 $w_\theta,\chi_\theta$，最高时间系数仍是(7)，与入值和规范无关。在 $w_\theta=0$、(15)的真实初值下，整个常态 ruling 更具体为
$$
\boxed{
\mathscr K_c(t,\theta)
=\mathscr R_c(\theta)-2\mathcal E_{S_c}(\phi_\theta,\chi_\theta)
+t^2\mathscr Q_c(\theta).
}
\tag{16}
$$
$\mathscr R_c$ 是在 $t=0$ 的完整 canonical 值，含原 second local 平方、第三 local 恢复及变化-profile chain；本稿不把它设成零。

## 3. 一般全路径的有限纯 self 纤维

要把(10)两个标量真正提升为全部相位，并在非恒段使用同一方程，必须在母库初选时保比原 $\mathcal F_{\rm rat}$ 更多的低阶资料。不能在一个旧冻结圆上免费添加。

先完整加入 [R480](R480-finite-full-third-outer-moments-and-zero-matrix-prototype-ruling.md) 的 $\mathcal F_{\rm all3}$。于是同一个新圆满足
$$
I_j\{\phi_\theta,\tau(\phi_\theta;D_\theta)\}=0,
\quad \tau\in W,\ j=0,1,2,\ \text{全部 }\theta.
\tag{17}
$$
此处只删除该配对中的完整第三 history，不删除第三场或其第四成本。

固定本稿真实初端 $S_c,h_s=k_s=0,A=T=0$。沿 R482 选一次原第三商势 lift，保
$$
P^{\rm end}
=\Pi(S,h_s,k_s)-\Pi(S_c,0,0).
\tag{18}
$$
$\Pi$ 包含速度二次势 $P_{\rm acc}$、$P_h$ 及原 $(k,\omega)$ 势。第二累计 $A=\Phi_m$ 始终是原八矩积分。

在(17)下，R482 的完整式为
$$
\begin{aligned}
\mathscr K^{\rm can}(S,m,\gamma,\upsilon,h_{ss},k_{ss};\theta)
={}&\mathscr R+\mathcal L_S(AD)
-\mathcal E_S(AD,AD)\\
&-4\mathcal E_S\{\phi,P^{\rm end}(\phi;D)\}
+2\mathcal E_S\{\phi,A(\phi,AD)\}.
\end{aligned}
\tag{19}
$$
$w=\chi=0$ 只用于定义这个 canonical 函数族；第8节再加一次固定 $\chi$。$\mathscr R$、$\mathcal L$ 是 R482(18)–(22)的完整原式，包括 $v=M_{\rm raw}D$ 的 chain。

### 3.1 为什么新增 pure self 确为 $C^2$

下面明确保三项抵消。单独 $\mathfrak b(Z,Z)$ 或
$-\mathcal E(AD,AD)$ 都通常含 $t^2=(u''')^2$；它们没有单独纳入低阶纤维。

对一个单包，保原两次恢复的非紧左尾，用 R299/R324 的定义写
$$
K_{\zeta}(u)
=\mathfrak b_\zeta(Z(u^2),Z(u^2))
+4\mathfrak b_\zeta(Y_u,C(u;u^2)).
\tag{20}
$$
$\zeta$ 包括(19)的当前有限状态、速度、加速度和真实初端常量，不是只取有理芽参数。这里 $C$ 是原完整第三恢复，含 $W_C$；不是仅取局部 $K^{(3)}$。

按 R296(16)，把右积分中仅线性含 $t$ 的每项先准确改写为
$$
J(At)=-\mathfrak A-JD_0\mathfrak A,\qquad
\mathfrak A(x,u,p,r,\mathbf J)
=\int_0^r A(x,u,p,\rho,\mathbf J)\,d\rho .
\tag{20a}
$$
其中 $D_0$ 是不含 $t\partial_r$ 的真实 $x$ 全导数部分；每个
$\mathbf J$ 的导数仍按它的原低阶密度取。共同右 collar 的
$\mathfrak A=0$，左端值原样保留。以下 $\partial_r^{\rm loc}$
仅对这份已降阶表示的局部 $r$ 取导，不删除 $\mathbf J$。

对任意 E8 算子 $X$，原六项式给
$$
X(u^2)''=\alpha_Xt+C^2,\quad
\partial_r^{\rm loc}X(u^2)'=\alpha_X,\quad
\partial_r^{\rm loc}X(u,Y(u^2))=\alpha_X\alpha_Y/2.
\tag{20b}
$$
置
$$
\beta=\frac{Q(\gamma p-e_sr)}{8h^3},\qquad
L=\alpha_m/2+\beta .
$$
原 second 分子的最高项是 $(1,0,e)Lt$。必须继续核其配套第三项。令
$$
\mathfrak a=Qr-hep,\quad
\mathfrak c=heu-Qp/2,\quad
n=h(u-zp/2),\quad t_0=\gamma u-e_sp/2 .
$$
R56 原三个 forcing 分子在(20a)后准确满足
$$
(P_C)_r^{\rm loc}=\mathfrak a\beta/(4h),\quad
(B_C)_r^{\rm loc}=\mathfrak c\beta/(2h),\quad
(T_s)_r^{\rm loc}
=nzh\beta+t_0(e\beta_s+e_s\beta).
\tag{20c}
$$
将它们放回原
$T_s/(2h^2)+K_0P-\lambda P_s+(K_0/z)B-\gamma B_s/h^2$，
用 R73 的完整 $M_{\rm raw}$ 系数，得到
$$
\ell_r^{\rm loc}=2\beta\beta_s-\beta\alpha_{M_{\rm raw}}.
$$
变化-profile 链的原 $\Psi$ 同时给
$$
\Psi_r^{\rm loc}=-\beta\alpha_{M_{\rm raw}},\qquad
(C_s)_r^{\rm loc}=(\beta^2)_s.
\tag{20d}
$$
这两个 $\beta\alpha_M$ 项必须一同保留才相消。其推导只用点态原分子、真实水平关系和(20a)，没有使用有理中心的特殊 $s$ 公式。

于是从本稿固定初端 $\beta_0=0,m_0=0$ 沿真实累计积分，
$$
\begin{aligned}
(W_C)_r^{\rm loc}
&=-\frac12\int\alpha_{M_{\rm raw}}\alpha_m\,ds
  +\int(\beta^2)_s\,ds\\
&=-\alpha_m^2/4+\beta^2 .
\end{aligned}
\tag{20e}
$$
这里用了 $m_s=M_{\rm raw}$；没有在后继非零速度点重新归零，也没有省掉初端势。

对实际幅度 $\phi=cu,D=du^2,d=a^2-c^2$，R56 的第三局部恢复另给
$$
(\eta_C)_{\rm prin}
=-cd\,\frac{Q(\gamma p-e_sr)}{8h^2}L\,t .
\tag{20f}
$$
将原 second square、第三 local 和第三 characteristic 三项放回完整 ruling，在同一个因子 $Qt^2/h$ 下，它们依次为
$$
\begin{array}{c|c}
\text{完整来源}&\text{该因子的系数}\\ \hline
-\mathfrak b(Z_D,Z_D)&-d^2L^2\\
\text{原 }Y\text{--third local}&-2c^2d\,\beta L\\
\text{原 }Y\text{--third characteristic}&
c^2d(-\alpha_m^2/4+\beta^2).
\end{array}
\tag{20g}
$$
后三项之和准确为 $-a^2dL^2$，所以整个原 source 的 principal 为
$$
-a_i^2d_i(\theta)\int\frac Qh
\left(\frac{\alpha_m}{2}+\beta\right)^2t^2.
\tag{21}
$$
这项一般非零，仍是一个 $C^3$ 目标；本稿从未把它整项宣成 $C^2$。

现在只在同一个原幅度恒等式内取形式 $a=0,d=-c^2$。
完整左边正是 $-c^4K_\zeta(u)$，而(20g)的总 $t^2$ 系数为零。
这才证明(20)有完整 quartic polynomial/$C^2$ 延拓。它不构造非法实际种子 $f=0$。剩下的一次 $t$ 再按(20a)及其外积分版本准确降阶；所有右原函数、左值和 Green 项保留。右方 inner 在当前包上只有原多项式尾，其分子没有两个三导相乘，故 cross 也只产生同类 $C^2$ 项。

使用(18)的商势 lift 不破坏这条结论。它与真实 $W_C$ 的差属于
$W$；其 pure self 改变量是原
$\mathcal E_S\{u,\tau(u;u^2)\}$ 的固定线性组合。R480(12)–(15)
已对全部 E8 交换子把这一完整配对准确降成 $C^2$，包括两条左尾的
Green 差；剩余十八核在对角上逐函数为零。因此更换 lift 只改变一个
已付 $C^2$ self，不能恢复或偷偷删去(21)。本稿可以用(19)定义有限当前状态的代表，同时保留原实际路径上的全部同值关系。

原左右两包的第二尾是 $\Pi_\mu(x)=xU_\mu+V_\mu$，第三 mixed 输出的系数是对 inner $\nu$ 线性的二次多项式 $\beta_\nu(x)$。R299/R324 的原尾推导给准确 whole 有序核
$$
\Gamma_\zeta(\mu,\nu)
=-2\Pi_\mu(\ell)\cdot U_\nu/h
+\mu\cdot\mathbf a_{\beta_\nu}/h
\tag{22}
$$
及校正 self
$$
\widehat K_\zeta=K_\zeta-\Gamma_\zeta(\mu,\mu)/2.
\tag{23}
$$
$\mu$ 仅含 $C^2$ 真矩，几何及 history 系数不对 profile 增阶，故(23)仍为完整 $C^2$ 观察。(22)保原 first-derivative 部分和两真实左尾；不使用 single-packet 左紧性。其选左零 collar 的依赖在(23)内逐项相消。

本稿低阶表只收(23)和另已完整降阶的加速度 self。全部非纯 source 的(21)仍在高阶目标系统中：旧二十行保持原值，本次只增加第5节明确给出的 $\mathscr Q_c,\mathscr G_c$ 两行，并在第6、7节与旧二十行一起证明主像和有限正根。没有另加一张未经支付的无限 $C^3$ 纤维。

### 3.2 新增观察是一个固定有限表

R56 有限代数、R73 八矩和 R77/R79 有限第三势空间使(19)取值于一个固定有限 profile 算子空间。几何系数是有限 Laurent/log 函数及 $k,\omega,\gamma,\upsilon,h_{ss},k_{ss},m$ 的有限多项式组合；固定初端只添加固定系数。因此 $\widehat K_\zeta$ 的真实函数跨度有限。

共同平移每一个单包后，R505(10)的完整原分子次数证明同样适用：$Y,Z,C$ 的三分量次数上界分别为 $(0,-\infty,1)$、$(4,3,5)$、$(8,7,9)$，包含真实 history 与其 $s$ 导数。两配对次数不超过10。移动单包左 strip 产生的项已在(22)(23)保住。因此
$$
\widehat K_\zeta(u_\xi)
=\sum_{d=0}^{10}\xi^d\,K_{\zeta,d}(u).
\tag{24}
$$
取这些完整函数在 $\zeta$ 中的一个有限真实生成表，再取全部 $0\le d\le10$ 的系数。允许冗余；不声称其数目就是秩。

另明确加入 R482(29)(30)(33)两加速度单包函数
$\mathfrak c_h(u;S),\mathfrak c_k(u;S)$
的全部有限几何系数和平移系数。它们已由该稿证明为 quartic/$C^2$，平移次数分别至多7、6。

把以上所有观察与 $\mathcal F_{\rm all3}$ 合并，记作
$$
\boxed{\mathcal F_{\rm path}.}
\tag{25}
$$
它包含旧 $F^\star$，每个新增分量均为完整、连续 polynomial/$C^2$ 泛函。定义从原完整恢复出发，不以 principal 定义任何一条低阶观察。

## 4. 同一可变母库上，全相位准确缩为一条且加速度全消

从起点保持
$$
\mathcal F_{\rm path}(u_i)
=\mathcal F_{\rm path}(u_0)
\tag{26}
$$
后，(24)在每个实际编码中都是同一个位置多项式。原 R299/R324 四次代数、真实三矩和(22)给
$$
\mathscr K^{\rm can}(\theta)
=\sin^2\theta\,\mathscr K^{\rm can}(\pi/2)
+\sin^2\theta\cos^2\theta\,\Xi,
$$
$$
\Xi=\sum_i(R_i^2-4T_i^2)\widehat K_\zeta(u_i)
+\sum_{r<s}\gamma_{rs}(\zeta)\mathcal A_{rs}.
\tag{27}
$$
这里 $T_i=a_ib_i$，$\mathcal A_{rs}$ 是原三条有序矩面积。

等背景布局有
$$
R_i^2-4T_i^2=(7B_0/2)R_i,\qquad
\sum_iR_i\xi_i^d=\sum_iT_i\xi_i^d=0\quad(d\le10).
$$
于是(26)清掉(27)第一项；原五个严格正 block 清掉三面积。十二完整 copy 的真实四次幅权和第十一差分清掉全部 odd 项。不同完整 base 之间的 cross 因 inner $D_\theta$ 三矩为零而准确消失。所有原宏复制仍按完整 base 进行。

对加速度，R482(42)(43)给
$$
\mathcal C_\alpha(\theta)
=\sum_i c_i(\theta)^2d_i(\theta)\,
\mathfrak c_\alpha(u_i;S),\quad \alpha=h,k,
\tag{28}
$$
其中跨包项准确为零，因为紧 outer 的 $\int F_uF_u'=0$。相同纤维及其真实平移次数，配原等背景矩和十二差分，使(28)整个为零。并非仅选两个相位将加速度消掉。

故在同一个新库、同一个真实初端和全部允许的当前状态上，
$$
\boxed{
\mathscr K^{\rm can}(s,\theta)
=\sin^2\theta\,\mathscr F(h,k,\omega,m,\gamma,\upsilon),
\qquad \mathcal C_h=\mathcal C_k=0.
}
\tag{29}
$$
$\mathscr F$ 仍保全部八矩、初端势及其平方。它不等于 R505 的单纯 second 能量；本稿没有使整个 $Y$–third 配对消失。

特别，取(29)在常态曲线上各时间系数，以及其在内部状态的真实速度导数，得到
$$
\mathscr Q_c(\theta)=\sin^2\theta\,\mathscr Q_c(\pi/2),\qquad
\mathscr G_c(\theta)=\sin^2\theta\,\mathscr G_c(\pi/2).
\tag{30}
$$

## 5. 两个新行的完整三导分裂

第一行是 R296/R315 对任意实际 E8 方向的完整平方身份。由(13)，
$$
\mathscr Q_c(\pi/2)
=\sum_i\lambda_i\int
\underbrace{\frac{Q_c^3(p-yr)^2}{64h_c^5}}_{\mathcal P_Q}
t^2+\mathcal B_Q,
\tag{31}
$$
$\mathcal B_Q$ 是保全部 left/ordered/Green 的 quartic/$C^2$ 余项。

第二行的因子可以直接从原 trilinear 式核出，不依赖(31)猜测。在 $\gamma=\upsilon=0$ 对真实 $k_s$ 求导，$e_s$ 的导数为 $-1/2$。R221(17)准确给
$$
\boxed{
\mathcal T_{k,c}(v;a,b)
=\frac1{64h_c^4}\int
\{Q_c^2v'''a''b''+2h_ce_cF_v a''b''\},
}
\tag{32}
$$
$$
F_v=Q_cv''-2h_ce_cv'+2h_c^2v.
$$
式(32)先用于真正紧的第一槽：在完整 $\mathscr G_c$ 中，第一槽是 $\phi$ 或整个 $A_cD$，后者由真实三矩确实紧。拆成单包时 $q=E(u,u)$ 可以有左二次尾。此时(32)的 physical 推导及 $F_q$ 转置要另保原左边项和 $F_q(\ell)$ 常数；这些只依赖 $q,q'$ 的真左尾、单包三矩及至多二阶数据，属于 $\mathcal B_G$ 的完整 $C^2$ 部分。不能称它们逐项为零。

因此若 $q=E(u,u)$、$q''=\alpha_Et+C^2$，保上述真尾以后，对含 $q'''$ 的积分使用紧 $u''$ 作 IBP，得到
$$
\mathcal T_{k,c}(q;u,u)
\equiv_2-\frac1{32h_c^4}\int Q_c^2r\alpha_Et^2,
$$
$$
\mathcal T_{k,c}(u;u,q)
\equiv_2\frac1{64h_c^4}\int Q_c^2r\alpha_Et^2.
\tag{33}
$$
第一式将 $Q_c^2r^2q'''$ 积分一次，产生
$-2Q_c^2r\alpha_Et^2$；其余项至多线性含 $t$。第二式的平方只来自
$Q_c^2u'''r q''$。这里新做的这一次 IBP 的边项含原紧 $r$ 而为零；它不代替上一段已经保住的 physical 左边项。

在单包上(9)的幅权依次为 $2d_i^2$、$-4c_i^2d_i$。两主项相加为
$$
-a_i^2d_i\frac{Q_c^2r\alpha_E}{16h_c^4}t^2
=\lambda_i\frac{Q_c^2r\alpha_E}{16h_c^4}t^2.
$$
取 $E=A_c$，由(13)得到
$$
\boxed{
\mathscr G_c(\pi/2)
=\sum_i\lambda_i\int
\underbrace{-\frac{Q_c^3r(p-yr)}{64h_c^6}}_{\mathcal P_G}
t^2+\mathcal B_G.
}
\tag{34}
$$
$\mathcal B_G$ 仍是完整 quartic/$C^2$ 余项。跨包部分含 inner 真三矩、outer 至多单三导；原 IBP 降阶后同样在这个余项内。没有把它设零。

## 6. 原二十行加这两行恰有真实二十二维主像

沿 R447 记
$$
W=p-xr,\qquad C=u-xp+x^2r/2.
$$
旧十九行只含 $x,W,C$；第20行为 $2x^4Cr$。真实偶点对的普遍零核准确是
$$
\alpha up+\beta pr,\qquad \alpha,\beta\text{ 为实常数}.
\tag{35}
$$
由于 $y=x+\omega_c$，两个新行在提出各自非零常数后为
$$
Q_c^3(W-\omega_cr)^2,\qquad
Q_c^3r(W-\omega_cr).
\tag{36}
$$

假定某个新组合可由旧二十行及(35)表示。作真实可逆 jet 代换
$$
p=W+xr,\qquad u=C+xW+x^2r/2.
$$
比较 $Cr$，(36)没有该项；旧第20行及(35)给
$2c_{20}x^4=\alpha x$，故 $c_{20}=\alpha=0$。再比较 $rW,r^2$，若两个新系数为 $a,b$，必须有
$$
(-2\omega_ca+b)Q_c^3=\beta,\qquad
(\omega_c^2a-\omega_cb)Q_c^3=\beta x.
\tag{37}
$$
$Q_c^3$ 为六次且首项 $h_c^6\ne0$。第一式迫
$b=2\omega_ca,\beta=0$；第二式随即迫
$-\omega_c^2a=0$。由(4)的 $\omega_c\ne0$，得 $a=b=0$。旧十九行再由 R324 独立性全零。

因此原22行在真实偶配对、任意原允许内窗和自由二阶 jets 的开集中仍独立。这里只用完整多项式恒等的开集延拓，没有把偶母中心的 $p$ 当成自由量。两新行的物理位置次数分别至多8、7，仍在原次数10的统一范围内。

## 7. 同一个四约束图册、低阶纤维和有限正根

这一节是存在性支付，不能只停在形式 principal 独立。

先固定实际宽度、全部布局、正四次 copy 权、$S_c$ 和共同合法窗口。在 R455 的同一共同-cap、四约束图册内，取
$\mathcal F_{\rm path}$ 的**限制最大秩**，并选有限个严格内支撑见证；没有预填其秩。第6节的22个 principal 见证仍只需要有限二阶 jets 的自由性和原避开主窗的四个正常纠正方向。

将四正常 minor、新 $F$ 的最大 minor 和22个 principal minor 放在同一个有限解析参数族。非零 minor 的有限乘积不恒零，所以可在原允许小邻域同时非零，再冻结这个新 $F$ 的值。这正是 R455、R447、R480 已付的同点选择顺序；不改变旧冻结母以后再追加等式。

每一主形状使用原十二个真实交替位置。其 $\lambda_i=-a_i^2R_i$ 交替，十二点 Vandermonde 的核亦交替；除去真实 $\lambda_i$ 后得到严格正平方幅核。因各行位置次数至多10，各形状的十二列张成其全部位置系数像。有限多个形状联合第6节的22维像，故联合正锥是 $\mathbb R^{22}$。

在同一个原有号三阶集中中加入新两行，完整映射仍有
$$
\mathbf T_{22,N}(\mathbf z)
=\mathbf b+\sum_i z_i^2\mathbf v_i+o_{C^1}(1).
\tag{38}
$$
$\mathbf b$ 包含全部原20值、两新值的 $C^2$ 余项、原 current/Green、跨包尾和所有实际 macro 基准。没有任何基准因“正锥”而被预先清零。

新增 $\mathcal F_{\rm path}$ 仅为有限 $C^2$ 观察，原四正常加限制最大 minor 的块三角 IFT 因而仍给 $C^2$ 小的完整有限纠正。它保持
$$
\mathbf q=0,\qquad
\mathcal F_{\rm path}(u_i)=\mathcal F_{\rm path}(u_0)
$$
以及原内区 $A<0$、外区全 germ、有限简单 $p$ 根、共同 $D-E_5>0$ 和已纳入的 $M_3\ne0$ 开条件。

正锥允许先在严格正幅盒内匹配(10)的完整有限目标；取22个独立列，其平方幅导数非退化。随后选择一个充分大但有限的集中参数，(38)给**真实有限根**。所有最后 copy 和五块使用同一个有限阈值。原共同宽度及同 $\mu$ 内区连通路径不变，所以 R459/R518 的母库接口继续适用其准确范围。

得到同一个圆上
$$
\boxed{
\mathbf q=0,\quad \mathcal F_{\rm path}\text{ 共同},\quad
\mathbf T_{20}=(0,\eta_P),\quad
\mathscr Q_c(\theta)=0,\quad
\mathscr G_c(\theta)=\sin^2\theta .
}
\tag{39}
$$
这不是一次数值搜索，也不宣称任意旧圆已满足(39)。

## 8. 同一固定第三规范支付整个真实常态区间

由(16)(29)(39)，存在完整实数
$r_c=\mathscr R_c(\pi/2)$，使常态 source 为
$$
\mathscr K_c(t,\theta)
=\sin^2\theta\,r_c-2\mathcal E_{S_c}(\phi_\theta,\chi_\theta).
$$
取一个固定 $\nu\in\mathbb R^3$ 满足
$$
2\mathbf w(S_c)\cdot\nu=r_c,\qquad
\mathbf w(S)=
\left(\frac{1+(h\omega-k)^2}{4h},
\frac{h\omega-k}{2},\frac h4\right).
\tag{40}
$$
$\mathbf w(S_c)\ne0$，故此有限线性选择总能完成。

用 R47/R56 原正定三矩 Gram 右逆选择**一次**相位光滑、周期、双 collar 紧的 $\chi_\theta$，使
$$
\mathbf I(\phi_\theta,\chi_\theta)=\sin^2\theta\,\nu,\qquad
\chi_0=\chi_\pi=0.
\tag{41}
$$
整个段上固定 $w_\theta=0$ 和这同一个 $\chi_\theta$，于是
$$
\boxed{\mathscr K_c(t,\theta)=0
\quad\text{对任意有限常态区间及全部相位}.}
\tag{42}
$$
完整第二、第三历史仍准确是(15)。

这确实超出 R512 的负能量障碍范围。在原最右一个非零 $R_i$ 包左边的真实空隙，
$$
A_cD_{\pi/2}
=-\frac{R_i\,y}{8h_c^2}
\int\{Q_c(u_i'')^2+2h_c^2(u_i')^2\}\ne0 .
\tag{43}
$$
右侧积分严格正，$y>0$，$R_i\ne0$。整个 $D_{\pi/2}$ 三矩为零，所以 $A_cD_{\pi/2}$ 双 collar 紧；(6)的正定性给
$$
\mathcal E_{S_c}(A_cD_{\pi/2},A_cD_{\pi/2})>0.
$$
由(39)，这个正能量准确由(7)的第二项抵消。故这里完整 $Y$–third 配对不能删除。矩阵非零、second 场非零、第三 history 非零与完整 ruling 零在同一个实际圆上同时成立。

(42)否定的是“R459 这种可变母类的每一个常态 bulk 都必有不可清平方项”这一普遍断言。它不对某个旧冻结圆给新的值，也不改变 R512 字面同形库的已付障碍。

## 9. 在同一常态历史内部，另一条完整速度导数严格非零

取一个固定 $t_0>0$，例如 $t_0=1$。在已付常态段内部，真实状态为
$$
S=S_c,\qquad m=t_0M_c,\qquad
\gamma=\upsilon=0,\qquad
T=-t_0^2A_c^2/2.
\tag{44}
$$
这不是任意指定八矩入值；由前面实际长度 $t_0$ 的常态段产生。

将固定(41)加入(29)，记全部相位的标量余式为
$$
F(S,m,\gamma,\upsilon)
=\mathscr F(S,m,\gamma,\upsilon)
 -2\mathbf w(S)\cdot\nu .
\tag{45}
$$
它在(44)为零。

核其真实 $k_s$ 导数时，必须保(19)。下面逐分量确认没有漏掉另一个速度一次项。固定当前 $S$，将框架分为 $TB$ 平面与 $N$ 轴：

- $Y$ 及 $Y_x$ 只有零次 $TB$ 分量；$\nabla_sY$ 的 $N$ 分量是零次、$TB$ 分量是速度一次。
- 第二 local $K$ 的 $N$ 分量是速度零次，$TB$ 分量是速度一次。因此 $|V_K'|^2$ 只有零次和二次。
- $\nabla_sK$ 的 $TB$ 分量只有零次、速度二次和加速度一次；其 $N$ 分量只有速度一次。因而 forcing $H(Y,K)$ 的对称 $T_{sx}$ 只有零次、速度二次和加速度一次。
- 该 forcing 的 $P_C,B_C$ 只有速度一次。R56 的 $\eta_C=-T_{sx}/(2h)+e_s(P_C)_x/(2h)+\gamma(B_C)_x/(2h)-(P_C)_s/2$ 中，后面三项亦只有速度二次和加速度一次。

这给 $\eta_-$、从而 R482 的完整 $\mathscr R$ 在零速度处没有一次项。chain 的 $v=M_{\rm raw}D$ 也没有一次项：R73 的所有速度项是 $\gamma^2,\gamma e_s,e_s^2$。$\Pi$ 的速度部分 $P_{\rm acc}$ 是二次，$P_h+\bar F$ 只依赖当前 scalar 状态；物理 $\mathcal E_S$ 和固定 $\nu$ 均不依赖速度。这里先保加速度项，随后才使用已付(28)将其完整系数置零，未把真实加速度预先设成零。

所以在固定当前 $S,m$ 的零速度偏导中，唯一一次项来自
$\mathcal L_S(AD)$。因(44)的 $A=t_0A_c$，
$$
\boxed{
\left.\partial_\upsilon F\right|_{(44)}
=t_0\,\mathscr G_c(\pi/2)=t_0\ne0 .
}
\tag{46}
$$
这里已经先将 $\omega_s=\upsilon/(2h)$ 代入；不是冻结真实 $\omega_s$ 后求一个不允许的偏导。

也没有把第三 history 当成独立可调量。它仍是(18)(19)代表的完整真实 class；$W$ 配对仅由同一个(17)准确消去。

## 10. 真正从常态 germ 平滑离开的非恒路径

由(46)，在(44)的一个固定状态邻域内，普通有限维 IFT 给光滑函数
$$
\upsilon=G(h,k,\omega,m,\gamma)
\tag{47}
$$
使 $F=0$。其分支通过原常态曲线，故在 $t$ 近 $t_0$ 时
$$
G(S_c,tM_c,0)=0.
\tag{48}
$$
所有 profile 积分在此已经是固定实系数；没有沿路径重新选母、规范或一个未知无限维逆。

现在把 $\gamma(s)$ 取为一个足够小、在 $s=t_0$ 右侧开始且于该点全平的非零光滑 bump。它是原真实高度速度控制。解
$$
\boxed{
\begin{aligned}
h_s&=\gamma(s),\\
k_s&=G(h,k,\omega,m,\gamma(s)),\\
\omega_s&=\frac{G(h,k,\omega,m,\gamma(s))}{2h},\\
m_s&=M_{\rm raw}\bigl(h,k,\omega,\gamma(s),
G(h,k,\omega,m,\gamma(s))\bigr).
\end{aligned}}
\tag{49}
$$
初值取(44)。原 frame 与位置再按
$F_s=F\Omega(k)$、$\alpha_s=h^2T$ 同步恢复。

这是光滑的有限维 ODE。选固定足够短区间和小控制盒，统一保持
$h>0,x+\omega>0$ 及(47)的同一分支。由(48)和 ODE 唯一性，控制开始以前的解正是原常态路径；控制在接点全平，故全部状态及几何 jets 与常态段平滑匹配。非零 $\gamma$ 使 $h$ 确实非恒，得到真正离开常态 germ 的路径。没有必要、也未在这里声称 $k$ 一定非恒。

沿整个拼接区间，(47)(49)给 $F=0$，因而
$$
\boxed{\mathscr K(s,\theta)=0
\quad\text{在同一个真实非恒局部区间、全部相位上成立}.}
\tag{50}
$$
两加速度是这条 ODE 的真实导数；(28)已使它们的完整 coefficient 为零，不将它们作为额外自由控制。

原八复制给二、三阶逐点 ruling 与左 collar 条件，(17)保完整第三外矩，固定(41)不改变 profile collars。于是按 R56 同一右锚恢复，可以在这个局部区间使用真正的二、三、四阶场；此处不施加 $s$ 周期，因而不把未付 period 伪称自动成立。

## 11. 这支付了哪一段桥，仍缺什么

本文给的是同一个加强 R459 母库、同一个 $w=0$ 和同一个固定 $\chi$ 下：

1. 一个正长度、非零真实 $M$ 漂移的常态区间，完整第四 ruling 为零；
2. 从该区间的真实前缀内部平滑离开的非恒局部路径；
3. 明确的正则输入：自由 $h_s$，而 $k_s$ 由原完整 scalar 方程决定。

它不是任意指定两端的返回桥。为替换 R70/R101/R518 中的某个实际控制段，至少仍须同时支付：

- 新段入口确为(44)这类已实现前缀，或另付相应非零 derivative；不改写 $m,T$ 入值；
- 同一全局 $w,\chi$ 的原两 period、十三行与其他保护芽；本稿(40)不是对已锁定 Gram 的免费重选；
- 新段末 scalar/frame/位置及完整 $M,T,V$ 的实际传递目标；
- 若串联多个局部反馈段，全部使用同一个合法物理窗口、右锚、冻结母和规范。

这些是具体的端点控制问题，不能再用 R518 的末成本全射代替。反过来，本稿也没有把一个未付的常态平方号作为普遍实际障碍：在这里(43)与(42)已经给出同类可变母源上的准确反例。

R517 的“周期标量自动矩阵返回”使用字面同形库中整个 $Y$–third 配对消失。本稿的(43)说明那条前提在当前库恰不成立。因此不从(50)猜测闭反馈轨道自动 $M=0$，也不把 $M_c^2=0$ 混同为二次 profile history 的平方零。

本稿完成的正向步骤是：在原四约束、共同 cap 和二十目标机制内部，以两条新的完整目标和一个明确有限低阶纤维，得到一个可实际走出的 all-phase ruling 局部路径。全闭词及主 README 的固定度量、完整连续等距族、嵌入、reach 和幅度条件仍未完成。


### 本稿原式与窄核范围

- R56/R73：全部分子、真实水平关系、八矩和第三变化-profile 链；
- R296/R299/R324：完整三导三项抵消、pure self 的准确 $C^2$ 延拓、两个真尾及有序角向核；
- R77/R79/R480/R482：有限第三势、完整 $W$ 外矩和全部 history 的当前状态代表；
- R455/R447/R480：共同 cap、四正常、限制最大低阶 minor、真实正幅根的同点初选；
- R221：两条新 trilinear 主项，紧第一槽和单包真左尾分别保留；
- R47/R56：同一个紧第三 Gram；普通有限维 IFT/ODE 给真实局部路径。

tail_cost 仅独立核了(33)之后
$2d^2(-1/32)-4c^2d(1/64)=-a^2d/16$
的末项因子，没有将该窄核扩大为新的 IBP、低阶纤维或整稿证明。全部新证明仍以本文显示的完整原式和范围为准。
