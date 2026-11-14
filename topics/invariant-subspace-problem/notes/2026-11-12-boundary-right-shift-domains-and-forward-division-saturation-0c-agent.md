# R200：慢边界核的标准右移域、有限旗消去与除法饱和

日期：2026-11-12（UTC）。作者：l2_moments。状态：已证明。本文同时适用于 R185、R188 的两个具体慢符号；最后的饱和问题仍未解决。

## 1. 对象与主结论

在负整数边界表示的 Hilbert 空间 $\mathcal H_-=\ell^2(\mathbb N_0)$ 上，
$$
Be_0=0,\qquad Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1).
$$
记
$$
W_0=1,\qquad W_n=\prod_{\nu=1}^n\alpha_{v_2(\nu)},\qquad
d_j=W_{2^j},\qquad a_j=(j+1)^{-2}.
$$
以下分别取
$$
T_N=\sum_{j\ge0}a_j\,\frac{B^{2^j}}{d_j},\qquad
T_Y=\sum_{j\ge0}a_j\,
\frac{B^{2^j}}{d_j}
\left(I+\frac{B^{2^j}}{d_j}\right)^{-1}.
\tag{1.1}
$$
两级数均按算子范数收敛。固定其中任意一个，简记 $T$，并置
$$
M=\ker T,\qquad N=\overline{BM}.
$$
本文只使用已由 R185、R188、R187 证明的下列真实边界事实：
$$
M\text{ 为无限维闭 }B\text{ 不变空间},\qquad
M\cap\ker B^r=\mathbb Ce_0\quad(r\ge1),
\tag{1.2}
$$
$$
e_0\in N,\qquad
\overline{B^rM}=N\quad(r\ge1).
\tag{1.3}
$$
(1.2) 也将在有限三角矩阵上重新核对。

对每个整数 $r\ge1$，定义标准右移逆
$$
J_rx=\sum_{n\ge0}x_n\frac{W_n}{W_{n+r}}\,e_{n+r}.
\tag{1.4}
$$
主结论为
$$
\boxed{
M\cap\operatorname{Dom}J_r
=M\cap\operatorname{Ran}B^r
=B^rM\oplus_{\rm alg}\mathbb Ce_0,
}
\tag{1.5}
$$
以及
$$
\boxed{
\overline{M\cap\operatorname{Dom}J_r}=N.
}
\tag{1.6}
$$
因此，对任意一个固定 $r\ge1$，
$$
\boxed{
N=M
\iff M\cap\operatorname{Dom}J_r\text{ 在 }M\text{ 中稠密}.
}
\tag{1.7}
$$

(1.5) 是代数直和，不是原 Hilbert 范数下的闭直和。它在准确的右移图范数下则是一个连续的一维分解，见第 4 节。本文不由 $\operatorname{Dom}J_r$ 在整个 $\mathcal H_-$ 中稠密推出 (1.7) 右侧。

## 2. 标准右移的准确闭域

令
$$
E_r=\operatorname{span}(e_0,\ldots,e_{r-1})=\ker B^r,\qquad E_0=\{0\}.
$$
这里下标 $r$ 是有限旗的维数，不是二进位位数。实际权积给
$$
B^re_{n+r}=\frac{W_{n+r}}{W_n}e_n.
\tag{2.1}
$$
于是
$$
\boxed{
\operatorname{Dom}J_r
=
\left\{x\in\mathcal H_-:
\sum_{n\ge0}|x_n|^2\frac{W_n^2}{W_{n+r}^2}<\infty\right\}
=\operatorname{Ran}B^r.
}
\tag{2.2}
$$

证明最后一个等号也给出全部预像。若 $x=B^ry$，则由坐标公式
$$
y=J_rx+v,\qquad v\in E_r.
\tag{2.3}
$$
反之，(2.2) 中的平方可和条件使 $J_rx\in\mathcal H_-$，并有 $B^rJ_rx=x$。特别 $J_rx$ 是垂直于 $E_r$ 的唯一预像。

$J_r$ 为闭算子：若 $x_k\to x$ 且 $J_rx_k\to y$，逐坐标极限给
$y_{n+r}=x_nW_n/W_{n+r}$ 及 $y|_{E_r}=0$，所以 $x\in\operatorname{Dom}J_r$ 且 $y=J_rx$。有限支撑向量属于其域，故它在整个 $\mathcal H_-$ 上稠密定义。

还准确成立
$$
B^rJ_rx=x,\qquad
J_rB^ry=y-P_{E_r}y,
\tag{2.4}
$$
以及
$$
B^{r-1}J_rx=J_1x
\quad(x\in\operatorname{Dom}J_r).
\tag{2.5}
$$
因此
$$
\operatorname{Dom}J_r\subseteq\operatorname{Dom}J_1,\qquad
\|J_1x\|\le\|B\|^{r-1}\|J_rx\|.
\tag{2.6}
$$
这些都是实际闭算子的等式，没有对 $B$ 使用一个不存在的有界逆。

## 3. 首阶 1 的有限旗消去

两种 $T$ 的形式首项均为
$$
t_1B,\qquad t_1=\frac{a_0}{d_0}=\frac1{\alpha_0}\ne0.
\tag{3.1}
$$
在 $E_r$ 上只需有限项：$B^nE_r=0$ 当 $n\ge r$；Cayley 逆也成为有限几何和。因此 $T|_{E_r}$ 是严格下三角矩阵，其第一副对角由非零 $t_1B$ 给出。等价地，
$$
T|_{E_r}=B|_{E_r}\,
\bigl(t_1I+\text{一个幂零多项式}\bigr).
$$
括号为有限维可逆矩阵，故
$$
\boxed{
TE_r=E_{r-1},\qquad
\ker(T|_{E_r})=\mathbb Ce_0.
}
\tag{3.2}
$$
这重新证明了 (1.2) 的有限旗部分。

取 $x\in M\cap\operatorname{Dom}J_r$。利用真正的有界交换关系，
$$
B^rTJ_rx=TB^rJ_rx=Tx=0.
$$
所以
$$
TJ_rx\in E_r.
\tag{3.3}
$$
其模 $TE_r=E_{r-1}$ 的障碍只剩最高坐标 $e_{r-1}$。

同时
$$
J_re_0=e_r/W_r,\qquad
\langle TJ_re_0,e_{r-1}\rangle
=\frac{t_1}{W_{r-1}}\ne0.
\tag{3.4}
$$
这里及以下内积取第一变量线性。选择唯一标量
$$
c=\frac{W_{r-1}}{t_1}\,
\langle TJ_rx,e_{r-1}\rangle,
\tag{3.5}
$$
便有
$$
TJ_r(x-ce_0)\in E_{r-1}=TE_r.
$$
再取 $v\in E_r$ 消去这个有限像：
$$
T\bigl(J_r(x-ce_0)+v\bigr)=0.
$$
因此
$$
x-ce_0
=B^r\bigl(J_r(x-ce_0)+v\bigr)\in B^rM.
\tag{3.6}
$$

反向包含显然成立，因为 $B^rM\subseteq M\cap\operatorname{Ran}B^r$，
且 $e_0\in M\cap\operatorname{Ran}B^r$。

还需验证直和。若 $B^ry=e_0$ 且 $y\in M$，(2.3) 给
$y=e_r/W_r+v$、$v\in E_r$；其 $T$ 像在 $e_{r-1}$ 的系数由 (3.4) 非零，矛盾。故
$$
e_0\notin B^rM.
\tag{3.7}
$$
结合 (3.6) 得到 (1.5)。再用 (1.3)，立即得到 (1.6)、(1.7)。

## 4. 所有阶数是同一条缺失行；图范数下的一维分解

在 $\operatorname{Dom}J_1$ 上定义
$$
\ell_T(x)=\langle TJ_1x,e_0\rangle.
\tag{4.1}
$$
它满足
$$
|\ell_T(x)|\le\|T\|\,\|J_1x\|,\qquad
\ell_T(e_0)=t_1.
\tag{4.2}
$$
由 (2.5)、$TB=BT$ 及实际首行权积，
$$
\begin{aligned}
\ell_T(x)
&=\langle TB^{r-1}J_rx,e_0\rangle\\
&=\langle B^{r-1}TJ_rx,e_0\rangle\\
&=W_{r-1}\langle TJ_rx,e_{r-1}\rangle.
\end{aligned}
\tag{4.3}
$$
所以 (3.5) 中的系数对全部 $r$ 一致：
$$
c=\ell_T(x)/t_1=\alpha_0\ell_T(x).
$$
主结论因而还可准确写为
$$
\boxed{
B^rM=
\{x\in M\cap\operatorname{Dom}J_r:\ell_T(x)=0\}.
}
\tag{4.4}
$$

置 $\mathcal D_r=M\cap\operatorname{Dom}J_r$，赋予图范数
$$
\|x\|_{\mathcal D_r}=(\|x\|^2+\|J_rx\|^2)^{1/2}.
$$
由于 $M$ 闭且 $J_r$ 闭，$\mathcal D_r$ 为 Hilbert 空间。
(2.6)、(4.2) 说明 $\ell_T|_{\mathcal D_r}$ 连续；
它在 $e_0$ 上非零。因此 (4.4) 的核是 $\mathcal D_r$ 中一个闭的余维 1 子空间，且
$$
x\longmapsto \frac{\ell_T(x)}{t_1}e_0
\tag{4.5}
$$
为连续投影。故 (1.5) 在这个图范数下是拓扑直和。

这个分解并没有提供原 Hilbert 范数下的有界投影。
确实，由 (1.3) 取 $x_k\in B^rM$、$x_k\to e_0$。
那么
$$
x_k-e_0\to0,\qquad
\ell_T(x_k-e_0)=-t_1\ne0.
\tag{4.6}
$$
所以 $\ell_T|_{\mathcal D_r}$ 作为原 Hilbert 范数中的线性泛函不可闭，
也不有界。其核在 $\overline{\mathcal D_r}=N$ 中稠密。

若需要准确的图范数右逆，可固定有限矩阵的逆
$$
K_r:E_{r-1}\longrightarrow E_r\cap e_0^\perp,
\qquad TK_r=I_{E_{r-1}},
$$
它由 (3.2) 存在且有界。对 $x\in\mathcal D_r$、$\ell_T(x)=0$，
$$
\mathcal R_rx=J_rx-K_rTJ_rx
\tag{4.7}
$$
属于 $M$，且 $B^r\mathcal R_rx=x$；并有
$$
\|\mathcal R_rx\|
\le(1+\|K_r\|\|T\|)\|J_rx\|.
$$
所有逆常数仅涉及这个固定有限旗。没有得到对原 $\|x\|$ 的一致控制。

## 5. 两具体符号的行系数

### 5.1. $T_N$：dyadic 缺失行

由实际单项式矩阵元，
$$
\boxed{
\ell_{T_N}(x)
=\sum_{j\ge0}\frac{a_j}{\alpha_j}\,x_{2^j-1},
\qquad x\in\operatorname{Dom}J_1.
}
\tag{5.1}
$$
该级数绝对收敛，因为 $\operatorname{Dom}J_1$ 的平方范数包含
$$
\sum_j |x_{2^j-1}|^2/\alpha_j^2,
$$
而 $a\in\ell^2$。这里使用 $d_j=W_{2^j-1}\alpha_j$。

因此对全部 $r$，
$$
B^r\ker T_N
=\left\{
x\in\ker T_N\cap\operatorname{Dom}J_r:
\sum_j\frac{a_jx_{2^j-1}}{\alpha_j}=0
\right\}.
\tag{5.2}
$$

### 5.2. $T_Y$：同样真实收敛的全部整数行

形式系数记为 $t_n^Y$。有限阶展开给
$$
t_n^Y
=
\sum_{\substack{j\ge0\\2^j\mid n}}
a_j\,(-1)^{n/2^j-1}d_j^{-n/2^j}
\quad(n\ge1).
\tag{5.3}
$$
对固定 $n$，该和只涉及有限多个 $j$，所以无需重排无限形式和。

真实向量 $T_Y^*e_0$ 的第 $n$ 坐标为 $t_n^YW_n$；
所有系数为实数。由 $T_Y$ 有界，
$$
\sum_{n\ge1}|t_n^YW_n|^2
=\|T_Y^*e_0\|^2<\infty.
$$
因此
$$
\boxed{
\ell_{T_Y}(x)
=\sum_{n\ge1}t_n^YW_{n-1}x_{n-1},
\qquad x\in\operatorname{Dom}J_1,
}
\tag{5.4}
$$
绝对收敛：把每一项写成
$(t_n^YW_n)(x_{n-1}W_{n-1}/W_n)$，
再用 Cauchy–Schwarz。

(5.4) 同 (4.4) 给出 $T_Y$ 的全部阶数像条件。
不因 Cayley 形式展开而假定一个未证明的有界除法算子。

## 6. forward 形式 Hilbert 主子模与准确饱和条件

用等距对应
$$
e_n\longleftrightarrow z^n/W_n
$$
把 $\mathcal H_-$ 写成形式 Hilbert 空间
$$
\mathscr H_W=
\left\{f(z)=\sum_{n\ge0}f_nz^n:
\sum_{n\ge0}|f_n|^2W_n^2<\infty\right\}.
\tag{6.1}
$$
这里允许形式级数的收敛半径为零，未把它视为某个开圆盘上的解析函数空间。
$B^*$ 对应有界的乘 $z$ 算子。

两种生成元分别为
$$
s_N(z)=\sum_j a_jz^{2^j}/d_j,\qquad
s_Y(z)=\sum_j a_j\,\frac{z^{2^j}/d_j}{1+z^{2^j}/d_j},
\tag{6.2}
$$
其中第二式按形式级数理解。实际有界的乘法算子是 $T_N^*$、$T_Y^*$，
其有界性来自 (1.1) 的算子范数收敛。

因为有限支撑向量稠密，而且
$e_n=(B^*)^ne_0/W_n$，有
$$
\mathcal I:=M^\perp
=\overline{\operatorname{Ran}T^*}
=\overline{\operatorname{span}\{(B^*)^nT^*e_0:n\ge0\}}
=\overline{s_T(z)\mathbb C[z]}^{\mathscr H_W}.
\tag{6.3}
$$
另一方面，
$$
N^\perp
=\{f\in\mathscr H_W:B^*f\in M^\perp\}
=\{f\in\mathscr H_W:zf\in\mathcal I\}.
\tag{6.4}
$$
故
$$
\boxed{
N=M
\iff
\{f\in\mathscr H_W:zf\in\mathcal I\}=\mathcal I.
}
\tag{6.5}
$$
这是实际 Hilbert 范数闭子模的除法饱和问题。
形式环中的首阶 1 分解 $s_T=z\cdot(\text{形式单位})$
只处理有限 jet，不能替代 (6.5) 的闭域问题。

## 7. $T_N^*$ 的真实柱和稀疏 Gram 矩阵

以下公式为继续研究 (6.5) 提供一个无近似的实际输入。
令
$$
\gamma_{n,j}=\frac{W_{n+2^j}}{W_nd_j}\in(0,1].
$$
则
$$
\boxed{
T_N^*e_n=\sum_{j\ge0}a_j\gamma_{n,j}e_{n+2^j}.
}
\tag{7.1}
$$
当 $n$ 的第 $j$ 位为 0，二进位中没有进位，所以 $\gamma_{n,j}=1$。
当从第 $j$ 位起恰有 $\ell\ge1$ 个连续 1，随后一位为 0，则实际权积为
$$
\boxed{\gamma_{n,j}=\alpha_{j+\ell}/\alpha_j.}
\tag{7.2}
$$
这也可由 $N_j=E_j+\eta_jE_j^*N_{j+1}$ 逐次递推得到；
连续进位的系数为
$\eta_j\cdots\eta_{j+\ell-1}=\alpha_{j+\ell}/\alpha_j$。

因此
$$
\boxed{
\langle T_N^*e_n,T_N^*e_m\rangle
=
\sum_{\substack{j,k\ge0\\n+2^j=m+2^k}}
a_ja_k\,
\frac{W_{n+2^j}^2}{W_nW_md_jd_k}.
}
\tag{7.3}
$$
$\gamma\le1$、$a\in\ell^1$ 保证这里的收敛。

当 $n\ne m$，非对角碰撞至多有一个有序指标对。
例如 $n>m$ 时，
$$
n-m=2^k-2^j,\qquad k>j.
$$
先由 $j=v_2(n-m)$ 唯一确定低指标，
再检查奇数部分是否为 $2^{k-j}-1$。
所以 Gram 的非对角支撑恰受这些二幂差位置限制。
本文尚未从该稀疏性推出一个除法范数估计。

## 8. 已确定的范围与尚存问题

有限旗的代数障碍已完整计算：每个阶数都只剩同一个 $e_0$ 方向，
而这个方向已经位于像的闭包中。
全部阶数的缺失行是同一个真实图范数连续泛函 $\ell_T$，
它在原 Hilbert 范数中不可闭。

现在 $N=M$ 的准确剩余条件是 (1.7)，等价于 (6.5)。
R187 的每个有限头满射及其有界线性延拓不能消去这个条件，
因为延拓常数随头增长而失控。
同样，$\operatorname{Ran}B^r$ 在整个空间中的稠密性，
不能自动传给与 $M$ 的交。

本文既未证明 $N=M$，也未构造 $N\subsetneq M$ 的见证。
它不改变边界表示与原 Haar 不变子商之间没有非零有界交织的事实，
也不声称完成原不变子空间问题。
