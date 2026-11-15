# R156：输入相位旋转不保持 canonical 第四成本空间

日期：2026-11-15。**已证明的反证与原式分解。** 本稿只作纸面推导，不运行新的 profile、几何或研究符号目标。使用 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R78](R78-complete-phase-P1-symmetric-square-conditions.md)、[R81](R81-real-third-hook-control-and-mixed-phase-response.md)、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R84](R84-fourth-cost-semigroup-and-frame-length-bound.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md) 和 [R122](R122-affine-G-orbit-and-real-joint-query-control.md)。

结论有两层。第一，保持几何控制对象及 canonical 固定目标定义时，输入替换 $q\mapsto e^{i\alpha}q$ 只有在 $\alpha\in\pi\mathbb Z$、即四次成本上的恒等操作时，才保持普适真实第四成本线性空间 $\mathcal U_4$。所有其他角度也不能保持其真实成本闭凸锥。第二，输入替换下完整 $-2$ 模式含荷 $4,2,0$，有限相位平均一般保留荷零项。两层均有 R81 的已证真实响应作为明确见证，无须假设任意形式张量可达。

这些结论排除的是上述普适操作。它们不排除某条特殊成本或某个特殊 profile 圆具有额外对称，也没有建立本课题所需的非零正性泛函或全部第四障碍。

## 1. 固定对象与两个不同的相位操作

全部真实路径使用同一个物理区间、共同右 collar、同一右原函数锚和同一真实 $s$ 起点。记

$$
q=f+ig,\qquad
F=f^2,\qquad
\phi_\theta=\cos\theta f+\sin\theta g,\qquad
D_\theta=F-\phi_\theta^2.
\tag{1}
$$

这里 $f^2=f\odot f$，对称张量约定与 R78 相同。R105 的 canonical 目标度量是

$$
g_X+\varepsilon^2\,dY_f\cdot dY_f.
$$

第二、第三场用零 scalar 传入历史恢复；其后的全部真实历史及导数继续保留。令 $\mathscr S$ 为同端口、frame 恒等、$M=T=0$ 的实际有限词成本集合，并取

$$
U=\mathcal U_4=\operatorname{span}_{\mathbb R}\mathscr S,\qquad
\mathscr C=\overline{\operatorname{cone}(\mathscr S)}.
\tag{2}
$$

所有空间首先是对一般共同右 collar profiles 成立的普适函数空间。可将下述输入替换看成作用在 R105 有限模板空间与其输入旋转像共同张成的有限环境空间上；不预设它作用于 $U$。

定义输入操作

$$
(\mathsf I_\alpha V)(f,g;\theta)
=V(f_\alpha,g_\alpha;\theta),
\qquad
\begin{pmatrix}f_\alpha\\g_\alpha\end{pmatrix}
=
\begin{pmatrix}\cos\alpha&-\sin\alpha\\
\sin\alpha&\cos\alpha\end{pmatrix}
\begin{pmatrix}f\\g\end{pmatrix}.
\tag{3}
$$

于是

$$
F_\alpha=f_\alpha^2=\phi_{-\alpha}^2,
\qquad
\phi_\theta(f_\alpha,g_\alpha)=\phi_{\theta-\alpha}(f,g).
\tag{4}
$$

所以 (3) 同时改变了固定二阶目标。它不是在同一个 $F=f^2$ 下仅将弯曲相位 $\theta$ 平移。

另一个纯函数操作是

$$
(\mathsf T_\alpha V)(f,g;\theta)
=V(f,g;\theta-\alpha)-V(f,g;-\alpha).
\tag{5}
$$

(5) 保留 $\theta=0$ 的零值，并对两个非零 Fourier 模式作通常的相位乘法。后文也直接检查它；不能因 (5) 的有限平均为零，就把它认作真实路径操作。

## 2. 完整路径的两张张量表，不删除历史

以下分解适用于一条任意有限真实路径 $B$，并不先要求 $M=T=0$。用 R83 的完整恢复记号定义

$$
Z_B(D)=\mathcal I_B H_D,
\qquad
U_B(x;D)=\mathcal I_B H(Y_x,Z_B(D)).
$$

物理第三场准确是 $-2U_B(\phi;D)$。设 $R_B$ 为沿该路径的第四 characteristic RHS 算子，定义

$$
\mathcal K_B(D_1,D_2)
=\int_B R_B\{-H(Z_B(D_1),Z_B(D_2))\}\,ds,
\tag{6}
$$

$$
\begin{aligned}
\mathcal L_B(x\odot y,D)
=2\int_B R_B\{&H(Y_x,U_B(y;D))\\
&+H(Y_y,U_B(x;D))\}\,ds.
\end{aligned}
\tag{7}
$$

$\mathcal K_B$ 对称；$\mathcal L_B$ 的两个对称平方槽一般不对称。各场在整条路径上恢复，故 (6)、(7) 含全部累计二、三阶历史。所有 $s$ 导数均按 R56 的真实方程处理，不能先把历史及其导数同时设零。由完整第四 forcing

$$
-H(Z_2,Z_2)-2H(Y_\phi,Z_3)
$$

直接得到

$$
\boxed{V_B(F,\phi)=\mathcal K_B(D,D)+\mathcal L_B(\phi^2,D).}
\tag{8}
$$

这与 R78 的对称平方结构相同；此处 (6)、(7) 是**整条路径**的表，不是删去桥成本后的局部漂移表。

特别令 $g=0$，置

$$
K_f=\mathcal K_B(f^2,f^2),\qquad
L_f=\mathcal L_B(f^2,f^2).
$$

则 $\phi_\theta=\cos\theta f$、$D_\theta=\sin^2\theta f^2$，所以

$$
\boxed{V_B(f,0;\theta)
=K_f\sin^4\theta+L_f\cos^2\theta\sin^2\theta.}
\tag{9}
$$

因此每条 canonical 真实路径在这个输入上的成本都是 $\theta$ 的偶函数。这个性质对全部路径成立，当然对 $U$ 中所有实线性组合也成立。等价地，普适线性查询

$$
\Omega_f(V)(\xi)
=\left.\partial_\theta V(f,0;\theta,\xi)\right|_{\theta=0}
\tag{10}
$$

在 $U$ 上恒为零。

只要找到一个 $K\in U$ 使 $\Omega_f(\mathsf I_\alpha K)\ne0$，就严格证明 $\mathsf I_\alpha K\notin U$。无需先将这个 $K$ 误称为单条独立实际负成本路径。

## 3. 已证真实 hook 响应提供非零见证

复用 R81 的同右锚正积分

$$
J(a)(\xi)=\int_\xi^r a(\eta)\,d\eta
$$

以及真实八矩二次算子

$$
P(a,b)=J(a''b''),\quad
R(a,b)=a'b'+\xi J(a''b''),\quad
S(a,b)=J(\eta a''b'').
$$

取

$$
\mathfrak H=[P,S]-3[P,R],\qquad
[P,Q](a;b,c)=P(a,Q(b,c))-Q(a,P(b,c)).
\tag{11}
$$

R71/R81 已用真实有限第三控制证明 $\mathfrak H\in W$，并证明全部 profiles 上的准确身份

$$
\mathfrak H(a;a,a)=0,
\qquad
\mathfrak H(a;b,c)+\mathfrak H(b;c,a)+\mathfrak H(c;a,b)=0.
\tag{12}
$$

采用 R81 的真实标准常态二次算子 $A\in E_8$：

$$
\begin{aligned}
A(f,f)={}&\frac\xi2 f^2-\frac{1+\xi^2}{2}ff'
+\frac{\xi(1+\xi^2)}4(f')^2\\
&+\frac{\xi^2-1}{8}J\bigl((1+\eta^2)(f'')^2+2(f')^2\bigr).
\end{aligned}
\tag{13}
$$

令完整响应

$$
K=\mathcal B_A(\mathfrak H)\in\mathcal R_8\subset U.
\tag{14}
$$

$\mathcal R_8\subset U$ 是 R105 已付的真实成本差与 span 结论。这里不把 (14) 自动当成一条成本恰为 $K$ 的单独实际环。

对同一个实 $f$ 定义

$$
T_f=\mathfrak H(A(f,f);f,f),\qquad C_f=2T_f.
\tag{15}
$$

现在在**全部槽同时**代入

$$
F=a^2f^2,\qquad \phi=bf,\qquad D=(a^2-b^2)f^2.
$$

由 R83/R109 的完整响应式

$$
\mathcal B_A(\mathfrak H)
=2\mathfrak H(AD;D)
-4\mathfrak H(\phi;\phi,AD)
+4A(\phi,\mathfrak H(\phi;D)),
\tag{16}
$$

(12) 给

$$
\mathfrak H(f;f,A(f,f))=-T_f/2,
\qquad
\mathfrak H(f;f,f)=0.
$$

因而三个完整项分别为

$$
2(a^2-b^2)^2T_f,\qquad
2b^2(a^2-b^2)T_f,\qquad 0,
$$

得到准确整函数身份

$$
\boxed{K(a^2f^2,bf)=C_f\,a^2(a^2-b^2).}
\tag{17}
$$

取 $a=1,b=\cos\theta$，恢复 R81 的

$$
\boxed{K(f,0;\theta)=C_f\sin^2\theta.}
\tag{18}
$$

存在共同右 collar 的真实 $C^\infty$ profile $f$ 和查询点，使 $C_f\ne0$。具体非零性已经由 R81(9)–(12) 支付：对 $c>1,m\ge8$ 的右幂尾 $f=B(c-\xi)^m+O((c-\xi)^{m+1})$，其结果等价于

$$
\begin{aligned}
C_f(\xi)={}&-
\frac{5(c^2-1)(1+c^2)B^4m^4(m-1)^3(m-3)(2m-5)}
{8(4m-9)}
(c-\xi)^{4m-8}\\
&+O((c-\xi)^{4m-7}).
\end{aligned}
\tag{19}
$$

R81 随后用同一偶 bump 的 $C^3$ 光滑逼近保持三矩恒等式和一个固定内部查询的非零值，取得所需 $C^\infty$ 见证。本稿不再执行尾计算或逼近实验。

## 4. 输入旋转不保持 U，也不保持真实闭锥

将 (3) 作用于退化输入 $(f,0)$。这时

$$
f_\alpha=\cos\alpha f,\qquad
 g_\alpha=\sin\alpha f,\qquad
 F_\alpha=\cos^2\alpha f^2,\qquad
 \phi'_\theta=\cos(\theta-\alpha)f.
$$

在 (17) 中取 $a=\cos\alpha,b=\cos(\theta-\alpha)$，得到

$$
\boxed{(\mathsf I_\alpha K)(f,0;\theta)
=C_f\cos^2\alpha
\bigl(\cos^2\alpha-\cos^2(\theta-\alpha)\bigr).}
\tag{20}
$$

特别取 $\alpha=\pi/4$：

$$
\boxed{(\mathsf I_{\pi/4}K)(f,0;\theta)
=-\frac{C_f}{4}\sin(2\theta).}
\tag{21}
$$

在 (19) 给出的非零查询处，它是非零奇函数。于是由 (9)、(10)

$$
\Omega_f(\mathsf I_{\pi/4}K)=-C_f/2\ne0,
\qquad
\boxed{\mathsf I_{\pi/4}K\notin U.}
\tag{22}
$$

因此输入相位旋转并不定义 $U$ 上的作用。更具体地，它不可能对所有真实零二、三阶闭词成本都保持 $\mathscr C$：若
$\mathsf I_{\pi/4}\mathscr C\subseteq\mathscr C$，则由
$U=\operatorname{span}\mathscr C$ 及线性性必有
$\mathsf I_{\pi/4}U\subseteq U$，与 (14)、(22) 矛盾。

这个反证用到了一个**已有真实响应方向**，没有用自由三线性张量，也没有把成本差当作实际成本逆元。输入旋转在少数特殊角度或特殊函数上的偶然恒等，不改变 (22) 对普适旋转机制的反证。

### 4.1 所有非平凡输入角均被排除

(20) 在零相位的一阶导数是

$$
\Omega_f(\mathsf I_\alpha K)
=-C_f\cos^2\alpha\sin(2\alpha).
\tag{22a}
$$

因此所有 $\sin(2\alpha)\ne0$ 的角都不保持 $U$。剩下仅需检查
$\alpha=\pi/2\pmod\pi$；这里不能因为 (22a) 为零就称操作可实现。

对每条 canonical 路径另取 $f=0$，以 $g$ 为任意实 profile。此时
$F=0,\phi_\theta=\sin\theta g,D=-\sin^2\theta g^2$，(8) 给

$$
V_B(0,g;\theta)
=\{\mathcal K_B(g^2,g^2)-\mathcal L_B(g^2,g^2)\}
\sin^4\theta.
\tag{22b}
$$

故 $U$ 的所有函数在这个输入处都满足
$\partial_\theta^2V|_{\theta=0}=0$。而当
$\alpha=\pi/2\pmod\pi$ 时，(3) 把 $(0,g)$ 变为 $(\mp g,0)$。
(17)、(18) 及四次齐次性给

$$
(\mathsf I_\alpha K)(0,g;\theta)=C_g\sin^2\theta,
\qquad
\left.\partial_\theta^2(\mathsf I_\alpha K)\right|_0
=2C_g\ne0
\tag{22c}
$$

于同一个 R81 非零 profile 见证。因此这些剩余 quarter turns 也不保持 $U$。
最后，$\alpha\in\pi\mathbb Z$ 只同时改变 $(f,g)$ 的整体符号；由第四阶的总 profile 次数为四，$\mathsf I_\alpha$ 在整个成本空间上恰为恒等。准确结论为

$$
\boxed{
\mathsf I_\alpha U\subseteq U
\quad\Longleftrightarrow\quad
\alpha\in\pi\mathbb Z.
}
\tag{22d}
$$

同理 $\mathsf I_\alpha\mathscr C\subseteq\mathscr C$ 也只有这些平凡角成立。
这是普适函数空间及其闭锥的结论；没有声称某个特选输入上的稳定子必须相同。

### 4.2 退化输入与合法圆的准确范围

在普适函数空间中，$g=0$ 只是一条检验原式身份的输入；它不被声称为主课题所需的非退化合法圆。一个普适身份必须在这个输入也成立，故 (22) 已足够。

还可以直接复用 R81§6 已构造的真实合法圆，而无需新补矩。该圆中最右 packet 只属于 $f$；在一个固定查询点 $\xi_0$ 及整个 $[\xi_0,r]$ 上，$g=0$，同时 $C_f(\xi_0)\ne0$。R105 的全部 profile 操作都是局部 jets、乘积和同一右锚的正次数 Volterra 原函数，所以在 $\xi_0$ 的值只依赖这段右区间。故 (9) 和 (21) 在这个**同一合法圆**的查询处仍成立。

圆的全部三矩和非退化性是 R81 已完成的构造；本稿没有默加左侧补偿，也没有换锚。常数正交旋转保该圆每个矩型的“等对角、零交叉”条件，故旋转后的输入仍合法。这依然不保固定目标 $dY_f\cdot dY_f$，也不把旋转后函数变成同一 canonical 成本。

该说明给出一个合法圆上的明确失败例。它不宣称对任意预给合法圆都有这个右尾结构，也不排除某个特选圆上的偶然可实现性。

## 5. 为什么两个 canonical 模式不等于两个输入荷

对 (8) 置

$$
\mathcal Q_B=\mathcal K_B-\operatorname{Sym}\mathcal L_B,
\qquad d=f^2-g^2,\qquad \zeta=e^{-i\theta}.
$$

R78 的同一代数适用于整路径表，给

$$
V_{-4}=\frac1{16}\mathcal Q_B(q^2,q^2),
\qquad
V_{-2}=-\frac14\bigl\{\mathcal L_B(F,q^2)+\mathcal Q_B(d,q^2)\bigr\}.
\tag{23}
$$

因为

$$
F=\frac{q^2+2q\odot\bar q+\bar q^2}{4},
\qquad
 d=\frac{q^2+\bar q^2}{2},
$$

第二式准确分为

$$
V_{-2}=A_4+A_2+A_0,
\tag{24}
$$

其中

$$
A_4=-\frac{\mathcal L_B(q^2,q^2)+2\mathcal Q_B(q^2,q^2)}{16},
$$

$$
A_2=-\frac{\mathcal L_B(q\odot\bar q,q^2)}8,
$$

$$
\boxed{A_0=
\frac{\mathcal L_B(q^2,\bar q^2)-2\mathcal K_B(\bar q^2,q^2)}{16}.}
\tag{25}
$$

三个下标分别是输入 $q\mapsto e^{i\alpha}q$ 的荷，故

$$
\boxed{
(\mathsf I_\alpha V)_{-4}=e^{4i\alpha}V_{-4},\qquad
(\mathsf I_\alpha V)_{-2}=e^{4i\alpha}A_4+e^{2i\alpha}A_2+A_0.
}
\tag{26}
$$

$-2$ 是输出弯曲相位 $\theta$ 的模式编号，不是输入旋转的单一荷。式 (25) 的零荷项来自固定目标槽，不能因输出模式非零就删掉。

例如对等距五相位 $\alpha_j=2\pi j/5$，输入平均在 $-4$ 模式为零，在 $-2$ 模式恰保 $A_0$。共轭和常数模式也须一起保留；常数模式仍由 $V(0)=0$ 决定。

R81 的同一个见证给一个更直接的非零平均。对 $(f,0)$ 将 (20) 在五相位上平均，常数与二、四次三角恒等式准确给

$$
\boxed{\frac15\sum_{j=0}^4
(\mathsf I_{\alpha_j}K)(f,0;\theta)
=\frac{C_f}{4}\sin^2\theta
=\frac14K(f,0;\theta).}
\tag{27}
$$

相应 $-2$ 荷零系数是 $-C_f/16\ne0$。因此“只有输出 $-4,-2$ 两模式，输入相位平均必零”本身已经是错误的代数推断；即使暂不问可实现性，也不能使用它。

## 6. 固定目标重置有明确余项；桥与历史不支付它

在 (8) 中暂省路径下标。给一般 $P=\phi^2$，设
$F_\alpha=F+\Delta$、$D_\alpha=F_\alpha-P$。双线性逐项展开给

$$
\boxed{
V(F_\alpha,P)
=V(F,P)-V(F,F_\alpha)
+(2\mathcal K-\mathcal L)(D_\alpha,\Delta).
}
\tag{28}
$$

这里 $V(F,P)$ 表示将第一 profile 平方槽写成 $P$ 的同一表达式；在相位重置时 $F_\alpha$ 也确为一个实际平方槽。式 (28) 保留了新的目标成本及完整余项。没有一般身份把最后一项设零。

R83/R84 的真实传递中，低阶控制改变的是传入的二、三阶 histories，第一 profile $\phi$ 与固定 $F$ 保持不动。特别 $M=T=0$ 插入块只加第四成本 $V$。R109 将部分历史成本证明属于 $\mathcal R_8$，并未授权更换固定目标；R122 的真实仿射变换也要求各块共用同一组 profiles，并为改变后的几何端口支付完整桥成本。

因此不能将 (4) 的 $F_\alpha-F$ 称为一个已付的输入 gauge，也不能在不同块中各选新的相位原点再直接援引 R84 加法律。若拼接始终属于原 canonical 系统，整条路径仍满足 (9)，无论中间的矩阵、第三历史、桥和基准多复杂。任何额外 $U$ 或 $\mathcal R_8$ 校正也被 (10) 杀掉，无法修复 (22) 的非零奇部。这个判断不依赖把桥成本置零。

对 (5) 的输出相位操作也可用同一个见证直接判定：

$$
(\mathsf T_{\pi/4}K)(f,0;\theta)
=C_f\bigl(\sin^2(\theta-\pi/4)-1/2\bigr)
=-\frac{C_f}{2}\sin(2\theta)\notin U.
\tag{29}
$$

(5) 的五相位平均确实为零，但它不保持 canonical 成本空间；这个形式零平均没有提供真实成本相消词。

## 7. 结论与剩余范围

已证明：

- 输入旋转保持普适真实成本空间 $U$ 或其真实成本闭凸锥，当且仅当 $\alpha\in\pi\mathbb Z$，此时四次成本上的操作就是恒等；
- 这不是单凭“未找到几何实现”的暂时判断，而是由所有 canonical 路径共有的偶性与一个已证真实响应产生的明确反证；
- 完整 $-2$ 输出模式在输入旋转下含荷 $4,2,0$，相位平均保留 (25)，R81 给非零实例；
- 只平移输出相位并重置零值的 (5) 也不保持 $U$，故其形式平均为零不能升级为真实成本抵消。

$\Omega_f$ 在 $U$ 上本来就是零泛函；本稿没有借它构造 $U$ 内的非零正性障碍，也没有证明存在或不存在非平凡真实零成本环。R145 的真实几何曲率反号、R122 已付的仿射控制和已有 lineality 结论保持各自原范围。完整第四函数、ruling、后续高阶及主课题完成标准仍须继续处理。
