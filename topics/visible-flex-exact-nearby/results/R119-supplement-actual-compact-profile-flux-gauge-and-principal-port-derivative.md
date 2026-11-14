# R119 续篇：实际 compact 控制的非线性通量规范、完整 mean 与主端图微分

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 固定第53–55束的同一个实际受控尾、同一当前
$\Gamma$ 和一个已经存在的完整标签解。对真正的径向 log-profile 方向
$\delta\log p_*=\psi$，本文从实际非线性 Darboux 方程消去
$\psi_y$，并给出真实局部源的 $\rho^5$ 费用；局部场的显式修正为
$\rho^4$。这两个幂使用第56–57束真实 compact 方向的幅度和长度，
不以其较粗 $C^4$ norm 代替。

消去式精确保留 pointwise holonomy 密度、其 mean 和独立高度常数。
随后把同一消去用于两条实际射线，给出包含全部 mean 的物理
height/total-flux 端图及其强微分恒等式。本文没有将局部源的
$\rho^5$ 界直接改名为完整固定标签响应或 $D_\Omega E$ 的界；
缺少的传播量在第9节明确给出。特别，裸角 pullback 没有被假定
在同一 Sobolev 空间中按算子 norm 可微。

## 1. 本对象的准确方程与取向

只在一个固定胞元内改变 compact shape，保持实际半径坐标和
$\mu_j$ 不动。原材料坐标满足 $r_y=r/\sqrt{12}$，物理 log 半径
$t=y/\sqrt{12}$。采用 R72 (2.4) 的真实物理扰动
$$
 p=v_\theta/r,\quad k=v_r,\quad
 w=\mu_jp_*/r^7,\quad E=1+w^2,\quad
 b=(\log p_*)_y,\quad \lambda=b-7/\sqrt{12}.
 \tag{C.1}
$$
这里 $p$ 不是 $p_*$，也不是 Jacobi flux。
设
$$
 q=p_\theta,\quad K=w+k,\quad T=1-p^2,\quad
 J=K+Eq,\quad D=ET-K^2=1-2wk-k^2-Ep^2,\quad z=k_\theta-p .
 \tag{C.2}
$$
$J/w$ 是此前的 $1+n_{\rm ph}$，不是根图 Jacobian。
实际小球保持 $J>0,D>0,T>0$。定义标量
$$
 f=\frac{w[-k-q+w(kq-p^2)]}{J},\qquad
 F_1=(0,f),\qquad
 V=\frac1{\sqrt{12}}\left(z,\frac{Ez^2}{J}\right).
 \tag{C.3}
$$
原完整、未截断方程准确为
$$
 (p,k)_y=V+\lambda F_1,\qquad w_y=\lambda w.             \tag{C.4}
$$
它包括真实 mean 小根；没有把 Galerkin 压缩逆与投影交换。
本文直接微分已经存在的全频解，故不需要另把一个错误的有限投影当作
(C.4)。

紧支方向来自第56–57束。以 ramp 坐标 $x$ 写
$dt=a\,dx,\ dy=\eta_j\,dx,\ a=\eta_j/\sqrt{12}$，
其支持在 strict 的未使用小区间，且
$$
 \|\psi^{(\ell)}\|_\infty\le\rho^{4-\ell}\quad(0\le\ell\le4),
 \qquad
 \|\psi^{(\ell)}\|_{L^1(dx)}\le2\rho^{5-\ell}.
 \tag{C.5}
$$
$\rho$ 是方向自己的真实支集尺度。有限方向的 $\ell^1$ 组合用其各自
(C.5) 相加；没有额外乘方向数。
在 compact 支集之外及所有离散标签切口，$\psi$ 连同前四 jet 为0。
径向两 phase 的一阶补偿在这些新支集方向上为0，见第54、57束。
若另消费非径向联立 $\Gamma^*(a,\Omega)$ 的导数，则还须加入第8节
明确保留的两个 bump 列。

## 2. 完整背景变分：无 $\psi_y$ 的准确 forcing

令 $\dot z=(\dot p,\dot k)$ 是固定标签、固定当前 $\Gamma$ 的实际
参数变分。准确有 $\dot w=\psi w,\dot\lambda=\psi_y$，所以
$$
 \dot z_y=D_z(V+\lambda F_1)\dot z
       +\psi w\partial_w(V+\lambda F_1)+\psi_yF_1 .
$$
引入真正的局部修正
$$
 \widehat z=\dot z-\psi F_1 .
$$
沿原解微分 $F_1$，保留 $w_y=\lambda w$ 后，所有含
$\lambda\,w(F_1)_w$、$\lambda D_zF_1F_1$ 和 $\psi_yF_1$
的项逐项相消。因此
$$
 \boxed{\quad
 \widehat z_y=D_z(V+\lambda F_1)\widehat z+\psi\mathcal R,
 \qquad
 \mathcal R=wV_w+D_zV\,F_1-D_zF_1\,V .
 \quad}                                                     \tag{C.6}
$$
$D_z$ 是完整角微分向量场的 Fréchet 导数。
$\mathcal R$ 不含 $b$、$b_y$ 或方向的任何径向导数。

为使这不是一个形式 bracket，下面给实际的完整两个分量。
准确代数给
$$
 f_k=\frac{w^2(Eq^2-T)}{J^2},\quad
 f_q=-\frac{w^2D}{J^2},\quad f_p=-\frac{2w^2p}{J},
$$
$$
 f_\theta=\frac{w^2}{J^2}
       [(Eq^2-T)k_\theta-Dp_{\theta\theta}-2pqJ].
 \tag{C.7}
$$
代回 (C.6)，第二分量中来自 $D_zV$ 与 $D_zF_1$ 的
$fz^2$ 项也相消，得到
$$
 \boxed{\begin{aligned}
 \mathcal R_p&=f_\theta/\sqrt{12},\\
 \mathcal R_k&=\frac1{\sqrt{12}}\left[
 \frac{2Ez}{J}f_\theta+
 \frac{w^2}{J^2}\{(2K-Eq)z^2+D z_\theta\}
 +\frac{2w^2pz}{J}\right].
 \end{aligned}}                                             \tag{C.8}
$$
这只需背景的两个角导数。其原点线性项是
$$
 \mathcal R_{\rm lin}
 =\frac1{\sqrt{12}}(-k_\theta-p_{\theta\theta},
                         k_{\theta\theta}-p_\theta).
 \tag{C.9}
$$
故不能把 (C.6) 的 forcing 错称为二次源；它的一次部分真实存在。

在整个胞元的左右端 $\psi=0$，所以 $\widehat z=\dot z$。
局部修正只改变内部表示，不改变任何真实两迹、外条件或内部标签。

## 3. Pointwise 密度不变量及准确 mean 行

实际 holonomy 密度为
$$
 \mathfrak m=\frac{T+Kq}{T\sqrt D},\qquad
 M=\langle\mathfrak m\rangle .
 \tag{C.10}
$$
令控制向量场 $\mathcal B=w\partial_w+f\partial_k$；
其作用保持 $p,p_\theta$。直接计算给
$$
 \mathcal BK=\frac{w^2(T+Kq)}J,\qquad
 \mathcal BD=\frac{2w^2qD}{J}.
$$
所以两个分子的变化准确抵消：
$$
 \boxed{\quad \mathcal B\mathfrak m=0,\qquad
       \dot{\mathfrak m}=D_z\mathfrak m[\widehat z].\quad} \tag{C.11}
$$
这是逐点恒等式，比只在积分后保 mean 更强。

另有
$$
 \mathfrak m_k=JD^{-3/2},\quad
 \mathfrak m_q=K/(T\sqrt D),
$$
$$
 \partial_\theta\frac K{T\sqrt D}-\mathfrak m_p
                       =\frac{E(k_\theta-p)}{D^{3/2}}.
$$
将 (C.4) 的 $V$ 部分代入，得到完整守恒律
$$
 \boxed{\quad
 \mathfrak m_y=
 \frac1{\sqrt{12}}\partial_\theta
             \frac{K(k_\theta-p)}{T\sqrt D}.
 \quad}                                                     \tag{C.12}
$$
全部 Fourier 项和 mean 都在此式中。因此真 $M=1$ 解的变分满足
$\langle D_z\mathfrak m[\widehat z]\rangle=0$；
它不是将 $\widehat k_0$ 或 $\dot k_0$ 置零。

高度另按原梯度关系恢复：
$$
 \dot v(y,\theta)=\dot v(y_-,\theta)
   +\frac1{\sqrt{12}}\int_{y_-}^{y}
           r(s)[\widehat k(s,\theta)+\psi(s)f(s,\theta)]\,ds .
 \tag{C.13}
$$
其中一个整体 mean 高度常数仍独立保留。另一端的高度 mean 是
(C.13) 的积分输出。本文不额外规定两个端点的 mean 高度。

## 4. 真实局部 norm：$\rho^4$ 修正及 $\rho^5$ forcing

令
$$
 \mathfrak n_{s,2}
 =w^{-1}\big(\|p\|_{\mathcal A_s^2}+\|k\|_{\mathcal A_s^2}\big)
 \le1/64,\qquad 0<w\le1,
$$
其中 $\|u\|_{\mathcal A_s^2}=\sum_m(1+|m|)^2e^{s|m|}|u_m|$，
包含 mean。这个假设由本对象原四态条带界得到：
$(1+M)^2e^{-2M}\le1$，故从已付宽4降到宽2即可，不增加径向
或标签输入权。下列代数也适用于复 Fourier 系数。

由 $\|(J-w)/w\|\le3\mathfrak n_{s,2}$、Banach 逆级数，
可安全取 $\|J^{-1}\|<2/w$、
$\|D\|,\|T\|<2$。在 (C.7) 保留每个分量后有
$$
 \|f\|_{\mathcal A_s}\le8w\mathfrak n_{s,2},\qquad
 \|f_\theta\|_{\mathcal A_s}\le32w\mathfrak n_{s,2}.
$$
(C.8) 的第二分量括号至多
$16w\mathfrak n_{s,2}+600w\mathfrak n_{s,2}^2$。
因 $1/\sqrt{12}<1/3$，两个分量的和远小于下面的安全常数：
$$
 \boxed{\quad
 \|\mathcal R_p\|_{\mathcal A_s}+\|\mathcal R_k\|_{\mathcal A_s}
                  <2^{10}w\mathfrak n_{s,2}.
 \quad}                                                     \tag{C.14}
$$
输出是两个分量的 $\mathcal A_s$ norm 之和；输入的两个角导数已全部在
$\mathfrak n_{s,2}$ 中，没有再次要求输出的两个角导数。

写 $n_I=\sup_I\mathfrak n_{s,2}$。真实 compact 方向于是给
$$
 \sup_I w^{-1}\|\psi F_1\|_{\mathcal A_s}
          \le8n_I\rho^4,\qquad
 \boxed{\quad
 \int_I w^{-1}\|\psi\mathcal R\|_{\mathcal A_s}\,dy
                   <2^{11}\eta_j n_I\rho^5 .
 \quad}                                                     \tag{C.15}
$$
径向 $w$ 在积分中逐点归一，未用 $w_{\max}/w_{\min}$ 制造额外损失。
这是真实背景的完整 forcing 费用；尚不是将其传播到所有标签的费用。

## 5. 原 canonical 状态中的修正其实为二次

对每个 $m\ne0$，原完整状态为
$$
 W_1=\nu_m v_m/r^4,\qquad
 W_2=\frac{p_*}{\sqrt{12}r^3}(k_m+(p_\theta)_m),
 \quad \nu_m=m^2(m^2-1)/12 .
 \tag{C.16}
$$
$p$ 在控制流 $\mathcal B$ 下不变，所以非mean $v$ 不变。
对 $W_2$ 同时微分真正的 $p_*$ 因子，得到
$$
 \mathcal B_W=
 \binom0{\frac{p_*}{\sqrt{12}r^3}\Pi_\perp(f+k+p_\theta)},
$$
$$
 f+k+q=\frac{k^2+2Ekq+Eq^2-w^2p^2}{J}.                     \tag{C.17}
$$
因此
$$
 \|\mathcal B_W\|_{\mathcal A_s}
                   <8(p_*w/r^3)\mathfrak n_{s,2}^2.
 \tag{C.18}
$$
只对物理 $(p,k)$ 修正而漏掉 canonical 第二行的 $p_*$ 微分，会留下
一个假的线性控制项；(C.17) 给出其准确取消。mean 始终用第3节，
不把 $m=0$ 代入退化的 $\nu_m$。

在 $M=1$ 的同一真实 mean 图上，canonical 全方程可以写成
$$
 W_y=\mathcal F_0(W,p_*,r)+b\,\mathcal B_W(W,p_*,r).
$$
确切定义是令 $\mathcal Tz$ 为 (C.16) 的线性角算子，则
$\mathcal F_0=-3W/\sqrt{12}+\mathcal T(V-7F_1/\sqrt{12})$；
mean 依原小根取值。所有 $p_*,r$ 偏导都包括该真实小根的导数。
令 $\widehat W=\dot W-\psi\mathcal B_W$，同一计算给
$$
 \widehat W_y=D_W\mathcal F\,\widehat W+\psi\mathcal R_W,
$$
$$
 \boxed{\quad
 \mathcal R_W=p_*\partial_{p_*}\mathcal F_0
  +D_W\mathcal F_0\,\mathcal B_W-D_W\mathcal B_W\,\mathcal F_0
  -\frac r{\sqrt{12}}\partial_r\mathcal B_W.
 \quad}                                                     \tag{C.19}
$$
仍没有 $\psi_y$。原点线性项准确是
$$
 (\mathcal R_W)_{\rm lin}
 =\begin{pmatrix}0&-\nu_m/p_*\\-p_*&0\end{pmatrix}W_m,
 \tag{C.20}
$$
因为 $\mathcal F_{0,\rm lin}=A_{m,p_*}W$ 而
$\mathcal B_W=O(W^2)$。式 (C.20) 恰为原真实两行矩阵的
$\partial_{\log p_*}$，不是理想剪切的导数。

所有离散端口及标签处 $\psi=0$，故 $\widehat W=\dot W$。
原 $\zeta_j,\tau_j$ 在这种 fixed-shape 变化中不变。
因此 (C.19) 确定的有源局部输出，按原完整规范组成 $g_\psi$ 后，
固定原标签的全响应准确满足
$$
 \dot X=(I-\mathcal G D\mathscr N(X))^{-1}\mathcal Gg_\psi .
 \tag{C.21}
$$
这里 $g_\psi$ 必须由实际局部线性化 flow 传播
$\psi\mathcal R_W$ 得到，不能只用 (C.15) 的积分替代。
原完整图在整个 $C^4$ 参数球上的可微性先给其粗空间归属，原 Neumann
给这一公式的唯一性；这里没有先假定新的 $\rho^5$ 传播界。
它保留两个 source 状态和全部 Fourier，不将 $g_\psi$ 擅自置零。

## 6. 两条真实射线也可消去方向的径向导数

回到物理 $t$，令 $Q=7-\partial_t\log p_*>0$、
$q_0=\sqrt Q$。本节 $q_0$ 与第1节 $q=p_\theta$ 不同。
在同一 actual background 上，准确有
$$
 d=\frac{E(k_\theta-p)}J,\qquad
 v_*=\frac{w\sqrt D}J,\qquad
 g_\sigma=-d-\sigma q_0v_*,\qquad
 (H_\sigma)_t=g_\sigma(t,H_\sigma).
 \tag{C.22}
$$
正是此前 $\nu=q_0v_*$ 的实际两个速度。
记 $S_\sigma=H_\sigma^{-1}$、
$\mathcal V_\sigma=\dot H_\sigma\circ S_\sigma$。
直接微分真 flow 得
$$
 \mathcal L_\sigma\mathcal V_\sigma=\dot g_\sigma,\qquad
 \mathcal L_\sigma=\partial_t+g_\sigma\partial_\theta
                                          -(g_\sigma)_\theta.
$$
因为 $\dot Q=-\psi_t$，令
$$
 c_\sigma=\frac{\sigma v_*}{2q_0},\qquad
 \widehat{\mathcal V}_\sigma=\mathcal V_\sigma-\psi c_\sigma ,
$$
则完整 source 准确变为
$$
 \boxed{\quad
 \mathcal L_\sigma\widehat{\mathcal V}_\sigma
 =-D_zd[\widehat z]-\sigma q_0D_zv_*[\widehat z]
 -\psi\{\mathcal Bd+\sigma q_0\mathcal Bv_*
                                      +\mathcal L_\sigma c_\sigma\}.
 \quad}                                                     \tag{C.23}
$$
$z$ 的参数变分与材料坐标换算按 (C.6) 使用，$\widehat z$ 是同一个场。
本式没有 $\psi_t$；原背景的 $q_{0,t}$ 仍真实存在。准确有
$$
 \mathcal L_\sigma c_\sigma
 =\frac{\sigma}{2q_0}
       [(v_*)_t-d(v_*)_\theta+v_*d_\theta]
                 -\frac{\sigma v_*q_{0,t}}{2q_0^2}.
 \tag{C.24}
$$
两个 $\sigma q_0v_*(v_*)_\theta$ 项相消，不以独立绝对值重复收费。

控制系数可完全从原状态算出：
$$
 \frac{\mathcal Bv_*}{v_*}
 =1-\frac{w^2(T+2Kq+Eq^2)}{J^2},\quad
 \mathcal BJ=\frac{w^2(T+Kq+2qJ)}J,
$$
$$
 \mathcal Bd=\frac E J f_\theta
                      +d\left(\frac{2w^2}E-\frac{\mathcal BJ}J\right).
 \tag{C.25}
$$
第4节同一代数球给
$\|\mathcal Bd\|+\|\mathcal Bv_*\|<2^{10}n_I$。
在径向原点，它们准确为0，而 (C.24) 为
$-\sigma q_{0,t}/(2q_0^2)$。实际 phase-annihilator 仅使这个
**径向**完整 endpoint 积分为0，不删除 (C.23) 的非径向剩余。

所有 $\psi c_\sigma$ 只在真 $q_0>0$ 的 compact 支集上定义，然后在
其余处以0延拓。因此没有跨越转向点除以 $q_0$，与 root collar 接合的左右真实 strict
切口上 $\widehat{\mathcal V}_\sigma=\mathcal V_\sigma$。

## 7. 完整 fixed-label kernel 的强微分，不是假同宽 pullback 导数

对任意真实角图，记
$C_Su=u\circ S$、$D_Hu=H'(u\circ H)$。
对光滑输入直接求导，
$$
 \dot D_Hu=D_H\partial_\theta(\mathcal V u),\qquad
 \dot C_Su=-\mathcal V\,\partial_\theta C_Su .
$$
令 $\partial_\theta^{-1}$ 在全部非mean Fourier 上按准确频率定义。
原完整波核
$\mathscr K_{\sigma\tau}=D_{H_\sigma}M_\kappa
 C_{S_\tau}\partial_\theta^{-1}$ 的导数于是为
$$
 \boxed{\begin{aligned}
 \dot{\mathscr K}_{\sigma\tau}
 ={}&D_{H_\sigma}M_{\dot\kappa+
                      (\kappa\mathcal V_\sigma)_\theta}
                           C_{S_\tau}\partial_\theta^{-1}\\
 &+D_{H_\sigma}M_{\kappa(\mathcal V_\sigma-\mathcal V_\tau)
                                          (S_\tau)_\theta}
                           C_{S_\tau}\Pi_\perp .
 \end{aligned}}                                             \tag{C.26}
$$
两支相同时第二行准确为0；跨支时不能删除它。所有 Fourier lag
和改变符号的输入输出仍在两个完整 composition 中。

对于任一有限 Sobolev 阶，右边是有界算子，费用来自显示的系数及真实
图的相应有限角导数。沿参数紧区间有统一费用时，(C.26) 在每个固定
输入上强成立：先在光滑稠密子空间证明，再用统一有界性取极限。
这不声称算子 norm 可微。即使平移 $C_\epsilon\partial^{-1}$，
同空间差商也可在 $|m|\asymp|\epsilon|^{-1}$ 上不按 norm 收敛；
不能对 naked pullback 使用 Banach-valued Cauchy 来省掉这一点。

两 mean 及所有低项必须由完整式一起微分。令
$X_\sigma=Z_\sigma+\sigma\alpha$、$\langle Z_\sigma\rangle=0$，则
$$
 w=c+\alpha(S_+-S_-)
       +\sum_\sigma C_{S_\sigma}\partial_\theta^{-1}Z_\sigma,
$$
$$
 \alpha_t=-\langle\kappa w\rangle/2,\quad
 (Z_\sigma)_t=-\frac{\sigma}2\Pi_\perp D_{H_\sigma}(\kappa w),
$$
$$
 c_t=-\alpha_t\langle S_+-S_-\rangle
       -\sum_\sigma\left\langle
          C_{S_\sigma}\partial_\theta^{-1}(Z_\sigma)_t\right\rangle .
 \tag{C.27}
$$
因此微分时同时保留 $\dot\alpha_t,\dot c_t$、两个逆图、
$\dot\kappa$ 及它们作用于 $w$ 的全部列。
(C.26) 只是 (C.27) 的四个波—波块；它从来没有取代全系统。

## 8. 真实物理端图、全部 source 及当前 $\Gamma$

用此前真实散度密度 $G$，令
$\Lambda=\sqrt{-\det G}$、$\ell=\log\Lambda$、
$T_\ell=(G^{tt}\ell_t+G^{t\theta}\ell_\theta)/2$。
本节的 $T_\ell$ 与第1节 $T=1-p^2$ 不同。
以下端点是 $\Lambda>0$ 的真实 strict 切口；到根处的 Airy 两迹仍须经原
完整 root 图，不能在 $\Lambda=0$ 处直接套本式。
从当前标签状态 $Y=(c,\alpha,Z_+,Z_-)$ 恢复
$$
 y_\sigma=(S_\sigma)_\theta
                      (Z_\sigma+\sigma\alpha)\circ S_\sigma,\qquad
 \zeta=y_+-y_- .
$$
完整 height/total-flux 端图准确是
$$
 \boxed{\quad
 \mathscr P_eY=
 (u,\pi)=
  (\Lambda^{-1/2}w,\,
        \sqrt\Lambda\,\zeta-T_\ell\Lambda^{-1/2}w).
 \quad}                                                     \tag{C.28}
$$
对 weak 源，$\pi$ 是 total flux；恢复 bare flux 最后减真实 $F^t_e$。
内部弱源 norm 不自动授予该端点迹。
(C.28) 包含高度 mean $c$、flux mean $\alpha$，以及真实逆图对其的混合。

固定同一个当前 $\Gamma$，记实际和径向参考的端图为
$\mathscr P_e,\mathscr P_e^0$，两者使用同一物理切口。
若 $C_H=U_0E$ 是第58束自己的准确 principal 坐标中的传播，则
$$
 C_{\rm phys}=\mathscr P_R U_0E\mathscr P_L^{-1}.
 \tag{C.29}
$$
等价地，令 $B_e=\mathscr P_e(\mathscr P_e^0)^{-1}$，
$$
 C_{\rm phys}=B_R C_{\rm phys}^0
       [\mathscr P_L^0E(\mathscr P_L^0)^{-1}]B_L^{-1}.
 \tag{C.30}
$$
$B_e$ 是实际 canonical/Fourier-integral 端口变换；没有把它按 norm
换成 $I$。正型 DN、root、source charge 必须在同一个 $B_e$ 下接合。

对光滑全数据，真实参数导数是
$$
 \dot C_{\rm phys}
 =\dot{\mathscr P}_R C_H\mathscr P_L^{-1}
  +\mathscr P_R\dot C_H\mathscr P_L^{-1}
  -C_{\rm phys}\dot{\mathscr P}_L\mathscr P_L^{-1}.
 \tag{C.31}
$$
端图导数含实际 $\mathcal V_\sigma\partial_\theta$、density 和
normal-shear 导数，通常为一阶 FIO。
它可按真实系数界从 $H^{s+1}$ 到 $H^s$ 消费，而不是无条件的
$H^s\to H^s$ 小算子。对输入频带 $M\le|m|\le2M$，该一阶费用可乘
$1+2M$；输出仍在完整 $H^s$，并未被截断。

若在两参数联立图上取总导数，准确应加
$$
 D_\Omega^{\rm total}
 =\partial_\Omega\big|_{\Gamma}
       +(D_\Omega\Gamma_1^*)\partial_{\Gamma_1}
       +(D_\Omega\Gamma_2^*)\partial_{\Gamma_2}.          \tag{C.32}
$$
两个系数由真实无限 phase 方程微分决定；径向原点的一阶补偿为0，
不意味着非零标签的这两列为0。
参考 $U_0,\mathscr P_e^0$ 也按同一当前 $\Gamma$ 微分。

ordinary 与 weak 源保持前篇真实换元
$F_d=\Lambda^{-1/2}F$、
$f_d=\Lambda^{-1/2}(f-\tfrac12\nabla\ell\cdot F)$，
并保留两个 total/bare 端荷。
参数求导加入这些实际密度、图和输入源的导数，不产生
$F^t_t$ 的未付 norm。
仿射散射仍是 $q=b_--Sb_+$，故
$\dot q=\dot b_--\dot S b_+-S\dot b_+$；两个 mean 都在 $b$ 中。

## 9. 本结论支付到哪里，下一笔实际费用是什么

本文已经给出该真实尾、该 compact 方向、该非零标签背景的
(C.6)、(C.8)、(C.15)、(C.17)–(C.21)。
因此方向的径向高导不是完整背景响应的必需 source 费。
两个实际射线、完整角混合和物理端图也已由
(C.23)、(C.26)、(C.28)–(C.32) 精确指定。

尚待定量的是把 $\psi\mathcal R_W$ 经过同一 actual 局部有源 flow
得到 $g_\psi$，在原 $\mathcal F_\beta$ 和随后 $\mathcal X_\beta$
中保持足够的 $\rho$ 次幂；以及将由此获得的
$\dot\kappa,\mathcal V_\sigma$ 送进完整 (C.26)–(C.27)。
只有付清这些量，才可把第58束的强微分消费者 (R.12) 用于真正
非径向 near-resonant cluster。
本篇没有由 $\sum64\eta_i$、裸角差或未传播的 (C.15) 宣称
physical network 差已经小于第57束的真实小 Wr 门。

[新准确代数程序](../scripts/fourfold_actual_compact_profile_flux_gauge_20261114.js)
与[实际执行记录](../notes/2026-11-14-R119-actual-compact-profile-flux-gauge-budget.json)
核查本篇完整有理恒等式和数字包络。没有恢复或冒称原 Python native。
