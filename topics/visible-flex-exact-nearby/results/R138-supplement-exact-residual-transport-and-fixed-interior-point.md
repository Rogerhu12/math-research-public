# R138 补篇：残差的准确输运主部、零平均旋转场与固定内点

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

**已证明的解析推进。** 同一 Qrepair 物理 frame 可使用固定环境点
$p=\tfrac12e_z$，其整个正区支撑严格大于 $2/5$；真实外端负型保持，
对应初值常数改为 $10$ 与 $1/20000$。
moving-to-physical Hessian 残差中唯一的方向角导恰是一项共同输运。
将它放入辅助旋转场的输运方程后，角缺陷满足一个没有方向角导源的准确守恒输运式。
完整修正能量误差只剩 order-one 的旋转场配对，并有下面不调用未知 PDE 逆的定量 Sobolev 估计。

本文不宣告内端正型或最终吸收门已经通过；不把 WVC hybrid
$\mathscr A_c$ 和真正 $DF(Q_c)$ 认作同一算子。

## 1. 已付的同一固定内点和新外端常数

取
$$
p=\tfrac12e_z,\qquad G=F-p,\qquad s=G\cdot n.
\tag{T.1}
$$
[同物理角 Qrepair 支撑证书](R138-supplement-actual-positive-support-for-repaired-physical-frame.md)
给 $F\cdot n>9/10$、$|F|<319/250$、$|n|=1$，直接推出
$$
\boxed{\qquad s>2/5,\qquad |G|<222/125.\qquad}
\tag{T.2}
$$
这是一次全域固定平移，不在不同端点选择不同的 $p$，也没有重新积分模型。

在外端圆锚把
[实际外端能量](R138-supplement-actual-outer-rotation-energy-and-mean-defect.md)
的 $h$ 换成
$$
\widehat h=
4347844570122155/4503599627370496-1/2>0.
$$
仍有 $t<0$、$z>0$、$t^2+z^2=1$，
$s_R=az-\widehat h t>2/5$。
因此 (O.13)--(O.16) 的每项符号和比值估计保持成立：
$$
\mathcal B_R\le-2\pi a_R^2s_R\mathcal N^2,
\qquad
\widetilde{\mathcal B}_R\le-2\pi a_R^2s_R\mathcal N^2,
\quad
\mathcal N=\|c_\perp\|_{H^{-1/2}_\theta}.
\tag{T.3}
$$
这里 $\widetilde{\mathcal B}=\mathcal B-2\int G\cdot(\omega\times H)$，
均值系数仍准确为
$2\pi a^2(\widehat h t^2-2azt)c_0^2$，并由 $2s_R$ 控制。

初始周期旋转、角缺陷不随 $p$ 改变：
$$
\omega_R=I_{2\pi}[a(-cX+bY)],\qquad H_R=azc_0e_z.
$$
将 $s_R>2/5$ 代入原逐项估计，得到
$$
\boxed{\quad
\|\omega_R\|_2<10\sqrt{-\widetilde{\mathcal B}_R},\qquad
\|H_R\|_2<\frac1{20000}\sqrt{-\widetilde{\mathcal B}_R}.
\quad}
\tag{T.4}
$$
事实上 $6/\sqrt{2/5}<10$ 且
$1/(32000\sqrt{2/5})<1/20000$。
这些使用真实 $2\pi$ 非归一化积分；零方向时按非严格不等式解释。
原 $p=0$ 的 $7$、$1/30000$ 没有沿用。

## 2. 完整坐标 Hessian 的唯一一阶项

只在本节用 $Q=(u,v)$ 表示 moving 场、$m=\langle v\rangle$，
$$
\Theta(\phi)=\phi+I_\phi(v/m-1),\qquad
\Theta_\phi=v/m>0,\qquad
Y=(B,C)=\bigl(u/v,1/v\bigr)\circ\Theta^{-1}=:\Psi(Q).
\tag{T.5}
$$
$I_\phi$ 是完整均值零 primitive。字母 $Y$ 在本节的 (T.5)--(T.11)
只指曲率对；第 3 节起恢复 frame 的 $Y$ 列。

令 $R=(R_u,R_v)=Q_r-F(Q)$，$R_m=\langle R_v\rangle$，
$h=(h_1,h_2)$、$\mu=\langle h_2\rangle$。定义
$$
\zeta_R=\frac1m I_\phi(R_v-vR_m/m),\quad
\zeta_h=\frac1m I_\phi(h_2-v\mu/m),
$$
$$
\epsilon=\zeta_R\circ\Theta^{-1},\qquad
\xi=\zeta_h\circ\Theta^{-1},\qquad
x=(b,c)=D\Psi_Qh.
\tag{T.6}
$$
同一 $\epsilon$ 就是 support 补篇 (S.11) 的
$\Theta_r-\tau$，不是另选的输运速度。
置 $\mathcal F(u,v)=(u/v,1/v)$，所有右侧 moving 量随后按
$\Theta^{-1}$ 拉回。准确地，
$$
\boxed{\quad
D^2\Psi_Q[R,h]=-\epsilon\,x_\theta+f_0,
\quad}
\tag{T.7}
$$
其中
$$
\boxed{\quad
f_0=D^2\mathcal F_Q[R,h]\circ\Theta^{-1}
 -\xi\,\partial_\theta
       \{D\mathcal F_QR\circ\Theta^{-1}\}
 +\left\{\xi(R_v/v)\circ\Theta^{-1}
                 +\frac\mu m\epsilon\right\}Y_\theta .
\quad}
\tag{T.8}
$$
这里完整的点乘 Hessian 是
$$
D^2\mathcal F_Q[R,h]=
\begin{pmatrix}
 -(R_uh_2+R_vh_1)/v^2+2uR_vh_2/v^3\\
 2R_vh_2/v^3
\end{pmatrix}.
\tag{T.9}
$$
(T.8) 中没有 $h_\phi$ 或 $x_\theta$；残差最多取一次角导。
完整 mean 和 primitive 没有删除。

**证明。** 写 $y_0=D\mathcal F_QR\circ\Theta^{-1}$。
已知 $D\Psi_Qh=D\mathcal F_Qh\circ\Theta^{-1}-\xi Y_\theta$。
在固定 moving $h$ 下沿 $R$ 微分。
真正角图二阶项满足
$$
D\zeta_h[R]=-(R_m/m)\zeta_h-(\mu/m)\zeta_R,
\qquad
\epsilon_\theta=(R_v/v)\circ\Theta^{-1}-R_m/m.
\tag{T.10}
$$
逆角微分贡献 $-\epsilon\partial_\theta$。
展开 $D\Psi_QR=y_0-\epsilon Y_\theta$ 后，
$\epsilon\xi Y_{\theta\theta}$ 与
$\epsilon\xi_\theta Y_\theta$ 两组项准确抵消，余项恰为
(T.7)--(T.8)。这也显示第一项是共同标量输运，不能与
J.33 的 off-diagonal hybrid 主部差混淆。

对原 genuinely homogeneous moving Jacobi 方向
$\mathcal D_{\rm mov}h=0$，R138 (J.32) 于是给
$$
D\mathcal R_{\rm phys}[x]=-\epsilon x_\theta+f_0.
\tag{T.11}
$$
独立 moving 普通源 $g$ 在 (T.8) 另加 $D\Psi_Qg$。
若 $g$ 本身含 WVC 的 $h_\phi$，本文未将它变成 zeroth order。

## 3. 消除方向角导的周期旋转输运

以下恢复 $O=(X,Y,n)$、$G=F-p$ 的 frame 记号。
固定已构造的同一物理 base，令
$$
V=\partial_r+\epsilon\partial_\theta,\qquad
V\omega=e(-bX+\alpha Y)=:U,
\quad \alpha=(2Bb-Ac)/C,
\tag{T.12}
$$
并使用第 1 节同一个外端周期初值。
这是辅助旋转提升的线性输运定义；当 $\epsilon\ne0$ 时，
不把它冒认为原固定物理径向 ODE 的 $\delta O=\omega\times O$。
它仍保留同一真实曲率方向 $x$、同一 base frame 和全部边界条件。

置
$$
W=a(-cX+bY),\qquad H=\omega_\theta-W.
$$
按与 (E.6) 相同的逐项计算，(T.11) 给
$$
\boxed{\quad
H_r+\partial_\theta(\epsilon H)=\mathcal S,
\quad}
\tag{T.13}
$$
$$
\boxed{\begin{split}
\mathcal S={}&a(f_{0,C}X-f_{0,B}Y)
 +e(-bZ_X+\alpha Z_Y)\\
 &-a\epsilon(-cX_\theta+bY_\theta)-\epsilon_\theta W.
\end{split}}
\tag{T.14}
$$
其中 $Z=O_\theta-O\Omega_\theta$ 是原 base 角缺陷。
直接核对的方法是先在 (E.6) 右侧加入
$-\partial_\theta(\epsilon\omega_\theta)$，再使用
$f=-\epsilon x_\theta+f_0$；两个
$\epsilon\omega_{\theta\theta}$ 恰好相消。
所以 (T.14) 对曲率方向是完整的 order-zero 算子，
没有方向角导和没有方向径向导。

由 $W=\omega_\theta-H$，有明确恢复
$$
b=\frac{W\cdot Y}{a},\qquad
c=-\frac{W\cdot X}{a},\qquad
\alpha=2u b-(A/C)c,
\quad h=\mathfrak M_Q(b,c).
\tag{T.15}
$$
原 $\mathfrak M_Q$ 的完整 inverse angle/mean 定义是 R138 (J.26)。
因此 (T.8)--(T.15) 定义一个明确零阶算子
$\mathcal T_R$，满足
$$
\mathcal S=\mathcal T_R(\omega_\theta-H)
\tag{T.16}
$$
（若有独立源，则另保其加项）。
它的所有系数来自已指定中心的 $R,R_\theta,Z$、角图和 frame，
不含待求 PDE 逆。

在本题四重加反射类中还有准确结论
$$
\boxed{\qquad \langle\omega(r,\cdot)\rangle_{2\pi}=0
\quad\hbox{对每个 }r.\qquad}
\tag{T.17}
$$
证明用 $\mathsf S=\operatorname{diag}(1,-1,1)$：
$X,n$ 在 $-\theta$ 处为 $\mathsf S$ 倍，$Y$ 为
$-\mathsf S$ 倍；$b,\epsilon$ 为 odd，$\alpha$ 为 even。
(T.12) 及其初值因而保持 $\omega(-\theta)=-\mathsf S\omega(\theta)$。
竖直分量是 odd，平均为零；水平平均由四重旋转等变为零。
这不要求把每个径向圆的刚体规范重新设一次。

## 4. 只有 order-one 配对的完整修正能量

取 $\lambda=G\cdot(\omega\times d\omega)$，
$\mathcal B=\int\lambda(\partial_\theta)$，
$\mathcal M=\int G\cdot(\omega\times H)$，
$\widetilde{\mathcal B}=\mathcal B-2\mathcal M$。
Gauss 方向平方仍准确为
$$
Q=(b-uc)^2+(K/C^2)c^2,\qquad
\mathscr Q=\int_L^R\int_0^{2\pi}ea\,s\,Q\,d\theta\,dr.
$$
将 $\omega_r=U-\epsilon\omega_\theta$ 代入普通外微分，再用
(T.13) 做守恒输运分部积分，得到
$$
\boxed{\begin{split}
2\mathscr Q={}&\widetilde{\mathcal B}_R
                 -\widetilde{\mathcal B}_L+\mathfrak R,\\
\mathfrak R={}&\int\!\!\int
 \bigl[(eX+2\epsilon F_\theta)\cdot(\omega\times H)
       +P\cdot(\omega\times U)\\
 &\hspace{25mm}+2G\cdot(\omega\times\mathcal S)
       -\epsilon F_\theta\cdot(\omega\times\omega_\theta)\bigr].
\end{split}}
\tag{T.18}
$$
$P=F_\theta-aY$ 仍是实际 base 位置缺陷。
特别，不能把 $F_\theta$ 在带 $\epsilon$ 的两项中悄悄换成 $aY$。
若 $R=Z=P=0$ 且 $H_R=0$，则 $\epsilon=\mathcal T_R=H=0$，
全部误差准确消失。

核对 (T.18) 时，未修改的外微分先多出
$+\epsilon F_\theta\cdot(\omega\times\omega_\theta)$。
而
$\int V\{G\cdot(\omega\times H)\}
=\mathcal M_R-\mathcal M_L-\int\!\!\int\epsilon_\theta
G\cdot(\omega\times H)$。
(T.13) 中相同的 $\epsilon_\theta H$ 正好抵消这一项，
留下 (T.18) 的四项和所示负号。

## 5. 一个不调用未知逆的实际域估计

本节的 Sobolev 范数在真实 $2\pi$ 圆上；归一化与否只要全篇一致。
令
$$
k(r)=\|\mathcal T_R(r)\|_{H^{-1/2}\to H^{-1/2}},\quad
q(r)=\tfrac12\|\epsilon_\theta(r)\|_{A^0},\quad
\Lambda=\int_L^R(q+k),\quad k_2=\|k\|_{L^2_r}.
\tag{T.19}
$$
这些可由 (T.8)--(T.16) 和原角图的乘积/primitive 上界直接构造；
完整 mean 是该算子的一部分。置
$\mathcal W=\|\omega\|_{L^2_rH^{1/2}_\theta}$、$\ell=R-L$。
(T.13) 给不循环的估计
$$
\boxed{\quad
\|H\|_{L^2_rH^{-1/2}}
\le\sqrt\ell\,e^\Lambda
       \{\|H_R\|_{H^{-1/2}}+k_2\mathcal W\}.
\quad}
\tag{T.20}
$$

这里守恒输运在 $H^{-1/2}$ 的增长率确可取 $q$。
在 Fourier 加权后，其对称矩阵项的绝对值至多
$$
\tfrac12|k-l|\,|\epsilon_{k-l}|,
$$
因为
$$
\frac{|l\langle k\rangle-k\langle l\rangle|}
 {\sqrt{\langle k\rangle\langle l\rangle}}
\le |k-l|.
$$
最后不等式平方后可由
$\langle k\rangle\langle l\rangle\ge1+|kl|$
与 $k^2+l^2\ge2|kl|$ 验证。
Schur 求和给所述 $q$；再由 (T.16) 和
$\|\omega_\theta\|_{H^{-1/2}}\le\|\omega\|_{H^{1/2}}$
应用一次 Grönwall 即得 (T.20)。

为完整记录能量费用，写
$$
U=\mathcal L(\omega_\theta-H),\qquad
\mathcal L=\gamma\{-X\otimes Y
       +Y\otimes[2uY+(A/C)X]\}.
\tag{T.21}
$$
令 $M_v$ 表示相应向量叉乘乘子，取任意真实上界
$$
\begin{split}
a_1(r)&\ge\|M_{eX+2\epsilon F_\theta}\|_{H^{-1/2}\to H^{-1/2}},\\
p_1(r)&\ge\|M_P\mathcal L\|_{H^{-1/2}\to H^{-1/2}},\\
r_1(r)&\ge2\|M_G\mathcal T_R\|_{H^{-1/2}\to H^{-1/2}},\\
e_1(r)&\ge\|M_{\epsilon F_\theta}\|_{H^{-1/2}\to H^{-1/2}}.
\end{split}
$$
例如完整矩阵 Fourier 和
$\sum_j(1+|j|)^{1/2}\|A_j\|$ 是合法乘子上界，
由 $\langle k+j\rangle/\langle k\rangle\le1+|j|$ 直接证明。
不用假定这些乘子与 Hilbert 算子或 primitive 对易。

令
$E_0=\sup(p_1+r_1+e_1)$、
$E_1=\sup(a_1+p_1+r_1)$。
逐项 Sobolev 对偶与 (T.20) 给
$$
\boxed{\begin{split}
|\mathfrak R|\le{}&
\{E_0+E_1\sqrt\ell\,e^\Lambda k_2\}\mathcal W^2\\
&+E_1\sqrt\ell\,e^\Lambda
       \|H_R\|_{H^{-1/2}}\mathcal W.
\end{split}}
\tag{T.22}
$$
(T.4) 已明确支付最后一行的初值。
本式把原来的未加权 $c$ 费用换成旋转场半阶能量；
它本身不声称所有系数已小到通过最终吸收。
将 $\mathcal W$ 与正区 turning 能量比较及内端真型的严格下界，
是接下来可以单独验算的数学步骤，不能用未知 full inverse 回填。

原 Qrepair/齐次方向连续时 (T.13)、(T.18) 没有人工 seam 原子；
若真实独立 affine jump 非零，则保留其 $H$ 跳与两侧
$\widetilde{\mathcal B}$ 有向差，不能改为普通 $dr$ 项。
