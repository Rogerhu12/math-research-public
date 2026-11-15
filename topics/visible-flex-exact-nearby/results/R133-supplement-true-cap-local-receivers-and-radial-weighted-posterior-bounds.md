# R133 续篇：同一真帽的双向局部接收核与径向加权后验界

2026-11-15，visible-exact / tail_connector。

**已证明下述解析核公式与条件型后验界，供独立核对。** 本篇使用原 ac1 / 440866 连续中心、真实区间 $[L,R]=[9/10,25/8]$ 和原全频参考线。它没有运行新数值，没有重新证明原 Riccati 包围，也不把已付右帽 $C^0<10^{-4}$ 当成所需的极小 ordinary body 界。

依赖[原物理全模帽](R133-supplement-actual-final-all-mode-physical-cap-Green.md) C.12--25、[普通 $L^1$ 源](R133-supplement-physical-cap-L1-Wiener-sources-and-practical-nonlinear-body-ball.md) A.3--19、[实际零宽双输入帽](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md) M.1--12、[RC 实际右帽球](R133-supplement-actual-right-cap-wide-C0-collar-entry.md)及[RB 真 moving $L^2$ 转换](R133-supplement-actual-right-cap-body-and-nonlinear-moving-L2-comparison.md)。

## 1. 同一个参考、两种角模和所有端值

角坐标是帽的真实物理 $\theta$；Fourier 频率 $k\in4\mathbb Z$，圆周测度归一。径向测度是 $dr$。对 $k\ne0$ 记 $M=|k|\ge4$，把 physical $B_k$ 乘原 unitary 因子 $i\operatorname{sgn}k$ 后记为 $b_k$，并令
$$
 d_k=b_k+q_Mc_k,\qquad
 A_D=M\gamma q_M-2\beta,\quad
 A_C=M\gamma q_M+\beta(\ell+1).
 \tag{RW.1}
$$
$q_M$ 是原真 rotational outer line 的同一条参考解，包含原 positive-tail fee；不把它替换成自由终端特征值。

原完整方程是
$$
 \begin{aligned}
 d_k'&=A_Dd_k+U_k,\qquad
 U_k=(-M\gamma+q_M\beta)\mathcal Q_k+F_{B,k}+q_MF_{C,k},\\
 c_k'&=-A_Cc_k+M\gamma d_k+V_k,\qquad
 V_k=\beta\mathcal Q_k+F_{C,k}.
 \end{aligned}\tag{RW.2}
$$
这里 $\mathcal Q$ 可为独立标量源，或实际 nonlinear $Q$ 的完整增量；$F_B,F_C$ 是普通物理体源。unitary $B$ 变换不改变本文所有绝对值和范数。端值是 $d_k(R)$、$c_k(L)$，不是两端均给 Dirichlet。

两 mean 必须另解
$$
 B_0'=-2\beta B_0+F_{B,0},\qquad
 c_0'=-\beta(\ell+1)c_0+\beta\mathcal Q_0+F_{C,0},
 \tag{RW.3}
$$
并各从右端给值。$\beta<0$；不能将后面 $M^{-1}=0$ 的高频极限当作这两个 mean 方程。当前反射实际族准确有 $B_0=0$，但普通算子公式先保留该行。

## 2. 真双向核和源点、输出点的不同 $q$

定义
$$
 E_D(r,t)=\exp\!\left(-\int_r^t A_D(s)\,ds\right)\quad(r\le t),
 \qquad
 E_C(t,r)=\exp\!\left(-\int_t^r A_C(s)\,ds\right)\quad(t\le r).
 \tag{RW.4}
$$
先从右解 $d$，再从左解 $c$，Fubini 给准确公式
$$
 \begin{aligned}
 d(r)&=E_D(r,R)d_R-\int_r^R E_D(r,t)U(t)\,dt,\\
 c(r)&=E_C(L,r)c_L+H_M(r,R)d_R
       -\int_L^R H_M(r,t)U(t)\,dt
       +\int_L^r E_C(t,r)V(t)\,dt,\\
 H_M(r,t)&=\int_L^{\min(r,t)}
       E_C(s,r)M\gamma(s)E_D(s,t)\,ds.
 \end{aligned}\tag{RW.5}
$$
这是同一个真实参考 $q_M$ 上的有序积分，没有换到任意新 reference。

令
$$
 T_{\rm dc}(v)=
 \sup_{L\le s\le v}\frac{\gamma(s)}{s_D(s)+s_C(s)},
 \quad A_D\ge Ms_D>0,\quad A_C\ge Ms_C>0.
 \tag{RW.6}
$$
可以用原闭行正包围对该比值作上界。对 $t\ge r$，从 $E_D(s,t)=E_D(s,r)E_D(r,t)$ 抽出右段；对 $t\le r$，从 $E_C(s,r)=E_C(s,t)E_C(t,r)$ 抽出左段。于是
$$
 H_M(r,t)\le
 \begin{cases}
 T_{\rm dc}(r)E_D(r,t),&t\ge r,\\
 T_{\rm dc}(t)E_C(t,r),&t\le r.
 \end{cases}\tag{RW.7}
$$
剩余共同积分中的 $M\gamma$ 由 $T_{\rm dc}M(s_D+s_C)$ 支配，指数核的质量至多1，故没有额外径向长度因子。

在 $r=L$ 时必须使用准确的
$$
 H_M(L,t)=0. \tag{RW.8}
$$
不能为了方便将它换成一个正的 $T_{\rm dc}(L)$ 贡献。

当 $\mathcal Q=0$ 时，普通源的完整 signed kernels 为
$$
 \begin{array}{c|cc}
 &F_B(t)&F_C(t)\\ \hline
 c(r)&-H_M(r,t)&{\bf1}_{t\le r}E_C(t,r)-q_M(t)H_M(r,t)\\
 b(r)&-{\bf1}_{t\ge r}E_D(r,t)+q_M(r)H_M(r,t)&
 -q_M(t){\bf1}_{t\ge r}E_D(r,t)
 -q_M(r){\bf1}_{t\le r}E_C(t,r)
 +q_M(r)q_M(t)H_M(r,t).
 \end{array}\tag{RW.9}
$$
源组合中的 $q_M(t)$ 与输出重建中的 $q_M(r)$ 不能互换。若只取正包络，可用四个分量核
$$
 \begin{aligned}
 K_{bB}&={\bf1}_{t\ge r}E_D+q_M(r)H_M,&
 K_{cB}&=H_M,\\
 K_{bC}&=q_M(t){\bf1}_{t\ge r}E_D
       +q_M(r){\bf1}_{t\le r}E_C+q_M(r)q_M(t)H_M,&
 K_{cC}&={\bf1}_{t\le r}E_C+q_M(t)H_M .
 \end{aligned}\tag{RW.10}
$$
所有量在本 cap 上非负。保留 signed 核可以另作更尖的合法计算；本文的正包络不依赖未知抵消。

## 3. 真局部 ordinary body receiver

给定真实输出子区间 $J\subset[L,R]$，对每个源点 $t$ 先分别取分量的 $L^2(J,dr)$：
$$
 \begin{aligned}
 {\cal K}_{B,J}(t)&=
 \sup_{M\in4\mathbb N}
    \{\|K_{bB}(\cdot,t)\|_{L^2(J)}
      +\|K_{cB}(\cdot,t)\|_{L^2(J)}\},\\
 {\cal K}_{C,J}(t)&=
 \sup_{M\in4\mathbb N}
    \{\|K_{bC}(\cdot,t)\|_{L^2(J)}
      +\|K_{cC}(\cdot,t)\|_{L^2(J)}\}.
 \end{aligned}\tag{RW.11}
$$
把 (RW.3) 对应的 backward mean kernel 的 $L^2(J)$ 与每个同类上界取最大，得到完整 $\widetilde{\cal K}_{B,J},\widetilde{\cal K}_{C,J}$。然后 Minkowski、Parseval 和完整 Fourier $\ell^1$ 求和给
$$
 \|b\|_{L^2(J\times S^1)}
 +\|c\|_{L^2(J\times S^1)}
 \le \int_L^R
 \{\widetilde{\cal K}_{B,J}(t)\|F_B(t)\|_{\mathcal A_0}
  +\widetilde{\cal K}_{C,J}(t)\|F_C(t)\|_{\mathcal A_0}\}\,dt
 \tag{RW.12}
$$
加上真实端值和 $\mathcal Q$ 的独立列。
这里不是将 $\|K_{bB}\|_2+\|K_{cB}\|_2$ 误写成
$\|K_{bB}+K_{cB}\|_2$；也没有把径向 $L^2$ 与 Fourier 径向 supremum 互换。

对左端 $b(L)$，若 $c_L=0$，known ordinary-source 列准确为
$$
 b(L)=-\int_L^R E_D(L,t)
             \{F_B(t)+q_M(t)F_C(t)\}\,dt
       +E_D(L,R)d_R. \tag{RW.13}
$$
一般 $c_L$ 还保 $-q_M(L)c_L$。mean 仍用 (RW.3)。
这是一个独立的未闭 receiver；只有为 $\mathcal Q$、真 outer 图和所有独立输入付费后，才可以称实际帽解的左端界。

旧已成 summary 中的 whole $L^1$ 与右 $C(R)$ 数不能反推出
(RW.12)--(RW.13)；新的 kernel restriction 是明确的新科学函数。

## 4. 径向权与全频质量界

取非负分片常数 $\lambda(r)$，节点可用原闭行的共同细分，定义
$$
 w(r)=\exp\!\left(-\int_L^r\lambda(s)\,ds\right),\qquad
 w(L)=1,\quad w(r)>0.
 \tag{RW.14}
$$
只给实际存在的同一个完整帽解乘这个权；不更换角坐标、端口或真外图。
有限区间上 $w$ 有严格正下界，故以下加权范数有限：
$$
 X_w=\sum_k\sup_{[L,R]}w(r)|b_k(r)|
       +\sum_k\sup_{[L,R]}w(r)|c_k(r)|.
 \tag{RW.15}
$$
这是两个 Wiener 范数之和，不是 Hilbert pair，也不是
$L^\infty_r\mathcal A_0$。

令 $\widetilde d=wd,\widetilde c=wc$。两阻尼准确变为
$$
 \widetilde A_D=A_D-\lambda,\qquad
 \widetilde A_C=A_C+\lambda.
 \tag{RW.16}
$$
backward 比值 $w(r)/w(t)=e^{\int_r^t\lambda}$ 减少 $D$ 阻尼；
forward 比值增加 $C$ 阻尼。两个号不能取成相同方向。

要求逐真闭行有
$$
 4s_D-\lambda>0,\qquad
 -2\beta-\lambda>0,\qquad
 -\beta(\ell+1)-\lambda>0.
 \tag{RW.17}
$$
第二个门只在包含独立 $B$ mean 的完整普通算子时需要；严格反射值定理中该行准确为0，也可仍使用此更强充分门。没有把检查 $M=4$ 代替整个非mean频率族。

对同一个高频参数 $z=M^{-1}\in(0,1/4]$，置
$$
 \begin{aligned}
 D_\lambda(z)&=\sup_r
   \frac{\gamma(r)+q_+(r)|\beta(r)|z}{s_D(r)-\lambda(r)z},\\
 T_\lambda(z)&=\sup_r
   \frac{\gamma(r)}{s_C(r)+\lambda(r)z},\\
 C_\lambda(z)&=\sup_r
   \frac{|\beta(r)|z}{s_C(r)+\lambda(r)z}.
 \end{aligned}\tag{RW.18}
$$
每个分母使用同一真系数的已付正向 lower；$q_+(r)$ 是已成真 reference upper。
令全局 $q_+=\sup q_+(r)$，则完整 nonmean 标量 $\mathcal Q$ 到 pair 的界是
$$
 K_{\lambda,\ne0}=
 \sup_{0\le z\le1/4}
 \{D_\lambda(z)+(1+q_+)[T_\lambda(z)D_\lambda(z)+C_\lambda(z)]\}.
 \tag{RW.19}
$$
这里 $z=0$ 只连续包住 $M\to\infty$；两 mean 的费用另为
$$
 K_{\lambda,0}=
 \sup_r\frac{|\beta(r)|}{-\beta(r)(\ell(r)+1)-\lambda(r)},\qquad
 K_\lambda=\max(K_{\lambda,\ne0},K_{\lambda,0}).
 \tag{RW.20}
$$
于是
$$
 \|\mathcal G_{Q,w}\mathcal Q\|_{X_w}
 \le K_\lambda\|\mathcal Q\|_{\mathfrak A_w},\qquad
 \|\mathcal Q\|_{\mathfrak A_w}=\sum_k\sup_r w|\mathcal Q_k|.
 \tag{RW.21}
$$
证明是对每个完整频率先用正阻尼 kernel 的质量，后作 $\ell^1$ 求和。
因此 (RW.20) 的最大值合法；不将这个 Wiener 结论自动授给
$\ell^2_k\sup_r$ 的 pair-sum Hilbert module。

同样令
$$
 H_{D,\lambda}=
 \max\!\left(1,\sup_{0\le z\le1/4}
   \{1+(1+q_+)T_\lambda(z)\}\right),\qquad H_C=1+q_+.
 \tag{RW.22}
$$
普通体源、两个 mean 和端值的完整正向界为
$$
 \begin{split}
 X_w\le{}&
 H_{D,\lambda}\int_L^R w\|F_B\|_{\mathcal A_0}\,dr\\
 &+(q_+H_{D,\lambda}+H_C)
             \int_L^R w\|F_C\|_{\mathcal A_0}\,dr\\
 &+H_C\|c_{\ne0}(L)\|_{\mathcal A_0}
 +w(R)\{H_{D,\lambda}\|d_{\ne0}(R)\|_{\mathcal A_0}
                       +|B_0(R)|+|c_0(R)|\}\\
 &+K_\lambda\|\mathcal Q\|_{\mathfrak A_w}.
 \end{split}\tag{RW.23}
$$
独立 true jumps 还按所在 $r_i$ 乘 $w(r_i)$，并用相同完整
$H_{D,\lambda}$、$q_+H_{D,\lambda}+H_C$ 支付。
原连续中心没有新 value jump，不等于可删任意独立方向跳。

## 5. 同一个实际非线性帽上的加权后验闭合

本节严格用 M 的同一实反射 product 域
$$
 \|\gamma_{\rm in}\|_{\mathcal A_0}<10^{-9},
 \qquad \|f_B\|_{\dot{\mathcal A}^2_0}<2^{-60},
 \tag{RW.24}
$$
或已成 X 的更小正角宽子域。保原 $\rho=3\cdot10^{-6}$、
$\|c_{\ne0}(R)\|\le9.9\cdot10^{-10}$；$f_B$ 是 normalized physical height，
其物理单位仍为 $s_Bf_B$。完整 mean/holonomy 外图已包含在这个实际解中。

写实际 correction 为 $x=(b,c)$，相对同一 repaired physical centre；$\gamma_{\rm in}=P_{\ne0}(C(L)-\widehat C(L))$，正是原真图的 inner 输入。
完整 $\mathcal Q$ 增量是 $Q_Bb+Q_Cc+\mathcal R_Q(b,c)$。
由已付 joint
$\max(\|Q_B\|,\|Q_C\|)<.051432066$ 得线性 weighted 界。
二次项必须沿准确 A.18 通分式证明，而非只从一个 unweighted 数字猜出：
$$
 \mathcal R_Q(b,c)
 =\frac{b^2-2ubc+(Kv^2+u^2)c^2}{\widehat C+c},\qquad
 \|\mathcal R_Q(x)\|_{\mathfrak A_w}
 \le\frac{12}{1-6\rho}\,\rho X_w<13\rho X_w.
 \tag{RW.25}
$$
每个二次乘积仅给一个因子乘 $w$，另一因子用真实已成 $X\le\rho$；
完整 reciprocal 仍用原 unweighted Neumann 级数。所有卷积 mean 保留。

真外图在同一个 $f_B$ 上的变化，保完整
$L_D=.006$、$L_0=.00075$ 上界。由于 $w(R)$ 是该端同一 scalar，
$$
 w(R)\|d_R-r_D\|\le L_D X_w,\qquad
 w(R)|c_0(R)-r_{C0}|\le L_0 X_w.
 \tag{RW.26}
$$
$r_D,r_{C0}$ 是同域完整 affine 值，已包含规定 $f_B$、真 outer comparison 和 centre mismatch。
反射使 $B_0=0$；不把它推广到独立一般奇偶输入。

定义
$$
 \begin{split}
 \eta_w={}&H_C\|\gamma_{\rm in}\|_{\mathcal A_0}
 +H_{D,\lambda}\int_L^R w\|F_B\|_{\mathcal A_0}\,dr\\
 &+(q_+H_{D,\lambda}+H_C)\int_L^R w\|F_C\|_{\mathcal A_0}\,dr
 +w(R)\{H_{D,\lambda}r_D+r_{C0}\},\\
 \chi_w={}&K_\lambda(.051432066+13\rho)
                   +.006H_{D,\lambda}+.00075.
 \end{split}\tag{RW.27}
$$
若新公开 directed computation 真正证明 $\chi_w<1$，则同一个已存在实际解满足
$$
                 X_w\le\frac{\eta_w}{1-\chi_w}. \tag{RW.28}
$$
这是后验界，不另行声明一个新存在球、角解析域或 unknown composition 定理。
$\chi_w\ge1$ 的候选只不给该新后验界，不能删去或叫作旧解失败。
$\lambda=0$ 的原已成界可直接原样复制作为比较；不得为本篇重算旧成功的 whole $L^1$ 和 Riccati 门。

例如 $J_+=[9/10,19/20]$ 上可进一步读出
$$
 \|b\|_{L^2(J_+\times S^1)}+\|c\|_{L^2(J_+\times S^1)}
 \le \left(\int_{J_+}w^{-2}\,dr\right)^{1/2}
                       \frac{\eta_w}{1-\chi_w}. \tag{RW.29}
$$
每个分量先由自己的 joint Wiener norm 取全径向上界，后作两分量求和；
这里没有遗漏 $\sqrt2$。原 unweighted RC 的 $X<1.75\cdot10^{-6}$
也给另一个完整候选，取两整界的最小值合法。

(RW.29) 相对的是 $\widehat W$，不是 $W_\delta$。
对 selected body 必须另加真实 $W_\delta-\widehat W$ 的同窗界，再用 RB 的
$80$ 倍普通 $L^2$ 真角转换。可以用其 $10|\delta|\sqrt{|J_+|}$ fallback，
也可以消费同窗 canonical 方向；不得因 $\gamma_{\rm in}$ 小就把这个 affine 项置零。
这些都不等于未知 low-cut 准入已通过。

还有一个不需该 selected affine triangle 的准确高投影读出：在同一个帽上
$Q_\delta=Q_0+\delta Z_{\rm can}$ 且 $Z_{\rm can}$ 的角支撑止于96。
对 RB 取其合法 $\delta=0$ 比较对象，得到
$$
 \|H_J(Q^*-Q_\delta)\|_{L^2(J_+\times S^1),\oplus_1}
 =\|H_J(Q^*-Q_0)\|_{L^2(J_+\times S^1),\oplus_1}
 \le80\{\|b\|_{L^2(J_+)}+\|c\|_{L^2(J_+)}\},
 \quad J\ge96. \tag{RW.29a}
$$
这里 $H_J$ 始终是 moving 角的正交投影，先使用 RB 的完整真角比较再投影；
没有把物理 Fourier 模与 moving Fourier 模相同。完整 finite193 cut 仍相对
$Q_\delta$，其真实 mean/affine 量不由 (RW.29a) 删除。若还要左乘径向 $P$，另付同窗 $p_+$。

### 5.1 已闭后验界到真实 inner $B$ 和 $C$ mean

令 $a_0=-\beta(\ell+1)>0$，在下式中用对应原闭行的真实 lower bound 记
$$
 e_D=e^{-4\int_L^R s_D},\quad
 e_{D,w}=e^{-\int_L^R(4s_D-\lambda)},\quad
 e_0=e^{-\int_L^R a_0},\quad
 e_{0,w}=e^{-\int_L^R(a_0-\lambda)},\quad
 A_Q=.051432066+13\rho .
 \tag{RW.30}
$$
$e_D$ 是所有 $M\ge4$ 真 $E_D(L,R)$ 的 upper；不是把实际频率固定成4。
同理 $e_{D,w}=e_D/w(R)$，$e_{0,w}=e_0/w(R)$。
定义新的完整 ordinary receiver
$$
 \eta_{B,L}=\int_L^R e^{-4\int_L^t s_D}
       \{\|F_B(t)\|_{\mathcal A_0}+q_+(t)\|F_C(t)\|_{\mathcal A_0}\}\,dt,
 \qquad
 \eta_{0,L}=\int_L^R e^{-\int_L^t a_0}|F_{C,0}(t)|\,dt.
 \tag{RW.31}
$$
若旧字段没有独立 physical mean，只能在第二式安全使用完整
$\|F_C(t)\|_{\mathcal A_0}$；不得从一个 norm 猜出均值的抵消。

由 (RW.8)、$b(L)=d(L)-q_M(L)\gamma_{\rm in}$ 和两独立 backward 积分，
同一个实际反射解满足
$$
 \begin{aligned}
 \|b_{\ne0}(L)\|_{\mathcal A_0}
 &\le q_+(L)\|\gamma_{\rm in}\|
       +\eta_{B,L}+e_Dr_D
       +\{(\sup_zD_\lambda(z))A_Q+.006e_{D,w}\}X_w,\\
 |c_0(L)|
 &\le\eta_{0,L}+e_0r_{C0}
       +\{K_{\lambda,0}A_Q+.00075e_{0,w}\}X_w .
 \end{aligned}\tag{RW.32}
$$
把 (RW.28) 代入后，这是同一真实图的 affine-plus-$\|\gamma_{\rm in}\|$
上界。$\mathcal Q$ 列只有一次，outer 列也没有再次乘原 closed inverse。
$B_0(L)=0$ 只由当前精确反射；$c_0(L)$ 仍为真实输出。
新的 $\eta_{B,L},\eta_{0,L}$ 需要公开计算，本文不授其数值大小。


## 6. 最小新公开消费者的准确对象

允许读取以下已成原件，均只恢复到公共 runner 的临时目录：

1. 原 7296 complete residual 行；cap 真交段1341行，原完整 mean 保留。
2. 原949条 reference 行及其 intrinsic native 对应行。
3. 已成 cached-cap 小 summary 的完整 physical source constants、旧成功 whole $L^1$/endpoint/RC身份。
4. 本篇及当前 M/RC 的准确源域合同。

原字段 `complete_residual_A0.U/V` 保存未乘 amplitude 的 moving 残差 norm；
physical conversion 在新加权积分的被积式中只乘一次 $|\alpha|$。
使用原完整 composition 与 repair residual 费用，不能用 response/adjoint residual 顶替背景 residual。
这里不消费 MC 的 raw response mean-flow；若未来改用 canonical $Q_\delta$ 源，
必须重新保 MC 的 $+\delta r_0e_2$，当前 collar restriction 不授全帽 raw-mean 界。

新科学只为指定有限组非零 $\lambda$ 计算 (RW.17)--(RW.29)，以及明确要求的
(RW.12)--(RW.13) kernel restrictions。每个 $\lambda$ 的全源积分、真端值、mean 分母、
all-frequency $z$ 区间和 $\chi_w$ verdict 全部输出。
不用新 inverse angle、target、Riccati、old convolution 或 old residual 生产器。

在连续 $z\in[0,1/4]$ 上可作有向区间细分。由于分母正，
$D_\lambda(z)$、$C_\lambda(z)$ 随 $z$ 非减，
$T_\lambda(z)$ 随 $z$ 非增；每个小区间对三者分别取有向安全端点，
再完整组合 (RW.19)。不得只在 $M=4$ 检查并沿用到全部频率，
也不能把三个量在不同频率取得的“最小值”相乘。

径向积分用真实闭行交集。若 $w$ 在某片上为
$w(l)e^{-\lambda_i(r-l)}$，其已知常数源积分准确使用
$w(l)(1-e^{-\lambda_i h})/\lambda_i$，$\lambda_i=0$ 时取真极限 $w(l)h$。
所有 exponential 及正分母由 directed Arb 在 Actions 中计算；
不能按交长比例缩旧整格积分，不能重算旧成功行再写为“新 restriction”。

(RW.12) 的局部 $L^2$ kernel 平方积分必须分别对两分量保完整，
或使用另一个明确安全的正上界；只有旧 scalar norm 时，不授更尖局部 receiver。
新 summary 只保完整小科学结论与所有输入身份，不持久化可重算 native。

## 7. 与当前总目标的关系

RC 已付同一实际帽右半宽 $C^0$ 门。(RW.28)--(RW.29) 需要新的权重/源积分成功结果，
才能给可能更小的 ordinary body 候选；本篇本身没有把这些候选视为已算通过。
左半 core、真正两侧同态、selected cut finite193、未知高带及 narrow MA 高域仍按原接口独立保留。

原 Green 的三种旧输出 Gram 不提供新33--96模局部接收；本篇的 cap 核也不能把物理角模自动认作 moving 投影。degree32 split 的高频恒等式可在同一个实际 moving 状态上另用，但未知 shell norm 仍须真实支付。

完整 core/far/mean/参数匹配和最终 single $G$ 的存在没有由一个未闭 source receiver 或
一个新的 weighted a priori 界替代。
