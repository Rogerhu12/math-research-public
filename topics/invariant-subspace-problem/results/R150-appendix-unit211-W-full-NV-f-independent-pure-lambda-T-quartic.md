# R150：W 完整原 N4 四次的 f 消失与三个同值纯 lambda,T 四次

日期：2026-11-28（Asia/Taipei）。
会话：Astra-ISP-8542378f-20261127。

## 1. 结论和原范围

本篇沿当前 W 原权图、原 $E_0,N_0,P_1$ 恢复坐标工作。
所有纯权分母仍限先行已经支付的范围；不向一般值碰撞
$h_U=k_U$ 外推这些权单位。

上一已返回的新四次
$$
\overline B_4=b_0(\widetilde Z_0+Dz_2)-a_\Delta z_1
$$
在把原 Gram 改写为同一点的 $(\lambda,T,f)$ 后，
**完全不含 $f$**。下面直接证明三个准确一次系数身份
$$
MQ\,[f]z_1=2b_0,\qquad
MQ\,[f](\widetilde Z_0+Dz_2)=2a_\Delta,\qquad
[f]\overline B_4=0.                                    \tag{1}
$$
因此它等于其准确 $f$ 常数项
$\mathcal B(\lambda,T)$，总几何次数至多四，且所有分母均为纯权单位。
这是完整纸面恒等式，不把尚未运行的新系数展开记为实际计算。

和已经发表的 $\mathcal R_4,\mathcal C_4$ 一起，
得到三个同一点的纯 $(\lambda,T)$ 四次必要式。
在 $b_0\ne0$ 图上，它们还准确恢复原值中心的二、三矩、
原 Delta 与完整 $N_4(V_{\rm val})$ 子系统。
$b_0=0$ 整支继续由独立输入处理，不能先当作单位删除。
全部原均值和个别 N/P 条件仍另行保留。

## 2. 先付款的 W 权恒等式

取
$$
u=e+1,\quad Q=ek,\quad \overline V=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{k\overline V},
$$
$$
\delta=1-Q,\quad m=u-\ell,\quad
M=\ell(2u-\ell Q)-u^2=\ell^2\delta-m^2=4bc\delta,
$$
$$
T_0=2u-\ell Q-2u^2,\quad
J=2u(1-u)+\ell Q,\quad
\Phi=T_0+4u-4+Q,\quad P_f=T_0(J-Q).
$$
直接代入这些原权公式，分别得到
$$
\begin{aligned}
T_0&=-\frac{ue(k+2)(k+4)}{\overline V},\\
\Phi&=-\frac{2e^2(k+4)}{\overline V},\\
J&=\frac{uek(k+2-4e)}{\overline V},\\
J-Q&=-\frac{2e^2k(2e+1)}{\overline V},\\
J-2uQ&=-\frac{uek(2e+1)(k+2)}{\overline V}.
\end{aligned}                                          \tag{2}
$$
将 (2) 后两行与前两行相乘，完整得到
$$
\boxed{\,J\Phi-P_f=2uQ\Phi.\,}                           \tag{3}
$$
这是当前 W 权式本身的恒等式；
没有新增权曲线假设，没有除 $2e+1$ 或一个未知首项。

## 3. 原 E0/N0/P1 的自由 f 仿射恢复

沿已经证明的原三个方程，记
$$
G=\lambda P_{02}-(1-u)T_0,\qquad
P_c=QP_{02}(\ell+T)-GT_0 .
$$
当 $\lambda,T,f$ 作为原恢复参数时，
$$
t=-\frac{P_ff+P_c}{bcQ\Phi},\quad
V=\frac{Jf-G+bcQt}{Q},\quad
W_1=\frac{T_0}{2}+2uf,\quad
A_1=2f-2V+2bc\,t.                                     \tag{4}
$$
这些都是原 $E_0,N_0,P_1$ 已有的线性恢复，
不是将一组较弱必要方程当作全原系统。
本篇只使用原权 $bc,Q,\Phi,M$ 的逆；不倒 $T_0$、$P_f$、
$D$、$b_0$ 或任何新的几何首项。

令 $[f]$ 表示把 $\lambda,T$ 固定后的 $f$ 一次系数。
由 (3)、(4)，置
$$
\beta:=bc[f]t=-\frac{P_f}{Q\Phi}
=2u-\frac JQ .
$$
于是
$$
[f]V=2u,\qquad [f]W_1=2u,\qquad
[f]A_1=2-\frac{2J}{Q}.                                 \tag{5}
$$
真实 native 恢复为
$$
\theta=u-\ell Q,\qquad
x=\frac{\theta V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M}.
$$
利用 $\theta-m=\ell\delta$，又有
$$
[f]x=\frac{2u\ell\delta}{M},\qquad
[f]y=-\frac{2um}{M}.                                   \tag{6}
$$
这保留整个自由 $f$，并没有选取物理 $f=0$。

## 4. 三条完整一次系数恒等式

记
$$
c_\lambda=3-2\lambda,\quad w=\lambda-1-T,\quad
A_\lambda=2\lambda^2-2\lambda+1,\quad D=\ell A_\lambda-T^2,
$$
$$
A_*=4uQ-J,\quad C_*=A_*m^2+J\delta\ell^2,
$$
$$
\begin{aligned}
a_\Delta={}&M\ell^2Q(3-4\lambda)+MA_*T^2
 +2MuQc_\lambda\ell T+DC_*,\\
b_0={}&2m(A_*T+uQc_\lambda\ell).
\end{aligned}                                          \tag{7}
$$
这些量都不含 $f$。

使用已刊完整原 N4 短式和已付 M 归一：
$$
\begin{aligned}
z_1&=-2(\ell c_\lambda+2T)y-2\ell w+mTt/\delta,\\
z_2&=2\{\ell(x-f)-my-bc\,t\},\\
\widetilde Z_0
 &=\ell^2A_1+4\ell^2(1-2\lambda)f+2\ell fD\\
 &\quad+2\ell uw(\ell c_\lambda+T)
   +2V(\ell^2+\ell c_\lambda T+T^2)
   +2bc\,t(T^2-\ell^2).
\end{aligned}                                          \tag{8}
$$
它们都对 $f$ 至多一次；这是 (4) 的真实代入次数。

先由 (5)、(6) 和 $bc\delta=M/4$ 得
$$
\begin{aligned}
[f]z_1
 &=\frac{4um}{M}(\ell c_\lambda+2T)+\frac{4mT\beta}{M}\\
 &=\frac{4m}{MQ}(uQ\ell c_\lambda+A_*T)
  =\frac{2b_0}{MQ}.                                    \tag{9}
\end{aligned}
$$
再直接得到
$$
[f]z_2=\frac{8um^2}{M}-\frac{4u(u-1)}{Q}.               \tag{10}
$$
这里
$$
C_*-MQ\ell
=4uQm^2+M(J-Q\ell)
=4uQm^2-2u(u-1)M,                                     \tag{11}
$$
所以
$$
MQ[f]z_2=2(C_*-MQ\ell).                                \tag{12}
$$

最后将 (5) 代入 (8)，合并其常数、T、T 平方项，得
$$
[f]\widetilde Z_0
=2\ell^2(3-4\lambda)+4u\ell c_\lambda T
 +\frac{2A_*T^2}{Q}+2\ell D.                           \tag{13}
$$
由 (7)，这准确等于
$$
\frac{2a_\Delta}{MQ}
-\frac{2D(C_*-MQ\ell)}{MQ}.
$$
合 (12) 即得到
$$
MQ[f](\widetilde Z_0+Dz_2)=2a_\Delta.                   \tag{14}
$$
(9)、(14) 立刻给
$$
[f]\overline B_4
=b_0\frac{2a_\Delta}{MQ}
-a_\Delta\frac{2b_0}{MQ}=0.                             \tag{15}
$$
因为 $\overline B_4$ 对 $f$ 至多一次，(15) 是它完全不含 $f$
的证明，不只是最高次项消失或某点的导数为零。

## 5. 新纯 lambda,T 四次的准确小定义

为写出这个常数系数，定义
$$
t_*=-\frac{P_c}{bcQ\Phi},\quad
V_*=-\frac GQ-\frac{P_c}{Q\Phi},\quad
W_*=\frac{T_0}{2},\quad A_{1*}=\frac{2G}{Q},
$$
$$
x_*=\frac{\theta V_*-mW_*}{M},\qquad
y_*=\frac{\ell W_*-uV_*}{M}.
$$
它们只是 (4) 的多项式常数系数，不是一个要求 $f=0$ 的原子图。
令 $z_{1*},z_{2*},Z_{0*}$ 为 (8) 在这些常数系数及形式 $f=0$
下的准确代入，则
$$
\boxed{\quad
\mathcal B(\lambda,T)
=b_0(Z_{0*}+Dz_{2*})-a_\Delta z_{1*}
=\overline B_4(\lambda,T,f).
\quad}                                                 \tag{16}
$$
所有 starred 恢复量对 $\lambda,T$ 都仿射。
故 $z_{1*},z_{2*},Z_{0*}$ 的次数分别至多 $2,1,3$，
而 $b_0,a_\Delta,D$ 次数分别至多 $1,2,2$，
从而 $\deg_{\lambda,T}\mathcal B\le4$。
其全部分母是已经支付的纯权单位。
特别没有倒置 $A_*$，整个 $b_0=0$ 与 $A_*=0$ 仍在 (16) 内。

## 6. 同一点三四次及补图的原值等价

沿[两个原四次](R150-appendix-unit211-W-original-two-quartic-necessary-values.md)，
取同一原值中心 $s$，并记
$$
q=Ms^2-D=\ell E_2,\quad
H=K-2mDs,\quad
K=\ell^2B_\lambda-3\ell A_\lambda T+2T^3,
$$
$$
L=a_\Delta+Mb_0s,\qquad
\Phi L=M\ell^2E_\Delta-C_*\Phi q.
$$
已付 M 的完整原 N4 直接身份是
$$
\Phi\mathcal B
=\Phi b_0\ell^2N_4(V_{\rm val})
 -M\ell^2z_1E_\Delta+\Phi(C_*z_1-b_0z_2)q.               \tag{17}
$$
它来自
$\ell^2N_4(V_{\rm val})=\widetilde Z_0+Mz_1s+Mz_2s^2$
的完整二次展开；不要求 $D$ 逆。

于是所有当前原点都满足纯值四次系统
$$
\mathcal R_4=M a_\Delta^2-D(Mb_0)^2=0,\qquad
\mathcal C_4=2mD a_\Delta+KMb_0=0,\qquad
\mathcal B=0.                                          \tag{18}
$$
三式始终是同一个 $\lambda,T$，没有另取根或值中心。

进一步，只在 $b_0\ne0$ 补图，定义
$$
s=-\frac{a_\Delta}{Mb_0}.
$$
直接乘回为
$$
q=\frac{\mathcal R_4}{M^2b_0^2},\qquad
H=\frac{\mathcal C_4}{Mb_0}.
$$
所以 (18) 给 $q=H=L=0$，从原身份恢复
$E_2=E_3=E_\Delta=0$；
其中
$H=\ell(2ms+3\ell+3T)E_2-\ell^2E_3$。
完整 N4 恒等式再给
$$
\ell^2N_4(V_{\rm val})=\frac{\mathcal B}{b_0}=0.
$$
因此在这个明确补图上，(18) 精确恢复该原值子系统，
不需要以未付范数代替原方程。
反向由原系统到 (18) 已由同样的恒等式证明。

$b_0=0$ 没有因此被删除；它是独立原二次/六次输入的完整分支。
本篇也没有说 (18) 已经包含所有原均值、NS/PS 或两谱个别 N/P。
这些条件和原物理要求仍须在同一点返回。

## 7. 来源与执行状态

使用的先行原定义为：

- [完整原 N4 三短式](R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)；
- [同值两个原四次](R150-appendix-unit211-W-original-two-quartic-necessary-values.md)；
- [原值低 D 理想压缩](R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)；
- [已实际返回的 paid-M 四次两列](R150-appendix-unit211-W-full-NV-paid-M-quartic-two-columns-and-two-scalars.md)。

上述同一个 $\overline B_4$ 已由726554源码首次完整返回，
run46124406408/job140915689273；
本篇没有再运行该原迹、两列或两个标量。

(2)–(17) 是这里写全的纸面代数证明。
后继自含小源可直接用 (16) 定义新纯值输入并保原组合，
不再从 native 或 alpha/chi 大矩阵恢复它。
尚未运行的新系数、结式、因式或原排空均不作为本篇事实。
