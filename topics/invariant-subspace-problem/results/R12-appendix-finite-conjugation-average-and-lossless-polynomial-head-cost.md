# R12 附录：有限共轭平均、真实多项式与无损截断成本

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / literature；AI-assisted，GPT-6 Astra Pro。

**状态：以下有限平均、准确多项式、无损成本上界与有限头成本提升均已证明。** 全部对象使用原加权 nilpotent 截断。多项式可有任意固定有限次数；压缩证明明确避开高次幂离开有限链后的返回。本文不从普通强稠密性推出平均保持某个未知输入的插值。

内部依赖：[R9](R9-radial-odometer-and-nilpotent-approximants.md)、[有限头最优成本](R12-appendix-contractive-deddens-core-and-exact-finite-head-cost.md)、[负幂域与等距共轭](R12-appendix-deddens-negative-domains-and-isometric-conjugation.md)。

## 1. 记号与已付接口

原算子为

$$
H=L^2(\mathbb Z_2,\mu),\qquad
A=M_wU,\qquad Uf(y)=f(y-1),
$$

$$
w(0)=0,\quad w(y)=\alpha_{v_2(y)}\ (y\ne0),\qquad
\alpha_j=\exp\left(
-\frac{280}{3}16^j+90\,8^j-300\,2^j+\frac{850}{3}
\right).
\tag{1.1}
$$

$w$ 连续，只有一个零点，$\|A\|=\alpha_0=e^{-20}<1$。置

$$
\beta_n=\|A^n\|=\prod_{a=1}^n\alpha_{v_2(a)},\qquad \beta_0=1.
\tag{1.2}
$$

Deddens 常数为

$$
c_A(X)=\inf\{C:\|A^\ell Xf\|\le C\|A^\ell f\|,
\ \ell\ge1,\ f\in H\}.
\tag{1.3}
$$

已付的共轭自同构是

$$
\Phi(X)=\overline{AXA^{-1}},
\qquad \Phi^{-1}(X)=A^{-1}XA,
$$

$$
c_A(\Phi^q(X))=c_A(X),\qquad
\|\Phi^q(X)\|\le c_A(X)\quad(q\in\mathbb Z).
\tag{1.4}
$$

逆幂均按实际定义域及有界延拓理解。若 $X$ 交换 $A$，则
$c_A(X)=\|X\|$。

固定 $m\ge0$、$N=2^m$，按 $y=r+Nz$ 分解

$$
H\simeq\mathbb C^N\otimes H_{\rm tail}.
\tag{1.5}
$$

低 $m$ 位下三角矩阵 $B=(b_{rs})$ 记为 $B^{\rm loc}=B\otimes I$。其精确成本公式为

$$
c_A(B^{\rm loc})=\max_{t\in\mathbb Z_2}\|C_B(t)\|,
$$

$$
C_B(t)_{rs}=
\begin{cases}
b_{rs}\dfrac{\beta_s}{\beta_r}
\displaystyle\prod_{a=s+1}^r w(t+a),&r\ge s,\\
0,&r<s.
\end{cases}
\tag{1.6}
$$

该最大值可精确化为至多 $2N$ 个有限端点矩阵范数；本稿使用的是这一已付最优常数，不改成另一个权或粗矩阵模型。

## 2. 有限共轭轨道与准确多项式

对 $0\le s\le r<N$，沿原正向链从输入数字 $s$ 到输出数字 $r$，没有越过 $N$ 的边界，权乘积恒为 $\beta_r/\beta_s$。因此

$$
B^{\rm loc}
=\sum_{0\le s\le r<N}
b_{rs}\frac{\beta_s}{\beta_r}
M_{\mathbf1_{\{y\bmod N=r\}}}A^{r-s}.
\tag{2.1}
$$

由 $AM_b=M_{b\circ\tau}A$，其中 $\tau(y)=y-1$，以及 $\operatorname{Ran}A$ 稠密，

$$
\Phi(M_b)=M_{b\circ\tau},\qquad \Phi(A^d)=A^d.
\tag{2.2}
$$

(2.1) 的全部乘法系数均为低 $m$ 位柱函数，周期为 $N$，故

$$
\Phi^N(B^{\rm loc})=B^{\rm loc}.
\tag{2.3}
$$

定义真正的有限平均

$$
\Pi_m(B^{\rm loc})
=\frac1N\sum_{q=0}^{N-1}\Phi^q(B^{\rm loc}).
\tag{2.4}
$$

周期性给 $\Phi(\Pi_m(B^{\rm loc}))=\Pi_m(B^{\rm loc})$，所以该平均交换 $A$。把 (2.1) 的每个模类指标沿完整周期平均，其均值为 $1/N$，得到准确公式

$$
\boxed{
\Pi_m(B^{\rm loc})
=\sum_{d=0}^{N-1}
\left[
\frac1N\sum_{s=0}^{N-1-d}
b_{s+d,s}\frac{\beta_s}{\beta_{s+d}}
\right]A^d.}
\tag{2.5}
$$

这不是一个未指定的弱极限，而是有限共轭和得到的原 $A$ 多项式。由 (1.4)，

$$
\boxed{
\|\Pi_m(B^{\rm loc})\|
=c_A(\Pi_m(B^{\rm loc}))
\le c_A(B^{\rm loc}).}
\tag{2.6}
$$

将同一个 $B^{\rm loc}$ 视为更高有限头上的矩阵时，新周期是 $N$ 的倍数，(2.4) 只重复已有周期，所以平均结果不变。可一致地记这个有限头平均为 $\Pi$。

平均没有保证保留 $B^{\rm loc}f$。若要由 (2.4) 保留指定输入上的插值，必须控制同一个 $f$ 在整个有限共轭轨道下的像，不能只控制 $q=0$ 的一项。

## 3. 原 nilpotent 截断及有限移位链

把原权在 $v_2(y)\ge m$ 处置零，得到原截断 $A_m$。在 (1.5) 下，

$$
A_m=J_N\otimes I,
$$

$$
J_Ne_s=
\alpha_{v_2(s+1)}e_{s+1}\quad(0\le s<N-1),
\qquad J_Ne_{N-1}=0.
\tag{3.1}
$$

这里 $J_N$ 是原加权 nilpotent 链，不是无权 Jordan 块。并且

$$
\|A-A_m\|=\alpha_m,\qquad
\|A_m\|\le\alpha_0.
\tag{3.2}
$$

对任意 $t\in\mathbb Z_2$，另定义有限链

$$
J_N(t)e_s=w(t+s+1)e_{s+1}\quad(s<N-1),
\qquad J_N(t)e_{N-1}=0.
\tag{3.3}
$$

若 $p(z)=\sum_{d=0}^D a_dz^d$ 是任意固定有限次数多项式，则

$$
\boxed{C_{p(J_N)}(t)=p(J_N(t)).}
\tag{3.4}
$$

证明：当 $r-s=d\ge0$ 时，$p(J_N)$ 的条目为
$a_d\beta_r/\beta_s$；代入 (1.6)，权比相消，恰得
$a_d\prod_{a=s+1}^r w(t+a)$。$d\ge N$ 的项在两个 nilpotent 矩阵中都为零。常数项给相同对角项，故 (3.4) 对全部 $D$ 成立。

## 4. 细圆柱压缩支付任意固定次数，避免高次返回

**引理。** 对每个 $N$、$t$ 和固定有限次数多项式 $p$，

$$
\|p(J_N(t))\|\le\|p(A)\|.
\tag{4.1}
$$

**证明。** 设 $\deg p\le D$。选不断增大的整数 $\ell$，满足

$$
2^\ell>N-1+D.
\tag{4.2}
$$

令

$$
E_{s,\ell}=t+s+2^\ell\mathbb Z_2,\qquad
e_{s,\ell}=2^{\ell/2}\mathbf1_{E_{s,\ell}}
\quad(0\le s<N).
\tag{4.3}
$$

这些圆柱互不相交，$e_{s,\ell}$ 正交归一。记
$V_\ell:\mathbb C^N\to H$ 为相应等距嵌入。

对 $0\le d\le D$，$A^de_{s,\ell}$ 支撑在
$t+s+d+2^\ell\mathbb Z_2$。由 (4.2)，该圆柱与某个
$E_{r,\ell}$ 相同当且仅当 $r=s+d$，且 $0\le r<N$。不存在高次幂离开所选链之后按模 $2^\ell$ 返回的情况。

若 $r=s+d$，矩阵系数为输出圆柱上原权乘积的平均：

$$
\langle A^de_{s,\ell},e_{r,\ell}\rangle
=
2^\ell\int_{E_{r,\ell}}
\prod_{a=0}^{d-1}w(y-a)\,d\mu(y).
\tag{4.4}
$$

由于 $w$ 连续，有限乘积在不断缩小的圆柱上趋于其在 $t+r$ 的值。因此

$$
\langle A^de_{s,\ell},e_{r,\ell}\rangle
\longrightarrow
\prod_{a=s+1}^r w(t+a).
\tag{4.5}
$$

其他位置为零；$d=0$ 为恒等矩阵。故

$$
V_\ell^*p(A)V_\ell\longrightarrow p(J_N(t))
$$

在有限维矩阵范数中成立。每个压缩范数不超过 $\|p(A)\|$，极限即给 (4.1)。零权端点也由连续性同样处理。证毕。

这里没有要求 $D<N$。当 $D\ge N$ 时，(4.2) 仍排除所有不应出现的返回项，而 $J_N(t)^d=0$ 的高次项也准确消失。

## 5. 原截断的无损 Deddens 成本与显式误差

由 (1.6)、(3.4)、(4.1)，

$$
\boxed{c_A(p(A_m))
=\max_t\|p(J_N(t))\|
\le\|p(A)\|.}
\tag{5.1}
$$

另一方面，$c_A(X)\ge\|X\|$，且 (3.2) 给 $p(A_m)\to p(A)$ 算子范数收敛。因此

$$
\boxed{\lim_{m\to\infty}c_A(p(A_m))=\|p(A)\|.}
\tag{5.2}
$$

每个成本仍由有限头的至多 $2N$ 个真实端点矩阵精确计算。

如果需要可核误差，令

$$
L_p=\sum_{d=1}^D d|a_d|\alpha_0^{d-1}.
$$

由幂差望远镜公式及 (3.2)，

$$
\|p(A)-p(A_m)\|\le\alpha_mL_p.
$$

结合 (5.1) 及 $\|p(A_m)\|\le c_A(p(A_m))$，得到

$$
\boxed{
c_A(p(A_m))
\le\|p(A)\|
\le c_A(p(A_m))+\alpha_mL_p.}
\tag{5.3}
$$

这控制的是原 $p(A)$ 的范数，不是另一个未支付相似常数的矩阵模型。

## 6. 真实多项式的有限头成本提升

若 $N>D$，由 (2.5) 与原链条目，

$$
\Pi_m(p(A_m))
=\sum_{d=0}^D\left(1-\frac dN\right)a_dA^d.
\tag{6.1}
$$

这显示平均不是无条件保留原插值：即便输入是截断多项式，其系数也出现明确的有限长度因子。

反过来，定义

$$
p_N(z)=\sum_{d=0}^D\frac{N}{N-d}a_dz^d,\qquad
B_N^{\rm loc}=p_N(A_m).
\tag{6.2}
$$

则准确有

$$
\boxed{\Pi(B_N^{\rm loc})=p(A).}
\tag{6.3}
$$

由无损界 (5.1)，

$$
\begin{aligned}
c_A(B_N^{\rm loc})
&\le\|p_N(A)\|\\
&\le\|p(A)\|+
\sum_{d=1}^D|a_d|\frac{d}{N-d}\beta_d.
\end{aligned}
\tag{6.4}
$$

对固定 $p$，右侧误差趋零。而 (2.6) 对任何满足
$\Pi(B^{\rm loc})=p(A)$ 的有限头下三角提升都给
$c_A(B^{\rm loc})\ge\|p(A)\|$。因此

$$
\boxed{
\inf_{\substack{B^{\rm loc}\text{ 为有限头下三角}\\
\Pi(B^{\rm loc})=p(A)}}
c_A(B^{\rm loc})
=\|p(A)\|.}
\tag{6.5}
$$

这个下确界结论针对固定真实多项式，未宣称某个有限头必然达到下确界，也没有扩展为任意 $X\in\mathcal D_A$ 的统一成本逼近定理。

## 7. 尚未支付的保输入问题

有限头成本公式和 (2.5) 给出了一个实际正向接口：可以在保留原权的有限凸约束中选择下三角来源，再用完整有限共轭轨道平均得到真正的 $A$ 多项式；(6.4) 还说明固定多项式可以几乎无损地提升回该有限模型。

但是，若只知道 $B^{\rm loc}f$ 接近目标 $g$，平均后的
$\Pi(B^{\rm loc})f$ 不必接近 $g$。全 $\mathcal D_A$ 单位球的强稠密性没有支付其他 $N-1$ 个共轭像。对于属于实际负幂域的 $f$，这些像是
$A^qB^{\rm loc}A^{-q}f$，必须保同一个输入及其真实原像。

下一步可以研究统一 $c_A$ 成本的有限头逼近是否存在，或在交换子类中进行保输入逼近并平均；本文只对固定有限次数多项式完成了无损成本和准确提升。未证明任意非零向量循环，未构造非零真闭普通不变子空间。
