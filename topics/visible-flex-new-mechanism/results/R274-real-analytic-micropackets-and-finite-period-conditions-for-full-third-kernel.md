# R274：真实解析微包选择与完整第三核修正的有限 period 判据

日期：2026-11-15。**完整纸面证明；没有新增求积、符号执行、人工检查或研究计算。**

本稿把 [R272 的零端逆解定理](R272-smooth-inverse-germs-for-the-full-third-kernel-at-flat-zero-ends.md) 接到 [R270](R270-odd-mother-perturbation-pays-a-further-Gaussian-zero-moment.md)、[R271](R271-six-complete-blocks-pay-the-first-two-positive-negative-Gaussian-moments.md)、[R273](R273-reflection-densities-pay-the-minus-one-minus-two-zero-moment.md) 的真实存在构造。不是事后替换一个已冻结数值圆：在这些构造最初选基础母函数时作下面的解析选择，随后按原顺序固定所有参数和最后位置，并分别求原方程。

对这个共同可选的圆，完整第三对角核 $Z$ 产生的修正具有以下准确性质：

- 全部 $K_f^\tau(g)$ 原式为零，因此两个 mixed 目标的额外 $\zeta$ 历史确实消失；
- 每个最细真实活动包的总通量自动为零；
- 全部零平台二导条件等价于每包一个真实势矩；不得将其换成只验全区间总矩；
- 付清这些势矩后，两端逆解自动光滑。完整 period 只剩这些势矩和全部内部 Laurent 条件。

这些是同一固定圆上的完整必要充分条件，尚未计算其响应矩阵、rank 或是否能消去原 canonical 成本。范围是 $B(E,Z)$ 的两个完整修正目标，不是整个 $\mathcal R_{p0}$，也不是第四 joint 已解。

## 1. 在所有实际求根以前选择基础解析包

取
$
 \psi(y)=
 \begin{cases}
 \exp[-1/(1-y^2)],& |y|<1,\\
 0,& |y|\ge1.
 \end{cases}                                                   \tag{1}
$
它是非零实偶光滑紧函数，在开支撑内解析，两端全平。先以它构造 [R265](R265-companion-directions-and-positive-blocks-pay-an-ordered-Gaussian-area.md) 的有限八微包偶母函数及 TM3 同源伴随，再作 R267/R270 的中央与两侧母包、真实奇扰动、两种外排序、完整八/十二副本以及最终正幅混合。

这些原存在证明对基础非零偶包的使用只要求实际正量 $m,C$、同源导数乘积、有限支撑、相应有限形状积分及 R270 已证的 $K=\int e_v^2>0$。选择 (1) 满足这些条件；不额外要求某个尚未证明的数值不等式。原顺序仍为先小正母宽 $h$、再有限间距 $A$、预选共同合法区间和最终位置、最后小正主宽 $\delta$ 与各处真正四变量 IFT。R271 的六个位置仍分别求根，不能把这里选择的母函数塞进旧根后声称所有条件未变。

R270 的局部奇方向为
$
 e_v=12r^2t+6v't^2+6v'rr'',\qquad r=v'',\quad t=v''' .             \tag{2}
$
它是 $v$ 的三个有限 jets 的和。在一个最细 $\psi$ 微包内，$v$ 只是非零常幅及仿射缩放的 $\psi$；所以 $e_v$ 是同一 $\psi^3$ 乘一个有理函数，其极点只可能位于支撑两端。把微包外延零后仍光滑全平。其他最细微包对 (2) 没有非局部贡献。

因此全部最终 $f,g$ 都是有限个互不交的最细微包的线性组合。每个微包是仿射搬移和实常幅作用下的
$
 \psi+\eta e_\psi,                                               \tag{3}
$
或其反射，$\eta$ 是该实际构造中的有限常数；未扰动包取 $\eta=0$。缩放产生的常因子可吸入 $\eta$。在同一个最细包内，TM3 只改变固定符号，故 $f,g$ 在该整个包上成固定实比例。不能把“成比例”错误上推到包含多个不同方向的整个三母包或完整 block。

## 2. 每个实际零端都有 R272 的准确 germ

在 (1) 的右端写 $y=1-t$。准确地，
$
 \frac1{1-y^2}=\frac1{2t-t^2}
 =\frac1{2t}+\frac14+t\,b(t),\qquad b\in C^\infty .
$
因而
$
 \psi'(1-t)=t^{-2}a_0(t)e^{-1/(2t)},\qquad a_0\in C^\infty,
 \quad a_0(0)\ne0.                                               \tag{4}
$
左端同理，仅改变非零前因子的符号。

任一有限阶导数 $\psi^{(k)}$ 都是 $\psi$ 乘有理函数。由 (2)，
$
 e_\psi'=\psi^3 R,\qquad
 \frac{e_\psi'}{\psi'}=\psi^2\widetilde R                           \tag{5}
$
在每个充分小的端邻域成立；$R,\widetilde R$ 只有有限阶端点极点。这里不声称 (5) 在 $\psi'=0$ 的中心有同一商表达。

有限负幂乘指数全平函数仍光滑全平，因此 (5) 在端点延拓为0，连同全部导数为0。于是 (3) 的导数为
$
 (\psi+\eta e_\psi)'=\psi'\{1+\eta\psi^2\widetilde R\}.
$
大括号在每个端点等于1；任意固定有限 $\eta$ 都不会取消 (4) 的首非零前因子。实际正宽 $w$、非零常幅和反射只把指数常数改成 $c=w/2>0$，并改变光滑非零因子。故每个真实活动包端点 $e$，以向内坐标 $t>0$ 表示，都有
$
 \boxed{f(e)=0,\qquad
 p(e+\sigma t)=f'(e+\sigma t)
       =t^{-2}a_e(t)e^{-c_e/t},\quad
 c_e>0,\quad a_e(0)\ne0.}                                       \tag{6}
$
最细包采用多个相继缩放时，$w$ 是实际总宽度。共同归一和最终正幅混合均为有限非零常幅，不改 (6)。

这是 R272 的明确类，$m=-2$。没有以“全平”代替它，也没有加入另一个形式渐近假设。

## 3. 内部解析、有限临界和有限退化全部成立

以非零 $f$ 最细微包的开支撑为活动区间 $J_j=(a_j,b_j)$。它们有限，彼此及固定外 collar 之间都有正长度的零平台。每个 $f|_{J_j}$ 解析；由 (6) 它不恒定，故没有内部开常平台。

置
$
 p=f',\qquad A_H=6pp''-2(p')^2 .
$
(6) 与 R272 的直接计算给
$
 A_H=p^2t^{-4}\{4c_e^2+O(t)\}.                                  \tag{7}
$
故充分靠近两端时 $pA_H\ne0$。在去掉这些端邻域后的紧内部，$p,A_H$ 均为不恒零的实解析函数。其零点若无限，紧性给内部聚点，解析唯一性便迫其中一个恒零，与端邻域矛盾。因此所有内部零点有限，且各自有限阶。

所以这一个实际新圆满足 [R225](R225-complete-period-range-flat-end-germs-and-finite-observation-quotient.md) 的全部解析活动区间前提。这个证明允许有限内部高阶临界点和 $A_H$ 重零点，不擅自假设全部简单。尚未列出它们的实际位置和个数；有限性不等于已经算完 Laurent 表。

## 4. 全 $Z$ 的原算子与逐包比例消失

由 [R258](R258-self-adjoint-hook-green-operator-and-complete-period-interface.md) 和 [R261 全八原局部式](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md)，对全部
$
 Z=\langle H_0,\ldots,H_6,J_0,J_1,J_2,\chi_1,\ldots,\chi_8\rangle
$
及 $\tau\in Z$，有原右锚身份
$
 K_f^\tau(w)=-J^3(\mathscr A_f^\tau w),\qquad
 \mathscr A_f^\tau
 =D^2(a_\tau D^2)+D(b_\tau D)+c_\tau,\qquad
 \mathscr A_f^\tau f=0.                                         \tag{8}
$
该局部算子自伴，系数关于 $f$ 的有限 jets 二次齐次。右 collar 三个积分常数是原式给出的零，不允许按包重设。

在每个最细包上 $g=\lambda_j f$，$\lambda_j$ 为常数；故
$
 \mathscr A_f^\tau g=\lambda_j\mathscr A_f^\tau f=0.
$
在包外 $f$ 全 jets 为0，全部算子系数为0；全平边界不生分布项。因此
$
 \boxed{K_f^\tau(g)=0\quad\text{于全 }I,\quad \tau\in Z.}         \tag{9}
$
若某微包的 $f$ 幅度为0，那里同样由全部系数为0处理，无须除该幅度；当前两斜率构造的 $f$ 微幅本来都非零。

原完整 mixed 响应含
$
 D_{\tau,A}
 =2K_f^\tau\{\Phi_A(f^2-g^2)\}
       +4\Phi_A(g,K_f^\tau g),
$
$
 E_{\tau,A}
 =-4K_f^\tau\{\Phi_A(fg)\}
       +4\Phi_A(f,K_f^\tau g).                                  \tag{10}
$
(9) 才允许在此圆删去最后两项。其余输入 $\Phi_A$ 保原右锚及真实左多项式尾；它们全局光滑，在每个活动包内部解析。采用 $2\cos\theta\sin\theta$ 规范时，$E$ 列仍须除二。

## 5. 每活动包的总 flux 自动为零

考虑任一实际有限和
$
 G=\sum_{\alpha=1}^N K_f^{\tau_\alpha}(w_\alpha),                 \tag{11}
$
其中 $w_\alpha$ 全局光滑、活动包内部解析，原右侧输出有共同零 collar。式 (10) 的两个完整目标及同一控制系数下的线性组合均属于此类。式中控制系数可吸收入 $w_\alpha$；讨论有限线性映射时，取固定输入 $w_\alpha^0$ 并写 $w_\alpha=\lambda_\alpha w_\alpha^0$，不让已冻结的圆或输入随控制系数重新求根。

[R264](R264-potential-tail-moments-and-complete-platform-flux-equivalence.md) 给每项准确 concomitant
$
 d_\alpha=(a_\alpha f'')'+b_\alpha f'=J(c_\alpha f),
$
$
 \Lambda_\alpha
 =a_\alpha(f'w_\alpha''-f''w_\alpha')
       +w_\alpha d_\alpha-fJ(c_\alpha w_\alpha),
 \qquad
 \Lambda_\alpha'=f'\{K_f^{\tau_\alpha}(w_\alpha)\}''.             \tag{12}
$
在每个真实微包端点，$f$ 及全部 jets 为0，$a_\alpha,d_\alpha$ 亦为0；$w_\alpha$ 及真原函数有限。故两端 $\Lambda_\alpha=0$。所以
$
 \boxed{\int_{a_j}^{b_j}pG''=0
       \quad\text{对每个 }j,\text{ 对整个控制组合成立}.}          \tag{13}
$
这里实际得到逐项零，但后续平台条件仍只对所选控制总和施加。不能因一个整大 block 的通量零，省略其内部多个真正活动包；本稿已在最细分解上逐包支付。

不需预先令平台二导为0便可得 (13)。非零尾常数乘 $\int p=f(b_j)-f(a_j)=0$ 与此相容；这不意味着那些尾已被删除。

## 6. 全部零平台条件等价于逐包势矩

原二导身份为
$
 G''=\sum_\alpha\{(a_\alpha w_\alpha'')'
                         +b_\alpha w_\alpha'
                         -J(c_\alpha w_\alpha)\}.              \tag{14}
$
在零平台，前两项准确为0。定义每个活动包的总势矩
$
 M_j=\sum_\alpha\int_{J_j}c_\alpha(x)w_\alpha(x)\,dx .           \tag{15}
$
从右往左，各平台的原二导是其右方所有 $M_j$ 之和的负值；最右平台给原0，跨过第 $j$ 包恰增加 $-M_j$。因此
$
 \boxed{G''=0\text{ 于全部平台和外 collar}
        \ \Longleftrightarrow\ M_j=0\text{ 对全部 }j.}           \tag{16}
$
总和只有一个零不能替代逐包零。不同控制方向允许在同一 $M_j$ 内相消；不要求每个方向自己的势矩都为0。全部端常数取自原右锚，未作任何重锚。

## 7. 完整 period 的有限必要充分条件

设 (11) 为固定有限组真实输入的线性组合，且同一固定圆已按第1节选择。令
$
 F_j(x)=\int_{a_j}^x pG''=\sum_\alpha\Lambda_\alpha(x),\qquad
 q_j=\frac{F_j}{A_Hp^2}.                                        \tag{17}
$
等号来自真实左端 $\Lambda_\alpha(a_j)=0$，不是自行选择一个有利的通量常数。

在每个内部 $pA_H$ 零点 $\zeta$，记 $n_\zeta=\operatorname{ord}_\zeta p$。内部解析性使 $q_j$ 亚纯，负幂只有有限项。完整条件是
$
 [ (x-\zeta)^k]q_j=0\quad(k\le -n_\zeta-2),
 \qquad
 [ (x-\zeta)^{-1}]q_j=0.                                       \tag{18}
$
不存在的负幂不添加条件。特别，$p$ 简单零点处允许的二阶极点不能错误判失败；乘 $p$ 积分后的真实解才是判据。

**定理。** 对 (11)，存在固定共同双 collar 为零的真实光滑 gauge $v$，使 $L_fv=G$，当且仅当全部 (15) 为0，且全部 (18) 成立。

**证明。** 必要性由 R225：平台门给 (16)，内部光滑性给 (18)。总通量 (13) 在本类自动成立。

反之，(15) 付清全部平台二导。结合 (13)、(6)，R272 对每个活动端给原变参数解
$
 u=v'=p\left(C+\int\frac{F_j}{A_Hp^2}\right)
$
的真实 $C^\infty$ 延拓。输入允许保原多项式左尾，仍满足所需光滑性。有限和与其相消原样包含在 R272 的界中，不要求每项独立可解。这里没有遗留一个“待核平端 germ”。

全部 (18) 使 $u$ 跨越每个内部退化点解析。然后按 R225 在正长度零平台中连接两侧真实端 jets，在共同最外 collar 令 $u=0$，并在一个平台内加紧 bump 令 $\int_Iu=0$。这些平台处原退化算子为0，所以不改已解微分方程。取原右端原函数得到双 collar 为零的 $v$。原右 collar 的 $G=G'=0$ 消去可能的全局仿射差，故确为 $L_fv=G$。证毕。

所有 (15)、(18) 关于控制系数线性且条数有限。在两个 mixed 目标上必须叠放同一控制向量的两组条件，不可分别选两个不相容的控制。若通过，period 所需的两个 gauge 可按原谐波组合；R185 的六矩核投影仍保 period，第四 ruling 仍须使用同一个所得 gauge 联立。

## 8. 已付接口与不能外推的范围

本稿同时保留 R270/R271/R273 已付的全部 profile 条件：解析母包是在最初自由选择中固定，原真实根和最后正幅随后重新按原存在证明选定；所有端芽和活动分解是同一最终圆的性质。没有迁移另一冻结圆的数值、旧 $F_8$ 或几何 metric。

定理给全 $Z$ 修正子像的准确有限线性判据，却没有给它的实际矩阵、零点列表或 rank，更没有证明矩阵足以控制原 canonical 成本。有限零点的存在证明不被冒作“扫描没有再发现零点即可停”的算法证书。

非零 step 端、一般振荡型全平 germ、非逐包比例的 $\zeta$ 历史及完整 $\mathcal R_{71}\cap\ker\pi$ 的其余部分不由本稿覆盖。原完整
$
 \mathcal R_{p0}=(\mathcal R_{71}\cap\ker\pi)+B(E,\langle\chi_1,\ldots,\chi_8\rangle)
$
不能被缩成 $B(E,Z)$。

原 canonical $V_d,V_e$ 未由这里证明具有同一自动端芽结论；若要消去它们，仍须消费它们的完整实际输出、共同控制及全部 period 条件。完整第四 joint、高阶收敛、同固定 $g$ 的有限连续族与 README 几何门仍然未付。
