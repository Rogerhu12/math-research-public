# R65. R53 端点的无限维核、有限解析切向的单射性与暖转接

2026-11-26，`Astra-held10-06bbeb39-20261126 / fixed_metric`。

本文证明当前 `curvature_blend=1` 的 R53 材料圆化映射确有一个
无限维端点核，同时证明这个事实不意味着任一有限 support Fourier
参数 Jacobian 在 lambda=1 自动秩亏。本文还给出从实际已接受核心到
补弧材料曲率控制族的等几何交接公式。

**没有计算本次实际 BVP Jacobian 的条件数，没有 near-1 新接受场，
没有新闭曲面或完成结果。** 新族保留一个实际锚点及完整 g；它不是
旧有限参数族的可逆换基，也不能追认 R52 的旧 cold 失败。

## 1. 固定目标曲率时的准确线性算子

固定一个周期 P=2pi/3、R53 的完整材料窗口 chi，记 W=1-chi。
chi 在保护弧内部恒为1，W在非空补弧开集上为正。固定目标圆曲率k。
R53 的归一化为

\[
\kappa_\lambda=(1-\lambda\chi)\kappa_0+\lambda\chi k
                  +\lambda W\beta,
\qquad
\beta=\frac{\int_0^P\chi(\kappa_0-k)\,du}{\int_0^P W\,du}.
\tag{1}
\]

所有旧核心周长及每周期转角固定，因此其材料曲率切向 r 满足
int r=0。固定k、窗口和lambda后，(1)的导数是

\[
T_\lambda r=(1-\lambda\chi)r+
 \lambda W\frac{\int\chi r}{\int W}.
\tag{2}
\]

由 int r=0，也可写成

\[
T_1r=W\left(r-\frac{\int Wr}{\int W}\right).
\tag{3}
\]

这些是材料曲率函数上的恒等式，不使用离散求积、参数缩放或
Newton 返回。若目标曲率随旧核心参数变化，则导数还有
lambda*chi*dk 与 beta 的相应项；本文不把那种情况混入(2)。

## 2. 无限维真核与 1-lambda 方向

取任意非零、光滑、偶且P周期的r，其支撑紧含于保护弧内部，
并使其周期积分为零。这样的空间无限维：在保护弧内选互不相交的
偶 bump，再用一条线性均值约束消去一个系数即可。
在r的支撑上chi=1、W=0，而int chi*r=int r=0，故

\[
\boxed{T_\lambda r=(1-\lambda)r.}
\tag{4}
\]

特别地 T1r=0。这些不是曲线刚体运动的重复参数，而是旧材料曲率
在会被端点圆化抹去的区域内的真实变化。对于任何满足
norm(c r)=|c| norm(r)的函数范数，(4)给出准确收缩因子1-lambda。

只要旧核心曲率严格为正，对足够小的实t，kappa0+t*r仍严格为正，
保留周期转角和反射性。按R52/R53的旋转闭合积分构造即可得到
真实单位速闭凸旧核心。因此这里的核方向属于实际允许的无限维
旧核心切空间，不是任意写下却不满足闭合的曲率扰动。

## 3. 有限 support Fourier 切向在端点仍单射

现在固定一个有限 support 核

\[
h(\phi)=1+\sum_{j=1}^M b_j\cos(3j\phi),\qquad h+h''>0.
\]

由于rho=h+h''是正的实解析函数，材料坐标
u(phi)=int_0^phi rho及其逆phi(u)均实解析。任何有限系数切向的
材料曲率变分r(u)也实解析，并满足int r=0。

若T1r=0，由(3)，r在W>0的一个非空开区间上等于常数。
实解析函数的恒等原理使r在整个连通材料圆周上等于同一常数。
其积分为零，故r恒为0。

还须说明r=0确实迫使support系数切向为零。材料切向角满足
phi'=kappa及固定规范phi(0)=0，所以delta kappa=0给delta phi=0。
单位切向Gamma'=i exp(i phi)的变分于是为零。旋转闭合规范

\[
\Gamma(0)=\frac{\int_0^P i e^{i\phi(u)}du}{e^{iP}-1}
\]

唯一决定常量，故delta Gamma也为零。其支撑函数及每个Fourier
系数的变分自然为零。这证明

\[
\boxed{\text{在每个固定有限M及正rho的原核上，端点核心映射的
support系数导数是单射。}}
\tag{5}

因此不能从保护弧上的局部导数为零，直接宣布当前M24或M32
全核心参数矩阵秩亏，更不能据此宣布完整Frenet/尾BVP不可解。

## 4. 为什么有限单射不提供统一稳定性

上述两个结论相容。取第2节非零光滑r，并令kappa_t=kappa0+t*r。
其单位速旋转闭合核心在小t时光滑且严格凸，可以写成具有同一
周长、旋转及反射规范的支撑函数h_t。令v=partial_t h_t at0。
它是光滑、偶、P周期函数，且其常数系数为零；后者来自
int h_t=int(h_t+h_t'')=2pi。

用cos(3j phi)的有限Fourier和v_N逼近v。光滑性给任意固定阶数的
一致导数收敛。正rho下，支撑函数到材料曲率的线性化依赖有限阶
导数和正的材料反函数，其在这些固定C^k范数间连续。因此有限
support切向诱导的r_N趋于r；例如取足够高阶的v_N收敛即可保证
r_N在C^0中趋于r。

(2)中的乘法和积分是C^0有界算子，所以T1r_N趋于0，而
norm(r_N)趋于norm(r)>0。由此不能给随M增长的完整有限support
切空间提供正的、独立于M的物理曲率下增益。对于lambda<1，
同样的逼近给

\[
\lim_{N\to\infty}
\frac{\|T_\lambda r_N\|_\infty}{\|r_N\|_\infty}=1-\lambda.
\tag{6}
\]

这是函数空间和截断增长的结构结论。对于固定M，(5)仍可能给
正的最小奇异值，并不要求它在lambda趋1时趋零。本文没有
给出当前M24/M32的数值大小、完整BVP的最小奇异值、Schur逆界，
或其具体停止原因。旧数值参数pscale=q^j又会改变普通矩阵条件数；
其影响不能与(6)的物理函数范数比较混为一谈。

## 5. 保留实际锚点的补弧材料控制族

设未来已有一个实际保存、被接受的near-1 R53场，旧support
参数向量为b*、同伦值为lambda*。冻结b*及原窗口、目标k，
对后续lambda定义原R53精确基准phase phi_base(u;lambda,b*)。
使用R52已定义的primitive

\[
\Psi_j(u)=\frac{W(u)\sin(3ju)}{3jN_j},\qquad
N_j=1+\frac{630}{256b(3j)},\qquad j=1,2,\ldots.
\]

令新的实际phase未知为d_j，定义

\[
\Phi(u;\lambda,d)=\phi_{base}(u;\lambda,b^*)+
                         \sum_{j=1}^M d_j\Psi_j(u).
\tag{7}
\]

每个primitive是固定的周期奇函数，在保护弧上连同需要的导数
恒为零。其曲率控制B_j=Psi_j'均值严格为零，且|B_j|<=1。
因此(7)保留旋转转角、反射和周长；只要完整曲率仍正，按原旋转
闭合积分给严格凸单位速核心。其完整位置和参数jets沿用R52：

\[
\partial_{d_j}\Gamma=
 -\frac{\int_0^P e^{i\Phi}\Psi_j}{e^{iP}-1}
 -\int_0^u e^{i\Phi}\Psi_j,
\quad
\partial_{d_j}\Gamma'=-e^{i\Phi}\Psi_j,
\quad
\partial_{d_j}\Gamma''=-e^{i\Phi}(B_j+i\Phi'\Psi_j).
\tag{8}
\]

在lambda=lambda*,d=0，(7)及完整旋转闭合积分与原实际核心
定义完全相同，故Gamma、Gamma'、Gamma''全函数相同，不仅
曲率相同，也不依赖拟合残差。在lambda=1，保护弧的曲率恒为
固定k，所有新未知都只修改补弧。这个新有限族通常不是原有限
support族的像；本条只声称锚点等几何和完整g保持。

核心变化不改变R63的目标g=ds²+a(s)²dtheta²。交接时冻结旧场
真实delta、完整桥与尾背景、角图和gauge。新函数空间的定义及
基准b*随后保持固定，不能在每次加密时重新挑b*来掩盖不收敛。

若交接还升M，使用已登记R48的完整lift传递

    Y_new = embed(Y_old) + a*chi_lift*(I_new-embed(I_old)).

系数为1。这里chi_lift是径向reference-lift窗口，与材料chi
不是同一对象。完整两jet按同一恒等式微分。R49继而保留同一
mean规则；不另设自由mean、常数高度或重新优化刚体。

## 6. 旧BVP接口的参数语义和准确链式

预备实现 `warm_supported_core_factory.py` 保持原gauge qg乘Y。
原fixed=True参数仍按代码令

    q_aux = q_seed * exp(p0),

其中在新族中q_aux仅是正的数值坐标载体，绝非旧物理support
主系数。取q_seed=qg，明确设置

\[
d_1=s\log(q_{aux}/q_g),\qquad
d_j=s\,c^{legacy}_{j-1}/pscale_{j-1}\quad (j\ge2).
\tag{9}
\]

factory返回的参数jets先逐列乘
[s/q_aux,s/pscale_1,...]。原fixed analytic Jacobian再乘
[q_aux,pscale_1,...]，结果恰为每列s。设计模式fixed=False的
p0仍是delta增量，此时q_aux固定、d1=0；固定g模式使用全部M个
phase未知。不能把新族的q_aux区间称作物理非零support幅度。
源字段和run种类必须显式标注新参数意义，不能无说明沿用旧
qbranch验收。默认预备scale为1；Y的gauge仍是旧值.06。
原WarpedBVP的1e-7<q_aux<.124坐标域仍保持；因此该适配器的
第一phase坐标覆盖s*log(1e-7/qg)<d1<s*log(.124/qg)，不是
无界的全局坐标。在qg=.06、s=1下，零交接点严格在内部，且
所有|d1|<.2都在该区间内。以后若实际步触及该坐标域，须如实
记录并另作明确的新坐标或重定中心，不能把它叫作曲率不可能性。

位置增量用

    i*exp(i*phi_base)*expm1(i*sum(d_j*Psi_j))

积分并按同一旋转闭合常量加回基准。d=0时该增量为literal零，
实现还直接委托原baseline的F/Ft/Ftt，避免把重新拟合或重新
求积的近似像称作等几何交接。核心正性仍使用原1e-5门槛；
三角界不足时采用已登记的完整曲率插值域守卫，不能放宽门。

## 7. 条件、旧失败及尚待实场的事项

R52材料q=.01/M8冷入口的真实失败已经登记在
`notes/2026-11-20-m3-material-first-terminal-and-cosine-entry.md`：
RMS约3.7868、节点预算终止、无实际尾调用。本路线保留一个
完整实际near-1解作为锚点，不重演该cold输入，也不转称那条
失败为接受。

预备factory通过了一个明确标成synthetic的接口检查：旧support
q=.06、七个零控制，lambda=.95、S=.5、b=.2、k=.2。零新控制的
F/Ft/Ftt在36个测试材料点均逐位相同；对原BVP参数0/3/7以1e-6
步长作中央差分，三jet最大差不超过2.96e-10；保护弧曲率变化
样本为0。这是新API及链式核对，**不是near-1 BVP场或转接执行**。
恒等式与圆弧性质由(7)—(9)证明，不由这些样本反推。
小检查入口为`check_warm_supported_core.py --repo REPO
--reference-source ORIGINAL_FIXED_METRIC_MODE3_CORE_PY`，不复制
70源到新生产目录，不启动BVP或尾求解。

直接R52窗口正弦基也可能在大M下有坐标病态。换族本身不证明
完整Jacobian良态。需要时可对同一个有限新span作明确可逆预条件；
R42的连续加权正交思想可用于奇primitive，再对其导数Gram
处理。任何数值预条件都不能丢列、变方程、变物理门，或冒称
尚未计算的Jacobian条件数。当前尚无实际near-1接受场，故未
生成新暖BVP输入、未运行新族求解，也未改变在跑的旧设计/真尾源。
