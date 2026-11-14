# R260：固定标量 jet 的一致性、角度量演化及有限投影的强迫误差

日期：2026-11-14。状态：**完整条件定理、原源码的解析核对与误差分解**。本文没有运行新的数值计算，没有改变原 scalar、Frenet 方程、求解器或接受容差，也不为课题 README 增加完成门。

源码返回的三元组 $(a,\mathtt{ap},\mathtt{app})$，只有在相应导数恒等式成立时，才可直接写成 $(a,a',a'')$。在固定有限 Gauss 半径表达上，返回的后两列来自设计相位；它们与有限和的字面导数之间须按同一对象记账。下面给出这种差异如何进入**真实目标度量**与二阶读出的精确公式，并把它与有限角投影、径向插值残差分开。

相关结果：[R251](R251-direct-relative-operator-metric-certificate.md) 直接检验实际有限场对同一个 $a^2$ 的归一化 Gram 算子误差，不依赖本篇的演化估计；[R249](R249-shared-node-inlet-parity-normal-form.md) 的共享节点 $C^2$ 规范形仍是合法的有限对象，不因本篇指出的 jet 解释差异而失效。原标量的完整分片、三个 bump 和已有元数据见[同源标量包络说明](../notes/2026-11-14-complete-scalar-piecewise-envelopes.md)。

## 1. 对象、符号与正则性

固定已经选定的全部设计参数与核心参数；本篇讨论一个固定标量和固定材料图，不把联解中尚未满足常数约束的不同节点参数当作新的 $s$ 依赖设计。记源码的三个实函数为

$$
a(s)>0,\qquad \nu(s):=\mathtt{ap}(s),\qquad
\eta(s):=\mathtt{app}(s).
$$

在一个光滑开分片上，设 $a\in C^1$、$\nu$ 连续。需要二阶结论时再假设 $a\in C^2$、$\nu\in C^1$。定义

$$
\varepsilon_0(s)=\nu(s)-a'(s),\qquad
\varepsilon_1(s)=\eta(s)-\nu'(s). \tag{1}
$$

特别地，$\varepsilon_1$ 的第二项是 $\nu'$，不是 $a''$；若可微，则

$$
\eta-a''=\varepsilon_1+\varepsilon_0'. \tag{2}
$$

这些是选定实函数之间的误差。构造常量的舍入、求值舍入以及数值逆材料图误差，若未包含在这些实函数定义内，应另行外包，不能把浮点程序作为对全部实数自变量可微的字面函数。

允许采用两种同一材料图的坐标：

- $\xi=\theta$ 时，固定密度 $\sigma(\xi)=1$；
- 原有限 Fourier 场的 $\xi=\phi$ 时，$\theta=\Phi_c(\phi)$，固定 $\sigma(\phi)=\rho_c(\phi)>0$。

目标度量在这两个坐标中分别为

$$
g=ds^2+a(s)^2\,d\theta^2
  =ds^2+a(s)^2\sigma(\xi)^2\,d\xi^2. \tag{3}
$$

这里 $\sigma$ 与 $s$ 无关，$\mathrm{Eucl}$ 表示空间欧氏度量。对一族正则空间纬圈 $F(s,\xi)$，设

$$
\lambda=|F_\xi|>0,\qquad T=F_\xi/\lambda,\qquad
T_\xi=\lambda\kappa N,\qquad B=T\times N,\qquad \kappa>0.
$$

$N$ 是纬圈主法向，$\kappa$ 是纬圈曲率，不是曲面的主曲率。原未投影 Frenet 速度为

$$
V(F;a,\nu)=\alpha N+\beta B,\qquad
\alpha=-\frac{\nu}{a\kappa},\qquad
\beta=\sqrt{1-\alpha^2}>0. \tag{4}
$$

以下定理均假定真实所用分片上的正则性和正域成立。实际有限网格上若仅检查了这些条件的样点值，不能仅凭本篇定理将它们升级成全角连续下界。证明只需所写一阶混合导数存在并可交换；当前角解析的有限场满足所需角向光滑性时，可以直接使用这些恒等式。

## 2. 未投影方程真正保持的角度量

### 定理 2.1：角速度是 $\nu/a$，而不预设为 $a'/a$

若 $F_s=V(F;a,\nu)$，则逐点有

$$
|F_s|^2=1,\qquad F_s\cdot F_\xi=0,\qquad
\partial_s\log\lambda=\frac{\nu}{a}. \tag{5}
$$

若某个初始截面满足 $\lambda(s_0,\xi)=a(s_0)\sigma(\xi)$，定义

$$
\widetilde a(s)
=a(s_0)\exp\!\left(\int_{s_0}^{s}\frac{\nu(t)}{a(t)}\,dt\right).
$$

则整个存在区间内的诱导度量恰为

$$
F^*\mathrm{Eucl}=ds^2+\widetilde a(s)^2\sigma(\xi)^2\,d\xi^2. \tag{6}
$$

因此在该区间上严格等距于 (3) 的必要且充分的标量一致性条件为

$$
\nu=a', \tag{7}
$$

这里仍以存在这样的正域解及正确初始角度量为前提；(7) 本身不是一个全局存在性定理。

**证明。** $N,B,T$ 是正交单位标架，故 (4) 给出前两个恒等式。由 $T\cdot V=0$ 求 $\xi$ 导数，再用 $T_\xi=\lambda\kappa N$，有

$$
T\cdot V_\xi=-T_\xi\cdot V=-\lambda\kappa\alpha.
$$

于是

$$
\partial_s(\lambda^2)
=2F_\xi\cdot F_{s\xi}
=2\lambda T\cdot V_\xi
=-2\lambda^2\kappa\alpha
=2\frac{\nu}{a}\lambda^2.
$$

积分得到 (5)、(6)。若 $\widetilde a=a$，对其正值取对数再求导得到 $\nu/a=a'/a$；反之，(7) 和初值使同一个一阶标量方程有同一个解。证毕。

### 推论 2.2：标量不一致的累积误差

设 $a$ 正、连续且分片 $C^1$，各段可用上述公式。令

$$
E(s)=\int_{s_0}^{s}\frac{\varepsilon_0(t)}{a(t)}\,dt,
\qquad
L_0(s)=\int_{s_0}^{s}\frac{|\varepsilon_0(t)|}{a(t)}\,dt
\quad(s\ge s_0).
$$

则

$$
\frac{\widetilde a(s)}{a(s)}=e^{E(s)},\qquad
\left\|g^{-1/2}(F^*\mathrm{Eucl}-g)g^{-1/2}\right\|_{\mathrm{op}}
=|e^{2E(s)}-1|
\le e^{2L_0(s)}-1. \tag{8}
$$

**证明。** $\partial_s\log(\widetilde a/a)=\varepsilon_0/a$，初始比值为一。参考正交标架下的 Gram 缺陷是 $\operatorname{diag}(0,e^{2E}-1)$，故算子范数正是式 (8)。证毕。

这个式子允许 $\varepsilon_0$ 有符号抵消；不能用 $\int|\varepsilon_0|/a$ 反向声称一个必然的误差下界。若 $\varepsilon_0$ 连续且并非恒为零，则 $E$ 不能在整段上恒为零，因而 (8) 的精确误差在某处非零；其**数值大小**仍须另算。固定 Gauss 的差异完全可能远小于原求解容差，不能只凭“不是恒等式”就宣布当前数值门失败。

### 推论 2.3：圆参考的真实方程

在材料角中取 $F=(R(s)\cos\theta,R(s)\sin\theta,Z(s))$，其中 $R>0$。选 $N=-e_r$、$B=e_z$，则 $\kappa=1/R$，(4) 给出

$$
R'=\frac{\nu}{a}R,\qquad
Z'=\sqrt{1-\left(\frac{\nu R}{a}\right)^2}. \tag{9}
$$

只有先有 $R=a$，才可将第二式写成 $Z'=\sqrt{1-\nu^2}$。若 $R(s_0)=a(s_0)$，第一式中 $R=a$ 在整段成立当且仅当 $\nu=a'$。将设计函数直接放进 $F=(a\cos\theta,a\sin\theta,Z)$ 并令 $Z'=\sqrt{1-\nu^2}$，不能绕过这一条件。

此外，当相关导数存在时，式 (6) 的实际内蕴 Gauss 曲率为

$$
-\frac{\widetilde a''}{\widetilde a}
=-\frac{\nu'}a-\frac{\nu(\nu-a')}{a^2}. \tag{10}
$$

这是由 $\widetilde a'/\widetilde a=\nu/a$ 直接求导得到的。它不把源码的 $\eta$ 自动认成 $a''$，也不把纬圈曲率 $\kappa$ 与内蕴 Gauss 曲率混用。

## 3. 有限角投影和径向残差是独立的强迫项

### 定理 3.1：一般有限场的精确强迫恒等式

对一个实际有限场，不要求它精确解未投影方程。以同一场自身的纬圈标架定义 (4)，再定义

$$
e=F_s-V(F;a,\nu). \tag{11}
$$

若所需导数存在，则

$$
\begin{aligned}
|F_s|^2-1&=2V\cdot e+|e|^2,\\
F_s\cdot F_\xi&=e\cdot F_\xi,\\
\partial_s(\lambda^2)
 &=2\frac{\nu}{a}\lambda^2+2F_\xi\cdot e_\xi,\\
\partial_s\log\frac{\lambda}{a\sigma}
 &=\frac{\varepsilon_0}{a}+\frac{T\cdot e_\xi}{\lambda}.
\end{aligned} \tag{12}
$$

令 $q=\lambda^2/(a^2\sigma^2)$，则另有精确变分常数式

$$
q(s,\xi)=e^{2E(s)}
\left[
q(s_0,\xi)+
\int_{s_0}^{s}e^{-2E(t)}
\frac{2F_\xi(t,\xi)\cdot e_\xi(t,\xi)}
     {a(t)^2\sigma(\xi)^2}\,dt
\right]. \tag{13}
$$

**证明。** 把 $F_s=V+e$ 代入前两项，用 $|V|=1$、$V\cdot F_\xi=0$。第三项是在定理 2.1 的计算中加入 $2F_\xi\cdot e_\xi$。对 $\lambda/(a\sigma)$ 取对数导数得到第四项；对 $q$ 求导并乘以积分因子 $e^{-2E}$ 得到 (13)。证毕。

对原有限旋转 $\phi$ 表示，令 $\mathcal P_{M,N}$ 表示**真实使用的均匀 $\phi$ 求积、模截断和重新合成**的整个世界坐标算子：先转到旋转框架，按原 cosine/sine 通道投影，再转回世界坐标。它与精确连续角投影不必相同。可以精确拆分

$$
e=
\underbrace{\bigl(\mathcal P_{M,N}V-V\bigr)}_{e_{\mathrm{ang}}}
+\underbrace{\bigl(F_s-\mathcal P_{M,N}V\bigr)}_{e_{\mathrm{rad}}}.
\tag{14}
$$

- $e_{\mathrm{ang}}$ 包括有限带宽误差及实际离散求积造成的 alias 差异；
- $e_{\mathrm{rad}}$ 是该有限场相对于同一个有限 RHS 的径向/插值残差。

对于保存节点后重建的物理 quintic，后者须针对这个 quintic 的真实导数解释；原求解器在另一 collocation 插值上的残差不能未经说明直接代入。浮点求值误差仍是独立记账项。小的 finite collocation 残差不意味着 $e_{\mathrm{ang}}=0$，也不意味着 $\varepsilon_0=0$。

式 (12) 是同一场的等式，因而也允许不同误差项发生抵消。本篇没有据单项的非零性断言某个实际有限场一定超过既定误差门。

### 推论 3.2：一个直接的相对算子上界

假设在所考察区间上，初始角度量满足

$$
1-\delta_0\le q(s_0,\xi)\le1+\delta_0,\qquad 0\le\delta_0<1.
$$

设真实连续界满足 $|e|\le\epsilon$、$\lambda(s,\xi)\ge\lambda_*(s)>0$，并记

$$
L(s)=\int_{s_0}^{s}
\left(\frac{|\varepsilon_0(t)|}{a(t)}
+\frac{\|e_\xi(t,\cdot)\|_\infty}{\lambda_*(t)}\right)\,dt,
\qquad Q(s)=(1+\delta_0)e^{2L(s)}.
$$

则

$$
(1-\delta_0)e^{-2L(s)}\le q(s,\xi)\le Q(s),
$$

并有

$$
\boxed{
\left\|g^{-1/2}(F^*\mathrm{Eucl}-g)g^{-1/2}\right\|_{\mathrm{op}}
\le
\max\{2\epsilon+\epsilon^2,\ Q(s)-1\}
+\epsilon\sqrt{Q(s)}.
} \tag{15}
$$

**证明。** 积分 (12) 最后一式，注意它给出 $\sqrt q$ 的对数变化。由于

$$
(1+\delta_0)e^{2L}-1
\ge 1-(1-\delta_0)e^{-2L},
$$

有 $|q-1|\le Q-1$。在目标正交基下，缺陷矩阵的两个对角分量绝对值分别不超过 $2\epsilon+\epsilon^2$、$Q-1$，混合分量为

$$
\frac{|e\cdot F_\xi|}{a\sigma}
\le\epsilon\sqrt q\le\epsilon\sqrt Q.
$$

把矩阵拆成对角部分与非对角部分，其算子范数至多为两者范数之和，即得 (15)。证毕。

这是一条可用的条件估计，不要求实际流程必须另作这一连续证书。R251 可以直接对同一场和同一 $a^2$ 检验真实 Gram 算子误差；原 README 允许的数值近似与严格证明之间的差距仍按原规定报告。

## 4. 返回的 app 如何影响二阶物理读出

### 命题 4.1：显式 $s$ 导数的精确偏差

在固定物理状态、固定纬圈标架和固定 $\kappa$ 下，(4) 中 $\alpha$ 的真实显式 $s$ 导数为

$$
\alpha_s^{\mathrm{true}}
=-\frac{\nu'}{a\kappa}
+\frac{\nu a'}{a^2\kappa}.
$$

原二阶读出使用的替代值为

$$
\alpha_s^{\mathrm{src}}
=-\frac{\eta}{a\kappa}
+\frac{\nu^2}{a^2\kappa}.
$$

两者之差恰为

$$
d_\alpha
=-\frac{\varepsilon_1}{a\kappa}
+\frac{\nu\varepsilon_0}{a^2\kappa}. \tag{16}
$$

相应未投影速度的显式导数偏差为

$$
d_\alpha\left(N-\frac{\alpha}{\beta}B\right),\qquad
\left|d_\alpha\left(N-\frac{\alpha}{\beta}B\right)\right|
=\frac{|d_\alpha|}{\beta}. \tag{17}
$$

**证明。** 对 $-\nu/(a\kappa)$ 用商法则，作差得到 (16)。由 $\beta^2=1-\alpha^2$，有 $\beta_s=-\alpha\alpha_s/\beta$。$N,B$ 正交且 $\alpha^2+\beta^2=1$，所以括号向量的模长为 $1/\beta$，得到 (17)。证毕。

若已知正下界 $a_*,\kappa_*,\beta_*$ 及 $|\nu|\le\nu_*$，则

$$
|\Delta V_s^{\mathrm{explicit}}|
\le \frac1{\beta_*}
\left(\frac{|\varepsilon_1|}{a_*\kappa_*}
+\frac{\nu_*|\varepsilon_0|}{a_*^2\kappa_*}\right). \tag{18}
$$

投影后的对应界还要使用实际 $\mathcal P_{M,N}$ 在所选范数中的算子界；不能把离散 Fourier 投影默认当作连续上确界范数下的压缩映射。

原 [LargeCoreSavedPrefix](../computations/geometry_20261114_large_core_saved_prefix.py) 先沿**保存的一阶状态**作 state JVP，再加入上述 da/db 显式项。式 (16) 正好对应这后一项。state JVP 中的方向若与当前有限 RHS 有差异，那是另一项保存导数/残差代价；该源也单独记录了这种差异。这里没有默许保存方向恰等于局部 RHS。

app 不进入 (4) 的一阶速度，因此 $\varepsilon_1$ 不直接出现在 (5)、(12)。即使 $\eta=\nu'$ 精确成立，$\varepsilon_0\ne0$ 仍会经 (16) 的第二项影响上述二阶替代公式。反过来，$\nu=a'$ 也不会单独保证所给 $\eta$ 就是正确二阶数据。

### 命题 4.2：二阶数据来源不改变共享节点 Hermite 的 $C^2$ 身份

给定任意一份共享节点值、一阶和二阶 jet，逐单元使用唯一五次 Hermite 多项式，得到一个精确定义的有限 $C^2$ 场。二阶 jet 是否为某个 ODE 的真实导数，不影响这一代数事实。

具体地，在长度 $h$ 的一个单元内，若两个场的端点值和一阶 jet 相同，二阶 jet 差为 $\Delta W_0,\Delta W_1$，置 $u=(s-s_j)/h$，则

$$
\Delta F(s)
=\frac{h^2}{2}\left[
u^2(1-u)^3\Delta W_0
+u^3(1-u)^2\Delta W_1
\right]. \tag{19}
$$

若两端差的模长均不超过 $\delta$，则整个单元有

$$
|\Delta F|\le h^2\delta/20,\qquad
|\Delta F_s|\le h\delta/2,\qquad
|\Delta F_{ss}|\le3\delta. \tag{20}
$$

**证明。** 式 (19) 的六个端点条件与两场之差相同，次数至多五，故由唯一性成立。其五次 Bernstein 控制向量为

$$
h^2(0,0,\Delta W_0/20,\Delta W_1/20,0,0).
$$

基函数非负且和为一，给出第一界；一次、二次导数控制向量分别是五倍一阶差与二十倍二阶差，再除以 $h,h^2$，给出其余两界。相邻单元共享同一数据时，零至二阶端点 jet 相同，故整体 $C^2$。证毕。

在端点本身，二阶差仍是给定的 $\Delta W_i$。因此细化 $h$ 可以削弱这种差对位置和一阶读出的影响，但不会自动把所给二阶数据变成某个不同 RHS 的真实导数。这不新增“所有六 jet 差必须达到机器精度”的课题完成门；它只说明在当前实际曲率/reach 预算中应使用实际有限场自己的导数。[R249](R249-shared-node-inlet-parity-normal-form.md) 的入口奇偶恒等式和共享节点规范形保持有效。

## 5. 当前完整 scalar 源的逐段对应

这里只核原源码，不给尚未完成的新场填写数值误差。三组实际冻结设计控制由 v3 PrefixControlsProfile 定义；v4 冻结同一份完整 v3 scalar spec，不把 active 参数向量为空误认为三个原 bump 消失。

| 段 | 半径的同源定义 | 返回 $\nu,\eta$ 与真实导数的关系 |
|---|---|---|
| 原 .99 prefix | 保存节点 jet 的五次 Hermite；有 bump 的共同细分上次数至多六 | 对同一个实多项式，解析导数一致；精确共享节点系数、舍入系数及浮点求值仍须按其真实身份区分 |
| 三个冻结控制 | $p_i w_i^2\,64x^3(1-x)^3$，端点零、一次、二次 jet 为零 | 同一多项式定义中的控制列为真实一二导，因此不会凭空修复或增加基函数的 $\varepsilon_0,\varepsilon_1$；舍入另计 |
| AngleConnector | 固定 48 点、三 panel 的部分积分有限和 | 返回 $\nu=\sin\varphi$、$\eta=-k\cos\varphi$；相位满足 $\varphi_s=-k$ 的实公式中有 $\eta=\nu'$，但一般没有 $a_{48}'=\nu$ |
| connector 后的显式 coast | $a_T-.985(s-T)$ | 在同一实仿射定义中 $\nu=-.985=a'$、$\eta=0$ |
| terminal bridge 的 flat turn / brake | 原固定 64 点有限和 | $\nu=\sin p$；半径导数要微分该有限和，不能用 $\sin p$ 直接替代 |
| terminal bridge 内部 coast | 原 64 点常相位有限和，仍为仿射 | 字面斜率是 $\sin p_0$ 乘原归一化权重总和；不应在位值证明里未经说明把该和设为一 |

源码依据：

1. [geometry_20261114_full_scalar_profile.py](../computations/geometry_20261114_full_scalar_profile.py) 的 base_jet、ScalarBump、CompleteProfile 固定了完整调用链。
2. [geometry_20261114_prefix_controls_profile.py](../computations/geometry_20261114_prefix_controls_profile.py) 将当前三个支撑放在非轴对称 prefix 内。
3. [geometry_20261114_r225_fixed_profile.py](../computations/geometry_20261114_r225_fixed_profile.py) 先构造精确有理 Hermite 系数，再转成浮点数组；profile 用该数组计算一二导。单元内的多项式导数关系与共享节点精确规范形、逐次舍入误差是三个不同层次。
4. [strong_20261114_scaled_core_tail_connector.py](../computations/strong_20261114_scaled_core_tail_connector.py) 的 integral/profile 使用固定 48 点部分求积，并直接返回设计相位的速度和加速度。
5. [alternative-neck-provider.py](../computations/alternative-neck-provider.py)、[alternative-neck-flatturn.py](../computations/alternative-neck-flatturn.py)、[alternative-neck-excursion.py](../computations/alternative-neck-excursion.py) 给出固定 64 点原 bridge。
6. [alternative-outward-probe.py](../computations/alternative-outward-probe.py) 的 frame/project/stats 给出 (4)、原有限投影及 (16) 所分析的显式二阶项；[geometry_20261114_fft_frenet.py](../computations/geometry_20261114_fft_frenet.py) 更换求值方式，不改变所选有限模空间。

### 5.1 bridge 相位本身还应保留的构造舍入项

平顶 turn 的相位写成

$$
p(u)=p_0+\frac{p_1-p_0}{1-\epsilon}J_\epsilon(u),
\qquad
J_\epsilon'(u)=r_\epsilon(u),\qquad
u=(s-s_0)/L.
$$

所以字面的相位导数为

$$
p_s=\frac{p_1-p_0}{L(1-\epsilon)}r_\epsilon(u).
$$

piece_jet 使用的值则为

$$
\widehat p_s=\operatorname{sign}(p_1-p_0)\,K\,r_\epsilon(u),
$$

而构造器用浮点计算 $L=|p_1-p_0|/[K(1-\epsilon)]$。若 $L,p_0,p_1,K,\epsilon$ 均固定为构造后的 binary 常量，两种系数之间的差也须保留：

$$
\varepsilon_1(s)
=\cos p(u)
\left[
\operatorname{sign}(p_1-p_0)K
-\frac{p_1-p_0}{L(1-\epsilon)}
\right]r_\epsilon(u), \tag{21}
$$

再加上所选读出模型中的求值误差。若定义的是未舍入的同一个代数构造，该括号才严格为零。brake 的相位是二次多项式，源 dp 使用该同一相位的一阶公式；内部 coast 的相位常数。此项与半径的 64 点求积误差是不同来源。

当前调用链明确把新 AngleConnector 峰值设为 $2.5$，把 terminal bridge 的构造峰值设为 $7.5$；原物理尾背景仍有自己的 curvatureBound=8 身份。不能因原 port 内的旧 tag 为 $8$ 而重建成另一条 bridge，这会改变本篇分析的 $a,\nu,\eta$。

## 6. 对同一个固定有限 Gauss 表达作严格外包

### 6.1 部分求积的真实导数

在一个正在增长的 panel 上，令起点为 $\ell$、当前宽度为 $d=u-\ell$，固定实际节点和归一化权重为 $x_q,w_q$。置 $f(v)=\sin\varphi(v)$，

$$
Q(d)=d\sum_{q=1}^{n}w_q f(\ell+x_qd).
$$

已完成的其他 panel 贡献常数。对同一个实表达直接微分得

$$
\begin{aligned}
Q'(d)
 &=\sum_qw_q\left[f(\ell+x_qd)
       +dx_q f'(\ell+x_qd)\right],\\
Q''(d)
 &=\sum_qw_q\left[2x_q f'(\ell+x_qd)
       +dx_q^2 f''(\ell+x_qd)\right].
\end{aligned} \tag{22}
$$

若 $a_Q(s)=a_0+L(C+Q(d))$、$u=(s-s_0)/L$，则

$$
a_Q'=Q'(d),\qquad a_Q''=Q''(d)/L.
$$

返回的 $\nu=f(u)$ 与 $a_Q'$ 之差就是

$$
\varepsilon_0=f(\ell+d)-Q'(d). \tag{23}
$$

这不等于仅仅评估 $Q(d)-\int_\ell^{\ell+d}f$ 的大小。积分误差本身小，不会在没有导数估计时自动给出其导数误差小。

两个有用的精确积分恒等式是

$$
\begin{aligned}
f(\ell+d)
 &=\int_0^1\!\left[f(\ell+dx)+dx f'(\ell+dx)\right]dx,\\
f'(\ell+d)
 &=\int_0^1\!\left[2x f'(\ell+dx)+dx^2 f''(\ell+dx)\right]dx.
\end{aligned} \tag{24}
$$

**证明。** 分别积分 $\partial_x[x f(\ell+dx)]$ 与 $\partial_x[x^2 f'(\ell+dx)]$。证毕。

因此 (23) 与 $f'(\ell+d)-Q''(d)$ 都是对明确新 integrand 的固定求积误差。可以直接对 (22)–(24) 作 interval/Taylor 外包，无需改动原 Gauss 点数、原 scalar 或任何物理节点。

### 6.2 一个完全保留 binary 节点/权重的误差公式

不必把实际节点、权重理想化成精确代数 Gauss 节点。设它们确实落在 $[0,1]$，并以精确有理数保留。对一个实函数 $g$，取多项式

$$
P(x)=\sum_{j=0}^{D}b_jx^j,\qquad
\|g-P\|_{\infty,[0,1]}\le\tau.
$$

定义实际 moment defect

$$
m_j=\frac1{j+1}-\sum_qw_qx_q^j.
$$

则

$$
\left|\int_0^1g(x)\,dx-\sum_qw_qg(x_q)\right|
\le
\left|\sum_{j=0}^{D}b_jm_j\right|
+\left(1+\sum_q|w_q|\right)\tau. \tag{25}
$$

也可把第一项保守地换成 $\sum_j|b_j|\,|m_j|$。若 $b_j$ 是区间系数，以相应严格区间运算包住第一项即可。

**证明。** 将 $g=P+(g-P)$ 代入；多项式部分逐幂精确积分，余项的积分模长至多 $\tau$，有限和模长至多 $\tau\sum|w_q|$。证毕。

当前相位在每个解析分片上是次数不超过四的多项式。对 $\sin$、$\cos$ 在有界相位区间作 Taylor 展开，实轴上各阶导数模长至多一，给出显式余项，再乘相位的一二阶多项式即可对 (24) 的两个 integrand 构造 $P,\tau$。对同一源分片进一步细分只改善包络，**不改变原积分表达**。使用更高精度和更细包络可以任意收紧这个固定函数的误差区间；不能保证其真实误差一定小于一个任意预选阈值。

式 (25) 自动保留实际权重和不恰为一、节点/权重构造舍入等差异。若采用理想 Gauss 的高阶误差公式，也必须另加这些实际常量与理想常量之差。仅比较 48 与 80 点读数不能代替对当前固定 48 点表达的严格误差界。

当 $f(\ell+d)=\sum_{j\ge0}c_jd^j$ 在相关范围内收敛时，另有可直接核对的级数

$$
\varepsilon_0(d)
=\sum_{j\ge0}c_j
\left[1-(j+1)\sum_qw_qx_q^j\right]d^j. \tag{26}
$$

它由逐项微分 $Q$ 得到。理想 $n$ 点 Gauss 对次数不超过 $2n-1$ 的多项式精确时，前 $2n$ 个方括号为零；实际 binary moment defect 应按其真实值保留。这解释了“不是严格恒等式”与“误差可能极小”可以同时成立，并没有给当前函数填写一个未经运行的数值量级。

### 命题 6.3：非零线性相位上，有限内部节点的部分求积导数不可能恒等

假设某个开 panel 内

$$
f(\ell+d)=\sin(A+Bd),\qquad B\ne0,
$$

求积节点有限且满足 $|x_q|<1$。则 $Q'(d)$ 不可能在任何非空开区间上恒等于 $f(\ell+d)$。

**证明。** $Q'$ 是有限个

$$
\sin(A+Bx_qd)+dBx_q\cos(A+Bx_qd)
$$

的线性组合。每一项被常系数微分算子 $(\partial_d^2+B^2x_q^2)^2$ 消去，所以

$$
\mathcal LQ'=0,\qquad
\mathcal L=\prod_q(\partial_d^2+B^2x_q^2)^2.
$$

另一方面，

$$
\mathcal L\sin(A+Bd)
=\left[\prod_q B^4(x_q^2-1)^2\right]\sin(A+Bd).
$$

括号严格正，而 $B\ne0$ 使最后的正弦不在任何开区间恒为零。因此两函数不能在一个开区间相等。证毕。

AngleConnector 的中段相位为一次多项式，斜率 $B=-LK$ 非零。**只要实际固定 Gauss 节点保持严格内部**，此命题便直接说明该中段的有限和导数与返回的 $\nu$ 不是精确函数恒等式。命题只给出非恒等性，不提供实际误差大小，不证明存在可观测的接缝跳变，也不判定既定数值容差是否已通过。

## 7. 分片接缝与精确对象的边界

若同一半径表达在各 panel 之间连续，则定理 2.1、式 (8)、(12)、(13) 可按段积分拼接，只需使用真实单侧导数。部分求积在一个 panel 完成后变为常数，新 panel 从零宽开始；在共同相位值 $f(u_*)$ 处，左右半径导数的候选值分别为

$$
Q_{\mathrm{old}}'(d_{\mathrm{full}}),\qquad
Q_{\mathrm{new}}'(0)=\left(\sum_qw_q\right)f(u_*).
$$

返回的 ap 两侧相等，并不独自证明这两个量精确相等。二阶导数也同样应使用 (22)。CompleteProfile.description 的接缝检查比较的是**返回的三列**，不是对有限和微分后的这两个单侧值。

另外，独立保存的段末 dr/a1、构造后的长度、舍入的多项式系数与另一段起始常量之间，可能还需要同一表示的舍入账。本文没有计算当前这些差的数值，也没有断言已经测到非零跳变。确切规范形、其数值 evaluator 以及另一个分别舍入的表达必须保持身份清楚。

若某种字面分片定义的 $a$ 本身在边界有跳变，而 $F_\xi$ 连续，则相对角长度还会在该处乘以 $a_-/a_+$；对数公式中相应加入 $\log(a_-/a_+)$。这条一般公式不能被用来虚构当前数据中存在这样的跳变。

若已声明的数学目标是相位的精确积分函数，而有限 Gauss 只是其 evaluator，则应以该目标的导数恒等式为准，并外包 evaluator 误差。若当前声明的目标是原固定有限和，则应外包原有限和及其真实导数。两种论证都可以明确陈述，但不能在“同一 $g$”精化中静默互换。对曲面自身，R249 的共享节点实 Hermite 规范形具有独立的精确 $C^2$ 定义；上述 scalar 解释问题不会取消它已证明的拼接恒等式。

## 8. 对当前精化和实际结论的准确含义

由前述定理可以得到以下有范围限制的结论：

1. 若固定 $a,\nu$，并证明一列精化场收敛到 (4) 的正域未投影解，且初始角度量正确，则极限保持的是 $\widetilde a$。只有 $\nu=a'$ 时，才由该方程本身推出对原目标 $a$ 的精确等距；否则极限目标误差由 (8) 给出。
2. 加密角模或角求积，只有在相应收敛得到支持时才会减小 $e_{\mathrm{ang}}$；细化物理网格或收紧解算容差，针对的是 $e_{\mathrm{rad}}$。二者均不会在定义上改变原固定 Gauss 造成的 $\varepsilon_0$，也不会自动使源码 $\eta$ 成为 $\nu'$。
3. 固定误差可以已经小于原 solver/机器精度预算，也可能需要明确外包；必须看实际量，不能从源结构单独推断它妨碍完成标准。真实有限场的直接同 $g$ Gram 读出与 R251 证书不依赖“RHS 必然严格保持 $g$”这一未证代理。
4. 改 Gauss 点数、用精确积分替换固定有限和、或直接把 ap 改成有限和导数，都须先明确改变的是 evaluator 还是所解的实函数/方程。本文不执行任何这类改变，不把设计变化夹进同一 $g$ 精化。
5. 同一有限共享节点场仍可以是精确 $C^2$；其度量误差、实际曲率、全空间 reach 和真实整像幅度须对该场本身解释。本篇不要求六 jet 相邻差达到机器精度，不增加新的科学验收门，也不声称尚无实际输出的新闭面已经通过任何门。

## 9. 本次只读源码身份

下列 SHA256 仅是本次读取文件的身份记录，不是一次数值运行的回执：

| 源文件（均在 computations/） | SHA256 |
|---|---|
| geometry_20261114_full_scalar_profile.py | 8ff23e31a58d0f8b087929d69ac8d6f9b6f2777615e50eef5ebe40ed7b6bed6b |
| geometry_20261114_prefix_controls_profile.py | f019e6b33c8e1776d5cca87c22efadd0f999766b894be855efb53ad10b4d6a24 |
| geometry_20261114_r225_fixed_profile.py | 478d0bf603ea05a9f20228ff2fd591e2f767e6ab0686a6129b1114aa831b0c6c |
| strong_20261114_scaled_core_tail_connector.py | 661d5d84dc0dd3da46f4936c2c3ad28f80df3475f421c56d770a2afa6402ac08 |
| alternative-neck-provider.py | 84ed048425c8b0f4deeec8af37828e318150cde5d59995da77f64d923591b9c2 |
| alternative-neck-flatturn.py | c0578ed401a2433c72ec99702c9c32a8412c66264a7fb81a8b8c74ba054fbbdd |
| alternative-neck-excursion.py | f70571b8356e33cb89eabae2dba4e173e6612dac4d65d5df74f5ec14c34ad53c |
| alternative-outward-probe.py | cf163a5c42cff95137a78eefda058b6a18f5f226b4261b686a42e645f4002fcb |
| geometry_20261114_fft_frenet.py | 973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401 |
| geometry_20261114_large_core_saved_prefix.py | 51eab8cdc878e22ad2c57bab129b1ef31463799596fcc40399fd8b0714ccbea0 |

本文的新增结论是同源一致性条件、强迫误差恒等式、二阶替代项偏差及固定有限求积的严格记账办法。没有调用原数值构造器，没有生成候选新解，没有改动任何既有求解源码或保存输入。

