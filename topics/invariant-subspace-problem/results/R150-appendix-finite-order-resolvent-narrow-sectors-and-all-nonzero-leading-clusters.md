# R150 附录：有限阶整预解、任意窄扇形与全部非零最高根簇

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf。

状态：完整证明；根代理与 boundary_resume_1cf 已独立核查真实计数、等价 Hilbert 范数、窄扇形预解及完整自然域。本文给出一个可检验的额外预算，移除[同次数分簇稿](R150-appendix-distinct-leading-clusters-complete-bell-factorization-and-pointwise-products.md)的有限消失阶要求。最高符号允许任意重根；原完整 Bell、全部常数移位、普通点态幂和复指数权均保留。

## 1. 结论及额外计数条件

保持[高次剪切稿](R150-appendix-all-polynomial-shears-fixed-complex-line-and-higher-companion-parts.md)的原函数
$$
u=u_*+\sum_j(a_j+d^0_j+e^0_j)\chi_j,\qquad
v=v_*+\sum_j(e^{i\psi}b_j+\gamma a_j+d^1_j+e^1_j)\chi_j,
\tag{1.1}
$$
其中
$$
a\ge0,\quad a\in\ell^2\setminus\ell^1,\qquad
b\in\ell^2(\mathbb R),\quad |b_j|\le C_0a_j,
$$
$d^\nu_j=0$ 于 $a_j=0$，$\sum_{a_j>0}|d^\nu_j|^2/a_j<\infty$，$e^\nu\in\ell^1(\mathbb C)$，常数与 $\psi$ 任意。

取同一实际锚
$$
Z=X_{a+d^0}+\omega,\qquad L=Z^{-1}\in A',\qquad
Y=e^{i\psi}X_b,
\tag{1.2}
$$
其中 $\omega$ 为前稿已支付的共享增生位移。再假设它的真实整预解具有某个有限阶界：
$$
\boxed{
\|(Z-z)^{-1}\|\le C\exp(C|z|^\rho)
\quad(z\in\mathbb C)
}
\tag{1.3}
$$
其中 $C<\infty,0<\rho<\infty$。

一个只用原正系数即可核验的充分条件是：存在 $p>1,c>0$，使充分大 $t$ 时
$$
\boxed{
\Theta_a(t):=\sum_j\lfloor ta_j\rfloor\ge ct^p.
}
\tag{1.4}
$$
§2 将连同复加权主误差一起证明 (1.4) 推出 (1.3)。

令 $k\ge2$，$F(x,y)$ 关于 $y$ 首一，次数为 $M\ge1$，并满足
$$
i+kj\le kM\qquad([x^iy^j]F\ne0).
\tag{1.5}
$$
定义最高符号
$$
H(s)=\sum_{i+kj=kM}[x^iy^j]F\,s^j.
$$
它是次数 $M$ 的首一标量多项式。只再要求
$$
\boxed{H(0)\ne0.}
\tag{1.6}
$$
等价地，$H$ 的全部根非零；也等价于 $F$ 中 $x^{kM}$ 的系数非零。

**定理 1。** 在 (1.1)—(1.3)、(1.5)—(1.6) 下，对全部 $\lambda\in\mathbb C$、整数 $r\ge1$ 和复 $\ell^2$ 第一阶指数权 $e^w$，
$$
\boxed{
[F(u,v)-\lambda]^r e^w
\text{ 对原实际 }A\text{ 循环。}
}
\tag{1.7}
$$

不再要求
$H_q^{(j)}(\kappa)=0$ 于 $q+j<m_\kappa$。
特别，对任意 $m>1,k\ge2$，
$$
F(x,y)=(y-x^k)^m+x^{km-1}
\tag{1.8}
$$
也在本定理内。它正是不满足前稿消失阶条件的真实超权余项实例。

## 2. 复加权主行也具有可核验的有限阶预算

令 $\zeta=a+d^0$。取坏集合
$$
B=\{j:|d^0_j|>a_j/2\}.
$$
由加权平方可和性，
$$
\sum_{j\in B}a_j\le4\sum_{a_j>0}|d^0_j|^2/a_j<\infty.
$$
补集上 $|\zeta_j|\ge a_j/2$，故
$$
\Theta_{|\zeta|}(t)
\ge\Theta_a(t/2)-\frac t2\sum_{j\in B}a_j.
\tag{2.1}
$$

[复加权主行稿 §4](R150-appendix-weighted-complex-main-real-controlled-skeleton-and-all-shear-powers.md)已经支付实际 carry、可和相位补偿及完整闭半群分解，给某些固定 $T,J$ 和 $\kappa>0$：
$$
\|e^{-tZ}\|
\le\exp\left[
-\kappa T\sum_{j\ge J}
\left\lfloor t|\zeta_j|/T\right\rfloor
\right].
\tag{2.2}
$$
删除有限物理头只扣 $O(t)$。因此 (1.4)、(2.1) 给有限常数
$C_1,\gamma_1>0$，使
$$
\boxed{
\|e^{-tZ}\|\le C_1e^{-\gamma_1 t^p}
\qquad(t\ge0).
}
\tag{2.3}
$$
这里 $p>1$ 正好使有限头和坏集的 $O(t)$ 成本可以吸收。

全平面真实 Laplace 逆
$$
(Z-z)^{-1}=\int_0^\infty e^{tz}e^{-tZ}\,dt
$$
在范数中收敛。Young 不等式如
[R134 计数半群稿 §4](R134-appendix-positive-counting-semigroup-and-finite-order-entire-resolvent.md)
给
$$
\|(Z-z)^{-1}\|
\le C_2\exp\left[C_3(\operatorname{Re}z)_+^{p/(p-1)}\right].
\tag{2.4}
$$
所以可取 $\rho=p/(p-1)$。

例如下降重排满足
$$
a_n^*\ge c_*(n+1)^{-\sigma},\qquad 1/2<\sigma<1,
$$
就可取 $p=1/\sigma$，因而 $\rho=1/(1-\sigma)$。实际物理排列任意，且原 weighted 与 $\ell^1$ 复误差仍完整保留。

本节没有把谐和临界 $\sigma=1$ 自动纳入有限阶预算。

## 3. 抽象排除引理：非零拟幂零簇不能作最高系数

设 $X$ 在一个非零 Hilbert 空间上最大增生、空谱，并有有限阶整预解界
$$
\|(X-z)^{-1}\|\le C e^{C|z|^\rho}.
\tag{3.1}
$$
设 $J$ 有界，与 $X$ 的全部预解交换，且
$$
\sigma(J)=\{\kappa\},\qquad\kappa\ne0.
\tag{3.2}
$$
固定 $k\ge2,c\ge0,|\alpha|=1$。假设
$$
Q_\pm=cX\pm\alpha JX^k,\qquad
\operatorname{Dom}Q_\pm=\operatorname{Dom}X^k
\tag{3.3}
$$
都最大增生。则矛盾。

### 3.1 保持全部收缩半群的等价 Hilbert 范数

写 $N=J-\kappa I$，它拟幂零。给任意 $\varepsilon>0$，定义
$$
\|x\|_\varepsilon^2
=\sum_{n\ge0}\varepsilon^{-2n}\|N^nx\|^2.
\tag{3.4}
$$
拟幂零性保证该级数由某个常数倍的 $\|x\|^2$ 支配；首项为
$\|x\|^2$，所以它是等价 Hilbert 范数，并且
$$
\|Nx\|_\varepsilon^2
=\varepsilon^2(\|x\|_\varepsilon^2-\|x\|^2)
\le\varepsilon^2\|x\|_\varepsilon^2.
\tag{3.5}
$$

$N$ 与 $X$ 的预解交换，也与自然 $Q_\pm$ 的完整域及预解交换，因此与三者的收缩半群交换。如果 $T$ 是其中任意一个收缩半群的成员，则逐项有
$$
\|Tx\|_\varepsilon^2
=\sum_n\varepsilon^{-2n}\|TN^nx\|^2
\le\|x\|_\varepsilon^2.
$$
所以 $X,Q_+,Q_-$ 在新 Hilbert 范数下仍最大增生。有限阶 (3.1) 只改变一个有限乘法常数，不改变指数 $\rho$。

以下固定足够小的 $\varepsilon$，在这个范数中工作，并省略下标。于是
$$
\|J-\kappa I\|\le\varepsilon,\qquad
\|J^{-1}\|\le2/|\kappa|
\tag{3.6}
$$
只要 $\varepsilon<|\kappa|/2$。

### 3.2 最高单位系数的真实图预算

高次剪切稿 §2 已从收缩半群的 Taylor 展开和有限 Vandermonde 反演证明
$$
\|X^ju\|
\le C_k\|u\|^{1-j/k}\|X^ku\|^{j/k},
\qquad 0<j<k.
\tag{3.7}
$$
它也支付自然 $X^k$ 的闭性。

由 (3.3)、(3.6) 及 (3.7) 吸收 $cX$，得到
$$
\boxed{
\|X^ku\|\le C_\varepsilon(\|Q_\pm u\|+\|u\|)
\quad(u\in\operatorname{Dom}X^k).
}
\tag{3.8}
$$
这里最高项 $J$ 是实际有界单位，不能仅用其一个字符代替。

### 3.3 窄扇形之外的准确右逆

置
$$
\beta=\alpha\kappa,\qquad R=|z|,\qquad
q_\pm(z)=cz\pm\beta z^k,
$$
并令
$$
F_\pm(z)=Q_\pm-q_\pm(z)I\mp\alpha Nz^k.
$$
在真实 $\operatorname{Dom}X^k$ 上，
$$
\boxed{
F_\pm(z)=(X-z)H_\pm(X,z),
}
\tag{3.9}
$$
其中
$$
H_\pm(X,z)
=cI\pm\alpha J\sum_{\ell=0}^{k-1}z^\ell X^{k-1-\ell}.
\tag{3.10}
$$

若
$$
-\operatorname{Re}q_\pm(z)\ge3\varepsilon R^k,
\tag{3.11}
$$
则最大增生预解和 $\|Nz^k\|\le\varepsilon R^k$ 的有界扰动给
$$
\|F_\pm(z)^{-1}\|\le(2\varepsilon R^k)^{-1}.
\tag{3.12}
$$
其像在真实 $\operatorname{Dom}X^k$。由方程、$|q_\pm(z)|=O(R^k)$ 和 (3.8)，对 $R\ge1$ 得
$$
\|X^kF_\pm(z)^{-1}\|\le C_\varepsilon.
$$
再由 (3.7)，
$$
\boxed{
\|X^jF_\pm(z)^{-1}\|
\le C_\varepsilon R^{j-k}
\quad(0\le j\le k).
}
\tag{3.13}
$$
于是 (3.10) 的各项都给
$$
\|H_\pm(X,z)F_\pm(z)^{-1}\|\le C_\varepsilon/R.
\tag{3.14}
$$

该乘积确实映入 $\operatorname{Dom}X$，因为 $F_\pm^{-1}$ 映入
$\operatorname{Dom}X^k$，而 $H_\pm$ 次数为 $k-1$。所以 (3.9) 给实际右逆；$X-z$ 的已知唯一逆遂满足
$$
\boxed{
(X-z)^{-1}=H_\pm(X,z)F_\pm(z)^{-1}.
}
\tag{3.15}
$$
这里不要求无界 $H_\pm$ 自身可逆。

### 3.4 扇形可任意窄

主符号的 $2k$ 条零射线为
$$
\operatorname{Re}(\beta e^{ik\theta})=0.
$$
先任选 $\nu>\rho$，再选
$$
0<h<\min\{\pi/(4k),\pi/(4\nu)\}.
$$
最后取 (3.4) 的 $\varepsilon$ 足够小，使
$$
4\varepsilon<|\kappa|\sin(kh).
\tag{3.16}
$$

在这 $2k$ 条零射线的角半宽 $h$ 扇形之外，
$$
|\operatorname{Re}(\beta z^k)|
\ge|\kappa|\sin(kh)R^k>4\varepsilon R^k.
$$
又因 $k\ge2$，充分大 $R$ 时 $cR\le\varepsilon R^k$。选取适当正负号，便有
$$
-\operatorname{Re}q_\pm(z)
=|\operatorname{Re}(\beta z^k)|-c\operatorname{Re}z
\ge3\varepsilon R^k.
$$
因此 (3.14)—(3.15) 在所有这些扇形外给统一 $C_\varepsilon/R$ 界。

在任一个剩余扇形内，旋转坐标为 $w=e^{-i\theta_0}z$，则
$|\arg w|\le h$。对预解的任意矩阵元 $f(z)$，考虑
$$
f(z)\exp(-\delta w^\nu),\qquad \delta>0.
$$
在此扇形中选定解析支，且
$$
\operatorname{Re}w^\nu
\ge|w|^\nu\cos(\nu h)>0.
$$
有限阶增长 $\exp(CR^\rho)$ 被 $\exp(-\delta cR^\nu)$ 压制。对内半径固定、外半径趋于无穷的截断扇形使用最大模原理，得到边界与内圆共同的固定界；再令 $\delta\downarrow0$，得到 $f$ 在整个扇形有界。

各矩阵元的边界预算可统一取为算子范数界，所以整个预解在全平面有界。Liouville 定理使其为常算子，而负实轴上的最大增生预解界
$\|(X+t)^{-1}\|\le1/t$ 迫它为零。这与它是逆矛盾，抽象引理得证。

## 4. 原完整 Bell 核先送到自然 $S=YL^k$ 的核

固定 $\lambda,r,w$，令 $D=rM$。先构造原完整
$[F(x,y)-\lambda]^r$ 的全部混合 Bell 多项式，再通过实际有界代换
$$
x_{\rm old}=Z+H_0,\qquad
y_{\rm old}=Y+R_0Z+K_0,\qquad H_0,R_0,K_0\in\mathfrak C=A'
$$
写成有限核心 $P(Z,Y)$。这些代换在已付共同自然深域上准确；原规范 Bell 仍由原循环图核心固定，不替换原 cumulant 或指数权。

在权 $(1,k)$ 下，正阶微分和这些有界平移严格降权，且关于 $y$ 的首一性保留。因此
$$
\widehat P(t,s)
=t^{kD}P(t^{-1},t^{-k}s)
=H(s)^r I+tE(t,s)
\in\mathfrak C[t,s],
\tag{4.1}
$$
关于 $s$ 首一、次数为 $D$，且 $\deg_sE<D$。

定义真实自然闭算子
$$
S=YL^k,\qquad
\operatorname{Dom}S=\{x:L^kx\in\operatorname{Dom}Y\}.
\tag{4.2}
$$
它闭，因为 $Y$ 闭、$L^k$ 有界；其域包含共同正则深域，故稠密。其完整图与全部 $\mathfrak C$ 交换。

代入有界 $L$ 得自然首一多项式
$$
Q(S)=\widehat P[L](S)
=S^D+\sum_{j<D}B_jS^j,\qquad
B_j\in\mathfrak C,
\quad\operatorname{Dom}Q=\operatorname{Dom}S^D.
\tag{4.3}
$$
这里所有系数只含非负有限 $L$ 次数。

若原规范最大 Bell 核含 $0\ne f$，把全部原倾斜 first 及 $Z,Y$ 纳入同一个 R186 有限正则族，取同一单射共同正则器 $\mathcal R$，选充分大的有限 $N\ge kD+2$。则
$$
h=\mathcal R^Nf\ne0
$$
进入所有所需长度至多 $kD$ 的实际词域，并仍满足原 $\mathcal Ph=0$。

因此 $h\in\operatorname{Dom}S^D$，且准确有
$$
\boxed{
Q(S)h=L^{kD}P(Z,Y)h=0.
}
\tag{4.4}
$$
没有声称原规范 Bell 域等于 $\operatorname{Dom}S^D$；这里只把一个核向量通过实际单射正则器送入自然核。

## 5. 真实相伴核图及有限非零谱

定义
$$
\Gamma=
\{(h,Sh,\ldots,S^{D-1}h):
h\in\operatorname{Dom}S^D,\ Q(S)h=0\}
\subseteq H^D.
\tag{5.1}
$$
由 (4.4)，$\Gamma\ne0$。

$\Gamma$ 闭：若其坐标分别收敛，前 $D-1$ 层用 $S$ 闭性识别；最高一层利用
$$
S^Dh=-\sum_{j<D}B_jS^jh
$$
的右侧收敛，再用最后一次 $S$ 闭性识别。

每个 $B_j$ 保持 $\operatorname{Dom}S$，所以同一等式的右侧也属于
$\operatorname{Dom}S$。故原 $h$ 自动进入 $\operatorname{Dom}S^{D+1}$，且
$Q(S)Sh=0$。逐次归纳可继续所有有限层。于是对角 $S$ 保持 $\Gamma$，并由有界相伴矩阵给出
$$
J=S^{(D)}|_\Gamma\in B(\Gamma).
\tag{5.2}
$$
全部对角 $\mathfrak C$ 保持 $\Gamma$ 并与 $J$ 交换。尤其对角 $L$ 的限制
$L_\Gamma$ 仍拟幂零。

从 (4.1)、(4.3) 的有限多项式恒等式得到
$$
\boxed{
H(J)^r=-L_\Gamma E[L_\Gamma](J).
}
\tag{5.3}
$$
右侧是一个拟幂零算子：$L_\Gamma$ 拟幂零，并与后面的有界算子交换。于是多项式谱映射给
$$
\boxed{\sigma(J)\subseteq\{s:H(s)=0\}.}
\tag{5.4}
$$
这是实际有界算子谱结论，不靠某个未知子空间上的字符等式。

由 (1.6)，右侧是一个有限非零集合。取一个非零 Riesz 分支
$\mathcal M\subseteq\Gamma$，使
$$
\sigma(J|_\mathcal M)=\{\kappa\},\qquad\kappa\ne0.
\tag{5.5}
$$
它是非零闭空间。因为每个对角 $A'$ 与 $J$ 交换，Riesz 投影也与其交换，所以 $\mathcal M$ 仍被全部对角 $A'$ 保持。

此处没有要求 $\Gamma$ 或 $\mathcal M$ 被原反射共轭 $C$ 保持。

## 6. $\mathcal M$ 上的完整自然域和两个最大增生多项式

以下省略有限对角放大的记号。令
$$
X=Z_\mathcal M,\qquad L_\mathcal M=X^{-1}.
$$
所有 $Z$ 的预解属于 $A'$ 并保持 $\mathcal M$，所以它的自然部分 $X$ 最大增生、空谱；实际预解是原预解的限制，有限阶 (1.3) 也保留。

取固定充分大的 $c$，令 $\alpha=e^{-i\psi}$。原两个实际 first
$$
A_\pm=cZ\pm\alpha Y
$$
已由共享位移预算证明最大增生；其预解属于 $A'$，所以其自然部分
$(A_\pm)_\mathcal M$ 也最大增生。稠密域由预解/Yosida 强逼近支付。

### 6.1 在全部 $\operatorname{Dom}X^k$ 上识别 $Y$

由 (5.2)，整个 $\mathcal M$ 都在自然 $S$ 域内，并且
$S|_\mathcal M=J$。对任意 $x\in\operatorname{Dom}X^k$，取
$$
y=X^kx\in\mathcal M.
$$
因为 $L_\mathcal M^ky=x$，自然定义 (4.2) 直接给
$$
x\in\operatorname{Dom}Y,\qquad
Yx=S y=JX^kx\in\mathcal M.
$$
所以准确有
$$
\boxed{
Y_\mathcal M x=JX^kx
\quad(x\in\operatorname{Dom}X^k).
}
\tag{6.1}
$$
这不只是在一个形式核心上的关系。

定义
$$
Q_\pm=cX\pm\alpha JX^k,\qquad
\operatorname{Dom}Q_\pm=\operatorname{Dom}X^k.
\tag{6.2}
$$
它们是 $(A_\pm)_\mathcal M$ 的限制。具体而言，取同一有限族的共同正则器逼近 $x$，它保持 $\mathcal M$，并在 $X^k,Y$ 图中同时收敛；在共同深域上 $A_\pm=cZ\pm\alpha Y$ 是准确自然式。原完整 $A_\pm$ 的闭性遂给所需包含。不预设一般自然和闭。

### 6.2 最高单位给准确满射，从而识别全部域

$J$ 在 $\mathcal M$ 上是有界单位，且与 $L_\mathcal M$ 交换。对每个 $\lambda\in\mathbb C$，
$$
(Q_\pm-\lambda)L_\mathcal M^k
=\pm\alpha J+cL_\mathcal M^{k-1}-\lambda L_\mathcal M^k.
\tag{6.3}
$$
右侧为有界单位：因 $k\ge2$，可提出 $\pm\alpha J$，剩下是
$I+$“拟幂零 $L_\mathcal M$ 乘有界交换子”。因此
$Q_\pm$ 在准确域 $\operatorname{Dom}X^k$ 上闭、空谱，真实逆为
$$
(Q_\pm-\lambda)^{-1}
=L_\mathcal M^k
\bigl(\pm\alpha J+cL_\mathcal M^{k-1}
-\lambda L_\mathcal M^k\bigr)^{-1}.
$$

取负实 $\lambda$。左边 $Q_\pm-\lambda$ 满射，而包含它的最大增生
$(A_\pm)_\mathcal M-\lambda$ 单射，所以两者的完整域和作用相等。于是
$$
\boxed{
cX\pm\alpha JX^k
\text{ 在准确域 }\operatorname{Dom}X^k
\text{ 都最大增生。}
}
\tag{6.4}
$$
现在 §3 的全部假设都已支付，包括有限阶增长、非零单谱簇、两个自然最高单位多项式的最大增生性。抽象引理给矛盾。

所以 $\Gamma=0$，原规范 Bell 核也为零。

## 7. 原循环性和具体新增范围

原完整规范 Bell 图仍为 $C$ 自伴，且原指数向量 $e^w$ 有 R186 的循环图核心。因此零核给像稠密，并有
$$
[\mathcal Pe^w]_A=\overline{\operatorname{Ran}\mathcal P}=H.
$$
$\mathcal Pe^w$ 正是 (1.7) 的原普通点态向量，定理1得证。

例如对任意 $1/2<\sigma<1$，取
$$
u=\sum_{j\ge0}(j+1)^{-\sigma}\chi_j,\qquad
v=i\sum_{j\ge0}(-1)^j(j+1)^{-\sigma}\chi_j.
$$
对所有 $k\ge2,m>1,\lambda\in\mathbb C,r\ge1$ 和复权 $w$，
$$
\boxed{
[(v-u^k)^m+u^{km-1}-\lambda]^r e^w
\text{ 循环。}
}
$$
这里
$$
t^{km}F(t^{-1},t^{-k}(1+t z))
=t^m z^m+t
$$
不满足原 $t^m$ 消失阶条件，所以不是前两篇平衡剪切乘积定理的改写。

更一般，(1.5) 下所有具有非零 $x^{kM}$ 系数的混合多项式均可使用，不要求已经给定剪切因式分解。

此前 Newton 非退化最高根条件成立时已有循环性，且部分旧范围允许更一般辅助行；该交集按旧来源扣除。本文新增的是有限阶预算下全部非零重簇及其不满足消失阶的余项。

有限阶增长是本稿额外支付的实质预算。谐和临界行、真正持久的零最高根簇、非整数 Newton 斜率，以及不落在固定复直线的独立复杂辅助骨架仍未由本文关闭。原真正常见证专属聚合上界、一般慢主理想和普通复 Hilbert ISP 也继续保持开放。
