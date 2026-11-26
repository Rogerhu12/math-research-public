# R586：完整历史的六元形式平均与原十九态导数的有限积分预收

日期：2026-11-26。**已证明的原式转换；未执行新符号、profile 求积、ODE、优化或秩计算。**

本文接 R578、R581、R584。对象是同一实际 R578 不交库及 R584 的整个十九态方程，不再只读 $A=0$ 的局部项。新的接口有三部分：

1. 完整局部、第二能量、线性项、有序第三复合和局部第三投影都只有两种明确的四次型；六元平均可在形式系数层准确完成。
2. 所有相应完整块读出的平移次数至多十，因此可用同一实际图中一组六正节点的参考计算，准确评价全部36个实际块；真实物理库没有更换。
3. 完整第三更新可先转置并消去母形四阶导数与第三右原函数，得到明确 C³ 多项式被积式。与 R584 的精确状态变换合并后，整个加速度和历史更新都有固定有限积分预收接口。

本文不把 C³ 真项擅自称为 C²，不假定完整第三 outer 零，不授有限八根或端图 rank。

## 1. 原完整块及六个正交变换

使用 R578 的同一个32微包基本块，暂记其未作正交旋转的两个 profile 为 $f_0,g_0$。在每个微包
$$
f_0=\alpha u,\qquad g_0=\beta u,\qquad \alpha\beta=0.
\tag{1}
$$
不同微包有真实间隙。因此不只 $f_0g_0=0$，任何两个导数的混合乘积也逐点为零。这个性质仅用于当前 R578/R521 从不交微包组成的基本块；不对一般重叠 profile 圆作此断言。

六个变换为
$$
f_{\vartheta,\epsilon}=\cos\vartheta\,f_0
-\epsilon\sin\vartheta\,g_0,\qquad
g_{\vartheta,\epsilon}=\sin\vartheta\,f_0
+\epsilon\cos\vartheta\,g_0,
$$
$$
\vartheta\in\{0,2\pi/3,4\pi/3\},\qquad\epsilon=\pm1.
\tag{2}
$$
由 (1)，整个二次差槽及其导数密度准确满足
$$
\Delta_{\vartheta,\epsilon}
=\cos(2\vartheta)\Delta_0,\qquad
\Delta_0=f_0\odot f_0-g_0\odot g_0.
\tag{3}
$$
这里 (3)用于实际二次微分/积分输入，依据混合导数乘积全部为零，不是先把一般对称槽当普通乘积。

原三条完整块真二尾因此同样统一乘 $\cos2\vartheta$：
$$
J_j^{\vartheta,\epsilon}
=\cos(2\vartheta)J_j^0,\qquad j=0,1,2.
\tag{4}
$$
$J_2$ 继续含原额外 $2(f')^2-2(g')^2$ 项。在微包之间没有重新归零。

R521/R523/R578 已付每个完整块的原二、三 ruling 与全部 $I_j(g,\Phi_E\Delta)$ 交叉条件。因此原 second 和所用 third 恢复在完整块外的 collars 真零，整个实际库的下述积分可按完整块相加。仅凭 (1)并不能推出这种跨块局部性；此处明确消费已付的完整块条件。

## 2. 两种齐次型及准确形式投影

在 R581 的形式变量中记 $C$ 为当前微包 $g$ 的系数，$D$ 为当前 $\Delta$ 的系数，$J_0,J_1,J_2$ 为真二尾；$u,p,r,t$ 为母形的0…3阶 jet。几何、矩阵坐标和加速度只作为系数。

下列两类四次型足够覆盖本文所有完整读出：

- **QQ 型：** 不含 $C$，在 $(D,J_0,J_1,J_2)$ 中总次数为2；
- **LLQ 型：** 含 $C^2$，在 $(D,J_0,J_1,J_2)$ 中总次数为1。

“Q”表示一个原二次输入的线性输出，计数只用于证明四次齐次性，不将它当新的独立状态。母形 jet 的次数也保留；上述表只记录角系数。

令 $D_0=\alpha^2-\beta^2$ 为未旋转基本块的当前微包系数。准确群平均满足
$$
\operatorname{Av}\cos^2(2\vartheta)=\frac12,
$$
$$
\operatorname{Av}
(\alpha\sin\vartheta+\epsilon\beta\cos\vartheta)^2
\cos(2\vartheta)
=-\frac{\alpha^2-\beta^2}{4}
=-\frac{D_0}{4}.
\tag{5}
$$
第二式用 $\alpha\beta=0$；三个角分别给
$\operatorname{Av}(\sin^2\vartheta\cos2\vartheta)=-1/4$、
$\operatorname{Av}(\cos^2\vartheta\cos2\vartheta)=1/4$。
反射副本保同一平均。

于是存在一个明确的形式投影 $\mathcal A$：

$$
\boxed{
\begin{aligned}
\mathcal A\{D^aJ^\mathbf b\,P\}
&=\tfrac12D_0^a(J^0)^\mathbf bP
&& (a+|\mathbf b|=2),\\
\mathcal A\{C^2D^aJ^\mathbf b\,P\}
&=-\tfrac14D_0^{a+1}(J^0)^\mathbf bP
&& (a+|\mathbf b|=1).
\end{aligned}}
\tag{6}
$$
$P$ 是不含这些角变量的原母 jet/位置/几何多项式。计算 (6)时先合并相同的形式单项式，再评价固定 profile 积分。因此任何由 (5)产生的零在积分前就是准确零，不依赖浮点三角函数及高项求积后的相减。

例如 R581 的最高项含
$$
D^2+2C^2D;
$$
(6)准确给 $(1/2-2/4)D_0^2=0$。但 (6)并不消掉任意 $D^2$ 项，尤其不能删除实际第二能量中的真正高导平方。

### 2.1 为什么完整历史也只出现这两种型

对固定任意实际矩阵 $A,M$，$q_A=\Phi_A\Delta$、$q_M=\Phi_M\Delta$、原局部 $K(\Delta)$及其真时间/空间导数，都对 $(D,J)$ 一次。第一场 $Y_g$ 及其导数都对 $C$ 一次。因此：

- R581 的 $|K_1|^2$ 为 QQ；其余第一场与 local/chain 配对为 LLQ。
- $G_j[A,M]=I_j(q_A,q_M)$ 为 QQ。
- $B_j[M,A]=I_j\{g,\Phi_M(g,q_A)\}$ 为 LLQ。
- $c_j=I_j\{g,\mathcal C_s(g;\Delta)\}$ 为 LLQ：$\mathcal C_s$ 对第一槽一次、对 $\Delta$ 一次，原变化-profile chain 保此次数。
- $\mathscr L=2\mathcal T(q_A;\Delta)-4\mathcal T(g;g,q_A)$，前项 QQ，后项 LLQ。

原空间导数把 $J_j$ 换成当前 $D$ 乘二次 jet 密度，保持 $(D,J)$ 次数；时间导数只改几何与真实矩阵系数。故 R584 中 $\dot\lambda\cdot A$、$\lambda\cdot M$、$G[M,A]/2-B[M,A]$及其完整组合仍全在这两类里。

没有 $C$ 的一次或三次型，也没有未经证明删掉的第三累计。$A$、$M$ 在这里是同一实际轨道的系数，不能任意时变替代原 $A_s=M$。

## 3. 完整平移次数与一个六节点参考积分

将一个完整基本块作位移 $c$，使用局部坐标 $\xi=y-c$。母形 jet 与微包系数不变，而真实二尾满足
$$
J_0^c=J_0^0,\qquad
J_1^c=cJ_0^0+J_1^0,\qquad
J_2^c=c^2J_0^0+2cJ_1^0+J_2^0.
\tag{7}
$$
所以可给形式变量赋平移权：
$$
\deg_{\rm tr}y=1,\quad
\deg_{\rm tr}J_0=0,\quad
\deg_{\rm tr}J_1=1,\quad
\deg_{\rm tr}J_2=2,
\tag{8}
$$
其余母 jet、$C,D$、几何及矩阵坐标权为0。加权次数不超过 $d$ 的整块积分就是位置 $c$ 的次数不超过 $d$ 的多项式；间隙及真尾按 (7)一起位移，未改变积分域的实际相对形状。

原 E8 六项式有系数次数
$$
\deg(A_0,A_1,A_2)\le(1,2,3),\qquad
\deg(B_0,B_1,B_2)\le(2,2,2).
\tag{9}
$$
据此 $q_A$、$q_A'$、$q_A''$ 的平移次数均不超过4。原第二分子 $K_0,K_1$ 及其时间协变导数次数均不超过4；第一分子及其协变导数不超过1。空间求导不增加 (8)的上界，因为 $J_1'=-yDr^2$、$J_2'=-D(y^2r^2+2p^2)$ 保各自权。

第4–6节将完整读出写成显式多项式。由这些式子逐项有：

| 读出 | 平移次数上界 |
|---|---:|
| R581 局部 $\mathscr R$、加速度列 | 8 |
| $\mathscr L$ 与其真实时间导数 | 9 |
| $c_j,\ 0\le j\le2$ | 9 |
| $B_j[M,A]$ | $j+8\le10$ |
| $G_j[M,A]$ | $j+8\le10$ |
| R584 的完整 $\sigma_s$ 分子 | 10 |

这些是实际系数的次数上界，不是数值拟合。

R578 每个群元素拥有6个正节点和正权 $(c_{\vartheta,\epsilon,i},w_{\vartheta,\epsilon,i})$，它们的0…10矩完全相同。取其中任意一组作为参考 $(\widehat c_i,\widehat w_i)$。对本稿任一完整读出 $P$，先分别用位置矩恒等式，再用 (6)，得到
$$
\boxed{
\sum_{(\vartheta,\epsilon),i}
w_{\vartheta,\epsilon,i}
\int_{\rm block(c_{\vartheta,\epsilon,i})}P_{\vartheta,\epsilon}
=
6\sum_{i=1}^6\widehat w_i
\int_{\rm block(\widehat c_i)}\mathcal A P.}
\tag{10}
$$
左侧是真实36块；右侧只是同一值的参考评价。没有把右侧6个重叠旋转场当成一个新的物理库，也没有改变母形、宽度或 collars。每个 $w$ 都来自实际幅 $w^{1/4}$ 的四次幂。

因此可把原36块的角平均在形式系数层完成，再仅求6个参考块的完整积分。必须保所有真实二尾与间隙；(10)不是对任意非多项式读出的空间稀疏采样。

## 4. 三矩的准确一次转置

对 $j=0,1,2$ 定义原 outer 密度
$$
\mathcal D_jg=y^j g^{(4)}+2j\,y^{j-1}g''' ,
\tag{11}
$$
$j=0$ 时第二项按零处理。由两端紧性，$I_j(g,q)=\int(\mathcal D_jg)q$；$j=2$ 的原 $2g'q'$ 正是 (11)中二阶额外项消去所需，未被省略。

对任意次数不超过2的几何/矩阵位置多项式 $a(y)$，记
$$
W=y^ja,\qquad V=2j\,y^{j-1}a
$$
（$j=0$ 时 $V=0$），定义
$$
\boxed{
\mathfrak P_j[a]
=Wg'''+(V-W')g''+(W''-V')g'
+(V''-W''')g.}
\tag{12}
$$
因为 $j\le2$、$\deg a\le2$，准确有 $W''''=V'''$。若 $j+\deg a<4$ 两边都零；唯一四次情形 $j=2,\deg a=2$ 的最高系数两边同为 $24a_2$。故
$$
(\mathfrak P_j[a])'=a\,\mathcal D_jg.
\tag{13}
$$
原左 collar 的 $g$ 全 jets 零使其确为从左端开始的原函数。于是
$$
\int a(\mathcal D_jg)Jq=\int\mathfrak P_j[a]q.
\tag{14}
$$
不要求 $Jq$ 左值为零；左尾经原 Fubini 转置完整保留。又对任意当前 C² 局部多项式 $Q_0$，
$$
\int(\mathcal D_jg)Q_0
=-\int\mathfrak P_j[1]\,\mathscr D Q_0,
\tag{15}
$$
其中 $\mathscr D=D_0+t\partial_r$ 是 R581 的真正空间导数，保全部二尾导数。

$\mathfrak P_j[a]$ 只用 $g,g',g'',g'''$。式 (14)(15)将原 outer 四阶母导数移除；没有猜测其高频首项。

## 5. 完整局部第三投影的显式 C³ 式

使用 R581 同一个分子记法 $Y_i,K_i,\nabla_s$，并令
$$
T=Y_1\cdot K_1,\qquad
W=(\nabla_sY_1)\cdot K_1+Y_1\cdot\nabla_sK_1,
$$
$$
U_0=Y_0\cdot K_0,\quad
V_0=(\nabla_sY_0)\cdot K_0+Y_0\cdot\nabla_sK_0,\quad
N_0=(\nabla_sY_0)\cdot\nabla_sK_0.
\tag{16}
$$
继续写
$$
z=y+\eta,\quad e=hz-k,\quad Q=1+e^2,\quad
e_s=\gamma z-\upsilon/2,
$$
$$
\kappa_0=kz^2-(k^2+1)z/h,\qquad
\mu=\upsilon/(2h)-\gamma k/h^2,\qquad
v=q_M.
$$
由原 R73(16)及 R56 恢复，完整局部第三 scalar 是
$$
\mathcal C_s(g;\Delta)
=C_{\rm loc}+a_TJT+a_WJW+a_JJ(Qg''v''+2h^2g'v'),
\tag{17}
$$
其中
$$
\begin{aligned}
C_{\rm loc}={}&\frac{N_0}{2h^2}
+\frac{\kappa_0/z}{2h}U_0
-\frac{\gamma V_0}{2h^3}
+\frac{\gamma^2U_0}{2h^4}\\
&-\frac{\mu}{4}g'v+\frac{\gamma Q}{8h^3}g'v',
\end{aligned}
\tag{18}
$$
$$
a_T=\frac{\kappa_0}{2h}+\frac{\gamma e_s}{2h^4},
\qquad a_W=-\frac{e_s}{2h^3},
\qquad a_J=\frac{e_s}{8h^3}.
\tag{19}
$$
特别 $\deg_y a_T\le2$、$\deg_y a_W,\deg_y a_J\le1$，恰可使用 (14)。

为核 (17)，原第三 $P=JT/(2h)$、$B=U_0/(2h)$ 给
$$
P_s=JW/(2h)-\gamma JT/(2h^2),\quad
B_s=V_0/(2h)-\gamma U_0/(2h^2).
$$
代入 $\ell=N_0/(2h^2)+\kappa_0P-e_sP_s/h^2
+(\kappa_0/z)B-\gamma B_s/h^2$，
再减原 chain
$$
\Psi=\mu g'v/4-\gamma Qg'v'/(8h^3)
-e_sJ(Qg''v''+2h^2g'v')/(8h^3)
$$
就得到 (17)–(19)。所有符号与两个 $h$ 次数因此有原式依据。

$C_{\rm loc}$ 只含母形二阶 jet 与真二尾；$v'=q_M'$ 也只含这些量。于是由 (14)(15)，
$$
\boxed{
\begin{aligned}
c_j=I_j(g,\mathcal C_s(g;\Delta))
=\int\big\{&
-\mathfrak P_j[1]\,\mathscr D C_{\rm loc}\\
&+\mathfrak P_j[a_T]T+\mathfrak P_j[a_W]W\\
&+\mathfrak P_j[a_J](Qg''v''+2h^2g'v')\big\}.
\end{aligned}}
\tag{20}
$$
右侧只含母形至三阶 jet 与原二尾，关于 $t=u'''$ 至多二次。真正的 $K_s$ 时间导数仍含实际 $(a,b)$，所以 $c_j$ 的加速度依赖没有丢失。这里没有把这些真实三导平方项自动消去。

次数检查：$C_{\rm loc}$ 的平移次数不超过6；$T,W$ 不超过5；(12)的次数不超过 $j+\deg a$。故 (20)最高不超过 $j+7\le9$，足够使用 (10)。

## 6. 有序复合、能量及线性项的完整预收式

### 6.1 有序 $B[M,A]$

写原 $\Phi_M$ 的六项系数为 $A_0,A_1,A_2,B_0,B_1,B_2$，保 (9)的次数和原 trace 关系。定义其不含新右尾的局部项
$$
Q_{\rm loc}=A_0gq_A+\frac{A_1}{2}(gq_A'+g'q_A)
+A_2g'q_A'.
\tag{21}
$$
它只使用二阶母 jet 与原二尾。将原
$$
\Phi_M(g,q_A)
=Q_{\rm loc}
+B_0J(g''q_A'')+B_1J(yg''q_A'')
+B_2J(y^2g''q_A''+2g'q_A')
$$
代入原三矩，并用 (14)(15)，得到
$$
\boxed{
\begin{aligned}
B_j[M,A]=\int\big\{&
-\mathfrak P_j[1]\mathscr D Q_{\rm loc}\\
&+(\mathfrak P_j[B_0]+y\mathfrak P_j[B_1]
+y^2\mathfrak P_j[B_2])g''q_A''\\
&+2\mathfrak P_j[B_2]g'q_A'\big\}.
\end{aligned}}
\tag{22}
$$
原有序 $M$ 在 outer 算子、$A$ 在 inner 槽，未对称化。所有新第三右尾已转置，$q_A$ 的原二尾仍在。最高平移次数为 $j+8\le10$。

### 6.2 $G[M,A]$

直接按三矩定义，
$$
\boxed{
G_j[M,A]=\int y^j q_M''q_A''
+\mathbf1_{\{j=2\}}\,2\int q_M'q_A'.}
\tag{23}
$$
$q_A'',q_M''$ 至多线性含 $u'''$。这是原能量的真实 C³ 双线性式，不对其正平方作虚构抵消。平移次数为 $j+8\le10$。

### 6.3 完整速度线性 $\mathscr L$

令
$$
H_1=D\{Q^2(2\gamma pr-e_sr^2)-2h\gamma eQp^2\},
$$
$$
H_2=D\{(\gamma Q-2hee_s)r^2-2h^2\gamma p^2\}.
\tag{24}
$$
由 R221(17)，对第一项 $\mathcal T(q_A;\Delta)$ 将唯一 $q_A'''H_1$ 分部积分，得到
$$
\boxed{
\mathcal T(q_A;\Delta)
=\frac1{32h^4}\int
\{-q_A''\mathscr D H_1
+(Qq_A''-2heq_A'+2h^2q_A)H_2\}.}
\tag{25}
$$
$H_1$ 在每微包两边为零，边界没有要求 $q_A$ 的真尾在微包间归零。

另一项仍直接用
$$
\begin{aligned}
\mathcal T(g;g,q_A)=\frac1{32h^4}\int\big[&
Q^2g'''\{\gamma(g'q_A''+g''q_A')-e_sg''q_A''\}\\
&-2h\gamma eQ\,g'''g'q_A'\\
&+F_g\{(\gamma Q-2hee_s)g''q_A''
-2h^2\gamma g'q_A'\}\big],
\end{aligned}
\tag{26}
$$
其中 $F_g=Qg''-2heg'+2h^2g$。于是
$$
\boxed{\mathscr L=2\mathcal T(q_A;\Delta)-4\mathcal T(g;g,q_A)}
\tag{27}
$$
为明确 C³ 多项式积分，平移次数不超过9。其几何系数对速度一次，可由 (25)(26)准确取 $\lambda_h,\lambda_k$。

真实 $\dot\lambda\cdot A$ 是在固定 $A$ 和固定 profiles 上对全部几何系数作时间导数，使用 $\eta_s=\upsilon/(2h)$、$\gamma_s=a,\upsilon_s=b$；随后另加 $\lambda\cdot M$ 才是 $D_s\mathscr L$。不得漏掉后一变化-profile 项。

## 7. 整个 $\sigma_s$ 的有限 Laurent 分子

R584 的完整中心化第三更新是
$$
\mathcal H=c-B[M,A]+\tfrac12G[M,A]
-e^{(0)}D_s\{\mathscr L/(4w_0)\}.
\tag{28}
$$
所有量都已由 (20)(22)(23)(25)(26)给出，故 (28)既保完整 incoming，也可直接在形式系数层组合。

为避免先求大积分再相减，令
$$
d_g=h\eta-k,\quad q_g=1+d_g^2,\quad
\dot q_g=2d_g(\gamma\eta-\upsilon/2).
$$
因 $4w_0=q_g/h$，
$$
D_s\{\mathscr L/(4w_0)\}
=\frac{(\gamma\mathscr L+hD_s\mathscr L)q_g
-h\mathscr L\dot q_g}{q_g^2}.
\tag{29}
$$
因此可先形成完整三向量分子
$$
\boxed{
\mathcal N=q_g^2\{c-B[M,A]+\tfrac12G[M,A]\}
-e^{(0)}\{(\gamma\mathscr L+hD_s\mathscr L)q_g
-h\mathscr L\dot q_g\},\qquad
\mathcal H=\mathcal N/q_g^2.}
\tag{30}
$$
$q_g\ge1$，除法不会因几何合法盒产生极点。$q_g$ 不含材料坐标，故 (30)不增加十次平移界。

原系数在 $h$ 上只有有限负次幂，其余几何变量及 $A$ 为有限多项式；$D_s\mathscr L$ 及 $c$ 对 $(a,b)$ 至多仿射。于是 (30)有有限 Laurent 系数展开，可以先以准确有理系数做形式平均、合并和系数收集，再预收有限个固定 C³ profile 积分。无需在每个 ODE 节点重新作一遍空间求积，也无需由一组静态数值状态拟合几何系数。

这些生成元可能线性相关；预收不把它们当可控、独立或满秩方向。最终实际函数仍由原式的准确组合确定。

### 对十九态方程的直接意义

R584 当前 ruling 使用
$$
R^0_\pm-4w_\pm\cdot\sigma_\pm-2w_\pm\cdot\bar\nu
$$
及原 $2\times2$ 加速度矩阵。$R^0$ 用 R581 的 C² 积分预收；完整 $(\sigma_\pm)_s$ 用 (30)预收，负侧严格使用原物理速度 $(-\gamma,\upsilon)$、加速度 $(a,-b)$、累计 $JA$ 后对整个导数反号。

这样每次 RHS 的所有项都来自同一母库、同一右锚和同一当前 incoming；没有“只稳定了局部项，仍以旧巨大高项差分更新第三历史”的隐藏缺口。

## 8. 实现与证据边界

固定积分可以用 (10)的六节点参考表示求值，且一份运行的所有分辨率必须保持 R578 母幅、宽度、位置图和完整块锚不变。幅权只按齐次四次身份提出一次，$t,\sigma,\nu,\bar\nu$ 这些已累计全库坐标不再按块乘权。

(20)–(30)给的是新的完整公式；其实际数值求积、系数缓存、十九态求根与端 Jacobian 尚待公开 Actions。不能以 R581 的一个局部状态收敛结果替代这些完整历史读出的精度，也不能以本稿的有限化替代 R584 的八个真实末端方程。

本文不重跑已经支付的 R581 首run，不把本稿未运行的预收写成已有数据。随后直接消费原有限接口，继续同一真实紧尺度路径、全部空间范围、末 germs 和完整第四目标。

### 原来源

- R73：完整 E8 六项式、原 chain 和有序第三累计。
- R221(17)：保真右尾的完整局部三线性配对。
- R521/R523：实际完整块的低阶 ruling、交叉矩与同相位正交平均。
- R578：六变换、六正节点、0…10共同正位置矩与实际不交 collars。
- R581：原局部第四 ruling 的 C² 表达及形式二尾导数。
- R584：可逆中心化第三坐标与十九态双边实际方程。

