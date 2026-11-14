# R279：完整真 MP Gram 的玻色仿射传输与扩大的低占据相邻范围

日期：2026-11-14。作者：Astra-ISP-789f / root、boundary_core。AI-assisted：ChatGPT，GPT-6 Astra Pro。

**状态：下列定理、常数及原连续尾推论已证明。** 新点是任意两个高度的真实 MP Gram 之间的仿射传输，由此改进全部低占据相邻常数，并把首边的已付范围扩大到 $s\delta\le1/(2\sqrt2)$。一般正权、任意出生的无条件相邻常数 1 或有限统一常数仍未证明；原 graph $\Gamma$、高返回费用与普通 ISP 不因本稿自动闭合。

## 1. 原算子、完整逆与主定理

允许下面两种实际模型：

1. $N$ 个正物理权 $b_i>0$，给定出生 $s\ge0$ 和最高高度 $n\ge2$，满足 $N\ge2s+n$；
2. 无限正行 $b\in\ell^2$，有无限多个非零权。这里只用固定孔层的有界算子，不要求 $b\in\ell^1$。

记
$$
D=\sum_i b_iE_i,\qquad S=\sum_i b_i^2>0,
\qquad K_s=\ker(D:\mathcal H_s\to\mathcal H_{s-1}).
$$
对 $0\le j\le n$，定义
$$
\mathcal J_{j,s}
=(D^j/j!:\mathcal H_{s+j}\to\mathcal H_s)^\dagger|_{K_s},
\qquad
\Gamma_{j,s}=\mathcal J_{j,s}^*\mathcal J_{j,s},
\qquad\Gamma_{0,s}=I_{K_s},
\tag{1.1}
$$
以及
$$
\boxed{X_j=\frac{S^j}{j!}\Gamma_{j,s}.}
\tag{1.2}
$$
第 2 节证明所需完整层满射和有界 MP。一直先取完整 $D^j$ 的最小逆，再把源限制到同一个 $K_s$。

**定理 1.1（任意高度的仿射传输）。** 对上述全部合法源及任意 $1\le r<n$，
$$
\boxed{X_n\succeq I+\frac nr(X_r-I).}
\tag{1.3}
$$
并且 $X_j\succeq I$。因此同一源空间上的序列
$$
\frac{X_j-I}{j},\qquad j\ge1,
$$
按 Loewner 序递增。特别，
$$
\boxed{
\Gamma_{n,s}\succeq n!S^{-n}
\{nS\Gamma_{1,s}-(n-1)I\},
}
\tag{1.4}
$$
首个非平凡情形为
$$
\boxed{
\Gamma_{2,s}\succeq\frac4S\Gamma_{1,s}-\frac2{S^2}I.
}
\tag{1.5}
$$
这些是无稀散假设的完整 primitive 算子序；它们不等于尚未证明的一般相邻对数凸序。

## 2. 全部用到的满射与无限行定义域

### 2.1 固定层有界性

在平方自由正交基上，对每个 $p\ge1$ 先逐目标坐标用 Cauchy–Schwarz，再按输入子集计数，得到
$$
\|D_pu\|^2
\le S\sum_{|J|=p-1}\sum_{i\notin J}|u_{J\cup\{i\}}|^2
=pS\|u\|^2.
\tag{2.1}
$$
所以无限 $\ell^2$ 行在每个固定层上有唯一有界延拓。截断行还满足
$$
\|D_p(b)-D_p(b^{(M)})\|
\le\sqrt p\,\|b-b^{(M)}\|_2\longrightarrow0.
$$

### 2.2 有限合法范围的完整幂满射

令 $S_be_I=(\prod_{i\in I}b_i)e_I$，则逐层有
$D_b=S_b^{-1}D_{\boldsymbol1}S_b$，故所有层间幂保持秩。等权行满足
$$
[D_{\boldsymbol1},D_{\boldsymbol1}^*]=NI-2\mathcal N.
$$
若 $v\in K_k(D_{\boldsymbol1})$，直接归纳给
$$
D_{\boldsymbol1}(D_{\boldsymbol1}^*)^\ell v
=\ell(N-2k-\ell+1)(D_{\boldsymbol1}^*)^{\ell-1}v.
\tag{2.2}
$$
对于 $k\le N/2$，反复用
$\mathcal H_k=\ker D_{\boldsymbol1}\oplus\operatorname{Ran}D_{\boldsymbol1}^*$
得到由这些 primitive 串张成的分解。需要的一步满射也直接来自
$D_{\boldsymbol1}D_{\boldsymbol1}^*\succeq(N-2k)I$
在 $\mathcal H_k$ 上的正性。

每条经过目标 $\mathcal H_s$ 的串出生于某个 $k\le s$。条件
$N\ge2s+j$ 保证它仍延伸到 $s+j$；(2.2) 中对应的每个系数非零。因此
$$
D_b^j:\mathcal H_{s+j}\to\mathcal H_s
\quad\text{满射，}\qquad0\le j\le n.
\tag{2.3}
$$
这也是[有限相邻常数归约](R271-appendix-universal-adjacent-height-constants-finite-models-and-continuous-tail.md) §1 的完整层论证。

### 2.3 无限正 $\ell^2$ 行的所有固定幂都满射

这里不需要尾权接近，也不需要找到稀散小块。固定有限预算 $P=s+n$，选取至少 $2P-1$ 个非零物理位组成有限块 $I$。有限正权的秩论证保证
$$
D_I:\mathcal H_{I,k+1}\to\mathcal H_{I,k}
$$
对全部 $0\le k\le P-1$ 满射。把这些有限维最小右逆作直和，得到一个只作用在 $I$ 位上的有界算子 $R_I$；它在上述输入层满足 $D_IR_I=I$。

写 $E=D_{I^c}$。在总次数有限的空间上，$E$ 与 $R_I$ 交换；$E$ 每次降低一个外部孔，$R_I$ 只增加内部孔。对目标总次数 $p-1$、$1\le p\le P$，置
$$
\boxed{
\mathcal R_p=R_I\sum_{\ell=0}^{p-1}(-ER_I)^\ell.
}
\tag{2.4}
$$
每个非零中间量仍在 $R_I$ 允许的内部输入次数内，而且
$(ER_I)^p=0$，因为初始外部孔数至多为 $p-1$。于是
$$
D_p\mathcal R_p
=(I+ER_I)\sum_{\ell=0}^{p-1}(-ER_I)^\ell=I.
\tag{2.5}
$$
这是有界右逆：由 (2.1)，在相关固定层上
$\|E\|\le\sqrt p\,\|b_{I^c}\|_2$，而和式只有有限项。没有使用 $\sum_i b_i<\infty$。

组合 $\mathcal R_{s+1},\ldots,\mathcal R_{s+j}$，得到全部固定幂的有界右逆。因此 (1.1) 在无限模型中也定义为完整、处处有界的真正 MP；各 $\Gamma_{j,s}$ 是同一 $K_s$ 上有界正可逆算子。这里的右逆常数可依赖固定预算和选定有限块；没有声称对任意增长次数统一。

## 3. 玻色模式证明仿射传输

沿用 [原玻色嵌入](R271-appendix-all-birth-low-occupation-bosonic-minimal-gram-comparison.md) §3。原平方自由空间等距嵌入对称玻色空间，删除满足
$$
\mathcal B|_{\mathcal H_p}=D_p,
\qquad \mathcal B=\sum_i b_i a_i,
\qquad[\mathcal B,\mathcal B^*]=SI.
$$
取单粒子单位向量 $b/\sqrt S$ 作为第零模式，令 $a_0=\mathcal B/\sqrt S$。在每个总次数 $p$ 上，玻色空间正交分为
$$
\mathscr F_p=\bigoplus_{k=0}^p|k\rangle_0\otimes\mathscr V_{p-k},
$$
其中 $\mathscr V$ 是其余正交模式的玻色空间。无限 $\ell^2$ 情形的同一分解仍是 Hilbert 正交直和；所有当前次数算子由 (2.1) 及相应玻色层界有界。

先归一 $S=1$。若 $f\in K_s$，则 $a_0f=0$，故 $f$ 全在第零模式的真空分量。令
$$
x=\mathcal J_{n,s}f,\qquad D^nx=n!f.
$$
由于 $D$ 就是玻色 $a_0$ 的实际限制，逐占据分量可知
$$
x=\sum_{k=0}^n|k\rangle_0x_k,
\qquad x_n=\sqrt{n!}\,f.
\tag{3.1}
$$
更高占据分量必须为零。仅保留最高分量已经证明
$\Gamma_{n,s}\succeq n!I$，即 $X_n\succeq I$。

现在取 $1\le r<n$，并令
$$
u=\frac{r!}{n!}D^{n-r}x.
\tag{3.2}
$$
这是**实际原硬核层**中的向量，满足 $(D^r/r!)u=f$，但不假定它是 $r$ 阶最小解。因此
$\|u\|^2\ge\langle\Gamma_{r,s}f,f\rangle$。

写 $u=\sum_{k=0}^r|k\rangle_0u_k$。由玻色下降系数直接得到
$$
u_k=\frac{r!}{n!}
\sqrt{\frac{(n-r+k)!}{k!}}\,x_{n-r+k},
\qquad u_r=\sqrt{r!}\,f.
\tag{3.3}
$$
当 $k=r-j$，从 $u_k$ 回算 $x_{n-r+k}$ 的范数平方权为
$$
w_j=\left(\frac{n!}{r!}\right)^2
\frac{(r-j)!}{(n-j)!},\qquad0\le j\le r.
$$
这些权满足
$$
w_0=\frac{n!}{r!},\qquad
\frac{w_j}{w_0}
=\frac{n(n-1)\cdots(n-j+1)}{r(r-1)\cdots(r-j+1)}
\ge\frac nr\quad(j\ge1).
\tag{3.4}
$$
只舍去 $x$ 中被 (3.2) 杀掉的低占据非负范数，准确有
$$
\begin{aligned}
\|x\|^2
&\ge\frac{n!}{r!}
\left\{\|u_r\|^2+\frac nr\sum_{k<r}\|u_k\|^2\right\}\\
&=\frac{n!}{r!}
\left\{\frac nr\|u\|^2-
\left(\frac nr-1\right)r!\|f\|^2\right\}\\
&\ge\frac{n!}{r!}
\left\{\frac nr\langle\Gamma_{r,s}f,f\rangle-
\left(\frac nr-1\right)r!\|f\|^2\right\}.
\end{aligned}
\tag{3.5}
$$
除以 $n!$ 就得到 $S=1$ 的 (1.3)。共同缩放 $D/\sqrt S$ 保持 primitive 空间，并使 $\Gamma_j$ 变为 $S^j\Gamma_j$，从而得到一般尺度。

证明没有使用逐次 MP 等于真幂 MP，也没有估计或删除完整 $D^*\mathcal J_1$ 的高出生部分。关键是 (3.2) 是合法原像，取最小范数只发生在正确方向。

## 4. 从仿射传输得到相邻比较的谱条件

固定 $r\ge1$，假定高度 $r+1$ 合法。由 (1.3)，
$$
X_{r+1}\succeq\frac{(r+1)X_r-I}{r}.
$$
右边正可逆，因为 $X_r\succeq I$。准确还原各阶乘并取逆，得
$$
\boxed{
\Gamma_{r,s}\Gamma_{r+1,s}^{-1}\Gamma_{r,s}
\preceq (r-1)!S^{-(r-1)}\,
f_r(X_r),
}
\tag{4.1}
$$
其中
$$
f_r(x)=\frac{r^2x^2}{(r+1)((r+1)x-1)},\qquad x\ge1.
\tag{4.2}
$$
函数 $f_r$ 在 $[1,\infty)$ 上递增：其导数的符号为
$x((r+1)x-2)\ge0$。

另一方面 $\Gamma_{r-1,s}\succeq(r-1)!S^{-(r-1)}I$。
因此只要 $f_r(X_r)\preceq I$，就得到所需首邻序。
准确的较大根为
$$
\boxed{
\beta_r=
\frac{(r+1)^2+
\sqrt{(r+1)^4-4r^2(r+1)}}{2r^2}>1.
}
\tag{4.3}
$$
二次式 $r^2x^2-(r+1)^2x+(r+1)$ 在 $x=1$ 为 $-r<0$，故
$$
\boxed{
I\preceq X_r\preceq\beta_r I
\quad\Longrightarrow\quad
\Gamma_{r,s}\Gamma_{r+1,s}^{-1}\Gamma_{r,s}
\preceq\Gamma_{r-1,s}.
}
\tag{4.4}
$$
只涉及一个真实 $X_r$ 的函数演算；未假定三个原 Gram 交换。

## 5. 扩大的全部低占据相邻范围

置
$$
M=\max_i b_i^2,\qquad\delta=M/S,
$$
$$
B_{s,r}=\prod_{j=1}^r[1-(2s+j-1)\delta].
\tag{5.1}
$$
有限和无限 $\ell^2$ 模型均沿用同一定义。假设
$$
(2s+r-1)\delta<1.
\tag{5.2}
$$
这里仅用 (5.2) 支付第 $r$ 阶上界；第 $r+1$ 阶的满射已经由合法位数或 §2.3 支付，不另要求 $(2s+r)\delta<1$。

### 5.1 完整逆上界的自足回顾

真实 Boolean 交换关系给
$$
DD^*-D^*D=SI-2\sum_i b_i^2n_i
\succeq(S-2pM)I\quad\text{于 }\mathcal H_p.
$$
对任意 $v\in\mathcal H_s$，置 $v_j=(D^*)^jv$、$a_j=\|v_j\|^2$。由准确配对和 Cauchy–Schwarz，
$$
a_{j+1}\ge\frac{a_j^2}{a_{j-1}}+[S-2(s+j)M]a_j.
$$
从 $a_1\ge(S-2sM)a_0$ 归纳，得到
$$
\frac{a_j}{a_{j-1}}\ge j[S-(2s+j-1)M]>0,
\qquad1\le j\le r.
$$
逐项相乘、在完整 $\mathcal H_s$ 上取逆并最后压到 $K_s$，便是
$$
\boxed{I\preceq X_r\preceq B_{s,r}^{-1}I.}
\tag{5.3}
$$
这正是[旧全部出生低占据稿](R271-appendix-all-birth-low-occupation-bosonic-minimal-gram-comparison.md)的上界；新内容是将它与 §3 的仿射传输组合。

### 5.2 新的准确常数

由 (4.1)、(4.2)、(5.3)，
$$
\boxed{
\Gamma_{r,s}\Gamma_{r+1,s}^{-1}\Gamma_{r,s}
\preceq
\frac{r^2}{(r+1)B_{s,r}(r+1-B_{s,r})}
\,\Gamma_{r-1,s}.
}
\tag{5.4}
$$
若用真正 $D^j$ 的 MP Gram
$H_{j,s}=\Gamma_{j,s}/(j!)^2$，并以
$$
\mathsf C_{r+1}(D;s)
=\inf\{C: C H_{r+1,s}\succeq
H_{r,s}H_{r-1,s}^{-1}H_{r,s}\}
$$
表示原真实第一下降的最优常数，Schur 邻居反转及准确阶乘给
$$
\boxed{
\mathsf C_{r+1}(D;s)
\le\frac{r+1}{B_{s,r}(r+1-B_{s,r})}.
}
\tag{5.5}
$$
旧上下标量界给的是 $[(r+1)/r]B_{s,r}^{-2}$。新上界与旧上界之比为
$$
\frac{rB_{s,r}}{r+1-B_{s,r}}\le1,
$$
$B_{s,r}<1$ 时严格改进。

令 $\alpha_r=\beta_r^{-1}$，亦即
$$
\alpha_r=
\frac{(r+1)^2-\sqrt{(r+1)^4-4r^2(r+1)}}{2(r+1)}.
\tag{5.6}
$$
于是新的常数 1 已付范围为
$$
\boxed{
(2s+r-1)\delta<1,\qquad B_{s,r}\ge\alpha_r
\quad\Longrightarrow\quad
\Gamma_r\Gamma_{r+1}^{-1}\Gamma_r\preceq\Gamma_{r-1}.
}
\tag{5.7}
$$
要一个无需乘积的充分条件，可用
$$
B_{s,r}\ge1-\delta A_{s,r},\qquad
A_{s,r}=\sum_{j=1}^r(2s+j-1)
=r\left(2s+\frac{r-1}{2}\right).
$$
当 $A_{s,r}>0$ 时，
$$
\boxed{\delta A_{s,r}\le1-\alpha_r}
\tag{5.8}
$$
同时保证所有因子为正及 (5.7)。$s=0,r=1$ 时 $A_{s,r}=0$，直接有 $X_1=I$，单独按 (4.4) 处理。

## 6. 首边的显式二次误差及新阈值

取 $r=1$。此时 $B_{s,1}=1-2s\delta$，所以在 $2s\delta<1$ 及原合法高度 2 范围内，
$$
\boxed{
\Gamma_{1,s}\Gamma_{2,s}^{-1}\Gamma_{1,s}
\preceq\frac1{2(1-4s^2\delta^2)}I,
\qquad
\mathsf C_2(D;s)\le\frac2{1-4s^2\delta^2}.
}
\tag{6.1}
$$
首阶误差在这个上界中是 $(s\delta)^2$。特别，
$$
\boxed{
s\delta\le\frac1{2\sqrt2}
\quad\Longrightarrow\quad
\Gamma_{1,s}\Gamma_{2,s}^{-1}\Gamma_{1,s}\preceq I,
\qquad\mathsf C_2(D;s)\le4.
}
\tag{6.2}
$$
这仍要求有限模型 $N\ge2s+2$，或无限正 $\ell^2$ 模型。不能只凭稀散数值条件删除合法位数；例如 $N=3,s=1$ 的等权行满足该数值阈值，却没有所需完整二阶满射。

此前单独组合上下标量界只能从
$\tfrac12(1-2s\delta)^{-2}\le1$
得到
$$
s\delta\le\frac{1-1/\sqrt2}{2}=0.146446\ldots.
$$
本稿扩大为 $1/(2\sqrt2)=0.353553\ldots$，没有缩小 primitive 源空间或替换实际权。
出生一首边已有[任意正权的更强范围](R271-appendix-universal-birth-one-first-adjacent-primitive-gram-bound.md)；本节扩大的是所有出生同时适用的低占据范围，不撤销该出生一结果。

## 7. 原连续尾的直接推论

对原
$$
D_m=\sum_{j\ge m}(j+1)^{-2}E_j,\qquad m\ge5,
$$
令 $x=m+1$。积分比较给
$$
S_m=\sum_{k=x}^{\infty}k^{-4}\ge\frac1{3x^3},\qquad
M_m=x^{-4},\qquad\delta_m\le\frac3x.
$$
因此在 $6s<x$ 时，整个原 $K_{s,m}$ 有
$$
\boxed{
\mathsf C_2(D_m;s)\le
\frac2{1-36s^2/x^2}.
}
\tag{7.1}
$$
特别，
$$
\boxed{
0\le s\le\frac{m+1}{6\sqrt2}
\quad\Longrightarrow\quad
\Gamma_{1,s,m}\Gamma_{2,s,m}^{-1}\Gamma_{1,s,m}\preceq I.
}
\tag{7.2}
$$
全部高度也可直接将 $\delta_m\le3/(m+1)$ 代入 (5.7) 或较简洁的
$$
\frac{3r}{m+1}\left(2s+\frac{r-1}{2}\right)\le1-\alpha_r.
\tag{7.3}
$$
无限层满射已经由 §2.3 在原物理尾上证明，不依赖有限等权池或先删掉早期真实尾位。

## 8. 范围和仍未支付的部分

仿射传输 (1.3) 本身适用于任意合法正权；相邻常数改进 (5.4)–(7.3) 使用了明确的低占据条件。特别不能由此把原大出生 $s$ 或合法巨孔窗口全部纳入。

首边的完整硬核纤维仍为
$\Gamma_1=I+L_s^*L_s$、
$\Gamma_2=2I+4L_s^*L_s+M_s^*M_s$
（$S=1$），见[同一纤维及 Euler 工作稿](../notes/2026-11-14-bosonic-hardcore-first-edge-789f-next.md)。一般参数还需支付
$M_s^*M_s\succeq(L_s^*L_s)^2-2L_s^*L_s-I$。
本稿没有把该未知平方项当成正数删去，也没有把只控制 trace 的跨出生抵消当成算子序。

原 graph $\Gamma=\mathcal T^*\mathcal T$ 与本文 primitive MP Gram 不同。一般高出生相邻常数、原两个 Schur 逆、高返回能量、$N=M$ 和普通 Hilbert ISP 均仍保留。
