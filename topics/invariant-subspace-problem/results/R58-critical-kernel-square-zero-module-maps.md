# R58：假设临界核向量的闭模映射必平方为零：谱二择与循环向量的平移稳定性

日期：2026-11-12（UTC）。会话：Astra-ISP-0c017065。子任务：critical_kernel。

**状态：已证明的条件结构定理。** 若原临界核 $K=\ker D$ 非零，则由其中任意向量及任意循环参考向量生成的闭模映射，必在其定义域上平方为零。该算子要么全域有界、非零且不属于 UHF 代数，要么预解集为空、谱为整个复平面。与此同时，沿 $K$ 平移保持 $A$ 的循环向量集合。本条本身没有构造非零核向量，也没有排除这两种分支。随后 R60 已独立证明原临界核为零，故这里对原候选的非零核前提不成立；保留本条作为闭模映射的条件结构工具，不解决完整 Hilbert 不变子空间问题。

依赖：R24 的双线性对称性，R34 的闭模映射框架，R53 的全等向性及 $K\subset\overline{\operatorname{Ran}D}$，R38 的 UHF 相对交换子识别，R32 的解析代数无零因子。以下重新证明全部闭包、定义域、谱及循环性步骤。

## 1. 所需的具体模型事实

仍令 $A$ 为本课题的 Haar 表示加权 odometer，
$$
H=L^2(\mathbb Z_2,\mu),\qquad
(Af)(y)=w(y)f(y-1),
$$
并沿用原临界
$$
Q=\prod_{j\ge0}(I+r_jN_j)(I+N_j)^{-1},\qquad
D=I-Q,\qquad K=\ker D.
$$
记
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\qquad
\mathcal C=C^*(I,A).
$$
有 $D\in\mathcal A$。R24 的共轭及双线性型为
$$
Cg(y)=\overline{g(-1-y)},\qquad
B(u,v)=\langle u,Cv\rangle.
$$
$B$ 连续、对称、非退化；$A$ 和 $D$ 对 $B$ 对称。

R53 证明
$$
B(K,K)=0,\qquad K\subseteq\overline{\operatorname{Ran}D}.
\tag{1.1}
$$
第二项的来源是
$$
(\overline{\operatorname{Ran}D})^\perp
=\ker D^*=CK,
$$
而全等向性等价于 $K\perp CK$。本条使用的是实际值域的闭包，绝不把 (1.1) 改写为尚未证明的 $K\subseteq\operatorname{Ran}D$。

$K$ 是闭的 $A$ 不变子空间，因为 $AD=DA$。

## 2. 对任意循环参考向量定义闭模映射

固定一个对 $A$ 循环的向量 $h$，以及任意 $f\in K$。定义
$$
\mathcal D_0=\{p(A)h:p\in\mathbb C[z]\},
$$
$$
X_0\bigl(p(A)h\bigr)=p(A)f.
\tag{2.1}
$$
$\mathcal D_0$ 在 $H$ 中稠密。

该映射定义良好：若 $p(A)h=0$，则与 $A$ 交换的 $p(A)$ 杀死 $h$ 的全部多项式轨道，所以由循环性 $p(A)=0$，进而 $p(A)f=0$。

在核心上有
$$
B\bigl(X_0p(A)h,q(A)h\bigr)
=B\bigl(p(A)h,X_0q(A)h\bigr).
\tag{2.2}
$$
确实，两边都等于 $B(f,p(A)q(A)h)$。

**引理 2.1。** $X_0$ 可闭。

**证明。** 若 $p_n(A)h\to0$、$p_n(A)f\to u$，则对每个多项式 $q$，
$$
\begin{aligned}
B(u,q(A)h)
&=\lim_n B(p_n(A)f,q(A)h)\\
&=\lim_n B(p_n(A)h,q(A)f)=0.
\end{aligned}
$$
$h$ 循环且 $B$ 非退化，故 $u=0$。证毕。

以下记
$$
X=\overline{X_0}.
\tag{2.3}
$$
它是闭、稠密定义算子，$\mathcal D_0$ 是其图范数核心，并且 $h\in\operatorname{Dom}X$、$Xh=f$。

## 3. 闭包的值域及定义域不变性

由 $p(A)f\in K$ 和 $K$ 闭，
$$
\boxed{\operatorname{Ran}X\subseteq K.}
\tag{3.1}
$$

对任意 $u\in\operatorname{Dom}X$，取 $p_n(A)h\to u$、$p_n(A)f\to Xu$。对这两个极限同时施加有界算子 $A$，再用闭图，得到
$$
A\operatorname{Dom}X\subseteq\operatorname{Dom}X,\qquad
XAu=AXu.
\tag{3.2}
$$
同理，对每个多项式成立该关系。

若 $S\in\mathcal A$，选多项式 $q_m(A)\to S$ 于算子范数。对固定 $u\in\operatorname{Dom}X$，
$$
q_m(A)u\to Su,\qquad
Xq_m(A)u=q_m(A)Xu\to SXu.
$$
$X$ 闭，故
$$
\boxed{
S\operatorname{Dom}X\subseteq\operatorname{Dom}X,\qquad
XSu=SXu
\quad(S\in\mathcal A,\ u\in\operatorname{Dom}X).
}
\tag{3.3}
$$
这是带有定义域的交换关系，不是将无界算子乘法视为处处有定义的恒等式。

特别取 $S=D$。由 (3.1)，$DXu=0$，因而
$$
D\operatorname{Dom}X\subseteq\operatorname{Dom}X,\qquad
XDu=DXu=0
\quad(u\in\operatorname{Dom}X).
\tag{3.4}
$$

## 4. 核的闭包包含关系及真正的平方零性质

闭算子的核是 $H$ 中闭子空间：若 $u_n\in\operatorname{Dom}X$、$Xu_n=0$ 且 $u_n\to u$，则闭图给 $u\in\operatorname{Dom}X$、$Xu=0$。

由于 $\operatorname{Dom}X$ 稠密，$D$ 有界，
$$
\overline{D\operatorname{Dom}X}
=\overline{\operatorname{Ran}D}.
$$
将 (3.4) 取闭包，得到
$$
\boxed{\overline{\operatorname{Ran}D}\subseteq\ker X.}
\tag{4.1}
$$
这里 $\ker X$ 的定义包括定义域条件，所以 (4.1) 同时断言整个闭子空间 $\overline{\operatorname{Ran}D}$ 已属于 $\operatorname{Dom}X$。

结合 (1.1)、(3.1) 和 (4.1)，
$$
\boxed{
\operatorname{Ran}X
\subseteq K
\subseteq\overline{\operatorname{Ran}D}
\subseteq\ker X.
}
\tag{4.2}
$$
于是
$$
\boxed{
X(\operatorname{Dom}X)\subseteq\operatorname{Dom}X,\qquad
X^2u=0\quad(u\in\operatorname{Dom}X).
}
\tag{4.3}
$$
换言之，$X^2$ 的定义域恰为 $\operatorname{Dom}X$，它在那里为零。若 $X$ 无界，则不能把这个定义域上的零算子等同于 $H$ 上的全域有界零算子；(4.3) 没有宣称 $\operatorname{Dom}X=H$。

该论证适用于任意循环 $h$，不只适用于 $h=1$。

## 5. 闭稠密定义平方零算子的谱二择

以下先作一般引理。

**引理 5.1。** 设 $X$ 是 Hilbert 空间上的闭、稠密定义算子，满足 (4.3)。对每个 $\lambda\ne0$，
$$
\boxed{
\operatorname{Ran}(\lambda I-X)=\operatorname{Dom}X,
\qquad
\ker(\lambda I-X)=\{0\}.
}
\tag{5.1}
$$
其在 $\operatorname{Dom}X$ 上的代数逆为
$$
\boxed{
(\lambda I-X)^{-1}v
=\lambda^{-1}v+\lambda^{-2}Xv
\quad(v\in\operatorname{Dom}X).
}
\tag{5.2}
$$

**证明。** 若 $u\in\operatorname{Dom}X$，则 $Xu$ 也在定义域，故 $\lambda u-Xu\in\operatorname{Dom}X$，给出 (5.1) 的值域包含。

反之，若 $v\in\operatorname{Dom}X$，则 $u=\lambda^{-1}v+\lambda^{-2}Xv$ 仍在定义域，而且 $X^2v=0$ 给
$$
(\lambda I-X)u=v.
$$
这证明值域等号。若 $(\lambda I-X)u=0$，则 $Xu=\lambda u$；施加 $X$ 得 $\lambda Xu=0$，从而 $u=0$。逆公式也随之成立。证毕。

现在假设 $f\ne0$，从而 $X\ne0$；由 (4.2)，$f\in\ker X$。

**定理 5.2。** 第 2 节的闭模映射 $X$ 恰有以下两个分支。

- **全域有界分支。** $\operatorname{Dom}X=H$，$X\in B(H)$，$X^2=0$，且
  $$
  \rho(X)=\mathbb C\setminus\{0\},\qquad \sigma(X)=\{0\}.
  \tag{5.3}
  $$
- **无界分支。** $\operatorname{Dom}X\ne H$，并且
  $$
  \boxed{\rho(X)=\varnothing,\qquad \sigma(X)=\mathbb C.}
  \tag{5.4}
  $$
  每个 $\lambda\ne0$ 都是连续谱点：$\lambda I-X$ 单射、值域稠密但不满；$0$ 是点谱点。

**证明。** 全域时闭图定理使 $X$ 有界，(5.2) 为有界逆；而 $\ker X$ 含 $f\ne0$，所以零属于谱。

非全域时，(5.1) 给每个非零参数的值域恰为稠密真子空间 $\operatorname{Dom}X$，故没有非零预解点。零仍有非零核。两种情况穷尽全部可能。证毕。

特别注意，“预解集为空”与“谱为空”正好相反。R39 的某些生成元具有空谱；本条的无界分支具有整个复平面作为谱，没有把两者混淆。

### 5.1 有界分支必在 UHF 之外

若全域有界分支成立，(3.2) 给 $X\in\{A\}'$，且 $X\ne0$、$X^2=0$。R38 证明
$$
\{A\}'\cap\mathcal C=\mathcal A,
$$
R32 证明 $\mathcal A$ 没有零因子。因此
$$
\boxed{X\notin\mathcal C.}
\tag{5.5}
$$
否则 $X\in\mathcal A$ 与 $X^2=0$ 会迫使 $X=0$，矛盾。

这排除的只是有界分支位于具体 UHF 内部的可能。完整交换子严格大于 $\mathcal A$，所以不能据此排除该分支本身。

## 6. 沿临界核平移保持循环性

记 $\operatorname{Cyc}(A)$ 为 $A$ 的全部循环向量。

**定理 6.1。** 对任意 $h\in\operatorname{Cyc}(A)$、$f\in K$ 和 $c\in\mathbb C$，
$$
\boxed{h+cf\in\operatorname{Cyc}(A).}
\tag{6.1}
$$
因而
$$
\boxed{\operatorname{Cyc}(A)+K=\operatorname{Cyc}(A).}
\tag{6.2}
$$
等价地，对任意 $u\in H$、$f\in K$，$u$ 循环当且仅当 $u+f$ 循环。

**证明。** $c=0$ 或 $f=0$ 时直接成立。其余情形使用前面对应 $h,f$ 的闭映射 $X$。

由 (4.3)，$I+cX$ 在 $\operatorname{Dom}X$ 上的逆为 $I-cX$，所以
$$
\operatorname{Ran}(I+cX)=\operatorname{Dom}X,
\tag{6.3}
$$
这是稠密子空间。另一方面，在核心上
$$
(I+cX)p(A)h=p(A)(h+cf).
\tag{6.4}
$$
因为 $\mathcal D_0$ 是 $X$ 的图范数核心，$I+cX$ 关于图范数连续，其核心上的像与全定义域上的像具有相同的 $H$ 范数闭包。故
$$
\begin{aligned}
[h+cf]_A
&=\overline{\{(I+cX)p(A)h:p\in\mathbb C[z]\}}\\
&=\overline{\operatorname{Ran}(I+cX)}
=\overline{\operatorname{Dom}X}=H.
\end{aligned}
$$
这证明 (6.1)。取全部 $h,f$ 得 (6.2)；反向循环性用循环参考向量 $u+f$ 和核向量 $-f$ 再应用 (6.1)。证毕。

尤其，一旦假设存在 $0\ne f\in K$，整条仿射直线 $1+\mathbb C f$ 都由循环向量组成。这个结论与 $f$ 自身非循环并不矛盾，因为该直线并不经过 $f$ 的非零标量倍数。

## 7. 准确的未解点

本条把假设的临界核向量施加了两项新结构约束：

1. 它产生的原始闭模映射已经平方为零，无需为得到平方零而另造一个扩大定义域的算子；谱严格服从第 5 节的二择。
2. 它是循环向量集合的平移方向，第 6 节适用于任意已知循环参考向量。

但这两项约束都不是矛盾。有界分支可以落在完整交换子而在 UHF 之外；无界、稠密定义、平方零、无预解点的闭算子在一般算子论中也并不禁止。还需要利用本模型的实际进位或更强的交换子结构，才能排除任一分支。

没有从“闭模映射可闭”推断它有预解点；没有把 $X^2$ 在非全域定义域上为零，当成全域有界算子恒等式；也没有将本条的条件性结论视为已经构造了非零 $f\in K$。临界核和主课题均继续未解。

