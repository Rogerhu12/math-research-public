# 任意三 spin 三角族：完整低源与硬回归的固定 Gaussian 生成核

本稿把三组任意有效 spin 的整个临界源放入一个固定 \(3\times3\) Gaussian 核。它不只生成中央硬源范数：所有低源两侧度量、raised Gram 和硬源交叉都有精确系数公式，进而给出完整第一 MP Gram 与实际非交换相位。

组大小可以任意增长。中央硬源始终一维，低源维数恰为三个边参数中正者的个数，至多 \(3\)。生成核的矩阵尺寸不随 spin 增长，只有所取的系数阶数增长。本文不把核的普通正性自动当作相位上界。

## 1. 有效长度、全部 primitive 及物理归一

取非负整数 \(A,B,C\)，不全为零，置
\[
q_1=A+B,\qquad q_2=A+C,\qquad q_3=B+C,\qquad
s=A+B+C.
\]
这是三个有效 spin 满足三角条件的完整参数化；总有效位数 \(2s\)。零长度组可以保留为平凡因子。各组平方权为 \(z_1,z_2,z_3>0\)。

使用三个聚合变量 \(\alpha_1,\alpha_2,\alpha_3\)，组内范数为
\[
\left\|\sum f_{\boldsymbol k}\alpha^{\boldsymbol k}\right\|_{\rm phys}^2
=\sum_{\boldsymbol k}\frac{|f_{\boldsymbol k}|^2}
{\prod_{i=1}^3\binom{q_i}{k_i}}. \tag{1.1}
\]
不带权 lowering 为 \(d_0=\sum_i\partial_{\alpha_i}\)。

记边 \(e\in\{12,13,23\}\)，对应边数
\[
a_{12}=A,\qquad a_{13}=B,\qquad a_{23}=C.
\]
中央硬源为
\[
\boxed{
U_0=\mathbb Cu,\qquad
u=(\alpha_1-\alpha_2)^A
(\alpha_1-\alpha_3)^B
(\alpha_2-\alpha_3)^C.
} \tag{1.2}
\]
全部低 primitive 源由正边对应的
\[
\boxed{
v_e=\frac{u}{\alpha_i-\alpha_j},\quad e=ij,\ a_e>0
} \tag{1.3}
\]
构成一个基。因此
\[
\boxed{\dim V_0=\#\{e:a_e>0\}\le3.} \tag{1.4}
\]

这里给出不遗漏源的直接证明。令
\(x=\alpha_1-\alpha_3,y=\alpha_2-\alpha_3\)。primitive 是齐次多项式 \(P(x,y)\)。
在总次数 \(s\) 上，三个组的次数界分别迫使
\[
y^C\mid P,\qquad x^B\mid P,\qquad (x-y)^A\mid P.
\]
三个因子互素且总次数为 \(s\)，所以只剩 (1.2)。
在总次数 \(s-1\) 上，必含因子
\[
x^{(B-1)_+}y^{(C-1)_+}(x-y)^{(A-1)_+}.
\]
若有 \(d\) 个正边，余下次数为 \(d-1\)。因为是两个差变量的齐次多项式，其空间维数为 \(d\)；(1.3) 给出 \(d\) 个独立元素，故恰为全部源。\(A=0\) 等边界没有额外隐藏方向。

实际大组的各个组内 primitive ladder，等距于这些有效长度的对称模块，且对 \(d_b,e_b\) 及伴随 reducing。因此本文逐块保留原组内的全部物理多重性与完整 MP 逆。

## 2. 二元齐次化与 Bargmann 范数

给每组引入两个变量 \(x_i,y_i\)，把 \(\alpha_i=x_i/y_i\) 齐次化到组次数 \(q_i\)。定义
\[
[ij]=x_i y_j-x_j y_i.
\]
于是
\[
u=[12]^A[13]^B[23]^C,
\]
\[
v_e=y_i y_j\prod_f[f]^{a_f-\mathbf1_{f=e}}. \tag{2.1}
\]
完整 raising \(e_0=\sum_i x_i\partial_{y_i}\) 对这些源给
\[
\boxed{
w_e:=e_0v_e
=(x_i y_j+x_j y_i)
\prod_f[f]^{a_f-\mathbf1_{f=e}}.
} \tag{2.2}
\]
这是把一条真实 singlet 边分别换成最低 triplet 与中央 triplet，而不是任意选取一个相邻源。

使用复 Gaussian/Bargmann 范数：独立变量 \(x_i\) 方差为 \(z_i\)，\(y_i\) 方差为 \(1\)。因此
\[
\|x_i^{k_i}y_i^{q_i-k_i}\|_{B,z}^2
=k_i!(q_i-k_i)!\,z_i^{k_i}.
\]
置
\[
K_q=q_1!q_2!q_3!,\qquad
\pi=\prod_i z_i^{q_i}.
\]
对于本节所有组次数固定为 \(q_i\) 的多项式，
\[
\boxed{\|f\|_{B,z}^2=K_q\,\|D f\|_{\rm phys}^2.} \tag{2.3}
\]
这个阶乘因子对硬源、全部低源、raised 源完全相同。

定义完整 Bargmann 矩阵
\[
M(z)=\langle u,u\rangle_{B,z},\quad
a_e(z)=\langle u,w_e\rangle_{B,z},
\]
\[
W_{ef}(z)=\langle v_e,v_f\rangle_{B,z},\qquad
S_{ef}(z)=\langle w_e,w_f\rangle_{B,z}. \tag{2.4}
\]
\(a\) 视作一行。以下构造同时生成这四项。

## 3. 硬源的固定有理生成函数

取三个复形式参数 \(t_{12},t_{13},t_{23}\)，组成反对称矩阵
\[
T=
\begin{pmatrix}
0&t_{12}&t_{13}\\
-t_{12}&0&t_{23}\\
-t_{13}&-t_{23}&0
\end{pmatrix},\qquad
Z=\operatorname{diag}(z_1,z_2,z_3).
\]
令
\[
F_T(x,y)=\exp(x^T T y)=\exp\!\left(\sum_e t_e[ e]\right).
\]
记 \(\xi_e=|t_e|^2\)。直接复 Gaussian 积分给
\[
\|F_T\|_{B,z}^2
=\det(I-T^*ZT)^{-1}. \tag{3.1}
\]
先在 \(\|Z^{1/2}T\|<1\) 内积分：消去 \(x\) 后，\(y\) 的精度为
\(I-T^*ZT\)，再将其正 Hermitian 矩阵酉对角化即可。随后作为原点形式幂级数读取，所以不要求所有参数同时落在收敛域内。

不同三边次数的态，若在组次数上相等，便须满足
\[
A+B=A'+B',\quad A+C=A'+C',\quad B+C=B'+C',
\]
从而 \(A=A',B=B',C=C'\)。因此全部交叉阶数在原物理内积中正交。准确得到
\[
\boxed{
\sum_{A,B,C\ge0}
\frac{M_{A,B,C}(z)}{(A!B!C!)^2}
\,\xi_{12}^A\xi_{13}^B\xi_{23}^C
=\frac1{\mathcal D(\xi;z)}.
} \tag{3.2}
\]
分母只有二次：
\[
\boxed{\begin{aligned}
\mathcal D={}&1-(z_1+z_2)\xi_{12}
-(z_1+z_3)\xi_{13}-(z_2+z_3)\xi_{23}\\
&+(\xi_{12}+\xi_{13}+\xi_{23})
(z_1z_2\xi_{12}+z_1z_3\xi_{13}+z_2z_3\xi_{23}).
\end{aligned}} \tag{3.3}
\]
证明是展开 \(\det(I-T^*ZT)\)：反对称 \(3\times3\) 矩阵的秩至多 \(2\)，一次项是
\(\operatorname{tr}(T^*ZT)\)，二阶主子式之和恰为 (3.3) 的第二行。

在全等权 \(z_i=1\) 时，
\[
\mathcal D=(1-\xi_{12}-\xi_{13}-\xi_{23})^2,
\]
从而直接得到完整归一
\[
\boxed{
M_{A,B,C}(1)=A!B!C!(A+B+C+1)!.
} \tag{3.4}
\]
实际硬源范数再除 \(K_q\)。这也显示 spin 的增长进入系数阶数和阶乘，生成核尺寸保持 \(3\)。

## 4. 所有低源 Gram 的一次物理插入

对每条边 \(e=ij\)，令
\[
\Psi_e=t_e y_i y_jF_T.
\]
其展开为
\[
\Psi_e=\sum_{\boldsymbol a:\,a_e>0}
\frac{a_e}{A!B!C!}\,
t_{12}^A t_{13}^B t_{23}^C\,v_e^{(\boldsymbol a)}.
\]
因此
\[
\boxed{
[\xi^{\boldsymbol a}]\,
\langle\Psi_e,\Psi_f\rangle_{B,z}
=\frac{a_ea_f}{(A!B!C!)^2}\,
W_{ef}^{(\boldsymbol a)}(z).
} \tag{4.1}
\]
对不同边也成立；乘上的 \(t_e,\overline{t_f}\) 正好把最终组次数对齐。

这整个 \(3\times3\) 生成矩阵还可写成显式固定有理核。令
\[
R=(I-T^*ZT)^{-1},\qquad \mathcal K=\mathcal D^{-1}.
\]
对 \(e=ij,f=k\ell\)，由消去 \(x\) 后的同一 Gaussian 的四阶 Wick 展开，
\[
\boxed{
\langle\Psi_e,\Psi_f\rangle_{B,z}
=\overline{t_e}t_f\,\mathcal K\,
\bigl(R_{ki}R_{\ell j}+R_{\ell i}R_{kj}\bigr).
} \tag{4.2}
\]
这里内积对第一变量共轭线性。四阶式也可直接逐坐标 Gaussian 积分展开证明；没有新的概率假设。

式 (4.2) 作为形式幂级数只含 \(\xi_e\)：这是 (4.1) 的组次数正交已保证的，不必独立假设各项相位抵消。取 \(t_e=\sqrt{\xi_e}>0\) 可用于代数表达；最终矩阵分母整除 \(\mathcal D^3\)。

因此完整低源 Gram \(W(z)\) 由固定 \(3\times3\) 有理核的系数明确恢复：
\[
\boxed{
W_{ef}^{(\boldsymbol a)}(z)
=\frac{(A!B!C!)^2}{a_ea_f}
[\xi^{\boldsymbol a}]\,
\langle\Psi_e,\Psi_f\rangle_{B,z},
\quad a_e,a_f>0.
} \tag{4.3}
\]
未出现随 spin 增长的完整物理层逆。

## 5. Raised Gram 与硬源交叉用同一个核生成

为了保全部回归，使用双变量核
\[
\boxed{
\mathcal K(T_L,T_R)
=\langle F_{T_L},F_{T_R}\rangle_{B,z}
=\det(I-ZT_R T_L^*)^{-1}.
} \tag{5.1}
\]
在 \(T_L=T_R=T\) 时就是 \(\mathcal D^{-1}\)。

令 \(S_e\) 为对称矩阵，其 \(ij,ji\) 元为 \(1\)、其它元为 \(0\)。沿 \(S_e\) 的 holomorphic 导数插入
\[
x_i y_j+x_j y_i.
\]
准确设置
\[
\Xi_e=t_e(x_i y_j+x_j y_i)F_T,
\]
\[
\mathcal A_e
:=\langle F_T,\Xi_e\rangle_{B,z}
=
t_e\,\left.\partial_{r_e}
\mathcal K(T,T+\sum_f r_fS_f)\right|_{r=0}, \tag{5.2}
\]
\[
\mathcal S_{ef}
:=\langle\Xi_e,\Xi_f\rangle_{B,z}
=
\overline{t_e}t_f
\left.\partial_{\overline{l_e}}\partial_{r_f}
\mathcal K(T+\sum_h l_hS_h,T+\sum_h r_hS_h)
\right|_{l=r=0}. \tag{5.3}
\]
这是明确的 \(3\times3\) 行列式求导，不是额外未定义的全层算子。分母分别整除
\(\mathcal D^2,\mathcal D^3\)。

与 (4.1) 相同的最终组次数正交给
\[
\boxed{
a_e^{(\boldsymbol a)}(z)
=\frac{(A!B!C!)^2}{a_e}
[\xi^{\boldsymbol a}]\,\mathcal A_e,
} \tag{5.4}
\]
\[
\boxed{
S_{ef}^{(\boldsymbol a)}(z)
=\frac{(A!B!C!)^2}{a_ea_f}
[\xi^{\boldsymbol a}]\,\mathcal S_{ef}.
} \tag{5.5}
\]
左边 \(a_e^{(\boldsymbol a)}(z)\) 表示硬源交叉；分母中的整数 \(a_e\) 表示边数，二者以参数标记区分。

每个系数层的联合块
\[
\begin{pmatrix}
M(z)&a(z)\\
a(z)^*&S(z)
\end{pmatrix}
\]
是真实硬源和 raised 低源的 Gram。应当先提取同一
\(\boldsymbol a\) 的系数，再作该有限源的 Schur；不能把生成函数层的逆与取系数互换。

## 6. 从生成核返回完整 MP 相位

此处的完整顶逆采用[主 spin 边界稿 §3](2026-11-14-arbitrarily-many-weight-dominant-spin-phase-bound-789f-next.md)已对任意 primitive 证明的补集身份；完整第一逆的中央投影亦见[全源 Hessian 推导](2026-11-14-central-partition-full-hessian-frame-and-phase-ward-block-789f-next.md)。这些身份先在完整层取 MP，再限制到实际源。

在实际源基
\[
\mathcal E_e=D_{s-1}^{-1}v_e,\qquad a_e>0
\]
中，全部原二次型为
\[
\boxed{
h=\frac{W(z^{-1})}{K_q},\qquad
\ell=\frac{\pi^{-1}W(z)}{K_q},\qquad
q=\frac{\pi^{-1}S(z)}{K_q}.
} \tag{6.1}
\]
第一式是完整原源度量；第二式来自真实顶补集 MP 逆；第三式来自实际
\(e_b\mathcal E\) 的中央 Gram。

完整硬源回归给
\[
\boxed{
g=\frac{\pi^{-1}}{4K_q}
\left(S(z)-a(z)^*M(z)^{-1}a(z)\right).
} \tag{6.2}
\]
\(M(z)\) 在本族中为一个正标量，括号是整个 \(d\le3\) 维源的 Schur。
中央补集在硬源与 raised 低源上符号相反，所以把正权表达换回实际倒数去权时，硬源交叉仅变号；其 Schur 正好是 (6.2)。

(6.2) 等于完整第一 MP 逆的 Gram：对实际低源 \(f\)，
\(d_b e_bf=2f\)，而 \(e_bf\) 正交投影掉整个实际硬源后恰为
\(2\mathcal J_1f\)。这里完整硬源已经由 §1 证明为一维，故无遗漏 nuisance。

实际相位完全恢复为
\[
J=h g^{-1}\ell+2g-q,
\]
\[
\boxed{
\Phi\preceq\kappa I
\iff
J^*\ell^{-1}J\preceq\kappa h
\iff
\begin{pmatrix}\kappa h&J^*\\J&\ell\end{pmatrix}\succeq0.
} \tag{6.3}
\]
所有逆现在只在至多 \(3\) 维的完整实际源上取，且来自同一系数层的物理 Gram。未用任意独立的正矩阵代替它们。

## 7. 范围与尚未支付的量化

任意三组有效 spin：

* 不满足多边形条件而低源非零的模块，已归入主 spin 边界定理；
* 满足三角条件的所有模块，准确由 \(A,B,C\ge0\) 参数化；
* 本稿对这些三角模块的全部源、全部 spin 大小和正权给同一个固定生成核，低源维数为正边数，不随边数大小继续增加。

生成核本身的 Gaussian 正性以及系数层的普通 Gram 正性，都不自动证明
(6.3)。真正仍需支付的是：在 (3.2)、(4.3)、(5.4)–(5.5) 给出的同一系数层上，硬源 Schur 与两侧源度量之间的非交换相位预算。尤其不能先在生成函数层 Schur，再把其系数称为实际 \(g\)。

本稿没有新增有限尺寸扫描，也没有将已证明的三对六位模型重复计为新正性结论。

