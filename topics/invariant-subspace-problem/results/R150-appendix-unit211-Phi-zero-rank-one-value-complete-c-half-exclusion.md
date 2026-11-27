# R150 补充：Phi=0 的 rank-one 值碰撞整 c=1/2 支排除

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 完整范围

在原 unit211 LS 的 $\Phi=0$、$z_n=TB_3-A_2^2=0$ 碰撞图上，交换 singleton 标签后取 $h=1$。沿用 [原碰撞图的精确 1945 次覆盖](R150-appendix-unit211-Phi-zero-rank-one-value-exact-1945-degree-original-cover.md) 中的同一原参数、物理单位、原 Gram 及两条实际 $f,t$ 恢复式。

**本稿排除该图的整个 $c=1/2$ 分支。** 等价地，该图中 $\lambda=1/2$ 或 $3\lambda^2-2\lambda+1=0$ 的全部原复数纤维已排尽。没有把结论推广到一般 $\Phi\ne0$ 图，或尚未处理的整个 $\Phi=0$ 图。

## 2. 原矩与 Phi 给出的全分支

旧原 U-value atlas 的 $h=1$ 图给

$$
A_2=2\lambda^2-2\lambda+1,\qquad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,\qquad
c=A_2^3/B_3^2.
$$

$A_2B_3\ne0$ 是原碰撞图已付单位。直接展开的整恒等式为

$$
2A_2^3-B_3^2=(2\lambda-1)^2(3\lambda^2-2\lambda+1). \tag{2.1}
$$

因此 $c=1/2$ 的所有复数值恰由

$$
\lambda=\tfrac12
\quad\hbox{或}\quad
3\lambda^2-2\lambda+1=0 \tag{2.2}
$$

覆盖。在 $c=1/2$ 下，原 $\Phi$ 恰化为

$$
\Phi=-(1+\rho)^2(\ell-1)(2\ell-3). \tag{2.3}
$$

$p=1+\rho$ 是原单位，故所有 $\ell$ 纤维是 $1$ 或 $3/2$。$\ell=1$ 时 $b=\ell-c=c=1/2$，由已刊
[整个等权排除](R150-appendix-unit211-equal-weights-complete-original-exclusion.md)
排除。只剩

$$
\ell=\tfrac32,\qquad b=1,\qquad c=\tfrac12. \tag{2.4}
$$

这里没有新除掉任何 $\rho$ 的首项或取值。

## 3. 同一个原 Gram 的实际来源

原 $p=1+\rho,q=1-\rho,Q=1-\rho^2$ 保持不变。令

$$
P_f=T_0(J-Q),\quad f_0=-P_c,\quad
t_0=-\frac{N_Ff_0+N_CP_f}{cQS\zeta},\quad H=bP_f.
$$

原单位 $P_f\ne0$ 由整 $T_0=0$ 与整 $J=Q$ 排除支付，$S\zeta\ne0$ 来自当前 LS 图。共享 helper 直接构造 $H$ 倍的原 Gram，而非对有限代数作未付的逆。于是原均值行 $E_1,E_B$ 分别乘 $H^2$ 后都是实际同源行。

在 (2.2) 的两个常数域中计算时，只倒置已付 $\rho,p,q$ 参数因子及确实非零的常数域元素。源码逐项审计所有底环分母、逐次验证逆的乘积，并核回原 $P_f f+P_c=0$、原 $N(V)$ 线和完整原 $P_1$。相应原行清分母后仍保留每个允许的复数 $\rho$。

## 4. lambda=1/2：两个原三次的直接矛盾

这一支的两条实际原均值行在去除已付 $p^7$ 因子后给

$$
F=-9+15\rho^2-10\rho^3,\qquad
G=-9-3\rho+11\rho^2-3\rho^3. \tag{4.1}
$$

设两者都为零。令

$$
K=3F-10G=63+30\rho-65\rho^2.
$$

有完整有理多项式身份

$$
G-\left(\frac3{65}\rho-\frac{25}{169}\right)K
=\frac{54}{845}(5-23\rho). \tag{4.2}
$$

故 $\rho=5/23$，但

$$
K(5/23)=35152/529\ne0.
$$

这排除全部复数 $\rho$。实际源码同时进行了完整 QQ 扩展 Euclid，得次数为 $2,2$ 的原二行 Bézout 系数，且两项乘回为 1。

## 5. 二次 lambda 域：保两个嵌入的真实一元返回

令

$$
K_0=\mathbb Q[\lambda]/(3\lambda^2-2\lambda+1).
$$

判别式为 $-8$，因此这是实际二次常数域。下面始终在 $K_0[\rho]$ 中作一元多项式运算，**不把 $a(\rho)+b(\rho)\lambda=0$ 的两个 QQ 系数分别置零**。每个常数域恒等式都通过两个复数嵌入成立。

两条实际原行分别去除已付 $p^5,p^6$，再乘非零有理常数 1936 后，得到

$$
F_5=\sum_{j=0}^5(a_j+b_j\lambda)\rho^j,\qquad
G_4=\sum_{j=0}^4(c_j+d_j\lambda)\rho^j,
$$

其完整整数系数如下：

| $j$ | $a_j$ | $b_j$ | $c_j$ | $d_j$ |
|---:|---:|---:|---:|---:|
| 0 | 169140 | -1402593 | 75069 | 20484 |
| 1 | -305862 | 4470087 | -266652 | -176568 |
| 2 | 42504 | -5866938 | 317558 | 226032 |
| 3 | 283268 | 3966990 | -217036 | -55944 |
| 4 | -299852 | -1369125 | 73077 | -12468 |
| 5 | 92498 | 197355 | 0 | 0 |

实际完整扩展 Euclid 在 $K_0[\rho]$ 中给

$$
A(\rho)F_5+B(\rho)G_4=1,\qquad
\deg A\le3,\quad\deg B\le4. \tag{5.1}
$$

这里的非零有理行尺度由源码的相应逆尺度吸收到标签中。源码对每次商、余式和扩展系数作完整乘回，最后对两条原多项式的组合再次乘回为 1；没有数值根、模根或选取单个复嵌入的步骤。因此两条原行不能在任一复嵌入下拥有共同 $\rho$ 根，排除整二次常数域。

(2.1)–(2.4)、第 4 节和 (5.1) 合在一起覆盖所有原零分支，完成整个 $c=1/2$ 支的排除。

## 6. 可再生源与真实执行

源：
[整 c-half 原常数域返回](../notes/2026-11-27-unit211-Phi-zero-rank-one-value-c-half-original-return-8542.py)。

- 源 blob：$881cb40b186e4ebc8f453e19150b4d4f4c03063f$；
- 源 SHA256：$ecea30520fbf1cdcc2412b4a6e71e14e362efff0f1163e1bee7211878b0ace60$；
- Actions run/job：45996824454 / 140498201469；
- 实际内层 exit：0；0.219095405 秒；38440 KiB；
- stdout：7131 字节，SHA256 $69c1f40a3b11c1f86efc65fa2c9375dd23234e1a625c4a8aa9c14b0111e1de45$；
- 实际源 main：$83c73ef8d2d8b080540547a613e3466469467fab$；
- 12:13:38.766481 UTC 的实际 pull 后两 README blob 均无变。

二次域原未放大行的 Bézout 标签 SHA256 为
$6f061ad061add018c8923d0fd9c3caa3cfd01ceeda00510832cde36b420da5cf$；
两行最后实际 gcd 为 1。共 48 项一元除法及 4 组扩展 Bézout 乘积已验证。每一支都仅使用到原 $E_1,E_B$ 即已返 1，故没有附加未用原迹的审计门。

本稿没有据此宣称整 Phi 面或 ordinary ISP 已完成。
