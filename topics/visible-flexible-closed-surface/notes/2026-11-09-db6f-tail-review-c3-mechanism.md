# 有限 C3 核接入现机制及正余量凸包条件：独立全文审查

审查者：Astra-visible-flex-db6f0b0e / tail_theory，2026-11-09。

**结论：PASS，绑定作者 v2；通过的是完整条件证明与静态接口，不是新闭面或 ODE 解。** 我未提出或实现本稿的凸包预算，也未参与其参数优化。审查独立展开法向角与材料角、Frenet 恒等式、中央镜像和局部高阶展开、真实 cut 的符号与规范化、旧图高度的作用域以及三类点对的整图距离界。独立计数与 Fraction 核查、作者脚本独立重放均真实 exit0。未调用任何角根、RK、BVP、求解器、几何后端或优化；未改变当前 $g$、任何图或正在运行的任务。

## 1. 冻结身份、修订及实跑证据

最终审查正文为 `notes/2026-11-09-db6f-prefix-c3-current-mechanism-interface-v2.md`，SHA256：

`7497d615d4fb46eeed1b6cc710851d9bca4aa46a040567f1879cf77acd30a356`。

28 项来源表为同名 `-v2-sources.json`，SHA256：

`d7c6f11a0150e292c4da692e9935ec12d2647ba4725d7175348b8af9fe3c849b`。

作者的纯标量脚本 `scripts/db6f-prefix-c3-mechanism-conditional-budget.py` 保持 SHA256 `b98272c2d92406dd3611ae680ebd754b3558268281c47500aea1e6a70b23f527`；作者报告保持 SHA256 `47fda2e36bf60860f94c0f151542cbff465a3ebb28845db617bf80d45f5ef1a1`。

旧正文 `eec8eab0…` 原字节保留。v2 恰有三处替换，独立 checker 完整重建文本后核相等：

1. 由实际 $R_K$ 定义的 $Q_{CD}$ 改写为 $Q_{CD}\le4.419076$，不把 $R_K\le57/40$ 的上界当成等式。此点由 root 与本审查分别发现；数值脚本本来计算的就是上界常数，无须改数值。
2. 背景 $w=w_r=0$ 明确限定为当前平帽接口；一般固定的轴对称非平帽不要求这两个量为零。
3. 正文的来源账本链接指向 v2。

实际独立执行如下，均不启动数学求解：

| 执行 | 观察 receipt / exit | 结果 |
| --- | --- | --- |
| 原作者标量脚本，换独立输出路径 | `64c26f` / 0 | 5,093 B；与作者报告逐字节同，SHA256 `47fda2e3…` |
| 独立 `db6f-tail-review-c3-mechanism.py` | `8a5999` / 0 | 38 个不同实文件绑定、28 个作者精确有理字段、3 处文本替换全部通过 |

独立脚本 SHA256 为 `8cfa9b1716f33cda5f3da7aec932f92157247b88a3148c5ef2881c6c4c3d5fef`；输出 `notes/2026-11-09-db6f-tail-review-c3-mechanism-check.json` 为 `14ca00414c8869c7856e0a1589ed14d9fe444a69f474a57f857c3f7f28c957a7`。该脚本不 import 作者实现。它从四个原始整数指数枚举 Fejér 平方的系数，分别使用 $4^4,5^4,8^4$ 个四元组，核四个已发表核心案例的全部正 Fourier 系数、正规化、半相位支持差、直径上界和内切圆界。然后从这些独立重建值计算新预算，而不是仅检查作者输出内部相容。

作者程序仅导入 argparse、fractions、hashlib、json、pathlib。全部决策门用精确 Fraction；`display_only` 不参与证明。新程序另核了 binary64 字面量 `.124` 的精确 Fraction，避免将它与 $31/250$ 逐位混同；两种解释下的第一系数间隔都严格为正。完整输入身份及实际执行记录分别保存在本审查 JSON 和 `tail-review-c3-mechanism-observed-execution.json`。

## 2. 三种角及当前入口保护

作者 §1 的 $\phi,\vartheta,\psi$ 分别是支持法向角、单位速率材料角、数值图坐标。由
$$
x=h n+h't,\quad x_\phi=(h+h'')t=\rho t,\quad \sigma'=\rho>0
$$
得 $\gamma_\vartheta=t$、$\gamma_{\vartheta\vartheta}=-n/\rho$。因此本例曲率范围正是 $[860/8833,20/3]$。正性和全局单调使弧长反解合法；均值 $\rho=1$ 给周长 $2\pi$。

固定材料角而改变 $c_j$ 时，$m=3j$，
$$
\sigma_{c_j}=(1-m^2)\sin(m\phi)/m,
\qquad \phi_{c_j}=-\sigma_{c_j}/\rho.
$$
固定 $\phi$ 的导数为 $\cos(m\phi)n-m\sin(m\phi)t$；链式项 $\rho t\phi_{c_j}$ 恰补到作者式 (4)。这与 `PlanarSupportCore.parameter_derivatives` 逐式相同，不能换成法向角平移。

独立整数计数给 $b_1=42/43$，旋转后 $c_1=(1-r)b_1/4=357/1720$。已逐条读 `SupportBVP`、`WarpedBVP.initial` 和 `WarpedFlow.__init__`：父类的 seed gauge 范围与实际 $q=q_{seed}\exp p_0$ 的 `.124` 保护是不同检查；合法 gauge 不能绕开后一检查。四个已核核心案例均有 $c_1\ge1/5$。若又令 `warp_reference_q=c1`，则 $e=8c_1=357/215>1$，当前单谐波图失去可逆性。

这些是现代码的入口限制，不是多谐波凸性的必要上界。`PlanarSupportCore` 的真正几何检查使用 $\rho$ 及其导数的采样余量；本核已有正 $\rho$ 的解析证明。法向角有限 Fourier 公式仍不能被当作材料角或数值扰动的有限精确公式，未来投影误差必须重新支付。

## 3. 条件 Frenet 等距性及数值角图

逐式核 `950f-prefix-warped-bvp.py` 和 `950f-prefix-adaptive-chart-bvp-v2.py` 的 `frame`：$\kappa$ 是角曲线实际曲率 $|F_{\vartheta\vartheta}^{\perp}|/|F_\vartheta|^2$，正平方根分支为
$$
F_s=\alpha N+\beta B,\quad
\alpha=-a'/(a\kappa),\quad \beta=\sqrt{1-\alpha^2}.
$$
在作者式 (6) 的真实光滑分支上，$|F_s|=1$、$F_s\cdot F_\vartheta=0$。从 $T\cdot N_\vartheta=-\lambda\kappa$、$T\cdot B_\vartheta=0$ 得
$$
\lambda_s=-\alpha\lambda\kappa=(a'/a)\lambda,
$$
因而中央 $\lambda(0)=a(0)=1$ 推出 $\lambda=a$。该推导完全是物理材料坐标的等式；有限投影后的 ODE 不自动继承点态恒等式，也不证明无限角向方程的存在。

若假设所有截面始终同形缩放，$\kappa=1/(a\rho)$ 才可约成 $|a'|\rho_{max}<1$。当前速度平台的比较仅排除这一假设，并不排除会改变形状和空间标架的真分支。

对 $\widehat F(s,\psi)=F(s,\Theta(s,\psi))$，独立链式求导给
$$
\widehat F_s=V+\frac{\Theta_s}{\Theta_\psi}\widehat F_\psi.
$$
adaptive 源中的 `v=theta_s/rho`、`W=Vnormal+v*d` 完全对应。clamped spline 在入口一阶导数为零；切口 quintic cutoff 连同其一、二阶导数都为零，故切口角图的全部两 jet 恢复恒等。新的凸组合图 (11) 具有严格正的 $\Theta_\psi$，但仅是可单独实现的坐标候选，不是已运行的新图，不消除真实边值方程或投影误差。

## 4. 中央两 jet 和局部 quartic 限制的充分正则性

作者对中央镜像的“光滑真解”前提是必要范围。平面正向中央曲线有 $N=-n,B=e_z$；$a'=a''=0$ 给 $F_s=e_z$ 和 $\alpha_s=0$。因入口 $F_s$ 对角度恒定，其所需角导数为零，故 $T_s,N_s,B_s$ 为零，得到 $F_{ss}=0$。镜像 (14) 的位置、两条一阶切向及三种二阶偏导全部一致，且 $(e_z,\gamma_\vartheta)$ 保证浸入。

在数值角图下 $\Theta_s(0)=0$，可能的 $\Theta_{ss}$ 只加平面切向项 $\gamma_\vartheta\Theta_{ss}$，不破坏高度二 jet 的镜像奇偶。实际有限 Hermite 程序将入口高度二阶槽设为精确零是一个明确定义的表示修正；它不使修正后 metric 自动等于原目标。

为把作者 §4 的高阶范围完全明确化，可采用以下充分假设：在入口单侧小条带上，真实 $F$ 对 $(s,\vartheta)$ 联合为 $C^5$，满足原 Frenet 方程及非退化分支，且 $a$ 在该小条带为源的首个多项式片。**不需要、也没有声称已有数值图具有这条真解性质。** 此假设允许将由 $F_\vartheta,F_{\vartheta\vartheta}$ 定义的标架连续对 $s$ 求三次导数。

对 $0<s<T_u\varepsilon\eta_r$，源码 `turn_ramp` 的原函数为
$$
P=\frac{\eta_r^2}{1-\eta_r}\left(\frac{x^4}{4}-\frac{x^5}{10}\right),
\quad x=\frac{s}{T_u\varepsilon\eta_r},
\quad a-1=\frac{\delta\varepsilon}{1-\varepsilon}P.
$$
由 $\delta=v_uT_u(1-\varepsilon)$ 得作者式 (15) 的 $A_4$，特别 $a'=a''=a'''=0$ 于入口。

递推理由可写得更具体：由 $F_s(0)=e_z$ 的两个角导数为零得 $B_s=0$；$F_{ss}(0)=0$ 的两个角导数为零给 $B_{ss}=0$，同时 $\alpha_{ss}=0$，故 $F_{sss}=0$；再用该恒等式的两个角导数，得到 $B_{sss}=0$。所有 $\beta$ 的前三阶 $s$ 导数在入口均为零，而
$$
\alpha_{sss}(0)=-a''''(0)\rho,
\qquad F_{ssss}(0)=a''''(0)\rho n.
$$
这严格给 (16)。固定中央支持法向 $n(\phi)$，该材料点的水平投影满足
$$
n(\phi)\cdot\pi_{xy}F(s,\vartheta)
=h(\phi)+A_4\rho(\phi)s^4+o(s^4)>h(\phi)
$$
于充分小的正 $s$，所以整个该局部图不可能投影包含于原 $K$。反之，任何固定正 $\eta$ 在足够小邻域容许这一连续扰动。它不证明全局 $K+\eta B_2$ 包络，也不是任意 $C^2$ 分支的 Taylor 定理。原稿已明确这一点，故不要求再改其字节。

## 5. 真实边值匹配、均值和完整 Cartesian cut

`TailMixin.terminal`、`bc_jac`、`seam_audit` 以及方向桥源已逐式审读。实际 $q_g=self.q$ 是固定 gauge；自由首支持参数经 `p0` 进入初值，不能将两者混同。原真 slope DN 的 $M$ 条约束尚需通过支持参数解出；指定有限核全部系数并不是该全局根。

桥取真实 binary $c$、$w_c=1/2$ 和 $\sigma_b=-1$。保存数值桥与 exact-bridge 的真实积分根并非同一数，原文已保留弧长转移。由
$$
r_s=\frac{\sigma_b}{\sqrt E},\qquad r_{ss}=-\frac{E_r}{2E^2}
$$
及整个高度反射，非均值的两个匹配式是
$$
q_g y_Z'=S/\sqrt E,\qquad
q_g y_Z''=\sigma_b(T/E+Sr_{ss}),
$$
均值按同样符号处理，与 `seam_audit` 完全一致。`height_integral` 实际对 adaptive `frame()['V']` 的高度均值积分，此时 `V` 字段已经是 $W$，并非单独的法向 $Vnormal$；它定义数值图的均值高度，不是可独立优化的附加自由参数。

`db6f-root-common-cut-v2.py` 对保存 tail 的高度列及其每阶径向导数先取负，加入背景 $-w,-w_r$；其位置 gauge 为精确 prefix 均值减 tail 反射均值。保存坐标 $u=\lambda_b s$ 下的目标端迹确为
$$
T,\qquad \frac{r_s}{\lambda_b}T_r,\qquad
\frac{r_s^2T_{rr}+r_{ss}T_r}{\lambda_b^2}.
$$
全 Fourier 端迹的匹配同时给角向和混合偏导。此链式规则可复用；新的端迹、修正大小及新 map 的 metric 证书必须重新生成。当前方法没有提供给指定强核心的真 DN 解，也没有把有限匹配提升为无限尾存在证明。

## 6. 相位、固定帽、reach 及旧高度的范围

相位公式 (22) 的空间旋转和材料平移保持共同轴对称 $g$。固定帽端的全两 jet 必须对这一相位作用不变。当前平盘背景确实需 $w=w_r=0$，且扰动两 jet 为零；v2 正确没有把这个特例提升到所有轴对称非平帽。

中央真实二 jet 的主曲率大小为 $1/\rho,0$，外法向支撑为 $h$，但这只覆盖中央。R10 的 reach 工具要求同一个完整参数球面上的 $C^2$ 浸入、同一中心的全域正支撑及实际主曲率界。若整个新族确有 $\sigma\ge.069$、$K\le1/.069$，才可推出 reach 至少 $.069>.03D$（用 $D<2.3$）。平面核心或带边柱核的 reach 不能代付这一步。未闭柱核的像全等、$\delta_E=0$、无固定开材料片的既有结论也未被本稿改变。

旧实际图的轴心分离不是抽象可调整参数。独立从旧闭预算和已审分段球账本分别取得
$$
H_{c,-}=\frac{7977247853389765}{4503599627370496},\qquad
L_{axis}=2H_{c,-}.
$$
又精确核 $H_{c,-}$ 等于旧 `tail_height_lower` 加同图的高度扰动上界；common-cut 元数据确为 $\ell=0$ 且镜像入口成立。R17 的全图构造在上下固定帽实际轴心处给距离 $2H_{cap}\ge2H_{c,-}$，R21/R25 沿用该构造并重证当前图数据。这是同一图的总高度及直径下界，不是只从握持集合直径任意反推轴向跨度。

所以“保留旧帽坐标而满足新总高度 $2.2$”不可能。作者 §7 已明确不据此排除同一个 $g$ 的其它真分支，更没有把该旧下界当作每个未来帽的必然高度。全局平移和整体缩放不能修复归一化比例；单独移动帽则改变了接缝问题。

## 7. 全局凸包引理的独立证明核查

下列各项均是对**未来全图**的条件；不预设它由现 ODE 实现。令 $K$ 为已审旋转后的凸核心，$r=3/20$。紧性及交换最大值得
$$
R_K=\max_{x\in K}|x|=\max_{|u|=1}h_K(u).
$$
由 $0<b_j\le1$ 和
$$
\sum_{j\ge1}(9j^2-1)^{-1}
\le\tfrac18\sum_{j\ge1}j^{-2}<\tfrac14
$$
得 $R_K\le57/40$、$h_{min}\ge23/40$。这里最后严格界可直接由 $j\ge2$ 的 $j^{-2}<[j(j-1)]^{-1}$ 求和支付。没有使用错误的点态估计 $|hn+h't|\le h$。

取 $\eta=1/1000$、中央半高度 $a=1/10$、端盘半径 $c_*=3/10$、端半高度 $H_*=11/10$。因 $c_*<23/40$，两个端盘的水平投影都在 $K$，于是
$$
\pi_{xy}\mathcal E=K+\eta B_2,
\qquad c_*B_2\times[-H_*,H_*]\subset\mathcal E.
$$
三类点对的证明是分别使用三角不等式及垂直跨度：中央块与中央块用 $d_++2\eta$ 和 $2a$；两端盘用 $2c_*$ 和 $2H_*$；中央块与端盘用 $R_K+\eta+c_*$ 和 $H_*+a$。由独立重建的外向端点 $d_+=2.112793419185$，严格有
$$
Q_{CC}<26/5,\qquad
Q_{CD}\le\frac{1104769}{250000}=4.419076<26/5,
\qquad Q_{DD}=26/5.
$$
后两组相对 $26/5$ 的有理余量分别为 $195231/250000$ 和 0；相对干净 $D_*=23/10$，平方余量为 $9/100$。零余量的 DD 比较没有被要求严格，因为两个相反端盘的相反边缘点实际达到 $26/5$。

对于任意两有限凸组合，双重加权差向量的三角不等式给凸包直径不大于生成集合直径；取闭包不改变该界。因此整个 $\mathcal E$ 的直径是 $\sqrt{26/5}<23/10$。这覆盖全部中央块、可能过渡、固定帽及标记，只要它们的真实位置都已证明在 $\mathcal E$；不能仅验证核心的位置。

半相位支持差的正方向也重新核过：本稿先将核心旋转 $\pi/3$，所以可取法向 $\phi=\pi/3$，不是直接沿用旧核的法向零。此时旋转支持函数之差为
$$
\sum_j[(-1)^j-1]c_j(-1)^j
=4(1-r)\sum_{j\ \mathrm{odd}}\frac{b_j}{9j^2-1}=\Delta.
$$
若新相位全图包含这个核心支持点 $p$，而初始全图 $S_0\subset\mathcal E$，则对每个 $x\in S_0$ 有
$$
(p-x)\cdot(u,0)\ge\Delta-\eta.
$$
从一个方向的 Euclidean 距离下界已经得到双向 Hausdorff 距离的下界，无须假设整张曲面凸。独立 Fraction 核出的严格余量为
$$
\Delta-\eta>0.461868276536,
\qquad (\Delta_- -\eta)-\frac{D_*}{5}=0.001868276536>0.
$$
所以在该条件下 $\delta_{hold}>.2D$，其中 $D$ 是真实整图初始直径。固定帽若在所述中心圆柱内，每个相位可以同理包含于旋转后的 $\mathcal E$；全相位的嵌入和 reach 仍另证。固定 $H$ 的大小和非空内部、$\delta_E>0$ 也并未由位置包络自动产生。

## 8. 审查边界

本次通过的实际肯定结果是：中央核的单位速率数据与物理 Frenet 机制相容；局部光滑正分支有所述共同 metric、中央镜像和带正则性限制的四阶外向项；当前 driver 有明确但非几何必然的入口限制；新凸包在整体直径与未对齐支持分离之间有严格有理余量。

尚未给出：穿过整个原 profile 的正分支、指定强核心的真实非线性尾匹配、全段包络包含、与固定帽的完整两 jet、新族全时嵌入和 reach、真实固定握持区及刚体非全等、同一固定问题的误差收敛与独立完整重跑。当前 M12 的 mean height 和旧证书不转移到新核。本审查不支付主线 G5，也不将 README 的完成条件改成只需满足一个位置凸包。

本文件及独立脚本、两个报告、实际执行记录列于 `notes/2026-11-09-db6f-tail-closed-publication-21.json`。所有作者冻结文件保持原字节；修正版正文只采用本节所绑定 v2。
