# 可数交换稠密值域的共同核心与未知核的零横截

日期：2026-11-12（UTC）。作者：critical_kernel。
状态：完整的辅助引理与严格抽象反例；按根代理要求先保存为未编号 note。

本稿区分两个命题：

- 可数个两两交换的有界 quasiaffinity 在全空间确有稠密的共同逆域；
- 这个共同逆域与另一个交换算子的非零核，仍可能只有零向量。

第二个现象即使同时保留拟幂零性、共同 $C$ 对称、核饱和性，以及所生成多项式代数没有零因子也会发生。它不构造本课题实际 $A$ 的不变子空间；实际 gauge 家族的额外结构仍可能排除该障碍。

## 1. 全空间的共同范围确实稠密

**引理1.1。** 设 $R_1,R_2,\ldots\in B(H)$ 两两交换，且每个 $R_i$ 单射、值域稠密。则

$$
\mathcal D_1=\bigcap_{i\ge1}\operatorname{Ran}R_i
$$

在 $H$ 中稠密。

**证明。** 置 $P_0=I$、$P_n=R_1\cdots R_n$。给定 $x_0\in H$ 和 $\varepsilon>0$，令 $y_0=x_0$。递归选择 $y_n$，使

$$
\|R_ny_n-y_{n-1}\|<\delta_n,
$$

其中 $\delta_n>0$ 足够小，使将这个差左乘以下每个有限有界算子后，所得范数均小于 $\varepsilon 2^{-n}$：

$$
P_{n-1},\qquad
P_{n-1}^{(i)}
=\prod_{\substack{1\le k<n\\k\ne i}}R_k
\quad(1\le i<n).
$$

这样的 $y_n$ 存在，因为 $R_n$ 值域稠密。

置 $x_n=P_ny_n$。于是

$$
\|x_n-x_{n-1}\|<\varepsilon2^{-n}.
$$

所以 $x_n\to x$ 且 $\|x-x_0\|<\varepsilon$。

固定 $i$。对 $n\ge i$，由交换性和单射性，

$$
z_{i,n}:=R_i^{-1}x_n
=\left(\prod_{\substack{1\le k\le n\\k\ne i}}R_k\right)y_n
$$

是准确的原像。对 $n>i$，构造保证

$$
\|z_{i,n}-z_{i,n-1}\|<\varepsilon2^{-n}.
$$

因此 $z_{i,n}\to z_i$。$R_i$ 有界给 $R_iz_i=x$，故 $x\in\operatorname{Ran}R_i$。这对每个 $i$ 成立，证明稠密性。证毕。

### 1.1 所有有限乘积的共同逆域

把全部有限乘积 $\prod_iR_i^{m_i}$ 枚举成一个可数族，仍可应用引理1.1。得到稠密空间

$$
\mathcal D
=\bigcap_{\substack{m_i\ge0\\\text{有限支撑}}}
\operatorname{Ran}\!\left(\prod_iR_i^{m_i}\right).
\tag{1.1}
$$

它被每个 $R_i$ 及其在 $\mathcal D$ 上的逆保持。若 $x=R_i y\in\mathcal D$，对任意有限乘积 $P$ 有 $x\in\operatorname{Ran}(R_iP)$；单射消去 $R_i$ 得 $y\in\operatorname{Ran}P$，故 $y\in\mathcal D$。

此外，$\mathcal D$ 是每个 $R_i^{-1}$ 的图核心。若 $x=R_i y$ 属于该逆的域，取 $y_n\in\mathcal D$、$y_n\to y$，则

$$
x_n=R_i y_n\in\mathcal D,\qquad
(x_n,R_i^{-1}x_n)=(R_i y_n,y_n)\to(x,y).
$$

同一结论适用于有限乘积的逆。这个共同核心是全空间结论，没有断言它与任意闭不变子空间相交稠密。

## 2. 核饱和性只能识别横截，不能保证横截非零

若 $B$ 与所有 $R_i$ 交换，$M=\ker B$，则

$$
\boxed{M\cap\operatorname{Ran}R_i=R_iM.}
\tag{2.1}
$$

确实，$R_i y\in M$ 时 $R_iBy=BR_iy=0$；$R_i$ 单射给 $By=0$。

因此若要把逐参数跨核方程升级成固定共同像，真正需要的是

$$
M\cap\mathcal D\ne\{0\},
\tag{2.2}
$$

或者一个已构造的交换子 $Q$ 使 $QM\ne0$ 且 $\operatorname{Ran}Q\subseteq\mathcal D$。仅有 §1 的全空间稠密性和 (2.1)，不能推出 (2.2)。

下面给出一个明确反例。它比只展示某个 $R|_M$ 不稠密更强：即使取单个 quasiaffinity 的所有正整数幂，共同逆域也会完全避开 $M$。

## 3. 两组交替快权

在 $\ell^2(\mathbb N_0)$ 中使用标准基 $e_j$。令 $N_\ell=4^\ell$。定义符号 $s_0=1$，并对 $\ell\ge1$ 在

$$
N_{\ell-1}\le j<N_\ell
$$

上置 $s_j=(-1)^\ell$。设

$$
\mu_j=\exp(-(2+s_j)(j+1)^2),\qquad
\nu_j=\exp(-(2-s_j)(j+1)^2).
\tag{3.1}
$$

故

$$
e^{-3(j+1)^2}\le\mu_j,\nu_j\le e^{-(j+1)^2}.
\tag{3.2}
$$

记 $U_\mu,U_\nu$ 为加权前移：

$$
U_\mu e_j=\mu_j e_{j+1},\qquad
U_\nu e_j=\nu_j e_{j+1}.
$$

二者有界、单射、紧且拟幂零。拟幂零性可直接由

$$
\|U_\mu^n\|,\ \|U_\nu^n\|
\le\exp\!\left(-\sum_{k=1}^n k^2\right)
\tag{3.3}
$$

得到。它们的值域都位于 $e_0^\perp$，故不稠密。

定义累积对数比

$$
D_n=\log\frac{\nu_0\cdots\nu_{n-1}}{\mu_0\cdots\mu_{n-1}}
=2\sum_{j<n}s_j(j+1)^2.
\tag{3.4}
$$

在每个块末 $n=N_\ell$，最新一块压过此前各块，给

$$
(-1)^\ell D_{N_\ell}
\ge2\left(\sum_{k=1}^{N_\ell}k^2
-2\sum_{k=1}^{N_\ell/4}k^2\right)
\ge\frac13N_\ell^3.
\tag{3.5}
$$

最后一界可由平方和公式直接验证。也可使用 $n\ge4$ 时

$$
\sum_{k=1}^n k^2\ge n^3/3,\qquad
\sum_{k=1}^{n/4}k^2\le n^3/16,
$$

得到更强的 $5n^3/12$ 下界。

因此 $D_n$ 沿两条子序列分别达到正、负的三次量级；固定有限平移只带来二次量级误差。

## 4. 一个拟幂零 quasiaffinity 及其交换核

在

$$
H_0=\ell^2(\mathbb N_0)\otimes\ell^2(\mathbb N_0)
$$

上定义

$$
B_0=U_\mu^*\otimes I,\qquad
R_0=I\otimes U_\nu-U_\mu^*\otimes I.
\tag{4.1}
$$

它们有界、互相交换。$B_0$ 拟幂零但不幂零，其核为

$$
M_0=\ker B_0=\mathbb Ce_0\otimes\ell^2(\mathbb N_0).
\tag{4.2}
$$

两个张量项都拟幂零并交换，所以 $R_0$ 也拟幂零。例如对任意 $\delta>0$，分别取幂界 $C_\delta\delta^n$，二项展开给 $\|R_0^n\|\le C_\delta^2(2\delta)^n$，再令 $\delta\downarrow0$。

关键是 $R_0$ 及 $R_0^*$ 都单射。

### 4.1 $R_0$ 的零核

写 $x=\sum_{n,k\ge0}x_{n,k}e_n\otimes e_k$。方程 $R_0x=0$ 给

$$
\mu_nx_{n+1,0}=0,
$$

以及 $k\ge1$ 时

$$
\mu_nx_{n+1,k}=\nu_{k-1}x_{n,k-1}.
\tag{4.3}
$$

于是 $x_{n,k}=0$ 当 $n>k$。对每个固定 $r\ge0$，

$$
x_{n,n+r}
=\frac{\prod_{j=r}^{r+n-1}\nu_j}
{\prod_{j=0}^{n-1}\mu_j}\,x_{0,r}.
\tag{4.4}
$$

乘积比的对数为

$$
D_n+\sum_{j=n}^{n+r-1}\log\nu_j-\sum_{j=0}^{r-1}\log\nu_j.
\tag{4.5}
$$

后两项的绝对值至多 $3r(n+r)^2+C_r$。在 (3.5) 的正子序列上，(4.5) 趋于 $+\infty$。因此只要 $x_{0,r}\ne0$，(4.4) 沿该子序列就不趋零，更不可能平方可和。故每个 $x_{0,r}=0$，继而 $x=0$。

### 4.2 $R_0^*$ 的零核

同样，

$$
R_0^*=I\otimes U_\nu^*-U_\mu\otimes I.
$$

零核方程先给 $y_{n,k}=0$ 当 $k>n$，并给

$$
y_{n+r,n}
=\frac{\prod_{j=r}^{r+n-1}\mu_j}
{\prod_{j=0}^{n-1}\nu_j}\,y_{r,0}.
\tag{4.6}
$$

其乘积比对数是

$$
-D_n+\sum_{j=n}^{n+r-1}\log\mu_j-\sum_{j=0}^{r-1}\log\mu_j.
$$

在 (3.5) 的负子序列上同样趋于 $+\infty$，所以所有 $y_{r,0}=0$，即 $\ker R_0^*=0$。

综上，

$$
\boxed{R_0\text{ 单射、值域稠密、拟幂零}.}
\tag{4.7}
$$

本稿不声称 $R_0$ 紧；张量恒等放大不保紧性。

## 5. 共同逆域与核的横截恰为零

由 (4.1)，在 $M_0$ 上，

$$
R_0|_{M_0}=I_{\mathbb Ce_0}\otimes U_\nu.
\tag{5.1}
$$

因 $R_0^n$ 单射且与 $B_0$ 交换，§2 的饱和性给

$$
M_0\cap\operatorname{Ran}R_0^n=R_0^nM_0
=\mathbb Ce_0\otimes\operatorname{Ran}U_\nu^n.
\tag{5.2}
$$

$\operatorname{Ran}U_\nu^n$ 中的向量前 $n$ 个坐标全为零，所以

$$
\bigcap_{n\ge1}\operatorname{Ran}U_\nu^n=\{0\}.
$$

于是

$$
\boxed{
M_0\cap\bigcap_{n\ge1}\operatorname{Ran}R_0^n=\{0\},
}
\tag{5.3}
$$

而 §1 给出

$$
\overline{\bigcap_{n\ge1}\operatorname{Ran}R_0^n}=H_0.
\tag{5.4}
$$

特别，共同逆域是全空间稠密的、被 $B_0$ 保持的线性空间，但 $B_0$ 在它上面单射，尽管 $B_0$ 在全 $H_0$ 上具有非零闭核。这正是不能以一个稠密共同核心替代核内论证的情形。

## 6. 加入共同 $C$ 对称而不改变零横截

令

$$
H=H_0\oplus H_0,\qquad
B=B_0\oplus B_0^*,\qquad
R=R_0\oplus R_0^*.
\tag{6.1}
$$

记 $C_0$ 为物理基上的逐坐标复共轭，定义

$$
\mathcal C(x,y)=(C_0y,C_0x).
$$

全部权为实数，所以直接计算给

$$
\boxed{B^*=\mathcal C B\mathcal C,\qquad R^*=\mathcal C R\mathcal C.}
\tag{6.2}
$$

$R$ 仍是拟幂零 quasiaffinity，$B,R$ 交换且均拟幂零。$B$ 不是幂零算子。

因为 $B_0^*=U_\mu\otimes I$ 单射，

$$
M=\ker B=M_0\oplus\{0\}\ne\{0\}.
$$

(5.3) 立即给

$$
\boxed{
M\cap\mathcal D_R=\{0\},\qquad
\mathcal D_R:=\bigcap_{n\ge1}\operatorname{Ran}R^n
\text{ 在 }H\text{ 中稠密}.
}
\tag{6.3}
$$

因此，即使全部 $R^n$ 共享同一共轭、彼此交换并与核算子交换，也不能从全空间共同范围稠密推出核内共同像非零。

### 6.1 此例不依赖多项式零因子

事实上 $\mathbb C[B,R]$ 这个多项式代数忠实于两个独立形式变量。

先看第一块。把 $P(B_0,R_0)$ 改写成

$$
Q(U_\mu^*\otimes I,\ I\otimes U_\nu),
\qquad Q(x,y)=P(x,y-x).
$$

$P\mapsto Q$ 是多项式环自同构。若 $Q\ne0$，取 $N$ 大于其 $x$ 次数，作用在 $e_N\otimes e_0$ 上。不同单项式 $x^iy^j$ 输出不同基向量

$$
e_{N-i}\otimes e_j
$$

乘非零权，所以其和不为零。因此表示单射。双倍后的表示仍单射，故

$$
P_1(B,R)P_2(B,R)\ne0
$$

对非零多项式 $P_1,P_2$ 成立。

这仅说明所生成多项式代数是整环；没有声称其范数闭包具有本题 $\mathcal A$ 的全部性质。

### 6.2 一个共同有界交换正则子的明确不可能性

若 $Q_0\in B(H)$ 与 $B$ 交换，且

$$
\operatorname{Ran}Q_0\subseteq\mathcal D_R,
$$

则 $Q_0M\subseteq M\cap\mathcal D_R=\{0\}$。所以这样一个 $Q_0$ 不可能单射。

特别，不能仅凭上述共同对称、交换、全空间稠密值域及拟幂零性，声称总能构造一个单射有界共同因子，其像同时包含于全部 $\operatorname{Ran}R^n$。

## 7. 对实际 gauge 路线的边界

本稿不否定本课题特定 resultant 家族可能存在固定共同像。反例中的家族是 $R^n$，具有不断增长的乘积次数；它不是已经识别为实际有限 gauge 余项的家族，也没有本题的单生成 dyadic 权移表示。

实际路线仍可利用这些反例没有提供的结构，例如统一有限 jet、具体解析 cocycle、原分母的特殊图核心或真正的核内估计。

严格保留的结论是：

$$
\text{全空间共同逆域稠密}
\quad\not\Longrightarrow\quad
\text{它与未知交换核非零相交}.
$$

因此，一个固定共同像仍须在实际模型中被构造或从其特有关系推导，不能由一般稠密性、共同 $C$ 对称或多项式整环性自动获得。
