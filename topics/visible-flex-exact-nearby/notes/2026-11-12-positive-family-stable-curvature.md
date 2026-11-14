# 真实 affine 正外段：先消去轴对称主项，再作有向曲率计算

2026-11-12，independent_audit。本文记录新实际外段引擎的准确等式和误差
预算。完整有限 body 覆盖仍在运行；除被完整报告覆盖的范围外，本文不把
采样或部分子区间称为已证正域。它不构造 $r>3$ 的非线性外延。

## 1. 同一准确族

中心使用 `type_fixed_step02_d5_exact_affine_step4_object.json`，

\[
\delta_4=-7789866024620307/4611686018427387904,
\qquad |\delta-\delta_4|\le 1/2000000.
\]

raw 相位与 mean 方向先形成完整准确多项式 germ，之后才把一个共同实参数
加入，最后进行三角运算与真无限角原函数。这个盒包含当前准确 $\delta_5$，
没有把方向加到已经四舍五入的控制数组中。所有正负 knots 用准确 Fraction
取共同分割；每一子区间显式选实际 scalar span。

源为 [fourfold_phase_positive_family_outer.py](../scripts/fourfold_phase_positive_family_outer.py)。
它复用冻结的 parameter-germ、native scalar、有向 Fourier 核及
[R64](../results/R64-actual-positive-collar-source-and-dn-input.md) 的准确
材料标架。冻结 R64 的 $\delta_4$ 单点报告不被覆盖或改称参数族。

## 2. 从真切向量中准确去掉圆周背景

始终在旋转柱坐标基书写向量。令

\[
T=(-\cos\gamma\sin\beta,\cos\gamma\cos\beta,\sin\gamma),
\qquad T_0=(0,1,0),\quad T_\Delta=T-T_0.
\]

小相位时，第二分量不能先分别算两个接近1的量再相减。改用准确式

\[
(T_\Delta)_2=-2\sin^2(\gamma/2)-2\sin^2(\beta/2)
                  +4\sin^2(\gamma/2)\sin^2(\beta/2).
\tag{1}
\]

第一、三分量直接为 $-\cos\gamma\sin\beta,\sin\gamma$。
源在这些完整径向 jet 上应用同一有向 FFT、同一旋转原函数乘子和准确
奇偶投影。背景的原函数恰是 $(a,0,Z)$，在 FFT 之后准确加回；不再把
频率零的常量背景当作未知 Fourier 尾。

记

\[
F=(a,0,Z)+F_\Delta,\quad
X=F_r=(a',0,Z')+X_\Delta,\quad X_\Delta=(F_\Delta)_r.
\tag{2}
\]

$F_\Delta$ 仍是准确零均值笛卡尔原函数在旋转基的表达。
其竖直零模准确为零；旋转基的径向零模一般不为零，必须保留。
因此

\[
E=\langle|F_r|^2\rangle=a'^2+Z'^2+e,
\quad
e=2a'\langle(X_\Delta)_1\rangle+
                       \langle X_\Delta\cdot X_\Delta\rangle.
\tag{3}
\]

式 (3) 没有把 $E$ 的非径向部分丢掉，也没有假设 $Z'=a^2$。
当前保存的高度 slope 和 radius 必须各自按实际 scalar 数据求导。

## 3. 准确曲率及其一阶径向导数

同步目标仍是 $E(r)dr^2+a(r)^2d\theta^2$。
其曲率分子

\[
N=a'E'-2a''E
  =2Z'(a'Z''-a''Z')+a'e'-2a''e.
\tag{4}
\]

这里 $a'^2$ 的两项抵消发生在代数式层，不在区间运算之后。
进一步

\[
N'=2Z''(a'Z''-a''Z')
       +2Z'(a'Z'''-a'''Z')+a'e''-a''e'-2a'''e,
\tag{5}
\]

\[
K_0=\frac{N}{2aE^2},\qquad
K_0'=\frac{N'}{2aE^2}
          -K_0\left(\frac{a'}a+\frac{2E'}E\right).
\tag{6}
\]

设 $D_1=X_\Delta,D_2=(X_\Delta)_r,D_3=(X_\Delta)_{rr}$，
则源实际形成

\[
\begin{aligned}
e&=2a'\langle(D_1)_1\rangle+\langle D_1\cdot D_1\rangle,\\
e'&=2a''\langle(D_1)_1\rangle+2a'\langle(D_2)_1\rangle
                                  +2\langle D_1\cdot D_2\rangle,\\
e''&=2a'''\langle(D_1)_1\rangle+4a''\langle(D_2)_1\rangle
             +2a'\langle(D_3)_1\rangle
             +2\langle D_2\cdot D_2+D_1\cdot D_3\rangle.
\end{aligned}
\tag{7}
\]

Parseval 的每个点积使用 $k$ 与 $-k$，而非在复径向 germ 上误用复共轭。
真实实径向限制当然给通常的实能量。

## 4. 真无限尾随小相位一起缩小

在每个实际径向点外的复圆盘、以及较大 normalized 角带上，设

\[
|\beta|+|\gamma|\le P,\qquad |a|\le A.
\]

逐分量积分恒等式

\[
T(\beta,\gamma)-T(0,0)
       =\int_0^1\frac d{ds}T(s\beta,s\gamma)\,ds
\]

给 $|(T_\Delta)_j|\le P e^P$。所以冻结原函数 Fourier 预算中的乘子
可以取 $APe^P$。这同时支付高频截断与低频 alias；并非仅改小一个
被猜测的高模尾。准确背景只含零模，其原函数已准确加回。

源使用径向圆盘半径 $R_0=.003$、外角宽 $\sigma_0=.32$。
每个实际 scalar span 的完整多项式只在自己的圆盘上作解析延拓；原函数
在实际径向子区间上的值和 jet 与真实曲面相同。没有把跨 knot 的整体
$C^4$ 径向函数称为解析函数。

若 $F_\Delta$ 的逐分量真实尾上界为 $\varepsilon$，则

\[
\varepsilon_j=j!\varepsilon/R_0^j,\qquad j=1,2,3
\tag{8}
\]

支付 $D_j$ 的逐分量误差。令 $B_j$ 是有限 $D_j$ 每个分量的 Fourier
$\ell^1$ 上界，$A_j\ge|a^{(j)}|$，则 (7) 依次添加

\[
\begin{aligned}
\epsilon_e={}&2A_1\varepsilon_1
                    +3(2B_1\varepsilon_1+\varepsilon_1^2),\\
\epsilon_{e'}={}&2A_2\varepsilon_1+2A_1\varepsilon_2
        +6(B_1\varepsilon_2+B_2\varepsilon_1+
                                      \varepsilon_1\varepsilon_2),\\
\epsilon_{e''}={}&2A_3\varepsilon_1+4A_2\varepsilon_2+2A_1\varepsilon_3\\
&+6(2B_2\varepsilon_2+\varepsilon_2^2+B_1\varepsilon_3
                   +B_3\varepsilon_1+\varepsilon_1\varepsilon_3).
\end{aligned}
\tag{9}
\]

所有有限数值舍入已经由有向向量核包含。式 (9) 先加入，再形成 (4)–(6)。
保留旋转基径向零模是式 (9) 中前三组线性费用的来源；漏掉它们会得到
错误的误差界。

## 5. 实际正能量密度与角流

本引擎继续使用 R64 的同一 $Y_z>0$、同一全 $\ell$ 口径与 R37
固定型别材料算子。准确有

\[
Y_z^2\widehat A=
\begin{pmatrix}\alpha&\alpha b\\
\alpha b&\alpha b^2+\eta K_0\end{pmatrix}.
\]

每个闭子区间付 $K_0>0$、$F_z>0$、真实 area/support/radius 分母、
$\alpha,\eta>0$，并覆盖全部角间隙和一条明确复角带。
在固定正切口 $r_0$ 出发解真实角流
$\Theta_r=b(r,\Theta)$，径向坐标保持不变，新的完整正密度是

\[
\operatorname{diag}(J\alpha,\eta K_0/J).
\tag{10}
\]

这里两个端点都为普通端点，故边界 trace 为 $H^{1/2}\oplus H^{1/2}$。
不把这个域的左端 $r_0=1/4$ 改称转折，也不把右端 $3$ 改称固定开帽。

角流 Jacobian 预算按每个真实子区间分别积分：

\[
\log\max(J,J^{-1})\le
       \sum_I |I|\sup_{I\times S^1}|b_\theta|.
\tag{11}
\]

复角流用相同逐段和。这比把核心处的最大值乘整个 body 长度更直接，
但仍是同一个 Gronwall 不等式。归一密度的第二个特征值先在每个单元
形成 $\eta K_0$ 的上下界，再取全域最大最小，避免把不同位置的不相关
极值相乘所造成的额外膨胀。

## 6. 当前实际计算范围

先运行相同参数盒的两个检查区间：$[1/4,17/64]$ 和 $[299/100,3]$。
后一段的43个准确子区间已经全部通过，末端小半径并未导致曲率分母失证。
这些局部报告仍是全域引擎的诊断；在完整 $[1/4,3]$ 的准确覆盖和汇总
完成之前，不从它们推出整个外部为正。

后续即使有限 body 全部通过，也还需为同一对象构造 $r>3$ 的实际外延，
匹配完整两迹、mean、普通源和固定开 $H$ 的零二 jet。
旧 R22/R23 的线性第四模尾不由 (1)–(11) 自动迁移过来。
