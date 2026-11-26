# R971 — 原六 sigma 的 norm130 来源、完整除法式与五伴随框架

日期：2026-11-27。**已证明：同一六输入中观察 $A+c+10d_0$ 的真实来源、全部多项式坐标、整正交框架和两种 CM 的完整伴随转移。** 本文不由范数、首阶或两个好位特征选取算术线。它与 R970 的固定秩二曲线相接，仍需完整 degree130 算子的真实投影；该门由 R972 的同次原 degree390 消费处理。所有旧 mixed 条件继续保留。

## 1. 同一个六输入及实际观察

采用 R958/R961 的原模型

$$
 E_1:y^2=x^3+1,\qquad dz=dx/(2y),\qquad
 x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad\sigma=z+\cdots.
$$

置

$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
g=3+\omega,\quad\bar g=2-\omega,\quad
\rho=-\nu_\sigma^{\otimes6}/84.
$$

原输入顺序为 $(\xi_1,\xi_2,\xi_3,x_0,c,d_0)$；其中 $x_0$ 是输入坐标，不与曲线函数 $x(z)$ 混淆。记

$$
A=\delta\xi_1+2\delta\xi_2+g\xi_3+\bar g x_0,\qquad
Y_*=A+c+10d_0.
$$

其行向量及实际边际是

$$
a_*=(\delta,2\delta,g,\bar g,1,10),\qquad
\boxed{F_*=\frac15(a_*)_*\rho
=-\frac{\sigma(\delta z)\sigma(2\delta z)\sigma(gz)\sigma(\bar gz)\sigma(z)\sigma(10z)}{420}.}
\tag{1}
$$

六个范数为 $3,12,7,7,1,100$，和恰为130。首项乘积为
$\delta(2\delta)g\bar g\cdot10=-420$，故 $[z^6]F_*=1$。
原奇 sigma 的四个奇 CM 系数恰为 $\delta,g,\bar g,1$；两个偶系数为 $2\delta,10$。全部半特征乘积因此是标准 even 半特征。其 Gaussian 用原 $N(a)$ 规律合并为130，且原六次旋转使角型为零。所以

$$
F_*\in V_{130}:=\sigma^{130}x^2K[X]_{\le21},\qquad X=x^3,\quad K=\mathbf Q(\omega).
\tag{2}
$$

以下全函数身份将进一步给质量列为零及第20列为一，避免仅凭 degree 和首阶识别它。

## 2. 完整五倍点除法给出全部22坐标

沿 R465/R961 的已固定来源，

$$
S_{34}=\sigma^{34}x^2P_S(X),\qquad
P_S=X^4-\frac{53}{7}X^3-\frac{12}{7}X^2-\frac{80}{7}X-\frac{128}{7}.
\tag{3}
$$

本篇的不同仅是把最后一个 $\sigma(2z)$ 换成 $\sigma(10z)/5$；故

$$
F_*=S_{34}\frac{\sigma(10z)}{5\sigma(2z)}.
\tag{4}
$$

写 $r_n=\sigma(nz)/\sigma(z)^{n^2}$。原 sigma 规范给

$$
r_2=-2y,\qquad r_3=3x(X+4),\qquad
r_4=-4y(X^2+20X-8).
$$

完整除法多项式递推 $\psi_5=\psi_4\psi_2^3-\psi_3^3$（其中 $r_n=(-1)^{n-1}\psi_n$）于是给

$$
\begin{aligned}
r_5&=32(X+1)^2(X^2+20X-8)-27X(X+4)^3\\
&=\boxed{5X^4+380X^3-240X^2-1600X-256}.
\end{aligned}
\tag{5}
$$

这来自同一曲线完整群律和 $y^2=X+1$，包含所有核点及其重数。它不是在几个普通点作插值。设 $r_5=\sum_{j=0}^4b_jX^j$。准确的组合式

$$
r_{10}(z)=r_5(2z)\,r_2(z)^{25}
$$

与原全倍点式

$$
x(2z)=\frac{x(X-8)}{4(X+1)},\qquad
\sigma(2z)=-2y\sigma(z)^4
$$

共同给

$$
\frac{\sigma(10z)}{5\sigma(2z)}=\sigma(z)^{96}\mathcal J_5(X),
$$

$$
\boxed{\mathcal J_5(X)=\sum_{j=0}^4
\frac{b_j}{5}\,64^{4-j}X^j(X-8)^{3j}(X+1)^{12-3j}.}
\tag{6}
$$

式 (6) 中 $0\le j\le4$，所以所有幂非负，整条有理函数的分母已全部消去。每项次数为 $12+j$；仅 $j=4$ 达到16，其首项系数为 $b_4/5=1$。故

$$
\boxed{F_*=\sigma^{130}x^2P_S(X)\mathcal J_5(X),\qquad
\deg(P_S\mathcal J_5)=20,\quad[X^{20}](P_S\mathcal J_5)=1.}
\tag{7}
$$

这就是 $V_{130}$ 中全部22坐标，第21质量列恰为零。它的系数位于 $\mathbf Z[1/35]$，不存在为提高阶数而任意选择的向量。

## 3. 原整框架及全部半特征

从第一行 $a_*$ 开始，按原 Hermitian 消元删去零起始指标

$$
5,\ 1,\ 0,\ 2,\ 3;\qquad\text{最后保留指标 }4.
$$

若当前剩余指标集为 $I$，$R_I=\sum_{j\in I}a_j\bar a_j$，新增行定义为

$$
r_i=R_Ie_i-\bar a_i\,a_*|_I,\qquad i\in I.
\tag{8}
$$

原第一行与所有新行组成 $L_*$。全部剩余范数链为

$$
\boxed{130,\ 30,\ 18,\ 15,\ 8,\ 1.}
\tag{9}
$$

每步 $r_i$ 与先前各行正交，且
$N(r_i)=R_I(R_I-N(a_i))$。这由 (8) 的三个内积项直接展开：
$R_I^2-R_IN(a_i)-R_IN(a_i)+N(a_i)R_I=R_I(R_I-N(a_i))$。
因而

$$
\boxed{L_*\bar L_*^t=\operatorname{diag}(130,3900,540,270,120,8).}
\tag{10}
$$

各条行的系数属于 $\mathbf Z[\omega]$。全部行范数为偶数；在 $\mathbf Z[\omega]/2\simeq\mathbf F_4$ 中，一个非零系数的范数模二为一，所以每行模二非零系数个数均为偶数。其原 odd sigma 半特征乘积恰为标准 even 半特征。式 (10) 同时使全部 Gaussian 交叉项为零。

准确的双向逆为

$$
(L_*^{-1})_{ji}=\frac{\overline{(L_*)_{ij}}}{N_i},
\qquad(N_0,\ldots,N_5)=(130,3900,540,270,120,8),
\tag{11}
$$

并有

$$
N(\det L_*)=(130\cdot30\cdot18\cdot15\cdot8)^2
=70963776000000.
\tag{12}
$$

这只有 $2,3,5,13$ 的素因子，尤其与 $7,19$ 互素。设

$$
\mathcal F_*=\frac15(L_*)_*\rho.
$$

在取任何边际以前，已由 (10) 和所有半特征得到完整 theta 张量

$$
\boxed{\mathcal F_*\in
\mathcal S_{130}\otimes\mathcal S_{3900}\otimes
\mathcal S_{540}\otimes\mathcal S_{270}\otimes
\mathcal S_{120}\otimes\mathcal S_8.}
\tag{13}
$$

其第一边际就是 (1)，没有从第一边际倒推整个张量的合法性。

## 4. 完整 CM 转移及其可用范围

保留 R961 已用原完整有限纤维确定的四个绝对相位

$$
N_{\gamma_7}\sigma=N_{\bar\gamma_7}\sigma=\sigma,\qquad
N_{\gamma_{19}}\sigma=N_{\bar\gamma_{19}}\sigma=\sigma,
$$

其中 $\gamma_7=3+\omega,\gamma_{19}=4+\delta$，
$N_\gamma=[\gamma]_*[\bar\gamma]^*/\gamma$。由于 (12) 与7、19互素，$L_*$ 在每一种六重 CM 核上都是双射。重排整个六重有限 trace，保全部中心、总规范 $\gamma^{-6}$ 和 (10)，得

$$
\boxed{N_{\gamma,Y_*}\prod_{i=1}^5N_{\gamma,Z_i}\mathcal F_*=\mathcal F_*}
\qquad(\gamma=\gamma_7,\bar\gamma_7,\gamma_{19},\bar\gamma_{19}).
\tag{14}
$$

在完整 $V_{130}$ 上的原逆身份、半单性及对应特征投影都以完整22列核定，不只在候选 $F_*$ 上核定。若同次消费者已经得到

$$
\Pi_*=P_7P_{19},\qquad\operatorname{im}\Pi_*=K\Phi_{*,1},\qquad
\Pi_*F_*=\alpha_*\Phi_{*,1},\quad \alpha_*\ne0,
\tag{15}
$$

则 $\Phi_{*,1}$ 是 R970 全部有限 Schwartz 已独立指定的算术来源；唯一性来自完整共同核，而非从两个特征值猜角色。

对 $B_\ell=\prod_{i=1}^5N_{\bar\gamma_\ell,Z_i}$，将 (15) 的实际有限多项式施于 $B_\ell$，并取五伴随的 simultaneous principal 平均。式 (14) 逐项把它转回第一轴投影。于是有完整张量身份

$$
\mathcal C_*\mathcal F_*=\Phi_{*,1}\otimes\Lambda_*,\qquad
\Lambda_*(0)=\alpha_*.
\tag{16}
$$

只在 $\alpha_*$、显示投影分母及 (12) 的固定坏素数之外，才能再说 $\Lambda_*$ 是 ordinary 整 Amice 卷积单位。这里没有提前给出非零的 $\alpha_*$，也没有用 (16) 删除 mixed cut。R970 的物理模型 $65^3$、共同模型17、真实微分周期及新来源清分母必须沿该篇的式 (35)–(39) 保留；(1) 的 $1/5$ 也始终保留。

## 5. 所有旧观察仍是混合观察

用原 $a=7+3\omega$，旧行依次为

$$
\begin{aligned}
a_S&=(\delta,2\delta,g,\bar g,1,2),\\
a_T&=(\delta,2\delta,g,\bar g,3\delta,4),\\
a_{W,+}&=(\delta,2\delta,g,\bar g,1,2a),\\
a_{W,-}&=(\delta,2\delta,g,\bar g,1,2\bar a),\\
a_Z&=(\delta,2\delta,g,\bar g,a,18).
\end{aligned}
\tag{17}
$$

每一行 $r$ 经 (11) 变成 $rL_*^{-1}$，并由完整恒等式
$(rL_*^{-1})L_*=r$ 返回。在完整伴随 CM 分支
$\beta=\gamma_7^j\gamma_{19}^k$ 和 $\zeta\in\mu_6$ 中，它的真实值是

$$
(rL_*^{-1})_0Y_*+\frac{\zeta}{\bar\beta}
\sum_{i=1}^5(rL_*^{-1})_iZ_i.
\tag{18}
$$

每个 finite torsion 中心和其既定 lift 同时保留；(18) 只是其连续变量部分。原单位条件、深管和 logarithm 都必须作用于此整个混合表达式。新算术来源上的中央导数零，只杀 (16) 上的完整独立伴随测试，不杀 (18) 中任意混合测试，不传播到来源乘积。

本篇新增的是实际 norm130 六 sigma 输入和全部转移数据。真正的 CM 非零投影、原 $H_{130}$ 的算术分量以及其余谱，均由 R972 的同次全390消费读取；固定曲线的无穷素数量词尚未解决。

## 依赖

- R465：原六 sigma 来源与 $S_{34}$ 的完整规范。
- R958/R961：完整 Hermitian 消元、全半特征、两种 CM 四方向的原奇 sigma 相位和伴随转移。
- R970：$E_*:y^2=x^3+65^3$ 的精确秩二、全部有限角色、degree130 的原算术线及通常 Selmer 桥。
- scripts/check-original-degree130-cross-cm-projection.py：同次生产的完整除法多项式、22列候选、原整 Gram/双逆/旧行返回；不读生成矩阵或系数表，不写可重算输出。
