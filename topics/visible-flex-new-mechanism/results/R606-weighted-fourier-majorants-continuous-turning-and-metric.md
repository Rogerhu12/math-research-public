# R606：完整高度的加权 Fourier 主控、连续 turning 根与真实 metric 传播

日期：2026-11-26。**已证明：对下述明确的有限系数高度表示，六个真实 jets 的连续角主控、有限角平均/系数的 alias 界、连续 turning 根的显式包围，以及由此到实际重构 metric 的误差界。** 本文没有执行科学计算，没有把当前任何径向采样、浮点 ODE、有限 DtN 口或一次优化输出认证为连续精确输入，也没有声称精确等距族、reach 或课题完成。

这不是重复 R594 中“如果知道高角导数界”的条件式：以下常数直接由当前 **tanh 前有限三角多项式、线性高模、R602 核心修正的有限径向系数** 构造；同时支付离散 turning 根与连续根的差。R594 的实际重构恒等最后才用于传播。

## 1. 准确对象、两种固定均值与量词

令 $I\subset(0,R)$ 为径向区间。首先每个陈述都可在一个固定 $r\in I$ 使用。要得到整个 $I$ 的结论，本文列出的系数界和不等式必须对 **每个 $r\in I$** 成立；后面给出只需径向二 jets 的区间实现方式。

取实值、偶、$\pi$ 周期的有限三角多项式

$$
v(r,\theta)=\sum_{m\in\mathcal V}v_m(r)\cos(m\theta),\qquad
L(r,\theta)=\sum_{m\in\mathcal L}L_m(r)\cos(m\theta),               \tag{1}
$$

其中 $\mathcal V,\mathcal L$ 为有限正偶数集合，所有系数在 $r$ 上为真正 $C^2$ 函数。当前11模表示的旧项取 $\mathcal V=\{2,4,6,8\}$；$\mathcal L$ 包含后置受迫4模、新增线性模和 R602 的最高44模。有限 DtN/ODE 输出若只近似这些函数，必须另外包围其误差，不能把近似 jets 直接当成(1)的准确 jets。

固定 $\sigma>0$，定义 $g=\sigma\tanh(v/\sigma)$。选定且始终保持以下一种角常数算子：

$$
Q g=\langle g\rangle
\quad\hbox{或}\quad
Q g=T_{N_0}g:=\frac1{N_0}\sum_{\ell=0}^{N_0-1}
 g(2\pi\ell/N_0),                                               \tag{2}
$$

其中 $N_0$ 是固定整数，与后续观测角网无关。本文当前实现取 $N_0=512$。完整高度为

$$
Z=h+f,\qquad h'=-W,\qquad f=(1-Q)g+L.                            \tag{3}
$$

因为(2)的节点、权重不随 $r$ 变化，$Q$ 与两个径向导数交换。因此 $f,f_r,f_{rr}$ 必须减去同一均值函数及其一、二阶导数；$f_\theta,f_{\theta\theta},f_{r\theta}$ 不受角常数影响。这样(3)定义的是一张与观测角网无关的真实高度。

有限 $Q=T_{N_0}$ 不必等于连续平均；这不会破坏 R576 的 turning/重构恒等。只要使用(3)的完整实际 jets，角常数仍是同一真实高度的一部分。不能同时把 $W$ 称为(3)的准确连续径向均值，除非另已支付这一差异。

## 2. 一个可直接计算的 Fourier 代数

对 $2\pi$ 周期函数定义

$$
\|a\|_\rho=\sum_{n\in\mathbb Z}|\widehat a_n|e^{|n|\rho},
\qquad \rho>0.                                                  \tag{4}
$$

此范数控制完整实轴 $L^\infty$ 范数，并有

$$
\|ab\|_\rho\le\|a\|_\rho\|b\|_\rho.                              \tag{5}
$$

证明是 Fourier 卷积与 $|n+k|\le |n|+|k|$。对有限实余弦多项式，

$$
\left\|\sum_{m>0}c_m\cos(m\theta)\right\|_\rho
=\sum_{m>0}|c_m|e^{m\rho},                                      \tag{6}
$$

正弦式相同。因此当前有限径向系数直接给出

$$
V_0=\|v\|_\rho,\ V_1=\|v_r\|_\rho,\ V_2=\|v_{rr}\|_\rho,\quad
V_t=\|v_\theta\|_\rho,\ V_{tt}=\|v_{\theta\theta}\|_\rho,\
V_{rt}=\|v_{r\theta}\|_\rho.                                    \tag{7}
$$

它们都是有限加法，不是从 FFT 尾差推测出的连续范数。

设 $a$ 偶且 $\pi$ 周期，$a=a_0+\sum_{j\ge1}a_j\cos(2j\theta)$。由(4)直接有

$$
\left\|\sum_{j>J}a_j\cos(2j\theta)\right\|_\infty
\le e^{-2(J+1)\rho}\|a\|_\rho.                                 \tag{8}
$$

这里不需额外几何级数因子：权重已经对整个 Fourier 系列求和。

令 $N$ 为偶数。直接对单个指数函数求和可得

$$
T_N a=\sum_{k\in\mathbb Z}\widehat a_{kN}.
$$

故

$$
|T_Na-\langle a\rangle|\le e^{-N\rho}\|a\|_\rho.                 \tag{9}
$$

若 $0<n<N/2$，离散余弦系数 $a_n^{[N]}=2T_N(a\cos n\theta)$ 的非主项索引分别属于 $n+kN$ 和 $-n+kN$，两集合互不相交，且非主项的绝对频率至少 $N-n$。于是

$$
|a_n^{[N]}-2\langle a\cos n\theta\rangle|
\le e^{-(N-n)\rho}\|a\|_\rho.                                  \tag{10}
$$

(9)(10)是准确 Fourier 恒等的绝对值估计；数值三角函数、求和、函数值舍入误差仍须加在右边。

## 3. tanh 项的完整六 jets

假设

$$
t_0:=V_0/\sigma<\pi/2,\qquad
A=\sec^2t_0,\qquad B=2\tan t_0\,\sec^2t_0/\sigma.                \tag{11}
$$

$\tan z$ 的奇次幂系数全为正：由 $T'=1+T^2,T(0)=0$ 的系数递推即可见；其收敛半径是 $\pi/2$。$\tanh z=-i\tan(iz)$，所以各项绝对值的主控为 $\tan t$。逐项微分并用(5)，得到

$$
\|\sigma\tanh(v/\sigma)\|_\rho\le \sigma\tan t_0,\quad
\|\operatorname{sech}^2(v/\sigma)\|_\rho\le A,
$$

$$
\left\|-\frac2\sigma\tanh(v/\sigma)
                 \operatorname{sech}^2(v/\sigma)\right\|_\rho\le B. \tag{12}
$$

将通常链式法则完整写出，未去均值六 jets 的界为

$$
U_0=\sigma\tan t_0,\quad U_r=AV_1,\quad
U_{rr}=AV_2+BV_1^2,
$$

$$
U_t=AV_t,\quad U_{tt}=AV_{tt}+BV_t^2,\quad
U_{rt}=AV_{rt}+BV_1V_t.                                        \tag{13}
$$

连续平均投影 $1-\langle\cdot\rangle$ 只删除零频系数，故不增(4)范数。若用固定有限均值 $T_{N_0}$，由(9)，

$$
\|(1-T_{N_0})a\|_\rho
\le(1+e^{-N_0\rho})\|a\|_\rho.                                 \tag{14}
$$

设 $\gamma=1$（连续均值）或 $\gamma=1+e^{-N_0\rho}$（固定有限均值）。用(6)直接计算 $L$ 的六 jets 范数 $\Lambda_0,\Lambda_r,\Lambda_{rr},\Lambda_t,\Lambda_{tt},\Lambda_{rt}$。则

$$
F_0=\gamma U_0+\Lambda_0,\quad
F_r=\gamma U_r+\Lambda_r,\quad
F_{rr}=\gamma U_{rr}+\Lambda_{rr},
$$

$$
F_t=U_t+\Lambda_t,\quad
F_{tt}=U_{tt}+\Lambda_{tt},\quad
F_{rt}=U_{rt}+\Lambda_{rt}                                      \tag{15}
$$

分别控制完整 $f,f_r,f_{rr},f_\theta,f_{\theta\theta},f_{r\theta}$。这里没有遗漏后置受迫项或从属核心项。

### 核心不能先拆开的一个组合

R576 的 Darboux 分子含 $-rWf_{rr}-rW'f_r$。在核心单独取绝对值会制造 $\delta^{-1}$ 爆炸，虽然真实和可有有限极限。应先按同一有限系数合并：

$$
V_P=\|Wv_{rr}+W'v_r\|_\rho,\qquad
\Lambda_P=\|WL_{rr}+W'L_r\|_\rho,
$$

$$
\boxed{P_r^{\,b}:=
 \gamma(AV_P+|W|BV_1^2)+\Lambda_P
 \ \ge\ \|(Wf_r)'\|_\rho.}                                    \tag{16}
$$

证明：$Wg_{rr}+W'g_r=d_1(Wv_{rr}+W'v_r)+Wd_2v_r^2$，其中 $d_1,d_2$ 是(12)中的两个函数；$Q$ 与径向导数及标量 $W$ 交换。最后加上 $WL_{rr}+W'L_r$。在(16)中必须先对每个系数作加法再取绝对值，不能用两个已分开且发散的界相加来冒充这个收益。

## 4. 同一高度的分母与 turning 函数

沿用 R594 的记号，令

$$
p=-W+f_r,\quad q=f_\theta,\quad t=f_{\theta\theta},\quad
b^2=r^2-q^2,\quad
M=r+pt-q^2/r,\quad N=r/b+r^2pt/b^3.                             \tag{17}
$$

定义以下完全显式的标量：

$$
x=F_t^2/r^2,\qquad
m=(|W|+F_r)F_{tt}+F_t^2/r,\qquad d_M=r-m.                       \tag{18}
$$

要求

$$
x<1,\qquad d_M>0.                                              \tag{19}
$$

Neumann/binomial 级数与(5)给

$$
\|M^{-1}\|_\rho\le d_M^{-1},
$$

$$
\|N\|_\rho\le
n_\rho:=(1-x)^{-1/2}
+\frac{(|W|+F_r)F_{tt}}{r(1-x)^{3/2}}.                          \tag{20}
$$

实轴上 $M\ge d_M$、$0<b\le r$，而 $N=Mr^2/b^3$，故

$$
N\ge n_-:=d_M/r>0.                                            \tag{21}
$$

写 $E=W^2+e$。准确有

$$
u^2=E-\frac{r^2p^2}{b^2}=e-s,\qquad
s=-2Wf_r+f_r^2+\frac{p^2q^2}{r^2-q^2}.
$$

再定义

$$
s_\rho=2|W|F_r+F_r^2+
       \frac{(|W|+F_r)^2F_t^2}{r^2-F_t^2}.                     \tag{22}
$$

则 $\|s\|_\rho\le s_\rho$。只要 $e>s_\rho$，同一解析平方根分支满足

$$
\left\|\frac N{\sqrt{e-s}}\right\|_\rho
\le \frac{n_\rho}{\sqrt{e-s_\rho}}.                             \tag{23}
$$

这是一个具体、可失败的充分门；它不是 R576 所有可行高度的必要条件。若某个大幅候选过不了(19)或(23)，只能说这一主控暂不适用，不能排除该几何机制。

## 5. 离散 turning 根到唯一连续根

给定一个实际近似值 $\widehat e>s_\rho$、一个明确半宽 $h>0$，满足

$$
\widehat e-h>s_\rho.                                           \tag{24}
$$

用同一完整高度定义 $T_N[N/\sqrt{\widehat e-s}]$。设其实际数值评价有已支付的绝对误差 $\epsilon_{\rm ev}$。令

$$
\epsilon=
\left|\left(T_N\frac N{\sqrt{\widehat e-s}}\right)_{\rm computed}-1\right|
+\epsilon_{\rm ev}
+\frac{n_\rho e^{-N\rho}}{\sqrt{\widehat e-s_\rho}},
$$

$$
\kappa=\frac{n_-}{2(\widehat e+h+s_\rho)^{3/2}},\qquad
d=\epsilon/\kappa.                                             \tag{25}
$$

若

$$
d\le h,                                                       \tag{26}
$$

则准确连续 turning 方程

$$
\left\langle\frac N{\sqrt{e_*-s}}\right\rangle=1                  \tag{27}
$$

在 $[\widehat e-d,\widehat e+d]$ 内有唯一根。

证明：由(9)(23)，左端减1在 $\widehat e$ 处绝对值不超过 $\epsilon$。在(24)的整个实区间，导数为
$-\frac12\langle N/(e-s)^{3/2}\rangle\le-\kappa$，这里用(21)与 $e-s\le\widehat e+h+s_\rho$。因此两端函数值分别非负、非正；介值定理给根，严格负导数给唯一性。R576 的正域唯一根于是正是该根。

记

$$
e_-=\widehat e-d,\quad e_+=\widehat e+d.
$$

那么在整个实圆周上

$$
E_*\ge W^2+e_-,\quad u_*^2\ge e_--s_\rho>0,\quad
\max_\theta\frac N{u_*^3}
\le\frac{n_\rho}{(e_--s_\rho)^{3/2}}.                           \tag{28}
$$

若 $\widehat e$ 来自有限网的56次二分加3次Newton，仍必须给出(25)中的评价误差；算法名称或一个很小的浮点 turning 残差不能替代这个误差项。这里没有把有限根直接认作连续根。

## 6. 直接控制非零 Darboux 模，无需先认证数值 $e'$

R576 消去纯背景后写成

$$
\mathscr D=A_t-\frac{e_*'}2M,
$$

$$
A_t=-r(Wf_r)'
-e_*W'f_{\theta\theta}
+(W^2+e_*)f_{rr}f_{\theta\theta}
-WW'f_rf_{\theta\theta}
$$

$$
\hspace{1.8cm}
-(W^2+e_*)(f_{r\theta}-f_\theta/r)^2
+rf_rf_{rr}+WW'f_\theta^2/r.                                  \tag{29}
$$

令 $G(e)=A_t(e)/M$。因为 $e_*'/2$ 是角常数，

$$
H:=\mathscr D/M=G(e_*)-e_*'/2
$$

的每个非零 Fourier 系数都与 $G(e_*)$ 相同。这允许从完整二 jets 直接支付所有非零误差；不需额外求一次三 jets 或先认证数值 $e'$。

令 $B_\rho=F_{rt}+F_t/r$。由(15)(16)(29)，

$$
A_\rho=
rP_r^{\,b}
+e_+|W'|F_{tt}
+(W^2+e_+)F_{rr}F_{tt}
+|WW'|F_rF_{tt}
$$

$$
\hspace{1.3cm}
+(W^2+e_+)B_\rho^2
+rF_rF_{rr}+|WW'|F_t^2/r,
\qquad G_\rho=A_\rho/d_M                                      \tag{30}
$$

控制 $\|G(e_*)\|_\rho$ 和 $\|G(\widehat e)\|_\rho$。

此外 $A_t$ 对 $e$ 准确仿射，因此

$$
\partial_eG=
\frac{-W'f_{\theta\theta}
+f_{rr}f_{\theta\theta}-(f_{r\theta}-f_\theta/r)^2}{M},
$$

$$
\|\partial_eG\|_\rho\le
L_\rho:=\frac{(|W'|+F_{rr})F_{tt}+B_\rho^2}{d_M}.                \tag{31}
$$

核心附近(30)仍应按真正相容的系数阶数取界。式(16)先付掉最明显的线性相消，但它不保证对任意粗区间都自动有小的 $G_\rho$。

## 7. 有限角读数到完整连续角误差

选 $J\ge1$ 且 $2J<N/2$。从同一个有限网、同一个完整高度和 $\widehat e$，计算

$$
\widetilde g_j=
\left(2T_N[G(\widehat e)\cos(2j\theta)]\right)_{\rm computed},
\quad 1\le j\le J.
$$

设这些值的评价误差已分别包围为 $\epsilon_j$。由(10)(25)(31)，

$$
|2\langle G(e_*)\cos(2j\theta)\rangle|
\le |\widetilde g_j|+\epsilon_j
+G_\rho e^{-(N-2j)\rho}
+dL_\rho e^{-2j\rho}.                                         \tag{32}
$$

最后一项确实有 $e^{-2j\rho}$：对一个实偶函数，其第 $2j$ 余弦系数在(4)中总计贡献该系数绝对值乘 $e^{2j\rho}$。

定义一个有限可计算的完整非零谱预算

$$
\boxed{
T=
\sum_{j=1}^{J}\left[
|\widetilde g_j|+\epsilon_j
+G_\rho e^{-(N-2j)\rho}
+dL_\rho e^{-2j\rho}\right]
+G_\rho e^{-2(J+1)\rho}.
}                                                               \tag{33}
$$

由(8)(32)，$G(e_*)$ 的全部非零角频率之和的真实 $L^\infty$ 范数不超过 $T$。本式不要求优化器低模已精确为0；所有低模实际剩余都留下了。

准确 turning 微分恒等仍给

$$
0=\langle \omega\mathscr D\rangle
=\left\langle \frac N{u_*^3}H\right\rangle.
$$

权严格正，所以 $H$ 的角常数绝对值不超过其非零部分的 $L^\infty$ 范数。故

$$
\|H\|_\infty\le2T,\qquad
\|\mathcal R\|_\infty
\le \frac{2n_\rho T}{(e_--s_\rho)^{3/2}}.                        \tag{34}
$$

这里没有用数值 $e'$，也没有均值分母退化问题。

## 8. 到同一实际位置的 metric 误差

由 R576/R594 的准确位置重构，

$$
W_*=\Pi_{2\pi}\big[b(\Pi_\pi\mathcal R)JT_{\rm tan}\big].
$$

内层的残差是 $\pi$ 周期零均值，外层向量是 $\pi$ 反周期。周期为 $P$ 的零均值原函数 $L^\infty$ 算子范数不超过 $P/4$，因此 R594 已证明

$$
\|W_*\|_\infty\le(\pi^2/8)\max b\,\|\mathcal R\|_\infty.
$$

用 $\max b\le r$ 及(28)(34)，得到完全显式的

$$
\boxed{
\Delta=
\frac{\pi^2r}{4\sqrt{W^2+e_-}}\,
 \frac{n_\rho T}{(e_--s_\rho)^{3/2}},
\qquad
\eta_{\rm actual}\le(1+\sqrt2)\Delta+\Delta^2.
}                                                               \tag{35}
$$

这里 $\eta_{\rm actual}$ 是由 **连续 turning 根和连续实际重构位置** 得到的度量相对误差。证明中每个输入误差都在(25)(32)(33)显式出现；若没有支付那些误差，不能只代浮点值后把(35)称为证书。正的误差界也不等于准确等距。

(35)不付曲率或全对点 reach；它没有用离散重构恒等替代实际位置的二阶导数。

## 9. 两个与当前新输入直接有关的额外误差

### 9.1 旧实际网均值与固定512均值

设旧网为 $N_1$，新固定网为 $N_0=512$。用(9)分别比较连续均值，得到三个真实径向常数差

$$
|\partial_r^d[(T_{N_1}-T_{512})g]|
\le (e^{-N_1\rho}+e^{-512\rho})U_d,
\qquad d=0,1,2,                                                \tag{36}
$$

其中 $U_d$ 分别为(13)的 $U_0,U_r,U_{rr}$。它们改变 $f,f_r,f_{rr}$，不改变三个角导数。对固定512与连续均值的比较，只保留(36)中 $e^{-512\rho}$ 一项。

这明确了本次新模型保留所有旧系数而改变实际径向常数的意义；不能说两个不同观测角网原先天然定义同一完整高度。

### 9.2 核心 turning 根的有限求积误差如何进入真高度

R602 的核心 $P=P_0$ 是最高22模的有限多项式。其连续根满足

$$
\langle(e_R+2P)^{-1/2}\rangle=1.
$$

对它直接使用第5节：取 $N=512$、$N(\theta)\equiv1$、$s=-2P$、$s_\rho=2\|P\|_\rho$。由此得到实际有限根与连续根的误差 $|d e_R|\le d_R$。

R602 的准确目标为

$$
P_1^*=
\{c(e_R+2P)P_{\theta\theta}-P_\theta^2
 +(2c+1)\langle P_\theta^2\rangle\}/R,\quad
c=\alpha/(1+\alpha).
$$

固定 $P$ 时，根误差准确产生

$$
dP_1^*=(c/R)d e_R\,P_{\theta\theta}.                             \tag{37}
$$

设真正添加的径向因子为
$\phi(r)=\chi(r)(R-r)^{\alpha+2}/[k(\alpha+2)]$。
从有限根改为准确核心根的完整高度差就是 $\phi\,dP_1^*$。它的六 jets 分别由

$$
\frac{c\,d_R}{R}
\big(
|\phi|\|P_{\theta\theta}\|_\rho,\
|\phi'|\|P_{\theta\theta}\|_\rho,\
|\phi''|\|P_{\theta\theta}\|_\rho,\
|\phi|\|P_{\theta\theta\theta}\|_\rho,\
|\phi|\|P_{\theta\theta\theta\theta}\|_\rho,\
|\phi'|\|P_{\theta\theta\theta}\|_\rho
\big)                                                         \tag{38}
$$

控制，全部仍是有限系数计算。这一差必须加入新高度系数/点值的区间包围，随后重新进入(15)–(35)；不能只在核心把残差写成0而不改正文。

$P_1^*$ 的三角次数最多44，$P_\theta^2$ 也最多44。512点求积及向最高44模投影在准确算术中对这些多项式完全准确，因为被积频率最高88，小于512。因此这里的非多项式求积误差来自核心根；剩余有限加乘和三角函数舍入仍须包含在区间误差中。

在 R597/R602 的 $\alpha>0$ 核心假设下，若旧预tanh场有逐阶一致的 $v=O(\delta^{\alpha+1})$，并且其有限正频率都小于512，则 $T_{512}v=0$。$\tanh(v/\sigma)=v/\sigma+O(v^3)$ 给均值项及两个径向导数分别为
$O(\delta^{3\alpha+3})$、$O(\delta^{3\alpha+2})$、$O(\delta^{3\alpha+1})$。
因 $W\sim k\delta^{-\alpha}$，它对核心 $P_0=\lim Wf_r$ 和
$P_1=\lim(Wf_r)'$ 的贡献均为0。因此当前 canonical 均值变更不改变 R602 的核心 trace 定义；它仍改变正文的实际高度。

## 10. 如何取得径向连续结论，以及本稿没有替代什么

(6)–(38)首先给固定 $r$ 上的连续全角结论。若只在1281个半径取值，即使每一圈都算得很精确，也只支付这些半径，不能自动覆盖间隙。

一个不需第三 jets 的实际做法是：把一个紧致正文径向区间分成有限闭小区间。在每个小区间上，对(1)每个系数、其一二阶径向导数、$W,W'$ 和(16)的先合并系数给出 **真实区间包围**。可在该小区间选一个固定 $\widehat e$，对有限角点的 turning 值和 $G$ 值用同一系数区间求包围。于是(18)–(35)成为对该整个小区间同时成立的不等式。各区间的上界取最大便给正文连续 metric 界。它不要求把径向导数差分成三 jets，也不能以采样极值代替系数区间。

必须分别支付：

- 原准确无限 flat germ 与有限 DtN 截断/数值口的误差；
- 真 ODE/connector/core 外传和所报告 jets 的误差；
- 全平内尾，包括新18/20/22模的实际归一常数；旧 R588 的既有范围不能不经证明直接扩用；
- 核心端的逐阶渐近及由(37)(38)产生的完整高度修正；
- 上述系数区间、有限点求值与舍入界。

这些项目可以在已有严格尾结论、精确 ODE和已定义有限系数表示上继续完成；本文没有靠当前有限样本宣布已经付完它们。

当前下一实际输入应在11模自然终态明确遗漏后，从其真实完整系数构造(7)(13)(16)(18)(22)(30)(31)和实际 $G=A_t/M$ 的必要角系数。它们属于一次明确的新增连续界工作，不能只重复旧 FFT 差或原相同优化来充作本定理的输入。若当前高度不满足某一充分主控门，保留其实际失败值，调整分区、角权或表示继续研究；这不是整个机制不存在的结论。

### 已登记依赖

- [R576](R576-exact-turning-elimination-and-finite-nonlinear-height-interface.md)：连续 turning 根、真实位置重构和二 jets Darboux 恒等。
- [R594](R594-exact-nonlinear-radial-acceleration-and-galerkin-leakage.md)：准确加权均值、两次原函数及实际 metric 传播。
- [R597](R597-nonlinear-core-trace-and-realizable-free-order.md)、[R602](R602-exact-nonlinear-core-trace-elimination.md)：核心完整 trace 与真实从属高度修正。
- [R600](R600-same-mild-tail-flat-kernels-through-thirty-two.md)：准确有限高模范围；不授未支付的数值传递误差。
