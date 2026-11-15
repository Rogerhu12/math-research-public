# 原全六层权一形式的 Fermat 模型与对数平方微分

日期：2026-11-15。会话：serre-public-astra-20261115 / sigma_uniform。

**状态：下列实际函数、标记、尺度和 Cartier 恒等式已证明。原 primitive / Legendre 同标签非零仍开放。** 本文继续 [KS 权一平方笔记](2026-11-15-sigma-Kronecker-weight-one-square-and-critical-convolution.md)，不改变原 R683 的十八个点或字符。所有有限恒等式均在正文推导，无新数值执行。

## 1. period-one 与原物理微分严格分开

原 R683 的曲线及周期为
$$
E_0:y_0^2=x_0^3-1,\qquad dz=\frac{dx_0}{2y_0},\qquad
\Lambda=\Omega(\mathbf Z+\zeta\mathbf Z),\quad\Omega>0,
$$
$$
\alpha^3=4,\qquad\beta^2=3,\qquad
s=\zeta-\zeta^2,\quad s^2=-3,
$$
其中 $\alpha,\beta$ 取原正实嵌入，$s=i\sqrt3$。

在模参数 $\tau$ 上使用 **period-one** 曲线
$$
\Lambda_\tau=\mathbf Z+\tau\mathbf Z,\qquad
x_\tau(\xi)=\wp_{\Lambda_\tau}(\xi),\quad
y_\tau(\xi)=\wp'_{\Lambda_\tau}(\xi)/2,
$$
$$
y_\tau^2=x_\tau^3+a_\tau x_\tau+b_\tau,\qquad
d\xi=\frac{dx_\tau}{2y_\tau}.
\tag{XF1}
$$
在 $\tau_0=\zeta$，同一原几何点的两个坐标满足
$$
x_{\tau_0}(z/\Omega)=\Omega^2x_0(z),\qquad
y_{\tau_0}(z/\Omega)=\Omega^3y_0(z).
\tag{XF2}
$$
下文没有在 (XF1) 的公式中把 $\Omega$ 设为一。

沿原全六层标记，令 $P_i=P+iQ$、$i=0,1,2$ 是原三个三挠点，
$T_j$、$j=0,1,2$ 是原三个非零二挠点。在原物理 CM 纤维：
$$
P_i=(\alpha\zeta^i,\beta),\qquad Q=(0,-i),\qquad
T_j=(\zeta^j,0).
\tag{XF3}
$$
这里 (XF3) 的 $i$ 在 $Q$ 坐标中是复数单位；在下标中是 $0,1,2$。
直接群律给 $P_{i+1}=P_i+Q$，所以这确实固定了三挠标记的方向。

对一个固定 torsion 标记 $R=a+b\tau$，写
$$
e_\tau(R)=\zeta_{\Lambda_\tau}(R)-a\eta_1-b\eta_\tau.
$$
这是在 torsion 截面上的全纯权一函数。Legendre 准周期关系给
$$
e_\tau(a+b\tau)
=\frac{\vartheta'(a+b\tau;\tau)}
       {\vartheta(a+b\tau;\tau)}+2\pi i b.
\tag{XF4}
$$
故 KS 中实际的 period-one 权一形式是
$$
E(\tau)=
\sum_{\delta=\pm1}\sum_{i,j=0}^2
       \delta\zeta^{j-i}e_\tau(\delta P_i+T_j).
\tag{XF5}
$$
在原物理纤维，$E(\tau_0)$ 是相同 completed-zeta 和的 $\Omega$ 倍；
其值虽然为零，后面的相位判定不使用这个零值。

## 2. 从原三挠直线构造两个权一坐标

因为 $P_0+P_1+P_2=O$，三个 $P_i$ 位于同一条直线
$$
y=\mu x+\nu.
$$
所有坐标在本节均为 (XF1) 的 period-one 坐标。
其横坐标是
$$
x^3-\mu^2x^2+(a_\tau-2\mu\nu)x+(b_\tau-\nu^2)=0
$$
的三个根。这个三次式整除
$\psi_3/3=x^4+2a_\tau x^2+4b_\tau x-a_\tau^2/3$。
比较系数即得
$$
a_\tau=-2\mu\nu-\mu^4,\qquad
b_\tau=-\frac{\nu^2+4\mu^3\nu+\mu^6}{3}.
\tag{XF6}
$$

令
$$
A_1=\sum_i\zeta^{-i}x(P_i),\qquad
A_2=\sum_i\zeta^i x(P_i).
$$
三次根的 resolvent 给
$$
A_1A_2=4\mu(\mu^3+3\nu),\qquad
\{A_1^3,A_2^3\}
=\{4(\mu^3+3\nu)^2,\,16\mu^3(\mu^3+3\nu)\}.
$$
原 CM 标记给 $A_1=3\alpha\Omega^2\ne0$、$A_2=0$，
所以在连通的同一全三层分支上，第一项对应 $A_1^3$。
定义实际权一函数
$$
\rho=\frac{2(\mu^3+3\nu)}{A_1}.
$$
于是
$$
\rho^2=A_1,\qquad
\rho^3=2(\mu^3+3\nu),\qquad A_2=2\mu\rho.
\tag{XF7}
$$
这也解释 $\rho$ 的符号：它由原 $P_i$ 的有向标记给出，不是事后
任取的平方根。其余点由有理延拓解释。在 CM 纤维，
$$
\mu(\tau_0)=0,\quad
\nu(\tau_0)=\Omega^3\beta,\quad
\boxed{\rho(\tau_0)=\Omega\,\frac{2\beta}{\alpha}>0,\qquad
\rho(\tau_0)^2=3\alpha\Omega^2.}
\tag{XF8}
$$

将 $\nu=(\rho^3-2\mu^3)/6$ 代入 (XF6)：
$$
a_\tau=-\frac{\mu(\rho^3+\mu^3)}3,\qquad
b_\tau=-\frac{\rho^6+20\mu^3\rho^3-8\mu^6}{108}.
\tag{XF9}
$$
全部三个点的实际坐标为
$$
x(P_i)=\frac{\mu^2+\rho^2\zeta^i+2\mu\rho\zeta^{-i}}3,
$$
$$
y(P_i)=\frac{\rho^3+2\mu\rho^2\zeta^i
                   +4\mu^2\rho\zeta^{-i}}6.
\tag{XF10}
$$
此外
$$
Q=\left(-\mu^2,\frac{\rho^3-8\mu^3}{6s}\right).
\tag{XF11}
$$
式 (XF10)--(XF11) 可直接验证三挠及加法。
例如在 $\rho=1$ 的标架，$P_0$ 到 $Q$ 的斜率为
$(s-1+2\mu)/(2s)$，代回群律即给出 $P_1$ 的横坐标；
纵坐标及 $P_2=P_0-Q$ 同样确定。因此后续模曲线确实携带原标记。

## 3. 一个带实际标记的 $X(6)$ 模型

写 $e_j=x(T_j)$ 并作原有序二挠点的 resolvent：
$$
r=\sum_j\zeta^je_j,\qquad t=\sum_j\zeta^{-j}e_j .
$$
因为 $\sum e_j=0$，
$$
e_j=\frac{r\zeta^{-j}+t\zeta^j}{3},\qquad
rt=-3a_\tau,\qquad r^3+t^3=-27b_\tau.
\tag{XF12}
$$
置三个权零函数
$$
U=\mu/\rho,\qquad R=r/\rho^2,\qquad T=t/\rho^2.
$$
由 (XF9)、(XF12)：
$$
\boxed{
RT=U(1+U^3),\qquad
4(R^3+T^3)=1+20U^3-8U^6.
}
\tag{XF13}
$$
在原标记 CM 点，
$$
(U,R,T)=(0,0,\alpha^{-1}).
\tag{XF14}
$$

为明确这里是实际模曲线，先把 $\rho$ 归一为一。
(XF9)--(XF11) 给出 $\mathbf P^1_U$ 上实际的全三层椭圆曲线；
其 $j$ 映射为
$$
j=-110592\,\frac{U^3(1+U^3)^3}{(1-8U^3)^3},
\tag{XF15}
$$
次数为十二，等于 $X(3)\to X(1)$ 的次数。因此 $U$ 是这一个
原全三层标记分支的参数。再加入有序三个非零二挠点，就是全六层；
(XF12) 可双向恢复它们，所以 (XF13) 的规范化是该 $X(6)$，
没有只凭 genus 相同来认定对象。

现在置
$$
D_0=1-8U^3,\qquad W=\frac{4(R^3-T^3)}{D_0}.
$$
由 (XF13) 直接相减平方：
$$
W^2=D_0.
$$
在开集上定义
$$
\mathsf x=\frac{4R}{3-W},\qquad
\mathsf y=\frac{4T}{3+W}.
\tag{XF16}
$$
有限因式分解给
$$
R^3=\frac{(3-W)^3(1+W)}{64},\qquad
T^3=\frac{(3+W)^3(1-W)}{64}.
$$
因此
$$
\boxed{
\mathsf x^3+\mathsf y^3=2,\quad
U=\frac{\mathsf x\mathsf y}{2},\quad
W=\mathsf x^3-1=1-\mathsf y^3,
}
\tag{XF17}
$$
$$
R=\frac{(3-W)\mathsf x}{4},\qquad
T=\frac{(3+W)\mathsf y}{4}.
$$
这些互逆有理式证明 (XF13) 的规范化就是平滑 Fermat cubic
$\mathsf x^3+\mathsf y^3=2$。原 CM 点为
$$
(\mathsf x,\mathsf y,W)=(0,2/\alpha,-1).
\tag{XF18}
$$
它在所有 $p\ge5$ 的相同良约化图上成立。

如需 Weierstrass 模型，明确取
$$
X_6=-\frac2{\mathsf x+\mathsf y},\qquad
Y_6=s\,\frac{\mathsf x-\mathsf y}{\mathsf x+\mathsf y}.
$$
则
$$
Y_6^2=X_6^3+1,\qquad
(X_6,Y_6)_{\rm CM}=(-\alpha,-s).
\tag{XF19}
$$
这给出与 Kaneko--Kuwata 的 genus-one Weierstrass 型相同的实际
有标记模型；没有声称它的坐标已等于该文用另一个 cusp 选定的
eta-quotient 坐标。标记由 (XF3)、(XF10)--(XF14) 固定，
而不是由一个未指定的 $j=0$ 同构固定。

## 4. 原十八项恰是一个 Fermat 坐标

因为 $e_\tau(-P)=-e_\tau(P)$、$e_\tau(T_j)=0$，
以及真正的 zeta 加法，
$$
e_\tau(P_i+T_j)=e_\tau(P_i)+
                    \frac{y(P_i)}{x(P_i)-e_j}.
$$
将其代入 (XF5)，$\sum_j\zeta^j=0$ 删去的仅是实际 $e_\tau(P_i)$ 项：
$$
E=2\sum_{i,j}\zeta^{j-i}\frac{y(P_i)}{x(P_i)-e_j}.
\tag{XF20}
$$
式 (XF12) 又给
$$
\sum_j\frac{\zeta^j}{x-e_j}
       =\frac{rx+t^2/3}{x^3+a_\tau x+b_\tau}.
$$
而 (XF10) 有准确的逆式
$$
\frac1{y(P_i)}
 =\frac{6(\rho-2\mu\zeta^i)}
        {\rho(\rho^3-8\mu^3)}.
$$
于是逐项求三个根之和，得
$$
\sum_i\frac{\zeta^{-i}}{y(P_i)}
 =-\frac{36\mu}{\rho(\rho^3-8\mu^3)},\qquad
\sum_i\frac{\zeta^{-i}x(P_i)}{y(P_i)}
 =\frac{6(\rho^3-2\mu^3)}{\rho(\rho^3-8\mu^3)}.
$$
因此
$$
\frac E\rho
=\frac{12\{R(1-2U^3)-2UT^2\}}{1-8U^3}.
\tag{XF21}
$$
最后使用 (XF17)：
$$
R(1-2U^3)-2UT^2
=\frac{\mathsf x}{16}
 \bigl((3-W)(3+W^2)-(1-W)(3+W)^2\bigr)
=\frac{\mathsf xW^2}{2}.
$$
故获得完整原函数恒等式
$$
\boxed{E(\tau)=6\,\rho(\tau)\,\mathsf x(\tau).}
\tag{XF22}
$$
所有常数和原字符都已在 (XF20) 保留。
在 $\tau_0$，这是 $\Omega$ 倍的物理 completed-zeta 和；
右侧的 $\rho(\tau_0)$ 也含同一 $\Omega$，见 (XF8)。

## 5. eta 相位由非零量固定

令 $q=e^{2\pi i\tau}$，Dedekind $\eta$ 取其标准 $q^{1/24}$ 分支。
由 (XF9)，period-one Weierstrass 判别式准确为
$$
\Delta_{\rm alg}=-16(4a_\tau^3+27b_\tau^2)
=-\frac{\rho^{12}(1-8U^3)^3}{27}
=(2\pi)^{12}\eta^{24}.
\tag{XF23}
$$
所以对全六层的权零函数
$$
V=\frac{(2\pi)^2\eta^4}{\rho^2}
$$
有 $V^6=-W^6/27$。比值 $V/W$ 是这个连通曲线上的常数。

在原 $\tau_0=\zeta$，$\rho^2=3\alpha\Omega^2>0$。
此外 $q=-e^{-\pi\sqrt3}$，无限乘积 $\prod_{n\ge1}(1-q^n)$
是正实数，因此 $\eta^4$ 的相位准确为 $e^{-\pi i/6}$。
结合 $W=-1$、$|V|=1/\sqrt3$，这唯一固定
$$
\boxed{
V=\frac{\zeta-1}{3}W,\qquad
\frac{(2\pi)^2\eta^4}{\rho^2}
       =\frac{\zeta-1}{3}(\mathsf x^3-1).
}
\tag{XF24}
$$
这个相位论证使用非零的 $\eta^4,\rho^2,W$，不使用 $E(\tau_0)=0$
来确定一个本来不可由零值确定的符号。

把有代数 Fourier 系数的归一写作
$\mathcal E=E/(2\pi i)$。由 (XF22)--(XF24)：
$$
\boxed{
\frac{\mathcal E^2}{\eta^4}
=\frac{108}{1-\zeta}\,
        \frac{\mathsf x^2}{\mathsf x^3-1}.
}
\tag{XF25}
$$
这是在带原六层标记的 $X(6)$ 上的明确有理函数。
它在原 CM 点有二阶零；分母在该点是单位。
这不是对高 Taylor 系数的单位断言。

## 6. 实际平方微分是显式对数微分

还可固定微分常数。置
$\widehat\mu=\mu/(2\pi i)$、$\widehat\rho=\rho/(2\pi i)$。
由标准 $a_\tau=-\pi^4E_4/3$、$b_\tau=-2\pi^6E_6/27$，
归一的 $a_\tau/(2\pi i)^4,b_\tau/(2\pi i)^6$ 分别为
$-E_4/48,E_6/864$。

令 $\partial_k=\theta_q-kE_2/12$ 为 Serre 导子。
Ramanujan 方程给归一的 $\partial a=6b$、$\partial b=-4a^2/3$。
将 (XF9) 代入，可直接核得
$$
\partial_1\widehat\mu
=\frac{\widehat\rho^3-2\widehat\mu^3}{6},\qquad
\partial_1\widehat\rho=\widehat\mu^2\widehat\rho.
\tag{XF26}
$$
两式的验证只需分别对 (XF9) 求导；对应 Jacobian 在一般点非零，
故它们由实际 $a,b$ 的导子唯一决定，并以有理恒等式延拓。
因此
$$
\theta_q U=\frac{\widehat\rho^2(1-8U^3)}6.
\tag{XF27}
$$

在 Fermat 曲线上令
$$
\omega_{\rm F}=\frac{d\mathsf x}{\mathsf y^2}.
$$
(XF17) 给 $dU=-W\omega_{\rm F}$。
用 (XF22)、(XF27) 约去全部 period-one 因子，得到
$$
\boxed{
\mathcal E(\tau)^2\frac{dq}{q}
=-216\,\frac{\mathsf x^2}{W}\omega_{\rm F}
=-216\,\frac{d\mathsf y}{\mathsf y^3-1}
=-72\sum_{a\in\mu_3}a\,d\log(\mathsf y-a).
}
\tag{XF28}
$$
中间一步只用 $d\mathsf y=-\mathsf x^2d\mathsf x/\mathsf y^2$。
因此没有留下待选的 holomorphic correction。

九个有限极点是 $\mathsf x^3=\mathsf y^3=1$，即这个标记模型的
九个有限 cusp；另三个 cusp 在 Fermat cubic 的无穷远处，
(XF28) 在那里正则。所有有限极点均为简单极点，留数在
$\mathbf Z[1/6,\zeta]$ 中。它们的实际位置和留数由 (XF28) 给出，
不是只用“torsion cusp”这个名称来代替计算。

作为一个直接后果，在每个 $p\ge5$、$p\equiv2\pmod3$ 的良约化上，
取含 $\zeta$ 的完美系数字段，令
$$
\alpha_0=\frac{d\mathsf y}{\mathsf y^3-1},\qquad
\alpha_1=\frac{\mathsf y\,d\mathsf y}{\mathsf y^3-1}.
$$
Cartier 的半线性与 $\mathcal C(d\log g)=d\log g$ 给
$$
\boxed{\mathcal C(\alpha_0)=\alpha_1,\qquad
       \mathcal C(\alpha_1)=\alpha_0.}
\tag{XF29}
$$
具体地，$a^{1/p}=a^{-1}$ 把 (XF28) 的 $a$ 与 $a^2$ 交换。
这是这个实际标量平方微分的二阶 Cartier 模，不是原临界
primitive 分量已经非零。


还有一个原尺度核对。由 (XF17)、(XF21) 在 CM 点得
$d\mathsf x/dU=\alpha$；(XF22)、(XF27) 因而给
$$
\delta_1E(\tau_0)=\frac{\alpha\rho(\tau_0)^3}{(2\pi i)^2}.
$$
代回 KS 的原定义，使用 $\rho(\tau_0)^3=6\beta\Omega^3$ 与
$C_+=144\beta/\alpha^2$，恰得
$C_2=-3\alpha\rho(\tau_0)^3/(\Omega^3C_+)=-1/2$。
这是与已成 R683 首系数的符号核对，不是新的数值测试。

## 7. 与临界源、Cayley 因子及原筛的精确关系

KS 已证明，保持原 $\mathcal A=\Omega^2\Im\zeta/\pi$，
对 Cayley 参数
$$
u=\frac{\tau-\tau_0}{\tau-\overline{\tau_0}}
$$
有完整原系数式
$$
\boxed{
\frac{(1-u)^{-1}E(\tau(u))}{\Omega C_+}
=\sum_{m\ge0}C_{m+1}
         \left(-\frac{\mathcal A u}{3}\right)^m.
}
\tag{XF30}
$$
只有 $m\equiv1\pmod3$ 的项非零。
(XF22)、(XF28) 因而识别了这个实际 test vector 的全局模形式，
并不把其 Taylor 参数改为 $\mathsf x$ 或 $\mathsf y$。

临界卷积仍需 KS 的
$[u^{p-1}](u^5E^2d\tau/du)$。式 (XF29) 控制的是未乘 $u^5$ 的
实际微分；Cartier 只允许把 $p$ 次幂因子提出，不能把 $u^5$
当作常数或 $p$ 次幂提出。$u$ 不是 $X(6)$ 的有理函数。
若用 Gauss--Manin 表示，$u$ 是两个指定水平 covector 与 Hodge
向量的配对之比；五次分子属于 $\operatorname{Sym}^5$，
但对应的五次分母标架也必须保留。本文没有以一个未经证明的
六维标量闭包消去这个标架。

更具体地，取两个独立的 (XF30) 参数，保留双变量乘积。
对 $p=6N+5$，原 $h=6i+7$ 对应
$$
m_1=h-3=6i+4,\qquad m_2=p-h-3,\qquad m_1+m_2=p-6.
$$
由原 R697 / KS，准确有
$$
C_{h-2}C_{p-h-2}
=-\frac{96}{Q_h}f_i^2g_{N-1-i}^2\pmod p,\qquad
Q_h=(h-2)(h-1)h(h+1)(h+2).
\tag{XF31}
$$
所有 $Q_h$ 是单位。因此 R770 的临界三因子目标等价于下列有不同单项式的
双变量向量不为零：
$$
\sum_{\substack{0\le i<N\\(h,p+1)=1}}
 Q_h\,P_{h-1}(1/s)^2\,
 C_{h-2}C_{p-h-2}\,
 t_1^{h-3}t_2^{p-h-3}\ne0.
\tag{XF32}
$$
它是 $-96$ 乘原 $P_{h-1}(1/s)^2f_i^2g_{N-1-i}^2$ 的向量。
让两个参数相等只留下一个可能相消的总和，并丢失原标签，
所以 (XF25) 的单个有理函数本身不能替代 (XF32)。

也不能把 (XF28) 未经比较就认成 R833 / R834 的指定源。
后者来自 R812 的线性产品
$\sum(-1)^j f_{N-1-j}g_j$ 及其原八个 Gaussian companion theta；
本篇 (XF31) 是 $C$ 的二次、即原 sigma 系数的四次表达。
目前没有把这两个指定 test vector 识别的已证线性同构。
本篇新增的是原对象的明确几何函数和准确标量 Cartier 作用；
原 $u^5$ 连接及 (XF32) 的 primitive / Legendre 投影非零仍须证明。

## 来源

- [KS 笔记](2026-11-15-sigma-Kronecker-weight-one-square-and-critical-convolution.md)：
  原 mixed-heat / Gaussian / Maaß 恒等及 (KS15) 的 $-192/Q_h$。
- [R683](../results/R683-even-weight-Cartier-channel-and-actual-r3.md)、
  [R697](../results/R697-original-sigma-six-sections-and-integral-square-roots.md)、
  [R770](../results/R770-same-primitive-label-square-and-finite-bilinear-pairing.md)：
  同一十八项、原 sigma 平方与真实同标签指标。
- Kaneko--Kuwata, *Elliptic normal curves of even degree and theta functions*,
  §8, https://www2.math.kyushu-u.ac.jp/~mkaneko/papers/KKtheta.pdf ：
  全六层 genus-one 模型的原文对照。正文以实际 torsion 标记和互逆
  有理式独立证明这里的模型，没有借用一个未定的标架。
- 标准 Weierstrass 群律、三除多项式、Ramanujan 方程与
  $\Delta_{\rm alg}=(2\pi)^{12}\eta^{24}$；
  本篇涉及的有限代数恒等式及全部常数都已在正文核算。
