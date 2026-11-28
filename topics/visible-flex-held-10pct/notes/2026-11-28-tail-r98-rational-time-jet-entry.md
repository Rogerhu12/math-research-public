# R98 的真实 fixed 前缀、切口和短柱时间常数入口

本条是已经实现并作精确代数核验的来源适配与计算结论。尚无真正
own fixed 输入执行记录，因而没有新增某个闭图的 $M_2,M_{g,2},V_{g,1}$
数值，也没有宣称全图时间证书。原 R98 条件命题、旧角表和旧科学场均未改。

## 1. 新实现和真实执行

新增三个独立源：

* scripts/resume_20261128/tail/rational_time_jet_bounds.py：
  全部 Fraction 运算的核心曲率、$\Gamma^{(5)}$、四阶角导、逆角图和时间界。
* scripts/resume_20261128/tail/qr_fixed_prefix_time_bounds.py：
  真正 own fixed 来源和原完整角表、cut 数据的消费入口。
* scripts/resume_20261128/tail/check_rational_time_jet_bounds.py：
  独立带符号隐式角图的精确代数核验。

三个源均实际 py_compile 返回 0；入口 --help 实际返回 0。
checker 实际返回 0，共 114 项通过。其 8 组形式有理角图各核全部 12 项
混合导数，另核零 chart 恒等、真实相位频率的代数关系、严格 dyadic
平方根上界、原端点 Gram 时间步条件和与已审核心曲率标量公式的一致性。
这些是形式代数输入，不是伪造的已接受场。没有调用 BVP、native、
低 $\lambda$ 场、核心位置积分或尾部再生。

原始小记录：
held10-tail-preparation/rational-time-jet-20261128/algebra.json，
SHA256 为 5aadef4085d88b95da38f46f12635692c036f2d8351d605c7a15b73d42ddc7ca。
完整来源 SHA 和实际命令在同名 JSON。

## 2. 复用原完整场，不重新选择均值或模式

新入口直接复用已冻结 qr_fixed_complete_prefix_c2.py 的 load_field、
RadialPolynomials 和原精确 Bernstein 多项式代数。真正的 own fixed
接受门先执行；以同一输入调用既有双场门仅复用完整来源检验，
没有计算或宣称“自己与自己”的精化结论。

load_field 原样核对真实 full physical H、完整 fixed_problem、源均值节点数、
GL6 规则、全部 planar/height 模式、共享 Hermite 定义、原完整
0..3 角表和真实 cut 系数。切口全部尾模及零模导数都保留。
入口不重建均值、共享系数或原角表；真实目标半径由原 FrozenTarget
及其向外舍入 oracle 在完整公共径向细分上重新给出正下界。

## 3. 新的四阶角导与 $\Gamma^{(5)}$

令原 support 为

$$
\rho_0(\phi)=1+\sum_m c_m\cos(m\phi),\qquad
B_j=\sum_m |c_m|m^j,\qquad r=1-B_0>0.
$$

所有保存模式都进入这些和。纯有理源按 R98 的原曲率链式式计算
$\kappa,\kappa_u,\kappa_{uu},\kappa_{uuu}$ 的上界及

$$
\|\Gamma^{(5)}\|
\le 6K^2K_1+K_3+K^4+4KK_2+3K_1^2.
$$

此处 $K^4$ 是四次幂。它没有假装原 true-core oracle 多返回一个字段，
也没有把 range(4) 的旧 0..3 表称为四阶导数表。

固定三重中心的真实单位速曲线还满足

$$
\sqrt3\,|\Gamma(u)|
=|\Gamma(u+2\pi/3)-\Gamma(u)|
\le 2\pi/3,
$$

故由 $\pi<22/7$、$\sqrt3>5/3$ 得
$|\Gamma|\le44/35$，真实 held 圆心
$O=\Gamma(\pi/3)-n(\pi/3)/k$ 满足
$|O|\le44/35+1/k$。这是原三重归一化的推论，不是另选原点，
也未把数值 Gauss 位置或圆整圆心当精确定义。

设 $\theta_0=\psi-E_0\sin(3\psi)/3$，$\rho=\theta_0'$。
新角导界使用完整恒等式

$$
(\Gamma\circ\theta_0)^{(4)}
=\rho^4\Gamma^{(4)}
+6\rho^2\rho'\Gamma^{(3)}
+(3(\rho')^2+4\rho\rho'')\Gamma''
+\rho'''\Gamma'.
$$

中心第二径向目标是 $b\Gamma'(\theta_0)$；其四阶角导完整为

$$
\begin{aligned}
&b^{(4)}\Gamma'
+(4b'''\rho+6b''\rho'+4b'\rho''+b\rho''')\Gamma''\\
&+(6b''\rho^2+12b'\rho\rho'
  +b(3(\rho')^2+4\rho\rho''))\Gamma^{(3)}\\
&+(4b'\rho^3+6b\rho^2\rho')\Gamma^{(4)}
+b\rho^4\Gamma^{(5)}.
\end{aligned}
$$

减去真实完整有限 Fourier 投影、端点系数及共享 lift 后，以三角不等式
形成新增 lift_fourth/center_fourth。旧 0..3 上界仍来自其原真实角表。
cut 的四阶界直接对实际全部系数区间累加 $|m|^4|c_m|$；
没有调用旧 height Fourier 读器只支持二阶的分支。

## 4. 同物理材料角，不用同计算角代替

记 $\theta=\psi-e(s)\sin(3\psi)/3$，并令

$$
\rho=1-e\cos3\psi,\quad
V=\rho^{-1},\quad U=\frac{e'\sin3\psi}{3\rho},
$$

$$
A=\frac{e''\sin3\psi/3+2e'\cos3\psi\,U
             -3e\sin3\psi\,U^2}{\rho}.
$$

这是实际逆图的 $V=\psi_\theta,U=\psi_s,A=\psi_{ss}$。
只在绝对值 majorant 中把最后的负号换为加号。
对 $F(s,\theta)=X(s,\psi(s,\theta))$，先构造

$$
F_s=X_s+UX_\psi,\qquad
F_{ss}=X_{ss}+2UX_{s\psi}+U^2X_{\psi\psi}+AX_\psi,
$$

再逐次作用 $D_\theta=V D_\psi$。有限 Taylor 系数以
$|D_\psi^j f|/j!$ 为上界；乘积取卷积、导数乘精确阶数，
$1/\rho$ 的系数按正递推计算。由此只需真实
$X_{s^r\psi^j}$ 的 $r\le2,\ r+j\le4$ 和 $e,e',e''$，
不需要不存在的共享径向三阶导数。

每个实际共享径向区间上的全模系数、lift 和 chart 都由原 Fraction
quintic/Bernstein 求界；中心与 cut repair 接点都显式加入细分。
所有区间完成后才给前缀常数。每段持久保存的只是实际三个时间常数、
正 frame 下界和可重算完整 majorant 的 SHA，不重复落盘大派生数组。

## 5. 可直接用于 R98 的常数和准确范围

在原 affine 相位 $\alpha(t)=\Omega t$ 下，新源按 R98 真 held 表达式计算
所有六个空间二阶 jet 的 $\partial_{tt}X$ 上界，再用全 Jacobian/
对称 Hessian 的 Frobenius 上界支付相应 operator/bilinear 范数。
按原 $g=ds^2+a(s)^2d\theta^2$ 归一化后单列
$M_{g,2}$ 和 $V_{g,1}$。平方根以经精确整数平方不等式验证的 dyadic
有理上界计算，显示浮点不参与认证。

短柱使用同一真实 $\Gamma$ 和相同 held 圆心，不改任何 cap 参数。
上下前缀通过原反射等距关系共用界。报告只在全径向覆盖后将以下三块置为完成：

* upper_prefix_and_cut；
* lower_reflected_prefix_and_cut；
* central_cylinder。

实际完整有限尾、两个 deep collar 和两个 Cartesian marker disk
仍逐项列在 pending_components。whole_surface_time_constants_certified
始终为 false；没有一个“部分最大值”被升级为全闭图常数。
它也不宣称原空间精化已是 Cauchy 列、时间插值已执行或 README 已完成。

未来一个真正 own fixed 场及其真实表/cut 返回后，执行：

~~~bash
python topics/visible-flex-held-10pct/scripts/resume_20261128/tail/qr_fixed_prefix_time_bounds.py \
  --source-run /absolute/actual-own-fixed/run.json \
  --tables /absolute/same-field-angular/summary.json \
  --cut /absolute/same-field-complete-cut/summary.json \
  --phase-end 4/5 --held-width 27/50 --cylinder-half-length .0025 \
  --outdir /absolute/scratch/new-own-fixed-time-prefix
~~~

这些示意路径没有被当作真实输入执行。下一独立组件须从同一真正
physical-H 全谱 bundle 支付完整尾、深 collar 和 Cartesian 盘时间界；
只有准确的组件并集全覆盖后才允许汇总全图 $M_2,M_{g,2},V_{g,1}$。
