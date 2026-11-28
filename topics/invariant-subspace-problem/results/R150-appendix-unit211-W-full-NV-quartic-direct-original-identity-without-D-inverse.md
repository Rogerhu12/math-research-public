# R150：同一 W 新四次的完整原 N4 直接组合，不逆 D

日期：2026-11-28（Asia/Taipei）。
会话：Astra-ISP-8542378f-20261127。

## 1. 准确范围

本篇沿当前 W 已限定的原权图及其原值参数，不扩大任何先行权单位的适用域。
特别不把以物理 $D\ne0$ 证明过的权排除外推到一般 $h_U=k_U$。
这里给出上一已返回 $\overline B_4$ 的更直接原理想来源：
这条组合本身不倒 $D$，不倒 $m$、$b_0$ 或任一原值首项，
而且不需要第三矩。
这是已有完整原身份的纸面合成，不重跑四次两列源或任何旧门。

## 2. 同一个原值向量

采用[两个原四次](R150-appendix-unit211-W-original-two-quartic-necessary-values.md)
的原值中心
$$
s=(\ell\zeta-T)/u,\qquad
q=Ms^2-D=\ell E_2,\qquad
D=\ell A_\lambda-T^2.
$$
同一原向量
$$
V_{\rm val}=(1,\lambda-1-T,h_U,k_U)
$$
满足
$$
\ell V_{\rm val}=\widetilde V_0+s\widetilde V_1,
$$
其中
$$
\widetilde V_0=(\ell,\ell w,\ell+T,\ell+T),\quad
\widetilde V_1=(0,0,m-\ell\rho,m+\ell\rho),\quad
w=\lambda-1-T,\quad \rho^2=\delta .
$$

[九变量完整 N4 三短式](R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)
准确给出
$$
\widetilde Z_0=N_4(\widetilde V_0),\quad
\widetilde Z_1=N_4(\widetilde V_0+\widetilde V_1)
 -N_4(\widetilde V_0)-N_4(\widetilde V_1),\quad
\widetilde Z_2=N_4(\widetilde V_1).
$$
$N_4$ 对值向量是二次齐次式，所以完整而非分量的原关系为
$$
\widetilde N:=\ell^2N_4(V_{\rm val})
=\widetilde Z_0+s\widetilde Z_1+s^2\widetilde Z_2.        \tag{1}
$$

沿已实际返回的 native 恒等式
$V=\ell x+my$、$uV-\ell W_1=-My$，定义
$$
\begin{aligned}
b_0&=2m\{A_*T+uQ\ell(3-2\lambda)\},\\
z_1&=-2\{\ell(3-2\lambda)+2T\}y-2\ell w+mTt/\delta,\\
z_2&=2\{\ell(x-f)-my-bc\,t\}.
\end{aligned}
$$
此前唯一 run46124406408/job140915689273 已完整返回
$$
b_\Delta=Mb_0,\qquad \widetilde Z_1=Mz_1,\qquad
\widetilde Z_2=Mz_2.                                   \tag{2}
$$
本篇引用这一已成身份，不再执行。

## 3. 直接完整原组合

记
$$
L=a_\Delta+Mb_0s,\qquad
\overline B_4=b_0(\widetilde Z_0+Dz_2)-a_\Delta z_1 .
$$
将 (1)、(2) 逐项代入，立即得到多项式身份
$$
\boxed{\quad
\overline B_4=b_0\widetilde N-z_1L-b_0z_2q .
\quad}                                                 \tag{3}
$$
其 $s$ 项因 $Mb_0z_1s$ 相消，$s^2$ 项因 $Mb_0z_2s^2$ 相消；
常数项恰为上述 $\overline B_4$，没有任何额外条件。

已刊原 Delta 身份为
$$
\Phi L=M\ell^2E_\Delta-C_*\Phi q,\qquad
C_*=A_*m^2+J\delta\ell^2 .
$$
因此 (3) 进一步给出不含 $1/\Phi$ 的完整交叉乘回：
$$
\boxed{\quad
\Phi\overline B_4
=\Phi b_0\ell^2N_4(V_{\rm val})
 -M\ell^2z_1E_\Delta
 +\Phi(C_*z_1-b_0z_2)q .
\quad}                                                 \tag{4}
$$
由于当前 W 图已经支付 $\Phi$，同一 $\overline B_4$ 直接属于
完整原 $N_4(V_{\rm val}),E_\Delta,E_2$ 生成的局部化理想。
不需要先乘物理 $D$ 再利用 $D\ne0$ 去除，也不需要原第三矩 $E_3$。

这不改变任何已运行对象：
726554 源所归约的四次正是 (3) 的 $\overline B_4$；
其两列和两个必要标量继续由同一完整原理想支持。
本篇只加强该已成对象的来源说明，没有声称新的数值投影或排空。

## 4. 整 b0 零支与其余范围

在 $b_0=0$ 上，原 $L=0$ 直接迫 $a_\Delta=0$；
这一推论本身也无需 $D$ 逆。
若 $A_*=0$ 同时发生，则
$b_0=2muQ\ell(3-2\lambda)$；
在当前已付 W 物理域，它只会落入已经关闭的
$\lambda=3/2$ 支。这是后继整 $b_0=0$ 新二次/六次输入的来源，
不是将 $A_*$ 支付到一般补图。

(3)、(4) 包括 $b_0=0$、$a_\Delta=0$ 及 $D=0$ 的代数零面。
但先行权局部化究竟允许哪些原物理点，仍由各先行定理的准确范围决定。
没有把当前 W 的权结论转移到尚未处理的一般值碰撞图，
也没有用 (3) 取代全部其余原均值、N/P 或个别值条件。
