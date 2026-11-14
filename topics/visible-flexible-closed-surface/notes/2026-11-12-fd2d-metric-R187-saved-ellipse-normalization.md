# R187/R190 当前保存轴长的准确周长与中央缩放消费

本组绑定当前小幅分支已经保存/读到的两条 IEEE-754 轴长：

- $A$ bits = 0x3ff0767c5c4cf6bc，显示 1.0289271932119126；
- $B$ bits = 0x3fef535f1f0053de，显示 .9789271932119126。

它们作为准确 dyadic 实数。没有重跑 55 步轴长搜索，也没有把该搜索解释成一个不同的精确 gap 方程解。准确中央曲线采用 [R187](../results/R187-closed-unit-angular-tangents-and-direct-position-metric.md) 的原有归一化：以准确 B32 $a_0$ 除以这条保存轴曲线的准确平均周长半径 $a_E$。真实 axis gap 另行包围。

## 1. 全部非负项的准确周长公式

对任意 $A,B>0$，记

$$
C=\frac{A+B}{2},\qquad q=\frac{A-B}{A+B},\qquad |q|<1.
$$

椭圆速度为

$$
\ell(\theta)=\sqrt{A^2\sin^2\theta+B^2\cos^2\theta}
=C\sqrt{1-2q\cos(2\theta)+q^2}.
$$

在单位圆上展开两个一致收敛的 binomial 级数：

$$
\sqrt{1-qe^{2i\theta}}\sqrt{1-qe^{-2i\theta}}.
$$

两支在 $q=0$ 取 1，并连续给出上式正平方根。由于 $|q|<1$，级数绝对一致收敛，可逐项积分；整周均值只保留相同指数。因此

$$
a_E=\frac1{2\pi}\int_0^{2\pi}\ell(\theta)\,d\theta
=C\sum_{n=0}^\infty \binom{1/2}{n}^{\!2}q^{2n}.
\tag{1}
$$

这是已有 common $a_0$ 正项有理证明的同一公式，现消费另一对实际保存轴，不借用旧椭圆的数值结果。

令 $t_n=\binom{1/2}{n}^2q^{2n}$，则

$$
t_0=1,\qquad
t_{n+1}=t_nq^2\frac{(2n-1)^2}{4(n+1)^2}.
$$

所有项非负，后续项比至多 $q^2$。累加 $0\le n<N$ 后，

$$
C\sum_{n=0}^{N-1}t_n
\le a_E
\le C\left(\sum_{n=0}^{N-1}t_n+\frac{t_N}{1-q^2}\right).
\tag{2}
$$

在 $q=0$ 的圆情形尾项准确零。全部输入 dyadic，式(2)全由 BigInt 有理运算完成。这里的截断误差是明确几何尾，不是 successive approximation 的浮点差。

## 2. 准确目标半径与归一化

准确 B32 中央 $a_0$ 来自已推文件
notes/2026-11-12-fd2d-balanced-moments-taylor-01.json，
8881 B，SHA256 0da13490030b82f536a921a97083b38f606ab604e7c7195c9053fb7975fa4b03。

本次直接使用其 enclosures.a0.binary_lower/binary_upper 的完整整数 mantissa 和 exponent，未先经 Number。该文件整体 passed=false 是其他已声明宽度偏好没有达到；其已带解析余项的 $a_0$ 区间仍有效，不得反过来删掉它或冒成一个新的成功整包。

由正区间除法，准确缩放与轴为

$$
\lambda=\frac{a_0}{a_E},\qquad
A_*=\lambda A,\qquad B_*=\lambda B,\qquad
\operatorname{gap}=\lambda(A-B).
\tag{3}
$$

没有将有限 evaluator 的 a0 或 aE 插入式(3)充作准确值。后续准确材料角也必须使用同一 $a_E$，使实际中央切向速度为 $a_0$。

## 3. 整条中央曲线的曲率范围

椭圆 $(A_*\cos\theta,B_*\sin\theta)$ 的准确曲率为

$$
\kappa(\theta)=
\frac{A_*B_*}
 {(A_*^2\sin^2\theta+B_*^2\cos^2\theta)^{3/2}}.
$$

令 $A_+\!=\max(A,B)$、$A_-\!=\min(A,B)$。分母在
$\lambda^3A_-^3$ 与 $\lambda^3A_+^3$ 之间变化，且两个端值真实取得，所以

$$
\kappa_{\min}=\frac{a_E}{a_0}\frac{A_-}{A_+^2},
\qquad
\kappa_{\max}=\frac{a_E}{a_0}\frac{A_+}{A_-^2}.
\tag{4}
$$

这是整条中央曲线的全域值，不是角网格采样；它不包含中央以外曲面或帽。

## 4. 真实执行和输出

源码
scripts/fd2d_R187_saved_ellipse_normalization_exact.cjs，
8239 B，SHA256 efdd34fd43db8da8b11e3cd0a319b04e11d068a36931b99cf0d8adb124a3ed45。

接口 certifySavedEllipseNormalization(input) 要求完整 raw axis bits、准确 $a_0$ 包、provider/candidate 身份；它明确设置 exact_gap_root_solved=false 和 material_angle_inverse_certified=false。

实际 functions JavaScript isolate 已完成当前真实 seed 消费，1.467 秒，无 OS 子进程。使用 $N=32$，输出向外取到 $2^{-192}$ dyadic 格；这一取整只是压缩严格有理输出，不改变式(2)的准确内部运算。

真实结果显示：

| 量 | 严格区间的显示值 |
|---|---:|
| $a_E$ | 1.0040828380214692 |
| 准确 scaled gap | .050000000000000024 |
| gap $-1/20$ | $2.590578219946084\cdot10^{-17}$，严格正 |
| $\kappa_{\max}$ | 1.0737022413329813 |

上述每个展示量的严格有理上下端点均在报告中，宽度为 $2^{-192}$；显示小数不是替代端点。

另一个准确圆输入的尾项和 gap 均准确为零，属于同一次薄算术核。没有主线 F/J、LM 或 BVP。

报告
notes/2026-11-12-fd2d-metric-R187-saved-ellipse-normalization-01-report.json，
11312 B，SHA256 8c2f37b42187712e5cb20cc24e7b862d5b71b8b4c20224738837ab84b23717c6。

本组付清当前保存轴长的准确周长、中央归一化和整条中央曲线曲率范围。完整材料角反解、primitive、准确 B32 全长/高度及整曲面 metric/curvature/reach 仍须各自的真实消费者。
