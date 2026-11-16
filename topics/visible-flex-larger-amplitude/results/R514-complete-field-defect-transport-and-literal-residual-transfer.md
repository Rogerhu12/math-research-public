# R514：当前完整闭场的 Frenet 缺陷输运与原有限残差到相对度量的条件传递

作者：exact_refinement（AI）。日期：2026-11-16。

**可信度：本文的准确恒等式和条件估计已由下文解析推导证明；没有取得新的数值常数，没有执行科学计算或产生实际场的 metric floor。** 原 RMS、BC、native、FD 与末审计的接受门全部不变。本文不把找到一个准确等距参考、证明全 BVP 逆界或通过本文的可选估计，增加为继续原求解、精化或 R459 直接测量的前门。

已有 [R249](R249-shared-node-inlet-parity-normal-form.md) 给出 Hermite 修补、完整 Fourier 角权与 Gram 扰动界；[R416](R416-current-C-cut-atlas-compatibility-and-accurate-geometric-patch.md) §9 已给准确 cut 修补的一阶场差到 Gram 差的公式；[R459](R459-fixed-closed-target-relative-error-and-refinement-evidence.md) 已实现完整域相对广义谱测量。本文不重新编号这些引理。新增内容是：**不借一个未知准确解，直接把同一当前场对准确 Frenet 速度的缺陷，以及其角长沿径向的缺陷，传到该场的完整相对 Gram 误差；并把原有限残差、frozen-RHS 换用、五次重构和闭面修补之间的真实差额逐项接上。**

## 514.1 固定的对象与已有源码范围

固定同一个准确 C 定义、全部允许根族、十个准确参数、完整 construction、首材料图以及 $t\in[0,1]$。对于根族中的一个成员 $\zeta$，记当前准确有限闭场为 $F_\zeta$、准确目标为 $g_\zeta$。所有下面的点态论证先固定同一个 $\zeta$；向外上界若对整个原族成立，结论再对全族统一成立。不同盒端点不能被换选成一个共同根。

当前对象遵循：

- R400：真实 frozen450 结果的完整 $3M+2$ 物理节点、原 frozen RHS 与现场第二 jet 字词，提升为准确共享节点五次 Hermite；它不等于未经比较的 SciPy cubic 或 rounded renderer。
- R409：全部原 native shooting 状态经真实径向重放，保存所有实际步端点和两个均值；径向 Cartesian 节点、有限差分形成的水平二阶数据、完整 FFT 字词、$B$ 与 collar 构成另一个明确的准确有限场。
- R416：准确 cut 系数与完整角 patch 形成当前用于 metric 的场；旧数值 cut patch 的界不能直接继承。
- R459：在同一准确 $g$ 与共同材料图下测量完整前缀、native、collar、patch、两反射和两帽的相对 Gram 算子范数；全 $t$ 转移来自准确共轭，不来自有限时间网格。

已核原作用点包括：

| 真实作用点 | 已有字段/操作 | 不能自动推出的量 |
|---|---|---|
| 原 c6a 的 frozen_physical_residual | 用末参数冻结 RHS；原 Lobatto 相对残差；另加实际节点相对残差平方的 $.05$ 端点项 | 准确五次场的完整闭域 ODE 缺陷 |
| 原 1c7 的 ContinuousTenSavedPrefix | 保存 physical_rhs；另求全部 DDY；保 node_saved_vs_local_RHS_max | complex-step DDY 是准确 ODE 二阶导数；全域重构误差已付 |
| 原 f76 的 SeparatedBoundary.__call__ | $r_0-1$、全部 $t_m+2m r_m$、全部高度、core 与入口 $r_m$ 的关联 | 只凭一个 BC 最大值忽略模式权、形成误差或实际 core 身份 |
| 原 5cc 径向重放 | 每个 shooting 段从其真实内端状态重新开始；全部 RK 步、端口倍率、两均值与段末 gap | native 归一残差就是整个连续径向场的 $C^1$ 误差 |
| 原 6a5 的 defining_node_coefficients | 完整 FFT；水平二阶由实际非均匀差商给定；垂直量保真实 mean/$w,w_r$ | 原 FFT、差商、背景或旧 root 标签与当前准确场严格一致 |
| 494fea70 的 Measurement.base_once | 当前完整六 jet 与准确目标；直接广义谱上下界 | 原 solver 阈值已换算成该全域范数 |

这里的旧 112 维来源是当前公式和接口的基线；R442/R451 等真实动态 $M$ 来源只有在其本身的完整闭包和场身份绑定后才能应用同一数学论证。公式不把旧 112 行零补成新 $M$ 数据。

## 514.2 同一当前场的准确速度与合法域

在一个完整 active 坐标片上取坐标 $(x,\phi)$，使目标为

$$
g=\mu(x)^2\,dx^2+A(x)^2\rho(\phi)^2\,d\phi^2,
\qquad \mu>0,\ A>0,\ \rho>0.
\tag{514.1}
$$

这里 $\rho$ 与 $x$ 无关，是该当前场完整材料角的导数。若使用原 $q=\phi/(2\pi)$，则统一把 $\rho$ 换成 $\Phi_q$，并把所有角导数取为 $q$ 导数；公式不混用两种单位。

在数值前缀坐标 $x=s_{\rm num}$ 上，

$$
k=L_*/L_{\rm num},\qquad
\mu=k,\quad A(x)=a_*(kx;p),\quad A_x=k\,a_{*,s}(kx;p).
\tag{514.2}
$$

在尾部径向坐标 $x=r$ 上，

$$
\mu^2=E_C(r),\qquad A(r)=r,\qquad A_x=1.
\tag{514.3}
$$

因此这里没有令 $L_*=L_{\rm num}$，没有用 geometric $1+(B')^2$ 替换 $E_C$，也没有把 numeric scalar 的返回 ap 无条件当成准确 $A_x$。使用准确切口图时，目标和完整 field jets 都按 R416 的同一图变换。

令

$$
d=F_\phi,\quad e=F_{\phi\phi},\quad Q=d\cdot d,\quad
C=d\times e,\quad W=C\cdot C,\quad B=Qe-(d\cdot e)d.
$$

定义

$$
P=A^2\mu^2W-A_x^2Q^3.
\tag{514.4}
$$

在当前完整闭片上，若 $A,\mu$ 的下界严格正且 $P>0$ 已付，则 $Q,W>0$，并可取一个明确的符号 $\sigma\in\{-1,1\}$，定义

$$
V=\frac{\sigma\sqrt P\,C-A_x Q B}{AW}.
\tag{514.5}
$$

这是 [R354](R354-full-Frenet-velocity-and-closed-step-Hermite-remainders.md) 准确速度恒等式在目标径向速度 $\mu$ 下的版本。前缀使用与原正平方根、取向相符的支；下片反射或径向反向时须实际变换该支，不能仍把它叫原上片正支。 更具体地，若空间变换为常正交矩阵 $J$、径向反向记为 $\epsilon\in\{-1,1\}$，则 $\widetilde\sigma=\epsilon\det(J)\sigma$，从而 $\widetilde V=\epsilon JV$；该符号随同真实坐标记录。这里没有改原 noJ/RK 程序，也没有把新的算式当作旧浮点执行逐词相等。

由 $|B|^2=QW$、$B\cdot C=d\cdot B=d\cdot C=0$、$e\cdot B=W$，直接得到

$$
|V|=\mu,\qquad d\cdot V=0,\qquad
e\cdot V=-\frac{A_x}{A}Q.
\tag{514.6}
$$

特别是 $\sqrt P$ 采用声明的非负实平方根，$\sigma$ 单独承载取向。真实闭域的严格正界不可由若干原角点最小值补造。若不能形成合法 $V$，以下“速度缺陷”估计在该片未付；这不拒绝原求解，不证明原场退化，也不阻止继续已有 R459 直接 Gram 包围。

## 514.3 只用完整六 jet 的角长输运恒等式

令 $\lambda=|F_\phi|>0$，定义相对角长

$$
h(x,\phi)=\frac{\lambda(x,\phi)}{A(x)\rho(\phi)}.
$$

对一个固定的准确根成员和固定角，准确有

$$
\boxed{\quad
\partial_x h=
\frac{F_\phi\cdot F_{x\phi}-(A_x/A)|F_\phi|^2}
     {A\rho\,|F_\phi|}
=:\tau(x,\phi).
\quad}
\tag{514.7}
$$

**证明。** $F$ 为当前准确 $C^2$ 场，故
$\partial_x\lambda=(F_\phi\cdot F_{x\phi})/\lambda$。
对 $\lambda/(A\rho)$ 求导，使用 $\rho_x=0$，合并分子即得。该式只需要 $F_\phi,F_{x\phi}$、准确 $A,A_x$ 和完整 $\rho$；不需要第三阶角导数，也不需要一个未知的准确 ODE 解。证毕。

若 $V$ 合法且实际还具有所需角导数，置

$$
r=F_x-V.
$$

由对 $d\cdot V=0$ 作角微分及 (514.6)，另得

$$
\tau=\frac{d\cdot r_\phi}{A\rho\,|d|},
\qquad
|\tau|\le \frac{|r_\phi|}{A\rho}.
\tag{514.8}
$$

(514.8) 是另一种可用估计；**拟接的最薄消费者可采用 (514.7)，不为它增加角三阶前门**。即使某处 $V_\phi$ 尚未形成，只要 (514.7) 的真实正分母和六 jet 已付，角长输运本身仍成立。

设沿明确径向路径 $[a,x]$ 有整个闭角圈的锚界

$$
\sup_\phi |h(a,\phi)-1|\le q_a
$$

以及闭域可积上界 $T(s)\ge\sup_\phi|\tau(s,\phi)|$。则

$$
|h(x,\phi)-1|
\le q_a+\int_{\min(a,x)}^{\max(a,x)}T(s)\,ds
=:q(x).
\tag{514.9}
$$

若全径向区间按真实全部节点、collar、patch、目标片边界分成闭块 $I_i$，每块全角界为 $T_i$，可以用

$$
q(x)\le q_a+\sum_{I_i\ {\rm 经路径}}
|I_i\cap[\min(a,x),\max(a,x)]|\,T_i .
\tag{514.10}
$$

这是完整闭块界之和，不能把实际有限角样点最大值代入。使用自适应 cell 时必须证明该径向路径上每个角均被相应有效界覆盖；不能把 DFS 已访问次数或未付 ledger 的 SHA 当成覆盖。可采用所有实际径向端点的公共细分并对各整角闭块取已付上界，原父 coarse 界仍可作合法 fallback。

## 514.4 由当前速度缺陷和角长直接控制完整 Gram

在一个闭块上，设同一 $V$ 支合法，并已有

$$
\frac{|r|}{\mu}\le\delta,\qquad |h-1|\le q,
\qquad \delta,q\ge0.
$$

定义非负数

$$
a=2\delta+\delta^2,\qquad
b=\delta(1+q),\qquad c=2q+q^2.
$$

那么当前完整场的相对 Gram 误差满足

$$
\boxed{\quad
\left\|g^{-1/2}(F^*e-g)g^{-1/2}\right\|_{\rm op}
\le
\frac{a+c+\sqrt{(a-c)^2+4b^2}}2 .
\quad}
\tag{514.11}
$$

**证明。** 在 (514.1) 的对角坐标中，相对误差矩阵的三项为

$$
D_{11}=\frac{|F_x|^2}{\mu^2}-1,\quad
D_{12}=\frac{F_x\cdot d}{\mu A\rho},\quad
D_{22}=h^2-1.
$$

用 $F_x=V+r$ 及 (514.6)，逐项有
$|D_{11}|\le a$，
$|D_{12}|\le\delta h\le b$，
$|D_{22}|\le c$。
对任意实单位向量 $u$，
$|u^TDu|\le (|u_1|,|u_2|)
\begin{pmatrix}a&b\\b&c\end{pmatrix}
(|u_1|,|u_2|)^T$。
右侧最大值是所列非负对称矩阵的最大特征值，即 (514.11)。证毕。

这里没有假设 $q<1$ 或把 (514.11) 是否小于人为 $\eta$ 设为原 native 接受门。若已有更细的 $h$ 区间，可直接用其端点得到 $|h^2-1|$ 上界并替换 $c$；这只改变估计精度。

该定理没有调用“残差小所以接近某个准确解”的断言。它测的是**当前场自身**，因此不需要先建立另一个等距参考的存在性。代价是必须真实付出 $\delta,\tau$ 的完整闭域界；原接受标量尚未提供这些量。

在不能形成 $V$ 的块，仍可直接从同一六 jet 包围 $|D_{11}|,|D_{12}|$，再结合合法角长界；或完整沿原 R459 算式直接计算。任何一条路线未付都不能改写为数值反证。

## 514.5 原入口边界能支付哪个角长锚

以下仅把原 BC 接到已有 [R237](R237-accepted-M96-core-global-certificate.md)/R249 的完整 Fourier 表达，不重证材料图定理。令 $n_m=2m$，入口实际位置系数为 $r_0,r_m,t_m,z_m$，材料 core 为 $c_m$。先按准确字词定义

$$
b_0=r_0-1,\quad b_{t,m}=t_m+n_m r_m,\quad
b_{c,m}=c_m-r_m.
$$

在旋转框架中，入口准确角导数与材料切向参考之差是

$$
F_\phi-\rho e_\phi=
\left(
-\sum_m b_{t,m}\sin n_m\phi,\ 
b_0+\sum_m[(n_m^2-1)b_{c,m}+n_m b_{t,m}]\cos n_m\phi,\ 
-\sum_m n_mz_m\sin n_m\phi
\right).
\tag{514.12}
$$

这是原 f76 左边界和 R249 的 $\mathcal W_\phi$ 逐项代入；所有实际 $M$ 项保留。原 c6a 结果把 core 取为实际入口 $r_m$；若当前绑定确实逐字保留这一关系，$b_{c,m}=0$。否则使用实际差或其完整界，不从“constant core”标签删掉它。R249 规范形将入口全部 $z_m$ 精确置零，因而规范形位置的最后一项为零；未投影场不能借该零性。

设 $A_0=A(0)>0$，真实 $\rho\in[\rho_-,\rho_+]$、$\rho_->0$。定义

$$
\begin{aligned}
B_r&=\sum_m|b_{t,m}|,\\
B_t&=|b_0|+\sum_m[(n_m^2-1)|b_{c,m}|+n_m|b_{t,m}|]
       +|1-A_0|\rho_+,\\
B_z&=\sum_m n_m|z_m|.
\end{aligned}
$$

令 $q_0=\sup_\phi|h(0,\phi)-1|$，则反三角不等式给一个完整角长锚：

$$
q_0\le \frac{\sqrt{B_r^2+B_t^2+B_z^2}}{A_0\rho_-}.
\tag{514.13}
$$

若 $A_0$ 是准确族变量，分子用其真实统一外包，分母用严格下界。只有原 DAG 确认 $A_0=1$ 时才能消去 $|1-A_0|$。

(514.13) 的模式权是原 R237/R249 三角界在实际 BC 行上的应用，不能从某个原 $M96$ 数值证书移用其数值端点到新 $M$。原打印 boundary_residual_max 若只给浮点形成的行最大值，还要保“准确字面 $b$ 减实际已形成 BC 行”的舍入差；这些小差可由真实节点字词现场准确形成，不能默认为零。即便所有行均有同一小界，$\sum n_m$、$\sum(n_m^2-1)$ 与 $\rho_-^{-1}$ 仍在换算中。故原 $10^{-11}$ 本身不是相对 metric 上界。

尾部也可以从真实 cuff 圆作独立锚：若原准确 collar/cap 拼接已保证位置恰为 $(r_c\cos\Theta,r_c\sin\Theta,H)$ 且目标角半径为同一 $r_c$，则该圆 $h=1$。这只支付角长锚；它不证明 cuff 径向速度满足 $\mu^2=E_C$，更不能由此略去 collar/B 的径向误差。

## 514.6 原 cubic 残差到当前 quintic 的完整形成差额

原 c6a 的 frozen-physical RMS 仍评价 SciPy 保存曲线；R400 保存的第一 jet 却是冻结末参数后重新形成的 physical_rhs。源码有意保存二者的节点相对差，不要求逐词一致。第二 jet 又是现场有限 ODE/complex-step 算式的返回。因此不能仅在“同一节点位置”这一条件下把当前 quintic 叫原 RMS 所测曲线。

在单元 $[x_0,x_1]$、$h=x_1-x_0>0$，声明一个准确 cubic 参考 $C$：它通过原实际位置 $Y_0,Y_1$ 以及明确的 cubic 端点斜率 $D^C_0,D^C_1$。当前准确 quintic $Q_H$ 通过同一位置、实际 frozen 斜率 $D^H_i$ 和实际第二 jet $E^H_i$。置

$$
\Delta D_i=D^H_i-D^C_i,\qquad
\Delta E_i=E^H_i-C''(x_i).
$$

用 R249 的左端 cardinal basis 与右端反射 basis，准确有

$$
Q_H-C=
h[H_{10}(t)\Delta D_0+H_{11}(t)\Delta D_1]
+h^2[H_{20}(t)\Delta E_0+H_{21}(t)\Delta E_1],
\quad t=(x-x_0)/h,
\tag{514.14}
$$

其中

$$
\begin{aligned}
H_{10}&=t-6t^3+8t^4-3t^5,&
H_{11}&=-4t^3+7t^4-3t^5,\\
H_{20}&=(t^2-3t^3+3t^4-t^5)/2,&
H_{21}&=(t^3-2t^4+t^5)/2 .
\end{aligned}
$$

**证明。** 右侧在两端的值为零，一阶 jet 为 $\Delta D_i$，二阶为 $\Delta E_i$。次数至多五；共享六个 Hermite 条件的唯一性即给等式。它不假定 DDY 是某个准确解的导数。证毕。

沿 R249 §5 已证明的 Bernstein 常数，对任何固定向量范数有

$$
\begin{aligned}
\|Q_H-C\|_\infty
&\le \frac{2h}{5}(\|\Delta D_0\|+\|\Delta D_1\|)
 +\frac{h^2}{20}(\|\Delta E_0\|+\|\Delta E_1\|)=:E_0,\\
\|Q_H'-C'\|_\infty
&\le 2(\|\Delta D_0\|+\|\Delta D_1\|)
 +\frac h4(\|\Delta E_0\|+\|\Delta E_1\|)=:E_1 .
\end{aligned}
\tag{514.15}
$$

所有 $3M+2$ 分量共同进入；原两均值没有删除。需要更窄界时可沿 (514.14) 取完整向外 Bernstein，而非只看若干中点。

原 rounded SciPy 多项式与这里声明的准确 cubic 的差仍单列。若选取其已形成系数字词作为另一准确 cubic，则必须相应保端点值差；不能同时假定它等于准确 Hermite 并把形成误差置零。只有实际逐源/字词关系足够时，才能选用简化的 (514.14)。

取明确的准确有限系数 RHS $f_N(x,y)$。若在实际 $C$ 与 $Q_H$ 之间完整 tube 上有合法域和 Lipschitz 界 $K_N$，则恒等式

$$
Q_H'-f_N(x,Q_H)
=[C'-f_N(x,C)]+(Q_H'-C')
-[f_N(x,Q_H)-f_N(x,C)]
$$

给

$$
\|Q_H'-f_N(x,Q_H)\|_\infty
\le \eta_C+E_1+K_NE_0,
\tag{514.16}
$$

其中 $\eta_C\ge\|C'-f_N(x,C)\|_\infty$ 必须覆盖整个闭单元。这个局部准确 RHS 的 Lipschitz 前提不同于全 BVP 可逆性；本文没有取得它的数值，也没有把实际 complex-step J 当作受证的该常数。

从 (514.15) 可以看见真实 mesh 依赖，但不能由 $h$ 变小就宣告误差下降：$\Delta D,\Delta E,K_N$ 随实际新数据变化，差商或未付形成误差可能抵消表面的 $h$ 因子。所有精化比较仍按 R459 的真实同目标证据。

## 514.7 有限 RMS、角投影、数值目标与准确缺陷之间还缺哪些量

原 RMS 是归一残差在实际有限 Lobatto 规则上的数值读出；原 c6a 明确按状态分量求平方和，并加入冻结控制造成的节点残差。增加常数行不会把它按维数稀释。下列换算只能在其前提真实给出时使用。

若某一准确参考规则实际具有正权 $w_\nu$，且已付

$$
\sum_\nu w_\nu\sum_j |r_j(x_\nu)/(1+|f_j(x_\nu)|)|^2\le R^2,
$$

则每个原节点、每个分量的归一缺陷不超过 $R/\sqrt{w_\nu}$。若再有该归一函数在整个闭单元上的变化界或 Lipschitz 界 $L_j$，并且该规则填充距离为 $d_i$，才可推出

$$
\sup_{x\in I_i}|r_j(x)/(1+|f_j(x)|)|
\le R/\sqrt{\min_\nu w_\nu}+L_j d_i.
\tag{514.17}
$$

还须用实际全域 $|f_j|$ 界还原未归一缺陷。原浮点 RMS 到上述准确有限和的差、真实权/节点与后端版本、rounded curve 与所声明参考之差均不能省略。本文不为未绑定后端硬填权，也不把原 $10^{-6}$ 直接填成 $\eta_C$。

从完整系数缺陷到 world 向量，可直接复用 R249 §5 的 $L_0,L_1,L_2$ 完整 Fourier 权。设 $\mathcal W$ 为真实旋转坐标合成，$f_N$ 是声明的准确有限角方程。对未修补 prefix，

$$
\partial_x(\mathcal W Q_H)-V_g[\mathcal W Q_H]
=
\mathcal W[Q_H'-f_N(x,Q_H)]
+\{\mathcal W f_N(x,Q_H)-V_g[\mathcal W Q_H]\}.
\tag{514.18}
$$

第一个括号由 (514.16) 及完整 $L_0$ 权控制。第二个括号至少要保：

1. 原有限角投影与连续全角速度的差，含 aliasing/高模，不由有限 N 个角点域通过消失；
2. 已声明有限参考与真实 FFT/平方根/归一化/投影执行之间的形成误差；
3. numeric scalar/长度与准确同 C 的 $A,A_x,\mu$ 之间的差。固定十词不使 compiler 中点目标等于准确族；
4. 若所用参考不是当前完整节点/全部 core/参数，保实际输入关联差，而不能换成另一个便利 root 或轨迹。

这些项可以合并为一个真实闭域外包，也可按上列来源分开；都不能凭源码 SHA 或 FD 相符置零。R354 的完整表达式及其局部导数界给其中部分可复用代数工具，不证明这些新实际外包已经取得。

R249 投影、R416 patch 和完整 shared-B/collar 之后，应对最终 $F$ 直接形成 (514.7)/(514.5)，或明确加入修补的一阶 jet 及速度变动。后一条需要同一合法 tube 上的速度变化界，不能只把几何修补的节点幅度加到 $\delta$。已有 R249/R416 的连续 jet 差可复用，不用重复证明，也不能从旧场 metric 继承新场结论。

## 514.8 native 尾、两 mean、shared B 与完整闭面

原 native 的 $2\times10^{-9}$ 是它实际离散方程的归一残差政策；本论证没有更换该尺度。它不是 (514.5) 的 $\delta$，原因在真实后处理链中可逐项定位：

- R409 的实际 Cartesian 重放不是完整原 accepted shooting 轨迹的逐词副本；各段从自己的内端状态重启，记录 RK 步端点和段末差。
- 物理径向坐标、真实端口倍率、同 C 数值 geometry 与允许准确 C 族之间的关系都在参考定义中；不能把代表点称作一个已选共同准确根。
- 两个 mean 的逐段增量与反向累积改变完整高度及背景。它们不是可从 224 个 shape 行省去的附属项；完整 $z_0$ 仍保。
- 全 FFT 字词定义新的准确 Fourier 数据；水平二阶由真实差商给定。RK 误差、FFT 形成误差、二阶差商与准确 Hermite 导数之间没有因原 native 成功而自动消失。
- shared $B$、cuff collar、全角 cut patch 与固定帽的选择是完整闭场的一部分；$B$ 不被认定满足 $1+(B')^2=E_C$。

因此一条从 native 离散残差出发的单独误差常数仍需其完整离散稳定性、归一尺度恢复及上述重构差额。**本文的直接缺陷路线可不经过那条未知逆界：对已经实际形成的完整尾场和准确 $E_C$ 直接包围 (514.5)/(514.7)。** 它不把 native 求解省掉，也不冒充已经把 native 阈值换算完毕。

在 patch/collar 上保同一当前准确场；不能改用未修补 $T_0$ 的六 jet。所有真实 seam 的准确 $C^2$ 与目标 atlas 条件仍由原 R409/R416/R417 等负责；输运式不会补出缺失的 seam。

两反射 active sheets 的 Gram 在真实刚性反射下保持；速度支如需使用须相应变换。两帽目标是各自完整准确 Cartesian 帽图的诱导度量，因此原真实帽绑定已付时误差为零，不是把帽 tensor 置零。非对称 marker 不被假称旋转对称。

完整闭面的结论由所有有效闭片的上界取最大值。未访、无界或缺目标的片保持未付；不能仅由 prefix 或 native 的某个上界写全闭结论。固定首材料和全相位的转移直接沿 R459 的同时拉回/共轭命题；本结果不额外要求新的时间导数，也不从 $4/8/16$ 点插值推出全 $t$。

## 514.9 真实消费者的最小接点与参数合同

本结果可以在**既有**完整 metric 求值中增加一个可选输出，不需要独立重跑一遍全域审计，更不需要先通过一个新门。尚未发布或执行该接线；下表给的是经实际源码核对的最小调用合同。

| 所需量 | 实际现成来源或必须新增的真实形成 |
|---|---|
| 同一场的完整六 jet | R459 的 self.current.evaluate(piece, radial, angular, lower)，每个 world 分量槽为 $(F,F_x,F_q,F_{xx},F_{xq},F_{qq})$；保实际已生成 family/source |
| prefix 的 $A,A_x,\mu^2$ | self.current.target.closed_range 的全部准确三 jet；$k=$ self.current.target.length/self.current.target.numeric_length，$A_x=k a_s,\mu^2=k^2$；已登记 refined-leaf/coast view 时使用其实际对象 |
| tail/collar 的 $A,A_x,\mu^2$ | 当前闭径向区间 $A=r,A_x=1$；原同 C live query 的合法 $E_C$ 外包；不以 $B'$ 替代 |
| 完整 $\rho$ | 现 Kernel.angle_density 与当前完整材料正界；若用首材料 q，所有 field/target jet 先按原公共材料 API 同时拉回 |
| 锚 | 实际入口的全 $b$ 行/真实 core 和 R249 投影，或已绑定的准确 cuff 圆；保原文件身份及准确形成责任 |
| $\tau$、$r/\mu$ | 在同一已求六 jet 与目标上按 (514.4)–(514.7) 向外形成；正分母、明确支、原全部片范围单列 |
| 径向积分预算 | 明确锚坐标/方向、真实径向闭分片、每块完整角覆盖及 $\sum h_iT_i$；不能只复用没有这些字段的旧 ledger SHA |
| 全局结果 | 与原 R459 直接界可逐片取已合法界的较小者；只对完整覆盖给全域上界，实际资源未完成照原地址保留 |

无需新选一个默认 $\eta$。可复用原 interval_bits/sqrt_bits、空间计划、同 C 查询十一参数和原绝对钟；新增的是明确的锚选择及每个使用速度估计片的取向来源，不是新的求解阈值。原 bound/ledger 只在该片完整计算后提交，partial 与原 phase work 未完成分责。

如果以后实际源码形成了这一输出，应至少单列：

- 原 RMS/BC/native 数值与尺度、真正来源以及哪些只作历史记录；
- same_field_frenet_defect 与 angular_length_transport 的已付范围/未付地址；
- 实际 $q_a,\delta,T_i$、目标/材料严格下界及合法支来源；
- 当前 bound 是“当前场直接缺陷界”还是“原有限残差加完整形成项后的传递界”；
- (514.16)–(514.18) 中各项是否真正取得，不以 null 解释为零；
- 与完整 R459 直接广义谱界的合成、全部两片/两帽/全时间 scope。

源码/参数/run/必要结论可持久保留；逐 cell 大账仍只在 Actions 临时，必要摘要守单 body 90KB，不拆包，不从旧 SHA 恢复已清数据。本文只给条件结果和具体消费者合同，没有新 workflow、没有改现有 reader 或正在运行的源。

## 514.10 此次实际已付与仍未付

已付的是三条明确联系：

1. 同一准确当前场、准确目标与合法支上的速度恒等式，加上只需六 jet 的角长输运；不需要另一个未知等距参考。
2. 当前速度缺陷与入口/径向角长误差到完整相对 Gram 算子界的显式公式 (514.11)，保真正正分母、所有片与全族量词。
3. 原 BC、冻结 RHS 换用、cubic→quintic 重构及有限角/目标形成差额到这些缺陷的完整条件连接；不重复 R249/R416 已有修补引理。

没有取得任何实际 $\delta,T_i,\eta_C,K_N$，没有把 $10^{-6}$、$10^{-11}$、$2\times10^{-9}$ 变成一个已认证的 metric floor，也没有证明任意 mesh/M/t 精化自动严格降误差。已有 R459 的真实上下界比较仍可独立继续；本文缺失的常数不升格为 README 的新门。

### 来源

除上述结果链接，本文按实际公开源码读取了：

- [原物理 FFT Frenet RHS](../computations/geometry_20261114_r225_free_core_bvp.py)，23914 B，SHA256 a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08。
- [原完整 full-DN 求解](../computations/geometry_20261114_full_dn_solve.py)，30017 B，SHA256 c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162。
- [原完整常数增广边界](../computations/geometry_20261114_full_dn_augmented.py)，11311 B，SHA256 f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e。
- [原物理角完整边界](../computations/geometry_20261114_physical_test_boundary.py)，6269 B，SHA256 3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681。
- [R400 SavedPrefix](../computations/geometry_20261115_continuous_ten_frozen450_saved_prefix.py)，18759 B，SHA256 1c7a2e1c39b0066ae7149ef2e35ff6936a70601f0545369848f04716ad8b4520。
- [R400 准确前缀 target](../computations/geometry_20261115_continuous_ten_frozen450_prefix_metric.py)，32761 B，SHA256 011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84。
- [R409 径向重放](../computations/geometry_20261115_current_C_ten450_radial_readout.mjs)，23039 B，SHA256 5cc3134ed58aed45efea012219aa2e889624c47b41d5ee9f558da231806ab568。
- [R409 shared 构造](../computations/geometry_20261115_current_C_ten450_shared_field.py)，48583 B，SHA256 6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3。
- [R459 完整证据消费者](../computations/geometry_20261116_fixed_target_complete_metric_evidence.py)，62091 B，SHA256 494fea70b97404af2be8ef0f3d685fadc2f59c6a30ea3af771de98a56b868b05。
- [既有固定 C 工作/误差范围说明](../notes/2026-11-16-fixed-C-query-work-resolution-and-metric-error-scope.md)，14065 B，SHA256 e1fb934ba3e5e1a23f08dcc772aebc3bbb9fc3e4b8b0794c4d83259f0f5ef5a5。
