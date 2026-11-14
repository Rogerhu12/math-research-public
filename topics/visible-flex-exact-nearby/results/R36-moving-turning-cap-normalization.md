# R36：移动转折的真实拉直、双端 shear 与单根正组件

2026-11-12，independent-audit。

**状态：已证明的局部适配结论。** 本文从真实移动转折曲线出发，
构造 R35 所需的正组件系数比较，不要求当前几何接近径向基点。
另完整补出本题更直接需要的“一个简单转折到一个普通椭圆切口”
版本：归一退化权为 $x$，两端 trace 为 $H^{1/3}\oplus H^{1/2}$。

这不包括平帽边缘的双主系数同时消失、极点极限，亦没有给出从正根
跨入负组件的完整 Airy 接线或真实反馈小除数逆。正角权与所需有限
几何 jets 仍须由实际候选独立供应。

## 1. 真实密度算子和非特征转折门

考虑实际坐标 $(s,\theta)$ 下的实散度密度算子
$$
Pu=\partial_s(a u_s+b u_\theta)
  +\partial_\theta(b u_s+c u_\theta),
\qquad
\mathsf A=\begin{pmatrix}a&b\\b&c\end{pmatrix}.
\tag{1.1}
$$
源以同一 $ds\,d\theta$ 密度书写。本篇默认已用 R32 的正 ground-state
变换处理了需要消去的零阶项；若没有，应把该真实项和其 form 费用
保留，不能直接引用 R35 的非负散度型定理。

在实际转折曲线 $s=t(\theta)$ 上，假设
$$
\det\mathsf A=0,\quad a>0,\quad
\partial_s\det\mathsf A\ne0,\qquad
\boxed{\quad 1-\frac ba t'(\theta)\ne0.\quad}
\tag{1.2}
$$
最后一项是必须检查的非特征条件。令 $x=s-t(\theta)$、$\eta=\theta$，
则拉直后 normal 系数在该根上为
$$
\widetilde a
=a-2bt'+ct'^2
=a\left(1-\frac ba t'\right)^2>0.
\tag{1.3}
$$
所以 (1.2) 精确保证法向系数不退化。
在 R29 的法向主符号 $N\partial_s^2-2M\partial_s\partial_\theta
+L\partial_\theta^2$ 中，$b/a=-M/N$，即两族特征在根处的共同速度。
若 (1.2) 失败，就不能把该根称为本篇所用的简单 Tricomi 型根。

以下系数和曲线取充分光滑。例如若最终只需 $r$ 个有界几何导数，
可以预先供应 $C^{r+3}$ 的系数及曲线表，并保各 reciprocal 的真实
正下界。本文不声称坐标归一化免费保留任意阶 jets。

## 2. 两条移动根的真实拉直

设正组件是
$$
\Omega=\{(s,\theta):t_-(\theta)<s<t_+(\theta)\},\qquad
t_+-t_->0,
\tag{2.1}
$$
$\mathsf A$ 在内部正定，在两根为秩一非负，并满足 (1.2)。
假设行列式在两侧都是简单零点，朝内部为正。
任选固定 $L>0$，置
$$
x=L\,\frac{s-t_-(\theta)}{t_+(\theta)-t_-(\theta)},\qquad
\eta=\theta,\qquad
k=x_s=\frac{L}{t_+-t_-}>0.
\tag{2.2}
$$
令 $J_\Psi=D_{(s,\theta)}(x,\eta)$。准确的新密度矩阵、源是
$$
\boxed{\quad
\widetilde{\mathsf A}
=\frac1kJ_\Psi\mathsf A J_\Psi^t,\qquad
\widetilde f=\frac1k f,
\quad}
\tag{2.3}
$$
右端都在逆坐标中取值。若存在零阶密度 $d$，其真实变换同为
$\widetilde d=d/k$。

在二维，密度矩阵的行列式满足准确恒等式
$$
\det\widetilde{\mathsf A}=\det\mathsf A
\quad\text{在对应点上}.
\tag{2.4}
$$
这里不是遗漏 Jacobian，而是
$k^{-2}(\det J_\Psi)^2=1$。普通非密度矩阵不可直接套用 (2.4)。

在两个端点，$x_\theta=-k t_\pm'$，因此
$$
\widetilde a
=k\,a\left(1-\frac ba t_\pm'\right)^2>0.
\tag{2.5}
$$
内部正定也给 $\widetilde a>0$，故它在整个闭圆柱有正下界。
由简单零点、正性和除法引理，
$$
\Delta(x,\eta):=
\frac{\det\widetilde{\mathsf A}(x,\eta)}{x(L-x)}
\tag{2.6}
$$
光滑延伸到两端，且在闭圆柱严格为正。
例如在左端，它的值为
$L^{-1}\partial_x\det\widetilde{\mathsf A}(0,\eta)>0$；
右端则为 $-L^{-1}\partial_x\det\widetilde{\mathsf A}(L,\eta)>0$。

对边界图 $s=t(\theta)$，原坐标的完整 graph conormal density 是
$$
p_{\rm graph}
=(a-bt')u_s+(b-ct')u_\theta
\tag{2.7}
$$
（outward 方向另乘相应符号）。将 (2.2) 逐项代入可直接核实：
(2.7) 正好等于新坐标的
$\widetilde p=\widetilde a\,u_x+\widetilde b\,u_\eta$。
所以真实 moving-boundary momentum 被保留；不能只取旧的
$a u_s+b u_\theta$ 充当斜边界的 conormal。

## 3. 双端真实角 shear：无需接近恒等映射

令
$$Q=\widetilde b/\widetilde a.$$
它在整个闭圆柱光滑。分别解真实圆周流
$$
\partial_x\Theta_-(x,\phi)=Q(x,\Theta_-(x,\phi)),
\quad \Theta_-(0,\phi)=\phi,
$$
$$
\partial_x\Theta_+(x,\phi)=Q(x,\Theta_+(x,\phi)),
\quad \Theta_+(L,\phi)=\phi.
\tag{3.1}
$$
二者均为保向圆周微分同胚，因为
$$
\partial_\phi\Theta_\pm
=\exp\left(\int_{x_\pm}^x
 Q_\eta(r,\Theta_\pm(r,\phi))\,dr\right)>0.
\tag{3.2}
$$
取两个支撑不交、值在 $[0,1]$ 的固定径向 cutoff $\chi_\pm$，
在对应根的邻域各等于 $1$。使用相容的实提升，定义
$$
\Theta(x,\phi)=\phi+
\chi_-(x)(\Theta_-(x,\phi)-\phi)
+\chi_+(x)(\Theta_+(x,\phi)-\phi).
\tag{3.3}
$$
在每个 $x$ 最多一个 cutoff 非零，所以
$$
J=\Theta_\phi
=(1-\chi_\pm)+\chi_\pm\partial_\phi\Theta_\pm>0
\tag{3.4}
$$
（或 $J=1$）。因此这个双端 shear 是真实全局微分同胚，
不需要假定 $\Theta_\pm-\phi$ 小，也不需要一个未经证明的解析流。

令
$$
\zeta=Q(x,\Theta(x,\phi))-\Theta_x(x,\phi),\qquad
U(x,\phi)=u(x,\Theta(x,\phi)).
$$
准确新矩阵为
$$
\boxed{\quad
\widehat{\mathsf A}
=\begin{pmatrix}
(\widetilde a\circ\Theta)J&
(\widetilde a\circ\Theta)\zeta\\
(\widetilde a\circ\Theta)\zeta&
\displaystyle
\frac{(\widetilde a\circ\Theta)\zeta^2+
(\det\widetilde{\mathsf A}/\widetilde a)\circ\Theta}{J}
\end{pmatrix}.
\quad}
\tag{3.5}
$$
它的行列式仍为
$\det\widehat{\mathsf A}=\det\widetilde{\mathsf A}\circ\Theta$。
在两根的整个邻域，$\zeta=0$ 精确成立，所以那里
$$
\widehat{\mathsf A}
=\operatorname{diag}\left(a_1,\frac{\det\widehat{\mathsf A}}{a_1}\right),
\qquad a_1=(\widetilde a\circ\Theta)J>0.
\tag{3.6}
$$
完整源和 momentum 同时变为
$$
\widehat f=J(\widetilde f\circ\Theta),\qquad
\widehat p=J(\widetilde p\circ\Theta).
\tag{3.7}
$$
这是高度 pullback 与对偶密度 pullback 的同一变换。
两端在边界本身的角标签为 identity；若再选独立 Liouville 角标签，
仍须各自变换源和对偶端口。

## 4. 进入 R35 的明确 $m,M$，不要求近径向

置 $\chi=x(L-x)$、$A_0=\operatorname{diag}(1,\chi)$。
由 (3.5)--(3.6)，归一矩阵
$$
C=A_0^{-1/2}\widehat{\mathsf A}A_0^{-1/2}
\tag{4.1}
$$
在两端光滑延伸。原因是 off-diagonal 在根的邻域恒为零，
而 $C_{22}=(\det\widehat{\mathsf A}/\chi)/a_1$ 在那里；
没有对一个一般非零 cross 项除以 $\sqrt\chi$。

若实际数据给
$$
0<a_0\le a_1\le a^*,\qquad
0<d_0\le\frac{\det\widehat{\mathsf A}}{\chi}\le d^*,
\qquad |C_{12}|\le b^*,
\tag{4.2}
$$
则可明确取
$$
\boxed{\quad
M=a^*+\frac{d^*+(b^*)^2}{a_0},\qquad m=\frac{d_0}{M}.
\quad}
\tag{4.3}
$$
事实上 $\det C=\det\widehat{\mathsf A}/\chi$，
且 $C_{22}=(\det C+C_{12}^2)/C_{11}$，
所以 $\lambda_{\max}(C)\le\operatorname{tr}C\le M$，
$\lambda_{\min}(C)=\det C/\lambda_{\max}(C)\ge d_0/M$。
这准确给
$$mI\le C\le MI.$$

即使只作定性命题，(1.2)、(2.6)、(3.2) 和紧性也保证存在有限的
(4.2)。要把它用于本题可核验的收敛门，则必须从实际输入给出这些
数值界，不能把“紧性保证有限”写成已有一个足够小的预算。

## 5. 一个移动简单转折到普通椭圆切口

现在设左边界 $s=t_0(\theta)$ 是满足 (1.2) 的简单根，
右边界 $s=t_1(\theta)>t_0(\theta)$ 是普通切口：
矩阵 $\mathsf A$ 在内部和整个右边界正定。
仍用
$$x=L(s-t_0)/(t_1-t_0),\qquad\eta=\theta.$$
(2.3)--(2.5) 和 graph conormal 恒等式仍准确成立。
此时
$$
\frac{\det\widetilde{\mathsf A}}x
$$
在闭圆柱严格为正；右端无需、也不允许假造另一个行列式零点。

只在左端作 (3.1) 的 root-anchored flow，并用一个 cutoff 使
$\Theta=\phi$ 在右切口的整个邻域。公式 (3.4)--(3.7) 不变，
cross 在左根邻域精确为零。
现在准确模型是
$$
\boxed{\quad
A_0=\operatorname{diag}(1,x),\qquad
C=A_0^{-1/2}\widehat{\mathsf A}A_0^{-1/2}.
\quad}
\tag{5.1}
$$
它在左端光滑延伸，右端因 $x=L>0$ 本就正则。
(4.2)--(4.3) 完全适用，只把 $\chi$ 改为 $x$。
所以同样不要求实际几何接近某个径向背景。

这正是一个转折外接普通尾部切口时的局部正组件。
切口外的实际 Robin/tail、持握或极点条件仍须接到同一个 full DN；
它们没有被 (5.1) 自动构造。尤其不能将两根的
$H^{1/3}\oplus H^{1/3}$ trace 强加于这里的普通右端。

## 6. 单根模型的真实 trace、延拓及明确常数

定义单根能量空间
$$
\|U\|_{V_1}^2
=\int_{[0,L]\times S^1}
 (|U|^2+|U_x|^2+x|U_\theta|^2),
\tag{6.1}
$$
角积分仍取 $d\theta/(2\pi)$。
令 $\lambda_n=\sqrt{1+n^2}$、$\ell=L/4$，真实 trace 空间是
$$
\mathcal T_1=H^{1/3}(S^1)\oplus H^{1/2}(S^1),\qquad
\|h\|_{\mathcal T_1}^2
=\sum_n\bigl(\lambda_n^{2/3}|h_{-,n}|^2
+\lambda_n|h_{+,n}|^2\bigr).
\tag{6.2}
$$

可以取端点常数
$$
\begin{aligned}
C_{{\rm tr},-}&=2\ell+\frac4\ell+\frac{16}{\ell^2},\\
C_{{\rm tr},+}&=2\ell+\frac4\ell+\frac{32}{3L\ell},\\
C_{E,-}&=\frac1\ell+\frac\ell3+\frac{\ell^2}{12},\\
C_{E,+}&=\frac1\ell+\frac\ell3+\frac{L\ell}{3},
\end{aligned}
\tag{6.3}
$$
并令
$$
\boxed{\quad
C_{\rm tr}^{(1)}=\max(C_{{\rm tr},-},C_{{\rm tr},+}),\qquad
C_E^{(1)}=\max(C_{E,-},C_{E,+}).
\quad}
\tag{6.4}
$$
则有真实满射 trace 和 Fourier 对角右逆 $E_1$，
$$
\boxed{\quad
\|\operatorname{Tr}U\|_{\mathcal T_1}^2
\le C_{\rm tr}^{(1)}\|U\|_{V_1}^2,\qquad
\|E_1h\|_{V_1}^2\le C_E^{(1)}\|h\|_{\mathcal T_1}^2.
\quad}
\tag{6.5}
$$

**左根证明。** 对第 $n$ 模取
$t_-=\ell\lambda_n^{-2/3}$。
基本定理在 $[t_-/2,t_-]$ 上给
$$
|U_n(0)|^2\le\frac4{t_-}
 \int_{t_-/2}^{t_-}|U_n|^2
 +2t_-\int_0^{t_-}|U_n'|^2.
$$
$n\ne0$ 时 $x\ge t_-/2$、$\lambda_n^2/n^2\le2$，所以
$$
\lambda_n^{2/3}|U_n(0)|^2
\le2\ell\int_0^{t_-}|U_n'|^2
 +\frac{16}{\ell^2}\int_{t_-/2}^{t_-}xn^2|U_n|^2.
\tag{6.6}
$$
$n=0$ 时将后一项换成
$(4/\ell)\int_{\ell/2}^{\ell}|U_0|^2$。

**右普通切口证明。** 取 $t_+=\ell\lambda_n^{-1}$，
在 $[L-t_+,L-t_+/2]$ 上平均同一基本定理。
此处 $x\ge3L/4$，故 $n\ne0$ 时
$$
\lambda_n|U_n(L)|^2
\le2\ell\int_{L-t_+}^L|U_n'|^2
+\frac{32}{3L\ell}
 \int_{L-t_+}^{L-t_+/2}xn^2|U_n|^2.
\tag{6.7}
$$
零模仍用 $4/\ell$ 的 $L^2$ 项。
两端使用的区间不交，故求和只需取 (6.4) 的最大值，不需把两个
端点常数相加。

**延拓证明。** 在左端用宽度 $t_-$ 的帐篷
$(1-x/t_-)_+$，右端用宽度 $t_+$ 的帐篷
$(1-(L-x)/t_+)_+$，分别乘真实边界 Fourier 系数。
两者支撑不交。左端三个能量分别由
$$
t_-/3,\quad t_-^{-1},\quad n^2t_-^2/12
$$
控制，得到 $C_{E,-}\lambda_n^{2/3}$。
右端分别由
$$
t_+/3,\quad t_+^{-1},\quad Ln^2t_+/3
$$
控制，得到 $C_{E,+}\lambda_n$。
这证明 (6.5)。帐篷可在同一能量范数光滑逼近，所以是实际空间中的
延拓；有限 Fourier 逼近再给全部 trace 数据的右逆。

## 7. 与 R35 的 full source/DN/Robin 和角权换算

在 (5.1) 的实际 $mI\le C\le MI$ 下，取
$$
P_1=-\operatorname{div}(\widehat{\mathsf A}\nabla),\qquad
\mathfrak e_1(U,V)=\int\widehat{\mathsf A}
(\nabla U,\nabla\overline V).
$$
普通源仍属于**完整** $V_1^*$。
对 $V_{1,00}=\ker\operatorname{Tr}$，逐角模区间 Poincaré 给
$$
D_L=1+L^2/\pi^2,\qquad
g_0=D_L/m,\qquad
\mathfrak e_1(U,U)\ge g_0^{-1}\|U\|_{V_1}^2.
\tag{7.1}
$$
这与 R35 完全相同，不能因右端普通而更改或漏掉 $D_L$。

于是 R35 §§3--4 的证明逐字给出同一真实
$G_1,\mathcal H_1,\Lambda_1,\mathcal K_1$：
$$
\begin{aligned}
\|G_1\|&\le g_0,\\
\|\mathcal H_1\|,\ \|\mathcal K_1\|
 &\le\sqrt{C_E^{(1)}}(1+Mg_0),\\
\|\Lambda_1\|&\le MC_E^{(1)},\\
\langle\mathcal K_1 f,h\rangle
 &=\mathfrak e_1(G_1f,E_1h)-\langle f,E_1h\rangle .
\end{aligned}
\tag{7.2}
$$
所有两端 cross、完整 source contact 和共同常数均保留。

边界等距归一化必须改为
$$
\boxed{\quad
Q_1=\operatorname{diag}\left(
(1-\partial_\theta^2)^{1/6},
(1-\partial_\theta^2)^{1/4}\right).
\quad}
\tag{7.3}
$$
它把 $\mathcal T_1$ 准确映到 $L^2\oplus L^2$。
因此 $B_1=Q_1^{-1}\Lambda_1Q_1^{-1}$ 有界自伴；
减去真实 real normal shear 后，R35 §5 的非实 Robin 双向满射
及 $\gamma^{-1}$ 的无权界照旧成立。

角权 $W_\sigma$ 在两个端点使用相同的实际 Fourier 权；
它与 (7.3) 的两个不同阶数都交换。故只要为归一矩阵 $C$ 及真实
shear 供应 R35 (6.1) 的解析表，或 (7.7) 的直接 log 表，
R35 §§6--7 的所有共轭/Neumann/source 结论成立，
其中 $C_E$ 换成 $C_E^{(1)}$，
$$
C_\Lambda^{(1)}
=C_E^{(1)}[1+2g_0(M+1)]^2,
\tag{7.4}
$$
其余宽度门和 Robin 的 $2/\gamma$ 界不变。

从 R32 的原算子起，必须按以下顺序保留同一个普通源和端口：
先作 $w=YU$，源变成 $Yf_\rho$、momentum 变成
$Yp_w-wp_Y$；再作 (2.3)、(3.7) 的真实密度变换；
最后若采用本节正号 $P_1=-\operatorname{div}$，右端整体取负。
边界弱范数和 full source-contact 都针对这个最终实际源。
复原时逆序恢复 normal shear、对偶角密度和 moving-graph conormal。

## 8. 真实正则范围及 Airy 接线的下一项输入

上述坐标和比较门只使用实际型别、非特征条件及有限 jets；
它们不自动供应一个正解析角带或直接 log 角宽。
即使原图对 $\theta$ 是有限 Fourier 和，如果 $s$ 方向只具有限阶
光滑性，隐式移动根 $t(\theta)$ 穿过相应径向拼接点后，也可能只具
有限阶光滑性。不能把原来的 Fourier 截断当作新坐标中的解析证明。
可通过真正的适当 Gevrey/光滑强表、充分的共同解析域，或明确的
单一解析 piece 范围逐项支付所需正则性。

在每个简单根的 collar 中，(3.6) 或其单根版本已经把实际算子
准确放成
$$
\partial_x(a_1 U_x)+\partial_\phi\!\bigl(x\,d_1 U_\phi\bigr),
\qquad a_1,d_1>0
\tag{8.1}
$$
（右根采用朝正侧的 defining coordinate）。
这提供了真实 simple-root Airy 构造的系数输入、source 和 conormal；
尚须实际构造两侧解、其有限高阶残差修正、共同通量 frame、
负阶相位和强源/输出预算，才可接 R34 的完整相位门。
仅凭 (8.1) 的形式，不能宣称这些步骤已经完成。

本题当前有限核心接尾应优先核验第 5--7 节的一根版本。
两根版本是一个另有明确范围的正 annulus 结果；
平面片边缘和极点均未被任何一个版本包含。

**来源。** 全 form、source contact 和角权逆使用本题
[R35](R35-positive-cap-without-background-smallness.md) 的已证固定域
论证；真实 ground-state 与全局线性化使用
[R32](R32-exact-darboux-and-full-scattering-interface.md)。
双端 root-anchored shear 的结构与邻题
[R513 §4](../../continuous-flexibility-swarm/results/R513-direct-log-physical-local.md)
一致，本文重新证明了无需近恒等小量的实轴 Jacobian、移动根
非特征门及实际 $m,M$，没有移植其原 profile 或累计预算。
