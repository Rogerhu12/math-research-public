# R516：纯一阶径向控制的共同17维四次域与原盒曲率分离

2026-11-16。本文从 [R514](R514-complete-fifty-one-ring-controls-and-conditional-seventeen-variable-curvature-fibers.md) 的真实三jet族继续，只作原式和源码纸面分析，没有执行几何、J、求积、符号程序、rank、LP、开发检查或旧实例恢复。

**结论。** 固定值层 $x_0=0$，用同一17系数改变一阶径向jet后，整圈的 $U$ 是仿射函数，$X_{ss}$ 是完整二次函数；其余二阶径向17系数仍只作仿射添加。原 metric 门是两条准确二次不等式，目标形算子第二列的完整门是一个显式四次不等式。它们作用于同一17维原盒投影，不能逐角另选法向。固定这17系数后，剩余曲率与原盒相容性有完整的 support-function 分离判据。本文同时给出连续整圈的法向速度恒等和准确的闭性范围。

## 1. 当前实际边界与本稿的新问题

唯一当前点仍是 [真实接受58](../notes/true57-nonlinear168-original-two-grid-accepted58-20261116.md)。原完整 $168$ 场、$172$ 物理盒、固定 $g,b_0$、高度和新增九个背景坐标均保持其原身份；本文只改变原末三个径向位置的 $u/v$ 系数。

其后一次 ring17 原输出的 root 只读收据为：

- run $\mathtt{43865295208}$，research $\mathtt{133292183126}$，source $\mathtt{35438c143eda961a0fa8836d387d0e537fba43b2}$；
- 两网不可变列最大值分别为 $5.502593686251275$、$5.502593694661017$，未排除 $K=1000/61$；
- 原完整物理盒下的 $18$ 变量有限问题返回 HiGHS status $2$、Infeasible、nit $0$；没有 raw18、dual 或候选；
- 没有后续候选预测或 actual，当前点仍58。

本稿没有重新读取或求解该实例。这个浮点后端状态不是严格不可行证明，也不能归因于未失败的不变列下界。本稿研究的是允许真实 $R_1$ 变化后，怎样得到更准确的共同低阶域和下一构造接口。

以下 $R_0,R_1,R_2$、精确 $W$、原九个 $u$ 角列和八个 $v$ 角列均取 R514 的定义。$R_k^{(j)}(\sigma)=\delta_{kj}$；必须使用原三条样条的全区延拓。固定

$$
x_0=0,\qquad x=x_1\in\mathbb R^{17},\qquad y=x_2\in\mathbb R^{17}.
\tag{1}
$$

这里 $y$只是最高径向jet控制，不是一个新的径向坐标。所有角点、两原角网、原物理盒同时使用这一组 $x,y$。

## 2. 同圈所有必要二jets的有限多项式结构

记原17个标量方向为

$$
m_j(\theta)=\big(\alpha_j(\theta),\beta_j(\theta)\big),
\qquad j=1,\ldots,17,
\tag{2}
$$

前九项只有 $u$ 分量，后八项只有 $v$ 分量；它们是原列，单Q不在增量中。令

$$
A(\theta)=\sum_jx_j\alpha_j(\theta),\qquad
D(\theta)=\sum_jx_j\beta_j(\theta).
$$

在 $s=\sigma$，标量值与所有角向导数不变，而

$$
(u_s,v_s)=(u_{*,s},v_{*,s})+\sum_jx_jm_j,\qquad
(u_{ss},v_{ss})=(u_{*,ss},v_{*,ss})+\sum_jy_jm_j .
\tag{3}
$$

因此 $T,T_\theta,T_u,T_v,T_{uu},T_{uv},T_{vv}$全部在当前58同一个 $(u_*,v_*)$上求值，不随 $x,y$变化。它们仍包含真实相位 $\theta+u_*$和 $c(v_*)=(1+v_*^2)^{-1/2}$，并非圆背景近似。

定义完整角向量

$$
Z_j=T_u\alpha_j+T_v\beta_j,\qquad V_j=a\Pi Z_j,
\tag{4}
$$

$$
\begin{aligned}
L_j={}&2a_s\Pi Z_j\\
 &+2a\Pi\!\left[
 (T_{uu}u_{*,s}+T_{uv}v_{*,s})\alpha_j
 +(T_{uv}u_{*,s}+T_{vv}v_{*,s})\beta_j
 \right],
\end{aligned}
\tag{5}
$$

$$
H_{ij}
=a\Pi\!\left[
 T_{uu}\alpha_i\alpha_j+
 T_{uv}(\alpha_i\beta_j+\beta_i\alpha_j)
 +T_{vv}\beta_i\beta_j
 \right]=H_{ji}.
\tag{6}
$$

所有 $\Pi$均作用完整原角圈。它们不由单轴值、少数 attainer 或局部代数取代。

记原归一二jet

$$
Z_{11,*}=X_{ss,*},\qquad
Z_{12,*}=X_{s\theta,*}/a,\qquad
Z_{22,*}=X_{\theta\theta,*}/a^2 .
$$

完整有限恒等式是

$$
\boxed{
\begin{aligned}
X&=X_*,& T&=T_*,& Z_{22}&=Z_{22,*},\\
U&=U_*+\sum_jV_jx_j,\\
Z_{12}&=Z_{12,*}+\sum_jZ_jx_j,\\
Z_{11}&=Z_{11,*}+\sum_jL_jx_j
          +\sum_{i,j}H_{ij}x_ix_j+\sum_jV_jy_j .
\end{aligned}}
\tag{7}
$$

式(7)中的双重求和按完整有序 $i,j$求和，故非对角项出现两次；不再另乘二。式(6)已保原 $T_{uv}$交叉项。

证明由原
$X_{ss}=a_{ss}\Pi T+2a_s\Pi T_s+a\Pi T_{ss}+b_se_3$
和完整链式直接得到。因 $R_1(\sigma)=0$，$T$不变；因 $R_1''(\sigma)=0$，最高标量二jet只由 $y$添加，但 $T_{ss}$中的 $u_s^2,u_sv_s,v_s^2$仍产生(6)。原高度 $b,b_s$不变，已经保在基点项中。

**计算范围的含义。** (7)是准确有限二次式，不是二阶Taylor截断。在未来同一明确账户中支付其必要完整系数后，任意新 $x,y$的同圈评价可用多项式收缩，不必每次重做当前 scalar frame 或17个完整 $\Pi$。这不意味着系数目前都已保存或可以免费重建；第11节专门说明原输出缺口。

## 3. 原172盒对一阶17变量的准确投影

对每个原角模式 $j$，令三个末径向物理系数的增量为 $c_j\in\mathbb R^3$。固定 $x_0=0$给

$$
c_j=W_{\cdot1}x_j+W_{\cdot2}y_j,\qquad
\nu_0\cdot c_j=0,\qquad
\nu_k=\big(\mathcal B_9^{(k)}(\sigma),
           \mathcal B_{10}^{(k)}(\sigma),
           \mathcal B_{11}^{(k)}(\sigma)\big).
\tag{8}
$$

并且 $x_j=\nu_1\cdot c_j,\ y_j=\nu_2\cdot c_j$。三jet矩阵可逆，所以(8)完整参数化该真实二维平面；不是丢掉第三个系数。

设由当前物理点减去原盒端点得到

$$
l_j\le c_j\le u_j.
$$

若未来任务另明确 $h\le h_{\max}<\infty$，才再逐项与
$[-h_{\max}/4,h_{\max}/4]$相交。本文不默加 $1/128$，也不改变原盒。定义

$$
\mathcal C_j=\{c\in\mathbb R^3:l_j\le c\le u_j,\ \nu_0\cdot c=0\}.
\tag{9}
$$

原盒有限，故每个非空 $\mathcal C_j$为紧凸多边形，允许线段或单点。其一阶投影准确是

$$
J_j=[\underline x_j,\overline x_j],\quad
\underline x_j=\min_{c\in\mathcal C_j}\nu_1\cdot c,\quad
\overline x_j=\max_{c\in\mathcal C_j}\nu_1\cdot c.
\tag{10}
$$

这两个端点可以不引入一般三维求解器而写成有限原式：选一个 $\nu_{0,k}\ne0$的自由坐标，另两个坐标各取自己的原下界或上界，再令

$$
c_k=-\frac{\sum_{\ell\ne k}\nu_{0,\ell}c_\ell}{\nu_{0,k}} .
\tag{11}
$$

保留落在全部原区间中的候选。至多 $3\times4=12$个候选，允许重复；在它们上取(10)的最小最大。因为一个盒与非零超平面的有界截面，其顶点至少有两个独立盒面活跃，故这些候选覆盖全部顶点。原三jet可逆保证 $\nu_0\ne0$。有零宽盒时仍保其相等约束；不除以零的 $\nu_{0,k}$。若原端点顺序错误或没有可行候选，就按空域处理。

由各模式的真实物理坐标分离，

$$
\mathcal J_1=\prod_{j=1}^{17}J_j
\tag{12}
$$

正是原物理盒在纯 $R_1$变量上的投影。它包含的含义仅为：每个 $x\in\mathcal J_1$至少有一个 $y$使物理盒成立。**它不说明这个 $y$满足曲率、metric以外的门或全部body门。**

固定 $x$后，真实可用的 $y$域是

$$
\mathcal Y(x)=
 \left\{y:\ l_{\ell j}-W_{\ell1}x_j
              \le W_{\ell2}y_j
              \le u_{\ell j}-W_{\ell1}x_j
 \right\}
 =\prod_j[L_j(x),U_j(x)] .
\tag{13}
$$

按 $W_{\ell2}$正负分别除并交换端点，零系数保原常数不等式。这与R514一致。若某个区间为空，先直接判该 $x$不可行；后面的 support function 不在空域上假定义为普通有限值。非空时各区间有限且可为零宽。

式(11)–(13)是纸面公式，没有执行12个枚举或任何原盒数值查询。

## 4. 当前17坐标上的原metric二次门

以下固定一个原角点；所有系数取同一个当前58和同一个网。令

$$
U(x)=U_*+\sum_iV_ix_i,\quad
T=T_*,\quad
F(x)=F_0+\sum_if_ix_i,\qquad f_i=V_i\cdot T,
$$

$$
E(x)=E_0+2\sum_i e_ix_i+\sum_{i,j}E_{ij}x_ix_j,
\quad e_i=U_*\cdot V_i,\quad E_{ij}=V_i\cdot V_j,
\quad G=T\cdot T>0.
\tag{14}
$$

原实际 metric 定义保持

$$
\eta=\frac{|E-1|+\sqrt{(E-1)^2+4F^2}}2 .
$$

给定明确目标 $\varepsilon\in(0,1)$，不用变量除法的准确两门为

$$
\boxed{
H_+(x)=\varepsilon(1+\varepsilon-E(x))-F(x)^2\ge0,
\qquad
H_-(x)=\varepsilon(E(x)-1+\varepsilon)-F(x)^2\ge0 .
}
\tag{15}
$$

这等价于 $\eta\le\varepsilon$，没有为浮点 $G-1$另造原metric门。

写 $d=E-F^2/G$。式(15)还准确等价于

$$
|F|\le\varepsilon,\qquad
1-\varepsilon+\left(\frac1\varepsilon-\frac1G\right)F^2
 \le d\le
1+\varepsilon-\left(\frac1\varepsilon+\frac1G\right)F^2 .
\tag{16}
$$

证明只把 $E=d+F^2/G$代回(15)；两端之差为
$2\varepsilon-2F^2/\varepsilon$。这显示metric同时限制平行分量 $F$和垂直幅度 $\sqrt d$，不能任意旋转法向后自由另选径向幅度。

若 $G\ge\varepsilon$，则 $d\ge1-\varepsilon>0$，
$q^2=Gd\ge G(1-\varepsilon)$。这是准确同一内积下的实数结论；实际normal-area门及其原容差仍独立保留。

要求全body相对58严格下降时，可将 $\varepsilon$设为已声明的
$\eta_{58}-\delta_\eta$，但这里只得到本圈必要门。当前58的全网metric峰位于 $.4725$，不能由峰位置直接推断本圈尚有多少可用余量。

## 5. 保实际G且无变量除法的完整四次曲率门

仍固定一个角点，设

$$
\begin{aligned}
w(x)&=U(x)\times T=w_0+\sum_iw_ix_i,&w_i&=V_i\times T,\\
Q(x)&=w(x)\cdot w(x),\\
c(x)&=w(x)\cdot Z_{22,*},\\
b(x)&=G\,w(x)\cdot Z_{12}(x)-F(x)c(x).
\end{aligned}
\tag{17}
$$

$Q$为二次，$c$为一次，$b$为二次，均直接取原归一二jets。这里 $b(x)$是本节曲率分子，不是冻结高度速度；后者仍记 $b_*$。

必须保 $Q>0$。由R514的真实正交形算子，直接化简得

$$
B(x)=\frac{b(x)}{GQ(x)},\qquad
C(x)=\frac{c(x)}{G\sqrt{Q(x)}} .
\tag{18}
$$

原 $Z_{12}=X_{s\theta}/a$、$Z_{22}=X_{\theta\theta}/a^2$已经保尺度。若改用 $T_s,T_\theta$，则对应分子为
$aG\,w\cdot T_s-F\,w\cdot T_\theta$和 $w\cdot T_\theta$，分母也必须同时补相应 $a$；不能只改分子。

对于任意 $K>0$，

$$
\boxed{
 B(x)^2+C(x)^2\le K^2
 \quad\Longleftrightarrow\quad
 P_K(x):=G^2K^2Q(x)^2-b(x)^2-c(x)^2Q(x)\ge0 ,
 \qquad Q(x)>0 .
}
\tag{19}
$$

这是同一17坐标的完整四次门，不是只保 $C$，也不是将 $B$独立设零。所有角点必须使用相同 $x$。它不含 $Q$或 $K\pm C$的变量除法，亦没有把实际 $G$设成1。

### 5.1 全部坐标系数

令

$$
\begin{aligned}
q_0&=w_0\cdot w_0,&q_i&=w_0\cdot w_i,
 &Q_{ij}&=w_i\cdot w_j,\\
c_0&=w_0\cdot Z_{22,*},&c_i&=w_i\cdot Z_{22,*}.
\end{aligned}
$$

并定义

$$
\begin{aligned}
b_0={}&G\,w_0\cdot Z_{12,*}-F_0c_0,\\
b_i={}&G(w_i\cdot Z_{12,*}+w_0\cdot Z_i)-f_ic_0-F_0c_i,\\
B_{ij}^{\rm pol}={}&
 \frac G2(w_i\cdot Z_j+w_j\cdot Z_i)
 -\frac12(f_ic_j+f_jc_i).
\end{aligned}
\tag{20}
$$

于是

$$
Q=q_0+\ell_q+Q_2,\quad
b=b_0+\ell_b+B_2,\quad c=c_0+\ell_c,
$$

$$
\ell_q=2\sum_iq_ix_i,\quad Q_2=\sum_{i,j}Q_{ij}x_ix_j,\quad
\ell_b=\sum_ib_ix_i,\quad B_2=\sum_{i,j}B_{ij}^{\rm pol}x_ix_j,\quad
\ell_c=\sum_ic_ix_i .
\tag{21}
$$

用 $k_0=G^2K^2$，式(19)的各齐次次数完整为

$$
\begin{aligned}
P^{[0]}={}&k_0q_0^2-b_0^2-c_0^2q_0,\\
P^{[1]}={}&2k_0q_0\ell_q-2b_0\ell_b-c_0^2\ell_q-2c_0q_0\ell_c,\\
P^{[2]}={}&k_0(\ell_q^2+2q_0Q_2)-(\ell_b^2+2b_0B_2)\\
 &-c_0^2Q_2-2c_0\ell_c\ell_q-q_0\ell_c^2,\\
P^{[3]}={}&2k_0\ell_qQ_2-2\ell_bB_2-2c_0\ell_cQ_2-\ell_c^2\ell_q,\\
P^{[4]}={}&k_0Q_2^2-B_2^2-\ell_c^2Q_2,\qquad
P_K=\sum_{r=0}^4P^{[r]} .
\end{aligned}
\tag{22}
$$

所以(19)可以只用真实当前向量点积与(4)的固定列形成明确多项式。式(20)的 $1/2$只是常数对称化；没有除以任何候选相关量。

若 $P_K<0$，该角点直接排除这个 $x$的全部 $y$。反之 $P_K\ge0$仅保证该点在允许第一个形算子对角元任意变化时可完成；它没有消去共同 $y$和原盒。

## 6. 连续整圈的新几何解释：法向曲线的速度

本节只对完整连续原式求 $\theta$导数，不把有限FFT数组的差分假作该导数。

设

$$
\widehat T=T/\sqrt G,\quad t=F/G,\quad
R=\sqrt{E-F^2/G},\quad e=(U-tT)/R,\quad n=e\times\widehat T .
\tag{23}
$$

真实原 jets 满足
$U_\theta=a_sT+aT_s$。用
$U=Re+tT$，与正交化中的 $tZ_{22}$相减，得到

$$
\boxed{
 B=\frac{n\cdot e_\theta}{a\sqrt G},\qquad
 C=\frac{n\cdot\widehat T_\theta}{a\sqrt G},\qquad
 B^2+C^2=\frac{|n_\theta|^2}{a^2G}.
}
\tag{24}
$$

证明中 $R_\theta e$与 $t_\theta T$均被 $n$正交杀掉，$tT_\theta$则与原混合项准确抵消。最后 $e,\widehat T,n$为正交标架，故
$n_\theta\cdot e=-n\cdot e_\theta$、
$n_\theta\cdot\widehat T=-n\cdot\widehat T_\theta$、
$n_\theta\cdot n=0$，即得平方和。此链式已获另一代理的窄纸面独核，范围只限连续分解，不扩大到列实现、原盒或离散FFT等价。

因此(19)在连续圈上等价于

$$
|n_\theta|\le a\sqrt G\,K .
\tag{25}
$$

目标并非只限制法向在每个角点可以转多少，而是同时限制它在整圈怎样转。任意两角点还必须满足球面距离界

$$
{\rm dist}_{S^2}\big(n(\theta_1),n(\theta_2)\big)
 \le K\int_{\theta_1}^{\theta_2}a\sqrt G\,d\theta
\tag{26}
$$

（选所用有向弧；两个方向分别有效）。这是共同曲率门的必要条件，不允许逐角另选互不相容的法向。

但不能据(25)任意设计一条法向曲线。还必须有同一 $x$使

$$
U=U_*+\sum_jV_jx_j,\qquad
\frac1{2\pi}\int_0^{2\pi}U\,d\theta=b_*e_3 ,
\tag{27}
$$

以及(15)、(16)、原盒。式(27)的均值约束来自每个 $\Pi Z_j$的真零均值；完整实际高度被保留。给定任意小速度法向再自由选择 $F,R$，一般不满足这些共同17列与全局均值。

有限两网可直接用(17)–(22)和原 $Z_{12},Z_{22}$，无需对数组作 $\theta$差分。离散谱导数、连续导数及原直接jets的浮点差异不能由(24)抹去。

## 7. 比逐项必要界更强的共同低阶域

给定原角集合 $\Theta$，定义

$$
\begin{aligned}
\mathcal D_{K,\varepsilon}=\{x\in\mathcal J_1:\ 
&H_+(x;\theta)\ge0,\ H_-(x;\theta)\ge0,\\
&Q(x;\theta)>0,\ P_K(x;\theta)\ge0
\quad\hbox{对所有 }\theta\in\Theta\}.
\end{aligned}
\tag{28}
$$

它是同一17参数域；有限 $\Theta$时明确由线性盒、二次门和四次门组成。不能把每点各自非空的集合分别选一个 $x$后称其交集非空。若该共同域为空，纯 $R_1/R_2$族已被排除，无须追做最高层。

原mirror也可在本圈保成二次式：

$$
X_{*,3}(\theta)^2Q(x;\theta)
 -\tau_m^2\,w_3(x;\theta)^2\ge0,
\tag{29}
$$

连同原 normal-area 门一起加入(28)。它需要真实 $X_{*,3}$；若该完整圈位置尚未保存，不能从仅有 $U/T$补造。位置型高度、ball、strip在准确 $x_0=0$族的本圈保持原值，但全body不因此保持。

连续精确frame中 $G=1$；在更一般的实际G公式下，若各点 $G\ge\varepsilon$，则(15)已经给一致的正面积下界。有限盒与连续固定系数此时使(28)成为闭有界域；若只保 $Q>0$而没有统一正下界，不能无条件声称该低阶域紧。原actual仍保独立regularity及原浮点容差。

(28)还不是全部环曲率可行域：它允许每个角点有一个独立的第一个对角元完成。下一节保共同最高17系数，使这一缺口精确可审。

## 8. 固定一阶态后的原盒 support-function 充要条件

固定一个真实 $x$，先要求(13)非空。用(7)取得 $y=0$的完整形算子 $A^x,B^x,C^x$，并定义

$$
\ell_j^x(\theta)=\frac{n(x;\theta)\cdot V_j(\theta)}
 {E(x;\theta)-F(x;\theta)^2/G(\theta)} .
\tag{30}
$$

最高层满足 $A=A^x+\sum_j\ell_j^xy_j$，$B,C$不变。四条准确曲率行直接写成

$$
\begin{aligned}
2K+A^x+C^x+\ell^x\cdot y&\ge0,\\
(K+C^x)(K+A^x+\ell^x\cdot y)-(B^x)^2&\ge0,\\
2K-A^x-C^x-\ell^x\cdot y&\ge0,\\
(K-C^x)(K-A^x-\ell^x\cdot y)-(B^x)^2&\ge0.
\end{aligned}
\tag{31}
$$

将它们逐项整理为
$r_\alpha(x)\cdot y\le d_\alpha(x)$。
不用除以 $K\pm C$，所以 $|C|=K$、$\ell=0$等退化情形都保原常数行。若要使用原 raw PSD 行和原数值行尺度，应沿原 $qI\pm K^{-1}\mathcal K$形成仿射行，不把(31)的单位阵尺度容差冒作旧行容差。

对非空有限盒 $\mathcal Y(x)=\prod_j[L_j,U_j]$，其 support function为

$$
h_{\mathcal Y}(v)=\sum_j\big(v_j^+U_j+v_j^-L_j\big),
\qquad v_j^+=\max(v_j,0),\quad v_j^-=\min(v_j,0).
\tag{32}
$$

设有限角网的行矩阵为 $\mathsf R(x)$、右端为 $d(x)$。则有完整等价：

$$
\boxed{
\exists y\in\mathcal Y(x):\mathsf R(x)y\le d(x)
\quad\Longleftrightarrow\quad
\lambda^{\mathsf T}d(x)
 +h_{\mathcal Y(x)}\!\left(-\mathsf R(x)^{\mathsf T}\lambda\right)
 \ge0\quad\text{对所有 }\lambda\ge0 .
}
\tag{33}
$$

**必要性。** 对任一可行 $y$，
$\lambda^{\mathsf T}\mathsf Ry\le\lambda^{\mathsf T}d$；
左边在盒上的最小值是
$-h_{\mathcal Y}(-\mathsf R^{\mathsf T}\lambda)$。

**充分性。** 若有限行与盒无交，紧盒上
$\min_y\max_\alpha(r_\alpha\cdot y-d_\alpha)>0$。
有限单纯形与紧凸盒的线性 minimax给一个
$\lambda\ge0,\sum\lambda_\alpha=1$，使(33)左边严格小于零。这就是真实有限分离，不需要Slater条件，也不要求盒有内点。

因此零宽区间完全允许。空盒则在此前已经失败，不能仍套(32)；原盒若无界，下面的连续圈论证也不能照搬。

**严格排除证据。** 一个明确非负 $\lambda$连同真实原行、原盒端点，若以精确或有向运算得到

$$
\lambda^{\mathsf T}d+
 h_{\mathcal Y}(-\mathsf R^{\mathsf T}\lambda)<0,
\tag{34}
$$

才是该固定一阶态的严格有限不相容证据。式(34)会联合多个角点和原盒；所有单点不变列通过仍可能失败于它。只报后端 Infeasible、没有返回乘子，不能宣称(34)已经支付。本文没有追算原ring17实例或替其补乘子。

## 9. 连续圈的闭性、有限见证及不能越过的边界

固定 $x$，假设真实 $Q$在整圈有正下界、各原系数连续，且 $\mathcal Y(x)$非空紧。每个角点的四条(31)给盒内闭集。

如果连续全圈的共同交集为空，紧性使某个有限角点、有限行子族的交集已经为空。再对该有限子族使用(33)，便有一个有限支撑的严格证据(34)。反之，全圈可行当然使每个这样的有限非负组合均非负。

所以连续圈的完整准则是：对**所有有限支撑的非负角行组合**满足(33)。这不是只检查既有粗细网，也不需要先假设乘子有密度。原两有限网通过仍不能授予连续所有角点；未来若只支付有限网，就只报告该范围。

有界条件不能省。例如一个无界变量上的无限族 $y\ge n$各有限子族可行但整体无交；本题避免该问题的来源是真实有限物理盒，不是形式上写了一个norm变量。零宽盒不妨碍紧性和证明。

综合(28)、(33)，完整纯 $R_1/R_2$环问题可写为：

1. 一个共同 $x$在原盒的准确投影及所有metric、normal/mirror、四次列门中；
2. 同一个 $x$对应的实际剩余盒 $\mathcal Y(x)$与全角共同曲率行满足(33)。

第1项为空可直接排除这个族；第1项非空仍要第2项。任何一个角点各自可选 $x$、或仅证每个 $x$有某个盒内 $y$，均不足以替代这个共同问题。

## 10. 下一真实构造可以利用什么，而不作盲目的全51搜索

这组公式给出的可执行顺序是结构性的，而不是新增一次已运行的算法：

- 从真实原盒准确投影出 $\mathcal J_1$，不任意指定17个独立新trust半径；
- 在同一当前frame上形成(4)及基点 $U,T,Z_{12},Z_{22}$，得到全部二次metric与四次列门；
- 只有通过共同低阶门的 $x$，才需要(5)–(7)的完整 $A^x$及共同最高层；
- 对固定 $x$，保原盒和(31)，必要时由(34)定位是哪些角行与哪些物理面共同冲突，而不是重解原 $x=0$实例；
- 一个真实新候选仍须完整body非线性预测与原两网14门，不能把本圈成功当reach或实际接受。

尤其(7)使所有新的低阶环态共享同一批当前frame偏导和完整 $\Pi$系数。它们不需要不断恢复ordinary或重做当前全168 J。若不选择预存全部 $H_{ij}$，也可在明确的新账户内对一个实际选定 $x$直接收缩原完整二次角函数再作 $\Pi$；这是真实新候选评价，费用仍记录，不冒已存全表。

本文尚未构造当前58的一个可行非零 $x$，也没有给当前实例的(34)。它给的是能直接形成下一小问题的完整原式，而非将不足的数值状态改名为几何排除。root后续必须以真实新的低阶态或严格分离问题定范围，不能重开已经结束的ring17。

## 11. 原已付数据可以复用到哪里

原 ring17 MODEL1保存了整圈 $U,T$、归一一/二jets、实际 $I/II/G/q$、形算子 $A/B/C$、normal和已收缩的 $\ell$等原数组。它们可按原来源直接用于基点，不重新求当前ordinary。

但是原源码
[frame_metric_current168_ring17.py](../scripts/frame_metric_current168_ring17.py)
中的成功输出有一项明确边界：

- 函数 $\mathtt{\_ring\_ell}$在运行中形成
  $\mathtt{ring\_Tss\_columns}$ 和
  $\mathtt{ring\_Tss\_primitives}$；
- $\mathtt{full\_record()}$保存 $\ell$和这些数组的身份hash；
- 成功记录的 $\mathtt{build\_cost}$经 $\mathtt{\_public}$排除私有 $\mathtt{\_arrays}$，没有保存完整三向量 $V_j$的数值。

因此已付 $\ell_j=n_*\cdot V_j/d_*$只给一个法向收缩，不能恢复 $V_j$的另外两个分量，也不能据此宣称纯R1所需完整kernel已经可读。式(4)的 $V_j$恰是原计算经过的向量，但“经过计算”与“成功stdout保留了其值”不同。

下一明确的新R1模型如需这些未保存的向量，必须如实列必要来源及恢复成本；不能把hash当数值，不得为观测而重跑原R2 LP。新(5)、(6)更是尚未支付的完整二次系数。原当前点、物理盒、精确样条嵌入和原已存圈数组则应直接复用，不重复旧检查。

对(29)需要的完整圈 $X_{*,3}$、实际height来源，也遵循同样原则。原58 selected缓存不是整圈位置缓存；缺失输入不能用零或一个标量门收据冒充。

## 12. 精确参数族与实际候选范围

(7)、(15)、(19)、(24)、(33)首先是准确实数族及同一原算子的陈述。它们不把二进制点积、FFT或浮点LP残差自动升级为严格数值证书。实际 $G$、原cross面积以及
$Q-(EG-F^2)$的浮点差应保留真实记录，不能静默消成零。

精确 $W_{\cdot1}x+W_{\cdot2}y$经逐坐标binary64舍入后，实际168坐标可能不再准确满足 $x_0=0$。必须保存未舍入嵌入、实际168/172、原盒/物理norm及舍入差，并对真正候选用完整场重新预测、原ordinary验收。原14门和严格eta下降没有被本圈四次门取代。

前102列可以不动此圈而改变中段，但仍与末三样条完整重叠；R514的有限混合项继续存在。本文未将其当成免费的全body修复，也未声称固定 $g$达到目标曲率或原reach已经构造完成。

本稿完成的是：纯R1共同17坐标的完整二次jet表、原盒准确投影、无变量除法四次列门、连续法向速度身份、以及剩余原盒曲率问题的严格分离准则。它让下一真实问题有明确低阶域、真实输入缺口和可审失败证据；当前58是否在原盒内可由这一族得到所需改善仍是下一未完成问题。
