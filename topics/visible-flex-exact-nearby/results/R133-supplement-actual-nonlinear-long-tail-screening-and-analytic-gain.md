# R133：实际长段的非线性远端筛选、完整 mean 与真正角解析增宽

**已证明。** 本篇消费[真实正帽—周期长段接合](R133-supplement-actual-positive-cap-and-periodic-long-tail-matching.md)
和[真正周期正帽的开放内侧图](R133-supplement-actual-periodic-cap-open-inner-graph.md)。
它处理同一原有限主体、graft 和 R74 长径向段，不替换为新 deep profile。
结论适用于全部 Fourier 模和完整参数区间，并保留 holonomy mean 小根。

固定远端 Dirichlet 数据 $f_B$ 时，改变内端 $f_*$ 对真实远端归一化斜率的影响满足

$$
\|\Delta K_{B,\perp}\|_{\dot A^1_\sigma}+|\Delta K_{B,0}|
 <25e^{-7L/4}\|f_*\|_{\dot A^2_\sigma}.
\tag{S.1}
$$

此外，真正的 **$f_B=0$ incoming 分量** 在远端获得物理角宽 $7L/16$：

$$
\|K_{B,\perp}(0,f_*)\|_{\dot A^1_{\sigma+7L/16}}
 <18\|f_*\|_{\dot A^2_\sigma},\qquad
\|D_{f_*}K_{B,\perp}(0,f_*)\|<24.
\tag{S.2}
$$

这是整个真实非线性 Dirichlet 解的估计；没有截断角频率，也没有将径向小量
冒充角解析增宽。非零 $f_B$ 的混合项在原物理角宽中另付。远端 label 逆、内侧
mixed body、两端 mean 匹配和最终闭面几何尚须继续完成。

## 1. 同一对象、完整空间与原非线性

采用 [R119 长径向 Dirichlet 定理](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md)
的准确坐标

$$
t=\omega(B-u)\in[0,L],\quad L=\omega B,\quad
a=a_Be^t,\quad w=a/(4\omega),\quad E=1+w^2.
\tag{S.3}
$$

$t=0$ 是与待解 tail labels 接合的远端，$t=L$ 是原 $r=25/8$ 的正帽端。
给定非mean物理角数据 $h(0)=f_B$、$h(L)=f_*$。记

$$
\|f\|_{\dot A^j_\sigma}
 =\sum_{m\in4\mathbb Z\setminus\{0\}}e^{\sigma|m|}|m|^j|f_m|.
$$

$\sigma$ 是此前真正接合定理使用的实际物理角宽，可随原参数变化；下文常数
在其整个已证范围统一。所有输入和导数列先在这个实际角宽中消费，只有显式说明
降低角宽时才使用统一下界。实际完整数据给

$$
L>24514072.626868956,\quad \sigma>.0690152937098778,
$$
$$
\|f_*\|_{\dot A^2_\sigma}\le r_f=10^{-8},\qquad
\|f_B\|_{\dot A^2_\sigma}\le 2^{-60}.
\tag{S.4}
$$

共同实、偶反射的四重数据给实际周期曲面；证明在其复化中成立，也适用于未加
偶约束的全部四重 Fourier 代数。共同角平移保留结论。

强空间 $\mathcal Y_\sigma$ 与源空间 $\mathcal F_\sigma$ 使用 R119 (D.4) 的
“每模先径向 supremum，再求和”。在 $\|h\|_{\mathcal Y}\le1/1024$ 内，完整
holonomy 小根 $\mu(h)$ 和实际非线性为

$$
P=h_\theta,\quad U=h_{\theta\theta},\quad
K=\mu(h)+2h+h_t,\quad V=2h_\theta+h_{t\theta},
$$
$$
\mathcal Q(h)=\Pi_\perp
 \frac{E(V-P)^2+K^2+2EKU+EU^2-w^2P^2}{1+K+EU},
\tag{S.5}
$$

$$
[(\partial_t+2)^2+\partial_\theta^2]h=\mathcal Q(h),
\qquad \|\mathcal Q(h)\|_{\mathcal F}\le512\|h\|_{\mathcal Y}^2,
\qquad \|\mu(h)\|_{C^0_t}\le256\|h\|_{\mathcal Y}^2.
\tag{S.6}
$$

这些估计来自 R119 的乘法、mean 读取、逆级数及 mean 小根的绝对 majorant，
并非只对逐点标量范数成立。原定理在

$$
r_*=2^{-20},\qquad
\|f_B\|_{\dot A^2_\sigma}+\|f_*\|_{\dot A^2_\sigma}\le2^{-25}
\tag{S.7}
$$

给唯一真实解 $\|h\|_{\mathcal Y}\le r_*$。其 mean 与水平 coframe 都已重建。
本篇在同一解上证明新估计。

## 2. 两种权的完整有限长 Green

令 $M=|m|\ge4$。原准确零 Dirichlet 核为

$$
G_M(t,s)=-e^{2(s-t)}
\frac{\sinh(M\min(t,s))\sinh(M(L-\max(t,s)))}{M\sinh(ML)},
$$

并有

$$
|G_M(t,s)|\le M^{-1}e^{-M|t-s|+2(s-t)},\qquad
|\partial_tG_M(t,s)|\le3e^{-M|t-s|+2(s-t)}.
\tag{S.8}
$$

考虑两种权：

$$
W_\nu(t)=e^{\nu(L-t)},\quad \nu=7/4;
\qquad
W_{\alpha,m}(t)=e^{\alpha M(L-t)},\quad \alpha=7/16.
\tag{S.9}
$$

加权 $\mathcal Y$ 在 $h,h_t,h_{tt}$ 的每一项上乘相同的权；**导数作用于真实
$h$，而不是作用于乘权后的 $h$**。源空间使用同一权。

对第一种权，$W_\nu(t)/W_\nu(s)=e^{\nu(s-t)}$，两半核的无量纲积分满足

$$
I_\nu(M)=\frac{M}{M-2-\nu}+\frac{M}{M+2+\nu}
 \le\frac{512}{31}.
\tag{S.10}
$$

对第二种权，相同计算给

$$
I_\alpha(M)=\frac{M}{(1-\alpha)M-2}
 +\frac{M}{(1+\alpha)M+2}
 =\frac{2}{1-(\alpha+2/M)^2}\le\frac{512}{31}.
\tag{S.11}
$$

分母严格正，最坏模式是完整空间中的 $M=4$。记 $I=512/31$。逐模积分后，
$M^2\|H\|_W\le I\|F\|_W$、$M\|H_t\|_W\le3I\|F\|_W$。准确方程
$H_{tt}=F-4H_t+(M^2-4)H$ 再给
$\|H_{tt}\|_W\le(1+4I)\|F\|_W$。所以两种权都满足完整强 Green 界

$$
\|\mathcal G_D\|_{\mathcal F_W\to\mathcal Y_W}
 \le1+8I<160.
\tag{S.12}
$$

这里先估计每个真实有限长核，再求全部频率之和，故没有交换径向 supremum
与 Fourier 求和。

内端齐次 lift 是

$$
B_M(t)=e^{2(L-t)}\frac{\sinh(Mt)}{\sinh(ML)}
=\frac{e^{-(M-2)x}-e^{-2ML+(M+2)x}}{1-e^{-2ML}},\quad x=L-t.
\tag{S.13}
$$

乘 $e^{cx}$，其中 $c=\nu$ 或 $c=\alpha M$，均有 $c<M-2$。第一指数项
不超过1，第二指数项不超过第一项。又 $1-e^{-2ML}>255/256$。对真实 $t$
导数逐项估计，三项 $M^2B_M,MB_M',B_M''$ 可分别取 $2,6,8$ 倍 $M^2$
的界。因此

$$
\|\mathcal L_*f_*\|_{\mathcal Y_W}
 \le16\|f_*\|_{\dot A^2_\sigma}.
\tag{S.14}
$$

所有反射项仍在准确式 (S.8)、(S.13) 中；没有先令 $L=\infty$。

## 3. 径向权的完整非线性导数，包括 mean

这里不能从普通未加权 Cauchy 导数界直接声称加权导数界。为支付这个步骤，
取原完整 Fourier/$C^0_t$ Banach 代数 $\mathcal A$，以及同宽、带径向权
$W_\nu$ 的双边 Banach module $\mathcal M_\nu$。它们满足

$$
\|au\|_{\mathcal M_\nu}\le\|a\|_{\mathcal A}\|u\|_{\mathcal M_\nu}.
$$

在平方为零的扩张代数中定义

$$
(a,u)(b,v)=(ab,av+bu),\quad
\|(a,u)\|=\|a\|_{\mathcal A}+\|u\|_{\mathcal M_\nu}.
\tag{S.15}
$$

这是单位范数为1的交换 Banach 代数。乘法、逆级数、mean 读取及非mean角原函数
具有原来的界；$W_\nu$ 与角算子可交换。径向系数 $w,E$ 处于第一分量。
原 mean 小根的同一绝对收缩 majorant 因此在 (S.15) 中成立。其第二分量准确是
$D\mu(h)v$，而 (S.5) 的第二分量准确是 $D\mathcal Q(h)v$。

若 $\|h\|_{\mathcal Y}\le r$、$\|v\|_{\mathcal Y_\nu}\le1$，把 $(h,rv)$
代入 (S.6)；其完整 norm 不超过 $2r$。在 $2r\le1/1024$ 时得到

$$
\|D\mathcal Q(h)v\|_{\mathcal F_\nu}\le2048r,
\qquad
\|D\mu(h)v\|_{C^0_\nu}\le1024r.
\tag{S.16}
$$

这同时保留了所有 mean 耦合和全部 Fourier 模，且不要求背景 $h$ 本身在径向
加权空间中很小。

令 $h_1=h(f_B,f_*)$、$h_0=h(f_B,0)$，$\delta h=h_1-h_0$。二者以及连接
它们的线段都在原 $r_*$ 球中。由于 $L$ 是有限真实数，径向权有有限上界，
原解本来就在这个加权空间中；这里没有先假设所求的小加权界。准确差方程、
(S.12)、(S.14)、(S.16) 给

$$
\|\delta h\|_{\mathcal Y_\nu}
 \le16\|f_*\|_{\dot A^2_\sigma}
 +160\cdot2048r_*\|\delta h\|_{\mathcal Y_\nu}.
$$

因 $160\cdot2048r_*=5/16$，

$$
\|\delta h\|_{\mathcal Y_\nu}
 \le\frac{256}{11}\|f_*\|_{\dot A^2_\sigma}<24\|f_*\|_{\dot A^2_\sigma},
$$
$$
\|\mu(h_1)-\mu(h_0)\|_{C^0_\nu}
 \le\frac1{44}\|f_*\|_{\dot A^2_\sigma}.
\tag{S.17}
$$

$1/44$ 是准确有理恒等式
$1024r_*\cdot256/11=1/44$，不是一个浮点近似。

## 4. 真正远端负荷、mean 斜率和 mean 高度

真实归一化斜率是

$$
K_{B,\perp}(f_B,f_*)=2f_B+h_t(0),\qquad
K_{B,0}(f_B,f_*)=\mu_0(h).
\tag{S.18}
$$

在固定 $f_B$ 的差中，$\delta h(0)=0$，故 (S.17) 立即给 (S.1)，并给单独的
mean 界

$$
|\Delta K_{B,0}|\le\frac1{44}e^{-7L/4}\|f_*\|_{\dot A^2_\sigma}.
\tag{S.19}
$$

实际物理高度导数须再乘 $w_B$：$\Delta(v_a)_B=w_B\Delta K_B$。
原 $u,r$ 方向及北帽实际高度 $Z_0-v$ 的符号仍由原接口准确转换；没有把
$K_B$ 改名为 grounded flux。

mean 高度也没有随斜率估计消失。两个真实解的 mean 高度跨度差准确是

$$
\Delta[v_0(L)-v_0(0)]
 =\int_0^L a(t)w(t)[\mu_t(h_1)-\mu_t(h_0)]\,dt.
\tag{S.20}
$$

由于 $aw(t)=aw(L)e^{-2(L-t)}$，(S.17) 给

$$
|\Delta[v_0(L)-v_0(0)]|
 \le\frac{aw(L)}{165}(1-e^{-15L/4})\|f_*\|_{\dot A^2_\sigma}.
\tag{S.21}
$$

这个跨度不被错误地赋予远端的 $e^{-7L/4}$ 因子。一个整体平均高度平移仍是
独立自由量；不能另把两个端点 mean 高度同时任意指定。

对原远端真实方程

$$
\mathfrak F(a,f_*)=k_B(a)+C_Lf_B(a)-S_Lf_*-E_D(f_B(a),f_*),
$$

在相同 labels $a$ 下准确有

$$
\mathfrak F(a,f_*)-\mathfrak F(a,0)
 =-\Delta K_{B,\perp}(f_B(a),f_*).
\tag{S.22}
$$

这里 $a$ 是 tail labels，不是物理半径。$\mathfrak F(a,0)$ 没有被置零，
完整 mean 斜率和高度跨度也要随 (S.19)–(S.21) 一起保留。

## 5. $f_B=0$ 时构造真正变角宽解

现在使用 (S.9) 的第二种权。它对应实际角宽

$$
\sigma(t)=\sigma+\alpha(L-t),\qquad \alpha=7/16.
\tag{S.23}
$$

完整 Fourier 代数的权满足

$$
e^{\alpha|m+n|(L-t)}
 \le e^{\alpha|m|(L-t)}e^{\alpha|n|(L-t)}.
\tag{S.24}
$$

mean 的权为1，单位 norm 也是1。先对每个卷积项取径向 supremum，再求全部
频率之和，得到乘法常数1。因此 (S.6) 的完整 majorant、mean 小根与全纯
导数界在这个变角宽代数中保持同样常数。

不能先假定原解具有变角宽：直接在完整 $\mathcal Y_\alpha$ 球
$\|h\|\le r_*$ 中构造。取 $f_B=0$，使用实际内端数据 $f_*$。
(S.12)、(S.14) 给球像

$$
16r_f+160\cdot512r_*^2
 <2.345059\cdot10^{-7}<r_*;
$$

完整收缩率至多 $160\cdot2048r_*=5/16$。故存在唯一加权解。由于所有权
不小于1，它也在原未加权 $r_*$ 球中，由原真实 Dirichlet 唯一性，它准确等于
已经构造并重建的真实曲面解。

对这个解令 $H_\alpha=\|h\|_{\mathcal Y_\alpha}$。用其已证球半径一次得

$$
H_\alpha\le16\|f_*\|+160\cdot512r_*H_\alpha,
\qquad H_\alpha\le\frac{1024}{59}\|f_*\|<18\|f_*\|.
\tag{S.25}
$$

同一完整导数方程给 $\|D_{f_*}h\|\le256/11<24$。在 $t=0$ 有 $h(0)=0$，
所以真实非mean斜率就是 $h_t(0)$；这证明 (S.2)。实际增宽满足

$$
\frac{7L}{16}>10724906.774255168,
\qquad \sigma+\frac{7L}{16}>10724906.843270461.
\tag{S.26}
$$

mean 斜率另使用 (S.19)，不能借角指数权删除。

若未来两端数据本身满足 $f_B\in\dot A^2_{\sigma+\alpha L}$，同一证明还可
在总加权边界预算上使用。外端准确 lift $A_M(t)$ 乘的相对权为
$W_{\alpha,m}(t)/W_{\alpha,m}(0)=e^{-\alpha Mt}$，其完整 $16$ 预算仍成立。
本篇实际允许的任意 $f_B\in\dot A^2_\sigma$ 并未被自动授予这个更强假设。

## 6. 非零远端背景的混合项和联立反馈

准确分解为

$$
\Delta K_B(f_B,f_*)
 =K_B(0,f_*)-K_B(0,0)+\mathcal M_B(f_B,f_*).
\tag{S.27}
$$

第一项有 (S.2) 的真正大角宽。第二项的完整非mean/mean norm 在原角宽中估计。
取 $\delta_B=2^{-27}$。因为

$$
\delta_B+2^{-60}+10^{-8}<2^{-25},
\tag{S.28}
$$

只针对原长段解，在每个 $\|f_B\|\le2^{-60}$ 周围都有半径 $\delta_B$ 的
全纯圆盘；这里无需把整个正帽联合解扩张到该大圆盘。对 (S.1) 应用 Cauchy，
再沿从0到 $f_B$ 的线段积分，得到

$$
\|\mathcal M_{B,\perp}\|_{\dot A^1_\sigma}+|\mathcal M_{B,0}|
 \le25e^{-7L/4}r_f\,\frac{\|f_B\|_{\dot A^2_\sigma}}{\delta_B}.
\tag{S.29}
$$

真正整帽已给 $f_*=\Phi(c_{\ne0}(1),f_B)$ 及完整导数列

$$
\|D_{f_B}\Phi\|<3.254260,\qquad
\|D_{c(1)}\Phi\|<.000844633495.
\tag{S.30}
$$

因此对复合的实际远端**增量** $\Delta K_B(f_B,\Phi)$，固定背景的 Cauchy 列
与 (S.17) 的内端导数列一起给

$$
\|D_{f_B}\Delta K_B\|
 \le25e^{-7L/4}\left(r_f/\delta_B+\|D_{f_B}\Phi\|\right)
 <128e^{-7L/4},
$$
$$
\|D_{c(1)}\Delta K_B\|<\frac1{32}e^{-7L/4}.
\tag{S.31}
$$

输出 norm 仍是非mean $\dot A^1_\sigma$ 加独立 mean 绝对值。这是新增 incoming
负荷的反馈列，不是整个 $\mathfrak F(a,0)$ 或 labels 逆的界。

## 7. 有限角导与 tail 标签权的区别

为明确 ordinary 强角导的实际大小，可降到固定物理角宽 $\sigma_0=1/512$。
令 $d=\sigma-\sigma_0>0$。对 $N\ge2$，$M\ge4$ 有

$$
\frac{(1+M)^N}{M}e^{-dM}
 \le(5/4)^N\left(\frac{N-1}{2d}\right)^{N-1}=:C_N.
\tag{S.32}
$$

这里使用 $e>2$ 的严格上界；它覆盖全部非零模式。于是完整非齐次角 norm
（mean 单独加回）满足

$$
\|\Delta K_B\|_{A^N_{1/512}}
 <25C_Ne^{-7L/4}r_f.
\tag{S.33}
$$

原生计算对 $N=224,404$ 保存 $\log C_N$ 和最后的严格正数界，未用 double
下溢的0代替真实量。但这些只是 ordinary 角导范数，并没有因此识别新 tail
的第224标签空间、raw404所需的径向或指数权。真正可供这些空间继续消费的
新事实是 (S.2)、(S.23) 的实际物理角解析增宽；非零 $f_B$ 混合项仍须联立。

## 8. 实际有向算术和保留范围

完整小 consumer 是 `scripts/fourfold_actual_long_tail_nonlinear_screening_v2.py`，
实际输出为 `notes/2026-11-13-R133-actual-nonlinear-long-tail-screening-v2-native.json.gz`。
它检查此前真正整帽和长段报告的完整性、同一目标/参数身份、完整 source SHA，
以384-bit Arb 消费所有方向端点。全部16个门实际通过，包括两个加权收缩、
真正 incoming 增宽、完整 mean、两个复合导数列和严格非零的指数筛选。

实际 $e^{-7L/4}$ 的正上界为

$$
e^{-7L/4}<4.743039073714\cdot10^{-18631072}.
\tag{S.34}
$$

因 native 保存 Arb 字符串，即使附属 `mid_float` 下溢为0也不影响这个量被完整
保留。首版源及 `...actual-nonlinear-long-tail-screening-native.json.gz` 保留：该次
唯一未通过的门是用 outward interval 的 `<=` 判断准确的 $1/44$ 等式。
v2 将该门改为 Python `Fraction` 的准确有理恒等式，并记录 (S.21) 的 mean 高度界；
原报告仍为 false，原先所有数值量继续保留。

本篇没有把远端 $f_B$ 置零来替代完整 tail 方程，而是分解并支付真正 incoming
与混合项。最终仍须在同一目标上解 $\mathfrak F(a,f_*)=0$，保留 mean 高度和
斜率，联立实际主体的另一迹，并证明整个闭曲面族的嵌入、握持与 reach。
