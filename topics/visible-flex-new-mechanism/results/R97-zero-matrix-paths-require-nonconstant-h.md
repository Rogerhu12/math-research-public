# R97. 真零二阶矩阵路径必须改变 $h$

本结果加强 [R93](R93-zero-matrix-geometric-energy-and-frame-length.md)。完整二阶矩阵 $M=0$ 不仅迫框架参数 $k$ 变号及 $\max|k|>1$，还迫 $h$ 非恒定。以下都是准确几何积分恒等式；不涉及数值路径，不推出四阶 $V$ 的符号，也不把框架参数 $k$ 当成曲面的主曲率。

## 1. 假设和结论

设真实标量路径定义在 $[0,L]$，$L>0$，$h>0$，有推导所需的连续导数，并在两端具有常值 scalar 芽。特别有 $h_s(0)=h_s(L)=0$。使用同一个初值积分

$$
\omega_s=\frac{k_s}{2h}.
\tag{1}
$$

两端的 $h,k,\omega$ 常值可以不同；不需要先假设框架闭合或空间位移闭合。假设完整二阶算子矩阵 $M=0$，不是只对一个选定 profile 或有限采样点令其为零。

记

$$
\rho=\frac{h_s}{h},\quad
E=\int_0^L\rho^2\,ds,\quad
K_2=\int_0^L k^2\,ds,\quad
F(s)=\int_0^s h(\sigma)k(\sigma)\,d\sigma.
$$

则

$$
F(0)=F(L)=0,\qquad K_2=L+E,
\qquad
\int_0^L hk\omega\,ds=K_2,
\tag{2}
$$

并且有新的相关恒等式

$$
K_2=-\int_0^L\frac{F k h_s}{h^2}\,ds
=-\int_0^L\frac Fh\,k\rho\,ds.
\tag{3}
$$

因此 $E>0$，即 $h$ 必须非恒定。更精确地，令 $U=F/h$，有

$$
\int_0^L(U^2-1)\rho^2\,ds
=L+\int_0^L(k+U\rho)^2\,ds.
\tag{4}
$$

若 $S=\|F/h\|_\infty$，则

$$
S>1,\qquad (S^2-1)E\ge L,
\qquad E\ge\frac{L}{S^2-1}>0.
\tag{5}
$$

这些是任何真实完整 $M=0$ 路径的必要条件，不是存在性充分条件。

## 2. 从完整 $M=0$ 到两个多项式系数

沿用 R93 的局部定义，令 $c$ 在一个共同物理开区间内变化：

$$
z=c+\omega,\quad e=hz-k,\quad Q=1+e^2,
\quad \ell_h=\left(\frac{h_s}{h^2}\right)_s,
$$

$$
K=kz^2-\frac{k^2+1}{h}z+\lambda_s,
\qquad \lambda=\frac{h_sz-h\omega_s}{h^2},
\qquad C=\frac{KQ}{8h},\quad D=\frac{Ke}{4}.
$$

完整 $M=0$ 给

$$
\int_0^L C(s,c)\,ds=0,\qquad
\int_0^L D(s,c)\,ds=0
\tag{6}
$$

对每个这样的 $c$ 成立。由于两边是 $c$ 的多项式，所有系数积分均零。R93 已逐式证明这一使用完整算子的步骤，并给出

$$
C_4=\frac{hk}{8},\qquad
C_3=\frac{hk\omega}{2}-\frac{3k^2+1}{8}
+\frac{h\ell_h}{8},
\tag{7}
$$

$$
D_2-\frac32C_3=\frac{k^2-1+h\ell_h}{16}.
\tag{8}
$$

积分 $C_4$ 得 $F(L)=0$。积分 (8) 得

$$
\int_0^L h\ell_h\,ds=L-K_2.
\tag{9}
$$

另一方面，完整保留边界项的分部积分是

$$
\int_0^L h\ell_h\,ds
=\left[\frac{h_s}{h}\right]_0^L
-\int_0^L\frac{h_s^2}{h^2}\,ds
=[\rho]_0^L-E.
\tag{10}
$$

故在尚未使用端芽条件前已经有 $K_2=L+E-[\rho]_0^L$。常值端芽令边界项消失，得到 (2) 的能量式。

现在积分 $C_3$，由 (7)、(9) 得

$$
0=8\int_0^L C_3\,ds
=4\int_0^L hk\omega\,ds-3K_2-L+(L-K_2).
$$

因此

$$
\int_0^L hk\omega\,ds=K_2.
\tag{11}
$$

这一恒等式仅用了完整系数积分，并没有通过微分未受控余项或假定 $\omega$ 是独立控制。

## 3. 唯一的 $\omega$ 积分与新的相关式

定义

$$
\chi=\omega-\frac{k}{2h}.
$$

由准确关系 (1)，

$$
\chi_s=\frac{k h_s}{2h^2}.
\tag{12}
$$

将 $\omega=k/(2h)+\chi$ 代入 (11)，得到

$$
K_2=\frac12K_2+\int_0^L F_s\chi\,ds.
$$

再次保留全部边界项：

$$
\frac12K_2=[F\chi]_0^L-\int_0^L F\chi_s\,ds.
\tag{13}
$$

这里 $F(0)=F(L)=0$，所以即使两端 $\chi$、$h$ 或 $k$ 不同，边界项也准确为零。用 (12) 即得 (3)。没有逐段重置 $\omega$，也没有把各常态平台各自选定的规范拼成不存在的真实路径。

若 $h$ 恒定，则 (3) 给 $K_2=0$，但 (2) 给 $K_2=L>0$，矛盾。这已经在不要求框架闭合的层面排除了正长度恒 $h$ 的完整零矩阵路径。

## 4. 完全平方与定量条件

由 (3)，

$$
\int_0^L(k+U\rho)^2\,ds
=K_2+2\int_0^L Uk\rho\,ds+\int_0^L U^2\rho^2\,ds
=-K_2+\int_0^L U^2\rho^2\,ds.
$$

再代 $K_2=L+E$，得到 (4)。于是

$$
L\le\int_0^L(U^2-1)\rho^2\,ds
\le(S^2-1)E.
$$

由于 $L>0$，必有 $E>0$、$S>1$，证明 (5)。此证明没有用 Cauchy 等号的额外假设；(4) 还准确记录了不等式的平方余项。

## 5. 与已有构造及 R93 的关系

[R37](R37-closed-geometry-zero-period-operator.md) 的四个 $(h,d)$ 平台允许各平台使用恒 $h$，但平台之间使用真实变 $h$ 连接，并沿 (1) 连续输运唯一的 $\omega$。R37 §4 已指出，全局变 $h$ 连接用来克服恒 $h$ 时 $\omega=k/(2h)+$常数的限制。这里排除的是**整条正长度路径都使用同一个恒 $h$ 且完整 $M=0$**；不排除 R37 的变 $h$ 连接构造，也不排除单个恒态平台。

R93 §4 的“若 $h$ 恒定，再加框架闭合可得 $L>\sqrt2\pi$”只是较弱的条件推论；本结果说明该同时完整 $M=0$ 的恒 $h$ 类实际上为空，应以此更强结论理解，不将前者当作可实现的特殊例。R93 的一般能量式、$k$ 变号、$\max|k|>1$、非恒 $h$ 情形的长度估计都保持有效。

最后，(2)–(5) 约束真实几何路径及其 primitive。它们没有证明 P0 action 非负，没有构造零四阶成本环，也没有把理想 $\pm1$ 跳接当成光滑真实路径。
