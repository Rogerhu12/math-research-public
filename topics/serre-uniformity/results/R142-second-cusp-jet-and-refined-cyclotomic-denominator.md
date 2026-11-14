# R142：尖点第二项消去与更强的实际分母理想

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明。** 始终保留 R69/R72 的实际秩零商存在这一前提，准确地说，实际三次角色有一个非零的水平 $p$ 中心值。变化导子下全部中心值共同为零的分支仍然开放。

R137 使用两条微分的常数项，证明实际分母参数的赋值不超过三色共同理想的深度。本篇使用它们的第二项：一个整线性组合使该项**精确为零**，因此形式积分要求新的圆分行列式具有两倍深度。这个消去不除以 $a_2(g)$，也不假定 $a_2(g)$ 非零或是剩余特征的单位。结论是一个只依赖 $p$、比 R137 更小或相同的分母上界整数；没有证明一般 exceptional 集为空。

## 1. 实际前提和两个圆分理想

沿用 [R137](R137-cyclotomic-denominator-depth-and-effective-bound.md) 的全部设置。具体而言，$p>37$，$E/\mathbb Q$ 无 CM，
$$
\rho_{E,p}(G_{\mathbb Q})=N_{\mathrm{ns}}(p),\qquad
\rho_{E,p}(I_p)=C^3\subsetneq C.
$$
写 $K$ 为真实二次商域，$\eta$ 为真实三次角色，并假设有归一化水平 $p$ 权二新形式 $g$、平凡 nebentype，满足
$$
L\left(\tfrac12,\pi_{g,K}\otimes\eta\right)\ne0.
\tag{142.1}
$$
R69/R72 给所需配对分支上的最优商 $q:J\twoheadrightarrow A$，$A(\mathbb Q)$ 有限，并给实际饱和整微分格。

对于任意 $F/\mathbb Q$，$F[p]\simeq E[p]$，写
$$
\operatorname{den}(j(F))=D^p,\qquad D\in\mathbb Z_{\ge1}.
$$
若 $\ell\mid D$，则 R2/R72 给
$$
\ell\equiv\varepsilon_K(\ell)\pmod p,\qquad
\ell\ge2p-1>p+1.
\tag{142.2}
$$

取 $\tau^2=-3$，三次角色 $\chi$ 和 $B_0,B_1,B_2$ 如 R137。设
$$
u_i=\sum_{b\in B_i}\zeta_p^b,\qquad
\theta=\zeta_p+\zeta_p^{-1},\qquad
L^+=\mathbb Q(\theta),\qquad \mathcal O^+=\mathbb Z[\theta],
$$
$$
A=A_p(\theta)=u_0,\qquad
B=B_p(\theta)=\frac{u_1-u_2}{\zeta_p-\zeta_p^{-1}},\qquad
\mathfrak J=(A,B).
\tag{142.3}
$$
记 $\sigma_2(\zeta_p)=\zeta_p^2$；它限制为 $L^+$ 的自同构。定义明确的实圆分整数
$$
\boxed{W_p=\theta A\sigma_2(B)-\sigma_2(A)B\in\mathcal O^+.}
\tag{142.4}
$$
它可直接由整数多项式计算：
$$
W_p=W_p(\theta),\qquad
W_p(T)=T A_p(T)B_p(T^2-2)-A_p(T^2-2)B_p(T).
\tag{142.5}
$$
可在 $\theta$ 的最小多项式模下约化；本证明不要求 $W_p\ne0$。

置
$$
\mathfrak K_p=\mathfrak J^2+(W_p)
=(A^2,AB,B^2,W_p).
\tag{142.6}
$$
对于每个非零素理想 $\lambda\subset\mathcal O^+$，采用 $v_\lambda(0)=+\infty$，定义
$$
\begin{aligned}
r_\lambda^{[2]}
&=\left\lfloor\frac{v_\lambda(\mathfrak K_p)}2\right\rfloor\\
&=\min\left(v_\lambda(\mathfrak J),
             \left\lfloor\frac{v_\lambda(W_p)}2\right\rfloor\right),\\
\mathfrak J_p^{[2]}&=\prod_\lambda\lambda^{r_\lambda^{[2]}},\qquad
N_p^{[2]}=\operatorname N_{L^+/\mathbb Q}(\mathfrak J_p^{[2]}).
\end{aligned}
\tag{142.7}
$$
因为 $A\ne0$，$\mathfrak J$ 和 $\mathfrak K_p$ 均为非零理想，乘积仅有有限个非零指数，$N_p^{[2]}$ 为正整数。如果 $W_p=0$，定义自动给 $\mathfrak J_p^{[2]}=\mathfrak J$。

**定理 142.1。** 在 (142.1) 和上述实际前提下，对每个 $\ell\mid D$，存在 $L^+$ 的一个 $\ell$ 上方素理想 $\lambda$，使得
$$
\boxed{
v_\lambda(\mathfrak J)\ge v_\ell(D),\qquad
v_\lambda(W_p)\ge2v_\ell(D).
}
\tag{142.8}
$$
两个不等式在**同一个实际尖点选出的同一个 $\lambda$** 上成立。因此
$$
\boxed{D\mid N_p^{[2]},\qquad N_p^{[2]}\mid N_p,}
\qquad N_p=\operatorname N(\mathfrak J),
\tag{142.9}
$$
并且
$$
\boxed{D^2\mid\operatorname N(\mathfrak K_p).}
\tag{142.10}
$$

特别，若某 $\ell\equiv\pm1\pmod p$ 的所有上方素理想中，每个满足 $v_\lambda(\mathfrak J)>0$ 的 $\lambda$ 都有 $v_\lambda(W_p)=1$，则 $\ell$ 不可能整除实际 $D$。不能将两个不同 $\lambda$ 上的单项高赋值拼成 (142.8)。

## 2. 精确消去第二项的形式积分引理

**引理 142.2。** 令 $R$ 为 $\mathbb Q_\ell$ 有限未分歧扩张的整数环，$\ell>3$，并允许任意有限扩张 $R'/R$。设 $h:\operatorname{Spf}R[[z]]\to\widehat{\mathcal A}$ 为阿贝尔概形的整形式态射，$h(0)=0$。取 $z_0\in R$，
$$v_\ell(z_0)=m\in\mathbb Z_{\ge1},\qquad h(z_0)=0,$$
所有赋值以 $v_\ell(\ell)=1$ 归一化。若某个整不变微分的拉回满足
$$
h^*\omega=(c_0+0\cdot z+c_2z^2+c_3z^3+\cdots)\,dz,
\qquad c_i\in R',
$$
则
$$v_\ell(c_0)\ge2m.$$

**证明。** 特征零形式对数给同一条微分的原函数。由 $h(z_0)=h(0)$，
$$
0=c_0z_0+\sum_{n\ge3}\frac{c_{n-1}}n z_0^n.
\tag{142.11}
$$
对每个 $n\ge3$，有 $v_\ell(n)\le n-3$：$n=3,4$ 时为零；若 $k=v_\ell(n)\ge1$，则 $n\ge5^k\ge k+3$。故
$$
v_\ell(c_{n-1}z_0^n/n)
\ge nm-v_\ell(n)
\ge3m+(n-3)(m-1)\ge3m.
$$
同时 $nm-v_\ell(n)\to\infty$，包括 $m=1$，所以尾和确实收敛且有赋值至少 $3m$。由 (142.11)，$v_\ell(c_0z_0)\ge3m$，得到结论。$R'$ 可以分歧，证明没有将积分分母 $n$ 视为单位。证毕。

## 3. 同一真实尖点的前两项

固定 $\ell\mid D$。由 R137 §§3–4，在未分歧局部模型上，实际有理点 $P$ 与它的唯一尖点提升 $c$ 满足
$$
\Phi(P)=\Phi(c),\qquad
\Phi(x)=q([\delta x-\mathcal D]),\qquad
\delta=(p^2-1)/2,
\tag{142.12}
$$
其中 $\mathcal D$ 为所有几何尖点之和。此步只用秩零、尖点挠性和未分歧形式群无挠；不预先假定 nonexceptional。

在同一实际 Tate 参数
$$z=q_{\mathrm{Tate}}^{1/p},\qquad v_\ell(z(P))=m=v_\ell(D)$$
中，R72 (72.12)–(72.14) 给每一有限线的完整展开
$$
\pi_b^*\omega
=\sum_{n\ge1}a_n(g)\kappa^n\zeta_p^{abn}z^{n-1}\,dz,
\quad a\in\mathbb F_p^\times,
\quad\kappa\in\mu_p.
\tag{142.13}
$$
$a$ 和 $\kappa$ 由实际基和尖点同时确定。唯一乘法线 $\infty$ 的拉回是 $p\sum_{n\ge1}b_nz^{pn-1}dz$，其中 $b_n$ 为整系数；因为 $p>37$，它不影响常数项或 $z^1$ 项。这里只需它的整性与起始次数，不要求知道 $b_n$。

定义同一根下的两个向量
$$
v(n)=
\begin{pmatrix}
\sigma_{na}(u_1-u_0)\\
\sigma_{na}(u_2-u_0)
\end{pmatrix},\qquad n=1,2.
$$
按 R72 (72.9)，两条实际商微分的拉回满足
$$
\begin{pmatrix}\Omega_1\\\Omega_2\end{pmatrix}
=\left(\kappa v(1)
   +a_2(g)\kappa^2v(2)z
   +O(z^2)\right)\,dz.
\tag{142.14}
$$
所有剩余系数整。这两条微分通过 R72 的最优商饱和格上升为真实 $A$ 的整不变微分；引入新形式系数只作平坦基变换。

将 $v(2)$ 的两个分量记作 $v(2)_1,v(2)_2$，取整线性组合
$$
\widetilde\Omega
=v(2)_2\Omega_1-v(2)_1\Omega_2.
\tag{142.15}
$$
其常数项是 $\kappa\det(v(1),v(2))$，而第二项精确为
$$a_2(g)\kappa^2\det(v(2),v(2))\,z=0.$$
没有除以 $a_2(g)$，也没有选择另一个频率或另一个实际点。

对于 $\Phi$ 的微分还统一乘以 $\delta$，它是 $\ell$-单位。对 $h=\Phi-\Phi(c)$ 用引理142.2及 (142.12)，得到
$$
v_\ell\bigl(\det(v(1),v(2))\bigr)\ge2m.
\tag{142.16}
$$

## 4. 行列式恰是 $W_p$ 乘一个单位

先令 $a=1$，写 $s=\zeta_p-\zeta_p^{-1}$，$C=u_1-u_2=sB$。由 $u_0+u_1+u_2=0$，
$$
v(1)=\frac12
\begin{pmatrix}-3A+C\\-3A-C\end{pmatrix}.
$$
同样，$v(2)$ 将各项换为 $\sigma_2$ 共轭；又
$$\sigma_2(C)=(\zeta_p^2-\zeta_p^{-2})\sigma_2(B)=s\theta\sigma_2(B).$$
逐项相乘即得精确恒等式
$$
\boxed{
\det(v(1),v(2))
=\frac32\bigl(A\sigma_2(C)-\sigma_2(A)C\bigr)
=\frac32sW_p.
}
\tag{142.17}
$$
对于实际的 $a$，同一式的右边为 $\frac32\sigma_a(sW_p)$。由于 $\ell>p+1>3$，$2,3$ 为单位；$\sigma_a(s)$ 也为单位，因为在 $\ell\ne p$ 处本原 $p$ 次根不可能约化成平方为一的元素。

因此 (142.16) 给同一个实际圆分嵌入下
$$v_\ell(\sigma_aW_p)\ge2m.$$
把 $\sigma_a$ 移到素理想上，就得到 (142.8) 的第二项。R137 对两条原始微分给出的第一项使用同一个尖点、同一个 $a$ 和同一个嵌入，所以二者确实在同一个 $\lambda$ 上成立。

## 5. 取理想范数及坐标不变性

由 (142.8)，实际 $\lambda$ 满足
$$
v_\lambda(\mathfrak K_p)\ge2m,\qquad
v_\lambda(\mathfrak J_p^{[2]})\ge m.
$$
由 (142.2)，$\ell$ 在 $L^+$ 完全分裂。因此对每个 $\ell\mid D$，取所有上方理想的范数至少包含上述实际 $\lambda$ 的贡献，得到 (142.9)、(142.10)。另一方面，$r_\lambda^{[2]}\le v_\lambda(\mathfrak J)$，故 $N_p^{[2]}\mid N_p$。

交换三次角色取向只令 $B,W_p$ 同时变号。改本原根只作 Galois 共轭。若固定根而把颜色坐标缩放为 $sb$，则 R137 给
$$
A'=\sigma_sA,\qquad B'=U_s\sigma_sB,\qquad
U_s=\frac{\zeta_p^s-\zeta_p^{-s}}{\zeta_p-\zeta_p^{-1}},
$$
其中 $U_s$ 是实圆分单位。利用
$$\theta\sigma_2(U_s)=U_s\sigma_s(\theta),$$
可直接算得
$$W_p'=U_s\sigma_s(W_p).$$
所以 $\mathfrak J_p^{[2]}$ 只作同一个 Galois 共轭，$N_p^{[2]}$ 不依赖这些坐标选择。不能从这个坐标不变性推得在给定实际点上可以自由改选 $a$。

## 6. 准确增强及保留的缺口

R137 的第一次微分只要求某个实际 $\lambda$ 上 $v_\lambda(\mathfrak J)\ge m$。本篇另要求 $v_\lambda(W_p)\ge2m$。例如 $v_\lambda(\mathfrak J)=v_\lambda(W_p)=1$ 时，第一条件允许 $m=1$，第二条件直接排除。

这是一条关于**实际分母**的严格必要条件，不是关于抽象共同根不存在的断言。$W_p$ 在任何共同零处本来至少消失一次，故仅在剩余域检验 $W_p=0$ 不会增加信息；必须保留第二阶赋值。本文没有把 $W_p\equiv0$ 的一阶同余误称为新筛。

由 $N_p^{[2]}\mid N_p$，R137 的 Parseval 总分母界继续适用；本篇没有声称改进它的全称渐近常数。若能证明所有可能的实际 $\lambda$ 均不足以达到 (142.8)，则可在不证明整个 $\mathfrak J_p$ 为单位理想的情况下得到整性。但目前尚未证明这个全 $p$ 断言。R122 的指定三色共同非零问题、全部中心值共同为零分支及课题完成标准均保持开放。

## 参考输入

- [R69](R69-forgetful-maps-and-unconditional-rank-zero-quotient.md)：准确非零中心值前提下的实际秩零商。
- [R72](R72-optimal-quotient-cusp-immersion-and-exceptional-denominators.md)，(72.7)、(72.9)、(72.12)–(72.15)：最优整格、忘线展开和同一实际尖点的参数。
- [R137](R137-cyclotomic-denominator-depth-and-effective-bound.md)，§§2–4：未分歧形式群中的商像相等、一阶深度和实际素理想。本文对全部高次积分分母重新给出所需的二阶估计。
