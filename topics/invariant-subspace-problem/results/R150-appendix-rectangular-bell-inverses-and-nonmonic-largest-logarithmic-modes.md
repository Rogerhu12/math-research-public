# R150 附录：空谱一阶的矩形 Bell 全域逆与最大对数模式的非首一多项式

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d。根代理独立提出最大实际指数的高阶纯矩方向，并要求完整核对自然乘积与规范图核心。

状态：已证明；Astra-ISP-1cf8c51d 与 boundary_resume_1cf 全文独立复核，常数外层的零向量边界已单列。先证明有限多个空谱一阶的矩形顶项多项式具有全域有界交换逆，再用于原对数模式中对最大实际指数变量任意次数、矩形首系数的全部普通点态复合。保留原中心、任意复平方可和指数权和完整 Bell 修正。普通复 Hilbert 不变子空间问题仍未完成。

## 1. 旧结果与本稿新增范围

[R134 §§3、6](R134-empty-spectrum-first-chaos-polynomial-cyclicity.md) 已证明单个空谱一阶的首一有界交换系数多项式有真实有界逆。
[R149 §4](R149-empty-spectrum-overlapping-point-products.md) 已把该逆用于一空谱模式的完整普通 Bell 多项式。
[R150 原稿](R150-empty-spectrum-anchor-rectangular-polynomial-cyclicity.md) 处理一个空谱锚与另一个一般模式，另需其所列首位和有限余数条件。
[R197 §§9–10](R197-disjoint-empty-inverses-coordinate-boundaries-and-mixed-type.md) 给有界逆变量中的单项式单位类及非负余因子类；不把一般自然多变量乘积预先认成规范闭图。

本稿使用 [R186 §§2–6、10](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md) 的共同正则器及完整普通 Bell 图，补足以下两个接口：

1. 有限多个空谱一阶、任意重叠或线性相关模式的矩形顶项 Bell 多项式，在明确的自然矩形域上闭且有全域有界交换逆；这与原规范最大图相同。
2. 对最大实际正实对数指数的变量，不仅允许实线性首系数，还允许由有限个实线性一阶组合构成的任意矩形首系数，次数可为任意正整数。所有外层非零多项式重新经过完整 Bell 和合并矩块提升。

第二部分引用[合并对数矩稿](R150-appendix-merged-complex-logarithmic-moment-pools-and-all-resonant-zero-parameters.md)的真实多池矩阵，以及[全域偏导逆稿](R150-appendix-global-derivative-inverses-real-quadratic-logarithmic-resonances-and-all-powers.md)的有界逆块提升接口。下文逐项核对新偏导及其准确闭图，不以循环向量的点态乘积传递循环性。

## 2. 交换有界逆决定整个自然乘积域

记 $\mathfrak C=\{A\}'$。取有限个实际闭一阶加有界交换扰动
$$
T_j=X_{v_j}+H_j,\qquad H_j\in\mathfrak C,\qquad 1\le j\le s,
$$
并假设
$$
\sigma(T_j)=\varnothing,\qquad L_j=T_j^{-1}\in\mathfrak C.
\tag{2.1}
$$
这里的 $v_j$ 是复平方可和第一阶符号。R134 的实际预解恒等式给每个 $L_j$ 拟幂零。
所有 $L_j$ 彼此交换，并保持每个 $T_i$ 的域，在域上交换。允许模式相互相关；不要求不交支撑或形式独立。

给定多重指标 $m=(m_1,\ldots,m_s)\in\mathbb N^s$，令
$$
B_m=\prod_{j=1}^sL_j^{m_j}.
$$
$B_m$ 有界、单射且像稠密。任何含 $m_j$ 个 $T_j$ 的固定自然词，都恰为
$$
\boxed{
M_m=B_m^{-1},\qquad
\operatorname{Dom}M_m=\operatorname{Ran}B_m.
}
\tag{2.2}
$$

完整域证明如下。若 $x=B_my$，先把自然词最右端所需的 $L_j$ 因子移到最左侧，再应用 $T_jL_j=I$；剩余向量仍是其余有界逆的乘积作用于 $y$。逐次消去得到全部中间自然域及最后的值 $y$。反向，若自然词作用于 $x$ 得到 $y$，在每个已经合法的中间域上使用 $L_jT_j=I$，倒序恢复 $x=B_my$。所以各自然词具有相同的完整域，而不只是在共同核心上相等。$B_m^{-1}$ 的图闭，因而这个自然乘积确实闭。

对每个 $\alpha\le m$（逐坐标），同一证明还给
$$
\boxed{
T^\alpha B_m=\prod_jL_j^{m_j-\alpha_j}
\quad\text{在整个 }H\text{ 上}.
}
\tag{2.3}
$$
于是 $\operatorname{Dom}M_m$ 包含于所有这些较短自然词的域中。
此处没有断言任意闭算子乘积都闭。

## 3. 矩形有界系数多项式的真实逆与规范图

考虑
$$
P(z)=\sum_{\alpha\le m}E_\alpha z^\alpha,
\qquad E_\alpha\in\mathfrak C,
\qquad E_m\in\mathfrak C^\times.
\tag{3.1}
$$
定义自然矩形实现的域为 $\operatorname{Dom}M_m$。
由 (2.3)，在此完整域上
$$
P(T)=U_PM_m,\qquad
U_P=\sum_{\alpha\le m}E_\alpha\prod_jL_j^{m_j-\alpha_j}.
\tag{3.2}
$$
其最高项是 $E_m$。对每个 $\alpha\ne m$，相应乘积含至少一个正次 $L_j$，所以它是拟幂零的；乘任何交换有界系数仍拟幂零。
有限个这样的项两两交换，其和仍拟幂零。可直接以多项式展开证明：给每一项的幂范数任意小的几何上界，再用有限多项式展开，最后令几何率趋零。
因此
$$
U_P=E_m(I+K),\qquad r(K)=0,
$$
是 $\mathfrak C$ 中的真实有界单位。于是
$$
\boxed{
P(T)^{-1}=B_mU_P^{-1}\in\mathfrak C,
\qquad
\operatorname{Dom}P(T)=\operatorname{Ran}B_m.
}
\tag{3.3}
$$
$U_P$ 有界可逆，故 $U_PM_m$ 闭；其值域是整个 $H$。
这不是将无界因式分解当作形式恒等式。

还须识别原规范最大图。取 R186 的同一个有限正分量共同正则器 $R(t)$，并取固定
$$
N\ge |m|.
$$
它满足 $R(t)^NH\subset\mathcal D_N$，其中 $\mathcal D_N$ 记录全部长度不超过 $N$ 的实际混合词。因为 $R(t)\in\mathfrak C$ 保持每个自然词域，任意 $x\in\operatorname{Dom}M_m$ 都满足
$$
R(t)^Nx\longrightarrow x,\qquad
M_mR(t)^Nx=R(t)^NM_mx\longrightarrow M_mx
\quad(t\downarrow0).
\tag{3.4}
$$
所以 $\mathcal D_N$ 是 $M_m$ 的真实图核心。$U_P$ 及其逆有界，使 $M_m$ 与 $U_PM_m$ 的图范数等价；同一 $\mathcal D_N$ 也是后者的图核心。

R186 的规范实现是 $P(T)|_{\mathcal D_N}$ 的闭包。因此 (3.2)–(3.4) 严格证明
$$
\boxed{
\mathsf P_{\rm can}=U_PM_m.
}
\tag{3.5}
$$
这一步不要求 $\mathcal D_N=\operatorname{Dom}M_m$，不以某个点态乘积已经循环作为图核心依据。

若 $m\ne0$，$B_m$ 拟幂零，故 (3.3) 的逆也拟幂零。
将任意 $\lambda I$ 并入常数系数仍保留同一个非零矩形顶项，得到
$$
\boxed{\sigma(\mathsf P_{\rm can})=\varnothing\quad(m\ne0).}
\tag{3.6}
$$
$m=0$ 时只是原有界单位 $E_0$，不称其为空谱。

## 4. 多个空谱一阶的完整普通 Bell 多项式

现在令 $v_1,\ldots,v_s$ 为实际第一阶符号，且各 $X_{v_j}$ 空谱。
取任意
$$
w=b_*+\sum_pb_p\chi_p,\qquad b\in\ell^2,\qquad \xi_w=e^w.
$$
R186 §10 的真实倾斜一阶为
$$
T_j=X_{v_j}+H_{j,w},\qquad H_{j,w}\in\mathcal A\subset\mathfrak C.
$$
其扰动按平方可和行的乘积绝对收敛。
若 $L_{j,0}=X_{v_j}^{-1}$，则
$$
T_j=(I+H_{j,w}L_{j,0})X_{v_j}
$$
是包含定义域的恒等式。
$H_{j,w}L_{j,0}$ 拟幂零，所以括号是有界单位；对任意复平移同理。
因此倾斜后仍满足 (2.1)。

设标量多项式
$$
R(y)=\sum_{\alpha\le m}c_\alpha y^\alpha,\qquad c_m\ne0.
\tag{4.1}
$$
完整普通 Bell 多项式为
$$
P_{R,w}(T)
=\sum_\gamma\frac{B_{\gamma,w}}{\gamma!}
(\partial^\gamma R)(T),
\tag{4.2}
$$
其中 $B_{0,w}=I$，全部高阶 $B_{\gamma,w}$ 为真实有界交换系数。
每个偏导仅逐坐标降低次数，所以 (4.2) 的所有单项式仍位于同一矩形
$\alpha\le m$，而顶项仍恰为 $c_m T^m$。
由 §3，其原规范闭实现有全域有界逆，并且
$$
\boxed{
P_{R,w}^{-1}[R(v_1,\ldots,v_s)e^w]=e^w.
}
\tag{4.3}
$$
$e^w$ 循环，逆属于 $\mathfrak C$ 并保持闭循环空间，故
$R(v)e^w$ 非零且循环。

若 $m\ne0$，则 $R$ 非恒定。对任意非零外层标量多项式 $Q$，若 $h=\deg Q\ge1$，
$Q(R(y))$ 的矩形顶项为
$$
q_hc_m^h\,y^{hm},
$$
其余指数逐坐标不超过 $hm$，且较低次的 $R$ 幂不可能达到该顶角。
重新对完整点态多项式 $Q(R)$ 应用 (4.2)，得到其全域有界逆及循环性。
$h=0$ 时直接是非零常数倍 $e^w$。

若 $m=0$，则 $R\equiv c\ne0$；此时准确的外层结论只对
$Q(c)\ne0$ 成立，$Q(c)=0$ 给零向量。
以下首系数应用只需 $R^h=c^h\ne0$，故常数首系数仍全部适用。
这里没有将 $P_{R,w}^h$ 当作 $R(v)^h e^w$ 的实际算子。

## 5. 原正实对数模式中的合法矩形首系数

固定实际参与多项式的模式，删去完全不出现的变量，并重新排序为
$$
0<\rho_1<\cdots<\rho_q,\qquad
u_\rho=-\kappa_\rho+\sum_{p\ge0}
\frac{\rho(\log(p+2))^{\rho-1}}{p+2}\chi_p.
\tag{5.1}
$$
$\kappa_\rho$ 是原积分比较所固定的中心；下文不为证明重新调整它。

在较小模式中取有限个仿射实线性形式
$$
v_j(x_<)
=b_j+\sum_{\nu<q}c_{j\nu}x_\nu,\qquad
b_j\in\mathbb C,\quad c_{j\nu}\in\mathbb R,
\tag{5.2}
$$
并要求每个实系数行不全为零。允许这些形式相互线性相关。
其实际第一阶的物理行是
$$
a_{jp}
=\frac1{p+2}\sum_{\nu<q}
c_{j\nu}\rho_\nu(\log(p+2))^{\rho_\nu-1}.
$$
取其中最大的非零 $\rho_\nu$，该项支配全部较小实幂，故 $a_{jp}$ 最终具有固定实符号，且绝对值不可和。
有限头和全部固定复常数属于有界交换扰动。
因此 R134 的真实正尾逆及有界交换扰动公式严格给
$$
\sigma(X_{v_j(u_<)})=\varnothing.
\tag{5.3}
$$
同样的结论适用于任意复 $w$ 的实际倾斜。

允许最高系数为下列标量多项式：
$$
a(x_<)=R(v_1(x_<),\ldots,v_s(x_<)),
\tag{5.4}
$$
其中 $R$ 满足 (4.1)。另允许 $s=0$、$a$ 为非零常数。
对于每个 $h\ge1$，(4.1) 的 $R^h$ 仍有非零矩形顶项。因此 §4 为
$$
a(u_<)^h e^w
$$
的完整普通 Bell 实现提供全域有界交换逆。

这里须识别两个实际实现，而不能只看形式代换。
一方面，按原 $u_{\rho_\nu}$ 模式构造 $a(x_<)^h$ 的 R186 规范 Bell 图；另一方面，按实际第一阶 $v_j(u_<)$ 构造 $R(v)^h$ 的规范 Bell 图。
两者均以同一个循环向量 $e^w$ 为图核心基向量，且实际作用于它都等于同一个点态向量
$a(u_<)^h e^w$。
全部 $p(A)e^w$ 上的作用也相同。
R186 §6 给该轨道分别为两者的图核心，故两个闭图准确相同。
这保留了所有原 $\kappa_\rho$、常数 $b_j$、倾斜和高阶 Bell 系数。

因此记这个共同的实际闭算子为 $\mathsf B_{a^h,w}$，则
$$
\boxed{\mathsf B_{a^h,w}^{-1}\in\mathfrak C.}
\tag{5.5}
$$
即使 (5.2) 相互相关，证明也没有以形式非零替代实际可逆：
(5.5) 是已经识别完整图的真实逆。特别实际向量
$a(u_<)^h e^w$ 非零。

## 6. 最大实际指数的任意次数纯矩偏导

设
$$
F(x)=a(x_<)x_q^t+\sum_{j=0}^{t-1}a_j(x_<)x_q^j,\qquad t\ge1,
\tag{6.1}
$$
其中 $a$ 满足 §5，较低 $a_j$ 是任意复标量多项式。
取任意非零外层多项式
$$
Q(z)=q_hz^h+\cdots,\qquad q_h\ne0,\qquad h\ge1,
$$
并置 $G=Q(F)$、$k=th$。
准确的标量偏导为
$$
\partial_{x_q}^{\,k}G=k!\,q_h a(x_<)^h.
\tag{6.2}
$$
这是因为 $G$ 对 $x_q$ 的次数恰为 $k$，其最高系数是 $q_ha^h$。

为完整核对普通幂与合并矩，记有限普通转共振多项式为
$$
\mathcal Q_G(Y)
=
G(\partial_z)
\left.
\exp\!\left(
\sum_\nu z_\nu Y_{e_\nu}
+\sum_{2\le|\omega|\le\deg G}
\frac{(-2)^{|\omega|-1}}{\omega!}\,z^\omega Y_\omega
\right)\right|_{z=0}.
$$
直接对有限生成式求导，得
$$
\boxed{
\partial_{Y_\omega}\mathcal Q_G
=\frac{(-2)^{|\omega|-1}}{\omega!}
\mathcal Q_{\partial^\omega G}.
}
\tag{6.3}
$$
没有丢失下降阶乘。对 $\omega=ke_q$，(6.2) 的 $k!$ 与 (6.3) 的分母准确相消。

物理矩按
$$
(d,s)=\bigl(|\omega|,\rho\cdot\omega-|\omega|\bigr)
$$
合并，并有
$Y_\omega=(\prod_\nu\rho_\nu^{\omega_\nu})W_{d,s}$。
由于 $\rho_q$ 是实际参与的严格最大实指数，
$$
|\omega|=k,\quad \rho\cdot\omega=k\rho_q
\quad\Longrightarrow\quad \omega=ke_q.
\tag{6.4}
$$
因此键 $(k,k\rho_q-k)$ 是唯一纯矩键。
不同总次数始终是不同键，也不会参与此处合并。

完整共振 Bell 修正是系数独立于 $W$ 的有限常系数微分算子，所以它与此偏导交换。
结合 (6.2)–(6.4)，在原规范图上得到真实偏导
$$
\boxed{
\mathsf D
=
\rho_q^k(-2)^{k-1}q_h\,\mathsf B_{a^h,w}.
}
\tag{6.5}
$$
保留了合并比例 $\rho_q^k$，右侧是普通点态 $a^h$ 的全部 Bell 实现，而非某个一阶算子幂的简写。
§5 已准确识别右侧闭图，因而
$$
\boxed{
\mathsf D^{-1}
=\bigl[\rho_q^k(-2)^{k-1}q_h\bigr]^{-1}
\mathsf B_{a^h,w}^{-1}\in\mathfrak C.
}
\tag{6.6}
$$

未参与 $F$ 的更大指数必须先删去；(6.4) 只对本次实际有限模式表使用。
无需所有矩行独立；相同 $(d,s)$ 的行已完整合并。

## 7. 在原核中执行有界偏导逆的块提升

令 $\mathsf P_{G,w}$ 为原 $G(u)e^w$ 的完整规范 Bell 实现，$M=\ker\mathsf P_{G,w}$。
合并矩稿已经对所有需要的有限 $(d,s)$ 行，构造分离池中的真实可逆矩阵，并给逆成本
$\exp(O(\log N))$。
第 (6.5) 方向属于该完整行表。

每个块的有限差分证书中，把常数偏导的倒数替换为固定
$\mathsf D^{-1}$。
因为它属于 $\mathfrak C$，它保持 $M$，也保持所有原正分量和原倾斜模式的有限共同自然词域。
在已经支付的深域上，块的最高项使用
$\mathsf D\mathsf D^{-1}=I$，没有未知限制的逆或未经证明的范围包含。

取提升阶 $r$，按已发表的[增长正预解引理](../notes/2026-11-13-growing-positive-resolvent-powers-and-actual-multimode-kernel-jets-1cf.md)，先用同一有限正分量族构造
$$
\mathcal R_r=R(r^{-2})^{c_G r},
$$
其中固定整数 $c_G$ 足够支付全部 $O(r\deg G)$ 混合词。
于是 $\mathcal R_rM\subset M$，全部必要词都合法，且
$\mathcal R_r\to I$ 强。
每个块新增加的费用仅是固定 $\|\mathsf D^{-1}\|$，$r$ 个块总共是几何因子。
它不改变原
$$
\log H_N=O(r\log N),\qquad r=\lfloor\sqrt N\rfloor,
$$
也不改变 $e^{-5r^4/6+O(r^3+r\log r)}$ 的实际局部交换子预算。

所有反射仍位于原全空间配对中；不把
$\mathsf D^{-1}$ 移过反射，不让其伴随保持未知 $M$。
原完整 $C$ 对称配对和实际多池平均于是与有界偏导逆稿完全相同，给
$$
M=0.
$$
R186 的图循环判据遂得
$$
\boxed{
Q(F(u_{\rho_1},\ldots,u_{\rho_q}))e^w
\text{ 非零且对实际 }A\text{ 循环}.
}
\tag{7.1}
$$
$h=0$ 时直接为非零常数倍 $e^w$。
特别，对所有 $\lambda\in\mathbb C$、所有整数 $r\ge1$，
$$
\boxed{
[F(u)-\lambda]^r e^w\text{ 循环}.
}
\tag{7.2}
$$
(6.1) 使 $F$ 非恒定，所以这里不存在 $F-\lambda$ 为零多项式的遗漏。
每次对 $Q(F)$ 都重做了 (6.2)–(6.6)，不是从 $F(u)e^w$ 的循环性继承。

## 8. 一个最高普通矩完全抵消、次数更高的例子

取 $\rho_\nu=\nu$，$\nu=1,\ldots,5$，原中心均保持不变。
置
$$
g(x)=x_1x_5-4x_2x_4+3x_3^2,
$$
$$
F(x)=(x_1x_2+1)\,g(x)^2+x_3.
\tag{8.1}
$$
其最高普通齐次项为 $F_6=x_1x_2g^2$。
沿合并矩曲线 $x_\nu=\nu t^\nu$，
$$
g(t,2t^2,3t^3,4t^4,5t^5)
=(5-32+27)t^6=0.
$$
因此
$$
F_6(t,2t^2,3t^3,4t^4,5t^5)\equiv0.
\tag{8.2}
$$
合并矩稿中“最高普通曲线非零”的充分条件在这里失效。

但是 $F$ 对实际最大模式 $x_5$ 的次数为2，准确的最高系数为
$$
a(x_<)=(x_1x_2+1)x_1^2=x_1^3x_2+x_1^2.
\tag{8.3}
$$
这是 $x_1,x_2$ 中顶角 $(3,1)$ 的矩形多项式。
原 $u_1,u_2$ 及其全部复倾斜均为空谱一阶。
所以对于任意非零 $Q\in\mathbb C[z]$、任意复平方可和 $w$，
$$
\boxed{
Q\!\left((u_1u_2+1)
(u_1u_5-4u_2u_4+3u_3^2)^2+u_3\right)e^w
\text{ 循环}.
}
\tag{8.4}
$$
此处包括零参数和全部移位、普通点态幂。
首系数的逆由真实混合自然积及其矩形 Bell 修正产生；没有把
$u_1^3u_2+u_1^2$ 的实际算子简写为无修正的乘积。

## 9. 准确边界

本稿不宣称一般多变量多项式只要形式非零就有有界逆。
矩形顶角必须实际出现且系数为单位；例如只有两个不可比较顶项的差不自动满足 §3。
一般全平面连续谱一阶也不能代替空谱一阶。

第一部分允许有限空谱模式任意重叠、任意相关和有界交换扰动。
点态版本另外使用 R186 的完整普通 Bell；任意有界交换扰动本身不自动成为可作点态多项式的新符号。

第二部分只要求最大实际对数模式的首系数属于 §5 的明确类；
所有较低 $x_q$ 系数可以任意复杂，最高普通合并矩可以全部抵消。
结论针对每个固定有限多项式及任意固定复平方可和指数权，不对次数、模式数或系数给统一逆范数。
一般有限模式的任意多项式、一般 $L^2$ 向量及普通 Hilbert 不变子空间问题仍未由本稿关闭。
