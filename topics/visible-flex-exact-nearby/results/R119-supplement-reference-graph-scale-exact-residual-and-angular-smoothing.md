# R119 续篇：固定参考图范数、完整非线性残差与实际角向平滑

2026-11-15，visible-exact / tail_connector。

**状态：下述固定参考图尺度、真实残差等价及角向平滑已证明。** 本篇保持原 fixed-stop simple-root 对象、$\zeta_{131}$、第二参数、真实径向分片和全部物理源单位。新增的是一个同时控制状态与其线性参考 residual 的 Banach 尺度。只控制四态的 $\mathscr X_s$ 不保证 residual 属于窄普通源域；本篇不作那个错误推断。

第一参数使用 L 的同一个真实低范数值图，holonomy mean 使用 M 的准确小根。角向 smoothing 先作用在固定参考的非mean高度，再重新计算这两个真实非线性量。一般有荷方向、外部匹配、两个 mean端列和物理高度跨度仍独立保留。本篇证明图范数与真实残差的等价、真正 smoothing 和完整 Fréchet余项；不把这些结论单独称作已完成的 Nash迭代。

## 1. 固定参考而不改变几何对象

使用已证明的：

* [L：低范数第一参数与高阶 tame 共轭](R119-supplement-low-norm-principal-Gamma-map-and-tame-high-conjugacy.md)；
* [M：完整 holonomy 荷与高度图](R119-supplement-finite-Sobolev-nonlinear-holonomy-charge-and-height-chart.md)；
* [C：非解背景与真径向 jets](R119-supplement-off-shell-controlled-radial-jets-and-exact-holonomy-retraction.md)；
* [N：二层完整网络逆](R119-supplement-two-level-full-network-tame-inverse-and-complete-sources.md)；
* [J：三径普通源与四径状态](R119-supplement-three-radial-source-jets-four-state-jets-and-1734-loss.md)。

固定同一个第二参数 $\gamma_2^\flat$，取 L.1 的径向参考 $w_0=w_{\gamma_1^*(0),\gamma_2^\flat}$。记
$$
 A_0^{\rm rad}=(\log w_0)_t,\quad Q_0=-A_0^{\rm rad},\quad
 q_0=w_0^2,\quad c_0=\frac{\mu_jp_{*,0}^2}{12r^{10}} .
 \tag{E.1}
$$
$A_0^{\rm rad}$ 不等于后文 holonomy 权 $A_W=JD^{-3/2}$。不冻结实际背景的系数；(E.1) 只用于定义固定线性坐标。

给定普通角 mean为0的真实高度 $u=u_\perp$，置
$$
 p_0=\frac{u_\theta}{a_{\rm ph}w_0},\quad
 k_0=\frac{u_t}{a_{\rm ph}w_0},\quad
 U_0=(p_0)_\theta,\quad V_0=(k_0)_\theta .
 \tag{E.2}
$$
因此 $(p_0)_t=V_0-(A_0^{\rm rad}+1)p_0$ 准确成立。仍取 $\ell_j=2^{-64}J_j^{-2}\delta_j^4$、$\ell_o=2^{-1024}$ 和原 $C_j$。定义
$$
 X_s^0(u)=
 \max\left\{\sup_j C_j^{-1}
    \max_{0\le a\le4}\ell_j^a
       \sup_{I_j}\|\partial_t^a(p_0,k_0,U_0,V_0)\|_{H^s},
 \quad
 2^{440}\max_{0\le a\le4}\ell_o^a
       \sup_{I_o}\|\partial_t^a(p_0,k_0,U_0,V_0)\|_{H^s}
                    \right\}.
 \tag{E.3}
$$
$I_o$ 指原有限 connector 部分，不重复收费已列出的第129胞。导数是原真实分片内的普通单侧导数。需要连续的高度及一阶 state traces 仍作为真实线性约束保留；broken norm 不自行证明更高接缝相容。

## 2. 窄源图范数不是状态范数的改名

定义固定 radial 线性 residual
$$
 e_0(u)=(k_0)_t-Q_0(2k_0+U_0),\qquad
 \mathcal L_0u=
 \begin{cases}
 c_0e_0(u),&\text{内部胞元},\\
 e_0(u),&\text{有限 connector}.
 \end{cases}
 \tag{E.4}
$$
有限项用 J.3 的真正 two-row ordinary 单位；不将内部 $c_0$ 移植到 connector。所有分量的普通角 mean准确为0，但这不对实际 nonlinear residual 的普通 mean作假设。

对源向量 $g$，记
$$
 Z_s^{[3]}(g)=
 \max\left\{\sup_j(\zeta_j\delta_j^{16})^{-1}
      \max_{0\le a\le3}\ell_j^a
           \sup_{I_j}\|\partial_t^ag_j\|_{H^s},
 \quad
 2^{440}\max_{0\le a\le3}\ell_o^a
           \sup_{I_o}\|\partial_t^ag_o\|_{H^s}\right\}.
 \tag{E.5}
$$
完整图尺度定义为
$$
                  \|u\|_{E_s}=X_s^0(u)+Z_s^{[3]}(\mathcal L_0u).
 \tag{E.6}
$$
从 $X_s^0$ 粗估裸 $c_0e_0$ 会出现 $c_0C_j/(\zeta_j\delta_j^{16})$；它没有一个可以删除的全层常数。因此 (E.6) 是真实增加的域条件。

$E_s$ 是完备的。若 $u_n$ 在 (E.6) 中为 Cauchy，则每个固定闭子片上的四态及所列径向导数、源及前三导分别收敛。第一运动学恒等式和 (E.4) 在分布中传到极限；非mean高度由 $u=a_{\rm ph}w_0I_\theta p_0$ 唯一恢复。原线性 trace约束是闭条件。最后取原 weighted supremum 即得极限仍在 (E.6)。这不假设全层最高 norm 中 Fourier多项式稠密。

独立常高度 $\lambda$ 不计入 (E.6)，另作 scalar坐标；不能每个胞元各添一个自由常数。一般 holonomy荷也不包含在 $k_0$ 的非mean部分中。

## 3. 原尺度上的准确 smoothing

令 $\Lambda_m=(1+m^2)^{1/2}$、$m\in4\mathbb Z$，以 $S_T=\mathbf1_{\{\Lambda_m\le T\}}(D_\theta)$ 表示真实角 Fourier投影。它不依赖 $j,t$。所有 (E.1) 系数径向，故
$$
 \mathcal L_0S_Tu=S_T\mathcal L_0u,\qquad
 \partial_t^aS_Tu=S_T\partial_t^au .
 \tag{E.7}
$$
两行、有限 connector、原线性 traces 和角 mean均保留。对 $0\le a\le b$，逐真实圆的 Parseval公式直接给
$$
 \|S_Tu\|_{E_b}\le T^{b-a}\|u\|_{E_a},\qquad
 \|(I-S_T)u\|_{E_a}\le T^{a-b}\|u\|_{E_b}.
 \tag{E.8}
$$
这里没有乘随层变化的角宽，没有交换 $\sum_m\sup_j$。需要该次序的核估计仍用 N.7 所付的两角阶。

同样，对 $s=(1-\vartheta)a+\vartheta b$，
$$
 \|u\|_{E_s}\le
       \|u\|_{E_a}^{1-\vartheta}\|u\|_{E_b}^{\vartheta}.
 \tag{E.9}
$$
先对每项用 Hilbert插值，再用 Hölder合并 source/state 两项及真实 supremum即可。若 $b>a$，(E.8)证明 $S_Tu\to u$ 于 $E_a$；不声称对任意 $E_a$ 成员在同一个 $E_a$ norm都收敛。

$S_T$ 只平滑非mean高度与参考线性源。它不保持一个未经证明的 nonlinear cap/return行；这样的行必须在重建后重新评价，并按原 source坐标保留。

## 4. 同一真实第一参数、mean 和高度重建

取
$$
                  \|u\|_{E_{1856}}\le
                   \rho_E:=2^{-8192016}.
 \tag{E.10}
$$
则 L.2 的 $\mathcal D_{20}$ 门成立。用唯一真实值图 $\gamma_1^*(u)$，置
$$
 \psi=\log(w/w_0),\quad
 w=w_0e^\psi,\quad q=q_0e^{2\psi},\quad
 Q=Q_0-\psi_t,\quad c=c_0e^{2\psi}.
 \tag{E.11}
$$
令 $P=e^{-\psi}p_0$、$K_\perp=e^{-\psi}k_0$、$U=e^{-\psi}U_0$、$V=e^{-\psi}V_0$。取 M.9 的同一个小根
$$
 \Phi_q(P,K_\perp+\kappa)=0,\qquad K=K_\perp+\kappa .
 \tag{E.12}
$$
这是 holonomy-one body图。它不定义 $\chi\ne0$ 上的第一参数值图，也不代替独立外荷的兼容等式。

真实高度为
$$
 z(t,\theta)=u(t,\theta)+\lambda+
      \int_{t_f}^{t}a_{\rm ph}(s)w(s)(1+\kappa(s))\,ds .
 \tag{E.13}
$$
积分穿过全部真实胞元，端值不重置。metric reference部分、mean高度跨度及 $\lambda$ 在两外端都是实际输出，不能包进小源后丢掉。

(E.12)给真正 $\chi=0$，由 M.16 才有
$$
 \langle A_WN\rangle=0,\quad
 A_W=JD^{-3/2},\quad N=c(K_t-\mathcal F),\quad
 N=\Pi_{A_W}(P_\perp N),\quad
 \Pi_{A_W}f=f-\frac{\langle A_Wf\rangle}{\langle A_W\rangle}.
 \tag{E.14}
$$
有限 connector在同式读 ordinary $e=K_t-\mathcal F$。(E.14)仅用于已经完成 (E.12)的真实场；不是任意 given charged source的恒等式。

## 5. 完整 residual 的精确 graph分解

令
$$
 {\cal Q}_F(W)=\mathcal F_Q(W)-Q(2K+U),\qquad
 \mathcal F_Q(W)=
 \frac{Q(2K+U+K^2+KU+qP^2)+(1+q)(V-P)^2}
                       {1+K+(1+q)U}.
 \tag{E.15}
$$
$\mathcal Q_F$ 的完整 Taylor从二次开始，包含真实 $\kappa$。在取普通非mean后，
$P_\perp K_t=e^{-\psi}[(k_0)_t-\psi_tk_0]$，
$P_\perp Q(2K+U)=e^{-\psi}(Q_0-\psi_t)(2k_0+U_0)$。
因此内部准确有
$$
 \boxed{\quad
 P_\perp N=e^\psi\mathcal L_0u
      +c_0e^\psi\psi_t(k_0+U_0)
      -cP_\perp{\cal Q}_F(W).
 \quad}                                                   \tag{E.16}
$$
$\kappa_t$ 和 $2Q\kappa$ 只在这一步被 $P_\perp$ 消去；完整 mean随后按 (E.14)恢复，绝不设 $\langle N\rangle=0$。$\psi_t(k_0+U_0)$ 是正号。

第一参数原支集都在旧实际胞元；唯一外行例外也在第129胞下降坡，不在新增 finite connector。故在该 connector，$\psi=0$，准确有
$$
               P_\perp e=e_0(u)-P_\perp{\cal Q}_F(W).
 \tag{E.17}
$$
若另给在那里变化的 metric方向，须用完整 $e^{-\psi}e_0+e^{-\psi}\psi_t(k_0+U_0)-P_\perp{\cal Q}_F$；该方向不属于当前冻结第二参数的图，仍按独立 metric列收费。

(E.16)--(E.17)不含未知源的径向 pullback，也没有 $\kappa_{tttt}$ 乘 $c$ 的裸大项。取三个 broken $t$ 导后最高只需 $Z_0$ 的三阶、$\psi$ 的四阶及 $Q_0$ 的三阶；完整状态重建本身才另用所给的四阶 $Z_0$。

## 6. 完整 profile 与统一 tame常数

以下 $20\le s\le8192$，令 $\epsilon=X_{20}^0(u)$、$x_s=X_s^0(u)$。
L.17沿 $\tau u$ 积分、G.19真实六邻胞及原 bump四阶导给
$$
 g_j:=\sup_{I_j}|\psi|
 \le2^{9216}J_j^2\delta_j^{-1}C_j^\#\epsilon^2,
$$
$$
 \max_{0\le a\le4}\ell_j^a|\partial_t^a\psi|
       \le2^{64}g_j,\qquad
 \max_{0\le a\le3}\ell_j^a|\partial_t^{a+1}\psi|
       \le2^{64}\delta_j^{-3/2}g_j .
 \tag{E.18}
$$
第129胞外行例外用 G的独立有限式。原 $\sup J^2\delta^{-1}C^\#<2^{160144}$ 给整个区间的第一组 scalar界小于 $2^{170000}\epsilon^2$。这些 scalar没有角导数。bump为degree6、仅 $C^2$；第四导只在原片内用，真实第三导跳不设为0。

M的小根和 (E.15)使用完整 reciprocal/二项式级数。按 M.23分配一份最高 norm：$k$ 个 Fourier因子满足
$\langle\sum m_i\rangle^s\le k^{s-1}\sum_i\langle m_i\rangle^s$；
在低球内，$k^s\epsilon^{k-1}$ 的完整级数收敛。
三个径向导数的有限 Leibniz数、scalar inverse低分母和四态的四阶 jets同属这一计算。每项至多一个高角因子，不要求高 $x_s$ 小。$s\le8192$ 的局部费用可宽取 $2^{524288}$：固定次数至多8的项只收 $8^s$、四次 Leibniz和低分母；余下无限项由 $k\le2^{k-1}$ 与 (E.10)求和。

乘普通源单位后，两个结构分别消费原 profile：
$$
 \frac{c(1+|Q|)(C_j^\#)^2}{\zeta_j\delta_j^{16}}
 \le2^{2048}J_jh_j^{-10}
       \frac{\zeta_j}{\mu_j}\delta_j^{-47/2},
$$
$$
 \frac{c\,C_j^\#|\psi_t|}{\zeta_j\delta_j^{16}}
 \le2^{16384}J_j^2h_j^{-10}
       \frac{\zeta_j}{\mu_j}\delta_j^{-49/2}\epsilon^2 .
 \tag{E.19}
$$
第一项是 R.33加完整六邻胞费，第二项是 G.20--G.21。
三个 scaled径向导数不增加负层幂：$\ell^aQ^{(a)}$ 用
$1+|Q|$ 的宽门，$\ell^ac^{(a)}/c$ 用 C.4--C.7，$\psi$ 用 (E.18)。

两个 profile完整三段 supremum各小于 $2^{200000}$；保留
$\delta_{4096}^{-3/2}$、$\delta_{8192}^{-485/4}$ 和129--8192全部前缀。深段净幂分别是 $103-10/256$ 与 $102-10/256$。
finite connector的 $e_o$ 保原 $2^{440}$ 单位与真实 profile；B.31/J.9有限 coefficients及 $\ell_o$ 给固定费用，并入同一宽预算。唯一浅端外 bump按 G 的 $2^{212992}$ 有限门，不套深尾正幂。

(E.16)后两项和 (E.17)第二项组成 $Q_{\rm src}(u)$。
它在这里还**不包括** $\Pi_{A_W}$ 对线性首项所作的 mean修正。
上述完整估计给
$$
       Z_s^{[3]}(Q_{\rm src}(u))
                    \le2^{2097152}\epsilon x_s .
 \tag{E.20}
$$
$\epsilon^2x_s$ 的 metric项已用 $\epsilon<1$ 放宽。
2097152 bits统一包含524288局部代数、200000全 profile、
170016 scalar multiplier、finite connector/mean及一次第一参数读出；不按因子重复乘此常数。
线性首项的 mean修正将在下一节保留其真实 $\mathcal L_0u$ 输入。

## 7. 图范数与真实 ordinary residual 等价

令 $\mathfrak F(u)$ 为重建后的完整 residual向量：内部读 $N$，finite connector读 $e$。令 $\mathfrak f(u)=P_\perp\mathfrak F(u)$。
(E.16)首项的乘子仅径向，其四阶 scaled derivatives与1之差小于
$2^{170016}\epsilon^2$。因此
$$
 \mathfrak f(u)=\mathcal L_0u+{\cal Q}(u),\qquad
 Z_s^{[3]}({\cal Q}(u))
       \le K_E\|u\|_{E_{20}}\|u\|_{E_s},
       \qquad K_E:=2^{2097152}.
 \tag{E.21}
$$
同一宽 $K_E$ 包括 $(e^\psi-1)\mathcal L_0u$；没有再叠加一份2百万 bits。

完整 mean要对 $\langle A_Wf\rangle/\langle A_W\rangle$ 求三个径向导。因 $\mathcal L_0u$ 普通 mean为0，该修正至少含一份状态小量。每项是低正下界、有限低 state jets与完整圆周配对，输出是角常数，不对它索取 $s$ 个 coefficient导数。其界保
$K_E\|u\|_{E_{20}}\|u\|_{E_s}$，而不是仅用 $X_s^0$。

以 $X_s^{\rm true}$ 表示当前 $w$ 下含 $\kappa$ 的完整四态 J.2 norm，不含独立高度常数。上述等式、小根四径导和 (E.21)给
$$
 \frac1{16}\|u\|_{E_s}
 \le X_s^{\rm true}(u)+Z_s^{[3]}(\mathfrak F(u))
 \le16\|u\|_{E_s},\qquad20\le s\le8192.
 \tag{E.22}
$$
下界先由 $K_\perp=e^{-\psi}k_0$ 读回参考四态，再用 (E.16)读回 $\mathcal L_0u$。所有 nonlinear项由
$K_E\|u\|_{E_{20}}<1/64$ 吸收，只用低球。
(E.10)严格给 N.1的 $\mathscr R_{1856}<2^{-8192000}$，更高背景仅有限。

## 8. 真正 nonlinear smoothing 先截高度、再重建

定义 $\mathfrak S_Tu$ 为以 $S_Tu$ 重新执行 (E.11)--(E.14)得到的物理场，而非直接截已补全的 $K$ 或 $\mathfrak F$。
L第一参数仍取同一值图，M小根仍为唯一 holonomy-one根，$\lambda$ 不改。
由 (E.8)、(E.10)、(E.22)，全部 $\mathfrak S_Tu$ 保原低门，
其实际 residual仍在同一个窄源域。

并不声称 $\mathfrak F(S_Tu)=S_T\mathfrak F(u)$。准确非mean差为
$$
 \mathfrak f(S_Tu)-S_T\mathfrak f(u)
                         ={\cal Q}(S_Tu)-S_T{\cal Q}(u).
 \tag{E.23}
$$
线性大项被 (E.7)完全消去。对 $20\le a<b\le8192$，
一次差及 (E.8)给
$$
 \begin{split}
 Z_a^{[3]}(\mathfrak f(S_Tu)-S_T\mathfrak f(u))
 \le K_E\{&
 T^{a-b}\|u\|_{E_{20}}\|u\|_{E_b}\\
 &+T^{20-b}\|u\|_{E_a}\|u\|_{E_b}\}.
 \end{split}
 \tag{E.24}
$$
固定 factor4仍在同一宽 $K_E$ 内。完整 mean差必须保两个场各自的
$\Pi_{A_W}$ 再比较，也由同型界支付；不能交换不同权的投影。

## 9. 同图中的 Fréchet 差与完整 mean方向

L给真实 $C^1$ 参数值图及统一二次 Fréchet余项。逐行余项仍带
真实 $C_j^\#$：由 $E_i^\ell/(\gamma_i^{\rm D})^2<2^{4416}$、
P.30正权公式及 mixed ODE，
$\gamma_i^{-1}(E_i^\ell)^2\le2^{4416}E_i^\ell$。
再解同一个低参数 fixed point、乘真实 metric曲线导数，即保 L.17相同 profile；不能将 uniform 参数上界粗赋给所有深层 physical $\gamma$。

结合 (E.15)、M小根及三个普通径向导数，在同一低球内有
$$
 \begin{split}
 Z_s^{[3]}(D{\cal Q}(u)[v])
 \le K_E\{&
 \|u\|_{E_{20}}\|v\|_{E_s}+
               \|u\|_{E_s}\|v\|_{E_{20}}\},\\
 Z_s^{[3]}({\cal Q}(u+v)-{\cal Q}(u)-D{\cal Q}(u)[v])
 \le K_E\{&
 \|v\|_{E_{20}}\|v\|_{E_s}
             +(1+\|u\|_{E_s})\|v\|_{E_{20}}^2\}.
 \end{split}
 \tag{E.25}
$$
$u,u+v$ 均在低球，高 $E_s$仅有限。这不宣称第一参数值图 $C^\infty$；显示的 $C^1$ 和二次余项已足够。

完整方向仍有 mean及 metric项：
$$
 D\mathfrak F(u)[v]
 =D\Pi_{A_W}[v]\,\mathfrak f(u)
       +\Pi_{A_W}\{\mathcal L_0v+D{\cal Q}(u)[v]\}.
 \tag{E.26}
$$
第一项是一个真实角常数，由背景 residual与 mean权变化配对产生；
不能因选择非mean source坐标而删除。它与 M/O的 $+\dot\psi\,N$、
residual-sensitive mean恒等式及 G完整 parameter height lift相容。

## 10. 原源列、known成员和下一迭代门

若一个旧解析成员满足本篇真实线性 traces，并在各普通片内
$\mathfrak F(u)=0$，则 (E.16)给
$\mathcal L_0u=-e^{-\psi}Q_{\rm src}(u)$（有限部分用 E.17）。
B.31的 $X_{8192}^0\le2^{133000}\mathcal X$、
$\mathcal X\le2^{-8388608}$ 于是给
$$
                    \|u\|_{E_{8192}}
                   \le2^{133001}\mathcal X<\rho_E .
 \tag{E.27}
$$
这只检验满足所列条件的真正旧成员。finite Newton候选若还具有
界面 mismatch、外 returned残差或独立 flux荷，须继续作为真实
source列保留；(E.27)不由局部 $N=0$ 推全匹配。

general charged方向仍用 M独立 Volterra荷图与 N/G的明确
projected反馈定义，不由 (E.14)自动进入第一参数值图。
外 $C_R/B_0$、两 mean端口、$\nu$、给定第二参数方向、
metric reference高度与真实原子全部是额外坐标或 residual输出；
角 cutoff不消去任何这些条件。

本篇得到同一域中的固定参考 closed graph、准确 Fourier smoothing、
重建后完整窄源、两层 tame及真实 mean方向。下一步须在这个尺度
给完整 actual approximate inverse，控制
$$
 c_{\rm ph}\mathcal L_Wh
       =c_{\rm ph}\mathcal J_Wh-\mathcal E_N[h]
 \tag{E.28}
$$
及参数/边界的准确项，再选择能支付1734损失和背景 $s+1796$
的实际 smoothing序列。N/J的端口和 source范围仍是输入；
(E.6)不创建一个尚未证明的同域 inverse，不提前登记物理 $C^2$存在性。
