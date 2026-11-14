# R37：固定型别修正与真实度量缺陷的 Newton 接口

2026-11-12，independent-audit。

**状态：已证明的中间结论。** 对当前真实严格星形图，本文给一个
保持目标径向曲率零集的自伴修正算子，并准确计算它与真实度量导数
之间的误差。修正系数由实际度量残差的 $C^2$ 范数控制，不由形变
振幅控制；球面兼容重建将这个误差转回真实应变，给明确的二次
Newton 接口。

这不是把修正算子称为真实导数。它的全频逆、有限增广、强角/径向
范数、多个持握帽的相对刚体条件和实际非线性收敛门仍须支付。
本文也不把有限阶径向 spline 自动升级为高阶光滑数据。

## 1. R32 的完整算子在真实材料坐标中的精确系数

固定当前浸入 $F$ 及其外法向 $n$。在材料圆柱 $(r,\theta)$ 上记
$$
R=|F|,\quad u=F/R,\quad \zeta=n\cdot u>0,\quad
G=\det g_F,\quad
\mathrm{II}=\begin{pmatrix}L&M\\M&N\end{pmatrix}.
$$
所有下面的线性化都使用这个**固定的当前坐标**；不会在一次求导中
随 $F+V$ 偷换成新的径向材料坐标。

径向投影的真实面积密度是
$$
j_u=\frac{\zeta\sqrt G}{R^2}.
\tag{1.1}
$$
R32 的 $B=\nabla_\sigma^2\rho+\rho\sigma$、$\rho=1/R$ 拉回材料坐标后，
$$
B=-\frac{\rho^2}{\zeta}\,\mathrm{II}.
$$
二维的散度密度矩阵为 $\operatorname{cof}B/j_u$，因此完整
$\mathcal D_\rho$ 拉回并乘以 $j_u$ 后为
$$
P w=\partial_r(a w_r+b w_\theta)
+\partial_\theta(b w_r+c w_\theta)+d w,
\tag{1.2}
$$
且有准确公式
$$
\boxed{\quad
\mathsf A=\begin{pmatrix}a&b\\b&c\end{pmatrix}
=-\frac{\operatorname{cof}(\mathrm{II})}{\zeta^2\sqrt G},
\qquad
\det\mathsf A=\frac{K_{g_F}}{\zeta^4}.
\quad}
\tag{1.3}
$$
$d=j_u\operatorname{tr}_\sigma B$ 是同一个真实零阶密度。
公式 (1.1) 可由径向投影的面积 Jacobian
$(F\cdot n)/|F|^3$ 直接得到；(1.3) 再由 R32 的第二基本形式恒等式
及二维 cofactor 的一次齐次性得到。

特别 $a=-N/(\zeta^2\sqrt G)$。以下只在已证明 $a>0$ 的有限材料
圆柱使用此消元；不能在 $N=0$ 处继续除以 $a$。

## 2. 固定目标曲率型别的真实修正

令 $g_0$ 为当前目标径向度量，其曲率 $K_0=K_{g_0}$ 只依赖 $r$。
置实际度量残差
$$e_g=g_F-g_0.$$
定义
$$
\omega=\frac{K_{g_F}-K_0}{\zeta^4 a},\qquad
\widehat a=a,\quad\widehat b=b,\quad
\widehat c=c-\omega=\frac{b^2}{a}+\frac{K_0}{\zeta^4a}.
\tag{2.1}
$$
若暂时保留同一个 $d$，则准确有
$$
\boxed{\quad
\det\widehat{\mathsf A}=\frac{K_0(r)}{\zeta^4},\qquad
P-\widehat P=\partial_\theta(\omega\partial_\theta).
\quad}
\tag{2.2}
$$
所以在目标简单根 $r=r_*$ 上，
$$
\partial_r\det\widehat{\mathsf A}|_{r_*}
=\frac{K_0'(r_*)}{\zeta(r_*,\theta)^4}.
\tag{2.3}
$$
根不再随角移动，法向系数仍为实际 $a>0$。
若 $K_0>0$，矩阵 $\widehat{\mathsf A}$ 正定；
若 $K_0<0$，它严格双曲。这些结论不要求当前非径向振幅很小。

全局应用可以在一个远离极点的材料圆柱中进行。取径向 cutoff
$\chi$，在全部目标转折及所需核心上等于 $1$，在该圆柱外等于 $0$，
并用 $\chi\omega$ 代替 $\omega$。此时
$$
\det\widehat{\mathsf A}
=\frac{(1-\chi)K_{g_F}+\chi K_0}{\zeta^4}.
\tag{2.4}
$$
若 cutoff 过渡区中两个曲率同为正，则不会产生新根。
这个共同符号可由下一节的明确残差界及目标正曲率余量验证。
它不是无条件的 cutoff 性质。

本步骤避免的是**为修正算子**引入移动隐式根：
其根固定为径向 $r_*$，后续 $r$-保持 shear 不需要先解
$t(\theta)$。它没有证明真实 $g_F$ 的曲率根不移动，
更没有把 $\widehat P$ 写成真实度量导数。

## 3. 曲率差的明确 $C^2$ 残差常数

在所用材料圆柱，假设两度量的最小特征值均至少 $m>0$，
各组件及其一、二阶坐标导数分别满足绝对界
$M_0,M_1,M_2$。记
$$
\varepsilon_j=\max_{a,b,\ |\alpha|=j}
\|\partial^\alpha(g_F-g_0)_{ab}\|_\infty,\qquad j=0,1,2.
$$
则可取完整粗界
$$
\boxed{\begin{aligned}
\|K_{g_F}-K_0\|_\infty
\le{}&\frac{2\varepsilon_2}{m^2}
+\frac{36M_1\varepsilon_1}{m^3}\\
&+\left(
\frac{36M_1^2}{m^4}
+\frac{8M_0M_2}{m^4}
+\frac{72M_0M_1^2}{m^5}
\right)\varepsilon_0.
\end{aligned}}
\tag{3.1}
$$

**证明。** 写第一类 Christoffel 符号
$$
\mathfrak C_{ij\ell}
=\tfrac12(g_{i\ell,j}+g_{j\ell,i}-g_{ij,\ell}).
$$
按与旋转度量 $dr^2+a(r)^2d\theta^2$ 给
$R_{1212}=-aa''$ 相容的约定，
$$
R_{1212}
=\tfrac12(2g_{12,12}-g_{11,22}-g_{22,11})
+g^{k\ell}
(\mathfrak C_{12k}\mathfrak C_{12\ell}
-\mathfrak C_{11k}\mathfrak C_{22\ell}).
\tag{3.2}
$$
有 $|\mathfrak C|\le3M_1/2$、$|\Delta\mathfrak C|\le3\varepsilon_1/2$、
$|g^{k\ell}|\le m^{-1}$，以及
$|\Delta g^{k\ell}|\le2\varepsilon_0/m^2$。
因此
$$
|R_{1212}|\le2M_2+18M_1^2/m,
$$
$$
|\Delta R_{1212}|
\le2\varepsilon_2+36M_1\varepsilon_1/m
+36M_1^2\varepsilon_0/m^2.
$$
再用 $\det g\ge m^2$、
$|\det g_F-\det g_0|\le4M_0\varepsilon_0$，以及
$K=R_{1212}/\det g$ 即得 (3.1)。

若 $\zeta\ge\zeta_*>0$、$a\ge a_*>0$，则
$$
\boxed{\quad
\|\omega\|_\infty
\le\frac{\text{(3.1) 的右端}}{\zeta_*^4a_*}.
\quad}
\tag{3.3}
$$
高阶系数界可对准确公式 (2.1)、(3.2) 逐阶求导；
每一项至少含一次 $e_g$ 或其导数。需要 $r$ 阶曲率差时，应供应
度量残差到 $r+2$ 阶及相应 reciprocal 表，不能把 (3.1) 的低阶界
充当任意高阶 tame 估计。

## 4. 保持真实帽 ground state 的自伴修正

只改主系数一般破坏原来的 $\mathcal D_\rho Y=0$。
在 $Y=a_0\cdot u>0$ 的正帽上，正确的零阶修正是
$$
\widehat d=-\frac{\operatorname{div}
 (\widehat{\mathsf A}\nabla Y)}{Y}.
\tag{4.1}
$$
它保 $\widehat P Y=0$，所以同一个真实变换仍有
$$
Y\widehat P(YU)=
\operatorname{div}(Y^2\widehat{\mathsf A}\nabla U).
\tag{4.2}
$$
零阶差也是残差因子：
$$
\widehat d-d=Y^{-1}\partial_\theta(\omega Y_\theta)
\tag{4.3}
$$
（使用 cutoff 时将 $\omega$ 换成 $\chi\omega$）。

有一个方便的全局自伴写法。选实光滑 $\ell(r,\theta)$，
在相应正帽等于 $Y_\theta/Y$，在核心可为 $0$，
并用固定 cutoff 在已知 $Y>0$ 的区域过渡。令
$$
Q_\ell=\partial_\theta-\ell,\qquad
Q_\ell^*=-\partial_\theta-\ell
$$
为材料密度中的真实形式 adjoint。定义
$$
\boxed{\quad
\widehat P-P
=Q_\ell^*(\chi\omega)Q_\ell.
\quad}
\tag{4.4}
$$
展开后主系数正是 $c-\chi\omega$，零阶增加
$$
(\chi\omega\ell)_\theta+\chi\omega\ell^2.
\tag{4.5}
$$
在帽上 $\ell=Y_\theta/Y$ 时，(4.5) 等于 (4.3)；
在 $\ell=0$ 的核心，仅剩 (2.2) 的主系数修正。
中间的每个新增项也仍含一次真实残差系数 $\omega$。

特别，弱层估计无需先对曲率差再求一次角导：
$$
\langle(\widehat P-P)w,\varphi\rangle
=\int\chi\omega\,
 (w_\theta-\ell w)\overline{(\varphi_\theta-\ell\varphi)}
 \,dr\,d\theta .
\tag{4.6}
$$
因此其 $H^1\to H^{-1}$ 大小直接由 $\|\omega\|_\infty$ 控制。
强径向/角向输出仍须按 (4.5) 支付相应有限 jets。

将该修改拉回球面，记为
$\widehat{\mathcal D}=\mathcal D_\rho+\mathcal E$。
若 $X=\partial_\theta$ 在球面上的实际推前向量场，
且修正支撑内 $j_u\ge j_*>0$，令
$$
q_*=\sup_{\operatorname{supp}\chi}
\sqrt{|X|_\sigma^2+|\ell|^2}.
$$
则由 (4.6) 有准确低层界
$$
\boxed{\quad
\|\mathcal Ew\|_{H^{-1}_\sigma}
\le \left\|\frac{\chi\omega}{j_u}\right\|_\infty
q_*^2\|w\|_{H^1_\sigma}
\le j_*^{-1}\|\omega\|_\infty q_*^2\|w\|_{H^1_\sigma}.
\quad}
\tag{4.7}
$$
这里 $H^1_\sigma$ 的平方范数为
$\int(|w|^2+|\nabla_\sigma w|^2)$。
所有密度、ground state 和 cutoff 都是实际对象。

## 5. 任意兼容缺陷的全局球面重建

延用 R32 的
$$
\mathcal Ce=\operatorname{div}\operatorname{div}e
-\Delta\operatorname{tr}e-\operatorname{tr}e,
$$
其真实形式 adjoint 为
$$
\mathcal C^*\phi
=\nabla^2\phi-(\Delta\phi+\phi)\sigma.
\tag{5.1}
$$
有
$$
\operatorname{div}(\mathcal C^*\phi)=0,\qquad
\mathcal C\mathcal C^*
=(\Delta+1)(\Delta+2).
\tag{5.2}
$$
一次球谐是 (5.2) 的全部 kernel。任意张量 $e$ 的
$\mathcal Ce$ 都与它们正交，因为 $\mathcal C^*Y_1=0$。

定义
$$
\boxed{\quad
\mathcal C^\dagger
=\mathcal C^*
[(\Delta+1)(\Delta+2)]^\dagger ,
\quad}
\tag{5.3}
$$
其中 $\dagger$ 只去掉一次球谐；零次球谐保留，其分母是 $2$。
则
$$
\mathcal P e:=\mathcal C^\dagger\mathcal Ce
\tag{5.4}
$$
是 $L^2$ 中到无散度对称张量的正交投影。
若 $q$ 与球面 Killing 场正交，解
$$
\operatorname{div}\mathcal L_q\sigma=\operatorname{div}e,
$$
就精确得到
$$
\boxed{\qquad e=\mathcal L_q\sigma+\mathcal P e.\qquad}
\tag{5.5}
$$

**证明。** R32 命题 4.1 的球谐构造对任意右端
$\operatorname{div}e$ 都可使用，因为它与 Killing 场自动正交。
其剩余张量 $T=e-\mathcal L_q\sigma$ 无散度，且
$\mathcal CT=\mathcal Ce$。
$\mathcal C^\dagger\mathcal Ce$ 也具有这两性质；
两者之差无散度且 $\mathcal C$ 为零，由 R32 的无迹/Codazzi
论证必为零。因此 (5.5) 成立。
无散度张量与所有 $\mathcal L_q\sigma$ 的 $L^2$ 配对为零，
故 (5.4) 确是正交投影。

令 $\mathcal H^s$ 为 R32 的旋转 Casimir Sobolev 范数。
对所有实 $s$，有明确界
$$
\boxed{\quad
\|\mathcal C^\dagger h\|_{\mathcal H^s}
\le\frac7{\sqrt{20}}\,
 \|h\|_{H^{s-2}_\sigma},
\qquad h\perp\{Y_1\}.
\quad}
\tag{5.6}
$$
因为在标量球谐 $\lambda=\ell(\ell+1)$ 上，
$$
\|\mathcal C^*Y_\ell\|_2^2
=(\lambda-1)(\lambda-2)\|Y_\ell\|_2^2.
$$
$\ell=0$ 给所需比值 $1/\sqrt2$；
$\ell\ge2$ 时
$$(1+\lambda)/\sqrt{(\lambda-1)(\lambda-2)}\le7/\sqrt{20},$$
最大值在 $\lambda=6$。旋转等变性保证输出仍在同一 Casimir 档。
本文把 $\mathcal C^\dagger$ 在一次球谐上定义为零，必要时可对任意
$h$ 使用同一个界和这个投影约定。

R32 对 $q$ 的重建范数也继续成立，且可用
$\|\mathcal L_q\sigma\|\le\|e\|$：分解 (5.5) 在每个 Casimir 档均
正交，所以切向场仍有一个有界、增一阶的真实重建。

## 6. 修正标量解与真实应变之间的精确误差

给当前完整期望应变 $f$，令 $w$ 满足
$$
\widehat{\mathcal D}w
=-\tfrac12\mathcal C(\rho^2f)+r_{\rm sc}.
\tag{6.1}
$$
这里 $r_{\rm sc}$ 是实际标量求解缺陷，不能默认为零。
置
$$e=\rho^2f-2wB,$$
按 (5.5) 重建 $q$，再按 R32 的准确式
$$V=\rho^{-1}(q+w\nabla\rho)+w u.$$
则
$$
\mathcal Ce
=2(\mathcal D_\rho-\widehat{\mathcal D})w+2r_{\rm sc},
$$
并有关键的**真实度量导数恒等式**
$$
\boxed{\quad
Dg_F[V]-f
=2\rho^{-2}\mathcal C^\dagger
\bigl[(\widehat{\mathcal D}-\mathcal D_\rho)w-r_{\rm sc}\bigr].
\quad}
\tag{6.2}
$$
证明只需将 (5.5) 放回
$\rho^2Dg_F[V]=\mathcal L_q\sigma+2wB$。
特别是误差的正负号来自真实重建，不是把 $\widehat{\mathcal D}$
误认成 $\mathcal D_\rho$。

若 (6.1) 只在去掉一次球谐的空间求解，则
$r_{\rm sc}$ 可含明确的一次球谐项；它在 (6.2) 中被
$\mathcal C^\dagger$ 杀去。但在局部 PDE、源和持握端口中，
这些项仍是实际有限维 source/约束，不能提前删除。
修正后所有失去的 translation kernel 也可用这三个明确增广变量
处理；这不等于已经证明增广系统满射。

对低层误差，记
$$
M_\rho=\|\rho^{-2}\|_\infty+
\left(\sum_{i=1}^3
 \|\mathcal L_{\Omega_i}(\rho^{-2})\|_\infty^2\right)^{1/2},
\qquad \Omega_i=e_i\times u.
$$
Leibniz 法则给乘法
$\|\rho^{-2}T\|_{\mathcal H^1}\le M_\rho\|T\|_{\mathcal H^1}$。
由 (4.7)、(5.6)，得到完全明确的实际应变误差界
$$
\boxed{\begin{aligned}
\|Dg_F[V]-f\|_{\mathcal H^1}
\le \frac{14M_\rho}{\sqrt{20}}
\left[
 \frac{q_*^2\|\omega\|_\infty}{j_*}\,
 \|w\|_{H^1_\sigma}
 +\|r_{\rm sc}\|_{H^{-1}_\sigma}
\right].
\end{aligned}}
\tag{6.3}
$$
这里 $\|\omega\|_\infty$ 由 (3.1)--(3.3) 的真实 $C^2$ 度量残差
控制。没有因坐标归一而消失的几何常数。

## 7. 准确 Newton 恒等式及有限导阶要求

若当前目标在这一步固定，取 $f=g_0-g_F=-e_g$。
令新图为 $F_{\rm new}=F+V$，则逐点有
$$
g_{F_{\rm new}}-g_0
=(Dg_F[V]-f)+dV\cdot dV.
\tag{7.1}
$$
因此 (6.2) 是修正逆的线性求解误差，
$dV\cdot dV$ 是真实几何的完整二次余项。
当已认证的修正标量逆给 $\|w\|\lesssim\|e_g\|$，
且 $r_{\rm sc}$ 具有相应二次小量时，
(3.3)、(6.3) 把第一项也给成一个残差乘修正的二次项。

这是一条准确接口，不是一个已经闭合的 Banach 收缩证明。
例如 (3.1) 使用残差到 $C^2$，
而 (6.3) 只陈述 $\mathcal H^1$ 输出；不能把它们视为同一个无损
Banach 档。要获得最终 $C^2$ 场及完整源，仍须选择足够的有限 Sobolev、
角权和径向档，支付两阶曲率源、逆的角损、乘法、坐标和每轮
smoothing/增量预算。R32 的切向重建不会自动补回这些缺失档。

若目标径向度量也随均值参数更新，$f$ 必须包含同一次实际参数导数列，
并把目标度量的参数 Taylor 余项计入 (7.1)。
不能在算完修正后自由重选一个目标来抹去未控制的非零模残差。

## 8. 持握不被全局兼容投影自动保留

即使 $f=w=0$ 在一个开帽，(5.5) 的全局投影
$T=\mathcal Pe$ 也未必在那里为零。因此此时只得
$$
\mathcal L_q\sigma=-T
$$
在该帽成立，不能直接套用 R32 的“局部 Killing 即可消去”论证。
准确固定帽需要一个额外修复，或在同一增广系统中直接保持其迹。

下面给一个可用的局部修复接口。设
$H_0\Subset H_1$ 为固定连通开帽，$f=w=0$ 在 $H_1$，
且 $H_1$ 中各点可由同一基点以长度至多 $D_H$ 的曲线连接。
对任意球面切向场 $q$，令
$$
E=\tfrac12\mathcal L_q\sigma,\qquad
r=\tfrac12\varepsilon^{ij}\nabla_iq_j,\qquad
\Omega(q)=u\times q+r u.
\tag{8.1}
$$
它满足 $q=\Omega(q)\times u$。在一个定向正交标架中，定义
$$
\beta_i=\varepsilon^{jk}\nabla_jE_{ik}.
$$
直接微分 (8.1)、交换球面协变导数，得到
$$
D_i\Omega=J(E_i{}^\sharp)+\beta_i u,\qquad
|D\Omega|^2\le |E|^2+2|\nabla E|^2.
\tag{8.2}
$$
例如正常坐标中
$\beta_1=E_{12;1}-E_{11;2}$、
$\beta_2=E_{22;1}-E_{12;2}$；
曲率项正好与微分 $r u$ 产生的切向旋转项抵消。

取 $\Omega_0$ 为基点的 $\Omega(q)$，则
$$
\|q-\Omega_0\times u\|_{C^0(H_1)}
\le D_H\bigl(\|E\|_\infty+\sqrt2\|\nabla E\|_\infty\bigr).
\tag{8.3}
$$
又
$\nabla(q-\Omega_0\times u)=E+(r-\Omega_0\cdot u)J$，
故同一式给明确 $C^1$ 界。继续微分 (8.2) 给任意预选有限阶界，
所需阶数是实际 $E$ 的对应有限阶，而不是一个免费光滑性结论。

在本情形 $E=-T/2$。先减去环境全局旋转 $\Omega_0\times F$，
它不改变应变；再取一个固定 cutoff $\chi_H$，在 $H_0$ 为零，
在 $H_1$ 外为一，将帽内剩余小切向场改为
$\widetilde q=\chi_H(q-\Omega_0\times u)$。
因 $w=0$ 在 $H_1$，实际 $\widetilde V$ 在 $H_0$ 精确为零。
新增应变是
$$
(\chi_H-1)\mathcal L_{q-\Omega_0\times u}\sigma
+d\chi_H\otimes(q-\Omega_0\times u)^\flat
+(q-\Omega_0\times u)^\flat\otimes d\chi_H,
\tag{8.4}
$$
再乘 $\rho^{-2}$。由 (8.3) 它由 $T$ 的对应有限范数控制，
所以在前面已经付出二次兼容缺陷时，修复不引入线性级别的新误差。

对多个不相连帽，只能用一个全局旋转消去共同部分。
各帽按 (8.1) 读出的 $\Omega_i$ 的相对差，仍须作为真实有限行条件
控制到同一二次级别，或精确设为相同。
不能分别减去不同的刚体旋转再称其为一个全局规范；
那会在连接区产生通常为一阶大小的新应变。

## 9. 与既有固定型别路线的关系和当前未付项

邻题的
[R492](../../continuous-flexibility-swarm/results/R492-updated-background-fixed-type-input.md)
使用的是残差修正型算子：
其真实导数与固定型别算子之差为一个
$\partial_\theta(B_F\,\mathcal F\,\partial_\theta)$ 项，
不是“对任意近似图，真实主系数已经固定型别”的声明。
本文独立从 R32 的实际全局标量化推导 (1.3)--(6.3)，把这种
残差修正准确转回当前真实度量导数；没有引入一个假定的全频 provider。

目前已经得到的正向接口是：

1. 真实 metric 残差的 $C^2$ 控制给 (3.1) 的曲率差，
   从而给一个固定径向转折的真实修正算子。
2. 帽上可保所选正 ground state，并保自伴 form、实际源和通量；
   核心保留其完整零阶项和有限增广。
3. 修正标量解通过 (6.2) 恢复到真实应变，误差明确是残差乘修正，
   而不是被省略的主项。
4. 精确持握可在已付兼容缺陷及相对刚体条件下按第 8 节修复。

尚须为当前候选的 $\widehat{\mathcal D}$ 构造真实 Airy/负组件/完整
相位正常形和强逆，支付 R34 的全部实际相位输入、有限低模及均值行，
并把 (7.1) 的二次预算闭合到有限可见形变。
本文没有宣布这些门已经满足。
