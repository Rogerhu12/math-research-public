# R773 — 原共同外域的帽平面返回、六支 carry 与五条件矩

日期：2026-11-15。**状态：已证明。**

本文不更换 R734 的最终测试 $q_N^*$。在 R764 的三个外部域已经真正合并的范围 $m\ge n\ge N$，将其共同域的全部五个型五坐标写成明确的原正矩。返回保原六支、整个 E 次数逆、所有参数与单位补项。

有两个需要先说明的范围。第一，原物理 $E_\perp$ 在共同帽深 N 域中自动深 N，故该域上的原 $E_\perp$ 浅 N 支确为空；归一后的 $E_\perp/\kappa^N$ 单位环带仍在。第二，本文不把 R737 的 cd 返回权 $\Phi_N$ 换成 q，也不删除该返回坐标中的 E-unit 条件。

为实际读取一个固定深度差的条件来源，本文另付原失败轴的完整第300层核。取真实 $n=N+300$ 后，五条件矩成为两个完整、无切集的正矩之差，总次数不超过60。它们使用同一个 q，并保全部第二项；其实际算术幅度及条件负一非零由文末公开执行增补支付。

## 1. 同一来源与共同外域

沿 R764、R767，记
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad u=\kappa^N,\quad N\in4\mathbf Z_{>0}.
\tag{1}
$$
全部旧射线、整逆与 $p>163$ 保持不变。来源为
$$
e_0=-\nu_\sigma^{\boxtimes6}/84,\qquad
h_W=\omega^2\mathcal T_*e_0,\qquad q=q_N^*.
$$
物理输入次序是 $(\xi_1,\xi_2,\xi_3,x,c,d)$。保原行
$$
\begin{aligned}
A&=\delta\xi_1+2\delta\xi_2+(3+\omega)\xi_3+(2-\omega)x,\\
Y&=A+c+2d,\\
C&=(\xi_1-\xi_3+x)/\delta,\qquad
B=-\xi_1+\omega\xi_3-\omega^2x,\qquad H_1=B+2\xi_2,\\
\mathfrak r&=(\xi_1-\omega^2\xi_3+\omega x)/\delta,\qquad
s=\mathfrak r+c,\quad t=\mathfrak r-c,\\
A_0&=A-\mathfrak r=2\delta\xi_2-\frac{4\delta}{3}B,\\
F&=s-B+\omega^2\xi_2+(2+3\omega)d,\qquad
G=13H_1+gF,\quad g=3-2\omega.
\end{aligned}
\tag{2}
$$
于是 $Y=A_0+s+2d$，而 q、Y 都不含 t。
本篇的 t 是 R764 的物理轴，不是另一个形式参数。

置
$$
\hat s=s-Y/17,\qquad \hat d=d-Y/17,\qquad
U=\hat s/2-3\hat d,\qquad Z_0=(1+3\omega)\hat s+2\hat d,
$$
$$
b_Y=(20+3\omega)/17,\qquad P=b_YY+Z_0.
\tag{3}
$$
$\hat s,\hat d,U,Z_0$ 全在 $Y^\perp$，并垂直于 t、C、$H_1$。
R764 的真实共同域恰为
$$
\boxed{\mathcal D^\infty_{n,N}
=\{Y\ {\rm unit},\ \hat s,\hat d\in p^N,\ U\notin p^n\}.}
\tag{4}
$$
它只在 $m\ge n$ 的整个 t 深域返回中取代三个外部域。
精确 t 环带的 unit 条件和 $m<n$ 的浅独占域仍按 R764 原式保留。

使用行内积 $\langle L,M\rangle=L\bar M^t$。
对实际非零行 L，始终记
$$
P_{L,z}=I+\frac{z-1}{N(L)}\bar L^tL .
\tag{5}
$$
它保所有正交伙伴，且 $L\circ P_{L,z}=zL$。

## 2. 原 E 浅支在共同深域上的准确范围

原物理行是
$$
E=(5+6\omega)A-29c-(58+87\omega)d
=E_\perp+(17+3\omega)t.
$$
将 R764 的式(25) 代入 (3)，得到整个六变量恒等式
$$
\boxed{E_\perp=-(17+3\omega)\hat s-(68+99\omega)\hat d.}
\tag{6}
$$
故在 (4) 中
$$
E_\perp\in p^N.
\tag{7}
$$
特别，(4) 再附原物理 $E_\perp\notin p^N$ 是空域。
在 R764 的 $m\ge n\ge N$ 返回中，
$$
E_j\longmapsto E_\perp+(17+3\omega)\omega^{2j}\kappa^m t
$$
也自动深 N；这是真实整数线性关系的结果。

(7) 不删除归一后的环带。下一节的帽平面返回把
$E_\perp$ 变成 $uE_\perp$，所以原
$v_p(E_\perp)=N+r$ 准确返回为 $v_p(E_\perp)=r$。
原物理浅 N 为空，与归一后的 E-unit 非空完全相容。
尤其 R737 对指定 cd 域先返回得到的 $\Phi_N$ 和 E-unit 门
不在 (7) 的同一坐标中，本文没有对它们作删项。

当 $m<N$ 时，原固定 E 和各 $E_j$ 还含各自的 t 项；
三个浅独占 CD 支、$N\le m<n$ 的不同失败支全部继续使用
R764(26)、(31)，不由 (7) 改写。

## 3. 保 Y、t、C、H1 的帽平面完整核

三个正交物理轴 $A_0,s,d$ 的范数为 $28,2,1$。为支付第一轴的完整半特征，写
$$
J'=\frac{\delta A_0}{2}=2B-3\xi_2,\qquad H_1=B+2\xi_2.
$$
其 Gram 为 $\operatorname{diag}(21,7)$，在 $(B,\xi_2)$ 上的变基行列式为7。
$J'$ 的三个 B 系数均为偶，$\xi_2$ 系数为奇；$H_1$ 的三个 B 系数为奇，
$\xi_2$ 系数为偶。因此分别是标准 odd degree21、odd degree7。
当前 $g_\pi=\pi_0/\bar\pi_0$ 在模42、14为1。
非零真实锚 $\sigma(\delta\gamma_7z)$、$\sigma(\gamma_7z)$
由原 sigma 核定标两个 whole 核均为 $\beta$。
$A_0=2J'/\delta$ 是固定 p-unit 拉回，故也有同一完整核。
s、d 的 whole 核已由 R764 给出，亦为 $\beta$。

这些轴与 t、C、$H_1$ 正交，保持全部伙伴。
$\mathcal T$ 固定 $A_0,s,d,H_1$，只在 t、C 上乘 $\omega^2$，
所以以上整个核也适用于 $h_W$。
纯 C 的六角平均 $\mathscr P_C$ 与这些核相容。

令 $\Pi_L=\bar L^tL/N(L)$，并定义真正的帽平面缩放
$$
P_{\widehat H,z}
=I+(z-1)(\Pi_{A_0}+\Pi_s+\Pi_d-\Pi_Y).
\tag{8}
$$
$(A_0,s,d)\mapsto(Y,\hat s,\hat d)$ 的行列式为1，且
$$
\operatorname{Gram}(\hat s,\hat d)
=\frac1{17}\begin{pmatrix}32&-2\\-2&15\end{pmatrix}.
$$
(8) 固定 Y、t、C、$H_1$，并同时把 $\hat s,\hat d$ 乘 z。
因而
$$
\{Y,\hat s,\hat d\in p\}=\{A_0,s,d\in p\}.
$$
对 $\mu=e_0,h_W$，完整三轴核给
$$
\mu|_{Y,\hat s,\hat d\in p}
=\beta^3(P_{Y,\kappa}P_{\widehat H,\kappa})_*\mu.
$$
另一方面，R764 的 whole Y 身份是
$\mu|_{Y\in p}=\lambda(P_{Y,-\kappa})_*\mu$；
该映射固定两条帽行。因此限制帽深后，用可逆线性推前的单射性约消，
得到
$$
\boxed{\mu|_{\hat s,\hat d\in p}
=-\lambda^2(P_{\widehat H,\kappa}R_Y)_*\mu.}
\tag{9}
$$
这里使用整个联合身份，未由 Y 边际推断帽核。
$R_Y$ 固定帽行，故迭代为
$$
\mu|_{\hat s,\hat d\in p^N}
=(-\lambda^2)^N(P_{\widehat H,u}R_Y^N)_*\mu.
$$
在原 $N\in4\mathbf Z$ 上，准确简化成
$$
\boxed{\mu|_{\hat s,\hat d\in p^N}
=\lambda^{2N}(P_{\widehat H,u})_*\mu.}
\tag{10}
$$
q 没有被假定固定帽平面；它的完整变化在下一节支付。

## 4. 原六支在帽返回下的逐项变化

令
$$
f=-\bar g/7=-(5+2\omega)/7,\qquad F_0=fH_1,\qquad J=F-F_0 .
$$
直接投影给
$$
\boxed{
J=\frac{17+3\omega}{14}\hat s
   +\frac{17+24\omega}{7}\hat d,\qquad N(J)=72/7,
}
\tag{11}
$$
而 $N(F_0)=19/7$。所以 (8) 使
$$
F\mapsto fH_1+uJ,\qquad
G\mapsto\frac{72}{7}H_1+guJ,\qquad
P\mapsto b_YY+uZ_0,\qquad U\mapsto uU.
\tag{12}
$$

为不隐藏混次规范，将原 q 唯一写成其实际齐次块的和。
$d\in\{6,12,18,24,30\}$，允许某块为零；每个 $P_{d,N}$ 都保
R734 在真实 $(\lambda,\kappa,u,\eta)$ 上的完整系数。
定义
$$
\widehat P_{d,N}
=\sum_{a+e+g'=d}
 \frac{[D^aE_c^eG^{g'}]P_{d,N}}{1+\lambda\kappa^e}
 D^aE_c^eG^{g'}.
\tag{13}
$$
原六支正是
$$
q=\sum_d\frac1{6b^{d/6}\Omega^d}
 \sum_{\zeta\in\mu_6}
 1_{\{F-\zeta C\in p^N,\ F+13\zeta C\ {\rm unit}\}}
 \widehat P_{d,N}((F-\zeta C)/u,F+13\zeta C,G).
\tag{14}
$$
(13) 是原整个 E 次数逆，不能仅在某个新坐标的 E 次数上重作它。

令
$$
L_\zeta=fH_1-\zeta C,\qquad
M_\zeta=7\bar f C+\bar\zeta H_1 .
\tag{15}
$$
两行正交，范数分别为 $26/7,26$，在 $(C,H_1)$ 上的行列式为 $-26/7$。
经 (12)，(14) 的深门准确冻结为 $L_\zeta\in p^N$；
因为 $uJ\in p^N$，没有近似误差。
在该门上，unit 条件仍准确等价于 C-unit。

### 4.1 两条完整 even 核与半特征

清分母后的实际行 $7\delta L_\zeta$、$\delta M_\zeta$
的度数是546、78。在模2下，第一行的非零候选系数是
$$
(1+\zeta,\ \omega+\zeta,\ \omega^2+\zeta),
$$
第二行的是
$$
(1+\bar\zeta,\ 1+\bar\zeta\omega,\ 1+\bar\zeta\omega^2).
$$
每组恰一个为零、另两个非零，其余原输入系数为偶。
所以两个轴对每个 $\zeta$ 都是原标准 even 半特征。
全部正交伙伴仍保留，没有 partner-dependent flat twist。

现射线给
$$
g_\pi\equiv1+546\pmod{1092},\qquad
g_\pi\equiv1+78\pmod{156}.
$$
这由原模4的 $g_\pi=3$ 和模3、7、13的 $g_\pi=1$ 合成。
两 whole Heisenberg 交织均为 scalar；
真实锚 $\Theta(\delta\gamma_7\gamma_{13}z)$、
$\Theta(\delta\gamma_{13}z)$ 继承原 $\Theta$ 的核心 $\beta$。
故两条实际轴的绝对 whole 核都准确为 $\beta$，
而非未定符号。这也对 $\mathscr P_Ce_0,\mathscr P_Ch_W$ 成立：
C 的六角旋转只置换 (15) 中的 $\zeta$，所有轴均有刚付的同一 whole 核。

### 4.2 完整 L 返回与 M-unit 第二项

在本节固定 $\zeta$。写
$$
C_\perp=C+\frac{7\bar\zeta}{26}L_\zeta
       =\frac{7f}{26}M_\zeta,\qquad
H_\perp=H_1+\frac{7g}{26}L_\zeta
       =\frac{7\zeta}{26}M_\zeta,
$$
$$
K_\zeta=J-\frac{36}{13}L_\zeta,\qquad
E_{0,\zeta}=14\zeta C_\perp,\qquad
G_{0,\zeta}=\frac{72}{7}H_\perp .
\tag{16}
$$
返回 $L_\zeta\in p^N$ 后，(14) 的三个参数完整变为
$$
\boxed{D'=L_\zeta+J,\qquad
 E_c=E_{0,\zeta}+uK_\zeta,\qquad
 G=G_{0,\zeta}+guK_\zeta.}
\tag{17}
$$
例如 E 参数中 L 的系数是
$19/26-91/26=-36/13$，故这里保有两部分，未只返回 F。

C-unit 准确返回 $C_\perp$-unit，即 $M_\zeta$-unit。
M 核固定 Y、t、帽平面、$L_\zeta$ 和 J，只缩放
$E_{0,\zeta},G_{0,\zeta}$。所以 unit depletion 的整个多项式权为
$$
\boxed{
\begin{aligned}
\mathcal Q_{d,\zeta,N}(u)
={}&\widehat P_{d,N}(L_\zeta+J,E_{0,\zeta}+uK_\zeta,
                                      G_{0,\zeta}+guK_\zeta)\\
&-\beta\,\widehat P_{d,N}(L_\zeta+J,\kappa E_{0,\zeta}+uK_\zeta,
                                      \kappa G_{0,\zeta}+guK_\zeta).
\end{aligned}}
\tag{18}
$$
第二项系数是 $-\beta=+\lambda$，不是原 C 分支中的 $\eta$。
$\eta$ 仍在原 $P_{d,N}$ 的真实系数内。
M 同时缩放两个参数，故 (18) 不能与 (13) 的原 E 次数逆免费抵消。

定义
$$
\widetilde\Phi_N(u)
=\sum_d\frac1{6b^{d/6}\Omega^d}
      \sum_{\zeta\in\mu_6}\mathcal Q_{d,\zeta,N}(u).
\tag{19}
$$
在 $\mathscr P_C$ 平均来源上，对不含 C 的其余测试，
六项积分相同，可以固定 $\zeta=1$ 并取消 $1/6$。
此时必须仍用 $\mathscr P_C$ 来源，不能把一个单支与未平均来源相认。

## 5. 原共同首行的完整五变量返回

R767 给出的真实五伙伴来源为
$$
\mathcal M_5=\frac1{84}\,
 \nu_{B_3}(C_0)\boxtimes\nu_\sigma(\xi_2)\boxtimes\nu_\sigma(d)
 \boxtimes\{2\nu_{f_3}(S)\boxtimes\nu_{B_3}(B)
                     +\nu_H(S)\boxtimes\nu_{P_3}(B)\},
\tag{20}
$$
其中 $S=\delta s,C_0=\delta C$，
$$
B_3=-y_b\sigma_b^3,\quad P_3=\sigma_b^3,\quad
f_3=-y_b\sigma_b^6,\quad H=(x_b^3-2b)\sigma_b^6.
$$
它准确等于 $\Omega^{-1}\pi_*(t\,\mathscr P_Ce_0)$，保全部五个伙伴；
$h_W$ 的对应来源是 $\omega\mathcal M_5$。

置 $\ell=n-N\ge0$。对任意完整有界测试
$f=f(Y,\hat s,\hat d)$，(10)、(17)、(18) 给
$$
\boxed{
\begin{aligned}
&\Omega^{-1}\int_{\substack{\hat s,\hat d\in p^N\\ U\notin p^n}}
 t\,q\, f(Y,\hat s,\hat d)\,de_0\\
&=\lambda^{2N}\beta^N
 \int_{U\notin p^\ell}\widetilde\Phi_N(u)\,
 f(Y,u\hat s,u\hat d)\,d\mathcal M_5 .
\end{aligned}}
\tag{21}
$$
这里只在 f 不依 C、$H_1$ 时将它移到 (18) 两项之外。
如果另附这些伙伴的测试或切集，第一项必须配
$f\circ P_{\widehat H,u}\circ P_{L_\zeta,u}$，
第二项配
$f\circ P_{\widehat H,u}\circ P_{L_\zeta,u}\circ P_{M_\zeta,\kappa}$；
两项不可合成 (21) 的单个 f。
若新增测试也不保纯 C 平均，必须回 R767(19) 的未平均边界。
这些限制不影响下面的全部原 Y、帽域、U、P 和 $E_\perp$ 观察。

特别，R764 的真正同域首行有无歧义的精确式
$$
\boxed{
\int_{\mathcal D^\infty_{n,N}}\frac{t}{P}q\,de_0
=\Omega\lambda^{2N}\beta^N
 \int_{\substack{Y\ {\rm unit}\\ U\notin p^\ell}}
 \frac{\widetilde\Phi_N(u)}{b_YY+uZ_0}\,d\mathcal M_5.
}
\tag{22}
$$
另附精确 t-unit 时，右边乘 $1-\beta\kappa$；
其余 t 环带归一系数按 R764 保留。
$h_W$ 的 (22) 乘 $\omega$。
若附原物理 $v_p(E_\perp)=N+r$，右侧附其真实 $r$ 环带；
(18) 两轴都正交于帽平面，故此前该环带确实不动。

## 6. 原失败轴的 whole 第300层核，无新射线

为把一个真正的 U 浅条件完全转为有限正矩，清单位后写
$$
\boxed{
U_0=17\delta U
=(1,-15,11+21\omega,10+21\omega,11\delta,-46\delta).
}
\tag{23}
$$
这是原六输入中的整数行。其范数准确为
$$
N(U_0)=7599=3\cdot17\cdot149,\qquad N(U)=149/17.
$$
前五个系数模2非零，最后一个为零，故是标准 odd 半特征。
U 正交于 Y、t、C、$H_1$；$\mathcal T$ 固定 U。
因此整个 U 轴的 theta 空间是原 canonical
$\mathcal S_{7599}^{\rm odd}$，保全部伙伴。
C 平均与该轴相容，t 的正一收缩亦与它交换。

现射线上 $g_\pi$ 模2、3为1，模17为 $-1$。
149在 K 中惰性；其剩余 norm-one 群阶150。
于是，不加任何149同余条件，
$$
g_\pi^{150}\equiv1\pmod{2\cdot7599}.
\tag{24}
$$
$p>163$ 已使全部清分母为单位。
原 odd canonical Heisenberg 规范与不可约性因而给
$$
K_{7599}^{150}=\epsilon_p I
$$
于整个空间；此时尚不猜 $\epsilon_p$。

付其绝对平方，取
$$
a_*=47\delta,\qquad b_*=18\delta,\qquad
N(a_*)+N(b_*)=3(47^2+18^2)=7599.
$$
真实非零两 sigma 联合
$$
\sigma(a_*z-\bar b_*w)\sigma(b_*z+\bar a_*w)
\tag{25}
$$
两轴正交、变基行列式7599，且 a 为 odd、b 为 even，
所以两个轴均是同一个标准 odd degree7599 半特征。
两原独立 sigma 同时深150的系数是
$\beta^{300}=\lambda^{300}$；
按两个正交 whole 核返回的系数是
$\lambda^{300}\epsilon_p^2$。
变基在 p 处可逆，两个域是同一实际域，两个物理缩放也相同。
由 (25) 非零，得 $\epsilon_p^2=1$。因此
$$
\boxed{K_{7599}^{300}=I.}
\tag{26}
$$
特别，对本文整个原来源及 (20)，
$$
\boxed{
\mu|_{U\in p^{300r}}
=\lambda^{300r}(P_{U,\kappa^{300r}})_*\mu,\qquad r\ge0.
}
\tag{27}
$$
这不是声称一层 U 核为 scalar。未经支付的单层第二态没有被省略；
(27) 只使用已定标的完整第300幂。

## 7. 一个真实固定深度差的五条件矩

现在取原整数
$$
n=N+300,\qquad m\ge n.
\tag{28}
$$
这个选择仍是 R764 的原共同域，未取极限代替有限域。
令
$$
R_U=P_{U,\kappa^{300}},\qquad
\Psi_N(u)=\widetilde\Phi_N(u)
          -\lambda^{300}\widetilde\Phi_N(u)\circ R_U.
\tag{29}
$$
因为 $R_U$ 固定 Y，(27) 给真实完整来源恒等式
$$
\boxed{
Y_*(1_{U\notin p^{300}}\widetilde\Phi_N(u)\mathcal M_5)
=Y_*(\Psi_N(u)\mathcal M_5).
}
\tag{30}
$$
这是原 U 浅失败条件的第二项，不是另加的中性测试。
所有权均完整转置；特别 $R_U$ 一般改变 J、$K_\zeta$ 和 $Z_0$。

设 $\mathbb T$ 是 R767(33)–(35) 的固定单位三角矩阵，
$r_i=5+6i$。原共同条件来源的全部五坐标准确为
$$
\boxed{
\begin{aligned}
m_{i,N}^{\rm nat}
 &=\frac1{b^i r_i!\Omega^{r_i}}
   \int Y^{r_i}\Psi_N(u)\,d\mathcal M_5,\qquad 0\le i\le4,\\
\operatorname{coord}\left[
 \Omega^{-1}Y_*(t\,1_{\hat s,\hat d\in p^N,\ U\notin p^{N+300}}
 q\,e_0)\right]
 &=\lambda^{2N}\beta^N\mathbb T^{-1}
   (m_{0,N}^{\rm nat},\ldots,m_{4,N}^{\rm nat})^t .
\end{aligned}}
\tag{31}
$$
(31) 是同一个原 q 的实际五条件矩，不是未切全域的 (R767)(26)。
它只需 (20) 上的正矩：
q 最高权30，$r_i\le29$，所以五变量总正次数不超过59；
还原 t 首矩后，原六 sigma 总次数不超过60。
原 $p>163$、全部整分母和真正 $\lambda,\kappa,u$ 范围完全足够。

同一条件来源仍在原裸 $\mathcal S_{34}$、type5中：
每个权方向都在 $Y^\perp$，所有齐次次数为 $0\bmod6$，
U 的第300层返回也固定 Y。
故其两算术幅度和完整三维 primitive 块必须按 R767(36) 全部读取。
(31) 没有据有限维数或裸非零猜某个幅度非零。

在固定 p 下，原 $P_{d,N}$ 的系数是同一个
$K(\lambda,\kappa,u,\eta)$ 有理式；其分母在 $u=0$ 为单位，
由 R734 的原整逆支付。式 (17)–(19)、(29) 对 u 只有非负幂。
因此 (31) 在清掉原单位分母后是明确有限 u 多项式。
$\lambda^{300}$、$\kappa^{300}$ 仍是实际代数参数，未以
$\kappa=0$ 或辅助域数值代替。
各块 $\Omega^{-d}$ 与正矩周期逐项相消，所有来源坐标在 K。
这一有限 carrier 允许以后按 R753 在真正有理系数上取 $u\to0$；
但实际非零条件必须由 (31) 自己支付。

## 8. 精确有理观察、浅域与总中央边界

在 (28) 的同一域，(22) 还给完整有理观察返回
$$
\boxed{
\begin{aligned}
\int_{\mathcal D^\infty_{N+300,N}}\frac{t}{P}q\,de_0
=\Omega\lambda^{2N}\beta^N\int_{Y\ {\rm unit}}
\left\{
 \frac{\widetilde\Phi_N(u)}{b_YY+uZ_0}
 -\lambda^{300}
  \frac{\widetilde\Phi_N(u)\circ R_U}
       {b_YY+u(Z_0\circ R_U)}
\right\}d\mathcal M_5 .
\end{aligned}}
\tag{32}
$$
两个分母不同，不能只在权上作 (29) 而冻结观察。
它们均为单位，且与 $b_YY$ 相差 $p^N$，故
$$
(32)=
b_Y^{-1}\Omega\int_{Y\ {\rm unit}}Y^{-1}\,
 d\nu_{\mathcal L_N}
+p^N\mathcal O,
\tag{33}
$$
其中 $\mathcal L_N$ 是 (31) 的实际条件来源，已经包含
$\lambda^{2N}\beta^N$。若需要更高阶，必须继续 (32) 的两个
完整分母，不用 (33) 代整个恒等式。

R764 的两个 W 行之差仍由其式(40) 给出：
原 $\lambda^n\beta^m\kappa^m$、$d_p$、
$1-\beta\kappa$（若有精确 t 环带）和全部高阶对数尾都保留。
本篇只把其中一条真正条件首行变成 (31)、(32)；
没有把它认成原未加权 $J'_S$ 或 $J'_T$。

全 t 分层仍包括 $m<N$ 的三个浅独占支、
$N\le m<n$ 的三条不同失败支、$m\ge n$ 的共同深支和整个深尾。
原 $I/O/X$、R737 的 cd 返回 E-unit、reference 项和原 T 相反外部
全部继续存在。文末增补虽然支付 (31) 的实际负一非零，
仍须在这个完整分割中支付另一条原中央约束，才可能关闭主目标。

## 依赖与执行范围

- [R764](R764-y-preserving-six-axis-and-three-cd-exterior-domains.md)：原整框架、Y/t 核、三个真实 CD/O 域及规范观察。
- [R767](R767-native-t-moment-and-complete-five-partner-boundary.md)：完整五伙伴来源、五条件坐标与算术/primitive 投影。
- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：未改的最终测试、整逆、全部参数与周期归一。
- [R529](R529-original-low-j-k-core-and-complete-st-carry.md)、[R533](R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md)：标准小度数的完整核与绝对规范。
- [R737](R737-common-depth-elimination-and-native-primitive-strips.md)：原 cd 与 paired 外部的完整范围。
- [R753](R753-discontinuous-point-projectors-and-finite-carrier-limits.md)：有限 carrier 与无限点投影的区别；本篇只使用有限有理坐标。

以上完整格、半特征、whole 核与真实域恒等式由代数证明支付。
式(31) 的具体幅度及其非零后果见以下已完成的公开运行增补；
可重算输出不另存文件。


## 公开执行增补 A. 同一条件来源的两算术幅度、负一非零与原外部

本增补使用已完成的公开 Actions。正文的格、whole 核和域身份不依赖此运行；运行只读取式(31) 已定义的实际有理坐标。

### A.1 真实运行及四个辅助非零值

- producer：[check-r773-native-conditional-five-moments.js](../scripts/check-r773-native-conditional-five-moments.js)；
- 参数：`--max-block=4 --taus=2,3 --with-b --b-g-blocks=3 --neutral-degree=12`；
- source commit：a98e0fc95f624d7fd4a83d71f86a19b7de2cf165；
- run：43726080626；job：132848187370；
- producer SHA256：a8d5b436e383831f418b04f546d6d18d7c1b13cde3f5a9d81694f692a7aec5b7；
- 原 R719 producer SHA256：29bd414c63ac4fdca93ae4b56ccdf2ccaa2114395bf96a52d2e8fd1ea809fdb2；
- stdout：6788字节；SHA256：
  1d58673c8174e98ef2af10087a97dc2a8bb5c8c78e93bb1ca20a40c821db6a4d。

该脚本从原 R594/R702/R715/R734 算法重建 q，不读取旧生成输出。
它在完整原50行、quarter 行和两条核列均保留的情况下，按
(18)、(20)、(29)、(31) 计算两个完整正矩生成式。
原 M-unit 第二项与 $\lambda^{300}P_{U,\kappa^{300}}$ 都先保留，
随后才取边界专门化 $\kappa=u=0$。
在这个边界，$P_{U,\kappa^{300}}$ 成为真实正交投影 $P_{U,0}$，
不是把 D 单独设为零。

令
$$
\mathcal F_\eta(\lambda,\kappa,u)
=\sum_{j=0}^4 c_j(\lambda,\kappa,u,\eta)\Xi_j,\qquad
c=\mathbb T^{-1}m^{\rm nat},
\tag{A1}
$$
即式(31) 去掉共同单位 $\lambda^{2N}\beta^N$ 后的完整来源。
用 R767 的全 CM13 投影写
$$
\mathcal F_\eta
=A_{\omega,\eta}D_{\omega,b}
 +A_{-,\eta}D_{-,b}+\mathcal F_{{\rm prim},\eta}.
\tag{A2}
$$
实际矩阵输入是在 $\mathbf F_{1009}$、$\omega=374$、
$b=\Omega=1$、$\lambda=(1-\tau)/\tau$。输出为

| $\tau$ | $\eta$ | $A_{\omega,\eta}(\lambda,0,0)$ | $A_{-,\eta}(\lambda,0,0)$ |
|---:|---:|---:|---:|
| 2 | $+1$ | 844 | 722 |
| 2 | $-1$ | 831 | 50 |
| 3 | $+1$ | 453 | 462 |
| 3 | $-1$ | 582 | 87 |

四点均重新验证原 q 的全部行；R734 的 a、$b_0$ 为629、240，
规范后真正 $\mathfrak j_2$ 为319。没有把旧五行读数50改称 $\mathfrak j_2$。
原50阶逆、五阶逆及 a 在这些点都非退化。
$1+\lambda=1/\tau$ 也非零；显示的新几何分母和正矩分母不含1009。

三个 primitive 坐标在这四个辅助点都为零。
这个有限零值**没有**被提升为 $\mathcal F_{{\rm prim},\eta}=0$。
以下证明完整保该三维来源，只使用表中两列的非零。

### A.2 旧射线上的实际单位幅度，量词包括全部 N

式(A1)、(A2) 的每个坐标都是正文已经定义的
$K(\lambda,\kappa,u)$ 有理式，$\eta$ 分别取 $\pm1$。
其固定分母来自原两级整逆、(13)、固定三角 reader、
完整 CM13 投影和 (23) 的整数几何。
这里没有 $\kappa^{-N}$ 遗留；它已经在真实 carry 深域返回中消去。

对每个 $\eta$，清掉这些分母，取
$A_{\omega,\eta}(L,0,0)$、$A_{-,\eta}(L,0,0)$ 的有理分子。
表中非零值证明四个固定 $K[L]$ 分子均不是零多项式。
这一步不需要辅助点属于原 ordinary ray，也不把它当一个实际 p。

将四个分子、全部分母的固定 Norm 多项式一并加入
[固定 CM 单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)
的有限乘积，代入 $L=-1/\bar\pi_0$。
在原完整固定射线的相对密度一子族上，该乘积为单位；
所删无限坏集仍为 $O(\sqrt X\log X)$，另删固定有限分母素数。
原射线本身没有被重定义，也未新增149同余条件。

实际 $\kappa=p\lambda^2\in p\mathcal O$、$u=\kappa^N\in p\mathcal O$。
所有分母在 $(\kappa,u)=(0,0)$ 为单位，故对上述同一素数子族，
**两种 $\eta$ 和所有 $N\in4\mathbf Z_{>0}$ 同时**有
$$
\boxed{
A_{\omega,\eta}(\lambda,\kappa,\kappa^N)\in\mathcal O^\times,\qquad
A_{-,\eta}(\lambda,\kappa,\kappa^N)\in\mathcal O^\times.
}
\tag{A3}
$$
$\lambda^{300}$ 完整属于这些有理式，未从单位性论证中删去。
有限测试证明的是固定分子非恒等零；
(A3) 才是实际 CM 参数上的结论。

### A.3 真正条件负一行非零，保整个 primitive 块

定义
$$
\mathfrak I_p(u)
=\Omega_p\int_{\mathcal O^\times}Y^{-1}
 d\nu_{\mathcal F_\eta(\lambda,\kappa,u)}(Y).
\tag{A4}
$$
R735 给 $D_{\omega,b},D_{-,b}$ 的原负一值及其共同周期点公式，
两值非零且在 $\overline{\mathbf Q}$ 上线性独立。
R761 支付整个 primitive 三块的准确 cyclic9 点域和点公式，
包括它们可能为零的情形。
其17惯性标签为 exact order9；两条 rank-one 线是不同的 order3 标签。
等价地，可先用实际2惯性平均杀 primitive，再用两个 cubic 标签分开。

因此，在每个固定 p、N 的**有限** point-log carrier 中，
(A3) 的非零两幅度不能被另一条算术线或 primitive 块抵消。
所有系数均在 K，周期已按 (A4) 统一，不是任意
$\mathbf C_p$ 系数。准确得到
$$
\boxed{\mathfrak I_p(\kappa^N)\ne0.}
\tag{A5}
$$
结合式(31)，这就是原同一测试、原同一有限失败域的结论：
$$
\boxed{
\int_{\substack{Y\ {\rm unit}\\
 \hat s,\hat d\in p^N,\ U\notin p^{N+300}}}
 \frac{t}{Y}\,q_N^*\,de_0
=\lambda^{2N}\beta^N\mathfrak I_p(\kappa^N)\ne0 .
}
\tag{A6}
$$
这不同于未切原域的 R767(27)。这里两条帽深和原 U 失败条件
都在，未把裸 $D_\omega$ 代入一个新条件域。

### A.4 固定五维 carrier 的极限及真实 P 分母

现在固定一个满足 (A3) 的实际 p。
先除掉原单位相位 $\lambda^{2N}\beta^N$；
该相位一般不随 N 收敛，本文不对它取极限。
(A1) 在 $u=0$ 正则且整，于是
$$
\mathcal F_\eta(\lambda,\kappa,\kappa^N)
=\mathcal F_\eta(\lambda,\kappa,0)+p^N
 \sum_{j=0}^4\mathcal O\,\Xi_j .
$$
这里始终只有同一个五维来源空间。
(A3) 也在 $u=0$ 成立，故按同一个有限点分离证明，
$$
\mathfrak I_p(0)\ne0,\qquad
\mathfrak I_p(\kappa^N)=\mathfrak I_p(0)+p^N\mathcal O .
\tag{A7}
$$
这不是把 point-only 投影延为 $\mathbf C_p$ 连续算子。
先在固定五维坐标中取代数有理系数的极限，再对该明确极限来源
用 R735/R761。它满足 R753 的有限 carrier 条件。

置 $v_p^*=v_p(\mathfrak I_p(0))<\infty$。
对充分大的原 $N\in4\mathbf Z$，$N>v_p^*$ 时，
(A6) 的赋值准确为 $v_p^*$。

对真正 P 观察，使用正文(32) 的**两个完整分母**。
它们在 Y-unit 上都是单位，并分别与 $b_YY$ 相差 $p^N$；
全部权及返回矩阵整有界。因此只有有界解析比较
$$
\boxed{
\lambda^{-2N}\beta^{-N}
 \int_{\mathcal D^\infty_{N+300,N}}\frac{t}{P}q_N^*\,de_0
=b_Y^{-1}\mathfrak I_p(0)+p^N\mathcal O .
}
\tag{A8}
$$
对这个有理积分或其无限幂展开，未施加任何点惯性投影。
所以 $N>v_p^*$ 时，(A8) 自身非零且赋值 $v_p^*$。
另附 t-unit 的原行准确乘 $1-\beta\kappa$，这个因子为单位。

回到 R764(40)，固定 $n=N+300$、$m\ge n$，取两个不同 $j,k$。
记 $I_j$ 为 R764(33) 在同一个共同深外部块上的 T 中央行。
则完整首项为
$$
\begin{aligned}
I_j-I_k
={}&-\frac{(1+3\omega)(\omega^{2j}-\omega^{2k})d_p}{b_Y}
 \lambda^{n+2N}\beta^{m+N}\kappa^m\mathfrak I_p(0)\\
&\quad+p^{m+N}\mathcal O+p^{4m}\mathcal O .
\end{aligned}
\tag{A9}
$$
所有显示系数除 $\kappa^m\mathfrak I_p(0)$ 外均为单位。
故在同一固定 p 的充分大 N 范围，
$$
\boxed{v_p(I_j-I_k)=m+v_p^*.}
\tag{A10}
$$
若使用精确 t 环带，首项再乘 $1-\beta\kappa$，
赋值不变；原高阶对数尾仍在 (A9) 的准确范围内。

### A.5 原中央实际要求的完整外部，不能删除

令 $r_n=(-\kappa)^n$，并保原全归一观察
$$
f_{j,n,w}
=1_{W_j\circ P_{Y,r_n}^{-1}\ {\rm unit}}
 \left\langle W_j\circ P_{Y,r_n}^{-1}\right\rangle^{d_pw}.
$$
R764 的完整 Y 核与原 $\pi_4$ 身份给
$$
\boxed{
\int_{\{Y\in p^n\}}f_{j,n,w}\,q_N^*\,de_0
=\lambda^n\beta^N\,6\delta\,k_jJ_T(w),
\quad (k_0,k_1,k_2)=(1,0,-\omega^2).
}
\tag{A11}
$$
对于 $m\ge n$，三个原
$\mathcal O_{j,n}\cap\{t\in p^m\}$ 是同一个完整物理块；
记它为 $\mathcal B_{n,m,N}$。将 (A11) 的域精确分成该块与
$\{Y\in p^n\}\setminus\mathcal B_{n,m,N}$。
记后者使用同一 $f_{j,n,w}$ 的中央导数为 $E_j$，则
$$
\boxed{
E_j-E_k
=\lambda^n\beta^N6\delta(k_j-k_k)J_T'(0)-(I_j-I_k).
}
\tag{A12}
$$
所以在原 $J_T'(0)=0$ 假设下，实际强制的是
$$
E_j-E_k=-(I_j-I_k),\qquad
v_p(E_j-E_k)=m+v_p^*,
\tag{A13}
$$
而不是 $I_j-I_k=0$。这给出了同一个原全外部必须承担的
明确非零差和准确赋值。

这里的完整外部包含所有浅 t 支、帽/U 补域、原观察各自的
unit 进入或失败支，以及按原坐标运输的 E 条件；
它不是把其中某一个参考支单独叫作 $E_j$。
原 R737 的 cd 返回 E-unit 仍保留。

还可准确分清 S 中央与本首行所在的来源。定义真实两投影
$$
e^{(1)}=\frac{\omega h_W-\omega^2e_0}{1-\omega^2},\qquad
e^{(\omega^2)}=\frac{e_0-\omega h_W}{1-\omega^2}.
\tag{A14}
$$
它们分别是 $\mathcal T_*$ 的特征1、$\omega^2$ 来源。
对任何本文 $\mathcal T$-不变的伙伴域 $\mathcal D$，
q、Y也不变，故
$$
Y_*(1_{\mathcal D}q\,e^{(\omega^2)})=0,
\qquad
Y_*(t\,1_{\mathcal D}q\,e^{(\omega^2)})
=Y_*(t\,1_{\mathcal D}q\,e_0).
\tag{A15}
$$
第二式使用 $t\mathcal T=\omega^2t$，保同一域与权。
另一方面完整
$$
W_*e^{(\omega^2)}=\frac{6\delta}{1-\omega^2}\nu_T .
\tag{A16}
$$
因此 S 的零并不在 (A15) 中产生一个额外负一零；
T 的原中央控制 (A16) 的**完整行**，其真实条件补偿正是
(A12)。本增补支付了原共同块的非零和全外部的必要差，
尚未将这个外部消掉，主中央目标仍保持开放。
