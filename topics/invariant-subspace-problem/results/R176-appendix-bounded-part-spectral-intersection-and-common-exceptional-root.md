# R176 附录：有界不变部分的谱相交、单一根分支与共同例外值

日期：2026-11-13（UTC）。作者：kernel_resume_1cf；Astra-ISP-1cf8c51d 已完成全文复核。
状态：完整证明。新增的是不同未知不变部分之间的谱相交及其共同根约束；不排除最后一个单根拟幂零分支。一般 Hilbert ISP 仍未完成。

## 1. 范围扣除与准确设置

[R176](R176-natural-polynomial-maximal-graphs-and-bell-domains.md) §8 已证明：最高系数可逆的自然多项式核上，一阶乘子处处定义且有界；在 $\mathcal A$ 系数情形，其谱包含于字符多项式的有限零集，并可作 Riesz 分解。
本稿不把这个核内有界化或有限谱归约重新登记为新增。

[R181](R181-bounded-coefficient-bell-polynomial-spectrum-trichotomy.md) 已给相应完整闭算子的空谱／单点谱／全平面谱分类，且明确保留全平面分支的可能点谱。
本稿新增：上述有限谱核实际上只能留下一个谱点；不同多项式、不同指数倾斜的全部非零核必须共用这个谱点。
继而给出至多一个实际坏位移以及第一位碰撞的共同根条件。

固定
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
a\in\ell^2(\mathbb C),\quad a\ne0,
$$
令 $X=X_u$ 为原 $H=L^2(\mathbb Z_2)$ 上的实际闭 first。
记
$$
\mathcal A=\overline{\mathbb C[I,A]},\qquad
\mathfrak C=\{A\}',\qquad
B(f,g)=\int f(y)g(-1-y)\,d\mu(y).
$$
使用以下已经证明的真实算子事实：

- R88：$\mathfrak C$ 交换并强生成于 $A$；其每个成员保持每个闭 $A$ 不变子空间。
- R125/R128：$X=CX^*C$；每个 $\mathfrak C$ 成员与完整 $X$ 域交换。
  对每个 dyadic 根 $\zeta$，
  $$
  U_\zeta XU_\zeta^*=X+D_\zeta,\qquad
  U_\zeta\operatorname{Dom}X=\operatorname{Dom}X,
  \tag{1.1}
  $$
  其中 $D_\zeta\in\mathcal A$ 是实际有限解析头，$\chi(D_\zeta)=0$。
- R128/R140 的共同正则器满足
  $R(t),S(t)=XR(t)\in\mathfrak C$、$R(t)\to I$ 强，
  并有 $R(t)Xf=S(t)f$ 于 $\operatorname{Dom}X$。
- $\mathcal A$ 是局部代数，唯一字符为 $\chi$；
  $E-\chi(E)I$ 在原 $H$ 上拟幂零。
  原 $A$ 单射、拟幂零，其加权 odometer 权几乎处处严格正。

因此，对任意闭 $A$ 不变 $M$ 和 $f\in M\cap\operatorname{Dom}X$，
$$
S(t)f\in M,\qquad S(t)f=R(t)Xf\longrightarrow Xf,
$$
所以 $Xf\in M$。
称非零闭 $A$ 不变空间 $M$ 为一个**有界部分**，若
$M\subseteq\operatorname{Dom}X$。
这时 $X_M=X|_M:M\to M$ 由闭图定理有界。

全部双线性对称只在原 $H$ 的完整定义域使用；
不假设 $CM=M$，也不把原共轭下降为 $M$ 上的自伴结构。

## 2. 任意两个有界部分的谱必相交

**定理 2.1。**
若 $M,N$ 是两个非零有界部分，则
$$
\boxed{\sigma(X_M)\cap\sigma(X_N)\ne\varnothing.}
\tag{2.1}
$$

### 2.1 Gauge 不改变有界部分的谱

对任意 dyadic $\zeta$，置 $N_\zeta=U_\zeta N$。
由 $U_\zeta AU_\zeta^*=\zeta A$，$N_\zeta$ 仍闭且 $A$ 不变。
由 (1.1)，它包含于 $\operatorname{Dom}X$，且
$$
X_{N_\zeta}
=U_\zeta X_NU_\zeta^* - D_\zeta|_{N_\zeta}.
\tag{2.2}
$$
右边的两个有界算子交换：$D_\zeta$ 保持 $N_\zeta$，并与 $X$ 域交换。
而
$$
\|(D_\zeta|_{N_\zeta})^n\|\le\|D_\zeta^n\|
$$
给限制后的拟幂零性。

若有界 $L,K$ 交换且 $K$ 拟幂零，则
$\sigma(L+K)=\sigma(L)$。
确实，对 $z\notin\sigma(L)$，
$K(z-L)^{-1}$ 拟幂零，故 $I-K(z-L)^{-1}$ 可逆；
反向将 $L+K$ 与 $-K$ 交换即可。
应用于 (2.2) 得
$$
\boxed{\sigma(X_{N_\zeta})=\sigma(X_N).}
\tag{2.3}
$$
这一步使用实际有界限制的幂范数，没有把全空间 $X$ 的谱传给限制。

### 2.2 不交谱给所有 gauge 的双线性正交

反设两谱不交。
固定 $\zeta$，两谱
$\sigma(X_M)$、$\sigma(X_{N_\zeta})$
仍为不交的非空紧集。
对位于两者共同预解集的 $z$，原 $B$ 对称给
$$
B((z-X_M)^{-1}f,g)
=
B(f,(z-X_{N_\zeta})^{-1}g),
\qquad f\in M,\ g\in N_\zeta.
\tag{2.4}
$$
为核对域，将
$f'=(z-X_M)^{-1}f\in M\subset\operatorname{Dom}X$、
$g'=(z-X_{N_\zeta})^{-1}g\in N_\zeta\subset\operatorname{Dom}X$
代入
$B((z-X)f',g')=B(f',(z-X)g')$ 即得。

选取位于共同预解集的有限轮廓组，绕第一紧集的指数为1、绕第二紧集为0。
对 (2.4) 作 Riesz 积分，得到
$$
B(M,U_\zeta N)=0
\quad\text{对每个 dyadic }\zeta.
\tag{2.5}
$$

### 2.3 全 Fourier 消失与总本质支撑矛盾

对 $f\in M,g\in N$，
$$
B(f,U_\zeta g)
=\zeta^{-1}\int f(y)g(-1-y)\zeta^{-y}\,d\mu(y).
\tag{2.6}
$$
乘积属于 $L^1$。
(2.5) 使其所有 dyadic Fourier 系数为零；
有限柱条件期望在 $L^1$ 收敛，故
$$
f(y)g(-1-y)=0\quad\text{几乎处处}.
\tag{2.7}
$$

每个非零闭 $A$ 不变空间的总本质支撑都为全测。
具体地，取其可数稠密族，令支撑并为 $S$。
严格正权和不变性使 $S$ 的一个 odometer 平移包含于 $S$；
平移保测，故两者模零相等。
遍历性及 $S$ 非零测给 $\mu(S)=1$。

分别取 $M,N$ 的可数稠密族。
(2.7) 对全部可数向量对同时成立，
却要求两个全测总支撑 $S_M$ 与 $-1-S_N$ 不交，矛盾。
定理得证。

## 3. 连通谱、共同有限谱点和有界扰动

**推论 3.1。**
每个非零有界部分 $M$ 的紧谱 $\sigma(X_M)$ 连通。

若不连通，可将其分为两个不交非空紧谱集。
相应 Riesz 投影给
$M=M_1\dotplus M_2$，两部分均非零、闭，且处处属于 $X$ 域。
投影与 $A|_M$ 交换，故两部分仍 $A$ 不变。
它们的 $X$ 谱不交，与定理 2.1 矛盾。

特别，每个有限谱有界部分的谱必是单点。
令
$$
\mathscr F_X
=
\{M:\ M\text{ 为非零有界部分且 }\sigma(X_M)\text{ 有限}\}.
$$
若该族非空，定理 2.1 给唯一标量 $r_X$，使
$$
\boxed{\sigma(X_M)=\{r_X\}\qquad(M\in\mathscr F_X).}
\tag{3.1}
$$
更且任意有界部分 $N$ 都满足
$$
r_X\in\sigma(X_N).
\tag{3.2}
$$
这里不断言 $\mathscr F_X$ 非空。
若为空，下文任何要求非零自然多项式核的情形都不可能发生。

现在取任意 $H_0\in\mathcal A$，令 $\widetilde X=X+H_0$。
两者有同一完整域及同一有界部分族。
在每个这样的 $M$ 上，
$H_0|_M-\chi(H_0)I$ 拟幂零且与 $X_M$ 交换，故
$$
\sigma(\widetilde X_M)=\sigma(X_M)+\chi(H_0).
\tag{3.3}
$$
所以有限谱部分族相同，且在其非空时
$$
\boxed{r_{\widetilde X}=r_X+\chi(H_0).}
\tag{3.4}
$$
特别，R176 的所有指数倾斜
$$
X_b=X+H_{a,b},\qquad H_{a,b}\in\mathcal A,\quad\chi(H_{a,b})=0
$$
共享同一个 $r_X$。
这里的扰动限定为 $\mathcal A$；一般 $\mathfrak C$ 扰动没有自动获得零字符拟幂零差。

## 4. 自然多项式至多有一个点谱参数

取
$$
T=P(X)=\sum_{k=0}^p E_kX^k,\qquad
E_k\in\mathcal A,\quad E_p\in\mathcal A^\times,\quad p\ge1,
$$
$$
\operatorname{Dom}T=\operatorname{Dom}X^p,\qquad
q_0(z)=\sum_{k=0}^p\chi(E_k)z^k.
\tag{4.1}
$$
R176 给完整自然闭域、$C$ 自伴及核内有界化。
对 $M_\lambda=\ker(T-\lambda I)\ne0$，
$$
M_\lambda\in\mathscr F_X,\qquad
\sigma(X_{M_\lambda})\subset q_0^{-1}(\{\lambda\}).
\tag{4.2}
$$
因此 (3.1) 给
$$
\boxed{\lambda=q_0(r_X).}
\tag{4.3}
$$

**定理 4.1。**
$T$ 至多有一个点谱参数。
若 $\mathscr F_X$ 为空，它没有点谱；
若非空，唯一可能参数为 $q_0(r_X)$，但不保证该参数实际为特征值。

此结论同时适用于所有 (4.1) 型多项式，
并非分别为不同算子选一个无关的根。
特别，若两个字符多项式没有公共根，
对应自然算子不可能都具有非零核。
更一般，全部具有非零核的这类自然算子的字符多项式，
都必须在同一个 $r_X$ 处为零。

任何实际特征核都无限维：
它是非零闭 $A$ 不变空间，
而单射拟幂零 $A$ 在非零有限维不变空间上的限制不可能存在。

在 R181 的全平面谱分支，
$$
\sigma(T)=\mathbb C.
$$
当 $\ker(T-\lambda)=0$ 时，原空间的 $C$ 自伴性给稠密像；
闭图定理又排除在谱内同时满射。
故
$$
\boxed{\mathbb C\setminus\{q_0(r_X)\}
\text{ 全部属于连续谱}}
\tag{4.4}
$$
（当 $\mathscr F_X$ 为空时，整个 $\mathbb C$ 均为连续谱）。
唯一可能例外仍未排除，不能把 (4.4) 写成无条件的全连续谱定理。

## 5. 同一主行的全部权、幂次和辅助，共用同一例外值

先取任意非恒定标量多项式 $q$。
R176/R181 给
$$
(q(u)-\lambda)^m e^w
=
T_{m,\lambda,b}e^w,\qquad
m\ge1,\quad b\in\ell^2,
$$
其真实自然多项式的字符为
$(q(z)-\lambda)^m$，最高系数可逆；
$e^w$ 是循环图核心向量。
因此，只要上式不循环，就必有
$$
\boxed{\lambda=q(r_X).}
\tag{5.1}
$$
所以对固定 $u,q$，把所有 $m$ 和所有复 $\ell^2$ 指数权合在一起，
实际不循环的标量位移至多一个。
这是实际坏值的限制，不是说可以在未知 $r_X$ 时明确判断该例外值。

更一般，取有限个任意 $\ell^1$ 辅助 first
$$
v_\nu=c_{\nu,*}+\sum_j c_{\nu j}\chi_j,\qquad
\beta_\nu=c_{\nu,*}+\sum_j c_{\nu j},
$$
以及
$$
F(U,V)=\sum_{k=0}^p U^k r_k(V),\qquad
r_p(\beta)\ne0.
\tag{5.2}
$$
[R147 慢辅助切片附录](R147-appendix-bounded-slow-auxiliary-slices-and-polynomial-cyclicity.md)
已支付其全部实际混合 Bell 系数与自然域。
$(F(u,v)-\lambda)^m e^w$ 的自然实现最高系数为实际单位，
字符为
$$
(F(z,\beta)-\lambda)^m.
$$
故任何不循环情形必须满足
$$
\boxed{\lambda=F(r_X,\beta).}
\tag{5.3}
$$
该标量不随 $m$、$w$ 改变。
不同辅助系数或不同 $F$ 的核也使用同一个主行 $r_X$，
而不是为每个耦合另选根。

## 6. 首位碰撞必须发生在这个共同根

保持 (5.2) 的记号。
令联合首位为
$$
j_0=\min\{j:|a_j|+\sum_\nu|c_{\nu j}|>0\},\qquad h=2^{j_0},
$$
并写
$$
a=a_{j_0},\quad c=(c_{\nu j_0})_\nu,\quad
p_0(z)=F(z,\beta),\quad p_1(z)=F(z-2a,\beta-2c).
$$
这里 $a$ 可以为零。

**定理 6.1。**
若对某个 $m\ge1$ 和某个指数权 $w$，
$(F(u,v)-\lambda)^m e^w$ 不循环，则
$$
\boxed{p_0(r_X)=p_1(r_X)=\lambda.}
\tag{6.1}
$$

证明先取一般自然 Bell 多项式 $P$，对应点态符号
$G(U,V)=(F(U,V)-\lambda)^m$。
其字符为
$g_0(z)=(p_0(z)-\lambda)^m$。
记
$g_1(z)=(p_1(z)-\lambda)^m$。
R147 慢辅助附录的真实余数分解给，对每个 $\zeta^h\ne1$，
$$
P_\zeta(z)-P(z)=A^hJ_\zeta(z),\qquad
J_\zeta\in\mathcal A[z],
\tag{6.2}
$$
其中 $P_\zeta(z)=(\gamma_\zeta P)(z+D_\zeta)$，且
$$
\chi(J_\zeta(z))
=
\frac{e^{-2b_{j_0}}(\zeta^h-1)}{d_{j_0}}
\,[g_1(z)-g_0(z)].
\tag{6.3}
$$
(6.2) 是实际有界系数恒等式，已由有限 residue 分解除去 $A^h$；
不是从形式消失阶擅自作有界除法。
全部等式在真正的共同自然域上成立。

若 $M=\ker P(X_b)\ne0$，则
$M\subset\mathcal D_\infty(X_b)$ 且
$\sigma((X_b)_M)=\{r_X\}$。
已知 $g_0(r_X)=0$。
反设 $g_1(r_X)\ne0$，则 (6.3) 在 $r_X$ 处非零，
所以 $J_\zeta((X_b)_M)$ 是 $M$ 上的实际单位。
详细地，
$(X_b)_M-r_XI$ 拟幂零，
每个系数限制减其字符也拟幂零，
它们全部交换。
因此
$J_\zeta((X_b)_M)-\chi(J_\zeta(r_X))I$
为有限个交换拟幂零项之和，仍拟幂零，证明单位结论。

R151 §3.1 给 $\overline{A^hM}=M$，
所以 (6.2) 推出
$$
\overline{(P_\zeta(X_b)-P(X_b))M}=M.
$$
对 $f\in M$、$g\in U_\zeta M=\ker P_\zeta(X_b)$，
两者都属于全部所需自然域；
原 $B$ 对称给
$$
B((P_\zeta-P)f,g)=0.
$$
取左边像的闭包，得到
$$
B(M,U_\zeta M)=0\qquad(\zeta^h\ne1).
\tag{6.4}
$$

由 (2.6)，任意反射乘积的 Fourier 支撑只在有限群 $\mu_h$，
所以在每个模 $h$ 柱上为常数。
由总本质支撑全测，每个柱上可选 $f_0,g_0\in M$，
使乘积在该柱上为非零常数。
任意 $f\in M$ 的 $f(y)g_0(-1-y)$ 也为柱常数，
故 $f$ 在该柱上为 $f_0$ 的标量倍数。
于是 $\dim M\le h$，与非零 $A$ 不变空间不能有限维矛盾。

所以 $g_1(r_X)=0$。
两个标量幂均为零恰给 (6.1)，证明完成。
本证明没有把其他 Riesz 根支被排除，误写成原 Bell 系数消失。

### 6.1 普通单模式多项式的固定根对

无辅助时，令 $\alpha=a_{j_a}\ne0$ 为主首位系数。
任何不循环的 $q(u)e^w$ 必须满足
$$
\boxed{q(r_X)=q(r_X-2\alpha)=0.}
\tag{6.5}
$$
这是两个不同的标量根，但未知核内的 $X$ 谱仍只有 $\{r_X\}$。
第二个标量根不自动产生第二个非零 Riesz 子空间。

因此，对固定 $u$，所有可能不循环的二次多项式，
若存在，都只能是
$$
c(z-r_X)(z-r_X+2\alpha),\qquad c\ne0.
\tag{6.6}
$$
R144/R147 以前已排除不满足首位根差的二次式；
这里新增的是不同二次式和不同权必须共用同一个有序根对。
单根平移幂的循环性仍归于旧 R144/R147，不重新登记。

### 6.2 全阶共振偏离的共同参数

沿用 R270C 和
[R236 全阶字符互素附录](R236-appendix-real-dyadic-factor-character-coprimality-and-all-order-deviations.md)
的
$$
F_q=\sum_k q_kF_k,\qquad
v_c=\sum_j c_j(\chi_j-1),\qquad c\in\ell^1.
$$
假设 $c$ 在主首位之前为零，记 $\delta=c_{j_a}$。
其两个首位字符切片为
$$
q(z),\qquad q(z)-2\alpha q'(z)-2\delta.
$$
因此，对任意 $m,w$，若
$(F_q+v_c-\lambda)^m e^w$ 不循环，则
$$
\boxed{
\lambda=q(r_X),\qquad
\delta=-\alpha q'(r_X).
}
\tag{6.7}
$$
R236 已给有限候选集
$\{q(z):\alpha q'(z)+\delta=0\}$；
这里不重复这个互素充分条件。
新增的是全部偏离尾、全部权、全部幂的实际坏值都只能来自同一个 $r_X$。
特别，当 $q(z)=z^2$ 时，能出现任何坏值的首位偏离系数
也至多一个：$\delta=-2\alpha r_X$。

## 7. 两种剩余二次核不能同时出现

这一应用不依赖尾率。
令 $\alpha=a_{j_a}\ne0$，并取任意首位之后的可和偏离
$c\in\ell^1$，即 $c_j=0$ 对 $j\le j_a$。
考虑
$$
S(u)=u^2-\alpha^2,
$$
$$
R_c(u)=F_2+v_c
=u^2+\sum_j(2a_j^2+c_j)(\chi_j-1).
\tag{7.1}
$$
它们的自然字符分别为 $z^2-\alpha^2$、$z^2$，没有公共根。
由定理 4.1：

- 若某个 $S(u)^m e^w$ 不循环，则对每个上述 $c$、
  每个 $n\ge1$ 和每个指数权 $\widetilde w$，
  $R_c(u)^n e^{\widetilde w}$ 全部循环。
- 若某个 $R_c(u)^n e^w$ 不循环，则对全部 $m\ge1$ 和全部指数权
  $\widetilde w$，$S(u)^m e^{\widetilde w}$ 全部循环。

第一类未知核由 (6.5) 只能有 $r_X=\alpha$；
第二类则只能有 $r_X=0$。
这给两类剩余核的互斥性，没有选择其中哪一类实际存在。

例如 R147 慢辅助附录的
$F=U^3+V^2$、$\alpha=c_{10}=1$、$\beta=0$
有两个字符候选
$$
2\pm\frac{10}{3\sqrt3}.
$$
上述定理进一步表明：将该例的所有权和所有点态幂合在一起，
两候选至多一个能实际失败。
若共同 $r_X$ 不是 $1\pm1/\sqrt3$，两个候选也都循环。
不据此指定究竟哪个候选可删。

## 8. 证明边界和继续保留的困难

1. 在空谱相位缺陷分支，旧 R138/R155 已排掉这些核；
   本稿没有为该分支登记新的排核范围。
2. 在有界 first 分支 $a\in\ell^1$，全 $H$ 本身就是有界部分，
   $r_X=a_*+\sum_j a_j$ 已由原 $\mathcal A$ 字符确定。
   本稿对未知 $r_X$ 的实质限制来自非绝对可和主行。
3. R259 已处理 $|a_j|\asymp(j+1)^{-\sigma}$、
   $\sigma>1/2$ 的普通简单根单模式多项式；
   R268/R269 又覆盖相应熵预算下的全部重数及有限头。
   本稿不把这些旧普通两根范围重新列为待解。
4. R236 同日的二位标量消元已经排除满足定量双池条件的全阶共振偏离 $F_q+v_c-\lambda$，包括两侧幂排序与可和幂次偏离、任意有限头例外及物理排列；§7 的互斥只增加一般未覆盖行的定性约束，不重计这些规则类。
5. 共同根 $r_X$ 只在非零有限谱部分存在时定义。
   本文没有构造这种部分，也没有证明它不存在。
6. 有限谱只剩一根，仍允许无限维、单射的拟幂零限制
   $X_M-r_XI$。
   不能由全空间某因子的单射稠密像，推出它在未知 $M$ 上稠密。
7. 对独立的多个无界慢模式，本文没有提供多变量 Bézout 单位；
   有界辅助在 §5 中先实际化为 $\mathcal A$ 系数，范围不能省略。
8. $C$ 自伴、跨核配对和所有自然域都在原空间证明；
   未在未知限制或子商中假定一个不存在的共轭。

普通 Hilbert ISP 以及最后单根慢共振核继续保留。
