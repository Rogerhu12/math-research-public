# R150 附录：物理对数曲线方向、完整合并矩偏导与光滑最高符号

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d。根代理独立核对合并目标方向、最高平移系数和原多池费用。

状态：已证明；Astra-ISP-1cf8c51d 与 boundary_resume_1cf 全文独立复核完整合并方向、真实闭图及块预算。固定真实物理行的一个曲线方向，用同一完整合并矩表构造有界偏导逆。由此处理平移首系数具有已付矩形逆的全部普通点态复合；特别包括最高实齐次符号沿对数曲线恒零、但在该曲线上有非零梯度的任意次数多项式。保留原中心、完整 Bell、全部标量移位和任意复平方可和指数权。普通复 Hilbert 不变子空间问题仍未完成。

## 1. 设置和结论

取不同的正实指数
$$
0<\rho_1<\cdots<\rho_q,
$$
以及原固定中心的实际模式
$$
u_{\rho_\nu}
=-\kappa_{\rho_\nu}
+\sum_{p\ge0}a_{\nu p}\chi_p,\qquad
a_{\nu p}
=\frac{\rho_\nu(\log(p+2))^{\rho_\nu-1}}{p+2}.
\tag{1.1}
$$
给定
$$
w=b_*+\sum_pb_p\chi_p,\qquad b\in\ell^2,
$$
下文使用同一个原 $\xi_w=e^w$，不调整任何 $\kappa_\rho$。

固定 $\tau>0$，定义实际曲线方向
$$
\boxed{
v_\nu(\tau)=\rho_\nu\tau^{\rho_\nu-1}.
}
\tag{1.2}
$$
这是固定实向量，不是新的物理行，也不把原变量替换成未验证的新模式。

对非恒定标量多项式 $F(x)$，把
$$
F(x+t v)=\sum_{j=0}^{p}a_j(x)t^j,\qquad a_p\ne0
\tag{1.3}
$$
视为关于一个形式标量 $t$ 的准确有限多项式。
要求 $p\ge1$，并记其实际最高系数为 $a=a_p$。

**定理1。** 假设对每个整数 $h\ge1$、每个复平方可和 $w$，
$a(u)^he^w$ 的完整普通 Bell 规范实现具有全域有界逆，且该逆属于
$\mathfrak C=\{A\}'$。
则对每个非零 $Q\in\mathbb C[z]$，
$$
\boxed{Q(F(u_{\rho_1},\ldots,u_{\rho_q}))e^w
\text{ 非零且对实际 }A\text{ 循环}.}
\tag{1.4}
$$

这个逆条件具有以下已经完整支付的可检查子类。
若
$$
a(x)=R(\ell_1(x),\ldots,\ell_s(x)),
\tag{1.5}
$$
其中各 $\ell_j=b_j+\sum_\nu c_{j\nu}x_\nu$ 的非恒定系数实、且不全为零，
$b_j\in\mathbb C$，允许这些形式相互相关；
$R$ 有一个真实矩形顶角
$$
R(y)=\sum_{\alpha\le m}c_\alpha y^\alpha,\qquad c_m\ne0,
\tag{1.6}
$$
则定理1的逆条件成立。也允许 $a$ 为非零常数。
这个子类由[矩形 Bell 逆稿](R150-appendix-rectangular-bell-inverses-and-nonmonic-largest-logarithmic-modes.md) §§2–5 付清。其真实闭图识别在 §5 再说明。

**定理2（光滑最高曲线分支）。** 设 $D=\deg F\ge2$，最高齐次部分
$F_D$ 为非零实系数多项式，并且
$$
H_F(\tau)
=F_D(\rho_1\tau^{\rho_1},\ldots,\rho_q\tau^{\rho_q})
\equiv0.
\tag{1.7}
$$
若存在一个 $\tau>0$ 使
$$
\boxed{\nabla F_D(v(\tau))\ne0,}
\tag{1.8}
$$
则 (1.4) 对全部非零 $Q$、任意复 $w$ 成立。
允许 $F$ 的全部较低齐次部分具有任意复系数。
最高部分为非零复标量乘实多项式时，同样成立。

若 $H_F$ 不恒为零，[合并对数矩稿](R150-appendix-merged-complex-logarithmic-moment-pools-and-all-resonant-zero-parameters.md)已经给 (1.4)；本稿新增的是 (1.7) 下的真实非零偏导方向。

## 2. 完整矩表及相同键的准确合并

对本次需要的有限普通次数 $d$，保留所有
$1\le|\omega|\le d$ 的原矩。令
$$
d_\omega=|\omega|,\qquad
s_\omega=\rho\cdot\omega-|\omega|,\qquad
c_\omega=\prod_\nu\rho_\nu^{\omega_\nu}.
$$
原物理矩行准确为
$$
\prod_\nu a_{\nu p}^{\omega_\nu}
=c_\omega\,m_{d_\omega,s_\omega}(p),\qquad
m_{d,s}(p)=\frac{(\log(p+2))^s}{(p+2)^d}.
\tag{2.1}
$$
所有相同 $(d,s)$ 的行先合并，不能把它们当作独立模式。

一次模式保留原中心：
$Y_{e_\nu}=u_{\rho_\nu}$，合并变量是
$W_{1,\rho_\nu-1}=u_{\rho_\nu}/\rho_\nu$。
对 $|\omega|\ge2$，原高矩
$$
Y_\omega
=\sum_p\Bigl(\prod_\nu a_{\nu p}^{\omega_\nu}\Bigr)(\chi_p-1)
$$
是绝对可和实际符号，并且
$$
Y_\omega=c_\omega W_{d_\omega,s_\omega}.
\tag{2.2}
$$
倾斜一阶、高矩算子及完整共振累积量遵循同一个精确比例；
该事实来自逐位生成函数的有限线性参数恒等式，不丢掉原常数。

记固定总矩阶 $k$ 出现的不同第二键为
$$
\mathcal S_k=\{\rho\cdot\omega-k:|\omega|=k\}.
$$
由 (1.2)，
$$
c_\omega\tau^{s_\omega}
=\prod_\nu v_\nu(\tau)^{\omega_\nu}.
\tag{2.3}
$$
所以在合并变量中定义的固定方向
$$
\boxed{
\partial_{\eta^{(k,\tau)}}
=\sum_{s\in\mathcal S_k}\tau^s
\partial_{W_{k,s}},
}
\tag{2.4}
$$
恰在每个原 $Y_\omega$ 上产生增量 $v^\omega$。
其他总矩阶的方向分量取零。
即使同一键有多个原 $\omega$，(2.3) 对它们同时成立；
因此 (2.4) 是合法的合并方向。

## 3. 有限生成式给出的真实方向偏导

对任意有限普通多项式 $G$，记普通转共振的有限多项式
$$
\mathcal Q_G(Y)
=
G(\partial_z)
\left.
\exp\!\left[
\sum_\nu z_\nu Y_{e_\nu}
+\sum_{2\le|\omega|\le\deg G}
\frac{(-2)^{|\omega|-1}}{\omega!}z^\omega Y_\omega
\right]\right|_{z=0}.
\tag{3.1}
$$
合并后的多项式记为 $\overline{\mathcal Q}_G(W)$。
准确的有限偏导恒等式是
$$
\partial_{Y_\omega}\mathcal Q_G
=\frac{(-2)^{|\omega|-1}}{\omega!}
\mathcal Q_{\partial^\omega G}.
\tag{3.2}
$$
当 $|\omega|=1$ 时同样成立。

对 (3.2) 按同一完整键先合并，再使用 (2.3) 求和，得到
$$
\begin{aligned}
\partial_{\eta^{(k,\tau)}}\overline{\mathcal Q}_G
&=(-2)^{k-1}
\sum_{|\omega|=k}\frac{v^\omega}{\omega!}
\overline{\mathcal Q}_{\partial^\omega G}\\
&=\frac{(-2)^{k-1}}{k!}
\overline{\mathcal Q}_{(v\cdot\partial_x)^kG}.
\end{aligned}
$$
即
$$
\boxed{
\partial_{\eta^{(k,\tau)}}\overline{\mathcal Q}_G
=\frac{(-2)^{k-1}}{k!}
\overline{\mathcal Q}_{(v\cdot\partial_x)^kG}.
}
\tag{3.3}
$$
这里各右侧带横线的多项式都先按同一完整键表合并；不与 (3.2) 的未合并 $Y$ 多项式混用。最后一式是多重指标二项展开，保留了全部阶乘。

令 $P_{G,w}$ 为真实倾斜共振 Bell 多项式：
它由作用于 $\overline{\mathcal Q}_G$ 的一个有限常系数微分指数得到，
其系数是合并物理行对应的真实有界累积量。
这些系数独立于显示变量 $W$，所以 (2.4) 与该有限微分算子交换。
因此 (3.3) 完整提升为
$$
\boxed{
\partial_{\eta^{(k,\tau)}}P_{G,w}
=
\frac{(-2)^{k-1}}{k!}\,
P_{(v\cdot\partial_x)^kG,w}.
}
\tag{3.4}
$$

右侧是显示普通多项式的全部 Bell 实现，不是丢掉累积量后的原多项式。
两边先在 R186 的一个足够高共同自然域上相同。
各自的规范图又以 $\mathbb C[A]e^w$ 为图核心，故 (3.4) 对对应实际闭实现成立。
不以等式成立于单个向量来推断任意闭扩张相同。

## 4. 全部外层多项式的固定有界偏导逆

取定理1的 (1.3)，以及非零
$$
Q(z)=q_hz^h+\cdots,\qquad h\ge1,\qquad q_h\ne0.
$$
令 $G=Q(F)$、$k=ph$。
关于平移参数的准确最高项是
$$
G(x+t v)=q_h a(x)^h t^{ph}
+\text{较低次 }t\text{ 项}.
$$
于是
$$
\boxed{
(v\cdot\partial_x)^kG=k!\,q_h a(x)^h.
}
\tag{4.1}
$$
这是整个标量多项式恒等式；不只在曲线上的一个取值成立。

代入 (3.4)，得到原合并矩表中的实际偏导
$$
\boxed{
\mathsf D_{G,\tau}
=(-2)^{k-1}q_h\,\mathsf B_{a^h,w},
}
\tag{4.2}
$$
其中 $\mathsf B_{a^h,w}$ 是普通点态 $a(u)^he^w$ 的规范 Bell 图。
定理1的前提给
$$
\boxed{
\mathsf D_{G,\tau}^{-1}
=\bigl[(-2)^{k-1}q_h\bigr]^{-1}
\mathsf B_{a^h,w}^{-1}\in\mathfrak C.
}
\tag{4.3}
$$
这里没有额外的纯模式 $\rho_q^k$ 因子：各 $\rho_\nu$ 已在 (2.3) 的方向分量中完整计入。

### 4.1 任意固定目标向量的实际矩池证书

合并矩稿对本次全部有限键构造 $K$ 个分离物理池。
每块取每池一个位，原矩阵
$$
\Xi_B=(m_g(p_i))_{g,i}
$$
可逆；所有真实逆成本的对数为 $O(\log N)$。
这是一整张矩阵的逆预算，故不限于一个坐标基向量。

令 $\eta=\eta^{(k,\tau)}$ 的全键坐标向量，并取
$$
\beta_B=\frac14\Xi_B^{-1}\eta.
$$
若 $L_{p_i}=4\sum_gm_g(p_i)\partial_{W_g}P_{G,w}$ 是真实一次反射系数，
则在已付自然深域上
$$
\sum_i\beta_{B,i}L_{p_i}=\mathsf D_{G,\tau}.
\tag{4.4}
$$
取相应的块输入
$$
Q_B=\mathsf D_{G,\tau}^{-1}
\sum_i\beta_{B,i}\prod_{j\ne i}t_{p_j}N_{p_j}.
\tag{4.5}
$$
其平方零最高项恰为原块的完整顶部乘积。
所有高次项仍由实际 $N_j^2=\eta_jN_{j+1}$ 处理。

$\tau,k,\eta$ 对本次固定多项式均固定，(4.5) 比原单位坐标证书只多一个固定 $\|\eta\|$ 和一个固定有界逆范数。
$r$ 次提升只增加几何费用，不改变
$$
\log H_N=O(r\log N),\qquad r=\lfloor\sqrt N\rfloor.
$$

### 4.2 原核、增长正则和原全空间配对

令 $M=\ker\mathsf P_{G,w}$。
每个块输入中的有界算子均属于 $\mathfrak C$，保持 $M$ 和每个固定共同词域。
由[增长正预解引理](../notes/2026-11-13-growing-positive-resolvent-powers-and-actual-multimode-kernel-jets-1cf.md)，取同一有限正分量正则器
$$
\mathcal R_r=R(r^{-2})^{c_G r},
$$
即可先在 $M$ 内支付全部 $O(r\deg G)$ 原混合词，并且
$\mathcal R_r\to I$ 强。
不要求整个 $M$ 预先有任何一阶自然域。

原矩池平均的非零弱极限、实际 carry 和局部四次交换子预算不变。
原 $C$ 双线性配对遂迫 $M=0$。
所有逆先在核内作用，最左的物理反射仍保持原顺序；
不把逆移过反射，也不让其伴随保持未知核。

R186 的完整图循环判据给 (1.4)。
$h=0$ 时是非零常数倍 $e^w$，单独成立。
这证明定理1。

## 5. 矩形平移首系数的条件确实可用

假设 (1.5)–(1.6)。
每个非恒定实线性形式 $\ell_j(u)$ 的物理行是有限个不同正实对数幂的实线性组合。
最大的非零实指数项支配其余项，所以该行最终具有固定实符号，绝对值不可和。
其有限头、原 $\kappa_\rho$ 和复常数均为有界交换扰动。
因此每个实际第一阶为空谱，任意复 $w$ 的倾斜后也仍空谱。

矩形 Bell 逆稿已经完整证明自然乘积
$$
\prod_jT_j^{m_j}
=\left(\prod_jT_j^{-m_j}\right)^{-1}
$$
的准确完整域，并用同一 $R(s)^N$ 给图核心，从而识别完整矩形 Bell 与原规范图。
对每个 $h\ge1$，$R(y)^h$ 的顶角为 $hm$、顶系数为 $c_m^h\ne0$；
其完整普通 Bell 因而有真实全域有界交换逆。

按原 $u$ 模式和按 $\ell_j(u)$ 模式构造的 $a(u)^he^w$ 两个规范闭图，
都以 $\mathbb C[A]e^w$ 为图核心，且其动作在该轨道上相同。
所以它们是同一个闭图。
模式相互相关不影响这个证明，不假设形式独立或未经证明的自然域相等。

若 $a$ 是非零常数，则 $a^hI$ 本身有界可逆。
这里不使用对常数 $a=c$ 的任意 $Q(c)$ 非零断言；本节仅需
$a^h=c^h\ne0$。
定理1的全部前提已经支付。

## 6. 光滑最高曲线：任意实最高次数及任意复低次

假设 (1.7)–(1.8)，固定一个满足 (1.8) 的 $\tau$，记 $v=v(\tau)$。
因为
$$
(\rho_1\tau^{\rho_1},\ldots,\rho_q\tau^{\rho_q})=\tau v
$$
且 $F_D$ 齐次，
$$
F_D(v)=\tau^{-D}H_F(\tau)=0.
\tag{6.1}
$$
对 $F_D(x+t v)$ 作有限齐次展开，$t^D$ 项为零，
$t^{D-1}$ 项准确为 $\nabla F_D(v)\cdot x$。
原 $F_{D-1}$ 部分还贡献常数 $F_{D-1}(v)$；
全部更低部分至多为 $t^{D-2}$。
所以
$$
\boxed{
p=D-1,\qquad
a(x)=\nabla F_D(v)\cdot x+F_{D-1}(v).
}
\tag{6.2}
$$
$\nabla F_D(v)$ 是非零实向量，$F_{D-1}(v)$ 可以为任意复数。
故 $a(u)$ 是非零实线性第一阶加复常数，其实际一阶及全部复倾斜为空谱。
完整普通 $a(u)^h$ 的有界逆由 R134 的单一空谱 Bell 定理，或由 §5 的单形式矩形特例给出。

定理1于是适用。对每个非零 $Q$ 都重做 (4.1)–(4.3)，证明全部普通点态复合，而不从 $F(u)e^w$ 的循环性推断其点态幂。

若 $F_D=cH_D$，其中 $c\ne0$、$H_D$ 为实齐次多项式，先对
$c^{-1}F$ 应用上述证明，再把外层多项式换为 $z\mapsto Q(cz)$。
此操作不改变原模式、原中心或权向量。定理2得证。

特别 $F$ 非恒定，因此对所有 $\lambda\in\mathbb C$ 和所有整数 $r\ge1$，
$$
\boxed{[F(u)-\lambda]^re^w\text{ 非零且循环}.}
\tag{6.3}
$$

## 7. 一个四次、最高普通曲线恒零的完整例子

取 $\rho_\nu=\nu$，$\nu=1,\ldots,5$，并令
$$
g_1=x_1x_5-\frac58x_2x_4,\qquad
g_2=x_2x_5-\frac56x_3x_4,
$$
$$
F_4=(x_1^2+x_2^2)g_1+(x_3^2+x_4^2)g_2,\qquad
F=F_4+x_3.
\tag{7.1}
$$
两项 $g_1,g_2$ 在原曲线 $x_\nu=\nu\tau^\nu$ 上分别为
$$
(5-\tfrac58\cdot8)\tau^6=0,\qquad
(10-\tfrac56\cdot12)\tau^7=0.
$$
因此 $H_F(\tau)\equiv0$。

在 $\tau=1$ 时 $v=(1,2,3,4,5)$。
有 $x_1^2+x_2^2=5$、$x_3^2+x_4^2=25$，
并且 $g_1(v)=g_2(v)=0$，所以
$$
\nabla F_4(v)=5\nabla g_1(v)+25\nabla g_2(v)
=\left(25,\frac{225}{2},-\frac{250}{3},-\frac{275}{4},55\right).
\tag{7.2}
$$
尤其 $\partial_5F_4(v)=55\ne0$。
这些系数与 $v$ 的内积为零，符合 Euler 恒等式
$v\cdot\nabla F_4(v)=4F_4(v)=0$。

由于 $F$ 没有三次齐次项，准确的平移最高系数就是
$$
a(x)
=25x_1+\frac{225}{2}x_2-\frac{250}{3}x_3
-\frac{275}{4}x_4+55x_5.
\tag{7.3}
$$
其实际物理行由最后的正 $\rho=5$ 项支配，故实际一阶为空谱。
对外层次数 $h$ 使用 $k=3h$，原合并矩目标为
$\eta_{(3h,s)}=1$，其余阶为零。
(4.2) 得到准确的偏导
$(-2)^{3h-1}q_h\mathsf B_{a^h,w}$，有全域有界交换逆。

因此所有
$$
\boxed{
Q\!\left[
(u_1^2+u_2^2)
\left(u_1u_5-\frac58u_2u_4\right)
+
(u_3^2+u_4^2)
\left(u_2u_5-\frac56u_3u_4\right)
+u_3
\right]e^w
}
\tag{7.4}
$$
均非零且循环，只需 $Q$ 为非零标量多项式。
全部 $u_\nu$ 使用原固定中心。

在原坐标中，(7.1) 对 $x_5$ 的首系数是
$x_1^3+x_1x_2^2+x_2x_3^2+x_2x_4^2$，它没有一个同时支配其余指数的原坐标矩形顶角。
本稿不据此宣称它不能经任何其他实线性形式表示归入旧矩形类；
(7.4) 的证明直接来自已验证的物理曲线方向。

## 8. 去重与剩余边界

[R236 双行平滑纤维稿](R236-appendix-two-row-resonant-smooth-fibers-and-sylvester-dichotomy.md)
使用一个无界主模式、一个绝对可和辅助模式和准确共振符号，在有限根块内证明偏导单位。
本稿处理多个独立无界对数模式的原普通点态多项式，采用全空间有界偏导逆和增长正则深域；
不把上述不同适用范围混同。

实二次最高符号的结论与[实二次全部普通复合稿](R150-appendix-global-derivative-inverses-real-quadratic-logarithmic-resonances-and-all-powers.md)一致。
新范围包括任意更高普通次数的光滑最高曲线分支，以及 §1 的一般矩形平移首系数。

若最高符号沿曲线的全部梯度同时消失，则 (6.2) 不再提供非零一阶首系数。
其中部分情况可由 §5 的更高矩形首系数处理；没有证明全部高阶接触情形都满足该条件。
同样，一般复最高符号的梯度一阶未必空谱，本稿不把全平面连续谱第一阶换成有界逆。

实际矩目标必须满足完整合并关系；任意选一个不兼容的原矩坐标，不能套用本稿。
式 (2.3)–(2.4) 正是当前方向合法的原因。
一般有限模式的全部多项式、一般正常见证源预算以及普通 Hilbert 不变子空间问题继续开放。
