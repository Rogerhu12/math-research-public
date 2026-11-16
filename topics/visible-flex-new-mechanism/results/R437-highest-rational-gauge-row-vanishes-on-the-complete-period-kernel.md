# R437：最高有理规范行在完整周期齐次核上恒零

日期：2026-11-16。**完整原式纸面证明。没有执行新的符号程序、积分、数值秩、profile 评价或研究计算。**

本稿消费 [R326](R326-one-global-second-gauge-pays-the-complete-rational-port-and-preserves-joint-cost.md) 与 [R327](R327-analytic-packet-period-kernels-and-a-finite-same-gauge-joint-system.md) 的同一个真实二阶规范、同一个周期算子及原十三行，不增加可控变量。结论是一条明确的行恒等式：

$$
\boxed{
P_{2,\theta}(k)=\frac{\kappa}{24}I_2\{Y(f,f),k\},
\qquad Y=\Phi_{p_2}.
}
\tag{1}
$$

右侧不依赖相位。对 R327 的全部紧周期齐次核，这一行准确为零。因此十三行矩阵不能满行秩；其底部十行的核像也不能是整个十维空间。这里没有宣称其余十二行独立或已可同时支付。

更具体地，只要两个真实周期特解存在，保持周期不变的任何后续规范都无法改变
$$
I_2\{Y(f,f),k_d\},\qquad I_2\{Y(f,f),k_e\}.
\tag{2}
$$
指定有理端口与整个第四周期同时可解，必先使这两个标量为零。其实际值未由本稿计算，不能把它们假定为零。

来源另为 [R259 原 E8 算子与尾](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R291 完整 cubic 身份](R291-exact-positive-Gaussian-square-moment-is-the-leading-energy.md)及 [R394 同规范条件接口](R394-conditional-complete-period-and-finite-same-gauge-interface.md)。R291 的原身份在下文重新给出不除以物理坐标的证明。

## 1. 保留真实固定输入

固定原实际几何及一个已安装的二次高度端口：
$$
M_{\rm total}=0,\qquad T_{\rm total}=\tau\mathfrak H,\qquad \tau\ne0,
$$
$$
h=H(1+\varepsilon\sigma^2),\qquad H>0,\quad
\varepsilon>0,\quad k=\kappa\ne0,\quad\omega=0.
\tag{3}
$$
令
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta,\qquad
\Delta=f\odot f-g\odot g.
$$
$\odot$ 是原对称二次槽。原三矩圆及完整第三 range 已按原构造支付。全部原函数仍用同一个共同右锚；后续二阶补偿 $k_\theta$ 是沿整个实际闭几何使用的同一紧 profile 家族。

原外矩为
$$
I_2(a,b)=\int_I\{x^2a''b''+2a'b'\}.
\tag{4}
$$
特别保留第二项。$Y(f,f)$ 一般具有真实二次左尾，以下没有将它截断或重锚。

把实际最细包写为
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad a_i\ne0,
\tag{5}
$$
支撑严格不交且有正间隙。所有八复制、十二复制、真实中心、宽度和幅度已经包含于(5)。采用 R327 的核分类条件：各包内 $f'$ 的零点有限阶，且 $A_f=6f'f'''-2(f'')^2$ 没有开零集。原解析包满足此条件；具有有限简单退化点的后续共同外 cap 库也可直接消费这一分类。

不允许以分别改变 incoming history、端口几何或目标函数的方式解释同一个齐次核列。

## 2. 原 cubic 恒等式，包含单包真实左尾

对任意紧 $u$，记 $p=u'$、$r=u''$。原同锚二次式为
$$
Y(u,u)
=-xu^2+x^2up-\frac{x^3}{2}p^2
-\frac{x^2}{4}J(x^2r^2+2p^2),
\qquad
J(F)(x)=\int_x^{r_*}F.
\tag{6}
$$
因此一个非零实包的左尾通常是
$$
-\frac{x^2}{4}I_2(u,u).
\tag{7}
$$
本节不要求单包三矩为零。

R259 的完整原二导配对与同锚分部积分给
$$
F_{Y,1}(u)=I_1\{u,Y(u,u)\}=\int_I f_1,
$$
$$
f_1=x^2ur^2-x^3pr^2+\frac{x^4}{6}r^3
+2up^2-\frac{2x}{3}p^3.
\tag{8}
$$
原代数导子 $\mathscr D u=x^2u'-2xu$ 满足 $\delta Y=0$。R259 的完整外矩递推因此是
$$
F_{Y,2}(u)=\int_I\mathscr V f_1,
$$
$$
\mathscr V f=-x^2f_x-2xf-2xu f_u-2u f_p+(2xr-2p)f_r.
\tag{9}
$$
这条递推已经保住非紧 $Y(u,u)$ 的左尾：另一个外槽 $u$ 及其所有端 jets 为零。

将(8)逐项代入(9)，得到准确总导数
$$
\begin{aligned}
\mathscr V f_1
={}&-4x^2upr+4x^3p^2r-4xup^2-8u^2p+2x^2p^3\\
={}&\frac d{dx}
\left(-2x^2up^2+\frac43x^3p^3-\frac83u^3\right).
\end{aligned}
\tag{10}
$$
原紧端使边项为零，故
$$
\boxed{F_{Y,2}(u)=I_2\{u,Y(u,u)\}\equiv0.}
\tag{11}
$$
这个证明不除以 $x$，也不需要物理区间避开零。它与 R291 的原能量证明给出同一个完整身份。

对任意另一个紧 $k$，在真正紧的族 $u+tk$ 上微分(11)：
$$
\boxed{
2I_2\{u,Y(u,k)\}=-I_2\{k,Y(u,u)\}.
}
\tag{12}
$$
这里只有输入 $u,k$ 被要求紧；输出 $Y(u,u)$ 保留(7)。没有在两个带尾方向上错误使用紧变分。

## 3. 完整最高有理行与相位无关

R326 定义的原线性系数是
$$
H_{X,j,\theta}(k)
=-I_j(XD_\theta,k)+2I_j\{\phi_\theta,X(\phi_\theta,k)\}.
\tag{13}
$$
用(12)，并保留准确二次槽恒等式
$YD_\theta+Y(\phi_\theta,\phi_\theta)=Y(f,f)$，立即有
$$
\boxed{
H_{Y,2,\theta}(k)=-I_2\{Y(f,f),k\}.
}
\tag{14}
$$
这是对任意紧 $k$ 的原函数配对身份，尚未要求 $L_f(k)=0$ 或三条直接矩为零。

再回 R326 的完整有理展开：
$$
\begin{aligned}
P_{\ell,\theta}(k)=[h^\ell]\bigg[
&2H\varepsilon\{
\mathcal T_h^\#(k;D_\theta)
-2\mathcal T_h^\#(\phi_\theta;\phi_\theta,k)\}\\
&+\sum_{p=-3}^{1}
\left\{\frac{1+\kappa^2}{4}h^{p-1}H_{A_p,0,\theta}(k)
-\frac\kappa2h^pH_{A_p,1,\theta}(k)
+\frac14h^{p+1}H_{A_p,2,\theta}(k)\right\}
\bigg].
\end{aligned}
\tag{15}
$$
原 local pairing $\mathcal T_h^\#$ 的幂仅为 $h^{-4},\ldots,h^0$。此处沿用 R259 的 $Y=\Phi_{p_2}$：R321 §1 及 R326 式(28)前把同一方向另记为 $V=p_2$，并把 $p_1$ 记为 $P_1$；该局部 $V$ 不同于 R259 的 $V=\Phi_{p_1}$。R312 式(16)的原 $\mathsf Q$ 末项直接写为 $-\kappa h_e(\sigma+\varepsilon\sigma^3/3)\Phi_{p_2}/2$，也确认这一对应。真实 centered history 的最高方向是
$$
A_1=-\frac{\kappa}{6}Y.
\tag{16}
$$
所以 $h^2$ 唯一来自(15)中 $p=1$ 的第三项；没有 local pairing 或其他 $A_p$ 槽可以贡献：
$$
P_{2,\theta}(k)
=\frac14H_{A_1,2,\theta}(k)
=-\frac{\kappa}{24}H_{Y,2,\theta}(k).
\tag{17}
$$
(14)与(17)证明(1)，包括系数、符号和完整相位。

R326 已证明反正切项与有理项的独立性，并保留完整三维 $\mathcal W_e$。这里的项在原 ruling 中是 $2\sigma h^2P_{2,\theta}(k)$。它属于奇部，不能由第三规范的偶 $\mathcal W_e$ 初值支付。因此(1)给出的必要行没有被既有 Gram 调整取消。

## 4. 它杀掉全部周期齐次核

记
$$
L_f(k)=\mathfrak H(k;f,f),\qquad
\ell_f(k)=I_2\{Y(f,f),k\}.
\tag{18}
$$
R327 的完整核分类为
$$
\ker L_f
=\operatorname{span}\{u_i,\chi_i\}_i\oplus\mathscr G,
\tag{19}
$$
其中 $\chi_i$ 在第 $i$ 个包的邻域为1，在其他包附近为0，变化只发生在间隙；$\mathscr G$ 是在全部包上为零的紧光滑函数。该分类已保原右锚、两个求导积分常数及有限阶临界点的光滑跨接。

### 4.1 母函数列

由于不交输入的原二次交叉密度为零，
$$
Y(f,f)=\sum_j a_j^2Y(u_j,u_j).
$$
在 $u_i$ 支撑上，其他项要么为原右零，要么为真实二次多项式尾。对任意紧 $v$ 和任意二次多项式 $q=Ax^2+Bx+C$，
$$
I_2(v,q)=2A\int x^2v''+2\int v'(2Ax+B)=0.
\tag{20}
$$
两个非零积分分别是 $4A\int v$ 与 $-4A\int v$。因此
$$
\ell_f(u_i)=a_i^2 F_{Y,2}(u_i)=0.
\tag{21}
$$
没有将右方单包的三矩置零。

### 4.2 平台列

原 adjoint 是
$$
L_2=x^2\partial_x^4+4x\partial_x^3,
\qquad
I_2(v,k)=\int kL_2v
\quad(k\text{ 紧}).
\tag{22}
$$
特别保留 $4x$ 中的 $x$。一个原二次尾在 $L_2$ 下为零。又
$$
\int L_2v=
[x^2v'''+2xv''-2v'].
\tag{23}
$$
对(7)中的纯 $x^2$ 左尾，(23)的括号准确为零；右零 collar 的括号也为零。于是
$$
\ell_f(\chi_i)=0.
\tag{24}
$$
这也正是 R327 原平台表中
$\ell_{Y,2}(\mu)=q_{Y,2}(\mu)=0$。这里并未说其他平台行都零；一般二次尾的线性项在(23)中会留下贡献。

### 4.3 间隙列及矩阵结论

对 $\eta\in\mathscr G$，$\eta$ 所在的每个间隙上 $Y(f,f)$ 都是一个真实二次多项式，故(20)或(22)给
$\ell_f(\eta)=0$。结合(19)—(24)：
$$
\boxed{\ell_f|_{\ker L_f}=0.}
\tag{25}
$$

因此 R327 的实际 $13\times2n$ 矩阵 $C_\theta$ 满足
$$
\boxed{\text{其 }P_2\text{ 行逐列恒为零，对全部 }\theta.}
\tag{26}
$$
总行秩至多12，底部十行的秩至多9；这里只给上界。真实八复制、十二复制的矩分离、更多包或更多不同中心，都不能使这一零行变成非零。并不因此断言其他行已经有共同右逆，或不存在别的行关系。

## 5. 两个 period 特解的不可调兼容条件

仍用 R326 的实际 incoming 矩阵
$$
X=\Phi_{\mathsf m_*}.
$$
它来自此前完整路径，已冻结。端口清理规范 $w_\theta^c=-XD_\theta$ 改变的两个真实周期目标是
$$
V_d^c=V_d-2\tau L_f(X\Delta),\qquad
V_e^c=V_e+2\tau L_f(X(f,g)).
\tag{27}
$$

先假设两个完整紧特解确实存在：
$$
L_f(k_d)=-\frac{V_d^c}{2\tau},\qquad
L_f(k_e)=-\frac{V_e^c}{2\tau}.
\tag{28}
$$
平台、总通量、全部内部退化点及平端逆解等原 range 条件，仍必须用于证明这个假设；本稿不从有限矩阵推出(28)。

周期方程的方便特解为
$$
k_\theta^0=\sin^2\theta\,k_d+
2\sin\theta\cos\theta\,k_e.
\tag{29}
$$
任何另一个周期解与它之差都属于(19)，所以由(1)、(25)，
$$
P_{2,\theta}(k_\theta)
=\frac{\kappa}{24}\{
\sin^2\theta\,\ell_f(k_d)
+2\sin\theta\cos\theta\,\ell_f(k_e)\}.
\tag{30}
$$
故在已经有(28)的前提下，存在同一个相位家族同时解周期及这一最高有理行，恰好等价于
$$
\boxed{\ell_f(k_d)=\ell_f(k_e)=0.}
\tag{31}
$$
充分性在本行范围内直接取(29)，它也具有准确的周期及 $0,\pi$ 两种子；不由此授予其他十二行。

两个值与紧特解的选取无关。等价地，(25)在真实像空间上定义线性泛函
$$
\mathfrak p_f:\operatorname{Im}(L_f|_{C_c^\infty(I)})\longrightarrow\mathbb R,
\qquad
\mathfrak p_f(L_fk)=\ell_f(k).
\tag{32}
$$
它是由完整原配对定义的 period 像泛函；没有在目标空间外延拓，也没有用未支付的 profile 矩自由度代替它。(31)可写为
$$
\mathfrak p_f\!\left(-\frac{V_d^c}{2\tau}\right)=
\mathfrak p_f\!\left(-\frac{V_e^c}{2\tau}\right)=0.
\tag{33}
$$

R327 的完整有限 iff 现可保原样读取：先付(28)与(31)，再对余十二行检验同一个核系数家族的线性方程、相位光滑性、周期和种子条件。相位秩降点的可除性条件没有被删除。

## 6. Incoming history 的贡献不能免费改掉

三矩使 $X\Delta$ 和 $X(f,g)$ 都是真紧函数。若用未施端口清理的 canonical 目标
$$
G_d^0=-V_d/(2\tau),\qquad G_e^0=-V_e/(2\tau),
$$
则(27)准确给
$$
G_d^c=G_d^0+L_f(X\Delta),\qquad
G_e^c=G_e^0-L_f(X(f,g)).
\tag{34}
$$
所以 canonical 与清理后的目标是否落入紧 $L_f$ 像是等价问题，但这不表示(33)的数值保持不变。只要它们在像内，
$$
\boxed{
\begin{aligned}
\mathfrak p_f(G_d^c)
&=\mathfrak p_f(G_d^0)+I_2\{Y(f,f),X\Delta\},\\
\mathfrak p_f(G_e^c)
&=\mathfrak p_f(G_e^0)-I_2\{Y(f,f),X(f,g)\}.
\end{aligned}}
\tag{35}
$$
这两项是完整二次输出的四次配对。R326 的八复制 cubic 零式不能直接删除它们。它们也不是两个新增独立控制参数：同一个实际 $\mathsf m_*$ 同时进入端口规范、两个周期目标以及其他原 joint 条件。

本稿没有断言(35)非零，也没有证明其值可调。它完成的是一条全核零行和对应的两个真实、特解无关的兼容条件。其余规范矩阵像、完整 actual cap 目标、共同十三行和其他几何段 ruling 仍各保原有未付边界。
