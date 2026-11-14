# R181：真实高次近特征序列与交换代数系数多项式的谱三分

日期：2026-11-12（UTC）。作者：critical_kernel。根代理预留 R181。

状态：完整证明。本文给真实闭 Bell 实现的完整谱集合。两个非空谱分支均不自动排核；绝对可和分支甚至允许整个多项式算子为零。没有把第一阶近特征关系直接提升为高次幂关系。

## 1. 定理与准确范围

设

$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad 0\ne a\in\ell^2,
$$

令 $X=X_u$ 为 R125 的实际闭一阶乘子。取

$$
P(X)=\sum_{k=0}^pE_kX^k,\qquad
p\ge1,\quad E_k\in\mathcal A,\quad E_p\in\mathcal A^\times,
\tag{1.1}
$$

其准确自然域是 $\operatorname{Dom}X^p$。R176 已证明它闭、稠密定义、$C$ 自伴。定义字符多项式

$$
q_0(z)=\sum_{k=0}^p\chi(E_k)z^k.
\tag{1.2}
$$

因为 $\chi(E_p)\ne0$，$q_0$ 的次数仍为 $p$。记相位缺陷

$$
\mathcal D(a,\theta)
=\sum_j\left(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\right).
$$

**主定理。**

$$
\boxed{
\sigma(P(X))=
\begin{cases}
\{q_0(a_*+\sum_ja_j)\},&a\in\ell^1,\\
\varnothing,&a\notin\ell^1,\ \mathcal D(a,\theta)<\infty
\text{ 对某个 }\theta,\\
\mathbb C,&a\notin\ell^1,\ \mathcal D(a,\theta)=\infty
\text{ 对全部 }\theta.
\end{cases}}
\tag{1.3}
$$

在第三种情形，对每个 $\mu\in\mathbb C$，都有有限柱单位向量 $x_m$ 满足

$$
x_m\rightharpoonup0,\qquad
\|(P(X)-\mu I)x_m\|\longrightarrow0.
\tag{1.4}
$$

这些向量确实属于全部自然幂域。因此每个 $\mu$ 都属于近似点谱，而且 $P(X)-\mu I$ 不是上半 Fredholm 算子。

在空谱分支，结论更允许全部 $E_k\in\{A\}'$、最高系数为有界单位。全平面分支的系数范围则保留为 $\mathcal A$，因为证明使用实际 UHF 边界上的标量特征；不能将一般有界交换子擅自代入。

## 2. 对任意有限乘积参考态统一的次数估计

令 $S_j=I-2E_j$ 为纯一位算子。取任意有限位乘积单位向量

$$
h=\bigotimes_{j\ge m}h_j,
$$

其中每个 $h_j\in\mathbb C^2$ 单位，且充分高位 $h_j=\Omega=(e_0+e_1)/\sqrt2$。设

$$
s_j=\langle S_jh_j,h_j\rangle,\qquad
\beta=\sum_{j\ge m}a_js_j.
\tag{2.1}
$$

因为 $\langle S_j\Omega,\Omega\rangle=0$，这个 $\beta$ 是有限和。

用 $h_j$ 作为每位的真空，任取正交单位向量 $h_j^\perp$ 作激发态。相对于这一乘积基，令 $\mathcal N_h$ 计数激发位，$\Lambda_h=I+\mathcal N_h$。

### 2.1 纯中心化尾的界

在基 $(h_j,h_j^\perp)$ 中，$S_j-s_jI$ 的真空对角元为0。其余三个矩阵元的绝对值不超过6，因为 $\|S_j\|<3$、$|s_j|\le\|S_j\|$。

于是纯中心化尾

$$
T_{m,h}^0=\sum_{j\ge m}a_j(S_j-s_jI)
$$

是一个产生项、一个消灭项和一个占据对角项之和。每类加权系数的 $\ell^2$ 范数至多 $6\|a_{\ge m}\|_2$。在激发次数 $q$ 上，各类范数分别由

$$
6\sqrt{q+1}\|a_{\ge m}\|_2,\quad
6\sqrt q\|a_{\ge m}\|_2,\quad
6\sqrt q\|a_{\ge m}\|_2
$$

控制。占据项用的是
$\left|\sum_{j\in F}a_jd_j\right|\le6\sqrt{|F|}\|a_{\ge m}\|_2$。

因此对整数 $s\ge0$，

$$
\boxed{
\|\Lambda_h^s T_{m,h}^0v\|
\le6(2^s+2)\|a_{\ge m}\|_2
\|\Lambda_h^{s+1/2}v\|.
}
\tag{2.2}
$$

常数与哪些位改变了参考态、改变的位数以及 $\beta$ 的大小都无关。大标量 $\beta$ 已在每个位的真空对角元处准确消去。

### 2.2 任意乘积参考态下的局部支撑界

若一个有界算子 $D$ 只作用于某个含 $L$ 位的集合，则

$$
\boxed{
\|\Lambda_h^sDv\|
\le(L+1)^s\|D\|\|\Lambda_h^sv\|.
}
\tag{2.3}
$$

证明：按该集合外的激发次数 $q$ 正交分解。在每一块中，集合内次数位于 $0,\ldots,L$，所以左侧最高权与右侧最低权的比至多

$$
\frac{(q+L+1)^s}{(q+1)^s}\le(L+1)^s.
$$

逐块平方求和即可。这个证明不依赖每位所选的真空向量。

## 3. 真实 carry 在任意乘积参考态上的统一控制

实际局部算子为

$$
N_j=A^{2^j}/d_j,\qquad
V_j=(I-N_j)(I+N_j)^{-1}.
$$

R171 的有限链截断给

$$
V_j-S_j=\sum_{\ell\ge j+1}B_{j,\ell},
\tag{3.1}
$$

其中每个 $B_{j,\ell}$ 只作用于位 $[j,\ell]$，并有

$$
\|B_{j,\ell}\|
\le18\,\frac{\alpha_\ell}{\alpha_j},
\qquad
\frac{\alpha_\ell}{\alpha_j}
\le\eta_j\eta_*^{\ell-j-1},
\quad
\eta_*=\sup_j\eta_j<1/4.
\tag{3.2}
$$

为明确其实际来源，截断 $N_j^{[\ell]}$ 是有限链算子，平方范数至多 $\eta_j$，故 $\|(I+N_j^{[\ell]})^{-1}\|<3$。相邻有限截断之差范数为 $\alpha_\ell/\alpha_j$；对 Cayley 变换使用准确逆差公式，给 (3.2) 的18。它不使用形式除法。

定义实际尾扰动

$$
K_m=\sum_{j\ge m}a_j(V_j-S_j)
=\sum_{j\ge m}\sum_{\ell\ge j+1}a_jB_{j,\ell}.
$$

由 (2.3)、(3.2) 和 Cauchy–Schwarz，

$$
\boxed{
\|\Lambda_h^sK_mv\|
\le\kappa_s\|a_{\ge m}\|_2\|\Lambda_h^sv\|,
}
\tag{3.3}
$$

其中可取与 $m,h$ 都无关的有限常数

$$
\kappa_s=
18\|\eta\|_2
\sum_{L\ge1}(L+2)^s\eta_*^{L-1}.
\tag{3.4}
$$

该级数在相应加权算子范数中绝对收敛。每个有限局部项保持 $\operatorname{Dom}\Lambda_h^s$；由 $\Lambda_h^s$ 闭性，极限也保持该域。

任意有限乘积基变换只把这些局部算子在相同的位集合内作酉共轭，支撑长度及通常算子范数不变。因此 (3.3) 确实对所有上述乘积参考态统一，并非只对原常函数真空成立。

令实际尾闭乘子

$$
Z_m=\sum_{j\ge m}a_jV_j.
$$

它只作用高于等于 $m$ 的尾空间。对中心化算子 $T_{m,h}=Z_m-\beta I$，(2.2)—(3.3) 给

$$
\|\Lambda_h^sT_{m,h}v\|
\le D_s\|a_{\ge m}\|_2\|\Lambda_h^{s+1}v\|,
\qquad
D_s=6(2^s+2)+\kappa_s.
\tag{3.5}
$$

这里的域是实际闭域：先在有限柱上证明，再用有限柱的 $\Lambda_h^{s+1}$ 图逼近、$Z_m$ 的闭性与 $\Lambda_h^s$ 的闭性，延拓到全部 $\operatorname{Dom}\Lambda_h^{s+1}$。有限改变乘积参考态保持有限柱空间，所以这个闭包步骤没有改变核心。

因为 $h$ 是相对真空，$\|\Lambda_h^rh\|=1$。反复使用 (3.5)，得到

$$
\boxed{
h\in\operatorname{Dom}Z_m^r,\qquad
\|(Z_m-\beta I)^rh\|
\le C_r\|a_{\ge m}\|_2^r,
\quad
C_r=\prod_{s=0}^{r-1}D_s,
}
\tag{3.6}
$$

并约定 $C_0=1$。这是全部固定中心幂的统一真实估计；常数不随乘积态使用的有限位数增长。

## 4. 无可和相位缺陷给任意指定的尾期望

现在假设 $a\notin\ell^1$，且每个 $\theta$ 都有 $\mathcal D(a,\theta)=\infty$。

对固定 $m$，令

$$
S_{m,N}=\sum_{m\le j<N}a_j,\qquad
L_{m,N}=\sum_{m\le j<N}|a_j|.
$$

则

$$
\boxed{L_{m,N}-|S_{m,N}|\longrightarrow+\infty
\quad(N\to\infty).}
\tag{4.1}
$$

证明：这些量等于

$$
\min_\theta\sum_{m\le j<N}
\left(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\right).
$$

如果它们有有界子列，选取对应的最小方向，再在圆周上取收敛子列 $\theta_N\to\theta_*$。对每个固定有限截断先取极限，其缺陷和不超过同一上界。最后单调取无穷和，得到尾上某个可和缺陷方向；加入有限头仍可和，与假设矛盾。

纯局部 $S_j=I-2E_j$ 的数值域准确为闭圆盘 $\overline D(1,1)$：对单位 $h_j$，

$$
\langle S_jh_j,h_j\rangle=1-2(h_j)_0\overline{(h_j)_1},
$$

而后一个乘积覆盖半径 $1/2$ 的闭圆盘。因此有限和的乘积态期望覆盖

$$
\overline D(S_{m,N},L_{m,N}).
\tag{4.2}
$$

给任意目标 $\beta\in\mathbb C$，由 (4.1) 可选 $N$ 使
$L_{m,N}-|S_{m,N}|\ge|\beta|$。于是 $\beta$ 属于 (4.2)，可逐位选择单位向量 $h_j$，使

$$
\sum_{m\le j<N}a_j\langle S_jh_j,h_j\rangle=\beta.
\tag{4.3}
$$

充分高位取 $\Omega$，得到 §2 所需的有限乘积参考态。

## 5. 全1头的真实 carry 与所有中心幂近特征

固定 $\lambda\in\mathbb C$。令

$$
\beta_m=a_*+\sum_{j<m}a_j.
$$

在 §4 中取尾目标

$$
\beta=\lambda-\beta_m,
$$

选择相应有限尾乘积单位态 $h_m$。低 $m$ 位取物理全1单位态，定义

$$
x_m=e_{1^m}\otimes h_m.
\tag{5.1}
$$

它是单位有限柱向量。其支撑包含于测度 $2^{-m}$ 的全1头柱，所以 $x_m\rightharpoonup0$。又由实际权公式，

$$
\|Ax_m\|\le\alpha_m\longrightarrow0.
\tag{5.2}
$$

现在控制完整 $X$ 的高次作用。写

$$
X-\lambda I=H_m+(Z_m-\beta I),
\qquad
H_m=\sum_{j<m}a_j(V_j-I).
\tag{5.3}
$$

$H_m$ 有界，且与实际尾 $Z_m$ 域交换。这个交换是实际 $N_j$ 函数的交换，不是把纯 $E_j$ 模型错误地放进低头。

设 $\Pi_{1,m}$ 为全1头柱投影。真实进位递推表明，对 $i<m$，

$$
\|N_i\Pi_{1,m}\|\le\frac{\alpha_m}{\alpha_i}
\le\eta_{m-1}.
$$

由于 $N_i$ 与自己的有界逆因子交换，

$$
\|(V_i-I)\Pi_{1,m}\|
=2\|(I+N_i)^{-1}N_i\Pi_{1,m}\|
\le6\eta_{m-1}.
$$

置 $L_m=6\sqrt m\,\|a\|_2$，则

$$
\|H_m\|\le L_m,\qquad
\|H_m\Pi_{1,m}\|\le L_m\eta_{m-1},
$$

以及对 $k\ge1$，

$$
\boxed{\|H_m^k\Pi_{1,m}\|\le L_m^k\eta_{m-1}.}
\tag{5.4}
$$

尾中心化幂保持物理头不变，所以其作用后的向量仍在 $\Pi_{1,m}H$。§3 已证明所需实际高次域。由于有界 $H_m$ 保持尾自然幂域并交换，可以在准确域上作二项式展开，得到

$$
\begin{aligned}
\|(X-\lambda I)^rx_m\|
\le{}&
C_r\|a_{\ge m}\|_2^r\\
&+\eta_{m-1}
\sum_{k=1}^r\binom rk
L_m^kC_{r-k}\|a_{\ge m}\|_2^{r-k}.
\end{aligned}
\tag{5.5}
$$

对每个固定 $r$，第一项趋零；第二项只是固定次数的 $m^{1/2}$ 多项式乘 $\eta_{m-1}$，也趋零。因此

$$
\boxed{
x_m\in\bigcap_{r\ge1}\operatorname{Dom}X^r,\qquad
\|(X-\lambda I)^rx_m\|\longrightarrow0
\quad\text{对每个固定 }r.
}
\tag{5.6}
$$

同一序列对全部固定整数 $r$ 成立；没有随 $r$ 更换已经选择的尾态。于是也有

$$
\|X^kx_m-\lambda^kx_m\|\longrightarrow0
\qquad(k\text{ 固定}).
\tag{5.7}
$$

这正是不能从一阶近特征关系直接省略的高次步骤。

## 6. Acal 系数在这些向量上趋向实际字符

**引理6.1。** 若单位向量 $x_m$ 满足 $Ax_m\to0$，则对每个 $E\in\mathcal A$，

$$
\boxed{\|(E-\chi(E)I)x_m\|\longrightarrow0.}
\tag{6.1}
$$

证明：取多项式 $p(A)$ 按范数逼近 $E$。字符连续且范数为1，所以

$$
\|(E-\chi(E)I)-(p(A)-p(0)I)\|
\le2\|E-p(A)\|.
$$

而 $p(A)-p(0)I=Aq(A)$，故

$$
\|(p(A)-p(0)I)x_m\|\le\|q(A)\|\|Ax_m\|\to0.
$$

先取 $m\to\infty$，再让范数逼近误差趋零即可。证毕。

这是 R174 的 UHF 边界状态在 $\mathcal A$ 上的更具体强向量形式。一般 UHF 元素或一般 $\{A\}'$ 元素不必满足相同的标量结论。

## 7. 真实多项式的全平面近似点谱

给任意 $\mu\in\mathbb C$，因为 $q_0$ 是非恒定复多项式，可选 $\lambda$ 使

$$
q_0(\lambda)=\mu.
$$

对这个 $\lambda$ 采用 §5 的同一弱零单位序列。所有 $x_m$ 都在自然多项式域中，且

$$
\begin{aligned}
(P(X)-\mu I)x_m
={}&\sum_{k=0}^p E_k(X^k-\lambda^kI)x_m\\
&+\left(\sum_{k=0}^p\lambda^kE_k-\mu I\right)x_m.
\end{aligned}
$$

第一行由 (5.7) 趋零。第二行括号属于 $\mathcal A$，字符恰为0，所以由 (5.2)、(6.1) 趋零。故 (1.4) 成立。

如果 $P(X)-\mu I$ 有有界逆，这些单位向量立即给矛盾。因此

$$
\boxed{\sigma(P(X))=\sigma_{\rm ap}(P(X))=\mathbb C.}
\tag{7.1}
$$

还可得到准确的本质结论：若闭算子 $P(X)-\mu I$ 的核有限维且像闭，则在核的正交补上有正下界。由于 $x_m\rightharpoonup0$，其有限维核投影趋零；(1.4) 与该下界矛盾。因此所有 $\mu$ 都不属于上半 Fredholm 集，更不属于 Fredholm 预解集。

这个论证不要求 $P(X)-\mu I$ 单射。可能的非零核仍需另行处理。由 R176 的 $C$ 自伴性，若某参数处核为零，则其像自动稠密，该参数是连续谱；若核非零，则是点谱。本文没有将第三分支的全部谱点写成连续谱。

## 8. 另外两个谱分支及实际预解式

### 8.1 绝对可和系数

若 $a\in\ell^1$，则

$$
X=a_*I+\sum_ja_jV_j\in\mathcal A,\qquad
\chi(X)=a_*+\sum_ja_j.
$$

所以 $P(X)\in\mathcal A$ 有界，由唯一字符及全空间谱公式，

$$
\boxed{\sigma(P(X))=\{q_0(a_*+\sum_ja_j)\}.}
\tag{8.1}
$$

这里不对这个唯一谱点的核另作无条件判断。一般系数甚至允许 $P(X)=0$：例如在本分支取 $p=1$、$E_1=I$、$E_0=-X\in\mathcal A$。即使采用真正的 Bell 系数，也可能因点态符号恒零而出现零算子，例如 $u=\chi_0$、$q(z)=z^2-1$。所以单点谱不能无条件写成连续谱。

### 8.2 可和相位缺陷且不可绝对求和

R138 给 $\sigma(X)=\varnothing$。置 $R=X^{-1}$。它是全域有界交换子，且拟幂零：对每个 $\lambda$，

$$
I-\lambda R=(X-\lambda I)R
$$

有界可逆，所以 $\sigma(R)\subseteq\{0\}$。

更一般允许 $E_k\in\{A\}'$、$E_p$ 为有界单位。自然幂域为

$$
\operatorname{Dom}X^p=\operatorname{Ran}R^p.
$$

对任意 $\mu$，令 $\widetilde E_0=E_0-\mu I$，其余 $\widetilde E_k=E_k$，定义

$$
U_\mu=I+\sum_{k<p}E_p^{-1}\widetilde E_k R^{p-k}.
$$

$U_\mu-I=RD_\mu$，其中 $D_\mu$ 有界且与拟幂零 $R$ 交换，因此 $RD_\mu$ 拟幂零，$U_\mu$ 可逆。准确域上有

$$
P(X)-\mu I=E_pU_\mu X^p.
$$

故

$$
\boxed{
(P(X)-\mu I)^{-1}=R^pU_\mu^{-1}E_p^{-1}\in\{A\}'.
}
\tag{8.2}
$$

其像确在 $\operatorname{Dom}X^p$。这给整个复平面的有界预解式，完成 (1.3)。

## 9. 单模式点态 Bell 多项式和任意 ℓ² 指数权

取任意

$$
w=b_*+\sum_jb_j\chi_j,\qquad b\in\ell^2.
$$

R176 已构造

$$
X_b=X+H_{a,b},\qquad
H_{a,b}\in\mathcal A,\quad\chi(H_{a,b})=0,
$$

及真实 $\mathcal A$ 系数 Bell 多项式 $P_{q,b}$，使

$$
q(u)e^w=P_{q,b}(X_b)e^w.
$$

最高系数是标量 $q_pI$，字符多项式为 $q$。自然闭实现

$$
T_{q,b}=P_{q,b}(X_b)
$$

的准确域是 $\operatorname{Dom}X^p$，它 $C$ 自伴，并有

$$
[q(u)e^w]_A=\overline{\operatorname{Ran}T_{q,b}}.
\tag{9.1}
$$

把 $X_b=X+H_{a,b}$ 在真正的共同自然域展开。由于 $H_{a,b}$ 与 $X$ 域交换，所得仍是 (1.1) 型的 $\mathcal A$ 系数多项式；因为 $\chi(H_{a,b})=0$，字符多项式仍为 $q$。

所以

$$
\boxed{
\sigma(T_{q,b})=
\begin{cases}
\{q(a_*+\sum_ja_j)\},&a\in\ell^1,\\
\varnothing,&a\notin\ell^1,\ \mathcal D(a,\theta)<\infty
\text{ 对某个 }\theta,\\
\mathbb C,&a\notin\ell^1,\ \mathcal D(a,\theta)=\infty
\text{ 对全部 }\theta.
\end{cases}}
\tag{9.2}
$$

这覆盖任意复 $\ell^2$ 指数权；倾斜只改变有界零字符系数，不改变此谱集合分类。

在绝对可和分支，若 $q(a_*+\sum_ja_j)\ne0$，则 $T_{q,b}$ 是实际单位，像向量循环。若该值为0，所得是唯一临界谱点；即使点态符号非零，其核仍不能仅由本稿排除。慢平方共振的有界临界情形正属于需要保留的这一边界。

对慢平方共振，

$$
T=X^2+B_2-a_{j_0}^2I
$$

仍保留完整 $B_2$。在 full-plane 第一阶分支，本文给 $\sigma(T)=\mathbb C$ 及每个参数的弱零近特征序列；它不证明 $\ker T=0$。在空谱第一阶分支，(8.2) 当然给全部 Bell 预解式及循环性，和已有空谱锚结果一致。

## 10. 证明边界

1. 全平面谱不是只由 $r=1$ 近特征关系推出；§§2–5 对任意有限乘积参考态控制了每个实际中心幂。
2. 真实低头和真实尾精确交换；纯尾只用于相对激发次数估计，全部 carry 由局部加权范数级数支付。
3. 所有近特征向量均为有限柱、属于全部自然幂域，并且弱趋零。
4. 全平面分支的系数限定为 $\mathcal A$。一般 $\{A\}'$ 系数不自动具有 (6.1) 的边界标量作用。
5. 谱三分给谱集合，不将未知核问题改名为已完成的谱问题。
6. 任意未知不变限制的谱未由 (1.3) 自动决定；测试序列未证明位于该限制内。
7. 本文的 $T_{q,b}$ 是作用于循环指数向量的自然闭 Bell 实现，不偷换为一个未核对域的点态乘法算子。

完整 Hilbert 不变子空间问题仍未解决。
