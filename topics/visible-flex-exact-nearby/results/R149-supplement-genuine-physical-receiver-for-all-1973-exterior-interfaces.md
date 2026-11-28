# 原负侧外部 1973 个接缝的两列物理接收

取原所选真实族 $|\delta|\le9368259853002/10^{23}$、原 $\eta_0$、$n=4|j|\ge N=388$，以及原负域多项式结点 $k=1973,\ldots,1$。每一项是从本结点到物理腰的点源。其余 $1974,\ldots,2549$ 由 [AGJR](R149-supplement-actual-all-576-genuine-root-window-interface-operators.md) 给出，另外 521 个同一多项式分点的有向跳精确为零。所有 $k\le1973$ 满足 $r_*-r_k>1/50$，故 $u_T=-T>1/20$，$V_n(T)=0$，$Z_n(T)=Z_n(-1/2000)$ 为整个物理圆上同一频率矩阵。[GAF](R149-supplement-all-frequency-two-ray-physical-bound-for-both-genuine-Airy-rows.md)

## 真实接缝幅

原 65 与 193 分量的斜率差分别取
$a_{1,k}-a_{1,k-1}-2h a_{2,k-1}-3h^2a_{3,k-1}$。每项先用原二进有理共同结点及两侧系数完成相减，再乘相应的 $\alpha,\delta$。$u,v$ 本身取原 $\alpha$ 中心、完整值修复、193 方向和 $v$ 的原独立背景。$m=\Pi[v_r]/\Pi v$ 在两个有向系数中保留。以下 $S,C$ 指 [GJS.1](R149-supplement-two-signed-coefficients-for-every-genuine-negative-interface.md) 的 $B,C$，其中 $-q_\rho/(2q)=K_r/(4K)$。置 $x=X_\phi,t=\omega_\phi,s=(3\omega/2)^{1/3},y=-t/s,T=-s^2$，$b=\eta\sqrt{-K}$。两分支合成的真正跳向量为
\[
 w=\tfrac12G\big(-i\epsilon(St/b+Cx), (Sx/b+Ct)/s\big)^t .
\]
相位、光学间隔及其到三阶的原物理角导，在同一闭结点由整件 GPR 的连续比较与原有向误差获得。保留原 $p_\pm=x\mp t>1/27$，以及 $u_T\ge1/20$。由 GJS 的 $L\log G$ 与 $L\log s$ 可写 $G=\kappa(\rho)\sqrt{s/q}$，$L\log\kappa=2\beta\Pi(u^2+Kv^2)$。原定义的 $G/\sqrt{s/q}$ 只依赖径向变量。在原锚点 $r_{1974}$，M 的 $G<23/10,\ -K/\rho<314,\ A>4$ 给
\[
 \kappa(r_{1974})\le(23/10)\sqrt{
 \sqrt{314(r_+-r_{1974})}/(4^{1/3}\sqrt{r_- -r_{1974}})} .
\]
按 GPR 全部原闭物理格积分 $|2\beta\Pi(u^2+Kv^2)|$，保留同一点 $w,w',w''$ 的共同径向标量。严格负域的真实紧支 $K_\delta,\gamma_\delta$ 与 $K_{\delta,r}$ 使用原紧支多项式在同侧的值与导数。所有角导均在原物理角定义。

## 输出的两个负阶

记 $\Delta=p_+p_-$，$H^{-1}=B=\Delta^{-1}\left(\begin{smallmatrix}-i\epsilon x&Ty\\y&-i\epsilon x\end{smallmatrix}\right)$。对整件两参考列 $U(w)$ 使用 [GJR 的两次有序恒等式](R149-supplement-genuine-root-window-interface-receiver-on-both-full-reference-columns.md)。由于 $V_n$ 在本圆为零，
\[
 U(w)\mathsf N^2=\partial^2U(B^2w)
 -\partial U((B^2w)'+B(Bw)')+U((B(Bw)')') .
 \tag{GJO.1}
\]
令 $v_2=B^2w, v_1=(B^2w)'+B(Bw)',v_0=(B(Bw)')'$。若 $s_-,s_+$ 同时夹住全圆 $s$，置 $z=\sqrt{N^{-2/3}+s_+^2}$，$M(v)=\sup|v_1|+z\sup|v_2|$（此处下标指分量）。以 $a=\min_\pm\inf p_\pm$，
\[
 A=\frac{2}{\sqrt a}\frac65
   \big(1+\tfrac58\log(s_+^2/s_-^2)\big)
   \min\!\left(\tfrac{18}{25},
         \left[2/(1+N^{2/3}s_-^2)\right]^{1/4}\right).
\]
这是 GAF 两真角换元及标量水平集分解和 [GIV 的两个初值界](R149-supplement-actual-sharpened-infinite-source-from-both-Airy-root-values.md)。每频率号的两行分支各有 $1/\sqrt2$，再对两个输入号用 Cauchy–Schwarz 给系数 $2/\sqrt a$。真实 $Z_n$ 固定，其原 $6/5$ 矩阵界涵盖初始剪切和两个原参考列。两种高度界均同时适用于高度和以 $z$ 加权的导数行，使用该光学区间上的统一包围。正负号共轭，故有向矩阵与 $w$ 的两个符号费用相同。

对 $P\Lambda^{-2}\partial^d$，$d=0,1,2$ 的范数界为 $1/17,4/17,1$。原 $n^{1/6}$ 和 $H^{-4/3}$ 输入给 $n^{-1/2}(1+n^{-2})^{2/3}$。因而每个真实有向端口满足
\[
 \|P U(w)\mathsf N^{1/6}\|_{H^{-4/3}\to H^{-2}}
 \le \frac{1+N^{-2}}{\sqrt N}A\big(M(v_2)+4M(v_1)/17+M(v_0)/17\big).
 \tag{GJO.2}
\]

原严格点源还需 $J:H^{-2}\to H^{-1}$。设 $P_0=\eta^{-1}I$，$p=\sqrt{17}/(4\eta)$。用原有限恒等式
$J=P_0-P_0LP_0+JL P_0 L P_0$。$P_0:H^t\to H^{t+1}$ 的范数至多 $p$。记 $U_k=\|\partial_\phi^ku\|_{A_0},V_k=\|\partial_\phi^kv\|_{A_0}$，由 $H^1$ 的乘法界及对偶，原
$L=-2\beta P M_{uv}P-2\beta P M_{v'} I M_u P$ 在 $H^{-1}$ 的范数至多
\[
 L_-=2|\beta|\{U_0V_0+U_1V_0+U_0V_1
                  +(V_1+V_2)(U_0+U_1)/4\}.
\]
故 $J$ 的所需增益界是 $p+p^2L_-(1+(7/5)(1855913/500000))$，末项只在真正的 $L^2$ 空间用已付的 $J,L$。[JWS](R133-supplement-joint-Wiener-contraction-and-small-complete-angular-inverse.md)
乘 [SP 的严格点源注入与全子区间传播](R133-supplement-complete-primitive-and-mean-strict-propagation-to-the-waist.md) 的 $192$ 及原反射腰读 $.719$，对全部 1973 个位置相加。公共输入费再乘 $12.4$。自然接缝没有径向长度因子。

可执行消费者对每个原结点保留全部有向跳、单独均值及 GJO.2 的原点源费用，按自然序完整写入私件并逐一保存可续前缀。首个实际运行的终态给外域数值及 $1/10,1$ 两个门。既有 576 个接缝只在合成时引用原结果。其余普通密度、根与物理端口各有独立接收。
