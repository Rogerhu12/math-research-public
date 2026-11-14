# Sigma 的补空间改变、惰性 size 与整数乘法恒等式

后续 [R38](../results/R38-exact-inert-sigma-size-and-jet-budget.md) 已把这里的惰性上界加强为准确半径和 size，并给出无限分母列及完整 jet 渐近。

**可信度：已证明的后续边界。** 日期：2026-11-12。沿用 fixed-sigma-height-and-inert-denominator 笔记的 $E,\omega,t,D,\Sigma$，置 $z(t)=\log_E(t)$。本笔记不改变 R36 的原始 Coleman 生成元。

## 1. 改变二次正规化不能消去惰性的 size 损失

特征零下，首项为 $t$ 的全部奇级数解
$$
D^2\log\sigma_c=-x+c
$$
准确为
$$
\sigma_c(t)=\Sigma(t)\exp\bigl(cz(t)^2/2\bigr).
\tag{1.1}
$$
由两解之比的对数二阶导数为 $c$，奇性消掉一次项、首项消掉常数项，立即得到 (1.1)。

**命题 1。** 对任意惰性 $p\ge7$ 及任意 $c\in\mathbb Q_p$，$\sigma_c$ 在 $p$ 处有正收敛半径，其图像的 Bost–Chambert-Loir size 满足
$$
\boxed{\quad S_p(\operatorname{graph}\sigma_c)\le p^{-1/(p+1)}.\quad}
\tag{1.2}
$$

**证明。** 正半径由 $\Sigma,z$ 的正半径及充分小圆盘上的指数收敛得到。若 $c\in\mathbb Z_p$，则 $z$ 到 $t^p$ 次的系数为 $p$ 整数：其非零项次数为 $4j+1$，而 $p\equiv3\pmod4$，所需这些次数都不被 $p$ 整除。计算 $\exp(cz^2/2)$ 到 $t^{p+1}$ 次只用至多 $(p+1)/2<p$ 次幂，故所有阶乘都是 $p$ 单位。这些指数系数于是全部 $p$ 整。

前一笔记的 $\Sigma$ 在 $t^{p+2}$ 前全部整，而
$$
v_p([t^{p+2}]\Sigma)=-1.
$$
与上述整数级数相乘，唯一非整贡献仍来自此项。因此
$$
v_p([t^{p+2}]\sigma_c)=-1.
$$
若 $v_p(c)<0$，因 $z=t+O(t^5)$、$\Sigma=t+O(t^5)$，有
$$
[t^3]\sigma_c=c/2.
$$
其赋值至多为 $-1$。两种情形分别给第一 Newton slope 至多
$-\log p/(p+1)$ 或 $-\log p/2$。由 $\sigma_c'(0)=1$ 和 Bost–Chambert-Loir Proposition 3.5(2)，得到 (1.2)。证毕。

若另乘一个固定 $A(t)\in\mathbb Q[[t]]$，满足 $A(0)=1$ 且在 $\mathbb Q(t)$ 上代数，则除有限多个素数外 $A\in\mathbb Z_p[[t]]$（Eisenstein 分母定理）。对这些素数，上述首个非整项的证明原样适用，故 $A\sigma_c$ 也满足 (1.2)。特别是固定的有理模型改变或在 $O$ 处非零的固定代数因子，不能修复这一惰性损失。

这只处理 (1.1) 及固定代数乘法修正；没有声称排除任意更复杂的新算术对象。

## 2. 整数乘法确实消掉 sigma，但同时消掉了所求高度

对正整数 $m\ge2$，令 $\Psi_m\in\mathbb Q(E)^\times$ 为由
$$
\operatorname{div}\Psi_m
=[m]^*(O)-m^2(O),\qquad
\Psi_m(t)=m\,t^{1-m^2}+\cdots
\tag{2.1}
$$
规定的除法函数。这个首项规范尤其给 $\Psi_2=-2y$，勿混用首项为 $-2$ 的常见 $2y$ 约定。

则对每个 $c$ 都有完全相同的恒等式
$$
\boxed{\quad
\frac{\sigma_c([m]t)}{\sigma_c(t)^{m^2}}=\Psi_m(t).
\quad}
\tag{2.2}
$$

**证明。** 先取 $c=0$ 并作复一致化。前一笔记的特征零唯一性将 $\Sigma(t(z))$ 识别为对应周期格的经典 Weierstrass $\sigma(z)$。其准周期公式使 $\sigma(mz)/\sigma(z)^{m^2}$ 为椭圆函数：指数因子准确相消，符号因子因 $m^2-m$ 为偶数而相消。该函数的除子和原点首项恰为 (2.1)，故等于 $\Psi_m$。这是有理形式级数恒等式，所以在每个局部域都成立。

对于一般 $c$，由 $z([m]t)=m z(t)$，
$$
\frac{\exp(cz([m]t)^2/2)}
{\exp(m^2cz(t)^2/2)}=1,
$$
所以 (2.2) 不变。证毕。

因此仅验证全部整数乘法分布关系不能识别二次正规化常数 $c$。在对数层面，这些关系恰好杀掉一个二次高度的 $m^2$-齐次部分；把 (2.2) 的右侧变成代数数并用 Baker 非零，不能直接恢复已经被算子消掉的严格高度。

## 3. 复侧的完整延拓确实存在

设 $\mathcal L$ 为 $(E,\omega)$ 的周期格。由经典 sigma 的乘积和准周期公式，
$$
s_c(z):=\Sigma(t(z))\exp(cz^2/2)
=\sigma_{\mathcal L}(z)\exp(cz^2/2)
$$
在整个复平面上延拓为整函数，零点准确为 $\mathcal L$，均为单零点。它的增长阶数为 $2$。

具体证明如下。将任意 $z$ 写成一个固定紧基本平行四边形中的点加格点；准周期乘子是关于格点坐标的至多二次指数，故
$|s_c(z)|\le\exp(O_c(1+|z|^2))$。另一方面，半径 $R$ 圆盘内格点数为 $\asymp R^2$，Jensen 公式使整函数的增长阶数至少为 $2$。因此恰为 $2$。

于是复延拓本身没有缺失。限制来自 §1 的有限处：任取一族 $c_p\in\mathbb Q_p$，其惰性 size 上界仍不可求和。不能把“固定 sigma、整复延拓、普通处全整”三项直接合并成全局代数化。

## 来源

- 本目录 2026-11-12-fixed-sigma-height-and-inert-denominator.md：固定级数、惰性首个分母和正半径。
- J.-B. Bost、A. Chambert-Loir，*Analytic curves in algebraic varieties over number fields*，Proposition 3.5(2)、Corollary 3.9 前的 Eisenstein 讨论，[原文](https://arxiv.org/pdf/math/0702593)。这里所有 size 都指该文的实际图像 size。
- NIST DLMF，[§23.2](https://dlmf.nist.gov/23.2)，式 23.2.6–8 及 23.2.15–17 的 sigma、zeta、准周期公式；[§23.10](https://dlmf.nist.gov/23.10)，式 23.10.10 亦直接核对 $\Psi_2=-2y$ 的符号。本文从这些公式给出 (2.2) 和增长阶数的证明。
