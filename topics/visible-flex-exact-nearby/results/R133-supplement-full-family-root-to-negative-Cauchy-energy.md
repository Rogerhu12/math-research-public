# R133：全参数根部到负区切口的完整普通源 Cauchy 估计

2026-11-14，visible-exact-astra-0df9 / root；phase_inverse 提供正则权的初始构造。

**解析结论。** 本文直接沿负区方向证明完整 moving Jacobi 系统的 Cauchy
估计，不反用只向根传播的旧能量。数值前提由独立公开 Actions consumer
消费原两个已完成 native；没有把未执行预算先标为通过。
全部角频率、独立 even mean 和普通源均保留。

## 1. 同一完整方程和所需前提

使用 [完整 moving scalarization](R133-supplement-complete-moving-root-scalarization.md)
(N.1)--(N.3) 的原物理角、归一圆测度、完整状态 $h=(h_1,h_2)$ 与普通源 $g$。
$\partial=\partial_\phi$、$\Pi f=\langle f\rangle$、
$I=\partial^{-1}(1-\Pi)$，物理频率 $k_j=4j$。
背景是修复定义440866a3…的同一显式族，固定 intrinsic $\eta_0$，
实参数 $|\delta|\le10^{-8}$；它不被当成真正非线性分支。

置 $\rho=r_*-r$、$q^2=-K$、$R=9/10^6$。本篇使用下列整域界：
$$
 q^2(0)=0,\quad (q^2)_\rho>59,\quad
 0\le q^2<61/10^5,\quad |\eta|\le a_*=63/50,
 \quad \gamma<28/25,\quad |b|<211/1000.                 \tag{C.1}
$$
原两根内在参数 bump 在此片准确零，因此同一原 root germ 可用。
真实 whole-family $u,v$ 在角方向至多96阶，所有二次局部系数和
$d=-bI(u^2+Kv^2)$ 至多192阶；最大物理 lag 是768。

记 $U_l,V_l$ 为完整 $\mathcal A_{1/1024}$ 导数上界，亦控制
ordinary $\mathcal A_0$。消费者要求
$$
 (U_0,U_1,U_2)<(.630,2.615,11.365),\quad
 (V_0,V_1,V_2)<(1.791,2.803,12.378).                  \tag{C.2}
$$
所有这些均由已完成的完整193方向、修复和 joint germ 预算消费，
不重建 response 或原 scalar germ。

## 2. 在根处正则、向负区耗散的 Fourier 权

令 $\Lambda_j=\sqrt{1+16j^2}$、$x=\rho\Lambda_j^{2/3}$，定义
$$
 w_j^2=q^2+\Lambda_j^{-2/3}e^{-x},\qquad
 \theta_j=\exp[-a_*(1-e^{-x})],\qquad
 Z=Mh,\quad M=\operatorname{diag}(\theta/w,\theta).     \tag{C.3}
$$
这些是完整正的 Fourier multipliers，非角向点乘权。准确地
$$
 w_\rho^2=(q^2)_\rho-e^{-x}>58,\qquad
 w\ge\Lambda^{-1/3},\quad w\ge q,\quad
 w\le W:=\sqrt{1+\sup q^2}<1.001,\quad\theta^{-1}<4 .
                                                               \tag{C.4}
$$
第二式由 $q^2\Lambda^{2/3}\ge59x$ 与 $59x+e^{-x}\ge1$ 得到。
根处 $w=\Lambda^{-1/3}$、$\theta=1$，所以
$$
 \|Z(0)\|^2=\|h_1(0)\|_{H^{1/3}}^2+\|h_2(0)\|_{L^2}^2 .
                                                               \tag{C.5}
$$
$h_2$ 的真正 mean 在此式中，未被移除。

原 $\rho$ 方向的主部是
$-\eta\left(\begin{smallmatrix}0&q^2\\1&0\end{smallmatrix}\right)\partial$。
在 $Z$ 上，它准确为
$$
 -\eta w\begin{pmatrix}0&1\\1&0\end{pmatrix}\partial
 +\begin{pmatrix}0&\eta\Lambda^{-2/3}e^{-x}w^{-1}\partial\\0&0\end{pmatrix}.
                                                               \tag{C.6}
$$
第一项 skew-adjoint。第二项逐频率的 norm 至多
$a_*\Lambda^{2/3}e^{-x}$，而
$\theta_\rho/\theta=-a_*\Lambda^{2/3}e^{-x}$ 在两行同时出现。
两者的实能量贡献之和非正；另有第一行 $-w_\rho/w\le0$。
因此无需把 $\sup_j\Lambda_j^{2/3}e^{-\rho\Lambda_j^{2/3}}$
对 $\rho$ 积分，根附近不存在这个人为发散。

## 3. 完整有限带乘子和 transport 的费用

固定 $\rho$，直接微分给
$$
 -\tfrac13\le\partial_{\log\Lambda}\log\theta\le0,\quad
 0\le-\partial_{\log\Lambda}\log w\le\tfrac13.
$$
第一式用 $(2a_*/3)xe^{-x}\le2a_*/(3e)<1/3$；
第二式用 $(1+x)e^{-x}\le59x+e^{-x}$。于是两个 $M_\nu$ 均有
$$
 |\partial_{\log\Lambda}\log M_\nu|\le1/3.             \tag{C.7}
$$
这里不是把两个绝对值相加到2/3：两个导数的符号相反。

设物理输入频率 $k$、lag $\ell$。由
$|\Lambda(k+\ell)-\Lambda(k)|\le|\ell|$，分别比较两个大小顺序，
$$
 |k|\left|{M_\nu(k+\ell)\over M_\nu(k)}-1\right|
 \le(1+|\ell|)^{1/3}|\ell|,\qquad
 {M_\nu(k+\ell)\over M_\nu(k)}\le(1+|\ell|)^{1/3}.      \tag{C.8}
$$
例如当 $\Lambda_{\rm out}<\Lambda_{\rm in}$，
$t=\Lambda_{\rm in}/\Lambda_{\rm out}\ge1$，
$t^{1/3}-1\le t^{1/3}(1-t^{-1})$；另一顺序用凹性。
最大lag768给 $(1+|\ell|)^{1/3}<10$。
Young convolution 因而在完整 $L^2$ 上给
$$
 \|M_\nu a M_\nu^{-1}\|\le10\|a\|_{\mathcal A_0},\quad
 \|[M_\nu,d]M_\nu^{-1}\partial\|\le10\|d_\phi\|_{\mathcal A_0}.
                                                               \tag{C.9}
$$
原 $\pm d\partial$ 的实能量增长至多 $\|d_\phi\|_\infty/2$，
所以 transport 总增长至多
$$
 D_{\rm tr}={21\over2}|b|(U_0^2+q_{\max}^2V_0^2)<.945 .
                                                               \tag{C.10}
$$
全 $\delta$ 产品的band192已明确付费，未借M32 band64常数。

## 4. 局部反应、原 primitive 和真正 mean rank

原三个局部系数是
$$
 L_{11}=-b(1+3u^2+Kv^2),\quad
 L_{22}=b(1-u^2-3Kv^2),\quad \ell_0=-2buv .
$$
由 (C.1)--(C.2)，其完整角norm分别小于 $.5,.3,.5$。
对角块用 (C.9)，交叉块用 $q^2/w\le q<1/40$、
$\theta^{-1}<4$、$w<W$，得到安全的总增长
$$
 D_{\rm loc}\le10(.5+.3)+4[(1/40)(.5)+1.001(.5)]<11 .
                                                               \tag{C.11}
$$
不假设反应块与 Fourier 权可交换。

完整非局部项仍是
$-2b(u_\phi,v_\phi)^T I(uh_1+Kvh_2)$。
对任意角乘子 $a$，
$$
 \|a f\|_{H^{1/3}}\le
 (\|a\|_{\mathcal A_0}+\|a_\phi\|_{\mathcal A_0})\|f\|_{H^{1/3}},
 \qquad
 \|I\|_{L^2\to H^{1/3}}={17^{1/6}\over4}<.41 .
                                                               \tag{C.12}
$$
第一式由 $\Lambda(k+\ell)/\Lambda(k)\le1+|\ell|$ 逐项卷积证明；
第二式的最大值在物理频率4处。因 $M_1\le\Lambda^{1/3}$、
$M_2\le1$，完整 primitive 的增长界为
$$
 D_I\le8|b|(WU_0+q_{\max}^2V_0)
       [.41(U_1+U_2)+V_1/4]<7 .                     \tag{C.13}
$$
这保留原 $I$ 的次序及全部乘法，不把它换成新的径向切片积分。

原 mean rank 项为 $\gamma z(Kv_\phi,-u_\phi)$，
$z=\Pi h_2$。$|z|\le4\|Z_2\|$，故其完整费用为
$$
 D_{\rm mean}\le4\gamma[q_{\max}^2(V_1+V_2)+U_1]<12 .  \tag{C.14}
$$
这是真正独立even mean的反馈，既未设零，也未并入一个假物理transport mean。
原ordinary源的mean同样包含在下一节的完整source norm。

## 5. 真正向负区传播的结论

令 $F(\rho)=\|g(\rho)\|_{H^{1/3}\times H^{1/3}}$。
(C.3)--(C.4) 给 $\|Mg\|\le F$。完整方程的所有项已经逐项覆盖，
因此
$$
 {d\over d\rho}\|Z\|
 \le(D_{\rm loc}+D_{\rm tr}+D_I+D_{\rm mean})\|Z\|+F
 <31\|Z\|+F.                                         \tag{C.15}
$$
由 Gronwall 和径向 Cauchy--Schwarz，对整个 $0\le\rho\le R$，
$$
 \|Z(\rho)\|\le e^{31R}
 \left[\|Z(0)\|+\sqrt R\,\|g\|_{L^2_\rho H^{1/3}}\right].
$$
$\|M^{-1}\|\le4W$、$\sqrt R=.003$ 且
$4W e^{31R}<41/10$，给
$$
 \boxed{\quad
 \sup_{0\le\rho\le9/10^6}\|h(\rho)\|_{L^2\times L^2}
 <{41\over10}\left[
  (\|h_1(0)\|_{H^{1/3}}^2+\|h_2(0)\|_{L^2}^2)^{1/2}
          +.003\,\|g\|_{L^2_\rho(H^{1/3}\times H^{1/3})}\right].
 \quad}                                                    \tag{C.16}
$$
对零输入用非严格版本。每个子区间可把 $\sqrt R$ 换成其实际
$\sqrt\rho$，但本文不以此宣称任何未经支付的不同参数域。

先在 Fourier Galerkin 系统证明 (C.15)。投影与 $M,\partial,\Pi,I$ 交换，
故常数独立于截断，所有完整乘子费用保持。逐固定Fourier坐标的
实ODE紧性、弱下半连续和稠密逼近给完整频率能量解；唯一性由
(C.15) 对零源零初值直接给出。finite band只用于实际背景系数，
未知解与source没有截断。普通源不需额外径向导数。

本结论是 $s=0$ 输出与明确根Airy两行输入的正向Cauchy定理。
它可将positive/root匹配校正的真实根误差送到负区cut；
不能反过来当成另一方向同常数估计，也不提供高Sobolev窗、
实际根反射有限常数、无限返回逆或非线性PDE存在。后续strong窗
若通过解析列核重建，仍需把相应输入和余项权重完整送入此式。
