# R150 附录：幂次好时间、全柱二分与圆序列预解预算

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。排序二分由根、kernel 与 normal 分别核验；本稿由 kernel 写出完整证明。

状态：完整证明；根代理已全文独立核查数列二分、真实半群预算、好圆最大模及全部自然域接口。

范围扣除：[旧排序二分](R150-appendix-counting-column-budget-dichotomy-and-all-real-controlled-shears.md)已把 $t\log t$ 好时间与归一化柱预算结合，用于平衡剪切；[有限阶非零簇稿](R150-appendix-finite-order-resolvent-narrow-sectors-and-all-nonzero-leading-clusters.md)已在全局有限阶整预解下移除最高重根的消失阶条件；[高次全柱稿](R150-appendix-polynomial-column-tests-and-invertible-normalized-parts.md)已证明实际柱条件下 $YZ^{-k}$ 不存在非零有界可逆完整部分。本稿不重计这三条结论。新增的是更强的数列二分、仅沿圆序列的预解增长条件及其完整窄扇形证明，最后据此删除正主行的全部计数和排序增长假设。

## 1. 原函数与无额外增长假设的结论

设
$$
a_j\ge0,\qquad a\in\ell^2\setminus\ell^1,\qquad
b\in\ell^2(\mathbb R),\qquad |b_j|\le C_0a_j
$$
且 $C_0<\infty$。固定任意 $\psi\in\mathbb R$、$\gamma,u_*,v_*\in\mathbb C$。取
$$
u=u_*+\sum_j(a_j+d_j^0+e_j^0)\chi_j,\qquad
v=v_*+\sum_j(e^{i\psi}b_j+\gamma a_j+d_j^1+e_j^1)\chi_j,
\tag{1.1}
$$
其中
$$
d_j^\nu=0\quad(a_j=0),\qquad
K_\nu^2:=\sum_{a_j>0}\frac{|d_j^\nu|^2}{a_j}<\infty,\qquad
e^\nu\in\ell^1(\mathbb C),\quad \nu=0,1.
\tag{1.2}
$$
这些都是原指定点态行；不先改变它们的 Bell 系数。

固定整数 $k\ge2$。令标量多项式 $F(x,y)$ 关于 $y$ 首一、次数 $M\ge1$，满足
$$
i+kj\le kM\qquad([x^iy^j]F\ne0).
\tag{1.3}
$$
定义其最高权符号
$$
H(s)=\sum_{i+kj=kM}[x^iy^j]F\,s^j.
$$
只要求
$$
\boxed{H(0)\ne0.}
\tag{1.4}
$$
因此全部最高根都非零，但允许任意重数，不要求各重根附近的低阶系数满足任何有限消失阶条件。

**定理 1。** 对 (1.1)—(1.4)，以及全部 $\lambda\in\mathbb C$、整数 $r\ge1$ 和复 $\ell^2$ first 指数权 $e^w$，
$$
\boxed{
[F(u,v)-\lambda]^r e^w
\text{ 是原实际 }A\text{ 的循环向量。}
}
\tag{1.5}
$$
这里没有对 $a$ 加下降重排下界、规则变差、计数上限、计数下限或尾平方比假设。

若正主行满足下文的柱分支，则 $e^{i\psi}b$ 还可换成任意复行 $c$，只需 $|c_j|\le C_0a_j$。一般复受控行在另一分支仍未由本稿覆盖。

## 2. 幂次好时间或小尾柱预算：完整数列二分

令
$$
r_1\ge r_2\ge\cdots>0,\qquad r\in\ell^2\setminus\ell^1,
$$
并记
$$
S_n=\sum_{j\le n}r_j,\qquad
G_n^2=\sum_{j>n}r_j^2,\qquad
\Theta(t)=\sum_j\lfloor tr_j\rfloor.
$$
每个固定 $t$ 的计数和有限，因为只有有限个 $r_j\ge1/t$。

**引理 2。** 下列两项至少有一项成立：

- 存在 $p>1$、$c>0$ 及 $t_\ell\to\infty$，使
  $$
  \boxed{\Theta(t_\ell)\ge c\,t_\ell^p.}
  \tag{2.1}
  $$
- 有
  $$
  \boxed{\liminf_{n\to\infty}\frac{nG_n^2}{S_n^2}=0.}
  \tag{2.2}
  $$

允许两项同时成立。(2.1) 只要求一列好时间，不要求所有充分大时间。

### 2.1 无幂次好时间迫全部次幂以下的部分和增长

假设 (2.1) 不成立。则对每个 $\varepsilon>0$，
$$
\Theta(t)=o(t^{1+\varepsilon}),
$$
特别存在有限 $C_\varepsilon$，使充分大 $t$ 时
$$
\Theta(t)\le C_\varepsilon t^{1+\varepsilon}.
\tag{2.3}
$$

取 $t_n=2/r_n$。对 $j\le n$，$t_nr_j\ge2$，所以
$$
\Theta(t_n)\ge\frac{t_n}{2}S_n.
$$
结合 (2.3)，
$$
S_n\le2C_\varepsilon(2/r_n)^\varepsilon,
\qquad
\boxed{r_n S_n^{1/\varepsilon}\le C'_\varepsilon.}
\tag{2.4}
$$
令 $\beta=1+1/\varepsilon>1$。由 $S_n-S_{n-1}=r_n$ 和中值定理，
$$
S_n^\beta-S_{n-1}^\beta
\le\beta r_n S_n^{\beta-1}
\le\beta C'_\varepsilon.
$$
求和得
$$
\boxed{S_n=O\bigl(n^{\varepsilon/(1+\varepsilon)}\bigr).}
\tag{2.5}
$$

任给 $\delta>0$，可以先选 $\varepsilon>0$ 使
$\varepsilon/(1+\varepsilon)<\delta$。因此
$$
\boxed{S_n/n^\delta\longrightarrow0
\quad\text{对每个 }\delta>0.}
\tag{2.6}
$$
这一步不使用任何系数逐项幂率。

### 2.2 未来最大点与完整尾平方预算

以下给出旧排序稿 §1.2 中未来最大点论证的完整形式，以明确新二分所需的精确量词。

固定 $0<\delta<1/2$ 和任意整数 $N$。由 (2.6)，正数列
$S_n/n^\delta$ 在 $n\ge N$ 上的最大值由某个有限 $m\ge N$ 取到。故对每个 $\ell\ge1$，
$$
\sum_{j=1}^{\ell}r_{m+j}
\le S_m\left[\left(\frac{m+\ell}{m}\right)^\delta-1\right].
\tag{2.7}
$$
置
$$
x_j=r_{m+j},\qquad
y_j=\frac{S_m}{m^\delta}
\bigl[(m+j)^\delta-(m+j-1)^\delta\bigr].
$$
两列均非负递减，且每个有限前缀满足
$\sum_{j\le\ell}x_j\le\sum_{j\le\ell}y_j$。

固定 $L$，令 $A_\ell=\sum_{j\le\ell}(x_j-y_j)\le0$。
离散分部求和给
$$
\sum_{j=1}^Lx_j(x_j-y_j)
=x_LA_L+\sum_{j=1}^{L-1}(x_j-x_{j+1})A_j\le0.
$$
再用 Cauchy–Schwarz，
$$
\sum_{j\le L}x_j^2
\le\sum_{j\le L}x_jy_j
\le
\left(\sum_{j\le L}x_j^2\right)^{1/2}
\left(\sum_{j\le L}y_j^2\right)^{1/2}.
$$
于是 $\sum_{j\le L}x_j^2\le\sum_{j\le L}y_j^2$；令 $L\to\infty$。

每个单位区间的积分 Cauchy–Schwarz 给
$$
\begin{aligned}
\sum_{j\ge1}y_j^2
&=\frac{\delta^2S_m^2}{m^{2\delta}}
\sum_{j\ge1}
\left(\int_{m+j-1}^{m+j}x^{\delta-1}\,dx\right)^2\\
&\le\frac{\delta^2S_m^2}{m^{2\delta}}
\int_m^\infty x^{2\delta-2}\,dx\\
&=\frac{\delta^2}{1-2\delta}\frac{S_m^2}{m}.
\end{aligned}
$$
所以
$$
\boxed{
\frac{mG_m^2}{S_m^2}\le\frac{\delta^2}{1-2\delta}.
}
\tag{2.8}
$$
$N$ 任意，故这给原数列下极限的上界。再令 $\delta\downarrow0$，得到 (2.2)。引理 2 证毕。

## 3. 实际幂次好时间给一列整预解圆周界

回到 (1.1)—(1.2)，置
$$
\zeta=a+d^0,\qquad Z=X_\zeta+\omega I,\qquad L=Z^{-1},
\qquad Y=e^{i\psi}X_b.
\tag{3.1}
$$
采用[复加权主行稿 §§2—4](R150-appendix-weighted-complex-main-real-controlled-skeleton-and-all-shear-powers.md)已支付的同一充分大实位移 $\omega$。于是 $Z$ 空谱、最大增生，全部预解属于 $A'$，$L$ 有界、单射、拟幂零；对每个充分大的实 $c$，
$$
cZ\pm e^{-i\psi}Y
$$
的原实际第一阶实现均最大增生。

本节不另换一个依赖好时间的位移。

### 3.1 加权主误差及有限物理头只扣线性成本

取
$$
B=\{j:|d_j^0|>a_j/2\}.
$$
由 (1.2)，$\sum_Ba_j\le4K_0^2<\infty$。补集上
$|\zeta_j|\ge a_j/2$，所以
$$
\Theta_{|\zeta|}(s)
\ge\Theta_a(s/2)-\frac s2\sum_Ba_j.
\tag{3.2}
$$

同一复加权主行稿 §4 的真实局部指数、可和相位补偿及有限集合半群分解，给固定 $T>0$、整数 $J$ 和 $\kappa>0$：
$$
\boxed{
\|e^{-tZ}\|
\le
\exp\left[-\kappa T
\sum_{j\ge J}\left\lfloor\frac{t|\zeta_j|}{T}\right\rfloor
\right]\qquad(t\ge0).
}
\tag{3.3}
$$
这里使用已经识别的无界半群，不使用形式无穷复指数乘积。删除前 $J$ 个物理位又只扣 $O(t)$。

假设正行的计数满足 (2.1)。取 $\tau_\ell=2Tt_\ell$。
由 (3.2)—(3.3)，存在 $\gamma>0$，使丢掉有限个指标后
$$
\boxed{
\|e^{-\tau_\ell Z}\|\le e^{-\gamma\tau_\ell^p},
\qquad \tau_\ell\to\infty.
}
\tag{3.4}
$$
因为 $p>1$，两个 $O(\tau_\ell)$ 成本均被 $\tau_\ell^p$ 吸收。实际物理排列完全任意。

### 3.2 按一个好时间分块的全半平面预算

令
$$
R_\ell=\frac{\gamma}{2}\tau_\ell^{p-1},
\qquad
\rho=\frac p{p-1}.
\tag{3.5}
$$
取子列使 $R_\ell$ 严格增加。$Z$ 最大增生，故其半群收缩。
对 $t=q\tau_\ell+s$，$q\ge0$、$0\le s<\tau_\ell$，
$$
\|e^{-tZ}\|\le\|e^{-\tau_\ell Z}\|^q.
$$
因此
$$
\begin{aligned}
\sup_{\operatorname{Re}z\le R_\ell}
\int_0^\infty |e^{tz}|\,\|e^{-tZ}\|\,dt
&\le
\frac{(e^{R_\ell\tau_\ell}-1)/R_\ell}
{1-e^{R_\ell\tau_\ell}\|e^{-\tau_\ell Z}\|}\\
&\le \frac{2e^{R_\ell\tau_\ell}}{R_\ell}
\end{aligned}
\tag{3.6}
$$
对充分大 $\ell$ 成立，因为分母中的乘积至多
$e^{-\gamma\tau_\ell^p/2}$。

该范数积分在一个包含所示闭半平面的开半平面内收敛。它在左半平面等于真实预解；由解析延拓及 $Z$ 空谱，在整个该区域仍等于 $(Z-z)^{-1}$。所以
$$
\boxed{
\sup_{\operatorname{Re}z\le R_\ell}\|(Z-z)^{-1}\|
\le C\exp(CR_\ell^\rho).
}
\tag{3.7}
$$
特别，
$$
\boxed{
\sup_{|z|=R_\ell}\|(Z-z)^{-1}\|
\le C\exp(CR_\ell^\rho),\qquad R_\ell\to\infty.
}
\tag{3.8}
$$
没有从 (3.8) 断言圆周之间也满足同一个有限阶函数。

任意有限放大、任意被全部对角 $A'$ 保持的闭空间上的自然部分，均继承 (3.8)：其预解是环境预解的真实限制。固定等价 Hilbert 范数只改变有限乘法常数，也保留同一 $\rho$ 和同一圆序列。

## 4. 仅凭好圆的完整窄扇形排除引理

本节精确替换有限阶非零簇稿 §3 的全局增长假设，其余自然域不放宽。

**引理 4。** 设非零 Hilbert 空间上的 $X$ 最大增生、空谱，且有某些 $C,\rho<\infty$、$R_\ell\to\infty$，满足
$$
\sup_{|z|=R_\ell}\|(X-z)^{-1}\|
\le C e^{CR_\ell^\rho}.
\tag{4.1}
$$
设 $J$ 有界并与 $X$ 的全部预解交换，
$$
\sigma(J)=\{\kappa\},\qquad \kappa\ne0.
$$
固定 $k\ge2$、$c\ge0$、$|\alpha|=1$。则下列两个算子不可能同时在所示准确自然域上最大增生：
$$
Q_\pm=cX\pm\alpha JX^k,\qquad
\operatorname{Dom}Q_\pm=\operatorname{Dom}X^k.
\tag{4.2}
$$

### 4.1 既保增生性又缩小拟幂零误差的 Hilbert 范数

写 $N=J-\kappa I$。它拟幂零。对任意 $\varepsilon>0$，
$$
\|h\|_\varepsilon^2
=\sum_{n\ge0}\varepsilon^{-2n}\|N^nh\|^2
\tag{4.3}
$$
定义一个等价 Hilbert 范数，并有 $\|N\|_\varepsilon\le\varepsilon$。
与 $N$ 交换的每个原收缩半群在此范数中仍收缩，因为可逐项交换后求和。

$N$ 与 $X$ 的预解、自然 $Q_\pm$ 及其预解交换，故三者的半群都满足这一条件。因而 $X,Q_\pm$ 在新范数中仍最大增生，(4.1) 只改变常数。以下在此范数中工作，取 $\varepsilon<|\kappa|/2$，使
$$
\|N\|\le\varepsilon,\qquad \|J^{-1}\|\le2/|\kappa|.
\tag{4.4}
$$

### 4.2 真实右逆及扇形外预算

收缩半群 Taylor/Vandermonde 插值已经在[高次剪切稿 §2](R150-appendix-all-polynomial-shears-fixed-complex-line-and-higher-companion-parts.md)支付：
$$
\|X^jh\|
\le C_k\|h\|^{1-j/k}\|X^kh\|^{j/k},
\qquad 0<j<k,\quad h\in\operatorname{Dom}X^k.
\tag{4.5}
$$
最高系数 $J$ 是实际单位，利用 (4.5) 吸收 $cX$ 得
$$
\|X^kh\|\le C_\varepsilon(\|Q_\pm h\|+\|h\|).
\tag{4.6}
$$

置
$$
\beta=\alpha\kappa,\quad R=|z|,\quad
q_\pm(z)=cz\pm\beta z^k,\quad
F_\pm(z)=Q_\pm-q_\pm(z)I\mp\alpha Nz^k.
$$
在准确 $\operatorname{Dom}X^k$ 上，
$$
F_\pm(z)=(X-z)H_\pm(X,z),
\qquad
H_\pm(X,z)=cI\pm\alpha J\sum_{j=0}^{k-1}z^jX^{k-1-j}.
\tag{4.7}
$$
若
$$
-\operatorname{Re}q_\pm(z)\ge3\varepsilon R^k,
\tag{4.8}
$$
最大增生预解和有界扰动给
$$
\|F_\pm(z)^{-1}\|\le(2\varepsilon R^k)^{-1}.
$$
其像在真实 $\operatorname{Dom}X^k$。由方程、(4.6) 及 (4.5)，对 $R\ge1$，
$$
\|X^jF_\pm(z)^{-1}\|\le C_\varepsilon R^{j-k},
\qquad 0\le j\le k.
\tag{4.9}
$$
所以
$$
\|H_\pm(X,z)F_\pm(z)^{-1}\|\le C_\varepsilon/R.
\tag{4.10}
$$
这个乘积的像确实在 $\operatorname{Dom}X$：逆的像先在
$\operatorname{Dom}X^k$，而 $H_\pm$ 的次数为 $k-1$。
(4.7) 遂给真实右逆，唯一性给
$$
\boxed{
(X-z)^{-1}=H_\pm(X,z)F_\pm(z)^{-1}.
}
\tag{4.11}
$$
没有要求无界第二因子 $H_\pm$ 自身可逆。

任选 $\nu>\rho$，再选
$$
0<h<\min\{\pi/(4k),\pi/(4\nu)\}.
$$
最后令 $\varepsilon$ 足够小，使
$4\varepsilon<|\kappa|\sin(kh)$。
在 $2k$ 条射线
$\operatorname{Re}(\beta e^{ik\theta})=0$
的角半宽 $h$ 扇形之外，
$$
|\operatorname{Re}(\beta z^k)|
\ge|\kappa|\sin(kh)R^k>4\varepsilon R^k.
$$
充分大 $R$ 时 $cR\le\varepsilon R^k$。选取适当正负号即得 (4.8)，所以这些扇形外一致有
$$
\|(X-z)^{-1}\|\le C_\varepsilon/R.
\tag{4.12}
$$

### 4.3 最大模原理只取已付的外圆

固定一个剩余扇形，中心角为 $\theta_0$，取足够大的固定内半径 $R_0$。
对任意单位向量 $f,g$，记整函数
$$
\varphi(z)=\langle(X-z)^{-1}f,g\rangle.
$$
在扇形中取 $w=e^{-i\theta_0}z$ 的一致解析幂支。
对 $\delta>0$，
$$
\varphi_\delta(z)=\varphi(z)e^{-\delta w^\nu}.
$$
因为 $|\arg w|\le h$，
$$
\operatorname{Re}w^\nu\ge |z|^\nu\cos(\nu h)>0.
$$

在两条边界射线和内圆上，(4.12) 与紧集上的预解界给某个固定 $M$，一致于单位 $f,g$，且与 $\delta$ 无关。
只在外半径等于 $R_\ell$ 的截断扇形使用最大模原理。该外弧上由 (4.1)，
$$
|\varphi_\delta(z)|
\le C\exp\left(CR_\ell^\rho-
\delta\cos(\nu h)R_\ell^\nu\right)\longrightarrow0.
\tag{4.13}
$$
因此对每个固定 $\delta>0$，让 $\ell\to\infty$ 得
$|\varphi_\delta|\le M$；再令 $\delta\downarrow0$ 得
$|\varphi|\le M$。

这一步只用了所选外圆上的 (4.1)，没有使用两个相邻好圆之间的任何增长估计。有限个扇形外已有 (4.12)，所以整个预解在全平面有界。Liouville 定理作用于各矩阵元，给常算子预解；负实轴上的最大增生界
$\|(X+t)^{-1}\|\le1/t$ 迫该常数为零，与真实逆矛盾。引理 4 证毕。

## 5. 两条分支在同一原完整 Bell 核上合流

本节把新数列二分与已付柱定理接起来，并明确未知闭图上的域接口。

### 5.1 原 Bell、固定正则器和真实自然相伴图

固定 $\lambda,r,w$，令 $D=rM$。首先使用原 (1.1) 和原指数权，构造
$[F(u,v)-\lambda]^r e^w$ 的全部混合 Bell 实现。
在此之后，复加权主行稿的真实有界系数代换才把其核心写成 $P(Z,Y)$：
$$
x_{\rm old}=Z+H_0,\qquad
y_{\rm old}=Y+R_0Z+K_0,\qquad H_0,R_0,K_0\in A'.
$$
这些代换只降权；正阶 Bell 微分也严格降权。因而
$$
\widehat P(t,s)=t^{kD}P(t^{-1},t^{-k}s)
=H(s)^rI+tE(t,s),\qquad \deg_sE<D.
\tag{5.1}
$$
原所有 mixed cumulant 和原点态幂保持不变。

定义自然闭算子
$$
S=YL^k,\qquad
\operatorname{Dom}S=\{h:L^kh\in\operatorname{Dom}Y\}.
\tag{5.2}
$$
闭性来自 $Y$ 闭、$L^k$ 有界；稠密域由共同正则器支付。令
$$
Q(S)=\widehat P[L](S)
=S^D+\sum_{j<D}B_jS^j,
\qquad B_j\in A',
\quad\operatorname{Dom}Q=\operatorname{Dom}S^D.
$$
不预设这个自然多项式在全空间上已经闭。

若原规范最大 Bell 核含 $f\ne0$，把全部原倾斜 first 及 $Z,Y$ 纳入
[R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)
的同一有限正则族。其单射正则器 $\mathcal R$ 的固定幂
$h=\mathcal R^Nf$，$N\ge kD+2$，进入所有所需实际词域，仍非零，并满足
$$
Q(S)h=L^{kD}P(Z,Y)h=0.
\tag{5.3}
$$
这里只把一个规范核向量送入自然核，没有等同两个完整域。

取真实核相伴图
$$
\Gamma=
\{(h,Sh,\ldots,S^{D-1}h):
h\in\operatorname{Dom}S^D,\ Q(S)h=0\}\subset H^D.
$$
它闭：前 $D-1$ 层用 $S$ 闭性，最高一层用
$S^Dh=-\sum_{j<D}B_jS^jh$ 的坐标收敛，再用 $S$ 闭性。
同一等式和有界系数保域逐次升级所有有限幂，所以对角 $S$ 保持 $\Gamma$，其完整部分
$$
J=S^{(D)}|_\Gamma
$$
由有界相伴矩阵给出。全部对角 $A'$ 保持 $\Gamma$ 并与 $J$ 交换。

对角 $L$ 的限制 $L_\Gamma$ 仍拟幂零；(5.1) 给
$$
H(J)^r=-L_\Gamma E[L_\Gamma](J).
$$
右侧拟幂零，故谱映射给
$$
\boxed{\sigma(J)\subseteq H^{-1}(0).}
\tag{5.4}
$$
由 (1.4)，$J$ 为实际有界单位。这些域和谱步骤正是有限阶非零簇稿 §§4—5 的接口，它们本身不使用有限阶增长或辅助行的实性。

### 5.2 小尾分支使用实际高次全柱定理

将正 $a$ 的非零系数下降重排为 $(r_n)$。若 (2.2) 成立，取最大的 $n$ 个系数所在的实际物理位，再并入前 $n$ 个物理位，沿小尾子列取 $F_n$。

高次全柱稿 §6 已逐项证明：对同一
$Z=X_{a+d^0}+\omega$、$Y=e^{i\psi}X_b$，这些集合递增穷尽，且
$$
|\sigma_n|\to\infty,\quad
\frac{\sum_{F_n}(|\zeta_j|+|e^{i\psi}b_j|)}{|\sigma_n|}\le C,
\quad
\frac{\sqrt{|F_n|}\,
(\|\zeta_{F_n^c}\|_2+\|b_{F_n^c}\|_2)}
{|\sigma_n|}\to0,
$$
其中 $\sigma_n=\omega+\sum_{F_n}\zeta_j$。
加权主误差的关键项为
$$
\frac{|F_n|\|d^0_{F_n^c}\|_2^2}
{\left(\sum_{F_n}a_j\right)^2}
\le\frac{2K_{0,n}^2}{S_n}\to0.
$$
因此该稿定理 1 直接排除 (5.4) 所给的非零有界可逆完整部分 $J$。

这个分支允许原骨架 $e^{i\psi}b$ 换成任意复受控行 $c$，其余 weighted 与 $\ell^1$ 误差仍按原完整 Bell 处理。

### 5.3 幂次好时间分支及完整自然域

若 (2.1) 成立，§3 给 $Z$ 的好圆预解界。
由 (5.4)，取一个非零 Riesz 分支 $\mathcal M\subseteq\Gamma$，使
$\sigma(J|_\mathcal M)=\{\kappa\}$、$\kappa\ne0$。
它仍被全部对角 $A'$ 保持。省略有限放大记号，令
$$
X=Z_\mathcal M,\qquad \alpha=e^{-i\psi}.
$$
$X$ 最大增生、空谱，并继承 §3 的同一好圆界。

整个 $\mathcal M$ 都属于 $\operatorname{Dom}S$。
任取 $x\in\operatorname{Dom}X^k$，由
$X^kx\in\mathcal M$ 和 $L_\mathcal M^kX^kx=x$，
自然定义 (5.2) 准确给
$$
x\in\operatorname{Dom}Y,\qquad
Yx=JX^kx.
\tag{5.5}
$$
这在全部 $\operatorname{Dom}X^k$ 上成立，不只在一个形式核心上成立。

取共享位移已允许的充分大 $c$。原实际 first
$cZ\pm\alpha Y$ 及其在 $\mathcal M$ 上的自然部分都最大增生；
后者的预解、Yosida 稠密逼近由全部 $A'$ 不变性保留。
定义
$$
Q_\pm=cX\pm\alpha JX^k,\qquad
\operatorname{Dom}Q_\pm=\operatorname{Dom}X^k.
$$
同一 R186 正则器在 $X^k$ 和 $Y$ 图中同时逼近，结合 (5.5) 和原 first 闭性，给
$$
Q_\pm\subseteq(cZ\pm\alpha Y)_\mathcal M.
\tag{5.6}
$$
这里没有把一般自然和的闭性免费使用。

对任意 $\lambda\in\mathbb C$，
$$
(Q_\pm-\lambda)L_\mathcal M^k
=\pm\alpha J+cL_\mathcal M^{k-1}-\lambda L_\mathcal M^k
\tag{5.7}
$$
是实际有界单位：提出 $\pm\alpha J$ 后，余项是
$I+$“拟幂零 $L_\mathcal M$ 乘有界交换子”。
因此 $Q_\pm$ 在所示准确域上闭、空谱，逆由 (5.7) 乘 $L_\mathcal M^k$ 给出。
取负实 $\lambda$，$Q_\pm-\lambda$ 满射，而 (5.6) 右侧减 $\lambda$ 单射，所以两者完整域相等。于是 $Q_+,Q_-$ 都最大增生。

现在引理 4 的全部假设均已支付，得到矛盾。
此处没有把原 $C$ 自伴性或通常伴随同域传给 $\mathcal M$。

### 5.4 回到原指定点态向量

引理 2 保证 §5.2、§5.3 至少一条适用，所以原规范最大 Bell 核为零。
原完整 $C$ 自伴性和原指数向量的 R186 循环图核心给
$$
[\mathcal P e^w]_A=\overline{\operatorname{Ran}\mathcal P}=H.
$$
$\mathcal Pe^w$ 正是原指定 $[F(u,v)-\lambda]^r e^w$。
定理 1 得证。

## 6. 新范围和仍保留的边界

特别，对任意正 $a\in\ell^2\setminus\ell^1$、原 (1.1) 的全部误差和骨架，
所有 $k\ge2,m>1$ 都满足
$$
\boxed{
\big[(v-u^k)^m+u^{km-1}-\lambda\big]^r e^w
\text{ 对全部 }\lambda,r,w\text{ 循环。}
}
$$
其局部最高簇展开含 $t^m z^m+t$，通常不满足原平衡分簇的 $t^m$ 消失要求。
这里不再要求正行先落在一个已知的全局有限阶增长族中。

更一般，权 $(1,k)$ 下关于第二变量首一、$x^{kM}$ 系数非零的全部标量多项式均在结论内，无须给定剪切因式分解。先前已覆盖的非退化最高根、平衡剪切及多尺度乘积只作为交集引用，不重复计为本稿新结论。

本稿没有把一般复受控辅助在好时间分支也实化。仍需另解真正持久的零最高簇（既有多尺度平衡分解已闭范围除外）、非整数 Newton 斜率及无相应真实预算的独立复行。原正常见证专属聚合上界、一般慢主理想和普通复 Hilbert ISP 也未由本稿完成。
