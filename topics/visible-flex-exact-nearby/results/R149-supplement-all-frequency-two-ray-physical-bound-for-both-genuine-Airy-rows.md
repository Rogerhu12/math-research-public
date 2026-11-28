# 全负域两个真实 Airy 状态行的物理傅里叶范数

保留 WUA 的实际 $\Psi_n=F_n Z_n$、原根剪切 $C_n$、两独立参考输入、$P_\pm=X\mp\omega$ 与原物理角周期 $\pi/2$。令 $\rho=r_*-r$，$S$ 为满足 $n=4|j|\ge N\ge388$ 的任意输入集合。令
$$
 l(\rho)=\min(5\rho/2,1/20),\qquad b_N(\rho)=(1+N^{2/3}l(\rho))^{-1/4}.
$$
下列算子将 $\ell^2(S;\mathbb C^2)$ 映到完整归一化 $L^2_\phi$：
$$
 \mathcal Y_k f=\sum_{j\in S} e^{4ijX(r,\phi)}
       n^{-k}[\Psi_n(T(r,\phi))]_{k+1,:} f_j,\qquad k=0,1.
$$
原实 $|\delta|\le10^{-8}$、同一固定 $\eta_0$ 上有
$$
 \|\mathcal Y_0\|\le36 b_N(\rho),\qquad
 \|\mathcal Y_1\|\le160 b_N(\rho).                                     \tag{GAF.1}
$$
普通 $dr$ 的 $L^2_rL^2_\phi$ 接收分别小于 $40N^{-1/6},176N^{-1/6}$。没有按频带宽度计数，也没有忽略低输出、物理均值或两输入列的相位关系。这里的两个状态行是原高度及原 $T$ 导数除以 $n$；其他物理幅须按原矩阵顺序接入。

## 同一物理圆上的光学长度范围

置 $u=-T$。在 $0\le\rho\le1/50$，由 $u=\rho A^{2/3}$、$A>4$ 得 $u\ge5\rho/2$；其后由全域共同漂移的正性，$u>1/20$。因此在整个 $0\le\rho\le r_*<1/4$，有 $u\ge l(\rho)\ge\rho/5$。[GDG.5–9](R133-supplement-complete-global-genuine-determinant-from-supported-potential.md)

原整件 WGS（72251 bytes，SHA256 8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e）中 complete_strict_phase_angular_orders_1_through_15 首项 $<27$，strict_phase_lower $>1/27$，complete_jets.t.group_upper 首项 $<19$。根窗由原 M.8 与双分支角导门给更强界。因此 $p_\pm=P_\pm'\in(1/27,27)$，$X_\phi$ 也在此区间，且 $u<19$。沿真实共同漂移，零根值的 $\omega$ 是 $b X_\phi$ 的积分，其中 $b=\eta\sqrt{-K}>0$ 为同一径向函数。用相同的 $\int_0^\rho b$ 同时上下夹住各角得
$$
 0<u_{\min}\le u_{\max},\qquad
       u_{\max}/u_{\min}\le(27^2)^{2/3}=81\qquad(\rho>0).            \tag{GAF.2}
$$

## 精确两相位及只需一阶的对数变差

沿用 [AHD.3–4](R149-supplement-full-Airy-matrix-correlation-and-integrated-Darboux-source.md)，$s=\lambda u,\lambda=n^{2/3}$，
$A=\operatorname{Ai}(-s),B=\operatorname{Bi}(-s),m=A^2+B^2,\ m_1=A'^2+B'^2$，此处撇号对 $s$。将 $(A,B)$ 写为 $\sqrt m(\sin\theta,\cos\theta)$，取任意连续真提升。Wronskian 给 $\theta'=1/(\pi m)$。从 $\theta$ 扣 $2s^{3/2}/3$ 得 $\delta$。同样将 $(A',B')$ 写为 $\sqrt{m_1}(\sin\theta_1,\cos\theta_1)$，由两条 Airy 方程有 $\theta_1'=s/(\pi m_1)$；记 $\delta_1=\theta_1-2s^{3/2}/3$。两相位解调都在包括零点的真轴上逐点成立；不需猜测提升常数。

令 $g(s)=\pi\sqrt s\,m(s)$。在 AHD.3 中换元 $v=st$ 后用 $1-e^{-w}\le w$ 及 $\Gamma(7/2)=15\sqrt\pi/8$ 得
$$
 1-5/(32s^3)\le g(s)\le1 .
$$
对 AHD.3 在被积式中积分 $\partial_t(\sqrt t\,e^{-st-t^3/12})$，得 $0\le-sm'/m\le1/2$。当 $s\ge1$，
$0\le s\delta'=s^{3/2}(g^{-1}-1)\le5/27$。当 $s\le1$，$m(s)\ge m(1)$ 给 $0\le s\delta'\le s(32/27-\sqrt s)<1/4$；多项式最大值 $4(32/27)^3/27<1/4$。于是 $h_\pm(s)=\sqrt m\,e^{\pm i\delta}$ 满足 $|s h_\pm'|\le |h_\pm|/2$。

对伴随行，$m_1=sm+m''/2$，$m_1'=-sm'$。AHD.3 的正测度给 $m''\ge0$，故 $0\le s m_1'/m_1\le1/2$。Wronskian 给 $m_1\ge1/(\pi^2 m)\ge\sqrt s/\pi$，因此 $\delta_1'\le0$。在 $s\ge1$ 时，对 AHD.3 求两次导并去掉 $e^{-t^3/12}$ 得 $m''\le3/(4\pi s^{5/2})$，从而 $\pi m_1\le\sqrt s(1+3/(8s^3))$，$s|\delta_1'|\le3/8$。在 $0\le s\le1$ 时，AHD.4 与 $\pi m\ge27/32$ 给 $\pi m_1\le128/81$，故 $s|\delta_1'|\le s^{3/2}(1-81\sqrt s/128)\le47/128<3/8$。$k_\pm=\sqrt{m_1}e^{\pm i\delta_1}$ 满足 $|s k_\pm'|\le5|k_\pm|/8$。

对 $m(0)$ 的积分在 $t=2$ 分开，前段小于 $2\sqrt2$，后段以 $e^{-t/3}$ 界得小于 $3e^{-2/3}<2$，二者之和小于 $\pi^{3/2}$。结合 $m(s)\le1/(\pi\sqrt s)$ 及刚证的 $m_1$ 上界，得
$$
 |h_\pm|\le2^{1/4}(1+s)^{-1/4},\qquad
 |k_\pm|\le(1+s)^{1/4}.
$$
给定 $r$，所以 $|h_\pm|\le 2^{1/4}b_N$，
$n^{-1/3}|k_\pm|\le\sqrt{N^{-2/3}+u_{\max}}\,b_N<\sqrt{20}\,b_N$。

## 整个真传播与可积径向费

恒等式 $2s^{3/2}/3=n\omega$ 表明每个三角行与 $e^{4ijX}$ 相乘，恰为 $e^{4ijP_+}$ 与 $e^{4ijP_-}$ 的和。每支常数行的范数为 $1/\sqrt2$，依据 $\operatorname{sgn}j$ 切换行的符号或次序只是在原输入上的定长对角。导数状态行另有整体符号和 $n^{-1/3}$。真实 $Z_n(-u)$ 始终在这两行右边。

在每个非根物理圆，任一带号幅 $a_j(u)$ 可在 $[u_{\min},u_{\max}]$ 写为左端值加 $\int{\bf1}_{u(\phi)>v} a_j'(v)dv$。每个 $v$ 的行是频率对角，其后依次是真 $C_{P_\pm}$ 与公共物理指示乘子。换元给 $\|C_{P_\pm}\|<\sqrt{27}$。WUA.21 给 $\|Z\|<6/5$；AHD.5 的逐点主函数还给
$$
 \int_0^\infty \sup_{n\ge N}\|\partial_v Z_n(-v)\|dv
 \le {6 M\over5N}\int_0^L c(v)v^{-1/2}dv<13/N.
$$
故两支之和的费用至多 $\sqrt{54}\, b_N C [\,\frac65(1+D\log81)+13/N\,]$，其中高度行 $(C,D)=(2^{1/4},1/2)$，导数行 $(C,D)=(\sqrt{20},5/8)$。用 $\log81<9/2$、$\sqrt{54}<15/2$, $\sqrt{20}<9/2$, $2^{1/4}<6/5$ 即得 (GAF.1)。在 $\rho=0$ 直接用 $u=0$ 的两个常数幅与 $Z_n(0)=C_n$，没有对零取对数。有限输入稠密给任意无限 $S$ 的结论。

最后 $\int_0^{r_*} b_N^2\,d\rho\le N^{-1/3}[\,2/\sqrt{125}+(23/100)\sqrt{20}\,]<(11/10)^2 N^{-1/3}$；在 $1/50$ 分段后，第一段使用 $\rho^{-1/2}$，第二段使用 $r_*<1/4$。这给所述普通径向两项费用，包括原根和全部严格格。物理负 Sobolev 阶、各非局部接收、零长度源与正区回馈仍使用各自真正的界。
