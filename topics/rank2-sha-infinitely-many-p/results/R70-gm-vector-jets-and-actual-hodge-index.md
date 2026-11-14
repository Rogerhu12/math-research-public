# R70. 固定 GM 向量 jet 与真实 Hodge 格指数

日期：2026-11-12。**状态：向量前缀比较、稀疏源 Smith 指数和固定周期首坏项已证明。**

使用 R68 的行约定 $\Phi(e^\phi)=F_pe$，令
$D=\operatorname{diag}(p^{-1},1)$、$N_p=DF_p$。
实际整 Frobenius 给
$$
N_p\in\operatorname{GL}_2(\mathbb Z_p[[t]]),\qquad
\det N_p=\frac{1-4t^2}{1-4t^{2p}}.
$$
但其整同构的源是
$\widetilde H^\phi=\mathbb Z_p[[t]]p^{-1}\omega^\phi\oplus
\mathbb Z_p[[t]]\eta^\phi$，而不是原始 $H^\phi$。
次数 $0,\ldots,k$ 的完整源 jet 格指数为 $k+1$。

## 1. 真正稀疏拉回的指数

若源是明确的 sections $t^j\omega,t^j\eta$，
$0\le j\le q=\lfloor k/p\rfloor$，则实际 $\phi$ 拉回只出现在次数 $pj$。
设 $E_{p,k}$ 为该原始稀疏插入，$T_k$ 为块下三角 Toeplitz 矩阵。
准确评价矩阵是
$$
T_k(N_p^t)E_{p,k}\operatorname{diag}(p,1,\ldots,p,1).
$$
前两个因子给原始嵌入，所以非零 Smith 指数准确为
$q+1$ 个 1 和 $q+1$ 个 0。输出再乘实际 $M_1=t^4v$、$v$ 整单位时，
相应指数为
$$
\max\left(0,\left\lfloor\frac{k-4}{p}\right\rfloor+1\right).
$$
这与拉回 $M_1$ 本身而产生四倍 $p$ 阶零点是不同映射。

一般整可逆矩阵 $N(t)$ 的 $T_k(N)$ 也整可逆。因此同一源格上的
**完整向量前缀**若只差这一变换，则其行格、所有阶 minors 理想和
饱和核均不变。此结论不自动适用于一个标量分量或任意改换后的 section space。

## 2. 固定周期的首坏方向

令 $Y=(K,L;K',L')$、$N_0=DF_p(0)$。水平恒等式准确重排为
$$
Y=N_p^{-1}\begin{pmatrix}
K(t^p)&p^{-1}L(t^p)\\pK'(t^p)&L'(t^p)
\end{pmatrix}N_0.
$$
中间矩阵的首坏系数为 $p^{-1}E_{12}t^p$，从而
$$
p[t^p]Y\equiv N_0^{-1}E_{12}N_0\ne0\pmod p,
\qquad [t^n]Y\text{ 整 }(n<p).
$$
乘实际 $M_1$ 后首坏次数准确为 $p+4$。
惰性时该方向在 $K'$，单个 $M_1K$ 的首坏次数则为 $p+5$。

右端初值的 $p$ 因子只补偿行列式线。共轭 $DY^\phi D^{-1}$ 在
$\operatorname{End}(H)$ 的四方向权为 $(0,-1,+1,0)$；总和零不消去负权。
因此不能将源 Hodge 指数与初值的 $p$ 未经计算地相减。

R68 的临界标量代表首坏推迟到 $2p+4$ 仍完全成立；但它含比例、
$p$ 次幂差及 Euler 逆，尚未与上述固定向量格作同源整比较。
下一问题是该指定非线性评价的实际张量或商格的饱和指数。
全文见 [GM 束 jet 格及 Hodge 指数](../notes/2026-11-12-gm-bundle-jet-lattices-and-hodge-index.md)。
