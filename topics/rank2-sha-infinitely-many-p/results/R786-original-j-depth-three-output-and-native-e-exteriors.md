# R786 — 同一原测试的 J 深全三输出、有限条件来源与两种 E 外部

日期：2026-11-15。**状态：以下完整来源、实际域返回及中央分解已证明。**

本文固定 R734 的同一个 $q=q_N^*$，不重新适配。R785 已把原共同三维深域内的物理 $E$ 门准确送成 $J$ 深门。本文支付这个 $J$ 条件的整个来源：先返回 $J$，再逐支返回原 carry 的两条隐藏轴，得到固定有限 theta 来源；$Y,P,t$ 三个观察全程不变。保留第四输出 $J$ 时，也给出原帽与 $U$ 失败条件的完整转置。

由此，纯 $Y/W$ 的两个真实外部均有精确两模式公式；原从 $Y$ 核返回的混合 $T$ 外部则保留一个明确的联合 Cauchy 行。其第一法向系数是实际五维条件来源，不再是一个未指定的条件测度。原 $E$ 深、浅两行之和准确读取 R767 的非零 $D_\omega$ 负一值；这不把任一个外部自行置零，也不产生尚未证明的中央矛盾。

## 1. 原三态、观察三维与隐藏 J

沿 R773、R777、R785，置
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad b=17,
\quad\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad u=\kappa^N,\quad N\in4\mathbf Z_{>0}.
\tag{1}
$$
保持全部旧射线、固定坏集、原整逆及 $p>163$。物理六输入仍为
$(\xi_1,\xi_2,\xi_3,x,c,d)$；所有下面的来源可同时施加原纯 $C$ 六角平均。
为简记，不再在每一式重复这个平均。

记
$$
\begin{gathered}
C=(\xi_1-\xi_3+x)/\delta,\quad
B=-\xi_1+\omega\xi_3-\omega^2x,\quad H_1=B+2\xi_2,\\
r=(\xi_1-\omega^2\xi_3+\omega x)/\delta,\quad
s=r+c,\quad t=r-c,\quad
A_0=2\delta\xi_2-\frac{4\delta}{3}B,\\
Y=A_0+s+2d,\quad a=1+3\omega,\quad
P=Y+as+2d,\quad W=P-at,\quad W_j=P-a\omega^{2j}t,\\
F=s-B+\omega^2\xi_2+(2+3\omega)d,\quad
g=3-2\omega,\quad f=-\bar g/7=-(5+2\omega)/7,\\
G=13H_1+gF,\qquad J=F-fH_1 .
\end{gathered}
\tag{2}
$$
原三个态为 $e_0,e_1,e_2$，$h_W=e_1+e_2$；其完整 $W$ 核为
$$
Ke_0=e_1,\quad Ke_1=e_0,\quad
Ke_2=-e_0-e_1-e_2,\quad Kh_W=-h_W .
\tag{3}
$$
定义
$$
c_B=1-\omega^2,\qquad
B_0=(e_0-\omega h_W)/c_B,\qquad B_1=KB_0 .
\tag{4}
$$
$B_0$ 是 R777 的原来源。下文的 $\mu$ 可取原三态空间中的任何固定线性组合，$\rho_\mu=q\mu$。

原观察空间与正交伙伴是
$$
\mathcal V=\operatorname{span}(Y,P,t),\qquad
\mathcal V^\perp=\operatorname{span}(C,H_1,J).
\tag{5}
$$
三个隐藏行彼此正交，范数分别为 $3,7,72/7$。
特别，$q$ 只依 $C,H_1,J$，因而逐点固定于 $\mathcal V$ 的所有线性缩放。
**$q$ 不固定 $J$ 缩放**，其变化必须按下文的六支支付。

令
$$
Z_0=P-b_YY,\quad b_Y=(20+3\omega)/17,\quad
Z=W-b_YY=Z_0-at,\quad h_0=17+3\omega .
$$
物理 $E=E_{YW}$ 的整个身份是
$$
\boxed{
E=E_{\mathcal V}+e_JJ,\qquad
E_{\mathcal V}=-\frac{17(25+48\omega)}{144}Z_0+h_0t,\qquad
e_J=-\frac{1841}{72}.}
\tag{6}
$$
$1841=7\cdot263$，故 $e_J$ 在当前范围为单位。
$E$ 同时正交于 $Y,W$，但不正交于整个 $\mathcal V$。

一切物理缩放采用原约定
$$
P_{L,z}=I+(z-1)\bar L^{\,t}L/N(L).
\tag{7}
$$
$M_{\mathcal V,z}$ 对 $\mathcal V$ 乘 $z$，对其正交补恒等。

## 2. J 和原两条 carry 轴在全部三态上的合法返回

R785 的完整标准 degree1512 平方、绝对锚和原半特征，已给
$$
e_0|_{J\in p^N}=\lambda^N(P_{J,u})_*e_0,\qquad
h_W|_{J\in p^N}=\lambda^N(P_{J,u})_*h_W .
\tag{8}
$$
这里 $N\in4\mathbf Z$，只使用已付的偶深身份。

式(8)也适用于 $e_1,e_2$，且保全部伙伴。理由可直接在来源上支付：
$J\perp W$，故 $P_{J,u}$ 与 $P_{W,\kappa}$ 交换、并各自固定另一条深条件。
把 $e_0$ 限制到 $J$ 深 $N$、$W$ 深1，分别先用(8)与(3)。
约去非零标量及可逆线性推前 $(P_{W,\kappa})_*$，得到 $e_1$ 的(8)；
再由 $e_2=h_W-e_1$ 得到第三态。这一步没有把单层 $J$ 核猜成 scalar。
因此
$$
\boxed{\mu|_{J\in p^N}=\lambda^N(P_{J,u})_*\mu}
\tag{9}
$$
对本篇全部 $\mu$ 成立，但尚未把 $q$ 穿过它。

固定 $\zeta\in\mu_6$，令
$$
L_\zeta=fH_1-\zeta C,\qquad
M_\zeta=7\bar f C+\bar\zeta H_1 .
\tag{10}
$$
这两行正交，范数 $26/7,26$，都垂直于 $\mathcal V,J$。
R773§4.1 已支付 $7\delta L_\zeta$、$\delta M_\zeta$ 的
degree546、78 标准 even 半特征、完整中心及真实 Theta 锚，两个 whole 核均为 $\beta$。
两轴又都垂直于 $W$。用刚才的相同 $W$ 核约消论证，把该完整身份从
$e_0,h_W$ 扩至 $e_1,e_2$。等价地，原 $W$-quarter 平移沿这两条轴的 flat 配对恰为零。
于是本篇使用
$$
\boxed{
\mu|_{L_\zeta\in p^N}=\beta^N(P_{L_\zeta,u})_*\mu,\qquad
\mu|_{M_\zeta\in p}=\beta(P_{M_\zeta,\kappa})_*\mu .}
\tag{11}
$$
它们均保原三态和整联合；没有把 quarter 来源换成原边际。

## 3. 同一个 q 的六支、全部 E 次数逆与 M-unit 第二项

按 R773(13)—(14)，将实际原权写成齐次块
$d\in\{6,12,18,24,30\}$。其系数仍是 R734 真实
$(\lambda,\kappa,u,\eta)$ 上的同一个有理式。记
$$
\widehat P_{d,N}
=\sum_{a+e+g'=d}
 \frac{[D^aE_c^eG^{g'}]P_{d,N}}{1+\lambda\kappa^e}
 D^aE_c^eG^{g'} .
\tag{12}
$$
原权准确为
$$
q=\sum_d\frac1{6b^{d/6}\Omega^d}
 \sum_{\zeta\in\mu_6}
 1_{\{F-\zeta C\in p^N,\ F+13\zeta C\ {\rm unit}\}}
 \widehat P_{d,N}((F-\zeta C)/u,F+13\zeta C,G).
\tag{13}
$$
原整个 $E_c$ 次数逆已经包含在(12)；不在返回坐标重新定义它。

先用(9)。$P_{J,u}$ 固定 $C,H_1,Y,P,t$，并使
$$
F\longmapsto fH_1+uJ,\qquad
G\longmapsto72H_1/7+guJ .
\tag{14}
$$
因此(13)的深门准确成为 $L_\zeta\in p^N$，不是只模 $p$ 的近似。
在此门上，unit 条件准确为 $C$-unit。

再用(11)返回 $L_\zeta$。令
$$
\begin{aligned}
C_\perp&=C+\frac{7\bar\zeta}{26}L_\zeta
            =\frac{7f}{26}M_\zeta,&
H_\perp&=H_1+\frac{7g}{26}L_\zeta
            =\frac{7\zeta}{26}M_\zeta,\\
K_\zeta&=J-\frac{36}{13}L_\zeta,&
E_{0,\zeta}&=14\zeta C_\perp,\qquad
G_{0,\zeta}=\frac{72}{7}H_\perp .
\end{aligned}
\tag{15}
$$
三个实际参数恰为
$$
D'=L_\zeta+J,\qquad
E_c=E_{0,\zeta}+uK_\zeta,\qquad
G=G_{0,\zeta}+guK_\zeta .
\tag{16}
$$
同时 $C$-unit 准确返回为 $M_\zeta$-unit。
最后以(11)做这个 unit depletion，得到完整多项式
$$
\begin{aligned}
\mathcal Q_{d,\zeta,N}(u)
={}&\widehat P_{d,N}(L_\zeta+J,E_{0,\zeta}+uK_\zeta,
                                      G_{0,\zeta}+guK_\zeta)\\
&-\beta\,\widehat P_{d,N}(L_\zeta+J,\kappa E_{0,\zeta}+uK_\zeta,
                                      \kappa G_{0,\zeta}+guK_\zeta),
\\
\widetilde\Phi_N(u)
={}&\sum_d\frac1{6b^{d/6}\Omega^d}
                \sum_{\zeta\in\mu_6}\mathcal Q_{d,\zeta,N}(u).
\end{aligned}
\tag{17}
$$
第二项系数为 $-\beta=+\lambda$；原 $\eta$ 仍在 $P_{d,N}$ 内。
该项同时缩放两个参数，不与(12)免费约消。

所有 $\mathcal Q$ 只依 $C,H_1,J$。每一块仍齐次次数 $d$。
到这里没有忘任何观察，也没有删除原 unit 第二项。

## 4. 完整 J 条件来源：三输出与保 J 的四输出

设 $\pi_3=(Y,P,t)$、$\pi_4^{\,J}=(Y,P,t,J)$。
对任意完整连续测试 $f(Y,P,t,J)$，(9)—(17)严格给
$$
\boxed{
\int_{J\in p^N} f(Y,P,t,J)\,q\,d\mu
=\lambda^N\beta^N
 \int f(Y,P,t,uJ)\,\widetilde\Phi_N(u)\,d\mu .}
\tag{18}
$$
三个正交观察在每一步都固定；$J$ 只在第一步乘 $u$。
后两条隐藏核固定 $J$，故(18)保留它作为第四输出。

特别，定义完整三输出来源
$$
\mathfrak F_{\mu,N}^{+}
=(\pi_3)_*(1_{J\in p^N}q\mu),\qquad
\mathfrak F_{\mu,N}^{-}
=(\pi_3)_*(1_{J\notin p^N}q\mu).
$$
则
$$
\boxed{
\mathfrak F_{\mu,N}^{+}
=\lambda^N\beta^N(\pi_3)_*(\widetilde\Phi_N(u)\mu),\qquad
\mathfrak F_{\mu,N}^{-}
=(\pi_3)_*(q\mu)-\mathfrak F_{\mu,N}^{+}.}
\tag{19}
$$
因 $N\in4\mathbf Z$，第一系数也可写为 $\lambda^{2N}$；保留
$\lambda^N\beta^N$ 更便于追踪两个不同来源步骤。

原 $\pi_4=(Y,W,W',G)$ 中性身份在忘 G 后还给
$$
\boxed{(\pi_3)_*(q\mu)=\beta^N(\pi_3)_*\mu .}
\tag{19a}
$$
这里用 R785 的 $\operatorname{span}(Y,P,t)=\operatorname{span}(Y,W,W')$。
原 e0 的身份就是 R734 保留的整 $\pi_4$ 返回。
$\mathcal T$ 保整个 $\mathcal V$，在其中固定 Y、P并把 t 乘 $\omega^2$，
而 $q\circ\mathcal T=q$，故它运输出 hW 的(19a)。
再把 e0 的(19a)限制到 W 深1，用(3)和 q 对 W 的正交性，
约去同一个 W 推前便得到 e1；e2=hW−e1完成三态。
因此(19)的浅来源准确为
$\beta^N(\pi_3)_*\mu-\mathfrak F_{\mu,N}^+$，
也属于同一个固定有限来源空间。这里只遗忘伙伴，不给任何 mixed 子域赋零。

若测试另依 $C,H_1$，则不能用(18)把它移出两项。
应回到每个 $\zeta$：第一项的测试完整转置为
$f\circ P_{J,u}\circ P_{L_\zeta,u}$，第二项再复合
$P_{M_\zeta,\kappa}$。本文所有 $Y,P,t,J$、帽/U 和物理 E 事件都在(18)的合法范围内。

## 5. 固定有限来源与实际读取范围

令原三态的完整生成函数为
$$
\Theta_\mu(\mathbf z;\mathbf v)=
\int\exp\!\left(
\frac{Yz_Y+Pz_P+tz_t+C v_C+H_1v_H+Jv_J}{\Omega}
\right)d\mu .
\tag{20}
$$
这是一个形式生成式，原 quarter theta-group 相位均已经包含在 $\mu$ 中。
它没有假定非正交的 $Y,P$ 两轴为外张量积。

把(17)中的 $C,H_1,J$ 换成
$\partial_{v_C},\partial_{v_H},\partial_{v_J}$，即可从(20)读取(19)。
所有导数总阶只在 $6,12,18,24,30$ 中。
因此去掉 $\lambda^N\beta^N$ 后，(19)属于由这些固定正交 jets 张成的有限来源空间。
它不是随 $N$ 增长的 $p^N$-torsion 池。

正交性保证这些隐藏 jets 不改变第一观察的 theta automorphy。
对整个 $\pi_3$，可在原有固定整覆盖上读同一个三维 theta 来源；
对保留 $J$ 的四输出，使用(20)同一有限阶 jet 模块即可，不宣称 $J$ 方向导数仍属于未微分的旧 theta 空间。

全部系数在 $K(\lambda,\kappa,u,\eta)$ 中。
各 $\Omega^{-d}$ 已同正矩的 $\Omega^d$ 抵消，$b^{d/6}$ 为原固定归一。
原 R734 分母、(12) 和固定几何分母都保留。
清掉这些已付分母后，对 $u$ 是一个固定次数的多项式；
这里只说固定次数，不把原整逆分子的次数偷换成30。
在固定 p 下它在 $u=0$ 正则，适用 R753 的有限 carrier 取极限规则。

以下三个有限读取特别具体：

1. 对任一原三态，$W_*\mathfrak F_{\mu,N}^{+}$ 在原 $\mathcal S_{72}$ 的 type0 十三维块中。基可取
   $\sigma^{72}x^{36-3j}$，$0\le j\le12$。
   完整正矩阶 $0,6,\ldots,72$ 决定来源；原权计入后总正次数不超过102。
2. 对 $\mu=B_0$，$\Omega^{-1}Y_*(t\mathfrak F_{\mu,N}^{+})$ 在原裸 $\mathcal S_{34}$ 的 type5 五维块中。它由下节的五个真实矩完全决定。
3. 对 $e_1,e_2$ 的完整 $Y$ 边际，保原 $2Y$ 覆盖的 $\mathcal S_{136}$ 二十三维块，不免费降为裸 $\mathcal S_{34}$。首 $0,6,\ldots,132$ 正矩加原权后总次数不超过162，仍小于当前 p。

以上是完整来源界，不从维数或单个有限值给中央、负矩赋零。

### 5.1 已有公开运行中的 J-only 五坐标

R767 的五伙伴来源 $\mathcal M_5$ 满足
$\Omega^{-1}\pi_*(tB_0)=\mathcal M_5$，保其全部五个伙伴。
令
$$
\mathcal L_N^J=Y_*(\widetilde\Phi_N(u)\mathcal M_5).
$$
式(18)准确给
$$
\boxed{
\Omega^{-1}Y_*(t\,1_{J\in p^N}qB_0)
=\lambda^N\beta^N\mathcal L_N^J .}
\tag{21}
$$
以 R767 的原五基及单位三角矩阵 $\mathbb T$，$r_i=5+6i$，其完整坐标是
$$
\boxed{
\operatorname{coord}(\mathcal L_N^J)
=\mathbb T^{-1}\left(
\frac{\int Y^{r_i}\widetilde\Phi_N(u)\,d\mathcal M_5}
 {b^i r_i!\Omega^{r_i}}\right)_{i=0}^{4}.}
\tag{22}
$$
这正是 R773 producer 已计算的第一返回项。
本篇去掉的是随后原 $U$ 失败所需的第二项；未把旧条件来源原样移过来。

该公开 run 43726080626、job132848187370 的
first_return_theta 已给下列边界坐标：

| 辅助 $\tau$ | $\eta$ | 原五基下降坐标 |
|---:|---:|---|
| 2 | $+1$ | $(383,347,810,68,231)$ |
| 2 | $-1$ | $(616,701,816,967,236)$ |
| 3 | $+1$ | $(728,722,862,956,88)$ |
| 3 | $-1$ | $(162,168,235,834,605)$ |

规范为 $\mathbf F_{1009}$、$\omega=374$、$b=\Omega=1$、
$\lambda=(1-\tau)/\tau$、$\kappa=u=0$。
原50行、quarter、核列、M-unit项均在该实际执行中验证。
表只读取已经公开的输出，不另执行、也不存生成数据。

这些数说明所定义的五维有理来源并非恒零。
它们本身尚未给 $\mathcal L_N^J$ 的两个算术投影或负一值非零；
R773 中后续 $U$ 扣除的算术幅度不得直接代入(22)。

## 6. 共享深平面把物理 E 深、浅准确送成 J 深、浅

记
$$
\mathscr V_r=\{Y,P,t\in p^r\},\qquad r\in2\mathbf Z_{\ge0}.
$$
它等价于 R785 两个正交框架中各三轴同时深 r。
该篇已付全部三态
$$
\rho_\mu|_{\mathscr V_r}
=\lambda^{3r}(M_{\mathcal V,\kappa^r})_*\rho_\mu .
\tag{23}
$$
若 $r\ge N$，由(6)及 $e_J$ 为单位，
$$
E\circ M_{\mathcal V,\kappa^r}\in p^N
\iff J\in p^N .
\tag{24}
$$
浅条件也准确取补集。设 $\epsilon=+$ 表示 E 深 N、J 深 N，
$\epsilon=-$ 表示相应浅补集。对任意完整测试 $f(Y,P,t)$，
$$
\boxed{
\int_{\mathscr V_r,\ E^\epsilon}
 f\circ M_{\mathcal V,\kappa^{-r}}\,d\rho_\mu
=\lambda^{3r}\int f\,d\mathfrak F_{\mu,N}^\epsilon .}
\tag{25}
$$
这同时支付深与浅，不把 E 当作三维中的齐次轴，也不删除其固定 $J$ 截距。

## 7. 纯 Y/W 外部的精确两模式，质量全保

对 $L=Y,W$，置
$$
A_{\mu,N}^{L,\epsilon}(w)
=\int_{E^\epsilon}f_w(L)\,d\rho_\mu,\qquad
F_{\mu,N}^{L,\epsilon}(w)
=\int f_w(L)\,d\mathfrak F_{\mu,N}^\epsilon,
$$
其中始终
$f_w(x)=1_{x\ {\rm unit}}\langle x\rangle^{d_pw}$。
因 $E,q$ 与 Y、W 都正交，且两轴在全部三态上的偶深核心已付，
对每个偶数 $r\ge N$ 有
$$
\int_{E^\epsilon,\ L\in p^r}
 f_w(L/\kappa^r)\,d\rho_\mu
=\lambda^r A_{\mu,N}^{L,\epsilon}(w).
\tag{26}
$$
现在取真实完整外部
$$
\mathscr R_{\mu,N}^{L,\epsilon}(r,w)=
\int_{\substack{E^\epsilon,\ L\in p^r\\ \mathscr V_r^c}}
 f_w(L/\kappa^r)\,d\rho_\mu .
$$
由(25)精确相减：
$$
\boxed{
\mathscr R_{\mu,N}^{L,\epsilon}(r,w)
=\lambda^r A_{\mu,N}^{L,\epsilon}(w)
 -\lambda^{3r}F_{\mu,N}^{L,\epsilon}(w).}
\tag{27}
$$
这是同一域上全部质量、Mellin函数和中央导数的身份。

令 $\mathsf T_2$ 将 r 变成 $r+2$，则
$$
\boxed{
\begin{aligned}
(\mathsf T_2-\lambda^6)\mathscr R(r,w)
 &=\lambda^{r+2}(1-\lambda^4)A(w),\\
(\mathsf T_2-\lambda^2)\mathscr R(r,w)
 &=\lambda^{3r+2}(1-\lambda^4)F(w).
\end{aligned}}
\tag{28}
$$
原已付的 $1-\lambda^2$、$1+\lambda^2$ 均为单位，故 $1-\lambda^4$ 为单位。
相乘即给真正的两模式递推。
这里 N、q 全固定；没有更换随 r 适配的测试。

对 E 深，R780 的完整三态表明确给出 $A$ 的 S/U/T 算术来源。
对 $B_0,B_1$，写得最短的是
$$
\begin{aligned}
A_{B_0,N}^{Y,+}&=0,\\
A_{B_1,N}^{Y,+}
 &=\frac{\lambda^{2N}}{c_B}
  \left(\langle2\rangle^{-d_pw}J_U(w)
                 +\frac{\delta\omega^2}{2}J_S(w)\right),\\
A_{B_i,N}^{W,+}
 &=\frac{\lambda^{2N}6\delta}{c_B}J_T(w),\\
A_{B_i,N}^{W,-}
 &=\frac{(\beta^N-\lambda^{2N})6\delta}{c_B}J_T(w),\qquad i=0,1.
\end{aligned}
\tag{29}
$$
原 $J_U(0)=0$ 才消去 $\log\langle2\rangle J_U(0)$ 项。
$B_1$ 的 E 浅 Y 行仍是 R780(16a) 的完整 $\Xi$、reference 与外谱，
不由三原中央消掉。

对 $B_0$，$\mathcal T_*B_0=\omega^2B_0$；
$Y,J,q$ 被 $\mathcal T$ 固定。因此
$$
F_{B_0,N}^{Y,+}=F_{B_0,N}^{Y,-}=0,\qquad
A_{B_0,N}^{Y,+}=A_{B_0,N}^{Y,-}=0 .
\tag{30}
$$
前两式由同一 J 深/浅域的 $\mathcal T$ 特征给出；
后两式分别由 R780 的深表和完整 Y 边际相减给出，
并未声称单个物理 E 门被 $\mathcal T$ 固定。
此外同一特征论证保留整个 (Y,P) 两输出：
$$
(Y,P)_*(1_{J\in p^N}qB_0)
=(Y,P)_*(1_{J\notin p^N}qB_0)=0.
\tag{30a}
$$
这才是在下一节同时含 $Z_0=P-b_YY$ 时消去所有不含 t 项的依据。
所以(27)的两个纯 Y 外部整函数确为零。
这不把下一节的混合 W 观察当作纯 Y 观察。

在 $J'_S=J'_T=J'_U=0$ 下，(27)给的是
$\mathscr R'(r,0)=-\lambda^{3r}F'(0)$，
只在(29)确有已付算术来源的行上这样使用。
未知的 $F'(0)$ 没有因此被消掉。

## 8. 原混合 T 外部：同一个有限联合上的完整 Cauchy 行

原 Y 返回中的 T 观察是
$$
W^{[-r]}=W\circ P_{Y,\kappa^{-r}}
=b_Y\kappa^{-r}Y+Z,\qquad Z=Z_0-at .
\tag{31}
$$
对偶 r 不另加一层反射；unit 条件始终是这一整观察的 unit。
因 $E,q$ 被 Y 缩放固定，
$$
\int_{E^\epsilon,\ Y\in p^r}f_w(W^{[-r]})\,d\rho_\mu
=\lambda^r A_{\mu,N}^{W,\epsilon}(w).
\tag{32}
$$
在其 $\mathscr V_r$ 子域，(31)返回成 $b_YY+\kappa^rZ$。
定义同一个固定联合上的真实行
$$
\mathcal D_{\mu,N}^{\epsilon}(z,w)
=\int f_w(b_YY+zZ)\,d\mathfrak F_{\mu,N}^{\epsilon}.
\tag{33}
$$
则完整混合外部
$$
\mathscr R_{\mu,N}^{Y;W,\epsilon}(r,w)
=\int_{\substack{E^\epsilon,\ Y\in p^r\\\mathscr V_r^c}}
 f_w(W^{[-r]})\,d\rho_\mu
$$
满足
$$
\boxed{
\mathscr R_{\mu,N}^{Y;W,\epsilon}(r,w)
=\lambda^r A_{\mu,N}^{W,\epsilon}(w)
 -\lambda^{3r}\mathcal D_{\mu,N}^{\epsilon}(\kappa^r,w).}
\tag{34}
$$
这里不能将 $\mathcal D(\kappa^r,w)$ 换成纯 $F^W(w)$，
也不能把(28)的两根过滤器直接用于(34)。

当 $z\in p\mathcal O$，所有坐标整，
$$
b_YY+zZ\ {\rm unit}\iff Y\ {\rm unit}.
\tag{35}
$$
故(33)在同一个 unit cut 上是有界解析 Cauchy 行：
$$
\begin{aligned}
\mathcal D_{\mu,N}^{\epsilon}(z,w)
=\int_{Y\ {\rm unit}}
 \langle b_YY\rangle^{d_pw}
 \exp\!\left(d_pw\log\left(1+\frac{zZ}{b_YY}\right)\right)
 d\mathfrak F_{\mu,N}^{\epsilon}.
\end{aligned}
\tag{36}
$$
其质量准确为 $F_{\mu,N}^{Y,\epsilon}(0)$，不随 z 变；
在一般态上保留
$d_p\log\langle b_Y\rangle F_{\mu,N}^{Y,\epsilon}(0)$。

对 $B_0$，由(30a)所有不含 t 的项整条消去。
因此
$$
\boxed{
\begin{aligned}
\partial_w\mathcal D_{B_0,N}^{\epsilon}(z,0)
={}&d_p\sum_{m\ge1}\frac{(-1)^{m+1}z^m}{m b_Y^m}\\
&\cdot\sum_{\substack{1\le k\le m\\k\equiv1\ (3)}}
 {m\choose k}(-a)^k
 \int_{Y\ {\rm unit}}Y^{-m}Z_0^{m-k}t^k
                      d\mathfrak F_{B_0,N}^{\epsilon}.
\end{aligned}}
\tag{37}
$$
条件 $k\equiv1\bmod3$ 由整个 $\mathcal T$ 特征和同一 J 深/浅域得到，
没有把每个单门强行平均。
式(37)保全部高负幂，不用一个负一矩代替完整对数。

令
$$
M_N^\epsilon=\int_{Y\ {\rm unit}}\frac tY\,
                        d\mathfrak F_{B_0,N}^{\epsilon}.
$$
则对 r≥1，
$$
\boxed{
\partial_w\mathcal D_{B_0,N}^{\epsilon}(\kappa^r,0)
=-\frac{d_pa}{b_Y}\kappa^r M_N^\epsilon+p^{2r}\mathcal O .}
\tag{38}
$$
这只使用实际整有界来源及 $mr-v_p(m)\ge2r$（m≥2，当前 p 范围），
未对无限级数施加点惯性投影。

深支的系数由(21)准确读取：
$$
M_N^+=\lambda^N\beta^N\,
 \Omega\int_{Y\ {\rm unit}}Y^{-1}d\mathcal L_N^J .
\tag{39}
$$
另一方面，深浅之和是原未加 J 条件的同一行。
R767 的完整原身份遂给
$$
\boxed{
M_N^++M_N^-
=-\frac{22}{21}\beta^N\Omega I_{\omega,-1}\ne0 .}
\tag{40}
$$
这里 $I_{\omega,-1}$ 是原 $D_{\omega,b}$ 的负一单位矩，
非零由 R735 支付。于是至少一个真实 E 深/浅共同平面返回的
第一系数非零；这一结论不要求先给(39)单独判号。
两支的高尾和全部外部仍按(34)保留。

例如在 $J'_T(0)=0$ 下，准确得到
$$
(\mathscr R^{Y;W,\epsilon})'(r,0)
=-\lambda^{3r}\partial_w\mathcal D^\epsilon(\kappa^r,0).
\tag{41}
$$
它是完整外部必须承担的值，不能被改读成
$\partial_w\mathcal D^\epsilon(\kappa^r,0)=0$。

## 9. 原帽、U 失败与 R783 补域：第四输出必须保

R783 已付
$$
\begin{aligned}
\hat s&=\frac7{36}J-\frac{17+24\omega}{72}Z_0,\\
\hat d&=-\frac{7a}{72}J+\frac{17+3\omega}{144}Z_0,\\
U&=u_JJ+u_ZZ_0,\qquad
u_J=\frac{7(4+9\omega)}{72},\quad
u_Z=-\frac{68+33\omega}{144}.
\end{aligned}
\tag{42}
$$
原帽为
$$
\mathcal H_N=\{Y\ {\rm unit},\ J,Z_0\in p^N,\
                                      U\notin p^{N+300}\}.
$$
只返回 J 时，(18)给其全部事件为
$$
\boxed{
Y\ {\rm unit},\quad Z_0\in p^N,\quad
u_JuJ+u_ZZ_0\notin p^{N+300}.}
\tag{43}
$$
物理 E 同时变为 $E_{\mathcal V}+e_JuJ$。
若再按 R785 返回 Z0 深 N，则(43)的失败准确成为
$u_JJ+u_ZZ_0\notin p^{300}$，观察 $P$ 变为 $b_YY+uZ_0$；
它与 R773 的整个帽/U 返回一致。原 U 第300层扣除不能省去。

因此(19)的三输出足以处理(25)—(41)，但不足以单独处理(43)的失败门；
后者使用(18)的四输出或 R773 的真实二项式。
对 R783 的 P 收缩帽像，仍必须保其 $P_\ell=P/\kappa^\ell$、
$Z_\ell=\vartheta P_\ell-b_YR$ 和
$u_JJ+u_ZZ_\ell\notin p^{N+300}$。
不能把它免费换成(43)，也不能从(30)删去其 W 观察。

同样，R780/R784 的三个物理 E 相对行仍使用
$E_j=E_\perp+h_0\omega^{2j}t$。
在原帽上 $E_j$ 深 N 恰对应 t 深 N；
在 R783 的 P 收缩像上，它们是 t-unit 内三条不同 affine disc。
它们全可在(18)的实际四输出中书写，却不能仅由(19)总质量恢复。
随 CM 分支变化的逆 Y 观察也仍按 R784 保持，未替换为固定 $t/P$。

## 10. 本篇提供的有限关系与剩余中央门

本篇把 R785(27) 的右端真正落实成(17)—(22)：
同 q、全部三态、原六支和 unit 第二项均付清。
原物理 E 深与浅共同平面返回，已经在同一对有限来源
$\mathfrak F_{\mu,N}^{+},\mathfrak F_{\mu,N}^{-}$ 上。

纯 Y/W 外部由(27)—(28)完全控制，含完整 Mellin 质量。
原混合 T 外部的剩余不是任意新测度，而是明确的有门线性算子
$$
\boxed{
\mathfrak F\longmapsto
\int_{Y\ {\rm unit}}
 \log\left(1+\frac{z(Z_0-at)}{b_YY}\right)d\mathfrak F ,
\qquad z=\kappa^r,}
\tag{44}
$$
加上(36)已列的原主 Mellin 项和质量。
对 B0，主项整条为零，(44)的第一系数就是(39)—(40)。
对 B1 及第三中央，主项、$\Xi$ 和 reference 按(29)、R780(16a)保留。

固定 p,N 的来源 carrier 是有限的；这不意味着(44)中全部
$z$ 级数可逐项作 point-only 投影或截去高负幂。
R739/R749/R753 的有限系数范围继续适用。
原中央为零仍只给(41)及其全部补域的完整相消，
还没有给一个独立关系把同一 $\mathfrak F$ 上的(44)置零。
这正是下一步须在原同域词或原第三来源中支付的剩余算子。

本篇未添加射线、未更换测试、未执行新数值任务。
§5.1只读取已公开 R773 的原第一项；其运行参数、producer与输出
SHA256均见该篇增补A.1。可重算输出未另存仓库或Release。

依赖：[R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)；
R735（原两条型五 Schwartz 与共同周期负一身份）；
[R767](R767-native-t-moment-and-complete-five-partner-boundary.md)；
[R773](R773-native-common-hat-domain-and-five-conditional-moment-return.md)；
[R777](R777-original-b-sector-p-t-core-and-complete-central-renewal.md)；
[R780](R780-original-third-central-b-state-and-true-w-deep-return.md)；
[R783](R783-native-hat-images-and-nonzero-cd-exterior-central-row.md)；
[R785](R785-original-three-state-even-frames-and-exact-e-gate.md)。
