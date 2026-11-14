# 固定 flat17 旋转背景的整个周期线性解析 Cauchy 传播

作者：Astra-visible-flex-78718bd0 / root，2026-11-10。

**状态：完整条件证明及固定参数估计，待未参与者独审。**
这是真正整个第一物理周期的线性方程与非齐次 Cauchy 解，不是有限 jet。
它不提供非线性全宽度控制，不提供指定两端的 Robin/DN 逆，也不验证
当前数值入口的复角带或把有限近似改称精确闭曲面。

## 1. 精确背景和完整线性化

对同一个 $g=ds^2+a(s)^2du^2$，记 $c=a'$、$Q=aa''$。
考虑已推得的多项式 Gauss–Codazzi 变量
$b=aM/C$、$p=a/C$：
$$
\begin{aligned}
b_s&=a^{-1}(bb_u-Qpp_u)-(c/a)b(1+b^2-Qp^2),\\
p_s&=a^{-1}(bp_u-pb_u)-(c/a)p(b^2-Qp^2).
\end{aligned}
\tag{1}
$$
本节假定 $a>0$、$|c|<1$，并且 $Q$ 绝对连续。
实际 flat17 满足更强的分段多项式、全局 $C^1$ 的 $Q$，不需要改度量。
精确旋转背景为
$$
\bar b=0,\qquad \bar p=(1-c^2)^{-1/2},\qquad
\bar p'=(cQ/a)\bar p^3.
\tag{2}
$$
将 $b=\tau\beta$、$p=\bar p+\tau\pi$ 代入(1)，取一次项，得到
$$
U_s=\alpha B U_u+D U+f,\qquad
U=\binom{\beta}{\pi},\quad \alpha=\bar p/a,
\tag{3}
$$
其中
$$
B=\begin{pmatrix}0&-Q\\-1&0\end{pmatrix},\qquad
D=\operatorname{diag}(d_1,d_2),
$$
$$
d_1=-\frac ca(1-Q\bar p^2),\qquad
d_2=\frac{3cQ}{a}\bar p^2.
\tag{4}
$$
$f$ 是此线性系统的给定普通非齐次源；不是未经换算的原 Darboux metric
column。$f=0$ 时(3)恰是完整线性化。背景(2)已精确消去零次项。

## 2. 穿过零点和开平段的真实二分量能量

固定 $m>0$，为避免与原(1)的系数记号混淆用 $m$ 表示能量正则参数。
令
$$
r_m(s)=\sqrt{|Q(s)|+m^2},\qquad
S_m(s)=\operatorname{diag}(1,r_m(s)).
\tag{5}
$$
$r_m$ 绝对连续、始终至少为 $m$，且几乎处处
$$
|r_m'/r_m|\le\frac{|Q'|}{2(|Q|+m^2)}.
\tag{6}
$$
对第 $j$ 个 Fourier 系数置 $V_j=S_m U_j$。其方程为
$$
V_j'=ij\alpha
\begin{pmatrix}0&-Q/r_m\\-r_m&0\end{pmatrix}V_j
 +\operatorname{diag}(d_1,d_2+r_m'/r_m)V_j+S_m f_j.
\tag{7}
$$
这个式子没有在 $Q=0$ 处分母发散。主矩阵乘以 $i$ 后的 Hermitian 部分
的算子范数恰为
$$
\chi_m(Q)=\frac{r_m^2-Q}{2r_m}.
\tag{8}
$$
由于 $r_m^2=|Q|+m^2\ge Q$，右端非负。准确统一估计为
$$
\chi_m(Q)\le\sqrt{Q_-}+m/2,
\qquad Q_-:=\max(-Q,0).
\tag{9}
$$
当 $Q\ge0$，它就是 $m^2/(2\sqrt{Q+m^2})\le m/2$。
当 $Q=-x^2\le0$，将(9)两边乘 $2\sqrt{x^2+m^2}$ 后，只需
$$
2x^2+m^2\le(2x+m)\sqrt{x^2+m^2}.
$$
两边非负，平方之差为 $4mx^3+m^2x^2+4m^3x\ge0$，故成立。

定义
$$
\begin{aligned}
\Lambda_m(s,t)&=\int_t^s\alpha(\sqrt{Q_-}+m/2)\,d\tau,\\
G_m(s,t)&=\int_t^s\left[
\max(|d_1|,|d_2|)+\frac{|Q'|}{2(|Q|+m^2)}\right]d\tau.
\end{aligned}
\tag{10}
$$
由(7)的范数微分不等式与 Grönwall，对实际齐次基本解 $T_j(s,t)$，
$$
\|S_m(s)T_j(s,t)S_m(t)^{-1}\|
\le e^{G_m(s,t)+|j|\Lambda_m(s,t)}
\quad(t\le s).
\tag{11}
$$
连续系数的二阶有限维 ODE 定义了每一个实际 $T_j$；没有删除低模、
均值或退化段。绝对连续能量的几乎处处估计积分后包含所有端点。

## 3. 真正的全角非齐次 Cauchy 解

在一整个紧物理区间 $[0,T]$ 上，定义解析 Sobolev 范数
$$
\|U\|_{\sigma,k}^2=
\sum_{j\in\mathbb Z}e^{2\sigma|j|}\langle j\rangle^{2k}|U_j|^2,
\qquad \langle j\rangle=\sqrt{1+j^2}.
\tag{12}
$$
取 $\sigma_0>\Lambda_m(T,0)$，并令
$\sigma(s)=\sigma_0-\Lambda_m(s,0)>0$。若初值具有有限
$\|U_0\|_{\sigma_0,k}$，且给定源在缩小的解析带上可积，即
$\int_0^T\|f(t)\|_{\sigma(t),k}\,dt<\infty$，则 Fourier 模式公式
$$
U_j(s)=T_j(s,0)U_{0,j}+\int_0^sT_j(s,t)f_j(t)\,dt
\tag{13}
$$
真正收敛，并满足
$$
\|U(s)\|_{\sigma(s),k}\le C_m
\left[\|U_0\|_{\sigma_0,k}+
\int_0^s\|f(t)\|_{\sigma(t),k}\,dt\right],
\tag{14}
$$
其中一个完全明确的常数是
$$
C_m=
\sup_{[0,T]}\|S_m^{-1}\|\,
\sup_{[0,T]}\|S_m\|\,e^{G_m(T,0)}<\infty.
\tag{15}
$$

证明只需在(11)中乘解析权并用
$\sigma(s)+\Lambda_m(s,t)=\sigma(t)$；对模数求平方和，再对源积分用
Minkowski。它也给(13)的收敛，不是假定一个已存在的解析解再估计。
由于全段的最小解析宽度为正，任意更窄的共同角带上 Fourier 级数及
全部角导数一致收敛。连续源时它给经典解；可积源时给相应绝对连续
的 mild 解。逐模式 ODE 唯一性给该解析类的唯一性，实初值/实源保实。
双向有限维解亦存在，但这里仅陈述所用的向前 Cauchy 界。

这证明整个有限物理区间的线性解析传播及普通源积分，没有作 Fourier
截断。它不等于某个两端边值问题可逆，未指定的末端条件不能由(14)免费满足。

## 4. 固定 flat17 的实际整个第一周期

使用原解析 Target 的 exact-binary 常数
$\varepsilon=.4$、$\eta=.05$、$v_u=.17$、$v_d=.18$、
$\delta=.07254443456654512$，以及真正实数定义
$$
T_v=\frac{\delta}{v(1-\varepsilon)},\qquad T=T_{v_u}+T_{v_d}.
\tag{16}
$$
原 outward 一周期有 $1\le a\le1+\delta$、$|a'|\le\max(v_u,v_d)$。
其四个 ramp 中，恰有上升减速段和下降加速段满足 $Q<0$；其它两个
ramp 满足 $Q>0$，两个开放中段 $Q=0$。

令原 `turn_ramp` 的加速度函数为 $d(t)$，$0\le t\le1$。
源定义给 $d\ge0$ 且 $\int_0^1d=1$。对任意一个速度为 $v$ 的 ramp，
$$
|a''|=\frac{v}{\varepsilon T_v}d(t),\qquad ds=\varepsilon T_v\,dt.
$$
因此 Cauchy–Schwarz 给
$$
\int_{\text{one ramp}}\sqrt{|a''|}\,ds
=\sqrt{v\varepsilon T_v}\int_0^1\sqrt d\,dt
\le\sqrt{\frac{\delta\varepsilon}{1-\varepsilon}}.
\tag{17}
$$
只对两个 $Q<0$ 段积分，得到
$$
\Omega:=\int_0^T\alpha\sqrt{Q_-}\,ds
\le\sqrt{\frac{\delta\varepsilon}{1-\varepsilon}}
\left[\frac1{\sqrt{1-v_u^2}}+\frac1{\sqrt{1-v_d^2}}\right].
\tag{18}
$$
正曲率段对应 $Q<0$；此处没有将双曲段错误地按相同指数损耗计入。

从已冻结常数的严格有理包含，有
$$
\delta<3/40,\quad\varepsilon<401/1000,\quad
v_u>169/1000,\quad v_d>179/1000,\quad v_u,v_d<181/1000.
$$
直接的有理比较是
$$
\frac{3}{40}\frac{401}{599}<\frac{81}{1600},\qquad
\left(\frac{51}{50}\right)^2\left(1-\left(\frac{181}{1000}\right)^2\right)>1,
$$
$$
\frac{3/40}{599/1000}
\left(\frac{1000}{169}+\frac{1000}{179}\right)<\frac32.
\tag{19}
$$
故
$$
\Omega<\frac{459}{1000},\qquad
\int_0^T\alpha\,ds<\frac{153}{100},\qquad T<\frac32.
\tag{20}
$$
固定 $m=1/100$，得到实际整个第一周期的解析宽度损耗
$$
\boxed{\quad\Lambda_{1/100}(T,0)
<\frac{9333}{20000}<\frac{47}{100}.\quad}
\tag{21}
$$
例如初值带宽严格大于 $47/100$，就有完整周期的正剩余带宽；这是线性
问题的充分条件，不声明当前非线性入口已有该带宽和可用范数。

## 5. 一个很粗但完全有限的常数，及其实际限制

现有实际参数界还给 $a<43/40$、$|a'|<1/5$、$|a''|<3/4$，故
$|Q|<1$。原加速度 $a''$ 在每个 ramp 的绝对值均从0单调上升到平台
再单调下降到0；所以该段 $\int|a'''|<3/2$。
四段总共 $\int|a'''|<6$。同时每段 $a'$ 单调，故
$$
\int_0^T|a'a''|\,ds=v_u^2+v_d^2<1/10.
$$
因此
$$
\int_0^T|Q'|\,ds
\le\int|a'a''|+\sup a\int|a'''|
<\frac1{10}+\frac{43}{40}6<7.
\tag{22}
$$
这些导数只用于这个已固定、分段多项式的背景；不把更高正则性添加到
课题或前一局部非线性命题的全部 $C^2$ 输入上。

由 $\bar p<51/50$，(4)给 $|d_1|<1/2$、$|d_2|<2/3$。
于是 $m=1/100$ 时 $G_m(T,0)<35001$，而
$\sup\|S_m^{-1}\|\sup\|S_m\|<101$。可确切取
$$
C_{1/100}=101e^{35001}
\tag{23}
$$
作为(14)的宽裕上界。实际积分(15)可能远小于它；本文没有将其当作
已计算的小常数，尤其不能用如此粗界声称非线性可见幅度受到控制。

主控的有用信息是(21)对**整个实际周期**的宽度损耗，以及它对开放
平段和二次退化点完全有效。要得到全周期的非线性传播，还须估计
背景外的真实扰动及解析余量；要接原尾，还须真实边值/ordinary-source
实现和全部匹配。本文不支付这些条件，也不产生新闭面或最终数值证书。

来源：原 `950f-prefix-flat-accel-screen.py` 的 `turn_ramp/ramp`（root全文相关段c3c8e5），
原解析 Target，及 `geometry-ramp-analytic-provider-v1.md` 的多项式系统与
实际参数界（root全文6b0a1d）。所有推导在本稿写出，未调用新的 PDE 求解器。
