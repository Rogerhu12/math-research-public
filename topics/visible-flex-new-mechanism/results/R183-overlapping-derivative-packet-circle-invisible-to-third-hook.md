# R183：真正重叠的导数分包 profile 圆与不可见第三 hook

日期：2026-11-15。**独立纸面构造；未运行新的研究计算。** 本稿接 [R180](R180-fixed-circle-invisible-third-hook-and-signed-fourth-period-gauge.md) 和 [R181](R181-degenerate-self-adjoint-equation-for-fixed-circle-period-gauges.md)，证明其真实有符号第四周期 gauge 并不只能用于不交 profile 平面。

准确结论是：存在真实闭合、$M=0$、整个 $T=\kappa\mathfrak H\ne0$ 的光滑周期几何，以及非退化、归一、$C^\infty$ 三矩圆，使任何常数可逆换基都不能把该圆变成两条支撑不交的 profiles；该圆的完整二、三阶 range 仍成立，且保留 R180 的第四周期有符号线。第四逐 ruling、第四周期本身的全函数匹配及有限等距族仍未解决。

## 1. Hook 的原函数只有单层三次导数密度

记 $J(F)(x)=\int_x^rF(\eta)\,d\eta$，采用 R81 的

$$P(a,b)=J(a''b''),\quad
R(a,b)=a'b'+xJ(a''b''),\quad
S(a,b)=J(\eta a''b''),$$

$$\mathfrak H=[P,S]-3[P,R].$$

对任意 a、b、c，置 $Q=S-3R$。直接求内层导数有

$$P(b,c)''=-(b''c'')',$$

$$Q(b,c)''=-b''c''+2x(b''c'')'
-3(b'''c'+b'c''').$$

代回 $P(a,Q(b,c))-Q(a,P(b,c))$，得到准确同锚表示

$$\boxed{\begin{aligned}
\mathfrak H(a;b,c)={}&-3a'b''c''-J(a''b''c'')\\
&+3J\bigl((\eta-x)a''(b''c'')'\bigr)\\
&-3J\bigl(a''(b'''c'+b'c''')\bigr).
\end{aligned}} \tag{1}$$

每一项只用三个输入的正阶导数和一个共同右积分。特别地，没有一个内层原函数尾常数继续乘另一个 packet 的导数。

R81 的原式恒等 $\mathfrak H(q;q,q)=0$ 也适用于“q 自身可在 collar 为常数、但所有正阶导数在那里为零”的辅助函数：P、R、S 以及证明中的全部边界只使用正阶导数。这里只在证明分解时使用这种辅助函数，最终几何 profiles 本身仍双 collar 为零。

## 2. 导数分包引理

设 $J_1,\ldots,J_m$ 是互不相交的紧区间，$\rho_j$ 是其中的实光滑紧支撑函数。设两条实 profiles 满足

$$f'=\sum_j a_j\rho_j,\qquad
g'=\sum_j b_j\rho_j,\qquad a_j,b_j\in\mathbb R. \tag{2}$$

即每个导数包内，向量 $(f',g')$ 沿一个固定实方向；profiles 的值在包间可以有非零平台。

**引理。** 对 $\mathcal P=\operatorname{span}_{\mathbb R}(f,g)$，

$$\boxed{\mathfrak H\big|_{\mathcal P\times\operatorname{Sym}^2\mathcal P}=0.} \tag{3}$$

**证明。** 取辅助函数 $\eta_j'=\rho_j$。它可以在两端取不同常数，但所有正阶导数支撑于 $J_j$。对任意 $a,b,c\in\mathcal P$，它们在 $J_j$ 上的所有正阶导数分别是 $\eta_j$ 正阶导数的固定倍数 $\alpha_j,\beta_j,\gamma_j$。

式 (1) 的每个被积项是同一点三个输入导数的乘积，所以不同 $J_j$ 的交叉项全为零。局部项也逐包分开，因此

$$\mathfrak H(a;b,c)
=\sum_j\alpha_j\beta_j\gamma_j
\mathfrak H(\eta_j;\eta_j,\eta_j)=0.$$

最后一步用同一个真实右锚的对角恒等式。这里不是声称一般第三恢复都局部化；局部化只对已经准确化简的这个 hook 成立。$\square$

## 3. 一个不能换基变成不交的具体重叠平面

在一个开区间中选择四个从左到右排列、互不交的导数支撑。取非负、非零、光滑紧支撑 $\rho_j$，归一化 $\int\rho_j=1$。令

$$s_j(x)=\int_{-\infty}^x\rho_j(t)\,dt,$$

$$f_0=s_1-s_3,\qquad g_0=s_2-s_4. \tag{4}$$

两者都是光滑紧支撑函数。其值从左到右依次经过

$$(f_0,g_0):(0,0)\longrightarrow(1,0)
\longrightarrow(1,1)\longrightarrow(0,1)
\longrightarrow(0,0).$$

导数满足 (2)，四个方向为 $(1,0),(0,1),(-1,0),(0,-1)$，所以 (3) 成立。

在三个包间开放平台，取值分别是 $(1,0),(1,1),(0,1)$，它们给三条不同的实射影方向。如果一个常数可逆实 $2\times2$ 矩阵把这个平面换为支撑不交的两函数，则变换后的每个取值必须落在两条坐标轴的并中。变回原坐标，全部原取值只能落在两条固定直线的并中；这不可能包含上述三条不同射影方向。

因此不仅没有 O(2) 换基，甚至没有任何常数 GL(2) 换基能把 (4) 变为不交支撑。这个性质使用 profile 的值，不与其导数分包相矛盾。

## 4. 准确三矩补偿保持导数分包

令 $q_0=f_0+ig_0$，记普通复平方的三个总矩

$$M_0(q)=\int(q'')^2,\quad
M_1(q)=\int x(q'')^2,\quad
M_2(q)=\int x^2(q'')^2+2\int(q')^2. \tag{5}$$

它们不必已为零。按 [R86](R86-left-moment-completion-preserves-right-Volterra-obstructions.md) 的准确三矩补偿，在 (4) 支撑左方选三个互不交的同形实偶 bump $\eta_j(x)=\eta(x-c_j)$，中心 $c_j$ 不同。令

$$a_0=\int(\eta'')^2>0,\qquad
a_2=\int x^2(\eta'')^2+2\int(\eta')^2.$$

三个 moment 列为

$$v_j=(a_0,\ a_0c_j,\ a_2+a_0c_j^2)^T.$$

其行列式是 $a_0^3\prod_{i<j}(c_j-c_i)\ne0$。准确求复数 $z_j$，使

$$\sum_jz_jv_j=-(M_0(q_0),M_1(q_0),M_2(q_0))^T.$$

任取 $\beta_j^2=z_j$，定义

$$\widehat q=q_0+\sum_j\beta_j\eta_j
=\widehat f+i\widehat g. \tag{6}$$

支撑分离给 $M_\nu(\widehat q)=0$，$\nu=0,1,2$。每个新增导数包中

$$(\widehat f',\widehat g')
=(\operatorname{Re}\beta_j,\operatorname{Im}\beta_j)\eta_j',$$

仍是一个固定实方向乘一个实函数。因此 (2)、(3) 完整保留；普通复平方根没有破坏 hook 消去。

左侧补偿不改变第三个原导数包上的 $(f_0,g_0)$，故真正重叠性质也保留。由 $M_0=0$，

$$\int(\widehat f'')^2=\int(\widehat g'')^2=:E>0,
\qquad \int\widehat f''\widehat g''=0.$$

严格正性因为右侧原矩形 profile 非零。另两复零矩给其余对角等长、交叉零矩。因此 $\widehat f,\widehat g$ 是非退化三矩圆；同乘 $E^{-1/2}$ 可归一化。

本节只使用有限准确积分来定义系数和一个可逆三阶线性系统，没有执行 profile 数值求积或拟合。没有声称可对所有参数连续选取复平方根；本构造只需要一个固定 pair。

## 5. 八个完整 packet 支付全部第三 ruling

把第 4 节的 pair 视作一个完整基本 packet，记为 $(f_*,g_*)$。取八个互不交的等距平移 $t_j=t_*+jL$，并取

$$a_j=(-1)^j\binom7j^{1/3},\qquad
f=\sum_{j=0}^7a_j f_*(x-t_j),\quad
g=\sum_{j=0}^7a_j g_*(x-t_j). \tag{7}$$

之后可对整个构造作共同实幅度及正仿射坐标缩放，放入真实几何的共同物理区间 I 并留双 collar。R39 的矩变换律保持三复零矩；导数分包和 (3) 也直接保留。

这里必须使用 [R52](R52-overlapping-profile-plane-complete-third-order-circle.md) 的两个二阶 forcing：

$$H_d=(dY_f)^2-(dY_g)^2,\qquad
H_c=\mathcal S(Y_f,Y_g).$$

$H_c$ 一般非零，不得套用不交平面的简化。每个基本 packet 的对角三矩相等和交叉三矩为零，分别使这两个 forcing 的二阶右尾在包外全零。故它们的 canonical 二阶解按 $a_j^2$ 局部化。

R46/R52 已证明：对任意固定真实变量几何，四条第三 forcing $(f,d),(g,d),(f,c),(g,c)$ 的完整 ruling 函数，在平移回基本坐标后都是平移参数 t 的次数至多六的多项式。其原式保留真实 second 历史与混合分量，不要求 f、g 在基本 packet 内不交。

因此四条 ruling 均按 $a_j^3=(-1)^j\binom7j$ 相加，第七有限差分使其对每个真实 s 准确为零。没有重新调整二阶 gauge，也不把二阶局部化外推到第四阶。

## 6. 在非零全第三算子的真实闭几何上完整通过三阶

取 R180 第 6 节的 Klein 闭合几何；它由实际有限控制和准确 frame 桥构成，有

$$M=0,\qquad T=\kappa\mathfrak H,\qquad \kappa\ne0.$$

构造有限条几何路径之后选择共同合法物理 I，再把 (7) 放入 I。全 M=0 和三矩支付两个二阶 forcing 的完整 range。

由 (3)，T 对 f、g 平面上的所有三次槽均为零，因此上述四条第三 forcing 的整个周期函数也全部为零。这替代了 R52 原构造使用的倒行奇性，不把整个 T 冒称为零。结合第 5 节的四条 ruling，完整 range 给真正光滑、周期、双 collar 的 $Z_d,Z_c$ 和 $W_{fd},W_{gd},W_{fc},W_{gc}$。

对同一个目标 $g_\varepsilon=g_X+\varepsilon^2(dY_f)^2$，令

$$Y_\theta=cY_f+sY_g,$$

$$Z_\theta=s^2Z_d-csZ_c,$$

$$W_\theta=s^2(cW_{fd}+sW_{gd})
-cs(cW_{fc}+sW_{gc}). \tag{8}$$

全部二、三阶方程成立，且 $\theta=0,\pi$ 的高阶校正为零。所得三阶 Taylor 圆的误差仍是统一 $O(\varepsilon^4)$，不是精确有限等距。

限制到任意非零基本 packet 的原矩形区间，第 3 节的不可换基证明仍成立。因此这确是一条真正重叠的合法 profile 圆，不是旧不交圆的常数旋转。

## 7. 原有符号周期 gauge 与多包版本继续合法

现在取 R180 的二阶齐次 gauge $w_\theta=a(\theta)w$，其中 a 光滑、$2\pi$ 周期且 $a(0)=a(\pi)=0$，w 在 f、g 的整个支撑邻域仿射。其与 f、g 的六个交叉矩仍全零，不依赖 f、g 是否重叠。R180 的真实第三补偿及 hook 循环身份逐字适用，给

$$\boxed{\Delta V_\theta
=-6\kappa C\,a(\theta)(f'')^2.} \tag{9}$$

取 $a(\theta)=\sin^2\theta$ 时 pure 模式不变，mixed 模式增加 $3\kappa C(f'')^2/2$。

也可以在 (7) 的八个完整 packet 包络上分别取仿射斜率 $C_j$。R181 逐包矩论证仍成立，并给至少八个非零、不交支撑、实线性无关的 mixed 周期方向

$$\Delta V_{-2}=\frac{3\kappa}{2}
\sum_{j=0}^7 C_j\bigl((a_j f_*(\,\cdot-t_j))''\bigr)^2. \tag{10}$$

真实几何、第一 profile 圆、目标和右锚不改变。二阶齐次 gauge 是新的固定圆选择，不是增加一个被假定为零成本的几何环。

## 8. 已消掉的限制与保留的问题

本稿消掉的是 R180 具体低阶例的“不交 profile 平面”限制。R50 以该不交性为前提的结论不能直接应用于这里，不能据此倒推本构造第四阶已经可解。

第四逐 ruling 对新增 gauge 的线性和二次影响、完整第四周期是否落在 (9)–(10) 或 R181 的退化方程像中，都仍未支付。真正重叠的几何并不自动具有 reach、嵌入或宏观幅度；各辅助路径可能很长。

本构造不重复或依赖 faithful 圆定理，不假设 R177 是良定义字符，也不调用新的函数秩或数值结果。其新增内容是一个准确、非退化、真正重叠且对真实第三 hook 不可见的 profile 类，以及它与已证明的第四周期 gauge 自由度的兼容。

