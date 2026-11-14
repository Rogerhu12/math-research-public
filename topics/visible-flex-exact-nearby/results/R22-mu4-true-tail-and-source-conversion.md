# R22：$\mu=4\sqrt2$ 背景的真实平尾、全频源及物理坐标转换

日期：2026-11-10。作者：visible-exact-astra-76e8 / a_posteriori_pde。

**状态：已证明。** 本文把 R11、R15、R19 的真实尾和普通源模块接到 R20 的
$k=4$ 背景。每个坐标、物理高度、两条迹、尾参数和普通源因子都在下面重新换算；
不把 $\mu=\sqrt2$ 的几何常数转授到新背景。未改主干几何使用 R21 的独立证书。

最终参数统一取：物理核心切口 $x=\pm20$，工作坐标 $u=4x$、$u_b=80$；
两个 bump 的宽和间隔在 $u$ 坐标中分别为 $\ell\le1/16$ 和 3；
$T_u\ge2^{24}$，$\Omega=2^{360}$。实际 connector 从物理
$x=T_u/4$ 开始。

## 1. 工作坐标不是原物理 Sturm 坐标

保留 R20、R21 的物理背景
$$
k=4,\quad \mu=k\sqrt2,\quad
q_{\rm phys}=32-(32+\sqrt2)\sech^2x,\quad
h_{xx}=q_{\rm phys}h,\quad h(0)=1,\ h_x(0)=0,
$$
$$
r=h^{-1},\qquad z_x=h^{-2}.
\tag{1.1}
$$
改用 $u=kx$，并记
$$
\omega=h_u/h,\quad
q_u=\frac{h_{uu}}h
=2-\left(2+\frac{\sqrt2}{16}\right)\sech^2(u/4).
\tag{1.2}
$$
则
$$
r_u=-\omega r,\qquad z_u=\frac{r^2}{k},\qquad
z_r=-W,\quad W=\frac r{k\omega}.
\tag{1.3}
$$
特别 $z_u$ 不是 $r^2$。把 $u$ 当成原物理 Sturm 坐标会把高度、metric 和尾匹配改掉。

R21 在物理 $x=3/2$ 的准确输入给
$h>26$、$h_x/h>24/5$，并在此后保持。因此 $u\ge6$ 时
$$
h(u)>26e^{(6/5)(u-6)},\qquad
\frac65<\omega<\sqrt2.
\tag{1.4}
$$
上界由 $\omega_u=q_u-\omega^2$ 的首次交叉论证得到。
在 $u\ge8$，
$$
\frac{16}{9}<q_u<2,\qquad
\left|\frac{\omega_u}{\omega^2}\right|<1.
\tag{1.5}
$$
前式用 $\cosh2>11/3$；后式用 $q_u>0$、$\omega>6/5$。
第四模核是
$$
y_4(u)=\sech^{16\sqrt2}(u/4),\qquad
\frac{y_{4,u}}{16\omega y_4}
=-\frac{\sqrt2\tanh(u/4)}{4\omega}\in(-3/10,-1/5)
\quad(u\ge8).
\tag{1.6}
$$
所以 R11 的实际接线初值门在这个明确位置已满足，不再只引用最终渐近存在。

## 2. 物理无穷小场、源重建与真实尾斜率

对 $m\ge2$，标量齐次方程为
$$
L_m^{(u)}y=-y_{uu}+m^2q_uy=0.
\tag{2.1}
$$
对应物理环境场是
$$
U=ry,\qquad T=-U/m,\qquad
\boxed{\quad C=k\left(\omega y-\frac{y_u}{m^2}\right).\quad}
\tag{2.2}
$$
这里 $C$ 是物理竖直分量。由 (1.3) 直接微分，
$$
rC_r=k(\omega y-y_u).
\tag{2.3}
$$
因此
$$
R=\frac{y_u}{m^2\omega y},\qquad
\frac{rC_r}{C}=\frac{1-m^2R}{1-R}.
\tag{2.4}
$$
多出的 $k$ 在这个比值里准确消掉，故 R11 从真 R72 取得的
$d_*\in(14,15)$、$R_*=(1-d_*)/(16-d_*)\in(-14,-13/2)$ 仍是同一个实际尾目标。

完整线性度量源也须按坐标转换。若 $P,Q_u,R_{uu}$ 是源张量的
$\theta\theta,u\theta,uu$ 分量，令
$$
C_0=hP/2,\qquad J=(hC_0)_u-mh^2Q_u,
$$
$$
f_u=\frac{m^2h^2}{2}R_{uu}-J_u.
\tag{2.5}
$$
解 $L_m^{(u)}\eta=f_u$ 后，真实重建为
$$
U=\eta/h,\qquad T=(C_0-U)/m,\qquad
\boxed{\quad
C=k\left(\omega\eta-\frac{\eta_u}{m^2}+\frac J{m^2}\right).
\quad}
\tag{2.6}
$$
代入三个线性度量方程即可验证：$z_u$ 的 $1/k$ 与 (2.6) 的 $k$ 相消，
所以消元源 (2.5) 形式不变。若使用物理 $x$ 张量，并把按物理坐标公式定义的中间源记为
$J^{[x]}=(hC_0)_x-mh^2Q_x$，则
$$
Q_u=Q_x/k,\qquad R_{uu}=R_{xx}/k^2,\qquad
J=J^{[x]}/k,\qquad
f_u=f_x/k^2.
\tag{2.7}
$$
不能把 $f_x$ 原样输入工作坐标的算子。

## 3. 真实 connector 的准确物理缩放

控制量记为
$$
t=\log h,\qquad q_c=\omega_u/\omega^2.
$$
由 (2.1) 得
$$
\frac{d\log\omega}{dt}=q_c,\qquad
\frac{dR}{dt}=q_c(1-R)+1-m^2R^2.
\tag{3.1}
$$
因此 R11 的全部明确短过渡和横截根在这个工作坐标中成立：
先精确准备 $R=-1/2$，用 $q_c=2$ 放大到 $\omega=\Omega$，
再用 $q_c=-1$ 主段和至 $q_c=-8$ 的短过渡精确达到 $R_*$。
它仍保持核心端 $h,h_u,h_{uu}$，也就保持 $h,h_x,h_{xx}$。
所有实际短段的 $q_c\in[-8,2]$，$\omega>2/3$，
且末端
$$
H<\frac65h_a(\Omega/\omega_a)^{1/2},\quad
\frac45\Omega<\omega_e<\frac54\Omega,\quad
0<y_e\le y_a(\Omega/\omega_a)^{-4}.
\tag{3.2}
$$
这些是同一 ODE 与相同初值盒的结论，不是从旧物理高度直接缩放出来的。

记真 R72 参考 cut128 半径为 $b_{\rm tail}\in(1,2)$，
$$
\delta=\frac2{25}2^{-128},\qquad
\bar W_b=\delta^6/b_{\rm tail}^7.
$$
准确水平、垂直和尾参数为
$$
\boxed{\quad
\rho=\frac1{Hb_{\rm tail}},\qquad
\lambda=\frac1{kH^2b_{\rm tail}\omega_e\bar W_b},\qquad
\epsilon_{\rm tail}=\frac\lambda\rho
=\frac1{kH\omega_e\bar W_b}.
\quad}
\tag{3.3}
$$
于是切口物理斜率
$W_e=(\lambda/\rho)\bar W_b=r_e/(k\omega_e)$，与 (1.3) 完全相同。
真尾常平台的 $rW_r/W=-7$，所以 $q_c=-8$；物理背景的完整二阶 jet 匹配。
第四模 $C=k\omega y(1-R)$ 及 $rC_r=d_*C$ 也同时匹配，真实高度方程给二阶高度 jet 匹配。

非线性尾仍须先在参考半径上以 (3.3) 的 $\epsilon_{\rm tail}$ 调用 R72，
再等比缩放 $\rho$。没有各向异性搬用一个既有非线性等距族。

同一个有限 connector 的真实物理主曲率为
$$
\kappa_\theta=\frac1{\sqrt{r^2+k^2\omega^2}},\qquad
\kappa_s=\frac{k^2(q_c+1)\omega^2}
{(r^2+k^2\omega^2)^{3/2}},
$$
$$
|\kappa_\theta|\le\frac1{k\omega},\qquad
|\kappa_s|\le\frac{|q_c+1|}{k\omega}.
\tag{3.4}
$$
这是物理 $1/k$ 因子；全局 reach 仍应由同一完整背景的几何证明给出。

## 4. 双 bump、真实全频线与实际谱误差

令 $L=3+2\ell$、$B_u=T_u-L$。在工作坐标区间 $[B_u,T_u]$ 放 R11 附录的两个 bump。
由 (1.4)–(1.5)，该整个区间满足其真实负势盒。
第四模的真实右端斜率为
$$
-\frac{y_{4,u}(T_u)}{4y_4(T_u)}
=\sqrt2\tanh(T_u/4)\in[1,3/2].
$$
第 3 节已经提供实际匹配起点，因此双 bump 的匹配曲线确实保持这个核。
变分方程、$D_4$ 的 $45/4,181$ 界及全部测度常数都是 $u$ 方程的计算；
没有额外 $k$ 因子。可同时选两帽参数，使所有 $m\in4\mathbb N$ 的允许线与增长线夹角满足
$$
|\sin\angle|\ge2^{-39}.
\tag{4.1}
$$
线本身来自 R15 的未冻结全标签真实尾，经第 3 节的实际 connector 传播。

在未改工作帽 $[80,B_u]$，Riccati 区间仍为
$[4/3,\sqrt2]$。这里下端点也可直接支付：$\cosh3>6$，故
在 $u\ge12$ 有 $q_u>2-(17/8)/36>31/16$。
若此时 $\omega\le4/3$，则
$\omega_u=q_u-\omega^2>31/16-16/9=23/144$；
由已有的 $\omega>6/5$，不到一个单位的 $u$ 长度就必越过 $4/3$，
之后该边界处导数严格为正，不能向下穿越。
因此 $u\ge13$ 已有 $\omega>4/3$，特别覆盖整个未改帽。
所以工作坐标 Robin 误差满足
$$
|\delta_{u,m}|
\le12m\,2^{39}e^{-(8/3)m(B_u-80)}.
\tag{4.2}
$$
物理导数是 $\partial_x=k\partial_u$，故
$$
\delta_{x,m}=k\delta_{u,m}.
\tag{4.3}
$$
当 $B_u-80\ge10$，(4.2) 已保证
$$
|\delta_{x,m}|\le\frac1{400k^3m^3}
=\frac1{25600m^3}.
\tag{4.4}
$$
例如乘上右侧分母后，常数小于 $2^{60}m^4e^{-(80/3)m}$；
该式对 $m\ge4$ 递减，其在 $m=4$ 小于 $2^{68-106}<1$。
当前 $T_u\ge2^{24}$ 当然满足此门。第四模自身误差准确为零。

R20 的物理谱逆、点源迹及 R13 的同一秩二公式于是给实际核心
$I_x=[-20,20]$ 的普通源界
$$
\boxed{\quad
\|y\|_2\le144m^2\|f_x\|_2,\qquad
\|y_x\|_2\le896m^3\|f_x\|_2,\qquad
\|y_{xx}\|_2\le4864m^4\|f_x\|_2
\quad}
\tag{4.5}
$$
于 $m\ne4$。其原始常数分别为 $9k^2,14k^3,19k^4$。
证明中点源列、其导数、迹矩阵的界分别为
$15k^{5/2}m^{5/2}$、$30k^{7/2}m^{7/2}$、$42k^3m^3$；
与 (4.4) 相乘仍是 $42/400$，所以 $9/8$ 的逆界不变。

若帽源产生工作坐标非齐次项 $\beta_{u,\pm}$，则物理端点项为
$\beta_{x,\pm}=k\beta_{u,\pm}$。核心边界负荷的额外 $L^2,H^1,H^2$ 界分别可取
$$
544m^{5/2}|\beta_x|_2,\qquad
4352m^{7/2}|\beta_x|_2,\qquad
17408m^{9/2}|\beta_x|_2.
\tag{4.6}
$$
这是 $17k^{5/2},34k^{7/2},34k^{9/2}$ 的准确代入。
第四模必须满足
$$
\int_{-20}^{20}f_xy_k\,dx+
y_k(20)\beta_{x,+}-y_k(-20)\beta_{x,-}=0.
\tag{4.7}
$$
均值和最低模兼容仍未被坐标变化取消。

## 5. 锥形真实源与 $h^2$ 规范

在工作帽 $80\le u\le B_u$，采用
$$
\mathcal F_{m,h}^{(u)}
=\sup_u e^{m(u-80)/2}h(u)^2
\frac{|f_u(u)|}{m^2},
$$
$$
\mathcal Y_{m,h}^{(u)}
=\sup_u e^{m(u-80)/2}h(u)^2
\left(|\eta|+\frac{|\eta_u|}{m}
+\frac{|\eta_{uu}|}{m^2}\right).
\tag{5.1}
$$
这里 $f_u=f_x/16$。精确屏障
$h(80)^2h(u)^{-2}e^{-m(u-80)/2}$ 满足
$$
\frac{L_m^{(u)}\mathfrak b_m}{\mathfrak b_m}
=(m^2+2)q_u-\frac{m^2}{4}-2m\omega-6\omega^2
>\frac{m^2}{4},
$$
因为 (1.5) 给与 R19 相同的逐项界。因此同一真实边界证明给
$$
\boxed{\quad
\mathcal Y_{m,h}^{(u)}
\le2^{50}\left(h(80)^2|\eta(80)|
+\mathcal F_{m,h}^{(u)}\right).
\quad}
\tag{5.2}
$$
换成物理 $x$ 时，导数项分别是
$|\eta_x|/(4m)$、$|\eta_{xx}|/(16m^2)$；这些因子不可省略。

用真实物理向量场、但以 $u$ 导数定义 R19 的一至三阶 jet 范数
$\mathcal E^3_{h,\rho_0;u}$。对 (2.5) 的实际二次度量源，
$|(h^2)_u|\le3h^2$、$|(h^2)_{uu}|\le8h^2$；
两份场范数的 $h^4$ 与消元源再乘权的 $h^4$ 准确抵消。所以
$$
\boxed{\quad
\sum_n e^{\rho_0m}\mathcal F_{m,h}^{(u)}
\le3\|Y\|_{\mathcal E^3_{h,\rho_0;u}}
\|Z\|_{\mathcal E^3_{h,\rho_0;u}}.
\quad}
\tag{5.3}
$$
物理竖直分量中的 $k$ 已包含在场范数里；它没有被在材料估计时抹掉。

对本背景单位第四模，R19 的 $u$ 导数计算仍给
$|y^{(j)}|/y\le1,6,42,336,3012$：其对数导数
$-4\sqrt2\tanh(u/4)$ 的更高导数只比旧界小。
物理高度 (2.2) 多一个 $k=4$，故全部一至三阶环境 $u$-jet 可保守取
$2^{15}y_4$。又
$$
h^2y_4\le2^{16\sqrt2}e^{-2\sqrt2u}
<2^{23}e^{-2\sqrt2u}.
$$
因此
$$
\|\varepsilon Z_k\|_{\mathcal E^3_{h,0;u};\,u\ge80}
\le2^{40}|\varepsilon|e^{-160\sqrt2}
<2^{-280}|\varepsilon|.
\tag{5.4}
$$
改为物理 $x$ 的三阶 jet 至多再乘 $4^3=64$。
特别 cap 的 $2^{50}$ 常数作用于这个实际输入仍小于
$2^{-230}|\varepsilon|$；本帽端模块有明确小量余地，不依赖可见幅度先取极小。

## 6. 真实全 connector 与标签：多出的 $k^2$ 已支付

固定
$$
\Omega=2^{360},\quad T_u\ge2^{24},\quad
u_b=80,\quad B_u=T_u-L.
\tag{6.1}
$$
第 3 节的准备、放大、末端过渡的总 $t=\log h$ 长度仍小于 127。
对全频状态 $Z_n=(y,y_t/m)$，
$$
\partial_tZ_n=
\begin{pmatrix}0&m\\m(q_c+1)&-q_c\end{pmatrix}Z_n,
$$
故整个实际 connector 正向费仍不超过 $e^{1143m}$。
双 bump 在 $u$ 上的真实费为 $e^{4mL}$。

设 $V^{\rm ref}$ 是 R72 参考半径、等比缩放 $\rho$ 以前的 raw 高度状态。
由 (2.2)、(2.3)、(3.3) 逐项得到
$$
(V^{\rm ref})_1
=\frac{k\nu_mH\omega_e}{b_{\rm tail}^3}(Z_1-Z_2/m),
$$
$$
(V^{\rm ref})_2
=-\frac{k(m^2-1)H\omega_e}{\sqrt{12}b_{\rm tail}^3}Z_1.
\tag{6.2}
$$
又 $\zeta_{128}=\epsilon_{\rm tail}\delta^{39/4}$，所以
$$
\zeta_{128}^{-1}\|V^{\rm ref}\|_\infty
\le k^2\delta^{-15/4}
\frac{H^2\omega_e^2}{b_{\rm tail}^{10}}m^4\|Z\|_\infty.
\tag{6.3}
$$
与旧背景相比，这里准确多出 $k^2=16$，并非一个遗漏的高度比例。

由实际准备段
$H^2\omega_e^2<8\Omega^3h(T_u)^2$，而
$h(T_u)^2/h(B_u)^2\le e^{2\sqrt2L}<e^{3L}$。
故 (5.2) 的 $h(B_u)^{-2}$ 与 (6.3) 的径向因子直接消去。
再支付 R15 的全部标签权
$e^{371m+2\cdot10^6(1+\log(1+m))^2}$，得到
$$
|a_n^{\rm tail}|
\le
\exp\left\{\left(-\frac{T_u}{2}+2000\right)m+
2\cdot10^6[1+\log(1+m)]^2\right\}
\left(h(80)^2|\eta_n(80)|+\mathcal F_{m,h}^{(u)}\right).
\tag{6.4}
$$
2000 仍覆盖全部变化：把旧左切口 20 换成 80 多花 $30m$，
$k^2=16$ 多花小于 $m$；旧总线性频率费用小于 $1854m$，仍有严格余量。
用 R15 的对数平方上界及 $(3/8)2^{24}>4502000$，最后得到
$$
\boxed{\quad
|a_n^{\rm tail}|
\le e^{-T_um/8}
\left(h(80)^2|\eta_n(80)|+\mathcal F_{m,h}^{(u)}\right).
\quad}
\tag{6.5}
$$
这对全部非零 $4\mathbb Z$ 模成立，且同一个参数已保持第四模核。
正负频率及两帽可在强 $\ell^1$ 范数中同时求和。

取原单位第四模时，尺度门也直接支付：由 (1.4) 可在 $T_u\ge20$
取 $h(T_u)>e^{T_u}/4$，而 $h(T_u)\le e^{\sqrt2T_u}$。
代入 (3.3) 与真实输入式，保守得到
$$
\epsilon_{\rm tail}<2^{270}e^{-T_u}<1,\qquad
|Y_{\rm lin}|<2^{290}e^{-2T_u}<1/24.
\tag{6.6}
$$
具体地，旧 $y_4$ 的 $2^6$ 尾常数换成 $2^{23}$，再付 $k^2=16$，
使 R11/R15 的 $2^{262}$ 常数至多变为 $2^{283}$，由 $2^{290}$ 覆盖。
加 bump 后的真实第四模振幅直接用 (6.5) 控制，不假定传输振幅保持。

## 7. 真尾自身的连续源及物理 $C^2$ 换算

参考尾的实际方程、标签层、R15 的 $\mathcal S_1,\mathcal S_2$、
常数 $2^{77}$ 和 $C^2$ 平坦指数 $19/4$ 不含 $k$；
它们在 (3.3) 的真实 $\epsilon_{\rm tail}$ 上使用，且始终是全部内部标签空间。

但从物理普通高度源搬到参考尾必须付缩放。令
$$
C^{\rm ref}(\bar r)=C^{\rm physical}(\rho\bar r)/\rho.
$$
则
$$
V^{\rm ref}=\rho^3V^{\rm physical},\qquad
F^{\rm ref}=\rho F^{\rm physical},\qquad
N^{\rm ref}=\rho^3N^{\rm physical},
\tag{7.1}
$$
其中 $F$ 是真实高度二阶方程的普通源，
$N=p_*F/(12r^2)$ 是其 canonical 源。式 (7.1) 来自两次物理半径微分，
不能把任意 Sturm 消元源未经重建就当作 $F$。
将 $N^{\rm ref}$ 代入 R15 的实际积分和点态源范数，才可调用其连续源 Green 结论。

一个有用的精确抵消是
$$
\boxed{\quad
\rho^{-1}\epsilon_{\rm tail}
=\frac{b_{\rm tail}}{k\omega_e\bar W_b}.
\quad}
\tag{7.2}
$$
参考尾高度的二阶物理缩放费至多 $\rho^{-1}$；
R15 的实际 $C^2$ 平坦界包含 $\epsilon_{\rm tail}$。
因此二者相乘后没有 $h(T_u)$ 因子。例如在参考胞元 $j$，
转为物理 Cartesian 二阶 jets 可统一取
$$
\|C^{\rm physical}\|_{C^2;\,j}
\le2^{96}626^{313}
\frac{b_{\rm tail}}{k\omega_e\bar W_b}
\delta_j^{19/4}
\left(\|X\|_{\mathcal X}
+\|N^{\rm ref}\|_{\mathcal S_1}
+\|N^{\rm ref}\|_{\mathcal S_2}\right).
\tag{7.3}
$$
$2^6$ 的额外常数覆盖参考半径 $1\le\bar r\le2$ 的极坐标到 Cartesian 转换。
平盘上的高度为零，极点没有再除一个未知小半径。
所以极大的 $T_u$ 不会仅因帽半径很小就把真实尾二阶扰动吹大；
强标签小量仍有物理意义。

## 8. 已匹配对象与范围

本稿支付的是同一 $k=4$ 物理对象：

1. R20/R21 的未改核心，物理 $z_x=h^{-2}$；
2. 工作坐标 $u=4x$ 下的未改长帽、双 bump 和实际 R11 connector；
3. 以 (3.3) 参数重新调用的完整 R72 真实尾和固定开平盘；
4. 全部高模的非零允许线、谱门、非齐次核心 DN、锥形普通源、
   统一强标签和物理 $C^2$ 源换算。

R21 的全局几何证书针对未改主干；实际 graft 的全局支撑、直径和 reach
应沿 (3.4) 及真实 tail 缩放另证，不能仅由本稿的坐标等价替代。
非线性尾产生的全部高两迹、mean、源重建中的 $J$ 项和最低模兼容也必须联立；
本稿不把实际尾流形换成其线性切空间，不宣称已经支付完整有限可见幅精确族。
