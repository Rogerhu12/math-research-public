# R633：固定平尾的 Morse 双核全域线性背景与紧支撑双参数

2026-11-28。**本稿构造一个真正两端全平的固定正 profile，保留第二、第三角模各一条全平核，并给出其余全部整数角模的共同加权参考逆。** 新增的控制先用四个正区密度 bump 保持径向坐标的右端 Cauchy 数据，再留下两个真实紧支撑 profile 参数恢复双核。中心的 $j^2$ 谱损失在全域组装中只增加固定的两阶角导数代价。

本稿使用 R630 的**左正规全线径向解**作中心截段。它不把另一个“小 $\nu$、有限区间”径向分支算入该结论。它也不是非线性等距嵌入定理：随状态的特征返回、非线性残差校正、这个新背景自己的非零端口及有限几何仍待支付。

## 1. 引用输入和结论的精确范围

中心的全部公式、谱分类及正区局部源界来自 [R630](R630-morse-double-kernel-all-frequency-center.md)。平尾输入取自 Hu 可读改排稿：

- [§7：Morse 平尾、自然端点线、深尾 Green 逆](https://github.com/Rogerhu12/math-research/blob/9525ec1c3ea6400e512710eb404424bc9f744f7b/papers/flexible-surface-readable-4/07-flat-tails.tex)；
- [§8：height-ratio 排除、同时选择、有限转接的质量与传播界](https://github.com/Rogerhu12/math-research/blob/9525ec1c3ea6400e512710eb404424bc9f744f7b/papers/flexible-surface-readable-4/08-spectral-selection.tex)；
- [§9：一般自伴模型的正 buffer 压缩、有限界面矩阵、末端 Robin 匹配](https://github.com/Rogerhu12/math-research/blob/9525ec1c3ea6400e512710eb404424bc9f744f7b/papers/flexible-surface-readable-4/09-reference-inverse.tex)。

以上引用限于已经写有证明的**线性**引理。原稿把频率写成偶整数，本稿第 3 节逐项核对并支付全部整数的扩展；原稿的单核保持连接不予引用，本稿用第 2、6 节替换。原稿的非线性存在定理不作为本稿结论的依据。

### 1.1 全域背景

存在有限 $0<a<b<\infty$ 和

$$
w_*\in C^\infty([a,b]),\qquad
w_*>0\text{ 于 }(a,b),\qquad
\partial_r^kw_*(a)=\partial_r^kw_*(b)=0\quad(k\ge0),       \tag{1}
$$

使

$$
L_j=(w_*\partial_r)'-\frac{j^2w_*'}r
$$

在真正自然全平端点条件下满足

$$
\dim\ker L_2=\dim\ker L_3=1,\qquad
\ker L_j=0\quad(j\ge4).                                  \tag{2}
$$

取实反射空间 $u(r,-\theta)=u(r,\theta)$，则第二、第三模各只保留余弦分量；不保留半周对称。全平核记为 $f_2,f_3$。

在固定紧集 $K_r\Subset(a,b)$ 上存在一个光滑二参数族
$w_\mu$，$\mu\in\mathbb R^2$，经过 $w_*$，满足

$$
w_\mu=w_*\quad\text{于 }[a,b]\setminus K_r.               \tag{3}
$$

控制区全为正曲率区。整个参数族准确保持每一个负曲率组件的 profile 和特征行程角。双核的真实形状响应矩阵

$$
\left(
\int_a^b f_j\,L'_{j,w_*}[\partial_{\mu_i}w_\mu]f_j\,dr
\right)_{j=2,3;\ i=1,2}                                  \tag{4}
$$

可逆。

### 1.2 共同逆及明确范数

取

$$
d\mathfrak m=12w_*r^{-2}\,dr,\qquad
\mathcal B_j=-(12w_*r^{-2})^{-1}L_j.
$$

覆盖有限中心与两条端尾，中心权归一为一。尾的第 $n$ 个 cell 使用

$$
S_n=\frac23n^3,\qquad
H_n=e^{-S_n},\qquad
q_n=n^{5/2}\log(e+n),\qquad \mathcal E_n=e^{q_n}.
                                                               \tag{5}
$$

若 $\vartheta_n$ 是固定有界重叠的 cell localizer，定义

$$
\|u\|_{\gamma,M}^2
=\|u\|_{\mathrm{core},L^2(d\mathfrak m)}^2
+\sum_{\text{两尾},\,n\ge N}
\left(\frac{\mathcal E_n}{\mathcal E_N}\right)^{2M}
\left(\frac{H_n}{H_N}\right)^{-2\gamma}
\|\vartheta_nu\|_{L^2(d\mathfrak m)}^2.                    \tag{6}
$$

在连接 gap 上取相邻权的几何平均并保持常数；与 (6) 等价的连续权只改变固定 coefficient exponent。

对每个紧区间 $[\gamma_-,\gamma_+]\Subset(0,1)$，存在固定
$M,M',C$，使同一个 profile 的参考逆满足

$$
\boxed{\|\mathcal G_jF\|_{\gamma,-M'}
\le C(1+j)^2\|F\|_{\gamma,M}\qquad(j\ge2).}               \tag{7}
$$

第二、第三模各加入一条紧支撑对称 row/column，标量坐标取普通绝对值；(7) 包含这些坐标。在其真实核相容子空间上，它就是约化逆。$j\ge4$ 不加 border。

回到普通 $dr$ 源 $L_ju=f$ 时，$F=-(12w_*r^{-2})^{-1}f$。两个源密度及范数的转换在 cell $n$ 只花费 $\mathcal E_n^C$，因此只需调整 (6) 的固定指数。对余弦 Fourier 级数求和，(7) 是固定的两阶角导数损失。普通一、二阶径向恢复为

$$
\|u_r\|_{L^2(n)}
\le C\mathcal E_n^C\big(\|f\|_{L^2(n^+)}
 +(1+j)\|u\|_{L^2(n^+)}\big),
$$
$$
\|u_{rr}\|_{L^2(n)}
\le C\mathcal E_n^C\big(\|f\|_{L^2(n^+)}
 +(1+j^2)\|u\|_{L^2(n^+)}\big),                          \tag{8}
$$

其中 $n^+$ 是固定加宽 cell。这里只列出已支付的线性范数；不把 (7) 自行升级为非径向状态邻域中的逆。

## 2. 四个正区 bump 使两个谱控制成为真实紧支撑 profile 控制

R630 中 $s=\sqrt5$，

$$
\rho=5(e^{-X}-e^{-2X})-\frac{33-14s}{20},\qquad
\mathcal P=e^{-2\eta X},\qquad
\eta^2=\frac{36s-27}{20}.
$$

令 $\psi_1$ 是 R630 的正左正规解，满足

$$
\psi_1''=(\eta^2-\rho)\psi_1,\qquad
r=e^{\eta X}\psi_1,\qquad r_X>0.
$$

### 2.1 为什么需要保持两个径向 Cauchy 数据

把 $\mathcal P$ 改为 $e^{-2\eta X+2\zeta}$ 且固定 $\rho$，虽然
$\zeta$ 紧支撑，径向方程右端的两个 Cauchy 数据仍会改变。只有在其恢复以后，$r$ 和 $w$ 才会在控制区外真正不变。以下同时支付这两个条件。

取一个充分左侧的有限正曲率区间 $I\Subset\{\rho<0\}$。对
$\zeta_\tau=\sum_{i=1}^4\tau_i\chi_i$，$\chi_i\in C_c^\infty(I)$，令

$$
\mathcal P_\tau=e^{-2\eta X+2\zeta_\tau},\quad
V_{0,\tau}=\eta^2+\zeta_\tau''-2\eta\zeta_\tau'
                         +(\zeta_\tau')^2,\quad \rho_\tau=\rho.
                                                               \tag{9}
$$

定义 $\psi_{1,\tau}$ 在 $I$ 左边等于 $\psi_1$，并解
$\psi_{1,\tau}''=(V_{0,\tau}-\rho)\psi_{1,\tau}$。取固定 $X_b>\sup I$，要求

$$
\psi_{1,\tau}(X_b)=\psi_1(X_b),\qquad
\psi_{1,\tau}'(X_b)=\psi_1'(X_b).                         \tag{10}
$$

当 (10) 成立，ODE 唯一性给 $\psi_{1,\tau}=\psi_1$ 于 $I$ 外两边。于是

$$
r_\tau=e^{\eta X-\zeta_\tau}\psi_{1,\tau}=r
\quad\text{于 }I\text{ 外},
$$
$$
w_\tau(r_\tau(X))=\lambda\mathcal P_\tau(r_\tau)_X
$$

也在同一个固定物理区间 $r(I)$ 外等于 $w$。对足够小参数，R630 的正性证明给 $(r_\tau)_X>0$；同时

$$
(w_\tau)_r=-\lambda\mathcal P_\tau\rho r_\tau/(r_\tau)_X>0
\quad\text{于 }I.
$$

故控制保持该区严格正曲率。

### 2.2 四个准确一阶权与满秩

在 $I$ 所在的左尾取另一条独立解

$$
\phi_1(X)=\psi_1(X)\int_X^{X_0}\psi_1(Y)^{-2}\,dY,
\qquad X_0>\sup I.
$$

其 Wronskian 与 $\psi_1$ 非零。以

$$
\mathcal C_1(\tau)=W(\psi_1,\psi_{1,\tau})(X_b),
$$
$$
\mathcal C_2(\tau)=W(\phi_1,\psi_{1,\tau})(X_b)
                         -W(\phi_1,\psi_1)(X_b)
$$

表示 (10) 的两个等价条件。微分 (9) 得

$$
\delta\psi_1''-(\eta^2-\rho)\delta\psi_1
                     =(\chi''-2\eta\chi')\psi_1.
$$

与 $\psi_1$、$\phi_1$ 作 Wronskian 并积分，分别得到

$$
\delta\mathcal C_1=\int\psi_1^2(\chi''-2\eta\chi')\,dX,
\qquad
\delta\mathcal C_2=\int\psi_1\phi_1(\chi''-2\eta\chi')\,dX.
                                                               \tag{11}
$$

第二、第三模的能量导数由 R630 得

$$
\delta E_j=\|\psi_j\|_2^{-2}
\int\psi_j^2(\chi''-2\eta\chi')\,dX,\qquad j=2,3.          \tag{12}
$$

记 $D^*=\partial_X^2+2\eta\partial_X$。四行权为

$$
D^*(\psi_2^2),\quad D^*(\psi_3^2),\quad
D^*(\psi_1^2),\quad D^*(\psi_1\phi_1).                   \tag{13}
$$

它们在一个充分左侧的正区上线性独立。为证明这一点，写 $t=e^{-X}\to\infty$。R630 的积分渐近给

$$
\psi_1=C e^{-st}t^{(s-1)/2}(1+O(t^{-1})),\qquad C>0,
$$

而对其反平方积分作一次分部积分，得

$$
\psi_1\phi_1=\frac1{2st}(1+O(t^{-1})).
$$

所写余项允许两次 $X$ 导数；它也可由二阶 ODE 递归读取。因此

$$
D^*(\psi_1\phi_1)
=\frac{1+2\eta}{2st}(1+O(t^{-1})),                       \tag{14}
$$
$$
D^*(\psi_1^2)=(4s^2t^2+O(t))\psi_1^2,
$$
$$
D^*(\psi_2^2)=(16s^2t^2+O(t))\psi_2^2,\qquad
D^*(\psi_3^2)=(36s^2t^2+O(t))\psi_3^2.
$$

后三者的指数衰减依次为 $e^{-2st},e^{-4st},e^{-6st}$；第一项 (14) 仅作代数衰减。一个恒等线性关系先除以 (14)，再依次除以后三项，其四个系数都必须为零。

由线性独立，可选四个有限点，使四个函数在这些点的值矩阵可逆：否则所有值向量的张成空间维数小于四，会给一个在整区间恒零的非平凡线性组合。以小不交邻域中积分为一的光滑 bump 逼近这些点评价，便得到真实有限宽的 $\chi_i$，使

$$
D_\tau(E_2,E_3,\mathcal C_1,\mathcal C_2)(0)
\quad\text{可逆}.                                      \tag{15}
$$

作一次常数可逆线性变换，把这四行导数化为单位阵。对最后两行应用有限维隐函数定理，得到一个二参数子族满足 (10)，且

$$
D_\mu(E_2,E_3)(0)=I_2.                                  \tag{16}
$$

这不是只写未知量个数：四行响应的公式、线性独立和实际 bump 选择均已给出。由于 $\rho$ 在整个四参数族上都固定，最终二参数子族准确保持中心行程角。由于 (10) 在负区之前已经恢复 Cauchy 数据，整个中央负曲率组件的物理 $r,w$ 都不变。

R630 第 7 节的局部源证明适用于任何固定有限个正区 bump。故在这一二参数族的一个固定小邻域内，$j\ge4$ 的中心逆仍有 $Cj^2$ 界；第二、第三模的固定紧支撑增广块也一致可逆。

## 3. Hu 平尾的全整数版本：所用尺度及扩展理由

两端分别取独立的尾序列。令 $d_n$ 为不小于 $e^{n^2}$ 的最小非平方整数，并置

$$
A_n=(d_n^{-1/2}+2d_n^{-9/2})^2,\qquad
B_n=d_n^{-9},
$$
$$
\lambda_n=e^{-n^{5/2}}\prod_{k=N}^n\sigma_k,\qquad
1\le\sigma_k\le2.                                      \tag{17}
$$

每个 Morse 小模型取 $\eta=0$，以
$r_{XX}=-\rho_n r,\ w=\lambda_n r_X$ 实现，截取其原稿规定的左右正 cap，连接长度取半径乘
$c_C\min(A_n,A_{n+1})^{12}$。正区用对 $\log w$ 导数的正插值匹配全部 germ。原稿 §7 的计算给

$$
|\partial_r^kw|\le e^{-n^{5/2}+C_kn^2},\qquad
\operatorname{dist}(\text{cell }n,\text{端点})
=e^{-n^2+O(n)}.                                        \tag{18}
$$

因此实际端点半径有限，且所有径向导数全平。每个负组件的特征行程角及全整数小除数为

$$
T_n=\frac{\pi}{2\sqrt{d_n}},\qquad
|\sin(kT_n)|\ge\frac1{3k\sqrt{d_n}}\quad(k\ge1).          \tag{19}
$$

以下四处是原稿的全部频率使用点；它们都允许每个整数 $j\ge2$。

**局部 Morse 谱。** 零能条件中的整数范数是
$j^2-d_n(2m+1)^2$，与 $j$ 的奇偶无关。因此原稿的
$\|H_{j,n}^{-1}\|\le8d_n^9$ 对所有整数 $j\ge2$ 成立。

**深尾。** gauge $u=r^{j^2}V$ 给

$$
(\mathsf p_jV_y)_y+j^2(j^2-1)\mathsf p_jV=0,\qquad
\mathsf p_j=wr^{2j^2-1}.
$$

正参数 $j^2(j^2-1)$、mass/resistance 乘积、对角占优和 continued fraction 收缩均不要求偶性。因此深尾的唯一自然线、$Cj^{-4}$ Hilbert 逆及

$$
|\partial_r^ku|\le \mathcal E_n^{C_k}e^{-S_n}             \tag{20}
$$

仍同时覆盖全部整数模式。固定任意 $j$，(20) 比任意固定次 $w$ 衰减得快。

**初始 cone 与入射斜率。** cone 的衰减解是 $r^{\pm j}$，
$|ru_r/(j^2u)|=1/j\le1/2$。其他 band 的 Riccati 比较也只用
$j\sqrt{A_{n-1}}$ 的下界。

**同时排除。** 取

$$
\mathcal H_n=C_*q_n A_n^{-1/2},\qquad
\mathcal I_n=\{j\in\mathbb Z:\mathcal H_{n-1}\le j<\mathcal H_n\}.
                                                               \tag{21}
$$

初始 band 收入所有 $2\le j<\mathcal H_N$。短正连接的无导数状态传递误差为

$$
O\!\left(q_n^2e^{-7n^2+O(n^{3/2}+n)}\right)=o(e^{-n^2}).
$$

对每个 $j\in\mathcal I_n$，原稿的代数 angle 排除区间长度不超过
$C\delta_n$，$\delta_n=c_0e^{-n^2}$。加入奇数至多把 band 个数界的常数增加一倍，仍有

$$
\sum_{n\ge N}C\,\#\mathcal I_n\,\delta_n
\le CC_*c_0\sum_{n\ge N}q_ne^{-n^2/2}<\frac12             \tag{22}
$$

（增大一次 $N$）。有限 product 上的 Fubini 排除和 coordinatewise 紧性仍选出**同一条尾**的全部 height ratios。自然线关于无限参数列的连续性来自同一个统一 continued-fraction 收缩，未改动。

这给出两个实际平尾及它们的辅助完整 cone。原稿 §8 的单核 $K$-slope 连接没有在本稿使用。

## 4. 固定物理连接与全域 profile 族

取第 2 节控制区 $I$ 左边的中心 cut $X_L$ 和唯一负组件右边的中心 cut $X_R$。稍后只需一次取充分远、仍有限的 cuts。

在正区写 $y=\log r$、$b_0(y)=rw_r/w$。由 R630 的转换，

$$
b_0=-\rho/\nu^2>0,\qquad \nu=r_X/r.
$$

在左远端 $b_0\to1$，在右远端

$$
b_0\longrightarrow
\frac{B}{(\eta+\sqrt{\eta^2+B})^2}>0.                     \tag{23}
$$

其固定阶 $y$-jets 在足够远的连接区域有统一界。以正 cutoff 插值将 $b_0$ 在一个有限 $y$ 区间接到 $b=1$，然后积分
$\partial_y\log w=b$。插值只在已是正区的地方发生，保持
$b\ge c>0$，在两端用常值 cutoff 匹配全部 germ。结果是一段真实 cone
$w=cr$。

在每端插入固定长 $L$ 的 cone head，再按 §3 选定的尾接上。尾可用半径 dilation
$\widetilde r=Rr,\ \widetilde w(Rr)=Rw(r)$ 放到所需半径，再乘一个正高度常数以匹配 $c$。这些操作不改变齐次核方程、尾的自然线、归一 angle、travel angle 或其 Hilbert 逆。

所有 cuts、插值、heads 和尾参数先固定。第 2 节的二参数控制在固定物理紧区内进行，因此它们全部**不随 $\mu$ 改动**。两端半径 $a,b$ 也固定。这得到实际的二参数全域 profile 族，尚未要求恰有双核。

除了中心一个负组件和 (17) 的两列 Morse 负组件，没有新增负曲率组件。中心行程角的界是 R630 的
$|\sin(kT)|\ge(3110k^3)^{-1}$，其他组件是 (19)。控制族准确保持这些角。

## 5. 全频增广逆：中心的 $j^2$ 代价如何进入真实组装

### 5.1 两个有限频率的中心 border

对于 $j=2,3$，在中心选一个紧支撑实列 $k_j$，与该模式的参考核配对非零，加入对称 row/column

$$
\mathbb H_j=
\begin{pmatrix}H_j&k_j\\k_j^*&0\end{pmatrix}.
$$

其逆存在：核配对先决定列系数，再用约化逆求补空间，最后由 row 决定核分量。R630 的加权核界保证这个有限秩操作在所需径向权中有界。小参数下仍一致可逆。对 $j\ge4$ 用 R630 的 $Cj^2$ 真逆。所有 border 支撑都在最终选取的正 buffers 内侧。

### 5.2 中心压缩的实际频率与 action

Hu §9 的 “Compression through positive intervals” 引理允许一般完整自伴模型，及一个紧支撑对称 border；其输入是一个明确的逆界 $B_0$，并不要求它与 $j$ 无关。这里

$$
B_0\le C(1+j)^2.                                       \tag{24}
$$

左中心 cut 的 Schrödinger 频率和保留正 buffer 的 action 可取

$$
m_{L,j}\asymp j e^{-X_L},\qquad
S_{L,j}\ge c j e^{-X_L};
$$

右中心 cut 可取

$$
m_{R,j}\asymp j,\qquad
S_{R,j}\ge c j(X_R-X_{\mathrm{fix}}),                    \tag{25}
$$

其中 $X_{\mathrm{fix}}$ 在右正区内固定，常数包含固定 $B>0$。左侧取固定 $X$ 宽的分段 buffer，右侧取增长的正区长度；cut 和内层的势上下界满足压缩引理的假设。

因此其小误差条件 $B_0m_{i,j}^2e^{-S_{i,j}}\ll1$ 对全部
$j\ge2$ 可由一次有限选择 $X_L\ll0$、$X_R\gg1$ 同时实现。紧支撑控制不改变 buffers，故这也是一个固定小 $\mu$ 邻域的统一选择。

物理 conormal 变换包含 Liouville 项。若 $\epsilon_i=-1$、$1$ 分别表示左、右外法向，则中心精确 leading impedance 为

$$
\kappa_i=\lambda\mathcal P_i
                 (\alpha_i^{\mathrm{in}}+\epsilon_i\eta).
                                                               \tag{26}
$$

左 cut 充分远时 $\alpha_i^{\mathrm{in}}\gg\eta$；右边则直接为正。因此
$\kappa_i>0$ 且与 $\lambda\mathcal P_i m_{i,j}$ 可比。这里没有遗漏 gauge 项。

### 5.3 其他模型和内部界面

固定 $j$，令 $n$ 是 (21) 的 transition index。此前每个尾模型
$m<n$ 满足
$\tau_{m,j}:=j\sqrt{A_m}\ge C_*q_m$。Hu 的局部 inverse、正 buffer 压缩与 (26) 给 Dirichlet 模型逆及其 Poisson maps。

把正连接的**完整** derivative matrix 保留为 $\Lambda_C$，不丢弃短连接的大 off-diagonal 项。内部精确 matching matrix 为

$$
S=S_0+E,\qquad
S_0=\operatorname{diag}(\kappa_i)+\bigoplus_C\Lambda_C,
\qquad S_0\ge\operatorname{diag}(\kappa_i)>0.              \tag{27}
$$

控制其归一误差的三种项是

$$
\mathcal E_m^{C(M)}(1+j)^C e^{-c\tau_{m,j}},
$$
$$
C(1+j+e^{-X_L}+X_R)^C
  e^{-c\min(j e^{-X_L},\,j(X_R-X_{\mathrm{fix}}))},
$$
$$
C_N(1+j)^C e^{-cjL}.                                   \tag{28}
$$

相较原稿，(24) 只增加 (28) 的一个固定多项式次数。先选 coefficient exponent，继而选 $C_*,N$，最后选固定的中心 cuts 与 heads，即可将全部局部归一误差压到 $1/8$ 以下。每个模型只占两条相邻界面，故有界重叠给整个矩阵

$$
\|S_0^{-1/2}\Omega^{\pm1}E\Omega^{\mp1}S_0^{-1/2}\|<1/2,
                                                               \tag{29}
$$

其中 $\Omega$ 是在每个 gap 上常值的边界权。该估计与模型个数无关。真实零边界内域逆仍是

$$
G_h=D_h+T_hS^{-1}T_h^*.                                 \tag{30}
$$

在强 leading energy norm 下，Poisson maps 有 $C/j$ 界；完整中心逆作用于 cutoff residual 的额外 $j^2$ 已被 (28) 的指数吸收。于是 matching correction 仍是 $O(j^{-2})$，直接中心块的代价为 $O(j^2)$。其他直接块的 coefficient exponents 由输出权支付，故

$$
\|G_hF\|_{\gamma,-M'}\le C(1+j)^2\|F\|_{\gamma,M}.         \tag{31}
$$

在整个有限内域只取其最大 coefficient weight，则还有原稿末端匹配所需的粗界

$$
\|W^{\pm1}G_hW^{\mp1}\|\le\mathcal E_n^C.                \tag{32}
$$

确实 $j<\mathcal H_n$ 给
$\log(1+j)^2=O(n^2+\log q_n)=O(q_n)$，所以新增的 $j^2$ 也被 (32) 吸收。这一处不能把中心 $j^2$ 当成免费，但它只改变明确的固定 $C$。

### 5.4 两个真正尾端的最后 matching

原稿 §9 的 complementary Robin 逆不要求自然端点线在入口的高度非零。它以其完整 Cauchy 向量为单位向量，取正交线作 Robin 条件，故适用于这里选定的全部整数模式。

每端 transition core 的 transfer、质量、深尾 Poisson 因子给

$$
\mathcal K_n=e^{Cn^2+C_o\tau_{n,j}},\qquad
\|R_o\|\le\mathcal E_n^C\mathcal K_n^2,
$$

并保留深尾 kernel 因子 $e^{-|S_k-S_m|}$。真正 matching angle 至少
$\delta_n=c_0e^{-n^2}$，需扣除的内域 boundary-matrix 误差由 (32) 与两个前置正 buffer 因子控制。

落在 transition index 及以外的输出项，其代价

$$
\mathcal E_n^C\delta_n^{-1}e^{C_o\tau_{n,j}}
\le\mathcal E_n^{C'}
$$

由 $j<\mathcal H_n$ 和增加输出 coefficient exponent 支付。回到固定内域的每一项，则在花费此代价之前先包含

$$
e^{-c\tau_{n-1,j}},\qquad
\tau_{n-1,j}/\tau_{n,j}\asymp e^n,
$$

或初始 band 的 $e^{-cjL}$。因此

$$
\mathcal E_n^C\delta_n^{-1}
 e^{C_o\tau_{n,j}-c\tau_{n-1,j}}
$$

统一有界，并可满足末端 $2\times2$ matching 的 Neumann 小误差条件。新增中心因子在 (32) 中已支付，不会在固定内域输出重新变成一个未控制的 coefficient factor。

这给真实全域两侧 inverse identities、普通 $dr$ Green reciprocity 及 (7)。整个参数小邻域共用同一正 buffer 和 angle 选择。

这些几何选择也不必随着 $[\gamma_-,\gamma_+]$ 改动。相邻 cell 的权比满足

$$
\left|\log(W_{m+1}/W_m)\right|
\le Cm^2+CMm^{3/2}\log(e+m)\qquad(|\gamma|\le1).
$$

该界没有 $(1-|\gamma|)^{-1}$ 因子。先用原始源密度转换选择一个固定源 coefficient exponent，再仅用 $|\gamma|\le1$ 选择 (28)、(29) 的几何。固定紧区间以后，远端 kernel 的 Schur 求和使用
$e^{-(1-|\gamma|)|S_k-S_m|}$；它只改变逆的常数和允许的输出 coefficient exponent，不改变已经选定的 profile。新增的中心 $j^2$ 因子与 $\gamma$ 无关，故这一选择顺序仍有效。

各深尾的自然线唯一性使端点属于该自然 realization。固定 $j$ 的 graph-domain 解在紧区 $H^2_{\mathrm{loc}}$，值和 conormal 必须跨每个有限界面连续；匹配矩阵和各块逆给唯一性。由截断、磨光和有限频率逼近源，再用已构造的逆，得到光滑 admissible fields 在 maximal graph norm 中稠密。这是实际 graph-domain 逆，而不是只在有限 Fourier 多项式上的形式解。

## 6. 两条真实端点线对中心双控制的 $C^1$ 收敛

第 5 节先给带两个有限 border 的全域逆；现在恢复原始算子的两条零模。

### 6.1 正区传递的低频收敛

仅在本小节固定 $j=2$ 或 $3$。在一个严格正 Schrödinger 区间中，
$\psi''=V\psi$、$V\ge m^2>0$。从右端向左传播非负外向 impedance
$p=-\psi'/\psi$，它满足逆向 Riccati 方程

$$
\partial_Yp=V-p^2.
$$

与 $m\tanh(mY)$ 比较得，经过初始宽 $1/m$ 后 $p\ge cm$。两条这种线的差在原坐标满足

$$
\partial_X(p_1-p_2)=(p_1+p_2)(p_1-p_2).
$$

因此从远端移向固定内截面，差至少以 $Ce^{-cm\ell}$ 衰减；若两端数据在参数上 $C^1$ 且其导数有固定多项式界，相同计算对导数也给这种衰减。这里 reference buffers 完全在控制区外，$V$ 不依赖控制参数，所以微分不产生沿长 buffer 的新增 forcing。

自然尾在辅助 cone 上为 $C_+r^j+C_-r^{-j}$。右尾的所选 angle 保证 $C_-\ne0$，左尾相应保证 $C_+\ne0$。对当前固定两个频率，系数比有限；长 cone head 使入口线以 $O(e^{-2jL})$ 趋于指向自然尾的衰减 cone 线。经过固定的严格正连接后，得到非负、有限的外向 impedance。中心 cuts 取足够远，其 gauge 后 impedance 也满足上述正区比较条件。

于是，在固定中心截面读取并作非零线性规范化的左右真实端点线，分别趋于完整 Morse 参考的左右 $L^2$ 线。收敛包括两个参数的一次导数，误差可记为

$$
\varepsilon(X_L,X_R,L)
\le C(1+e^{-X_L}+X_R)^C
 \big(e^{-c e^{-X_L}}+e^{-c(X_R-X_{\mathrm{fix}})}\big)
 +C_{\mathrm{tail}}e^{-2L}
\longrightarrow0.                                     \tag{33}
$$

这个估计只用于固定的 $j=2,3$，不拿它代替第 5 节的全频共同逆。左远端的正 buffer 可以取固定 $X$ 宽，$\rho$ 的二次指数增长给第一项；右端正势有固定下界，给第二项。

第 2 节保持了两个径向 Cauchy 数据，所以外部连接和真尾不随参数变化。它们在 (33) 中的参数导数为零；中间有限传播的参数依赖由普通线性 ODE 得 $C^1$。这排除了“尾随着控制改变但没有估导数”的缺口。

更具体地，可在控制区两侧固定各一个正区截面。真实尾线与参考线在这些截面的误差都不依赖 $\mu$；其后的差别只经过固定有限区间上、对 $\mu$ 光滑的传递矩阵。对该矩阵和规范化的乘除法微分，误差仍为 $O(\varepsilon)$。因此 (35) 的 $C^1$ 结论不需要对无限尾参数求导。

### 6.2 有限维隐函数恢复双核

令 $\Phi_j^\infty(\mu)$ 为完整中心的两个稳定线在固定截面的 Wronskian，令
$\Phi_j^{\mathrm{flat}}(\mu)$ 为左右**真实全平端点线**的同样 Wronskian。规范化截面选在两条零模都非零的固定位置；小参数下可用相同规范化。

完整中心处，$\Phi_j^\infty(0)=0$。对稳定解方程作 Green 恒等式，得到

$$
\partial_{\mu_i}\Phi_j^\infty(0)
=c_j\int\psi_j^2\,\partial_{\mu_i}V_0\,dX,\qquad c_j\ne0.
                                                               \tag{34}
$$

这里 $c_j$ 只由两条稳定线的非零规范化因子及 Wronskian 方向决定。式 (16) 因而给

$$
\det D_\mu(\Phi_2^\infty,\Phi_3^\infty)(0)\ne0.
$$

(33) 给

$$
(\Phi_2^{\mathrm{flat}},\Phi_3^{\mathrm{flat}})
\longrightarrow(\Phi_2^\infty,\Phi_3^\infty)
\quad\text{于一个固定小邻域的 }C^1\text{ 范数}.            \tag{35}
$$

取一次充分远而有限的 cuts 和 heads，有限维隐函数定理给
$\mu_* \to0$，使

$$
\Phi_2^{\mathrm{flat}}(\mu_*)=
\Phi_3^{\mathrm{flat}}(\mu_*)=0.                          \tag{36}
$$

最终 $w_*=w_{\mu_*}$ 固定。左右自然线准确相同，所以两条非零核在真正平帽端全平，满足 (20)。两个端点的自然线均一维，故每条频率的全域核至多一维。第 5 节的未增广 $j\ge4$ 逆排除了其他全部整数频率的核。这证明 (1)、(2)。

再对真实 Wronskian微分，(34) 的物理版本是 (4)，只差每行一个非零规范化因子。(35) 保证该矩阵在 $\mu_*$ 仍可逆。这也证明了最终全域背景上的真实紧支撑双参数横截性。

## 7. 零、一模以及物理 profile 列

上述两条 border 的构造没有支付低频零、一模，需使用它们正确的端口条件。对普通源
$L_0u_0=f_0$、$L_1u_1=f_1$，固定外帽，分别要求

$$
\int_a^b f_0\,dr=0,\qquad \int_a^b r f_1\,dr=0.
$$

设

$$
J_0(r)=\int_a^r f_0(s)\,ds,\qquad
J_1(r)=\int_a^r s f_1(s)\,ds.
$$

则由 [R629](R629-nonlinear-curvature-moments-and-double-kernel-reduction.md)，准确逆为

$$
u_0(r)=-\int_r^b J_0(s)/w_*(s)\,ds,
$$
$$
u_1(r)=-r\int_r^b J_1(s)/(w_*(s)s^2)\,ds.                \tag{37}
$$

内帽的一个高度常数和一个真实倾斜系数自由；外帽固定。减去固定的内帽高度 step 和 $r\cos\theta$ 倾斜 cutoff 后，剩余场有 (6) 的全平尾界。因为 $a,b$ 固定且 $w_*^{\pm1}$ 在第 $n$ 个 cell 只花 $\mathcal E_n^C$，(37) 的尾和、除法与积分仅改变固定 coefficient exponent，不增加新的角频代价。

反射空间中第一模只有余弦，故低频有上述两个相容条件；不加反射时还须加第一正弦矩和相应内帽倾斜分量。R629 的非线性三矩身份说明这些不是任意外力，但本稿这里只建立其线性参考逆。

第 5 节为方便使用了各单频的对称紧 border。转为真实二参数 profile 列时，使用 (4) 的可逆矩阵：先将源与两条核配对，解这个 $2\times2$ 系统得到参数系数；减去两条真实形状列后用共同约化逆；最后加入核分量满足两条固定规范化 row。所有列和 row 都紧支撑，有限秩变换在 (6) 的同一空间中有界。这给 R629 双核有限块所需的实际全域参考输入。

## 8. 此后不能省略的非线性与有限几何步骤

本稿已接入真实平尾，并在同一个固定 profile 上支付全整数径向参考逆，恢复两条准确核，且把 profile 参数限制到固定物理紧区。与 R628 只给固定有限频率端点线的情形相比，全频参考这一缺口在所引用并逐项扩展的线性框架内已闭合。

不过，以下量仍不能跨构造借用：

- R628 的 $\beta=15/8$ 来自其分段中心，不能当作本稿 Morse 中心的端口系数。
- 本稿的低频 $C^1$ 匹配采用左正规径向解。右 type root 上取小 $\nu$ 的有限分支只有有限左正区，不能直接使用 (33) 的远切口论证。
- (7) 是径向参考的逆。求非零有限幅值等距根，还需控制非径向状态的特征返回图、所有小除数及 residual-corrected 线性化。中心行程角在控制参数中固定，并不等于它在任意非线性状态中自动固定。
- 即使取得小幅准确嵌入，也还须把真实内帽刚体姿态、全像握持 Hausdorff 位移及 reach/直径在同一个有限模型中量化。

这些是继续构造要支付的输入；本稿没有以参考 inverse、无限远切口极限或尚未量化的小幅分支代替 README 的完成标准。
