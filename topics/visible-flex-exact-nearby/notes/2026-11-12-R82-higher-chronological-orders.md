# R82 的可选高阶时间有序截断

本说明沿用 R82 全部真实对象、固定参考和带宽合同。它不改变已经完成的
二阶公式，也不宣布当前实际参数源需要升阶；应先取得实际 $B_1,B_2$。
本次仅给一般尾公式和有限实现接口，没有运行新的高阶计算。

## 1. 一般 n 阶参数尾

令 $q_\lambda=2A/R<1$、$L=1/q_\lambda$，并将辅助流写成

\[
 X_\lambda=x+\sum_{r\ge1}\lambda^r U_r.
\]

保留 $r\le n$，并对这些准确有序系数作一、二阶真实参数微分。
R82 在 $|\lambda|=L$ 已证明

\[
 |\partial_pX_\lambda|\le eLB_1,\qquad
 |\partial_p^2X_\lambda|
 \le eLB_2+2e(2e-1)L^2B_1^2/R.
\]

所以 Cauchy 系数界对 $r\ge n+1$ 求和，直接给

\[
 \boxed{T_{1,n}=\frac{eB_1q_\lambda^n}{1-q_\lambda}},\qquad
 \boxed{T_{2,n}=\frac{eB_2q_\lambda^n+
                  2e(2e-1)B_1^2q_\lambda^{n-1}/R}{1-q_\lambda}}.
\]

特别地，$n\ge2$ 时 $T_{i,n}=q_\lambda^{n-2}T_{i,2}$，$i=1,2$。
三阶多付一个 $2A/R$，四阶多付其平方。这里的“阶”是小场缩放 $\lambda$
的时间有序阶数，不是参数导数阶数。
如同时需要零阶流的统一公式，$|X_\lambda-x|\le LA$ 给
$T_{0,n}\le A q_\lambda^n/(1-q_\lambda)$；在 $n=2$ 时优先保留 R72 更细的
$A^3/[2(R-A)^2]$，不以粗界覆盖它。

## 2. 有限时间/Fourier 系数的可选递推

以下 $g_x,g_{xx},g_{xxx}$ 都是真正的空间导数，不是归一化 Taylor 系数。
准确的前四项为

\[
\begin{aligned}
 \partial_vU_1&=g_0,\\
 \partial_vU_2&=g_{0x}U_1,\\
 \partial_vU_3&=g_{0x}U_2+\tfrac12g_{0xx}U_1^2,\\
 \partial_vU_4&=g_{0x}U_3+g_{0xx}U_1U_2
                                      +\tfrac16g_{0xxx}U_1^3.
\end{aligned}
\]

全部首值为零。一般递推是

\[
 \partial_v U_r=
 \sum_{m=0}^{r-1}\frac{\partial_x^m g_0}{m!}
 \sum_{\substack{r_1+\cdots+r_m=r-1\\r_j\ge1}}
                 U_{r_1}\cdots U_{r_m},
\]

其中 $m=0$ 的空乘积仅在 $r=1$ 贡献 $1$。
每个参考段开始时，所有 $U_r$ 都继承上一段的准确末值；段内逐级积分，
不可把三、四阶项在每段重置为零。

在截断环 $\mathbb C[\varepsilon]/(\varepsilon^3)$ 中置

\[
 g^{[p]}=g_0+\varepsilon g_1+\tfrac12\varepsilon^2g_2,
 \qquad
 U_r^{[p]}=U_r+\varepsilon\partial_pU_r
                         +\tfrac12\varepsilon^2\partial_p^2U_r.
\]

将以上递推直接在此环中计算，即保留每个有序阶的两阶参数链式项；输出
$\varepsilon^2$ 系数时乘 $2$。有限时间多项式可以准确积分，有限 Fourier
空间导数使用标签频率 $ik$，每次乘积保留全部和频或另付投影费。
最高 Fourier 次数随有序阶线性增长，不因时间段数而必须指数增长。

近似三源不需要恰是一个已保存有限族的形式导数；但高阶递推相对真实三源的
误差必须重新支付。R82 (82.14) 只针对保留到二阶的表达式，不能原样用于
$U_3,U_4$。可逐项用外带的源误差及 Cauchy 导数界支付，或对辅助 $\lambda$
域上的完整源差作统一估计后提取系数。应在实际 $B_1,B_2$ 表明需要升阶时
再选择和实现，不以这份一般尾说明冒称高阶实际密度已经认证。

沟通更正：此前一条消息的 $U_4$ 末项漏写了 $1/6$；以上公式采用标准导数，
含准确阶乘。没有程序或数值结果使用过那条漏项表达式。
