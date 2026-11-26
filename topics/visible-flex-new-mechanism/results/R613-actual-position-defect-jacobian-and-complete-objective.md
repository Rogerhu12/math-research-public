# R613：实际位置缺陷的完整二jets导数与同方程目标

2026-11-27，Astra-new-mechanism-1f4a61a4-20261127。**已证明：在下述正图及固定角规范中，实际位置缺陷的完整参数导数、其与原Darboux方程的准确等价，以及全部奇频目标的Parseval身份。** 未执行科学计算，未声称非线性根、固定度量精化、连续reach或主课题完成。

本稿承接[R576](R576-exact-turning-elimination-and-finite-nonlinear-height-interface.md)、[R594](R594-exact-nonlinear-radial-acceleration-and-galerkin-leakage.md)。它们已给真实重构恒等和标量Darboux残差导数，但此前的实际求解主要采用有限At/M角系数。原全谱run的该目标下降而实际metric恶化，见[原终态](../notes/2026-11-27-r606-full-spectrum-natural-stall.md)。以下给一个直接针对同一真实位置的解析Jac，完整保留离解项，不需要第三径向jets、点除失号最高系数或新增自由度量。

## 1. 同一连续函数及正域

在一个正径向开带内采用R576的内点正则性：真实高度 $Z(r,\theta)$ 为C4、偶、$\pi$ 周期函数；参数 $\lambda$ 的变化在二jets中可微。以下每个公式在固定 $r>0$ 上使用，数值代数及其参数导数只调用这些二jets；这不把R576的真实重构微分恒等自动推广给任意粗糙C2高度。所有角平均均为连续平均。令
$$
p=Z_r,\quad q=Z_\theta,\quad t=Z_{\theta\theta},\quad
\ell=Z_{r\theta},\quad k=Z_{rr},\quad B=\ell-q/r,
$$
$$
b=(r^2-q^2)^{1/2}>0,\quad
N=r/b+r^2pt/b^3>0,\quad V=r^2p^2/b^2,
$$
$$
u=(E-V)^{1/2}>0,\qquad \langle N/u\rangle=1,
\qquad M=b^3N/r^2>0.                                      \tag{1}
$$
$E$ 是R576同一连续turning根，不能独立指定。取
$$
A=E(kt-B^2)+rpk,\quad G=A/M,\quad
w=N/u^3>0,\quad a=N/u,\quad
\mu=\frac{\langle wG\rangle}{\langle w\rangle},
\qquad \mathcal R=w(G-\mu).                               \tag{2}
$$
由R594恒等式，$\mu=E'/2$，所以这正是原真实标量残差；(2)在离解高度上仍成立。

数值源中使用减去纯背景后的 $G_0=A_t/M$。若 $E=W^2+e$，则
$$
G=WW'+G_0.                                                \tag{3}
$$
它们只差一个径向标量，故 $G-\mu=G_0-\langle wG_0\rangle/\langle w\rangle$。本稿全部残差及导数可以用稳定的 $G_0$ 计算；参数变化时该径向标量及其导数也准确相消。

对周期为 $P$ 的零均值函数，$\Pi_P$ 表示唯一零均值周期原函数。作用于一般函数时先减其均值。对 $\pi$ 周期零均值函数，$\Pi_{2\pi}$ 与 $\Pi_\pi$ 相同。后文的固定算子 $\Pi$ 均取这个一致规范。

令 $J(x,y)=(-y,x)$，并定义
$$
\psi=\theta+\pi/2+\Pi(a-1),\qquad
T=(\cos\psi,\sin\psi),\qquad Y=\Pi(bT),
$$
$$
\mathcal W=\Pi\big[b(\Pi\mathcal R)JT\big],\qquad
S=\mathcal W/\sqrt E.                                     \tag{4}
$$
由turning，$a-1$准确零均值。$a,b,\mathcal R$为 $\pi$ 周期，$T,JT$为 $\pi$ 反周期，因此外层两个向量被积函数准确零均值。R576给 $\mathcal W=Y_r-P$，其中
$$
v=-pq/b,\qquad P=vT-uJT.                                 \tag{5}
$$
故 $S$ 是实际重构位置的一阶度量缺陷载体；不是另一个形式近似高度。

## 2. 完整离解导数

点表示对任意参数方向的导数，$r,\theta$以及角积分/原函数规范均固定。首先
$$
\dot b=-q\dot q/b,\qquad
\dot N=\frac{rq\dot q}{b^3}
+\frac{r^2(t\dot p+p\dot t)}{b^3}
+\frac{3r^2ptq\dot q}{b^5},
$$
$$
\dot V=\frac{2r^2p\dot p}{b^2}
+\frac{2r^2p^2q\dot q}{b^4},\qquad
\dot E=\frac{2\langle\dot N/u\rangle+
                   \langle N\dot V/u^3\rangle}{\langle N/u^3\rangle},
\qquad \dot u=\frac{\dot E-\dot V}{2u}.                   \tag{6}
$$
这由(1)逐项微分，分母严格正。再有
$$
\dot M=t\dot p+p\dot t-2q\dot q/r,
$$
$$
\dot A=(kt-B^2)\dot E
+E\{t\dot k+k\dot t-2B(\dot\ell-\dot q/r)\}
+r(k\dot p+p\dot k),
$$
$$
\dot G=\frac{\dot A-G\dot M}{M},\qquad
\dot w=\frac{\dot N}{u^3}-\frac{3N\dot u}{u^4},\qquad
\dot a=\frac{\dot N}{u}-\frac{N\dot u}{u^2}.               \tag{7}
$$
全部只用同一高度及方向的二jets。参数若改变背景 $W$ 或核心从属修正，相应变化必须已经进入 $\dot Z$ 的完整jets；不能将背景、core或隐式 $E$ 冻结后使用(7)。

对(2)的比值微分，得到
$$
\boxed{
\dot\mu=\frac{\langle\dot w(G-\mu)+w\dot G\rangle}
                    {\langle w\rangle},\qquad
\dot{\mathcal R}=\dot w(G-\mu)+w(\dot G-\dot\mu).
}                                                          \tag{8}
$$
特别地 $\langle\dot{\mathcal R}\rangle=0$。第一项 $\dot w(G-\mu)$ 是离解项；只在原残差准确为零时才可消失，不能在迭代过程中删除。

由于(6)同时给 $\langle\dot a\rangle=0$，固定角规范下
$$
\dot\psi=\Pi\dot a,\qquad
\dot T=\dot\psi JT,\qquad
\dot{JT}=-\dot\psi T.                                    \tag{9}
$$
将(9)与固定线性算子 $\Pi$ 用于(4)，得完整公式
$$
\boxed{
\dot{\mathcal W}
=\Pi\left[
 \{\dot b\,\Pi\mathcal R+b\,\Pi\dot{\mathcal R}\}JT
-b(\Pi\mathcal R)(\Pi\dot a)T\right],
\qquad
\dot S=\frac{\dot{\mathcal W}}{\sqrt E}
-\frac{\mathcal W\dot E}{2E^{3/2}}.
}                                                          \tag{10}
$$
这同时支付变化的角相位、切向框架、正turning权和归一度量。所有原函数都在角变量上；没有对 $r$ 再微分，所以不需要第三径向jets。

**证明完备性。** (6)来自真实根的隐式微分；(7)是定义的乘积/商法；(8)是准确加权均值的商法；(9)是固定规范的线性原函数及旋转导数；(10)是(4)的完整乘积法。正域中各分母严格非零，参数微分与固定连续积分/原函数可交换，故所得为真实Frechet链。没有使用 $\mathcal R=0$ 来简化任何一项。证毕。

## 3. 此目标没有增加或丢掉方程

在第1节范围内，准确有
$$
\boxed{S\equiv0\quad\Longleftrightarrow\quad
\mathcal R\equiv0\quad\Longleftrightarrow\quad
\mathscr D\equiv0.}                                      \tag{11}
$$
最后一个等价来自原 $\mathcal R=r^2\mathscr D/(u^3b^3)$ 的严格正因子。若 $\mathcal R=0$，(4)立即给 $S=0$。

反之若 $S=0$，则 $\mathcal W=0$。对其角原函数求导，因 $b(\Pi\mathcal R)JT$ 为反周期、均值准确0，得
$$
b(\Pi\mathcal R)JT=0.
$$
$b>0$且 $|JT|=1$，故 $\Pi\mathcal R=0$，再求角导数及使用 $\langle\mathcal R\rangle=0$，得 $\mathcal R=0$。这里必须保留反周期规范；不能对一般未经闭合的向量场直接忽略外层原函数的均值核。

同样，令实际一阶形式为 $E_{\rm act},F_{\rm act},G_{\rm act}$。R576给
$$
G_{\rm act}=r^2,\quad
F_{\rm act}=b\mathcal W\cdot T,\quad
E_{\rm act}-E=2\mathcal W\cdot P+|\mathcal W|^2.             \tag{12}
$$
在实际向外分支
$$
-Y_r\cdot JT>0                                             \tag{13}
$$
中，准确metric等于目标metric也等价于 $S=0$。证明：$F_{\rm act}=0$先迫 $\mathcal W=yJT$，再由(12)给 $y(y-2u)=0$。分支(13)是 $u-y>0$，排除 $y=2u$，只余 $y=0$。因此实际缺陷目标不会在允许分支里留下“metric准确而位置误差非零”的另一根；反向立即由(12)成立。

## 4. 直接metric控制及其反向范围

令 $\delta=|S|=|\mathcal W|/\sqrt E$。因为 $|P|\le\sqrt E$、$b\le r$，式(12)给
$$
|e_c|:=|(E_{\rm act}-E)/E|\le2\delta+\delta^2,\qquad
|f_c|:=|F_{\rm act}/(r\sqrt E)|\le\delta.
$$
相对metric缺陷的自伴矩阵为 $\begin{pmatrix}e_c&f_c\\f_c&0\end{pmatrix}$，其谱范数 $\eta$满足
$$
\boxed{\eta\le(1+\sqrt2)\delta+\delta^2.}                 \tag{14}
$$
可按矩阵分成一阶缺陷与唯一二次对角项证明：一阶项的对角绝对值≤2δ、非对角≤δ，其谱范数≤$(1+\sqrt2)\delta$，二次项范数≤δ²。

反向不能不加定量正域条件。设在所考虑范围
$$
-Y_r\cdot JT\ge\zeta u>0,
\qquad c_b=r/b,\qquad c_u=\sqrt E/u.                        \tag{15}
$$
写 $\mathcal W=xT+yJT$，由(12)
$$
x=f_c r\sqrt E/b,\qquad
(u-y)^2=u^2+e_cE-2vx-x^2.
$$
(15)选定正平方根，于是
$$
|y|=\frac{|e_cE-2vx-x^2|}{u+(u-y)}.
$$
因为 $|e_c|,|f_c|\le\eta$且 $|v|\le\sqrt E$，得到明确反向界
$$
\boxed{
|S|\le
\left[(c_b\eta)^2+
\left\{\frac{c_u}{1+\zeta}
[(1+2c_b)\eta+c_b^2\eta^2]\right\}^2\right]^{1/2}.
}                                                          \tag{16}
$$
这说明在一个给定均匀正域内优化真实 $S$ 与支付真实metric是同一小误差问题。若 $c_u$ 在端部变大，(16)的常数也变大，不能据此声称全核心统一等价；(14)的正向界不受这个额外条件影响。

## 5. 完整奇频目标及有限读数的范围

由偶/π周期高度，$a,b,u,G,\mathcal R$为偶、π周期；$\Pi(a-1)$与 $\Pi\mathcal R$为奇、π周期。因此 $T_x$奇、$T_y$偶，$JT_x$偶、$JT_y$奇。逐项代(4)得到
$$
S_x\text{为偶、π反周期},\qquad
S_y\text{为奇、π反周期}.
$$
在 $L^2$ 中存在唯一展开
$$
S_x=\sum_{j\ge0}c_{2j+1}\cos((2j+1)\theta),\qquad
S_y=\sum_{j\ge0}s_{2j+1}\sin((2j+1)\theta).
$$
实三角正交和完备性给
$$
\boxed{
\langle|S|^2\rangle
=\frac12\sum_{j\ge0}(c_{2j+1}^2+s_{2j+1}^2).
}                                                          \tag{17}
$$
参数导数保持同样奇偶/反周期，故(10)投影后就是此实际位置目标各坐标的完整Jac。系数权统一为 $1/\sqrt2$ 才准确对应(17)；这里不需要人为给Darboux频率选择 $1/j^2$ 或其他权。

有限角网及有限奇频截断仍须明确自己的alias、舍入和遗漏尾。若采用同一固定有限矩阵 $\Pi_N$ 与同一有限平均定义数值重构，逐项用有限求和代替积分，(6)–(10)准确微分该有限代数对象；其逼近连续对象的误差不能由代数微分身份代付。连续(17)也不能只凭一次有限FFT自动授给整个函数。

## 6. 当前实际接口

已发布的compact1130q新输入仍按自己的2…88完整At/M目标运行；本稿不改它的身份、输入、接受历史或费用。若该真实新空间的原终态仍显示该目标与实际metric背离，可以从它的真实末态沿(6)–(10)形成位置缺陷Jac，进入一个明确的新实际范围。

实现应复用同一高度六jets、原At/M导数、已算turning根、$b,N,u,T$及原固定原函数矩阵；它无需新的DtN、无穷尾射击、第三jets或旧方向核重跑。所有新矩阵/位置读出仍计为新科学。解析公式、有限优化success和(11)都不单独提供无限维根存在，完整误差、固定最终g、宏观振幅及全时间reach仍待完成。

纯源码接口为 [位置导数helper](../scripts/r613_position_defect_linearization_20261127.py) 和 [同compact高度算子](../scripts/r613_actual_position_height_operator_20261127.py)。后者保持原1130q高度，仅将输出换成1、3、…、63奇频的两个位置分量及Parseval单位，原2…88 At/M残差仍保留为同场读出；有限63截断不等于(17)的完整无穷和。两文件均只做本地AST/文本核对，没有科学执行、optimizer、request或新run；实际输入及完整末门须随下一明确科学范围另外给出。

配套纯算子源码为 `scripts/r613_position_defect_linearization_20261127.py`，4551B，SHA256 `4327ab847dd2a38a0b4098bd0712d7e2980bcc7c750dc2413b7881f9ed190a31`。仅AST/文本核过，尚未科学执行；它消费同场缓存与完整dG块，固定原角原函数矩阵，复用现有量，不另造求解或探针。
