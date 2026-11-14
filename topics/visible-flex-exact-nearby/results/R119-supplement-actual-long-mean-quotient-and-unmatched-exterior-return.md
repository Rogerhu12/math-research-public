# R119 续篇：实际长段 mean 商、未拼平界面与完整外返回图

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇继续
[真实未覆盖负分量及外两端口](R119-supplement-actual-uncovered-negative-bridge-and-complete-exterior-root-two-port.md)。
保留其真实 $e_X$、cut128、$C$、$B$，另将原长径向段的帽侧端点记为
$A$。这里 $B$ 仍是长段 $t=0$，$A$ 是 $t=L$；不把两个端点改名成同一个口。

在已经构造的实际 tail/connector 和实际非线性长段上，先解长段
Jacobi 的完整正定问题。两端非mean高度给定，整体高度只有一个
gauge；外 mean 高度是输出，mean 通量是自然边界荷。然后准确支付
两背景在 $B$ 尚未匹配的 $\mu,d$ 差及 holonomy 的有限秩行。

所得外返回图作用在全部 $L^2(e_X)$ 波输入上。与同一实际系数的
自伴拼接比较，非自伴差由真实斜率残差控制。本文没有把这条反射
称作 $I-\mathcal E_a\mathcal T_a$ 已可逆，也不把原强标签权从开放
内部逆免费转授。帽侧数据、ordinary/weak 源、两 mean 和参数列仍
按下文的实际接口保留。

## 1. 同一长段与完整 raw Jacobi 系数

使用[实际长段 Dirichlet 定理](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md)
(D.1)--(D.13),(D.23)--(D.28) 的真实解，及
[固定停止完整源定理](R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md)
(D.30)--(D.36) 的同一实际接口。记

$$
 t=\log(a/a_B),\quad 0\le t\le L,\qquad
 a=a_Be^t,\quad w=a/(4\omega),\quad \mu_0=w/a=1/(4\omega),
$$
$$
 1<L<2^{25},\qquad 1/6<\mu_0<1/4,\qquad
 \|h_{\mathrm{long}}\|_{\mathcal Y_\sigma}\le2^{-20},
 \quad \sigma\ge1/16.                                   \tag{R.1}
$$

$h_{\mathrm{long}}=v_\perp/(aw)$ 是原非线性长段的归一化高度，
不是下面的 raw Jacobi 高度 $H=\dot v$。北帽物理高度为 $Z_0-v$；
如改用 $\dot Z$，全部状态、标签和源同时取反。

沿原实际背景，记 $P,U,K,V$ 为长段 (D.6)--(D.9) 的相对变量，
包括 $K$ 的真实 mean 小根，并令

$$
 E=1+w^2,\quad J=1+K+EU,\quad
 \mathfrak d=1-w^2(2K+K^2+EP^2),\quad
 N=\|P\|_{A_\sigma}+\|U\|_{A_\sigma}
       +\|K\|_{A_\sigma}+\|V\|_{A_\sigma}<2^{-18}.
$$

完整固定度量 Jacobi 方程采用同一
[物理 Hamiltonian 及 weak 源](R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md)
(J.2)--(J.5)：

$$
 \operatorname{div}(G\nabla H)=g-\operatorname{div}F,\qquad
 \pi=\mu(H_t-dH_\theta)+F^t,
$$
$$
 G=\mu\begin{pmatrix}1&-d\\-d&d^2+v^2\end{pmatrix},\quad
 \mu=\mu_0J\mathfrak d^{-3/2},\quad
 d=E(V-P)/J,\quad v=\sqrt{\mathfrak d}/J .                \tag{R.2}
$$

这里长段 $Q=-1$，所以 $G$ 正定。准确地，

$$
 \frac{G}{\mu_0}=
 \begin{pmatrix}
 J\mathfrak d^{-3/2}&-E(V-P)\mathfrak d^{-3/2}\\
 -E(V-P)\mathfrak d^{-3/2}&
 \dfrac1{J\sqrt{\mathfrak d}}+
 \dfrac{E^2(V-P)^2}{J\mathfrak d^{3/2}}
 \end{pmatrix}.                                         \tag{R.3}
$$

由 $|J-1|\le2N$、$|\mathfrak d-1|<3N$，在同一绝对幂级数中
分别估计倒数和平方根，得到

$$
 \|G/\mu_0-I\|_{A_\sigma;2\times2}<64N<2^{-12}=:\varepsilon .
 \tag{R.4}
$$

例如第一、交叉、第二对角条目与参考之差依次小于 $12N,3N,10N$；
64 同时支付矩阵 norm 和全部复 Fourier 乘积。
对实背景，$(1-\varepsilon)\mu_0I\le G\le
(1+\varepsilon)\mu_0I$。复角平移 $|\operatorname{Im}\tau|<1/128$
仍在原 $A_\sigma$ 域内，整个复型的实部至少为参考能量的一半。
这给真实角交换子所需的全纯域，并非对实点界作复化猜测。

## 2. 自然 mean 条件与唯一整体高度

先取 $F=g=0$。固定两个非mean高度

$$
 \Pi_\perp H(0)=f,\qquad \Pi_\perp H(L)=f_*,
 \qquad \langle H(0)\rangle=\lambda,\qquad
                  \langle\pi(L)\rangle=0 .             \tag{R.5}
$$

最后一行是自然 mean 通量条件。它不是给外端再指定一个 mean 高度。
原 holonomy 恒等式 (J.23)--(J.24) 准确给
$DM[\dot v]=\langle\pi-F^t\rangle$；因而在齐次固定目标方向上，
(R.5) 正是原 $M=1$ 小根的线性化。

令 $\mathcal V$ 为 $H^1([0,L]\times\mathbb T)$ 中
$U(0)=0$、$\Pi_\perp U(L)=0$ 的空间。型

$$
 a_L(U,V)=\int_0^L\langle G\nabla U,\nabla V\rangle\,dt
                                                               \tag{R.6}
$$

在 $\mathcal V$ 上强制；$U(L)$ 的 mean 是自由测试变量。
Lax--Milgram 给唯一 (R.5) 解。常高度 $\lambda$ 不改变型或通量。
对光滑数据，积分分部恢复完整方程及自然 mean 条件；一般数据
由同一型闭包给出，而不是另求一个投影方程。

在实际全纯长段 Dirichlet 图上微分得到的 $H$ 满足 (R.5)，
因此由上述唯一性与本解相同。它含原 mean 小根的导数，未另造
一个不同的 elliptic 背景。两个端点 mean 高度仍只有一个自由量。

## 3. 两端非mean DN 与准确径向参考

定义

$$
 \mathcal N_L(f,f_*)=
 \bigl(-\Pi_\perp\pi(0),\,\Pi_\perp\pi(L)\bigr),\qquad
 \mathscr B(f,f_*)^2=\sum_{m\ne0}|m|(|f_m|^2+|(f_*)_m|^2).
                                                               \tag{R.7}
$$

$\mathcal N_L$ 是
$\dot H^{1/2}\oplus\dot H^{1/2}$ 到其对偶的完整自伴正算子，
保留当前非径向卷积。它的二次型是 (R.6) 在相应 Dirichlet 类上的
最小值。

径向参考的 mean 为常数，且非mean完整矩阵为

$$
 (\mathcal N_{L,0})_m
 =\mu_0|m|
 \begin{pmatrix}
 \coth(|m|L)&-\operatorname{csch}(|m|L)\\
 -\operatorname{csch}(|m|L)&\coth(|m|L)
 \end{pmatrix},\qquad m\in4\mathbb Z\setminus\{0\}.       \tag{R.8}
$$

其两个特征值为 $\mu_0|m|\tanh(|m|L/2)$ 和
$\mu_0|m|\coth(|m|L/2)$。因此

$$
 \frac1{16}\mathscr B^2
  <\langle\mathcal N_L(f,f_*),(f,f_*)\rangle
  <\mathscr B^2,\qquad
 (1-\varepsilon)\mathcal N_{L,0}
 \le\mathcal N_L\le(1+\varepsilon)\mathcal N_{L,0}.       \tag{R.9}
$$

最后的形式不等式来自对每个同一 Dirichlet 类分别最小化 (R.4)。
它不把真实 DN 逐模对角化。特别 $\mathcal N_{BB}$ 对非mean
$B$ 数据有同一 $1/16$ 下界，完整 cross $\mathcal N_{BA}$ 不为零。

原强数据的物理单位准确为

$$
 f= a_Bw_B\,\dot f_B,\qquad
 f_*=a_*w_*\,\dot f_*,\qquad
 H_t(B)=a_Bw_B\,\dot K_B .                              \tag{R.10}
$$

在径向齐次情形，把 (R.8) 的首行除以 $\mu_0a_Bw_B$ 得到

$$
 \dot K_{B,\perp}
 =-|D|\coth(L|D|)\dot f_B
   +|D|e^{2L}\operatorname{csch}(L|D|)\dot f_* .         \tag{R.11}
$$

这恰是固定停止篇 (D.7),(D.29) 的 $-\mathsf C_L$ 和
$\mathsf S_L$，包括有限长反射。$e^{2L}$ 来自真实高度单位比，
没有被估成1。mean 上没有新增 $1/L$ Robin 行。

## 4. ordinary/weak 源、两 mean 输出及裸端荷

允许给定总 mean 通量 $q_A=\langle\pi(L)\rangle$。
对 $g,F\in L^2$，在 $\mathcal V$ 上的准确右端是

$$
 a_L(H,V)
 =q_A\,\overline{\langle V(L)\rangle}
   -\int_0^L\langle g,V\rangle\,dt
   -\int_0^L\langle F,\nabla V\rangle\,dt .             \tag{R.12}
$$

非zero Dirichlet 数据先作同一 lift。所有符号来自
$\operatorname{div}(G\nabla H+F)=g$。
记

$$
 \mathfrak S_L=L\|g\|_{L^2}
       +\|F\|_{L^2}+\sqrt L\,|q_A| .
\tag{R.13}
$$

因 $\|V\|_{L^2}\le L\|V_t\|_{L^2}$、
$|\langle V(L)\rangle|\le\sqrt L\|V_t\|_{L^2}$，
以及 $G>I/8$，零 Dirichlet source 解满足
$a_L(H,H)^{1/2}<4\mathfrak S_L$。
两端非mean仿射荷 $(\ell_B,\ell_A)$ 由同一 Green 配对定义，
且

$$
 \|(\ell_B,\ell_A)\|_{\dot H^{-1/2}\oplus\dot H^{-1/2}}
 <8\mathfrak S_L .
\tag{R.14}
$$

可直接以 (R.7) 的齐次解作测试：其能量小于 $\mathscr B$，
完整 $L^2$ norm 小于 $4L\mathscr B$，外 mean 高度小于
$3\sqrt L\,\mathscr B$。这同时证明源行的范数和其真实单位。

两个 mean 的准确输出为

$$
 q_B:=\langle\pi(0)\rangle=q_A-\int_0^L\langle g\rangle\,dt,
\qquad
 \langle H(L)\rangle-\lambda
 =\int_0^L\left\langle
       dH_\theta+\mu^{-1}(\pi-F^t)\right\rangle dt .
                                                               \tag{R.15}
$$

这些式子保留非mean乘积。源导致的平均高度差小于
$12\sqrt L\,\mathfrak S_L$；齐次边界部分可用
$3\sqrt L\,\mathscr B$。不把任何一个 mean 输出设为0。

对真实 holonomy 方向，端点要求是
$q_A-\langle F^t_A\rangle=DM_A$，另有 metric 的直接变分荷时
把该已知荷一起保留。内部 $L^2$ 或测度 norm 不自动给出裸
$F^t_A,F^t_B$ 迹。带 atom 的强源先按真实 height/flux 跳分段，
使用单侧迹和 BV 解；不得将高度跳的 $H$ 冒作连续能量解。

更一般的 weak 数据仍可在 (R.12) 的真实连续泛函域内消费。
本文给出的 $L^2$ 门是一个明确充分域，不声称任意 raw 源在
grounded/normal 变换下保持同范数。

## 5. 未拼平的两背景：先核同一物理量

现在取 $B$ 两侧已经构造的 tail/connector 背景 $T$ 与长段背景
$L$。它们具有同一目标、同一物理半径和角、同一非mean高度 $f_B$。
用唯一高度平移对齐其 mean 高度，所以 $P,U$ 在 $B$ 相同。
归一化径向斜率仍可能不同，记

$$
 R_B=K_{T,\perp}-K_{L,\perp},\qquad
 \mathfrak r=\|R_B\|_{\dot A^1_\sigma}.                \tag{R.16}
$$

两侧各自满足同一个完整 $M=1$ 小根。固定 $P,U$ 时，原 holonomy
的准确导数为

$$
 D_KM[\dot K]=w^2\langle J\mathfrak d^{-3/2}\dot K\rangle .
                                                               \tag{R.17}
$$

这个恒等式可由原积分式直接微分；其系数就是 $\mu/\mu_0$。
沿两个小根之间的同一小球积分，利用
$\|J\mathfrak d^{-3/2}-1\|<12N$，得
$|K_{T,0}-K_{L,0}|<24N\|R_B\|_{A_\sigma}$。所以

$$
 \|K_T-K_L\|_{A_\sigma}
  +\|\partial_\theta(K_T-K_L)\|_{A_\sigma}<2\mathfrak r .
                                                               \tag{R.18}
$$

没有把原非mean残差直接当成完整 mean 残差。这里 $w^2$ 在
隐函数导数的分子、分母同时消去，并未倒除极小物理半径。

由 (R.2) 的准确商式定义

$$
 r_\mu=\mu_T/\mu_L,\qquad
 b_\mu=\mu_T(d_L-d_T),\qquad
 \mathcal P_{\mu_T}z=z-\frac{\mu_T}{\langle\mu_T\rangle}\langle z\rangle .
                                                               \tag{R.19}
$$

同一 $A_\sigma$ 代数和 (R.18) 给

$$
 \|r_\mu-1\|_{A_\sigma}
       +\mu_0^{-1}\|b_\mu\|_{A_\sigma}<2^{12}\mathfrak r .
                                                               \tag{R.20}
$$

例如 $J_T-J_L=K_T-K_L$，
$\mathfrak d_T-\mathfrak d_L=
-w^2(2+K_T+K_L)(K_T-K_L)$，而
$d_T-d_L$ 的分子是
$E[(K_T-K_L)_\theta J_L-(V_L-P)(K_T-K_L)]$。
分母均在已付 $1/8$ 球中。真实 mean 投影在 (R.19) 明列，
不把它换成 Fourier $\Pi_\perp$。

## 6. 原非mean matching 的准确线性化与 mean 输出

先令 Jacobi 高度在 $B$ 连续。指定原非mean径向导数跳
$b_\perp$, $\langle b_\perp\rangle=0$，它使用 raw $H_t$ 单位。
保留两侧真实 weak 法向荷，定义

$$
 \pi_{\rm tmp}
   =r_\mu\pi_L+b_\mu H_\theta+\mu_T b_\perp
                   +F_T^t-r_\mu F_L^t .
                                                               \tag{R.21}
$$

给定 tail 侧总 mean 通量 $q_T$，原匹配的完整两行准确等价于

$$
 H_T=H_L,\qquad
 \boxed{\quad
 \pi_T=\mathcal P_{\mu_T}\pi_{\rm tmp}
             +\frac{\mu_T}{\langle\mu_T\rangle}q_T .
 \quad}                                                       \tag{R.22}
$$

证明只需从 $\pi=\mu(H_t-dH_\theta)+F^t$ 反解：
$\pi_{\rm tmp}$ 对应完整导数 $H_{L,t}+b_\perp$。
向它加 $\mu_Tc$ 只改变一个常径向导数，
故保持全部非mean matching；唯一使 $\langle\pi_T\rangle=q_T$
的常数是

$$
 c_B=\frac{q_T-\langle\pi_{\rm tmp}\rangle}{\langle\mu_T\rangle}.
                                                               \tag{R.23}
$$

因此真实 mean 径向斜率差就是 $c_B$，并非已经等于0。
归一化 $K$ 单位须再除 $a_Bw_B$。
若另有高度跳 $u$，先令 $H_T=H_L+u$，在 (R.21) 另加
$-\mu_Td_Tu_\theta$；真实径向跳仍按其原单位输入。

在固定目标齐次 holonomy 方向，$q_T=q_L=0$。这时 (R.22)
保留完整 mean 约束；两侧背景若真正匹配，则
$r_\mu=1,b_\mu=0$，它准确变成 $\pi_T=\pi_L$。
若 $q_T,q_L$ 非零，原总通量兼容行仍是规定的
$q_T-q_L$ 等于真实界面 mean 荷，不可由投影自行指定。

在未匹配背景，原两个非线性 mean 小根之差是
$\mu(P,K_{L,\perp}+R_B)-\mu(P,K_{L,\perp})$。
它在 $R_B=0$ 时准确为0；微分时包含背景导数与 $R_B$ 的乘积。
(R.23) 正是这一 mean 输出的 raw 表达，不能提前删除。
只有实际非线性非mean方程消为0之后，两小根才相同。

## 7. $B$ 的全频小缺口及源行

将长段帽侧非mean高度暂置0、源荷置0，保留其 mean 自然条件。
于是 $\pi_L=-\mathcal N_{BB}H_B$，且该输出的 mean 为0。
由 (R.22)，

$$
 \pi_T=-\mathcal N_{BB}H_B+\mathcal E_BH_B,\qquad
 \mathcal E_BH=
 \mathcal P_{\mu_T}
       \bigl[-(r_\mu-1)\mathcal N_{BB}\Pi_\perp H
                                      +b_\mu H_\theta\bigr].
                                                               \tag{R.24}
$$

$\mathcal E_B1=0$、$\langle\mathcal E_BH\rangle=0$。
它既保常高度零方向，又保真实 mean 通量，没有将当前斜率差
伪装成一个自伴 Robin 系数。

$\sigma\ge1/16$ 给完整乘法界
$\|M_b:H^s\to H^s\|\le2^{14}\|b\|_{A_\sigma}$，$|s|\le2$；
该数直接由 $(1+|k|)^2e^{-|k|/16}$ 的上确界和 Young 和得到。
结合 (R.9),(R.19)--(R.20)，可统一取

$$
 \boxed{\quad
 \|\mathcal E_B:\dot H^{1/2}\to\dot H^{-1/2}\|
                                     <2^{32}\mathfrak r .
 \quad}                                                       \tag{R.25}
$$

在兼容总mean域 $q_T=q_L$ 上（其非zero差另作仿射荷），取
$B$ 的原波单位 $x_B=\Lambda H_B,y_B=\Lambda^{-1}\pi_B$，
完整界面 map 与恒等之差也小于 $2^{40}\mathfrak r$：
确切条目是 $\Lambda^{-1}M_{r_\mu-1}\Lambda$ 和
$\Lambda^{-1}M_{b_\mu}\partial_\theta\Lambda^{-1}$，
再保 (R.19) 的 mean 行。这里没有对未知高模取有限截断。

帽侧数据、长段源、$q_T,q_L$ 及端荷形成 (R.24) 的完整仿射项

$$
 b_B=\mathcal P_{\mu_T}
 \bigl[r_\mu(-\mathcal N_{BA}f_*-\ell_B+q_L)
                      +\mu_Tb_\perp+F_T^t-r_\mu F_L^t\bigr]
                 +\frac{\mu_T}{\langle\mu_T\rangle}q_T .
                                                               \tag{R.26}
$$

其中 $q_L=q_A-\int g_0$，且 $f_*$ 用 (R.10) 的真实物理单位。
这个式子保完整 infinite cross、两个 mean 和所有 source 列。
$\Gamma^*$ 两列及 $\nu$ 的作用从各自真正体源和帽侧数据进入；
fixed-stop 的 compact metric 方向不改变 $B$ 处目标，并不使其
Jacobi 响应或源变成0。其它改变端点目标的方向须加入真实直接
metric 荷，不能沿用固定目标零荷。

## 8. 接回整个非负 connector：一个真正可逆的外消元

先用同一实际 connector 和同一实际长段系数，人工只要求其
raw 总通量连续；帽侧非mean高度为0，外 mean 通量为0。
这定义一个自伴正的比较问题，记其 $C$ 端 DN 为 $\mathcal N_C^s$。
它不是把实际未解 matching 冒作已解：差额就是 (R.24)，随后完整加入。

在原 $C\to B$ 能量中加入
$\langle\mathcal N_{BB}H_B,H_B\rangle$。
由 (R.9)，该能量控制 $B$ 非mean迹的
$\dot H^{1/2}$ norm，费用小于4。
$C$ 零迹时，mean 高度差由原径向能量控制，故能量空间没有常数核。
对给定 $C$ 数据，原零 $Q$ 平台的 lift 仍可支持在到达严格正区之前，
费用小于16；常高度另取整段常函数，能量为0。
所以

$$
 0\le\mathcal N_C^s,\quad
 \|\mathcal N_C^s:L^2_C\to L^2_C\|<2^{16},\qquad
 \ker\mathcal N_C^s=\mathbb C .
                                                               \tag{R.27}
$$

实际 matching 改为 (R.24)，相当于从该型减去
$\langle\mathcal E_BH_B,V_B\rangle$。
因其输出 mean 为0，不必为测试函数的平均高度再付一个长电阻。
(R.25) 给其相对型 norm 小于

$$
 \eta_B=2^{36}\mathfrak r .                              \tag{R.28}
$$

若 $\eta_B<1/2$，同一能量空间上真正 Neumann/Lax--Milgram
反演给唯一实际外消元，记其 $C$ 端图为 $\mathcal N_C^a$。
常高度仍为准确零方向，真实 mean 荷按 (R.26) 作为仿射输入。
这个消元从未除以指数小的 positive transmission。

下面接三阶端点需要比裸 $L^2$ 差多一点角正则。
原[正区跨口平滑](R119-supplement-actual-positive-cross-port-smoothing-and-exterior-unitary-two-port.md)
(S.5)--(S.11) 的嵌套正缓冲仍在同一 $C\to B$ 段内，
远侧增加正型 $\mathcal N_{BB}$ 不改变该局部 Caccioppoli 证明。
零 $C$ 迹的角 commutator 解亦可用同一相对型反演。

为明确费用，(R.4) 的复角域给长段型的角导相对 norm 小于
$2^{10}$；(R.25) 的角导给 $2^{7}\eta_B$，
整个强制型的余量大于1/2。原正缓冲内
$\|\partial_\theta U_f\|_{H^1}<2^{374}a(U_f,U_f)^{1/2}$。
角 commutator 的零 $C$ 迹修正 $W_f$ 的能量先付 $2^{20}$。
在该缓冲内取固定截面，准确用
$U_{\partial f}=\partial U_f-W_f$ 的完整 trace 作外侧 Dirichlet
lift；这个组合满足齐次实际外方程，故它到 $B$ 的能量小于
$2^{400}\|f\|_{L^2}$。没有把单独 $\partial U_f$ 的 coefficient
commutator 源误当成0。
由

$$
 f=f_0+\partial_\theta f_1,\qquad
 f_0=\Lambda^{-2}f,\quad
 f_1=-\partial_\theta\Lambda^{-2}f,
$$

和准确的
$U_{\partial f_1}=\partial U_{f_1}-W_{f_1}$，
得到对实际/比较两图共同有效的远侧迹门

$$
 \|H_B(f)\|_{H^{1/2}}
                           <2^{512}\|f\|_{H^{-1}_C}.
                                                               \tag{R.29}
$$

这里也支付了 $B$ 高度 mean：对 $f_0$ 用原 connector 的
height lift 及径向 Poincare（费小于 $2^{190}$）；
对 $\partial f_1$，$\langle\partial U_{f_1}(B)\rangle=0$，
$W_{f_1}$ 的零 $C$ 迹和同一 Poincare 给小于 $2^{210}$。
这些费用均在 $2^{512}$ 内。
粗 $C$ 输入的全域场是分布场；只在正缓冲之后使用真实能量。
原零平台并没有被要求对粗 $C$ 数据产生全域 $H^1$。
完整 mean、高低交叉和长段 mean 自然条件均在上述型中。

两解的精确 Green 配对因此给

$$
 \langle(\mathcal N_C^a-\mathcal N_C^s)f,g\rangle
 =-\langle\mathcal E_BH_{B,a}(f),H_{B,s}(g)\rangle .
$$

(R.25),(R.29) 先对光滑数据、再通过唯一延拓，给

$$
 \|\mathcal N_C^a-\mathcal N_C^s:
                         H^{-1/8}\to H^{1/8}\|
                    <2^{1060}\mathfrak r .              \tag{R.30}
$$

$2^{1060}$ 包含 $32+512+512$ 及复对偶费用。
这里的正阶输出来自真实跨正区平滑，不是从四个角交换子
自动推断的对角频率增益。

## 9. 三阶转折和 $e_X$：真正实际外返回

取原 $\mu_*=\mu_0(C)>2^{-363}$，令
$\mathcal N^s=\mu_*^{-1}\mathcal N_C^s$。
其复角域现在取 $1/128$。原
[三阶转折](R119-supplement-actual-cubic-turning-complete-reflection-and-strong-sources.md)
(T.8)--(T.10) 的证明逐项给

$$
 \|\mathcal N^s(\tau)\|_{2\to2}<2^{379},\qquad
 |(\mathcal N^s)_{mn}|<
                     \frac{2^{420}}{(1+|m-n|)^4}.
                                                               \tag{R.31}
$$

只把原角圆盘 $1/4$ 换为 $1/128$；四阶 Cauchy 多付20 bits。
(T.11)--(T.25) 的反向能量、$H_C\in H^{-1/8}$、
截断虚通量极限和反向满射证明只用这个完整自伴图；
它们不要求 $\mathcal N^s$ 对常数严格正。
因此其 cut128 反射仍是完整 onto unitary，保留常高度方向。

记 $\mathcal P_C$ 为该齐次解的 $C$ 迹，
$\mathcal K_C$ 为真实边界源 $e_C$ 的 $C$ 迹。
原 (T.19),(T.29)--(T.30) 给

$$
 \|\mathcal P_C:L^2_D\to H^{-1/8}_C\|<2^{13},\qquad
 \|\mathcal K_C:H^{1/8}_C\to H^{-1/8}_C\|<2^{32}.        \tag{R.32}
$$

第二门可直接重取原证明的全部常数：
零 incoming 时 $\|\beta\|<2^{15}\|e_C\|$；
同一端能量及 (T.17)--(T.19) 随后给
$H_C$ 迹小于 $2^{29}\|e_C\|$，再宽放三 bits。
它不是由某一个 Airy 高度值猜测的 source-to-trace norm。

由 (R.30)，

$$
 \|\Delta\mathcal N:H^{-1/8}\to H^{1/8}\|
       <2^{1500}\mathfrak r,\qquad
 \Delta\mathcal N=\mu_*^{-1}
                    (\mathcal N_C^a-\mathcal N_C^s).
                                                               \tag{R.33}
$$

实际边界迹准确解

$$
 H_C=\mathcal P_C\alpha_D+
           \mathcal K_C(\Delta\mathcal N H_C+e_C).
                                                               \tag{R.34}
$$

只要 $2^{1532}\mathfrak r<1/2$，这个真正同空间方程严格收缩。
它给完整 actual cut128 反射 $\mathscr S_D^a$ 与仿射源；
齐次差满足
$\|\mathscr S_D^a-\mathscr S_D^s\|<2^{1600}\mathfrak r$。
实际反射一般不是精确酉，不能抹掉这一差。

最后消费前篇 (X.18)--(X.23) 的同一个 onto $J$-unitary
$e_X\leftrightarrow D$ 两迹传递，双向 norm 小于 $K_X=2^{8192}$。
对 unitary 比较图，原 Möbius 分母逆小于 $K_X$；
加入上述差之后，分母用一次真实 Neumann 级数反演，费小于
$2K_X$。于是得到

$$
 \boxed{\quad
 \beta_X=\mathcal E_a\alpha_X+b_X,\qquad
 \|\mathcal E_a-\mathcal E_s\|_{L^2\to L^2}
                         <2^{20000}\mathfrak r,\qquad
 \mathcal E_s^*\mathcal E_s
  =\mathcal E_s\mathcal E_s^*=I .
 \quad}                                                       \tag{R.35}
$$

这是真正非mean matching、mean 通量约束及未拼平系数的外返回，
覆盖所有频率。没有把 $e_X$ 认作 cut128，也没有删除未知高输入。
前篇的 root、strict、物理密度和 normal shear 费用全部保留。

## 10. 实际残差门、完整源域及剩余闭合

在固定停止篇 (D.34)--(D.36) 的已构造 incoming 对上，
(R.16) 就是其未消去的实际 $\mathcal F_c$，故

$$
 \mathfrak r<2^{-119738000},\qquad
 2^{20000}\mathfrak r<2^{-119718000}.                  \tag{R.36}
$$

此处使用原 $\sigma=1/16$ 的真实残差，不把它错误送进需要2074
角宽的旧 $\mathsf D_0^{-1}$。所有 (R.28),(R.33)--(R.35) 门
都有显示余量，残差本身仍没有被置零。

(R.35) 的仿射输入由 (R.26)、connector 的真实 ordinary/weak
源、三阶段 (T.27) 的强源和前篇 (X.26)--(X.28) 的根联合源
按真实次序组成。一个明确的最终端口源域是：实际消元得到的
$e_C\in H^{1/8}$、三阶源属于
$\mathcal M(H^{1/2})$、strict 源属于前篇
$\mathcal M(H^{-1/2}\oplus H^{-1/2}\oplus\mathbb C)$，
root 源具有原联合 norm。
在此域，(R.34) 的 source 逆费小于2，再按前篇完整源链传播。
不将任意 raw $L^2$ 源免费声明属于所有这些窗口；
(R.12)--(R.15),(R.26) 是它必须实际通过的完整映射。

特别，长段及 $B$ 的 (R.26) 可以直接消费，而不是只留下一个
未知的 $e_C$ 条件。定义原单位边界预算

$$
 \mathfrak B_B=\|f_*\|_{H^{1/2}}+8\mathfrak S_L+
 |q_T|+|q_L|+\mu_0\|b_\perp\|_{H^{-1/2}}
 +\|F_T^t\|_{H^{-1/2}}+\|F_L^t\|_{H^{-1/2}} .
 \tag{R.37}
$$

(R.26) 与完整乘法界给 $\|b_B\|_{H^{-1/2}}<2^{20}\mathfrak B_B$。
用实际外型的 adjoint 齐次解作 Green 测试；它与 (R.29) 有相同
强制余量、角 commutator 和 trace 常数，故
$\|\ell_C(b_B)\|_{H^{1/8}}<2^{512}\|b_B\|_{H^{-1/2}}$。
除 $\mu_*$ 并付实际型逆，足够的共同门为
$\|e_C(b_B)\|_{H^{1/8}}<2^{900}\|b_B\|_{H^{-1/2}}$。
mean 荷在 (R.29) 的完整 $H_B$ trace 中已经付清。

再按 (R.32)--(R.35) 的真源链，帽侧数据和整个 long 源到原
$e_X$ 的仿射输出可安全取

$$
                   \|b_X^{\,\mathrm{long},B}\|_2
                            <2^{22000}\mathfrak B_B .   \tag{R.38}
$$

这没有倒除 $a_Bw_B$；若用户给的是归一化
$\dot f_*,\dot K_B$，先逐项按 (R.10) 换成上述 raw 单位。
connector/root 内其它源仍按原强/联合 source 合同另外加入。

长段 $q_A$、tail 的 $q_T$、连接段积分源及全部端点 $F^t$ 荷
仍满足各自的 (R.15),(R.22)--(R.23)。
唯一 $\lambda$ 对齐一个整体高度；另一端高度、mean 斜率差和
全源通量兼容都是输出/保留行。齐次真正拼平时它们退化为同一个
物理常高度方向，只可商去这一维，不可商去 canonical mean 的
所有分量。

开放内部篇 (M.28)--(M.30) 的外条件现在有了实际消费者：
将 (R.35) 按其固定 incoming/outgoing 顺序代入即可。
仍须反演真正的闭合算子 $I-\mathcal E_a\mathcal T_a$，
支付原强标签/源权，并与帽/body 的独立数据、参数 Schur 和几何
联立。本篇证明的是此前缺失的实际外图、其完整 mean/source
接口以及未拼平造成的明确小差；未把这个组件重新命名为最终逆。

全文为新的解析推导，没有新增本地数值实验。
