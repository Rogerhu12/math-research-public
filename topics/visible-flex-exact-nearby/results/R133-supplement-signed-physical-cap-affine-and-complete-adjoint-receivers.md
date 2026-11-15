# R133：同源物理帽仿射负荷的完整有符号伴随接收式

2026-11-15，visible-exact / tail_connector。

**已证明下述同一物理对象的准确恒等式、完整误差合同及新有符号泛函的计算式。** 原 full-cap 伴随提案、7908 个已成 ordinary residual Gram、真实两端数据和实际帽值球均保持其原身份。本文不重做原 QR、原 residual norm 网格、原 Green sweep 或任何成功积分；新目标是同一源作用于原 97 个已知试件的完整有符号向量。其实际大小、选定参数的仿射门及非线性 core 匹配尚待新的公共消费者核验。

## 1. 固定物理方程及准确基点

固定原 ac1 候选、完整连续修补 440866、物理 $\eta_0$、原反射类和 $I=[L,R]=[9/10,25/8]$。记已知 moving 中心为 $\widehat Q=(u,v)$，真实物理中心为
$$
 \widehat W=(\widehat B,\widehat C)
   =\left(\frac uv,\frac1v\right)\circ\Theta^{-1},
 \qquad m=\langle v\rangle_\varphi,\quad
 \Theta=\varphi+m^{-1}I_\varphi(v-m),\quad j=\Theta_\varphi=v/m.
 \tag{SA.1}
$$
$m<0$，但 $j>0$。角内积均用归一化完整圆周测度。原 intrinsic 修改仅支持在 $(.05,.18)$；这里整个帽的 intrinsic metric 与已安装原物理帽相同。

使用 [M](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md) M.1–M.8 的实际实反射 product 域
$$
 \|\gamma\|_{A^0}<10^{-9},\qquad
 \|f\|_{\dot A^2}<2^{-60},\qquad
 W_*(\gamma,f)=\widehat W+y .
 \tag{SA.2}
$$
$\gamma$ 是同物理角中的完整非mean曲率输入，恰有
$$
 P_\perp y_C(L)=\gamma,\qquad
 \|y\|_{X_0}\le\rho=3\,10^{-6},\qquad
 \|P_\perp y_C(R)\|_{A^0}\le9.9\,10^{-10}.
 \tag{SA.3}
$$
$X_0$ 是逐 Fourier 系数径向 supremum 后求 $\ell^1$、两分量取和的原 joint Wiener norm。特别 $\gamma=0$ 时，内端非mean $C$ 差准确为零；这里用 M.8 的身份，不由量级或 mean 规范猜测。$B_0=0$ 来自原反射；$C_0$ 是实际输出。

写
$$
 A(B,C)=\frac{K+B^2}{C},\qquad
 {\cal F}_{\rm phys}(B,C)
 =\binom{\gamma_{\rm rad}\partial_\theta A-2\beta B}
              {\gamma_{\rm rad}\partial_\theta B+\beta(A-C)} .
 \tag{SA.4}
$$
$\gamma_{\rm rad}$ 是固定径向系数，不是内曲率参数 $\gamma$。
[连续物理帽](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md) C.7 与
[完整物理 Green](R133-supplement-actual-final-all-mode-physical-cap-Green.md) C.3–C.19 给
$A_{\rm phys}=D{\cal F}_{\rm phys}(\widehat W)$，完整两行正是原伴随篇 A.6。

令 $R_{\rm raw}=\widehat Q_r-{\cal F}_{\rm mov}(\widehat Q)$ 为准确连续中心的物理归一 moving residual。它包括原 amplitude 一次及完整 continuity repair，不能用 mean-completed response 的残差替换。准确协变与 Gauss 余项给
$$
 \begin{split}
 R_{\rm phys}&=\widehat W_r-{\cal F}_{\rm phys}(\widehat W)
                =D\Psi(\widehat Q)R_{\rm raw},\\
 D_0y&=-R_{\rm phys}+{\cal V}{\cal R}_Q(y),\qquad
 D_0=\partial_r-A_{\rm phys},\\
 {\cal V}q&=(\gamma_{\rm rad}\partial_\theta q,\ \beta q),\\
 {\cal R}_Q(b,c)&=
 \frac{b^2-2u^\flat bc+(K(v^\flat)^2+(u^\flat)^2)c^2}
                         {\widehat C+c}.
 \end{split}
 \tag{SA.5}
$$
上标 $\flat$ 表示同一已知 moving 量拉到物理角。式 (SA.5) 是 [A](R133-supplement-physical-cap-L1-Wiener-sources-and-practical-nonlinear-body-ball.md) A.7、A.18 的 value 恒等式。没有 residual Hessian 项；该项仅在线性化 moving 方程的共轭中出现。第二个源分量 $\beta q$ 的 mean 完整保留。

## 2. 97 个原试件与选定 moving 读出

使用 [原伴随后验](R133-supplement-full-cap-adjoint-high-to-low-boundary-grams.md) A.1–A.18 的同一准确分片 Hermite 试件 $z_\lambda=(z_{\lambda,B},z_{\lambda,C})$，线性依赖
$\lambda=(f_\lambda,a_\lambda)\in\mathbb R^{97}$。前 96 个坐标是
$\sqrt2\sin(4j\varphi)$，末坐标是独立常数 mean。物理试件保留全部 128 odd、128 nonmean even 和一个 even mean；其有限支撑只是已知试件的定义，不截断未知 $y$ 或任何源。

可固定原 $S_0$，也可在 $|\delta|\le10^{-10}$ 取原选定已知 $Q_\delta(L)$ 的真实 $S_\delta$。后者始终保持同一个 physical circle；变化只进入准确已知读出及其左缺陷：
$$
 S_\delta g=v_\delta(g\circ\Theta_\delta),\qquad
 S_\delta^*g=m_\delta(g\circ\Theta_\delta^{-1}),\qquad
 d_{\lambda,\delta}=S_\delta^*f_\lambda,
$$
$$
 \begin{split}
 \Lambda_{\lambda,\delta}(y)
 &=\langle d_{\lambda,\delta},y_B(L)\rangle_\theta
                         +a_\lambda\langle y_C(L)\rangle_\theta,\\
 \zeta_\lambda&=P_\perp z_{\lambda,C}(L),\\
 e_{\lambda,L,\delta}
 &=\big(z_{\lambda,B}(L)-d_{\lambda,\delta},
                      \langle z_{\lambda,C}(L)\rangle-a_\lambda\big),\\
 r_{\lambda,0}^*&=-z_{\lambda,r}-A_{\rm phys}^*z_\lambda .
 \end{split}
 \tag{SA.6}
$$
$m_\delta$ 在准确式中带原符号。选定 $Q_\delta$ 不把 $A_{\rm phys}$ 或 $r_{\lambda,0}^*$ 改名为 selected 背景；本篇的主体仍在 $\widehat W$。原左端 Gram 只认证 $S_0$ 的缺陷；使用 $S_\delta$ 时须另付准确已知的 $d_{\lambda,\delta}-d_{\lambda,0}$，或直接认证当前 $e_{\lambda,L,\delta}$。独立 mean 行使用物理 $C_0$ 单位；若另缩放该行，试件、affine 和误差须同步缩放。

所有真实内部节点保留 $[z]_\tau=z(\tau+)-z(\tau-)$。给任意完整 ordinary/divergence 源 $D_0y=F$，分片弱积分准确给
$$
 \begin{split}
 \Lambda_{\lambda,\delta}(y)
 ={}&-\langle\zeta_\lambda,\gamma\rangle
       +\langle z_\lambda(R),y(R)\rangle
       +\int_I\langle r_{\lambda,0}^*,y\rangle\,dr
       -\int_I\langle z_\lambda,F\rangle\,dr\\
    &-\sum_\tau\langle[z_\lambda]_\tau,y(\tau)\rangle
       -\langle e_{\lambda,L,\delta},
                         (y_B(L),\langle y_C(L)\rangle)\rangle .
 \end{split}
 \tag{SA.7}
$$
角散度项按分布对光滑已知试件配对。原 M 的弱值解已足以使用此式；没有先假设未知高角导。

若改用旧 $\mathcal D=D_0-\mathcal H_R$，则
$\mathcal D y=-R_{\rm phys}+{\cal V}{\cal R}_Q(y)-\mathcal H_Ry$，
而 $r^*_{\lambda}=r^*_{\lambda,0}-\mathcal H_R^*z_\lambda$。于是
$$
 \int\langle r_\lambda^*,y\rangle
       -\int\langle z_\lambda,-\mathcal H_Ry\rangle
                         =\int\langle r_{\lambda,0}^*,y\rangle .
 \tag{SA.8}
$$
这是准确相消。使用 $r_{\lambda,0}^*$ 时不得再加入 $W_H$，也不得又把同一 $\mathcal H_Ry$ 当第二未知源收费。

## 3. 真外图、affine 端值与独立 Cmean

记 $\widehat Z=P_\perp\widehat C(R)$。用当前同一真实长图的完整函数 $d(Z,f)$、$c_0(Z,f)$ 和真实乘子 $q_{\rm true}$，定义已知有符号缺陷
$$
 r_D^f=J\widehat B(R)+q_{\rm true}\widehat Z-d(\widehat Z,f),
 \qquad
 r_m^f=\langle\widehat C(R)\rangle-C_{\rm ref}(R)-c_0(\widehat Z,f).
 \tag{SA.9}
$$
$J$ 的非零物理 Fourier 乘子是 $i\,{\rm sgn}(k)$，故
$J^*=J^{-1}=-J$ 且 $(J^{-1})^*=J$。不在 mean 上逆 $J$。

用原伴随自伴径向 reference multiplier $Q_{\rm ref}$（与 $J$ 交换），置
$$
 \begin{split}
 \Delta_D^f(t)&=d(\widehat Z+t,f)-d(\widehat Z,f)
                                      +(Q_{\rm ref}-q_{\rm true})t,\\
 \Delta_m^f(t)&=c_0(\widehat Z+t,f)-c_0(\widehat Z,f),\\
 e_{\lambda,R}&=P_\perp z_{\lambda,C}(R)-Q_{\rm ref}Jz_{\lambda,B}(R).
 \end{split}
 \tag{SA.10}
$$
完整 reference 比较项明留。实际 $t=P_\perp y_C(R)$ 满足
$$
 Jy_B(R)+Q_{\rm ref}t=\Delta_D^f(t)-r_D^f,\qquad
 \langle y_C(R)\rangle=\Delta_m^f(t)-r_m^f .
 \tag{SA.11}
$$
所以原 terminal 配对准确等于
$$
 \begin{split}
 \langle z_\lambda(R),y(R)\rangle
  ={}&\langle e_{\lambda,R},t\rangle
       +\langle Jz_{\lambda,B}(R),\Delta_D^f(t)\rangle
       +z_{\lambda,C,0}(R)\Delta_m^f(t)\\
     &-\langle Jz_{\lambda,B}(R),r_D^f\rangle
       -z_{\lambda,C,0}(R)r_m^f .
 \end{split}
 \tag{SA.12}
$$
这里使用反射 $B_0=0$，没有删除 $C_0$。完整 general-parity M 的独立 $B_0$ 另有端值列，不在本 97 行反射定理中改成零。

$\Delta_D^f,\Delta_m^f$ 的费用必须使用当前 M product 上的完整
[I.9](R133-supplement-actual-cap-inner-Poisson-perturbation-and-complete97-interface.md)
或更尖已付真列，包括正的 reference 比较项。不能挪用只在原 $\widehat Z$ 极小球上的旧 A.13 常数。本文记其合法 Lipschitz 上界为 $L_D,L_m$。

## 4. 一个完整有符号向量及其四类余项

令 $q_y={\cal R}_Q(y)$，定义
$$
 q_\lambda^*=-\gamma_{\rm rad}z_{\lambda,B,\theta}
                                      +\beta z_{\lambda,C}.
 \tag{SA.13}
$$
第二项保留其完整 mean。由 (SA.5)、(SA.7)、(SA.12)，有
$$
 \Lambda_{\lambda,\delta}(y)
          ={\cal A}_{\lambda,\delta}^{\gamma,f}
                    +{\cal E}_{\lambda,\delta}(y),
 \tag{SA.14}
$$
其中已知部分为
$$
 {\cal A}_{\lambda,\delta}^{\gamma,f}
 =-\langle\zeta_\lambda,\gamma\rangle
       +\int_I\langle z_\lambda,R_{\rm phys}\rangle\,dr
       -\langle Jz_{\lambda,B}(R),r_D^f\rangle
       -z_{\lambda,C,0}(R)r_m^f ,
 \tag{SA.15}
$$
而完整误差为
$$
 \begin{split}
 {\cal E}_{\lambda,\delta}(y)
 ={}&\int_I\langle r_{\lambda,0}^*,y\rangle\,dr
                  -\int_I\langle q_\lambda^*,q_y\rangle\,dr\\
 &-\sum_\tau\langle[z_\lambda]_\tau,y(\tau)\rangle
       -\langle e_{\lambda,L,\delta},
                          (y_B(L),\langle y_C(L)\rangle)\rangle\\
 &+\langle e_{\lambda,R},t\rangle
       +\langle Jz_{\lambda,B}(R),\Delta_D^f(t)\rangle
       +z_{\lambda,C,0}(R)\Delta_m^f(t).
 \end{split}
 \tag{SA.16}
$$
第一行分别是试件 ordinary 缺陷和真实非线性 Gauss 源；第二行是内部 jump/左读出；第三行是真外图反馈。它们同时作用于同一个真实 $y$，不能宣称相互正交。

当一个源项只有已成 norm upper 而没有 signed 数组时，可以在已知向量中选其零提案，再把完整缺项列入误差。例如不能以 $r_D$ 的 norm upper 冒有符号端值，也不能因其很小就设 $r_D=0$。

## 5. 不重算旧 residual norm 的准确新源泛函

对于原分片连续中心，直接分片积分一次即得
$$
 \begin{split}
 \int_I\langle z_\lambda,R_{\rm phys}\rangle\,dr
 ={}&[\langle z_\lambda,\widehat W\rangle]_L^R
       -\sum_\tau\langle[z_\lambda]_\tau,\widehat W(\tau)\rangle\\
 &-\int_I\langle z_{\lambda,r},\widehat W\rangle\,dr
       -\int_I\langle z_\lambda,
                        {\cal F}_{\rm phys}(\widehat W)\rangle\,dr .
 \end{split}
 \tag{SA.17}
$$
所有量现在是已知的。中心的准确连续修补使其没有额外 value-jump；原一侧径向导仍在每片中完整保留。式 (SA.17) 计算新的 signed functional，不重建旧 7296 个 residual norm，也不以这些正上界的差代替 signed residual。

更具体地，若 $\widetilde z=z\circ\Theta$，并对已知 physical 导数先求导再复合，则
$$
 \langle z,\widehat W\rangle_\theta
           =m^{-1}\langle u\widetilde z_B+\widetilde z_C\rangle_\varphi .
 \tag{SA.18}
$$
把 physical 角导移到试件上，(SA.17) 的完整体积分 integrand 是
$$
 \begin{split}
 {\cal I}_\lambda(r)=m^{-1}\big\langle&
   -u(z_{B,r}\circ\Theta)-(z_{C,r}\circ\Theta)
   +\gamma_{\rm rad}(Kv^2+u^2)(z_{B,\theta}\circ\Theta)\\
   &+\gamma_{\rm rad}u(z_{C,\theta}\circ\Theta)
   +2\beta u(z_B\circ\Theta)
   -\beta(Kv^2+u^2-1)(z_C\circ\Theta)\big\rangle_\varphi .
 \end{split}
 \tag{SA.19}
$$
这是 $j\widehat B=u/m$、$j\widehat C=1/m$、
$jA(\widehat W)=(Kv^2+u^2)/m$ 的准确消去。没有 $m_r$ 漏项：
径向分部使用的是 $z_r$ 在固定 physical 角的导数；(SA.18) 只读端值，并未把 $\partial_r(z\circ\Theta)$ 冒成 $z_r\circ\Theta$。

只有已知 forward angle $\Theta$ 被使用。原 Hermite 试件是 finite physical Fourier 和，所以复合由
$$
 e^{4ij\Theta}=e^{4ij\varphi}e^{4ij(\Theta-\varphi)}
$$
的完整已知指数卷积给出，须给全部 omitted Fourier tail 的有向界。
$m^{-1}$ 使用原严格 mean gap；$Kv^2+u^2$、$v$ 的零槽、所有正负 mode 和两 germ 的真径向交集均保留。原 amplitude 只在 $u,v$ 构造中乘一次。

(SA.17)–(SA.19) 可以沿原 saved scalar jets 和旧 Hermite/candidate 定义形成新的径向多项式包围，完成 97 维 signed 积分与完整 remainder。不能只以旧 midpoint action 或试件有限动作残差宣称这个积分已经认证。新向量的各区间贡献、端值、内输入和选定中心差须先有符号相加，再求欧氏 norm。

### 5a. 三组已知 physical moments 对全部 97 列共同收缩

因为试件的 physical angular degree 恰为 128，新泛函只需要以下准确已知 moments。对 $1\le l\le128$，
$$
 \begin{split}
 {\sf B}_l(r)&=\frac2m\langle u\sin(4l\Theta)\rangle_\varphi,\\
 {\sf C}_l(r)&=\frac2m\langle\cos(4l\Theta)\rangle_\varphi,\\
 {\sf A}_l(r)&=\frac2m\langle(Kv^2+u^2)\cos(4l\Theta)\rangle_\varphi,
 \end{split}
 \qquad
 {\sf C}_0=\frac1m,\quad
 {\sf A}_0=\frac{\langle Kv^2+u^2\rangle_\varphi}{m}.
 \tag{SA.19a}
$$
它们分别是完整 physical $\widehat B,\widehat C,A(\widehat W)$ 的 raw sine/cosine 幅度；$\mathsf B_0=0$ 只因反射。每个非mean的 Parseval 权是 $1/2$，mean权是 $1$。写 $z_B=\sum_{l=1}^{128}b_l\sin(4l\theta)$、
$z_C=c_0+\sum_{l=1}^{128}c_l\cos(4l\theta)$，则
$$
 \begin{split}
 {\cal I}_\lambda
 ={}&\frac12\sum_{l=1}^{128}
 \big[(-b_l'+2\beta b_l-4l\gamma_{\rm rad}c_l){\sf B}_l
       +(-c_l'+\beta c_l){\sf C}_l
       +(4l\gamma_{\rm rad}b_l-\beta c_l){\sf A}_l\big]\\
 &+(-c_0'+\beta c_0){\sf C}_0-\beta c_0{\sf A}_0,\\
 \langle z,\widehat W\rangle_\theta
 ={}&\frac12\sum_{l=1}^{128}
                     (b_l{\sf B}_l+c_l{\sf C}_l)+c_0{\sf C}_0 .
 \end{split}
 \tag{SA.19b}
$$
这里 $b_l,c_l$ 仍是线性于全部 97 个输入的原 Hermite 行，撇号是其真实径向导数。三组 moments 可每个真实共同径向域计算一次，再与 97 列共同收缩；无需为每一列重复已知指数展开。

(SA.19a) 中的 $e^{4il(\Theta-\varphi)}$ 必须包含完整严格指数尾，径向多项式的余项也须完整认证。只算有限 physical moments 是因为已知试件有限；不截断 $R_{\rm phys}$、$y$、$q_y$、左端目标 $d_{\lambda,\delta}$ 或 $r_{\lambda,0}^*$ 的任何未知/系数输出。$C_0,A_0$ 单独按完整均值公式计算，不用非mean的 $1/2$ 权或任何二次 normalization。

## 6. 已成 Grams 的合法消费与 actual 值误差

对同一实际 $y$ 选定一条已经通过的 [RW](R133-supplement-actual-radial-weighted-cap-and-complete-left-receivers.md) weight，满足
$w(L)=1$、$w>0$。记合法实际上界
$$
 Y_w\ge\|wy\|_{L^2_rL^2_{\theta,\mathrm{pair}}},
 \quad Y_L\ge\|(y_B(L),\langle y_C(L)\rangle)\|_{L^2\oplus\mathbb R},
 \quad Z_R\ge\|P_\perp y_C(R)\|_2 .
 \tag{SA.20}
$$
可从同一 RW row 的 $X_w(\gamma,f)$ 统一取
$Y_w=\sqrt{R-L}\,X_w$、$Y_L=X_w$，
以及 $Z_R=\min(\zeta,X_w/w(R))$；全部输入域与 affine 负荷不变。
这些是 joint norm 对 ordinary $L^2$ 的正确单向读出。

若对所有 $\|\lambda\|_{\mathbb R^{97}}\le1$ 已认证
$$
 \begin{gathered}
 \|w^{-1}r_{\lambda,0}^*\|_{L^2}\le D_w,\quad
 \|w^{-1}q_\lambda^*\|_{L^2}\le Q_w,\quad
 \|e_{\lambda,L,\delta}\|\le E_L,\quad
 \|e_{\lambda,R}\|_2\le E_R,\\
 \|z_{\lambda,B}(R)\|_2\le Z_B,\quad
 |z_{\lambda,C,0}(R)|\le Z_m,\quad
 \|[z_\lambda]_\tau\|_2\le J_\tau ,
 \end{gathered}
 \tag{SA.21}
$$
则 (SA.16) 给
$$
 \|{\cal E}_{\cdot,\delta}(y)\|_{\mathbb R^{97}}
 \le (D_w+13\rho Q_w)Y_w+E_LY_L
       +(E_R+L_DZ_B+L_mZ_m)Z_R
       +\sum_\tau J_\tau\,\|y(\tau)\|_2 .
 \tag{SA.22}
$$
这里逐点
$$
 |{\cal R}_Q(y)|\le13|y|_{\mathbb R^2}^2
                          \le13\rho|y|_{\mathbb R^2}
$$
由原 $|v^\flat|<6$、$|u^\flat|<1/50$、
$|K(v^\flat)^2+(u^\flat)^2|<2$ 和 $|y|\le\rho$ 给出：分子至多 $(2+1/50)|y|^2$，
分母倒数至多 $6/(1-6\rho)$，两者的乘积严格小于 $13|y|^2$。
从而 $\|wq_y\|_{L^2}\le13\rho Y_w$。
没有将 $Q$ 列降成不含 mean 的散度源。

原 [7908 完整报告](../notes/2026-11-15-R133-actual-complete7908-cap-adjoint-residual-Grams.md)
已分别认证 formal ordinary、Hessian、true ordinary 及四个 field Gram。
$w=1$ 时可直接取
$D_w=\sqrt{\|W_{\rm formal}\|}\le\sqrt{{\rm tr}\,W_{\rm formal}}$，不重复任何原计算，也不加入 $W_H$。$Q_w$ 可由原 $B_\theta,C$ field Gram 和原径向 $\gamma_{\rm rad},\beta$ 包围合法组合。

若要更尖的 weighted/local 误差，只能对原各 closed-cell 完整 PSD Gram 乘同胞元的完整 $w^{-2}$ 上界后求和，或另证新的对应 functional；不能按区间长度比例缩 whole Gram。可用已成 RW 的 rate upper 给 $w(r)^{-1}\le e^{\lambda_+(r-L)}$，这只产生新权的保守重组，不重跑 RW 的已成功积分。所有 signed off-diagonal 项先保留到实际 PSD/Loewner 操作以后。逐项 Cauchy/triangle 对同一个 $\lambda$ 使用，不能把误差平方当独立源直接相加。

原 v2 shared-node exact Hermite 试件连续；若新消费者逐 receipt 恢复并验证共享端值，则内部 $J_\tau=0$ 可由定义准确使用。若改试件、改接片或只保一侧近似，则全部 jump 恢复收费。真 $9/10$ 必须读第一 Hermite 的准确短延拓。

## 7. 选定参数的准确 affine 源及 height

令
$$
 \Delta W_\delta(L)=\Psi(Q_\delta(L))-\widehat W(L),\qquad
 \bar\gamma_\delta=P_\perp\Delta W_{\delta,C}(L).
 \tag{SA.23}
$$
这是完整已知 finite moving cut 在真实物理角中的值差，通常有无限 physical Fourier 尾。
[W](R133-supplement-known-finite-cut-Wiener-angle-and-sharp-low-curvature-entry.md)
已经单独给它的真实帽输入门；这里不将 moving 96 support 误作 physical support。

在 (SA.14) 取 $\gamma=\bar\gamma_\delta$，定义
$$
 {\cal B}_{\lambda,\delta}^{f}
  ={\cal A}_{\lambda,\delta}^{\bar\gamma_\delta,f}
    -\langle d_{\lambda,\delta},\Delta W_{\delta,B}(L)\rangle
    -a_\lambda\langle\Delta W_{\delta,C}(L)\rangle .
 \tag{SA.24}
$$
则 [AR](R133-supplement-actual-cap-affine-height-and-single-integral-boundary-elimination.md)
与 [SR](R133-supplement-uniform-secant-cap-rows-and-complete-finite193-nonlinear-receivers.md)
的准确 base 源
$$
 b_\delta^f=
 \left(\Pi_{96}S_\delta
       [B_*(\bar\gamma_\delta,f)(L)-B_\delta(L)],
       C_{*,0}(\bar\gamma_\delta,f)(L)-C_{\delta,0}(L)\right)
 \tag{SA.25}
$$
满足
$$
              \|b_\delta^f-{\cal B}_\delta^f\|_{97}
                        \le {\cal E}_{\rm bound}
 \tag{SA.26}
$$
其中右端是 (SA.22) 的完整值，另加新 signed vector 的全部认证误差。
在 (SA.24) 中保留 $\bar\gamma_\delta$、已知中心差和 signed 源的关联；
先对三项分别取 norm 再相加只给粗 bound，不能宣称得到新的 signed 改善。

可先固定一个真实 $f_{\rm ref}$。原 I.16 在同一 product 上给
$$
 \|b_\delta^f-b_\delta^{f_{\rm ref}}\|_{97}
       \le\frac7{25}\|f-f_{\rm ref}\|_{\dot H^2}.
 \tag{SA.27}
$$
完整 $C$ mean 在内，$s_B$ 固定；物理高度变化时仍用
$\delta f=(\delta y_B-f\delta s_B)/s_B$。若新 signed 计算本已对整个 height 球统一包围，不重复加入此差。
单一 $\lambda$、mean-height span、waist 和 high body/cut 仍是原 SR 的独立列，本篇不删除或设置它们。

## 8. 可执行范围与尚未授予的数值

后继最小公共消费者应锁定以下原件：

1. 原 v2 的 1977 shared nodes、257 physical states、97 原正交输入和每片两端导数；它们只恢复，不重新 QR。
2. 原 7908 scalar jets、exact continuous candidate/repair，以及现有 formal ordinary/field/端点 Grams；只读原成功对象，不重算。
3. 原当前 RW 值界及同一个真实 $f,\gamma$ 域；不以只含 $\gamma$ 的响应界替非零 affine 值。
4. 新 (SA.17)–(SA.19)、真外端 signed 项或完整缺项费、(SA.24) 的已知选定差；全部同 physical circle/归一测度/真实 $dr$。
5. 全部新 remainder、(SA.22)、未通过的输入或大小门均完整输出。

旧 proposal 的 finite-action check 本身不是 continuous certificate。已成 formal ordinary Gram 是另外一份真正证书；二者的身份必须同时锁定。原小表没有保存 signed residual 时不能倒推它；这里的新积分由明确的已知函数定义重新认证，仅属于新 affine functional。

本文不宣称新 $\mathcal B_\delta^f$ 已算出、不宣称 (SA.22) 小于未知 cut 门，也不把 positive upper 失败解释为实际算子奇异。完成新数值后，仍须与 SR 的同态五输入、CH 的真实 $H^1$ chart 余项及 core 全域入口逐项组合；旧 RW/F/CP/Green 的全部成功与失败记录保持原样。
