# 当前 flat-cut 度量的完整圆形基准及增量方程

日期：2026-11-12。范围：现有 R136、R156 的直接推论及可执行的表示设计；不改变当前主求解的输入或方程，不声称非圆分支存在。

## 1. 结论与既有实现

当前不可变候选 `2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json` 的 SHA256 为 `7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1`。取所有物理 bump 参数 $\delta=0$，它确实具有一个完整、准确的回转面解。中央曲线为半径 $a_0$ 的圆；切口处三个第二基本形式分量全部为零，并与零控制的准确平面尾带相接。本说明补出的严格全段界是

$$
\max(|\kappa_1|,|\kappa_2|)<7<7.2.
$$

这项构造已有来源，不能称为首次找到圆形背景。

| 已有对象 | 已经提供的内容 | 对当前任务的适用边界 |
| --- | --- | --- |
| [R136 §7](../results/R136-peak-spacer-prefix-continuous-radius-and-outer-design-domain.md) | 当前准确标量候选的完整回转面、共享两 jet 和平切口 | 正是本说明采用的基准；原文的全段曲率数值只是采样，本次从其已闭严格包补出连续界 |
| [R156](../results/R156-terminal-brake-trace-regularity-and-round-tail-reference.md) | 当前 terminal brake 的准确圆形 $n_R,l_R$ 与零尾弧性质 | 是上述全段基准在最后一段的特例；其中加入非零 tail 的参考一般不是完整 Codazzi 解 |
| [BalancedCurvatureCore 定义](2026-11-12-fd2d-metric-balanced-curvature-core-definition.md)、[实现](../scripts/fd2d_balanced_curvature_core.py) | `base_kind='circle'` 在固定材料图中的准确圆及保持周期闭合的中央曲率参数 | 零参数时无需用有限 Fourier 系数抵消原非圆种子 |
| [旧 circle 分支入口](../scripts/fd2d-gc-bvp-design-start.py)、[small01 原生场说明](2026-11-12-fd2d-metric-gc-native-field-and-inlet-proof.md) | 旧 p148 物理候选已经采用圆基准、小 gap 和外 coast 参数 | 其真实解、线性端口及共振条件不能移给当前 flat-cut 的新 $g$ |
| [LogShapeGC](../scripts/fd2d_gc_logshape.py)、[稳定背景相消](../scripts/fd2d_gc_logshape_stable.py) | $n_r=\sqrt{1-a_s^2}/a$ 的全段背景归一和 `expm1` 相消 | 此 log 图要求 $n_r>0$，不能直接覆盖当前 $n_r=0$ 的平切口 |
| [旧回转面 body 消费者](../scripts/fd2d-gc-body-background-check.py) | 独立旋转面位置与标架的有限核对 | 对象为旧 p148，并非本次新 ODE 或当前全域几何证书 |

本次检索未发现已闭的、同时覆盖当前平切口和当前 raw 三场框架的完整圆形增量 provider。现有 raw provider 虽允许 circle 中央曲线，其完整 lifting 仍包含截断 seed、current-radius tail 及非圆 frozen-coast 参考；只更换 `base_kind` 不会使零 raw correction 成为这里的完整圆形解。

## 2. 完整准确解及两端数据

沿用 R136 的准确物理经线坐标 $s$、半径函数 $a(s)$ 和材料角 $u$，令

$$
g_0=ds^2+a(s)^2du^2,\qquad a_s=\sin\phi,
\qquad b=\cos\phi\ge0.
$$

在保留的 Hermite feedback 段，定义 $\phi=\arcsin a_s$；R136 已证该段 $|a_s|<1$。后续采用候选本身定义的相位，而不是再对数值 $a_s$ 求反三角函数。准确相位范围是 $[-\pi/2,.3]$。定义

$$
z_0(s)=\int_0^s b(t)\,dt,\qquad
X_0(s,u)=(a(s)\cos u,a(s)\sin u,z_0(s)).
$$

记 $e_r=(\cos u,\sin u,0)$、$e_\theta=(-\sin u,\cos u,0)$，则

$$
e_1=\sin\phi\,e_r+\cos\phi\,e_z,
\qquad e_2=e_\theta,
\qquad N=e_1\times e_2=-\cos\phi\,e_r+\sin\phi\,e_z.
$$

直接微分得到 $E=1,F=0,G=a^2$。采用现有源的分量顺序 $(n,m,l)$，第二基本形式的正交分量为

$$
\boxed{n_0=\frac{\cos\phi}{a},\quad m_0=0,\quad l_0=-\phi_s.}
\tag{1}
$$

Hermite 段等价地使用

$$
b=\sqrt{1-a_s^2},\qquad n_0=b/a,\qquad l_0=-a_{ss}/b.
\tag{2}
$$

式 (2) 只在该段的已证正 $b$ 域使用。切口不计算 $0/0$。相位段使用式 (1) 及准确 terminal 标记 `exact_endpoint_phase='-pi/2'`。

令 $c_0=a_s/a$、$K_0=-a_{ss}/a$，则

$$
l_0n_0=K_0,
\qquad (n_0)_s=c_0(l_0-n_0),
\qquad (m_0)_s=0=\frac1a(l_0)_u-2c_0m_0.
\tag{3}
$$

第二式由 $(\cos\phi/a)_s=-\sin\phi\,\phi_s/a-\cos\phi\,a_s/a^2$ 直接得到。因此这是一组完整 Gauss–Codazzi 解，不是将正交标架当作等距性的替代验证。

中央柱上 $a=a_0,\phi=0$，故 $n_0=1/a_0,m_0=l_0=0$，$X_0(0,u)=a_0e_r$、$e_1=e_z$。`BalancedCurvatureCore(coefficients=0,base_kind='circle')` 正好给出同一曲线和定向。在固定 seed 图 $u=U_{\rm seed}(\xi)$ 中，它仍是同一物理圆，不要求材料角与计算角相等。

切口半径为 $r_c=4/5$，terminal 相位和相位导数准确等于 $-\pi/2,0$。因此

$$
X_0(s_c,u)=(r_c\cos u,r_c\sin u,Z_0),\quad
e_1=-e_r,\quad e_2=e_\theta,\quad N=-e_z,
\quad(n_0,m_0,l_0)=(0,0,0),
\tag{4}
$$

其中 $Z_0=z_0(s_c)$ 是完整积分所得的真实高度。不能将它擅自设为 $1.25$。生成报告中约 $1.2975177376030373$ 的显示值是已有有限求积诊断，不在本说明中升级为严格位置区间。

令准确平尾的全部 Bernstein 控制为零，则其弯曲角和曲率恒零；按同一内向 $s$ 定向，整个 $r\in[.32,.8]$ 平尾在高度 $Z_0$ 上与 (4) 接合。R136 的共享两 jet、相位连续和 terminal $\phi_s=0$ 保证实际曲面至少 $C^2$。这里没有要求第二基本形式具有径向二阶连续性，也没有引入额外 $C^3/C^4$ 曲面条件。

## 3. 全段主曲率严格小于 7

由于 $m_0=0$，主曲率正是 $n_0,l_0$。R136 已证全域 $a\ge4/5$，因此

$$
0\le n_0\le\frac54.
\tag{5}
$$

本次 [有理消费者](../scripts/fd2d_round_prefix_curvature_bound.py) 只读取已经闭存的 [R136 精确标量包](2026-11-12-fd2d-peak-spacer34-radius-certificate-02.json)，核其候选和源身份，再作以下精确有理运算。没有重求 ODE，也没有通过加密采样替代区间界。

保留的 51 个 Hermite 片已经给出速度与加速度的 Bernstein 界。分别汇总为 $V,A$，对准确 binary64 编码和准确书写十进制编码，消费者均直接核得

$$
0\le a_s\le V<1,\qquad |a_{ss}|\le A,
\qquad A^2<4(1-V^2).
$$

由式 (2) 可得全部反馈片 $|l_0|<2$。这里使用有理平方比较，没有把浮点开方作为证明。

普通 cubic phase bridge 的 $\phi_s$ 是二次 Bernstein 多项式，三个控制值为

$$
\phi_s(0),\quad
\frac{3(\phi(1)-\phi(0))}{L}-\phi_s(0)-\phi_s(1),\quad
\phi_s(1).
$$

用原严格相位包计算它们的区间，全部绝对值小于 $7/2$。两个 soft-turn 按准确 $L=|\Delta\phi|/(K\cdot23/25)$ 定义，并有归一 ramp 在 $[0,1]$，所以其峰值恰不超过已给 $K=3.4<7/2$。所有 coast 上 $l_0=0$。

terminal brake 的两端相位导数为零，其相位是 cubic smoothstep。因此直接使用 $6t(1-t)\le3/2$ 得

$$
|l_0|\le\frac{3(\pi/2-1.45)}{2L}<7,
\qquad L=.026.
\tag{6}
$$

最后不等式由原严格 $\pi$ 包及各自准确长度编码的有理比较确认。输出上界的显示值为：binary64 编码 $6.969018853551731$，书写十进制编码 $6.969018853551728$。整个 prefix 的严格结论都是 $|\kappa_i|<7$；零控制平尾的曲率为零。

真实运行：session `69373`，初块 `9fddb8`、结束块 `1efb27`，自然退出 `0`。计算内部耗时 `0.04588851899825386` 秒。[完整报告](2026-11-12-fd2d-round-prefix-curvature-bound-01.json) 保留精确有理界。此界只适用于冻结的 $\delta=0$ 回转面；不借给当前已接受的非零 $\delta$ 实体，也不由曲率界单独推出全局 reach。

## 4. 完整圆基准加增量：固定物理 $g_\delta$

现有物理外设计为

$$
a_\delta=a+\sum_j\delta_j\psi_j,
\qquad c_\delta=\frac{a_\delta'}{a_\delta},
\qquad K_\delta=-\frac{a_\delta''}{a_\delta}.
$$

保持圆形参考 $(n_0,0,l_0)$ 固定，定义完整实际场

$$
n=n_0+\eta,\qquad m=\mu,\qquad l=l_0+\lambda.
\tag{7}
$$

这里 $(\eta,\mu,\lambda)$ 指完整角函数的实际增量；它可以由 P1 raw 系数、完整 tail lifting 及 R153/R155 等已声明映射合成，不能只指某个投影后的低模差。度量变化在下列强迫项中全部保留。也不需要 $g_\delta$ 自身仍有 $|a_\delta'|\le1$ 的回转实现。

在固定材料角中，以

$$
C_n=n_s-a_\delta^{-1}m_u-c_\delta(l-n),
\quad C_m=m_s-a_\delta^{-1}l_u+2c_\delta m,
\quad G=ln-m^2-K_\delta
$$

为缺陷。代入 (7)，仅用准确恒等式 (3)，得到

$$
\boxed{C_n=\eta_s-a_\delta^{-1}\mu_u-c_\delta(\lambda-\eta)
 +(c_0-c_\delta)(l_0-n_0),}
\tag{8}
$$

$$
\boxed{C_m=\mu_s-a_\delta^{-1}\lambda_u+2c_\delta\mu,}
\tag{9}
$$

$$
\boxed{G=l_0\eta+n_0\lambda+\eta\lambda-\mu^2+K_0-K_\delta.}
\tag{10}
$$

这些是准确恒等式，不是围绕圆形的线性化。全部已知圆形贡献已解析相消；$\delta\ne0$ 时的 $c_0-c_\delta$ 和 $K_0-K_\delta$ 不能删除。

现固定 atlas 为 $u=U(s,\xi)$，记

$$
A=U_s/U_\xi,\qquad I=1/(a_\delta U_\xi).
$$

圆形参考与角无关，所以 (8)–(9) 在此图中准确变为

$$
C_n=\eta_s-A\eta_\xi-I\mu_\xi-c_\delta(\lambda-\eta)
 +(c_0-c_\delta)(l_0-n_0),
\tag{11}
$$

$$
C_m=\mu_s-A\mu_\xi-I\lambda_\xi+2c_\delta\mu.
\tag{12}
$$

即使该 atlas 原来由非圆 ruling 参考设计，它仍可作为固定计算图使用；没有理由因更换基准就悄改 $U$。所有 retained modes、角补余和实际节点/内点行应从上述完整函数定义重新得到。

## 5. 可直接实现的 lifting 与 cell 残差

一种明确的新表示是

$$
(n,m,l)=S_0+Y_{\rm raw}
 +\eta_T(s)\,\kappa_\beta(a_\delta(s)\sin U)
 (\cos^2U,-\sin U\cos U,\sin^2U),
\tag{13}
$$

然后按新表示的准确声明合成需要保留的 R153/R155 映射。$\eta_T$ 可沿用现有固定物理 tail 窗，$\beta$ 是独立的 tail16 参数；完整 tail 角函数不投影掉。式 (13) 不再添加原非圆 coast lifting。它与当前主线是不同的函数表示，不能把它标为对已有接受态的同函数加密。

中央精确柱上令 $Y_m=Y_l=0$，$Y_n=n_c(d)-1/a_0$ 并沿柱恒定。准确中央 $n_c$ 仍由 circle-base provider 给出；中央 Fourier 约束和 exact-cylinder 消元可以按同一数据重新构成。切口上令 $Y_{\rm raw}=0$。由于 $S_0(s_c)=0$、$\eta_T(s_c)=1$、$a_\delta(s_c)=.8$，切口第二基本形式就是完整准确 tail 数据。

当 $d=0,\beta=0,\delta=0,Y_{\rm raw}=0$ 时，式 (13) 为完整 $S_0$，并且全部连续缺陷严格为零。R153 正 $n$ coast 映射和 R155 正 trace 映射在其适用段都把此准确解映回自身；平切口沿准确 tail 的原样处理，不能在全零点硬作一般平方根除法。新增 active 列、整 hat 冗余和 gauge 必须按实际新表示的支撑条件声明，不能沿用旧非圆 lifting 的语义猜测。

设某一 cell 为 $[s_i,s_{i+1}]$，长 $h_i>0$，$Q_i$ 是所选择的归一求积。圆基准可以在求积之前解析消去，采用

$$
\frac{\eta_{i+1}-\eta_i}{h_i}
 -Q_i\!\left[A\eta_\xi+I\mu_\xi+c_\delta(\lambda-\eta)
 +(c_\delta-c_0)(l_0-n_0)\right],
\tag{14}
$$

$$
\frac{\mu_{i+1}-\mu_i}{h_i}
 -Q_i\!\left[A\mu_\xi+I\lambda_\xi-2c_\delta\mu\right].
\tag{15}
$$

已知 $n_0$ 的端点差由 (3) 准确消去，不先用粗 Gauss2 近似参考右端，再把其残差误认作需要 raw 系数补偿的物理缺陷。式 (14)–(15) 对增量的有限求积误差仍存在，也必须保留原有完整角补余、Gauss 行、曲率行及所选内部物理区间目标。

该改写并非将完整 tail 强迫抹去：$\eta,\mu,\lambda$ 包含全部真实 lifting，它们的实际端点值、径向一 jet 和角 jet 原样出现在 (11)–(15) 中。若采用 R152 一类端点恒等式与分片高阶求积，需显式适配新的 representation/source 身份，不能冒用旧严格 class guard。

## 6. 全参数方向导数

以下 $D$ 是任意中央、tail、raw 或 profile 参数方向；参考 $S_0$ 和计算 atlas 固定。记 $Dc_\delta,DK_\delta$ 为原真实 bump 导数，并令

$$
DI=-I\,Da_\delta/a_\delta.
$$

式 (10)–(12) 的完整方向导数为

$$
DG=l\,D\eta+n\,D\lambda-2\mu D\mu-DK_\delta,
\tag{16}
$$

$$
\begin{aligned}
DC_n={}&D\eta_s-A D\eta_\xi-I D\mu_\xi
 -c_\delta(D\lambda-D\eta)-DI\,\mu_\xi\\
&-Dc_\delta\bigl[\lambda-\eta+l_0-n_0\bigr],
\end{aligned}
\tag{17}
$$

$$
DC_m=D\mu_s-A D\mu_\xi-I D\lambda_\xi
 +2c_\delta D\mu-DI\,\lambda_\xi+2Dc_\delta\mu.
\tag{18}
$$

原 bump 公式仍为

$$
Dc_\delta=\frac{Da_\delta'-c_\delta Da_\delta}{a_\delta},
\qquad DK_\delta=-\frac{Da_\delta''+K_\delta Da_\delta}{a_\delta}.
$$

尤其式 (13) 的 $D\eta,D\mu,D\lambda$ 包含 current-radius 输入 $a_\delta\sin U$ 的链式项，非线性 R153/R155 合成也必须完整微分。径向求积是固定物理 $s$ 上的求积；本表示没有偷偷加入随未知参数变化的积分节点或 clock。

## 7. 从 gap=0 起步的接口及未证明事项

现 raw 入口和旧 small-gap 入口均有 `(gap(d)-gap_target)/gap_target`。这不支持准确零 gap；不能把 `gap_target=0` 直接塞进现 driver，也不能只省略该行。

若采用新的圆基准分支，令目标幅度为 $\varepsilon\ge0$，选一个与 $\varepsilon$ 无关的固定正尺度 $\sigma$，使用

$$
B_{\rm gap}(d,\varepsilon)=\frac{\operatorname{gap}(d)-\varepsilon}{\sigma},
\qquad D_d B_{\rm gap}=\frac{D_d\operatorname{gap}}{\sigma},
\qquad \partial_\varepsilon B_{\rm gap}=-1/\sigma.
\tag{19}
$$

例如可以把当前目标量级 $\sigma=.9$ 作为全条分支不变的数值尺度；它只是归一选择，不是新几何限制。在 $\varepsilon=0$ 时，准确 $d=\beta=\delta=Y=0$ 满足该行和所有连续 GC/边界方程。此时中央 $A=B=a_0$，没有强目标需要的非圆 gap，也没有因此满足 held 或 $\delta_E$。

需要强调，圆形准确解并不保证有任意小非圆解经过它。固定物理 $g_0$ 时，圆基准处的一阶 Gauss 方程是

$$
l_0\eta+n_0\lambda=0.
$$

它仍要与一阶 Codazzi、中央幅度约束和真实 tail 端口一起满足。切口 $n_0=l_0=0$ 使这条 Gauss 线性化退化；非负 Bernstein tail 控制的零点又是其允许参数锥的边界。不能未经实际核/分支分析就断言 Newton 可逆或已有非圆分支。

若同时允许径向外设计，线性化中保留 $-DK_\delta$ 与 $-Dc_\delta(l_0-n_0)$。但这些在物理材料角中本来是径向项，不能据此宣称任意非零角模的一阶边值问题都可解。可能需要选取合适的外设计基准、支路参数或伪弧长条件；本说明没有替它们求根，没有开启新 BVP。

可行动顺序是：新 provider 明确采用完整已知圆基准；在固定正 $\sigma$ 下使准确圆端点可表示；对真实小幅边界问题选择并验证分支；随后逐步增加实际 gap，所有外设计变化都记作新物理 $g$；最终冻结 $g$ 后再作同 $g$ 的 P1/Fourier 加密与完整后验。是否由当前直接 gap=.9 导致停滞仍属未验证假说，当前主线不因此被改写或放弃。

完整曲面最终仍须支付实际位置/标架、tail 刚体 registration、真实 $Z$、中央 gap、全时 held、全对法球和固定帽闭合。这里的全段曲率界和准确圆基准没有替代这些条件。
