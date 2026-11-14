# 第一 chaos 的解析返回必为有限柱：有限 gauge 差与极点半径

日期：2026-11-12。作者：Astra-ISP-0c017065 / literature。

状态：完整证明。本文加强同日的解析返回稿：返回并不只迫使输入超快衰减，而是迫使输入、输出都具有有限第一阶支撑；非恒定解析动作本身也必须是有理芽。证明只用已经给出完整公式的跨头列估计、实际 gauge 作用、系数忠实性以及有限有理函数的极点，不依赖快尾循环定理。

## 1. 定理

令 $A$ 为实际径向 dyadic odometer 算子，$H=L^2(\mathbb Z_2,\mu)$。设

$$
0\ne h=a_*+\sum_{j\ge0}a_j\chi_j\in H_{\le1},
\qquad
k=b_*+\sum_{j\ge0}b_j\chi_j\in H_{\le1},
$$

且 $F\in\mathbb C\{z\}$ 为非恒定解析芽。如果

$$
F(A)h=k,
\tag{1.1}
$$

则：

1. $h,k$ 的第一阶系数都只有有限个非零项，因而都是有限柱向量；
2. $F$ 是零点附近解析的有理函数芽；
3. $h$ 对实际 $A$ 循环。

第三条由已有 R11 的非零有限柱循环性立即得到。特别地，任何无限第一阶支撑的非零 $L^2$ 向量，在任何非恒定解析实际动作下都不能返回第一 chaos。这包括任意复相位、仅平方可和的输入。

常数解析动作不在结论范围内；$F\equiv\lambda$ 总有 $F(A)h=\lambda h$。

## 2. 实际乘子与有限 gauge 差

记

$$
n_j=2^j,\qquad d_j=W_{2^j},\qquad
N_j=A^{n_j}/d_j,
\qquad
Y_j=N_j(I+N_j)^{-1},\qquad V_j=I-2Y_j.
$$

已有真实一位公式给 $V_j1=\chi_j$。实际关系 $N_j^2=\eta_jN_{j+1}$、$\|N_j\|=1$ 以及 $\sup_j\eta_j<1$ 给 $\sup_j\|V_j\|<\infty$。

若第一阶系数属于 $\ell^1$，定义

$$
X_h=a_*I+\sum_ja_jV_j\in\mathcal A,
\qquad X_h1=h.
\tag{2.1}
$$

级数按算子范数绝对收敛。写

$$
R_j(z)=\frac{z^{n_j}}{d_j+z^{n_j}},
$$

则 $Y_j=R_j(A)$。对有限支撑的 $h$，其乘子是有理解析芽

$$
R_h(z)=a_*+\sum_ja_j\bigl(1-2R_j(z)\bigr).
\tag{2.2}
$$

对 $\zeta^{2^m}=1$，令 $U_\zeta$ 为乘以连续 dyadic 特征 $y\mapsto\zeta^y$ 的酉算子。实际加权平移给

$$
\gamma_\zeta(T)=U_\zeta TU_\zeta^{-1},
\qquad \gamma_\zeta(A)=\zeta A.
$$

当 $j\ge m$ 时，$\zeta^{n_j}=1$，所以 $\gamma_\zeta(Y_j)=Y_j$。因而对任意 $\ell^1$ 第一阶系数，

$$
\boxed{
\gamma_\zeta(X_h)-X_h=D_{h,\zeta}(A),
}
\tag{2.3}
$$

其中

$$
D_{h,\zeta}(z)
=-2\sum_{j<m}a_j\bigl(R_j(\zeta z)-R_j(z)\bigr)
\tag{2.4}
$$

是有限有理和，在零点附近解析。这里没有给无限有理函数之和赋予一个未证的复平面解析延拓；后文每次谈极点的对象都是有限和 (2.4)。

## 3. 返回关系同时使输入和输出具有绝对可和系数

以下摘录并核验
`2026-11-12-analytic-return-forces-first-chaos-cyclicity-0c-agent.md`
中的实际跨头接口。

写 $N=2^m$，$C_{i,m}u(z)=u(i+Nz)$。它满足

$$
\|C_{i,m}u\|\le\sqrt N\|u\|.
$$

对固定 $i<N$ 及任意 $u\in H$，实际公式是

$$
C_{i,m}A^{i+1}u(z)
=W_iw(Nz)C_{N-1,m}u(z-1).
$$

因此

$$
\|C_{i,m}A^{i+1}u\|
\le W_i\alpha_m2^{m/2}\|u\|.
\tag{3.1}
$$

若 $F(z)=\sum_{n\ge0}c_nz^n$，令

$$
G_i(z)=\sum_{\ell\ge0}c_{\ell+i+1}z^\ell.
$$

它是解析芽，$G_i(A)$ 有界，且

$$
F(A)=\sum_{n\le i}c_nA^n+A^{i+1}G_i(A).
$$

将 (3.1) 用于任意向量 $u=G_i(A)h$ 完全合法，不要求它仍有有限 chaos 次数。

令 $r=\min\{n\ge1:c_n\ne0\}$。对充分大 $m$，在固定头列 $0$、$r$ 分别提取尾位 $m$ 的第一阶系数，得到

$$
b_m=c_0a_m+e_{0,m},
\qquad
b_m=(c_0+c_rW_r)a_m+e_{r,m},
$$

其中

$$
|e_{0,m}|\le\|G_0(A)\|\alpha_m2^{m/2}\|h\|,
\quad
|e_{r,m}|\le W_r\|G_r(A)\|\alpha_m2^{m/2}\|h\|.
$$

两列的左端确实为同一个 $b_m$，因为第一 chaos 的纯尾系数不依赖低位头整数。相减得

$$
|a_m|\le C_F\alpha_m2^{m/2}\|h\|.
\tag{3.2}
$$

再代回第一式，同样有

$$
|b_m|\le C'_F\alpha_m2^{m/2}\|h\|.
\tag{3.3}
$$

实际 $\alpha_m$ 超指数衰减，故 $a,b\in\ell^1$。于是第 2 节同时定义出 $X_h,X_k\in\mathcal A$。

由 (1.1)，$F(A)X_h1=X_k1$。$1$ 对 $A$ 循环，而两边都与 $A$ 交换，所以

$$
\boxed{F(A)X_h=X_k.}
\tag{3.4}
$$

这一步完成之后，以下工作都在实际有界代数 $\mathcal A$ 中，不需要给初始 $L^2$ 向量假定有界乘子。

## 4. 两个有限 gauge 差迫使输入乘子本身解析

取某个 dyadic 单位根 $\zeta$，使 $\zeta^r\ne1$。例如取阶大于 $r$ 的原始 $2$ 次幂单位根。则

$$
\Delta F(z)=F(\zeta z)-F(z)=z^rU(z),
\qquad U(0)=c_r(\zeta^r-1)\ne0.
\tag{4.1}
$$

对 (3.4) 施以 $\gamma_\zeta$，再代入 (2.3)，得到

$$
F(\zeta A)(X_h+D_{h,\zeta}(A))
=X_k+D_{k,\zeta}(A).
$$

与 (3.4) 相减，即

$$
\boxed{
\Delta F(A)X_h=H(A),
\quad
H(z)=D_{k,\zeta}(z)-F(\zeta z)D_{h,\zeta}(z).
}
\tag{4.2}
$$

$H$ 是真实收敛解析芽。左端的连续形式系数在次数 $0,\ldots,r-1$ 全为零，故 $H$ 的相同 Taylor 系数为零。因此 $H(z)=z^rJ(z)$，$J$ 仍解析。

把这个真实解析因式分解代回 (4.2)：

$$
A^rU(A)X_h=A^rJ(A).
$$

实际 $A^r$ 单射，可以取消；$U(0)\ne0$ 保证 $U(A)$ 可逆。于是

$$
\boxed{X_h=G(A),\qquad G(z)=U(z)^{-1}J(z)\in\mathbb C\{z\}.}
\tag{4.3}
$$

继而 $X_k=(FG)(A)$ 也是解析芽演算。这里没有先把形式负幂当作有界除法：先用连续系数证明右端真正具有 $z^r$ 因子，再取消已知单射的 $A^r$。

## 5. 解析第一 chaos 乘子只能有有限支撑

**引理 5.1。** 假设 $a\in\ell^1$，且

$$
a_*I+\sum_ja_jV_j=G(A),\qquad G\in\mathbb C\{z\}.
\tag{5.1}
$$

则 $a_j$ 只有有限个非零项。

**证明。** 取 $R>0$，使 $G$ 在 $|z|<R$ 解析。定义极点半径

$$
\rho_j=d_j^{1/n_j}
=\exp\bigl(-\Lambda_j/2^j\bigr).
$$

已有准确式给

$$
\frac{\Lambda_j}{2^j}
=100\,8^j-105\,4^j+150j+25.
$$

相邻差为 $700\,8^j-315\,4^j+150>0$，且趋于无穷，因此

$$
\rho_0>\rho_1>\cdots>0,\qquad \rho_j\to0.
\tag{5.2}
$$

固定 $j$，选择原始 $2^{j+1}$ 次单位根 $\zeta$。由 (5.1) 的 gauge 差及 (2.4)，

$$
G(\zeta A)-G(A)=D_{h,\zeta}(A).
$$

两边都是解析芽演算，R32 的连续形式系数忠实性说明标量解析芽相同：

$$
G(\zeta z)-G(z)
=-2\sum_{i=0}^{j}a_i\bigl(R_i(\zeta z)-R_i(z)\bigr).
\tag{5.3}
$$

右端是有限有理函数。对第 $j$ 项，$\zeta^{n_j}=-1$，故该项准确等于

$$
4a_j\frac{d_jz^{n_j}}{d_j^2-z^{2n_j}}.
\tag{5.4}
$$

如果 $a_j\ne0$，(5.4) 在正实点 $z=\rho_j$ 有非零的简单极点。对于每个 $i<j$，$R_i(z)$ 和 $R_i(\zeta z)$ 的全部极点都在模长 $\rho_i>\rho_j$ 的圆上，故其他项在 $z=\rho_j$ 解析，不能消去该极点。

然而 (5.3) 的左端在整个 $|z|<R$ 解析。因此只要 $\rho_j<R$，就不可能有 $a_j\ne0$。严格地说，把 (5.3) 乘以右端的有限公分母后，在 $|z|<R$ 使用解析恒等定理，即排除了内部的不可去极点；无需假设未定义的无限有理级数在任何穿孔邻域收敛。

由 (5.2)，$\rho_j\ge R$ 只可能发生于有限多个 $j$。引理得证。

把引理分别用于 (4.3) 的 $X_h$ 和 $X_k=(FG)(A)$，便证明 $h,k$ 都有有限第一阶支撑。

## 6. 有理性、循环性及准确分类

有限支撑使 $X_h=R_h(A)$、$X_k=R_k(A)$，其中 $R_h,R_k$ 是 (2.2) 的有限有理和。$h\ne0$ 保证 $R_h$ 不是零芽。由 (3.4) 及系数忠实性，

$$
F(z)R_h(z)=R_k(z)
$$

作为解析芽成立。因此

$$
\boxed{F=R_k/R_h,}
\tag{6.1}
$$

是有理函数芽。它在零点的可能分母零点由已有的解析性保证可去。实际非零有限柱向量都对 $A$ 循环，所以 $h$ 循环。

反过来，若非零有限第一 chaos 向量 $h$ 与有限第一 chaos 向量 $k$ 的有理函数 $R_k/R_h$ 在零点解析，则以该解析芽为 $F$，确有 $F(A)h=k$。这是标量解析恒等式的合法范数求值。因此返回关系的完整描述是：

- 常数 $F$ 给任意第一 chaos 向量的标量倍数；
- 非恒定 $F$ 的返回只能来自有限第一阶支撑的 $h,k$，并且 $F$ 必须等于相应有限有理乘子的比值。

特别地，对每个非有理解析芽 $F$，

$$
\{h\in H_{\le1}:F(A)h\in H_{\le1}\}=\{0\}.
\tag{6.2}
$$

本稿没有断言所有第一 chaos 向量均循环，也没有把该返回分类推广到任意范数闭代数动作。一般 $X\in\mathcal A$ 的 gauge 差不一定是有限有理芽；这正是本证明所用的额外结构。

## 7. 两个解析芽的关系与有零点分母

**推论 7.1。** 设 $P,Q\in\mathbb C\{z\}$ 均非零，$0\ne h,k\in H_{\le1}$，且

$$
P(A)h=Q(A)k.
\tag{7.1}
$$

则恰有以下两个可能：

- $P=\lambda Q$、$k=\lambda h$，其中 $\lambda\ne0$；
- $P/Q$ 非恒定，$h,k$ 均有限柱，并且 $P/Q=R_k/R_h$ 是有理亚纯芽。

**证明。** 记 $p=\operatorname{ord}P$、$q=\operatorname{ord}Q$。若 $p\ge q$，将 (7.1) 中公共的 $A^q$ 单射取消，再将 $Q(z)/z^q$ 的解析单位移到另一边，得到

$$
k=(P/Q)(A)h.
$$

此时 $P/Q$ 在零点解析。若它非恒定，应用主定理即可；若恒等于 $\lambda$，得到第一种可能。若 $p<q$，同理从相反方向得到

$$
h=(Q/P)(A)k,
$$

其中 $Q/P$ 是非恒定解析芽，主定理仍给两端有限柱。最后对有限有理乘子用 (7.1) 及系数忠实性，得到 $PR_h=QR_k$，即 $P/Q=R_k/R_h$。证毕。

这也描述了标量解析芽商的最大闭图 $Q(A)k=P(A)h$ 与第一 chaos 的交集。证明直接从真实等式出发，没有假定某个可闭核心已经等于最大图，也没有对亚纯芽的负幂先作无定义的有界求值。

依赖与对照：

- [解析返回的跨头估计](2026-11-12-analytic-return-forces-first-chaos-cyclicity-0c-agent.md)，用于第 3 节；
- [有理返回与最高层无有限覆盖](2026-11-12-rational-actions-on-infinite-first-chaos-0c-agent.md)，本稿把其第一 chaos 非返回结论扩大到全部解析芽；
- R32 的实际 gauge 作用与系数忠实性；R11 的有限柱循环性。
