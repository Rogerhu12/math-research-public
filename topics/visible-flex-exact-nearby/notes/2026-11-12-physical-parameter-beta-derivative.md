# 物理坐标 beta 参数导数：有限部交换和解析 H 公式

## 1. 用途、假设与已完成范围

本篇证明一个便于实际验证的参数接口。设固定准确 affine 家族
\(F(r,\theta,\delta)\) 在一个闭实参数区间 \(\Delta\) 上满足：

1. 目标径向曲率 \(K(r,\delta)\) 在 \(0\le r<t(\delta)\) 严格负，
   在 \(t(\delta)\) 为统一简单根；固定 \(b\) 位于所有这些根的左侧。
2. \(b\) 到所有 \(t(\delta)\) 同属一个固定 scalar spline span。
   原点附近采用准确径向奇偶对称，使 \(F_z/r>0\) 和全部实际分母有统一门。
3. 物理 bulk 上各函数和参数一 jet 分段光滑，原有 spline knots
   与 \(\delta\) 无关，密度在其交界可积。根 collar 的相关 germ
   对 \(\rho=t(\delta)-r\) 和 \(\theta\) 在共同复域解析，
   且对实 \(\delta\) 连续可微。下文 Taylor 界均在整个 \(\Delta\) 上统一。
4. \(d,\omega,\ell,\zeta\) 使用同一 R37 实际算子口径；
   不把一个参数点的零阶系数保留到另一个参数点。

目标不是预先要求这些门在任意宽参数盒成立，而是在给定实际盒上逐项支付。
本篇完成恒等式、有限部微分和误差公式；
尚未给出当前实际家族的完整 \(B_\delta\) 数值。
当前 h=1e-8 根/collar 测试不被称为最终 KAM 参数盒。

本接口的优点是：为了将准确点的 \(\beta\) 扩展至距离约 \(10^{-5}\)
的参数盒，只需一个粗但真实的 \(|\beta'|\) 上界。
例如若能实际付 \(B_\delta\le1000\)，该距离仅增加 \(0.01\)
的相位预算；这里的 1000 是目标示例，不是已证实际常数。

## 2. 固定物理 r 的有限部微分严格交换

用 R50/R52 的归一化，在物理 \(n=4j\) 下

\[
\beta(\delta)=\frac12\operatorname{FP}
 \int_0^{t(\delta)}\langle J(r,\theta,\delta)\rangle_\theta\,dr.
\tag{2.1}
\]

写

\[
J(t(\delta)-\rho,\theta,\delta)
=\rho^{-5/2}G(\rho,\theta,\delta),
\]

其中 \(G\) 在 \(\rho=0\) 解析。所有根端点展开只有半整数幂。
因此

\[
\boxed{
2\beta'(\delta)=\operatorname{FP}
\int_0^{t(\delta)}
\langle \partial_\delta J(r,\theta,\delta)|_r\rangle_\theta\,dr.}
\tag{2.2}
\]

证明可直接从截断积分开始。对
\(I_\varepsilon(\delta)=
\int_0^{t(\delta)-\varepsilon}\langle J\rangle_\theta dr\)
求导得到

\[
I_\varepsilon'
=\int_0^{t-\varepsilon}\langle J_\delta|_r\rangle_\theta dr
+t'\langle J(t-\varepsilon,\cdot,\delta)\rangle_\theta.
\]

第二项的展开为
\(t'\sum_{n\ge0}\langle G_n\rangle
\varepsilon^{n-5/2}\)，其中没有常数项。
统一解析性允许对消去有限多个发散幂后的余项求导；
取常数项即给出 (2.2)。固定物理 knots 不产生移动界面项。

这也与已有
[参数微分接口](2026-11-12-parameter-beta-differentiation-interface.md)
完全一致。记 \(H_0(\rho,\delta)=\langle J(t-\rho,\cdot,\delta)\rangle\)，则

\[
J_\delta|_r= (H_0)_\delta|_\rho+t'(H_0)_\rho.
\]

在 collar 上对第二项积分，只有 \(t'H_0(\eta)\) 的有限端点贡献；
\(\rho=0\) 仍无常数项。于是得到旧接口的
\(t'J(b)+\operatorname{FP}\int_0^\eta (H_0)_\delta|_\rho\,d\rho\)。
式 (2.2) 没有把真实移动根冻结，也没有将 \(t'\) 置零。

## 3. 物理参数导数的解析化

以下下标 \(\delta\) 始终表示固定物理 \(r,\theta\) 的参数导数，
之后再将所得函数评价在 \(r=t(\delta)-\rho\)。
把已消去 \(\zeta^2\) 公因子的 R37 密度写为

\[
J=\frac{D-\frac14(af^2+2bfg+\widehat c\,g^2)}
        {\sqrt{-K}},
\quad
D=d+\omega(\ell^2+\ell g),
\tag{3.1}
\]
\[
f=\frac{K_r}{2K}-2(\log\zeta)_r,\qquad
g=-2(\log\zeta)_\theta,\qquad
\widehat c=\frac{b^2+K}{a}.
\]

令

\[
q(\rho,\theta,\delta)=-\frac{K(t-\rho,\delta)}{\rho},
\quad \kappa=\sqrt q,\quad
k=K_\delta|_r,\quad k_r=(K_r)_\delta|_r.
\]

目标 \(K\) 径向，所以 \(q,k\) 本身无角变量；将其写在同一域上
只是为了统一公式。真根可去因子使 \(q\) 在 \(\rho=0\) 解析且
\(q(0,\delta)=K_r(t,\delta)>0\)。定义

\[
P=\rho f
=-\frac12-\rho\left(\frac{q_\rho}{2q}
                         +2(\log\zeta)_r\right),
\tag{3.2}
\]
\[
R=\rho^2 f_\delta
=-\frac{\rho k_r}{2q}
 -\frac{K_r k}{2q^2}
 -2\rho^2(\log\zeta)_{r\delta},
\tag{3.3}
\]
\[
N=\rho^2D-\frac14
 \left(aP^2+2\rho bPg+\rho^2\widehat c\,g^2\right).
\tag{3.4}
\]

式 (3.3) 由
\(f_\delta=k_r/(2K)-K_rk/(2K^2)-2(\log\zeta)_{r\delta}\)
和 \(K=-\rho q\) 得到。这里没有对 \(q\) 作固定根的伪参数微分。

于是

\[
\boxed{J_\delta|_r=\rho^{-7/2}H}
\tag{3.5}
\]

且整个解析分子为

\[
\begin{aligned}
H=\kappa^{-1}\bigg[
&\rho^3D_\delta
-\frac{\rho a_\delta P^2}{4}
-\frac{aPR}{2}
-\frac{\rho^2b_\delta Pg}{2}
-\frac{\rho bRg}{2}\\
&-\frac{\rho^2bP g_\delta}{2}
-\frac{\rho^3\widehat c_\delta g^2}{4}
-\frac{\rho^3\widehat c\,g g_\delta}{2}
+\frac{Nk}{2q}
\bigg].
\end{aligned}
\tag{3.6}
\]

这里

\[
D_\delta=d_\delta
 +\omega_\delta(\ell^2+\ell g)
 +\omega(2\ell\ell_\delta+\ell_\delta g+\ell g_\delta).
\tag{3.7}
\]

证明只需对 (3.1) 作准确乘积/商微分，乘 \(\rho^3\)，并代入
\(f=P/\rho\)、\(f_\delta=R/\rho^2\)。
最后一项的正号来自
\(-(\sqrt{-K})_\delta/\sqrt{-K}=-k/(2K)=k/(2\rho q)\)。
所有 (3.6) 中的系数在根处解析；因此 \(H\) 确为解析函数，
不是用逐列或逐点的渐近式替代全角对象。

一个独立的最低阶核查是

\[
H(0)=-\frac{5a(0)k(0)}{32q(0)^{3/2}}
      =\frac{5a(0)t'}{32\sqrt{q(0)}}.
\tag{3.8}
\]

后一等式用 \(k(0)+t'q(0)=0\)。
原 \(G_0=-a/(16\sqrt q)\)，所以
\(H_0=-(5/2)t'G_0\)，与直接微分
\(G_0(t-r)^{-5/2}\) 的首奇异项相符。

## 4. 只需要固定物理参数一 jet

公式 (3.6) 使用 \(F,F_r,F_{rr},F_{rrr}\) 及它们的参数一 jet，
角导数和实际分母，另有目标 \(E,E_r,E_{rr}\) 及参数一 jet。
没有为了计算 \(t'\) 再引入一次径向微分；
\(K_r\) 本就由几何三 jet 给出。

对准确 affine 家族，物理 scalar 的参数导数可以直接在同一 spline
多项式上构造，而非差分两份已四舍五入的快照。
特别是 raw phase 的方向先乘固定 base 的三次/二次幂，再作准确奇偶对称；
mean 半径和准确 slope 原函数沿同一方向微分。

若 \(\beta_{\rm ang},\gamma_{\rm ang}\) 表示 R33 角相位，
物理切向在随物理角 \(\theta\) 旋转的柱坐标基中的分量为

\[
T=(-\cos\gamma_{\rm ang}\sin\beta_{\rm ang},
    \cos\gamma_{\rm ang}\cos\beta_{\rm ang},
    \sin\gamma_{\rm ang})
\]

这里 \(\beta_{\rm ang}\) 不含背景角 \(\theta\)。下述分量范数及
\(T_\delta\) 的界始终在这一旋转基中取，故不另乘
\(e^{|\operatorname{Im}\theta|}\)；若切回固定 Cartesian 分量，必须另付此因子。
物理 \(\theta\) 导数则仍包含该基的旋转矩阵项，不能只微分相位函数。

参数导数由

\[
T_\delta=T_{\beta_{\rm ang}}(\beta_{\rm ang})_\delta
         +T_{\gamma_{\rm ang}}(\gamma_{\rm ang})_\delta
\]

准确得到。若共同复域上
\(|\beta_{\rm ang}|_{\rm imag}\le B\)、
\(|\gamma_{\rm ang}|_{\rm imag}\le G\)，
方向大小界为 \(B_\delta,G_\delta\)，则每个切向分量可以使用
\((B_\delta+G_\delta)e^{B+G}\) 的安全界。
因此参数导数的无限 primitive 尾仍可由同一 Fourier alias 几何和计算，
径向导数再由同一 Cauchy 圆盘支付。
不能只对有限 DFT 求导而漏掉无限尾的参数一 jet。

## 5. 全角 Taylor 有限部和显式误差

假设对整个参数盒和共同复域

\[
|\rho|<R,\quad |\operatorname{Im}(4\theta)|<\sigma
\]

已证 \(|H|\le M_H\)。记 \(\eta(\delta)=t(\delta)-b\)，
\(0<\eta_-\le\eta\le\eta_+<R\)。
将角平均展开为 \(\langle H\rangle=\sum_{n\ge0}h_n\rho^n\)，则

\[
I_{\delta,\rm collar}
=\operatorname{FP}\int_0^\eta
 \rho^{-7/2}\langle H(\rho,\cdot,\delta)\rangle\,d\rho
=\sum_{n\ge0}
\frac{h_n\eta^{\,n-5/2}}{n-5/2}.
\tag{5.1}
\]

取 \(N\ge2\) 并保留 \(0\ldots N\) 项，径向余项严格有

\[
E_{\rm rad}\le
\frac{M_H\,\eta_+^{\,N-3/2}}
 {(N-3/2)R^{N+1}(1-\eta_+/R)}.
\tag{5.2}
\]

证明用 Cauchy 系数界 \(|h_n|\le M_H/R^n\)，从 \(n=N+1\)
起积分绝对值；其积分幂次为 \(n-5/2\)。
特别地，这里不能误用原 \(J\) 的 \(-5/2\) 密度尾指数。

若角方向使用归一角 \(x=4\theta\) 的 \(A\) 点 trapezoid，完整角平均误差为

\[
E_A=\frac{2M_He^{-\sigma A}}{1-e^{-\sigma A}}.
\]

对其 \(\rho\) Taylor 系数逐项用 Cauchy，得到整个有限部的角误差

\[
E_{\rm ang}\le
\frac{2E_A\,\eta_-^{-5/2}}{1-\eta_+/R}.
\tag{5.3}
\]

原因是全部整数 \(n\ge0\) 满足 \(|n-5/2|\ge1/2\)。
因此只需系数球、真根 \(\eta\) 的区间以及 (5.2)、(5.3)，
就能将有限部参数导数夹在严格区间中。

## 6. Bulk 可以只付绝对上界

为了得到 \(|\beta'|\) 的粗但有效的界，不要求 bulk 与 collar 的
巨大项进行高精度抵消。将所有固定正、负 spline knots 精确分段，
对每个真实闭子段 \(I_\nu\subset[0,b]\) 证明连续全角界

\[
|J_\delta(r,\theta,\delta)|\le M_\nu
\quad(r,\theta,\delta\in I_\nu\times\mathbb T\times\Delta).
\]

腰部用准确奇对称的积分商同时控制值和参数一 jet。
则

\[
B_{\rm bulk}=\sum_\nu |I_\nu|M_\nu
\]

包含整个普通积分的绝对值，不需要另作角求积。
这些 \(M_\nu\) 必须覆盖节点间隙和无限 primitive 尾；
单独对角节点取最大值不够。

若 (5.1) 的含全部误差区间为 \([L_c,U_c]\)，则

\[
\boxed{
|\beta'(\delta)|
\le B_\delta
:=\frac12\left[
B_{\rm bulk}+\max(|L_c|,|U_c|)
\right].}
\tag{6.1}
\]

在同一实际家族中，若点 \(\delta_0\) 已有
\(\beta(\delta_0)\in[L_0,U_0]\)，参数区间离该点的最大距离为 \(d\)，
就严格得到

\[
\beta(\Delta)\subset[L_0-B_\delta d,\ U_0+B_\delta d].
\tag{6.2}
\]

式 (6.1) 允许保守三角不等式。只有在实际预算仍太大时，
才需要对 bulk 导数做真正有向积分以回收抵消。

## 7. 当前实现边界

原 sym 图的完整 \(\beta\) 已由独立 directed bulk/collar 和准确覆盖证明。
当前 exact affine \(\delta_3\) 的点 collar 已完成，点 bulk 在运行；
两者不与原图混用。
参数 h=1e-8 的 native Arb 根入口已完成，其 collar 正作独立测试。
本篇的固定物理参数一 jet、解析 \(H\) 及 (6.1) 尚待实际代码和预算，
因此本篇不把点证书自动扩展成最终 KAM 参数盒证书。
