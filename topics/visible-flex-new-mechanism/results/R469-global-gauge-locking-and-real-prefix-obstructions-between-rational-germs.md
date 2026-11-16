# R469：同一规范的全段锁定、真实两类核列与多端芽的二阶前缀障碍

日期：2026-11-16。**完整原式纸面证明；没有执行符号程序、profile 积分、原根恢复、数值秩、人工检查或新的科学计算。**

本文接续 [R467](R467-conditional-actual-highest-gauge-control-and-one-complete-thirteen-row-normalization.md) 与已发表的 [R468](R468-real-height-pulse-fills-affine-residual-and-completes-actual-enhanced-cost-control.md)。后者在同一完整 $J_{\rm aff}$ 和同一实际母库上，把实际成本截面的条件降为共同关系 $\mathfrak h\in\operatorname{span}(\mathfrak y)$；它没有支付闭路径上其它 $s$ 段的第四 ruling。本文不以四个完整 self 的部分结论代替尚须满足的共同关系。

新增结论有三项。

1. 一旦 R467 的指定有理端芽已付，第三齐次规范的三个 ruling 矩就被该端芽**唯一锁定**。在其它段上不能再选一个独立的三维修正。剩余问题可准确投影为一个全局线性问题，完整平方、交叉和真实历史均保留。
2. 对当前不交 rank-one 包圆，周期齐次核中全部间隙函数对这个**全路径**问题不可见。其余作用恰由每包母函数和真实平台两列给出；本文给两列在任意真实 $h,k,\omega$ 上的完整式，尤其平台列的 local 项是 $-\tfrac12d_i\,\mathbf w'\cdot\mu_i$，不是零。
3. 若同一物理坐标中存在两个 $\omega=0$ 的真实有理端芽，则最高奇行之差完全消去共同二阶规范：
$$
\frac{24}{\kappa_b}P^{(b)}_{2,\theta}
-\frac{24}{\kappa_a}P^{(a)}_{2,\theta}
=\ell_f\!\left((X_b-X_a)D_\theta\right).
$$
在当前库上，这准确等于
$\sin^2\theta\,d_f(X_b-X_a)$。因而所有这些端芽同时可解，必须支付实际二阶前缀的相对读出；只有全周期 $M=0$ 或一个全成本最高标量并不支付它。

这里没有声称当前实际路径已违反该新必要门，也没有把多个有理端芽假设强加给任意路径。一般其它 $s$ 段仍由第 7 节的同一全局算子处理。

## 1. 固定同一实际对象

沿用 R467 的一条真实闭几何、同一个目标、共同物理区间 $I=[\ell,r]$、双零 collar、原右积分与整个路径的起点。设
$$
M=0,\qquad \mathbf T=\tau\mathfrak H,\qquad \tau\ne0,
\tag{1}
$$
并令
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta
=\sin^2\theta\,\Delta-2\sin\theta\cos\theta(f\odot g),
\quad \Delta=f\odot f-g\odot g .
\tag{2}
$$
整个二、三阶 range、原三矩圆和 R467 所用的完整成本条件均按其原范围保留。

全部最细实际包写为
$$
f=\sum_{i=1}^n a_i u_i,\qquad
g=\sum_{i=1}^n b_i u_i,\qquad a_i\ne0 .
\tag{3}
$$
包络严格不交且有正间隙。每包的 $f'$ 只有有限阶零，$A_f=6f'f'''-2(f'')^2$ 没有开零集；R455/R460 的有限简单内部点库满足这个已经使用的核分类条件。多峰、多 simple-$p$ 点不新增每包核常数。

使用一组已经由 R467 选出的完整二阶、三阶规范
$(\bar w_\theta,\bar\chi_\theta)$。它们沿整条路径使用，随相位光滑、周期，在 $\theta=0,\pi$ 为零。已经有：

- 同一个第四 period 恒零；
- 三条真实合法性矩为零；
- 指定有理端芽 $U_*$ 的全部十个端口系数以及三个真实初值均已付。

把其余完整第四 ruling 记为
$$
\mathscr R_\theta(s).
\tag{4}
$$
因此 $\mathscr R_\theta|_{U_*}=0$，但尚不设它在其它段为零。它包含原 canonical 第三场的全部局部项、二/三阶入历史、R467 的实际原型、桥、复制与 Klein 基准。

后续改变只写成
$$
w_\theta=\bar w_\theta+\eta_\theta,\qquad
\chi_\theta=\bar\chi_\theta+\zeta_\theta .
\tag{5}
$$
不在其它端口重置 $w$、$\chi$、右锚或累计历史。

## 2. 从完整平方式看第三规范为什么被锁定

记原三个配对
$$
\mathbf I(a,b)=
\left(\int a''b'',\ \int xa''b'',\
\int(x^2a''b''+2a'b')\right),
\tag{6}
$$
以及全部真实几何上的
$$
d=h\omega-k,\qquad
\mathbf w(s)=
\left(\frac{1+d^2}{4h},\frac d2,\frac h4\right).
\tag{7}
$$
两处 $w$ 记号不同：$\mathbf w$ 是三维几何权，$w_\theta$ 是二阶 profile 规范。

[R184](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md) 的完整公式是
$$
\widetilde{\mathscr K}_\theta
=\mathscr K^0_\theta+\mathcal B_\theta(w_\theta)
-\mathbf w\cdot\mathbf I(w_\theta,w_\theta)
-2\mathbf w\cdot\mathbf I(\phi_\theta,\chi_\theta).
\tag{8}
$$
$\mathcal B_\theta$ 是原完整线性响应，不是把 (8) 只留一阶后的近似。于是 (5) 的准确增量为
$$
\delta\mathscr K_\theta
=\mathcal B_\theta(\eta_\theta)
-\mathbf w\cdot
\left\{
2\mathbf I(\bar w_\theta,\eta_\theta)
+\mathbf I(\eta_\theta,\eta_\theta)
+2\mathbf I(\phi_\theta,\zeta_\theta)
\right\}.
\tag{9}
$$

在 $U_*$ 上，
$$
h=H(1+\varepsilon\sigma^2),\quad
k=\kappa\ne0,\quad\omega=0,\qquad H,\varepsilon>0.
\tag{10}
$$
原三权张成 $\operatorname{span}\{h^{-1},1,h\}$，在任何非空端芽开区间独立。故选择三个具有不同 $h$ 值的真实点 $s_1,s_2,s_3\in U_*$ 后，
$$
W_*=(\mathbf w_j(s_i))_{1\le i\le3,\ 0\le j\le2}
\tag{11}
$$
可逆。对任意光滑 $s$ 函数 $A$ 定义固定的线性抽取及归一化
$$
\nu_*(A)=W_*^{-1}(A(s_1),A(s_2),A(s_3))^T,\qquad
\mathcal P_*A=A-\mathbf w\cdot\nu_*(A).
\tag{12}
$$
取点只定义一个真实有限线性算子；没有执行采样，也不以这三个值代替全端芽恒等。关键恒等是
$$
\nu_*(\mathbf w\cdot v)=v,\qquad
\mathcal P_*(\mathbf w\cdot v)=0
\quad(v\in\mathbb R^3).
\tag{13}
$$

若一个允许的 $\eta_\theta$ 已保持原十个端口系数，那么
$\mathcal B_\theta(\eta_\theta)|_{U_*}\in\mathbf w|_{U_*}\cdot\mathbb R^3$。
为继续保持完整端芽为零，(9) **迫使**
$$
\boxed{
\mathbf I(\phi_\theta,\zeta_\theta)
=\frac12\nu_*\!\bigl(\mathcal B_\theta(\eta_\theta)\bigr)
-\mathbf I(\bar w_\theta,\eta_\theta)
-\frac12\mathbf I(\eta_\theta,\eta_\theta).
}
\tag{14}
$$
这个三向量唯一。R47/R326 的原三矩 Gram 右逆提供同 collar 的真实
$\zeta_\theta$；其矩以外的核对整条路径的 ruling 均没有作用。

因此代入 (14) 后，在**整个**闭路径准确有
$$
\boxed{\delta\mathscr K_\theta
=\mathcal P_*\mathcal B_\theta(\eta_\theta).}
\tag{15}
$$
这一步不是删掉平方项：它们逐项进入 (14)，然后由同一个全局第三规范支付。第三规范不改变整个第四 period，因为 $M=0$。

若 $\eta_\theta$ 光滑、周期并保种子，则 (14) 也如此，原 Gram 右逆可同步选择。不能为了另一个 $s$ 段再改变这个三向量而仍声称保留 $U_*$。

## 3. 真正剩余的周期核和十三门

保持已经为零的完整 period 要求
$$
L_f\eta_\theta=0,\qquad L_f\eta=\mathfrak H(\eta;f,f).
\tag{16}
$$
保持第三合法性和指定端芽商要求原 R326/R327 的十三行
$$
\mathcal A_\theta(\eta_\theta)
=
\left(
\mathbf I(\phi_\theta,\eta_\theta),\
(P_{\ell,\theta}(\eta_\theta))_{-4\le\ell\le2},\
(H_{B,j,\theta}(\eta_\theta))_{0\le j\le2}
\right)=0.
\tag{17}
$$
这些是原行，不另换一套方便的条件；$P_2$ 在完整 period 核上为零的身份也保留，不把十三称作秩。

[R327](R327-analytic-packet-period-kernels-and-a-finite-same-gauge-joint-system.md) 的原核分类给
$$
\ker L_f
=\operatorname{span}\{u_i,\chi_i:1\le i\le n\}
\oplus\mathscr G,
\tag{18}
$$
其中 $\chi_i$ 在第 $i$ 包邻域恒为1、在其他包邻域恒为0，只在真实间隙过渡；
$\mathscr G$ 是在所有活动包上恒零的同 collar 光滑函数。平台 $\chi_i$ 并非间隙函数。

分类保留整个右锚和左仿射尾。特别，不能对每个内部 $p=0$ 子区间另给一套常数，也不能把每个包端的平台值重新清零。

## 4. 全部间隙函数对全路径 ruling 都不可见

本节把 R327 的指定端口结论推进到任意真实几何段；不要求该段是偶 germ、有理 germ 或常态。

保原全路径累计
$$
\mathsf m(s)=\int_{s_0}^{s}M_{\rm raw}(t)\,dt,\qquad
\mathsf A_s=\Phi_{\mathsf m(s)}.
\tag{19}
$$
[R221](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md) 的完整原式是
$$
\begin{aligned}
\mathcal B_\theta(\eta)
={}&2\mathcal T_s(\eta;D_\theta)
-4\mathcal T_s(\phi_\theta;\phi_\theta,\eta)\\
&-2\mathcal E_s(\mathsf A_sD_\theta,\eta)
+4\mathcal E_s\{\phi_\theta,\mathsf A_s(\phi_\theta,\eta)\},
\end{aligned}
\tag{20}
$$
其中
$\mathcal E_s(a,b)=\mathbf w(s)\cdot\mathbf I(a,b)$。

**命题 1。** 对当前 (3) 的真实圆，
$$
\boxed{\mathcal B_\theta(\eta)(s)=0
\quad(\eta\in\mathscr G,\ \text{所有 }s,\theta).}
\tag{21}
$$

**证明。** 原 $\mathcal T_s$ 已由 R221 的真实右尾转置写成局部三槽积分。两个 inner 的全部密度在活动包中；$\eta$ 及其 jets 在那里为零。所以两项 $\mathcal T_s$ 均为零。原 E8 六项式又逐项给
$\mathsf A_s(\phi_\theta,\eta)=0$。

在每个间隙上，$\mathsf A_sD_\theta$ 是由右方实际包产生的一个确定二次多项式 $q$，它通常不为零。$\eta$ 按有限个间隙分开后每一项都在间隙两端平紧。原配对保
$$
I_0(\eta,q)=I_1(\eta,q)=I_2(\eta,q)=0.
\tag{22}
$$
当 $q=Ax^2+Bx+C$ 时，$I_2$ 中两个非零积分分别为
$4A\int\eta$ 和 $-4A\int\eta$。故 (20) 的余项也零。证毕。

因此 (18) 中的无限维间隙自由度既不改变十三门，也不改变 (15) 的全路径响应。它造成的完整平方和交叉仍按 (14)进入第三矩，但没有独立的全段控制作用。

这个结论使用当前 $f,g$ 在同一包间隙上同时为零；不将它外推到一般 R221 中可能在 $f$ 常值段上仍有非零 $g$ 的圆。

## 5. 母函数列在任意真实段上的完整式

令
$$
c_i(\theta)=a_i\cos\theta+b_i\sin\theta,\qquad
d_i(\theta)=a_i^2-c_i(\theta)^2,\qquad
\mu_i=\mathbf I(u_i,u_i).
\tag{23}
$$
所有位置、宽度、幅度和最终母形都取当前实际值。

定义
$$
\mathfrak C_i(s)=
\mathcal T_s(u_i;u_i,u_i)
-\mathcal E_s\{u_i,\mathsf A_s(u_i,u_i)\}.
\tag{24}
$$
则从 (20)准确有
$$
\boxed{
\mathcal B_\theta(u_i)(s)
=2\{a_i^2-3c_i(\theta)^2\}\mathfrak C_i(s).
}
\tag{25}
$$

local 两项的系数分别是 $d_i$ 与 $c_i^2$。history 项中，其他包的输出在 $u_i$ 上要么为右零，要么为真实二次多项式尾；它与紧 $u_i$ 的三个配对由 (22)为零。故没有删单包尾，而是先保尾再完成配对，得到系数 $d_i-2c_i^2=a_i^2-3c_i^2$。

式 (24)的所有 $s$ 依赖都是显式的。为固定 local 规范，设
$$
e=hx+d,\quad Q=1+e^2,\quad
\gamma=h_s,\quad\delta=d_s,\quad e_s=\gamma x+\delta,
\quad F_c=Qc''-2hec'+2h^2c.
$$
R221 原三线性式为
$$
\begin{aligned}
\mathcal T_s(c;a,b)=\frac1{32h^4}\int_I\Big[
&Q^2c'''\{\gamma(a'b''+a''b')-e_sa''b''\}\\
&-2h\gamma eQ\,c'''a'b'\\
&+F_c\{(\gamma Q-2hee_s)a''b''-2h^2\gamma a'b'\}
\Big]\,dx .
\end{aligned}
\tag{26}
$$
特别，(25)保真实 $\mathsf A_s$ 的全部八维入历史，不把它换成各段自己的零初值。

## 6. 平台列的导数项与真实尾表

对任一原 E8 方向 $X$，记
$$
\operatorname{tail}_X(\mu)=A_Xx^2+B_Xx+C_X,\qquad
\ell_X(\mu)=(0,-2A_X,2B_X),\qquad
q_X(\mu)=2\mathbf I\{u,X(u,1)\}.
\tag{27}
$$
后一式只依赖 $\mu=\mathbf I(u,u)$。沿用 R259 的记号
$P=r_0,R=r_1,S=s_0,L=p_0,U=s_1,V=p_1,T=t_1,Y=p_2$，原表为：

| $X$ | $\ell_X(\mu)$ | $q_X(\mu)$ |
|---|---|---|
| $P$ | $(0,0,0)$ | $(0,0,0)$ |
| $R$ | $(0,0,2\mu_0)$ | $(0,0,0)$ |
| $S$ | $(0,0,0)$ | $(0,0,0)$ |
| $L$ | $(0,\mu_0/2,0)$ | $(0,-\mu_0/2,-\mu_1)$ |
| $U$ | $(0,0,2\mu_1)$ | $(0,0,0)$ |
| $V$ | $(0,\mu_1/2,0)$ | $(\mu_0/2,0,-\mu_2/2)$ |
| $T$ | $(0,0,2\mu_2)$ | $(0,0,0)$ |
| $Y$ | $(0,\mu_2/2,0)$ | $(\mu_1,\mu_2/2,0)$ |

这里 $V=p_1$、$Y=p_2$，不沿用 R326 某处把 $p_2$ 临时记为 $V$ 的局部别名。对 $\mathsf A_s$ 的 $\ell,q$ 按真实八系数线性组合。

**命题 2。** 全路径的平台列准确为
$$
\boxed{
\begin{aligned}
\mathcal B_\theta(\chi_i)(s)
={}&-\frac{d_i(\theta)}2\,\mathbf w'(s)\cdot\mu_i\\
&+2\mathbf w(s)\cdot
\left\{-d_i(\theta)\ell_{\mathsf A_s}(\mu_i)
+c_i(\theta)^2q_{\mathsf A_s}(\mu_i)\right\}.
\end{aligned}}
\tag{28}
$$

**local 项。** 在 $u_i$ 支撑上，$\chi_i=1$ 且所有正阶导数为零。由 (26)，
$$
\begin{aligned}
\mathcal T_s(\chi_i;u_i,u_i)
=\frac1{16h^2}\Big[
&\{\gamma(1+d^2)-2hd\delta\}\mu_{i,0}\\
&-2h^2\delta\mu_{i,1}-\gamma h^2\mu_{i,2}
\Big]
=-\frac14\mathbf w'(s)\cdot\mu_i.
\end{aligned}
\tag{29}
$$
同时 $\mathcal T_s(\phi_\theta;\phi_\theta,\chi_i)=0$。
式 (29)中的 $\mu_{i,2}$ 包含原 $2(u_i')^2$，不能只留二导部分。

**history 项。** 原 adjoint/左右二次尾差给
$$
\mathbf I(\mathsf A_sD_\theta,\chi_i)
=d_i\,\ell_{\mathsf A_s}(\mu_i),\qquad
2\mathbf I\{\phi_\theta,\mathsf A_s(\phi_\theta,\chi_i)\}
=c_i^2q_{\mathsf A_s}(\mu_i).
\tag{30}
$$
来自其他包的同一多项式尾在 $\chi_i$ 两侧相消；来自本包的尾差保留为 $\ell$。代入 (20)即得 (28)。

这也说明平台不能随间隙函数一起删掉。其 global 作用包含一个真实 $\mathbf w'$ 项以及真实 history 乘 $\mathbf w$ 项。改变 $\chi_i$ 的间隙插值只增加命题 1 的不可见项，不改变 (28)。

## 7. 指定端芽已付之后，全部其它段的准确有限接口

令原十三行的 $13\times2n$ 矩阵仍为
$$
C_\theta=
\bigl(\mathcal A_\theta(u_1),\ldots,\mathcal A_\theta(u_n),
\mathcal A_\theta(\chi_1),\ldots,\mathcal A_\theta(\chi_n)\bigr).
\tag{31}
$$
用 (25)、(28)定义全路径函数列
$$
F_{i,\theta}=\mathcal P_*\mathcal B_\theta(u_i),\qquad
F_{n+i,\theta}=\mathcal P_*\mathcal B_\theta(\chi_i).
\tag{32}
$$
这些仍是原 $s$ 上的完整函数，不用有限采样代替它们。

**定理 3。** 在第 1 节已经取得 R467 同一规范的前提下，保其全 period、三合法矩及指定端芽，并使所有其它 $s$ 段的 ruling 也为零，等价于存在一个光滑周期的真实系数族
$\beta_\theta\in\mathbb R^{2n}$，在 $\theta=0,\pi$ 为零，满足
$$
\boxed{
C_\theta\beta_\theta=0,\qquad
\mathscr R_\theta(s)+
\sum_{j=1}^{2n}(\beta_\theta)_jF_{j,\theta}(s)=0
\quad\text{对全部 }s,\theta .
}
\tag{33}
$$

必要性由原核分类 (18)分解 $\eta_\theta$。其母/平台系数可在各包内固定点读取，故保光滑、周期和种子。命题 1 消掉全部 gap 部分，(17)给第一式，(15)给第二式。

反过来，由 $\beta_\theta$ 取同一个
$\eta_\theta=\sum\beta_i u_i+\sum\beta_{n+i}\chi_i$。它属于整个 period 核并保十三门；用 (14)的原 Gram 右逆选择一个全局 $\zeta_\theta$。则 (33)与 (15)支付整个 ruling，没有在各段分别选第三矩。所有函数仍同 collar、相位光滑、周期和 seed。证毕。

这不是重新声称 R221 的一般 48 行判据已经可解。新增的是对**已经支付 R467 的当前库**作准确限制：三个全局第三矩已被锁定、全部 gap 像为零，余作用的两类列已逐式显示。不能凭大量包数认定 (33)满射，也不能用逐相位解代替其光滑 seed 家族。

还有一个先于 (33)的全局必要门。把 R221 的 18 个 local 几何生成元和 24 个真实 history 生成元记为
$$
g^{\rm loc}=\{\gamma h^{i-4}d^j,\delta h^{i-4}d^j:
i,j\ge0,\ i+j\in\{0,2,4\}\},\qquad
g^{\rm hist}_{X,j}=a_X(s)\mathbf w_j(s),
\tag{34}
$$
其中 $\mathsf A_s=\sum_Xa_X(s)X$。定义
$$
\mathcal V_*=\operatorname{span}\{\mathcal P_*g_\rho:1\le\rho\le42\}.
\tag{35}
$$
(25)、(28)都属于这个固定空间，故
$$
\mathscr R_\theta\in\mathcal V_*
\tag{36}
$$
是全段可解的必要条件。42 是生成元数，不是秩。原 canonical 第三 history 仍在 $\mathscr R$；它不因完整 fourth period 为零而自动落入 (35)。

更换已付 R467 规范只将 $\mathscr R$ 改一个 (33)允许的像，故其真正的余类不变。选择 (12)的另一组三点也不改变可解性：对保持端芽商的增量，两组抽取都读出同一个端芽 $\mathbf w$ 系数。

## 8. 第二个真实有理端芽产生一个规范无关的最高行差

现在单独考虑一个实际可直接检验的情形。除 $U_a=U_*$ 外，同一真实路径另有一个双侧开端芽 $U_b$：
$$
h=H_j(1+\varepsilon_j\sigma_j^2),\quad
k=\kappa_j\ne0,\quad\omega=0,\qquad
H_j,\varepsilon_j>0,\quad j=a,b .
\tag{37}
$$
使用同一个物理 $x$ 和右锚。各 $\kappa_j,H_j,\varepsilon_j$ 可不同。若两端芽具有同一个非零常值 $\omega$，也可从起点作**一次共同**坐标识别后使用此式；不允许为不同 $\omega$ 的端芽各自平移 profiles 后比较同一行。

令两中心的真实累计算子为
$$
X_j=\Phi_{\mathsf m(s_j^*)},\qquad
X_b-X_a=\Phi_{\int_{s_a^*}^{s_b^*}M_{\rm raw}(s)\,ds}.
\tag{38}
$$
它们来自整个路径同一个起点。每个端芽的正确中心化规范坐标是
$$
k_{j,\theta}=w_\theta+X_jD_\theta ,
\tag{39}
$$
因为原端芽清理规范是 $-X_jD_\theta$。

由原 R312/R326 的中心比较，centered canonical ruling 为偶函数。真实第三初值、规范平方与第三齐次项都属于该端芽的偶三矩空间；原入历史不删除，而是通过 (39)进入完整奇响应。因而要支付该端芽的 ruling，必须令其最高奇系数为零。

[R437](R437-highest-rational-gauge-row-vanishes-on-the-complete-period-kernel.md) 对任意紧 $k$ 的完整身份是
$$
P^{(j)}_{2,\theta}(k)=\frac{\kappa_j}{24}\ell_f(k),
\qquad
\ell_f(k)=I_2\{Y(f,f),k\},\quad Y=\Phi_{p_2}.
\tag{40}
$$
该最高行不含 $H_j,\varepsilon_j$，也不依赖相位；原 ruling 中对应的是
$2\sigma_jh^2P^{(j)}_{2,\theta}$。即使某一端芽的 centered 偶部还未付，它也不可能消掉这个奇项。

由 (39)、(40)，对**任意同一个** $w_\theta$，准确有
$$
\boxed{
\frac{24}{\kappa_b}P^{(b)}_{2,\theta}(k_{b,\theta})
-\frac{24}{\kappa_a}P^{(a)}_{2,\theta}(k_{a,\theta})
=\ell_f\{(X_b-X_a)D_\theta\}.
}
\tag{41}
$$
共同 $\ell_f(w_\theta)$ 直接相消。这个身份甚至不需要先假设第四 period 已付；更不需要限制 $w_\theta$ 的相位谐波。第三规范只能改偶三矩空间，不能改变 (41)。

定义原两个四次配对
$$
d_f(X)=I_2\{Y(f,f),X\Delta\},\qquad
e_f(X)=I_2\{Y(f,f),X(f,g)\}.
\tag{42}
$$
$X\Delta$ 与 $X(f,g)$ 因完整三矩闭合而真紧，$Y(f,f)$ 的真实二次左尾仍保留。

[R444](R444-original-hook-response-action-and-the-highest-second-period-blind-row.md) 在当前同步八/十二及外宏包装上已经证明
$$
e_f(X)=0\quad(X\in E_8).
\tag{43}
$$
于是 (41)化为
$$
\boxed{
\frac{24}{\kappa_b}P^{(b)}_{2,\theta}(k_{b,\theta})
-\frac{24}{\kappa_a}P^{(a)}_{2,\theta}(k_{a,\theta})
=\sin^2\theta\,d_f(X_b-X_a).
}
\tag{44}
$$

**定理 4：真实前缀必要门。** 若同一个全局规范支付 (37) 两个端芽的完整 ruling，则
$$
\boxed{
d_f\!\left(\Phi_{\int_{s_a^*}^{s_b^*}M_{\rm raw}(s)\,ds}\right)=0.
}
\tag{45}
$$
如果已按 R467 支付端芽 $a$，那么端芽 $b$ 的最高行准确为
$$
P^{(b)}_{2,\theta}(k_{b,\theta})
=\frac{\kappa_b}{24}\sin^2\theta\,d_f(X_b-X_a).
\tag{46}
$$
这不是估计或 principal 项，而是原完整行值。若 (45)非零，(33)中的任何剩余 period 核、任意更多包间插值及全部第三规范都不能补救。

本定理没有断言当前实际构造一定含第二个 (37)端芽，或已经产生一个非零 (45)。它提供一个准确的第一阻断值；一般段仍用 (25)、(28)、(33)。

## 9. 多个端芽：一个成本最高值，加真实相对前缀值

若有有限个同坐标端芽 $U_1,\ldots,U_q$，定义
$$
\mathfrak D_f(s)=d_f(\Phi_{\mathsf m(s)}),\qquad
\mathfrak D_f'(s)=d_f(\Phi_{M_{\rm raw}(s)}).
\tag{47}
$$
全周期 $M=0$ 只给
$\mathfrak D_f(s_0+L)=\mathfrak D_f(s_0)$；不要求内部中心值相同。

在两个 canonical period 源已经属于真实 $L_f$ 像时，用 R437 的像泛函记
$$
b_d^0=\mathfrak p_f\!\left(-\frac{V_d}{2\tau}\right),\qquad
b_e^0=\mathfrak p_f\!\left(-\frac{V_e}{2\tau}\right).
\tag{48}
$$
它们只由同一个完整成本及真实 period 规范确定，不能在不同端芽另选。由原 incoming 公式及 (43)，第 $j$ 端芽的两个最高值是
$$
b_d^{(j)}=b_d^0+d_f(X_j),\qquad
b_e^{(j)}=b_e^0 .
\tag{49}
$$
因此全部这些最高门准确等价于
$$
\boxed{
b_e^0=0,\qquad
b_d^0+d_f(X_1)=0,\qquad
d_f(X_j-X_1)=0\quad(2\le j\le q).
}
\tag{50}
$$
这里有至多 $q-1$ 个列出的相对前缀标量；不宣称它们独立。

R467/R468 的完整成本与 $K_P=\mathcal B_P\mathfrak H$ vertical 接口支付的是 (50)的共同成本值。固定几何前缀时，在成本上增加 $\eta\mathcal B_Z\mathfrak H$ 会把所有 $b_d^{(j)}$ 同时改
$-\eta d_f(Z)/\tau$，其相对差保持。当前初选还有
$$
d_f(P)=\eta_P\ne0.
\tag{51}
$$
故 (45)并非在整个 E8 上恒为零的 profile 恒等式；一个 $P$ 方向的真实前缀差能被它读出。

尤其不能把 $q$ 个中心的 $X_j$ 当作互不相关的规范参数。它们由真实累计 (38)相联；后置一个完成时 $M=0$ 的块，若不穿过这些标记中心，就不改变这些相对前缀。即使该块准确校正了整个 $J_{\rm aff}$ 和一个最高 scalar，也不因此支付所有 (50)。

## 10. 前缀门是标记路径资料，不是免费加入 U 的一个新成本坐标

式 (45)只使用二阶真实历史。它不是本文已证明可由完整第四成本 $V\in U$ 单独恢复的线性函数。故不能未经证明把
$V\mapsto d_f(X_b-X_a)$ 加到 $J_{\rm aff}$，再直接援用 R468 的有限成本截面。

原 [R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md) 确实给出任意端点的任意有限八矩桥。这说明 (50)可作为一个**真实几何前缀的有限设计目标**，而非只能形式地改 $X_j$。其准确范围如下。

取有限个已经指定的端芽段，外接到常值 collar。固定真实 frame/scalar 端数据和一组目标中心矩阵 $Z_j$。在进入第 $j$ 段之前，前面已完成的累计矩阵和该段从入口至中心的原积分都已确定。给连接桥指定两者与 $Z_j$ 的准确差作为 $M$ 目标，R70 的有限圈数 IFT 就准确实现该中心值。连接的两个端点在真实常值 collar 内，R70 完成分部积分矩与原累积的边界差在那里为零；端芽入口到中心的非平段则始终使用原 $M_{\rm raw}$ 积分，不将它替成一个丢边项的局部矩。最后一座桥可以把全累计矩阵复位为零。参数在固定紧盒内时，先固定足够大的有限圈数，得到光滑依赖；所有连接成本、时间、真实 $\omega$ 和端数据都保留。

这项逐段构造只证明**八矩前缀层**的可实现性。它一般同时改变第三成本、第四全部基准、其余段 ruling 与总长度；也不自行闭合中心线位移。共同物理窗口仍须按 R70/R468 从起点选够，不能事后把新桥塞进任意已冻结的窄窗口。本文没有把它当作完成 R467 全假设的反例或一个新的完整实际联合截面。

若未来要从起点同时装有限个端芽，可以把这些有限矩阵/标量前缀目标保为真实标记路径条件；再把所有新桥产生的第三、第四基准完整送入原后续构造。完成后的 $M=\mathbf T=0$ 成本控制若放在全部标记端芽之外，确实保持已经固定的前缀差。其余规范仍须共同满足 (33)，并不因最高差全零自动完成。

这给出了一个具体的新接口，而不是要求“再加更多 arbitrary gauge”：先保真实标记前缀，再处理同一全局函数像。

## 11. 当前构造下一次真正需要的有限资料

对一条实际固定且已满足 R467 前提的路径，继续判断全段 fourth range 所需的资料可准确列为：

1. 原 canonical 第四 ruling 的完整目标 $\mathscr R_\theta(s)$，使用已经选定的同一个 $(\bar w_\theta,\bar\chi_\theta)$；不可只留其全周期积分。
2. 全路径的真实 $h,k,\omega$、18 个 local 系数与八个累计 $a_X(s)$，从同一个原起点读取；所有桥、prototype 重复与拼接段必须在内。
3. 当前实际最细包的三矩 $\mu_i$ 与 (24)的完整 cubic 配对；它们组成 (25)、(28)的两类列。无需恢复无限多个 gap 方向，它们已由命题 1 严格排除。
4. 原十三门矩阵 (31)及相位/seed 条件，与上述全段函数同时使用；不另造一个独立端口规范。
5. 如果实际路径含多个 (37)端芽，先读取 (45)/(50)的真实相对前缀。这些值若不为零，可在求解 (33)之前准确停止这条固定几何的同规范路线。

这些都是原字段或原式；本文没有执行它们的数值评价，也没有要求重算已付的 self/rank 或 3974 forcing。若要新计算，必须针对同一实际路径的这些尚未评价资料另写明确源码与公开任务；不能从旧全成本收据反造内部历史。

## 12. 完成范围与直接来源

本文已经证明：

- 指定有理端芽支付后，全局第三 ruling 矩的唯一性及保真归一化 (14)—(15)；
- 当前 rank-one 圆的全部 gap 对全段无效，以及任意真实几何上的母/平台完整列 (25)、(28)；
- 同一 period、同一十三门、同一第三规范下的准确全段接口 (33)；
- 两个及有限多个同坐标有理端芽的规范不变量 (41)—(50)，包括原 $I_2$、真实前缀和当前 $e_f=0$ 的因子；
- 任意有限八矩桥只在其真实二阶前缀范围内可以支付这些标记目标，不免费保第三、第四或完整 ruling。

直接来源为 R56、R70、R184、R221、R312、R326、R327、R437、R444、R455、R460、R464、R467、R468，本文各处按所需原式引用。R468 的新增实际截面已经发表；它只负责其注明的完整成本目标，不替代本文标记前缀或全段条件。

没有由本文得到实际全路径第四校正、全阶收敛、闭面嵌入、reach 或主问题的大振幅指标。新的结论是一个可以准确使用的限制：**单一端芽的十三行支付后，全局规范的剩余能力有明确列式，而多个端芽之间已经出现一个不能由任何共同规范消掉的真实二阶前缀差。**
