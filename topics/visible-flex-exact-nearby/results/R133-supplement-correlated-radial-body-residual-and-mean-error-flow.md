# R133 补篇：共同径向多项式残差与完整均值误差方程

2026-11-14。**下述恒等式、区间算法及五个实际闭片界已证明。**
完整7721片正在分段计算；本篇没有声称全体残差或连续逆已经完成。
所有列仍属于原 ac1 算子，不将它们改名为连续修复后的算子。

## 1. 为什么更换残差表示

原 body v3 已完成全部7721条系数及正反均值数组，随后在523条体残差处保存
并主动停止。将 $h'$ 与 $Ah$ 分别取宽区间会丢掉它们的实际抵消；所得大上界
不能判定真实残差大，更不能判定解不存在。

本篇保留原全部 Hermite 数据、目标、参数、均值和 Fourier 输出。
仅在同一径向变量里先计算准确的 $h'-Ah-F_\nu$ 多项式，再取范数。
真实参数仍是 $\eta=\eta_0+\delta\eta$、$|\delta\eta|\le10^{-9}$，
不是仅在 $\eta_0$ 的采样。

## 2. 准确的两条 mean 误差方程

按 mean 与非零模分块，记

$$
A=\begin{pmatrix}A_\perp&a\\ b&c\end{pmatrix},\qquad
D=\partial_r-A,
\quad
c=\beta\bigl(1-\langle u^2+Kv^2\rangle-2Km^2\bigr),
\quad m=\langle v\rangle.
\tag{C.1}
$$

这里完整块 $b$ 为

$$
bw=-2\beta m\langle uw_1+K(v-m)w_2\rangle,
\qquad
b^*=-2\beta m\binom{u}{K(v-m)}.
\tag{C.2}
$$

$a=(Ae_2)_\perp$ 由同一个完整 moving 算子计算，含零 mean 原函数项
和真正的 $\gamma\langle h_2\rangle JQ_\varphi$ 项。不得只取局部矩阵第二列。
(C.2)直接由完整 mean 方程微分，且与直接算出的 $A^*e_2$ 非零部分一致。

原完整有限试解分别写成
$\widehat q=(w,\widehat z)$、$\widehat\psi=(\lambda,\widehat\mu)$。
其 mean 不是先验真解；这里只把它作为高质量的显式近似。
定义完整残差

$$
R_q=D\widehat q-F_\nu,\qquad R_\psi=D^*\widehat\psi.
\tag{C.3}
$$

令真正回填的 $z,\mu$ 满足原已证 mean 方程及真正右 regular/左腰幅 mean 条件，
并令 $e_z=z-\widehat z$、$e_\mu=\mu-\widehat\mu$。
逐式相减得到

$$
e_z'=c e_z-(R_q)_0,\qquad
e_\mu'=-c e_\mu+(R_\psi)_0.
\tag{C.4}
$$

第一条从右端反向积分，第二条从左端正向积分。
右端数据为 $e_z(R)=z_R-\widehat z(R^-)$，左端数据为
$e_\mu(0)=\mu_0-\widehat\mu(0^+)$；$z_R$ 和 $\mu_0$ 仍使用完整物理端口。
它们没有被有限模型中的 mean 零值代替。

由于真正的 $z,\mu$ 连续，每一条原有限试解 mean 跳都给

$$
e(r_i^+)=e(r_i^-)-[\widehat e]_{r_i}.
\tag{C.5}
$$

因此正向推进先积分后减去右跳，反向推进在向左积分前加回右接口的原跳。
代码准确保留这两个方向。所有跳来自原 dyadic Hermite 系数的有理 Horner 运算。

真正完成均值后的非零残差为

$$
R_{q,\perp}^{\rm true}=R_{q,\perp}-a e_z,
\qquad
R_{\psi,\perp}^{\rm true}=R_{\psi,\perp}-b^* e_\mu.
\tag{C.6}
$$

两个 mean 残差准确为零。这没有把未知 mean 删除：它们分别由(C.4)及真实端值
恢复，并经(C.6)反馈回完整非零方程。

## 3. 同一径向变量和完整 angular 支撑

对每个真实闭区间 $[l,r]$，设
$t=(x-(l+r)/2)/h$、$h=(r-l)/2$。
原背景和两条完整试解的所有 cubic 及其真实径向导数先准确换成 $t$ 的多项式。
不跨任何背景/试解 PPoly 接缝、原 scalar germ 或 compact-control 接缝。

每个真实标量 $f\in\{\gamma,\beta,K,s\}$ 使用

$$
f(x)=f(c)+h f'(c)t+\tfrac12h^2f''(c)t^2+
\tfrac16h^3 f'''(\xi_x)t^3,
\qquad \xi_x\in[l,r].
\tag{C.7}
$$

中点前三项和整闭盒第三导数都使用完整真实 primitive 及其无限尾。
将每个有向系数选取 dyadic 中心，多余半径进入统一径向 Wiener 误差。
最后一项是允许随 $x$ 变化的余项，不被冒称为常系数 cubic。

这类误差只来自径向标量；$\bar Q$ 本身保留全部32模、试解保留全部96模。
故即使包含标量 primitive 的无限尾，当前试解残差仍准确具有最多
$96+2\cdot32=160$ 的角指标支撑。512点有向 FFT 容纳全部乘积。
这里没有对未知无限角尾求导：当统一误差的实际角支撑为 $|j|\le d$ 时，

$$
\|\partial_\varphi e\|_{A^0}\le4d\|e\|_{A^0},\quad
\|Ie\|_{A^0}\le\tfrac14\|e\|_{A^0},\quad
\|e-\langle e\rangle\|_{A^0}\le\|e\|_{A^0}.
\tag{C.8}
$$

角常数误差的导数与原函数准确为零。乘法统一误差使用
$N_1E_2+N_2E_1+E_1E_2$，并传播每个误差的真实有限支撑。
这样非局部原函数、rank-one mean、全部局部项和径向导数在取范数前已经共同抵消。

compact 参数列的准确符号仍为
$\gamma_\nu=w\gamma/2$、$K_\nu=-wK+T w'$，其中
$T=\beta/(2\gamma^2a^2)$。
$T$ 到三阶的 jets 由同一真 $a,\gamma,\beta$ 算出；所需
$a'=\beta a$、$a''=(\beta'+\beta^2)a$、
$a'''=(\beta''+3\beta\beta'+\beta^3)a$ 都是恒等式。
原 $w=4096[t_0(1-t_0)]^6$ 在其真实支集内以完整12次多项式保留。
这里物理响应已含背景 $s_\nu$，不再额外加入一次该列。

## 4. 径向积分、mean 流和完整配对

有限径向多项式先准确转成 Legendre 多项式。若
$p(t,\varphi)=\sum_k P_k(\varphi)L_k(t)$，则

$$
\int_l^r\|p\|_{H^s_\varphi}^2\,dx
=(r-l)\sum_k{\|P_k\|_{H^s_\varphi}^2\over2k+1}.
\tag{C.9}
$$

Fourier Gram 保留两符号和 mean。统一误差 $E$ 对 $H^s$ 的费用是
$(1+(4d)^2)^{s/2}E$，再乘 $\sqrt{r-l}$ 加入局部径向 $L^2$。
原 $A_\sigma$ 费用另保 $e^{4d\sigma}E$。

对(C.4)中 $e'=A(x)e+B(x)$，整盒 $A\in\mathbf A$、$B\in\mathbf B$
给标准变常数包络

$$
e(h)\in e^{h\mathbf A}e(0)+h\phi_1(h\mathbf A)\mathbf B,
\qquad \phi_1(z)=(e^z-1)/z.
\tag{C.10}
$$

系数可以真正随 $x$ 变化：指数权始终正，积分权由 $\mathbf A$ 的两个端点
夹住。$\phi_1$ 用完整 Taylor 尾证明，不采用未证明的点值指数。
将 $h$ 换成 $[0,h]$ 同时给整片误差包络。
完整消费者必须先核齐全部7721片及其顺序、共同输入和 source，再推进两条流。
任何缺片、重叠、换源或只到中间点的报告都不能触发完整结论。

最后按(C.6)合并每片的 $L^2,H^{1/3},H^1,A_\sigma$ 费用。
全部原非零模跳仍另外相加；完成的 mean 跳准确为零。
有符号体配对也保留相关项：

$$
\int\langle\psi,R_q^{\rm true}\rangle
=\int\langle\lambda,R_{q,\perp}\rangle
 -\int\langle\lambda,a\rangle e_z.
\tag{C.11}
$$

第一项在共同径向多项式中准确积分；第二项使用真实 mean 误差流。
零 Fourier 卷积直接配对相反频率，不通过可能混叠的256阶乘积采样取 mean。
边界仍接此前完整物理 regular/腰幅消费者，并不由(C.11)自动授予 Schur 非零。

## 5. 已实际完成的必要域检查与正在执行的范围

以下均是同一个原 ac1/全 $\eta$ 对象的真实闭片；表中尚未加(C.6)的全域 mean 误差。

| 原公共 row | 域的用途 | 响应非零 $L^2$ sup | 伴随非零 $L^2$ sup |
|---:|---|---:|---:|
| 0 | 腰起始片 | $5.167782\,10^{-7}$ | $6.892447\,10^{-5}$ |
| 477 | 原宽盒界暴涨处 | $6.129725\,10^{-7}$ | $6.962764\,10^{-5}$ |
| 1000 | 真 compact 参数支集内 | $2.093195\,10^{-6}$ | $6.846824\,10^{-5}$ |
| 6000 | 正型主体 | $1.854931\,10^{-7}$ | $3.122211\,10^{-5}$ |
| 7719 | 真自然 graft | $1.464472\,10^{-13}$ | $1.365327\,10^{-12}$ |

row477 的 mean 残差分别含于约 $\pm4.268\,10^{-9}$ 与
$[-1.920,2.748]\,10^{-5}$。这解决了原先分别包裹导致的巨大误差，
但仍须完成全域(C.4)，不能把这五片当成全主体。

完整分片作业共享同一全输入，只算尚未完成的互斥 row；五个实际成功片不重算。
每个子过程有明确 AS 上限和独立 checkpoint/退出记录。
原 row477 无 AS 的 profiling 过程曾实际退出137且没有 native，原因未证明；
保留该事实后，同一数学源的 AS1792MiB 实际计算正常返回0。
原 signed 积分的794片被真实进程信号终止，亦保留后沿同源恢复。
这些过程事件不改任何数学 gate，也不成为终止研究的理由。

完整新 mean-error 消费器现已实现；尚未拿未完成的7721片作为其执行输入。
全频主体逆、修复中心的算子差、未知高模反馈和真正非线性闭合仍须继续支付。
