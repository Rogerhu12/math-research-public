# R76：真实全尾 Robin 的角权与保留物理均值行的正域逆

## 0. 已付范围与实际对象

本篇在 [R74](R74-actual-full-tail-robin-and-augmented-positive-cap.md)
已构造的同一实际闭近似背景上，支付完整有限正域加真实无限尾的
**同宽角向加权 Poisson、普通源与 contact**。角权为
\[
 W_s(n)=e^{s|n|},\qquad\hbox{或}\qquad
 W_s(n)=e^{s\omega_{\log}(|n|)},\quad
 \omega_{\log}(t)=\log(e+t)^{3/2}-1.
 \tag{76.1}
\]
本次实际充分界是
\[
 \boxed{|s|\le 2^{-100}.} \tag{76.2}
\]
它使用真实剪切角 \(\varphi\)，不是未经转换的原物理角数据。
regular 端的真实角图、边界密度与物理平均值约束全部保留。

参数域仍是 [R69](R69-actual-closed-approximate-exterior-and-two-held-disks.md)
和 R74 的准确仿射区间
\[
 \delta\in\delta_4+[-1/2000000,1/2000000],\qquad
 \delta_4=-7789866024620307/4611686018427387904.
 \tag{76.3}
\]
每个固定参数使用 R74 的真实全频双 bump 选择；下面常数逐点一致。
这里没有证明该选择随参数连续，也没有把它升级成完整非线性族。
本篇只支付能量空间及其完整 trace/contact 尺度；任意更高 Sobolev
窗口、参数 tame 差量与中央混合型反馈逆仍需单独完成。

数值部分由
[实际有向证书源](../scripts/fourfold_phase_weighted_exterior_robin.py)
和
[256-bit 完整报告](../notes/2026-11-12-actual-weighted-exterior-robin-certificate.json)
逐项计算。它们核对 R69/R74 完整报告的 SHA 与准确参数域，不从
有限角采样推断下面的复域或全频性质。

## 1. 空间、真实边界形式与已知实际常数

令 \(x=r-t(\delta)\in[0,L]\)，\(L<25/8\)，取 R69 的真实剪切角。
使用全 \(2\pi\) 物理角圆，再限制到 \(4\mathbb Z\) 不变子空间。
定义
\[
 \|v\|_{\mathcal V}^2
 =\int_0^L\int_{S^1}
       (|v|^2+|v_x|^2+x|v_\varphi|^2)\,d\varphi\,dx.
 \tag{76.4}
\]
两端 trace 空间为 \(H^{1/3}\oplus H^{1/2}\)，平方 trace 常数
\(C_t<37.710\)，Fourier 对角延拓平方常数 \(C_e<2.321\)。
这些常数包含完整零模和两端 cross。

设 regular 端真实角图是 \(\theta=H(\varphi)\)，
\(J=H'>0\)，\(\phi_0=(2\pi)^{-1/2}\)。令
\[
 C_Hf=f\circ H^{-1},\qquad
 \ell(v)=\langle Jv(L,\cdot),\phi_0\rangle_{L^2(d\varphi)}.
 \tag{76.5}
\]
因此 \(\ell(v)\) 正是 regular 端**物理角平均 Fourier 系数**。
真实全尾算子在非零 \(4\mathbb Z\) 模上的乘子为 \(\gamma_m\)，
R74 已证明 \(m/7<\gamma_m<m/5\)。为书写半正形式，把其常数乘子
定义为零；真实尾的平均高度及剩余平均通量仍另行施加。

完整形式是
\[
 \mathfrak b(v,w)=\int \nabla_0v\cdot C\overline{\nabla_0w}
 +\langle\Gamma_{\rm ext}C_Hv(L),C_Hw(L)\rangle_{L^2(d\theta)},
 \quad\nabla_0=(\partial_x,\sqrt{x}\partial_\varphi).
 \tag{76.6}
\]
这里 \(m_+I<C<M_+I\)，\(m_+>0.005804\)，\(M_+<146.966\)。
在闭子空间
\[
 X=\{v\in\mathcal V:v(0)=0,\ \ell(v)=0\}
 \tag{76.7}
\]
上，R74 的真实逆与全形式 norm 满足
\[
 g\le(1+L^2/2)/m_+<2^{10},\qquad
 M_*\le M_++(J_*/5)C_t<180,
 \quad J_*<4.137.
 \tag{76.8}
\]

后续 Fourier 角权不保持 (76.7) 的物理平均约束，故不能直接在
\(X\) 上套用一个没有运输约束的加权 Neumann 论证。第 7 节会
准确运输 trial 与 test 两个空间。

## 2. 当前真实角流的改进复域与 Jacobian 扇形

R69 全部 1423 个正域 cell 供应物理角带
\(\sigma_0=1/512\)，以及真实剪切速度 \(b\) 的积分上界
\[
 I_r=\int\sup_{\theta\in\mathbb R}|b_\theta|\,dr
 <1.419749401109,
 \qquad
 I_c=\int\sup_{|\Im\theta|\le\sigma_0}|b_\theta|\,dr
 <7.157688228407.
 \tag{76.9}
\]
报告中的未取整有向端点用于所有计算。

### 2.1 真实流的首次出管估计

若某个真实径向位置上 \(M_r,M_c\) 分别控制上述两个 norm，
Cauchy 公式及沿竖线积分给
\[
 |b_\theta(\theta+iy)|
 \le M_r+\frac{|y|}{\sigma_0-|y|}M_c,
 \qquad
 |\Im b_\theta(\theta+iy)|
 \le\frac{|y|}{\sigma_0-|y|}M_c.
 \tag{76.10}
\]
这里用到了 \(b_\theta\) 在实轴取实值。令
\[
 s_0=\sigma_0/20,
 \quad J_f=e^{I_r+I_c/19},
 \quad \rho=\frac{s_0}{2J_f}.
 \tag{76.11}
\]
在假设 \(|\Im\Theta|\le s_0\) 的首次出管区间上，真实方程
\(\Theta_r=b(r,\Theta)\) 和 (76.10) 给
\(|\Im\Theta|\le J_f|\Im\varphi|\le s_0/2\)。因此整条流均在
\(s_0/2\) 内，而不是只在径向节点上成立。

对 \(J(r,\varphi)=\Theta_\varphi\) 用真实方程
\(J_r=b_\theta(r,\Theta)J\)，初值 \(J=1\)。置
\[
 M=e^{I_r+I_c/39},\qquad \alpha=I_c/39<1/5.
 \tag{76.12}
\]
于是对整条流、全部 \(|\Im\varphi|\le\rho\)，
\[
 |J|,|1/J|\le M,\qquad
 |\arg J|\le\alpha,
 \quad \Re J\ge\mu:=\frac{49}{50M},
 \quad \frac{|\Im J|}{\Re J}\le\frac{10}{49}<\frac14.
 \tag{76.13}
\]
证明最后两式只需 \(\cos(1/5)\ge49/50\) 和
\(\sin(1/5)\le1/5\)。此处 \(1/J\) 指真实 Jacobian 的倒数；
不需要免费假设一个同宽复逆角图。

所有实际系数只把 \(r\) 当作时间。有限径向样条分段在端点连续，
每段角变量的 holomorphic norm 已有统一积分上界，故分段 ODE 的
真实复流与其 Jacobian 可依次连接。本论证没有进行角依赖的径向
换元，也没有从径向 \(C^4\) 猜无限 mixed-radial 解析性。

### 2.2 同一管内的实际矩阵

R69 的旧复系数界恰为
\(M_{c,\mathrm{old}}=J_{c,\mathrm{old}}M_{\mathrm{phys}}\)，其中
\(M_{\mathrm{phys}}\) 是真实 \(\alpha,\eta K_0/x\) 的全 cell 上界。
故在新管上可取
\[
 M_C=\frac{M_{c,\mathrm{old}}}{J_{c,\mathrm{old}}}M.
 \tag{76.14}
\]
证书用旧分子上端点除以旧分母下端点。真实实轴正性及 (76.8)
完全不变。实际有向安全值为
\[
 \rho>8.09977\,10^{-6},\qquad M<4.96931,\qquad \mu>0.197210.
 \tag{76.15}
\]

## 3. \(|D|\) 的正确拉回：密度是主符号消去的原因

这里所有 adjoint 都相对于显示的实测度。准确地
\[
 C_H^*=M_JC_H^{-1},\qquad B_H=C_H^*|D_\theta|C_H.
 \tag{76.16}
\]
普通相似共轭 \(C_H^{-1}|D_\theta|C_H\) 的主符号为
\(|\xi|/J\)。本篇实际边界形式 (76.6) 的双侧密度拉回才有主符号
\(|\xi|\)。这不是假定 \(H\) 保测度，也不是把它当作酉变换。

在全 \(2\pi\) 圆上直接逐 Fourier 模验证
\[
 |D|f(x)=\frac1{4\pi}\operatorname{PV}
 \int_0^{2\pi}\frac{f(x)-f(y)}{\sin^2((x-y)/2)}\,dy.
 \tag{76.17}
\]
例如 \(n>0\) 时
\(\int(1-\cos nt)\csc^2(t/2)\,dt=4\pi n\)，由有限几何级数
\(|\sum_{k=0}^{n-1}e^{ikt}|^2\) 的积分得到。
准确换元给
\[
 B_Hf(x)=\frac1{4\pi}\operatorname{PV}\int
 (f(x)-f(y))\frac{H'(x)H'(y)}
 {\sin^2((H(x)-H(y))/2)}\,dy.
 \tag{76.18}
\]
定义差核
\[
 K_H(z,w)=
 \frac{H'(z)H'(w)}{\sin^2((H(z)-H(w))/2)}
 -\frac1{\sin^2((z-w)/2)}.
 \tag{76.19}
\]
两项的二阶极点及一阶极点准确消去。其可去对角值为
\[
 K_H(z,z)=\frac23\frac{H'''(z)}{H'(z)}
 -\left(\frac{H''(z)}{H'(z)}\right)^2
 +\frac{H'(z)^2-1}{3}.
 \tag{76.20}
\]
由泰勒展开即可逐项得到这个式子；尤其没有残留一个未经控制的
角一阶微分算子。

## 4. 差核在真实共同复平移下的可计算界

下面只需要 \(z=x+\tau,w=y+\tau\)，\(x,y\) 实，
\(|\Im\tau|\le r:=\rho/2\)。没有声称两个自变量可在任意独立
复带上取值。令 \(d\in[0,\pi]\) 为 \(x-y\) 的圆周距离。
从 (76.13) 和 Cauchy 公式可取
\[
 M_2=2M/\rho\ge|H''|,\qquad
 M_3=8M/\rho^2\ge|H'''|.
 \tag{76.21}
\]

### 4.1 对角附近

当 \(d\le1/M\) 时，取短 lift 的差 \(D=H(z)-H(w)\)，
\(g=D/(z-w)\)。有 \(|D|\le1\)、\(\Re g\ge\mu\)。设
\(h_0=H'(w),h_1=H'(z)\)，梯形积分余项给
\[
 \left|g-\frac{h_0+h_1}{2}\right|\le M_3d^2/12,
 \qquad |h_1-h_0|\le M_2d,
\]
\[
 |h_0h_1-g^2|\le(M_2^2/4+MM_3/6)d^2.
 \tag{76.22}
\]
对 \(|u|\le1\)，初等正弦级数给
\[
 \csc^2(u/2)=4/u^2+R(u),\qquad |R(u)|<1.
 \tag{76.23}
\]
具体地 \(|2\sin(u/2)-u|\le(10/237)|u|^3<|u|^3/20\)，
从而余项模不超过 \(164/361<1\)。代入 (76.19) 得
\[
 K_{\rm near}=
 \frac{M_2^2+(2/3)MM_3}{\mu^2}+M^2+1.
 \tag{76.24}
\]

### 4.2 离开对角

共同平移线上的 \(\Re H'\) 严格为正，且 \(H(z+2\pi)=H(z)+2\pi\)。
选择整数 \(k\) 使 \(a=\Re(D-2\pi k)\in[-\pi,\pi]\)。沿短路或
其互补圆弧积分 (76.13)，均给
\[
 |a|\ge\mu d,\qquad |\Im D|\le|a|/4.
 \tag{76.25}
\]
若 \(|b|\le|a|/4\)，则
\[
 \Re\sin^2((a+ib)/2)=\tfrac12(1-\cos a\cosh b)\ge a^2/16.
 \tag{76.26}
\]
例如用 \(1-\cos a\ge2a^2/\pi^2\)、\(\pi^2<10\)、
\(\cosh(\pi/4)<8/5\) 即得更强的 \(3a^2/40\) 下界。
于是 \(d\ge1/M\) 时可取
\[
 K_{\rm far}=16M^4/\mu^2+10M^2,
 \qquad M_K=\max(K_{\rm near},K_{\rm far}).
 \tag{76.27}
\]
差核有界，故 (76.18) 减 (76.17) 已不需要 PV。其乘法项与积分项
各自的 \(L^2\) norm 不超过 \(M_K/2\)，总 norm 不超过 \(M_K\)。
这也证明共同平移后的差算子在 \(|\Im\tau|\le r\) 解析且有统一
operator norm；可先对每个矩阵元积分，再用上述一致 Schur 界。

## 5. 真实 Robin 的其余项：没有只保留主阶

R74 的入口记号为
\[
 A_0=4\omega+a_*^2/z_*,\quad p_*=a_*^2/z_*,\quad
 b=4\omega/A_0,\quad
 c_0=b/A_0,\quad c_1=(1-b^2)/A_0.
 \tag{76.28}
\]
稳定线的准确乘子可写成
\[
 \gamma_m^0=c_0m+c_1-c_1b/(m+b).
 \tag{76.29}
\]
\(0<b\le1\)，且本次可用实际区间常数
\[
 b\ge b_-:=4\omega_-/A_+>0,\qquad
 c_0\le(4\omega_-)^{-1},\qquad c_1\le2p_*/A_-^2.
 \tag{76.30}
\]

为估计算子，把 (76.29) 定义在所有整数 \(|m|\)，其零模恰为零；
真实尾误差只在非零 \(4\mathbb Z\) 上保留，在其他模置零。这只是
估计用的扩充。因为真实 \(H(\varphi+\pi/2)=H(\varphi)+\pi/2\)，
\(C_H\) 保持 \(4\mathbb Z\)，限制后恰为原实际算子。

### 5.1 准确 order-zero resolvent

\(R_b=(|D|+b)^{-1}\) 的核是
\[
 R_b(t)=\frac1{2\pi}\int_0^1
 q^{b-1}\frac{1-q^2}{1-2q\cos t+q^2}\,dq.
 \tag{76.31}
\]
它由 Poisson 核的 Fourier 级数积分得到。对于 (76.25) 的复差，
\[
 |1-2q\cos D+q^2|
 \ge (1-q)^2+q\mu^2d^2/4.
 \tag{76.32}
\]
把 \(q\) 积分分在 \(1/2\)。前半段由 \(8/b_-\) 控制，后半段
由 \(2\log(1+2/(\mu^2d^2))\) 控制。由于
\[
 \frac1{2\pi}\int_{-\pi}^{\pi}
       2\log(1+2/(\mu^2d^2))\,dd
 \le2\log(1+2/\mu^2)+2,
\]
真实密度拉回的共同平移 operator norm 可取
\[
 M_R=M^2\{8/b_-+2\log(1+2/\mu^2)+2\}.
 \tag{76.33}
\]
这个可积对数界也证明 (76.31) 的解析延拓没有跨过未经排除的核极点。
此外 \(C_H^*IC_H=M_J\)，共同平移 norm 至多 \(M\)。

### 5.2 全部真实无限尾误差

令 \(B=2^{24}-25/8\)。R74 已从每个真实强尾方向证明
\[
 |E_m|:=|\gamma_m-\gamma_m^0|
 \le2^{42}m e^{-2m\omega_-B},\qquad m\in4\mathbb N.
 \tag{76.34}
\]
对共同复平移有 \(|\Im(H(x+\tau)-H(y+\tau))|\le2Mr\)。因此
\[
 q_E=e^{-4(2\omega_-B-2Mr)},\qquad
 M_E=M^2\,2^{45}\frac{q_E}{(1-q_E)^2}
 \tag{76.35}
\]
控制真实 \(C_H^*EC_H\) 的算子 norm。\(2^{45}\) 含正负全部频率
及 \(m=4j\) 的真实因子，没有把归一角 \(4\theta\) 当成物理角。
报告实际验证 \(M_E<2^{-100}\)，计算时没有把它设成零。

综合以上，令 \(\Lambda=\langle D_\varphi\rangle\)，
\[
 \mathcal B=\Lambda^{-1/2}
 (C_H^*\Gamma_{\rm ext}C_H-c_0|D_\varphi|)\Lambda^{-1/2}.
 \tag{76.36}
\]
其共同复平移在宽 \(r\) 内的 norm 至多
\[
 M_B=c_{0,+}M_K+c_{1,+}(M+M_R)+M_E.
 \tag{76.37}
\]
这包含准确 rational order-zero 项、全真实尾误差和零模。

## 6. 全矩阵 Fourier lag 与同宽 signed 交换界

设一个圆上算子 \(A\) 在共同平移下解析，宽 \(h\) 内 norm 至多
\(M_A\)。其第 \(d\) 条 Fourier lag 是 operator-valued Fourier
投影，而不是逐列估计：
\[
 (A_d)_{mn}=\mathbf1_{m-n=d}A_{mn},\qquad
 \|A_d\|\le M_Ae^{-h|d|}.
 \tag{76.38}
\]
证明：对实平移，矩阵元乘 \(e^{i(m-n)\tau}\)；将投影积分移至
\(\Im\tau=\pm h\) 即得。统一 operator norm 允许求和所有 lag。

对 (76.1) 两种权，写指数函数为 \(\psi(|n|)\)。均有
\[
 |\psi(|m|)-\psi(|n|)|\le|m-n|.
 \tag{76.39}
\]
direct-log 情形由
\(\omega_{\log}'(t)=3\sqrt{\log(e+t)}/[2(e+t)]\le3/(2e)<1\)
得到；它同时递增、凹且在零点为零。于是 \(|s|\le h/2\) 时
\[
 \|W_sAW_s^{-1}-A\|
 \le |s|\,N(M_A,h),\qquad
 N(M_A,h)=\frac{2M_Ae^{-h/2}}{(1-e^{-h/2})^2}.
 \tag{76.40}
\]
这来自 \(e^{|s||d|}-1\le|s||d|e^{|s||d|}\) 后的几何级数求和。
同样证明对截断权 \(e^{s\min(\psi(|n|),N)}\) 一致成立；截断是
Lipschitz 的，未制造一个低频不连续跳跃。

对实际内部系数、边界余项及平均密度分别取
\[
 N_C=N(M_C,\rho),\qquad N_B=N(M_B,r),\qquad
 N_J=N(M,\rho).
 \tag{76.41}
\]
边界主项 \(c_0|D_\varphi|\) 与两种权准确交换。
因而完整形式在 \(\mathcal V\to\mathcal V^*\) 的加权差满足
\[
 \|\mathfrak b_s-\mathfrak b\|\le |s|N_0,
 \quad N_0=N_C+C_tN_B,
 \quad\mathfrak b_s(v,w)=\mathfrak b(W_s^{-1}v,W_sw).
 \tag{76.42}
\]
\(C_t\) 是完整 regular \(H^{1/2}\) trace 平方费，正是
(76.36) 的归一范数所需的两个 trace 因子。

## 7. 真实平均约束的双侧运输与逆

令 \(e\) 为 R36 的 regular 常数 trace 延拓：转折端为零、regular
trace 为 \(\phi_0\)，\(\|e\|_{\mathcal V}\le\sqrt{C_e}\)。
它逐径向位置角常数，所以 \(W_se=e\)。真实 degree-one 换元给
\(\ell(e)=(2\pi)^{-1}\int J=1\)。

记 \(\ell_s=\ell W_s^{-1}\)。由 (76.40) 对 \(J\phi_0\) 的作用，
\[
 \|\ell_s-\ell\|_{\mathcal V^*}
 \le |s|\sqrt{C_t}N_J.
 \tag{76.43}
\]
在 \(X\) 上定义
\[
 T_sv=v-e\ell_s(v).
 \tag{76.44}
\]
则 \(T_s\) 准确将 \(X\) 双射到转折 trace 零、\(\ell_s=0\) 的
空间。其逆是 \(z\mapsto z-e\ell(z)\)。因此
\[
 \|T_s-I\|\le |s|T_0,
 \qquad T_0=\sqrt{C_eC_t}\,N_J.
 \tag{76.45}
\]

若 \(U=W_sv\)，实际平均条件是 \(\ell_s(U)=\xi\)。另一方面，
加权弱式采用 test \(W_sw\)，故齐次 test 条件是
\(\ell_{-s}(w)=0\)。所以应在固定空间 \(X\) 上研究
\[
 \mathfrak b_s^X(v,w)=\mathfrak b_s(T_sv,T_{-s}w).
 \tag{76.46}
\]
trial/test 不能同用 \(T_s\)。当 \(|s|T_0\le1/4\) 时，
\[
 \|\mathfrak b_s^X-\mathfrak b\|
 \le |s|N_*,\qquad
 N_*=2N_0+3M_*T_0.
 \tag{76.47}
\]
事实上第一差项至多
\(|s|N_0(1+|s|T_0)^2\le2|s|N_0\)，两个运输及其乘积的费用
至多 \(M_*(2|s|T_0+|s|^2T_0^2)\le3M_*|s|T_0\)。

由 R74 的实际逆，只需
\[
 |s|\le\min\left\{\frac\rho4,\frac1{4T_0},
                          \frac1{2gN_*}\right\}
 \tag{76.48}
\]
即可得 \(\| (\mathfrak b_s^X)^{-1}\|\le2g\)。这是直接在固定
空间上的 Neumann 证明，没有假设平均约束与角权交换。

### 7.1 全源、数据与完整 contact

设转折数据为 \(a\)，regular 物理平均系数为 \(\xi\)，并记
\[
 a_s=W_sa,\qquad F_s(w)=F(W_sw).
 \tag{76.49}
\]
写 \(E=E_-(a_s)+e\xi\)。因为第一个延拓的 regular trace 为零，
而第二个角常数，有 \(\ell_s(E)=\xi\)。求
\(U=E+T_sz\)，\(z\in X\)，使用 (76.46)。置
\[
 \varepsilon_T=|s|T_0,\quad
 \delta_b=|s|N_0,\quad t_s=1+\varepsilon_T,\quad
 M_s=M_*+\delta_b.
\]
则
\[
 \|U\|_{\mathcal V}
 \le A_s\|(a_s,\xi)\|_{H^{1/3}\oplus\mathbb C}
       +B_s\|F_s\|_{\mathcal V^*},
\]
\[
 B_s=2g t_s^2,\qquad
 A_s=\sqrt{C_e}(1+B_sM_s).
 \tag{76.50}
\]
所有直和均取 Hilbert norm。用同一个完整延拓定义 contact，得到
\[
 \|(W_sp_{\rm turn},\lambda_0)\|_{H^{-1/3}\oplus\mathbb C}
 \le\sqrt{C_e}M_sA_s\|(a_s,\xi)\|
       +\sqrt{C_e}(M_sB_s+1)\|F_s\|.
 \tag{76.51}
\]
确切地，任意 test 的残差为
\[
 \mathfrak b_s(U,w)-F_s(w)
 =\langle W_sp_{\rm turn},w(0)\rangle
       +\lambda_0\,\overline{\ell_{-s}(w)}.
 \tag{76.52}
\]
对 \(E_-(h)+e\eta\) 有 \(\ell_{-s}=\eta\)，所以 (76.51)
控制的就是实际 physical mean-flux 行，不是另一条人工平均。

对正权，可先在截断权下使用上述一致估计，再由 Fourier 系数的
Fatou 性质取得真实权。也可以在权定义的 Hilbert completion 中
直接用 (76.38) 的绝对 lag 收敛定义 (76.42)。负权使用对应的
Fourier completion 与正权对偶配对；它对普通物理数据和正权解的
交集与原弱解一致。没有声称任意负解析权元素都是普通分布或可
逐点评价的函数。

### 7.2 普通源的实际尺度

在剪切及 ground-state frame 中，普通体源为
\[
 f_{\rm sh}=-JY_z\,f_{\rm phys}\circ\Theta.
 \tag{76.53}
\]
原动量先按 \(Y_zp_w-wp_{Y_z}\) 形成，再取真实对偶角换元。
regular 物理角负荷 \(d_\theta\) 拉回为
\(d_\varphi=C_H^*d_\theta=Jd_\theta\circ H\)。
因此实际加权 \(F_s\) 的充分输入是
\[
 W_sf_{\rm sh}\in L^2_xH^{-2/3}_\varphi,
 \qquad W_sd_\varphi\in H^{-1/2}_\varphi,
\]
\[
 \|F_s\|_{\mathcal V^*}
 \le2\|W_sf_{\rm sh}\|_{L^2H^{-2/3}}
       +\sqrt{C_t}\|W_sd_\varphi\|_{H^{-1/2}}.
 \tag{76.54}
\]
第一项是 R69 已付的无边界条件内部 \(H^{2/3}\) 能量增益；权和
Fourier Sobolev 乘子交换。第二项由完整 regular trace 对偶得出。
在零权时，原物理 \(L^2\) 密度转换费小于 2.034、regular
\(H^{-1/2}\) 原物理负荷到 \(\mathcal V^*\) 的费用小于16。
非零权时必须使用显示的真实拉回源，或另付原角到剪切角的宽度
转换；本篇没有把 \(C_H\) 自身宣布为同宽解析复合算子。

### 7.3 未删除的实际均值 pivot

R74 证明的实际常数转折列满足
\(\lambda_0(v_*)=-E_*\)，且 \(E_*^{-1}<2^{12}\)。该等式和
常数模的权不变，所以同一个 pivot 在本篇保留。给定余项产生的
\(\lambda_0^{\rm rem}\) 与真实尾目标 \(\eta\)，仍准确取
\[
 a_0=(\lambda_0^{\rm rem}-\eta)/E_*.
 \tag{76.55}
\]
这将平均通量写成转折平均值的一条实际关系；中央方程仍须同时
满足它。不能据此删除全局零模或有限低块。

## 8. 本次实际有向预算

源在 256 bits 下读同一 R69/R74 完整报告，首先逐项核对实际对象，
再计算 (76.11)–(76.48)。所有小差分分母使用 \(\operatorname{expm1}\)，
全部尾项保留为非零 Arb 球。得到下列安全上界：

| 已支付的实际量 | 严格安全值 |
|---|---:|
| 新剪切角带 \(\rho\) | \(>8.09977\,10^{-6}\) |
| 全流 \(|J|,|1/J|\) | \(<4.96931\) |
| \(\Re J\) | \(>0.197210\) |
| \(|D|\) 差核 \(M_K\) | \(<9.033\,10^{13}\) |
| 全 Robin 归一余项 \(M_B\) | \(<1.546\,10^{13}\) |
| 充分权预算 \((76.48)\) | \(>9.8813\,10^{-31}>2^{-100}\) |
| 选定权处 Neumann 比率 \(g|s|N_*\) | \(<0.399168\) |
| 完整 weighted Poisson \(A_s\) | \(<483116\) |
| 原均值 pivot 的逆 | \(<2056.883\) |

从未取整数值，可统一使用简洁的结论
\[
 \boxed{
 \|W_sv\|_{\mathcal V}
 \le2^{21}\|(W_sa,\xi)\|_{H^{1/3}\oplus\mathbb C}
       +2^{12}\|F_s\|_{\mathcal V^*}.}
 \tag{76.56}
\]
\[
 \boxed{
 \|(W_sp_{\rm turn},\lambda_0)\|_{H^{-1/3}\oplus\mathbb C}
 \le2^{30}\|(W_sa,\xi)\|_{H^{1/3}\oplus\mathbb C}
       +2^{21}\|F_s\|_{\mathcal V^*}.}
 \tag{76.57}
\]
对 (76.1) 两种角权、两种符号、全部 \(|s|\le2^{-100}\)，以及
(76.3) 中每个固定准确参数，均为同一个真实外部几何和允许尾线
的估计。负帽由实际腰反射给出同一界；并未拆掉其 mean 或 source。

可重放命令：

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/fourfold_phase_weighted_exterior_robin.py \
  --out /workspace/scratch/f6a2c7886477/weighted-exterior-robin-replay.json
```

本篇已将 R74 的无权外部接口变为真实同宽角权接口。仍未支付的是
中央混合型完整反馈的有限低块、所选远端 bump 的参数正则性、全局
非线性收敛，以及同一闭背景的最终 reach 与 5% 可见幅度。这里的
正宽与完整源估计是它们可以使用的已证输入，不是这些剩余结论。
