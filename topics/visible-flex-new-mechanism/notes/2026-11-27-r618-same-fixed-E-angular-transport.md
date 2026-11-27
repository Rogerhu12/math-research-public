# R618：同一个固定 E 的均值、连接与实际位置角误差传递

日期：2026-11-27；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

本文补足新的固定E响应与[R615](../results/R615-position-fourier-majorants-and-discrete-primitive-error.md)
之间的实际数学接口。下列定理在列出的真实输入包围下证明；当前实际397的原M/ODE、
角求积、径向覆盖与舍入还没有全部支付，不能把本定理直接登记成当前场的证书。
本稿没有启动科学计算或改变任何已发布scope。

与旧R615观察器的关键区别是：**目标一直是那一个冻结参考高度的连续$E_*(r)$。**
只包围其数值评价误差，并在这个同一目标下修正实际均值$p_0$；
不通过修改E把当前响应的turning根重新闭合。
旧R615的原函数alias、有限矩阵范数和奇频尾引理直接复用，不重证它们。

## 1. 一个三角系统，两个真实标量约束

先固定一个正文内点$r>0$；最终连续径向证书须使本节全部界在同一径向cell一致成立。
固定完整实际角高度$f$及其二阶空间jets，它保持原canonical512定义，
不随本节数值误差比较更换角减均值。假设这些函数对角解析、对r至少C2；
目标$E_*$为已经完整冻结的C1函数。

沿用固定参考背景$W>0,W_r$，写

$$
e=E-W^2,\quad e_r=E_r-2WW_r,\quad
p_0=-W+\gamma x,\quad s_r=\beta z,\quad p_0'=-W_r+\beta z,            \tag{1}
$$

其中本节在固定r比较时$\gamma,\beta>0$是固定尺度，不把它们当独立误差变量。
数值均值chart取$\gamma=W$（$\lambda$）或$\gamma=1/W$（$\zeta$）；
暂取任意正$\beta$，第6节给内帽完全归一的选择。

记

$$
q=f_\theta,\quad t=f_{\theta\theta},\quad d=\gamma x+f_r,
\quad p=-W+d,\quad b^2=r^2-q^2,\quad u^2=E-r^2p^2/b^2,
$$
$$
N=r/b+r^2pt/b^3,\quad C=Et+rp,\quad B=f_{r\theta}-q/r,
\quad M=r+pt-q^2/r,\quad\omega=r^2/(u^3b^3),
$$
$$
K=(e+Wd)t+rd-Wq^2/r,
\qquad
D=C(\beta z+f_{rr})-EB^2-W_rK-e_rM/2,
\quad\mathcal R=\omega D.                                      \tag{2}
$$

这就是现有稳定chain的准确分拆，不将两个大的核心平方相减恢复有限余项。
把(2)展开也有$D=C(p_0'+f_{rr})-EB^2-E_rM/2$，但数值消费继续用分拆式。

取正的turning残差尺度$\nu$：$\lambda$时$\nu=W^2$，$\zeta$时$\nu=1$。
真正的两个连续约束是

$$
F(E,x):=\frac{\langle N/u\rangle-1}{\nu}=0,
\qquad
G(E,e_r,x,z):=\langle\mathcal R\rangle=0.                     \tag{3}
$$

第二式对z准确仿射，且

$$
F_x=\gamma c_0/\nu,\quad F_E=-\langle N/u^3\rangle/(2\nu),
\quad G_z=\beta c_0,\qquad c_0=\langle\omega C\rangle.         \tag{4}
$$

在同一连续正分支$c_0\ne0$上，先解F，再解G。
因为$e_r$是这个同一$E_*$的真实导数分拆，R587/R618已证G给出的$p_0'$
正是第一式隐式根的径向导数；它不是独立拟合出来的第二个参数。
这一步需要C1目标及同一分支，不能用一张独立$E_r$节点表替代。

## 2. 固定目标误差先进入同根均值，再进入连接

设实际有限mean规则为$T_{N_m}$，已计算的数值标量为
$\widehat E,\widehat e_r,\widehat x,\widehat z$。
另已有对那一个冻结目标的真实误差包围

$$
|E_* -\widehat E|\le d_E,\qquad
|e_{*,r}-\widehat e_r|\le d_r.                              \tag{5}
$$

这些输入可接已有
`2026-11-27-r618-fixed-target-evaluation-and-zero-entry.md` §2的同根导数预算；
旧有限M/ODE及源误差仍须装入真实包围，不能因有角预算便默认0。

在声明的整个实参数盒上，假设$b,u,N>0$，$c_0$符号固定，并已有

$$
|F_x|\ge m_T>0,\qquad |\beta c_0|\ge m_C>0,
\qquad |F_E|\le L_{T,E}.                                  \tag{6}
$$

这些是整个盒的界，不能只在数值根中心观察到$c_0$非零。
在数值中心准确函数
$H(\theta)=(N/u-1)/\nu$及$\widehat{\mathcal R}(\theta)$上设有Wiener界
$H_\rho,\widehat R_\rho$。有限规则、实际点值和算术误差给

$$
\begin{aligned}
\epsilon_T&=|\widehat F_{N_m}|+\epsilon_{T,\rm eval}
                       +e^{-N_m\rho}H_\rho,\\
\epsilon_G&=|\widehat G_{N_m}|+\epsilon_{G,\rm eval}
                       +e^{-N_m\rho}\widehat R_\rho.
\end{aligned}                                               \tag{7}
$$

这里$\widehat F_{N_m}$是同一有理化残差的实际有限值，不通过两个单位量相减重造；
$\widehat G_{N_m}$可从同场完整$\mathcal R$的有限平均读取。
两个$\epsilon_{\cdot,\rm eval}$都须支付真实样值、系数及浮点运算误差。
若其未付，(7)就只是条件输入，不能用“数值均值约等于0”将它们置零。
平均alias界直接复用R606；常数模抵消不改变它。

在$z=\widehat z$切片及整个$(E,e_r,x)$盒上，给定

$$
|G_E|\le L_{G,E},\qquad |G_{e_r}|\le L_{G,r},
\qquad |G_x|\le L_{G,x}.                                  \tag{8}
$$

则同一连续分支上的真实根满足

$$
\boxed{d_x:=\frac{\epsilon_T+L_{T,E}d_E}{m_T},
\qquad |x_*-\widehat x|\le d_x,}                           \tag{9}
$$
$$
\boxed{d_z:=\frac{\epsilon_G+L_{G,E}d_E+L_{G,r}d_r+L_{G,x}d_x}{m_C},
\qquad |z_*-\widehat z|\le d_z.}                           \tag{10}
$$

**存在与量词。** 若$[\widehat x-d_x,\widehat x+d_x]$严格落在已声明正域/同符号盒内，
则均值定理使其两端F异号（相等情况可扩大为已声明严格内盒），从而得到唯一根。
第一式已有该根时，同一均值定理也直接给(9)。G对z仿射，斜率由(6)离0，
所以它在该真实$(E_*,e_{*,r},x_*)$处有唯一z，并由(7)(8)给(10)。
用于后面全盒范数的z区间必须真的包含$\widehat z\pm d_z$；
如果未包含，扩大声明盒并重新支付该盒界，不能沿用原中心常数。

证明只用了同一个E的误差范围，没有调用以新响应重求可变E的reclosure。
$d_E$和$d_x$分别保留是必要的：前者改变u和归一度量，后者改变p、N及相位。
这里的唯一根仅指两个标量均值约束。它们不强制完整角函数$D(\theta)$为0，
不证明这个固定E容纳所选非圆τ1 core trace，也不证明随角带增长存在一致逆。
这些仍是R618列出的完整非线性求解与极限问题；后面的误差上界可能远大于目标。

## 3. 全部离解微分：保留独立连接量，避免少付一项

把$E,e_r,x,z$暂作四个独立实参数，仅用于在真实盒内比较两个辅助位置。
对一个方向$(\dot E,\dot e_r,\dot x,\dot z)$，完整微分为

$$
\dot p=\gamma\dot x,\quad
\dot u=\frac{\dot E}{2u}-\frac{r^2p\gamma\dot x}{ub^2},
\quad\dot N=\frac{r^2t\gamma\dot x}{b^3},
\quad\dot\omega=-3\omega\dot u/u,
$$
$$
\dot C=t\dot E+r\gamma\dot x,\quad
\dot M=t\gamma\dot x,\quad
\dot K=t\dot E+(Wt+r)\gamma\dot x,
$$
$$
\boxed{\dot D=\dot C(\beta z+f_{rr})+C\beta\dot z
 -B^2\dot E-W_r\dot K-M\dot e_r/2-e_r\dot M/2,
\quad \dot{\mathcal R}=\dot\omega D+\omega\dot D.}           \tag{11}
$$

没有使用$D=0$、$F=0$或$G=0$删除离解项。特别是$\dot\omega D$、
$C\beta\dot z$和$M\dot e_r/2$都存在。
按四个坐标取单位方向，(11)立即给可消费的导数表：

| 方向i | $u_i$ | $N_i$ | $D_i$ |
|---|---|---|---|
| $E$ | $1/(2u)$ | $0$ | $t(\beta z+f_{rr}-W_r)-B^2$ |
| $e_r$ | $0$ | $0$ | $-M/2$ |
| $x$ | $-r^2p\gamma/(ub^2)$ | $r^2t\gamma/b^3$ | $\gamma\{r(\beta z+f_{rr})-W_r(Wt+r)-e_rt/2\}$ |
| $z$ | $0$ | $0$ | $\beta C$ |

令$a=N/u$，于是

$$
a_i=N_i/u-Nu_i/u^2,\qquad
\mathcal R_i=-3\omega(u_i/u)D+\omega D_i.                 \tag{12}
$$

由平均范数不超过Wiener范数，(8)可直接取
$L_{G,i}\le\sup_{\mathcal B,z=\widehat z}\|\mathcal R_i\|_\rho$。
所有表项都是完整已有系数、乘积与正分母函数，能在同一R606式范数组装中包围；
不需要另跑一个旧科学探针。若保守包络失败，只表示该包络不够强。

## 4. 两次primitive保留在同一固定E位置的误差中

在全参数盒上定义辅助对象

$$
\phi=\Pi(a-1),\quad T=e^{i(\theta+\pi/2+\phi)},
\quad Q=i b(\Pi\mathcal R)T,\quad \mathcal S=\Pi Q/\sqrt E.   \tag{13}
$$

离开连续约束时，它只是比较用的辅助函数，不声称对应另一张等距面。
在真实$(E_*,e_{*,r},x_*,z_*)$处，R587/R613/R618的同根链给
它就是实际归一位置缺陷。这里p0与p0′来自同一隐式根，正是第1节的两约束。

假设整个盒已包住

$$
E\ge E_->0,\quad
\|b\|_\rho\le B_\rho,\quad\|a\|_\rho\le A_\rho,
\quad\|\mathcal R\|_\rho\le R_\rho,
$$
$$
\|a_i\|_\rho\le A_i,\quad\|\mathcal R_i\|_\rho\le R_i,
\qquad
T_\rho=e^{\rho+A_\rho/2},\quad
Q_\rho=B_\rho T_\rho R_\rho/2,\quad S_\rho=Q_\rho/\sqrt{E_-}. \tag{14}
$$

角高度的原偶/π周期对称性使a、R为偶频，T、Q、S为奇频。
复用R615：内层$\Pi$在偶频上范数至多$1/2$，外层奇频上至多1。
对(13)准确微分，得到

$$
Q_i=i bT\{\Pi\mathcal R_i+i(\Pi\mathcal R)(\Pi a_i)\},
\qquad
\mathcal S_i=\Pi Q_i/\sqrt E-\mathbf1_{i=E}\mathcal S/(2E).
$$

所以可取完整、明确的Lipschitz常数

$$
\boxed{L_{S,i}=
\frac{B_\rho T_\rho}{2\sqrt{E_-}}
   \left(R_i+\frac{R_\rho A_i}{2}\right)
 +\mathbf1_{i=E}\frac{S_\rho}{2E_-}.}                      \tag{15}
$$

特别是z方向$a_z=0$，$R_z=\beta\|\omega C\|_\rho$即可；
参考度量归一的$S/(2E)$项只在E方向出现，不能漏掉。
沿连接数值中心与真实根的实线段积分，整个盒包含该线段时，

$$
\boxed{\|\mathcal S_* -\widehat{\mathcal S}\|_\rho
\le d_S:=L_{S,E}d_E+L_{S,e_r}d_r+L_{S,x}d_x+L_{S,z}d_z.}    \tag{16}
$$

这完整传递了参考E、同根导数、implicit mean和connection的误差，
没有把旧R615的可变E根位移常数直接移植到新问题。

## 5. 同一个有限重构的奇频读数怎样成为连续metric界

固定数值中心的四个标量，只将它们看作准确实常数。
令$N_o$为实际输出角网，$4\mid N_o$，$\Pi_{N_o}$仍是原常数/Nyquist置零矩阵。
同场finite S由准确采样的$\widehat a,\widehat b,\widehat{\mathcal R}$
按两次原finite primitive形成。函数求值/矩阵及算术误差另在系数误差$e_{k,x},e_{k,y}$中支付。

这里连接量$\widehat z$已作为中心的一部分固定，不再在本节换一次加权均值。
因此原R615(13)(14)(17)给

$$
P_{\sigma,N_o}(F)=\left(\frac1\sigma+\frac2{N_o}\right)e^{-N_o\rho/2}F,
\quad K_{N_o}=\pi/\sqrt3,
$$
$$
\epsilon_\phi=P_{2,N_o}(A_\rho),\qquad
\epsilon_p=P_{2,N_o}(R_\rho),
$$
$$
\boxed{\epsilon_S=
\frac{P_{1,N_o}(Q_\rho)+K_{N_o}r
 [\epsilon_p+(R_\rho/2)\epsilon_\phi]}{\sqrt{E_-}}.}        \tag{17}
$$

与旧R615中$\epsilon_\mu$相关的一项由(7)(10)(16)中真实connection误差承担，
不是把该误差删除。$N_m$与$N_o$可以不同：前者用于同一mean泛函的数值评价，
后者用于实际位置primitive；两条alias账各自保留，不能把输出mean默认为0。
即使有限中心的$\langle\widehat a\rangle\ne1$，(13)(17)依然是辅助函数比较；
只有校正到真实F=0后才用于实际metric身份。

取正奇数$K<N_o/2$，实际同一finite S奇频读数为
$\widehat c_k,\widehat s_k$，并且相对于准确finite代数对象的系数误差已包为
$e_{k,x},e_{k,y}$。同R615的奇频系数与尾引理，令

$$
\beta_k=2\epsilon_S+S_\rho e^{-(N_o-k)\rho}+d_S e^{-k\rho},
$$
$$
\boxed{\Delta_S=
\sum_{k=1,3,\ldots,K}
\left[\max\{|\widehat c_k|+e_{k,x},|\widehat s_k|+e_{k,y}\}+\beta_k\right]
 +S_\rho e^{-(K+2)\rho}.}                                  \tag{18}
$$

每个奇频的真实复向量振幅仍是$\max(|c_k|,|s_k|)$，不多付无根据的平方根因子。
于是对同一固定目标下的真实重构位置，

$$
\boxed{\|\mathcal S_*\|_\infty\le\Delta_S,
\qquad \eta_{\rm actual}\le(1+\sqrt2)\Delta_S+\Delta_S^2.}  \tag{19}
$$

证明依次是两次primitive误差、实际Fourier alias、(16)同根传递与完整未保留奇频尾。
这里只复用已证明的R615引理及R613实际metric身份，没有以目标下降替代任何误差项。

## 6. 真内帽不能把一个绝对E浮点误差除以W²

当$W\le1$时，采用已经实际实现的$\gamma=W$，并取

$$
y=(e-1)/W^2,\qquad \xi=e_r/W^2,\qquad x=\lambda,
\qquad\beta=W,\quad z=s_r/W.                              \tag{20}
$$

此处应直接包围准确函数y、ξ的求值误差，而不是把`E`附近的一个绝对ulp
当作$W^2$量级误差。二者在真帽附近相差任意大倍数。
设$v=x+f_r/W$，则准确有

$$
\bar n=\frac{(q/W)^2}{b(r+b)}+
        \frac{r^2(v-1)(t/W)}{b^3},\qquad
\bar u=y+2v-v^2-(v-1)^2q^2/b^2,
$$
$$
N=1+W^2\bar n,\quad u^2=1+W^2\bar u,
\quad
\boxed{H=\frac{N/u-1}{W^2}
 =\frac{2\bar n+W^2\bar n^2-\bar u}{u(N+u)}.}             \tag{21}
$$

所以(7)的$H_\rho$可从右侧直接组装，不需把一个单位量的范数除以$W^2$。
同时令

$$
\bar C=C/W=E(t/W)+r(v-1),\quad
\bar B=B/W=f_{r\theta}/W-q/(rW),
$$
$$
\bar K=K/W=(e+W^2v)(t/W)+rv-q^2/r,
$$
$$
\boxed{\bar D=D/W^2
 =\bar C(z+f_{rr}/W)-E\bar B^2-(W_r/W)\bar K-\xi M/2.}    \tag{22}
$$

用$\bar G=\langle\omega\bar D\rangle$取代未归一G，两个标量导数变为

$$
F_x=\langle\omega\bar C\rangle,
\quad F_y=-\tfrac12\langle N/u^3\rangle,
\quad \bar G_z=\langle\omega\bar C\rangle.                \tag{23}
$$

真实内尾非退化量于是是$c_0/W$，不要求渐近为0的$c_0$拥有跨帽常数下界。
(9)(10)逐字适用于变量$(y,\xi,x,z)$及(21)(22)的归一残差，
实际位置中仍使用真实$\mathcal R=W^2\omega\bar D$及同一E。
位置导数常数应直接在(20)(22)中先代入
$\dot E=W^2\dot y,\dot e_r=W^2\dot\xi$后组装；
不先形成数值溢出的$1/W^2$常数，再企图乘回$W^2$消掉。

参考导数也可使用同一个稳定分拆：若参考$x=0$，将原
$A_t=Cf_{rr}-EB^2-W_rK$写作

$$
\bar A_t=A_t/W^2
=\bar C(f_{rr}/W)-E\bar B^2-(W_r/W)\bar K,
\qquad
\xi_*=
2\frac{\langle\omega\bar A_t\rangle}{\langle N/u^3\rangle}. \tag{24}
$$

这仍是同一参考turning根的真实导数公式，不能重新选一份ξ函数。
其weighted mean alias和根位移可按已有固定target §2的通分/商微分证明支付，
只是将整个真实归一表达式先写出后消费，不重证旧基本估计。
完整原germ及新增Gaussian尾在帽至数值口上的真实性与误差还由已发表真尾证明承担，
一张内点网或binary64下溢到0不替代该区间。

## 7. 当前能消费什么，以及未支付的量词

新固定E scope已将完整同场的D/V/L/奇频、mean/Nyquist/角闭合与双实际位置
列入同一必要末态读出，能够共享同一套系数与标量receipt；
本稿不要求独立重跑旧R606门。
若新scope在入口失败，只能使用其真实已完成覆盖，不能补造末态数组消费本定理。

实际使用(19)必须绑定同一个目标、response、完整系数、r区间和mean/output规则，
并确实支付(5)至(8)、(11)至(14)及全部系数误差；未付项目应保持未解决。
当前canonical512是高度定义的一部分，连续mean只是评价同一函数，不能换成新的高度定义。
本文只给角向及同根传递；连续径向/核心/帽的覆盖、全部时间与reach还需各自完整证明。
它没有把有限角带静态根、条件观察或小幅固定E候选称作README完成。
