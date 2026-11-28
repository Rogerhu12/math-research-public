# 用两条真实输运方程求首幅的完整自由波算子

取 [G.4–9 的同一 genuine residual](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md)，在一侧原光滑严格片内写
\[
 L=\partial_\rho+d\partial_\phi,\quad L_\sigma=L+\sigma b\partial_\phi,\quad
 W=L^2-b^2\partial_\phi^2,\quad \mathfrak A_0=W+T_0 L+V_0+i_\epsilon\vartheta Q\mathcal K .
\]
这里 $b=\eta\sqrt{-K}$ 是径向量，$Q=b/s,\ s=\sqrt{-T},\ i_\epsilon=i\,\mathrm{sgn}(j)$。$x=X_\phi,v=\omega_\phi,p_\sigma=x-\sigma v$；以下所有角导都在原物理角。令 $w_0=(a,i_\epsilon w)^t=G(x^2+v^2,2i_\epsilon xv/s)^t,\ \mathfrak A_0w_0=(f_a,i_\epsilon f_b)^t$。故
\[
 f_a=(W+T_0 L+V_0)a-\vartheta Q T w,\quad
 f_b=(W+T_0 L+V_0)w+\vartheta Q a .
\]
在实参数上写 $R_\sigma=i_\epsilon r_\sigma$。直接用 [FR1 的带号原输运方程](R149-supplement-first-order-genuine-ray-ratio-by-signed-wave-integration.md)，得到
\[
 L_\sigma r_\sigma=F_\sigma=\frac{-\sigma f_a+s f_b}{2bG p_\sigma^3}.
 \tag{GFW.1}
\]
这一步恢复自由源中的 $\vartheta Q\mathcal K$。容许频率依赖的 genuine 势随后在原 G.7 中计入。

对任一公共标量幅 $M$，记 $\kappa=b_\rho-bd_\phi$。由
$L_{-\sigma}L_\sigma=W+\sigma\kappa\partial_\phi$ 及
$L_{-\sigma}r_\sigma=F_\sigma-2\sigma b\,\partial_\phi r_\sigma$，逐原实点有
\[
\begin{split}
 W(Mr_\sigma)={}&(WM)r_\sigma+
       M(L_{-\sigma}F_\sigma-\sigma\kappa\partial_\phi r_\sigma)\\
 &+(L_{-\sigma}M)F_\sigma+
       (L_\sigma M)(F_\sigma-2\sigma b\,\partial_\phi r_\sigma),\\
 L(Mr_\sigma)={}&(LM)r_\sigma+M(F_\sigma-\sigma b\,\partial_\phi r_\sigma).
\end{split}                                                        \tag{GFW.2}
\]
原首幅是 $w_1=(i_\epsilon\alpha,\zeta)^t$，其中
\[
 \alpha=\sum_\sigma M_\sigma r_\sigma,\qquad
 \zeta=\sum_\sigma \sigma M_\sigma r_\sigma/s,\qquad
 M_\sigma=G p_\sigma^2/2 .
\]
将 (GFW.2) 逐支应用于 $M_\sigma,\sigma M_\sigma/s$。两结果以原 $\mathfrak A_0$ 耦合项 $(i_\epsilon\vartheta QT\zeta,-\vartheta Q\alpha)^t$ 合成，得到完整 $\mathfrak A_0w_1$。$q$ 个归一物理角导只用 $r_\sigma$ 到 $q+1$ 角阶；无需数值求它的任一径向导，第三阶混合导只施于已知的首项几何。$F_\sigma$ 与 $L_{-\sigma}F_\sigma$ 均保两真实方向及正确负号。

## 一侧导和有接缝的径向矩

`fourfold_codazzi_genuine_signed_free_wave.py` 按固定真实点的归一化 $\rho,\phi$ 系数实现 (GFW.1–2)。用
\[
 x_\rho=bv_\phi-(dx)_\phi,\quad v_\rho=bx_\phi-(dv)_\phi,\quad
 \omega_\rho=bx-dv
\]
给前三阶固定角径向导；$s=(3\omega/2)^{1/3}$。令 $k=-K/\rho,\ B=b/\sqrt{\rho},\ A=3\omega/(2\rho^{3/2})$，$F=Bx$。对 $A_j=L^jA$，原正权方程和它在一侧的 $j$ 阶导为
\[
 \rho L A_j+(3/2+j)A_j=(3/2)L^jF .
 \tag{GFW.3}
\]
因 $L\rho=1$ 此式直接归纳成立。固定物理角的混合导由
$\partial_\rho A_j=A_{j+1}-d\partial_\phi A_j$ 恢复，角漂移的非交换项全部出现。在真接缝用同一个有向括号，$A,A_1$ 连续，而
\[
 [A_2]=3[LF]/(2\rho),\qquad
 [A_3]=\big(3[L^2F]/2-7[A_2]/2\big)/\rho .
\]
这是正权矩由前一片接入后一片所需的单侧量。直接使用各原片有符号等式
$A_j=((3/2)L^{j-1}F-(j+1/2)A_{j-1})/\rho$ 亦保留原跳。仅在原内禀 $K$ 的光滑域上
$\rho\partial_\rho k_j+(1+j)k_j=-\partial_\rho^{j+1}K,\ k_j=\partial_\rho^jk$。$G=E A^{1/6} k^{-1/4}$ 的径向标量满足 $E_\rho=2\beta\Pi S\,E$（根常数含在 $E$）。一物理圆上可先以 $E/E(\rho_0)$ 的真实三阶 jet 运算，最后乘一次共同 $E(\rho_0)$；在 (GFW.1) 分子和分母中该常数准确约去。

`fourfold_codazzi_genuine_strong_radial_inputs.py` 从原 65 坐标 cubic、193 坐标方向与原 scalar 模型取得 $d,b,\eta,\beta\Pi S$ 的三阶、$K$ 的四阶及 $T_0,V_0,\vartheta$ 的两阶。方向在最大合格同一 cubic 区间长 $h$、值界 $M$ 下的归一阶 $j=1,2,3$ 费用是 $18M/h,48M/h^2,32M/h^3$。首项见 [DMR](R149-supplement-positive-moment-reception-and-sharp-one-sided-direction-cost.md)。后二项可直接取同一 $-1,-1/2,1/2,1$ 上的四基插值：未归一二阶导行在 $1$ 的绝对和 $24$、在 $-1$ 亦为 $24$，中间为它们的凸组合；三阶导常行的绝对和为 $24$。乘 $(2/h)^j/j!$ 即得。真值修复分片常数的一侧正阶导为零。所有 scalar 导先在原中心上以完整七阶余项限制到闭格，再用 $K_\delta=e^{-\delta w}(K+\delta T_{\rm met}w')$、$\gamma_\delta=\gamma e^{\delta w/2}$ 的真实乘积。不同阶的中间变量只保共同已经付费的阶数。

## 同一首 genuine 残差中消去势的一阶导

令 $\mathcal K=\left(\begin{smallmatrix}0&T\\1&0\end{smallmatrix}\right)$，
$E_{12}=\mathcal K'$, $\mathcal K^\sharp=\mathcal K-2TE_{12}$。
记原有 $C^{64}$ 势为 $V$，$\mathcal B(T)=\int_0^1 V(t^2T)\,dt$，
$\mathcal D_T=Q(xD+QTy\partial_\phi)$，$D=-L,\ y=T_\phi$。保留真实两输入和 $n$ 依赖性。对任一幅 $h$，真实原波算子的积法则给
\[
 \mathfrak A_0(\mathcal B\mathcal K h)
 =\mathcal B\mathcal K\mathfrak A_0 h+
  2(\mathcal B'\mathcal K+\mathcal B E_{12})\mathcal D_T h+
  [(\mu\mathcal B''+A_T\mathcal B')\mathcal K+
          (2\mu\mathcal B'+A_T\mathcal B)E_{12}]h .
\]
这里主符号在 $dT,dT$ 上为 $\mu$，与 $dh$ 上的交叉为 $\mathcal D_T h$。$\vartheta Q\mathcal K$ 与自身矩阵相乘可在这一项中交换。原 $\mathfrak C_j$ 的 $E_{12}$ 仍位于左侧。代入 $V=\mathcal B+2T\mathcal B'$ 与 $V'=3\mathcal B'+2T\mathcal B''$ 后，
\[
\begin{split}
 L_{1,j}={}&\mathfrak A_0 w_1+\mathcal B\mathcal K\mathfrak A_0 w_0
 -\mu V(w_1+\mathcal B\mathcal K w_0)\\
 &+2\mathcal B'\mathcal K^\sharp\mathcal D_T w_0
 +[(\mu\mathcal B''+A_T\mathcal B')\mathcal K^\sharp
                                  -\mu\mathcal B'E_{12}]w_0 .
\end{split}                                                       \tag{GFW.4}
\]
该完整未归一 G.7 加数中没有独立 $V_T$。在 $T<-1/2000$ 区域，$\mathcal B,\mathcal B',\mathcal B''$ 的真实长尾依式保留。拼接处按原单侧状态，(GFW.2–4) 只给普通 $dr$ 体项；原 WUA.46–47 的实际状态跳须另以同一 $J$ 接入。此处尚未给 $(GFW.4)$ 的全域 Sobolev 数值或最后物理返回范数。
