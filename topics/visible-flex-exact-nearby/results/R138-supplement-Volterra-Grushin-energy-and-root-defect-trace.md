# R138 补篇：Volterra–Grushin 体能量与真根缺陷迹

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

**已证明：**对同一个 Qrepair 的真实齐次 Jacobi 方向，有限旋转能量先直接控制完整角缺陷的 $L^2$ 体范数，再经准确 moving drift 给旋转场 $L^2_rH^{2/3}$ 与根迹 $H^{1/3}$。由此，根缺陷还在 $H^{-1/3}$ 中有准确极限。R138 体残差吸收中的未知 $L^2H^{1/2}$ 范数被消去，只剩两个原能量和明确的已知系数预算。

新的关键是反向 Volterra 核在根附近的平方质量含 $(r-r_*)/K(r)$，不会产生不可积的 $1/K$。下文直接支付全区间 $K(r)\ge(r-r_*)/120$ 和 Grushin 常数 $209,78$。没有运行新科学数值，也没有把尚未评估的 residual 乘子预算写成已过门。

本篇先对光滑方向证明，再在显示的有限能量范数中闭合。原弱齐次核的能量辨认在第 9 节单独接入同一个完整高图；不能只凭外端较强迹获得体能量。WVC hybrid 的额外主部差仍按 R138 (J.33)--(J.34) 单独保留。

## 1. 同一对象与准确能量

采用[残差输运补篇](R138-supplement-exact-residual-transport-and-fixed-interior-point.md)的同一外锚、$p=\tfrac12e_z$、$G=F-p$、完整 $\epsilon$、辅助旋转 $\omega$ 和缺陷
$$
W=\omega_\theta-H=a(-cX+bY),\qquad
H_r+\partial_\theta(\epsilon H)=\mathcal T_R W.
\tag{V.1}
$$
$\mathcal T_R$ 是 (T.14)--(T.16) 明列的零阶线性算子，包含完整 mean、角 primitive、同一逆角与实际 $Z$；不是待求 BVP 的逆。

设 $L=R-r_*$、$x=r-r_*$、$\sigma=G\cdot n>2/5$，
$$
\kappa=Kv^2,\qquad
M=1+u^2+\kappa,\qquad
\delta=b-uc,\qquad
Q=\delta^2+\kappa c^2.
$$
定义物理全圈的两个非负量
$$
\mathcal E=\int_{r_*}^R\int_0^{2\pi}ea\sigma Q\,d\theta\,dr,\qquad
\mathcal B=-\widetilde{\mathcal B}_R\ge0.
\tag{V.2}
$$
最后一个符号及同外端完整 DN/mean 图来自[外端补篇](R138-supplement-actual-outer-rotation-energy-and-mean-defect.md)和 (T.2)--(T.5)。准确已有
$$
\|\omega_R\|_{L^2_\theta}\le10\sqrt{\mathcal B},
\qquad
\|H_R\|_{L^2_\theta}\le\frac{\sqrt{\mathcal B}}{20000}.
\tag{V.3}
$$
全部圆周范数使用同一个非归一化 $d\theta$；Fourier Sobolev 权为 $\langle k\rangle^s$，环境向量不改成四分之一圆周。

## 2. 已付全正区的线性曲率下界

真根的既有区间包含于 $(.238,.239)$。原[完整正区曲率定理](R133-supplement-whole-positive-reference-floor-and-cached-producer.md)第 2 节实际给
$$
K'>46\quad\hbox{于 }[.238,.239],\qquad
K>.02679531>1/40\quad\hbox{于 }[.239,25/8].
$$
$K$ 在原全部 scalar 接口连续，且 $K(r_*)=0$。由于 $14/5<L<3$，准确有
$$
\boxed{\qquad K(r)\ge x/120
       \quad(r_*\le r\le R).\qquad}
\tag{V.4}
$$
在第一段用 $K\ge46x$；在第二段用 $x<3$。这里不取根区间端点为根，不需要候选曲率近似，也没有扩张参数范围。

## 3. 完整体缺陷直接由退化能量控制

对 $s\in\{0,-1/3\}$，取任一明确上界
$$
k_s(r)\ge\|\mathcal T_R(r)\|_{H^s_\theta\to H^s_\theta}.
$$
令
$$
\Lambda_\epsilon=\frac12\int_{r_*}^R
                 \|\epsilon_\theta(r)\|_{A^0_\theta}\,dr,
\qquad E_\epsilon=e^{\Lambda_\epsilon},
$$
$$
C_W(r)=\sup_\theta\frac{M}{\gamma\sigma v^2},
\qquad
J_0=\int_{r_*}^R\frac{x\,C_W(r)\,k_0(r)^2}{K(r)}\,dr.
\tag{V.5}
$$
根处的被积函数按连续上界解释。(V.4) 直接给
$J_0\le120\int C_Wk_0^2$，所以这不是新的根奇性条件。

从
$\kappa[(\delta+uc)^2+c^2]\le M(\delta^2+\kappa c^2)$，
得逐点
$$
K|W|^2\le\frac{a^2M}{v^2}Q.
\tag{V.6}
$$
因此 $K\|W(r)\|_2^2\le C_W(r)e_Q(r)$，其中
$e_Q(r)=\int ea\sigma Q\,d\theta$ 是完整径向能量密度。

保守输运 $\partial_rH+\partial_\theta(\epsilon H)=0$ 在 $L^2$ 的任意方向传播范数至多 $E_\epsilon$。准确的反向 Duhamel 估计于是给
$$
\|H(r)\|_2\le E_\epsilon\left[
 \|H_R\|_2+
 \int_r^R k_0(t)\sqrt{\frac{C_W(t)}{K(t)}}
                         \sqrt{e_Q(t)}\,dt\right].
\tag{V.7}
$$
标量核
$\mathbf1_{r<t}k_0(t)\sqrt{C_W(t)/K(t)}$
在 $(r,t)$ 上的平方积分恰为 $J_0$。对 Hilbert 值的源先取范数，再用标量 Hilbert–Schmidt 不等式，得到
$$
\boxed{\quad
\|H\|_{L^2_rL^2_\theta}
\le h_E\sqrt{\mathcal E}+h_B\sqrt{\mathcal B},
\quad
h_E=E_\epsilon\sqrt{J_0},\quad
h_B=\frac{E_\epsilon\sqrt L}{20000}.
\quad}
\tag{V.8}
$$
没有以 $\sup_r\|H(r)\|_2$ 代替这里的 $L^2_r$ 范数；根端该强 supremum 可能没有这一估计。真实源和全部 mean 留在 $\mathcal T_R$。

## 4. 精确 drift，两个平方能量与只需一阶的角图

令
$$
\vartheta=\Theta_\phi=v/m,\qquad
w(r,\phi)=\omega(r,\Theta(r,\phi)).
$$
原准确 lift 满足
$\Theta_r=d\vartheta-\gamma u+\epsilon$。
所以对
$D'=\partial_r+(\epsilon-\gamma u)\partial_\theta$
有
$$
D'\omega\circ\Theta=(\partial_r-d\partial_\phi)w.
\tag{V.9}
$$
不是固定 moving 角的 $\partial_r$。利用 (T.11) 与 (V.1)，准确得到
$$
D'\omega+\gamma uH
=e\{-\delta X+(u\delta-\kappa c)Y\}.
\tag{V.10}
$$
右侧平方不超过 $e^2M Q$。这和 (V.6) 是同一能量的两个不同受控方向。

设完整已知系数上界为
$$
C_E=\sup_{r,\theta}
 \left\{\frac{\gamma M}{\sigma\vartheta}
              +\frac{\vartheta M}{\gamma\sigma v^2}\right\},
\qquad
C_H=\sup_{r,\theta}
 \left\{\frac{\gamma^2u^2}{\vartheta}+K\vartheta\right\}.
\tag{V.11}
$$
把准确 Jacobian $d\phi=d\theta/\vartheta$ 留入积分，逐项平方给
$$
\|(\partial_r-d\partial_\phi)w\|_2^2+
             \|\sqrt K\,w_\phi\|_2^2
\le2C_E\mathcal E+2C_H\|H\|_{L^2_rL^2_\theta}^2.
\tag{V.12}
$$

取唯一全圈 drift flow
$$
\psi_r(r,\xi)=-d(r,\psi(r,\xi)),\qquad \psi(R,\xi)=\xi,
\quad v_*(r,\xi)=w(r,\psi(r,\xi)).
$$
记
$$
D_0=\int_{r_*}^R\|d_\phi(r)\|_\infty\,dr,\qquad
\Gamma=e^{D_0},\qquad
A_\Theta=\sup_{r,\phi}\max\{\vartheta,\vartheta^{-1}\}.
\tag{V.13}
$$
一阶变分方程给 $\Gamma^{-1}\le\psi_\xi\le\Gamma$。普通 $L^2$ 换元及 (V.4)、(V.12) 给
$$
\mathfrak G:=
\int\left(|(v_*)_r|^2+\frac{x}{120}|(v_*)_\xi|^2\right)
\le2\Gamma\{C_E\mathcal E+C_H\|H\|_2^2\}.
\tag{V.14}
$$

若一个圆周双射的导数及逆导数至多 $A$，则 composition 在 $L^2$ 和 $H^1$ 的范数都至多 $\sqrt A$：前者用逆 Jacobian，后者的导数项用正 Jacobian。由这两个 Hilbert 空间的准确插值得
$$
\|f\circ\chi\|_{H^s}\le\sqrt A\,\|f\|_{H^s},
\qquad0\le s\le1.
\tag{V.15}
$$
因此下面的 $H^{2/3}$ 和 $H^{1/3}$ 只需 $\psi_\xi$，不需再支付 drift flow 的二阶导数。真实 $\Theta$ 和同一 whole-circle flow 两次 composition 的总因子至多 $\sqrt{A_\Theta\Gamma}$。

## 5. 一个完整的显式 Grushin 不等式

设 $z:[0,L]\times\mathbb S^1\to\mathbb R^3$ 光滑，
$14/5<L<3$，定义
$$
\mathfrak G_z=\int\left(|z_x|^2+\frac{x}{120}|z_\xi|^2\right).
$$
则无须在根端加条件，
$$
\boxed{\quad
\|z\|_{L^2_xH^{2/3}_\xi}^2
\le209\,\mathfrak G_z+78\,\|z(L)\|_2^2,
\quad}
\tag{V.16}
$$
$$
\boxed{\quad
\|z(0)\|_{H^{1/3}_\xi}^2
\le419\,\mathfrak G_z+156\,\|z(L)\|_2^2.
\quad}
\tag{V.17}
$$

**证明。** 对单个非零整数频率 $k$，置
$c=1/120$、$h=(ck^2)^{-1/3}$。若 $2h\le L$，对
$x\in[0,h]$、$y\in[h,2h]$ 用
$$
|z_k(x)|^2\le2|z_k(y)|^2+
                         4h\int_0^{2h}|z_k'|^2.
$$
先平均 $y$ 再积分 $x$，而 $[h,L]$ 上
$ck^2x\ge h^{-2}$，得
$$
h^{-2}\int_0^L|z_k|^2
\le4\int_0^L|z_k'|^2+
                  3ck^2\int_0^Lx|z_k|^2.
$$
若 $2h>L$，则
$|k|^{4/3}<4c^{-2/3}/L^2$。包含零模并求和，使用
$\langle k\rangle^{4/3}\le1+|k|^{4/3}$，得到
$$
\|z\|_{L^2H^{2/3}}^2
\le C_0\mathfrak G_z+
           (1+C_0/L^2)\|z\|_2^2,\qquad
C_0=4c^{-2/3}<100.
$$
从真实外端逐径向积分，
$$
\|z\|_2^2\le2L\|z(L)\|_2^2+L^2\|z_x\|_2^2.
$$
所以系数分别为 $L^2+2C_0<209$ 与
$2L+2C_0/L<78$，证明 (V.16)。

对任一 Fourier 分量，普通一维迹式
$|f(0)|^2\le2\|f\|_2^2/L+2\|f\|_2\|f'\|_2$
乘以 $\langle k\rangle^{2/3}$ 后用 $2ab\le a^2+b^2$，给
$$
\|z(0)\|_{H^{1/3}}^2
\le\|z_x\|_2^2+(1+2/L)\|z\|_{L^2H^{2/3}}^2.
$$
$1+2/L<2$，代入 (V.16) 即得 (V.17)。证明同时覆盖零模；没有把环境向量的均值删掉。证毕。

## 6. 把所有未知体 Sobolev 范数消成两个原能量

由于 $\psi(R)=\mathrm{id}$，
$$
\|v_*(R)\|_2^2\le A_\Theta\|\omega_R\|_2^2
\le100A_\Theta\mathcal B.
$$
结合 (V.8)、(V.14)--(V.17)，定义
$$
\begin{split}
w_E&=\Gamma\sqrt{418A_\Theta}
                   (\sqrt{C_E}+\sqrt{C_H}h_E),\\
w_B&=\Gamma\sqrt{418A_\Theta C_H}\,h_B
                      +10A_\Theta\sqrt{78\Gamma},\\
z_E&=\Gamma\sqrt{838A_\Theta}
                   (\sqrt{C_E}+\sqrt{C_H}h_E),\\
z_B&=\Gamma\sqrt{838A_\Theta C_H}\,h_B
                      +10A_\Theta\sqrt{156\Gamma}.
\end{split}
\tag{V.18}
$$
于是
$$
\boxed{\quad
\|\omega\|_{L^2_rH^{2/3}_\theta}
\le w_E\sqrt{\mathcal E}+w_B\sqrt{\mathcal B},\qquad
\|\omega(r_*)\|_{H^{1/3}_\theta}
\le z_E\sqrt{\mathcal E}+z_B\sqrt{\mathcal B}.
\quad}
\tag{V.19}
$$
这也控制 (T.22) 的 $L^2H^{1/2}$。右侧只有指定中心的系数、residual 乘子、真角图、同一个完整外端图和两项原能量；没有待求 inverse norm。

## 7. 真根的完整缺陷迹在自然负阶窗口中存在

保守输运在每个 $H^{-\tau}$、$0\le\tau\le1/2$ 的传播因子仍可取 $E_\epsilon$。说明其精确频率界即可：
令 $\lambda_k=\langle k\rangle$，对所有整数 $k,l$，
$$
\left|k(\lambda_l/\lambda_k)^\tau
       -l(\lambda_k/\lambda_l)^\tau\right|\le|k-l|.
\tag{V.20}
$$
当 $k,l$ 同号，可令 $k\ge l\ge0$，左侧有符号表达随 $\tau$ 单调下降且非负。当二者异号，它是 $\tau$ 的凸函数，最大值在 $0$ 或 $1/2$；后一个端点正是 (T.19) 已证的平方不等式。零模直接包含。对称部的 Schur 行列和于是均至多 $\tfrac12\|\epsilon_\theta\|_{A^0}$。

记 $K_-=\|k_{-1/3}\|_{L^2_r}$。由 (V.1)、(V.19) 及
$\|\omega_\theta\|_{H^{-1/3}}\le\|\omega\|_{H^{2/3}}$，完整源在 $L^1_rH^{-1/3}$ 可积。因此 $H(r)$ 在 $r\downarrow r_*$ 有该空间的准确极限，且
$$
\boxed{\quad
\|H(r_*)\|_{H^{-1/3}}
\le r_E\sqrt{\mathcal E}+r_B\sqrt{\mathcal B},
\quad}
\tag{V.21}
$$
$$
r_E=E_\epsilon K_-(w_E+h_E),\qquad
r_B=E_\epsilon\{1/20000+K_-(w_B+h_B)\}.
\tag{V.22}
$$
这里完整 mean 是 $k=0$，没有丢掉。根型 (U.12)--(U.14) 使用的是
$\mathsf H=\vartheta H$ 和 moving pullback；其准确 multiplication/composition 因子须再保留，不能把 (V.21) 自动称为 moving 范数。

## 8. 明确的二变量吸收入口

设 (T.22) 中两个已知系数预算为 $E_0,E_1$。其证明及 (V.8)、(V.19) 直接给
$$
|\mathcal R_{\rm err}|
\le a_{EE}\mathcal E+
a_{EB}\sqrt{\mathcal E\mathcal B}+a_{BB}\mathcal B,
\tag{V.23}
$$
其中
$$
\begin{split}
a_{EE}&=E_0w_E^2+E_1w_Eh_E,\\
a_{EB}&=2E_0w_Ew_B+E_1(w_Eh_B+w_Bh_E),\\
a_{BB}&=E_0w_B^2+E_1w_Bh_B.
\end{split}
\tag{V.24}
$$
若根全角消费者最终证明
$\widetilde{\mathcal B}_L\ge-C_*\|H(r_*)\|_{H^{-1/3}}^2$
（$C_*$ 必须包含完整 (U.12)--(U.14)、原 mean 消元和角图费用），则令
$$
A=a_{EE}+C_*r_E^2,\quad
C=a_{BB}+C_*r_B^2,\quad
T=a_{EB}+2C_*r_Er_B.
$$
准确能量恒等式变成
$$
(2-A)\mathcal E+(1-C)\mathcal B
\le T\sqrt{\mathcal E\mathcal B}.
\tag{V.25}
$$
因此三个明确 scalar 比较
$$
A<2,\qquad C<1,\qquad
T^2<4(2-A)(1-C)
\tag{V.26}
$$
足以排除这一能量类中的真实齐次核。严格二元二次型证明 (V.26) 的结论；再由 $\mathcal E=\mathcal B=0$、(V.8) 及 (V.19) 得 $Q=H=\omega=0$。$K>0$ 于开正区，故原 $(b,c)=0$；完整 $D\Psi$ 可逆，原方向也为零。

这不是声称 (V.26) 已过门。与原未闭形式估计不同，(V.23)--(V.26) 不再包含任意未知方向范数或未知 inverse。剩余新消费者是指定中心的完整系数/残差预算和同实际 frame 的根全角型；它们保持各自真实范围。

## 9. 同一个原弱齐次核已有有限体能量

固定外端补篇第 8 节的同一个 prescribed high-stable 根输入为零的真 $Q_\delta$ 齐次核。有限 head 为 $h_L\in L^2_rE_{193}$，独立普通、外端与 affine 源为零；完整 head-to-high 作用与有限 low/mean 外端输入没有置零。这里为本篇已付 support 取 $\delta=0$，即同一 Qrepair。

该节已经用同一 base-order 七列高图构造强解，再以原 negative-one 高图的唯一性辨认原弱解。除了外端迹，这份同一 [P.14--P.15 合同](R133-supplement-full-real-delta-positive-high-root-to-regular-graph.md)实际给出
$$
h_H\in L^2([r_*,R]\times\mathbb S^1_\phi).
\tag{V.27}
$$
这是[实际 run 43617150971 的全七列结论](R133-supplement-actual-full-real-delta-positive-high-root-to-regular-graph.md)第 3 节的整段原态 $L^2$ 输出，采用真实 collar 长度与 body 重构因子。它不是从 $Z$ 的某个端值倒推体范数。有限 head 所产生的 high 源只到原 shell288，故确属于该 base-order 普通 $L^2_rH^{1/3}_\phi$ 接口；不要求径向光滑。

完整 physical/moving 微分的 [C.11](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md) 为
$$
(b,c)=P_Q(h\circ\Phi)
 -(B,C)_\theta I_\theta[C(h_2\circ\Phi)],
\qquad
P_Q=\begin{pmatrix}C&-BC\\0&-C^2\end{pmatrix}.
\tag{V.28}
$$
这里 $I_\theta$ 明确去掉零模，而原 even mean 留在 $P_Q$ 和完整角变化。背景 $v,m$ 的真实 gap、所有角系数及角图 Jacobian 在本紧区间有界；primitive 在这个四重标量类上的 $L^2$ 范数是 $1/4$。因此 (V.28) 是有界 $L^2$ 映射，给 $(b,c)\in L^2$，从而 $\mathcal E<\infty$。

还可直接说明积分身份的合法性。此时 $W\in L^2$，(V.1) 的已知零阶源在 $L^1_rL^2_\theta$，所以 $H\in L^\infty_rL^2_\theta$。原外迹 (O.22) 给 $\omega_R$ 的足够角正则性；解 (T.11) 后，分布意义的 $\omega_\theta=W+H$ 及 $\omega_r=U-\epsilon\omega_\theta$ 都在 $L^2$。故可先在原各光滑片上平滑、再以这些强 $L^2$ 关系通过极限，得到本文所用的能量与迹身份。后续 (V.8)--(V.26) 不使用这个原 $L^2$ 重构常数来控制 $\mathcal E$，所以没有循环调用待证有限 Schur。

任意粗自由 high-stable 输入若不属于 base-order 强窗，上述辨认不自动成立。对 hybrid 必须另付 (J.33)--(J.34)，不能由本篇授予其有限能量核排除。

对有真实接口原子的版本，(V.1) 的 Duhamel 公式须逐个保留对应跳项；本篇使用连续 Qrepair 和齐次原 transmission，所以不引入人为状态跳。原分片系数和一侧导数继续按其真实区间消费，不能用本篇的积分符号抹去原接口定义。
