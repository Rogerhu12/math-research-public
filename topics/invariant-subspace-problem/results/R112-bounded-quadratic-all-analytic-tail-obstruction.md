# R112：有界二阶乘子的绝对幂表示及全部解析尾幂型障碍

**当前范围更新：** 后续 R122/R123 已证明本构造单射、值域稠密及符号全 H 循环；本文保留的是表示和幂型判据的严格边界。

日期：2026-11-12
作者：Astra-ISP-0c017065 / l2_moments
状态：R112 完整已证稿；此前根逐段独审通过。执行器重置后依据完整证明重建，并明确记录所有 $s>1$ 的直接推论。

本文构造
$$
0\ne f\in C(\mathbb Z_2)\cap H_{\le2},\qquad f(0)=0,
$$
其实际有界交换乘子 $S=X_f\in\mathcal A$ 满足：

1. 不存在绝对可和的归一化幂表示
   $S=\sum_{n\ge0}c_nA^n/W_n$，$\sum_n|c_n|<\infty$；
2. 通过递归远移 Hadamard 块，可以同时保证：对每个零点附近的解析芽 $F$ 及每个 $s>1$，
   $$
   \boxed{
   \liminf_{N\to\infty}
   \frac{-\log\|(S-F(A))^N\|}{N^s}=0.
   }
   $$
   特别地 $\tau_4(S-F(A))=0$，没有一个解析头使 R109 的严格四次型比较直接适用。

这两项均是已证方法边界，不证明 $S$ 有非零核，也不证明 $f$ 不循环。

## 1. 归一化系数的连续提取

令
$$
W_n=\|A^n\|,\quad W_0=1,\quad M_n=A^n/W_n.
$$
对有限多项式 $P(A)=\sum_np_nA^n$，定义
$$
\kappa_n(P(A))=W_np_n.
\tag{1.1}
$$
有真实算子范数界
$$
\boxed{|\kappa_n(P(A))|\le\|P(A)\|.}
\tag{1.2}
$$

证明：取 $N=2^m>\max(n,\deg P)$，令
$$
e_i^{(m)}=\sqrt N\,1_{\{\text{低 }m\text{ 位}=i\}}.
$$
这些向量正交归一。实际有限链上，对 $0\le k<N$，
$$
A^ke_0^{(m)}=W_ke_k^{(m)}.
$$
因为路径不跨越头周期，其权重精确为 $W_k$，独立尾坐标。因此
$$
\langle P(A)e_0^{(m)},e_n^{(m)}\rangle=W_np_n,
$$
得到 (1.2)。这不是仅由形式唯一性推断的范数下界。

所以 $\kappa_n$ 唯一连续延拓到 $\mathcal A$，范数至多 $1$。普通形式系数
$\gamma_n(T)=\kappa_n(T)/W_n$ 满足
$$
\gamma_n(TU)=\sum_{k=0}^n\gamma_k(T)\gamma_{n-k}(U),
\tag{1.3}
$$
由多项式范数逼近和有限系数乘法得到。无需假定无限形式 Taylor 级数有正收敛半径。

定义绝对归一化级数代数
$$
\mathcal L_W
=\left\{\sum_{n\ge0}c_nM_n:\sum_n|c_n|<\infty\right\},
\qquad \|T\|_W=\sum_n|c_n|.
\tag{1.4}
$$
(1.2) 保证表示唯一，$c_n=\kappa_n(T)$。又
$$
M_iM_j=\frac{W_{i+j}}{W_iW_j}M_{i+j},\qquad
W_{i+j}\le W_iW_j,
$$
所以
$$
\boxed{\|TU\|_W\le\|T\|_W\|U\|_W,\qquad \|T\|\le\|T\|_W.}
\tag{1.5}
$$
若 $F(z)=\sum a_nz^n$ 为解析芽，则
$$
\|F(A)\|_W=\sum_n|a_n|W_n<\infty
\tag{1.6}
$$
因为解析系数至多指数增长而 $W_n$ 有四次指数衰减。任意固定解析芽及其固定有限次幂的加权绝对系数尾都趋于零。

## 2. 有限 Walsh 乘子的真实公式

令
$$
N_j=A^{2^j}/W_{2^j},\qquad
R_j=N_j(I+N_j)^{-1},\qquad
V_j=I-2R_j.
$$
对有限集合 $J$，
$$
\boxed{X_{\chi_J}=\prod_{j\in J}V_j.}
\tag{2.1}
$$

取 $m>\max J$，$e_0=1_{\{\text{低 }m\text{ 位}=0\}}$。实际有限链与
$W_k=\prod_{b_j(k)=1}W_{2^j}$ 给
$$
\prod_{j<m}(I+N_j)e_0=1,
$$
$$
\prod_{j<m}(I+\epsilon_jN_j)e_0=\chi_J,\qquad
\epsilon_j=-1\ (j\in J),\quad \epsilon_j=1\ (j\notin J).
$$
所有幂指数小于 $2^m$，此处没有忽略进位。各 $I+N_j$ 可逆，约去即得 (2.1)。$1$ 循环保证乘子唯一。

该公式只针对互不重复的 Walsh 变量，不声称纯／实际乘子对应在一般乘法下是代数同态。

## 3. 分母误差在加权绝对代数中很小

实际关系
$$
N_j^2=\eta_jN_{j+1},\qquad \|N_j\|=1
$$
给
$$
\|N_j^s\|\le\eta_j^{\lfloor s/2\rfloor}.
$$
每个 $N_j^s$ 是一个归一化整数幂的标量倍数，故其 $\mathcal L_W$ 范数等于算子范数。因此
$$
R_j=\sum_{s\ge1}(-1)^{s-1}N_j^s
$$
在 $\mathcal L_W$ 中收敛，并且
$$
\boxed{
\|R_j-N_j\|_W
\le\frac{2\eta_j}{1-\eta_j}.
}
\tag{3.1}
$$
由 $\sup_j\eta_j<1$，放大一个固定常数 $C_0$ 可使
$$
\|R_j\|_W\le1+C_0\eta_j,\qquad
\boxed{\|R_iR_j-N_iN_j\|_W\le C_0(\eta_i+\eta_j).}
\tag{3.2}
$$
后一式由 $(R_i-N_i)R_j+N_i(R_j-N_j)$ 和 (1.5) 得到。

对 $i\ne j$，
$$
N_iN_j=M_{2^i+2^j}.
\tag{3.3}
$$
不同无序位对给不同的二进位指数。

## 4. Hadamard 块及连续二阶向量

对 $n\ge1$，设
$$
N^{(n)}=2^{4n},\qquad t_n=2^{-n},\qquad L_n=2^{2n}=\sqrt{N^{(n)}}.
\tag{4.1}
$$
取互不相交的位组
$$
I_n=\{i_x:x\in\mathbb F_2^{4n}\},\qquad
J_n=\{j_y:y\in\mathbb F_2^{4n}\},
$$
不同块使用的全部位也互不相交。位置在 §7 递归规定。

用 Sylvester 矩阵 $H_{xy}=(-1)^{x\cdot y}$，$HH^*=N^{(n)}I$，定义
$$
u_{i_xj_y}=t_n(N^{(n)})^{-3/2}H_{xy},
\qquad
q_n=\sum_{x,y}u_{i_xj_y}\chi_{i_x}\chi_{j_y}.
\tag{4.2}
$$
对任意 $\pm1$ 向量 $x,y$，
$$
|x^THy|\le\|x\|_2\|Hy\|_2=(N^{(n)})^{3/2},
$$
所以
$$
\|q_n\|_\infty\le t_n.
\tag{4.3}
$$
但
$$
\sum_{i,j}|u_{ij}|=t_n\sqrt{N^{(n)}}=2^n.
\tag{4.4}
$$
每个固定行或列的绝对和为
$$
t_n/\sqrt{N^{(n)}}=2^{-3n}\le1.
\tag{4.5}
$$

只有零标号行及零标号列的行和、列和非零，均为 $N^{(n)}$。因此
$$
q_n(0)=t_n/\sqrt{N^{(n)}}.
$$
令
$$
f_n=q_n-q_n(0)1,\qquad f=\sum_{n\ge1}f_n.
\tag{4.6}
$$
由 $\|f_n\|_\infty\le2t_n$，级数一致收敛。故
$$
0\ne f\in C(\mathbb Z_2)\cap H_{\le2},\qquad f(0)=0.
\tag{4.7}
$$
非零性由任意一个非零二阶 Walsh 系数可见。

R92 的次数统一乘子界给
$$
\|X_{f_n}\|\le C_2\|f_n\|_\infty\le2C_2t_n.
$$
于是
$$
S=\sum_nS_n\in\mathcal A,\qquad S_n=X_{f_n},\qquad S1=f.
\tag{4.8}
$$
这里按块算子范数绝对收敛；不声称按单个 Walsh 系数绝对收敛。

## 5. 不存在绝对归一化全幂表示

令 $\beta_i$ 为全部块的行／列系数和（每个物理顶点只属于一个块的一侧）。每块仅有两个非零 $\beta_i$，所以
$$
\sum_i|\beta_i|=2\sum_{n\ge1}2^{-3n}<\infty.
\tag{5.1}
$$
逐块用 (2.1) 展开：
$$
S_n=-2\sum_i\beta_iR_i+4\sum_{i,j}u_{ij}R_iR_j.
\tag{5.2}
$$
定义有限归一化多项式
$$
P_n=-2\sum_i\beta_iN_i+4\sum_{i,j}u_{ij}N_iN_j.
\tag{5.3}
$$
不同一位、二位指数互不混合，故
$$
B_n:=\|P_n\|_W
=4t_n\left(\sqrt{N^{(n)}}+\frac1{\sqrt{N^{(n)}}}\right).
\tag{5.4}
$$

由 (3.1)—(3.2)，
$$
\sum_n\|S_n-P_n\|_W
\le C\left[
\sum_i|\beta_i|\eta_i+
\sum_{i,j}|u_{ij}|(\eta_i+\eta_j)
\right]<\infty.
\tag{5.5}
$$
第二项按顶点整理为
$\sum_i\eta_i\sum_j|u_{ij}|$，由 (4.5) 至多为 $\sum_i\eta_i<\infty$。
因此
$$
E=\sum_n(S_n-P_n)\in\mathcal L_W.
\tag{5.6}
$$
并且 $\sum_nP_n=S-E$ 按算子范数收敛。

每个 $\kappa_k$ 连续，所以 $S-E$ 的二位系数恰为 $4u_{ij}$，一位系数恰为 $-2\beta_i$。由 (4.4)，其全部归一化系数绝对和无穷。加上 $\ell^1$ 系数的 $E$ 不能改变这一点：
$$
\boxed{\sum_{k\ge0}|\kappa_k(S)|=\infty.}
\tag{5.7}
$$
任意绝对归一化表示的系数必须等于 $\kappa_k(S)$，所以不存在这样的表示。此结论对所有不交块放置均成立。

## 6. 每块提供一个慢幂衰减的正系数

取一个 $2n$ 维子空间 $U\subset\mathbb F_2^{4n}$。其正交补也有
$L_n$ 个元素，且
$$
H_{xy}=+1\qquad(x\in U,\ y\in U^\perp).
$$
令 $T_n$ 为这些 $L_n$ 个行位和 $L_n$ 个列位，置
$$
\nu_n=\sum_{j\in T_n}2^j.
\tag{6.1}
$$
它恰有 $2L_n$ 个二进位 $1$。

有精确正系数
$$
\boxed{
\kappa_{\nu_n}(P_n^{L_n})
=a_n=
4^{L_n}(L_n!)^2
\left[t_n(N^{(n)})^{-3/2}\right]^{L_n}>0.
}
\tag{6.2}
$$
证明：$L_n$ 个因子最多提供 $2L_n$ 次位出现。任何一次线性项、重复位或进位都使最后的二进位数少于 $2L_n$，不能到达目标。故只能由完全不交的二次项组成，每个所选行、列位恰出现一次。有 $L_n!$ 个完美匹配及 $L_n!$ 个因子排序。所选子矩阵系数全正相等，没有相消。

由 $\log(L_n!)\ge L_n\log L_n-L_n$ 及 $L_n=2^{2n}$，
$$
-\log a_n\le CnL_n=O(L_n\log L_n).
\tag{6.3}
$$
因此对每个固定 $s>1$，
$$
\frac{-\log a_n}{L_n^s}\longrightarrow0.
\tag{6.4}
$$

## 7. 递归远移块：统一处理全部解析芽

令第 $n$ 块占用
$$
[m_n,m_n+2N^{(n)}),
$$
前半为行位、后半为列位，且要求
$$
m_{n+1}>m_n+2N^{(n)}.
\tag{7.1}
$$
未来块的形式首阶于是大于本块目标 $\nu_n$。

选择 $m_n$ 前，之前的有限解析和
$$
S_{<n}=\sum_{\ell<n}S_\ell
$$
已经固定。它来自一个零点附近的真正有理解析芽，常数项为零。设普通系数为 $\gamma_k(S_{<n})$，定义非负系数主函数
$$
H_n(z)
=\sum_{k\ge1}|\gamma_k(S_{<n})|z^k
+\sum_{k\ge1}n^{k+1}z^k.
\tag{7.2}
$$
它的收敛半径为正。令
$$
A_n=\sum_{k\ge1}W_k[z^k]H_n(z)<\infty.
\tag{7.3}
$$

对于任意满足
$$
F(0)=0,\qquad |[z^k]F|\le n^{k+1}\quad(k\ge1)
\tag{7.4}
$$
的解析芽，$G=S_{<n}-F(A)$ 的普通系数被 $H_n$ 控制，并有
$\|G\|_W\le A_n$。每个固定零常数解析芽对所有充分大 $n$ 都满足 (7.4)。

$B_n,a_n$ 不依赖块位置。选择 $m_n$ 足够大，使位段分离，并同时有：

1. 对每个 $1\le k\le L_n$，
   $$
   \sum_{\nu\ge2^{m_n}}W_\nu[z^\nu]H_n(z)^k
   \le\frac{a_n}{8(1+B_n)^{L_n}};
   \tag{7.5}
   $$
2. 分母误差满足
   $$
   \|S_n-P_n\|_W\le
   \min\left(1,\frac{a_n}
   {8L_n(A_n+B_n+1)^{L_n-1}}\right).
   \tag{7.6}
   $$

两者可同时实现：(7.5) 只有有限个固定解析幂，其加权尾趋零；(3.1)—(3.2) 又给
$$
\|S_n-P_n\|_W\le C B_n\eta_{m_n}\to0.
$$
所以每一步都有某个有限 $m_n$ 满足全部要求。未假定某种尚未证明的统一解析半径或统一尾速度。

## 8. 任意解析头之后的全部超线性下幂型都为零

固定 $F(0)=0$ 的解析芽。对所有充分大的 $n$，(7.4) 成立。令
$$
G=S_{<n}-F(A),\qquad L=L_n,\qquad P=P_n.
$$

### 8.1 旧解析幂的贡献

$P$ 的每个幂指数及 $\nu_n$ 都是 $2^{m_n}$ 的倍数。在
$$
(G+P)^L=P^L+\sum_{k=1}^{L}\binom LkG^kP^{L-k}
$$
中，任何混合项对 $\nu_n$ 的贡献要求 $G^k$ 总指数也是此倍数。$G(0)=0$ 排除总指数为零，因此必须至少为 $2^{m_n}$。即使保留常数的情形，零指数加至多 $L-k$ 个当前二位因子也不能产生目标的 $2L$ 个二进位 $1$。

由 $W_{\alpha+\beta}\le W_\alpha W_\beta$ 和 (7.5)，
$$
\begin{aligned}
\left|\kappa_{\nu_n}((G+P)^L-P^L)\right|
&\le\sum_{k=1}^{L}\binom Lk
\frac{a_n}{8(1+B_n)^L}B_n^{L-k}\\
&\le a_n/8.
\end{aligned}
\tag{8.1}
$$
这里保留了全部旧解析项，包括它们无限高的 Taylor 幂。

### 8.2 当前分母误差

设 $E_n=S_n-P_n$。加权代数中的幂差估计给
$$
\begin{aligned}
\|(G+S_n)^L-(G+P)^L\|_W
&\le L\|E_n\|_W
(A_n+B_n+\|E_n\|_W)^{L-1}\\
&\le a_n/8
\end{aligned}
\tag{8.2}
$$
由 (7.6)。所以
$$
\left|\kappa_{\nu_n}((S_{<n}+S_n-F(A))^{L_n})\right|
\ge3a_n/4.
\tag{8.3}
$$

### 8.3 未来块的形式阶

未来块的最小形式指数至少 $2^{m_{n+1}}>\nu_n$。其和按算子范数收敛，每个低阶连续系数均为零。利用 (1.3) 的有限系数乘法，它们对目标幂的 $\nu_n$ 系数完全没有贡献。因此
$$
\boxed{
\|(S-F(A))^{L_n}\|
\ge|\kappa_{\nu_n}((S-F(A))^{L_n})|
\ge a_n/2.
}
\tag{8.4}
$$
最后的范数下界直接使用 §1 的实际矩阵元。

由 (6.4)，对任意 $s>1$，
$$
\liminf_{N\to\infty}
\frac{-\log\|(S-F(A))^N\|}{N^s}\le0.
$$
对任何有界算子 $T$，$\|T^N\|\le\|T\|^N$ 保证该下极限不小于零，故等于零。

若 $F(0)\ne0$，则 $\kappa_0(S-F(A))=-F(0)$，由 (1.2)—(1.3)，
$$
\|(S-F(A))^N\|\ge|F(0)|^N.
$$
同样使全部 $s>1$ 的下幂型为零。于是主结论对所有解析芽成立。

特别地，任意有限块头后的算子尾也满足零四次下型。这里已检查块算子尾本身，不仅指出其全系数绝对可和失败。

## 9. 准确结论与未判定事项

所构造 $f$ 连续、有界、次数至多二、原点值为零，实际乘子在 $\mathcal A$ 中。但它的唯一归一化全幂系数不在 $\ell^1$；任意解析头余项又有零四次下型。因此 R110 的绝对级数机制和 R109 的严格四次型比较都不能自动覆盖它。

构造仍与 $S$ 单射稠密相容。R101 已排除该 $f$ 与任意非零有限次数另一端全矩消失；任意无限次数另一端尚未由本稿判定。没有把一种判据的失败当作实际非零核或 ISP 反例。
