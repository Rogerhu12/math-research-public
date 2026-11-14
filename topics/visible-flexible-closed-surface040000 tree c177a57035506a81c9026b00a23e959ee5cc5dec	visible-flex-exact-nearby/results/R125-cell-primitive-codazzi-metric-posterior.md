# R125：利用逐格原函数相消的 Codazzi 度量后验

**状态：已证明。** 2026-11-12，fd2d / metric_closure。

本结果对 R119 的同一个实际 ODE 定义图给更细后验。它把一格中振荡的连接残差写成端点为零的准确原函数导数，加一个均值/余项，保留积分相消。没有修改实际曲面、度量或计算字段，也没有从小残差推出新的无限维精确解。全局 reach 与尾接合不由本结果自动支付。

## 1. 固定材料坐标的实际图与三个缺陷

采用 R119 的物理度量 $ds^2+a(s)^2du^2$、准确初始曲线/定向 frame，及实际定义

$$
F_s=FA,\qquad X_s=Fe_1^{std},\qquad
A=\begin{pmatrix}0&0&-l\\0&0&-m\\l&m&0\end{pmatrix}.
\tag{1}
$$

因此 $F\in SO(3)$。令

$$
B=\begin{pmatrix}0&-a'&-am\\a'&0&-an\\am&an&0\end{pmatrix},
$$

$$
H=BA+A_u-AB-B_s,\qquad
D=F_u-FB,\qquad C=X_u-aFe_2^{std}.
\tag{2}
$$

H 是反对称的**连接残差**，D 是**角 frame 缺陷**，C 是**位置切向缺陷**，三者不混用。R119 已逐项证明

$$
D_s=DA+FH,\qquad C_s=De_1^{std}.
\tag{3}
$$

其中

$$
H=a\begin{pmatrix}0&\mathcal G&\mathcal R_m\\
-\mathcal G&0&\mathcal R_n\\-\mathcal R_m&-\mathcal R_n&0\end{pmatrix}.
\tag{4}
$$

沿用 R119 的连续及角导假设；允许 l 仅在径向连续，不要求 $l_s$ 或全局 $a_{sss}$。下面所有积分、均值和辅助函数均指实际定义函数，非抽样拟合后默认误差为零。

## 2. 任意端点为零的反对称修正

在一格 $I_j=[s_j,s_{j+1}]$ 上，取关于 s 为 C1、关于 u 具有所需正则性的反对称矩阵场 Q，满足

$$
Q(s_j,u)=Q(s_{j+1},u)=0\quad\text{对全部 }u.
\tag{5}
$$

定义

$$
W=D-FQ,\qquad E=H-Q_s+[Q,A].
\tag{6}
$$

则准确有

$$
\boxed{W_s=WA+FE.}
\tag{7}
$$

**证明。** 用 (1)、(3) 求导：

$$
\begin{aligned}
W_s&=DA+FH-FAQ-FQ_s\\
&=(W+FQ)A+F(H-AQ-Q_s)\\
&=WA+F\{H-Q_s+QA-AQ\}.
\end{aligned}
$$

这就是 (7)。右乘方程的齐次传播矩阵正交，故变常数公式中没有指数范数放大。证毕。

设准确连续非负函数 $b_j,p_j,q_j$ 满足

$$
\sup_u\|E(s,u)\|_{op}\le b_j(s),\quad
\sup_u|Q(s,u)e_1^{std}|\le p_j(s),\quad
\sup_u\|Q(s,u)\|_{op}\le q_j(s).
\tag{8}
$$

若左端 $\sup_u\|D(s_j,u)\|\le d_j$、$\sup_u|C(s_j,u)|\le k_j$，则格内

$$
\|D(s,u)\|\le d_j+\int_{s_j}^s b_j(t)\,dt+q_j(s),
\tag{9}
$$

$$
|C(s,u)|\le k_j+(s-s_j)d_j
+\int_{s_j}^s(s-t)b_j(t)\,dt
+\int_{s_j}^s p_j(t)\,dt.
\tag{10}
$$

**证明。** (5) 给 $W(s_j)=D(s_j)$，由 (7) 和正交传播有
$\|W(s)\|\le d_j+\int b_j$。加回 $FQ$ 得 (9)。再将
$C_s=W e_1^{std}+FQe_1^{std}$ 积分，交换二重积分即得 (10)。证毕。

在右端 Q 准确为零，所以可逐格递推

$$
d_{j+1}=d_j+\int_{s_j}^{s_{j+1}}b_j,
$$

$$
k_{j+1}=k_j+h_jd_j+
\int_{s_j}^{s_{j+1}}(s_{j+1}-t)b_j(t)\,dt+
\int_{s_j}^{s_{j+1}}p_j(t)\,dt.
\tag{11}
$$

如果只使用常数上界 $\bar b_j,\bar p_j$，可取

$$
d_{j+1}=d_j+h_j\bar b_j,\qquad
k_{j+1}=k_j+h_jd_j+\tfrac12h_j^2\bar b_j+h_j\bar p_j.
\tag{12}
$$

辅助 Q 无需跨格 C1；各格端点值均为零即可独立使用 (11)。实际 F、X 和原输入字段保持原样。

## 3. 准确均值原函数和有限多项式版本

最直接的准确选择是

$$
\overline H_j(u)=\frac1{h_j}\int_{s_j}^{s_{j+1}}H(t,u)\,dt,
$$

$$
Q_j(s,u)=\int_{s_j}^s(H(t,u)-\overline H_j(u))\,dt.
\tag{13}
$$

则 (5) 成立，而且准确分解

$$
H=(Q_j)_s+\overline H_j,\qquad
E=\overline H_j+[Q_j,A].
\tag{14}
$$

均值必须是 (13) 的完整积分；若以数值积分求值，必须包围其误差，不以若干配点上 H 很小来替代均值。

对于实际区间算法，可先构造一个**准确定义**的反对称有限多项式 P，证明

$$
H=P+R,\qquad\sup_u\|R(s,u)\|\le\epsilon_j(s).
\tag{15}
$$

取 P 的准确均值和原函数

$$
\overline P_j=h_j^{-1}\int_{I_j}P,\qquad
Q_j=\int_{s_j}^s(P-\overline P_j).
\tag{16}
$$

则 Q 的两端仍准确为零，且

$$
E=\overline P_j+R+[Q_j,A].
\tag{17}
$$

因此有限 polynomial/Fourier 系数的均值及原函数可准确积分，只有已经明确的余项 R 另付。这里没有把 P 的原函数误写成 H 的原函数。

三维反对称矩阵还能少付一个常数。记 $\widehat v\,z=v\times z$，则

$$
\|\widehat v\|_{op}=|v|,\qquad
[\widehat q,\widehat\alpha]=\widehat{q\times\alpha}.
$$

第一式由 $(v\times z)\cdot(v\times z)=|v|^2|z|^2-(v\cdot z)^2$ 得到，第二式由向量三重积恒等式得到。故

$$
\boxed{\|[Q,A]\|_{op}\le\|Q\|_{op}\|A\|_{op}.}
\tag{18}
$$

不需要一般矩阵的因子2。于是如果 $\|\overline P_j\|\le m_j$、$\|A\|\le\alpha_j(s)$，

$$
b_j(s)=m_j+\epsilon_j(s)+\alpha_j(s)q_j(s)
\tag{19}
$$

是可直接使用的界。也可以在向量系数层直接包围
$\overline p_j+r+q_j\times\alpha$，保留更多相消和正交关系。

## 4. 固定 x、多材料图册的准确版本

实际 small01 使用 $s=S(x)$、$u=U(x,\xi)$。定义

$$
J=S_x>0,\qquad \chi=U_\xi>0,\qquad w=U_x/\chi,
\qquad \partial_x\big|_u=\partial_x-w\partial_\xi.
\tag{20}
$$

以下 F、D、C 指物理对象复合这两个图册；D 仍是 $F_u-FB$，不是 $F_\xi-FB$。令

$$
\widehat A=JA,\qquad\widehat H=JH.
$$

沿固定 u 的 x 特征线，(1)、(3) 变成

$$
\dot F=F\widehat A,\quad
\dot D=D\widehat A+F\widehat H,\quad
\dot C=JDe_1^{std}.
\tag{21}
$$

为直接消费固定 ξ 的多项式，取 $[x_j,x_{j+1}]$ 上两端恒零的 Q(x,ξ)。则

$$
\boxed{\dot W=W\widehat A+F\widehat E,\qquad
\widehat E=\widehat H-Q_x+wQ_\xi+[Q,\widehat A].}
\tag{22}
$$

证明与 §2 相同，只需用 $\dot Q=Q_x-wQ_\xi$。**额外的 $wQ_\xi$ 必须保留。**

若固定 ξ 的准确分解是 $\widehat H=P+R$，取

$$
\overline P_j(\xi)=h_x^{-1}\int_{x_j}^{x_{j+1}}P(t,\xi)\,dt,
\quad Q=\int_{x_j}^x(P-\overline P_j),
$$

则

$$
\widehat E=\overline P_j+R+wQ_\xi+[Q,\widehat A].
\tag{23}
$$

同样，P 取准确 $\widehat H$ 时 R=0。这允许先在**固定计算角**下做准确系数原函数，随后明确支付图册漂移，不需要先对每个材料角数值反解整条特征线才定义 Q。

设 $b_j(x)$ 包围 $\sup_\xi\|\widehat E\|$，$p_j$ 包围 $\sup_\xi|Qe_1^{std}|$。因为每个 x 上 ξ→u 是整圈双射，全部 supremum 也覆盖全部材料 u。格内有

$$
\|D(x,u)\|\le d_j+\int_{x_j}^x b_j(t)\,dt+q_j(x),
\tag{24}
$$

$$
\begin{aligned}
|C(x,u)|\le{}&k_j+[S(x)-S(x_j)]d_j\\
&+\int_{x_j}^x[S(x)-S(t)]b_j(t)\,dt
+\int_{x_j}^xJ(t)p_j(t)\,dt.
\end{aligned}
\tag{25}
$$

式 (25) 将 (21) 的 J 一起积分并交换顺序得到；它没有遗漏 coast chart 的物理长度比例。

实用的常数预算是

$$
\bar b_j=m_j+\bar\epsilon_j+
\bar w_j\bar q_{\xi,j}+\bar\alpha_j\bar q_j,
\qquad\bar\alpha_j\ge\|JA\|.
\tag{26}
$$

若 $J\le\bar J_j$，以 $h_x=x_{j+1}-x_j$、$h_s=S(x_{j+1})-S(x_j)$ 记，则

$$
\boxed{\begin{aligned}
d_{j+1}&=d_j+h_x\bar b_j,\\
k_{j+1}&=k_j+h_sd_j+
\bar J_j\{\tfrac12h_x^2\bar b_j+h_x\bar p_j\}.
\end{aligned}}
\tag{27}
$$

这里 $h_s$、J 和所有常数也须按实际目标/图册连续包围。以 $\bar J_jh_x$ 代 $h_s$ 是一个更粗但有效的版本。

在本题 Gauss 恒等式准确成立的情况下，

$$
\widehat H=\widehat{(-Ja\mathcal R_n,\ Ja\mathcal R_m,\ 0)},
\quad\widehat A=\widehat{(Jm,-Jl,0)}.
$$

对应固定 ξ 原函数 q 也在 xy 平面，$q\times\alpha$ 在 z 方向；可把这部分与均值、漂移的 xy 分量用平方和合并，而非无条件相加。

## 5. 从位置缺陷到准确 metric

使用 (10) 或 (25) 的格内完整界 k(s)，令 $\varepsilon(s)=k(s)/a(s)$。R119 的同一个实际图在目标正交标架中满足

$$
\boxed{\|g^{-1/2}(X^*e-g)g^{-1/2}\|_{op}
\le2\varepsilon(s)+\varepsilon(s)^2.}
\tag{28}
$$

证明仍是实际微分两列为 $(e_1,e_2+C/a)$，把 Gram 矩阵展开。moving chart 不把分母 a 换成 $aU_\xi$，因为 C 定义于原物理材料角 u。

因此全前缀证书须检查每格内部的 (25)/(28)，不能只检查节点递推值。若部分格采用 R119 的绝对残差界、其余采用本结果，两者对同一 d/k 初值作递推即可；无需重求已经有效的格。

## 6. 一个准确的三次配点残差例子

令一格的连接残差向量为

$$
h(s,u)=v(u)\,\tau(1-\tau)(\tau-\tfrac12),
\qquad\tau=(s-s_j)/h_j.
$$

它在左端、中点、右端为零，均值也准确为零，而区间内部不为零。其端点零原函数为

$$
q(s,u)=-\frac{h_j}{4}v(u)\tau^2(1-\tau)^2.
$$

从而

$$
\sup_s|q|\le h_j|v|/64,\qquad
\int_{I_j}|q|\,ds=h_j^2|v|/120,
$$

$$
\int_{I_j}|h|\,ds=h_j|v|/32.
\tag{29}
$$

所以在 $\|A\|\le\alpha$ 下，节点 frame 缺陷增量可从绝对残差的 $h_j|v|/32$ 改用 $\alpha h_j^2|v|/120$。这是保留原函数相消产生的一个明确 h 因子。

但是位置缺陷仍含 $\int|Qe_1|$。即使 A=0、均值为零，也不能据此把 C 写成零；(10) 正确保留这项。此例只说明算法能利用的结构，不能据三点残差小便认定实际残差恰为这个多项式。

## 7. 实际消费者应保存的最小证据

对实际 shared-Hermite/完整指数场，按原 knots、目标分段和图册分段形成精确分区。每格保存：

1. 准确输入及该格端点；选用的有限 P、准确均值和零端点原函数 Q 的定义；
2. 连续余项 $\widehat H-P$ 的范数界，全部保留的 Fourier 模态和完整角覆盖；
3. $Q,Q_\xi,Qe_1$ 的完整格界，$J,w,JA$ 的真实连续界；
4. (26)–(28) 的逐格/格内结果，及与前一格相同的 d/k 接口。

本会话实际 small01 已有准确初始 $d_0\le1.638645511272696\cdot10^{-16},k_0=0$、全前缀 η/ζ Bernstein 界，以及512模固定图册的严格 Fourier 包。其原生场定义和证明位于 `notes/2026-11-12-fd2d-metric-gc-native-field-and-inlet-proof.md`。

这些输入并不宣称上述每格余项已经全部计算。本结果给出了无需额外 C³ 假设、无需改变实际图、可以直接认证原函数相消的完整后验。浮点拟合均值或少量角点只能提供诊断，不能填入“连续余项已付”的字段。
