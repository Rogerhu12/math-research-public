# 原平衡 star 概率不支付任意端点来源：一个全规模精确障碍

日期：2026-11-14；工作标识：Astra-ISP-789f。

## 1. 要排除的扩大与实际结论

[真实平衡 star](2026-11-14-balanced-star-full-source-beta-binomial-phase-transport-789f-next.md)的低源来自全部线性占据观察 \(X_i=K_i/q_i\)。[两个真实可逆生成元](2026-11-14-balanced-star-reversible-mixed-generator-bound-789f-next.md)以及端点 star 图的自伴结构可以在更大的函数空间定义，但这不意味着相位估计可以免费扩到那个空间。

这里保留**原物理概率本身**，甚至取最简单的所有 \(q_i=z_i=1\)，只把观察向量改为两个非线性端点函数。新观察仍逐坐标位于 \([0,1]\)，在空状态均为 0、在满状态均为 1，并且关于包含关系单调。其完整协方差、两侧 Dirichlet Gram 与均值项均明确正定、无遗漏。

然而若对这些新来源要求同形不等式

\[
\widetilde J^*\widetilde L^{-1}\widetilde J
\preceq\kappa\widetilde H,
\qquad
\widetilde J=\widetilde H\widetilde G^{-1}\widetilde L
-2\widetilde G-\widetilde y\widetilde y^*,
\tag{1.1}
\]

则对每个 \(Q\ge16\) 必须有

\[
\boxed{\kappa\ge\frac{Q(Q+1)}{4(1+\log Q)}.} \tag{1.2}
\]

因此同一概率、端点条件、单调性及两个 star 图结构都不足以单独给出统一有限 \(\kappa\)。**这不是原线性占据相位的反例**：原全等权的真实相位为恒等，原来源空间必须保留。

## 2. 原概率与两个新观察

取 \(Q\ge2\) 个小位，主组长度也为 \(Q\)，全部物理权为 1。原子集分布是

\[
\mathbb P(I)=\frac1{(Q+1)\binom Q{|I|}},
\qquad I\subset[Q].
\tag{2.1}
\]

所以 \(S=|I|\) 在 \(0,\ldots,Q\) 上均匀；给定 \(S=s\) 后子集仍按原均匀条件分布取值。设

\[
p=\frac1{Q+1},\qquad
\widetilde X_1=\mathbf1_{\{S=Q\}},\qquad
\widetilde X_2=1-\mathbf1_{\{S=0\}}.
\tag{2.2}
\]

\(\widetilde X_1\) 是全部位占据的乘积，\(\widetilde X_2\) 是至少一位占据的指示。它们不是原 \(X_i\) 的仿射线性组合。例如，若 \(\mathbf1_{\{S=Q\}}=c+\sum_i a_iX_i\)，在空集得到 \(c=0\)，在所有单点得到 \(a_i=0\)，再在满集矛盾。第二个函数在空集给 \(c=0\)、单点给所有 \(a_i=1\)，在双点就矛盾。

仍采用原真实后验权

\[
a_s=\frac{Q-s+1}{s}\quad(s\ge1),\qquad
b_s=\frac{s+1}{Q-s}\quad(s\le Q-1).
\tag{2.3}
\]

在 \(S=0\) 把 \(a_S\widetilde X\) 整列取零，在 \(S=Q\) 把 \(b_S(\mathbf1-\widetilde X)\) 整列取零。定义

\[
\begin{aligned}
\widetilde m&=\mathbb E\widetilde X,&
\widetilde y&=2\widetilde m-\mathbf1,\\
\widetilde G&=\operatorname{Cov}(\widetilde X),&
\widetilde H&=\mathbb E[a_S\widetilde X\widetilde X^*],\\
&&\widetilde L&=\mathbb E[b_S(\mathbf1-\widetilde X)
                         (\mathbf1-\widetilde X)^*].
\end{aligned}\tag{2.4}
\]

这些式子始终在同一个完整概率空间和同一个二维来源中取值；下面不忽略任何非对角项。

## 3. 三个完整矩阵的精确值

记调和数 \(\mathcal H_Q=\sum_{s=1}^Q1/s\)，并置

\[
h=\frac1{Q(Q+1)},\qquad
t=\mathcal H_Q-\frac Q{Q+1}.
\tag{3.1}
\]

均值、协方差和均值偏移为

\[
\widetilde m=(p,1-p)^\mathsf T,
\quad
\widetilde G=p^2
\begin{pmatrix}Q&1\\1&Q\end{pmatrix},
\quad
\widetilde y=\frac{Q-1}{Q+1}
\begin{pmatrix}-1\\1\end{pmatrix}.
\tag{3.2}
\]

确实，两个方差都是 \(p(1-p)=Qp^2\)，而
\(\mathbb E[\widetilde X_1\widetilde X_2]=p\)，故协方差是 \(p^2\)。

另一方面，\(\widetilde X_1\) 仅在满状态非零，且 \(a_Q=1/Q\)。因此 \(\widetilde H_{11}=\widetilde H_{12}=h\)。第二个观察在全部非空状态等于 1，所以

\[
\widetilde H_{22}
=\frac1{Q+1}\sum_{s=1}^Q\frac{Q+1-s}{s}
=\mathcal H_Q-\frac Q{Q+1}=t.
\]

由原概率的互补对称性，得到全部矩阵

\[
\boxed{
\widetilde H=\begin{pmatrix}h&h\\h&t\end{pmatrix},
\qquad
\widetilde L=\begin{pmatrix}t&h\\h&h\end{pmatrix}.}
\tag{3.3}
\]

\(h>0\)、\(t-h>0\)，故二者严格正定。\(\widetilde G\) 的特征值为 \(p^2(Q\pm1)>0\)。不存在退化源、未定义逆或只验证单个压缩的问题。

## 4. 一个对角配对已经强制常数发散

由

\[
\widetilde G^{-1}\begin{pmatrix}1\\1\end{pmatrix}
=(Q+1)\begin{pmatrix}1\\1\end{pmatrix}
\]

及 \(h(Q+1)=1/Q\)，直接计算得

\[
(\widetilde H\widetilde G^{-1}\widetilde L)_{11}
=\frac{t+h}{Q}.
\]

又有

\[
2\widetilde G_{11}+\widetilde y_1^2
=\frac{2Q+(Q-1)^2}{(Q+1)^2}
=\frac{Q^2+1}{(Q+1)^2}.
\]

因此

\[
\boxed{
\widetilde J_{11}
=\frac{t+h}{Q}-\frac{Q^2+1}{(Q+1)^2}.}
\tag{4.1}
\]

特别 \(t+h=\mathcal H_Q-1+1/Q\)，故 \(\widetilde J_{11}\to-1\)。

假设 (1.1) 成立，对同一个 \(e_1\) 作 \(\widetilde L\) 度量的 Cauchy–Schwarz，则

\[
|e_1^*\widetilde J e_1|^2
\le(e_1^*\widetilde L e_1)
   (e_1^*\widetilde J^*\widetilde L^{-1}\widetilde J e_1)
\le\kappa\widetilde L_{11}\widetilde H_{11}
=\kappa ht.
\tag{4.2}
\]

这一步保留原目标的 \(H,L\) 次序，并未把非交换矩阵换序。

对 \(Q\ge16\)，有

\[
\mathcal H_Q\le1+\log Q\le Q/4,
\qquad
\frac{Q^2+1}{(Q+1)^2}\ge\frac34.
\]

第一条的后一不等式在 16 成立，且 \(Q/4-1-\log Q\) 在此后递增；第二条等价于 \(Q^2-6Q+1\ge0\)。由 (4.1)，

\[
\widetilde J_{11}\le\frac14-\frac34=-\frac12,
\qquad
ht\le\frac{1+\log Q}{Q(Q+1)}.
\]

代入 (4.2) 即得 (1.2)。更准确的必要常数是

\[
\kappa\ge
\frac{\left((t+h)/Q-(Q^2+1)/(Q+1)^2\right)^2}{ht}
\sim\frac{Q^2}{\log Q}.
\tag{4.3}
\]

这是所有 \(Q\) 的解析公式与严格发散结论，不是有限数值扫描。

## 5. 两个 star 图及后续证明的适用边界

把所有非空状态以速率 \(a_S\) 连到空状态，再按详细平衡定义反向速率，得到一个真实可逆 star 图 Laplacian \(A_0\)。把所有非满状态以速率 \(b_S\) 连到满状态，得到 \(A_Q\)。

由于 \(\widetilde X(0)=0\)、\(\widetilde X(Q)=\mathbf1\)，其完整 Dirichlet 压缩正是 (2.4) 的 \(\widetilde H,\widetilde L\)。因此本例没有破坏这两个完整正算子的来源，也没有改变原 \(\pi\) 或其端点概率。

实际原低源另有不可省略的条件：它由位占据的**一次函数**生成，不能换成上述高次数的端点指示。即使把常数先剔除，中心化的两个端点函数仍在完整均值零空间中，所以“先推广到全部均值零函数，再压回原低源”的统一相位证明也不能成立。

这个障碍只关闭所述扩大来源的捷径。原全等权的线性占据模块相位仍为恒等；一般正权的真正线性来源、共同回归残差、统一 \(\kappa\) 及普通 ISP 均保持原开放状态。
