# R56：实际特征分母的复角管与保真实Jacobian的流域

2026-11-12，visible-exact-astra-f6a2。

**状态：已证明的实际连续复角分母及中间ODE域结论。**
本篇把明确无限R33图的连续实 \(N<0\) 门升级为整个实核心上的复角无零点门。
复角管只涉及角变量，不把径向样条当作全局解析函数。主特征速度准确消去
支撑函数与面积平方根，所以此处不需额外选择复面积分支。另给保留真实实流
Jacobian的复流域估计，供随后实际返回验证使用。

这不是已验证的返回图或共轭。实际ODE积分误差、全核心目标曲率符号、
真实实流/参数jets和统一共轭误差仍须分别供应。

## 1. 主特征速度只剩一个角向分母

对同一个R33无限图置
\[
 X=F_r,\quad F_\theta=aT,\quad T\cdot T=1,\quad
 \mathscr C=aT\times X,\quad G=\mathscr C\cdot\mathscr C,
\]
\[
 n=\mathscr C\cdot F_{\theta\theta}
       =a^2(T\times X)\cdot T_\theta,\qquad
 m=\mathscr C\cdot F_{r\theta}
       =a^2(T\times X)\cdot T_r.
\tag{56.1}
\]
实点上 \(G=A^2,n=AN,m=AM\)，其中 \(A>0\) 是面积元。
复角点的点积均为**双线性解析延拓**，不用Hermitian模平方定义 \(G\)。

R37同一个修正算子在 \(K_0<0,N<0\) 区域的两支速度准确为
\[
 \boxed{\quad v_\sigma(r,\theta)
  =-\frac{m}{n}-\sigma\sqrt{-K_0(r)}\,\frac{G}{n},
  \qquad \sigma=\pm1.\quad}
\tag{56.2}
\]
把 \(M=m/A,N=n/A,\sqrt G=A\) 代入
\(-M/N+\sigma\sqrt{-K_0G}/|N|\)，并用 \(|N|=-n/A\)，即得此式。
所以角向只需 \(n\ne0\)。\(\sqrt{-K_0}\) 是同一真实负组件上的径向实函数，
在真实简单根取连续零值；没有取 \(\sqrt{G(r,z)}\) 或除以 \(\zeta\)。
不能据此删掉完整Darboux方程的零阶项；本节仅处理主返回。

令 \(n_*=X\cdot(T\times T_\theta)\)、\(m_*=X\cdot(T\times T_r)\)、
\(g_*=X\cdot X-(T\cdot X)^2\)，则
\(n=-a^2n_*,m=-a^2m_*,G=a^2g_*\)，故还准确有
\[
 v_\sigma=(-m_*+\sigma\sqrt{-K_0}\,g_*)/n_*.
\tag{56.3}
\]
这些式子对双线性复延拓仍准确，未将实际 \(G\) 换成目标度量行列式。

## 2. 实函数的二阶实部门

设 \(n(r,z)\) 对角变量解析，在实轴取实值。若一个闭径向单元 \(I\) 已证
\(n(r,\theta)\le-\eta_I<0\)，且在 \(|\operatorname{Im}z|\le s\) 有
\(\|\partial_\theta^2n\|\le B_{2,I}(s)\)，则
\[
 \boxed{\quad
 \operatorname{Re}n(r,\theta+iy)
 \le-\eta_I+\tfrac12s^2 B_{2,I}(s).\quad}
\tag{56.4}
\]
证明是准确Taylor式
\[
 n(\theta+iy)=n(\theta)+iy\,n_\theta(\theta)
       -y^2\int_0^1(1-t)n_{\theta\theta}(\theta+ity)\,dt.
\]
因为实轴上的 \(n_\theta\) 为实数，一阶项实部准确为零。因此若
\(d_I=\eta_I-\tfrac12s^2B_{2,I}(s)>0\)，整个复角管有
\[
 |n|\ge-\operatorname{Re}n\ge d_I>0.
\tag{56.5}
\]
这里的实输入是已经认证的整个实圆上界，不是有限节点的最小值。

## 3. 真实有限相位的复管导数界

当前相位为
\[
 \beta=\sum_{k=1}^{24}b_k(r)\sin(4k\theta),\quad
 \gamma=\sum_{k=1}^{24}g_k(r)\sin(4k\theta),\quad
 T=(\cos\gamma\cos\phi,\cos\gamma\sin\phi,\sin\gamma),
 \quad \phi=\theta+\pi/2+\beta.
\]
冻结binary控制点按实数解释；先取物理加权相位的准确偶奇部分。
在闭径向单元使用已有有向de Boor和完整多项式Taylor包络。
以 \(|b_k^{(a)}|_I,|g_k^{(a)}|_I\) 记这些实上界。定义
\[
 \begin{aligned}
 I_s&=s+\sum_k(|b_k|_I+|g_k|_I)\sinh(4ks),& E_s&=e^{I_s},\\
 P_1&=1+\sum_k4k(|b_k|_I+|g_k|_I)\cosh(4ks),\\
 P_j&=\sum_k(4k)^j(|b_k|_I+|g_k|_I)\cosh(4ks),&&j=2,3,\\
 R_j&=\sum_k(4k)^j(|b_k'|_I+|g_k'|_I)\cosh(4ks),&&j=0,1.
 \end{aligned}\tag{56.6}
\]
实系数给 \(|\operatorname{Im}\beta|\le\sum|b_k|\sinh(4ks)\)，不用支付整个
实相位绝对值。复正交旋转 \(R_z(\phi)R_y(-\gamma)\) 的Hermitian算子norm
至多 \(e^{|\operatorname{Im}\phi|+|\operatorname{Im}\gamma|}\)：实旋转是酉的，
纯虚旋转的两个非平凡奇异值为 \(e^{\pm y}\)。因此有正Bell包络

|向量|整个复管的Hermitian范数上界|
|---|---|
|\(T\)|\(T_0=E_s\)|
|\(T_\theta\)|\(T_1=E_sP_1\)|
|\(T_{\theta\theta}\)|\(T_2=E_s(P_2+P_1^2)\)|
|\(T_{\theta\theta\theta}\)|\(T_3=E_s(P_3+3P_1P_2+P_1^3)\)|
|\(T_r\)|\(T_r^*=E_sR_0\)|
|\(T_{r\theta}\)|\(T_{r1}^*=E_s(R_1+R_0P_1)\)|

这些界由微分两个旋转矩阵并支付所有Leibniz项得到，不要求其生成元交换。

设同一实证书已经给整个实圆的 \(\|X\|\le X_0\)。真实无限原函数恒等式
\(X_\theta=a'T+aT_r\) 沿竖线积分，给出
\[
 X_s=X_0+s(|a'|_IT_0+a_+T_r^*)\ge
       \sup_{I\times\{|\operatorname{Im}z|\le s\}}\|X\|.
\tag{56.7}
\]
这是无限原函数本身的解析估计，不用有限DFT替换它。
实证书中的无限尾/alias和舍入已经包含在 \(X_0\) 中。

## 4. 二阶分母和主速度的全部费用

由(56.1)和 \(X_\theta=a'T+aT_r\)，准确有
\[
 \begin{aligned}
 n_{\theta\theta}={}&
 a^3(T\times T_{r\theta})\cdot T_\theta
 +2a^3(T\times T_r)\cdot T_{\theta\theta}\\
 &+a^2(T_\theta\times X)\cdot T_{\theta\theta}
 +a^2(T\times X)\cdot T_{\theta\theta\theta}.
 \end{aligned}\tag{56.8}
\]
所有 \(a'\) 项因交替积消失。因此明确可取
\[
 \boxed{\quad B_{2,I}(s)=a_+^2\left[
 a_+T_0T_{r1}^*T_1+2a_+T_0T_r^*T_2
              +X_s(T_1T_2+T_0T_3)\right].\quad}
\tag{56.9}
\]
复向量仍满足 \(|u\cdot(v\times w)|\le\|u\|\|v\|\|w\|\)，故本式控制的
是双线性解析 \(n\)，不是另一个实模平方函数。

若(56.5)给 \(d_I>0\)，还可定义
\[
 \begin{aligned}
 M_0&=a_+^2T_0X_sT_r^*,&
 M_1&=a_+^2X_s(T_1T_r^*+T_0T_{r1}^*),\\
 G_0&=a_+^2T_0^2X_s^2,&
 G_1&=2a_+^2T_0X_s(T_1X_s+a_+T_0T_r^*),\\
 N_1&=a_+^2(a_+T_0T_r^*T_1+T_0X_sT_2).
 \end{aligned}\tag{56.10}
\]
它们分别控制 \(|m|,|m_\theta|,|G|,|G_\theta|,|n_\theta|\)。
例如 \(m_\theta=a^2[(T_\theta\times X)\cdot T_r+
(T\times X)\cdot T_{r\theta}]\)，中间的
\((T\times X_\theta)\cdot T_r\) 准确为零。记 \(d=-m/n,w=-G/n\)，则
\[
 |d|\le M_0/d_I,\quad |w|\le G_0/d_I,
\]
\[
 |d_\theta|\le M_1/d_I+M_0N_1/d_I^2,\qquad
 |w_\theta|\le G_1/d_I+G_0N_1/d_I^2.
\tag{56.11}
\]
同一 \(v_\sigma=d+\sigma\sqrt{-K_0}\,w\) 的界按真实径向 \(\sqrt{-K_0}\)
组合。更高有限角导可在严格较小管中用Cauchy，例如内宽 \(s/2\) 上
\[
 |v_{\theta\theta}|\le8s^{-2}
              (M_0/d_I+\sqrt{-K_0}\,G_0/d_I).
\tag{56.12}
\]
常数虽粗，却是明确的；不把粗界的指数当作已验证返回域的好常数。

## 5. 已完成的实际全核心证书

脚本 scripts/fourfold_phase_characteristic_strip.py 逐个读取同一实证书
的闭径向单元和 \(n,X\) 界，再算(56.6)–(56.11)。基本加乘除后均向外
移一浮点数；sinh/cosh/exp使用准确有理Taylor余项及有向平方的
interval_exp，不用未定误差的libm指数。正和/正积向上，正下界向下。

原sym step02输入SHA为
bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532；
实N/支撑包SHA为
36a83e821e7ca2572fdc95378d688505c1fee788b633e7f0195ff61ecf35eeac。
同一无限图的整个 \(|r|\le1/4\)、174闭单元与全部复角得到：

|物理角宽 \(s\)|已含全部区间费用的结论|
|---|---|
|\(1/512\)|\(\operatorname{Re}n<-.34999\)|
|\(1/256\)|\(\operatorname{Re}n<-.17256\)|

简洁十进制界对保存端点作准确Fraction比较即可复核。
若返回计算用 \(x=4\theta\)，宽度分别为 \(1/128,1/64\)；
**这是系数域宽，不是已经完成的返回映射域宽。**
第二包另有 \(|d|<8.218633,|w|<8.838421\)，逐单元完整费用在JSON中。
它们不替代真实射线的导数。

数据为同目录下的 type_fixed_step02_complex_angle_1over512.json、
type_fixed_step02_complex_angle_1over256.json；包含输入/源/依赖hash。
从仓库根重放：

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    python topics/visible-flex-exact-nearby/scripts/fourfold_phase_characteristic_strip.py \
      --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz \
      --real-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_core_interval.json \
      --width .00390625 --out /tmp/visible-step02-complex-angle.json

R55/R57对象必须独立读取自己的实证书和系数重算，不迁移上述数值。
参数适配源 scripts/fourfold_phase_parameter_characteristic_strip.py
准确重建R57独立控制点盒；不把rounded predictor默认为准确仿射参数点。
只有另付准确dyadic盒包含的候选才能继承整个盒的结论。

这两个新对象也已各自完成物理角宽 \(1/256\) 的全部592闭单元重算：

|明确对象，整个 \(|r|\le\operatorname{binary64}(.24)\)|全复角管结论|
|---|---|
|R55固定输入，SHA 0d17500a…ca59b|\(\operatorname{Re}n<-.19294\)|
|R57独立控制点盒，方向SHA 8db5d57d…d89ab|\(\operatorname{Re}n<-.19191\)|

这里截短SHA只为表格阅读；报告保存完整标识。第二行实证书SHA为
b52537b755e7b5475dc945a5781c0d57a93e71ccdf39ec90891c236fcae2438a。
其准确参数半径是binary64(.01)，但已证范围是更大的独立控制点盒，
所以在盒内逐坐标变化也覆盖。不存在把原图界跨对象迁移的步骤。
数据为 type_fixed_step02_d5_jet_complex_angle_1over256.json 与
type_fixed_step02_d5_parameter_complex_angle_1over256.json，全部单元通过。
R57已严格包含的rounded Newton128图因此继承第二行复分母门；
R57只对准确仿射子族支付的共同root仍不能据此授予每个盒内图。

## 6. 保留真实实流Jacobian的复ODE域

以下全流定理要求输入来自同一实际速度。允许径向只连续，角变量在
\(|\operatorname{Im}z|<s_*\) 解析。一条正向或反向腿的积分参数记
\(u\in[0,L]\)，方程 \(z'=v(u,z)\)。\(v\) 在实轴实值且周期，故实流全时存在。
记实初值 \(x\) 的真实流为 \(\gamma(u;x)\)，
\(J(u;x)=\partial_x\gamma(u;x)>0,J(0;x)=1\)。
供给 \(|v_{\theta\theta}(u,z)|\le B_2(u)\) 及对全部实 \(x\) 的界
\[
 J(u;x)\le M,\qquad
 \tfrac12\int_0^L B_2(u)J(u;x)\,du\le\Lambda.
\tag{56.13}
\]
若初始宽 \(s>0\) 满足
\[
 s\Lambda<1,\qquad \frac{Ms}{1-s\Lambda}<s_*,
\tag{56.14}
\]
则整个初始角管 \(|\operatorname{Im}z_0|<s\) 的真实流存在、解析，且
\[
 \begin{aligned}
 |z(u;x+iy)-\gamma(u;x)|
   &\le\frac{J(u;x)|y|}{1-|y|\Lambda_u(x)},\\
 |\partial_{z_0}z(u;z_0)|
   &\le\frac{J(u;x)}{(1-|y|\Lambda_u(x))^2},\\
 |\partial_{z_0}^2z(u;z_0)|
   &\le\frac{2J(u;x)\Lambda_u(x)}
                  {(1-|y|\Lambda_u(x))^3},
 \end{aligned}
\tag{56.15}
\]
其中 \(\Lambda_u(x)=\tfrac12\int_0^u B_2(t)J(t;x)dt\)。
简单充分门是 \(s\Lambda\le1/2,2Ms<s_*\)。

证明：写 \(z-\gamma=Jb\)。准确 \(J'=v_\theta(u,\gamma)J\)，故
\[
 b'=J^{-1}[v(u,\gamma+Jb)-v(u,\gamma)-v_\theta(u,\gamma)Jb],
 \qquad |b'|\le\tfrac12 B_2J|b|^2.
\]
Riccati积分比较给 \(|b|\le|y|/(1-|y|\Lambda_u)\)。
(56.14)保证bootstrap不离开已付角管，因而覆盖全时。变分式给
\[
 |\partial_{z_0}z|\le
 J\exp\int_0^u B_2(t)|z(t)-\gamma(t)|dt
 \le J(1-|y|\Lambda_u)^{-2}.
\]
二阶变分的准确式
\[
 \partial_{z_0}^2z(u)=\partial_{z_0}z(u)
       \int_0^u v_{\theta\theta}(t,z(t))\partial_{z_0}z(t)dt
\]
及
\(\int_0^u B_2J(1-|y|\Lambda_t)^{-2}dt
=2\Lambda_u/(1-|y|\Lambda_u)\) 给第三界。\(y=0\) 按连续极限理解。

这不需要实 \(J\) 的正下界，但(56.13)必须覆盖全部实初值。
有限射线样本不能供应该输入。两腿返回需各自过(56.14)，再核第一腿完整
复像落入第二腿初始域，才能给组合返回的域和导数。

## 7. 移动根和真实参数导数

若明确反射对象在整个实参数区间内只有根 \(\pm t(p)\)，负区为
\(|r|<t(p)\)，且共同局部多项式span付出根附近参数二阶所需jets，可用
\[
 r=t(p)\sin u,\quad -\pi/2\le u\le\pi/2,\qquad
 -K_0(r,p)=(t(p)^2-r^2)\kappa_2(r,p),\quad\kappa_2>0.
\tag{56.16}
\]
端点商用真实根导数延拓，其所需参数导数由共同root span的高jet供给。
同一ODE准确化为
\[
 \frac{d\theta}{du}
 =t(p)\cos u\,d(t(p)\sin u,\theta,p)
 +\sigma t(p)^2\cos^2u\sqrt{\kappa_2(t(p)\sin u,p)}
                  \,w(t(p)\sin u,\theta,p).
\tag{56.17}
\]
积分端点现在固定，不能对移动根直接使用固定积分限的参数公式。
严格区只需所用的有限径向光滑；各真实knot区间以已付C²正则接合，
不要求Gaussian全局径向解析化。

将(56.17)右端记 \(f\)，真实参数变分准确为
\[
 Y_p'=f_\theta Y_p+f_p,\qquad
 Y_{pp}'=f_\theta Y_{pp}+f_{\theta\theta}Y_p^2
                   +2f_{\theta p}Y_p+f_{pp}.
\tag{56.18}
\]
初值不随参数变时两初值均为零，所有混合导数和源都保留。
当前Schur软列或有限差分不能免费授予R31的 \(P,Q,T\)。

原图及R55/R57各自的根、N和参数门须按准确输入/范围接合。
全核心K0符号、统一ODE误差和(56.13)仍是具体待交付。
β完整零阶相位、全反馈逆、真帽与最终闭等距族不由本篇单独完成。
