# R56. 只用 C² jet 范围的连续度量证书与严格余量下的有限终止

维护：Astra-held10-1b6d88ec-20261120 / n4_continue。

**已证明：** 对已固定实际曲面图和已固定目标度量，给出一个连续误差包围定理；只要求图为 $C^2$、目标矩阵为 $C^1$，不要求径向或角向三阶导数，不以 DFT、径向梯形积分或节点最大值代替连续界。若实际误差在门限内留有严格余量，且输入的区间值、积分和反函数包围可随精度收敛，下面的局部矩阵组织在有限次细分后能证明该门限。

**本条没有完成任何新候选的数值认证。** 它不证明当前 $\lambda=.02$ 场通过 $10^{-6}$ 门，不证明真实尾、闭合、reach、完整 $t$ 族或 README 第 5 条的固定参数加密收敛。已经失败的候选不能由这里的充分条件变成成功。R31、R36、R39 中属于别的核、profile 和参数的数值常数不在这里复用。

R31 已为一个特定图支付了完整连续度量界；R36 已证明一阶 jet 误差向 Gram 矩阵误差的传递。本条新增的是：把实际 $C^2$ 的二阶 jet 区间组织成局部缺陷多项式，给出仅用可验证范围的常数，并证明这种组织在严格余量下可有限终止。归一化矩阵在盒内的变化乘在**已经相消的度量缺陷**上，避免各向异性坐标中不消失的过估计。

## 1. 固定对象与坐标

取闭矩形坐标片 $x=(s,\psi)$，周期角可用有限个有重叠的片覆盖。实际图 $F(s,\psi)\in\mathbb R^3$ 在该片的邻域为 $C^2$。分片五次表示指已经声明的同一个 $C^2$ 函数；三阶导数可以在节点跳跃。

固定材料角 $\theta=\theta(s,\psi)$，令 $\rho=\theta_\psi>0$、$\tau=\theta_s$。固定的真实目标度量为

$$g=\sigma(s)^2\,ds^2+a(s)^2\,d\theta^2,\qquad \sigma>0,\quad a>0.$$

这里 $\sigma$ 是经向尺度，不是尾端高度符号。若代码的 $s$ 不是目标真实弧长，而真实弧长为 $\zeta(s)$，则 $\sigma=\zeta'(s)$、$a=a_{\rm true}\circ\zeta$。不能把 native profile 与真实 profile 的差置零。假设 $a,\sigma$ 为 $C^1$、$\theta$ 为 $C^2$，计算坐标中的目标矩阵

$$
G=
\begin{pmatrix}
 \sigma^2+a^2\tau^2 & a^2\tau\rho\\
 a^2\tau\rho & a^2\rho^2
\end{pmatrix}
\tag{1}
$$

为 $C^1$。定义

$$
C=
\begin{pmatrix}
 1/\sigma&0\\
 -\tau/(\sigma\rho)&1/(a\rho)
\end{pmatrix},\qquad C^TGC=I_2.
\tag{2}
$$

记 $D=DF=[F_s,F_\psi]$，所需相对误差为

$$\eta_F(x)=\left\|C^TD^TDC-I_2\right\|_2.\tag{3}$$

换取另一满足 $\widetilde C^TG\widetilde C=I$ 的矩阵时，$\widetilde C=CO$，$O$ 正交，故 (3) 不变。向量范数均为 Euclidean 范数，矩阵范数均为算子范数。所有数值上界须带向外舍入；浮点特征值本身不是严格上界。

## 2. C² 给出的一阶 jet 余项

设盒 $K$ 的中心为 $x_0$、半宽为 $h_s,h_\psi$，$\xi=x-x_0$。选定向量 $p_s,p_\psi$ 和对称 Hessian 系数

$$A_{ss},\quad A_{s\psi}=A_{\psi s},\quad A_{\psi\psi}\in\mathbb R^3.$$

它们可以是有理或 dyadic 数。假设实际中心一阶 jet 的误差满足

$$
\|F_s(x_0)-p_s\|\le\epsilon_s,\qquad
\|F_\psi(x_0)-p_\psi\|\le\epsilon_\psi
$$

且**整个盒上**有二阶 jet 振幅界

$$
\begin{split}
 \|F_{ss}-A_{ss}\|&\le\Omega_{ss},\\
 \|F_{s\psi}-A_{s\psi}\|&\le\Omega_{s\psi},\\
 \|F_{\psi\psi}-A_{\psi\psi}\|&\le\Omega_{\psi\psi}.
\end{split}
\tag{4}
$$

定义局部二次多项式

$$
P=p_0+p_s\xi_s+p_\psi\xi_\psi+
 \tfrac12A_{ss}\xi_s^2+A_{s\psi}\xi_s\xi_\psi+
 \tfrac12A_{\psi\psi}\xi_\psi^2.
\tag{5}
$$

$p_0$ 不影响度量。沿中心至 $x$ 的线段对一阶导数积分，得到

$$
\begin{split}
 \|F_s-P_s\|&\le e_s
 :=\epsilon_s+h_s\Omega_{ss}+h_\psi\Omega_{s\psi},\\
 \|F_\psi-P_\psi\|&\le e_\psi
 :=\epsilon_\psi+h_s\Omega_{s\psi}+h_\psi\Omega_{\psi\psi}.
\end{split}
$$

于是

$$\boxed{\ \|D-DP\|_2\le d:=\sqrt{e_s^2+e_\psi^2}.\ }\tag{6}$$

这里只用了 $F\in C^2$ 和微积分基本定理。(4) 是 Hessian 相对于选定 $A_{ij}$ 的振幅，不是把全局 Hessian 大小直接乘以盒宽。若范围包围收敛，取范围中心为 $A_{ij}$ 可使 $\Omega_{ij}\to0$；精确中心值时，(6) 的误差是 $o(h_s+h_\psi)$。

### 2.1 目标矩阵只需 C¹

取对称矩阵 $G_0,B_s,B_\psi$，令

$$Q=G_0+B_s\xi_s+B_\psi\xi_\psi.$$

如果中心误差和全盒梯度振幅分别满足

$$
\|G(x_0)-G_0\|_2\le\epsilon_g,\quad
\|\partial_sG-B_s\|_2\le\omega_s,\quad
\|\partial_\psi G-B_\psi\|_2\le\omega_\psi,
$$

同样的线积分给出

$$\boxed{\ \|G-Q\|_2\le e_g:=\epsilon_g+h_s\omega_s+h_\psi\omega_\psi.\ }\tag{7}$$

$\partial_sG,\partial_\psi G$ 只涉及 $a',\sigma'$ 和 $\theta$ 的二阶导数。也可用更高精度的已验证多项式 $Q$；后文只使用 (7)。

## 3. 先相消，再作矩阵 Bernstein 包围

形成对称缺陷多项式

$$S=(DP)^TDP-Q.\tag{8}$$

**先在有理数或带误差的系数层完成乘法和减法，再取绝对值、范数或区间。** 不分别包围接近 1 的平方和和目标值后相减。

将盒线性映到 $[0,1]^2$，写成 tensor Bernstein 形式

$$
S(t,u)=\sum_{i=0}^{d_s}\sum_{j=0}^{d_\psi}
 S_{ij}\,\mathcal B_i^{d_s}(t)\mathcal B_j^{d_\psi}(u),
\tag{9}
$$

其中 $\mathcal B_i^d(t)=\binom di t^i(1-t)^{d-i}$。二次 $P$、仿射 $Q$ 可取 $d_s=d_\psi=2$。若幂基系数为 $U_{pq}$，精确转换为

$$
S_{ij}=\sum_{\substack{p\le i\\q\le j}}
 \frac{\binom ip}{\binom{d_s}p}
 \frac{\binom jq}{\binom{d_\psi}q}U_{pq}.
\tag{10}
$$

权非负且和为 1，范数凸性给出

$$\sup_K\|S\|_2\le b:=\max_{i,j}\|S_{ij}\|_2.\tag{11}$$

选一个固定的中心归一化矩阵 $C_0$，以及可靠上界

$$
c_0\ge\|C_0\|_2,\qquad
e_C\ge\sup_K\|C-C_0\|_2,\qquad c=c_0+e_C.
$$

计算

$$\eta_0:=\max_{i,j}\|C_0^TS_{ij}C_0\|_2.\tag{12}$$

对对称矩阵 $M=\left(\begin{smallmatrix}u&v\\v&w\end{smallmatrix}\right)$，精确有

$$
\|M\|_2=
 \left|\frac{u+w}{2}\right|
 +\sqrt{\left(\frac{u-w}{2}\right)^2+v^2}.
\tag{13}
$$

因此 (11)、(12) 仅需有限个有理运算及向外平方根包围。$C_0$ 不必精确等于 $C(x_0)$，其中心误差计入 $e_C$。

### 定理 1：单盒连续相对误差界

令

$$
\eta_P=\eta_0+(2c_0e_C+e_C^2)b+c^2e_g,\qquad \delta=cd.
\tag{14}
$$

则全盒上

$$
\boxed{\quad
 \eta_F\le\eta_P+2\sqrt{1+\eta_P}\,\delta+\delta^2.
 \quad}
\tag{15}
$$

**证明。** 由 (2)、(8)，

$$
C^T(DP)^TDP\,C-I=C^TSC+C^T(Q-G)C.
$$

写 $C=C_0+\Delta C$，保留中心归一化后的缺陷：

$$
\begin{split}
 \|C^TSC\|_2
 &\le \|C_0^TSC_0\|_2
 +(2\|C_0\|_2\|\Delta C\|_2+\|\Delta C\|_2^2)\|S\|_2\\
 &\le\eta_0+(2c_0e_C+e_C^2)b.
\end{split}
$$

第二项不超过 $c^2e_g$，故 $\eta_P$ 包围 $P$ 的相对误差，并且
$\|DP\,C\|_2\le\sqrt{1+\eta_P}$。由 (6)，
$\|(D-DP)C\|_2\le\delta$。展开
$(DC)^TDC-(DP\,C)^T(DP\,C)$ 的两个交叉项和一个平方项，或直接用 R36 的一阶 jet 到 Gram 矩阵传递式，即得 (15)。证毕。

### 3.1 为什么不能只用 $c^2b$

$c^2b$ 有效但可能很松。即使盒缩成一点，它仍可能严格大于
$\|C(x_0)^TS(x_0)C(x_0)\|_2$，在各向异性坐标中永久浪费门限。(12) 先按实际方向归一化；(14) 中归一化变化项乘在已经相消的 $S$ 上。这两点支持下面的有限终止结论。

## 4. 有限覆盖与严格余量下的有限终止

有限盒覆盖所需正则图域，每盒都保持真实 $a,\sigma,\rho$ 的正下界且 (15) 不超过 $\varepsilon$，就得到整个图域上的连续误差 $\eta_F\le\varepsilon$。不是只覆盖五次节点、角采样点或网格边。

### 定理 2：条件性的有限终止

设图域紧，$F\in C^2$、$G\in C^1$，且 $G$ 一致正定。假设：

1. 中心值、二阶 jet、目标一阶导数及 $C$ 的范围都有可靠包围；
2. 盒直径趋零并提高精度时，包围一致收敛到点值；真实积分、反函数、mean 和中心值计算的误差也可缩小；
3. 实际误差有严格余量：存在 $\Delta>0$ 使 $\sup\eta_F\le\varepsilon-\Delta$。

则按二阶 jet 范围中点选 $A_{ij}$，按目标梯度范围中点选 $B_s,B_\psi$，并提高中心值计算精度，存在**有限**矩形细分，使每盒 (15) 都小于 $\varepsilon$。

**证明。** 紧性给二阶 jet、目标一阶导数和 $C$ 的一致连续性及有界性。由假设 2，中心误差、$\Omega_{ij}$、$\omega_s,\omega_\psi$、$e_C$ 可同时任意小。因此 $d,e_g,e_C\to0$，$c,b$ 一致有界。

把缩小盒中的 $\xi$ 改写为 $t,u$ 后，(8) 的非常数系数都含至少一个盒半宽，其余因子一致有界。每个 Bernstein 系数与中心实际矩阵
$D(x_0)^TD(x_0)-G(x_0)$ 之差一致趋零；$C_0$ 可一致逼近 $C(x_0)$。故 (12) 与 $\eta_F(x_0)$ 的差一致趋零，(14)、(15) 的其余项一致趋零。取足够小的盒和足够高的精度使总差小于 $\Delta/2$；有限个盒覆盖紧域，每盒界小于 $\varepsilon-\Delta/2$。证毕。

裸 $C^2$ 假设不给出统一盒数或运行时上界；固定当前表达式后，区间范围提供可计算连续模量。实际误差恰好等于门限，或 oracle 有不可缩小的误差底时，本条不保证有限终止。未得到证书也不推出解不存在。

仅对 Laurent 系数使用**全周期绝对系数和**，虽有效，却通常不随角盒缩小收敛到点值，不能据此援引定理 2。应以局部角区间、局部多项式余项或等价的收敛求值支付该条件。

若已有一个 $C^2$ 拓扑连续的紧参数族，可把参数区间也纳入各 jet 的包围，空间导数仍只需二阶。本条不构造该族，也不允许几个离散 $t$ 值代替全参数包围。

## 5. 实际五次场与解析核心的可计算常数

本节说明可靠输入的来源，不新增未执行的 solver 或认证入口。每次认证固定同一 profile、角图、完整核心、$q,c$、窗口、同伦参数、真实切点和高度锚；只细分验证盒、提高区间精度，不改变物理参数。

### 5.1 实际 piecewise quintic

在原始径向段上，将已声明状态写为

$$Y(s)=\sum_{k=0}^{5}A_k(s-s_0)^k.$$

子区间 $[l,l+\ell]$ 映为 $t\in[0,1]$ 时，精确幂系数和 Bernstein 系数为

$$
a_r^I=\ell^r\sum_{k=r}^{5}\binom kr A_k(l-s_0)^{k-r},
\qquad
b_j=\sum_{r=0}^{j}\frac{\binom jr}{\binom5r}a_r^I.
\tag{16}
$$

$Y$ 的分量落在相应 $b_j$ 的凸包中；$Y',Y''$ 分别具有 Bernstein 系数

$$
\frac5\ell(b_{j+1}-b_j),\qquad
\frac{20}{\ell^2}(b_{j+2}-2b_{j+1}+b_j).
\tag{17}
$$

对向量区间用向外 Euclidean 范数包围。先沿原始 knots 和 profile 分段点切开再限制子区间。这里只用 $Y,Y',Y''$；$Y'''$ 跳跃不影响定理 1。

R31 的实际图采用共享端点二阶 jet 定义的 Hermite 对象。若当前格式只给舍入后的幂系数，不能因为端点 jet 在浮点下接近就宣称它们在实数意义下严格相同。应使用原本已声明的共享 jet 函数，或支付保存/求值表示与它的差；不能为通过认证静默修补节点，改变实际图。

### 5.2 保留已知多项式，不必把全部对象截成二次

定理 1 只需要已知多项式 $P,Q$ 以及 (6)、(7) 的有效误差界。因此实际计算可以完整保留五次 $Y$、已知径向权函数和有限 Fourier/Laurent 乘积，只给非多项式核心部分支付局部余项。

对固定角向 $C^2$ 向量函数 $H$，在半宽 $h$ 的区间上，若 $H''$ 相对选定 $A$ 的振幅不超过 $\omega$，中心值及一阶导数误差为 $\epsilon_0,\epsilon_1$，则相应二次多项式 $H_P$ 满足

$$
\|H'-H_P'\|\le\epsilon_1+h\omega,\qquad
\|H-H_P\|\le\epsilon_0+h\epsilon_1+\tfrac12h^2\omega.
\tag{18}
$$

对径向 lift $h(s)H(\psi)$，一阶 jet 误差乘以对应的 $|h|,|h'|$ 范围即可；$hH'$ 项使用 (18) 第一式。这是固定 lift 的误差核算，不改变 lift 系数。

特别地，R48 完整参考补偿是
$h=a\chi$、$h(I_{\rm new}-E I_{\rm old})$，其系数为 1；不能误乘材料核心或旧 raw 核的圆化参数 $\lambda$。可以沿用 R36 的 lift 余项合并方法，但常数必须由这一次固定参数重新计算。

有限三角函数可保留 Laurent 代数，也可用可靠局部三角函数包围。对 elementary basis 使用解析导数，不等于假设整个图在径向节点有三阶导数。缺陷的系数相消应在范围膨胀之前完成；真实背景与近似背景若不相同，其差须保留。

### 5.3 核心只需位置与二阶材料 jet

R53 材料曲率核心的 $\phi,\Gamma$ 由真实积分定义，且

$$\Gamma'=i e^{i\phi},\qquad \Gamma''=-\kappa e^{i\phi}.\tag{19}$$

故范围来自 $\phi,\kappa$ 的范围及 $\Gamma$ 的真实积分包围，不需要 $\kappa'$ 或 $\Gamma'''$。旧 support/raw 核可在正速度下用真正的根区间包围单调弧长反函数，再代入已知二阶 jet；方法可参考 R36，数值常数不能照搬。

积分可用区间 Riemann 和、区间多项式或带已证余项的求积。常数遵从原源定义，例如原按精确十进制解释的宽度不能一律改成相邻 binary float。(4) 要求实际连续函数范围，不是密集采样极值。

### 5.4 同一个 mean primitive 是对象的一部分

设完整图为 $F=P+m(s)e_3$。若原对象采用固定 $K$ 个计算角节点的均值

$$
\mu_K(s)=\frac1K\sum_{\nu=0}^{K-1}W_z(s,2\pi\nu/K),
\qquad
m(s)=m_0+\int_{s_0}^{s}\mu_K(r)\,dr,
\tag{20}
$$

认证始终使用同一个 $K,m_0,W$。原 mean_nodes 为 512 时，审计角网格升至 1024 不允许把 $\mu_{512}$ 换成 $\mu_{1024}$。实际 jet 为

$$
\begin{split}
 F_s&=P_s+\mu_K e_3,& F_\psi&=P_\psi,\\
 F_{ss}&=P_{ss}+\mu_K'e_3,&
 F_{s\psi}&=P_{s\psi},&
 F_{\psi\psi}&=P_{\psi\psi}.
\end{split}
\tag{21}
$$

必须给出连续 $\mu_K,\mu_K'$ 范围；有限径向表、梯形累计量或几个高度查询都不足够。$m_0$ 也不是新增的接缝自由参数。

对于当前来源中的分离表示

$$
P=G_{\rm bg}(s,\psi)
 +q\sum_jY_j(s)B_j(\psi)+h(s)H(\psi),
\tag{22}
$$

径向 $Y,h$ 为 $C^2$，$B_j,H$ 的角向二阶 jet 已给出。即使 $Y'''$ 跳跃，

$$
\partial_sP_{\psi\psi}
 =(G_{\rm bg})_{s\psi\psi}
 +q\sum_jY_j'B_j''+h'H''
\tag{23}
$$

仍由该表示直接定义并连续。若背景的该 mixed jet 已给出，(23) 不要求 $Y'''$ 或 $H'''$。原 Frenet 速度 $W$ 对 $s$ 的求导只涉及这些 mixed jets、profile 相应二阶量和原正的 Frenet 分母；原域门内可逐项区间求值，再按固定有限和求得 $\mu_K'$。这是利用实际分离表示的附加结构，**不是**声称任意 $C^2$ 函数都拥有全部三阶 mixed jets。

若对象定义的是连续角均值 $\mu_\infty=(2\pi)^{-1}\int W_z\,d\psi$，就必须包围该积分和同一个 $W_{z,s}$ 积分。连续区间范围给收敛 Riemann 包围，不要求高阶求积导数。

若实际高度函数定义为某个有限 Gauss 查询公式，不能未经证明就把其导数识别为 (20) 的 integrand。应对那个实际函数求导并支付差，或使用原本已声明的连续 primitive 及其可靠求值误差。改变 mean 定义是在改变图，不属于加密验证。

必要时可用精确代数改善 mean 相消。在原取向和 $\sigma=1$ 的 Frenet 域内，写
$W=\alpha N+\beta B+vP_\psi$、
$\beta=\sqrt{1-\alpha^2}$，选背景
$\beta_0=\sqrt{1-a_s^2}>0$，则

$$
W_z-\beta_0
=\alpha N_z+\beta(B_z-1)
 +\frac{a_s^2-\alpha^2}{\beta+\beta_0}
 +v(P_\psi)_z.
\tag{24}
$$

若 $B_z>-1$，还可用
$B_z-1=-(B_x^2+B_y^2)/(1+B_z)$。
这些恒等式使用实际正交 Frenet 标架，不要求 $|F_\theta|=a$。若选取的背景不是实际目标，只能把 (24) 当计算组织，不能删去实际背景缺陷。

## 6. 不求完整 Rtheta 的 C² 标量积分备选界

此节给一个连接已有全 Frenet 残差引理的连续充分条件。它通常比定理 1 的直接矩阵界保守，但不需要 $R$ 的角向高阶导数。

先取同一 native 弧长目标 $\sigma=1$，并保持实际角向速度非零。令

$$d=P_\psi,\quad d_\psi=P_{\psi\psi},\quad
t=P_{s\psi},\quad v=\tau/\rho.$$

固定材料角的径向导数为 $\partial_s-v\partial_\psi$。定义
$u=|F_\theta|/a=|d|/(a\rho)$。
由 $\rho_s=(v\rho)_\psi$ 及坐标导数的交换，

$$
\boxed{\quad
(\partial_su)_{\theta}={\cal U}:=
 \frac{
 a\,d\cdot t-a v\,d\cdot d_\psi
 -(a v_\psi+a_s)|d|^2
 }{a^2\rho|d|}.
\quad}
\tag{25}
$$

这是实际 $C^2$ 场的恒等式，不先假设 $|F_\theta|=a$。它等于
$[T\cdot F_{s\theta}-(a_s/a)|F_\theta|]/a$，
其中 $T=F_\theta/|F_\theta|$。
mean 与角无关而准确消去；moving-chart 两项 $-v_\psi d-vd_\psi$ 均保留。

对每个径向区间 $I_j$ 与全角盒的交叉，若区间求值得到
$U_j\ge\sup_{I_j\times S^1}|{\cal U}|$，
且实际入口有
$b_0\ge\sup_\theta|u(s_0,\theta)-1|$，则

$$b_j=b_0+\sum_{i\le j}|I_i|U_i\tag{26}$$

在前 $j$ 个径向区间每一点包围 $|u-1|$。证明是沿每条固定材料角曲线积分，再用全角上界覆盖它；无需在计算 $\psi$ 中追踪该曲线。(26) 是有连续 integrand 范围支持的上 Darboux 和，不是径向梯形近似。$b_0$ 来自实际入口场；核心单位速度不能消除未支付的有限 inlet BC 残差。

在同一正的实际 Frenet 域内，取 $V$ 为原单位法向速度，明确使用材料径向残差
$R=(\partial_s-v\partial_\psi)F-V=P_s+m'e_3-(V+vP_\psi)$，并验证
$r_j\ge\sup_{I_j\times S^1}|R|$。已有恒等式给

$$
|g_{ss}^F-1|\le2r_j+r_j^2,\quad
|g_{s\theta}^F|/a\le r_j(1+b_j),\quad
|g_{\theta\theta}^F/a^2-1|\le2b_j+b_j^2.
$$

因而连续相对算子误差不超过

$$
\max\left(
 2r_j+r_j^2+r_j(1+b_j),\
 2b_j+b_j^2+r_j(1+b_j)
\right).
\tag{27}
$$

(25) 的分子可先代数相消再作区间范围，无须经 DFT 求完整 $R_\theta$。有限采样的 $U_j,r_j$ 仍不能替代连续上界。真实目标若与 native profile 不同，须用主定理的真实 $G$，或另外支付已证度量传递，不能直接沿用 (27)。

## 7. 与实际场和完成标准的关系

实际 $\lambda=.02$ 场的 R 壳诊断已经执行：它区分物理五次场的径向投影残差和角向补空间，并比较 (25) 的同一标量与 DFT 切向投影。这些是用于选择表示空间的浮点诊断；本条没有把它们升级为 (4)、(7)、(20) 或 (26) 的连续区间输入。

本方法的最小可验证输入是：

- 同一实际图的中心一阶 jet 和全盒二阶 jet 范围；
- 同一真实 $G$ 的中心值、一阶导数范围和正定归一化范围；
- 同一 mean primitive 的实际导数及必要二阶 jet 范围；
- 精确或带可靠误差的缺陷多项式系数和有限个 $2\times2$ 矩阵上界。

保留五次/有限 Laurent 部分，只对非多项式余项局部包围，并先消去背景，是为了让盒数反映真正缺陷的变化，避免两个大而接近的 Gram 项相减主导误差。定理 2 证明严格余量下该组织没有永久的坐标过估计；它不预言当前候选具有该余量。

新的低加速度 profile、圆弧窗口或振幅参数一旦选定，必须为那一个固定 $g$ 和实际图重新生成输入。一个前缀的连续度量门即使通过，也仍须继续支付真实尾、闭合族、全 $t$ reach、握持比例和固定参数加密要求。

## 来源

- [R31：实际闭合 M16 图的连续度量](R31-continuous-metric-of-the-actual-closed-m16-map.md)：共享二阶 jet、完整 Laurent/Bernstein 运算及真实 profile 的目标传递。
- [R36：raw 核真实积分和度量传递](R36-raw-core-true-integrals-and-metric-transfer.md)：一阶 jet 的 Gram 误差传递；不复用旧参数的数值界。
- [R39：积分核心的径向预算](R39-integral-core-radial-metric-budget.md)：旧候选条件预算，不是新参数常数。
- [R48：完整参考补偿](R48-exact-reference-compensation-for-mode-extension.md) 与 [R49：真实 mean 的参考转移不变性](R49-frenet-mean-invariance-under-exact-reference-transfer.md)。
- [R53：材料曲率圆化核心](R53-material-flattening-homotopy-and-positive-domain.md)：真实积分和二阶材料 jet。
- [完整 Frenet 残差到度量的界](../notes/2026-11-20-n4-full-frenet-residual-metric-bound.md) 与 [实际 R/Rtheta 壳诊断](../notes/2026-11-20-n4-readonly-full-residual-shell-entry.md)：同一实际 C² 场及固定 mean 约定。

