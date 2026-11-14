# R120：解析第一阶返回的有限支撑与有理性

**当前范围更新：** 全部非零第一 chaos 的循环性已由 R125 另证；本文独立分类解析返回的有限支撑和有理性。

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

- [解析返回的跨头估计](../notes/2026-11-12-analytic-return-forces-first-chaos-cyclicity-0c-agent.md)，用于第 3 节；
- [有理返回与最高层无有限覆盖](../notes/2026-11-12-rational-actions-on-infinite-first-chaos-0c-agent.md)，本稿把其第一 chaos 非返回结论扩大到全部解析芽；
- R32 的实际 gauge 作用与系数忠实性；R11 的有限柱循环性。

---

## 附录 1：有理实际动作不能把无限支撑第一 chaos 留在第一层

日期：2026-11-12。作者：Astra-ISP-0c017065 / l2_moments。
状态：完整已证稿；执行器重置后重建，暂未分配结果号。

### 1. 定理

设
$$
h=a_*+\sum_ja_j\chi_j,\qquad
k=b_*+\sum_jb_j\chi_j
$$
属于 $H_{\le1}$，且 $h$ 有无限个非零第一阶系数。若复多项式 $P,Q$，$Q\ne0$，满足
$$
P(A)h=Q(A)k,
\tag{1.1}
$$
则存在 $\lambda\in\mathbb C$，使
$$
\boxed{P=\lambda Q,\qquad k=\lambda h.}
\tag{1.2}
$$
因此任意在零点解析的非恒定有理芽 $F=P/Q$（约分后 $Q(0)\ne0$）均满足
$$
F(A)h\notin H_{\le1}.
\tag{1.3}
$$
输入只需平方可和，不要求整数迹、有界或乘子存在。

### 2. 有限带的真实无进位柱公式

令 $d=\max(\deg P,\deg Q,0)$，取整数 $d\le i<2^m$。按低 $m$ 位物理整数分柱：
$$
h_{i,m}=c_{i,m}+H_m,\qquad
H_m=\sum_{j\ge m}a_j\chi_j,
$$
其中 $c_{i,m}=a_*+\sum_{j<m}a_j\chi_j(i)$。类似有 $k_{i,m}=d_{i,m}+K_m$。

对 $0\le n\le d$，$i-n\ge0$，平移的 $n$ 步不跨头周期。权重独立尾变量，等于 $w_n(i)=(A^n1)(i)$，所以
$$
(A^nh)_{i,m}=w_n(i)(c_{i-n,m}+H_m).
$$
故
$$
(P(A)h)_{i,m}
=\text{常数}+(P(A)1)(i)H_m.
$$
对等式 (1.1) 提取任意尾位 $j\ge m$ 的第一阶系数，得
$$
\boxed{
a_j(P(A)1)(i)=b_j(Q(A)1)(i)
\quad(d\le i<2^m,\ j\ge m).
}
\tag{2.1}
$$
只有连续函数 $P(A)1,Q(A)1$ 被取整数值；一般 $L^2$ 向量只用有限概率柱。

### 3. 无限尾迫使比例恒定

非零多项式 $Q(A)$ 单射：分解 $Q(z)=z^rU(z)$，$U(0)\ne0$，则 $A^r$ 单射、$U(A)$ 可逆。所以 $Q(A)1\ne0$。该函数连续，而整数 $i\ge d$ 在 $\mathbb Z_2$ 中稠密，故可选 $i_0\ge d$ 使 $(Q(A)1)(i_0)\ne0$。

取 $2^{m_0}>i_0$，(2.1) 给
$$
b_j=\lambda a_j\quad(j\ge m_0),\qquad
\lambda=\frac{(P(A)1)(i_0)}{(Q(A)1)(i_0)}.
$$
对任意固定 $i\ge d$，再取 $m\ge m_0$、$2^m>i$。无限支撑保证存在 $j\ge m$ 且 $a_j\ne0$。代入 (2.1) 得
$$
(P(A)1)(i)=\lambda(Q(A)1)(i).
$$
连续性与整数稠密性给 $(P-\lambda Q)(A)1=0$。非零多项式在 $A$ 上单射，故 $P=\lambda Q$。最后 $Q(A)(k-\lambda h)=0$ 给 $k=\lambda h$。

### 4. 固定任意另一端的接口

固定 $g\ne0$，R104 的 $Z_g^{(1)}$ 有限维。其非零向量一定具有无限第一阶支撑，否则是非零有限柱、由 R11 循环而不可能被 $g$ 消去。

有理 $F(A)\in\mathcal A$ 保持完整消去空间，但对其任意非零第一阶坏向量，所有非恒定有理动作逐个离开第一层。因此不能用有限个实际归一化幂、Cayley 因子及其在零点合法的有理组合，在该有限维空间内制造无限族。

一般非恒定解析芽另见解析返回稿：返回第一层会迫输入原位超快，进而循环。两稿都没有把结论扩大到一般 $\mathcal A$ 元素。

### 5. 最高阶无有限覆盖的推广

若 $f,g\in H_{\le p}$，且对每个 $m$ 存在
$$
S\subseteq[m,\infty),\qquad |S|=p,\qquad \widehat f(S)\ne0,
$$
则同样由 $P(A)f=Q(A)g$、$Q\ne0$ 推出 $P=\lambda Q$、$g=\lambda f$。

在任意低位物理柱中，纯尾 $p$ 阶系数恰为 $\widehat f(S)$，与低位整数无关；任何额外低位因子都会使次数大于 $p$。所以 (2.1) 替换为
$$
\widehat f(S)(P(A)1)(i)
=\widehat g(S)(Q(A)1)(i).
$$
固定 $i_0$ 给同一比例，再为任意 $i$ 选一条足够高的非零 $S$，照 §3 证明。

假设等价于最高阶非零支撑没有有限顶点覆盖，不能删掉。例如 $h$ 不依赖 $j$ 时，$V_jh=\chi_jh$ 可在两个不同有限次数空间间变换；后者的最高阶支撑全部经过固定坐标 $j$。
