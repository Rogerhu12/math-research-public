# R254 第三附录：真实平方核的纯高尾高阶删除约束与低孔正交近似

日期：2026-11-13（UTC+8）。作者：boundary。
状态：已证明的实际中间结论；同时覆盖规范边界 $N/Y$ 两种慢和。保留全部混合项，不通过相似消去它们。本稿不证明 $M=\overline{BM}$。

## 1. 实际核、原物理位号和混合截断

沿用 R254 首位图。把原最低位移除后，归一化快速尾移位为 $C$，$\|C\|=1$；令

$$
\eta=\eta_0=e^{-1070},\qquad b_j=(j+2)^{-2}.
$$

分别取真实慢尾

$$
\mathcal A_N=\sum_{j\ge0}b_j\bar N_j,\qquad
\mathcal A_Y=\sum_{j\ge0}b_j\bar Y_j.
$$

这里的 $\mathcal A$ 是图中的慢尾，不是原 Haar 快移位。R254 已证明 $\|\mathcal A\|<2/3$，并给

$$
Z_N=\mathcal A_N,\qquad
Z_Y=\mathcal A_Y(I+\mathcal A_Y)^{-1},\qquad
K=\ker(Z^2-\eta C).
$$

对原慢核 $M$，每个向量唯一写为 $w=(u,-Zu)$、$u\in K$；本稿估计适用于所有这样的 $u$，不额外假设 $w\in W$。

在 $N$ 情形置

$$
P=\mathcal A^2-\eta C.
$$

在 $Y$ 情形乘实际有界可逆单位 $(I+\mathcal A)^2$，置

$$
P=\mathcal A^2-\eta C(I+\mathcal A)^2.
\tag{1.1}
$$

因为所有函数均与 $C$ 交换，且 $\|\mathcal A\|<1$，两种情形都严格有 $K=\ker P$。$Y$ 的单位只用于核等价，不把原伴随源未经变换地沿用。

取 $m\ge2$、$d=2^m$。头包含图中前 $m$ 位，即原物理位 $1,\ldots,m$。记其真实截断为 $C_m,\mathcal A_m$，并令

$$
D=D_m^{\mathrm p}=\sum_{j\ge m}b_jE_j
$$

为独立的无穷纯高尾删除和。混合截断是

$$
\mathcal A^{[m]}=\mathcal A_m\otimes I+I\otimes D.
$$

以下省略张量单位。R254 的实际预算为

$$
\|\mathcal A-\mathcal A^{[m]}\|\le26\eta_m,\qquad
\|C-C_m\|\le\eta_m,
\tag{1.2}
$$

$$
\|\mathcal A_m\|+\|D\|<\frac23,\qquad
C_m^d=0.
\tag{1.3}
$$

$\mathcal A_m$ 是 $C_m$ 的零常数多项式。这里 $\eta_m$ 使用**原物理位号**，精确值为

$$
\boxed{\ -\log\eta_m
=1400d^4-630d^3+300d.\ }
\tag{1.4}
$$

后文保留此真实指数；若只用粗界 $770d^4$，不能得到本稿的 $700d^4$ 主余量。

## 2. 保留混合项的有限头消元恒等式

定义对应的混合符号：

$$
P_m=(\mathcal A_m+D)^2-\eta C_m
\quad(N),
$$

$$
P_m=(\mathcal A_m+D)^2
-\eta C_m(I+\mathcal A_m+D)^2
\quad(Y).
\tag{2.1}
$$

二者均可写成

$$
P_m=D^2+Q_m,
$$

其中

$$
Q_m=\mathcal A_m^2+2\mathcal A_mD-\eta C_m
\quad(N),
$$

$$
Q_m=\mathcal A_m^2+2\mathcal A_mD
-\eta C_m(I+\mathcal A_m+D)^2
\quad(Y).
\tag{2.2}
$$

线性混合项 $2\mathcal A_mD$ 完整保留。由于 $\mathcal A_m$ 是 $C_m$ 的零常数多项式，$Q_m$ 是 $C_m,D$ 的交换多项式且含有因子 $C_m$。因此

$$
Q_m^d=0,\qquad Q_mD=DQ_m.
\tag{2.3}
$$

设 $a=\|\mathcal A_m\|$、$\delta=\|D\|$，则 $a+\delta<2/3$。两种情形统一满足

$$
\|Q_m\|\le(a+\delta)^2+\eta(1+a+\delta)^2
<\frac49+\frac{25}{9}\eta<\frac12,
\qquad
\|D^2\|<\frac12.
\tag{2.4}
$$

置

$$
R_m=\sum_{k=0}^{d-1}(-Q_m)^kD^{\,2(d-1-k)}.
\tag{2.5}
$$

由交换几何和及 $Q_m^d=0$，准确有

$$
\boxed{\ R_mP_m=P_mR_m=D^{2d}.\ }
\tag{2.6}
$$

并且

$$
\boxed{\ \|R_m\|\le d\,2^{1-d}.\ }
\tag{2.7}
$$

证明 (2.7) 时，(2.5) 每项的两因子指数之和都是 $d-1$，直接用 (2.4) 即可。这里既没有把 $D$ 当成幂零，也没有改变头尾分级。

## 3. 实际核的高阶纯尾约束

先支付实际符号误差。由 (1.2)—(1.3)，

$$
\|\mathcal A^2-(\mathcal A^{[m]})^2\|
\le\frac{104}{3}\eta_m.
$$

在 $Y$ 情形，另有

$$
\begin{aligned}
&\|C(I+\mathcal A)^2
-C_m(I+\mathcal A^{[m]})^2\|\\
&\qquad\le
\|C-C_m\|\|I+\mathcal A\|^2+
\|C_m\|\|(I+\mathcal A)^2-(I+\mathcal A^{[m]})^2\|\\
&\qquad\le
\left(\frac{25}{9}+\frac{260}{3}\right)\eta_m
=\frac{805}{9}\eta_m.
\end{aligned}
$$

因此，因 $\eta<1/100$，

$$
\boxed{\ \|P-P_m\|
\le\left(\frac{104}{3}+\frac{805}{9}\eta\right)\eta_m
<36\eta_m.\ }
\tag{3.1}
$$

这也包含更小的 $N$ 误差。

若 $u\in K=\ker P$，则由 (2.6)，

$$
D^{2d}u=R_m(P_m-P)u.
$$

从而得到本稿第一个结论：

$$
\boxed{\ \|D^{2d}u\|
\le36d\,2^{1-d}\eta_m\,\|u\|,
\qquad u\in K.\ }
\tag{3.2}
$$

这是实际无穷核上的算子范数估计，没有使用有限支撑假设，也没有相似条件数。它不是 $D^{2d}u=0$ 的断言。

## 4. 无穷纯尾每一完整孔层上的明确右逆

本节独立于实际核。令 $\mathcal H_q^{(m)}$ 是纯高尾的完整 $q$ 孔层，位置可以无限远。$D$ 将 $\mathcal H_{q+1}^{(m)}$ 送入 $\mathcal H_q^{(m)}$。

**引理。** 对每个 $q\ge0$，存在有界

$$
G_q:\mathcal H_q^{(m)}\longrightarrow\mathcal H_{q+1}^{(m)},
\qquad DG_q=I,
$$

且

$$
\boxed{\ \|G_q\|
\le18(m+q+2)^{3/2}e^{7q}.\ }
\tag{4.1}
$$

**证明。** 记原系数 $a_j=(j+2)^{-2}$、$j\ge m$。取

$$
J=4(q+m+2),\qquad
\beta=(m+J+2)^{-2}.
$$

把前 $J$ 个尾位置 $j=m,\ldots,m+J-1$ 的系数截平为 $\beta$，其余保留 $a_j$，所得为 $\widetilde a_j$。所有 $\widetilde a_j\le\beta$，且

$$
\sum_j\widetilde a_j^2\ge J\beta^2.
$$

令 $C_{\widetilde a}=\sum\widetilde a_jE_j^*$ 为纯创建算子。真实局部 CCR 给

$$
C_{\widetilde a}^*C_{\widetilde a}
-C_{\widetilde a}C_{\widetilde a}^*
=\sum_j\widetilde a_j^2(I-2n_j).
$$

在完整 $q$ 孔层上 $\sum_jn_j=qI$，故

$$
\|C_{\widetilde a}f\|^2
\ge\beta^2(J-2q)\|f\|^2.
\tag{4.2}
$$

于是 $C_{\widetilde a}$ 有左逆 $L_{\widetilde a}$，范数至多
$[\beta\sqrt{J-2q}]^{-1}$。可取通常的
$(C_{\widetilde a}^*C_{\widetilde a})^{-1}C_{\widetilde a}^*$；不假设它保持有限位置支撑。

令 $\rho_j=a_j/\widetilde a_j\ge1$，在第 $q$ 层上定义对角 $S_q$，对有限洞集 $F$ 乘以 $\prod_{j\in F}\rho_j$。仅前 $J$ 位的 $\rho_j$ 不为 $1$，故它在整个孔层上有界且 $\|S_q^{-1}\|\le1$。精确相似方向是

$$
C_aS_q=S_{q+1}C_{\widetilde a}.
$$

所以

$$
L_a=S_qL_{\widetilde a}S_{q+1}^{-1}
$$

是 $C_a$ 的左逆，只需支付 $S_q$。最大乘积取前 $q$ 位，因此

$$
\|S_q\|
\le\left[
\frac{(m+J+2)^q}{\prod_{k=0}^{q-1}(m+k+2)}
\right]^2.
\tag{4.3}
$$

当 $q\le m+2$，逐因子比率不超过 $10$；当 $q>m+2$，用
$m+J+2\le5(q+m+2)<10q$ 及 $q!\ge(q/e)^q$。包括 $q=0$ 的空乘积在内，

$$
\|S_q\|\le(10e)^{2q}<e^{7q}\quad(q>0),
$$

$q=0$ 时两边等于 $1$。又

$$
J-2q\ge2(q+m+2),\qquad
m+J+2\le5(q+m+2),
$$

故

$$
\frac1{\beta\sqrt{J-2q}}
\le\frac{25}{\sqrt2}(q+m+2)^{3/2}
<18(q+m+2)^{3/2}.
$$

取 $G_q=L_a^*$ 即得 (4.1)。证明完全在真实无穷孔层上进行。证毕。

## 5. 到纯尾高阶核的正交距离

令 $r\ge1$，$\Pi_{m,r}$ 为 $I_{\rm head}\otimes D^r$ 的核的正交投影。由于 $D^r$ 严格降低尾孔数 $r$，该核按尾孔数正交分解，所以 $\Pi_{m,r}$ 与每个尾孔截断交换。

记 $P_{\le Q}^{\rm tail,m}$ 为尾孔数至多 $Q$ 的投影。对 $Q\ge r$，由 (4.1) 复合 $r$ 次，$D^r:\mathcal H_q^{(m)}\to\mathcal H_{q-r}^{(m)}$（$r\le q\le Q$）有右逆，其范数至多

$$
\Gamma_{m,Q,r}
=18^r(m+Q+1)^{3r/2}e^{7rQ}.
\tag{5.1}
$$

具体取 $G_{q-1}\cdots G_{q-r}$；指数和为
$7\sum_{p=q-r}^{q-1}p\le7rQ$。对 $q<r$，整个孔层本来就在核中。

对每个 $u_q$，从 $u_q$ 减去上述右逆作用于 $D^ru_q$，便落入核；正交投影的距离不大于这个候选修正的范数。各输出孔层彼此正交，张量上任意有限头向量也保持正交，因此

$$
\boxed{\ 
\|(I-\Pi_{m,r})P_{\le Q}^{\rm tail,m}u\|
\le\Gamma_{m,Q,r}\|D^ru\|
\qquad(u\in H).
\ }
\tag{5.2}
$$

这是对实际正交投影的估计，不是把一个斜投影的范数当成 $1$。

取 $r=2d$，记 $\Pi_m=\Pi_{m,2d}$。对实际核 $u\in K$，(3.2) 与 (5.2) 给

$$
\boxed{\ 
\|(I-\Pi_m)P_{\le Q}^{\rm tail,m}u\|
\le\varepsilon_{m,Q}\|u\|,
\ }
\tag{5.3}
$$

其中完全显式地

$$
\varepsilon_{m,Q}
=36d\,2^{1-d}\eta_m\,
18^{2d}(m+Q+1)^{3d}e^{14dQ}.
\tag{5.4}
$$

若 $Q<2d$，左侧为零，故无需另作预算。

## 6. 一个全 $m\ge2$ 有效的窗口

取

$$
Q_m=50d^3.
$$

将真实 (1.4) 代入 (5.4)：

$$
\begin{aligned}
\log\varepsilon_{m,Q_m}\le{}&
-700d^4+630d^3-300d\\
&+\log(36d)+(1-d)\log2+
2d\log18+3d\log(m+50d^3+1).
\end{aligned}
\tag{6.1}
$$

所以渐近主率是 $-(700+o(1))d^4$。这个主率用的是原物理跨界 $\eta_m$ 的 $1400d^4$，不是粗 $770d^4$。

还可给不依赖“大 $m$”的简明界。对 $d\ge4$，

$$
m+50d^3+1\le52d^3,\qquad
\log(36d)\le2d,\qquad
\log d\le d/2.
$$

故除 $630d^3$ 外的正项至多 $20d+9d\log d\le20d+(9/2)d^2$。而

$$
630d^3+20d+\frac92d^2<200d^4
\qquad(d\ge4).
$$

丢掉 (6.1) 中其余负项，得到

$$
\boxed{\ 
\|(I-\Pi_m)P_{\le50d^3}^{\rm tail,m}u\|
\le e^{-500d^4}\|u\|,
\qquad m\ge2,\ u\in K.
\ }
\tag{6.2}
$$

由正交投影收缩性，

$$
\boxed{\ 
\|(I-\Pi_m)u\|
\le\|P_{>50d^3}^{\rm tail,m}u\|
+e^{-500d^4}\|u\|.
\ }
\tag{6.3}
$$

尾孔数大于 $Q$ 必然意味着全部图尾的总孔数大于 $Q$，因此若 $\tau_Q(u)$ 表示总孔尾范数，也有

$$
\boxed{\ 
\operatorname{dist}(u,\ker(I_{\rm head}\otimes D^{2d}))
\le\tau_{50d^3}(u)+e^{-500d^4}\|u\|.
\ }
\tag{6.4}
$$

整个尾项的系数是 $1$，没有相似条件数。

更一般地，对任意固定 $0<\lambda<100$、$Q=\lfloor\lambda d^3\rfloor$，(5.4) 给

$$
\log\varepsilon_{m,Q}
\le-\bigl(1400-14\lambda+o(1)\bigr)d^4.
\tag{6.5}
$$

本稿不声称 $\lambda=100$ 的端点，也不以未证明的更优固定层右逆常数替换 $7$。

## 7. 与当前能量缺口的关系

这个估计直接来自真实核方程和严格头幂零性。线性混合项保留在 $Q_m$ 中，它没有被视作同级齐次项，也没有被粗略删掉。

$\ker D^{2d}$ 一般远大于 $\ker P_m$，因此 (6.4) 不能改写成到 $\ker P_m$、到 $N$ 或到某个真实原像空间的距离。该投影也不能未经核验地与 $P_m$ 交换。虽然它按孔层分解并范数为 $1$，$D$ 的核投影通常只给不变子空间，并不使它约化 $D$。

对每个固定有限孔向量，当 $2d$ 足够大时，它本来就在 $\ker D^{2d}$。本稿新增的是：对实际 $K$ 中的向量，这种近似可定量推进到 $50d^3$ 的孔窗口，同时误差仍为 $e^{-500d^4}$，且在窗口外仅付原向量的普通 Hilbert 尾。

下一有效接口是利用这个真实纯尾高阶约束控制保留混合项后的有限模块能量，或在该高阶核上构造有已付带宽的左右等价。现阶段没有从 (6.4) 得出 $W=0$ 或非零 $W$ 的构造。
