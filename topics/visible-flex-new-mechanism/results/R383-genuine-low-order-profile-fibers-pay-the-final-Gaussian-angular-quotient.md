# R383：原面积不变的真实低层母纤维与双号模块支付最后的 Ω 角商

日期：2026-11-15。**完整有限纸面构造；未执行符号程序、求积、参数扫描、人工测试或研究计算。**

[R379](R379-complete-ZZ-second-angular-quotient-and-the-frozen-quartic-remainder.md) 已将同一真实偶弱圆的全部对称 Gaussian 外矩归结为唯一残量
$$
\Omega(f,g)=\operatorname{Re}\int(q'-xq'')^4,\qquad q=f+ig.
$$
其末端 $\mathcal F_\star$ 纤维对此量严格没有响应。本稿改变更早的真实强模块：在一个原本所有面积为零的等背景模板中，只改变一个编码位置的共享母，准确保持该位置的三个真实矩和各完整副本的实际 self 和。这个较小的有限观察纤维具有一个真实 $\Omega$ 自由方向。

从而得到两个完整实强模块，全部18面积、原 $\mathfrak j,\mathfrak k$ 与完整第三保持零，而 $\Omega$ 分别为严格正、负值。它们以正幅及有限正伸缩精确补掉当前弱基线的 $\Omega$，新增 $\Psi$ 成本任意小。最后在同一个重新初选的末控制器上应用 R379 的17行有限根，准确支付全部十个对称 Gaussian 乘积。这里不把单独原 self 的形式线性独立当成实际母参数，也不把新增观察当作自动可控。

来源：
[R183](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、
[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、
[R263](R263-ordered-Gaussian-area-81-scalar-recursion.md)、
[R277](R277-low-jet-observation-fibers-and-high-jet-energy-control-for-equal-background-circles.md)、
[R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)、
[R325](R325-inward-weak-hook-circles-pay-three-directed-rows-and-the-one-history-compatibility.md)、
[R349](R349-complete-second-self-and-positive-cone-pay-the-fourth-Gaussian-area.md)、
[R353](R353-ordered-tails-and-three-positive-centers-pay-the-positive-minus-two-first-moment.md)、
[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)、
[R360](R360-complete-positive-negative-second-self-and-six-dimensional-middle-cone.md)、
[R364](R364-local-angular-quotient-and-five-target-control-pay-the-negative-three-minus-one-product.md)、
[R372](R372-complete-ZZ-zero-angular-quotient-and-nine-target-finite-frequency-control.md)、
[R379](R379-complete-ZZ-second-angular-quotient-and-the-frozen-quartic-remainder.md)、
[R380](R380-sixteen-real-targets-and-one-finite-root-pay-the-complete-Y-square.md)。

## 1. 原规范与新有限观察

固定原小共振参数 $0<\kappa^2<1/100$ 和非零 Gaussian 系数
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},\quad
L=\Phi_{p_0},\quad U=\Phi_{s_1},\quad Y=\Phi_{p_2},
$$
$$
W=aR+bS,\qquad Z=dL+eU .
$$
特别 $e,a-b,d-5e$ 非零。右锚、三个 $I_j$、真实 nonlegal self 全取原规范
$$
S_{XY,j}(u)=2I_j\{u,[X,Y](u;u^2)\}.
\tag{1}
$$
每个 self 保留原 primitive 和 Green 项，不要求实单包三矩零。

空间反射后可能非零的九个 area 位置是
$$
\mathcal A_{\rm ev}=
\{WP1,\ ZP0,\ ZP2,\ ZW1,\ ZY0,\ ZY2,\ WY1,\ PY0,\ PY2\}.
\tag{2}
$$
它们各有两个 angular even 系数；另外九个外矩由完整空间反射为零，所有 angular odd 由原十二完整副本清除。

先固定原 R277/R280 等背景编码、五个完整 blocks、八／十二副本及最后空间镜像。每个实际微包的平方背景满足
$$
b_i^2=B,\quad a_i^2=B+R_i,\quad
R_i\in\{-B/2,8B\},\quad T_i=a_ib_i,
$$
$$
\sum_iR_it_i^m=\sum_iT_it_i^m=0\quad(0\le m\le10),
$$
$$
a_i^4-5a_i^2b_i^2=\frac{9B}{2}R_i,\qquad
\operatorname{Re}(a_i+ib_i)^4=\frac{7B}{2}R_i.
\tag{3}
$$
R280 的三有序矩面积及五 block 正权取原真值；它们不由微包 self 替代。该原模板对任意共同非零实偶紧母具有全部18面积零。其相对布局可先固定，母矩的共同正归一只在选母后加入；固定母矩的后续变化不再改变任何权。

选一个编码位置 $i_*$，$R_{i_*}\ne0$。只允许这个位置在所有既定八／十二副本及空间镜像中的母共同改变。把这些实际出现位置记为 $c_\nu$、原正四次权记为 $\omega_\nu$。所有真正的 $c_\nu,\omega_\nu$ 从始至终保留。

取固定正半母区间 $I\Subset(0,1/2)$，令
$$
Ev(y)=v(y)+v(-y),\qquad v\in C_c^\infty(I).
$$
因此 $Ev$ 是实际偶紧母，所有原子和控制方向均有共同 collar。定义半母的三个真实矩
$$
\mu(v)=\left(\int(v'')^2,\ 
\int y(v'')^2,\ 
\int[y^2(v'')^2+2(v')^2]\right).
\tag{4}
$$
固定这三个半母矩，比只固定偶母的两个非零矩更强；它也保留下面所有真实有序尾。

对(2)的每个位置，定义一个**实际值和**
$$
A_{XY,j}(v)=\sum_\nu\omega_\nu
S_{XY,j}(T_{c_\nu}Ev).
\tag{5}
$$
另外保两个原 local 四次量的实际和
$$
\mathfrak j(u)=\int[3(u')^2(u'')^2+u(u'')^3-2xu'(u'')^3],
$$
$$
\mathfrak k(u)=\int[(u')^2(u'')^2-\tfrac25xu'(u'')^3].
$$
令 $A_{\mathfrak j},A_{\mathfrak k}$ 按(5)同样定义，最后设
$$
O(v)=\sum_\nu\omega_\nu\int
\{(T_{c_\nu}Ev)'-x(T_{c_\nu}Ev)''\}^4.
\tag{6}
$$

新观察是
$$
\mathcal A(v)=(\mu(v),\ A_{XY,j}(v)\ ((XY,j)\in\mathcal A_{\rm ev}),
\ A_{\mathfrak j}(v),A_{\mathfrak k}(v)).
\tag{7}
$$
这里不是原 $\mathcal F_\star$ 的全部平移系数。本稿将准确证明：
在一开始选择的实际正则母附近，(7)可以全部不变，而(6)有两侧真实变化。

## 2. 每个观察的真实有序加法缺陷

R277 的原 cubic／Green 降阶证明：(1)是固定共同支撑 $C^2$ 域上的连续四次多项式。原 $J(r^2),J(xr^2),J(x^2r^2+2v^2)$ 和左矩项全部保留。(5)—(7)因此也为连续多项式，没有在本稿增加任何仅形式定义的观察。

若紧实包 $u$ 完全在紧实包 $v$ 左方，则
$$
S_{XY,j}(u+v)-S_{XY,j}(u)-S_{XY,j}(v)
=\Gamma_{XY,j}(\mu(u),\mu(v)),
\tag{8}
$$
其中 $\Gamma$ 是原真实矩双线性式。

可以直接看见(8)为何保全尾：二次交叉输出 $X(u,v)$ 为零；右包二次场在左包上是原三矩决定的二次左尾。它进入左 outer 的原 $[X,Y]$，产生原 sl2 作用的矩双线性项。左包二次场在右包上为零。右包三次场的左二次尾与紧 outer $u$ 在全部三个 $I_j$ 下正交，包括 $I_2$ 的 $2u'w'$。因此剩下的交叉项恰为(8)，而不是将单包左尾置零。

平移和反射的矩矩阵为
$$
M_c\mu=(\mu_0,\mu_1+c\mu_0,\mu_2+2c\mu_1+c^2\mu_0),
\qquad
R_\mu\mu=(\mu_0,-\mu_1,\mu_2).
\tag{9}
$$
若 $v,w$ 在正半区间内依次不交，则偶扩展的顺序是
$Rw,Rv,v,w$。对一个实际 copy 中的(8)，其四个新增项准确为
$$
\begin{aligned}
&\Gamma(M_cR_\mu\mu(w),M_cR_\mu\mu(v))
+\Gamma(M_cR_\mu\mu(w),M_c\mu(v))\\
&+\Gamma(M_cR_\mu\mu(v),M_c\mu(w))
+\Gamma(M_c\mu(v),M_c\mu(w)).
\end{aligned}
\tag{10}
$$
每项都是半母两个真实三矩的双线性式。对全部实际 $\omega_\nu$ 求和，
每个 $A_\alpha$ 因而有一个固定实矩阵 $C_\alpha$，满足
$$
A_\alpha(v+w)-A_\alpha(v)-A_\alpha(w)
=\mu(v)^TC_\alpha\mu(w)\qquad(v<w).
\tag{11}
$$
$A_{\mathfrak j},A_{\mathfrak k},O$ 是 local 四次式，故其 $C_\alpha=0$。

(10)也说明，冻结半母的全部三矩后，一处母变化不会改变它与任何其它真实包的跨核；无需把整个普通母的内部子包假定为 legal。

## 3. 有序四次数据的精确微分关系引理

以下给出使用实际母参数所需的证明，不以“generic rank”代替。

设 $F$ 是共同 collar 的实紧 profile 上连续四次多项式，并有固定矩阵 $C$ 的真实有序缺陷
$$
F(u+v)-F(u)-F(v)=\mu(u)^TC\mu(v),\qquad u<v.
\tag{12}
$$
若对所有光滑、$D\mu$ 满秩的 profile，存在一个常于其切方向的向量 $\lambda(u)$，使
$$
DF(u)=\lambda(u)\cdot D\mu(u),
\tag{13}
$$
则
$$
\boxed{C=C^T,\qquad F(u)=\tfrac12\mu(u)^TC\mu(u).}
\tag{14}
$$

证明如下。取两个不交、各自 $D\mu$ 满秩的真实包 $u<v$。
四次及二次齐次性给 $\lambda(tu)=t^2\lambda(u)$。
分别只变分左右两包，在 $tu+sv$ 上由(12)—(13)得同一个乘子
$$
t^2\lambda(u)+s^2C\mu(v)
=s^2\lambda(v)+t^2C^T\mu(u).
$$
独立改变 $t,s>0$，故
$$
\lambda(u)=C^T\mu(u),\qquad \lambda(v)=C\mu(v).
\tag{15}
$$
同一个中间包先作右包、再作左包，得到
$(C-C^T)\mu(v)=0$。任何非空小区间都容得下三个同宽、不同中心的真实小包；其三矩列是非零公共因子乘一个三点 Vandermonde。改变三个非零实幅，$D\mu$ 满秩，矩像含实开集。故 $C=C^T$。

对任意 regular 紧包，其支撑两侧共同 collar 内都能放这种辅助包，
所以 $\lambda(u)=C\mu(u)$。对幅度方向使用 Euler 恒等，
$4F=DF[u]=2\mu^TC\mu$，得到(14)。regular 光滑点稠密：
可在任一 compact 支撑的余 collar 加三个任意小的上述实包，
再用连续性延拓。因此(14)适用于全部原域。

等价说，对一组有限四次观察 $F_1,\ldots,F_m$，
若一个**固定常向量** $c$ 对所有真实 $u$ 的全部 $\ker D\mu(u)$ 消灭
$c\cdot DF(u)$，那么该固定组合 $c\cdot F$ 必为一个二次矩二次式。
这里的“所有 profile、同一个常向量”不能换成某一点依赖于 $u$ 的猜测系数。

## 4. 从有限导数见证到同一个实际母

令 $V$ 为下列有限维目标向量的全局线性包：
$$
(DF_1(u)[h],\ldots,DF_m(u)[h]),\qquad
D\mu(u)[h]=0,
\tag{16}
$$
$u,h$ 取共同正半区间内的光滑实紧函数。
有限目标维数保证只需有限个实际 $(u_\ell,h_\ell)$ 即可张成 $V$。

对每一对同时作独立的真实正仿射输运。原矩变换是(9)的可逆三角伸缩版，故 $D\mu[h_\ell]=0$ 精确保留。原 E8 全式和真实 Green 的仿射次数有限，所以(16)的每个坐标对这些有限平移／正宽参数是有限 Laurent 多项式；其系数是真实固定积分，不被当作自由输入。

先选一个非零的见证 minor。在全仿射参数的 identity 处它非零，故该 Laurent 多项式不恒零。把所有 supports 放入指定 $I$ 的互不交小子区间是一非空开条件；非零实解析多项式不能在整个这样的开域为零。因此可以一次选出**实际有限、严格不交**的仿射参数，同时保原 minor。

这只是用正式参数多项式证明某个合法开域含非零点；没有把 identity 时可能重叠的 supports 当成合法并置，也不执行任何参数搜索。

将输运后的所有母相加为一个真正的 $v_0$。式(11)的交叉微分全部含相应 $D\mu[h_\ell]=0$，所以
$$
DF_\alpha(v_0)[h_\ell]=DF_\alpha(u_\ell)[h_\ell].
\tag{17}
$$
原有限 minor 在这个**同一个**真实母上实现。再加三个足够小、严格不交的矩 regularizer，保证 $D\mu(v_0)$ 满秩；对原 $h_\ell$ 而言交叉微分仍为零。

令 $r$ 是旧观察在(16)的投影空间维数。任何 regular profile 上
$D(\mu,F_{\rm old})$ 的秩不超过 $3+r$；(17)可以同时达到这个上界。
因此选定真实 minor 后，其邻域中整个旧观察秩恒为 $3+r$。
$C^\infty$ 在原 $C^2$ 域稠密，且矩方向可用上述固定三个 regularizer 纠正，
所以该上界也适用于相同 $C^2$ 邻域。

若额外观察 $O$ 不在“旧观察的常系数组合＋二次矩二次式”中，
§3 说明它在(16)中给一个额外独立行。于是同一个实际母可以满足
$$
\operatorname{rank}D(\mu,F_{\rm old},O)
=\operatorname{rank}D(\mu,F_{\rm old})+1.
\tag{18}
$$
选择 $3+r$ 个真实旧输出坐标及固定光滑方向，再添一个 $O$ 方向，
有限 IFT 给一个真实光滑曲线
$$
\boxed{
\mu(v_\eta)=\mu(v_0),\quad
F_{\rm old}(v_\eta)=F_{\rm old}(v_0),\quad
O(v_\eta)=O(v_0)+\eta
}
\tag{19}
$$
于一个双侧实际小区间。

(19)中的全部旧行由局部常秩支付，而不是只固定所选 minor 的几行。
没有把无限维纤维、无限频率或任意指定母函数视作实际解。
所有最终 $v_\eta$ 都是同一个光滑基点加有限个固定光滑方向，
故仍为共同 collar 的 $C^\infty$ 函数。

## 5. 本稿的 O 确实不是旧观察加矩的组合

现取 $F_{\rm old}$ 为(5)的九个实际 self 和及
$A_{\mathfrak j},A_{\mathfrak k}$。
必须证明(18)的独立性；R379 只证明旧更大纤维冻结 $O$，不能代替这一点。

先记录真实正伸缩权：
$$
\begin{array}{c|c}
\text{self 或 local 量}&u(x/H)\text{ 的完整权}\\ \hline
WP1,\ ZP0&-7\\
ZP2,\ ZW1,\ PY0,\ \mathfrak j,\mathfrak k&-5\\
ZY0,\ WY1,\ PY2,\ \mathcal O&-3\\
ZY2&-1 .
\end{array}
\tag{20}
$$
这里 $\mathcal O(u)=\int(u'-xu'')^4$。
三个真实矩的权分别为 $-3,-2,-1$，矩二次式的可能权为 $-6,-5,-4,-3,-2$。

原二次 nonlegal 反射增加由真实三矩决定的二次多项式尾。嵌套时更外层右积分还可能增加一个三次 profile 系数的二次输出多项式；它与紧 outer 在全部三个 $I_j$ 下准确正交。剩下的内尾通过原 sl2 作用收成三矩二次式。因此由原恢复和(8)，对(2)的 reflection-even 位置，
$$
S_\alpha(Ru)=S_\alpha(u)+\text{三矩的二次式}.
\tag{21}
$$
因此 $S_\alpha(Ev)$ 模矩二次式等于 $2S_\alpha(v)$，
而 $O(Ev)=2O(v)$、$\mathfrak j(Ev)=2\mathfrak j(v)$、
$\mathfrak k(Ev)=2\mathfrak k(v)$。

所有实际 copy 偏移 $c_\nu$ 保留。
将半母变为 $v(y/H)$ 时，某权 $w_\alpha$ 的原 self 和准确是
$H^{w_\alpha}$ 乘 $c_\nu/H$ 的有限多项式。
其最高 H 次项模矩二次式为
$2(\sum\omega_\nu)H^{w_\alpha}S_\alpha(v)$。
对一个固定紧 $v$，在 $H=1$ 的小开区间内仍有合法支撑；
该开区间上成立的有限 Laurent 身份即可逐系数比较，
不需要把 $H\to\infty$ 的 profile 真放进原母区间。

假设 $O$ 属于旧观察加矩二次式的常系数 span。
按(20)先比较唯一权 $-1$ 的项：
其系数所乘的
$$
S_{ZY,2}=(d-5e)S_{LY,2}
$$
不是零泛函。原 R349 local 密度中
$-x^2u^2r^2$ 的 Euler 最高四导系数非零，且 $d-5e\ne0$。
故该项系数必须为零。

再比较权 $-3$。所有其余更低权观察及 $\mathfrak j,\mathfrak k$ 均不能进入此系数。
约去共同正因子，假设将迫出一个原单包身份
$$
\mathcal O
=\alpha S_{ZY,0}+\beta S_{WY,1}+\gamma S_{PY,2}
+\eta\,\mu_1\mu_2.
\tag{22}
$$
其他矩乘积没有权 $-3$。

R360 的完整 nonlegal 身份
$$
S_{PY,2}=-2S_{RY,1}-2S_{SY,1}-\mu_1\mu_2
\tag{23}
$$
及原真实 self 加法给
$$
\Gamma_{RY,1}=0,\quad \Gamma_{ZY,0}=0,\quad
\Gamma_{SY,1}(\mu,\nu)=-\mu_2\nu_1/2 .
\tag{24}
$$
对(22)取两个不交真实包的加法缺陷。
$\mathcal O$ 是 local，故其缺陷零。
先比较 $\mu_1\nu_2$，再比较 $\mu_2\nu_1$，得
$$
\eta=\gamma,\qquad b\beta=2\gamma.
$$
所以(22)必进一步退化为
$$
\mathcal O=A S_{RY,1}+B S_{ZY,0}.
\tag{25}
$$
这一步保留了(23)的 $\mu_1\mu_2$，也正使用(24)的不对称原尾；
不能只在 legal 复输入上删矩以后推它。

最后直接用原 local 密度排除(25)。
记 $v=u',r=u''$。R353/R270 给
$$
\begin{aligned}
S_{LY,0}={}&\int[u^2r^2-4xuvr^2+3x^2v^2r^2+x^2ur^3
-\tfrac43x^3vr^3+\tfrac5{24}x^4r^4],\\
S_{UY,0}={}&\int[-u^2r^2+8xuvr^2-9x^2v^2r^2-3x^2ur^3
+\tfrac{16}3x^3vr^3-\tfrac{25}{24}x^4r^4-\tfrac23v^4],\\
S_{RY,1}={}&-S_{LY,0}-\mathcal O/12 .
\end{aligned}
\tag{26}
$$
一个只含 $u,u',u''$ 的 local 密度若其紧积分恒零，
其 Euler 表达的最高 $u^{(4)}$ 系数，即密度对 r 的二阶偏导，必须为零。
对(25)比较这个系数中的 $u^2,xuv$，得到
$$
-2A+2(d-e)B=0,\qquad
8A+(-8d+16e)B=0.
$$
因为 $e\ne0$，必 $A=B=0$。
但 $\mathcal O$ 的同一最高系数为
$$
12x^2(v-xr)^2\not\equiv0
$$
于原正半区间的开放 jet 域，矛盾。

故(22)不可能，§4 的额外一行独立性准确成立。
这给了一个完整原式的有限 jet 见证，而非只声称不同积分“应当独立”。

## 6. 在一个原模板中产生真实 Ω 两侧

把§4应用于现在的旧观察，得到一个实际半母 $v_0$ 及双侧小族 $v_\eta$。本节母函数只要求非零实偶紧光滑，不要求点态正。R277/R280 的三矩编码、ordered 面积与完整第三包装均在此域成立，$m=\int(u'')^2>0$ 已足。
从起点用 $u_0=Ev_0$ 建立 R277/R280 的共同母强模板。
其原矩、真实原始副本和空间镜像均按§1固定。
共同母版本的所有18面积为零，且
$$
\Omega_{\rm template}=0
$$
由(3)与 $\mathcal O(T_tu_0)$ 至多四次的真实平移多项式直接得到。

只在选定位置 $i_*$ 的整组实际 copies 中，把 $u_0$ 换成 $Ev_\eta$。
其半母三矩固定，故该位置每个真实副本的完整三矩都原样固定。
所有它与其它编码位置之间的 $\Gamma$，以及 R280 三个有序矩面积全部不变。

剩下仅有 self 变化。由(3)，任一 reflection-even area 的变化准确为
$$
\Delta E_{04}=BR_{i_*}\,\Delta A_\alpha,\qquad
\Delta E_{22}=\frac{9B}{2}R_{i_*}\,\Delta A_\alpha.
\tag{27}
$$
两者都为零。角 odd 的原十二阶有限差分和空间反射结构共享同一个实际变化，继续清零；没有在一个单副本中单独变母。

同样，$\Delta A_{\mathfrak j}=\Delta A_{\mathfrak k}=0$，
所以全模块的原 $\mathfrak j,\mathfrak k$ 保持零。
新的 $\Omega$ 却准确为
$$
\boxed{\Delta\Omega=\frac{7B}{2}R_{i_*}\,\eta.}
\tag{28}
$$
固定一个足够小的实际 $\sigma>0$，沿(19)选相反参数，
便得到两个真正的强完整模块 $\mathcal C_+,\mathcal C_-$，满足
$$
\boxed{
\Omega(\mathcal C_\pm)=\pm\sigma,\qquad
\text{全部18面积}=0,\qquad \mathfrak j=\mathfrak k=0.
}
\tag{29}
$$

每个微包的 f、g 仍是同一个实紧 profile 的两个实倍数；
因此强 hook 条件逐包保留。每个完整八副本共享变化后的基础 profile，
原 cubic 平移次数不变，故原七次差分仍支付完整第三场的真左尾。
十二副本与 R280 五完整块的原权、右锚和共享初值没有改变。
(29)不是只到对角第三或只保几个端矩的结论。

原 $ZP0$ self 的非零常数系数同时说明(19)固定
$C(u)=\int(u'')^4$ 的实际 copy 和。
更直接地，(29)给原 quartic 圆张量身份；在强块上 $W=0$，R325(30)于是给
$$
\Psi_\theta(\mathcal C_\pm)=\psi_\pm\sin^2\theta,\qquad \psi_\pm>0.
\tag{30}
$$
$\psi_\pm$ 都是真实有限原值。三条 directed 行暂保为其真实有限值，
没有在这一步宣称它们零。

## 7. 正幅、大有限伸缩与原弱基线的精确相接

取 R379 末控制器以前的同一个真实弱基线 $\mathcal B$。
其全部18面积、原 $\mathcal T$ 已零，弱 rank-two 核、宽过渡、补矩、
全部既定中心及完整第三都固定，且
$$
\Psi_\theta(\mathcal B)=-\Delta\sin^2\theta,\quad \Delta>0,\qquad
\Omega(\mathcal B)=\Omega_0\in\mathbb R.
$$
这是完整实际基线，不能只保一个未补矩 weak core。

若 $\Omega_0=0$，无需新补偿。
否则取(29)中与 $\Omega_0$ 异号的 $\mathcal C$。
正伸缩 $f_H(x)=f(x/H)$、$g_H(x)=g(x/H)$ 的完整权是
$$
\Omega(\mathcal C_H)=H^{-3}\Omega(\mathcal C),\qquad
\Psi(\mathcal C_H)=H^{-7}\Psi(\mathcal C).
\tag{31}
$$
第一式直接由 $f_H'-xf_H''=H^{-1}(f'-yf'')$ 得；
第二式对强完整块是 R325 的真实 $\int r^4$ 式，不是三导主项估计。

赋予这个实际模块正四次幅
$$
\rho_H^4=|\Omega_0|H^3/\sigma .
$$
它精确贡献 $-\Omega_0$，而 $\Psi$ 新成本是
$$
\frac{|\Omega_0|\psi_{\mathcal C}}{\sigma H^4}\sin^2\theta .
\tag{32}
$$
取一个足够大的有限 H，使该值小于 $\Delta/2$，
并使新模块的整个正、负包络分别落在旧偶基线两端之外。
所有旧中心原地不动。

每个完整块的 inner D 三矩各自为零，且完整第三已经支付，
故原 R325 的真二次尾／第三范围加法适用：
(29)的零面积、$\mathfrak j,\mathfrak k$、弱单 hook 与旧完整第三均同点保留。
局部 $\Omega$ 也严格相加。
于是同一个新弱基线 $\widehat{\mathcal B}$ 满足
$$
\boxed{
\Omega(\widehat{\mathcal B})=0,\quad
\text{全部18面积}=0,\quad \mathcal T=0,\quad
\Psi_\theta(\widehat{\mathcal B})<0\quad(\sin\theta\ne0).
}
\tag{33}
$$
其原弱 rank-two 开段没有改变。
$\Psi$ 和三 directed 行的归一、同一公共幅度及圆的三矩条件均按原齐次式保持；
必要的公共正归一只同乘零等式。

## 8. 同一个最终17行根闭合全部对称二history

现在从起点选择 R379 的末端强控制器，使用(33)这个新实际基线。
其原共母版本自身 $\Omega=0$；R379(33)已证明，
在完整 $\mathcal F_\star$ 纤维上，各母的 $\mathcal O$ 全部平移系数准确固定，
所以末端有限频率变化不会重开(33)。

先用该真实强控制器的静态正幅，准确使 $\Psi=0$。
这里须区分两个层级：
在允许纤维变化中，弱核固定，强块 $W=0$，
且 $\mathcal F_{\rm new}$ 保 $\int(u'')^4$；
因此按 R325(13)(30)及其§8，$\Psi$ 在每个纤维点已经准确保持。
三条 directed 行和原对称 $C^3$ 目标才由下一个共同根支付。
不能把 $\Psi$ 误称为需由17行根另外恢复的 $C^3$ 量。

保全部真实 copy 权、相对位置、原 Green、平台尾和强弱跨块初值，
应用 R379 的17个实际标量／204正列证明。
同一个实际有限 N 同时给原16个零和
$\mathcal Q_{ZZ,2}(\pi/2)=0$。
R379 的准确全角式现在是
$$
\mathcal Q_{ZZ,2}(\theta)=
\sin^2\theta\,\mathcal Q_{ZZ,2}(\pi/2)
+c_\Omega\sin^2\theta\cos^2\theta\,\Omega(\widehat{\mathcal B})=0.
\tag{34}
$$
所以在这个同一个最终真实偶弱圆上，
$$
\boxed{
P^2,\ PW,\ PZ,\ PY,\ ZW,\ Z^2,\ W^2,\ ZY,\ WY,\ Y^2
\text{ 的全部三个外矩、全部 }\theta\text{ 均为零}.
}
\tag{35}
$$
全18个反对称面积、$\mathcal T,\Psi$、三 directed 行和原指定一层也同时保持。
不拼接不同最终圆的零，不把有限主秩单独当成完整角函数已付。

## 9. 有限选择顺序与准确范围

全部选择都是有限的：

1. 固定 Gaussian 系数、原等背景编码和完整 copy 结构；在固定正半母区间上定义(5)—(7)。
2. 用§3—5的原有序加法、有限导数见证和 Laurent minor，
   选一个真实母及固定光滑方向，取得双侧有限 IFT 族。
3. 在该共同母构造的完整模板中只改一个共享编码位置，
   选出(29)两个真正的 $\Omega$ 双号模块；所有内部 supports、原尾和正权此时固定。
4. 对已经完成的弱基线使用一个有限 H 和真实正幅(32)，
   精确支付 $\Omega$ 并保负 $\Psi$ 储备。
5. 最后固定新末控制器的母、17种形状、204真实位置、静态正幅和有限幅盒，
   然后取一个共同有限 N。之后不再平移、重锚或单独修改旧块。
6. 所有正负支撑包络确定后，才按 R354 的 $\omega$ 下界桥和初选小 $h_e$
   安装同一实际几何及共振保护芽。非零共同 $h_e$ 因子只重标原行，
   不改变这里的零条件；不能把这个新设计当成旧冻结窄 I 的免费扩域。

本稿新增的是低层真实 $\Omega$ 控制和同圆完整 Gaussian 二history 支付。
原零／一history的全部函数、canonical 第四 period、
各平台／退化点／平端条件、整条路径 ruling 和同一 gauge 的 joint 相容仍须原式继续支付。
也不继承另一几何已付的 wholeE、Morse 或全局嵌入／reach。
