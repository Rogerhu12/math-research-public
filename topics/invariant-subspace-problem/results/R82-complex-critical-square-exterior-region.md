# R82：临界平方组合的复系数外部区域

日期：2026-11-12（UTC）。经主会话逐段核验。

**状态：已证明的中间结论；完整 ISP 尚未完成。**

本条是 [正实系数联合尾比较](../notes/2026-11-12-positive-critical-square-joint-bound-0c-agent.md) 的独立扩展。复系数产生的 Gaussian 线性项完整保留并完成平方；不能只把实系数结论中的 $c$ 换成 $|c|$。

## 1. 结论

取
$$
1<p\le17/10,\qquad q=2p-1\le12/5,\qquad c\ne0.
$$
令 $(a_q,b_q)$ 为已认证的纯 $q$ 尾区间，并取其有理负余量：
$$
(a_q,b_q,\kappa_q)=
\begin{cases}
(1,20,13/100),&1<q\le2,\\
(1/10,30,1/2000),&2<q\le12/5.
\end{cases}
$$
定义
$$
C_0(q)=\frac{2\arctan(b_q-1)+\pi/2}{q},
\qquad
C_1(p,q)=\frac{\sqrt{a_qb_q}}
{4\kappa_q(p-1)^2}.
\tag{1.1}
$$
令 $\phi=\arg c\in[-\pi,\pi]$。

**定理 1.1。** 若
$$
\boxed{|c|>C_0(q)+C_1(p,q)\sin^2(\phi/2),}
\tag{1.2}
$$
则实际算子
$$
\boxed{L_p^2+cL_q}
$$
单射且值域稠密。

正实方向的相位罚项为零，恢复前稿的明确正实阈值；所有复方向在
$|c|>C_0+C_1$ 时都得到统一保证。这里没有声称中间有界区域已被覆盖。

## 2. 复时间使纯 $q$ 尾保持正实

仍记
$$
V_m=C_{p,m}^2+cC_{q,m},\qquad M=m+2.
$$
对 $v\in[a_q,b_q]$ 取
$$
t=\frac{vM^q}{c}.
\tag{2.1}
$$
于是 $\bar t\,\bar c=vM^q$。Gaussian 整函数恒等式给
$$
e^{-\bar tV_m^*}1
=
\sqrt{\frac{M}{4\pi}}
\int_{\mathbb R}e^{-My^2/4}
\exp\!\left[
iM^p\sqrt{\frac v{\bar c}}\,y C_{p,m}^*
-vM^q C_{q,m}^*
\right]1\,dy.
\tag{2.2}
$$
这里使用 $q+1=2p$。任意一致选择的平方根均可；改变平方根符号等于 $y\mapsto-y$。对每个有限 $m,v$，Gaussian 压过算子指数的线性增长，故该 Bochner 积分绝对收敛。

令
$$
x_{j,m}=(j+2)/M,\qquad
a_j=vx_{j,m}^{-q},
\qquad
b=-i\sqrt{v/\bar c}.
$$
积分内的第 $j$ 位范数平方为
$$
P_{\mathbb C}(a_j+b yx_{j,m}^{-p}).
$$
因为 $a_j$ 是实数，
$$
\boxed{
P_{\mathbb C}(a_j+b yx^{-p})
=P(a_j)+(a_j-1)\Re(b)\,yx^{-p}
+\frac{|b|^2y^2x^{-2p}}2.}
\tag{2.3}
$$
这就是必须保留的线性相位项。

## 3. 完成平方的有限 $m$ 比较

定义
$$
A_m(v)=\frac1M\sum_{j\ge m}
\frac{x_{j,m}^{-2p}}{P(vx_{j,m}^{-q})},
$$
$$
B_m(v)=\frac1M\sum_{j\ge m}
\frac{(vx_{j,m}^{-q}-1)x_{j,m}^{-p}}
{P(vx_{j,m}^{-q})},
$$
$$
\Gamma_m(v)=|b|^2A_m(v),\qquad
\Lambda_m(v)=\Re(b)B_m(v).
\tag{3.1}
$$
由 $\log(1+z)\le z$ 对实 $z>-1$，式 (2.3) 给积分内向量相对于纯 $q$ 尾向量的范数比
$$
\le
\exp\left[\frac M2\Lambda_m(v)y
+\frac M4\Gamma_m(v)y^2\right].
$$
此处即使线性项为负也合法，因为原来的比值始终为正。

若 $\Gamma_m(v)<1$，对 Gaussian 完成平方，得到真实的有限 $m$ 不等式
$$
\boxed{
\|e^{-\bar tV_m^*}1\|
\le
F_{q,m}(vM^q)
\frac{
\exp\!\left[\dfrac{M\Lambda_m(v)^2}
{4(1-\Gamma_m(v))}\right]}
{\sqrt{1-\Gamma_m(v)}}.
}
\tag{3.2}
$$
所有相位影响都在 $\Lambda_m(v)^2$ 中，没有被隐含在常数内。

## 4. 统一控制两个系数

令 $R=|c|$。平方根的两个实不变量为
$$
|b|^2=\frac vR,\qquad
(\Re b)^2=\frac vR\sin^2(\phi/2).
\tag{4.1}
$$
临界代换与正实稿相同：
$$
\Gamma_m(v)\longrightarrow
\frac1{qR}\int_0^v\frac{dz}{P(z)}
$$
在认证区间上一致。这一步可保留明确的有限 $M$ 余量：令
$$
C_{q,b}=2+\frac{4b_q q(1+b_q)}{2q+1}.
$$
对 $f_v(x)=x^{-(q+1)}/P(vx^{-q})$，直接求导并用
$P\ge1/2$、$|P'(z)|\le1+b_q$ 得
$\int_1^\infty|f_v'(x)|\,dx\le C_{q,b}$。逐区间的和积分比较遂给
$$
\left|
\Gamma_m(v)-\frac1{qR}\int_0^v\frac{dz}{P(z)}
\right|
\le\frac{b_qC_{q,b}}{RM}.
\tag{4.2a}
$$
因此
$$
\sup_v\limsup_m\Gamma_m(v)\le C_0(q)/R.
\tag{4.2}
$$
条件 (1.2) 保证 $R>C_0$，故分母有统一正余量。
具体地，取 $M\ge2b_qC_{q,b}/(R-C_0)$ 即保证
$1-\Gamma_m(v)\ge(R-C_0)/(2R)>0$，所以每个实际有限 $M$ 的
Gaussian 完成平方都合法；继续令 $M\to\infty$ 时，其分母一致趋向相应的严格正极限。

另外，精确初等不等式
$$
\frac{|z-1|}{P(z)}
=\frac{2|z-1|}{1+(z-1)^2}\le1
$$
给
$$
|B_m(v)|
\le\frac1M\sum_{j\ge m}x_{j,m}^{-p}
\le\frac1{p-1}+\frac1M.
\tag{4.3}
$$
将 (4.1)—(4.3) 代入 (3.2)，得到一致的联合尾指数界
$$
\boxed{
\frac1M\log\|e^{-\bar tV_m^*}1\|
\le h_q(v)
+\frac{v\sin^2(\phi/2)}
{4(p-1)^2(R-C_0(q))}
+o(1).}
\tag{4.4}
$$
正实方向 $\phi=0$ 时，额外项严格消失。

## 5. 负 BW 与实际核结论

R77 对任意固定复时间方向均保留真实误差，并给
$M+o(M)$ 次的头多项式。故 (4.4) 可以直接代入实际核分离。

纯 $q$ 尾的严格证书给
$$
J_q=g+\int h_q\,d\nu\le-\kappa_q.
$$
谐测的第一矩为
$$
\int v\,d\nu(v)=\sqrt{a_qb_q}.
$$
所以新的 BW 指数至多
$$
-\kappa_q+
\frac{\sqrt{a_qb_q}\sin^2(\phi/2)}
{4(p-1)^2(R-C_0(q))}.
$$
条件 (1.2) 正好使它严格为负。因此所有实际核向量的均值为零；$A$ 不变性与 $A^*$ 的常函数循环性迫核为零。复对称性给稠密值域。定理得证。

## 6. 未覆盖范围

本条给外部区域及靠近正实方向的更优阈值。它不宣称与 R75 的小型区域无缝相接；临界中间参数仍需别的估计。

这里仅处理平方临界关系 $q=2p-1$，因为 Gaussian 二次恒等式和精确代换均在这一关系下使用。更高次主面不能未经新的积分表示与范数证明就照搬这些常数。

所列结论继续依赖纯 $q$ 尾已经认证的负积分范围；没有把 $q$ 的上限从 $12/5$ 扩大。

