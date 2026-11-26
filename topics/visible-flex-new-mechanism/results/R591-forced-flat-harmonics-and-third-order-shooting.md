# R591：实际二阶非均值修正、全平强迫解与三阶射击条件

日期：2026-11-26。**已证明下列准确强迫解、条件性核心匹配与有限阶射击接口**。本稿不是有限等距族存在定理。

使用 R576 的同一高度/turning 构造、R583 的准确无限端模及 R575 的径向均值通量。下面的 F 必须是一个**准确**全平且核心 trace 为零的场；某次浮点射击残差小并不自动满足该假设。

## 1. 对象、核心及线性算子

固定 $r_c<r<R$，$W>0$，$h'=-W$。近内端取同一 R583 温和振荡尾；近核心令
$W=B(R-r)^{-\alpha}$ 乘以有逐阶导数控制的余项，
$1/2<\alpha<1$。沿用 R576 的正则核心坐标和假设。
记

$$
E_0=1+W^2,\qquad
P_m q=(Wq')'-m^2W'q/r,\qquad L_m=rP_m.
\tag{1}
$$

设 $j=2$，$\mu=j^2=4$，$F$ 是准确非零解 $P_jF=0$，在帽端全平，$F(R)=0$。
用

$$
A=\frac{W(\mu F-rF')}{\mu-1},\qquad A'=WF'
\tag{2}
$$

归一 $A(R)=1$。这是允许的：若 $F(R)=A(R)=0$，正则核心二系统的唯一性会使 F 恒为零。

记 $\delta=R-r$。积分因子给准确公式

$$
F(r)=(\mu-1)r^\mu\int_r^R
       \frac{A(t)}{t^{\mu+1}W(t)}\,dt.
\tag{3}
$$

所以在足够靠近核心处 $F>0,F'<0$，并有

$$
F\sim\frac{\mu-1}{RB(1+\alpha)}\delta^{1+\alpha},
\qquad F'\sim-\frac{\mu-1}{RB}\delta^\alpha.
\tag{4}
$$

这些关系用于端口证明，不以有限差分观察替代准确导数余项。

## 2. 二阶完整展开：真正需要的是 2j 模强迫返回

取平均高度不变，

$$
Z=h+\epsilon F(r)\cos(j\theta)
       +\epsilon^2G(r)\cos(2j\theta),
\qquad E=E_0+\epsilon^2e_2+O(\epsilon^3).
\tag{5}
$$

R576 的准确 Darboux 分子为

$$
\mathcal D=
E\{Z_{rr}Z_{\theta\theta}
 -(Z_{r\theta}-Z_\theta/r)^2\}
+rZ_rZ_{rr}
-\frac{E'}2\{r+Z_rZ_{\theta\theta}-Z_\theta^2/r\}.
\tag{6}
$$

定义

$$
Q_c=(rF'-\mu E_0F)F''+\mu WW'FF',
\qquad
Q_s=-\mu E_0(F'-F/r)^2+\mu WW'F^2/r.
\tag{7}
$$

逐项收集 (6) 的二阶项，得到

$$
[\epsilon^2]\mathcal D=
\left(-L_{2j}G+\frac{Q_c-Q_s}{2}\right)\cos(2j\theta)
+\frac{Q_c+Q_s}{2}-\frac r2e_2'.
\tag{8}
$$

核对方法：$F''\cos j\theta$ 与 $-\mu F\cos j\theta$ 给 $-\mu F F''\cos^2j\theta$；
混合导数平方给 $-\mu(F'-F/r)^2\sin^2j\theta$；
$rZ_rZ_{rr}$ 给 $rF'F''\cos^2j\theta$；
最后一个括号给 (7) 的两个 $WW'$ 项。再用平方角公式即得 (8)，无三阶导数。

因此二阶任务准确分为

$$
\boxed{L_{2j}G=(Q_c-Q_s)/2,\qquad
 e_2'=(Q_c+Q_s)/r.}
\tag{9}
$$

turning 根本身的二阶均值展开给出更直接的代数式

$$
\boxed{e_2=
\frac{1+3W^2}{2}F'^2
-\frac{\mu(1+W^2)}rFF'
+\frac{\mu(1+W^2)}{2r^2}F^2.}
\tag{10}
$$

证明：$b=r-\epsilon^2\mu F^2\sin^2(j\theta)/(2r)+O(\epsilon^3)$，
$N=1+\epsilon\mu WF\cos(j\theta)/r
+\epsilon^2\{\mu F^2\sin^2(j\theta)/(2r^2)-\mu FF'\cos^2(j\theta)/r
+4\mu WG\cos(2j\theta)/r\}+O(\epsilon^3)$。
展开 $\langle N/\sqrt{E-r^2Z_r^2/b^2}\rangle=1$，其均值恰给 (10)。
直接微分 (10)，再用 $L_jF=0$，得到 (9) 的均值等式。

(10) 也就是 R575 的 $e_2=2J_0$：代入 (2) 到该条
$Q=(\mu-1)^2A^2/\mu+\mu F^2$ 和
$J_0=(-Q/(4r))'+((1+1/\mu)A'^2+F'^2)/4$，收集 $F'^2,FF'/r,F^2/r^2$ 即得。
因此均值设计不会免除 (9) 的真实四阶角模返回。

## 3. 此强迫确有全平内尾解，不只是形式方程

以下引理支付 (9) 的内尾存在性，后面三阶源也适用。

**引理。** 固定目标 $m\in\{2,4,6,8\}$。若 S 在共同温和尾上光滑，且每个固定阶 u 导数均满足
$|\partial_u^kS|\le C_k e^{-u^2/12}$，
则 $L_mG=S$ 在某个完整内尾上有真实光滑全平解。任意两个全平解之差是该 m 模的准确齐次全平核倍数。

**证明。** 置 $\nu=m^2,G=r^\nu y$，$r_u=-\ell/u^2$。不是只作渐近替换，而是准确变换为

$$
(py_u)'+\varepsilon py
=|r_u|r^{\nu-1}S=:H,
\quad
p=W r^{2\nu}/|r_u|,\quad
\varepsilon=\nu(\nu-1)|r_u|^2/r^2.
\tag{11}
$$

取 R583 的真实峰 $\alpha_n$，从足够大的固定 N 开始；可以先取 $\alpha_N\ge1000$，再为下面的渐近界向后有限移动。
R583 的比值界给 $k_{n-1}/V_n,k_n/V_n\le e^{-\alpha_n}$。例如
$2\cdot1024e^{42}a^4e^{-3a/2}\le e^{-a}$ 在 $a\ge1000$ 成立。

每 cell 的准确含势 Dirichlet 问题仍可逆。它的两个端值插值 $H_L,H_R$ 由正 Green 控制满足绝对值至多2。
零端值的强迫解所产生的端点外通量恰为
$\int H_LH$、$\int H_RH$；这是对准确方程作 Lagrange 恒等式，而不是假定强迫符号。
故每个通量绝对值至多 $14\sup|H|$。
R583 的 $V_n$ 下界只损失一个 $e^{C\alpha_n}$ 和多项式因子，所以节点匹配写成

$$
y_n=-\frac{k_{n-1}}{V_n}y_{n-1}
    -\frac{k_n}{V_n}y_{n+1}+g_n,
\qquad |g_n|\le C e^{-\alpha_n^2/13}.
\tag{12}
$$

这里 1/13 是从 1/12 吸收线性指数损失后的严格余量。固定 $y_N=0$。
在序列范数 $\sup_{n>N}e^{\alpha_n^2/40}|y_n|$ 上，前一邻点项的算子范数至多
$\exp[-\alpha_n+14\alpha_n/40]$，后一项至多 $e^{-\alpha_n}$；
因为 $6<\alpha_n-\alpha_{n-1}<7$。
总和小于1/2。于是 (12) 是真正的收缩映射，给唯一衰减节点解。

每 cell 内重建准确 ODE 解，(12) 保证通量连续。零端强迫解的 Green 范数至多
$49/(2(1-.001))$ 乘以 $\|H/p\|_\infty$；$1/p$ 只增加线性指数和多项式。
齐次插值由节点控制。各固定阶导数再由 ODE 递推，最多损失 $e^{C_k u}$ 和多项式，因而可分别界为 $C_k e^{-u^2/41}$，全部径向导数仍全平。
两全平解之差为齐次解；其与 R583 核的 $W$-Wronskian 在平端为零，故差是核倍数。证毕。

为何 (9) 满足引理：R583 的节点链在足够大 u 后有 $|\rho_n|\le e^{-\alpha_n}$，从而
$|F^{(k)}|\le C_k e^{-u^2/15}$；这里利用
$\alpha_n^2-\alpha_N^2\le14\sum_{\ell=N+1}^n\alpha_\ell$，并吸收每 cell 的线性指数损失。
(7) 是两个 F jets 的乘积，W 及其导数只带线性指数/多项式，故 S 的各固定阶导数满足引理。
这是准确强迫的全平解，不是数值口内置零。该构造暂未给可用于宏观估计的良好算子常数。

## 4. 真实核心匹配及明确尚需检查的分母

把第3节的某个全平特解向外延伸。因为 W 在开区间严格为正，普通 ODE 唯一性适用。
对一般强迫定义
$A_m=W(m^2G-rG')/(m^2-1)$，则

$$
G'=\frac{m^2}rG-\frac{m^2-1}{rW}A_m,\qquad
A_m'=WG'-\frac{S}{m^2-1}.
\tag{13}
$$

(7) 在核心有界：由 (4) 可逐项看到 $W^2F F''$、$WW'FF'$ 和 $W^2F'^2$ 有有限极限，
$rF'F''=O(\delta^{2\alpha-1})$ 趋零，其余项更小。
因此 S 连续到核心。R576 正则 x 坐标中 (13) 的系数与强迫连续，故 G 和 A_m 有有限核心 trace。

令 $\phi_m$ 是任意非零准确全平齐次 m 模。若

$$
\phi_m(R)\ne0,
\tag{14}
$$

则 $G=G_p-G_p(R)\phi_m/\phi_m(R)$ 是唯一核心 trace 为零的全平解。
(14) 必须另付；已有浮点 $C/A$ 数值不能把它升级为准确非零证明。

该 G 由积分因子满足 $G=O(\delta^{1+\alpha})$，
$WG'=-(m^2-1)A_m/r+m^2WG/r$ 连续，而且微分后一阶仍连续；用 (13) 及 S 连续即可核对。
所以它满足 R576 要求的 $P_c=WG'$ 的 C¹ 核心端口，不仅是 G(R)=0。

还可在非共振情形写真实 Green 表达式：取右端齐次解 $\psi_m(R)=0,A_{\psi_m}(R)=1$，
$\Omega=W(\phi_m\psi_m'-\phi_m'\psi_m)=-(m^2-1)\phi_m(R)/R$。
写已经构成的准确解为 $G=a(r)\phi_m+b(r)\psi_m$ 并取通常的变参数规范。则
$b'=\phi_mS/(r\Omega)$、$a'=-\psi_mS/(r\Omega)$。
两全平函数的 Wronskian 在帽端为零，故 $b(r)=\int_{r_c}^r\phi_mS/(t\Omega)\,dt$；
核心 $G(R)=0,\phi_m(R)\ne0$ 给 $a(R)=0$。由此准确得到

$$
G(r)=\frac{\psi_m(r)}{\Omega}
  \int_{r_c}^{r}\phi_m(t)\frac{S(t)}t\,dt
+\frac{\phi_m(r)}{\Omega}
  \int_r^R\psi_m(t)\frac{S(t)}t\,dt,
\tag{15}
$$

但在尚未独立控制右端解向内的增长前，不把 (15) 的两个积分分开当作数值稳定算法；第3节的 cell 强迫/匹配构造才是已付存在证明。实际程序也不能用巨大两项相消代替误差界。

## 5. 三阶基频射击可以用明确的紧支撑均值控制

选定非负、非零、C∞ 的 B_control，紧支撑于足够靠近核心且与核心端点分离的开环。
令 $W_t=W+tB_\mathrm{control}$，t 足够小保持正值、帽尾和核心端口。
对相同帽端归一的齐次 j 模，核心 shooting 比 $c(t)=C_t/A_t$ 的导数满足

$$
c'(0)=-\frac{R}{\mu-1}D,\qquad
D=\int B_\mathrm{control}
\left[-F'^2+\frac{2\mu}rFF'-\frac{\mu}{r^2}F^2\right]dr.
\tag{16}
$$

证明：$\dot P_jF=(B_\mathrm{control}F')'-\mu B_\mathrm{control}'F/r$。
分部积分给 $\int F\dot P_jF=D$。
$P_j\dot F=-\dot P_jF$ 的 Wronskian 边界项在帽端为零，在核心为
$(\mu-1)\dot C/R$；当前 C=0、A=1，故 $\dot c=\dot C$，得到 (16)。

由 (3)(4)，此支撑内 $F>0,F'<0$，所以方括号严格负，D<0。
因此 **存在一个完全明确选择方式的紧支撑均值控制，其核心射击横截性严格非零**。
这里不声称原数值 gain bump 自动有同样符号，也不把改变 W 的设计过程叫同 g 弯曲。

现假定第4节已得到准确 G。令

$$
U=F'-F/r,\quad V=G'-G/r,
$$
$$
K_c=r(F'G''+G'F'')-\mu E_0(4GF''+FG'')
        +\mu WW'(4GF'+FG'),
$$
$$
K_s=-4\mu E_0UV+4\mu WW'FG/r,
$$
$$
N_j=(K_c+K_s)/2+\mu F(e_2W'-We_2'/2),
\qquad N_{3j}=(K_c-K_s)/2.
\tag{17}
$$

这是 (6) 的三阶展开：交叉的 $\cos j\theta\cos2j\theta$ 与
$\sin j\theta\sin2j\theta$ 分别给 K_c、K_s；e2 只与一阶角模相乘，给 (17) 的末项。
对称性使 turning 根的三阶纯径向项为零。

设 $t=\epsilon^2t_2$，再加入
$\epsilon^3\{K(r)\cos j\theta+H(r)\cos3j\theta\}$。
三阶方程准确为

$$
P_jK=N_j/r-t_2\dot P_jF,\qquad
P_{3j}H=N_{3j}/r.
\tag{18}
$$

基频的核心可解条件是 $\int F(N_j/r-t_2\dot P_jF)=0$，由 (16) 严格解出

$$
\boxed{t_2=\frac{\int F N_j/r}{D}.}
\tag{19}
$$

全平特解由第3节构造；用 F 的 Wronskian 恒等式，(19) 使其核心 C trace 恰为零。
再加一个 F 倍数即可令 K 的核心 A trace 为零，从而固定一阶幅度的归一。
3j=6 模若满足对应的 (14)，也按第4节唯一匹配。
这些源在帽端是快速高斯衰减的乘积：$1/15+1/41>1/12$，所以含 F 与 G 的交叉项仍满足第3节的明确指数；含 e2 的项更快。核心连续，所有积分均为准确有限量。

## 6. 对下一真实输入的作用与界限

本稿支付了以下具体接口：二阶 j4 源 (7)(9)、不经均值数值积分的 e2 (10)、该强迫的真实无限全平端解、非共振时完整核心返回、可严格选出的射击横截控制，以及三阶基频/六阶角模源与幅度条件 (17)–(19)。

这给后继高度求解可直接加入的准确二阶/三阶校正方向。它仍只有有限阶消残差，未证明任意非零 epsilon 的完整 Darboux 残差恰为零。
目前数值输入的准确背景共振、m=4/6 的核心非共振分母及数值 ODE 误差也没有由本稿自动认证。
完整有限分支还需要全角频率逆与余项控制，或另一份真正收敛/可验证的非线性解。所有宏观握持与全局 reach 仍另行支付。

