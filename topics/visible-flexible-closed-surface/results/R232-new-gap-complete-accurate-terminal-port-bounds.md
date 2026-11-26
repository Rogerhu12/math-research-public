# R232：最后 ramp 格所需的完整准确 coast 端口连续差界

本条把新 gap1.05/v.045 前缀的完整末端口作为真实对象消费。准确曲线是 R224/R225 同一保存 Γ95 实 Fourier 和；旧端迹是同一 ramp master 的第 16 节点，全部实 Fourier 次数 384，不省略高频。本条给出准确弧长角反参后的 $P,V,A$ 及其 native 角一、二阶导数差，供最后一个长约 $.00375$ 的 Hermite 格实际消费；尚不声称那个完整格已通过。

## 1. 对象和新的准确目标盒

令冻结 dyadic 中央椭圆半轴为 $A,B$，$\ell=(A^2\sin^2\theta+B^2\cos^2\theta)^{1/2}$，$a_\ell=\operatorname{mean}\ell$。本文取准确 dyadic $v,r$，即保存二进数 $.045,.06$，并令

$$
f_0=a_\ell+vr/2.
$$

这是 R229/R231 归一化前缀的准确目标。它与 R224 的 $P(7/5,1/2)/(2\pi)+(9/200)(3/50)/2$ 是两个极接近但不同的定义。实际有理比较发现前者不包含在 R224 原窄目标盒内；本条没有偷用那一窄盒。它重新把新 $f_0$ 带入同一 Γ95 的完整 coast 几何包含。

写原准确 Γ95 曲线为 $\Gamma(\eta)$、其 native 速度 $q_\Gamma=|\Gamma'|$、准确周长半径 $a_\Gamma=\operatorname{mean}q_\Gamma$、常数 Fourier 系数 $C_\Gamma$。R225 给出的准确弧长盒为

$$
\frac{79658596287913338895451555727}{79228162514264337593543950336}
\le a_\Gamma\le
\frac{79658596287972559706017116211}{79228162514264337593543950336}.
$$

源码显式消费该上下界，并核 R225 正文中的分子及同一 coast master SHA。准确 coast 入口在中央 native $\theta$ 中定义为

$$
\int_0^{\eta(\theta)}q_\Gamma(\tau)\,d\tau
=\frac{a_\Gamma}{a_\ell}\int_0^\theta\ell(\tau)\,d\tau,\qquad
P_*(\theta)=C_\Gamma+\frac{f_0}{a_\Gamma}
[\Gamma(\eta(\theta))-C_\Gamma].
$$

因此实际 matching 不是简单地令 $\eta=\theta$。后续所有端口均消费同一 $\eta$。

## 2. 准确 ruling 入口的全部导数

先在 Γ95 自己的 native 角中写

$$
T=\Gamma'/q_\Gamma,\quad
T_u=(a_\Gamma/q_\Gamma)T',\quad
U=T_u/|T_u|,\quad
\rho=v/|T_u|,
$$

$$
d=-\rho U+\sqrt{1-\rho^2}\,(T\times U),\qquad N=d\times T.
$$

全域包含证明 $|T_u|>v$，并且 $T'\cdot N>0$，故所有平方根和除法在整个圆周合法。准确径向一、二阶端迹是

$$
V_*=d,\qquad
A_*=\frac{a_\Gamma}{f_0}
\frac{(d'\cdot N)^2}{q_\Gamma(T'\cdot N)}N.
$$

这正是 R137 的 $(m^2/n)N$，因为 $m=(a_\Gamma/f_0)(d'\cdot N)/q_\Gamma$、$n=(a_\Gamma/f_0)(T'\cdot N)/q_\Gamma$。$P_*,V_*,A_*$ 不是独立拟合或独立投影的三个函数。

实现对上述表达式作准确区间 Taylor 代数，计算至少八阶 native 导数；曲线输入到第十一阶。逆和平方根系数按准确卷积递推求出，零阶分母及根号全域严格为正。方向 $N=d\times T$ 与已登记 supplier 一致。

## 3. 同 native 角差的连续证书

圆周分成 2048 个完整角块。每块中心是准确 $\pi$ 的有理倍；三角函数使用现有 96-bit 定向整数 Taylor 包含。任意 Fourier 导数在整个角块的盒，使用中心值、中心下一导数及完整二阶 Taylor 余项：

$$
F^{(j)}(\theta_0+h)
\in F^{(j)}(\theta_0)
+hF^{(j+1)}(\theta_0)
+\frac{h^2}{2}[-M_{j+2},M_{j+2}],
$$

$$
M_{j+2}\ge
\sum_k |k|^{j+2}(|a_k|+|b_k|).
$$

比较 accurate ruling 的 $d,A_*$ 与旧 $V,A$ 时，旧场的 $|k|\le95$ 部分在同一中心作 Taylor 比较。对每个所需导数阶 $r=0,1,2$，保留中心差的前六项，再加整个角块上 $r+6$ 阶差的余项。若 $\beta_j$ 是两函数 Taylor 系数之差，半宽为 $h_*$，则逐 Cartesian 分量求和的安全界为

$$
\sum_{j=r}^{r+5}\frac{j!}{(j-r)!}|\beta_j|h_*^{j-r}
+\frac{h_*^6}{6!}\sup_{\rm cell}|(F_*-F_{\rm low})^{(r+6)}|.
$$

整个余项导数的盒也来自同一准确 Taylor 代数，未由中心采样猜测。旧 $95<|k|\le384$ 的每个系数再按 $|k|^r$ 完整绝对和加入。位置 $P$ 的同角差则直接按 Γ95 与完整 Γ384 的准确 Fourier 系数差，以及统一缩放误差计算。

## 4. 完整弧长反参和两阶链式法则

写 $p=f_0/a_\ell$。准确整数全频卷积证明

$$
R=q_\Gamma^2-p^2\ell^2
$$

及 $R',R''$ 的全圆周绝对和上界。取这些上界为 $r_0,r_1,r_2$，并设 $q_*>0$。从

$$
e=q_\Gamma-p\ell=\frac{R}{q_\Gamma+p\ell}
$$

得

$$
|e|\le e_0:=\frac{r_0}{q_*+p_-B}.
$$

因此准确平均值满足 $|a_\Gamma-f_0|\le e_0$；源码将这项新准确积分包含与 R225 盒相交，没有把浮点周长数定义成 $a_\Gamma$。

令 $\delta_a$ 控制 $|a_\Gamma-f_0|$，并取 $M_{q'},M_{q''},M_{\ell'}$ 的全域界。有

$$
|e'|\le e_1:=
\frac{r_1}{q_*+p_-B}
+\frac{r_0(M_{q'}+p_+M_{\ell'})}{(q_*+p_-B)^2}.
$$

零均值速度差 $D=q_\Gamma-(a_\Gamma/a_\ell)\ell$ 满足

$$
|D|\le d_0=e_0+\delta_a A/a_{\ell,-},\qquad
|D'|\le d_1=e_1+\delta_a M_{\ell'}/a_{\ell,-}.
$$

其完整圆周积分为零，所以从较短互补弧积分和 $q_\Gamma\ge q_*$ 得

$$
|\eta-\theta|\le e_\eta:=\pi d_0/q_*.
$$

再准确微分反参等式：

$$
|\eta'-1|\le e_{\eta,1}:=(d_0+M_{q'}e_\eta)/q_*,
$$

$$
|\eta''|\le e_{\eta,2}:=
[d_1+M_{q''}e_\eta+(2e_{\eta,1}+e_{\eta,1}^2)M_{q'}]/q_*.
$$

对任一准确 native 端口函数 $F$，若其同角比较误差是 $\delta_0,\delta_1,\delta_2$，其一至三阶自身导数界为 $M_1,M_2,M_3$，则真正中央 native 角中的误差不超过

$$
\delta_0+M_1e_\eta,
$$

$$
\delta_1+M_2e_\eta+M_1e_{\eta,1},
$$

$$
\delta_2+M_3e_\eta+M_2(2e_{\eta,1}+e_{\eta,1}^2)+M_1e_{\eta,2}.
$$

位置函数在这里保留准确比例 $f_0/a_\Gamma$；没有把它省略为 1。上述步骤同时支付部分弧长反参、一阶角导数和二阶角导数，R225 的集合距离单式未被当成这个完整结论。

## 5. 实际严格输出

下表是严格有理上界再向外取短小十进上界，列 $r$ 表示 native $\theta$ 导数阶。全部 2048 块已覆盖。

| 端口差 | $r=0$ | $r=1$ | $r=2$ |
|---|---:|---:|---:|
| $P_*-P_{\rm old}$ | $9.349\cdot10^{-12}$ | $3.817\cdot10^{-11}$ | $1.118\cdot10^{-9}$ |
| $V_*-V_{\rm old}$ | $1.587\cdot10^{-11}$ | $8.868\cdot10^{-10}$ | $6.659\cdot10^{-8}$ |
| $A_*-A_{\rm old}$ | $3.958\cdot10^{-10}$ | $5.173\cdot10^{-8}$ | $7.744\cdot10^{-6}$ |

准确反参误差分别小于 $4.747\cdot10^{-12}$、$1.396\cdot10^{-11}$、$1.757\cdot10^{-10}$；统一比例偏离 1 小于 $2.480\cdot10^{-13}$。完整报告保存每项的准确有理上界，而非仅这些显示值。

同一进程在完整角块和整段 $\sigma\in[0,.02]$ 中，用新 $f_0$ 重新消费 R137 geometry，得到

$$
D>0.9719082693,\qquad U_t>0.9657910246,\qquad
0.1949854446<|\kappa_{\rm nonzero}|<8.892834503.
$$

这是本次新目标盒的实际包含，不是重命名 R224 原结论；此补算属于准确末端口消费的参数绑定。

## 6. 真实执行和范围

源码 6a65-geometry-final-ramp-port-certificate.py 的 SHA256 为
0cfe24c3be23e90986345119bac15c65a018aeaa9ba909318b9bbcb4d06ddc90。

完整进程自然 exit **0**，127.190803270 s，RSS **35544 KiB**。输入 ramp master SHA 为 0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7，coast master SHA 为 f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d。

完整新 report SHA 为 88b4cc19139143fdb1e85f446750f3daea70d978a139171702bb3fe6381adc89，stdout SHA 为 75fe640dbe2e1c0e19c8b989ddfa76f44f5867c719dc844437c9cf1af5159a5a。报告绑定 R225 原证明、原 Gram 入口、整数算术及本次源码 SHA，保存全角整数行流 SHA。

本条严格支付的是准确两种端口的完整连续差；接下来的 Hermite 修正必须支付短格中的 $1/L,1/L^2$ 放大，不能直接沿用前 15 格的证书。整个最后格、归一化及真实后段继续。

