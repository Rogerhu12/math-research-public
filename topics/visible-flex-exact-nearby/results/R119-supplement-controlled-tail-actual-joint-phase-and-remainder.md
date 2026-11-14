# R119 续篇：控制后新尾的真实非径向双相位选择、完整余项与 incoming 重实例

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 固定第53–54束的一个真实径向控制
$\Omega=(s,\Xi)$，其中 $\Xi$ 在已付 phase-annihilator 球
$\|\Xi\|_{\ell^\infty(C^4)}<2^{-64}$ 内，并作第54束准确两 bump
补偿。对这个新对象，重新构造非零标签的无限联立两相位选择；
所有真实主返回和完整首密度相位仍取原已选算术目标。
第51束的完整 $4/3$ 阶余项与全网络高块也在新对象上重获。

此外，在本对象上重新停止第四 connector、重新选定一个实际外好参数，
并在此后固定该参数，实际正帽—长段的 incoming 固定点再次存在。
这个固定点的真实剩余没有清零。径向中频选择的角宽合同仍不是非径向
同权逆；完整 $\mathcal F_c=0$ 保持为未闭任务。

## 1. 同一个新对象与全部已付输入

采用
[控制后全图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
及[准确 radial phase 补偿](R119-supplement-radial-phase-compensation-and-full-Wronskian-Hessian.md)。
对每个完整内部负分量 $i$，令
$\bar\Gamma_i(\Omega)=\Gamma_i^0+\eta_i(\Xi_i)$。
其 radial $\omega_i,\beta_i^0$ 准确等于原两参数算术选择的目标。
$\Theta=-2\int\sqrt Q\,dt$、标准角 $x=4\theta$，物理角周期为 $\pi/2$。
最外截断分量 $(129,2)$ 仍留在外匹配行，其内部反项为0。

对标签取
$$
 A_*=2^{-262148},\qquad \|a\|_{\ell^1_{224}}<A_*,
 \qquad \mathcal X=16\|a\|_{224}\le2^{-262144}. \tag{N.1}
$$
内部标签是原真实层 $b_m$ 上的两态标签，不是共同 cut 的任意高度。
由第53束，全部参数复盒中都存在真全频解，$\|X\|<\mathcal X$。
统一放宽定义
$$
 N_j^c=2^{200}h_j^{-5}\frac{\zeta_j}{\mu_j\delta_j^2},
 \quad (N_j^c)^\#=N_j^c+\mathbf1_{j\ge130}N_{j-1}^c,\quad
 n_i=4(N_j^c)^\#\mathcal X .
 \tag{N.2}
$$
在未改前缀，这只把旧状态界放宽 $2^{16}$；在新深段它是真正新局部图
所给的界。准确有
$$
 \sum_{j\ge129}(K_j^{\rm ref})^2N_j^c<2^{160016},
 \quad K_j^{\rm ref}=2^{5000}(j+4)^5\delta_j^{-10}. \tag{N.3}
$$
$\delta_{4096}^{-3/2}\delta_{8192}^{-485/4}$ 两个全局逆幂和全部
129–8192前缀包含在此式中。

新增 $C^4$ 形状在 strict 支集内，根附近整个 quartic germ 未改。
除了第53束已经逐项核查的 $Q,Q_t,Q_{tt}$ 外，原更宽
$$
 |Q_{ttt}|<2^{40}(j+5)\delta_j^{-6} \tag{N.4}
$$
也保持：新增项最多
$2^{-64}(\sqrt{12}/\eta_j)^4
=147456\,2^{-64}\delta_j^{-6}<2^{-46}\delta_j^{-6}$。
多个支集只要求 $C^4$ 范数可求和。其零延拓前四 jet 连续，所以不会
给所需 $Q_{ttt}$ 制造额外跳幅；原有限个 quintic/旧 bump 接缝的 BV
项照常保留。没有要求新 compact 方向的第五及更高导数有统一界。

## 2. 两个原参数的实际 radial 逆仍在同一复域

在 $\bar\Gamma(\Omega)$ 处，两个 phase 的归一 Jacobian 与旧两个 bump
的完整有向积分完全相同：形状支集和两 bump 分离，平移不改 phase。
故原
$$
 .085<T_1<.087,\ .058<T_2<.061,\quad
 -.023<B_1<-.021,\ -.010<B_2<-.008,\quad
 \det(T_s;B_s)>2^{-11}
$$
仍适用。第54束给
$|\bar\gamma_1|<2^{-23}$、$|\bar\gamma_2|<2^{-85}$；
全部复域仍为 $|\gamma_1|<2^{-15},|\gamma_2|<2^{-29}$。

以第二变量的增量 $q_i$ 为参数，准确求第一变量曲线
$$
 \Theta_i(\chi_i(q_i,\Omega),\bar\gamma_{2,i}+q_i,\Omega)
                       =\omega_i/4,\quad |q_i|<2^{-32},
 \qquad|\partial_q\chi_i|<2 .
 \tag{N.5}
$$
这是原完整复逆的重新应用；其输入复盘及分母界在新基点逐项保留。
令
$$
 f_i^\Omega(q)=
 \frac{\beta_i(0,\chi_i(q,\Omega),\bar\gamma_{2,i}+q,\Omega)
                          -\beta_i^0}{\sqrt{\mathcal B_i}},
 \quad \mathcal B_i=\sqrt{12}\Delta_i/\eta_j .
$$
原真实导数与 Cauchy 费用给
$$
 |(f_i^\Omega)'(0)|>2^{-9},\quad |(f_i^\Omega)''|<2^{36},
$$
$$
 f_i^\Omega(\varphi_i^\Omega(z))=z,\qquad
 |z|<2^{-267},\quad|(\varphi_i^\Omega)'|<2^{10}.
 \tag{N.6}
$$
这不是将首相位当作一个免费独立参数。所有逆由真实两 bump 方程定义。

## 3. 全部真实 principal 返回的无限 KAM

固定 $\|q\|_{\ell^\infty}<2^{-34}$，先从 (N.5) 的 radial 曲线出发。
真实两射线 map 仍使用完整
$\nu=\sqrt Q\,\sqrt D/J$ 和漂移，不能将小绝对角差当作同宽小算子。

原 KAM proof 的各项输入是：同一 $\kappa_i$、第一 phase 的真实逆、
完整角解析宽度、$n_i$ 状态界和全部参数平均行。第53束及 (N.2) 已在
新对象上重新给出这些门；仅状态粗界相对原题增加 $2^{16}$。
根图、strict flow 和正段的系数宽盒不变。因此实际小量为
$$
 \mu_{\rm KAM}<2^{304}A_*=2^{-261844}<2^{-64}. \tag{N.7}
$$
在每步当前 $h_i$ 上评价
$(D_pF_i[p])\circ h_i$，先反解真正无限平均行，再反解全部非零 Fourier
cohomological 行。旧二次收敛证明由这些同一显示门重实例化，给
$$
 \gamma_{1,i}^*(a,q,\Omega),\quad
 R_i(a,\gamma_1^*,\bar\gamma_2+q,\Omega)\circ h_i
                                  =h_i\circ T_{\omega_i/4}.
 \tag{N.8}
$$
所有层、全部角模和 $q$ 的交叉参数列保留。其逐行改动可取
$$
 |\gamma_{1,i}^*-\chi_i(q_i,\Omega)|
 <2^{39}(j+4)\sqrt j\,\delta_j^{-3/4}
                   (N_j^c)^\#\mathcal X . \tag{N.9}
$$
它们是联合全纯的 endpoint/return maps。
对平移控制的全纯性使用第53束固定段坐标；不在固定物理 $t$ 的
$C^2$ 函数空间中穿过移动接缝作未经证明的复求值。

## 4. 真首密度相位与第二无限行

实际 Jacobi 散度密度仍是
$$
 G=\mu\begin{pmatrix}1&-d\\-d&d^2-Qv^2\end{pmatrix},
 \quad\Lambda=\sqrt{-\det G},\quad
 \kappa=\frac{P(\Lambda^{-1/2})/\Lambda^{-1/2}}{\Lambda}.
$$
第49束证明的完整有限部定义在本对象上逐项重建：
$$
 \beta_i=-\frac12\lim_{\epsilon\downarrow0}
 \left\{\frac12\int_{\Omega_\epsilon}
          \kappa\,dt\,\frac{d\theta}{\pi/2}
             -\sum_{e=\pm}\frac{5b_e}{48\epsilon^{3/2}}\right\}.
 \tag{N.10}
$$
完整根图和 $\kappa\,dt\,d\theta$ 的 Piola 不变量保持；
新形状不进根，正型两端 DN 的 raw 系数也未变。
strict 部分只用已经保留的前四径向系数及实际状态上界。
所以完整首符号仍是此密度平均，且
$$
 |\beta_i(a,\Gamma,\Omega)-\beta_i(0,\Gamma,\Omega)|
 <2^{144}(j+5)^3\delta_j^{-5}(N_j^c)^\#\mathcal X,
$$
$$
 \sum_i\frac{|\beta_i(a,\Gamma,\Omega)
                     -\beta_i(0,\Gamma,\Omega)|}{\sqrt{\mathcal B_i}}
                                      <2^{160048}\mathcal X.
 \tag{N.11}
$$
差分包括两根有限部、constant canonical 到原固定 $t$ 的图差、
完整 height 密度和 normal shear；不是两个发散积分的粗绝对比较。

在 (N.8) 的真实 principal 选择之后定义
$$
 E_i(a,q,\Omega)=
 \frac{\beta_i(a,\gamma_1^*,\bar\gamma_2+q,\Omega)
       -\beta_i(0,\chi_i(q_i,\Omega),\bar\gamma_{2,i}+q_i,\Omega)}
       {\sqrt{\mathcal B_i}} .
$$
(N.9) 的完整 radial 首相位变化加 (N.11) 给
$$
 \sum_i|E_i|<2^{160056}\mathcal X,\qquad
 \|D_qE\|_{\ell^\infty\to\ell^\infty}<2^{160091}\mathcal X
 \quad(\|q\|\le2^{-256}).
 \tag{N.12}
$$
第二式是在整个复 $\ell^\infty$ 方向盘半径 $2^{-35}$ 上 Cauchy 得到，
没有逐列求导后漏掉列和。

准确第二行是
$$
 q_i=\varphi_i^\Omega(-E_i(a,q,\Omega)).
 \tag{N.13}
$$
在 $\|q\|\le2^{-256}$ 上，其像小于
$2^{160066}\mathcal X\le2^{-102078}$，
Lipschitz 常数小于
$$
 2^{160101}\mathcal X\le2^{-102043}<1/2 .
 \tag{N.14}
$$
因此同一次无限联立收缩给唯一 $q^*(a,\Omega)$，定义
$$
 \Gamma^*(a,\Omega)=
 \big(\gamma_1^*(a,q^*,\Omega),\,\bar\gamma_2+q^*\big).
$$
对全部完整内部分量，准确有
$$
 R_i(a,\Gamma^*,\Omega)\circ K_i=K_i\circ T_{\omega_i/4},
 \qquad\beta_i(a,\Gamma^*,\Omega)=\beta_i^0 .
 \tag{N.15}
$$
所有 complete mean 和源列仍在方程中。

## 5. 真实完整 $4/3$ 余项及高网络重实例

第51束的全输入、全输出证明在本对象上使用以下新输入：
(N.2)–(N.4)、同一 root germ、真固定端点 Cauchy、
两相位 (N.15) 及新角费用
$$
 \epsilon_i^c=2^{8192}(j+5)^{16}\delta_j^{-16}
                   (N_j^c)^\#\mathcal X,\qquad
 \sum_i\epsilon_i^c<2^{160048}\mathcal X<2^{-102096}.
 \tag{N.16}
$$
同样的至少26阶角 Cauchy 只作用角方向，不作用于新的径向 $C^4$ 支集。

strict 完整跨支恒等式 $K=\partial_tL-Z$ 保持。
一次分部积分作用于全 Duhamel，端项 $U_dLU$ 及
$Z+[L,K_d]+LK_{\rm cross}+LK_{\rm sm}$ 的真实顺序不变。
所有输出阶仍在原密度窗 $[-9/2,7/2]$ 内，strict 余项仍可取
$2^{4608}(j+5)^{32}\delta_j^{-56}$。
新增形状给 (N.4) 内的连续项，不增加旧有限 BV 接缝原子数。

根区的两次完整 Volterra 各给 $2/3$ 阶；全部 Fourier lag、
mean 与跨锥都在原卷积中。真正 $V,V_\xi$、height、normal shear 和
两行 Airy frame 的余量由 (N.2)、(N.16) 支付，原
$2^{6002}b_e^8$ inverse-defect 门保持。
正型原始 profile 没有改变；完整双端 form、Poisson/contact 与
源 charge 在实际非径向小背景上重新使用 (N.16)。

KAM wave 表示仍使用完整
$F_e\operatorname{diag}(U_K,U_K)F_e^{-1}$，
包括交叉块；signed-J 的两侧恒等式给真实 polar map 满射。
不把固定 Airy frame 中的 naked pullback 当作同宽小扰动。

因此全部有序复合重新给
$$
 \boxed{\quad
 \|\mathcal E_i:H^s(\hbox{相邻全部端口})\to H^{s+4/3}\|
 <C_i=2^{20000}(j+5)^{64}\delta_j^{-100},\quad |s|\le1 .
 \quad} \tag{N.17}
$$
完整低输入到无限高输出已在原全 Duhamel/Volterra 链支付，
不是在输出端乘一个输入 cutoff。
新的每一实际分量满足原全部宽盒，所以这里确实沿用原显示常数；
不是仅因“参数很小”而转授旧算子。

取同一
$$
 T_i=2^{65536}(j+5)^{204}\delta_j^{-320},\qquad
 d_i=2^{167}(j+5)^3\delta_j^{-13/2}.
$$
准确一行费仍为
$$
 d_iC_iT_i^{-1/3}
 =2^{-5035/3}(j+5)^{-1}\delta_j^{1/6}.
 \tag{N.18}
$$
相邻度数不超过8，全部行列和给真正 HH feedback 小于 $2^{-1024}$
及其 Neumann 逆。完整移动低行、两个 mean、最外分量、ordinary 和
weak source 都作为真实输入保留。

## 6. 同一最终目标及实际远端 map

固定控制 $\Omega$，标签角平移 $T_\phi a=(e^{im\phi}a_m)_m$ 不改变
任何径向形状或其两相位。完整 flow、密度有限部和两个无限固定点的
唯一性给
$$
 \Gamma^*(T_\phi a,\Omega)=\Gamma^*(a,\Omega),\qquad
 D_a\Gamma^*(0,\Omega)=0 .
 \tag{N.19}
$$
第二式用非mean Fourier 基及标签 $\ell^1$ 稠密性证明，未删 mean 方程。
固定一个最终标签的整个 phase 族因此共用同一目标度量。
若以后还让 $\Omega$ 随标签改变，其所有 metric/source 导数要另加；
本篇没有把它们设为0后用于更大的选择。

在 radial 基点 $\bar\Gamma(\Omega)$ 上，按第53束真正第四线重新停止
finite connector，再选一个实际好外参数 $t_0(\Omega)$。
此后对所有 $a$ 固定这个 $t_0$；不声称好集最小元随 $\Omega$ 解析，
也不声称这个原点好角门在每个非零背景自动保持。
内部两相位选择与全图可联合依赖 $\Omega$；
带这个逐点 $t_0$ 选择的全外对象没有据此取得全参数解析选择。

同一 $H\omega$ 不变量使 $a_*,z_*,\omega$ 及原长段 $[0,B]$
准确不变，因而已存在的周期正帽—长段 map $\Phi$ 是同一个真实算子。
定义
$$
 \mathcal F_{c,\Omega}(a)
 =k_B(a)-K_{B,\perp}(f_B(a),\Phi(c,f_B(a))).
 \tag{N.20}
$$
独立 $f_B$、两条非mean迹、mean小根和唯一高度积分全部保留。
由实际复球、raw404 和有限接口相同宽盒，
对 $65536\le\beta\le262144$ 有
$$
 s_\beta=\beta-88823/400,\qquad
 \|f_B(a)\|_{\dot A^2_{s_\beta}}+\|k_B(a)\|_{\dot A^1_{s_\beta}}
                                      <2^{-443}\|a\|_\beta,
$$
$$
 \|[D\mathcal F_{c,\Omega}(a)-D_{0,\Omega}]b\|_{\mathfrak Z_{s_\beta}}
 <2^{-400}(\|a\|_\beta+e^{-7L/4})\|b\|_\beta,
$$
$$
 \|D_{0,\Omega}^{-1}g\|_\beta\le
             \tfrac1{16}\|g\|_{\mathfrak Z_{\beta+1850}}.
 \tag{N.21}
$$
这里每一个 map 和 $D_{0,\Omega}$ 都属于这个新对象。
(N.19) 给原点固定度量 Jacobi 的正确身份。
整个 $\|a\|_\beta<1/64$ 复球确在 (N.1) 内，因为
$\|a\|_{224}\le e^{-4(\beta-224)}\|a\|_\beta
<2^{-5(\beta-224)}\|a\|_\beta$。
(N.21) 是有明确宽差的完整估计，不称作同权相对小量。

## 7. 本对象上实际 incoming 固定点重新求解

真正长段的输入仍满足
$$
 \|f_*\|_{\dot A^2_\sigma}\le r_f=10^{-8},\qquad
 S=\sigma+7L/16>10724906.843270461,
$$
$$
 g_*(f_*)=K_{B,\perp}(0,f_*),\quad
 \|g_*(f_*)\|_{\mathfrak Z_S}<18\|f_*\|,\quad
 \|Dg_*\|<24 .
 \tag{N.22}
$$
对新实际 $D_{0,\Omega}$，定义
$$
 a^{\rm in}_\Omega(f_*)=D_{0,\Omega}^{-1}g_*(f_*).
$$
用其新 raw404/good-angle 合同和最小非零频率4，重新得到
$$
 \|a^{\rm in}_\Omega(f_*)\|_{224}<2^{-60000000}r_f,\qquad
 \|Da^{\rm in}_\Omega\|<2^{1-60000000}.
 \tag{N.23}
$$
该式是新实际有界算子的像，不是旧 map 的标签值改名。

现在尾图包含完整 $\Gamma^*(a,\Omega)$。它在 (N.1) 的真实小复球上
满足 $\|f_B(a)\|<2^{-443}\|a\|$。
对 $\|a\|\le A_*/4$，沿单位方向取半径 $A_*/2$ 的 Cauchy 圆盘，
仍得 $\|Df_B\|<2^{-442}$。没有假定联合参数 map 在
$\ell^1_{224}$ 的原 $1/64$ 大球上定义。

在 $R_a=2^{-60000000}$ 球上，重新解
$$
 a=D_{0,\Omega}^{-1}
             g_*(\Phi(c,f_B(a))).
 \tag{N.24}
$$
全部 $f_B$ 都在帽原独立 $2^{-60}$ 域；
原完整帽复球给 $\|D_{f_B}\Phi\|<2^{35}$。
故此新 map 的像小于 $R_a r_f$，其完整反馈小于
$2^{1-60000000+35-442}=2^{-60000406}$。
它有唯一真正全频固定点 $a_{c,\Omega}^{\rm inc}$，
与实际帽和长段在同一个 $f_B(a)$ 上同时取值。

仍须保留准确剩余：
$$
 \mathcal F_{c,\Omega}(a)
 =R_T(a)-E_B(f_B(a))-M_B(f_B(a),f_*).
 \tag{N.25}
$$
$R_T=k_B+\mathsf C_Lf_B-D_{0,\Omega}a$，
$E_B=K_B(f_B,0)+\mathsf C_Lf_B$，
$M_B=K_B(f_B,f_*)-K_B(f_B,0)-g_*(f_*)$。
这是新 joint map 的完整恒等式。

只用 (N.1) 的实际小球时，二阶 Cauchy 系数应诚实地放宽为
$\|R_T(a)\|_{\mathfrak Z_{\sigma_B}}
<2^{261710}\|a\|_{224}^2$，$\sigma_B=777/400$。
不能沿用旧固定参数在 $1/64$ 球得到的更小二次常数。
结合真实长段的 $E_B,M_B$ 门，在上述新 incoming 固定点有
$$
 \|\mathcal F_{c,\Omega}(a)\|_{\mathfrak Z_\sigma}
 <2^{-119738000}. \tag{N.26}
$$
它没有被设为0，而且 (N.26) 的角宽不足以再次直接喂给
$D_{0,\Omega}^{-1}$。在更宽标签球上的有限 Newton 链可以由 (N.21)
重新执行；任意有限步都不能取代无限闭合。

## 8. 保留的真实缺口与全部源

新径向中频控制的实际 Wronskian gap 已可在自己的角宽损耗下消费。
但把其逆直接乘非径向绝对状态 $N_j^c\mathcal X$，并不保证同权小：
在接近真实 $T_i$ 的移动中频中，完整分母可以远小于该绝对量。
(N.17)–(N.18) 只闭合 HH，不闭合这一中矩阵。
仍须证明实际非径向 Schur 的相对逆/联合控制，
并将 $H D_0^{-1}EG$ 送回原相同标签与 source 空间。

ordinary、weak、两端 total/bare 区分及两个 mean 一直保留。
实际参数变化采用第53–54束的完整 $\delta G,\delta^2G$；
非径向处微分真正 Darboux 方程和 mean 小根，
不把 radial $G$ 当成 updated Jacobi 系数。
物理固定半径还含停止尺度项 $A\,\delta\ell$；
平均高度始终是
$Z_e-\int_{a_e}^a w$，保留 $w_e\delta a_e$ 和唯一 $\lambda$。
只有 (N.25) 真正为0时，两边相同非mean两迹才强迫两个 mean 小根相等。
本篇没有提前宣称全部曲面已接合或 README 完成。

[新严格预算程序](../scripts/fourfold_controlled_tail_actual_joint_phase_and_remainder_20261114.js)
和[原生执行记录](../notes/2026-11-14-R119-controlled-tail-actual-joint-phase-remainder-budget.json)
为新的纯 V8 / BigInt 有理计算；没有恢复或冒称原 Python native。
