# R65：临界闭商的全平面连续谱、所有参数的除法障碍及精确图核心

日期：2026-11-12（UTC）。子任务：literature。**状态：已证明。**

沿用 R60 的实际算子 $A,L$。这里的逆符号只定义在真实值域上，不表示有界逆。本条证明两个最大闭实现

$$
X=A^{-1}L,\qquad Y=L^{-1}A
$$

均稠密定义、闭、单射、值域稠密，而且

$$
\boxed{\sigma(X)=\sigma_c(X)=\mathbb C,
\qquad\sigma(Y)=\sigma_c(Y)=\mathbb C.}
$$

它们的点谱和剩余谱均为空。相应 R34 模映射的最小闭包也具有同一谱结论；第 8 节进一步用 R23 的强单位多项式证明最小闭包等于最大图。

作为所需的有界除法障碍，还将 R49 推广为：对任意固定 $\lambda\in\mathbb C$ 和整数 $m\ge1$，不存在任何 $B\in B(H)$ 使

$$
(L-\lambda A)B=A^m.
$$

特别地，$\operatorname{Ran}(L-\lambda A)$ 与每个 $\operatorname{Ran}A^m$ 都互不包含，虽然两者均稠密。

依赖：R24 的复对称性；R32 的解析系数；R36 的原方向真实除法障碍；R49 的范数保持辅助单边表示及 $L$ 系数尺度；R60 的 $L$ 单射稠密；R62给 $L-\lambda A$ 与 $A-\lambda L$ 对全部参数单射稠密。全部新的系数估计、闭图关系和谱推导在下文完整给出。

## 1. 最大与最小闭比值的一般框架

设 $F,G\in B(H)$ 交换，二者均单射且值域稠密。定义

$$
\operatorname{Dom}T_{F/G}
=\{u\in H:Fu\in\operatorname{Ran}G\},
\qquad
GT_{F/G}u=Fu. \tag{1.1}
$$

$G$ 单射使右边唯一确定 $T_{F/G}u$。这是此关系的**最大图**：

$$
\operatorname{Graph}T_{F/G}
=\{(u,v)\in H\oplus H:Fu=Gv\}. \tag{1.2}
$$

### 引理 1.1：定义域、闭性、逆及交换

有

$$
\operatorname{Ran}G\subseteq\operatorname{Dom}T_{F/G},
\qquad T_{F/G}Gh=Fh. \tag{1.3}
$$

因此定义域稠密。图 (1.2) 是有界映射 $(u,v)\mapsto Fu-Gv$ 的核，所以闭。$F$ 单射给 $T_{F/G}$ 单射；(1.3) 又说明其值域包含稠密的 $\operatorname{Ran}F$。

并且

$$
(T_{F/G})^{-1}=T_{G/F},
\qquad
\operatorname{Ran}T_{F/G}=\operatorname{Dom}T_{G/F}. \tag{1.4}
$$

这是将 (1.2) 的两个坐标交换后的直接结果。

若有界算子 $S$ 同时与 $F,G$ 交换，则

$$
S\operatorname{Dom}T_{F/G}\subseteq\operatorname{Dom}T_{F/G},
\qquad T_{F/G}Su=ST_{F/G}u. \tag{1.5}
$$

证明是对 $GTu=Fu$ 施加 $S$，再用 $G$ 单射。这里明确保留定义域条件。

### 1.1 最小闭图与 R34 的关系

在稠密空间 $\operatorname{Ran}G$ 上定义

$$
T_0(Gh)=Fh.
$$

其图为 $\{(Gh,Fh):h\in H\}$，包含在 (1.2) 中，故可闭。记

$$
T^{\min}_{F/G}=\overline{T_0}.
$$

则

$$
\operatorname{Graph}T^{\min}_{F/G}
=\overline{\operatorname{Ran}\begin{pmatrix}G\\F\end{pmatrix}},
\qquad
T^{\min}_{F/G}\subseteq T_{F/G}. \tag{1.6}
$$

这给出了两个不同的闭算子定义，不能未经证明取消包含号。

在本课题中，若 $F,G\in\mathcal A$，$1$ 对 $A$ 循环，则 R34 从循环向量 $G1$ 到 $F1$ 的核心

$$
p(A)G1\longmapsto p(A)F1
$$

的图闭包恰为 (1.6)：对每个 $h\in H$，选 $p_n(A)1\to h$，由 $F,G$ 有界同时得到 $Gp_n(A)1\to Gh$ 与 $Fp_n(A)1\to Fh$。反向核心包含关系显然。因此 R34 的闭包是这里的**最小**闭实现，不是定义上直接等于最大图。

### 1.2 复对称性给出的准确对偶关系

若 $F=CF^*C$、$G=CG^*C$，则

$$
\boxed{
T_{F/G}=C(T^{\min}_{F/G})^*C,
\qquad
T^{\min}_{F/G}=C(T_{F/G})^*C.
} \tag{1.7}
$$

**证明。** 对 $T_0$ 使用伴随定义：$v\in\operatorname{Dom}T_0^*$ 且 $T_0^*v=w$ 当且仅当对每个 $h\in H$，

$$
\langle Fh,v\rangle=\langle Gh,w\rangle,
$$

即 $F^*v=G^*w$。令 $u=Cv$、$q=Cw$，这个关系等价于 $Fu=Gq$。故 $CT_0^*C$ 的图正是最大图 (1.2)。又 $T_0^*=(T^{\min}_{F/G})^*$，得到第一个等式。两个算子均稠密定义且闭，取共轭伴随再次得到第二个等式。证毕。

因此最小实现是 $C$-对称的，因为它包含于自己的共轭伴随最大实现。但不能顺带称最大实现也 $C$-对称：对最大实现，该断言结合 (1.7) 正好等价于两种实现相等。一般框架本身不保证相等；本条的两个具体商将在第 8 节单独证明相等。

### 1.3 预解点与真实有界因子的等价

设某个 $\lambda$ 使 $P_\lambda=F-\lambda G$ 单射。则 $T_{F/G}-\lambda$ 单射，且

$$
\boxed{
\lambda\in\rho(T_{F/G})
\iff
\exists B\in B(H),\quad (F-\lambda G)B=G.
} \tag{1.8}
$$

这里采用 $B=(T_{F/G}-\lambda)^{-1}$ 的符号约定；改用 $\lambda-T$ 只改变逆算子的负号。

**证明。** 若 $B$ 为预解逆，左乘 $G$ 得 $(F-\lambda G)B=G$。反之，若这个有界因子存在，则

$$
FB=G(I+\lambda B),
$$

所以 $BH\subseteq\operatorname{Dom}T_{F/G}$，且 $(T_{F/G}-\lambda)B=I$。已知的单射性使 $B$ 同时为定义域上的左逆，故为有界处处定义的预解逆。证毕。

同样，由 (1.3)，

$$
(T_{F/G}-\lambda)Gh=(F-\lambda G)h. \tag{1.9}
$$

因此若 $P_\lambda$ 值域稠密，则最大、最小实现的 $T-\lambda$ 都有稠密值域。

## 2. 原临界系数与辅助单边表示

沿用 R49 的记号

$$
W_n=\|A^n\|=\prod_{s=1}^n a_{v_2(s)},\quad W_0=1,
\qquad d_j=W_{2^j},\qquad \lambda_j=-\log d_j.
$$

这里 $\lambda_j$ 是带下标的实尺度，和不带下标的谱参数 $\lambda\in\mathbb C$ 不同。已有

$$
\lambda_j=100\,16^j-105\,8^j+(150j+25)2^j,
\qquad \lambda_j\ge16\lambda_{j-1},
\qquad \lambda_0=20. \tag{2.1}
$$

原临界对数的范数绝对收敛级数为

$$
L=\sum_{n\ge1}c_nA^n,\qquad c_n>0.
$$

特别地

$$
c_1=\frac25e^{20},\qquad c_2>0.
$$

对于 $n\ge2$，定义

$$
p(n)=\frac{n}{2^{v_2(n)}}\lambda_{v_2(n)}.
$$

R49 给出

$$
0<c_n\le e^{p(n)}, \tag{2.2}
$$

$$
\beta_j:=c_{2^j}d_j,
\qquad \beta_j\sim\delta_j,
\qquad \delta_j=\frac2{(j+2)^2+1}. \tag{2.3}
$$

在同一 UHF 代数 $\mathcal C=C^*(I,A)$ 上，R49 构造了等距含单位 $*$-表示

$$
\pi:\mathcal C\longrightarrow B(\ell^2(\mathbb N_0)),
$$

满足

$$
J:=\pi(A),\qquad Je_k=a_{v_2(k+1)}e_{k+1}.
$$

它保留范数与正算子序。只用这种正序转移，不把一个表示中的核转移到另一个表示。

对每个谱参数置

$$
H_\lambda=L-\lambda A,
\qquad
\Lambda_\lambda=\pi(H_\lambda).
$$

若某个任意有界 $B$ 满足 $H_\lambda B=A^m$，则

$$
A^mA^{*m}\le\|B\|^2H_\lambda H_\lambda^*.
$$

应用 $\pi$ 后为

$$
J^mJ^{*m}\le\|B\|^2\Lambda_\lambda\Lambda_\lambda^*.
$$

由此实际构造有界 $T$：先在 $\operatorname{Ran}\Lambda_\lambda^*$ 上定义

$$
S(\Lambda_\lambda^*u)=J^{*m}u.
$$

正序不等式使其良定义且有界；在该值域闭包上连续延伸，再于正交补置零。取 $T=S^*$，得到

$$
\Lambda_\lambda T=J^m,\qquad \|T\|\le\|B\|. \tag{2.4}
$$

写

$$
Te_0=\sum_{k\ge0}b_kW_ke_k.
$$

则

$$
|b_k|W_k\le\|B\|, \tag{2.5}
$$

并且逐坐标比较给出形式恒等式

$$
\left((c_1-\lambda)z+\sum_{n\ge2}c_nz^n\right)
\left(\sum_{k\ge0}b_kz^k\right)=z^m. \tag{2.6}
$$

每个坐标只涉及有限和；这里没有假设标量级数在非零点收敛。

## 3. 全部谱参数与全部有限幂的除法障碍

**定理 3.1。** 对所有 $\lambda\in\mathbb C$、所有整数 $m\ge1$，不存在 $B\in B(H)$ 满足

$$
\boxed{(L-\lambda A)B=A^m.} \tag{3.1}
$$

证明分清两个首阶情形：

$$
(r,\kappa)=
\begin{cases}
(1,c_1-\lambda),&\lambda\ne c_1,\\
(2,c_2),&\lambda=c_1.
\end{cases} \tag{3.2}
$$

其中 $\kappa\ne0$，而 (2.6) 的第一个形式因子的首阶恰为 $r$。若 $m<r$，形式阶立即矛盾。因此唯一需要另论的最低情形 $\lambda=c_1,m=1$ 已被直接排除：辅助表示中的 $\Lambda_{c_1}$ 不产生第 1 坐标，而 $Je_0$ 在该坐标非零。

以下固定 $\lambda$ 及 $m\ge r$。形式商唯一为

$$
\sum_{k\ge0}b_kz^k
=\frac{z^{m-r}}{\kappa}
\left(1+\sum_{n\ge r+1}\frac{c_n}{\kappa}z^{n-r}\right)^{-1}.
\tag{3.3}
$$

注意 $\kappa$ 可以很小或为复数；下面的界显式允许这种情况，不使用 R49 中仅适用于原 $c_1>1$ 的简化。

### 3.1 适用于首阶 $1$ 或 $2$ 的统一指数预算

对 $h\ge2$、$r\in\{1,2\}$，置

$$
q_h^{(r)}=\frac{\lambda_h}{2^h-r}.
$$

这些数随 $h$ 严格递增。事实上，由 (2.1)，相邻比值至少为

$$
16\frac{2^{h-1}-r}{2^h-r}>1\quad(h\ge3).
$$

并且对所有 $n\ge r+1$、$v_2(n)\le h$，有

$$
\boxed{p(n)\le q_h^{(r)}(n-r).} \tag{3.4}
$$

若 $j=v_2(n)\ge2$，写 $n=u2^j$，则

$$
\frac{p(n)}{n-r}
=\frac{u\lambda_j}{u2^j-r}
\le\frac{\lambda_j}{2^j-r}\le q_h^{(r)}.
$$

若 $j=0$，$n$ 是至少为 $3$ 的奇数，左边不超过 $3\lambda_0/(3-r)\le60$。若 $j=1,r=1$，左边不超过 $\lambda_1$；若 $j=1,r=2$，则 $n\ge6$，左边不超过 $3\lambda_1/4$。这些有限上界均小于 $q_2^{(r)}$，因为 $\lambda_2\ge16\lambda_1$、$\lambda_1=1110$、$\lambda_0=20$。由此得到 (3.4)。

令

$$
k_0=\lceil m/r\rceil,
\qquad s=r(k_0+1)-m\in\{r,r+1,\ldots,2r-1\}.
$$

对 $J\ge3$，取

$$
N_J=\sum_{j=0}^{k_0-1}2^{J+j},\qquad
S_J=N_J-rk_0,\qquad
P_J=\sum_{j=0}^{k_0-1}\lambda_{J+j}.
$$

在 (3.3) 中取 $b_{N_J-s}$，形式几何展开给

$$
b_{N_J-s}
=\sum_{k=1}^{S_J}(-1)^k\kappa^{-k-1}
\sum_{\substack{n_1,\ldots,n_k\ge r+1\\
\sum_i(n_i-r)=S_J}}
\prod_{i=1}^kc_{n_i}. \tag{3.5}
$$

主项来自 $k=k_0$ 且多重集为
$\{2^J,\ldots,2^{J+k_0-1}\}$ 的 $k_0!$ 个排列：

$$
M_J=(-1)^{k_0}k_0!\,\kappa^{-k_0-1}
\prod_{j=0}^{k_0-1}c_{2^{J+j}}. \tag{3.6}
$$

**引理 3.2。** (3.5) 中每个非主项组合都满足

$$
\sum_i p(n_i)\le P_J-\lambda_J/2. \tag{3.7}
$$

**证明。** 从最高预定层 $J+k_0-1$ 向下检查。若更高层的预定 dyadic 项都已经各取一次，在层 $q$ 剩余的成本预算为

$$
S(q)=\sum_{j=J}^{q}(2^j-r)
=2^{q+1}-2^J-r(q-J+1)<2^{q+1}.
$$

剩余项不可能有 $v_2(n_i)>q$，因为这时
$n_i-r\ge2^{q+1}-r>S(q)$。若 $v_2(n_i)=q$，则只能 $n_i=2^q$；更大的奇数倍成本已经超预算。而这样的项至多一个，因为

$$
2(2^q-r)-S(q)=2^J+r(q-J-1)>0.
$$

非主项必有第一个缺失的预定层 $q$；否则全部成本恰由预定项耗尽。缺失后所有剩余项的二进阶均不超过 $q-1$。由 (3.4)，其 $p$ 值和小于

$$
q_{q-1}^{(r)}2^{q+1}
=\lambda_{q-1}\frac{2^{q+1}}{2^{q-1}-r}
\le8\lambda_{q-1}\le\lambda_q/2.
$$

这里 $q\ge J\ge3$、$r\le2$ 保证中间分母估计。主项在这些剩余层的 $p$ 值至少为 $\lambda_q$，因此损失至少 $\lambda_q/2\ge\lambda_J/2$。加回已相同的高位项即得 (3.7)。证毕。

### 3.2 复数首项和小首项不会破坏主项优势

令 $D_\kappa=\max(1,|\kappa|^{-1})$。成本 $S_J$ 的有序正整数组合数为 $2^{S_J-1}$，且每个组合长度 $k\le S_J$。由 (2.2)、(3.7)，余项 $E_J=b_{N_J-s}-M_J$ 满足

$$
|E_J|\le D_\kappa(2D_\kappa)^{S_J}
\exp(P_J-\lambda_J/2). \tag{3.8}
$$

主项的模为

$$
|M_J|=k_0!|\kappa|^{-k_0-1}e^{P_J}
\prod_{j=0}^{k_0-1}\beta_{J+j}.
$$

$\lambda$ 与 $m$ 固定，故 $D_\kappa,k_0$ 固定；$S_J=O_m(2^J)$，而 $\lambda_J\ge20\,16^J$，且 (2.3) 给 $\beta_{J+j}\asymp J^{-2}$。因此 (3.8) 严格给出

$$
E_J=o(M_J). \tag{3.9}
$$

这是每个固定参数的证明，不声称误差对 $\lambda\to c_1$ 一致；首阶抵消已经由 $r=2$ 分支单独处理。

### 3.3 带真实权的形式商系数发散

$N_J$ 的二进制展开只在 $J,\ldots,J+k_0-1$ 位取 $1$，故 R13 的无进位乘法给

$$
W_{N_J}=e^{-P_J}.
$$

当 $J$ 足够大使 $s<2^J$ 时，$v_2(N_J)=J$，并且对 $1\le t<s$，$v_2(N_J-t)=v_2(t)$。因此

$$
\frac{W_{N_J}}{W_{N_J-s}}=a_JW_{s-1}.
$$

把它代入 (3.6) 与 (3.9)，得到

$$
\boxed{
b_{N_J-s}W_{N_J-s}
=\frac{(-1)^{k_0}k_0!}
{\kappa^{k_0+1}a_JW_{s-1}}
\prod_{j=0}^{k_0-1}\delta_{J+j}\,(1+o(1)).
} \tag{3.10}
$$

其模趋于无穷：$W_{s-1}$ 是固定正数，有限个 $\delta$ 的乘积只按 $J^{-2k_0}$ 衰减，而 $a_J$ 超快趋零。这与 (2.5) 矛盾，证明定理 3.1。

对于预解问题真正需要的 $m=1$、$\lambda\ne c_1$，此式简化为

$$
b_{2^J-1}W_{2^J-1}
\sim-\frac{\delta_J}{(c_1-\lambda)^2a_J}.
$$

## 4. 全部 pencil 值域与全部幂值域互不包含

**推论 4.1。** 对每个 $\lambda\in\mathbb C$、$m\ge1$，

$$
\operatorname{Ran}A^m\not\subseteq\operatorname{Ran}(L-\lambda A),
\qquad
\operatorname{Ran}(L-\lambda A)\not\subseteq\operatorname{Ran}A^m.
\tag{4.1}
$$

**证明。** R62 给 $H_\lambda=L-\lambda A$ 单射。若第一个包含成立，则最大解 $B=H_\lambda^{-1}A^m$ 处处定义且图闭，因而由闭图定理有界，违背定理 3.1。

若第二个包含成立，则特别有 $\operatorname{Ran}H_\lambda\subseteq\operatorname{Ran}A$。由于 $L=H_\lambda+\lambda A$，立即得到 $\operatorname{Ran}L\subseteq\operatorname{Ran}A$，与 R36 矛盾。证毕。

这些都是实际值域的不包含关系。R62 与 $A$ 的已知性质同时给

$$
\overline{\operatorname{Ran}H_\lambda}
=\overline{\operatorname{Ran}A^m}=H.
$$

## 5. 最大比值 $X=A^{-1}L$ 的全部谱

按 (1.1) 定义

$$
\operatorname{Dom}X=\{u:Lu\in\operatorname{Ran}A\},
\qquad AXu=Lu. \tag{5.1}
$$

由引理 1.1，$X$ 闭、稠密定义、单射、值域稠密，并满足

$$
XAh=Lh.
$$

R36 的 $\operatorname{Ran}L\not\subseteq\operatorname{Ran}A$ 保证 $\operatorname{Dom}X\ne H$。所以 $X$ 无界：若闭且稠密定义的算子在其定义域上有统一有界范数，则其连续延伸与闭性会迫使定义域等于 $H$。

对任何 $\lambda\in\mathbb C$，R62 使 $L-\lambda A$ 单射。因此 $X-\lambda$ 无核。而

$$
(X-\lambda)Ah=(L-\lambda A)h
$$

又使其值域稠密。若 $\lambda\in\rho(X)$，则由 (1.8) 存在有界 $B$ 满足

$$
(L-\lambda A)B=A,
$$

这已经被定理 3.1 的 $m=1$ 情形排除。

最后，$X-\lambda$ 不可能满射：它闭且单射，若满射，其逆是处处定义的闭算子，从闭图定理自动有界，于是 $\lambda$ 是预解点，仍矛盾。

因此每个参数都是连续谱点：

$$
\boxed{
\rho(X)=\varnothing,\quad
\sigma_p(X)=\sigma_r(X)=\varnothing,\quad
\sigma_c(X)=\sigma(X)=\mathbb C.
} \tag{5.2}
$$

## 6. 反向最大比值 $Y=L^{-1}A$

定义

$$
\operatorname{Dom}Y=\{u:Au\in\operatorname{Ran}L\},
\qquad LYu=Au.
$$

由 (1.4)，$Y=X^{-1}$，其定义域等于 $\operatorname{Ran}X$。它闭、稠密定义、单射、值域稠密。R49 或推论 4.1 的 $\lambda=0,m=1$ 给定义域不是全 $H$，所以它也无界。

对任何 $\lambda$，R62 使 $A-\lambda L$ 单射稠密，因此

$$
\ker(Y-\lambda)=0,
\qquad
\overline{\operatorname{Ran}(Y-\lambda)}=H,
$$

后一个结论可直接由 $(Y-\lambda)Lh=(A-\lambda L)h$ 得到。

若 $\lambda\in\rho(Y)$，(1.8) 给有界 $B$ 满足

$$
(A-\lambda L)B=L. \tag{6.1}
$$

当 $\lambda=0$ 时，这是 $AB=L$，被 R36 排除。当 $\lambda\ne0$ 时，令 $\mu=1/\lambda$，由 (6.1) 得

$$
(L-\mu A)B=-L/\lambda.
$$

因此有界算子 $B'=-\lambda^2B-\lambda I$ 满足

$$
\begin{aligned}
(L-\mu A)B'
&=\lambda L-\lambda(L-\mu A)\\
&=A,
\end{aligned}
$$

与定理 3.1 矛盾。和第 5 节同样，闭图定理排除满射而逆无界的例外。所以

$$
\boxed{
\rho(Y)=\varnothing,\quad
\sigma_p(Y)=\sigma_r(Y)=\varnothing,\quad
\sigma_c(Y)=\sigma(Y)=\mathbb C.
} \tag{6.2}
$$

## 7. 不预设图相等时的最小实现谱

令

$$
X_{\min}=T^{\min}_{L/A},\qquad
Y_{\min}=T^{\min}_{A/L}.
$$

根据 §1.1，它们分别是 R34 从 $A1$ 到 $L1$、从 $L1$ 到 $A1$ 的闭模映射。两者包含于相应最大实现，因此无特征值；又其核心已经包含

$$
(X_{\min}-\lambda)Ah=(L-\lambda A)h,
\qquad
(Y_{\min}-\lambda)Lh=(A-\lambda L)h,
$$

故对所有参数都有稠密值域。

它们也不可能有预解点。一般地，若闭算子 $S\subseteq T$、$T-\lambda$ 单射，而 $S-\lambda$ 满射，则必有 $S=T$：给定 $u\in\operatorname{Dom}T$，取 $v\in\operatorname{Dom}S$ 使 $(S-\lambda)v=(T-\lambda)u$；单射性给 $u=v$。所以最小实现的任何预解点都会也是最大实现的预解点，与 (5.2)、(6.2) 矛盾。

因此

$$
\sigma_c(X_{\min})=\sigma_c(Y_{\min})=\mathbb C,
$$

其点谱、剩余谱及预解集都为空。它们也都无界。

另一方面，(1.7) 只给出

$$
X=CX_{\min}^*C,\qquad X_{\min}=CX^*C,
$$

$$
Y=CY_{\min}^*C,\qquad Y_{\min}=CY^*C.
$$

截至本节尚未使用 $X=X_{\min}$ 或 $Y=Y_{\min}$。两个闭图相等精确等价于

$$
\overline{\{(Ah,Lh):h\in H\}}
=\{(u,v):Lu=Av\}. \tag{7.1}
$$

交换两个坐标显示两种比值的相等性是同一个问题。全平面连续谱本身没有给出 (7.1)。

## 8. R23 的强单位多项式给出精确图核心

**定理 8.1。** 式 (7.1) 成立。因此
$$
X=X_{\min},\qquad Y=Y_{\min},\qquad
X=CX^*C,\qquad Y=CY^*C.
$$

**证明。** R23 已构造无常数项的收缩多项式 $p_n(A)$，使
$$
p_n(A)\longrightarrow I\quad\text{强算子拓扑}.
$$
把有限多项式分解为 $p_n(z)=z r_n(z)$。若 $(u,v)$ 在最大图中，即 $Lu=Av$，令
$$
h_n=r_n(A)u.
$$
多项式 $r_n(A)$ 与 $A,L$ 交换，故
$$
Ah_n=p_n(A)u\longrightarrow u,
$$
$$
Lh_n=r_n(A)Lu=r_n(A)Av=p_n(A)v\longrightarrow v.
$$
这给出最大图内每个向量的实际核心逼近，证明最大图包含于最小图闭包。反向包含在 (1.6) 已证。交换两个图坐标即给反向比值的相等性；再用 (1.7) 得两者的 $C$-自伴等式。证毕。

整个证明只要求 $p_n(A)$ 强趋 $I$；$r_n(A)$ 的范数可以发散。它没有建立被 R36/R49 否定的有界分母，也没有把某个谱结论误作图核心条件。

更一般地，若有界 $F$ 与 $A$ 交换，则同一构造说明最大闭图 $Fu=Av$ 的 $A^{-1}F$ 以 $\operatorname{Ran}A$ 为图核心。对分母 $A^m$，使用 $p_n(A)^m=A^m r_n(A)^m$；收缩界与强收敛保证该幂仍强趋 $I$，结论也成立。

## 9. 研究意义与剩余缺口

本条既判定全部闭商谱，也完成其定义域图核心。最容易漏掉的 $\lambda=c_1$ 已单独处理：$m=1$ 用形式首阶，所有 $m$ 用完整 $n-r$ 预算。

这些谱属于闭无界算子，没有从它们导出原有界 $A$ 的真不变子空间。一般解析芽比值的图核心和有界可除性继续研究；任意有限 R16 乘积和及任意非零 $L^2$ 向量的循环性仍未由本条得到。
