# R58：径向柱帽的真实端口、线性谱与无限函数匹配条件

**状态：已证明，完整未参与者全文独立审查通过。** 2026-11-10 UTC。
作者 tail_review_continued_2；完整独立审查 coupled_prefix；root 全文核收作者及审稿。

本结果给已有真实周期正C端口的两jet匹配条件，区分平面边镜射和插入开柱，
并在同一径向度量、指定旋转基态、真实正则中心及参数可微族范围内，
证明完整线性Gauss–Codazzi、中心能量、高频解析必要条件、球心逐模共振门、
固定开弧的无限频率要求，以及二阶的两项强迫。
这是明确范围内的必要条件，不构造帽，不推出一般闭曲面或非径向路线不可能。

## 采用与来源

- 完整作者稿 notes/2026-11-10-db6f-radial-cylinder-cap-linear-matching-v1.md；
  commit 92236c4b60e5996eb4b17efbfdfd6412e4bc84b0，
  blob 0e9e0413b0c196ad3c988f7135392327ac3ac8ad，22996 UTF-8 B，
  SHA256 a93f8a74f2a23726dd93310d41c85b27499311ed8634c57b37453e48907c9c62。
- [完整未参与者独立审查](https://github.com/Rogerhu12/math-research/blob/63db2491b82e47340a4991cbf5e524a74d473506/topics/visible-flexible-closed-surface/notes/2026-11-10-db6f-prefix-review-radial-cap-linear-matching.md)；
  commit 63db2491b82e47340a4991cbf5e524a74d473506，
  blob 1104b88bf264c8329e09d53ea4b4fc2baaf4190a，16287 UTF-8 B，
  SHA256 0d101bf56b2e3d47f5b50cc56765cdd763da31c64b0a7bd8ff76160263aff2b8。
  作者十一节全部接受，无阻断修改。审者未参与变元、谱、能量、高频或匹配推导。
- 来源清单SHA256 5de0dc7ed284e2f47ad69e9027d8b68554cb849ba66107699355e91ddfbc31fc；
  审查闭件清单commit a2d21b14e4fe210caf26981f905299481f99342f，
  SHA256 d445bef5ab7c12a99798fc748a796129dea06873a335dc66a9feb153084b206d。
- 作者§9的标量平面曲线变分始终按§4式(15)的共同e_z conormal gauge解释。
  若平面随参数倾斜，须先作刚体规范化；倾斜不改变曲率变分k。
  完整独审§8明确保留此范围，不把未规范化的竖直变分略去。
- 0 数学程序、ODE/PDE、BVP、矩阵、网格或主求解器执行。固定文本读取和哈希不替实际计算。
  本结果不支付主G5、闭合、可见幅度、量化reach或最终独立重跑。

下方逐字保留作者全部十一节。作者稿的历史待审状态由本采用记录更新。

---

## 1. 固定来源、真正输入与未转移的结论

以下均为冻结文本，不读取其中任何数值数据附件。

- [径向 mixed flux 原稿](https://github.com/Rogerhu12/math-research/blob/013eba46d6875cf0f6e83ce3fb66e430a9f1e05b/topics/visible-flexible-closed-surface/notes/2026-11-10-db6f-radial-mixed-flux-cap-gate-v1.md)，作者 commit 013eba46d6875cf0f6e83ce3fb66e430a9f1e05b，全文独审 6c123d0a9250e548666d60a0683a26d020b16b10。它证明 J=a∮M du 守恒，正则中心要求 J=0；本稿不重复把这个零门当充分条件。
- [实际光滑固定 H 柱核](https://github.com/Rogerhu12/math-research/blob/be7b380055c1906a1abacfc5682da0e372ef8579/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-smooth-core-fixed-h-reach-v1.md)，全文独审 5597dffd479f6ca0c80f3cba871862a319af20e9。共同单位速率角 u∈R/(2πZ)，柱边 a=1、a′=0、M=L=0、C=κ(u)>0、真实 F_r=e_z。
- [正 K 有心帽及平坦外领](https://github.com/Rogerhu12/math-research/blob/b86b496d59518717e9335a098879c657395df899/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-positive-k-centered-cap-flat-outlet-v1.md)，全文独审 758407b0f63f61ef3250d3ed47352f11574038bb。帽中心的共同材料度量为 dρ²+sin²ρ du²；参数 A 改变嵌入，不改变这个度量。A=1 的中心图是旋转球面基态。
- [root 显式支撑核冻结 v1](https://github.com/Rogerhu12/math-research/blob/747186528fa80bb233d837b1685c84174dc02db3/topics/visible-flexible-closed-surface/notes/2026-11-10-db6f-root-explicit-support-core-visible-reach-v1.md)，这里只读取并使用第 2–3 节的定义 h_τ=1+τψ、共同材料弧长和固定弧。该稿的全几何审查由另一分工负责；本文不重复支付其 reach、位移或原稿其他不等式。下述一阶曲率计算只依这些明确公式，不依其余结论。
- [题目 README 固定快照](https://github.com/Rogerhu12/math-research/blob/626b6123f05b37793b85aae640d2bb25810318f2/topics/visible-flexible-closed-surface/README.md)。它要求共同 g、闭 C² 全时族及其余量化和复现门；没有全局 C3 要求。

这里的 τ 是形变参数，r 是物理单位速率径向材料坐标，u 的周期始终是 2π。a(r) 必须对全部 τ 为同一个函数。不能在每个时间另选帽半径、中心曲率或径向剖面后称它们具有同一材料度量。

## 2. 原方程与完整两 jet

令

$$
g=dr^2+a(r)^2du^2,\qquad a>0,
$$

并选择实际框架 e_1=F_r、e_2=F_u/a、N=e_1×e_2。写

$$
L=F_{rr}\cdot N,\qquad M=F_{ru}\cdot N,\qquad C=F_{uu}\cdot N.
$$

直接由度量和单位法向，

$$
\begin{aligned}
F_{rr}&=LN,\\
F_{ru}&=a'e_2+MN,\\
F_{uu}&=-aa'e_1+CN,\\
N_r&=-Le_1-(M/a)e_2,\\
N_u&=-Me_1-(C/a)e_2.
\end{aligned}
\tag{1}
$$

Gauss–Codazzi 为

$$
LC-M^2=-aa'',\qquad
M_r=L_u-\frac{a'}aM,\qquad
C_r=M_u+\frac{a'}aC+aa'L.
\tag{2}
$$

例如交换混合三阶导数的法向分量给

$$
M_r-L_u=F_{ru}\cdot N_r-F_{rr}\cdot N_u=-(a'/a)M,
$$

$$
C_r-M_u=F_{uu}\cdot N_r-F_{ru}\cdot N_u=aa'L+(a'/a)C.
$$

这些计算也可按已审通量稿在 C² 的分布意义理解。本文的模态 ODE 只用它们的线性化。

在 C>0 区域，

$$
L=(M^2-aa'')/C.
\tag{3}
$$

因此 M,C 的径向 Cauchy 系统为

$$
\binom{M}{C}_r=
\begin{pmatrix}
2M/C&-(M^2-aa'')/C^2\\
1&0
\end{pmatrix}
\binom{M}{C}_u+
\binom{-(a'/a)M}{(a'/a)C+aa'(M^2-aa'')/C}.
\tag{4}
$$

其角主特征值是

$$
\lambda_\pm=\frac{M\pm\sqrt{aa''}}C.
\tag{5}
$$

所以 aa''>0 是负 Gauss 曲率的双曲区域，aa''<0 是正 Gauss 曲率的椭圆区域，aa''=0 是退化区域。已审的 Q=aa''≥0 能量存在定理没有自动覆盖后一种椭圆边值匹配。

### 2.1 一个端口匹配引理

考虑两张已经真实周期、同一材料角和同一定向 gauge 的图，在待贴圆周上满足：

- a、a′ 相等；
- 整个圆周上的 M(u)、C(u) 相等，且 C>0；
- 两侧使用一个共同 C² 径向度量，因此 a″ 的接缝值也相等。

在一个固定 u=u_*，用一个空间刚体运动把位置和完整正交框架配准。随后沿 u 的方程

$$
F_u=ae_2,\quad
(e_1)_u=a'e_2+MN,\quad
(e_2)_u=-a'e_1+(C/a)N,\quad
N_u=-Me_1-(C/a)e_2
\tag{6}
$$

是同一个有限维线性/仿射 ODE，具有相同初值。唯一性给整个圆周的位置和框架一致。再用(3)得到 L 一致，(1)给全部二阶偏导一致。

这证明：在上述准确前提下，两个真实端口的 C² 贴合可以核成 **两个整圈函数 M,C，加上共同 a,a′,a″ 和一个点的位置/框架配准**。它没有把位置 monodromy 留成另一个可事后调整的函数，因为两端口本来就真实周期，且(6)实际传递位置。

对于逐 τ 的帽件，配准运动可由一个固定材料锚点的两套框架唯一确定；若输入联合光滑，该运动也联合光滑。移动帽件本身不改变已固定的核心 H，但它不能改变 M,C 的角向函数。

边界同一速度 a 下，保持一维材料度量的角重标只有 u↦u+u_0 或 u↦−u+u_0；任意随 u 变的重排并非自由控制。若要从外部进入帽中心，须先把径向反向和必要的角翻向真实拉回到共同 gauge，再比较这些函数及 a′ 的符号。不能拿帽向外的正斜率与桥向内的负斜率直接相等。

C=0 的端口不在本引理的 Gauss 消元范围；在那里须另外匹配 L，不能除以零。

## 3. 平面边、常向径向矢量和镜射/插柱

由(6)，

$$
(e_1)_u=a'e_2+MN.
\tag{7}
$$

在某一材料圆周上，a′=0 且 M=0 当且仅当 e_1 为常向量。一个方向已经归一后可记 e_1=e_z。因为 F_u⊥e_z，圆周位于一个与 e_z 垂直的平面 P 内。

所以“a′=0、M=0”在这里有真实空间内容：它给平面边及固定常向 conormal。它强于平均 mixed flux 为零。反过来，真实平面边配上实际常向单位 F_r=e_z，也迫使(7)中的两个正交系数分别为零。

### 3.1 单纯镜射只需这些一阶几何条件

令实际帽 F(r,u) 定义于 r≥0、F(0,u)=Γ(u)∈P、F_r(0,u)=e_z。令 S_P 是关于 P 的空间反射，在 r<0 置

$$
G(r,u)=S_P F(-r,u).
\tag{8}
$$

边上 N=e_z×e_2 位于 P，故 S_P N=N。由(1)和 a′=M=0，

$$
G_r=-S_Pe_z=e_z,\qquad
G_{rr}=S_P(LN)=LN,
$$

$$
G_{ru}=-S_PF_{ru}=0,\qquad
G_{uu}=S_P(CN)=CN.
\tag{9}
$$

位置与一阶导数也相等。因此实际 C² 帽可在此边镜射成为 C² 双帽，**并不要求 L=0**。这只支付接缝光滑性；双帽全局是否嵌入、是否具有固定开 H 及足够 reach，还要另外证明。更高阶镜射光滑性也不由(9)自动得到。

### 3.2 插入开圆柱要求额外的 L=0

若在同一边前面插入真正的开柱

$$
F^{\rm cyl}(r,u)=\Gamma(u)+r e_z,
\tag{10}
$$

柱侧 F_rr=0。C² 匹配因而还要求帽侧 L=0。在 C>0、M=0 下，Gauss 式精确化为

$$
L=-aa''/C,
$$

所以插柱需要 a″=0；仅 a=1、a′=0 不足够。实际开柱入口取 a 恒等于1的一段，则全部径向 metric jet 均匹配，但它仍没有解决后面的帽 BVP。

这一区别避免把能够镜射的帽直接称作能够夹住开圆柱核的帽。

## 4. 固定旋转帽基态与变分的准确假设

以下给必要条件，不先假设完整帽族已经构造出来。

选择一个固定 a∈C∞([0,T))，满足

$$
a(0)=1,\quad a'(0)=0,\quad a>0,\quad |a'|<1\quad(0\le r<T).
\tag{11}
$$

允许 a″ 改变符号；若要求开柱入口，再令 a=1 于 0 的一个邻域。记

$$
b(r)=\sqrt{1-a'(r)^2}>0,\qquad
Z(r)=\int_0^r b(s)\,ds.
$$

考虑实际旋转基态

$$
F_0(r,u)=(a(r)\cos u,\ a(r)\sin u,\ Z(r)).
\tag{12}
$$

它有共同 g，且 r=0 的真实径向方向为 e_z。选

$$
N_0=-b\,e_{\rm rad}+a'e_z,
$$

便得

$$
M_0=0,\qquad C_0=ab,\qquad L_0=-a''/b.
\tag{13}
$$

这里 e_rad=(cos u,sin u,0)。a′ 可以在桥中先正后负，故本模型允许先向外鼓出的负曲率段。b>0 排除了内部轴向速度为零的特殊转折；不能把结论越过这项假设。

假设 r=T 是一个真正光滑的中心。写 ρ=T−r，并先要求该旋转基态中心曲率 k_*²>0，于是

$$
a=\rho-\frac{k_*^2}{6}\rho^3+O(\rho^5),\qquad
b=k_*\rho+O(\rho^3).
\tag{14}
$$

第 8 节为写出完全显式的中心传递，会再加上一个**圆球度量开核心**条件；第 6 节的能量必要式不需要该加强。

现在假设存在与(12)具有**同一个 a(r)** 的实际等距族 F_τ，并在 τ=0 至少可在 C² 拓扑单侧微分。为避免无关弱导数记号，可先考虑在去中心域联合光滑的族；线性 Codazzi 在弱意义同样给下述模态 ODE。写

$$
\ell=\partial_\tau L|_0,\quad
m=\partial_\tau M|_0,\quad
c=\partial_\tau C|_0.
$$

若它真实贴着一族单位速率平面柱边 Γ_τ，且 F_{τ,r}(0,u)=e_z，则

$$
m(0,u)=0,\qquad c(0,u)=k(u):=\partial_\tau\kappa_\tau(u)|_0.
\tag{15}
$$

当 a″(0)=0 时，插柱所需的 ℓ(0,u)=0 也会由线性 Gauss 式自动给出。

这些假设覆盖“从圆柱初态和旋转帽基态出发的光滑接帽方案”。它们没有证明所有可能的初态帽都旋转；也不把 τ 仅 C² 连续而不可微的族纳入此线性论证。

## 5. 从原 Gauss–Codazzi 完整导出的线性系统

固定 a 后线性化(2)：

$$
C_0\ell+L_0c=0,\qquad
m_r=\ell_u-\frac{a'}a m,\qquad
c_r=m_u+\frac{a'}a c+aa'\ell.
\tag{16}
$$

由(13)，

$$
\ell=\frac{a''}{ab^2}\,c.
\tag{17}
$$

引入

$$
x=am,\qquad \zeta=\frac ba c,\qquad
P=\frac{aa''}{b^3},\qquad R=\frac b{a^2}>0.
\tag{18}
$$

第一式的消去为

$$
x_r=a\ell_u
=\frac{a''}{b^2}c_u=P\zeta_u.
$$

第二式中，用 b′/b=−a′a″/b²，

$$
\begin{aligned}
\zeta_r
&=\frac ba m_u+
 \left(\frac{b'}b-\frac{a'}a+\frac{a'}a+\frac{a'a''}{b^2}\right)\zeta\\
&=\frac b{a^2}x_u=R x_u.
\end{aligned}
$$

因此准确的线性化是

$$
\boxed{\quad x_r=P\zeta_u,\qquad \zeta_r=R x_u.\quad}
\tag{19}
$$

b、P、R 全部由一个共同 a 决定；它们不是可逐角模态自由选择的控制函数。

按 f_n=(2π)^{-1}∫f(u)e^{-inu}du 作 Fourier 分解。对 n≠0，

$$
x_n'=inP\zeta_n,\qquad
\zeta_n'=inR x_n,
$$

从而

$$
\boxed{\quad
\left(\frac{\zeta_n'}R\right)'+n^2P\zeta_n=0.
\quad}
\tag{20}
$$

柱端的完整条件是

$$
\zeta_n(0)=k_n,\qquad \zeta_n'(0)=0.
\tag{21}
$$

第二个条件来自点态 m=0，不是只来自通量的平均条件。

还有一个有用但不改变边值问题的化简。置 y_n=aζ_n，用 b²=1−a′²逐项微分，(20)等价于

$$
\left(\frac{y_n'}b\right)'
 +(n^2-1)\frac{a''}{ab^3}y_n=0.
\tag{22}
$$

以实际轴向高度 Z 作坐标、A(Z)=a(r(Z))，有

$$
A_{ZZ}=\frac{a''}{b^4},\qquad
\boxed{\quad (y_n)_{ZZ}+(n^2-1)\frac{A_{ZZ}}A\,y_n=0.\quad}
\tag{23}
$$

例如验证(22)：ζ=y/a 给 ζ′/R=(a/b)y′−(a′/b)y，且 (a′/b)′=a″/b³；代回后恰留下 n²−1。入口 a′=0，所以 y_Z(0)=0。式(23)清楚显示同一个剖面 A 同时决定全部 n 的线性传递。

## 6. 正则中心给出的边界条件与能量恒等式

因为 F_τ 在固定中心材料图上可在 C² 微分，线性第二形式作为一个真实 Cartesian 二次型有界。因 |∂_r|=1、|∂_u|=a，

$$
m=O(a),\qquad c=O(a^2).
$$

结合(14)、(18)，

$$
x_n=O(\rho^2),\qquad
\zeta_n=O(\rho^2),\qquad
\zeta_n'=inR x_n=O(\rho).
\tag{24}
$$

同时 R=O(ρ^{-1}) 且 P=O(ρ^{-1})。所以

$$
\frac{\zeta_n'\overline{\zeta_n}}R
=in x_n\overline{\zeta_n}\longrightarrow0,
\tag{25}
$$

并且 |ζ_n′|²/R 和 |P||ζ_n|² 在中心可积。这里没有用“极坐标表达有界”冒充中心正则；(24)由真实 Cartesian C² 变分推出。

把(20)乘以共轭 ζ_n，在 [0,T−ε] 积分，取实部，再用入口(21)及中心(25)，得到

$$
\boxed{\quad
\int_0^T\frac{|\zeta_n'|^2}{R}\,dr
=n^2\int_0^T P|\zeta_n|^2\,dr.
\quad}
\tag{26}
$$

这对每个活动 n≠0 都成立。它是一个完整必要恒等式，不是对某个采样模态的数值残差。

### 6.1 纯非负 Gauss 曲率旋转帽的线性排除

若整段 a″≤0，即 K=−a″/a≥0，则 P≤0。式(26)的左边非负、右边非正，故 ζ_n′=0。中心 ζ_n→0 迫使 ζ_n恒0，再由(19)有 x_n恒0。

n=0 也直接满足 x_0′=ζ_0′=0，中心(24)迫使二者为零。故全部 m,c,ℓ 为零，特别是柱边 k(u)恒0。

因此：

> 在(11)–(15)的旋转基态、正则正曲率中心及可微共同度量族范围内，纯非负 Gauss 曲率的径向帽桥不能承接任何非零一阶柱边曲率形变。若某个模态实际活动，桥上必须有 a″>0 的负 Gauss 曲率区域，并满足(26)的精确加权平衡。

更进一步，若度量及第二形式的一阶变化都零，则实际变分只可能是无穷小刚体运动：把框架变分写成 δe_i=Ω(r,u)e_i，Ω 反对称；固定的连接系数给 Ω_r=Ω_u=0，随后 δF−ΩF为常向量。固定一个开 H 就消去这种刚体自由度。

本结论不排除仅在 τ 的高阶开始变化、在此旋转基态一阶完全静止的族；也不能从它单独推出非线性局部刚性或一般不可能性。

## 7. 纯正曲率段对非解析柱数据的局部高频障碍

这一节不需要帽中心，只需固定有限区间 [0,r_2]，a,b 正且光滑，P≤0；并存在闭子区间 [r_1,r_2] 上

$$
-P\ge p_*>0,\qquad R\ge r_*>0.
\tag{27}
$$

令 n≥1，η_n=i x_n，则(19)成为

$$
\eta_n'=-nP\zeta_n,\qquad \zeta_n'=nR\eta_n.
\tag{28}
$$

初值是 η_n(0)=0、ζ_n(0)=k_n。由于所有系数都只依 r 且为实数，解是 k_n 乘上初值 (0,1) 的实解。对该归一解，在 P≤0 区间上两个分量保持非负，ζ≥1。

在 [r_1,r_2] 上，(28)是非负耦合系统，其积分方程逐次迭代逐项不小于常系数系统

$$
\eta'=np_*\zeta,\qquad \zeta'=nr_*\eta,
\quad (\eta,\zeta)(r_1)=(0,1).
$$

常系数解的第二分量是 cosh(n√(p_*r_*)(r−r_1))。于是

$$
|\zeta_n(r_2)|
\ge |k_n|\cosh(n\alpha),\qquad
\alpha=\sqrt{p_*r_*}(r_2-r_1)>0.
\tag{29}
$$

若实际线性解在 r=r_2 是一个有界周期函数，其 Fourier 系数有同一个有限上界 B，于是

$$
|k_n|\le 2B e^{-n\alpha}.
\tag{30}
$$

实数据的负频率是共轭，故 k 的 Fourier 级数在任意 |Im u|<α 的严格子条带内绝对收敛。**初始 k 必须实解析。**

因此，非零且在某个开弧恒零的 C∞ 柱曲率一阶 bump，不能沿这种“此前从无负曲率，随后有真正正曲率 slab”的线性 Cauchy 演化到达 r_2。即使 P 在离开圆柱时无限阶平坦，只要后面有(27)，这个结论仍成立。

这不是说所有含椭圆段的桥都失败：若之前有 P>0 的负曲率区，(28)不再是同向非负系统，可以准备不同的相位；上述比较证明便不能沿用。那种情况下要支付下一节的真实边值匹配，而不是从非解析初值直接调用角解析 CK。

## 8. 对圆球中心核心的完全显式共振门

为把中心条件写成一个精确可检查的标量门，进一步取某个 σ>0 和固定 ρ_*>0，使

$$
a(r)=\sigma\sin\frac{T-r}{\sigma}
\quad\text{在 }0<T-r<\rho_*<\pi\sigma/2.
\tag{31}
$$

这与已有正 K 帽的共同圆球核心相容；它只是本节的准确假设，不是所有可能中心的定义。

在该核心，b=a/σ，P=−σ/a，R=1/(σa)。对 n≥1，(20)的两个独立解可直接写成

$$
\zeta_n
=A_n\tan^n\frac{\rho}{2\sigma}
+B_n\cot^n\frac{\rho}{2\sigma}.
\tag{32}
$$

验证只需 d log tan(ρ/(2σ))/dρ=1/a。对应稳定项和增长项分别满足

$$
x_n=i\sigma\zeta_n,\qquad x_n=-i\sigma\zeta_n.
\tag{33}
$$

中心(24)先排除 B_n。n=1 的剩余项仅为 O(ρ)，也与 c=σζ=O(ρ²)矛盾，所以 n=1 必为零。n≥2 的衰减项与该必要中心阶数相容；本稿不因此自动宣布任意无穷级数在中心光滑。

对每个整数 n≥2，定义 v_n：先在圆球核心取

$$
v_n(r)=\tan^n\frac{T-r}{2\sigma},
$$

然后按(20)唯一延伸到 r=0。这里是精确定义的线性 ODE 解，不是实际数值执行。令

$$
D_n(a)=v_n'(0),\qquad
\mathcal R(a)=\{n\ge2:D_n(a)=0\}.
\tag{34}
$$

若 n∈R(a)，则 v_n(0)不能为零，否则线性 ODE 的零 Cauchy 初值会使 v_n恒零，与核心定义矛盾。由入口(21)，任何实际可微接帽族必须满足

$$
\boxed{
\quad k_n\ne0\ \Longrightarrow\ n\in\mathcal R(a),\qquad
\zeta_n(r)=k_n\,\frac{v_n(r)}{v_n(0)}.
\quad}
\tag{35}
$$

负频率由共轭给出。

这是同一个固定 a 的无限函数匹配门。选择一个 a 后，所有 D_n 同时被确定。允许为不同 n 另选 a，或为不同 τ 另选 a，都不解决题目的共同度量要求。

即使某个 n 的 D_n 精确为零，(35)首先只给一项线性第二形式候选。无穷模求和的全阶控制、真实非线性族、位置和嵌入、固定 H 及全局 reach 仍须另证；不能将一次有限模 shooting 成功写成完整 BVP。

## 9. 柱边自身的闭合约束及固定 H 的无限模性质

基态柱边是单位圆。对任何实际单位速率平面闭曲线族，写

$$
\partial_\tau T_\tau|_0=f(u)\nu_0(u),\qquad
\nu_0=e_z\times T_0.
$$

由 Frenet 方程，曲率变化 k=f′。切向周期给

$$
\int_0^{2\pi}k\,du=0.
$$

真实位置闭合给 ∫fν_0 du=0。对 k=f′ 积分分部，因此

$$
k_0=k_1=k_{-1}=0.
\tag{36}
$$

这三项不是可自由传给帽的曲率模态。f 的常数项及积分位置锚点对应平面刚体运动，不提供新的 k。

若该实际族在一个材料开弧逐点固定，则该弧上 δΓ、δT、k 都为零。若一阶变分非刚体，k不恒零：k=0 会使 f 为常数，而固定弧迫使 f=0，继而 δΓ是被固定弧消去的常向量。

一个非零三角多项式不能在开弧恒零。因此这种 k 必有无限多个非零 Fourier 模态。结合(35)：

> 对具有圆球中心核心的指定旋转基态，任何一阶非平凡且固定开弧的柱族若要由同一个径向 a 接帽，R(a) 必须包含 k 的全部无限频率支集。只有有限个共振模态时，这一条具体可微固定 H 路线被排除。

无限 R(a) 也不被本文证明充分；它可能没有支持所需固定弧函数，或者缺少(35)的无穷级数控制和更高阶兼容。

### 9.1 当前显式支撑核的实际一阶数据

只用来源 root 稿第 2–3 节的精确定义，令

$$
h_\tau(\phi)=1+\tau\psi(\phi),\qquad
q(\phi)=\psi+\psi'',\qquad
\rho_\tau=1+\tau q.
$$

共同材料弧长满足 u_τ′=ρ_τ，且 u_0=φ。因此

$$
\kappa_\tau(u)=\frac1{1+\tau q(\phi_\tau(u))}
\quad\Longrightarrow\quad
k(u)=-q(u)=-(\psi+\psi'')(u).
\tag{37}
$$

在 τ=0，逆材料角变化只乘以基态曲率的角导数0，所以没有遗漏一个重参数项。

该 ψ 平均为零、在固定开弧恒零且不恒零。于是 k_0=0，且 Fourier 乘子给 k_{±1}=0。若 k恒零，则 ψ″+ψ=0，开弧零迫使 ψ恒零，矛盾。故 k 是非零、在开弧恒零的 C∞ 函数，必有无限个活动模态。

所以若为这个具体初态选择(12)、(31)的旋转帽基态，不能只调一个帽参数 A 或几个射击参数去匹配有限几个模态便称函数已经贴合。式(35)给出真正需要进一步解决的无限门。它不判断该 root 稿现有有边核心的正确性，也不把帽匹配障碍移到主 flat17。

## 10. 二阶方程说明一阶共振仍不是非线性 BVP

设有足够光滑的候选族，按无阶乘约定展开

$$
M=\tau m+\tau^2m_2+O(\tau^3),\qquad
C=C_0+\tau c+\tau^2c_2+O(\tau^3),
$$

$$
L=L_0+\tau\ell+\tau^2\ell_2+O(\tau^3).
$$

二阶 Gauss 系数给

$$
C_0\ell_2+L_0c_2+\ell c=m^2,
$$

故

$$
\ell_2=-\frac{L_0}{C_0}c_2+S,\qquad
S=\frac{m^2}{ab}-\frac{a''c^2}{a^2b^3}.
\tag{38}
$$

对 x_2=am_2、ζ_2=bc_2/a 使用同样消去，得到

$$
(x_2)_r=P(\zeta_2)_u+aS_u,\qquad
(\zeta_2)_r=R(x_2)_u+ba'S.
\tag{39}
$$

这两项强迫包含一阶模态的乘积，不会因各个一阶 D_n 为零而自动消失。入口二阶曲率来自实际 Γ_τ，不能另自由指定；中心仍须满足真实 Cartesian 正则。

因此一阶共振只是第一道必要门。随后要解(39)及更高阶兼容，或给一个真正的非线性存在/边值理论，并支付级数或参数极限。本文没有做这个替代。

## 11. 可以据此继续的具体研究，而非已完成事项

目前的精确问题可写成：

- 一次性选择共同 a，包含所需平柱入口、允许的负/正曲率过渡和正则帽中心；
- 在该 a 上从实际 Γ_τ 的全函数边数据求解 Gauss–Codazzi，并满足中心正则；
- 若仍用旋转基态和圆球核心，首先核(35)及当前 k 的无限支集，再处理(39)；
- 或明确改变为另一种非旋转基态、非径向共同材料度量及其真实方程，从而不再套用本文的模态对角化。仅改坐标名字不能消去其原有假设。

反射引理只解决已经存在的真实帽的接缝；端口引理只减少匹配记账；零 flux、能量平衡、共振或局部 Cauchy 存在都没有产生当前所缺的完整帽族。

全文所有推导均为纸面数学。没有新的数学程序、Python、终端、PDE、矩阵或几何数值执行；没有制造帽、边值解、网格或 README 完成证据。保存与固定回读只核文本身份。下一步应为未参与者全文独审及真正函数边值机制，而非有限模“通过”后的阶段性收尾。
