# R119 续篇：有限 Sobolev 主返回 KAM 与第一真实度量反项

2026-11-15，visible-exact / tail_connector。

**状态：已证明。** 本篇在原 fixed-stop simple-root 对象上，
为一个明确的新有限角状态域构造完整 principal 共轭及第一真实
$\Gamma$ 参数。所有层和新增外行 $(129,2)$ 在同一个加权
$\ell^\infty$ 方程中选择，目标旋转保持原值。构造不要求未知高度
角解析；从 $H^{8192}$ 的实际圆周 map 得到 $C^{8188}$ 共轭的
四阶损失在下文用完整 dyadic 迭代证明。

本篇使用已证明的 [有限角 nonlinear mean 与高度图](R119-supplement-finite-Sobolev-nonlinear-holonomy-charge-and-height-chart.md)，
记为 M。第一参数不再只是原 analytic 标签图上一个未说明的延拓。
它确实定义在下述物理非mean高度域。第二个完整密度相位、变化背景上的
全网络 inverse 和最终非线性迭代，均不由本篇宣称完成。

## 1. 同一目标、真实物理高度与新辅助域

固定原真实形状/平移控制 $\Omega$、原第二参数
$\gamma_{2,i}=\bar\gamma_{2,i}+\mathfrak q_i$，
$\|\mathfrak q\|_\infty<2^{-34}$，以及原外部 finite good 参数。
以下常数对这些已付实盒统一，但不在粗径向函数空间中微分移动接缝。

完整指标是
$$
 \mathcal I_+=\{(j,k):j\ge129,\ k=1,2\},\qquad o=(129,2).
 \tag{P.1}
$$
使用 [完整两参数算术](R119-supplement-actual-two-parameter-complete-phase-arithmetic.md)
Q.1--Q.6 和 [新外联合相位](R119-supplement-new-outer-joint-two-phase-scalar-normal-form-and-high-feedback.md)
J.2--J.4 的同一个二次目标。
对所有 $i$，准确有
$$
 |e^{in\omega_i}-1|>\frac{\kappa_i}{4096|n|},\quad n\ne0,
 \qquad \gamma_i^{\rm D}:=\kappa_i/4096 .
 \tag{P.2}
$$
这用的是后来已经固定的二次目标，不是最早 stronger KAM K.17
仅有 $|n|^{-2}$ 的一般好集。全控制篇 N 第1节明确保持这些
$\omega_i,\beta_i^0$；外行也不使用有限主体另一个旋转数。

写相位坐标 $p$ 的 norm 为
$\|p\|_{\mathcal P}=\sup_i|p_i|/\kappa_i$。
[新外 principal](R119-supplement-new-outer-two-root-complete-principal-return-and-joint-KAM.md)
O.9--O.14 和旧内部真实曲线给
$$
 \gamma_{1,i}(p)=G_i\!\left(
       \frac{\omega_i-\Omega_i^0+p_i}{4}
       -\theta_{2,i}(\gamma_{2,i})-\theta_{\Xi,i}\right),
 \qquad |G_i'|<2^{-16}\kappa_i^{-1}.
 \tag{P.3}
$$
在已付盘 $\|p\|_{\mathcal P}<4$ 上这是真实 metric 参数。
以后只使用闭盘 $1/4$。写 $w_0=w_{\gamma_1(0)}$，
$$
 w_p=w_0e^{\Psi_p},\qquad
 \Psi_p=\sum_i\psi_{1,i}\{\gamma_{1,i}(p)-\gamma_{1,i}(0)\}.
 \tag{P.4}
$$
每点至多一个第一 bump，故
$|\Psi_p|<2^{-20}$、$|D_p\Psi_p[\dot p]|<2^{-18}\|\dot p\|_{\mathcal P}$。
全部 root germ、真接缝位置及 fixed stop 保持。

独立未知是同一物理角中的非mean高度 $u_\perp$，其角平均为0。
它在实际材料区间分片 $C^1_t$，真实相邻高度和一阶径向迹相等。
这里 $t=\log a_{\rm ph}$；在尾上与 $\log r$ 仅差固定常数。
对于参考 $w_0$ 定义
$$
 P_0=\frac{(u_\perp)_\theta}{a_{\rm ph}w_0},\qquad
 K_{\perp,0}=\frac{(u_\perp)_t}{a_{\rm ph}w_0},\qquad
 U_0=(P_0)_\theta,\quad V_0=(K_{\perp,0})_\theta .
$$
以 M.1--M.4 的原 $C_j$ 定义新 norm
$$
 \|u_\perp\|_{\mathscr H}=
 \max\left\{
 \sup_{j\ge129}C_j^{-1}\sup_{I_j}
       \|(P_0,K_{\perp,0},U_0,V_0)\|_{H^{8196}},
 \quad
 2^{440}\sup_{\mathrm{cut128}\to e_0}
       \|(P_0,K_{\perp,0},U_0,V_0)\|_{H^{8196}}
 \right\}.
 \tag{P.5}
$$
这是新的有限 Sobolev norm，不是原 $\ell^1_{224}$ 标签的别名。
允许一个独立的真实平端总高度 $\lambda$；它不进入 (P.5)。
置
$$
 R=\|u_\perp\|_{\mathscr H}\le R_*:=2^{-2097152}.
 \tag{P.6}
$$
原 $\zeta_j$、$\mu_j$、深首剪切和 fixed-stop 几何均未改。

对每个 $p$，四个非mean态准确乘 $e^{-\Psi_p}$。
以 M.9 的唯一小根补全
$$
 \Phi_{w_p^2}(P,K_\perp+\varkappa)=0,\qquad K=K_\perp+\varkappa.
 \tag{P.7}
$$
该式要求真正 nonlinear holonomy 为1，不要求 nonmean PDE residual 为0。
所有尾区有 $w_p^2<1/4$；新增负 connector 上
$w=a/(4\omega)$、$a<7\cdot10^{-6}$、$\omega>2^{359}$ 给更强的同一门。
M 的可去商、真实 mean 和 tame 小根因而适用于整条 (P.1) 路径。

总物理 mean 高度取
$$
 H_0(t)=\lambda+
   \int_{t_f}^t a_{\rm ph}(s)w_p(s)\{1+\varkappa(s)\}\,ds .
 \tag{P.8}
$$
原参考高度已包含在其中；correction mean 是另一个积分
$\int a_{\rm ph}w_p\varkappa$。第一参数变化时不能只固定后一个积分，
也不能在每胞重新令 mean 高度为0。principal 系数不依赖独立常数
$\lambda$，但 (P.8) 的真实外端高度以后仍是匹配列。

## 2. 非解背景上的准确 principal 流

令 $q=w_p^2$、$E=1+q$，继续使用 M 的
$$
 D=1-q(2K+K^2+EP^2),\quad J=1+K+EU,\quad
 d=\frac{E(V-P)}J,\quad v=\frac{\sqrt D}J,\quad Q=-(\log w_p)_t.
$$
直接对 M.15 的完整商式求导，得到
$$
 {\cal F}_V=2d,\qquad {\cal F}_U+d^2=Qv^2 .
 \tag{P.9}
$$
后一式可乘 $J^2$ 核对；所需代数为
$(1+K)J-E(2K+U+K^2+KU+qP^2)=D$。
没有使用 $K_t={\cal F}$。所以当前非解背景也有同一个真实 principal
特征，不能把其 residual 当成改变这两项的理由。

在每个真实完整负分量，两支流和 return 准确为
$$
 (F_\sigma)_t=-d(t,F_\sigma)-\sigma\sqrt Q(t)\,v(t,F_\sigma),
 \quad F_\sigma(t_-)=\mathrm{id},\qquad
 {\cal R}^{\rm ph}_i=F_-^{-1}\circ F_+ .
 \tag{P.10}
$$
只沿实 $t$ 和实角解 ODE。两个可积平方根端点原样包含；
$\Gamma$ bumps 与这些端点分离。径向 return 是
$\theta-2\int_{I_i}\sqrt Q\,dt$，与 O.8/O.17 的符号相同。
不需要将未知 finite-Sob 函数评价在一个复角或 mixed root 图上。

置标准角 $x=4\theta$，将准确径向平移先扣去：
$$
 {\cal R}_{i,p,u}(x)=x+\omega_i+p_i+f_i(p,u,x).
 \tag{P.11}
$$
完整 $K_0=\varkappa$ 留在 $d,v$ 中。它不是删除 mean 后定义的近似 map。

## 3. 有限角的真实 return 预算

写 $C_j^\#=C_j+\mathbf1_{j\ge130}C_{j-1}$，$J_j=j+4$，并定义
$$
 E_i=2^{524288}J_j C_j^\#\ (i\ne o),\qquad
 E_o=2^{524288}.
 \tag{P.12}
$$
在 (P.6)、$\|p\|_{\mathcal P}\le1/4$ 上，真正 maps 满足
$$
 \|f_i\|_{H^{8192}}\le E_iR,\qquad
 \|D_pf_i[\dot p]\|_{H^{8192}}\le E_iR\|\dot p\|_{\mathcal P},
$$
$$
 \|D_uf_i[\dot u]\|_{H^{8192}}\le E_i\|\dot u\|_{\mathscr H},\qquad
 \|D_u^2f_i[\dot u,\dot v]\|_{H^{8192}}
       \le E_i^2\|\dot u\|_{\mathscr H}\|\dot v\|_{\mathscr H},
$$
$$
 \|D_p^2f_i[\dot p,\dot q]\|_{H^{8192}}
       \le E_iR\|\dot p\|_{\mathcal P}\|\dot q\|_{\mathcal P},\qquad
 \|D_pD_uf_i[\dot p,\dot u]\|_{H^{8192}}
       \le E_i\|\dot p\|_{\mathcal P}\|\dot u\|_{\mathscr H}.
 \tag{P.13}
$$

下面列出该较宽常数的实际推导，以免从有限角光滑性无偿推出统一常数。
对 $2\le s\le8196$，Fourier 卷积给
$$
 \|z^n\|_{H^s}\le
   n^s(2\|z\|_{H^1})^{n-1}\|z\|_{H^s}.
 \tag{P.14}
$$
把 $J^{-1},D^{1/2}$ 的完整级数及 M.13 的有界 mean 分母展开；
低 norm 小于 $2^{-24}$，级数半径可取 $1/32$。
使用 $\sum n^s x^n\le s!x/(1-x)^{s+1}$ 及
$s!\le2^{14s}$，得到 $d,v-1$、其所需两次实参数变分的
$C^{s-2}$ 费用不超过 $2^{32(s+8)}$ 乘相应局部状态 norm 或其乘积。
mean 根在第二变分中用 M 的完整有界分母；它不丢掉独立 mean 行。
从 $H^{s}$ 到 $C^{s-2}$ 的一维 Fourier Cauchy 费用小于4。
具体取 $k=8192$：由8196输入取得 $d,v-1$ 及系数变分的
$C^{8194}$ 界。零阶流的 $C^k$ Lipschitz 需要 $a_\theta$，
一次 $u$ 变分需要 $a_u,a_\theta$，二次需要
$a_{uu},a_{u\theta},a_{\theta\theta}$；最后一项乘两条一次变分。
因此最大角导确为 $k+2=8194$。$p$ 变化的参考平移也只增加同样的
一、二次角导。没有以 $C^{8192}$ 系数直接支付二次 ODE 变分。

对一个实圆周 ODE，将真实径向标量平移移出后，
在 $C^k$ 位移球 $\|g\|_{C^k}<1/8$ 中使用
$$
 \partial^k(a\circ(\mathrm{id}+g))
  =\sum_{\ell=1}^k
     (a^{(\ell)}\circ(\mathrm{id}+g))
       B_{k,\ell}(1+g',g'',\ldots).
$$
由 Faà di Bruno 的完整分拆数，$a$ 及其一阶变分的 composition
和 Lipschitz 系数均可取
$(k+2)!2^{4k+16}\le2^{18k+50}$，$k\le8192$。
把两支 return 写成“正支、反向负支”的一个有序实 ODE，
只使用这个一次 composition 账，不先乘两个独立逆图的粗界。
其 Picard Lipschitz 常数小于 $1/8$，因为全部显示高阶系数费乘
$R_*$ 仍小于 $2^{-1000000}$。
一次变分解同一线性积分方程；二次变分的完整乘积另用
$\|fg\|_{C^k}\le2^k\|f\|_{C^k}\|g\|_{C^k}$。
故一次费用被 $2^{51k+2048}$ 覆盖，二次费用被其平方覆盖。

这里的真实径向积分使用旧 stronger K.13--K.15 的
$\int(1+\sqrt Q)<32(j+4)$，外行使用 O.4--O.7 的
$\int_{I_o}(1+\sqrt Q)<2^9$；没有以短胞长度代外行。
即使以原六邻胞读取四态，原 profile 的相邻比较
$N_j\le2^{132}C_j^\#$ 也在上述2048 bits中支付。
从 $C^k$ 回 $H^k$ 的费用至多 $2^{k/2}\sqrt{k+1}$，同样已包括；
$51\cdot8192+2048<524288$。

$p$ 微分另由 (P.3)--(P.4) 和原局部平方根差式给
$$
 \int_{I_i}|D_p\sqrt Q[\dot p]|\,dt
       \le2^{10}\kappa_i\|\dot p\|_{\mathcal P}.
 \tag{P.15}
$$
以准确变化的径向旋转为参考时，它只造成角系数的一次实导数。
在 (P.13) 的8196输入与8192输出之间已有余量支付它。
径向 $G_i$ 的第二次 weighted 参数导数从同一半径4的原真实复逆盘取得，
这是纯有限维径向参数的 Cauchy 费；它与一次参数导数一起留在上述2048 bits内。
这是固定真实 $u_\perp$ 的 metric 微分；未用角解析 Cauchy，
也没有把 M.33 的 $2q\Psi\,\partial_q\Phi$ 删除。

最后，O.22--O.23 已给全层而非截断预算
$$
 \sup_jj(j+4)C_j^\#\delta_j^{-3/2}<2^{201},\quad
 \kappa_i^2>2^{-55}\delta_j^{3/2}/j,\quad
 \kappa_o^{-2}<2^{263}.
$$
因此
$$
 B_*:=\sup_{i\in\mathcal I_+}\frac{E_i}{(\gamma_i^{\rm D})^2}
       <2^{524600}.
 \tag{P.16}
$$
内部指数为 $524288+24+55+201=524568$，外行是
$524288+24+263=524575$。这保留原两次规范切换和完整浅前缀。

## 4. 一个完整的解析 a-posteriori 步

本节在标准 $2\pi$ 圆上证明所需有限光滑 KAM 的解析子步骤。
固定 $0<\gamma\le1$ 及
$|e^{in\omega}-1|\ge\gamma/|n|$。
设实解析 lift $f$ 在宽 $2r$ 上满足 $|f''|\le1$，
$0<r\le1/64$。当前实解析 $h=\mathrm{id}+v$ 在宽 $r$ 上满足
$|h'-1|\le1/8$，当前实常数为 $\tau$。记
$$
 {\cal E}=f\circ h+\tau-h\circ T_\omega,\quad
 a=h'\circ T_\omega,\quad \epsilon=\|{\cal E}\|_r .
$$
在每个 Newton 子步中只需保持 $|h'-1|<1/4$。于是 $|a^{-1}|<4/3$，
而实平均 $\langle a^{-1}\rangle>4/5$。

令
$$
 \delta\tau=-\frac{\langle{\cal E}/a\rangle}
                        {\langle1/a\rangle},\qquad
 w\circ T_\omega-w=\frac{{\cal E}+\delta\tau}{a},
 \quad \langle w\rangle=0,\qquad
 \delta h=h'w .
 \tag{P.17}
$$
平均行先准确消去，全非零 Fourier 行随后除以
$e^{in\omega}-1$。完整 Fourier 和
$\sum_{n\ne0}|n|e^{-\sigma|n|}\le2\sigma^{-2}$、
$\sum_{n\ne0}n^2e^{-\sigma|n|}\le8\sigma^{-3}$
给
$$
 |\delta\tau|\le4\epsilon,\quad
 \|w\|_{r-\sigma}\le64\gamma^{-1}\sigma^{-2}\epsilon,\quad
 \|w'\|_{r-\sigma}\le256\gamma^{-1}\sigma^{-3}\epsilon,
$$
$$
 \|\delta h\|_{r-\sigma}\le128\gamma^{-1}\sigma^{-2}\epsilon,\qquad
 \|\delta h'\|_{r-2\sigma}\le2^{11}\gamma^{-1}\sigma^{-3}\epsilon .
 \tag{P.18}
$$
这里 $\delta h'$ 中的 $h''w$ 使用 $h'-1$ 的 Cauchy 导数，
没有把这一项删掉。

准确 automatic reducibility 是
$f'(h)h'=a+\mathcal E'$。因此新误差等于
$\mathcal E'w$ 加 $f$ 的完整二阶 Taylor 余项。对 $0<\sigma<r/8$，
在宽 $r-3\sigma$ 上
$$
 \epsilon_{\rm new}\le2^{20}\gamma^{-2}\sigma^{-6}\epsilon^2 .
 \tag{P.19}
$$
实解析且导数接近1保证
$|\operatorname{Im}h(x+iy)|\le(5/4)|y|$。
同样估计每个 $h+t\delta h$，所以 Taylor 路径始终在 $f$ 的宽 $2r$
中；不以实方向位移的绝对大小来错误缩短角带。

固定初始宽 $r_0$，取
$\sigma_\nu=r_0\,2^{-\nu-5}$，每次消费 $3\sigma_\nu$。
总消费 $3r_0/16<r_0/2$。设
$$
 A=2^{50}\gamma^{-2}r_0^{-6},\qquad
 z_\nu=A\,2^{6\nu+6}\epsilon_\nu .
$$
(P.19) 准确推出 $z_{\nu+1}\le z_\nu^2$。
若
$$
 \epsilon_0\le2^{-80}\gamma^2r_0^6,                       \tag{P.20}
$$
则 $z_0\le2^{-24}$，全部子步均合法且收敛。
(P.18) 求和后，在宽 $r_0/2$ 上
$$
 \|\Delta h\|\le2^{18}\gamma^{-1}r_0^{-2}\epsilon_0,\quad
 \|\Delta h'\|\le2^{27}\gamma^{-1}r_0^{-3}\epsilon_0,\quad
 |\Delta\tau|\le8\epsilon_0 .
 \tag{P.21}
$$
这些和使 $|h'-1|$ 始终小于 $1/4$。所得共轭的误差准确为0，
并非只作一次截断近似。

## 5. 完整 dyadic 极限：四阶损失的来源

**有限光滑引理。** 若整数 $16\le s\le8192$，$u$ 为实 $H^s$ 周期函数，
$$
 \varepsilon=\|u\|_{H^s}\le2^{-524288}\gamma^2 ,
 \tag{P.22}
$$
则唯一实反项 $\tau(u)$ 使
$$
 (x+\omega+u(x)+\tau(u))\circ h=h\circ T_\omega
 \tag{P.23}
$$
有归一 $\langle h-\mathrm{id}\rangle=0$ 的实
$C^{s-4}$ degree-one 微分同胚解，且
$$
 \|h-\mathrm{id}\|_{C^{s-4}}
       \le2^{262144}\gamma^{-1}\varepsilon,\quad
 \|h-\mathrm{id}\|_{C^1}\le2^{64}\gamma^{-1}\varepsilon,\quad
 \|h'-1\|_\infty<1/8 .
 \tag{P.24}
$$

证明不引用一个未付损失的 finite-smooth KAM 定理。
令 $N_n=2^n$、$u_n=P_{|m|\le N_n}u$。
对 $u_0$，从 $h=\mathrm{id},\tau=0,r_0=1/64$ 使用第4节；
其初误差小于 $2\varepsilon$，(P.20) 有充分余量。
得到 $h_0$ 在宽 $w_0=1/128$ 上的准确共轭。

归纳设 $h_{n-1}$ 对 $u_{n-1}$ 已准确共轭，宽
$w_{n-1}=1/(128N_{n-1})$，复导数离1小于 $1/8$。
对新 $u_n$，旧 $h_{n-1}$ 的初误差恰是
$(u_n-u_{n-1})\circ h_{n-1}$。由 Fourier Cauchy--Schwarz 及
$|\operatorname{Im}h_{n-1}|\le(9/8)w_{n-1}$，
$$
 \epsilon_n\le4\varepsilon N_{n-1}^{1/2-s}.                \tag{P.25}
$$
新 $f_n=x+\omega+u_n$ 在宽 $2w_{n-1}$ 上满足
$|f_n''|<4\varepsilon<1$：最大指数为
$N_n\,2w_{n-1}=1/32$。
(P.22)、$s\ge16$ 给
$\epsilon_n\le2^{-80}\gamma^2w_{n-1}^6$。
完整解析子迭代因而在宽
$w_n=w_{n-1}/2$ 得到对 $u_n$ 的准确共轭。
(P.21) 的复一阶导增量之和由
$2^{27}\gamma^{-1}\sum_n w_{n-1}^{-3}\epsilon_n$ 控制，
(P.22)、(P.25) 使此和小于 $1/64$；所以归纳使用的复导数门确实保持。

对任意 $0\le k\le s-4$，(P.21) 和实轴 Cauchy 估计给
$$
 \|h_n-h_{n-1}\|_{C^k}
 \le2^{20+k}k!\gamma^{-1}w_{n-1}^{-k-2}
                     \varepsilon N_{n-1}^{1/2-s}
 \le2^{37+22k}\gamma^{-1}\varepsilon
                     N_{n-1}^{k+5/2-s}.                 \tag{P.26}
$$
用了 $k!\le2^{13k}$；$k\le8188$。
最后指数至多 $-3/2$，故每个显示导数的整个 dyadic 和收敛。
连同初步、各导数之和及最后 mean 归一化的因子2，
$37+22\cdot8188+16<262144$。
单独取 $k\le1$ 给 (P.24) 的较紧 $2^{64}$。
所以 $h_n\to h$ 于 $C^{s-4}$，$\tau_n$ 亦收敛，
$u_n\to u$ 于 $C^1$，极限确实满足 (P.23)。
此处不存在残留有限截断，亦没有把角解析性赋给 $h$。

唯一性如下。若 $\tau_2>\tau_1$ 都给同一 irrational rotation，
用第一共轭搬运第二个 lift，所得 map 严格大于 $x+\omega$，
并因紧圆周有严格正的统一 gap。其每步增量都大于 $\omega$ 加此 gap，
故 lift rotation number 严格大于 $\omega$，矛盾。
同一反项的两个共轭相差一个与 irrational rotation 交换的圆周
homeomorphism；它只能为旋转。归一 mean 消除该自由度。

这也证明反项的真实 $C^0$ Lipschitz 界
$$
 |\tau(u)-\tau(v)|\le\|u-v\|_{C^0}                         \tag{P.27}
$$
（只对本引理内两个输入）。若超出此界，两相应 lifts 处处严格有序，
用上一段同一论证即矛盾。

## 6. 反项微分：同一个实物理变量中的正权平均

在 (P.22) 的严格小球内，$\tau$ 是 $H^s\to\mathbb R$ 的
$C^1$ map，准确微分为
$$
 D\tau(u)[\dot u]=
 -\frac{\left\langle
       \dot u(h(x))/h'(x+\omega)\right\rangle}
       {\left\langle1/h'(x+\omega)\right\rangle}.
 \tag{P.28}
$$
实分母是正的；因此
$|D\tau(u)[\dot u]|\le\|\dot u\|_{C^0}$。
这不是把 invariant mean 当成原 Fourier mean。

为证明微分而不是形式写下线性化，设 $v$ 是小增量，
$\Delta\tau=\tau(u+v)-\tau(u)$。
由 (P.27)，$|\Delta\tau|\le\|v\|_\infty$。
用当前准确 $h$ 共轭新的 map，Taylor 展开给
$$
 g(x)=x+\omega+a(x)+b(x)\Delta\tau+r_2(x),\quad
 b=1/h'\circ T_\omega,\quad a=b(v\circ h),\quad
 \|r_2\|_\infty\le4\|v\|_\infty^2 .                       \tag{P.29}
$$
(P.24) 对前六个导数的较紧部分和保证这个 Taylor 常数；
本处只使用实 $h^{-1}$。取 $g$ 的任一 invariant probability $\nu_g$。
准确 rotation identity 为
$\int(g-x-\omega)\,d\nu_g=0$，可由迭代位移除以步数得到。

对于 $z\in H^4$，全 Fourier 方程
$w\circ T_\omega-w=z-\langle z\rangle$ 给
$\|w'\|_\infty\le4\gamma^{-1}\|z\|_{H^4}$。
利用 $\nu_g$ 的不变性，
$$
 \left|\int z\,d\nu_g-\langle z\rangle\right|
 \le4\gamma^{-1}\|z\|_{H^4}\|g-T_\omega\|_\infty .
$$
分别取 $z=a,b$，保持 $a,b$ 的相关性并使用
$\langle b\rangle>1/2$，得到
$$
 |\Delta\tau-D\tau(u)[v]|
 \le2^{64}\gamma^{-1}\|v\|_{H^6}\|v\|_{C^0}.             \tag{P.30}
$$
这里 composition 的 $H^4$ 费用只用 $h$ 的前六阶导数，
(P.22) 使它们一致小。因 $s\ge16$，这是一个真正 Fréchet 余项。

归一化共轭对 $H^s$ 输入连续于 $C^1$：使用 (P.24) 的统一
$C^{s-4}$ 有界性提取子列，极限共轭的唯一性识别每个子列。
(P.28) 遂在 $H^s$ 的算子 norm 中连续。
最后由同一式及 (P.24) 的 $C^1$ 门，
$$
 |D\tau(u)[v]+\langle v\rangle|
 \le2^{72}\gamma^{-1}\|u\|_{H^s}\|v\|_{C^1}.
 \tag{P.31}
$$
下文的第一参数二次小量将用此实际正权公式，而非未付的
finite-smooth 二阶 KAM 定理。

## 7. 所有实际第一参数的一次无限选择

对 (P.11) 每一行，令 $\tau_i$ 为第5节在固定真实
$(\omega_i,\gamma_i^{\rm D})$ 上的反项 functional，定义
$$
 {\mathfrak T}_i(p,u)=\tau_i(f_i(p,u,\cdot)).
 \tag{P.32}
$$
由 (P.6)、(P.13)、(P.16)，
$$
 \frac{\|f_i\|_{H^{8192}}}{(\gamma_i^{\rm D})^2}
 \le B_*R<2^{-1572552}<2^{-524288}.
$$
所以全部深层及外行都在第5节的同一个合法域内。

准确主相位方程是 $p_i=\mathfrak T_i(p,u)$，不是把 $\tau_i$
添加成一个自由 metric 以外的参数。由 (P.27)--(P.28)，
$$
 \|\mathfrak T(p,u)\|_{\mathcal P}\le B_*R,\qquad
 \|D_p\mathfrak T\|_{\mathcal P\to\mathcal P}\le B_*R<1/2 .
 \tag{P.33}
$$
故闭盘 $\|p\|_{\mathcal P}\le1/4$ 上存在唯一无限固定点 $p^*(u)$。
这不是先计有限窗口再省略深层极限；相同完备 weighted
$\ell^\infty$ 空间的 Picard 级数直接收敛。

(P.30)、(P.13) 给这个无限 map 的统一 Fréchet 余项。
例如 $u$ 方向反项余项除以 $\kappa_i$ 后受
$$
 2^{65}\frac{E_i^2}{\gamma_i^{\rm D}\kappa_i}
                       \|\dot u\|_{\mathscr H}^2
 \le 2^{65}B_*^2\|\dot u\|_{\mathscr H}^2
$$
控制；$p$ 和 mixed 余项由 (P.13) 的后两项以同样顺序支付。
这些是整 Banach 方向，不是逐坐标导数的 supremum。
用该统一二次余项和差商得到导数的算子 norm 连续性，
所以 $p^*$ 是真实 $C^1$ Banach map，且
$$
 Dp^*=(I-D_p\mathfrak T)^{-1}D_u\mathfrak T,\qquad
                  \|(I-D_p\mathfrak T)^{-1}\|<2 .
 \tag{P.34}
$$
所有交叉参数行都保留。没有以径向支集相离替代这个真实非径向平均方程。

于是
$$
 {\cal R}_{i,p^*,u}\circ h_i=h_i\circ T_{\omega_i},
 \quad h_i\in C^{8188},\quad
 \|h_i-\mathrm{id}\|_{C^{8188}}
       \le2^{262144}(\gamma_i^{\rm D})^{-1}E_iR .
 \tag{P.35}
$$
物理第一列是 $\gamma_{1,i}^*(u)=\gamma_{1,i}(p^*(u))$，
第二列 $\gamma_{2,i}=\bar\gamma_{2,i}+\mathfrak q_i$ 此时仍是给定的完整变量。
(P.3) 保证第一列留在原真实 $2^{-16}$ 盒内；
原 $\omega_i$ 和 $\beta_i^0$ 目标数没有重新选择。

## 8. 零点的一阶抵消与真正逐层二次尺度

在 $u_\perp=0$ 时，$\varkappa=0$，每个 $p$ 的误差 $f_i(p,0)=0$。
在这个径向点，对任意非mean高度方向，
$$
 \dot d=E(\dot V-\dot P),\qquad
 \dot v=-E(\dot K_\perp+\dot U),\qquad \dot\varkappa=0 .
 \tag{P.36}
$$
其角平均都为0。线性化真实 ODE 只沿径向旋转搬运这些函数，
所以 $\langle D_uf_i(p,0)[\dot u]\rangle=0$。
(P.28) 在 $h=\mathrm{id}$ 时是负普通平均，因而
$D_u\mathfrak T(p,0)=0$。这个消去来自全 mean 小根，
不是预先删去原 PDE 的 mean 方程。

用 (P.13) 的二次 $u$ 门及 (P.31)，对当前 $R$ 有
$$
 |D_u\mathfrak T_i[\dot u]|
 \le2^{80}(\gamma_i^{\rm D})^{-1}E_i^2R
                                      \|\dot u\|_{\mathscr H}.
 \tag{P.37}
$$
因此先取完整 weighted norm，再代回逐行方程，可得
$$
 \|Dp^*[\dot u]\|_{\mathcal P}
       \le2^{1049300}R\|\dot u\|_{\mathscr H},
$$
$$
 |Dp_i^*[\dot u]|
       \le2^{524681}E_iR\|\dot u\|_{\mathscr H}.
 \tag{P.38}
$$
第一式使用
$\kappa_i=4096\gamma_i^{\rm D}$、
$E_i/(\gamma_i^{\rm D})^2\le B_*$：
$2^{80}\sup E_i^2/(\gamma_i^{\rm D}\kappa_i)
 \le2^{1049268}$，再乘 (P.34) 的2。
逐行第二项是 $E_iR\|Dp^*\|_{\mathcal P}$；
$R_*$ 使它小于 $E_iR$，而首项
$2^{80}E_iR(E_i/\gamma_i^{\rm D})\le2^{524680}E_iR$。
这说明逐层费用不是用一个共同最大 $E_i$ 重命名。

回到真实 metric 单位，
$|D\gamma_{1,i}^*|\le2^{-18}\kappa_i^{-1}|Dp_i^*|$。
内部 $\kappa_i^{-1}<2^{28}J_j\delta_j^{-1}$、外部
$\kappa_o^{-1}<2^{132}$，从而
$$
 |D\gamma_{1,i}^*[\dot u]|
 \le2^{1050000}J_j^2\delta_j^{-1}C_j^\#\,
                     R\|\dot u\|_{\mathscr H}\quad(i\ne o),
$$
$$
 |D\gamma_{1,o}^*[\dot u]|
 \le2^{1050000}R\|\dot u\|_{\mathscr H}.
 \tag{P.39}
$$
沿 $\lambda u_\perp$ 积分，分别以 $R^2$ 替换
$R\|\dot u\|$ 即给 $\gamma_1^*-\gamma_1^{\rm rad}$ 的二次值界。
(P.39) 是新物理有限角域中的真 profile；它不冒称旧
$\ell^1_{224}$ 标签导数已经在任意近邻背景保持。

## 9. 角平移、两 mean 与真实源列的身份

固定 $\Omega,\mathfrak q$ 后，(P.5)、(P.7) 与所有真实 ODE
都与同一个角平移交换。principal maps 按该平移共轭；
反项的唯一性与无限固定点的唯一性给
$$
 \gamma_1^*(u_\perp(\,\cdot\,,\theta+\vartheta))
                         =\gamma_1^*(u_\perp),\qquad
 D_u\gamma_1^*(0)=0 .                                    \tag{P.40}
$$
一个最终非mean高度的整个角轨道因而有同一第一 metric 参数。
这不选择第二相位，也不宣称完整解族已存在。

真实物理共轭是 $K_i(\eta)=h_i(4\eta)/4$。
完整两迹仍按
$$
 H^{\rm new}=H\circ K_i,\qquad
 \pi^{\rm new}=K_i'(\pi\circ K_i),\qquad
 \int\pi^{\rm new}H^{\rm new}=\int\pi H                  \tag{P.41}
$$
搬运。$\pi$ 是带 weak 径向势的 total 通量；通量 mean 保持，
高度 mean 是准确 $\langle H\circ K_i\rangle$。
没有用任意粗源经过 mixed root 图的假有界性。
正区双端图、非对角 cross、外 $C_R/B_0$、原 $\nu$、
ordinary/weak/原子源仍按其真实单位独立保留。

当方向同时改变 $u_\perp$ 和真实第一 metric，置
$\psi=\sum\psi_{1,i}D\gamma_{1,i}^*$，若第二参数也变动则还必须加
$\sum\psi_{2,i}D\mathfrak q_i$，形状方向另加准确的 $\delta\Xi$。
总高度变化包含 (P.8) 的完整导数。M.33--M.37 给非解背景上的准确式
$$
 \dot{\mathfrak r}=Lh-e_\psi-\psi\mathfrak r,\qquad
 \dot N=c_{\rm phys}(Lh-e_\psi)+\psi N,\qquad
 c_{\rm phys}=\frac{\mu_jp_*^2}{12r^{10}} .                \tag{P.42}
$$
拆去真实参考 lift $(h_\psi)_t=a_{\rm ph}w\psi$ 后，仍是
$\dot N=c_{\rm phys}(L\widetilde h-e_{\psi,\rm rem})+\psi N$。
这里 $+\psi N$ 在非解背景不能消失，lift 的两个真实端点输出也不能删。
本篇 (P.39) 给它所需第一参数的实际费用；其返回某个完整 source norm
及第二参数补偿另须按相应源定理收费。
在本篇 holonomy-one 子域，M.16 还给真实 weighted residual mean 为0；
这不是将 residual 本身或它的 ordinary Fourier mean 设为0。

最后说明与旧已知成员的认同。这一入口直接来自原完整
analytic 局部解图，不来自前篇 R 仅输出到 $Y_{64}$ 的逆。
[controlled 全图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
C.22 对任意绝对宽 $\tau\ge0$ 给
$\Phi_j:B_{\mathcal A_{\tau+h_j}}\to\mathcal A_\tau$，
C.23 给同宽的完整四态。
C.24 及 [强深全标签](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md)
U.2 的准确规范为
$$
 X_{m,j}=(-1)^j\zeta_j^{-1}e^{|m|\tau_j}V_{m,j},\qquad
 \tau_j-\tau_{j-1}=h_j>0,\qquad\tau_{128}=5177/400 .
$$
先使用原 $\sum_m e^{224|m|}\sup_j|X_{m,j}|$ norm，逐胞得到
$$
 \sum_m e^{(\tau_j+224)|m|}|V_{m,j}|
 \le\zeta_j\|X\|_{\mathcal X_{224}} .
$$
于是 C.22--C.23 取 $\tau=\tau_{j-1}+224$，整胞四态保持至少
$\tau_{128}+224>236$ 的绝对角宽。$h_j\to0$ 是每胞支付的宽损，
不是该成员只剩 $h_j$ 条带；这里没有把标签224本身直接当作
未知物理状态的角宽。嵌 (P.5) 只需这个逐胞统一的实 $t$
Wiener 界，不交换 $\sum\sup$ 和 $\sup\sum$。
新增 connector 用新对象 S.25 的原余宽 $2683/800>3$。

现在用
$\sup_m\langle m\rangle^{8196}e^{-3|m|}<2^{131072}$，
连同原六邻胞、$C_j^\#\le2^{128}C_j$ 和真实 radial norm 比，
得到 (P.5) 的安全界 $R\le2^{132000}\mathcal X$；
connector 的 $2^{-447}$ 原门也落在这里较宽的 $2^{-440}$ norm 内。
因此当前 $\mathcal X\le2^{-8388608}$ 的已知 analytic 成员进入 (P.6)。
在该成员自己的真实 $u_\perp$、真实 $\mathfrak q$ 和相同 $\lambda$ 上，
(P.7)--(P.8) 与原 mean/高度图由唯一性一致，原第一参数也满足
(P.32)。所以新第一参数等于原第一参数。

这个认同是把**已经给定的实际成员**代入同一个新图。
它没有把旧标签图的 $u_\perp(a,\Gamma)$ 在参数方向冻结；
若再以原 $a$ 作坐标，必须使用完整链式法则。
也没有从 (P.35) 推出原 analytic224 输出或全部 Airy 余核的解析 lag。

## 10. 本条的完成范围与下一具体门

本条已在保持原 $\zeta_{131}$、全部真实根/形状/两 bump/尺度的前提下，
关闭新有限角域的第一 principal 参数问题：全 Fourier、
全无限层、新外行、正确 mean 小根与真实 metric 参数导数均已支付。
有限光滑共轭来自 (P.17)--(P.26) 的完整收敛级数，未引用未付的
“四阶损失”黑箱。

尚须在同一个新域上定义并控制完整密度首相位 $\beta$，包括两端 root
有限部、真实径向接缝和固定端角；旧 analytic J.10--J.17 的二次参数
消去不能仅凭 (P.35) 自动转授。还须有变化背景上同一 source/状态域的
全网络 inverse 或相应 tame 逆，才能将本条与 M 的 mean/height、
R 的固定背景2050阶逆损失及真实外帽/ν 联立成非线性存在性。
特别，R 目前只保证 $Y_s$、$s\le64$；一般该类修正不自动属于
(P.5) 的 $H^{8196}$ 输入域。将它送回本域必须实际支付新的
smoothing 或更高阶 tame 逆及其全迭代费用。
本条不把这些尚欠门改称 Picard 收缩，也不以有限角光滑性冒充旧标签空间。
