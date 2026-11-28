# 两真列 Airy 行列相关与全负轴 Darboux 强迫的实数值界

沿用 [WUA.18–22](R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md)、[WES.10–23](R133-supplement-selected-free-waist-exact-scattering-and-complete-endpoint-comparison.md)。$L=1/2000$，$n=4|j|\ge388$，$\lambda=n^{2/3}$，$z=j^{-2}$。矩阵范数为两分量欧氏算子范数；所有估计对两输入列、两符号以及原公共实参数域成立。任意负轴端点 $T,S$ 的完整相对传播满足
$$
 \|\mathcal U_{\rm ext}(T,S)^{\pm1}\|<103/100,
 \qquad n\|\mathcal U_{\rm ext}(T,S)-Id\|<11 .                       \tag{AHD.1}
$$
全 Darboux 强迫 $H=\mathcal B_{\rm ext}''+V_{\rm ext}\mathcal B_{\rm ext}$ 和保原顺序的 scattering 积分满足
$$
 \int_{-\infty}^0|H(T)|dT <851000,\qquad
 \|\mathsf S_n \mathcal J_{n,\infty}\|<2^{20}n^{-2}.                   \tag{AHD.2}
$$

## 负轴自由两行的精确乘积

设 $A(s)=\operatorname{Ai}(-s), B(s)=\operatorname{Bi}(-s)$ 及 $m=A^2+B^2$。由 Airy 方程，平方、乘积均满足 $w'''+4s w'+2w=0$。有
$$
 m(s)=\pi^{-3/2}\int_0^\infty e^{-st-t^3/12}t^{-1/2}dt.              \tag{AHD.3}
$$
为验证，右端代入三阶方程所得被积式正比于 $\partial_t(4\sqrt t\,e^{-st-t^3/12})$，边界为零。对 $s\to\infty$ 换元 $v=st$ 与支配收敛给 $\pi\sqrt s\,m_{\rm RHS}\to1$。三个独立解 $A^2,AB,B^2$ 构成该方程基础组，因为 $A,B$ 的 Wronskian 非零。原 WES 使用的两支实 Airy 首项在同一角 $\theta=2s^{3/2}/3+\pi/4$ 给 $\pi\sqrt s$ 倍的这三解分别为 $\sin^2\theta,\sin\theta\cos\theta,\cos^2\theta$ 加趋零项。逼近三种不同的 $\theta\bmod\pi$ 即得满足上述极限的唯一线性组合为 $A^2+B^2$。

故 $0<\pi m(s)\le s^{-1/2}$（$s>0$），且 $|m'(s)|\le |m'(0)|$。由标准零点值 $\operatorname{Bi}(0)=\sqrt3\operatorname{Ai}(0)$、$\operatorname{Bi}'(0)=-\sqrt3\operatorname{Ai}'(0)$ 与 Wronskian 得 $m'(0)=-2/(\pi\sqrt3)$。保留同一 $s$ 的两行相关性，有
$$
 \pi\sqrt{(A^2+B^2)(A'^2+B'^2)}
 =\sqrt{1+(\pi m'/2)^2}\le2/\sqrt3.                                 \tag{AHD.4}
$$
这是两行模之积的最优整轴上界，$s=0$ 取等。$F_n^{-1}e_2[F_n]_{2,:}$ 的算子范数正是 (AHD.4) 左侧；缩放 $\lambda$ 因 Wronskian 准确消去。

## 紧支撑势的完整相互作用

写 $t=-T$, $c(t)=\chi_V(-t)$, $v(t)=V(z,-t)$，$a=L/2$。$c$ 在 $[0,a]$ 为一，在 $[L,\infty)$ 为零，$-c'$ 为 $[a,L]$ 中关于 $3L/4$ 对称的概率密度。令随机变量 $b$ 具有此密度。则
$$
 \int_0^L{c(t)\over\sqrt t}dt=2\mathbb E\sqrt b\le\sqrt{3L},
 \qquad \int_0^L c(t)dt=\mathbb E b=3L/4.
$$
[原完整势界](R133-supplement-actual-complete-common-radial-potential-and-root-piece-image.md) 给 $M=276,M_1=26431,M_2=3830956$ 分别控制 $v,v',v''$。WUA.20 的矩阵是两个真实自由高度向量构成的秩一积，因此
$$
 \int_{-\infty}^0\|\mathcal K_{\rm ext}(T)\|dT
 \le {M\over n}\int_0^L {c(t)\over\sqrt t}dt
 < {107\over10 n}.                                                     \tag{AHD.5}
$$
时间有序级数及逆序级数给 (AHD.1)：$x=107/(10n)<7/250$，$e^x\le(1-x)^{-1}<103/100$，且 $e^x-1\le x/(1-x/2)$。尤其 $\|(\mathsf S_n-C_n)C_n^{-1}\|<11/n$，保留了原非零根剪切 $C_n$。

## 全势导数积分和非零负尾

设 $F(t)=c(t)v(t)$，以零延拓到 $t\ge L$，$b_0(t)=\mathcal B_{\rm ext}(-t)=\int_0^1 F(h^2t)dh$。在 $0\le t\le a$ 有 $|b_0''|\le M_2/5$。对 $t\ge a$，精确关系 $2t b_0'+b_0=F$ 给
$$
 |b_0''(t)|\le {|F'(t)|\over2t}+{3\over2t}\int_0^1 h^2|F'(h^2t)|dh .
$$
第二项积分换元 $u=h^2t$ 后为 $\frac12\int_0^L {|F'(u)|\over u}\min(1,(u/a)^{3/2})du$。保留整条 $t\ge a$ 半轴，得到
$$
 \int_0^\infty |b_0''|dt
 \le {aM_2\over5}+{M_1\over3}
       +\int_a^L {|c'|M+c M_1\over u}du
 \le {LM_2\over10}+{5M_1\over6}+{3M\over2L}.
$$
最后用 $\int_a^L c=L/4$ 和 $u\ge a$；对概率密度 $|c'|$，凸函数 $1/u$ 不超过端点割线，而 $\mathbb E b=(a+L)/2$，故 $\int |c'|/u\le(1/a+1/L)/2$。再加 $\int|F b_0|\le3LM^2/4$，代入上述整数直接给 (AHD.2) 的第一式。$t>L$ 处实际 $b_0$ 的 $t^{-1/2}$ 尾已在换元积分中接收。

## 保留真实传播顺序的绝对接收

WES.21 中 $\Psi(T)^{-1}=Z(T)^{-1}F_n(T)^{-1}$。将固定左矩阵 $\mathsf S_n=Z(-L)$ 保持在积分左边，得真实传播 $Z(-L)Z(T)^{-1}=\mathcal U_{\rm ext}(-L,T)$。于是 (AHD.1)、(AHD.4) 给完整被积矩阵在乘 $H/n^2$ 前的上界 $(103/100)(2/\sqrt3)<6/5$。两根输入列及两个状态行一并保留。由 $(6/5)851000<2^{20}$ 得 (AHD.2) 余式，对任意输入频带均可直接作为对角矩阵估计。完整 WES.22 还含 $\mathsf S_nD_n^{\rm root}$；采用原 AD 首列共同右归一时，则保其对应的真正第二列和带号剪切差 $d_n$。物理幅与端点接收仍须照 WES.37–41 接入。


外部标准恒等式另核 NIST DLMF [零点初值](https://dlmf.nist.gov/9.2#ii)、[Wronskian 9.2.7](https://dlmf.nist.gov/9.2.E7)、[负轴渐近 9.7.9](https://dlmf.nist.gov/9.7.E9) 与 [9.7.11](https://dlmf.nist.gov/9.7.E11)（2026-11-28查阅）。本页对所用Laplace恒等式、相关乘积、完整势积分及原传播次序已给独立推导，未把外部渐近式当作有限参数误差界。
