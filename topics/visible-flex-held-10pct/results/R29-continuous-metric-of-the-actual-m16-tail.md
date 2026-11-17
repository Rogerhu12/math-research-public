# R29. 实际 M16/steps64 尾的全连续、全角固定 g 误差界

会话：Astra-held10-7322d0de-20261118；共同工作 `closed_geometry`。2026-11-17 UTC。

## 结论与明确范围

对 R28 的同一个 M16/steps64 有限 C² 图，令 $g_0$ 是 R21、R27 定义的真实旋转背景度量。在整个有限尾 $b\le R\le r_{\rm cut}$、全部材料角及全部相位上，严格有

\[
 \left\|g_0^{-1/2}(F_\alpha^*g_{\mathbb R^3}-g_0)g_0^{-1/2}\right\|_{\rm op}
 \le\frac{590094565153063}{590295810358705651712}
 <10^{-6}.
\]

分数的浮点显示为 $9.996590773606874\times10^{-7}$。**这是按照 $10^{-6}$ 门槛停止区间细分所得的充分上界，其大小反映本次认证预算，不是实际误差最大值的估计。** 这里没有重新求解 BVP、改物理 g、改有限尾表示或用数值工厂归一化值替代真积分值。

圆领已由 R21/R28 给出连续 metric 界 $<1.36\times10^{-29}$，两顶固定帽对自己的固定度量误差为零，故尾、圆领和帽的这些门可以合并。**prefix 的连续同 g 误差仍待支付，本条不宣布全闭面的 metric 已通过，也不宣布本课题完成。**

## 1. 认证对象

使用 R28 原 M16 pair、36,892段有限尾及相同 outer-ulp reparametrization。manifest SHA-256 为
`0981145822b75bba0fa5af23754aa2b25d8a056d592796fc0c1358c01c312b58`。
尾 checkpoint SHA-256 为
`7d29ca238ddcd623659ccdae7814432a615ef85a89faae82970c93402add0c06`。

旋转背景直接采用 R27 的最终真积分证书
`a0358af3311b198312e32a96305e53e1210cabd2c652621ef233b07dbf111294`，
含同一固定参数的 $\lambda$、各 cell 真实积分及内端半径区间。所有参考量在真正的 $R$ 处求值：

\[
 g_0=(1+w(R)^2)\,dR^2+R^2d\theta^2.
\]

扰动仍在

\[
 r_V(R)=R+(c-r_{\rm cut})
 S_5\!\left(\left[\frac{R-(r_{\rm cut}-d)}d\right]_{[0,1]}\right),
 \qquad d=\text{原 binary64 的 } .02
\]

处取值。$R,r_V$ 没有混用。该映射严格递增，值、一阶和二阶链式项均进入本次界。半径归一化因子及累计节点由 `Fraction` 精确计算；有限导数数据为定义该图的原 binary64 常数。

## 2. 从真实部分积分到实际 $w(R)$

R21 已证明这个固定背景满足 $0\le w\le .41$、$|\kappa_r|\le8$。因此

\[
 |w_R|\le8(1+w^2)^{3/2}
 \le8(1+.41^2)^{3/2}<11.                         \tag{1}
\]

最后一个严格不等式也以有理数平方比较 $64(1+(41/100)^2)^3<121$ 检查。背景为 C² 图，故 $w$ 对真实 $R$ 是全局11-Lipschitz函数；该结论跨原分段界及 $|w_x|$ 的 cusp 仍成立。

数值工厂只给每个待查 $R_i$ 提议一个原段与参数 $x_i$。以 R27 的 cell0 真实内半径为起点，对所提议参数的有序格点累计

\[
 R(x_i)=R_{\rm inner}
 +\sum_{\rm previous\ pieces}\int(A+\lambda B)
 +\int_0^{x_i}(A+\lambda B).                       \tag{2}
\]

每个部分积分都使用 R27 的总变差端点式、未决 turning 子区间完整值域界及带四阶区间余项的 Simpson 公式；每段积分目标宽度为 $10^{-18}$。参数格不是 quadrature 误差估计的依据。区间加法、初等函数和所有系数运算均向外舍入。

由于 $w(x_i)$ 可从同一原公式直接区间求值，式 (1) 给出

\[
 w(R_i)\in w(x_i)+[-11,11]\bigl(R_i-[R(x_i)]\bigr). \tag{3}
\]

这是真实 $R_i$ 处的界，不把工厂的求逆残差当作真实半径残差。只要提议参数属于已定义的背景，式 (3) 本身就成立；错误或不精确的提议只会使区间变宽，不能产生错误认证。

本次共使用5034个中心，真实部分积分的5371个叶区间。所有提议中心的真实半径差上界最大为 $2.817301594554\times10^{-14}$。九段累计到外端的区间宽约 $4.10\times10^{-14}$，并严格包含固定的 $r_{\rm cut}$。

在全尾计算前，还在 $.2154422816672151$、$.28304471508506235$、$.29649762863045936$ 三个关键半径处，使用 $r_x>0$ 的区间下界验证左右严格不等式

\[
 \overline{R(x_i-h)}<R_i<\underline{R(x_i+h)}.
\]

所得逆参数区间宽分别小于 $1.513\times10^{-13}$、$3.968\times10^{-11}$、$3.884\times10^{-11}$。结合物理半径上的均值公式，真实 $w(R_i)$ 与数值工厂返回值的绝对差上界分别小于 $6.036\times10^{-14}$、$3.411\times10^{-14}$、$2.803\times10^{-14}$。全尾证明使用式 (3) 的更直接传播，不要求对每一个 stiff inverse 求出窄参数区间。

## 3. 有限 Fourier 的完整 metric 代数

写实际有限图的扰动为复平面分量 $P(R,\theta)$ 和实高度分量 $Z(R,\theta)$。例如上半的高度为 $Z_{\rm cap}-h(R)-Z(R,\theta)$。令 $E=1+w^2$。相对误差矩阵的三个分子恰为

\[
 A=2\Re(e^{-i\theta}P_R)+|P_R|^2+2wZ_R+Z_R^2,
\]

\[
 B=\Re(e^{-i\theta}P_\theta)
 +R\Im(e^{-i\theta}P_R)
 +\Re(P_R\overline{P_\theta})+(w+Z_R)Z_\theta,
\]

\[
 C=2R\Im(e^{-i\theta}P_\theta)+|P_\theta|^2+Z_\theta^2.
\]

因此相对误差矩阵为

\[
 M(R,\theta)=
 \begin{pmatrix}A/E&B/(R\sqrt E)\\ B/(R\sqrt E)&C/R^2\end{pmatrix}.  \tag{4}
\]

$P$ 的频率为 $1+3k$，$Z$ 的频率为 $3j$，所以 (4) 的全部项都属于有限 Laurent 频率 $3k$，最高绝对角频率至多192。本次**直接对完整 Laurent 系数卷积**，没有角网格、DFT 或 alias 推断。

设 (4) 的三个系数向量为 $a_k,b_k,c_k$。对任意 $\theta$，

\[
 \|M(R,\theta)\|_{\rm op}
 \le\max\left\{\sum_k|a_k|+\sum_k|b_k|,
               \sum_k|c_k|+\sum_k|b_k|\right\}.    \tag{5}
\]

这是实对称矩阵的绝对行和界与 Laurent 三角不等式。奇函数交叉项的系数是纯虚数，源码只保存其虚部实系数；绝对系数和完全相同。

逐项对 (4) 求 $R$ 导数，保留全部乘积和分母导数，得到 $\partial_RM$ 的同类全角界。这里只需要 $P,Z$ 的二阶径向 jets、$w,w_R$，与当前有限图的 C² 正则性相符，不假设三阶有限图收敛。

有限位置、一阶、二阶函数在每个径向段上使用 Bernstein 系数包围。对子区间先用 de Casteljau 限制再取控制点凸包；跨节点时取覆盖段的并集包围。位置的起点是对全部前置导数多项式的外向积分，不使用保存的显示位置代替该积分。

## 4. 连续径向覆盖的接受条件

对真实径向区间 $I=[l,r]$ 选一个严格内部中心 $R_i$，令

\[
 d_i=\max(R_i-l,r-R_i).
\]

先用式 (3) 与有限图的精确点系数，得到 (5) 的点界 $m_i$。在整个 $I$ 上，使用

\[
 w(I)\subseteq[w(R_i)]+[-11d_i,11d_i],\qquad
 w_R(I)\subseteq[-11,11],
\]

与 Bernstein 函数包围，得到 $\|\partial_RM\|_{\rm op}\le L_i$。由矩阵值函数的微积分基本定理，全部 $R\in I$、全部 $\theta$ 都满足

\[
 \|M(R,\theta)\|_{\rm op}\le m_i+d_iL_i.             \tag{6}
\]

只有将右端向外舍入后仍严格小于 $10^{-6}$，该区间才被接受；否则在真实 $R$ 坐标上二分并计算新的严格中心。新的中心部分积分从已认证参数格点继续累计，不替换背景或有限图。

cell0 原有4612个区间。第一轮211段尚未通过，其中最大尝试界为 $1.91348599161\times10^{-6}$；这些只是过宽的充分界，不是违反门槛的证明。二分一次后的422个子区间全部通过。最终4823个区间的精确有理端点首尾相接，从内分界一直覆盖到真正的 $r_{\rm cut}$，无遗漏区间。

物理相位作用为材料角平移加空间转动，均保留相对度量范数；因此全角结论同时覆盖 $0\le\alpha\le\pi/3$。

## 5. 七个深 cell 的独立连续界

深 raw cells 1至7不需要依赖接近零的 metric 抵消。将 Bernstein 系数分别求绝对和，记平面/高度径向界为 $p,z$，角向界为 $p_t,z_t$，真实半径范围为 $[r_-,r_+]$。R21 在 cell0 以内有 $w\le1/49$；本有限内分界与真实 cell0 内半径之间的差已经由 R27 及式 (1) 支付。整个七-cell 范围因此可统一取 $W=.021$。

由第3节分子式和 $E\ge1$，可取三个非负界

\[
 A_* =2p+p^2+2Wz+z^2,
\]

\[
 B_* =\frac{p_t+r_+p+pp_t+(W+z)z_t}{r_-},
 \qquad
 C_* =\frac{2r_+p_t+p_t^2+z_t^2}{r_-^2}.
\]

则相对 operator 误差至多 $\max(A_*+B_*,C_*+B_*)$。所有系数和先向外求界，之后标量预算用精确有理数合并。各 raw cell 的上界显示为：

| raw cell | 连续全角相对 operator 上界（显示） |
|---|---:|
| 7 | $7.557124\times10^{-27}$ |
| 6 | $1.075887\times10^{-20}$ |
| 5 | $2.882260\times10^{-16}$ |
| 4 | $5.801344\times10^{-13}$ |
| 3 | $3.501668\times10^{-11}$ |
| 2 | $1.128090\times10^{-9}$ |
| 1 | $1.251845\times10^{-7}$ |

这些连续区间与第4节的浅区间精确衔接，得到开头的整个有限尾界。

## 6. 浮点卷积的外向包围与执行来源

基础区间运算沿用 R23 的 `nextafter` 核。有限卷积对每个输入区间选择一个 binary64 中心，并向外包围其半径。真实卷积与中心卷积之差由

\[
 r_a*|b_c|+|a_c|*r_b+r_a*r_b
\]

控制。每个卷积系数至多含 $n$ 个乘积与 $n-1$ 次加法；使用 $8nu$ 的保守舍入系数及 subnormal 绝对补项，包围中心卷积和上述非负辅助卷积，再向外合并。这里 $u=2^{-53}$，所有实际长度远小于使该界失效的范围。因而 NumPy 卷积的返回值不是直接被当成精确系数。

本次完成时间93.93秒，正式输出 SHA-256 为
`09fe17ffb99467ae7688215636d29c2eb8a7db2f151284e1008f718d7f1fc732`。
输出另保存真实背景格与全部接受区间的 scratch 哈希；可再生数组及逐区间表不入 Git。源码及完整执行记录为：

- [certify_background_queries.py](../scripts/resume_closed/certify_background_queries.py)：真实部分积分、三个局部严格逆区间及物理半径传播。
- [interval_tail_metric.py](../scripts/resume_closed/interval_tail_metric.py)：实际有限表示的外向 Bernstein/链式界和完整 Laurent metric 代数。
- [certify_continuous_tail_metric.py](../scripts/resume_closed/certify_continuous_tail_metric.py)：深段连续界、真实背景格和全部径向接受条件。
- [continuous_tail_metric_execution.json](../scripts/resume_closed/continuous_tail_metric_execution.json)：实际命令及输入、源码、输出哈希。

主命令如下；`CONSTANTS`、`BACKGROUND_CERTIFICATE` 由 R27 产生，其余输入是 R28 的同一来源与 manifest。

```bash
python topics/visible-flex-held-10pct/scripts/resume_closed/certify_continuous_tail_metric.py \
  --manifest M16_STEPS64_MANIFEST --tail-reader TAIL_READER \
  --constants CONSTANTS --background-certificate BACKGROUND_CERTIFICATE \
  --source-topic SOURCE --checkpoint M16_TAIL_CHECKPOINT \
  --threshold 1e-6 --piece-width 1e-18 --out SCRATCH/continuous-metric.json
```

本条完成的是同一实际有限尾此前未支付的连续同 g 门。R28 的全域几何、固定帽与非全等性结论继续适用；prefix 的连续 metric 及真正增幅仍需继续完成。
