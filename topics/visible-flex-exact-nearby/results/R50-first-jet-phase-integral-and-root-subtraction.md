# R50：完整首相位的分部降阶、物理减项与固定零阶口径

2026-11-12，visible-exact-astra-f6a2。

**状态：已证明的中间结论。** 在R46已经明确的同一双根完整网络前提下，
把其完整首相位平均改写为一个在严格负区只用主系数一阶的有限部积分。
这减少实际计算所需的全域几何导数；根端减项和连续区间积分仍须另付有限Taylor
数据。本文不给当前候选的相位数值或全频逆，也不省略R46的正帽/全源/余项前提。

## 1. 同一个真实算子与完整相位

设负组件为
\[
\Omega=(x_-,x_+)\times\mathbb R/(\ell\mathbb Z),
\qquad
Pu=\operatorname{div}(A\nabla u)+du,
\qquad A=\begin{pmatrix}a&b\\b&c\end{pmatrix},
\]
其中 \(a>0\)、\(\mu=\sqrt{b^2-ac}>0\)。在两个端点均有R46的真实
simple-turn坐标及合法有限Taylor展开。所有积分使用真实材料密度，不把
普通矩阵张量与散度密度混同。置
\[
 f=\log\mu,\qquad
 \mathcal F=\mu^{1/2}P(\mu^{-1/2})
 =d-\tfrac12\operatorname{div}(A\nabla f)
                         +\tfrac14(\nabla f)^tA\nabla f.
\tag{50.1}
\]
若实际两端网络满足R46 §9所列全部接线条件，则相对于
\(e^{2\pi i j\theta/\ell}\) 的完整往返首相位系数为
\[
 \langle\beta\rangle
 =\frac1{2\pi}\operatorname{FP}\int_\Omega
                    \frac{\mathcal F}{\mu}\,dx\,d\theta.
\tag{50.2}
\]
本文仅改写同一数值。它不从主返回旋转直接推断(50.2)已经是任何尚未构造的
闭帽网络的相位。

## 2. 精确降阶及根部边界有限项

定义
\[
 \boxed{\quad
 J=\frac1\mu\left[d-\frac14(\nabla\log\mu)^t
                                        A\nabla\log\mu\right].\quad}
\tag{50.3}
\]

**定理50.1。** 在上述前提及以下展开所需的有限实际正则下，
\[
 \boxed{\quad
 \operatorname{FP}\int_\Omega\frac{\mathcal F}{\mu}
 =\operatorname{FP}\int_\Omega J.
 \quad}
\tag{50.4}
\]
严格区的 \(J\) 点值只使用 \(A,d\) 和 \(A\) 的一阶导数。

**证明。** 用 \(\nabla(\mu^{-1})=-\mu^{-1}\nabla f\)，逐项计算得到
\[
 \frac{\mathcal F}{\mu}
 =J-\frac12\operatorname{div}
                   \left(\mu^{-1}A\nabla\log\mu\right).
\tag{50.5}
\]
在任意离根正距离的截断区域，此式是普通散度恒等式。角方向周期，故只有
两端真实法向边界项。分别以 \(\rho>0\) 指向负区，写
\[
 \mu=\kappa(\rho,\theta)\sqrt\rho,\qquad
 \kappa>0,\qquad l=\log\kappa.
\tag{50.6}
\]
在这一真实坐标中，混合密度系数 \(b\) 已按方向变换。径向通量是
\[
 \mu^{-1}(a f_\rho+b f_\theta)
 =\frac{a}{2\kappa}\rho^{-3/2}
       +\frac{a l_\rho+b l_\theta}{\kappa}\rho^{-1/2}.
\tag{50.7}
\]
所有系数有实际Taylor展开；右边只有 \(\rho^{-3/2}\)、
\(\rho^{-1/2}\)、\(O(\rho^{1/2})\)，没有有限常数或log项。
所以两个边界通量的有限部分均为零，(50.5)给(50.4)。这也说明不能直接
把未减去发散项的边界通量当成零；消失的只是其有限常数。证毕。

若严格区径向只有分段有限光滑，上述等式可在各段积分。主系数和相应一阶
通量连续时，内部knot的边界项两两抵消；不会产生隐藏的点质量。
例如R46给出的真实 \(C^2\cap W^{3,\infty}\) 系数足够。

## 3. 新被积函数必须使用自己的物理减项

由(50.3)、(50.6)，准确分解为
\[
 J=\widetilde A\rho^{-5/2}
             +\widetilde B\rho^{-3/2}
             +\widetilde C\rho^{-1/2},
\tag{50.8}
\]
其中
\[
 \boxed{\begin{aligned}
 \widetilde A&=-\frac{a}{16\kappa},\\
 \widetilde B&=-\frac{a l_\rho+b l_\theta}{4\kappa},\\
 \widetilde C&=\frac1\kappa
           \left[d-\frac14(\nabla l)^tA\nabla l\right].
 \end{aligned}}\tag{50.9}
\]
故其两个不可积系数是
\[
 \boxed{\begin{aligned}
 g_0(\theta)&=-\frac{a(0,\theta)}{16\kappa(0,\theta)},\\
 g_1(\theta)&=
 \left.\frac{-a_\rho-3a\kappa_\rho/\kappa
                         -4b\kappa_\theta/\kappa}{16\kappa}
                                                   \right|_{\rho=0}.
 \end{aligned}}\tag{50.10}
\]
它们是 \(\widetilde A(0)\) 和
\(\widetilde A_\rho(0)+\widetilde B(0)\)，与R46原被积函数的
\(f_0,f_1\) 不同。具体地，本篇定义
\[
 \operatorname{FP}\int_\Omega J
 =\lim_{\epsilon_\pm\downarrow0}
 \left[\int_{\Omega_{\epsilon_\pm}}J
 -\sum_{i=\pm}\int_0^\ell
    \left(\frac23 g_{0,i}\epsilon_i^{-3/2}
                  +2g_{1,i}\epsilon_i^{-1/2}\right)d\theta\right].
\tag{50.11}
\]
不得用新的点值函数配旧 \(f_0,f_1\) 相减。

固定一个根collar \(0<\rho<\eta\)，其有限部分为
\[
 \int_0^\eta\int_0^\ell
   [J-g_0\rho^{-5/2}-g_1\rho^{-3/2}]\,d\theta\,d\rho
 -\int_0^\ell\left(\tfrac23g_0\eta^{-3/2}
                                  +2g_1\eta^{-1/2}\right)d\theta.
\tag{50.12}
\]
变数 \(\rho=s^2\) 把第一个积分化成有界连续函数的普通积分：
\[
 \begin{aligned}
 B(s,\theta)={}&
 2\frac{\widetilde A(s^2)-\widetilde A(0)
                       -s^2\widetilde A_\rho(0)}{s^4}\\
 &+2\frac{\widetilde B(s^2)-\widetilde B(0)}{s^2}
                         +2\widetilde C(s^2).
 \end{aligned}\tag{50.13}
\]
在 \(s=0\) 连续取值
\(\widetilde A_{\rho\rho}(0)+2\widetilde B_\rho(0)
+2\widetilde C(0)\)。避免相近数相减的准确表达为
\[
 B(s,\theta)=2\int_0^1(1-t)\widetilde A_{\rho\rho}(ts^2,\theta)dt
       +2\int_0^1\widetilde B_\rho(ts^2,\theta)dt
       +2\widetilde C(s^2,\theta).
\tag{50.14}
\]
所以一个可直接支付的全collar上界是
\[
 \|B\|_\infty\le
 \|\widetilde A_{\rho\rho}\|_\infty
       +2\|\widetilde B_\rho\|_\infty+2\|\widetilde C\|_\infty.
\tag{50.15}
\]
若还供应所需下一阶导数，则
\[
 \begin{aligned}
 \|B_s\|_\infty&\le\sqrt\eta\left(
 \tfrac23\|\widetilde A_{\rho\rho\rho}\|_\infty
       +2\|\widetilde B_{\rho\rho}\|_\infty
       +4\|\widetilde C_\rho\|_\infty\right),\\
 \|B_\theta\|_\infty&\le
 \|\widetilde A_{\rho\rho\theta}\|_\infty
       +2\|\widetilde B_{\rho\theta}\|_\infty
       +2\|\widetilde C_\theta\|_\infty.
 \end{aligned}\tag{50.16}
\]
这些来自对(50.14)求导和准确积分 \(\int_0^1t(1-t)dt=1/6\)、
\(\int_0^1t\,dt=1/2\)。例如用实矩形中点规则、网格宽
\(h_s,h_\theta\)，该普通双积分的误差不超过
\[
 \frac{\ell\sqrt\eta}{4}
       (h_s\|B_s\|_\infty+h_\theta\|B_\theta\|_\infty).
\tag{50.17}
\]
或直接用每格的有向函数包络，不必采用中点规则。

**输入阶数界线。** 严格区点值降阶不表示完整有限部证书只需主系数一jet。
根端 \(\kappa_\rho(0)\) 由
\(\kappa^2=(b^2-ac)/\rho\) 得到，确切地
\[
 \kappa_\rho(0)=\frac{\partial_\rho^2(b^2-ac)(0)}{4\kappa(0)}.
\tag{50.18}
\]
(50.15)–(50.17)又需要相应真实root Taylor数据。若根部collar严格处在一个
共同多项式knotspan内部，可在该局部单独支付；它不是从浮点根位置获得的免费输入。

## 4. R37固定型别算子的完整零阶项

令 \(A,d\) 为R32/R37的真实材料Darboux系数，
\[
 \widehat A=\begin{pmatrix}a&b\\b&c-\chi\omega\end{pmatrix},
 \quad \widehat d=d+(\chi\omega\ell_0)_\theta
                              +\chi\omega\ell_0^2,
\tag{50.19}
\]
其中 \(\ell_0\) 是R37选定的真实函数，这里下标避免与角周期 \(\ell\) 混淆。
本节所有 \(\mu,f,J\) 使用同一个 \(\widehat A,\widehat d\)。对任意固定严格截面，
一次角积分分部准确给
\[
 \int_0^\ell\frac{(\chi\omega\ell_0)_\theta}{\mu}d\theta
 =\int_0^\ell\frac{\chi\omega\ell_0 f_\theta}{\mu}d\theta.
\tag{50.20}
\]
因此平均相位也可用以下角平均被积函数：
\[
 \boxed{\quad
 \langle\beta\rangle=\frac1{2\pi}\operatorname{FP}\int_\Omega
 \frac{d+\chi\omega(\ell_0^2+\ell_0f_\theta)
                       -\tfrac14(\nabla f)^t\widehat A\nabla f}{\mu}.
 \quad}\tag{50.21}
\]
这只消去角积分中的导数，**不是**新的点值算子恒等式。原PDE、普通源、
边界及Newton残差仍使用(50.19)的完整 \(\widehat d\)。根旁新增零阶项除以
\(\mu\) 仅为可积的 \(\rho^{-1/2}\) 项；(50.10)的不可积减项不改变。

若保持同一主矩阵但换合法 \(\ell_0\) 为 \(\ell_1\)，则准确相位差为
\[
 \Delta\langle\beta\rangle
 =\frac1{2\pi}\int_\Omega
 \frac{\chi\omega(\ell_1-\ell_0)
                         (\ell_1+\ell_0+f_\theta)}{\mu}.
\tag{50.22}
\]
这是普通可积积分，明确显示选定零阶口径的重要性。它不是任意调相位而
不支付Newton扰动常数的许可。

## 5. 实际星形几何的三jet点值公式

在真实材料圆柱上，用外向叉积约定
\[
 X=F_r,\quad Y=F_\theta,\quad C=Y\times X,\quad
 A_* =|C|,\quad R=|F|,\quad h=C\cdot F>0,
 \quad \zeta=\frac{h}{A_*R}.
\tag{50.23}
\]
用 \(L_*=C\cdot F_{rr}\)、\(M_*=C\cdot F_{r\theta}\)、
\(N_*=C\cdot F_{\theta\theta}\)，准确有
\[
 a=-\frac{N_*}{\zeta^2 A_*^2},\quad
 b=\frac{M_*}{\zeta^2 A_*^2},\quad
 c=-\frac{L_*}{\zeta^2 A_*^2},\quad
 K_F=\frac{L_*N_*-M_*^2}{A_*^4}.
\tag{50.24}
\]
这与R37同一个材料密度一致。设 \(u=F/R\)，则
\[
 d=a|u_r|^2+2b\,u_r\cdot u_\theta+c|u_\theta|^2,
 \qquad u_i=\frac{F_i-u(u\cdot F_i)}R.
\tag{50.25}
\]
由三个真实平移核及 \(|u|=1\) 得到此 \(d\)，不除以会在腰部消失的 \(u_z\)。

对 \(i=r,\theta\)，
\[
 C_r=F_{r\theta}\times F_r+F_\theta\times F_{rr},\quad
 C_\theta=F_{\theta\theta}\times F_r+F_\theta\times F_{r\theta},
\]
\[
 (\log\zeta)_i=\frac{C_i\cdot F}{h}
                -\frac{C\cdot C_i}{A_*^2}
                -\frac{F\cdot F_i}{R^2}.
\tag{50.26}
\]
因 \(C\cdot F_i=0\)，(50.26)没有遗漏 \(h_i\) 的项。
当 \(\chi=1\) 覆盖整个负组件且目标曲率 \(K_0(r)<0\)，
\[
 \widehat c=\frac{b^2}a+\frac{K_0}{\zeta^4a},\quad
 \omega=\frac{K_F-K_0}{\zeta^4a},\quad
 \mu=\frac{\sqrt{-K_0}}{\zeta^2},
\]
\[
 \boxed{\quad
 f_r=\frac{K_0'}{2K_0}-2(\log\zeta)_r,
 \qquad f_\theta=-2(\log\zeta)_\theta.\quad}
\tag{50.27}
\]
所以(50.21)点值只额外需要 \(K_0,K_0'\)。对R33实际目标
\(g_0=E(r)dr^2+a_0(r)^2d\theta^2\)，
\[
 E=\langle|F_r|^2\rangle_\theta,\quad
 E'=2\langle F_r\cdot F_{rr}\rangle_\theta,\quad
 E''=2\langle|F_{rr}|^2+F_r\cdot F_{rrr}\rangle_\theta,
\]
\[
 C_0=a_0'E'-2a_0''E,\qquad
 C_0'=a_0'E''-a_0''E'-2a_0'''E,
\]
\[
 \boxed{\quad K_0=\frac{C_0}{2a_0E^2},\qquad
 K_0'=\frac{C_0'}{2a_0E^2}
                         -K_0\left(\frac{a_0'}{a_0}+\frac{2E'}E\right).
 \quad}\tag{50.28}
\]
这里的角平均针对真实无限原函数；有限DFT版本还须支付角尾、alias和舍入。
半径三阶导数若不是输入参数直接给出，也可由总阶不超过三的实际几何jet重建。
记 \(\lambda=|F_\theta|\)、\(T=F_\theta/\lambda\)、
\(\Pi=I-TT^t\)、\(h=F_{r\theta}\)，从角积分分部得
\[
 a_0''=\left\langle\frac{|\Pi h|^2}{\lambda}
                                    -T_\theta\cdot F_{rr}\right\rangle,
\]
再对真实径向求导并对含 \(F_{rr\theta}\) 的项作角积分分部，得到
\[
 a_0'''=\left\langle
 -3\frac{\lambda_r|\Pi h|^2}{\lambda^2}
 -3(T_r)_\theta\cdot F_{rr}-T_\theta\cdot F_{rrr}
 \right\rangle.
\tag{50.28a}
\]
这里 \((T_r)_\theta\) 至多使用三jet；没有偷偷要求 \(F_{rrr\theta}\)。
因此所有严格区点值至多使用实际 \(F\) 的三jet。若选择R46的
\(\ell_0=\partial_\theta\log(F_z/r)-\partial_\theta\log R\)，
还须先证明其奇性、\(F_z/r>0\) 及腰部光滑延拓；除以一个很小的浮点 \(F_z\)
并不支付该门。

## 6. 四重角尺度及反射计算

(50.2)的角周期不能漏算。对本题四重商圈，\(\ell=\pi/2\)，频率为
\(4j\)，所以
\[
 \langle\beta\rangle=\frac14\operatorname{FP}
                \int_{x_-}^{x_+}\langle J\rangle_\theta\,dx.
\tag{50.29}
\]
若**实际对象**有严格径向反射且两个根为 \(\pm t\)，同一密度为偶函数时才可写
\[
 \langle\beta\rangle=\frac12\operatorname{FP}
                   \int_0^t\langle J\rangle_\theta\,dr.
\tag{50.30}
\]
二进制knots的近对称不授予这一步。可先显式定义对称化的相位、半径和
准确坡度积分，并为与旧候选的差付界，再对那个对象使用(50.30)。

径向PT模型 \(P=\partial_r^2-V\partial_\theta^2\) 的(50.3)为
\(-V'^2/(16V^{5/2})\)，正好是R46(9.17)去掉有限部为零的总导数后的一项。
其全径向有限部为 \(\pi/(4\nu_0)\)，(50.29)得到
\(\beta=\pi/(16\nu_0)\)，与R34在 \(n=4j\) 的准确端口相位一致。
这个校准检查符号和频率因子，不能代替当前实际候选的有限部证书。

## 7. 继续验证的具体界线

一个完整数值证书应冻结同一个实际对象、角周期、\(\ell_0,\chi\)，然后分别支付：
严格区(50.21)的有向区间积分；每个root的(50.10)及(50.14)；两者的同一截面接线；
无限角原函数与计算表达之间的全部尾/alias/舍入。只把浮点发散积分拟合到常数，
或改变cut后数字接近，均不等于这样的证书。

主返回参数和真实共轭仍由R31/R48的实际输入门支付；完整相位区间再送入R34，
并与R43/R45–47/R49的强余项、全部源、有限低块和真帽接口合并。主目标仍未完成。
