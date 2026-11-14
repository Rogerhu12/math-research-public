# R2：二、三角模混合产生横向中心漂移的精确局部环带

日期：2026-11-14。作者：`/root/mechanism`，AI 辅助研究。

**状态：已证明。** 本结果构造一个真正的局部解析等距嵌入环带，并证明其材料圆周平均中心具有非零横向加速度。它尚无两个圆领、没有固定帽，不能作为闭曲面或主课题达标结果。它给 R1 偏心端口路线提供一个具体而非纯形式的破对称种子。

## 1. 精确凸初始圈与材料角

固定 $a_0>0$，以及实数 $A,B$ 满足 $|A|+|B|<1$。令

$$
\rho(\varphi)=a_0(1+A\cos2\varphi+B\cos3\varphi),
\quad
T(\varphi)=(\cos\varphi,\sin\varphi,0),
\quad
\nu(\varphi)=(-\sin\varphi,\cos\varphi,0).
\tag{1}
$$

因为 $\rho>0$、且 $\rho$ 的一阶 Fourier 模为零，按

$$
\frac{d\gamma}{d\varphi}=\rho(\varphi)T(\varphi)
\tag{2}
$$

积分得到一条闭合严格凸的解析平面曲线，长度为 $2\pi a_0$。一个明确的原函数是

$$
\begin{aligned}
\gamma_x/a_0={}&(1+A/2)\sin\varphi+(A/6)\sin3\varphi
 +(B/4)\sin2\varphi+(B/8)\sin4\varphi,\\
\gamma_y/a_0={}&(-1+A/2)\cos\varphi-(A/6)\cos3\varphi
 +(B/4)\cos2\varphi-(B/8)\cos4\varphi,\\
\gamma_z={}&0.
\end{aligned}
\tag{3}
$$

闭合由直接求导和 $2\pi$ 周期性可核。严格凸性也可直接看出：从任一切线方向 $\varphi_0$ 出发，曲线相对该切线的法向投影之导数是 $\rho(\varphi)\sin(\varphi-\varphi_0)$，在两个半圆上先严格同号、后严格反号，且闭合时回到零。因此除起点外整条曲线严格位于该切线的一侧，曲线嵌入且严格凸。

定义材料角

$$
\theta=\Theta(\varphi)
=\varphi+\frac A2\sin2\varphi+\frac B3\sin3\varphi.
\tag{4}
$$

其导数 $\Theta'=\rho/a_0>0$，且 $\Theta(\varphi+2\pi)=\Theta(\varphi)+2\pi$，故有解析圆周逆映射 $\varphi(\theta)$。以下将 $\gamma,T,\nu,\rho$ 视作 $\theta$ 的周期函数。由 (2)—(4)，

$$
\gamma_\theta=a_0T,
\qquad
T_\theta=\frac{a_0}{\rho}\nu,
\qquad
\nu_\theta=-\frac{a_0}{\rho}T.
\tag{5}
$$

可给 (3) 加一个常向量，使其材料角均值为零；这只是一项整体平移，不允许在不同 $s$ 截面分别置中。

## 2. 局部等距存在定理

**定理。** 设 $a(s)$ 在 $s=0$ 邻域实解析，满足 $a(0)=a_0$、$a'(0)=0$、且 $a>0$。则存在 $\varepsilon>0$ 和一个实解析嵌入

$$
X:(-\varepsilon,\varepsilon)\times S^1\longrightarrow\mathbb R^3
$$

使

$$
X(0,\theta)=\gamma(\theta),\qquad X_s(0,\theta)=e_3,
\qquad
X^*e=ds^2+a(s)^2d\theta^2.
\tag{6}
$$

证明使用的是径向一阶、角向一阶的 Gauss–Codazzi 系统。没有对径向一阶、角向二阶的热方程型正常形误用 Cauchy–Kovalevskaya 定理。

### 2.1 真正的一阶非特征 CK 系统

写第二基本形式为

$$
\mathrm{II}=\ell\,ds^2+2m\,ds\,d\theta+n\,d\theta^2.
$$

在 $n\ne0$ 的开集中，取

$$
\ell=\frac{m^2-aa''}{n},
\tag{7}
$$

并对 $(m,n)$ 求解

$$
\begin{aligned}
m_s&=\frac{2m}{n}m_\theta
       -\frac{m^2-aa''}{n^2}n_\theta-\frac{a'}a m,\\
n_s&=m_\theta+\frac{a'}a n+aa'\frac{m^2-aa''}{n}.
\end{aligned}
\tag{8}
$$

初值为

$$
m(0,\theta)=0,\qquad n(0,\theta)=\frac{a_0^2}{\rho(\theta)}>0.
\tag{9}
$$

式 (8) 的右端对 $(s,\theta,m,n,m_\theta,n_\theta)$ 解析；它没有高于一阶的角向导数，且已解出全部径向一阶导数。初值解析且 $n$ 在紧圆周上有统一正下界。因此标准一阶 CK 定理在每个初始点给唯一局部解析解。有限覆盖、局部唯一性和初值周期性将这些解粘成某个统一窄圆柱上的周期解析解；缩小圆柱后仍有 $n>0$。

这里采用的标准定理可精确核对：Robert L. Bryant，*Lecture 2: Some Classical PDE Background and Generalizations*，2026-02-03，Theorem 1、式 (1.1)，第 1 页，作者讲义：
[https://sites.math.duke.edu/~bryant/Eilenberg/Lecture02.pdf](https://sites.math.duke.edu/~bryant/Eilenberg/Lecture02.pdf)。本稿只调用其一阶解析局部存在唯一性，不借它声称任何全局延拓或数值稳定性。

由 (7)—(8) 得完整 Gauss–Codazzi 方程

$$
\ell n-m^2=-aa'',\qquad
m_s=\ell_\theta-\frac{a'}a m,\qquad
n_s=m_\theta+\frac{a'}a n+aa'\ell.
\tag{10}
$$

### 2.2 恢复标架，核清全部约束和圆周 monodromy

令 $E=(e_1,e_2,N)$ 为以三个向量作列的正交标架。定义斜对称矩阵

$$
U=\begin{pmatrix}
0&0&-\ell\\
0&0&-m/a\\
\ell&m/a&0
\end{pmatrix},\qquad
V=\begin{pmatrix}
0&-a'&-m\\
a'&0&-n/a\\
m&n/a&0
\end{pmatrix}.
\tag{11}
$$

直接代入 (10) 可得

$$
V_s-U_\theta+[U,V]=0.
\tag{12}
$$

例如其 $(1,2)$ 项是 $-a''-(\ell n-m^2)/a=0$；$(1,3)$ 项是 $-m_s+\ell_\theta-(a'/a)m=0$；$(2,3)$ 项是 $[-n_s+m_\theta+(a'/a)n+aa'\ell]/a=0$。斜对称性给其余项。

对每个 $\theta$，解常微分方程

$$
E_s=EU,\qquad E(0,\theta)=(e_3,T(\theta),\nu(\theta)).
\tag{13}
$$

因为 $U$ 斜对称，$E$ 始终属于 $SO(3)$；初值确实正定向，因为 $e_3\times T=\nu$。系数和初值周期，所以解周期。由 (5)、(9) 及 $a'(0)=0$，初态还满足 $E_\theta=EV$。

不能只解 (13) 就默认角向标架约束成立。令 $D=E_\theta-EV$，结合 (12) 直接微分得

$$
D_s=DU,
\qquad D(0,\theta)=0.
$$

ODE 唯一性给 $D=0$，于是 $E_\theta=EV$ 在全窄圆柱上成立。这里实际核掉了角向标架约束，也保留了初圈的周期标架；没有用局部基本定理自动跳过环带的 monodromy。

现在定义

$$
X(s,\theta)=\gamma(\theta)+\int_0^s e_1(v,\theta)\,dv.
\tag{14}
$$

它周期且 $X_s=e_1$。令 $Z=X_\theta-ae_2$。由两组标架方程，

$$
Z_s=(e_1)_\theta-a'e_2-a(e_2)_s
=(a'e_2+mN)-a'e_2-mN=0,
$$

而 $Z(0,\theta)=\gamma_\theta-a_0T=0$。所以 $X_\theta=ae_2$，准确得到 (6) 的全部三项度量约束。因为 $a>0$、$e_1,e_2$ 单位正交，$X$ 是浸入。

### 2.3 真正的局部嵌入

初始曲线 $\gamma$ 已嵌入，且 $e_3,T,\nu$ 线性无关。考虑

$$
Y(s,\theta,v)=X(s,\theta)+vN(s,\theta).
$$

在 $(0,\theta,0)$，三方向导数为 $e_3,a_0T,\nu$，故由逆函数定理在每个初始点附近局部单射。初圈紧，取有限覆盖，可选统一窄的 $s,v$ 范围，使足够接近的角点对处在某个这样的单射邻域内。对角距有统一正下界的其他点对，初圈嵌入和紧性给 $|\gamma(\theta)-\gamma(\theta')|$ 的正下界；再缩小 $s,v$ 范围，连续性保持这些点对分离。两类点对合起来给 $Y$ 在更窄的管域全局单射。限制到 $v=0$，即得某个 $\varepsilon>0$ 上的 $X$ 为嵌入。定理证毕。

## 3. 横向中心加速度的准确公式

记材料角平均中心

$$
C(s)=\frac1{2\pi}\int_0^{2\pi}X(s,\theta)\,d\theta.
\tag{15}
$$

在中央初圈，$X_s=e_3$、$N=\nu$、$m=0$。从 (7)、(9) 得

$$
X_{ss}(0,\theta)=\ell(0,\theta)\nu(\theta)
=-\frac{a''(0)\rho(\theta)}{a_0}\nu(\theta).
\tag{16}
$$

利用 $d\theta=(\rho/a_0)d\varphi$，于是

$$
\boxed{
C''(0)=-\frac{a''(0)}{2\pi a_0^2}
\int_0^{2\pi}\rho(\varphi)^2\nu(\varphi)\,d\varphi.}
\tag{17}
$$

对 (1) 的二、三模种子，展开 $\rho^2$。只有乘积

$$
2AB\cos2\varphi\cos3\varphi
=AB(\cos\varphi+\cos5\varphi)
$$

产生一阶模；所有其他项与 $\nu=(-\sin\varphi,\cos\varphi,0)$ 积分为零。因此

$$
\int_0^{2\pi}\rho^2\nu\,d\varphi
=\pi a_0^2AB\,e_2^{\mathrm{ambient}},
$$

其中 $e_2^{\mathrm{ambient}}=(0,1,0)$，不与移动标架 $e_2(s,\theta)$ 混同。最终得到

$$
\boxed{C''(0)=-\frac{a''(0)AB}{2}(0,1,0).}
\tag{18}
$$

只要 $a''(0)AB\ne0$，这就是严格非零的横向中心加速度。特别可取

$$
a(s)=a_0+\frac q2s^2,\qquad q>0,
$$

此时局部 $K=-a''/a<0$，同一准确度量上的解析环带具有

$$
C_\perp(s)-C_\perp(0)=-\frac{qAB}{4}s^2(0,1)+O(s^3).
\tag{19}
$$

这里 $O(s^3)$ 属于已证真实解析解，而非仅形式 Taylor 级数。式 (18) 是从同一解得到的中心变化，不是逐层平移人为产生的。

更一般地，对任意正解析闭合曲率半径 $\rho$，只要其均值为 $a_0$、一阶矩为零，上述存在证明和 (17) 同样成立。中心启动由 $\rho^2$ 的一阶矩决定，而不是由 $\rho$ 自身的一阶矩决定；后者为零正是初圈闭合所需条件。

## 4. 上下镜像仍会消掉两端的相对偏心

若 $a(s)$ 为偶函数，则 $\widetilde X(s,\theta)=P X(-s,\theta)$，其中 $P=\operatorname{diag}(1,1,-1)$，具有同一初始位置、同一初始 $X_s=e_3$ 和同一度量。它的第二基本形式系数为

$$
\widetilde\ell(s,\theta)=\ell(-s,\theta),\quad
\widetilde m(s,\theta)=-m(-s,\theta),\quad
\widetilde n(s,\theta)=n(-s,\theta).
$$

它们满足同一 CK 初值问题，因此由局部解析唯一性 $\widetilde X=X$。于是 $X_\perp(s,\theta)$ 为偶函数，$C_\perp(s)=C_\perp(-s)$。所以即使 (18) 非零，也不能把两个镜像截面的共同横移误称为端口之间的偏心。

为了目标双圆领有不同轴线，必须最终破坏这种径向镜像，或把不同的分支/过渡接在两侧。单纯把本局部构造上下反射并封帽，既没有圆领闭合，也没有相对偏心。

还可精确求一阶不对称响应。由 (8) 及初值，在 $s=0$ 有 $n_s=0$，从 (7) 得 $\ell_s=-a'''(0)\rho/a_0$；又 $N_s=-\ell e_3$。故

$$
(C'''(0))_\perp=-\frac{a'''(0)AB}{2}(0,1).
\tag{20}
$$

若 $a'''(0)\ne0$，则两个等距参数截面之间的横向中心差满足

$$
C_\perp(s)-C_\perp(-s)
=-\frac{a'''(0)AB}{6}s^3(0,1)+O(s^5).
\tag{21}
$$

它只描述真正局部解的截面中心，不说明这两个截面已经是圆领。

## 5. 本结果支付与未支付的内容

本结果已支付：正解析凸初圈、严格一阶非特征 CK 的真实局部存在、完整 Gauss–Weingarten 约束恢复、角向位置与标架周期、局部嵌入，以及中心漂移的准确系数。

尚未支付：延拓到准确圆领、两个圆领的相对非零偏心、固定帽、整闭曲面、全相位不相交、整体 $D$ 下的 $0.3$ 位移与 $0.03$ reach。小环带的局部存在半宽也没有给定一个足以完成上述目标的数值下界。

因此本结果只是具体可计算的新机制入口。下一步应在完整位置和标架不被逐圈置中的前提下推进、匹配圆领；不能将 (18) 的非零数值直接当作已存在的闭曲面幅度。
