# R601 — 同一实际有限残差与完整解析投影的 world 角导数界

作者：ChatGPT /root（AI）。日期：2026-11-16。

**可信度：已证明的条件估计及完整源码组件；尚未执行本组件，没有取得实际数值界或新的接受场。** 本文新增的是 R580 完整解析投影误差的物理角一阶导数，以及它与 R596 实际完整系数残差的同对象组合。R514 已证明的角长输运与相对 Gram 估计、R519 已接入的同次六 jet 局部诊断直接引用，不重新编号为新定理。原 BVP、native、FD、fullDN、metric DFS、最后审计和所有接受门均不改变。

## 601.1　真实对象和所补的一项

已刊 [R580](R580-complete-complex-angle-strip-and-exponential-tail-alias.md) 从原 R553 同一次完整系数 tube、准确 scalar 和联合正域返回中构造真实复角带，并对连续 Fourier 尾与原有限 DFT 的所有整数 alias 给完整 C0 上界。它不支付真实 saved-RHS 与该准确有限参考之间的形成差。

已刊 [R596](R596-actual-saved-RHS-and-complete-finite-DFT-defect.md) 绑定真实 checkpoint 的全部 Y/DY/U/DU、十准确参数、原 scalar、原 deadline 和全部系数，针对全部 N 个准确角及 3M+2 行形成闭单元上的完整有限参考残差。它不是用原有限 RMS 数字直接命名一个连续误差，也不把 DY 与 DU 强行逐词相等。

两者合起来可以控制当前准确前缀场的速度缺陷。但 [R514](R514-complete-field-defect-transport-and-literal-residual-transfer.md) 的另一条角长估计需要该缺陷的物理角导数。本文补这一项，并明确旋转框架产生的连接项。不能把旋转分量的导数直接当成 Cartesian world 导数；遗漏该项会在径向 mean 上已经出错。

本组件只用已经存在的完整解析带、实际有限残差与原有理平方根；不重扫物理角，不重做 FFT/DFT，不对 field 或准确 target 作第二次查询，不引入新的分格、clock、线程或原始数组。

## 601.2　固定坐标、系数和有限投影

固定同一个允许准确 C 成员、同一实际十参数、同一准确未修补 prefix quintic Q，以及原数值径向坐标 s。物理角为 phi，单位是弧度。它不同于 q=phi/(2*pi)，也不同于后来拉回的共同材料角。

实际 layout 是

$
Q=(r_0,\ldots,r_M,t_1,\ldots,t_M,z_0,\ldots,z_M),
\qquad n=3M+2.
$

令 E(phi) 是实角下从柱坐标旋转分量到 Cartesian 的正交框架，令 S_M 表示含 E 的完整系数合成。原旋转分量分别为

$
R=r_0+\sum_{j=1}^M r_j\cos(2j\phi),\quad
T=\sum_{j=1}^M t_j\sin(2j\phi),\quad
Z=z_0+\sum_{j=1}^M z_j\cos(2j\phi).
$

于是 X=S_M Q=E(R,T,Z)。原两 mean 均在状态中，t mean 仅由已声明的奇对称为零，不是读回时删去的行。

准确目标沿这一数值坐标为

$
g=\mu^2 ds^2+A(s)^2\rho(\phi)^2d\phi^2,\qquad
\nu=A_s.
$

在实际 prefix 来源里，mu=Ltrue/Lnumeric，nu=mu*a_true,s；不能把 numeric profile 的 ap 换成它。R596 与 R580 通过**同一个实际 R575 对象**使用同一组 A,nu,mu；这既不是两个有相同文件名的对象，也不是两个后来用 SHA 配对的不同场。

令 V_+(X;A,nu,mu) 为原正平方根的准确 Frenet 速度，旋转分量记为 v。R580 的完整解析带与向量范数对固定分支成立；R596 实际有限参考的 sigma=+1 已由原 BatchedFFTFlow 正平方根来源绑定。这个标记不识别 native DtN worker 的 root 分支；反射和径向反向还需真实分支变换。

令 F_N(s,Q) 为 R596 全 N 点、全部保留行的准确有限 DFT 参考；Pi_{M,N} v 是它在旋转分量中的完整重构。N 为原偶数且 N>=4M+4，保留 signed frequency 集合为 {-2M,-2M+2,...,2M}，没有保留 Nyquist。有限参考满足

$
S_M F_N=E\,\Pi_{M,N}v.
$

这是两件已刊组件绑定的同一数学参考，不是原 floating FFT 执行的逐字复制。

## 601.3　完整 Fourier 尾的导数

R580 已完整付出一个全原 prefix 共用的带宽 h>0 与复三向量范数上界 C>=0，使同一 v 在 |Im(phi)|<=h 上解析并满足 ||v||<=C。组件已承担所有原终叶、准确族与整角覆盖；若只付一个局部角盒或若干点，下文不能全域使用。

写

$
v(\phi)=\sum_{j\in\mathbb Z}\widehat v_{2j}e^{2ij\phi}.
$

由同一闭带的 Cauchy 移线，或先在 h'<h 移线再取极限，

$
\|\widehat v_{2j}\|\le C e^{-2|j|h}.
$

这是复三向量的 Euclidean/Hermitian 范数，不能再乘一个未经需要的3。带宽正保证一阶加权级数也绝对一致收敛，所以可以逐项微分。

令 r0=e^{-2h}。完整被截尾的旋转导数满足

$
T_1^{\rm exact}
=4C\sum_{j=M+1}^{\infty}j r_0^j.
$

两边 signed frequencies 给系数2，角微分给频率2j，合为4。由完整几何级数逐项微分，准确有

$
\sum_{j=M+1}^{\infty}j r^j
=r^{M+1}\left(\frac{M+1}{1-r}+\frac{r}{(1-r)^2}\right).
$

因此，只要 r0<=r<1，

$
\boxed{\quad
T_1=4C r^{M+1}
\left(\frac{M+1}{1-r}+\frac{r}{(1-r)^2}\right)
\quad}
\tag{601.1}
$

是整个无限导数尾的上界。每个级数项对 r 非减，故把 r0 换为 r 只增大上界；没有舍弃未算尾。

原 R580 的同一个准确有理数为

$
r=\left[\sum_{k=0}^{L}\frac{(2h)^k}{k!}\right]^{-1},\qquad L\ge1.
$

完整正项和小于等于 exp(2h) 且严格大于1，所以 r0<=r<1。R601 直接消费原 R580 已形成的 r、1-r 和 r^{M+1} 的完整外包，不重算该 Taylor 和，不引入一个不同的 r 或猜测一个常数。

## 601.4　全部 alias 的导数与真正 world 连接项

令 A_alias 是 R580 已完整包含全部保留 signed bins、每个非零整数 alias 的旋转重构范数和上界。原组件给

$
A_{\rm alias}
\le\min\left(
\frac{2C r^{N/2-M} S_{2M+1}(r)}
{(1-r)S_{N/2}(r)},\
\frac{2C r^{M+1}}{1-r}
\right),
\quad S_n(r)=\sum_{j=0}^{n-1}r^j,
$

实际返回的是经过原向外舍入的 alias_upper_used。此处直接用那个真实返回值，不重新比较未返表达式或从小数显示截断。

每个重构的保留频率绝对值不超过2M。故对**已经重构的 alias 多项式**逐项微分，其范数不超过 2M*A_alias。这里乘的是保留 bin 的频率。高频原 Fourier 项的真实导数已在完整 T1 中；不能把 alias 的原高频当成重构频率，也不能凭固定网格声称投影与微分、任意相移全都交换。

设 w_rot=v-Pi_{M,N}v。若 D0 是 R580 的真实完整 C0 投影差，则

$
\|w_{\rm rot}\|\le D_0,\qquad
\|\partial_\phi w_{\rm rot}\|\le T_1+2M A_{\rm alias}.
\tag{601.2}
$

Cartesian world 差为 w=E w_rot。对实角，

$
E'=EJ,\qquad J(a,b,c)=(-b,a,0),\qquad \|J\|_{\rm op}=1.
$

因此

$
w_\phi=E(w_{{\rm rot},\phi}+Jw_{\rm rot})
$

并得到

$
\boxed{\quad
\|w_\phi\|
\le D_1:=T_1+2M A_{\rm alias}+D_0.
\quad}
\tag{601.3}
$

E 只在**实角**被用为正交框架。没有把复 E 当成 unitary，也没有把旋转分量的复带上界偷换成另一个复 Cartesian 范数。

例子只需准确符号即可看出连接项必要：若旋转误差为常向量 (a,0,0)，其旋转分量导数为零，但 world 误差为 a*e_r(phi)，导数范数仍是 |a|。这也是不能在角导数责任里删掉 r0 的原因。

## 601.5　完整系数残差的 world C1 权

设实际完整系数残差为

$
e=Q'-F_N(s,Q),\qquad
\|e\|_\infty\le\eta_Q.
$

这个 eta_Q 是 R596 对全部原终叶、整个径向闭单元和全部物理行付出的真实上界；不能用原 RMS、一个节点残差或某个旧 run 的 max 替代。

已有 R596 完整 C0 合成常数是

$
C_{0,M}=\sqrt{2(M+1)^2+M^2}.
$

world 角导数在旋转框架中准确为

$
\begin{aligned}
(\partial_\phi S_M e)_r
&=-\sum_{j=1}^{M}(2j e_{r,j}+e_{t,j})\sin(2j\phi),\\
(\partial_\phi S_M e)_t
&=e_{r,0}+\sum_{j=1}^{M}(2j e_{t,j}+e_{r,j})\cos(2j\phi),\\
(\partial_\phi S_M e)_z
&=-\sum_{j=1}^{M}2j e_{z,j}\sin(2j\phi).
\end{aligned}
\tag{601.4}
$

用完整三角权逐分量外包，三条权分别是

$
M(M+2),\qquad (M+1)^2,\qquad M(M+1).
$

第二条多出的1来自真实径向 mean。垂直 mean 仍保留在完整状态和 C0 中，只是它的 phi 导数准确为零。因此

$
\boxed{\quad
\|\partial_\phi S_Me\|
\le C_{1,M}\eta_Q,\qquad
C_{1,M}=
\sqrt{[M(M+2)]^2+[(M+1)^2]^2+[M(M+1)]^2}.
\quad}
\tag{601.5}
$

该系数范数是一个合法的保守上界，不声称达到精确算子范数。原所有3M+2行和两mean都保留；没有换成只控制一个 height block 的常数。

## 601.6　同一个实际场的 C0/C1 缺陷

在同一坐标和同一准确目标下，定义

$
r=X_s-V_+(X).
$

实际有限重构给恒等式

$
r=S_M[Q'-F_N(s,Q)]+\{S_MF_N(s,Q)-V_+(X)\}.
$

对 s 不依赖的原合成框架逐 phi 微分，并应用601.3、601.5，可得

$
\boxed{
\begin{aligned}
\|r\|&\le C_{0,M}\eta_Q+D_0=:E_0,\\
\|r_\phi\|&\le C_{1,M}\eta_Q+D_1=:E_1.
\end{aligned}}
\tag{601.6}
$

源码的第一项直接沿用 R596 实际已返回的 global_reconstructed_finite_ODE_residual_upper；它可能包含原平方根外包，因此不把它降回理想实数常数的未舍入值。C1 则通过实际已绑定 R521 的有理平方根上端点形成。

R596 的 eta_Q 是当前准确 Q 对同一准确有限参考的完整差额。它已经包含保存字词、实际 scalar/长度/数值影子相对于该参考的**总差额**，但不隔离内部 FFT/三角表/编译库每次舍入。601.6 不把那些未隔离成分补成零，也不重复把同一总差额加两遍。R596 对 literal cubic、DY/DU 不同、各节点形成差的独立责任仍原样保留；601.6 本身不额外要求 literal cubic 必须成功，亦不把所有节点形成摘要变成新门。

## 601.7　如何接到已证 R514，而不重造六 jet 门

R514 的同一目标、同一合法分支给

$
\tau=\partial_s\frac{|X_\phi|}{A\rho}
=\frac{X_\phi\cdot r_\phi}{A\rho|X_\phi|},
\qquad
|\tau|\le\frac{|r_\phi|}{A\rho}.
$

故若实际整块已经另付 A>=A_->0、rho>=rho_->0，

$
|\tau|\le\frac{E_1}{A_-\rho_-}.
\tag{601.7}
$

这直接复用 R514(514.8)。再有真实 BC/cuff 锚和完整径向路径积分，便沿原514.9–514.11控制角长与相对 Gram。**本组件不接受调用者填写的 A_-、rho_-、锚或路径常数，也没有实际形成它们。** 因此当前返回不能称为已经取得闭面 metric floor，不能把原1e-6、1e-11或2e-9阈值直接代入601.7。

R519 已经用同次六 jet直接形成局部 h、tau、两个 V_sigma 和条件 Gram 界；其路径完全可以独立继续。R601 不要求 R519 为它加第三阶角导数，也不要求 R575 的 B2 诊断先成功。解析带给601.1所需的角可微性；缺带时这里只报告未付，不改变已有直接六 jet或R459 Gram包围。

前缀的真实 rho、原 BC 准确字与模式权、径向积分、cut patch/collar/native/两帽及全t责任仍由各自完整来源付清。本组件不把未修补前缀的缺陷不加差项地继承给最终 patched 场。

## 601.8　物理角、材料拉回、反射与原网格

若 phi=Theta(q)，Theta_q=kappa>0，且 Theta 与径向坐标无关，则已经建立的 world 缺陷满足

$
(r\circ\Theta)_q=\kappa(r_\phi\circ\Theta).
$

因此只能用实际全域 kappa 上界转换 E1；q=phi/(2*pi) 时因子准确是2*pi，不能漏掉。目标密度也同时变换为 rho*Theta_q；在601.7的比值中可以按实际同一点关系消去该正因子，而不能把不同盒端点任意配对成一个新更窄界。

若再改径向坐标 s=s(u)，则 r_u=s_u r，角导数也乘 s_u；mu、A_u和径向积分长度必须同步变换。固定刚性旋转或反射只在真实坐标和 sigma=epsilon*det(J)*sigma 的分支合同下传递；不能以“范数不变”省掉参考速度分支。

这些是已建立误差的拉回，不声称有限N个物理点重新投影后与任意材料相移交换。R601不会在新角点重新做一个DFT，也不会用原base的alias常数证明另一套未绑定网格。

## 601.9　向外形成，不在 r_upper=1 时伪造失败

原 R580 的同一 r 给正下界 g_lo<=1-r、r<=r_hi<=1及 p_hi>=r^{M+1}。有限工作精度可能有 r_hi=1，尽管准确 r<1。R601 保留原独立正 gap，而不用1-r_hi作为分母，也不把这个舍入现象变成新的域失败。

源码形成

$
4C\,p_{\rm hi}
\left(\frac{M+1}{g_{\rm lo}}+
\frac{r_{\rm hi}}{g_{\rm lo}^2}\right),
$

其每个输入方向都给601.1的上界。全为非负项，避免用 (M+1)-M*r 的差消去再不当地混用相关端点。之后每次 relative_dyadic_bounds 只取上端点。alias导数、world连接项、系数C1、最终E0/E1均包含这些实际向外舍入；没有将尾项截断或把小正数underflow为零。

若预算在任何一步停止，原 ResourceStop/RuntimeError 与 MemoryError 原样向原调用者传播，保实际 unfinished operation。没有独立计时、额外重试、扩大budget或忽略未知后缀。向外算术会消耗原预算，不承诺同一资源内完成与旧运行相同的cell数量。

## 601.10　实际源码所有权与完整结束调用

交付源码为
[geometry_20261116_actual_analytic_saved_RHS_C1_defect.py](../computations/geometry_20261116_actual_analytic_saved_RHS_C1_defect.py)。

绑定入口只接收两个**已经真实加载的对象**：

- BoundAnalyticProjection，固定R580源35149B/0abe4629415a0e9219a50cf248f30bdceb9819b4338189b811101bdadf3d543f；
- BoundSavedRHSDefect，固定R596源56627B/8a242686845844df64d248b7b9fd47096ff2c7a8c2044346c85fc9b7425afb3f。

代码通过实际类定义module、__file__、完整源SHA、basename、目录及class identity检查，不搜索同名便利模块。两个对象的R575必须是同一Python对象，field/current/tubes/api/M/N/precision和实际budget callback亦相同。R575已经绑定R553/R521和原全部DFT来源；R596另保真实完整数组及clock。

R601拥有这两个对象的**原结束调用位置**，不是在两者已经各自finish之后再调用一遍：

1. 用原真实coverage、完整ledger、error/stop/close_errors调用actual R580.summary；
2. 调用actual R596.summary，不传另一个R575组成对象，避免另算一次投影组合；
3. 两者的全域标志与原退休计数均真实完整时，才形成601.6；
4. 将两份原summary完整保留在自己的necessary对象中，不删未知键、unpaid、错误、scope、来源或未访责任。

它不接受外部h/C/eta/summary来冒实际常数。不用只相同hash代替活对象一致性，也不以一个祖先完整计数替另一条未完成序列。

第二次结束调用只允许带原实际error/stop/close error的恢复分支；原R580完整条件在此为false，故只有元数据，不重算解析全局界。R601的新C1形成也不重试。若曾有先前已完成值，恢复只把它保为明确的历史值，当前complete仍false；不能在后来的错误下保留旧global成功标签。

## 601.11　完整覆盖和诚实未付

组合要求原 completed_all_DFS_work=true、完整ledger真实存在、原error/stop/close_errors为空、R580全部解析终叶和R596全部Q残差终叶付清，且两条observed/committed/split/terminal计数与同一个R553一致。每个原终叶都完成之后，才可对有限闭覆盖取原极值，得到全prefix E0/E1。

只有局部成功、粗父覆盖但未清退休责任、某个尚在计算的DFT和、非零unvisited stack或未返ledger均不被解释成已取得全域组合。原R580/R596的详细错误及原coverage各自保留，R601新增的formation_error也独立记录。来源/完整性检查失败仅表示本可选诊断未付，不把它升级为原场的数学拒绝。

本组件没有改necessary单体90000/70，没有新增raw文件或把数组编码进Git。完整原summary可能使未来必要对象仍然过大；新caller必须在其实际整个选定对象上保原完整语义和原上限。本组件不承诺fits，不拿source identity恢复未返正文，也不把文件身份叫全ledger逐行读完。

## 601.12　已付与下一真实调用

已付的是601.1–601.6的完整估计、world连接与mean责任、同坐标R514接点，以及具实际对象约束、原预算和原结束调用所有权的完整source。没有执行本库、没有本地数值求值/import/AST/compile/fixture，没有新的run或数值常数。

后继须在其真实完整source闭包中登记本源，并在同一个R575上创建R580和R596，再将两份原结束调用交给本组件。原R580.inspect/retire、R596.cell/retire和原DFS分裂仍照原顺序；本组件不替代它们。实际caller、necessary、完整source身份与正式run必须独立公开，不能只添加一个source表项就称已使用。

本题仍须真实取得接受的非零完整112/338/450、同一固定g的闭C2族、reach/held/反射距离、准确全域metric和同目标实际精化证据。本文既不宣布这些已完成，也不把本可选较强误差路线变成README的新前门。
