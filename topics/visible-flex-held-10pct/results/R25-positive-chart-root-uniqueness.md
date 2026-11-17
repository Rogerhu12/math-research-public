# R25. 正 A 图内完整有限动量根的全局唯一性与残差界

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。以下为**已证明的有限维命题**，用于判断局部根重试是否改变已选正 A 分支；不宣称任意高度边界都有完整非线性尾。

固定 $r,w>0$、$E=1+w^2$ 及已给定实有限高度系数 $Q$ 决定的实角场 $P$、$T=P_u$。设 $\phi_0=1,\phi_1,\ldots,\phi_M$ 是所用完整实 Fourier 基，$L=\sum l_j\phi_j$，并记

$$K=L-T,\qquad S=1-w^2P^2,\qquad D=1-w^2(2K+K^2+EP^2),\qquad A=1+L+w^2T.$$

设内积为精确周期积分，或正权有限求积；Gram 矩阵 $\Gamma=(\langle\phi_i\phi_j\rangle)$ 正定。原均值及非均值方程为

$$\mathcal M_i(l)=\left\langle\frac{\omega-1}{w^2}\phi_i\right\rangle=t_i,\qquad
\omega=D^{-1/2}\left(1+\frac{w^2(1+K)T}{S}\right).$$

其中 $t_0=0$；绝不能删掉该均值方程。以下所有条件均施加在内积所用角域上，因此固定求积命题不冒充全角命题。

## 命题

对任意 $a,d,s>0$，集合

$$\mathcal U=\{l:A>a,\ D>d,\ S>s\}$$

是凸集（可能为空）。在 $\mathcal U$ 内 $\mathcal M$ 是单射，而且任意 $l_0,l_1\in\mathcal U$ 满足

$$\|l_1-l_0\|_2\le
\frac{E^{3/2}}{a\lambda_{\min}(\Gamma)}
\|\mathcal M(l_1)-\mathcal M(l_0)\|_2.$$

特别地，同一完整目标 $t$ 在同一正 A 图里至多有一个根。若两个数值根的完整 moment 残差分别不超过 $\varepsilon_0,\varepsilon_1$，则其系数差不超过右侧常数乘 $(\varepsilon_0+\varepsilon_1)$。

## 证明

$S$ 与 $l$ 无关。$A>a$ 在每个角上是 $l$ 的线性半空间。又

$$D=E-w^2\bigl((1+L-T)^2+EP^2\bigr).$$

所以 $D>d$ 是线性函数 $1+L-T$ 的一个开区间约束，或空约束；亦可直接看作凹二次函数的严格超水平集。因此上述所有角约束的交集凸。连续角情形的统一严格余量同样给凸域。

固定 $P,T$ 对 $L$ 求导。利用

$$D+w^2(1+K)^2=ES,$$

有

$$\frac{\partial}{\partial L}\frac{\omega-1}{w^2}
=\frac{1+K}{D^{3/2}}\left(1+\frac{w^2(1+K)T}{S}\right)+\frac{T}{S\sqrt D}
=\frac{(1+K)+ET}{D^{3/2}}=\frac{A}{D^{3/2}}.$$

故完整 Jacobian 为

$$G_{ij}(l)=\left\langle\frac{A}{D^{3/2}}\phi_i\phi_j\right\rangle.$$

在域内 $D\le E$、$A>a$，因而对每个向量 $z$，

$$z^TG(l)z\ge\frac{a}{E^{3/2}}z^T\Gamma z
\ge\frac{a\lambda_{\min}(\Gamma)}{E^{3/2}}\|z\|_2^2.$$

令 $v=l_1-l_0$。连接线段全在 $\mathcal U$，积分微分恒等式得到

$$v^T\bigl(\mathcal M(l_1)-\mathcal M(l_0)\bigr)
=\int_0^1v^TG(l_0+tv)v\,dt
\ge\frac{a\lambda_{\min}(\Gamma)}{E^{3/2}}\|v\|_2^2.$$

再用 Cauchy–Schwarz 即得所述界；目标相同时得到 $v=0$。数值残差推论由三角不等式直接成立。证毕。

在当前均匀 $N$ 点、$\phi_j=\sqrt2\cos(3j\theta)$ 的实现中，$N>6M$ 已保证 $\Gamma=I$；实际原门更强，要求 $N>12M$。证明针对精确实数代数与已说明的积分/求积；浮点舍入误差仍须单独计入。

## 对局部重试的作用和边界

原 `root` 从其线性 target 作初值，该初值可能落在正 A 域外，即使域内存在解。用 $\lambda(Q,\pi)$ 从零状态延拓、每一步仍调用原 Newton/root/guard，可以提供另一初值。只要最终返回完整目标且通过原残差和 D/S/A 门，它不能在此凸域内返回另一个不同的精确根。此命题不保证整个 $\lambda$ 路径可解，更不保证全局 shooting、前缀 BVP、闭合或 10% 比例；失败时保留原错误。
