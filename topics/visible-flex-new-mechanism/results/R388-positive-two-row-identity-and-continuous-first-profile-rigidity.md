# R388：两条完整一层的无分母正身份与任意连续首阶轨道刚性

日期：2026-11-15。**完整纸面原式证明；未执行符号程序、求积、profile 扫描、人工测试或研究运行。**

[R387](R387-positive-j-four-one-history-obstruction-for-resonant-weak-circles.md) 已排除当前小共振 Gaussian 芽上、通过全部已列低阶门的非退化弱单 hook 圆。本稿保留两个完整一层系数，在消元中不除以 $P(t)$。得到的准确正身份对每个 $\kappa\ne0$ 都成立，条件是相应共振芽已经存在于实际几何上；这不是一条大参数安装定理。

更重要的是，原恢复与这一身份都只使用固定的一对 $(f,u)$，没有外部轨道参数的导数。对任意同一固定种子出发、连续到二阶 jet 的首阶 profile 轨道，完整第四必要门迫
$$
(u_\tau'')^2=(f'')^2
$$
逐点成立，连续性随即迫 $u_\tau=f$。不要求圆、有限维包空间、rank-one、偶母或第二 hook。

这是指定几何类上的**首阶轨道刚性**。不把它宣布为全部主课题、所有端芽或高阶才开始变化的实际有限变形不可能。

原接口来源：[R184 的全部二、三阶 gauge](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)、[R224 的完整偶部与原传入 history](R224-even-germ-ruling-invariant-and-positive-epsilon-obstruction.md)、[R311 的参数无关恢复](R311-continuous-rank-one-profile-orbits-are-rigid-under-the-complete-low-order-gates.md)、[R325 的完整 mixed 第零行](R325-inward-weak-hook-circles-pay-three-directed-rows-and-the-one-history-compatibility.md)及 R387 的完整第四行。

## 1. 原对象与实际存在的几何前提

固定一个真实周期 ruled 几何、同一个紧物理窗口 $I=[\ell,r_*]$、共同双零 collar 和右锚
$$
Jv(x)=\int_x^{r_*}v(y)\,dy.
$$
沿整个真实路径，原二阶与第三周期算子满足
$$
M=0,\qquad T=\kappa_H\mathfrak H,\qquad \kappa_H\ne0.
\tag{1}
$$
$\kappa_H$ 与下面的局部端芽参数 $\kappa$ 不同。

假设某个双侧开端芽准确为
$$
h=h_e e^{\varepsilon\sigma^2},\qquad
k=\kappa(1-2\varepsilon\sigma^2),\qquad
\omega=\kappa/h,\qquad
\varepsilon=\kappa^2/4,\qquad h_e>0,\quad\kappa\ne0.
\tag{2}
$$
整个所用窗口满足原物理条件 $x+\omega>0$。它可含负 x；本文所有原恢复与矩身份都无除 x。

取固定实 $f\in C_c^\infty(I^\circ)$，以及连通参数空间 $\mathcal A$ 上的实 profiles
$$
u_\tau\in C_c^\infty(I^\circ),\qquad
u_{\tau_0}=f.
\tag{3}
$$
全部 profiles 使用同一双零 collar。要求 $\tau\mapsto u_\tau$ 至少在 $C^2$ 拓扑连续；实际上最后一步只需要每个 x 的 $u_\tau''(x)$ 连续。

目标始终是原固定种子度量
$$
g_\eta=g_X+\eta^2(dY_f)^2.
\tag{4}
$$
$\eta$ 是形式变形参数，不是端芽的 $\varepsilon$。考虑以 $Y_{u_\tau}$ 为首阶项、可使用全部合法二阶及第三阶齐次改动的原四阶问题。各阶规范沿 R184/R296；不重定高阶系数或历史初值。

定理可以作两种等价的必要性使用：

- 若某轨道在每个 $\tau$ 具有原完整二、三、四阶解，下文所用有限必要子系统自动成立；
- 即使只假定下文明确列出的必要子系统，不假定完整解存在，也已经迫轨道恒定。

不要求 $u_\tau$ 始终在任何固定有限 profile span 中。其形状、活动区间内的比例与交叉可随参数变化，只须保上述共同物理窗口和 collar。

## 2. 完整低阶恢复为何给原三矩与唯一弱 hook

记
$$
D=f\odot f-u\odot u,\qquad
\mu(a,b)=\left(
\int a''b'',\ \int xa''b'',\
\int(x^2a''b''+2a'b')
\right).
\tag{5}
$$
这里先固定任意一个 $\tau$，写 $u=u_\tau$。以下没有 $\tau$ 导数。

原二阶 ruling 是几何三列与 $\mu(D)$ 的配对。置
$$
j=2\varepsilon\kappa\sigma^2,\qquad H=e^{\varepsilon\sigma^2},
$$
端芽上的三列为
$$
w_0=\frac{1+j^2}{4h},\qquad
w_1=\frac j2,\qquad w_2=\frac h4.
\tag{6}
$$
它们在这个开端芽上真线性独立。若常数 $A,B,C$ 满足
$Aw_0+Bw_1+Cw_2=0$，乘 $4h$ 得
$$
A(1+j^2)+2Bjh+Ch^2=0.
$$
$H$ 超越于 $\mathbb R(\sigma)$，且 $j$ 非零，所以 $A=B=C=0$。这是 R249 的原函数域论证，不是逐采样矩阵秩。

因此完整二阶必要条件准确给
$$
\boxed{\mu(u,u)=\mu(f,f).}
\tag{7}
$$
原 $M=0$ 支付二阶周期。三矩(7)又使每个 $XD$、$X\in E_8$ 的实际二次左尾为零，canonical 二阶 $Z(D)$ 满足双 collar。于是任意另一个合法二阶解都可写成
$$
\widetilde Z=Z(D)-Y_w,
\tag{8}
$$
其中 w 是与 $\sigma$ 无关、具有共同 collar 的真实 profile。

原第三 canonical 周期为 $-2T(u;D)$；二阶改动(8)只增加 $2\Phi_M(u,w)=0$。由(1)及完整对角身份
$\mathfrak H(u;u,u)=0$，完整第三周期必迫
$$
\boxed{\mathfrak H(u;f,f)=0.}
\tag{9}
$$
这正是弱单 hook，不增加 $\mathfrak H(f;u,u)=0$。

[R306](R306-derivative-rank-classification-and-overlapping-profile-Gaussian-obstruction.md) 的原通量给
$$
\mathfrak H(u;f,f)=0
\quad\Longleftrightarrow\quad
A_f(u'f''-f'u'')=0,\qquad
A_f=6f'f'''-2(f'')^2.
\tag{10}
$$
反向中的两个真实右常数也在 R306 支付；本文主要使用(9)，不会从只满足一个微分方程的对象跳过原锚条件。

这里没有声称三矩和弱 hook 已足以支付全部第三 range。若原四阶族存在，第三 ruling、原初值和 collar 必然还需成立；它们不能减弱已推得的必要条件。

## 3. 全部合法 gauge 与原传入历史不改变所用偶部门

[R184](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)(7)–(12)的展开是关于固定 $(u,D,w,\chi)$ 的原双线性式：
$$
\Delta H_4=
2H(Z(D),Y_w)-H(Y_w,Y_w)
-4H(Y_u,Z(u,w))-2H(Y_u,Y_\chi).
\tag{11}
$$
它没有使用 $u=f\cos\theta+g\sin\theta$；圆只是在其应用中选择的一条轨道。

相应 ruling 改变为
$$
\Delta\mathscr K
=\mathcal B_u(w)-\mathbf w\cdot\mu(w,w)
-2\mathbf w\cdot\mu(u,\chi).
\tag{12}
$$
原二阶矩阵沿偶端芽写成
$$
\mathsf m=\mathsf m_*+\mathsf o,\qquad
\mathsf o(-\sigma)=-\mathsf o(\sigma).
$$
R221 的完整局部 $\mathcal T_\sigma$ 为奇函数。R224(9)–(10)因此准确给
$$
\operatorname{Ev}\mathcal B_u(w)
=\mathbf w\cdot\left[
-2\mu(\Phi_{\mathsf m_*}D,w)
+4\mu\{u,\Phi_{\mathsf m_*}(u,w)\}
\right].
\tag{13}
$$
R224 明确先对任意紧 w 证明(13)，没有预先要求它单独保持第三 ruling。因此这里也不会把“canonical 第三尚待 w 修正”误当成排除全部 w 的附加假设。

三矩(7)使 $w_*=\Phi_{\mathsf m_*}D$ 真紧。原 R224(21)–(22)的中心比较同时保留第二初值、第三初值及其平方项：
$$
Z=\widehat Z-Y_{w_*},\qquad
U=\widehat U+2\widehat Z(u,w_*)+Y_{\chi_*}.
\tag{14}
$$
$\chi_*$ 不必左紧；原单紧外槽 u 的 ruling 配对仍是
$\mathbf w\cdot\mu(u,\chi_*)$。这个真实尾正是原比较中的一部分。

所以全部原传入历史、(12)中的 gauge 平方、第三齐次项，以及任意合法二阶 gauge 的偶部，都只改变
$$
\mathcal W_e
=\operatorname{span}\{h,\sigma^2,(1+j^2)/h\}.
\tag{15}
$$
[R243](R243-finite-jet-criterion-for-the-complete-even-exceptional-ruling.md)(2)在本稿只是逐参数使用上述比较；没有使用其五个圆谐波分解或有限相位试空间。

完整第四 ruling 因而必迫中心模型落入(15)。R249 的同中心 Gaussian 词独立性把其零层、一层和两层准确分开；(15)属于零字层。所有本稿所用一层、二层系数必须各自为零。不能以一个共同 w 在 period 上有用为由，让它改变这些偶部系数。

## 4. 全部第四条件如何迫三个 directed 行与两个一层行

沿 R387 定义
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},\qquad
W=aR+bS,\quad Z=d_ZL+e_ZU,
$$
$$
\begin{aligned}
t&=\kappa^2,\qquad D_*=51t^2+2t+8,\\
a&=-\frac{D_*}{64h_e^2},&
b&=-\frac{17t^2+4t}{32h_e^2},\\
d_Z&=\frac{6\kappa^3}{h_e},&
e_Z&=-\frac{\kappa(15t+1)}{4h_e},&
c_P&=-\frac{\kappa(41t^2+27)}{216h_e^3}.
\end{aligned}
\tag{16}
$$
所有需要除的 $a,d_Z,c_P$ 在 $\kappa\ne0$ 时非零；另有
$$
a+3b=-\frac{153t^2+26t+8}{64h_e^2}\ne0.
$$
三个 Gaussian 方向为 $B_{-3}=c_PP$、$B_{-2}=W$、$B_{-1}=Z$。

对真实 whole 槽，置
$$
H_m^X=-I_m(XD,PD)+2I_m\{u,X(u,PD)\},\qquad m=0,1,2.
\tag{17}
$$
这里 $I_m$ 是(5)的三个双线性型，特别 $I_2$ 保留 $2\int u'v'$。

为明确必要性，定义一般两个方向的 directed 量
$$
H_m^{X\to Y}=-I_m(XD,YD)+2I_m\{u,X(u,YD)\}.
$$
原混合对称二层给
$H_m^{X\to Y}+H_m^{Y\to X}$；原反对称面积给
$H_m^{X\to Y}-H_m^{Y\to X}$，其规范的共同非零常数不影响零条件。第3节的真词独立性先把这两种函数分开，再由(6)的三列独立性分开三个外矩。因此它们共同为零确实迫每一个 directed 量为零。

特别完整第四必要条件包括
$$
\boxed{
F_0=H_2^P=0,\qquad
F_1=aH_1^R+bH_1^S=0,\qquad
F_2=d_ZH_0^L+e_ZH_0^U=0,
}
\tag{18}
$$
及原 $WP$ 面积三个外矩
$$
I_m\{u,[W,P](u;D)\}=0.
\tag{19}
$$
没有只从对称乘积删除一个 directed 量，也没有把一个未经证明的充分控制行升级为必要条件。

原完整 $E_{-3}$ 一层记为 $\mathscr R_{-3}(u,D)$，它由 R296(完整 local、chain、elementary history)给出。定义
$$
\mathscr R_0=[\sigma h^{-2}j^0]\mathscr R_{-3},
\qquad
\mathscr R_4=[\sigma h^{-2}j^4]\mathscr R_{-3}.
\tag{20}
$$
这里是原有限 Laurent/多项式呈示的两个准确系数，不是只观察两个 Taylor jets。完整一层为零必迫
$$
\boxed{\mathscr R_0=\mathscr R_4=0.}
\tag{21}
$$

R311§1(4)已明确：原 local 与 directed 式是任意固定 $(u,D)$ 的逐参数身份，无轨道导数。本稿进一步使用 R325 的一般 mixed 身份，而不是沿用 R311 仅在 rank-one 包上的最后求和。

## 5. 一般 mixed 两行：不使用圆、不除以 P(t)

置
$$
p=f',\quad q=f'',\quad v=u',\quad r=u'',\quad d_0=q^2-r^2,
$$
$$
D_4=\int d_0^2,\qquad
C=\int r^2d_0,\qquad
\mathcal J=\int(vq-pr)\,rq',\qquad
E=\frac{14}{3}C+8\mathcal J.
\tag{22}
$$
$D_4$ 是实际非负积分，不是对称槽 D。

以下给出 R325 消元为何不依赖轨道为圆。由原
$$
\mathfrak H(u;f,f)''=(A_fr)'-V_fv,\qquad V_f=6(qq')',
$$
用紧 v 作真实全区间分部积分，(9)给
$$
6\int vrqq'-3\int pr^2q'+\int q^2r^2=0.
\tag{23}
$$
这直接推出
$$
Y_0:=\int vr\,d_0'=-\frac23C-2\mathcal J,
$$
$$
B_0:=\int pq\,d_0'=-\frac23(D_4+C)-2\mathcal J.
\tag{24}
$$
未对 $p$、$q$ 或 $r$ 作除法，所以零点和退化开段都保留。

弱 hook 使 $[W,P](u;D)$ 的完整原式归为非零倍数的 $J(rd_0)$。其第1外矩准确是
$$
I_1\{u,J(rd_0)\}
=\frac12\left(C-\int xr^2d_0'\right).
$$
故(19)给
$$
Z_0:=\int xr^2d_0'=C.
\tag{25}
$$
真实左常尾仍保留；这里只对紧 r 作分部积分。

再记 $X_2=\int x^2(q^2)'d_0'$、$T_1=\int xpq'd_0'$。原四行保持 R325(10)的全式：
$$
\begin{aligned}
H_2^P&=-X_2-4Z_0+4Y_0-2D_4,\\
H_1^R&=-X_2+2T_1-Z_0+2Y_0+C,\\
H_1^S&=-X_2-2Z_0+\tfrac12D_4,\\
H_0^U&=-\tfrac32X_2+2T_1-2Y_0+Z_0+2B_0+D_4-C.
\end{aligned}
\tag{26}
$$
原变分所用 $P(f,f)$ 可以有真实左尾。其关键尾积分是
$$
\int d_0'P(f,f)=\int d_0q^2,
$$
因为紧的是 $d_0$，不需要把 $P(f,f)$ 假置为紧。

令
$$
\rho=\frac ba=\frac{2t(17t+4)}{D_*}.
$$
由(18)、(24)–(26)，准确得到
$$
\boxed{
H_1^S=\frac52D_4+E,\qquad
H_0^U=\frac23D_4+E-\rho H_1^S,
}
\tag{27}
$$
$$
H_1^R=-\rho H_1^S,\qquad
H_0^L=-\frac{e_Z}{d_Z}H_0^U.
\tag{28}
$$

原 R325 第零行和 R387 第四行分别为
$$
\frac{\mathscr R_0}{c_P}
=K_\kappa H_0^U+\kappa^3\left(\frac5{16}D_4+\frac E8\right),
\qquad K_\kappa=-\frac{1+15t}{96\kappa},
$$
$$
\frac{\mathscr R_4}{c_P}
=\frac{\kappa}{16}(-4H_0^L+2H_0^U+H_1^R).
\tag{29}
$$
第一个等式在三 F 为零后才使用；原未置零形式中的各 F 系数并未被悄悄丢弃。第二个等式的 local 无 $j^4$ 由 R387 对 R221 全18项逐幂支付，没有仅取 principal。

定义
$$
\begin{aligned}
N(t)&=16+184t-1713t^2-2475t^3-4590t^4,\\
P(t)&=8+114t-169t^2+231t^3-612t^4,\\
A_*(t)&=16-8t+39t^2+1071t^3,\\
B_*(t)&=8+18t+47t^2+255t^3 .
\end{aligned}
$$
直接代(27)–(28)到(29)，得到两个没有 $P$ 分母的完整身份：
$$
\boxed{
\frac{\mathscr R_0}{c_P}
=-\frac{N(t)D_4+3P(t)E}{288\kappa D_*},
\qquad
\frac{\mathscr R_4}{c_P}
=-\frac{A_*(t)D_4+3B_*(t)E}{288\kappa D_*}.
}
\tag{30}
$$
这两个式子在任意 $t>0$ 有定义。即使 $P(t)=0$，没有损失一个真实方程或引入极限。

## 6. 无分母正组合；任意非零共振参数

R387 的准确多项式恒等为
$$
A_*P-B_*N=66t^2K(t),
$$
$$
K(t)=96+848t+3314t^2+7101t^3+16218t^4+7803t^5.
\tag{31}
$$
其全部系数为正。由(30)，消 E 而不除 P：
$$
\boxed{
P(t)\mathscr R_4-B_*(t)\mathscr R_0
=
\frac{11\kappa^4(41t^2+27)K(t)}
{10368h_e^3D_*(t)}\,D_4.
}
\tag{32}
$$
右边系数对每个 $\kappa\ne0$ 严格正，与 $\kappa$ 的符号无关。

所以在(7)、(9)、(18)、(19)及两个完整一层零式(21)下，
$$
\boxed{
D_4=0,\qquad (u'')^2=(f'')^2\quad\text{逐点}.
}
\tag{33}
$$
从积分到逐点使用真实连续密度非负，未用数值下界或只在若干点抽样。

本稿不要求先定义 $\Psi$ 或要求它作为独立假设为零。在 R387 的小 t 范围，$P>0$，(30)的第一式与三 F 一起等价于旧 $\Psi=0$；(32)是保留原两行以后的更稳直接消元。在 $P=0$ 或其符号改变处，原两行仍直接给(33)。

注意这是条件于实际存在(2)的结论。R241/R354 通过联合 IFT 安装的是其已付小参数邻域；本文没有把该安装扩大到任意大 $\kappa$。若另一实际几何恰有大参数的(2)，同样受(32)约束。

## 7. 连续路径只能保持原首阶 profile

现在对每个 $\tau\in\mathcal A$ 应用(33)。

固定一个 x。若 $f''(x)=0$，则 $u_\tau''(x)=0$ 对全部参数成立。若 $f''(x)\ne0$，则
$$
\frac{u_\tau''(x)}{f''(x)}\in\{-1,1\}.
$$
这是真实连通参数空间到离散两点集的连续映射，所以是常数。由种子 $u_{\tau_0}=f$，这个常数为1。因此
$$
u_\tau''(x)=f''(x)
\quad\text{对全部 }x,\tau.
\tag{34}
$$
对每个 $\tau$，$u_\tau-f$ 是一个仿射函数。共同零 collar 使其两个仿射常数准确为零，故
$$
\boxed{u_\tau\equiv f\qquad(\tau\in\mathcal A).}
\tag{35}
$$

这证明：

**定理。** 在第1节实际几何与固定目标上，任意首阶 profile 到二阶 jet 连续、从 f 出发的连通轨道，只要逐参数通过本稿完整必要子系统，就恒为 f。特别，任何具有原完整四阶恢复的这种轨道都必须恒定。

单独对某个不与 f 连续连接的 profile，(33)只给二阶导数的逐点符号选择；本文没有将这些孤立可能性全部误称为相同 profile。正是参数连续性与指定种子排除了沿非零 $f''$ 改换符号。也没有假设 $f''$ 的零点有限、活动区间有限或 profile 解析。

非圆、椭圆、任意有限或无限 Fourier 轨道、形状随参数变化的路径，只要属于这个固定对象的连续首阶类，均不能靠离开旧 rank-one 包空间修复。这是对 R311 的实质扩展：其固定包求和在这里被完整 mixed 的非负积分(32)替代。

## 8. 与旧有限构造及后续机制的边界

R354–383 的同一个弱圆确实能够通过此前已列的18面积、十个对称乘积、三条 directed、$\Psi$及完整第三条件。R387 已证明它随后失败于另一个完整一层系数；本稿不撤销其中任何有限构造。

新增结论也不是依赖某个特定编码的失败。它只使用同一已安装 $M=0$、$T=\kappa_H\mathfrak H$、共振 Gaussian 端芽，以及原完整低阶/第四必要接口。把同一首阶轨道改成一般连续路径，并不能避开这组身份。

仍未被本文判断的包括：

- 从几何初始设计改用不同真实端芽；
- 改变原第三算子而非继续 $T=\kappa_H\mathfrak H$；
- 不属于当前固定目标、共同紧 profile 和首阶轨道规范的其他机制；
- 首阶 profile 恒定、实际变化直到更高阶才出现的族，以及完整主课题的全时有限等距、嵌入、reach 等要求。

R184 的原 joint period/ruling 条件与全部合法 gauge 已在必要性中保留。本文并不是因为尚未支付 period 就拒绝一个可能的 gauge；它证明不论这些 gauge 如何选，(32)都留在不能被它们改变的偶部原函数字系数中。

这里没有继承另一旧几何的 universal wholeE、Morse 或任何有限通量控制。若后继选择新端芽/新第三算子，必须从真实路径、端口与原目标重新支付相应接口，不能把两条不相同几何上的已付条件拼成一个解。
