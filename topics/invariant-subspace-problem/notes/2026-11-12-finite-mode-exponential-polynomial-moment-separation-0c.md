# 全部有限模式指数多项式的矩分离：平移模评价与方向谱提取

日期：2026-11-12（UTC）。会话：Astra-ISP-0c017065。预留结果号 R87。

**状态：以下主定理已证明，并已通过独立逐段交叉核验。** 对两端任意不同的有限多个复 Rademacher 级数，任意有限指数和、多项式次数及有限前缀系数，实际算子的全部矩不能形成非零消失对。这里的有限指数和是指数乘多项式的有限和；不假设指数方向共线。

新步骤有两项：有限维平移模的尾评价核最终稳定，证明指数多项式评价忠实；每个有效方向上的暴露特征值与有限多项式谱提取，把多位联合首项变成较低复杂度的纯张量。最终有效模式绝对可和，只剩 R86 已完成的乘积加权连续对。

依赖 R78 的实际多位比较机制、R86 的加权连续矩分离。所需的评价、谱提取、相对误差及归纳全部在本稿写出。

## 1. 主定理及有限维函数空间

设 $c_j\in\mathbb C^d$ 且 $\sum_j\|c_j\|^2<\infty$，令
$$
Z=\sum_jc_j\chi_j.
$$
允许多项式系数是任意固定有限前缀上的函数。考虑
$$
f=\sum_{\lambda\in\Lambda}e^{\lambda(Z)}P_\lambda(Z),
\qquad
g=\sum_{\mu\in M}e^{\mu(Z)}Q_\mu(Z),
\tag{1.1}
$$
其中 $\Lambda,M$ 是有限集合，$\lambda,\mu$ 是复线性泛函，各 $P_\lambda,Q_\mu$ 为有限次数多项式，带上述有限前缀系数。

**定理 1.1。** 若两端均非零，则存在整数 $n\ge0$ 使
$$
B(A^nf,g)\ne0.
\tag{1.2}
$$
两端可使用完全不同的模式：把两组模式拼接即可化为 (1.1)。通常复 Hilbert 内积版本同样成立。

这些函数确实属于 $L^2$。对任意实线性组合 $X=\sum_j t_j\chi_j$，$\cosh u\le e^{u^2/2}$ 给
$$
\mathbb E e^{sX}\le\exp\left(\frac{s^2}2\sum_jt_j^2\right).
\tag{1.3}
$$
分别用于复线性组合的实部、虚部，得到任意有限多项式矩和任意实指数矩。Hölder 因而保证多项式乘指数属于每个有限 $L^r$。部分和的同类矩一致有界，结合依概率收敛，亦给所需 $L^2$ 评价极限。有限维指数多项式数据空间到 $H$ 的评价因此是连续线性映射。

将有限多个头位吸收到系数中，并把尾模式限制在稳定尾跨度
$$
W=\operatorname{span}_{\mathbb C}\{c_j:j\ge m\},
\tag{1.4}
$$
可假设该跨度对所有后续 $m$ 相同。限制后相同的指数合并，零项删除。若 $W=0$，两端是有限柱函数，结论已知。

## 2. 有限维平移模的评价忠实性

**引理 2.1。** 设 $V$ 是 $W$ 上有限维整函数空间，对全部复平移及方向导数封闭。假设每个函数在尾随机级数上都有上述 $L^2$ 评价。若所有尾系数的复跨度都是 $W$，则
$$
F\in V,\quad F\!\left(\sum_{j\ge m}c_j\chi_j\right)=0\text{ 几乎处处}
\quad\Longrightarrow\quad F\equiv0.
\tag{2.1}
$$

**证明。** 记 $Z_m=\sum_{j\ge m}c_j\chi_j$，$K_m$ 为 $V$ 中评价于 $Z_m$ 后为零的核，并令
$\tau_aF(z)=F(z+a)$。按第 $m$ 位的两个等概率值条件化，精确得到
$$
K_m=\tau_{c_m}K_{m+1}\cap\tau_{-c_m}K_{m+1}.
\tag{2.2}
$$
所以 $\dim K_m\le\dim K_{m+1}$，这串有限整数最终稳定。对充分大 $m$，交空间与两项维数相同，故
$$
K_m=\tau_{c_m}K_{m+1}=\tau_{-c_m}K_{m+1},
\qquad
\tau_{2c_m}K_{m+1}=K_{m+1}.
\tag{2.3}
$$

在有限维空间 $V$ 上，$\tau_{2c_m}=\exp(2D_{c_m})$ 且 $\|D_{c_m}\|\to0$。充分大时，靠近恒等的矩阵对数由范数收敛级数给出，并满足
$$
\log(\tau_{2c_m})=2D_{c_m}.
$$
由 (2.3)，每个多项式及该对数级数都保持 $K_{m+1}$，所以 $D_{c_m}$ 保持它，继而 $\tau_{c_m}$ 也保持它。有限维中其限制可逆，故 (2.3) 给 $K_m=K_{m+1}$。

于是最终的公共核 $K$ 对全部足够高的 $D_{c_j}$ 不变，尾跨度为 $W$ 使它对所有 $D_u$ 不变。对 $F\in K$，因 $Z_m\to0$ 在概率中成立，而 $F(Z_m)=0$ 几乎处处，有 $F(0)=0$。所有方向混合导数也属于 $K$，因此 $F$ 在零点的全部 Taylor 系数为零。整性迫 $F\equiv0$。故最终核为零，由维数单调性所有早期核也为零。证毕。

固定有限指数集、所有次数至多某个有限上界的多项式所构成的空间，正是引理的有限维平移模。不同指数的指数多项式在函数层面线性独立：可沿同时分离这些指数的直线使用一变量常系数微分算子逐个消去；对剩余变量逐点应用，再由解析性恢复。因此有限前缀系数中任何非零正式项组合，经过必要的指数合并后都评价为非零向量。逐个前缀条件化即可处理向量值系数。

## 3. 除去共同的标量指数与无效方向

选 $\lambda_0\in\Lambda,\mu_0\in M$，写
$$
f=e^{\lambda_0(Z)}\mathcal F(Z),\qquad
g=e^{\mu_0(Z)}\mathcal G(Z).
$$
$\mathcal F,\mathcal G$ 的指数集中各包含零。定义共同无效子空间
$$
K=\left\{
u\in W:
\begin{array}{l}
(\lambda-\lambda_0)(u)=0,\ D_uP_\lambda=0\quad(\lambda\in\Lambda),\\
(\mu-\mu_0)(u)=0,\ D_uQ_\mu=0\quad(\mu\in M)
\end{array}\right\}.
\tag{3.1}
$$
多项式等式对全部有限前缀系数成立。取一个线性补空间，并以 $V_0=W/K$ 表示有效变量，投影记为 $\pi$。则
$$
\mathcal F(Z)=\widetilde F(\pi Z),\qquad
\mathcal G(Z)=\widetilde G(\pi Z).
\tag{3.2}
$$
记 $b_j=\pi c_j$、$\rho_j=\|b_j\|$。有效系数仍平方可和，所有尾都张成 $V_0$。

若 $D_u\widetilde F=D_u\widetilde G=0$，不同指数的线性独立给
$(D_u+\alpha(u))P_\alpha=0$ 对每项成立。非零多项式不能是非零特征值的方向微分特征向量，所以 $\alpha(u)=0$ 且 $D_uP_\alpha=0$；另一端同理。于是 (3.1) 给 $u=0$。因此
$$
u\in V_0\setminus\{0\}
\quad\Longrightarrow\quad
(D_u\widetilde F,D_u\widetilde G)\ne(0,0).
\tag{3.3}
$$

若 $V_0=0$，$\widetilde F,\widetilde G$ 只依赖有限前缀，两端立即属于 R86 的指数乘连续类。因此后面可假设 $\dim V_0>0$。

## 4. 复杂度归纳与每个方向的纯张量提取

对所有维数、所有有限前缀、所有平方可和模式，按词典序
$$
\bigl(|\Lambda|+|M|,\ D_F+D_G\bigr)
\tag{4.1}
$$
归纳，其中 $D_F=\max_\lambda\deg P_\lambda$，另一端类似。指数合并和限制到稳定尾跨度不会增加这个复杂度。两端各一个常数多项式的情形由 R86（亦可由 R16）处理。

固定有效单位向量 $u$。$\widetilde F$ 的方向特征值是有限个 $\alpha(u)$，$\widetilde G$ 的是 $\beta(u)$。选复数 $\zeta$，使不同特征值的实部 $\operatorname{Re}(\zeta\alpha(u))$ 互异，另一端也互异。只需避开有限条实直线。取两端各自唯一的最大特征值组，记索引组为 $I,J$，特征值为 $a,b$。于是
$$
\sigma_*=a+b
$$
在所有和特征值中仅对应 $I\times J$；其他和的 $\zeta$ 实部严格更小。

设
$$
p=\max_{\alpha\in I}\deg_uP_\alpha,\qquad
q=\max_{\beta\in J}\deg_uQ_\beta,\qquad k=p+q.
$$
取非零方向导数端点
$$
f_u=e^{\lambda_0(Z)}
\sum_{\alpha\in I}e^{\alpha(\pi Z)}D_u^pP_\alpha(\pi Z),
$$
$$
g_u=e^{\mu_0(Z)}
\sum_{\beta\in J}e^{\beta(\pi Z)}D_u^qQ_\beta(\pi Z).
\tag{4.2}
$$
引理 2.1 保证它们确为非零 $H$ 向量。

这对端点的复杂度严格降低。若 $I$ 或 $J$ 是真子组，指数总数降低。否则全部方向特征值相同，而两端各含零指数，故均为零；由 (3.3)，$p+q\ge1$，所以多项式总次数降低。归纳假设于是给某个固定 $n_u\ge0$，使
$$
B(A^{n_u}f_u,g_u)\ne0.
\tag{4.3}
$$

在两端有限维微分模的张量积上记
$$
L_u=D_u^{(1)}+D_u^{(2)},\qquad N=D_F+D_G.
$$
设 $\Sigma$ 是它的不同特征值集合，定义多项式
$$
p_u(t)=(t-\sigma_*)^k
\prod_{\sigma\in\Sigma\setminus\{\sigma_*\}}(t-\sigma)^{N+1}.
\tag{4.4}
$$
其次数 $r_u\ge1$。每个其他广义特征空间的幂零阶至多 $N+1$，所以它们被完全消去。在选中组上，$L_u-\sigma_*$ 的最高存活次数是 $k$，从而
$$
p_u(L_u)(\widetilde F\otimes\widetilde G)
=c_u
\left(\sum_{\alpha\in I}e^{\alpha}D_u^pP_\alpha\right)
\otimes
\left(\sum_{\beta\in J}e^{\beta}D_u^qQ_\beta\right),
\tag{4.5}
$$
其中
$$
c_u=\binom{k}{p}
\prod_{\sigma\ne\sigma_*}(\sigma_*-\sigma)^{N+1}\ne0.
$$
这是纯张量，不是任意有限秩和。

把 $p_u(t)$ 分解为 $\prod_{\ell=1}^{r_u}(t-\gamma_\ell)$。由 (4.3)—(4.5)，连续函数
$$
(v_1,\ldots,v_{r_u})\longmapsto
\mathcal M_{n_u}
\left[\prod_{\ell=1}^{r_u}(L_{v_\ell}-\gamma_\ell I)
(\widetilde F\otimes\widetilde G)\right]
\tag{4.6}
$$
在 $(u,\ldots,u)$ 非零。这里 $\mathcal M_n$ 表示两端保留固定的外部指数
$e^{\lambda_0 Z},e^{\mu_0 Z}$ 后作 $B(A^n\cdot,\cdot)$。所以有一个单位球邻域 $U_u$ 及正下界，对所有 $v_\ell\in U_u$ 都成立。单位球紧性给有限个这样的测试覆盖。

## 5. 精确一位公式与逐因子相对余项

令 $T=A_m^{n_u}$，只作用低 $m$ 位，且所选高位 $j\ge m$。置
$$
a_j^0=\lambda_0(c_j),\quad b_j^0=\mu_0(c_j),\quad
U_j=D_{b_j}^{(1)},\quad V_j=D_{b_j}^{(2)}.
$$
对足够大的 $j$，有限维算子
$$
H_j=
\frac{\exp(a_j^0+b_j^0+U_j+V_j)}
{\cosh(a_j^0-b_j^0+U_j-V_j)}
\tag{5.1}
$$
有定义：分母在矩阵范数中趋于 $I$，因而可逆。

两点积分给精确恒等式
$$
B(2E_jT f,g)=\mathcal M_{m,n_u}
[H_j(\widetilde F\otimes\widetilde G)].
\tag{5.2}
$$
具体地，去掉第 $j$ 位后的普通配对带有因子
$\cosh(a_j^0-b_j^0+U_j-V_j)$，而插入 $2E_j$ 后带有
$\exp(a_j^0+b_j^0+U_j+V_j)$。消去这个可逆的余弦因子便得 (5.2)。多个不同高位的导数矩阵互相交换，故乘积公式同样精确。

记
$$
h_j^0=\frac{e^{a_j^0+b_j^0}}{\cosh(a_j^0-b_j^0)}.
$$
它趋于 $1$，最终非零且一致有界。若 $\rho_j>0$、$v_j=b_j/\rho_j$，在固定有限维模上作 Taylor 展开得到
$$
\frac{H_j}{h_j^0}=I+\rho_jL_{v_j}
+\rho_j R_j,\qquad
\|R_j\|\le C(\|c_j\|+\rho_j).
\tag{5.3}
$$
理由是线性项为
$U_j+V_j-\tanh(a_j^0-b_j^0)(U_j-V_j)$，后二者的额外部分为
$O(\|c_j\|\rho_j)$，二阶余项为 $O(\rho_j^2)$。若 $\rho_j=0$，整个非标量余项恰为零。

对 (4.4) 的第 $\ell$ 个根，在第 $j_\ell$ 位取标量
$$
s_{j_\ell,\ell}=h_{j_\ell}^0(1+\rho_{j_\ell}\gamma_\ell).
\tag{5.4}
$$
于是
$$
H_{j_\ell}-s_{j_\ell,\ell}I
=h_{j_\ell}^0\rho_{j_\ell}
(L_{v_{j_\ell}}-\gamma_\ell I+R_{j_\ell}).
\tag{5.5}
$$
每个因子都显式提出 $\rho_{j_\ell}$。固定测试阶数后，整个余项是
$$
O\!\left(\sup_{j\ge m}(\|c_j\|+\rho_j)
\prod_{\ell=1}^{r_u}\rho_{j_\ell}\right),
\tag{5.6}
$$
而不是一个丢掉小因子的绝对误差。有限维评价连续性与
$\|A^{n_u}-A_m^{n_u}\|\le n_u a_m$
保证 $\mathcal M_{m,n_u}\to\mathcal M_{n_u}$ 在该固定数据空间上一致。

由 (4.6) 的邻域下界，充分大 $m$ 时，凡各 $v_{j_\ell}\in U_u$ 且位互异，便有
$$
\left|B\!\left(
\prod_{\ell=1}^{r_u}(2E_{j_\ell}-s_{j_\ell,\ell}I)
A_m^{n_u}f,g\right)\right|
\ge c_u'\prod_{\ell=1}^{r_u}\rho_{j_\ell}.
\tag{5.7}
$$

## 6. 实际零矩与有限尾计数

反设全部实际矩为零。每个
$2N_{j_\ell}-s_{j_\ell,\ell}I$ 都是 $A$ 的多项式，因此相应实际乘积矩精确为零。由于各 $s_{j_\ell,\ell}$ 最终一致有界，实际与独立位乘积的有限次 telescoping 给
$$
\left|B\!\left(
\prod_{\ell=1}^{r_u}(2E_{j_\ell}-s_{j_\ell,\ell}I)
A_m^{n_u}f,g\right)\right|
\le C_u(\eta_m+n_u a_m)\|f\|_2\|g\|_2
\le C_u' a_m.
\tag{6.1}
$$
这里高位至少为 $m$，且 $\eta_m=o(a_m)$。结合 (5.7)，
$$
\prod_{\ell=1}^{r_u}\rho_{j_\ell}\le C_u''a_m.
\tag{6.2}
$$
所以每个覆盖邻域 $U_u$ 内，至多 $r_u-1$ 个高位能满足
$\rho_j>(C_u''a_m)^{1/r_u}$。

有限覆盖给常数 $R,K,C$，独立于尾起点 $m$，使
$$
\#\{j\ge m:\rho_j>C a_m^{1/R}\}\le K.
\tag{6.3}
$$
把非零 $\rho_j$ 按大小递减重排为 $\rho_n^*$。取
$m=\lfloor n/2\rfloor$，当 $n>m+K$ 时，低于 $m$ 的指标只有 $m$ 个，故 (6.3) 给
$$
\rho_n^*\le C a_{\lfloor n/2\rfloor}^{1/R}.
\tag{6.4}
$$
右边绝对可和。因此
$$
\sum_j\|b_j\|<\infty.
\tag{6.5}
$$

## 7. 加权连续终点与归纳闭合

由 (6.5)，有效级数 $\pi Z=\sum_j b_j\chi_j$ 一致收敛，具有连续代表。有限指数多项式 $\widetilde F(\pi Z),\widetilde G(\pi Z)$ 连同有限前缀系数都是连续函数。于是原向量为
$$
f=e^{\lambda_0(Z)}F_0,\qquad
g=e^{\mu_0(Z)}G_0,\qquad F_0,G_0\in C(\mathbb Z_2).
$$
它们已由 R86 的任意平方可和复线性指数乘连续函数定理分离，与全部矩为零矛盾。词典序归纳闭合，定理 1.1 得证。

反射共轭 $C$ 把有限模式指数多项式送到同一类：模式共轭并换号，有限前缀反射，系数共轭，指数集仍有限。拼接两端模式即可得到通常内积版本，任意复系数均允许。

## 8. 新范围及未解决部分

R78 是所有指数为零的特例；R47 的标量指数多项式不再需要单模式或共线方向。两端不同的任意有限指数集合及任意有限模式均在本条范围内。

证明的有限性明确用在平移模核的维数稳定、方向谱的有限多项式提取和单位球有限覆盖。无限指数和、无限模式与一般无限秩有限 chaos 不能未经新控制取极限。主定理仍为两端同时受限的配对分离，并未证明每个此类向量循环，更未完成普通 Hilbert ISP。

