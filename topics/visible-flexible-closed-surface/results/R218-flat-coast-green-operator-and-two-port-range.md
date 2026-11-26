# R218：准确平坦 ruling 带的全角耦合 Green 算子与双端值域

2026-11-26，Astra-visible-flex-6a65e705-20261126 / g5-and-exact。

**状态：以下条件引理已证明。** 它给准确平坦参考上的完整法向兼容方程、
保留全角耦合的 Green 算子、双端源矩和定量界。
它不把当前近似 M12 的第二形式当成准确秩一数据，
不把法向兼容误作完整等距边值问题可解，
也不以仅有 $10^{-10}$ 的 C⁰ 残差上界代替所需高阶输入。

## 1. 准确局部对象及全局 ruling 条带

设 $A$ 是一个材料环带，$X:A\to\mathbb R^3$ 为**准确**
$X^*e=g$、$K_g=0$ 的浸入，选择全局单位法向 $n$，约定
$II_{ij}=\langle X_{ij},n\rangle$。
本节在光滑内部采用经典微分；R137 的准确 ruling supplier 可在其光滑内部使用它。
C² 接口及只具有弱导数的源另按 §7 处理，
不向本题增加全曲面必须 C³ 或 C⁴ 的要求。

假设 $II$ 处处秩一，其非零主曲率为
$\lambda=\operatorname{tr}_gII$，并已有**实际参考**的界

$$
|\lambda|\ge\lambda_*>0.
$$

写 $II=\lambda\,\eta^\flat\otimes\eta^\flat$，其中 $\eta$ 为单位特征方向。
取单位零曲率方向 $T\perp\eta$，方向选择从左端指向右端。
还须有完整材料流坐标

$$
\mathcal F:\{(\theta,\tau):\theta\in\mathbb R/P\mathbb Z,\ 
0\le\tau\le L(\theta)\}\longrightarrow A,\qquad
\partial_\tau\mathcal F=T,                         \tag{1}
$$

其为环带的微分同胚，$0<L(\theta)\le L_*$，
左右边界对应 $\tau=0,L(\theta)$。
所有数据和流坐标按 $\theta$ 的真实材料周期匹配。
(1) 排除 ruling 回返、未覆盖分支、域内相交或端口处切触；
仅有 $K=0$ 并不能代付这一全局入口。

### 仿射半径坐标中可实际核对的充分条件

若 $g=ds^2+f(s)^2du^2$，$f>0,\ f''=0$，并在其正交标架中写

$$
II=\begin{pmatrix}\ell&m\\m&\nu\end{pmatrix},
$$

这里 $\nu$ 是角向分量，**不等同于**上面的非零特征值 $\lambda$。
若 $\nu\ne0$，准确 Gauss 方程给 $\ell=m^2/\nu$。
令 $\beta=m/\nu$，则

$$
T=\frac{\partial_s-(\beta/f)\partial_u}{\sqrt{1+\beta^2}},
\qquad
\lambda=\nu(1+\beta^2).                            \tag{2}
$$

若 $\beta$ 是整个闭材料环带上的 C¹ 周期函数且 $|\beta|\le B_*$，
ODE $du/ds=-\beta(s,u)/f(s)$ 在圆周上给每层的全局微分同胚。
其 $s$ 分量严格向右，所以确实给 (1)，且

$$
L_*\le(b-a)\sqrt{1+B_*^2}.                         \tag{3}
$$

必须使用准确 supplier 的 $II$、真实材料角和端口；
不能将 native 数值角或一个径向背景的比值替代 $\beta(s,u)$。

## 2. 完整曲率线性化与符号

对对称二张量 $B$，定义平坦目标的线性化 Gaussian 曲率

$$
\mathcal C_g(B)=\frac12\{\operatorname{div}_g\operatorname{div}_gB
-\Delta_g\operatorname{tr}_gB\}.                  \tag{4}
$$

这是 Gaussian 曲率，不是 scalar curvature 的两倍。
由
$\delta\Gamma^k_{ij}=
(\nabla_iB_j{}^k+\nabla_jB_i{}^k-\nabla^kB_{ij})/2$
微分曲率再收缩，得到一般公式
$\delta K=(\operatorname{div}\operatorname{div}B-\Delta\operatorname{tr}B
-K\operatorname{tr}B)/2$；
本节 $K=0$ 正好给 (4)。

切向变分 $v$ 的度量变化为 $\mathcal L_vg$，法向变分 $wn$ 为
$-2wII$。由于 pullback 保持准确零曲率，

$$
\mathcal C_g(\mathcal L_vg)=0.                    \tag{5}
$$

准确 Euclidean immersion 的 Codazzi 方程给

$$
\operatorname{div}II=\nabla H,\qquad H=\operatorname{tr}II,
\quad
\operatorname{div}(\operatorname{cof}_gII)=0,
\quad \operatorname{cof}_gII=Hg-II.
$$

于是直接展开得到关键符号恒等式

$$
\begin{aligned}
\mathcal C_g(-2wII)
&=\Delta(wH)-\operatorname{div}\operatorname{div}(wII)\\
&=H\Delta w-II:\nabla^2w\\
&=(\operatorname{cof}_gII):\nabla^2w.              \tag{6}
\end{aligned}
$$

两项 $\nabla H\cdot\nabla w$ 以及
$w[\Delta H-\operatorname{div}\operatorname{div}II]$ 准确抵消。
因此完整线性等距修复

$$
B+\mathcal L_vg-2wII=0
$$

必定满足

$$
(\operatorname{cof}_gII):\nabla^2w=-\mathcal C_g(B). \tag{7}
$$

没有删掉角依赖系数，亦没有以某个有限 Fourier 主对角项代替该算子。

在 §1 的 $s,u$ 坐标中，左边的完整表达为

$$
\nu w_{ss}
-\frac{2m}{f}(w_{su}-qw_u)
+\ell\left(\frac{w_{uu}}{f^2}+qw_s\right),
\qquad q=f'/f.                                   \tag{8}
$$

式 (8) 的 $\ell,m,\nu$ 可任意依赖角度；
Fourier 化时它们与 $w$ 的导数必须保留全部卷积。
它是 R213 法向兼容思路在准确 $K=0$ 情形的几何形式，
而不是另作一个径向对角模型。

## 3. 单位 ruling 确实为 geodesic

由准确秩一结构，

$$
\operatorname{cof}II=\lambda\,T^\flat\otimes T^\flat.
$$

还须证明 $\nabla_TT=0$，才能把 Hessian 写成普通二阶流导数。
对 Codazzi 取

$$
(\nabla_TII)(\eta,T)=(\nabla_\etaII)(T,T).
$$

右边为零，因为 $II(T,\cdot)=0$；
左边为 $-\lambda\langle\eta,\nabla_TT\rangle$。
$\lambda\ne0$ 给其为零，且单位 $T$ 有
$\langle T,\nabla_TT\rangle=0$，故 $\nabla_TT=0$。
因此

$$
(\operatorname{cof}II):\nabla^2w=\lambda\,T(Tw).
$$

在真实流坐标 (1) 中，(7) 准确化为

$$
\partial_\tau^2\widetilde w(\theta,\tau)=
F(\theta,\tau),\quad
F:=-\frac{\mathcal C_g(B)}{\lambda}\circ\mathcal F,
\quad
\widetilde w=w\circ\mathcal F.                   \tag{9}
$$

这不是忽略耦合：系数、曲率源、流线及两端位置仍随整个 $\theta$ 函数变化。
角耦合由真实 ruling 流保留。

## 4. 单端逆、输出端迹与双端两个源矩

给定左端输入
$\widetilde w(\theta,0)=a(\theta)$、
$\partial_\tau\widetilde w(\theta,0)=b(\theta)$，唯一解为

$$
\boxed{\widetilde w(\theta,\tau)=
a(\theta)+\tau b(\theta)+
\int_0^\tau(\tau-r)F(\theta,r)\,dr.}              \tag{10}
$$

直接两次微分验证 (9)，初值也准确成立；差的二阶导为零而两初值为零，
所以唯一。

定义完整输出函数

$$
M_0(\theta)=\int_0^{L(\theta)}F(\theta,r)\,dr,\qquad
M_1(\theta)=\int_0^{L(\theta)}(L(\theta)-r)F(\theta,r)\,dr.
$$

则右端精确输出是

$$
\widetilde w_{\rm right}=a+Lb+M_1,\qquad
(\partial_\tau\widetilde w)_{\rm right}=b+M_0.     \tag{11}
$$

因此左端输入为零且右端也要求零时，准确必要充分条件为

$$
\boxed{M_0(\theta)=M_1(\theta)=0
\quad\text{对全部材料 }\theta.}                 \tag{12}
$$

这两项是**两个完整的周期函数条件**，
不是总共两个标量，更不是选中 48 个测试槽为零就自动成立。
如果右端自由，(11) 正是要交给相邻非平坦块或其它准确 provider 的源端迹；
不能把它们静默设为零。

### 开领条件及所有 normal 两 jets

为在左右**开领**保持 $w=0$，须假定 $F=0$ 在相应开领。
若整个误差张量 $B$ 在这些开领恒零，这是充分条件。
左开领的 $a=b=0$ 使 $w$ 恒零。
右开领中 $F=0$ 使 $w$ 沿每条 ruling 为仿射函数，
再由 (12) 得其在右开领恒零。
所以只要已具备 C² 正则性，左右开领的全部 normal 0–2 jets 都准确为零，
包括角向和混合 jets，而不只是两个截面的值。

只要求两个截面 $w=0$ 不够；不要求 $F=0$ 的开领时，
(12) 也不能推出开领恒零。
若最终完整位置字段在开领恒零，原完整修复方程还强制 $B=0$ 在那里；
仅 $\mathcal C_g(B)=0$ 不够。

## 5. 定量范围与导数损失

对左端零输入，由 (10) 直接有

$$
\|w\|_\infty\le\frac{L_*^2}{2\lambda_*}
\|\mathcal C_g(B)\|_\infty,\qquad
\|Tw\|_\infty\le\frac{L_*}{\lambda_*}
\|\mathcal C_g(B)\|_\infty,
$$
$$
\|T(Tw)\|_\infty\le\frac1{\lambda_*}
\|\mathcal C_g(B)\|_\infty.                       \tag{13}
$$

对非零初值，前两界分别加
$\|a\|_\infty+L_*\|b\|_\infty$ 和 $\|b\|_\infty$。
这些常数明确使用实际域长度、实际非零主曲率下界，
可由 R137 supplier 的真实数据支付。

若需要横向 C² 界，就必须再控制
$\mathcal F,L,\lambda$ 的横向导数及 $F$ 的两阶横向导数。
例如在流坐标中对 (10) 的固定 $\tau$ 两次 $\theta$ 微分，
得到同样核对 $\partial_\theta^jF$ 的积分，$j=0,1,2$；
换回材料坐标还乘入真实流及逆流的导数。
在 (11) 的右端沿 $\theta$ 微分则要保留 $L'、L''$ 的 Leibniz 项。

由于 (4) 对 $B$ 有两个导数，
一个 $B$ 的 C⁰ 小数值界既不控制 (13)，
也不控制横向 C² 输出。平坦带的退化算子沿 ruling 积分，
不能凭此获得不损角阶数的椭圆估计。
在逐角模模型中这个损失会表现为 $k^2$；
式 (9)–(13) 保留的是不截模、全角耦合版本。

## 6. 法向兼容的值域不是完整等距值域

即使 (12) 准确成立，完整问题仍须解

$$
\mathcal L_vg=2wII-B                              \tag{14}
$$

并支付材料圆周周期、全局 holonomy、两个开领的实际切向条件，
以及允许的 Killing/gauge 核。
(7) 只说明 (14) 的局部曲率兼容；在环带上不能跳过这些全局条件。

一个准确反例显示双端 normal 源矩不足以固定全部端口：
取平圆柱 $g=ds^2+r^2du^2$，令
$B=e(s)\,ds^2$，其中 $e$ 紧支撑且 $\int_a^b e(s)\,ds\ne0$。
此时 $\mathcal C_g(B)=0$，故 $F=0$，两个函数矩都为零，
且 normal 解为 $w=0$。
但 (14) 的径向式强制 $2\partial_sv^s=-e$，
两端同时 $v^s=0$ 不可能。
这个反例也在开领有完整 $B=0$，并非靠违反开领假设造成失败。

另如平圆柱上的常数非零角向应变，局部曲率兼容为零，
但周期角位移的导数不可能有非零角平均；
这说明不能把局部平面上的势函数存在直接当作材料环带上的周期字段存在。

即使完整线性问题已解，非线性准确 metric 还含
$\langle dW,dW\rangle$，并且迭代后参考算子和端迹都会改变。
本文既未给全部邻近候选的保端口全空间右逆，
也未证明 Newton/Nash–Moser 的收敛小球。

## 7. 对当前两条实际线的使用范围

1. 对当前新 R137 准确 coast supplier：
   先核真实 $n\ne0$、ruling Jacobian、材料周期及流域，
   再从实际 II 得 $\lambda_*,B_*,L_*$，可以准确使用本引理；
   左端输入和右端 (11) 都作为完整函数端口传递。
   开平接头只有在源开领为零、normal 两矩和完整切向匹配均支付后才能保留。
2. 对 R21/R114 的近似 M12：
   实际 $h=X^*e\ne g$，准确切向线性化为 $\mathcal L_vh$，
   其 II 不可假定相对目标 $g$ 准确秩一或满足目标 Codazzi。
   不能将近似 II 直接代入 (9) 就宣称求得原问题右逆。
   当前多径向弱应力和真实 Cartesian 复合仍仅生成、检验有限方向。
3. 对只有全局 C² 的图：
   单位法向通常只有 C¹。
   若使用 $wn$，须支撑在真实光滑片并消掉片边界两 jets，
   或用实际 C² Cartesian 位移实现。仅弱源 $F\in L^\infty$
   给 ruling 方向的弱二阶解，不自动给全局 C² 位移。
   现有分片表示的接口须单独按实际两 jets 处理。

本引理不同于 R77 的径向周期—桥—真尾反馈表：
它只在准确平坦 ruling 块上给显式全耦合普通源解和准确端口输出，
不会代付非平坦块、annulus 切向 holonomy 或全图的全频反馈逆。

来源为本题 [R213](R213-tangential-compatibility-and-normal-correction.md)、
[R137](R137-flat-coast-ruling-two-jets-and-actual-inlet-consumer.md)、
[R77](R77-actual-support-robin-bridge-port-transfer.md)；
新恒等式、Green 公式、值域条件及估计均在上文直接证明。

