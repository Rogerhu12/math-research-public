# R73：强交换子的边界商与左右代数独立

日期：2026-11-12（UTC）。经主会话逐段核验。**状态：已证明。**

本条研究 R37 的实际有界强乘积交换子 $Y$。它不把 R32 的系数泛函直接延伸到完整交换子；先从逃逸柱向量的真实压缩构造一个完全正极限，再利用有限前缀在辅助单边表示中的**强*零极限**及两侧正序界，证明该极限确实升级为一个 $*$-商映射。

记

$$
\mathcal C=C^*(I,A),\qquad
\mathcal D=C^*(\mathcal C,Y).
$$

本条构造满的收缩含幺 $*$-同态

$$
\boxed{\Pi:\mathcal D\longrightarrow\mathcal C,\qquad
\Pi|_{\mathcal C}=\operatorname{id},\qquad\Pi(Y)=0.}
$$

因此对任意有限 $d$：

$$
\boxed{
\sum_{k=0}^{d}H_kY^k=0,\ H_k\in\mathcal C
\implies H_0=\cdots=H_d=0,
}
$$

右系数关系 $\sum_{k=0}^{d}Y^kH_k=0$ 也有同样结论。特别，$Y$ 在整个交换解析代数 $\mathcal A$ 上代数超越，而不只是 $Y\notin\mathcal C$。

依赖：R9/R12 的实际局部矩阵与进位误差；R32 的解析系数；R37 的强乘积及单射稠密性；R49 的忠实单边表示。本条所有新增边界映射、强*零极限、乘法性及取消方向均完整证明。

## 1. R37 的参数及必须保留的统一常数

取 R37 参数

$$
0\le s_j\le t_j,\qquad
\sum_jt_j^2<\infty,\qquad
\sum_j(t_j-s_j)=\infty.
$$

记 $c_u=(1+u^2)^{-1/2}$，以及

$$
h_j(0)=c_{s_j}(1+s_j),\quad h_j(1)=c_{s_j}(1-s_j),
$$

$$
g_j(0)=c_{t_j}(1+t_j),\quad g_j(1)=c_{t_j}(1-t_j).
$$

令

$$
W_j=(h_j(0)I+h_j(1)N_j)
(g_j(0)I+g_j(1)N_j)^{-1},
\qquad Y_N=\prod_{j<N}W_j.
$$

R37 给强极限 $Y_N\to Y$，其中 $Y\ne0$、单射、值域稠密、拟幂零，且与 $A$ 交换。

置

$$
m_j=\sqrt{\frac{1+t_j^2}{1+s_j^2}}\ge1,
\qquad C_{\mathrm{tot}}=\prod_{j\ge0}m_j<\infty.
$$

R37 的增生 Cayley 估计给

$$
\|W_j\|\le m_j,\qquad
\|Y_N\|\le C_{\mathrm{tot}}. \tag{1.1}
$$

有限前缀可逆，且

$$
Y=Y_NZ_N=Z_NY_N,\qquad
\|Z_N\|\le C_N:=\prod_{j\ge N}m_j. \tag{1.2}
$$

这里特别有

$$
1\le C_N\le C_{\mathrm{tot}},\qquad C_N\longrightarrow1. \tag{1.3}
$$

后面所有强极限中的 $C_N^2$ 都使用统一上界 $C_{\mathrm{tot}}^2$；不会仅凭裸强收敛而忽略可变常数。

另外

$$
\alpha_j=\frac{h_j(0)}{g_j(0)}>0,\qquad
q_N=\prod_{j<N}\alpha_j\longrightarrow0. \tag{1.4}
$$

每个 $W_j/\alpha_j$ 的常数系数为 $1$，首个可能非零的非常数项阶数至少为 $2^j$。因此对每个固定 $r$，$Y_N/q_N$ 的前 $r$ 阶形式系数在 $2^N>r$ 后固定。

## 2. 逃逸柱压缩给出的真实极限映射

令 $N=2^d$，在 Haar 空间中取标准柱向量

$$
e_r^{(N)}=\sqrt N\,1_{\{y\equiv r\pmod N\}},
\qquad0\le r<N.
$$

定义收缩部分等距 $V_d:\ell^2(\mathbb N_0)\to H$：

$$
V_de_r=
\begin{cases}
e_r^{(2^d)},&r<2^d,\\
0,&r\ge2^d.
\end{cases}
$$

则 $V_d^*V_d=P_{2^d}\to I$ 强收敛。

R49 已从局部矩阵表示构造等距含幺 $*$-表示

$$
\pi:\mathcal C\longrightarrow B(\ell^2(\mathbb N_0)),
\qquad
J:=\pi(A),\quad
Je_r=a_{v_2(r+1)}e_{r+1}. \tag{2.1}
$$

由于 $\pi$ 等距，它忠实，且 $\pi(\mathcal C)$ 是范数闭的 $C^*$ 子代数。最后才能合法地用 $\pi^{-1}$ 把边界像识别回具体 $\mathcal C$。

### 2.1 双侧近似交织

对固定 $r$ 及充分大的 $d$，

$$
AV_de_r=V_dJe_r.
$$

当 $r\ge1$ 时还有 $A^*V_de_r=V_dJ^*e_r$。当 $r=0$ 时，$J^*e_0=0$，而

$$
\|A^*e_0^{(2^d)}\|\le a_d\longrightarrow0,
$$

因为对应回绕边的权至多 $a_d$。由有限支撑向量稠密性及统一范数界，

$$
\|XV_dx-V_d\pi(X)x\|\longrightarrow0
\quad(X=A,A^*,\ x\in\ell^2).
$$

对有限 $*$-多项式用乘法伸缩及统一范数界，再用 $\mathcal C$ 的范数稠密性，得到

$$
\boxed{
\|XV_dx-V_d\pi(X)x\|\longrightarrow0
\quad(X\in\mathcal C,\ x\in\ell^2).
} \tag{2.2}
$$

特别地

$$
V_d^*XV_d\longrightarrow\pi(X)\quad\text{强收敛}
\quad(X\in\mathcal C). \tag{2.3}
$$

### 2.2 在 $\mathcal D$ 上取完全正压缩极限

每个

$$
\Phi_d(S)=V_d^*SV_d,\qquad S\in\mathcal D,
$$

都是完全正收缩。$\mathcal D$ 由有限多个生成元 $A,Y$ 及其伴随生成，因而可分。对这些生成元的可数个代数词及可数个矩阵元同时作对角子列，选出 $d_\nu\to\infty$，使全部相应压缩矩阵元收敛。

有限复线性组合的极限随之存在；由 $\|\Phi_d(S)\|\le\|S\|$，这些极限定义有界算子，并唯一按范数连续延伸到整个 $\mathcal D$。记所得映射为

$$
\Phi:\mathcal D\longrightarrow B(\ell^2).
$$

对所有 $S\in\mathcal D$，沿该子列有 $\Phi_{d_\nu}(S)\to\Phi(S)$ 弱算子收敛。正矩阵的弱极限仍正，所以 $\Phi$ 完全正；又 $\Phi_d(I)=P_{2^d}\to I$，故它含幺且收缩。

由 (2.3)，

$$
\Phi(X)=\pi(X)\qquad(X\in\mathcal C). \tag{2.4}
$$

### 2.3 此时只知道 $\mathcal C$ 双模性

由 (2.2)，对 $X\in\mathcal C$、$S\in\mathcal D$ 的矩阵元可把 $X$ 或 $X^*$ 从 $V_d$ 一侧移到 $\pi(X)$ 一侧，误差趋零。取极限得到

$$
\boxed{
\Phi(XS)=\pi(X)\Phi(S),\qquad
\Phi(SX)=\Phi(S)\pi(X).
} \tag{2.5}
$$

这也可从完全正映射的可乘域证明，但这里由真实近似交织直接得到。到此**尚未**证明 $\Phi$ 在整个 $\mathcal D$ 上乘法相容，不能把 (2.5) 中的 $X$ 换成任意 $S\in\mathcal D$。

## 3. 有限强乘积在辅助表示中强*趋零

下面证明比固定系数趋零更强的事实：

$$
\boxed{\pi(Y_N)\longrightarrow0\quad\text{于强*拓扑}.} \tag{3.1}
$$

### 3.1 伴随方向：稳定的有限行

若 $\pi(Y_N)=\sum b_r^{(N)}J^r$ 仅按形式系数记号理解，则

$$
\langle\pi(Y_N)e_j,e_i\rangle
=
\begin{cases}
b_{i-j}^{(N)}W_i/W_j,&i\ge j,\\
0,&i<j.
\end{cases}
$$

对固定 $i$，(1.4) 后的系数稳定性给 $b_r^{(N)}=q_Nb_r$（$0\le r\le i$），其中 $b_r$ 与充分大的 $N$ 无关。因此 $\pi(Y_N)^*e_i$ 是一个固定有限支撑向量乘 $\overline{q_N}$，趋于零。

由 $\|\pi(Y_N)\|=\|Y_N\|\le C_{\mathrm{tot}}$，有限支撑向量稠密性给

$$
\pi(Y_N)^*\longrightarrow0\quad\text{强收敛}. \tag{3.2}
$$

### 3.2 正向：实际尾与纯局部尾的统一范数比较

对充分大的 $j$，有 $0\le s_j\le t_j\le1/2$。写

$$
\rho_u=\frac{1-u}{1+u},
\qquad
\kappa_j=\rho_{s_j}-\rho_{t_j}
=\frac{2(t_j-s_j)}{(1+s_j)(1+t_j)}.
$$

于是 $0\le\kappa_j\le2t_j$，故 $\sum_j\kappa_j^2<\infty$，并且

$$
W_j(T)=\alpha_j(I+\rho_{s_j}T)(I+\rho_{t_j}T)^{-1}
=\alpha_j\bigl[I+\kappa_jT(I+\rho_{t_j}T)^{-1}\bigr].
$$

对实际 $T=N_j$ 及局部 $T=E_j$，预解式范数均一致有界：

$$
\|(I+\rho_{t_j}N_j)^{-1}\|
\le\frac2{1-\eta_0},
\qquad
\|(I+\rho_{t_j}E_j)^{-1}\|\le2.
$$

利用

$$
T(I+rT)^{-1}-U(I+rU)^{-1}
=(I+rT)^{-1}(T-U)(I+rU)^{-1},
$$

以及 $\|N_j-E_j\|=\eta_j$、最终 $\alpha_j\le1$，存在固定常数 $K$，使

$$
\|W_j(N_j)-W_j(E_j)\|\le Kt_j\eta_j\le K\eta_j. \tag{3.3}
$$

这里 $\alpha_j\le1$ 是因为 $u\mapsto(1+u)/\sqrt{1+u^2}$ 在 $[0,1]$ 上递增，而充分大时 $0\le s_j\le t_j\le1/2$。

纯局部因子恰为

$$
\widetilde W_j:=W_j(E_j)=\alpha_j(I+\kappa_jE_j). \tag{3.4}
$$

R37 的增生 Cayley 估计只用局部算子是收缩，因此也适用于 $E_j$，给

$$
\|\widetilde W_j\|\le m_j.
$$

所以原尾、纯尾及望远镜式中出现的混合前后缀都被同一个有限总乘积 $C_{\mathrm{tot}}$ 控制。由 (3.3) 对有限有序乘积伸缩，

$$
\left\|\prod_{j=k}^{N-1}W_j
-\prod_{j=k}^{N-1}\widetilde W_j\right\|
\le K C_{\mathrm{tot}}^2\sum_{j\ge k}\eta_j,
\qquad N\ge k. \tag{3.5}
$$

不要求混合的原与纯因子彼此交换；通常的有序乘积望远镜恒等式已经足够。右边与 $N$ 无关并随 $k\to\infty$ 趋零。

在单边表示中，各 $\pi(E_j)$ 是计算基二进位提升。对 $e_0$，不同选位集合给不同的整数基向量，因此

$$
\left\|\pi\left(\prod_{j=k}^{N-1}\widetilde W_j\right)e_0\right\|
=\frac{q_N}{q_k}
\prod_{j=k}^{N-1}\sqrt{1+\kappa_j^2}
\longrightarrow0
\quad(N\to\infty,\ k\text{ 固定}). \tag{3.6}
$$

这里 $q_N/q_k\to0$，第二个乘积因 $\sum\kappa_j^2<\infty$ 而有界。

将 $Y_N=Y_k\prod_{j=k}^{N-1}W_j$ 与 (3.5)—(3.6) 结合，先令 $N\to\infty$，得到

$$
\limsup_{N\to\infty}\|\pi(Y_N)e_0\|
\le K C_{\mathrm{tot}}^3\sum_{j\ge k}\eta_j.
$$

再令 $k\to\infty$，得 $\pi(Y_N)e_0\to0$。每个 $\pi(Y_N)$ 与 $J$ 交换，而 $e_0$ 对 $J$ 循环，因为 $J^re_0=W_re_r$。统一范数界于是给

$$
\pi(Y_N)\longrightarrow0\quad\text{强收敛}. \tag{3.7}
$$

(3.2) 与 (3.7) 证明 (3.1)。

注意辅助表示中的极限为零，原 Haar 表示中的强极限为非零 $Y$。这并不矛盾：$\pi$ 只有在 $\mathcal C$ 范数拓扑下连续，本节没有从原强极限直接传递 $\pi$。

## 4. 两侧 Schwarz 缺陷都为零，才获得真正商同态

由 (1.2) 的两个相等分解，

$$
YY^*\le C_N^2Y_NY_N^*,
\qquad
Y^*Y\le C_N^2Y_N^*Y_N. \tag{4.1}
$$

应用正映射 $\Phi$，右侧在 $\mathcal C$ 中，故

$$
\Phi(YY^*)\le C_N^2\pi(Y_N)\pi(Y_N)^*,
$$

$$
\Phi(Y^*Y)\le C_N^2\pi(Y_N)^*\pi(Y_N).
$$

对每个固定 $x\in\ell^2$，右边二次型分别被
$C_{\mathrm{tot}}^2\|\pi(Y_N)^*x\|^2$、
$C_{\mathrm{tot}}^2\|\pi(Y_N)x\|^2$ 控制，由 (3.1) 都趋零。因此

$$
\boxed{\Phi(YY^*)=\Phi(Y^*Y)=0.} \tag{4.2}
$$

### 4.1 完全正性给出的四种消失

对于任意 $S\in\mathcal D$，正的 $2\times2$ 算子矩阵

$$
\begin{pmatrix}
YY^*&YS\\S^*Y^*&S^*S
\end{pmatrix}
=
\begin{pmatrix}Y\\S^*\end{pmatrix}
\begin{pmatrix}Y^*&S\end{pmatrix}
$$

经 $\Phi$ 后仍正。左上角由 (4.2) 为零，正块矩阵的对应非对角块必为零（对向量 $(tu,v)$ 的二次型任取复标量 $t$ 即可验证）。所以 $\Phi(YS)=0$，取伴随又给 $\Phi(SY^*)=0$。

将 $Y$ 换成 $Y^*$，利用 (4.2) 的另一式，也得

$$
\boxed{
\Phi(YS)=\Phi(Y^*S)=\Phi(SY)=\Phi(SY^*)=0
\quad(S\in\mathcal D).
} \tag{4.3}
$$

这一步依赖两侧正序极限，不能仅从 $\Phi(Y^k)=0$ 推出。

### 4.2 从代数词到整个 $\mathcal D$

每个由 $\mathcal C,Y,Y^*$ 组成的代数词，如果含有 $Y$ 或 $Y^*$，先用 (2.5) 拉出第一个此类字母之前的 $\mathcal C$ 因子，再用 (4.3)，其 $\Phi$ 像为零。完全不含 $Y,Y^*$ 的词属于 $\mathcal C$，由 (2.4) 映为 $\pi$ 的值。

所以在这个范数稠密的 $*$-代数上，$\Phi$ 正好是把 $Y,Y^*$ 置零、保留 $\mathcal C$ 的代数同态。乘积展开说明它在该子代数上保持乘法与伴随。由于 $\Phi$ 收缩，范数极限把这些恒等式推广到整个 $\mathcal D$。

同时 $\Phi(\mathcal D)\subseteq\pi(\mathcal C)$，因为代数词的像在 $\pi(\mathcal C)$ 中，而该像范数闭；反向包含由 (2.4) 得到。于是

$$
\Pi=\pi^{-1}\circ\Phi:\mathcal D\longrightarrow\mathcal C
$$

是满的含幺收缩 $*$-同态，满足

$$
\Pi|_{\mathcal C}=\operatorname{id},\qquad\Pi(Y)=0.
$$

其值已由范数稠密的生成词唯一决定，因此不依赖第 2 节选择的对角子列。

## 5. 左右系数关系中的正确取消方向

**定理 5.1。** 若

$$
\sum_{k=0}^{d}H_kY^k=0,\qquad H_k\in\mathcal C,
$$

则全部 $H_k=0$。

**证明。** 应用 $\Pi$，得到 $H_0=0$。剩余关系可写成

$$
\left(\sum_{k=1}^{d}H_kY^{k-1}\right)Y=0.
$$

$Y$ 的值域稠密，括号中的算子有界，所以它必须为零。再次应用 $\Pi$ 得 $H_1=0$。重复有限次，得到全部系数为零。这里使用的是**稠密值域来右取消 $Y$**；不要求 $H_k$ 与 $Y$ 交换。证毕。

对右系数关系

$$
\sum_{k=0}^{d}Y^kH_k=0,
$$

应用 $\Pi$ 得 $H_0=0$，然后写成

$$
Y\left(\sum_{k=1}^{d}Y^{k-1}H_k\right)=0.
$$

这次由 **$Y$ 单射来左取消**，再逐阶迭代，得到同样结论。

特别地，当系数限制为 $\mathcal A$ 时，它们与 $Y$ 交换，所以这是通常交换代数意义下的代数超越：不存在任何非零 $\mathcal A$ 系数多项式关系。

### 5.1 收敛算子值解析系数级数也没有关系

若 $H_k\in\mathcal C$ 满足某个 $M,\rho>0$ 的界
$\|H_k\|\le M\rho^{-k}$，则因 $Y$ 拟幂零，左右有序级数
$\sum H_kY^k$、$\sum Y^kH_k$ 都绝对范数收敛。任一系列若为零，其所有系数也必为零。

证明仍为逐阶取消：应用 $\Pi$ 先得 $H_0=0$；移位级数
$\sum_{k\ge0}H_{k+1}Y^k$ 仍绝对收敛，可合法右乘 $Y$，再用稠密值域取消。右有序系列用单射性左取消。这没有把未收敛形式级数赋予算子值。

## 6. 实际非解析交换子的范数代数结构

令

$$
\mathcal I=\ker\Pi.
$$

这是 $\mathcal D$ 的非零闭双侧 $C^*$ 理想，包含 $Y$；它是真理想，因为 $\Pi(I)=I$。并且

$$
\mathcal I\cap\mathcal C=\{0\},
\qquad
0\longrightarrow\mathcal I\longrightarrow\mathcal D
\xrightarrow{\Pi}\mathcal C\longrightarrow0
$$

是由 $\mathcal C$ 的原嵌入分裂的短正合列。这里的分裂不宣称 $\mathcal D$ 是两个 $C^*$ 代数的直积。

这个真范数理想却在强拓扑下逼近整个 $\mathcal D$。因为 $Y$ 单射，$Y^*Y$ 的核为零；连续函数
$f_n(t)=t/(t+1/n)$ 满足 $f_n(0)=0$，故 $f_n(Y^*Y)\in\mathcal I$，且由有界自伴算子的谱演算，

$$
f_n(Y^*Y)\longrightarrow I\quad\text{强收敛}.
$$

对每个 $S\in\mathcal D$，$f_n(Y^*Y)S\in\mathcal I$ 强趋 $S$。这再次显示不能把 $\Pi$ 的范数连续性升级成强连续性。

再看真正的交换子范数代数

$$
\mathcal B=\overline{\mathcal A[Y]}^{\|\cdot\|}
\subseteq\{A\}'.
$$

$\Pi(\mathcal B)=\mathcal A$：对有限有序多项式取常数项，随后按范数取极限。令 $\mathcal K=\mathcal I\cap\mathcal B$，则每个 $S\in\mathcal B$ 都有唯一分解

$$
\boxed{S=X+K,\qquad X\in\mathcal A,\ K\in\mathcal K,}
$$

其中 $X=\Pi(S)$，且 $\|\Pi(S)\|\le\|S\|$。$\mathcal K$ 是 $\mathcal B$ 中包含 $Y$ 的非零闭理想。

因此原解析范数代数在这个明确更大的有界交换子代数中，成为一个有收缩代数回缩的子代数；新的强乘积极限方向由独立的核理想承载。这是对实际非解析交换子的一项结构结论，不只是在某个芽分式类中给谱分类。

### 6.1 直接强交织与完整序列的压缩

前述边界构造还可给不选子列的直接结论。由 $Y=Z_NY_N$，对固定 $x$ 有
$$
\|YV_dx\|\le C_N\|Y_NV_dx\|.
$$
先令 $d\to\infty$，用 (2.2) 和 $V_d^*V_d\to I$，再令 $N\to\infty$，用 $C_N\le C_{\rm tot}$ 与 $\pi(Y_N)\to0$ 强收敛，得到 $YV_dx\to0$。另一分解 $Y=Y_NZ_N$ 取伴随后，以完全相同的估计得到 $Y^*V_dx\to0$。

结合 (2.2)，对生成词逐次伸缩再作范数逼近，得到对所有 $S\in\mathcal D$ 的完整序列结论
$$
\boxed{\|SV_dx-V_d\pi(\Pi(S))x\|\longrightarrow0.}
$$
相同结论对 $S^*$ 成立。特别地，全部压缩 $V_d^*SV_d$ 强*趋于 $\pi(\Pi(S))$。这也直接说明前面 CP 子列构造得到的映射是唯一的。

### 6.2 边界理想给任意有界因子的真实除法障碍

若 $0\ne F\in\mathcal C$、$K\in\mathcal I$，则不存在任何 $B\in B(H)$ 使 $KB=F$，也不存在使 $BK=F$ 的有界 $B$。第一种关系给
$$
FF^*\le\|B\|^2KK^*,
$$
两边均在 $\mathcal D$ 内，应用正的 $*$-同态 $\Pi$ 就得 $FF^*\le0$，矛盾。第二种关系对 $F^*F\le\|B\|^2K^*K$ 同样处理。不要求 $B$ 属于 $\mathcal D$。

尤其对每个 $m\ge0$ 都不存在 $YB=A^m$ 或 $BY=A^m$。由真实值域包含的闭图因子引理，任何非零 $\mathcal C$ 算子的值域都不包含于 $\operatorname{Ran}Y$。更一般地，若 $K_1,\ldots,K_s\in\mathcal I$，也不可能有
$$
\operatorname{Ran}F\subseteq\sum_{i=1}^s\operatorname{Ran}K_i.
$$
否则对行算子 $(K_1,\ldots,K_s):H^s\to H$ 的最小范数解用闭图定理，得到 $FF^*\le C\sum_iK_iK_i^*$，应用 $\Pi$ 再次矛盾。这里是实际值域而非闭包；这些值域的闭包可以等于 $H$。

## 7. 边界与未解问题

本条没有证明整个 $\{A\}'$ 都等于 $\mathcal B$，没有证明 $\mathcal K$ 每个非零元素单射，也没有证明 $\mathcal B$ 的范数闭包中仍无零因子。有限多项式及指定收敛系数系列的独立性，不能未经证明传到任意范数极限。

同样，$\mathcal I$ 的存在是较大 $C^*$ 代数的理想结构，不是原有界 $A$ 的闭不变子空间。本文没有由一个 $C^*$ 商直接推出普通不变子空间，也没有把辅助表示的强*零极限移作原 Haar 表示的零极限。

本条真正完成的是：真实逃逸柱压缩构造、辅助前缀强*趋零、两侧 Schwarz 缺陷归零、因此合法升级的 $*$-商映射，以及由稠密值域/单射性分别保证的左右系数取消。

