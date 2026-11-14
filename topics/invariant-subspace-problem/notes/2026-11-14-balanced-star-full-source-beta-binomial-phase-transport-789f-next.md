# 含一维硬源的任意多组平衡模块：完整 Beta–binomial 相位运输

本稿处理小组有效长度 \(q_1,\ldots,q_m\ge1\)、主组有效长度
\(Q=\sum_iq_i\) 的真实组模块。中央硬源为一维，临界低源为 \(m\) 维，位数、组数和全部独立正权均不受限。

新增结构不只是三个单高度 Gram 的分别表达：全部源、硬源回归、两侧度量及非自伴相位来自同一个明确的联合概率 \((T,K_1,\ldots,K_m)\)。由此得到一个完整跨源正 Gram、两条同一系数的均值运输身份，以及精确的秩二位移关系。本文尚未由这些约束支付一般相位常数。

## 1. 原物理模型和完整源

采用物理标准子集正交归一的 Boolean 空间。第 \(i\) 个小组有 \(q_i\) 位、平方权 \(z_i>0\)；主组有 \(Q\) 位、平方权 \(1\)。总位数 \(2Q\)。在所有组内对称的 reducing 模块上，
\[
d_b=\sum b_jE_j,\qquad e_b=\sum b_j^{-1}E_j^*.
\]
与[主 spin 边界稿](2026-11-14-arbitrarily-many-weight-dominant-spin-phase-bound-789f-next.md)相同，聚合坐标的实际范数是
\[
\left\|\sum f_{\boldsymbol k,\ell}
\alpha^{\boldsymbol k}\gamma^\ell\right\|^2
=\sum\frac{|f_{\boldsymbol k,\ell}|^2}
{\prod_i\binom{q_i}{k_i}\binom Q\ell}. \tag{1.1}
\]
其中 \(d_0=\sum_i\partial_{\alpha_i}+\partial_\gamma\)。

所有 primitive 是差变量 \(\alpha_i-\gamma\) 的多项式。每个差变量次数至多 \(q_i\)，因此：
\[
U_0=\ker d_0\cap\mathcal S_Q=\mathbb Cu,\qquad
u=\prod_i(\alpha_i-\gamma)^{q_i}, \tag{1.2}
\]
\[
V_0=\ker d_0\cap\mathcal S_{Q-1}
=\operatorname{span}\{v_i:1\le i\le m\},\qquad
v_i=\frac{u}{\alpha_i-\gamma}. \tag{1.3}
\]
这些 \(m\) 个源线性无关，因为在差变量中它们是不同的单项式。没有遗漏其它低源。

令 \(D_j=\operatorname{diag}(b_I)\)，则实际源基
\[
\mathcal E_i=D_{Q-1}^{-1}v_i
\]
一般非正交。以下 \(h,g,\ell,q\) 一律表示在这同一源基中的真实二次型：
\[
h=\mathcal E^*\mathcal E,\quad
g=(\mathcal J_1\mathcal E)^*(\mathcal J_1\mathcal E),\quad
\ell=(\mathcal J_2\mathcal E)^*(\mathcal J_2\mathcal E),\quad
q=(e_b\mathcal E)^*(e_b\mathcal E), \tag{1.4}
\]
其中 \(\mathcal J_1,\mathcal J_2\) 是完整 \(d_b,d_b^2/2\) 的 MP 逆后限制到源。组模块是 reducing，故不先在 \(V_0\) 压缩再取逆。

直接使用实际 raising，
\[
\boxed{e_0v_i=(\alpha_i+\gamma)v_i.} \tag{1.5}
\]
真实硬源回归身份为
\[
4g=q-\text{对 }D_Q^{-1}U_0\text{ 的完整投影 Gram}. \tag{1.6}
\]
本模块硬源恰为一维，所以这里才可以减一个秩一项。

## 2. 一个明确的联合概率

置
\[
L_i(t)=1-t+z_it,\qquad
F(t)=\prod_iL_i(t)^{q_i},\qquad
Z_F=\int_0^1F(t)\,dt,\qquad
\pi=\prod_i z_i^{q_i},
\]
\[
c=(Q+1)\pi^{-1}Z_F.
\]
令
\[
T\ \hbox{具有密度 }\rho(t)=F(t)/Z_F,\quad 0<t<1.
\]
给定 \(T=t\)，令 \(K_i\) 相互独立，且
\[
K_i\mid T=t\sim\operatorname{Binomial}(q_i,p_i(t)),
\qquad p_i(t)=\frac{z_it}{L_i(t)}.
\]
记
\[
X_i=K_i/q_i,\quad X=(X_i)_{i=1}^m,\quad
m=\mathbb EX,\quad n=\mathbf1-m,\quad y=2m-\mathbf1. \tag{2.1}
\]
向量 \(m\) 与组数符号由上下文区分；所有矩阵尺寸都是组数乘组数。

联合概率积分后为
\[
\boxed{
\mathbb P\{K_i=k_i,\ 1\le i\le m\}
=\frac{\prod_i\binom{q_i}{k_i}z_i^{k_i}}
{(Q+1)Z_F\,\binom Q{\sum_i k_i}}.
} \tag{2.2}
\]
这是原硬源 \(u\) 的真实物理子集系数平方的归一化，不另假设抽样模型。条件于全部 \(K_i\)，后验恰为
\[
\boxed{T\mid K\sim\operatorname{Beta}(K_{\rm tot}+1,Q-K_{\rm tot}+1),}
\quad K_{\rm tot}=\sum_iK_i. \tag{2.3}
\]

定义同一概率下的三个完整矩阵
\[
\mathsf G=\operatorname{Cov}(X),
\]
\[
\mathsf H=\mathbb E\!\left[\frac{1-T}{T}\,XX^*\right],\qquad
\mathsf L=\mathbb E\!\left[\frac{T}{1-T}\,
(\mathbf1-X)(\mathbf1-X)^*\right]. \tag{2.4}
\]
这些期望有限：条件概率在相应端点提供消失因子。它们都严格正定；例如 \(K\) 的每个合法值有正概率，\(\operatorname{Cov}(X)\) 不可能在一个非零系数方向为零。

## 3. 全部物理二次型的同源识别

准确有
\[
\boxed{
h=c\mathsf H,\qquad g=c\mathsf G,\qquad
\ell=c\mathsf L,\qquad
q=c(4\mathsf G+yy^*).
} \tag{3.1}
\]

下面给出完整识别，特别保留原源度量和硬源回归。

### 3.1 顶逆和两侧源度量

在实际 \((Q-1)\) 层，源 \(v_i\) 的系数相对于
\(\prod_j\binom{q_j}{k_j}\) 为
\[
(-1)^{Q-1-\sum k_j}\frac{q_i-k_i}{q_i}.
\]
由 (1.1)，对 \(i\ne j\)，
\[
\langle D_{Q-1}v_i,D_{Q-1}v_j\rangle
=(Q+1)\int_0^1 F(t)\frac{t(1-t)}{L_i(t)L_j(t)}\,dt.
\]
对角多出同一 binomial 条件方差，故全矩阵为
\[
\frac{\langle Dv_i,Dv_j\rangle}{(Q+1)Z_F}
=
\mathbb E_\rho\left[
\frac{t(1-t)}{L_iL_j}
+\mathbf1_{i=j}\frac{z_it^2}{q_iL_i^2}
\right]. \tag{3.2}
\]
右边正是 \(\mathsf L_{ij}\)。

完整顶 MP 逆给
\[
\ell_{ij}=\pi^{-1}\langle Dv_i,Dv_j\rangle.
\]
该身份可由原补集容斥逐项证明，见主 spin 边界稿 §3；那里证明的完整顶逆对任意 primitive 成立，不依赖空硬源。

又
\[
F_{\boldsymbol z^{-1}}(t)=\pi^{-1}F_{\boldsymbol z}(1-t).
\]
对源度量 \(h_{ij}=\langle D^{-1}v_i,D^{-1}v_j\rangle\) 使用 (3.2) 的倒数权，得到
\[
\frac{h_{ij}}c
=
\mathbb E_\rho\left[
\frac{z_iz_jt(1-t)}{L_iL_j}
+\mathbf1_{i=j}\frac{z_i(1-t)^2}{q_iL_i^2}
\right]
=\mathsf H_{ij}. \tag{3.3}
\]
两个式子中的附加对角项都保留，不能只取条件均值的 Gram。

### 3.2 中央硬源回归给完整协方差

在中央层，相对于硬源 \(u\) 的子集系数，(1.5) 的系数为
\[
\frac{2k_i}{q_i}-1=2X_i-1.
\]
因此带权中央物理 Gram 为
\[
\pi^{-1}(Q+1)Z_F\,
\mathbb E[(2X-\mathbf1)(2X-\mathbf1)^*]
=c(4\mathsf G+yy^*).
\]
中央补集在硬源与 raised 低源上分别为相反的标量符号，因此把正权中央表达换回实际倒数去权，只会改变两者的交叉符号，不改变这个 Gram 或其秩一投影。

实际硬源平方范数为 \(c\)，交叉均值为 \(\pm cy\)。由 (1.6)，完整硬源投影 Gram 恰为 \(cyy^*\)，故
\[
\boxed{g=c\operatorname{Cov}(X).}
\]
这里减去的是已经证明等于整个 \(U_b\) 的硬源，绝没有漏掉额外 nuisance。

条件方差分解还给
\[
\boxed{
\mathsf G=\operatorname{Cov}_\rho(p(T))
+\operatorname{diag}\left(
\frac{\mathbb E_\rho p_i(T)(1-p_i(T))}{q_i}
\right).
} \tag{3.4}
\]
两个部分都来自同一测度；尤其不把有限组的条件 binomial 噪声删掉。

## 4. 完整非交换目标和一个新的同源正块

在原非正交源中，准确相位交叉为
\[
J=h g^{-1}\ell+2g-q=c\mathsf J,
\]
\[
\boxed{\mathsf J=\mathsf H\mathsf G^{-1}\mathsf L
-2\mathsf G-yy^*.} \tag{4.1}
\]
物理等距源是 \(\mathcal E h^{-1/2}\)，所以目标有固定的非交换次序：
\[
\boxed{
\Phi\preceq\kappa I
\iff
\mathsf J^*\mathsf L^{-1}\mathsf J\preceq\kappa\mathsf H
\iff
\begin{pmatrix}
\kappa\mathsf H&\mathsf J^*\\
\mathsf J&\mathsf L
\end{pmatrix}\succeq0.
} \tag{4.2}
\]
不把 \(\mathsf H,\mathsf G,\mathsf L\) 当作彼此可交换的标量矩。

同一联合概率给完整的、通常非自伴的交叉 Gram：
\[
\boxed{
\begin{pmatrix}
\mathsf H&mn^*-\mathsf G\\
nm^*-\mathsf G&\mathsf L
\end{pmatrix}\succeq0.
} \tag{4.3}
\]
证明取同一物理概率空间中的两列
\[
A=\sqrt{\frac{1-T}{T}}\,X,\qquad
B=\sqrt{\frac{T}{1-T}}\,(\mathbf1-X).
\]
则
\[
\mathbb E AB^*
=\mathbb E[X(\mathbf1-X)^*]
=mn^*-\operatorname{Cov}(X).
\]
因此 (4.3) 保留所有源方向和真实混合项。这不是把三个分别正定的矩阵任选后拼块。

(4.3) 的交叉与 (4.1) 的交叉不同；本文没有以 (4.3) 自动替代目标 (4.2)。

## 5. 后验消积分与同一系数均值运输

由 (2.3)，
\[
\mathsf H
=\mathbb E\left[
\frac{Q-K_{\rm tot}+1}{K_{\rm tot}}XX^*
\right],\quad
\mathsf L
=\mathbb E\left[
\frac{K_{\rm tot}+1}{Q-K_{\rm tot}}
(\mathbf1-X)(\mathbf1-X)^*
\right]. \tag{5.1}
\]
第一式在 \(K_{\rm tot}=0\) 的整项定义为 \(0\)，因为 \(X=0\)；第二式在
\(K_{\rm tot}=Q\) 同样定义为 \(0\)。这也由相应条件期望直接得到。

令组长度列
\[
\boldsymbol q=(q_1,\ldots,q_m)^*,\qquad
k=\mathbb EK_{\rm tot}=\boldsymbol q^*m.
\]
由于 \(\boldsymbol q^*X=K_{\rm tot}\)，(5.1) 给
\[
\boxed{
(\mathsf H+\mathsf G)\boldsymbol q=(Q+1-k)m,
} \tag{5.2}
\]
\[
\boxed{
(\mathsf L+\mathsf G)\boldsymbol q=(k+1)n.
} \tag{5.3}
\]
例如，
\[
\mathsf H\boldsymbol q
=(Q+1)m-\mathbb E[XK_{\rm tot}]
=(Q+1-k)m-\mathsf G\boldsymbol q.
\]
第二式同理。这两个式子的系数是同一组长度向量，不能分别选择源。

后验均值还给
\[
\mathbb ET=\frac{k+1}{Q+2},\qquad
\mathsf G\boldsymbol q
=(Q+2)\operatorname{Cov}_\rho(p(T),T). \tag{5.4}
\]
这些是完整回归在共同源上的实际运输约束。

## 6. 精确秩二位移与对角关系

令
\[
Z=\operatorname{diag}(z_1,\ldots,z_m),\qquad z=Z\mathbf1.
\]
由条件平均的恒等式
\[
(z_i-z_j)p_i(t)p_j(t)=z_ip_j(t)-z_jp_i(t)
\]
以及 (3.4) 中条件噪声只在对角，得到
\[
\boxed{
[Z,\mathsf G]=(Zn)m^*-m(Zn)^*.
} \tag{6.1}
\]
因此真实协方差的位移秩至多为 \(2\)，包括所有组长和独立权。

由 (3.2)，
\[
(z_i-z_j)\mathsf L_{ij}=m_i-m_j\quad(i\ne j),
\]
所以
\[
\boxed{[Z,\mathsf L]=m\mathbf1^*-\mathbf1m^*.} \tag{6.2}
\]
全部对角噪声也给一个准确矩阵身份：
\[
\boxed{
\mathsf H=Z\mathsf LZ-
\operatorname{diag}\!\left(\frac{z_i y_i}{q_i}\right).
} \tag{6.3}
\]
确实，非对角由 (3.2)–(3.3) 直接相等；对角差是
\[
\frac{z_i}{q_i}
\mathbb E_\rho\frac{(1-T)^2-z_i^2T^2}{L_i(T)^2}
=\frac{z_i}{q_i}\mathbb E_\rho(1-2p_i)
=-\frac{z_i y_i}{q_i}.
\]
从而
\[
[Z,\mathsf H]=(Zm)z^*-z(Zm)^*. \tag{6.4}
\]
以上公式在重复权值处仍是原积分恒等，不要求除以 \(z_i-z_j\)。

这些位移关系与 (4.3)、(5.2)–(5.3) 必须联合使用。只保一个 Cauchy 型非对角矩阵而丢掉真实对角、均值或回归，会改变目标。

## 7. 量词与下一条实际缺口

本稿覆盖任意组数、任意正整数有效组长、任意正权的平衡主组模块。低源维数随组数增长，原组内全部 primitive 多重性可逐个作为正交副本保留；完整 MP 不因该分解改变。

两权情形已经由独立全位数定理支付。本稿给含硬源、任意多权情形的新的完整共同概率正块和运输约束；尚需在这些真实约束下证明
\[
(\mathsf H\mathsf G^{-1}\mathsf L-2\mathsf G-yy^*)^*
\mathsf L^{-1}
(\mathsf H\mathsf G^{-1}\mathsf L-2\mathsf G-yy^*)
\preceq \kappa\mathsf H
\]
具有与组数、组长、权值无关的有限 \(\kappa\)，或找出真实反例。

严格对数凹的标量密度 \(F\) 不允许把该非交换矩阵命题直接升级为标量引理。本文不引用矩阵 Prékopa、Lee–Yang 或其它外部定理来代付它，也未增加有限数值扫描。

