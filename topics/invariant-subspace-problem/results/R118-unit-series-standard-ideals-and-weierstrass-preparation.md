# R118：单位幂级数的标准理想及Banach准备

日期：2026-11-12（UTC）。作者：Astra-ISP-0c017065。拟登记 R118。

**状态：完整证明；l2_moments、literature 已全文独立复核。** 本稿把 R115 的一类 Hilbert 核结论加强为实际交换 Banach 代数中的闭理想等式。准备因子的系数属于 $\mathcal A$，不是标量；本文给出自含构造、残数系数公式及合法的准幂零求值，不以标量准备定理的名称略过这一点。

## 1. 主定理

令
$$
\mathcal A=\overline{\mathbb C[I,A]},\qquad
W_n=\|A^n\|,\qquad M_n=A^n/W_n.
$$
$\mathcal A$ 是交换含幺 Banach 代数，唯一特征为形式常数项 $\chi$。对 $r\ge1$，记
$$
I_r=\overline{A^r\mathcal A}.
\tag{1.1}
$$
设 $V_n\in\mathcal A$，$\|V_n\|\le1$，并令
$$
S=\sum_{n\ge1}c_nM_nV_n,\qquad
r=\min\{n:c_n\ne0\},\qquad \chi(V_r)\ne0.
\tag{1.2}
$$
若 $c$ 有无限支持，设 $c_\ell^*$ 为其非零模长的非增重排，假定
$$
\boxed{
\Gamma(c)=\liminf_{\ell\to\infty}
\frac{-\log c_\ell^*}{\ell^3}>400r^4.
}
\tag{1.3}
$$
此条件保证 $\sum_n|c_n|^\varepsilon<\infty$，对每个 $\varepsilon>0$ 成立，故 (1.2) 绝对按算子范数收敛。

**定理 1.1。** 在上述条件下，
$$
\boxed{\overline{S\mathcal A}=I_r.}
\tag{1.4}
$$
更具体地，存在单位 $Z_K\in\mathcal A$，使
$$
SZ_K\longrightarrow A^r
\quad\text{于算子范数。}
\tag{1.5}
$$
若 $c$ 只有有限支持，则不需 (1.3)，(1.2) 的首项条件已经足够。

阈值 $400r^4$ 是本证明的充分阈值。R115 的较低阈值 $(80/3)r^4$ 仅凭已有论证给 Hilbert 空间上的单射稠密，不在本文被误写成同样的闭理想结论。

## 2. 所需全系数上界与标准理想

实际二进位公式给
$$
-\log W_n=\sum_{b_j(n)=1}\Lambda_j,\qquad
\Lambda_j=100\,16^j-105\,8^j+(150j+25)2^j.
$$
对每个 $j\ge0$，
$$
105\,4^j\ge150j+25,
$$
可从 $j=0,1$ 直接验证并以乘 $4$ 归纳。因此
$$
\Lambda_j\le100\,16^j,\qquad
-\log W_n\le100\sum_{b_j(n)=1}16^j\le100n^4.
\tag{2.1}
$$
特别地，
$$
W_n^{-1}\le e^{100n^4}.
\tag{2.2}
$$

记 $\gamma_j(T)$ 为 $\mathcal A$ 上连续的普通形式系数。则
$$
\boxed{
I_r=\{T\in\mathcal A:\gamma_0(T)=\cdots=\gamma_{r-1}(T)=0\}.
}
\tag{2.3}
$$
一边由连续系数乘法立得。反向，取多项式 $P_m(A)\to T$，减去其前 $r$ 个系数项：
$$
Q_m(A)=P_m(A)-\sum_{j<r}\gamma_j(P_m(A))A^j.
$$
若 $T$ 的这些系数为零，则 $Q_m(A)\to T$，每个 $Q_m$ 都真正被 $A^r$ 整除，故 $T\in I_r$。这也证明 $I_r$ 的余维恰为 $r$。

(1.2) 的每个有限头均在 $A^r\mathcal A$ 中，所以
$$
S\in I_r,\qquad \overline{S\mathcal A}\subseteq I_r.
\tag{2.4}
$$
主要工作是反向包含；不能由形式首项直接得出它。

## 3. 交换 Banach 代数系数的准备构造

本节在任意交换含幺 Banach 代数 $\mathcal B$ 中进行。设
$$
F(z)=z^rU(z),\qquad
U(z)=u+\sum_{\ell\ge1}u_\ell z^\ell,\qquad u\in\mathcal B^\times,
\tag{3.1}
$$
在零点附近解析。则存在 $\mathcal B$ 值解析芽
$$
P(z,w)=z^r+\sum_{i=0}^{r-1}a_i(w)z^i,\qquad a_i(0)=0,
$$
以及解析芽 $V(z,w)$，满足
$$
\boxed{F(z)+wI=P(z,w)V(z,w),\qquad V(0,0)=u.}
\tag{3.2}
$$

这里给出构造及收敛证明。选足够小的半径 $R>0$，使 $U$ 及 $U^{-1}$ 都在绝对系数 Banach 代数
$$
\mathcal W_R(\mathcal B)
=\left\{\sum_{\ell\ge0}b_\ell z^\ell:
\sum_{\ell\ge0}\|b_\ell\|R^\ell<\infty\right\}
$$
中。对于 $U^{-1}$，可先令
$\|u^{-1}(U-u)\|_{\mathcal W_R}<1$，再用 Neumann 级数。

写
$$
P(z,w)=z^r+\sum_{n\ge1}p_n(z)w^n,\qquad \deg p_n<r,
$$
$$
V(z,w)=U(z)+\sum_{n\ge1}v_n(z)w^n.
$$
若前面各项已知，令
$$
h_n(z)=\mathbf1_{\{n=1\}}I-\sum_{j=1}^{n-1}p_j(z)v_{n-j}(z).
$$
记 $\Pi_{<r}$ 为取前 $r$ 项系数的投影，定义
$$
p_n=\Pi_{<r}(U^{-1}h_n),\qquad
v_n=U\,\frac{U^{-1}h_n-p_n}{z^r}.
\tag{3.3}
$$
除以 $z^r$ 的分子前 $r$ 系数精确为零，故该式合法，且逐项满足 (3.2)。

在 $\mathcal W_R$ 范数中，$\|\Pi_{<r}\|\le1$，删去前 $r$ 项再除 $z^r$ 的范数至多 $R^{-r}$。因此存在仅依赖这一个 $U,R$ 的常数 $C\ge1$，使
$$
d_n:=\|p_n\|_{\mathcal W_R}+\|v_n\|_{\mathcal W_R}
\le C\mathbf1_{\{n=1\}}+C\sum_{j=1}^{n-1}d_jd_{n-j}.
\tag{3.4}
$$
Catalan 递推的直接归纳给
$$
d_n\le C^{2n-1}\operatorname{Cat}_{n-1}
\le C(4C^2)^{n-1}.
$$
所以两级数对充分小 $|w|$ 收敛，并在一个双圆盘中给真正解析恒等式 (3.2)。缩小圆盘后，$V(z,w)$ 在其中可逆。这里的半径可以随 $F$ 改变；后文不要求统一半径。

## 4. 准备系数的精确残数公式

对 $1\le m\le r$，取 §3 圆盘内部一个足够小的圆 $|z|=\rho$，使 $U(z)$ 及 $F(z)$ 在此圆上均可逆。对充分小 $w$，定义
$$
s_m(w)=\frac1{2\pi i}\int_{|z|=\rho}
z^mF'(z)(F(z)+wI)^{-1}\,dz.
\tag{4.1}
$$
这是 $\mathcal B$ 中的范数积分。因所有系数交换，(3.2) 的对数导数等式成立；$V_zV^{-1}$ 在圆内解析，不贡献积分。因此 $s_m$ 也是 $P_zP^{-1}$ 的相同积分。

将 $P_zP^{-1}$ 的 Laurent 展开与 $P$ 相乘并逐项比较，得到 Newton 恒等式
$$
s_m+a_{r-1}s_{m-1}+\cdots+a_{r-m+1}s_1+ma_{r-m}=0,
\quad 1\le m\le r.
\tag{4.2}
$$
这只是交换系数下的代数恒等式，不需要把 $\mathcal B$ 的特征当作忠实表示，也不需要在 $\mathcal B$ 中选择根。

(4.1) 对 $w$ 作 Neumann 展开。零次项为零；对 $n\ge1$，积分分部给
$$
\begin{aligned}
[w^n]s_m(w)
&=(-1)^n\frac1{2\pi i}
\int z^mF'(z)F(z)^{-n-1}\,dz\\
&=(-1)^n\frac mn\frac1{2\pi i}
\int z^{m-1}F(z)^{-n}\,dz.
\end{aligned}
$$
所以
$$
\boxed{
[w^n]s_m(w)=
(-1)^n\frac mn[z^{rn-m}]U(z)^{-n}.
}
\tag{4.3}
$$
负次系数按零理解。公式完整保留准备系数的 $\mathcal B$ 值结构。

## 5. 对全部有限头统一的四次系数界

回到 $\mathcal B=\mathcal A$。对 $K>r$，令
$$
F_K(z)=\sum_{r\le n<K}\frac{c_n}{W_n}V_nz^n
=z^rU_K(z).
\tag{5.1}
$$
首项
$$
u=U_K(0)=\frac{c_r}{W_r}V_r
\tag{5.2}
$$
不依赖 $K$，而且是单位。因为 $\sup_n|c_n|<\infty$，(2.2) 给
$$
\|[z^\ell](u^{-1}U_K(z)-I)\|
\le D e^{100(r+\ell)^4}\qquad(\ell\ge1),
\tag{5.3}
$$
其中 $D$ 与 $K$ 无关。

**引理 5.1。** 对每个固定 $\delta>0$，存在 $C_\delta\ge1$，与 $K$ 无关，使 §3 的全部准备系数满足
$$
\boxed{
\|[w^n]a_{i,K}(w)\|
\le C_\delta^n e^{(100+\delta)r^4n^4},
\qquad n\ge1,\quad0\le i<r.
}
\tag{5.4}
$$

**证明。** 置 $H_K=u^{-1}U_K-I$。取 (4.3) 中 $q=rn-m\ge0$。负二项展开为
$$
U_K(z)^{-n}
=u^{-n}\sum_{p\ge0}(-1)^p{n+p-1\choose p}H_K(z)^p.
\tag{5.5}
$$
当 $q\ge1$ 时，只有 $1\le p\le q$ 参与，且每个组成
$\ell_1+\cdots+\ell_p=q$ 都有 $\ell_j\ge1$。

对任意这种组成，凸性给
$$
\sum_{j=1}^p(r+\ell_j)^4
\le
(r+q-p+1)^4+(p-1)(r+1)^4.
$$
右端作为 $p\in[1,q]$ 的函数是凸的，故不超过两个端点值的较大者，尤其
$$
\sum_{j=1}^p(r+\ell_j)^4
\le(r+q)^4+q(r+1)^4.
\tag{5.6}
$$
由 $q\le rn$，
$$
100\sum_j(r+\ell_j)^4
\le100r^4(n+1)^4+100r(r+1)^4n.
$$
对任意固定 $\delta>0$，存在有限 $C'_{\delta,r}$，使
$$
100r^4(n+1)^4+100r(r+1)^4n
\le(100+\delta)r^4n^4+C'_{\delta,r}n
\quad(n\ge1).
\tag{5.7}
$$
例如把左减右后除以 $n$，所得表达式最高次项为负，故正上确界有限。

所有组成数、负二项式系数、$D^p$ 及 $\|u^{-1}\|^n$ 的总贡献至多为 $C^n$：这是因为 $q\le rn$、$p\le q$，组成总数至多 $2^q$，而 $\binom{n+p-1}{p}\le2^{n+p}$。$q=0$ 时只有 $u^{-n}$，同样满足此界。于是
$$
\|[z^{rn-m}]U_K^{-n}\|
\le C^n e^{(100+\delta)r^4n^4}.
\tag{5.8}
$$
(4.3) 给所有 $s_m$ 同样的界。

最后，(4.2) 表明每个 $a_i$ 是 $s_1,\ldots,s_r$ 的固定有限多项式，无常数项，单项式的因子数至多 $r$。在 $w^n$ 系数中，每个非零因子至少占一次 $w$，而
$$
n_1+\cdots+n_t=n
\quad\Longrightarrow\quad
\sum_{\nu=1}^t n_\nu^4\le n^4.
$$
有限多项式常数及至多多项式增长的组成数可再吸收进 $C_\delta^n$，得到 (5.4)。证毕。

注意：每个 $a_{i,K}$ 本身仍是通常解析芽；(5.4) 是为跨 $K$ 比较给出的统一粗界，并未把一个发散形式级数直接送入演算。

## 6. 在实际代数中的解析求值合法性

若 $\mathcal A$ 值二元解析芽写成
$$
G(z,w)=\sum_{a,b\ge0}G_{ab}z^aw^b,
$$
而 $T,R\in\mathcal A$ 均拟幂零，则
$$
G(T,R)=\sum_{a,b\ge0}G_{ab}T^aR^b
\tag{6.1}
$$
绝对按范数收敛。

确实，解析性给某个正 $R_1,R_2$ 和有限 $M$，
$\|G_{ab}\|\le MR_1^{-a}R_2^{-b}$。任取
$0<t_1<R_1$、$0<t_2<R_2$，拟幂零性给
$$
\|T^a\|\le C_1t_1^a,\qquad
\|R^b\|\le C_2t_2^b
$$
对所有非负整数成立，双级数便由两个几何级数控制。全部系数和求值元交换，因此乘法及解析恒等式可逐绝对级数求值。

取
$$
B_K=\sum_{n\ge K}c_nM_nV_n.
\tag{6.2}
$$
$A,B_K$ 的特征均为零，故均拟幂零。将 §3 的恒等式在 $(z,w)=(A,B_K)$ 处求值，得到
$$
S=
\left(A^r+\sum_{i<r}a_{i,K}(B_K)A^i\right)
V_K(A,B_K).
\tag{6.3}
$$
而
$$
\chi(V_K(A,B_K))=\chi(V_K(0,0))=\chi(u)\ne0.
$$
唯一特征性质保证 $V_K(A,B_K)$ 是 $\mathcal A$ 中的单位。故可定义
$$
Z_K=V_K(A,B_K)^{-1}\in\mathcal A^\times,
$$
并有真实恒等式
$$
\boxed{
SZ_K=A^r+\sum_{i<r}a_{i,K}(B_K)A^i.
}
\tag{6.4}
$$
本节没有要求 $\|A\|$、$\|B_K\|$ 落入某个依 $K$ 缩小的解析半径。它使用的是拟幂零幂的最终几何小量与绝对求值。

## 7. 真实尾幂使准备余项趋于零

取
$$
400r^4<\gamma<\Gamma(c).
$$
选择 $\delta>0$ 及 $0<\varepsilon<1$ 足够小，使
$$
D=\frac{(1-\varepsilon)\gamma}{4}>
(100+\delta)r^4.
\tag{7.1}
$$
R110/R115 的真实占据估计在这里给
$$
\boxed{
\|B_K^n\|
\le \sigma_K^n e^{-b_Kn^4},
\quad
\sigma_K=\sum_{j\ge K}|c_j|^\varepsilon\longrightarrow0,
}
\tag{7.2}
$$
其中，删去有限个最大系数后，
$$
b_K=(A_K^{-1/3}+D^{-1/3})^{-3}
\longrightarrow D,\qquad
A_K=\frac14\left(\sum_{j\ge K}j^{-4/3}\right)^{-3}.
\tag{7.3}
$$
为说明附带因子无遗漏：$(M_jV_j)^s=M_j^sV_j^s$ 的范数不超过
$\exp[-j^4(s-1)^4/4]$；$n$ 个因子中 $d$ 个不同指标分别支付重复项 $A_K(n-d)^4$ 和不同系数项 $Dd^4$，保留的 $\varepsilon$ 次系数按有序元组求和正好给 $\sigma_K^n$。二项 Hölder 给 (7.3)。系数衰减保证这一求和绝对收敛。

由 (7.1)—(7.3)，存在 $\zeta>0$，使所有充分大 $K$ 均有
$$
b_K\ge(100+\delta)r^4+\zeta.
$$
结合 (5.4)，
$$
\begin{aligned}
\|a_{i,K}(B_K)\|
&\le\sum_{n\ge1}
C_\delta^n e^{(100+\delta)r^4n^4}
\|B_K^n\|\\
&\le
\sum_{n\ge1}(C_\delta\sigma_K)^n e^{-\zeta n^4}
\longrightarrow0.
\end{aligned}
\tag{7.4}
$$
所有 $i<r$ 都只有有限个。由 (6.4)，
$$
\|SZ_K-A^r\|
\le\sum_{i<r}\|A^i\|\,
\sum_{n\ge1}(C_\delta\sigma_K)^n e^{-\zeta n^4}
\longrightarrow0.
\tag{7.5}
$$
这就证明 (1.5)，继而由 (2.4) 得 (1.4)。

若 $c$ 有限支持，直接写 $S=A^rU$，其中
$$
U=\sum_{n\ge r}\frac{c_n}{W_n}A^{n-r}V_n,\qquad
\chi(U)=\frac{c_r}{W_r}\chi(V_r)\ne0.
$$
这是有限有界和，$U$ 可逆；因此有限支持情况也成立。

## 8. 普遍表示、幂及 Boolean 例子

令 $\pi:\mathcal A\to B(X)$ 为任意 Banach 空间上的连续含幺代数表示。由两个闭理想相等，可得
$$
\boxed{
\ker\pi(S)=\ker\pi(A)^r,\qquad
\overline{\pi(S)X}=\overline{\pi(A)^rX}.
}
\tag{8.1}
$$
核等式直接使用 (1.5) 及 $S\in I_r$，并利用全部表示像交换；值域等式则在每一方向用相应的范数逼近。这里不是仅在原 Hilbert 表示中成立的结论。

在实际表示中，$A$ 单射且值域稠密，于是重得 $S$ 单射稠密及 $S1$ 循环。更强之处是 (1.4)—(1.5) 与 (8.1)。

若 $S,T$ 分别满足闭理想等式 $I_r,I_s$，则连续乘法和逐项逼近给
$$
\overline{ST\mathcal A}=I_{r+s}.
\tag{8.2}
$$
具体地，$A^r=\lim Sx_n$、$A^s=\lim Ty_n$ 给 $A^{r+s}$ 是 $ST\mathcal A$ 的极限，反向包含由 $S\in I_r,T\in I_s$ 得到。固定次幂因此满足
$$
\overline{S^d\mathcal A}=I_{rd}.
\tag{8.3}
$$

特别地，对
$$
S=\sum_{\varnothing\ne J\subset\mathbb N_0,\ |J|<\infty}
b_J\prod_{j\in J}Y_j,\qquad
n(J)=\sum_{j\in J}2^j,
$$
令
$$
c_{n(J)}=3^{|J|}b_J,\qquad
V_{n(J)}=3^{-|J|}\prod_{j\in J}(I+N_j)^{-1}.
$$
这些 $V_n$ 的范数至多为 $1$，且首项特征非零。若加权模长的降序三次型大于 $400r^4$，
$r=\min\{n(J):b_J\ne0\}$，则
$$
\overline{S\mathcal A}=I_r.
\tag{8.4}
$$
尤其降序超三次衰减满足此条件，允许真正无限 Walsh 次数。

## 9. 准确边界

本稿证明的是一个明确系数类的标准闭主理想，不是一般 $\mathcal A$ 的标准理想分类。R112 的连续二阶构造甚至没有绝对归一化幂表示，也不能被这里的假设自动覆盖。

(1.5) 没有给 $Z_K$ 的一致范数界，更没有宣称某个固定有界算子满足 $SZ=A^r$。范数闭理想包含与真实有界除法不同；既有除法反例继续有效。

本稿使用的 $\mathcal A$ 值解析演算仅在交换系数与拟幂零求值元下建立；不向一般非交换系数或任意形式级数推广。完整 ISP 与实际 $A$ 的普通不变格仍未解决。

依赖：
[R115 带因子归一化幂](../notes/2026-11-12-unit-normalized-series-boolean-cyclicity-0c-agent.md)；
[R116 一阶标准闭主理想](../notes/2026-11-12-first-chaos-standard-closed-principal-ideal-0c-agent.md)；
[R112 二阶表示障碍](../notes/2026-11-12-bounded-quadratic-no-l1-power-series-0c-agent.md)。
