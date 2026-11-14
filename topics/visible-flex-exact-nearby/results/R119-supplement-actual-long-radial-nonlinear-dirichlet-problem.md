# R119 续篇：实际长径向段的全频非线性 Dirichlet 问题及 mean 输出

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 本篇在 R74 的同一未改长径向段 $0\le u\le B$ 上，
对全部非零 $4\mathbb Z$ 频率解一个真正的非线性两端 Dirichlet 问题。
得到精确旋转目标度量的 $C^2$ 嵌入、两端完整高度/径向迹、真实水平
重建以及不可删除的 mean 高度差和径向迹。常数不随长段长度增长。

本篇尚未把两个 Dirichlet 数据与 R119 的 tail+connector chart 及 R74
两个 bump 的全部非线性两迹联立。文末明确写出尚缺的实际算子方程；
不以这个已解 Dirichlet 问题代替 regular 高输入逆。

## 1. 同一实际径向段和归一化

使用 [R74 (74.2)–(74.4)](R74-actual-full-tail-robin-and-augmented-positive-cap.md)：
$$
 T=2^{24},\quad B=T-25/8,\quad
 7/5<\omega<3/2,\quad 0<a_*<7\cdot10^{-6},
$$
$$
 a(u)=a_*e^{-\omega u},\qquad z_u=a^2/4.
 \tag{D.1}
$$
令 $a_B=a_*e^{-\omega B}$，反向半径时间为
$$
 t=\log(a/a_B)=\omega(B-u),\quad
 0\le t\le L:=\omega B,
 \qquad w=\frac{a}{4\omega},\quad A=aw_a/w=1.
 \tag{D.2}
$$
真实 $L>1$。目标度量在物理半径上为
$(1+w^2)da^2+a^2d\theta^2$，原北帽高度斜率为 $-w$。
本篇用正高度扰动 $v$ 推 Darboux 方程，北帽实际高度为 $Z_0-v$。

对非mean部分定义
$$
 h(t,\theta)=\frac{v_\perp(t,\theta)}{a(t)w(t)},
 \qquad \langle h\rangle=0.
 \tag{D.3}
$$
取任意固定实际物理角宽 $\sigma>0$。可直接取 $\sigma=1/512$；
全证明使用同宽范数，不从有限模式外推。

对每模 $h_m\in C^2([0,L])$，定义完整强 norm
$$
 \|h\|_{\mathcal Y_\sigma}
 =\sum_{m\in4\mathbb Z\setminus\{0\}}e^{\sigma|m|}
  \left(|m|^2\|h_m\|_\infty
       +|m|\|h_m'\|_\infty+\|h_m''\|_\infty\right).
 \tag{D.4}
$$
源空间为
$\|f\|_{\mathcal F_\sigma}=\sum_{m\ne0}e^{\sigma|m|}\|f_m\|_\infty$。
所需 Fourier 乘法在“先径向 sup、后求和”的 Banach 代数中进行，
没有交换 $\sup\sum$ 与 $\sum\sup$。

两端给定零均值数据 $f_B,f_*$，定义
$$
 \|(f_B,f_*)\|_{\partial,\sigma}
 =\sum_{m\ne0}e^{\sigma|m|}|m|^2
                   (|(f_B)_m|+|(f_*)_m|).
 \tag{D.5}
$$
它们指定的是实际非mean高度
$v_\perp(a_B)=a_Bw_B f_B$、$v_\perp(a_*)=a_*w_* f_*$。
平均高度只在内端给一个整体平移 $\lambda$，外端平均高度是下面的输出。
为与本题已有规范一致，几何结论取实、偶反射的四重数据；其复化仍含
全部 $4\mathbb Z$ 频率。以下代数与 Green 估计也在不加偶约束的整个
$4\mathbb Z$ Fourier 空间成立，偶子空间由唯一性保持。

## 2. 完整 mean 小根和非线性方程

沿用 R119 的相对变量。对于给定 $h$，
$$
 P=h_\theta,\quad U=h_{\theta\theta},\quad
 K_\perp=2h+h_t,\quad V=2h_\theta+h_{t\theta}.
 \tag{D.6}
$$
源 R25 (2.1) 的五项相对和满足
$$
 \mathcal R\le\frac{17}{4}\|h\|_{\mathcal Y_\sigma}.
 \tag{D.7}
$$
例如各项 $P,U,K_\perp,K_\perp+U,V-P$ 依次有
$1/4,1,3/8,11/8,5/4$ 倍 $\|h\|_{\mathcal Y}$ 的界。
因此 $\|h\|_{\mathcal Y}\le1/1024$ 时，同一完整 holonomy-one 方程
给唯一全纯 mean 小根
$$
 K_0=\mu_t(h),\qquad K=K_0+K_\perp,
 \qquad \|K_0\|_{C^0_t}\le12\mathcal R^2
                         <256\|h\|_{\mathcal Y}^2.
 \tag{D.8}
$$
该方程及根正是 R25 的归一化 mean，不是将 $K_0$ 设成0。
R25 的代数证明也适用于这里的强 Fourier/$C^0_t$ 代数，因为乘法、
mean 读取和逆级数的常数仍为1。

令 $E=1+w^2$。实际四状态范数有
$$
 N=\|P\|+\|K\|+\|U\|+\|V\|
 \le\frac{25}{8}\|h\|_{\mathcal Y}+256\|h\|_{\mathcal Y}^2
 <4\|h\|_{\mathcal Y}.
 \tag{D.9}
$$
R119 的准确式 (119.10) 在 $A=1$ 给
$$
 \mathcal Q(h)=\Pi_\perp
 \frac{E(V-P)^2+K^2+2EKU+EU^2-w^2P^2}{1+K+EU}.
 \tag{D.10}
$$
非mean完整方程于是是
$$
 \boxed{\quad
 \bigl[(\partial_t+2)^2+\partial_\theta^2\bigr]h
       =\mathcal Q(h),\qquad
 h(0)=f_B,\quad h(L)=f_*.
 \quad}                                                     \tag{D.11}
$$
它的源包含全部高频和 mean 小根造成的耦合。
由 R119 的逐项二次界，
$$
 \|\mathcal Q(h)\|_{\mathcal F_\sigma}
 \le512\|h\|_{\mathcal Y_\sigma}^2,
 \qquad \|h\|_{\mathcal Y_\sigma}\le1/1024.
 \tag{D.12}
$$
在半径 $r\le1/2048$ 的球上，完整全纯 map 的 Cauchy 导数界还给
$$
 \|\mathcal Q(h)-\mathcal Q(k)\|_{\mathcal F_\sigma}
 \le2048r\|h-k\|_{\mathcal Y_\sigma}.
 \tag{D.13}
$$
方向圆盘半径为 $r$，全部输入仍在 $2r\le1/1024$ 球内。

## 3. 同宽、与真实长度无关的完整 Green

对每个 $m\ne0$、$M=|m|\ge4$，线性方程是
$$
 H''+4H'+(4-M^2)H=F.
 \tag{D.14}
$$
零 Dirichlet Green 的准确核为
$$
 G_M(t,s)=
 -e^{2(s-t)}
 \frac{\sinh(M\min(t,s))\sinh(M(L-\max(t,s)))}
      {M\sinh(ML)}.
 \tag{D.15}
$$
因 $L>1,M\ge4$，$1-e^{-2ML}>1/2$。逐项对 (D.15) 求导，得到
$$
 |G_M(t,s)|\le\frac1M e^{-M|t-s|+2(s-t)},
$$
$$
 |\partial_tG_M(t,s)|\le
       3e^{-M|t-s|+2(s-t)}.
 \tag{D.16}
$$
在 $t=s$ 取任一单侧导数；积分式的一阶导数存在且连续。
积分两个指数半核给
$$
 M^2\|H\|_\infty\le3\|F\|_\infty,\qquad
 M\|H'\|_\infty\le8\|F\|_\infty.
$$
再用准确方程恢复 $H''$，
$$
 \|H''\|_\infty\le12\|F\|_\infty.
$$
故完整 Fourier Green $\mathcal G_D$ 在**同一个角宽**上满足
$$
 \boxed{\quad
 \|\mathcal G_D\|_{\mathcal F_\sigma\to\mathcal Y_\sigma}<32.
 \quad}                                                     \tag{D.17}
$$
这些是逐频的完整 ODE 核及其积分，没有配点，也没有角截断。

两个准确齐次 lift 分别是
$$
 A_M(t)=e^{-2t}\frac{\sinh(M(L-t))}{\sinh(ML)},\qquad
 B_M(t)=e^{2(L-t)}\frac{\sinh(Mt)}{\sinh(ML)}.
 \tag{D.18}
$$
它们的 $M^2|H|,M|H'|,|H''|$ 范数依次至多
$2M^2,6M^2,8M^2$。因此两端完整 lift $h_D$ 有
$$
 \|h_D\|_{\mathcal Y_\sigma}\le16\|(f_B,f_*)\|_{\partial,\sigma}.
 \tag{D.19}
$$
特别没有把长区间的真末端换成无限半线后漏掉反射项。

## 4. 真正的非线性两端解

取准确半径
$$
 r_*=2^{-20},\qquad
 \|(f_B,f_*)\|_{\partial,\sigma}\le2^{-25}=r_*/32.
 \tag{D.20}
$$
定义完整 map
$$
 \mathcal T(h)=h_D+\mathcal G_D\mathcal Q(h).
 \tag{D.21}
$$
在 $\|h\|_{\mathcal Y}\le r_*$ 上，
$$
 \|h_D\|\le r_*/2,\qquad
 \|\mathcal G_D\mathcal Q(h)\|
 \le2^{14}r_*^2=r_*/64,
$$
$$
 \operatorname{Lip}(\mathcal T)
 \le32\cdot2048r_*=1/16.
 \tag{D.22}
$$
所以 (D.21) 自映且严格收缩，给唯一真实 $h\in\mathcal Y_\sigma$
解 (D.11)。全纯性来自同一复球的统一收缩，实共轭、四重周期及偶反射
由唯一性保持。

这个定理是完整 PDE 的非线性存在性，不是只解其线性化或有限矩阵。
其适用输入是 (D.20) 的实际两端**非mean Dirichlet 数据**，范围没有扩张。

## 5. mean 由原方程恢复，而非另加一个自由 Dirichlet 条件

令
$$
 v_0(t)=\lambda+\int_0^t a(s)w(s)K_0(s)\,ds,
 \qquad v(t,\theta)=a(t)w(t)h(t,\theta)+v_0(t).
 \tag{D.23}
$$
因为 $(aw)_t=2aw$，它准确恢复
$v_a=wK$、$v_\theta=awP$，不改变 (D.6) 的非mean状态。
平均高度差和两端 mean 斜率因此是明确输出
$$
 \boxed{\quad
 v_0(L)-v_0(0)=\int_0^L awK_0\,dt,
 \qquad (v_a)_0(0)=w_BK_0(0),\quad (v_a)_0(L)=w_*K_0(L).
 \quad}                                                     \tag{D.24}
$$
两端平均高度不能再分别指定。
还可保留长度无关的量化：
$$
 \frac{|v_0(t)-\lambda|}{a(t)w(t)}
 \le\frac12\|K_0\|_\infty
 <128\|h\|_{\mathcal Y}^2.
 \tag{D.25}
$$

为核完整 PDE，先在任意严格较窄正角宽微分；解析 Fourier 衰减使所有
所需角导存在。由于非mean方程已解，第二个 Darboux 方程的 residual
只可能是一个径向 mean 函数。另一方面，(D.8) 使完整
$$
 M=\left\langle
  \frac{1+(w+v_a)(v_\theta/a)_\theta/(1-(v_\theta/a)^2)}
       {\sqrt{1-2wv_a-v_a^2-(1+w^2)(v_\theta/a)^2}}
 \right\rangle
$$
准确等于1。写 $\mathfrak e(t)=K_t-F_t$；由 (D.11)，它是纯 mean。
源 R72 (2.6) 在当前 $t$ 和 $K$ 归一化下准确变成
$$
 M_t=w^2\left\langle D^{-3/2}(1+K+EU)\mathfrak e\right\rangle
 =w^2\left\langle D^{-3/2}(1+K+EU)\right\rangle\mathfrak e.
$$
这里 $w>0$，括号内因子在已付相对球中可逆，所以 residual 必为0。
由此 $K_{0,t}$ 也由完整二次源控制；不是靠对 mean 公式任意增加一阶
角正则性。所得恒等式及界再回到原 $\sigma$ 的强空间。

R119 (119.22)–(119.24) 的准确平面 coframe 现在闭合，$M=1$ 给旋转
holonomy，偶反射固定角规范，四重旋转消去水平平移周期。
因此完整 $F=(F_h,Z_0-v)$ 精确诱导 (D.2) 的同一目标度量。
它不是只有一个满足 Darboux 方程而未重建的高度函数。

## 6. 完整两端 Neumann 输出、mean 及真实 grounded 变换

两端的实际高度和径向迹由
$$
 v_\perp=aw f,\qquad
 (v_a)_\perp=w(2f+h_t),\qquad
 (v_a)_0=wK_0
 \tag{D.26}
$$
给出；$f=f_B$ 或 $f_*$。没有把 $2f+h_t$ 误当成未归一的物理导数。
令 $h_D$ 为完整线性 Dirichlet 解，$k=h-h_D$。
两端 $k=0$，故 (D.16) 给**两个端点合计**的完整二次误差
$$
 \sum_{m\ne0}e^{\sigma|m|}|m|
       (|k_m'(0)|+|k_m'(L)|)
 \le16\|\mathcal Q(h)\|_{\mathcal F_\sigma}
 \le2^{13}\|h\|_{\mathcal Y}^2.
 \tag{D.27}
$$
两端 mean 斜率除以各自的 $w$ 后合计小于
$2^9\|h\|_{\mathcal Y}^2$，mean 高度差保留 (D.24) 的准确积分。
所以这个 Dirichlet-to-two-trace map 没有丢高模或 mean 行。

若需要与主体在 radial/ground-state frame 接合，对真实参数方向
$\dot F$ 准确使用
$$
 w_{rad}=F\cdot\dot F/|F|,\qquad
 v_{gs}=F\cdot\dot F/Z,\qquad
 p_{gs}=(Y_z^2\mathsf A\nabla v_{gs})\cdot da.
 \tag{D.28}
$$
水平变化由 R119 (119.31)–(119.33) 对刚得到的真实 coframe 微分，
实际动量由 (119.34) 给出；这里可直接取物理半径，$\rho_*=1$。
两端 outward 方向相反。这个准确变换包括 $Z_a$、水平位移、normal
和 momentum shear；(D.26) 并未把高度导数改名为物理通量。
在该实际正径向段有任意严格正角宽余量用于它所需的有限角导。

## 7. 物理二阶和局部嵌入范围

在正交极坐标基中，$A=1$ 的实际高度 Hessian 是
$$
 (\nabla^2v)_{aa}=\frac wa(-K-U+\mathcal R),\quad
 (\nabla^2v)_{a\theta}=\frac wa(V-P),\quad
 (\nabla^2v)_{\theta\theta}=\frac wa(K+U),
 \tag{D.29}
$$
其中 $\mathcal R$ 是 (D.10) 投影前的完整二次源。
因 $w/a<5/28$，$\|K+U\|<3\|h\|/2$、
$\|V-P\|\le5\|h\|/4$、$\|\mathcal R\|\le512\|h\|^2$，
完整高度 $C^2$ norm（去掉整体平移）小于 $8\|h\|_{\mathcal Y}$。

R119 全 connector 续篇 (S.13) 的水平重建适用于此处同一相对球。
它的二阶费用为 $2^{12}(w^2/a)N$；现在
$w^2/a<a/16<7\cdot10^{-6}/16$、$N<4\|h\|$，故该费用
小于 $\|h\|/100$，一阶和零阶更小。于是
$$
 \boxed{\quad
 \|F-F_0+\lambda e_z\|_{C^2({\rm actual\ long\ segment})}
 <16\|h\|_{\mathcal Y}\le2^{-16}<1/1000.
 \quad}                                                     \tag{D.30}
$$
这里北帽采用 $Z_0-v$，故去平移时的符号是 $+\lambda e_z$。
该式保留了物理半径的全部费用：角向二阶出现的 $a^{-1}$ 与 $w$ 配对，
不能分别把极小半径丢掉或估成另一个巨大常数。

水平投影作为实际平面 annulus 上的映射，完整 Cartesian 导数满足
$\|dF_h-I\|\le2^8w^2N<1/3$。任意两点 $x,y$ 可先在较小半径上走
短圆弧，再沿半径连接；该路径保持在 annulus 内，长度至多
$$
 \big||x|-|y|\big|+\min(|x|,|y|)\,|\Delta\theta|
 \le(1+\pi/2)|x-y|<3|x-y|.
$$
沿此路对完整位移 $F_h-I$ 积分，得到
$|F_h(x)-F_h(y)|\ge(1-3\|dF_h-I\|_\infty)|x-y|>0$。
因此 annulus chart 自身全局单射；这个证明保留全部径向/角向交叉导数。
与全部主体、尾和握持区组成的
闭面的全局嵌入及 reach，仍须在 matching 完成后统一使用既有预算。

## 8. 现在精确缺哪一个算子方程

把 R119 的非线性 tail+connector 两迹穿过 R74 两个真实 bump 后，
在 $u=B$ 记其完整高度/径向输入为
$$
 (f_B(a),\ k_B(a),\ m_B(a))
$$
（$m_B$ 包括 mean 高度、mean 斜率及实际 holonomy 负荷）。
本篇已构造映射
$$
 \mathcal N_B(f_*,f_B)=
 (2f_B+h_t(0),\ K_0(0),\ v_0(L)-v_0(0))
 \tag{D.31}
$$
以及外端的同一完整两迹。因此剩余方程是**实际**的
$$
 k_B(a)=\Pi_\perp\mathcal N_B(f_*,f_B(a)),
 \qquad
 \text{全部 mean 高度/斜率匹配},
 \tag{D.32}
$$
并须在真实 normal/grounded frame 用 (D.28) 接合。
需要证明的是 (D.32) 对全部高 incoming 和普通源的可解性、统一强逆
及邻域控制。R74 只支付其基态线性边界选择；R119 的强标签小余项和
R15 的纯指数标签权没有自动提供这个同一空间的非线性逆。
本篇不把 (D.32) 再当作一个未说明的黑箱假设来宣称最终族已存在。

[准确有理程序](../scripts/fourfold_long_radial_nonlinear_bvp_20261113.py)
及 [完整小报告](../notes/2026-11-13-R119-long-radial-nonlinear-bvp-budget.json)
核实际长度门、完整 Green/两端 lift 费用、mean 半径、非线性收缩及
物理二阶预算。全频解来自上述核公式与完整 Banach 收缩。
