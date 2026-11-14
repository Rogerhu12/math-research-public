# R133 补篇：最终 regular 端口的全模 L2 图和无导损 Hilbert 接线

2026-11-13。**已证明，完整有理预算实际执行，30 门全过。**
本篇在最终完整 moving 中心的真实 $R=25/8$ 端口上支付两个此前不同的门：
原非线性 long 图的导数延拓到完整 $L^2$ 方向；
以及原物理角 Hilbert–Robin 行到 moving 角的同阶接线。
未知 Fourier 尾、真实 mean 小根、外侧独立数据和原 regular 指数费全部保留。

实际中心 SHA256 是
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413。
本篇消费[实际最终端口](R133-supplement-final-moving-centre-actual-regular-boundary.md)
已经完成的完整端值/条带证书，不重做失联大数组。
下面的预算由可用 V8 中 BigInt 精确有理算术执行，不冒称恢复了 Arb 作业。

## 1. 原 long 强空间的真正 L2 module

原 [R119 完整 long 定理](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md)
使用先逐 Fourier 模径向 supremum、后 $\ell^1$ 的代数。
记

$$
 \|a\|_{\mathfrak A}=\sum_m\|a_m\|_{C^0_t},\qquad
 \|x\|_{\mathfrak M}=
       \left(\sum_m\|x_m\|_{C^0_t}^2\right)^{1/2}.
                                                               \tag{L.1}
$$

全部 mean 都包含在这两个定义中。完整卷积的 Young 不等式给

$$
 \|ax\|_{\mathfrak M}\le\|a\|_{\mathfrak A}\|x\|_{\mathfrak M}.
                                                               \tag{L.2}
$$

这里最后的 $\ell^2$ 确实在逐模径向 sup **之后**，没有换成
$\sup_t\ell^2$。固定背景始终在 $\mathfrak A$；方向才在 $\mathfrak M$。

对非mean高度方向定义

$$
 \|h\|_{\mathcal Y_2}=
 \left[\sum_{m\ne0}
 \left(|m|^2\|h_m\|_\infty+
       |m|\|h_m'\|_\infty+\|h_m''\|_\infty\right)^2\right]^{1/2},
 \quad
 \|f\|_{\mathcal F_2}=
 \left[\sum_{m\ne0}\|f_m\|_\infty^2\right]^{1/2}.        \tag{L.3}
$$

原逐模完整 Green 核已经给
$|m|^2\|H_m\|_\infty+|m|\|H_m'\|_\infty+\|H_m''\|_\infty
<32\|F_m\|_\infty$。因此它在 (L.3) 中仍有范数小于 32。
原真正两端 lift 同样逐模给

$$
 \|h_D\|_{\mathcal Y_2}
 \le5\|f_B\|_{\dot H^2}+3\|f_*\|_{\dot H^2},
 \qquad
 \|f\|_{\dot H^2}^2=\sum_{m\ne0}|m|^4|f_m|^2.           \tag{L.4}
$$

不能从一个抽象 $\ell^1\to\ell^1$ 常数推出这些式子；
这里使用的是原先已经证明的逐模正核和实际两端 lift。

严谨地，把 $\mathfrak A\oplus\varepsilon\mathfrak M$ 定义为平方零扩张：

$$
 (a,\xi)(b,\zeta)=(ab,a\zeta+b\xi),\qquad
 \varepsilon^2=0,\qquad
 \|(a,\xi)\|=\|a\|_{\mathfrak A}+\|\xi\|_{\mathfrak M}.
                                                               \tag{L.5}
$$

(L.2) 说明它是交换 Banach 代数；mean 读取、非mean 投影和径向积分
在其中保持原范数界。逆级数和平方根级数仍收敛于相同的球。
所以原 holonomy 方程的真实小根 $\mu(h)$ 在此代数中也有唯一小根；
其 $\varepsilon$ 分量就是 $D\mu[h]$，没有把它设零。

原 long 的准确非线性式、$\|\mathcal Q(h)\|\le512\|h\|^2$、
两端核和收缩可逐项在 (L.5) 中重做。每个背景乘方向的项由 (L.2)
控制；两个方向之积准确为零。对有限 Fourier 方向，唯一性使这个
$\varepsilon$ 分量与原真解图的导数一致。有限方向在 (L.3) 稠密，
于是得到唯一的有界完整 $L^2$ 导数延拓。

这证明的是实际小背景上真实导数的延拓，
**不是**任意 $L^2$ 非线性输入球的存在定理。

## 2. 真 curvature 图的 L2 导数，包括两个 mean

沿用[实际正帽—long 接合](R133-supplement-actual-positive-cap-and-periodic-long-tail-matching.md)
的原物理角和准确公式。记
$Z=(C-C_{\rm ref})_{\ne0}$，
$\|Z\|_{A^0}\le r_Z$，
$\|f_B\|_{\dot A^2}\le r_B=2^{-60}$，
$r_f=10(r_Z+r_B)$、$F=r_f+r_B$。
固定的背景是真 long 解，满足 $\|h\|_{\mathcal Y_1}<6F$。

原余项在平方零代数仍有

$$
 \|\mathcal R_C\|\le R_CF^2,\quad
 \|\mathcal R_D\|\le R_DF^2,\quad
 |c_0|\le R_0F^2,\qquad
 R_C=2^{12},\ R_D=2^{14},\ R_0=2^{11}.                 \tag{L.6}
$$

为核导数常数，在 $\mathfrak M$ 单位方向上取复数参数圆盘
$|\epsilon|\le F$。扩张代数的完整输入 norm 小于 $2F<2^{-25}$，
故同一二次界给
$\|D\mathcal R_j\|_{\mathfrak M}\le4R_jF$。
这是在新 Banach module 中重证 Cauchy 估计，没有把旧 $A^0$ 导数
无理由地转授为 $L^2$ 导数。

真实 $\mathcal L_C^{-1}:L^2_{\ne0}\to\dot H^2$ 是逐频乘子，范数小于9。
令

$$
 \kappa_C=36R_CF,\qquad J_f=\frac9{1-\kappa_C}.          \tag{L.7}
$$

原完整 regular 与有限长反射费允许取一个共同的严格正上界

$$
 \epsilon_q<\epsilon,\quad\epsilon_s<\epsilon,\qquad
 \epsilon=2^{-512}.                                   \tag{L.8}
$$

这是由真实 $L>2^{24}$ 和原指数界得出的较粗有理费用；
没有把原指数小量置零，也不依赖第四模的误差必须准确为零。

完整真实端口写成

$$
 J_\theta B+Q_\theta Z=d(Z,f_B),\qquad
 C_0-C_{\rm ref}=c_0(Z,f_B),\qquad B_0=0,              \tag{L.9}
$$

其中 $J_\theta$ 的 Fourier 乘子是 $i\operatorname{sgn}(m)$，
$Q_\theta$ 是真实 $q_m$。这里的图导数是实际 nonlinear boundary residual 在该 $Z$ 输入处的导数：先用真正 long 解计算 $d,c_0$，再在最终有限中心的准确角图上拉回。它不假定有限中心的 $B$、mean $C$ 已经等于这两个输出；原非零边界 residual 仍保留。真实导数在完整物理 $L^2$ 上满足

$$
 \|D_Zf_*\|<J_f,\quad
 L_d:=\|D_Zd\|<\epsilon+4R_DFJ_f,\quad
 L_0:=|D_Zc_0|<4R_0FJ_f.                              \tag{L.10}
$$

独立 $f_B$ 方向以 $\dot H^2$ 量度；不能删除这个输入。准确可取

$$
 J_B=\frac{\epsilon+\kappa_C}{1-\kappa_C},\qquad
 \|D_{f_B}f_*\|<J_B,
$$
$$
 \|D_{f_B}d\|<\epsilon+4R_DF(1+J_B),\quad
 |D_{f_B}c_0|<4R_0F(1+J_B).                           \tag{L.11}
$$

真实小根 $\mu$ 的方向分量参与 (L.6)–(L.11) 的全部二次/余项。
独立整体 mean 高度仍是自由平移；mean 高度差及两端 mean slope 仍由
原 $\mu$ 积分输出。$B_0=0$ 只来自整个偶/奇反射类，不能借此清掉
$c_0$ 或高度常数。

实际 $q_m>.9999999999993$ 全频成立；所以
$D_ZB=J_\theta^{-1}(-Q_\theta+D_Zd)$ 是全非mean
$L^2$ 同构。其逆范数小于 $(q_{\min}-L_d)^{-1}$。
实际有理预算为：

| 原定输入球 | $L_d$ | $L_0$ | $\|(D_ZB)^{-1}\|$ |
|---|---:|---:|---:|
| $r_Z=10^{-12}$ | $5.898255\,10^{-6}$ | $7.372818\,10^{-7}$ | $1.000005899$ |
| $r_Z=10^{-10}$ | $.000589911$ | $.000073739$ | $1.000590260$ |

最终候选的真实 $Z$ 已证明小于 $2.532986\,10^{-13}$，故属于第一球。
两种半径事先明确；没有按符号门循环选择半径。

## 3. 真角变换的 Hilbert 共轭不损导数

最终端口准确是 $\theta=\phi+\psi(\phi)$、
$j=\theta_\phi=v/m>0$。其已付连续条带范数为

$$
 \sigma=1/8,\qquad
 \|\psi\|_{A^0_\sigma}<P=1.480385\,10^{-11}.             \tag{L.12}
$$

令 $x=4\phi$、$\Theta(x)=4\theta(x/4)$，则
$\Theta'=j$。完整 Fourier 级数给

$$
 \epsilon_1=\|j-1\|_\infty\le P/\sigma,\quad
 \epsilon_2=\|j_x\|_\infty\le2P/(4\sigma^2),\quad
 \epsilon_3=\|j_{xx}\|_\infty\le6P/(16\sigma^3).         \tag{L.13}
$$

所用 $n!/\sigma^n$ 来自 $e^t\ge t^n/n!$，保留全部模。
实际 $\epsilon_1<1/4$。

设 $Tf=f\circ\theta$，$J_\phi=i\operatorname{sgn}(D_\phi)$，
$\mathcal K=TJ_\theta T^{-1}-J_\phi$。
并不声称 $T-I$ 在同阶 Sobolev 空间小。
对 $s=x-y\in[-\pi,\pi]$，$\mathcal K$ 的积分核除整体负号外是

$$
 \Delta(x,y)=j(y)\cot\frac{\Theta(x)-\Theta(y)}2
                         -\cot\frac{x-y}2.             \tag{L.14}
$$

定义
$R(s)=\cot(s/2)-2/s$，在 $s=0$ 取解析延拓。
在 $|s|\le5\pi/4$ 有

$$
 |R|<1,\qquad |R'|<1,\qquad |R''|<1.                  \tag{L.15}
$$

一个完全显式证明使用完整部分分式
$R(s)=-(s/\pi^2)\sum_{n\ge1}(n^2-(s/(2\pi))^2)^{-1}$。
把 $n=1$ 分离，余项分别用
$\sum_{n\ge2}n^{-2}<2/3$、
$\sum_{n\ge2}n^{-4}<5/48$（前者可取 $n=2,3,4,5$ 后用尾积分，后者取 $n=2$ 后用尾积分）；再用 $3<\pi<22/7$。
实际预算逐项核对以下三个有理上界小于1：

$$
 \frac5{12}\left(\frac{64}{39}+\frac{512}{693}\right),\quad
 \frac19\left(\frac{5696}{1521}+\frac{71936}{53361}\frac23\right),\quad
 \frac5{216}\left(\frac{888832}{59319}
                +\frac{793\cdot65536}{231^3}\frac5{48}\right).
$$

现在置
$A=\int_0^1j(y+ts)\,dt$。奇性准确相消成

$$
 2\left(\frac{j(y)}{\Theta(x)-\Theta(y)}-\frac1s\right)
 =-\frac2A\int_0^1(1-t)j_x(y+ts)\,dt.                 \tag{L.16}
$$

因此整个核在对角连续延拓，并有

$$
 |\Delta|\le
 K_0:=\frac{\epsilon_2}{1-\epsilon_1}
                         +(1+\pi)\epsilon_1.          \tag{L.17}
$$

对 (L.16) 再微分一次，并用 (L.15)，得到

$$
 |\partial_x\Delta|\le K_1:=
 \frac{\epsilon_3}{3(1-\epsilon_1)}
 +\frac{\epsilon_2^2}{2(1-\epsilon_1)^2}
 +(2+\pi)\epsilon_1+\epsilon_1^2.                      \tag{L.18}
$$

核是完整周期核，切换 $s=\pm\pi$ 的 lift 时两边准确一致。
故积分微分没有额外端项。归一化 $L^2$ 上的直接积分估计给

$$
 \|\mathcal Kf\|_{L^2}\le K_0\|f\|_{L^2},\qquad
 \|\partial_\phi\mathcal Kf\|_{L^2}\le4K_1\|f\|_{L^2}.
$$

于是对每个 $0\le s\le1$，

$$
 \boxed{\|\mathcal K\|_{H^s\to H^s}
 \le K_0+4K_1<7.190442\,10^{-9}.}                     \tag{L.19}
$$

所有 mean 也在这个完整算子估计内。它是真无穷空间的积分核界，
没有使用有限 Fourier 矩阵来外推。

## 4. weighted mean 与真正 Robin 行的范围

物理非mean 在拉回后满足 $\langle j w\rangle_\phi=0$，
而不必满足 $\langle w\rangle_\phi=0$。记这个偶空间为 $\mathcal E_j$。
$P_{\ne0,\phi}:\mathcal E_j\to\mathcal E_0$ 的准确逆是

$$
 z\longmapsto z-\langle jz\rangle_\phi.                 \tag{L.20}
$$

其 $H^s$ 范数不超过 $\sqrt{1+\epsilon_1^2}$，因为
$\langle jz\rangle=\langle(j-1)z\rangle$，常数与非mean在全部 $H^s$
中正交。用普通 moving 非mean 投影时，必须保留 (L.20)，不能删掉
这个 physical weighted mean。

因此奇 $L^2$ 到偶非mean $L^2$ 的完整 leading Robin 行

$$
 P_{\ne0,\phi}TJ_\theta T^{-1}
       =J_\phi+P_{\ne0,\phi}\mathcal K
$$

可逆；对全部 $0\le s\le1$，其逆范数小于
$1/(1-K_0-4K_1)<1.000000011$。

$T,T^{-1}$ 在 $0\le s\le1$ 的 $H^s$ 范数均不超过
$(1-\epsilon_1)^{-1/2}$。所以真实
$q_m-q_*$ 的完整乘子费经共轭最多乘
$(1-\epsilon_1)^{-1}$，仍保留原严格正指数费。
独立物理 mean 方程则仍是 (L.9) 的第二行，绝不通过 (L.20) 消除。

第2节已证明的 nonlinear derivative 范数是 $L^2$。
(L.19) 的更强同阶结论只授予 Hilbert 共轭本身；它没有自动把整个
nonlinear long DN 的导数升级为任意 $H^s$ 范数。

## 5. 完整 curvature 方向到 moving 状态的准确图

本节沿用实际完整实反射空间：$f,u$ 为奇函数，$g,v$ 为偶函数，均含全部允许角模；偶 mean 保留。零均值 primitive 规范下 $\langle vI(vg)\rangle=0$，故下面的角图微分无需另加常数旋转项。这是同一无限维反射空间的全 $L^2$ 结论。

设物理曲率方向拉回为
$f=\delta B\circ\theta$、$g=\delta C\circ\theta$。
固定物理角的 reciprocal 方向 $k$ 和真实 moving 方向 $h$ 准确满足

$$
 k_1=v f-uvg,\qquad k_2=-v^2g,\qquad
 h=k+Q_\phi I(k_2/v)=k-Q_\phi I(vg).                   \tag{L.21}
$$

这是反向角图的准确微分，不假定近似中心已经满足 PDE。
它的第二平均为

$$
 z:=\langle h_2\rangle_\phi
   =-m\langle vg\rangle_\phi
   =-m^2\,\delta C_0.                                 \tag{L.22}
$$

所以真正 cap mean 导数恰好产生非零的 moving mean 输出；
不能删掉这个状态。

原端口条带还给

$$
 \|u\|_{A^0_\sigma}<1.643190\,10^{-9},\quad
 \|v-m\|_{A^0_\sigma}<9.603792\,10^{-9},\quad
 |m|,|v|<7,\quad |m|,|v|>5.8.                         \tag{L.23}
$$

上界7可从原 $\omega<3/2,w<1/800000$ 和已证
$|C_0-C_{\rm ref}|<6.055\,10^{-43}$ 推出；程序也按有理式核对，
并不从采样 extrema 得到。令
$U_1=U_\sigma/\sigma,V_1=V_\sigma/\sigma$。
由 $I:L^2_{\ne0}\to L^2$ 的准确范数 $1/4$，(L.21) 给

$$
 \|h_1\|_2\le7\|f\|_2+7(U_\sigma+U_1/4)\|g\|_2,\qquad
 \|h_2\|_2\le(49+7V_1/4)\|g\|_2.                     \tag{L.24}
$$

把真实 graph 的
$\|\delta B\|_2\le(1+L_d)\|\delta Z\|_2$、
$\|\delta C\|_2\le(1+L_0)\|\delta Z\|_2$
及完整角测度费代入，两个明确半径下均得到

$$
 \boxed{\|h\|_{L^2_\phi}<50\|\delta Z\|_{L^2_\theta}.}  \tag{L.25}
$$

反向使用准确 variation bridge
$\chi=v^{-1}I(h_2-zv/m)$，
$k_2=h_2-v_\phi\chi$，
$g=-k_2/v^2$，有

$$
 \|\chi\|_2
 \le \frac{1+7/5.8}{4\cdot5.8}\|h_2\|_2,\qquad
 \boxed{\|\delta Z\|_{L^2_\theta}<.03\|h_2\|_{L^2_\phi}.}
                                                               \tag{L.26}
$$

(L.25)–(L.26) 的 forward graph 使用 fixed $f_B$ 的 homogeneous
方向。独立 $f_B$ 的非齐次列依 (L.11) 保留并加进 (L.24)；
它没有被设为零。独立 mean 行数据与整体高度同样单独保留。

例如小球中由 (L.22) 的实际 mean 输出系数小于
$.000036126808\|\delta Z\|_2$；原 $10^{-10}$ 球的系数小于
$.003613205\|\delta Z\|_2$。二者都不是零。

## 6. 计算、身份和剩余真正接口

源为
[scripts/fourfold_codazzi_final_regular_L2_Robin.mjs](../scripts/fourfold_codazzi_final_regular_L2_Robin.mjs)；
完整报告为
[30 门有理预算](../notes/2026-11-13-R133-final-regular-L2-Robin-rational.json)。
同一完整预算函数已在 V8 实际执行，所有30门通过；Node CLI 可重放相同
BigInt 运算。它消费已发表完整 endpoint/long/regular 定理中的明确有理
外包，不声称重新运行任何原 native 或恢复完整候选数据。

本篇使最终实际外端的全模线性图、weighted mean 和 moving 状态端口成为
可消费对象，供真实体区正型两端逆和 $\nu$ 标量 Schur 使用。
真正远端 label 方程
$k_B(a)+C_Lf_B(a)-S_Lf_*-E_D(f_B(a),f_*)=0$ 仍须联立。
体区全反馈、独立 $\nu$ scalar 非零、全闭面与可见弯曲目标没有由这个
外端定理自动完成。
