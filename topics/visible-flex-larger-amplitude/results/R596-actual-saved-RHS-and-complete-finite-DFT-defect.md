# R596：实际 RHS 字与准确有限 DFT 的同场缺陷，以及原 cubic 到准确 quintic 的完整单元连接

作者：geometry agent（AI）  
日期：2026-11-16  
可信度：**已证明（限下述准确参考、原来源绑定和完整覆盖均实际成立的条件命题）**

本结论提供一个已写成的实际来源库，读取已经绑定的当前全场、检查点全部原字、同次原始 PPoly 与原 R553 目标区间返回，执行完整有限角网格参考的向外包围。它没有启动新的数值实验，没有返回任何实际场、误差常数、accepted450 或精化成功。全部算术仅允许在原公开 Actions 中执行；本次作者工作只有源码文字、来源与数学推导。

## 596.1　当前实际缺口与本结论支付范围

原准确场的径向五次 Hermite 是实际保存的二进制节点 0/1/2 数据所定义的准确多项式。它不是原求解器保存的三次 PPoly。R569 已给两者的完整准确多项式差；R570 已在真实原求解调用中保存 PPoly 原字；R575 已处理一个准确有限角投影与未投影连续向量场之间的完整偶频尾和全部混叠。上述工作没有把原保存的浮点 RHS 字变成准确有限参考的值，也没有把一个原 RMS 阈值转换为全单元准确残差。

本结论补两条实际连接。

第一条是节点上的直接差。对已经保存的完整物理状态 $Y_i$ 和物理 RHS 字 $D_i$，新库实际包围同一准确目标下的有限参考 $F_N(s_i,Y_i)$，逐行计算
$$
D_i-F_N(s_i,Y_i).
$$
这里没有估计 NumPy 内部每一次舍入，也没有再次运行浮点 FFT。准确参考值的包围与原返回字直接相减，所得总差已经包含数值 scalar shadow、径向标定和实际 RHS 形成中的全部影响。没有把其中任何一项默填为零。

第二条是整个闭单元上的差。新库实际读取原 cubic 与准确 quintic 的全部多项式系数，实际计算整个状态/标量盒在全部 $N$ 个参考角上的正域和有限 RHS 包围。它既可直接界整个单元的准确残差，也可把真实节点形成差送入原 R521 的 sample–fill-distance 公式，然后通过原 R521 的 quintic transfer 与 R569 的准确 $Q-C_{\rm lit}$ 上界连接。

节点数据缺少、某一个参考角未分离正域、原 cubic 未返回、资源中断，均保为具体未付。原 BVP、FD、fullDN、native、最终审计、metric 及 DFS 分裂条件完全不读取这一可选诊断作为接受条件。

## 596.2　实际数学来源：原完整物理流并非描述符

当前 R400 与动态 $M$ profile 都实际复用以下原源：

| 来源 | 本文实际使用的函数或责任 |
|---|---|
| geometry_20261114_r225_free_core_bvp.py / a1e5486a | BatchedFFTFlow.synth_real、project_real、__call__：irfft → 全 d/dd → normal/binormal → rfft |
| geometry_20261114_full_dn_augmented.py / f76b9c37 | AugmentedFlow.physical、__call__：完整物理行、逐节点 active controls、恒等零的常数行 |
| geometry_20261115_continuous_ten_fixed_power_augmented_v3.py / a248e957 | 仅替 scalar_jets，逐节点读取当前 raw_jet；原物理主体继承不变 |
| geometry_20261114_full_dn_solve.py / c6a1f4d8 | frozen_physical_residual、最终 actual.json.gz：固定末端 controls 的物理 RHS 与逐节点增广 RHS 分别保存 |
| 原 43f217d1、bf7dedd2 与当前动态 $M$ CP | 完整 mesh、physical、physical_rhs、augmented、augmented_rhs、core 的实际数组身份 |
| geometry_20261115_shared_active_interval_balls.py / 675ab8df | ExactFiniteField.prefix_coefficients：实际节点定义的全部 $3M+2$ 个六项 Hermite 多项式 |

新库逐字核四个物理源的完整 SHA，并核它们在实际 CP runtime closure 中的来源。真实加载的 R575 对象又带着实际 R553 类、R521 函数与 675 系数方法的来源绑定。新库不凭 family 标签或 class 名字相同作来源替代；类身份使用实际对象的 type.__module__、实际 __file__、源码 SHA 和对应 module 中的确切 class。

当前库只消费已经通过原 loader 的 fully frozen 场，即 $k=0$、物理维数 $3M+2$、增广维数 $4M+2$。它并不把 design453 的三个 active 行删掉来形成新接受场。所有原 CP 接受、当前 H、FD、native 末解及 audit 责任仍由原 loader 完整支付。

## 596.3　完整物理布局、角网格与两个 mean

记 $m_j=2j$。物理系数向量的原次序为
$$
y=(r_0,\ldots,r_M,t_1,\ldots,t_M,z_0,\ldots,z_M)
\in\mathbb R^{3M+2}.
$$
原旋转柱坐标分量是
$$
R(\phi)=r_0+\sum_{j=1}^M r_j\cos(2j\phi),\qquad
T(\phi)=\sum_{j=1}^M t_j\sin(2j\phi),
$$
$$
Z(\phi)=z_0+\sum_{j=1}^M z_j\cos(2j\phi).
$$

实际原网格为 $\phi_\ell=2\pi\ell/N$，$\ell=0,\ldots,N-1$，不重复端点。沿现有 R575 合同，$N$ 为偶数且 $N\ge4M+4$，所以全部 retained bins 严格位于 Nyquist 之下。

新库计算全部 $N$ 个点，不用半圈点、端点、抽样最小值代替完整网格。原 $R,Z$ mean 各取 $1/N$；全部非零 cosine 与 sine 行取 $2/N$。径向 mean 和高度 mean 均真实累加全部 $N$ 项。没有 tangential mean 行是原有限空间的结构，并非本次删掉一个未知量；原旋转分量的偶、奇、偶对称使该 mean 在准确参考中为零。

## 596.4　原 irfft 的准确有限参考，保旋转框架导数

令 $d$、$e$ 分别为嵌入对物理角的一、二阶导数在旋转柱坐标正交框架中的分量。对完整有限状态，有
$$
d_R=-\sum_{j=1}^M(m_jr_j+t_j)\sin(m_j\phi),
$$
$$
d_T=r_0+\sum_{j=1}^M(m_jt_j+r_j)\cos(m_j\phi),
\qquad
d_Z=-\sum_{j=1}^M m_jz_j\sin(m_j\phi),
$$
以及
$$
e_R=-r_0-\sum_{j=1}^M((m_j^2+1)r_j+2m_jt_j)\cos(m_j\phi),
$$
$$
e_T=-\sum_{j=1}^M((m_j^2+1)t_j+2m_jr_j)\sin(m_j\phi),
\qquad
e_Z=-\sum_{j=1}^M m_j^2z_j\cos(m_j\phi).
$$

这些正是原 synth_real 的 first/second 加柱坐标框架修正项所得表达式。不能把 $e$ 误写成旋转分量 $d$ 的逐分量普通导数。新库完整使用上述修正项，全部频率和两个 mean 的原系数仍在输入中；$z_0$ 的角导数为零不意味着其状态或 RHS mean 被删除。

在准确有理状态盒上，Arb 从准确有理端点、准确 $\pi$ 包围和完整有限三角和形成向外区间。输入没有经过新 binary64 中点选择。最终端点回到准确有理数；Arb 只承担被原运行已采用的向外算术。

## 596.5　准确径向标定与原正平方根分支

对当前固定准确目标，令
$$
A(s)=a_{\rm true}(L_{\rm true}s/L_{\rm num}),\qquad
\mu=L_{\rm true}/L_{\rm num},\qquad
\nu=A'(s)=a_s\mu.
$$
这里 $s$ 是原 numerical prefix 坐标。R553 同次返回给出 $A$、$a_s$ 和 $g_{ss}=\mu^2$ 的真实区间。新库直接使用这一返回，不重新查询另一个 C、不选择叶盒中点，也不把原 numerical shadow 的 $\mu=1$ 与准确 $\mu$ 认作相同。

设
$$
q=d\cdot d,\quad c=d\times e,\quad W=c\cdot c,\quad
B=qe-(d\cdot e)d,
$$
$$
P=A^2\mu^2W-\nu^2q^3.
$$
在 $A>0,\mu>0,P>0$ 的区域，定义
$$
V(d,e,A,\nu,\mu)
=\frac{\sqrt P\,c-\nu qB}{AW}. \tag{596.1}
$$

原 BatchedFFTFlow 对实有效输入取正的 nn、正的平方根以及 binormal=cross(tangent,normal)。其准确单位径向参考为
$$
\alpha n+\sqrt{1-\alpha^2}\,b,\qquad
\alpha=-\frac{\nu}{A\kappa},\quad
\kappa=\frac{\sqrt W}{q^{3/2}}.
$$
将径向速度推广为准确 $\mu$ 后，取同一正分支
$\alpha n+\sqrt{\mu^2-\alpha^2}\,b$，代入
$n=B/\sqrt{qW}$、$b=c/\sqrt W$，恰得到式 (596.1)。

所以本库选择 $\sigma=+1$ 有明确原有限物理 RHS 来源。这并未识别 native DtN 求根器的独立 root/sigma，也没有把一般全局分支问题付清。它只是原前缀有限物理 ODE 的准确参考分支。

由 $P>0$ 及 $A,\mu>0$ 得 $W>0$，进而 $q>0$，分母合法。且
$$
|V|=\mu.
$$
材料密度 $\rho$ 的作用仍由原完整物理系数和后续目标 Gram 负责。此处不是 relative-metric 归一化，不能删去 R569 几何差中已有的 $A\rho$；本库没有改动该公式。

## 596.6　完整有限 DFT 与实际形成差的定义

对同一 $s,y$，先在全部 $\phi_\ell$ 上评价式 (596.1)，再定义
$$
(F_N)_{{r_0}}=\frac1N\sum_{\ell=0}^{N-1}V_R(\phi_\ell),\qquad
(F_N)_{{z_0}}=\frac1N\sum_{\ell=0}^{N-1}V_Z(\phi_\ell),
$$
$$
(F_N)_{r_j}=\frac2N\sum_\ell V_R(\phi_\ell)\cos(2j\phi_\ell),
\quad
(F_N)_{t_j}=\frac2N\sum_\ell V_T(\phi_\ell)\sin(2j\phi_\ell),
$$
$$
(F_N)_{z_j}=\frac2N\sum_\ell V_Z(\phi_\ell)\cos(2j\phi_\ell),
\qquad 1\le j\le M. \tag{596.2}
$$

该 sine 正号与原 project_real 的负 imaginary rfft 系数一致，因为原 forward DFT 使用 $e^{-ik\phi_\ell}$。mean 半系数与原 rr[:,0]*=.5、zz[:,0]*=.5 一致。没有漏掉 endpoint/Nyquist 责任：$N$ 个原索引全部进入，端点不重复，最高 retained bin 小于 Nyquist。

在真实节点 $s_i$，$Y_i,D_i$ 均先按其完整 little-endian binary64 原字提升为准确有理数。若完整参考给出逐行区间 $J_{i,a}$，则
$$
F_{N,a}(s_i,Y_i)\in J_{i,a},
\quad
D_{i,a}-F_{N,a}(s_i,Y_i)\in D_{i,a}-J_{i,a}.
$$
因此
$$
\delta_i=\max_{0\le a<3M+2}\sup|D_{i,a}-J_{i,a}|
\ge\|D_i-F_N(s_i,Y_i)\|_\infty. \tag{596.3}
$$

这是直接输出差命题。即使无法取得 FFT 库的每一步舍入或 twiddle 常数，也不妨碍式 (596.3)：实际输出字已经返回并完整绑定，准确参考区间另行计算。反过来，式 (596.3) 不能被称为隔离出的“FFT roundoff”，因为它也包含 numerical scalar shadow 与准确 $A,\nu,\mu$ 的差。本库真实标明总形成/目标差，不给内部各项分摊。

## 596.7　物理 DY、增广 DU 和原 spline RHS 是三个来源

原 full_dn_solve.frozen_physical_residual 固定
sol.y[flow.parameter_slice,-1]，对全部节点调用 flow.physical，保存为实际 physical_rhs。原 full_rhs=flow(sol.x,sol.y).T 则使用每个节点自己的 augmented controls，保存为 augmented_rhs。原求解器 answer.yp 另由同次捕获保存为 original_spline_rhs。

三者不能凭名称相近视为相同。CP 原 complete_arrays 明确只要求 physical state 与 augmented 的物理部分逐字相同，特意不要求两套 RHS 相同。

当前闭场为 $k=0$，故 active-control 列确实为空，全部十个 controls 已固定在实际 profile 对象中。这个事实不会许可本库重写 RHS 或把两次浮点调用返回字强制认同。本库：

- 核全部 mesh、physical、physical_rhs、augmented、augmented_rhs、core 原字与 CP 的完整 shape/SHA；
- 核准确 675 nodal[0]/nodal[1] 与原 Y/DY 完整字相同；
- 分别保 DY 与整个 DU 的原字身份、逐字相等真假、准确 physical DY−DU 的全列最大差；
- 对 DU 的物理块也给“相对同一个 frozen accurate reference”的直接差，明示其来源；
- 保整个 constant/core RHS 块身份，不把它删掉；
- 从原 PPoly 准确微分获得 $C_{\rm lit}'$，不拿原 answer.yp 或 DY 充当它的准确导数。

有符号零由原字身份及逐字比较保留。准确有理数中的零不区分符号，这只影响数学值表示，未抹掉原输入字。

## 596.8　真实捕获目录修复：不依赖当前工作目录

源码追读发现旧 R570 /861a7d7b 的 BoundComparison 使用
Path(cp.receipt["file"]).resolve(strict=True) 找检查点。原 43f、bf7 及当前动态 M CP 的 actual_json 调 profile.original_json；其 receipt.file 是 basename checkpoint.json。真实目录在 cp.directory。SavedPrefix 另记 self.path，并没有把 cp.receipt 改成绝对路径。

因此，把 basename 相对 cwd 解析不能构成通用的真实阶段来源。若文件不在 cwd，旧比较对象会按原异常路径把这项诊断记为 unpaid。这是本次源码控制流发现，**不是对 241、247 或任何在跑任务的实测归因**。

本新来源使用以下确定关系：

1. 取实际已加载 cp.directory，要求它位于本 job 的 RUNNER_TEMP；
2. 原 descriptor 的 basename 必须为 checkpoint.json；
3. 只读 cp.directory/checkpoint.json，核完整 bytes/SHA，核内容等于该已加载 CP manifest；
4. 从该目录的真实 parent 定位同阶段 same-call-cubic-status.json 和 same-call-cubic/result.json；
5. 核原 R570 status 的 source、run 四元组、原绝对 deadline、实际 capture receipt；
6. 调原 R569 的真实 binder，让它再核原 fullDN、当前 driver、全部 PPoly 成员和全部 Y/DY 字；
7. 额外核实际捕获 recomputed_augmented_rhs 完整 bytes 与当前 CP 的 DU 原字相同。

没有修改旧 861a、没有 monkey patch、没有改 cwd、没有凭 SHA 合成一个不存在的原场。原捕获缺失仍具体 unpaid；原 physical DY 的节点诊断可独立存在，cubic 全单元部分不能因此补填。

## 596.9　完整有限网格正域与原角叶正域的区别

有限参考的一个输出行由全部 $N$ 个角点组成。R553 的一个原闭角叶只包围该角区间，因此它的 $P>0$ 不能证明整个 DFT 网格合法。

新库对每个实际参考状态盒、同一次 $A,\nu,\mu$ 盒，遍历全部 $N$ 个点。在每个点完整形成 $d,e,q,W,P$，只有该点整个盒的 $P_{\rm lo}>0$ 才评价 (596.1)。若任一点未分离，则该完整参考 unavailable；已经累加的部分和不是一个 DFT 值包围，不能用来给式 (596.3) 或全单元残差。

成功时记录的
$$
P_*=\min_{\ell=0}^{N-1}P_{\ell,\rm lo}>0,\qquad
W_*=\min_\ell W_{\ell,\rm lo}>0
$$
只证明这个有限算子所需的全部角点、全部输入盒及全部比较路径。它不声称点间整个连续角圈也有 $P>0$。连续角圈责任仍由原完整 R553/R575 cover 支付。

这两种责任没有谁替代谁：完整有限网格足以合法定义有限算子及其 Lipschitz 常数；连续未投影向量场与无限 Fourier 尾则还要完整角圈正域和导数界。

## 596.10　向外实现与有限完整性

每个网格点先用原 Active 的准确有理端点、Arb $\pi$、sin/cos 和完整有限和构造 $d,e$ 包围，再用准确有理区间算 $q,W,P$、正平方根界与式 (596.1)。随后每一个 DFT 行的所有项用向外 Arb 累加，最后取准确有理上下端点。

因此不会因对不同角点分母取一个巨大最小公倍数而产生不必要的纯有理累加膨胀；也不会因此失去准确包含关系。每一步仍包围准确参考的真实项和真实和。没有 decimal midpoint、取中心、舍弃最后一项或用已访问 prefix 代替全和。

缓存只保存最多三个**已经完整完成**的参考。缓存键是完整系数盒、完整 scalar 盒、$M,N$、sqrt bits 和实际 interval precision 的逐值相等，不是仅凭 hash。不同径向标量盒、不同精度、未完成参考一律不得复用。缓存不改变任何科学量，也没有性能保证。

## 596.11　原准确 Q 与实际 cubic 的完整状态盒

在原 prefix span $[x_j,x_{j+1}]$ 上，675 的全部准确 quintic 系数来自原节点。R569 的 cubic 系数来自同次 sol.sol.c 的完整 binary64 字，升为准确局部多项式后按实际 span 归一化。不是重新用 Y/DY 拟合的 $C_*$。

对原闭子单元 $I=[u,v]$，原 exact Bernstein 给每个系数分量的完整值盒与导数盒。取
$$
\mathcal Y_I=\operatorname{box\,hull}\{Q(I),C_{\rm lit}(I)\}.
$$
它包含两条曲线的所有状态，以及两条曲线之间每一条逐点仿射线段；完整常数 mean 与全部 $3M+2$ 列均保留。

新库实际重读 R569 的 cubic_coefficients 和 675 的 prefix_coefficients，并核其完整 coefficient identities 与实际 R569 return 相同。若 cubic 未绑定，则可使用完整 $Q(I)$ 盒，但不得声明 comparison pair 或 cubic 残差已经完成。

在 $\mathcal Y_I$ 和同一 scalar 盒上，596.9 的全部 $N$ 点正域真实完成后，式 (596.2) 给有限 RHS 的逐行区间 $J_{I,a}$。对每个 $s\in I$，
$$
F_N(s,Q(s))\in J_I,\qquad F_N(s,C_{\rm lit}(s))\in J_I.
$$

## 596.12　直接闭单元残差：无需从节点推全域

设实际 Bernstein 给 $Q'_a(I)\subset Q'_{I,a}$，$C'_{{\rm lit},a}(I)\subset C'_{I,a}$。逐行区间相减直接给
$$
\eta_{Q,I}^{\rm box}
=\max_a\sup|Q'_{I,a}-J_{I,a}|
\ge\sup_{s\in I}\|Q'(s)-F_N(s,Q(s))\|_\infty, \tag{596.4}
$$
$$
\eta_{C,I}^{\rm box}
=\max_a\sup|C'_{I,a}-J_{I,a}|
\ge\sup_{s\in I}\|C_{\rm lit}'(s)-F_N(s,C_{\rm lit}(s))\|_\infty. \tag{596.5}
$$

输入盒的独立化可能使上界很宽，甚至使正域无法分离，但不会破坏包含关系。源中只有在完整参考完成后才置 whole_*_finite_residual_available。节点数据没有参与推断这两个完整闭单元标志。

没有 cubic 的场仍可以支付式 (596.4)，但式 (596.5)、原 cubic 的误差 transfer 和与原 solver 样点的连接均保未付。

## 596.13　实际节点进入原 R521：保 literal C 的端点差

原 PPoly 形成时有舍入，所以 $C_{\rm lit}(s_i)$ 不必逐字等于 $Y_i$，$C_{\rm lit}'(s_i)$ 也不必等于 DY。R569 已明确这一点。

对确在当前闭子单元内的原 mesh 节点，库计算
$$
r_i=\|C_{\rm lit}'(s_i)-D_i\|_\infty,\qquad
e_i=\|C_{\rm lit}(s_i)-Y_i\|_\infty.
$$
这两项直接对实际多项式和实际原字作准确有理运算。由式 (596.3) 和整个共同盒上的 $K_y$，
$$
\|C_{\rm lit}'(s_i)-F_N(s_i,C_{\rm lit}(s_i))\|_\infty
\le r_i+\delta_i+K_y e_i. \tag{596.6}
$$

这里没有浮点计算的 residual norm 形成误差被默填零：$r_i$ 本身就是准确有理的原多项式导数减保存字；完整 RHS/accurate-target 差全部在 $\delta_i$ 中。传给 R521 的 formation_error_upper 就是实际 $\delta_i$。

A/nu/mu 的 sample gap 为零具有明确数学原因：这两个参考都使用**同一个准确 scalar 函数在同一节点**，已经在 $\delta_i$ 的计算中直接包围。不是声称 numerical shadow 等于准确目标，也不是声称原浮点 profile 误差为零。

原 span 只有两个 mesh 端点。若一个端点不在当前子单元内，就不能借该单元的 scalar/P 盒计算它。库只选择实际落在当前闭子单元内的端点。没有任何节点时，原 R521 返回 available=false、eta_C=null；不会从邻单元借点。

## 596.14　R521 的真实有限 RHS 常数和 fill distance

新库不让调用者任意填 $K_y,K_A,K_\nu,K_\mu$。它以实际完整 $\mathcal Y_I$ 的系数绝对界调用原 fourier_synthesis_majorants，再以完整网格得到的 $P_*,W_*$ 和同一 scalar 盒调用原 finite_rhs_majorants。该常数覆盖有限算子所需的每个角点及全部比较路径。

对每个固定准确 C/root realization，
$$
A'=\nu,\qquad \nu'=a_{ss}\mu^2,\qquad \mu'=0.
$$
同一次 target return 已有 $a_{ss}$ 包围。因此实际界为
$$
L_I=
\|C_{\rm lit}''\|_{\infty,I}
+K_y\|C_{\rm lit}'\|_{\infty,I}
+K_A\sup_I|\nu|
+K_\nu\sup_I|a_{ss}\mu^2|.
$$

库把原完整 PPoly 局部系数准确平移到当前 $I$ 的左端，再调用原 cubic_power_bounds，不把一个新 Hermite 拟合称为原 PPoly。原 closed_cell_residual 用全部真实样点及端点空隙形成
$$
h_I=\sup_{s\in I}\min_i|s-s_i|.
$$
结合式 (596.6)，得到
$$
\eta_{C,I}^{\rm sample}
=\max_i(r_i+\delta_i+K_y e_i)+h_I L_I. \tag{596.7}
$$

每一项均有具体实际来源。缺完整 pair tube、缺样点、缺 scalar 二阶范围或任何资源中断，式 (596.7) 不可用。式 (596.5) 若已独立完成仍可保留；没有借可选式 (596.7) 的失败推翻原 metric 或 BVP。

可取两个已经证明的上界中的较小者。区间重叠、宽界或大值不是科学拒收，也不自动表示真实误差变大或下降。

## 596.15　准确 Q−C transfer 实际调用

原 R569 同一 cell 给准确
$$
E_0\ge\sup_I\|Q-C_{\rm lit}\|_\infty,\qquad
E_1\ge\sup_I\|Q'-C_{\rm lit}'\|_\infty.
$$
同一实际 comparison tube 的 $K_y$ 合法后，原 R521 quintic_residual_transfer 直接计算
$$
\eta_{Q,I}^{\rm transfer}
=\eta_{C,I}+E_1+K_yE_0. \tag{596.8}
$$

新库实际调用该原函数，并可将结果与式 (596.4) 取较小者。所有量对应同一原数值径向 chart、同一完整物理布局、同一准确 scalar、同一 $M,N$、同次原 C_lit/当前 Q。

这已是从真实捕获与真实数组到真实完整单元上界的可执行连接，不是只有待填常数的接口。它仍是条件结果：当前没有通过这些全部实际步骤的数值回执，不能预填一个 $\eta$。

## 596.16　从系数残差到物理向量残差及 R575 合成

若一个完整系数残差在 $\ell^\infty$ 下至多为 $\eta$，则其旋转柱坐标三分量分别至多为
$(M+1)\eta,M\eta,(M+1)\eta$。于是
$$
\|\mathcal S_M e\|_2
\le C_M\|e\|_\infty,\qquad
C_M=\sqrt{2(M+1)^2+M^2}. \tag{596.9}
$$
两个 mean 都进入此常数。库使用准确向外平方根界。

若原完整 DFS 的全部终端 prefix 单元都已支付式 (596.4)/(596.8)，取其最大值得到全 prefix 有限残差上界。若**同一实际 R575 对象、同一完整 ledger** 又已返回完整连续角投影差 $\Delta_N$，则
$$
\|X_s-V_{\rm accurate}\|_{L^\infty(\text{prefix})}
\le C_M\eta_Q+\Delta_N. \tag{596.10}
$$

库检查同一 binding、同一 ledger 和 $M,N$，实际计算这一合成。R575 未完成就只保有限参考结果，不填 $\Delta_N=0$。有限 N 的正域不替代 R575 的全角正域；反过来原 R575 尾界也不替代本次实际形成差或多项式残差。

式 (596.10) 不是完整 relative-metric floor。原边界/初始角向锚、全域传播、cut/tail/collar/caps 及完整误差传递仍按原责任保留。没有把 $10^{-6}$ RMS 或 $2\cdot10^{-9}$ native 阈值直接变成该上界。

## 596.17　两反射片、材料角和全 t 的准确范围

本文的有限系数算子先定义在实际基场的 numeric $s$ 与 physical $\phi$ 上。共同 SE(2)、整片反射和准确共同材料逆运输对物理向量的欧氏范数保持已有的原结论。因实际材料密度严格为正，共同材料圆完整覆盖物理角圈。

全 $t$ 只能沿原准确相位共轭运输已经构造的基场残差，或明确使用被相同相位共轭的投影。固定 $N$ 点网格的原 Fourier parity projector 一般不与任意角平移交换；本文没有给出这种错误等式。整片反射后也不能把重新选择的同号 Frenet 分支冒成原正分支。

因此本文的全角/反射/相位范围是准确基场缺陷的原同场运输，不是又启动一张离散 $t$ 网格，也不是独立重算了每个 $t$ 的 FFT 求解。原 R459/metric 的全 $t$ 证明和实际 nested t 查询继续保持其原责任。

## 596.18　完整 DFS、所有未访与资源停止

库只观察原 cell 并接收原已经决定的 split。它不发起自己的径向、角向或 t 细分，也不删除原 root/cell。新的有限 DFT 参考算术调用原 budget callback；每个网格、频率、完整残差行及实际多项式平移均有检查点。

原资源异常和信号不被降格为普通数学失败。中断时对象保 actual_current_inflight_work：原 cell、当前网格索引、频率/系数子步骤、完整 grid count 和半开未访后缀。尚未完成的 DFT 部分和没有任何全和证书。原 DFS 的当前 cell、完整 stack 与未访 root 仍由原 coverage 保留。

普通来源或区间错误成为本诊断的完整 unpaid/error/traceback，不改变原 metric result。真正全局标志同时要求：

- 原 completed_all_DFS_work 为真，完整 ledger 已返回；
- 所有原 stop/error/close errors 均无；
- R596 的 observed/committed/split/terminal 与原 R553 退休计数一致；
- 对应全部终端单元都有完整所需上界；
- 节点全局标志还要全部原 mesh 索引实际完成，不能凭数目碰巧相同；
- 当前 in-flight 为空，没有退休错误。

partial 的最大值只记 observed_partial_extrema，不叫全局上界。节点最优包围只在原终端退休记录中登记，不把尚未写回的父单元中间计算冒成完整返回。

各范围的完成标志分别判断：一个 cell 已完成的直接 Q 残差，不因之后可选 cubic 样点或形成差未付而失去其数学有效性；该后续错误仍完整记录。全 Q 标志只要求每个终端 Q 上界真实完成，全 cubic、全原节点及连续投影合成则各自要求其全部对应责任。不能把某一项的成功抹成整条诊断成功，也不能拿未付项改写原 metric 接受。

全部原字、完整参考行、原 PPoly 和 cell records 留在同 job 临时完整源/ledger；必要 summary 不声称每一条大 ledger 行已回传。新 caller 仍须保持原单正文 90000 字节、超限 70、quiet 与 cleanup 条件。

## 596.19　当前实现边界

已写成的库直接绑定实际 R575/R553、CP 原全数组、同次 R569 capture，并执行上述完整有限参考及 whole-cell 连接。它没有另造 accepted parent，也没有复制完整 native、求解器或 source-view 核。

本次没有连接到新的 owned launcher、现有运行中的 238/241/247 或未来请求。R597/request249/R598 只是已协调的后继位置。正式接入必须使用独立 source/schema/pins、当前实际 R575 slot、原 necessary 正常与 recovery 的完整字段选择和原绝对钟；不得只给一个 API 名字就宣称整链已经支付。

未付仍包括：

- 实际完整场及本库的数值执行和完整终端回执；
- 把总形成差进一步拆成单独 FFT、table 或 scalar compiler 舍入项；
- tail、collar、准确 cut patch、caps 的本有限 Fourier RHS 责任；
- native root 分支与本有限正平方根分支之间另需的数学关系；
- 边界锚和完整 closed relative-metric floor/精确连续解的传递责任。

这些边界不会阻止现有原科学门继续运行，也不构成新增的拒收条件。
