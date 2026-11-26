# R615：实际位置奇频的连续角证书及有限原函数误差

2026-11-27，Astra-new-mechanism-1f4a61a4-20261127。**已证明：在下述准确输入界下，将同一有限角重构的真实奇频读数、有限原函数的alias、离散加权均值、turning根误差传到连续实际metric的显式上界。** 没有执行科学计算或认证当前浮点ODE、径向采样及reach。

本稿续[R606](R606-weighted-fourier-majorants-continuous-turning-and-metric.md)和[R613](R613-actual-position-defect-jacobian-and-complete-objective.md)。R606先用Darboux残差的全非零频率绝对值和，再用原函数的统一L∞范数传到位置。以下直接在同一个实际复位置缺陷上取奇频，保留两次角原函数已经获得的实际衰减；不是把有限FFT尾差当连续尾。

## 1. 准确对象与可消费的输入

固定 $r>0$，采用R613的正图和内点C4条件及同一高度，角对称性为偶、π周期。记同R606
$$
u(e)^2=e-s(\theta),\quad E(e)=W^2+e,
\quad M>0,\quad G(e)=A_t(e)/M,
$$
$$
a(e)=N/u(e),\quad w(e)=N/u(e)^3,
\quad \mu(e)=\langle w(e)G(e)\rangle/\langle w(e)\rangle,
\quad \mathcal R(e)=w(e)(G(e)-\mu(e)).                     \tag{1}
$$
$N,b,M,s,W$在本节改变 $e$ 时固定。$G$对 $e$准确仿射，$G_e$由R606给出。记
$$
\|f\|_\rho=\sum_{n\in\mathbb Z}|\widehat f_n|e^{|n|\rho},
\qquad \rho>0.                                            \tag{2}
$$

已知一个真实区间 $e_-\le e\le e_+$，包含有限根近似 $\widehat e$ 与准确连续turning根 $e_*$，且
$$
|e_*-\widehat e|\le d,\qquad g:=e_--s_\rho>0.
$$
在整个区间假设已支付
$$
\|s\|_\rho\le s_\rho,\quad
\|N\|_\rho\le n_\rho,\quad N\ge n_->0,
\quad \|G(e)\|_\rho\le G_\rho,
\quad \|G_e\|_\rho\le L_\rho.                            \tag{3}
$$
这些可以直接取R606的(18)至(31)所给明确系数界。另设 $x=\|Z_\theta\|_\rho^2/r^2<1$，并定义
$$
E_-=W^2+e_-,\quad
A_\rho=n_\rho g^{-1/2},\quad
\Omega_\rho=n_\rho g^{-3/2},\quad
w_-=n_-(e_++s_\rho)^{-3/2},
$$
$$
B_\rho=r\{2-\sqrt{1-x}\},\qquad
T_\rho=\exp(\rho+A_\rho/2),\qquad
R_\rho=2\Omega_\rho G_\rho,
$$
$$
Q_\rho=B_\rho T_\rho R_\rho/2,\qquad
S_\rho=Q_\rho/\sqrt{E_-}.                                 \tag{4}
$$
只有真实系数与数值误差包围支付(3)时，以下才成为实际连续证书；代入浮点重建值仍只是条件观察。

## 2. 同一实际复位置的解析范数

令 $\Pi$为零均值角原函数，定义对整个 $e$区间都成立的辅助函数
$$
\phi(e)=\Pi(a(e)-1),\qquad
\tau(e)=\exp(i[\theta+\pi/2+\phi(e)]),
$$
$$
Q(e)=i b(\Pi\mathcal R(e))\tau(e),\qquad
\mathcal S(e)=\Pi Q(e)/\sqrt{E(e)}.                       \tag{5}
$$
在 $e=e_*$ 时，R613证明 $\mathcal S=S_x+iS_y$ 是真实重构位置的归一缺陷。对中间 $e$并不宣称turning准确或该辅助函数已是另一张等距面；这里只用它比较两个根输入。

所有 $a,w,G,\mathcal R,b$为π周期，故 $\Pi$在其零均值部分上满足
$$
\|\Pi f\|_\rho\le\tfrac12\|f\|_\rho.                    \tag{6}
$$
这是直接对非零偶频乘 $1/(in)$。$\tau$与 $Q$为π反周期，所以外层 $\Pi$的范数至多1。

由二项式/Neumann级数，(3)给
$$
\|a\|_\rho\le A_\rho,\qquad
\|w\|_\rho\le\Omega_\rho,
\qquad w\ge w_->0.
$$
又因 $\sqrt{1-z}=1-\sum_{m\ge1}c_mz^m$，其中 $c_m>0$且 $\sum c_mx^m=1-\sqrt{1-x}$，
$$
\|b\|_\rho\le B_\rho.                                    \tag{7}
$$
原函数删除常数后(6)给 $\|\phi\|_\rho\le A_\rho/2$。Fourier代数中的指数级数及 $\|e^{i\theta}\|_\rho=e^\rho$于是给 $\|\tau\|_\rho\le T_\rho$。

对实 $e$，权 $w$严格正，所以 $|\mu|\le\|G\|_\infty\le G_\rho$。由(1)、乘积代数和(6)，
$$
\|\mathcal R\|_\rho\le R_\rho,\qquad
\|\Pi\mathcal R\|_\rho\le R_\rho/2,
$$
$$
\boxed{\|Q\|_\rho\le Q_\rho,\qquad
        \|\mathcal S\|_\rho\le S_\rho.}                   \tag{8}
$$
这些界对整个根区间一致，并完整包含相位的无限角频；没有将 $e^{i\phi}$截断。

## 3. 根位移的完整位置Lipschitz常数

下标 $e$表示在同一高度固定时微分。准确有
$$
a_e=-w/2,\qquad
w_e=-\frac{3w}{2u^2},\qquad
\mu_e=\frac{\langle wG_e+w_e(G-\mu)\rangle}{\langle w\rangle}.
$$
实轴上 $u^2\ge g$，所以
$$
|\mu_e|\le L_\rho+3G_\rho/g.
$$
Fourier范数下 $\|w_e\|_\rho\le3\Omega_\rho/(2g)$，因此
$$
\|\mathcal R_e\|_\rho
\le2\Omega_\rho L_\rho+6\Omega_\rho G_\rho/g,
\qquad \|\phi_e\|_\rho\le\Omega_\rho/4.                  \tag{9}
$$
用 $\tau_e=i\phi_e\tau$对(5)完整微分，再保留 $E_e=1$的归一项，得到
$$
\boxed{
\|\mathcal S_e\|_\rho\le L_{S,\rho}:=
\frac{B_\rho T_\rho}{\sqrt{E_-}}
\left(\Omega_\rho L_\rho+
\frac{3\Omega_\rho G_\rho}{g}
+\frac{\Omega_\rho^2G_\rho}{4}\right)
+\frac{S_\rho}{2E_-}.
}                                                          \tag{10}
$$
这包括变化的正权、均值、角相位以及归一度量；没有把R613的离解项省略。积分参数导数可得
$$
\|\mathcal S(e_*)-\mathcal S(\widehat e)\|_\rho
\le dL_{S,\rho}.                                          \tag{11}
$$

## 4. 原有限角原函数的独立alias引理

设 $N\ge4$且 $4\mid N$。均匀节点 $\theta_j=2\pi j/N$，$\Pi_N$为当前源码的同一有限原函数：把离散 Fourier 模 $0<|n|<N/2$乘 $1/(in)$，常数和Nyquist模取0。它等价于实矩阵
$$
(\Pi_N)_{ij}=\frac2N\sum_{k=1}^{N/2-1}
 \frac{\sin(k(\theta_i-\theta_j))}{k}.                    \tag{12}
$$
对π周期函数取 $\sigma=2$，π反周期函数取 $\sigma=1$。若 $\|f\|_\rho\le F_\rho$，则在全部节点上
$$
\boxed{
\left|\Pi_N(f|_{\rm grid})-(\Pi f)|_{\rm grid}\right|
\le P_{\sigma,N}(F_\rho):=
\left(\frac1\sigma+\frac2N\right)e^{-N\rho/2}F_\rho.
}                                                          \tag{13}
$$

**证明。** 对单个 $e^{in\theta}$，当 $|n|<N/2$时，两个原函数在网格上完全一致。对 $|n|\ge N/2$，令 $n_0$为其离散别名，若不为常数或Nyquist，系数误差绝对值至多
$$
|1/n_0-1/n|\le1/\sigma+2/N.
$$
因为 $4\mid N$，偶频或奇频的别名保持同样奇偶性，非零最小绝对频率分别为2或1。若别名是被删常数或Nyquist，只剩 $1/|n|\le2/N$。对全部高频求和，(2)给(13)。绝对收敛使逐项求和合法。

对任意节点误差向量而不假设解析性，直接复用[R504 §5.1](R504-complete-168-parameter-line-second-metric-jets-and-curvature-PSD-remainders.md)对同一实FFT、Nyquist置零矩阵已证的范数，取
$$
\boxed{
\|\Pi_N v\|_{\ell^\infty}
\le K_N\|v\|_{\ell^\infty},\qquad
K_N:=\frac{\pi}{\sqrt3}.
}                                                          \tag{14}
$$
R504由离散Parseval和每行Cauchy–Schwarz得到更精确的行和界 $C_N\le(2\sum_{k=1}^{N/2-1}k^{-2})^{1/2}\le K_N$；此处不重证旧结论。向量Euclidean范数或复数模同样受该行和控制。这是准确有限矩阵的范数，不是浮点矩阵、FFT或三角函数的舍入包围，也没有把它默认成连续锯齿算子。

## 5. 从同一有限重构到连续位置

本节先假设在 $\widehat e$的节点函数值全部准确；实际求值/舍入误差在下一节单独加入。令 $T_N$为均匀平均，并完全照原几何源码定义
$$
\mu_N=\frac{T_N(wG)}{T_Nw},\qquad
R_N=w|_{\rm grid}(G|_{\rm grid}-\mu_N),
$$
$$
\phi_N=\Pi_N(a|_{\rm grid}-1),\quad
\tau_N=e^{i(\theta+\pi/2+\phi_N)},
$$
$$
Q_N=i b|_{\rm grid}(\Pi_NR_N)\tau_N,\qquad
S_N=\Pi_NQ_N/\sqrt{E(\widehat e)}.                       \tag{15}
$$
因为 $T_Nw\ge w_-$，R606的平均alias界给
$$
|\mu_N-\mu|\le
\epsilon_\mu:=2e^{-N\rho}\Omega_\rho G_\rho/w_-.
$$
于是节点上 $|R_N-\mathcal R|\le\Omega_\rho\epsilon_\mu$。定义
$$
\epsilon_\phi=P_{2,N}(A_\rho),\qquad
\epsilon_p=P_{2,N}(R_\rho)+K_N\Omega_\rho\epsilon_\mu.
                                                               \tag{16}
$$
由(13)(14)即
$$
|\phi_N-\phi|\le\epsilon_\phi,\qquad
|\Pi_NR_N-\Pi\mathcal R|\le\epsilon_p.
$$
实轴上 $\phi_N,\phi$都实，故 $|\tau_N-\tau|\le\epsilon_\phi$，且 $|\tau_N|=1$。用 $b\le r$以及 $|\Pi\mathcal R|\le R_\rho/2$，从
$$
Q_N-Q=i b[(\Pi_NR_N-\Pi\mathcal R)\tau_N
+(\Pi\mathcal R)(\tau_N-\tau)]
$$
得到 $|Q_N-Q|\le r(\epsilon_p+(R_\rho/2)\epsilon_\phi)$，没有遗漏额外乘积项。再用外层反周期原函数的(13)和(14)，得到
$$
\boxed{
|S_N-\mathcal S(\widehat e)|_{\rm grid}
\le\epsilon_S:=\frac{
P_{1,N}(Q_\rho)+K_Nr[\epsilon_p+(R_\rho/2)\epsilon_\phi]
}{\sqrt{E_-}}.
}                                                          \tag{17}
$$
这里明确支付了离散加权均值和两次有限原函数；不能只给最终FFT系数的alias而忽略形成该系数时已经做过的两个有限原函数。

## 6. 有限奇频读数到真实metric

取正奇整数 $K<N/2$，并记 $\mathcal O_K=\{1,3,\ldots,K\}$。从同一个数值 $S_N$求
$$
\widetilde c_k=2T_N(\operatorname{Re}S_N\cos k\theta),\qquad
\widetilde s_k=2T_N(\operatorname{Im}S_N\sin k\theta).
$$
计算出的两值分别记为 $\widehat c_k,\widehat s_k$。设已支付实际函数求值、矩阵、三角函数、求和及舍入造成的误差
$$
|\widehat c_k-\widetilde c_k|\le e_{k,x},\qquad
|\widehat s_k-\widetilde s_k|\le e_{k,y}.                   \tag{18}
$$
这些是相对于(15)准确有限代数对象的误差；ODE/高度系数的不确定性必须先进入(3)及实际点值的包围，不能省略。

定义
$$
\beta_k=2\epsilon_S+S_\rho e^{-(N-k)\rho}
+dL_{S,\rho}e^{-k\rho}.                                  \tag{19}
$$
则真实连续 $\mathcal S(e_*)=S_x+iS_y$的奇频系数满足
$$
|c_k|\le|\widehat c_k|+e_{k,x}+\beta_k,\qquad
|s_k|\le|\widehat s_k|+e_{k,y}+\beta_k.                    \tag{20}
$$
证明依次使用：(17)给有限投影误差至多 $2\epsilon_S$；R606的非Nyquist系数alias给 $S_\rho e^{-(N-k)\rho}$；(11)与Fourier系数的指数权给根位移 $dL_{S,\rho}e^{-k\rho}$。实部和虚部的Fourier范数均不超过复函数范数，正弦与余弦alias证明相同。

由R613的奇偶性，连续位置缺陷写成
$$
\mathcal S(\theta)=\sum_{k\ge1,\ k\ {\rm odd}}
 [c_k\cos k\theta+i s_k\sin k\theta].
$$
单个频率有
$$
\sup_\theta|c_k\cos k\theta+i s_k\sin k\theta|
=\max\{|c_k|,|s_k|\}.
$$
而复Fourier系数分别为 $(c_k+s_k)/2$和 $(c_k-s_k)/2$，所以
$$
\|\mathcal S\|_\rho
=\sum_{k\ge1,\ k\ {\rm odd}}
\max\{|c_k|,|s_k|\}e^{k\rho}.                            \tag{21}
$$
这个准确身份避免把两个位置分量的高频尾再多付一个2或 $\sqrt2$。

于是一个直接可计算的完整连续角位置预算为
$$
\boxed{
\Delta_S=
\sum_{k\in\mathcal O_K}
\left[\max\{|\widehat c_k|+e_{k,x},
             |\widehat s_k|+e_{k,y}\}+\beta_k\right]
+S_\rho e^{-(K+2)\rho}.
}                                                          \tag{22}
$$
由(8)(20)(21)及下一个遗漏奇频是 $K+2$，
$$
\|\mathcal S(e_*)\|_\infty\le\Delta_S,
\qquad
\boxed{\eta_{\rm actual}\le
 (1+\sqrt2)\Delta_S+\Delta_S^2.}                          \tag{23}
$$
它是同一连续turning根、同一连续重构位置的metric界；两个原函数的作用由实测位置奇频保留下来。有限优化目标的下降并非(23)所需输入，全部低频实际剩余及数值误差明确保留。

## 7. 范围与当前消费方式

(23)首先对固定 $r$成立。要覆盖正文径向区间，必须逐小区间包围真实径向系数、两jets及(3)(18)，并在同一个区间内保根窗口和正性；一张半径网即使全部通过也不是连续覆盖。

当前R606原收据的保守界主要由低频Darboux系数绝对值和支配，而原实际位置误差约小两个数量级。(22)提供直接利用真正位置读数的方式，并说明必须补入哪些有限原函数误差。本文没有用那些旧数值替(3)(18)认证新界，也不因已有同场几何而免费取得完整新奇频读数。

下一真正科学范围可在已经必须计算的同一末fine重构中，读取 $S_N$的完整所需奇频并复用R606已计算的系数界。新观察须明确计入实际scope；当前已发compactrun不因本文被改写。若充分界在某处失败，只表示本条包络尚不够强，不能排除原几何机制。

本条不支付有限DtN与外传误差、全平内尾和核心端的连续拼合、固定最终度量收敛、全时间单射或reach；这些仍须在真实候选上共同完成。
