# R630：Morse 二、三双核中心、全整数频谱界与保持行程角的双控制

2026-11-28。**已证明一个明确的全线中心参考模型：恰有第二、第三角模各一个零能核，其他全部整数角频有显式多项式谱隙；唯一负曲率区的特征行程角有显式小除数界；两个只支撑在正曲率区的密度参数对双核满秩，并在固定小参数邻域内保留其余全频逆。**

这里的中心参考坐标是整条 $X\in\mathbb R$。其单调径向坐标从 $0$ 到 $\infty$，不是两端全平的有限环带。第 8 节明确区分全线参考、有限截段和尚待组装的真实平尾。这一结果不把中心谱界移交给未构造的全域算子，也不声称已有有限等距闭嵌入或 README 所要求的宏观几何。

## 1. 同一个明确中心与目标

记

$$
s=\sqrt5,\qquad
A=5,\qquad
B=\frac{33-14s}{20},\qquad
\eta^2=\frac{36s-27}{20},\qquad \eta>0,
$$
$$
\rho(X)=5(e^{-X}-e^{-2X})-B,\qquad
\mathcal P(X)=e^{-2\eta X}.                              \tag{1}
$$

因为 $2<s<9/4$，

$$
0<B<\frac14,\qquad \eta^2>\frac94,\qquad A>4B.
$$

对于**每个整数** $j\ge2$，定义 $L^2(\mathbb R,dX)$ 上的闭二次型自伴实现

$$
H_j=-\partial_X^2+\eta^2-j^2\rho(X).                       \tag{2}
$$

其势在左端趋于 $+\infty$，在右端趋于 $\eta^2+j^2B>0$。令 $\Pi_j$ 为其零空间的 $L^2$ 正交投影；没有零空间时取 $\Pi_j=0$。本稿证明

$$
\dim\ker H_2=\dim\ker H_3=1,\qquad
\ker H_j=0\quad(j\ge4),                                  \tag{3}
$$
$$
\left\|R_j\right\|_{2\to2}\le2880j^2,\qquad
R_j=(H_j|_{(\ker H_j)^\perp})^{-1}(I-\Pi_j).               \tag{4}
$$

这里包括奇数频率；不使用半周对称去掉第三模。

参数并非搜索得到。若先写 $\sqrt A=x>2$，要求第二模基态与第三模第一激发态同时为零，解两个准确代数方程得到

$$
B=\frac{x^2}{4}-\frac{7x}{10}+\frac25,\qquad
\eta^2=\frac{9x}{5}-\frac{27}{20}.                         \tag{5}
$$

取 $x=\sqrt5$ 使其余谱的分离可以用二次整数范数完成。

## 2. 完整 Morse 谱及无遗漏的零能分类

### 2.1 谱公式

令 $\omega=j\sqrt A$、$\alpha_j=(\omega-1)/2$、
$E_\infty=\eta^2+j^2B$。完整离散谱为简单特征值

$$
E_{j,n}=E_\infty-(\alpha_j-n)^2,
\qquad n=0,1,\ldots,\quad n<\alpha_j.                     \tag{6}
$$

本质谱是 $[E_\infty,\infty)$，其上没有 $L^2$ 特征函数。以下给出所需证明，使 (6) 不依赖对偶频单核定理的扩展。

固定 $\omega,E_\infty$，引入

$$
H_\alpha=-\partial_X^2+\omega^2e^{-2X}
 -\omega(2\alpha+1)e^{-X}+E_\infty,\qquad
D_\alpha=\partial_X+\alpha-\omega e^{-X}.
$$

直接乘开得

$$
H_\alpha=D_\alpha^*D_\alpha+E_\infty-\alpha^2,\qquad
H_{\alpha-1}=D_\alpha D_\alpha^*+E_\infty-\alpha^2.         \tag{7}
$$

$D_\alpha$ 的核为 $e^{-\alpha X-\omega e^{-X}}$，恰在 $\alpha>0$ 时属于 $L^2$；$D_\alpha^*$ 的形式核在左端增长。因此每下降一个整数参数，只删除一个基态。下降至 $-1<\alpha\le0$ 时

$$
H_\alpha-E_\infty=D_0^*D_0-2\omega\alpha e^{-X}\ge0,
$$

故不再有阈值下谱。反向提升不会丢掉已列出的能级，因为若提升前能量为 $E_\infty-\beta^2$，提升参数 $\alpha>\beta>0$，则

$$
\|D_\alpha^*\phi\|_2^2=(\alpha^2-\beta^2)\|\phi\|_2^2>0.
$$

左端为束缚端，右端在阈值下指数衰减，故截断积分无边界项，(7) 对闭二次型实现成立。两个 $L^2$ 解的 Wronskian 在左端为零，且沿线常数，因此每个能级简单。

为核对阈值以上部分，将实线在一点分为两半。左半势趋于无穷，由二次型尾界和有界区间的 $H^1$ 紧嵌入得紧预解式；右半势与常数 $E_\infty$ 的差指数衰减，故其本质谱为 $[E_\infty,\infty)$。改变两半的一个匹配条件只产生有限秩预解式差。对 $E>E_\infty$，在充分晚的右尾解 Volterra 方程

$$
u_\pm(X)=e^{\pm ikX}+
\int_X^\infty \frac{\sin(k(Y-X))}{k}
\big(V(Y)-E_\infty\big)u_\pm(Y)\,dY,\quad
k=\sqrt{E-E_\infty}.
$$

指数尾使积分为压缩，得到两条导数也有相应渐近的 $e^{\pm ikX}(1+o(1))$ 解，其 Wronskian 非零。阈值处把核换成 $Y-X$，得到 $1+o(1)$、$X+o(X)$ 两条解。没有非零线性组合属于 $L^2$。这完成 (6) 和全部谱类型的证明。

### 2.2 准确分类与整数范数常数

令 $N=2n+1$。合法离散能级恰满足

$$
N\text{ 为正奇数},\qquad N<js.
$$

代入 (1)、(6)，有

$$
20E_{j,N}=sU+V,\qquad
U=36-14j^2+10jN,\quad V=8j^2-5N^2-27.                    \tag{8}
$$

$U,V$ 都是整数。由于 $s$ 无理，$E=0$ 等价于 $U=V=0$。由 $U=0$ 得

$$
N=\frac{7j^2-18}{5j}.
$$

将其代入 $5j^2V=0$，准确得到

$$
-9(j^2-4)(j^2-9)=0.
$$

于是零能只有

$$
(j,N)=(2,1),\qquad (j,N)=(3,3).                          \tag{9}
$$

它们都满足 $N<js$，分别对应 $n=0$、$n=1$。这证明 (3)，不遗漏高频或高径向激发态。

对于其他合法 $(j,N)$，整数 $V^2-5U^2$ 非零。因为 $j\ge2$、$N<js$，

$$
|U|\le36+14j^2+10jN<46j^2,
$$
$$
|V|\le8j^2+5N^2+27<40j^2.
$$

因此

$$
|V-sU|<(40+\tfrac94\,46)j^2<144j^2.
$$

用非零整数范数，

$$
1\le |V^2-5U^2|=|V+sU|\,|V-sU|
 <144j^2|20E|,
$$

得到

$$
\boxed{|E_{j,N}|\ge\frac1{2880j^2}
\quad\text{于 (9) 以外的全部合法离散能级}.}                \tag{10}
$$

本质谱阈值大于 $\eta^2>9/4$，也满足这一更弱的下界。谱定理给 (4)。

两条零模可明确取为

$$
\psi_2(X)=e^{-(s-1/2)X-2s e^{-X}},
$$
$$
\psi_3(X)=e^{-\frac{3s-3}{2}X-3s e^{-X}}
                 \big((3s-2)-6s e^{-X}\big).              \tag{11}
$$

第一式是 (7) 的基态；第二式是用 $D_{\alpha_3}^*$ 提升 $\alpha_3-1$ 的基态。第二式恰有一个简单零点。

## 3. 唯一负曲率区与全整数行程角界

在本稿径向转换下，$\rho>0$ 对应 $w_r<0$，即背景负 Gaussian 曲率区。令

$$
t_\pm=\frac{1\pm\sqrt{1-4B/5}}2,\qquad
0<t_-<\tfrac12<t_+<1.
$$

则 (1) 在全线的唯一正区间是

$$
I_-=\{X:\rho(X)>0\}
       =(-\log t_+,-\log t_-).                            \tag{12}
$$

两个端点均为简单 type root。其特征行程角是

$$
T=\int_{I_-}\sqrt{\rho(X)}\,dX
 =\pi\left(\frac{s}{2}-\sqrt B\right)=\pi\alpha.            \tag{13}
$$

为核对积分，取 $t=e^{-X}$。被积式化为

$$
s\int_{t_-}^{t_+}
\frac{\sqrt{(t-t_-)(t_+-t)}}{t}\,dt.
$$

写 $t=c+h\cos\vartheta$，其中 $c=(t_-+t_+)/2$、
$h=(t_+-t_-)/2$，并用

$$
\frac{h^2\sin^2\vartheta}{c+h\cos\vartheta}
=c-h\cos\vartheta-\frac{c^2-h^2}{c+h\cos\vartheta}.
$$

积分为 $\pi s(c-\sqrt{c^2-h^2})$；再用
$t_-+t_+=1$、$t_-t_+=B/5$，即得 (13)。

现在给完全显式的无理数界。由 $B<1/4$、$s>2$ 得 $\alpha>1/2$；由

$$
B-(s/2-1)^2=\frac{3(s-2)}{10}>0
$$

得 $\alpha<1$。由 $\sqrt B=s/2-\alpha$ 平方得

$$
\alpha^2-\frac25=s\left(\alpha-\frac7{10}\right),
$$

因此

$$
p(\alpha)=0,\qquad
p(x)=100x^4-580x^2+700x-229.                              \tag{14}
$$

$p$ 没有有理根：若 $p(q)=0$ 且 $q$ 有理，则
$(q^2-2/5)^2=5(q-7/10)^2$。$q=7/10$ 不满足该式；否则该式使 $\sqrt5$ 为有理数。

给定整数 $k\ge1$，取距离 $k\alpha$ 最近的整数 $m$。于是 $m/k\in[-1,2]$，且

$$
k^4p(m/k)=100m^4-580m^2k^2+700mk^3-229k^4
$$

是非零整数。在 $[-1,2]$ 上

$$
|p'(x)|=|400x^3-1160x+700|\le6220.
$$

中值定理和 $p(\alpha)=0$ 给

$$
\left|\alpha-\frac mk\right|\ge\frac1{6220k^4},\qquad
\operatorname{dist}(k\alpha,\mathbb Z)\ge\frac1{6220k^3}.
$$

最后用 $|\sin(\pi y)|\ge2\operatorname{dist}(y,\mathbb Z)$，

$$
\boxed{|\sin(kT)|\ge\frac1{3110k^3}\qquad(k\ge1).}          \tag{15}
$$

这是全部整数返回频率的界，不只是偶数频率；常数不涉及数值试验。

## 4. 一个实际正且递增的径向转换

### 4.1 正积分公式

需要解

$$
r_{XX}-2\eta r_X+\rho r=0,\qquad r>0,\quad r_X>0.          \tag{16}
$$

令

$$
\beta=\sqrt{\eta^2+B}=\sqrt{\frac{11s+3}{10}},\quad
z=2s e^{-X},\quad
a=\beta-\frac s2+\frac12>0,\quad b=1+2\beta.
$$

定义

$$
U(a,b,z)=\frac1{\Gamma(a)}
\int_0^\infty e^{-zt}t^{a-1}(1+t)^{b-a-1}\,dt,
$$
$$
\psi_1(X)=e^{-z/2}z^\beta U(a,b,z),\qquad
r(X)=e^{\eta X}\psi_1(X).                                \tag{17}
$$

积分及其 $z>0$ 上的各阶导数局部一致收敛，且正。积分
$\partial_t(e^{-zt}t^a(1+t)^{b-a})$ 的两端边界值为零，故

$$
zU_{zz}+(b-z)U_z-aU=0.
$$

代入 (17)、用 $\partial_X=-z\partial_z$，得到

$$
\psi_1''=(z^2/4-sz/2+\beta^2)\psi_1
        =(\eta^2-\rho)\psi_1.                             \tag{18}
$$

又

$$
\eta^2-\max_X\rho
=\frac{22s-19}{20}>0.                                    \tag{19}
$$

因此 $\psi_1''>0$。

### 4.2 两端渐近、单调性和权

当 $z\to\infty$，在积分中取 $t=u/z$。对
$(1+u/z)^{b-a-1}$ 作一次带积分余项的展开，得到

$$
U(a,b,z)=z^{-a}(1+O(z^{-1})),
$$
$$
\psi_1=e^{-z/2}z^{(s-1)/2}(1+O(z^{-1})),\qquad
\frac{\psi_1'}{\psi_1}=\frac z2-\frac{s-1}{2}+O(z^{-1}).
                                                               \tag{20}
$$

同一积分估计允许求一次所写导数。尤其 $\psi_1,\psi_1'\to0$ 于 $X\to-\infty$。结合 $\psi_1''>0$，得到 $\psi_1'>0$ 于全线。于是

$$
\nu:=\frac{r_X}{r}=\eta+\frac{\psi_1'}{\psi_1}>\eta>0.
                                                               \tag{21}
$$

当 $z\downarrow0$，仍取 $t=u/z$，则

$$
z^{2\beta}U(a,b,z)
=\frac1{\Gamma(a)}
\int_0^\infty e^{-u}u^{a-1}(u+z)^{b-a-1}\,du
\longrightarrow\frac{\Gamma(2\beta)}{\Gamma(a)}.
$$

$b-a-1=\beta+s/2-1/2>0$；支配收敛和同样的一阶导数估计给

$$
\psi_1=Cz^{-\beta}(1+O(z)),\qquad
\frac{\psi_1'}{\psi_1}=\beta+O(z),\quad C>0.               \tag{22}
$$

因此 $r$ 从 $0$ 严格递增至 $\infty$，且

$$
\nu\asymp1+e^{-X}.                                       \tag{23}
$$

这里及以下 $\asymp$ 的常数只依赖 (1) 的固定模型。

### 4.3 与真实径向核方程的准确关系

取任意常数 $\lambda>0$，定义

$$
v=r_X,\qquad w(r(X))=\lambda\mathcal P(X)v(X)>0.
                                                               \tag{24}
$$

(16) 给

$$
w_r=-\frac{\lambda\mathcal P\,\rho r}{v}.
$$

因此 $\rho<0$ 的地方确实是 $w_r>0$ 的正曲率区，$\rho>0$ 的地方是负曲率区。令

$$
L_ju=(wu_r)_r-\frac{j^2w_r}{r}u,\qquad
\psi=\sqrt{\mathcal P}\,u.
$$

直接换元得到

$$
\boxed{L_ju=-\frac{\lambda\sqrt{\mathcal P}}{v}H_j\psi.}  \tag{25}
$$

故 $f_j(r(X))=\mathcal P^{-1/2}\psi_j(X)$，$j=2,3$，
是同一个正 $w$ 上的两条准确核。任取

$$
X_L<-\log t_+,\qquad X_R>-\log t_-,
$$

(24) 在有限环带 $r(X_L)\le r\le r(X_R)$ 上是实际光滑正 profile，且包含整个唯一负曲率组件。此时边界还不是平帽。

## 5. 中心全频逆在径向自然权中的界

由 (23) 及二次势，存在固定常数 $c,C>0$，使

$$
V_j=\eta^2-j^2\rho\ge c j^2\nu^2-Cj^2.                  \tag{26}
$$

例如先用 $5t^2-5t\ge(5/2)t^2-5/2$，再用
$\nu^2\le C_0(1+t^2)$ 即得。

对于 $\psi=R_jf$，谱界 (4) 和闭二次型能量给

$$
cj^2\|\nu\psi\|_2^2
\le |\langle\psi,f\rangle|+Cj^2\|\psi\|_2^2
\le C_1j^6\|f\|_2^2.
$$

这里在 $j=2,3$ 时 $H_j\psi=(I-\Pi_j)f$，但
$\psi\perp\ker H_j$，故配对仍是 $\langle\psi,f\rangle$。由此及取伴随，

$$
\|\nu R_j\|+\|R_j\nu\|\le C_2j^2.                         \tag{27}
$$

再取 $\psi=R_j(\nu f)$，先用 (27) 得 $\|\psi\|_2\le C_2j^2\|f\|_2$。将 (26) 再用一次，得到

$$
cj^2\|\nu\psi\|_2^2
\le\|\nu\psi\|_2\|f\|_2+C_3j^6\|f\|_2^2.
$$

以 Young 不等式吸收首项，得

$$
\boxed{\|\nu R_j\nu\|_{2\to2}\le C_4j^2.}                \tag{28}
$$

先在紧支撑源上证明，再按密度延拓。$\nu\psi_2,\nu\psi_3$ 均属于 $L^2$，所以两条有限秩核的规范化也受此权控制。

若取

$$
\varpi=12w/r^2,\qquad \mathcal B_j=-\varpi^{-1}L_j,
$$

则准确换元恒等式为

$$
\mathcal B_j(\mathcal P^{-1/2}\psi)
=\mathcal P^{-1/2}\frac{H_j\psi}{12\nu^2},
$$
$$
\int\varpi|u|^2\,dr=12\lambda\int\nu^2|\psi|^2\,dX.
                                                               \tag{29}
$$

所以 (28) 是这个自然径向 $L^2$ 权中的 $O(j^2)$ 逆界；第二、第三模须保留各一条核相容条件及一条规范化。这里的 $j^2$ 是所证明的角频代价，不把它解释为尚未建立的全部非线性 tame 估计。

## 6. 两个正曲率区密度控制：对双核满秩且行程角不变

### 6.1 参数族和实际径向实现

选两个实 $C_c^\infty$ 函数 $\chi_1,\chi_2$，支撑位于
$\{\rho<0\}$ 的同一个有限左侧区间，并与 type root 有正距离。令

$$
\zeta_\tau=\tau_1\chi_1+\tau_2\chi_2,\qquad
\mathcal P_\tau=e^{-2\eta X+2\zeta_\tau},\qquad
\rho_\tau=\rho.
$$

于是

$$
V_{0,\tau}
=\frac{(\sqrt{\mathcal P_\tau})''}{\sqrt{\mathcal P_\tau}}
=\eta^2+\zeta_\tau''-2\eta\zeta_\tau'+(\zeta_\tau')^2,
$$
$$
H_{j,\tau}=-\partial_X^2+V_{0,\tau}-j^2\rho.              \tag{30}
$$

该族准确保持 $\rho$、两个 type root 和 (13) 的 $T$；因此 (15) 在整个参数族上原样成立。

它也有实际正径向实现。令 $\psi_{1,\tau}$ 在支撑左侧等于 (17) 的 $\psi_1$，并解

$$
\psi_{1,\tau}''=(V_{0,\tau}-\rho)\psi_{1,\tau},\qquad
r_\tau=e^{\eta X-\zeta_\tau}\psi_{1,\tau}.
$$

当 $\tau$ 足够小时，(19) 使 $V_{0,\tau}-\rho$ 在全线仍正；左端初始 $\psi,\psi'$ 均正，故两者沿全线保持正。再缩小参数使 $\|\zeta_\tau'\|_\infty<\eta/2$，则

$$
\frac{(r_\tau)_X}{r_\tau}
=\eta-\zeta_\tau'+\frac{\psi_{1,\tau}'}{\psi_{1,\tau}}
>\eta/2.
$$

因此 $r_\tau$ 仍从 $0$ 递增至 $\infty$，且

$$
(r_\tau)_{XX}
+(\mathcal P_\tau'/\mathcal P_\tau)(r_\tau)_X+\rho r_\tau=0.
$$

以 $w_\tau=\lambda\mathcal P_\tau(r_\tau)_X$ 定义真实 profile，(25) 继续成立。

### 6.2 一个可选择的满秩 $2\times2$ 矩阵

$j=2,3$ 的简单零特征值分别有光滑延续 $E_2(\tau),E_3(\tau)$。固定 $\psi_j$ 的归一化后，直接微分特征方程并与 $\psi_j$ 配对得

$$
\partial_{\tau_i}E_j(0)
=\frac1{\|\psi_j\|_2^2}
\int\psi_j^2(\chi_i''-2\eta\chi_i')\,dX
=\frac1{\|\psi_j\|_2^2}\int\chi_i W_j\,dX,
$$
$$
W_j=(\psi_j^2)''+2\eta(\psi_j^2)'.                        \tag{31}
$$

这两个权并非成比例。事实上当 $t=e^{-X}\to\infty$，由 (11)

$$
W_j=(4j^2s^2t^2+O(t))\psi_j^2>0,
$$
$$
\frac{W_3}{W_2}
\sim\frac94\,36s^2\,t^s e^{-2st}\longrightarrow0.          \tag{32}
$$

在每个充分左侧的有限点，$W_3/W_2>0$。所以可先选一个这样的 $X_2$，再选更左的有限 $X_1$，使两处比值不同。以分别围绕 $X_1,X_2$ 的小不交邻域为支撑，取非负且积分为一的 $\chi_1,\chi_2$。缩小支撑后，

$$
\det\left(\int\chi_i W_j\,dX\right)_{j=2,3;\ i=1,2}
\longrightarrow
W_2(X_1)W_2(X_2)
\left(\frac{W_3(X_2)}{W_2(X_2)}
      -\frac{W_3(X_1)}{W_2(X_1)}\right)\ne0.
$$

故可取真实有限宽、光滑紧支撑的两个 bump，使

$$
\boxed{\det D_\tau(E_2,E_3)(0)\ne0.}                      \tag{33}
$$

该选择全部发生在正曲率区内，且保持 (15) 准确不变。因此调节双核不要求同时改动负曲率组件的行程角。

## 7. 正区控制与其他全部频率真正相容

谱隙只有 $j^{-2}$ 时，任意位置的小 $L^\infty$ 扰动并不能仅凭总预解式界获得统一小邻域。这里利用控制支撑在严格正曲率区内，证明比全局逆强得多的局部源界。

### 7.1 正区源的 $O(j^{-2})$ 逆界

设 $K$ 为第 6 节两个 bump 支撑之并的一个固定紧邻域，仍满足
$\rho<0$ 且与 type root 有正距离。则存在只依赖该选择的 $C_K$，使

$$
\boxed{\|R_j\mathbf1_K\|_{2\to2}
       +\|\mathbf1_KR_j\|_{2\to2}\le C_Kj^{-2}
       \quad(j\ge2).}                                   \tag{34}
$$

这里第二、第三模仍使用约化逆。

证明如下。选择 $K\Subset I_0\Subset I_1\Subset\{\rho<0\}$，其中闭包均紧。取 $\delta>0$ 使 $-\rho\ge2\delta$ 于 $I_1$。将 $-\rho$ 在 $I_0$ 附近延拓为全线光滑有界函数 $q_+\ge\delta$，定义

$$
H_j^+=-\partial_X^2+\eta^2+j^2q_+,\qquad
\|(H_j^+)^{-1}\|_{2\to2}\le(\delta j^2)^{-1}.
$$

其正 Green 核满足

$$
0\le G_j^+(X,Y)\le
\frac1{2j\sqrt\delta}e^{-j\sqrt\delta|X-Y|}.                \tag{35}
$$

这是常系数 $-\partial_X^2+\delta j^2$ 的正 Green 核比较：该核作用于 $H_j^+$ 给 $\delta_Y$ 加一个非负函数；在有限区间用最大值原理比较，再令端点趋于无穷即得 (35)。

对支持在 $K$ 的 $f$，令 $u_+=(H_j^+)^{-1}f$。取 $\zeta=1$ 于 $K$ 邻域，支撑位于 $I_0$，且其导数支持与 $K$ 距离为正。由 (35)，在这些导数支持的固定邻域上

$$
\|u_+\|_2\le Cj^{-1}e^{-cj}\|f\|_2.
$$

该处源为零。以更大但仍与 $K$ 分离的 cutoff 乘齐次方程并积分，得 Caccioppoli 界

$$
\|u_+'\|_{L^2(\operatorname{supp}\zeta')}
\le Cj^{-1}e^{-c'j}\|f\|_2.
$$

具体地，$\int\vartheta^2|u_+'|^2+\int V_+\vartheta^2|u_+|^2
=-2\int\vartheta\vartheta'u_+u_+'$，用 Young 不等式吸收一半首项即可；右边只需较大邻域的上述指数界。

因此 $u_0=\zeta u_+$ 满足

$$
H_ju_0=f+h,\qquad
h=[-\partial_X^2,\zeta]u_+,\qquad
\|h\|_2\le Cj^{-1}e^{-c'j}\|f\|_2.
$$

由 $R_jH_j=I-\Pi_j$，

$$
R_jf=(I-\Pi_j)u_0-R_jh.
$$

结合 (4)，

$$
\|R_jf\|_2
\le\left(\frac1{\delta j^2}+Cj e^{-c'j}\right)\|f\|_2
\le C_Kj^{-2}\|f\|_2.
$$

最后一步只用 $\sup_{x\ge2}x^3e^{-c'x}<\infty$。取伴随给 (34) 的另一半。该证明没有假设高频本征函数的未证局部化。

### 7.2 一个固定小参数邻域内的全频稳定性

记

$$
\delta V_\tau=\zeta_\tau''-2\eta\zeta_\tau'+(\zeta_\tau')^2.
$$

它支持于固定 $K$，且 $\|\delta V_\tau\|_\infty\to0$。对于 $j\ge4$，(34) 给

$$
\|R_j\delta V_\tau\|
\le C_Kj^{-2}\|\delta V_\tau\|_\infty.
$$

选择一个**与 $j$ 无关**的小 $\tau$ 邻域，使右边不超过 $1/2$。于是

$$
H_{j,\tau}^{-1}
=(I+R_j\delta V_\tau)^{-1}R_j,\qquad
\boxed{\|H_{j,\tau}^{-1}\|\le5760j^2\quad(j\ge4).}         \tag{36}
$$

第二、第三模的非零谱与零谱有各自固定正间隔。再缩小同一个参数邻域，只有 $E_2(\tau)$、$E_3(\tau)$ 可能接近零，其他谱保持远离零。用 $H_j+\Pi_j$ 的有界逆作有限频率扰动即可证明这一点；不需要高频一致的普通扰动论。

因此第 6 节的双核控制是真正可与全频中心谱界并用的有限维控制。若外部组装产生一个足够小的、对 $\tau$ 为 $C^1$ 的双核匹配误差，且它的两行导数收敛于 (31)，则 (33) 允许用 $\tau_1,\tau_2$ 恢复两条核，中心部分仍保 (15)、(36)。这最后一句是一个明确的条件式应用：外部组装必须实际证明所列 $C^1$ 小误差；本稿尚未提供该组装。

## 8. 对当前任务支付了什么、还需要什么输入

与 R628 的两块常斜率中心相比，这里支付的是同一个模型上的**全部整数角频**参考逆及其控制稳定性。第二、第三模同时为核，既不靠把不同 $w$ 的模式拼起来，也不靠恢复半周对称删除第一、第三模。R629 的零/一模三矩消元和真实旋转尾图表仍可作为低频端口的独立输入。

这里有三个不同对象：

1. **全线参考算子。** (1)–(36) 的谱、行程角、单调径向转换和正区双控制已经证明。
2. **有限中心截段。** (24) 在任意覆盖 (12) 的有限 $[X_L,X_R]$ 上给真实光滑正 $w$。若边界条件取参考全线解的准确稳定 DtN 条件，它只是全线问题的限制；这种 DtN 尚不是平帽。
3. **真正全平端的全域背景及非线性根。** 仍须接入有全频控制的左右平尾，证明参考截断到真实尾的全部匹配误差及其双参数导数；随后还须支付随状态的特征返回和残差校正，求得一个有限非零幅值的准确等距嵌入，并检查有限几何。

特别，(17) 的全线径向坐标在左端趋于零、右端趋于无穷；不能把这两个参考端声称为有限半径的开放平帽。不能把两条中心零模直接当作 R628 已有的非零倾斜系数：新中心接真实尾之后仍须计算它自己的端口系数。也不能用无限截断、无限控制或不断变细的几何去代替 README 的固定度量与 reach 要求。

本稿的新可用输入是一个实际给出公式、可保留全整数频控制、且可独立恢复两个共振的中心。下一构造可以用它替换偶频单核谐振子中心，逐项接付真实平尾；无须重新寻找未知的双核中心或另行假设一个高频谱隙。
