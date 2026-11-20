# R138 补篇：截顶曲率的自由根迹与完整有限读出

2026-11-20，visible-exact-astra-ac637-20261120 / joint_kernel。

**状态：已证明。** 本篇只给解析迹不等式和可消费的有限 Gram 合同，不计算新科学目标，不授予完整根型正性、边值逆或精确闭曲面。沿用 [Z 补篇](R138-supplement-sharper-outer-lift-and-capped-curvature-energy.md) 的同一连续 Qrepair、真实根、真实物理角图与 drift flow。已成 X/Y/GB 的球只读；尤其旧 Y 的 $r_E,r_B$ 不由本篇替换。

## 1. 全环境频率、自由端点与归一化

记 $x=r-r_*$、$L=R-r_*$。Z.1--2 已证明

$$
\frac{14}{5}<L<\frac{29}{10},\qquad
\delta=\frac1{1840},\quad b=\frac1{40}=46\delta,
\quad d=L-\delta>0,\quad
K(r)\ge k_{\rm cap}(x):=\min(46x,b).
\tag{RT.1}
$$

角内积取 $\langle f,g\rangle=(2\pi)^{-1}\int_0^{2\pi}f^*g$，Fourier 基为 $e^{ik\xi}$、$k\in\mathbb Z$。所有环境向量分量均保留，$k=0$ 也保留。定义

$$
E_k[f]=\int_0^L\bigl(|f'|^2+k^2k_{\rm cap}|f|^2\bigr)\,dx,
\qquad
\overline{\mathfrak G}_{\rm cap}[z]
=\sum_{k\in\mathbb Z}E_k[z_k].
\tag{RT.2}
$$

右式含全部环境分量。函数在 $x=0,L$ 都不施加边界条件；后文辅助极小函数的自然端点条件不是未知函数的条件。原 scalar low $j\le96$/high $j\ge97$ 的频率是 $4j$，但乘真实 frame/系数后的环境频率未必只剩 $4j$。本篇不把 scalar $j=96,97$ 免费识别成环境单频 $384,388$。

## 2. 非零频率的自由外端精确 step 界

对 $k\ne0$ 置 $t=|k|/\sqrt{40}$，并定义

$$
c_k=\delta+\frac{\coth(td)}{t}.
\tag{RT.3}
$$

则对任意复值 $f\in H^1(0,L)$，

$$
\boxed{\quad |f(0)|^2\le c_kE_k[f],\qquad k\ne0.\quad}
\tag{RT.4}
$$

**证明。** 用 $k_{\rm step}=0$ 于 $[0,\delta]$、$k_{\rm step}=b$ 于 $[\delta,L]$ 降低势能。给定 $a=f(0)$、$v=f(\delta)$，第一段能量至少 $|a-v|^2/\delta$。第二段仅固定左值 $v$，对外端值自由极小化；其辅助极小函数为

$$
u(x)=v\frac{\cosh(t(L-x))}{\cosh(td)},
\qquad
\int_\delta^L(|u'|^2+t^2|u|^2)
=t\tanh(td)|v|^2.
$$

将任意 $f$ 写成此 $u$ 加左端为零的函数，交叉项由 $u''=t^2u$、$u'(L)=0$ 消失，故该极小值对所有 $f$ 是下界。再对复数 $v$ 完成平方，得到

$$
\frac{|a-v|^2}{\delta}+t\tanh(td)|v|^2
\ge\frac{|a|^2}{\delta+1/(t\tanh(td))}.
$$

这证明 (RT.4)。整个证明没有要求未知 $f'(L)=0$ 或 $f'(0)=0$。

由 $e^{2s}-1\ge2s$ 有 $\coth s\le1+1/s$，所以可直接消费

$$
c_k\le\widehat c_k:=%
\delta+\frac{\sqrt{40}}{|k|}+\frac{40}{d k^2}.
\tag{RT.5}
$$

若只使用已证统一长度，可将 $d$ 换成 $d_-:=14/5-\delta$；因 $d>d_-$，这只放宽上界。若使用真实根区间，则必须用 $d$ 的严格正下界，不以中点替代。

### 2a. 全高尾的 $|k|^{-2/3}$ 界

若 $h=(46k^2)^{-1/3}\le\delta$ 且 $2h\le L$，则另有

$$
|f(0)|^2\le3hE_k[f]
=3\,46^{-1/3}|k|^{-2/3}E_k[f].
\tag{RT.6}
$$

事实上，对 $y\in[h,2h]$，Young 与 Cauchy--Schwarz 给

$$
|f(0)|^2\le3|f(y)|^2+\frac32|f(0)-f(y)|^2
\le3|f(y)|^2+3h\int_0^{2h}|f'|^2.
$$

对 $y$ 平均，并用 $k^2k_{\rm cap}(y)\ge46k^2h=h^{-2}$，即得 (RT.6)。整数 $|k|\ge16000$ 足以保证条件；这只是有理量级比较 $46(16000)^2>1840^3$ 及 (RT.1)。因此可在该范围使用 $\min(c_k,3h)$。此式保证完整高频有 $|k|^{2/3}$ 的根值能量代价；不能把 step 界在无穷远的常数 $\delta$ 当成真正的最优高频行为。

### 2b. 零模不能删除

对 $k=0$，准确保留

$$
|f(0)-f(L)|^2\le L E_0[f].
\tag{RT.7}
$$

非零常函数说明不存在 $|f(0)|^2\le C E_0[f]$。本篇不从 C4/reflection 的名称推断未知环境向量的平均为零，也不假定一般角换元保持普通平均。后文不付外值的资格来自**接收器的严格零平均**，不是删除未知的环境零模。

## 3. 保留两端相关性的完整正二次式

若需要同时利用外值，对 $k\ne0$ 定义

$$
c_k^D=\delta+\frac{\tanh(td)}t,\qquad
e_k=\operatorname{sech}(td),\qquad
\tau_k=t\tanh(td).
$$

同样的降低势能给

$$
\boxed{\quad
E_k[f]\ge
\frac{|f(0)-e_k f(L)|^2}{c_k^D}
+\tau_k|f(L)|^2 .\quad}
\tag{RT.8}
$$

证明只需在 cap 段两端值为 $v,w$ 时使用准确最小能量

$$
t\coth(td)(|v|^2+|w|^2)
-2t\operatorname{csch}(td)\Re(v\overline w),
$$

加上 $|f(0)-v|^2/\delta$ 后对 $v$ 完成平方。对外值 $w$ 再极小化，得到 $c_k=c_k^D+e_k^2/\tau_k$，复得 (RT.4)。$k=0$ 的连续极限正是 (RT.7)：$c_0^D=L,e_0=1,\tau_0=0$。

## 4. 有限 Gram 与环境零模的完整接口

设有限读出 $A:L^2(S^1;\mathbb C^3)\to\mathbb C^m$ 的第 $i$ 行是 $a_i$，即 $(Az)_i=\langle a_i,z\rangle$。先假设每行 $\langle a_i\rangle=0$。令 $C$ 为非零 Fourier 频率上乘以 $c_k$ 的正乘子；可逐频换成 (RT.5)，或在符合条件处换成 (RT.6) 的较小值。由 (RT.4) 逐频 Cauchy--Schwarz，

$$
\boxed{\quad
\|Az(0)\|^2\le\|ACA^*\|\,
\overline{\mathfrak G}_{\rm cap}[z].\quad}
\tag{RT.9}
$$

等价地，对每个 $\lambda\in\mathbb C^m$，先对同一个 signed 组合 $\sum_i\lambda_i a_i$ 求 Fourier Gram，再取 $\|\lambda\|=1$ 上确界。不得把不同接收器、环境分量或交叉项当成独立正数后称为此精确 Gram。使用正数 majorant 可以，但须明确另付其损失。

一般行含 mean 时，记 $A_0=AP_0$、$A_\perp=A(I-P_0)$。零模与非零模的径向能量互相正交，(RT.7) 给完整形式

$$
\boxed{\quad
\|Az(0)-A_0z_0(L)\|^2
\le\|L A_0A_0^*+A_\perp C A_\perp^*\|\,
\overline{\mathfrak G}_{\rm cap}[z].\quad}
\tag{RT.10}
$$

这里 $A_0z_0(L)$ 是实际外端环境平均的贡献，未设为零；若只知外值范数，可再用三角不等式。更紧的两端相关性可直接由 (RT.8) 消费。

## 5. drift 密度对偶保平均，不要求未知场 mean0

沿 V.9--15 和 Z.7--9，真实变量是

$$
w(r,\phi)=\omega(r,\Theta(r,\phi)),\qquad
v_*(r,\xi)=w(r,\psi(r,\xi)),\qquad
\Gamma^{-1}\le\psi_\xi\le\Gamma.
\tag{RT.11}
$$

所有下式取真实根的同一个 $\psi$。对 moving $\phi$ 接收器 $a$，其准确对偶为密度

$$
T_\psi a=(a\circ\psi)\psi_\xi,
\qquad
\langle a,w(r_*)\rangle_\phi
=\langle T_\psi a,v_*(0)\rangle_\xi.
\tag{RT.12}
$$

直接换元给 $\langle T_\psi a\rangle=\langle a\rangle$。因此 $a$ 的 mean0 被准确保留，即使 $w$ 或 $v_*$ 的普通平均不为零。反之，无权 composition $a\circ\psi$ 不能代替 (RT.12)。

对 mean0 的 $a$，三种完整环境范数同时满足

$$
\|T_\psi a\|_2\le\sqrt\Gamma\|a\|_2,\qquad
\|T_\psi a\|_{\dot H^{-1/2}}
\le\sqrt\Gamma\|a\|_{\dot H^{-1/2}},\qquad
\|T_\psi a\|_{\dot H^{-1}}
\le\sqrt\Gamma\|a\|_{\dot H^{-1}}.
\tag{RT.13}
$$

第一式由 $\int|(a\circ\psi)\psi_\xi|^2\,d\xi=\int|a(\phi)|^2\psi_\xi(\psi^{-1}\phi)\,d\phi$。令 $I$ 是环境 mean0 primitive，则

$$
I_\xi T_\psi a=(I_\phi a)\circ\psi
-\langle(I_\phi a)\circ\psi\rangle_\xi.
$$

正交去平均不增 $L^2$ 范数，无权 composition 的 $L^2$ 范数至多 $\sqrt\Gamma$，从而证明第三式。第二式是同一 mean0 Fourier Hilbert scale 的端点插值；两端算子范数都是 $\sqrt\Gamma$，所以中间范数也不超过它。不需要 $\psi_{\xi\xi}$。

用 (RT.5)、(RT.12)--(RT.13)，定义

$$
N(a)^2=\delta\|a\|_2^2
+\sqrt{40}\|a\|_{\dot H^{-1/2}}^2
+\frac{40}{d}\|a\|_{\dot H^{-1}}^2.
\tag{RT.14}
$$

得到无外端费用的

$$
\boxed{\quad
|\langle a,w(r_*)\rangle|^2
\le\Gamma N(a)^2\,
\overline{\mathfrak G}_{\rm cap}[v_*],\qquad \langle a\rangle=0.\quad}
\tag{RT.15}
$$

若已严格证明 $a$ 的真实环境频率均满足 $|k|\ge M$，可令
$N(a)^2\le[\delta+\sqrt{40}/M+40/(dM^2)]\|a\|_2^2$。
这项频率资格必须针对最终接收器，而不是只针对原 scalar 输入。

### 5a. 同一有限 Gram 的密度费用

对 mean0 行 $a_i$，令 $G_\nu$ 的元素为
$\langle a_i,|D|^{-\nu}a_j\rangle$，$\nu=0,1,2$。对每个行组合应用 (RT.13)，得到 Loewner 上界

$$
A_\psi C A_\psi^*
\preceq\Gamma\left(\delta G_0+\sqrt{40}G_1+\frac{40}{d}G_2\right),
\tag{RT.16}
$$

其中 $A_\psi$ 的行是 $T_\psi a_i$。右侧保留真实系数/完整 Fourier 尾/环境三分量和所有交叉项；这些 Gram 或其上界是下一消费者须支付的量，本篇没有给数值。无需重算或重建整条 drift flow。

若读出原本在 physical $\theta$，必须先以
$T_\Theta a=(a\circ\Theta)\Theta_\phi$ 变成 moving $\phi$ 密度。其三种范数的范数至多再乘 $\sqrt{A_\Theta}$，证明与 (RT.13) 相同。可直接估真实 $T_\Theta a$ 以减少损失，但不能省去 Jacobian、把 moving $\phi$ 等同 physical $\theta$，或把两种内积混用。

## 6. 周期 primitive 接收器与完整源项

特别地若 $a=P'$ 是同一个 moving $\phi$ 中的周期向量导数，严格有 $\langle a\rangle=0$，而 $P$ 的 mean 仍保留。令
$P_0\ge\|P\|_2$、$P_1\ge\|P'\|_2$。Parseval 给

$$
\|P'\|_{\dot H^{-1}}\le P_0,\qquad
\|P'\|_{\dot H^{-1/2}}^2
=\sum_{k\ne0}|k||P_k|^2\le P_0P_1.
$$

故可直接使用

$$
N(P')^2\le\delta P_1^2+\sqrt{40}P_0P_1+\frac{40}{d}P_0^2,
\qquad
\|P\|_{H^{1/3}}\le
P_0^{2/3}(P_0^2+P_1^2)^{1/6}.
\tag{RT.17}
$$

第二式是非齐次 $L^2/H^1$ 插值，包含 $P$ 的环境 mean。若准确根消元的读出是
$-\rho^{-1}[\langle P',w(r_*)\rangle+\langle P,h\rangle]$，本篇只控制第一项；第二项仍用真实同角 $h$ 的 $H^{-1/3}$ 费用和 (RT.17) 支付。旧 Y 的 $r_E,r_B$ 在其原 physical 范数和角变换资格下完整保留；转成 moving density 时要显式付原 $A_\Theta$ 费用，不能把 $h$ 设为零或将两个项的 mean 一并删掉。

## 7. 同一实际能量的消费与 $2\pi$

Z.9 和旧 V.8 给非归一角能量

$$
\mathfrak G_{\rm cap}[v_*]^{1/2}
\le\sqrt\Gamma\{\sqrt{C_E}\sqrt{\mathcal E}
+\sqrt{C_H}\|H\|_2\},\qquad
\|H\|_2\le h_E\sqrt{\mathcal E}+h_B\sqrt{\mathcal B}.
\tag{RT.18}
$$

此处 $\mathfrak G_{\rm cap}=2\pi\overline{\mathfrak G}_{\rm cap}$。所以对用归一 $\langle\ ,\ \rangle$ 的 moving mean0 接收器，准确得到

$$
\boxed{\quad
\sqrt{2\pi}|\langle a,w(r_*)\rangle|
\le\Gamma N(a)\left[
(\sqrt{C_E}+\sqrt{C_H}h_E)\sqrt{\mathcal E}
+\sqrt{C_H}h_B\sqrt{\mathcal B}\right].\quad}
\tag{RT.19}
$$

若全部能量也用归一角积分，令 $\overline{\mathcal E}=\mathcal E/(2\pi)$、$\overline{\mathcal B}=\mathcal B/(2\pi)$，则删去左侧 $\sqrt{2\pi}$ 并将右侧能量换成加横线者。若根型负部写成 $2\pi\|Aw\|^2$，这个 $2\pi$ 恰与非归一能量相消，不再另加或遗漏。

有限行向量的 (RT.19) 把 $N(a)$ 换成
$\|\delta G_0+\sqrt{40}G_1+(40/d)G_2\|^{1/2}$。两个 $\sqrt\Gamma$ 分别来自真实密度对偶和 Z.9 的体能量换元，合为 $\Gamma$。这里不额外出现 $A_\Theta$ 的前提是接收器已经与 $w=\omega\circ\Theta$ 同在 moving $\phi$；若从 physical 接收器起步，则按第 5 节付对应费用。

这提供相对体能量的完整有限读出接口。完整 high Schur、有限负部矩阵、上述真实行 Gram 及其 $h$ 源费用仍须实际支付；原 all-root-data 正型失败不推出实际可达根迹上的核，也不由本篇自动转成整体逆。
