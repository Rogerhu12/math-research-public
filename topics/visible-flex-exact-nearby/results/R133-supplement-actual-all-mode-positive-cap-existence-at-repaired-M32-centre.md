# R133 续篇：修补 M32 中心附近的实际全模正帽解

2026-11-15，visible-exact / root。

**已证明实际局部存在、闭球内唯一及解析参数依赖。**
同一固定 $\eta_0$、ac1 候选的 440866 连续修补中心，在真实帽区间
$[9/10,25/8]$ 上，具有下面明确边界数据域中的完整非线性曲率解。
实际公开运行已经支付先前端点定理唯一缺少的加权系数门。
这里没有把有限 Fourier 截断解冒作全模解，也没有把本帽的存在
提升为尚未匹配的闭曲面族。

## 1. 对象与已支付证据

中心 $\widehat W=(\widehat B,\widehat C)$ 使用
[连续中心与真实物理残差](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md)
的原定义。完整身份为：

- 原候选 SHA256：ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413。
- 连续修补定义 SHA256：440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47。
- 固定 $\eta=\eta_0,\delta=0$，原 intrinsic 数据、$\alpha,\nu$ 和真实物理角 $\theta$ 不变。
- 帽为 $I=[L,R]=[9/10,25/8]$；此处 $L$ 是帽的左端，不是长段长度。

解析部分是
[完整加权端点定理 E.1--E.23](R133-supplement-weighted-Q-endpoint-invariance-and-small-analytic-cap-ball.md)，
SHA256 0e6c0f6acfa4a40378176cf56e03ee941d1932885149a64cd145a7b4e9b91cfe。
其普通源与完整非线性代数来自
[物理帽 L1 主体证明](R133-supplement-physical-cap-L1-Wiener-sources-and-practical-nonlinear-body-ball.md)，
原积分已由公开运行 43692857656/1 支付。

新增实际证据为
[43695160055/1 的完整加权消费报告](R133-supplement-actual-cached-weighted-cap-Q-and-endpoint-margins.md)，
SHA256 ef8013989ea063657e9636415719fdf6fa27f8484765022d73d7361bc00d8d7a。
该运行 child return code 0，21/21 门通过，科学程序实际用时
1.277747273000017 秒。原 process SHA256 为
3034426e40730fb3e6b880df66e551b4b0b158ecd178b833e532dfe07bfe18fb；
完整小结 SHA256 为
c0b2ba3c7c51f64c602f94951144dae92057dbedc7ef0ea3b83ed1a88a50fdb4。

其中准确的联合范数先对每个 Fourier 系数取全径向 supremum，再求和。
包含全部正负频率和已知 $Q_C$ 的非零 mean；实际门为
$$
 q_w=\max\{\|wQ_B\|_{\mathscr A_\sigma},
                  \|wQ_C\|_{\mathscr A_\sigma}\}
 <3.561348304031\,10^{-6}<10^{-5},\qquad
 K_e<4.898174641284<5 .
 \tag{X.1}
$$
完整原尾、真实 outer、连续修补与两均值的费用均已在原报告内。
唯一新数学是原 mean cubic 在1346个共同闭格上的 Bernstein 范围及
新加权组合；所有旧 target、全卷积、L1 积分、Riccati 和物理端矩均未重算。

本篇消费这些已成数字和 E 的证明；没有再次运行数学程序。
消费者本身保留的 false scope 标志是该有限消费者的原范围，
本篇的全模存在性来自下面对完整解析定理的应用。

## 2. 完整空间与真正独立的边界数据

取
$$
 \sigma=\frac1{8192},\qquad \rho=3\,10^{-6},\qquad
 \zeta=9.9\,10^{-10},\qquad \bar Z=10^{-9}.
 \tag{X.2}
$$
$X_\sigma$ 是逐系数连续函数的加权 $\ell^1$ pair 空间：
$$
 \|x\|_{X_\sigma}
 =\sum_{k\in4\mathbb Z}e^{\sigma|k|}\sup_{r\in I}|b_k(r)|
  +\sum_{k\in4\mathbb Z}e^{\sigma|k|}\sup_{r\in I}|c_k(r)|,
 \qquad x=(b,c).
 \tag{X.3}
$$
取共同反射子空间，$b$ 奇、$c$ 偶。复化保这个线性 parity，
不把复系数与复共轭混为一谈。实解另加通常的实共轭条件。
没有未知 Fourier cutoff；$C$ mean 保留在 (X.3) 内。
$B$ mean 为0是指定反射类的准确结论。

独立输入为
$$
 \gamma=P_{\perp,\theta}(C(L)-\widehat C(L)),\qquad
 \|\gamma\|_{A_\sigma}\le10^{-9},
 \qquad
 \|f_B\|_{\dot A^2_\sigma}\le2^{-60}.
 \tag{X.4}
$$
$\gamma,f_B$ 都是偶、四重周期、非mean数据。
$f_B$ 是原长段另一端的归一非mean高度；
其物理高度为 $s_Bf_B$，$s_B=a_Bw_B>0$。没有把 $s_B$ 设成1。
(X.4) 不指定帽左端的 $B$、$C$ mean、平均高度或相位。

帽右端采用同一个真实非线性长段曲率图。给定
$$
 Z=P_{\perp,\theta}(C(R)-C_{\rm ref})
       =Z_0+c_{\ne0}(R),
 \tag{X.5}
$$
该图给出真实 $B(R)$、独立 $C_0(R)$ 及其 holonomy mean，
保持原有限长段反射、regular multiplier 和完整非线性项。
它不是额外把右端 mean 置零的线性 Robin 替代。
原图的定义域是 $\|Z\|_{A_\sigma}<\bar Z$ 与 (X.4) 的高度域。

## 3. 实际的压缩自映射

令
$$
 {\cal B}=\{x\in X_\sigma:\|x\|_{X_\sigma}\le\rho,\
                   \|c_{\ne0}(R)\|_{A_\sigma}\le\zeta\}.
 \tag{X.6}
$$
它含0，是完整 Banach 空间中的闭集；右端 evaluation 连续。
实际已知端值满足
$$
 \|Z_0\|_{A_\sigma}<2.696354530653\,10^{-13},
 \qquad \|Z_0\|+\zeta<10^{-9}.
 \tag{X.7}
$$
所以整个 $\mathcal B$ 中的真实 outer 都有定义，
不是先在域外求值后再声称端点很小。

$\mathcal T_{\gamma,f_B}$ 取 E.21 后定义的准确两端 reference Green：
施加已知真实残差、完整线性 $Q$ 列、精确二次余项以及真实 outer
非线性差；独立 $C$ mean 按同图的 mean 行确定。
对 $u=\widehat B/\widehat C,\ v=1/\widehat C$，准确二次项为
$$
 {\cal R}_Q(b,c)
 =\frac{b^2-2ubc+(Kv^2+u^2)c^2}{\widehat C+c},
 \qquad
 \|{\cal R}_Q(x)\|<13\|x\|^2 .
 \tag{X.8}
$$
分母、全卷积及 mean 都在该式中。E.9 的同一端点核给
线性加权费用 $10^{-4}\|x\|$，二次费用 $65\|x\|^2$。
未知二次源没有被假设具有额外径向衰减。

原已成实际全源小于 $3.208341026859\,10^{-7}$，完整线性和
outer 反馈系数小于 $0.878289249280$。使用 E 已证明的宽整数预算，
对整个 $\mathcal B$ 有
$$
 \|\mathcal T_{\gamma,f_B}x\|
 <3.23\,10^{-7}+.879\rho+208\rho^2
 =2.961872\,10^{-6}<.99\rho ,
$$
$$
 \|\mathcal T_{\gamma,f_B}x-\mathcal T_{\gamma,f_B}y\|
 \le(.879+416\rho)\|x-y\|
 =.880248\|x-y\|,\qquad {\rm Lip}\,\mathcal T<.881 .
 \tag{X.9}
$$
真实右端的全部反馈同时满足
$$
 \|(\mathcal T_{\gamma,f_B}x)_{C,\ne0}(R)\|
 <3\,10^{-14}+10^{-4}\rho+65\rho^2+\zeta/200
 =8.8998\,10^{-10}<.9\zeta.
 \tag{X.10}
$$
这里 known ordinary、未知 linear $Q$、未知 quadratic $Q$、
完整 outer 四部分各有明确项。$C$ mean 在主体及 true outer 中另保，
不被冒作非mean端点源。以实际 (X.1) 代替宽阈值还能得到
$6.827271113222\,10^{-10}$ 的上界，但存在性只需要 (X.10)。

因此 $\mathcal T_{\gamma,f_B}:{\cal B}\to{\cal B}$ 是严格压缩。
Banach 定理给唯一 $x_{\gamma,f_B}\in{\cal B}$，
并且
$$
 \|x_{\gamma,f_B}\|_{X_\sigma}<.99\rho,\qquad
 \|(x_{\gamma,f_B})_{C,\ne0}(R)\|_{A_\sigma}<.9\zeta .
 \tag{X.11}
$$
唯一性只在这个已证明的闭球和同一边界数据内陈述。
所有未知 Fourier 模均参加固定点方程。

## 4. 固定点确实解原非线性曲率方程

reference Green 是原两行物理 Codazzi 系统的准确双端解算子。
E 中的 $Q_Bb+Q_Cc+{\cal R}_Q(x)$ 是同一原 Gauss 分式的
精确差，没有截去更高阶项。已知残差采用连续修补后的真实
物理残差，其与 correction 方程的相反源逐项相消。
故
$$
 W_{\gamma,f_B}=\widehat W+x_{\gamma,f_B}
 \tag{X.12}
$$
满足原固定 intrinsic 数据的完整 Gauss--Codazzi 系统，
(X.4) 的左非mean条件，以及 (X.5) 的真实右曲率图。

原已证 $\|1/\widehat C\|<6$ 且 $\|c\|\le\rho$ 给
$\|c/\widehat C\|<6\rho<1$。Gauss 分母在整个复球内不为0；
对实参数，$C$ 保持中心的负号。于是原代数与 reference 的还原合法。

固定点首先由连续系数的完整积分方程构成。
在任何严格较小角条带上可逐项求角导；
真实 target 具有相应光滑性的径向区间，由原等式恢复径向导。
人工 cubic 分格的中心残差和校正对应项准确相消，
不留下实际 Codazzi 跳跃。
这个论断不提高真实 graft 本身的已指定正则性，
也不代替其他物理接缝的验证。

取 $x_0=0,\ x_{n+1}=\mathcal T_{\gamma,f_B}x_n$，数学上有
$$
 \|x_n-x_{\gamma,f_B}\|_{X_\sigma}
          \le\rho(.881)^n .
 \tag{X.13}
$$
(X.13) 是完整算子的收敛证明；本文没有宣称已经数值执行了这些迭代，
更未把它作为新近似曲面的计算收据。

## 5. 参数依赖和合法的小条带导数

所有分母及真实 long 图在相应复偶参数球内解析，
(X.9) 的收缩常数对参数统一。逐次迭代全纯并局部一致收敛，
所以 $x_{\gamma,f_B}$ 在
$\|\gamma\|<10^{-9},\|f_B\|_{\dot A^2_\sigma}<2^{-60}$
内为 Banach 空间值全纯函数；在闭域连续。
实参数产生实对称解。

固定 $f_B$ 时，改变 $\gamma$ 只改变原 $H_C<3$ 的左数据列。
比较两个完整固定点可得
$$
 \|x_{\gamma_1,f_B}-x_{\gamma_2,f_B}\|_{X_\sigma}
 \le\frac3{1-.881}\|\gamma_1-\gamma_2\|_{A_\sigma},
 \qquad \frac3{1-.881}<26 .
 \tag{X.14}
$$
在高度半球 $\|f_B\|_{\dot A^2_\sigma}\le2^{-61}$，
完整原半径 $2^{-60}$ 允许任意相容偶方向的 Cauchy 圆盘，
因此
$$
 \|D_{f_B}x_{\gamma,f_B}\|_{\dot A^2_\sigma\to X_\sigma}
 \le 2^{61}\rho<2^{43}.
 \tag{X.15}
$$
同一半球凸，故也给这个域内的 Lipschitz 界。
(X.15) 使用归一高度；若改为物理高度方向，必须保留 $s_B^{-1}$。

对每个整数 $q\ge0$，完整 Fourier 级数及
$t^q e^{-t}\le q!$ 给
$$
 \|\partial_\theta^q x_{\gamma,f_B}\|_{X_{\sigma/2}}
 <q!\left(\frac2\sigma\right)^q\rho .
 \tag{X.16}
$$
此处的范数是同样逐 Fourier 模的 joint norm。
(X.16) 是 correction 的界；整个 $W$ 还须加已知中心的对应导数。
它不授原高 Sobolev 帽证明所需的极小 $M_{8212}$ 邻球，
也不把物理角宽 $1/8192$ 扩为尾部标签的大宽。

## 6. 后续真实端口必须继续联立

本篇实际付清此前 E.12 条件，因此当前反射类的局部正帽曲率解
已经存在。此时仍保留的实际输出包括 $B(L)$、$C_0(L)$、
内端 mean 高度/通量和相位。它们未被预设为与另一段相同。

将右曲率图读成真实长段 Dirichlet 高度、有限长段 far 标签方程、
内帽到 mixed-body 的全部端列，以及共同 mean 高度只允许的一个
$\lambda$，都须按原完整匹配方程使用。
帽未知量的 moving 读出仍须用真实 $C$ mean、primitive 和 inverse angle，
不能授任意零宽函数免费同阶组合。

全部无限反馈、强返回与 cutoff、真实 $\nu$ Schur、两相位的同对象约束、
闭合与嵌入、held/reach 和四 marker 仍是独立全局完成门。
本篇没有把已知仿射 $Q_\delta$ 称为全族 PDE 解，
也没有以局部帽存在代替 README 的精确闭等距族。
