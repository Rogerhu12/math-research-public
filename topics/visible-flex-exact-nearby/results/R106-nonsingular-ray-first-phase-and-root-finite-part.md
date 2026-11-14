# R106：真实非均值射线首相位的降阶、根部无奇异有限部和字段接口

2026-11-12，constructive-route。

**状态：完整证明的相位重建接口；真实候选已有一次小范围字段执行。**
本篇把 R46 的整个有符号首相位写成两个只用一阶主系数的积分及准确端点项，
再把 simple turn 的沿射线有限部化为连续函数积分。它保留原先角平均会消掉的
角散度和根端有限项，正好补 R104 所需的非均值系数输入。
当前没有完整返回相位的角乘子范数，也没有宣布 R104 的强余项或全 PDE 逆通过。

R37 的实际算子、同一个平移核零阶口径、真实无限 R33 图和参数身份始终固定。
核代码仅作已认证几何球上的代数；真实射线、其雅可比、连续积分及角 strip
必须另外由同一对象支付，不能以浮点 principal 图或平均相位替代。

## 1. 严格负区的准确沿射线降阶

令
$$
P=\operatorname{div}(A\nabla)+d,\qquad
A=\begin{pmatrix}a&b\\b&c\end{pmatrix},\quad
a>0,\quad \mu=\sqrt{b^2-ac}>0,
$$
$$
L=\log\mu,\quad q=b/a,\quad \nu=\mu/a,\quad
\mathcal F=\mu^{1/2}P(\mu^{-1/2}),\quad V=\mu^{-1}A\nabla L .
\tag{106.1}
$$
所有量是同一个真实散度密度算子的系数；特别 $d$ 包含 R37 的完整零阶修正。
R46/R50 的逐点恒等式为
$$
\frac{\mathcal F}{\mu}
=\frac{d-\frac14\nabla L^tA\nabla L}{\mu}
-\frac12\operatorname{div}V .
\tag{106.2}
$$
允许把第一项准确分解为
$$
\frac{d-\frac14\nabla L^tA\nabla L}{\mu}
=D+\partial_\theta S .
\tag{106.3}
$$
这里 $D$ 是约化密度；它本身既不等于 $\mathcal F/\mu$，也不允许沿射线时
丢掉 $\partial_\theta S$。

取 R46 的支约定 $\sigma=\pm1$：
$$
\Theta_r=v_\sigma(r,\Theta),\qquad
v_\sigma=q-\sigma\nu,\qquad
\Theta(r_0,\eta)=\eta,\qquad J=\Theta_\eta>0 .
\tag{106.4}
$$
真实有符号半程首相位为
$$
h_\sigma(\eta)=\frac12\int_{r_0}^{r_1}
       (\mathcal F/\mu)(r,\Theta(r,\eta))J(r,\eta)\,dr .
$$

**定理106.1。** 在该实际闭严格区上有准确恒等式
$$
\boxed{
h_\sigma=
\frac12\int_{r_0}^{r_1}(D\circ\Theta)J\,dr
+\frac12\partial_\eta\int_{r_0}^{r_1}S\circ\Theta\,dr
-\frac14\left[J(V_r+\sigma L_\theta)\circ\Theta\right]_{r_0}^{r_1}.}
\tag{106.5}
$$
第二个积分中没有额外 $J$；在其外取完整输入标签导数。端点项不作为时间密度
积分。若实际时间为 $\tau$，前两项准确乘 $dr/d\tau$，不能换为绝对值。

**证明。** 任意向量场 $V$ 的真实拉回满足
$$
(\operatorname{div}V)\circ\Theta\,J
=\partial_r(JV_r\circ\Theta)
+\partial_\eta[(V_\theta-v_\sigma V_r)\circ\Theta].
\tag{106.6}
$$
这由 $J_r=(v_\sigma)_\theta\circ\Theta\,J$ 展开后逐项相消。又
$$
b-av_\sigma=\sigma\mu,\qquad
c-bv_\sigma=\sigma\mu v_\sigma,
$$
故
$$
V_\theta-v_\sigma V_r
=\sigma(L_r+v_\sigma L_\theta)
=\sigma\partial_r[L(r,\Theta)].
\tag{106.7}
$$
把 (106.3)、(106.6)、(106.7) 代入 (106.2)，两次普通积分即得 (106.5)。
所有端点都使用同一条真实射线和同一个 $J$。有限径向 spline 切分处，
只有当这些实际通量连续且所有积分使用同一符号时，内端点才准确抵消。$\square$

这个降阶直接消去了严格区中 $\operatorname{div}V$ 的额外径向微分。
它不能省掉证明真实射线、$J$ 和角向微分所需的实际正则与有向误差。

## 2. 当前 R37/R33 图上的完整字段

本节 $r,\theta$ 都是原物理坐标，向量以旋转柱坐标基表示。记
$$
C=F_\theta\times F_r,\quad G=C\cdot C,\quad R=F\cdot F,\quad
H=C\cdot F,\qquad \zeta=\frac{H}{\sqrt{GR}},
$$
$$
l=C\cdot F_{rr},\quad m=C\cdot F_{r\theta},\quad n=C\cdot F_{\theta\theta},
\quad a_0=-n/G,\quad b_0=m/G,\quad c_0=-l/G .
\tag{106.8}
$$
这里 $a_0=\zeta^2a$；不是内在周长半径。真实目标曲率为 $K_0(r)<0$。置
$$
k=\sqrt{-K_0},\qquad
\omega_0=\frac{(ln-m^2)/G^2-K_0}{a_0},\qquad
\widehat c_0=\frac{b_0^2+K_0}{a_0}.
\tag{106.9}
$$
于是 $\mu=k/\zeta^2$，$q=b_0/a_0$，$\nu=k/a_0$。原平移核势的缩放量为
$$
d_0=\frac1R\left[
a_0\left(|F_r|^2-\frac{(F\cdot F_r)^2}{R}\right)
+2b_0\left(F_r\cdot F_\theta-\frac{(F\cdot F_r)(F\cdot F_\theta)}R\right)
+c_0\left(|F_\theta|^2-\frac{(F\cdot F_\theta)^2}{R}\right)\right].
\tag{106.10}
$$
固定 R46/R50 所用的真实函数
$$
\ell=\partial_\theta\log(F_z/r)-\partial_\theta\log|F| .
\tag{106.11}
$$
非零 $r$ 处可以直接用 $F_{z,\theta}/F_z-(F\cdot F_\theta)/R$；
含腰部的盒必须使用已经支付的平滑商，不能在包含零的 $F_z$ 上相除。

令 $z_r=\partial_r\log\zeta,z_\theta=\partial_\theta\log\zeta$。由六个真实二jet：
$$
z_i=\frac{C_i\cdot F}{H}-\frac{C\cdot C_i}{G}
                      -\frac{F\cdot F_i}{R},\quad i=r,\theta,
$$
$$
C_r=F_{r\theta}\times F_r+F_\theta\times F_{rr},\qquad
C_\theta=F_{\theta\theta}\times F_r+F_\theta\times F_{r\theta}.
$$
其中 $C\cdot F_i=0$ 已准确使用。故
$$
L_r=\frac{K_0'}{2K_0}-2z_r,\qquad L_\theta=-2z_\theta.
\tag{106.12}
$$
本篇字段为
$$
\boxed{
D=\frac{d_0+\omega_0(\ell^2+\ell L_\theta)
-\frac14(a_0L_r^2+2b_0L_rL_\theta+\widehat c_0L_\theta^2)}k,}
$$
$$
\boxed{
S=\frac{\omega_0\ell}{k},\qquad
V_r=\frac{a_0L_r+b_0L_\theta}{k},\qquad
V_\theta=\frac{b_0L_r+\widehat c_0L_\theta}{k}.}
\tag{106.13}
$$

**证明它确属同一完整零阶口径。** 实际 R37 修正是
$\widehat d=d+(\omega\ell)_\theta+\omega\ell^2$、
$\omega=\omega_0/\zeta^2$，而 $\mu=k/\zeta^2$、$k_\theta=0$。
因此
$$
\frac{(\omega\ell)_\theta}{\mu}
=\partial_\theta(\omega_0\ell/k)+(\omega_0\ell/k)L_\theta .
$$
连同原 $d=d_0/\zeta^2$，得到 (106.3)、(106.13)。所以该 $D$ 与冻结
beta bulk 源的约化密度准确相同，$S$ 正是其角平均分部所丢掉的通量。$\square$

代码 scripts/fourfold_subprincipal_ray_fields.py 实现 (106.8)–(106.13)，
检查 $-K_0,G,R,H,a_0$ 的正实部，保留复球与参数宽度，不作参数中点替换。
它只对调用者提供的真实无限图六jet作代数，并不自动产生几何证书。

### 2.1 可以直接执行的完整角范数合同

假设同一实际射线及 $J$ 已在标签 strip $|\Im\eta|\le s_1$ 上认证，且
$$
|(D\circ\Theta)J|\le B(r),\quad |S\circ\Theta|\le Q(r),\quad
|J(V_r+\sigma L_\theta)\circ\Theta|_{r_i}\le E_i .
$$
对 $0<s_0<s_1$，(106.5) 和 Cauchy 给
$$
\|h_\sigma\|_{\infty,s_0}\le
\frac12\int B(r)|dr|
+\frac1{2(s_1-s_0)}\int Q(r)|dr|+\frac{E_0+E_1}{4}.
\tag{106.14}
$$
若标签周期已经准确归一为 $2\pi$，再取 $0<s<s_0$、整数 $m\ge0$，则
$$
M_{m,s}(h_\sigma)\le
2^{m/2}\|h_\sigma\|_{\infty,s_0}
\left[1+2\sum_{j\ge1}(1+j)^m e^{-(s_0-s)j}\right].
\tag{106.15}
$$
这里 $M_{m,s}$ 是带 $e^{s|j|}$ 的 R104 乘子和。证明用
$|(h_\sigma)_j|\le\|h_\sigma\|_{\infty,s_0}e^{-s_0|j|}$
及 $\langle j\rangle^m\le(1+|j|)^m$。级数可用有限阶几何级数导数准确求和。
因此只要真正的 $B,Q,E_i$ 已付，就得到可接 R104 的有限数；
它们当前尚未由平均 beta 或 principal endpoint 图自动提供。

## 3. Simple turn 的沿射线连续化

在每一个实际根旁，**先把径向方向改为指向负区**，记该坐标为 $\rho$。
$a,b,c,d$ 都是换向后的密度系数；正根处原 mixed 系数须相应反号。
假设在实际共同 root germ 中
$$
\mu=\kappa(\rho,\theta)\sqrt\rho,\qquad
\kappa>0,\qquad k_*=\kappa/a,\qquad q=b/a,\qquad l=\log\kappa.
\tag{106.16}
$$
此处 $\kappa$ 是实际散度密度的根因子。它不是 R83 的目标曲率
$K_0(r)/(r-t)$；混用二者会改变后面的高度相关项。

R46 (9.6)–(9.7) 的准确分解为
$$
\mathcal F/\mu=A_*\rho^{-5/2}+B_*\rho^{-3/2}+C_*\rho^{-1/2},
$$
$$
A_*=\frac5{16k_*},\qquad
B_*=\frac{a l_\rho+b l_\theta-a_\rho-b_\theta}{4\kappa},\qquad
C_*=\frac{d-\frac12\operatorname{div}(A\nabla l)
                      +\frac14\nabla l^tA\nabla l}{\kappa}.
\tag{106.17}
$$
令 $\rho=s^2$。真正根发出的支满足一个无奇异 ODE：
$$
\Theta_s=2s\,q(s^2,\Theta)-2\sigma s^2 k_*(s^2,\Theta),\qquad
\Theta(0,\eta)=\eta,\quad J=\Theta_\eta .
\tag{106.18}
$$
所有所需导数在当前实际 root germ 内支付。定义
$$
N_\sigma(s,\eta)
=J(s,\eta)\,[A_*(s^2,\Theta)+s^2B_*(s^2,\Theta)
                                      +s^4C_*(s^2,\Theta)] .
\tag{106.19}
$$
半程相位的密度准确是 $N_\sigma(s,\eta)/s^4\,ds$。

**定理106.2。** 置 $D_t=\partial_\rho+q\partial_\theta$，根值用下标0。
则
$$
N_\sigma=c_0+c_2s^2+O(s^4),\qquad
c_0=\frac5{16k_{*0}},\quad
c_2=\frac{q_{\theta0}-(D_t\log k_*)_0}{16k_{*0}}.
\tag{106.20}
$$
特别 $s^1,s^3$ 系数都准确为零，没有沿射线有限部中的 logarithm 项。

**证明。** (106.18) 给
$$
\Theta=\eta+q_0s^2-\frac{2\sigma}3k_{*0}s^3+O(s^4),\qquad
J=1+q_{\theta0}s^2-\frac{2\sigma}3(k_{*0})_\theta s^3+O(s^4).
$$
由于 $B_*=(D_t\log k_*-q_\theta)/(4k_*)$，
$s^2$ 系数为 $D_t A_*+q_\theta A_*+B_*$，化简得到 (106.20)。
$s^3$ 系数只来自 $JA_*$，准确为
$$
-\frac{2\sigma}3\partial_\eta(k_{*0}A_{*0})
=-\frac{2\sigma}3\partial_\eta(5/16)=0 .
$$
各系数在原函数上至少有四阶实际 $s$ 正则即可使用下式，不把全域 C4 spline
解释为任意跨 knot 高导数。$\square$

若 $N_\sigma$ 在同一已付标签范数上有连续第四 $s$ 导数，则
$$
g_\sigma(s)=
\frac{N_\sigma(s)-c_0-c_2s^2}{s^4}
=\frac16\int_0^1(1-u)^3\partial_s^4N_\sigma(us)\,du ,
\tag{106.21}
$$
在 $s=0$ 取 $\partial_s^4N_\sigma(0)/24$。这是无相近发散项相减的准确表示。
因此至 $\rho=R^2$ 的半程有限部为
$$
\boxed{\quad
\operatorname{FP}h_\sigma
=\int_0^R g_\sigma(s)\,ds-\frac{c_0}{3R^3}-\frac{c_2}{R}.
\quad}
\tag{106.22}
$$
若公共 Wiener norm 下有
$\sup_s\|\partial_s^4N_\sigma\|\le N_4$、$\|c_i\|\le C_i$，则
$$
\|\operatorname{FP}h_\sigma\|
\le \frac{R N_4}{24}+\frac{C_0}{3R^3}+\frac{C_2}{R}.
\tag{106.23}
$$

R83 的真实根数据准确给 $Y_0'=1/k_{*0}$ 和
$h_1=(D_t\log k_*-q_\theta)_0$，所以
$$
\boxed{\quad c_0=5Y_0'/16,\qquad c_2=-Y_0'h_1/16.\quad}
\tag{106.24}
$$
这些是物理根标签下的一形式系数。换标签时两者都须乘真实标签导数。

## 4. 直接使用已恢复 D 字段的更低阶 root 公式

当前 R37 的 $\ell$ 平滑且 $\mu\asymp\sqrt\rho$，故
$S=O(\rho^{-1/2})$；$\int S\,d\rho$ 已可积。
R50 的约化密度减项表明
$$
D=\widetilde A\rho^{-5/2}+\widetilde B\rho^{-3/2}
                                      +O(\rho^{-1/2}),
\quad
\widetilde A=-\frac1{16k_*},\quad
\widetilde B=-\frac{D_t l}{4k_*}.
\tag{106.25}
$$
$D$ 与 R50 含完整 $d$ 的约化密度只差一个 $O(\rho^{-1/2})$ 的角散度，
所以两个不可积系数相同。

置 $\widetilde N=s^5JD(s^2,\Theta)$。与 §3 同样的展开给
$$
\boxed{\quad
\widetilde c_0=-Y_0'/16,\qquad
\widetilde c_2=Y_0'\,[h_1-4(D_t\log\kappa)_0]/16,
\quad \widetilde N_1=\widetilde N_3=0.\quad}
\tag{106.26}
$$
仍可用 (106.21)–(106.23)，但换成 $\widetilde N,\widetilde c_i$。
注意 $D_t\log\kappa$ 依赖同一个实际 height；不能把 R83 的曲率根因子
导数或 grounded height 的值代入原 R37 的 $D$。

还须保留一个原平均算法看不见的根端常数。由
$$
V_\rho=\frac1{2k_*}\rho^{-3/2}
                 +\frac{D_t\log\kappa}{k_*}\rho^{-1/2}
$$
及 (106.18)，$JV_\rho$ 的有限常数为零：
唯一可能的 $s^3$ 项是
$-\frac{2\sigma}3\partial_\eta[k_{*0}/(2k_{*0})]=0$。
而 $JL_\theta\to\partial_\eta\log\kappa_0$。故根到 cut 的准确式为
$$
\boxed{
\begin{aligned}
\operatorname{FP}h_\sigma={}&
\operatorname{FP}\left[\frac12\int_0^{\rho_c}D\circ\Theta\,J\,d\rho\right]
+\frac12\partial_\eta\int_0^{\rho_c}S\circ\Theta\,d\rho\\
&-\frac14[J(V_\rho+\sigma L_\theta)\circ\Theta]_{\rho_c}
+\frac{\sigma}{4}\partial_\eta\log\kappa_0 .
\end{aligned}}
\tag{106.27}
$$
最后一项是周期导数，平均为零；非均值相位中不能删除。

在原 R37 height、径向 $K_0$ 下，$\kappa_0=\sqrt{|K_0'(t)|}/\zeta_0^2$，所以
$$
\partial_\eta\log\kappa_0=-2J_0(\log\zeta)_\theta .
\tag{106.28}
$$
它可由根上的真正二jet直接计算，不除以 $K_0$ 或 $F_z$。核代码的
root_log_density_coefficient_label_derivative 实现此式。
代码的 root_phase_from_reduced_terms 保留 (106.27) 的全部四项。

## 5. 与实际 canonical cut 的非均值比较

本节说明 (106.22) 不是一个另造的减项规范。设合法 canonical 坐标在原根图为
$$
\xi=A_0(\theta)\rho+B_0(\theta)\rho^2+O(\rho^3),\qquad
\phi(0,\theta)=H_0(\theta),\quad A_0>0,\ H_0'>0 .
\tag{106.29}
$$
本节的 $A_0,B_0$ 只指坐标系数，区别于 (106.17)。
canonical 两支满足
$\phi=H_0(\eta)-\sigma\frac23\xi^{3/2}$，主特征方程给
$$
H_0' k_{*0}=A_0^{3/2}.
\tag{106.30}
$$
散度密度的真实 Jacobian 和正 height 共轭共同给准确一形式恒等式
$$
(\mathcal F/\mu)(\rho,\Theta)J\,d\rho
=H_0'\left[\frac5{16\xi^{5/2}}+
   \frac{V_{\rm can}(\xi,H_0-\sigma2\xi^{3/2}/3)}{\sqrt\xi}\right]d\xi .
\tag{106.31}
$$
这是 R46 的完整密度变换，不能只变 principal phase。

沿同一物理射线，
$$
\xi=A_0\rho+(A_0' q_0+B_0)\rho^2
       -\frac{2\sigma}3 A_0' k_{*0}\rho^{5/2}+O(\rho^3).
$$
所以 $\xi^{-3/2}$ 的有限常数为
$\sigma A_0'k_{*0}A_0^{-5/2}$。canonical 半程的唯一不可积分项之原函数为
$-5H_0'\xi^{-3/2}/48$，其下端贡献给
$$
\boxed{\quad
\operatorname{FP}_{\rho}h_\sigma
-H_0'\operatorname{FP}_{\xi}h_{{\rm can},\sigma}
=\frac{5\sigma}{48}\partial_\eta\log A_0.
\quad}
\tag{106.32}
$$
两式上端必须是同一实际点。若只取角平均，右边为零，恢复 R46/R50
固定材料有限部不变；逐标签时这个项不能无条件抹去。

本题 R83 的准确 root-anchored 构造满足
$\xi=\rho+c\rho^2+O(\rho^3)$，所以 $A_0\equiv1$，
(106.32) 的额外项准确为零。且 $c=2h_1/5$，故
$c_2=-5Y_0'c/32$，和 (106.24) 相符。
这里使用的是 R83 已证明的实际坐标 Taylor 恒等式，不是浮点拟合。

## 6. 两个准确校准

对自由 Tricomi 算子 $P=\partial_\rho^2-\rho\partial_\theta^2$，
$k_*=1$，$\mathcal F/\mu=5/(16\rho^{5/2})$。
本篇给
$$
D=-1/(16\rho^{5/2}),\quad S=0,\quad
V_\rho=1/(2\rho^{3/2}),\quad L_\theta=0.
$$
到 cut $R^2$ 时，(106.27) 的前一有限部是 $+1/(48R^3)$，
cut 项是 $-1/(8R^3)$，总和为 $-5/(48R^3)$，
与 (106.22) 的 $c_0=5/16,c_2=0$ 完全一致。
严格区 $[\rho_0,\rho_1]$ 则给两个端点之差；定向不能混用。

再作任意实际正角 height $t(\theta)$ 共轭 $\widetilde P=tPt$。
R46 的 $\mathcal F/\mu$ 准确不变；本篇字段的改变量为
$$
\Delta D=-\sqrt\rho\,(\log t)_{\theta\theta},\qquad
\Delta L_\theta=2(\log t)_\theta,\qquad
\Delta\log\kappa_0=2\log t .
$$
沿 $\Theta=\eta-\sigma2\rho^{3/2}/3$，令 $l=\log t$，
$\int_0^{\rho_c}\sqrt\rho\,l''(\Theta)d\rho
=-\sigma[l'(\Theta_c)-l'(\eta)]$。
(106.27) 中 bulk、cut 和 root 的改变量逐项相消。
若删除根端 $\sigma\partial_\eta\log\kappa_0/4$，这一准确 height 不变性就被破坏。
这也是非均值根常数的独立符号与因子核对。

## 7. 同 R104 的标签、完整 frame 和普通源接线

本篇相位系数是标签一形式。若 $\eta=\Psi(x)$，则
$$
h_x(x)=h_\eta(\Psi(x))\Psi'(x).
\tag{106.33}
$$
物理 quarter 标签周期为 $\pi/2$，归一标签 $x=4\eta$ 时
$h_x(x)=h_{\rm ph}(x/4)/4$。如果在核调用中已经传入
$J=\partial\Theta/\partial x$，结果已是归一系数，不可再除以4。
对第二项取 Fourier 标签导数时是 $ij$，物理角微分才是 $4ij$。
最终 R46 (7.3) 的真实共轭同样以 (106.33) 转移，不改变完整首系数的平均。

两个真实 roots、严格区、Ai/contact 和所有端口按 R46 §9 的实际假设接好后，
角平均恢复已认证 R50 beta。同一个 principal 圆返回或 beta 平均单独成立，
并不证明这些完整端口/源/强余项已就绪。

特别 R46 的局部物理 cut 源和 R104 的归一标签右端不是同一个 norm。
须保留真实注入 $\mathcal J_{\rm wire}$，其包含 $x=4\eta$、
完整 $\mathscr G_H$ 及实际端口变换。R107 已把弱散度源先重建为真实 Cauchy 源；
再用实际 $K_{{\rm wire},s+1}=\|\mathcal J_{\rm wire}\|$ 接
R104 (104.26)，不能默认这个常数为1。
首相位的完整非均值预算与普通源范数是两份实际合同，本篇没有相互替代。

## 8. 已执行内容、原始输入与剩余计算

2026-11-12 原生环境恢复后，确已执行以下同对象小计算：
准确 $\delta_5\pm10^{-9}$，$r=1/8$，Q512，192bit，
R33 真无限 primitive 的六jet及 $K_0,K_0'$，八个准确物理角
$\theta_j=\pi j/16$（$j=0,\ldots,7$），逐点送入 (106.8)–(106.13)。
原始输入分别为：

- object SHA256：91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848；
- origin：0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b；
- direction：8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab；
- 核源码：0e5b12ddcd259d24c4e004d7353e2ce13375adee12de050551d423ff3e1874aa。

实际执行约0.47秒，得到有限区间场；随后执行器再次 unavailable。
对话中留下的显示球记录和精确命令保存在配套 note，**仅作为真实执行诊断**：
没有补造丢失的大报告，没有把八角点推广成连续角覆盖、真实射线积分、
整个首相位或 $M_{S+3}(b-\beta)$ 证书。

下一实际计算直接使用本篇已证公式：付同一真实 ray/J、两个有符号积分、
准确端点及 root 连续余项，然后把每段的完整标签函数经 R46 接入 R104。
当前还缺这些完整量及真实强余项；本篇不是课题闭族完成证书。
