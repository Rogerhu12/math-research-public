# R47：有限 Airy 试解、全部角频输出与真实物理源强界

2026-11-12，visible-exact-astra-f6a2。

**状态：有限正则的局部算子定理，尚未认证当前候选的所有系数输入。**
本篇支付 R45(6.3) 所需的特殊 Ai residual 强界。证明先逐个 Fourier
lag 作完整矩阵估计，再作真实的逐径向角图变换；不从单列 norm
直接推算子 norm，也不把任意 anisotropic source 的混合坐标变换
称为无损。结果与 R45 一起给同一个 full 正组件的归一 DN/Cayley
$4/3$ 余项。

这里使用普通有限 Sobolev 窗口。若要正 log 权，还须给实际复角
域或相应带权 amplitude 预算；有限光滑本身不支付它。

## 1. 全 lag 算子判据

角变量周期 $2\pi$，积分归一化为 $d\phi/(2\pi)$。
令 $b_j(r,\phi)$ 为实际函数，$r$ 在固定有限区间上。定义
$$
(Th)(r,\phi)=\sum_{j\in\mathbb Z}b_j(r,\phi)h_je^{ij\phi}.
\tag{1.1}
$$
设 $g\ge0$、$s\in\mathbb R$，取整数
$p>|s+g|+1$。假设存在同一个 $M$，对全部 $j$ 有
$$
\left\|\sup_\phi|b_j(r,\phi)|\right\|_{L^2_r},\quad
\left\|\sup_\phi|\partial_\phi^p b_j(r,\phi)|\right\|_{L^2_r}
\le M\langle j\rangle^{-g}.
\tag{1.2}
$$
均值 $j=0$ 也包括在输入内。

**命题 1.1。** 有真实强界
$$
\boxed{\quad
\|T:H^s\to L^2_rH^{s+g}_\phi\|\le L_{s,g,p}M,\quad}
\tag{1.3}
$$
其中令 $a=|s+g|$，可取
$$
L_{s,g,p}=2^{a/2}\left[1+2^{a/2+1}
 \left(1+\frac1{p-a-1}\right)\right].
\tag{1.4}
$$

**证明。** 对 $l\ne0$ 在角变量积分分部 $p$ 次，得到
$$
\|(b_j)_l\|_{L^2_r}\le
M|l|^{-p}\langle j\rangle^{-g};
$$
$l=0$ 用 (1.2) 第一式。固定 lag $l=k-j$ 时，输出只是一个
移位对角矩阵。对这个完整矩阵有
$$
\begin{aligned}
&\sum_j\int\langle j+l\rangle^{2(s+g)}
 |(b_j)_l(r)h_j|^2dr\\
&\qquad\le 2^a\langle l\rangle^{2a}
 M^2w_p(l)^2\sum_j\langle j\rangle^{2s}|h_j|^2,
\end{aligned}
\tag{1.5}
$$
其中 $w_p(0)=1$、$w_p(l)=|l|^{-p}$。先对这个固定 lag 取完整
$L^2_r\ell^2_j$ norm，然后对 $l$ 使用三角不等式。因为
$$
\sum_l\langle l\rangle^a w_p(l)
\le1+2^{a/2+1}\sum_{l\ge1}l^{a-p}
\le1+2^{a/2+1}\left(1+\frac1{p-a-1}\right),
$$
便得 (1.3)。先对有限输入证明，再由稠密性延伸。这个论证包括全部
输出频率、cross sign 和 mean，未将 $\sup_j$ 错移到径向积分外。$\square$

## 2. 正实轴 Airy 的显式有限导数和矩

记 $A(t)=\operatorname{Ai}(t)$、$a_0=A(0)>0$。
只使用 Airy 方程 $A''=tA$、正轴衰减解及其初值；标准初值与衰减
首项见 [DLMF 9.2](https://dlmf.nist.gov/9.2#ii)、
[DLMF 9.7.5–6](https://dlmf.nist.gov/9.7#ii)。以下界由方程证明。

正轴上 $A>0$、$A'<0$。例如若正轴有首个零点，之后由
$A''=tA$ 和过零方向不可能再趋于零，违背衰减条件；
$A''\ge0$ 与 $A'(\infty)=0$ 再给导数符号。
令 $W=A'^2-tA^2$，则 $W'=-A^2$ 且 $W(\infty)=0$，故
$-A'/A\ge\sqrt t$，从而
$$
0<A(t)\le a_0e^{-2t^{3/2}/3}.
\tag{2.1}
$$
又因 $(t+u)^{3/2}\ge t^{3/2}+u^{3/2}$，有
$$
W(t)=\int_t^\infty A(v)^2dv
\le a_0^2 c_0e^{-4t^{3/2}/3},\qquad
c_0=\frac23\left(\frac34\right)^{2/3}\Gamma(2/3).
$$
所以
$$
|A'(t)|\le a_0\sqrt{t+c_0}\,e^{-2t^{3/2}/3}
\le a_0(1+t+c_0)e^{-2t^{3/2}/3}.
\tag{2.2}
$$

为所有后续有限导数定义真实多项式
$$
P_0=1,\ Q_0=0,\qquad
P_{d+1}=P_d'+tQ_d,\quad Q_{d+1}=P_d+Q_d'.
\tag{2.3}
$$
准确有 $A^{(d)}=P_dA+Q_dA'$。用 $|P|_+$ 表示把系数取绝对值
所得的非负系数多项式，置
$$
H_d(t)=|P_d|_+(t)+(1+t+c_0)|Q_d|_+(t).
$$
于是
$$
\boxed{\quad |A^{(d)}(t)|\le
a_0H_d(t)e^{-2t^{3/2}/3},\qquad t\ge0.\quad}
\tag{2.4}
$$
这里只需有限次多项式递推，没有未量化的渐近余项。

对 $n\ge0$、$a>0$，所需矩有明确值
$$
\boxed{\quad
I_n(a)=\int_0^\infty z^ne^{-\frac43(az)^{3/2}}dz
=\frac23a^{-n-1}\left(\frac34\right)^{2(n+1)/3}
 \Gamma\!\left(\frac{2(n+1)}3\right).\quad}
\tag{2.5}
$$
因此每个有限非负多项式 $Q$ 的
$\int Q(z)^2e^{-4(az)^{3/2}/3}dz$ 都是一份明确有限和。
数值证书中可进一步把这些常数作有向区间包络；本篇无需给浮点值。

## 3. 真实混合坐标中的 Ai amplitude

在物理 collar $r\ge0$ 上，设真实坐标写为
$$
y=r\,a(r,\theta),\qquad \phi=H_r(\theta),
\qquad 0<a_-\le a\le a_+,
\quad 0<m\le\partial_\theta H_r\le M_H.
\tag{3.1}
$$
$H_r$ 是 degree-one 的实际圆图。令 $K_r=H_r^{-1}$，并写
$\widetilde a(r,\phi)=a(r,K_r\phi)$。
下列角导数上界全部是**同一真实图上的实际输入**：
$$
\sup|\partial_\phi^v\widetilde a|\le A_v\quad(v\ge1),
\qquad \sup|\partial_\phi^v c(r,\phi)|\le C_v.
\tag{3.2}
$$
其中 $c$ 可含实际 $J/t$、cutoff、系数和有限乘积，不能删掉它们。

固定 $k,d\in\mathbb N_0$、实数 $\alpha$ 和
$\lambda_j=q|j|$ ($j\ne0$, $q>0$)。考虑
$$
b_j(r,\phi)=r^k\lambda_j^\alpha c(r,\phi)
 A^{(d)}\!\left(r\widetilde a(r,\phi)\lambda_j^{2/3}\right).
\tag{3.3}
$$
允许另乘 $\operatorname{sgn}(j)$ 的固定幂，它不改变估计。
令 $\mathcal B_{v,u}$ 为指数型 partial Bell 多项式，约定
$\mathcal B_{0,0}=1$；其它不合法指标为零。即准确链式法则为
$$
\partial_\phi^v f(a)
=\sum_{u=0}^v f^{(u)}(a)
 \mathcal B_{v,u}(a',\ldots,a^{(v-u+1)}).
\tag{3.4}
$$
定义有限非负多项式
$$
\mathcal P_v(z)=\sum_{w=0}^v\binom vw C_{v-w}
 \sum_{u=0}^w
 \mathcal B_{w,u}(A_1,\ldots,A_{w-u+1})
 z^{k+u}H_{d+u}(a_+z),
\tag{3.5}
$$
其中 $w=u=0$ 项按约定直接为 $C_vz^kH_d(a_+z)$。
再置
$$
M_v^{\rm Ai}=a_0\left[
 \int_0^\infty\mathcal P_v(z)^2e^{-\frac43(a_-z)^{3/2}}dz
 \right]^{1/2}.
\tag{3.6}
$$
它由 (2.5) 完全明确计算。

**命题 3.1。** 令 $e=\alpha-2k/3-1/3$。则
$$
\left\|\sup_\phi|\partial_\phi^v b_j|\right\|_{L^2_r}
\le M_v^{\rm Ai}\lambda_j^e.
\tag{3.7}
$$
若 $e\le-g$，对全部非零频率可在 (1.2) 使用
$$
M=2^{g/2}q^e\max(M_0^{\rm Ai},M_p^{\rm Ai}).
\tag{3.8}
$$

**证明。** 链式法则每次打到 Airy 参数时带
$r\lambda_j^{2/3}\partial_\phi^v\widetilde a$，而非无条件的
$\lambda_j^{2/3}$。置 $z=r\lambda_j^{2/3}$，用 (2.4)、(3.2)
逐项界导数，得到
$$
\sup_\phi|\partial_\phi^v b_j|
\le a_0\lambda_j^{\alpha-2k/3}
 \mathcal P_v(z)e^{-\frac23(a_-z)^{3/2}}.
$$
平方后作真实径向积分 $dr=\lambda_j^{-2/3}dz$，便得 (3.7)。
最后 $|j|^e\le|j|^{-g}\le2^{g/2}\langle j\rangle^{-g}$，给 (3.8)。
对 $j=0$ 使用实际另给的列和它的两个 $L^2C^v$ norm，再与 (3.8)
取最大值。$\square$

这给所有频率共享的 lag 控制；它不是把逐列径向估计未经证明地
合并成算子。真正合并步骤正是命题 1.1。

## 4. 逐径向角图的普通 Sobolev 费用

这里明确支付最后一个 $\phi=H_r(\theta)$，不把 (3.3) 的输出坐标
直接当作物理角。对整数 $N\ge0$，设
$h_v=\sup_{r,\theta}|\partial_\theta^vH_r|$，并记
$$
D_0(H)=1,\qquad
D_n(H)=\sum_{k=1}^n\mathcal B_{n,k}(h_1,\ldots,h_{n-k+1}).
$$
准确链式法则、换元和 $H'\ge m$ 给
$$
\|C_{H_r}:H^N\to H^N\|
\le C_N^+(H):=m^{-1/2}
 \left(\sum_{n=0}^N\binom NnD_n(H)^2\right)^{1/2}.
\tag{4.1}
$$
这里 $C_Hu=u\circ H$，不是 half-density，也没有近恒等假设。

负阶由真实伴随 $C_H^*=M_{K'}C_K$ 支付。逆图的导数上界可递推为
$$
\kappa_1=m^{-1},\qquad
\kappa_n=m^{-1}\sum_{k=2}^n h_k
 \mathcal B_{n,k}(\kappa_1,\ldots,\kappa_{n-k+1})
\quad(n\ge2),
\tag{4.2}
$$
因为 $H\circ K=\mathrm{id}$，而 $K'\ge1/M_H$。
Leibniz 公式给
$$
\|M_{K'}:H^N\to H^N\|
\le U_N:=\left[\sum_{n=0}^N\binom Nn
 \left(\sum_{v=0}^n\binom nv\kappa_{v+1}\right)^2\right]^{1/2}.
\tag{4.3}
$$
故可取 $C_N^-(H)=U_N C_N^+(K)$ 作为 $H^{-N}$ norm。
在相邻整数之间作 Hilbert 插值，得到任意有限实阶 $t$ 的明确
$C_t(H)$。所有 sup 都同时覆盖 $r$，因此
$$
\|C_{H_r}v(r,\cdot)\|_{L^2_rH^t_\theta}
\le C_t(H)\|v\|_{L^2_rH^t_\phi}.
\tag{4.4}
$$
结合 (1.3)、(3.8)，特殊 Ai amplitude 从输入 $H^s$ 到实际
$L^2_rH^{s+g}_\theta$ 的 norm 至多 $C_{s+g}(H)L_{s,g,p}M$。
角图随径向变化不破坏这条结论，因为该 norm 中并无径向微分。
本命题不对任意 mixed source 变换作相同断言；它先使用了 Ai 参数
的真实 $y=r a$ 结构和全部 lag 估计。

## 5. 三阶 flat principal 已足够给所需 residual

在实际 canonical 正 collar 上，角仍取周期 $2\pi$，考虑
$$
P_{\rm can}=-\partial_y^2-q^2y\partial_\phi^2
-\partial_y(E_{11}\partial_y+E_{12}\partial_\phi)
-\partial_\phi(E_{12}\partial_y+E_{22}\partial_\phi)+V.
\tag{5.1}
$$
全部系数是当前实际拉回/height 后的系数。假设
$$
E_{ab}=y^3 e_{ab},\qquad
\partial_yE_{ab}=y^2\widetilde e_{ab},
\tag{5.2}
$$
所需有限角导数的 $e,\widetilde e,V$ 以及物理变换后的对应系数均有
实际一致界。没有以小振幅假定这些系数接近背景。

取实 cutoff $\chi(y)$，在 $[0,h/2]$ 为1，在 $[h,\infty)$ 为0，
并付所需有限导数。定义 $\lambda_j=q|j|$ ($j\ne0$)、$\lambda_0=1$，
以及实际试解
$$
\mathcal Qh=c\sum_{j\in\mathbb Z}
 \lambda_j^{-1/3}\chi(y)A(y\lambda_j^{2/3})h_je^{ij\phi}.
\tag{5.3}
$$
它在其它端的一个邻域中恒为零。根处由于 $E_{11}=E_{12}=0$、
$\chi'=0$，准确有
$$
A_A=cA(0)\Gamma^{-1/3},\qquad
C_A=-cA'(0)\Gamma^{1/3},\qquad\Gamma e_j=\lambda_je_j.
\tag{5.4}
$$
这里 $C_A$ 是已扣除实际 height shear 后的 canonical outward flux。
mean 使用 (5.3) 的真实列，未被删除。

对非零 $j$，自由部分准确消失。展开 $P_{\rm can}\mathcal Q$ 后，
每一项都是有限个 $c_*(y,\phi)y^k\lambda_j^\alpha
A^{(d)}(y\lambda_j^{2/3})e^{ij\phi}$。
下表列出全部项；表中的系数还包含 $c$、符号、$\chi$ 及其导数。
一次角微分带的 $j$ 写成 $\lambda_j/q$，故表中另外保留 $q$ 费用。

| residual 项 | $(k,\alpha,d)$ | 另乘 | 径向 $L^2$ 指数 $e$ |
| --- | --- | --- | --- |
| $V\chi D_A$ | $(0,-1/3,0)$ | $1$ | $-2/3$ |
| $-\chi''D_A$ | $(0,-1/3,0)$ | $1$ | $-2/3$ |
| $-2\chi' D_{A,y}$，写 $\chi'=y(\chi'/y)$ | $(1,1/3,1)$ | $1$ | $-2/3$ |
| $-E_{11}\chi D_{A,yy}$ | $(3,1,2)$ | $1$ | $-4/3$ |
| $-2E_{11}\chi'D_{A,y}$ | $(3,1/3,1)$ | $1$ | $-2$ |
| $-E_{11}\chi''D_A$ | $(3,-1/3,0)$ | $1$ | $-8/3$ |
| $-(\partial_yE_{11})\chi D_{A,y}$ | $(2,1/3,1)$ | $1$ | $-4/3$ |
| $-(\partial_yE_{11})\chi'D_A$ | $(2,-1/3,0)$ | $1$ | $-2$ |
| $-2E_{12}\chi\partial_\phi D_{A,y}$ | $(3,4/3,1)$ | $q^{-1}$ | $-1$ |
| $-2E_{12}\chi'\partial_\phi D_A$ | $(3,2/3,0)$ | $q^{-1}$ | $-5/3$ |
| $-(\partial_yE_{12})\chi\partial_\phi D_A$ | $(2,2/3,0)$ | $q^{-1}$ | $-1$ |
| $-(\partial_\phi E_{12})\chi D_{A,y}$ | $(3,1/3,1)$ | $1$ | $-2$ |
| $-(\partial_\phi E_{12})\chi'D_A$ | $(3,-1/3,0)$ | $1$ | $-8/3$ |
| $-E_{22}\chi\partial_\phi^2D_A$ | $(3,5/3,0)$ | $q^{-2}$ | $-2/3$ |
| $-(\partial_\phi E_{22})\chi\partial_\phi D_A$ | $(3,2/3,0)$ | $q^{-1}$ | $-5/3$ |

其中 $D_A=c\lambda_j^{-1/3}A(y\lambda_j^{2/3})$；若已将 $c$ 包入
$D_A$，表的系数不能再重复乘一次。所有行均有 $e\le-2/3$。
$\chi'/y$ 在根附近恒为零，在其支撑上 $y\ge h/2$，故是真正有界
且有已付有限角/径向导数的系数。这一步支付 cutoff，未假装它的导数为零。

mean 由于人为定义 $\lambda_0=1$ 而多出自由 residual
$-c y\chi(y)A(y)h_0$。它及表中 $j=0$ 的实际非零项具有有限
$L^2C^p$ norm，由 (2.4)–(2.5) 同样支付；有角微分的 $j=0$ 项则
准确为零。它是保留输出角频的实际有限输入列。

## 6. 原物理算子的完整 source 界

设实际正 height 与坐标关系为
$$
u_{\rm ph}(r,\theta)=t(r,\theta)
 U(y(r,\theta),\phi(r,\theta)),\qquad t>0,
$$
并已按密度/conormal 的真实公式定义 $P_{\rm can}$，使准确恒等式为
$$
P_{\rm ph}\bigl(t\,U\circ\Psi\bigr)
=\frac{J_\Psi}{t}(P_{\rm can}U)\circ\Psi.
\tag{6.1}
$$
$J_\Psi>0$ 是真实二维 Jacobian。不能只使用一个边界圆图的导数
代替它；也不能把缺少 source-contact 的表达式当成 (6.1)。

按 (3.1) 写 $y=r a$。对表中各行，把 $y^k$ 改成 $r^k a^k$，
并把 $J_\Psi/t$、$a^k$、实际系数、cutoff、所有常数及 $q$ 费用
合入 $c(r,\phi)$，其中 $\theta=K_r\phi$。由真实链式法则计算
(3.2) 的 $C_v$。这给同一个原物理 residual 的完整表示
$$
f_{\rm ph}=P_{\rm ph}(t\,\mathcal Q\circ\Psi)
=C_{H_r}\sum_{j\in\mathbb Z}b_j(r,\phi)h_je^{ij\phi},
\tag{6.2}
$$
其中 $b_j$ 是表中有限项之和，包含 mean 修正。

**定理 6.1。** 对任意已付实际有限窗口 $s$，取
$p>|s+2/3|+1$，并供应上面表中系数及坐标的相应有限 jets。
则
$$
\boxed{\quad
f_{\rm ph}:H^s\longrightarrow L^2_rH^{s+2/3}_\theta
\quad\text{有界}.\quad}
\tag{6.3}
$$
其明确常数可取
$$
F_s=C_{s+2/3}(H)L_{s,2/3,p}
 \left[\sum_{\text{表中实际项}}
 2^{1/3}\max(1,q^{e})\max(M_0^{\rm Ai},M_p^{\rm Ai})
 +M_{\rm mean}\right],
\tag{6.4}
$$
其中表内另列的 $q^{-1},q^{-2}$ 已合入各项 $C_v$，
$M_{\rm mean}$ 是仅均值自由修正列的真实 norm。各行已经使用
$\max(1,q^e)$，因此同时覆盖非零频率 (3.8) 和该行在 mean 上
仍有的 $\lambda_0=1$ 项；实际为零的角微分 mean 项无需另增费用。

**证明。** 每行由命题 3.1 有 (1.2) 且 $g=2/3$。
表中求和与实际 mean 列保留后，命题 1.1 给完整角输出。
最后 (4.4) 支付同一个实际 $H_r$；乘上真实 $J_\Psi/t$ 已在
(3.2) 中计入，故输出正是原物理源。$\square$

试解首先对有限 Fourier 输入定义，它是整个正组件上的真实能量函数。
这里还须保留 canonical 根迹到物理根迹的准确变换。记本端
$$
B_\partial=M_{t(0,\theta)}C_{H_0},\qquad
A_{\rm ph}=B_\partial A_A
\tag{6.5}
$$
（其余端 trace 为零）。则使用**原物理** Poisson/Dirichlet 算子时，
准确恒等式是
$$
\mathcal Q^{\rm ph}=\mathcal H_{\rm ph}A_{\rm ph}
                         +G_{\rm ph}f_{\rm ph}.
\tag{6.6}
$$
不能把 canonical 的 $A_A$ 原样当作物理边界值。(6.3)、R45 以及
真实 $B_\partial$ 的有限乘法/复合界给这个式子的有界延拓，故不需
假定任意混合坐标都对自然能量无损。

若把所有端口的 $B_\partial$ 组成块对角算子，真实 canonical DN
按 Green 配对为
$$
\Lambda_{\rm can}=B_\partial^*\Lambda_{\rm ph}B_\partial
                     -\Sigma_\partial,
\tag{6.7}
$$
其中 $\Sigma_\partial$ 是同一 height/坐标变换产生的实 normal shear。
对零边值 particular，shear 项为零，所以 source conormal 变为
$B_\partial^*\mathcal K_{\rm ph}f_{\rm ph}$。因此真正回接 R45 的式子是
$$
C_A-\Lambda_{\rm can}\iota_iA_A
=B_\partial^*\mathcal K_{\rm ph}f_{\rm ph}.
\tag{6.8}
$$
$B_\partial^*$ 的角密度和 height 范数也必须计入最终常数。
它们由本篇§4及同一实际边界乘法预算支付，未被写成一。

## 7. 如何以负侧有限 jets 给正侧三阶 flat principal

这里解释 (5.2) 的有限延拓口径，并列出真实预算，避免另解一个未付的
椭圆 Cauchy 问题。假设 R39 的负侧实际 canonical 坐标/height 在
根上已有所需有限混合 jets；实际原始系数在根两侧拥有相同的这些
jets。取 normalizing 坐标的四次径向 Taylor 多项式及 height 的
三次 Taylor 多项式，角系数保持原真实函数。

在根部，principal 密度只依赖原密度、坐标的一 jet 及 height 的值。
因此其径向0、1、2 jet 只用坐标至三 jet、height至二 jet及原系数
至二 jet，全部与负侧准确 canonical 化相同。正侧变成 $y=-\xi$
后，准确得到
$$
\partial_y^v E(0,\phi)=0,\qquad v=0,1,2.
\tag{7.1}
$$
径向 Taylor 延拓不改变原正侧算子：$E,V$ 始终从实际原系数用这组
真实坐标/height 重新计算，而不是另外选一个更方便的正侧 PDE。

对需要的各个角导数 $b\le p+\text{链式预算阶数}$，若实际 collar
上已有
$\sup|\partial_\phi^b\partial_y^3E|\le M_{3,b}$，则完整积分余项给
$$
e(y,\phi)=\frac12\int_0^1(1-t)^2
 \partial_y^3E(ty,\phi)dt,\qquad
\widetilde e(y,\phi)=\int_0^1(1-t)
 \partial_y^3E(ty,\phi)dt,
\tag{7.2}
$$
故 $|\partial_\phi^b e|\le M_{3,b}/6$、
$|\partial_\phi^b\widetilde e|\le M_{3,b}/2$。
这准确支付 (5.2)。$V$ 含坐标/height 的低阶项，须由同一变换公式
完整计算并界有限角导数，不可设为零。

实际图仍须通过 collar 门：$J_\Psi>0$、$t>0$、$a_->0$、
$\partial_\theta H_r>0$ 及相应逆的有限界。可由根部正下界与实际
有限径向导数上界选取 $h>0$，例如对每个正量 $v$ 使用
$h\sup|v_r|\le\inf v(0)/2$。涉及 $y/r$ 的量按其 Taylor 多项式
的真实商延拓到根。两端 collar 还须不相交。

这些是有限显式检查，不要求 $C-I$ 在整个正组件小，也不把当前
C4 径向样条自动变成具有所有这些高混合 jets 的对象。实际数据若
不足，先构造带有明确 $C^2$ 改变量的光滑候选再支付这些门。

## 8. 可完全明确选择的有限光滑 cutoff

给所需阶数 $p$，取整数 $N\ge p+3$。在 $h/2<y<h$，令
$z=2y/h-1$，设置
$$
\chi(y)=1-c_N\int_0^z t^N(1-t)^Ndt,\qquad
c_N=\frac{(2N+1)!}{(N!)^2},
\tag{8.1}
$$
并在两外区延拓为1和0。它是 $C^N$ 函数，所需 $p+2$ 阶导数
连续，且 $0\le\chi\le1$。对 $1\le r\le p+2$，可取明确上界
$$
\|\chi^{(r)}\|_\infty\le
c_N(2/h)^r
\sum_{k=\max(0,r-1-N)}^N
 \binom Nk\frac{(N+k)!}{(N+k-r+1)!}.
\tag{8.2}
$$
这是对有限多项式逐项取绝对值；不需要外部光滑函数的未知常数。
$\chi'/y$ 的导数由 Leibniz 公式及其支撑上 $y^{-1}\le2/h$ 同样
明确支付。若最终要任意多阶，可按实际需要重新选择更高 $N$；
每个有限强余项只用其中有限阶。

## 9. 与 R45 和完整相位的准确连接

定理 6.1 真正给 R45(6.3) 的物理源输入；(5.4) 给准确根迹，
不是仅给一个未标余项的 leading symbol。因而在 R45 的同一 full
Dirichlet/Robin realization 和端角/height/shear 全部已匹配时，
归一 DN 的各 root 输入列有 $4/3$ 强余项；all-root 组件的真实
Airy Cayley 为 $-I+R_{4/3}$，其他端口和 source 依旧完整保留。

这里只支付正侧的一项真实输入。负侧R43、strict负区R46、实际返回图
及完整反馈还需在同一frame接合，才能识别R34需要的常相位、$\beta$
和强余项常数；有限低块、无限平帽和非线性收敛也没有由此自动完成。
