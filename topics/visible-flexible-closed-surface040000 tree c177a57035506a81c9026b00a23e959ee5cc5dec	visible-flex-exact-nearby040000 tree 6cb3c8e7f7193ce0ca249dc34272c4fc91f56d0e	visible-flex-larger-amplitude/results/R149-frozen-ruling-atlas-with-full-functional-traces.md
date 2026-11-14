# R149：冻结母线标签 atlas 与完整函数迹的同物理接合

**状态：已证明。** 本结果给出一个具体的全局分片角 atlas，在整个已定义 coast 使用自然母线标签，前后以正凸组合返回旧计算角图。它不改变物理度量，不除以未知 raw $n$，并严格区分新有限场的准确接合与旧场的有限投影误差。

## 1. 固定对象与标签含义

物理度量始终写为

$$
g_\delta=ds^2+a_\delta(s)^2du^2,\qquad a_\delta>0.
$$

当前 $a_\delta$ 可包含已有真实径向 bump 参数。以下角图全部固定于原 R139 入口及同一 base candidate，不随当前 $\delta$、中央系数或尾系数更新。

记原固定 seed 材料映射为 $S(\xi)=U_{\rm seed}(\xi)$。当前旧角图是

$$
O(s,\xi)=(1-\beta(s))S(\xi)+\beta(s)\xi,\qquad
0\le\beta\le1. \tag{1}
$$

这里 $\xi$ 是冻结 seed 的法向角标签，$S'(\xi)>0$。所有提升使用同一原点与同一 $2\pi$ deck convention，不能在凸组合之前各自把角度独立模掉 $2\pi$。

R139 的物理 coast 是 $[c,d]$，$d=c+L_c$。给定冻结入口 $n_c(t)>0,m_c(t)$，置

$$
k(t)=m_c(t)/n_c(t),\quad r_0=a_c/v,\quad r=r_0+\sigma,
$$
$$
Q=\sqrt{r_0^2+(1+k^2)\sigma(2r_0+\sigma)},\qquad
w_0=\frac{\sigma(2r_0+\sigma)}{r_0+Q},
$$
$$
\mathcal U(\sigma,t)
  =t-\frac1v\arctan\frac{k(t)w_0}{r_0+w_0}. \tag{2}
$$

其准确正 Jacobian 是

$$
\mathcal U_t=\frac{D}{vQ}>0,\qquad
D=a_c+w_0\bigl(v(1+k^2)-k_t\bigr). \tag{3}
$$

本次 coast 计算角选为

$$
N(s,\xi)=\mathcal U(s-c,S(\xi)). \tag{4}
$$

**标签区分：** 已闭 `FrozenRulingChart` 的 $\xi$ 是冻结入口 seed-normal 标签；字面的入口材料标签是 $t=S(\xi)$。两者沿同一母线均为固定标签，但 Fourier 模式 $\cos(2j\xi)$ 与 $\cos(2jt)$ 不是同一个有限空间。本次采用 (4)，不暗中交换这两种空间。

R139 的准确正性包适用于 (2)–(3) 的冻结输入；当前 raw $n$ 可为零或负，均不参与 (2) 的分母。换成另一个正的 $a_\delta$ 时，(2) 仍是合法的参考角图，但它的 native GC 场不会因此自动成为新度量的准确解。

## 2. 明确的四段 atlas

取 $s_-<c<d<s_+<L$，本次具体约定为

$$
s_-=.55,\quad c=.5919999999999992,\quad
d=.8675434451024153,\quad s_+=1.40.
$$

$c,d,L_c$ 的准确机器记录及原始数学身份由 R139 入口与 atlas manifest 绑定；上述十进制用于展示。令 $E(\xi)=N(d,\xi)$，并令 $S_5$ 为在单位区间外截断的 quintic step。定义

$$
q_-(s)=S_5\left(\frac{s-s_-}{c-s_-}\right),\qquad
q_+(s)=S_5\left(\frac{s-d}{s_+-d}\right).
$$

采用以下全函数图：

$$
U(s,\xi)=
\begin{cases}
O(s,\xi),&s\le s_-,\\
(1-q_-(s))O(s,\xi)+q_-(s)S(\xi),&s_-\le s\le c,\\
N(s,\xi),&c\le s\le d,\\
(1-q_+(s))E(\xi)+q_+(s)O(s,\xi),&d\le s\le s_+,\\
O(s,\xi),&s\ge s_+.
\end{cases} \tag{5}
$$

因此中央及切口的开放邻域完全使用旧图。当前原 blend 在约 $1.3996347877$ 已到材料圆图，故在 $s\ge1.40$ 有 $U=O=\xi$；原尾 reader 的真实材料切口定义保留。

旧保存网格已有 $s_-,c,d$；新 provider 明确补入 $1.40$ 这一计算 knot，节点数由122变123。这个节点插入不改物理 profile。实际消费者仍以新 NPZ 内保存的节点为准，不凭名称重建或偷偷删节点。

## 3. 正性、周期、D2 与完整角迹

由 (1)，$O_\xi=(1-\beta)S'+\beta>0$；由 (3)–(4)，

$$
N_\xi=\mathcal U_t(s-c,S(\xi))S'(\xi)>0.
$$

过渡图的角导数是两个严格正角导数的凸组合，故 (5) 全域满足 $U_\xi>0$。各函数连续于有限个紧条带、分母有已证明严格余量，因此存在统一 $\eta>0$，使每片 $U_\xi\ge\eta$。这一正性不依赖当前未知字段的符号。

所有图满足 $U(s,\xi+2\pi)=U(s,\xi)+2\pi$，故是圆上的定向保持 degree-one 微分同胚。对于本题 D2 数据，$S$ 为奇提升且满足 $S(\xi+\pi)=S(\xi)+\pi$；入口 $n_c$ 偶、$m_c$ 奇且均 $\pi$ 周期，所以 $k$ 奇、$w_0$ 偶，(2) 的角移位为奇且 $\pi$ 周期。于是 $N,E,O$ 及其标量凸组合都保持相同 D2 结构。

因为 $q_-(c)=1$、$N(c,\xi)=S(\xi)$，入口两侧作为**完整角函数**相等。出口由 $q_+(d)=0$ 与 $E=N(d,\xi)$ 同理。$s_-,s_+$ 两端回到同一旧图。对这些全函数恒等式作一次、二次角微分，得到所有接口的

$$
[U]=[U_\xi]=[U_{\xi\xi}]=0. \tag{6}
$$

这是解析函数迹恒等式，不是对有限角节点相等的推断，也没有对 $E$ 或 $N$ 先作低模 Fourier 截断。

## 4. 单侧径向 jets 必须真实记录

入口过渡 $A=(1-q)O+qS$ 满足

$$
\begin{aligned}
A_s&=(1-q)O_s+q'(S-O),\\
A_{ss}&=(1-q)O_{ss}-2q'O_s+q''(S-O),\\
A_{s\xi}&=(1-q)O_{s\xi}+q'(S'-O_\xi).
\end{aligned} \tag{7}
$$

出口过渡 $B=(1-q)E+qO$ 满足

$$
\begin{aligned}
B_s&=qO_s+q'(O-E),\\
B_{ss}&=qO_{ss}+2q'O_s+q''(O-E),\\
B_{s\xi}&=qO_{s\xi}+q'(O_\xi-E').
\end{aligned} \tag{8}
$$

由于 $S_5'$、$S_5''$ 两端为零，在 $c$ 的过渡侧有 $U_s=0$，而准确 coast 侧一般有 $U_s=-k/a_c\ne0$。在 $d$ 的出口过渡侧同样有 $U_s=0$，coast 侧通常非零。$U_{ss},U_{s\xi}$ 也应分别消费真实单侧公式。不得把整个 atlas 宣称为全局 $C^1$，也不得为了让节点导数看起来相同而平均、抹平这些真实值。

接口约定可用 `side='coast'|'left'|'right'`：solver 默认选 coast 侧作节点记录；Gauss2 内点处不涉及选择。native reader 的 `side='left'` 或 `'right'` 必须同时选择该侧的 P1 斜率和 (7)–(8)/(2) 的径向图 jet，不能只改 correction slope 却留着另一侧的 $U_s$。

已知接口必须在积分片定义中明确。R146 的 lifting 端点积分只用共同的函数值，不受这些单侧径向 jets 的选择影响。

## 5. 同物理度量与完整三场方程

在每片上，原目标的准确拉回为

$$
U^*g_\delta
 =(1+a_\delta^2U_s^2)ds^2
 +2a_\delta^2U_sU_\xi\,ds\,d\xi
 +a_\delta^2U_\xi^2d\xi^2, \tag{9}
$$

其行列式为 $a_\delta^2U_\xi^2>0$。这只是同一 $ds^2+a_\delta^2du^2$ 的坐标表达。

计算字段 $\widetilde f=f\circ U$ 的真导数关系为

$$
f_u=\widetilde f_\xi/U_\xi,\qquad
f_s|_u=\widetilde f_s-(U_s/U_\xi)\widetilde f_\xi. \tag{10}
$$

因此两条 Codazzi 仍准确为

$$
\begin{aligned}
\widetilde n_s&=\frac{\widetilde m_\xi}{a_\delta U_\xi}
  +\frac{a_\delta'}{a_\delta}(\widetilde l-\widetilde n)
  +\frac{U_s}{U_\xi}\widetilde n_\xi,\\
\widetilde m_s&=\frac{\widetilde l_\xi}{a_\delta U_\xi}
  -2\frac{a_\delta'}{a_\delta}\widetilde m
  +\frac{U_s}{U_\xi}\widetilde m_\xi.
\end{aligned} \tag{11}
$$

Gauss 约束是 $\widetilde l\widetilde n-\widetilde m^2=-a_\delta''/a_\delta$。三分量保持独立；没有在未知 $n=0$ 处作消元。不能在过渡片漏掉 (11) 的 $U_s/U_\xi$ 项。

由于整个 $U$ 固定于已有参考输入，未知 profile/tail/central 参数的 $U_p$ 均为零；目标 $a_\delta,a_\delta',a_\delta''$ 与实际 lifting 的参数导数仍完整保留。参考 base 上的 native GC 恒等式不替换 (11) 的当前目标。

## 6. 新有限场如何准确接合

设实际新 correction 用统一标签 $\xi$ 的有限 Fourier 基 $B(\xi)$ 与全域共享的径向 P1 节点系数 $y_j$，并以完整函数 lifting $L(s,\xi)$ 定义

$$
\widetilde f(s,\xi)=B(\xi)P_1(y_j)(s)+L(s,\xi). \tag{12}
$$

若 $L$ 在四接口具有共同的值及角二 jet，(12) 的两侧就有共同的完整函数与角二 jet：同一个接口节点只保存一份 $y_j$，不分别给两边重投影。

本次旧 seed lifting 的截止恰为 $s_-=.55$；角图发生变化的区域中它已为零。剩余 tail lifting 和 R144 冻结 reference 都是明确的物理函数与当前 $U$ 的复合，且其标量权重只依赖 $s$。由 (6)，这些 lifting 在接口具有准确共同角迹。特别是 coast reference 不能只保存成低角样本表后各侧独立插值。

结合 (6)、(10)，新物理字段

$$
f(s,u)=\widetilde f(s,\Xi(s,u)),\qquad U(s,\Xi(s,u))=u,
$$

具有连续的 $f,f_u,f_{uu}$。这证明的是新 (12) 自身的同物理接合；并没有声称它等于之前另一个有限场。

若要**保持某个外段原场不变而仅更换 coast**，则必须把给定的完整物理迹 $T(u)$ 精确复合为 $T(U(s_i,\xi))$。若这不是新有限 Fourier 空间中的函数，不能把它截断后声称原迹得到保留。最小可计算修正是在相邻片加入一个明确的 endpoint carrier：

$$
\chi(s)\bigl[T(U(s_i,\xi))-\widetilde f_{\rm bare}(s_i,\xi)\bigr],
\qquad\chi(s_i)=1,
$$

并使 $\chi$ 在另一个已声明端点为零。方括号保留全函数与其角导数；若 $T$ 依赖共享接口未知系数，它的全部相应 Jacobian 列也必须保留。这样可准确接合而不暗中丢高模。当前全局 joint 求解方案采用 (12) 的共享节点与新 warm，并不宣称这种“保持旧外段”的额外身份。

## 7. 换图 warm 不是无误差有限重表达

令 $\Xi_O(s,u)$ 为旧图的逆。保持旧物理场的准确表达是

$$
\widehat f(s,\xi)
 =\widetilde f_{\rm old}
   \bigl(s,\Xi_O(s,U(s,\xi))\bigr). \tag{13}
$$

其 correction 角函数通常不再是有限 Fourier 多项式。当前变图区的 lifting 全部是同一物理函数的复合，故准确有

$$
L_{\rm new}(s,\xi)
 =L_{\rm old}\bigl(s,\Xi_O(s,U(s,\xi))\bigr). \tag{14}
$$

所以 warm 可以只转换 correction；但转换后的函数仍需作明确有限投影。对每个实际保存节点 $s_j$，记

$$
C_j^*(\xi)
 =B\bigl(\Xi_O(s_j,U(s_j,\xi))\bigr)y_{\rm old}(s_j),
\qquad
y_j^{\rm new}=P_K C_j^*. \tag{15}
$$

此处旧 $y_{\rm old}(s_j)$ 在新增节点1.40由旧真实 P1 函数求值。增加节点与角投影是两件不同操作：前者可准确保留原 P1 函数，后者一般改场。未变图区可以直接复制或 P1 重采原系数，避免无意义再投影。

新的场由 $P_1(y_j^{\rm new})$ 和 $L_{\rm new}$ 定义。节点遗漏是完整函数 $C_j^*-BP_KC_j^*$；格内另有先 P1 后非线性复合与先复合后 P1 的差。有限角采样只能给实际有限诊断，不能把连续角尾称为已证明零。若 $P_K$ 实际使用有限 DFT，采样混叠、求逆误差和浮点误差也要与准确的投影定义区分。

无论这些 warm 遗漏大小如何，只要 (12) 的共享节点与全函数 lifting 定义保持一致，新场本身的接口连续性成立。旧场的准确身份或旧实际几何证书则不能因接口连续而自动转移。

## 8. 固定材料坐标的实际 $C^2$ 重建

按 R141，以统一的原材料角 $u$ 解

$$
F_s=FA(l,m),\qquad X_s=Fe_1,
$$

其中 $A$ 为原反对称物理连接矩阵。第6节给出 $A,A_u,A_{uu}$ 的共同连续迹，线性积分方程与其角变分因此跨接口唯一连续延续，实际 $X$ 为 $C^2$。这一论证不要求 atlas 的 $U_s$ 连续，也不要求 P1 字段的全局径向一导数连续。

后验依旧使用实际位置的 Gram、法向与两 jet，不能用辅助 $l,m,n$ 自动替代实际曲率。若 GC 仍有残差，图的定义仍明确，但等距、闭合、嵌入、reach、帽接合和强比例必须继续支付。

材料相位族仍作用在 $u$。当前一般只有 D2 deck 对称，不能把新标签 $\xi$ 的任意平移当作原材料的同一个旋转等距运动。

## 9. 最小 native reader 定义

新 checkpoint 应显式保存以下身份与定义，而不是继续把 `blend` 当成完整实际角图：

- 实际 `mesh/corrections/parameters`、candidate SHA、`physical_bumps` 支撑、固定 base 参数和完整 seed/tail/coast lifting 定义。
- `angular_atlas_definition`：旧图定义、冻结 R139 入口和依赖源、(5) 的四接口、quintic step、coast 标签含义、默认节点侧及参数冻结声明。
- 新增1.40节点的确切值与旧 P1 重采样规则；warm 的原输入 SHA、有限角投影规则、材料逆求值误差和实际遗漏诊断。

reader 对任意 $(s,\xi)$ 按其声明条带返回 $U,U_\xi,U_{\xi\xi},U_s,U_{s\xi},U_{ss}$，并按相同侧求真实 P1 斜率。随后计算完整 (12) 及其真 jets；对于物理查询 $(s,u)$，求当前 atlas 的单调逆，再用 (10) 与

$$
f_{uu}=\frac{\widetilde f_{\xi\xi}U_\xi-
                    \widetilde f_\xi U_{\xi\xi}}{U_\xi^3}.
$$

旧图 reader 不得仅因参数维数和网格仍能读入就消费新 checkpoint。缓存键仍须包含实际 $s$ 和完整材料角列；旧 coast cache 中同 $s$ 的旧角列不能借作新角列。直接在已知母线标签求 R139 参考值可免一次逆映射，但那是同一准确函数的新求值路径，必须单独绑定其源与实际数值误差。

本结果本身不运行新的 BVP，不产生主态收敛声明。实际 provider、warm 和完整消费者的运行身份由各自闭存记录给出。
