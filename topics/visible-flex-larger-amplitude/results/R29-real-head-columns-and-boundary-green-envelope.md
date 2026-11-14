# R29：真实头部的整胞元线性列与两端 Green 包络

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

**状态：已证明的可计算有限频窗工具。** 本文在 R26 定义的同一个实源上，把正标量积分转成准确线性流的区间包络，再把 R23 的完整非线性源预算送到固定浅端低高度的边值 Green 算子。整个推导控制胞元内每一点，未用端点小量代替整胞元范数。它不把有限频窗改名为全频无限尾，也不把有限 Galerkin worker 的压缩逆等同于完整点态方程。

## 1. 实对象、坐标与有限频窗

采用 [R26](R26-real-head-source-interval-and-port-coordinates.md) 的固定背景：所有保存的浅源参数、二进制 global warp alpha 和 factory 捕获的 `oldCut` 固定；$n\ge160$ 使用有理源参数 $65/64$。各指数、对数和积分取这些固定参数所定义的实函数。本文处理胞元 $n=12,\ldots,224$，内端 physical node225、外端 physical node12。真实外切 $R_{\rm out}$ 的另一个接口不因此被支付。

令 $m=2j$，$1\le j\le J\le46$，

$$
u_m=m^2-4,\qquad \nu_m=\frac{m^2(m^2-1)}{12},\qquad
\rho=2^{11/4},\qquad \mu_{n+1}=\mu_n/\rho.
\tag{1.1}
$$

$Q,\Xi_n$ 是 R23 的物理 canonical 坐标。每一胞元内的准确线性方程为

$$
\frac d{dr}\begin{pmatrix}Q\\\Xi_n\end{pmatrix}
=\begin{pmatrix}
u_m/r&\sqrt{12}\mu_n/(r^8w)\\
-\nu_m\sqrt{12}r^6w/\mu_n&-u_m/r
\end{pmatrix}
\begin{pmatrix}Q\\\Xi_n\end{pmatrix}.
\tag{1.2}
$$

向外由胞元 $n$ 进入 $n-1$ 时，$Q$ 连续而 $\Xi_{n-1}=\Xi_n/\rho$。因此

$$P:=\mu_n\Xi_n\tag{1.3}$$

是跨胞元连续的物理 momentum。特别地，node12 保存的 worker canonical 坐标使用 $\mu_{11}$；胞元12的边界值须乘 $\rho$，不可把二者直接混用。

R18 (9.4) 给每个准确深线性列在 node225 的起始直线

$$Q=1,\qquad \Xi=s_m+e_m,\qquad |e_m|\le\nu_m2^{-60},\tag{1.4}$$

其中 $s_m$ 是有理深源理想大特征值对应的 raw 斜率，$s_2=0$。线性方程逐模解耦，所以 (1.4) 可逐列使用；它不是把未知非线性深 trace 强行改成 Robin 等号。

## 2. 去掉对角项后的正标量核

作一个全局定义的对角规范

$$
Q=(r/r_c)^{u_m}q,\qquad
\Xi_n=(r/r_c)^{-u_m}\xi.
\tag{2.1}
$$

以任一递增材料坐标 $x$ 表示胞元的一段，则

$$q_x=a(x)\xi,\qquad \xi_x=-b(x)q,\qquad a,b>0,\tag{2.2}$$
$$
a=(r_c/r)^{2u_m}r^{-8}\sqrt{12}\mu_n\frac{r_x}{w},\qquad
b=(r/r_c)^{2u_m}r^6\nu_m\frac{\sqrt{12}}{\mu_n}r_xw.
\tag{2.3}
$$

这个变换的行列式为1。相应单胞元规范流也准确满足 $\det T=1$。

在 $12\le n\le158$，R26 已证明 cap 不起作用且 $\chi=1$，故

$$r_x=\frac{|w_x|}{8(1+w^2)^{3/2}}+
\alpha_{\rm warp}\frac{(r_o)_x}{1+w^2}.\tag{2.4}$$

把正的实际半径幂在一个闭 panel 上作区间包络，剩下四个正标量积分。自由项在未 warp 的源坐标中准确化为

$$
\sqrt{12}\mu_n\int\frac{(r_o)_x}{w}\,dx
=\int\ell\frac{r_o^8}{p_*}\,dx,
\qquad
\frac{\sqrt{12}}{\mu_n}\int(r_o)_xw\,dx
=\int\ell p_*r_o^{-6}\,dx.
\tag{2.5}
$$

这里 $\ell$ 是该段的 log 长度，$p_*$ 是九段源的正 profile。$1/(1+w^2)$ 用 R22 的 $W_n$ 包在 $[1/(1+W_n^2),1]$ 内。log 过渡的被积函数先除以左端正值，使规范后的被积函数在左端等于1，再用 Arb/Acb 作向外包围；原正因子保留在积分外。这避免绝对容差把极深层的正积分淹没。

曲率项使用准确原函数

$$
G_a(w)=\log w-\log(1+\sqrt{1+w^2})+
\frac1{\sqrt{1+w^2}},\qquad
G_b(w)=\frac{w^2}{\sqrt{1+w^2}(1+\sqrt{1+w^2})},
\tag{2.6}
$$

其导数分别为 $1/[w(1+w^2)^{3/2}]$ 和 $w/(1+w^2)^{3/2}$。所以两个曲率正积分准确等于 $\sqrt{12}\mu_n\operatorname{TV}(G_a)/8$ 与 $\sqrt{12}\operatorname{TV}(G_b)/(8\mu_n)$。R26 已给过渡段 $w_x=0$ 的全部根；按这些根分段取总变差，不需采样极值。

在胞元159受保护的内 collar，只用实际自由系数位于 $[1/(1+W_n^2),\alpha_{\rm warp}]$、曲率系数位于零与完整曲率项之间的严格范围；实际半径用 R22 的整个159以后尾宽包围。$n\ge160$ 的新源未 warp，$r=r_o$，仅保留自由项。三个区段都来自同一个固定背景，未在159处切换成另一条浅源。

由此得到每个 panel 上准确的

$$A=\int a\,dx\in[A_-,A_+],\qquad B=\int b\,dx\in[B_-,B_+].\tag{2.7}$$

## 3. 不因巨大 shear 失效的 Peano–Baker 包围

设 $p=A_+B_+<1$。在有序积分展开中，一个含 $k$ 个 $a$ 因子和 $l$ 个 $b$ 因子的项，其绝对值不超过

$$\frac{A_+^kB_+^l}{k!l!}.\tag{3.1}$$

证明是把保持各自 $a$ 时间和 $b$ 时间有序的区域放大到两个独立单纯形的积；正性允许放大积分区域。实际交替次序的区域只是其中的子集。

记

$$E_p=\frac{p^2}{4(1-p)},\qquad O_p=\frac{p^2}{12(1-p)}.\tag{3.2}$$

由于矩阵 (2.2) 的非零项交替出现且符号交替，准确流 $T$ 满足逐项区间

$$
T_{11},T_{22}\in[1-p-E_p,1+E_p],
\tag{3.3}
$$
$$
T_{12}\in[A_--A_+(p/2+O_p),\ A_++A_+O_p],
\tag{3.4}
$$
$$
T_{21}\in[-B_+-B_+O_p,\ -B_-+B_+(p/2+O_p)].
\tag{3.5}
$$

例如第三阶 $12$ 项绝对值至多 $A_+p/2$，第五阶以后之和至多 $A_+O_p$；第四阶以后对角余项之和至多 $E_p$。这逐项证明了 (3.3)–(3.5)，没有以小的 $p$ 偷换小的 $A_++B_+$。

当 $p\le2^{-20}$ 时，完整 panel 流、任意子区间流及它们的逆，绝对值都逐项不超过

$$
M=\begin{pmatrix}
1+E_p&A_+(1+O_p)\\
B_+(1+O_p)&1+E_p
\end{pmatrix}.
\tag{3.6}
$$

对于逆，用准确恒等式 $T^{-1}=\left(\begin{smallmatrix}T_{22}&-T_{12}\\-T_{21}&T_{11}\end{smallmatrix}\right)$。对于子区间，将其两个正积分缩小到 $A_+,B_+$；(3.6) 仍适用。对角下界不会产生更大的绝对值，因为 $p<1$。

把一个胞元的 panel 按向外次序编号 $1,\ldots,N$。前向全程的正 majorant 为 $M_N\cdots M_1$，反向为 $M_1\cdots M_N$。每个 $M_i\ge I$ 逐项成立，故任意连续子乘积也被相应全程乘积逐项支配。这同时支付了整胞元任意起止点的 Cauchy 界和单列在胞元内的 supremum，而非只支付节点。

## 4. 保留共同幅度的区间传播

单纯对两个巨大坐标独立作区间箱传播，可能丢失共同幅度的相关性，使实际非零的高度列包围含零。本文的可执行改进保持

$$v=c(1,s)\quad\hbox{或}\quad v=c(s,1).\tag{4.1}$$

每一步用 (3.3)–(3.5) 包围 $T(1,s)$ 或 $T(s,1)$，选取一个整个区间不含零的坐标作新 pivot，把其区间乘到 $c$。新方向是一个 Möbius 商。因为准确 $\det T=1$，只要分母不为零，它对原 $s$ 的导数符号固定：新旧 pivot 相同时为正，不同时为负，绝对值为分母平方的倒数。故只需在旧 $s$ 区间的两个端点分别作带系数区间的商，再取 union，就包含整个准确方向像。这里使用了准确流的行列式恒等式，不要求包围矩阵中每一个独立选取的矩阵也行列式1。

这个单调 Möbius 包围避免把同一方向变量在分子分母中的相关性再次丢掉。它没有取中点或凭经验重置误差；每个缩小都有上述确定的单调性证明。只要 normalized pivot 区间不含零，公共幅度与新方向的区间对就继续包含原来的每条准确列。

跨胞元的 $\Xi$ 规范变换同样准确乘到相应分量。需要 whole-cell supremum 时，先由 (4.1) 得到两个坐标的向外绝对值，再作用 (3.6) 和 (2.1) 的实际半径区间。因此保留相关性的传播不会削弱整胞元 majorant 的合法性。

若某一步两个候选 pivot 区间都含零，或者浅 cut 的 $Q$ 区间含零，程序必须报未证，不能把它解释成真实图有零点，也不能继续除法。增加精度、细分或改进包围之后才能使用高度图。

## 5. 准确线性参考的整胞元 R23 输入

设由 (1.4) 传播得到的准确线性列为 $\phi_m$，且已证明

$$0\notin[\phi_{Q,m}(r_{12})].\tag{5.1}$$

给定有限个明确实数 $h_m$，准确线性参考为

$$Z_m^{\rm ref}(r)=\frac{h_m}{\phi_{Q,m}(r_{12})}\phi_m(r).\tag{5.2}$$

输入也可以是保存的 binary64 数按其准确 dyadic 值读取；这只定义一个参考边界坐标，不把它当作数值解真误差区间。未选择的参考系数可明确置零，但真实非线性解相应系数没有因此被断言为零。

由各 panel 的实际路径 majorant 得到 $q_{m,n},x_{m,n}$，分别是参考在胞元 $I_n$ 内 $|Q_m|,|\Xi_m|$ 的上界。于是

$$
x_n=\sum_{m\in\mathcal L}e^{\tau m}
\big((1+m)^3q_{m,n}+(1+m)x_{m,n}\big)
\tag{5.3}
$$

是 R23 强范数的合法上界。求和在逐模、逐分量的 supremum 之后，和 R23 (1.4) 完全相同。若 $x_n\le\mathfrak r_n$，完整 mean root 及完整点态非线性源均存在，并有

$$F_n=B_nx_n^2,\qquad H_nx_n^2\tag{5.4}$$

分别控制完整全频源的 $L^1_r\mathcal W_\tau$ 范数和 mean 高度增量。即使线性参考只有有限 Fourier 项，(5.4) 仍包含倒数和完整 mean 产生的全部频率；没有把非线性源截成同一有限多项式。

## 6. 固定浅高度的 Wronskian Green 公式

固定单频 $m$。另取准确齐次解 $\psi_m$，在浅 cut 的胞元12规范中满足

$$\psi_Q(r_{12})=0,\qquad \psi_{\Xi,12}(r_{12})=1.\tag{6.1}$$

在连续坐标 $(Q,P)$ 中，(1.2) 的矩阵迹为零，所以

$$
W_m=\phi_Q\psi_P-\phi_P\psi_Q
=\mu_{12}\phi_Q(r_{12})\ne0
\tag{6.2}
$$

在整个头部恒定。局部 source 为 $(0,f_m)$，此处 $f_m$ 指 $\Xi_n$ 方程中的 source；在 $(Q,P)$ 中 source 是 $(0,\mu_n f_m)$。

要求内端变化位于 $\phi_m$ 的直线上，外端变化满足 $Q(r_{12})=0$。变参数公式给

$$
(\mathcal G_m f)(r)=
\phi_m(r)\int_r^{r_{12}}
\frac{\psi_Q(s)\mu(s)f_m(s)}{W_m}\,ds
+\psi_m(r)\int_{r_{225}}^r
\frac{\phi_Q(s)\mu(s)f_m(s)}{W_m}\,ds.
\tag{6.3}
$$

向量 $\phi_m(r),\psi_m(r)$ 在输出处使用当地 $\Xi$ 规范。把两个积分微分，边界 jump 恰为 $(0,f_m)$；内端第二项为零，外端第一项为零且 $\psi_Q=0$。因此 (6.3) 逐项验证了方程和两端条件。非零 Wronskian 同时给唯一性。

公式 (6.3) 直接使用互补边界解，不作两个巨大的初值传播项之差。巨大的 $\phi_Q(r_{12})$ 出现在分母中，正是边值问题对不稳定增长的抵消；不能先把它丢掉，再以全 Cauchy 范数代替 Green 范数。

## 7. 从全源积分到整胞元强范数的有限窗算子界

把 $\phi$ 的整胞元上界除以 $|\phi_Q(r_{12})|$ 的严格下界，记为 $\Phi^Q_{m,k},\Phi^\Xi_{m,k}$。从 (6.1) 用准确逆流向内传播 $\psi$，结合 §3 的反向 majorant，得到 $\Psi^Q_{m,k},\Psi^\Xi_{m,k}$。定义

$$\Phi^X_{m,k}=(1+m)^3\Phi^Q_{m,k}+(1+m)\Phi^\Xi_{m,k},$$
$$\Psi^X_{m,k}=(1+m)^3\Psi^Q_{m,k}+(1+m)\Psi^\Xi_{m,k}.$$

胞元下标越大越靠内。对 $k\ne n$，可以取

$$
\gamma^{(m)}_{kn}=\frac{\mu_n}{\mu_{12}}
\begin{cases}
\Phi^X_{m,k}\Psi^Q_{m,n},&k>n,\\
\Psi^X_{m,k}\Phi^Q_{m,n},&k<n.
\end{cases}
\tag{7.1}
$$

对同胞元，两个积分分支会随 $r,s$ 改变，故分别最大化两个输出分量：

$$
\gamma^{(m)}_{nn}=\frac{\mu_n}{\mu_{12}}
\left[(1+m)^3\Phi^Q_{m,n}\Psi^Q_{m,n}
+(1+m)\max\{\Phi^\Xi_{m,n}\Psi^Q_{m,n},
\Psi^\Xi_{m,n}\Phi^Q_{m,n}\}\right].
\tag{7.2}
$$

用两个加权分量之和的最大值替代 (7.2) 一般不足以控制 R23 的先取 supremum 后求和的范数。

令 $\Gamma_{kn}\ge\sup_{m\in\mathcal L}\gamma^{(m)}_{kn}$。因为 Fourier 算子对角，指数权在同一模的输入输出处准确抵消，(6.3) 和 Tonelli 定理给

$$
\boxed{X_k(\mathcal G P_{\mathcal L} f)
\le\sum_n\Gamma_{kn}\int_{I_n}\|f(s)\|_{\tau,0}\,ds.}
\tag{7.3}
$$

这里取各模块范数的 supremum 后乘统一的输入 $\ell^1$ 总质量，不再加一个 $J$ 倍。程序把每个正 majorant 向上舍入到二进制幂，再逐项取最大值；准确 mantissa/exponent 决定舍入，不用浮点 log 决定界。

特别地，将 (5.4) 的**完整源**作为输入有

$$Y_k:=\sum_n\Gamma_{kn}B_nx_n^2.\tag{7.4}$$

它支付完整源低频投影的真实头部响应，不是仅比较浅端两个 slope。高于 $\mathcal L$ 的 source 仍需另一个全频 Green/传播估计。

## 8. 一个精确但明确限定的收缩推论

取空间范数 $\|V\|_*:=\max_n X_n(V)/x_n$，其中 $x_n>0$。若 $2x_n\le\mathfrak r_n$，且

$$\eta:=\max_kY_k/x_k<1/8,\tag{8.1}$$

则如下辅助有限窗边值问题存在唯一的局部解：保留 $\mathcal L$ 内非均值变量，对完整点态非线性向量场在输出处投影到 $\mathcal L$，每一步仍使用完整 mean root；内端使用准确**线性**深直线，外端固定 (5.2) 的高度。

证明：在 $Z^{\rm ref}$ 周围取 $\|V\|_*\le1$，则状态各胞元范数至多 $2x_n$。由 R23 和 (7.3)，映射 $V\mapsto\mathcal G P_{\mathcal L}\mathcal N(Z^{\rm ref}+V)$ 的范数不超过 $4\eta<1$。对两输入，R23 (1.7) 给 source 差至多 $8B_nx_n^2\|V-\widetilde V\|_*$，所以 Lipschitz 常数至多 $8\eta<1$。Banach 不动点定理给结论；积分方程再给与源正则性相符的径向解，mean 高度统一积分而不逐胞元重置。

这是完整证明的辅助命题。它既不是 original worker 所用的压缩 Galerkin 逆问题，也没有把 R18 的非线性深图换成线性图后仍宣称全频精确尾。要用于主问题，还须把真实非线性深图及窗外响应作为同一个耦合映射的输入，并允许最终高频浅 cut 高度改变。

## 9. 可复算实现与准确边界

实现入口为：

- `computations/closure_real_head_source_enclosure.py`：R26 的同函数实源及闭 panel 半径包围。
- `computations/closure_real_linear_head_enclosure.py`：正核、Peano–Baker panel、独立真实低频列、整胞元参考和完整源预算。
- `computations/closure_projective_interval_column.py`：§4 的公共幅度区间列。
- `computations/closure_real_head_green_enclosure.py`：准确 Wronskian 归一、反向列及 (7.3)–(8.1)。

所有输入 binary64 参数先转成准确分数，所有区间输出保存向外端点的 dyadic mantissa/exponent。显示用的小数不是证书本体。范数上界字段表示一个已计算正 majorant 的包围，取其 upper endpoint 才是所断言的上界，不能把该区间当作未知真实范数的双侧包围。

单次运行是否实际通过 (5.1)、R23 半径和 (8.1)，由对应输出给出；未通过时不援引上述条件推论。实现中逐模包含46个列的运行，才可称46模已覆盖。旧 M8 运行或补零的参考向量都不支付其余38个列。所有脚本、源输入及分组输出的 hash 随结果保存。

本文控制的是 node225 到 node12。它不支付 node12 到物理外切的源积分/非线性误差、前缀实际匹配、闭曲面全时嵌入或 reach，也不把这些剩余条件作为停工理由。
