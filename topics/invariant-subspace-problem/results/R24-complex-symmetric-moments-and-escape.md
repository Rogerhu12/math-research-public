# R24：复对称双线性矩：交换子结构及有限阶精确匹配

日期：2026-11-12（UTC+8）。会话：Astra-ISP-e2cb8f94，子任务 `centered_literature`。

**状态。** §§1–5 的结论均有完整证明，是具体模型的中间进展；没有构造全部矩消失的非零向量对，没有证明普通不变格平凡，不主张文献新颖性。本条给出一组越来越多阶的**精确**矩匹配，明确算出首个失败矩与范数逃逸，不能把它当成无限阶解。依赖 R9、R11、R12 的已证公式；本文重新推导所需双线性恒等式。

## 1. 复对称性与交换子为交换代数

采用内积第一变量线性的约定。仍在 $H=L^2(\mathbb Z_2,\mu)$ 上令

$$
(Af)(y)=w(y)f(y-1),\qquad w(y)=a_{v_2(y)},\qquad w(0)=0,
\tag{1.1}
$$

其中 $a_j>0$ 为 R9 的严格递减权。定义

$$
(Cf)(y)=\overline{f(-1-y)},\qquad
B(f,g)=\langle f,Cg\rangle=\int f(y)g(-1-y)\,d\mu(y).
\tag{1.2}
$$

$C$ 是反线性等距对合；$B$ 是连续、非退化、对称的复双线性形式。由

$$
(A^*f)(y)=w(y+1)f(y+1),\qquad w(-y)=w(y),
$$

直接得到

$$
CA^*C=A,\qquad B(Af,g)=B(f,Ag).
\tag{1.3}
$$

对任意有界算子 $S$ 记 $S^\sharp=CS^*C$；这个运算复线性且逆转乘积次序。

**引理 1.1（一般循环复对称算子）。** 若 $T=CT^*C$ 有循环向量 $e$，则每个 $S\in\{T\}'$ 都满足 $S^\sharp=S$，并且交换子代数 $\{T\}'$ 是交换的。

**证明。** 对任意复多项式 $p,q$，交换关系及 $T$ 的 $B$-对称性给

$$
\begin{aligned}
B(Sp(T)e,q(T)e)
&=B(p(T)Se,q(T)e)\\
&=B(Se,p(T)q(T)e)\\
&=B(p(T)e,Sq(T)e).
\end{aligned}
$$

多项式轨道稠密，$S$ 与 $B$ 连续，所以 $B(Sx,y)=B(x,Sy)$ 对所有 $x,y$ 成立，即 $S^\sharp=S$。若 $S,R\in\{T\}'$，则 $SR$ 也在交换子中，因此

$$
SR=(SR)^\sharp=R^\sharp S^\sharp=RS.
$$

证毕。

R11 已证明 $e=1$ 对本算子 $A$ 循环，所以引理适用。这并不把交换子认成有界多项式的 SOT/WOT 闭包，也不推出每个普通不变子空间均超不变。它仅说明：不能在交换子中寻找非零 $C$-反对称算子来自动制造抵消，因为 $S^\sharp=-S$ 与上述结论合起来会迫使 $S=0$。

**文献边界。** 复对称算子的标准双线性语言见 Stephan Ramon Garcia、Emil Prodan、Mihai Putinar，*Mathematical and physical aspects of complex symmetric operators*，arXiv:1404.1304v3（2014），§2.3，式 (2.26)、Lemma 2.27，PDF pp. 9–10：<https://arxiv.org/pdf/1404.1304>。本文的交换子引理已给出自含证明，不将其作为新颖性声称。早期文献为 Garcia–Putinar，*Complex symmetric operators and applications*，Trans. Amer. Math. Soc. 358 (2006), 1285–1315，DOI <https://doi.org/10.1090/S0002-9947-05-03742-6>；本次其 AMS PDF 链接返回 403，没有为该引理猜测定理号。Garcia 的 2010 公开问题稿末页仍将复对称类的普通 ISP 列为问题：<https://nsa.fjfi.cvut.cz/problems/01_ESF_2010/2010-04/2010-04_ESF_Garcia.pdf>。这只是该历史出处的范围，不用它代替截至本次的完整文献核查。

## 2. 两个平方矩相等与一般矩消失严格等价

记

$$
Q_n(h)=B(A^nh,h),\qquad n\ge0.
\tag{2.1}
$$

因为 $B(A^n\cdot,\cdot)$ 对称，任意 $h,g$ 满足

$$
\boxed{B(A^n(h+g),h-g)=Q_n(h)-Q_n(g).}
\tag{2.2}
$$

因此若存在 $h\ne\pm g$ 使 $Q_n(h)=Q_n(g)$ 对所有 $n\ge0$ 成立，则 $f=h+g\ne0$、$v=C(h-g)\ne0$ 满足 $\langle A^nf,v\rangle=0$ 对所有 $n$ 成立，其闭循环子空间为非零真不变子空间。

反过来，若已有非零矩消失对 $f,v$，取

$$
h=\frac{f+Cv}{2},\qquad g=\frac{f-Cv}{2}.
\tag{2.3}
$$

则 $h+g=f\ne0$、$h-g=Cv\ne0$，且 (2.2) 给全部平方矩相等。故允许一般 $h,g$ 时，这只是同一个存在性问题的等价表达，不能计作已经构造出解。

**有界交换子参数化的准确含义。** 若固定循环向量 $e$，尝试写 $g=Se$，其中有界 $S\in\{A\}'$，则

$$
Q_n(Se)=B(A^nS^2e,e)
$$

由 §1 得到。若全部矩与 $e$ 相同，便有

$$
B((S^2-I)e,A^ne)=0\qquad(n\ge0).
$$

循环性和非退化性迫使 $(S^2-I)e=0$，再用交换关系及循环性得到 $S^2=I$。若 $Se\ne\pm e$，则 $S\ne\pm I$，于是 $(I\pm S)/2$ 已是两个非零有界交换幂等算子（不要求正交），给出不变子空间。这是有效的充分构造，但仍需真正找到非平凡的 $S$；不能用它绕开存在性难题。

## 3. 跨越高位边界的精确分解

固定 $k\ge0$，令 $N=2^k$，把 $y$ 唯一写成

$$
y=r+Nz,\qquad 0\le r<N,\quad z\in\mathbb Z_2.
$$

只依赖第 $k$ 位的函数写成

$$
g_{\alpha,\delta}(y)=
\begin{cases}
\alpha,&z\text{ 偶},\\
\delta,&z\text{ 奇}.
\end{cases}
\tag{3.1}
$$

定义尾权平均

$$
c_k=\sum_{s=1}^{\infty}2^{-s}a_{k+s},\qquad
\rho_k=\frac{c_k}{a_k}.
\tag{3.2}
$$

由严格递减性，$0<\rho_k<1$，并且

$$
\frac12\frac{a_{k+1}}{a_k}\le\rho_k\le\frac{a_{k+1}}{a_k}\longrightarrow0.
\tag{3.3}
$$

对于整数 $n=qN+t$，$0\le t<N$，区间 $y,y-1,\dots,y-n+1$ 含有的 $N$ 的倍数个数为

$$
d=d_{r,n}=\begin{cases}q+1,&r<t,\\q,&r\ge t.\end{cases}
\tag{3.4}
$$

这些倍数是 $Nz,N(z-1),\dots,N(z-d+1)$。其余因子的 $2$-进赋值都小于 $k$，所以只依赖 $r,n$，与 $z$ 无关。故存在正数 $K_{k,n}(r)$ 使

$$
W_n(r+Nz)=K_{k,n}(r)\prod_{j=0}^{d-1}a_{k+v_2(z-j)}.
\tag{3.5}
$$

空乘积取 $1$；碰到权的零点只涉及零测集，不影响积分。

又 $y-n$ 的高位尾部是 $z-d$，而 $-1-y$ 的高位尾部为 $-1-z$。因此：

- $d$ 偶数时，$g(y-n)g(-1-y)=\alpha\delta$；
- $d$ 奇数时，$z$ 奇数给乘积 $\alpha^2$，$z$ 偶数给乘积 $\delta^2$。

设 $\mathcal W_{k,d}(z)=\prod_{j=0}^{d-1}a_{k+v_2(z-j)}$，并在奇数 $d$ 时记

$$
O_{k,d}=\mathbb E(\mathcal W_{k,d}\mid z\text{ 奇}),\qquad
E_{k,d}=\mathbb E(\mathcal W_{k,d}\mid z\text{ 偶}).
\tag{3.6}
$$

对应 $r$ 的双线性矩贡献，在偶数 $d$ 时是

$$
\frac{K_{k,n}(r)}N\alpha\delta\int\mathcal W_{k,d}\,d\mu,
\tag{3.7}
$$

在奇数 $d$ 时是

$$
\frac{K_{k,n}(r)}{2N}
\bigl(\alpha^2O_{k,d}+\delta^2E_{k,d}\bigr).
\tag{3.8}
$$

特别地

$$
O_{k,1}=a_k,\qquad E_{k,1}=c_k,
\tag{3.9}
$$

$$
O_{k,3}=a_k^2c_k,\qquad
E_{k,3}=a_ka_{k+1}c_{k+1}.
\tag{3.10}
$$

为核实 (3.10)，在奇数情形写 $z=2u+1$，三项权为 $a_k,a_{k+1+v_2(u)},a_k$；中间项的均值正是 $c_k$。在偶数情形写 $z=2u$，三项权为 $a_{k+1+v_2(u)},a_k,a_{k+1+v_2(u-1)}$；$u,u-1$ 一个奇一个偶，两个尾权乘积的平均是 $a_{k+1}c_{k+1}$。这给出全部公式。

## 4. 精确匹配到第 $2^{k+1}$ 阶，以及首个失败矩

**定理 4.1。** 令 $h=1$，并定义实正函数

$$
g_k(y)=\sqrt{\rho_k}\,\mathbf1_{\{b_k=0\}}(y)
+\rho_k^{-1/2}\,\mathbf1_{\{b_k=1\}}(y).
\tag{4.1}
$$

则 $g_k\ne\pm1$，且

$$
Q_n(g_k)=Q_n(1)\qquad(0\le n\le2^{k+1}).
\tag{4.2}
$$

但在紧接的第 $2^{k+1}+1$ 阶，设

$$
C_k=\prod_{j=0}^{k-1}a_j^{2^{k-j-1}},\qquad C_0=1,
$$

则有严格负的精确差值

$$
\boxed{
Q_{2N+1}(g_k)-Q_{2N+1}(1)
=\frac{C_k^2}{2N}(1-\rho_k)\frac{a_k^2}{c_k}
\bigl(a_{k+1}c_{k+1}-c_k^2\bigr)<0.
}
\tag{4.3}
$$

**证明。** (4.1) 的两取值满足

$$
\alpha\delta=1,\qquad
a_k\alpha^2+c_k\delta^2=a_k+c_k.
\tag{4.4}
$$

当 $0\le n\le2N$ 时，每个 $r$ 的跨界数 $d$ 只能取 $0,1,2$。偶数情形由 (3.7) 和 $\alpha\delta=1$ 与常函数完全相同；$d=1$ 的情形由 (3.8)、(3.9)、(4.4) 完全相同。因此 (4.2) 成立。

当 $n=2N+1$ 时，只有 $r=0$ 给 $d=3$，其余 $r$ 都给 $d=2$，故差值仅来自 $r=0$。该段的非 $N$ 倍数各在两整段内出现一次，所以

$$
K_{k,2N+1}(0)
=\left(\prod_{j=1}^{N-1}a_{v_2(j)}\right)^2=C_k^2.
$$

将 (3.10)、$\alpha^2=\rho_k$、$\delta^2=\rho_k^{-1}$ 代入 (3.8)，差值为

$$
\begin{aligned}
\frac{C_k^2}{2N}
\bigl[(\rho_k-1)a_k^2c_k
+(\rho_k^{-1}-1)a_ka_{k+1}c_{k+1}\bigr]
\end{aligned}
$$

化简即得 (4.3) 的等式。

R12 的权比公式给

$$
\frac{a_{j+1}}{a_j}
=\exp(-1400\,16^j+630\,8^j-300\,2^j)
\le e^{-770\,16^j}<\frac14.
$$

因此

$$
a_{k+1}c_{k+1}\le a_{k+1}a_{k+2}
<\frac14a_{k+1}^2\le c_k^2,
\tag{4.5}
$$

证明严格负号。证毕。

**单一高位族中的完整分类。** 若 $g_{\alpha,\delta}$ 满足 $Q_0(g)=Q_0(1)$ 和 $Q_N(g)=Q_N(1)$，则必有

$$
(\alpha,\delta)=(1,1),\ (-1,-1),\
(\sqrt{\rho_k},\rho_k^{-1/2}),\
(-\sqrt{\rho_k},-\rho_k^{-1/2}).
\tag{4.6}
$$

事实上零阶条件给 $\alpha\delta=1$，而 $n=N$ 时 (3.5) 的非倍数因子恒为 $C_k$，故得到第二个 (4.4)。消去 $\delta=1/\alpha$，有

$$
(\alpha^2-1)(a_k\alpha^2-c_k)=0.
$$

这给 (4.6)，包括所有复取值情形。因此该族的非平凡解均为 $\pm g_k$；它们恰好匹配到 $2N$，下一阶失败。匹配到 $2N+1$ 时只剩 $\pm1$。

## 5. 范数逃逸和精确矩消失对的弱极限陷阱

由 (4.1)

$$
\|g_k\|^2=\frac12(\rho_k+\rho_k^{-1})\longrightarrow\infty.
\tag{5.1}
$$

结合 (3.3)，还得到

$$
\|g_k\|\ge\left(2\frac{a_{k+1}}{a_k}\right)^{-1/2}.
\tag{5.2}
$$

这是单一高位族内全部非平凡匹配解的共同障碍，不只是某个任意选择造成的范数增大。它不覆盖一般的多位函数或一般 $h$。

另一方面，可以把两个矩消失分量各自单位化，定义

$$
f_k=\frac{1+g_k}{\|1+g_k\|},\qquad
v_k=\frac{C(1-g_k)}{\|1-g_k\|}.
\tag{5.3}
$$

分母非零。由 (2.2)、(4.2)，对每个 $k$ 有

$$
\boxed{\langle A^nf_k,v_k\rangle=0\qquad(0\le n\le2^{k+1}).}
\tag{5.4}
$$

但由 $\rho_k\to0$ 和两个点上的显式值，

$$
f_k-\sqrt2\,\mathbf1_{\{b_k=1\}}\longrightarrow0,
\qquad
v_k+\sqrt2\,\mathbf1_{\{b_k=0\}}\longrightarrow0
\quad\hbox{于 }L^2.
\tag{5.5}
$$

例如第一式只需将 $1+g_k$ 除以 $\rho_k^{-1/2}$：它在第 $k$ 位为 $0,1$ 时分别为 $\sqrt{\rho_k}+\rho_k$、$1+\sqrt{\rho_k}$，归一化因子趋于 $1/\sqrt2$；第二式先用 $C$ 交换两个位值再同样计算。

高位柱投影 WOT 趋于 $I/2$，所以

$$
f_k\rightharpoonup\frac1{\sqrt2}\,1,
\qquad
v_k\rightharpoonup-\frac1{\sqrt2}\,1.
\tag{5.6}
$$

两个弱极限非零，但它们的零阶配对等于 $-1/2$；与 (5.4) 的每一项零阶配对均为零并不矛盾，因为两个分量都只有弱收敛。展开平方距离可得

$$
\left\|f_k-\frac1{\sqrt2}1\right\|\longrightarrow\frac1{\sqrt2},
\qquad
\left\|v_k+\frac1{\sqrt2}1\right\|\longrightarrow\frac1{\sqrt2}.
\tag{5.7}
$$

因此没有强收敛子列。本例是在本算子上、每步有越来越多**精确**零矩的非退化双弱极限，具体实现了 R15 所警示的断点；仍不能传递为全部矩消失的真正向量对。

## 6. 继续研究的精确问题

多位尾函数可以有比 (4.6) 更多的自由度。要继续这个构造，必须证明一族精确匹配向量具有足够的强紧性，或直接构造非零极限并控制全部矩；仅凭有限层解存在或两个单位化分量的非零弱极限不够。下一项可计算问题是：固定 $h=1$，在越来越深的有限柱函数空间中，非平凡平方矩匹配是否必有范数逃逸，或能否通过多位纠缠保留一个强极限。该有限柱限制下的答案也不能自动扩张到一般 $h,g\in L^2$。

有限柱函数空间中的完整分类与精确最小范数现已证明，见 [R27](R27-finite-prefix-moment-classification.md)。一般 $L^2$ 向量的缺口仍保留。
