# R46：正角向第二形式的闭圈环带可在有限距离进入平坦开领

**已证明；完整独立审查通过。** 这是带两条边界的中间构造，不满足本题闭曲面完成标准。

作者：independent-geometry-continued-2。独立审查：tail-review-continued-2。root 全文复核并于 2026-11-09 登记。

固定作者稿 commit `0239fffd6e5206dfadb778db4ba5a057e01cfc5a`，blob `24c70487248a1766119cb06d1299d9686901205c`，见 [完整作者稿](../notes/2026-11-09-db6f-positive-epicycle-finite-flat-collar-v1.md)。完整独审 commit `e927f688421290880733e8de0ddc2d017ef8c574`，blob `0029b892d6801f19e4a7342a55051c185a2e1f76`，见 [逐节独立审查](../notes/2026-11-09-db6f-tail-review-positive-epicycle-finite-flat-collar-v1.md)。独审另冻结并实际以 JavaScript 隔离运行时独跑 63 项 BigInt 有理常数门，全部通过；这不等于 PDE、BVP 或几何轨迹运行，后三者本结论均为 0 次。

得到实际周期位置、共同度量、全时间嵌入及正 reach 的非全等环带族；有限径向位置后是开平坦仿射领。新族没有固定 H；旧 R44/R45 的握持区及 reach/D>0.03 不可转移。出口锥角严格小于 2π，第二基本形式仍为非零秩一形式，未匹配 R43、水平核心或闭合接口。时间长度及可见幅度尚未有效定量。

下文保留已冻结作者稿的完整证明；登记前 root 已通读其全部 13 节和上述完整独审。没有改换其构造、参数或证明身份。

---

# 正角向第二形式的闭合 epicycle：到有限平坦仿射领的真实延拓

**状态：新的完整作者存在性证明，待未参与者全文独审。**
2026-11-09，独立几何分工。本文不读取主优化数组，不运行 BVP、tail 或 RK。
它替换先前鞍环的球面种子与变形族；不是先前固定握持区族的直接延拓。
先前恢复版鞍环证明及其独审保持冻结。

本稿实际构造一个共同精确度量的 $C^\infty$ 嵌入环带族：从闭圈直纹鞍环
出发，在有限径向距离内进入一个开平坦领。空间圈对全部径向位置与全部
变形参数都真实闭合。两像非全等，不是单张曲面或只有局部形式可积性。

代价与边界同时明确：新族在角变量上解析，**不保留先前 bump 族的固定
开握持区**；本稿未安排新的 $H$。末端的平坦度量有仿射而非恒定斜率为
$1$ 的周长函数，其锥角在本构造中远小于 $2\pi$，第二基本形式不归零，
不能用作 R43 的欧氏平圆环出口。参数有效数值、可见振幅、闭曲面、按全
直径归一的 reach 门及网格都未支付。

## 1. 固定来源与证据范围

球面 epicycle 的路线参考 Bates–Melko，
*On curves of constant torsion I*（2012），§1 式 (1.1)、§2.1
Definition 2.1 和 §2.2 的 $(1,-3)$ 例子：
[原论文 HTML](https://arxiv.org/html/1206.7086v1)。
下文重新给出本坐标约定中的闭合、符号和嵌入证明；不把论文图示作为
嵌入证明，也不依赖其空间曲线的未展示长公式。

演化定理使用作者 Nishida 的 Orsay 78.02 讲义，
*Nonlinear Hyperbolic Equations and Related Topics in Fluid Dynamics*，
Chapter III §2，Hypothesis 2.1 与 Theorem 2.1，印刷 pp.64–65，
以及 pp.72–73 对仅演化变量连续的一阶拟线性系统的应用：
[作者讲义正文](https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/bb/b2/bbb2303a-1e17-4807-a319-290a5b030b2f/n_nishida-102.pdf)。
所用版本只要求演化变量连续；存在时间取决于解析尺度中的一致 Lipschitz
界、初始右端界和时间范围。它不取演化变量的高阶导数。
这里只在线读取文本，没有下载或渲染 PDF。

本文在终端环境不可用时作为新小文本保存。本文所用的一组 25 个基础有理界曾用会话内
纯 JavaScript BigInt 分数运算实际检查通过，另有 9 个端点与管界补充门通过；
这不是终端子进程，没有可报的
进程退出码，也没有已封存的源码哈希执行链。证明本身写出全部估计，可逐项
手核；不能把该检查当作本稿的独立程序重跑。本文也未调用 PDE 数值求解器。

## 2. 一个全圈角向系数严格同号的显式种子

固定 $b>0$。令

$$
\eta=\frac1{\sqrt2},\quad
D=1+6\eta-3\eta^2,\quad
p=\sqrt{\frac{2(1-\eta^2)}D},\quad q=\sqrt{1-p^2},\quad
\omega=\frac{2\pi}{3}.
\tag{1}
$$

$p,q>0$。取标准的 $R_z,R_y$，其中
$R_y(\gamma)(x,y,z)=(\cos\gamma\,x+\sin\gamma\,z,y,
-\sin\gamma\,x+\cos\gamma\,z)$。定义

$$
\bar d(\theta)=R_z(\theta)R_y(\pi/4)
       (p\cos3\theta,-p\sin3\theta,q),\qquad d_0=-\bar d.
\tag{2}
$$

整体负号用于把下文球面测地曲率取为正，不改变 $d_0\times d_0'$。
方向曲线为单位向量且有材料 C3。复水平分量为

$$
\bar d_W=\eta q\,e^{i\theta}
  +\frac{p(\eta-1)}2e^{4i\theta}
  +\frac{p(\eta+1)}2e^{-2i\theta},\qquad
\bar d_z=\eta(q-p\cos3\theta).
\tag{3}
$$

三个水平频率都模 $3$ 等于 $1$，竖直频率为 $0,\pm3$。
全圈向量面积的水平分量因 C3 为零，其竖直常数项为

$$
\eta^2q^2+\frac{p^2}2(\eta^2-6\eta+1)=0,
\tag{4}
$$

最后的等式正是 (1)。所以 $\int_0^{2\pi}d_0\times d_0'=0$。

记

$$
J(\theta)=(\eta-3)q-\eta p\cos3\theta,\qquad W=10-6\eta.
$$

则

$$
k_0^2:=|d_0'|^2=W-J^2,\qquad
\det(\bar d,\bar d',\bar d'')
 =J(19-9\eta-J^2)+3Wq=:\mathcal T.
\tag{5}
$$

一种短核算如下。在 $R_z(\theta)R_y(\pi/4)$ 的旋转坐标系内，
令 $v=(p\cos3\theta,-p\sin3\theta,q)$、
$w=(-\eta,0,\eta-3)$、$e=(0,0,1)$，则一阶导数为 $w\times v$，
二阶导数为 $w\times(w\times v)+3(e\times w)\times v$。
用 $|v|=1$、$w\cdot v=J$、$|w|^2=W$ 即得 (5)。

下面给出不用网格的宽有理界：

$$
.707<\eta<.708,\qquad .516<p<.518,\qquad .855<q<.857.
\tag{6}
$$

$\eta$ 的界可平方核；函数
$2(1-x^2)/(1+6x-3x^2)$ 在此区间递减，其导数分子为
$-4(3x^2-2x+3)<0$，所以 $p,q$ 的界也由有理端点平方核得。
由 (6)，

$$
j_-:=(.707-3)(.857)-(.708)(.518)<J
<j_+:=(.708-3)(.855)+(.708)(.518)<0.
$$

用有理多项式直接计算，有

$$
10-6(.708)-j_-^2>\frac3{10},\qquad W<6.
\tag{7}
$$

令 $C_-=19-9(.708)$、$Z_+=3(10-6(.707))(.857)$。
因为 $J<0$，

$$
\mathcal T\le J(C_--J^2)+Z_+.
$$

右侧作为 $J<0$ 的函数严格凸；在闭区间 $[j_-,j_+]$ 上其最大值
位于端点，而两个端点值都严格小于 $-1$。这只是两个有理三次式比较。
因此

$$
\boxed{\frac3{10}<k_0^2<6,\qquad \mathcal T<-1,\qquad
\kappa_0:=\frac{-\mathcal T}{k_0^3}>\frac1{15}.}
\tag{8}
$$

$\kappa_0$ 是 $d_0$ 按单位球面弧长定向后的测地曲率。
最后用到 $6\sqrt6<15$。整个全圈角向第二形式因此可避开零点。

## 3. 闭中心曲线的实际公式和严格嵌入

定义七个正系数

$$
\begin{aligned}
R&=\frac12+(3\eta-\tfrac34)p^2,&
P&=\frac{pq}{2}(\tfrac32+\eta),\\
A&=\frac{pq(1-\eta)^2}{4},&
B&=\frac{\eta p^2(1-\eta)}{28},&
C&=\frac{\eta p^2(1+\eta)}{20},\\
U&=\frac{\eta pq(3-2\eta)}3,&
V&=\frac{p^2}{24}.
\end{aligned}
\tag{9}
$$

零平均原函数 $c_0'=b\,d_0\times d_0'$ 恰为

$$
\begin{aligned}
-\frac{i}{b}(c_0)_W
 &=Re^{i\theta}+Ae^{4i\theta}+Pe^{-2i\theta}
      +Be^{7i\theta}+Ce^{-5i\theta},\\
\frac1b(c_0)_z&=-U\sin3\theta-V\sin6\theta.
\end{aligned}
\tag{10}
$$

例如直接从 (3) 得水平叉乘频率 $1,4,-2,7,-5$ 的系数分别为

$$
-R,\quad -4A,\quad 2P,\quad -7B,\quad 5C,
$$

竖直叉乘为 $-3U\cos3\theta-6V\cos6\theta$，所以 (10) 的每项
都可直接微分核验。它真正闭合且 $c_0(\theta+\omega)=R_z(\omega)c_0(\theta)$。

由 (6) 可得以下严格有理包络：

$$
.86<R<.88,\quad .48<P<.5,\quad
0<A<.01,\quad0<B<.003,\quad0<C<.017,\quad
U>.16,\quad0<V<.012.
\tag{11}
$$

令 $s=3\theta$、$x=\cos s$，并写

$$
r(s)=R+Pe^{-is}+Ae^{is}+Be^{2is}+Ce^{-2is}.
$$

则 $-i(c_0)_W/b=e^{i\theta}r(3\theta)$，且
$|r|>.33$、$|r|<1.41$。平方模为

$$
|r|^2=h_0+h_1\cos s+h_2\cos2s+h_3\cos3s+h_4\cos4s,
$$

其中

$$
\begin{aligned}
h_1&=2(CP+PR+RA+AB)>.8256,\\
h_2&=2(CR+PA+RB)<.0452,\\
h_3&=2(CA+PB)<.00334,\qquad
h_4=2CB<.000102.
\end{aligned}
$$

由 $|T_n'(x)|\le n^2$，得到

$$
\frac{d|r|^2}{dx}
>.8256-4(.0452)-9(.00334)-16(.000102)
=\frac{153277}{250000}>\frac35.
\tag{12}
$$

另一方面 $(c_0)_z/b=-\sin s\,(U+2V\cos s)$，其中

$$
U-2V>.136>.13.
\tag{13}
$$

若 $c_0(\theta)=c_0(\phi)$，由 (12) 得
$\cos3\theta=\cos3\phi$；由 (13) 和高度相同再得
$\sin3\theta=\sin3\phi$。故 $\theta-\phi$ 是 $2\pi/3$ 的整数倍。
这时水平坐标仅相差相应 C3 旋转，且 $|r|>0$，所以只有
$\theta=\phi\pmod {2\pi}$ 才能相等。中心曲线是实际嵌入圆周。

还可取得粗的全局 co-Lipschitz 常数。对任意两点，记空间弦长为 $d$。
由 (12) 及 $|c_W|<1.41b$，

$$
|\Delta\cos3\theta|\le \frac{47}{10}\frac db.
$$

再用高度及 (13)，

$$
|\Delta\sin3\theta|
\le\frac{1+.024(4.7)}{.13}\frac db
=\frac{214}{25}\frac db.
$$

两个常数的平方和小于 $100$，故
$|e^{3i\theta}-e^{3i\phi}|<10d/b$。同时
$P+A+2B+2C<.55$，所以

$$
|r(3\theta)-r(3\phi)|
\le .55|e^{3i\theta}-e^{3i\phi}|<5.5d/b.
$$

用水平位置式及 $|r|>.33$ 得
$|e^{i\theta}-e^{i\phi}|<20d/b$。
若 $\Delta_\theta\in[0,\pi]$ 是最短角距离，则
$\Delta_\theta\le(\pi/2)|e^{i\theta}-e^{i\phi}|<32d/b$，即

$$
|c_0(\theta)-c_0(\phi)|\ge \frac b{32}\Delta_\theta.
\tag{14}
$$

从 (2) 求两次导数有 $|d_0''|\le16$，故
$|c_0''|=b|d_0\times d_0''|\le16b$。
沿最短参数弧作 Taylor 余项估计，对任意单位中心曲线法向 $\nu$，

$$
2|\nu\cdot(q_1-p_1)|
\le \frac{16384}{b}|q_1-p_1|^2.
\tag{15}
$$

紧曲线最近点的法向条件加距离平方比较立即给出
$\operatorname{reach}(c_0)\ge b/16384$。此处中心曲线无边。

## 4. 一个保持球面长度与向量面积的真实角解析族

本节构造新族；不把先前非解析 bump 族用于解析 Cauchy 定理。

设 $T_0=d_0'/k_0$、$n_0=d_0\times T_0$。定义奇的解析周期函数

$$
h(\theta)=\sin6\theta-\mu(T_0)_z(\theta),\qquad
\mu=\frac{\int_0^{2\pi}\sin6\theta\,(T_0)_z\,d\theta}
          {\int_0^{2\pi}(T_0)_z^2\,d\theta}.
\tag{16}
$$

分母严格正：$(T_0)_z=-3\eta p\sin3\theta/k_0$。
$h\ne0$，因为在 $\cos3\theta=0$ 处 $\sin6\theta=0$ 而
$(T_0)_z\ne0$，两函数不可能为常数倍。
$h$ 与 $(T_0)_z$ 在 $d\theta$ 内积下正交。

对 $\tau\in\mathbb R$、$\alpha\in\mathbb R^2$ 令

$$
f_{\tau,\alpha}=\tau h+\alpha_1(d_0)_z+\alpha_2\kappa_0,\qquad
d_{\tau,\alpha}=\cos f_{\tau,\alpha}\,d_0+\sin f_{\tau,\alpha}\,n_0.
\tag{17}
$$

这些标量全都以 $\omega$ 为周期，因此方向场恒为单位向量并 C3 等变。
保持两个实约束：

$$
\int_0^{2\pi}(d_{\tau,\alpha}\times d_{\tau,\alpha}')_z\,d\theta=0,
\qquad
\int_0^{2\pi}|d_{\tau,\alpha}'|\,d\theta=\ell,
\quad
\ell:=\int_0^{2\pi}k_0\,d\theta.
\tag{18}
$$

水平向量面积对任意参数已由 C3 为零，所以这是完整闭合约束。

若 $\delta d=f n_0$，分部积分给向量面积变分
$-2\int f k_0 d_0$，长度变分为 $-\int f k_0\kappa_0$。
所以 (18) 对 $\alpha$ 的 Jacobian 为

$$
-\operatorname{diag}(2,1)\,G,\qquad
G_{ij}=\int_0^{2\pi}k_0 g_i g_j\,d\theta,\quad
(g_1,g_2)=((d_0)_z,\kappa_0).
\tag{19}
$$

两个函数线性无关。为作有理核查，在 $\cos3\theta=1$ 处，由 (6)
直接有 $k_0^2<2/5$、$|(d_0)_z|<1/4$，故
$|\kappa_0/(d_0)_z|>12$。
在 $\cos3\theta=-1$ 处，则 $k_0^2>3$、
$|(d_0)_z|>9/10$。此外 $|\mathcal T|<6$：
写 $a=-J>0$，用
$a(C-a^2)\le2C^{3/2}/(3\sqrt3)$、$C=19-9\eta<13$，
及 $3Wq>14$，即得
$-\mathcal T<2\cdot13(11/3)/5-14<6$。
因此第二点 $|\kappa_0/(d_0)_z|<2$。比值不恒定，故 $G$ 严格正定。

有限维解析隐函数定理于是给真实解析的 $\alpha(\tau)$，
$\alpha(0)=0$，使 (18) 对全部充分小 $\tau$ 精确成立。
由于 $h$ 为奇函数，而 $k_0,(d_0)_z,\kappa_0$ 为偶函数，
两个约束在自由方向 $h$ 上的一阶变分都是零，所以

$$
\alpha'(0)=0.
\tag{20}
$$

记 $d_\tau=d_{\tau,\alpha(\tau)}$、$k_\tau=|d_\tau'|$。
缩小参数范围，使 $k_\tau>0$、$\kappa_\tau>1/30$。
在一个共同复角条带和复参数小圆盘内，球面范数的平方根选取实轴正分支，
所有函数解析；这也说明这里的“解析 IFT”没有对模长作非全纯延拓。

## 5. 积分常数、材料坐标与正宽环带

令

$$
\widehat c_\tau(\theta)=b\int_0^\theta d_\tau\times d_\tau'\,dx,\qquad
c_\tau=\widehat c_\tau-\frac1{2\pi}\int_0^{2\pi}\widehat c_\tau\,d\theta.
\tag{21}
$$

由 (18)，$\widehat c_\tau$ 周期；(21) 指定了真实的零平均积分常数。
周期原函数的 C3 变换差为常数，取平均后该常数为零，所以
$c_\tau(\theta+\omega)=R_z(\omega)c_\tau(\theta)$。
这个积分常数按 $\tau$ 重新归一；没有把它预设为同一个固定空间锚点。

定义

$$
u_\tau(\theta)=\int_0^\theta k_\tau(x)\,dx,\qquad
u\in\mathbb R/\ell\mathbb Z,\qquad \theta=\theta_\tau(u).
\tag{22}
$$

总长度精确相同，且每扇区长度为 $\ell/3$。逆函数在共同复条带中解析，
并满足材料 C3 移位。令

$$
B_\tau(v,u)=c_\tau(\theta_\tau(u))+v\,d_\tau(\theta_\tau(u)).
\tag{23}
$$

若 $T=d_u$、$n=d\times T$，则 $c_u=bn$，所以

$$
g=dv^2+(b^2+v^2)du^2,\qquad
L=0,\quad M=-\frac b{\sqrt{b^2+v^2}},\quad
C_{\!II}=\sqrt{b^2+v^2}\,\kappa_\tau(u).
\tag{24}
$$

这三个二次型分量的结论对全部时间精确成立。

为给后面留统一余量，缩小参数范围，使

$$
\|c_\tau'-c_0'\|_\infty\le b/64,\qquad
\|c_\tau''-c_0''\|_\infty\le b,\qquad |d_\tau'|\le4.
$$

于是中心曲线弦长至少 $(b/64)\Delta_\theta$，二阶导数至多 $17b$，
由同一法向 Taylor 证明，其 reach 至少

$$
\rho=\frac b{69632}.
\tag{25}
$$

取 $w=b/10^6$。全部 $|v|\le2w$ 都在同一中心曲线正常管内，故 (23)
是全时间正宽嵌入；其共同材料宽度没有随时间改变。

还需一个对共同材料坐标的全局弦长常数。对两个带上位置 $x,y$，
令 $p_1,q_1$ 为其中心曲线足点。由 (15) 的扰动版及 $2w/\rho<1/5$，

$$
|p_1-q_1|\le\frac54|x-y|,\qquad
b\Delta_\theta\le80|x-y|,\qquad
|v-\widehat v|<3|x-y|.
$$

最短材料弧长差 $\Delta_u$ 不大于沿最短角弧积分的长度，
所以 $\Delta_u\le4\Delta_\theta$。故

$$
\sqrt{(v-\widehat v)^2+b^2\Delta_u^2}<321|x-y|.
\tag{26}
$$

这是空间弦长界，非只对局部微分的下界。

## 6. 新族不是重参数化或刚体运动

以下还证明完整延拓后两像不全等。先讨论中心的对称小环带。

度量 (24) 的曲率为 $-b^2/(b^2+v^2)^2$，严格确定 $|v|$。
所以对称环带上的任一内在自等距只能是
$(v,u)\mapsto(\epsilon v,\zeta u+\beta)$，
$\epsilon,\zeta=\pm1$：第一坐标由曲率确定；跨 $v=0$ 的光滑性固定符号；
比较 $dv^2$、$du^2$ 系数再给第二坐标的形式。

若任意小的非零参数序列产生与基础像刚体全等的环带，则取刚体正交部分、
材料移位的收敛子列；平移也因两紧像一致有界而有界。用极限基础对称消去后，
可得到趋于恒等的正交矩阵
$Q_j$ 与移位 $\beta_j$，满足

$$
Q_jD_{\tau_j}(u)=D_0(u+\beta_j),\qquad
D_\tau(u)=d_\tau(\theta_\tau(u)).
\tag{27}
$$

离散的径向和角向反射已在与极限对称复合后消去；这没有漏掉全
$\mathrm E(3)$ 中的反射。

线性映射
$(\Omega,\beta)\mapsto\Omega\times D_0-\beta(D_0)_u$
没有核。若 $\beta\ne0$ 且落在核中，方向曲线是某个固定旋转群的轨道，
球面曲率恒定，与 §4 两点的曲率界矛盾；若 $\beta=0$，则非恒定的
$D_0$ 迫使 $\Omega=0$。有限维单位球紧性给其范数的一致正下界。
对 (27) Taylor 展开，先由此得
$|\log Q_j|+|\beta_j|=O(|\tau_j|)$，再除以 $\tau_j$ 取极限，
说明 $\dot D_0$ 必是一个旋转加材料平移的一阶方向。

其球面法向分量因此必须属于
$\{\Omega\cdot T_0:\Omega\in\mathbb R^3\}$。
而由 (17)、(20)，重参数化只加切向分量，这一法向分量恰为 $h$。
$h$ 的 C3 周期性先迫使可能的 $\Omega$ 只有竖直分量：
对三次移位取平均，剩下的水平关系在 $\theta=0,\omega$ 处迫使水平系数零。
又由 (16) 的正交性，$h$ 不可能为 $(T_0)_z$ 的非零常数倍。
矛盾。故全部充分小的非零 $\tau$ 给出全 $\mathrm E(3)$ 下非全等的环带像。

这个证明的有限维切轨道估计可写得更明确：若
$s_j=|\log Q_j|+|\beta_j|$ 且 $|\tau_j|/s_j\to0$，
(27) 除以 $s_j$ 会产生一个非零核向量。故 $s_j=O(|\tau_j|)$；
此后参数有界，除以 $\tau_j$ 的子列极限合法。
所用基础曲率的非恒定性由 §4 也直接给出：
第一点 $\kappa_0>3$，第二点 $\kappa_0<6/5$。

## 7. 共同径向度量的实际平坦截止

余下先取 $b=1$；最后把空间位置统一乘 $b$ 即恢复尺度。
此时 $w=10^{-6}$，在 $r_0=w$ 处从 (23) 接出。记
$a_0=\sqrt{1+r_0^2}$、$a_1=r_0/a_0$。

选定一个明确 $C^\infty$ 截止 $0\le\psi\le1$，
在 $s\le1/4$ 为 $1$，在 $s\ge3/4$ 为 $0$。
例如令 $E(x)=e^{-1/x}$（$x>0$）及 $E(x)=0$（$x\le0$），取

$$
\psi(s)=\frac{E(3/4-s)}{E(3/4-s)+E(s-1/4)}.
$$

对待定的正数 $\delta\le w$，定义

$$
\begin{aligned}
a_\delta''(r)&=\frac{\psi((r-r_0)/\delta)}{(1+r^2)^{3/2}},\\
a_\delta(r)&=a_0+a_1(r-r_0)
       +\int_{r_0}^r(r-s)a_\delta''(s)\,ds .
\end{aligned}
\tag{28}
$$

于是 $a_\delta=\sqrt{1+r^2}$ 在 $r\le r_0+\delta/4$ 的邻域，
而在 $r\ge r_*=r_0+3\delta/4$ 为正的仿射函数。
所有截止 jet 光滑。整个固定时间窗 $|r-r_0|\le1/4$ 内，
不论 $\delta$ 多小，都有一致界

$$
\frac12<a_\delta<2,\qquad |a_\delta'|<1,\qquad
|a_\delta''|\le1.
\tag{29}
$$

这些界不含截止的三阶或更高导数。我们不会假设那些高导数对
$\delta\to0$ 一致有界。

共同度量选为

$$
g_\delta=dr^2+a_\delta(r)^2du^2.
\tag{30}
$$

它在旧环带上恰为 (24)，在有限位置 $r\ge r_*$ 上恰有 $K=0$。
尚需证明这个指定度量和指定初始全圈位置真的可实现，不能只检查曲率。

## 8. Gauss–Codazzi 的明确演化及统一 CK 寿命

在坐标 $(r,u)$ 写第二形式为 $(L,M,C)$。Gauss 方程消去 $L$：

$$
L=\frac{M^2-a_\delta a_\delta''}{C}.
\tag{31}
$$

两条 Codazzi 方程恰为

$$
M_r=L_u-\frac{a_\delta'}{a_\delta}M,\qquad
C_r=M_u+\frac{a_\delta'}{a_\delta}C+a_\delta a_\delta' L.
\tag{32}
$$

初值是同一实际嵌入环带在 $r_0$ 的第二形式：

$$
M(r_0,u,\tau)=-1/a_0,\qquad
C(r_0,u,\tau)=a_0\kappa_\tau(u)>1/30.
\tag{33}
$$

这不是任意选择一条新 Cauchy 曲线；全部初始位置、标架和两 jet 都由
(23) 确定。式 (31) 在初始点给 $L=0$。

下面逐项验证所引定理，并处理 $\delta$ 的循环问题。
初值 $\mathcal U_0=(M_0,C_0)$ 对周期变量 $u$ 和小参数 $\tau$ 在共同
复邻域解析。可选 $\rho_0,\tau_0>0$，令它在
$|\operatorname{Im}u|<2\rho_0,|\tau|<2\tau_0$ 内有有限范数 $B$，
且在较小邻域上 $|C_0|\ge1/60$。令 $c=1/120$，选未知增量
$\mathcal V=\mathcal U-\mathcal U_0$ 的球半径 $\mathcal R\le c$。

取 Banach 尺度 $X_\rho$：在
$|\operatorname{Im}u|<\rho,|\tau|<\tau_0$ 上有界全纯、以 $\ell$ 为周期
的二分量函数，范数为最大分量上确界，$0<\rho<\rho_0\le1$。
这是一个范数次乘性的代数，且

$$
\|\partial_u f\|_{\rho'}\le
\frac{\|f\|_\rho}{\rho-\rho'}\quad(0<\rho'<\rho).
\tag{34}
$$

在 $\|\mathcal V\|_\rho<\mathcal R$ 内，$|C|\ge c$；
令 $B_1=B+\mathcal R$，则

$$
|L|\le L_*:=\frac{B_1^2+2}{c}.
\tag{35}
$$

把 (32) 写为 $\mathcal U_r=A_\delta(r,\mathcal U)\mathcal U_u+
B_\delta(r,\mathcal U)$，其实际系数为

$$
A_\delta=
\begin{pmatrix}2M/C&-(M^2-a_\delta a_\delta'')/C^2\\1&0\end{pmatrix},
\quad
B_\delta=
\begin{pmatrix}
-(a_\delta'/a_\delta)M\\
(a_\delta'/a_\delta)C+a_\delta a_\delta'L
\end{pmatrix}.
\tag{36}
$$

(29) 与 $|C|\ge c$ 给 (36) 及其关于 $(M,C)$ 的一阶导数一个
仅依赖 $B_1,c$ 的上界；例如可统一取
$\Lambda=100(1+B_1)^3(1+c^{-3})$。
初值在更宽条带解析，故
$\|(\mathcal U_0)_u\|_\rho\le B/\rho_0$。
代入 (34)，得到增量右端 $\mathcal F_\delta$ 的一致估计

$$
\begin{aligned}
\|\mathcal F_\delta(r,V)-\mathcal F_\delta(r,W)\|_{\rho'}
 &\le \frac{C_*}{\rho-\rho'}\|V-W\|_\rho,\\
\|\mathcal F_\delta(r,0)\|_\rho&\le K_*,
\end{aligned}
\tag{37}
$$

其中可取 $C_*=\Lambda(2+\mathcal R+B/\rho_0)$、
$K_*=\Lambda(1+B/\rho_0)$。常数同时对所有小 $\delta$ 一致。
系数关于 $r$ 连续，关于解析变量与未知量全纯；(37) 正是 Nishida
Hypothesis 2.1 的尺度条件，初始右端的有界性还强于所需的
$K/(\rho_0-\rho)$ 型界。

由该 Theorem 2.1，存在一个 $T_*>0$，它只依赖上述共同常数、
$\rho_0,\mathcal R$ 和固定时间窗，**不依赖 $\delta$ 或截止高导数**，
使每个 $\delta$ 的 (31)–(33) 都在
$|r-r_0|<T_*$ 的较窄条带中唯一可解。
现在再选

$$
0<\delta<\min(w,T_*/2).
\tag{38}
$$

因此平坦截止位于一个已经一致存在的解区间内；没有先选截止再假定
其 CK 寿命长过截止的循环。$C$ 在实变量上保持正，$|M|>1/2$，
因为 $\mathcal R\le1/120$ 且 $M_0=-1/a_0<-2/3$。

对每个固定 $\delta$，系数关于 $r$ 为 $C^\infty$；
在进一步缩窄的解析条带上反复微分 (32)，得解关于 $r$ 为 $C^\infty$。
$\tau$ 是上述 Banach 空间的全纯被动变量，迭代极限对它仍全纯；
故解关于全部实变量联合 $C^\infty$，参数区间可一次取共同闭子区间。
现实性、$\ell$ 周期性和 $\ell/3$ 的 C3 周期性由唯一性保持。

## 9. 标架与位置的真实单值性

不能只写“Gauss–Codazzi 可积”而略过全圈位置。令
$e_1=F_r,e_2=F_u/a,N=e_1\times e_2$。
先用旧曲面在 $r_0$ 的实际位置和标架作初值，然后按 $r$ 解

$$
F_r=e_1,\quad
(e_1)_r=L N,\quad
(e_2)_r=(M/a)N,\quad
N_r=-L e_1-(M/a)e_2.
\tag{39}
$$

这是光滑系数的线性标架 ODE 加位置积分。其正交性由反对称系数保持。
Gauss–Codazzi (31)–(32) 正是下列 $u$ 方程与 (39) 的相容条件：

$$
\begin{aligned}
F_u&=ae_2,\\
(e_1)_u&=a'e_2+M N,\\
(e_2)_u&=-a'e_1+(C/a)N,\\
N_u&=-M e_1-(C/a)e_2 .
\end{aligned}
\tag{40}
$$

例如把 (40) 的每个误差对 $r$ 求导，利用 (31)–(32)，得到齐次线性
误差系统；初值误差为零，故它们处处为零。因此诱导度量恰为 (30)。

所有初始位置和标架都是 $\ell$ 周期，(39) 系数也周期，ODE 唯一性
直接给 $F(r,u+\ell,\tau)=F(r,u,\tau)$，而不只有标架回转平凡。
同理有
$F(r,u+\ell/3,\tau)=R_z(\omega)F(r,u,\tau)$。
由 (21) 指定的积分常数、初始实际位置和 (39)，没有额外的平移 monodromy。

在 $r_0\le r\le r_0+\delta/4$ 上 $a$ 恰为旧函数，
旧第二形式也满足 (31)–(33)，故解析尺度唯一性给两者相同；
再由 (39) 的唯一性，位置也相同。因此新旧图在一个开环领上重叠，
接合是 $C^\infty$ 的，不是仅匹配有限 jet。

## 10. 全时间嵌入及带边 reach

固定材料域为
$[-w,w+\delta]\times(\mathbb R/\ell\mathbb Z)$。
其中 $r\le r_0$ 用旧图，另一侧用 (39)。全族使用同一个
$\ell,\delta,a_\delta$。

用旧公式 $B_\tau(r,u)$ 作为比较图，它在 $|r|\le2w$ 已嵌入；
由 (26)，$b=1$ 时其全局参数 co-Lipschitz 常数可取
$\gamma=1/321$。在新领上，旧 $r$ 切向为 $D_\tau(u)$；
由 (39) 和 (35)，

$$
|F_r-(B_\tau)_r|\le L_*\delta.
$$

又由 (40)，$F_{ur}=a'e_2+MN$，而 $(B_\tau)_{ur}=T_\tau$。
在初始圈 $F_u=(B_\tau)_u$，故

$$
|F_u-(B_\tau)_u|\le(B_1+2)\delta.
$$

令 $C_1=L_*+B_1+2$。进一步缩小同一个 $\delta$，使

$$
\delta C_1<\gamma/2.
\tag{41}
$$

这些界仅用 (29)、(35)，仍不含截止高导数。
在共同参数域上沿最短 $u$ lift 的直线段积分导数差，
结合旧全局弦长界，得到

$$
|F(P)-F(Q)|\ge\frac{\gamma}{2}|P-Q|_{\rm lift}.
\tag{42}
$$

所以全部时间都是嵌入，并非仅由局部浸入性推断。

还可完整处理边界的 reach。从 (39)–(40)，

$$
|F_{rr}|\le L_*,\quad |F_{ru}|\le1+B_1,\quad
|F_{uu}|\le2+B_1.
$$

故方向 Hessian 范数可统一取
$M_*=L_*+4+3B_1$。若 $p=F(P)$ 是任意空间点 $z$ 的最近曲面点，
即使 $P$ 在两条边界之一，通向任一 $Q$ 的可行参数线段也给

$$
(z-p)\cdot DF(P)(Q-P)\le0.
$$

Taylor 余项和 (42) 因而给

$$
(z-p)\cdot(F(Q)-p)
\le\frac{|z-p|}{2}\,M_*\frac4{\gamma^2}|F(Q)-p|^2.
$$

最近点距离小于 $\gamma^2/(4M_*)$ 时，距离平方比较严格排除第二最近点。
紧性保证最近点存在，故

$$
\operatorname{reach}(F_\tau)\ge
\frac{\gamma^2}{4M_*}>0
\quad\text{对全部时间}.
\tag{43}
$$

这里已保留 co-Lipschitz 常数平方，并使用边界处单侧可行导数，
没有套用无边曲面的法向条件。恢复空间尺度 $b$ 后，下界乘 $b$。
此界依赖解析数据的有限常数，当前没有数值化，也不声称达到 $0.03D$。

## 11. 完整环带的非全等与未继承的握持区

§6 的非全等也能作用于完整延拓图，而不假定刚体必须保存我们的人为拼接线。
在旧中心环带，$K=-1/(1+r^2)^2$。新领 $r\ge w$ 上，
$a\ge1$，且 $a''\le(1+r^2)^{-3/2}$，所以

$$
|K(r)|\le(1+w^2)^{-3/2}
<(1+w^2/4)^{-2}.
$$

最后一个严格不等式对 $0<w\le1$ 可平方后作有理多项式比较。
因此由内在曲率阈值
$K<-(1+w^2/4)^{-2}$ 恰好识别出中心开环带 $|r|<w/2$。
任何整体欧氏全等诱导的内在等距都必须保留该集合，继而限制为 §6
已经排除的中心环带全等。故完整延拓族也在全 $\mathrm E(3)$ 下非平凡。
两紧像上的最小刚体 Hausdorff 距离能在有界平移和紧正交群上取到，
所以非零小参数给严格正的商像距离，未给有效幅度界。

新族没有固定扇区 bump：控制函数在整个角圈解析，(21) 的空间积分常数也
按参数重新归一，未要求固定。因此先前恢复版鞍环的固定 $H$ 不能搬到本文。
这里没有提供满足握持条件的开集合，也没有以材料点运动替代像 Hausdorff
变化量。后续若要满足题目，必须另造相容的固定区及其接线。

## 12. 有限平坦领到底是什么

在 $r\in[r_*,w+\delta]$，(28) 给

$$
a(r)=A_\delta+B_\delta(r-r_*),\qquad B_\delta>0,\qquad K=0.
$$

斜率有 $B_\delta\le a_1+\delta<2w$，而由 (8)
$\ell<2\pi\sqrt6<16$，所以其锥角满足

$$
0<B_\delta\ell<32w=32\cdot10^{-6}\ll2\pi.
\tag{44}
$$

把 $\rho=a/B_\delta$、$\varphi=B_\delta u$ 作为局部平面极坐标，
可见这是具有该锥角的平坦环领；它不是全角 $2\pi$ 的欧氏平圆环。
不是只说“锥角也许不同”：在本参数选择下它严格不同。

此外 $C\ge c>0$、$|M|>1/2$，Gauss 方程在平坦领给
$L=M^2/C>0$。第二基本形式是非零的秩一形式，未归零。
因此该端既不匹配 R43 平领的指定度量与全两 jet，也不自动匹配水平核心。
没有在这里套用 R42 的正 C 条件作为 R43 那些角零点的延拓定理。

本稿新增的严格内容是：一个实际闭圈且全时间嵌入的角解析非刚体族，
能在**有限径向距离**由严格负曲率进入开平坦领，保留真实周期位置、
材料 C3、共同精确度量及正 reach；截止可以在已证明统一存在的时间内完成。
仍未得到闭曲面、固定握持区、可见幅度、目标归一 reach 或可用的 R43/核心
接合。这些缺口没有被本存在性结论消去。

## 13. 复核提示

有限代数部分的关键检查链为：

1. (3) 的零频项给 (4)，叉乘积分给完整位置 (10)。
2. 旋转坐标中的 $w\times v$ 与二阶导数给 (5)，凸三次式端点给 (8)。
3. 有理系数包络 (11) 给径向单调 (12)、高度符号 (13) 和弦长 (14)。
4. 两个约束的 Jacobian 是已证明严格正定的 Gram 矩阵，不以数值行列式替代。
5. (36) 的解析尺度界只用 $a,a',a''$，所以 (38) 的共同截止长度可真正选择。
6. 位置周期由 (39) 的逐点 ODE 唯一性获得，不止是形式 Gauss–Codazzi。
7. (42)–(43) 对同一个固定宽度、同一个参数区间和整个有边环带成立。

本文没有声称一个未给出的 PDE 数值轨迹已执行。可执行复算程序、有效
$\tau$ 区间和 $\delta$ 数值应在终端恢复后另建证据链；不能回填旧脚本
退出作为这项新构造的运行证明。
