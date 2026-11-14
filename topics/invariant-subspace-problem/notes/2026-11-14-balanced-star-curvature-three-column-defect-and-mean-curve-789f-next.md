# 真实 contrast 曲率：完整 Schur 与至多三列的点态负部

一般 N-log 凹已由[完整有限正权反例](2026-11-14-balanced-star-actual-matrix-curvature-counterexample-789f-next.md)排除。本稿不再要求整个曲率非负，而保留其准确剩余结构：在同一完整 additive contrast 源中，曲率是一个对角压缩加一个明确的二阶块。它给出“PSD 减至多三列平方”的精确分解。全部移动的二阶块来自真实条件均值曲线及其导数；尚未把这点态分解送过原全局回归或积分。

## 1. 同一个完整密度和固定 Lorentz 形式

取 \(Q\ge2\)、全部 \(z_i>0\)。记
\[
L_i(t)=1-t+tz_i,\quad L=\operatorname{diag}(L_i),\quad
F(t)=\prod_iL_i(t),\quad Z=\operatorname{diag}(z_i),\quad0<t<1.
\]
令 \(E:\mathbb C^{Q-1}\to\mathbb C^Q\) 是 \(\mathbf1^\perp\) 的固定等距源嵌入。实际条件 Bernoulli 概率为 \(p_i(t)=tz_i/L_i(t)\)。完整 contrast 密度仍是
\[
\langle M(t)v,v\rangle
=\frac{F(t)}{t(1-t)}\mathbb E_t
\left|\sum_i(Ev)_iX_i\right|^2.
\]
它严格正定。定义固定矩阵
\[
B_0=Z-\frac{z\mathbf1^*+\mathbf1z^*}{2},\qquad
\mathscr G(t)=L^{-1}B_0L^{-1},\qquad T(t)=E^*\mathscr G(t)E.
\]
准确有
\[
\boxed{M(t)=F(t)T(t).} \tag{1.1}
\]
这里 \(\mathscr G\) 是全层 Lorentz 形式，与原平衡 star 的协方差矩阵 \(G=\operatorname{Cov}(X)\) 不同。

证明 (1.1)：若 \(y=L^{-1}Ev\)，则
\[
(1-t)\mathbf1^*y+t z^*y=0.
\]
在这一准确源超平面上，
\[
y^*B_0y=y^*Zy+t(1-t)|(z-\mathbf1)^*y|^2,
\]
这正是原完整条件方差加条件均值平方的表达。

\(B_0\) 在 \(\mathbf1^\perp\) 上正定，而
\(\mathbf1^*B_0\mathbf1=(1-Q)\sum_i z_i<0\)。因此其惯性恰为 \((Q-1,1)\)，无零特征值。也可直接使用
\[
Z^{-1/2}B_0Z^{-1/2}
=I-\frac{ab^*+ba^*}{2},\quad
a=Z^{1/2}\mathbf1,\quad b=Z^{-1/2}\mathbf1,
\]
其两个非平凡特征值是
\[
1-\frac{Q\pm\|a\|\|b\|}{2}.
\]
其中一个严格负，另一个至少为 \(1\)。

## 2. 完整源逆和 normal Schur

以下所有逆都取在已经指明的完整空间。令
\[
N=\mathscr G^{-1}\mathbf1,
\qquad d=\mathbf1^*\mathscr G^{-1}\mathbf1.
\]
由于 \(E^*\mathscr GE=T\succ0\) 且 \(\mathscr G\) 恰有一个负方向，完整 Schur 补给
\[
\boxed{d<0,\qquad
ET^{-1}E^*
=\mathscr G^{-1}-\frac{NN^*}{d}.} \tag{2.1}
\]
特别是右边为非负，核恰为 \(\mathbb C\mathbf1\)。这保留实际 \(E\) 源，绝不是任取一个正面再假设同一逆。

置
\[
\lambda_i=\frac{z_i-1}{L_i},\qquad
\Lambda=\operatorname{diag}(\lambda_i),\qquad
k_2=\sum_i\lambda_i^2.
\]
则
\[
\mathscr G'=-\Lambda\mathscr G-\mathscr G\Lambda,
\]
\[
\mathscr G''=2\Lambda^2\mathscr G+2\mathscr G\Lambda^2
             +2\Lambda\mathscr G\Lambda,
\qquad(\log F)''=-k_2.
\]
令 \(C=[\mathscr G,\Lambda]\)、\(r=E^*\mathscr G'N\)。利用 (2.1) 和逐项乘法，真实曲率
\(\mathcal K_M=M'M^{-1}M'-M''\) 满足
\[
\boxed{
\frac{\mathcal K_M}{F}
=E^*\!\left[k_2\mathscr G-2\Lambda\mathscr G\Lambda
       +C\mathscr G^{-1}C^*\right]E-\frac{rr^*}{d}.
} \tag{2.2}
\]
具体而言，
\[
\mathscr G'\mathscr G^{-1}\mathscr G'-\mathscr G''
=C\mathscr G^{-1}C^*-2\Lambda\mathscr G\Lambda,
\]
而标量 \(F\) 的对数二阶导贡献 \(k_2T\)。最后的 \(-rr^*/d\) 是实际完整 normal Schur 的正项。

## 3. 保原源后二阶块的精确降维

令
\[
x=(z_i/L_i)_i,\quad y=(1/L_i)_i,\quad
D_0=\operatorname{diag}(z_i/L_i^2),\quad
k=\frac{1-t}{t},
\]
\[
u=E^*y,\qquad v=E^*\Lambda y,\qquad U=[u\ v]. \tag{3.1}
\]
有
\[
\mathscr G=D_0-\frac{xy^*+yx^*}{2},
\]
且因为 \(E^*\mathbf1=0\)，
\[
E^*x=-ku,\qquad E^*\Lambda\mathbf1=-u/t,
\qquad E^*\Lambda x=-u/t^2-kv. \tag{3.2}
\]

定义两个完整环境列组成的 \(Q\times2\) 矩阵
\[
A=\left[
k\Lambda y-\frac{\mathbf1}{2t^2} ,\
\frac{\mathbf1}{2t}-ky
\right],
\]
及二维列
\[
w=\binom{2/t}{0}-A^*N.
\]
由交换子的直接展开和 (3.2)，
\[
\boxed{E^*C=UA^*,\qquad r=Uw.} \tag{3.3}
\]
第一式完整地保留了原源的所有交叉；第二式也可由
\(\mathscr G\Lambda N=\Lambda\mathbf1+CN\) 立即得到。

因此，定义明确的自伴 \(2\times2\) 矩阵
\[
R_2=
\begin{pmatrix}k_2k&-t^{-2}\\-t^{-2}&-2k\end{pmatrix}
+A^*\mathscr G^{-1}A-\frac{ww^*}{d}. \tag{3.4}
\]
则 (2.2) 完全化为
\[
\boxed{
\frac{\mathcal K_M(t)}{F(t)}
=E^*\operatorname{diag}\!\left[
\frac{z_i}{L_i^2}(k_2-2\lambda_i^2)
\right]E
+U R_2U^*.
} \tag{3.5}
\]
例如 (3.4) 的第一块来自
\[
E^*(k_2\mathscr G-2\Lambda\mathscr G\Lambda)E
=E^*D_0(k_2I-2\Lambda^2)E
 +k_2k uu^*-t^{-2}(uv^*+vu^*)-2kvv^*.
\]
全部剩余量只使用固定 \(B_0\) 的完整逆、真实 normal Schur 和一个二阶矩阵，不含提前压缩的逆。

## 4. 显式 PSD 减至多三列平方

令
\[
D_{\rm curv}=\operatorname{diag}\!\left[
\frac{z_i}{L_i^2}(k_2-2\lambda_i^2)
\right]=D_+-D_-,
\]
其中 \(D_\pm\) 是逐项正、负部。因为
\(k_2=\sum_i\lambda_i^2\)，不可能有两个不同指标都满足
\(2\lambda_i^2>k_2\)。所以
\[
\operatorname{rank}D_-\le1. \tag{4.1}
\]
对仅有二阶的 \(R_2\)，置
\[
R_{2,\pm}=\frac{|R_2|\pm R_2}{2},\qquad
|R_2|=(R_2^2)^{1/2}.
\]
这些都是明确的非负二阶矩阵。若 \(D_-\ne0\)，令 \(j\) 是其唯一非零位置；若为空，以下第一列取零。定义
\[
W(t)=\sqrt F\left[
\sqrt{(D_-)_{jj}}\,E^*e_j\ ,\ U R_{2,-}^{1/2}
\right]. \tag{4.2}
\]
右边总共至多三列。由 (3.5)，准确有
\[
\boxed{
\mathcal K_M(t)
=F\bigl[E^*D_+E+U R_{2,+}U^*\bigr]-W(t)W(t)^*.
} \tag{4.3}
\]
第一项为 PSD。因此对每个 \(0<t<1\)，
\[
\boxed{n_-(\mathcal K_M(t))\le\min\{3,Q-1\}.} \tag{4.4}
\]
这里给出了完整分解，不只是一条 rank 计数。

## 5. 坏方向的真实来源与量词限制

对于固定 \(t\)，函数
\(z\mapsto(z-1)/(1-t+tz)\) 严格递增。因此对角负部若存在，其指标必为全部权中的最小或最大权之一。跨整个 \(t\) 区间，这部分只需两个固定的物理坐标；若存在并列最大绝对值，它们不可能同时满足严格负部条件。

另一方面，由 \(y'=-\Lambda y\)，
\[
\boxed{v=-u'.} \tag{5.1}
\]
若 \(c(t)=E^*p(t)\) 是同一实际条件均值的 contrast 部分，则
\[
\boxed{u=-\frac{c(t)}{1-t},\qquad
v=\frac{c'(t)}{1-t}+\frac{c(t)}{(1-t)^2}.} \tag{5.2}
\]
因此 (3.5) 中全部移动的二阶块，恰来自真实条件均值曲线及其导数，而非可以自由选择的两个坏源。

(4.3)–(4.4) 是点态结论。列 \(W(t)\) 随 \(t\) 移动，积分后不保留“三维负部”；(5.2) 的曲线整体也可以张成更大的空间。前述完整反例还证明相对负曲率的大小不可能在全部位数、正权上统一有界。本稿没有从有限负指数推出原 \(H,G,L\) 的全局回归界、固定有限维缺陷或最终相位常数。后续必须将 (5.2) 与原同源均值回归一并运输，不能分别估计它们的范数。
