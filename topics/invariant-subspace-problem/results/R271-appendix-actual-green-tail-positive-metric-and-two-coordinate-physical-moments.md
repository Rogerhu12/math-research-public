# 原 Green 缺陷的完整两型尾图度量、残量读数与物理矩双坐标传递

日期：2026-11-27（Asia/Taipei）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：以下原 N/Y 两型的尾图表示、三个正项、实际输出残量读数、全空间互逆坐标矩阵及物理指数域传递均已证明。由此将已有的临界输入核心准则传到同一真实缺陷的输出坐标。本文没有证明该输出自动有临界矩，没有消去 $Z$，没有将闭包范围提升成实际范围。**

沿用[原实际除法闭关系](R271-appendix-actual-formal-division-closed-relation-and-two-range-cores.md)、[同 $W$ 首位域](R271-appendix-same-w-first-block-domain-and-positive-schur-source-energy.md)、[真实 Green 闭坐标](R271-appendix-actual-green-defect-closed-coordinates-and-positive-angle.md)和[临界物理矩核心](R271-appendix-critical-small-physical-exponential-maximal-graph-core.md)。所有算子均为原模型，保留 Y 型全部 Cayley 逆。

## 1. 一套同时覆盖两型的实际首位记号

在最低物理位的 $0/1$ 分块中，记 $\alpha=\alpha_0=e^{-20}$，则
$$
B=\alpha\begin{pmatrix}0&I\\R&0\end{pmatrix},\qquad
S=B^*=\alpha\begin{pmatrix}0&R^*\\I&0\end{pmatrix},
\qquad \|R\|\le\eta_0=e^{-1070}.
$$
原 $R^*$ 单射；$H$ 为相应原尾算子，满足 $HR=RH$、
$\|H\|<13/20$。置
$$
D_N=I,\qquad D_Y=I-R.
$$
使用每型自己的 $H$ 和 $D$，两型准确写成
$$
T=\begin{pmatrix}D^{-1}&0\\0&D^{-1}\end{pmatrix}
  \begin{pmatrix}H&I\\R&H\end{pmatrix}.                  \tag{1.1}
$$
特别 Y 型的 $D^{-1}$ 没有被截断或换成恒等。

置 $G=G_0^*$。对 $y=(a,b)\in\mathcal H\oplus\mathcal H$，
$y\in\mathcal D(G)$ 当且仅当存在唯一 $g\in\mathcal H$ 满足
$$
H^*a=R^*g.                                             \tag{1.2}
$$
此时
$$
\boxed{
Gy=f=\alpha^{-1}
\begin{pmatrix}
D^{*-1}(a+H^*b)\\
D^{*-1}(g+b)
\end{pmatrix}.}                                        \tag{1.3}
$$
证明是将 $T^*y=Sf$ 逐行乘原 $D^*$；用 $H^*D^*=D^*H^*$、
$R^*D^*=D^*R^*$，第二行先给 $f^{(0)}$，第一行再用 $R^*$ 单射给
$f^{(1)}$。因此 (1.2) 是实际范围条件，未用 $\overline{\operatorname{Ran}R^*}$ 代替它。

定义真正闭的尾图及其闭核心
$$
\mathscr G=\{(a,g):H^*a=R^*g\},\qquad
\mathscr C=\overline{\{(R^*t,H^*t):t\in\mathcal H\}}.
                                                               \tag{1.4}
$$
$H^*,R^*$ 交换保证 $\mathscr C\subset\mathscr G$。由于原核心列
$(Sh,T^*h)$ 在 $h=(u,v)$ 时对应
$$
(a,g)=\alpha(R^*v,H^*v),\qquad b=\alpha u,
$$
所以原 $\mathcal C=\overline{\{(Sh,T^*h)\}}$ 准确对应于
$(a,g)\in\mathscr C$ 和任意 $b\in\mathcal H$。这是同一原图的有界可逆坐标变换，故两边取的是同一 Hilbert 图闭包。

## 2. 全部自由 $b$ 消去后的三个正项

下文的 $\mathsf W$ 是正度量算子，不是稳定缺陷空间 $W$。置
$$
\mathsf W=(D^*D)^{-1}=D^{-1}D^{*-1},\qquad
A_0=H\mathsf W H^*+\mathsf W,\qquad
B_0=\mathsf W^{-1}+H^*\mathsf W^{-1}H,
$$
$$
A=A_0+\alpha^2I,\qquad
c=H\mathsf W a+\mathsf W g,\qquad r=a-H^*g.              \tag{2.1}
$$
这些正算子全部有界可逆；$\alpha$ 始终保留。

由 (1.3)，原图范数平方为
$$
Q(a,g,b)=\|a\|^2+\|b\|^2+
\alpha^{-2}\left(
 \|\mathsf W^{1/2}(a+H^*b)\|^2+
 \|\mathsf W^{1/2}(g+b)\|^2\right).                     \tag{2.2}
$$
其唯一最小 $b$ 及准确平方完成是
$$
b_{\min}=-A^{-1}c,\qquad
Q(a,g,b)=q(a,g)+\alpha^{-2}\|A^{1/2}(b-b_{\min})\|^2.
                                                               \tag{2.3}
$$
而最小值具有三个分别非负的原项：
$$
\boxed{
q(a,g)=\|a\|^2+
 \alpha^{-2}\|B_0^{-1/2}r\|^2+
 \|A_0^{-1/2}(A_0+\alpha^2I)^{-1/2}c\|^2.}             \tag{2.4}
$$

核 (2.4) 的完整 Schur 步骤如下。若先不计 $\alpha^2\|b\|^2$，
(2.2) 括号中的最小值为
$$
\|\mathsf W^{1/2}a\|^2+\|\mathsf W^{1/2}g\|^2
-\langle A_0^{-1}c,c\rangle
=\langle B_0^{-1}r,r\rangle.                           \tag{2.5}
$$
确切地，极小残量 $(v_0,v_1)$ 满足
$H\mathsf W v_0+\mathsf W v_1=0$。写
$(\mathsf W v_0,\mathsf W v_1)=(z,-Hz)$，则
$r=v_0-H^*v_1=B_0z$，并且加权平方范数为
$\langle z,r\rangle$。这证明 (2.5)。再用
$$
A_0^{-1}-(A_0+\alpha^2I)^{-1}
=\alpha^2 A_0^{-1}(A_0+\alpha^2I)^{-1}
$$
即得第三个正项。

N 型精确退化为
$$
A_0=I+HH^*,\qquad B_0=I+H^*H,\qquad c=Ha+g.             \tag{2.6}
$$
Y 型则必须保 (2.1) 的 $\mathsf W$，不能把它与 $H$ 或 $H^*$ 任意交换。

给出独立于极小 $\alpha$ 的粗等价界，方便核清没有隐藏 $\alpha^{-1}$：
$$
\frac12I\le\mathsf W\le2I,\qquad
\frac12I\le A_0,B_0\le3I,\qquad A_0+\alpha^2I\le4I.
$$
所以由 (2.4) 和 $g=\mathsf W^{-1}(c-H\mathsf W a)$，
$$
\boxed{
\frac1{100}\left(\|a\|^2+\|g\|^2+\alpha^{-2}\|r\|^2\right)
\le q(a,g)\le
100\left(\|a\|^2+\|g\|^2+\alpha^{-2}\|r\|^2\right).}     \tag{2.7}
$$
例如下界可用
$q\ge\|a\|^2+\alpha^{-2}\|r\|^2/3+\|c\|^2/12$
及 $\|g\|^2\le8\|c\|^2+14\|a\|^2$；
上界用 $q\le\|a\|^2+2\alpha^{-2}\|r\|^2+4\|c\|^2$。
常数 $100$ 仅包住这些有限数，不吞并原 $\alpha^{-2}$。

由 (2.3)，真正缺陷
$\mathcal E=\operatorname{Graph}G\ominus\mathcal C$
准确对应于
$$
(a,g)\in\mathscr G\ominus_q\mathscr C,\qquad b=b_{\min}.  \tag{2.8}
$$
也就是说正交性须用 (2.4) 的同一度量；不能改成任意尾图范数中的正交补再把原最小来源原样搬回。

## 3. 剩余稳定分量的同源准确读数

置
$$
K=H^2-R,\quad L=\ker K,\quad J u=(u,-Hu),\quad
\mathsf G_L=P_L(I+H^*H)|_L.
$$
原 $M=\ker T=J L$，$\mathsf G_L=J^*J$（将 $J$ 视为从 $L$ 出发）。
记
$$
r_D=D^{*-1}r.
$$
由 (1.2)，准确有
$$
K^*g=-H^*r,\qquad
K^*D^{*-1}g=-H^*r_D.                                  \tag{3.1}
$$
这里使用 $D^*$ 与 $H^*,K^*$ 的实际交换关系；没有将其中任一实际像改成闭包像。

从 (1.3) 逐项消去同一个 $b$，得到
$$
J^*f=\alpha^{-1}P_Lr_D.
$$
所以对每个原图对，而不只对缺陷，
$$
\boxed{
P_Mf=\alpha^{-1}J\mathsf G_L^{-1}P_Lr_D,\qquad
\|P_Mf\|^2=
\alpha^{-2}\langle\mathsf G_L^{-1}P_Lr_D,P_Lr_D\rangle.} \tag{3.2}
$$
特别
$$
\frac{\alpha^{-2}}{1+\|H\|^2}\|P_Lr_D\|^2
\le\|P_Mf\|^2\le\alpha^{-2}\|P_Lr_D\|^2.                \tag{3.3}
$$

(3.1) 又给 $r_D\perp H L$。因为 $HL\subset L$，
$$
P_Lr_D\in\ker(H|_L)^*.
$$
这与 (3.2) 读出的 $P_Mf\in W=M\ominus\overline{BM}$ 一致。
但不能由此断言 $H^*P_Lr_D\in\operatorname{Ran}K^*$：
(3.1) 给的是整个 $r_D$，而 $P_L$ 不与 $H^*$ 任意交换。

因此在原闭坐标 $X=\{v+Zv:v\in F\}$ 中，
$Z=0$ 的这一准确接口是：对 (2.8) 中全部同源尾图缺陷，
证明 $P_Lr_D=0$。本稿没有支付这个结论。

## 4. 真实缺陷两坐标之间的全空间互逆矩阵

两条原方程
$$
T^*y=Sf,\qquad By+Tf=0
$$
的第二行、第一行分别给
$$
a+H^*b=\alpha D^* f^{(0)},\qquad
f^{(1)}+Hf^{(0)}=-\alpha D b.                          \tag{4.1}
$$
因此对实际 $\mathcal E$ 中的同一对，
$$
\boxed{f=U_Dy,\qquad y=V_Df,\qquad V_D=U_D^{-1},}       \tag{4.2}
$$
其中这两个算子实际定义在整个两块 Hilbert 空间上：
$$
U_D=
\begin{pmatrix}I&0\\-H&I\end{pmatrix}
\begin{pmatrix}\alpha^{-1}D^{*-1}&0\\0&-\alpha D\end{pmatrix}
\begin{pmatrix}I&H^*\\0&I\end{pmatrix},                 \tag{4.3}
$$
$$
V_D=
\begin{pmatrix}I&-H^*\\0&I\end{pmatrix}
\begin{pmatrix}\alpha D^*&0\\0&-\alpha^{-1}D^{-1}\end{pmatrix}
\begin{pmatrix}I&0\\H&I\end{pmatrix}.                   \tag{4.4}
$$
三因子的逆逐个反序相乘即得 $U_DV_D=V_DU_D=I$，不需要任何额外交换假设。

特别
$$
V_Df=
\begin{pmatrix}
\alpha D^* f^{(0)}
+\alpha^{-1}H^*D^{-1}(Hf^{(0)}+f^{(1)})\\
-\alpha^{-1}D^{-1}(Hf^{(0)}+f^{(1)})
\end{pmatrix}.                                        \tag{4.5}
$$
这里的全域矩阵不把 $X$ 或 $Y$ 变成 $B,T$ 不变空间，也不将 $U_D$ 认作整个 $G$：只有 (4.1) 的同源对才同时满足 $f=Gy=U_Dy$。

## 5. 原物理指数权下的完整矩阵预算

令 $\mathcal N_{\rm tail}$ 为全部高位物理孔数，完整
$\mathcal N=\operatorname{diag}(\mathcal N_{\rm tail},
\mathcal N_{\rm tail}+I)$。以下在有限物理坐标上先共轭，再证明有界延拓。

记原归一化尾移位为 $U_j$（$j\ge1$），则
$$
U_j^2=\eta_jU_{j+1},\qquad R=\eta_0U_1,
$$
$$
H_N=\sum_{j\ge1}a_jU_j,\qquad
H_Y=(I-R)\sum_{j\ge1}a_jU_j(I+U_j)^{-1}-R,
\quad a_j=(j+1)^{-2}.                                 \tag{5.1}
$$
对任意实数 $|s|\le1$，真实删除列的纯项共轭权至多为 $e$；长度
$\ell\ge1$ 的 borrow 项至多为
$$
e^{\ell-1}\frac{\alpha_{j+\ell}}{\alpha_j}\le\eta_j.
$$
对伴随创建列同样成立。各固定移位的列像仍正交，故
$$
\|e^{s\mathcal N_{\rm tail}}U_j e^{-s\mathcal N_{\rm tail}}\|,
\quad
\|e^{s\mathcal N_{\rm tail}}U_j^* e^{-s\mathcal N_{\rm tail}}\|
\le e.                                                \tag{5.2}
$$
平方身份保留，因而所有原 Cayley 逆的共轭都满足
$$
\|(I+U_j(s))^{-1}\|
\le\frac{1+e}{1-e\eta_j}<4,                             \tag{5.3}
$$
伴随方向也一样。这是完整逆的有界延拓，不是截取前几项。

由 $\sum_{j\ge1}a_j<2/3$ 和 $e\eta_0<1/100$，(5.1)--(5.3) 给
$$
\|H(s)\|,\ \|H^*(s)\|\le8,\qquad
\|D(s)^{\pm1}\|,\ \|D^*(s)^{\pm1}\|\le2
\quad(|s|\le1).                                       \tag{5.4}
$$
$H^*(s)$ 表示原 $H^*$ 的相同方向共轭，未把它误写成 $H(s)^*$。

完整最低位使 (4.3)--(4.4) 的上、下三角非对角块另外分别得到
$e^{-s}$、$e^s$ 因子。因此每个三角因子的范数至多
$1+8e<23$，中间因子至多 $2/\alpha$。得到
$$
\boxed{
\|e^{s\mathcal N}U_De^{-s\mathcal N}\|,
\quad
\|e^{s\mathcal N}V_De^{-s\mathcal N}\|
\le\frac{2048}{\alpha_0}\qquad(|s|\le1).}               \tag{5.5}
$$

对 $0\le s\le1$，令
$\mathcal H_s=\operatorname{Dom}e^{s\mathcal N}$，
采用范数 $\|e^{s\mathcal N}\cdot\|$。(5.5) 证明原 $U_D,V_D$
互逆地保持 $\mathcal H_s$。严格地，先在有限坐标核 (5.5)，再在
$\mathcal H_s$ 范数中取有限坐标逼近；原 $U_D,V_D$ 在 $\mathcal H$ 有界及
$e^{s\mathcal N}$ 的闭性保证所得加权像就是原算子的像。

所以对每个实际缺陷对：
$$
\boxed{
y\in\mathcal H_s\iff f\in\mathcal H_s,\qquad
\frac{\alpha_0}{2048}\|e^{s\mathcal N}f\|
\le\|e^{s\mathcal N}y\|
\le\frac{2048}{\alpha_0}\|e^{s\mathcal N}f\|
\quad(0\le s\le1).}                                   \tag{5.6}
$$

## 6. 临界原核心现在也可从输出坐标进入

取原已付的
$$
s_0=\frac{2+2\log(3/2)}{14}<1.
$$
若同一 $(y,f)\in\mathcal E$ 的输出满足
$f\in\mathcal H_{s_0}$，(5.6) 首先实际给
$y\in\mathcal H_{s_0}$。临界物理矩核心定理遂对这同一个最大图来源给
$(y,f)\in\mathcal C$，与 $\mathcal E\perp\mathcal C$ 合用得到零对。

因此原两个闭坐标空间满足
$$
\boxed{
X\cap\operatorname{Dom}e^{s_0\mathcal N}
=Y\cap\operatorname{Dom}e^{s_0\mathcal N}
=\{0\}.}                                              \tag{6.1}
$$
这包括临界等号，也包括“实际输出 $f$ 的总物理孔数有界”的情形；
先前仅从输入 $y$ 的有界孔数进入核心的限制不再必要。

更一般地，对任意原最大图对令 $\xi=By+Tf$。只用第一块残量，(4.5) 精确变为
$$
y=V_Df+\alpha^{-1}\binom{-H^*\xi^{(0)}}{\xi^{(0)}}.      \tag{6.2}
$$
所以若实际 $f\in\mathcal H_{s_0}$ 且
$\xi^{(0)}\in\operatorname{Dom}e^{s_0\mathcal N_{\rm tail}}$，
同一 $y$ 也有临界矩，因而该原对进 $\mathcal C$。这里必须支付的是同一个第一块 Green 残量；不能从 $\xi\in\mathcal H$ 自动宣称它有指数矩。真实 $\mathcal E$ 中 $\xi=0$，正是 (6.1) 的无额外残量情形。

(6.1) 是同一实际缺陷的排除准则，不是物理平滑保持 $X,Y$ 的证明。若要用它消去整个 $\mathcal E$ 或只消去 $Z$，仍须产生实际落在这些闭来源空间内、且具有所需物理矩的向量，或另外支付 (3.2) 的原残量投影。本文没有提供这一步，也没有改变 $N=M$ 的开放状态。
