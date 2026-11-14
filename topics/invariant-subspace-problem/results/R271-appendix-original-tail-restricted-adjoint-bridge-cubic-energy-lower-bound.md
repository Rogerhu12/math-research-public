# R271 附录：原完整尾受限伴随桥的三次能量下界与同源第一 jet

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本稿在原无限尾 $a_j=(j+1)^{-2}$ 上，保留完整 primitive 正交投影，构造单位 $f\in K_q$ 使真正的
$$
(D:\mathcal H_{q+2}\to\mathcal H_{q+1})^\dagger
(D_3|_{K_{q+1}})^*f
$$
具有 $q^3$ 量级的平方范数下界。测试读取的是实际受限伴随产生的 primitive 返回源，不是任意坏 primitive，也不是旧真幂底项。

随后把同一个 $f$ 放入一个明确的原可实现源 $r$，使实际第一 jet 恰为
$\zeta_1(r)=2A_m^4x\otimes C_0^*f$，并同时支付原左与完整右费用。还可使所有更高 jet 严格为零，而完整右费保持与 $q$ 无关的上界。
这仍未控制经过 $\mathcal G^\dagger$ 和第二桥 $\mathcal R$ 后的完整高源。
未验证这些源来自同一个固定 $w\in W$，也未支付其原 flat 费用。
因此本稿不是完整实际高返回、纯 $S_H^\dagger$ 或新 $H_2^\circ$ 的反例；无权 $N=M$ 和普通 Hilbert ISP 仍为 OPEN。

依赖：[原配对几何](R239-appendix-complete-first-triplet-resolution-and-minimal-energy.md)、[全部低三维块模式的联合分析](R271-appendix-low-triplet-count-joint-retraction-and-original-high-energy-bound.md)、[原精确真幂底项及两座 primitive 桥](R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)。
本稿不使用近似玻色运输；远尾在每一步都是原 $D_J$。

## 1. 原完整尾和主结论

记
$$
D=D_m=\sum_{j\ge m}(j+1)^{-2}E_j,\qquad
C=D_{3,m}=\sum_{j\ge m}(j+1)^{-6}E_j,
$$
$$
K_p=\ker D\cap\mathcal H_p,\qquad
C_0=C|_{K_{q+1}}:K_{q+1}\longrightarrow K_q.
$$
因为 $[D,C]=0$，这个限制合法；它在原 Hilbert 范数中的真正伴随是
$$
C_0^*=P_{K_{q+1}}C^*|_{K_q}.
\tag{1.1}
$$

取
$$
m\ge255,\qquad q\ge(m+2)^2,\qquad
N=q+1,\qquad J=m+2N.
$$
特别，原 $d=2^m,\ 4d\le q\le e^{d^3/4}$ 的合法窗口在这些头长上满足所需下界。

**定理 1.1。** 存在原单位向量 $f=f_{m,q}\in K_q$，使
$$
\boxed{
\left\|
(D:\mathcal H_{q+2}\to\mathcal H_{q+1})^\dagger C_0^*f
\right\|^2
\ge\frac{J^3}{192(m+2)^{13}}.}
\tag{1.2}
$$
所有原单步最小右逆在固定孔层存在；也可把 (1.2) 读成对每一个可行原像的下界。
本文下面显式定义 $f$，并证明它确由同一个原受限伴随产生。

## 2. 原共 primitive 测试和完整核投影

在前 $N$ 个相邻原对 $I_i=\{m+2i-2,m+2i-1\}$ 上，沿用
$$
a_i=(m+2i-1)^{-2},\quad b_i=(m+2i)^{-2},\quad
\sigma_i=\sqrt{a_i^2+b_i^2},
$$
$$
h_i=(b_i|10\rangle-a_i|01\rangle)/\sigma_i,\qquad
g_i=(a_i|10\rangle-b_i|01\rangle)/\sigma_i,
$$
$$
t_i=(b_i|10\rangle+a_i|01\rangle)/\sigma_i,\qquad
\rho_i=2a_ib_i/\sigma_i^2,\quad
\delta_i=(a_i^2-b_i^2)/\sigma_i^2.
$$
局部原删除严格满足 $D_ih_i=0,\ D_i^*g_i=0$。
令
$$
h=\bigotimes_{i=1}^Nh_i\otimes\Omega_J,\qquad
z=\bigotimes_{i=1}^Ng_i\otimes\Omega_J,\qquad
\rho=\prod_{i=1}^N\rho_i.
\tag{2.1}
$$
两者均为原单位 $N$ 孔向量，$h\in K_N$，且
$$
\langle h,z\rangle=\rho\ge e^{-2/(m+1)}.
\tag{2.2}
$$
真正完整尾的伴随作用在 $z$ 上时，整个前缀被准确杀掉：
$$
D^*z=\left(\bigotimes_i g_i\right)\otimes D_J^*\Omega_J,\qquad
\boxed{\|D^*z\|=\beta:=\sqrt{S_J},\quad
S_J=\sum_{j\ge J}(j+1)^{-4}\le\frac1{3J^3}.}
\tag{2.3}
$$

现在取完整原正交投影
$$
\boxed{k=P_{K_N}z.}
\tag{2.4}
$$
没有将 $P_{K_N}$ 换成前缀核投影或某个模型投影。
因为 $h\in K_N$，
$$
\|k-h\|\le\|z-h\|
=\sqrt{2(1-\rho)}\le\frac2{\sqrt{m+1}}=:\epsilon_m,
\quad
\|k\|\ge|\langle k,h\rangle|=\rho.
\tag{2.5}
$$

## 3. 只读取零、一、二个三维块的原坐标

令 $U_N$ 为前稿的完整前缀合成：局部外部正交基
$p_i,f_{i,0},f_{i,1},f_{i,2}$
分别送到原 $h_i,\Omega_i,t_i,|11\rangle_i$。
这里只把它在远尾张量恒等，记
$$
x=(U_N^{-1}\otimes I)k.
$$
该有限前缀同构始终存在；下面仅估计 $x$ 中三维 $Q$ 块数 $0,1,2$ 的分量。

完整低块数分析界给
$$
\left\|\Pi_{\le2}(U_N^{-1}\otimes I)\right\|
\le a_2:=\rho^{-1}\exp\!\sqrt{2\sum_i\delta_i^2}
\le\exp\!\left(\frac2{m+1}+\sqrt{\frac6{m+1}}\right)<2.
\tag{3.1}
$$
最后一式对 $m\ge255$ 成立；这个界不含 $N$。
记 $x_r$ 为恰有 $r$ 个 $Q$ 块的分量。
$h$ 的坐标只有 $r=0$ 项，因此 (2.5)、(3.1) 给
$$
\boxed{\|x_1\|,\ \|x_2\|\le a_2\epsilon_m<\frac14.}
\tag{3.2}
$$

因 $k$ 的总孔数是 $N$，零 $Q$ 分量只能是全部 $p_i$ 加远尾真空。
记其系数为 $x_0$。完整对偶身份
$$
U_N^*\left(\bigotimes_i g_i\right)
=\rho\bigotimes_i p_i
$$
以及 $k=P_{K_N}z$ 给
$$
\rho x_0=\langle k,z\rangle=\|k\|^2,
\qquad
\boxed{x_0=\|k\|^2/\rho\ge\rho.}
\tag{3.3}
$$
尤其这个系数为非负实数，不存在任意相位抵消。

每个一 $Q$ 分量只能有两种物理次数：
在该块取 $f_{i,1}$ 且远尾真空，系数记为 $\xi_i$；
或在该块取 $f_{i,0}$ 且远尾为一孔向量 $y_i$。
因此
$$
\sum_i\|y_i\|^2\le\|x_1\|^2<1/16.
\tag{3.4}
$$
原 $D$ 在外部坐标中保持每个 $P/Q$ 模式，并且
$D_i f_{i,1}=\rho_i\sigma_i f_{i,0}$。
完整 $Dk=0$ 在每个一 $Q$ 模式中于是准确给
$$
\boxed{\rho_i\sigma_i\,\xi_i+D_Jy_i=0.}
\tag{3.5}
$$
这里 $D_J$ 作用在真正的一孔远尾，未换成标量近似。

## 4. 原三次删除只改变三维块数至多一

置
$$
c_i=\frac{\sigma_i^3\delta_i}{2}
=\frac{\sigma_i(a_i^2-b_i^2)}2,\qquad
c_*=\left(\sum_{i=1}^Nc_i^2\right)^{1/2}.
\tag{4.1}
$$
逐个原物理基计算，局部 $C_i=a_i^3E_{m+2i-2}+b_i^3E_{m+2i-1}$ 在外部坐标中严格为
$$
\boxed{
U_i^{-1}C_iU_i
=\frac{\sigma_i^2}{2}(0\oplus\mathsf D_i)
+c_i\bigl(\rho_i|f_{i,0}\rangle\langle p_i|
-|p_i\rangle\langle f_{i,2}|\bigr).}
\tag{4.2}
$$
具体地，$C_ip_i=\rho_i c_if_{i,0}$，
$C_if_{i,1}=(\rho_i\sigma_i^3/2)f_{i,0}$，
$C_if_{i,2}=(\sigma_i^3/2)f_{i,1}-c_ip_i$。
这保留原两条不等的三维删除权，也保留非原始模式之间的耦合。

读取 $(U_N^{-1}\otimes I)Ck$ 中
“恰一个 $Q$ 块，且该块是真空 $f_{i,0}$，远尾亦真空”的整个外部正交行，
所得系数向量记为 $Y\in\mathbb C^N$。
由 (4.2)，只有 $x_0,x_1,x_2$ 能贡献到这个行，任何更高 $Q$ 分量都不能贡献。
利用 (3.5) 消掉 $\xi_i$，准确得到
$$
\boxed{
Y=x_0(\rho_i c_i)_{i=1}^N
+\left[(C_J-\tfrac12\sigma_i^2D_J)y_i\right]_{i=1}^N
+\mathcal L_c x_2.}
\tag{4.3}
$$
最后一个算子只把某个 $f_{j,2}$ 降为 $p_j$，并取上述目标行。
由向量值 Cauchy--Schwarz 和二 $Q$ 输入，
$$
\boxed{\|\mathcal L_cx_2\|\le\sqrt2\,c_*\|x_2\|.}
\tag{4.4}
$$
这是一整个正交行的界，不是逐 $i,j$ 估计后丢掉交叉项。

特别，(4.3) 是外部坐标行，不能假装它等于原物理空间到
$\bigotimes_{j\ne i}h_j\otimes\Omega_i$ 的正交投影。
那些原物理测试会额外读取更高 $Q$ 模式。
下面通过已经支付的完整分析范数把 $Y$ 转回原范数，避免这项混同。

## 5. 全部误差与原返回源的非零下界

先给 $c_*$ 的原权下界。
令 $x=m+2i-1$，则
$$
a_i^2-b_i^2=x^{-4}-(x+1)^{-4}
\ge4(x+1)^{-5},\qquad
\sigma_i\ge(x+1)^{-2}.
$$
故 $c_i\ge2(m+2i)^{-7}$。
因 $N\ge m$，积分比较给
$$
\begin{aligned}
c_*^2
&\ge4\sum_{i=1}^N(m+2i)^{-14}\\
&\ge\frac2{13}\left[(m+2)^{-13}-(m+2N+2)^{-13}\right]\\
&\ge\frac2{13}(1-2^{-13})(m+2)^{-13}
>\frac1{9}(m+2)^{-13}.
\end{aligned}
$$
因此
$$
\boxed{c_*>\frac1{3(m+2)^{13/2}}.}
\tag{5.1}
$$

在真正一孔远尾上，
$$
\|D_J\|_{\mathcal H_1\to\mathbb C}=\beta\le(3J^3)^{-1/2},
\quad
\|C_J\|_{\mathcal H_1\to\mathbb C}
=\left(\sum_{j\ge J}(j+1)^{-12}\right)^{1/2}
\le(11J^{11})^{-1/2}.
$$
且 $\sigma_i^2/2\le(m+1)^{-4}$。
所以 (4.3) 的中间算子范数至多
$$
b_*=\frac{\beta}{(m+1)^4}+\frac1{\sqrt{11}J^{11/2}}.
\tag{5.2}
$$
本稿 $q\ge(m+2)^2$ 保证 $J\ge(m+2)^2$。
结合 (5.1)，第一项除以 $c_*$ 至多
$$
\sqrt3\frac{(m+2)^{7/2}}{(m+1)^4}
\le\frac{2\sqrt3}{\sqrt{m+1}}<\frac14
\quad(m\ge255),
$$
这里使用 $((m+2)/(m+1))^{7/2}<2$。
第二项除以 $c_*$ 至多
$(3/\sqrt{11})(m+2)^{-9/2}<1/4$。
于是
$$
\boxed{b_*<c_*/2.}
\tag{5.3}
$$

又 $\rho\ge7/8$，并且每个 $\rho_i\ge\rho\ge7/8$。
由 (3.2)–(3.4)、(4.3)–(4.4) 得
$$
\begin{aligned}
\|Y\|
&\ge \rho\min_i\rho_i\,c_*
-b_*\left(\sum_i\|y_i\|^2\right)^{1/2}
-\sqrt2c_*\|x_2\|\\
&>\left(\frac{49}{64}-\frac18-\frac38\right)c_*
=\frac{17}{64}c_*>\frac14c_*.
\end{aligned}
\tag{5.4}
$$
全部向量都属于原完整尾；完整核投影造成的误差正是由 (3.2) 处理。

读出 $Y$ 的行是前缀“至多一个 $Q$”完整分析的一个正交压缩。
其范数不超过 $a_1\le a_2<2$，故
$$
\boxed{\|Ck\|\ge\|Y\|/a_1>c_*/8
>\frac1{24(m+2)^{13/2}}.}
\tag{5.5}
$$
因为 $k\in K_N$ 且 $[D,C]=0$，有 $Ck\in K_{N-1}=K_q$。
现在明确取
$$
\boxed{f=Ck/\|Ck\|\in K_q,\qquad \|f\|=1.}
\tag{5.6}
$$
这一定义使用真正 $k=P_{K_N}z$，从未绕过该投影。

令 $\eta=C_0^*f=P_{K_N}C^*f$。同一个原投影给
$$
|\langle\eta,z\rangle|
=|\langle C^*f,k\rangle|
=\|Ck\|>c_*/8.
\tag{5.7}
$$
对任意原 $u\in\mathcal H_{q+2}$ 满足 $Du=\eta$，由 (2.3)，
$$
\beta\|u\|\ge|\langle u,D^*z\rangle|
=|\langle\eta,z\rangle|>c_*/8.
$$
用 (5.1) 及 $\beta^2\le1/(3J^3)$，得到
$$
\|u\|^2>\frac1{576\beta^2(m+2)^{13}}
\ge\frac{J^3}{192(m+2)^{13}}.
$$
特别原真正最小原像满足 (1.2)。证毕。

这是原 $C_0^*$ 的真实范围中的下界。
例如试图用只依赖 $S_m=\sum_{j\ge m}(j+1)^{-4}$ 的常数统一控制
$\|D^\dagger C_0^*f\|$，会与合法大 $q$ 的 (1.2) 冲突。
但本结论还不能替换完整 $\mathcal G^\dagger\zeta$ 后的高返回。

## 6. 同一个原源可以只有第一 jet，并有便宜的完整右修复

保留原真实 $A=A_m$，不将它换成一个人为小头。
定义原严格正可逆算子
$$
M_2=D^2(D^*)^2:\mathcal H_q\longrightarrow\mathcal H_q,
\qquad g=M_2f.
\tag{6.1}
$$
其逆存在性由原完整 $D^2$ 满射给出；这里不是顺次 MP 逆的平方。

原交换子
$$
[D,D^*]=S_mI-2W,\quad [D,W]=C,\quad [D,C]=0
$$
给 $\operatorname{ad}_D^3(D^*)=0$。
Leibniz 公式因而给
$\operatorname{ad}_D^5((D^*)^2)=0$。
因为 $Df=0$，准确得到
$$
\boxed{D^3g=D^5(D^*)^2f=0.}
\tag{6.2}
$$

### 6.1 原左可实现性与全部左费用

对任意原头向量 $x$，令左候选仅有以下三个尾孔层：
$$
v_q=A^2x\otimes g,\qquad
v_{q-1}=-Ax\otimes Dg,\qquad
v_{q-2}=x\otimes D^2g,
\tag{6.3}
$$
其余层为零。(6.2) 和头尾交换直接给
$$
P_{<q}(A+D)v=0,\qquad
\boxed{r=(A+D)v=A^3x\otimes g\in\mathscr R_q.}
\tag{6.4}
$$
所有首末端方程均已列入，亦保原 $D^d$ 联合旗。

完整费用显式支付。由 $\|D_m\|\le1/m,\ \|A_m\|\le6$ 及三个孔层正交，
$$
\begin{aligned}
\mu(r)^2\le\|v\|^2
&=\|A^2x\|^2\|g\|^2
+\|Ax\|^2\|Dg\|^2+\|x\|^2\|D^2g\|^2\\
&\le\left(6^4m^{-8}+6^2m^{-10}+m^{-12}\right)\|x\|^2\\
&<37^2m^{-8}\|x\|^2.
\end{aligned}
\tag{6.5}
$$
同时 $\|r\|\le216m^{-4}\|x\|$。
这是上界，不将 (6.3) 免费认作左最小者。

### 6.2 准确消掉全部更高 jet

现在进一步取
$$
\boxed{x\in\ker A^5,\qquad A^4x\ne0.}
\tag{6.6}
$$
原循环头中有这样的向量；也可固定一个较小原头中的该向量，再按原嵌套包含送入更大头。

原完整第一桥公式为
$$
\eta_t(r)=P_{K_q}[D^{t+1}(D^*)^{t+1}]^{-1}r,\qquad
\zeta_t(r)=t(t+1)H_{t-1}^{-1/2}A^t C_0^*\eta_t(r).
\tag{6.7}
$$
所有尾算子都与 $A$ 交换。由 (6.1)、(6.4) 及 $H_0=I$，
$$
\boxed{
\eta_1(r)=A^3x\otimes f,\qquad
\zeta_1(r)=2A^4x\otimes C_0^*f,\qquad
\zeta_t(r)=0\ (t\ge2).}
\tag{6.8}
$$
最后一式不是忽略其余项：每个 $\eta_t$ 的头因子仍为 $A^3x$，
所以 $A^t\eta_t$ 的头因子为 $A^{t+3}x=0$。

同一个源的第一伴随 primitive 返回因而满足
$$
\boxed{
\|D^\dagger\zeta_1(r)\|^2
\ge\frac{\|A^4x\|^2J^3}{48(m+2)^{13}}.}
\tag{6.9}
$$

### 6.3 同源完整右链只有两层，全部费用独立于 q

令
$$
c_1=A^3x\otimes D(D^*)^2f,\qquad
c_2=-A^4x\otimes(D^*)^2f,\qquad c_j=0\ (j\ge3).
\tag{6.10}
$$
它们分别在原尾层 $q+1,q+2$。直接核对
$$
Dc_1=r,\qquad Dc_2=-Ac_1,\qquad Ac_2=0.
\tag{6.11}
$$
最后一式使用 (6.6)。
又 $D^5(D^*)^2f=0$，所以 $D^dc_1=D^dc_2=0$；
这里 $d=2^m\ge5$。原头旗也由 $A^3x,A^4x$ 的真实头像保持。
因此 (6.10) 是原宽 $d$ 内的完整合法右修复，并有
$$
\boxed{
\alpha(r)^2\le\lambda(r)^2
\le\|A^3x\|^2m^{-6}+\|A^4x\|^2m^{-4}.}
\tag{6.12}
$$
这与 (6.9) 是同一个 $f$、同一个 $x$、同一个 $r$，没有换来源来拼两种估计。

同样，完整桥算子
$$
(\mathcal G\xi)_t
=A\xi_{t-1}-H_{t-1}^{1/2}H_t^{-1/2}\xi_t
$$
有同源候选
$$
\xi_0=2A^3x\otimes C_0^*f,\qquad \xi_j=0\ (j\ge1).
$$
由 (6.8)，它准确满足 $\mathcal G\xi=\zeta(r)$。
因此
$$
\boxed{\|\mathcal G^\dagger\zeta(r)\|
\le2\|A^3x\|\|C_0^*f\|
\le\frac{2\|A^3x\|}{5m^5},}
\tag{6.13}
$$
其中 $\|C_0^*\|\le\|C\|\le1/(5m^5)$。
这明确说明原完整桥可从头端处理第一 jet，根本不需要先支付
$D^\dagger C_0^*f$ 这个大范数。

### 6.4 同源分离的准确范围

若固定一个原小头 $p$ 中满足
$A_p^5x=0,\ A_p^4x\ne0$ 的 $x$，原准确递归
$$
A_{p+1}=
\begin{pmatrix}A_p&b_pI+K_p\\0&A_p\end{pmatrix}
$$
保证在所有较大头上 $A_m^jx=A_p^jx$。
这保留真实 carry，不引入替代头矩阵。

对这样的固定 $x$，(6.5)、(6.9)、(6.12) 给同源量的明确比较
$$
\boxed{
\frac{\|D^\dagger\zeta_1(r)\|^2}{\lambda(r)^2+\mu(r)^2}
\ge
\frac{\|A_p^4x\|^2J^3}
{48(m+2)^{13}
\left(\|A_p^3x\|^2m^{-6}
+\|A_p^4x\|^2m^{-4}
+37^2m^{-8}\|x\|^2\right)}.}
\tag{6.14}
$$
沿原合法 $q\ge4d=4\cdot2^m$，右侧趋于无穷。
所以第一受限伴随后的逐步尾逆，确实可以在同一个原可实现源上，
远大于已经付清的完整左右最小费用。

(6.14) 也说明为何不能把 (1.2) 当作完整高返回的反例：
这里所有更高 jet 已严格为零，完整 $\mathcal G^\dagger\zeta$ 已有 (6.13) 的小上界，
完整右费用也有 (6.12) 的小上界。
原新高能量更满足
$$
0\le\lambda(r)^2-\alpha(r)^2
\le\|A_p^3x\|^2m^{-6}+\|A_p^4x\|^2m^{-4}.
$$
剩下仍未估计的是
$\mathcal R\mathcal G^\dagger\zeta(r)$ 在纯 $S_H^\dagger$ 度量中的费用。
本稿也没有付原混合 flat 费用，或证明这些 $r$ 来自同一个固定非零 $w\in W$ 的实际窄来源。
