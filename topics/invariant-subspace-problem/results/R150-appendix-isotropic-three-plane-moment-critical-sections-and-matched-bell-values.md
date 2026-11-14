# R150 附录：两个全等向三维平面的完整矩临界截面与匹配 Bell 值

日期：2026-11-13（UTC）。作者：normal_rebuild / Astra-ISP-1cf8c51d。

状态：**已证明。** 本稿准确处理下述两个指定三维平面上的全部有限 ordinary 矩临界截面，包含全部 $h\ge2$；没有声称它们穷尽完整临界簇，也没有从截面消失推出全局 Jacobian 归属或新的循环性。

本稿接[六模式完整第三矩消元](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)。原平方证明选出的三个 first 方向并非只杀掉两个孤立的已知点：它们杀掉下面两个平面上、任意高次的整个允许临界截面族。对立方，完整第三矩张量的准确余因子是一次式。

## 1. 原六模式与完整有限矩泛函

沿用实化坐标 $x_j=i^j y_j$ 及
$$
F_0(y)=\frac12y^{\mathsf T}Ky,\qquad
K=\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix},\qquad
v(z)=(1,z,z^2,z^3,z^4,z^5)^{\mathsf T}.
$$
准确有 $F_0(v(z))=0$。这里的全部转置均为复双线性代数转置，不是 Hilbert 伴随。

固定 $h\ge2$。在一个完整 ordinary 显示点 $(y,W)$ 上，定义次数不超过 $2h$ 的有限线性泛函
$$
\Lambda(P)=\mathcal Q_P(y,W).
$$
它的截断指数生成函数为
$$
M_\Lambda(t)=
\exp\!\left[
y\cdot t+
\sum_{d=2}^{2h}\frac{(-2)^{d-1}}{d!}
\sum_{m=0}^{5d}W_{d,m}
\sum_{i_1+\cdots+i_d=m}t_{i_1}\cdots t_{i_d}
\right]
\pmod{\deg t>2h}.
\tag{1.1}
$$
这个定义只涉及有限多项式和有限系数。没有要求 $\Lambda$ 为正态、正测度或真实联合谱值。

设 $E:\mathbb C^3\to\mathbb C^6$ 单射，$W_E=\operatorname{Ran}E$。本稿称 $\Lambda$ **支撑于 $W_E$**，准确意思是
$$
\Lambda(P)=0
\quad\text{当 }P|_{W_E}=0\text{ 且 }\deg P\le2h.
\tag{1.2}
$$
因此存在唯一次数不超过 $2h$ 的三变量泛函 $\widetilde\Lambda$，使
$$
\Lambda(P)=\widetilde\Lambda\big(P(E\xi)\big).
\tag{1.3}
$$
“唯一”使用 $E$ 有左逆；每个三变量多项式都可写成某个 $P(E\xi)$。等价地，(1.1) 可写成某个截断级数 $\widetilde M(E^{\mathsf T}t)$。

这是一项对**完整有限矩泛函**的假设；仅有一次坐标 $y\in W_E$ 远远不够。

## 2. 两个准确的有理全等向平面

定义
$$
E_+=\begin{pmatrix}
1&0&0\\0&1&0\\0&0&1\\
8/5&-32/5&5\\
8&-152/5&93/5\\
744/25&-2776/25&313/5
\end{pmatrix},
$$
$$
E_-=\begin{pmatrix}
1&0&0\\0&1&0\\0&0&1\\
-864/5&-864/5&-27\\
23328/5&22464/5&2781/5\\
-2402784/25&-2286144/25&-52623/5
\end{pmatrix}.
\tag{2.1}
$$
它们的前三行均为单位矩阵，故秩恰为三。直接乘法给
$$
E_+^{\mathsf T}KE_+=E_-^{\mathsf T}KE_-=0.
\tag{2.2}
$$
所以 $F_0$ 在两个平面 $W_\pm=\operatorname{Ran}E_\pm$ 上都恒零。

令
$$
P_+(z)=z^3-5z^2+\frac{32}{5}z-\frac85,
\qquad
P_-(z)=z^3+27z^2+\frac{864}{5}z+\frac{864}{5}.
\tag{2.3}
$$
各 $E_\pm$ 的行正是递推
$$
a_{n+3}=s_\pm a_{n+2}-p_\pm a_{n+1}+q_\pm a_n
$$
从前三项展开的矩阵，其中
$$
(s_+,p_+,q_+)=(5,32/5,8/5),\qquad
(s_-,p_-,q_-)=(-27,864/5,-864/5).
$$
两三次式的判别式分别为 $3488/125$ 与 $153684864/125$，均非零。
故若 $z_1,z_2,z_3$ 是相应三次式的三个根，则
$$
W_\pm=\operatorname{span}\{v(z_1),v(z_2),v(z_3)\}.
\tag{2.4}
$$
式 (2.2) 同时说明这三个物理方向两两 $K$-正交。

更关键的是完整一次投影的精确分解
$$
\boxed{
E_\pm^{\mathsf T}K v(z)=P_\pm(z)\,\psi_\pm(z),
}
\tag{2.5}
$$
其中
$$
\psi_+(z)=
\begin{pmatrix}-z^2-32/5\\128/5-z^2\\5z-19\end{pmatrix},
\qquad
\psi_-(z)=
\begin{pmatrix}-z^2+32z+3456/5\\-z^2+32z+3296/5\\5z+77\end{pmatrix}.
\tag{2.6}
$$
写 $\psi_\pm(z)=L_\pm(1,z,z^2)^{\mathsf T}$，其系数矩阵行列式分别为 $-160$ 与 $160$，故二者都可逆。

## 3. 投影曲线的唯一二次关系

置
$$
C_+=\begin{pmatrix}
279&121&608\\121&-521&-608\\608&-608&-1024
\end{pmatrix},
\qquad
C_-=\begin{pmatrix}
-1769&1369&5024\\1369&-969&-5024\\5024&-5024&-1024
\end{pmatrix},
$$
$$
Q_\pm(u)=u^{\mathsf T}C_\pm u.
\tag{3.1}
$$
直接展开得到
$$
Q_\pm(\psi_\pm(z))=0,
\qquad \det C_+=\det C_-=163840000\ne0.
\tag{3.2}
$$
下面使用的不是数值拟合，而是准确的齐次理想等式：对任意齐次 $T\in\mathbb C[u_0,u_1,u_2]$，
$$
\boxed{
T(\psi_\pm(z))\equiv0
\quad\Longleftrightarrow\quad Q_\pm\mid T.
}
\tag{3.3}
$$

证明如下。先用可逆线性换元 $u=L_\pm a$，化到 $(a_0,a_1,a_2)=(1,z,z^2)$。模 $a_0a_2-a_1^2$ 后，任意齐次多项式可约成不同时含正次 $a_0$ 与 $a_2$ 的单项式之和。在固定总次数 $n$，这些余下的 $2n+1$ 个单项式代入 $(1,z,z^2)$ 后给 $1,z,\ldots,z^{2n}$，次数各异。因此代入恒零当且仅当余式为零，齐次核理想恰为 $(a_0a_2-a_1^2)$。再由 (3.2) 和二次核空间为一维，非零 $Q_\pm$ 恰是该生成元的非零倍数，得到 (3.3)。这个证明也保留了射影无穷端点。

## 4. 支撑平面上的完整临界条件

设 $\Lambda$ 是 (1.1) 给出的任意允许 finite ordinary 矩泛函，并且满足 (1.2)，支撑于固定一个 $W_\pm$。定义其完整第 $h$ 次矩形式
$$
T_h(u)=\widetilde\Lambda\big((u\cdot\xi)^h\big).
\tag{4.1}
$$
它是三变量齐次 $h$ 次多项式。所有低矩、交叉矩和 ordinary 累积量都包含在 $T_h$ 中。

**定理。** 在上述准确支撑假设下，$(y,W)$ 是完整 $\mathcal Q_{F_0^h}$ 的零临界点，当且仅当
$$
\boxed{Q_\pm\mid T_h.}
\tag{4.2}
$$

证明。对任意物理方向 $v(z)$，因 $F_0(v(z))=0$，
$$
F_0(Y+t v(z))=F_0(Y)+t\,v(z)^{\mathsf T}KY.
$$
因此
$$
(v(z)\cdot\nabla)^d F_0^h
=\frac{h!}{(h-d)!}F_0^{h-d}
\big(v(z)^{\mathsf T}KY\big)^d\quad(0\le d\le h),
\tag{4.3}
$$
且 $d>h$ 时为零。

对 $d<h$，右侧因含正次 $F_0$ 而在 $W_\pm$ 上恒零，故被 $\Lambda$ 送为零。$F_0^h$ 自身亦然。一次方向 $v(z)$ 张成整个六维空间，所以所有一次显示偏导都已核验为零。对每个二阶及更高显示矩，完整 ordinary 恒等式
$$
\partial_{W_{d,m}}\mathcal Q_{F_0^h}
=\frac{(-2)^{d-1}}{d!}\,\mathcal Q_{\mathcal D_{d,m}F_0^h}
$$
把其导数转成 (4.3) 的对应 $z$ 系数；这里 $\mathcal D_{d,m}$ 保留全部有序指标。于是所有 $d<h$ 与 $d>h$ 的导数都严格为零，唯一剩下的是 $d=h$ 的整个系数列。

由 (1.3)、(2.5)，最后这列全零准确等价于
$$
0\equiv\Lambda\big((v(z)^{\mathsf T}KY)^h\big)
=P_\pm(z)^h T_h(\psi_\pm(z)).
$$
$P_\pm$ 非零，故它等价于 $T_h(\psi_\pm(z))\equiv0$。式 (3.3) 即给 (4.2)。这核验了完整显示空间的全部导数，没有遗漏高阶或合并坐标。证毕。

特别，在立方情形，准确有
$$
\boxed{
\text{该支撑族中的完整临界条件}
\quad\Longleftrightarrow\quad
T_3(u)=Q_\pm(u)\,\ell(u)
}
\tag{4.4}
$$
其中 $\ell$ 是某个一次齐次式，包括零式。不能把这个 $T_3$ 换成均值的一次符号立方。

## 5. 原平方候选杀掉两个平面的全部匹配矩值

任取固定 $r\in\mathbb C^6$。在完整显示点上，匹配 first Bell 的准确值为
$$
\mathcal Q_{(r\cdot Y)^h}(y,W)
=\Lambda((r\cdot Y)^h)
=T_h(E_\pm^{\mathsf T}r).
\tag{5.1}
$$
所以，若
$$
Q_\pm(E_\pm^{\mathsf T}r)=0,
\tag{5.2}
$$
则 (4.2) 保证 (5.1) 在该平面的**每一个**允许完整临界点上为零，任意 $h\ge2$ 均成立。

对原方向 $r=(A,B,0,0,0,1)$，直接用 (2.1)、(3.1) 得
$$
Q_+(E_+^{\mathsf T}r)=-f(A,B),\qquad
Q_-(E_-^{\mathsf T}r)=g(A,B),
\tag{5.3}
$$
其中恰为旧平方节点的两个二次式
$$
f=-279A^2-242AB-65856A+521B^2-46784B+271360,
$$
$$
g=-1769A^2+2738AB-16087680A-969B^2+19820160B+140341248.
$$
取任意一个三次式
$$
3725d^3-43931504d^2+6080833024d+52565262336=0
$$
的实根，并置
$$
A=-\frac{521d^2-46784d+271360}{160(5d-704)},\qquad B=A+d.
\tag{5.4}
$$
[原精确平方证明](R150-appendix-six-mode-exact-jacobian-jets-and-all-square-fibers.md)已证明三个实根分别位于 $(-9,-8)$、$(144,149)$、$(11600,11700)$，分母非零，且 (5.4) 准确满足 $f=g=0$。因此同一三个 $r$ 同时满足两个平面的 (5.2)。

回到原坐标的 first 仍为
$$
a=iA U_1+B U_2+U_6=i(r\cdot y).
$$
其完整 Bell $h$ 次只给 (5.1) 乘非零标量 $i^h$。既有 first 空谱和单 first 完整 Bell 有界逆仍适用；这里没有改变实际物理行、指数权或原自然域。

在 $h=3$ 时，完整第三矩 Schur 换元的临界点满足 $Z=0$，故 $S_r=B_r$。本稿因此证明：这三组选取的 $B_r$ 在上述两个平面的**全部**允许立方临界截面上消失。它没有证明 $B_r$ 在其余临界点上消失，更没有仅由这个受限消失断言 $B_r^N\in(\nabla R_3)$。

## 6. 这个支撑条件确有完整 ordinary 实例

取 (2.4) 中的三个根和形式独立的三个标量 $X_1,X_2,X_3$。给每个 $X_i$ 任意有限累积量 $\kappa_{d,i}$（不作正性要求），令
$$
Y=\sum_{i=1}^3 X_i v(z_i).
$$
其生成函数对数是
$$
\sum_{d=1}^{2h}\frac1{d!}\sum_i\kappa_{d,i}
\big(v(z_i)\cdot t\big)^d.
$$
于是它是允许的完整显示点：
$$
y_j=\sum_i\kappa_{1,i}z_i^j,\qquad
W_{d,m}=\frac1{(-2)^{d-1}}\sum_i\kappa_{d,i}z_i^m\quad(d\ge2).
\tag{6.1}
$$
全部累积量都保留真实合并键，生成函数又完全经 $E_\pm^{\mathsf T}t$ 因子化，所以 (1.2) 自动成立。是否临界，仍须且只须 (4.2)，并非任意累积量都临界。

这同时说明本稿覆盖的是有限 ordinary 矩参数的整族；不是只重复两个旧平方节点，也不要求该形式泛函由一个正概率分布实现。

## 7. 可复算的有限数据与仍开的问题

[自含有理核验脚本](../notes/2026-11-13-isotropic-three-plane-moment-sections-verify.py)只用 Python 标准库的 `Fraction`，逐项核验 (2.2)、(2.5)、(3.2)、两个 $\det L_\pm$、三次判别式和 (5.3)。其余结论由上述完整代数证明直接推出。

当前未付的是一般完整临界点的支撑分类，以及由完整全局 Jacobian 理想得到匹配 Bell 的自然幂证书。平面支撑不许从一次坐标、少数矩、有限域点数或一个局部 Hessian 核推断。原六模式 $F^3$ 零参数、其他高次目标与普通 ISP 均保持开放。
