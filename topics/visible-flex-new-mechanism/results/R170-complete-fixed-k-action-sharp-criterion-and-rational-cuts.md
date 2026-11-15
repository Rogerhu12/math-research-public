# R170：固定 k 的完整三层 action 的准确判据与有理切割接口

日期：2026-11-15。**已证明。** 本稿为纸面推导，不运行新的积分、profile、原式编译或候选优化。它同时保留零、二、四导数层，给出固定 k 子类的充要判据；它不是只研究最高层，也不把中间层单独要求非负。

依据 [R140](R140-full-action-multiplier-equivalence-for-real-cost-positivity.md)、[R148](R148-sharp-one-dimensional-highest-action-positivity.md)、[R164](R164-covariant-eight-matrix-multiplier-for-positive-affine-characters.md)、[R165](R165-prescribed-h-quadratic-highest-action-and-loglinear-frequency-gate.md) 及 [R168](R168-reflection-of-corrected-low-action-and-four-head-relations.md)。所有系数来自同一个真实权 −2 字符及同一个 R164 规范化乘子。

## 1. 固定一个真实 k 后的四个常数

固定任意实数 $\kappa$，只考虑真实路径

$$
k(s)=\kappa,\qquad h(s)>0,\qquad \omega(s)=\omega_*.
\tag{1}
$$

因此 $\omega_s=k_s/(2h)=0$ 确实成立。区间有限，h 光滑且在两端开邻域分别为正的常数；左右常数不必相同。末 frame 由真实 ODE 给出，R140 允许该末 frame，不另要求位置闭合。

取 R164 修正静态函数 $a_{\rm static}(k)$、修正二次函数 $b_2(k)$，以及 R165 的最高标量 $a,b,\ell,m$。定义

$$
A=a+b\kappa^2,\quad Q=\ell+m\kappa^2,\quad
B=b_2(\kappa),\quad C=a_{\rm static}(\kappa).
\tag{2}
$$

字母 C 在本文仅指修正静态值；它不是 R165 的 $A_{kk}$ 系数。由于真实 $k_s,k_{ss}$ 均为零，完整修正 action 准确退化为

$$
\mathcal F_\kappa[h]=\int\left[
C h^{-2}+B h^{-4}h_s^2+A h^{-4}h_{ss}^2
+Q h^{-6}h_s^4\right]ds.
\tag{3}
$$

所有面积项与含 k 导数的项在这条真实子类上为零；没有从一般 action 中把它们删掉。B 已包含同一乘子的完整二阶修正。

置

$$
D=Q+\frac{25}{9}A,
\qquad S=\frac43\sqrt A+\sqrt D
\quad\text{（S 仅在 A,D 非负时定义）}.
\tag{4}
$$

**主定理。** 式 (3) 对全部有限正平端 h 非负，当且仅当

$$
\boxed{A\ge0,\qquad D\ge0,\qquad C\ge0,
\qquad B+2\sqrt C\left(\frac43\sqrt A+\sqrt D\right)\ge0.}
\tag{5}
$$

因此，真实正字符必须对每个实 $\kappa$ 满足 (5)。反之，全部 $\kappa$ 的 (5) 只证明所有固定 k 路径的完整 action 非负，仍不足以处理同时变化的 h、k 或赋予外坐标一个真实泛函。

## 2. 变量 p=1/h 与全部边界项

令 $p=1/h$。p 同样严格正、光滑、两端为常值 germs。准确微分给出

$$
h_s=-\frac{p_s}{p^2},\qquad
h_{ss}=\frac{2p_s^2}{p^3}-\frac{p_{ss}}{p^2},
$$

$$
h^{-4}h_{ss}^2
=p_{ss}^2-4\frac{p_{ss}p_s^2}{p}+4\frac{p_s^4}{p^2}.
\tag{6}
$$

因为端部 $p_s=0$，

$$
\int\frac{p_{ss}p_s^2}{p}\,ds
=\frac13\int\frac{p_s^4}{p^2}\,ds.
\tag{7}
$$

这里使用的端势是 $p_s^3/(3p)$；它在两个端部各自为零，不需要左右 p 相等。记

$$
X=\int p_{ss}^2,\quad Y=\int\frac{p_s^4}{p^2},\quad
Z=\int p_s^2,\quad W=\int p^2.
\tag{8}
$$

全部积分均在同一个有限区间上。式 (3) 等价于

$$
\boxed{\mathcal F_\kappa[h]=H+B Z+C W,
\qquad H=A X+\left(D-\frac A9\right)Y.}
\tag{9}
$$

特别，中间常数 B 可以为负；主定理衡量它与静态、最高层之间准确可容许的关系。

## 3. 一个准确且 sharp 的非负函数插值不等式

假设 $A,D\ge0$。本节证明

$$
\boxed{H W\ge S^2 Z^2,\qquad
\inf_{p>0\ {\rm smooth,\ flat},\ Z>0}\frac{HW}{Z^2}=S^2.}
\tag{10}
$$

下确界允许任意有限区间；每条测试 p 始终严格正且平端。用于说明 sharp 的极限函数可以有零点或无穷尾，但它们只用于产生合法的有限近似，不能直接作为原路径。

### 3.1 A>0：恒等式与下界

置

$$
q=\frac13+\sqrt{D/A},\qquad
Y_q(p)=p_{ss}-q\frac{p_s^2}{p}.
\tag{11}
$$

由 (7)，

$$
H=A\int Y_q(p)^2,
\qquad \int pY_q(p)=-(1+q)Z.
\tag{12}
$$

于是 Cauchy–Schwarz 给

$$
HW\ge A(1+q)^2Z^2=S^2Z^2.
\tag{13}
$$

下面的 sharp 论证同时说明该 Cauchy 下界在正平端函数类中不能提高。

### 3.2 q>1/3：准确等号形状与合法逼近

考虑方程

$$
Y_q(p)=-\lambda p,\qquad \lambda>0.
\tag{14}
$$

三个参数范围分别有以下正形状；表中可再作任意正的空间缩放。

| 参数 | 极限形状 | 对应 $\lambda$ |
|---|---|---|
| $1/3<q<1$ | $p(s)=\cos(s)^{\alpha}$，$|s|<\pi/2$，$\alpha=1/(1-q)>3/2$ | $\alpha$ |
| $q=1$ | $p(s)=e^{-s^2/2}$ | $1$ |
| $q>1$ | $p(s)=\cosh(s)^{-\alpha}$，$\alpha=1/(q-1)>0$ | $\alpha$ |

逐次微分即核实 (14)。对 cosine 幂先在端点外延为零。其 $X,Y,Z,W$ 都有限：端点最严格的条件来自 $p_{ss}^2$ 与 $p_s^4/p^2$，两者的主阶都是距离的 $2\alpha-4$ 次幂，正因 $\alpha>3/2$ 可积。

在该范围，$p_s^3/p$ 的端通量也趋零；Gaussian 和 cosh 形状则因尾部衰减满足相同的无边界积分身份。于是各形状满足

$$
H=A\lambda^2W,\qquad (1+q)Z=\lambda W,
\qquad \frac{HW}{Z^2}=A(1+q)^2.
\tag{15}
$$

这些极限形状可以在 $X,Y,Z,W$ 四项中同时由合法 p 逼近。对 cosine 幂，在长度 $\varepsilon$ 的端部截断并平滑时，$X,Y$ 的改变为 $O(\varepsilon^{2\alpha-3})$，其余两项也趋零。对 Gaussian/cosh，先在充分远的尾部用有限宽的平滑截断变为零，衰减保证四项误差趋零。截断可选非负光滑函数，边缘具有足够高的消失阶。

然后在这个**已经固定的有限区间**上加一个正底 $\epsilon$，并把它延成两端的正常值 germs。加底保持导数，而

$$
\frac{p_s^4}{(p+\epsilon)^2}\le\frac{p_s^4}{p^2}
$$

且在正值处收敛；支配收敛给 Y 收敛。X、Z 不变，W 在固定有限区间上收敛。如需最后的小卷积，可先固定 $\epsilon>0$ 再做，因分母有正下界，四项连续；原常端芽在更小的两端邻域保持。依次选择尾截断、正底和光滑化参数，得到严格正的 $C^\infty$ 平端 p，(15) 的比值不变地逼近。没有向无限长常值尾部积分。

### 3.3 临界 q=1/3：不能直接截断 cosine 的3/2次幂

当 $D=0$ 时，形式形状 $p=\cos^{3/2}s$ 的 X、Y 各自对数发散，且 $p_s^3/p$ 的端通量不消。直接代入它不合法。

取 $q_n=1/3+\delta_n>1/3$、$\delta_n\downarrow0$，并令

$$
\alpha_n=\frac1{1-q_n}>\frac32,\qquad p_n=\cos(s)^{\alpha_n}
\quad (|s|<\pi/2).
$$

这些形状的 $W_n,Z_n$ 收敛到有限非零值，而端点幂估计给

$$
Y_n=O(\delta_n^{-1}).
\tag{16}
$$

定义 $H_n^{(q_n)}=A[X_n+(q_n^2-2q_n/3)Y_n]$。对固定的**目标** $q=1/3$，

$$
H_n^{(1/3)}=A(X_n-Y_n/9)
=H_n^{(q_n)}-A\delta_n^2Y_n.
\tag{17}
$$

第一项按 (15) 满足准确等号，第二项为 $O(\delta_n)$。所以

$$
\frac{H_n^{(1/3)}W_n}{Z_n^2}\longrightarrow\frac{16A}{9}=S^2.
\tag{18}
$$

对每个固定 n，先按上节完成正底、平端、光滑化，使该 n 的四项误差任意小，再取 n 的极限。这一顺序支付了临界端通量和发散积分，不把 $q_n\to q$ 当作未经控制的形式连续性。

### 3.4 A=0 与完全退化情形

若 $A=0,D>0$，则 $H=DY$。Cauchy–Schwarz 直接给

$$
Z^2=\left(\int p\frac{p_s^2}{p}\right)^2\le WY.
$$

极限形状 $p=e^{-|s|}$ 满足 $Y=W=Z=1$。中心只有一阶折角；此处没有 X 项，因此平滑中心所产生的 Y、Z、W 误差均趋零。再截掉远尾，加正底并平端化，得到合法近似，故 sharp 常数为 $D=S^2$。

若 $A=D=0$，则 H 恒为零，(10) 的下确界就是零。该退化情形不需要构造等号 ODE。

## 4. 完整三层判据的证明

### 4.1 充分性

在 $A,D,C\ge0$ 下，由 (10)，

$$
H+CW\ge2\sqrt{HCW}\ge2\sqrt C\,S Z.
$$

故若 (5) 的最后一式成立，

$$
\mathcal F_\kappa[h]\ge(B+2\sqrt C\,S)Z\ge0.
\tag{19}
$$

当 Z=0 时，p 是常数，原 action 为 $CW\ge0$，同样包括在内。

### 4.2 三个基础符号条件的必要性

取常路径给 $C\ge0$。若完整 action 对所有 h 非负，R140 的真实时长缩放迫最高层非负；R148 在该固定 k 子类上的准确判据随即给 $A\ge0,D\ge0$。这一步没有要求 B 独立非负。

### 4.3 最后一式的 sharp 必要性

先设 $S>0$。对任意非恒定合法 p，记

$$
K_p=\frac{HW}{Z^2},\qquad x=Z/W>0.
$$

于是

$$
\mathcal F_\kappa[h]/W=K_p x^2+B x+C.
\tag{20}
$$

把同一 p 的自变量伸缩为 $p_L(s)=p(s/L)$，$K_p$ 不变，而 $x$ 乘 $L^{-2}$，因此 x 可取任意正数。若

$$
B+2S\sqrt C<0,
$$

则存在某个 $x_*>0$ 使 $S^2x_*^2+Bx_*+C<0$。由 (10) 的 sharp 性，先选一条**有限、正、平端、光滑**的 p，使 $K_p$ 足够接近 $S^2$，再选一个有限 $L>0$ 使 x 等于 $x_*$，(20) 就严格为负。这证明必要性，包括 $C=0$ 的边界。

若 $S=0$，已经有 $A=D=0$，此时 action 为 $BZ+CW$。若 $B<0$，取任一非恒定正平端 p，并通过缩短其时长使 $Z/W$ 足够大，仍得到严格负值。因此必须 $B\ge0$，正是 (5) 在 S=0 时的条件。主定理得证。

整个反例构造都是先固定一个合法有限形状，再作有限时长选择。令 h=1/p 后，h 对每一条所选路径都有有限正上下界，真实 $\omega$ 常值；需要的共同 profile 带可在这些有限数据选定之后确定。没有把极限中的 p=0、h=无穷大或无限长路直接作为物理对象。

## 5. 无新积分的有理线性必要行

式 (5) 的耦合门还可写为

$$
B+\frac83\sqrt{AC}+2\sqrt{CD}\ge0.
\tag{21}
$$

在 $A,D,C\ge0$ 下，对任意正实 $t,s$，AM–GM 给

$$
\frac83\sqrt{AC}\le\frac43(tA+C/t),
\qquad 2\sqrt{CD}\le sC+D/s.
$$

因此每个真正正字符都满足

$$
\boxed{B+\frac43(tA+C/t)+sC+D/s\ge0
\qquad(t,s>0).}
\tag{22}
$$

反过来，对全部正 t、s 取下确界，其准确值就是 (21) 的左边。在系数严格正时分别在 $t=\sqrt{C/A}$、$s=\sqrt{D/C}$ 取到；零系数情形通过正参数趋于0或无穷的极限给出同一下确界。正有理数稠密，故 (22) 只对正有理 t、s 逐条要求，也与 (21) 等价。

这给现有有理必要系统一个直接接口：固定有理 $\kappa,t,s$ 后，A、Q、B、C 都是已发表同一字符坐标的线性行，$D=Q+25A/9$ 也线性，所以 (22) 是一条准确有理半空间。无需重新计算真实路径积分、原 forcing、profile 值或旧 RREF。

若某个外候选在一个有理 $\kappa$ 违反 (21)，且 A、D、C 非负，则存在正有理 t、s 使 (22) 严格切掉它。若违反发生在实 $\kappa$ 且有严格余量，各系数对 k 的连续性也允许选邻近有理 $\kappa$；出现基础符号条件负值时应直接用对应已证明必要条件，而不先把负数带入平方根。

没有违反具体候选时，不应无目标地加密 t、s、k 网格。对一个外点通过所有已取行，也不能宣布其完整固定 k 正性，更不能宣布真实函数关系或一般变 k action 已支付。

## 6. 结论范围

新增的是固定 k 子类的**完整零/二/四导数 action 充要判据**、正平端函数类的 sharp 插值常数、临界截断的完整支付，以及可直接消费已存线性行的有理必要条件。

式 (5) 允许 B 为负，只限制其负值可由同一静态与最高层支付到什么程度。它没有把 R140 的完整正性错误拆成各层分别非负。任何应用仍使用同一 R164 乘子，不为各 k 或各路径重新选 μ。

本稿不宣称现有外候选违反新门，不证明外坐标已经定义真实字符，也不授 signed control、完整 period/ruling 或主课题的闭嵌入、固定 g 连续等距族与全时 reach。
