# R698　从实际纬圈切向消去一行闭性与全部自由中心斜率

[R687](R687-global-darboux-frames-with-quantitative-periodic-immersion-reconstruction.md) 的一般标架可以精确降到一张单位切向 $T$ 和一个有符号标量 $a$。径向目标 $E$ 可在设计时求出，冻结后作为同一函数固定。以下变换在真实解上等价；从任一已付未解态进入时，除了保持原 $T$，还给出改变中心和径向列的精确式。本文不重复运行原方程。

## 一　正交纬圈迫使角切向导数不为零

用 $r_0=.075,r_1=.22$ 区别于未知场 $a$。在材料环上取 $D=F_r,T=F_\varphi/r$，目标 $g=E(r,\varphi)\,dr^2+r^2d\varphi^2$，$e=\sqrt E>0$。真解的 $|T|=1,D\cdot T=0$。由 $D_\varphi=T+rT_r$，
$$
 D\cdot T_\varphi=-D_\varphi\cdot T=-1,\qquad v=|T_\varphi|\ge 1/e>0 .       \tag{1}
$$
设 $U=T_\varphi/v,\ B=T\times U$。则 $(T,U,B)$ 是正交架，唯一的有符号量 $a=D\cdot B$ 给出
$$
 D=-U/v+aB,\qquad E=v^{-2}+a^2 .                                           \tag{2}
$$
允许 $a$ 为任意符号及穿越零。分母只用 $v$；在未解态需实查 $\inf v>0$，真解则已有 (1)。原角曲线的法曲率可为零。

反过来，给定正则单位 $T$ 和有符号 $a$，由 (2) 左式定义 $D$，令 $G=D_\varphi-T-rT_r$。对任意这样的试场，$D\cdot T=0,D\cdot T_\varphi=-1$，所以 $G\cdot T=0$ 准确成立。设 $w=U_\varphi\cdot B$，则 $U_\varphi=-vT+wB, B_\varphi=-wU$，两条独立闭性方程为
$$
 rT_r\cdot U=v_\varphi/v^2-a w,\qquad
 rT_r\cdot B=a_\varphi-w/v .                                               \tag{3}
$$
它们与 $G=0$ 完全等价，不舍弃第三个原方程的任何非零方向。再施加一个标量 $v^{-2}+a^2=E$ 以完成正确的径向度量。采用未除 $a$ 的形式使两平接圈也可直接处理。上式 $w$ 的点态展开用于 $T$ 二次角可微、$a$ 一次角可微的场。一般仅有 $C^2$ 的真实浸入仍逐点满足 (1)–(2) 及 $D_\varphi=T+rT_r$；此时直接以连续的真实 $D_\varphi$ 作正交投影，不凭空要求 $F_{\varphi\varphi\varphi}$。对更低正则的试场须把 $D_\varphi$ 以保守弱式处理；这里的有限角—样条候选在每个所用角方向光滑。

## 二　整圈位置、真实内平移与全域误差

以 $\overline f=(2\pi)^{-1}\int_0^{2\pi}f\,d\varphi$，$I=\partial_\varphi^{-1}(1-\overline{\phantom{x}})$ 取零均值原函数。外圈中心为零，定义
$$
 C'(r)=\overline D(r),\quad C(r)=-\int_r^{r_1}\overline D(s)\,ds,
 \qquad F=C+rIT.                                                           \tag{4}
$$
于是任意试场的实际偏差恰有
$$
 F_r-D=-IG,\qquad F_\varphi/r-T=-\overline T,\qquad
 r\overline T(r)=\int_r^{r_1}\overline G(s)\,ds .                      \tag{5}
$$
最后一式使用已知外平圈 $\overline T(r_1)=0$。若 (3) 与 (2) 的标量行成立，则 (5) 给 $F_r=D,F_\varphi=rT$，且 $F$ 为所求度量的局部浸入。反射 $S=\operatorname{diag}(1,-1,1)$ 下有 $T(r,-\varphi)=-S T(r,\varphi)$，$U,B$ 作 $S$ 变换；$a$ 取偶函数，则 $C_y=0$。实际内平移是 (4) 的两个分量，内姿态由真实内平圈给出，不能继续把内中心作为无成本自由量。

设 $s_0=\|(v^{-2}+a^2)/E-1\|_\infty$，$e_*\le\inf e$ 正，$\delta\ge\sup_r\overline{|G|^2}^{1/2}$，定义
$$
 L^2=\frac{\pi^2\delta^2}{3e_*^2}
      +\left(\frac{r_1-r_0}{r_0}\delta\right)^2.
$$
则整个连续重建的相对度量误差不超过 $s_0+2\sqrt{1+s_0} L+L^2$。事实上 $(D/e,T)$ 的 Gram 矩阵是对角阵，偏差仅在第一项，算子范数不超过 $\sqrt{1+s_0}$ 的是这张两列微分本身。由 (5) 的零均值原函数 $L^2\to L^\infty$ 界 $\pi/\sqrt3$ 和从真实外端积分的角均值，新的两列微分之差算子范数不超过 $L$，展开平方即得。$G\cdot T=0$ 使 $|G|^2$ 正是 (3) 两个残差的平方和。各整数有限角网须逐角细化或连续积分，不能把离散频谱逆直接充作 $I$。

实际二阶列为
$$
 F_{rr}=\overline{D_r}+2IT_r+rIT_{rr},\quad
 F_{r\varphi}=(1-\overline{\phantom{x}})(T+rT_r),\quad
 F_{\varphi\varphi}=rT_\varphi.                                          \tag{6}
$$
两圈取 $T=Qe_\varphi,T_r=T_{rr}=0,a=a_r=0$，$Q$ 为该端给定的常数刚姿。由 $U=-Qe_r,B=Qe_z$ 得两端 $D=Qe_r,D_r=0$；(4)–(6) 的两阶 jets 为真实平圈全部两阶导数。未解时仍可用 (6) 的法向、主曲率及 R662 的两框和真刚件验厚度；(3) 的一阶误差不能替这些量给上界。旋转 $E(r)$ 及同一固定 $E$ 的基相位实际通过时，才可用 R655/R680 的材料角平移和刚姿共轭付全部相位。

## 三　准确嵌入 R680 并消费原 R687 真实未解场

在 R680 真锚 $T=Qe_\varphi,v=1,U=-Qe_r,B=Qe_z$，
$$
 a=-p(1.01+\cos\varphi),\quad
 D=Qe_r-p(1.01+\cos\varphi)Qe_z,\quad E=1+p^2(1.01+\cos\varphi)^2 .
$$
$\overline D=-1.01p Qe_z$ 正是原中心斜率；(2)–(6) 在同一真实曲面上准确成立。

更重要的是，可直接从 R687 自然完成的实际任一态读取同一 $T_*,D_*=e_*P_*,C_*',G_*=(D_*)_\varphi-T_*-r(T_*)_r$。这里的 $e_*$ 只在本段指原态实际函数。只要其 $v_*=|(T_*)_\varphi|>0$，置 $a_*=D_*\cdot B_*$，保留原 $T_*$ 本身及 $a_*$ 的整函数，毋须把 $a_*$ 先截成更低阶 Fourier 列。由于 $D_*\cdot T_*=0$，新径向列和新重心的改变准确为
$$
 D_{\rm new}-D_* = \frac{G_*\cdot T_*}{v_*}U_*=:J,\qquad
 C_{\rm new}(r)-C_*(r)=\int_{r_1}^r(\overline J-d_*)(s)\,ds,\qquad
 d_*=C_*'-\overline{D_*}.                                                   \tag{7}
$$
这在每个材料点是满足两个强制点积的最近径向列。实际 $F$ 只改径向中心函数，差即上述中心差；由新中心的一、二阶导会改变真实度量和曲率，故旧硬门不能原样搬用。标量行改变为 $(2D_*\cdot J+|J|^2)/E$ 加原径向偏差，仍应计算全项。新闭性向量是 $G_*+J_\varphi$，只有 $T_*$ 向分量已被准确消去；未宣称其余范数必下降。若 $v_*$ 的实测或连续正则性不足，应区分待核区间及已核点，不能用 (1) 对未解场反推正下界。原有限角数读数、连续解析重建和实际模拟器的有限求积中心仍须像 [R689](R689-continuous-metric-and-tube-enclosures-for-the-actual-two-native-fields.md) 一样分列。

## 四　保留完整变化空间的实际列

在已给正则 $T_*$ 上，可以用 $s_1U_*+s_2B_*=:V$ 作单位球指数坐标，
$$
 T=(\cos|V|)T_*+\operatorname{sinc}(|V|)V .
$$
$s_1,s_2$ 为奇角函数，$a=a_*+A$ 的 $A$ 为偶角函数。它们在 $V=0$ 给出全部反射类的切向变化和独立有符号法向速度变化；选定有限基后必须保全它的每一列。在大步跨过球指数图的反极点前，可在真正接受的实际 $T$ 上重新立图。$T$ 的自由径向样条在两端去三列，$A$ 去两列；原被运输的完整 $a_*$、各项端 jet 仍要实核。将 $E$ 设计到径向、或者在原已冻结的解析 $E$ 上求解，要保留各自所用的真实源身份。

任意实际参数变化给
$$
 \delta v=U\cdot\delta T_\varphi,\quad
 \delta U=(\delta T_\varphi-U\delta v)/v,\quad
 \delta B=\delta T\times U+T\times\delta U,\qquad
 \delta D=-\delta U/v+U\delta v/v^2+B\delta a+a\delta B .
$$
全闭性微分为 $\delta G=(\delta D)_\varphi-\delta T-r(\delta T)_r$，两行分别取 $\delta U\cdot G+U\cdot\delta G$ 和 $\delta B\cdot G+B\cdot\delta G$；标量行的微分为 $-2\delta v/v^3+2a\delta a-\delta E$。中心与全部实际曲率列分别按 (4)、(6) 微分。在未解场，不能省略标架变化与残差的点积，或把 $\delta C'$ 当原来的独立参数。这里给出下一真实全列推进的数学输入，尚未为已付 R687 态读取 $v_*$ 或求出任何有限根。
