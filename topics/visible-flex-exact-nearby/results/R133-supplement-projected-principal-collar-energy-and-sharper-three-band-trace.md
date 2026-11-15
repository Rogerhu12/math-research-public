# R133：正 collar 的投影主部能量与三带迹收尖

状态：精确解析补篇，供独立核对。原 LT 及成功 NR 数值均保持原样；本篇没有新数值执行。

依赖 [正 collar 完整能量 E](R133-supplement-positive-collar-energy-and-residual-sensitive-first-angular-cut-trace.md)、[LT 三带迹](R133-supplement-finite193-middle-band-and-infinite-collar-trace.md) 和 [NR 消费者](R133-supplement-saved-nonmean-restriction-and-three-band-trace-consumer.md)。所有圆周测度、物理频率 $4j$、径向 $dr$、$P$、真实 mean 及 rank-one 项与这些原件相同。

## 1. 固定投影下的精确能量

**(PE1)** 令 $\mathsf H$ 为固定 Fourier 正交投影，在两分量上采用相同频率集合；因此它与 $\partial_\phi$、径向标量、径向 cutoff 和
$$
J_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix}
$$
交换。令 $a=a(r)$ 为真实、连续、正的径向系数，$d=d(r,\phi)$ 为真实标量。假定同原 E 的弱导数域，$a\in W^{1,\infty}$，且
$$
a\ge a_->0,\qquad |a_r/a|\le L,\qquad |d|\le d_+.
$$
这些都是实际背景的条件；复方向可取值于复 Hilbert 空间，但不能据此把背景 $a,d$ 改为复值。

在 $\operatorname{ran}\mathsf H$ 上定义
$$
\mathcal L_{\mathsf H}u
=u_r-\mathsf H(d\,u_\phi)+aJ_0u_\phi,\qquad u=\mathsf Hu. \tag{PE1}
$$
设 $u$ 在径向两端零。完整圆周 Hilbert 配对给
$$
\operatorname{Re}\langle\mathsf H(d u_\phi),aJ_0u_\phi\rangle
=\operatorname{Re}\langle d u_\phi,aJ_0u_\phi\rangle=0. \tag{PE2}
$$
第一步用正交投影和 $aJ_0u_\phi\in\operatorname{ran}\mathsf H$，第二步用 $d,a$ 实及 $J_0^*=-J_0$。

**(PE2)** 因 $J_0\partial_\phi$ 自伴，
$$
2\operatorname{Re}\langle u_r,J_0u_\phi\rangle
=\partial_r\operatorname{Re}\langle u,J_0u_\phi\rangle .
$$
对整个真实径向区间积分，得到准确恒等
$$
\begin{aligned}
\|\mathcal L_{\mathsf H}u\|_2^2
={}&\|u_r-\mathsf H(d u_\phi)\|_2^2+\|a u_\phi\|_2^2\\
&-\int a_r\,\operatorname{Re}\langle u,J_0u_\phi\rangle\,dr .
\end{aligned}\tag{PE3}
$$
因此
$$
\|u_r-\mathsf H(d u_\phi)\|_2^2+\tfrac12\|a u_\phi\|_2^2
\le \|\mathcal L_{\mathsf H}u\|_2^2+\tfrac12L^2\|u\|_2^2. \tag{PE4}
$$
若
$$
E\ge\|\mathcal L_{\mathsf H}u\|_2+L\|u\|_2,
$$
则仍可使用原常数
$$
c_p=2/a_-,\qquad c_r=1+2d_+/a_-,\qquad
\|u_\phi\|_2\le c_pE,\quad \|u_r\|_2\le c_rE. \tag{PE5}
$$
径向恢复付 $\|\mathsf H(d u_\phi)\|_2\le d_+\|u_\phi\|_2$，没有删去 $d_+$。

以上先对光滑有限 Fourier 函数证明，再按原能量域闭包。径向 piece 边界必须是同一个连续状态及连续 $a$；若另有实际跳，则相应边界配对不能省略。本篇没有把两个独立单侧解自动匹配。

## 2. 完整投影方程和第一能量

**(PE3)** 保持原完整方程
$$
\mathcal Lz=\mathcal A(z)z+F,\qquad
\mathcal L=\partial_r-d\partial_\phi+aJ_0\partial_\phi.
$$
取 $\mathsf H=H_J$、$z_H=H_Jz$、$z_L=\Pi_Jz$。直接投影给
$$
\mathcal L_{H_J}z_H
=H_J\bigl(\mathcal A(z)z+F\bigr)+H_J(d\,\partial_\phi z_L). \tag{PE6}
$$
此式保持 $\mathcal A(z)$ 的全部 mean/rank-one 项。

令 $I=[c-2\ell,c+2\ell]$，$\chi=1$ 于内窗，$\chi=0$ 于两端，
$|\chi'|\le\ell^{-1}$。对 $u=\chi z_H$ 有额外真实源 $\chi'z_H$。
采用 LT 的完整 $A_0$ 及
$$
Z=\|z\|_{L^2(I)},\quad Z_L=\|\Pi_Jz\|_{L^2(I)},\quad
Z_H=\|H_Jz\|_{L^2(I)},\quad N_J=4J,
$$
可取
$$
\widehat E_J=
F_J+A_0Z+N_Jd_+Z_L+(L+\ell^{-1})Z_H,\qquad
F_J=\|H_JF\|_{L^2(I)}. \tag{PE7}
$$
于是 PE5 适用于 $\chi z_H$。

原 LT5 的展开仍正确；它在完整空间内处理高输入的低输出，额外支付了 $(N_Jd_++D_1)Z_H$。本篇在固定投影空间内保留该主部，PE2 已准确处理其 cross。非负系数条件下 $\widehat E_J\le E_J^{\rm LT}$，所以原 LT/NR 所有上界继续有效。

**(PE4)** 记
$$
\kappa_J=\sqrt{1+[4(J+1)]^{-2}},\qquad
p_c=\|P(c)^{-1}\|.
$$
同一完整高频集合上，原两端 FTC 与 Cauchy 给
$$
\|H_Jh(c)\|_{H^{1/2}}
\le p_c\sqrt{\kappa_Jc_pc_r}\,\widehat E_J
=:\widehat V_J . \tag{PE8}
$$
这里 $h=P^{-1}z$，$P$ 为径向，故与 Fourier 投影交换，$p_c$ 只付一次。两个端点 FTC 取平均后没有额外因子 2。

## 3. finite193、中间带和远高频

**(PE5)** 对 $J=96$，可保留完整 $Z$，也可用 $Z\le Z_L+Z_H$ 得
$$
\widehat E_{96}\le
F_{96}+(A_0+384d_+)Z_L+(A_0+L+\ell^{-1})Z_H. \tag{PE9}
$$
$\Pi_{96}$ 包含完整 even mean；并未把 mean 行设为零。

对 $J=288$，令 $Z_L=\|\Pi_{96}z\|$、$Z_M=\|(\Pi_{288}-\Pi_{96})z\|$、
$Z_F=\|H_{288}z\|$、$Z_H=(Z_M^2+Z_F^2)^{1/2}$。
复用 LT 的真实 finite reference $W_0$、$d_0$、$\mathcal A_*$：
$$
H_{288}\mathcal A_*\Pi_{96}=0,\qquad
H_{288}d_0\partial_\phi\Pi_{96}=0. \tag{PE10}
$$
这两个等号来自完整 degree-$96/192$ 支撑，含真实 rank/mean，不涉及未知高频截断。

若原已付差为
$$
\|\mathcal A(z)-\mathcal A_*\|\le a_\Delta,\qquad
\|d-d_0\|_\infty\le d_\Delta,
$$
则 PE6 直接给
$$
\widehat E_{288}=
F_{288}+A_*Z_H+a_\Delta Z+
384d_\Delta Z_L+1152d_+Z_M+(L+\ell^{-1})Z_F. \tag{PE11}
$$
特别地，
$$
\widehat E_{288}\le F_{288}+
(a_\Delta+384d_\Delta)Z_L+
\left[A_*+a_\Delta+
\sqrt{(1152d_+)^2+(L+\ell^{-1})^2}\right]Z_H . \tag{PE12}
$$
middle 到 far 的 $1152d_+$ 耦合仍保留；只处理 far 自身主部中已有的低输出。所有 source 支撑及 raw mean 更正均继续用 MC/MA/NR 原身份，不能把近似态的未知 $H_{288}Pf$ 设为零。

**(PE6)** 对已满足同一 MA 五例真解假设的状态，将 LT20 中 $V_J$ 换成 PE8 的 $\widehat V_J$ 即得
$$
\|h(c)\|_{H^1}^2
\le \Lambda_{96}^2c_L^2+
\Lambda_{288}\widehat V_{96}^2+
2^{48}\widehat V_{288}^{32768/16385}. \tag{PE13}
$$
$2^{24}$ 高阶插值仅作用于 $H_{288}$；中间带依旧单独读出。实际未知 finite cut 和左右 body 范数仍是输入。

## 4. 含普通角导残差的第二能量

**(PE7)** 要作 LT22–23 的直接 $H^1$ 读出，必须先使用完整微分方程
$$
\mathcal Lp=\mathcal A_1p+\mathcal B_{10}z+F_\phi,\qquad p=z_\phi .
$$
其中真实 $d_\phi p$ 已在 $\mathcal A_1$ 内，完整上界为原 $A_1,B_{10}$。本篇没有删除这一项。再用 PE6 处理 $p_H$，低频两项分别付
$A_1N_JZ_L$ 和 $N_J^2d_+Z_L$。

采用原第二 cutoff，导数上界 $2/\ell$、支撑位于第一 cutoff 等于 1 的内窗，可取
$$
\widehat E_J^{(1)}=
F_J^{(1)}+B_{10}Z+
(A_1N_J+N_J^2d_+)Z_L+
(A_1+L+2/\ell)c_p\widehat E_J,\qquad
F_J^{(1)}=\|H_JF_\phi\|_2. \tag{PE14}
$$
随后完整角高投影迹满足
$$
\|H_Jh(c)\|_{H^1}
\le p_c\kappa_J\sqrt{c_pc_r\widehat E_J\widehat E_J^{(1)}}. \tag{PE15}
$$
这是同一解的两次能量和中心径向 trace；不预设未知高角导。若用差商闭包，仍保原完整 shifted Leibniz、ordinary residual 各阶及 mean 项。

## 5. 数值范围和未付项

**(PE8)** 本篇没有更改 NR 43720373326 的科学源、成功回执或五组数值。现有 NR 仍是合法上界。若后继只需更尖系数，可从已存完整 $A_0,A_*,a_\Delta,d_+,d_\Delta,L,c_p,c_r,p_c$ 按 PE9、PE12 正向重组；不得以两个独立上界相减来制造更尖的数值界。

$H_{96}$、$H_{288}$ 是物理 Fourier 投影；物理曲率 shape 中 $j_\delta$、两条真实 mean、测度变换及右帽匹配仍按 W/LT 单独处理。对近似态，actual mean-speed 中的 $f_2/m$ 和全部 $H_JPf,H_JPf_\phi$ 必须另付。只有同一真解、同一实际高阶域时才使用 PE13；否则 PE15 也必须带该态完整系数和 residual。

本篇提供投影主部的精确能量和相应更尖条件界，不证明 core 存在、GH 闭合、实际未知范数或低曲率门已过。
