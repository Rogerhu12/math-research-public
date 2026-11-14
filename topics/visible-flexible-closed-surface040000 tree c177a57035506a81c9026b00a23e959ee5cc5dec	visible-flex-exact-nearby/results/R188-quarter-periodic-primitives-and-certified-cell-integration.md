# R188：直接位置表示的四分之一周期 primitive、完整列与连续积分余项

**状态：已证明。** 本结果消费 [R187](R187-closed-unit-angular-tangents-and-direct-position-metric.md) 的完整角函数，给出准确 quarter primitive、零均值/Fubini、全残差和 Gauss–Newton 列的四折恒等式，以及可独立包围准确位置图的 cell 积分余项。它不将有限 DFT、数值积分的角导数或 sampled metric 宣称为准确完整切向量。本文不证明任何当前非圆初值已满足剩余等距或几何要求。

## 1. 假设与完整对称性

令 $s$ 属于一个明确物理径向区间，$\Theta=u+\vartheta$，其中 $\vartheta(s,u)$ 与 $\Phi(s,u)$ 均关于 $u$ 为奇函数，并具有周期 $\pi$。定义

$$
T=(-\sin\Theta\cos\Phi,\ \cos\Theta\cos\Phi,\ \sin\Phi).
$$

这些是完整三角复合，不截断其产生的 Fourier 高频。对任意参数，假设相同对称性作为函数恒等式保持。以下用到的径向或参数导数连续时，允许逐项微分这些恒等式；不要求额外的径向三阶导数。

记 $A=\pi/2$，以及正交反射

$$
D_x=\operatorname{diag}(-1,1,1),\qquad
D_y=\operatorname{diag}(1,-1,1),\qquad
S=\operatorname{diag}(-1,-1,1).
$$

奇性和 $\pi$ 周期给出

$$
T(-u)=-D_yT(u),\qquad
T(\pi-u)=-D_xT(u),\qquad
T(u+\pi)=ST(u).
\tag{1}
$$

特别地，$T_x$ 是奇且 $\pi$ 反周期，$T_y$ 是偶且 $\pi$ 反周期，$T_z$ 是奇且 $\pi$ 周期。其完整 $2\pi$ 平均准确为零。相同分量规律适用于 $T_s,T_{ss},T_p,T_{sp}$，以及任何确实存在且在同一物理坐标下取的参数列。不能把会破坏对称性的任意外加角列混入本结论。

## 2. 准确 quarter primitive

对 $0\le u\le A$，定义

$$
Y_x(u)=-\int_u^A T_x(v)\,dv,\qquad
Y_y(u)=\int_0^u T_y(v)\,dv,
\tag{2}
$$

$$
Y_z(u)=\int_0^u T_z(v)\,dv
-\frac1A\int_0^A(A-v)T_z(v)\,dv.
\tag{3}
$$

将它们按

$$
Y(-u)=D_yY(u),\qquad
Y(\pi-u)=D_xY(u),\qquad
Y(u+\pi)=SY(u)
\tag{4}
$$

延拓。

**定理。** 式 (2)–(4) 给出的 $Y$ 恰是 R187 唯一零均值周期 primitive $\mathcal PT$；特别地，$Y_u=T$、完整周期闭合及完整均值零均为准确恒等式。

**证明。** 在 quarter 内对 (2)–(3) 微分即得 $Y_u=T$。由 (1)，$\vartheta$ 和 $\Phi$ 在 $u=0,A$ 为零，因而 $T_x(0)=0$、$T_y(A)=T_z(0)=T_z(A)=0$。式 (2) 还给出 $Y_x(A)=0$、$Y_y(0)=0$，这与 (4) 的反射接头相容。对角函数的连续导数微分 (1)，可得到每个实际存在阶数所需的单侧接头恒等式；因此延拓具有原函数允许的相应正则性，且导数为完整 $T$。

$Y_x,Y_y$ 的 $\pi$ 反周期使其完整平均为零。对 $Y_z$，Fubini 给出

$$
\int_0^A\left(\int_0^u T_z(v)\,dv\right)du
=\int_0^A(A-v)T_z(v)\,dv,
$$

故由 (3) 有 $\int_0^A Y_z=0$。式 (4) 中 $Y_z$ 在全部四个 quarter 的积分相同，完整均值也为零。两个零均值周期 primitive 的差是零均值常向量，只能为零，遂与 R187 定义一致。∎

这不要求 quarter 上 $\int_0^A T_z=0$；通常该积分非零。不能遗漏 (3) 的加权矩，也不能以离散节点均值替代它。

## 3. 径向导数和全部参数列

上述积分区间在物理角 $u$ 下固定，$A=\pi/2$ 与所有状态参数无关。对连续的所需导数，用紧域上的微分积分交换可得

$$
Y_s=\mathcal P T_s,\qquad
Y_{ss}=\mathcal P T_{ss},\qquad
Y_p=\mathcal P T_p,\qquad
Y_{sp}=\mathcal P T_{sp}.
\tag{5}
$$

每个右端都逐分量使用同一组式 (2)–(3)，包括竖向加权矩。不能只对 raw Fourier 系数微分而漏掉 lifting、物理 profile 或已参数化端口的变化。

以 $X=aY+Ze_z$ 表示真实位置，则

$$
\begin{aligned}
X_s&=a_sY+aY_s+Z_se_z,\\
X_u&=aT,\\
X_{ss}&=a_{ss}Y+2a_sY_s+aY_{ss}+Z_{ss}e_z,\\
X_{su}&=a_sT+aT_s,\qquad X_{uu}=aT_u.
\end{aligned}
\tag{6}
$$

参数列由这些完整公式的乘积法则给出。例如

$$
(X_s)_p=(a_s)_pY+a_sY_p+a_pY_s+aY_{sp}+(Z_s)_pe_z.
\tag{7}
$$

这里只需 $T,T_s,T_{ss},T_u$ 与实际使用的参数混合列；不会因积分消费者引入完整曲面必须 $C^3$ 的新条件。

若采用随参数变化的角 chart，必须先转换为固定物理 $u$ 的导数，再使用 (5)。若仅为求值使用 $u=U(s,\xi)$，则例如

$$
(\partial_sY)_{\xi}=Y_s+T\,U_s,\qquad
Y_\xi=T\,U_\xi.
$$

不能把沿固定 $\xi$ 的导数误代为 (6) 的物理 $Y_s$。R187 当前直接表示以物理 $u$ 为定义，不需要旧 moving atlas 的反解。

## 4. 真实残差、全 Jacobian 与四折目标

记 $V=X_s$。R187 的剩余实际归一残差为

$$
r_E=|V|^2-1,\qquad r_F=V\cdot T.
$$

由 (4)，$X(-u)=D_yX(u)$、$X(\pi-u)=D_xX(u)$，轴向中心项保持相同。故 $V$ 在反射下无额外负号，而 $T$ 有一个负号，于是

$$
r_E(-u)=r_E(u),\quad r_E(\pi-u)=r_E(u),
$$

$$
r_F(-u)=-r_F(u),\quad r_F(\pi-u)=-r_F(u).
\tag{8}
$$

二者在 $u\mapsto u+\pi$ 下均周期。所有保持对称的参数列 $J_E,J_F$ 具有对应相同符号。因此

$$
\rho=r_E^2+2r_F^2
$$

在四个 quarter 反射下不变，且

$$
\int_0^{2\pi}\rho\,du=4\int_0^A\rho\,du.
\tag{9}
$$

同样有

$$
\int_0^{2\pi}(J_E^\top J_E+2J_F^\top J_F)\,du
=4\int_0^A(J_E^\top J_E+2J_F^\top J_F)\,du,
\tag{10}
$$

以及梯度中的 $\int(J_E^\top r_E+2J_F^\top r_F)$ 四折恒等式。式 (10) 保全部状态/参数交叉项，不是只保对角或范数。

### 4.1 完整周期梯形与 quarter 端点半权

取整数 $m\ge1$、$h=A/m$。完整周期 $4m$ 个点为 $u_j=jh$，$j=0,\ldots,4m-1$。由 (8)，

$$
\sum_{j=0}^{4m-1}\rho(u_j)
=4\left[\frac12\rho(0)
+\sum_{j=1}^{m-1}\rho(jh)
+\frac12\rho(A)\right].
\tag{11}
$$

证明仅需按反射轨道计数：两个轴端点轨道各含两个点，其余 quarter 内点各有四个对应点。式 (11) 对完整梯度和 normal 的逐项积也成立。

若原目标是 full mean $(4m)^{-1}\sum\rho$，quarter 残差应按 $w_j/m$ 加权，其中 $w_0=w_m=1/2$，内部 $w_j=1$；其 E 行乘 $\sqrt{w_j/m}$、F 行乘 $\sqrt{2w_j/m}$。若原目标是未归一求和或积分，应分别保相应的 $4w_j$ 或 $4hw_j$，不能遗漏四倍因子或端点半权。

因此 $m=16$ 的 17 个 quarter 节点与 64 个完整周期节点给同一准确有限目标及相同完整 normal/gradient。浮点求和次序或旧独立求值的舍入不必逐位相同；本定理没有宣称已经运行的旧 full-grid 包被逐字恢复。

### 4.2 连续相对度量与浸入

准确角向等距由 $|T|=1$ 给出，故相对误差矩阵完整为

$$
\begin{pmatrix}r_E&r_F\\r_F&0\end{pmatrix},
\quad
\|B\|_{\rm op}
=\frac{|r_E|}{2}+\sqrt{\frac{r_E^2}{4}+r_F^2}.
\tag{12}
$$

对连续盒严格包围 $V,T$ 即可消费 (12)；不需要再把准确零的 G 残差换成区间依赖误差。Gram 行列式为 $a^2(1+r_E-r_F^2)$。数值节点上的小值不替代全域 (12) 的上界或该行列式的连续正下界。

## 5. cell 累计和 Fubini 的先合系数实现

令 $t=u/A\in[0,1]$，查询点为 $t_0$。把角 partition 在 $t_0$ 处分开。对每个 cell $[l,r]$，所有需要积分的 channel 都表示完整 $W(s,t)=V(s,At)$，其中 $V$ 可以是 $T,T_s,T_{ss}$ 或任意所需参数列。

在式 (2)–(3) 中，一个 cell 对 $Y/A$ 的权为：

| 分量 | cell 在 $t_0$ 左侧 | cell 在 $t_0$ 右侧 |
|---|---|---|
| x | 0 | $-1$ |
| y | 1 | 0 |
| z | $t$ | $t-1$ |

尤其竖向 primitive 可以直接写成

$$
\frac{Y_z(u)}A
=\int_0^{t_0}t\,W_z(s,t)\,dt
+\int_{t_0}^1(t-1)W_z(s,t)\,dt.
\tag{13}
$$

它与 (3) 是准确同一函数。先合并这些权重，再包 cell 积分，可避免“两个较大 primitive/mean 区间相减”造成不必要膨胀。没有删去 Fubini 矩；矩已完整包含在 (13) 中。

可以缓存每个准确 cell 的完整积分和第一矩，随后以同一来源做 prefix/suffix 累计；也可以直接按上表逐 cell 累加。两种方法必须绑定相同实际 $V$、径向盒、参数值、物理角和完整 cell 分区。不能因径向点相同而借用另一参数或另一角 chart 的缓存。

## 6. 严格 Taylor cell 积分和角余项

本节给出一个不依赖未知 Gauss 求积误差估计的完整条件。令 $c=(l+r)/2$、$h=(r-l)/2$。假设已经严格得到 Taylor 系数盒 $C_k$ 和全 cell 余项上界 $M_n$，使对全部查询径向参数与 $t\in[l,r]$，

$$
W(s,t)=\sum_{k=0}^{n-1}c_k(s)(t-c)^k+R_n(s,t),
\quad c_k(s)\in C_k,\quad
|R_n(s,t)|\le M_n|t-c|^n.
\tag{14}
$$

分量或各参数列可以有不同的 $M_n$。例如用完整物理角导数界可取

$$
M_n=\frac{A^n}{n!}
\sup_{s,\ u\in[Al,Ar]}|\partial_u^nV(s,u)|.
\tag{15}
$$

这是角向余项条件；不要求存在径向三阶导数。若某角接头缺乏所选高阶角导数，应在真实片界分开，或使用该处确实有效的较低阶条件/自然区间积分；不能把高阶假设扩展到未付片界。

令 cell 权写成 $w(t)=\alpha+\beta(t-c)$。Taylor 多项式的准确积分为

$$
I_{\rm poly}
=\alpha\sum_{\substack{0\le k<n\\k\ {\rm even}}}
 C_k\frac{2h^{k+1}}{k+1}
+\beta\sum_{\substack{0\le k<n\\k\ {\rm odd}}}
 C_k\frac{2h^{k+2}}{k+2}.
\tag{16}
$$

对第 5 节的所有非零权，$w$ 在该 cell 上不换号，所以

$$
\left|\int_l^r w(t)R_n(s,t)\,dt\right|
\le |\alpha|M_n\frac{2h^{n+1}}{n+1}.
\tag{17}
$$

**证明。** 由符号固定，$|w|=|\alpha|+\operatorname{sgn}(\alpha)\beta(t-c)$。将 (14) 的绝对余项代入，对称区间上奇项积分为零，即得 (17)；若 $\alpha=0$ 且不换号，则该线性权恒零。式 (16) 由各幂的准确积分得到。∎

将 (16) 扩张 (17)，再乘准确 $A$ 并对完整分区求和，就是 (2)–(3) 的严格 primitive 包。由同一公式逐 channel 消费 (5)，即可得到实际位置所需全部两jet和参数列。准确性来自完整积分及显式余项，不来自 Gauss8/12 两次读数接近。

### 6.1 正大小角盒

若需 $u\in[u_-,u_+]$ 的完整盒，选择其中准确中心 $u_0$，先按上节包围 $Y(s,u_0)$，再用

$$
Y(s,u)-Y(s,u_0)=\int_{u_0}^uT(s,v)\,dv
$$

和整个角盒的实际 $T$ 包扩张。同理 $Y_s$ 用 $T_s$、$Y_{ss}$ 用 $T_{ss}$、$Y_p$ 用 $T_p$。这个步骤消费连续全角盒；它不会将离散中心值冒成该盒上界。

## 7. 与现有准确输入和有限求值的接口

一个最薄实际 provider 应明确给：

- 实际角函数定义、全部保存系数、物理径向 knots 和边界 lifting 的来源 SHA；
- 固定物理 $s,u$ 下的 $T,T_s,T_{ss},T_u$，以及实际需要的参数列；
- 按 (14) 的 cell Taylor 系数盒与完整余项界，或等价的已认证完整积分/第一矩；
- 准确 profile $a,a_s,a_{ss}$ 和轴向中心 $Z,Z_s,Z_{ss}$，参数变化时还给相应完整列。

可复用 fd2d_gc_current_native_interval.py 的准确有理/Arb endpoints、区间记录与显式 unresolved 机制；但其旧 GC raw field 工厂不是本 T provider，不能只改名字即消费。

R118 的准确原椭圆/矩包可以提供其已绑定的固定 $a_0$ 或既定 balanced seed 常数。R187 实际新 ellipse 的 dyadic A/B、准确周长和等弧长反解必须另与该新曲线绑定。不能把 R118 固定对象的包充作任意新 A/B 的证书。可复用相同正有理周长级数、严格单调 arc bracket 和完整三角链式公式，但必须保存实际新参数和尾项。

R181 B32 的准确 profile 则由其独立新定义/消费者提供；R171 旧 7c3f base 包不等于 B32。若准确物理终点与保存 float label 不同，必须使用明确末域覆盖，而非用近似相等默许遗漏。

完整 finite provider 可以用 fixed composite Gauss8 同时求 $T,T_s$ 和参数列的近似积分；固定节点/权与参数无关时，相同求积与参数微分交换。它仍是准确 primitive 的数值求值，不意味着该离散 primitive 对查询角 $u$ 的数值导数等于完整 $T$。最终消费者应使用 (14)–(17) 包准确积分，且始终从完整 T 公式得到 $X_u,X_{su},X_{uu}$。

## 8. 范围与实现状态

本定理支付了准确 quarter primitive、真实 mean/Fubini、全部列、四折有限目标/normal、严格 cell 积分余项及连续角盒的数学依据。没有在本文中执行新的 whole field、F/J、BVP 或 body 计算；也没有给当前坏初值补造通过证书。

R187 已保存的原实际初值 kernel/report 保持身份；后续 quarter provider 的新浮点执行须记录其自身来源与结果。C² 径向基必须按真实 knot 分片消费，参数列必须属于相同完整表示。最终强目标仍须由实际良好候选的完整等距、曲率、reach、闭帽与幅度证书共同支付。
