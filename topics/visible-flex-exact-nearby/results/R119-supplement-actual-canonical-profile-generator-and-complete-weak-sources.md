# R119 续篇：真实 profile 变分的完整 Hamiltonian 核、两 mean 与 weak 源

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 在第53–60束同一个真实非零标签背景上，本篇将
compact log-profile 方向写成原物理 height/total-flux 的完整变分。
一个准确的局部剪切消去方向的径向导数；剩下的直接生成算子只含
两个角导数，其系数不含 $Q_t$、$Q_{tt}$，甚至不含 $Q$。
它的二次型在径向原点准确等于第56束的真实 Wronskian 核。
实际背景响应、两个自由 mean、全部 angular modes、ordinary/weak
源和两个 bare-flux 端荷均保留。

这给出可在实际短支集上比较的完整算子。这里没有把下述二阶强变分
直接称为同阶 norm 的 $D_\psi E$，也没有将一个径向 rank-one
控制替代非径向多频簇的正定控制。

## 1. 当前对象及完整物理两迹

用[真实通量规范](R119-supplement-actual-compact-profile-flux-gauge-and-principal-port-derivative.md)
的 $p,k,w,E,K,T,J,D,f,F_1,V$。本篇的 $t=\log r$，所以
$$
 r_t=r,\qquad w_t=-Qw,\qquad
 (p,k)_t=\mathcal U-QF_1,\qquad
 \mathcal U=\left(k_\theta-p,{E(k_\theta-p)^2\over J}\right).
 \tag{J.1}
$$
这里 $Q=-A_\Gamma$，$J=w+k+Ep_\theta$ 是**有量纲**的原分母。
对 profile 控制向量场和真实 Jacobi 系数，记
$$
 \mathcal B=w\partial_w+f\partial_k,\quad
 d={E(k_\theta-p)\over J},\quad
 v_*={w\sqrt D\over J},\quad
 \mu={J\over rD^{3/2}},\quad
 a=\mu^{-1},\quad c=\mu v_*^2={w^2\over rJ\sqrt D}.
 \tag{J.2}
$$
本篇 $a$ 只表示逆密度，不是坡长。所有系数均为当前实际背景的
系数；参考径向量在下文加下标0。

原 raw Jacobi 矩阵为
$$
 G=\mu\begin{pmatrix}1&-d\\-d&d^2-Qv_*^2\end{pmatrix}.
$$
给定普通源 $g$ 和 weak 向量源 $(F^t,F^\theta)$，采用约定
$$
 \operatorname{div}(G\nabla h)
       =g-\partial_tF^t-\partial_\theta F^\theta,
 \qquad \pi=\mu(h_t-dh_\theta)+F^t .
$$
准确的一阶系统是
$$
 Y_t=\mathsf A Y+s,\quad Y=(h,\pi),\qquad
 \mathsf A=
 \begin{pmatrix}d\partial_\theta&a\\Q L_c&\partial_\theta M_d\end{pmatrix},
 \quad L_c=\partial_\theta M_c\partial_\theta,
 \tag{J.3}
$$
$$
 s=\binom{-aF^t}{g-\partial_\theta(F^\theta+dF^t)} .
 \tag{J.4}
$$
$M_b$ 表示乘以 $b$；如 $L_cM_a$，其作用次序不得交换。
式 (J.3) 只用 $F^t$，没有要求 $F^t_t$ 存在。

对全部周期数据，
$$
 (\pi_0)_t=g_0,\qquad
 (h_0)_t=\langle dh_\theta+a\pi-aF^t\rangle.
 \tag{J.5}
$$
因此两个 mean 是独立的状态坐标。非径向时第二行不是一个径向
电阻式，不能将其中非 mean 乘积删去。

## 2. 一个保留两 mean 的准确局部剪切

对固定物理 $r$、固定当前 $\Gamma$ 的方向
$\dot{\log p_*}=\psi$，有 $\dot Q=-\psi_t$。
令实际背景响应为
$$
 \widehat z=(\dot p,\dot k)-\psi F_1.
$$
对任意背景系数 $b=b(r,w,p,k,p_\theta,k_\theta)$，准确分解为
$$
 \dot b=\widehat b+\psi\mathcal Bb,\qquad
 \widehat b=D_{(p,k)}b[\widehat z].
 \tag{J.6}
$$
下列两个恒等式在整个真实小球成立：
$$
 \boxed{\quad \mathcal Ba=af_k,\qquad
 (\mathcal U-d\partial_\theta)c+c d_\theta=-{cd^2\over E}.\quad}
 \tag{J.7}
$$
第一式的证明是
$$
 {\mathcal B\mu\over\mu}
 ={\mathcal BJ\over J}-{3\mathcal BD\over2D}
 ={w^2(T-Ep_\theta^2)\over J^2}=-f_k.
$$
第二式中 $r,w$ 在 $\mathcal U$ 作用时固定。直接有
$$
 \mathcal UD-dD_\theta=0,\qquad
 \mathcal UJ-dJ_\theta=Jd_\theta+{E(k_\theta-p)^2\over J}.
$$
代入 $\log c=2\log w-\log r-\log J-\frac12\log D$ 即得 (J.7)。
用 (J.1) 还得到
$$
 c_t+Q\mathcal Bc+c d_\theta-dc_\theta
                         =-c(1+d^2/E).                 \tag{J.8}
$$
其中的 $-c$ 是真实 $r_t=r$ 的贡献，不能遗漏。

定义整个物理 height/flux 空间上的剪切
$$
 \mathsf B=\begin{pmatrix}0&0\\-L_c&0\end{pmatrix},
 \qquad \widehat{\dot Y}=\dot Y-\psi\mathsf BY.
 \tag{J.9}
$$
它保持高度，通量修正为 $-\psi\partial_\theta(ch_\theta)$，所以
两个 mean 均不变。$\mathsf B^2=0$；在光滑数据上它是准确的
Hamiltonian 剪切，不是一个删除高模的近似。

## 3. 完整混合算子：无方向径向导数

定义实际背景响应算子
$$
 \widehat{\mathsf A}=
 \begin{pmatrix}
 \widehat d\,\partial_\theta&\widehat a\\
 QL_{\widehat c}&\partial_\theta M_{\widehat d}
 \end{pmatrix},\qquad b_d=\mathcal Bd.
$$
则完整变分准确满足
$$
 \boxed{\quad
 (\widehat{\dot Y})_t
 =\mathsf A\widehat{\dot Y}
       +(\widehat{\mathsf A}+\psi\mathsf R)Y
       +\widehat s_\psi ,\quad}
 \tag{J.10}
$$
其中
$$
 \boxed{\quad
 \mathsf R=
 \begin{pmatrix}
 M_{b_d}\partial_\theta-M_aL_c&M_{af_k}\\
 -L_{c(1+d^2/E)}&\partial_\theta M_{b_d}+L_cM_a
 \end{pmatrix},\qquad
 \widehat s_\psi=\dot s-\psi\mathsf Bs .\quad}
 \tag{J.11}
$$
特别 $\mathsf R$ 不含 $Q,Q_t,Q_{tt}$，不含 $\psi_t$ 或更高的
方向径向导数。它至多为二阶角微分算子。

**证明。** 从 (J.3) 微分并代入 (J.9)，齐次系数为
$$
 \dot{\mathsf A}-\psi_t\mathsf B
            -\psi\mathsf B_t+\psi[\mathsf A,\mathsf B].
$$
$\dot Q=-\psi_t$ 使第一项中的全部 $\psi_t\mathsf B$ 准确消去。
按 (J.6) 分离 $\widehat{\mathsf A}$ 后，所剩的直接部分是
$\psi(\mathcal B\mathsf A-\mathsf B_t+[\mathsf A,\mathsf B])$，
这里 $\mathcal B\mathsf A$ 不对 $Q$ 再求导。
完整 commutator 的四块依次为
$$
 -M_aL_c,\quad0,\quad
 L_{cd_\theta-dc_\theta},\quad L_cM_a .
$$
下左块原本的三阶角项相消，而没有交换乘法与角微分。
再用 (J.7)、(J.8)，得到 (J.11)。非齐次项就是
$\dot s-\psi\mathsf Bs$。证明完毕。

对端点在支集之外的真实全频 Cauchy 算子 $C(t,s)$，
$\psi$ 在两端为0，故其准确强导数为
$$
 \dot C(t_R,t_L)=
 \int_{t_L}^{t_R}C(t_R,t)
       (\widehat{\mathsf A}(t)+\psi(t)\mathsf R(t))
                          C(t,t_L)\,dt .                \tag{J.12}
$$
这是先在光滑数据、再在所付 Sobolev 窗之间的强恒等式。
$\mathsf R$ 的二阶阶数仍在；不能据此声称裸角 pullback 已按同阶
operator norm 可微。两端 physical density/shear 恢复及其导数仍按
第59束 (C.28)–(C.32) 的真实次序消费。

## 4. 完整 Hamiltonian 二次型及与原 Wr 核的准确识别

令
$$
 \mathsf J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 \Omega(Y,Z)=\langle Y,\mathsf JZ\rangle_{L^2_\theta}.
$$
$\mathsf A^*\mathsf J+\mathsf J\mathsf A=0$。
式 (J.11) 的右下块准确等于左上块的负伴随，两个非对角块自伴，
所以 $\mathsf R$ 也 Hamiltonian，完整角 mean 不例外。

对复数据，用实值 Hermitian 二次型记
$$
 \begin{split}
 \mathcal K_{\rm act}(Y)
 :=\langle Y,\mathsf J\mathsf RY\rangle
 ={}&\langle c(1+d^2/E)|h_\theta|^2-af_k|\pi|^2\rangle\\
 &-2\operatorname{Re}\langle\overline\pi\,b_dh_\theta
                 +c\overline{h_\theta}(a\pi)_\theta\rangle,
 \end{split}                                               \tag{J.13}
$$
$$
 \mathcal H_{\widehat z}(Y)
 :=\langle Y,-\mathsf J\widehat{\mathsf A}Y\rangle
 =\langle Q\widehat c|h_\theta|^2+\widehat a|\pi|^2\rangle
       +2\operatorname{Re}\langle\overline\pi\,\widehat d h_\theta\rangle.
 \tag{J.14}
$$
因此任何真实齐次解都满足
$$
 \boxed{\quad
 [\Omega(Y,\dot Y)]_{t_L}^{t_R}
 =\int_{t_L}^{t_R}
       \{\psi\mathcal K_{\rm act}(Y)-\mathcal H_{\widehat z}(Y)\}\,dt .
 \quad}                                                     \tag{J.15}
$$
不同两解的完整 pairing 由极化得到。实际 scattering 的输入端归一
与当前 physical 端图必须一起使用；(J.15) 没有预先将它们设为参考值。

在径向原点，$d=b_d=0$、$f_k=-1$、$a=1/\mu_0$、$c=\mu_0=w/r$。
对任意单个非零 Fourier 模 $M=|m|$，$\pi=\mu_0h_t$，所以
$$
 \boxed{\quad
 \mathcal K_0(Y)=\mu_0\bigl(|h_t|^2
                   -2M^2\operatorname{Re}(\overline h h_t)+M^2|h|^2\bigr).
 \quad}                                                     \tag{J.16}
$$
这就是第56束的完整控制核，包含真实密度和两迹；没有只匹配主符号。
对 mean，准确为 $|\pi_0|^2/\mu_0$。常高度的零列源于原 height
平移不变性，而不是从状态空间删去该 mean。

## 5. 同物理截面上的真实小差：不比较裸 pullback

设 $n=w^{-1}(\|p\|_{\mathcal A_2^2}+\|k\|_{\mathcal A_2^2})<2^{-32}$。
在同一物理截面取
$$
 u=\sqrt{\mu_0}h,\qquad v=\pi/\sqrt{\mu_0},\qquad
 \mathcal E_1=\|u_\theta\|_2^2+\|v_\theta\|_2^2+\|v\|_2^2,
 \quad\mathcal E_0=\|u_\theta\|_2^2+\|v\|_2^2 .
$$
完整有理系数及其第一个角导给
$$
 \|a\mu_0-1\|_{\mathcal A_1^1},\
 \|c/\mu_0-1\|_{\mathcal A_1^1},\
 \|f_k+1\|_{\mathcal A_1^1}<2^{10}n,
 \qquad\|b_d\|_{\mathcal A_1}<2^{10}n .
 \tag{J.17}
$$
例如 $a\mu_0=D^{3/2}/(J/w)$，$c/\mu_0=(J/w)^{-1}D^{-1/2}$；
$|(J-w)/w|\le3n$、$|D-1|\le3n$，逆及平方根在半径1/8内
的绝对幂级数给各自与其一阶角导的费用小于 $2^8n$。
$f_k=w^2(Ep_\theta^2-T)/J^2$ 用同一分母即可。
$b_d$ 用第59束 (C.24) 的完整表达式，再用宽2到1支付一个角导。
常数 $2^{10}$ 留足各分量求和余量。

将 (J.13) 准确改写为
$$
 \begin{split}
 \mathcal K_{\rm act}
 ={}&\langle C(1+d^2/E)|u_\theta|^2-Af_k|v|^2\rangle\\
 &-2\operatorname{Re}\langle\overline v b_du_\theta
                   +C\overline{u_\theta}(Av)_\theta\rangle,
 \qquad A=a\mu_0,\ C=c/\mu_0,
 \end{split}
$$
得到完整物理二次型比较
$$
 |\mathcal K_{\rm act}(Y)-\mathcal K_0(Y)|<2^{16}n\mathcal E_1.
 \tag{J.18}
$$
此处两个型作用在**同一个真实 $Y$**；没有将真实解偷换成参考解。
同样令
$\widehat n=w^{-1}(\|\widehat p\|_{\mathcal A_2^2}
                  +\|\widehat k\|_{\mathcal A_2^2})$，
完整商法则给
$$
 |\mathcal H_{\widehat z}(Y)|
                  <2^{16}(1+Q)\widehat n\mathcal E_0.    \tag{J.19}
$$
这真正消费第60束 (L.2) 的 gauged 两分量求和范数，未加回
$\psi F_1$ 的 $\rho^4$ 项。

对当前支集 $dt=a_{\rm ramp}dx$，$\int|\psi|dt\le2a_{\rm ramp}\rho^5$。
所以在一个完整 strict 分量内，(J.18) 的直接误差不超过
$2^{17}a_{\rm ramp}n_I\rho^5\sup\mathcal E_1$；
(J.19) 的响应误差不超过
$2^{20}(j+4)\widehat n_I\sup\mathcal E_0$。
后者使用已付真实 $\int(1+Q)dt<16(j+4)$。
再代第60束 (L.2) 才得到对应的 $\rho^5$ 费用。
若两个分量跨相邻胞元，$n_I,\widehat n_I$ 使用实际相交胞元的和。

这里仍须在真实 Cauchy 解上控制 $\mathcal E_0,\mathcal E_1$。
对输入频带作 $M$ 费用时，完整输出不是被投影回该频带；
实际传播和所有 mean 输出需另行保留。

## 6. 完整梯度混合式及一个有用的定量强源门

为把本核与第60束的背景响应接在同一状态上，再给等价的梯度式。
用材料坐标 $y=\sqrt{12}t$，记
$F=V+\lambda F_1$、$\lambda=-Q/\sqrt{12}$。
任意完整 Jacobi 梯度方向 $u=D_z z[\xi]$ 满足 $u_y=D_zF\,u$。
它不被限制为 $DM[u]=0$。定义
$$
 \widehat{\dot u}=\dot u-\psi D_zF_1u .
$$
对第59束准确背景方程 (C.6) 微分，得到
$$
 (\widehat{\dot u})_y=D_zF\,\widehat{\dot u}
 +\{D_z^2F[\widehat z,\cdot]+\psi D_z\mathcal R\}u .
 \tag{J.20}
$$
这包括 $D_z^2F[\widehat z,u]$，不能只求冻结背景的 profile 导数。
其直接参考项为
$$
 \mathcal R_0u={1\over\sqrt{12}}
            (-u_{k,\theta}-u_{p,\theta\theta},
                         u_{k,\theta\theta}-u_{p,\theta}).
$$

下面的门只损两个明确角导数。对 $|s|\le4$，令
$\mathcal K_\psi=D_z^2F[\widehat z,\cdot]+\psi D_z\mathcal R$。
则
$$
 \|w^{-1}(\mathcal K_\psi-\psi\mathcal R_0)u\|_{H^s}
 \le2^{24}(1+|\lambda|)\widehat n\|u/w\|_{H^{s+1}}
       +2^{32}|\psi|n\|u/w\|_{H^{s+2}} .                \tag{J.21}
$$
**完整 tame 证明。** 把 $p/w,k/w$ 及其前两个角 jet 当作独立
Banach-algebra 变量，取这些变量 norm 的和。
第59束 (C.14) 在复球 $R=1/64$ 上给
$\|\mathcal R/w\|\le2^{10}\|z/w\|_{\mathcal A^2}$；
同一完整有理式给 $\|F/w\|\le4(1+|\lambda|)\|z/w\|_{\mathcal A^1}$。
中心 norm 至多 $R/4$，两个独立方向各用半径 $R/4$。
双变量 Cauchy 因而给
$\|D^2(\mathcal R/w)\|\le2^{20}$、
$\|D^2(F/w)\|\le2^{12}(1+|\lambda|)$。
沿从0到实际背景的线段积分前一式，即得
$\|D(\mathcal R/w)-\mathcal R_0\|\le2^{20}n$。

把这些 jet 导数展开为真实微分算子时，每个输出至多六个
独立 jet 系数；保留两个输出的求和再付 $2^4$。
在宽1上，任意 $|s|\le4$ 的乘法费用小于
$2^7\|b\|_{\mathcal A_1}$，因为
$(1+x)^4\le65e^x$ 且
$\langle m+n\rangle^{s}/\langle m\rangle^s
 \le(1+|n|)^{|s|}$。
合计这些因素仍严格小于 (J.21) 的常数。
该证明使用完整卷积及所有有符号频率，没有有限模压缩。

代第60束的已付 $\widehat n$、$n_i\le4(N_i^c)^\#X_*$，以及
$\int(1+|\lambda|)dy<64(j_i+4)$，得到每个实际 strict 分量的
完整强源门
$$
 \int\|w^{-1}(\mathcal K_\psi-\psi\mathcal R_0)w
             :H^{s+2}\to H^s\|\,dy
 <2^{872}(j_i+4)(N_i^c)^\#X_*P_j\rho^5,
 \quad P_j=h_j^{-14}\delta_j^{-7/4} .                    \tag{J.22}
$$
若该分量不遇控制支集，直接 $\psi\mathcal R_0$ 项为0，仍有
真实背景响应列。此式没有把全空间强门降格成逐模估计；其两个角导数
也没有在转向点或全网络中被免费消去。

## 7. Holonomy 的线性化正是自由 raw 通量 mean

对 $\mathfrak m=(T+Kp_\theta)/(T\sqrt D)$，第59束的逐点恒等式给
$$
 D_z\mathfrak m[u]
 =J D^{-3/2}(u_k-du_p)
    +\partial_\theta\left({K\over T\sqrt D}u_p\right).
 \tag{J.23}
$$
由于 $u_p=h_\theta/r$、$u_k=h_r$，第一项恰是 bare flux。
所以
$$
 DM[u]=\langle\pi-F^t\rangle.                         \tag{J.24}
$$
这是同一量纲下的准确等式，不是只比较一个主符号。
背景固定 $M=1$ 不要求任意 Jacobi Cauchy 数据满足 $DM[u]=0$。

在齐次情况下，令 $\alpha=DM[u]$。对完整控制求导，
$\mathcal BM=0$ 及其 $z$ 导数使全部局部 $\psi$ 项消去，准确有
$$
 \dot\alpha=DM[\widehat{\dot u}]+D_z^2M[\widehat z,u].
 \tag{J.25}
$$
$\alpha$ 可以是任何独立输入；式 (J.25) 没有把它或其响应设为0。
高度仍通过
$$
 \dot h_y={r\over\sqrt{12}}
             (\widehat{\dot u}_k+\psi(D_zF_1u)_k)
$$
恢复，并保留一个独立平均高度初值。

## 8. Weak 源、端荷与实际下一消费者

(J.11) 的完整仿射项可直接写成
$$
 \boxed{\quad
 \widehat s_\psi=
 \binom{-\dot aF^t-a\dot F^t}
 {\dot g-\partial_\theta(\dot F^\theta+\dot dF^t+d\dot F^t)
                                  -\psi L_c(aF^t)} .\quad}
 \tag{J.26}
$$
最后一项保留为角 weak divergence
$-\partial_\theta[\psi c\partial_\theta(aF^t)]$ 即可。
这只使用实际源的角正则，不要求 $F^t_t$；若所给源窗口没有这个
额外角导，(J.26) 只作为相应较弱空间的强导数，不能冒称无损。
对 arbitrary $L^1_t$ 源，乘以 $\psi$ 只给 $\rho^4$，没有免费的
支集长度。源另有真实径向 sup 时才能得到 $\rho^5$。

两个端点仍准确使用
$\pi_{\rm bare,e}=\pi_e-F^t_e$ 及
$\dot\pi_{\rm bare,e}=\dot\pi_e-\dot F^t_e$。
这些迹的存在与范数仍须由原输入空间授予。
因为 $\psi=0$ 于所有原切口，局部剪切没有改变任何真实端口。
在联立 $\Gamma^*(a,\Omega)$ 上还必须加入两个真实
$D_\Omega\Gamma_s^*$ 列；本篇偏导固定当前 $\Gamma$。

(J.12)、(J.15)、(J.18)–(J.22) 现在给完整 $D_\psi E$ 的实际
源及局部 quadratic 核。要把它们用于非径向近共振簇，仍须在同一
physical principal 识别下传播这些源，比较真实多频簇上的二次型，
并保留全网络的状态质量及两参数补偿。
单独的径向指数谱隙、裸角小位移或 (J.22) 的二阶强门均不替代它们。

[准确代数与有理预算程序](../scripts/fourfold_actual_canonical_profile_generator_20261114.py)
及[实际执行记录](../notes/2026-11-14-R119-actual-canonical-profile-generator-budget.json)
保存本次新计算；没有复用失联的旧 native。
