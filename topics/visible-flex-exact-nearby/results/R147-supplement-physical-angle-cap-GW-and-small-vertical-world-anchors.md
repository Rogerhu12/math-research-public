# R147 PWA：物理角 GW 与实际帽的完整竖直小锚

2026-11-28，visible-exact-astra-b0d5a16-20261128 / cap_world。

**已证明。** 对 [CW](R147-supplement-actual-cap-world-anchors-and-supported-nu-height.md)
的同一个真实 reflected M cap、同一个 axial world、同一个高度常数
$\lambda$，以及下方同一 selected passive core，在 $b=9/50$ 有

$$
 \boxed{a_0<3.649\,10^{-6},\qquad p_0<8.56\,10^{-6}.}       \tag{PWA.1}
$$

这两个完整 actual-anchor 槽可直接用于 H96。其锚误差变成
$ .00005185 H_j+.000011056 G_j$，并且保留原数值 kernel 误差、
两个 mean、腰的坐标项和所有独立 world ports。整个原帽积分、
reference height、RHI 与 H96 trial 积分均不重算。

关键是先在**同一个物理角**中比较真实帽与原 raw radial model，
完整支付 raw residual 产生的角速度缺陷，最后才回到原 moving
angle。原 $R$ 端的竖直 row 和高度恰与角无关；$L$ 端的真角差
则乘已证明的小竖直导数，不能省略它或把两个角坐标混为一谈。

## 1. 对象、完整旧输入和几个准确标量关系

固定 $L=9/10,R=25/8,\eta=\eta_0$。保留 M/CW 的原 product：
$\|\gamma_{\rm in}\|_{A^0}<10^{-9}$、
$\|f_B\|_{\dot A^2}<2^{-60}$，以及几何实现所需的原有限正则性。
下文 $\gamma$ 单指本征径向系数，不指 inner input。
本条不证明尚未进入这个 product 的未知 core 已合格。

记真实帽为 $W_*=(B_*,C_*)$，连续修补中心为 $\widehat W$，
原 raw moving pair 为 $U^0=(u^0,v^0)$。原 raw frame/position 为
$\mathsf Q^0,F^0$，保留 determinant $-1$ 的法向约定。
[CG](R133-supplement-actual-cap-in-final-geometry-C0-ball.md)
已对这个实际存在的帽证明

$$
 t=\|W_*-\widehat W\|_{X_0}<t_*:=2.684\,10^{-6},
 \qquad \|\widehat U-U^0\|_{\mathscr A_{1/32},{\rm pair}}
       <\epsilon:=5\,10^{-18}.                         \tag{PWA.2}
$$

两 mean 和所有 Fourier modes 在这两个完整范数内。
[C 的原完整 native](../notes/2026-11-14-R133-complete-C0-state-nu-geometry-response-identities.json)
经 [LCW](R147-supplement-local-cap-anchors-from-complete-saved-geometry.md)
整件恢复、核 SHA 和7722行覆盖后，原 row6376 与1753已经给出

$$
 S:=\int_L^R a\gamma\,dr
   \le\int_L^R|c_0|\,dr<.583398=:S_*,\qquad
 \int_b^R|c_0|\,dr<1.713494=:J_* .                     \tag{PWA.3}
$$

这里 $c_0=(a\gamma,a\tau_0,0)$，故第一行只是限制同一已存
非负积分的一个分量。没有减去两个 upper 来恢复子区间长度。

[完整本征 run43674917925/1](../notes/2026-11-15-R133-actual-cached-complete-cap-intrinsic-bounds.md)
的 whole summary/process 给整个帽上的

$$
 |\beta|<5.64,\qquad 0<\gamma<5.64,\qquad 0<K<.255.   \tag{PWA.4}
$$

同一 rotational reference 满足 $C_{\rm ref}<0$，
$\ell=K/C_{\rm ref}^2$。其已成
[all-mode Green](R133-supplement-actual-final-all-mode-physical-cap-Green.md)
的两个**定义关系**还给

$$
                         .9<\ell<2.                  \tag{PWA.5}
$$

下界来自准确 $K_0=(1+\ell_-)^{-1}<.523455817<10/19$。
上界使用原 suffix enclosure 的具体构造：每盒的 upper root 是
$(d_++\sqrt{d_+^2+4\ell_+})/2$，其中 $d_+\ge0$；原 $q_+$
包含这个 root，因此 $\ell_+\le q_+^2$。
原全帽 $q_+<1.389936764$，其平方小于2。
这个推导使用原 coefficient enclosure 的根定义，绝非从一个
未知解的 norm upper 反推出未知系数。

CW.18–21、ACT.7–8 以及原 cap coefficient table 给

$$
\begin{gathered}
3<|m_0|<6,\quad |v^0|<6,\quad |u^0|<1/50,
\quad j_0=v^0/m_0>31/32,\quad
\|j_0\|_{\mathscr A_0}<33/32,\\
\|\Omega_{\phi,0}\|<2.157,\quad |c_{\phi,0}|<4.001,
\quad a<4.131,\\
\|E_0\|<\varepsilon_Q:=3.127699\,10^{-8},\qquad
|P_0|<\varepsilon_F:=4.956566\,10^{-8}.                 \tag{PWA.6}
\end{gathered}
$$

$E_0=(\mathsf Q^0)_\phi-\mathsf Q^0\Omega_{\phi,0}$、
$P_0=(F^0)_\phi-\mathsf Q^0c_{\phi,0}$ 是原完整非零 angular
defects，包含每个原接口，不把 raw model 当成 GC 解。

## 2. Raw/repaired 角桥只占明确的极小费用

令 $\Theta_0:\phi\mapsto\theta$ 是 raw curvature angle，
$\Phi_0=\Theta_0^{-1}$；加帽号和星号分别指 repaired 与 actual。
在整条 raw-to-repaired 直线路径上，有
$|v|>2.9,|m|>3,|u|<.021$，
$|u_\phi|<.084,|v_\phi|<.376$ 和 $j>31/32$。
这些量来自同一完整 table 与 (PWA.2)，并留有严格余量。
改变均值时准确地

$$
 \Delta(v/m)=\frac{\Delta v}{m+\Delta m}
             -\frac{v\Delta m}{m(m+\Delta m)}.
$$

完整 $\mathscr A_0$ 范数、$\|I\|=1/4$ 与 inverse slope
$32/31$ 给

$$
 \|\widehat\Phi-\Phi_0\|_\infty<\epsilon .            \tag{PWA.7}
$$

同样，在相同 physical angle 下用
$A=Kv+u^2/v,B=u/v,C=1/v$ 比较，得到足够宽松的完整界

$$
 \|\widehat A-A_0^p\|_\infty+
 \|\widehat B-B_0^p\|_\infty+
 \|\widehat C-C_0^p\|_\infty<20\epsilon.               \tag{PWA.8}
$$

例如这些三个 moving readout 对 state 的差分系数和小于1；
其原 moving angular derivatives 的和也小于1。
先比较同一 moving label 的商，再用 (PWA.7) 比较已知 reference
的两个评价点，即已足够给 $2\epsilon$，此处仍保守用20。
这不涉及未知帽的角导数。

CG.8–9 的准确 changing-mean 恒等式及 $|m_*|<7$ 进一步给

$$
 \|\Phi_*-\widehat\Phi\|_\infty
 \le {7\over4}\|C_*-\widehat C\|_{\mathscr A_0},
 \quad
 \|\Phi_*-\Phi_0\|_\infty<{7\over4}t+\epsilon.       \tag{PWA.9}
$$

这保留真实 even mean。reflection 固定同一 integration constant；
没有另外选一个匹配相位。注意这里只需 physical-to-moving 的
$\Phi$，不必再乘一个 inverse-angle Lipschitz 常数。

## 3. 在物理角中精确保留 raw residual

原完整 moving identity 中，置
$S_0=(u^0)^2+K(v^0)^2$，
$d_0=-\beta I S_0$，$\tau_0=d_0j_0-\gamma u^0$。
原方程的真实残差为 $R_u,R_v$，$R_0=\Pi R_v$。准确的角速度是

$$
 (\Theta_0)_r=\tau_0+e_0,\qquad
 e_0={1\over m_0}I(R_v-j_0R_0),\qquad
 (\Phi_0)_r=-{\tau_0+e_0\over j_0}\circ\Phi_0 .       \tag{PWA.10}
$$

不能删除 $e_0$。对每个原 piece 定义
$q_0^p=e_z^T\mathsf Q^0\circ\Phi_0$、
$f_0^p=e_z^TF^0\circ\Phi_0$，并令

$$
 M_0^p=\Omega(0,a\gamma A_0^p,a\gamma B_0^p).
$$

将原 $M_0$ 减去 $\tau_0\Omega_{\phi,0}/j_0$，三个 skew
entries 正好成为 $(0,a\gamma A_0,a\gamma B_0)$。
完整 chain rule 因而给

$$
\begin{split}
 (q_0^p)_r&=q_0^pM_0^p
   -q_0^p\Omega_{\phi,0}^p(e_0/j_0)^p
   +(e_z^TE_0)^p(\Phi_0)_r,\\
 (f_0^p)_r&=q_0^p(a\gamma,0,0)^T
   -q_0^p(0,ae_0^p,0)^T+(e_z^TP_0)^p(\Phi_0)_r.
                                                        \tag{PWA.11}
\end{split}
$$

真实帽在同一物理角准确满足
$(q_*^p)_r=q_*^p\Omega(0,a\gamma A_*,a\gamma B_*)$、
$(f_*^p)_r=q_*^p(a\gamma,0,0)^T$。
固定本征度量使两个径向 position velocities 的第一分量相同。

[原完整7296-row residual](../notes/2026-11-14-R133-final-complete-moving-residual.md)
给 $\int\|R_v\|_{A^0}dr<5.237515\,10^{-8}$；原表是 standardized
残差，physical moving 残差乘 $\alpha<1$，此处合法保留较大上界。
因此

$$
 \int_L^R\|e_0\|_\infty dr
 \le{65\over384}\int\|R_v\|_{A^0}dr<9\,10^{-9}=:E_* .
                                                        \tag{PWA.12}
$$

这里 primitive 的输入严格 zero mean，$j_0R_0$ 中的 mean 未去掉。
原完整 $Q_C=\ell-(u^0)^2-K(v^0)^2$ 在 moving joint
$\mathscr A_{1/32}$ 范数中小于 $.051432066$；故
$d_0=\beta I Q_C$。使用 (PWA.4),(PWA.6) 得

$$
\begin{split}
 \int_L^R\|(\Phi_0)_r\|_\infty dr
 &\le{89\over40}\,5.64
       \left({.051433\over4}+{32\over31\cdot50}\right)
       +{32\over31}E_*\\
 &<.421=:V_* .                                         \tag{PWA.13}
\end{split}
$$

原 raw $\mathsf Q^0,F^0$ 在径向连续，$\Phi_0$ 在原 candidate
interfaces 可以跳。完整原 $v$ jump 的 $A^0$ 和小于
$6.408789\,10^{-13}$。同一个 changing-mean 商及 inverse slope
给 $\sum\|[\Phi_0]\|_\infty\le(65/372)6.408789\,10^{-13}$。
用原 whole $\|\mathsf Q^0_\phi\|<2.156,|F^0_\phi|<4$，
两项 physical pullback jump 的总和各小于 $10^{-12}$。
它们以下作为真实 impulses 加入，不以一侧值代替另一侧。

于是 (PWA.11) 的完整 forcing-plus-jump 预算为

$$
\begin{split}
 Z_Q&\le2.157{32\over31}E_*+\varepsilon_QV_*+10^{-12}
                       <3.33\,10^{-8}=:z_Q,\\
 Z_F&\le4.131E_*+\varepsilon_FV_*+10^{-12}
                       <5.81\,10^{-8}=:z_F.            \tag{PWA.14}
\end{split}
$$

这些费用在原 ordinary $dr$ 上，覆盖整个帽与全部原 interfaces。

## 4. 先界 raw 的竖直角导数，再支付真正的相位差

只用完整旧 coefficients 构造同一本征 rotational vertical row

$$
 q_{\rm rot}=(-aC_{\rm ref},0,-\beta/\gamma).
$$

准确 intrinsic identities
$a^2C_{\rm ref}^2+(\beta/\gamma)^2=1$、
$C_{\rm ref}'=\beta(A_{\rm ref}-C_{\rm ref})$ 与
$(\beta/\gamma)'=-a^2\gamma K$ 给

$$
 |q_{\rm rot}|=1,\quad
 q_{\rm rot}'=q_{\rm rot}\Omega(0,a\gamma A_{\rm ref},0),
 \quad q_{\rm rot}\Omega_{\theta,\rm ref}=0,
 \quad\|\Omega_{\theta,\rm ref}\|=1,                    \tag{PWA.15}
$$

其中 $\Omega_{\theta,\rm ref}=\Omega(\beta/\gamma,0,aC_{\rm ref})$。
这些是原 positive reference 的准确恒等式，并非新 radial target。
在 $R$，RA.3、RA.19–20 给 $q_0^p=q_{\rm rot}$ 恰成立。

为界完整 raw curvature 偏差，令 $s=1/C_{\rm ref}<0$。
$Q_C+u^2=\ell(1-v^2/s^2)$，(PWA.5) 给

$$
 |1-v^2/s^2|<{.051432066+(1/50)^2\over.9}<.058.
$$

$v/s>0$，故 $v/s>.97$。原 repaired physical table 与
(PWA.8) 给 raw $|C_0^p|<.319,|B_0^p|<.0063$，因此

$$
 |C_0^p-C_{\rm ref}|<.319{.058\over1.97}<.0094.
                                                        \tag{PWA.16}
$$

由 $|1/C_0^p|<6$ 及完整 Gauss quotient，

$$
 |A_0^p-A_{\rm ref}|+|B_0^p|
 <2(.0094)+6\{(.0063)^2+2(.0094)^2\}+.0063<.0264.
$$

(PWA.11),(PWA.14) 与正交 Duhamel 因而证明整帽

$$
 \|q_0^p-q_{\rm rot}\|_\infty
 <S_*(.0264)+z_Q<.015402=:r_0.                         \tag{PWA.17}
$$

现在用原 angular GW **defect identity**，不对 $C^0$ 界求导。
因为 $\Omega_{\phi,0}=j_0\Omega_{\theta,0}$，且
$q_{\rm rot}\Omega_{\theta,\rm ref}=0$，在完整 original moving
angle 上

$$
\begin{split}
 \|(e_z^T\mathsf Q^0)_\phi\|_\infty
 &\le{33\over32}r_0+4.001(.0063+.0094)+\varepsilon_Q
                         <.0787=:G_z,\\
 |(e_z^TF^0)_\phi|&\le4.001r_0+\varepsilon_F
                         <.061624=:F_z.              \tag{PWA.18}
\end{split}
$$

第二式保留 $P_0$ 并用 $q_{{\rm rot},Y}=0$。
这是竖直 row 的新小界；没有把整个 frame 的 rotation derivative
假装很小。参考的完整 angular defects 正是两式最后一项。

## 5. 真帽的 physical radial 差与原 moving L 锚

对 $x=(b,c)=W_*-\widehat W$，完整 Gauss remainder 给
$A_*-\widehat A=-\ell c+Q_Bb+Q_Cc+\mathcal N_2(x)$。
已成 repaired bounds 是 $\|Q_B\|<.039196064$、
$\|Q_C\|<.051432066$、$\|\mathcal N_2(x)\|\le13t^2$。
(PWA.5),(PWA.8) 因而给完整 pair

$$
 \|A_*-A_0^p\|_\infty+\|B_*-B_0^p\|_\infty
       <2.052t+13t^2+20\epsilon.                       \tag{PWA.19}
$$

同一 RA $R$-anchor 是 $r_q=10^{-12},r_f=6\,10^{-21}$。
RA.20 的 raw vertical row 与 RA.3 的 raw height 均与角无关，故这
两个界在同一 physical angle 下原样成立，无须也不能虚构一个
新的 endpoint gauge。位置始终模原一个 $\lambda$。

用 skew 变系数的正交 Duhamel，(PWA.11),(PWA.14),(PWA.19)
在**整个帽**证明

$$
 Q_p:=\|q_*^p-q_0^p\|_\infty
 <r_q+S_*(2.052t_*+13t_*^2+20\epsilon)+z_Q
 <3.247\,10^{-6}.                                    \tag{PWA.20}
$$

对应物理位置差上界是 $r_f+S_*Q_p+z_F$。
最后返回同一 moving label。准确分解中的第二项为
$q_0(L,\Phi_0(\Theta_*(\phi)))-q_0(L,\phi)$；由
$\Phi_*(\Theta_*(\phi))=\phi$，它的距离不超过 (PWA.9)。
于是原 moving $L$-ports 满足

$$
\begin{split}
 A_{0,L}&<3.247\,10^{-6}+G_z({7\over4}t_*+\epsilon)
                         <3.617\,10^{-6},\\
 P_{0,L}&<r_f+S_*(3.247\,10^{-6})+z_F
                    +F_z({7\over4}t_*+\epsilon)
                         <2.243\,10^{-6}.             \tag{PWA.21}
\end{split}
$$

这个末项就是完整真实相位费用。没有用 $C^0$ 推未知 $C^1$，没有
把 raw residual、两侧 jumps 或 changing mean 归零。

## 6. Selected core、完整弱 receiver 与 particular height

在 $[b,L]$ 原 ACT 差分预算保持
$D=15.736315(2\,10^{-9})$、$E=30.196406(2\,10^{-9})$。
由其准确径向方程和 (PWA.3)，

$$
 a_0<A_{0,L}+3.148\,10^{-8}<3.649\,10^{-6},\qquad
 p_0<P_{0,L}+J_*(A_{0,L}+D)+E<8.56\,10^{-6}.          \tag{PWA.22}
$$

它们仍比较 actual cap-anchored **passive** core 和原 raw model；
未完成的 $L$ 曲率匹配不由此变成事实。没有在 $L$ 或 $b$ 再做平移。

对一阶锚可直接用 CW.24 的真帽 angular equations，保留 CG 的
moving value 界 $e=.000099309$，得到

$$
 A_{1,L}<.000413,\quad B_{1,L}<.000425,\qquad
 a_1<.000466,\quad b_1<.001417.                        \tag{PWA.23}
$$

这里仍付完整 $E_0,P_0$；selected core 用 ACT.1，未将 core 有限
degree bound 外推到实际帽。原 WRA 全四行故可改用

$$
 |\mathcal L_b(h)|<94013(D_*+J_-)+6651F_-
                                      +3001F_{\rm st}+8852J_{\rm st}.
                                                        \tag{PWA.24}
$$

全部原 weak source spaces、ordinary $dr$、true root/strict ports
及独立 $\Pi J e_z^T(Y_b+K_b\mathsf Q_bx)$ 保持。

对 CW 明确定义的 supported NP particular，整个 $r\ge b$ exterior、
两个 cap inputs、world placement 与 $\lambda$ 皆冻结，仍由准确
几何 ODE 唯一性给 $Y_b=K_b=0$。消费原 AWH 的两个完整 norm，

$$
 .031082487a_0+.006877446p_0<1.73\,10^{-7},
$$

同一未归一化列的实际 cap-anchored mean-height 因而满足

$$
 \boxed{-.025370374<c_H<-.025229626<0,
                         \qquad |c_H^{-1}|<39.64.}     \tag{PWA.25}
$$

该结论保留原 reference interval $[-.0253702,-.0252298]$ 的全部
数值误差，并未重积分或改变 particular 的定义。

## 7. H96 的完整误差替换与复用界限

H96 的完整锚表达式仍是

$$
 (k_q+a_0)14.20875H_j+(k_f+p_0+.684a_0)G_j.
$$

使用 (PWA.1) 可直接重组为

$$
 14.20875k_qH_j+k_fG_j+.00005185H_j+.000011056G_j.       \tag{PWA.26}
$$

必须从同一 whole H96 conclusion 读取原 $H_j,G_j,k_q,k_f$ 与
完整 signed centers，再对整个公式付费。不能从旧 error subtotal
减去某个 norm upper。原腰项、independent world ports、两 mean、
原 normalization/phase 与 full finite/high correction 全部仍在。

配套 [exact reader](../scripts/fourfold_codazzi_physical_angle_cap_anchor_saved_bounds.py)
已验证整件旧输入、读取 whole saved bounds 并**一次完成42个新
有理比较，全部通过**；旧 scientific target 调用数0。其 source
SHA256 为 `a94ddfc8069b979dc152c31b4c985ed2e2499dde2fcaae67257e7b0cc884817c`。
它不执行任何旧 coefficient、Green、geometry 或 height target。
本文没有宣称尚未完成的完整 Schur、nonlinear core 或最终冻结闭族
已经存在。
