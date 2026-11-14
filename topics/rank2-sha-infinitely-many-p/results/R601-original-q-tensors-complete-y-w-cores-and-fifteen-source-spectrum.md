# R601 — 原 Q 两张量、完整 Y/W 核与真实十五维算术谱

日期：2026-11-14。**状态：已证明。**

本篇直接处理 R599 的同一个完整补偿来源。
实际 $Q$ 三次角投影将它分成两个固定低 degree 张量支；
它保持原矩形，但其测试必须按真实 $Q$ 旋转运输。

两个支在整个五变量格上满足明确的核心：
$Y$ 一层与 $W$ 四层都将两支负交换，前者保一个实际 $Y$ 反射。
全部 half-period 中心相位与绝对标量在下文支付。
这也给 R599 补偿来源的两个非齐次核心，强迫项就是原矩形的两个
真实像；这两个像与原矩形严格不交，余补域仍保留。

对含原负五矩的支，其实际 $Y$ 边际已算完整二十三坐标。
共同 CM 来源空间恰十五维：原 $S$ 系数为 $1/2$，
两条秩零参考的质量相反，四个三维外块均非零，
而新 $E_{2312}$ 线的整个投影为零。
不将这些参考或外块的中央导数赋零。

## 1. 原五变量来源与可真正交换的 Q 投影

沿用
[R466](R466-fixed-two-division-sources-and-new-rank-two-sextic-curve.md)、
[R572](R572-original-c-splitting-and-simple-pole-unit.md)、
[R590](R590-original-six-carry-branches-and-sole-b-fibre.md)、
[R594](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md)、
[R599](R599-original-complement-and-negative-five-return.md)
的同一个原射线、全部坏集和周期：
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1,\quad\Omega\in\mathcal O^\times.
\tag{1}
$$
当前 $p\ge71$、$p\equiv7\bmod64$。

保全部五个物理变量 $\mathbf x=(Z,Q,r,c,d)^t$，定义
$$
\boxed{
\begin{aligned}
\nu_1&=\frac1{42}\nu_{f_1}(Z)\otimes\nu_\Sigma(Q)
          \otimes\nu_\sigma(r)\otimes\nu_\sigma(c)\otimes\nu_\sigma(d),\\
\nu_2&=\frac1{42}\nu_{f_3}(Z)\otimes\nu_\Theta(Q)
          \otimes\nu_\sigma(r)\otimes\nu_\sigma(c)\otimes\nu_\sigma(d),\\
\nu^\flat&=\nu_1-\nu_2 .
\end{aligned}}
\tag{2}
$$
这里 $f_1=-x_\wp y_\wp\sigma^6,\ f_3=-y_\wp\sigma^6$、
$\Sigma=\sigma^2,\Theta=x_\wp\sigma^2$，符号和 $1/42$ 均未变。

令 $R_Q$ 只把实际 $Q$ 乘 $\omega$，逐个固定其余四输入。
因为 $\Sigma$ 型二、$\Theta$ 型零，完整来源恒等式是
$$
\boxed{
\nu_1=\frac13\sum_{j=0}^2\omega^{-2j}(R_Q^j)_*\nu^\flat,\qquad
-\nu_2=\frac13\sum_{j=0}^2(R_Q^j)_*\nu^\flat .
}
\tag{3}
$$
这是原完整有界测度的等式，未新增曲线中央。

保 R599 的实际矩形
$$
\mathscr R_n=\{Z\ {\rm unit},\ Q,r,c,d\in p^n\},\qquad n\ge1.
\tag{4}
$$
$R_Q$ 保持 (4)，所以 (3) 可以与这个切集或其整个补集交换。
但它将原两个观察中的 $a_QQ$ 换成 $\omega^j a_QQ$；
同一测试的两个 Mellin 单位条件和 log 必须同时运输。
这里没有将 $R_Q$ 称为保原 $Y/W$ 的几何。

## 2. 全五坐标中的 Y/W 方向

记
$$
a_Z=(-2+\omega)/2,\quad a_Q=(4+3\omega)/2,\qquad
G_5=\operatorname{diag}(6,2,1,1,1).
$$
原完整观察是
$$
\boxed{
\begin{aligned}
Y&=a_ZZ+a_QQ+2\delta r+c+2d,\\
W&=a_ZZ+a_QQ+2\delta r+3\delta c+4d .
\end{aligned}}
\tag{5}
$$
以行 $L$ 表示线性形式，用
$N(L)=L G_5\bar L^t$。准确有
$$
N(Y)=34,\qquad N(W)=72,\qquad
\langle Y,W\rangle=37-3\delta .
\tag{6}
$$
对 $L=Y,W$ 定义整个物理算子
$$
\boxed{
P_{L,t}=I+(t-1)\frac{G_5\bar L^tL}{N(L)} .
}
\tag{7}
$$
它使 $L$ 乘 $t$，固定其全部正交伴随；
分母在当前处都是单位。
特别 $R_Y=P_{Y,-1}$ 是完整五变量中的真实反射。

例如四个坐标减去相应 $Y$ 投影，连同 $Y$ 构成完整框架。
其分母只含当前的单位，且交叉 Gaussian 项全零。
在第一 $Y$ 方向取 $[2]$，(2) 的实际五因子参数系数为
$$
\boxed{(-\bar\gamma,\ a_{13},\ 4\delta,\ 2,\ 4),\qquad
\bar\gamma=2-\omega,\quad a_{13}=4+3\omega .}
\tag{8}
$$
所以整个第一格是 standard even $\mathcal S_{136}$。
第一 $W$ 的同一固定覆盖则为
$$
\boxed{(-\bar\gamma,\ a_{13},\ 4\delta,\ 6\delta,\ 8),}
\tag{9}
$$
整个第一格为 standard even $\mathcal S_{288}$。
其余四个完整伴随保留，未仅比较一个边际。
这些固定覆盖在当前处都是单位，故还原物理深度时与 restriction
和 $\kappa$ 缩放严格相容。

## 3. 两个 whole 核的完整中心与绝对锚

写 $K_N$ 为去掉原外部 $\lambda$ 和物理 $\kappa$ 缩放后的
整个 standard even $\mathcal S_N$ 核。
令
$$
B_N=\frac12\sum_{t\in E[2]}T_t^{(N)}-I .
$$
本节的 $N=136,288$ 都被八整除。
在完整 Schrödinger 基上，
$$
\boxed{
B_Ne_j=(-1)^j e_{(1+N/2)j+N/2}.
}
\tag{10}
$$
特别它将两个完整 Heisenberg 生成元分别送到
$-\mathsf X^{1+N/2}$、$-\mathsf Z^{1+N/2}$。
这些负号来自中心，不能只按模 $N$ 的坐标置换省掉。

### 3.1 整个 degree136

R466 的当前射线给
$$
g_\pi=(203,136)\pmod{272}.
$$
第一生成元的完整像由
$203/136+\omega=67/136+(1+\omega)$ 得到，
第二个由 $-1+(67/136)\omega$ 得到。
两次格约化的中心符号都是负一，所以真实交织为
$-\mathsf X^{67},-\mathsf Z^{67}$。
这与 $R_YB_{136}$ 完全相同。

原非零锚 $S(2z)$ 满足
$K_{136}S(2z)=S(2z)$，且为偶函数、全部二挠 lift 固定。
故不可约性给整个空间的绝对式
$$
\boxed{K_{136}=R_YB_{136}.}
\tag{11}
$$
这也与 R466 已付的 $K_{136}=-N_7^9$ 一致。

### 3.2 整个 degree288 的第四幂

当前已有
$\pi_0\equiv-1+2\omega\bmod64$、$\pi_0\equiv1\bmod27$。
在整个中心模 $576$ 上，
$$
\boxed{
g_\pi=(91,72),\quad
g_\pi^2=(217,432),\quad
g_\pi^4=(433,288),\quad
g_\pi^8=(289,0).
}
\tag{12}
$$
$g_\pi^4$ 对两个生成元的真实交织为
$-\mathsf X^{145},-\mathsf Z^{145}$：
其整数代表分别是 $(433,288)$ 和 $(-288,145)$，
两个 Weyl 中心指数均为奇数。
所以 $K_{288}^4$ 与 (10) 的 $B_{288}$ 只差一个共同标量。

真实原锚 $T(2z)$ 的核心为 $+1$，来自原 $T_{72}$ 的完整核心
及固定 $[2]$ 拉回。
它的四个二挠 lift 全固定，故 $B_{288}T(2z)=T(2z)$。
这支付所剩绝对标量：
$$
\boxed{K_{288}^4=B_{288}.}
\tag{13}
$$
本篇没有由模 $288$ 的交织免费定号，也没有宣称 $K_{288}$ 自身
在两个来源上是一层 scalar。

## 4. 全 half-period 相位与两张量的准确负交换

令 $t=\alpha/2$，$\alpha$ 为原周期格向量。
在 (8) 或 (9) 的前两个因子中，
$$
-\bar\gamma t=\omega t-\alpha,\qquad
a_{13}t=\omega t+(2+\omega)\alpha .
\tag{14}
$$
将它们分别在 degree6、degree2 的 canonical lift 中降为
同一个 $\omega t$ 时，产生完整符号
$$
(-1)^{3E(\omega\alpha,-\alpha)+
             E(\omega\alpha,(2+\omega)\alpha)}
=(-1)^{N\alpha}.
\tag{15}
$$
这里 $E$ 是原整交替形式；两个行列式分别为
$N\alpha,-2N\alpha$。

原 odd sigma 的周期特征是
$\chi(\alpha)=(-1)^{N\alpha}$。
在 $Y$ 三个 sigma 因子中，平移为
$2\delta\alpha,\alpha,2\alpha$，其总符号正是
$\chi(\alpha)$。
在 $W$ 中为 $2\delta\alpha,3\delta\alpha,4\alpha$，
其总符号也为 $\chi(\alpha)$，因为 $N\delta=3$。
它与 (15) 精确相消。

完整 Gaussian 因子也相消：原正交伴随满足
$\sum N_i\bar a_i u_i=0$，故各因子的 canonical 平移乘积
正是整个 first-axis 的 lift。
因此 (11) 或 (13) 中的 $B_N$ 在 (2) 上准确归结为
$$
\boxed{\mathfrak B=
\frac12\sum_{s\in E[2]}T_s^{(6)}\otimes T_s^{(2)}-I}
\tag{16}
$$
作用于实际 $Z,Q$ 两因子，逐个保其余三个 sigma。
没有留下一个未记录的 $\chi$ 或 flat twist。

这个小算子可直接用原 sigma 加法式计算。
置 $P_1=f_1(z)\Sigma(q)$、$P_2=f_3(z)\Theta(q)$。
对非零二挠点 $t=(e,0)$，$e^3=-b$，canonical 常数满足
$c_t^4=(3e^2)^{-1}$，且
$$
\sigma_t(z)^2=c_t^2(x_\wp(z)-e)\sigma(z)^2,\quad
x_\wp(z+t)=\frac{e(x_\wp(z)+2e)}{x_\wp(z)-e},\quad
y_\wp(z+t)=\frac{-3e^2y_\wp(z)}{(x_\wp(z)-e)^2}.
$$
所以两个完整乘积分别为
$$
(T_t^{(6)}f_1)(z)(T_t^{(2)}\Sigma)(q)
=\frac{y_z\sigma(z)^6\sigma(q)^2}{3e}
 (x_z+2e)(x_q-e),
$$
$$
(T_t^{(6)}f_3)(z)(T_t^{(2)}\Theta)(q)
=\frac{y_z\sigma(z)^6\sigma(q)^2}{3e}
 (x_z-e)(x_q+2e).
$$
对三个 $e$ 求和，用 $\sum e=\sum e^{-1}=0$ 得
$$
\sum_{t\ne0}T_tP_1=P_1-2P_2,\qquad
\sum_{t\ne0}T_tP_2=-2P_1+P_2 .
$$
再加原点项，完整得到
$$
\boxed{\mathfrak B P_1=-P_2,\qquad \mathfrak B P_2=-P_1.}
\tag{17}
$$
这是整个二变量函数恒等式，故保持全部四个 first-axis 伴随，
不是只由 $q=0$ 的质量确定一个候选矩阵。

## 5. 全五变量的两个真实核心与补偿来源

由 (11)、(13)、(17)，还原原 $\lambda,\kappa$ 后，对 $i=1,2$
准确有
$$
\boxed{
\nu_i|_{\{Y\in p\}}
=\beta(P_{Y,-\kappa})_*\nu_{3-i},\qquad
\nu_i|_{\{W\in p^4\}}
=-\lambda^4(P_{W,\kappa^4})_*\nu_{3-i}.
}
\tag{18}
$$
第一式的负物理尺度包含真实 $Y$ 反射，不能改成
$P_{Y,\kappa}$ 后删掉域的变化。
特别原差来源满足
$$
\boxed{
\nu^\flat|_{\{Y\in p\}}
=\lambda(P_{Y,-\kappa})_*\nu^\flat,\qquad
\nu^\flat|_{\{W\in p^4\}}
=\lambda^4(P_{W,\kappa^4})_*\nu^\flat .
}
\tag{19}
$$
两层 $Y$ 或八层 $W$ 返回各自同一个支。
一个 $Y$ 步和一个 $W^4$ 步也返回同一个支，外部 scalar 为
$\lambda^5$，但物理矩阵的次序不得交换。
例如完整真词域
$$
\{Y\in p,\ W(P_{Y,-\kappa^{-1}}\mathbf x)\in p^4\}
$$
上的来源是
$$
\lambda^5(P_{Y,-\kappa}P_{W,\kappa^4})_*\nu_i .
\tag{20}
$$
这保全部旧观察和条件，不是只写一个来源矩阵。

### 5.1 R599 同一个补偿的来源与非齐次核

在完整五维中定义
$$
r_{i,n}=1_{\mathscr R_n}\nu_i,\qquad
\eta_{i,n}=(1-1_{\mathscr R_n})\nu_i,\qquad
\eta_n=\eta_{1,n}-\eta_{2,n}.
\tag{21}
$$
R599 的两个实际加权补项相加后，准确给
$$
\boxed{\eta_n(\ell)=\mathcal E_n.}
\tag{22}
$$
这里必须先保原 $O_n+K_n$ 的完整和：
单独 $O_n$ 或 $K_n$ 不能改成 (21) 的来源。
式 (3) 与 (21) 交换，因而也准确分离这个同一个补偿来源。

矩形 (4) 上 $Y,W$ 均单位，所以 (18) 给两个完整非齐次式
$$
\boxed{
\eta_{i,n}|_{\{Y\in p\}}
=\beta(P_{Y,-\kappa})_*(\eta_{3-i,n}+r_{3-i,n}),
}
$$
$$
\boxed{
\eta_{i,n}|_{\{W\in p^4\}}
=-\lambda^4(P_{W,\kappa^4})_*(\eta_{3-i,n}+r_{3-i,n}).
}
\tag{23}
$$
强迫项是整个真实矩形来源，不是一个先取质量的常数。
这是 R599 同一个 $\mathcal E_n$ 的来源/核接口，未增加新的中央零。

### 5.2 两个实际像及仍保留的余补域

令
$$
\mathscr R_n^Y=P_{Y,-\kappa}\mathscr R_n,\qquad
\mathscr R_n^W=P_{W,\kappa^4}\mathscr R_n .
\tag{24}
$$
其完整逆域分别是
$$
Y\in p,\quad P_{Y,-\kappa^{-1}}\mathbf x\in\mathscr R_n,
\qquad
W\in p^4,\quad P_{W,\kappa^{-4}}\mathbf x\in\mathscr R_n .
\tag{25}
$$
所以每个原 $Z,Q,r,c,d$ 条件及 $\kappa$ 逆幂都明确保留。

在原矩形上模 $p$ 只有 $Z$ 自由。实际 (7) 给
$$
\begin{aligned}
Z(P_{Y,0}\mathbf x)&\equiv(47/68)Z,&
W(P_{Y,0}\mathbf x)&\equiv
a_Z\frac{-3(1+\delta)}{34}Z,\\
Z(P_{W,0}\mathbf x)&\equiv(41/48)Z,&
Y(P_{W,0}\mathbf x)&\equiv
a_Z\frac{35+3\delta}{72}Z .
\end{aligned}
\tag{26}
$$
另四个原坐标在两个像中的系数均为当前处单位，完整列在证书。
$47<71$ 且 $47\equiv47\bmod64$，$41<71$；
$N(35+3\delta)=4\cdot313$ 而 $313\equiv57\bmod64$。
所以无需细分原射线，准确有
$$
\boxed{
\mathscr R_n^Y\subset
 \{v_p(Y)=1,\ W\ {\rm unit},\ Z,Q,r,c,d\ {\rm unit}\},
}
$$
$$
\boxed{
\mathscr R_n^W\subset
 \{Y\ {\rm unit},\ v_p(W)=4,\ Z,Q,r,c,d\ {\rm unit}\}.
}
\tag{27}
$$
三域 $\mathscr R_n,\mathscr R_n^Y,\mathscr R_n^W$ 严格不交；
后两域都在原 $\eta_n$ 的真正外矩形中。
其余补集仍完整存在，不能由三域不交赋它零值。

对任意完整有界测试 $f$，(18) 准确给
$$
\int_{\mathscr R_n^Y}f\,d\nu_i
=\beta\int_{\mathscr R_n}f(P_{Y,-\kappa}\mathbf x)\,d\nu_{3-i},
$$
$$
\int_{\mathscr R_n^W}f\,d\nu_i
=-\lambda^4\int_{\mathscr R_n}f(P_{W,\kappa^4}\mathbf x)\,d\nu_{3-i}.
\tag{28}
$$
若 $f$ 含 R594 的 $\widetilde{\mathcal W}_n(F,G)$，则 $F,G$
和其中七个余类矩也必须按 (7) 同时转置。
只对已完整相加后的 (22) 使用无权补偿来源。

## 6. 实际 Q 第一支的整个 Y 多项式

令 $P_Y(z)$ 是 $Y_*\nu_1$ 的真实生成函数，
$F_Y(z)=P_Y(2z)$。由 (2)、(5) 的原因子，准确有
$$
\boxed{
F_Y(z)=-\frac1{42}
 f_1(\bar\gamma z)\,
 \Sigma(a_{13}z)\,
 \sigma(4\delta z)\sigma(2z)\sigma(4z)
 \in\mathcal S_{136}^{\mu_6=0}.
}
\tag{29}
$$
这里 $\bar\gamma=2-\omega$，$a_{13}=4+3\omega$。
负号来自 $f_1(-z)=-f_1(z)$，没有改原 $1/42$。
另一支的真实 $Y$ 边际是 $P_Y-S$。

以下给它的整个多项式，而不是只比较首项。
置 $X=x_\wp^3$，以及
$$
r_7=\frac{8+12\omega}{7}b,\quad q_7=X-r_7,\quad
U_7=X^2+(28r_7+12b)X+r_7(7r_7+24b),
$$
$$
V_7=(U_7+3XU_7')q_7-6XU_7,
\quad
q_{13}=X^2-(4+12\omega)bX+\frac{16-48\omega}{13}b^2,
$$
$$
R_2=X^2+20bX-8b^2,\qquad
V_4=X^4-536bX^3-1344b^2X^2-2048b^3X-512b^4 .
$$
则
$$
\boxed{
\frac{F_Y}{\sigma^{136}x_\wp^2}
=-\frac{16\bar\gamma\delta a_{13}^2}{21}
 (X+b)^2q_7U_7V_7q_{13}^2R_2^2(X-8b)V_4 .
}
\tag{30}
$$
这是 degree21 的全多项式。
使用 R541/R490 的原 CM13 division 多项式和原 CM7 公式，
$$
\sigma(\bar\gamma z)=\bar\gamma\sigma^7q_7,\quad
x_\wp(\bar\gamma z)=\frac{x_\wp U_7}{\bar\gamma^2q_7^2},\quad
y_\wp(\bar\gamma z)=\frac{y_\wp V_7}{\bar\gamma^3q_7^3},
$$
以及
$$
\sigma(4z)=-4y_\wp\sigma^{16}R_2,\qquad
x_\wp(4z)=
 \frac{x_\wp(X-8b)V_4}{16(X+b)R_2^2},\qquad
\sigma(4\delta z)=\delta x_\wp(4z)\sigma(4z)^3
$$
即可逐项得到 (30)；全部幂、符号和常数已保留。

其首项为
$$
F_Y(z)=\frac{752-320\omega}{21}z^6+O(z^{12}),
\qquad F_Y(0)=0 .
\tag{31}
$$
(31) 不用于猜任何 CM 特征。
下节使用整个二十三坐标确定实际算术分量。

## 7. 完整 CM7/13/19 谱，保两个参考与四外块

使用 R466/R542 已付的整个二十三维矩阵，
在基 $\sigma^{136}x_\wp^2X^j,\ 0\le j\le22$ 上记
$$
M=N_7,\qquad
D=\omega^{-1}N_{19}M^{-2}.
$$
完整 principal 关系为
$$
M^{18}=I,\quad D^2=I,\quad DM=MD,\qquad
N_{13}=M^{23}=M^5,\quad N_{19}=\omega DM^2 .
\tag{32}
$$

### 7.1 负块和实际新线

对 (30) 的完整向量，精确有
$$
\boxed{\frac{I-M^9}{2}F_Y=\frac12S(2z).}
\tag{33}
$$
$M$ 的实际最小多项式为
$$
\boxed{(t+1)(t-1)(t^6+t^3+1).}
\tag{34}
$$
整个 $M=\omega$、$M=\omega^2$ 投影均为零；
$-\omega,-\omega^2$ 两条也为零。
所以新 $E_{2312}$ 对应的整条共同投影准确为零，
不是只根据其质量为零作排除。

### 7.2 两条原 rank0 参考

令 $H_1^{\rm ref}$、$H_4^{\rm ref}$ 是 R466 已完成全部角色识别、
在共同 $b$ frame 中规范质量一的两条真实来源。
它们分别来自固定曲线 $E_{-136}$、$E_{668168}$，且
$$
\begin{array}{c|c|c|c|c}
 &D&N_7&N_{19}&F_Y\text{ 的系数}\\ \hline
H_1^{\rm ref}&+1&1&\omega&\delta/(3024b)\\
H_4^{\rm ref}&-1&1&-\omega&-\delta/(3024b).
\end{array}
\tag{35}
$$
两条固定曲线的秩零身份已付；本篇没有将其中央导数赋零。
这也不是把 $D=-1$ 那条误指为 $E_{-136}$。

### 7.3 四个完整外三维块

对 $\epsilon=\pm1$、$\tau=\omega,\omega^2$，在 $M^9=1$ 块上取
$$
F_{\epsilon,\tau}
=\frac{I+\epsilon D}{2}
 \frac{I+\tau^{-1}M^3+\tau^{-2}M^6}{3}
 \frac{I+M^9}{2}F_Y .
\tag{36}
$$
四块全非零，每块循环维数三、最小多项式 $t^3-\tau$。
全部原质量为
$$
\begin{array}{c|cc}
 &\tau=\omega&\tau=\omega^2\\ \hline
D=+1&-\delta/(3024b)&0\\
D=-1&+\delta/(3024b)&0.
\end{array}
\tag{37}
$$
零质量的两个外块仍是非零的整个来源。

完整共同分解于是为
$$
\boxed{
F_Y=\frac12S(2z)
+\frac{\delta}{3024b}(H_1^{\rm ref}-H_4^{\rm ref})
+\sum_{\epsilon=\pm1,\ \tau=\omega,\omega^2}F_{\epsilon,\tau}.
}
\tag{38}
$$
$M$ 循环维数为八，$D=+1$ 和 $D=-1$ 的共同循环维数分别为八、
七，合起来恰为十五。
证书保存全部二十三坐标、所有六个特征投影和四个外块；
所有显示身份和秩由特征零 CM 消元得到，没有使用素数采样。

在 $b=1$ 时上述新向量的有理系数分母最小公倍数为
$$
3024=2^4\,3^3\,7.
$$
一般 $b$ 用
$$
F_{Y,b}(z)=b^{-1}F_{Y,1}(b^{1/6}z)
$$
还原：第 $j$ 列乘 $b^{21-j}$，参考和外块的质量乘 $b^{-1}$。
所以 (35)–(38) 的尺度完整，当前处也无需新增坏集。

### 7.4 普通核、周期尺度与可用的原算术行

由 $K_{136}=-M^9$ 和 (33)，整条边际满足
$$
\boxed{K_{136}F_Y=S(2z)-F_Y.}
\tag{39}
$$
还原物理 $Y$ 后为
$$
\boxed{\nu_{P_Y}|_p=\lambda[\kappa]_*(\nu_S-\nu_{P_Y}).}
\tag{40}
$$
这是 (18) 在整个边际上的核对；
(18) 的联合证明独立保了所有伴随，并未从 (40) 逆推它。

固定 $[2]$ 的 Mellin 尺度满足
$$
J_{F(z/2)}(u)=\langle2\rangle^{-d_pu}J_F(u),\qquad
J'_{F(z/2)}(0)=J'_F(0)-d_p\log_p\langle2\rangle J_F(0).
\tag{41}
$$
(38) 的参考及两个非零质量外块要逐项保 (41)。
只有完整和的质量抵消后，才可消去共同尺度项。

还有一个合法的原算术条件行。
在完整 $Y$ first-axis 上先取 principal 角，再取
$M=-1$ 的整个投影；R466 已付该线在整个二十三维空间中恰一维。
(33) 因而提升为完整四伴随的 tensor 身份
$$
\boxed{\Pi_S^{(Y)}\nu_1=\nu_S\otimes\Lambda_S,\qquad
                 \Lambda_S(0)=1/2}
\tag{42}
$$
（这里已按 (41) 返回原物理 $Y$）。
伴随整性可由固定 $S(2z)$ 的第六系数 $64$ 提取，
其分母 $6!$ 在当前处为单位。
所以对任意完整四伴随测试 $\varphi$，
$$
\int 1_{Y\ {\rm unit}}d_p\log\langle Y\rangle
       \varphi\,d(\Pi_S^{(Y)}\nu_1)
=J'_S\,\Lambda_S(\varphi).
\tag{43}
$$
这确实使用原已合格的算术来源。
但是 $\Pi_S^{(Y)}$ 不能自动与 (4) 的原混合切集交换；
使用 (43) 处理 $\eta_{i,n}$ 或实际矩形像时，仍须保每个 CM 分支的
真实转置。对未经该投影的 $Q$ 旋转中央，(35)–(38) 的未知参考
和外块全部存在，不能由 $J'_S=0$ 给它们整条赋零。

## 8. 与原总行的范围及精确文件

本篇实际支付了：

- 同一个 R599 补偿来源的两个真实 $Q$ 张量支，及与原矩形的准确交换；
- 全五坐标的一层 $Y$、四层 $W$ 核，全部中心相位和绝对 scalar；
- (23) 的非齐次来源关系及 (24)–(28) 的两个真实外矩形像；
- 原实际 $Y$ 来源的完整十五维 CM 分解和 (42) 的合法原 $S$ 条件行。

R599 式 (28) 中的 $\mathcal T$、两个真实补偿和原 $I_1$ 仍完整保留。
三域的互不相交、一个投影的单位伴随或两个参考的非零质量
均未证明余补集消失，也未完成原无穷 $p$ 中央非零。

- [check-r601-q-tensor-split-and-complete-y-w-cores.js](../scripts/check-r601-q-tensor-split-and-complete-y-w-cores.js)
- [check-r601-q-tensor-split-and-complete-y-w-cores.json](../scripts/check-r601-q-tensor-split-and-complete-y-w-cores.json)

脚本复用已发表的完整 degree136 CM7/CM19 矩阵，
以 BigInt 有理 CM 算术重建整个 (30)、全部投影和秩，
并精确核定完整 half-period 相位、两个 Schrödinger 交织、
全部物理行和三域单位系数。数据不重复保存原大矩阵。
所有新等式已经在当前 JavaScript 环境精确通过；
无独立复跑或额外审批门槛。
