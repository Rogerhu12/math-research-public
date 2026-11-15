# R255：完整第三对角核的具体三维补串与双混合响应公式

日期：2026-11-15。**完整纸面证明。** 本稿继承 R254 的八个真实提升及十八维对角像，没有运行新的原式编译、旧列恢复、profile 评价、正规化或矩阵消元。

新增结论有两项。第一，给出 $Z_{71}$ 中既有七维 hook 串之外的真实三维 $V_2$ 的三个准确完整原索引公式，因而第三对角核 $Z$ 的十八个生成元均可明确写出。第二，对任意完整第三对角零算子给出保全部历史项的完整响应公式和固定圆的两个真实混合目标。后者不是固定圆 period 商已经满射的断言。

来源：[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R87](R87-exact-complete-P1-separation-and-smooth-moment-circles.md)、[R208](R208-every-universal-pure-response-has-a-second-jet-representative.md)、[R213](R213-two-mixed-sources-and-gauge-invariant-platform-obstructions-after-pure-closure.md)、[R247](R247-complete-response-Jacobi-presentation-and-pure-kernel-decomposition.md)、[R254](R254-eight-exact-third-diagonal-lifts-and-eighteen-dimensional-image.md)。

## 1. 记号和全部右尾

采用 R247/R254 的完整三槽：
$$
C(A,B)(a;b,c)
=\Phi_A(a,\Phi_B(b,c))-\Phi_B(a,\Phi_A(b,c)).
\tag{1}
$$
$C_i$ 是 E 坐标 $(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$ 的全部 $i<j$ pair 字典序，原索引从零开始。记
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},
\quad L=\Phi_{p_0},\quad U=\Phi_{s_1},
\quad V=\Phi_{p_1},\quad T=\Phi_{t_1},\quad E_+=\Phi_{p_2}.
\tag{2}
$$
式 (1) 中把上述符号直接作为二次算子使用，例如 $C(P,T)=C_{21}$。不能把它与原八维空间中的标量坐标混同。

为便于纸面分部积分，本稿记
$$
\mathcal J(F)(x)=\int_x^{r_*}F(\xi)\,d\xi=-I(F)(x).
\tag{3}
$$
这是正右积分，故 $\mathcal J(F)'=-F$。所有输入及相关端项在共同右 collar 为零；完整左尾保留。(3) 只是记号换号，不更换物理右锚。

对任意 $a,b$ 记
$$
J_2(a,b)=\mathcal J\{x^2a''b''+2a'b'\}.
$$
R73 的完整八矩二次式在 (2) 的记号中为
$$
\begin{aligned}
P(a,b)&=\mathcal J(a''b''),\\
R(a,b)&=a'b'+xP(a,b),\\
S(a,b)&=\mathcal J(xa''b''),\\
L(a,b)&=\tfrac12(ab'+a'b)-\tfrac{x}{2}a'b'
-\tfrac{x^2}{4}P(a,b)+\tfrac14J_2(a,b),\\
U(a,b)&=xa'b'+xS(a,b)+\tfrac12J_2(a,b),\\
V(a,b)&=-\tfrac12ab+\tfrac{x}{2}(ab'+a'b)
-\tfrac{x^2}{2}a'b'-\tfrac{x^2}{4}S(a,b),\\
T(a,b)&=x^2a'b'+xJ_2(a,b),\\
E_+(a,b)&=-xab+\tfrac{x^2}{2}(ab'+a'b)
-\tfrac{x^3}{2}a'b'-\tfrac{x^2}{4}J_2(a,b).
\end{aligned}
\tag{4}
$$
下面只用这些完整原式作纸面导数与分部积分；没有把任何原函数截成局部项。

## 2. 一个明确的最低权对角零算子

定义
$$
\boxed{
\mathfrak J
=4C(L,R)-4C(L,S)-3C(P,T)+2C(R,U)+4C(S,U).
}
\tag{5}
$$
按完整原索引，即
$$
\boxed{\mathfrak J=4C_3-4C_4-3C_{21}+2C_{23}+4C_{25}.}
\tag{6}
$$
本节证明
$$
N\mathfrak J=0,\qquad H\mathfrak J=-\mathfrak J,\qquad
\Delta\mathfrak J=0,\qquad \mathfrak J\ne0.
\tag{7}
$$
其中 $\Delta\tau(q)=\tau(q;q,q)$。

### 2.1 完整平移导子

对任意多线性算子，取 R247 的
$$
N=\mathscr L_{\partial_x},\qquad
H=\mathscr L_{x\partial_x-1},\qquad
\delta=\mathscr L_{x^2\partial_x-2x}.
\tag{8}
$$
$N$ 在组合上满足 Leibniz 规则。由 (4)、共同右零 collar 及 $\mathcal J(D F)=-F$，逐项得
$$
\begin{aligned}
NP&=0,& NR&=NS=P,& NL&=-\tfrac12(R-S),\\
NU&=R+2S,& NV&=L-\tfrac12U,& NT&=2U,\qquad
NE_+=2V-\tfrac12T.
\end{aligned}
\tag{9}
$$
这些是完整二次算子身份，不仅是对角式。令 $Q=R-S$。则 $NQ=0$，于是 (5) 的前两项 $4C(L,Q)$ 在 N 下为零。其余三项的 N 像为
$$
-6C(P,U)+2\{C(P,U)+2C(R,S)\}
+4\{C(P,U)-C(R,S)\}=0.
$$
故 $N\mathfrak J=0$。

(4) 中各二次算子的 H 权依次为
$$
P:-2,\quad R,S:-1,\quad L,U:0,\quad V,T:1,\quad E_+:2.
$$
因此 (5) 的全部完整三次项 H 权均为 $-1$，得到 (7) 的第二式。这里三线性 H 权等于真仿射权加二，所以 $\mathfrak J$ 的真仿射权为 $-3$。

### 2.2 在重标查询点零处的准确同锚分部积分

先在一个查询点坐标为零、右锚为任意 $r_*>0$ 的区间写原式。这里只是一个通用坐标计算；第 2.3 节把它搬回任意原物理查询点，不要求原允许区间包含零。

记
$$
p=q',\qquad r=q'',\qquad t=q''',
$$
并将没有积分符号的量都在查询点零处评价。定义四个真实尾量
$$
\begin{aligned}
\mathsf A&=\mathcal J(qr^2)(0),&
\mathsf B&=\mathcal J(xpr^2)(0),\\
\mathsf C&=\mathcal J(x^2r^3)(0),&
\mathsf D&=q(0)P(q,q)(0)+p(0)S(q,q)(0).
\end{aligned}
\tag{10}
$$
它们始终是同一个真实 q 的积分和局部值，没有独立赋值。

原二次对角式及所需导数，由 (4) 给出：
$$
\begin{aligned}
P(q,q)'&=-r^2,\\
R(q,q)'&=2pr+P(q,q)-xr^2,&
R(q,q)''&=2(p-xr)t,\\
S(q,q)'&=-xr^2,&
S(q,q)''&=-r^2-2xrt,\\
L(q,q)'&=(q-xp)r-\tfrac{x}{2}P(q,q),&
L(q,q)''&=(q-xp)t-\tfrac12\{xr^2+P(q,q)\},\\
U(q,q)'&=2xpr+S(q,q)-\tfrac32x^2r^2,&
U(q,q)''&=2pr-2xr^2+2xpt-3x^2rt,\\
T(q,q)''&=-2p^2+4xpr-2x^2r^2+2x^2pt-2x^3rt.
\end{aligned}
\tag{11}
$$

下面列出全部用到的非平凡积分改写；右端端项均由同一零 collar 消失，左端的 $qP,pS,p^3$ 保留：
$$
\begin{aligned}
\mathcal J(p^2r)(0)&=-p(0)^3/3,\\
\mathcal J(pP(q,q))(0)&=-q(0)P(q,q)(0)+\mathsf A,\\
\mathcal J(x^2prt)(0)&=-\mathsf B-\mathsf C/2,\\
\mathcal J(x^3r^2t)(0)&=-\mathsf C,\\
\mathcal J(xqrt)(0)&=-\mathsf A/2-\mathsf B/2,\\
\mathcal J(xrP(q,q))(0)&=q(0)P(q,q)(0)-\mathsf A+\mathsf B.
\end{aligned}
\tag{12}
$$
例如第三式来自 $rt=(r^2)'/2$；第六式来自
$D(xpP)=pP+xrP-xpr^2$。这些改写完整保留原函数的真实耦合。

将 (11) 代入五个完整 C 的对角，使用 (12)，得到：
$$
\begin{aligned}
\Delta C_3(0)&=\frac{p^3}{6}+\frac{\mathsf A}{2}
-\mathsf B+\frac{\mathsf C}{4},\\
\Delta C_4(0)&=\frac{\mathsf D}{2}
-\frac{\mathsf B}{2}+\frac{\mathsf C}{4},\\
\Delta C_{21}(0)&=\frac{2p^3}{3}+2\mathsf B-\mathsf C,\\
\Delta C_{23}(0)&=\mathsf D+\frac{2p^3}{3}
-\mathsf A+2\mathsf B-\frac{\mathsf C}{2},\\
\Delta C_{25}(0)&=\mathsf B-\frac{\mathsf C}{2}.
\end{aligned}
\tag{13}
$$
为使此表可直接手核，五个未改写表达式依次为：
$$
\begin{aligned}
\Delta C_3(0)
={}&\frac{qP+p^3}{2}
+\mathcal J\!\left(
\frac{x^2prt}{2}-\frac{x^3r^2t}{2}
+p^2r+\frac{pP}{2}-\frac{xpr^2}{2}\right)(0),\\
\Delta C_4(0)
={}&\frac{pS}{2}
+\mathcal J\!\left(
\frac{x^2r^3}{4}-\frac{x^3r^2t}{2}
-\frac{xpr^2}{2}-xqrt+x^2prt+\frac{xrP}{2}\right)(0),\\
\Delta C_{21}(0)
={}&\mathcal J\!\left(
-2p^2r+4xpr^2-2x^2r^3+2x^2prt-2x^3r^2t\right)(0),\\
\Delta C_{23}(0)
={}&pS+\mathcal J\!\left(
-x^2prt+x^3r^2t-2p^2r-pP+xpr^2\right)(0),\\
\Delta C_{25}(0)
={}&\mathcal J\!\left(
3xpr^2-\frac32x^2r^3+2x^2prt-2x^3r^2t\right)(0).
\end{aligned}
\tag{14}
$$
(14) 中 P、S 的未写输入均为 $(q,q)$。直接把 (13) 乘以 (6) 的系数相加，$p^3,\mathsf A,\mathsf B,\mathsf C,\mathsf D$ 的每个系数分别为零。故
$$
\Delta\mathfrak J(q)(0)=0
\tag{15}
$$
对全部上述真实 q 及任意允许右锚成立。

### 2.3 任意物理查询点与移动上锚

现在取原允许物理区间内任意查询点 $x_0$，令
$$
y=x-x_0,\qquad \widetilde q(y)=q(x_0+y),\qquad
\widetilde r_*=r_*-x_0.
$$
原同锚积分准确变成
$$
\int_x^{r_*}F(\xi)\,d\xi
=\int_y^{\widetilde r_*}F(x_0+\eta)\,d\eta.
\tag{16}
$$
共同零 collar 同时平移；没有把右端积分常数丢掉。重标后的算子是原显式多项式系数 $x$ 改为 $y+x_0$ 的共轭。其平移导子正是 N，因此有限多项式平移作用为 $\exp(x_0N)$。这个断言也可由 (4)、(9) 逐个展开；在零 collar 内改变锚位置不改变积分值。

由于 $N\mathfrak J=0$，重标后的 $\mathfrak J$ 与以 y 为坐标、以 $\widetilde r_*$ 为右锚的同一个公式相等。将 (15) 用于 $\widetilde q$，便得
$$
\Delta\mathfrak J(q)(x_0)=0.
\tag{17}
$$
$x_0$ 任意，(17) 是完整 universal 函数身份。这里平移是证明中的坐标重标，不是对某个固定圆宣称已有实际几何控制；也没有假定原物理区间含有坐标零。

### 2.4 完整非零

(6) 是原 28 个完整交换子的非零常系数组合。R87 已付这 28 个完整三槽算子的真实独立性。因此 $\mathfrak J\ne0$。这一步不以原项数、形式符号独立或新采样代替真实证据。

## 3. 三条完整生成元与对角核的具体分解

### 3.1 完整 E 表的 projective 导子

把 $\delta=\mathscr L_{x^2\partial_x-2x}$ 作用于 (4)，完整分部积分给：
$$
\begin{aligned}
\delta P&=-2(R+S),&
\delta R&=4L-2U,&
\delta S&=-2U,\\
\delta L&=-2V-\tfrac12T,&
\delta U&=4V-2T,&
\delta V&=-E_+,\\
\delta T&=4E_+,&
\delta E_+&=0.
\end{aligned}
\tag{18}
$$
例如 $D^2(x^2a'-2xa)=x^2a'''+2xa''-2a'$；代入 $\delta P$ 后使用
$$
\mathcal J\{D(x^2a''b'')+2xa''b''-2D(a'b')\}
=-x^2a''b''+2S(a,b)+2a'b',
$$
即得第一式。其余各式由 (4) 同样逐项核验，保全部 J 项。也可用 (9)、$[N,\delta]=2H$ 及已付 E 的 $V_4\oplus V_2$ 结构核其系数；没有恢复或计算新原列。

$\delta$ 对完整 C 满足
$$
\delta C(A,B)=C(\delta A,B)+C(A,\delta B).
\tag{19}
$$
因此 (6)、(18) 给出：
$$
\boxed{
\begin{aligned}
\mathfrak J_0&=\mathfrak J
=4C_3-4C_4-3C_{21}+2C_{23}+4C_{25},\\
\mathfrak J_1&=\delta\mathfrak J
=8C_5-16C_9-8C_{10}+12C_{13}+4C_{24}-4C_{26},\\
\mathfrak J_2&=\delta^2\mathfrak J
=96C_0+32C_{11}-24C_{14}+4C_{27}.
\end{aligned}
}
\tag{20}
$$

为固定索引和符号，后两式还可写为
$$
\begin{aligned}
\mathfrak J_1
={}&16C(R,V)+8C(S,V)+4C(R-S,T)
+8C(L,U)-12C(P,E_+),\\
\mathfrak J_2
={}&96C(L,V)+32C(V,U)+4C(U,T)+24C(R,E_+).
\end{aligned}
\tag{21}
$$
再次施 (18)、(19)，$\mathfrak J_2$ 的导数为
$$
\begin{aligned}
&48C(V,T)-96C(L,E_+)\\
&\quad-32C(E_+,U)-64C(V,T)\\
&\quad+16C(V,T)+16C(U,E_+)\\
&\quad+96C(L,E_+)-48C(U,E_+)=0.
\end{aligned}
$$
因此
$$
\boxed{\delta^3\mathfrak J=0.}
\tag{22}
$$
这个核零是完整三槽的纸面身份，不是只在对角的推断。

### 3.2 三条真实独立，且完整对角为零

对角映射与 N、H、$\delta$ 的同时输入/输出作用交换。由 (17) 得
$$
\Delta\mathfrak J_0=\Delta\mathfrak J_1
=\Delta\mathfrak J_2=0.
\tag{23}
$$
又由 (7) 和 sl2 关系，
$$
N\mathfrak J_1=-2\mathfrak J_0,\qquad
N\mathfrak J_2=-2\mathfrak J_1.
\tag{24}
$$
$\mathfrak J_0\ne0$，故后两条也非零；三者 H 权分别为 $-1,0,1$，所以真实独立。于是
$$
\mathfrak J_3=\operatorname{span}\{\mathfrak J_0,\mathfrak J_1,\mathfrak J_2\}
\simeq V_2.
\tag{25}
$$

R247 已证明
$$
\mathfrak H=C(P,S)-3C(P,R),\quad
\Delta\mathfrak H=0,\quad
\mathfrak H_7=\operatorname{span}\{\delta^j\mathfrak H:0\le j\le6\}
\simeq V_6.
$$
两个不同不可约模交零。R254 已给真实 $\dim Z_{71}=10$，所以本稿的显式升级是
$$
\boxed{Z_{71}=\mathfrak H_7\oplus\mathfrak J_3.}
\tag{26}
$$
再把 R254 的八个完整 $\chi_j=\tau_j-\gamma_j$ 加入，得到完整第三对角核的一组明确十八元生成：
$$
\boxed{
Z=\mathfrak H_7\oplus\mathfrak J_3
\oplus\operatorname{span}\{\chi_{30},\chi_{32},\chi_{34},
\chi_{37},\chi_{40},\chi_{100},\chi_{104},\chi_{109}\}.
}
\tag{27}
$$
(27) 的最后八维直和是原完整空间中的直和，不宣称该补空间对 $\delta$ 不变。

## 4. 任意第三对角零算子的完整 hook 公式

以下不要求 $\tau\in W_{71}$，只要 $\tau$ 是最后两槽对称的完整三线性算子，并满足 $\Delta\tau=0$。因此适用于 (27) 的全部十八个生成元。

### 4.1 极化身份保全部槽

在 $\Delta\tau(\phi+\epsilon b)=0$ 中取 $\epsilon$ 的一次系数，得
$$
\boxed{\tau(b;\phi,\phi)+2\tau(\phi;\phi,b)=0.}
\tag{28}
$$
对固定真实 seed $f$，定义整个线性 profile 算子
$$
K_f^\tau(w)=\tau(w;f,f).
\tag{29}
$$
它保原右锚和原尾，且 $K_f^\tau(f)=0$。这是完整原算子，不预先认作某个局部微分算子或既有合法 gauge 的像。

令 $F=f^2$、$D=F-\phi^2$。R83/R247 的完整第四响应是
$$
\mathcal B_A(\tau)
=2\tau(\Phi_A D;D)-4\tau(\phi;\phi,\Phi_A D)
+4\Phi_A(\phi,\tau(\phi;D)).
\tag{30}
$$
对 $b=\Phi_A D$ 用 (28)，前两项恰变为 $2K_f^\tau(b)$；因为 $\Delta\tau(\phi)=0$，还有
$$
\tau(\phi;D)=\tau(\phi;f,f)-\tau(\phi;\phi,\phi)
=K_f^\tau(\phi).
$$
所以
$$
\boxed{
\mathcal B_A(\tau)(f^2,\phi)
=2K_f^\tau\!\left(\Phi_A(f^2-\phi^2)\right)
+4\Phi_A\!\left(\phi,K_f^\tau(\phi)\right).
}
\tag{31}
$$
特别，第二项是原式第三 history 项在对角核条件下的准确改写，不能省去。

### 4.2 同一固定圆的两个混合函数

现在固定任意真实 $f,g$，令
$$
\phi_\theta=c f+s g,\qquad c=\cos\theta,\quad s=\sin\theta,
\qquad \zeta_\tau=K_f^\tau(g).
$$
由 $K_f^\tau(f)=0$，
$$
K_f^\tau(\phi_\theta)=s\zeta_\tau,\qquad
D_\theta=s^2(f^2-g^2)-2cs\,fg.
$$
(31) 因而准确化为
$$
\boxed{
\mathcal B_A(\tau)(f^2,\phi_\theta)
=s^2\,\mathcal D_{A,\tau}+cs\,\mathcal E_{A,\tau},
}
\tag{32}
$$
其中
$$
\boxed{
\begin{aligned}
\mathcal D_{A,\tau}
&=2K_f^\tau\!\left(\Phi_A(f^2-g^2)\right)
+4\Phi_A(g,\zeta_\tau),\\
\mathcal E_{A,\tau}
&=-4K_f^\tau\!\left(\Phi_A(fg)\right)
+4\Phi_A(f,\zeta_\tau).
\end{aligned}
}
\tag{33}
$$
这保全部 phase。它对给定 $f,g$ 是整个输出函数的身份，既非单个点值，也非只一个局部端层。

如果额外已证明 $K_f^\tau(g)=0$，才可删去 (33) 中的两项 $\Phi_A(\cdot,\zeta_\tau)$。即使此值为零，也不能自动把 $K_f^\tau$ 当作原 $L_f$；$K_f^\tau=L_f$ 或某个准确比例必须另有原式身份。

R213/R247 对特定已付八包圆的 $\tau=\mathfrak H$ 已证明
$\mathcal B_A(\mathfrak H)=2L_f(\Phi_A D_\theta)$，且所用二阶 profile 合法。这是一个有额外来源的特殊情形。对 $\mathfrak J_0,\mathfrak J_1,\mathfrak J_2$ 及八个 $\chi_j$，(31)–(33) 本身不授该特殊结论。

### 4.3 这项改写保留了真实信息

对于全部 seed f 的族，$K_f^\tau$ 能恢复完整 $\tau$：最后两槽极化给
$$
\tau(w;b,c)
=\tfrac12\{K_{b+c}^\tau(w)-K_b^\tau(w)-K_c^\tau(w)\}.
\tag{34}
$$
因此使用 K 表示不是把完整三槽降成对角信息。但在一个已经固定的 f 上，$\tau\mapsto K_f^\tau$ 可能有核，不能从 universal 的 (34) 宣称固定 seed 仍忠实。

## 5. 对完整响应和完整 period 商的边界

(27)、(31) 为第三对角核产生的第四响应提供了具体完整来源。仅交换子部分的形式定义域为
$$
E\otimes Z_{71}
\simeq(V_4\oplus V_2)\otimes(V_6\oplus V_2),
$$
其维数 80；按不可约类型为
$$
V_{10}\oplus2V_8\oplus3V_6\oplus4V_4\oplus3V_2\oplus V_0.
\tag{35}
$$
这是已付有限模类型的纸面分解，不是八十个第四响应的真实秩。本次没有评价其中任何新第四响应，也没有把 (27) 的十八维乘以八后宣称得到 144 个独立真实成本。

更重要的是，R247 已明确
$$
\mathcal R_{\mathrm p0}
=(\mathcal R_{71}\cap\ker\pi)+\mathcal B(E,\operatorname{span}\chi_j),
\tag{36}
$$
而一般只能断言
$$
\mathcal B(E,Z_{71})\subseteq\mathcal R_{71}\cap\ker\pi.
$$
第三对角非零的若干方向仍可有 pure 零第四响应。故 (27) 不取代 (36) 的第一项，也不宣称第三对角核已经覆盖整个第四 pure 核。

对 R225 的完整固定圆 period 观测商，仍须将 (33) 的两个真实函数同时与全部合法 $L_f$ 的像比较，保平台、内部退化、总通量、平端延拓及右锚常数。同一圆上的这个商不是 sl2 模；$\delta$ 同时作用全部输入和输出，不能在应用 $\delta$ 后把 f、g、$L_f$ 假定不变。

(20)、(27) 和 (31)–(34) 是本稿已完成的完整原式结论。它们提供新的可消费生成元和准确双混合目标，但不预报其固定圆像秩，不把真实响应差的线性跨度等同于零基准有符号实际成本，也不授同一二阶 gauge 的完整 period/ruling 联调或主课题完成。

作者责任：本稿只使用已发表原式和手写有限代数/同锚分部积分；未作新研究计算，未把实际完整独立性替换为形式标签独立。
