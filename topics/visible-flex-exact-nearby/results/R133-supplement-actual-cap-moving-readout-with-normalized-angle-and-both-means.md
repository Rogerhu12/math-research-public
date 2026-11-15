# R133 续篇：实际帽解的 moving 读出、准确角规范与两个均值

2026-11-15，visible-exact / root。

**已证明完整复邻域中的换角读出，并应用于实际全模帽解。**
真实物理曲率决定一个唯一的归一 moving 角；其 inverse 在明确的
共同复条带中存在。下面同时证明原角相位规范、两个曲率均值、
完整 joint Wiener 读出和有限高阶值界，不给任意零宽函数免费组合。

实际解来自
[X：修补 M32 中心的全模正帽存在性](R133-supplement-actual-all-mode-positive-cap-existence-at-repaired-M32-centre.md)，
SHA256 8b49cd59f90b8869dca4be635b80a7f7e34c04af4b8632ad772b0a9b45bfcd86。
已知中心的更宽物理系数界来自
[连续中心 C.4--C.8](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md)，
SHA256 b2acc995d8ef0c880c93b21226f53da0470a9945e53f67643106b0522a8c2404。
本文只消费这些解析界和已成 X，没有新数值计算。

## 1. 完整坐标邻域与平均值

所有 Fourier 频率为 $k\in4\mathbb Z$；均值使用同一归一圆周测度。
径向区间仍为 $I=[9/10,25/8]$，joint norm 的顺序为
先逐系数取 $\sup_{r\in I}$，再对频率求和。
令
$$
 s_0=\frac1{64},\qquad \sigma=\frac1{8192},\qquad
 \rho=3\,10^{-6},\qquad \tau=\frac{\sigma}{32}=2^{-18}.
 \tag{Y.1}
$$
用帽证明的真实物理中心 $\widehat W=(\widehat B,\widehat C)$。
其已付完整界可宽取为
$$
 \|\widehat C\|_{\mathscr A_{s_0}}<\frac13,\qquad
 \|1/\widehat C\|_{\mathscr A_{s_0}}<6,\qquad
 \|\widehat B/\widehat C\|_{\mathscr A_{s_0}}<\frac1{50}.
 \tag{Y.2}
$$
中心在实角上 $\widehat C<0$，所以 $-\widehat C>1/6$。
这里的 $1/\widehat C$ 与 $\widehat B/\widehat C$ 都是已转到
物理角后的函数；没有把 moving 范数直接套到物理函数。

先证明一个独立坐标引理：允许任意复四重 pair
$$
 W=(B,C)=\widehat W+(b,c),\qquad
       \|(b,c)\|_{X_\sigma}\le\rho .
 \tag{Y.3}
$$
这个引理本身不声称一般 parity 的数据已有 PDE 解。
实际应用最后限制到 X 已证明的复反射参数域。

写
$$
 c_0(r)=\langle C\rangle_\theta,\qquad
 \widehat c_0(r)=\langle\widehat C\rangle_\theta,\qquad
 j=C/c_0,\quad \widehat j=\widehat C/\widehat c_0.
 \tag{Y.4}
$$
由于 $\widehat C$ 实负，
$|\widehat c_0|>1/6$；(Y.3) 给
$|c_0|>1/6-\rho>1/7$。归一因子使用真实复数 $c_0$，
不以 $|c_0|$ 代替它。
因此
$$
 \langle j\rangle_\theta=1,\quad
 \|\widehat j\|_{\mathscr A_{s_0}}<2,\quad
 \widehat j(r,\theta)>\frac12\ \text{在实角上},
$$
$$
 \|j-\widehat j\|_{\mathscr A_\sigma}
 \le7\|c\|+7\cdot6\,\|\widehat C\|\,|\langle c\rangle|
 <21\rho .
 \tag{Y.5}
$$
取原零mean primitive $I_\theta=\partial_\theta^{-1}P_{\ne0}$，
其 $4\mathbb Z$ Wiener norm 为 $1/4$，并定义
$$
 h=I_\theta(j-1),\qquad
 \Phi(\theta)=\theta+h(\theta),\qquad
 \widehat h=I_\theta(\widehat j-1).
 \tag{Y.6}
$$
于是 $\Phi'=j$，$\Phi(\theta+\pi/2)=\Phi(\theta)+\pi/2$，并且
$$
 \|h-\widehat h\|_{\mathscr A_\sigma}<21\rho/4.
 \tag{Y.7}
$$

## 2. 共同复条带中的全局 inverse

记 $S_s=\{z:|\Im z|<s\}$。因为
$s_0-\sigma/2>1/128$，完整 Fourier Cauchy 估计给
$$
 \|\widehat j_\theta\|_{\mathscr A_{\sigma/2}}<256.
$$
从实角向竖直线积分，得到在整个 $S_{\sigma/2}$ 上
$$
 \Re\widehat j>\frac12-256\frac\sigma2
              =\frac{31}{64},\qquad
 \Re j>\frac{31}{64}-21\rho>\frac{15}{32}.
 \tag{Y.8}
$$
这个结论对 (Y.3) 的全部复 pair 都成立，不依赖 $C$ 为实函数。

对 $z_1\ne z_2$，复条带凸，故
$$
 \frac{\Phi(z_2)-\Phi(z_1)}{z_2-z_1}
       =\int_0^1 j(z_1+t(z_2-z_1))\,dt
$$
的实部大于 $15/32$。因此整个 lift 上 $\Phi$ 单射。
这一步是全局单射证明，不只是在每个实角应用局部 inverse 定理。

$\widehat\Phi(\theta)=\theta+\widehat h(\theta)$ 在实线上实值。
在上、下边界，由 (Y.7)--(Y.8) 分别有
$$
 \Im\Phi(x+i\sigma/2)
  >\frac{31\sigma}{128}-\frac{21\rho}{4}>\frac{\sigma}{16},
$$
$$
 \Im\Phi(x-i\sigma/2)
  <-\frac{31\sigma}{128}+\frac{21\rho}{4}<-\frac{\sigma}{16}.
 \tag{Y.9}
$$
严格数值比较只用 (Y.1) 的有理数：
$23/1048576>63/4000000$。

周期商圆柱上的 argument principle 现在给
$$
                  S_{\sigma/16}\subset\Phi(S_{\sigma/2}).
 \tag{Y.10}
$$
具体地，使用同伦 $\Phi_t(z)=z+t h(z)$。
(Y.9) 使上下边界在整个同伦中不碰任何
$w\in S_{\sigma/16}$；周期度始终为1。
因此每个该 $w$ 的原像计重数为1，与全局单射一致。
也可将圆柱写成 $\zeta=e^{iz}$ 的环域，用
$\zeta\exp(i t h(z))$ 的同一边界同伦作该计数。

存在唯一全纯 inverse
$$
 \Theta=\Phi^{-1}:S_{\sigma/16}\longrightarrow S_{\sigma/2},
 \quad
 \Theta(\varphi+\pi/2)=\Theta(\varphi)+\pi/2,\quad
 |\Theta'|<32/15.
 \tag{Y.11}
$$
上述域和界对全径向区间及 (Y.3) 统一。
对于实 $W$，它就是实圆周上严格增的 degree-one inverse。

## 3. 完整 joint moving 读出

在 $\varphi$ 条带定义
$$
 u=(B/C)\circ\Theta,\qquad v=(1/C)\circ\Theta .
 \tag{Y.12}
$$
这里 $u,v$ 是原 moving 物理曲率变量，不是归一多项式的 $U,V$。
若需要后者，必须使用原准确
$U=u/\alpha,\ V=(v-s)/\alpha,\ s=C_{\rm ref}^{-1}$。

(Y.2)--(Y.3) 的 Banach 代数给
$$
 \frac BC=\frac{\widehat B/\widehat C+
                      (1/\widehat C)b}{1+(1/\widehat C)c},
 \qquad
 \frac1C=\frac{1/\widehat C}{1+(1/\widehat C)c},
$$
$$
 \|B/C\|_{\mathscr A_\sigma}
 <\frac{1/50+6\rho}{1-6\rho}<\frac1{32},\qquad
 \|1/C\|_{\mathscr A_\sigma}<\frac6{1-6\rho}<7.
 \tag{Y.13}
$$
因此在共同 inverse 条带 $S_{\sigma/16}=S_{2\tau}$，
完整复函数的 supremum 分别小于 $1/32$ 与7。
为了得到 joint Wiener norm，先对每个物理频率 $k=4j$ 用 Cauchy：
$$
 \sup_r|u_{4j}(r)|<(1/32)e^{-8\tau|j|},\qquad
 \sup_r|v_{4j}(r)|<7e^{-8\tau|j|}.
$$
再求和而不交换 $\sup$ 与 $\sum$，得到
$$
 \|u\|_{\mathscr A_\tau}+\|v\|_{\mathscr A_\tau}
 <(7+1/32)\left(1+\frac2{e^{4\tau}-1}\right)
 <\frac8\tau=2^{21}.
 \tag{Y.14}
$$
完整正负频率各计一次，常数项是括号中的1。
这里的条带损失是证明的一部分；没有声称 $\Theta$ 的任意
零宽组合在原 Wiener 或 Sobolev 空间同阶有界。

## 4. 原相位规范与两个 mean 的准确反演

记 $\ell=\pi/2$。对于复数据，将 $\varphi$ 的一个实周期经
$\Theta$ 映为 $\theta$ 条带中的曲线 $\Gamma$。
它的两端相差 $\ell$。所有下面的 integrand 都在
$S_{\sigma/2}$ 全纯且周期，因此 $\Gamma$ 可变形回任意实周期。

由 $\varphi=\Phi(\theta)=\theta+h(\theta)$ 和 $d\varphi=j\,d\theta$，
$$
 \begin{split}
 \langle\Theta(\varphi)-\varphi\rangle_\varphi
 &=-\frac1\ell\int_\Gamma h(\theta)(1+h_\theta(\theta))\,d\theta\\
 &=-\langle h\rangle_\theta
                  -\frac1{2\ell}\int_\Gamma\partial_\theta(h^2)\,d\theta=0 .
 \end{split}
 \tag{Y.15}
$$
这是原 moving 平均的准确零值，不是一个可以任意重选的相位常数。
同一换元给
$$
 m:=\langle v\rangle_\varphi=\frac1{c_0},\qquad
 \langle u\rangle_\varphi=\frac{\langle B\rangle_\theta}{c_0}.
 \tag{Y.16}
$$
两式使用有符号的复平均和完整 Jacobian。
没有以 mean-free 投影删掉一个曲率 mean。

由 (Y.11)--(Y.12)，
$$
 \Theta_\varphi=(c_0/C)\circ\Theta=v/m,\qquad
 \boxed{\quad
 \Theta(\varphi)=\varphi+I_\varphi(v/m-1).
 \quad}
 \tag{Y.17}
$$
最后的常数准确由 (Y.15) 固定。
所以 (Y.12) 恰好反演原
$\Psi(u,v)=(u/v,1/v)\circ\Theta^{-1}$，
包括其零 moving mean 的角规范。
反向从原规范的 $\Theta$ 开始，同一个积分恒等式说明
$\Theta^{-1}-{\rm id}$ 的物理平均也为0；不存在遗漏的整体角平移。

对于实际 X 的反射解，$C$ 偶、$B$ 奇，$h$ 与 $\Phi,\Theta$
的位移为奇，故 $v$ 偶、$u$ 奇。
于是 $\langle u\rangle_\varphi=0$，而
$m=1/c_0$ 仍是完整的非零输出。
这不把独立的 holonomy mean、高度 mean 或整体高度常数删去。

## 5. 实际参数依赖与一个有限高阶窗口

对任意全纯依赖参数的 (Y.3) pair，(Y.4)--(Y.8) 在同一域内全纯。
(Y.10)--(Y.11) 的统一域及非零导数给全纯 inverse 依赖。
逐 Fourier 系数 Cauchy 和 (Y.14) 的统一可求和支配说明，
读出在严格较小的 $\mathscr A_\tau$ joint 空间中也是
Banach 空间值全纯映射。
这一步不以逐点全纯直接代替强范数全纯。

应用于 X 的
$\|\gamma\|_{A_\sigma}<10^{-9}$、
$\|f_B\|_{\dot A^2_\sigma}<2^{-60}$ 复偶域，
得到实际 moving 曲率
$Q_{\gamma,f_B}=(u_{\gamma,f_B},v_{\gamma,f_B})$ 的全纯依赖。
实输入给实解。其两mean及相位始终由 (Y.15)--(Y.17) 决定。

为避免把解析条带读出误称为已付的高阶小球，明确写出可用值界。
设
$$
 \|Q\|_{\mathfrak M_q}
 =\left(\sum_k\langle k\rangle^{2q}\sup_I|u_k|^2\right)^{1/2}
 +\left(\sum_k\langle k\rangle^{2q}\sup_I|v_k|^2\right)^{1/2}.
$$
它控制每个径向截面的完整 $H^q\oplus_1H^q$ norm。
由 $(1+x)^q e^{-\tau x}\le2^q q!\tau^{-q}$ 和 (Y.14)，
$$
 \|Q_{\gamma,f_B}\|_{\mathfrak M_q}
 <2^{21+19q}q!
 \le2^{21+32q}\quad(0\le q\le8160).
 \tag{Y.18}
$$
$q=0$ 单独直接读 (Y.14)；$q\ge1$ 时 $q<8192=2^{13}$
给 $q!\le2^{13q}$。该界包括完整 mean 和全部正负频率。

同一完整参数球的 Cauchy 估计，在相应半球给
$$
 \|D_{f_B}Q\|_{\dot A^2_\sigma\to\mathfrak M_q}
 <2^{82+32q},\qquad
 \|D_\gamma Q\|_{A_\sigma\to\mathfrak M_q}<2^{52+32q}.
 \tag{Y.19}
$$
这些值和两导数对 $0\le q\le8160$ 都可宽取 $2^{262144}$。
$f_B$ 方向仍按归一高度计；物理高度方向须乘 $s_B^{-1}$。
这里的参数输入是已经声明的解析球，(Y.19) 不建立任意零宽
有限 Sobolev 方向的同阶算子界。

(Y.18) 是整个 $Q$ 的有限大界，并非
$Q-\widehat Q$ 落入 $2^{-8388608}$ 的原高 Sobolev 帽邻球。
它也不把大标签宽 $224$ 或 $s_\beta$ 授给当前 moving 解。

## 6. 原方程、真实内端及仍须匹配的量

实际 X 的 $W$ 解原固定 intrinsic 的 Gauss--Codazzi 方程。
(Y.12)、(Y.17) 是其原物理化的准确反演；
在真实 target 的相应径向正则区间，逆与径向导数按完整链式法则求取。
原连续中心篇的精确残差协变于是给同一 moving 方程的零残差。
这是对实际解的坐标读取，没有改变 $\eta_0,\alpha,\nu$ 或 gauge，
也没有把已知仿射 $Q_\delta$ 重新标成真解族。

在内端 $L=9/10$，当前 moving 数据及相位现在有明确、合法的读出；
$m(L)$ 来自真实 $C_0(L)$，原独立 $B(L)$ 也未预先与 body 相等。
它们仍须进入全体相应端列。帽右端实际长段高度图保持
[H 的物理角单位、两个 mean 与唯一整体高度](R133-supplement-small-positive-width-true-cap-to-long-height-readout.md)。

未知角的进一步方向导数或粗糙输入仍须使用
[完整 good tangent 与 weighted mean](R133-supplement-exact-unknown-outer-angle-good-tangent-and-full-means.md)
的准确公式及各自已付 norm；本条带引理不替代那些合同。

本文付清当前实际帽的非线性坐标读出与相位/两均值身份。
全负体、强返回、完整 cutoff 与 $\nu$ Schur、界面 lifting、
全部内端 height/flux/phase，以及闭合嵌入和几何尺度仍继续联立。
