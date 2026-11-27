# 同一规范来源的全整数 carry 窗口倒数能量

日期：2026-11-27（UTC）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：以下同源必要预算及条件充分判据已证明；实际 $W$ 来源是否满足发散条件仍未知，未证明 $N=M$。**

本稿使用 [R247 的真实移位次数通量](../results/R247-shifted-degree-energy-flux-and-square-root-criterion.md)，不重新登记该通量公式。新增的是对**同一个规范形式原像**的全整数倒数窗口能量求和。它不同于旧高尾修复最小能量或不同头来源的倒数判据：本文不选择新原像，也不重新最小化来源。新判据包含有限次迭代对数超过平方根的层增长，并允许不规则的实际窗口能量。

## 1. 原来源及每一项的实际定义域

固定原 N 或 Y 模型，记
$$
M=\ker T,\qquad N=\overline{BM},\qquad W=M\ominus N,
\qquad w\in W.
$$
令 $h$ 为同一 $w$ 的唯一规范形式原像 $T^*h=w$，并按总物理孔数写
$$
h_p=\mathsf P_ph.
$$
[R234 的共同尾相似右逆](../results/R234-appendix-single-tail-similarity-and-exponential-hole-right-inverse.md) 已证明每个 $h_p$ 是实际 Hilbert 向量，且存在有限 $H_w$ 使
$$
\|h_p\|\le H_we^{24(p+1)}.
\tag{1.1}
$$
这里不假定 $h\in\mathcal H$。

两模型共同的准确局部 carry 分解为
$$
T=D+\sum_{L\ge1}K_L,
\qquad
\|K_L\|\le\delta_L:=52e^{-770\,16^{L-1}},
\tag{1.2}
$$
其中 $K_L$ 只作用于前 $L+1$ 个物理位。式 (1.2) 保留全部原 carry；Y 型的真实 Cayley 逆已包括在同一 $K_L$ 预算中。

对 $n\ge1$ 定义与 R247 相同的整数次数窗口
$$
I_{n,L}=[\max(0,n-L-1),\ n+L+1],
\qquad h_{I_{n,L}}=\sum_{p\in I_{n,L}}h_p.
$$
引入两个**同一来源**的非负量
$$
\boxed{
E_n(h)=\sum_{L\ge1}\delta_L\|h_{I_{n,L}}\|^2,
\qquad
F_n(w)=\sum_{L\ge1}\delta_L\|w_{I_{n,L}}\|^2.
}
\tag{1.3}
$$
每个 $E_n(h)$ 均有限：由 (1.1)，其第 $L$ 项至多
$$
\delta_L H_w^2(2L+3)e^{48(n+L+2)},
$$
而 (1.2) 使这个级数收敛。$F_n(w)$ 的有限性直接来自 $w\in\mathcal H$。

记固定正数
$$
A_\delta=\sum_{L\ge1}(2L+3)\delta_L<\infty.
\tag{1.4}
$$
所有来源仍是原 $w,h$；没有把一个有限孔层属于 $\mathcal H$ 误换为全部层平方可和。

## 2. 全整数同源倒数预算

R247 的准确移位截断已经消去全部纯项 $D^*$，并给
$$
\|\mathsf P_{\le n}w\|^2
\le2\sum_{L\ge1}\delta_L
       \|h_{I_{n,L}}\|\,\|w_{I_{n,L}}\|.
\tag{2.1}
$$
在同一个 $L$ 和同一个窗口上作 Cauchy--Schwarz，得到
$$
\boxed{
\|\mathsf P_{\le n}w\|^4\le4E_n(h)F_n(w).
}
\tag{2.2}
$$

另一方面，对固定孔数 $p$ 和固定 $L$，至多有 $2L+3$ 个整数 $n\ge1$ 使 $p\in I_{n,L}$。因此非负 Tonelli 求和给
$$
\begin{aligned}
\sum_{n\ge1}F_n(w)
&=\sum_{L\ge1}\delta_L\sum_{p\ge0}
  \#\{n\ge1:p\in I_{n,L}\}\,\|w_p\|^2\\
&\le A_\delta\|w\|^2.
\end{aligned}
\tag{2.3}
$$
这个计数包含 $L\ge n$、窗口覆盖原点的全部项。

若 $E_n(h)=0$，(2.2) 强迫 $\mathsf P_{\le n}w=0$；将该项的 $0/0$ 记为 $0$。事实上，本稿所有 $\delta_L>0$，且固定 $n$ 的窗口随 $L$ 穷尽全部次数，所以任一个 $E_n(h)=0$ 还强迫 $h_p=0$ 对所有 $p$ 成立，进而 $w=0$。于是 (2.2)--(2.3) 得到
$$
\boxed{
\sum_{n\ge1}
\frac{\|\mathsf P_{\le n}w\|^4}{E_n(h)}
\le4A_\delta\|w\|^2.
}
\tag{2.4}
$$
本稿实际来源的 $E_n(h)$ 由 §1 已全部有限。若在更一般的形式来源上使用扩展非负值写法，可以把有限分子除以 $+\infty$ 记为 $0$；那不会给缺失的有限性提供任何帮助。

特别，若 $w\ne0$，选 $n_0$ 使
$$
\|\mathsf P_{\le n}w\|^2\ge\frac12\|w\|^2
\qquad(n\ge n_0).
$$
此后 $0<E_n(h)<\infty$，且有明确必要预算
$$
\boxed{
\sum_{n\ge n_0}\frac1{E_n(h)}
\le\frac{16A_\delta}{\|w\|^2}<\infty.
}
\tag{2.5}
$$
因此，只要同一个实际规范来源满足
$$
\sum_{n\ge1}\frac1{E_n(h)}=\infty,
\tag{2.6}
$$
就必有 $w=0$。对 $1/E_n$ 的单独求和把 $E_n=0$ 解释为 $+\infty$；这与 (2.4) 中的 $0/0$ 约定用途不同。

也可只在一个明确子集 $\mathcal S\subset\mathbb N$ 上验证倒数和发散，因为 (2.4) 对任意子集继续成立；不能未经计算就把任意稀疏子列视为仍有发散倒数和。

## 3. 超过平方根的迭代对数层增长仍足够

定义正函数
$$
\ell_1(t)=\log(e+t),\qquad
\ell_{j+1}(t)=\log(e+\ell_j(t)),
\qquad
b_k(t)=(t+1)\prod_{j=1}^k\ell_j(t)
\quad(k\ge0).
\tag{3.1}
$$
空积为 $1$。每个 $\ell_j\ge1$ 且递增。对所有 $s,t\ge0$，
$$
\ell_j(t+s)\le(1+s)\ell_j(t),
\qquad
b_k(t+s)\le(1+s)^{k+1}b_k(t).
\tag{3.2}
$$
第一式对 $j=1$ 来自
$\log(e+t+s)\le\log(e+t)+\log(1+s)$；随后在递推中用
$e+(1+s)\ell_j(t)\le(1+s)(e+\ell_j(t))$ 归纳。第二式再乘上 $t+s+1\le(1+s)(t+1)$。

**推论。** 若对某个固定有限整数 $k\ge0$ 存在 $C<\infty$ 使同一规范来源满足
$$
\boxed{\|h_p\|\le C\sqrt{b_k(p)}\qquad(p\ge0),}
\tag{3.3}
$$
则 $w=0$。

证明。对 $p\in I_{n,L}$，有 $p\le n+L+1$，所以 (3.2) 给
$$
\|h_{I_{n,L}}\|^2
\le C^2(2L+3)(L+2)^{k+1}b_k(n).
$$
于是
$$
E_n(h)\le C^2 A_{\delta,k}b_k(n),
\qquad
A_{\delta,k}:=
\sum_{L\ge1}\delta_L(2L+3)(L+2)^{k+1}<\infty.
\tag{3.4}
$$
对于固定 $k$，基本积分比较及逐次对数换元给
$$
\sum_{n\ge1}\frac1{b_k(n)}=\infty.
\tag{3.5}
$$
也可将 (3.1) 与充分大 $n$ 时的
$n\log n\log\log n\cdots\log^{(k)}n$ 作固定常数比较，再积分；定义中的 $e$ 平移只处理有限小参数。
由 (3.4)--(3.5) 得 (2.6)，故 $w=0$。

$k=0$ 包含 R247 已有的平方根层增长；新增的例子包括
$$
\|h_p\|=O\bigl(\sqrt{(p+1)\log(e+p)}\bigr),
$$
以及再乘上任意**固定有限层**迭代对数的平方根。没有把有限层数换成随 $p$ 增长的层数，也没有宣称超过发散边界的所有增长都可用。

## 4. 当前用途与未支付来源

式 (2.4) 是原同一个 $w\in W$ 及其规范 $h(w)$ 的必要正预算。它可以用实际窗口能量检验，不要求逐层统一增长，不更换原像，也不要求未知 $w$ 的尾部满足额外衰减率。

本稿为窗口有限性使用的是方便的粗界 (1.1)。更好的既有指数阈值已经由 [R239 的实际指数右逆附录 A.11](../results/R239-appendix-exponential-hole-right-inverses-and-true-tail-regularization.md) 支付为 $\kappa>2+2\log(3/2)$；[R271 的实际全局各向异性读数 §1](../results/R271-appendix-true-global-anisotropic-low-head-growing-tail-adjoint-readout.md) 明确使用其中的 $\kappa=3$ 规范来源界。这些较好的有限指数界同样允许 $E_n(h)$ 指数增长和 (2.5) 的倒数可和，并非本文新增结论。因此本文未证明 (2.6) 对真实未知 $W$ 成立，未支付首位 $\Gamma(u)$ 的实际像费用，也未支付此前临界 $15/16$ 附录的输出逆权。后续继续保留同一 $u$、$w$ 和全部物理孔层。
