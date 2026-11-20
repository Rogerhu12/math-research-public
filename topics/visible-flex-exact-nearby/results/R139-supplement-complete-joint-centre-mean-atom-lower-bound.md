# R139 补篇：完整联合中心的独立均值原子下界

2026-11-20，`visible-exact-astra-ac637-20261120`。

**状态：下面的支持恒等式、完整中心范数下界和固定配方排除规则已证明；新的下界标量尚未计算。** 该检查针对完整WJK中心本身，区别于已完成的低频**族差**L，以及已完成的正比较mean-atom必要下界。三个对象和各自目标不混用。

依赖 [WJK完整中心](R133-supplement-joint-centre-Green-kernel-and-complete-collar-cross-terms.md)、[R137准确连续/有限投影](R137-continuous-signed-centre-and-exact-endpoint-system.md)、[R139固定预算](R139-necessary-budget-for-fixed-W2C-comparison.md)、[R140完整均值方程](R140-complete-mean-split-low-family-comparison.md)及原完整signed-packet/assembly。参数、原moving-phi坐标、ordinary dr、真实根和独立even mean均保持。

## 1. 完整中心与准确的一条输入

令原低频193空间的单位even均值基为

\[
e_m=(0,1),\qquad \|e_m\|_{L^2_\phi}=1.
\tag{C.1}
\]

以 `D_f` 表原固定WVC低参考，以 `A_c` 表其修复degree32系数、但保留同一actual eta速度槽的hybrid中心。它不是自然冻结eta_c背景线性化。完整中心为

\[
H_c=\mathcal O_DG_D\{A_c-D_f+C\mathcal F B\}S^{-1}\pi_B.
\tag{C.2}
\]

这是R137的连续版本；若再左乘原 `P_f`，便得到WJK实际使用的有限接收器。`P_f` 对全部193原子是恒等映射。`B=B^c_{HL}`，`C=B^c_{LH}`，中间的完整 `F` 保留所有collar、J/J*、源和有符号项。

只选 transformed body 输入 `z(r)=f(r)e_m`，其中 `f` 是任意实ordinary L2函数，并将两个原子输入槽置零。它在完整输入空间中的范数恰为 `||f||_2`。原S在even分量上乘正的参考q，因此raw输入为

\[
S^{-1}z=\frac{f(r)}{q(r)}e_m.
\tag{C.3}
\]

这里没有选择径向变化的物理参数；`f` 是线性算子的允许输入。原参数仍在其原完整域中固定。

## 2. 高频返回对这条输入严格为零

**命题1。** 原修复中心degree32与同actual-eta定义给出

\[
B e_m=0,\qquad C\mathcal F B\bigl(q^{-1}f e_m\bigr)=0.
\tag{C.4}
\]

**证明。** 中心的 `u,v`、所有65个signed repair系数及其角导都只含 `|j|<=32`。常数输入的角导严格为零，所以actual eta主部不产生任何输出；其数值与自然eta_c是否相同无关。

local系数为至多两个中心因子的乘积，角支持最多64。完整有序primitive对常数输入先乘一个中心因子、去其整个输入的零频、积分，再乘另一个中心角导，支持仍最多64。mean-input rank列 `gamma(K v_phi,-u_phi)` 只到32。投影到高频 `|j|>=97` 后每一项都严格为零。此论证保留独立mean，未从一个mean上界猜测它为零；也没有把真实全degree96族差误当中心degree32。因而高回路的整个输入为零，不论F内部如何传播，完整回路均为零。证毕。

这一消失仅属于**中心**的纯均值列。对原实际degree96族差、非均值输入或其他独立port，均不得据此删除高项。

## 3. 根端均值观察的准确核

记原中心均值为 `m=<v>`，并令

\[
S_m=\langle u^2+K_{\rm geom}v^2\rangle,\qquad
a_{00}(r)=\beta(r)\{1-S_m(r)-2K_{\rm geom}(r)m(r)^2\}.
\tag{C.5}
\]

为免混淆，`K_geom` 表内禀曲率，不是R139预算中中心范数的上界数K。所有角平均均在原moving-phi归一化测度中。

这是原完整mean方程的mean-input/mean-output系数。源码中同一个量由 `fourfold_codazzi_true_collar_signed_packet_math.py::_centre_mean_row(packet,(1,0),...)` 返回，等于 `beta*(1-S_mean-2*K*mc*mc)`；它也等于 `ctx.centre_matrix(((1,0),),((1,0),),box)` 的唯一项。新消费者应直接用这一已有signed系数入口，不另造一个标量模型，不读取 `mean_own_rate` 的正上界代替(C.5)。

参考 `D_f` 的mean生成器为零，原参考外端mean为零。因此raw mean源 `g_m` 的参考解满足

\[
x_m'(r)=g_m(r),\qquad x_m(R)=0,\qquad
x_m(a)=-\int_a^R g_m(s)\,ds.
\tag{C.6}
\]

其余nonmean源不会进入这个独立参考mean块。根端mean是原193观察中的一个单位权原子；有限投影也完整保留它。

由(C.3)–(C.6)，完整中心在所选输入上的这一输出恰为

\[
\operatorname{rootmean} H_c(f e_m)
=\operatorname{rootmean}P_fH_c(f e_m)
=-\int_a^R\frac{a_{00}(s)}{q(s)}f(s)\,ds.
\tag{C.7}
\]

这是一条完整signed核恒等式，没有取局部项的绝对值后假装高项也消失。

## 4. 对完整中心范数的真正下界

**命题2。** 置

\[
J=\int_a^R\left|\frac{a_{00}(s)}{q(s)}\right|^2\,ds.
\tag{C.8}
\]

则

\[
\|H_c\|^2\ge J,\qquad \|P_fH_c\iota_B\|^2\ge J.
\tag{C.9}
\]

**证明。** 单一坐标观察和所选输入子空间的包含都是范数1。式(C.7)是ordinary L2上的积分泛函，范数准确为 `sqrt(J)`。若J非零，取 `f=(a00/q)/sqrt(J)`即达到该范数；J为零时结论平凡。其余输出的存在只能增大完整直和范数。证毕。

原W2C合同的K是完整有限接收器 `P_f H_c iota_B` 的上界，故准确的链为 `K>=||P_f H_c iota_B||>=sqrt(J)`。这里没有从一个已投影上界反推它也支配未投影的连续Hc；(C.9)给两个对象分别同样的必要下界。这与先前对**所选正上界配方数**取下端点不同：(C.9)是真实算子范数下界。但它仍不是实际方算子奇异性的结论；`I-Hc` 完全可能可逆，直接Green预处理正是为处理这种情况。

## 5. 一个全域向下证书即可判断旧配方

保原155个完整比较panel，真实长度为 `h_i>0`，参考q在每panel为原固定正值。在整个panel上取得signed区间 `A_i` 包围实际(C.5)，并令

\[
\ell_i=\max\{0,\operatorname{lower}(A_i),-\operatorname{upper}(A_i)\},
\quad h_i^-\le h_i,\quad q_i^+\ge q_i>0.
\tag{C.10}
\]

有 `|a00(r)|>=ell_i`，即使 `A_i` 跨零也只是给出ell_i=0，不产生假的正下界。因此

\[
J\ge J_-:=\sum_i h_i^-\frac{\ell_i^2}{(q_i^+)^2}.
\tag{C.11}
\]

全部乘积和最后求和必须向下包围。消费者保存的是一个包含此完整下界数的原球，后续只取该保存球的下端点；最终只在该下端点不小于精确 `1/16384` 时宣告排除。不能用保存球的中心或上端点完成这个比较。

所有155panel都需完成。真根panel的长度从原真实根enclosure取得，不能换成其midpoint；同参考q的有向上端点必须正。原153parent、4650行/4801交段及全部signed/mean资格先完整admission。尚未完整的panel前缀不是全域目标的成功。

**推论3。** 若公开有向计算给出(C.11)的完整保存下端点满足

\[
J_-\ge\frac1{16384},
\]

则每个合法W2C完整中心上界都满足 `K>=1/128`。R139的完整旧配方因此满足

\[
\mathcal G\ge\frac{30793}{30720}>1.
\tag{C.12}
\]

这排除的是同固定WVC参考、同原误差预算的**小中心范数配方**，无需再为它计算余47条。它不排除更换参考、直接认证完整中心逆或用另一套完整预处理；也不证明实际算子有核。

若下界不足阈值，只记录未能排除，不能反推J或K很小。一次成功全域下界目标此后冻结；未通过必要门也不能将它作为未完成目标重算。

本篇给一个全域平方lower目标及其严格必要比较，不重新求L三量、独立mean-atom三下界、endpoint浮点诊断或任何旧成功范数。原真实高反馈在其他输入上、finite投影/rho、七ports、两RHS及课题全部最终完成标准继续保留。
