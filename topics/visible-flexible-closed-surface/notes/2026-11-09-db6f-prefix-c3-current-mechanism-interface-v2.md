# 有限正核与当前 twist 前缀的实际接口：可接入的公式及尚未支付的条件

作者：Astra-visible-flex-db6f0b0e / coupled_prefix，2026-11-09。

**状态：静态源码核对、完整条件推导及轻量有理账本，待独立审查。** 本稿不修改 flat17、当前目标 $g$、前缀/尾求解器或任何已冻结数据；没有运行新的前缀、角根、RK、优化或几何后端。有限正核本身的证明与标量账本已获 `tail-review-c3-core-proofs.md` 全文独审。这里研究的是它与实际机制的接口，不把该核心称为闭曲面解。

结论有明确的两面。单位速率有限正核确实符合现有物理 Frenet 机制的中央初值类型，且 flat17 在 $s=0$ 的平坦条件容许 $\ell=0$ 的 C² 镜像。**它不能直接替换当前 driver 的入口数值**：$N=7,r=3/20$ 的第一支持系数为 $357/1720>.124$，会触发当前 `WarpedBVP.initial` 的搜索保护；若再把它当作 `warp_reference_q`，现有单谐波角图也会失去可逆性。更关键的是，尚无它的全段正分支、真实尾 DN 匹配及闭合几何。

旧 $.9/1.1$ 高度预算只是乘积盒的充分条件，并非必要高度限制。下文给出一个有正中央带、正投影余量的具体凸包位置条件：同一个 $N=7,r=.15$ 核若被未来完整图满足，则允许总高度 $2.2$，仍有 $D<2.3$ 和 $\delta_{\rm hold}>.2D$。**位置条件不是 ODE 解；当前实际 M12 图也不满足这个高度条件。**

## 1. 三种角坐标及精确中央数据

使用三个不同的角：$\phi$ 是平面支持法向角，$\vartheta$ 是物理单位速率材料角，$\psi$ 是数值角图。$s$ 始终表示物理经向弧长。

有限核稿的凸体先旋转 $\pi/3$，使其第一支持系数为正。旋转后的支持函数写为
$$
h(\phi)=1+\sum_{j=1}^{14}c_j\cos(3j\phi),\qquad
c_j=\frac{2(1-r)(-1)^{j+1}b_j}{9j^2-1},
\qquad r=\frac3{20}.
\tag{1}
$$
$b_j$ 是该稿的有限平方 Fejér 系数。这次旋转不改变曲率半径、直径、相位像距离或任何下述预算。令
$$
\rho=h+h'',\qquad x(\phi)=h(\phi)n(\phi)+h'(\phi)t(\phi),
$$
$$
\vartheta=\sigma(\phi)
=\phi+\sum_{j=1}^{14}\frac{(1-9j^2)c_j}{3j}\sin(3j\phi),
\qquad \sigma'=\rho\ge\frac3{20}>0.
\tag{2}
$$
因此 $\gamma(\vartheta)=x(\sigma^{-1}(\vartheta))$ 是实解析、周长 $2\pi$ 的单位速率曲线，并且
$$
\gamma_\vartheta=t(\phi),\qquad
\gamma_{\vartheta\vartheta}=-\frac{n(\phi)}{\rho(\phi)},\qquad
\frac{860}{8833}\le\kappa\le\frac{20}{3}.
\tag{3}
$$
这些正是 `notes/fixed_metric_mode3_core.py` 的 `normal_geometry`、`arc`、`evaluate` 所用公式。其 `parameter_derivatives` 也有直接核对：对 $m=3j$，固定材料角求导，
$$
\partial_{c_j}\gamma
=\cos(m\phi)n(\phi)-\frac{\sin(m\phi)}m t(\phi).
\tag{4}
$$
证明是将固定 $\phi$ 导数 $\cos(m\phi)n-m\sin(m\phi)t$ 与由 $\sigma$ 反解得到的 $\rho t\,\partial_{c_j}\phi$ 相加；后者的切向系数是 $(m^2-1)\sin(m\phi)/m$。因此不是把法向角平移误当成单位速率参数。

这里的 14 模只表示 (1)–(2) 的法向角公式。$\sigma^{-1}$ 以及 $\gamma(\vartheta)$ 一般不是 14 模材料 Fourier 多项式。当前 `initial` 还会将精确曲线减去精确圆背景，再投影到 $\psi$ Fourier 基；必须重新计算该投影误差，不能直接继承解析核心的精确 metric、曲率或位移数字。

## 2. 与物理 Frenet 方程逐式对应

设 $F(s,\vartheta)$ 的每条角曲线正则、曲率非零。定义
$$
\lambda=|F_\vartheta|,\qquad
T=F_\vartheta/\lambda,\qquad
N=T_\vartheta/|T_\vartheta|,\qquad
\kappa=|T_\vartheta|/\lambda,\qquad B=T\times N.
$$
目标活动带 metric 为 $ds^2+a(s)^2d\vartheta^2$。当前物理法向速度正是
$$
F_s=V=\alpha_F N+\beta_F B,
\qquad
\alpha_F=-\frac{a'}{a\kappa},\qquad
\beta_F=\sqrt{1-\alpha_F^2}>0.
\tag{5}
$$
`950f-prefix-warped-bvp.py` 与 `950f-prefix-adaptive-chart-bvp-v2.py` 的 `frame` 使用这个分支；符号 $\alpha_F$ 不表示尾 momentum root 的另一个 $A$。

**条件等距性证明。** 若一个足够光滑的真实解在全段满足
$$
a>0,\quad \lambda>0,\quad \kappa>0,\quad |a'|<a\kappa,
\tag{6}
$$
则 $|F_s|=1$ 且 $F_s\cdot F_\vartheta=0$。由 Frenet 关系，
$$
\lambda_s=T\cdot\partial_\vartheta V
=-\alpha_F\lambda\kappa=\frac{a'}a\lambda.
\tag{7}
$$
若中央 $a(0)=1$、$F(0,\vartheta)=\gamma(\vartheta)$，则 $\lambda(0)=1$，所以 $\lambda=a$，恰得共同目标 metric。核心的非圆形并不改变这个初值论证。

(7) 不证明解存在到尾切口。原曲线方程含角向二阶导数；有限 Galerkin 系统的局部 ODE 正则性不能直接当成无限角向方程的存在定理。离散 `project` 只匹配投影后的速度，也不自动保留 (7) 的点态等式。实际图的连续 metric 证书及 README G5 仍须新做。

核心的 $\rho_{\min}$ 控制最大曲率，而 (6) 中危险的方向是**最小曲率**。本例 $\kappa_{\min}=860/8833\simeq.09736$；flat17 的速度平台是 $.17$ 和 $.18$。如果假想截面只作同形缩放，则条件要求 $|a'|\rho_{\max}<1$，这些平台会违反它。真实解会改变截面及空间 Frenet 标架，故这不是全段失败证明；它精确说明不能用中央 $\rho\ge.15$ 代付全段分支正性。

## 3. 当前实现的两个具体入口限制

### 3.1 第一支持系数保护

本例 $b_1=42/43$，从 (1) 得
$$
c_1=\frac{357}{1720}\simeq.20755814.
\tag{8}
$$
当前 `WarpedBVP.initial` 明确要求实际第一支持系数 $10^{-7}<q<.124$；其父类还要求正的 seed gauge 小于 $.2$。即使保留合法 gauge 再通过参数 $p_0$ 令 $q=q_{seed}e^{p_0}$ 达到 (8)，前一个保护仍会拒绝。

这个 $.124$ 是当前数值入口的搜索范围，不是“第一系数大于 $.125$ 就不凸”的几何定理。本例其它支持模使 $\rho$ 严格正，已有解析证明。四个已核有限核例子的正向第一支持系数都至少 $.2$，不能作为原 driver 的直接参数替换。本文没有修改这个保护或绕过原构造器。

`PlanarSupportCore` 本身容许多个支持系数，但还用采样及全导数界核验 `rho_lower`，并数值反解弧长；它的实际浮点检查与投影仍是未来输入的一部分。解析式 (2) 是几何定义，不应拿它静默跳过现有数值检查。

### 3.2 数值角图不等于核心的材料角

当前图为
$$
\Theta(s,\psi)=\psi-e(s)\sin(3\psi)/3,
\qquad \chi=\Theta_\psi=1-e(s)\cos(3\psi)>0.
\tag{9}
$$
$e(s)$ 由冻结样条、参考值 $8q_{warp}$ 和端部平滑截止共同给出。若错误地取 $q_{warp}=c_1$，则 $8c_1=357/215>1$，连中央角图都不再可逆。参考 warp 可以独立于实际支持系数，保留原合法参考值不会产生这个特定错误；但这不解决 (8) 的实际支持保护，也不保证有限模误差或 BVP 可解。

在 (9) 下，固定 $\psi$ 的速度是
$$
\partial_s(F\circ\Theta)=V+
\frac{\Theta_s}{\Theta_\psi}\partial_\psi(F\circ\Theta).
\tag{10}
$$
原 adaptive `frame` 正是将这个切向运输项加到 (5)，而不是把 $\psi$ 当物理单位速率角。切口的 $\Theta=\psi$ 且差的前两阶 jet 为零，所以原尾端匹配无需额外角链式项。

若将来单独实现更合适的角图，一个明确的正性候选是
$$
\Theta_{new}(s,\psi)=(1-\zeta(s))\sigma(\psi)+\zeta(s)\psi,
\quad 0\le\zeta\le1,
\quad \partial_\psi\Theta_{new}=(1-\zeta)\rho+\zeta\ge\min(r,1)>0,
\tag{11}
$$
其中 $\zeta=0$ 在入口邻域、$\zeta=1$ 在切口邻域。它在入口直接使用有限法向公式，并在切口恢复材料角；用 (10) 的完整链式规则可保持同一个物理 $g$。这只是一个未实现的数值坐标选择，既非新的解，也不使现有“精确圆背景加有限扰动”表示自动变成有限精确表示。当前 frozen chart 不变。

## 4. 中央镜像可接，但不是任意强曲线已经闭合

当前 `db6f-prefix-flat-profile.py` 安装的 flat ramp 在入口有
$$
a(0)=1,\qquad a'(0)=a''(0)=0.
\tag{12}
$$
平面正向曲线的 $N=-n$、$B=e_z$。对满足 (5) 的光滑解，(12) 给
$$
F(0,\vartheta)=(\gamma(\vartheta),0),\quad F_s(0,\vartheta)=e_z,
\quad F_{ss}(0,\vartheta)=0.
\tag{13}
$$
最后一式用 $\alpha_{F,s}(0)=0$，以及 $F_{s\vartheta}(0)=0$ 导出的 $B_s(0)=0$。所以定义下半部
$$
F_-(s,\vartheta)=\operatorname{diag}(1,1,-1)F_+(-s,\vartheta)
\quad(s\le0)
\tag{14}
$$
得到同一个 C² 中央接口。非零平面角切向与 $e_z$ 保证该接口浸入。若使用数值角图，入口 $\Theta_s=0$，$\Theta_{ss}$ 可能只增加一个平面切向二 jet；镜像所需的高度二 jet 仍为零。

`db6f-root-mirror-hermite.py` 对有限图实际施加的是这些镜像奇偶条件，特别是将入口高度二 jet 精确设零。它的定义可在新数据上重新使用，但这是有限表示修正，仍要重新算 metric；旧数值误差界不会转移到新核心。

$\ell=0$ 只表示两半部在此直接镜像，不另加中央柱段。它没有删除现有外向/内向 meridian 周期、桥、尾或帽的高度。

### 零投影泄漏与外向 flat ramp 的局部冲突

还有一个具体的、带正则性前提的限制。令 $T_u=\delta/[v_u(1-\varepsilon)]$，$\varepsilon$ 为 ramp 比例，$\eta_r$ 为 ramp_eta。在入口第一小段直接展开原 `turn_ramp`，
$$
a(s)=1+A_4s^4+O(s^5),\qquad
A_4=\frac{v_u}{4T_u^3\varepsilon^3(1-\eta_r)\eta_r^2}>0.
\tag{15}
$$
若真实分支在此足够光滑，可以把 (5) 连续求到四阶，则
$$
F_{ss}(0)=F_{sss}(0)=0,\qquad
F_{ssss}(0,\vartheta)=a''''(0)\rho(\phi)n(\phi),
$$
$$
F(s,\vartheta)=(\gamma(\vartheta),s)+A_4s^4(\rho(\phi)n(\phi),0)+o(s^4).
\tag{16}
$$
理由是前三阶尚未产生角向变化，故相应的 $B$ 导数为零；首个非零平面项来自 $\alpha_F N$。在任一中央支持法向取内积，(16) 严格超出 $K$ 的支持值。因此对这种光滑外向分支，整个初始图的投影精确包含于中央 $K$ 的**零泄漏**假设不能成立。

这不是任意 C² 分支的高阶 Taylor 定理，也不是存在性或全局失败结论。它解释了为什么下文采用 $K+\eta B_2$ 的正余量；任何固定 $\eta>0$ 在足够小的中央邻域不会与 (16) 冲突。全段投影界仍未证明。

## 5. 实际边值未知量、桥与共同 cut

当前固定 $g$ 的 BVP 并非“指定所有中央支持系数后自动接尾”。它有 $M$ 个自由支持参数：$q=q_{seed}e^{p_0}$ 与 $c_j=p_{j-1}\,pscale_{j-1}$，$j\ge2$；用 $M$ 个真实尾端条件决定这些参数。记原非均值高度切口为 $H(c)$，真实 slope DN 为 $S(H)$，则核心方程具有
$$
\Phi(c;g)=S_{prefix}(c;g)-S(H_{prefix}(c;g))=0
\tag{17}
$$
的形式。将 (1) 的全部 $c_j$ 固定，只证明了中央曲线，并没有支付 (17)。可以把有限正核当作未来初猜或目标邻域，但最终支持系数的变化必须重新验证其强位移与凸性预算。当前小幅支路或某个固定点角根的唯一性不提供这个全局边值根及其非退化性。

原桥由实际 tail cut 固定：$c=.6$、$w_c=.5$，$\sigma_b=\operatorname{sgn}(c-1)=-1$。这里 $c$ 是保存 binary 数对应的精确值 $5404319552844595/9007199254740992$，不把它另换成 $3/5$；$w_c=1/2$。在源码的实数模型中
$$
p(t)=p_t(3t^2-2t^3)+L_b p_s(t^3-t^2),\quad
p_t=\operatorname{atan2}(1,w_c),\quad
p_s=-\frac{\sigma_b w_{r,c}}{(1+w_c^2)^{3/2}},
$$
$$
L_b\int_0^1\sin p(t)\,dt=1-c,\quad
a=1+\sigma_bL_b\int_0^t\sin p,\quad a'=\sigma_b\sin p.
\tag{18}
$$
正式共同 metric 使用已有 exact-bridge 根定义及弧长变换，而不是把数值根与精确根当成同一常数。保留原 $g$ 时不能把 $L_b$、速度或尾 cut 自由改短。

在切口角图两 jet 已为恒等的条件下，`TailMixin` 的物理标度为
$$
H_j=\sigma_b q_g y_{Z,j}(L),\qquad
q_g y'_{Z,j}(L)=\frac{S_j(H)}{\sqrt E},\qquad E=1+w_c^2.
\tag{19}
$$
$q_g$ 是固定数值 gauge，不是可任意替换的实际支持幅度。$r_s=\sigma_b/\sqrt E$、$r_{ss}=-E_r/(2E^2)$；反射整个高度后，第二 jet 要求
$$
q_g y''_{Z,j}(L)=\sigma_b\left(\frac{T_j(H)}E+S_j(H)r_{ss}\right).
\tag{20}
$$
均值 first/second 使用同样的完整高度关系。它们由 `seam_audit` 明确记录，不能只匹配非均值的第一导数。原真实 DN 仍需在所用有限问题中收敛且保持 $D,S,A$ 正分支，并通过原 Jacobian/audit；这也不自动支付无限极限。

现有 `db6f-root-common-cut-v2.py` 对完整 Cartesian 两 jet 做精确 Hermite 公共端迹修正。上尾是
$$
T(r,\vartheta)=
\left(r e^{i\vartheta}+V_h(r,\vartheta),\ H_c+\int_r^c w(\rho)\,d\rho-V_z(r,\vartheta)\right).
\tag{21}
$$
若保存前缀坐标 $u=\lambda_b s$，其目标端 jet 是 $T$、$(r_s/\lambda_b)T_r$、$(r_s^2T_{rr}+r_{ss}T_r)/\lambda_b^2$。完整 Fourier 端迹包含所有角导数与混合导数。此公式可复用，数值端迹与误差证书不可复用；若该修正不随同一问题的加密趋小，就仍不能支付 G5。

## 6. 固定帽和相位机制需要哪些真实条件

若最终活动带确实具有共同轴对称目标 metric，活动部分使用
$$
F_\alpha(s,\vartheta)=R_\alpha F_0(s,\vartheta-\alpha),
\quad 0\le\alpha\le2\pi/3.
\tag{22}
$$
材料角平移与空间旋转共同给原活动 metric；中央像包含 $R_\alpha\Gamma$。这不要求中央曲线本身轴对称。

但是要让另加的帽保持逐点固定，cuff 处必须是轴对称圆领的**全部 Cartesian 两 jet**，而非只有圆形位置。对当前平帽接口，现有尾 collar 把扰动及其前两阶径向导数精确降为零，背景还需 $w=w_r=0$；一般固定轴对称非平帽不必满足这两个零条件。这些性质才使 (22) 与固定帽 C² 拼接，并使相位在 C² 拓扑连续。未来新数据仍须支付全圆领与完整闭图的 metric、嵌入及曲率。

本例中央的实际二 jet 局部主曲率为 $1/\rho$ 与 0，支撑 $F\cdot n=h\ge(1+r)/2$；这只给中央的好余量。全闭面仍要按 R10 的完整假设控制全域支撑及实际主曲率，例如当 $D<2.3$ 时 $\sigma_0\ge.069$、$K_0\le1/.069$ 足以给该工具所需的全 reach 下界。平面或带边柱核的 reach 不能代替这个全域结论。

未闭柱核自身的全部像刚体全等，$\delta_{\rm E}=0$，且无固定非空开材料片。未来固定帽的真实握持区大小以及破坏全部 $\mathrm E(3)$ 全等的矩/其它不变量必须另证。当前 R16/R21 的体积矩数值属于旧完整图，不能移到本例。

## 7. 当前实际高度不是 $\ell$ 的自由旋钮

R21/R25 的同一 M12 图已取 $\ell=0$。其闭预算的两固定轴心点间距下界为
$$
L_{axis}=\frac{7977247853389765}{2251799813685248}
>3.542609695989968.
\tag{23}
$$
这些点在同一轴上，故 (23) 同时是该图总 $z$ 跨度及整体直径的下界。它来自相同共同 cut 高度和已闭帽的位置，不是松球盒的上界。仅把中央解析核换成新公式、而保留这些实际帽坐标，不能得到下文的高度 $2.2$ 条件，更不能得到原乘积盒的 $.9/1.1$ 条件。

现有数值图的均值高度由原 `height_integral` 得到。在 $\psi$ 表示中它积分的是 (10) 的均值 $\langle W_z\rangle_\psi$；切口角图恒等时才与物理角均值直接相同。它不是一个可独立调小的 BVP 参数。全图刚体平移不改变高度跨度；单独移动上下帽会破坏接缝，除非重新给出满足方程的新过渡。

这个事实不证明“相同 $g$ 的任何其它分支高度都至少 (23)”。$\langle W_z\rangle$ 依赖解，新的真实分支或新的度量设计可能给不同高度，目前没有相应存在或不可能性证明。整体缩放也不能改善问题：$\Delta,D,\rho$ 和总高度一起缩放，归一比例不变。

## 8. 一个允许总高度 2.2 的完整条件位置引理

本节保留 $N=7,r=3/20$，不作参数搜索。已有精确有理账本给
$$
\Delta>.462868276536=:\Delta_-,\qquad
d:=\operatorname{diam}K\le2.112793419185=:d_+.
\tag{24}
$$
设 $B_2$ 为二维闭单位圆盘。取
$$
\eta=\frac1{1000},\qquad a=\frac1{10},\qquad
c_*=\frac3{10},\qquad H_*=\frac{11}{10},
$$
$$
C=(K+\eta B_2)\times[-a,a],\qquad
D_\pm=c_*B_2\times\{\pm H_*\},\qquad
\mathcal E=\operatorname{conv}(C\cup D_+\cup D_-).
\tag{25}
$$
$a$ 在本节仅为中央半高度，不是前面 meridian 函数 $a(s)$。它为中央曲线留出正的垂直带；$\eta$ 则留出正的水平余量。没有假定从中央曲线立即沿收缩锥面移动。

### 8.1 严格的原点半径界和投影包含

对任意紧凸体，
$$
\max_{x\in K}|x|=\max_{|u|=1}\max_{x\in K}x\cdot u=\max h.
\tag{26}
$$
这使用紧集上最大值的交换，不是把 $|h n+h't|$ 错估成 $|h|$。由 $0<b_j\le1$ 及
$$
\sum_{j\ge1}\frac1{9j^2-1}
\le\frac18\sum_{j\ge1}\frac1{j^2}<\frac14
$$
可得
$$
R_K:=\max_K|x|\le\frac{3-r}{2}=\frac{57}{40}=1.425,
\qquad h_{\min}\ge\frac{1+r}{2}=\frac{23}{40}.
\tag{27}
$$
上面的级数粗界可以仅用 $1/j^2<1/[j(j-1)]$（$j\ge2$）望远镜求和；不需数值三角或 $\pi$ 近似。旋转 (1) 不改变极值。于是 $c_*B_2\subset K$。投影与凸包交换，故
$$
\pi_{xy}(\mathcal E)
=\operatorname{conv}(K+\eta B_2,c_*B_2)=K+\eta B_2.
\tag{28}
$$
同时 $c_*B_2\times[-H_*,H_*]\subset\mathcal E$。所以半径不超过 $c_*$、高度在该范围内的固定帽及标记可以满足这个位置包含条件；这里没有构造它们的 metric 或接缝。

### 8.2 三类点对及凸包直径

在生成集合 $C\cup D_+\cup D_-$ 内，任意点对属于下面三类，相应平方距离上界为
$$
Q_{CC}=(d_++2\eta)^2+(2a)^2,
$$
$$
Q_{DD}=4(c_*^2+H_*^2)=\frac{26}{5},
$$
$$
Q_{CD}=(R_K+\eta+c_*)^2+(H_*+a)^2.
\tag{29}
$$
同一端盘内的点对也被 $Q_{DD}$ 覆盖。所有常数以有理数计算，严格得到
$$
Q_{CC}<\frac{26}{5},\qquad Q_{CD}\le4.419076<\frac{26}{5},
\qquad \frac{26}{5}<\left(\frac{23}{10}\right)^2.
\tag{30}
$$
凸包不会增大直径：若 $x=\sum_i a_i x_i$、$y=\sum_j b_j y_j$ 为有限凸组合，则
$$
|x-y|=\left|\sum_{i,j}a_i b_j(x_i-y_j)\right|
\le\sum_{i,j}a_i b_j|x_i-y_j|
\le\operatorname{diam}(C\cup D_+\cup D_-).
$$
一般闭凸包用极限得到相同界。因此
$$
\operatorname{diam}\mathcal E\le\sqrt{26/5}<2.3.
\tag{31}
$$
两相反端盘的相反边缘点事实上达到 $Q_{DD}$，但应用只需上界。

### 8.3 转移到未来完整族的精确假设

设未来已构造的完整初始像 $S_0$ 满足 $S_0\subset\mathcal E$，包括全部过渡、帽和标记；某个时刻 $S_{\pi/3}$ 包含 $(R_{\pi/3}\Gamma,0)$。还须独立给出满足 README 的固定握持区。选择实现半相位支持差 $\Delta$ 的法向 $u$，以及相应的旋转核心支持点 $p$。由 (28)，所有 $x\in S_0$ 满足
$$
(p-x)\cdot(u,0)\ge\Delta-\eta.
$$
于是对**完整图**有
$$
D=\operatorname{diam}S_0\le\sqrt{26/5}<2.3,
\qquad
\delta_{\rm hold}\ge\Delta-\eta>.461868276536>.46>.2D.
\tag{32}
$$
没有把平面直径 $d$ 替代 README 的 $D$。如果活动带像按 (22) 旋转，而固定帽在上述中心圆柱内，则每个相位还包含于相应的 $R_\alpha\mathcal E$，相同点对界继续有效；这不代付全相位嵌入和 reach。

这里 $2H_*=2.2$，明显大于先前乘积盒的 $.9$。因此高度预算在几何不等式层面没有被迫只能用极矮的整体；代价是必须实际证明经向位置收缩到 (25) 的凸包，而不是将全平面宽度与全高度同时取最大。中央有正带与正余量，所以 (13)、(16) 的局部 jet 不构成对 (25) 的即刻反例。**仍未证明任何满足 (17) 的解落在 (25) 内。**

## 9. 可复现范围和实际剩余门

新的纯 Fraction 程序为 `scripts/db6f-prefix-c3-mechanism-conditional-budget.py`。它仅读取冻结有限核账本及同一 M12 闭预算，核 (8)、(24)、(27)、三类平方距离、(32) 的严格余量和旧轴心高度超过新 $2.2$。实际作者执行 receipt `65e22d`、exit0；没有调用任何数值几何接口。

```bash
python scripts/db6f-prefix-c3-mechanism-conditional-budget.py \
  --out notes/2026-11-09-db6f-prefix-c3-mechanism-conditional-budget-NEW.json
```

固定输入身份、本文所读源码及已有证明见同 stem 的 `sources.json`；完整路径是 `notes/2026-11-09-db6f-prefix-c3-current-mechanism-interface-v2-sources.json`。旧图的高度、正支撑及 metric 数值只用于识别旧对象，不作为新候选证书。

实际尚未支付的条件具有明确接口：中央多模数据的合法新入口与足够精确投影；(6) 的全段正性及 (17) 的真实全局边值解；(19)–(21) 的完整端迹与逐次趋零的修正；cuff 全二 jet 与固定帽；真实闭图位于 (25) 的连续位置界；全时浸入、嵌入、reach、固定握持区及非全等；以及原 README 的同 $g$ 加密与独立完整重跑。这个清单不是新任务门槛，只定位现有完成标准中不能由平面核心证明替代的部分。

可确定的直接替换失败点是当前 $.124$ 入口保护与误设 warp 后的角图不可逆；可确定的正面接口是精确单位速率中央数据、条件共同 metric、$\ell=0$ 的 C² 中央镜像，以及具有严格余量的完整位置预算。本文不改变正在继续的 flat17 主线研究。
