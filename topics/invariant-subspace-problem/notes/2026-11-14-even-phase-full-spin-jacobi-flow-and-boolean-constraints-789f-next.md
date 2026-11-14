# 偶相位的完整 spin–Jacobi 流与必须保留的 Boolean 约束

本稿给任意偶位数、任意正权沿对数射线的完整非微扰相位表示。中央层是块 Jacobi 矩阵的指数；相邻 \(m=-1\) 层具有相关的非零同 spin 对角，不能从中央矩阵删掉首行后直接代替。全部高 spin 先进入完整指数，再取真实硬源 Schur。

这里证明精确身份和实际序列约束，不声称一般相位常数已经支付。特别地，不能把所列 Jacobi 块当作可任意选择的矩阵。

## 1. 原物理空间及归一的全部 spin 层

取 \(2s\) 位 Boolean Hilbert 空间，标准子集基正交归一，记
\[
d=\sum_iE_i,\qquad e=d^*,\qquad
H=[d,e]=2sI-2N.
\]
磁层记号为 \(m=N-s\)。因此中央层为 \(m=0\)，临界低源所在层为 \(m=-1\)。

对 \(0\le j\le s\)，令
\[
\mathcal K_j=\ker d\cap\mathcal H_{s-j}.
\]
这是 spin \(j\) 的 multiplicity 空间，其最低磁数为 \(-j\)。在 \(|m|\le j\) 时，定义
\[
I_{j,m}f
=\frac{e^{j+m}f}{\nu_{j,m}},\qquad
\nu_{j,m}^2=\frac{(j+m)!(2j)!}{(j-m)!}. \tag{1.1}
\]
由原 commutator 反复求范数，\(I_{j,m}\) 是等距映射。标准有限 ladder 分解给
\[
\mathcal H_{s+m}
=\bigoplus_{j\ge|m|}I_{j,m}\mathcal K_j. \tag{1.2}
\]
所有后续压缩使用这个固定的物理酉坐标，而非随权变化的基。

给任意实数列 \(\xi=(\xi_i)\)，定义原占据中心化算子
\[
X(\xi)=\sum_i\xi_i(n_i-\tfrac12I),\qquad
d_\xi=\sum_i\xi_iE_i,\qquad e_\xi=d_\xi^*.
\]
记其在磁层 \(m\) 上、通过 (1.2) 写出的完整矩阵为 \(X_m(\xi)\)。

## 2. 真正的 primitive 块与三塔分解

定义
\[
A_j(\xi)=P_{\mathcal K_j}X(\xi)|_{\mathcal K_j},
\qquad
R_j(\xi)=d_\xi|_{\mathcal K_j}:
\mathcal K_j\longrightarrow\mathcal K_{j+1}. \tag{2.1}
\]
\(A_j(\xi)\) 自伴；\(R_s=0\)。\(R_j\) 确落在 primitive，因为
\(d d_\xi=d_\xi d\)。

原局部关系为
\[
[d,X(\xi)]=d_\xi,\qquad
[X(\xi),e]=e_\xi,\qquad
[d,e_\xi]=-2X(\xi),
\]
\[
[d,d_\xi]=0,\qquad [e,e_\xi]=0. \tag{2.2}
\]
对 \(f\in\mathcal K_j\)，先由 \(d^2Xf=0\) 得
\[
Xf=A_jf+\frac{eR_jf}{2(j+1)}. \tag{2.3}
\]
若 \(j\ge1\)，再由 \(d^3e_\xi f=0\) 和 (2.2) 得完整正交三塔
\[
\boxed{
e_\xi f
=R_{j-1}^*f
-\frac1j eA_jf
-\frac{1}{2(j+1)(2j+1)}e^2R_jf.
} \tag{2.4}
\]
第一项落在 \(\mathcal K_{j-1}\)，后两项分别是 spin \(j,j+1\) 的相应 ladder 层，故彼此物理正交。第一项为 \(R_{j-1}^*\) 是由原伴随直接确定的。

当 \(j=0\) 时，\(A_0=0\)，(2.4) 应读取为
\[
e_\xi f=-\tfrac12e^2R_0f.
\]
没有除以零，也没有虚构负 spin 源。

## 3. 全部磁层的精确块 Jacobi 系数

因为
\[
X e^kf=e^kXf+k e^{k-1}e_\xi f,
\]
将 (2.3)–(2.4) 代入 \(k=j+m\)，再用 (1.1) 归一，得到：

* 同 spin 对角块为
  \[
  \boxed{(X_m)_{j,j}=-\frac mj A_j(\xi)\quad(j\ge1).} \tag{3.1}
  \]
* 从 spin \(j\) 到 spin \(j+1\) 的块为
  \[
  \boxed{
  (X_m)_{j+1,j}
  =
  \sqrt{\frac{(j+1)^2-m^2}{2(j+1)(2j+1)}}\,R_j(\xi).
  } \tag{3.2}
  \]
* 下降块为该式的真实伴随；除此之外所有块为零。

在中央 \(m=0\) 层，所有同 spin 对角严格为零，而
\[
\boxed{
(X_0)_{j+1,j}
=\sqrt{\frac{j+1}{2(2j+1)}}\,R_j.
} \tag{3.3}
\]
所以 \(X_0\) 是真正的自伴块 Jacobi 矩阵。

在相邻 \(m=-1\) 层，
\[
\boxed{(X_{-1})_{j,j}=A_j/j,\qquad j\ge1,} \tag{3.4}
\]
\[
\boxed{
(X_{-1})_{j+1,j}
=\sqrt{\frac{j(j+2)}{2(j+1)(2j+1)}}\,R_j.
} \tag{3.5}
\]
上升块相对于中央块乘
\(\sqrt{1-(j+1)^{-2}}\)，但 (3.4) 一般非零，不能遗漏。
例如 \(\xi_i=a\) 全相同，中央 \(X_0=0\)，而
\(X_{-1}=-aI\)；仅靠中央非对角块显然不能恢复相邻层。

本节不调用外部 Wigner–Eckart 定理，所有系数已经由原 \(d,e\) 三塔推导。

## 4. 完整指数给实际非微扰相位

这里使用[完整中央回归与真实源度量](2026-11-14-central-partition-full-hessian-frame-and-phase-ward-block-789f-next.md)中的同源 h/ell/g/q 定义；顶逆的完整补集身份见[主 spin 稿 §3](2026-11-14-arbitrarily-many-weight-dominant-spin-phase-bound-789f-next.md)。

给任意实 \(\xi\)，可通过共同权缩放先取
\(\sum_i\xi_i=0\)，令平方权
\[
z_i(t)=e^{t\xi_i}.
\]
此时 \(\pi=\prod_i z_i=1\)，且在各磁层，物理对角权就是
\(\exp(tX_m(\xi))\)。

记
\[
W(t)=\exp(-tX_0).
\]
先在完整中央层求这个指数，包括所有 \(j\ge2\) 的真实块。然后取其 spin \(0,1\) 块
\[
M=W_{00},\qquad C=W_{01},\qquad Q=W_{11},
\]
并定义
\[
\boxed{S=Q-C^*M^{-1}C>0.} \tag{4.1}
\]
在固定 unweighted 低源 \(\mathcal K_1\) 上，实际四个二次型准确为
\[
\boxed{
h=(e^{-tX_{-1}})_{11},\qquad
\ell=(e^{tX_{-1}})_{11},\qquad
g=\tfrac12S,\qquad q=2Q.
} \tag{4.2}
\]

说明如下。由 (1.1)，从最低 spin \(1\) 源到中央 raised 源的映射为
\(e|_{\mathcal K_1}=\sqrt2\,I_{1,0}\)。因此其完整中央 Gram 是
\(q=2Q\)。实际去权硬源由 spin \(0\) 的整个 \(\mathcal K_0\) 给出，完整硬源回归为
\[
4g=2(Q-C^*M^{-1}C).
\]
两侧 \(h,\ell\) 分别是完整原源度量与真实顶 MP Gram；\(\pi=1\) 时它们恰为
\(m=-1\) 层的两个相反指数压缩。这证明 (4.2)。

实际相位交叉因此化为
\[
\boxed{
J=h g^{-1}\ell+2g-q
=2hS^{-1}\ell-Q-C^*M^{-1}C.
} \tag{4.3}
\]
完整目标仍有固定的非交换方向：
\[
\boxed{
\Phi\preceq\kappa I
\iff J^*\ell^{-1}J\preceq\kappa h
\iff
\begin{pmatrix}\kappa h&J^*\\J&\ell\end{pmatrix}\succeq0.
} \tag{4.4}
\]

必须先对完整 \(X_0,X_{-1}\) 取指数，再压缩；把它们截成前两 spin 后取指数会删掉真实高 spin 的贡献。式 (4.1) 只短路整个实际硬源，而不是把其它层误认成额外 nuisance。

在一个 reducing 模块若没有 spin \(0\)，则相应 \(M,C\) 为空，(4.1) 按
\(S=Q\) 读取；这与已经支付的空硬源主 spin 边界一致。

中央链的奇偶酉 \(\operatorname{diag}((-1)^jI)\) 把 \(X_0\) 变成 \(-X_0\)，所以
\(M,Q,S\) 随 \(t\) 为偶，\(C\) 为奇；而 \(h(-t)=\ell(t)\)，(4.3) 给
\(J(-t)=J(t)^*\)。这是整个非微扰源的精确关系。

## 5. Jacobi 块不是任意矩阵：实际 Boolean 约束

从任意抽象自伴块 Jacobi 矩阵出发不能自动套用 (4.4)。这里至少有以下原物理约束，而且全部来自同一占据系。

### 5.1 所有轴向权方向严格交换

对任意实 \(\xi,\eta\)，原占据投影两两交换，所以每个磁层上
\[
\boxed{[X_m(\xi),X_m(\eta)]=0.} \tag{5.1}
\]
此外
\[
R_{j+1}(\xi)R_j(\eta)
=R_{j+1}(\eta)R_j(\xi)
\]
由 \(d_\xi d_\eta=d_\eta d_\xi\) 直接成立。
(3.1)–(3.2) 中的所有 \(A_j,R_j\) 都线性依赖同一个 \(\xi\)，不是为每个磁层分别选择。

### 5.2 全部三塔范数给一个二次递推约束

原硬核局部身份为
\[
[d_\xi,e_\xi]=-2X(\xi^2),\qquad
\xi^2=(\xi_i^2)_i.
\]
注意 \(X(\xi^2)=\sum_i\xi_i^2(n_i-\tfrac12I)\)，即使
\(\sum_i\xi_i=0\)，也不能删去其中心化常数。

对 \(\mathcal K_j\) 的真实源，使用 (2.4) 的三项物理正交及 ladder 范数，得到
\[
P_{\mathcal K_j}e_\xi^*e_\xi|_{\mathcal K_j}
=
R_{j-1}R_{j-1}^*
+\frac2j A_j(\xi)^2
+\frac{R_j^*R_j}{(j+1)(2j+1)}.
\]
减去 \(d_\xi^*d_\xi=R_j^*R_j\)，恰得
\[
\boxed{
R_{j-1}R_{j-1}^*
+\frac2jA_j(\xi)^2
-\frac{j(2j+3)}{(j+1)(2j+1)}R_j^*R_j
=-2A_j(\xi^2),\qquad j\ge1.
} \tag{5.2}
\]
这保留了同 spin 对角、上下两个真实桥以及平方权方向的共同来源。不能只保中央 \(R_j\) 而任意补一个 \(A_j\)。

### 5.3 仍待支付的同一共同差

式 (4.3) 的两个可能很大项
\[
2hS^{-1}\ell,\qquad Q+C^*M^{-1}C
\]
必须作为同一个实际差控制。分别估计其范数不提供统一相位常数。
本稿没有由 (5.1)–(5.2) 或普通指数正性推断它已经有界。

因此新的非微扰问题是：对由真实共同 \(n_i\) 产生的全部
\(A_j(\xi),R_j(\xi)\)，能否在完整指数和首硬源 Schur 中证明 (4.4) 的某个统一有限
\(\kappa\)。这是原相位的完整重建，不是只检查零权附近的二阶项。

