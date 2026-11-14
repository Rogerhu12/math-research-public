# R46：严格负区的真实 Cauchy 首相位、通量 frame 与强余项

2026-11-12，independent-audit。

**状态：已证明的有限组件结论。** 本篇直接对实际散度算子构造两支
有限 WKB 列，用同一真实 Cauchy 问题的源估计把其精确 residual 变成
全 Fourier 矩阵的二阶强余项。系数不必接近径向背景。主传播由真实
角流决定，首个逆频率系数来自一个明确的实密度。均值、反向支、
normal shear 以及全部端口源均保留。

角变换的准确通量矩阵也在这里给出。它由 $Q_H$ 和
$(Q_H^{-1})^*$ 共同组成；没有把 $Q_H$ 本身误认为普通 $L^2$ 酉。
最后将严格区与 R43 的真实 root collar 相接，给出在已匹配完整
frame 下的有限部分相位公式。当前候选仍须供应实际组件、所需系数
范数、正侧 Ai/source 输入和全域有限块；本篇不是 README 的闭族
完成证书。

## 1. 实际算子、尺度及几何势

在有限圆柱 $I\times S^1$，$I=[x_0,x_1]$、角周期 $2\pi$，考虑
$$
Pu=\partial_x(au_x+bu_\theta)
    +\partial_\theta(bu_x+cu_\theta)+du=f,
\qquad p=au_x+bu_\theta,
\tag{1.1}
$$
其中 $a,b,c,d$ 都是实际实系数，且在整个闭圆柱上
$$
a>0,\qquad \mu=\sqrt{b^2-ac}>0.
\tag{1.2}
$$
全部不等式取可验证的一致上下界。对所用有限阶，假设下面出现的
系数、流和导数范数有限；例如 $C^{K+8}$ 系数足够支付下文涉及
$K$ 阶角导数的一切有限量。更经济的分别径向/角导数预算也可直接
按公式支付；这里不要求无限径向光滑。

记
$$
\alpha=a^{-1},\quad q=b/a,\quad \nu=\mu/a,\quad
D_t=\partial_x+q\partial_\theta,\quad m=\mu^{-1/2},
$$
$$
T=\frac{a\mu_x+b\mu_\theta}{2\mu}
  =\frac{D_t\mu}{2\nu},\qquad
\boxed{\quad \mathcal F=\mu^{1/2}P(\mu^{-1/2}).\quad}
\tag{1.3}
$$
$P$ 在 (1.3) 中包括真实零阶项 $d$。若
$A=\left(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\right)$，
直接微分给
$$
\boxed{\quad
\mathcal F=d-\tfrac12\operatorname{div}(A\nabla\log\mu)
             +\tfrac14(\nabla\log\mu)^tA\nabla\log\mu.
\quad}
\tag{1.4}
$$
它一般不等于原零阶势 $d$。

令 $\Lambda e_j=\max(1,|j|)e_j$，$D=-i\partial_\theta$，
$J_f=\operatorname{sgn}D$（均值上为零）；$\Pi_\varepsilon$ 为
$\varepsilon j>0$ 的投影，$\Pi_0$ 为均值投影。
使用完整空间
$$
E_s=(H^s)^2,\qquad
\mathcal P_s=H^{s+1/2}\oplus H^{s-1/2},
\tag{1.5}
$$
后一个空间的两项是准确的 $(u,p)$。

对实或复函数 $v$，使用可计算的乘法上界
$$
M_s(v)=2^{|s|/2}\sum_l\langle l\rangle^{|s|}|v_l|,
\qquad \|M_v:H^s\to H^s\|\le M_s(v).
\tag{1.6}
$$
径向依赖量的 $M_s$ 可逐 $x$ 使用，或取一致上界。

## 2. 同一个真实 Cauchy 问题的有限范数

本节把 R32 的能量常数写成可直接计算的有限矩阵，不借用一个
尚未证明的高频逆。令 $\gamma=\mu^2/a$、$Z=(u,u_\theta,p)^t$。
则 (1.1) 准确等价于约束保持的系统
$$
Z_x=A_3Z_\theta+B_3Z+(0,0,f)^t,
\tag{2.1}
$$
$$
A_3=\begin{pmatrix}0&0&0\\0&-q&\alpha\\0&\gamma&-q\end{pmatrix},
\quad
B_3=\begin{pmatrix}0&-q&\alpha\\0&-q_\theta&\alpha_\theta\\
-d&\gamma_\theta&-q_\theta\end{pmatrix},
\quad H_3=\operatorname{diag}(1,\gamma,\alpha).
\tag{2.2}
$$
$H_3A_3$ 对称。初始第二分量为 $u_\theta$ 时，第一式的角导数与
第二式相同，因此约束在真实演化中保持。

为控制 $k$ 阶角导数，将 $Z_j=\partial_\theta^jZ$，$0\le j\le k$，
堆成向量。令 $A_k$ 为 $A_3$ 的块对角阵，
$H_k=\operatorname{diag}_{j=0}^k[\binom kjH_3]$。$B_k$ 的第
$(j,l)$ 块是以下两项之和（范围外取零）：
$$
\binom j{j-l}\partial_\theta^{j-l}B_3\quad(0\le l\le j),
\qquad
\binom j{j-l+1}\partial_\theta^{j-l+1}A_3\quad(1\le l\le j).
\tag{2.3}
$$
取
$$
\Gamma_k(x)=\frac12\sup_\theta\left\|
H_k^{-1/2}\{(H_k)_x-(H_kA_k)_\theta+H_kB_k+B_k^*H_k\}
H_k^{-1/2}\right\|,
\tag{2.4}
$$
$$
h_* =\inf\min(1,\gamma,\alpha)>0,\qquad
h^* =\sup\max(1,\gamma,\alpha),
$$
$$
\mathfrak E_{k+1/2}
=\sqrt{h^*/h_*}\exp\left(\int_{x_0}^{x_1}\Gamma_k(x)dx\right).
\tag{2.5}
$$
这些量不要求小。它们给正向、反向、任意子区间的真实齐次传播
$\mathcal T(x,y)$ 的界
$$
\|\mathcal T(x,y):\mathcal P_s\to\mathcal P_s\|
\le\mathfrak E_s.
\tag{2.6}
$$
先在 $s=k+1/2$ 使用 (2.5)，在 $s=-k-1/2$ 使用相同常数，再在
相邻已付层之间取 Hilbert 插值常数。

**证明。** 对 (2.1) 及其角微分作能量估计，分部积分只产生
(2.4) 的 Hermitian 矩阵。又
$$
\sum_{j=0}^k\binom kj\|\partial_\theta^jZ\|_2^2
=\|u\|_{H^{k+1}}^2+\|p\|_{H^k}^2.
$$
因此 Gronwall 给 (2.5)。同一矩阵 norm 同时控制反向演化。
Friedrichs 截断和该一致能量界构造实际解，反向估计给唯一性及满射。
真实 Green 恒等式保存
$$
\frac1i\int(p\overline u-u\overline p),
\tag{2.7}
$$
其对偶空间恰为 $\mathcal P_{-s}$。对反向传播取该通量伴随，得到
负 $s$ 的 (2.6)。插值给其余有限实窗口。以上都保留均值。

实际普通源由 Duhamel 精确给出，特别
$$
\|(u,p)(x)\|_{\mathcal P_s}
\le\mathfrak E_s\left(\|(u,p)(y)\|_{\mathcal P_s}
             +\int_y^x\|f(r)\|_{H^{s-1/2}}dr\right),
\tag{2.8}
$$
反向时将积分改为无向区间积分。源若原来具有额外 divergence 或
boundary-contact 结构，必须先保持其实际结构再作相应变换；不能
只把它的名称换成 (2.8) 的普通源。$\square$

## 3. 准确通量 frame 与真实坐标变化

### 3.1 包括均值与 normal shear 的 frame

定义
$$
U=M_m\Lambda^{-1/2},\qquad
Y=M_{\mu^{1/2}}\Lambda^{1/2}=(U^*)^{-1},
$$
$$
\boxed{\quad
\mathscr F(x)\binom{z_+}{z_-}
=\frac1{\sqrt2}
\binom{U(z_++z_-)}{-TU(z_++z_-)+iY(z_+-z_-)}.
\quad}
\tag{3.1}
$$
$U^*(-TU)$ 自伴且 $U^*Y=I$，所以
$$
\mathscr F^*\left[\frac1i
\begin{pmatrix}0&I\\-I&0\end{pmatrix}\right]\mathscr F
=J,\qquad J=\operatorname{diag}(I,-I).
\tag{3.2}
$$
它在全空间上准确可逆：令
$$
r=\Lambda^{1/2}\mu^{1/2}u,\qquad
t=-i\Lambda^{-1/2}\mu^{-1/2}(p+Tu),\qquad
z_\pm=(r\pm t)/\sqrt2.
\tag{3.3}
$$
此处实 shear $T$ 没有并入一个未计算的“较低阶项”。

以下显式有限数可供后文使用：
$$
u_s=2^{1/4}M_{s+1/2}(m),\quad
y_s=M_{s-1/2}(\mu^{1/2}),\quad t_s=M_{s-1/2}(T),
$$
$$
F_s=\{u_s^2+(t_su_s+y_s)^2\}^{1/2},
\tag{3.4}
$$
$$
I_s=\{M_{s+1/2}(\mu^{1/2})^2
       +\sqrt2 M_{s-1/2}(m)^2(1+t_s^2)\}^{1/2}.
\tag{3.5}
$$
由 (1.6) 及 $\Lambda$ 与 $\langle D\rangle$ 的比较，
$\|\mathscr F:E_s\to\mathcal P_s\|\le F_s$、
$\|\mathscr F^{-1}:\mathcal P_s\to E_s\|\le I_s$。
故准确幅度传播
$$
\mathcal C(x,y)=\mathscr F(x)^{-1}\mathcal T(x,y)\mathscr F(y)
\tag{3.6}
$$
是 onto $J$-unitary，且 norm 不超过 $I_s(x)\mathfrak E_sF_s(y)$。

### 3.2 正 height 变化的准确抵消

若 $u=t v$，$t>0$，采用实际共轭算子 $\widetilde P=tPt$，则
$$
\widetilde A=t^2A,\quad\widetilde\mu=t^2\mu,\qquad
\widetilde T=t^2T+t(a t_x+b t_\theta).
\tag{3.7}
$$
真实 conormal 满足
$$
t p_u=p_v+t(a t_x+b t_\theta)v.
\tag{3.8}
$$
将 (3.7)–(3.8) 代入 (3.3)，$r,t$ 两个幅度组合都准确不变。
因此这一 height 共轭在本 frame 中不另生一个未计入的首相位。

### 3.3 真实角变换不是只乘主 half-density

设旧角坐标 $\theta=H(x,\eta)$，$H_\eta>0$，$H$ 为 degree-one
圆微分同胚。固定 $x$，记 $C_Hv=v\circ H$。密度式坐标变化准确给
$$
u_{\rm new}=C_Hu,\quad p_{\rm new}=H_\eta C_Hp,\quad
\mu_{\rm new}=C_H\mu,\quad T_{\rm new}=H_\eta C_HT.
\tag{3.9}
$$
即使 $H$ 依赖 $x$，其 $H_x$ 项也在 conormal 内准确相消。
定义
$$
Q_H=\Lambda^{1/2}C_H\Lambda^{-1/2},\qquad
P_H=\Lambda^{-1/2}M_{H'}C_H\Lambda^{1/2}=(Q_H^{-1})^*.
\tag{3.10}
$$
由 (3.3)，完整幅度变化为
$$
\boxed{\quad
\mathscr G_H=\frac12
\begin{pmatrix}Q_H+P_H&Q_H-P_H\\Q_H-P_H&Q_H+P_H\end{pmatrix}.
\quad}
\tag{3.11}
$$
$\mathscr G_H$ 准确 onto $J$-unitary。$Q_H$ 本身一般不是普通
$L^2$ 酉，故不能只用它的 principal half-density 忽略 (3.11)。

这里有一个比一般主符号论更强的准确矩阵事实。由
$D C_H=M_{H'}C_HD$，当 $j,k\ne0$ 时
$$
(P_H)_{kj}=\operatorname{sgn}(k)\operatorname{sgn}(j)(Q_H)_{kj}.
\tag{3.12}
$$
因此同号 Fourier 块上 $P_H=Q_H$ **逐项准确成立**；差只出现在
跨符号及均值行列。$Q_He_0=e_0$；$P_He_0=\Lambda^{-1/2}H'$，
其真实非零输出也须保留。下面 §4 的分部积分给这些差任意已付的
有限阶强平滑界。

此外
$$
Q_HQ_G=Q_{G\circ H},\qquad
\mathscr G_H\mathscr G_G=\mathscr G_{G\circ H}
\tag{3.13}
$$
都准确成立。若反转径向方向，conormal 与 $T$ 同时反号，(3.3)
中的 $r$ 不变、$t$ 反号，即两个幅度支准确互换。

## 4. 有限角流的明确复合与跨频率常数

本节只需要实际实角图的有限导数，供后文全部强范数使用。
若 $H'\ge m_H>0$，定义 Bell 系数
$$
b_{00}=1,\qquad b_{j+1,l}=\partial_\theta b_{jl}+H'b_{j,l-1},
\tag{4.1}
$$
范围外系数取零。于是
$\partial_\theta^j(v\circ H)=\sum_l b_{jl}(v^{(l)}\circ H)$。
对整数 $k\ge0$ 取
$$
N_k(H)=m_H^{-1/2}
\left[\sum_{j=0}^k\binom kj
                   \left(\sum_{l=0}^j\|b_{jl}\|_\infty\right)^2\right]^{1/2}.
\tag{4.2}
$$
则 $\|C_H:H^k\to H^k\|\le N_k(H)$。负整数层可取
$$
N_{-k}(H)=M_k\bigl(1/(H'\circ H^{-1})\bigr)N_k(H^{-1}),
\tag{4.3}
$$
因为 $C_H^*=M_{1/(H'\circ H^{-1})}C_{H^{-1}}$。其余实层用
相邻整数插值。记结果仍为 $N_s(H)$。

再对一个实际乘子 $a_0$ 定义跨符号常数。对 $t\in[0,1]$ 令
$\psi_t=tH+(1-t)\theta$，并递推
$$
v_0=a_0,\qquad v_{r+1}=-\partial_\theta(v_r/\psi_t'),
\qquad B_N(a_0,H)=\sup_{t,\theta}|v_N(t,\theta)|.
\tag{4.4}
$$
$\psi_t'\ge\min(1,m_H)$，所以只需要明确的有限导数与正下界。
若输入 $\varepsilon j>0$，输出 $\varepsilon k\le0$，则
$$
|(M_{a_0}C_H)_{kj}|
\le B_N(a_0,H)(|j|+|k|)^{-N}.
\tag{4.5}
$$
这是以整数 $|j|+|k|$ 为振荡参数，对周期积分分部 $N$ 次的准确
估计，边界项为零。对 $t_0\ge0$，选整数
$N>2|s|+t_0+1$，可取
$$
X_{s,t_0}(a_0,H)
=2^{2|s|+t_0+1}B_N(a_0,H)
 \left(1+\frac1{N-2|s|-t_0-1}\right)
\tag{4.6}
$$
作为
$$
\| (\Pi_{-\varepsilon}+\Pi_0)M_{a_0}C_H\Pi_\varepsilon:
H^s\to H^{s+t_0}\|
\tag{4.7}
$$
的上界。证明是在 (4.5) 中乘两侧 Sobolev 权，分别对行、列求和
后用 Schur 判据；所用级数由 $1+1/(p-1)$ 控制。含均值输入的
单列直接以其实际输出 $H^{s+t_0}$ norm 支付。

这些都是有限无权范数。仅有有限 $C^N$ 不能由 (4.5) 推出正
direct-log 宽度。若同一角图确实解析，可改用 R41 的真实复合及
指数跨频率界；严格区的加权 Cauchy/source 仍须使用实际已付估计。

## 5. Riccati 系数与精确有限 WKB residual

### 5.1 Riccati 的首个实势

在正频率上先形式地写 $p=Z_\sigma u$，$\sigma=\pm1$。准确
Riccati 恒等式为
$$
(Z_\sigma)_x+i(qDZ_\sigma-Z_\sigma qD)+q_\theta Z_\sigma
 +Z_\sigma\alpha Z_\sigma+\gamma D^2-i\gamma_\theta D+d=0.
\tag{5.1}
$$
按 $D$ 次数消去二阶、一阶及零阶，得到
$$
\boxed{\quad
Z_\sigma=i\sigma\mu D+\frac\sigma2\mu_\theta-T
           +\frac{i\sigma\mathcal F}{2\nu}D^{-1}
           +\text{至少二阶降阶项}.
\quad}
\tag{5.2}
$$
这里只把 (5.2) 用作有限系数恒等式；实际传播由下一节的精确列
构造支付，不假设存在收敛的无限 Riccati 级数。

为核对零阶系数，置 $A_0=\mu_\theta/2$。其偶部分为
$$
d-D_tT-q_\theta T+\mu\partial_\theta(\alpha A_0)
                  +\alpha(A_0^2+T^2)=\mathcal F,
\tag{5.3}
$$
其奇部分准确为零，因为
$$
D_tA_0+q_\theta A_0-\mu\partial_\theta(\alpha T)
                                     -2\alpha A_0T=0.
\tag{5.4}
$$
(5.3) 也可直接化为 (1.4)。$D v=vD-i v_\theta$ 给全部这些系数。
特别两支通过该阶互为通量伴随，不能删掉实项
$\sigma\mu_\theta/2-T$。

### 5.2 真实特征流与一阶修正

令
$$
v_\sigma=q-\sigma\nu,\qquad
\partial_x\Theta_\sigma(x,\eta)
 =v_\sigma(x,\Theta_\sigma(x,\eta)),\quad
\Theta_\sigma(x_0,\eta)=\eta,\qquad S_\sigma=\Theta_\sigma^{-1}.
\tag{5.5}
$$
实际 ODE 的 $\Theta_{\sigma,\eta}$ 是
$\exp\int\partial_\theta v_\sigma$，故严格为正；其余所需有限
导数逐阶由同一个变分方程计算。整个过程以真实 $x$ 为时间，不
把径向变量隐式混入角变量。

令 $D_\sigma=\partial_x+v_\sigma\partial_\theta$，定义实际实函数
$$
D_\sigma h_\sigma=\frac{\mathcal F}{2\mu S_{\sigma,\theta}},
\qquad h_\sigma(x_0,\theta)=0.
\tag{5.6}
$$
它的输入角表达为
$$
\widehat h_\sigma(x,\eta)
=h_\sigma(x,\Theta_\sigma(x,\eta))
=\int_{x_0}^x\frac{\mathcal F}{2\mu}
 (r,\Theta_\sigma(r,\eta))\Theta_{\sigma,\eta}(r,\eta)dr.
\tag{5.7}
$$

输入频率 $j\ne0$，记 $\lambda=|j|$、$\varepsilon=\operatorname{sgn}j$；
幅度支用 $\tau=\pm1$，特征支为 $\sigma=\tau\varepsilon$。定义
$$
u^{\rm app}_{\tau,j}
=\frac1{\sqrt2}\lambda^{-1/2}m e^{ijS_\sigma}
                         (1+i\tau h_\sigma/\lambda),
\qquad p^{\rm app}_{\tau,j}=a u^{\rm app}_{\tau,j,x}
                            +b u^{\rm app}_{\tau,j,\theta}.
\tag{5.8}
$$
其 residual 是**精确等式**
$$
\boxed{\quad
P u^{\rm app}_{\tau,j}
=\frac{i\tau}{\sqrt2}\lambda^{-3/2}e^{ijS_\sigma}P(mh_\sigma).
\quad}
\tag{5.9}
$$

**证明。** 有
$$
A\nabla S_\sigma
=\sigma\mu S_{\sigma,\theta}(1,v_\sigma),\qquad
\operatorname{div}(A\nabla S_\sigma)
=\sigma (D_\sigma\mu)S_{\sigma,\theta}.
$$
所以 eikonal 项为零，$m=\mu^{-1/2}$ 准确解其输运振幅方程。
对 $m(1+i\tau h/\lambda)e^{ijS}$ 展开 $P$，交叉项恰为
$-2\mu m S_\theta D_\sigma h=-m\mathcal F=-Pm$，留下 (5.9)。
没有任何未控制的逐列 $O(\lambda^{-2})$。

在起点，$h=h_\theta=0$、$h_x=\mathcal F/(2\mu)$。因此高度与
(3.1) 完全相同，而准确初始 momentum 差为
$$
\frac{i\tau}{\sqrt2}m\frac{\mathcal F}{2\nu}
                          \lambda^{-3/2}e^{ij\theta}.
\tag{5.10}
$$
它也必须由真实 Cauchy 估计支付。$\square$

## 6. 从精确 residual 到全矩阵二阶强余项

固定输出 $x\in I$。下列所有 $S_\sigma,h_\sigma$ 在所示 $x$ 或
积分变量处取值。令
$$
\mathfrak R_s(r)=2^{1/4}\sum_{\tau,\varepsilon=\pm1}
 M_{s+3/2}(P(mh_{\tau\varepsilon}))(r)
 N_{s+3/2}(S_{\tau\varepsilon}(r)),
\tag{6.1}
$$
$$
d_s=2^{3/4}M_{s+3/2}\left(m\mathcal F/(2\nu)\right)(x_0),
$$
$$
C_s^{\rm err}=I_{s+2}(x)\mathfrak E_{s+2}
 \left[d_s+\int_{x_0}^x\mathfrak R_s(r)dr+F_{s+2}(x_0)\right]+1.
\tag{6.2}
$$
这里 $\mathfrak E_{s+2}$ 可以取整个 $I$ 的上界。定义
$$
\mathcal W_0=\Pi_0 I+
\operatorname{diag}_{\tau=\pm1}
 \sum_{\varepsilon=\pm1}\Pi_\varepsilon Q_{S_{\tau\varepsilon}}
 \left(I+i\tau M_{\widehat h_{\tau\varepsilon}}\Lambda^{-1}\right)
 \Pi_\varepsilon.
\tag{6.3}
$$
两个幅度支以及两种频率符号都在这里保留。

**定理 6.1。** 准确传播 (3.6) 满足
$$
\boxed{\quad\mathcal C(x,x_0)=\mathcal W_0+R_2,\qquad
R_2:E_s\longrightarrow E_{s+2}.\quad}
\tag{6.4}
$$
下面给一个完整显式上界。对每个 $\sigma=\tau\varepsilon$，置
$$
X_s^\sigma=2^{1/4}X_{s+1/2,2}(1,S_\sigma)
                  +2^{3/4}X_{s+3/2,1}(h_\sigma,S_\sigma),
\tag{6.5}
$$
$$
L_s^\sigma=2M_{s+3/2}
 \left(\frac{\mathcal F}{2\mu\nu S_{\sigma,\theta}}\right)
 N_{s+3/2}(S_\sigma),
\tag{6.6}
$$
$$
K_s(v)=2^{1+|s+2|/2}\sum_l\langle l\rangle^{|s+2|+1}|v_l|.
\tag{6.7}
$$
则可以取
$$
\boxed{\quad
\|R_2:E_s\to E_{s+2}\|
\le C_s^{\rm err}
 +\sum_{\tau,\varepsilon=\pm1}
 \left[2X_s^{\tau\varepsilon}+L_s^{\tau\varepsilon}
  +2^{1/4}N_{s+5/2}(S_{\tau\varepsilon})
                 K_s(\widehat h_{\tau\varepsilon})\right].
\quad}
\tag{6.8}
$$
没有系数幅度小性条件。

**证明第一步：真实源修正。** 将 (5.8) 按全部非零输入频率求和，
记真实两行 $(Q,p_Q)$。式 (5.9)、(1.6)、(4.2)–(4.3) 直接给
$$
\|PQ:E_s\to H^{s+3/2}\|\le\mathfrak R_s.
$$
这是算子复合界，不是由单列范数猜出的全矩阵界。初始差 (5.10)
的 $H^{s+3/2}$ norm 由 $d_s$ 控制。用 (2.8)，再用
$\mathscr F(x)^{-1}$，得到与真实非零列传播之间的 $E_s\to E_{s+2}$
差，界为 (6.2) 中去掉 $F_{s+2}(x_0)$ 和末尾 $1$ 的部分。

均值在 WKB 主式中暂取 $\Pi_0 I$，其**真实**差为
$\mathcal C\Pi_0-\Pi_0$。均值输入在全部 Sobolev 阶 norm 相同，
所以 (2.6)、(3.4)–(3.5) 给
$I_{s+2}\mathfrak E_{s+2}F_{s+2}(x_0)+1$，正是 (6.2) 的余下项。
它虽只有两个输入列，其无限输出按实际高阶 norm 全部支付了。

**第二步：准确变换实际 momentum。** 对一列的 Fourier 算子，写
$$
K=\Lambda^{1/2}C_{S_\sigma}
 (I+i\tau M_{\widehat h_\sigma}\Lambda^{-1})\Lambda^{-1/2}\Pi_\varepsilon,
$$
$$
L=\Lambda^{-1/2}M_{\mathcal F/(2\mu\nu S_{\sigma,\theta})}
                    C_{S_\sigma}\Lambda^{-3/2}\Pi_\varepsilon.
\tag{6.9}
$$
将完整 $p_Q$ 代入 (3.3)，精确得到
$$
r=K/\sqrt2,\qquad
t=\frac\tau{\sqrt2}(\varepsilon J_fK+L).
\tag{6.10}
$$
关键消去是
$D_th_\sigma/\nu-\sigma h_{\sigma,\theta}
=\mathcal F/(2\mu\nu S_{\sigma,\theta})$。
故同幅度支的输出为
$$
\Pi_\varepsilon K+\tfrac12\Pi_0K+\tfrac12L,
$$
另一幅度支为
$$
\Pi_{-\varepsilon}K+\tfrac12\Pi_0K-\tfrac12L.
\tag{6.11}
$$
(4.7) 分别给坏符号/均值部分的界 (6.5)；(1.6) 给 $L$ 的二阶
强界 (6.6)。合并两行至多付 $2X_s^\sigma+L_s^\sigma$。

**第三步：明确 ordering 费用。** 同支剩余 $K$ 准确为
$$
Q_{S_\sigma}
 [I+i\tau\Lambda^{1/2}M_{\widehat h_\sigma}\Lambda^{-3/2}]
 \Pi_\varepsilon.
$$
把方括号中的修正换为 $i\tau M_{\widehat h_\sigma}\Lambda^{-1}$，
矩阵差为
$$
(\sqrt{\Lambda_k}-\sqrt{\Lambda_j})
       (\widehat h_\sigma)_{k-j}\Lambda_j^{-3/2}.
$$
对非零输入 $j$，其绝对值不超过
$|k-j||(\widehat h_\sigma)_{k-j}|\Lambda_j^{-2}$。
Peetre 不等式和 Young 给准确的二阶上界 (6.7)。再乘
$Q_{S_\sigma}:H^{s+2}\to H^{s+2}$ 的界
$2^{1/4}N_{s+5/2}(S_\sigma)$，即得 (6.8)。$\square$

完整普通源在幅度 frame 中的输出仍为
$$
\mathscr F(x)^{-1}\int_y^x\mathcal T(x,r)(0,f(r))^t dr,
\tag{6.12}
$$
其 $E_s$ norm 不超过 $I_s(x)\mathfrak E_s\int\|f(r)\|_{H^{s-1/2}}dr$。
任何随后消端口或 Schur 操作都须同时带上这项与均值。

## 7. 首系数平均、密度不变量与准确角群

由 (5.7) 对输入角积分、再用 $d\theta=\Theta_{\sigma,\eta}d\eta$，
两种特征支有完全相同的平均：
$$
\boxed{\quad
\langle\widehat h_\sigma(x_1)\rangle
=\frac1{4\pi}\int_{x_0}^{x_1}\int_0^{2\pi}
                        \frac{\mathcal F}{\mu}\,d\theta dx.
\quad}
\tag{7.1}
$$
这里没有用角平均势代替实际特征；Jacobian 是从真实变分方程中
准确消掉的。

### 7.1 坐标与 height 不变量

对保向真实二维坐标 $\Psi$，$J_\Psi>0$，密度变换为
$\widetilde A=D\Psi A D\Psi^t/J_\Psi$，故
$$
\widetilde\mu=\mu\circ\Psi^{-1},\qquad
\widetilde{\mathcal F}=(\mathcal F/J_\Psi)\circ\Psi^{-1}.
\tag{7.2}
$$
因此 $\mathcal F\,dx\,d\theta/\mu$ 是一个实际密度。
若 $\widetilde P=tPt$、$t>0$，则
$\widetilde\mu=t^2\mu$、
$\widetilde{\mathcal F}=t^2\mathcal F$，因为
$tP[t(t^2\mu)^{-1/2}]=tP(\mu^{-1/2})$。
所以 $\widetilde{\mathcal F}/\widetilde\mu=\mathcal F/\mu$。
反向坐标以绝对 Jacobian 的密度形式理解。

### 7.2 首相位在真实角共轭下的平均不变

在一个固定符号锥上，一阶算子
$M_v\Lambda^{-1}$ 被 $Q_H$ 共轭后，其首系数为
$$
Q_H(M_v\Lambda^{-1})Q_H^{-1}
=M_{(v\circ H)H'}\Lambda^{-1}+R_2.
\tag{7.3}
$$
另一方向的首系数为 $(v/H')\circ H^{-1}$。两者的角平均均为
$\langle v\rangle$。

这里 $R_2$ 是所付有限窗口内的真实强余项。一个完全有限的证明是：
先用 $D C_H=M_{H'}C_HD$ 把 $C_HD^{-1}C_H^{-1}$ 改为
$D^{-1}M_{H'}$；均值的误差是实际光滑有限输入列。再交换
$D^{-1}$ 与乘子，矩阵差为 $v_{k-j}(j-k)/(jk)$，在同号频率上
由 (1.6) 加一阶 lag 权给二阶界；坏频率由 (4.5)–(4.7) 支付。
最后将 $\Lambda^{\pm1/2}$ 交换到外侧，用与 (6.7) 相同的矩阵
估计。所有费用只由本篇的 $M,N,X,K$ 在相应移位窗口给出，有限
个有界算子复合时逐项相乘即可。没有假设普通 half-density 与
$Q_H$ 的完整次首符号相同。

所以有限多个实际段的主 $Q_H$ 因 (3.13) 准确合成，而它们的
实一阶相位平均按 (7.3) 相加。若实际返回图确有一个已付的
圆共轭到旋转，继续用准确的 $Q_H$ 群作共轭不会再增加该平均。
同号压缩引起的差由 (3.12) 与 (4.7) 支付。下面把普通酉修正的
满射与强常数也明确支付。令
$\widetilde Q_H=\Pi_{\ne0}Q_H|_{\Pi_{\ne0}L^2}$。因为 $Q_He_0=e_0$，
这是准确的常数商作用，逆为 $\widetilde Q_{H^{-1}}$。真实换元
$C_H^*DC_H=D$ 给
$$
\widetilde Q_H^*J_f\widetilde Q_H=J_f,\qquad
\widetilde Q_HJ_f\widetilde Q_H^*=J_f.
\tag{7.4}
$$
第二式使用上述实际商逆，未借用未经支付的 Fredholm index。
按正、负频率把它分成 $\left(\begin{smallmatrix}A&B\\C&D_0\end{smallmatrix}\right)$，
有
$$
A^*A-I=C^*C,\qquad AA^*-I=BB^*.
\tag{7.5}
$$
故 $A$ 同时有闭像、单射及满射，$\|A^{-1}\|\le1$。
$U=A(I+C^*C)^{-1/2}$ 是准确 onto unitary。

为给完整强常数，记 $L=C^*C\ge0$，对实际所付窗口令
$$
K_{s,m}=\|L:H^s\to H^{s+m}\|,\qquad
J_s=\|L:H^0\to H^{|s|}\|,\qquad m\ge0.
$$
$K,J$ 由 (4.7) 与相应负窗口的伴随界相乘支付。
$R_\mu=(\mu+L)^{-1}$，$\mu\ge1$，先有 $\|R_\mu\|_{L^2}\le\mu^{-1}$。
由 $R_\mu=\mu^{-1}(I-LR_\mu)$，对 $s\ge0$ 得
$\|R_\mu\|_{H^s}\le\mu^{-1}(1+J_s/\mu)$；负层由自伴对偶得到
同一式。准确谱积分
$$
(I+L)^{-1/2}-I
=-\frac2\pi\int_0^\infty (1+t^2)^{-1}L R_{1+t^2}\,dt
\tag{7.6}
$$
于是给
$$
\boxed{\quad
\|U-A:H^s\to H^{s+m}\|
\le\|A\|_{H^{s+m}\to H^{s+m}}\,
K_{s,m}\left(\frac12+\frac{3J_s}{8}\right).\quad}
\tag{7.7}
$$
所用两个积分是 $\int_0^\infty(1+t^2)^{-2}dt=\pi/4$ 和
$\int_0^\infty(1+t^2)^{-3}dt=3\pi/16$。
因此这个准确 polar 不改已付的 $1/j$ 首相位。
常数商只用于角 frame 的构造；实际 PDE 的 mean 行列已经在
§6 全部回填，不能因为 (7.4) 就从原问题删掉。上述事实也不能
代替全 PDE 的端口满射与源接线。

## 8. 固定 regular cut 上的 Airy 次首项

为将 (7.1) 与 R43 拼接，需要 root frame 到 (3.1) 的实际次首项，
不能只比较振幅。令
$Y_\tau(t)=\operatorname{Bi}(-t)+i\tau\operatorname{Ai}(-t)$，
$\eta=\tfrac23t^{3/2}$、$Z=t^{1/4}Y_\tau(t)$。R43 给准确终端
Volterra 方程及 $Z''+(1+5/(36\eta^2))Z=0$。置
$A_*=5/72$，则
$$
Z_{\rm app}=\pi^{-1/2}e^{i\tau(\eta+\pi/4)}
                         (1-i\tau A_*/\eta)
\tag{8.1}
$$
的准确 residual 为
$$
Z_{\rm app}''+(1+5/(36\eta^2))Z_{\rm app}
=-\frac{2i\tau A_*(1+A_*)}{\sqrt\pi\,\eta^3}
                           e^{i\tau(\eta+\pi/4)}.
\tag{8.2}
$$
与同一个无穷端振荡条件相减，Volterra 迭代给，对 $t\ge1$，
$$
\sqrt\pi|Z-Z_{\rm app}|\le\frac1{4\eta^2},\qquad
\sqrt\pi|Z'-Z_{\rm app}'|\le\frac1{4\eta^2}.
\tag{8.3}
$$
确切地，residual 的 $L^1([\eta,\infty))$ 为
$A_*(1+A_*)\eta^{-2}/\sqrt\pi$；再乘
$e^{5/(36\eta)}\le e^{5/24}<4/3$，小于 (8.3) 的右端。
对导数，微分同一个 Volterra 公式后以 $|\cos|\le1$ 得相同上界。

对物理频率 $\lambda=q|j|$、固定 cut $\xi=\delta>0$，这给
$$
D_\tau(\delta,j)
=\frac c{\sqrt\pi}\lambda^{-1/2}\delta^{-1/4}
 e^{i\tau(\lambda\frac23\delta^{3/2}+\pi/4)}
 \left[1-\frac{5i\tau}{48\lambda\delta^{3/2}}
                         +O_{\rm strong}(\lambda^{-2})\right].
\tag{8.4}
$$
高度余项的无量纲系数至多 $9/(16\delta^3)$；动量使用
$D_\tau'+D_\tau/(4\delta)$，其主相同，另外多出的
$A_*/\eta^2$ 也为二阶。因此 (8.3) 同时给准确 Cauchy 两行的强
二阶余项。频率若未满足 $\delta\lambda^{2/3}\ge1$，只有有限个
模式，按 R39 的准确 Ai 值、导数和 (3.3) 支付有限列，不能删除。

特别，在 (3.1) 的 canonical frame 内，真实 Airy 到严格区的
同支首相位正好是
$$
\boxed{\quad -\frac{5\tau}{48q\,j_{\rm abs}\,\delta^{3/2}},
\qquad j_{\rm abs}=|j|.\quad}
\tag{8.5}
$$
跨幅度支余项为二阶；这是包含实 shear $1/(4\delta)$ 后的结论。
若使用 $2\pi$ 角 $\vartheta=q\phi$，canonical 密度为
$\operatorname{diag}(1/q,-q\xi)$，conormal 为 $U_\xi/q$，
$T=1/(4q\xi)$。与 R39 振幅之间另有准确实常数
$\sqrt{2/\pi}\,c\,q^{-1/2}$；它必须按完整通量归一同步携带。
这个实常数不产生 (8.5) 的虚首相位。

例如自由 Tricomi 算子 $a=1,b=0,c=-x,d=0$ 有
$$
\mathcal F=\frac5{16x^2},\quad\mu=\sqrt x,\qquad
\frac12\int_{x_0}^{x_1}\frac{\mathcal F}{\mu}dx
=\frac5{48}(x_0^{-3/2}-x_1^{-3/2}),
\tag{8.6}
$$
与两个 (8.5) 的差准确一致。这同时核对 (5.2)、(5.9) 的符号。

## 9. 两个真实 simple turn 之间的有限部分相位

本节是上述定理的接线推论，**前提按实际对象逐项列出**：

1. 一个负组件的两端都有 R39 的真实 canonical collar，坐标、height、
   full conormal、source 均已经准确给出；中间严格区满足本篇。
2. 每个 collar 的实际势及首 Dyson 输入满足 R43，正侧同一 full
   realization 满足 R45 的 Ai residual/source 门，从而同一个
   root frame 上真实反射为 $-I+R_{4/3}$，包括 cross。
3. 若端口还接有 regular cut、尾或别的组件，先按实际全网保留它们
   的全部源和反馈；本节单一双根公式只应用于确实满足前两项的
   两端闭合组件。使用的每个 inverse/Schur 块都须有实际有限窗口
   的界；全局有限低块并不由下列高频公式自动可逆。

在上述前提下，一个来回的高频反馈主式可写成
$$
I+Q_{\mathcal R}\left(I+iM_\beta\Lambda^{-1}\right)+R_{4/3},
\tag{9.1}
$$
其中 $\mathcal R$ 为实际两支特征的返回图，$R_{4/3}$ 是包含全部
跨支及 source 接线误差的强余项；$\beta$ 的角依赖可由前述精确
相位系数逐段 (7.3) 相加。这里显示的 $+$ 对应以下固定约定：
两端 root Ai 反射各为 $-I$，每次通过两根之间的主 Airy 接合有
两个 $\pi/4$ 相位；来回的 Maslov 因子为 $-1$，移到反馈左端为
(9.1)。若另换 frame 或端口定向，必须同时变换反馈式，不能只
抄一个常相位。

该约定下完整首系数的平均为
$$
\boxed{\quad
\langle\beta\rangle=\frac1{2\pi}
          \operatorname{FP}\int_\Omega\frac{\mathcal F}{\mu}
                                             dx\,d\theta.
\quad}
\tag{9.2}
$$
这不是用一个 principal 返回图代替 PDE 低阶项；$\mathcal F$ 来自
整个实际算子 (1.1)。准确的有限部分定义如下。第 $i$ 个 canonical
root 角周期为 $\ell_i$，取 cut $\xi_i=\delta_i$，$\Omega_\delta$
为删去两个 collar 后的严格区。则
$$
\begin{aligned}
\operatorname{FP}\int_\Omega\frac{\mathcal F}{\mu}
={}&\int_{\Omega_\delta}\frac{\mathcal F}{\mu}\,dx\,d\theta\\
&+\sum_{i=\pm}\left[
 \int_0^{\delta_i}\int_0^{\ell_i}\frac{V_i(\xi,\phi)}{\sqrt\xi}
                                               d\phi\,d\xi
 -\frac{5\ell_i}{24\delta_i^{3/2}}\right].
\end{aligned}
\tag{9.3}
$$
它与合法 cut 的选择无关，等于
$$
\lim_{\delta_\pm\downarrow0}\left[
\int_{\Omega_\delta}\frac{\mathcal F}{\mu}\,dx\,d\theta
-\sum_{i=\pm}\frac{5\ell_i}{24\delta_i^{3/2}}\right].
\tag{9.4}
$$

**证明。** 在 canonical collar 中，(1.4) 准确给
$\mathcal F=V+5/(16\xi^2)$、$\mu=\sqrt\xi$；(7.2) 保证同一
密度可从物理图转入该坐标。严格区的一次通过给 (7.1)，root 的
真实势贡献由 R43 (4.3) 给，Airy 到严格 frame 的几何修正是
(8.5)。因 $q_i\ell_i=2\pi$，一次通过的平均恰为 (9.3) 除以
$4\pi$。在右根反转径向方向时，(3.3) 将两个幅度支交换；逆向
通过再加上相同的实首系数。因此来回平均是其两倍。

每次真实角变化使用 (3.11)，同号块使用 (3.12)，首系数转移用
(7.3)，故所有 Jacobian 与 half-derivative ordering 已支付；没有
另漏一个端口 shear 的 $1/j$ 项。R43 与正侧 R45 的余项都是
$4/3$ 阶，严格区及固定 cut Airy frame 的余项是二阶。有限复合
保持至少 $4/3$ 阶；若实际逆参与，使用准确恒等式
$A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}$ 和其已付窗口 norm。每项常数
由 (6.8)、R43/R45 的常数与这些有限乘子/复合 norm 相乘求和，
没有仅按逐列渐近来接线。

最后对 (9.3) 的任意 $\delta_i$ 微分：严格区边界贡献是
$-\int(V_i/\sqrt{\delta_i}+5/(16\delta_i^{5/2}))d\phi$，
势积分与显式 counterterm 正好抵消它。$V_i/\sqrt\xi$ 可积，给
(9.4)。$\square$

若随后用实际已付圆共轭与首阶同调消去 $\beta$ 的非均值部分，
常数 $1/j$ 相位仍是 (9.2)，不会因为共轭远离恒等而改变。
这允许直接对真实几何积分作区间预算；仍必须证明实际返回图的
rotation 参数、全相位小除数、余项窗口和低块，而不能由 (9.2)
单独宣布全 PDE 可逆。

### 9.1 可直接用固定物理径向 cutoff 计算同一个有限部

不必为了计算 (9.2) 先数值积分整个 canonical 流。设在一个真实
simple root 旁已经用固定材料坐标写成 $(\rho,\theta)$，
$\rho>0$ 指向负区，且
$$
b^2-ac=\rho\kappa(\rho,\theta)^2,\qquad \kappa>0.
\tag{9.5}
$$
这里 $a,b,c,d$ 是这一坐标中的同一个密度算子；左、右根各自按
其实际方向变换，不能直接沿用未反向的 mixed 系数 $b$。
假设这些函数有以下 Taylor 式所需的有限一致导数。置
$l=\log\kappa$，则 (1.4) 给准确分解
$$
\frac{\mathcal F}{\mu}
=A_0(\rho,\theta)\rho^{-5/2}
+B_0(\rho,\theta)\rho^{-3/2}
+C_0(\rho,\theta)\rho^{-1/2},
\tag{9.6}
$$
$$
\begin{aligned}
A_0&=\frac{5a}{16\kappa},\\
B_0&=\frac{a l_\rho+b l_\theta-a_\rho-b_\theta}{4\kappa},\\
C_0&=\frac1\kappa
\left[d-\tfrac12\operatorname{div}(A\nabla l)
                      +\tfrac14(\nabla l)^tA\nabla l\right].
\end{aligned}
\tag{9.7}
$$
为避免与 (5.3) 的辅助标量混淆，本小节的 $A_0,B_0,C_0$ 仅指
(9.7) 三个函数；它们不是主矩阵 $A$。
因此真实密度的两个不可积系数为
$$
\boxed{\quad f_0(\theta)=\frac{5a(0,\theta)}{16\kappa(0,\theta)},\qquad
f_1(\theta)=
\left.\frac{a_\rho-a\kappa_\rho/\kappa
                 +4b\kappa_\theta/\kappa-4b_\theta}{16\kappa}
\right|_{\rho=0}.\quad}
\tag{9.8}
$$
即
$\mathcal F/\mu=f_0\rho^{-5/2}+f_1\rho^{-3/2}+O(\rho^{-1/2})$。
在固定物理截面 $\rho=\epsilon$ 上，应准确减去
$$
\frac23\epsilon^{-3/2}\int f_0(\theta)d\theta
       +2\epsilon^{-1/2}\int f_1(\theta)d\theta.
\tag{9.9}
$$
只有在 canonical 坐标里第二项才自动为零。

**命题 9.2。** 若另一合法 root defining function 为
$y=\rho\,a_*(\rho,\theta)$，$a_*>0$，且它与真实角图至少 $C^3$，
则按 (9.9) 定义的 Hadamard 有限部与 (9.3) 相同。

**证明。** 在旧坐标中，新截面 $y=\delta$ 是
$$
\rho=r_\delta(\theta)
=k_0(\theta)\delta+k_1(\theta)\delta^2+O(\delta^3),\qquad k_0>0.
$$
真实密度的一个径向原函数在根旁是
$$
-\tfrac23 f_0\rho^{-3/2}-2f_1\rho^{-1/2}
                         +c(\theta)+O(\rho^{1/2}).
$$
将 $r_\delta$ 代入，前两项只产生 $\delta^{-3/2}$、
$\delta^{-1/2}$ 与 $O(\delta^{1/2})$；没有常数或 logarithm。
所以两个截断方式的常数项相同。依赖 $\rho$ 的角图通过真实
Jacobian 改写同一积分，(7.2) 已经保证其密度等价，也不产生额外
常数。由 canonical 展开 $f_0=5/16,f_1=0$，得到 (9.3)。
$\square$

这也给一个不含奇异 cancellation 的实际积分方法。对固定
$\eta>0$，每个根 collar 的有限部分等于
$$
\int_0^\eta\int\left[
\frac{\mathcal F}{\mu}-f_0\rho^{-5/2}-f_1\rho^{-3/2}
\right]d\theta\,d\rho
-\int\left[\tfrac23 f_0\eta^{-3/2}+2f_1\eta^{-1/2}\right]d\theta.
\tag{9.10}
$$
作 $\rho=s^2$。括号项连同 $d\rho$ 变成连续有界的实际函数
$$
2\frac{A_0(s^2)-A_0(0)-s^2A_{0,\rho}(0)}{s^4}
 +2\frac{B_0(s^2)-B_0(0)}{s^2}+2C_0(s^2).
\tag{9.11}
$$
其在 $s=0$ 的值准确为
$A_{0,\rho\rho}(0)+2B_{0,\rho}(0)+2C_0(0)$。若不愿在区间算术
中相减相近数，前两项分别用
$$
2\int_0^1(1-t)A_{0,\rho\rho}(ts^2)dt,\qquad
2\int_0^1B_{0,\rho}(ts^2)dt
\tag{9.12}
$$
替代，都是准确恒等式。故有限阶真实系数区间即可预算 (9.2)，
无须把不稳定的发散积分外推成一个“数值有限部”。

### 9.2 必须固定同一个实际零阶口径

对 R32 的真实材料 Darboux 算子，设 $u=F/|F|$。三个平移核
$P u_i=0$、$\sum_i u_i^2=1$ 给一个不需除以某个 $u_i$ 的公式：
$$
\boxed{\quad d=\sum_{i=1}^3 A\nabla u_i\cdot\nabla u_i.\quad}
\tag{9.13}
$$
证明是对 $\sum_i u_iPu_i=0$ 展开散度；单位长度的导数项为零，
余下正好是 (9.13)。这对某个平移核在腰部为零也仍成立。

若使用 R37 的固定型别修正
$\widehat P=P+Q_\ell^*(\chi\omega)Q_\ell$，则本篇应使用
$$
\widehat c=c-\chi\omega,\qquad
\widehat d=d+(\chi\omega\ell)_\theta+\chi\omega\ell^2
\tag{9.14}
$$
的**同一** $\widehat P$ 计算 $\widehat\mu,\widehat{\mathcal F}$。
不能只修正 principal 行列式而继续沿用原来的 $d$。

一种没有任意 core 过渡的可行选择有明确前提：若实际对称图中
$F_z$ 关于材料 $r$ 为奇函数，且 $F_z/r>0$ 光滑贯穿所用圆柱，
则
$$
u_z=rG,\quad G=\frac{F_z}{r|F|}>0,\qquad
\ell=\partial_\theta\log G
=\partial_\theta\log(F_z/r)-\partial_\theta\log|F|.
\tag{9.15}
$$
于是 $Q_\ell u_z=0$ 在腰部也准确成立，(9.14) 保留全局这一个
平移核；两侧正帽可以分别用 $u_z$ 与 $-u_z$。这些奇性、正下界
和光滑延拓须由实际图支付，不能从一个采样图自动授予。
不同合法 $\ell$ 不改变 principal 返回图，却改变 (9.2)。
在固定同一个 $\widehat A$ 时，两个有界零阶选择的首相位差恰为
$$
\Delta\langle\beta\rangle
=\frac1{2\pi}\int_\Omega
              \frac{\Delta\widehat d}{\widehat\mu}\,dx\,d\theta;
\tag{9.16}
$$
这是普通可积积分，因为 simple root 旁只有 $\rho^{-1/2}$。
所以实际 $\ell,\chi$ 的选择必须与后续 Newton residual 接口一致。

### 9.3 精确 PT 模型核对往返因子

取径向算子 $P=\partial_x^2-V(x)\partial_\theta^2$，其中
$V=\nu_0^2\operatorname{sech}^2x-\mu_0^2$、
$0<\mu_0<\nu_0$，在两根之间 $V>0$。这里
$\mu=\sqrt V$，(1.4) 给
$$
\frac{\mathcal F}{\mu}
=-\frac{V''}{4V^{3/2}}+\frac{5V'^2}{16V^{5/2}}
=-\frac14\left(\frac{V'}{V^{3/2}}\right)'
                         -\frac1{16}\frac{V'^2}{V^{5/2}}.
\tag{9.17}
$$
总导数在两根的原函数只有半整数发散幂，没有常数项，所以其
有限部积分为零。令 $a_*^2=\nu_0^2-\mu_0^2$、
$k_*=a_*/\nu_0$，依次作
$\tanh x=k_*\sin\vartheta$、$z=\tan\vartheta$，准确得到
$$
\frac{V'^2}{V^{5/2}}dx
=\frac{4\nu_0}{a_*^2}
 \left[(1-k_*^2)z^2+k_*^2-\frac{k_*^2}{1+z^2}\right]dz.
\tag{9.18}
$$
多项式原函数 $z^3,z$ 在真实距根变量中也只有半整数幂，故有限部
只剩 $-\pi k_*^2$。于是
$$
\operatorname{FP}\int\frac{V'^2}{V^{5/2}}dx=-\frac{4\pi}{\nu_0},
\qquad
\boxed{\quad\operatorname{FP}\int\frac{\mathcal F}{\mu}dx
                         =\frac{\pi}{4\nu_0}.\quad}
\tag{9.19}
$$
角周期 $2\pi$ 下，(9.2) 的往返 $1/n$ 系数正好为
$\pi/(4\nu_0)$。限制到 $n=4j$ 时，$1/j$ 系数为
$\pi/(16\nu_0)$，与 R34 精确 PT 谱量
$2\pi[\sqrt{(4j\nu_0)^2+1/4}-4j\mu_0]$ 的次首项一致。
这核对了 (9.2) 的因子和符号；没有由这个可解模型向任意实际
组件转授正侧或全网输入。

## 10. 本篇输入的实际正则范围与继续接线

本篇 §§1–8 的默认结论是有限无权 Sobolev 强范数。真实严格区
构造使用固定径向时间与角 ODE，不需要把一个 C4 径向样条当成
混合坐标下角解析函数。但若要放入正 direct-log 或解析角权，须
同时支付真实流的复合、乘子以及真实 Cauchy/source 的加权界。
R41 只支付角图复合；它不自动支付全部混合径向 source。

有一个对本题样条可用的严格有限径向版本。对所需各阶角导数，
若 $a,b,c,d$ 关于 $x$ 都是 $C^2\cap W^{3,\infty}$，且保留
(1.2) 的一致正下界，则 §§2–7 的结论仍成立；(6.1) 的径向积分
及相关 sup 按弱导数与本质上界计算。事实上 $m\in
C^2\cap W^{3,\infty}$，$\mathcal F$ 径向 Lipschitz，真实角 ODE
与 (5.6) 给 $h_\sigma\in C^1\cap W^{2,\infty}$。所以
$p^{\rm app}$ 连续且径向绝对连续，(5.9) 在分布意义与几乎处处
都成立，其右端为普通 $L^\infty_x$ 源，没有 knot 上的 delta。
(2.4) 只用较低径向导数，其能量证明与近似极限照旧成立。
因此分段 quintic、全局 C4 的真实 $F$ 所形成的系数，在所有
分母正下界及上述实际导数界已付时，可沿真实材料 $r$ 穿过有限
个 knot；不必为了严格区这一项把全局样条改为径向 $C^\infty$。

root collar 的高 jet 则可另作局部支付：若 R37 的固定材料 root
已严格落在一个多项式 knot span 内部，且到两端 knot 有正距离，
便可把 R39/R47 的整个小 collar 留在该 span 中。该处有限 Fourier
样条及分母不为零的真实几何系数有任意所需有限径向 jet；若要
复角域，仍须验证相同分母在所用域内不为零及实际坐标有正域宽。
这是一项可验证的局部条件，不是由浮点 root 位置直接授予。

在全部相应加权界确实存在时，§6 的证明按实际有界复合逐项继续
成立；两次 R41 复合若各花 $\varepsilon$ 个 Sobolev 导数，R43 的
$4/3$ 阶余项在 $\varepsilon<1/6$ 时仍保留严格大于一阶的增益。
有限低频、均值、刚体/持握约束与 R37 的真实 residual 因子都应
继续进入原全域 Newton 接口。

本篇自证有限 WKB 与通量计算；Cauchy 的框架对应
[R32](R32-exact-darboux-and-full-scattering-interface.md) §§8–9，
root 的准确 Ai 定义与全轴界对应
[R39](R39-finite-component-airy-transfer-input.md)，
真实首 Dyson 项对应
[R43](R43-first-airy-phase-and-four-thirds-remainder.md)，
正侧完整 source/contact 及 Cayley 对应
[R45](R45-positive-interior-gain-and-full-source-contact.md)。
这些引用是本题实际接口，均未把当前候选尚欠的输入当成已付。
