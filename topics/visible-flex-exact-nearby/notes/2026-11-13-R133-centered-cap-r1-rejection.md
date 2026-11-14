# R133：真实非零中心帽残差的首次完整拒绝

2026-11-13。该次计算完整覆盖 $[1,25/8]$，原 whole $\eta$、全部
primitive 尾、M64准确有限中心、所有物理 Fourier 输出以及 mean
均保留。935个闭径向盒是原898个系数盒与完整中心的三次多项式
接缝的共同细分。这里记录的是一个实际充分门的失败，不能据此
断言真实帽问题无解。

## 准确残差与无穷尾

令中心为 $(\widehat B,\widehat c)$，$C=C_0+c$，
$Q=(B^2+\ell c^2)/(C_0+c)$。非零模使用
$b_m=i\operatorname{sgn}(m)B_m$、$M=|m|$。完整中心残差是
$$
R_b/M=(b_r+2\beta b)/M-\gamma\ell c+\gamma Q,
$$
$$
R_c/M=(c_r+\beta(\ell+1)c-\beta Q)/M-\gamma b.
$$
mean $B$ 中心准确为零，mean $C$ 残差则是
$R_{c0}=c_0'+\beta(\ell+1)c_0-\beta Q_0$，没有省去。

计算保留 $Q$ 的完整 Neumann 多项式
$$
Q_J={B^2+\ell c^2\over C_0}
       \sum_{j=0}^{J}(-c/C_0)^j,\qquad J=3.
$$
它的所有有限 Fourier 卷积逐系数用 directed Box 算术完成。
每个系数先跨全部径向盒取最大绝对上界，最后求和；没有把
$\sum_m\sup_r$ 换成 $\sup_r\sum_m$。

设中心全域 $A_0$ 范数分别为 $B_*,c_*$，
$C_*\le\inf|C_0|$、$\Lambda\ge\max(1,\sup\ell)$，
$q=c_*/C_*<1$。无穷尾在同一全域范数中满足
$$
\|Q-Q_J\|\le
 {B_*^2+\Lambda c_*^2\over C_*}{q^{J+1}\over1-q}.
$$
该尾对 $R_b/M,R_c/M,R_{c0}$ 的费用分别乘
$\gamma_+$、$|\beta|_+/4$、$|\beta|_+$；即使低模也全部覆盖。

## 完整逆核与实际 DQ

使用已真正支付的全模式线性核，中心的固定点残差上界为
$$
\varepsilon\le H_{\partial}
 +{H_D\over\sigma_D}\|R_b/M\|_{\mathcal X_0}
 +\left({H_Dq_+\over\sigma_D}+{H_C\over\sigma_C}\right)
            \|R_c/M\|_{\mathcal X_0}
 +K_{c0}^{F}\|R_{c0}\|_{C^0_r}.
$$
内端非mean $c$ 准确取中心值。三个独立外端口预算各为 $10^{-8}$，
其中 $d_R$ 用 $A_2$ 预算；中心右迹与真正 R74 全频 Jacobi 线的
差另行支付，不假定准确为零。右端 mean 均保留。

对误差球 $\|W_B\|+\|W_c\|\le\rho$，令
$B_+=B_*+\rho,c_+=c_*+\rho,d=C_*-c_+>0$。完整非线性导数满足
$$
\|DQ\|\le\max\left\{
 {2B_+\over d},\quad
 {2\Lambda c_+\over d}+{B_+^2+\Lambda c_+^2\over d^2}
\right\}.
$$
这里使用两分量 $\ell^1$ 输入范数，故是两个偏导上界的最大值。
乘完整 Green 核 $K$ 得 $L$。实际 Banach 门应是
$L<1$ 和 $\varepsilon+L\rho<\rho$，两条都必须通过。

## 原生结果与失败身份

| 量 | 原生有向上界的外向显示 |
| --- | ---: |
| $B_*$ | $<0.001710807041$ |
| $c_*$ | $<0.001446821796$ |
| 无穷 Neumann 尾 | $<1.7968110\,10^{-13}$ |
| $\|R_b/M\|$ | $<0.000447984363$ |
| $\|R_c/M\|$ | $<0.000220890638$ |
| mean 残差 | $<2.807949\,10^{-6}$ |
| $\varepsilon$ | $<0.001983476358$ |
| $\rho$ | $0.002$ |
| $L$ | $<0.713068194$ |
| $\varepsilon+L\rho$ 的计算上界 | $0.003409612744>\rho$ |

因此本次没有给 $[1,25/8]$ 授证。无限尾已经很小；实际剩余预算
主要来自径向中心与宽目标盒的相关性损失。后续版本将共同微分
完整残差后作径向 Taylor，继续使用相同真实目标、同一中心和
同一误差半径；本次失败源码和完整 native 不改。

首次 v1 在任何数学门执行前遇到 `Box` 不支持 item assignment 的
API 异常，退出码1；原源码及小异常记录保留。独立 v2 改为显式
复制区间的 lower/upper 数组，并处理 scalar norm reduction。
它没有更改冻结的区间算术模块或上述公式。v2 才是本篇完整935盒
原生报告，不能将 v1 异常称为数学失败。

文件和完整输入/source/dependency SHA 在本结论 manifest 中逐项
记录。整个结果仍只针对驱动帽；body 两迹、真实 nonlinear regular
外尾及周期 holonomy 没有因一个线性坐标或外端小量被删除。
