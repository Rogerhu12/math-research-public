# 原 charge 四十的有限纤维商、三倍分歧长度与同前缀分解

日期：2026-11-16。**状态：下列同一原来源的全局正合列、全部 Gauss 帽的有限商、非固定纤维上的准确长度及光滑分支上的 Smith 块已证明。原 $K_1$ 在该有限商中的像、指定三尾及同一 $R,S$ 的全部提升仍未判定。**

本篇接[原 charge 四十 cubic 原函数格](2026-11-16-r872-native-cubic-euler-primitive-and-tail-nullspace.md)、[真实值像与三倍水平消失](2026-11-16-r872-primitive-value-image-and-cubic-horizontal-vanishing.md)及[原零 charge 四列](2026-11-16-r872-native-primitive-zero-charge-and-negative-horizontal-value.md)。

新结论把全部原来源模掉“一个 $F$ 因子及 cubic 原函数”后的余项放到**真实有限底纤维商和一个明确的 $H^1$ 核**中。这个 $H^1$ 核不被删除；固定十九角、移动水平及奇点也不被改成环境满射。

## 1. 原来源与真正因子格

取原剩余域 $k$、同一来源
$$
\mathcal W_D=\bigoplus_{n=0}^{D}
Y^n q_n(t)k[t]_{\le e_{n+1}},\qquad
q_n=(t h_7)^{A_n}(t-1)^{B_n}d^{-C_n},
$$
其中
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad
C_n=\lfloor n/2\rfloor,
\quad h_7=16t^2+4t+7,\quad d=1+8t .
$$
保同一个原 $F$、$C=(F)$、全部十九角及原 $B_D$ 线束。假设
$$
b=\deg_YF>0,\qquad
\boxed{D\ge4b,\qquad p>D+40.}
\tag{1}
$$
原不可约 $F^4$ 来源确在 $\mathcal W_D$ 时，第一项由 $Y$ 次数相加得到；本文仍将它显式列出。假设 $F$ 不可约，且 $F(0,1)=0$、$F_Y(0,1)\ne0$。因此
$$
\gcd(F,YF_Y)=1\quad\text{于 }k(t)[Y].
\tag{2}
$$
这里 $b<p$ 保证 $F_Y\ne0$；$F\ne Y$。

令
$$
L=E+40,\qquad E=Y\partial_Y,\qquad
\mathscr V_j=\mathcal W_D\cap F^jk(t)[Y],\quad
\mathscr J_3=L^{-1}\mathscr V_3 .
\tag{3}
$$
$L$ 对第 $n$ 个原 charge 除以或乘以 $40+n$，所以由 (1) 是同一来源的整单位自同构。它不改变任何原角帽。后文的 $H^1$ 是底 $\mathbf P^1_t$ 上真实系数束的上同调，不是给原物理评价像另作饱和。

为记录全部帽，置 $c=C_D$，只在系数计算中使用固定的识别
$$
\widehat{\mathcal W}_D=d^c\mathcal W_D\subset k[t,Y].
\tag{4}
$$
选 $F$ 的一个 $k[t]$-本原多项式代表 $\widehat F\in k[t,Y]$。这只是计算同一个 $F^jk(t)[Y]$ 的分母；不重选实际 $P^{\rm fact}$、$g$ 或其整数提升。最后的来源恒等式均按同一个 $d^c$ 除回，原 $M$ 及其高尾不变。以下系数束公式用 $\widehat F$，几何和物理式仍可写 $F$。

## 2. 全十九角的显式系数束

[R491，§3](../results/R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md) 已证明清分母来源准确由下表 Gauss 半空间给出。把每个固定不可约因子记为 $\nu$，其次数为 $\deg\nu$；分裂后也可逐几何点读取。

| 固定有限因子 $\nu$ | $e_\nu$ | $w_\nu$ | 原下界 $c_\nu$ |
|---|---:|---:|---:|
| $t,h_7$ 的因子 | $4$ | $-1$ | $-2$ |
| $t-1$ | $3$ | $-1$ | $-1$ |
| $d$ | $2$ | $1$ | $2c$ |

定义
$$
v_\nu\!\left(\sum a_nY^n\right)
=\min_n\{e_\nu\operatorname{ord}_\nu a_n+w_\nu n\},
\qquad
v_\infty\!\left(\sum a_nY^n\right)
=\min_n\{-2\deg_t a_n+9n\}.
$$
无穷远下界为 $c_\infty=-2c-8$。这些是真赋值，对非零乘积准确相加。

对 $j=0,1,3,4$ 及 $0\le n\le D-jb$，置
$$
\begin{aligned}
\alpha_{j,n,\nu}
&=\max\left(0,
\left\lceil
\frac{c_\nu-jv_\nu(\widehat F)-w_\nu n}{e_\nu}
\right\rceil\right),\\
\beta_{j,n}
&=\left\lfloor
\frac{9n+2c+8+jv_\infty(\widehat F)}2
\right\rfloor,\\
\ell_{j,n}
&=\beta_{j,n}-\sum_\nu\alpha_{j,n,\nu}\deg\nu .
\end{aligned}
\tag{5}
$$
取底曲线 $\mathscr B=\mathbf P^1_t$ 上的分裂束
$$
\mathscr A_j=
\bigoplus_{n=0}^{D-jb}
Y^n\mathcal O_{\mathscr B}
\left(\beta_{j,n}\infty-\sum_\nu
\alpha_{j,n,\nu}[\nu]\right).
\tag{6}
$$
负的 $\ell_{j,n}$ 仍保留为线束，不能因它没有全局截面就删掉。

**命题 1。** 令 $\mathscr W=\mathscr A_0$，并在其原有理系数空间内定义
$$
\mathbf V_j=\mathscr W\cap \widehat F^{\,j}k(t)[Y],
\qquad \mathbf J_3=L^{-1}\mathbf V_3 .
\tag{7}
$$
则
$$
\boxed{\mathbf V_j=\widehat F^{\,j}\mathscr A_j,\qquad
H^0(\mathscr B,\mathscr W)=d^c\mathcal W_D.}
\tag{8}
$$
所以 $H^0(\mathbf V_j)$ 和 $H^0(\mathbf J_3)$ 除回 $d^c$ 后恰是 (3) 的原格。

**证明。** 若 $\widehat F^{\,j}A$ 在原清分母格中，Gauss 值相加把每个下界减去 $jv_\nu(\widehat F)$，无穷远亦然。因 $\widehat F$ 在 $k[t]$ 上本原，任一有限底点的普通系数最小阶为零；故 $A$ 不能有被 $\widehat F^{\,j}$ 全部抵消的底变量极点。每个系数还必须正则，这正是 (5) 中的 $\max(0,\cdot)$。逐个 $Y^n$ 得到 (5)–(6)，反向直接相加。它保原全部有限角、无穷远和每一 charge 帽。

在任一底 DVR 上，$\mathbf V_j$ 是在实际 $\mathscr W$ 内取的因子交：若非零底参数乘一个来源落入该交，该来源本身已在同一个 $k(t)[Y]$ 因子理想中。因此 $\mathbf V_j$ 在 $\mathscr W$ 内饱和，商为局部自由。这里没有饱和物理 $M$ 的像，也没有扩大任何来源；保留的下一节之和一般并不饱和。 $\square$

特别，$\ell_{0,n}=e_{n+1}$。各有限域残数度数已在 (5) 中计算；不需要把非分裂 $h_7$ 点当两个可独立赋值的来源。

## 3. 原有限纤维商和它的准确总长

前两注的逐次除 $F$ 证明在底每个局部格中都成立：
$$
\boxed{\mathbf V_1\cap\mathbf J_3=\mathbf V_4.}
\tag{9}
$$
确实，若 $W=FA$ 且 $LW\in(F^3)$，依次模 $F$ 给
$F\mid A$，再由 $2e$、$3e$ 给余下两次整除，其中 $e=EF$ 且 (2) 保这些除法。反向显然。因为交仍在原 $\mathscr W$ 内，所以没有丢角条件。

这些束的泛点秩分别为
$$
D-b+1,\quad D-3b+1,\quad D-4b+1.
$$
由 (1)、(9)，$\mathbf V_1+\mathbf J_3$ 泛点等于 $\mathscr W$。定义真实、通常非零的有限长度层
$$
\boxed{\mathscr T_D=\mathscr W/(\mathbf V_1+\mathbf J_3).}
\tag{10}
$$
得到完整正合列
$$
\boxed{
0\longrightarrow\mathbf V_4
\longrightarrow\mathbf V_1\oplus\mathbf J_3
\longrightarrow\mathscr W
\longrightarrow\mathscr T_D\longrightarrow0 .
}
\tag{11}
$$
第一箭头为 $W\mapsto(W,-W)$，第二箭头为相加。

另一个等价、便于实际读取的正合列是
$$
\boxed{
0\longrightarrow\mathbf J_3/\mathbf V_4
\xrightarrow{\ \operatorname{res}\ }
\mathscr W/\mathbf V_1
\longrightarrow\mathscr T_D\longrightarrow0 .
}
\tag{12}
$$
左右两个非扭层均为秩 $b$ 的真实系数束。中间的商是原来源的因子商；在固定角未证明相应限制满射前，不能把它自行改名为全部环境 $H^0(C,\mathcal O_C(B_D))$。

由分裂束 (6) 的次数，整个有限商的长度准确为
$$
\boxed{
\operatorname{length}_k\mathscr T_D
=
\sum_{n=0}^{D}\ell_{0,n}
-\sum_{n=0}^{D-b}\ell_{1,n}
-\sum_{n=0}^{D-3b}\ell_{3,n}
+\sum_{n=0}^{D-4b}\ell_{4,n}.
}
\tag{13}
$$
这包括固定十九角所在底纤维、两水平、所有残域以及奇异纤维。它不是用几何分支数估计的长度。式 (13) 也不表示全局来源能任意指定这整个有限层的值。

## 4. 全局拼接的 $H^1$ 核必须保留

记 $\mathscr M=\mathbf V_1+\mathbf J_3$，并定义
$$
\mathscr E_D=
\ker\!\left[
H^1(\mathbf V_4)\longrightarrow
H^1(\mathbf V_1)\oplus H^1(\mathbf J_3)
\right].
\tag{14}
$$
所有 $H^i$ 都在同一底 $\mathscr B$ 上。

将 (11) 分成两条短正合列，再取上同调，给原全局来源商的准确结构
$$
\boxed{
0\longrightarrow\mathscr E_D
\longrightarrow
\frac{H^0(\mathscr W)}
 {H^0(\mathbf V_1)+H^0(\mathbf J_3)}
\longrightarrow
\operatorname{im}\!\left[H^0(\mathscr W)\to
H^0(\mathscr T_D)\right]
\longrightarrow0 .
}
\tag{15}
$$
右边是**实际像**。不把它换成全部 $H^0(\mathscr T_D)$。

这个 $H^1$ 核有原系数的有限矩阵，不是另加一个不可见抽象条件。借 (8) 和 $L:\mathbf J_3\simeq\mathbf V_3$，其箭头来自
$$
\boxed{
A\longmapsto
\left(\widehat F^{\,3}A,\;
-\,4(E\widehat F)A-\widehat F\,LA\right):
\mathscr A_4\longrightarrow\mathscr A_1\oplus\mathscr A_3 .
}
\tag{16}
$$
各项属于显示的真角格，因为
$L(\widehat F^{\,4}A)=
\widehat F^{\,3}(4(E\widehat F)A+\widehat F LA)$。
它保持同一个 $A$，不能分别选两项。

若 $\ell=\ell_{j,n}\le-2$，在该项的固定角乘子被写出之后，
$H^1\mathcal O_{\mathbf P^1}(\ell)$ 可由 Laurent 幂
$t^{\ell+1},\ldots,t^{-1}$ 读取；其余项的 $H^1$ 为零。
因此 (16) 只需原 $\widehat F$ 的系数卷积、原 $40+n$ 及这些有限 Laurent 余类。
这也说明“全局无截面”的负次数项不能被删掉。

特别有两个精确充分门：
$$
\ell_{4,n}\ge-1\ \text{对全部 }n
\quad\Longrightarrow\quad \mathscr E_D=0;
\tag{17}
$$
以及
$$
\boxed{
D=4b\ \text{且有非零原 }F^4\text{ 来源}
\quad\Longrightarrow\quad H^1(\mathbf V_4)=0.
}
\tag{18}
$$
对于 (18)，$\mathscr A_4$ 只有一个线束项，而该非零来源给它一个非零全局截面，所以 $\ell_{4,0}\ge0$。没有把此单项情形推广到 $D>4b$。

若一个原 $W$ 的 $\mathscr T_D$ 值为零，先得到 $W\in H^0(\mathscr M)$；其是否能在同一原全局格中分成 $V_1+J_3$，恰由 (14) 中的连接类决定。有限纤维条件与这个连接类都为零，才得到真正的同预算分解。

## 5. 非固定整纤维：长度恰为三倍原 $Z$

现在只在固定底点
$$
\Sigma=\{0,1,h_7=0,-1/8,\infty\}
$$
以外的一个底 DVR $\mathcal O_a$ 上工作。此处原 $q_n$ 都是单位，
$$
\mathscr W_a=\mathcal O_a[Y]_{\le D}.
$$
把 $F$ 看成相对 $\mathbf P^1_Y$ 上次数 $b$ 的本原截面；它没有整条底纤维分量。令
$$
Z_a=(F,EF)
$$
是这一**整个相对纤维邻域**内的交概形，包含有限 $Y$、$Y=0$、$Y=\infty$、重根及奇点。原 $E$ 在正水平框中的零阶项按线束度数保留。

由于 $D\ge4b$，相对 $\mathbf P^1$ 上
$\mathcal O(D)$ 到 $4C$ 的截面限制满射；这是
$H^1(\mathbf P^1,\mathcal O(D-4b))=0$ 的准确次数门。
相同门支付 $3C$ 和 $C$ 的限制。于是本纤维的有限商可用原同一个算子
$$
\mathcal M_a:
H^0(4C,\mathcal O(D))
\longrightarrow
H^0(3C,\mathcal O(D))\oplus
H^0(C,\mathcal O(D)),
\qquad
W\longmapsto(LW,\ W|_C)
\tag{19}
$$
读取。

第一分量满射：先把任一 $3C$ 截面提升为次数至多 $D$ 的原多项式，再用同一个 $L^{-1}$。故 $\operatorname{coker}\mathcal M_a=\mathscr T_{D,a}$。

在第二分量的核 $F\mathcal O_{3C}(D-C)$ 上，用 $F$-adic 三层过滤。第一分量的三个关联分次箭头准确为
$$
\boxed{e,\quad 2e,\quad 3e,\qquad e=(EF)|_C.}
\tag{20}
$$
公共 $40$ 及一阶导数的其它项只进入三角矩阵的非对角位置。每个乘 $e$ 的余长度是 $\operatorname{length}Z_a$；$e$ 在整曲线函数域中非零，不是零因子。因此行列式估值相加给
$$
\boxed{
\operatorname{length}_{\mathcal O_a}\mathscr T_{D,a}
=3\,\operatorname{length}_{\mathcal O_a}Z_a .
}
\tag{21}
$$
这里两边按残域次数计数。

若 $F$ 在本纤维可取 monic 仿射式，则
$$
\operatorname{Norm}_{\mathcal O_a[Y]/F}(YF_Y)
=(-1)^{\star}F(t,0)\operatorname{disc}_YF,
$$
所以
$$
\operatorname{length}\mathscr T_{D,a}
=3v_a\!\left(F(t,0)\operatorname{disc}_YF\right).
\tag{22}
$$
式 (21) 比 (22) 范围更完整：遇 $Y=\infty$ 或非 monic 框，用 (19)–(21)，不漏水平支。

这个证明在原奇异曲线环与整个交概形上进行，无须先正规化，也没有用普通迹配对代替 Gorenstein 数据。它只给长度，**不把 $\mathscr T_{D,a}$ 的 Smith 形认成乘 $e^3$ 的 Smith 形**。固定 $\Sigma$ 上原系数格不等于上述无角自由多项式格，不能搬用 (21) 删除其真实贡献；那里仍用 (5)–(16) 的原矩阵。

## 6. 光滑 tame 分支的实际 Smith 块

本节再假设 $Q$ 是上述非固定纤维中的光滑点，$F_t(Q)\ne0$。
完成并按必要的残域扩张后，写
$$
t-t(Q)=\phi(x),\qquad
\operatorname{ord}_x\phi=m,\qquad
1\le m\le b,\qquad 3m<p.
$$
这些是原分支的次数；(1) 已支付 $3m<p$。在以下局部块中仍保固定底参数的偏导，不把它误成沿曲线总导数。

### 6.1 非水平分支

若 $Y(Q)\ne0,\infty$，置 $G=Y^{40}W$。这个乘子在该点是实际单位，且
$$
LW\in(F^3)
\quad\Longleftrightarrow\quad
\partial_YG\in(F^3).
$$
令 $v=G|_C$、$D_t=(\phi'(x))^{-1}\partial_x$。
沿图 $F=0$ 展开，准确得到
$$
\boxed{
v\text{ 是局部原函数值}
\quad\Longleftrightarrow\quad
D_t v,\ D_t^2v,\ D_t^3v\text{ 都正则}.
}
\tag{23}
$$
反向不是维数推断：可取
$$
G(t,x)=\sum_{j=0}^{3}
\frac{(t-t(Q)-\phi(x))^j}{j!}\,D_t^jv(x).
\tag{24}
$$
逐项对固定 $t$ 的 $x$ 求导，前三项相消，余项被
$(t-t(Q)-\phi(x))^3$ 整除。再除同一个单位 $Y^{40}$。
把 (24) 模 $F^4$ 后用原次数 $D\ge4b$ 的完整限制返回，不添加局部来源列。

tame 换参数可令 $t-t(Q)=u^m$。对 $u^n$ 连续求三次 $D_t$，在首个出现负指数之前，其系数均不被 $p$ 整除；唯一可以提前停止的是 $n$ 为 $m$ 的倍数。因此 (23) 的准确值格是
$$
k(Q)[[t-t(Q)]]+(t-t(Q))^3k(Q)[[u]].
\tag{25}
$$
恢复 $W$ 时乘 $Y^{-40}$。所以本分支的有限商为
$$
\boxed{
\mathscr T_{D,Q}\simeq
\left(\mathcal O_a/(t-t(Q))^3\right)^{m-1}
}
\tag{26}
$$
并保原残域。简单分歧 $m=2$ 的块只有一个三次因子；
加上未受阻的常数方向，其指数是 $(0,3)$，而不是乘 $e^3$ 所可能给出的 $(1,2)$。

### 6.2 两水平分支

在真实单项式框中，负水平用 $x=Y$，正水平用 $x=Y^{-1}$：
$$
L=\lambda+\varepsilon x\partial_x,\qquad
(\lambda,\varepsilon)=(40,1)\ \text{或 }(D+40,-1).
\tag{27}
$$
不要用一个依 $x$ 的任意单位改变这个算子。

写一个局部来源的 $F$-adic 展开为
$$
W=a_0(x)+(t-t(Q)-\phi(x))a_1(x)
+(t-t(Q)-\phi(x))^2a_2(x)
+(t-t(Q)-\phi(x))^3a_3(x).
$$
条件 $LW\in(F^3)$ 逐层给
$$
a_{j+1}
=\frac{(\lambda+\varepsilon x\partial_x)a_j}
 {(j+1)\varepsilon x\phi'(x)},\qquad j=0,1,2 .
\tag{28}
$$
若 $a_0$ 首阶 $n<3m$，在首次出现负指数之前，
分子的首系数是 $\lambda+\varepsilon(n-jm)$。
负水平这些整数介于 $40$ 与 $40+3m-1$；
正水平介于 $D+40-(3m-1)$ 与 $D+40$。
由 $D\ge4b\ge4m$ 和 $p>D+40$，它们全为单位。
因此 (28) 不可能始终正则，得到
$$
a_0\in x^{3m}k(Q)[[x]]
=(t-t(Q))^3k(Q)[[x]].
\tag{29}
$$
此处 $e$ 的实际阶为 $m$。式 (21) 的准确长度正好是 $3m$，故 (29) 已是全部局部值像，并得到
$$
\boxed{
\mathscr T_{D,Q}\simeq
\left(\mathcal O_a/(t-t(Q))^3\right)^m .
}
\tag{30}
$$
它比只写三倍水平交更精确地保了该点的投影分歧。若 $F_t$ 不为单位、点奇异或位于固定十九角，本节的分支 Smith 式不外推；原完整 (10)、(13)、(19) 仍保留相应实际层。

局部分裂后的各闭点块可以下降：在 $4C$ 的互素 idempotent 上，
微分其 $e_i^2=e_i$ 关系给 $Ee_i=0\bmod F^3$，故 (19) 保这些块。
这不是允许全球来源逐块自由指定。所有残域长度和对偶迹仍一起返回原域。

## 7. 真三长前缀在已存在分解上准确相容

现在回到 R872 的原低松弛窗口：
$$
r=3,\qquad \tau=3+2h-s\in\{1,2,3\},\qquad
\tau<\ell\le h-1,\qquad h<s-4,\qquad T=s-13 .
\tag{31}
$$
仍用同一实际／参考轴、全部 $c_*U_0/P_{134}$、
$$
\Gamma=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^4,w^{\ell+13}\epsilon^3),
$$
及原 $K_1=\ker\bar M$。

前三长块给 $L^iW(t,g)\in w^T$（$i=0,1,2$），只是除去原固定公共单位读取。令 $Y=\psi(t)$ 为同一个 $F$ 的光滑分支，
$\zeta=\log(g/\psi)$，$\operatorname{ord}_w\zeta=h$。
有限 Euler Taylor 给
$$
W|_C=e^{40\zeta}
\sum_{i=0}^{2}\frac{(-\zeta)^i}{i!}(L^iW)(t,g)
+O(w^{3h}).
$$
由 $T<3h$，
$$
\boxed{W\in K_1\ \Longrightarrow\ 
\operatorname{ord}_P(W|_C)\ge T.}
\tag{32}
$$
所用阶乘是单位，所有乘子都是原同一个单位；不增加目标长度。

前面的原函数格定理已支付：对 $J\in\mathscr J_3$，所有其它长／短块自动满足，而
$$
J\in K_1\quad\Longleftrightarrow\quad
\operatorname{ord}_P(J|_C)\ge T .
\tag{33}
$$
其差的 Euler Taylor 余项从 $4h+2$ 开始；零角的真实 $t^2$ 门保留。

于是，若一个原 $W\in K_1$ 已经有**真正全局来源分解**
$W=W_F+J$，$W_F\in\mathscr V_1$、$J\in\mathscr J_3$，
则 $J|_C=W|_C$。由 (32)–(33)，同一个 $J\in K_1$，
随即同一个 $W_F\in K_1$。所以准确有
$$
\boxed{
K_1\cap(\mathscr V_1+\mathscr J_3)
=(K_1\cap\mathscr V_1)+(K_1\cap\mathscr J_3),
}
\tag{34}
$$
且两部分的交恰是 $\mathscr V_4\subset K_1$。

这里右边都是 (3) 的**全局原格**。式 (34) 不说任一局部
(24) 可拼成该分解；(14)–(18) 正是不能省去的全球边界。

## 8. 对三尾及同一修正的实际结论

保原三尾
$$
\Pi(W)=
([w^{s-3}]W_2(W),[w^{s-2}]W_2(W),[w^{s-1}]W_2(W)).
$$
已证明 $\Pi(\mathscr J_3)=0$。所以当一个实际 $W\in K_1$
在 (15) 中的有限纤维值及连接类都为零时，(34) 给
$$
\boxed{
\Pi(W)=\Pi(W_F),\qquad
W_F\in\mathscr V_1\cap K_1,
}
\tag{35}
$$
而且这个返回在同一个 $\mathcal W_D$ 内完成。
若 (18) 适用，只需检真正的有限纤维值；若不适用，
(16) 的 $H^1$ 核仍在。

更准确地，原 $K_1/(\mathscr J_3\cap K_1)$ 中，
含一个 $F$ 因子的子空间是
$$
(\mathscr V_1\cap K_1)/\mathscr V_4;
$$
其余部分单射到 (15) 的实际全局来源商。
因此未知的非 $F$ 部分现在被定位为**原有限纤维障碍和原连接类**，
而不是一个可自由选择的环境修正。

这没有证明这些障碍在全 $K_1$ 上为零，也没有证明
$\Pi(\mathscr V_1\cap K_1)$ 已知。式 (13)、(21)、(26)、(30)
均不应被当作带前缀的满像或新的单位左行。
负水平四列仍与同一个 $W$ 的其它值相连；
例如 $z_-\ge1$ 时 $\mathscr J_3|_{H_-}=0$，
真正分解还强制 $W|_{H_-}=(F H)|_{H_-}$，不能单独改它。

若用 (35) 改写 R872 第二／三页的指定 scalar，只替换该
$\Pi$ 响应；原同一 $R,S$ 的其余
$\beta_1$、normal、三条十三行 carry 和更高整商仍须全部代入。
不新增中央零，也不由有限层的长度宣布原主目标关闭。

本篇是原来源和原框的符号证明；没有新增数学数值运行。
