# R576：turning 消去径向度量、二 jets 真残差与有限高度接口

状态：完整纸面推导；尚未给出非轴对称有限高度解，也未给出本题完成证书。
本条把 R574 的 Darboux 方程和 R575 的径向 metric 设计提升到准确有限非线性：径向度量可以由每一圈的 turning 条件唯一消去，剩下的是非零角模的真实高度方程。
它同时给出该方程不为零时，按同一构造得到的位置图的准确 metric 误差。
闭面、固定握持区、reach 和宏观位移仍须对实际解分别支付。

来源：R574、R575 的已登记公式；下面全部计算与证明在本条展开。
没有执行本地科学计算。

## 1. 高度、对称性和两个必要正性

在 $r_c<r<R$ 上给定足够光滑的高度 $Z(r,\theta)$，其角变量为 $2\pi$ 周期，并满足
$$
Z(r,-\theta)=Z(r,\theta),\qquad
Z(r,\theta+\pi)=Z(r,\theta).                         \tag{1}
$$
内点推导可取 $C^4$；下文的代数值只调用高度的二阶 jets，并不借此自动主张所有粗糙 $C^2$ 高度都有四阶曲率公式。
记
$$
p=Z_r,\qquad q=Z_\theta,\qquad
b=\sqrt{r^2-q^2},\qquad v=-\frac{pq}{b},             \tag{2}
$$
并要求 $b>0$。
再记
$$
N=b_r-v_\theta
 =\frac r b+\frac{r^2pZ_{\theta\theta}}{b^3}>0,
\qquad V=\frac{r^2p^2}{b^2}.                         \tag{3}
$$
(3) 的展开没有省略 $Z_{r\theta}$：由
$b_r=(r-qZ_{r\theta})/b$ 和 $v_\theta$
展开后，两项中的 $qZ_{r\theta}/b$ 抵消；
$b^2+q^2=r^2$ 给出最后一式。

令 $\langle\cdot\rangle$ 表示归一角平均。
本条中 $\Pi$ 始终是 $2\pi$ 周期的零均值角原函数：
$$
\partial_\theta\Pi f=f-\langle f\rangle,
\qquad \langle\Pi f\rangle=0.                         \tag{4}
$$
对向量逐分量使用同一定义。

## 2. 唯一径向 metric：turning 方程确有根

对每一固定 $r$，考察
$$
\mathcal T_r(E)=\left\langle
 \frac{N}{\sqrt{E-V}}
\right\rangle,
\qquad E>\max_\theta V.                              \tag{5}
$$
存在唯一 $E(r)$ 满足
$$
\mathcal T_r(E(r))=1.                                \tag{6}
$$
证明如下。
在定义域内
$$
\partial_E\mathcal T_r(E)
 =-\frac12\left\langle\frac{N}{(E-V)^{3/2}}
   \right\rangle<0.                                  \tag{7}
$$
当 $E\to\infty$，被积函数一致趋零。
当 $E\downarrow V_{\max}$，取 $V$ 的一个最大点 $\theta_0$。
由于 $V$ 对角变量为 $C^2$，在其小邻域有
$$
0\le V_{\max}-V(\theta)
 \le C\,|\theta-\theta_0|^2.
$$
同时连续正函数 $N$ 在该邻域有正下界 $n_0$。
所以 $\mathcal T_r(E)$ 下界包含
$$
\frac{n_0}{2\pi}
\int_{-\delta}^{\delta}
\frac{dt}{\sqrt{E-V_{\max}+Ct^2}},
$$
它趋于无穷；若 $C=0$ 则发散更快。
因此 (6) 有唯一根。这里并没有把 $E\downarrow V_{\max}$ 的发散当成未经验证的假设。
局部隐函数定理及 (7) 给出该根的光滑依赖。

以后统一定义
$$
u=\sqrt{E-V}>0,\quad
a=\frac Nu>0,\quad
c=\frac{va-u_\theta}{b}.                             \tag{8}
$$
于是 $\langle a\rangle=1$。
由 (1)，$b,N,u,a$ 为偶函数，$v,c$ 为奇函数，故 $\langle c\rangle=0$。
所有这些函数都是 $\pi$ 周期。

## 3. 闭合平面圈与准确的预测速度

定义角度、单位切向和位置
$$
\psi=\frac\pi2+\theta+\Pi(a-1),\qquad
T=(\cos\psi,\sin\psi),\qquad
Y=\Pi(bT).                                           \tag{9}
$$
令 $J(x,y)=(-y,x)$。
因为 $a,b$ 是 $\pi$ 周期且 $\langle a\rangle=1$，有
$$
\psi(\theta+\pi)=\psi(\theta)+\pi,
\qquad bT(\theta+\pi)=-bT(\theta).
$$
因此 $\langle bT\rangle=0$，每圈准确闭合，且
$$
Y_\theta=bT,\qquad
Y(\theta+\pi)=-Y(\theta),\qquad \langle Y\rangle=0.   \tag{10}
$$
零均值规范同时固定了每圈的平面中心，不再引入自由的逐圈平移。

与目标旋转度量
$$
g=E(r)\,dr^2+r^2\,d\theta^2                         \tag{11}
$$
对应的预测径向速度是
$$
P=vT-uJT.                                           \tag{12}
$$
的确，如果 $Y_r=P$，则对 $X=(Y,Z)$ 有
$$
|X_\theta|^2=b^2+q^2=r^2,
\quad X_r\cdot X_\theta=vb+pq=0,
\quad |X_r|^2=u^2+v^2+p^2=E.                         \tag{13}
$$
最后一式使用 $v^2+p^2=r^2p^2/b^2$。

## 4. Darboux 残差的二 jets 形式

定义角连接的曲率残差
$$
\mathcal R=\partial_r a-\partial_\theta c.           \tag{14}
$$
它的表面写法似乎含有高度三阶导数，但这些导数准确相消。
下面给出可直接算的二 jets 式及其来源。

设
$$
\begin{aligned}
M&=r+pZ_{\theta\theta}-\frac{q^2}{r}
   =\frac{b^3N}{r^2}>0,\\
Q&=Z_{rr}Z_{\theta\theta}
   -\left(Z_{r\theta}-\frac qr\right)^2,\\
A&=EQ+rpZ_{rr},\\
\mathscr D&=A-\frac{E'}2 M.
\end{aligned}                                                     \tag{15}
$$
则
$$
\boxed{\displaystyle
\mathcal R=\frac{r^2}{u^3b^3}\,\mathscr D.}          \tag{16}
$$

### 4.1 连接式与三阶导数为何消失

二维剩余度量为
$$
\gamma=g-dZ^2=(u\,dr)^2+(v\,dr+b\,d\theta)^2.         \tag{17}
$$
令正交余标架 $e^1=u\,dr$、$e^2=v\,dr+b\,d\theta$，
角连接 $\omega=c\,dr+a\,d\theta$。
(3)、(8) 给出
$$
de^1=\omega\wedge e^2,
\qquad de^2=-\omega\wedge e^1.
$$
因此 $\mathcal R=-K_\gamma ub$，符号可由
$\gamma=u(r)^2dr^2+r^2d\theta^2$ 的
$K_\gamma=u_r/(ru^3)$ 核对。

更直接地，记 $H=\nabla_g^2Z$、$w=1-|\nabla_gZ|_g^2>0$。
由 $\gamma_{ij}=g_{ij}-Z_iZ_j$，两 Levi-Civita 连接的差准确为
$$
\Gamma(\gamma)^k{}_{ij}-\Gamma(g)^k{}_{ij}
 =-\frac{Z^kH_{ij}}w.                                \tag{18}
$$
对 (18) 求曲率时，所见三阶项仅通过
$\nabla_iH_{jk}-\nabla_jH_{ik}$ 出现；这是对一形式 $dZ$
的曲率交换子，等于背景曲率与 $dZ$ 的收缩，因而不含独立三阶导数。
其余一阶与二次连接项合并给出
$$
K_\gamma=
\frac{K_g(1-|\nabla_gZ|_g^2)-\det H/\det g}
     {(1-|\nabla_gZ|_g^2)^2}.                         \tag{19}
$$
也可在 $g$ 的正交正规标架直接展开 (18) 得到 (19)。
对 (11)，全部所需项为
$$
\begin{gathered}
K_g=\frac{E'}{2rE^2},\qquad
H_{rr}=Z_{rr}-\frac{E'}{2E}p,\qquad
H_{r\theta}=Z_{r\theta}-\frac qr,\qquad
H_{\theta\theta}=Z_{\theta\theta}+\frac rE p,\\
w=\frac{u^2b^2}{Er^2},\qquad
\det H-K_g(\det g)w=\frac{\mathscr D}{E}.
\end{gathered}                                                     \tag{20}
$$
代入 (19) 即
$K_\gamma=-r^2\mathscr D/(u^4b^4)$，从而得 (16)。
这明确支付了三阶相消，而不是在数值实现中把它们当成零。

### 4.2 $E'$ 也由二 jets 唯一给出

由 $\langle a\rangle=1$ 及周期性，$\langle\mathcal R\rangle=0$。
将 (15)--(16) 取平均，得到
$$
\boxed{\displaystyle
E'=2\,
\frac{\left\langle r^2A/(u^3b^3)\right\rangle}
     {\left\langle N/u^3\right\rangle}.}             \tag{21}
$$
分母严格为正，恰为 (7) 中导数的 $-2$ 倍。
这里的 $E'$ 是 (6) 所定义根的实际导数；并非另外选的径向函数，也没有用独立 $E'$ 掩盖残差。
先对光滑高度用隐函数定理求得实际 $E'$，再用恒等式消去三阶导数，便严格得到 (21)。
只要计算中使用同一 turning 根和 (21)，(16) 的平均为零；仍须解掉所有非零角模。

### 4.3 竖直核心附近的稳定差量

若 $Z=h+f$、$h'=-W$，取 $e=E-W^2$。
则
$$
V-W^2=-2Wf_r+f_r^2
       +\frac{(-W+f_r)^2 f_\theta^2}{b^2}.            \tag{22}
$$
应以 $u^2=e-(V-W^2)$ 求根，避免两个无穷大背景量相减。
定义 $\widetilde A=A-WW'M$；其完全展开为
$$
\begin{aligned}
\widetilde A={}&-rWf_{rr}-rW'f_r-eW'f_{\theta\theta}
 +(W^2+e)f_{rr}f_{\theta\theta}
 -WW'f_rf_{\theta\theta}\\
&-(W^2+e)\left(f_{r\theta}-\frac{f_\theta}{r}\right)^2
 +rf_rf_{rr}+\frac{WW'}r f_\theta^2.
\end{aligned}                                                     \tag{23}
$$
于是
$$
e'=2\frac{\langle r^2\widetilde A/(u^3b^3)\rangle}
              {\langle N/u^3\rangle},\qquad
\mathscr D=\widetilde A-\frac{e'}2M.                 \tag{24}
$$
在轴对称背景 $f=0$ 上，$e=1$、$\widetilde A=0$、$\mathcal R=0$。
实现仍须监测数值条件数及端点退化；(22)--(24) 不是浮点误差证书。

## 5. 不为零的残差给出真实位置 metric 误差

由 $\langle c\rangle=0$，(9)、(14) 给出
$$
\psi_r-c=\Pi\mathcal R.                              \tag{25}
$$
直接微分 (10)、(12)，并用 $b_r=v_\theta+ua$，得
$$
\partial_r(bT)-\partial_\theta P
 =b(\Pi\mathcal R)JT.                               \tag{26}
$$
因为 $Y_r$、$P$ 都为 $\pi$ 反周期，二者平均均为零。
故不存在遗漏的径向平移常数，准确地有
$$
\boxed{\displaystyle
W_*:=Y_r-P=\Pi\big[b(\Pi\mathcal R)JT\big].}         \tag{27}
$$
这里 $W_*$ 是二维向量误差，与背景斜率 $W$ 区别。
对于实际重构的 $X=(Y,Z)$，
$$
\begin{aligned}
G_{\rm act}&=r^2,\\
F_{\rm act}&=b\,W_*\cdot T,\\
E_{\rm act}-E&=2W_*\cdot P+|W_*|^2.
\end{aligned}                                                     \tag{28}
$$
因此残差到实际 metric 误差的转换是准确恒等式，不只是线性估计。
相对目标正交标架中，令
$$
\epsilon=\frac{E_{\rm act}-E}{E},\qquad
\zeta=\frac{F_{\rm act}}{r\sqrt E}.
$$
其对称 metric 缺陷矩阵为
$\begin{pmatrix}\epsilon&\zeta\\\zeta&0\end{pmatrix}$，
故准确谱范数为
$$
\eta=\frac{|\epsilon|+\sqrt{\epsilon^2+4\zeta^2}}2.   \tag{29}
$$
若 $\delta=|W_*|/\sqrt E$，还得
$|\epsilon|\le2\delta+\delta^2$、$|\zeta|\le\delta$，
因为 $|P|\le\sqrt E$ 且 $b\le r$。

**范围限制。** (21)、(27)--(29) 只需要高度二 jets 及角积分，所以能支付实际 metric 的计算。
当 $\mathcal R\ne0$，实际 $Y_{rr}$ 还含 $\partial_rW_*$；它通常需要更高高度导数或独立的位置重构。
不能把本条的二 jets metric 公式写成二 jets 已经支付实际主曲率或 reach。
在准确 $\mathcal R=0$ 的解上可用 $Y_r=P$ 及其相容导数算曲率；仍需全域上界。

## 6. 准确解的严格凸圈、嵌套和全局嵌入

若 $\mathcal R=0$，(27) 给出 $Y_r=P$。
又有 $\psi_\theta=a=N/u>0$，一圈总 turning 为 $2\pi$。
因此每条闭曲线 $\theta\mapsto Y(r,\theta)$ 都是严格凸的正向单圈。
这一事实也可直接验证：对每一固定单位向量 $n_\phi$，
$\partial_\theta(Y\cdot n_\phi)=bT\cdot n_\phi$ 恰有两个零；
在 $-JT=n_\phi$ 的那个零，二阶导数为 $-ba<0$。
故每一方向唯一支撑点，曲线是其严格凸体的边界，没有自交或多重覆盖。

令 $K_r$ 为其凸体，外法向为 $n=-JT$。
按固定法向角 $\phi$ 参数化唯一支撑点 $\theta(r,\phi)$，定义
$$
s(r,\phi)=Y(r,\theta(r,\phi))\cdot n_\phi.
$$
则
$$
\partial_r s
 =Y_r\cdot n_\phi
  +(Y_\theta\cdot n_\phi)\partial_r\theta
 =u>0.                                               \tag{30}
$$
第二项因切向与法向垂直而准确为零。
因此 $r_1<r_2$ 时 $K_{r_1}\subset\operatorname{int}K_{r_2}$。
这是固定法向的支撑导数结论；不能用固定材料角的径向距离变化替代它。
各圈严格嵌套且每圈单射，所以 $Y$ 是平面环域的全局单射参数化。
其局部 Jacobian 也为 $\det(Y_r,Y_\theta)=ub>0$。
于是 $X=(Y,Z)$ 是该环域上的图，准确嵌入。

### 6.1 内端开平盘

若在 $r\le r_c$ 有 $h$ 常数、$f=0$，且从外侧的全部径向 jets 全平，则
$$
b=r,\ N=1,\ E=1,\ u=1,\ \psi=\theta+\pi/2,
\ Y=r(\cos\theta,\sin\theta)
$$
在开平盘准确成立。
外侧隐函数根在 $E=1$ 处非退化，所以 $E-1$、$Y-r(\cos\theta,\sin\theta)$ 同样全平。
由此开盘与环域光滑连接；不是仅在一个边界圆上固定。

### 6.2 外端退化与 $C^2$ 竖直核心连接

外端必须另外核对，不由内点 turning 方程自动得到。
下面给出一组充分条件。
记 $d=R-r$，假设
$$
W=Bd^{-\alpha}(1+O(d^\sigma)),\qquad
\frac12<\alpha<1,\quad \sigma>1-\alpha,\quad B>0,     \tag{31}
$$
且一阶导数具有对应余项估计；选
$r=R-d_0x^m$、$m=1/(1-\alpha)>2$。
于是 $h_x\to c_0>0$、$h_{xx}\to0$，其中 $h'=-W$。
要求
$$
f(R,\theta)=0,\qquad P_c(r,\theta):=Wf_r
\text{ 在 }r=R\text{ 有 }C^1\text{ 延伸},              \tag{32}
$$
并要求足够的角向光滑性及相应混合导数一致性。
可明确取 $P_c$ 对 $(r,\theta)$ 为 $C^1$，其前两阶角导数也对 $r$ 为 $C^1$。

由
$f(r,\theta)=-\int_r^R P_c(t,\theta)/W(t)\,dt$，
$f=O(d^{1+\alpha})$、$f_r=O(d^\alpha)$，同类角导数也成立。
(22) 中的 $V-W^2$ 有 $C^1$ 极限 $-2P_c(R,\theta)$；
其中 $f_r^2=O(d^{2\alpha})$ 的一阶导数趋零，正是使用 $2\alpha>1$ 的地方。
同时 $b\to R$、$N\to1$，并有 $C^1$ 延伸。
对差量 $e$ 使用 (6) 的隐函数定理，得 $e,u,a$ 的 $C^1$ 延伸。
在准确解上 $Y_r=vT-uJT$ 有 $C^1$ 延伸且有界。
故
$$
Y_x\to0,\qquad
Y_{xx}=r_{xx}Y_r+r_x^2Y_{rr}\to0,
\qquad Z_x\to c_0,\quad Z_{xx}\to0.                 \tag{33}
$$
混合导数同样匹配。
这里 $r_{xx}\to0$ 使用 $m>2$；$Z_{xx}$ 的背景余项使用 $m\sigma>1$。
于是边界曲线可与同一平面曲线的竖直广义柱面 $C^2$ 连接。

核心极限具体为
$$
u_R^2=e_R+2P_c(R,\theta),\qquad
\left\langle(e_R+2P_c(R,\theta))^{-1/2}\right\rangle=1,
\qquad (\psi_\theta)_R=1/u_R.                        \tag{34}
$$
若选择 $\langle f\rangle=0$，则 $\langle P_c\rangle=0$。
这给出有限核心形状的准确边界通量，而不是只给椭圆的无限小方向。
例如给定任意同样反射及中心对称、周长 $2\pi R$ 的严格凸光滑核心，
以常速 $R$ 的弧长角参数写其正 turning 导数 $k(\theta)>0$、$\langle k\rangle=1$。
取
$$
u_R=1/k,\qquad e_R=\langle u_R^2\rangle,\qquad
P_c(R,\theta)=\frac{u_R^2-\langle u_R^2\rangle}{2}    \tag{35}
$$
便准确编码其核心端口。
这不证明该端口能被整张高度解实现；那仍是边值问题。

### 6.3 闭面是额外有条件结论

若上述内外端条件成立，核心高度为常数 $z_c>0$，且上半盘 $Z>0$，
则可反射得到下半盘 $(Y,-Z)$，再用核心曲线上的竖直柱面
$z\in[-z_c,z_c]$ 连接。
严格嵌套说明上、下盘的内部投影严格在核心凸体内部，柱面投影只在其边界；
正负高度分开两盘。
配合 (33)，得到连通闭合 $C^2$ 嵌入球面。
该闭面的材料度量在上、下盘为 (11)，在柱段为
$dz^2+R^2d\theta^2$，保持角平移对称。
但 $z_c$、包围球、条带、全局曲率、远点对 reach 和宏观相位位移均没有由此自动满足本题阈值。

## 7. 下一真实有限边值问题及固定 $g$ 的边界

本条给出可执行、非摄动的设计问题：选取全平背景 $h$ 与足够自由的非均值高度 $f$，
满足开平盘条件、(31)--(32)、核心通量条件以及 $b,N>0$；
逐圈用 (6) 设计 $E$，用 (21) 计算其准确导数，最后解
$$
\mathcal R(r,\theta)=0                              \tag{36}
$$
的全部非零角模。
核心 $j=2$ 通量可先从
$P_c(R,\theta)=-3\varepsilon\cos(2\theta)/R+\cdots$
开始；高次谐波应保留为真实未知数。
也可将 (35) 与 [R579的严格宏观核心](R579-smooth-thick-rounded-core-with-exact-perimeter-and-macro-budget.md)一起作为有限目标。
一个紧支撑背景控制可用于横截的幅度条件，但不自动支付高次模逆、整个尾部解或非线性收敛。

径向自由空间必须能包含已付的准确全平线性尾及其相容修正；
仅把单个平坦指数乘有限末端多项式，不因其形式光滑就包含真正的核。
角向离散也不能把某个固定有限 Fourier 高度截断的零残差当成完整非圆解。
后继实现可使用具无限角谱的解析非线性参数化及逐层加密，并始终从实际位置用 (28)--(29) 检查缺陷。
本条没有把任何有限离散拟合登记为准确解。

每次改变 $h,f$ 后重求 (6)，目标 $g$ 也随设计变化。
这是寻找一张静态旋转度量嵌入，不能冒充同一固定 $g$ 下的弯曲或精化序列。
只有选定完整 $E_*(r)$ 并冻结它之后，才可开展固定 $g_*$ 的精化、收敛及 reach 认证。
该阶段可把径向均值高度作为未知量来满足同一 turning 条件，
但其可解性、全平端点及加密收敛仍须实际支付；不能由本条的设计式直接继承。

最终若真得到一张满足全部闭面和定量几何条件的非轴对称解，
旋转材料相位给出的同度量族才可使用既登记的相位机制。
本条只完成有限高度方程与真实几何输出之间的严格接口；研究继续进入该边值问题。
