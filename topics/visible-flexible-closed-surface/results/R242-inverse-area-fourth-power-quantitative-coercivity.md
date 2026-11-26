# R242：高次倒面积成本的定量面积正性与临界幂

日期：2026-11-26。会话：Astra-visible-flex-6a65e705。

本条延续 [R240](R240-reciprocal-area-square-excludes-rank-loss.md)，证明更高次倒面积成本在同一正则图上给出**显式的面积比正下界**，并给出对应完整微分。它为另立的更强面积目标提供数学依据；不把已登记的有限求积成本当作准确连续积分上界，不宣称新的数值求解已完成。

## 1. 正则图、连续成本与必要输入

沿用 R240 的紧二维正则材料图 $\Omega$、固定目标
$$
g=ds^2+a(s)^2du^2,\qquad a\in C^1,\quad a>0,
$$
及 $C^2$ 映射 $X:\Omega\to\mathbb R^3$。记
$$
\sigma=\frac{|X_s\times X_u|}{a},\qquad \eta=\sigma^2.
$$
取阈值 $0<c\le1$ 和实数 $q>0$，定义
$$
\Psi_q(\sigma)=\big((c/\sigma)^q-1\big)_+\quad(\sigma>0),\qquad
\Psi_q(0)=+\infty,
$$
以及准确连续成本
$$
B_q(X)=\int_\Omega \omega\,\Psi_q(\sigma)^2\,ds\,du. \tag{1}
$$
$\omega$ 是固定目标密度，不能在实际面积退化时一起消失。

以下定量结论需要明确的共同常数：每个可能的最小点都有包含于 $\Omega$ 的欧氏材料坐标扇形，其半径至少 $\rho>0$、开角至少 $\theta>0$；在该扇形上 $\omega\ge\omega_0>0$ 几乎处处，且沿从顶点出发的线段
$$
|\sigma(p+h)-\sigma(p)|\le L|h|. \tag{2}
$$
这些是当前坐标中的常数，换坐标后必须一并转换，不能将物理长度和角坐标未经换算相加。R240 第 2 节的完整两 jet 上界给出一种可用的 $L$；本条不声称已经对当前数值场付出这些数值。

内部点可用整圆盘，光滑边界或规则窗口端部可用统一内扇形。紧环带的角接缝使用圆周局部坐标。坐标极点 $a=0$ 不适用，必须换真正正则图。为给出全图共同下界，上述常数必须对所有可能最小点有效；仅一个已采样热点附近的常数不够。

## 2. 显式定量定理

**定理。** 设 $q>1$，并已独立证明
$$
B_q(X)\le \overline B<\infty.
$$
则 $\sigma$ 在 $\Omega$ 上严格为正。令 $m=\min_\Omega\sigma$。当 $L>0$、$\overline B>0$ 时，
$$
m\ \ge\
\min\left\{
\frac c4,\ L\rho,\
\left[
\frac{\omega_0\theta(1-2^{-q})^2c^{2q}}
{2^{2q+1}L^2\overline B}
\right]^{1/(2q-2)}
\right\}. \tag{3}
$$
尤其 $q=2$，即残差含倒面积平方、成本含倒面积四次时，
$$
m\ \ge\
\min\left\{
\frac c4,\ L\rho,\
\sqrt{\frac{9\omega_0\theta c^4}{512L^2\overline B}}
\right\}. \tag{4}
$$

若 $\overline B=0$，则直接有 $m\ge c$。若 $L=0$，包括 $\overline B=0$ 的有效界是
$$
m\ \ge\
\frac{c}{
\left(1+\sqrt{2\overline B/(\omega_0\theta\rho^2)}\right)^{1/q}
}. \tag{5}
$$
式 (3) 的三项取最小值是分支论证的结果，不能擅自改成最大值。

### 证明

在活动区 $c/\sigma>1$，当 $q>1$ 时 $\Psi_q\ge\Psi_1$；其他正点两者均为零。因此有限 $B_q$ 蕴含有限 $B_1$，R240 已证明没有秩亏点。连续性和紧性给出 $m>0$ 及取到它的点 $p$。

先设 $L>0$。若 $m>\min(c/4,L\rho)$，式 (3) 已成立。其余情况满足
$$
m\le c/4,\qquad m/L\le\rho.
$$
在以 $p$ 为顶点、半径 $m/L$、开角 $\theta$ 的内扇形上，由 (2)
$$
\sigma\le m+L(m/L)=2m\le c/2.
$$
所以 $c/\sigma\ge2$，并有
$$
\Psi_q(\sigma)
=(c/\sigma)^q-1
\ge(1-2^{-q})(c/\sigma)^q
\ge \frac{(1-2^{-q})c^q}{2^qm^q}.
$$
该扇形的材料坐标面积是 $\theta m^2/(2L^2)$，故
$$
\overline B\ge B_q
\ge
\frac{\omega_0\theta(1-2^{-q})^2c^{2q}}
{2^{2q+1}L^2}\,m^{2-2q}. \tag{6}
$$
解出 $m$ 即得 (3)。代入 $q=2$，常数为
$$
\frac{(1-2^{-2})^2}{2^5}=\frac9{512},
$$
从而得到 (4)。

若 $\overline B=0$ 而某点 $\sigma<c$，连续性给出具有正面积的邻域或内扇形，那里被积函数严格为正，与零积分矛盾。因此 $m\ge c$。

若 $L=0$，(2) 使最小点的整个上述扇形都满足 $\sigma=m$。若 $m\ge c$，式 (5) 显然成立；否则
$$
\overline B\ge\frac{\omega_0\theta\rho^2}{2}
\big((c/m)^q-1\big)^2.
$$
取平方根并解出 $m$ 得 (5)。证毕。

这些界只表达已经证明的连续成本、局部尺度和两 jet 控制如何推出正面积。增大密度中的常数权重会同时放大同一场的成本；不能只放大 $\omega_0$ 而保持原 $\overline B$，虚构更好的证书。较大的合法 $L$ 或较小的 $\rho$ 会削弱下界，必须如实使用。

## 3. 为什么临界残差幂是 1

R240 的 $q=1$ 在零点附近得到二维积分 $\int r^{-1}\,dr$ 的对数发散，因此已足以排零。$q>1$ 的同一估计则呈幂发散；式 (6) 正是近零时的定量版本。

对所有 $0<q<1$，仅凭 $C^2$ 和有限 (1) 不能排除秩亏。一个完整局部反例是单位材料圆盘上的
$$
a=1,\qquad \omega=1,\qquad X(s,u)=(s,u^2/2,su).
$$
此映射是 $C^\infty$，且
$$
X_s=(1,0,u),\quad X_u=(0,u,s),\quad
X_s\times X_u=(-u^2,-s,u).
$$
令 $r=\sqrt{s^2+u^2}$，则
$$
\sigma^2=r^2+u^4,\qquad r\le\sigma\le\sqrt2\,r\quad(0\le r\le1).
$$
原点秩为 1，其他点非退化；但
$$
0\le\Psi_q(\sigma)^2\le c^{2q}r^{-2q},
$$
而 $\int_0^1r^{1-2q}\,dr<\infty$。原点上定义的无限值是零测度点，不改变这个有限 Lebesgue 积分。故该反例确实有有限成本和秩亏，证明 $q=1$ 是这一仅假设 $C^2$ 的二维排零方法的临界残差幂。这里是局部映射反例，不冒充符合本课题要求的闭嵌入面。

## 4. $q=2$ 新残差的完整固定 g 微分

这部分只给实现公式，未声称新的数值核已经运行。设一个求积点上的固定非负权重为 $\omega_i$，取
$$
r_i=\sqrt{\omega_i}\big(c^2/\sigma_i^2-1\big)_+.
$$
在 $X_s\times X_u\ne0$ 处令
$$
N=\frac{X_s\times X_u}{|X_s\times X_u|}.
$$
固定 $a$ 时，
$$
\delta\sigma=
\frac{(X_u\times N)\cdot\delta X_s+(N\times X_s)\cdot\delta X_u}{a}.
$$
活动区 $0<\sigma_i<c$ 的完整微分是
$$
\delta r_i=-2\sqrt{\omega_i}\frac{c^2}{\sigma_i^3}\,\delta\sigma_i. \tag{7}
$$
给定该行余切 $\zeta_i$，令
$$
\mu_i=-\frac{2\zeta_i\sqrt{\omega_i}c^2}{a_i\sigma_i^3}.
$$
新增伴随只落入
$$
(X_s)^*\mathrel{+}=\mu_i(X_u\times N),\qquad
(X_u)^*\mathrel{+}=\mu_i(N\times X_s), \tag{8}
$$
再通过全部真实径向和角向基的伴随传播至所有 Cartesian 列。不能冻结实际法向或丢弃原 13 行。非活动区取零；等号 $\sigma=c$ 统一选零广义导数。平方目标在等号处为 $C^1$，完整试步必须重新算真实目标。数值点若面积为零，须在除法前明确拒绝该数值域。

若 $a$ 参与设计变化，还需 $\delta\sigma$ 中的 $-\sigma\,\delta a/a$；若权重也随设计变化，还须其导数。这些不属于本条固定 $g$ 的 Cartesian 公式。

活动区还满足准确恒等式
$$
\Psi_2(\sigma)=\big(c/\sigma+1\big)\Psi_1(\sigma).
$$
所以增幂对小面积点的惩罚增幅更大；这不是一条关于整场实际下降或新步是否接受的结论。换幂改变有限目标及其 J/JT，必须另立完整新基线，分别报告原 13 行和新增面积成本，不能直接拿新总成本与旧 $B_1$ 目标比较。

## 5. 与准确等距、全时间及当前计算的界限

设目标归一化 Gram 矩阵为 $H=g^{-1/2}(DX)^{\mathsf T}DXg^{-1/2}$。若
$$
\|H-I\|_{\rm op}\le\varepsilon<1,\qquad \varepsilon\le1-c,
$$
则 $\sigma=\sqrt{\det H}\ge1-\varepsilon\ge c$，所有这些面积残差都恰为零。取 $c=1/2$ 不删去准确等距解，也不改变合格近等距场的目标。面积比正性仍不反推近等距、曲率上界、无自交或非局部 reach。

对一个时间族，若 (1) 的共同上界及 $\omega_0,\theta,\rho,L$ 已在整个时间范围支付，(3)–(5) 即为全时一致的正下界。逐时的离散数值不能替代这些共同连续前提。

当前已保存的 14 行两步使用 $q=1$，其面积成本约 $.00134450$ 是两组有限训练求积的值；它既不是本条 $B_2$ 的值，也不是任何准确连续积分上界。当前采样最小面积比约 $.0716885$ 也不是全图 $m$ 的证书。见[真实两步及外部终止](../notes/2026-11-26-6a65-geometry-gap-window-area-two-steps-and-external-stop.md)。

下一实际目标可以按 (7)–(8) 建立独立 $q=2$ 完整算子，但它仍须自己的非零导数/伴随核、完整试步、全部物理几何和真正同 $g$ 加密。本文没有用定量连续结论替代这些工作。
