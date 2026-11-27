# R1030 — 实际三次角域、完整五点规范化与三倍来源格

日期：2026-11-27 UTC。**已证明。** 原两条 degree390、rank 至少二
的完整来源，经实际 $[\delta]^{-1}$ 缩放后，成为 charge65 的固定来源。
它们生成原角函数域的真实三次扩张。本文支付全部公共除子、
全部195个剩余权、秩36270的固定自由整基，以及一个显式同来源导子。

新每权 Hilbert 主项是 $62m/65$，累积主项是 $31M^2/65$；
其三倍改善来自已经证明的函数域扩张，不是把任意角函数加进原格。
整个原六位评价与来源范数也一并保留。生成元中央零仍不传播到任意乘积。

## 1. 原固定缩放与整个角式

保持原
$$
E:y^2=x^3+1,\quad X=x^3,\quad
t=-X^{-1},\quad \Theta=x\sigma^2,\quad
\delta^2=-3.
$$
本篇 $z$ 始终是同一个原微分参数。令
$$
u=t(z/\delta),\qquad
\widehat\Theta=\Theta(z/\delta)^3.
$$
原完整除法恒等
$$
\sigma(\delta z)=\delta\sigma(z)^3x(z),\qquad
x(\delta z)=-\frac{X+4}{3x^2}
$$
逐式给
$$
\boxed{
t=-\frac{27u}{(1-4u)^3}=:\tau(u),\qquad
\Theta=(1-4u)\widehat\Theta.
}
\tag{1}
$$
物理原点的分支准确为
$u=-t/27+O(t^2)=w/27+O(w^2)$，
$\widehat\Theta(0)=1$，其中 $w=z^6$。
不能在三次方程的其它分支上另选一个原点。

对原任一完整角来源 $F=\Theta^d f(t)$，若
$3\deg f\le d$，有整个多项式身份
$$
\boxed{
F=\widehat\Theta^d P_F(u),\qquad
P_F(u)=(1-4u)^d f\!\left(-\frac{27u}{(1-4u)^3}\right).
}
\tag{2}
$$
这里每个原项都保留；没有只对一个前缀作变量代换。
若 $\operatorname{ord}_0 f=r$，则
$$
\deg P_F=d-2r.
\tag{3}
$$
式 (3) 来自 $u=\infty$ 处 $\tau(u)=27/(64u^2)+O(u^{-3})$，
其最高系数由原非零 $t^r$ 系数确定。

取 R981/R982 的两条完整归一来源
$$
\Psi_{35}=\Theta^{195}f_{35}(t),\qquad
\Psi_{53}=\Theta^{195}f_{53}(t).
$$
它们的全部来源系数、原有限角色、rank 与全 Selmer 桥均沿原文；
本篇不重新从两个好位谱猜身份。定义两个新的实际整函数
$$
\widehat\Psi_i(z)=\delta^6\Psi_i(z/\delta),\qquad i=35,53.
$$
于是
$$
\boxed{
\widehat\Psi_i=-27\,\widehat\Theta^{65}f_i(u),\qquad
\widehat\Psi_i=w+O(w^2).
}
\tag{4}
$$
R982 已付的完整事实为
$$
\deg f_i=64,\qquad
\operatorname{ord}_0 f_i=\operatorname{ord}_1 f_i=1,
$$
以及固定分母 $245$、$5845$。式 (4) 使用整个原多项式。

## 2. 两种原中央、同 charge 与所有原范数

### 2.1 惰性处是真正的特征零同 charge

令 $p=6s-1>13^4$，$d_p=p+1$，
$c=[z^{d_p}]\log(\sigma/z)$，
$q_\delta=\delta^{d_p}/3\in1+p\mathcal O$。
由原整数插值及完整 Tate 收敛，准确有
$$
\boxed{
J_{130,\widehat\Psi_i}(v)
=\delta^6q_\delta^{-v}J_{390,\Psi_i}(v).
}
\tag{5}
$$
质量为零，所以
$$
j_{130,\widehat\Psi_i}=\delta^6j_{390,\Psi_i}.
\tag{6}
$$
这是完整中央函数的身份，不是只用模 $p$ 的
$\delta^{p+1}=3$。

Gaussian 整性也由同一个原来源支付：
$$
e^{-130cz^{d_p}}\widehat\Psi_i(z)
=\delta^6
 \exp\!\bigl(130c(q_\delta^{-1}-1)z^{d_p}\bigr)
 G_{390,\Psi_i}(z/\delta).
\tag{7}
$$
指数系数整、$\delta$ 是当前单位，
故 R602/R614 的 Hurwitz 界、完整整窗及 R989 的七八端点逐项继承。
在 $w^{-1}$ 的首阶归一后，
$$
\widehat B_i(w)
=B_i(w/\delta^6)
 \exp\!\bigl(130c(q_\delta^{-1}-1)w^s\bigr).
\tag{8}
$$
因此 $\Phi_*,\Phi_{260},\widehat\Psi_{35},\widehat\Psi_{53}$
四条真实 canonical 来源的 charge 都是65，
其五高轴扰动准确为同一个 $e^{(65/17)\eta_x}$。

它们不因此落入原22维空间：
(4) 在三次角域中，等价的 $T_S^{130}G$ 表示保留
$130S=S$ 的非平凡三挠线束与全部原 Miller 相位。
(1)、(4)、(7) 已经指定这一个完整来源。

### 2.2 普通处保持同一个单位切域

在原普通 CM 嵌入下，$[\delta]$ 是 formal group 的整单位自同构。
准确的测度关系是
$$
\nu_{\widehat\Psi_i}
=\delta^6[\delta^{-1}]_*\nu_{\Psi_i}.
$$
它保持原单位域。对 R968 的权 $(p-1)v$，
$$
\mathcal L_p^{\rm ord}(\widehat\Psi_i;v)
=\delta^6\langle\delta^{-1}\rangle^{(p-1)v}
 \mathcal L_p^{\rm ord}(\Psi_i;v).
\tag{9}
$$
原 rank 至少二的中央值为零，故中央首导数的零在 (9) 两边等价。
没有改成独立切各个伴随域的新测度。

### 2.3 同来源范数没有遗漏缩放成本

实处 $\widehat\Psi_i$ 是固定整函数，
其原 theta 二次增长由 $390/|\delta|^2=130$ 给出。
在好有限处，$\delta$ 是单位，原整圆盘及
$\|\Psi_i\|_r\le r^6$ 保持。
在固定坏位3，$z/\delta$ 的固定缩放只增加
$O(k+M+1)$ 的前缀费用。
所以 R957/R960 的同一真实整数像格及商范数证明适用于这些实际来源。
本篇没有为新有理角基另选一个廉价整数格。

## 3. 三次角域的真实生成：完整 trace 而非次数猜测

旧 $A^{(8)}$ 取 R996 的八来源环，其函数域已严格是
$\mathbf Q(\Theta,t)$。令
$$
F_i(u)=\frac{f_i(u)}{(1-4u)^{65}}.
$$
则 $\widehat\Psi_i=-27\Theta^{65}F_i(u)$。

R982 的完整 $\delta$-trace 为零准确给
$$
\boxed{\operatorname{Tr}_{\mathbf Q(u)/\mathbf Q(t)}F_i(u)=0.}
\tag{10}
$$
为核这不是一个新自由 trace，写 $P=z/\delta,Q=z$。
若 $\Psi_i(P)=\sigma(P)^{390}R_i(P)$，
原 theta trace 的有理部分是
$$
\delta^{-130}\operatorname{Tr}_{[\delta]}
 \left(\frac{R_i(P)}{x(P)^{130}}\right).
$$
再除去目标 $x(Q)^{65}$，并代入
$x(Q)=-(X(P)+4)/(3x(P)^2)$，
整个被迹项正好变为 $F_i(u)$。
这保留原 raw pull、sigma 及目标微分的绝对尺度；
零值与是否取平均无关。

有理映射 $\tau$ 的次数为三。
$F_i$ 非零；若它属于 $\mathbf Q(t)$，
(10) 会变成 $3F_i=0$。因此它不属于原角域。
三是素数度，故
$$
\boxed{
\mathbf Q(\Theta,t)(\widehat\Psi_i)
=\mathbf Q(\Theta,u)
=\mathbf Q(\widehat\Theta,u).
}
\tag{11}
$$
任意一个新来源已经生成全部三次扩张。

在每个原允许的 $p>3$，(1) 仍为次数三的可分映射。
$F_i$ 的原首项保证其约化非零，(10) 的整身份保持，
所以同一个证明给剩余函数域中的真实三次生成。
这会在第7节用于导子的 $p$-饱和；
没有将特征零独立性直接外推到所有剩余域。

## 4. 全部三支、真实新零点与完整公共除子

原映射的完整特殊纤维为

| source $u$ | target $t$ | 分歧指数 |
|---|---:|---:|
| $0$ | $0$ | 1 |
| $\infty$ | $0$ | 2 |
| $1$ | $1$ | 1 |
| $-1/8$ | $1$ | 2 |
| $1/4$ | $\infty$ | 3 |

确实
$$
\tau'(u)=-\frac{27(1+8u)}{(1-4u)^4},\qquad
1-\tau(u)=\frac{(1-u)(1+8u)^2}{(1-4u)^3}.
\tag{12}
$$
其它纤维都按这个完整次数三的映射处理。

### 4.1 新两源在 $-1/8$ 的零

$F_i$ 在 $u=1,-1/8$ 正则。
在 $t=1$ 专门化 (10)，完整三支给
$$
F_i(1)+2F_i(-1/8)=0.
$$
由原 $f_i(1)=0$ 得
$$
\boxed{f_i(-1/8)=0.}
\tag{13}
$$
这里的重数二是真实分歧，不是删掉一个共轭分支。

### 4.2 新两源在 $1/4$ 的零

R1021 的已付完整 odd3 来源把每条 $\Psi_i$ 写成非零固定倍数的
$$
(T_S^{130}G_i-T_{-S}^{130}G_i)(\delta z),
\qquad S=(0,1),
$$
其中 $G_i$ 是完整十二个十三字之和，且为奇函数。
两译算子的原点指数因子相同。
因此 $\Psi_i(0)=0$ 准确给 $G_i(S)=0$，
奇性又给 $G_i(-S)=G_i(0)=0$。

若 $X(P)=-4$，原 $\delta$ 映射给 $\delta P=\pm S$。
上面两个译项分别在 $0,S,-S$ 或其格点平移处读取；
每一项都单独为零，全部准周期因子非零。
因此
$$
\boxed{f_i(1/4)=0.}
\tag{14}
$$
这使用完整原来源与相位，不从两个好位的本征值猜一个有限角色。

### 4.3 准确候选规范化

R996 的旧规范化是
$D_8=(64[\infty]-[0]-[1])/195$。
把 (1) 的整个 theta 因子和 (12) 的所有分歧带入，得到
$$
\boxed{
\widehat D=
\frac{193[\infty]-[0]-[1]-2[-1/8]-3[1/4]}{195},
\qquad \deg\widehat D=\frac{62}{65}.
}
\tag{15}
$$
令
$$
a_m=\lceil m/195\rceil,\quad
b_m=\lceil2m/195\rceil,\quad
c_m=\lceil3m/195\rceil,
$$
$$
Q_m(u)=u^{a_m}(u-1)^{a_m}(1+8u)^{b_m}(1-4u)^{c_m},
$$
$$
q_m=\left\lfloor\frac{193m}{195}\right\rfloor
-2a_m-b_m-c_m.
$$
对应完整分次环为
$$
\boxed{
\widehat B_m=
\widehat\Theta^m Q_m R[u]_{\le q_m},
\qquad
\widehat B=\bigoplus_{m\ge0}\widehat B_m.
}
\tag{16}
$$
$R$ 保原全部固定坏集，并包含 (4) 的固定来源分母及 $1/6$。
负上界表示零空间。
(16) 是实际 Gauss 赋值环的交，因而正规。

旧来源全部属于 (16)。
新 weight65 来源的完整要求恰为
$$
Q_{65}=u(u-1)(1+8u)(1-4u),\qquad q_{65}=60.
$$
R982、(13)、(14) 及 $\deg f_i=64$ 逐项证明其属于
$\widehat B_{65}$。
原 $\Phi_*,\Phi_{260}$、degree390 两源等已经属于旧 $B^{(8)}$
的附加列，沿 (2) 也继续属于 (16)。
以下环可把这些原完整列一并保留；
不会借它们的个数增加未经证明的深块。

## 5. 同权1365的原三参数支付全部有限整性

保持 R996 的三条实际来源参数
$\mathcal X_{42}^{65},\mathcal X_{70}^{39},Z^7$。
在旧共同因子 $\Theta^{1365}[t(t-1)]^7$ 后，
它们的三个完整括号记作 $H_j(t)$。
R996 已付：这些是 $\mathcal O_{\mathbf P^1}(434)$
的无共同零截面，且在全部原允许剩余域中仍成立。

置
$$
L=1365,\qquad M=1302=3\cdot434,\qquad
\widehat\rho_L=\widehat\Theta^L Q_L.
$$
其三个原参数在 (16) 中准确成为
$$
\boxed{
\widehat\rho_L\,\widehat H_j(u),\qquad
\widehat H_j(u)=(-27)^7(1-4u)^{1302}H_j(\tau(u)).
}
\tag{17}
$$
这是整个 $\mathcal O(434)$ 截面的有限拉回，
故 $\widehat H_j$ 在整个 $\mathbf P^1_R$ 上无共同零。
在 $u=1/4$ 也保留原434次项；不能只检查仿射一般点。

对 $0\le r<L$，
$$
\widehat B_{Ln+r}
=\widehat\Theta^r Q_r\widehat\rho_L^n
 R[u]_{\le Mn+q_r}.
\tag{18}
$$
写 $r=195a+v$ 可得 $q_r=186a+q_v$。
对 $0\le v<195$，最低值为 $-4$，
且 $q_v<-1$ 恰在 $v=1,2,3$。
所以全部 $q_r\ge-4$，
$q_r<-1$ 也仅在 $r=1,2,3$。

应用原三参数的完整 Koszul 复形，
当 $Mn+q_r\ge2M-1$ 时乘法在整格上满射。
故一般 $r$ 只需保 $n=0,1$，
上述三个例外另保 $n=2$。
所有模生成元的原权仍不超过
$$
\boxed{2L+3=2733.}
\tag{19}
$$
因此 $\widehat B$ 在旧 $A^{(8)}$ 上有限。
结合 (11)、正规性与真实夹持，
$$
\boxed{
\overline{A^{(8)}[\widehat\Psi_{35},\widehat\Psi_{53}]}
=\widehat B.
}
\tag{20}
$$
把已验证属于 (16) 的其它原来源并入，不改变该规范化。
这同时证明 (15) 是完整公共除子；
没有漏掉一个尚未检查的共同有限零点。

## 6. 全部195余权与秩36270的同一个自由整数格

取
$$
\widehat\Lambda_m=
\widehat\Theta^m Q_m\mathbf Z[u]_{\le q_m},\qquad
\widehat\rho=\widehat\Theta^{195}Q_{195},\qquad
P_0=\mathbf Z[\widehat\rho,\widehat\rho u^{186}].
$$
每个 $Q_m$ 都 primitive，Gauss 引理给同一实际整数交格。
对 $0\le r<195$、$0\le i<186$，令
$$
h_{r,i}=\left\lceil\frac{i-q_r}{186}\right\rceil,\qquad
e_{r,i}=\widehat\Theta^rQ_r\widehat\rho^{h_{r,i}}u^i.
$$
准确有
$$
\boxed{
\widehat\Lambda=
\bigoplus_{\substack{0\le r<195\\0\le i<186}}
P_0e_{r,i},\qquad
\operatorname{rank}_{P_0}\widehat\Lambda=36270.
}
\tag{21}
$$

为核全边界，$q_0=0$，其余显示分段为
$$
q_r=
\begin{cases}
r-5,&1\le r\le65,\\
r-6,&66\le r\le97,\\
r-8,&98\le r\le130,\\
r-9,&131\le r\le194.
\end{cases}
$$
所以全部 $h_{r,i}\in\{0,1,2\}$。
值2只发生在 $r=1$ 的 $i=183,184,185$，
$r=2$ 的 $i=184,185$ 和 $r=3$ 的 $i=185$；
最高基权仍为393。

证明 (21) 时固定总权 $195n+r$，
把实际角指数唯一写成 $186v+i$。
原帽正等价于 $n-v\ge h_{r,i}$，
遂把全部整单项式基按系数一返回到 (21)。
没有省略任何余权或最高短块。

若 $r+s=195d_0+r'$，完整乘法只多因子
$$
\frac{Q_rQ_s}{Q_{195}^{d_0}Q_{r'}}
=u^{\epsilon_0}(u-1)^{\epsilon_1}
 (1+8u)^{\epsilon_2}(1-4u)^{\epsilon_3},
\qquad \epsilon_j\in\{0,1\}.
\tag{22}
$$
其次数至多4、整数系数绝对值和至多90。
再按 (21) 返回，$P_0$ 系数总次数至多4；
这也由两基权之和不超过786直接核定。
因此完整固定乘法有显示的有限成本。

## 7. 显式 trace 导子、全部整返回与 p-饱和

取一个实际生成元
$$
Z_*=\widehat\Psi_{35}\in\widehat B_{65}.
$$
用 (11) 的三次函数域 trace 定义
$$
T_2=\operatorname{Tr}(Z_*^2),\qquad
T_3=\operatorname{Tr}(Z_*^3),
$$
$$
\boxed{
\Delta=\det\bigl(\operatorname{Tr}(Z_*^{i+j})\bigr)_{0\le i,j\le2}
=\frac12T_2^3-3T_3^2\in B^{(8)}_{390}.
}
\tag{23}
$$
完整 trace0 给三次最小式
$Y^3-(T_2/2)Y-T_3/3$，因此 (23) 是同一实际 trace 配对的行列式。
它非零，不是另挑一个子式。

$B^{(8)}$ 正规，$\widehat B$ 已在其上有限整，
故上述 traces 及后面的全部 trace 系数确实在旧 $B^{(8)}$ 中。
对任意 $b\in\widehat B_m$，
trace 配对的完整 adjugate 回乘准确给
$$
\boxed{
\Delta b=A_0+A_1Z_*+A_2Z_*^2,\qquad
A_j\in B^{(8)}_{m+390-65j}.
}
\tag{24}
$$
这是全部三列的真实身份，不是只说存在一个有理分解。

R996 的原导子 $c_8$ 权为69615，且
$c_8B^{(8)}\subset A^{(8)}$。
所以可以固定取
$$
\boxed{
c_{\rm new}=c_8\Delta,\qquad
C_{\rm new}=70005,\qquad
c_{\rm new}\widehat B_m
\subset A^{(8)}[Z_*]_{m+70005}.
}
\tag{25}
$$
特别 $c_{\rm new}\in A^{(8)}$，由旧实际返回直接表达，
没有把新规范化参数免费当作来源。

在任一原允许 $p>3$，第3节已证明 $\bar Z_*$
仍生成次数三的可分扩张。
因此 (23) 的 trace 配对在剩余函数域中仍非退化，
$\bar\Delta\ne0$。
这不是要求 $\Delta$ 的某个指定 Taylor 系数为单位。
连同原 $\bar c_8\ne0$，它支付
$c_{\rm new}$ 在整个显示整环中的非零性。

若 $c_{\rm new}b=pa$，
在 $\widehat B/p\widehat B$ 约化，
它仍是显示多项式 Gauss 模型的整环，故 $b=pb_1$，
继而 $a=c_{\rm new}b_1$。
因此导子像在真实来源环中 $p$-饱和。
不由此推断截断 jet 像饱和。

(19) 的固定生成元、(17) 的原来源返回、(24) 的完整 trace
与旧 $c_8$ 表一起给
$$
\deg_{\rm sources}\operatorname{return}(c_{\rm new}b)
\le\left\lfloor\frac{m+70005}{17}\right\rfloor,\qquad
\|\operatorname{return}(c_{\rm new}b)\|_1
\le C^{m+1}\|b\|_{\rm basis}.
\tag{26}
$$
每次只使用固定有限表；分母素数不随 $m$ 变化。
清固定 $D_{\rm ret}^{m+1}$ 后，
仍是原真正整数像格中的整单射，费用为 $O(m+1)$。

### 7.1 原点位移与完整六块费用

若需要 R960 的显示导子前缀位移，
令 $L_*=\operatorname{lc}f_{35}\ne0$。
在 $t=0$ 的两个 $u=\infty$ 分支，
$Z_*/\Theta^{65}$ 的首项分别为 $\pm\beta\sqrt t$，
其中
$$
\beta^2=\frac{27L_*^2}{4^{127}}.
$$
第三支从 $t$ 起。
因此
$$
\Delta/\Theta^{390}
=\frac{3^9L_*^6}{4^{380}}\,t^3+O(t^4).
\tag{27}
$$
原点阶准确为三。
若要把这一指定首项也当作单位，
另外排除固定非零 $L_*$ 分子的素因子即可；
(25) 的全环非零与饱和本身不需要这一额外首项条件。

沿 R996 的 $r_8=r_c+16$，
新导子位移为
$$
r_{\rm new}=r_8+3=r_c+19.
$$
原六块比较完整保留
$\exp((70005/17)a_p\epsilon)$、
全部五次高轴项及 $5r_{\rm new}$ 个真实跨界费用；
物理窗仍按 $L+r_{\rm new}<p$ 等原条件使用。
不能因为自由模扩大三倍，就删掉这些原目标方向。

## 8. 精确 Hilbert 改善与原完整评价

由 (16)、(25)，
$$
\boxed{
\dim\widehat B_m=\frac{62}{65}m+O(1),\qquad
\sum_{m\le M}\dim A_{\rm new,m}
=\frac{31}{65}M^2+O(M).
}
\tag{28}
$$
这里 $A_{\rm new}$ 可包括第4节全部已核原列。
每个维数都来自真实来源函数域及导子返回。

也有一个不依赖规范化描述的直接核对：
$1,Z_*,Z_*^2$ 在旧函数域上线性独立，故
$$
A^{(8)}\oplus Z_*A^{(8)}\oplus Z_*^2A^{(8)}
$$
在真实来源环中严格直和。
两个实际权位移65、130均保留，
R996 的主项直接给 (28) 的下界，
与完整规范化结果一致。

仍使用 R989/R996 的同一个原
$$
\Gamma_L^{(6)}
=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^6,w^\ell\epsilon^5)
$$
及其全部有序行。
在这个真实评价中，$u=u(t)$ 是 (1) 在原点的唯一整分支；
导数 $-27$ 为单位，所以全部形式系数在 $\mathbf Z[1/3]$ 中。
先代原 $t(w)$，再代
$$
\widehat\Theta=\Theta/(1-4u(t)).
$$
最后一个分母在原点为单位，全部整数幂按原完整单位逆读取。

原高轴仍只有同一个 $H_p,E_p$ 所给的实际五轴。
$u(t)$ 不随这五轴改变，没有新增可选的角高位。
联合坏 canonical 下，
R989 已付的原 $\Theta$ 评价模 $p^6$ 逐项不动；
因此上述整个三次角评价也逐列、逐行、逐物理前缀不动。
所有原低权列、新列及 (25) 的导子费用都在同一个目标内。

特别，对第8节的三个真实来源副本，物理矩阵准确是
$$
\boxed{
[\ \mathcal J_{\rm old}\ ,\
 M_{\mathcal J(Z_*)}\mathcal J_{\rm old,\,65}\ ,\
 M_{\mathcal J(Z_*)^2}\mathcal J_{\rm old,\,130}\ ],
}
\tag{28a}
$$
下标65、130保留对应的来源权位移，
$M$ 是同一 $\Gamma_L^{(6)}$ 中的真实乘法。
三个像的秩不能相加。
它们还保留完整三次关系
$$
M_{\mathcal J(Z_*)}^3
-\frac{\mathcal J(T_2)}2M_{\mathcal J(Z_*)}
-\frac{\mathcal J(T_3)}3I=0.
\tag{28b}
$$
在 nilpotent 目标或某个物理前缀上，
这个关系及所有共同核仍须实际读取。

新输入可在同 charge65 上写成
$$
F_{\widehat\Psi_i}^{[6]}(x)
=\sum_{h=1}^6
\frac{(-1)^{h-1}(h-1)!p^{h-1}}
 {(65/17)^h a_p^{h-1}}
[w^{hs-1}]\widehat B_i(w)e^{(65/17)\eta_x}.
\tag{29}
$$
(7)–(8) 支付全部尾及原两次真实除 $p$ 的输入。
更明确地，若 $b_i$ 是原 $\Psi_i$ 的前五系数行，
新行的第 $r$ 项准确为 $(-27)^{1-r}b_{i,r}$。
记此行作 $\widehat b_i$，则同一个原五位点提升 $x_5$ 上的真实六位余式为
$$
\boxed{
\widehat{\mathfrak r}_{i|5,p}^{[6]}
=F_{\widehat\Psi_i}^{[6]}(x_5)
-\widehat b_iB_5^{-1}F_{\rm old5}^{[6]}(x_5)
\pmod{p^6}.
}
\tag{30}
$$
所有原前五项仍读到第六位，
$H_p,E_p$ 仍是 R989(39)–(42) 的那两个确定数，
包括完整低卷积和 $8^s$ 的全部进位。
必要点与 (30) 都按这个同一参考取值。
不能把这些新的确定系数当作独立 H/E 参数，
也不能仅由同 charge 就认它们与旧22列线性相同。

## 9. 全位同格含义与继续 forcing 的准确范围

新来源的首项、普通单位域、惰性整圆盘与实增长已在第2节支付。
因此对真实来源整数像格及同一个完整前缀，
原实位估计仍为
$$
-3k\log k+3k\log(M+1)+O(k+M+1),
$$
原好普通范数不增，
原无条件惰性包络及固定坏位费用仍按 R957/R960 使用。
增加固定个数的来源只改变呈示空间的多项式次数，
其对数费用为 $O(\log(M+1))$。

本篇真正改变的是 (28) 的来源维数主项、
(21) 的完整整数基和已付 (25) 的同来源返回。
原 $a+2b<3$ 的全位门、全部 $P_2/Z$ 缺陷、
真正后页及仿射 forcing 仍须在这个扩大后的实际矩阵中消费。
生成元中央全零不使一般乘积中央全零；
本篇没有按维数三倍宣称三个额外深块或无穷性已成。

全文为原恒等式、固定有限 trace 与整模证明。
未执行本地数学，未增加素数扫描或读取一个缓存矩阵来替代来源。
