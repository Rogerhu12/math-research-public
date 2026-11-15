# R119 续篇：完整闭网络的 1024 阶角 Sobolev 窗与物理帽反馈

2026-11-15，visible-exact / tail_connector。

**状态：解析证明；固定实际背景的有限角 Sobolev 窗及物理帽反馈。** 本篇固定已经选择的同一
simple-root 对象、同一公共五盒参数点和真实
$\Gamma^*(a,\Omega)$。起点是
[新外 mixed 闭网络](R119-supplement-new-outer-complete-mixed-weighted-Schur-and-closed-nonmean-inverse.md)
（记 Y）、
[闭 mean 商](R119-supplement-new-closed-mean-compatibility-gauge-and-complete-fixed-CR-inverse.md)
（记 Z）以及
[完整物理帽—尾 Schur](R119-supplement-complete-physical-cap-tail-Sobolev-Schur-with-all-mean-charges.md)
（记 L）。

这里新增的是有限角 Sobolev 窗。它不是原 $\ell^1_{224}$ 标签逆。
径向 $C^4$ 形状没有被要求具有第五阶统一导数；
全篇高导数只作用于角变量。所有估计作用实际完整算子，包含低频、
两条 mean、非径向混频、帽回馈和真正 source 列。

置物理 Fourier 权
$\langle m\rangle=(1+m^2)^{1/2}$、$m\in4\mathbb Z$，
$\Lambda_\phi=\langle D_\phi\rangle$，并令
$$
 q_*=1024,\qquad g=4/3,\qquad
 \mathcal X\le2^{-8388608},\quad
 \epsilon_L=e^{-7L/4}<2^{-33554432}.
 \tag{U.1}
$$
本文使用的新投影和谱权是
$$
 T_j^\sharp=\max(2^{1048704}J^2\delta_j^{-9},\,2^{1056768}),
 \qquad
 v_j^\sharp=2^{-600000}J^{-4165}\delta_j^{1073/32},
 \quad J=j+5.
 \tag{U.2}
$$
全部根波均用 Y 的同一个 unitary 表示 $H_a$。
这些是证明用的截断和源/状态权，未改变任何物理切口、
profile、目标相位或五盒参数。

主结论为：$0\le s\le1024$ 时，对下文准确有序的 remaining 源 $k$，
指定物理平端高度 $\lambda$，有唯一的完整增广解
$$
 (I-S_{{\rm rem},a}^\sharp)x+\sigma_\circ\tau=k,
 \qquad \ell x=\lambda ,
$$
$$
 \boxed{\quad
 \|v^\sharp x\|_{H^s}
 <2\|(v^\sharp)^{-1}k\|_{H^s}
       +2^{-595199}|\lambda|,\qquad
 \tau=\frac{\mathcal L_a k}{\mathcal L_a\sigma_\circ}.
 \quad}
 \tag{U.3}
$$
$\mathcal L_a$、$\sigma_\circ$ 和 $\ell$ 是原物理通量/高度单位。
真正可解仍恰要求 $\mathcal L_a k=0$。high 与 deep-low 的完整
Poisson、源窗和反向重建在第6节给出。第8节进一步证明同一物理帽
反馈在这些有限 Sobolev 窗仍收缩。

## 1. 本篇实际调用的解析输入

负片的完整输入是：

* [负散射完整 word](R119-supplement-complete-negative-scattering-and-network-word-in-slope-units.md)
  W.7--W.26、W.33--W.49；
* [完整根 Volterra](R119-supplement-root-high-output-Volterra-without-low-frequency-condition-number.md)、
  [根首相位](R119-supplement-complete-root-first-phase-in-slope-units.md)
  F.3--F.15；
* [根图二阶余项](R119-supplement-complete-root-graph-two-order-slope-budget.md)
  G.5--G.20；
* [strict 全输入高输出](R119-supplement-complete-strict-high-output-in-root-slope-units.md)
  S.12--S.27；
* [固定 scalar 正常形](R119-supplement-fixed-scalar-normal-form-and-slope-unit-high-network.md)
  Z.9--Z.29；
* 新外 F.1--F.39 和 J 的同一完整两根、principal、首相位接线。

原 $|s|\le4$ 等结论不直接改写成 $s=1024$。下面重新使用其完整
核与系数公式。固定角条带可统一缩到
$$
                         \sigma_0=2^{-20}.
 \tag{U.4}
$$
这严格小于 root 的 $1/128$、strict/graph 及 KAM word 的
$1/1024$ 和新正片 N.28 的 $1/256$。这些角域属于原实际
固定片/端图，不在径向接缝两侧假设解析延拓。
每个真实 flow 是一个实径向平移加已付解析小量；
W.15 的 graph 路径域与路径次数无关。
KAM/同调解的解析余宽由原 N.8、N.15--N.16 和 scalar
Z.14--Z.24 提供，不能仅由 26 阶导数的存在推出 (U.4)。

以下始终保留真正复合角图，不把
$C_F-C_{F_\circ}$ 当作同阶小算子。需要小的是其完整
transport commutator，或者原同阶 generator 差中已经带
$D_\phi^{-1}$ 的组合。

## 2. 一个明确的有限角费用

记
$$
                           B_*=2^{65536}.
 \tag{U.5}
$$
下面三种操作，各使用至多一份 $B_*$。

第一，若完整 Fourier 核已给 lag 包络
$a_\ell e^{-2^{-18}|\ell|}$，乘
$\langle m\rangle^s/\langle n\rangle^s$，
$|s|\le1032$，只增加
$(1+4|m-n|)^{|s|}$。附加至多24次非驻相积分时，最多要付
$p\le1088$ 的同类 moment。直接用
$$
 x^p e^{-c x/2}\le p!(2/c)^p,\qquad
 \sum_{\ell\in\mathbb Z}e^{-c|\ell|/2}<1+4/c,
 \quad c=2^{-18},
$$
以及 $p!<2^{11p}$，得到相应 moment 小于 $2^{40000}$。
两条 wave、两个 Fourier 锥、半阶平衡和有限二项式计数
均可放在余下的25536 bits中。这个结论先求完整行列和，
不从单列 supremum 推断算子 norm。

第二，设 $F(\phi)=\phi+\alpha+\eta(\phi)$，
$\alpha$ 为真实径向平移，$|\eta|$ 及其复域导数具有原小量
$\varepsilon$。去掉 $\alpha$ 后，用真实路径
$F_t=\mathrm{id}+t\eta$ 及
$V_t=\eta\circ F_t^{-1}$。其 Jacobian 和逆在 $[1/2,2]$。
对整数偶数 $q\le1030$，令
$W_q=(1-\partial_\phi^2)^{q/2}$。准确展开
$$
 [W_q,V_t\partial_\phi]W_q^{-1},\qquad
 [W_q,M_{\partial_\phi V_t}]W_q^{-1}
 \tag{U.6}
$$
后，最高未抵消导数为 $q+1$；每一项至少含一个
$\eta$ 的导数。各 $\partial_\phi^rW_q^{-1}$ 在所需
$r\le q$ 的 Fourier norm不超过1。Cauchy、
二项式系数和有限逆函数费用给 (U.6) 的积分 norm
$<B_*\varepsilon$。因此真实 density transport 及逆的
$H^q$ norm至多 $\exp(B_*\varepsilon)$；与原 $L^2$ 表示
共轭的差也至多 $2B_*\varepsilon$，只要
$B_*\varepsilon<1/4$。负阶用真实 density 对偶，
非整数阶用 Hilbert 插值。半阶波平衡只移动这一有限指数窗。
这里没有估计裸 $C_F-I$。

第三，同号压缩的 cross/polar 项可继续使用原 signed-Green
的双侧恒等式。跨锥相位满足
$|\partial_\phi(nF-m\phi)|\ge(|m|+|n|)/2$。
作至多 $q+24$ 次原非驻相积分，导数只作用原解析角系数，
给 $H^q\to H^{q+20}$ 的真实 cross 核。
Cauchy的阶乘、积分系数阶乘和
$\sigma_0^{-(q+24)}$ 的总 bits小于 $2^{16}$；
故它仍只需一份 $B_*$ 乘原 $2^{4096}\varepsilon$。
两个 polar defect 的绝对可和
$(I+F)^{-1/2}$ 级数在同一 $H^q$ norm中求和；
第一项支付20阶，余项支付同阶小 norm。
mean 与非mean的有限行列按同一解析系数处理。
因此没有把旧20阶门本身免费当作1024阶门。

这些规则也适用于原普通 multiplier、primitive、
fixed-root Airy 矩阵和一次真实 source 积分：
radial Fourier multiplier与 $W_q$ 准确交换；
只有完整 lag、真实 angle transport 或非径向系数需要收费。
径向大相位不是 $B_*$ 倍的指数增长率。

## 3. 同阶完整传播：先付全部低频

令 $n_i=4(N_j^c)^\#\mathcal X$、
$\lambda_i=2^{32}\sqrt J\,\delta_j^{-9/4}$。
W.8 的三段 $N_j^c$ 原样保留：
$$
 N_j^c\le
 \begin{cases}
 2^{220}\delta_j^{7/4},&129\le j\le4096,\\
 2^{185}\delta_{4096}^{-3/2}\delta_j^{827/256},
                                      &4097\le j\le8192,\\
 2^{185}\delta_{4096}^{-3/2}\delta_{8192}^{-485/4}
                         \delta_j^{31867/256},&j\ge8193.
 \end{cases}
 \tag{U.7}
$$
$(N_{129}^c)^\#=N_{129}^c$，没有虚构 $N_{128}^c$ 端项。
本篇使用更宽的完整预算
$$
 \sum_{j\ge129}2^{262144}J^{128}\delta_j^{-96}(N_j^c)^\#
                                <2^{1100000}.
 \tag{U.8}
$$
这里给出有限前缀的核算。第一段逐项 bits小于
$262144+1792+220+(96-7/4)4100<651000$。
第二段小于
$262144+1792+185+6150+93\cdot8196<1033000$。
第三段第一项小于
$262144+1792+185+6150+(121.25-28)8196<1035000$；
之后的相邻比小于 $2^{-27}$。
有限项数、邻项重编号的权比和两个分量的费用合计小于
$2^{120}$，仍严格低于 (U.8)。
因而乘真实 $\mathcal X$ 后总费 $<2^{-7288608}$。
这一步包含所有浅层，而不是只用深段正幂。

设 $T$ 是一个完整负片的两根 Cauchy 矩阵，
$T_q=W_qTW_q^{-1}$。对 root，用 W.12 的同一个
radial $Y$ 演化和完整角 multiplier 差；
其1024阶增加至多 $B_*$，两个 Airy/$Y$ 转换仍是
同频矩阵。对 strict，原完整
$$
 E_i=2^{300}J^3\delta_j^{-5}n_i,\qquad
 G_i=2^{1024}J^5\delta_j^{-10}
$$
分别增加 $B_*$ 和一个最终因子2：
相对于准确 Fourier 对角的 radial generator 作 Duhamel，
$G_iB_*E_i<1/4$ 由 (U.8) 支付。
graph 用 G.5、G.15 的完整小时间 generator；
principal 恢复用 (U.6)。所有 mean lift 的非constant角系数
也在这些公式内。

可逐项采用下面的宽界：
$$
\begin{array}{c|c}
\text{真实单因素的 }T_q-T\text{ 或相同相对差}&\text{上界}\\ \hline
\text{root，包含 mean 和两 Airy 行}&B_*\,2^{6000}b^4n_i\\
\text{strict 固定标签全演化}&2B_*G_i^2E_i\\
\text{graph 及其 principal 恢复}&B_*\,2^{2048}b^2n_i\\
\text{纯 principal/polar 与首相位}&B_*\,2^{8192}
                       (1+\lambda_i)\epsilon_i^c .
\end{array}
 \tag{U.9}
$$
root 第一行比 W.12--W.13 的
$2^{4500}b^{2/3}n_i$ 更宽；graph 行使用真实图高因子，
不乘没有图高的裸 endpoint 条件数。strict 行只用两个完整
propagator，不再乘第三个 strict 条件数。

整个 word 有不到32个因素。左右完整子乘积分别用
W.26 的 $2^{8192}\lambda_i^{12}$，
而非逐因素重复相乘。代入 $\lambda_i$ 和
$\epsilon_i^c=2^{8192}J^{16}\delta_j^{-16}(N_j^c)^\#\mathcal X$，
(U.9) 的最大 strict 幂为 $\delta^{-79}$，
其它项更小。故完整两方向都满足
$$
 \|T_q-T\|\le e_i,\qquad
 e_i:=2^{262144}J^{128}\delta_j^{-96}(N_j^c)^\#\mathcal X.
 \tag{U.10}
$$
新有限外片使用 F.25 的 $2^{32768}$、
F.13 的实际有限 generator 和 $n=2^{-12}\mathcal X$；
同样推导的费用小于 $2^{262144}\mathcal X$。
没有把新 simple-root 当作旧 quartic。

从 Cauchy 到 scattering 不能粗乘一个大的 $D$ 块。
写 $T=(A,B;C,D)$。真实 anti-$J$ 恒等式给
$\|B^{-1}\|,\|C^{-1}\|,\|DB^{-1}\|\le1$。
若 $\|T_q-T\|\le e<1/16$，则
$$
 \|B_q^{-1}\|\le2,\qquad
 D_qB_q^{-1}-DB^{-1}
 =(E_D-DB^{-1}E_B)B_q^{-1},
$$
所以 $\|D_qB_q^{-1}\|\le1+4e$。
把原 unitary scattering 的真实解 $(a,b)$ 代入新方程，
其 residual 的 norm不超过 $\sqrt2e\|a\|$；
准确 affine scattering 公式 W.43 因而给
$$
                  \|S_{-,q}-S_-\|<8e,\qquad
                  \|S_-^{\pm1}\|_{H^q\to H^q}<2 .
 \tag{U.11}
$$
反向和负阶使用同一完整反向 word。各明确 principal/首相位模型的
径向部分都是同频酉矩阵；非径向 commutator 的完整有限和同样由
(U.8) 支付。因此这些模型的全部子乘积及逆在本篇角窗中 norm
小于2，而不是把原 $L^2$ 酉性直接改写成高阶酉性。
该论证未假定 $T_q$ 仍为普通酉，也未删除 mean。

## 4. 重新支付完整强余项与同表示差

在所有负片，重新使用辅助证明阈值
$$
                         L_i^\flat=2^{131072}\lambda_i .
 \tag{U.12}
$$
它只用于本节估计，不是物理切口。
root 全高 feedback 的最坏系数是
$2^{2217}B_*(b/M)^{2/3}$。
即使在不到 $2^{56}$ 的所有内部缓冲后，(U.12) 仍使它
小于 $2^{-19000}$。strict 的一阶 generator 更小。
因此原两次 Volterra、两次 source 积分及有序跨支分部积分
在此阈值上成立。

一项或两项完整 lag/角操作分别收 $B_*$ 或 $B_*^2$。
root 两次 Volterra最多为
$2^{4098}B_*^2b^{4/3}$；
strict、graph 的强二阶式最多为
$2^{2048}B_*^2\lambda_i^2$ 和
$2^{1024}B_*^2b^2$，随后按原输出插值。
整个 word 高输出及真正反向 word可统一取
$2^{150000}\lambda_i^{4/3}$。
真实远带保留 W.15--W.20 的完整路径/跨锥 kernel：
新增角权由第2节付清后，20阶远带项仍可取
$2^{150000}M^{4/3-20}$。strict 的低到高项仍用
W.22 的 generator 差，不能假设 strict 存在一个有界
complex-shift propagator。将 (U.8) 的真实 $\mathcal X$
与 (U.12) 的 $L^{4/3}$ 相乘，所有这类项仍小于
$2^{-7000000}\lambda_i^{4/3}$。

低输出则必须保留，并用 (U.11)：
其完整强费用至多
$4(2^{131072}\lambda_i)^{4/3}<2^{174765}\lambda_i^{4/3}$。
由原 W.38 的四个准确 block 恒等式和真实反向 word，得到
$$
 \|S_--S_-^{(1)}:H^s\to H^{s+4/3}\|,
 \quad
 \|(S_--S_-^{(1)})^*:H^s\to H^{s+4/3}\|
                    <2^{180000}\lambda_i^{4/3},
 \quad |s|\le1024 .
 \tag{U.13}
$$
这里每个 mean 入列仍由相同完整 Fourier 行列和支付。

正片使用的是另一种确已成立的输入：
[完整 positive 根余项](R119-supplement-positive-full-Airy-remainder-in-root-slope-units.md)
P.20--P.25 在真实 complex shift $|\Im z|<1/1024$
给完整 $(R(z)+I)\Lambda_\phi^{4/3}$ 界；
新 P/N 则给真实 $R_{\rm adj}=R_a^{-*}$，
不把实际非自伴外返回当作 $R_a^*=R_a^{-1}$。
在这些有界 complex-shift 算子族上取 Fourier 元，
其矩阵恰乘 $e^{i(m-n)z}$，第2节真正 lag-Schur
付一份 $B_*$；取伴随所需完整另一侧最多再付一份。
于是所有所需正片强费用可放在
$2^{140000}\lambda_i^{4/3}$，
同阶正/逆费用可取 $B_*$。
新有限正片使用 $\lambda_i=\Lambda_o=2^{2048}$。

scalar 正常形仍沿原 Z.12 的密度协变和 Z.19 的准确
ordered Duhamel。真正大径向平均与 $\Lambda_\phi$ 交换；
非径向 exponent 的同阶积分只增加 $B_*$，
由 (U.8) 支付。二次项仍准确有两个 order-minus-one 因素，
不是把一个低输出强界乘到整个算子上。
首系数、$\beta_i^0$、两个 $\Gamma^*$ 和原参数导数不改变。
包括正负 word、相邻至多8块、两个 $H_a$ 和实际全部 mean，
完整共同 unitary 表示给
$$
 \widehat U_a=U_d+\mathcal R_a,\qquad
 \|\mathcal R_i:H^s\to H^{s+4/3}\|,
 \ \|\mathcal R_i^*:H^s\to H^{s+4/3}\|
                 <2^{262144}\lambda_i^{4/3}.
 \tag{U.14}
$$
账的最大组合为 $180000+65536+2\cdot66+12<262144$。
实际有限正返回只有已付 norm界，未使用其酉 Schur 结论。

同一规则作用原 Q7/V 的完整物理 generator 差和 Y.9--Y.15：
其中 source/target 的一次角导仍保留。
每个比较最多有真实输入角恢复、generator/系数和输出角恢复
三组需要第2节；完整左右演化的 $H^s$ 界已由 (U.9)--(U.11)
而非新的指数 Gronwall 提供。因此旧行的两种一阶差改为
$$
 \|\Delta\widehat U_j:H^{s+1}\to H^s\|,
 \quad\|\Delta\widehat U_j^*:H^{s+1}\to H^s\|
 <2^{196608}\epsilon_j^{\rm old},
$$
$$
 \epsilon_j^{\rm old}
   =2^{35000}J^{40}\delta_j^{-47}\mathcal N_j\mathcal X .
 \tag{U.15}
$$
新有限行的对应界为
$2^{196608+262144}(\mathcal X+\epsilon_L)$，
仍仅支持在真实层129--131及其原相邻列。
这不是说 Schur 后仍有限邻接。

## 5. 新高阈值及恢复被移入 remaining 的频段

(U.2) 的第一项恰为 $2^{1048576}\lambda_j^4$；
其相邻比小于 $2^{10}$。有限平台为
$2^{1048576}\Lambda_o^4=2^{1056768}$。
同一高相位整数门继续给一阶 inverse，
真实 high feedback 的上界是
$$
 2^{262144+12+256+32} (2^{1048576})^{-1/3}
                                    <2^{-87080}.
 \tag{U.16}
$$
这里256 bits支付任何原允许的邻块权比，32 bits支付所有
实际块计数和缓冲。故完整 Neumann、其真正 adjoint 及 source式给
$$
 \|wR_H^\sharp g_H\|_{H^s}<2^{14}\|wg_H\|_{H^{s+1}},
 \qquad
 \|wE_H^\sharp w^{-1}\|_{H^s},
 \ \|wF_H^\sharp w^{-1}\|_{H^s}<2^{-79000}.
 \tag{U.17}
$$
对原径向右 Poisson还保留
$\Omega_H E_{H,\circ}^\sharp P_{L,\rm int}$ 的同界，
$\Omega_j=\max(1,\langle m\rangle/(1+T_j^\sharp))$。
它只用于真正内部低输入；独立 $C_R$ 或其它外源没有 cutoff 权限。

新的 remaining 比 Y 多了旧 high 中的一段。不能由旧谱选择
直接宣称这些新增行已有 inverse。
令 $E$ 为
$T_j^+\le|m|<T_j^\sharp$，先在同一个径向 full inverse 中
保留这些行，再压缩消去真正新 high。
原 high/deep 准确解耦，且径向全部算子与
$\Lambda_\phi$ 交换。
旧 remaining inverse 的两侧新权费用为
$2^{-270400}$，因为 $v^\sharp=2^{-135200}v^+$。
恢复 $E$ 时，原 high particular 的对角直接项付
$$
 2^{14}\sup_j (v_j^\sharp)^2(1+T_j^\sharp)<2^{-128000}.
 \tag{U.18}
$$
第一阈值分支给
$2^{-151296}J^{-8328}\delta_j^{929/16}$，
平台分支给 $2^{-143232}J^{-8330}\delta_j^{1073/16}$；
因此 (U.18) 包含所有浅层。
两个旧 high Poisson仍在新权上小于 $2^{-9000}$；
完整恢复的 block inverse是
$R_H+E_HR_{\rm rem}F_H$ 及其两条 cross，
所以其全部 norm严格小于1。
这是真正恢复原已知 inverse 的有序 block 恒等式，
不是重新抽取一个“有限窗口数”。
由此
$$
          \|v^\sharp R_{N,\circ}^\sharp v^\sharp\|_{H^s}\le1 .
 \tag{U.19}
$$
同一公共五盒参数点可用；没有另外逐频选择参数。

## 6. deep-low、remaining 差及完整 mean

deep-low 投影保持原
$P_D=\mathbf1_{\{j\ge8193,\ 0<|m|\le
2^{-40}\delta_j^{-1/8}\}}$，
$F_j=2^{4096}J^4\delta_j^{-5}$。
径向
$E_{H,\circ}^\sharp P_D=P_DF_{H,\circ}^\sharp=0$
仍是准确零式。
原 deep Green 在 Fourier 频率上对角，因此其 $H^s$ kernel
门没有额外角费；actual 差按 (U.15) 付第2节费用。
原两种有序差
$$
 \Delta S_HP_D=[I,F_{H,a}]\Delta\widehat U P_D,\qquad
 P_D\Delta S_H=P_D\Delta\widehat U[I;E_{H,a}]
 \tag{U.20}
$$
仍将一次角导付成 $2A_j$。所有高外长程反馈由 (U.17)
控制；新有限行在 (U.20) 中准确不出现。
因此原完整 deep-low L.21--L.27 的真允许线、Green与两侧Poisson
在本篇每个 $H^s$ 窗满足
$$
 \|wF^{-1}R_D^\sharp F^{-1}w^{-1}\|<2^{66},\quad
 \|wF^{-1}E_D^\sharp w^{-1}\|,
 \ \|wF_D^\sharp F^{-1}w^{-1}\|<2^{130}.
 \tag{U.21}
$$
无限尾没有被截成有限终点。上述 $w$ 包括
$1,v^\sharp,(v^\sharp)^{-1}$ 及证明用 $F^{\pm1},F^{\pm2}$；
其邻块比仍在原 $2^{256}$ 之内。

现在完全按 Y.21、Y.23 的两个有序 Schur 恒等式，重付完整
actual-minus-radial remaining 差。
相对 Y，角窗费至多 $2^{196608}$；
一次 low cutoff 至多增 $2^{983040}$；
双逆谱权增 $2^{270400}$。
所以原直接项 $2^{-5868864}$ 变成至多
$$
                 2^{-4418816}.
 \tag{U.22}
$$
三个含 deep Poisson 的项由 (U.20) 收 $A_j$，
没有新的 $T_j^\sharp$ 费用；
原 $2^{-5934500}$ 变成至多 $2^{-5467492}$。
其准确深幂仍为
$31867/256-1987/16=75/256$，全部65536层前的有限段和
之后的几何比均与 Y 相同。

有限新行另算，不能只换旧权。$j\le131$ 给
$(v_j^\sharp)^{-1}<2^{638200}$，有关阈值是
$2^{1056768}$。真实列和及 Poisson 因子再付 $2^{20}$，
完整 bits 为
$$
 2\cdot638200+262144+196608+1056769+20=2791941 .
$$
故此项小于
$2^{2791941}(\mathcal X+\epsilon_L)<2^{-5596666}$。
三个来源相加，安全得到同一完整 Hilbert 算子门
$$
 \boxed{\quad
 \|(v^\sharp)^{-1}(S_{{\rm rem},a}^\sharp-
                   S_{{\rm rem},\circ}^\sharp)
       (v^\sharp)^{-1}\|_{H^s\to H^s}<2^{-4300000}.
 \quad}
 \tag{U.23}
$$
这里 canonical mean 的全部行列在内；不是只证明非mean压缩。

径向 mean Green仍为 Z.11 的从平端向外的真实 height/flux积分，
不是开放 Robin inverse。Z.15 的向外增长核乘新 $v^\sharp$
后更小；mean 与 $\Lambda_\phi$ 准确交换。
加 (U.19) 得完整径向 generalized inverse
$R_\circ^\sharp$，同样满足 Z.17 的全部恒等式，
$\|v^\sharp R_\circ^\sharp v^\sharp\|\le1$。
$ \|v^\sharp c_\circ\|<2^{-595200}$。

在强 source 空间
$\mathscr Y_s^\sharp=\{k:\|(v^\sharp)^{-1}k\|_{H^s}<\infty\}$
直接解
$$
 h=k+\Delta S^\sharp(c_\circ\lambda+R_\circ^\sharp h),
 \qquad
 x=c_\circ\lambda+R_\circ^\sharp h .
 \tag{U.24}
$$
(U.23) 给真正同空间收缩。Z.19、Z.21--Z.27 的准确物理
通量恒等式于是给 (U.3)，包括
$\mathcal L_a\sigma_\circ\ne0$。
$s\ge0$ 时这些强 source属于原 Z 的物理域；
新的全局常数权比有限，原 root mean 两迹的同一性保持。
因此由原域唯一性，本篇解与原较弱解准确相同。
没有以弱序列 norm把“零平端高度”擅自宣布为闭条件。

## 7. 真正 source 域及两向恢复

所有 physical 普通、weak、BV/原子、$\nu$、
$D\Gamma^*$、独立 $B_R,C_R$ 和参数坐标列，
先按原完整 Piola、total flux、density、根图、strict及正DN
映射得到同一个 $\widehat g=H_a^*g$。
随后准确有
$$
 k_L=g_L+F_H^\sharp g_H,\qquad
 k=k_{\rm rem}+F_D^\sharp k_D ,
$$
$$
 x_D=E_D^\sharp x_{\rm rem}+R_D^\sharp k_D,\qquad
 x_H=E_H^\sharp(x_{\rm rem}+x_D)+R_H^\sharp g_H .
 \tag{U.25}
$$
本篇要求的窗口逐项为：
high source在 $H^{s+1}$，
deep source在 $\|wFk_D\|_{H^s}$，
remaining source在
$\|(v^\sharp)^{-1}k\|_{H^s}$；
相应状态按 (U.17)、(U.21)、(U.3) 读取。
每个 source分量使用其真实单位。一般 body $L^2$
不自动给 $F^t$ 裸端荷；原子解保持单侧迹/BV解释。
参数微分仍包括 $\dot H_a^*g$、真实端角/停止尺度项、
$\delta(a_Bw_B)$、$\delta\mu_0$、$\delta\Phi_R$，
以及两条 $\Gamma^*$ 列。固定背景的本定理没有把这些列设零。

在任意有限根/Fourier截断先用这些原位恒等式，
以 (U.17)、(U.21)、(U.23) 的与穷尽无关界取极限。
反向恢复出的 actual incoming在原真实平端域中唯一。
这同时证明整个 mixed 网络，而非只证明逐模径向正型。

## 8. 同一物理帽在全部有限窗上的真实 Schur

此节保持 L.1--L.28 的精确范围：
原 ac1 physical cap，或 C.8--C.9 已认证的连续修补 physical cap，
固定 $\eta_0,\delta=0$。
不将原 $L^2$ Hessian小量转授为
$H^{-3/2}$ 的 moving/all-$4\mathbb Z$ 图，也不扩到 full $\delta$。

记 $s_B=a_Bw_B$。原真正同物理角 complex-shift family及
signed-lag核，在第2节收费后给
$$
 C_f:H^{s+1/2}_\perp\longrightarrow H^{s-3/2}_\perp,
       \qquad \|C_f\|<2^{40}B_*,
$$
$$
 Q_Z:H^{s-3/2}_\perp\longrightarrow H^{s-1/2},
       \qquad \|Q_Z\|<2^{64}B_*\,s_B\epsilon_L .
 \tag{U.26}
$$
这里 $Z$ 是 L 中的非mean曲率未知；实际 $B_R,C_R$ 两mean仍由
原独立荷/holonomy方程读取，不作为任意附加自由零模。
$Q_Z$ 仍含真实未匹配
$P_{\mu_T}M_{r_\mu}$、全部 particular mean和 raw $c_B$；
不是将帽曲率 mean先投掉。
旧QB/Qc同一物理角 $A_{1/64}$ 门与 L28 的修补转授在这里照用，
没有把 derivative upper相减成新的差界。

完整 B/root positive source窗也同样增加至多一份 $B_*$：
真实 adjoint root Wronskian含 mean，
$R_{\rm adj}=R_a^{-*}$ 的次序不改。
用 (U.3)、(U.17)、(U.21) 及有限根129--131的实际单位，
全尾边界响应满足
$$
 T_B:H^{s-1/2}\longrightarrow H^{s+1/2},
                         \qquad
             \|T_B\|<2^{1600000}/s_B .
 \tag{U.27}
$$
具体有限费用可核为：源、状态两次
$(v^\sharp)^{-1}<2^{638200}$；
两次角 moment $2^{65536}$；
原 positive强 source 14000 bits；
两次有限 $F<2^{5000}$；
其余高/deep Poisson、两个 unitary表示和源的有限和
小于 $2^{1024}$。总和
$2\cdot638200+2\cdot65536+14000+10000+1024
=1432496<1600000$。
根源已有准确的一阶余量，未以有限 cutoff给任意外输入补这个导数。
零物理高度 gauge和真实 flux兼容按第6节保留。

原准确 coupled equation仍是
$$
 Z=Z_{\rm cap}+C_f f_B,\qquad
 f_B=f_B^{\rm tail}+T_B Q_Z Z .
$$
于是于每个 $H^{s-3/2}$，完整反馈满足
$$
 \|C_fT_BQ_Z\|
 <2^{1600000+2\cdot65536+104}\epsilon_L
 <2^{-31000000}.
 \tag{U.28}
$$
原所有 $s_B$ 准确抵消，帽全高反馈没有被截成有限头。
因此 $I-C_fT_BQ_Z$ 在这些同空间窗的 inverse norm小于2。
这是真实 physical cap-tail Schur；通量兼容、独立 $B_R$ mean、
原 long mean高度跨度和 nonlinear mean条件依然是原方程，
未由本节自动消去。

## 9. 本结论与下一项的明确边界

本篇付清的是固定实际背景的1024阶角 Sobolev闭网络及同空间物理
帽 Schur。没有把它改名为原 $\ell^1_{224}$ analytic标签逆：
$H^s\to H^{s+4/3}$、甚至任何指定有限阶的这一结论，都不能推出
指数 Fourier 权的返回。nonlinear angle pullback尤其不能靠
“有一个正解析条带”就获得未付的固定224权。

也没有单凭角正则宣称平端 $C^2$。将它用于原几何完成标准，
下一步必须显式使用 remaining 的
$|m|>2^{-40}\delta_j^{-1/8}$，
把角衰减变成层衰减，重付真实 mean 的向外因果Green、
全部 high/deep源和 physical root/strict/positive重建；
最后再处理原非线性方程及 $\nu$/全参数兼容。
本篇所有新常数均由显示的有限角公式和旧完整核重付，
没有新的数值实验，也没有重算旧科学 native。
