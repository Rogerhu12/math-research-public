# R119 续篇：真实 regular 长尾高度输出到 Codazzi 曲率边界

2026-11-13，visible-exact-astra-ac0d / newton_source。

**本篇完成的接口。** 把 R119 已解的完整非线性长径向 Dirichlet 问题，
准确变换为 R126 的正交第二基本形式边界 $(B,C)$，保留 mean 小根、
两端反射、真实法向方向以及平均高度输出。并算出完整频率的线性 Robin
算子及反射源。这是可以供将来的 body/cap 两端求解器消费的真实尾端合同。

接口位于原 $r=25/8$，不是 $r=1/4$。
尚未穿过整个实际正帽、两个 bump 或连接部，尚未消去 tail labels，
所以不能把这里的 Robin 算子直接放到 $r=1/4$ 并称作完整帽 DN。

## 1. 真实坐标与方向

使用 [R119 实际长径向非线性 Dirichlet 定理](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md) 的同一对象：
$$
u=4c_0(r-25/8),\quad a=a_*e^{-\omega u},\quad
w=\frac a{4\omega},\quad E=1+w^2,\quad
\chi=\frac wa=\frac1{4\omega}.
\tag{C.1}
$$
这里 $7/5<\omega<3/2$、$0<a_*<7\cdot10^{-6}$；$E$ 在本篇只表示
半径坐标的系数。物理 $r$ 系数是 $(a_r)^2E$，不能把两者混淆。
真实目标和北侧高度分别为
$$
g_0=E\,da^2+a^2d\theta^2,\qquad Z=Z_{\rm ref}-v,
\qquad (Z_{\rm ref})_a=-w.
\tag{C.2}
$$
由于物理 $r$ 增大时 $a$ 减小，R126 使用的框架是
$$
X=-\frac{F_a}{\sqrt E},\qquad Y=\frac{F_\theta}{a},\qquad
n=Y\times X=\frac{F_a\times F_\theta}{a\sqrt E}.
\tag{C.3}
$$
在小球内它保持北极方向 $n_z>0$。

定义完整相对状态
$$
P=\frac{v_\theta}{aw},\quad
U=\frac{v_{\theta\theta}}{aw},\quad
\mathcal K=\frac{v_a}{w},\quad
V=\frac{v_{a\theta}}{w}=\mathcal K_\theta,
$$
$$
D=1-w^2\bigl(2\mathcal K+\mathcal K^2+EP^2\bigr),\qquad
J=1+\mathcal K+EU.
\tag{C.4}
$$
$\mathcal K$ 是高度斜率状态，包含 R119 的 mean 小根；它不是目标 Gaussian
曲率，后者记 $K_g$。完整 gradient 恒等式给
$$
n_z^2=1-\frac{Z_a^2}{E}-\frac{Z_\theta^2}{a^2}
=\frac DE,
\qquad n_z=\frac{\sqrt D}{\sqrt E}.
\tag{C.5}
$$

## 2. 准确曲率边界：不需要二阶径向 trace

任意 Euclidean 坐标函数的内在 Hessian 满足
$\nabla_g^2 Z=n_z\,\mathrm{II}$。
本目标在 $(a,\theta)$ 中有
$\Gamma^\theta_{a\theta}=1/a$、$\Gamma^a_{\theta\theta}=-a/E$。
所以按 (C.3) 的物理 $r$ 方向，
$$
\begin{aligned}
\nabla_g^2 Z(X,Y)
&=-\frac{Z_{a\theta}-Z_\theta/a}{a\sqrt E}
=\frac{w(V-P)}{a\sqrt E},\\
\nabla_g^2 Z(Y,Y)
&=\frac{Z_{\theta\theta}+aZ_a/E}{a^2}
=-\frac{wJ}{aE}.
\end{aligned}
\tag{C.6}
$$
因此完整真实输出为
$$
\boxed{
B=\chi\frac{V-P}{\sqrt D},\qquad
C=-\chi\frac{J}{\sqrt E\sqrt D},\qquad
A=\frac{K_g+B^2}{C}.
}
\tag{C.7}
$$
最后一条使用已经解出的真实 Gauss 方程；不再要求候选另供 $v_{aa}$。
对于同一原始长尾，
$$
K_g=\frac{\chi^2}{E^2},\qquad
A_{\rm ref}=-\frac\chi{E^{3/2}},\qquad
B_{\rm ref}=0,\qquad C_{\rm ref}=-\frac\chi{\sqrt E}.
\tag{C.8}
$$
这些符号和 $A_{\rm ref}C_{\rm ref}=K_g>0$ 一致。

在内端 $t=L$，令真实 Dirichlet 数据为 $f_*$。
R119 解给出的全部状态是
$$
P=(f_*)_\theta,\quad U=(f_*)_{\theta\theta},\quad
\mathcal K=\mu_L(h)+2f_*+h_t(L),\quad
V=\partial_\theta[2f_*+h_t(L)].
\tag{C.9}
$$
这是准确的两端 Dirichlet-to-curvature map。
即使 $f_*=0$，另端数据 $f_B$ 也会经有限长度反射产生非零 $h_t(L)$；
不能因此把 $B,C$ 设置为 reference 值。

平均高度仍是 R119 的输出
$v_0(L)-v_0(0)=\int_0^L aw\mu_t(h)\,dt$。
它不出现在 (C.7) 的曲率里，却是最终位置接合的一条真实条件。
物理高度径向迹也完整保留：
$$
v_r=-4c_0\omega aw\mathcal K,\qquad
Z_r=c_0a^2(1+\mathcal K).
\tag{C.10}
$$
(C.7) 是非线性曲率迹，不是 R37/R74 的 grounded 线性 flux。
需要该 flux 时仍须使用完整原法向/shear 变换。

## 3. 全角严格小球与 mean 曲率输出

R119 的真实定理允许
$$
\|(f_B,f_*)\|_{\partial,\sigma}\le2^{-25},\qquad
\|h\|_{\mathcal Y_\sigma}\le r_*=2^{-20}.
$$
由其完整 Fourier 代数估计，
$N=\|P\|+\|\mathcal K\|+\|U\|+\|V\|<4r_*$，
$|\mu_t(h)|<256r_*^2$。该强范数包含完整角频率及径向 supremum，
因此下列点值界对整个真角圈成立。
由 (C.1) 有
$$
0<w<\frac1{800000},\quad 0<\chi<\frac5{28},\quad
E<1+\frac1{800000^2}.
$$
准确有理算术给
$$
|D-1|\le w^2(2N+N^2+EN^2)<2^{-55},\qquad
|J-1|\le(1+E)N<9r_*.
\tag{C.11}
$$
从而 $D,J>0$，曲率图没有分母问题，并有
$$
\left|\frac C{C_{\rm ref}}-1\right|<10r_*,\qquad
|B|<2r_*,\qquad |C-C_{\rm ref}|<2r_*.
\tag{C.12}
$$

完整 mean 不能指定为 reference。它虽然是二次小量，但确实是输出。
为给一个明确界，写 $x=D-1$，
$$
D^{-1/2}=1+w^2\mathcal K+
\tfrac12w^2(\mathcal K^2+EP^2)+R,
\qquad |R|\le x^2.
$$
因为 $|x|<1/4$，Taylor 余项常数
$(3/8)(4/3)^{5/2}<1$，所以这个不等式成立。
又 $\langle U\rangle=0$、$\langle\mathcal K\rangle=\mu_t(h)$。
将它乘以 $J$ 并取 mean，得到
$$
\left|\frac{\langle C\rangle}{C_{\rm ref}}-1\right|
\le E|\mu_t(h)|+7w^2N^2
<(256+368w^2)r_*^2<257r_*^2.
\tag{C.13}
$$
其中 $7w^2N^2$ 的来源是
$|\langle\mathcal K^2+E\mathcal KU\rangle|w^2<3w^2N^2$，
乘以 $J$ 的下一二次项 $<3w^2N^2$，以及
$|JR|<18w^4N^2<w^2N^2$。
因而
$$
\boxed{\quad
|\langle C\rangle-C_{\rm ref}|<46r_*^2.
\quad}
\tag{C.14}
$$
该 bound 是输出误差预算，不允许把输出直接清零。
对本题真实偶反射四重数据，$P,V$ 奇、$D$ 偶，故 $B$ 为奇函数、
$\langle B\rangle=0$ 准确成立；这符合 R126 从腰传播的 mean $B$ 行。

脚本 `scripts/fourfold_phase_codazzi_regular_trace_budget.py` 用准确有理数
核验 (C.11)–(C.14) 及下一节的完整频率常数。它检查的是本证明的算术门，
没有声称运行一个尚未构造的全帽 nonlinear solver。

## 4. 保留有限长度反射的完整线性 Robin 关系

在线性化的零状态，$\mu=0$。对 $m\in4\mathbb Z\setminus\{0\}$、$M=|m|$，
R119 的真实两端输出是
$$
\mathcal K_m(L)=c_M(f_*)_m-s_M(f_B)_m,
\quad c_M=M\coth(ML),\quad s_M=Me^{-2L}\operatorname{csch}(ML).
\tag{C.15}
$$
它与 $2f_*+h_t(L)$ 一致，且 $s_M$ 不是零。
对 (C.7) 完整求一阶变分，包括 $D^{-1/2}$ 的一阶项，得到
$$
\delta B=\chi\partial_\theta(\mathcal K-f_*),\qquad
\delta C=-\chi\sqrt E\,(\mathcal K+\partial_\theta^2f_*).
\tag{C.16}
$$
这里 $\sqrt E$ 不能漏掉；它来自
$\delta(J/\sqrt D)=E\mathcal K+E U$。

令 $\delta C_\perp$ 表示非mean部分。消去 $(f_*)_m$ 后，准确得到
$$
\boxed{
(\delta B)_m=
\frac{im(c_M-1)}{\sqrt E(M^2-c_M)}(\delta C)_m
-\chi\frac{im\,s_M(M^2-1)}{M^2-c_M}(f_B)_m.
}
\tag{C.17}
$$
这是完整频率的真实长尾线性 Robin 图和非零反射源。
当 $f_B=0$，其有限长度 Fourier multiplier 为
$im(c_M-1)/(\sqrt E(M^2-c_M))$。
只有在**另外取无限长度极限**时它才趋于 $i\operatorname{sgn}(m)/\sqrt E$；
本合同不作这个极限。

由于 $M\ge4,L>1,e>2$，
$$
\coth(ML)<\frac{257}{255},\qquad
\frac{M^2}{M^2-c_M}\le\frac{1020}{763}<\frac32,
$$
$$
\frac{M(c_M-1)}{M^2-c_M}
=\frac{M\coth(ML)-1}{M-\coth(ML)}
\le\frac{773}{763}<2.
\tag{C.18}
$$
本节明确采用非零物理模的齐次二阶权
$$
\|f\|_{A^0_\sigma}
=\sum_{m\in4\mathbb Z\setminus\{0\}}e^{\sigma|m|}|f_m|,
\qquad
\|f\|_{\dot A^2_\sigma}
=\sum_{m\in4\mathbb Z\setminus\{0\}}e^{\sigma|m|}|m|^2|f_m|.
\tag{C.19}
$$
这与 R119 的边界权一致，零模独立处理。
所以 $f_*$ 到 $\delta C_\perp/(\chi\sqrt E)$ 的主算子
$M^2-c_M$ 有同宽 $A^0_\sigma\to\dot A^2_\sigma$ 逆范数 $<3/2$，
而 (C.17) 的齐次 Robin 图在同一 $A^s_\sigma$ 上范数 $<2$。
这不删除任意低非零频率；最小的真实频率就是 $M=4$。
mean 行仍由 (C.13) 的完整非线性输出给出。
如果改用非齐次权 $(1+|m|)^2$，必须乘上
$(1+1/4)^2=25/16$；对应的逆范数安全界是 $<75/32$，不能仍写 $<3/2$。

## 5. 给真正 body/cap 求解器的合同

使用这个接口时，边界未知至少包括实际 $f_*$ 以及 R119 安装图给的
$f_B$ 和 labels。必须先由同一 nonlinear Dirichlet 解取得
$\mathcal K_*=\mu_L+2f_*+h_t(L)$，再用 (C.7)、(C.9) 形成 $(B,C)$。
同时保留 (C.10) 和 mean 高度输出，以便与实际位置/框架接合。

这不会替代尚未解的 R119 内端 scalar residual
$$
\mathfrak F=k_B+C_Lf_B-S_Lf_*-E_D=0,
\tag{C.20}
$$
也不会替代两个实际 bump 的条件。
一个有限两场 solver 若使用 (C.17) 作线性边界预条件，必须把 (C.7) 的
真实非线性差、非零反射源和 mean 输出作为未清零的 residual 保存。
只有穿过真实 body、连接和原长尾之后，才能称为 $r=1/4$ 的实际 cap map。

最后，当前 `SymmetricAffineGeometry` 中的 frozen phase/base BSpline
定义域是 $[-3,3]$。直接对该浮点对象在 $r=25/8$ 求值会作多项式外插，
并非本合同的已安装 long-radial/graft 对象。任何未来 producer 都须显式
切换到真实连接和 (C.1)；不得以这种外插值充当 regular 端数据。
