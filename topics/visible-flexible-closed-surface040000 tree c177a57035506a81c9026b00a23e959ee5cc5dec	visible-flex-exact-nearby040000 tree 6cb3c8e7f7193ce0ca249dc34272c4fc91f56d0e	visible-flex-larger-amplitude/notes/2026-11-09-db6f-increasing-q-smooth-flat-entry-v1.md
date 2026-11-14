# 从 Q=0 向上进入鞍领：光滑角数据的背景消去与阻尼能量

**状态：完整作者推导，待未参与者全文独审。** 2026-11-09，独立几何分工。
本稿给一个新的精确 PDE 存在定理，适用于 Q=aa''>=0 且 Q'>=0 的径向方向。
它允许角向非解析的光滑初值，特别是具有固定开片的局部 bump。
本稿不修改此前 Q'<=0 的冻结稿，不读优化数组，不运行 PDE、BVP、tail、RK 或网格。

证明采用标量背景 P 与 X=P+QZ。Q=0 处不直接除以 Q；
实际构造使用 Q+epsilon，最后对物理变量 X,Y 取极限。
有限 epsilon 的近似方程无需与原给定 a 几何相容。
本稿不把这个正 C 局部定理用于 C=0 角零点、正曲率出口或整个闭面。

## 1. 来源、分工与准确结论

Gauss–Codazzi 和变量 X=M/C、Y=1/C 使用
[固定 9daa8aba8a341855811d2f1c164bfb3ca7eab0bc](https://github.com/Rogerhu12/math-research/blob/9daa8aba8a341855811d2f1c164bfb3ca7eab0bc/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-root-monotone-flat-collar-smooth-data-v1.md)
的相同记号。
该单调下降定理已由
[15b02049c367e344901fb13264a950f8ff5bf933](https://github.com/Rogerhu12/math-research/blob/15b02049c367e344901fb13264a950f8ff5bf933/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-monotone-flat-collar-smooth-data-v1.md)
全文独审。其混合能量是本稿方法的来源。
本稿的新背景消去、反向权重及 Q=0 极限另行证明；
root 在讨论中参与核对任意解的运输估计、近似 PDE 身份和被动参数范围，
不计作本稿的独立审查人。

固定材料圆周 T_ell，a是 [0,T_0] 上的光滑正函数，记

$$
Q=aa'',\qquad \mu=a'/a,\qquad \beta=aa'.
\tag{1}
$$

假定

$$
0\le Q\le Q_*,\quad Q'\ge0,\quad
|\mu|+|\beta|\le B_* .
\tag{2}
$$

给定光滑周期初值 M_0,C_0，C_0>0。定义
X_0=M_0/C_0、Y_0=1/C_0、y_*=\min Y_0>0。

**定理。** 存在 T>0，使

$$
L=(M^2-Q)/C,\qquad
M_r=L_u-\mu M,\qquad C_r=M_u+\mu C+\beta L
\tag{3}
$$

在 [0,T]×T_ell 上有唯一光滑周期解，并保持 C>0。
存在时间可只依赖
T_0,ell,Q_*,B_*、||X_0||_{H^5}、||Y_0||_{H^4} 和 y_*，
不依赖 Q' 的大小或任何更高径向导数。
定理包括 Q(0)=0、Q先平零一段、Q在0处无穷阶消失、以及 Q恒等于0。

若初值光滑依赖紧区间中的被动参数，而 a,Q,mu,beta 对该参数固定，
统一的上述界给共同时间，实际解也联合光滑依赖参数。
没有声称截止族的全部高阶径向导数有统一界。

## 2. 物理变量与无 Q 背景

在 Y>0 时，(3) 等价于

$$
\begin{aligned}
X_r&=X X_u-QY Y_u-2\mu X-\beta X^3+\beta QXY^2,\\
Y_r&=X Y_u-Y X_u-\mu Y-\beta YX^2+\beta QY^3 ,
\end{aligned}
\tag{4}
$$

并通过
C=Y^{-1}、M=X/Y、L=(X^2-QY^2)/Y
还原 (3)。
(4) 是最终取极限的变量；不以 Z本身代替实际解。

先解标量方程

$$
P_r=P P_u-2\mu P-\beta P^3,\qquad P(0,u)=X_0(u).
\tag{5}
$$

这是 Q=0 时 X的完整方程。
沿 u'(r)=-P，值 p(r)=P(r,u(r)) 满足
p'=-2mu p-beta p^3。
设 m=1+||X_0||_{C^1}、Bbar=max(1,B_*)。
例如取

$$
T_P\le\min\{T_0,\,(28\overline Bm^2)^{-1},\,(4m)^{-1}\}
\tag{6}
$$

即可通过首次越界证明 |p|<2m。
对初始位置求导有
p_alpha'=(-2mu-3beta p^2)p_alpha，
故 |p_alpha|<=2m；
特征投影 u_alpha=1-int_0^r p_alpha >=1/2。
因此 (5) 有共同正时间内的真正光滑周期解，且 P的 C1 范数统一有界。

对 (5) 作角向整数阶能量估计，Leibniz 公式和运输项分部积分给

$$
\frac d{dr}\|P\|_{H^s}^2
\le c_s(1+\|P\|_{W^{1,\infty}})^4\|P\|_{H^s}^2 .
\tag{7}
$$

常数还可依赖 B_*、ell，但没有径向系数导数。
所以所有高阶角范数在同一 T_P 内有界，不需按 s缩短时间。
低阶 H5界只依初始 H5界及上述共同常数。
光滑参数依赖直接由特征 ODE 及其保持可逆的投影得到。

## 3. 正则化后精确的阻尼系统

取 0<epsilon<=1，记

$$
q=Q+\epsilon,\qquad
\sigma=Q'/q\ge0,\qquad
X=P+qZ .
\tag{8}
$$

本节的小写 q只是近似系数，不是任何球面种子的常数。
把 (8) 代入 (4)，暂以 q代替 Q，可精确得到

$$
\begin{aligned}
Z_r={}&(P+qZ)Z_u-Y Y_u-\sigma Z\\
 &+(P_u-2\mu-3\beta P^2)Z
       -3\beta qPZ^2-\beta q^2Z^3+\beta(P+qZ)Y^2,\\
Y_r={}&(P+qZ)Y_u-qY Z_u
       -YP_u-\mu Y-\beta Y(P+qZ)^2+\beta qY^3 .
\end{aligned}
\tag{9}
$$

初值为

$$
Z(0,u)=0,\qquad Y(0,u)=Y_0(u).
\tag{10}
$$

(5) 恰消去不带 q的背景项，q'Z/q成为第一式的负阻尼。
例如 X X_u-P P_u
=q(PZ_u+ZP_u)+q^2ZZ_u，
以及 X^3-P^3=q(3P^2Z+3qPZ^2+q^2Z^3)，
逐项即给 (9)。

有限 epsilon 的 (9) 只是光滑近似 PDE：
它使用原 mu,beta，却把 Q替换成 q。
不声称 q=aa''，不重构一个伪称与原 g一致的近似曲面。
只有 epsilon->0 后的 (4) 用于实际几何。

## 4. 反向混合能量与有利的 Q' 项

以下 D=partial_u，s>=4。使用一维周期乘积及交换子估计

$$
\|fg\|_{H^s}\le c_s(\|f\|_\infty\|g\|_{H^s}
                         +\|g\|_\infty\|f\|_{H^s}),
$$

$$
\|[D^s,f]Dg\|_2
\le c_s(\|Df\|_\infty\|g\|_{H^s}
                         +\|Dg\|_\infty\|f\|_{H^s}).
\tag{11}
$$

它们可由整数阶 Leibniz 展开、一维 Sobolev 插值与 Young 不等式证明；
来源 1 的 §§3–5 给出了同一估计的完整用法。
所有导数在角方向，q、sigma、mu、beta不产生交换子。

令

$$
E_s=q\|Z\|_{H^s}^2+\|Y\|_{H^s}^2+\|Z\|_{H^{s-1}}^2 ,
\qquad
K_1=1+\|P\|_{H^5}+\|Z\|_{W^{1,\infty}}
                         +\|Y\|_{W^{1,\infty}} .
\tag{12}
$$

对 (9) 取 j阶角导数，最高项为

$$
(Z_j)_r=X(Z_j)_u-Y(Y_j)_u-\sigma Z_j+\cdots,
$$

$$
(Y_j)_r=X(Y_j)_u-qY(Z_j)_u+\cdots,\quad X=P+qZ.
\tag{13}
$$

分别与 qZ_j、Y_j 配对。
在半能量导数中，权重导数与阻尼之和恰为

$$
\frac12q'\|Z_j\|_2^2-q\sigma\|Z_j\|_2^2
=-\frac12Q'\|Z_j\|_2^2\le0 .
\tag{14}
$$

最高交叉项则恰消去为

$$
-q\int Y\{Z_j(Y_j)_u+Y_j(Z_j)_u\}\,du
=q\int Y_u Z_jY_j\,du .
\tag{15}
$$

其绝对值不超过
sqrt(q)||Y_u||_infinity
(q||Z_j||_2^2+||Y_j||_2^2)/2。
对角运输项为
-int X_u(qZ_j^2+Y_j^2)/2。
这里 q<=Q_*+1，所有系数统一有界。

交换子的权重也完整匹配。例如第一式中 -[D^j,Y]Y_u
与 qZ_j 配对给
c sqrt(q)||Y_u||_infinity
sqrt(q)||Z||_{H^j}||Y||_{H^j}。
第二式的 -q[D^j,Y]Z_u 同样受控。
运输系数 X=P+qZ 中的高阶 Z总带 q，
所以第二式的运输交换子不会出现裸露的 Hs阶 Z。
含 P的项只需要 P的已知 Hs或Hs+1范数。

零阶项也保留这一结构：Z方程可不带 q依赖 Y，
但它与 qZ_j 配对；Y方程对 Z的每一项都带 q。
P_u Z、Y P_u 的高阶项用已知的 ||P||_{H^{s+1}}。
所以加权高阶部分满足一个上界
c_s(K_1)(E_s+||P||_{H^{s+1}}^2)，
不含 q^{-1} 或 sigma的正系数。

最后对 Z方程只取 s-1阶并直接与 Z_j 配对。
唯一需要增加一阶的项 -Y Y_u 由 ||Y||_{H^s} 控制；
X Z_u 是通常运输项。
负阻尼在这里给
-2sigma||Z||_{H^{s-1}}^2，
没有使用 q的正下界。合并得

$$
\boxed{\quad
E_s'+Q'\|Z\|_{H^s}^2
   +2\sigma\|Z\|_{H^{s-1}}^2
\le c_s(K_1)\{E_s+\|P\|_{H^{s+1}}^2\}.
\quad}
\tag{16}
$$

c_s还可依赖 ell,Q_*+1,B_*，而不依赖 epsilon、Q'或更高径向导数。
这就是与单调下降能量互补的方向；不能删掉背景 (5) 而保留 (14)。

## 5. 同一正时间内的 Galerkin 构造

令 P_N 为角 Fourier正交投影，保留 |n|<=N。
把 (9) 两个完整右端投影，以 (0,P_NY_0) 为初值。
背景 P仍用 (5) 的真实解。
对每个 epsilon>0，这是一组系数光滑的有限维多项式 ODE。

P_N与角导数及径向标量交换。
能量配对的 Z_j、Y_j 在投影空间内，
故外层 P_N可在配对时消掉，(16) 保持同一常数。
尤其阻尼仍精确是 -sigma Z_N。

由一维 Sobolev 嵌入，
E_4控制 Y的H4和Z的H3，
从而控制两者的 W1,infinity 范数。
P的H5已经在统一 T_P内受控。
因此选一个大于统一初始 E_4与P低阶界的固定 B，
再由首次越界估计选 T_1>0，
可以使所有 epsilon,N 解在 [0,T_1] 上 E_4<B。
T_1只依定理列出的数据，有限维解在这个区间内不会爆破。

(9) 的 Y方程完全没有 sigma。
上述低阶界给统一

$$
\|(Y_{\epsilon,N})_r\|_{H^2}\le C(B).
\tag{17}
$$

所有充分大的 N满足 P_NY_0>=3y_*/4。
再统一缩短时间，使 (17) 的 C0积分变化<=y_*/4，
便有 Y_{epsilon,N}>=y_*/2。
有限个小N不参与取极限；近似 ODE本身也不需先假定 Y>0 才能定义。

现在固定任意 s>=4。
低阶控制使 (16) 的 c_s(K_1) 一致有界；
(7) 已在同一时间上控制 P的Hs+1。
Gronwall因而给每一个 E_s一致界。
**所有 s使用同一个已经选定的 T**，不按高阶数据再缩短时间。
用 E_{s+1} 可在 q接近0处仍控制 Z的非加权 Hs范数。

## 6. 对实际 X,Y取极限，而不强求 sigma Z的等度连续

近似 Z的时间导数含 sigma，不能据 (16) 就声称它统一有界。
改令

$$
X_{\epsilon,N}=P+qZ_{\epsilon,N}.
\tag{18}
$$

把 (9) 第一式写成 Z_r=P_N R_Z-sigma Z，
其中 R_Z是删去负阻尼的右端。
由于 q'=Q'、q sigma=Q'，

$$
(X_{\epsilon,N})_r=P_r+qP_N R_Z .
\tag{19}
$$

这里 sigma项**精确抵消**。
由全部角向界，(19) 和 Y方程在每个有限角 Sobolev阶
都有统一时间导数界。

等价地，(19) 与 (4) 的 q版本只差 q(P_N-I)R_Z；
R_Z的任意高角范数一致有界，故该投影尾在低阶范数趋0。
Y方程的投影尾也一样。
因此可取 epsilon_j->0、N_j->infinity 的对角子列，
用紧的角 Sobolev嵌入和 Arzela–Ascoli，
使实际 X_{epsilon,N},Y_{epsilon,N}
在 C([0,T],H^k) 中对所有有限 k强收敛。

在这些范数中乘积连续，q->Q；
极限满足原 (4)、实际初值 X_0,Y_0及Y>=y_*/2。
(4) 先给一次径向导数。
对固定光滑系数反复微分，并使用已得全部角向导数，
得到联合 C-infinity。
由 C=1/Y、M=X/Y、L=(X^2-QY^2)/Y 得到实际 (3)。
高径向导数无需在不同截止之间一致有界。

## 7. 任意光滑解的唯一性：没有附加隐藏的 Z初值

须证明唯一性属于原物理方程，而不只是选了 Z(0)=0 的近似族。

令 (X,Y) 为任意同初值光滑解，V=X-P。
由 (4) 与 (5)，

$$
V_r=X V_u+A V+QF,\qquad V(0)=0,
$$

$$
A=P_u-2\mu-\beta(X^2+XP+P^2),\qquad
F=-Y Y_u+\beta XY^2 .
\tag{20}
$$

这是沿速度 -X 的线性运输方程。
对任意有限角阶作能量估计，已知光滑系数在紧时间窗有界，
Duhamel或Gronwall给

$$
\|V(r)\|_{H^s}
\le C_s\int_0^r Q(t)\,dt
\le C_s rQ(r).
\tag{21}
$$

最后一步仅用 Q非减。
所以在 Q>0 上，Z=V/Q 的每个 Hs范数是 O(r)，
而不是未经证明地假设有限。

如果 Q先在 [0,r_*] 恒为0，
(20) 先给 X=P；
Y则满足唯一的线性运输方程
Y_r=P Y_u-(P_u+mu+beta P^2)Y。
从 r_*重新积分 (20)，有
||V(r)||Hs<=C_s(r-r_*)Q(r)，
故 Z在正侧的所有有限角阶趋0。
若 Q恒为0，以上三角系统已给全部唯一性。

对两个光滑解，在 Q>0 上取其 Z,Y之差。
主矩阵仍是

$$
\begin{pmatrix}X_1&-Y_1\\-QY_1&X_1\end{pmatrix},
$$

且第一分量有负阻尼 -(Q'/Q)delta Z。
零阶差矩阵的结构为

$$
\begin{pmatrix}b_{11}&b_{12}\\Qb_{21}&b_{22}\end{pmatrix}.
\tag{22}
$$

第二行对 Z的耦合确实带Q，因为 X=P+QZ。
所有 b系数在正侧有界到任意所需角阶，
由 (21) 其界不在 r趋r_*时爆破。
对差使用 (16) 的同型能量，得到 E_diff'<=C_s E_diff，
其中有利阻尼被丢掉，常数独立于起点离 r_*多近。
从 r=r_*+h积分再令 h下降到0；
(21) 和相同 Y初值使 E_diff(r_*+h)->0。
于是差为0，唯一性对所有原光滑解成立。

## 8. 光滑被动参数

参数只改变初值，不改变 a,Q,mu,beta。
背景 P的参数导数由特征 ODE 在同一个时间窗内控制。
对有限 epsilon,N 的方程求参数导数，
最高阶导数仍满足 (13) 的主矩阵和同一负阻尼；
零阶矩阵仍有 (22) 的结构。
已知 P参数导数及低参数阶项只形成非齐次项。
利用先前已控制的任意高角阶，逐参数阶对混合能量作归纳，
得到不依 epsilon,N 的全部有限参数导数界。

sigma不依参数，因此不会出现未知的 sigma参数导数。
重建 X=P+qZ 后，参数微分的时间导数也按 (19) 抵消sigma。
同样的紧性论证把这些导数传到极限；
分布导数的唯一性使其成为实际解的参数导数。
最后由原方程作径向 bootstrap，得到完整联合光滑族。
若 Q或a也依参数，则需另行核查，本文不声称该更广范围。

## 9. 实际平坦出口再进入负曲率

取
[69ea0bcb043eca3d051fe020489eb418c9271466](https://github.com/Rogerhu12/math-research/blob/69ea0bcb043eca3d051fe020489eb418c9271466/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-flat-outlet-ruling-continuation-v1.md)
中由真实位置和标架给定的正 C平坦入口，a(0)=a_0>0、a'(0)=B>=0。
该母线稿自己的独审身份独立；本节也可直接用任何已存在的平坦入口。

令 chi为固定非减光滑函数，chi=0于 x<=1/4，chi=1于 x>=3/4，
0<=chi<=1。对固定 q_*>0 及待选 delta，取

$$
Q_\delta(r)=q_*\chi(r/\delta),\qquad
a_\delta''=Q_\delta/a_\delta,\quad
a_\delta(0)=a_0,\quad a_\delta'(0)=B.
\tag{23}
$$

在一个固定小径向窗，标量ODE给 a严格正，
a,a',mu,beta有与delta无关的统一界。
初始 X_0,Y_0以及低阶角范数也不依delta。
本定理先给共同 T>0，再选 0<delta<T/2。
整个上升段和其后的正Q开领都在已证寿命内。

以真实入口位置和实际框架重构

$$
F_r=e_1,\quad (e_1)_r=LN,\quad
(e_2)_r=(M/a)N,\quad N_r=-Le_1-(M/a)e_2 .
\tag{24}
$$

(3) 是它与角向框架方程的相容条件，角方程误差为齐次线性径向系统。
故实际诱导度量是共同 g=dr^2+a_delta^2du^2。
周期初值与周期系数使位置及框架一起周期；
C3也同样保留，没有平移monodromy自由量。
在 r<=delta/4，Q=0、a=a_0+Br；
§7 唯一性和实际位置初值给与旧平坦领的开重叠一致，全部jet匹配。

新领 r>=3delta/4 的 K=-q_*/a_delta^2<0，
所以这是真正的非平曲率入口。
角数据可以非解析，旧域中的固定H仍逐点固定。
由统一低阶界和单位径向速度，把delta再缩小，
可使新增图在 C1内保持全时间嵌入；明确数值预算在另稿实际圆柱实例中给出。
这里不把局部延拓预支成指定终端边值解、闭面或有效幅度。

## 10. 检查身份与未付关口

本稿的核心步骤是 (14) 的阻尼符号、
(16) 的权重完整性、(19) 的实际变量紧性、
以及 (21) 对任意原解的唯一性入口。
它们需要全文独立审查，有限代数恒等式不能替代存在证明。

没有新的数值或终端数学程序执行声明。
后续具体实例须固定共同 a、参数范围、材料H与实际位置，
并重新证明全E(3)、嵌入和reach。
本定理始终在 C>0 图内，未处理 R43 的角零点或转入正曲率后的完整接合。
