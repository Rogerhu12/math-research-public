# R133：同一真实正帽的径向衰减及增长解析角宽

**已证明。** 取[完整非零中心驱动帽](R133-supplement-complete-nonzero-centred-cap-with-interface-jumps.md)
在 $[1,25/8]$ 上已证明的解族，并选择三个准确外输入
$d_{\ne0}(25/8)=B_0(25/8)=c_0(25/8)=0$。这是该真实解族的一个成员，
不是未经证明的 nonlinear regular 条件。对这个成员，完整
$|\eta|\le10^{-9}$、全角圆及全部 primitive 尾下，有

$$
\boxed{\quad
\sum_{m\in4\mathbb Z}e^{.06901529|m|}
 \left(|\widehat B_m(25/8)|+|c_m(25/8)|\right)
 <7.034794836\cdot10^{-10}.
\quad}
\tag{S.1}
$$

这里 $C=C_r+c$，并非把整个非零旋转曲率 $C_r$ 计为小量。
其间真实所有模式已在解中，不是对有限候选外迹的外推。
本篇只证明曲率的强筛选；height/flux 的完整转换、周期框架和真实另一端
regular/label 条件仍须接入。

## 1. 随半径增长的解析权

令 $L=3/2$、$R=25/8$、$s(r)=a(r)/a(L)$。实际整个后缀 $a'<0$，
所以 $0<s\le1$。对准确正数 $\mu,\tau$ 定义

$$
W_m(r)=s(r)^{\mu+\tau|m|},\qquad
\sigma(r)=\tau\log\frac{a(L)}{a(r)},
\quad
\|u\|_{\mu,\tau}
 =\sum_m\sup_{[L,R]}\frac{|u_m(r)|}{W_m(r)}.
\tag{S.2}
$$

pair 范数仍为 $B$、$c$ 两项之和，mean $m=0$ 使用同一径向权 $s^\mu$。
这是完整加权 Fourier Banach 空间。因为
$|m+n|\le|m|+|n|$ 且 $0<s\le1$，

$$
\frac{W_mW_n}{W_{m+n}}
=s^{\mu+\tau(|m|+|n|-|m+n|)}\le1.
\tag{S.3}
$$

故卷积乘法有范数常数1。径向有界标量是乘子。常数函数1在此范数下不必具有
范数1；下文不对逆函数单独使用这种说法，而把 $Q$ 展为从二次项开始的完整级数。
于是对于 $\|U\|_{\mu,\tau}\le\rho<C_*:=\inf|C_r|$，仍有

$$
\|Q(U)\|_{\mu,\tau}\le\frac{\Lambda\rho^2}{C_* -\rho},
\quad
\|DQ(U)\|\le\Lambda\left(
\frac{2\rho}{C_* -\rho}+\frac{\rho^2}{(C_* -\rho)^2}\right),
\qquad \Lambda\ge\max(1,\sup\ell).
\tag{S.4}
$$

这来自 $Q=(B^2+\ell c^2)C_r^{-1}\sum_{j\ge0}(-c/C_r)^j$，
每一项至少有两个受控场因子。没有遗漏商展开的无限尾，也没有截断未知高频。

## 2. 加权全频三角系统及 mean

保留完整真实 R74 regular 比值 $q_m(r)>0$，令 $b_m=i\operatorname{sgn}(m)\widehat B_m$、
$d_m=b_m+q_mc_m$。对 $m\ne0$、$M=|m|$，置
$\bar d_m=d_m/W_m$、$\bar c_m=c_m/W_m$、$\bar Q_m=Q_m/W_m$。
由 $W_m'/W_m=(\mu+\tau M)\beta$ 和原准确三角系统，

$$
\begin{aligned}
\bar d_m'&=
 \left[M(\gamma q_m-\tau\beta)-(2+\mu)\beta\right]\bar d_m
 +(-M\gamma+q_m\beta)\bar Q_m,\\
\bar c_m'&=M\gamma\bar d_m
 -\left[M(\gamma q_m+\tau\beta)+\beta(\ell+1+\mu)\right]\bar c_m
 +\beta\bar Q_m.
\end{aligned}
\tag{S.5}
$$

第一行从 $R$ 向内积分，第二行从 $L$ 向外积分。两个 mean 准确满足

$$
\bar B_0'=-(2+\mu)\beta\bar B_0,
\qquad
\bar c_0'=-\beta(\ell+1+\mu)\bar c_0+\beta\bar Q_0.
\tag{S.6}
$$

它们都按指定的外输入向内解，$c_0$ 的非线性积分不被删除。

写 $t=-\beta/\gamma>0$。每一个真实闭盒上保留已证的全频区间
$q_\ell\le q_m\le q_u$。对所有 $M\ge4$，C 行的归一率下界为

$$
\delta_C=q_\ell-t\left(\tau+\frac{\ell+1+\mu}{4}\right)>0,
\tag{S.7}
$$

其中右侧整式按实际区间运算取下界。D 行归一率至少 $q_\ell+\tau t>0$。
实际系数有变化，所以仍采用逐点正核比估计，而不把整个区间长度乘入。
可用的核常数为

$$
\begin{aligned}
T&=\sup\delta_C^{-1},\quad
K_C=\sup\frac{t}{4[q-t(\tau+(\ell+1+\mu)/4)]},\\
K_D&=\sup_{y\in\{0,1/4\}}
 \frac{1+qty}{q+\tau t+(2+\mu)ty},
\quad K_0=\sup\frac1{\ell+1+\mu}.
\end{aligned}
\tag{S.8}
$$

第三式确实控制所有频率：对固定真实 $q,t$，该比值是 $y=1/M$ 的分式线性函数，
其导数符号固定，所以 $0\le y\le1/4$ 的最大值在两个端点。
端点各自在完整 $q,t$ 区间上包络，而非抽样。

令 $q_+=\sup q_m$，则全部非零分量及 mean 的完整源核为

$$
H_C=1+q_+,\quad H_D=1+(1+q_+)T,
\qquad K=\max\{K_0,H_DK_D+(1+q_+)K_C\}.
\tag{S.9}
$$

这同时支付由 D 源驱动 C 的三角项。当前外输入准确为零，故线性边界预算
只有 $H_C\|c_{\ne0}(L)\|_{A_0}$。增长角宽在 $L$ 恰为零，所以不预先要求
内端无限数据有正解析宽。

## 3. 真实内侧数据及同一分支识别

不能只把有限中心在 $L$ 的值代入。既有完整帽给真误差
$e<5.407903434\cdot10^{-5}$；完整中心在准确 $L=3/2$ 的有理 Horner 求值给

$$
\|\widehat c_{\ne0}(L)\|_{A_0}<1.192912691\cdot10^{-5},
\quad
\|c_{\ne0}(L)\|_{A_0}<6.600816124\cdot10^{-5}.
\tag{S.10}
$$

后者是整个真实解的内端预算，允许无限高模。同时，在后缀全部准确三次片上
逐模取最大值，得到

$$
\|\widehat B\|_{X_0,[L,R]}<1.244997375\cdot10^{-5},
\quad\|\widehat c\|_{X_0,[L,R]}<1.203396113\cdot10^{-5},
$$

因此原实际解后缀的完整 pair 范数小于 $7.856296921\cdot10^{-5}$。

在加权空间以 (S.10) 的真正数据构造固定点后，仍须证明它就是原解。
同一实际系数另取 $\mu=\tau=0$，在未加权球 $\rho=.0004$ 上得到完整
Lipschitz 常数小于 $.039082458$。新加权解的未加权范数至多 $.0004$，
原解后缀也在这个球内。两者满足相同四输入的真实积分方程，故其差范数
不超过 $.039082458$ 倍自身，因而准确相等。这一步没有把“另一个小解”
直接当成已证分支。

## 4. 实际闭盒核验与严格结果

实际选

$$
\mu=\frac32,\quad\tau=\frac1{128},\quad\rho=\frac1{2500}.
\tag{S.11}
$$

原真实系数/native 与其已证全频 Riccati 后缀提供 **663 个完整闭盒**，
包含原 body/graft 接缝、全部 scalar germ 和真正 regular 入口。
逐盒 (S.7) 全部严格为正。完整有向算术给

$$
\begin{gathered}
q_+<1.059751811,\quad T<33.105584,\quad
K_D<1.051862,\quad K_C<8.327667,\quad K_0<.293223,\\
H_C<2.059751811,\quad H_D<69.189285,
\quad K<89.930493,\quad C_*>.1705338016608,\quad\Lambda<1.097170317.
\end{gathered}
\tag{S.12}
$$

由 (S.4)、(S.9)、(S.10)，球像和完整未知导数为

$$
H_C\|c_{\ne0}(L)\|_{A_0}+K\frac{\Lambda\rho^2}{C_* -\rho}
 <.000228752400<.0004,
\quad
K\sup\|DQ\|<.464505257<1.
\tag{S.13}
$$

Banach 收缩给完整加权解；§3 把它准确识别为原实际解后缀。
其 $\theta$ 全解析正则在每个 $r>L$ 都由 (S.2) 直接得到。

原真实端点半径另给

$$
\frac{a(R)}{a(L)}<.000145700473512,
\quad \sigma(R)>.0690152937098,
\quad s(R)^{3/2}<1.758698709\cdot10^{-6}.
\tag{S.14}
$$

于是 (S.2) 与半径 $\rho$ 给 (S.1)。如只需要更小外迹，固定点还满足实际
球像界 $.000228752400$，可再乘同一个径向权得到更紧数值；该推论不需要
另一次 PDE 求解，也不修改管半径。

为了明确角宽和径向衰减的取舍，同一源还实际算过
$\mu=4/3,\tau=1/64,\rho=.0004$：其完整收缩小于 $.219737844$，
外宽大于 $.138030587419$，外解析曲率小于 $3.066723414\cdot10^{-9}$。
两组都是真正全频结果；(S.1) 采用前一组更强径向衰减。

## 5. 执行对象与下一接口

源为 `scripts/fourfold_codazzi_cap_radial_analytic_screening.py`。实际报告为

- `notes/2026-11-13-R133-cap-analytic-screening-r15-mu3halves-native.json.gz`；
- `notes/2026-11-13-R133-cap-analytic-screening-r15-mu4thirds-native.json.gz`。

报告保存全部663闭盒的真实率与核、原完整正帽/中心/接口报告的身份、真误差预算、
完整逐模式后缀界、同一解识别和两次实际算术结果。数值计算只消费原已证明的
whole-$\eta$/whole-angle/full-primitive 系数界，新的指数、对数、分式与有限
中心系数均用有向算术；没有靠角采样宣称解析全频界。

本篇选择的 $d_R=0,c_0(R)=0$ 不是完整 nonlinear regular 图。
下一步应把小解析非零 $C_R$ 送入真正 R119 Dirichlet-to-curvature map 的局部逆，
保留它输出的 $B_R$、$C_0(R)$ 和平均高度，再与正帽的外端口联立。
在完整物理第二形式两迹实际一致之前，不授周期 holonomy 或闭面结论。
