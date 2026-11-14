# 全部自然混合 first 词共同域的自动一致图半范数与完备性

日期：2026-11-13（UTC+8）。作者：normal_next；AI-assisted，GPT-6 Astra Pro。状态：工作 note，记录实际共同域的拓扑事实。有限预解乘积的慢符号值域障碍已由 R253 第二附录证明，本稿不重复登记该结论。

## 1. 定义与一阶基础

$X_b$ 表示原 Haar 模型中 $b\in\ell^2$ 的实际闭 first 乘子。
定义
$$
\mathcal E_k=
\{f\in H:\text{每个长度不超过 }k\text{ 的自然词 }
X_{b^{(1)}}\cdots X_{b^{(r)}}f
\text{有定义，所有 }b^{(\nu)}\in\ell^2\},
$$
$\mathcal E_0=H$。自然词包含每个中间输入的域要求；最右侧算子先作用。
置
$$
M_0(f)=\|f\|,\qquad
M_r(f)=\sup_{\|b^{(1)}\|_2,\ldots,\|b^{(r)}\|_2\le1}
\|X_{b^{(1)}}\cdots X_{b^{(r)}}f\|,
\qquad
p_k(f)=\sum_{r=0}^kM_r(f).
\tag{1.1}
$$
下面证明每个 $M_r(f)$ 的有限性自动来自共同自然域，不是另加的定义条件。

[R253 单 first 附录 §4](../results/R253-appendix-all-first-common-domain-and-slow-range-obstruction.md)
已证明：对于 $g\in\mathcal E_1$，
$$
T_g:\ell^2\to H,\qquad T_gb=X_bg
$$
为有界线性映射。
关键是对支撑于前 $n$ 位的有限柱 $v$，
$$
\|X_b^*v\|
\le(3\sqrt n+1+8\|\eta\|_2)\|b\|_2\|v\|.
\tag{1.2}
$$
高位纯项互相正交，低位有限和，实际 carry 使用
$\|V_j-V_j^0\|\le8\eta_j$。
在这样的 $v$ 上配对给系数线性性。
若 $b_\ell\to b$、$X_{b_\ell}g\to y$，(1.2) 又给
$\langle y,v\rangle=\langle g,X_b^*v\rangle=\langle X_bg,v\rangle$，
故 $T_g$ 图闭。它全域定义，所以闭图定理给有界性。

## 2. 每个有限阶的单位球上界自动成立

对词长 $r$ 归纳证明：
$f\in\mathcal E_r$ 时，
$$
T_{r,f}(b^{(1)},\ldots,b^{(r)})
=X_{b^{(1)}}\cdots X_{b^{(r)}}f
\tag{2.1}
$$
是联合连续的 $r$ 重线性映射。$r=1$ 已证。

假设所有较短词的结论成立。
固定除第一个槽以外的系数行。
对应内层输出属于 $\mathcal E_1$，因为 $\mathcal E_r$ 的定义允许任意最外系数行。
故第一个槽的连续性由一阶结论给出。

若变化的是第 $j>1$ 个槽，最外层 $X_{b^{(1)}}$ 固定。
设该槽 $c_\ell\to c$ 且全词输出收敛到 $y$。
由长度 $r-1$ 的归纳假设，内层输出在 $H$ 中收敛到取 $c$ 时的正确内层输出。
再由最外层实际 $X_{b^{(1)}}$ 闭，
$y$ 必为槽参数取 $c$ 时的全词输出。
因此该槽映射全域且图闭；它的线性性来自一阶共同域上的系数线性性和其他实际线性算子的复合。
闭图定理给这一槽连续。

于是每个槽都分别连续。
在 Banach 空间的有限重线性映射中，分别连续性可由一致有界原理逐阶提升为联合有界性。
具体说，固定最后一个参数时，前 $r-1$ 个参数在单位球上的输出有界；
把这前 $r-1$ 个参数取遍单位球，得到关于最后参数的一族有界线性映射。
该族逐点有界，一致有界原理给算子范数的一致上界。
这同时完成重数归纳。因此
$$
\boxed{f\in\mathcal E_r\ \Longrightarrow\ M_r(f)<\infty.}
\tag{2.2}
$$
没有把无界算子乘积本身未经证明地当作闭算子；
每次闭图论证只使用最后单个固定闭 first 和已经连续的内层短词。

## 3. 实际共同图范数的完备性

$(\mathcal E_k,p_k)$ 是 Banach 空间。
若 $(f_n)$ 为 $p_k$-Cauchy，则 $f_n\to f$ 于 $H$，
且对每个固定行组和每个长度 $r\le k$，词输出在 $H$ 中也 Cauchy。
先对长度一使用 $X_b$ 的闭性。
再逐长度归纳：内层词的极限已确定，最外层 $X_b$ 闭，
故全词极限等于作用于 $f$ 的正确自然词。
所以 $f\in\mathcal E_k$。

每个固定词输出范数均在上述极限下连续，
对单位球取上确界，再对有限多个长度求和，得到下半连续性
$$
p_k(f_n-f)
\le\liminf_{\ell\to\infty}p_k(f_n-f_\ell)\longrightarrow0.
$$
证明完备。

令
$$
\mathcal E_\infty=\bigcap_{k\ge0}\mathcal E_k.
\tag{3.1}
$$
递增范数族 $(p_k)$ 使它成为 Fréchet 空间。
事实上，在每个 $p_k$ 中 Cauchy 的序列在每个 Banach 空间 $\mathcal E_k$ 中有极限；
这些极限因具有相同的 $H$ 极限而相容。
这里处理的是全部不可数系数行，由第 2 节的自动一致有界性压到可数个词长范数。

## 4. 次数光滑域、指数次数域与有界交换算子的接口

为避免混淆，用
$$
\mathcal G_\infty=
\bigcap_{s\ge0}\operatorname{Dom}(I+\mathcal N)^s
$$
表示 R253 第二附录的全部多项式次数光滑域。
[该附录 §1](../results/R253-appendix-polynomial-degree-smooth-domain-and-finite-resolvent-denominators.md)
证明了对实际 first 的一致估计
$$
\|X_bf\|_s\le K_s\|b\|_2\|f\|_{s+1},
\qquad \|f\|_s=\|(I+\mathcal N)^sf\|.
$$
逐次应用，所有中间次数域都有定义，得到
$$
\boxed{
\mathcal G_\infty\subseteq\mathcal E_\infty,\qquad
p_k(f)\le C_k\|f\|_k.
}
\tag{4.1}
$$
因此这个包含是连续映射，不只是逐个词的域包含。

同样，
[R207 指数次数附录 §A](../results/R207-appendix-exponential-chaos-weights-and-bounded-branch-head-cost.md)
对 $H_\sigma=\operatorname{Dom}e^{\sigma\mathcal N}$ 给
$$
\|X_b:H_\sigma\to H_{\sigma-\delta}\|
\le C\|b\|_2\delta^{-1/2},
\qquad 0<\delta\le\sigma\le1.
$$
把 $\sigma$ 分成 $k$ 个等长步，支付每个自然中间域，得
$$
H_\sigma\subseteq\mathcal E_\infty,\qquad
p_k(f)\le C_k'\sigma^{-k/2}\|e^{\sigma\mathcal N}f\|.
\tag{4.2}
$$

若有界 $Q$ 保持每个 $\operatorname{Dom}X_b$ 且按域与之交换，
则自然词逐次迭代给
$$
Q\mathcal E_k\subseteq\mathcal E_k,\qquad
p_k(Qf)\le\|Q\|p_k(f).
\tag{4.3}
$$
特别这适用于 $Q\in\mathcal A$：
用 $p_n(A)\to Q$ 于算子范数，
在一个 first 域中以 $X_b$ 的闭性取极限，即得该域交换；
随后逐词迭代。
这里没有对任意未经核查的无界乘积直接声称交换域。

## 5. 对已有值域障碍的逻辑关系

R253 第二附录已经给出单位向量 $z_n\in\mathcal G_\infty$，
使对 $S=S_N$ 或 $S_Y$ 分别有
$$
Sz_n\longrightarrow0\quad\text{于全部多项式次数图范数}.
$$
由 (4.1)，同一序列满足
$$
p_k(Sz_n)\longrightarrow0\quad\text{对每个 }k.
$$
而且该附录已经证明
$\mathcal G_\infty\not\subseteq\operatorname{Ran}S$。
所以仅从集合包含也立即得到
$$
\mathcal E_\infty\not\subseteq\operatorname{Ran}S.
$$
本稿无需另造有限头链、另作对角化，或再次登记有限 first 预解乘积的分母障碍。

新增内容只是全部自然混合词域的自动一致图半范数、Banach/Fréchet 完备性及明确连续接口。
它不构造 R244 中由假想正常见证决定的乘子配对域，
也不排除真正无穷预解式乘积。
