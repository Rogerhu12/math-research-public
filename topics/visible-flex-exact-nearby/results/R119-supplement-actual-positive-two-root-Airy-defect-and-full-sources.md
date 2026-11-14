# R119 续篇：实际正型双根的完整 Airy 反射、4/3 阶 defect 与全部源

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对强尾的每一个完整内部正型分量，在两个真实根的
同一个原 Airy 框架中，完整双端反射为

$$
 R_{+,m}=-I+E_{+,m},\qquad
 \|E_{+,m}\|_2<2^{30}(a_*/|m|)^{4/3},\quad m\in4\mathbb Z\setminus\{0\},
 \qquad a_*:=\max(a_-,a_+).
 \tag{A.1}
$$

这里 $a_e=|A_t(t_e)|$ 是真实根斜率。反射是包含两个 off-diagonal
块的完整矩阵，且在包括 mean 的全空间上准确酉。特别，它没有另一个
未计入的 $1/|m|$ 首相位。根 mean 是实际的两维边界系统，未被清零。
由已有真实斜率界，还可统一写成

$$
 \|R_++I:H^s\longrightarrow H^{s+4/3}\|
       <2^{64}(j+5)\delta_j^{-3},\qquad s\in\mathbb R.
 \tag{A.2}
$$

这里 $j$ 指承载该正型上升 quintic 的真实胞元；两根均取该胞元的实际
$\delta_j$，不把相邻分量的标号误换进斜率预算。

参考径向系数与 Fourier 乘子交换，故 (A.2) 在任意共同 Wiener/解析权
中也成立。它不是非径向更新的自动结论。此处实际正型区完全不受
[第二度量参数](R119-supplement-actual-phase-preserving-subprincipal-metric-parameter.md)
改动，所以结论同时适用于该新径向候选族。全文还保留完整 ordinary、
weak source、两个端点的 total/bare 区别，以及真实 height 和 Jacobian。

本篇不把单个正型块的反射当作整个无限网络的逆。其下一消费者仍须接入
两个实际负根和严格区的完整首相位、低模及内部两列 Green 核。

## 1. 同一真实双根、两侧解析 germ 和 height 单位

使用[无损失参考 Airy 证明](R119-supplement-uniform-frequency-reference-Airy-Cauchy.md)
的准确四次 germ、真实复盘和 $|V|<16$。在每个根令 $\xi$ 向相邻负区为正，
$z=-\xi$ 向当前正区为正，取实际 collar

$$
 0\le z\le H:=1/64,\qquad \kappa_e=|m|/a_e.
 \tag{A.3}
$$

两端各自使用其真实 $a_e$，不假定二者相同。令 $x$ 为前篇准确根变量，
$g=d\xi/dx$、$\mu=w/a_{\rm phys}$。对物理 raw 竖直高度 $h$ 定义

$$
 U=\sqrt{a_e g\mu}\,h,\qquad
 r=\tfrac12\partial_z\log(g\mu).
 \tag{A.4}
$$

这与前篇 $v=\sqrt{g\mu}h$ 只差实际常数 $\sqrt{a_e}$，所以在整个
真实 collar 上准确满足

$$
 -U_{zz}+\kappa_e^2zU-V_e(-z)U=0,\qquad |V_e|<16.
 \tag{A.5}
$$

所有角积分用同一物理 $d\theta/(2\pi)$；四重子空间的实际频率是
$m\in4\mathbb Z$，没有再乘一个隐藏的4。原正型散度能量在此 collar
准确化为

$$
 \int\left(|U_z-rU|^2+\frac z{a_e^2}|U_\theta|^2\right)dz\,
                                                    \frac{d\theta}{2\pi}.
 \tag{A.6}
$$

这是从 $|dt|=dz/(a_eg)$、$A=zg^2$ 直接换元所得。因
$|g-1|<1/8$、$|g_x|<1/2$、$|(\log\mu)_t|<2$ 及 $a_e>1$，

$$
 |r|\le\tfrac12\left(\frac{1/2}{(7/8)^2}
                         +\frac2{a_e(7/8)}\right)<2=:G,
 \qquad d:=1-GH=31/32.
 \tag{A.7}
$$

根到相邻 quintic 接缝的原 $|x|$ 距离大于13。两正侧 collar 也互不相交：
若 $z_0=s_0(1-s_0)=\sqrt{7/(30B)}$，两根间的 $a_e t$ 距离为
$60Bz_0(1-4z_0)$，而 $B>2^{190}$、$z_0<2^{-20}$。
此距离远大于1；每个 collar 的 $a_e|t-t_e|$ 小于 $8H/7$。
因此两个 trial 都是真实正分量内支集相离的函数。

根处 $U_e=\sqrt{a_e\mu_e}h_e$。把真实 raw outward DN 按这一 height
作对偶变换，记其矩阵为 $\Lambda_E$。同一 canonical outward flux 是
$p_e=-U_z(0)$，故

$$
 \Lambda=\Lambda_E-\operatorname{diag}(r_e(0)).
 \tag{A.8}
$$

两者都是真正 full 双端矩阵。$\Lambda_E\ge0$；$\Lambda$ 自伴，但本篇不
把扣除 shear 后的它继续当成非负。正型区的内部解和 Dirichlet 逆不受
这个边界二次型扣除改变。

## 2. 完整正分量 Poisson 的两个 collar 增益

先固定任意真实频率，包括0，令
$\bar\kappa_e=\max(1,\kappa_e)$、$x_e=\bar\kappa_e^{1/3}U_e$。
在每个 collar 用长度 $l=\min(H,\kappa_e^{-2/3})$ 的线性 ramp；
$m=0$ 时用 $l=H$。原能量的径向/角向及质量积分分别为

$$
 l^{-1}+\kappa_e^2l^2/12,\qquad l/3.
$$

将它们除以 $\bar\kappa_e^{2/3}$，在 $\kappa_e^{2/3}$ 的两个区间上
取端点最大值，得到每个延拓的实际能量不超过

$$
 E_*|x_e|^2,\qquad
 E_*:=\left(\sqrt{65}+2\sqrt{H/3}\right)^2<128.
 \tag{A.9}
$$

两支 ramp 支集相离，故完整正分量的真正调和解由最小能量原理满足
$\mathcal E\le E_*\|x\|_2^2$。没有在 collar 远端给这个解另加边界条件。

记 $J_e=\int_0^H(|U_z|^2+\kappa_e^2z|U|^2)$。基本定理给
$\|U\|_{L^2}\le\sqrt{2H}|U_e|+H\|U_z\|_{L^2}$；由 (A.6)，

$$
 \left(\sum_eJ_e\right)^{1/2}
 \le T_*\|x\|_2,
 \qquad T_*:=\frac{\sqrt{E_*}+G\sqrt{2H}}d<16.
 \tag{A.10}
$$

完整频率增益使用真实相邻区间比较。在 $\kappa^{-2/3}\le H/2$ 时，
将 $[0,\kappa^{-2/3}]$ 与其相邻区间比较；在其余频率直接用上面的
trace 不等式。两种情形都给

$$
 \kappa^{4/3}\int_0^H|U|^2
       \le4J_e+4\kappa^{2/3}|U_e|^2.
$$

再加质量项，并用 $\bar\kappa^{4/3}\le1+\kappa^{4/3}$，得

$$
 \left(\sum_e\bar\kappa_e^{4/3}\|U\|_{L^2_z}^2\right)^{1/2}
 \le P_*\|x\|_2,
 \quad P_*:=\sqrt{(4+H^2)T_*^2+4+2H}<64.
 \tag{A.11}
$$

这是完整 Poisson 算子在两个 collar 的联合界，涵盖所有端口输入、
两端交叉与 mean。它没有要求一个正型区内部的质量下界均匀于整条尾。

## 3. 真正完整 source/contact，含 Jacobian 与 weak 端点

在两个 collar 中允许 canonical 源
$f-\partial_zF^z-\partial_\theta F^\theta$。逐模定义

$$
 S_o^2=\sum_e\bar\kappa_e^{-4/3}\|f_e\|_{L^2_z}^2,
 \qquad
 S_w^2=\sum_e\int_0^H\left(|F_e^z|^2
                                   +\frac{a_e^2}{z}|F_e^\theta|^2\right)dz.
 \tag{A.12}
$$

任一已有其它区间的源仍作为独立 full source 输入，不被本地范数授予或
删除。对这里的源，完整 total-flux contact $q$ 是该同一 Poisson 的
负伴随，故 (A.10)--(A.11) 直接给

$$
 \|\bar\Gamma^{-1/3}q\|_2\le64S_o+16S_w,
 \quad\bar\Gamma=\operatorname{diag}(\bar\kappa_-,\bar\kappa_+).
 \tag{A.13}
$$

为明确物理源的单位，若原正算子写成
$-\operatorname{div}(G_0\nabla h)=f_{\rm ph}-\operatorname{div}F_{\rm ph}$，
令 $\epsilon_e=\operatorname{sign}(dt/dz)$，$T=\sqrt{a_eg\mu}$。真实换元是

$$
 F^z=\epsilon_e F_{\rm ph}^t/T,\qquad
 F^\theta=F_{\rm ph}^\theta/(a_egT),\qquad
 f=f_{\rm ph}/(a_egT)-rF^z.
 \tag{A.14}
$$

因此普通源的 Jacobian $1/(a_eg)$、height 因子 $1/T$，以及 weak 源的
额外零阶项 $-rF^z$ 都真实保留。若消费第41束的
$\operatorname{div}G_0=s-\operatorname{div}F$ 约定，应代
$f_{\rm ph}=-s$、$F_{\rm ph}=-F$，不能只翻普通源的号。

正区 $z$ 向内，所以 canonical total outward flux 是
$p_{\rm tot}=-U_z+F^z(0)$；bare $p=-U_z=p_{\rm tot}-F^z(0)$。
(A.12) 本身不授予 $F^z(0)$ 的端点迹。若消费者需要 bare Airy 两迹，
必须另给这两条真实迹的空间与范数；仅 weak DN 时则使用 total flux。

## 4. 真实截断 Ai 两列及全矩阵 defect

以下先令 $|m|\ge a_*$，所以两端 $\kappa_e\ge1$。
记 $A_0=\operatorname{Ai}(0)$、$A_1=\operatorname{Ai}'(0)$、
$c_A=-A_1/A_0$、$c=c_A^{-1/2}$。仍使用原 R39 定义；其中
$A_0>1/4$、$1/2<c_A<1$。

取真实 $C^2$ cutoff：在 $[0,H/2]$ 上为1；在 $[H/2,H]$ 上用
$1-10u^3+15u^4-6u^5$，$u=2z/H-1$；之后为0。准确有

$$
 \|\chi'\|_\infty\le4/H,\qquad
 \|\chi''\|_\infty\le24/H^2.
 \tag{A.15}
$$

第 $e$ 列取 $Q_e=c\kappa_e^{-1/3}\chi(z)
\operatorname{Ai}(\kappa_e^{2/3}z)$，在其它位置延为0。两个真实端迹为

$$
 (Q_e)_e=cA_0\kappa_e^{-1/3},\qquad
 (p_{Q_e})_e=-cA_1\kappa_e^{1/3},
 \tag{A.16}
$$

另一根的高度和 flux 都为0。其准确 ordinary residual 为

$$
 f_e=-c\kappa_e^{-1/3}
 [\,V_e\chi\operatorname{Ai}
    +2\chi'\kappa_e^{2/3}\operatorname{Ai}'
    +\chi''\operatorname{Ai}\,].
 \tag{A.17}
$$

括号中的 Ai 参数始终是 $\kappa_e^{2/3}z$。
需要的两个完整无穷积分有准确值

$$
 \int_0^\infty\operatorname{Ai}(s)^2ds=A_1^2,
 \qquad
 \int_0^\infty s^2\operatorname{Ai}'(s)^2ds=\frac47A_1^2<1.
 \tag{A.18}
$$

第一式由 $(\operatorname{Ai}'^2-s\operatorname{Ai}^2)'=-\operatorname{Ai}^2$。
若 $I_3=\int s^3\operatorname{Ai}^2$、$J_2=\int s^2\operatorname{Ai}'^2$，
对 $(s^2\operatorname{Ai}\operatorname{Ai}')'$ 和
$(s^3\operatorname{Ai}'^2-s^4\operatorname{Ai}^2)'$ 积分分别给
$J_2=I_0-I_3$、$3J_2=4I_3$，证明第二式。端点项由真实 Ai 衰减消失。

在 $\chi'$ 支集上 $s\ge\kappa_e^{2/3}H/2$，故
$\kappa_e^{2/3}\|\operatorname{Ai}'\|_{L^2_s(\mathrm{supp}\chi')}
\le2H^{-1}\|s\operatorname{Ai}'\|_{L^2_s}$。换元并保留所有三项得到

$$
 \kappa_e^{-2/3}\|f_e\|_{L^2_z}
 <c\,[16+24/H^2+16/H^2]\,\kappa_e^{-4/3}
 <c\,2^{18}\kappa_e^{-4/3}.
 \tag{A.19}
$$

这不是逐列渐近：两个 residual 支集相离，其完整两列到 (A.12) 源空间
的 norm 就由同一个最大值控制，再用完整 (A.13)。令

$$
 \Gamma=\operatorname{diag}(\kappa_-,\kappa_+),\qquad
 B=\Gamma^{-1/3}\Lambda\Gamma^{-1/3}.
$$

由真恒等式 $p_Q-\Lambda\operatorname{Tr}Q=\mathcal Kf$，得到

$$
 \|B-c_AI\|_2
 <2^{28}\max_e\kappa_e^{-4/3}.
 \tag{A.20}
$$

这里的 $B$ 仍有真实两端 cross；它没有被逐端主符号替换。

## 5. 原 Airy 反射、全部低模与 mean

令 $\mathfrak a=\sqrt3+i$、$\mathfrak b=\sqrt3-i$。
原 Airy 根框架的两个高度/flux 行准确为

$$
 U=cA_0\Gamma^{-1/3}(\mathfrak a z_++\mathfrak b z_-),\qquad
 p=-c c_AA_0\Gamma^{1/3}(\mathfrak b z_++\mathfrak a z_-).
 \tag{A.21}
$$

代入真正 $p=\Lambda U+q$ 后得到

$$
 z_-=R_+z_++s_+,\qquad
 R_+=-(\mathfrak b B+c_A\mathfrak a)^{-1}
                         (\mathfrak a B+c_A\mathfrak b),
$$
$$
 s_+=-(\mathfrak b B+c_A\mathfrak a)^{-1}
                           \Gamma^{-1/3}q/(cA_0).
 \tag{A.22}
$$

$B$ 自伴，实谱上分母的模平方是
$4(t^2+c_At+c_A^2)\ge3c_A^2$，因此该实际矩阵准确酉、满射。
由 $R_++I=-2i(\mathfrak b B+c_A\mathfrak a)^{-1}(B-c_AI)$，
(A.20) 给 (A.1)。在 $0<|m|<a_*$，直接用准确酉性
$\|R_++I\|\le2$，仍满足同一个 (A.1)，未删除这些模式。

对 $m=0$ 使用原 R39 两列 $D_\pm(\xi,0)=c(1\pm i\xi/\pi)$。
两端实际 canonical mean DN 记为 $\Lambda_0$，则

$$
 R_{+,0}=-I+\frac{2i}{\pi}(\Lambda_0+i/\pi)^{-1},\qquad
 s_{+,0}=-c^{-1}(\Lambda_0+i/\pi)^{-1}q_0.
 \tag{A.23}
$$

这是同一纯散度 mean 的两端完整系统，包括原常数高度方向和通量方向；
扣除 shear 后 $\Lambda_0$ 未必有零特征值，但仍准确自伴。
$R_{+,0}$ 酉且 $\|R_{+,0}+I\|\le2$。这就证明 (A.2) 的全频版本。

源的同样全频界可明确写成

$$
 \|s_{+,m}\|_2\le2^{10}\tau_m(S_o+S_w),\quad
 \tau_m=\max_e(\bar\kappa_e/\kappa_e)^{1/3}\ (m\ne0),\quad\tau_0=1.
 \tag{A.24}
$$

低频的 $\tau_m$ 真实保留；它来自 Airy frame 与有质量 Poisson trace
之间的比例，不能因径向参考而删去。mean 用 (A.23) 与 (A.13) 单独支付。
各端 bare source charge 仍按第3节恢复。

## 6. 实际范围与下一接口

原强尾的 $a_*<2^{16}\sqrt{j+5}\delta_j^{-9/4}$ 给 (A.2)，包括
$\langle m\rangle/|m|$ 和 mean 的余量。第二径向参数支集全部在负区，
所以这里的 full positive DN、两个 germ、normal shear 和 source
单位在它的整个实际参数盒中准确相同。

至此完整正型块的首项确实是原 Airy 框架中的 $-I$，余项有真实
$4/3$ 阶界；不能另把它当成两个互不相通的端阻抗。真实返回的首相位
还要用同单位的负根 potential 积分、固定 cut Airy 次首项和整个严格区
相接。内部 Green 的余项逆、参数导数与非径向更新并未由 (A.1) 自动完成。

严格代数、两个 Ai moment、全频 ramp 分界及有向常数见
[原生预算程序](../scripts/fourfold_actual_positive_two_root_Airy_20261113.py)
和[完整报告](../notes/2026-11-13-R119-positive-two-root-Airy-budget.json)。
