# R119 续篇：紧支形状的真实两相位补偿、统一复域与 Wronskian 二阶界

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇给共同径向参数选择所需的完整局部合同：
在每个实际下降坡的未占用区间内，任意 $C^4$ 紧支形状的复球
$\|\Xi\|_{C_x^4}<2^{-64}$ 都有唯一真实两 bump 补偿，准确保持
同一个完整 principal 相位和首相位。补偿在全部层上有统一全纯
定义域、一次和二次导数界。

对真实两相位线性 annihilator 子空间，补偿从二阶开始，且
$$
 \|\gamma(\Xi)-\gamma^0\|\le\|\Xi\|^2,\qquad
 \|D\gamma(\Xi)\|\le\|\Xi\|,\qquad
 \|D^2\gamma(\Xi)\|<2. \tag{H.1}
$$
这些界可以直接用于任意有限组或可求和的实际 compact 方向。
固定两侧真实 unit Robin 线时，完整 normalized Wronskian 的
Hessian 满足
$$
 \boxed{\quad
 \|D^2_\Xi\mathcal W_m\|
 <2^{22}K_j^3\big(M+B/M\big)^2,\qquad
 K_j=2^{6000}(j+5)^8\delta_j^{-16},\quad M=|m|\ge4 .
 \quad} \tag{H.2}
$$
这是原真实两解 transfer 的二阶界；没有用高频近似，
也没有把复高频 Cauchy 流假定为有统一小范数。
普通源、weak 源和 mean 的变化式在末节完整保留。
本篇仍不声称已选择所有中频共同参数或已闭合完整非径向外方程。

## 1. 同一实际族与相位单位

使用
[新控制族全图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
的两参数 profile、真实平移和 compact 形状。只在 $j\ge8193$
操作；所有 prefix 和两个接缝保持同一对象。记
$$
 a=\eta_j/\sqrt{12},\quad B=\Delta/a,\quad
 d=1/\Delta<1/80,\quad e=1/B<2^{-190},\quad
 J=(7/16,15/32).
 \tag{H.3}
$$
$\gamma_1,\gamma_2$ 仍是原两 disjoint bump 的坐标。
它们的复盒准确为 $2^{-15},2^{-29}$，实盒为各自的一半。
固定一个实际实基点
$$
 |\gamma_1^0|<2^{-18},\qquad|\gamma_2^0|<2^{-32}.
 \tag{H.4}
$$
第50束已选定的算术基点严格满足此式。
$\Xi\in C^4_0(J;\mathbb C)$；这里使用各阶 supremum 的最大值，
而使用四阶和范数至多1的控制当然也合法。

必须区分光学长度 $S$ 与两射线主相位：
$$
 \Theta=-2S=-2\int_I\sqrt Q\,dt,\qquad
 \beta=-\mathfrak b/2 .
 \tag{H.5}
$$
$\beta$ 是已识别的真实完整返回首系数，含原根有限部。
本篇所有变分远离根，故相同 root/endpoint 项在差分中准确相消。
没有把一个严格内部积分的固定偏移常数置零。

下降坡整体平移保持 $S$ 和 $\beta$ 准确不变；
所有以下补偿可在任意已许用的平移上进行。
固定全局同一方向的两个参数归一输出为
$$
 \mathsf F(\gamma)=
   \left(\sqrt B\,\Theta(\gamma,0),\,
                    \beta(\gamma,0)/\sqrt B\right).
 \tag{H.6}
$$
在 $J$ 上原两个 bump 为0，令
$$
 u_0=S'(x)+7e,\qquad u=u_0-d\,\Xi'(x).
$$
完整 phase 的形状改变量准确是
$$
 \mathsf C_1(\Xi)
       =-2\Delta\int_J(\sqrt u-\sqrt{u_0})\,dx,
$$
$$
 \mathsf C_2(\Xi)=
 \int_J\left\{\frac{\Delta}{16}
 [F_e(u)-F_e(u_0)]
 +\frac1{64\Delta}
 [u_x^2u^{-5/2}-(u_0)_x^2u_0^{-5/2}]\right\}dx,
$$
$$
 F_e(u)=u^{3/2}+2e\,u^{1/2}+e^2u^{-1/2}.
 \tag{H.7}
$$
此式由第52束的完整 compact 变分泛函积分得到；原材料测度
$dt=a\,dx$ 已包含在 $\Delta=aB$ 中。

支集分离给**准确的加法分解**
$$
 \left(\sqrt B\,\Theta(\gamma,\Xi),\,
                 \beta(\gamma,\Xi)/\sqrt B\right)
       =\mathsf F(\gamma)+\mathsf C(\Xi).
 \tag{H.8}
$$
因此没有被隐藏的 $\gamma$–$\Xi$ phase 混合导数。
这不是全 PDE 解图的解耦：后者仍保留所有参数的交叉依赖。

## 2. 形状 phase map 的完整复球

在 $\|\Xi\|_{C^4}<2^{-20}$ 上，
$\operatorname{Re}u>3/2,\ |u|<2,\ |u_x|<7$。
所有幂使用与正实值相接的唯一平方根分支。
由 $|J|=1/32$ 及 $d<1/80$，直接微分 (H.7) 给
$$
 \|D\mathsf C(\Xi)\|_{C^4\to\ell^\infty_2}<1/16,\qquad
 \|D^2\mathsf C(\Xi)\|_{C^4\times C^4\to\ell^\infty_2}
                                          <2^{-10}.
 \tag{H.9}
$$
下面列出完整分量账，避免从形式 phase map 预支常数。
第一行一次导数是 $\int\psi' u^{-1/2}dx$，小于 $1/32$；
二次导数小于 $d|J|/2<1/5120$。

第二行的一次导数由
$$
 \frac1{16}|F_e'(u)|\,|\psi'|,\quad
 \frac{d^2}{64}
 [2|u_x||\psi''|+\tfrac52|u_x|^2|\psi'|]
$$
控制，$|F_e'|<3$。其积分小于
$3/512+(273/2)/(64\cdot80^2\cdot32)<1/16$。
二次导数的第一部分小于 $d|J|/16$，因为 $|F_e''|<1$；
第二部分不超过
$$
 \frac{d^3|J|}{64}
 \left[2+10\cdot7+\frac{35}{4}7^2\right].
$$
二者和小于 $2^{-10}$。
这些是完整复方向估计，不用 real positivity 代替复模分母。

## 3. 两原参数的真逆与二阶费

[真实两参数横截](R119-supplement-actual-phase-preserving-subprincipal-metric-parameter.md)
的完整区间积分给
$$
 .085<T_1<.087,\quad .058<T_2<.061,\qquad
 -.023<B_1<-.021,\quad -.010<B_2<-.008,
$$
$$
 \det\begin{pmatrix}T_1&T_2\\B_1&B_2\end{pmatrix}>2^{-11}.
 \tag{H.10}
$$
其中 $T_s=\sqrt B\,\Theta_{\gamma_s}$、
$B_s=\mathfrak b_{\gamma_s}/\sqrt B$。
因此实际 $\mathsf A=D\mathsf F(\gamma^0)$ 为
$$
 \mathsf A=
 \begin{pmatrix}T_1&T_2\\-B_1/2&-B_2/2\end{pmatrix},
 \qquad |\det\mathsf A|>2^{-12},\qquad
 \|\mathsf A^{-1}\|_{\infty\to\infty}<2^9.
 \tag{H.11}
$$
最后一式保留真实行列式；两个 inverse 行分子的和分别
小于 $.066$、$.0985$，均小于 $1/8$。

所需复 Hessian 也单独支付。原两个 bump 满足
$|\psi_1'''|\le3\cdot2^{16}$、
$|\psi_2'''|\le3\cdot2^{22}$。这来自
$\psi_s'''=384\ell_s^{-3}(1-12z+30z^2-20z^3)$ 及
$|1-12z+30z^2-20z^3|\le1$ 于 $[0,1]$。
于是整个原复参数盒在两个支集上都有
$$
 |u|>1/2,\qquad |u_x|<7,\qquad |u_{xx}|<64.
$$
原无量纲 Jacobian 公式 (P.12)--(P.13) 给
$\|D\mathsf F\|_{\infty\to\infty}<4$：
第一行之和小于 $105/64$；每个 $|B_s|<1$，
后者由
$$
 \frac78\left(\frac3{16}+\frac{3e}{16}
                       +\frac{9e^2}{16}\right)
 +\frac{12}{80^2}\left(24+\frac{735}{16}\right)<1
$$
直接包住。各支集都使用自己的真实长度，以上只是放宽。

在 $|\gamma_1|\le2^{-16},|\gamma_2|\le2^{-30}$，
沿任意单位 $\ell^\infty$ 复方向可用半径 $2^{-31}$ 的盘。
Banach Cauchy 公式因而给完整双线性 Hessian
$$
 \|D^2\mathsf F\|<2^{34}. \tag{H.12}
$$
不只对两个坐标分别微分后遗漏交叉范数。

## 4. 统一全纯补偿与 annihilator 上的二阶起步

令
$$
 r_\gamma=2^{-48},\qquad r_\Xi=2^{-64}.
$$
在 $\|\eta\|\le r_\gamma$ 中求
$$
 \eta=-\mathsf A^{-1}
 \{\mathsf C(\Xi)+\mathsf F(\gamma^0+\eta)
                   -\mathsf F(\gamma^0)-\mathsf A\eta\}.
 \tag{H.13}
$$
其导数 norm 小于
$2^{9+34-48}=2^{-5}$，且 forcing 小于 $2^{-59}$。
Taylor 二次 self-map 费用至多 $2^{-54}$；
两者和小于 $r_\gamma$。因此对整个
$\|\Xi\|<r_\Xi$ 的复球，(H.13) 有唯一全纯解。
真实数据的共轭唯一性给实补偿，且
$$
 \|\eta(\Xi)\|\le2^6\|\Xi\|,\quad
 \|D\eta\|\le2^6,\quad \|D^2\eta\|<2^{58}. \tag{H.14}
$$
这里当前 $D\mathsf F$ 的逆小于 $2^{10}$；二阶公式为
$$
 D^2\eta=-(D\mathsf F)^{-1}
 \{D^2\mathsf C+
             D^2\mathsf F[D\eta,D\eta]\}.
 \tag{H.15}
$$
新增参数始终留在第53束真实两个复盒内。

定义闭线性子空间
$$
 \mathcal Z=\{\Xi\in C^4_0(J):
                     D\mathsf C(0)\Xi=0\}.
 \tag{H.16}
$$
第52束的 phase-annihilating 方向以及
[已量化 compact 方向](R119-supplement-quantitative-phase-preserving-compact-control.md)
都属于 $\mathcal Z$；消 $S$ 也准确消 $\Theta=-2S$。

在 $\mathcal Z$ 上，(H.9) 给
$\|\mathsf C(\Xi)\|\le2^{-11}\|\Xi\|^2$。
当前逆小于 $2^{10}$，所以 $\|\eta\|\le\|\Xi\|^2$。
沿任意 $\psi\in\mathcal Z$，
$\|D\mathsf C(\Xi)\psi\|\le2^{-10}\|\Xi\|\|\psi\|$，
故 $\|D\eta\|\le\|\Xi\|$。
再由 (H.15)，
$$
 \|D^2\eta\|<
 2^{10}\big(2^{-10}+2^{34}2^{-128}\big)
       =1+2^{-84}<2 .
$$
这证明 (H.1)。它是同一小球上的完整双线性界，不仅是
原点某一个方向的二阶 jet。

若 $\Xi_0$ 支持于以前已用的区间，而新 $\psi\in\mathcal Z$
支持于与其不交的区间，则 (H.7) 的局部加法性进一步给
$$
 D\mathsf C(\Xi_0)\psi=D\mathsf C(0)\psi=0,\qquad
 D\eta(\Xi_0)\psi=0. \tag{H.17}
$$
所以以后在一个尚未改变的 quartic germ 上生成的新控制，
在当前完整 profile 处仍无一阶补偿项。不是错误地把原点
零导数沿整个参数路径免费延用。

不同负分量的径向 phase map 分离，全部常数统一。
因此 (H.13) 同时给完整
$\ell^\infty_i(C^4_0(J))$ 球上的联合全纯补偿。
任意有限组 $\Xi_i=\sum_k\varepsilon_{i,k}\psi_{i,k}$、
$\|\psi_{i,k}\|_{C^4}\le1$ 且
$\sup_i\sum_k|\varepsilon_{i,k}|<2^{-64}$ 都合法；
同一条件下的无限和也在真实 $C^4$ 空间收敛并保持两 phase。
本句不声称已为全部频率选到非共振参数。

## 5. 当前真实两解的 Wronskian Hessian

本节取实 $\Xi\in\mathcal Z$、$\|\Xi\|<2^{-64}$。
固定第52束的两个真实 $Q=7$ 窗口端点，全部控制支集在其内。
所有控制和两个补偿 bump 的端 jets 为0，所以两端 $\mu,Q$
及 physical height/flux 到固定 wave 的变换准确不动。
取
$$
 k=\sqrt{7M^2-16},\quad
 Y=(\sqrt k\,u,u_t/\sqrt k),\quad u=\sqrt\mu\,h .
$$
其真实径向方程是
$$
 Y_t=\mathsf A_mY,\qquad
 \mathsf A_m=
 \begin{pmatrix}
 0&k\\
 -[M^2Q+Q_t/2-(1+Q)^2/4]/k&0
 \end{pmatrix}. \tag{H.18}
$$
第53束已经为本新对象重新支付实际完整两根 Cauchy；
两侧固定 wave 转换后可用本篇 (H.2) 的 $K_j$
控制全部实内部子区间的正反向流。
不把这个实能量界未经证明转成复高频演化界。

记一阶物理形状为
$\theta_\psi=\psi+\sum_sD\eta_s[\psi]\psi_s$，
二阶为 $\theta_{\psi,\varphi}=\sum_sD^2\eta_s[\psi,\varphi]\psi_s$。
用 (H.1) 及两原 bump 的完整 $C_x^2$ 界，
对 $\|\psi\|,\|\varphi\|\le1$ 有
$$
 \|\theta_\psi\|_{C_x^2}<2,\qquad
 \|\theta_{\psi,\varphi}\|_{C_x^2}<2^{19}. \tag{H.19}
$$
真实导数为
$$
 DQ[\psi]=-(\theta_\psi)_t,\qquad
 D^2Q[\psi,\varphi]=-(\theta_{\psi,\varphi})_t .
$$
只有输入形状的已付二阶径向导数出现，没有未知解的高径向 jet。

令 $R=M+B/M$。因 $k\ge2M$、$Q<2B$、$B=\Delta/a$、
$\Delta>80$，从 (H.18) 的实际下左行直接得到
$$
 \int\|D\mathsf A_m[\psi]\|dt<2R,\qquad
 \int\|D^2\mathsf A_m[\psi,\varphi]\|dt<2^{20}R.
 \tag{H.20}
$$
第一式使用
$\int|\theta_t|\le2$、$\int|\theta_{tt}|\le2/a$。
第二式含完整补偿二阶项；直接二次项为
$\theta_{\psi,t}\theta_{\varphi,t}/(2k)$，积分小于 $1/(Ma)$，
而二阶形状的线性项至多 $2^{19}R$。所有 $dt=a\,dx$ 因子
都已保留。

对真 transfer $\mathcal C_m=\mathcal U(b,a)$，
一次 Duhamel 与完整两次有序 Duhamel 因而给
$$
 \|D\mathcal C_m\|<2K_j^2R,
$$
$$
 \|D^2\mathcal C_m\|
 \le K_j^2\,2^{20}R+
                  2K_j^3(2R)^2
 <2^{22}K_j^3R^2 . \tag{H.21}
$$
这里在两个次序各有完整 middle propagator，未删掉其中一列。

令 $l,r$ 为固定实 unit 左右线，normalized Wronskian 为
$\mathcal W_m=[r,\mathcal C_m l]$。由于两条真实外侧数据对本
窗口控制固定，(H.21) 立即给 (H.2)。
局部负 pocket 加两侧正型 DN 对角 Robin 满足这项固定性；
正型 off-diagonal 仍是完整相邻源输入。
若消费者使用随第四停止而改变的全局右线，则必须另加
$r',r''$ 两列，不能原样套用 (H.2)。

特别，在当前真实共振处得到一个 $\|\psi\|_{C^4}\le1$ 的新
annihilator 方向且 $|\mathcal W_m'|\ge L_{j,m}>0$ 后，
对
$$
 |\varepsilon|\le
 \min\{r_{\rm free},\ L_{j,m}/(4H_{j,m})\},\qquad
 H_{j,m}=2^{22}K_j^3R^2
$$
真实一阶导数在该段变化小于 $L_{j,m}/4$。
这是把已付一阶横截升级为有限参数单调段的合法入口；
共同所有频率的 bad-set 与后续控制保隙仍须实际选择。

## 6. 全标签消费者、metric 源和 mean

将上述补偿复合进第53束真全标签图。
在 $\mathcal Z$ 上，归一参数一阶 norm 由 $\Xi$ 的
$2^{21}$ 权占主导，二阶补偿参数 norm 至多 $2^{31}$；一般双线性方向另外保留第53束的极化费用。
因此完整 endpoint/强标签解给
$$
 \|D_\Xi X\|_{\mathcal X_\beta}\le2^{25}\|a_{\rm lab}\|_\beta,
 \qquad
 \|D_\Xi^2X\|_{\mathcal X_\beta}<2^{50}\|a_{\rm lab}\|_\beta .
 \tag{H.22}
$$
这里 $a_{\rm lab}$ 是内部标签，不能与坡长 $a$ 混用。
所有 Fourier、mean 小根和端口反馈都包括在实际复合中。
固定物理 $C^2$ 空间仍只使用第53束已证连续性；
不从 endpoint 全纯性断言平移接缝的 $C^2$ 全纯性。

固定局部高度尺度时，令 $\theta_1,\theta_2,\theta_{12}$
分别为完整 $\delta\log p_*$ 和其混合二阶变分。
径向散度密度
$G=\mu\operatorname{diag}(1,-Q)$ 的准确二阶变化是
$$
 G_{12}=\mu\operatorname{diag}
 \left(\theta_1\theta_2+\theta_{12},\
 -Q(\theta_1\theta_2+\theta_{12})
 +\theta_1(\theta_2)_t+\theta_2(\theta_1)_t
 +(\theta_{12})_t\right). \tag{H.23}
$$
故有源二阶解须保
$$
 P h_{12}=-\operatorname{div}
 (G_{12}\nabla h+G_1\nabla h_2+G_2\nabla h_1)
$$
以及给定 ordinary/weak 源本身的实际参数导数。
它们按第53束完整总通量两态进入，没有 $F^t_t$ 范数。
本篇没有因补偿一阶为0而把这些二阶源列删除。

例如在 canonical 总通量状态中，固定材料 $f,F$ 时，
第53束 weak 第一源行正比于 $p_*^{-1}F^t$，
因此其一阶为 $-\theta$ 倍原行，二阶为
$(\theta_1\theta_2-\theta_{12})$ 倍原行。
若指定的是 $e$ 而 ordinary $f=w^2e$ 随度量变化，
还须保留 $f_1=2\theta_1f$、
$f_{12}=(4\theta_1\theta_2+2\theta_{12})f$。
完整 affine propagated source 的一、二阶 Duhamel 含
$\mathcal U_1\mathcal J$、$\mathcal U\mathcal J_1$，
以及 $\mathcal U_{12}\mathcal J$、
$\mathcal U_1\mathcal J_2$、$\mathcal U_2\mathcal J_1$、
$\mathcal U\mathcal J_{12}$，顺序不能交换。
本篇的 homogeneous Wronskian Hessian 没有免费授予这些列
在任意未给定 source norm 中的小界。

真实 mean 电阻的一、二阶分别是
$$
 -\int\theta\,\mu^{-1}dt,\qquad
 \int(\theta_1\theta_2-\theta_{12})\mu^{-1}dt. \tag{H.24}
$$
真实 mean flux、唯一高度 $\lambda$ 和全部高度积分继续保留；
两 phase 固定并不使 (H.24) 为0。
外尺度或移动 cut 变化时还要使用第53束一般 $\delta G$
以及完整 $Z_e+w_e\delta a_e$ 端项。

## 7. 严格运算及准确范围

新的纯 JS/BigInt 程序
[scripts/fourfold_radial_phase_compensation_Wronskian_Hessian_20261114.js](../scripts/fourfold_radial_phase_compensation_Wronskian_Hessian_20261114.js)
和[完整有理预算](../notes/2026-11-14-R119-radial-phase-compensation-Wronskian-Hessian-budget.json)
记录本篇实际显示门。它是本次真正执行的新实现，不是原 native 回放。
公式 (H.7)、(H.18) 和全部变分在正文从实际方程推导。

已得真实统一复补偿域、完整参数二阶费、可复合全标签图、
同一 fixed-port Wronskian 的实际 Hessian，以及所有源/mean
必须保留的变化式。实际中频共同参数选择及非径向全
$\mathcal F_c$ 仍是继续任务。
