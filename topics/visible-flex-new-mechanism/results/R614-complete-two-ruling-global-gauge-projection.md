# R614：两条完整 ruling 的全局常规范投影与真实非退化性

2026-11-27。**已证明：R609 的两个自由常规范可由同一整条真路径唯一消元；
在四偶共同根上两规范列必不退化，且完整离解导数如下。**
本稿为纸证。未给出投影后两函数与三个/四个端积分的共同根。

本稿允许 $h^2-H^2(1+d^2)$ 变号，不加 prepared 中心或正首层支条件。
原真 $\eta,A,\rho^\pm$、一个固定 $\chi$、完整正势和全部负侧反号保持。
正交结论明确要求双侧同权；若两 ruling 使用不同单位，必须用第 4 节的完整加权 Gram。

## 1. 同一完整路径上的两列

沿用 [R609](R609-true-integral-histories-and-kinetic-input.md) 的函数消元。
在同一个归一化区间 $x\in[0,1]$ 上，由实际 $h,k,L$ 产生原几何
$g=(h,k,\eta,\gamma,\upsilon)$、八个真矩 $A$ 和两侧六个真历史 $\rho^\pm$。
中心 $H=h(0)>0$，原 $k(0)=\eta(0)=\gamma(0)=0$、$b(0)=k_{ss}(0)=0$。
四奇中心由真尾积分产生，未固定为 prepared 值。

记

$$
d=h\eta-k,\qquad q=1+d^2,\qquad
m=h^2-H^2q,\qquad \beta=\frac{m}{2h}.
\tag{1}
$$

这里 $\beta$ 是规范配对列，不是原加速度 $b=k_{ss}$。
负侧为 $g^-=(h,-k,-\eta,-\gamma,\upsilon)$、$A^-=JA$。
中心常数 $\zeta_0$ 按 R609 (17) 准确确定，包含当前 $H,v,A_c,a(0)$ 的全部依赖。

从原完整 ruling 中只暂时置自由 $\zeta_1=\zeta_2=0$，定义

$$
\begin{aligned}
\mathcal B_+={}&R^0(g,A)+C_h(g,A)a+C_k(g,A)b
 -4w(g)\!\cdot\!\rho^+-4D(g,A;g_c,A_c)-2w_0(g)\zeta_0,\\
\mathcal B_-={}&R^0(g^-,JA)+C_h(g^-,JA)a-C_k(g^-,JA)b
 -4w(g^-)\!\cdot\!\rho^--4D(g^-,JA;g_c,A_c)-2w_0(g^-)\zeta_0.
\end{aligned}
\tag{2}
$$

所有原历史和完整正势仍在 (2) 内。
因为 $w_0(g^-)=w_0(g)$，而 R609 (15) 的两个剩余配对分别为
$d\zeta_1/2$、$m\zeta_2/(4h)$，原残差准确是

$$
\boxed{N_+=\mathcal B_+-d\zeta_1-\beta\zeta_2,\qquad
       N_-=\mathcal B_-+d\zeta_1-\beta\zeta_2.}
\tag{3}
$$

故两个控制列在双侧函数空间中为

$$
\mathcal A_1=(d,-d),\qquad \mathcal A_2=(\beta,\beta).
\tag{4}
$$

这是**整段两个实数**的线性作用，不是逐点选择规范。
$\zeta_0$ 没有重新成为独立未知数。
即使实际母完全不关于正负位置对称，(3) 仍成立：
母不对称的全部效应在两个各自真实的 $\mathcal B_\pm$ 中，未假定两者相等。

## 2. 四偶共同根上两列都必不为零

设 R609 的四个真实偶端积分均为零。
[R612](R612-exact-physical-length-elimination-and-three-true-end-integrals.md)
已证明 $K=\int k^2>1$、$U=\int(h_x/h)^2>0$。

**命题 1。** 此时

$$
\int_0^1d^2\,dx>0,\qquad
\int_0^1\beta^2\,dx>0.
\tag{5}
$$

**证明第一式。** 若 $d$ 恒零，则 $\eta=k/h$。
由真运动学 $\eta_x=k_x/(2h)$ 得 $k_x=2(h_x/h)k$。
结合 $k(0)=0$，线性微分方程唯一性给 $k=0$，与 $K>1$ 矛盾。
连续性把非恒零提升为严格正的平方积分。

**证明第二式。** 若 $\beta$ 恒零，则
$h^2=H^2(1+d^2)$。置 $\theta=\arctan d\in(-\pi/2,\pi/2)$、
$I=-\eta/h$。由原运动学直接算得

$$
I_x=\frac{d_x}{h^2}=\frac{\theta_x}{H^2}.
$$

中心 $I(0)=\theta(0)=0$，因此 $I=\theta/H^2$，
$h=H\sec\theta$，以及

$$
k=h\eta-d=-h^2I-d=-\theta\sec^2\theta-\tan\theta.
$$

于是原 $p_1$ 密度在整个区间准确为

$$
-kd=\tan^2\theta+\theta\tan\theta\sec^2\theta\ge0.
\tag{6}
$$

由于 $\theta$ 与 $\tan\theta$ 同号，等号仅当 $\theta=0$。
真实 $p_1$ 总积分为零故迫 $\theta=0$，继而 $k=0$，又与 $K>1$ 矛盾。
故 $\beta$ 不恒零，平方积分严格正。证毕。

这没有假定 $m$ 全程正或负，也不要求 $d,m$ 的零点简单。
它只保证在任何真实共同根上两个**整段**列非零；
不提供某个未解初猜的统一数值下界，也不从连续结论推出有限采样矩阵必满秩。

## 3. 同权双侧的准确分解与唯一常规范

定义实际偶、奇部分

$$
\mathcal E=\frac{\mathcal B_++\mathcal B_-}{2},\qquad
\mathcal O=\frac{\mathcal B_+-\mathcal B_-}{2}.
\tag{7}
$$

这两个名称只指双侧和差，和原矩槽“奇/偶”命名无关。
由 (3)，

$$
\frac{N_++N_-}{2}=\mathcal E-\beta\zeta_2,\qquad
\frac{N_+-N_-}{2}=\mathcal O-d\zeta_1.
\tag{8}
$$

取同一个固定正权 $\omega(x)>0$，令
$\langle f,g\rangle_\omega=\int\omega fg$。
在双侧使用同一权时，(4) 的交叉内积逐点抵消，

$$
\|N_+\|_\omega^2+\|N_-\|_\omega^2
=2\|\mathcal O-d\zeta_1\|_\omega^2
 +2\|\mathcal E-\beta\zeta_2\|_\omega^2.
\tag{9}
$$

只要两个列范数非零，整段最小二乘常数唯一且准确为

$$
\boxed{\zeta_1^*=\frac{\langle d,\mathcal O\rangle_\omega}{\langle d,d\rangle_\omega},
\qquad
\zeta_2^*=\frac{\langle\beta,\mathcal E\rangle_\omega}{\langle\beta,\beta\rangle_\omega}.}
\tag{10}
$$

命题 1 保证任何真实四偶共同根都落在这一有效范围内。
因此原两个完整 ruling 有一组全程常规范使其同时恒零，
当且仅当

$$
\mathcal O-\zeta_1^*d=0,\qquad
\mathcal E-\zeta_2^*\beta=0
\quad\hbox{在整个区间成立。}
\tag{11}
$$

等价地，下面的完整非负缺陷为零：

$$
\mathscr D=
\|\mathcal O-\zeta_1^*d\|_\omega^2+
\|\mathcal E-\zeta_2^*\beta\|_\omega^2.
\tag{12}
$$

若函数连续且权严格正几乎处处，积分为零迫两残差处处零。
这里只用同一原函数上的积分，不以有限点残差代替连续结论。

可将 (12) 展成两个 Cauchy–Schwarz 缺额，
例如 $\|\mathcal O\|_\omega^2-\langle d,\mathcal O\rangle_\omega^2/\|d\|_\omega^2$。
但数值实现应优先用已经配出常数后的完整残差平方，避免两个大数相减。
式 (10) 只除整个区间的严格正范数；**不在 $d$ 或 $m$ 的零点作逐点除法**。
这些零点上的原条件仍由 (11) 保留，不能省去。

若两个 ruling 都除以同一个冻结单位，(9)(10) 完全不变，
只将目标整体乘一个常数。R609 首函数源正是这种同单位范围。

## 4. 双侧不同单位时的正确 Gram

若实际目标对两侧使用不同固定单位或不同正权 $\omega_+,\omega_-$，
则不能继续使用 (9)(10) 的简单正交。
在双侧空间定义

$$
\langle f,g\rangle=\int(\omega_+f_+g_++\omega_-f_-g_-).
$$

令 $f=(\mathcal B_+,\mathcal B_-)$，
$\mathcal A(z_1,z_2)=z_1\mathcal A_1+z_2\mathcal A_2$。
其完整 Gram 和右端是

$$
G=\begin{pmatrix}
\int(\omega_++\omega_-)d^2&\int(\omega_+-\omega_-)d\beta\\
\int(\omega_+-\omega_-)d\beta&\int(\omega_++\omega_-)\beta^2
\end{pmatrix},
\tag{13}
$$

$$
\mathcal A^*f=
\binom{\int d(\omega_+\mathcal B_+-\omega_-\mathcal B_-)}
      {\int\beta(\omega_+\mathcal B_++\omega_-\mathcal B_-)}.
\tag{14}
$$

在 (5) 且两权严格正几乎处处时，$G$ 正定。
因为对任何 $z$，

$$
z^TGz=\int\{\omega_+(z_1d+z_2\beta)^2
                 +\omega_-(-z_1d+z_2\beta)^2\}.
$$

若此值为零，两平方均几乎处处零，相加相减得
$z_1d=z_2\beta=0$；(5) 给 $z_1=z_2=0$。
故不同单位下的准确最优常数是

$$
\boxed{\zeta^*=G^{-1}\mathcal A^*f.}
\tag{15}
$$

这里权固定，所有几何变化都在 $f,\mathcal A$ 内。
若有意令单位随未知曲线变化，须另加权的导数；不能沿用下一节的冻结权公式。

## 5. 完整离解导数与不能省掉的残差项

在 $G>0$ 的范围，令

$$
r=f-\mathcal A\zeta^*,\qquad
\Pi=\mathcal A G^{-1}\mathcal A^*.
$$

正规方程是 $\mathcal A^*r=0$。
对任意真实曲线变分，记
$u=\delta f-(\delta\mathcal A)\zeta^*$。
微分正规方程，得到

$$
\boxed{\delta\zeta^*
 =G^{-1}\{\mathcal A^*u+(\delta\mathcal A)^*r\},}
\tag{16}
$$

以及

$$
\boxed{\delta r=(I-\Pi)u
 -\mathcal A G^{-1}(\delta\mathcal A)^*r.}
\tag{17}
$$

证明是
$0=\delta(\mathcal A^*r)=(\delta\mathcal A)^*r+\mathcal A^*(u-\mathcal A\delta\zeta^*)$，
再代回 $\delta r=u-\mathcal A\delta\zeta^*$。
最后一项一般在离解状态不为零；只有 $r=0$ 时才能直接删去。
因此将连续或离散规范投影放进求解器时，
不能用只在根上成立的 Schur 公式冒完整离解 Jacobian。

对目标 $\tfrac12\|r\|^2$，由 $r\perp\operatorname{im}\mathcal A$ 则有准确简化

$$
\delta\left(\frac12\|r\|^2\right)
=\langle r,\delta f-(\delta\mathcal A)\zeta^*\rangle.
\tag{18}
$$

所以一阶目标梯度不需要显式 $\delta\zeta^*$，
但完整残差 Jacobian 仍须 (17) 的全部项。
这两个事实并不矛盾。

$\delta f$ 包含同一真曲线的 $\eta$、四奇尾积分、全部 $A$、六个 $\rho$、
正势和中心 $\zeta_0$ 的完整链；不是只微分局部静态系数。
若同时采用 R612 的准确长度消元，$\delta L$ 也必须进入每条链。
两列导数包含 $\delta H$ 和 $\delta d$：

$$
\delta\beta=\frac{\delta m}{2h}-\frac{m\delta h}{2h^2},\qquad
\delta m=2h\delta h-2H(1+d^2)\delta H-2H^2d\delta d.
\tag{19}
$$

中心高度不能冻结为旧值。

## 6. 对实际续算的作用与范围

R609 首函数源已经在同一曲线的全部双侧点上拟合两个常规范，
并通过完整联合 Jacobian 再全局拟合；本稿不要求为验证该旧线性拟合而重跑。
本稿新增的是：真实四偶根上的全局非退化证明、奇偶两完整残差的明确分工、
不同双侧单位时的正确加权矩阵，以及显式投影后的完整离解导数。

实际新的数学输入可以直接优化三/四个端积分加两条投影后的完整函数。
若 $d$ 或 $m$ 在某段很小，只能据实际范数和原残差调整组织；
不能逐点除以它们，不能改成任意逐点规范，不能把 $m>0$ 当成原方程必要条件。
若数值两列近退化，本稿也不提供免付的统一条件数下界。

离散求积和有限配点版的 (13)–(18) 是对应有限残差模型的准确代数，
但没有补上连续积分、原 ruling 根、period/pose、有限非线性族或宏观 reach。
这些主完成条件全部保留。
