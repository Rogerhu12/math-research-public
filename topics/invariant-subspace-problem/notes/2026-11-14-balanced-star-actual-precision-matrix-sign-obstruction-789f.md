# 原平衡 star 的完整协方差逆并非总是 M 矩阵

本稿直接在原全部线性占据源中给出有理正权反例。即使原计数分布满足严格 MTP2，完整协方差逆仍可有严格正的非对角项。因此，不能用该逆的 M 矩阵符号免费控制均值通道。这里不否定原相位界，也不否定候选标量界 $m^*G^{-1}n\le Q$。

## 1. 同一个真实模型

取 $R\ge1$，$Q=R+2$，所有小位组长 $q_i=1$，正权平方为

$$
z=(r,r^{-1},\underbrace{1,\ldots,1}_{R}),\qquad r>0.
$$

原主组长为 $Q$。设

$$
D=r+r^{-1}+4\ge6,\qquad a(t)=t(1-t).
$$

原潜变量密度的未归一化分子与积分为

$$
F(t)=(1-t+rt)(1-t+r^{-1}t)=1+(D-6)a(t),
\qquad Z_F=\int_0^1F(t)\,dt=\frac D6.
$$

给定 $T=t$，各 $X_i$ 是独立 Bernoulli，成功率仍为 $z_it/(1-t+z_it)$。因此 $G=\operatorname{Cov}(X)$ 正是原整个 $Q$ 维低源的协方差；没有更换概率、添加非线性观察或丢弃总数通道。

记两个异常位为 $+$、$-$。直接积分给

$$
m_+=\frac{r+2}{D},\qquad m_-=\frac{r^{-1}+2}{D},
\qquad m_++m_-=1,
$$

其余每个位均值 $1/2$。例如

$$
\mathbb E X_+X_-=\frac2D,\qquad
\mathbb E(X_+T)=\frac{r+3}{2D},\qquad
\mathbb E T^2=\frac3{10}+\frac1{5D}.
$$

于是完整协方差的各块完全明确：

$$
G_{\{+,-\},\{+,-\}}
=\frac1{D^2}
\begin{pmatrix}2D-3&3\\3&2D-3\end{pmatrix},
\qquad
G_{\{+,-\},\mathrm{pool}}
=\frac1{2D}\begin{pmatrix}\mathbf1_R^*\\\mathbf1_R^*\end{pmatrix},
\tag{1.1}
$$

$$
G_{\mathrm{pool},\mathrm{pool}}
=\frac{D-1}{5D}I_R+\frac{D+4}{20D}\mathbf1_R\mathbf1_R^*.
\tag{1.2}
$$

全部非对角协方差均为正。另一方面，每个 Bernoulli 的条件方差在 $0<t<1$ 严格正，所以任意非零线性来源都具有正条件方差；特别 $G\succ0$。

## 2. 保留完整逆后的符号

池块在总数方向的特征值为

$$
v_R=\frac{(R+4)D+4R-4}{20D}.
$$

令 $C_R=(R+4)D+4R-4$。消去全部 $R$ 个池坐标的真实 Schur 补为

$$
S=\frac1{D^2}
\begin{pmatrix}2D-3&3\\3&2D-3\end{pmatrix}
-h\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad h=\frac{5R}{D C_R}.
\tag{2.1}
$$

特别

$$
S_{+-}
=\frac{(12-2R)D+12R-12}{D^2 C_R}.
\tag{2.2}
$$

两条对称/反对称特征值分别为

$$
\lambda_+(S)=\frac{2(R+4)(D-1)}{D C_R},\qquad
\lambda_-(S)=\frac{2(D-3)}{D^2}.
$$

它们均严格正。完整块逆公式是

$$
(G^{-1})_{\{+,-\},\{+,-\}}=S^{-1},
$$

所以这里不是先压掉池块、再对错误的压缩矩阵取逆。由上述两个特征值，准确得到

$$
\boxed{
(G^{-1})_{+-}
=\frac{D\bigl[(R-6)D-6(R-1)\bigr]}
 {2(R+4)(D-1)(D-3)}.}
\tag{2.3}
$$

当

$$
R>6,\qquad D>\frac{6(R-1)}{R-6},
\tag{2.4}
$$

该完整逆的非对角项严格为正。例如取 $R=8$、$r=20$，即 $Q=10$ 的实际权型 $(20,1/20,1^8)$，有 $D=481/20$，并且

$$
\boxed{(G^{-1})_{+-}=\frac{29341}{2328972}>0.}
\tag{2.5}
$$

这就排除了所有原正权模型的完整协方差逆都为 M 矩阵的命题。

## 3. 原分布确实严格 MTP2

原物理位占据集合 $I\subseteq[Q]$ 的概率为

$$
\mathbb P(X=\mathbf1_I)
=\frac{z_I}{(Q+1)Z_F\binom Q{|I|}}.
$$

外场因子 $z_I$ 在任意二坐标格不等式中准确抵消。令 $c_s=\binom Qs^{-1}$。对于 $0\le s\le Q-2$，

$$
\frac{c_s c_{s+2}}{c_{s+1}^2}
=\frac{(s+2)(Q-s)}{(s+1)(Q-s-1)}>1.
$$

这验证了全部严格二坐标格不等式。更一般的格不等式由这些二阶差相加而得，故该正分布满足 MTP2。因而本反例的逆符号失败不能归因于破坏原正关联结构，也不需要借用一般分布的反例。

## 4. 同族均值逆费用及准确失败范围

令 $n=\mathbf1-m$、$y=m-n$。本族中

$$
y=\frac{r-r^{-1}}D(1,-1,0,\ldots,0).
$$

故 $y$ 位于真实反对称 reducing 方向。对称的异常位和池总数构成另一个真实二维块，直接逆解得

$$
\mathbf1^*G^{-1}\mathbf1
=D+\frac{5RD}{(R+4)(D-1)},
\qquad
y^*G^{-1}y=\frac{D^2-8D+12}{D-3}.
$$

使用 $m=(\mathbf1+y)/2$、$n=(\mathbf1-y)/2$，得到

$$
\boxed{
m^*G^{-1}n
=\frac14\left[5+\frac3{D-3}
             +\frac{5RD}{(R+4)(D-1)}\right].}
\tag{4.1}
$$

特别当 $r\to\infty$ 时，该量趋于 $5(R+2)/(2(R+4))$，并没有随 $R$ 发散。本族只排逆矩阵逐项符号路线，不排 $m^*G^{-1}n\le Q$ 的可能性；更不能把其中任一标量界直接替代原完整相位

$$
J=HG^{-1}L-2G-yy^*,\qquad J^*L^{-1}J\le\kappa H.
$$

原均值、总数和全部线性源的共同回归仍须保留。普通 ISP 未因此解决。
