# 工作接口：指定普通矩的完整临界截面与 Bell 分母的次数限制

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：有限完整代数证明；root 与 boundary 全文独立复核通过。只限制给定零纤维 Jacobian 理想中的特定分母；不作不循环或实际联合谱的结论。

本稿接[完整 ordinary Bell 的曲线临界簇](2026-11-13-complete-ordinary-bell-curve-critical-locus-and-symbol-denominator-boundary-1cf.md) §§1–6。
旧截面只保留零次、一次普通矩；这里允许任意指定有限普通矩，因此可以区分不同次数的**完整** first Bell 多项式。
所有幂和乘积的类型在下文保留。

## 1. 原合并坐标与有限普通矩

保留 $q$ 个归一连续对数模式、物理曲线
$$
v(z)=(1,z,\ldots,z^{q-1}),
$$
以及非零齐次二次式
$$
F(x)=\frac12x^{\mathsf T}Kx,\qquad K=K^{\mathsf T},\qquad
F(v(z))\equiv0.
\tag{1.1}
$$
六模式的原复二次例满足这些条件。

取非恒定标量多项式
$$
Q(\eta)=\sum_{j=0}^{n}q_j\eta^j,\qquad
\mathcal S=\{j\ge1:q_j\ne0\},\qquad G=Q(F).
$$
固定一个足够大的有限次数 $D\ge2n$；若还检验其它有限多项式，则同时令 $D$ 大于等于它们的次数。
沿用完整、已经合并的坐标
$$
W_{1,m}=x_m,\qquad
W_{d,m}\quad(2\le d\le D,\ 0\le m\le(q-1)d).
$$
填充而未出现在 $\mathcal Q_G$ 中的坐标，其偏导为零。

令 $\mu_0=1$，任取 $\mu_1,\ldots,\mu_D\in\mathbb C$。
在有限截断环 $\mathbb C[s]/(s^{D+1})$ 中定义
$$
M(s)=\sum_{j=0}^{D}\frac{\mu_j}{j!}s^j,\qquad
\log M(s)=\sum_{j=1}^{D}\frac{\kappa_j}{j!}s^j.
\tag{1.2}
$$
常数项为一，故有限对数存在且唯一；特别 $\kappa_1=\mu_1$。
这只是有限代数，不使用概率测度、收敛级数或无界指数算子。

对任意固定 $z_0\in\mathbb C$，规定显示点
$$
\boxed{
x=\mu_1v(z_0),\qquad
W_{d,m}=\frac{\kappa_d}{(-2)^{d-1}}z_0^m
\quad(2\le d\le D).
}
\tag{1.3}
$$
同一 $(d,m)$ 始终只有一个坐标，没有拆开相同物理行。

## 2. 在截面上的完整 ordinary 求值

定义有限线性泛函 $\mathbb E_\mu$ 于一变量次数至多 $D$ 的多项式上：
$$
\mathbb E_\mu[T^j]=\mu_j.
$$
它不被假定为正泛函。

对任何 $\deg H\le D$，原完整 ordinary 变换为
$$
\mathcal Q_H(x,W)=
\exp\left[
\sum_{d=2}^{D}\frac{(-2)^{d-1}}{d!}
\sum_mW_{d,m}\mathcal D_{d,m}
\right]H(x),
$$
其中
$$
\sum_m z^m\mathcal D_{d,m}=(v(z)\cdot\nabla)^d.
$$
把 (1.3) 代入，并把一次平移同有限微分算子合并，得到
$$
\begin{aligned}
\left.\mathcal Q_H\right|_{(1.3)}
&=\left.
\exp\left[\sum_{d=1}^{D}\frac{\kappa_d}{d!}
(v(z_0)\cdot\nabla)^d\right]H(x)\right|_{x=0}\\
&=\left.
\sum_{j=0}^{D}\frac{\mu_j}{j!}
(v(z_0)\cdot\nabla)^jH(x)\right|_{x=0}.
\end{aligned}
$$
所以
$$
\boxed{
\left.\mathcal Q_H\right|_{(1.3)}
=\mathbb E_\mu[H(Tv(z_0))].
}
\tag{2.1}
$$
这是完整有限生成式的恒等式，包含全部高矩。

## 3. 全部合并偏导的精确公式

记
$$
b(z_0,\zeta)=v(z_0)^{\mathsf T}K v(\zeta).
$$
由 (1.1) 的两个各向同性方向，
$$
F(Tv(z_0)+s v(\zeta))=Ts\,b(z_0,\zeta).
\tag{3.1}
$$
因此对每个 $d\ge1$，
$$
\mathbb E_\mu\!\left[
(v(\zeta)\cdot\nabla)^dG(Tv(z_0))
\right]
=d!\,q_d\mu_d\,b(z_0,\zeta)^d,
\tag{3.2}
$$
其中 $q_d=0$ 当 $d>n$。
原完整偏导公式与 (2.1) 给
$$
\boxed{
\left.
\sum_m\zeta^m\partial_{W_{d,m}}\mathcal Q_G
\right|_{(1.3)}
=(-2)^{d-1}q_d\mu_d\,b(z_0,\zeta)^d.
}
\tag{3.3}
$$
$d=1$ 时这里的偏导就是全部一次坐标 $\partial_{x_m}$，系数 $(-2)^0=1$；
$d\ge2$ 时保留原 $d!$ 和 $(-2)^{d-1}$，没有漏掉有序指标的重数。
通过比较 $\zeta$ 的有限系数，(3.3) 同时核验每一条实际合并键的偏导。

又由 $F(Tv(z_0))=0$，
$$
\left.\mathcal Q_G\right|_{(1.3)}=Q(0).
\tag{3.4}
$$
于是
$$
\boxed{
\mu_j=0\quad(j\in\mathcal S)
\ \Longrightarrow\
(1.3)\text{ 是完整 }\mathcal Q_G
\text{ 的临界点，临界值为 }Q(0).
}
\tag{3.5}
$$
若 $Kv(z_0)\ne0$，则 $b(z_0,\zeta)$ 不是零多项式，(3.3) 还说明 (3.5) 的矩条件是这个单方向截面内的必要条件。
本稿的分母排除只使用充分方向，故不需要额外的非退化假设。

## 4. 完整 first Bell 分母的次数限制

设
$$
\mathcal J_Q=
\left(
\mathcal Q_G-Q(0),
\ \partial_{x_m}\mathcal Q_G,
\ \partial_{W_{d,m}}\mathcal Q_G
\right)
$$
是同一有限完整显示环中的零纤维 Jacobian 理想。

取有限个非零齐次一次式 $a_i(x)$、正整数 $m_i,N_i$，并假设
$$
m_i\notin\mathcal S\qquad\text{对每个 }i.
\tag{4.1}
$$
把有限表填充到 $D\ge\max_i m_i$，仍不改变原 $\mathcal Q_G$。
选择普通矩
$$
\mu_0=1,\qquad
\mu_m=1\quad(m\in\{m_i\}),\qquad
\mu_j=0\quad\text{其余 }1\le j\le D.
\tag{4.2}
$$
(4.1) 保证全部支撑矩 $\mu_j$、$j\in\mathcal S$ 为零，因此得到 (3.5) 的临界点。

每个 $a_i(v(z))$ 是非零一变量多项式；有限多个这样的多项式可以同时避开其零点。
选这样的 $z_0$，(2.1) 给
$$
\left.\mathcal Q_{a_i^{m_i}}\right|_{(1.3)}
=\mu_{m_i}a_i(v(z_0))^{m_i}\ne0.
$$
所以
$$
\boxed{
\prod_i\big(\mathcal Q_{a_i^{m_i}}\big)^{N_i}
\notin\sqrt{\mathcal J_Q}.
}
\tag{4.3}
$$
理由只是：根理想中的多项式必在理想的每个共同零点上为零。
不需要反向 Nullstellensatz 或完整临界簇分类。

这里的 $\big(\mathcal Q_{a^m}\big)^N$ 是完整 ordinary Bell 多项式的**自然代数幂**，
不是 $\mathcal Q_{a^{mN}}$。
(4.3) 明确覆盖前一种类型。

在这个截面族内，对单个非零齐次 first，$\mathcal Q_{a^m}$ 恒为零当且仅当 $m\in\mathcal S$。
这句话只描述本截面；它不宣称那些匹配支撑次数的分母已经属于 Jacobian 根理想。

## 5. 原六模式各点态幂的含义

对 $Q(\eta)=\eta^h$，$\mathcal S=\{h\}$。
因此对每个 $h\ge1$、每个 $m\ne h$ 及非零齐次 first $a$，
$$
\boxed{
\big(\mathcal Q_{a^m}\big)^N
\notin\sqrt{\mathcal J_{F^h,0}}
\qquad(N\ge1).
}
\tag{5.1}
$$
特别，原 $F^2$ 已由[精确有理jet与真实Bell逆](../results/R150-appendix-six-mode-exact-jacobian-jets-and-all-square-fibers.md)闭合；其中可用的完整 Bell 平方分母，不能作为同类 Jacobian 分母直接搬到任意 $F^h$、$h\ne2$。
这个排除仍成立，即使该 first 的真实规范算子空谱、其完整 Bell 平方拥有全域有界逆。

例如 $h=3$，取 $x=0$，只让
$$
W_{2,m}=-\frac12z_0^m
$$
非零，其余高矩为零。
这对应单方向形式普通矩生成式 $M(s)=e^{s^2/2}$ 的有限截断，所有奇数矩为零。
(3.3) 给 $\mathcal Q_{F^3}$ 的完整零梯度，而完整平方的 $-2a^{\mathsf T}Ha$ 精确给
$$
\boxed{\mathcal Q_{a^2}=a(v(z_0))^2\ne0.}
$$

## 6. 保留的范围

当 $Q'(0)=0$ 且只取 $m_i=1$，本稿恢复旧的一次符号分母障碍。
真正新增的是对任意次数的**完整** first Bell 多项式及其有限自然幂乘积的区分。

没有排除支撑次数内的完整 Bell 分母、不同次数的线性组合、非 first 的 Bell 多项式、真实快累积量证书或其他算子证明。
(3.5) 只是完整普通矩的显示临界截面，不证明其坐标能由原实际联合谱实现。
本稿不推出非循环向量、不变子空间或普通 ISP 的结论。
