# 全负域 genuine 接缝的两个实际系数

在原修复族的一个严格负域接缝，括号为物理 $r$ 的右迹减左迹。令 $u,v$ 是原两物理场，$\Delta u=[u_r],\Delta v=[v_r]$，独立均值比 $m=[\eta_r]/\eta=\Pi\Delta v/\Pi v$。记 $q=\sqrt{-K}$、$b=\eta q$、$s=\sqrt{-T}$、$x=X_\phi$ 和 $t=\omega_\phi=-sT_\phi$。$q_\rho$ 沿原 $\rho=r_*-r$，$\beta$ 是漂移的原几何系数，$\ell=-2\beta uv$。置
\[
 B=2\beta(Kv\Delta v-u\Delta u)
     +m\{\beta(1+u^2-Kv^2)-q_\rho/(2q)\},\qquad
 C=\{-2\beta(v\Delta u+u\Delta v)-\ell m\}/\eta .
 \tag{GJS.1}
\]
则真实两参考列的共同向量为
\[
 [Dw_1^V]=[Dw_1]=\frac G2
 \binom{-i\epsilon(Bt/b+Cx)}
              {Bx/(bs)+Ct/s},\qquad
 j_n=(JP\,n^{1/6}\mathcal U_{n,\epsilon}^{\rm ext}([Dw_1]),0).
 \tag{GJS.2}
\]
其中 $D=\partial_r-d\partial_\phi$、$\epsilon=\mathrm{sgn}\,j$。原 PW/WUA 动力校正以相反有向原子接收试探状态的跳。零频只在实际的 $P$ 处投影，$m$ 在 (GJS.1) 的两处分量中出现。两原参考输入、原 $Z_n,C_n$、$J$ 和腰部输出仍按其原次序。本式覆盖真实势的支持、过渡和支持外。

## 有向跳对两个波方程的作用

令 $L=-D$、$S=u^2+Kv^2$、$d_\phi=-\beta P S$，$A=x^2+t^2$，$W=2xt/s$。在 [GFW.1](R149-supplement-signed-free-first-wave-and-correlated-genuine-potential.md) 的原记号中，$w_0=G(A,i\epsilon W)^t$，$\mathfrak A_0w_0=(f_a,i\epsilon f_b)^t$。物理侧迹满足
\[
 [Lb]=-bm,\qquad [Ld_\phi]=\beta P[S_r],\qquad
 [T_0]=m,\quad [V_0]=m b_0-[b_{0,r}],\quad [\vartheta]=C,
 \quad b_0=\beta(1-u^2-3Kv^2).
\]
这些等式用 $\eta=-\gamma\Pi v$、[J.2–14](R133-supplement-exact-first-forcing-seams-and-first-correction-jump.md) 的物理原系数。严格负域的两个紧支边界，$w=4096z^6(1-z)^6$ 接零，$w$ 及前五导消失。$K_\delta=e^{-\delta w}(K+\delta T_{\rm met}w')$ 的同一二阶导与 $q,q_r,q_{rr}$ 在该处连续；$\beta,\gamma$ 及本式所需的一阶导亦连续。内禀缓存切分在原同侧函数取迹。因此上述跳恒等式延续至整个严格负域。原多项式修复是分片常数，其一侧正阶导为零。

真光线给
\[
 Lx=bt'-d'x,\quad Lt=bx'-d't,\quad Ls=bx/(2s^2),\qquad
 LG/G=2\beta\Pi S+bx/(4s^3)-q_\rho/(2q),
\]
撇号表示物理角导。最后一式由 $G=E A_f^{1/6}(-K/\rho)^{-1/4}$、$A_f=s^3/\rho^{3/2}$ 和 $\rho LA_f=(3/2)(bx/\sqrt\rho-A_f)$ 直接得到。$G,s,x,t$ 的一阶 $L$ 导和所有角导连续。故
\[
 [L^2x]=[Lb]t'-\beta P[S_r]x,\quad
 [L^2t]=[Lb]x'-\beta P[S_r]t,\quad
 [L^2s]=[Lb]x/(2s^2),\quad
 [L^2G]/G=-2\beta\Pi[S_r]+[Lb]x/(4s^3).
\]
对 $GA,GW$ 使用乘积和链式法则。$[Lb]=-bm$ 消去各 $x',t',s$ 的输运微分项。$A,W$ 对 $(x,t)$ 都为二次齐次，故其余共同标量是
\[
 -2\beta[S_r]-[b_{0,r}]
  +m\{-2d'+2\beta\Pi S-q_\rho/(2q)+b_0\}=B.
\]
一增益项 $\vartheta Q\mathcal K$ 的原 $Q=b/s$ 则给
\[
 [f_a]/G=BA-C(b/s)TW,\qquad [f_b]/G=BW+C(b/s)A .
 \tag{GJS.3}
\]

令 $p_\sigma=x-\sigma t$，$M_\sigma=Gp_\sigma^2/2$。原真输运 $L_\sigma r_\sigma=F_\sigma=(-\sigma f_a+s f_b)/(2bGp_\sigma^3)$ 给 $[Dr_\sigma]=-[F_\sigma]$，因为真 $r_\sigma$ 值与切向导连续。由 $w_1=(i\epsilon\sum M_\sigma r_\sigma,\sum\sigma M_\sigma r_\sigma/s)^t$，两个分量分别是
\[
 i\epsilon\frac{t[f_a]-sx[f_b]}{2b(x^2-t^2)},\qquad
 \frac{x[f_a]-st[f_b]}{2bs(x^2-t^2)}.
\]
代入 (GJS.3)，以 $T=-s^2$ 消去同一 $x^2-t^2=p_+p_->0$，得到 (GJS.2)。这一步在两个真分支加和后消除了全部 $p_\sigma$ 分母和 $r_\sigma$ 值。原真势修正 $\mathcal B\mathcal K w_0$ 为 $C^1$，原 $z,Jb_2$ 连续，故 WUA.46–47 的完整状态跳恰为所列值。[WUA.46–49](R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md)

## 原全接口与可复用的已认证输入

逐一保留原 3070 个接口。2549 个原多项式内结点各用原 $\Delta u,\Delta v,\Pi\Delta v$。在其余 521 个同一原多项式上的细分点，物理 $r$ 一阶导的两迹相等，且上述内禀连续性适用；(GJS.1) 两量同时为零。按真实函数的双侧导得零，包括紧支边界，不使用相邻区间球重合。根处给原解析 germ 和原正侧端口，腰处给原终端；两者均不并入严格接缝。原 [全部四端点和跳](R133-supplement-actual-complete-global-genuine-waist-error-and-all-endpoints.md) 的数值记录完整保留。

原半径 $1/50$ 的 1079 个双侧真实结点已经有全 65 与 193 分量的导数差和独立均值，其中负侧 576 个。可按原整件读取有向均值及其原分量范数；[原跳量整件](R133-supplement-actual-first-Airy-seams-and-six-forcing-windows.md)。该旧 Airy 成果对其指定参考剖面成立；(GJS.2) 保留新的 genuine $\Psi_n$。在其余负侧结点，三次原片 $a_{3,i}h^3+a_{2,i}h^2+a_{1,i}h+a_{0,i}$ 的原斜率差为 $a_{1,i+1}-a_{1,i}-2h_i a_{2,i}-3h_i^2a_{3,i}$。中心与方向均在原共同二进制有理结点取此差，分别依真 $\alpha,\delta$ 相加，均值列只收一次。接缝传播没有径向长度因子。
