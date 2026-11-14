# 真实 additive contrast 密度的一般矩阵 N-log 凹性为假

本稿给出有限正权、完整 reducing 源上的精确反例：平衡 star 的实际 additive contrast 矩阵密度不必 N-log 凹。这里计算的是完整矩阵逆后的曲率，不是把一个标量压缩的曲率当成完整矩阵曲率。结论仅排除将这一密度一般性地放入要求 N-log 凹权的矩阵 Brascamp–Lieb 定理的路线；它不否定原实际相位不等式。

## 1. 准确矩阵密度与曲率

先把小组拆成 \(Q\) 个独立位。取 \(z_i>0\)，令
\[
L_i(t)=1-t+z_it,\qquad F(t)=\prod_{i=1}^{Q}L_i(t),
\qquad p_i(t)=\frac{z_it}{L_i(t)}.
\]
条件于 \(t\in(0,1)\)，各 \(X_i\sim\operatorname{Bernoulli}(p_i(t))\) 独立。这是原平衡 star 联合概率中的真实条件分布，没有另换测度。

令 \(E:\mathbf1^\perp\hookrightarrow\mathbb C^Q\) 为任意固定正交归一源坐标。对 \(v\in\mathbf1^\perp\)，写 \(f_v(X)=\sum_i v_iX_i\)。定义整个 \(Q-1\) 维源上的正定矩阵密度
\[
\langle M(t)v,v\rangle
=\frac{F(t)}{t(1-t)}\,\mathbb E_t|f_v(X)|^2. \tag{1.1}
\]
严格正定来自每个 Boolean 状态的正条件概率以及非零 additive 源不可能恒为零。

令 \(Z=\operatorname{diag}z_i\)、\(L=\operatorname{diag}L_i\)、\(c=z-\mathbf1\)。由完整条件方差和均值，准确有
\[
M(t)=F(t)E^*L^{-1}\bigl[Z+t(1-t)cc^*\bigr]L^{-1}E. \tag{1.2}
\]
等价地，这个完整矩阵有 PSD Bernstein 系数展开
\[
\langle M(t)v,v\rangle
=\sum_{s=1}^{Q-1}t^{s-1}(1-t)^{Q-s-1}
\sum_{|I|=s}z_I\left|\sum_{i\in I}v_i\right|^2. \tag{1.3}
\]
两端消失只使用 \(\sum_i v_i=0\)。

一维 N-log 凹所需的真实矩阵曲率条件是
\[
\mathcal K(t):=M'(t)M(t)^{-1}M'(t)-M''(t)\succeq0. \tag{1.4}
\]
对任意固定可逆源坐标变换 \(S\)，密度 \(\widetilde M=S^*MS\) 的曲率严格为 \(S^*\mathcal KS\)。所以可以在固定非归一基中计算二次型的符号；不能在非 reducing 子块上先压缩再取逆。

## 2. 一个保持全部源的对称族

取整数 (R\ge1\)，置 (Q=R+2\)，并取全部有限正权
\[
z=(r,r^{-1},\underbrace{1,\ldots,1}_{R}),\qquad r>0.
\]
记
\[
d=r+r^{-1}-2\ge0,\qquad e=r-r^{-1},\qquad
a=t(1-t).
\]
则
\[
F(t)=1+da,\qquad e^2=d(d+4). \tag{2.1}
\]

后 \(R\) 位的置换群同时保持条件概率、完整源 \(\mathbf1^\perp\) 及所有 \(M(t)\)。因此该源正交分为：

- 后池内部 contrast：两个头系数为零，池系数和为零，维数 \(R-1\)；
- 池置换不变源：维数 \(2\)，可取下面的固定基。

这两块在所有 \(t\) 下的交叉为零，因而同时约化 \(M,M',M''\) 及完整逆 \(M^{-1}\)。取后一块的基
\[
v_A=(1,-1,0,\ldots,0),\qquad
v_B=(-R/2,-R/2,1,\ldots,1). \tag{2.2}
\]
二者均在 \(\mathbf1^\perp\)，且在原欧氏源度量中正交，平方范数分别为
\[
\|v_A\|^2=2,\qquad \|v_B\|^2=R(R+2)/2. \tag{2.3}
\]

## 3. 完整两维块的精确计算

在 (2.2) 的同一固定源基中，真实密度严格是
\[
\boxed{
M_{\rm sym}(t)=
\begin{pmatrix}
d+2 & Re(t-\tfrac12)\\
Re(t-\tfrac12)&
R+\dfrac{R^2}{4}(d+2)-R(R-1)d\,t(1-t)
\end{pmatrix}.
} \tag{3.1}
\]

以下给出直接来源，保留条件 binomial 噪声。令 \(S_R\) 是后池的占据数，则 \(S_R\sim\operatorname{Binomial}(R,t)\)，且与两个头独立。源函数是
\[
f_A=X_0-X_1,\qquad
f_B=S_R-\frac R2(X_0+X_1).
\]
首先，真正 pair contrast 给
\[
\frac Fa\mathbb E_t f_A^2=r+r^{-1}=d+2.
\]
又
\[
\mathbb E_t(f_Af_B)
=R(t-\tfrac12)(p_0-p_1),\qquad
p_0-p_1=\frac{ae}{F},
\]
得到 (3.1) 的交叉项。

最后，把 \(f_B\) 写为两个独立项
\[
f_B=(S_R-Rt)-\frac R2(X_0+X_1-2t).
\]
后池项方差是 \(Ra\)，而两个头的直接 Bernoulli 计算给
\[
\frac Fa\mathbb E_t(X_0+X_1-2t)^2
=(d+2)-4da.
\]
故
\[
\frac Fa\mathbb E_t f_B^2
=RF+\frac{R^2}{4}\bigl[(d+2)-4da\bigr],
\]
这正是 (3.1) 的右下项。

在后池 contrast 块上，条件均值为零、条件方差为 \(a\|v\|^2\)，所以另一个完整块恰为
\[
M_{\rm pool}(t)=F(t)I_{R-1}. \tag{3.2}
\]

## 4. 真完整曲率及明确五位反例

在 \(t=1/2\)，(3.1) 为正对角矩阵，且
\[
M_{\rm sym}(\tfrac12)
=\operatorname{diag}\!\left(d+2,\ R(1+R/2+d/4)\right),
\]
\[
M_{\rm sym}'(\tfrac12)
=\begin{pmatrix}0&Re\\Re&0\end{pmatrix},\qquad
M_{\rm sym}''(\tfrac12)
=\operatorname{diag}(0,2R(R-1)d).
\]
因此曲率也准确对角化。特别是其第二个二次型为
\[
\boxed{
\bigl(\mathcal K_{\rm sym}(\tfrac12)\bigr)_{BB}
=\frac{R^2e^2}{d+2}-2R(R-1)d
=\frac{Rd\,[4-(R-2)d]}{d+2}.
} \tag{4.1}
\]
第一项为 \(R^2e^2/[R(1+R/2+d/4)]\)，非负；后池曲率是 \(2dI_{R-1}\)。所以当
\[
R\ge3,\qquad d>\frac4{R-2}, \tag{4.2}
\]
时，整个真实 \(Q-1\) 维曲率恰有一个严格负方向。

取最简单的具体值
\[
\boxed{Q=5,\quad R=3,\quad r=6,\quad
z=(6,1/6,1,1,1).}
\]
此时 \(d=25/6,e=35/6\)，完整两维块为
\[
\boxed{
M_{\rm sym}(t)=
\begin{pmatrix}
37/6&(35/2)(t-1/2)\\
(35/2)(t-1/2)&135/8-25t(1-t)
\end{pmatrix}.
} \tag{4.3}
\]
在 \(t=1/2\)，真实完整逆给
\[
\boxed{
\mathcal K_{\rm sym}(\tfrac12)
=\operatorname{diag}(490/17,-25/74).
} \tag{4.4}
\]
若改用原物理正交归一源 \(v_A/\sqrt2\)、\(v_B/\sqrt{15/2}\)，则该块是
\[
\operatorname{diag}(245/17,-5/111).
\]
其余两维后池 contrast 的曲率为 \((25/3)I_2\)。这明确保留了全部四维源以及真正完整矩阵逆。

## 5. 量词和方法边界

有限正权例 (4.3)–(4.4) 已足以否定一般 (1.4)，不依赖权趋于零或无穷的极限，也不是浮点病态诊断。

该族还给相对负曲率的准确量级：
\[
\frac{(\mathcal K_{\rm sym})_{BB}}{(M_{\rm sym})_{BB}}
=\frac{4d\,[4-(R-2)d]}{(d+2)(d+2R+4)}
\longrightarrow -4(R-2)\quad(d\to\infty). \tag{5.1}
\]
所以即使只要求 \(\mathcal K\succeq-CM\)，在所有位数和全部正权上也不能从这一密度得到维数无关的有限 \(C\)。这只限制该具体曲率预算；有限负方向仍可与真实共同回归中的其它块抵消。

特别地，固定端点补偿也不能在全规模统一修复这个条件。对任意固定 \(c\ge0\)，若 \(\widetilde M=[t(1-t)]^cM\)，则完整矩阵微分给
\[
\mathcal K_{\widetilde M}
=[t(1-t)]^c\left\{\mathcal K_M+
 c\left[t^{-2}+(1-t)^{-2}\right]M\right\}.
\]
在中心，括号中沿同一个 \(v_B\) 的相对二次型由 (5.1) 趋于
\(-4(R-2)+8c\)。只须取整数 \(R>2c+2\)，再取足够大的**有限**正权 \(r\)，这个二次型便严格为负。因此不存在对全部位数和全部正权统一适用的固定端点指数 \(c\)。

原目标仍是完整平衡 star 源的
\[
J=HG^{-1}L-2G-(2m-\mathbf1)(2m-\mathbf1)^*,
\qquad J^*L^{-1}J\preceq\kappa H.
\]
本文没有否定它，也没有把矩阵曲率的负方向当成实际相位的反例。它准确排除的是：不再核实真实正曲率，就把 (1.1) 的矩阵密度直接送入要求 N-log 凹的矩阵 Brascamp–Lieb 定理。

## 6. 所排除的文献应用条件

Cordero-Erausquin, *On matrix-valued log-concavity and related Prékopa and Brascamp–Lieb inequalities*, [arXiv:1801.04862](https://arxiv.org/abs/1801.04862)，§3 Theorem 4，给出矩阵 N-log 凹权下的完整方差估计；[作者全文](https://webusers.imj-prg.fr/~dario.cordero/Docs/articles/matrix_log_concave_5.pdf)明确要求该曲率条件。这里不反驳该定理，而是证明本课题的 (1.1) 密度一般不满足其假设；固定端点幂也不能在全规模统一补齐。原相位中的均值、总数与共同回归仍须联合保留，不能用这个失败的充分条件替代原问题。
