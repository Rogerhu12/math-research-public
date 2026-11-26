# R70. 从全周期相位列到补弧列的设计同伦

维护：Astra-held10-06bbeb39-20261126。2026-11-26 UTC。

本条给出独立 v4 相位族。它在中间设计阶段允许改变保护弧内的入口曲率，在终点严格回到 R68 的补弧族。证明其旋转闭合、反射对称、正则性、单位曲率列界、可复用的曲率插值守卫、每个有限阶的无核性，以及非零控制的正确 λ 导数。源码和小型实际 API 检查同时给出。

**本条没有证明完整 BVP 可逆或可解，没有给出新的接受场，也没有完成 λ=1、真实非线性 DN、共同 Cartesian 二jet、固定问题收敛、全时 reach 或 10% 指标。** 有限相位列无核与完整 BVP 的边界响应无核是不同命题。

## 1. 固定数据及新族

沿用 [R53](R53-material-flattening-homotopy-and-positive-domain.md) 的完整原支撑向量和固定目标曲率，记其真实材料相位为 $\phi^0_\lambda(u)$。完整支撑向量在此设计过程中固定，不因截断阶数重新拟合。沿用 [R68](R68-complement-interval-phase-controls.md) 的真实常数和窗口：

$$
P=\frac{2\pi}{3},\qquad c=P/2,\qquad
0<S<c,\quad L=c-S,\quad 0<b<L,
$$

$$
v(u)=\begin{cases}u,&0\le u<c,\\u-P,&c\le u<P,\end{cases}
\qquad
W(v)=S_9\!\left(\min\!\left(1,\max\!\left(0,\frac{L-|v|}{b}\right)\right)\right),
$$

$$
S_9(t)=126t^5-420t^6+540t^7-315t^8+70t^9,
\qquad D_1=\frac{630}{256b},\qquad \omega_j=\frac{j\pi}{L}.
$$

这里 $S,b$ 是所绑定输入的字面实数；$P,L,\omega_j$ 中的 $\pi$ 是真实常数。double 求值只是评价实现，不能把数值频率重新定义成另一目标。

定义全周期列、补弧列和混合列：

$$
A_j(u)=\frac{\sin(3ju)}{3j},\qquad
B_j(u)=\frac{W(v(u))\sin(\omega_jv(u))}{\omega_j+D_1},
\qquad
\Psi_j^\lambda=(1-\lambda)A_j+\lambda B_j.
\tag{1}
$$

在保护弧上把 $B_j$ 定义为零，再作 $P$ 周期延拓。对 $0\le\lambda\le1$，新相位为

$$
\phi_{\lambda,d}(u)=\phi^0_\lambda(u)+\sum_{j=1}^M d_j\Psi_j^\lambda(u).
\tag{2}
$$

执行入口沿用 R53 已有正 λ 域；数学式 (1) 可连续延拓到 λ=0。每个 M 严格取同一族的前 M 列，没有依 M 改频率、改窗、改归一化。无限系数可采用例如
$\sum_j(1+\omega_j^4)|d_j|<\infty$；这足以控制到四阶相位导数，有限列严格补零嵌入。

## 2. 同一基准、三重闭合、反射与 C² 依赖

$A_j$ 是 $P$ 周期奇函数。R68 已证 $B_j$ 的同样性质，且在保护弧内为零。故混合列也满足这两个性质。基准具有

$$
\phi^0_\lambda(u+P)=\phi^0_\lambda(u)+P,
\qquad \phi^0_\lambda(-u)=-\phi^0_\lambda(u),
$$

因而式 (2) 保持同样的相位规范。令

$$
T(u)=i e^{i\phi_{\lambda,d}(u)},\quad
\rho=e^{iP},\quad I=\int_0^P T(u)\,du,\quad
\Gamma(0)=\frac{I}{\rho-1},\quad
\Gamma(u)=\Gamma(0)+\int_0^uT(t)\,dt.
\tag{3}
$$

于是 $|\Gamma'|=1$，且
$\Gamma(u+P)=\rho\Gamma(u)$；三次旋转给完整 $2\pi$ 闭合和周长 $2\pi$。反射关系给
$T(P-u)=-\rho\overline{T(u)}$，所以 $I=-\rho\bar I$，从而 $I/(\rho-1)$ 为实数。再由 $T(-u)=-\overline{T(u)}$ 得
$\Gamma(-u)=\overline{\Gamma(u)}$。这固定了同一旋转中心和相位规范，没有另加随参数漂移的刚体运动。

窗在外端五阶消失；其内部平顶拼点至少 C4。R68 的补弧列全局 C4，全周期列光滑，所以混合相位至少 C4，曲线至少 C5，特别为 C2。这里不把整个相位称为 C5。

在每个固定有限 M 上，$\phi,\phi_u$ 连续依赖 $(\lambda,d)$。由

$$
\Gamma'=i e^{i\phi},\qquad
\Gamma''=-\phi_u e^{i\phi}
\tag{4}
$$

和式 (3) 的固定区间积分可知 $(\lambda,d)\mapsto\Gamma$ 连续地取值于 C2；在有限参数上也可按这些公式微分。带权无限系数空间中的绝对一致收敛给同一结论。若曲率 $\kappa=\phi_u$ 保持正，得到同规范的严格凸单位速闭核心。

在 $d=0$ 时，式 (2) 就是完整原基准。数值 provider 对 F、Fu、Fuu 明确委托同一个基准对象，位置增量用 expm1 积分，因此零控制不靠采样拟合、另建近似基准或换中心来实现。参数导数是新列的导数，不声称与 v3 参数 Jacobian 相同。

## 3. 中间入口自由度与 λ=1 的准确圆弧

在保护弧 $|u-c|\le S$，$W=0$，而固定目标曲率的 R53 基准满足

$$
\phi^0_\lambda(u)=(1-\lambda)\phi_{\rm original}(u)
       +\lambda\{c+k(u-c)\}.
$$

因此 v4 的保护弧内有

$$
\phi_{\lambda,d}(u)=(1-\lambda)
 \left(\phi_{\rm original}(u)+\sum_jd_j\frac{\sin(3ju)}{3j}\right)
 +\lambda\{c+k(u-c)\},
$$

$$
\kappa_{\lambda,d}(u)=(1-\lambda)
 \left(\kappa_{\rm original}(u)+\sum_jd_j\cos(3ju)\right)+\lambda k.
\tag{5}
$$

所以 λ<1 时可改变该弧内的入口曲率；λ=1 时所有控制在此处消失，曲率严格为 k，给出半径 $1/k$ 的准确圆弧。外部积分可能决定这个圆弧的圆心位置，但不改变其准确曲率和材料弧长。

对比 v2/v3：那些族的全部相位控制在保护弧内恒为零，因而其每个参数的入口相位、曲率变化在这里都为零。原 R53 支撑系数在 λ<1 的保护弧内一般有 $(1-\lambda)\partial_c\kappa_{\rm original}$ 的非零变化。v4 恢复一组能够作用在该区间内的中间相位方向，终点才收回补弧族。这是实际改变中间未知核心族，**不是**把失败的固定 δ 问题重命名，也不是仅重标度同一个有限 span。

它不证明原失败来自这个切向限制。现有失败的 Newton 返回也没有建立固定 δ 的连续兼容性障碍；原 δ 设计与此族均须按各自真实输入继续验证。

λ=1 时数值 `_basis` 直接返回补弧四 jet，而不是再做可能改变舍入的凸组合。故使用相同基准、控制和窗口时，终点数值族与 v3 逐位相同。尽管如此，v4 run 的 KIND 和 provenance 独立，实际 DN 或认证入口仍须显式识别它，不能只因终点公式相同就冒用旧接受记录。

## 4. 曲率列界及原守卫为何可保持

$\|A_j'\|_\infty\le1$。对补弧列，由 $0\le W\le1$ 和 $\|W'\|_\infty\le D_1$，

$$
\|B_j'\|_\infty
 \le\frac{\omega_j+D_1}{\omega_j+D_1}=1.
$$

凸组合给

$$
\|\partial_u\Psi_j^\lambda\|_\infty\le1,\qquad
\kappa_{\rm base,min}-\|d\|_1
 \le\kappa_{\lambda,d}
 \le\kappa_{\rm base,max}+\|d\|_1.
\tag{6}
$$

因此原始三角曲率域门可以不变。为核对其后备用的周期插值门，取原窗口导数界

$$
D_2=\frac{2520}{64b^2},\qquad
D_3=\frac{7560/16+5040/64}{b^3}.
$$

它们分别来自
$S_9''=2520t^3(1-t)^3(1-2t)$ 与
$S_9'''=7560t^2(1-t)^2(1-2t)^2-5040t^3(1-t)^3$
在 $[0,1]$ 上的直接上界。乘积求导给

$$
\|B_j'''\|_\infty\le C_j:={
 \omega_j^2+3\omega_jD_1+3D_2+D_3/\omega_j
 \over 1+D_1/\omega_j}.
\tag{7}
$$

关键的正差为

$$
C_j-\omega_j^2
 ={2\omega_jD_1+3D_2+D_3/\omega_j\over1+D_1/\omega_j}>0.
$$

由 $S>0$ 得 $L<P/2=\pi/3$，所以 $\omega_j>3j$。全周期列满足
$\|A_j'''\|_\infty=(3j)^2<\omega_j^2<C_j$。故

$$
\|\partial_u^3\Psi_j^\lambda\|_\infty
 \le(1-\lambda)(3j)^2+\lambda C_j\le C_j.
\tag{8}
$$

这正是曲率二阶导数列的界。现有共同 provider 使用
`baseline_second_bound + abs(d) @ C` 的插值守卫仍保守，原曲率下限、节点上限和域拒规则不需要改变。这里证明的是公式所需的真实上界；现有 floating guard 本身没有向外舍入，仍明确标为数值域门，不能当连续区间证书。

## 5. 每个有限阶的列无核，以及这不包含什么

固定 M 和 λ<1。若

$$
\sum_{j=1}^M a_j\partial_u\Psi_j^\lambda(u)\equiv0,
$$

则在保护弧的非空开区间内，式 (5) 给

$$
(1-\lambda)\sum_{j=1}^M a_j\cos(3ju)=0.
$$

有限三角多项式为实解析函数；在一个开区间为零便处处为零。由完整周期余弦正交性，全部 $a_j=0$。因此每个 λ<1 的有限曲率列严格独立。λ=1 时直接使用 R68 的补弧下界，仍严格独立，没有在此重复其证明。

同理相位列无核：其导数若为零可用上段，或者先用奇性排除非零常数。对完整规范曲线，若一阶核心二jet变化为零，则尤其 $\delta\Gamma'=-e^{i\phi}\delta\phi=0$，故相位变化为零，得到相同的有限参数单射。

对每个固定 M，连续 L2 Gram 矩阵随 λ 连续，且在紧区间 $[0,1]$ 上处处正定，因此存在某个正的最小特征值下界。此论证**没有给出有用的定量值，没有给出随 M 一致的界，也没有证明实际离散投影或 BVP Jacobian 的秩和条件数**。R68 的 λ=1 补弧多项式界不能自动搬到所有混合 λ。

## 6. λ 导数的交叉项和实际参数链

在固定 u、窗口和 d 下，

$$
\partial_\lambda\phi_{\lambda,d}
 =\partial_\lambda\phi^0_\lambda
   +\sum_jd_j(B_j-A_j),
\qquad
\partial_\lambda\kappa_{\lambda,d}
 =\partial_\lambda\kappa^0_\lambda
   +\sum_jd_j(B_j'-A_j').
\tag{9}
$$

沿 $d=d(\lambda)$ 还须加 $\sum_jd_j'\Psi_j^\lambda$ 及其 u 导数。`_basis_lambda_derivative` 仅返回式 (9) 的 basis 差；基准 λ 导数必须另外相加。当前 BVP 每步把 λ 作为给定设计参数，不把 λ 放进未知 p，因而原 p-Jac 没有遗漏一个 λ 未知列。未来若写 λ 预测器，不能漏掉式 (9) 的非零 d 交叉项。

继承的数值 gauge 始终为同一个 $q_g$，乘 Y 的仍是 $q_g$。旧正数 q 输入仅作为辅助坐标：

$$
q_{\rm aux}=q_g e^{p_0},\qquad
d_1=\sigma\log(q_{\rm aux}/q_g)=\sigma p_0,
$$

$$
s_j=\max(q_g^{j+1},10^{-9}),\quad
c_{{\rm legacy},j}=s_jp_j,\quad
d_{j+1}=\sigma c_{{\rm legacy},j}/s_j=\sigma p_j.
\tag{10}
$$

因此实际 p 参数链是 $d=\sigma p$；factory 对旧输入返回的链为 $\sigma/q_{\rm aux}$ 和 $\sigma/s_j$，再与原 BVP 链相乘。不能把 p0 重新解释成 δ，也不能把 q_aux 当物理振幅或乘 Y 的 gauge。保留现有辅助 q 域与 exp 预检，不用改域门来取得接受。

## 7. 实际入口、接受身份和未支付义务

独立源码在 `scripts/resume_20261126/`：

- `warm_homotopy_core_factory_v4.py` 定义式 (1) 及四 jet；
- `warm_fixed_m3_model_v4.py` 的 KIND 为 `warm-supported-material-phase-fixed-metric-v4`；
- `warm_zero_control_reexpression_v4.py` 只接受已通过完整原门的 v3 零控制锚；
- `warm_fixed_m3_step_v4.py` 每个新的 λ 步真实调用原 BVP；
- `warm_fixed_m3_continue_v4.py` 组织实际转换、步进、失败二分和必要升 M。

直接转换必须核实际 raw 的全部 p 为零、实际物理 phase controls 为零、λ 等于原锚值。它保持完整原支撑、δ、物理尾、原径向和材料 chart、gauge、固定字面 mean1168、原 raw 节点与场，并重新实际核完整两jet、raw 方程、RMS、BC、双角度量等式/门。它保留 `solver_invoked=false`、`solver_success=null` 和真实上游 solver provenance，不伪造一次新求解。非零 v3 控制不能原样交给 v4，也不能先置零声称同图。

后续每步原 RMS、scaled BC、physical BC、角点下限 `16*(3*M+1)` 及双角完整度量门均保持。必要升 M 时使用完整 exact-lift 的系数1补偿，不只补零投影。失败场不会晋为 accepted 锚；只有真实成功求解后单独 metric 未门才允许按原流程升 M。

[R63](R63-fixed-metric-and-solution-core-variables.md) 说明固定 δ 和物理 profile 时核心是未知解而不是目标 g 的参数；此处完整 g、mean1168 和 chart 均固定。但改变 λ 改变式 (2) 指定的入口族，仍称固定度量下的设计延续。只有 λ=1 固定后的真实同一完整 BVP 精化才可付固定问题收敛债；现有有限小检查没有支付这项债。

实际小检查及运行入口见 [v4 执行说明](../notes/2026-11-26-warm-v4-homotopy-entry.md)。旧 v2/v3 和共同源码没有被本条修改。真实非线性 DN、严格 core/mean oracle、全桥/全尾连续认证等入口必须按新 KIND 和完整定义显式接入；本条没有把旧场数值证书转贴过来。
