# 真实上角进位不能仅以“小”处理：精确图核反例

日期：2026-11-12（UTC）。独占稿：critical_kernel。
状态：**已证明的通用迁移障碍。** 执行器重置后重建。本例不是本题固定 dyadic 系数模型的反例。

## 1. 构造及全部局部条件

取非零单射有界拟幂零 K，例如本仓库实际 A。令 J=tK，
t>0 足够小使 0<∥J∥<1/2，并记

$$
\eta=\|J^2\|>0,\qquad N=J^2/\eta.
$$

N 单射、拟幂零、范数为 1，η→0。在 H⊕H 上设

$$
M=\begin{pmatrix}0&\eta N\\I&0\end{pmatrix}
=\begin{pmatrix}0&J^2\\I&0\end{pmatrix},
\qquad
E=\begin{pmatrix}0&0\\I&0\end{pmatrix}.
$$

则 M 单射、拟幂零，且

$$
M^2=\eta\,\operatorname{diag}(N,N),\qquad
\|M\|=1,\qquad \|M-E\|=\eta.
\tag{1}
$$

固定 a≠0，令 C=aJ(I−J)^{-1} 在两分量上对角作用，
并设

$$
Y=M(I+M)^{-1},\qquad S=aY+C.
$$

C 与 J、N、M 交换，而且

$$
\|C\|/|a|\le\|J\|/(1-\|J\|)\longrightarrow0.
\tag{2}
$$

## 2. 核恰为整个尾空间参数的闭图

定义

$$
\mathcal G_-=\{(-Jy,y):y\in H\}.
$$

M 在此图上对应 −J，所以 Y 对应 −J(I−J)^{-1}，从而
S 在图上恒零。

事实上，记 \widehat J=diag(J,J)，有

$$
S=a(I-\widehat J)^{-1}
(M+\widehat J)(I+M)^{-1},
$$

$$
M+\widehat J
=\begin{pmatrix}J&J^2\\I&J\end{pmatrix}
=\begin{pmatrix}J\\I\end{pmatrix}\begin{pmatrix}I&J\end{pmatrix}.
$$

后者核恰为 𝒢_-。I+M 在图上对应 I−J，故保持该图且在其上可逆。因此

$$
\boxed{\ker S=\mathcal G_-\ne\{0\}.}
\tag{3}
$$

图参数映射 y↦(−Jy,y) 有界，其逆为第二分量投影，故这是实际闭核。

## 3. 精确 Schur 对照

对应真实一位图的 Schur 多项式为

$$
C^2-\eta N(C+aI)^2.
$$

由于 ηN=J²、C+aI=a(I−J)^{-1}，它恒等于零，解释了 (3)。

删去进位的纯局部算子 aE+C 却单射：方程
(Cx,ax+Cy)=0 中，C 单射先给 x=0，再给 y=0。

所以任意小的真实上角进位，可以把一个单射纯局部算子变成有完整图核的算子。这是明确的零点核投影不连续性，而非仅抽象警告。

## 4. 准确的障碍范围

本例同时满足：η 任意小；N 单射拟幂零且范数1；M 单射拟幂零并满足 (1)；尾范数比 (2) 任意小；相关尾算子互相交换。因此仅依赖这些小量和交换性，不足以把纯 birth-death 核递推转为真实模型。

但这里 C 被选为 J 的有理函数，尚未实现为本题规定的
C=∑_{\ell>j}a_\ell N_\ell(I+N_\ell)^{-1}，且 N 未固定为真实归一化幂 N_{j+1}。本例不否定该特殊模型的单射性；其迁移证明必须额外利用真实 dyadic 相干关系或更强的近零谱估计。

参见
[纯尾 birth-death 定理](2026-11-12-pure-tail-dominance-birth-death-kernel-0c-agent.md)。
