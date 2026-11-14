# R32：真实 C3 相位、C2 无穷小场与非退化二阶恢复障碍

日期：2026-11-14。完整证明；已独立复核一般 h 的点态因子与周期积分密度。这里分别核对 profile、公开无穷小场 $Y$ 和线性校正场 $Z$ 的正则性；不把它们混称为一个已经存在的有限 $C^2$ 族。

## 1. 通用简单 C 根定理延伸到 3<rho<4

沿用 [R26](../results/R26-generic-D0-simple-root-phase-opening.md) 的记号、显式 jet 和非退化量 $\mathcal K$。将比值条件改为

$$C(x_0)=0,\quad \gamma=C'(x_0)\ne0,\qquad
R=\frac{W(x_0)}\gamma\in\left(-\frac54,-\frac12\right),
\qquad\mathcal K\ne0.\tag{1}$$

定义

$$\rho=\frac{1+\sqrt{9-32R}}2\in(3,4),\qquad
\sigma=\rho-3\in(0,1).$$

R26 的零至三阶 jet 构造仍合法：$A_2=\gamma(1-R)$、$W=\gamma R$、$2W+\gamma=\gamma(2R+1)$ 都不为零。它给
$L=L'=0$、$L''=-\gamma f'''$ 和 $\ell=-\gamma f'''/2\ne0$。

**局部存在引理。** 存在真实实解析基底 $f$，并且对每个固定复数 $\eta$，缩短区间后存在实际正侧解

$$q(x_0+t)=f(x_0+t)+\chi(t),\qquad
\chi(t)=t^\rho\{\eta+O(t^\sigma)\},\quad t>0,\tag{2}$$

满足 $Q[q]=0$。差的前四阶导数具有相应逐项渐近。把 $\chi=0$ 定义在 $t\le0$，得到全局局部 $C^3$ 解；若 $\eta\ne0$，第四阶导数在正侧通常按 $t^{\rho-4}$ 发散。

**证明。** 实基底的 Fuchs 谱仍为

$$-4,-3,\rho-4,-3-\rho,$$

现在四个实部全负，R26 的解析 $O(t)$ 收缩原封不动适用。横向 indicial 多项式仍为
$\ell r(r-1)(r-\rho)(r+\rho-1)$。

写 $\chi=t^\rho v$、$v(0)=\eta$。除以 $t^{\rho-2}$ 后，非线性项具有因子 $t^\sigma$；最高 Euler 导数系数趋于 $\ell\ne0$。令
$V=(v-\eta,\theta v,\theta^2v,\theta^3v)$，则

$$\theta V=J_\rho V+G(t,V),\qquad
\operatorname{spec}J_\rho=\{0,-\rho,1-\rho,1-2\rho\},$$

且在有界 jet 球内

$$G=O(t^\sigma),\qquad D_VG=O(t^\sigma).$$

使用连续函数的权范数 $\sup|V(t)|/t^\sigma$ 和

$$V(t)=\int_0^1s^{-J_\rho-1}G(st,V(st))\,ds.$$

因为 $\sigma>0$ 且 $J_\rho$ 最大实部为零，核
$\int_0^1\|s^{-J_\rho}\|s^{\sigma-1}\,ds$ 有限。缩短区间后得到自映射和收缩。Euler 系统给前四个 Euler 导数的相同余项估计，因此

$$\chi^{(j)}(t)=\eta(\rho)_j t^{\rho-j}
+O(t^{\rho+\sigma-j}),\qquad0\le j\le4.\tag{3}$$

零至三阶均趋零，所以拼接为 $C^3$；第四阶的首项在 $\eta\ne0$ 时非零并发散。它仍局部可积，因为 $\rho-4>-1$，故拼接不产生第四阶分布导数的 Dirac 项。证毕。

若 $\operatorname{Im}\eta\ne0$，这是一个真实的复相位开启。满秩 $B_j$ 情况下可像 R26 一样选局部积分常数，使 $O,O',O''$ 在锚点为零。由于 $q'''$ 连续、$q^{(4)}$ 局部可积，$O''$ 绝对连续，$Q=O'''=0$ 跨过接点仍成立；这里没有隐蔽的跳跃源项。局部常数仍不是完整右尾。

## 2. 逐阶核对 Y：C3 profile 的确给 C2 无穷小场

在固定紧物理带上，$u$ 和 $\xi=h/u-\omega$ 之间为光滑坐标变换，$u$ 不为零。公开公式准确写成

$$Y_\phi=U\phi(\xi)+V\phi'(\xi),\qquad
U=uB,\quad V=-\frac{uT+wB}{2h},\quad w=h^2-ku.\tag{4}$$

这里 $V$ 是曲面法向方向：它与 $N$ 以及 $wT-uB$ 都正交，且从不为零。不能把 $V$ 当成切向量。

对任意曲面坐标方向 $i,j$，完整的一、二阶链式公式为

$$Y_i=U_i\phi+(U\xi_i+V_i)\phi'+V\xi_i\phi'',$$

$$\begin{aligned}
Y_{ij}={}&U_{ij}\phi
+(U_i\xi_j+U_j\xi_i+U\xi_{ij}+V_{ij})\phi'\\
&+(U\xi_i\xi_j+V_i\xi_j+V_j\xi_i+V\xi_{ij})\phi''
+V\xi_i\xi_j\phi'''.
\end{aligned}\tag{5}$$

因此 (2) 的差场满足

$$Y_\chi=O(t^{\rho-1}),\qquad
dY_\chi=O(t^{\rho-2}),\qquad
d^2Y_\chi=O(t^{\rho-3})\longrightarrow0.$$

它可与负侧零场作 $C^2$ 拼接。这个结论准确限于无穷小场 $Y$；它没有支付下一阶校正的正则性。

## 3. 二阶恢复会出现额外的 q″ 项

本节使用本题已经证明的完整 range 公式。取真实实解析基底 profile $f$ 和 (2) 的开启差 $\chi$，令

$$\Delta H=dY_{f+\chi}\cdot dY_{f+\chi}-dY_f\cdot dY_f.$$

点积为复双线性点积。假设所用局部积分常数使完整周期相容成立，并把差的法向坐标分量 $\Delta r$ 在 $\xi=x_0$ 锚定为零；这对应左右校正匹配同一基底。记

$$D_s=\partial_s|_\xi,\quad c=D_su,\qquad
\mathcal R=Y_{f,u}\cdot V.$$

这里 $D_s$ 是沿固定渐近叶的导数，不是已为零的周期系数 $D$。

**校正正则性引理。** 令

$$\mathcal S_1=
\frac{D_sY_f\cdot D_sV+(wk-u)\mathcal R-cD_s\mathcal R}{u^2},\tag{6}$$

在固定的 $s_0$ 起取原函数 $P_s=\mathcal S_1$，再定义

$$G=P-\frac{D_sY_f\cdot V-c\mathcal R}{u^2}.\tag{7}$$

则自然 range 恢复所得差校正在相位点的奇异主项为

$$\Delta Z=-G(s,x_0)V(s,x_0)\chi''(\xi-x_0)
+Z_{\mathrm{reg}},\qquad Z_{\mathrm{reg}}\in C^2.\tag{8}$$

齐次 profile gauge 只能改变 $G(s,x_0)$ 的一个与 $s$ 无关的常数。因此，在保持同一左侧基底校正的这类恢复中，可消去 (8) 的第四阶爆发并获得 $C^2$ 拼接，当且仅当

$$\partial_sG(s,x_0)=0\quad\hbox{对所有 }s.\tag{9}$$

完整周期条件在这一阶只给 $\oint\partial_sG\,ds=0$，不等于 (9)。

**证明。** 第一条 range 方程为 $2\Delta r_u=\Delta H_G$。将 (4) 求 $u$ 导数，最高 profile 导数项为 $V\xi_u\chi''$。因此跨相位点积分并作一次分部积分，得到

$$\Delta r=\mathcal R\chi'+R_3,\qquad R_3\in C^3.\tag{10}$$

这里线性交叉项的其余部分是光滑系数乘 $\chi$ 或其积分；纯平方项积分的最低阶为 $t^{2\rho-3}>t^3$。这些项及其前三阶导数具有所需连续极限，故所写的 $C^3$ 余项确实成立。沿 $s$ 求导只微分光滑系数，不再增加 profile 导数。

完整 adapted range forcing 是

$$\mathcal S=\frac{\tfrac12|D_sY|^2+(wk-u)r-cD_sr}{u^2}.$$

于是 (10) 给

$$\Delta\mathcal S=\mathcal S_1\chi'+S_3,\qquad S_3\in C^3.$$

令 range 变量 $\mathcal W=\zeta/u^2$，$\zeta=wp-uq$。沿 $s$ 积分得

$$\Delta\mathcal W=P\chi'+W_3,\qquad W_3\in C^3,$$

从而

$$\Delta\zeta_u=-hP\chi''+C^2\text{ 余项},\tag{11}$$

其中用到了 $\xi_u=-h/u^2$。$P$ 在 $x_0$ 周期，因为 (6) 的全周期积分等于 $L[f](x_0)=0$；其在邻近 $\xi$ 的非周期部分也可并入余项，因为 $L[f]=O((\xi-x_0)^2)$。完整的 $\Delta\mathcal W$ 本身按假设周期。

另一个 range 变量为

$$\mathcal A=H_F-r_s|_u
=H(D_s,\partial_u)-c r_u-D_sr.$$

利用 (10)，其差的最高项准确是

$$\Delta\mathcal A
=(D_sY_f\cdot V-c\mathcal R)\xi_u\chi''
+C^2\text{ 余项}.$$

恢复式 $\eta=(\mathcal A-\zeta_u)/2$ 因而给

$$\Delta\eta=\frac h2G\chi''+C^2\text{ 余项}.$$

再使用
$p=(\zeta+u\eta)/h^2$、$q=\eta-kp$，得到向量主项

$$\frac{G}{2h}(uT+wB)\chi''=-GV\chi''.$$

将平滑系数在 $\xi=x_0$ 取值只改变一个 $C^2$ 余项，因为
$(\xi-x_0)\chi''$ 的二阶导数为
$2\chi'''+(\xi-x_0)\chi^{(4)}\to0$。这证明 (8)。

当法向坐标锚相同时，全部齐次自由度为
$\Delta\mathcal W\mapsto\Delta\mathcal W+g(\xi)$，其向量场正是 $Y_{-g}$。
要消去 (8) 的非 $C^2$ 主项，可在一个 $s$ 点选择 $g=-G(s_0,x_0)\chi'$；在其余 $s$ 点仍留下
$-\{G(s,x_0)-G(s_0,x_0)\}V\chi''$。由于 $V\ne0$ 且 (3) 的 $\chi^{(4)}$ 真正发散，它不能属于 $C^2$，除非 $G(s,x_0)$ 恒定。反之，恒定时该 gauge 准确消掉唯一的非 $C^2$ 主项，其余项的二阶 jet 在相位点为零，给所需拼接。证毕。

等价地，将 (7) 求 $s$ 导数，可直接检查待付的点态条件为

$$\partial_sG
=-\frac{(D_s^2Y_f-2(c/u)D_sY_f)\cdot V}{u^2}
+\left\{\frac{wk-u}{u^2}+D_s\left(\frac c{u^2}\right)\right\}\mathcal R.\tag{12}$$

这是真实逐点条件，不是把其积分均值投影掉。它没有被 R26 的两个退化 jet 条件自动支付。

## 4. 一般 h 的点态门与非退化相位不相容

本节不再要求 $h$ 恒常，只要求原几何的 $h>0$ 和周期条件成立。结论因而同时覆盖 [R31](../results/R31-closed-geometry-negative-physical-root-and-local-phase.md) 的恒 $h=1$ 构造。

**二阶恢复障碍。** 若 $M=L|_{\mathcal P_2}$ 可逆，则 §1 的归一化非退化开启不能满足 (9)。因此这些真实局部 $C^3$ profile 和 $C^2$ 无穷小场，不能经 §3 的同左锚、自然 profile 二阶恢复得到与原实解析基底匹配的 $C^2$ 校正。这个结论保留 §3 已允许的全部 $s$ 无关齐次 profile gauge。

**证明。** 固定相位坐标 $x=x_0$，并在一般变量 $\xi$ 下记

$$z=\xi+\omega,\quad e=hz-k,\quad u=h/z,\quad w=ue,\qquad
z_s=\frac{k_s}{2h},\quad e_s=h_sz-\frac{k_s}{2},\quad
c=\frac{h_s}{z}-\frac{k_s}{2z^2}.$$

定义实际的二次多项式密度

$$\begin{aligned}
\mathscr K(s,\xi)
&=\frac{wk-u}{u^2}+D_s\left(\frac c{u^2}\right)\\
&=kz^2-\frac{k^2+1}{h}z-D_s^2(z/h).
\end{aligned}\tag{13}$$

于是 $\mathscr K_\xi=2kz-(k^2+1)/h-D_s^2(1/h)$，并且
$\mathscr K_{\xi\xi}=2k$。

令 $f_j=f^{(j)}(x)$，$j=0,1,2$；这些是固定的 profile jet 数，均不依赖 $s$。记 $\mathscr J=D_s^2-2(c/u)D_s$，并令下列几何量在 $\xi=x$ 取值。由 $U=uB$、$V=-(T+eB)/(2z)$ 和框架微分式，得到

$$\begin{aligned}
D_sU&=cB+uN,\\
\mathscr J U&=-kuT+(c_s-u-2c^2/u)B,\\
D_sV&=\frac{z_s}{2z^2}T-\frac h2N+
\left\{\frac{(e+hz)z_s}{2z^2}-\frac{h_s}{2}\right\}B.
\end{aligned}\tag{14}$$

在固定 $s$ 下对 $u$ 求导，还得到

$$\mathcal R=R_0f_0+R_1f_1+R_2f_2,\qquad
R_0=-\frac e{2z},\quad
R_1=\frac{1+e(hz+e)}{4hz},\quad
R_2=-\frac{1+e^2}{4h}.\tag{15}$$

将 (14) 代入 (12)，分别比较 $f_0,f_1,f_2$ 的系数。前两项准确化为

$$-\frac{(\mathscr J U)\cdot V}{u^2}+\mathscr K R_0
=-\frac{k(1+e^2)}{2h},$$

$$-\frac{(\mathscr J V)\cdot V}{u^2}+\mathscr K R_1
=\frac{1+e^2}{4h}\mathscr K_\xi.$$

第一式可直接把
$u^2\mathscr K=kue+c_s-u-2c^2/u$ 代入。为明确第二式的导数相消，暂记

$$p=z_s,\quad g=h_s,\quad
Q_e=1+e^2,\quad L_0=Q_e+ehz,\quad
P=p_s-\frac{2gp}{h},\quad H=-h_{ss}+\frac{2g^2}{h}.$$

将 (14) 再求一次 $D_s$，并使用 $e_s=gz-hp$、$e_{ss}=h_{ss}z-hp_s$，得到

$$-\frac{(\mathscr J V)\cdot V}{u^2}
=\frac{L_0P}{4h^2z}+\frac{ezH}{4h^2}+\frac{z^2}{4},\qquad
\mathscr K=kz^2-\frac{k^2+1}{h}z-\frac Ph-\frac{zH}{h^2}.$$

加上 $\mathscr K R_1=\mathscr K L_0/(4hz)$ 后，$P$ 项准确消去，$H$ 项等于 $-Q_eH/(4h^3)$。剩余部分用恒等式

$$h^2z^2+L_0(ke-1)=Q_e(2khz-k^2-1)$$

化成 $Q_e\mathscr K_\xi/(4h)$，证明第二式。$f_2$ 的系数则直接是 $\mathscr K R_2$。因此得到一般的点态恒等式

$$\boxed{\quad
G_s(s,x)=\frac{1+e^2}{4h}
\left[-2k f_0+\mathscr K_\xi(s,x)f_1-\mathscr K(s,x)f_2\right].
\quad}\tag{16}$$

特别地，当 $h=1$、$\omega=k/2$ 时，
$\mathscr K=kx^2-x-k^3/4-k/2-k_{ss}/2$、
$\mathscr K_\xi=2kx-1$。这恢复可直接由 $k_s,k_{ss}$ 展开检查的恒速公式。

现在取与 $f$ 在 $x$ 具有**零、一、二阶 jet** 的二次多项式

$$P_2(\xi)=f_0+f_1(\xi-x)+\frac{f_2}{2}(\xi-x)^2.$$

对每个固定 $s$ 定义

$$E_s[P_2](\xi)=-2kP_2(\xi)+\mathscr K_\xi(s,\xi)P_2'(\xi)
-\mathscr K(s,\xi)P_2''(\xi).\tag{17}$$

因为 $\mathscr K_{\xi\xi}=2k$、$P_2'''=0$，逐项微分恰给

$$\partial_\xi E_s[P_2]
=-2kP_2'+2kP_2'+\mathscr K_\xi P_2''
-\mathscr K_\xi P_2''=0.\tag{18}$$

因此 $E_s[P_2]$ 对 $\xi$ 恒常。若点态门 (9) 成立，(16) 中 $(1+e^2)/(4h)>0$ 给 $E_s[P_2](x)=0$，从而对每个 $s$ 和每个 $\xi$ 都有 $E_s[P_2](\xi)=0$。

完整积分式的来源也可逐项核对。由 [六项 Volterra 公式的 §5](../notes/literature-volterra-polynomial-20261114.md)，记 $d=h\omega-k$，三个尾矩系数为

$$B_0=\frac18\oint\mathscr K\frac{d^2+1}{h}\,ds,\qquad
B_1=\frac14\oint\mathscr Kd\,ds,\qquad
B_2=\frac18\oint\mathscr Kh\,ds.$$

这里保留 $\mathscr K$ 中的二阶 $s$ 导数；若改成只含一阶导数的版本，所需操作是
$\oint a\{-D_s^2(z/h)\}\,ds=\oint(D_sa)D_s(z/h)\,ds$，周期端项为零。由 $e=d+h\xi$、$C=B_0+\xi B_1+\xi^2B_2$、$W=B_1+2\xi B_2$，以及同文的 $A_1$ 密度，立刻得到一般 $h$ 的实际积分式

$$\begin{aligned}
A_1(\xi)&=-\frac12\oint\frac{k(1+e^2)}h\,ds,\\
C(\xi)&=\frac18\oint\mathscr K(s,\xi)\frac{1+e^2}h\,ds,\qquad
W(\xi)=\frac14\oint\mathscr K(s,\xi)e\,ds.
\end{aligned}$$

由 $e_\xi=h$ 和 [R7](../results/R7-nine-coefficients-and-polynomial-profiles.md) 已证几何恒等式 $A_2=C'-W$，进一步得到

$$2A_2(\xi)=\frac14\oint\mathscr K_\xi(s,\xi)\frac{1+e^2}h\,ds.$$

故完整的固定系数一元算子 $L=A_1+2A_2\partial_\xi-2C\partial_\xi^2$ 满足

$$L[P_2](\xi)=\oint\frac{1+e^2}{4h}
E_s[P_2](\xi)\,ds\equiv0.\tag{19}$$

沿 $s$ 积分后，这里的多项式系数都是固定实数；不是在每个 $s$ 另选一个不同的算子或二次式。既然 $M=L|_{\mathcal P_2}$ 可逆，(19) 强制 $P_2\equiv0$，与 §1 的归一化 $f_0=1$ 矛盾。证毕。

在简单 $C$ 根上，R31 的精确关系

$$\mathcal K_{\mathrm{jet}}=-\frac{\det M}{4A_2W}$$

说明这里的矩阵条件与通用相位定理的非退化条件完全一致，因为所用比值区间内 $A_2W\ne0$。所以不能通过改变 $s$ 原函数的基点，或增加 §3 的 $s$ 无关 gauge，来同时保留该非退化相位和 $C^2$ 二阶校正。

该结论不需要闭合中心曲线、嵌入或 reach 假设；它是沿完整周期球面框架的点态恢复障碍。它也没有否定 R31 的局部 profile 存在定理，更没有把一条一般连续 $C^2$ 有限族擅自提升为在参数上二次可微的族。

## 5. 实际系数与剩余全局问题

高频 Klein 闭合构造的同一协议也能把 (1) 的比值区间放进实际几何：取其极限参数

$$a=20,\quad e_*=1/2,\quad D_{\mathrm{energy}}=1845/2.$$

其简单正根上准确有

$$C'=247/8,\qquad W=-1107/32,\qquad W/C'=-1107/988
\in(-5/4,-1/2).$$

非对称高频扰动的行列式首项仍为正，有限曲线的空间闭合仍由 Klein 旋转和精确给出。因此局部 $C^3$ profile 及其 $C^2$ 无穷小场的门不是任意形式系数假设。但 §4 已证明：所有这里的非退化分支都不能同时满足 (9)，改变 $h$ 也不能消除这个障碍，所以在 §3 所指定的同左锚恢复中，二阶校正并非 $C^2$。

此外，两个简单四阶外尾仍保护各自最近的内部 $C$ 根，使那里的 $L\ne0$。所以这个简单 $C$ 根的局部开启不能直接插入那一对外尾。真正剩余的仅 $C^3$ 全局逃逸还要研究 $C\ne0$ 且 $L$ 更高退化处的动力学，或改变外端类别，并同时核对完整校正的空间正则性。

本引理只给局部存在和一个明确的二阶 $C^2$ 门，不宣称有限参数的 $C^2$ 弯曲一般不可能。尤其，没有假定任意连续有限族必在参数上具有值于 $C^2$ 空间的二阶 Taylor 展开。
