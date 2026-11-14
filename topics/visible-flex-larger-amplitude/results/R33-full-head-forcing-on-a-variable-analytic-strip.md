# R33：变解析条带上的全头非线性源与完整频率闭合

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

状态：**已证明，带明确可计算输入的全频闭合工具**。本文修复 R23 的径向 $L^1$ 源到同一条带强状态范数的失导数问题：改用逐频率径向密度范数，在一个固定的、沿径向变化的解析条带空间中构造 Green 算子。有限频窗之外的全部高频用显式积分核支付，不把每次迭代丢一条带伪装成同一 Banach 空间上的收缩。实际强尾尚未支付本文全部数值门。

## 1. 实背景、物理变量与一个固定函数空间

取一个有限真实径向区间 $I=[a,b]\subset(r_c,R_{\rm out}]$，其中 $a>r_c>0$。背景为

$$
g=(1+w(r)^2)\,dr^2+r^2d\theta^2,\qquad
0<w(r)\le\frac12.
\tag{33.1}
$$

要求 $w\in C^1(I)$，允许有限个具有相同一阶数据的光滑片接缝；在开光滑片上有足够的经典正则性。所有函数指同一固定实源，不混用保存的独立 $E,w,E'$ 字段。R31 已证明当前 R26 全背景 $w<1/2$，但这不表示下述非轴输入已经支付。

令 $h=h_0+v_h$、$h_0'=w$，并记

$$
p=\frac{(v_h)_\theta}{r},\qquad
\kappa=(v_h)_r,\qquad
\mathsf P=\frac p w,\qquad
K=\frac\kappa w,\qquad
\lambda=\frac{w_r}{w},\qquad c=\frac1r+|\lambda|.
\tag{33.2}
$$

$\kappa_\perp$ 是非均值部分；均值由第 2 节的完整 holonomy 小根决定。

选择一个正幅度函数 $V(r)>0$、一个权 $B(r)\ge1$，以及解析角宽 $\tau(r)\ge\tau_{\min}>0$。先假设这三个函数为分片 $C^1$ 且连续；后述向外收缩的权跳变也允许。物理归一状态为

$$
U_1=\frac{Bp}{V},\qquad U_2=\frac{\kappa_\perp}{V}.
\tag{33.3}
$$

取非零偶 Fourier 频率，定义

$$
\boxed{
\|U\|_{\mathcal X}
=\sum_{m\ne0}(1+|m|)
\left[
\sup_{r\in I}e^{\tau(r)|m|}|U_{1,m}(r)|
+\sup_{r\in I}e^{\tau(r)|m|}|U_{2,m}(r)|
\right].}
\tag{33.4}
$$

这里先逐模、逐分量取径向 supremum，再求和。空间在一次选定 $B,V,\tau$ 后保持不变，固定点迭代不再改变它们。

对标量 Fourier 场，类似地写

$$
\|f\|_{\mathcal A_k}
=\sum_m(1+|m|)^k
\sup_r e^{\tau(r)|m|}|f_m(r)|.
\tag{33.5}
$$

由于 $e^{\tau(r)|m|}\le e^{\tau(r)|j|}e^{\tau(r)|m-j|}$，且
$1+|m|\le(1+|j|)(1+|m-j|)$，这些空间对乘法为 Banach 代数。证明直接使用逐项卷积、supremum 的次乘性和非负级数交换；不是把点态 Wiener 界自动换成强径向界。只依赖 $r$ 的系数是此代数中的中心元素，其范数为普通 supremum。

令

$$
A_*=\sup_I\frac Vw.
\tag{33.6}
$$

则每个实径向点的相对一阶范数满足

$$
\|\mathsf P(r)\|_{\tau(r),1}
+\|K_\perp(r)\|_{\tau(r),1}
\le\frac{V(r)}{w(r)}\|U\|_{\mathcal X}.
\tag{33.7}
$$

下面的主要域条件是 $A_*\|U\|_{\mathcal X}\le1/64$。这是完整径向输入，不能从端点小量推定。

## 2. 完整 mean 小根在 $w\le1/2$ 的统一域

这一节把 R23 所用的小根界推广到外头也可使用的域。令

$$
S=1-w^2\mathsf P^2,\qquad
D=1-w^2(2K+K^2+E\mathsf P^2),\qquad E=1+w^2.
$$

准确转角率为

$$
\Gamma=
\left(1+\frac{w^2(1+K)\mathsf P_\theta}{S}\right)D^{-1/2}.
\tag{33.8}
$$

在 $w=0$ 用解析延拓解释归一式

$$
\frac{\Gamma-1}{w^2}=K+\mathsf P_\theta+\mathcal R(K,\mathsf P).
\tag{33.9}
$$

设 $T=\|K\|_0+\|\mathsf P\|_1\le1/20$。所有范数可以是某个固定角宽 Wiener 代数，也可以是 (33.5) 的强代数。二项级数与几何级数给

$$
\|\mathcal R(K,\mathsf P)\|_0\le2T^2,\qquad
\|\partial_K\mathcal R\|_{0\to0}\le\frac52 T\le\frac18.
\tag{33.10}
$$

第二个算子界在这里只沿常数 mean 方向使用。

给出常数核算。置 $z=w^2(2K+K^2+E\mathsf P^2)$，则
$\|z\|\le(2T+5T^2/4)/4<3/100$。将 (33.9) 的余项依次分成

$$
\begin{aligned}
\mathcal R={}&
\tfrac12(K^2+E\mathsf P^2)
+\frac{(1-z)^{-1/2}-1-z/2}{w^2}\\
&+\frac{K+w^2\mathsf P^2}{1-w^2\mathsf P^2}\mathsf P_\theta\\
&+\frac{(1+K)\mathsf P_\theta}{1-w^2\mathsf P^2}
\bigl((1-z)^{-1/2}-1\bigr).
\end{aligned}
\tag{33.11}
$$

第一项至多 $5T^2/8$；第二项使用二阶 Taylor 余项系数 $\le1/2$，至多 $9T^2/16$。第三项使用
$\|K\|\|\mathsf P\|_1\le T^2/4$，至多 $3T^2/10$。最后一项用
$(1-z)^{-1/2}-1$ 的范数 $\le3\|z\|/5$，至多 $7T^2/20$。四常数之和为 $147/80<2$。求常数 $K$ 方向导数后，

$$
\partial_K\frac{\Gamma-1}{w^2}
=\frac{\mathsf P_\theta}{S}D^{-1/2}
+\left(1+\frac{w^2(1+K)\mathsf P_\theta}{S}\right)
(1+K)D^{-3/2}.
$$

减去1，使用 $D^{-1/2}\le21/20$、$D^{-3/2}\le11/10$、
$\|D^{-3/2}-1\|\le7\|z\|/4$ 及 $S^{-1}\le(1-T^2/4)^{-1}$，得到
$(43/30+231/256)T<(5/2)T$。所有比较均只涉及上面的有理范围。

现在令 $\mathsf P,K_\perp$ 均无均值，且
$R=\|\mathsf P\|_1+\|K_\perp\|_1\le1/32$。在 $|M|\le4R^2$ 上，
$K=K_\perp+M$ 给 $T\le R+4R^2\le9R/8<1/20$。
方程

$$
M=-\langle\mathcal R(K_\perp+M,\mathsf P)\rangle
\tag{33.12}
$$

把此圆盘映入自身，因为 $2(9/8)^2R^2<4R^2$；由 (33.10) 它收缩。故存在唯一完整 holonomy 小根，且

$$
\boxed{|M|\le4R^2.}
\tag{33.13}
$$

迭代由全纯运算构成并一致收敛，所以小根全纯。若 $R\le1/64$，在非均值输入周围作半径 $R$ 的复 Cauchy 圆盘，整个圆盘位于 $1/32$ 域，给

$$
\|DM\|\le16R.
\tag{33.14}
$$

这些结论包含全部频率，且实输入保持实根。实数据下 $S,D$、后面出现的 $1+K+E\mathsf P_\theta$ 均严格为正。

在第 1 节的归一里，令 $a_0(r)=V(r)/w(r)$。将 $M=a_0^2\widetilde M$ 代入 (33.12)，余项在 $(K,\mathsf P)$ 中的每个单项总次数至少为2；除去 $a_0^2$ 后，其余 $a_0$ 都为非负幂的中心系数。相同代数证明遂给

$$
\|\widetilde M\|_{\mathcal A_0}\le4\|U\|_{\mathcal X}^2.
\tag{33.15}
$$

这一步明确支付了径向 supremum；不依赖把仅逐点存在的 mean 根拼成未经控制的强范数函数。

由于 $M$ 本身只有第零 Fourier 模，(33.15) 也可直接由逐点二次界除以 $a_0(r)^2$ 后取 supremum 得到；此处没有交换无限频率和径向 supremum 的次序。

## 3. 全频源的点态密度范数

R23 的真实物理方程在非均值变量上为

$$
p_r=\frac{(\kappa_\perp)_\theta-p}{r},\qquad
(\kappa_\perp)_r
=-\lambda(\kappa_\perp+p_\theta)+f,
\tag{33.16}
$$

其中完整 mean $K_0=M$ 已保留，且

$$
f=w\,\mathscr H_\perp,\qquad
\mathscr H=
(1+K+E\mathsf P_\theta)^{-1}
\left[
\frac E r(K_\theta-\mathsf P)^2
+\lambda(K+\mathsf P_\theta)^2
+\lambda w^2
(2K\mathsf P_\theta+\mathsf P_\theta^2-\mathsf P^2)
\right].
\tag{33.17}
$$

这来自完整点态 Darboux 方程；不是有限 Galerkin 的压缩乘法逆。

定义严格正的源密度

$$
d(r)=\frac{c(r)V(r)^2}{w(r)}
$$

及强源范数

$$
\boxed{
\|f\|_{\mathcal Y}
=\sum_{m\ne0}\sup_{r\in I}
\frac{e^{\tau(r)|m|}|f_m(r)|}{d(r)}.}
\tag{33.18}
$$

若 $A_*\|U\|_{\mathcal X}\le1/64$，则

$$
\boxed{\|f(U)\|_{\mathcal Y}\le16\|U\|_{\mathcal X}^2.}
\tag{33.19}
$$

若两个输入均在此域，则

$$
\boxed{
\|f(U)-f(\widetilde U)\|_{\mathcal Y}
\le32(\|U\|_{\mathcal X}+\|\widetilde U\|_{\mathcal X})
\|U-\widetilde U\|_{\mathcal X}.}
\tag{33.20}
$$

**证明。** 在 (33.5) 的强代数中，除去 $a_0=V/w$ 后，
$K_\theta-\mathsf P$ 的范数至多 $X:=\|U\|_{\mathcal X}$；
$K+\mathsf P_\theta$ 的范数至多 $2X$。完整 $K/a_0$ 的范数也至多 $2X$，由 (33.15) 及 $A_*X\le1/64$ 保证。分母与1之差的范数小于 $1/2$，其逆范数至多2。

将方括号除以 $c\,a_0^2$，三个中心系数的绝对值分别至多 $2,1,1/4$；三个二次式分别至多 $X^2,4X^2,6X^2$。因此乘逆后至多
$2(2+4+6/4)X^2=15X^2<16X^2$。
非均值投影在 $\mathcal A_0$ 中范数不超过1。

差分时，完整 $K/a_0$ 及 $K+\mathsf P_\theta$ 的归一差范数至多 $2\|U-\widetilde U\|_{\mathcal X}$；这由 (33.14) 或归一 Cauchy 界得到。方括号的归一差至多
$(15/2)(X+\widetilde X)\|U-\widetilde U\|$。
逆因子差至多 $16A_*\|U-\widetilde U\|$；与另一个二次式相乘后的额外项至多
$120A_*\widetilde X^2\|U-\widetilde U\|$。
使用 $A_*\widetilde X\le1/64$，总常数小于32，给 (33.20)。$\square$

mean 高度不另设一个边值条件。由 (33.13)，它沿头部的物理修正满足

$$
|(v_{h,0})_r|\le
4\frac{V(r)^2}{w(r)}X^2,
\qquad
|\Delta v_{h,0}|
\le4X^2\int_I\frac{V^2}{w}\,dr.
\tag{33.21}
$$

这是从同一个 mean 根统一积分的高度，不允许逐胞元重置。

## 4. 有限窗 Green 与物理变量转换

固定自由低频集合 $\mathcal L=\{2,4,\ldots,92\}$。在内端 $r=a$，低频使用 R18 **准确线性深图**的直线；在外端 $r=b$ 固定低频高度。对 $|m|>92$，线性参考的内端两分量均为零，非线性深 trace 的全部高频稍后由边界提升加入。高频外端高度保持自由。

低频的准确 Wronskian 必须非零。满足该条件时，R29 的两端 Green 公式给低频核；高频使用向外的初值 Volterra 核。这些核都对应同一个真实 $w$。不能在内端把理想 Robin 与准确线性深图不加误差地互换。

为转用 R29 的列，物理 canonical 坐标满足

$$
p_m=imr^3Q_m,\qquad
(\kappa_\perp)_m=m^2r^3Q_m+
\frac{\sqrt{12}\mu_n}{r^4w}\Xi_m,
\qquad
f_{\Xi,m}=\frac{r^4w}{\sqrt{12}\mu_n}f_m.
\tag{33.22}
$$

$\Xi_n$ 随胞元换规范，$p,\kappa$ 则连续；因此本结果没有在胞元接缝忘记 $\mu$ 因子。

写 $K_m(r,s)$ 为从物理 $f_m(s)$ 到物理二向量 $(Bp,\kappa_\perp)_m(r)$ 的准确 Green 核。它对低频有两个积分分支，对高频在 $s>r$ 时为零。定义

$$
g_m=(1+|m|)\sum_{i=1}^2
\sup_{r\in I}\frac1{V(r)}
\int_I |K_{m,i}(r,s)|\,d(s)
e^{(\tau(r)-\tau(s))|m|}\,ds.
\tag{33.23}
$$

若有 $g_m\le\gamma$ 对全部非零偶频率成立，则

$$
\boxed{\|\mathcal Gf\|_{\mathcal X}\le\gamma\|f\|_{\mathcal Y}.}
\tag{33.24}
$$

**证明。** 置
$F_m=\sup_s e^{\tau(s)|m|}|f_m(s)|/d(s)$。
逐模逐分量的三角不等式给输出强范数至多
$\sum_m g_mF_m\le\gamma\sum_mF_m$。
没有再乘频数，也没有把两个分量的 supremum 合成较小的“先相加再取 supremum”。$\square$

只要选定一个有限偶阈值 $M>92$，所有 $0<|m|<M$ 的 (33.23) 都是有限计算：

- $|m|\le92$：使用同一实源的准确互补边界列、Wronskian 以及径向 panel 上的核积分；
- $92<|m|<M$：使用准确向外 Cauchy 列或对一组频率同时有效的正比较矩阵；
- 输入权 $d(s)$ 必须留在实际源位置，输出 $V(r)$ 及角权必须留在实际输出位置。把两个不相容位置的最大值先粗乘仍然有效，但可能严重浪费预算。

第 5 节给剩余无限频率一个显式上界，因此 (33.24) 不再要求逐个计算无限多个模式。

## 5. 连续条带恢复高频的一阶角导数

物理二向量 $Y_m=(Bp_m,\kappa_{\perp,m})$ 的线性方程为

$$
Y_m'=
\begin{pmatrix}
B'/B-1/r&imB/r\\
-im\lambda/B&-\lambda
\end{pmatrix}Y_m+
\begin{pmatrix}0\\f_m\end{pmatrix}.
\tag{33.25}
$$

定义可计算的非负函数

$$
\alpha=\max\{0,B'/B-1/r,-\lambda\},\qquad
\beta=\max\{B/r,|\lambda|/B\},
$$

$$
\eta=\max\{0,\alpha-(\log V)'\}.
\tag{33.26}
$$

归一线性传播 $Y/V$ 的复 $\ell^1$ 矩阵范数由列和估计得到

$$
\|\mathcal U_m(r,s)\|_1
\le\exp\!\int_s^r(\eta+|m|\beta)\,du,
\qquad s\le r.
\tag{33.27}
$$

对角项使用其实数符号；没有把负的 $-1/r$ 或 $-\lambda$ 无理由改为绝对值。

假设存在 $\chi(r)>0$ 及常数 $k>0$，满足

$$
\boxed{
-\tau'\ge\beta+\frac{\eta}{M}+\chi,\qquad
\frac{d(r)}{V(r)}=\frac{c(r)V(r)}{w(r)}\le k\chi(r).}
\tag{33.28}
$$

则全部 $|m|\ge M$ 的向外 Green 响应满足

$$
\boxed{g_m\le2k\left(1+\frac1M\right).}
\tag{33.29}
$$

**证明。** 由 (33.27)、(33.28)，对 $|m|\ge M$，

$$
e^{(\tau(r)-\tau(s))|m|}
\|\mathcal U_m(r,s)\|_1
\le e^{-|m|\int_s^r\chi}.
$$

源归一后是 $(0,f_m/V)$。对每个输出分量，

$$
\begin{aligned}
&(1+|m|)\int_a^r
e^{-|m|\int_s^r\chi}\frac{d(s)}{V(s)}\,ds\\
&\quad\le k(1+|m|)
\int_a^r\chi(s)e^{-|m|\int_s^r\chi}\,ds
\le k\frac{1+|m|}{|m|}.
\end{aligned}
$$

再按 (33.4) 分别取两个分量的 supremum，得到 (33.29)。$\square$

这里恰是连续核积分提供了 $1/|m|$，补回状态范数中的一个角导数。若把源只控制在径向 $L^1$，任意窄的源峰会取消这一积分收益，故原来的失导数不能靠简单写成同一 $\tau$ 的 $\sup_m\Gamma_m$ 来修复。

实际可以先选 $\gamma_{\rm hi}>0$，令
$k=\gamma_{\rm hi}/[2(1+1/M)]$，再取
$\chi=cV/(kw)$。需要支付的总角宽就是

$$
\int_I\beta\,dr+\frac1M\int_I\eta\,dr
+\frac1k\int_I\frac{cV}{w}\,dr
\le\tau(a)-\tau(b).
\tag{33.30}
$$

这是正材料积分与实际幅度包络的预算，不是未知的无限模范数。也可选择更有利的 $\chi$，或直接用 (33.23) 支付若干中间频带。

若 $B$ 在胞元间向外下降而 $V$ 连续，$Y/V$ 的跳变矩阵为
$\operatorname{diag}(B_+/B_-,1)$，范数不超过1，因此不增加 (33.27) 的代价。更一般的已知正规范放大 $J>1$ 可在 $\tau$ 中加入向外下降至少 $(\log J)/M$ 的一次跳变。实际物理 $p,\kappa$ 仍须连续；这些跳变只属于辅助范数。

### 5.1 已有深头材料界给出的有限规模

在 physical node225 到 node12 的 213 个胞元中，取 R22 的逐胞元常数 $B_n$，向外切换不会增大范数。其积分满足
$\int\beta<4$，而

$$
\int\alpha\le(\log2)\sum_{n=12}^{224}(3n+32)
=82218\log2.
\tag{33.31}
$$

若选 $V$ 向外非递减，则 $\eta\le\alpha$。例如 $M=4096$ 时，$\log2<7/10$ 给

$$
\int\beta+\frac1M\int\eta
<4+\frac{287763}{20480}<18.052.
\tag{33.32}
$$

因而从角宽38到角宽1的预算中，还留下超过18.948的宽度给 $\chi$。这只支付该区间的**线性材料代价**；$V$ 的真实包络、$\int cV/w$、有限模式 $m<4096$ 的 Green、以及 R18 宽度38输入球仍须各自核销。外侧 0 至 11 胞元若纳入同一个区间，其三项积分也必须加入，不能从 (33.32) 免费得到。

## 6. 真正非线性深图的边界提升

取 R18 的 F224（physical node225）作为 $r=a$，并固定深端角宽 $\tau_F$。设

$$
S_F=\frac{\epsilon_{\rm phys}\delta_{224}^{11/2}}{r_c^{10}},
\qquad
z_j=(-1)^{224j}e^{2j\tau_F}Q_{{\rm phys},2j}(a)/S_F.
\tag{33.33}
$$

令 $\mathcal D(z)$ 为 R18 真正完整 trace 与具有相同低46高度的准确线性 trace 之差，使用其归一 raw 范数。R18 已给

$$
\|\mathcal D(z)\|_{\rm raw}\le C_D|z|_1^2,\qquad
C_D=2^{1967},\qquad |z|_1\le2^{-1947}.
\tag{33.34}
$$

$\mathcal D$ 的低46高度分量为零，低46动量及全部高频的高度/动量均保留。因为图在此复球全纯，若 $|z|_1\le2^{-1948}$，Cauchy 估计给

$$
\|D\mathcal D(z)\|\le4C_D|z|_1.
\tag{33.35}
$$

这不是把 (33.34) 仅有的实数二次界擅自微分；使用的是 R18 已建立的完整全纯图。

记 $\mathcal B$ 为把 $\mathcal D$ 的边界偏差提升到头部的准确线性解算子。低频在浅端高度为零，深端满足相应 Robin 缺陷；高频直接给内端两分量，浅端高度自由。对于 R29 的规范 $\phi_Q(a)=1$，$\psi_Q(b)=0$、物理 Wronskian $W_m$，低频 raw 动量缺陷 $d_m$ 的提升为

$$
\mathcal B_m d_m(r)=\frac{\mu(a)}{W_m}\psi_m(r)d_m.
\tag{33.36}
$$

因为 $\psi_\Xi(a)-t_m\psi_Q(a)=W_m/\mu(a)$，此式逐项满足两端条件。输入归一 $\mathcal D$ 时还须乘回 $S_Fe^{-|m|\tau_F}$ 及无害的相位符号。高频则使用真实 Cauchy 传播。

要求核销

$$
\|\mathcal B d\|_{\mathcal X}\le b_D\|d\|_{\rm raw}.
\tag{33.37}
$$

有限模式按真实列直接计算。无限模式也有有限显式尾界：若
$\delta_F=\tau_F-\tau(a)>0$，第 5 节的传播给

$$
b_{D,\rm hi}
\le
\frac{2S_F}{V(a)}
\left[
a^3(B(a)+1)+\frac{\sqrt{12}\mu(a)}{a^4w(a)}
\right]
\left(1+\frac3{\delta_F}\right)^3.
\tag{33.38}
$$

证明只需把 (33.22) 的端点矩阵作用到 raw 两分量，再用
$\sup_{m\ge0}(1+m)^3e^{-\delta_Fm}\le(1+3/\delta_F)^3$；
两个输出分量的独立 supremum 给安全因子2。有限正比较频带或 R22 的真实深 trace 线性包络可以使实际 $b_D$ 更小。

记 $\mathcal E$ 为从头部状态取深端低46归一高度的线性算子，核销
$|\mathcal E U|_1\le e_D\|U\|_{\mathcal X}$。一个直接的有限上界为

$$
e_D\le
\frac{V(a)}{S_FB(a)a^3}
\max_{m\in\mathcal L}
\frac{e^{(\tau_F-\tau(a))m}}{m(1+m)}.
\tag{33.39}
$$

若将 $\mathcal B D\mathcal D\,\mathcal E$ 连成一次带权计算，比先取三个粗范数更小，也可直接使用它的严格算子界。不能删去这个反馈项：内端低高度会随头部非线性校正一起改变。

## 7. 同一 Banach 空间中的全频联合收缩

令 $U^{\rm ref}$ 是第 4 节准确线性参考：低46浅端高度给定，深端在准确线性深图上；高频参考为零。这只定义参考，不是把最后真解的高频设零。记已核销

$$
\|U^{\rm ref}\|_{\mathcal X}\le x,\qquad
z^{\rm ref}=\mathcal E U^{\rm ref},\qquad
|z^{\rm ref}|_1\le z_0.
\tag{33.40}
$$

在固定空间 $\mathcal X$ 中，对校正 $W$ 定义

$$
\mathcal T(W)=
\mathcal G f(U^{\rm ref}+W)
+\mathcal B\mathcal D(z^{\rm ref}+\mathcal E W).
\tag{33.41}
$$

**全频闭合定理。** 假设第 4–6 节的 $\gamma,b_D,e_D$ 已按准确实源核销，包括无限高频；存在 $\rho>0$，令
$T=x+\rho$、$z_*=z_0+e_D\rho$，满足

$$
A_*T\le\frac1{64},\qquad z_*\le2^{-2048},
\tag{33.42}
$$

$$
\boxed{16\gamma T^2+b_D C_D z_*^2\le\rho,}
\tag{33.43}
$$

$$
\boxed{L:=64\gamma T+4b_D C_D z_*e_D<1.}
\tag{33.44}
$$

则 (33.41) 在 $\|W\|_{\mathcal X}\le\rho$ 内有唯一固定点。它给出完整非线性头部解，与 R18 的真正全频深尾准确接合，保留完整 mean，并在外切口达到指定低46高度。外切口的全部高频高度由解决定，不再强加为零。

**证明。** (33.19)、(33.24)、(33.34)、(33.37) 给
$\|\mathcal T(W)\|\le16\gamma T^2+b_D C_Dz_*^2\le\rho$。
对两个输入，(33.20) 给第一项差至多
$64\gamma T\|W-\widetilde W\|$。
第二项在 $z$ 球内沿复线段积分 (33.35)，差至多
$4b_D C_Dz_*e_D\|W-\widetilde W\|$。
故 $\mathcal T$ 以常数 $L<1$ 收缩。

所有频率已包含在 $\mathcal X,\mathcal Y,\mathcal D$ 中，且高频 Green 界由 (33.29) 支付。没有通过频率截断改变方程，也没有在迭代中改变 $V,B,\tau$ 或再损失角宽。Banach 固定点定理因此直接适用。

若边界数据满足实函数所需的 Fourier 共轭对称，映射保持这一闭子空间，因此固定点为实高度；复球只用于统一估计和全纯性。

准确 Green 公式逐模给 (33.16)。$\tau_{\min}>0$ 及强 Fourier 可和性使所有更窄正条带上的角导数一致收敛；积分式与背景正则性给物理状态沿径向的导数。由
$C_m=rp_m/(im)$ 和第一条方程可知 $C_m'=\kappa_{\perp,m}$。
再按 (33.21) 统一积分 mean，得到同一个真实高度 $h$，而非三组互不相容的 $H/P/Q$ 数据。

在深端，低46高度等于 $z^{\rm ref}+\mathcal E W$，低46动量恰等于相同高度下的准确线性深动量加 $\mathcal D$；高频的两分量也等于 $\mathcal D$ 的对应输出。故完整非均值 trace 与 R18 完全相同。完整 mean 小根的唯一性给 slope 一致，mean 高度沿用深尾同一个 cuff 平移规范。完整方程又给二阶径向导数一致。$\square$

### 7.1 为什么 projected 非均值方程恢复完整 mean 方程

这一点不能仅由“均值很小”略过。对由 (33.16) 与 mean 根重建的实高度，非均值 Darboux 方程已经成立，所以完整径向方程的剩余缺陷为一个仅依赖 $r$ 的常数 $c_0(r)$。

使用 R32 的连接 $G\,dr+\Gamma\,d\theta$，$\Gamma$ 只依赖 $h_\theta,h_{\theta\theta},h_r,E$。其径向导数中 $h_{rr}$ 的系数为

$$
\partial_{h_r}\Gamma
=
\frac{h_r+E h_{\theta\theta}/r}
{\bigl(E-h_r^2-Eh_\theta^2/r^2\bigr)^{3/2}}
=\frac{w(1+K+E\mathsf P_\theta)}{D^{3/2}}>0.
\tag{33.45}
$$

$G_\theta$ 不含 $h_{rr}$。对满足准确 Darboux 方程的二阶 jet，
$\Gamma_r-G_\theta=0$，由 R32 的平直恒等式，或直接代入其显式连接可验证。因此一般情形准确有

$$
\Gamma_r-G_\theta=(\partial_{h_r}\Gamma)c_0(r).
$$

完整 mean 根使 $\int_0^{2\pi}\Gamma\,d\theta=2\pi$ 恒定；
对 $\theta$ 积分就得到
$c_0(r)\int_0^{2\pi}\partial_{h_r}\Gamma\,d\theta=0$。
后一个积分严格为正，所以 $c_0=0$。完整 mean 方程确实恢复；不是另设一个不相容的边界条件。

在光滑片上此计算为经典导数，在拼接圈通过连续两 jet 延拓。因此 $h$ 在整个有限头是 $C^2$，并满足真实全频 Darboux 方程。

### 7.2 以真实近似为中心的残差版本

也可使用任意已定义的真实解析路径 $\bar U$，并准确包围

$$
\varepsilon=
\|U^{\rm ref}+\mathcal G f(\bar U)
+\mathcal B\mathcal D(\mathcal E\bar U)-\bar U\|_{\mathcal X}.
\tag{33.46}
$$

把 $T$ 改为 $\|\bar U\|+\rho$，$z_*$ 改为
$|\mathcal E\bar U|+e_D\rho$。若域条件成立，且以这些量定义的 (33.44) 满足

$$
L<1,\qquad \varepsilon+L\rho\le\rho,
\tag{33.47}
$$

则在 $\bar U$ 周围同样得到唯一全频真解。证明对映射在 $\bar U$ 处展开并用同一个 Lipschitz 界即可。残差必须属于准确实源、全部频率、完整 mean 及准确深图；有限 worker 的一个残差数字不能直接代入 (33.46)。

## 8. 低窗必须保留频率与源位置

第 7 节给出一个简单的标量充分门，实际核销时不应为了形式简洁丢掉已知结构。已保存的 M8 参考及低窗 Green 通过一个辅助收缩，不表示扩展至46模后仍通过。尤其把同一个完整源 $L^1$ 质量同时灌入最坏的全部低窗模式，会产生过宽的上界。

可以保留有限个频率或频带的非负核上界，并分别记录
$F_j=\sum_{m\in\mathcal I_j}\sup_r e^{\tau(r)|m|}|f_m|/d$、
状态各块范数及深端低参数。若在闭盒中已有残差向量 $\varepsilon_i$ 与严格非负 Lipschitz 矩阵 $L_{ij}$，且存在正半径向量 $\rho_i$ 与 $q<1$ 满足

$$
\varepsilon_i+\sum_jL_{ij}\rho_j\le\rho_i,\qquad
\sum_jL_{ij}\rho_j\le q\rho_i,
\tag{33.48}
$$

则以 $\max_i\|W_i\|/\rho_i$ 为范数，完全相同的证明给收缩。完整 mean 及倒数产生的跨块项仍须包含在 $L_{ij}$ 中；不能只保留有限多项式卷积的支撑后宣布其余项为零。

这不是额外的存在性要求，而是避免粗上界失效的一种等价实施方式。第 5 节仍一次覆盖最后那个无限频带。

## 9. 与 R23、R29、R31、R32 及深端预算的准确接口

物理范数 (33.4) 与 R23 的 canonical 强范数并不相同。反变换为

$$
Q_m=\frac{p_m}{imr^3},\qquad
\Xi_m=\frac{r^4w}{\sqrt{12}\mu_n}
\bigl(\kappa_{\perp,m}+im p_m\bigr).
\tag{33.49}
$$

R23 对 $Q$ 有三阶角权，对 $\Xi$ 有一阶角权；因此从 (33.4) 反取那个强范数一般还需要一阶角导数。若某胞元上
$\tau(r)\ge\tau_n+\sigma_n$ 且 $\sigma_n>0$，可用

$$
(1+|m|)e^{-\sigma_n|m|}\le1+\frac1{\sigma_n}
\tag{33.50}
$$

与 (33.49) 的实际径向系数支付这一转换。必须保留正角宽差，不能把两种范数的同名半径逐字互换。若只需 R18 的前46个端点参数，可直接使用有限评价 (33.39)，不必先转整个胞元的全部高频。

R29 的真实低窗列可以转成 (33.23)；它们的 scalar $L^1$ Green 常数无需也不应被改名为本文的点态密度常数。R23 的点态精确恒等式已在第 3 节重新核销为强密度界，包含 source 的全部频率和 mean。

R31 给予当前 R26 背景 $|\kappa_0|\le8$。若经 (33.49)–(33.50) 或直接包围真实高度，支付其非轴曲率门，则可得到实际头部的主曲率界。本文的相对存在域 $1/64$ 本身不是 $|\kappa|\le33/4$ 的证书；R31 所用深球 $2^{-16}$ 也不能用 $1/64$ 代替。

与 R18 全频深尾接合后，cuff 的平两 jet 极限来自该同一精确深尾。R32 遂从真实 Darboux 方程与正投影构造全局展开、精确周期和内平盘；外 cut 的严格凸性、Cartesian 外延数据与强前缀两 jet 仍按 R30/R27/R10 核销。若全部门对参数族一致，固定点依赖在该固定空间连续；方程、共同正条带及 R18 两 jet 界将其提升为所需的 $C^2$ 连续性。物理相位族也由 R32 处理。

完整46深参数的较窄 strip 预算可用作 (33.42) 的输入，但必须在本范数中重新转换评价或使用逐模界。仅八个非零参考系数只是参考选择；真实修正允许全部46低模和所有高频非零。

## 10. 当前可核查的有限清单与未支付量

应用本结果需要的是下列具体输入。

1. 同一实源上的 $r,w,w_r,\mu_n$ 与真实端口，含全部外侧 cap/warp 公式；由 R26 及其源区间工具提供。
2. 一次选定的 $B,V,\tau$、$A_*$ 和 (33.30) 的三个材料积分；其中 $V$ 是实际路径球的幅度尺度，不是端点值的替代品。
3. 全部 $m<M$ 的 (33.23) 或更细的有限块核积分，以及 (33.28) 的无限高频门。低46的 Wronskian 非零、中频向外 Cauchy、剩余高频解析尾各有明确职责。
4. 完整低46深参数域、$\mathcal B$ 和 $\mathcal E$ 的真实规范与界，特别是 (33.33) 中的 $r_c^{10}$、$\delta^{11/2}$ 和角宽因子。
5. (33.43)–(33.44)，或保留频率块的 (33.48)，以及实际完整 mean 高度积分。

这些条件全部通过时，第 7 节已证明真正的全频头加深尾存在；没有剩下“把有限窗当作全频”的隐含步骤。当前强 H 的这些条件尚未全部通过，本文也没有把已有 M8 辅助解、有限 worker 或单 cut 修正当成通过。完成闭曲面还需强前缀匹配、全域曲率、法向弦/直径及握持幅度；本结果不改变原课题完成标准。

## 11. 准确常数账本

[tail_full_head_strip_budget.py](../computations/tail_full_head_strip_budget.py)
及其 [有理输出](../notes/2026-11-12-tail-r33-full-head-strip-budget.json)
逐项核算第 2–3 节的根号幂、余项、mean 小根、自映射与源差分常数，以及第 5.1 节的213胞元材料比较。25项准确分数比较均通过；没有径向积分、尾部求解或 Node 作业。

复算命令：

    python computations/tail_full_head_strip_budget.py \
      --out notes/2026-11-12-tail-r33-full-head-strip-budget.json

输出将实际源包络、有限窗 density Green、深图反馈及完整强头闭合均明确标为尚未支付。这份常数账本不能替代第 10 节的候选输入。


## 12. 已支付的实际物理密度与无限高频窗口

本节使用 R35 的 **q003 新实背景**非等半径盒，不使用旧 stored 强前缀的径向轨迹。全部46低模均保留。它实际支付第 5 节的一整个无限频窗及其真正 R18 非线性高边界；$94\le |m|<8192$ 的头内自产源仍未支付。

### 12.1 从同一个 canonical 盒定义物理包络

令 $I_n$ 为 physical cell $n=12,\ldots,224$，$\tau_n=1+(n-12)\log2/4$，并取 R35 已核验盒的准确外包数

$$
\overline X_n=U_n X_n^{\rm ref}.
$$

计算实现将乘积的向外 dyadic 上端点固定为 $\overline X_n$，以后不随未知解变化。记 $\overline\mu_n\ge\mu_n>0$ 为同一真实列保存的 dyadic 上界，$R_*=(257/256)r_c$。取准确固定数

$$
\ell_n\ge\frac{|I_n|}{r_c},\qquad
T_n^{\log}=5(n+9),\qquad
B_n\ge\sqrt{\frac{T_n^{\log}}{\ell_n}},\qquad
a_n\ge1+\frac{2B_n}{9},
$$

其中 $B_n,a_n$ 取逐式向外的 dyadic 上界；$\ell_n$ 取 R22 实宽公式与已包围 $r_{\rm out}-r_{\rm in}$ 的较小上界。定义

$$
\boxed{
V_n(r)=\overline X_n
\left[a_n r^3+\frac{\sqrt{12}\,\overline\mu_n}{r^4w(r)}\right].
}
\tag{33.51}
$$

这是一个固定正函数，不把胞元最小 $w$ 代到端点来定义整条路径的幅度。特别在深端 port，它保留真实 $w(a)=\mu_{224}/r_o(a)^7$。

由 $|m|/(1+|m|)^2\le2/9$、$m^2/(1+|m|)^2\le1$，(33.22) 给：若 $X_{\tau_n}(Z;I_n)\le\overline X_n$，则

$$
\sum_{m\ne0}(1+|m|)
\left[
\sup_{I_n}\frac{e^{\tau_n|m|}|B_np_m|}{V_n}
+\sup_{I_n}\frac{e^{\tau_n|m|}|\kappa_{\perp,m}|}{V_n}
\right]\le1.
\tag{33.52}
$$

具体地，$Q$ 对两个分量的系数和至多
$(B_n|m|+m^2)/[a_n(1+|m|)^2]\le1$；$\Xi$ 的系数至多
$\mu_n/\overline\mu_n\le1$。分别使用 $V_n\ge\overline X_na_nr^3$、
$V_n\ge\overline X_n\sqrt{12}\overline\mu_n/(r^4w)$ 后，先取各分量的径向 supremum 再相加，仍得到 (33.52)。没有交换强范数次序。

所以任何位于该 canonical 盒内的路径，在下述较宽物理条带中满足
$\|U^{\rm low}\|_{\mathcal X_+}\le213$。这里用每个模式的全域 supremum不超过213个胞元 supremum之和；没有将全域范数误写成最大胞元范数。

在212个接口，实际账本逐一验证：

$$
B_{n-1}\le B_n,\quad
\overline X_{n-1}a_{n-1}\ge\overline X_na_n,\quad
\overline X_{n-1}\overline\mu_{n-1}
 \ge\overline X_n\overline\mu_n.
\tag{33.53}
$$

于是 $V$ 向外跳变只增加，且 $B$ 只减少。物理场 $p,\kappa_\perp$ 连续时，$Y/V$ 的接口矩阵
$\operatorname{diag}((B_+/B_-)(V_-/V_+),V_-/V_+)$ 的 $\ell^1$ 范数不超过1。
这将第 5 节的连续权结论直接扩到当前分片权；未知物理高度没有跳变。

### 12.2 三项材料预算及连续条带

在一个开胞元内，$(\log V)'$ 是 $3/r$ 与 $-4/r-\lambda$ 的凸组合。因为 $B_n$ 为常数，$\alpha=(-\lambda)_+$，从而

$$
\eta\le|\lambda|+\frac4r,\qquad
\beta\le\frac{B_n}{r}+\frac{|\lambda|}{B_n}.
\tag{33.54}
$$

R22 的未触发 cap 公式及 $p_*\ge\delta_n/2$ 给
$w\ge\underline\mu_n\delta_n/(2R_*^7)=:\underline w_n$。因此可使用

$$
A_n=
\overline X_n
\left[\frac{a_nR_*^3}{\underline w_n}
+\frac{\sqrt{12}\overline\mu_n}{r_c^4\underline w_n^2}\right]
\ge\sup_{I_n}\frac{V}{w},
$$

$$
D_n=A_n(T_n^{\log}+\ell_n)
\ge\int_{I_n}\frac{cV}{w}\,dr,
\tag{33.55}
$$

以及
$\int_{I_n}\beta\le B_n\ell_n+T_n^{\log}/B_n$、
$\int_{I_n}\eta\le T_n^{\log}+4\ell_n$。所有 $\underline\mu_n$、半径宽度与 $\overline X_n$ 都来自同一真实源的已核验包，不是二进制 profile 样本。

192-bit Arb 的实际输出给

$$
\begin{aligned}
A_*&<5.106082\times10^{-17},\\
D:=\sum_nD_n&<5.435942\times10^{-15},\\
\sum_n\int\beta&<1.214440,\qquad
\sum_n\int\eta<135255.002312.
\end{aligned}
\tag{33.56}
$$

取 $M=8192$，$k$ 为 $4D$ 的 dyadic 上界，$\sigma=1/8$，并令
$\chi=cV/(kw)$。在每个胞元选

$$
-\tau'=
s_n\left[
\frac{B_n}{r}+\frac{|\lambda|}{B_n}
+\frac{|\lambda|+4/r}{M}
+\frac{cV}{kw}
\right],\qquad s_n\ge1.
\tag{33.57}
$$

$s_n$ 由该正实函数积分归一，使其恰好达到保存的两个端点角宽；每个端点差均大于相应已核销积分上界，故 $s_n\ge1$。账本从深端向外递推选端点，并在下一胞元的 $\tau_n-\sigma$ 下截断；另扣准确 $2^{-128}$ 处理有向舍入。这定义一个同一连续条带，不是每次迭代另丢角宽。

全部213个胞元实际满足

$$
\tau(r)+\sigma\le\tau_n\quad(r\in I_n),\qquad
\tau(a)>37.6118005696,\qquad
\tau(b)>0.1444358307.
\tag{33.58}
$$

由 (33.52)，较宽条带 $\tau+\sigma$ 上的低场范数至多213。由 (33.29)，所有 $|m|\ge8192$ 的完整物理源 Green 同时满足

$$
\boxed{\gamma_{\ge8192}<4.349285\times10^{-14}.}
\tag{33.59}
$$

这是真正作用于点态源密度的算子界，覆盖整个无限频带；不是 R34 的端点高 trace 传播界。

### 12.3 真正深图高边界与高窗口非线性闭合

在同一 $V,B,\tau$ 下，用 port 的 $p_*=1$、真实 $\mu_{224}$ 和实半径界代入 (33.38)–(33.39)。实际得到

$$
\log_2 b_{D,\ge8192}<2230.959822,\qquad
\log_2 e_D<-2182.086936.
\tag{33.60}
$$

这里 $\tau_F=38$，$\tau_F-\tau(a)>0.3881994303$；$S_F$ 仍是 (33.33) 的物理尺度，没有省掉 $r_c^{10}$。R35 盒的完整46低高度满足
$|z|_1<2^{-2203.2158567}<2^{-2200}$。完整 mean 由相同小根给出。

固定一个频率支撑在 $|m|<8192$ 的物理低场 $L$，假设
$\|L\|_{\mathcal X_+}\le213$ 且其46个深高度为上述 $z$。特别，R35 的低46辅助解满足此范数条件；这一步没有说它已经解了其余中频方程。对 $H=P_{\ge8192}H$ 定义

$$
\mathcal T_{\rm hi}(H)
=\mathcal G_{\rm hi}P_{\ge8192}f(L+H)
+\mathcal B_{\rm hi}P_{\ge8192}\mathcal D(z).
\tag{33.61}
$$

其中 $f$ 每次都使用完整 mean 根和完整点态倒数。因为
$\tau+\sigma$ 上的 $f(L)$ 强密度范数至多 $16\cdot213^2$，投影到 $|m|\ge8192$ 后限制到 $\tau$ 给

$$
\|\mathcal G_{\rm hi}P_{\ge8192}f(L)\|_{\mathcal X}
\le16\gamma_{\rm hi}\,213^2e^{-8192/8}
<2^{-1502.2365}.
\tag{33.62}
$$

这次条带余量只用于固定低场产生的高残差；高未知量本身仍在同一个 $\tau$ 空间迭代。真正深图的高边界给

$$
\|\mathcal B_{\rm hi}P_{\ge8192}\mathcal D(z)\|_{\mathcal X}
\le b_{D,\rm hi}2^{1967-4400}<2^{-202.0401}.
\tag{33.63}
$$

在 $\|H\|_{\mathcal X}\le2^{-190}$ 内，
$A_*(213+1)<1/64$，完整 mean 域成立；(33.20) 给映射的 Lipschitz 常数

$$
L_{\rm hi}\le64\gamma_{\rm hi}(213+1)
<5.956780\times10^{-10}.
\tag{33.64}
$$

(33.62)、(33.63) 加上 $L_{\rm hi}2^{-190}$ 小于
$0.000237436\cdot2^{-190}$。故 (33.61) 在该闭球严格自映并收缩，给唯一的完整无限高频响应。高源的 Cauchy 初值为零，非零高初值恰来自真正 R18 $\mathcal D(z)$；没有把高 trace 删除。

此处保持 $z$ 固定是合法的：$\mathcal E$ 只评价低46高度，而 $H$ 的支撑为 $|m|\ge8192$，所以 $\mathcal EH=0$。将低场也作为未知量时，低场到 $z$、再到全部深图的反馈仍须加入联合块矩阵；R36 已支付的低深图部分可作为其中一个块。

### 12.4 可重算文件和准确剩余窗口

工具为 [tail_r33_physical_density_budget.py](../computations/tail_r33_physical_density_budget.py)，实际输出为
[完整213胞元密度账本](../notes/2026-11-12-tail-r33-physical-density-window.json.gz)。
它保存全部包络系数、角宽端点、212个接口、8项真门、输入和工具 hash；
正式退出码为0，未作径向积分、Node 作业或新的数值 BVP。源码中的范数和输出明确保留完整 mean、全部46深参数及全部 $|m|\ge8192$。

截至本节，$94\le|m|\le8190$ 的头内自产源 Green 及其与低46、高无限窗的耦合尚未支付；后续第13节已用独立的 plateau 盒补齐中频及它与无限窗口的联合响应，低46反作用仍另列。R34 的端点 trace 传播上界没有直接替代源算子。外侧 cell0至11及真正强前缀的共同实面问题也未由本节完成。因此本节是第7节联合闭合的一个已实际支付块，未宣称完整头已经成立。

另外，[strong cut 条带工具](../computations/tail_strong_cut_strip_budget.py) 与
[完整 M16 cut 账本](../notes/2026-11-12-tail-r33-strong-m16-cut-strip.json)
把旧 stored 响应的全部非均值 $H/P$ 系数明确选作新实 cut 上的 dyadic 参考数据，得到
$R_{1/64}<0.0155699233513<1/64$，余量约 $5.51\times10^{-5}$。它只核销单个参考 cut 的域，完整实径向路径和强前缀尚须单独处理。

## 13. 有序局部核、胞元因果盒与全部高频联合响应

本节补齐中频源窗口，并将它与无限高频块联合。**低46场在本节保持固定，低场受到高场的反作用尚未支付。** 具体数据使用 R38 的 q003 真实参考和完整46维 plateau 盒；R39 的强 M20 参考必须另代入账本，不能继承这里的幅度常数。

R38 的整胞元角宽为 $\widetilde\tau_n=\max(2,1+(n-12)\log2/4)$。
将 (33.51) 中 $\overline X_n$ 换成其真实 $U_nX_n^{\rm ref}$，
其它源和连续条带构造不变。连续条带仍取第12节原来的较窄上限，
不是免费提升到 plateau 宽度。完整213胞元的区间账本给

$$
\gamma_\infty<3.172246\,10^{-13},\quad
A_*<3.775879\,10^{-16},\quad
\log_2 b_{D,\infty}<2234.432118.
\tag{33.65}
$$

全部212个正规范接口向外不增，且 $\tau+1/8\le\widetilde\tau_n$。
(33.52) 的逐胞元版本给低场 $L$ 在每个胞元较宽条带上的物理强范数至多1。
R38 的整个低盒满足 $|z|_1<2^{-2231}$，下面使用 $z_*=2^{-2231}$。

### 13.1 物理局部有序核

在一个胞元固定 $B=B_n$，令 $Y=(Bp,\kappa_\perp)$。齐次系统为

$$
Y_r=
\begin{pmatrix}
-1/r&imB/r\\
-im\lambda/B&-\lambda
\end{pmatrix}Y.
\tag{33.66}
$$

加权 $e^{\tau(r)|m|}$ 后，复 $\ell^1$ 对数范数是两列实对角元加非对角元模的最大值。由 (33.57) 中
$-\tau'\ge B/r+|\lambda|/B+\chi$，第一列的上界非正，第二列给

$$
\mu_1\le(1-|m|/B)_+(-\lambda)_+-|m|\chi.
\tag{33.67}
$$

保留 $\lambda<0$ 的实际位置，而舍去额外的非正
$-|m|\eta/8192$。在一个面板上，设 $\log w$ 降变差为 $T_-$，
$J_-\le\int\chi\,dr\le J_+$、$V_-\le V\le V_+$。
对频窗 $m_-\le|m|\le m_+$ 置 $q=(1-m_-/B)_+$。
入口的加权物理 $\ell^1$ 上界为 $R$、源强密度范数至多1时，

$$
\begin{aligned}
R_{\rm end}
&\le e^{qT_--m_-J_-}R+
\frac{kV_+e^{qT_-}}{m_-}(1-e^{-m_-J_+}),\\
\sup_{\rm panel}\frac{e^{\tau|m|}|Y|_1}{V}
&\le\frac{e^{qT_-}R+
kV_+e^{qT_-}(1-e^{-m_-J_+})/m_-}{V_-}.
\end{aligned}
\tag{33.68}
$$

证明是有序变分常数式加 $d=kV\chi$，以及
$\int_s^r\chi(u)e^{-m_-\int_u^r\chi}\,du
=(1-e^{-m_-\int_s^r\chi})/m_-$。
每个源只积其后的衰减，所以此界适用于任意连续源。
源取零、入口取1同时给齐次核。

这些面板只读取 R26 的同一真实函数。
$\log w$ 的导数为显式多项式加常数，完整临界根均由区间围住；
端点与临界点于是围住值域、总变差和降变差。
cell12至23 的真实公式

$$
dr=\frac{|dw|}{8(1+w^2)^{3/2}}+
\frac{\alpha}{1+w^2}\,dr_o
\tag{33.69}
$$

连同已付 $w<2^{-12}$、$\alpha>2$ 给

$$
\begin{aligned}
\int c\,dr&\le {\rm TV}(\log w)
+\frac{{\rm TV}(w)/8+\alpha\Delta r_o}{r_c},\\
\int c\,dr&\ge {\rm TV}(\log w)+\frac{\Delta r_o}{2R_*}.
\end{aligned}
\tag{33.70}
$$

再乘 (33.51) 给出的 $V/w$ 正值域并除以 $k$，得到 $J_\pm$。
按 $\log w$ 值域宽度不超过 $1/16$ 作 dyadic 细分，共30792面板，
没有径向 ODE 或新的基本矩阵积分。每个胞元分别计算零入口的源响应
和单位入口的齐次响应。例如 cell12 的94–96窗局部强范数源核
小于 $2^{-17.61697}$；其它胞元传来的齐次项仍须另加。

### 13.2 真实 canonical 矩阵与物理核的交集

令 $\nu_m=m^2(m^2-1)/12$、$Z=(Q,\Xi/\nu_m)$。
真实正比较整胞元矩阵 $C_n$ 的对角元至少1、其它元非负，
故它也控制任意有序子区间：补回被略去的正比较段只会逐项增大矩阵。
向外跨接口须乘 $J=\operatorname{diag}(1,1/\rho)$，
$\rho=2^{11/4}$。

对加权 canonical 入口 $z$，齐次端点上界为
$e^{-m_-\Delta\tau_n}C_nJz$，胞元内部则先用 $C_nJz$。
不能把整胞元的角宽下降施加到入口附近。源的准确注入为
$(0,t f/\nu_m)$，$t=r^4w/(\sqrt{12}\mu_n)$，故

$$
I_n\ge\int_{I_n}\frac{r^4w}{\sqrt{12}\mu_n}d(r)\,dr
\quad\Longrightarrow\quad
z_{\rm end}^{\rm source}\le C_n(0,I_n/\nu_{m_-})^T.
\tag{33.71}
$$

坐标变换为

$$
Q=\frac{p}{imr^3},\qquad
\frac{\Xi}{\nu_m}
=\frac{r^4w}{\sqrt{12}\mu_n\nu_m}
(\kappa_\perp+imp).
\tag{33.72}
$$

将 (33.68) 转为同一坐标后，可对源项和齐次项分别取逐分量最小值，
然后相加。这只是交叉使用两个有效上界，不改变实际解。
账本还保留物理 $e^{\tau|m|}(|Bp|+|\kappa_\perp|)$ 的端点上界，
跨接口只乘 $\max(1,B_{\rm new}/B_{\rm old})=1$，避免重复坐标转换损失。
两个物理分量各自的径向 supremum 由联合 supremum 的两倍控制，
安全因子2全程保留。

十一窗为94–96、98–104、106–112、114–128、130–192、
194–256、258–512、514–1024、1026–2048、
2050–4096、4098–8190。
前九窗的真 $C_n$ 覆盖全部213胞元；
末两窗的真矩阵覆盖 cell16至224，cell12至15完全用上述物理核，
不外推矩阵。

令 $\Gamma_{nj}$ 为 cell$j$ 上单位源到 cell$n$ 输出的强范数界。
先保留有序传播，再对十一窗取最大值。源向外传播，$j<n$ 时核为零，
其余给

$$
\|(\mathcal G_{\rm mid}f)|_{I_n}\|_{\mathcal X_n}
\le\sum_{j=n}^{224}\Gamma_{nj}\|f|_{I_j}\|_{\mathcal Y_j}.
\tag{33.73}
$$

这是真实的逐胞元源算子，不是端点 trace 传播界。

### 13.3 中频半径与距离权分别支付

固定低场 $L$，令中频未知量在 cell$n$ 的半径为 $R_n$。
在 source cell$j$，完整 $f(L)$ 的自产频窗密度至多
$16e^{-m_-(\widetilde\tau_j-\tau_{\rm inner,j})}$。
R18 的全部中频边界由 $2^{1967}z_*^2$ 乘回准确 $S_F$ 和角权，
再经同一有序核传播；没有把高 Cauchy 初值设零。
两项合为 $b_n$。由 (33.20)，

$$
\|f(L+H)-f(L)\|_{\mathcal Y_j}
\le64R_j(1+R_j).
\tag{33.74}
$$

因此足够支付三角二次不等式

$$
R_n>b_n+
64\sum_{j=n}^{224}\Gamma_{nj}R_j(1+R_j).
\tag{33.75}
$$

账本由 cell224 向外取每项较小正二次根的 $1.01$ 倍并核验严格包含。
再独立选正距离权 $W_n$，核销

$$
\max_n\frac{64\sum_{j=n}^{224}
\Gamma_{nj}(1+2R_j)W_j}{W_n}<\frac34.
\tag{33.76}
$$

较大的单向跨胞元增益由距离权承担，定义域半径无需等于距离权。
完整第二版实际得到

$$
\max_nR_n<2^{-58.64170118},\qquad
L_{\rm mid}<0.742577410,
\tag{33.77}
$$

且所有 mean 域 $A_n(1+R_n)<1/64$ 通过。
第一版少用 cell16至23 的两高窗真矩阵，其粗 majorant 在 cell12
二次判别式失败，局部对角数却仅 $0.00031838$；
该失败保留为界不足，未冒称真实方程障碍。
补入八胞元真实矩阵后 (33.75)–(33.76) 同时成立。

### 13.4 联立整个无限高频窗口

令 $H_\infty=P_{\ge8192}H_\infty$ 的全头强范数半径为 $h$。
每胞元完整高未知量至多 $R_j+h$。由
$\sum_m\sup_I a_m\le\sum_j\sum_m\sup_{I_j}a_m$，
全头源范数至多为213个局部源强范数之和。
因此以下有限组正不等式同时覆盖全部高频：

$$
\begin{aligned}
R_n&>b_n+64\sum_{j=n}^{224}\Gamma_{nj}
(R_j+h)(1+R_j+h),\\
h&>b_\infty+
16\cdot213\,\gamma_\infty e^{-8192/8}\\
&\hspace{22mm}
+64\gamma_\infty\sum_{j=12}^{224}(R_j+h)(1+R_j+h).
\end{aligned}
\tag{33.78}
$$

$b_\infty=b_{D,\infty}2^{1967}z_*^2$ 是完整真深图的无限高边界。
只有固定低场 $f(L)$ 使用已有的 $1/8$ 宽度余量；
两个未知高块始终在同一 $\tau(r)$ 空间，不额外丢解析宽度。

取无限块的距离权为1，中频权为 $W_n$。
中频输出的第$j$列为
$64\Gamma_{nj}(1+2(R_j+h))$，无限输入列为其对$j$求和；
无限输出行则用 $64\gamma_\infty(1+2(R_j+h))$ 及其和。
这些完整带权行和小于1即给同一 Banach 空间的收缩。
实际取 $h=2^{-90}$，完整214块账本给

$$
\begin{aligned}
\max_nR_n&<2^{-58.64170060},\\
\|\mathcal T_\infty\|&<2^{-94.15695099}<2^{-90},\\
L_{\rm middle\ rows}&<0.742577410,\\
L_{\rm infinite\ row}&<3.452574\,10^{-8}.
\end{aligned}
\tag{33.79}
$$

中频包含、无限包含、完整 mean 域以及两类带权导数行和五门全部通过。
故对固定在上述低盒内的低46场及其深高度 $z$，
**全部偶频率 $|m|\ge94$ 有唯一联合响应**，
满足完整高频非线性方程和真实 Cauchy 深边界。
其中无限点态乘法、完整 mean 和全部高源都保留。

本结论尚未说加入高响应之后低46方程仍成立。
真正全头闭合还需高场到低方程的输出、低变化到高响应的 Lipschitz 列
以及低盒原来的 map 余量。外 cell0至11和强前缀仍独立。

### 13.5 可复算材料

包络在 [plateau 密度账本](../notes/2026-11-12-tail-r33-plateau2-density-window.json.gz)。
局部工具是
[tail_r33_middle_local_scalar.py](../computations/tail_r33_middle_local_scalar.py)
及 [齐次适配器](../computations/tail_r33_middle_local_homogeneous.py)，
输出 [完整局部核](../notes/2026-11-12-tail-r33-plateau2-middle-local-homogeneous.json.gz)。
真实矩阵为 R34 原九窗包，以及
[cell24至224 两高窗](../notes/2026-11-12-closure-middle-high-subhead24.json.gz)、
[cell16至23 两高窗](../notes/2026-11-12-closure-middle-high-subhead16to23.json.gz)。

[tail_r33_middle_causal_box.py](../computations/tail_r33_middle_causal_box.py)
输出 [因果矩阵和中频盒](../notes/2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz)，
保存全部213胞元、逐对核、最坏频窗、真深边界、半径、权和输入 hash。
[tail_r33_high_joint_box.py](../computations/tail_r33_high_joint_box.py)
输出 [完整高频联合盒](../notes/2026-11-12-tail-r33-plateau2-high-joint-box.json)。
两项均正式退出0，无新非线性数值求解；比较使用192-bit Arb 的向外端点。

## 14. 较宽纯低源的端点权与低到高变化率

本节继续使用第13节同一 q003 plateau 低域、同一 $V,B,\tau$、同一真实核。
它加强固定低场的高响应和一条参数导数列，不宣称反向低反馈通过。

### 14.1 只对常 strip 纯低源使用的出口衰减

第13节任意源的 $\mathcal Y$ 权是随 $r$ 变化的 $\tau(r)$，
不能把整胞元角宽下降强加给胞元出口附近的源。
但固定低场 $L$ 在整胞元的常数角宽 $\widetilde\tau_j$ 上有强范数界，
其纯低非线性源满足
$\sum_m\sup_{I_j}e^{\widetilde\tau_j|m|}|f_m(L)|/d\le16$。
因此 raw canonical 源积分的出口可直接使用

$$
z_{{\rm end},j}^{\,f(L)}
\le16e^{-m_-(\widetilde\tau_j-\tau_{{\rm outer},j})}
C_j(0,I_j/\nu_{m_-})^T.
\tag{33.80}
$$

证明是在真实源 $f_m(L)$ 上先提出常数 $e^{-\widetilde\tau_j|m|}$，
执行 raw 有序积分，最后在输出乘 $e^{\tau_{\rm outer}|m|}$。
这一操作不涉及源位置的未知 $\tau(s)$。
胞元内部上界继续用 $\tau_{\rm inner}$，物理有序核继续用原有有效界；
在出口交叉取最小值。对 $f(L+H)-f(L)$ 不使用 (33.80)，
其全部核仍按同一窄条带。

加入真实 cell16至23 两高窗矩阵后，94–96 窗的全头纯低源响应上界
从 $2^{-71.9015}$ 改为 $2^{-95.0909}$。
用新的纯低残差向量重新支付 (33.78)，取 $h=2^{-110}$，给

$$
\max_nR_n<2^{-86.92442653},\qquad
\|\mathcal T_\infty\|<2^{-122.43102677}<2^{-110}.
\tag{33.81}
$$

定义域、完整 mean 和两类收缩门全部通过。
另把每个中频窗自己的核作用到完整高源界
$64(R_j+h)(1+R_j+h)$，加纯低源与真实深边界，
并和总半径 $R_n$ 取最小值，得到逐窗强范数包络。
例如 cell12 的94–96窗小于 $2^{-87.69026478}$。
这里一个窗的数值控制其全部正负模的强范数之和，
不是允许每个模式分别重复使用整个窗的预算。

### 14.2 完整低到高 Lipschitz 列

R38 的低距离为

$$
d_{\rm low}(\delta L)
=\max_n\frac{X_{\widetilde\tau_n}(\delta L|_{I_n})}
{W_n^{\rm low}X_n^{\rm ref}}.
\tag{33.82}
$$

$W_n^{\rm low}$ 是无量纲倍数，而 $V$ 用
$U_nX_n^{\rm ref}$ 构造，故
$\|\delta L\|_{\mathcal X_n,\widetilde\tau_n}
\le d_n\,d_{\rm low}$，$d_n=W_n^{\rm low}/U_n$。
不得把无量纲 $W_n^{\rm low}$ 再除一次 $X_n^{\rm ref}$。

先设 $d_{\rm low}=1$。在某胞元沿低方向取复圆
$|\zeta|\le1/d_n$，其低场 $L+\zeta\delta L$ 范数至多2。
实际全部胞元满足 $A_n(2+R_n+h)<1/64$，
因此完整 mean 根和点态源在这个复圆上全纯。
由 (33.19) 与 Cauchy，

$$
\|Df(L)\delta L\|_{\mathcal Y_n,\widetilde\tau_n}
\le64d_n.
\tag{33.83}
$$

这一纯低导数和 (33.80) 使用相同常 strip 的源算子。
再写 $t_n=R_n+h\le1$，
$F(\zeta)=f(L+H+\zeta\delta L)-f(L+\zeta\delta L)$。
(33.20) 在原窄 strip 上给
$\|F(\zeta)\|\le32(4+t_n)t_n\le160t_n$，
再次用 Cauchy 得

$$
\|[Df(L+H)-Df(L)]\delta L\|_{\mathcal Y_n,\tau}
\le160t_nd_n.
\tag{33.84}
$$

所以没有给未知 $H$ 添加额外解析宽度。
将 (33.83) 的较宽纯低列和 (33.84) 的窄带列分别送入真核，
就得到低变化对全部高方程的导数。

深图部分同样不能省略。R38 低 metric 的真实 far evaluation 界
记为 $e_D^{\rm low}$。第13节保存的高边界向量已含
$C_Dz_*^2$；将它乘
$4e_D^{\rm low}/z_*$ 即为 (33.35) 给出的
$\mathcal B D\mathcal D(z)\mathcal E\delta L$ 上界。
这个式子保留全部中频、无限高频和完整46维深输入。

为了避免用极小的源尺度距离权去衡量独立深边界变化，
仍取无限距离权为1，同时令中频距离权至少为 $R_n/h$，
再按完整高自导数正矩阵向外递推增大。
定义域半径不变，重新检查后的中频权行和小于
$0.742577410$，无限行和小于 $0.000240936$。
在这个明确的高距离和 (33.82) 的低距离下，实际给出

$$
\|\partial_L\mathcal T_{\rm high}\|
<2^{-83.56628443},\qquad
\|D H(L)\|
<2^{-81.60849500}.
\tag{33.85}
$$

第二式由第一式除以 $1-L_{\rm high}$，是有唯一高响应时的
Banach 参数估计。它是一条真实低到高列，不能用来替代
高到低列或原低盒的 map 余量。

### 14.3 数据与下一接口的准确范围

[常 strip 低源工具](../computations/tail_r33_middle_wide_low_density.py)
与 [完整纯低响应](../notes/2026-11-12-tail-r33-plateau2-middle-wide-low-density.json.gz)
给 (33.80)。
[重新支付联合盒](../computations/tail_r33_refined_high_joint_box.py)
生成 [含新距离权的高盒](../notes/2026-11-12-tail-r33-plateau2-high-joint-coupling-metric.json)。
[逐窗工具](../computations/tail_r33_high_band_envelopes.py)
输出 [213胞元十一窗包络](../notes/2026-11-12-tail-r33-plateau2-high-band-envelopes.json.gz)。
[低到高列工具](../computations/tail_r33_low_to_high_column.py)
输出 [完整导数账本](../notes/2026-11-12-tail-r33-plateau2-low-to-high-coupling-column.json)。
它们均正式退出0。

把窄高场直接投到原较宽低域的首个统一密度界没有通过；
最坏为 source cell12 对输出模式92，再到 target cell13。
这是具体范数上界失败，不是不存在性结论。
共同连续 $\tau$ 的低强空间及显式 far 参数变量是可继续核销的接口，
其核、定义域和收缩必须另算；不得把 R38/R39 的较宽盒结论免费搬过去。

## 15. 同一连续 strip 的真实面板位置与源材料

为了保留 Green 核的源、输出位置，本节给第13节所用**同一**
$\tau(r)$ 的逐面板区间，不另选条带。
cell12至23 使用 (33.69)，端口物理半径取同源真实列的已证区间；
所有源参数、$V,B,k$ 与第13节完全相同。

在源坐标 $x\in[u,v]$ 上，完整临界根给 $w$、$\log w$、
$w/\sqrt{1+w^2}$ 的值域和总变差。
若 $w_-\le w\le w_+$，未变形半径增量为 $\Delta r_o$，
则该面板物理宽度满足

$$
\frac18{\rm TV}\!\left(\frac w{\sqrt{1+w^2}}\right)
+\frac{\alpha\Delta r_o}{1+w_+^2}
\ \le\ \Delta r\ \le\
\frac18{\rm TV}\!\left(\frac w{\sqrt{1+w^2}}\right)
+\frac{\alpha\Delta r_o}{1+w_-^2}.
\tag{33.86}
$$

总变差本身也以区间解释。
从真实内端口正向累加这些正宽度，并从真实外端口反向减去剩余宽度，
两个区间的交集同时包含同一个实际面板端点。由此取得
$\ell=\int dr/r=\log(r_{\rm right}/r_{\rm left})$ 的严格正区间。
这一步只有正函数的上下界积分，不需要新的径向求积或 ODE。

在面板的 $r,w$ 区间上，(33.51) 的两项分别取正上下界，
给 $V$ 和 $A=V/w$。记
$T={\rm TV}(\log w)=\int|\lambda|\,dr$，
则正材料
$\mathfrak m=\int cV/w\,dr$
被 $(\ell+T)[A_-,A_+]$ 围住。
第13节连续 strip 的基准积分恰为

$$
\mathfrak b
=\left(B+\frac4M\right)\ell+
\left(\frac1B+\frac1M\right)T+\frac{\mathfrak m}{k},
\qquad M=8192.
\tag{33.87}
$$

设某面板端点之前的 $\mathfrak b$ 积分为 $P$、之后为 $Q$；
它们均严格非负且 $P+Q>0$。若已经围住各自上下端点，

$$
\frac{P_-}{P_-+Q_+}
\le\frac{P}{P+Q}\le
\frac{P_+}{P_++Q_-}.
\tag{33.88}
$$

于是
$\tau=\tau_{\rm inner}
-(\tau_{\rm inner}-\tau_{\rm outer})P/(P+Q)$
给准确的面板端点区间。整面板再利用 $\tau$ 向外单调下降。
这种前缀/余段比值保留了总量与局部量的关系，
没有将 $\tau_{\rm inner}$ 和 $\tau_{\rm outer}$ 任意放在同一源点。

canonical 源材料还可避免全胞元 $w_{\min}^{-2}$：
由 (33.51) 直接得到

$$
\frac{r^4Vw}{\sqrt{12}\mu}
=\overline X_n
\left(\frac{a_nr^7w}{\sqrt{12}\mu}
+\frac{\overline\mu_n}{\mu}\right).
\tag{33.89}
$$

把这个正函数的面板上下界乘 $\mathfrak m$，就围住
$\int r^4cV^2/(\sqrt{12}\mu)\,dr$，正是实际 canonical 源的注入积分。
完整 mean 仍属于源函数 $f$；此处只提供其已定义密度的几何材料。

工具 [tail_r33_continuous_strip_panels.py](../computations/tail_r33_continuous_strip_panels.py)
已正式退出0：12个胞元、30792面板、44.89秒。
[完整面板索引](../notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels-summary.json)
列出每胞元 gzip 文件和 SHA。
cell12 的 $\tau$ 端点最大区间宽小于 $5.833\,10^{-5}$，
cell13 小于 $1.069\,10^{-9}$，其余更窄。
各面板保存有理源坐标、$r,w,V,V/w$、材料与累计积分、
真实 $\tau$ 两端及 (33.89) 的源积分。
这支付共同条带的真实位置数据；其与带符号低46基本列组合后的
Green 算子及全频收缩仍须另行实际核算。

本轮持久检查点只收 cell012、cell013 两个完整包。
cell014 至 cell023 的完整面板仅在当前执行器，**未提交**；
若执行器丢失必须重算，不能假称它们仍已保全。
[完整重建记录](../notes/2026-11-12-tail-r33-continuous-strip-panel-checkpoint.md)
保存准确命令、依赖 SHA、正式退出0及全部十二包原始 SHA。

## 16. 保留频率与两种径向材料的完整源导数

本节保留真实 Darboux 源的二次主部，并给完整 mean 与点态分母的
明确余项界，用于共同连续 strip 的低高联合核算。
这是完整源的恒等分解，没有把主部单独代替原方程。
实际共同空间正矩阵的所有数值门仍需核算。

### 16.1. 完整恒等分解

使用 R33 的同一非均值归一状态与完整 mean 根，记

$$
a=V/w,\quad u_1=Bp/V,\quad u_2=\kappa_\perp/V,
\quad \beta=M/a,
$$

$$
T=u_1/B,\quad S=\partial_\theta u_1/B,\quad
A=\partial_\theta u_2-T,\quad C=u_2+S,
\quad Z=u_2+E S.
$$

这里 $B,V,w$ 只依赖径向坐标。定义两种非负材料

$$
d_1=\frac{V^2}{rw},\qquad
d_\lambda=\frac{|\lambda|V^2}{w},\qquad E=1+w^2.
$$

$d_1>0$；$\lambda=0$ 时第二项直接解释为零，不除以
$d_\lambda$。令 $\epsilon_\lambda=\operatorname{sgn}\lambda$。
将 $\mathsf P=aT$、$K=a(u_2+\beta)$ 逐项代入 R33 (33.17)，得

$$
f(u)=\mathscr P_\perp\frac{
E d_1 A^2+
\epsilon_\lambda d_\lambda
\bigl[(C+\beta)^2+w^2\{2(u_2+\beta)S+S^2-T^2\}\bigr]
}{1+a(Z+\beta)}.
\tag{33.90}
$$

因此二次主部是

$$
Q(u)=\mathscr P_\perp\left[
E d_1 A^2+
\epsilon_\lambda d_\lambda
\{C^2+w^2(2u_2S+S^2-T^2)\}\right].
\tag{33.91}
$$

完整剩余项 $R=f-Q$ 保留 $\beta$ 的全部频率依赖以及整个乘法逆。
下面界定的是这个实际剩余项，而非截断 Taylor 多项式。

### 16.2. 保留 $m=a+b$ 的二次导数

为免混淆本节把中心频率记为 $j$，变化频率记为 $b$，输出
$m=j+b$。固定径向点的行向量为

$$
A_j=(-1/B,ij),\quad C_j=(ij/B,1),\quad
S_j=(ij/B,0),\quad T_j=(1/B,0).
$$

对中心 $u$ 和变化 $v$，直接求导给

$$
\begin{aligned}
(DQ(u)v)_m={}&2E d_1\sum_{j+b=m}(A_j u_j)(A_b v_b)\\
&+2\epsilon_\lambda d_\lambda\sum_{j+b=m}
\bigl[(C_j u_j)(C_b v_b)\\
&\hspace{25mm}+w^2\{u_{2,j}(S_bv_b)+(S_ju_j)v_{2,b}
 +(S_ju_j)(S_bv_b)-(T_ju_j)(T_bv_b)\}\bigr].
\end{aligned}
\tag{33.92}
$$

所有偶数正负频率都按实际复 Fourier 约定保留。实函数的共轭
对称可以用来节省存储，但不删掉其强 Wiener 范数中的两份质量。

此式还有一个应在实际列中精确保留的相消。由 R33 (33.22)，

$$
u_{1,j}=\frac{iBj r^3Q_j}{V},\qquad
u_{2,j}=\frac{j^2r^3Q_j}{V}
+\frac{\sqrt{12}\mu\Xi_j}{r^4wV},
$$

所以

$$
C_j u_j=\frac{\sqrt{12}\mu\Xi_j}{r^4wV}.
\tag{33.93}
$$

这应从同一个真实 $\Xi$ 区间直接计算，避免先给两个大项分别
取绝对值而丢失相消。$A_j u_j$ 则等于
$ij[(j^2-1)r^3Q_j+\sqrt{12}\mu\Xi_j/(r^4w)]/V$。

### 16.3. 可直接接 Green 核的正列

在一个固定源面板 $J$，给出五个**各自已经先取径向 supremum**
的中心帽

$$
(\widehat A_j,\widehat C_j,\widehat U_{2,j},
\widehat S_j,\widehat T_j)
\ge\sup_{s\in J}e^{\tau(s)|j|}
(|A_ju_j|,|C_ju_j|,|u_{2,j}|,|S_ju_j|,|T_ju_j|).
$$

输入变量是

$$
x_{b,\ell}=(1+|b|)\sup_{s\in I_n}
e^{\tau(s)|b|}|v_{\ell,b}(s)|,
\qquad \sum_{b,\ell}x_{b,\ell}=\|v\|_{\mathcal X_n}.
$$

若 $j=m-b$ 在中心支持内，令

$$
\omega_{mjb}=\sup_{s\in J}
e^{\tau(s)(|m|-|j|-|b|)}\le1.
$$

括号中指数不正，故用已证的面板 $\tau$ 下端点求此上界。
两种材料的正系数列为

$$
L^{(1)}_{m;b,1}=\frac{2\omega_{mjb}}{1+|b|}
\frac{E\widehat A_j}{B},\qquad
L^{(1)}_{m;b,2}=\frac{2\omega_{mjb}}{1+|b|}
E|b|\widehat A_j,
\tag{33.94}
$$

$$
\begin{aligned}
L^{(\lambda)}_{m;b,1}
={}&\frac{2\omega_{mjb}}{1+|b|}
\left[\frac{|b|\widehat C_j}{B}
+w^2\left\{\frac{|b|(\widehat U_{2,j}+\widehat S_j)}{B}
+\frac{\widehat T_j}{B}\right\}\right],\\
L^{(\lambda)}_{m;b,2}
={}&\frac{2\omega_{mjb}}{1+|b|}
(\widehat C_j+w^2\widehat S_j).
\end{aligned}
\tag{33.95}
$$

$E,w^2$ 取该源面板的严格上界。把这两个矩阵与该面板的
$d_1,d_\lambda$ 真实 Green 材料积分组合，再按非负级数交换求和。
这保留了输出 $m$、输入 $b$ 和源面板；不会把点态
$\sum|f_m|$ 错当作 $\sum\sup|f_m|$。
若 Green 的输出已经使用 R33 的 $(1+|m|)$ 强范数，(33.94)、(33.95)
无需再乘一遍输出权。

若中心仅含 $0<|j|\le92$，则低输出 $0<|m|\le92$
的主部变化只有 $0<|b|\le184$。所以主部的高到低输入恰在
94至184之内，$|b|\ge186$ 只通过下面的完整余项进入低方程。
这是一项精确的频率支持结论，与幅度大小无关。

### 16.4. 完整 mean 与分母的有理余项界

使用 R33 同一强径向代数。设 $X=\|u\|_{\mathcal X}$，
$A_*X\le1/32$，其中 $A_*=\sup a$。由完整 mean 小根，

$$
\|\beta/a\|_{\mathcal A_0}\le4X^2.
$$

此外
$\|A\|,\|C\|,\|u_2\|,\|S\|,\|T\|\le X$，
$\|Z\|\le5X/4$。记 $D=1+a(Z+\beta)$，则

$$
\|D-1\|\le\frac54 A_*X+4(A_*X)^2
\le\frac{11}{8}A_*X<\frac12,
\quad \|D^{-1}\|\le2.
$$

按两种材料写 $R=\mathscr P_\perp(d_1R_1+
\epsilon_\lambda d_\lambda R_\lambda)$，其中

$$
R_1=E A^2(D^{-1}-1),
$$

$$
R_\lambda=
\{2\beta(C+w^2S)+\beta^2\}D^{-1}
+\{C^2+w^2(2u_2S+S^2-T^2)\}(D^{-1}-1).
$$

将所有含 $a$ 的项先精确提出一因子 $a(r)$，剩余项只含
非负次幂的径向中心系数；因此下列是先逐模取 supremum 的强界：

$$
\|R_1/a\|_{\mathcal A_0}
\le\frac{55}{16}X^3<4X^3,
$$

$$
\|R_\lambda/a\|_{\mathcal A_0}
\le\left[2\left(10+\frac12\right)+\frac{11}{2}\right]X^3
=\frac{53}{2}X^3<27X^3.
\tag{33.96}
$$

这里使用了
$\|C^2+w^2(2u_2S+S^2-T^2)\|\le2X^2$，
以及
$\|2\beta(C+w^2S)+\beta^2\|/a
\le(10+16/32)X^3$。故没有把 mean 的高次项省略。

若进一步 $A_*X\le1/64$，沿任一单位强范数方向取半径 $X$
的复 Cauchy 圆。圆内状态范数至多 $2X$，仍在 (33.96) 的域内。
全纯性来自同一完整 mean 小根与实际乘法逆。因此

$$
\|D(R_1/a)(u)\|\le32X^2,\qquad
\|D(R_\lambda/a)(u)\|\le216X^2.
\tag{33.97}
$$

这些余项包含全部 Fourier 频率。可把额外 $a(r)$ 保留在材料
积分中，或用已证的每胞元 $A_*$；不得把它从方程中删除。
$X=0$ 时导数为零，由解析延拓或直接二次消失得到。

### 16.5. 围绕已证辅助低解的完整共同空间方程

令 $L_{\rm aux}$ 为 R38 或 R39 已证的46模辅助非线性解；
其径向中心帽用真实线性列加已证 canonical 修正盒围住。
该辅助解满足完整低投影方程和真实低 far 图，虽尚无完整高场。
将全未知写为 $L_{\rm aux}+v+H$。低源差恒等为

$$
f(L_{\rm aux}+v+H)-f(L_{\rm aux})
=DQ(L_{\rm aux})(v+H)+Q(v+H)
+R(L_{\rm aux}+v+H)-R(L_{\rm aux}).
\tag{33.98}
$$

因此原辅助低方程的纯低残差精确消去；高方程仍保留已经支付的
$\mathscr P_{\rm high}f(L_{\rm aux})$。
第3节核算第一项，第4节给完整余项，而
$Q(v+H)$ 是显式二次项。独立 far 变量需同时保留
$D(z)-D(z_{\rm aux})$ 及 far evaluation 方程。
只有完整正矩阵的定义域包含和加权收缩实际通过后，才能宣称
这个共同空间中的全头闭合；本证明本身不代替那些数值门。

### 16.6 可执行接口

[逐频率正列工具](../computations/tail_r33_quadratic_source_columns.py)
的 `quadratic_mode_columns` 接收每个 signed 中心模式的五个面板帽，
输出每个输入频率和两个物理分量分别对应的两种材料正列。
帽使用复 Fourier 系数，余弦幅度必须先除以2；共轭两模均保留。
[有理常数账本](../notes/2026-11-12-tail-r33-two-material-fourier-derivative-ledger.json)
已正式退出0，核销本节十一条有理范围及有限卷积支持。
其中的接口示例不是实际中心或真实 Green 积分，不能冒充整个联合门。

### 16.7 固定频谱质量的径向中心分解

非零频率均满足 $|m|\ge2$，所以在单位物理强输入下，
$u_2,S,T$ 的算子范数分别不超过 $1/3,1/B,1/(3B)$。
$A$ 的算子范数不超过1，$C$ 不超过 $\max(1/3,1/B)\le1$。
因此第16.1节二次主部在两材料之和 $d=d_1+d_\lambda$ 的强源范数中满足

$$
\|Q(u)\|_{\mathcal Y}\le\frac32 X^2,\qquad
\|DQ(u)\|_{\mathcal X\to\mathcal Y}\le3X.
\tag{33.99}
$$

确实，径向项的二次系数至多 $E\le5/4<3/2$；
对数材料项的二次系数至多
$1+w^2(2/3+1+1/9)\le13/9<3/2$。
其对称双线性式直接给导数系数 $2\cdot13/9<3$，
无须额外 Cauchy 损失。

为了把真实径向中心小性放入核，写
$L_{\rm aux}=L_{2,\rm lin}+R_c$，前者是参考的实际线性模式2，
后者包括全部其余实际线性模式及完整非线性辅助修正。
在一个源胞元，记 $c_l$ 为 $R_c$ 每个 signed 模式的 canonical
强径向质量。它由先逐模取径向 supremum 定义，不随径向位置变化。
设 $\sum_lc_l\le R_{\rm can}$，令
$\eta_l=c_l/R_{\rm can}$；则 $\eta_l\ge0$、$\sum_l\eta_l\le1$。
若 $R_{\rm can}=0$，对应部分直接为零。

(33.52) 的逐模证明与 $|l|\ge2$ 给

$$
(1+|l|)e^{\tau(r)|l|}
\bigl(|R_{c,1,l}(r)|+|R_{c,2,l}(r)|\bigr)
\le\eta_l\,\varepsilon(r),\qquad
\varepsilon(r)=\frac{R_{\rm can}}{\overline X_n}
 e^{-2(\widetilde\tau_n-\tau(r))}.
\tag{33.100}
$$

若变化各模式、两分量的强质量之和为 $x_b$，
$DQ(R_c)$ 的输出源由固定卷积质量
$(\eta*x)_m$ 和径向材料 $3\varepsilon(r)d(r)$ 控制。
卷积质量之和至多 $\sum_bx_b$，而且独立于径向位置。
故可先把 $\varepsilon d$ 放进每个模式的真实 Green 积分，
再对输出模式取最大值；没有使用不合法的 $\sup/\sum$ 交换。

对主模式2，使用带 $e^{2\tau}$ 的完整实余弦/正弦幅度帽
$A_2,C_2,U_{2,2},S_2,T_2$。两个 signed 复半幅使共同源质量可取
$\nu_m=(x_{m-2}+x_{m+2})/2$，且 $\sum_m\nu_m\le\sum_bx_b$。
真实径向材料 profile 为

$$
\begin{aligned}
g_1&=2EA_2,\\
g_\lambda&=2\left[C_2\max(1/3,1/B)
+w^2\{U_{2,2}/B+S_2/3+S_2/B+T_2/(3B)\}\right].
\end{aligned}
\tag{33.101}
$$

因此完整低 Green 可分别保存四个正核：主核已含
$g_1d_1+g_\lambda d_\lambda$ 的全部导数系数；修正核只含
$\varepsilon d$、外乘3；二次核只含 $d$；余项核直接含 $a(r)d$、
外乘216。不能对主核再乘一次2，不能对已经含 $a(r)$ 的余项核
再重复乘胞元 $A_n$。

记各胞元中心强范数至多1、总新变化半径为 $t$，
且 $A_n(1+t)\le1/64$。由 (33.97)、(33.99) 沿线段积分，
未使用径向主 profile 的一般源变化也满足

$$
K_n(t)=3t+\frac32t^2+216A_n(t+t^2+t^3/3),\qquad
K_n'(t)=3(1+t)+216A_n(1+t)^2.
\tag{33.102}
$$

在低方程可把线性项分别替换为已付主核与3倍修正核；
$3t^2/2$ 乘二次核，$216(t+t^2+t^3/3)$ 乘含 $a$ 的余项核。
这些是完整源的共同空间正矩阵接口；实际所有胞元的核、far 行、
定义域和距离权仍须全部核算后才给全头闭合。

## 17. R39 实际 strong M20 域的完整高响应

第13、14节的同一证明现已实际用于 R39 的 strong M20 参考：
root q085 成功 M20 的全部20个切口高度在新 rational-tail 度量上重解，
node12 的20个高度均保留，校正仍含46个低自由度。
这不是后来的 q095 M24 新入口，也不是旧容量射线。

对 R39 已证较宽盒内的每个固定低场，重新以其
$U_nX_n^{\rm ref}$ 构造并核销实际 $V,k,\tau$。
浅12至23的30792个局部物理面板重算；其余仍使用同源真实正矩阵。
八个密度门、213胞元中频定义域与全部无限窗的五个联合门通过，得

$$
\max_n R_n<2^{-77.14232196},\qquad h=2^{-96},\qquad
\|\mathcal T_\infty\|<2^{-108.57290918}.
\tag{33.103}
$$

中频最大加权导数行和小于 $0.742627852$，无限行和小于
$0.000237326$。真实 far 球为 $|z|_{38}\le2^{-2224}$，
完整 mean 与 R18 的全部高 trace 仍进入同一联合方程。

在 R39 的原较宽低距离下，按第14.2节实际重算的低到高列给

$$
\|\partial_L\mathcal T_{\rm high}\|<2^{-72.53661320},\qquad
\|DH(L)\|<2^{-70.57854105}.
\tag{33.104}
$$

此列包含纯低宽带部分、高依赖窄带部分与完整 far 导数。
它不直接适用于把未知低校正改到共同窄 strip 后的新距离。

[强 M20 完整高盒](../notes/2026-11-12-tail-r33-strong-m20-high-joint-box.json)
和 [低到高列](../notes/2026-11-12-tail-r33-strong-m20-low-to-high-column.json)
保存全部定义域和行界。
[完整说明与运行事实](../notes/2026-11-12-tail-r33-strong-m20-high-response.md)
及 [紧凑恢复清单](../notes/2026-11-12-tail-r33-strong-m20-high-response-manifest.json)
保留源、依赖和重建命令；两份较大派生包明确未提交。
联合盒的终态 JSON 完整，而其最后一次会话退出码在上下文切换后
没有保留下来；本记录没有补写未取回的 exit0。新导数列已正式退出0。
本节仍只给固定低场的唯一完整高响应；反向低方程、外0至11胞元和
整个强闭面尚未因此完成。
