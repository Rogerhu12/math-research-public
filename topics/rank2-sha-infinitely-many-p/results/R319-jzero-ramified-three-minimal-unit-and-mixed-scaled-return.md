# R319：原范数三同源、最小单位返回与混合缩放的完整有限输入

日期：2026-11-13。**状态：原 $\delta=\sqrt{-3}$ 同源的全部 theta 因子、最小次数二单位乘子、完整二次返回空间及 $2^a\delta^b$ 的统一返回次数已证明。同一 $q^2$ 目标中的尺度进位和原完整中央等式全部保留；没有把缩放条件的数量当成独立 Smith 深度。**

## 1. 原三来源及两个线性单位

采用 R309 的同一固定 $b=17$、$t=-b/x^3$，
$$
X=7bH_1,\qquad Y=H_3,\qquad Z=H_5,\qquad
(X,Y,Z)=\rho(a(t),B(t),C(t)),
$$
其中
$$
\begin{aligned}
\rho&=\Theta^{17}(1+8t),\qquad \Theta=x\sigma^2,\\
a&=16t^4-12t^3+3t^2-7t,\\
B&=256t^4+1472t^3-1200t^2+200t+1,\\
C&=-128t^4-832t^3+1968t^2-280t+1.
\end{aligned}                                                    \tag{1}
$$
$\mathcal A_m$ 是 $X,Y,Z$ 的**原齐次次数 $m$** 部分，
而其归一化在 $\rho^mR[t]_{\le4m}$ 中。这里
$R=\mathbf Z[1/(42b)]$；本文的所有新有限代表只有二、三处分母。

置
$$
g_2=8t^2+20t-1,\qquad d=t(t-1)g_2^2,
$$
以及两个真实线性来源
$$
\boxed{
U=\frac{-48X+5Y+4Z}{9}=\rho(1+8t)^3,\qquad
V=\frac{Y+Z}{2}=\rho g_2^2.}                                    \tag{2}
$$
二者在原点的值都为一。$U$ 正是 R316 的五因子来源：
$$
U=\Theta(z)\Theta(2z)^4
  =\sigma^{34}x^5(x^3-8b)^4.                                   \tag{3}
$$
若 $Q_4=x^6+20bx^3-8b^2$，则
$$
V=\sigma^{34}x^2(x^3-8b)Q_4^2.                                 \tag{4}
$$
所以 $U$ 的零点只在原三挠点与六挠点；$V$ 另在十二个原始四挠点有二阶零。这里的单位是原点单位，不是将它们的完整 Mellin 导数置零。

R309 的归一化曲线有节点 $t=0,1$，以及 $g_2=0$ 的自切双点。节点处原次数 $m$ 的粘合是
$$
f(1)=729^m f(0).                                                \tag{5}
$$
自切双点的两个分支在 $Y\ne0$ 图中的共同坐标为
$\xi=X/Y+1/24$，原函数的值及关于 $\xi$ 的一次项分别相同。
完整导子要求在 $0,1$ 各零一次、在 $g_2$ 两根各零二次。

下面使用完整整格
$$
\rho^D d\,R[t]_{\le4D-6}\ \subset\ \mathcal A_D
\qquad(D\ge2).                                                  \tag{6}
$$
这不是把归一化免费当成原格。R309 的三个原 conic 满足
$C_j(X,Y,Z)=\rho^2d t^j$，$j=0,1,2$。
其已有五个原三次代表及本篇证书中的 $dt^5,dt^6$ 三次代表，
分母只含二、三；后两项可取分母
$2^{14}3^{11}$、$2^{15}3^{11}$。因此三个 $C_j$ 乘归一化的全部
$0,\ldots,4m$ 角，覆盖 $dR[t]_{\le4m+2}$，并由 R309 的原
Koszul 递推逐次留在 $\mathcal A_{m+2}$。这给 (6)，没有随 $D$
新增的坏素数。等价地，节点及自切双点的全部导子条件已经支付。

## 2. 真范数三映射与完整 carrier

取 $\delta=\sqrt{-3}=1+2\omega$。在原 $E_b$ 上，
$$
x(\delta z)=-\frac{x^3+4b}{3x^2},\qquad
\sigma(\delta z)=\delta x(z)\sigma(z)^3.                         \tag{7}
$$
第一式由原三同源及 $\delta^2=-3$ 给出。第二式的两侧有相同零除子；
原 sigma 的 CM 准周期满足
$\eta(\delta\gamma)=\bar\delta\eta(\gamma)$，
故其比值为常数，而原点首项给常数 $\delta$。
也可直接以 $\sigma=z+O(z^7)$ 定标。没有遗留二次指数因子。

于是
$$
\Theta(\delta z)=(1-4t)\Theta(z)^3,\qquad
\boxed{\tau(t):=t(\delta z)=-\frac{27t}{(1-4t)^3}},               \tag{8}
$$
及
$$
\boxed{\frac{\rho(\delta z)}{\rho(z)^3}
=\mathcal R(t):=
\frac{(1-4t)^{14}((1-4t)^3-216t)}{(1+8t)^3}.}                   \tag{9}
$$
实际角映射还满足
$$
\tau-1=\frac{(t-1)(1+8t)^2}{(1-4t)^3},\qquad
\tau\equiv-t-\frac52\pmod{g_2}.                                \tag{10}
$$
所以它交换两个自切分支。原零质量平面是
$\langle X,Z-Y\rangle$；这两个函数在 $t=0,1$ 都为零。
由 (10)，
$$
r_X(t)=\mathcal R(t)a(\tau(t)),\qquad
r_{Z-Y}(t)=\mathcal R(t)(C-B)(\tau(t))                           \tag{11}
$$
的分母都只剩 $1+8t$ 的一次幂，且无穷角阶均不超过十二。
对原 $X$，该极确实存在；其分子准确为
$$
\begin{aligned}
(1+8t)r_X={}&27t(t-1)(4t-1)^2(16t^2+4t+7)\\
&\cdot(64t^3-48t^2+228t-1)\\
&\cdot(1792t^4-3136t^3+2112t^2-40t+1).
\end{aligned}                                                   \tag{12}
$$

**非零质量来源不可能有原点为单位的返回。**
实际
$$
\mathcal R(0)=1,\quad \tau(0)=0,\quad
\mathcal R(1)=-3^{13},\quad \tau(1)=1.
$$
所以对质量非零的原线性来源 $T$，其
$T(\delta z)/\rho^3$ 在节点两支的比为 $-3^{19}$，而次数三的原粘合应为
$729^3=3^{18}$，多了准确因子 $-3$。
任何原次数 $m$ 的单位乘子在两支的比固定为 $729^m$；
因此不能改变这个差异。这是实际来源的节点计算，不是一般矩阵的反例。

## 3. 原 $H_1$ 的最小单位乘子与全二次空间

仅用 $U$ 清分母并不够：$U X(\delta z)$ 仍不满足自切点的粘合。
准确地，
$$
\boxed{\frac{r_X(t)}{B(t)^3}\equiv\frac{3(4t-1)}8\pmod{g_2}.}     \tag{13}
$$
右边在 $g_2$ 两根的值不同，且差为单位乘这两根之差。

设原乘子的角多项式为 $k(t)$。在 $Y$ 图中写
$k/B^m$。其两分支值原本相同；(13) 强迫该值为零。
其共同一次项再乘 (13) 的两个不同值，又迫共同一次项为零。
故任何返回乘子必须被 $g_2^2$ 整除。
此外 (12) 的真实极要求它被 $1+8t$ 整除。

原次数一的角次数不超过四，而
$(1+8t)g_2^2$ 的次数是五。因此：
$$
\boxed{\text{原 }X(\delta z)\text{ 不存在任何非零次数一返回乘子。}} \tag{14}
$$
这个结论比只检查一个候选 $U$ 强。

次数二时，全部返回乘子准确是
$$
\boxed{
K=\rho^2(1+8t)g_2^2P(t),\quad
\deg P\le3,\quad P(1)=81P(0).}                                 \tag{15}
$$
必要性由上述两类条件及角次数八得出；最后一个条件正是原节点 (5)，因为
$(1+8t)g_2^2$ 在 $1$ 的值为 $3^8$，次数二原比为 $3^{12}$。
反之，这些条件使 $K$ 本身满足原全部粘合；
$Kr_X$ 的角次数不超过二十且被 $d$ 整除，故由 (6) 返回 $\mathcal A_5$。

一个原点单位、角次数最小为六的选择是
$$
\boxed{
K_\delta=
\frac{4608X^2-1392XY-1776XZ+41Y^2+77YZ+44Z^2}{162}
=\rho^2(1+8t)(1+80t)g_2^2.}                                   \tag{16}
$$
于是
$$
K_\delta H_1(\delta z)\in\mathcal A_5,\qquad K_\delta(0)=1.       \tag{17}
$$
同一个乘子也返回整个零质量平面。全部三维空间 (15) 可用
$P=1+80t,\ t(t-1),\ t^2(t-1)$ 给出；每一项的原二次代表和返回的原五次代表
都在旁列 JSON 中，不以存在性取代整代表。

例如对缩放后的原 $X=7bH_1$，有
$$
K_\delta X(\delta z)=Q_5(X,Y,Z),
$$
其中
$$
\begin{aligned}
288Q_5={}&718848X^3Y^2+1658880X^3YZ+1327104X^3Z^2\\
&-24192X^2Y^3+73728X^2Y^2Z+193536X^2YZ^2+55296X^2Z^3\\
&-192XY^4-480XY^3Z-480XY^2Z^2-1920XYZ^3-384XZ^4\\
&+7Y^5-11Y^4Z+16Y^3Z^2+20Y^2Z^3-16YZ^4-16Z^5.
\end{aligned}                                                   \tag{18}
$$
因此原 $H_1$ 的右端就是 $Q_5/(7b)$；原曲线和原固定整格都没有更换。

有一条需明确区分的特殊零质量线：
$$
F_*:=Z-Y-48X=-144\rho\,t(t-1)g_2.
$$
它本身已在两个自切分支各零一次，故
$$
K_*=\frac{24X+2Y+Z}{3}
=\rho(4t-1)(8t+1)g_2,\quad K_*(0)=1,\quad
K_*F_*(\delta z)\in\mathcal A_4.                               \tag{19}
$$
证书给出完整四次代表。但它的中央导数是
$J_5'-J_3'-336bJ_1'$；原 $J_1'=0$ 不使它自动为零。
(19) 不是一个新秩二来源。

## 4. 全部混合 $2^a\delta^b$ 缩放的统一返回

此节指数 $a,b$ 为非负整数；固定曲线参数仍为十七。
设
$$
\alpha=2^a\delta^b,\qquad q=\operatorname N(\alpha)=4^a3^b.
$$
$\sigma(\alpha z)/\sigma(z)^q$ 是原 CM 除法函数；
其准周期由 $\eta(\alpha\gamma)=\bar\alpha\eta(\gamma)$ 及原半特征抵消。
所以 $H_1(\alpha z)/\rho^q$ 是 $\mu_6$ 不变的有理函数，即 $t$ 的有理函数。
其可能极仅来自 $\rho$ 的两个固定零集合。

为不隐藏角次数，逐处列出实际阶数：

| 原位置 | $\rho$ 的零阶 | $U$ 的零阶 | $V$ 的零阶 |
|---|---:|---:|---:|
| 两个非零三挠点 $x=0$ | 14 | 5 | 2 |
| 六个 $x^3=8b$ 的六挠点 | 1 | 4 | 1 |
| 十二个原始四挠点 | 0 | 0 | 2 |

原 $H_1$ 在 $O$ 零六阶，在非零二挠点和 $x=0$ 的三挠点均零二阶；
这些都是 R297 的原除子事实。

现在设 $b\ge1$。$\alpha$ 杀掉上述三挠点，故其拉回在 $x=0$ 零六阶。
因此 $H_1(\alpha z)/\rho^q$ 的无穷角阶为
$$
\frac{14q-6}{3}.                                               \tag{20}
$$
在 $x^3=8b$：
若 $a\ge1$，$\alpha$ 同时杀二、三部分，原零阶为六；
若 $a=0$，它送到非零二挠点，原零阶为二。
故该处有理分母的次数分别为 $q-6$、$q-2$。

考虑 $U^mV^eH_1(\alpha z)$，原次数
$D=q+m+e$。清掉这个有限极要求
$$
3m\ge q-6\quad(a\ge1),\qquad
3m\ge q-2\quad(a=0).                                          \tag{21}
$$
无穷角次数不超过 $4D$ 的准确条件是
$$
\frac{14q-6}{3}+3m+4e\le4(q+m+e)
\quad\Longleftrightarrow\quad m\ge\frac{2q}{3}-2.                \tag{22}
$$
在节点两个原像，$H_1(\alpha z)$ 均有足够零阶。
当 $a\ge1$ 时，原始四挠点送到二挠点或原点，至少零二阶，已付完整自切导子；
当 $a=0$ 时，取 $e=1$ 由 $V$ 支付这两阶。由 (6) 得到真正原格中的统一式：
$$
\boxed{
\begin{array}{ll}
a\ge1,\ b\ge1:
&U^{\,2q/3-2}H_1(2^a\delta^bz)\in\mathcal A_{\,5q/3-2};\\[2mm]
a=0,\ b=1:
&UVH_1(\delta z)\in\mathcal A_5;\\[2mm]
a=0,\ b\ge2:
&U^{\,2q/3-2}VH_1(\delta^bz)\in\mathcal A_{\,5q/3-1}.
\end{array}}                                                   \tag{23}
$$
所有乘子在原点都是一。特别第一条不是粗略将每一次返回次数相乘：
例如 $q=12$ 的混合同源返回次数为十八。

纯倍点情形也可用同一个 $U$ 写成
$$
U^{\,2(4^a-1)/3}H_1(2^az)
\in\mathcal A_{(5\cdot4^a-2)/3}\qquad(a\ge1).                   \tag{24}
$$
此时 $x=0$ 仍送到非零三挠点，故 (20) 的六改成二。
完整倍点有限目标另见 R314；(24) 的阶数证明与这里一致。

## 5. 同一个 $q^2$ 目标的全部尺度进位

固定好惰性 $p=6s-1>7$、$p\ne17$。令 $d_p=p+1=6s$，
$\kappa=34c_p$ 为 R301 的原 Gaussian 系数，
$a_p=p\kappa\in\mathbf Z_p^\times$，并置
$$
w=z^6,\qquad G(w)=e^{-\kappa w^s}\rho(z).
$$
沿 R309 使用同一完整有限目标
$$
\mathcal T_{s,\ell}
=\mathbf Z_p[w,\epsilon]/
 (w^s-p\epsilon,\ \epsilon^3,\ w^\ell\epsilon^2).                \tag{25}
$$
原 $\rho$ 在其中为 $G e_2(a_p\epsilon)$，其中
$e_2(v)=1+v+v^2/2$。

对上述每个 $\alpha$，令
$$
c_\alpha=\alpha^6=64^a(-27)^b,\qquad
\Delta_{\alpha,p}=\frac{\alpha^{p+1}-q}{p}\in\mathbf Z.           \tag{26}
$$
整数性来自惰性剩余 Frobenius：
$\alpha^p\equiv\bar\alpha\pmod p$。
若 $\mathcal R_\alpha(t)=\rho(\alpha z)/\rho(z)^q$，则准确有
$$
\boxed{
G(c_\alpha w)=G(w)^q\mathcal R_\alpha(t)
       \exp(-a_p\Delta_{\alpha,p}w^s).}                         \tag{27}
$$
在 (25) 中，最后一项必须完整取为
$e_2(-p a_p\Delta_{\alpha,p}\epsilon)$，而尺度变量是
$$
\epsilon_\alpha=\alpha^{p+1}\epsilon
=(q+p\Delta_{\alpha,p})\epsilon.
$$
因此全部三块的真实抵消为
$$
e_2(-p a_p\Delta_{\alpha,p}\epsilon)\,
e_2(a_p(q+p\Delta_{\alpha,p})\epsilon)
=e_2(qa_p\epsilon)\pmod{\epsilon^3}.                            \tag{28}
$$
只保 $\epsilon_\alpha=q\epsilon$，或删掉 (27) 的一项，都会遗失同一矩阵的下一位。

返回乘子 $U^mV^e$ 在同一目标中的真实像是
$$
G^{m+e}e_2((m+e)a_p\epsilon)
(1+8t)^{3m}g_2^{2e}.                                          \tag{29}
$$
它是整单位：$G(0)=1$、$t(0)=0$、$g_2(0)=-1$。
其逆的指数部分准确为
$e_2(-(m+e)a_p\epsilon)$，其他各项在有限目标中逐项整地求逆。
所以除掉返回乘子是在这个**同一有限目标**中的整单位行操作，
不损任何 Smith 长度，也没有移走边界行。
这仅比较指定来源与其返回像；没有声称全部目标格的像已经饱和。

## 6. 原完整中央条件及尚须支付的独立性

为了明确算术输入，记 $\mathcal J_{q,T}$ 为来源 $T$ 使用几何次数
$34q$、Gaussian $q\kappa$ 的同一 Newton 归一化。
对 $T(z)=H_1(\alpha z)$，有
$$
\boxed{
\mathcal J_{q,H_1(\alpha z)}(u)
=\left(\frac{\alpha^{p+1}}q\right)^u\mathcal J_{1,H_1}(u).}        \tag{30}
$$
比例在 $1+p\mathbf Z_p$ 中。证明可在每个非负整数 $k$ 直接读原 Taylor
系数：
$$
\mathcal J_{q,H_1(\alpha z)}(k)
=k!(q\kappa)^{-k}\alpha^{d_pk}h_{d_pk}
=\left(\frac{\alpha^{d_p}}q\right)^k\mathcal J_{1,H_1}(k).
$$
两边都由 R301 的相同 Gauss 范数论证在 $\mathbf Z_p$ 解析。
这里 $\alpha$ 是 $p$ 进单位；新的 Gaussian 与缩放后原 Gaussian
之差为 $a_p\Delta_{\alpha,p}z^{d_p}$，在 R301 的半径上指数范数为一。
所以非负整数上的等式推出完整解析等式，未省略 Newton 尾。

因原 $\mathcal J_{1,H_1}(0)=0$，
$$
\mathcal J_{q,H_1(\alpha z)}'(0)=\mathcal J_{1,H_1}'(0).          \tag{31}
$$
故假设原中央导数为零时，(23) 所返回的**除乘子后的真实观察**
全部为零。不是说 $U^mV^eH_1(\alpha z)$ 本身的 Mellin 导数为零。

混合缩放的尺度还有准确乘法式
$$
\frac{\alpha^{p+1}}q
=\left(2^{p-1}\right)^a
 \left(\frac{(-3)^{(p+1)/2}}3\right)^b,                         \tag{32}
$$
其 $p$ 进对数为
$(p-1)(a\log_p2+b\log_p3/2)$。

由 (23)，次数至多 $D$ 时可纳入的 $a,b\ge1$ 的数目是
$$
\frac{(\log D)^2}{2\log4\,\log3}+O(\log D).                     \tag{33}
$$
这是三角区域中的整点计数：$a\log4+b\log3$ 的上界为
$\log(3(D+2)/5)$，边界误差为 $O(\log D)$。
每一条都已支付原来源、单位乘子、全部进位及原中央等式。

但这些条件仍来自同一个完整算术中央零。
(28)、(30) 尤其说明：单靠尺度的差别或 (33) 的数量，不足以断言
它们在原低次有限像中给出独立深 Smith 因子。
下一项实际工作是把 (23)、(29) 放入同一个原有限评价映射，
计算其新增像和真实 Bockstein 约束；跨 $p$ 非零仍未证明。

## 7. 精确证书

[check-jzero-ramified-three-and-mixed-return.py](../scripts/check-jzero-ramified-three-and-mixed-return.py)
及旁列 JSON 有 **41 项精确检查全部 PASS**：
原角映射与 theta 单位、次数一的完整秩障碍、全三维二次返回空间、
原五次/特殊四次代表、完整导子末两角，以及三块尺度抵消。
没有抽取目标素数作扫描，也没有用有限计算替代 (23)、(30) 的全体证明。

直接依赖：
[R297](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)、
[R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
[R309](R309-three-original-jzero-quartic-conductor-and-paid-q2-image.md)、
[R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。

