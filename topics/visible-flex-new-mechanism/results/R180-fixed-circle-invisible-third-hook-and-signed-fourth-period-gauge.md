# R180：固定圆不可见的第三 hook 与准确有符号第四周期 gauge

日期：2026-11-15。**纸面完整证明，无新的研究编译、profile 积分或几何计算。** 依据 [R71](R71-third-holonomy-commutators-and-complete-fourth-P1.md)、[R81](R81-real-third-hook-control-and-mixed-phase-response.md)、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)。真实闭合例再用 [R37](R37-closed-geometry-zero-period-operator.md)、[R46](R46-eight-packet-complete-third-order-circle.md) 和 [R72](R72-same-state-zero-second-third-arbitrary-frame-bridge.md)。

本稿证明一个此前的全算子零条件会隐藏的自由度：真实路径的整个第三算子可以非零，却对选定 profile 圆的低阶相容通道不可见；此时二阶齐次 gauge 可以在保持同一目标及完整二、三阶 range 的同时，准确改变第四周期函数。这个改变有任意实系数，不伴随未知的偶次周期成本。

**范围。** 这是一条第四周期控制线，不是第四完整 range 解。第四逐 ruling 条件没有因本稿自动支付，也未构造有限非零参数的精确等距族。本稿不以此否定条件性 canonical 正字符：新的二阶 gauge 和非零第三算子产生了原零传入 canonical 类之外的交叉项。

## 1. 同一目标与固定圆实际需要的低阶通道

固定真实周期 ruled 几何，scalar 状态及 frame 平滑返回，取共同紧物理区间 $I$，其上 $h>0$、$\xi+\omega>0$。全部 profiles 在双侧开放 collar 为零，使用同一右锚和同一个 $s$ 起点。

记路径的完整 second 算子及 third 算子为

$$A=\Phi_M,\qquad T(a;b,c),$$

其中 T 仅对内两槽对称。固定两个实 profiles f、g 与目标规则

$$F=f^2,\qquad \phi_\theta=c f+s g,
\qquad c=\cos\theta,\quad s=\sin\theta,$$

$$g_\varepsilon=g_X+\varepsilon^2(dY_f)^2,
\qquad D_\theta=F-\phi_\theta^2=s^2d-cs e,$$

$$d=f^2-g^2,\qquad e=2f\odot g. \tag{1}$$

对于零传入 second/third scalar 历史，R83 给二阶周期 $A(D_\theta)$ 和三阶周期 $-2T(\phi_\theta;D_\theta)$。因此它们对全部相位为零，当且仅当分别满足

$$A(d)=A(e)=0, \tag{2}$$

以及

$$\boxed{T(f;e)=0,\qquad T(g;d)=0,
\qquad T(f;d)-T(g;e)=0.} \tag{3}$$

这里每个等式都是整个 $\xi$ 函数恒等式。证明只需展开

$$T(\phi_\theta;D_\theta)
 =cs^2\{T(f;d)-T(g;e)\}+s^3T(g;d)-c^2sT(f;e).$$

三个实相位函数 $cs^2,s^3,c^2s$ 线性独立。式 (2)、(3) 只是周期门；相应逐 ruling 条件仍须支付。它们不要求 A、T 在所有其他 profiles 上为零。

以下取更强而可真实实现的 $M=0$，但**不**取整个 $T=0$。

## 2. 一个真实可达且对角恒零的第三算子

记正右积分为 $J(F)(x)=\int_x^rF(\eta)\,d\eta$。采用 R81 的三个准确八矩算子

$$P(a,b)=J(a''b''),\qquad
R(a,b)=a'b'+xJ(a''b''),\qquad
S(a,b)=J(\eta a''b'').$$

定义

$$\mathfrak H=[P,S]-3[P,R],\qquad
[P,Q](a;b,c)=P(a,Q(b,c))-Q(a,P(b,c)). \tag{4}$$

R71 的有限真实控制环实现任意固定有限倍数 $\kappa\mathfrak H$，同时保持 $M=0$ 以及同一 scalar/frame 端口。R81 已证明原式恒等

$$\mathfrak H(q;q,q)=0, \tag{5}$$

及其三次极化

$$\mathfrak H(a;b,c)+\mathfrak H(b;c,a)
+\mathfrak H(c;a,b)=0. \tag{6}$$

它不是零算子。若 w 在 f 支撑的邻域内准确仿射，$w'=C$，则同一右锚的原式给

$$\boxed{\mathfrak H(w;f,f)=-3C(f'')^2.} \tag{7}$$

式 (7) 不需要把 w 在整个物理区间取成非紧支撑直线：只需在那里仿射，再在远离 f 的区域光滑截断。

设一条真实路径满足

$$\boxed{M=0,\qquad T=\kappa\mathfrak H,
\qquad\kappa\ne0.} \tag{8}$$

由 (5)，对固定目标 F，

$$T(\phi_\theta;D_\theta)
=\kappa\mathfrak H(\phi_\theta;f,f)
=\kappa s\mathfrak H(g;f,f). \tag{9}$$

所以其固定圆第三周期门准确缩成一个函数条件

$$\boxed{\mathfrak H(g;f,f)=0.} \tag{10}$$

例如 f、g 支撑不交时，该条件成立，实际上 $\mathfrak H$ 在
$\operatorname{span}(f,g)\times\operatorname{Sym}^2\operatorname{span}(f,g)$ 上全零：内交叉的 P、R、S 都为零，再用 (5)、(6) 即得剩余槽为零。整个 universal 算子仍由 (7) 证明非零。

## 3. 不改变目标的二阶齐次校正及真实三阶补偿

现在假设已选定的 f、g 圆在 (8) 的几何上，使用共同 canonical 锚，完整二阶和三阶 range 已经成立。第 6 节给一个真实的闭合例。

取任意实光滑 w，在整个 $\operatorname{supp}f\cup\operatorname{supp}g$ 的邻域内满足

$$w(\xi)=C\xi+b, \tag{11}$$

并在双侧外 collar 恒为零。选择任意 $2π$ 周期光滑实相位函数 a，使

$$a(0)=a(\pi)=0,\qquad w_\theta=a(\theta)w. \tag{12}$$

把二阶校正改为

$$Z_{2,\theta}^{\rm new}=Z_{2,\theta}-Y_{w_\theta}. \tag{13}$$

$Y_w$ 是同一几何上的齐次无穷小弯曲，故 (13) 不改变二阶度量方程，目标仍是 (1) 的同一个 $g_\varepsilon$。它不改变一阶 f、g，也不改变几何 M、T。

三阶 forcing 的变化是 $2H(Y_{\phi_\theta},Y_{w_\theta})$。其中 $H$ 沿用 R83 的对称双线性规范。按同一右锚与真实 $s$ 历史，取补偿

$$Z_{3,\theta}^{\rm new}
=Z_{3,\theta}+2Z_B(\phi_\theta,w_\theta), \tag{14}$$

这里 $Z_B(a,b)$ 是 $H(Y_a,Y_b)$ 的完整 second 恢复，不在中间拼接点重锚。

**式 (14) 是合法的周期、双 collar 校正。** 对 $a=f$ 或 g，三个交叉总矩为

$$I_0(a,w)=\int a''w''=0,\qquad
I_1(a,w)=\int \xi a''w''=0,$$

$$I_2^*(a,w)=\int\xi^2a''w''+2\int a'w'
=2C\int a'=0. \tag{15}$$

前两项因为 $w''=0$ 于 a 的支撑邻域；最后一项使用 a 的双端零值。故二阶平方极化 forcing $H(Y_a,Y_w)$ 的全部逐 ruling 条件成立。其完整周期函数是 $A(a,w)=0$，由整个 M=0 支付。完整 range 定理因而给 (14) 所用真实光滑、周期、双 collar 场。

因此 (13)、(14) 保持原圆的完整二、三阶相容性。又由 (12)，$\theta=0,\pi$ 两个准确种子的新增校正同时为零。没有靠一个非周期或未付 collar 的形式解改变第四项。

## 4. 第四周期的准确有符号函数线

记原 canonical 第四周期为 $V_B(F,\phi_\theta)$。R83 的传入历史公式对 (13)、(14) 直接给

$$\begin{aligned}
\Delta V_\theta={}&2T(w_\theta;D_\theta)
-4T(\phi_\theta;\phi_\theta,w_\theta)\\
&-A(w_\theta,w_\theta)+2A(\phi_\theta,u_\theta).
\end{aligned} \tag{16}$$

可取传入 third scalar $u_\theta=0$；事实上整个 A=0 使最后两项对任意允许的 $u_\theta$ 都为零。特别是二阶 gauge 的平方项没有产生未记载的 $C^2$ 周期成本。

在 (6) 中取 $(a,b,c)=(w_\theta,\phi_\theta,\phi_\theta)$，得到

$$\mathfrak H(w_\theta;\phi_\theta,\phi_\theta)
+2\mathfrak H(\phi_\theta;\phi_\theta,w_\theta)=0.$$

代入 $D_\theta=F-\phi_\theta^2$，(16) 准确化为

$$\boxed{\Delta V_\theta
=2\kappa\mathfrak H(w_\theta;F).} \tag{17}$$

这一步对任意 $w_\theta$ 都成立；(11)、(15) 是为了同时支付新增校正的真实 range。再用 (7)、(12)，得到

$$\boxed{V^{\rm new}_{B,\theta}
=V_{B,\theta}-6\kappa C\,a(\theta)(f'')^2.} \tag{18}$$

系数 C 可取任意有限实数；w 的截断可固定，只改变仿射幅度。式 (18) 是整个 $\xi$ 函数的准确身份，不是采样值、导数切向或只到一阶的展开。几何、目标、第一 profile 圆及真实锚全不改变。

尤其取 $a(\theta)=\sin^2\theta$。在 $\zeta=e^{-i\theta}$ 规范中，

$$\boxed{\Delta V_{-4}=0,\qquad
\Delta V_{-2}=\frac{3\kappa C}{2}(f'')^2,\qquad
\Delta V_0=-3\kappa C(f'')^2.} \tag{19}$$

共轭模式同步改变，故 $\theta=0$ 的零值继续成立。只要 $f\ne0$，其紧支撑性质迫 $f''$ 不恒为零，(19) 因而给一个非零且两号都可取的完整 mixed 周期方向。

任意相位函数 a 也可用于 (18)；因此 pure 模式不变是 $\sin^2\theta$ 这一选择的性质，而非任意二阶 gauge 的普遍性质。

## 5. 这条线对第四求解准确意味着什么

在固定的 (8) 几何和合法圆上，所有 (11)–(14) 的 gauge 给

$$V_{B,\theta}+\mathbb R\,\sin^2\theta(f'')^2$$

这一真实可取的第四周期仿射线。若原周期恰为该函数方向的实倍数，可以准确选择 C 将它消去；一般周期函数不在这一条线上，本稿不声称满射。

即使第四周期被这一线消去，第四 forcing 的逐 s ruling 条件仍可能不为零。完整 fourth forcing 含真实二阶 gauge 的平方及三阶补偿，尽管其 $C^2$ 周期积分为零，不能因此把其 ruling 影响删掉。

特别是已有不交 profile 圆和常态段的第四 ruling 障碍（例如 R50 的适用情形）仍然有效。本稿的具体低阶例不是新的完整四阶成功候选，不应因此安排重复的旧不交 packet 数值。

## 6. 完整低阶假设有真实闭合的实现，且整个 T 确实非零

固定一个常值 scalar germ S。由 R71、R81 构造一条实际有限环 $L_t$，首末 frame I、首末 scalar S，且

$$M_{L_t}=0,\qquad T_{L_t}=t\mathfrak H,\qquad t\ne0.$$

由 R72，取同一 scalar 端口下两条实际桥 $C_j:I\to g_j$，其中

$$g_1=\operatorname{diag}(1,-1,-1),\qquad
g_2=\operatorname{diag}(-1,1,-1),$$

且每条 $M=T=0$。令

$$P_1=L_tC_1,\qquad P_2=C_2.$$

因为每段 M=0，真实 composition 的第三交叉项为零，所以

$$M_{P_1}=M_{P_2}=0,\qquad T_{P_1}=t\mathfrak H,
\qquad T_{P_2}=0. \tag{20}$$

按 R37 的 Klein 八边词 $1,2,1,2,2,1,2,1$ 拼接：每类路径分别在
$\mathcal G=\{I,g_1,g_2,g_1g_2\}$ 的四个左旋位置各出现一次。ambient 左旋不改变 scalar 算子。端 frame/scalar germs 全部准确相接，且

$$\sum_{g\in\mathcal G}g=0$$

使两类路径的真实中心线位移分别相消。得到有限、光滑、闭合周期浸入带，并有

$$\boxed{M_{\rm total}=0,\qquad
T_{\rm total}=4t\mathfrak H\ne0.} \tag{21}$$

不是先把单桥的位移设为零，也没有用倒行把全第三算子消去。构造完有限条路径后选择共同物理区间 I，再选择 profiles；不声称任意预给窄 I 都容许这些辅助桥。

在 I 内取 R46 的八个三矩配平、不交平移 packet 圆。其 f、g 支撑不交，故 (10) 成立，完整三阶周期为零。R46 第 2–6 节的 ruling 消去只用真实变量几何公式、共同零起点锚、每 packet 三矩配平和七阶有限差分：它对任意这条固定真实几何同样成立，不需要几何另有倒行奇对称。具体地，每 packet 的二阶校正局部化，平移参数的第三 ruling 次数至多 6，八个幅度的三次幂为 $(-1)^j\binom7j$，所以每个真实 s 的全部两条 ruling 函数都为零。

M=0 与三矩支付二阶完整 range；(10) 和上述有限差分支付三阶完整 range。于是第 3 节的前提确有真实、闭合、非退化、光滑 profile 圆实例，且其全第三算子仍由 (21) 严格非零。统一实缩放可以归一化圆而不改变任何零条件。

## 7. 为什么这不直接否定 canonical U 上的正字符

R105/R109 的 U 使用零传入 second/third scalar 的 canonical 恢复，保持固定的 quartic profile 规则。这里 w 是选定圆之后独立选择的二阶齐次 profile；它的仿射斜率 C 不是由原零传入规则自动给出的 $P(D)$。

R83 已明确：当整个 $M=T=0$ 时，任意允许的传入历史只使第四历史增加同一个 $V_B$。本稿保 M=0，但故意采用 $T=\kappa\mathfrak H\ne0$；T 只在原圆所需的低阶槽上不可见，不能删掉它在 w 槽中的值。式 (16) 正是那个未被删除的真实交叉项。

所以，若 R177 指定点最终定义了 U 上的正字符，它对本几何的**原 canonical** 成本仍适用；不能未经证明便把同一泛函和同一作用量公式延到独立 w 的新增成本，再得出矛盾。反过来，本稿也没有证明任何实际第四周期已归零，更没有证明完整 fourth ruling、所有阶、收敛、嵌入或 reach。

所证明的新事实准确是：全第三算子零并非固定圆完整低阶相容性的必要条件；保留一个在该圆上不可见但在二阶 gauge 上可见的真实第三 hook，能产生 (18) 这种零基线、准确有符号的第四周期变化。
