# R133 补篇：实际正帽的一阶目标 jets，先消去半径幂再微分

**状态：已证明。** 本篇给同一实际目标在一个真实闭标量 germ 内的稳定一阶
系数公式、完整 primitive 余项和原生三盒计算。它只证明所列系数包络；尚不
给新的 nonlinear cap 存在区间、全 body 匹配或闭曲面。

## 1. 同一对象与需要消去的项

目标及 whole-parameter 身份完全沿用
[R133 实际旋转帽](R133-actual-rotational-positive-cap-and-Codazzi-Jacobi-graph.md)：

$$
g_0=E(r)\,dr^2+a(r)^2\,d\theta^2,
\qquad E=\langle |F_r|^2\rangle,
\tag{J.1}
$$

其中 $F$ 为原完整无限 primitive 对象，参数中心
$-7789843107295549/4611686018427387904$，$|\eta|\le10^{-9}$。
本篇只在原 body 的实际 scalar germ 内工作；不把 body 公式外插入 natural
graft。紧支撑控制 $E_\nu=E\exp(\nu h)$ 在 $r\ge.18$ 恒等于本目标，故在
本篇的正帽域没有更换目标，但这不转授任何原腰分支的证书。

直接微分
$K=-a''/(aE)+a'E'/(2aE^2)$ 在小 $a$ 时会分别包络两个很大的相消项。
这种包络仍正确，却可能完全不适合残差验证。以下恒等式先在精确代数中
消去这些半径幂，再形成每个有向数值包络。

## 2. 完整 primitive 与稳定标量

在旋转笛卡尔基底写原位置为

$$
F=a(e_r+P)+z e_z,
\qquad L=\frac{a'}a,
\qquad H=\frac{z'}{a^2},
\qquad u=LP+P'.
\tag{J.2}
$$

原 primitive 的垂直均值恒为零。以 $u_{0,x}$ 表示水平径向分量的零 Fourier
系数，则

$$
e=2L u_{0,x}+\langle u\cdot u\rangle,
\qquad \bar E=\frac E{a^2}=L^2+a^2H^2+e,
\qquad R=\frac{E-a'^2}{a^4}=H^2+\frac e{a^2}.
\tag{J.3}
$$

这里均值中的积是在真实角圆周上的积，不是有限节点的替代定义；有限 Fourier
零卷积及无限余项将在第 5 节共同包围它。

由 (J.3) 直接微分，得

$$
\bar E'=2LL'+2a^2LH^2+2a^2HH'+e',
\qquad
R'=2HH'+\frac{e'-2Le}{a^2}.
\tag{J.4}
$$

将 (J.1) 的曲率公式代入 $E=a^2\bar E$，得到精确分子

$$
\begin{aligned}
N&=H^2(L^2-L')+LHH'
       +\frac{Le'-2L'e}{2a^2},\\
K&=\frac N{\bar E^2},
\qquad \ell=\frac{K}{C_{\rm ref}^2}
             =\frac N{\bar E R},
\qquad C_{\rm ref}=-\sqrt{\frac R{\bar E}}.
\end{aligned}
\tag{J.5}
$$

例如，原曲率分子的重写为
$a^{-2}[-L'\bar E+(L/2)\bar E']$；代入 (J.3)–(J.4) 后，$L'L^2$
两项先准确抵消，余下即 (J.5)。这说明新公式计算的是同一个 $K$。

## 3. 一阶 jets 的精确公式

对已经消减的分子微分，得

$$
\begin{aligned}
N'={}&2HH'(L^2-L')+H^2(2LL'-L'')\\
 &+L'HH'+L(H'^2+HH'')\\
 &+\frac{Le''-(L'+2L^2)e'+(4LL'-2L'')e}{2a^2}.
\end{aligned}
\tag{J.6}
$$

最后一行包括分母 $a^{-2}$ 的导数；不能只微分其分子。因而，在
$a,\bar E,R,N>0$ 的闭盒上，

$$
\begin{aligned}
\beta&=L,& \beta'&=L',\\
\gamma&=\sqrt{\bar E},&
\gamma'&=\frac{\bar E'}{2\gamma},\\
K'&=\frac{N'-2N\bar E'/\bar E}{\bar E^2},&
\ell'&=\frac{N'}{\bar E R}
       -\ell\left(\frac{\bar E'}{\bar E}+\frac{R'}R\right),\\
C_{m ref}'&=\beta(\ell-1)C_{m ref}.&&
\end{aligned}
\tag{J.7}
$$

最后一式是旋转参考的准确 Codazzi 恒等式；也可直接将 (J.3)–(J.5) 代入
$C_{m ref}'/C_{m ref}=(R'/R-\bar E'/\bar E)/2$ 验证。使用这条恒等式不
删除任何非旋转 primitive 对 $E$ 的贡献。

### 3.1 同 germ 的 $L''$、$H''$

在实际 scalar polynomial 中先形成

$$
N_L=aa''-a'^2,
\qquad N_H=az''-2a'z'.
\tag{J.8}
$$

于是

$$
L'=\frac{N_L}{a^2},\quad
L''=\frac{aN_L'-2a'N_L}{a^3},\qquad
H'=\frac{N_H}{a^3},\quad
H''=\frac{aN_H'-3a'N_H}{a^4}.
\tag{J.9}
$$

程序在真实 scalar 多项式的系数层完成 (J.8)–(J.9) 的乘法和相减，再作
区间 Horner 求值。它不把多个未消减的大函数值先各自取范围。全部系数仍
保留原 whole-$\eta$ 区间和算术包络。闭盒不能跨真实 scalar germ；在接缝
端点仅使用所属单侧多项式的闭包，不假定更高阶导数跨接缝相等。

## 4. $e''$ 的完整有限部分

由 (J.2)，

$$
u'=L'P+LP'+P'',\qquad
u''=L''P+2L'P'+LP''+P'''.
\tag{J.10}
$$

对 (J.3) 求导得到

$$
\begin{aligned}
e'={}&2L'u_{0,x}+2Lu'_{0,x}+2\langle u\cdot u'\rangle,\\
e''={}&2L''u_{0,x}+4L'u'_{0,x}+2Lu''_{0,x}\\
&+2\langle u'\cdot u'\rangle+2\langle u\cdot u''\rangle.
\end{aligned}
\tag{J.11}
$$

有限部分的每一个零卷积都通过所有有限 Fourier 系数与其反序系数求和。
两项二次导数 $2u'\cdot u'$ 和 $2u\cdot u''$ 均保留。

## 5. 完整无限 primitive 尾的费用

沿用 R133 provider 已证明的复径向 Cauchy 尾：若原 $A^0$ primitive
余项为 $\tau$、可用复径向半径为 $\rho$，则每一坐标有

$$
\|P^{(j)}-P_{\rm fin}^{(j)}\|_{A^0}
 \le\varepsilon_j=\frac{j!\tau}{\rho^j},\qquad 0\le j\le3.
\tag{J.12}
$$

设 $M_j$ 是 $u^{(j)}_{\rm fin}$ 各坐标完整有限 $A^0$ 范数的最大值，
$L_0=|L|,L_1=|L'|,L_2=|L''|$。令

$$
\begin{aligned}
U_0&=L_0\varepsilon_0+\varepsilon_1,\\
U_1&=L_1\varepsilon_0+L_0\varepsilon_1+\varepsilon_2,\\
U_2&=L_2\varepsilon_0+2L_1\varepsilon_1+L_0\varepsilon_2+\varepsilon_3.
\end{aligned}
\tag{J.13}
$$

则三个实均值误差分别被以下量包围：

$$
\begin{aligned}
\epsilon_e={}&2L_0U_0+3(2M_0U_0+U_0^2),\\
\epsilon_{e'}={}&2L_1U_0+2L_0U_1
 +6(M_0U_1+M_1U_0+U_0U_1),\\
\epsilon_{e''}={}&2L_2U_0+4L_1U_1+2L_0U_2\\
 &+6(2M_1U_1+U_1^2)
 +6(M_0U_2+M_2U_0+U_0U_2).
\end{aligned}
\tag{J.14}
$$

证明只用 $A^0$ 的乘法不等式以及三个坐标求和。例如
$2\langle u'\cdot u'\rangle$ 的误差不超过
$6(2M_1U_1+U_1^2)$；$2\langle u\cdot u''\rangle$ 给最后一项。
其余项为 (J.11) 的线性误差。因此，给有限实均值分别添加
$[-\epsilon_e,\epsilon_e]$、$[-\epsilon_{e'},\epsilon_{e'}]$、
$[-\epsilon_{e''},\epsilon_{e''}]$ 后，(J.3)–(J.7) 包围真实无限对象。

有限 Fourier FFT、有限零卷积、scalar polynomial 和正分母运算均通过既有
`CBox`/`Box` 的有向实/虚矩形算术完成；最终标量转为 Arb 实包络。转实前
核对虚部包含零，所有开方和相除前明确核对正性。故本篇没有以有限 FFT
替代无限 primitive，也没有靠相邻点重叠证明连续盒。

## 6. 原生执行的三个完整闭盒

实际程序为
[fourfold_codazzi_positive_cap_stable_jets.py](../scripts/fourfold_codazzi_positive_cap_stable_jets.py)，
报告为
[完整三盒 native](../notes/2026-11-13-R133-positive-cap-stable-jets-pilot-native.json.gz)。
全部使用 320-bit Arb、512 个 primitive 节点、原参数中心和整个
$|\eta|\le10^{-9}$ 区间，真实闭盒端点保存在报告的准确分数中。下表用外扩的
十进制数列出部分结果：

| 闭盒（端点以 native 的 dyadic 分数为准） | $\ell'$ 包络 | $K'$ 包络 | $e''$ 无限尾费用 |
|---|---|---|---|
| $[1,1.0025]$ | $[-2.141379,-1.358531]$ | $[-.412929,-.326254]$ | $<1.602\times10^{-32}$ |
| $[1.2975,1.3]$ | $[-.476006,-.212646]$ | $[-.071444,-.054410]$ | $<3.456\times10^{-34}$ |
| $[1.5,1.5025]$ | $[-.232617,-.078645]$ | $[-.033624,-.025161]$ | $<1.826\times10^{-35}$ |

对每盒，程序另核新计算的 $a,\beta,\gamma,K,C_{m ref},\ell$ 与原完整
1334 盒 R133 native 的同一盒包络相交。该检查仅是同对象实现的一致性检查；
新 jets 的整个闭盒有效性来自上述直接区间运算和尾证明，不来自相交检查。

这三盒不能外推成整个正帽的导数证书。后续 consumer 必须在每个实际请求的
闭盒重新执行 (J.2)–(J.14)，保留完整 germ/参数/输入身份。

## 7. 用于完整有限残差的共同 Taylor 展开

若 $\mathcal R_J(r,\theta,\eta)$ 是固定完整有限 Neumann 多项式的残差，
径向中心 $r_c$ 与闭盒 $I$ 属于同一真实 scalar germ 和同一候选三次片，则

$$
\mathcal R_J(r,\eta)
\in\mathcal R_J(r_c,\eta)
 +(r-r_c)\,\mathcal R_J'(I,\eta).
\tag{J.15}
$$

这里对每个真实 $\eta$ 沿径向用微积分基本定理，随后统一包含所有 $\eta$。
对完整有限 Fourier 系数逐项求导，使用 (J.7)，即可有向计算右侧。也可以
与同一系数的直接区间求值逐项相交：两个包络都包含该系数在整个 $I$ 与
参数盒上的值，故交集仍包含真实值；空交集必须报错，不能取并集掩盖实现错误。

此步骤只处理完整有限部分。真正有理项的无限 Neumann 余项仍须在全径向
$\sum_m\sup_r$ 范数中另外支付，不能因使用 (J.15) 而省略。完整非零中心
收缩所需的残差、全 $DQ$、四独立驱动端口及两 mean 行也未由本篇提前授予。

复跑三盒：

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_codazzi_positive_cap_stable_jets.py \
  --out /tmp/R133-positive-cap-stable-jets-independent.json.gz
```

本次独立源码审阅核对了 (J.6)、(J.9)、(J.11) 与 (J.14) 的全部项；该审阅
未重跑 native。三盒的实际数值来自上述已保存的原生执行。
