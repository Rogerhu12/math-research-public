# R60 所用负积分常数的严格有理证书

日期：2026-11-12（UTC）。子任务：critical_kernel；与 literature 子任务协作。

**状态：已完成的标量积分子引理。** 对下述明确参数，证明
$$
\boxed{
J\le-\frac{51746665241}{375000000000}
<-\frac{13}{100}<0.
}
\tag{0.1}
$$
证明由解析插值误差及 41 个经 Arb/Acb 严格区间运算验证的有理界组成。没有将普通浮点结果的负号当成证明。此笔记只负责常数证书；它在原临界核证明中的用途由 R60 正文处理。

复现脚本：[2026-11-12-critical-negative-integral-certificate-0c.py](2026-11-12-critical-negative-integral-certificate-0c.py)。

## 1. 积分、概率测度与参数化

令
$$
P(q)=1-q+\frac{q^2}{2}
=\frac{1+(q-1)^2}{2}>0,
$$
$$
h(u)=\frac12\int_1^\infty
\log P\!\left(\frac{u}{x^2}\right)\,dx
\qquad(1\le u\le20),
$$
$$
g=\log\frac{\sqrt{20}+1}{\sqrt{20}-1},
$$
$$
J=g+\frac{\sqrt{20}}{\pi}
\int_1^{20}\frac{h(u)}{u\sqrt{(u-1)(20-u)}}\,du.
\tag{1.1}
$$
积分在两个端点的平方根奇性可积。定义
$$
d\nu(u)=
\frac{\sqrt{20}}{\pi u\sqrt{(u-1)(20-u)}}\,du.
$$
作代换
$$
u(\theta)=\frac{20}{20\cos^2\theta+\sin^2\theta},
\qquad0\le\theta\le\frac\pi2.
\tag{1.2}
$$
直接微分（或先令 $t=\tan\theta$）得到
$$
d\nu(u)=\frac2\pi\,d\theta.
$$
故 $\nu$ 是 $[1,20]$ 上概率测度，而且
$$
J=g+\int h\,d\nu
=g+\frac2\pi\int_0^{\pi/2}h(u(\theta))\,d\theta.
\tag{1.3}
$$

## 2. 无穷积分的可微性及统一插值误差

$P(q)\ge1/2$，在固定 $u\in[1,20]$ 上，原积分的尾为 $O(x^{-2})$，故 $h$ 有限。关于 $u$ 的一、二阶导数可分别用常数倍的 $x^{-2}$、$x^{-4}$ 控制，所以可在积分号下两次求导。

写 $q=u/x^2$。有
$$
h''(u)=
\int_1^\infty
\frac{1-(q-1)^2}
{x^4(1+(q-1)^2)^2}\,dx.
\tag{2.1}
$$
因为
$$
\left|
\frac{1-s^2}{(1+s^2)^2}
\right|\le1\qquad(s\in\mathbb R),
$$
得到
$$
\boxed{|h''(u)|\le\int_1^\infty x^{-4}\,dx=\frac13.}
\tag{2.2}
$$

在每个单位区间 $[i,i+1]$（$i=1,\ldots,19$），令 $\ell$ 为连接 $h(i)$ 与 $h(i+1)$ 的直线。则
$$
h(u)\le
\ell(u)+\frac16(u-i)(i+1-u)
\le \ell(u)+\frac1{24}.
\tag{2.3}
$$
一个自含证明是考虑
$$
v(u)=\ell(u)+\frac16(u-i)(i+1-u)-h(u).
$$
它在两个端点为零，且由 $h''\ge-1/3$ 有 $v''=-1/3-h''\le0$。凹函数不小于端点连线，所以 $v\ge0$。

对概率测度 $\nu$ 积分，得到关键上界
$$
\boxed{
J\le g+\int_1^{20}\ell(u)\,d\nu(u)+\frac1{24}.
}
\tag{2.4}
$$
这里 $\ell$ 是 19 段线性插值函数。误差项是整个积分的 $1/24$，不是每段相加 19 次的误差。

## 3. 精确计算插值积分的权重

定义累积质量和累积第一矩
$$
F(u)=\nu([1,u]),\qquad
M(u)=\int_1^u t\,d\nu(t).
$$
由 (1.2) 得
$$
F(u)=\frac2\pi
\arctan\sqrt{\frac{20(u-1)}{20-u}}
\quad(1<u<20),
\tag{3.1}
$$
$$
M(u)=\frac{2\sqrt{20}}{\pi}
\arcsin\sqrt{\frac{u-1}{19}}.
\tag{3.2}
$$
连续端点值为
$$
F(1)=M(1)=0,\qquad F(20)=1,\qquad M(20)=\sqrt{20}.
$$

对 $i=1,\ldots,19$，写
$$
\mu_i=F(i+1)-F(i),\qquad
m_i=M(i+1)-M(i),
$$
$$
L_i=(i+1)\mu_i-m_i,\qquad
R_i=m_i-i\mu_i.
\tag{3.3}
$$
这两个数分别是非负函数 $i+1-u$ 和 $u-i$ 在该段上的积分，实际上严格正。因此
$$
\int_i^{i+1}\ell\,d\nu=L_i h(i)+R_i h(i+1).
\tag{3.4}
$$
合并相邻段，定义
$$
\omega_1=L_1,\quad
\omega_i=R_{i-1}+L_i\ (2\le i\le19),\quad
\omega_{20}=R_{19}.
$$
它们是分段线性帽函数的积分，满足 $\omega_i>0$、$\sum_i\omega_i=1$，并且
$$
\int_1^{20}\ell\,d\nu
=\sum_{i=1}^{20}\omega_i h(i).
\tag{3.5}
$$

## 4. 端点 $h(i)$ 的闭式与分支

令
$$
\alpha=\frac{1+\mathrm i}{2},\qquad z=\alpha u.
$$
因为
$$
P(u/x^2)=\left|1-\frac z{x^2}\right|^2,
$$
有
$$
h(u)=\operatorname{Re}\int_1^\infty
\operatorname{Log}\left(1-\frac z{x^2}\right)\,dx.
$$
此处使用主值对数。$z$ 严格位于上半平面，故 $1-z/x^2$ 始终位于下半平面，没有穿过主值对数的割线。

令 $s=\sqrt z$ 为第一象限的主值平方根。直接求导验证
$$
\frac{d}{dx}
\left[
x\operatorname{Log}\left(1-\frac z{x^2}\right)
+2s\,\operatorname{atanh}(s/x)
\right]
=
\operatorname{Log}\left(1-\frac z{x^2}\right).
$$
$s/x$ 始终严格位于上半平面，也不穿过 $\operatorname{atanh}$ 的实轴割线。方括号在 $x\to\infty$ 时趋零，因此
$$
\boxed{
h(u)=\operatorname{Re}\left[
-\operatorname{Log}(1-\alpha u)
-2\sqrt{\alpha u}\,
 \operatorname{atanh}\sqrt{\alpha u}
\right].
}
\tag{4.1}
$$
脚本只在 $u=1,\ldots,20$ 上评价这些有限个闭式，不进行未经界定误差的无穷数值积分。

## 5. 可逐项核对的有理表

设尺度 $S=10^6$。下表的整数 $H_i,W_i$ 满足
$$
h(i)<H_i/S<0,\qquad
0<W_i/S<\omega_i.
\tag{5.1}
$$
另有
$$
g<454900/S.
\tag{5.2}
$$
这些 41 个不等式由 §6 脚本使用严格球区间验证；所有输入均为整数或精确有理数。

| $i$ | $H_i$：$h(i)$ 的上界分子 | $W_i$：$\omega_i$ 的下界分子 |
|---:|---:|---:|
| 1 | -472908 | 374494 |
| 2 | -770203 | 206910 |
| 3 | -895043 | 85429 |
| 4 | -936462 | 52567 |
| 5 | -936594 | 37253 |
| 6 | -913840 | 28606 |
| 7 | -877308 | 23166 |
| 8 | -832002 | 19501 |
| 9 | -780896 | 16918 |
| 10 | -725863 | 15045 |
| 11 | -668138 | 13671 |
| 12 | -608563 | 12670 |
| 13 | -547730 | 11969 |
| 14 | -486062 | 11534 |
| 15 | -423871 | 11368 |
| 16 | -361384 | 11523 |
| 17 | -298776 | 12155 |
| 18 | -236176 | 13754 |
| 19 | -173683 | 19342 |
| 20 | -111374 | 22113 |

每个 $H_i<0$，所以将正权重替换成下界，方向为上界：
$$
\omega_i h(i)
\le \omega_i\frac{H_i}{S}
\le \frac{W_iH_i}{S^2}.
\tag{5.3}
$$
这解释了为何表中需要权重的**下界**。$\sum_iW_i/S=0.999988$ 而非 $1$ 不造成漏项；(5.3) 是对每项独立成立的上界。

现在完全使用整数算术：
$$
\frac{454900}{10^6}
+\sum_{i=1}^{20}\frac{W_iH_i}{10^{12}}
=-\frac{179657773976}{10^{12}}.
$$
结合 (2.4)，
$$
\begin{aligned}
J
&\le-\frac{179657773976}{10^{12}}+\frac1{24}\\
&=-\frac{51746665241}{375000000000}\\
&<-\frac{13}{100},
\end{aligned}
\tag{5.4}
$$
最后一步的正余量为
$$
-\frac{13}{100}
+\frac{51746665241}{375000000000}
=\frac{2996665241}{375000000000}>0.
$$
这给出 (0.1)。

## 6. 严格区间验证、运行环境和复现

运行命令（从仓库根目录）：

    python topics/invariant-subspace-problem/notes/2026-11-12-critical-negative-integral-certificate-0c.py

本轮运行环境为：

- Python 包 python-flint 0.9.0；
- 其链接的 FLINT 3.6.0；
- 工作精度 ctx.prec = 256 位；
- 输入仅用整数及 fmpq 精确有理数，没有 Python float 或内置复浮点输入。

arb/acb 的输出是包含精确值的球区间；比较返回真要求整个输入区间满足比较，不是比较中点。这两个语义见 python-flint 的官方 [General concepts — Inexact numbers and numerical evaluation](https://python-flint.readthedocs.io/en/latest/general.html#inexact-numbers-and-numerical-evaluation)。本轮于 2026-11-12 查读该文档，并核对了 arb/acb 的公开接口。

脚本逐个断言 h(i) 的球上端小于表中精确有理上界，以及权重球下端大于表中精确有理下界；再断言加入解析误差后的整个球上端小于 $-13/100$。另外，脚本用 Python Fraction 独立验证 (5.4) 的最终有理算术。

本轮实际输出的主要区间为
$$
g+\int\ell\,d\nu
\in
[-0.1796662212736663944407822834938549352536814471563416170753302559679238919
\ \pm 3.16\times10^{-74}],
$$
$$
g+\int\ell\,d\nu+\frac1{24}
\in
[-0.1379995546069997277741156168271882685870147804896749504086635893012572252
\ \pm 5.03\times10^{-74}].
$$
最终结论依赖脚本中的严格有理比较和 §2 的解析误差，不依赖这些小数的视觉符号。表中较粗的六位有理数已足以留出近 $0.008$ 的负号余量。

## 7. 使用边界

本证书严格证明参数 $a=1,b=20$ 的标量常数 $J<-13/100$。它既不自动验证任何算子估计，也不承担从模型近似传回实际进位算子的误差；这些是 R60 主证明中的独立论证。把本证书用于别的区间端点或别的 $P$ 时，需要重新核算。

