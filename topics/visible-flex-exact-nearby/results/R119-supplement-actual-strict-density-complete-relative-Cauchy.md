# R119 续篇：真实严格负段的全空间密度传递与同空间相对 Cauchy

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对强首剪切新公共度量族的同一个实际非零标签解，
在两个已固定的原径向严格切口之间，把两条真实特征流准确拉回后，
完整 Cauchy 演化与**同一 $\Gamma$ 的径向参考**在同一个 Sobolev
空间中相对接近。没有投掉有限低部或任何高模；两个独立 mean 和
普通、弱源全部参加演化。对本篇定义的完整状态，取
$$
 K_j^{\rm st}=2^{512}(j+4)^5\delta_j^{-10}.
$$
全部内部负分量的相对 interaction 费用满足
$$
 \boxed{\quad
 \sum_i\eta_i<2^{192000}\|X\|_{\mathcal X_{224}},\qquad
 \|X\|\le2^{-262144}\Longrightarrow
 \sum_i\eta_i<2^{-70144}.
 \quad}                                                     \tag{S.1}
$$
这支付先前尚缺的完整严格段幅度/mean 传递。真实两射线主相位仍
包含在输出角图中；本篇不声称它与零标签主相位相同，也不把本篇
相对 Cauchy 门当作已经接通正型双端 DN 的完整混合网络逆。

## 1. 原对象、真实切口与全部输入

采用
[强首剪切全标签图](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md)
的 $\delta_j,\mu_j,\zeta_j,h_j,\Gamma$ 和完整解 $X$，不更换 profile。
算子门在实参数 $\Gamma$ 和实背景解上证明；Jacobi 数据可以复数值。
令 $I_i=[t_L,t_R]$ 是一个内部负分量，删去两端
[真实根图接线](R119-supplement-actual-root-graph-to-fixed-radial-two-port.md)
中所定 $\xi_*=1/64$ 以内的 collar 后所剩的原 $t$ 区间。
其两端是固定原径向切口，且
$$
 Q=-A_\Gamma>1/128,\qquad q=\sqrt Q>1/16.
 \tag{S.2}
$$
跨胞分量采用较深胞元编号 $j$。令
$$
 N_j=2^{184}h_j^{-5}\frac{\zeta_j}{\mu_j\delta_j^2},\qquad
 N_j^\#=N_j+\mathbf1_{j\ge130}N_{j-1},\qquad
 n_i=4N_j^\#\|X\|.                                       \tag{S.3}
$$
全标签局部图的完整四态界给原物理角宽4上的
$\|(P,K,U,V)\|<n_i$。这是真正全部径向点的界；根上的实段
唯一性说明同一原解被此前 CK 解覆盖。下文使用
$n_i<2^{-32}$；实际 (S.1) 的输入远强于此。

本篇始终用物理角 $\theta$，周期 $\pi/2$，频率 $m\in4\mathbb Z$。
记 $\mathcal A_r=\ell^1(e^{r|m|})$，$H^s$ 权为 $(1+|m|)^s$，
所有圆周平均均归一化。为免与 $q=\sqrt Q$ 混淆，Sobolev 指数写
$\upsilon$，范围为
$$
                  -9/2\le\upsilon\le7/2.                 \tag{S.4}
$$
这覆盖前篇 Airy 两行采用的全部 $|s|\le4$ 窗。

## 2. 准确判别式密度及完整 potential

仍写参考坡度为 $w_{\rm ref}$，物理半径为 $a$。设
$$
 E=1+w_{\rm ref}^2,\quad J=1+K+EU,\quad
 D=1-w_{\rm ref}^2(2K+K^2+EP^2),
$$
$$
 d=E(V-P)/J,\qquad v=\sqrt D/J,\qquad
 \mu=(w_{\rm ref}/a)JD^{-3/2},\qquad \nu=qv.
$$
实际 raw Jacobi 散度矩阵与普通源是
$$
 G=\mu\begin{pmatrix}1&-d\\-d&d^2-Qv^2\end{pmatrix},
 \qquad f=w_{\rm ref}^2JD^{-3/2}e.                         \tag{S.5}
$$
因此正判别式密度准确为
$$
 \Lambda=\sqrt{-\det G}=\mu qv
        ={w_{\rm ref}\over a}\,{q\over D},\quad
 \ell=\log\Lambda=\ell_0+r,\quad r=-\log D,
 \quad \ell_0=\log((w_{\rm ref}/a)q).                       \tag{S.6}
$$
令 $m_0=\Lambda^{-1/2}$、$w=\sqrt\Lambda\,h$。这里 $w$ 是
Jacobi 密度高度，与 $w_{\rm ref}$ 不同。直接乘开散度式，得到
$$
 m_0P(m_0w)=\operatorname{div}(\widehat G\nabla w)+\kappa w,
 \quad
 \widehat G={G\over\Lambda}
 =\begin{pmatrix}\nu^{-1}&-d\nu^{-1}\\
            -d\nu^{-1}&d^2\nu^{-1}-\nu\end{pmatrix},
$$
$$
 \boxed{\quad
 \kappa=-\frac12\operatorname{div}(\widehat G\nabla\ell)
        -\frac14\nabla\ell\cdot\widehat G\nabla\ell .\quad}
 \tag{S.7}
$$
没有在此式删去密度的径向导数。径向参考的 $d=0,v=D=1$，故
$$
 \kappa_0=qV_w,\qquad
 V_w={Q_t\over2Q}-{(1+Q)^2\over4Q}
             +{5Q_t^2\over16Q^3}-{Q_{tt}\over4Q^2}.        \tag{S.8}
$$
它恰是
[全频参考证明](R119-supplement-uniform-frequency-reference-Airy-Cauchy.md)
(F.15) 的完整 wave potential。

以下给出实际 potential 差的自足费用。用原完整方程
$$
 P_t=V-(A+1)P,\qquad
 K_t={-A(2K+U+K^2+KU+w_{\rm ref}^2P^2)+E(V-P)^2\over J}
$$
及已直接证明的准确恒等式
$$
 (\partial_t-d\partial_\theta)\log v+d_\theta
 ={A(1-v^2)-d^2\over E},
$$
$$
 d_t-dd_\theta-Avv_\theta
 =d\left[-1+{A(w_{\rm ref}^2-v^2)-d^2\over E}\right],
 \quad D_t-dD_\theta={2Aw_{\rm ref}^2DU\over J}.            \tag{S.9}
$$
角宽4到2的 Cauchy 估计、$|J^{-1}|<2$ 和 $|D^{-1}|<2$ 给
以下刻意放宽的完整界。表中范数均是实际角 Wiener 范数；
需要一项额外角导时在宽1上消费剩余的一个单位。
$$
\begin{array}{c|c}
 \text{量}&\text{上界}\\ \hline
 d, v-1, d_\theta, v_\theta&2^5n_i\\
 d_t, v_t&2^{10}(1+Q)n_i\\
 r_\theta, r_{\theta\theta}&2^8w_{\rm ref}^2n_i\\
 r_t&2^8w_{\rm ref}^2(1+Q)n_i\\
 r_{t\theta}&2^{12}w_{\rm ref}^2(1+Q)n_i\\
 r_{tt}&2^{24}w_{\rm ref}^2[|Q_t|+(1+Q)^2]n_i .
\end{array}                                                 \tag{S.10}
$$
最后一行由 $r_t=dr_\theta-2Aw_{\rm ref}^2U/J$ 微分一次得到：
$U_t=(P_t)_\theta$、$J_t=K_t+E_tU+EU_t$ 仍只用完整四态及角导；
$w_{{\rm ref},t}=Aw_{\rm ref}$。所以没有借一个未支付的 $A_{tt}$。

把 $\widehat G$ 三个系数记作 $a_1,b_1,c_1$，令
$\Delta a_1=a_1-1/q$。同一商法则给
$$
\begin{split}
 |\Delta a_1|&\le2^6n_i/q,\qquad
 |\Delta a_{1,t}|\le2^{12}n_i[(1+Q)/q+|q_t|/q^2],\\
 |b_1|&\le2^6n_i/q,\quad |b_{1,\theta}|\le2^9n_i/q,\\
 |b_{1,t}|&\le2^{14}n_i[(1+Q)/q+|q_t|/q^2],\quad
 |a_1|\le2/q,\quad |c_1|\le3q,\quad |c_{1,\theta}|\le2^9qn_i.
\end{split}                                                 \tag{S.11}
$$
小量 $n_i<2^{-32}$ 保证 $d^2/q^2$ 项已包含在 $|c_1|\le3q$ 内。
又
$$
 L:=\ell_{0,t}=-1-Q+{Q_t\over2Q},\qquad
 L_t=-Q_t+{Q_{tt}\over2Q}-{Q_t^2\over2Q^2}.
$$
从 (S.7) 减去参考式，完整差准确是
$$
\begin{split}
 \kappa-\kappa_0={}&-\tfrac12\partial_t(\Delta a_1L)
 -\tfrac12\partial_\theta(b_1L)
 -\tfrac12\operatorname{div}(\widehat G\nabla r)\\
 &-\tfrac14\big[
 \Delta a_1L^2+2a_1Lr_t+2b_1Lr_\theta
     +a_1r_t^2+2b_1r_tr_\theta+c_1r_\theta^2\big].
\end{split}                                                 \tag{S.12}
$$
令
$$
 W(t)=1+{(1+Q)^2\over q}+{|Q_t|\over q}
                  +{Q_t^2\over q^5}+{|Q_{tt}|\over q^3}.
$$
代 (S.10)--(S.11)，利用 $q>1/16$、$w_{\rm ref}<1$ 和
$2(1+Q)|Q_t|/q^3\le(1+Q)^2/q+Q_t^2/q^5$：
前两项未乘 $1/2$ 的界分别为 $2^{16}n_iW,2^{10}n_iW$；
完整 $\operatorname{div}(\widehat G\nabla r)$ 的界为 $2^{36}n_iW$；
最后方括号的界为 $2^{32}n_iW$。例如其中最大的径向项
$a_1r_{tt}$ 不超过 $2^{25}n_i[(1+Q)^2+|Q_t|]/q$；
$a_{1,t}r_t$ 的交叉项正由显示的不等式控制。其余每项都是
(S.11) 与 (S.10) 的直接乘积。因此安全地有
$$
 \|\kappa-\kappa_0\|_{\mathcal A_1}<2^{64}n_iW(t),\qquad
 \int_IWdt<2^{64}(j+4)^2\delta_j^{-5}.                     \tag{S.13}
$$
后一式逐项使用参考 (F.3) 的真实几何界；它的四个非平凡项就是
(F.16) 的各项去掉系数，最大额外因子仅4，常数项 $|I|<4\delta$。
$Q_{tt}$ 是实际分片 $L^\infty$ 导数，$Q_t$ 连续，所以没有
遗漏径向 delta 负荷。

## 3. 两条真实密度流及两个独立 mean

先取齐次源。令
$$
 p=\mu(h_t-dh_\theta),\quad
 T={\mu\over2}(\ell_t-d\ell_\theta),\quad
 z=w_\theta,\quad \zeta={p+Th\over\sqrt\Lambda},\quad
 y_\sigma=(z+\sigma\zeta)/2.
$$
则 (S.7) 准确等价于
$$
 (y_\sigma)_t+\partial_\theta(g_\sigma y_\sigma)
      =-\sigma\kappa w/2,\qquad
 w_t=dz+\nu\zeta,\qquad g_\sigma=-d-\sigma\nu.             \tag{S.14}
$$
取从 $t_L$ 出发的真实流与逆标签
$$
 (H_\sigma)_t=g_\sigma(t,H_\sigma),\quad H_\sigma(t_L)=\mathrm{id},
 \quad S_\sigma=H_\sigma^{-1},\quad
 \mathcal D_H=M_{H'}C_H,\quad X_\sigma=\mathcal D_{H_\sigma}y_\sigma.
$$
这里及下文 prime 仅表示角导。所有密度 pullback 都在真实位置：
$$
             (X_\sigma)_t=-\sigma\mathcal D_{H_\sigma}(\kappa w)/2.
 \tag{S.15}
$$
没有以参考平移替代 $H_\sigma$。

设 $D_\theta=-i\partial_\theta$，$D_\theta^{-1}$ 在 mean 为0。
周期高度的完整相容条件是
$$
 \langle X_+\rangle=\alpha,\quad
 \langle X_-\rangle=-\alpha,\quad Z_\sigma=X_\sigma-\sigma\alpha,
$$
$$
 \boxed{\quad w=c+\alpha(S_+-S_-)
       -i\sum_{\sigma=\pm}C_{S_\sigma}D_\theta^{-1}Z_\sigma .\quad}
 \tag{S.16}
$$
自然 lift 的差 $S_+-S_-$ 周期，故此式是周期函数；逐角微分即得
$w_\theta=y_++y_-$。$c$ 是独立高度积分常数，在左切口等于
$\langle w\rangle$，其后一般不等于物理平均。两个 mean 的准确行是
$$
 \alpha'=-\tfrac12\langle\kappa w\rangle,\qquad
 c'=-\alpha'\langle S_+-S_-\rangle
        +i\sum_\sigma\langle C_{S_\sigma}D_\theta^{-1}Z_\sigma'\rangle.
 \tag{S.17}
$$
这里没有一点处的 $H^s$ 求值。证明可对
$\phi_\sigma(\eta)=\sigma\alpha\eta-iD_\theta^{-1}Z_\sigma(\eta)$
微分：$w=c+\sum\phi_\sigma\circ S_\sigma$，且
$S_{\sigma,t}=-g_\sigma S_{\sigma,\theta}$。剩余
$\sum C_{S_\sigma}\phi_\sigma'$ 的角导为0，取平均便是 (S.17)。

完整固定标签空间是
$$
 \mathcal F_\upsilon=\mathbb C^2\oplus H^\upsilon_0\oplus H^\upsilon_0,
 \quad Y=(c,\alpha,Z_+,Z_-),\quad
 \|Y\|=|c|+|\alpha|+\|Z_+\|_{H^\upsilon}+\|Z_-\|_{H^\upsilon}.
 \tag{S.18}
$$
全部非零 Fourier 模位于两个 $Z$ 中，两个 mean 位于 $c,\alpha$。
本篇没有高低投影，也没有待外部解出的有限头部历史。

## 4. 同空间小差的真实来源

令 $H_\sigma^0=\theta-\sigma\int_{t_L}^tq$ 是同一 $\Gamma$ 的
径向流，$S_\sigma^0=(H_\sigma^0)^{-1}$。
真实 log-quintic 几何给 $\int_I(1+Q)dt<16(j+4)$，且
$\int_Iqdt<1$。消去参考实平移后，对真实复角 ODE 应用 Picard
和 (S.10)，在角宽2上得到
$$
 |H_\sigma-H_\sigma^0|<2^{12}(j+4)n_i,\qquad
 |S_\sigma-S_\sigma^0|<2^{13}(j+4)n_i.
$$
在宽1的完整 $C^8$ 界因此可安全记为
$$
 r_i=2^{32}(j+4)n_i.                                     \tag{S.19}
$$
实际输入使 $r_i<2^{-32}$。例如 (U.25) 的完整前缀加深尾预算
直接给 $r_i<2^{160036}\|X\|<2^{-102108}$。

以下标准圆周估计的常数也明示：对 (S.4) 的全部指数，实际
$C_H,\mathcal D_H$ 及逆的范数不超过 $2^{20}$；并有
$$
 \|\mathcal D_H-\mathcal D_{H^0}\|_{H^{\upsilon+1}\to H^\upsilon}
       <2^{48}r_i,
$$
$$
 \|(C_S-C_{S^0})D_\theta^{-1}\|_{H^\upsilon_0\to H^\upsilon}
       <2^{49}r_i.                                       \tag{S.20}
$$
为自足性，可用 $H_\lambda=H^0+\lambda(H-H^0)$ 写
$\partial_\lambda C_{H_\lambda}=M_{H-H^0}C_{H_\lambda}\partial_\theta$；
密度式再加 $(H-H^0)'C_{H_\lambda}$。到整数6阶的乘积与链式法则
仅需 $C^8$，非恒等导数组合少于 $2^{16}$，$|H'-1|<2^{-32}$。
正整数阶付 $2^{20}$ 即足够；负阶用
$C_H^*=\mathcal D_{H^{-1}}$，再作 Sobolev 插值。对差式同样先
保留那一次 $\partial_\theta$，然后由 $D_\theta^{-1}$ 消去；
频率 $|m|\ge4$ 上 $\|D_\theta^{-1}\|_{H^\upsilon\to H^{\upsilon+1}}
\le5/4$。这证明 (S.20)，没有主张裸 pullback 的同阶 norm 小。

把 (S.16) 记成 $w=R_HY$，(S.15) 的右端两行记成 $B_Hw$。
若一对 $V_\sigma$ 的均值相反，定义 $L_HV$ 为
$$
 \alpha'=\langle V_+\rangle,\quad Z_\sigma'=\Pi_0V_\sigma,
 \quad c'=-\alpha'\langle S_+-S_-\rangle
                 +i\sum_\sigma\langle C_{S_\sigma}D_\theta^{-1}\Pi_0V_\sigma\rangle.
$$
则完整演化就是
$$
                         Y'=\mathcal A_HY,\qquad
                         \mathcal A_H=L_HB_HR_H.          \tag{S.21}
$$
$R_H:\mathcal F_\upsilon\to H^{\upsilon+1}$、
$L_H:(H^\upsilon)^2\to\mathcal F_\upsilon$ 的 norm 都小于 $2^{22}$；
参考二者小于4。式 (S.20) 给
$$
 \|R_H-R_0\|_{\mathcal F_\upsilon\to H^\upsilon}<2^{50}r_i,\qquad
 \|L_H-L_0\|<2^{51}r_i.
$$
角宽1的函数作为全部所需 $H^\upsilon$ 乘子，其 norm 小于
$2^{20}$ 倍 $\mathcal A_1$ norm，这由
$(1+|m+n|)/(1+|m|)\le1+|n|$ 直接得到。

用有序分解
$$
 \mathcal A_H-\mathcal A_0
 =(L_H-L_0)B_0R_0+L_H(B_H-B_0)R_0+L_HB_H(R_H-R_0)
$$
估计。中间项的角图差作用于 $R_0$ 的一阶增益；最后一项已由
(S.20) 完整支付。三个相应费用可分别取
$2^{53}r_i|\kappa_0|$、
$2^{72}r_i|\kappa_0|+2^{64}\|\kappa-\kappa_0\|_{\mathcal A_1}$、
$2^{92}r_i|\kappa_0|+2^{112}r_i\|\kappa-\kappa_0\|_{\mathcal A_1}$。
由于 $r_i<2^{-32}$，得到真正同空间结论
$$
 \|\mathcal A_H-\mathcal A_0\|_{\mathcal F_\upsilon\to\mathcal F_\upsilon}
 <2^{96}\big[\|\kappa-\kappa_0\|_{\mathcal A_1}+r_i|\kappa_0|\big],
$$
$$
 \boxed{\quad
 \int_I\|\mathcal A_H-\mathcal A_0\|dt
 <2^{256}(j+4)^3\delta_j^{-5}N_j^\#\|X\|.
 \quad}                                                     \tag{S.22}
$$
完整非零模、两个 mean、高低互耦均包含在 (S.21)--(S.22)。

## 5. 参考条件数：非零全部频率和真正高度 mean

这里不能直接把此前原梯度框架的常数槽当作真实高度 mean。
下面分别付两者，然后在同一个 $\mathcal F_\upsilon$ 中合并。

对非零模，参考严格 wave 变量是 $w=\sqrt{\mu_0q}\,h$，
$ds=qdt$，$w_{ss}+(m^2+V_w)w=0$。若
$|m|\ge m_*=2^{64}(j+4)^2\delta^{-5}$，则
$\int|V_w|ds/|m|<1/16$。两行 $(imw,w_s)$ 的双向 norm 小于2；
到 $(y_+,y_-)$ 的恒定矩阵及参考标签实平移只增加因子2。
高频严格 Cauchy norm 因而小于4。

若 $0<|m|<m_*$，保留此前完整低频原梯度能量
$2^{160}(j+4)\delta^{-1}M^{5/3}$，$M=1+|m|$。
从参考原两行
$\sqrt{\mu_0}\operatorname{diag}(\sqrt\omega,\omega^{-1/2})(im h,h_t)$
到 $(imw,w_s)$ 的完整矩阵是
$$
 C_m=\begin{pmatrix}
 \sqrt{q/\omega}&0\\
 \ell_{0,t}/(2im\sqrt{q\omega})&\sqrt{\omega/q}
 \end{pmatrix},
 \quad \omega=(Q+\varrho^2M^{-2/3})^{1/2},\quad
 \varrho=32(j+4)/\delta.                                  \tag{S.23}
$$
其 inverse 具有同一剪切的相反号。$q>1/16$ 给任意两个截面的
双框架费用小于
$$
 2^{20}[1+\varrho M^{-1/3}+L_*^2M^{-2}],\qquad
 L_*=2^{25}(j+4)\delta^{-3}\ge|\ell_{0,t}|.                \tag{S.24}
$$
这里同时取两个截面统一上界，未把两个 norm 之一省去。
代 $M<2m_*=2^{65}(j+4)^2\delta^{-5}$，完整低频费用不超过
$$
 2^{180}(j+4)\delta^{-1}
 [M^{5/3}+2^5(j+4)\delta^{-1}M^{4/3}
                  +2^{50}(j+4)^2\delta^{-6}M^{-1/3}]
 <2^{300}(j+4)^5\delta^{-10}.                             \tag{S.25}
$$
因此没有留下任何频率损失。特别没有先把两框架以最大的
$\delta^{-3}$ 统收再重复付费；(S.24) 保留各频率的真正剪切比例。

真正 mean 用原守恒通量 $p_0=\mu_0(h_0)_t$。在状态
$(\sqrt{\Lambda_0}h_0,p_0/\sqrt{\Lambda_0})$ 中，双向传递准确为
$$
 \begin{pmatrix}r_{ts}&k_{ts}\\0&r_{ts}^{-1}\end{pmatrix},
 \quad r_{ts}=\sqrt{\Lambda_0(t)/\Lambda_0(s)},\qquad
 k_{ts}=\sqrt{\Lambda_0(t)\Lambda_0(s)}\int_s^t\mu_0^{-1}d\tau.
 \tag{S.26}
$$
参考 $\mu_0$ 比例 $<2^{272}\delta^{-2}$、
$q_{max}<2^6\sqrt{j+4}\delta^{-3/4}$、$q_{min}>1/16$ 给
$$
 |r_{ts}^{\pm1}|<2^{142}(j+4)^{1/4}\delta^{-11/8},\qquad
 |k_{ts}|<2^{280}\sqrt{j+4}\delta^{-7/4}.
$$
到密度通量 $\zeta_0=p_0/\sqrt\Lambda_0+(\ell_{0,t}/2q)w_0$
的每个实际剪切 norm 小于 $2^{29}(j+4)\delta^{-3}$。
最后 $\alpha=\zeta_0/2$、$c=w_0-2\alpha\int_{t_L}^tq$，
因 $\int_Iq<1$，两端这个转换的费用各小于4。
故真正完整 mean 双向费用小于
$$
                     2^{350}(j+4)^3\delta^{-31/4}.         \tag{S.27}
$$
结合 (S.25) 和高频项，参考完整演化满足
$$
 \boxed{\quad
 \|\mathcal U_0(t,s)\|_{\mathcal F_\upsilon\to\mathcal F_\upsilon}
 <K_j^{\rm st}=2^{512}(j+4)^5\delta_j^{-10},\quad t,s\in I_i.
 \quad}                                                     \tag{S.28}
$$
径向参考逐模对角，因此这个界对 (S.4) 的所有指数同时成立。

## 6. 有限前缀与新深尾的实际总预算

真正 interaction picture
$\mathcal U_0(s,t)\mathcal U_H(t,s)$ 的 generator 由 (S.22)、
(S.28) 控制，故可取
$$
 \eta_i=2^{1280}(j+4)^{13}\delta_j^{-25}N_j^\#\|X\|,\qquad
 \|\mathcal U_0(s,t)\mathcal U_H(t,s)-I\|\le e^{\eta_i}-1.
 \tag{S.29}
$$
这在全部模式和两个 mean 的 Banach 空间直接使用 Picard；
不重复花角宽，也不把普通绝对误差除以极小尾迹。

为明确保留新规范的全局因子，实际参数为
$$
 \delta_j=(2/25)2^{-j},\quad
 \mu_j/\epsilon=\begin{cases}\delta_j^6,&j\le4096,\\
                 \delta_{4096}^{3/2}\delta_j^{9/2},&j>4096,
                 \end{cases}
$$
$$
 \zeta_j/\epsilon=\begin{cases}\delta_j^{39/4},&j\le8192,\\
                 \delta_{8192}^{-485/4}\delta_j^{131},&j>8192,
                 \end{cases}\quad
 h_j=\begin{cases}9/100,&j\le4096,\\8\delta_j^{1/256},&j>4096.
                 \end{cases}                              \tag{S.30}
$$
所以 $N_j$ 的三个幂依次为 $7/4,827/256,31867/256$，两个
接缝的全局因子均保留。令 $B_j=2^{1280}(j+4)^{13}\delta_j^{-25}N_j^\#$。
Arb 256 位定向计算给下表的向外界（完整数值在所附报告中）：

| $j$ | $\log_2B_j$ 上界 |
|---:|---:|
| 129 | 4657.058 |
| 130 | 4682.574 |
| 4096 | 96956.234 |
| 4097 | 97023.584 |
| 4098 | 97048.734 |
| 8192 | 186186.177 |
| 8193 | 186207.803 |
| 8194 | 186108.325 |

在各浅区间内，$\delta^{-25}N_j$ 及其前一层项都严格增加，
因为 $25>7/4,827/256$。8194 之后两项都已进入第三幂，且
$$
 {B_{j+1}\over B_j}
 \le\left({j+5\over j+4}\right)^{13}2^{25-31867/256}<2^{-90}.
$$
129 至8193的全部有限层数小于 $2^{14}$；每层至多两个负分量。
加真正几何尾，得
$$
                         2\sum_{j\ge129}B_j<2^{192000},
$$
即 (S.1)。这是真正未缩减有限前缀和全部深尾的预算；
既不扔掉 $\delta_{4096}^{-3/2}$，也不把8193层的旧/新邻胞混为一项。
在实际工作输入上
$$
 \sum_i\|\mathcal U_0(s,t)\mathcal U_H(t,s)-I\|<2^{-70143},
 \qquad \|\mathcal U_H(t,s)\|<2K_j^{\rm st}.                \tag{S.31}
$$

## 7. 实际普通源、弱源与真实物理两迹

现在保留原方程 $Ph=f-\operatorname{div}F$。准确高度变换为
$$
 F_d=m_0F,\qquad f_d=m_0\left(f-\tfrac12\nabla\ell\cdot F\right).
 \tag{S.32}
$$
置真实 total 密度通量
$$
 \zeta={w_t-dw_\theta\over\nu}+F_d^t.
$$
则 (S.14)--(S.15) 中的完整 source 是
$$
 \mathcal S_\sigma={\sigma f_d\over2}
       -\tfrac12\partial_\theta[(\nu+\sigma d)F_d^t+\sigma F_d^\theta],
 \qquad X_\sigma'=\mathcal D_{H_\sigma}[-\sigma\kappa w/2+\mathcal S_\sigma].
 \tag{S.33}
$$
独立高度行和两个 mean 仍为
$$
 w_t=dw_\theta+\nu\zeta-\nu F_d^t,\qquad
 \alpha'=\tfrac12\langle f_d-\kappa w\rangle,
$$
$$
 c'=-\alpha'\langle S_+-S_-\rangle
     +i\sum_\sigma\langle C_{S_\sigma}D_\theta^{-1}Z_\sigma'\rangle
     -\langle\nu F_d^t\rangle.                            \tag{S.34}
$$
最后这一弱源的高度 mean 行不能删除。证明中
$\partial_\theta\sum C_{S_\sigma}\phi_\sigma'=-\partial_\theta(\nu F_d^t)$，
取平均即得它；源满足
$\langle\mathcal S_++\mathcal S_-\rangle=0$，故两个密度均值仍相反。

完整源 norm 直接写成
$$
 \mathfrak S_{i,\upsilon}:=
 \int_I\left[
 \sum_{\sigma=\pm}\left\|
 {\sigma f_d\over2}-\tfrac12\partial_\theta
       ((\nu+\sigma d)F_d^t+\sigma F_d^\theta)
 \right\|_{H^\upsilon}
 +\|\nu F_d^t\|_{H^\upsilon}\right]dt.                    \tag{S.35}
$$
从零初值到完整输出 $\mathcal F_\upsilon$ 的真实源列满足
$$
                     \|Y_{\rm src}(t)\|<2^{48}K_j^{\rm st}
                                                   \mathfrak S_{i,\upsilon}.
 \tag{S.36}
$$
这是实际 $\mathcal D_H$、$L_H$、独立高度行和 (S.31) 的有序
Duhamel 估计。它允许一般实径向 $L^1_tH^\upsilon_\theta$ 源；
没有把混合径向角坐标换元应用于一个未授予径向正则性的源。

普通源 $F=0$ 时，实际因子保留为
$$
 f_d=a^{1/2}w_{\rm ref}^{3/2}{J\over\sqrt q\,D}\,e.
 \tag{S.37}
$$
$J/D$ 的 $H^\upsilon$ 乘子 norm 小于2，于是
$$
 \mathfrak S_{i,\upsilon}
 \le2\int_I{a^{1/2}w_{\rm ref}^{3/2}\over\sqrt q}
                                  \|e(t)\|_{H^\upsilon}dt.
 \tag{S.38}
$$
若消费 $L^2_t$，须对显示的真实径向权另作 Cauchy--Schwarz；
不将其暗换为无权单位。根图区域的普通源仍需要前篇已经明确的
联合正则性，(S.38) 不升级该区域的源权限。

由完整 $Y$ 恢复 (S.16)，再用
$$
 y_\sigma=\mathcal D_{S_\sigma}(Z_\sigma+\sigma\alpha),\quad
 \zeta=y_+-y_-,\quad h=\Lambda^{-1/2}w,
$$
$$
 \boxed{\quad p+F^t=\sqrt\Lambda\,\zeta-T\Lambda^{-1/2}w.\quad}
 \tag{S.39}
$$
因此两端实际高度、真实法向剪切和整个通量均保留。特别
$$
 \langle h\rangle=\langle\Lambda^{-1/2}w\rangle,\qquad
 \langle p+F^t\rangle
 =\langle\sqrt\Lambda\,\zeta-T\Lambda^{-1/2}w\rangle.      \tag{S.40}
$$
它们一般不是 $c$、$2\alpha$。给 bare 通量需另付真实端点
$F^t(t_L),F^t(t_R)$ 的迹；(S.35) 的体源 norm 本身不授予这些迹。

把 (S.16)、(S.39) 组成的准确物理端口到固定标签状态映射记为
$\mathcal Q_t$。在齐次情形，实际原两迹传递和本篇比较对象准确是
$$
 U_{\rm phys}=\mathcal Q_{t_R}^{-1}\mathcal U_H(t_R,t_L)\mathcal Q_{t_L},
 \quad
 U_{\rm cmp}=\mathcal Q_{t_R}^{-1}\mathcal U_0(t_R,t_L)\mathcal Q_{t_L}.
 \tag{S.41}
$$
式 (S.29) 是由 $\mathcal Q_{t_L}$ 归一后的完整相对误差。
极小 $w_{\rm ref}/a$ 等物理尺度留在这两个明确端口映射里，
不被称作一个对所有层无权有界的物理转换。

## 8. 接入范围与下一项真实缺口

本篇和真实根/Airy、图接线一起支付同一非零标签背景的负型
内部传播。全部角图和系数可随真实标签、$\Gamma$ 连续选择；
系数的复解析性不等于粗 $H^s$ 裸 pullback 的无损耗算子解析性。
一次参数差由 (S.20) 的一次积分增益支付；更高参数导数必须保留
相应角阶分级，不能自动重复此一次增益。

尚待联立的是：新候选上的实际双射线 return 相位修调、转向与
正型两端完整 DN 的归一、外部真实非线性输入的可达性及其全部
源列。特别 (S.41) 的输出角图是真实的，不能由 $H-H^0$ 很小
就把所有频率的主相位替换为参考相位。这里证明的全空间严格段
相对门正是把这部分保留之后得到的幅度和 mean 控制。

[符号恒等式与实际前缀/深尾预算程序](../scripts/fourfold_actual_strict_density_relative_20261113.py)
和[完整定向报告](../notes/2026-11-13-R119-actual-strict-density-relative-budget.json)
记录 (S.7)、(S.12)、(S.33)--(S.34)、所有 mean/频率条件数及
(S.29)--(S.31) 的实际预算。
