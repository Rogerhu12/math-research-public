# 偶临界相位二阶核的至多四有效位约化与每个固定方向的局部界

本稿把等权二阶正性真正推进到**包括二阶退化在内的每个固定方向的完整局部相位界**。核心不是逐个估计四阶大项，而是证明：二阶核所在的实际组 Casimir 模块，抽去组内 singlet 后至多只含四个有效 Boolean 位。这些完整模块已由全四权相位定理控制。

本文所有源度量、组链同构和 MP 逆均为物理 Hilbert 内积下的对象。结论的邻域半径依赖方向；本文不把这种量词改成一个共同开邻域，更不声称所有正权、所有位数的统一相位界已经完成。

## 1. 实际相位与已证二阶能量

在 \(M=2s\) 位的 Boolean Hilbert 空间上，令

\[
d_b=\sum_{i=1}^{2s}b_iE_i,
\qquad e_b=\sum_{i=1}^{2s}b_i^{-1}E_i^*,
\qquad b_i>0.
\]

低源和硬上源分别为

\[
V_b=\ker d_b\cap\mathcal H_{s-1},\qquad
U_b=\ker d_b\cap\mathcal H_s.
\]

令 \(G_b\)、\(L_b\) 分别为完整 \(d_b\) 与 \(d_b^2/2\) 的 MP 逆在 \(V_b\) 上的 Gram，并令 \\(A_{0,b}=e_b^*|_{U_b}:U_b\to V_b\)。定义

\[
H_{0,b}=G_b^{-1}L_b-2G_b-A_{0,b}A_{0,b}^*,
\qquad \Phi_b=H_{0,b}^*L_b^{-1}H_{0,b}. \tag{1.1}
\]

这是偶临界池的实际相位费用，不是原无限算子的 graph Gram。

固定 \(x\in\mathbb R^{2s}\)、\(\sum_i x_i=0\)，取

\[
z_i(\varepsilon)=b_i(\varepsilon)^2=1+\varepsilon x_i>0.
\]

写 \\(d_0=\sum E_i\)、\(e_0=d_0^*\)、\(V_0=\ker d_0\cap\mathcal H_{s-1}\)、\(U_0=\ker d_0\cap\mathcal H_s\)。对 \(D_j=\operatorname{diag}(\prod_{i\in I}b_i)\) 于第 \(j\) 层，

\[
\mathcal E_\varepsilon=D_{s-1}^{-1}|_{V_0},\qquad
H_\varepsilon=\mathcal E_\varepsilon^*\mathcal E_\varepsilon,
\qquad \mathcal U_\varepsilon=\mathcal E_\varepsilon H_\varepsilon^{-1/2}
\]

是真正从固定 \(V_0\) 到 (V_{b(\varepsilon)}\) 的等距同构。

已证的全出生二阶定理（`2026-11-14-all-birth-even-phase-equal-weight-second-variation-789f-next.md`）给

\[
I-\mathcal U_\varepsilon^*\Phi_{b(\varepsilon)}\mathcal U_\varepsilon
=\varepsilon^2 K_x+O_{s,x}(\varepsilon^3), \tag{1.2}
\]

\[
K_x=\tfrac14 B_x^*B_x+\tfrac12 S_x^*S_x,
\quad B_x=d_x|_{V_0},\quad S_x=P_{U_0}d_x^*|_{V_0},
\quad d_x=\sum_i x_iE_i.
\]

其中 \(X_j=\sum_i x_i n_i\) 使用**占据**投影 \(n_i\)，并有实际正交两塔恒等式

\[
X_s e_0|_{V_0}=S_x+\tfrac16 e_0^2 B_x.
\]

因此

\[
\boxed{\ker K_x=\ker(X_s e_0|_{V_0}).} \tag{1.3}
\]

本稿处理 (1.3) 中可能存在的核，不能在该核上仅凭 \(O(\varepsilon^3)\) 断言正性。

## 2. 按相等方向值分组的物理正交链

令 \(x\) 的不同值为 \(\xi_1,\ldots,\xi_m\)，对应互不相交组 \(I_g\)、组大小 \(q_g\)。记

\[
d_g=\sum_{i\in I_g}E_i,\quad e_g=d_g^*,\quad
N_g=\sum_{i\in I_g}n_i,\quad m_g=N_g-q_g/2.
\]

这些组算子满足

\[
[d_g,e_g]=q_gI-2N_g=-2m_g,
\quad [m_g,e_g]=e_g,
\quad [m_g,d_g]=-d_g.
\]

每组有标准的物理正交 ladder 分解。具体地，取单位 primitive 向量 \(p_g\) 于组内次数 \(a_g\)，满足 \(d_gp_g=0\)。令

\[
h_g=q_g-2a_g\ge0,\qquad j_g=h_g/2,
\]

\[
u_{g,k}=\frac{e_g^k p_g}{\sqrt{k!\,h_g!/(h_g-k)!}},
\quad 0\le k\le h_g.
\]

由上述交换式逐次得到

\[
\begin{aligned}
d_g u_{g,k}&=\sqrt{k(h_g-k+1)}\,u_{g,k-1},\\
e_g u_{g,k}&=\sqrt{(k+1)(h_g-k)}\,u_{g,k+1},\\
m_g u_{g,k}&=(k-j_g)u_{g,k}.
\end{aligned} \tag{2.1}
\]

各链正交，且链和等于整组空间：链是 \(d_g,e_g,N_g\) 的 reducing 子空间；若正交补非零，在其最小非零次数选一个向量即被 \(d_g\) 杀死，从而再生成一条链，有限维中过程终止。不同 primitive 多重性保持为彼此正交的同型副本。

把每组选定链作张量积，得到全空间的正交 reducing 分解。固定一个这样的模块，记

\[
J=\sum_g j_g,\qquad a=\sum_g a_g=s-J.
\]

该模块的全次数为 \(a+\sum_g k_g\)。因 \(2s\) 为偶数，\(J\) 为非负整数。全中央层 \(\mathcal H_s\) 对应 \(\sum_g m_g=0\)，而 \(V_0\) 的次数对应有效次数 \(J-1\)。没有非零 \(V_0\) 的模块直接忽略。

## 3. 二阶核只能出现在 \(J\le2\) 的模块

**定理 3.1。** 在上述任何固定组链模块中，若存在非零 \(v\in V_0\) 满足 \(K_xv=0\)，则

\[
\boxed{J=\sum_gj_g\le2.} \tag{3.1}
\]

**证明。** 置 \(f=e_0v\)。由于 \(v\) 是全次数 \(s-1\) 的 primitive，

\[
\|f\|^2=2\|v\|^2>0,\qquad e_0d_0f=2f. \tag{3.2}
\]

又由 (1.3)，\(X_s f=0\)。在中央层

\[
X_s=\sum_g\xi_gN_g
=\tfrac12\sum_i x_i+\sum_g\xi_gm_g
=\sum_g\xi_gm_g.
\]

记 \(P_0\) 为该固定模块中央层上 \(X_s\) 的零特征空间投影。不同组之间有

\[
[X_s,e_gd_h]=(\xi_g-\xi_h)e_gd_h.
\]

当 \(g\ne h\) 时 \(\xi_g\ne\xi_h\)，所以

\[
P_0e_gd_hP_0=0.
\]

因 \(f=P_0f\)，完整 \(e_0d_0\) 的二次型严格化为

\[
2\|f\|^2
=\langle f,e_0d_0f\rangle
=\Big\langle f,\sum_g e_gd_g f\Big\rangle. \tag{3.3}
\]

在 (2.1) 的共同磁量子数基下，

\[
e_gd_g=j_g(j_g+1)-m_g^2+m_g.
\]

中央层 \(\sum_gm_g=0\)，且 \(|m_g|\le j_g\)，因此

\[
\sum_g e_gd_g
=\sum_g[j_g(j_g+1)-m_g^2]
\succeq\Big(\sum_gj_g\Big)I=JI.
\]

与 (3.3) 合并给 \(2\ge J\)。证毕。

这里没有把 \(X_s\) 的零支持误认为“只能在一个等值组活动”。例如四位方向 \((-1,0,0,1)\) 的真实退化向量位于 \((j_1,j_2,j_3)=(1/2,1,1/2)\)，恰有 \(J=2\)，符合 (3.1)。其退化核不沿整条直线保持等号，已在独立方法边界稿中精确说明。

## 4. 同一组链模块内的完整 MP 与相位就是 \(2J\) 有效位模型

沿 \(z_i=1+\varepsilon x_i\)，同一组内的权为共同值

\[
b_g(\varepsilon)=\sqrt{1+\varepsilon\xi_g}.
\]

因而

\[
d_b=\sum_gb_gd_g,\qquad e_b=\sum_gb_g^{-1}e_g.
\]

它们及其物理伴随、次数投影都保持 §2 的固定正交组链分解。对第 \(g\) 组，把 (2.1) 的 \(h_g+1=2j_g+1\) 维链等距映为 **\(2j_g\) 个相等权 \(b_g\) 位的对称模块**；标准归一的对称 Boolean 链恰具有 (2.1) 的系数。此映射没有额外的权依赖范数因子。

张量积后得到 \(2J\) 个有效位的物理等距同构，总次数仅减去固定整数 \(a=s-J\)。特别地，

\[
V_b\longleftrightarrow\ker d_b^{\rm eff}\cap\mathcal H_{J-1}^{\rm eff},
\qquad
U_b\longleftrightarrow\ker d_b^{\rm eff}\cap\mathcal H_J^{\rm eff}. \tag{4.1}
\]

当 \(j_g=0\) 时，整组 chain 为一个 singlet，在实际 \(d_g,e_g\) 上均为零，只贡献固定次数平移和正交多重性。

由于全空间分解是 \(d_b\) 及其伴随的共同正交 reducing 分解，完整 \\(d_b^n/n!\) 的 MP 逆也逐模块分解。这可直接由最小范数逆的定义看出：不同块的输入、输出正交，给定一个块的源，任何其他块的原像分量只增加范数而不改变该源。故完整 MP 逆先计算后压源，和 (4.1) 的物理等距同构严格兼容；这里没有先把完整逆替成 primitive 压缩的逆。

同理，\(G,L,A_0,H_0,\Phi\) 全部在这些相同物理块上按 (1.1) 分解。源输运 \(\mathcal U_\varepsilon\) 也保持它们，因为 \(D_{s-1}\) 在每组只是 \(b_g^{N_g}\) 的乘积，保持每条组链；其压缩源度量及正平方根亦如此。

于是所有 \(J\le2\) 且源非零的块，完整相位等于二位或四位有效模型相位的 reducing 限制。四位全正权结果已证

\[
\Phi_{\rm eff}\preceq I
\]

（`2026-11-14-four-bit-all-weight-even-phase-bound-789f-next.md`）。二位情形也直接有

\[
G=(z_1+z_2)^{-1},\quad L=(z_1z_2)^{-1},\quad
H_0=\frac2{z_1+z_2},\quad
\Phi=\frac{4z_1z_2}{(z_1+z_2)^2}\le1. \tag{4.2}
\]

因此这些 \(J\le2\) 块在**整条仍保持正权的直线**上都满足相位界，含退化核在内；不是仅给出其二阶系数的正性。

## 5. 每个固定方向的完整局部界

**定理 5.1。** 对每个有限偶位数 \(M=2s\) 和每个固定 \(x\in\mathbb R^{2s}\)、\(\sum x_i=0\)，存在 \(\eta_{s,x}>0\)，使得

\[
|\varepsilon|<\eta_{s,x}
\quad\Longrightarrow\quad
z_i=1+\varepsilon x_i>0\ \text{且}\ \Phi_{b(\varepsilon)}\preceq I. \tag{5.1}
\]

**证明。** 用同一个方向分组作上述有限正交分解。所有 \(J\le2\) 块由 §4 对整个正权区间满足相位界。其余源非零块有 \(J>2\)；由定理 3.1，正算子 \(K_x\) 在这些块上没有核，因有限维而严格正定。若这些块非空，取其有限直和上的最小特征值 \(c_{s,x}>0\)。式 (1.2) 在这个固定有限维源上是算子范数展开，因此存在 \(C_{s,x}<\infty\) 和正半径，使

\[
I-\mathcal U_\varepsilon^*\Phi_{b(\varepsilon)}\mathcal U_\varepsilon
\succeq\varepsilon^2(c_{s,x}-C_{s,x}|\varepsilon|)I
\]

于这些高 \(J\) 块。再缩小半径使 \(C_{s,x}|\varepsilon|<c_{s,x}/2\)，它们的缺陷即严格正。若高 \(J\) 块为空，则不需这个步骤。与低 \(J\) 块合并，且 \(\mathcal U_\varepsilon\) 是物理等距同构，得 (5.1)。证毕。

**一个加强。** 若 \(2s\ge6\) 且 \(x_i\) 两两不同，每组都是一个位，唯一组 spin 为 \(j_g=1/2\)，故全部实际源模块都有 \(J=s>2\)。此时 \(K_x\) 在整个 \(V_0\) 上严格正，(5.1) 对充分小非零 \(\varepsilon\) 是严格不等式。即使某些中央 \(s\)-子集和为零，也不影响这个结论；单个零和支持不足以容纳总 spin \(1\) 的中央向量。

对不居中的一般方向，先把 \(x_i\) 减去平均值。共同平方权缩放 \(z\mapsto\lambda z\) 使 \(G\mapsto\lambda^{-1}G\)、\(L\mapsto\lambda^{-2}L\)、\(H_0\mapsto\lambda^{-1}H_0\)，所以 \(\Phi\) 不变。将 \(1+\varepsilon x_i\) 除以 \(1+\varepsilon\bar x\) 后，参数变为 \(\varepsilon/(1+\varepsilon\bar x)\)，故同一方向性结论仍成立。

## 6. 准确量词与仍未支付的范围

本稿给出的是

\[
\forall s\ \forall x\quad \exists\eta_{s,x}>0
\quad\forall|\varepsilon|<\eta_{s,x}:\ \Phi(1+\varepsilon x)\preceq I.
\]

它没有证明 \(\inf_{\|x\|=1}\eta_{s,x}>0\)，也没有证明任意正权点的相位界。方向发生合组时，某些高 \(J\) 块的二阶最小特征值可以趋于零；不能把固定方向的有限维正定直接改成统一方向余量。

本稿新增的是对所有方向的真实退化核支付：核只能落在全程 reducing 的至多四有效位块，四位定理控制其完整费用；其余块再使用严格二阶能量。它不依赖四阶逐点能量猜测，不引入抽象 Hodge 代替真实源，也没有把原 graph 或一般复 Hilbert 不变子空间问题视为完成。
