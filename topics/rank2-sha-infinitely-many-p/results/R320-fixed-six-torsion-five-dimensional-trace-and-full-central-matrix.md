# R320：固定六挠参考的五维真实同源迹与完整中央矩阵

日期：2026-11-13。**状态：以下原五维全纯 theta 空间的固定 $E[6]$ 极点、全部含常数同源迹、四个实际特征方向、三个原来源的完整列，以及同一 Newton 观察的全部运输与尾界均已证明。五维空间的闭合在这里是实际来源的闭合；原中央泛函的额外等变性没有被加入。**

本篇固定 $E_b:y^2=x^3+b$、$b=17$，取原 $dz=dx/(2y)$、$x=z^{-2}+\cdots$、$y=-z^{-3}+\cdots$、$\sigma=z+\cdots$。令
$$
X=x^3,\qquad \Theta=x\sigma^2,\qquad
U=\Theta(z)\Theta(2z)^4.
\tag{1}
$$
所有 $H_1=S,H_3,H_5$ 均为 R306–308 已付的原来源，不另改其 Schwartz、period 或权。

## 1. 同一个原参考及五维全纯空间

准确倍点式 $\Theta(2z)=x(X-8b)\sigma^8$ 给
$$
\boxed{U=\sigma^{34}x^5(X-8b)^4
       =\frac{-336bS+5H_3+4H_5}{9},\qquad U(0)=1.}
\tag{2}
$$
第二个等式由原三个多项式逐项相等证明，生产证书也独立核定它。

置 $d_0=X-8b$。本篇的有理空间为
$$
\mathcal V_6=
\operatorname{span}\left\{
1,\ A=\frac1X,\ B_1=\frac1{d_0},\
B_2=\frac1{d_0^2},\ B_3=\frac1{d_0^3}\right\}.
\tag{3}
$$
其实际极点只有两类：

- $x=0$ 的两条三挠点，此处 $X$ 是三阶局部参数，$A$ 有三阶极；
- $X=8b$ 的六条六挠点，此处 $X-8b$ 是一阶局部参数，$B_j$ 有 $j$ 阶极。

这些阶数指曲线上的真实局部阶。$U$ 在前两点各有五阶零，在后六点各有四阶零，因此
$$
\boxed{U\mathcal V_6\subset H^0(E_b,\mathcal L_{34})}
\tag{4}
$$
全部全纯。其具体形式为
$$
U\mathcal V_6
=\left\{\sigma^{34}x^2(X-8b)Q(X):\deg Q\le4\right\}.
\tag{5}
$$
例如五个基元对应的 $Q$ 依次是
$$
X(X-8b)^3,\quad (X-8b)^3,\quad
X(X-8b)^2,\quad X(X-8b),\quad X.
$$
它们独立，因而正好给 (5)。这是 R312 已出现的同一个真实五维全纯 theta 子空间，现在用全部固定六挠极的参考作了准确重写。

原目标商为
$$
\boxed{
g_U=\frac SU=
\frac{(X+b)(7X^2-4bX+16b^2)}
     {7X(X-8b)^3}.}
\tag{6}
$$
它从 $z^6$ 开始。没有把一个非挠极替换成任意点；(2)、(6) 是特征零来源恒等式。

### 1.1 普通处的实际参考质量也为单位

惰性处原 Newton 质量为 $\mathcal J_U(0)=U(0)=1$。普通处取 R308 的同一 $\bar\pi$，并令 $c=c_3\in\mu_3$、$c_5=c^2$。由原三个完整 $p$-core，
$$
m_U=M_U(0)=1-\frac{5c+4c^2}{9\bar\pi}.
\tag{7}
$$
这是真实的单位群质量，并非只用 $U(0)$ 代替它。

当 $c=1$，(7) 是 R308 已付的 $m_3$。当 $c\ne1$，置 $C=5c+4c^2\in\mathcal O_K$，有 $\operatorname N C=21$。若 $m_U$ 不是单位，则
$$
p\mid\operatorname N(9\bar\pi-C)
=81p+21-9\operatorname{Tr}(\bar\pi\bar C).
$$
而
$$
|21-9\operatorname{Tr}(\bar\pi\bar C)|
\le21+18\sqrt{21p}<p\qquad(p>7000).
$$
所以只能 $9\operatorname{Tr}(\bar\pi\bar C)=21$，与迹为整数矛盾。因此所有普通 $p>7000$ 的 $m_U$ 均为单位。此处只把 $U$ 用作 (2) 的实际参考，三个原算术角色仍是 $H_k$ 各自的角色。

## 2. 真实微分迹及全部相位

固定非零整数
$$
n\equiv1\pmod6.
$$
允许 $n$ 为负数。定义
$$
\mathcal T_nR\,dz=[n]_*(R\,dz)
=\frac1n\sum_{[n]Q=P}R(Q)\,dz.
\tag{8}
$$
因为 $[n]$ 固定全部 $E[6]$，(3) 的极支撑与最大阶均被保持。下面支付其准确常数，而不只由支撑判断维数。

### 2.1 两种真实平移和

令 $T$ 是一个固定的六挠点。原加法公式及 $\mu_3$ 对 $E[n]$ 的作用给
$$
\sum_{[n]Q=P}x(Q-T)=n^2x(P-T),\qquad
\sum_{[n]Q=P}y(Q-T)=n^3y(P-T).
\tag{9}
$$
证明第一式时，极与首项比较只留下常数。原全核满足
$\sum_{R\in E[n]\setminus\{O\}}x(R)=0$，因为 $[\omega]$ 置换该核且 $x(\omega R)=\omega x(R)$，故常数准确为零。第二式由第一式沿原微分求导；每个分支的导数带 $1/n$。所以在微分迹中，$x$ 平移线的特征值为 $n$，$y$ 平移线为 $n^2$。这证明包括负 $n$ 的符号。

取 $\theta^6=b$、$\omega^2+\omega+1=0$，以及
$$
T_0=(0,\theta^3),\qquad
P_j=(2\theta^2\omega^j,3\theta^3),\quad j=0,1,2.
$$
$T_0$ 为三挠点，$[2]P_j=(0,\theta^3)$，$[3]P_j$ 为非零二挠点，故 $P_j$ 的阶准确为六。

由原加法公式直接得到
$$
y(z-T_0)-y(z+T_0)
=-2\theta^3-\frac{8b\theta^3}{X},
\tag{10}
$$
$$
\frac16\sum_{j=0}^2
\frac{x(z-P_j)+x(z+P_j)}{2\theta^2\omega^j}
=1+60bB_1+432b^2B_2,
\tag{11}
$$
$$
-\frac1{18\theta^3}\sum_{j=0}^2
\{y(z-P_j)-y(z+P_j)\}
=1+228bB_1+4320b^2B_2+20736b^3B_3.
\tag{12}
$$
例如 (11) 使用的原对点和为
$$
x(z-P)+x(z+P)
=\frac{2(ax^2+a^2x+2b)}{(x-a)^2}.
$$
对 $a^3=8b$ 的三个 $a$ 求和后，分子准确变成
$6(X^2+44bX+16b^2)$，除以 $(X-8b)^2$ 即得 (11)。
(12) 由同一差分求导得到，其分子为
$X^3+204bX^2+864b^2X+256b^3$。这些公式保留原 $\mu_3$ 权，不把三个平移的系数统一成一。

### 2.2 唯一的对数微分方向及准确常数

对每个 $P_j$ 定义真实有理函数
$$
f_j=
\left(\frac{y-2\theta\omega^{2j}x+\theta^3}
           {y+2\theta\omega^{2j}x-\theta^3}\right)^3
\frac{y-\theta^3}{y+\theta^3}.
\tag{13}
$$
分子中的第一条直线在 $P_j$ 相切；其余交点是 $-(2P_j)$。水平线是三挠切线。因此
$$
\operatorname{div}(f_j)=6(P_j)-6(-P_j),\quad
f_j(O)=1,\quad f_j(-z)=f_j(z)^{-1}.
\tag{14}
$$
原直线微分给出完整恒等式
$$
\boxed{
\frac{d\log f_j}{dz}
=12\theta\omega^{2j}
 +\frac{36\theta^3}{x-2\theta^2\omega^j}.}
\tag{15}
$$
于是
$$
\boxed{
E_B:=B_1+\frac1{12b}
=\frac1{432\theta^7}\sum_{j=0}^2
       \omega^j\frac{d\log f_j}{dz}.}
\tag{16}
$$
这里的 $1/(12b)$ 是完整加权直线常数，不能删除。

由于 $nP_j=P_j$，范数的除子与 (14) 相同。其原点值由奇数核的 $Q,-Q$ 配对准确为一：
$$
\operatorname{Norm}_{[n]}f_j=f_j.
\tag{17}
$$
所以 (16) 是真实特征值一的微分方向，不留未定范数常数。它直接给
$$
\mathcal T_nB_1=B_1+\frac{1-n}{12b}.
\tag{18}
$$

## 3. 含全部常数的五维矩阵

定义
$$
\begin{aligned}
E_A&=A+\frac1{4b},\\
E_B&=B_1+\frac1{12b},\\
E_X&=1+60bB_1+432b^2B_2,\\
E_Y&=1+228bB_1+4320b^2B_2+20736b^3B_3.
\end{aligned}
\tag{19}
$$
(9)–(18) 给完整特征表：
$$
\boxed{
\mathcal T_n1=n,\quad
\mathcal T_nE_A=n^2E_A,\quad
\mathcal T_nE_B=E_B,\quad
\mathcal T_nE_X=nE_X,\quad
\mathcal T_nE_Y=n^2E_Y.}
\tag{20}
$$
因这些五个函数独立，全部微分迹已经计算。按 (3) 的基，准确为
$$
\boxed{\begin{aligned}
\mathcal T_nA={}&n^2A+\frac{n^2-n}{4b},\\
\mathcal T_nB_1={}&B_1+\frac{1-n}{12b},\\
\mathcal T_nB_2={}&nB_2+\frac{5(n-1)}{36b}B_1
                         +\frac{5(n-1)}{432b^2},\\
\mathcal T_nB_3={}&n^2B_3+\frac{5n(n-1)}{24b}B_2\\
&+\frac{(n-1)(19n-31)}{1728b^2}B_1
 +\frac{(n-1)(n-31)}{20736b^3}.
\end{aligned}}
\tag{21}
$$
矩阵 $M(n)$ 采用“第 $i$ 列是 $\mathcal T_nq_i$ 的系数”约定。它满足
$$
M(m)M(n)=M(mn),\quad
\det M(n)=n^6,\quad
\det(t-M(n))=(t-1)(t-n)^2(t-n^2)^2.
\tag{22}
$$
这些是完整实际矩阵恒等式；生产证书分别核定全部列、常数和复合。

### 3.1 所有惰性素数的原 Cartier 平方像

取 $p\ge11$、$p\equiv5\pmod6$、$p\ne17$，令 $n=-p$。
此时 $n\equiv1\pmod6$，所以不需要另加一个特殊 Galois 类来固定这些六挠点。

矩阵 (21) 的分母在这些 $p$ 处都是单位。模 $p$ 后，它是准确的秩一幂等，像为
$$
\boxed{\overline{\mathcal T_{-p}\mathcal V_6}
=\mathbf F_p E_B.}
\tag{23}
$$
R313 的有限平坦微分迹在约化后是 Cartier 平方，所以 (23) 也是这些实际微分的 Cartier 平方像。也可逐个局部主部核定：二、三阶极被 Cartier 平方杀掉；归一的 $d\log$ 方向由 (17) 固定；全纯微分在超奇异曲线上被杀掉。

## 4. 三条原来源的准确特征列

记
$$
C_3=X^3-204bX^2-384b^2X+64b^3,\quad D=(X+4b)C_3,
$$
$$
D_5=X^4+280bX^3+1968b^2X^2+832b^3X-128b^4.
$$
则原三个商准确为
$$
g_1=\frac SU,\qquad
g_3=\frac{D}{X(X-8b)^3},\qquad
g_5=\frac{D_5}{X(X-8b)^3}.
\tag{24}
$$
按 $(1,E_A,E_B,E_X,E_Y)$，完整系数表为：

| 实际特征函数 | $g_1$ | $g_3$ | $g_5$ |
|---|---:|---:|---:|
| $1$ | $-1/(224b)$ | $3/2$ | $0$ |
| $E_A$ | $-1/224$ | $-b/2$ | $b/4$ |
| $E_B$ | $-3/112$ | $-9b$ | $9b$ |
| $E_X$ | $1/(224b)$ | $3/2$ | $-3/2$ |
| $E_Y$ | $3/(896b)$ | $-9/8$ | $27/16$ |

该表是有理函数恒等式；没有由维数推定来源身份。特别
$$
\boxed{
\overline{\mathcal T_{-p}g_1}
=-\frac3{112}E_B\ne0.}
\tag{25}
$$
所以所有上述惰性 $p$ 的这个原有理微分迹都非零。它是否给原中央观察的非零，要用下一节的同一加权变换判断。

## 5. 真正的 theta 迹及完整 Newton 运输

对 $T\in U\mathcal V_6$ 定义真实、依赖原参考的来源算子
$$
\boxed{
\mathscr T_{U,n}T
=U\,\mathcal T_n(T/U).}
\tag{26}
$$
逐支式为
$$
\mathscr T_{U,n}T(z)
=\frac{U(z)}n\sum_{R\in E[n]}
  \frac{T(z/n+R)}{U(z/n+R)}.
\tag{27}
$$
在每个分支内，分子和分母是同一原 theta 线丛的截面，完整 Gaussian、半特征与平移 lift 准确相消；外面的 $U(z)$ 仍是原参考。因而 (27) 就是 (26) 的几何迹，且由 (21) 落回 (5)。没有把它直接认作 R300 的另一个 Hecke $p$-core。

当 $p\mid n$，单支 Taylor 级数的收敛圆盘可以小于原 Newton 圆盘。因此先在有理函数域中作完整有限迹和 (21) 的相消，再使用原解析变换；这里没有逐支作未经支付的 Mellin 交换。

现在固定上节的惰性 $p$，置
$$
d=p+1,\quad \kappa_b=34c_b,\quad
c_b=[z^d]\log(\sigma_b(z)/z),\quad
v_p(\kappa_b)=-1.
$$
始终用 R301–303 的同一完整变换
$$
\mathcal J_T(u)=
\sum_{h\ge0}[z^{dh}](e^{-\kappa_bz^d}T)
                      \kappa_b^{-h}(u)_h.
\tag{28}
$$
$U$ 的共同 Gaussian 与原 $S,H_3,H_5$ 相同，且
$\mathcal J_U\in1+p\mathbf Z_p\langle u\rangle$。定义
$$
\mathscr L_U(T)=
\left(\frac{\mathcal J_T}{\mathcal J_U}\right)'(0).
\tag{29}
$$
因为 $\mathcal J_S(0)=0$，
$$
\boxed{\mathscr L_U(S)=\mathcal J_S'(0).}
\tag{30}
$$
所以参考改变没有改变原目标非零的含义。

写 $q=(1,A,B_1,B_2,B_3)$。整个原权变量中的准确式是
$$
\boxed{
\frac{\mathcal J_{\mathscr T_{U,n}(Uq_i)}(u)}
     {\mathcal J_U(u)}
=\sum_{j=0}^4 M(n)_{ji}
       \frac{\mathcal J_{Uq_j}(u)}{\mathcal J_U(u)}.}
\tag{31}
$$
这由原来源恒等式 (21) 逐项得到。所有常数列都在 (31) 中保留；求导后只有 $q_0=1$ 的那一行准确为零。

更明确地，令
$$
\Phi_E(u)=\frac{\mathcal J_{UE}(u)}{\mathcal J_U(u)}-E(O),
\qquad \ell_E=\Phi_E'(0).
$$
由实际特征列，
$$
\boxed{\begin{aligned}
\Phi_{g_1}(u)
={}&-\frac1{224}\Phi_{E_A}(u)
-\frac3{112}\Phi_{E_B}(u)
+\frac1{224b}\Phi_{E_X}(u)
+\frac3{896b}\Phi_{E_Y}(u),\\
\Phi_{\mathcal T_ng_1}(u)
={}&-\frac{n^2}{224}\Phi_{E_A}(u)
-\frac3{112}\Phi_{E_B}(u)
+\frac n{224b}\Phi_{E_X}(u)
+\frac{3n^2}{896b}\Phi_{E_Y}(u).
\end{aligned}}
\tag{32}
$$
因此完整交换差正是
$$
\boxed{
\Phi_{\mathcal T_ng_1}-\Phi_{g_1}
=(n^2-1)\left(-\frac{\Phi_{E_A}}{224}
                    +\frac{3\Phi_{E_Y}}{896b}\right)
+\frac{n-1}{224b}\Phi_{E_X}.}
\tag{33}
$$
这给出了实际缺项的三条原有限行，没有把“有限维”变成一个免费的标量等变断言。

### 5.1 同一个完整尾界

取原 $R=p^{-1/(2p)}$。$\widehat U=e^{-\kappa_bz^d}U$ 在此圆盘的 Gauss 范数至多一。对 $q=A$ 或 $B_j$，其原整参数展开从 $z^{6j}$ 开始，其中 $A$ 取 $j=1$。因而
$$
v_p\!\left([z^{dh}](\widehat Uq)\kappa_b^{-h}\right)
\ge\left\lceil\frac{h(p-1)+6j}{2p}\right\rceil.
\tag{34}
$$
这使完整 Tate 级数一致收敛。若只求中央导数，截去 $h>A_0$ 的尾具有下界
$$
\boxed{
\left\lceil\frac{(A_0+1)(p-1)+6j}{2p}\right\rceil
+v_p(A_0!).}
\tag{35}
$$
(21) 的矩阵整，故全部运输保持这些界；所有高位都可用同一个原尾界控制。

四条 $\Phi_E$ 均在 $p\mathbf Z_p\langle u\rangle$。取 $n=-p$，(32) 于是给
$$
\boxed{\begin{aligned}
\mathscr L_U(\mathscr T_{U,-p}S)
={}&-\frac3{112}\ell_{E_B}
-\frac p{224b}\ell_{E_X}\\
&+p^2\left(-\frac{\ell_{E_A}}{224}
                  +\frac{3\ell_{E_Y}}{896b}\right),
\end{aligned}}
\tag{36}
$$
以及整个权变量中的同余
$$
\boxed{
\Phi_{\mathcal T_{-p}g_1}(u)
\equiv-\frac3{112}\Phi_{E_B}(u)
\pmod{p^2\mathbf Z_p\langle u\rangle}.}
\tag{37}
$$
其中剩下的真正来源是
$$
\boxed{
UB_1=\sigma^{34}x^5(X-8b)^3
=\sigma^6\Theta^2\Theta(2z)^3.}
\tag{38}
$$
它从 $z^6$ 开始，全部零也是固定六挠点；(16) 给它准确的范数固定对数微分表达。式 (36)–(38) 保留原 theta 乘子，未将该行直接替换成一个对数常数。

## 6. 原有限空间上的实际无标量边界

一个精确的有限证书说明 (33) 不能自动删除。在 $p=23,b=17$，
$$
[z^{24}]\frac U X
=-\frac{10343098809781711}{857800125}\equiv7\pmod{23},
$$
$$
[z^{24}]\frac U{X-8b}
=-\frac{33503806082698781}{9435801375}\equiv5\pmod{23}.
\tag{39}
$$
这些数由原 $x,\sigma$ 方程递推得到，没有对来源拟合。

这里还要保留 $b=17$ 的尺度。R301 在基曲线 $b=1$ 上的首分母，经实际同构给
$$
pc_b\equiv-b^s(-1)^s4^{-s}\binom{2s}{s}\pmod p,
\qquad s=(p+1)/6.
\tag{40}
$$
所以在 $p=23$，$pc_b=5$、$\kappa_b^{-1}/p=18$。完整首 divided 行与 (35) 因而给
$$
\boxed{
\frac{\ell_{E_A}}{23}\equiv11,\qquad
\frac{\ell_{E_B}}{23}\equiv21\pmod{23}.}
\tag{41}
$$
两条实际中央行均非零，而它们在同一 $\mathscr T_{U,-23}$ 下的特征值分别为 $23^2$ 和一。若这个真正五维空间上存在
$\mathscr L_U\mathscr T_{U,-23}=\alpha\mathscr L_U$，
则 (41) 分别迫 $\alpha=23^2$ 和 $\alpha=1$，矛盾。

该证书针对明确的同一来源空间和同一原中央观察。它不从一个有限素数推出跨素数非零或消失；其作用是准确保住 (33) 所显示的缺项。

## 7. 结果范围与复算

本篇把原 $S$ 放入一个在全部惰性 $[-p]$ 真实迹下闭合的固定五维全纯空间，并给出全部矩阵、常数、三条原列、完整 Newton 返回和实际非齐次行。尤其 (25) 是统一的非零原 Cartier 像，而 (36) 明确列出将其转成原中央非零时仍需比较的实际行。

生产证书
[check-jzero-fixed-six-torsion-full-trace.py](../scripts/check-jzero-fixed-six-torsion-full-trace.py)
及其 JSON 的 **29 项精确检查全部 PASS**，逐项核定原三挠与六挠加法式、实际 Miller 微分、完整矩阵及复合、三个来源列、秩一像和 (39)–(41)。首 Taylor 递推从
$$
W=z^2x=1+\sum_{r\ge1}W_rz^{6r},\quad
W_1=-b/7,\quad
W_r=\frac{\sum_{j=1}^{r-1}W_jW_{r-j}}{(r-1)(6r+1)}
$$
与
$\log(\sigma/z)=-\sum W_rz^{6r}/[6r(6r-1)]$
重建，保留原符号、微分和 $b$ 尺度。

直接依赖：
[R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
[R303](R303-jzero-inert-full-selmer-period-comparison-and-central-criterion.md)、
[R307](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)、
[R308](R308-jzero-rank-zero-reference-full-pcore-and-central-masses.md)、
[R312](R312-original-central-projection-fixed-poles-and-complete-kernels.md)、
[R313](R313-jzero-frobenius-square-actual-trace-and-central-first-layer.md)、
[R318](R318-actual-torsion-norm-translated-sigma-and-full-central-division-log.md)。

