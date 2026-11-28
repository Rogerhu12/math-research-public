# R133 JWS：联合 Wiener 界给出的完整角向逆收缩

2026-11-28，visible-exact-astra-b0d5a16-20261128。

**已证明。** 在原修补实族、原整个 strict 区间上，同一个完整角向逆满足

\[
\boxed{\quad
\|J\|_{L^2_{\mathrm{even},0}\to L^2_{\mathrm{odd}}}<\frac75,
\qquad
\|J\|_{L^2_{\mathrm{even},0}\to H^1_{\mathrm{odd}}}<\frac{29}5.
\quad}                                                   \tag{JWS.1}
\]

原标量分母同时有新的完整下界 $D_J>3/8$。这不是另选一个有限矩阵逆；
所有物理频率、完整乘子、原 primitive 与均值关系都留在同一算子里。
关键是使用已存**两个分量的联合** Wiener 界，先控制乘积，再取算子范数。
将联合界分别松给两个分量，会丢掉本次收缩。

## 1. 同一对象、原整件及唯一输入

保持 [JI](R133-supplement-complete-real-interval-angular-inverse-and-physical-mean.md)
的完整定义：$Q^\delta=(u,v)=\bar Q+\delta Z$，$|\delta|\le10^{-8}$，
固定 intrinsic $\eta_0$，原连续修补与全部真实接缝，

\[
0\le r\le r_c=\frac{76285779072683}{320000000000000},\qquad
\eta=-\gamma\Pi v,\quad \beta=a_{\rm phys}'/a_{\rm phys},\quad
P=1-\Pi,\quad I=\partial_\phi^{-1}P.                       \tag{JWS.2}
\]

角测度归一，周期 $\pi/2$，频率为 $4j$。$u$ 为奇函数，$v$ 为偶函数；
$\eta$ 是上式的 characteristic scalar，不是固定 intrinsic 参数。
原方程未假定 nonlinear residual 为零。

本次只消费 SJ run **43768006977/1** 的完整成功 execution：

`notes/strict_radial_first_symbol_defect_ci/run-43768006977-1/execution.json`，
46318 bytes，SHA256
`2540a3a81f1b6cd83c24b6a1c9ad2bdc119fb04a9a37c0251f6157a3cbc7cb88`。

其完整内嵌 actual 已成功，原26 gates 全过。原 JI 全文11769 bytes，SHA256
`01e4a33be5d895ccbfc949310a86bf561c8dccdfe1c1eff973fa1298fcc91cf1`。
同一 actual 的 `mathematical_parameters` 给出原联合 Fourier $A_0$ 范数

\[
U+V\le S=7+19\,10^{-8},\qquad
U_1+V_1\le D=6+83\,10^{-8},                              \tag{JWS.3}
\]

其中 $U=\|u\|_{A_0}$、$V=\|v\|_{A_0}$、
$U_1=\|u_\phi\|_{A_0}$、$V_1=\|v_\phi\|_{A_0}$。
这些都是完整分量和，包含原物理 scalar、修补值及实际 $v$ 的均值；
不是某个 Fourier 节的范数。

原整球是

\[
|\beta|\le[0.2105543925434142493523470516159096075630292956
             \mathbin{+/-}3.42\,10^{-47}],
\]
\[
\eta\ge[1.108659019086831048943366795356268994510173798
             \mathbin{+/-}3.93\,10^{-46}],
\]

这里 upper 使用第一球上端，lower 使用第二球下端。因此可取

\[
b=\frac{1053}{5000}>|\beta|,\qquad
e=\frac{5543}{5000}<\eta,\qquad |2\beta/\eta|<2/5.        \tag{JWS.4}
\]

只读取原球，不重算 SJ、原修补多项式、任何 ODE 或旧 JI/WEJ 目标。

## 2. 完整余算子的联合界

原完整算子是

\[
A=\eta\partial_\phi+L,\qquad
L=-2\beta P M_{uv}P-2\beta P M_{v_\phi}IM_uP.             \tag{JWS.5}
\]

所有因子顺序不变。$P$ 在 $L^2$ 上为收缩，$I$ 的同阶范数是 $1/4$；
各完整乘子的 $L^2$ 范数不超过其 $A_0$ 范数。奇性给 $U\le U_1/4\le D/4$。
由于 $D/4<S/2$，函数 $x(S-x)$ 在此区间递增，所以

\[
UV\le U(S-U)\le\frac D4\left(S-\frac D4\right),\qquad
UV_1\le\frac{U_1V_1}{4}\le\frac{D^2}{16}.               \tag{JWS.6}
\]

两个上界可以相加；无需断言它们的最大值在同一点实现。于是

\[
\boxed{\quad
\|L\|_{L^2\to L^2}
\le2|\beta|\left(UV+\frac{UV_1}{4}\right)
<L_*:=2b\left(\frac{DS}{4}-\frac{3D^2}{64}\right)
<3.711826.
\quad}                                                  \tag{JWS.7}
\]

这里的 $I M_u$ 作用于完整未知函数，未作任何频率截断。
独立均值在反射实现里按原投影处理，$v$ 的真实均值没有从乘积中删掉。

## 3. 全频 Neumann 逆及同一 realization

在原奇 $L^2$ 空间令 $P_0=\eta^{-1}I$。它把偶 mean-zero 输入送到奇空间，
且 $P_0\eta\partial$ 在奇空间为 identity。完整新有理比较给

\[
\|P_0L\|\le\frac{L_*}{4e}<\frac{21}{25}<1,\qquad
4e-L_*>\frac57.                                         \tag{JWS.8}
\]

因此

\[
J=(1+P_0L)^{-1}P_0,
\qquad
\|J\|_{L^2\to L^2}
\le\frac1{4\eta-\|L\|}<\frac1{4e-L_*}<\frac75.            \tag{JWS.9}
\]

这是整个 Hilbert 空间的收缩，不是有限 determinant。解的分布方程
$\eta\partial h=f-Lh$ 给 $h\in H^1$，随后 $Ah=f$。
奇性消掉唯一可能的积分常数，齐次方程同样给唯一性。因此它与 JI.11 的
双侧逆是**同一个** $J$，而不是为负窗另选的逆。

由同一方程可直接给导数，不将 $J$ 与导数交换：

\[
\|\partial J\|_{L^2\to L^2}
\le e^{-1}(1+L_*\,7/5)<28/5.                            \tag{JWS.10}
\]

原物理 Bessel 范数满足
$\|h\|_{H^1}^2=\|h\|_2^2+\|\partial_\phi h\|_2^2$，且
$(7/5)^2+(28/5)^2=833/25<841/25=(29/5)^2$，证明 JWS.1。
同一 $L^2$ inverse norm 也适用于其准确 reflected adjoint；没有因此
声明无关的 full signed-circle realization 已逆。

## 4. 原均值分母与积分因子也保联合相关

保持 JI.5 的 $\alpha=2\beta/\eta$、
$a_J=\exp\{-\alpha I(uv)\}$、
$D_J=\Pi[a_J(1-\alpha uIv)]$。不把 $a_J$ 与物理半径混同。
用 $S<57/8,D<49/8$，得

\[
\|\alpha I(uv)\|_{A_0}
\le\frac{2/5}{4}\frac{49}{32}
                  \left(\frac{57}{8}-\frac{49}{32}\right)
=\frac{8771}{10240}<\frac78.                             \tag{JWS.11}
\]

$A_0$ 为完整 Banach 代数。指数幂级数因此给
$\|a_J\|_{A_0},\|a_J^{-1}\|_{A_0}\le e^{7/8}<5/2$，实点另有
$a_J>2/5$。这项指数比较可纯有理证明：设 $x=7/8$，从第四项起相邻比
不超过 $x/5=7/40$，故

\[
e^x\le1+x+x^2/2+x^3/6+\frac{x^4}{24(1-x/5)}<5/2.         \tag{JWS.12}
\]

由于 $Iv=I^2v_\phi$，联合一阶和进一步给

\[
|\alpha|\|u\|_\infty\|Iv\|_\infty
\le\frac25\frac{U_1V_1}{64}
\le\frac25\frac{(49/8)^2}{256}
=\frac{2401}{40960}<\frac1{16}.                           \tag{JWS.13}
\]

这是两个导数之和的乘积界，而不是分别取 $7$ 后再乘。因此原完整标量分母满足

\[
\boxed{\quad D_J>\frac25\frac{15}{16}=\frac38.\quad}     \tag{JWS.14}
\]

JI.11 的 $c=\Pi(uh)$ 仍在精确解公式中；它也不等于物理状态的独立 even mean
$z$。原 $z$ 方程、两物理密度 mean、ordinary source、接缝及外端口均未消掉。

## 5. 后继可用的常数与边界

| 同一整个 strict 区间上的完整对象 | 新有理界 |
|---|---:|
| $L:L^2\to L^2$ | $1855913/500000$ |
| $P_0L:L^2_{\rm odd}\to L^2_{\rm odd}$ | $21/25$ |
| $J:L^2_{\rm even,0}\to L^2_{\rm odd}$ | $7/5$ |
| $\partial J:L^2_{\rm even,0}\to L^2_{\rm even,0}$ | $28/5$ |
| $J:L^2_{\rm even,0}\to H^1_{\rm odd}$ | $29/5$ |
| $D_J$ 的实正下界 | $3/8$ |
| $a_J$ 与 $a_J^{-1}$ 的完整 $A_0$ 上界 | $5/2$ |

新 signed global G.7/G.12–14 消费者可使用这里的 $J_0,L_0,D_J$。
要得到 $H^{-8/3}\to H^{-5/3}$、$H^{-5/3}\to H^{-2/3}$ 等窗，仍须其对应
完整 multiplier bounds 和原有序有限逆恒等式；不能把 $7/5$ 直接贴到那些窗。
旧 root inverse 的独立同域球继续有效，不能把本 strict 区间延长到未读的 root collar。
全部旧 JI/WEJ 候选和失败记录保留。本篇不证明正侧 BVP、incoming inverse、
有限 Schur、exact core 或最终闭等距族。

新脚本 `scripts/fourfold_codazzi_joint_wiener_angular_inverse_saved_bounds.py`
只读上述两个完整原件，用 `fractions.Fraction` 验证本篇15项新有理比较。
不导入旧 producer、不恢复旧数组、不重跑旧科学目标。输出只作临时复核记录，
按根规则15保留源码、参数、字节数及 SHA，不提交可重算数据。

本会话首次执行上述新有理消费者，15项全部通过；原科学目标与载体恢复均为0。
完整临时输出3674 bytes，SHA256
`19843e50c6fe867b5039390fba68051152085974dc2e23779f41f8e56bc21d00`；
源码 SHA256 `87529ece471ea43c0f8530afbc8a8276b156d0d3be43c4eea79fadfe367288a8`。
命令参数为 `--repo . --output <temporary-file>`，输出已存在时拒绝覆盖；
后继读取本篇已证有理常数，不要求为每次使用重跑这15项。
