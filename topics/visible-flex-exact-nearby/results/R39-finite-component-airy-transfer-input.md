# R39：有限实际组件的 Airy–Volterra 传播及全网输入接口

2026-11-12，independent-audit。

**状态：本文的局部定理及其常数已证明；实际候选的全网逆尚未完成。**
本文给任意一个已经验证为非特征简单转折的真实算子，构造完整
Airy 振幅实现，并给出可从有限实际系数导数计算的正逆和普通源常数。
没有“当前几何减径向基点很小”的假设。小量来自实际转折邻域的长度，
不是把非径向主系数当作低阶小扰动。

本文允许有限多个正、负组件。每个组件的全部端口、均值、普通源和
跨端耦合均保留；中央负组件的圆周返回图不被当作全域反馈。最后
明确列出：要接到完整有限阶相位及全网逆，还须在实际候选上支付哪些
输入。R499 的 finite columns、共同 Gram 和高频正常形没有在本篇
被无条件移植。

## 1. 范数、实际算子与定理范围

设根角的真实长度为 $\ell>0$，记
$$
q=2\pi/\ell,\qquad e_j(\phi)=e^{iqj\phi},\qquad
\langle j\rangle=(1+j^2)^{1/2}.
$$
使用平均测度 $d\phi/\ell$，并定义
$$
\|u\|_{H^s_\ell}^2=\sum_{j\in\mathbb Z}
 \langle j\rangle^{2s}|u_j|^2,
\qquad E_s=(H^s_\ell)^2.
\tag{1.1}
$$
物理频率是 $|qj|$，而不是 $|j|$；下面保留所有圆长因子。

局部主定理针对真实 canonical 方程
$$
\boxed{\quad U_{\xi\xi}-\xi U_{\phi\phi}
       +V(\xi,\phi)U=f(\xi,\phi),\quad 0\le\xi\le h\le1.\quad}
\tag{1.2}
$$
$V$ 为实函数，并具有下文实际使用的有限角导数和径向连续性。
不是只取 $V$ 的平均，也不删去它与 $j=0$ 的耦合。
先证明 (1.2) 的完整定理，再在 §6 给出真实散度算子到它的准确变换。
§§2–7 的传播结论是无权、有限阶 Sobolev 结论。即使 R37 已把
roots 固定，后续 exact Tricomi 逆坐标仍可能令物理径向变量依赖
新角；固定 root 加有限 Fourier 输入不自动支付该 canonical
系数的正解析宽或直接 log 角权。§8 的加权正组件结论仅在 R35
自身的真实 form 权门成立时使用，两种输入不能互相替代。

一组有限 Sobolev 档记为 $\mathcal S\subset\mathbb R$。需要某个
增益的输出档时，把该档也加入 $\mathcal S$；这是一张预先确定的
有限表，不声称免费获得任意多阶导数。

## 2. 独立的全负实轴 Airy 界

使用标准 Airy 函数的初值及 Wronskian：
$$
\begin{aligned}
\operatorname{Ai}(0)&=\frac1{3^{2/3}\Gamma(2/3)},&
\operatorname{Ai}'(0)&=-\frac1{3^{1/3}\Gamma(1/3)},\\
\operatorname{Bi}(0)&=\frac1{3^{1/6}\Gamma(2/3)},&
\operatorname{Bi}'(0)&=\frac{3^{1/6}}{\Gamma(1/3)},
\end{aligned}
\qquad
\operatorname{Ai}\operatorname{Bi}'-
\operatorname{Ai}'\operatorname{Bi}=\pi^{-1}.
\tag{2.1}
$$
这些标准恒等式见 NIST DLMF
[9.2.3–9.2.7](https://dlmf.nist.gov/9.2#ii)。以下全轴估计由能量法
直接证明，不调用未给误差的渐近级数。

**引理 2.1。** 对 $t\ge0$，以及 $Y=\operatorname{Ai}$ 或
$Y=\operatorname{Bi}$，都有
$$
\boxed{\quad |Y(-t)|\le5(1+t)^{-1/4},\qquad
 |Y'(-t)|\le5(1+t)^{1/4}.\quad}
\tag{2.2}
$$

**证明。** 令 $y(t)=Y(-t)$，则 $y''+ty=0$。
在 $0\le t\le1$，$E_y=y^2+(y')^2$ 满足
$$
E_y'=2(1-t)yy'\le(1-t)E_y,
\qquad E_y(t)\le e^{t-t^2/2}E_y(0).
\tag{2.3}
$$
在 $t\ge1$，令
$$
\tau=\tfrac23t^{3/2},\qquad z(\tau)=t^{1/4}y(t).
$$
逐项微分得到
$$
z_{\tau\tau}+\left(1+\frac5{36\tau^2}\right)z=0.
\tag{2.4}
$$
因此 $E_z=z^2+z_\tau^2$ 满足
$|E_z'|\le5E_z/(36\tau^2)$。在 $\tau_0=2/3$，
$$
(z,z_\tau)=(y,y'+y/4)\big|_{t=1},\qquad
E_z(\tau_0)\le\frac{25}{16}E_y(1),
$$
从而
$$
\sqrt{E_z(\tau)}\le\frac54 e^{17/48}\sqrt{E_y(0)}.
\tag{2.5}
$$
由 $y=t^{-1/4}z$ 和
$y'=t^{1/4}z_\tau-\tfrac14t^{-5/4}z$，可用共同常数
$\tfrac{25}{16}e^{17/48}\sqrt{E_y(0)}$ 同时控制 (2.2) 中两项。
这里 $t^{-1/4}\le2^{1/4}(1+t)^{-1/4}$，且
$2^{1/4}<5/4$；$0\le t\le1$ 的 (2.3) 也由该常数覆盖。

最后，$e^{-t}\ge1-t$ 在 $[0,1]$ 给
$$
\Gamma(2/3)\ge9/10,\qquad \Gamma(1/3)\ge9/4.
$$
代入 (2.1)，四个初值的绝对值都小于 $1$，所以
$E_y(0)<2$。用 $e^{17/48}<\sqrt3<7/4$、$\sqrt2<3/2$，上述
共同常数小于 $525/128<5$。证毕。

## 3. 全频率、含均值的精确 Airy 框架

置
$$
c_A=-\operatorname{Ai}'(0)/\operatorname{Ai}(0)>0,
\qquad c=c_A^{-1/2}.
\tag{3.1}
$$
对 $j\ne0$，$\lambda=q|j|$，定义 Fourier 乘子
$$
D_\pm(\xi,j)=c\lambda^{-1/3}
 \bigl[\operatorname{Bi}(-\xi\lambda^{2/3})
       \pm i\operatorname{Ai}(-\xi\lambda^{2/3})\bigr].
\tag{3.2}
$$
对 $j=0$ 定义
$$
D_\pm(\xi,0)=c(1\pm i\xi/\pi).
\tag{3.3}
$$
它们都精确满足自由方程
$D''+\xi\lambda^2D=0$，并且
$$
F_*(\xi)=\begin{pmatrix}D_+&D_-\\D_+'&D_-'\end{pmatrix},
\qquad \det F_*(\xi,j)=-2ic^2/\pi
\quad\text{对每个 }j\in\mathbb Z.
\tag{3.4}
$$
第二行始终是完整的 $\xi$ 导数。均值列不被删除，也不需要对
$|D|$ 的均值求逆。

为列出全部费用，定义
$$
\begin{aligned}
A_\ell&=\max\{1,2^{1/6}q^{-1/3}\},& C_D&=10cA_\ell,\\
C_{P,0}&=10c\max\{\pi^{-1},q^{1/3}\},\\
C_P(h)&=10c\max\{\pi^{-1},q^{1/3}+h^{1/4}q^{1/2}\},\\
C_H(\delta)&=10c\max\{1,2^{1/4}\delta^{-1/4}q^{-1/2}\}
\quad(0<\delta\le h).
\end{aligned}
\tag{3.5}
$$
引理 2.1 立即给，对任意实 $s$，
$$
\begin{array}{ll}
\|D_\pm(\xi)\|_{H^s\to H^{s+1/3}}\le C_D,
 &0\le\xi\le h,\\
\|D_\pm'(0)\|_{H^s\to H^{s-1/3}}\le C_{P,0},\\
\|D_\pm'(\xi)\|_{H^s\to H^{s-1/2}}\le C_P(h),
 &0\le\xi\le h,\\
\|D_\pm(\delta)\|_{H^s\to H^{s+1/2}}\le C_H(\delta).
\end{array}
\tag{3.6}
$$
例如第一项使用 $\langle j\rangle^{1/3}|j|^{-1/3}\le2^{1/6}$；
第三项使用
$(1+\xi\lambda^{2/3})^{1/4}\le1+h^{1/4}\lambda^{1/6}$。
这些不等式同时覆盖 $j=0$。

根与严格负切口的自然 Cauchy 空间分别是
$$
\mathcal P_{0,s}=H^{s+1/3}\oplus H^{s-1/3},\qquad
\mathcal P_{\delta,s}=H^{s+1/2}\oplus H^{s-1/2}.
\tag{3.7}
$$
令
$$
\begin{aligned}
B_0&=\sqrt{2(C_D^2+C_{P,0}^2)},&
I_0&=\frac{\pi}{\sqrt2c^2}\sqrt{C_D^2+C_{P,0}^2},\\
B_\delta&=\sqrt{2(C_H(\delta)^2+C_P(h)^2)},&
I_\delta&=\frac{\pi}{\sqrt2c^2}
          \sqrt{C_H(\delta)^2+C_P(h)^2}.
\end{aligned}
\tag{3.8}
$$
则 $F_*(0)$ 从 $E_s$ 到 $\mathcal P_{0,s}$ 的 norm 至多 $B_0$，
其逆至多 $I_0$；$F_*(\delta)$ 对应的两个 norm 至多
$B_\delta,I_\delta$。逆的公式就是
$$
F_*^{-1}=\frac{i\pi}{2c^2}
  \begin{pmatrix}D_-'&-D_-\\-D_+'&D_+\end{pmatrix}.
\tag{3.9}
$$
因此这是完整的双向 Cauchy 框架，不只是一对近似振荡列。

此外，直接用 (2.1) 与 (3.3) 可核对
$$
F_*^*\left[\frac{\pi c_A}{2i}
 \begin{pmatrix}0&I\\-I&0\end{pmatrix}\right]F_*
=J,\qquad J=\operatorname{diag}(I,-I).
\tag{3.10}
$$
即 $\pi c_A\operatorname{Im}\langle U,U_\xi\rangle$ 是准确的
双振幅 Green 通量；这个常数在 ordinary source 中也必须保留。

## 4. 从有限导数计算势的乘法常数

在区间 $[0,h]$ 定义
$$
M_r(V)=2^{|r|/2}\sum_{k\in\mathbb Z}\langle k\rangle^{|r|}
              \sup_{\xi\in[0,h]}|V_k(\xi)|.
\tag{4.1}
$$
则
$$
\|Vu\|_{H^r}\le M_r(V)\|u\|_{H^r}.
\tag{4.2}
$$
证明只需
$\langle j\rangle^r/\langle j-k\rangle^r
\le2^{|r|/2}\langle k\rangle^{|r|}$ 与离散 Young 不等式。
这里是 Fourier 系数径向上确界的和，不与较弱的
“各径向点 Fourier 和的上确界”混淆。

不必逐一计算无限多个 Fourier 系数。令归一角
$\vartheta=q\phi$，任选整数 $p>|r|+1$，并供应实际界
$$
B_0(V)=\sup|V|,\qquad B_p(V)=\sup|\partial_\vartheta^pV|.
$$
对非零 $k$ 作 $p$ 次积分分部，再用单调级数积分比较，得到
$$
\boxed{\quad
M_r(V)\le2^{|r|/2}\left[
B_0(V)+2^{1+|r|/2}B_p(V)
\left(1+\frac1{p-|r|-1}\right)\right].\quad}
\tag{4.3}
$$
右端是有限实际导数的显式费用。它可以很大；下节以真实短 collar
吸收其同档大小，不要求它来自小振幅。

## 5. 实际全频 Airy–Volterra 定理

对每个 $s\in\mathcal S$ 定义
$$
K_s=\frac{\pi C_D^2}{c^2}M_{s+1/3}(V)
    =100\pi A_\ell^2M_{s+1/3}(V),
\qquad G_\ell=\frac{\pi C_D}{\sqrt2c^2}.
\tag{5.1}
$$
取
$$
\boxed{\quad 0<\delta\le h,\qquad
\delta\max_{s\in\mathcal S}K_s\le1/10.\quad}
\tag{5.2}
$$
若最大值为零，则第二个限制空缺。输入 $h$、$V$ 和圆长来自实际
canonical 组件；不是从别的背景沿用的参数。

**定理 5.1。** 在 (5.2) 下，(1.2) 具有如下精确实现。
对每个 $s\in\mathcal S$，初始振幅 $z_0\in E_s$，以及
$f\in L^1([0,\delta];H^{s-1/3}_\ell)$，存在唯一
$z\in C([0,\delta];E_s)$ 的振幅解，并由
$$
\binom{U}{U_\xi}=F_*(\xi)z(\xi)
\tag{5.3}
$$
给出相应的真实 PDE Cauchy 解。准确方程为
$$
\begin{aligned}
z'&=\mathcal K(\xi)z+\Gamma_f(\xi),\\
\Gamma_f&=\frac{i\pi}{2c^2}\binom{-D_-f}{D_+f},\\
\mathcal K z&=\frac{i\pi}{2c^2}
 \binom{-D_-}{D_+}\bigl[-V(D_+z_++D_-z_-)\bigr].
\end{aligned}
\tag{5.4}
$$
它满足
$$
\|\mathcal K(\xi)\|_{E_s\to E_{s+2/3}}\le K_s,
\qquad
\|\Gamma_f(\xi)\|_{E_s}\le G_\ell\|f(\xi)\|_{H^{s-1/3}}.
\tag{5.5}
$$
齐次传播记作 $C(\xi,\eta)$。正向及反向均有
$$
\boxed{\quad
\|C(\xi,\eta)\|_{E_s\to E_s}
\le e^{K_s|\xi-\eta|}\le e^{1/10},
\quad 0\le\xi,\eta\le\delta.\quad}
\tag{5.6}
$$
完整普通源公式是
$$
z(\xi)=C(\xi,0)z_0+
\int_0^\xi C(\xi,t)\Gamma_f(t)\,dt,
\tag{5.7}
$$
特别
$$
\sup_\xi\|z(\xi)\|_{E_s}
\le e^{1/10}\left[\|z_0\|_{E_s}
 +G_\ell\int_0^\delta\|f(t)\|_{H^{s-1/3}}dt\right].
\tag{5.8}
$$
从根 pair 到严格 cut pair 的齐次 norm 至多
$B_\delta e^{1/10}I_0$，反向至多 $B_0e^{1/10}I_\delta$；
零初值的 cut source norm 至多
$$
B_\delta e^{1/10}G_\ell
\|f\|_{L^1_\xi H^{s-1/3}}.
\tag{5.9}
$$

**证明。** 在 (5.4) 的 $\mathcal K$ 中，row $(D_+,D_-)$ 从
$E_s$ 到 $H^{s+1/3}$ 的 norm 至多 $\sqrt2C_D$；中间乘法由
(4.2) 控制；column $(-D_-,D_+)^t$ 再增益 $1/3$，其 norm
同为 $\sqrt2C_D$。乘上 $\pi/(2c^2)$ 正好得到 (5.5)，不是
一个隐藏的 background 常数。source column 的同样计算给
$G_\ell$。

将 $E_{s+2/3}\hookrightarrow E_s$，$\mathcal K$ 是强连续且一致有界的
算子族，标准逐次 Volterra 积分的第 $n$ 项 norm 不超过
$K_s^n|\xi-\eta|^n/n!$。级数绝对收敛，给存在、唯一性和
(5.6)；反向积分给同一个逆 $C(\eta,\xi)$。同一估计证明
(5.7)–(5.9)。

还须核实它真解 PDE：自由 $F_*$ 解无势的一阶 Cauchy 系统，
而其第一行乘 $(-D_-,D_+)^t$ 恒为零。因此对
$U=D_+z_++D_-z_-$ 微分时，$z'$ 的附加项在第一行准确消去，
得到 (5.3) 的完整第二槽。再微分第二槽，利用 (3.9) 得到
$U_{\xi\xi}-\xi U_{\phi\phi}=f-VU$。反过来，一个处于该
Cauchy 实现中的解经 (3.9) 必须满足 (5.4)，所以双向等价。
先在平滑数据上逐项验证，再由上述有界式延拓到声明的空间。
根处的较高 momentum trace 由 $F_*(0)$ 定义；不声称正距离处
的 momentum 仍有根处的 $H^{s-1/3}$ 正则。证毕。

### 5.1 真实通量、有限增益和势的差量

当 $V$ 实且 $f=0$ 时，Green 恒等式给
$$
\partial_\xi\operatorname{Im}\langle U,U_\xi\rangle=0.
$$
因此由 (3.10)
$$
C(\xi,\eta)^*J C(\xi,\eta)=J
\tag{5.10}
$$
在 $E_0$ 上准确成立。普通源则保留 (5.7) 的 affine 项，不能
由齐次通量等式删除。

另有实际有限增益
$$
\|C(\xi,\eta)-I\|_{E_s\to E_{s+2/3}}
\le |\xi-\eta|K_s e^{1/10}.
\tag{5.11}
$$
这是直接把 $C-I=\int\mathcal K C$ 用于较高输出档，不是完整
classical symbol expansion，也没有得到根 frame 的 $4/3$ 阶余项。

若 $V,\widetilde V$ 在同一个 canonical 圆和区间都满足 (5.2)，
则 Duhamel 恒等式给同档差量
$$
\|C_V(\xi,\eta)-C_{\widetilde V}(\xi,\eta)\|_{E_s\to E_s}
\le |\xi-\eta|e^{1/10}\,
100\pi A_\ell^2M_{s+1/3}(V-\widetilde V).
\tag{5.12}
$$
其中两个传播因子的指数相加，长度总和恰为 $|\xi-\eta|$。
若实际几何同时改变坐标、圆长或 source map，须另计那些变换的
差量；(5.12) 不会免费支付 moving composition。

## 6. 实际简单转折到 canonical 算子的完整代数

先按 [R36](R36-moving-turning-cap-normalization.md) 支付实际
移动根的非特征条件、拉直和 root-anchored shear。在负侧
$x\ge0$，真实密度主矩阵成为
$$
\operatorname{diag}(A(x,\theta),-xB(x,\theta)),\qquad A,B>0.
\tag{6.1}
$$
若使用 [R37](R37-fixed-type-metric-defect-newton-interface.md)
的 modified 算子，其 roots 是目标曲率的真实 roots；目标存在
额外简单零点时也必须全部保留。

### 6.1 根角的实际长度与 height

置 $A_0(\theta)=A(0,\theta)$、$B_0(\theta)=B(0,\theta)$，定义
$$
Y'(\theta)=\sqrt{A_0/B_0},\qquad
\ell=\int_0^{2\pi}Y'(\theta)d\theta,
\qquad t_0=(A_0B_0)^{-1/4}.
\tag{6.2}
$$
令 $y=Y(\theta)$，再作 $u=t_0v$ 并左乘 $t_0$。新的主系数为
$$
a=t_0^2A/Y',\qquad b=t_0^2BY',
\qquad a(0,y)=b(0,y)=1.
\tag{6.3}
$$
如果 (6.1) 中还带真实零阶密度 $d$，新的完整零阶项为
$$
q_*=t_0^2(d/Y')-x t_0\partial_y(BY'\partial_y t_0),
\tag{6.4}
$$
所有旧函数均在逆角中取值。没有假设 $d=0$，也没有丢掉
height 共轭产生的项。此时算子为
$$
P_*v=\partial_x(a v_x)-\partial_y(xb v_y)+q_*v.
\tag{6.5}
$$

### 6.2 实特征坐标及准确势

令 $d_*=\sqrt{b/a}$。用带符号实变量 $z$ 解两个实际圆周流
$$
\partial_z\theta_\pm(z,\eta)
 =\pm2z^2d_*(z^2,\theta_\pm(z,\eta)),
\qquad \theta_\pm(0,\eta)=\eta.
\tag{6.6}
$$
它们是保向圆周微分同胚；对初角的导数等于相应
$\pm2z^2(d_*)_y$ 沿流积分的指数。逆标签记为 $S_\pm(z,y)$。
由唯一性 $S_-(z,y)=S_+(-z,y)$，且
$S_\pm=y\mp(2/3)z^3+O(z^5)$。定义
$$
\Delta=S_--S_+,\quad R=\frac{3\Delta}{4z^3},\qquad
\phi=\frac{S_++S_-}{2},\quad
\xi=xR^{2/3},\quad x=z^2.
\tag{6.7}
$$
在 $z=0$ 不作数值除零，而使用准确的有限积分
$$
\frac{\Delta}{z^3}
=\frac12\int_0^1(1-t)^2\partial_z^3\Delta(tz,y)dt.
\tag{6.8}
$$
$R$ 与 $\phi$ 为偶函数，$R(0)=1$，$\phi(0,y)=y$。
偶函数向 $x$ 的有限阶下降由
$F'(z)/z=\int_0^1F''(tz)dt$ 逐次完成，只使用有限实际导数。

例如可在预定原 collar $0\le x\le h_0$ 验证有限几何门
$$
a,b>0,\qquad \tfrac12\le R\le\tfrac32,\qquad
\phi_y\ge\tfrac12,\qquad
J_\Psi:=\xi_x\phi_y-\xi_y\phi_x\ge\tfrac12.
\tag{6.9}
$$
这些量在根处分别为 $1,1,1,1$，所以对任何具有所需有限光滑性
的实际非特征简单根，缩小 collar 能满足 (6.9)。实际使用时仍须
记录所选 $h_0$、正下界和导数界；“足够短”不能代替数值证书。
因为固定 $x$ 时 $\phi$ 保向，且
$\partial_x\xi|_\phi=J_\Psi/\phi_y>0$，该变换在整个 collar
单射，其像包含 $0\le\xi\le h_0/2$ 的完整圆柱。

逆标签满足
$(S_\pm)_x\pm\sqrt{x}\,d_*(S_\pm)_y=0$。将
$S_\pm=\phi\mp(2/3)\xi^{3/2}$ 代回，两次平方的和、差给
$$
a\xi_x\phi_x-xb\xi_y\phi_y=0,\qquad
a\phi_x^2-xb\phi_y^2
=-\xi(a\xi_x^2-xb\xi_y^2).
\tag{6.10}
$$
故真实 density 主矩阵准确变为
$$
\alpha\operatorname{diag}(1,-\xi),\qquad
\alpha=\frac{a\xi_x^2-xb\xi_y^2}{J_\Psi}
       =\sqrt{\frac{xab}{\xi}}>0.
\tag{6.11}
$$
第二个公式在根处以 $\xi/x=R^{2/3}$ 延伸，说明 $\alpha(0)=1$。
它也由二维 density 行列式在坐标变换下不变直接核对。

记换元后的零阶密度为 $q_0=(q_*/J_\Psi)\circ\Psi^{-1}$。
再令旧 height 为 $\alpha^{-1/2}U$，左乘 $\alpha^{-1/2}$。
完整算子正是 (1.2)，其势为
$$
\boxed{\quad
V=\frac{q_0}{\alpha}
-\frac12(\log\alpha)_{\xi\xi}
-\frac14(\log\alpha)_\xi^2
+\xi\left[\frac12(\log\alpha)_{\phi\phi}
          +\frac14(\log\alpha)_\phi^2\right].\quad}
\tag{6.12}
$$
这是对 $\alpha^{-1/2}P_{\rm transformed}(\alpha^{-1/2}U)$ 的
直接乘积法则；一级项准确消去，所有零阶项保留。

### 6.3 从实际有限 jet 表计算 (4.3)

令 $L=\log\alpha$，在所选 canonical 圆柱中记录
$$
L_{i,j}=\sup|\partial_\vartheta^i\partial_\xi^jL|,
\qquad Q_p=\sup|\partial_\vartheta^p(q_0/\alpha)|,
\qquad \vartheta=q\phi.
$$
由 (6.12) 逐项微分，任意非负整数 $p$ 都有显式上界
$$
\begin{aligned}
B_p(V)\le{}&Q_p+\tfrac12L_{p,2}
 +\tfrac14\sum_{j=0}^p{p\choose j}L_{j,1}L_{p-j,1}\\
&+h q^2\left[
 \tfrac12L_{p+2,0}
 +\tfrac14\sum_{j=0}^p{p\choose j}L_{j+1,0}L_{p-j+1,0}
\right].
\end{aligned}
\tag{6.13}
$$
与 (4.3)、(5.1) 组合就得到真实 $\delta$ 门。根原系数、短流、
reciprocal、偶下降和逆坐标所需的有限 jet 次数须事先预留；保守地
供应 (6.5) 系数至 $C^{2p+12}$ 足以执行这里到 $B_p(V)$ 的
有限微分过程。该保守次数不声称最优，也不把一张仅 $C^4$ 的
径向 spline 自动升级到它。

## 7. 普通源、完整边界动量和安全的实坐标 source 范数

将 §6 中全部实际坐标合记为
$\Psi:(r,\theta)\mapsto(\xi,\phi)$，绝对 Jacobian 为
$J_\Psi>0$。将全部正 height 因子合记为新坐标中的 $t$，即
$u_{\rm ph}=(tU)\circ\Psi$。准确源式是
$$
\boxed{\quad f_{\rm can}=t(f_{\rm ph}/J_\Psi)\circ\Psi^{-1}.\quad}
\tag{7.1}
$$
这是密度变换再左乘 height，并非只把 $f$ 作函数复合。若
$f_{\rm ph}=\operatorname{div}F$，置
$$
\widetilde F=(D\Psi F/J_\Psi)\circ\Psi^{-1},
$$
则 Piola 变换和乘积法则给
$$
f_{\rm can}=\operatorname{div}(t\widetilde F)
             -\nabla t\cdot\widetilde F.
\tag{7.2}
$$
最后一项必须保留。将 (7.2) 当作 ordinary source 使用定理 5.1
时，还要验证其声明的 $L^1_\xi H^{s-1/3}$ 范数；仅给一个弱
divergence 源不自动满足该条件。

为避免混合径向、角坐标下的未付各向异性声称，以下给一个保守且
完全可计算的充分输入。令 $X=\Psi^{-1}$，$a=t/(J_\Psi\circ X)$，
$b_i=\partial_\vartheta X_i$，取整数
$m\ge\max(0,\lceil s-1/3\rceil)$。定义有限系数递推
$$
C_{0,0}=a,\qquad
C_{k+1,\gamma}=\partial_\vartheta C_{k,\gamma}
 +\sum_{i=1}^2 b_i C_{k,\gamma-e_i},
\tag{7.3}
$$
越界项取零。准确有
$$
\partial_\vartheta^k(a f_{\rm ph}\circ X)
=\sum_{|\gamma|\le k}C_{k,\gamma}
       (\partial^\gamma f_{\rm ph})\circ X.
$$
记
$$
A_m=\max_{0\le k\le m}\sum_{|\gamma|\le k}
                         \|C_{k,\gamma}\|_\infty,
\qquad
\|f\|_{C^m}=\max_{|\gamma|\le m}\|\partial^\gamma f\|_\infty.
$$
由 $(1+j^2)^m=\sum_{k=0}^m{m\choose k}j^{2k}$，得到
$$
\boxed{\quad
\|f_{\rm can}\|_{L^1_\xi H^{s-1/3}}
\le\delta\,2^{m/2}A_m\|f_{\rm ph}\|_{C^m}.\quad}
\tag{7.4}
$$
所有系数仅在实坐标上取值。可以另证更精细的 Sobolev source
输入以减轻损失，但不能从 (7.4) 推出任意
$L^2_rH^s_\theta$ 源在 mixed 坐标中无损。

边界高度变换记为 $C_\Gamma u_{\rm ph}=U$，其真正对偶给
$$
C_\Gamma^{-*}p_{\rm ph}=p_{\rm can}+\sigma_\Gamma U.
\tag{7.5}
$$
这里 $p$ 是散度密度的完整 graph conormal，不是只取某一个
normal derivative。对单独的 (6.11) 共轭、正向平切口，
$$
\alpha^{-1/2}p_{\rm transformed}
=U_\xi-\tfrac12(\log\alpha)_\xi U,
$$
直接显示 (7.5) 的真实 shear。若原切口为 $r=R(\theta)$，
须保留 R36 的
$(a-bR')u_r+(b-cR')u_\theta$，再作该边界参数的 Jacobian
和 height 对偶。canonical cut 到普通物理 cut 的双向比较还需
实际 spacelike 门及其有限 norm；本篇没有以 height trace 代替
第二槽。

## 8. 正组件的有限角 Sobolev bootstrap 不要求振幅小

本节补充 [R35](R35-positive-cap-without-background-smallness.md)
与 R36 中已经构造的真实正组件 Dirichlet 逆。使用那里同一个
自然域 $\mathcal V_0$、实际 form、同一个 source 对偶和全部边界。
设 $G=P^{-1}:\mathcal V_0^*\to\mathcal V_0$ 的真实 norm 为
$L_G$。无权时可取 $L_G=g_0$；满足 R35 小角权门时，在共同
加权表示中可取 $L_G=2g_0$。

记实际矩阵表示为
$A=A_0^{1/2}CA_0^{1/2}$，其中 $A_0$ 只依赖径向变量。
对 $k\ge1$，供应实际 commutator form bound
$$
M_k\ge\|\operatorname{ad}_{\partial_\vartheta}^k P
          \|_{\mathcal V_0\to\mathcal V_0^*}.
\tag{8.1}
$$
无权时 $M_k=\|\partial_\vartheta^kC\|_\infty$ 是充分选择。
加权时应用同一边界和 form 表示，充分选择为
$$
M_k=\sum_{n\in\mathbb Z}|n|^k w(n)
                      \sup_x\|C_n(x)\|,
\tag{8.2}
$$
其中解析权 $w(n)=e^{|\sigma||n|}$，或 R35 的直接 log 权
$w(n)=e^{|\sigma|\omega(|n|)}$。因为权与角导数以及 $A_0$
交换，(8.2) 控制的是实际共轭后 commutator；不把非局部加权
乘法误写成一个新的点态矩阵。

若 $u=Gf$，令
$X_k=\|\partial_\vartheta^ku\|_{\mathcal V}$、
$F_k=\|\partial_\vartheta^kf\|_{\mathcal V_0^*}$。直接对
$Pu=f$ 作差商并归纳可得
$$
\boxed{\quad X_0\le L_GF_0,\qquad
X_k\le L_G\left[F_k+
 \sum_{j=1}^k{k\choose j}M_jX_{k-j}\right].\quad}
\tag{8.3}
$$
证明中最高角导项仍由同一个真实 $G$ 求解；其余项都是低阶
已知量，零 Dirichlet trace 也与角差商交换。先以平滑近似证式，
再用差商的弱紧致性得到有限正则提升。因此 (8.3) 是一个明确
有限递推，而不是在高 Sobolev 档要求 $C-I$ 小的 Neumann 展开。
例如，取
$$
A_0=L_G,\qquad
A_k=L_G\left[1+\sum_{j=1}^k{k\choose j}M_jA_{k-j}\right]
\tag{8.4}
$$
便有 $X_k\le A_k\max_{0\le j\le k}F_j$。
非整数中间档可在这些已付整数档间插值；负档须对同一个真实
adjoint 使用上述估计后作对偶。加权情形的 adjoint 对应相反
符号权，所以正负权门都要验证。

这给正组件的有限角正则费用。full DN 的 source/contact 仍使用
R35 的完整 Green 公式；不因提升正则而删除其源积分项或跨端项。

## 9. 有限多个实际组件的接线范围

设实际型别证书给出有限多个简单 roots，且每个所用 root 满足
R36 的非特征门。对每个负组件分别进行两端的 §5 传播和内部
严格双曲传播；对每个正组件分别使用其真实完整 DN/Robin 实现。
不能把隔在两个负组件之间的正区间改成两个彼此独立的半线阻抗。

在所有真实端口都已变到一致 Green 归一以后，记负组件完整
scattering 的直和为 $S$，正组件完整 Cayley 的直和经实际端口
排列后的算子为 $R$。包含源和接触项的方程为
$$
y=Sx+s,\qquad x=Ry+h,
\qquad
\boxed{\quad (I-RS)x=h+Rs.\quad}
\tag{9.1}
$$
$s,h$ 包括每一个 ordinary source 的真实传播、正组件 contact
以及给定端数据。若有实耦合、多个帽、全局 mean 或刚体条件，
必须同时加入 (9.1) 的实际有限约束，不把它们压成某一个 root 的
Fourier 常数。

例如，若一个实际曲率在正半轴依次发生三次简单变号，且关于中点
偶对称，负区为中央一个环带及左右各一个外环，那么共有三个负
组件和六个 root 端口。两个中间正区间各贡献真实 $2\times2$
端口 Cayley，两个外正区各贡献实际终端实现。即使中央组件的
返回及完整相位已经可逆，也还没有支付另两个负组件及其全网
耦合的 (9.1)。这是接线的确定性事实，不以浮点型别扫描代替实际
root 证书。

当 $I-RS$ 在声明的源域、gauge 和有限约束下有真实双向逆，且
每个局部实现有本文和 R32/R35 的唯一性时，局部解按完整 height
及相反 outward conormal 接合，准确给全域弱 PDE 解；反之全域
解切开必满足 (9.1)。这只是带全部条件的等价，没有在本文构造
那个尚欠的全网逆。平帽边缘、极点和多帽相对刚体条件仍用本题
实际接口单独处理。

## 10. 到完整有限阶相位及高频逆仍须支付的输入

本文已独立支付了 simple-turn 实正规化、含均值的完整
Airy–Volterra Cauchy、ordinary source 和正组件的有限角
bootstrap。要使用邻题 R499 的后续结构，至少还需下列**实际
候选上的**输入。

1. **足够阶的真实系数表。** 按最终 source、Sobolev 窗口和所需
   余项增益先选有限阶；验证所有 reciprocal、短流、cut trace
   和实际参数导数。有限阶径向 spline 不自动有直接 log 或角
   解析延拓，mixed 逆坐标也不能送到非解析的复径向变量上。
2. **完整 finite root columns 的实际 residual。** 需要同时估计
   height、完整 momentum、正侧截断 Ai 试解，以及其回到物理
   source 空间后的算子 norm。单列 $L^2$ 数字不等于全 Fourier
   算子界；本篇的 (5.11) 也不是任意阶余项。
3. **同一个 full positive DN 和共同 Gram。** 必须从真实正侧
   解与完整 source contact 得到 Ai defect，保两端 cross、常数
   ground-state 和真实边界 shear；然后才可验证两支的共同
   Gram 及 true $J$-polar normalization。
4. **高切与真实低块。** 若已单独证明某个真实根 frame 在所需
   较低输入档满足 $L_N-I:H^{s-4/3}\to H^s$，norm 为
   $C_{s-4/3}$，那么
   $$
   \|(L_N-I)\Pi_{>J_0}\|_{H^s\to H^s}
   \le C_{s-4/3}\langle J_0\rangle^{-4/3}
   $$
   可通过增大 $J_0$ 变小；这不要求 $C_{s-4/3}$ 本身小。只给
   $H^s\to H^{s+4/3}$ 的一档 bound 并不足以得到这个右侧高切式。
   但若要改动
   高切，须保原固定 reference/frame 的一致性。该式完全没有
   证明真实有限低块可逆；低块、核、gauge 和有限增广需另付。
5. **全部负组件的完整 strict transfer 与 symbol。** 必须带
   实际低阶势、幅度、Maslov 常相位、$|D|^{-1}$ 和
   $|D|^{-2}$ 系数，以及达到所需强范数的真实 smoothing
   remainder。主特征返回的 Diophantine 性只处理主 transport，
   不会删除 R34 的完整相位算术门。
6. **全网络的真反馈逆及 Newton 费用。** 将各组件的高低频与
   cross 相接，验证 (9.1) 而不是其中一个对角块。再按 R37
   支付 metric-defect 因子的有限阶损失、重建、固定握持区及
   二次项，才能进入本题精确等距修正。

以上是明确的迁移边界，不是把 R499 的原小振幅结论当作本题
当前有限幅候选的定理。局部 real Sobolev 传播在这里已经闭合；
本题 README 所需的闭曲面精确族、可见位移和 reach 预算仍以
最终全链严格证书为准。

## 11. 来源及可独立核查的范围

本文只从标准 Airy 初值、Wronskian、有限实 ODE 和散度变换出发
证明 §§2–8 的声明，常数在式 (3.5)、(4.3)、(5.1)、(6.13)、
(7.3)、(8.3) 中给出。标准 Airy 恒等式的公开 primary 来源是
[NIST DLMF §9.2](https://dlmf.nist.gov/9.2)。

研究时核读了邻题
[R492 §§3–4](../../continuous-flexibility-swarm/results/R492-updated-background-fixed-type-input.md)
和
[R499 B §§0–9](../../continuous-flexibility-swarm/results/R499-updated-fixed-type-fhl-m3-high.md)
的 root coordinate、完整 source、finite columns、common Gram
和实际端口接口。它们解释 §10 中哪些输入是后续方法真正需要的；
其原全局小量、材料 uniformity 和实际全域实现没有被省略后引用。
