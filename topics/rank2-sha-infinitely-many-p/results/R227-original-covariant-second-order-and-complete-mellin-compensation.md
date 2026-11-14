# R227 — 原两列的固定协变二阶分解、有限 Lamé 块与完整 Mellin 补偿

日期：2026-11-13。**状态：以下固定有理分解、两个实际有限协变空间及保原 theta 的完整 Mellin 等式已证明。没有证明这些空间对原中央泛函闭合，也没有由两个有理单位推出原中央非零。**

本篇继续 [R226](R226-actual-double-descent-and-torsion-central-transport.md) 的实际二挠运输。
原 $A,B,\Theta,c$ 全部保留。固定二阶分解中的单位现在确实出现在原 theta 恒等式里；
普通导数与协变导数之间的一、二阶补偿也全部写出。

## 1. 原连接与两个固定有理单位

记
$$
\Theta=\vartheta(2z)^{17},\quad
V=\frac{\Theta'}{\Theta},\quad
\nabla=\partial_z-V,\quad
\nu=-X/Y,\quad
\xi=\nu^4=q(1-4q),\quad
\phi=2\sqrt q,\quad \rho=\sqrt{1-4q}.
$$
所有根均取原点既定首项。原微分规范给
$$
q'=4\nu^3,\quad \nu'=1-8q,\quad
(\nu')^2=1-16\nu^4,\quad \nu''=-32\nu^3.                   \tag{1}
$$
若 $U=\vartheta'/\vartheta$，则原 sigma 恒等式给 $U'=u^2$。
因为 $u(2z)=2\nu$，准确有
$$
V=34U(2z),\qquad V'=272\nu^2.                              \tag{2}
$$
于是对每个原有理因子 $f$，
$\nabla(\Theta f)=\Theta f'$、$\nabla^2(\Theta f)=\Theta f''$。
这里的 $V$ 是同一原 theta 连接，不以普通导数替代它。

定义两个固定多项式
$$
P_A(\xi)=
-\frac{17}{1155}-\frac{53}{3850}\xi
+\frac{16}{4125}\xi^2-\frac{128}{525}\xi^3,                 \tag{3}
$$
以及用 $t=4q$ 写的
$$
\begin{aligned}
P_B(t)={}&-\frac{2261}{81920}
+\frac{953}{102400}t-\frac{2887}{192000}t^2
+\frac{1501}{22400}t^3\\
&-\frac{49}{600}t^4+\frac{101}{2310}t^5-\frac4{455}t^6.
\end{aligned}                                             \tag{4}
$$
令
$$
\beta_A=\frac{34}{1155},\qquad
\beta_B=\frac{2261}{81920}.
$$
两者对每个目标 $p>19$ 都是单位。

**固定实际二阶分解：**
$$
\boxed{\quad
A=\nabla^2\bigl(\Theta\nu^2P_A(\xi)\bigr)+\beta_A\Theta,
\qquad
B=\frac14\nabla^2\bigl(\Theta\phi P_B(4q)\bigr)
       +\beta_B\Theta\rho.
\quad}                                                     \tag{5}
$$
所有项是同一原次数六十八 theta 截面；没有先删掉公共 theta。

### 1.1 第一列的证明

由 (1)，
$$
(\nu^2P(\xi))''=\mathscr D_AP(\xi),
$$
其中
$$
\mathscr D_A=
16\xi^2(1-16\xi)\partial_\xi^2+
(28\xi-576\xi^2)\partial_\xi+2-96\xi.                       \tag{6}
$$
对单项式，
$$
\mathscr D_A\xi^n
=2(4n+1)(2n+1)\xi^n
 -32(4n+3)(2n+1)\xi^{n+1}.                                \tag{7}
$$
把 (3) 代入，即得到
$$
\mathscr D_AP_A+\beta_A
=\xi+\frac{48}{5}\xi^2-\frac{256}{5}\xi^3+\frac{4096}{5}\xi^4
=a_0(q).
$$
这证明 (5) 的第一式。

也可用固定余核泛函
$$
\lambda_A(\xi^n)=\frac{(1/4)_n}{16^n(3/4)_n}
$$
直接识别常数。由 (7)，$\lambda_A\mathscr D_A=0$，
而 $\lambda_A(a_0)=34/1155$。
该计算只认定固定二阶余类，不宣称它就是原中央泛函。

### 1.2 第二列与原 trace 单位的同一性

对 $f=\phi b(q)$，(1) 给
$$
f''=4\rho\,\mathscr D_{1/2}b,\qquad
\mathscr D_{1/2}
=8q^2(1-4q)\partial_q^2+
 (14q-80q^2)\partial_q+1-16q.                              \tag{8}
$$
因此
$$
\mathscr D_{1/2}q^n
=(4n+1)(2n+1)q^n
 -16(n+1)(2n+1)q^{n+1}.                                  \tag{9}
$$
固定泛函
$$
\lambda_B(q^n)=\frac{(1/4)_n}{4^n n!}
$$
准确杀掉 (9)。从最高次逐项解 $\mathscr D_{1/2}P=b_0-\beta$，
得到 (4)，且
$$
\beta=\lambda_B(b_0)=\frac{2261}{81920}.
$$
这就是 R207 原裸全迹的同一个有理数，而非另选一个单位参考。
代入原 $\Theta$ 后得到 (5) 第二式。

在 $t=4q$ 变量中，(9) 的对角为 $(4n+1)(2n+1)$、
升阶系数为 $-4(n+1)(2n+1)$；这也直接核对 (4) 全部系数。
所有新分母的素因子均不超过 $13$，因此没有隐藏的目标素数例外。

## 2. 两个真正的有限 Lamé 块

有限的是协变算子，普通 $\partial_z$ 仍会产生 $V$。
两个原列对应的势不同，以下分别保留。

### 2.1 与原 A 匹配的九维块

令
$$
\mathscr L_{16}=\nabla^2+4352\nu^2.
$$
它保持原固定空间
$$
\boxed{\quad
\mathcal W_A=
\Theta\,\mathbf Q[\xi]_{\le4}
\ \oplus\
\Theta\nu^2\,\mathbf Q[\xi]_{\le3}.
\quad}                                                     \tag{10}
$$
对第一块，
$$
\mathscr L_{16}(\Theta\xi^n)
=\Theta\nu^2\left(
4n(4n-1)\xi^{n-1}
 +(4352-64n(4n+1))\xi^n
\right).
$$
$n=4$ 的最高项准确为零。对第二块，
$$
\mathscr L_{16}(\Theta\nu^2P)
=\Theta(\mathscr D_AP+4352\xi P),
$$
次数至多四。这证明 (10)。

在基
$\Theta(1,\xi,\ldots,\xi^4)\oplus
\Theta\nu^2(1,\xi,\ldots,\xi^3)$ 中，上下两个非零矩阵块分别为
$$
\begin{pmatrix}
2&0&0&0\\
4256&30&0&0\\
0&3680&90&0\\
0&0&2592&182\\
0&0&0&992
\end{pmatrix},
\qquad
\begin{pmatrix}
4352&12&0&0&0\\
0&4032&56&0&0\\
0&0&3200&132&0\\
0&0&0&1856&240
\end{pmatrix}.                                             \tag{11}
$$
原 $A$ 及 (5) 的伴随截面都在这个实际空间中。

事实上原 $A$ 本身循环。取整数向量
$$
5A=(0,5,48,-256,4096;0,0,0,0).
$$
由 (11) 形成九个 Krylov 列
$5A,\mathscr L_{16}(5A),\ldots,\mathscr L_{16}^8(5A)$。
其行列式模固定辅助素数 $13$ 为 $10$。
一个可直接复核的消元证书如下：行号从零起，
交换 $(0,1),(1,5),(3,6),(5,7),(7,8)$ 后，
逐列消元主元为
$$
(5,8,12,12,5,6,11,11,1)\pmod{13}.
$$
带交换符号的乘积是 $10$。因此有理秩确为九。
这个固定辅助计算只证明有理矩阵秩，不是目标 $p$ 扫描或中央非零证据。

### 2.2 与原 B 及其真正二挠运输匹配的十六维块

令
$$
\mathscr L_{15}=\nabla^2+3840\nu^2.
$$
它保持
$$
\boxed{\quad
\mathcal W_B=
\Theta\rho\,\mathbf Q[q]_{\le7}
\ \oplus\
\Theta\phi\,\mathbf Q[q]_{\le7}.
\quad}                                                     \tag{12}
$$
准确公式为
$$
\mathscr L_{15}(\Theta\phi b)=4\Theta\rho\,T_1b,\qquad
\mathscr L_{15}(\Theta\rho a)=4\Theta\phi\,T_0a,
$$
$$
T_1=
8q^2(1-4q)\partial_q^2+
(14q-80q^2)\partial_q+1+1904q,
$$
$$
T_0=
2q(1-4q)^2\partial_q^2+
\frac12(3-40q)(1-4q)\partial_q+477-1904q.                    \tag{13}
$$
这里 $T_0=\tau T_1\tau$，$\tau:q\mapsto1/4-q$。
对 $q^n$，$T_1$ 的对角为 $(4n+1)(2n+1)$，
升阶为 $1904-32n^2-48n$；
$T_0$ 的降阶为 $n(4n-1)/2$，对角为
$477-16n^2-10n$，升阶为前者的相反数。
两个升阶在 $n=7$ 都准确为零，证明 (12)。

原 $B$、R226 的 $\mathcal T_RB$、$S$、参考 $\Theta\rho$，
以及 (5) 的第二个伴随截面全部在 (12) 中。
这不是只有 $B,\mathcal T_RB,S$ 的小块。具体令 $t=4q$，
$T:t\mapsto1-t$，$M=T_1$ 的矩阵为对角
$(4k+1)(2k+1)$、次对角
$480-4(2k+1)(k+1)$ 的整数双对角矩阵。
原整数多项式向量是
$$
b=(0,5,-18,140,-400,496,-288,64)
=20b_0(t/4).
$$
由 $b,(MT)b,\ldots,(MT)^7b$ 形成的行列式模辅助 $13$ 为 $2$。
只交换零起行号 $(0,1)$ 后，消元主元为
$$
(5,12,10,7,3,11,10,10)\pmod{13}.
$$
故其有理秩八。分解成 $\tau$ 的正、负两块，
$\mathscr L_{15}$ 分别作用为 $4MT,-4MT$，
所以原 $B,\mathcal T_RB$ 联合生成整个十六维空间。

更小的二列闭合已经被固定准确系数排除：
$b,Tb-b,MTb$ 的前三行 minor 是 $16204\ne0$。
没有据此排除原完整 Mellin 泛函另有特殊关系。

## 3. 普通导数及乘法的完整 Mellin 规则

以下令 $p=4r-1>19$、$d=p+1$、$v=z^d$，
$c=68k_r$ 始终取原共同 gauge，$v_p(c)=-1$。
使用同一完整变换
$$
\mathcal J(F;u)=
\sum_{h\ge0}[z^{dh}](e^{-cv}F)c^{-h}(u)_h.                \tag{14}
$$
它在非负整数 $k$ 的准确插值为
$$
\mathcal J(F;k)=k!c^{-k}[z^{dk}]F.
$$
记 $\mathcal E=z\partial_z$。对下文所有实际函数，有
$$
\boxed{\quad
\mathcal J(\mathcal EF;u)=du\,\mathcal J(F;u),\qquad
\mathcal J(cvF;u)=u\,\mathcal J(F;u-1).
\quad}                                                     \tag{15}
$$
第二式再迭代给
$\mathcal J(c^2v^2F;u)=u(u-1)\mathcal J(F;u-2)$。
这些都是同一完整变换中的规则，不是函数乘法与 Mellin 乘法的交换。

证明先在所有 $k\ge0$ 用准确系数插值；两边在同一个闭单位盘解析，
非负整数在 $\mathbf Z_p$ 稠密，故解析唯一性给 (15)。
下节单独支付所使用函数的解析性，特别不把 $V$ 的无限乘法无证当成有界运算。

## 4. 原 V 补偿的准确完整公式

把 (5) 统一写成
$$
A_j=\frac14\nabla^2\mathcal C_j+\beta_jH_j,
\quad j=A,B,
$$
其中
$$
\begin{aligned}
\mathcal C_A&=4\Theta\nu^2P_A(\xi),& H_A&=\Theta,\\
\mathcal C_B&=\Theta\phi P_B(4q),& H_B&=\Theta\rho.
\end{aligned}
$$
令
$$
G_j=z^{-2}\mathcal C_j,\qquad
G_j(0)=-2\beta_j,\qquad W=zV.
$$
所有 $\mathcal C_j$ 都确实在原点至少二阶零，
所以这里除 $z^2$ 是实际形式 germ 的合法操作；
$G_j$ 不被冒称为另一个全局 theta 截面。

直接展开协变导数并用 (15) 分部积分，得到
$$
\boxed{\quad
\begin{aligned}
\mathcal J(\nabla^2\mathcal C_j;u)
={}&(du+1)(du+2)\mathcal J(G_j;u)\\
&-2(du+1)\mathcal J(WG_j;u)
+\mathcal J((W^2+z^2V')G_j;u).
\end{aligned}
\quad}                                                     \tag{16}
$$

完整代数证明如下：
$$
\nabla^2(z^2G)
=(\mathcal E+1)(\mathcal E+2)G
 -2W(\mathcal E+2)G+(W^2-z^2V')G.
$$
又
$\mathcal E(WG)=W\mathcal EG+(\mathcal EW)G$，
$\mathcal EW=W+z^2V'$。
因此把 $W\mathcal EG$ 改写为整体 Euler 导数后，
补偿项准确变成 (16) 中的 $W^2+z^2V'$。
不能把这个正号换回未分部积分的负号，也不能删掉 $W$ 项。

### 4.1 无除法的收敛证明

置
$$
\widehat\Theta=e^{-cv}\Theta,\qquad
g_j=G_j/\Theta.
$$
这里 $g_j$ 是固定的椭圆有理 germ 除以其已付的 $z^2$，
在原点正则。
R54 的同一残余盘
$R=p^{-1/(2p)}$ 上，$\widehat\Theta$、$g_j$ 及所需导数有界。
除 $z^2$ 只改变固定 Gauss 常数，不改变随 $h$ 增长的指数。

事实上 (16) 所需的乘积可以不除 $\widehat\Theta$ 来定义：
$$
e^{-cv}WG_j
=z\bigl(\widehat\Theta'+cdz^{d-1}\widehat\Theta\bigr)g_j,
$$
$$
e^{-cv}(W^2+z^2V')G_j
=z^2 e^{-cv}\Theta''\,g_j.
$$
右边只包含 $\widehat\Theta$ 的至多二阶导数及有限个 $cv$ 因子，
所以在同一盘有界。没有使用指数在整个单位盘的收敛，也没有假设一个未经证明的全局 theta 逆函数。

若一个残余的 Gauss 范数为 $C_R$，
其第 $dh$ 系数乘 $c^{-h}$ 的范数至多
$$
C_R\,p^{-h+dh/(2p)}
=C_R\,p^{-(p-1)h/(2p)}.
$$
这随 $h$ 几何趋零；$(u)_h$ 的整系数 Gauss 范数至多一。
因此 (14) 中每一所用函数都定义同一个 Tate 盘上的解析函数，
(15)–(16) 及其导数均合法。

## 5. 完全显式的有限差式与共同指数的准确抵消

从 (16) 中分离原共同指数。
令
$$
W_0=W-dcv,\qquad
\mathcal F_j(u)=\mathcal J(G_j;u),
$$
$$
\mathcal G_j(u)=\mathcal J(W_0G_j;u),\qquad
\mathcal H_j(u)=
\mathcal J((W_0^2+\mathcal EW_0-W_0)G_j;u).
$$
这些补偿再次有无除法表达
$$
e^{-cv}W_0G_j=z\widehat\Theta' g_j,\qquad
e^{-cv}(W_0^2+\mathcal EW_0-W_0)G_j
=z^2\widehat\Theta''g_j.                                  \tag{17}
$$
所以它们保留同一实际 $\widehat\Theta$，没有新自由变量。

用 (15) 得到
$$
\boxed{\quad
\mathcal J(A_j;u)
=\beta_j\mathcal J(H_j;u)
 +\frac14\mathscr P_d(\mathcal F_j,\mathcal G_j,\mathcal H_j;u),
\quad}                                                     \tag{18}
$$
其中
$$
\begin{aligned}
\mathscr P_d(F,G,H;u)={}&
(du+1)(du+2)F(u)
+du(d-3-2du)F(u-1)\\
&+d^2u(u-1)F(u-2)
-2(du+1)G(u)+2duG(u-1)+H(u).
\end{aligned}                                             \tag{19}
$$
本式是固定伴随 germ 的三个完整函数与有限次平移，
不是首层截断，也没有遗失原中央之后的尾。

所有纯常数贡献可以准确看清：
$$
\mathscr P_d(F_0,0,0;u)=2F_0
$$
对整个变量 $u$ 恒成立，而不是只模 $p$。
本篇 $F_0=G_j(0)=-2\beta_j$，故这个贡献是 $-4\beta_j$。
如果仅保共同 Gaussian 和参考的质量一，
它恰与 (18) 的 $\beta_j$ 抵消。
所以两个固定有理单位均没有形成一个未被支付的加性中央单位。

特别，对 (18) 求导得到保留全部连接残差的准确条件
$$
\boxed{\quad
\begin{aligned}
4\mathcal J'(A_j;0)={}&
4\beta_j\mathcal J'(H_j;0)+2\mathcal F_j'(0)\\
&+d(d-3)\bigl(\mathcal F_j(-1)-\mathcal F_j(0)\bigr)
-d^2\bigl(\mathcal F_j(-2)-\mathcal F_j(0)\bigr)\\
&-2\mathcal G_j'(0)+2d\mathcal G_j(-1)+\mathcal H_j'(0).
\end{aligned}
\quad}                                                     \tag{20}
$$
这里 $\mathcal G_j(0)=\mathcal H_j(0)=0$；
常数 $\mathcal F_j(0)$ 的抵消已准确完成。
(20) 的负整数值是完整解析函数值，不能无证换成单个正权的经典临界 $L$ 值。

## 6. 原首行 p² 与 K 的准确有限接口

(16) 的同一代数在任意整数权 $n$ 给特征零系数恒等式
$$
\begin{aligned}
[z^n]A_j={}&\beta_j[z^n]H_j\\
&+\frac14\left(
(n+1)(n+2)[z^n]G_j
-2(n+1)[z^n](WG_j)
+[z^n]((W^2+z^2V')G_j)
\right).
\end{aligned}                                             \tag{21}
$$
取 $n=d,2d$，就是原两行的有限、可准确计算的协变运输。

各个右侧项可能有负 $p$ 层；
第二权甚至可能在分项中出现两层。
必须先按 (21) 形成原 $R_1$ 和原 raw $R_2$，
再取整组合
$\widehat R_2=\mathrm{raw}R_2-cR_1$。
在原 $R_1\in pO$ 后，才使用
$$
K=\overline{\mathrm{raw}R_2-2cR_1}.
$$
因此 (21) 保留第一行模 $p^2$，没有把它降成模 $p$ 的零向量，
也没有在 $p^{-1}O$ 或 $p^{-2}O$ 中提前取普通约化。
所有系数均来自固定有理 germ；需要时可直接按有理数计算，避免精度误判。

R226 已执行的原 $p43$ 校准仍给第一行
$(899,1683)\bmod43^2$、第二整行 $(22,2)\bmod43$；
原列 $B-20A$ 的 $u=8,K=12$ 没有改变。
本篇不增加目标素数计算。

## 7. 实际已付范围与继续的算术接口

(5) 把 R207 的固定 trace 单位送进了原 $B$ 的真实 theta 恒等式，
并且给了原 $A$ 的另一个固定单位。
(10) 和 (12) 是原两列的实际有限协变空间；
其势分别为 $4352\nu^2$ 和 $3840\nu^2$，不能冒称同一个标量闭包。
原 $A$ 在九维块中循环，原 $B$ 与其真实二挠运输联合生成十六维块。

但是普通导数会产生 $V$，其完整中央作用已经由
(16)–(20) 明确付出。
有限协变空间的闭合，不等于原标量投影、Euler 观测或 Mellin 行的闭合。
尤其不能从原两条中央导数为零，直接推出整个九维或十六维空间的中央导数都零。

下一项具体剩余是识别 (20) 中同一个实际伴随 germ 和
$\widehat\Theta',\widehat\Theta''$ 补偿的完整算术行，
或在原首行失败下直接证明 (21) 形成的 $K$ 不全零。
R226 已识别的 $\mathcal T_RB$ 属于同一 E34 的 $m\equiv2\pmod4$ 权值行；
(4) 的伴随多项式并不等于该单一有限向量，
所以不能只凭同次数或相邻权，就为它套用一个已知秩零或非中心临界非零结论。
