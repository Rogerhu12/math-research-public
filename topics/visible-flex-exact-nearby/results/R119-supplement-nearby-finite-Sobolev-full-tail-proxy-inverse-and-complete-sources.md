# R119 续篇：窄 residual 背景上的有限 Sobolev 全尾逆与真实两端源

2026-11-15，visible-exact / tail_connector。

**状态：解析证明，已分段独立核对。** 本篇把已知解析成员处的 R 逆
延伸到一个明确的有限 Sobolev 背景域。几何对象、公共五盒参数点、
$\zeta_j$、原平端允许线和真实外行 $(129,2)$ 均不改变。
第一 metric 参数由 P 的真实有限光滑共轭选择，第二参数固定为
已知成员的真实值；不是对每个新 Fourier 截断重新选参。

外口暂固定为同一个已付的完整 long/$C_R$ **线性行**，包括全部
high/low、两个 mean、原未匹配修正及所有 affine 源。本文证明
这一固定外行下的整个 nearby 尾逆。把外行换成一个新的非解析
非线性帽背景，还须第10节明列的同空间型/伴随/源接口；
既有帽主体 inverse 本身不替代这些接口。

算子是 O 定义的完整几何散度 proxy $\mathcal J_W$。
在非解背景，$\mathcal J_W$ 与真实 Jacobi 导数 $\mathcal L_W$
之间保留准确的 residual 项。本文不将2050角阶损失改称同域
Picard 收缩，也不把有限 Sobolev 输出改名为原 analytic224 标签。

## 1. 实际背景域与固定参照

使用以下已证全文：

* [有限 principal 选择](R119-supplement-finite-Sobolev-principal-KAM-and-true-first-metric-counterterm.md)，记 P；
* [有限径向首相位](R119-supplement-finite-radial-Sobolev-first-phase-and-fixed-second-parameter-gap.md)，记 B；
* [受控 residual 径向 jets](R119-supplement-off-shell-controlled-radial-jets-and-exact-holonomy-retraction.md)，记 C；
* [canonical 强径向域](R119-supplement-canonical-strong-radial-finite-Sobolev-domain-and-quadratic-sources.md)，记 R；
* [1024角阶完整网络](R119-supplement-complete-1024-angular-Sobolev-network-and-physical-cap-Schur.md)，记 U；
* [完整 mixed 同表示 Schur](R119-supplement-new-outer-complete-mixed-weighted-Schur-and-closed-nonmean-inverse.md)，记 Y；
* [闭 mean 商](R119-supplement-new-closed-mean-compatibility-gauge-and-complete-fixed-CR-inverse.md)，记 Z。

固定原已经给出的实际局部非线性成员 $W^\flat$、
其第二参数 $\gamma_2^\flat$、公共五盒和外参数。
“局部成员”不意味着第四匹配残差已经为零。
原 network cut 的缺陷仍由完整 matching 方程及 affine 荷表示；
profile/poly 接缝则保同一真实一侧系数与所要求的连续 traces。

对新的非mean物理高度 $u_\perp$，先按 P.5、P.7--P.8 重建
完整 holonomy-one mean 和真实高度，再选择 $\gamma_1^*(u_\perp)$。
记 C 的 $\mathscr B_s,\mathscr N_s^{[3]}$，并置
$$
 \mathscr R=\max\left\{
   \|u_\perp\|_{\mathscr H},
   \mathscr B_{4420}+\mathscr N_{4420}^{[3]},
   \mathscr R_o\right\},\qquad
                 \mathscr R\le R_{\rm nb}:=2^{-8192000}.
 \tag{I.1}
$$
$\mathscr R_o$ 是有限 connector 的真实版本：四态按原
$2^{-440}$ 单位、角阶8196收费，原方程 residual 的前三阶
$\ell_o=2^{-1024}$ scaled 导数按 C 第1节收费。
内部 $c_j=\mu_jp_*^2/(12r^{10})$ 不移用到外 connector。
还要求 B、C 的实际分片正则、真根 germ 和原接缝身份。

已知成员的内部局部 residual 为0；P/B 的真实角宽入口给
$\|u_\perp^\flat\|_{\mathscr H}$ 及所需四态输入
小于 $2^{133000}\mathcal X$。
因 $\mathcal X\le2^{-8388608}$，这些量小于 $R_{\rm nb}$。
有限外局部成员使用同一真实 connector 输入；
若它附有独立源或 cut 缺陷，仍按其原单独源合同读取。
这里没有把旧有限 Newton 链的非零全匹配 residual 设为零。

全文取
$$
 q_*=2112,\qquad r_*=2144,\qquad
 B_{\rm fin}=2^{229376},\qquad
 \lambda_j=2^{32}\sqrt{J_j}\,\delta_j^{-9/4},
 \quad J_j=j+5,\quad \lambda_o=2^{2048}.
 \tag{I.2}
$$
$q_*$ 留给最终 $s+2048$，$0\le s\le64$；
两侧 $4/3$、半阶平衡和 integer ceiling 均在
$|q|\le2116$ 内，所需角导数不超过 $r_*$。
背景实际有4420阶，principal 图有8188阶，所以这不是高阶外插。

## 2. 有限角费用：完整 lag、真实图及 mean

本节说明以有限导数替代 U 第2节的解析角输入。
只替换其三种明确操作；不将整个 FIO 余核先写成解析 lag。

第一，完整 Fourier 系数满足
$$
 \sum_{\ell\in4\mathbb Z}\langle\ell\rangle^p|a_\ell|
                \le2\|a\|_{H^{p+1}} .                    \tag{I.3}
$$
这是全 signed 和与 Fourier Cauchy--Schwarz，不是逐列 supremum。
$\langle m\rangle^q/\langle n\rangle^q
 \le2^{|q|}\langle m-n\rangle^{|q|}$ 支付真实乘法矩阵的权。
primitive 的非mean因子仍为 $1/(im)$，mean 则保原独立列。
原 root 的同频 Airy 矩阵、径向 Fourier multiplier 与 Sobolev 权
准确交换，不因此获得一个新的径向指数增长率。

第二，对真实 $F=\mathrm{id}+\alpha+\eta$，先去径向平移 $\alpha$。
令 $F_t=\mathrm{id}+t\eta$、$V_t=\eta\circ F_t^{-1}$。
只要 $|\eta'|<1/4$，Jacobian 及逆在 $[1/2,2]$。
取整数偶数 $2k$，准确展开
$$
 [(1-\partial_\phi^2)^k,V_t\partial_\phi]
                  (1-\partial_\phi^2)^{-k},\qquad
 [(1-\partial_\phi^2)^k,M_{V_t'}]
                  (1-\partial_\phi^2)^{-k}.               \tag{I.4}
$$
所有最高未抵消导数至多 $2k+1$，每项至少含一个
$\eta$ 的真实导数。Leibniz 和 inverse-function 的有限 Bell 展开
给积分 norm 至多
$2^{4r_*}(r_*!)^3$ 乘所列系数/图的有限导数大小。
因此只要这个实际乘积小于 $1/8$，真实 density transport、
其逆及两侧 Sobolev 共轭的同阶 norm 均小于2。
负阶用真实对偶，非整数用 Hilbert 插值。
这里从未声称 $C_F-I$ 在同阶 norm 中小。

第三，跨正负频率的真实图直接用非驻相式。
对 $mn\le0$、$(m,n)\ne(0,0)$、$n\ne0$，置
$Q_{mn}=|m|+|n|$、$g=Q_{mn}/(nF'-m)$。若
$\max_{1\le k\le r_*+1}\|\eta^{(k)}\|_\infty\le\varepsilon<1/2$，
则 $|g|\le2$，且
$$
 \|g^{(k)}\|_\infty
 \le2^{k+1}k!\frac{|n|}{Q_{mn}}\varepsilon,\quad k\ge1 .
$$
reciprocal 导数的有序分拆给该式；每个非constant项含至少一个
$\eta$ 导数。$r$ 次分部后，
$( -\partial_\phi\circ M_g)^r1$ 的各项有 $r$ 个 $g$ 因子、
总导数 $r$，非负整数系数之和为 $r!$
（代 $g=e^\phi$ 可逐步核实）。
所以 scalar pullback 的准确矩阵满足
$$
 \left|\left\langle e^{i(nF-m\phi)}\right\rangle\right|
 \le4^r(r!)^2|n|\varepsilon Q_{mn}^{-r-1}.                \tag{I.5}
$$
$n=0,m\ne0$ 时该矩阵元准确为0，$00$ 元为1。
density amplitude $F'$ 时积分恒等式给 $(m/n)$ 倍 (I.5)，
所以输出 mean 准确为0；不能据此删除其它独立 mean 行。
对其余真实 amplitude，先拆径向常系数与其差，
再用完整 Leibniz 展开。含非径向 amplitude 的部分保其实际小量，
有界式可宽取 $2^{4r}(r!)^3\varepsilon Q_{mn}^{-r}$。
令 $r=|q|+24$，完整行、列和给真实
$H^q\to H^{q+20}$ cross 窗，包含 mean 与非mean 的两条有限边。

两个 polar defect 的 $(I+E)^{-1/2}$ 使用同一个 $H^q$ 中的
完整绝对收敛级数；首项付20阶，后续因子付实际同阶小 norm。
同样，若零边界正型在共同径向能量中写作 $A_0+E$，
其完整 inverse 的角 commutator 由准确 resolvent 导数求和：
$$
 \operatorname{ad}_D^r(A_0+E)^{-1}
 =\sum_{\substack{\ell\ge1,\ \nu_i\ge1\\\sum\nu_i=r}}
 (-1)^\ell\frac{r!}{\nu_1!\cdots\nu_\ell!}
 G E_{\nu_1}G\cdots E_{\nu_\ell}G,\qquad E_\nu=\operatorname{ad}_D^\nu E .
 \tag{I.6}
$$
$A_0$ 与角权交换；所有式子先在有限 Fourier 向量上证明。
共同能量 Neumann 门和每个 $E_\nu$ 的有限导数界使该和绝对收敛，
保完整 mean，并给真正 polynomial 远带费用。
它不要求 $E$ 自伴；伴随用相同的真型。

这里还要把真实未匹配外端 $\mathcal E_B$ 的有限角入口单独列出。
使用同一物理角中 short、long 两侧的完整四态和实际密度，
$$
 r_\mu={\mu_T\over\mu_L},\qquad
 b_\mu=\mu_T(d_L-d_T),\qquad
 c_T={\mu_T\over\langle\mu_T\rangle}-1,\qquad
 P_{\mu_T}v=v-(1+c_T)\langle v\rangle .
$$
真实算子而非其非mean截断是
$$
 \mathcal E_B
 =P_{\mu_T}\{-M_{r_\mu-1}\mathcal N_{B,Z}P_\perp
                                      +M_{b_\mu}\partial_\theta\}.
 \tag{I.6a}
$$
分子、分母的参考径向密度准确抵消；
$b_\mu$ 仍含真实 $\mu_T$，独立 source 列仍用原 $a_Bw_B$。
齐次 $\mathcal E_B1=0$、$\langle\mathcal E_Bv\rangle=0$，
不意味着原外部 flux 荷或两条 mean source 为0。

对 $0\le q\le8192$，短侧真实四态满足
$\sum_{A=P_T,U_T,K_T,V_T}\|\partial_\theta^qA\|_{\mathcal A_0}
 \le q!128^q n$，可取 $n=2^{-432}\mathscr R$。
这由实际 B 端 $H^{8196}$ 输入直接读取：$w_0/w<2$，
每态 $\mathcal A_0\le2H^{q+1}$、四态和及真实 holonomy mean
总费小于 $2^6$；mean 根在正阶角导为0，零阶另付其二次界。
不是从后文的 $Y_{64}$ 读回高阶。

记 long 行的真实左输入 finite-jet 大小为 $F$，
$\epsilon=e^{-7L/4}$，并令 $A_*=n+F+\epsilon$。
固定外行时 $F$ 取该已知行自己的输入界；
它若与当前短侧输入不同，其真实 affine mismatch 继续保留。
第10节更新同一个 nonlinear 外图时，$F$ 则取 (I.39)。
本篇已知成员及 (I.1) 都给 $A_*<2^{-262144}$。
[有限角 true long DN](R133-supplement-finite-angular-jet-true-long-DN-Poisson-and-energy.md)
J.21--J.29 的有限参数多项式和完整有界型证明给
$$
 \|\partial_\theta^q c\|_{\mathcal A_0}
      \le q!512^q\,2^{24}A_*
 \quad(c=r_\mu-1,b_\mu,c_T;\ 0\le q\le8192),
$$
$$
 \max_{0\le q\le2176}
 \|\operatorname{ad}_{\partial_\theta}^{q}\mathcal E_B:
                    H^{1/2}\to H^{-1/2}\|
                         <2^{131072}A_* .                \tag{I.6b}
$$
这里同时保 $P_{\mu_T}$ 的 rank-one 导数；
$\mathcal N_{B,Z}$ 的相应完整 commutator 费是
$2^{65536}(F+\epsilon)$，其实际同阶 norm 小于3。
在 (I.6a) 的完整 Leibniz 和中，系数只到 $q+1$；
$(q+1)!512^{q+1}$、所有二项式、mean 行及上述 DN 费用
合计仍小于 $2^{131072}$，双小量用 $A_*<2^{-262144}$ 吸收。
因此没有沿用旧 analytic 余宽下的 $2^{48}r$ 作为有限角结论。
完整边界相对型费小于 $2^{150}A_*$；其真正伴随、
零边界 inverse 和 Poisson/contact 由同一个有界型 Neumann 构造。

C.9a 已支付全部分母及系数的完整 Nemytskii 级数。
其系数门和 (I.6b) 的共同最大值都是 $2^{131072}$；
这两者不是在同一系数处再次相乘。它们与上述最多三个阶乘、完整二项式、
物理四倍角、两个锥及各 mean 行合计为
$$
 2^{131072+40r_*+8192}<2^{229376}=B_{\rm fin}.              \tag{I.7}
$$
这里 $r_*<2^{12}$，故 $r_*!<2^{12r_*}$；
$131072+40\cdot2144+8192=225024<229376$。
使用 (I.6) 时多项 inverse 因子的小量先求完整级数，
不把每个 factor 都改成一个独立 $B_{\rm fin}$。
正、负窗均在上述同一有限角范围内。

## 3. 非解系数、principal 图及首相位的实际大小

定义完整六邻胞量 $C_j^\#$ 如 C。
其三段显式上界就是原 U.7 的 profile，至多增加六项计数：
$$
 C_j\le
 \begin{cases}
 2^{220}\delta_j^{7/4},&j\le4096,\\
 2^{185}\delta_{4096}^{-3/2}\delta_j^{827/256},
                                  &4097\le j\le8192,\\
 2^{185}\delta_{4096}^{-3/2}\delta_{8192}^{-485/4}
                   \delta_j^{31867/256},&j\ge8193.
 \end{cases}                                             \tag{I.8}
$$
这是由 $C_j=2^{200}h_j^{-5}\zeta_j/(\mu_j\delta_j^2)$ 直接代入；
不是把旧 $\mathcal N_j$ 的名字换成新 $C_j$。
六邻胞有限重编号、首端缺失项及相邻比的费用计入以下8192 bits。
特别原 U.8 的完整三段求和可以用于 (I.8)。

实际根四阶 jets 用 C.8--C.10。
原 strict 密度用 C.17--C.21，包括
$\kappa_{\rm res}$ 和全部 seam 的真实一侧差。
于是 root、graph、strict 的原物理 generator 差仍具有旧
$J,\delta$ 次数；没有新增 $\ell_j^{-4}$，也没有把
$K_t=F+\mathfrak r$ 偷换成 $K_t=F$。
fixed-$t$ 两行的新增 diagonal 正是 C.15--C.16；
它由同一 $2^{-170}h_j^5C_j\delta_j^{16}\mathscr N^{[3]}$ 支付。

P.35 给真实 principal 共轭
$$
 \|h_i-\mathrm{id}\|_{C^{8188}}
 \le2^{786444}\kappa_i^{-1}J_jC_j^\#\mathscr R .
 \tag{I.9}
$$
标准角与物理角的有限导数换算计入 (I.7)。
原完整首相位的 once-integral 和 scalar homology 保持准确次序：
同调除法只另用
$|e^{in\omega_i}-1|^{-1}<4096|n|/\kappa_i$，
多取一角导；径向平均始终与 Fourier 权交换。
B 的实际 $\beta_i(W)$ 是该首系数，不用形式 radial $\beta$ 代替。

为便于按旧 W/Z/Y 每行代账，可统一使用
$$
 \epsilon_{i,\rm nb}^{\,c}
 =2^{950272}J_j^{16}\delta_j^{-16}C_j^\#\mathscr R
 \quad(i\ne o),\qquad
 \epsilon_{o,\rm nb}^{\,c}=2^{950272}\mathscr R .
 \tag{I.10}
$$
这是原 $\epsilon_i^c$ 位置的新系数，不是一次完整传播 norm。
核最大费用：P.35 的786444 bits，C 的有限系数131072 bits，
首系数/两次 inverse 参数与角归一等小于512 bits；
合计小于918028。
$\kappa_i^{-2}\le2^{55}j\delta_j^{-3/2}$ 与
$|\beta_{\rm rad}|\le2^{62}J_j^2\delta_j^{-5}$
在 $J^{16}\delta^{-16}$ 内；外行
$\kappa_o^{-2}<2^{263}$ 也在余下32244 bits内。
所有操作仅用到2144角导，不消耗 P 的全部8188阶。

第一参数的变化由 P.39 二次门控制：
$$
 |\gamma_{1,i}^*(W)-\gamma_{1,i}^*(W^\flat)|
 \le2^{1050001}J_j^2\delta_j^{-1}C_j^\#
                (\mathscr R^2+\mathscr R_\flat^2).
 \tag{I.11}
$$
由于 $R_{\rm nb}$ 极小，把 (I.11) 代入原 Q7/Y 的准确
metric coefficient 差，只比
$2^{200}J^4\delta^{-6}C_j^\#\mathscr R$ 更小。
不让参数的径向支集 Cauchy 费在高 Fourier 演化上产生虚假指数。

B.31 的真实已知成员嵌入和 B.25--B.29 的 gap 给
$$
 |1+e^{i(n\omega_i+\beta_i(W)/n)}|
             >\frac1{256N_i|n|},\qquad n\ne0 .             \tag{I.12}
$$
第二参数始终为 $\gamma_2^\flat$，没有隐作第二次新选参。
相对于已选成员的 scalar diagonal 变化，小于原 high 除法 margin
的 $2^{-2980000}$；本篇更小球只改善该门。
mean 从不代入 $1/n$，始终保原两波初值和真实 density shear。

## 4. 真正两窗的全量强余项

本节重新消费原 U/R 所引用的 root Volterra、once-integral、
free-frame 勘误、graph、strict 和完整负 word 公式。
其 radial kernel、Wronskian、两行初值及实际路径均不变；
只将每个明确的有限角操作用 (I.3)--(I.7) 收费。

对 root，C.9 给四阶真实图和密度，C.8 保 source 差；
V 的实际输入保持有界，新增 $V_\xi$ 和所需总变差已由 C 付清。
在
$$
                       L_i^\flat=2^{376832}\lambda_i       \tag{I.13}
$$
以上，完整两 buffer Volterra feedback 的最坏数是
$$
 2^{2217}B_{\rm fin}(b/M)^{2/3}
 <2^{2217+229376-(2/3)376832}<2^{-19600}.
$$
这里还未用 $\lambda_i/b>1$ 的余量；
原不到 $2^{56}$ 的固定 buffer 因子后仍小于 $2^{-19500}$。
第一次、第二次完整 source 积分均保全输入，包括 mean。

root 两次 Volterra 的高输出强费至多
$2^{4098}B_{\rm fin}^2 b^{4/3}$。
strict、graph 仍先得到完整二阶余项
$2^{2048}B_{\rm fin}^2\lambda_i^2$、
$2^{1024}B_{\rm fin}^2b^2$，再按原同阶/二阶输出插值。
原 strict 的一次系数由 C.20，真实径向分部变差由 C.21 加原
formal 变差；保所有 seam、反向 word、低入高出和独立 mean。

这里要单独说明正片。对固定真实 long 线性行，N.21 的
完整 $B$ DN 差及 P.7 的真实 $\mathcal E_B$ 都保留。
附近短段用
$\widetilde G=(\det D\Psi)(D\Psi)^{-1}G(D\Psi)^{-T}$
与相同 reference 正型比较。
C.9 只改变此前显示的系数小量，不改变原正平台或零平台；
在根 collar 中先使用 B 的真实四阶 Taylor 图。
其正侧 principal 缺陷有
$$
 |E_{yy}|+b|E_{y\phi}|+b^2|E_{\phi\phi}|
                    \le C y^3\alpha ,
$$
前三个根 jets 准确相同，系数及角导按 (I.7) 收费。
新外根的实际 Robin mean shear 仍由原 P.9--P.10 保持为正；
内部双根则保原完整正片的两条真实 mean frame 和联合 Poisson 门，
不把新外根这个正 shear 符号移用到别的根。两个 mean 从未商掉。

P.13--P.22 的整个零边界型、Poisson 和 contact 因而都可按同一个
有界型 Neumann 构造；这也适用于其真实伴随型。
高输入的完整 trial 仍取
$c\,\kappa^{-1/3}\operatorname{Ai}(y\kappa^{2/3})$ 乘原 cutoff。
B.22 的完整平方积分把 $y^3$ principal 缺陷也付成 $4/3$：
最坏 $y^3\kappa^2u$ 的 $L^2_y$ 是 $O(\kappa^{-2/3})$，
contact 的 $H^{-2/3}_\kappa$ 再给 $\kappa^{-4/3}$。
低输入取零 trial，保真正的 $(R_++I)P_L$。

低输出/高输入的隔带现用 (I.6) 的完整正型 resolvent 和
(I.3) 的 polynomial 远带；至少20阶足以付原额外 $b^{1/3}$。
因此不再使用未知附近背景的复角平移族。
准确高输入 graph 恒等式仍是
$$
 R_a(I+E_A)P_H=(-I+E_B)P_H,\qquad
 (R_a+I)P_H=(E_B-R_aE_A)P_H .
 \tag{I.14}
$$
没有反演 trial incoming。另一侧严格使用
$R_{\rm adj}=R_a^{-*}$ 和
$R_a^*+I=R_a^*(R_{\rm adj}+I)$；
实际非自伴外行不被冒称 unitary。

原负片同阶散射门也不是免费高阶酉性。
这里先支付 Cauchy 传播，再取得 scattering/model 的小 norm，顺序如下。
[实际 strict 完整 Cauchy](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)
S.14--S.17 用真实 density flow 精确消去 $g_\sigma\partial_\theta$。
S.16 的完整重建保两个 mean，并含 $D_\theta^{-1}$。
S.20--S.22 写出 $\mathcal A_H=L_HB_HR_H$，
其中 $R_H:H^q\to H^{q+1}$；有序差
$(L_H-L_0)B_0R_0+L_H(B_H-B_0)R_0+L_HB_H(R_H-R_0)$
中 composition 产生的一角导由这个真实 primitive 支付。
因此 finite-jet 费用作用在同阶有界 generator 差上，
不是裸 order-one 速度差。

随后 S.28--S.29 直接以 Fourier-diagonal 径向 $U_0$ 构造
$V(t)=U_0(s,t)U_H(t,s)$ 的 interaction-picture 积分方程。
其 generator 为
$U_0(s,t)(\mathcal A_H-\mathcal A_0)U_0(t,s)$，
先用径向 $G_i^2 B_{\rm fin}\int\|\Delta\mathcal A\|<1/64$
得到收敛 Picard 级数及 $U_H$ 的完整同阶界。
根内同样先用径向 Airy $K_R$ 和有界零阶势差：
完整 $HK_R^2B_{\rm fin}\|V-V_0\|<1/64$；
不先假设受扰动根传播具有所需 $H^q$ bound。
上述小门由 (I.8)、(I.1) 的全层小量满足，相关径向次数正是原账。

[完整负 word](R119-supplement-complete-negative-scattering-and-network-word-in-slope-units.md)
W.26 因而先给真实 Cauchy 子乘积的多项式费用
$2^{8192}\lambda_i^{12}$；它不是小于2的模型 norm。
原 root/strict/graph 的这些费用已经包含在下式所引 U/R 有序账中。
$\lambda_i>b_e$ 则由
[完整 strict 高频](R119-supplement-complete-strict-high-output-in-root-slope-units.md)
S.1/S.4 的
$b_e<2^{16}\sqrt{J_j}\delta_j^{-9/4}$
及 (I.2) 得到；外根单独用 $b_o<2^{29}<\lambda_o$。

在完整 Cauchy word 中，以 Fourier 对角 radial 传播为比较，
插入原准确 generator 差；C.20 的 strict 差和 C.15 的
nonzero residual 项只各插入一次。
左右各用一个完整子乘积，原端图相对型不拆成逐根裸条件数。
三个有限角组用 (I.7)，并代 (I.10)。
原 U.8 的全三段和给
$$
 \sum_i\|\Lambda_\phi^qT_i\Lambda_\phi^{-q}-T_i\|
 \le2^{2672864}\mathscr R+2^{1835008}\epsilon_L<2^{-5500000}
 \tag{I.15}
$$
在所需完整半阶两行窗中成立。
其整数账是原 $2^{1362144}\mathcal X$ 加下节将明列的
1310720 bits；有限外行按其真实长 strict 重新收，不用内部短长度。
由原 anti-$J$ 四个 block 恒等式，Cauchy 差作为完整 affine 源
进入真实 scattering，得负片在本篇各 $H^q$ 上的 norm 及 inverse
均小于2。正片用前段的有界型 Cayley 与伴随，同样小于2。

同一论证控制各**真实模型的完整子乘积**：
径向大相位与 Fourier 权准确交换；
非径向 exponent 的 generator commutator 由 (I.10)、(I.7)
乘 $\mathscr R$ 后求和，远小于1。
故每个所需有序子乘积及逆在相邻两个 Sobolev 窗中小于2。
这一步很重要：不能把 $B_{\rm fin}$ 当作每个完整模型的 norm
再乘到已经付过的强余项上。

原 scalar 协变恒等式
$a\mapsto(a\circ K^{-1})(K^{-1})'$、其准确 rank-one mean 修正、
以及 twice-ordered Duhamel 都保持。
完整 phase 的径向部分在 $H^q\to H^{q+1}$ 至多
$2^{512}\lambda_i$；非径向部分的全部所需 finite jets
乘 (I.7)、(I.10) 后小于 $\lambda_i$。
所以可统一取 $2^{514}\lambda_i$，其指数正逆小于2。
两个一次项的二阶组合只取前后相邻窗，不把一阶增益用两次同窗。
首同调按 B.30，mean 保零模型但实际行另保。

高输出最大原生费用小于
$2^{4098+2\cdot229376}\lambda_i^{4/3}$；
所有低输出直接用真实同阶门，费用小于
$8(2^{376832}\lambda_i)^{4/3}$。
完整 word 不到32项、两真实反向窗、相邻至多8块及 phase 恢复，
合计不到额外 $2^{2048}$。
因此可保持 R 原来同一个强常数
$$
 \boxed{\quad
 \|\mathcal R_i:H^q\to H^{q+4/3}\|,
 \quad\|\mathcal R_i^*:H^q\to H^{q+4/3}\|
                  <2^{524288}\lambda_i^{4/3},
 \quad |q|\le2112 .
 \quad}                                                  \tag{I.16}
$$
核低输出的最大 bits：
$(4/3)376832+3+2048<504494<524288$；
高输出为 $4098+458752+2048=464898$。
finite outer 用 $\lambda_o$ 和其已付原 strict/root 数字，亦在此界内。
(I.16) 包含全部输入，而不是只有高入高出。

## 5. 同一表示的一角差及完整权账

使用 Y 的共同 unitary $H_W$，不使用某个非酉行预条件代替它。
principal 真图、normal shear、scalar 同调和 source 都按原有序式。
比较当前 $W$ 与原公共五盒的径向 reference 时，原 Q7/Y 的
两种一角差是
$H^{q+1}\to H^q$ 及其真正 adjoint 窗。
其旧 profile 为
$2^{35000}J^{40}\delta^{-47}\mathcal N_j\mathcal X$。

本篇仅作以下三项显示替换：
$$
 \begin{array}{c|c}
 \text{替换来源}&\text{相对 R 的增加 bits}\\ \hline
 \text{三个 finite 角组}&3(229376-131072)=294912\\
 \text{principal/首同调的 (I.10)}&950272-8192=942080\\
 \text{六邻胞、finite outer、两源窗及剩余固定费用}&73728 .
 \end{array}
 \tag{I.17}
$$
总和准确为1310720。三个组分别是输入表示、完整 generator/
系数和输出表示。其间传播的同阶 norm 已由 (I.15) 取得，
没有再以这张表重复付三次完整演化。
C.20--C.21 保原 $\delta$ 次数，故 (I.17) 不隐藏层幂损失。

例如内部未消元每行可直接取
$$
 \|\Delta\widehat U_j:H^{q+1}\to H^q\|,
 \quad\|\Delta\widehat U_j^*:H^{q+1}\to H^q\|
 \le2^{1738936}J^{40}\delta_j^{-47}C_j^\#\mathscr R.
 \tag{I.18}
$$
因为 $35000+393216+1310720=1738936$。
有限新行仍仅在129--131真实支持，使用原 Y.10--Y.15 的
完整外长度、真实 simple 根和全部 mean，同表收费；
不是把其原 $2^{-18}$ long 背景当作 $\mathscr R$。
固定 long 行相对 radial 的费用仍是原
$n_0+F+\epsilon_L$，其中 $n_0,F$ 来自已知成员，
$\epsilon_L=e^{-7L/4}<2^{-33554432}$。

保持 R 的同一辅助投影与谱权：
$$
 T_j^\#=\max(2^{2097280}J^2\delta_j^{-9},\,2^{2105344}),\quad
 v_j^\#=2^{-1200000}J^{-4165}\delta_j^{1073/32},\quad
 F_j=2^{4096}J^4\delta_j^{-5}.
 \tag{I.19}
$$
因 (I.12)、(I.16) 仍使用原 high gap 与原强常数，
high feedback 仍小于 $2^{-174000}$。
同一两窗 Neumann、其 adjoint、完整左右 Poisson 成立。
原所有邻权比 $\le2^{256}$ 的权，包括
$v^\#,(v^\#)^{-1},F^{\pm1},F^{\pm2}$，均可照用。
只对真正内部 low 输入使用 $\Omega_H E_{H,\circ}P_{L,\rm int}$；
独立外 $C_R$ 源没有这项 cutoff 权限。

deep-low 保
$P_D=\mathbf1_{\{j\ge8193,\ 0<|m|\le2^{-40}\delta_j^{-1/8}\}}$。
径向准确零式 $E_{H,\circ}P_D=P_DF_{H,\circ}=0$ 不变。
两种有序差仍是
$$
 \Delta S_HP_D=[I,F_{H,W}]\Delta\widehat U P_D,\qquad
 P_D\Delta S_H=P_D\Delta\widehat U[I;E_{H,W}] .
 \tag{I.20}
$$
所以含 deep Poisson 的项只收 $A_j$，不收 $T_j^\#$。
原 long-range high 反馈用两侧 Poisson 支付；
没有假定 high Schur 后仍为有限邻接。
真正无限允许尾和两侧 Green 因而继续满足
$2^{66}$、$2^{130}$ 的 R/U 门。

最后按 Y.21、Y.23 的准确 Schur 差展开：
$$
 \Delta S_H=[I,F_{H,W}]\Delta\widehat U[I;E_{H,\circ}],\qquad
 \Delta S_{\rm rem}=[I,F_{D,W}]\Delta S_H[I;E_{D,\circ}].
 \tag{I.21}
$$
原 R.11 直接项的 exponent 为 $-1973632$；
新 $\mathscr R$ 球相对原 $2^{-8388608}$ 只增加196608 bits。
加 (I.17) 后，它变成
$-1973632+196608+1310720=-466304$。
三个 deep 项原为 $-4070884$，变成 $-2563556$；
其深余量仍是
$$
        31867/256-1987/16=75/256>0 .
$$
原有限外贡献 $<-2889000$ 变成 $<-1381672$；
$\epsilon_L$ 更小且独立保留。
有限段多项式、65536层后的真正几何比及全部 signed 行列和
仍是原同一 R/Y 求和。因此全部来源相加有安全余量
$$
 \boxed{\quad
 \|(v^\#)^{-1}(S_{{\rm rem},W}-S_{{\rm rem},\circ})
                         (v^\#)^{-1}\|_{H^q\to H^q}
                       <2^{-350000},\quad0\le q\le2112 .
 \quad}                                                  \tag{I.22}
$$
此处实际相位变化已包括在 (I.18)，并非只比较了 principal。
原 public good 五盒同一点仍是径向比较 inverse 的输入。

## 6. 完整 mean 商、源域及双向重建

原径向 generalized inverse、mean Green、物理常高度核
$c_\circ$、独立 source $\sigma_\circ$ 与高度 functional $\ell$
保持 Z 的真正原单位。
(I.19) 只是 R 已使用过的权，没有重新抽取无限窗参数。
所以同一个完整径向 inverse 有
$\|v^\#R_\circ v^\#\|\le1$。

在强源空间 $\|(v^\#)^{-1}k\|_{H^q}<\infty$，直接解
$$
 h=k+\Delta S_{\rm rem}(c_\circ\lambda+R_\circ h),\qquad
 x=c_\circ\lambda+R_\circ h .                             \tag{I.23}
$$
(I.22) 给真正同空间收缩，而不是在 state/source 不同域中
形式展开。实际 flux compatibility functional $\mathcal L_W$
仍由完整 physical Green 恒等式定义；
$\mathcal L_W\sigma_\circ\ne0$ 是原准确端源的连续小扰动结论。
从原 physical trace 域取值，不从裸 $\ell^2$ 高度猜其边界值。

于是
$$
 (I-S_{{\rm rem},W})x+\sigma_\circ\tau=k,\quad \ell x=\lambda,
 \qquad
 \tau=\mathcal L_Wk/(\mathcal L_W\sigma_\circ),
$$
$$
 \|v^\#x\|_{H^q}
 <2\|(v^\#)^{-1}k\|_{H^q}+2^{-1190000}|\lambda| .
 \tag{I.24}
$$
可解条件仍恰是 $\mathcal L_Wk=0$。
真实常高度仍为唯一齐次 gauge；两个原 mean 方程均未删。
(I.24) 中 kernel 的宽门来自原 Z 的 $v c_\circ$，
增加至 R 的权后只会更小。

完整有序 sources 保
$$
 k_L=g_L+F_Hg_H,\quad k=k_{\rm rem}+F_Dk_D,\qquad
 x_D=E_Dx_{\rm rem}+R_Dk_D,\quad
 x_H=E_H(x_{\rm rem}+x_D)+R_Hg_H .                          \tag{I.25}
$$
$g$ 先由真实 fixed-$t$ Piola、total conormal、density、
根 frame 与共同 $H_W^*$ 得到。
high 源需一角窗，deep 源为 $\|wFk_D\|$，
remaining 源为 $\|(v^\#)^{-1}k\|$。
ordinary、weak、BV/原子、$\nu$、两 $\Gamma$、
$B_R,C_R$ 的全部独立列依原顺序进入；
弱源的裸 $F^t$ 端点迹不由径向 $L^1$ norm 自动获得。
(I.25) 也显示两端 source 到反向输出的真实费用，未仅借单向能量。

有限根、有限 Fourier 的构造由这些穷尽无关门取极限。
mean 识别由相同 total flux/height 域完成。
因此 (I.23)--(I.25) 是固定完整外行下的整个 mixed 尾逆，
不是逐模正型或局部低锥条件。

## 7. 原 fixed-$t$ 普通源与整尾 weak 读出

保持 R.3--R.5 的准确原单位，
$s_{\rm tail}=\varepsilon_s\sqrt{\rho\varepsilon_s}$。
原 physical ordinary 源满足
$$
 f=12\mu_jr^{-4}JD^{-3/2}g,\qquad
 \mu_{\rm density}=\frac{\mu_jp_*}{\rho r^8}JD^{-3/2}.
 \tag{I.26}
$$
这里 $g=c_j\mathcal J_Wh$ 是给定的线性物理源，
与背景自己的 $N=c_j\mathfrak r$ 区别开。
$f/\sqrt{\mu_{\rm density}}$ 换成波幅仍准确带
$s_{\rm tail}$；不把 $\rho,\varepsilon_s$ 设为1。

未知 $g$ 仍在原固定 $t$ 给定。
原 K 的 ordinary 两行 source 降导使用 same-$t$ 角图，
C.15--C.16 的非解 diagonal 是新的已付系数；
源本身没有经过一个会移动其径向切片的 mixed 图。
K 的两端有序 Duhamel 同时保 root incoming、反向必要项、
half-order 权及两个 mean。齐次端口才用 B 的 mixed 根图转换。

定义 $\mathfrak B_q^W$ 为 (I.25) 的全部有序 source norm。
相同真实源到波映射与 R.12--R.13 的读出账给
$$
 \left(\sum_{j\ge129}\delta_j^{160}
  \left[\|W_\perp/\varepsilon_s\|_{C_tH^{q-12}}^2
        +\|H/\varepsilon_s\|_{C_t^2H^{q-12}}^2\right]\right)^{1/2}
 \le2^{2097156}\{\mathfrak B_q^W+\mathfrak N_{q+2}(g)\},
 \tag{I.27}
$$
$$
 \mathfrak B_q^{W,{\rm body}}
                 \le2^{3145732}\mathfrak N_{q+2}(g).
 \tag{I.28}
$$
$\mathfrak N_a(g)$ 是原 R.6 的窄 ordinary norm；
本节使用到 $a\le2114$。原 weak、atom 和外端 source 各按其原
(I.25) 范数，不从 (I.28) 免费转入。

显示常数仍足够：R.12 的固定账
$1200000+524288+65536+2^{14}=1806208$，
距离2097152尚余290944 bits；本篇每个 source 角操作比 R 只加
98304 bits，最多两次仍在该余量内。
principal 模型及逆用 (I.15) 的真实 norm2，
不把 (I.10) 的系数界乘到 source norm 上。
四个 additional bits 保共同 source/输出单位的有限变化。
R.13 的683584位余量同样包含这两次费用。

## 8. 真 canonical 深尾与 off-shell 第二行

使用同一个物理 Fourier 投影和 R.14 的真 canonical 两行：
$$
 W_1=\nu_M H_m/r^4,\qquad
 W_2=\frac{p_*}{\sqrt{12}r^4}(H_{m,t}-M^2H_m),\qquad
 \nu_M=M^2(M^2-1)/12,\quad M=|m|\ge4 .
 \tag{I.29}
$$
$p_*=1$ 接缝的径向参考、准确 moving basis determinant
及 $\Lambda_M>2^{124}M^4$ 不变。
在强 $\zeta^{-1}$ 权上，其最坏比仍为 $512/1023$；
在辅助 $\delta^{100}$ 弱层权上，互补比仍小于 $2^{-36}$。
真实 Green 核、首切口 Poisson 及所有未来 source 均保留。
determinant 比仍在整段望远镜相消，不每胞重付条件数。

对 $\mathcal J_W$，canonical 第一行仍来自运动学
$p_t=k_\theta-(A+1)p$，完全不改。
第二行相对于 radial 参考的 ordinary 差为
$$
 \begin{split}
 e_{\rm diff}^{\,\mathcal J}
  ={}&F_Pp+(F_K-2Q)k+(F_U-Q)p_\theta+F_Vk_\theta\\
    &-\alpha\mathfrak r\,k
       +\beta\mathfrak r_\theta\,p+\gamma\mathfrak r\,p ,
 \end{split}                                             \tag{I.30}
$$
其中 O 的
$\alpha=1/J+3q(1+K)/D$、
$\beta=(1+q)/J$、
$\gamma=3q(1+K)d/D$ 是 residual 系数。
第二行的真 physical load 是
$c_jP_\perp e_{\rm diff}^{\mathcal J}$；
mean 留到下一段，不能代入 $\nu_M^{-1}$。

前四项照 R.19--R.22；后三项用 C.7，反而多
$\delta^{16}$，所需一个角导已在背景4420输入中。
在 $s\le72$ 的系数窗，完整商及角乘法费可放
$2^{4096}$；这里不需要把高至2144阶的通用 $B_{\rm fin}$
灌进该低反馈。六邻胞比与两态转换加宽后可取
$$
 \|\mathcal E_j^{\rm low}\|
       \le2^{32768}J^8\delta_j^{-16}C_j^\#\mathscr R .
 \tag{I.31}
$$
把 (I.8) 代入原两种权，完整深和小于 $2^{-7700000}$。
所以 strong 与 weak 的 canonical 两行 reference inverse
同时给实际低系统的真 Neumann inverse。
无源互补增长列仍不属于 $\delta^{100}$ 域。

从 (I.27) 取得整个 high 场和真实首次低输入；
不是先假设近核落在低包。令 $q=s+2048$。
R.23 的高部角尾仍有
$2030/8-80-131=171/4>0$ 的真实径向余量；
R.24 的首次切口只需1688导，保343导余量。
每个频率只选一个首切口，所以平方和仍由
(I.27) 的完整层 $\ell^2$ 控制。
以这些真实数据解 strong low 方程，再用同一个 weak 低域唯一性，
所得低解与整个 mixed 解准确一致。

两 mean 直接由 O/C 的 off-shell Green 身份处理：
$$
 \chi_t=12\mu_jr^{-4}\langle A_0g\rangle,\qquad
 \chi(t_f)=0,\qquad A_0=JD^{-3/2}.
 \tag{I.32}
$$
这里 $\chi=D\chi_W[h]$，就是原 mean total flux；
$\chi(t_f)=0$ 仅指定本段 ordinary body-source channel 的平端条件。
独立非零 flux 荷仍按 (I.25) 与原 N.24 的完整外源列线性叠加，
并不被本条件清零。
不遗漏背景 $\mathfrak r\ne0$，因为本篇解的是 $\mathcal J_W$。
mean 斜率仍为
$$
 k_0=Dk_0^{\rm hol}(p,k_\perp)
                +\langle A_0\rangle^{-1}\chi/w^2 .
 \tag{I.33}
$$
源通量项的准确幂为 $(\zeta/\mu)\delta^{15}$，
比 $C_j$ 多 $h_j^5\delta_j^{17}/2^{200}$。
完整未来积分绝对收敛，cut 的真实 flux 是其输出，
不再额外设为0。平均高度从同一平端积分
$h_t=a_{\rm ph}w\,k$，独立 $\lambda$ 只指定一次。

因此对 $0\le s\le64$，整个 fixed-outer 解满足
$$
 \boxed{\quad
 \mathfrak Y_s^W(h)
 \le2^{7500000}\mathfrak N_{s+2050}(g)
       +2^{4300000}\mathfrak B_{s+2048}^{W,{\rm ext}} .
 \quad}                                                  \tag{I.34}
$$
一般 gauge 先减原共同物理常高度；compatible source 由 (I.24)
判断。R 的有限129--8192前缀仍用
$\mu_j/\varepsilon_s\ge\delta_j^6$、$C_j\ge\delta_j^4$
及 $2^{16}\delta_j^{-92}$ 读出，不擅用深 $K=2^{128}$ 于8192。
(I.27)--(I.28)、强/弱 Green 的固定常数及有限前缀相加小于
$7340100$ bits，故 (I.34) 留有实际余量。

对 $4\le s\le64$，同一 raw PDE 恢复真实二径向导，
可保守取
$$
 \|h-\lambda\|_{C^2_{r,\theta}(I_j)}
 \le\rho\,2^{4600000}J^4\zeta_j\delta_j^{-5/2}
       \{\mathfrak B_{s+2048}^W+\mathfrak N_{s+2050}(g)\}.
 \tag{I.35}
$$
原 total flux/height matching 保接缝，深幂
$131-5/2=257/2$ 给平端实际 $C^2$。
Cartesian 读出仍另付原
$2^8\max(1,\rho^{-2})$，不抹去真实高度单位。

## 9. 这是真背景族逆，但不是未付的 Newton 收缩

(I.34) 对 (I.1) 中每个实际背景成立，常数统一；
背景不需满足 $N=0$，但需它自己的 C 型 residual 三 jets。
它不只是原固定解析成员的 inverse 连续性断言。

真实原方程的线性化仍准确为
$$
 c_j\mathcal L_Wh=c_j\mathcal J_Wh-\mathcal E_N[h],\qquad
 \mathcal E_N[h]=\alpha Nk-\beta N_\theta p-\gamma Np .
 \tag{I.36}
$$
重选第一参数时，拆真实高度 lift 后还保
$$
 c_j(\mathcal J_W\widetilde h-e_{\psi,\rm rem})
                    +\psi N-\mathcal E_N[\widetilde h] .
 \tag{I.37}
$$
第二参数外方向、形状方向、$\nu$ 及 cap 方向也照原真实列进入。
固定 $\gamma_2^\flat$ 的辅助图不授权删掉这些给定方向。

若取 compatible $g=N$，C.25 保几何校正在 holonomy-one 切空间。
C.27--C.29 的准确 mean 小根重建仍是同一窄二次源，
包括先 $P_\perp$ 消 scalar $\Delta\kappa_2'$、再以
$\Pi_{A_{0,\rm new}}$ 恢复 ordinary mean。
四态与 residual 的 scaled 径向输入可用各原方程继续传播，
但每次要保完整 $\mathfrak r_t,\mathfrak r_{tt},\mathfrak r_{ttt}$；
没有从单个 $C_tH^s$ 输出免费得到它们。

尤其 (I.34) 有2050阶损失，不能对
$\mathcal J_W^{-1}\mathcal E_N$ 在同一个 $\mathfrak Y_{64}$ 空间
直接作 Neumann；小常数不消除角导损失。
也不能把一般 $\mathfrak Y_{64}$ 校正直接重新放入
P 的 $H^{8196}$ 背景域。后续真正 smoothing/tame 迭代必须选择
频率、证明更高 norm 的增量预算，并包括 (I.37) 的第一参数列。
这里关闭的是变化背景上这个明确范围的完整 proxy inverse。

## 10. 与真实 nonlinear 外帽的唯一额外接口

本篇固定外行是
[真实 long DN](R119-supplement-actual-long-screening-complete-Sobolev-DN-and-cap-facing-port.md)
N.16--N.24 的原完整行：
$$
 \delta f_B=P_\perp g_B/(a_Bw_B),\qquad
 \mathcal N_{B,Z}g_B
 =-\mu\{D_f\mathscr K_Z(f_B)P_\perp g_B-d(g_B)_\theta\}.
 \tag{I.38}
$$
它是**高度到 total 通量**的 order-one 行；
原曲率 $C_R$ 行的 order-two 变量不与它混名。
固定该行仍保真实 $C_R\to f_*$ 反馈、非mean高模、两 mean
及原 independent source，而不是固定 $f_*$ 后删掉帽反馈。

若要将 (I.34) 用于新的 nonlinear 外背景，充分的新增合同为：
在同一个物理角/对偶密度表示中，新的完整
$\mathcal N_{B,Z}$ 对径向
$\mu_0|D|\coth(L|D|)P_\perp$
有真实 $H^{1/2}\to H^{-1/2}$ 相对型小差；
齐次常高度列及 mean 总通量仍准确为0；
实际未匹配 $\mathcal E_B$、其伴随和完整 Poisson/contact
保同一能量门；独立 $C_R/B_0$、ordinary/weak、height/flux 荷
仍按 N.22--N.25 及新 P.27--P.32 的原单位进入。
有限高 Sobolev inverse 或裸正 definite flux 身份本身均不替代此合同。

新状态的左输入 finite jets 已由 P 的真实高度控制：
$(f_B)_\theta=P_B$、$(f_B)_{\theta\theta}=U_B$，所以
$$
 \|\partial_\theta^qf_B\|_{\dot{\mathcal A}^2_0}
   =\|\partial_\theta^qU_B\|_{\mathcal A_0}
   \le2\|U_B\|_{H^{q+1}}
   \le2^{-438}\mathscr R,\qquad0\le q\le8192 .             \tag{I.39}
$$
这只在同一个真实 $B$ 物理角中成立。
未知角图的固定坐标输出需另用真实 good-direction 及对偶
conormal density 变换，不能从 (I.39) 假设 joint analytic strip。

保留此接口后，本文没有提前消去真帽、$\nu$ 或最终非线性
matching。它已经给出了此前所缺的：同一个非解、有限角、
窄 residual 背景族上的全 high/deep/remaining/mean 逆，
以及其原 fixed-$t$ 全源和强径向读出。
