# 已证明：同一点有符号间隙的输运与降阶全 WUA.13

本文使用 [WUA.4–16](R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md) 的同一真实负侧和同一隐式 $\delta_*$. 所有径向微分都是原实际片上的单侧微分，$D=\partial_r-d\partial_\phi$，$b=\eta\sqrt{-K}>0$。下文 $r\le c$，$c=76285779072683/320000000000000$；原根片仍在 $c$ 的另一侧。结论是可直接计算的等式及阶数，没有给沿路数值上界。

## 从物理截面出发的真标签

令 $t=c-r$，$h_\sigma(0,z)=z$，$\partial_t h_\sigma=(d+\sigma b)(c-t,h_\sigma)$，$\sigma=\pm1$。设 $P^c_\sigma=X(c,\cdot)-\sigma\omega(c,\cdot)$，其中 $\omega=2(-T)^{3/2}/3$。真实根标签恰是
$$
 P_\sigma(r,\phi)=P^c_\sigma(h_\sigma(t,\cdot)^{-1}(\phi)).
$$
这是 WUA.4 真实流在 $c$ 的组合律。由于 $\partial_z h_\sigma=\exp\int_0^t d_\phi(c-u,h_\sigma(u,z))du>0$，逆在统一提升上唯一。$P^c_\sigma$ 可以直接按有符号根级数读取，不需要在 $c$ 求逆。标签角单项 $e^{inP_\sigma}$ 始终使用真相位。

设 $p_\sigma=\partial_\phi P_\sigma$，$x=(p_++p_-)/2$，$v=\omega_\phi$。第三个提升 $h_0$ 满足 $\partial_t h_0=d(c-t,h_0)$，$h_0(0,z)=z$。由 $D\omega=-bx$ 有
$$
 \omega(c-t,h_0(t,z))=\omega(c,z)+\int_0^t b(c-u)x(c-u,h_0(u,z))du .
$$
积分核为正；同一等式的标记角微分给出相关的物理角导数，方法是先微分积分和 $h_0$，再合成 $h_0^{-1}$ 的导数。这对任意有限角阶成立，因为每个原片上的角微分连续且在闭片上有界，实际径向分片有限。$p_\sigma=x-\sigma v$。这样可在原速度差远小于单个角格宽时直接围住 $\omega,v$；未把两个独立角格之差当有符号速度。

## 波算子的有符号链式公式

写 $B=D^2-b^2\partial_\phi^2$，$k=Dd_\phi+d_\phi^2$，$m=b_r+3b d_\phi$。由 $(D-\sigma b\partial_\phi)P_\sigma=0$ 及 $[D,\partial_\phi]=d_\phi\partial_\phi$，
$$
 DP_\sigma=\sigma b p_\sigma,\quad
 BP_\sigma=\sigma(b_r+b d_\phi)p_\sigma,\quad
 Dp_\sigma=\sigma b\partial_\phi p_\sigma+d_\phi p_\sigma ,
$$
$$
 Bp_\sigma=\sigma m\partial_\phi p_\sigma
             +(\sigma b d_{\phi\phi}+k)p_\sigma .
$$
最后一式来自对 $Dp_\sigma$ 再施 $D$ 并减去 $b^2\partial_\phi^2p_\sigma$。取半和与有向半差即得下表，所有量处在同一物理角。

| $f$ | $Df$ | $f_\phi$ | $Bf$ |
| --- | --- | --- | --- |
| $\omega$ | $-bx$ | $v$ | $-(b_r+bd_\phi)x$ |
| $x$ | $-b v_\phi+d_\phi x$ | $x_\phi$ | $-m v_\phi-bd_{\phi\phi}v+kx$ |
| $v$ | $-b x_\phi+d_\phi v$ | $v_\phi$ | $-m x_\phi-bd_{\phi\phi}x+kv$ |

对每个量存 $(f,Df,f_\phi,Bf)$。乘积和标量复合的第四槽分别为
$$
 B(fg)=g Bf+f Bg+2(DfDg-b^2 f_\phi g_\phi),\qquad
 B(F(f))=F'(f)Bf+F''(f)((Df)^2-b^2 f_\phi^2).
$$
第一式直接用 Leibniz 公式；第二式对两个二阶导数分别用链式法则。取 $s=(3\omega/2)^{1/3}$，$C=(k_*/\eta_*)^{1/6} q^{-1/2}E_G$，$G=C(3\omega/2)^{1/6}$。径向 $C$ 的四槽为 $(C,C_r,0,C_{rr})$；其在 $c$ 的值还可由任一固定实角的 $G(c)/(3\omega(c)/2)^{1/6}$ 读取。因 $T=-s^2$、$y=T_\phi=-v/s$，WUA.10 的两行为
$$ a=G(x^2+v^2),\qquad w=2i\epsilon Gxv/s . $$
用上述四槽积/幂分别计算 $Ba,Bw,Da,Dw$ 即已消去三阶标签导数。

具体设 $\mathcal D=(x-v)(x+v)$，$\mu=b^2\mathcal D/s^2$，$DX=-bv$，$DT=bx/s$。置
$$ (h_0,h_1)^t=H_D(a,w)^t,
\qquad (u_0,u_1)^t=
 (yT h_1-i\epsilon x h_0,\ y h_0-i\epsilon xh_1)^t/\mathcal D .$$
这是 $H^{-1}H_D(a,w)^t$，因为 $K_T^2=T Id$，$\det H=-\mathcal D$。于是完整有符号源是
$$
 (F_b,F_a)^t=-\mu^{-1}
 \left[(Ba,Bw)^t-T_0(Da,Dw)^t+V_0(a,w)^t-\vartheta(u_0,u_1)^t\right].
$$
原 $\vartheta$ 项、$\epsilon=\operatorname{sgn}j$ 和两真实方向均保留。求此源的 $j$ 阶角导，$x_\phi,v_\phi$ 至多要求真实标签 $j+2$ 阶；$d$ 最多 $j+2$ 阶角导及 $\partial_r\partial_\phi d$ 的 $j$ 阶角导。其余原始系数各按该表达式求真实 $j$ 阶角导。特别 $j=6$ 需要标签至 8 阶。若用共同流积分 $\omega$ 本身至 8 阶，该积分要 $x$ 至 8 阶，故整个方案仍保留标签至 9 阶。

在每条 $h_\sigma$ 上，WUA.16 的比值 $R_\sigma=v_{1,\sigma}/v_{0,\sigma}$ 的向内导数为
$$
 -\frac{b (x+\sigma v)}{s}\,
 \frac{F_a/2-i\epsilon\sigma F_b/(2s)}{G(x-\sigma v)^2}.
$$
由 $DT-\sigma bT_\phi=b(x+\sigma v)/s$ 和 $dt=-dr$ 得负号。起点是实根级数 $R_\sigma(c,z)=(a_1+i\epsilon\sigma s b_1)/(G(x-\sigma v)^2)$，其中 $a_1,b_1$ 使用对应频率符号的 WUA.16 解。每段按同一定向积分，角求导至 6 阶。原行跳跃、物理平均方程、全正侧匹配和响应仍须另算。此恒等式不授任何一项全频响应上界。
