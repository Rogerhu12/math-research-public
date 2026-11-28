# 已证明：全圆真实标签误差的三角传播与无根奇幂的作用量矩

使用 [CRW](R149-supplement-correlated-ray-wave-forcing-and-signed-cut-seed.md) 的同一两方向、真实角和截面。下列等式作用于全部真实解。有限谱试函数仅出现在可估残差里，$e^{inP_\sigma}$ 始终保留真相位。

## 全圆输运的有限阶误差

在一个原单侧片上以向内距离 $t$ 作时间，记 $L=\partial_t+d\partial_\phi$，$L_\sigma=L+\sigma b\partial_\phi$，$b=\eta\sqrt{-K}$ 是径向标量。令 $P_\sigma=\phi+u_\sigma$。对任一实、周期、有限谱分片时间多项式 $q_\sigma$，置
$$
 f_\sigma=-[\partial_t q_\sigma+(d+\sigma b)(1+\partial_\phi q_\sigma)],\qquad
 e_\sigma=u_\sigma-q_\sigma .
$$
则 $L_\sigma e_\sigma=f_\sigma$。对 $m\ge0$ 记 $e_m=\partial_\phi^m e/m!$、$f_m,d_m$ 同理。沿真实特征，
$$ L_\sigma e_m=f_m-md_\phi e_m-\sum_{j=1}^{m-1}j d_{m-j+1}e_j .$$
这是归一化 Leibniz 展开，$d+\sigma b$ 的正阶角导与 $d$ 相同，$m=0$ 也保留。取全格上界 $S\ge\max(0,\sup(-d_\phi))$，$F_m\ge\sup|f_m|$，$D_k\ge\sup|d_k|$，下严格三角矩阵 $N_{mj}=j D_{m-j+1}$（$1\le j<m$，其余零）。若 $y_m$ 是入端 $\|e_m\|_\infty$ 上界，则步长为 $h$ 的全步及出端同获上界
$$
 \boxed{\quad
 Y_m=e^{mSh}\left[\sum_{k=0}^m\frac{h^k}{k!}(N^ky)_m
       +\sum_{k=0}^m\frac{h^{k+1}}{(k+1)!}(N^kF)_m\right].\quad}
$$
证明是沿每条特征取绝对值，乘 $e^{-mSt}$，低阶的权 $e^{-(m-j)St}\le1$，积分迭代有限终止。$Y_m$ 非负且关于 $h$ 单调。非零试函数接缝必须把实际角导跳跃 $q^- -q^+$ 加进误差，其中 $+,-$ 按向内方向；真实标签连续。试函数可显式选择连续，端点若另外舍入必须计差。这个门只需原真实速度和有限试函数的完整解析残差，不对未知误差求导。源可在实际原径向片先合带符号的时间/角谱再估，不忽略截频外乘积。计算核在 fourfold_codazzi_true_characteristic_residual_transport.py。

$\widetilde X=\phi+(q_++q_-)/2$，$\widetilde\omega=(q_--q_+)/2$。真实 $L\omega=bX_\phi$，故在相同完整源上还可独立沿 $L$ 传播 $\omega-\widetilde\omega$，$m$ 阶源上界为
$$
 \|\partial_\phi^m(b\widetilde X_\phi-L\widetilde\omega)/m!\|_\infty+
 |b|\,(m+1)(Y_{+,m+1}+Y_{-,m+1})/2 .
$$
与两个标签直接误差的交集保持两真实相位的相关信息。一阶强制比值 $R_\sigma$ 是同样的非保守输运，右端为 CRW 的完整 $F_a,F_b$，上述证明原样适用并保留其真实初值。

## 作用量矩与实际径向接缝

写 $\rho=r_*-r>0$、$k=-K/\rho$、$B=b/\sqrt\rho=\eta\sqrt k$、$x=X_\phi$、$A=3\omega/(2\rho^{3/2})$。$L\rho=1$。由 $L\omega=bx$ 直接得
$$
 LA+\frac{3}{2\rho}A=\frac{3}{2\rho}Bx .
$$
置 $F=Bx$、$A_j=L^jA$。在每个真实单侧片上，对 $j=0,1,2$ 有
$$
 L A_j+\frac{j+3/2}{\rho} A_j=\frac{3}{2\rho} L^j F .
$$
确实，乘 $\rho$ 再沿 $L$ 微分一次即由 $j$ 得 $j+1$。设同一共同漂移特征由 $\rho_l$ 流到 $\rho_r$，$a=j+3/2$。逐实际片精确地
$$
 A_j(\rho_r)=\left(\frac{\rho_l}{\rho_r}\right)^a A_j(\rho_l^+)
  +\frac32\int_{\rho_l}^{\rho_r}
       \left(\frac{u}{\rho_r}\right)^a (L^jF)(u)\frac{du}{u}.
$$
积分权的质量为 $\frac{3}{2a}[1-(\rho_l/\rho_r)^a]$。两端 $\rho$ 使用同一个真实根。片内的未知源误差因此只乘这个有界权，而非逐点用 $1/\rho$ 或 $1/\rho^2$。在 $c$ 的初值可用同一真实根片的 $\chi,T$ 及其二维有符号 Taylor/Cauchy 导数。对任意角阶，对矩方程作上节的归一化微分；$1/\rho$ 是径向量，不产生新的角微分。齐次传播的额外因子恰是 $(\rho_l/\rho_r)^a$，强迫按相应正权积分。每一原片独立有效。

$F$、$d$、$x$、$d_\phi$ 连续；$Lx=b\omega_{\phi\phi}-d_\phi x$ 也连续。因此 $A,A_1$ 连续，$A_2$ 在每真接缝的向内跳跃必须保留
$$
 [A_2]=\frac{3}{2\rho}[LF]=\frac{3}{2\rho}[LB]x .
$$
这是从 $\rho A_2+(5/2)A_1=(3/2) LF$ 得到，等式对每个真实角可直接微分。跳跃用原一侧 $B$ 的导数。没有在此假定修复后 $m_r$ 连续。

类似地，$k(\rho)=\rho^{-1}\int_0^\rho K_r(r_*-s)ds$ 因 $K(r_*)=0$。在单侧片上 $k_j=\partial_\rho^j k$ 满足
$$ \rho(k_j)_\rho+(j+1)k_j=(-1)^j\partial_r^{j+1}K .$$
其积分权质量 $[1-(\rho_l/\rho_r)^{j+1}]/(j+1)$。$j=0,1,2$ 只用到原始真实 $K,K_r,K_{rr},K_{rrr}$。若源有接缝，直接以两侧原导数和上述微分等式确定入端；未把后片当作原根解析延拓。也可与原单侧 $-K/\rho$ 及其导数正当交取。

## 真实首振幅及其源

严格实负侧 $A,k>0$。直接回代 WUA.6、WUA.9–10 得
$$
 T=-\rho A^{2/3},\quad s=\sqrt\rho A^{1/3},\quad
 G=(k_*/\eta_*)^{1/6}E_G A^{1/6}k^{-1/4},
$$
$$
 a_0=G(x^2+4\rho^3 A_\phi^2/9),\qquad
 b_0^{\rm amp}=\frac{4i\epsilon}{3}\rho G x A_\phi A^{-1/3}.
$$
可在每真片使用 $D=-L$、$D^2=L^2$ 与 $b^2=\rho B^2$ 计算完整 WUA.13，不对单个根奇幂求两次导后才尝试相消。所需 $L A_\phi=\partial_\phi A_1-d_\phi A_\phi$，再用同一交换子有 $L^2 A_\phi=\partial_\phi A_2-2d_\phi\partial_\phi A_1+(d_\phi^2-Ld_\phi)A_\phi$。写 $v=\omega_\phi=(2/3)\rho^{3/2} A_\phi$，则
$$
 Lx=(2/3)\rho^2 B A_{\phi\phi}-d_\phi x,\qquad
 Lv=b x_\phi-d_\phi v.
$$
从 $L v_\phi=b x_{\phi\phi}-2d_\phi v_\phi-d_{\phi\phi}v$ 得
$$
 L^2x=(\rho B/3+2\rho^2 (LB)/3)A_{\phi\phi}
       +\rho B^2 x_{\phi\phi}
       -(4/3)\rho^2 B d_\phi A_{\phi\phi}
       -(2/3)\rho^2 B d_{\phi\phi} A_\phi
       -(Ld_\phi)x-d_\phi Lx .
$$
$L^2 F=(L^2B)x+2(LB)Lx+B L^2x$。若直接给 $A_2$ 至七个角导，最顶项 $x_{\phi\phi}$ 需要真实标签至十阶。CRW 直接波算子写法的标签预算仍是九阶；本正则矩公式额外这一阶不充作已算。$H_D=-i\epsilon Q_f H K_T$ 由 $DX=-Q_f T T_\phi$、$DT=Q_f x$ 及 $K_T^2=T Id$ 直接相乘。因此自由 WUA.13 的最后一项为 $+i\epsilon\vartheta Q_f(T b_0^{\rm amp},a_0)^t$。这条恒等式不替代含 $V_{\rm ext}$ 的 deformed $B$。

这里没有给出全域带符号试函数残差的数值、未将有限相位误差乘无界 $n$，亦未主张全高返回已经可逆。全过程的强迫、体/跳/平均和归一化仍须在各自原单位中接收。
