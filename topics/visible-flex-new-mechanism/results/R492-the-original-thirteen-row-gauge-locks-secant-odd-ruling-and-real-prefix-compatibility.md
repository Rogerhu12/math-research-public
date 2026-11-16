# R492：原十三规范锁定正割段的奇 ruling 及其真实前缀相容条件

日期：2026-11-16。**完整原式纸面证明。没有执行符号程序、profile 求积、原根恢复、矩阵秩、开发检查或新的科学计算。**

[R488](R488-real-secant-height-patches-and-complete-same-gauge-ruling.md) 已把一条真实正割高度段的完整第四 ruling 缩为三个系数，但没有授予这三个系数在原十三行核中的满射。本稿准确支付其中的奇行：在当前从起点选取的偶母库上，这个新行在整个 period 齐次核中的作用，已经是原四行 $P_{-4},P_{-3},P_{-2},H_{B,0}$ 的显示线性组合。

因此，保护有理芽与完整 period 已同时支付之后，剩余同一个二阶规范不能再改变任一正割段的奇 residual。平台列不为零；它们恰好通过 $P_{-2}$ 进入上述身份。这个结论不是“包数不够”，而是原全核上的准确行关系。

本稿还将该固定 residual 写为一个真正的 period-source 商泛函，加上同一个最终词中两个真实二阶前缀之差。对有限多段只需有限个实际系数，但本文没有宣称它们已为零、已独立或已可由实际路径控制。两个 even 系数、所有连接桥的 ruling、全部成本与相位条件仍保留。

## 1. 同一个真实圆、完整核和被保护的规范

固定 R455/R480 从构造起点选取的同一个库、同一实际闭词、物理区间 $I=[x_-,x_+]$、双零 collar 和原右积分
$$
J(q)(x)=\int_x^{x_+}q(t)\,dt.
$$
设原总矩阵和第三 period 为
$$
M=0,\qquad \mathbf T=\tau\mathfrak H,\qquad \tau\ne0.
\tag{1}
$$
不交 rank-one 包圆为
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta .
\tag{2}
$$
所有 $a_i\ne0$。实际位置、正宽度、复制权、角色、suffix 和最终母形全部保留。

当前母库的每个 $u_i$ 关于自己的中心偶对称；平移与正宽度缩放不改变
$$
\mathfrak p(u_i):=\int u_i'(u_i'')^2=0.
\tag{3}
$$
这里用的是原偶函数类中的构造，不从 whole $W$ 外矩为零推(3)。后文也给不满足(3)时的准确附加项，避免把结论扩大到任意母。

沿用原三个完整配对
$$
\mathbf I(a,b)=\left(
\int a''b'',\
\int xa''b'',\
\int(x^2a''b''+2a'b')
\right).
\tag{4}
$$
$L_f k=\mathfrak H(k;f,f)$ 是原完整 period 算子。R327/R469 的同 collar 核分类是
$$
\ker L_f=
\operatorname{span}\{u_i,\chi_i\}_i\oplus\mathscr G,
\tag{5}
$$
其中 $\chi_i$ 在第 $i$ 包邻域为1、在其它包邻域为0，且只在真实间隙内过渡；$\mathscr G$ 在所有活动包上恒零。不同包的真实平台值没有被清零。有限 simple-$p$ 点与原 $A_f$ 点的全核分类前提仍按原文保留。

已支付的有理保护芽采用同一物理 $x$：
$$
h=H_p(1+\varepsilon\sigma^2),\qquad
k=\kappa\ne0,\qquad\omega=0,\qquad H_p,\varepsilon>0.
\tag{6}
$$
记
$$
K=1+\kappa^2,\qquad
a=\frac{K(\varepsilon-2K)}{32H_p^2},\qquad
e=\frac{\kappa K}{4H_p},\qquad t=-\frac{\varepsilon}{4},
\qquad B=aR-2eL+eU+tT .
\tag{7}
$$
原十三行仍是
$$
\mathcal A_\theta(\eta)=
\bigl(\mathbf I(\phi_\theta,\eta),\
(P_{\ell,\theta}(\eta))_{-4\le\ell\le2},\
(H_{B,j,\theta}(\eta))_{0\le j\le2}\bigr).
\tag{8}
$$
十三是原列出的条件数，不是本稿新算的秩。

设 R467/R469 的同一个全局规范已经支付完整 period、合法性和这个保护芽。后继允许变化必须满足
$$
L_f\eta_\theta=0,\qquad \mathcal A_\theta(\eta_\theta)=0.
\tag{9}
$$
第三规范的三个 ruling 矩则由 R469(14)唯一锁定，包含新旧二阶规范的平方和交叉。不能在另一个 $s$ 段重新选择它们。

## 2. 真实正割段及准确奇行

考虑同一实际词中的一条 R488 正割段：
$$
k=0,\quad \omega=\omega_s\text{ 为常数},\quad
v=h_s/h,\quad v_s=1+v^2,\quad
h=H_s\sqrt{1+v^2},\quad y=x+\omega_s .
\tag{10}
$$
$H_s>0$。只作坐标记号 $y=x+\omega_s$，不搬动原 profiles 或改变右锚。

该段真实累计算子准确为
$$
\mathsf A_s=\mathsf A_*+\mathsf A_{\rm sec},\qquad
\mathsf A_{\rm sec}=-\frac{v}{8h^2}R_y-\frac v8T_y .
\tag{11}
$$
$\mathsf A_*$ 是原积分常数；若中心 $v=0$ 位于实际段内，它就是这个真实中心的 incoming 算子。它不是可自由赋值的矩阵。下面的核列身份在任何非空正割子段成立，不要求能沿该分支作 $M=0$ 返回。

原完整响应是
$$
\begin{aligned}
\mathcal B_\theta(\eta)
={}&2\mathcal T_s(\eta;D_\theta)
-4\mathcal T_s(\phi_\theta;\phi_\theta,\eta)\\
&-2\mathcal E_s(\mathsf A_sD_\theta,\eta)
+4\mathcal E_s\{\phi_\theta,\mathsf A_s(\phi_\theta,\eta)\}.
\end{aligned}
\tag{12}
$$
其中在 $y$ 坐标
$$
\mathcal E_s(a,b)=\frac{I_0^y(a,b)}{4h}+\frac h4I_2^y(a,b).
\tag{13}
$$
原 $I_2$ 的一导项始终保留。

R488(39)—(41)给
$$
\mathcal B_\theta(\eta)|_{\rm sec}
=\frac vh\,\beta_\theta^{H_s,\omega_s}(\eta)
+2\mathbf w(s)\cdot\mathbf H_{\mathsf A_*,\theta}(\eta),
\tag{14}
$$
$$
\mathbf H_{\mathsf A_*,\theta}(\eta)
=-\mathbf I(\mathsf A_*D_\theta,\eta)
+2\mathbf I\{\phi_\theta,\mathsf A_*(\phi_\theta,\eta)\}.
$$
后项在 $v$ 中偶。因此 $\beta$ 是完整奇系数，不是 principal 或只看一个几何点的近似。

为固定任意紧 $\eta$ 上的定义，置
$$
\mathsf R_H=-R_y/(8H^2)-T_y/8,\qquad
\dot{\mathcal T}_H=\left.\partial_v\mathcal T_s\right|_{v=0}.
$$
则
$$
\begin{aligned}
\beta_\theta^{H,\omega}(\eta)=H\big[
&2\dot{\mathcal T}_H(\eta;D_\theta)
-4\dot{\mathcal T}_H(\phi_\theta;\phi_\theta,\eta)\\
&-2\mathcal E_H(\mathsf R_HD_\theta,\eta)
+4\mathcal E_H\{\phi_\theta,\mathsf R_H(\phi_\theta,\eta)\}
\big].
\end{aligned}
\tag{15}
$$
$\dot{\mathcal T}_H$ 正是 R488(40)的完整原 local pairing，来自 R221 的原尾转置。这一定义适用于任意紧输入；下文更简单的母/平台公式只在(5)中使用。

## 3. 母列的完整相消：没有三阶平方或被删的左尾

暂取任意真实紧 $u$，记 $p=u'$、$r=u''$，所有位置变量写 $y$。原 E8 对角为
$$
R_y(u,u)=p^2+yJ(r^2),\qquad
T_y(u,u)=y^2p^2+yJ(y^2r^2+2p^2).
\tag{16}
$$
这两个输出通常都有真实左尾。定义
$$
F_{X,j}^y(u)=I_j^y\{u,X_y(u,u)\}.
$$
R259 原表与同锚 IBP 给以下完整式：
$$
\begin{aligned}
F_{R,0}^y&=-\frac13\int r^3,\\
F_{R,1}^y&=\int(-pr^2+yr^3/3),\\
F_{R,2}^y&=\int(y^2r^3-4ypr^2+2ur^2),\\
F_{T,0}^y&=\int(2ypr^2-y^2r^3)=-F_{S,2}^y,\\
F_{T,2}^y&=\int\left(
-2y^3pr^2+\frac{y^4r^3}{3}
-\frac{4yp^3}{3}+2y^2ur^2+4up^2
\right).
\end{aligned}
\tag{17}
$$
尤其
$$
F_{R,2}^y+F_{T,0}^y
=2\mathfrak m_y(u),\qquad
\mathfrak m_y(u)=\int(u-yp)r^2 .
\tag{18}
$$

可以直接对全段代入 R469(26)，不必由中心的一次导数猜整个函数。此时
$\gamma=hv$、$e_{\rm geom}=hy$、$(e_{\rm geom})_s=hvy$。把原积分提出 $v/(32h^3)$ 后，剩余密度为
$$
\begin{aligned}
&Q^2u'''(2pr-yr^2)-2h^2yQ\,u'''p^2\\
&\quad +(Qr-2h^2yp+2h^2u)
\{(1-h^2y^2)r^2-2h^2p^2\},\qquad Q=1+h^2y^2.
\end{aligned}
\tag{19}
$$
分别按 $1,h^2,h^4$ 收集并做紧外槽 IBP，积分系数准确是
$$
-F_{R,0}^y,\qquad F_{R,2}^y+F_{T,0}^y,\qquad -F_{T,2}^y .
\tag{20}
$$
例如零次项用
$2pru'''=(pr^2)'-r^3$、$r^2u'''=(r^3)'/3$；
二次项归约为 $2\int(u-yp)r^2$；
四次项还使用
$\int y^2p^2r=-2\int yp^3/3$。
所有端项包含紧 $u$ 的 jets。没有要求(16)的原 primitive 左常数为零。

于是完整 local 项为
$$
\mathcal T_s(u;u,u)
=\frac{v}{32h^3}
\left[-F_{R,0}^y+h^2(F_{R,2}^y+F_{T,0}^y)-h^4F_{T,2}^y\right].
\tag{21}
$$
另一方面，原能量项准确是
$$
\mathcal E_s\{u,\mathsf A_{\rm sec}(u,u)\}
=-\frac{v}{32h^3}
\left[F_{R,0}^y+h^2(F_{R,2}^y+F_{T,0}^y)+h^4F_{T,2}^y\right].
\tag{22}
$$
两式相减得到全段恒等式
$$
\boxed{
\mathcal T_s(u;u,u)
-\mathcal E_s\{u,\mathsf A_{\rm sec}(u,u)\}
=\frac{v}{8h}\mathfrak m_y(u).
}
\tag{23}
$$
这里相消的是完整三次 pairing，不能把它引用成任意第四 forcing 或其它真实状态的零身份。

令
$$
c_i=a_i\cos\theta+b_i\sin\theta,\qquad
d_i=a_i^2-c_i^2,\qquad \zeta_i=a_i^2-3c_i^2 .
$$
R469 的母列为 $\mathcal B_\theta(u_i)=2\zeta_i\mathfrak C_i$。
把真实常历史 $\mathsf A_*$ 留在(14)的偶项，(23)准确给
$$
\boxed{
\beta_\theta^{H_s,\omega_s}(u_i)
=\frac{\zeta_i}{4}\mathfrak m_y(u_i).
}
\tag{24}
$$
特别它不含 $H_s$。位置改变只按
$$
\mathfrak m_y(u)=\mathfrak m_x(u)-\omega_s\mathfrak p(u)
\tag{25}
$$
作用；在当前偶母库中(3)使它也不含 $\omega_s$。

## 4. 平台列不为零，而且正好支付必需的额外项

记 $\mu_{i,j}^y=I_j^y(u_i,u_i)$。R469 的完整平台式为
$$
\mathcal B_\theta(\chi_i)
=-\frac{d_i}{2}\mathbf w_y'\cdot\mu_i^y
+2\mathbf w_y\cdot
\{-d_i\ell_{\mathsf A_s}(\mu_i^y)+c_i^2q_{\mathsf A_s}(\mu_i^y)\}.
\tag{26}
$$
其中
$$
\mathbf w_y=(1/(4h),0,h/4),\qquad
\mathbf w_y'=(-v/(4h),0,hv/4).
$$
原真实尾表给
$$
q_{R_y}=q_{T_y}=0,\quad
\ell_{R_y}=(0,0,2\mu_{i,0}),\quad
\ell_{T_y}=(0,0,2\mu_{i,2}^y).
$$
所以
$$
\ell_{\mathsf A_{\rm sec}}
=\left(0,0,-\frac{v\mu_{i,0}}{4h^2}
-\frac{v\mu_{i,2}^y}{4}\right).
$$
(26)中与 $\mu_{i,2}^y$ 相乘的两个奇项准确相消，两个 $\mu_{i,0}$ 项相加。保留 $\mathsf A_*$ 的偶项后得到
$$
\boxed{
\beta_\theta^{H_s,\omega_s}(\chi_i)=\frac{d_i\mu_{i,0}}4 .
}
\tag{27}
$$
$\mu_{i,2}^y$ 的原 $2p^2$ 贡献已在相消之前保全，不能以省略该项取得同一个结论。

R469 又给全部 gap 的 $\mathcal B$ 在整个路径为零。由(5)，任意
$$
\eta=\sum_i\lambda_i u_i+\sum_i\nu_i\chi_i+\eta_{\rm gap}
\quad\text{属于 }\ker L_f
$$
于是满足
$$
\boxed{
\beta_\theta^{H_s,\omega_s}(\eta)
=\frac18\sum_i\lambda_i\zeta_i
(F_{R,2}^y(u_i)+F_{T,0}^y(u_i))
+\frac14\sum_i\nu_i d_i\mu_{i,0}.
}
\tag{28}
$$
这一步已经覆盖完整 period 核，不只是母列的一个子空间。

## 5. 原四行的准确消元，保平台而不求新秩

以下 cubic 均回到保护芽的原 $x$ 坐标。R464(21)与 R327(11)给
$$
\begin{aligned}
J_{-4}(u)&=-K^2H_p\varepsilon F_{R,0}(u)/24,\\
J_{-3}(u)&=-\kappa KH_p\varepsilon F_{R,1}(u)/6
-K^2\varepsilon F_{R,0}(u)/192 .
\end{aligned}
\tag{29}
$$
还需一个原先未单列的系数。R326 的
$$
A_{-3}=-K\varepsilon H_pR/12,\quad
A_{-2}=K\varepsilon R/48,\quad
A_{-1}=H_paR+\varepsilon H_pT/4
$$
代入 R327(11)，先得到
$$
\begin{aligned}
J_{-2}
={}&\frac{K\varepsilon H_p}{16}(F_{R,2}-F_{S,2})
-\frac{KH_pa}{4}F_{R,0}
-\frac{K\varepsilon H_p}{16}F_{T,0}\\
&+\frac{\kappa K\varepsilon}{96}F_{R,1}
+\frac{K\varepsilon H_p}{48}F_{R,2}.
\end{aligned}
$$
用(17)中的完整 $F_{S,2}+F_{T,0}=0$，准确化为
$$
\boxed{
J_{-2}
=\frac{K\varepsilon H_p}{12}F_{R,2}
-\frac{KH_pa}{4}F_{R,0}
+\frac{\kappa K\varepsilon}{96}F_{R,1}.
}
\tag{30}
$$
母列是 $P_\ell(u_i)=\zeta_iJ_\ell(u_i)$、
$H_{B,0}(u_i)=-\zeta_iF_{B,0}(u_i)$。
由 R259 的 $L,U$ 原表，
$$
\boxed{
F_{B,0}=aF_{R,0}-3eF_{R,1}
-e\mathfrak p(u)+tF_{T,0}.
}
\tag{31}
$$
不先设偶性时，(31)的 $\mathfrak p$ 项不能删。

平台行则直接取 R464(28)—(29)的原完整值：
$$
P_{-4}(\chi_i)=P_{-3}(\chi_i)=H_{B,0}(\chi_i)=0,\qquad
P_{-2}(\chi_i)=\frac{K\varepsilon H_p}{6}d_i\mu_{i,0}.
\tag{32}
$$
所有 gap 对这些行也零。这里不需要 $M_3(u_i)\ne0$，不求任意 Vandermonde 逆，不执行旧九行的秩；只消费原四行本身。

对任意紧输入 $\eta$ 定义以下**原行的固定线性组合**：
$$
\begin{aligned}
\mathcal F_0(\eta)
&=-\frac{24}{K^2H_p\varepsilon}P_{-4,\theta}(\eta),\\
\mathcal F_1(\eta)
&=-\frac6{\kappa KH_p\varepsilon}P_{-3,\theta}(\eta)
-\frac K{32\kappa H_p}\mathcal F_0(\eta),\\
\mathcal F_2(\eta)
&=\frac{12}{K\varepsilon H_p}P_{-2,\theta}(\eta)
+\frac{3a}{\varepsilon}\mathcal F_0(\eta)
-\frac{\kappa}{8H_p}\mathcal F_1(\eta).
\end{aligned}
\tag{33}
$$
分母非零已由(6)保证。这三个记号不是新 profile 观察或新的可控状态。

在(5)的分解上，(29)—(32)逐项给
$$
\begin{aligned}
\mathcal F_0(\eta)&=\sum_i\lambda_i\zeta_iF_{R,0}(u_i),\\
\mathcal F_1(\eta)&=\sum_i\lambda_i\zeta_iF_{R,1}(u_i),\\
\mathcal F_2(\eta)&=\sum_i\lambda_i\zeta_iF_{R,2}(u_i)
+2\sum_i\nu_i d_i\mu_{i,0}.
\end{aligned}
\tag{34}
$$
最后一式的第二项是平台的真实贡献；若把平台当作 gap，下一定理会少掉整个(27)。

定义
$$
\boxed{
\ell_\theta(\eta)=\frac18
\left[
\mathcal F_2(\eta)+
\frac{-H_{B,0,\theta}(\eta)-a\mathcal F_0(\eta)
+3e\mathcal F_1(\eta)}{t}
\right].
}
\tag{35}
$$
这是原十三行中四行的显示线性组合。

## 6. 完整 period 核上的行关系与准确适用边界

将(31)(34)代入(35)，再与(25)(28)比较，得到更一般的身份
$$
\boxed{
\beta_\theta^{H_s,\omega_s}(\eta)-\ell_\theta(\eta)
=\left(\frac e{8t}-\frac{\omega_s}{4}\right)
\sum_i\lambda_i\zeta_i\mathfrak p(u_i),
\qquad \eta\in\ker L_f .
}
\tag{36}
$$
它同时核清了偶母条件、位置平移和平台项各自用在哪里。

**定理 1。** 对当前(3)的真实库，
$$
\boxed{
\beta_\theta^{H_s,\omega_s}|_{\ker L_f}
=\ell_\theta|_{\ker L_f}.
}
\tag{37}
$$
因而对任一允许的同十三规范变化(9)，
$$
\boxed{\beta_\theta^{H_s,\omega_s}(\eta_\theta)=0.}
\tag{38}
$$
结论对每一个实际相位成立，对所有正 $H_s$、所有允许的常 $\omega_s$ 成立。

证明已由完整两类列及 gap 给出，没有从一个矩阵维数猜满核。它不需要新几何、另一个特殊母、局部多项式近似或有限点采样。

尤其，R488(44)中的第一条
$$
b_\theta+\beta_\theta^{H_s,\omega_s}(\eta_\theta)=0
$$
在当前原核上准确退化为
$$
\boxed{b_\theta=0.}
\tag{39}
$$
这是固定当前真实路径及 profile 后的必要兼容。若有某个真实相位的原 $b_\theta\ne0$，则全部母/平台数目、gap 函数和第三零矩规范都不能在保持原 period 与保护芽的同时修复这一段。它不宣称当前尚未评价的 $b_\theta$ 非零，也不宣称改变真实路径后仍不可能。

式(37)只在完整 period 核上成立。对任意紧 particular $k$，仍必须使用(15)；不能把(35)直接替代 $\beta(k)$。本稿没有从对角 cubic 身份推出任意三槽对称性。

## 7. 真正的 source 商，而非另选一个规范的自由数

对固定相位和固定 secant 参数，定义
$$
\mathfrak b_{\theta;H_s,\omega_s}(G)
=(\beta_\theta^{H_s,\omega_s}-\ell_\theta)(k),
\qquad L_fk=G,\quad k\in C_c^\infty(I).
\tag{40}
$$
定义域是原 $L_f$ 的**真实同 collar 紧像**。由(37)，两个真逆之差属于整个(5)，故右侧准确相同。于是(40)是 well-defined 的线性 source 泛函。

这里没有宣称所有形式 source 都在像内，也没有假设退化微分算子存在一个无穷维连续右逆。若只使用一个已经证实位于像内的有限 source 空间，可以对一组基各取一次真实紧逆，再线性延拓；不同选择给同一个(40)。R327 的两条真实 particular 正提供当前相位族所需的最小入口。所有内部 $A_f$ 点、simple-$p$ 点、原左尾与平端条件先由真 range 支付，不能用(40)绕过它们。

现在令保护芽中心的真实 incoming 算子为 $\mathsf A_p$。原规范写成
$$
w_\theta=-\mathsf A_pD_\theta+k_\theta,\qquad
L_fk_\theta=G_\theta^c,\qquad
\mathcal A_\theta(k_\theta)=0.
\tag{41}
$$
其中
$$
G_\theta^c=-V_\theta^c/(2\tau)
$$
保原全 period、实际总成本及中心修正；没有重新施加或丢掉 $-1/(2\tau)$。

对一条实际含中心的正割段，记其真实中心算子为 $\mathsf A_s^*$。相对该中心，第二规范的完整输入是
$$
q_\theta^*=w_\theta+\mathsf A_s^*D_\theta
=k_\theta+(\mathsf A_s^*-\mathsf A_p)D_\theta .
\tag{42}
$$
$D_\theta$ 的三个真矩均零，因此 E8 作用后的这一项真紧；其实际前缀值没有被重置。

R488(24)—(27)证明，在中心清理 $q^*=0$ 时，原完整二/三阶场的奇系数为零，且此结论保任意第三 incoming。改变到(42)后，完整二阶平方及第三矩项在本 patch 都偶，所以当前完整奇系数准确为
$$
b_\theta^{\rm sec}
=\beta_\theta^{H_s,\omega_s}(q_\theta^*).
\tag{43}
$$
用(35)(40)(41)得到本稿的真实路径条件：
$$
\boxed{
b_\theta^{\rm sec}
=
\mathfrak b_{\theta;H_s,\omega_s}(G_\theta^c)
+\beta_\theta^{H_s,\omega_s}
\bigl((\mathsf A_s^*-\mathsf A_p)D_\theta\bigr).
}
\tag{44}
$$
两项都由同一个真实对象确定。第一项是全 period source 的商读出；第二项是原最终词在两个中心之间的真实二阶积分
$$
\mathsf A_s^*-\mathsf A_p
=\Phi_{\int_{s_p^*}^{s_s^*}M_{\rm raw}(s)\,ds}.
\tag{45}
$$
它不是“原总 $M=0$”能单独支付的量。

不含中心的正割子段仍有定理1与固定 residual(39)。式(44)在本稿按实际含中心的情形使用；没有为了取一个方便中心而插入新段、倒行、删桥或改变原 incoming。

## 8. 多个真实段及一个有限而非逐相位重求的接口

若同一真实路径中有有限多条正割段，(37)表明，在只保持 period 的情况下，所有段的奇系数对同一个 $\eta$ 的变化都是同一个数 $\ell_\theta(\eta)$。所以它们任意两者的差，已经不受 period 齐次选择影响。再保原十三门后，$\ell_\theta(\eta)=0$，每条段的奇系数都分别锁定。

这不是分别选择多个 $\chi$ 能修复的现象。原第三贡献、第二规范平方和交叉在每一条正割段均属于其 even 三权空间；R469 的共同第三矩仍只有一套。

对含中心的这些段，(44)还给一个准确的有限输入格式。按 R327 取两条已有的真紧逆
$$
L_fk_d=G_d^c,\qquad L_fk_e=G_e^c,\qquad
k_\theta^0=\sin^2\theta\,k_d+
2\sin\theta\cos\theta\,k_e .
\tag{46}
$$
不要求这个 particular 自己已经满足十三行。式(40)允许用(46)评价商项；不能把(46)直接冒作最终规范。

$\beta_\theta$ 和 $\ell_\theta$ 的系数是 $\sin\theta,\cos\theta$ 的次数至多二多项式，源及(42)的前缀项也至多二次。利用 $\sin^2\theta+\cos^2\theta=1$ 统一齐次度，并保源在 $0,\pi$ 为零，(44)可准确写成
$$
b_\theta^{\rm sec}
=b_{31}\cos^3\theta\sin\theta
+b_{22}\cos^2\theta\sin^2\theta
+b_{13}\cos\theta\sin^3\theta
+b_{04}\sin^4\theta .
\tag{47}
$$
这是四个真实生成系数，不宣称它们独立，也没有执行 Fourier 采样。系数可由原两条真逆、完整(15)(35)与(45)按多项式展开定义。它们保 true range、原尾与全部前缀，并不要求重求每个相位的退化逆。

因此 $m$ 条实际含中心的正割段给至多 $4m$ 个这样的固定兼容系数。可重复的只是有限代数定义，不是把任何一个已付科学输出重新执行。本稿没有把这些系数一律称为 C² 母观察，更没有宣称旧二十目标、924 个全 $W$ 外矩或旧 signed 成本像已经支付它们。

若要用实际成本/路径来控制(47)，必须对同一个最终词同步保持 period range、$\tau$、保护芽、允许前缀及所有新桥的完整 $V$ 与 ruling。先单独选择一个规范使(47)为零，再另作矩阵/第三复位，不会自动保住这些数。

## 9. 对真实连接构造的后果与尚未支付的部分

本稿给出的推进是具体的：

- R488 的 secant 奇行在原全 period 核上的作用已完全算出，母列、平台列、gap 与平移范围均有准确原式。
- 在当前 even 母库，旧四行的(35)恰好就是它的全核限制；原十三行付完后不能再把该行列为新增 homogeneous 控制。
- 固定实际路径若违反(39)，则该路径在原允许规范内确实被排除；这不等于所有实际路径被排除。
- 真实待付数不是一个可自由指定的瞬时矩阵坐标，而是(44)的共同 source 商与真实相对前缀，最多可按(47)作有限完整记录。

两个 even 系数还须使用 R488(42)—(44)的原共同线性行。它们可能有额外关系；本稿既不把它们宣为满射，也不从奇行不可调推它们不可调。全局第三 Gram 的原作用只在未被其它段锁定时可独立使用，不能重复消费。

R488 还已证明，正割分支的原 $t_1$ 密度严格负，没有正长度 $M=0$ 返回块，并且不能沿同分支平接常 collar。因此，真实闭词所需的连接段仍不可删除。R472 的矩阵/第三前缀截面若用于构造这些连接，必须保其完整基准；本稿没有把连接段自动纳入正割三函数空间，也没有宣称其 ruling 已支付。

这给下一实际构造一个明确顺序：先在同一真实词与同一原 source 中支付(44)的固定奇系数，再研究两个 even 行与连接段全 ruling 的共同像。不能以更多母列、同 $w$ 的 gap 函数、原第三零矩变化或一个零总矩阵，替代这里已经锁定的真实兼容值。

## 10. 直接来源与独立核对范围

- [R221](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)：完整 local pairing 与二阶规范线性响应。
- [R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)：原 E8 对角、完整 cubic 及保尾 IBP。
- [R326](R326-one-global-second-gauge-pays-the-complete-rational-port-and-preserves-joint-cost.md) 与 [R327](R327-analytic-packet-period-kernels-and-a-finite-same-gauge-joint-system.md)：原十三行、真实 centered history、完整 period 核。
- [R455](R455-four-natural-moments-with-one-common-degenerate-pair-and-twenty-targets.md) 与 R480：当前从起点选取的 even 母类和共同复制。
- [R464](R464-nonzero-cubic-mothers-and-complete-nine-row-same-period-gauge-control.md)：原母前三行和全部平台尾表。
- [R467](R467-conditional-actual-highest-gauge-control-and-one-complete-thirteen-row-normalization.md)、[R469](R469-global-gauge-locking-and-real-prefix-obstructions-between-rational-germs.md)：同一真 range、保护规范、全路径母/平台响应及真实前缀范围。
- [R488](R488-real-secant-height-patches-and-complete-same-gauge-ruling.md)：实际正割族、完整仿射场、三个 ruling 系数与任意紧输入上的奇行定义。

全部新增推导都是上述原式的有限纸面相消。同行窄核只用于所列 cubic 相减与局部配对因子，不把它冒作全局几何或数值验证。
