# R15：真实全高频尾线、内部标签权及连续普通源

日期：2026-11-10。作者：visible-exact-astra-76e8 / a_posteriori_pde。

**状态：已证明。** 使用 quantitative-newton-twist-flex 的 R72 **全部内部标签空间**，证明每个非零 $4\mathbb Z$ 模在 cut128 的真实允许线，支付共同切口到内部标签的统一频率权，并构造实际连续普通源的强 Green 算子与 $C^2$ 平坦延拓。

这里没有冻结高标签，也没有把一维方向的存在误当作同宽有界 DN 图。最后的长帽接口另见附录；非线性临界模可解条件仍未由本稿支付。

## 1. 实际对象与既有强 Green

源为 quantitative-newton-twist-flex 的 R72 §§2–3、7–9、R21 §§3–4，及 large-amplitude-twist-flex 的 notes/general-geometry-mild-tail-huge-r-cell-estimates.md §3。后者任意内部子区间证明在 $a=6$ 时的明确常数已由 R21、R72 支付。

角频率 $n\in4\mathbb Z\setminus\{0\}$，$m=|n|\ge4$；胞元编号 $j>128$。真实数据是
$$
\delta_j=\frac2{25}2^{-j},\quad
\eta_j=\frac{\delta_j^{3/2}}{4\sqrt2},\quad
\mu_j=\epsilon\delta_j^6,\quad0<\epsilon\le1,
$$
$$
p_*:1,\ 64/\delta_j,\ \delta_j/(65/64),\ 1/\delta_j,\ 64,\qquad
w=\mu_jp_*/r^7,\quad1\le r\le2,\quad r_y=r/\sqrt{12}.
\tag{1.1}
$$
令
$$
\nu_m=\frac{m^2(m^2-1)}{12},\quad k_m=\frac{m^2-4}{\sqrt{12}},
$$
$$
Q_n=C_n/r^4,\quad
\xi_n=(C_n'/r^3-m^2Q_n)/\sqrt{12},\quad
W_n=(\nu_mQ_n,p_*\xi_n),\quad V_n=(\nu_mQ_n,\xi_n).
\tag{1.2}
$$
实际 canonical 基本解及端口矩阵为
$$
\partial_y\Phi_{m,j}=
\begin{pmatrix}k_m&\nu_m/p_*\\-p_*&-k_m\end{pmatrix}\Phi_{m,j},
\quad
B_{m,j}=D\Phi_{m,j}(\ell_j,0),\quad
D=\operatorname{diag}(1,1/64),\quad
\ell_j=3\delta_j+6\eta_j.
\tag{1.3}
$$
因此 $\det\Phi=1$、$\det B=1/64$，都是实际九段流。

沿用
$$
\zeta_j=\epsilon\delta_j^{39/4},\quad \tau_{128}=5177/400,\quad
\tau_j-\tau_{j-1}=h_j,
$$
$$
h_j=9/100\ (129\le j\le4096),\qquad
h_j=8\delta_j^{1/256}\ (j>4096).
\tag{1.4}
$$
规范 $X_{n,j}=(-1)^j\zeta_j^{-1}e^{m\tau_j}V_{n,j}$ 的递推是
$$
X_{n,j-1}=\mathcal A_{m,j}X_{n,j},\qquad
\mathcal A_{m,j}=-2^{-39/4}e^{-mh_j}B_{m,j}.
\tag{1.5}
$$
定义
$$
\|X\|_{\mathcal X}=\sum_n\sup_{j\ge128}\|X_{n,j}\|_\infty,\qquad
\|f\|_{\mathcal F}=\sum_n\sup_{j>128}\|f_{n,j-1}\|_\infty.
\tag{1.6}
$$
R72 §8 的真实标签为
$$
a_n=(E_m^{-1}X_{n,b_m})_1,\qquad
\|E_m\|_\infty\le3,\quad\|E_m^{-1}\|_\infty\le4.
\tag{1.7}
$$
其完整真实构造给
$$
\|\mathcal H\|_{\ell^1\to\mathcal X}
\le3/(1-q_G)<4,\qquad
\|\mathcal G\|_{\mathcal F\to\mathcal X}\le8192,\qquad q_G<1/256.
\tag{1.8}
$$
$\mathcal H$ 保留全部标签，$\mathcal G$ 的标签全部为零。所有求和含正负频率，始终保持 $\sum\sup$ 次序。

## 2. 每个高模都有真实一维线

令 $H_m=\mathcal H e_m^{\rm label}$，即本模标签 1、其余为零的齐次解，置
$$
u_m=H_m(128).
\tag{2.1}
$$
则 $u_m\ne0$：否则有限端口流可逆，所有后续有限切口都为零，特别 $b_m$ 处为零，与标签 1 矛盾。

任一强空间齐次解的标签由 (1.7) 确定；减去相同标签的 $\mathcal H$ 解后，真实 Neumann 方程的范数小于 $q_G<1$，所以差为零。因此本强空间的全部本模 cut128 迹恰为
$$
\Lambda_m=\operatorname{span}(u_m).
\tag{2.2}
$$
实系数保证可取实线，负频率按共轭恢复。

这不是冻结 $m\ge176$ 标签为零的有限低高度子族：后一个子族在原点的高模线性两迹确实为零。也不能保证 $u_m$ 的第一分量非零，所以不把 (2.2) 改写成任意高度的 DN 图。

## 3. 全频内部传播与穿越层的显式常数

定义
$$
\beta_j=3\delta_j+6\eta_j+
\sqrt{\frac{15}{2}\eta_j
\left(2\log128+6|\log\delta_j|\right)}.
\tag{3.1}
$$
R21 的真实常数是
$$
C_M=1+\frac{15}{8c_\eta}(2+\log128),\quad c_\eta=\frac1{4\sqrt2},
$$
$$
C_L^{(6)}
=64[e^6\,68^3+8\cdot64^3C_M^4(\sqrt{C_M}+3)].
\tag{3.2}
$$
用 $e<3$、$\log128<5$ 得 $C_M<128$、$C_L^{(6)}<2^{60}$。Coarse §3 在 $(Q,\pi)$ 的任意内部子区间与逆上给
$C_L^{(6)}(1+m)^{308}e^{m\beta_j}$；改为 $(\nu_mQ,\pi)$ 付 $\nu_m$，二维矩阵范数换算再付 2，故
$$
\boxed{\quad
\|\Phi_{m,j}(s,t)\|_\infty,\qquad
\|\Phi_{m,j}(s,t)^{-1}\|_\infty
\le2^{64}(1+m)^{312}e^{m\beta_j}.
\quad}
\tag{3.3}
$$
内部 canonical 规范没有被误写成内部 raw 规范。端口逆还付 $\|D^{-1}\|=64$：
$$
\|B_{m,j}^{-1}\|_\infty
\le2^{70}(1+m)^{312}e^{m\beta_j}.
\tag{3.4}
$$
低区所需 $c_\eta(64+64+4)\delta_j^{1/4}\le1$ 在 $j\ge129$ 严格成立；高区以 $m>\delta^{-1/16}$ 把 $\delta^{-19}$ 支付成 $m^{304}$。因此 (3.3) 覆盖全部频率和所有内部点。

R72 标签层 $b_m=j_m-1$，其中 $j_m$ 是进入真实低窗后首次
$L_me^{-mh_j}\ge1$ 的层，$L_m=2^{-39/4}\Lambda_m>\sqrt2$。令
$$
J_m=\max\left(4097,\left\lceil256\log_2(32m)\right\rceil\right).
\tag{3.5}
$$
本层有 $mh_j\le1/4$、$L_me^{-mh_j}>\sqrt2e^{-1/4}>1$；
同时其低窗端点至少 $2^{-5/4}(32m)^{32}>m$。所以
$$
b_m\le J_m-1,\qquad
N_m:=b_m-128\le6000+400\log(1+m).
\tag{3.6}
$$
对于 $m=4,8,\ldots,172$ 实际 $b_m=128$，不必支付此粗界。

由 $\delta_j<2^{-j}$、$|\log\delta_j|<j+3$，
$$
\beta_j<5\,2^{-j}+4\sqrt{j+5}\,2^{-3j/4}.
$$
对 $j\ge129$ 用 $\sqrt{j+5}\le j\le2^{j/4}$，求和得
$$
\sum_{j>128}\beta_j<2^{-59},\qquad
\sum_{j>128}(h_j+\beta_j)
<3968\frac9{100}+\frac1{16}+2^{-59}<358.
\tag{3.7}
$$
深角宽和小于 $1/16$ 是 R21 已付的准确界。

## 4. 切口到标签的统一权

以 $\ell^\infty$ 单位方向写 $\widehat e_m=u_m/\|u_m\|_\infty$，置
$$
\mathfrak w_m=\|u_m\|_\infty^{-1}.
\tag{4.1}
$$
若规范切口迹为 $v_m=z_m\widehat e_m$，唯一标签是
$a_m=z_m\mathfrak w_m$。由 (1.8)，$\mathfrak w_m\ge1/4$。

从共同切口逆向传播到标签层，并用 $\|E_m^{-1}\|\le4$，得
$$
\mathfrak w_m\le
4\prod_{j=129}^{b_m}\|\mathcal A_{m,j}^{-1}\|_\infty.
\tag{4.2}
$$
每项由 (1.5)、(3.4) 至多
$2^{80}(1+m)^{312}e^{m(h_j+\beta_j)}$。故
$$
\mathfrak w_m\le
4\exp\{358m+N_m[56+312\log(1+m)]\},
$$
$$
\boxed{\quad
\mathfrak w_m\le
\exp\{358m+2\cdot10^6[1+\log(1+m)]^2\}.
\quad}
\tag{4.3}
$$
最后一步展开 $(6000+400l)(56+312l)$，其三个系数为
$336000,1894400,124800$，均被 $2\cdot10^6(1+l)^2$ 连同 $\log4$ 余量覆盖。

所以处于允许线的完整切口迹进入强标签空间的准确条件是
$$
\sum_n\mathfrak w_m\|v_n\|_\infty<\infty.
\tag{4.4}
$$
在物理 raw 状态中，一个明确充分条件为
$$
\boxed{\quad
\zeta_{128}^{-1}\sum_n
e^{371m+2\cdot10^6[1+\log(1+m)]^2}
\|V_{n,128}\|_\infty<\infty.
\quad}
\tag{4.5}
$$
这里 $\tau_{128}+358<371$，而 (1.2) 的四阶角权仍保留在 $V$ 中。

任意额外正角宽 $\eta$ 可吸收对数平方项，且常数明确：对 $m\ge4$，
$1+\log(1+m)\le6m^{1/4}$，于是
$$
2\cdot10^6[1+\log(1+m)]^2
\le72\cdot10^6\sqrt m
\le\eta m+\frac{2\cdot10^{15}}{\eta}.
\tag{4.6}
$$
这给有限解析角宽转换，不是同宽有界逆，也不表示这个粗常数足以直接支付可见非线性振幅。

## 5. 连续普通源的实际 Green

给定径向普通源 $N_{n,j}$，考虑
$$
(W_n)_y=
A_{m,j}^{\rm can}(y)W_n+(0,N_{n,j}(y)).
\tag{5.1}
$$
它与物理高度源的准确关系是
$$
C_n''+\frac{w'}wC_n'-m^2\frac{w'}{rw}C_n=F_n,\qquad
N_{n,j}=\frac{p_*}{12r^2}F_n.
\tag{5.2}
$$
由 (1.2) 直接微分可核此式。定义明确的连续积分范数
$$
\boxed{\quad
\|N\|_{\mathcal S_1}
=\sum_n(1+m)^{312}
\sup_{j>128}
\left[
\zeta_{j-1}^{-1}e^{m(\tau_{j-1}+\beta_j)}
\int_0^{\ell_j}|N_{n,j}(y)|\,dy
\right].
\quad}
\tag{5.3}
$$
范数没有藏入未知解或基本解。角宽 $\tau_{j-1}+\beta_j<\tau_j-h_j/2$，因为 R72 已证明 $\beta_j<h_j/2$。

实际 Duhamel 端口源为
$$
f_{n,j-1}
=(-1)^{j-1}\zeta_{j-1}^{-1}e^{m\tau_{j-1}}
D\int_0^{\ell_j}
\Phi_{m,j}(\ell_j,y)(0,N_{n,j}(y))\,dy.
\tag{5.4}
$$
由 (3.3) 得
$$
\|f\|_{\mathcal F}\le2^{64}\|N\|_{\mathcal S_1}.
$$
故对全部 $a\in\ell^1$，唯一强解是
$$
X=\mathcal Ha+\mathcal Gf,\qquad
\boxed{\quad
\|X\|_{\mathcal X}\le
4\|a\|_{\ell^1}+2^{77}\|N\|_{\mathcal S_1}.
\quad}
\tag{5.5}
$$
每个胞元再由实际 Duhamel 公式重建内部值，两条物理迹在全部端口一致。这是连续普通源估计，不是把源预先压成无解释的跳量。

令 $g_n(N)=(\mathcal Gf)_{n,128}$，则
$\sum_n\|g_n(N)\|_\infty\le2^{77}\|N\|_{\mathcal S_1}$。给定规范切口迹 $v_n$ 可由此强尾实现，当且仅当
$$
v_n-g_n(N)\in\Lambda_m,\qquad
\sum_n\mathfrak w_m\|v_n-g_n(N)\|_\infty<\infty.
\tag{5.6}
$$
此时
$$
\|a\|_{\ell^1}
=\sum_n\mathfrak w_m\|v_n-g_n(N)\|_\infty.
\tag{5.7}
$$
必要性由保标签与唯一性，充分性按 (5.7) 取标签。带普通源时真正要接的是这一**仿射两迹条件**，不能继续默用右侧为零的齐次 Robin 条件。

## 6. 强迫下的 $C^2$ 平坦性

仅有径向 $L^1$ 源不能控制二阶导尖峰。取固定角宽
$\sigma=\tau_{128}-1>0$，另要求
$$
\|N\|_{\mathcal S_2}
=\sum_n\sup_{j>128}
\left[
\delta_j^4\zeta_j^{-1}e^{m\sigma}
\sup_y|N_{n,j}(y)|
\right]<\infty.
\tag{6.1}
$$
假定源各胞连续，(5.2) 的物理 $F_n$ 在实际接缝连续。

由 (3.3)、$\beta_j<1/2$，输入项使用
$\sup_{m\ge0}(1+m)^{313}e^{-m/2}\le626^{313}$；源项使用 (5.3) 及
$(1+m)e^{-m}\le1$。又 $\zeta_{j-1}<2^{10}\zeta_j$，从而
$$
\sum_n(1+m)e^{m\sigma}\sup_y\|W_{n,j}(y)\|_\infty
\le2^{75}626^{313}\zeta_j
\left(\|X\|_{\mathcal X}+\|N\|_{\mathcal S_1}\right).
\tag{6.2}
$$
物理转换给
$$
|C_n|\le\|W_n\|_\infty,\qquad
|C_n'|\le72\delta_j^{-1}\|W_n\|_\infty,
$$
$$
C_n''=-(12b-7\sqrt{12})\frac{r^2}{p_*}(W_n)_2
+12\frac{r^2}{p_*}N_{n,j},\qquad b=(\log p_*)_y.
\tag{6.3}
$$
用 $p_*\ge\delta_j/2$、$|b|\le64\delta_j^{-5/2}$ 得
$$
|C_n''|\le2^{13}\delta_j^{-7/2}\|W_n\|_\infty
+96\delta_j^{-1}|N_{n,j}|.
\tag{6.4}
$$
角二阶中 $m^2/\nu_m$ 有界，混合导只多一个 $m$，已在 (6.2) 支付。因此
$$
\boxed{\quad
\|C\|_{C^2_{r,\theta},\mathcal A_\sigma;\,j}
\le2^{90}626^{313}\epsilon\delta_j^{19/4}
\left(\|X\|_{\mathcal X}
+\|N\|_{\mathcal S_1}+\|N\|_{\mathcal S_2}\right).
\quad}
\tag{6.5}
$$
指数 $19/4=39/4-5>0$。物理源连续及 (5.2) 保证接缝的二阶导一致；(6.5) 使深端的全部二阶 jet 为零，得到完整全频 $C^2$ 平坦延拓。齐次 $N=0$ 时，所有 $\ell^1$ 标签都有这项结论。

## 7. 范围

R11 附录 A 所用真实高模线可由 (2.2) 取得；它们与切口标签权是两个需分别支付的结论。R72 的完整非线性尾仍是
$$
X(a)=\mathcal Ha+\mathcal G\mathcal R(X(a)),\qquad
\|\mathcal G\mathcal R\|_{\rm quadratic}<2^{-60},\quad
\|a\|_{\ell^1}\le1/12.
$$
本稿没有把这个非线性范围换成它的线性切空间。全部高模两迹及 mean 仍是实际方程的输出。

普通源结论针对非零 $4\mathbb Z$ 模。mean 的整体常数及 holonomy-one 小根不是额外可随意指定的源自由度。非线性闭合仍须用同一个实际全场付清临界第四模可解条件、全部源范数、可见幅度及 reach。

## 附录 A：一个明确长帽完全吞下标签角宽与全 connector 费用

本附录把 (4.5) 的大费用真正支付掉。固定
$$
\Omega=2^{360},\qquad T\ge2^{24},\qquad
L=3+2\ell\le25/8,\qquad B=T-L.
\tag{A.1}
$$
背景采用 R11 的实际第四模 connector 和 R72 尾，再在 $[B,T]$ 用 R11 附录 A 的同一匹配曲线选取一个共同好参数。两帽均如此。R14 的几何与起点结论对每个 $T\ge9$ 一致成立，故没有把不同接线对象混在一起。

以下 $Y_n=(y_n,y_n'/m)$，端点向量取 Euclidean 范数；标签和尾状态继续用 (1.6) 的范数。

### A.1 固定 $\Omega$ 确实满足真实尾的尺度门

未改背景满足
$$
h(T)\le\cosh(\sqrt2T)\le e^{\sqrt2T}.
\tag{A.2}
$$
因为 $\cosh(\sqrt2x)-h$ 的 $(\partial_x^2-2)$ 像为
$(2+\sqrt2/4)\sech^2x\,h>0$，且原点两初值为零，(A.2) 由正 Green 核直接得到。

R14 给 $h(1)>7/8$、$h'(1)>0$。还可稍加强它的增长下界：
$2+\sqrt2/4<19/8$，而
$\cosh1>37/24$、$(37/24)^2>19/8$，所以 $h''/h>1$ 于 $x\ge1$。
常系数比较于是给
$$
h(T)>\frac78\cosh(T-1)>\frac18e^T.
\tag{A.3}
$$
R11 准备段满足
$$
h(T)\le h_a<\frac32h(T),\qquad
\frac23<\omega_a<3.
\tag{A.4}
$$
其中上界 $\omega_a<3$ 来自两个短段至多 $3\eta$ 的正积分，主段 $q=-1$ 只使 $\omega$ 减小。

记 R11 末端为 $H,\omega_e$。由其实际放大和终端估计，
$$
H^2<5\Omega h(T)^2,\qquad
\omega_e<\frac54\Omega,\qquad
H\omega_e>\frac14h(T)\Omega^{3/2}.
\tag{A.5}
$$
在真实参考尾 $1<b<2$、$\delta_{128}>2^{-132}$，故
$\bar W_b=\delta_{128}^6/b^7>2^{-799}$。于是
$$
\epsilon_{\rm tail}=(H\omega_e\bar W_b)^{-1}
<2^{264}e^{-T}<1.
\tag{A.6}
$$
R11 的最低模低高度门也实际满足。对原单位 $y_4=\sech^{4\sqrt2}x$，
准备段 $y_a\le y_4(T)$，所以
$$
h_a^2y_a\omega_a^3
<2^{12}e^{-2T}.
$$
又
$$
40b\bar W_b/K_4
=800b^{-10}\delta_{128}^{-15/4}e^{4\tau_{128}}
<2^{610}.
$$
因此 R11 (7.3)–(7.4) 的真实 $Y_{\rm lin}$ 满足
$$
|Y_{\rm lin}|<2^{262}e^{-2T}<1/24.
\tag{A.7}
$$
这两项先保证未加 bump 的 R11 背景及线性接线确实可用。加 bump 后第四模可能改变传输振幅；下面的全模标签界会直接控制这一振幅，无需假定其等于原来数值。

### A.2 未改负势帽：从角分离得到真正的输出状态界

在 $[2,B]$ 取实际增长解 $g_m$，满足
$$
g_m(2)=1,\qquad g_m'(2)=\sqrt2m.
$$
此区间 $16/9<-V_4<2$，Riccati 比较给
$$
\frac43\le\frac{g_m'}{mg_m}\le\sqrt2,\qquad
g_m(B)/g_m(x)\ge e^{(4/3)m(B-x)}.
\tag{A.8}
$$
好参数的实际允许线在 $B$ 处与 $Y(g_m;B)$ 的正弦夹角至少
$\varepsilon_*=2^{-39}$。先设帽与 connector 上无源。
Sturm Wronskian 的常数性给
$$
\varepsilon_*\|Y_n(B)\|_2\|Y(g_m;B)\|_2
\le|\det(Y_n(2),Y(g_m;2))|
<2\|Y_n(2)\|_2.
$$
所以真正的正向状态满足
$$
\boxed{\quad
\|Y_n(B)\|_2\le
2^{40}e^{-(4/3)m(B-2)}\|Y_n(2)\|_2.
\quad}
\tag{A.9}
$$
这里用了 Wronskian 和完整增长幅度，而不是把角距本身当成内部标签范数。

若允许普通源 $L_ny_n=f_n$ 支持在未改帽 $[2,B]$，但 $B$ 以外保持齐次，则同一 Wronskian 的导数为 $f_ng_m/m$，从而 (A.9) 的右端改为
$$
2^{40}e^{-(4/3)m(B-2)}\mathcal C_n,\qquad
\mathcal C_n=
\|Y_n(2)\|_2+
\frac1m\int_2^B e^{(4/3)m(x-2)}|f_n(x)|\,dx.
\tag{A.10}
$$
这个源权是明确的径向普通源积分，不是端口跳量。任意无衰减的帽末端源不自动满足一个与 $T$ 无关的小权。

### A.3 双 bump 和整个 connector 的正向全频传播

在双 bump 区间 $|V|<4$，状态 $Y$ 的生成矩阵最大行和至多 $4m$，所以正向传播至多 $e^{4mL}$。

connector 取 R11 的实际变量 $t=\log h$ 和 $q=\omega'/\omega^2$，对所有模式使用
$$
Z_n=(y_n,y_{n,t}/m).
$$
其**真实**方程是
$$
\frac{dZ_n}{dt}
=\begin{pmatrix}0&m\\m(q+1)&-q\end{pmatrix}Z_n.
\tag{A.11}
$$
R11 各段 $-8\le q\le2$，整个 $t$ 长度小于
$$
\frac13+2\eta+
\frac12\log(\Omega/\omega_a)+\log(9/8)+2\eta<127,
$$
用的是 $\omega_a>2/3$、$\log2<7/10$、$\log(3/2)<1/2$。
因 $m\ge4$，(A.11) 的最大行和不超过 $7m+8\le9m$，故
$$
\|Z_n({\rm end})\|_\infty
\le e^{1143m}\|Z_n({\rm start})\|_\infty.
\tag{A.12}
$$
起点 $\omega_0>1$，所以 $\|Z({\rm start})\|_\infty\le\|Y(T)\|_\infty$。组合 (A.9)–(A.12)，并用 $B=T-L$、$L\le25/8$，得到
$$
\|Z_n({\rm end})\|_\infty
\le2^{41}
\exp\!\left[-\left(\frac43T-1164\right)m\right]\mathcal C_n.
\tag{A.13}
$$
全 connector 的可能增长已收费；没有假定所有高模沿第四模不变方向。

### A.4 真实尾缩放及强标签的全部费用

令 $V^{\rm ref}_{n,128}$ 是在 R11 的 $\epsilon_{\rm tail}$ 参考半径 $b$ 上、等比缩放 $\rho$ 之前的 raw 状态。因为物理高度先除以 $\rho$、半径除以 $\rho$，准确有
$$
V^{\rm ref}_{n,128}=\rho^3V^{\rm physical}_{n,128}.
$$
用 $C=\omega(y-y_t/m^2)$、$rC_r=\omega(y-y_t)$ 逐项得到
$$
(V^{\rm ref})_1
=\frac{\nu_mH\omega_e}{b^3}(Z_1-Z_2/m),\qquad
(V^{\rm ref})_2
=-\frac{(m^2-1)H\omega_e}{\sqrt{12}b^3}Z_1.
\tag{A.14}
$$
特别第二式中 $Z_2$ 准确抵消。由于
$\zeta_{128}=\epsilon_{\rm tail}\delta_{128}^{39/4}$，
(A.5)、(A.6) 给
$$
\zeta_{128}^{-1}\|V^{\rm ref}_{n,128}\|_\infty
\le8\delta_{128}^{-15/4}\Omega^3e^{3T}m^4
\|Z_n({\rm end})\|_\infty.
\tag{A.15}
$$
这里 $2\sqrt2T<3T$ 只用于一个保守上界；所有横向、纵向及 $\epsilon$ 因子都已保留。

用 $\delta_{128}^{-15/4}<2^{496}$、$\Omega^3=2^{1080}$，再代入 (4.5)、(A.13)，得到
$$
|a_n|
\le2^{1620}m^4
\exp\!\left\{
-\frac43Tm+3T+1535m+
2\cdot10^6[1+\log(1+m)]^2
\right\}\mathcal C_n.
$$
对 $m\ge4$，$3T\le3Tm/4$、$4\log m\le3m/2$、
$1620\log2\le284m$，故
$$
|a_n|\le
\exp\!\left\{
-\frac7{12}Tm+2000m+
2\cdot10^6[1+\log(1+m)]^2
\right\}\mathcal C_n.
\tag{A.16}
$$
函数 $[1+\log(1+m)]^2/m$ 在 $m\ge4$ 递减，且在 4 小于 $9/4$。
因此对数项不超过 $4500000m$。最后
$$
\frac T3\ge\frac{2^{24}}3>4502000
$$
支付全部剩余费用，得到准确的统一结论
$$
\boxed{\quad |a_n|\le e^{-Tm/4}\mathcal C_n
\qquad(n\in4\mathbb Z\setminus\{0\}).\quad}
\tag{A.17}
$$
这是从核心 $x=2$ 的实际允许解，经未改帽、双 bump、整个 connector、真实缩放和无限尾标签的完整界。它覆盖任意高频，没有固定角带损失。若仅有核心源，$\mathcal C_n=\|Y_n(2)\|_2$；两端逐一同样成立。

### A.5 与 R13 普通源逆的实际组合

取源支持在 $I=[-2,2]$；$|n|\ne4$ 使用 R13 的实际 Robin 解。其界
$\|y\|_2\le9m^2\|f_n\|_2$、
$\|y'\|_2\le14m^3\|f_n\|_2$、
$\|y''\|_2\le19m^4\|f_n\|_2$
通过
$$
|v(\pm2)|\le\tfrac12\|v\|_{L^2(I)}+2\|v'\|_{L^2(I)}
$$
给
$$
\|Y_n(\pm2)\|_2\le50m^3\|f_n\|_2.
\tag{A.18}
$$
该迹不等式可取一个函数值不超过均方根的点，再沿区间积分得到。

对 $|n|=4$，要求 R13 的实际兼容条件
$\int_I f_ny_4=0$ 并选定核规范。其余谱离零大于 10，
全线投影逆有 $\|y\|_2\le\|f_n\|_2/10$。能量式给
$\|y'\|_2^2\le(1/10+32/100)\|f_n\|_2^2$，
核心内 $\|y''\|_2\le(1+32/10)\|f_n\|_2$，所以 (A.18) 也成立。可另加的齐次第四模振幅按 (A.17) 独立计入。

于是每帽的真实全部内部标签满足
$$
\sum_n e^{\sigma m}|a_n|
\le50\sum_n e^{\sigma m}m^3e^{-Tm/4}\|f_n\|_2
\le3200e^{-T}\sum_n e^{\sigma m}\|f_n\|_2
\qquad(\sigma\ge0).
\tag{A.19}
$$
两个真实齐次尾的强范数合计由 $\|\mathcal H\|<4$ 得
$$
\boxed{\quad
\|X_{\rm left}\|_{\mathcal X,\sigma}
+\|X_{\rm right}\|_{\mathcal X,\sigma}
\le25600e^{-T}
\sum_n e^{\sigma m}\|f_n\|_{L^2(I)}.
\quad}
\tag{A.20}
$$
这已经把 R13 的普通核心源接入全部真实尾的强空间，不是只保留形式 Robin 行。源在长帽时还须使用 (A.10) 的已给权；源在实际尾时须使用正文 (5.3)、(6.1) 和仿射迹。没有把这些不同源位置的费用抹成同一个免费常数。

完整非线性问题仍须对它实际产生的帽源、connector 源及临界兼容逐项付费。特别 (A.20) 不能直接改写成任意非径向背景的统一线性逆。
