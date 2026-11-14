# m2 实际有限尾、C² 圆领和固定帽的装配路线

2026-11-10，geometric_amplification，GPT-6 Astra Pro，AI-assisted。

**状态：可复现的完整有限网格与条件引理应用账本；数值证据。不是本题完成，不是当前候选的精确无限非轴对称尾存在性证明，也没有闭面 reach 证书。**

## 1. 本轮实际完成了什么

对已存实际非线性耦合候选 `root-neck-q003-actual-outer-m8.json.gz`，以及其 `tail-response_0003`，已经完成：

1. 在 pinned source `869436630c99aa5a68afb55bd8877c826034d117` 上，将原 integrated-Fr exporter 的 C3 Fourier 格改成当前 m2 格，并接入实际 Fourier-root split-flux 引擎。均值高度跨全部 stage 连续积分，没有逐纬线重置。
2. 用同一固定旋转背景生成径向高度原函数，保留完整尾高度反射和一次常数高度平移。
3. 保留原已保存的 **quintic** 前缀轨迹，按物理材料角重建；作独立的完整 Cartesian cut 两-jet 审计和显式微小公共端迹修正。
4. 使用原项目实际调用的固定背景 Hermite 圆领，接上两个固定平盘和四个固定 C3 标记。该有限圆领的度量缺陷仍计入账本。
5. 输出三个共同材料索引的闭网格，以及 R11 可直接读取的坐标/法向样本。对运动部分与固定帽的 19,268,064 个空间点对，已经解析消去全部连续相位。

主输出：

- [完整装配报告](geometric-actual-q003-closed-assembly.json)；
- [相位 0](geometric-actual-q003-closed-phase0.ply.gz)、[相位 π/4](geometric-actual-q003-closed-phase1.ply.gz)、[相位 π/2](geometric-actual-q003-closed-phase2.ply.gz)；
- [全相位交叉点对报告](geometric-actual-q003-closed-all-phase-cross-pairs.json)与[直接接口 NPZ](geometric-actual-q003-closed-normal-samples.npz)；
- [圆领精确有理预算](geometric-actual-q003-collar-budget.json)；
- [有限尾 manifest](geometric-actual-q003-tail-m8-s16-manifest.json)、[背景高度数据](geometric-actual-q003-closed-heights.json)、[采样计划](geometric-actual-q003-closed-plan.json)。

此样本的点云位移比仅约 `0.00160762`，离本题 `0.2` 目标很远。它用于验证真实有限尾到整面文件的接口，不是把小幅度示例算作任务完成。

## 2. 原项目中的“闭合”究竟是哪一层结论

原 visible 课题的 [R17](../../visible-flexible-closed-surface/results/R17-exact-finite-visible-closed-geometry.md) 和 [R21](../../visible-flexible-closed-surface/results/R21-m12-whole-map-and-actual-metric-decrease.md) 明确构造的是指定的**有限 C² 闭映射**。它们可以对那张有限图给出严格区间几何与度量预算，但没有宣称选定的 finite DN 已经是精确无限非线性 stable graph。

原 finite tail 的最深端通过一个显式 Hermite 扰动层归零，旋转背景本身保持为原来的完整无限背景；它并非把一个已证存在的非轴对称无限解直接画到 cuff。原 R21 第 7 节仍将 G5、源方程/无限谱/无限尾的精确存在性列为未付事项。这与原任务允许诚实报告严格存在性差距一致，也意味着不能把原课题的 finite mesh exporter 当成当前候选的精确闭等距构造器。

关键映射如下。

| 来源 | 可以复用的内容 | 不能随文件名一起继承的结论 |
|---|---|---|
| smooth-unrippled [R6：固定无限背景上的实际 XYZ、C² 圆领闭合](../../smooth-unrippled-twist-flex/results/R6-fixed-metric-c2-collar-closure.md) | 同一背景上的完整端点 Hermite 公式；所有混合/角向两-jet；度量、完整向量 Darboux、局部曲率和嵌套投影预算 | 端点小不推出公共外域 C² Cauchy，不推出无限非线性解或全局 reach |
| large-amplitude [R16](../../large-amplitude-twist-flex/results/R16-periodic-development-and-metric-error.md) | 实际周期平面发展；完整 Darboux/curl/均值/平移 period 的误差公式 | 单独 height 准确、Φ≈1 或一圈闭合不等于实际二维等距发展；一般非零残差 C² 还要额外条件 |
| large-amplitude [R20](../../large-amplitude-twist-flex/results/R20-mild-r64-c2-single-tail.md) | 其字面深源上的完整偶 π 周期 Fourier、完整均值、C² 单尾和受限 18 参数族 | 不是当前不同源的任意浅切口 Dirichlet-to-Neumann 图，不替当前有限改造头做全频非线性延拓 |
| large-amplitude [R28](../../large-amplitude-twist-flex/results/R28-fixed-deep-background-c2-cuff.md) | 当前 default 深源校准根存在/定位及旋转背景的 C² 平极限公式 | 不是非轴对称高度的收敛证明；有限 warp 的新归一和候选数值常数仍须单独核实 |
| large-amplitude [R31](../../large-amplitude-twist-flex/results/R31-fixed-background-cartesian-tail-taper.md) | 已有真实 Cartesian 源及其全深部强范数下，同一背景上的可消失误差 taper | 固定 taper 的误差再小，也不消除固定 Fourier 或有限 DN 缺陷 |
| visible [R15](../../visible-flexible-closed-surface/results/R15-weighted-inner-background-and-collar-bounds.md) | 固定背景与 Hermite 预算的调用方式 | 原 `curvatureBound=6`、cuff>0.14 的具体证明不能原数值复制到当前 K8、cuff≈0.05 |
| swarm [R520](../../continuous-flexibility-swarm/results/R520-actual-newton-zero-height-closed-flexibility.md) | 在它自己选定的 metric/参数上存在某个精确 C² 闭族 | 不是当前冻结 metric 的边界求解器，不提供当前幅度、直径或 reach 比例 |
| swarm [R78 extract](../../continuous-flexibility-swarm/agent-work/914b-final-height/R78-explicit-caps-phase-activation-extract.md) | 真实 round collar 上的固定帽与全相位作用；不要求额外第三阶正则性 | 它的径向/高度分离和外绕帽几何不是当前 neck 的分离证书 |
| 本题 [R8](../results/R8-fixed-cap-curvature-markers.md)、[R9](../results/R9-cylindrical-graph-global-embedding.md)、[R10](../results/R10-height-two-jet-cartesian-seam.md)、[R11](../results/R11-exact-all-phase-normal-chord-reduction.md) | 四标记、全局圆柱图条件、Cartesian seam 唯一性和连续相位 normal-chord 消元 | 必须分别支付全曲率、全局空间条件和真实完整高度两-jet，不能由点云替代 |

原课题 [infinite-tail applicability audit](../../visible-flexible-closed-surface/notes/2026-11-09-audit-infinite-tail-applicability.md) 的有限源/全频/延拓区分在这里仍适用。当前 m2 已消除了该报告讨论的 C3 频率不相容，但以下源和边界条件差别没有随之消失。

## 3. m2 已匹配的部分与尚不匹配的 R20 输入

当前参数是

$$
R=64,\quad a_{\mathrm{exp}}=11/4,\quad
\delta_n=.006\,2^{-n},\quad
\eta_n=.0003\,2^{-3n/2},\quad r_c=.05\text{（保存 binary 值）}.
$$

R20 的字面源则是

$$
\delta_n=.08\,2^{-n},\qquad \eta_n=.004\,2^{-3n/2}.
$$

当前 `rejoinR20At=null`。空间缩放不能改变这些无量纲 log-cell 长度，整数换下标也不能将 `.08` 精确变成 `.006`。改成某个 R20 rejoin 可以成为**另一张以后冻结的 metric**，不能在审计当前固定 g 时暗中替换。

m2 的偶 π 周期空间确实符合 R20 的角向空间。反射使径向相位均值为零，π 反周期的平面切向量使平移 period 为零；这有利于同轴发展，但完整 Darboux 方程、精确角平均根、正投影余量与真实径向相容性仍是输入。

R20 只给其充分深处的受限 18 参数 trace family；它没有给任意解析 Dirichlet 数据上的完整 DN。`protectCell=160` 不是该定理已经指定并认证的非线性起始深度。要在当前切口用它，仍需先获得当前源的全频尾结果，再把实际 trace family 向外通过所有固定 finite modifications 传播，支付分支分母、投影余量、解析宽度损失和切口坐标的可逆性。

## 4. 本轮的完整有限定义和均值账本

### 4.1 前缀保持原来的 quintic 轨迹

当前 prefix coefficient chunk 的形状是 `(6, 840, 25)`，确为源 `c2_interpolant` 产生的五次表示。**没有重新把轨迹变成另一张插值图。** 本轮核出的内部浮点 0/1/2 阶接缝残差为

$$
5.42\,10^{-20},\quad4.44\,10^{-16},\quad3.55\,10^{-15}.
$$

这些数是保存多项式系数的算术审计，不是新全域 C² 区间证书。最初将此保存格式误认为 scipy 原始 cubic 解的判断已撤回。均值高度继续由保存轨迹的 velocity mean 原函数恢复，其一、二导数由同一函数取得。

数值图使用辅助角 η；输出先用 `SavedPrefix.inverse` 求解真实材料角 θ 的 pullback。径向导数也转换为固定 θ 导数。不会把 η 的平移当作材料等距作用。

### 4.2 实际有限尾

本轮使用 8 raw cells、每 stage 16 步、256 个角节点、planar degree 47、64 点角向审计；实际尾含 4,723 个共享节点。`Fr` 是端点 `Fr/Frr` 与物理中点 `Fr` 定义的 quartic，位置为其精确积分；额外 shooting 接缝修正明确纳入有限定义。

物理径向宽度由独立正积分的 exact binary 值和一个精确有理总归一表示，不从相近的舍入绝对半径相减。8 个 `.f64.gz` 总计 8,371,294 B，单个约 1.04–1.05 MB。其 manifest SHA256 为

`2fe168e1b2d38a5388761f426f41f5ef324a64cc1d65cd2e0d8a9c604a663892`。

由于旧 exporter 的 collar packet 留有仅属于原候选的 `6.001` 默认背景假设，本轮将该字段改成 `null`，并标明 `backgroundCurvatureCertificate=false`。没有借用该错误默认值。清理标签后的完整重导出使全部 8 个数值块的 SHA256 **逐个不变**。

### 4.3 高度方向与公共切口

记 finite tail 的相对场为 $V$、背景斜率为 $w$，上半片定义为

$$
T(r,\theta)=\left(r e^{i\theta}+V_{xy}(r,\theta),\quad
H_c+\int_r^c w(u)\,du-V_z(r,\theta)\right).
$$

负号作用在**整个尾高度**。每个 stage checkpoint 只存形状量，不能把重新生成的一圈 canonical 坐标均值各自置零后直接拼起来；必须累计两个 mean integration channels。这里选一次常数

$$
H_c=\operatorname{mean}Z_{\mathrm{prefix}}(S)
+\operatorname{mean}V_z(c).
$$

实际数字为

| 量 | 数值 |
|---|---:|
| prefix cut mean | 1.8355891452338908 |
| tail cut mean correction | −5.77167462123×10⁻¹⁰ |
| 一次常数偏移 $H_c$ | 1.8355891446567234 |
| 背景从 cuff 到 cut 的高度 | 0.022684311165528714 |
| 上平帽高度 | 1.858273455822252 |

物理 cut 保存为 `0.30000000000000004`，参数字符串中的 `rCut=0.3` 与它相差一 ulp；本装配保留实际端点，未静默改半径。用

$$
r_s=-E^{-1/2},\qquad r_{ss}=-E_r/(2E^2)
$$

将 tail 的径向两-jet 转换到 prefix 的材料 s。对完整 XYZ 的 0/1/2 阶差，在 prefix 最后 `W=0.1` 上使用原公共端迹 quintic 公式。修正前本次**独立积分表示**的最大两-jet 差 `5.5731e-12`，修正后采样最大 `1.5067e-13`。它与 root 的 actual scalar-to-Cartesian seam audit 是不同误差层，不能将此数或后面的 full-vector Darboux 数混在一起。

### 4.4 原固定背景上的 Hermite 圆领

本次

$$
r_N=.05056158669090205,\qquad
L=r_N-r_c\simeq .00056158669090206.
$$

圆领上的相对场为

$$
\widetilde V=S(x)A_0+L H_1(x)A_1+L^2 H_2(x)A_2,
\quad x=(r-r_c)/L,
$$

$$
S=10x^3-15x^4+6x^5,\quad
H_1=-4x^3+7x^4-3x^5,\quad
H_2=(x^3-2x^4+x^5)/2,
$$

其中 $A_j=\partial_r^jV(r_N,\theta)$ 来自**同一 integrated tail** 的原始 endpoint 系数。这里没有删除深处旋转波形、压缩背景几何或改变 g。

`geometric-tail-collar-budget.py` 直接把这些 binary 系数解释为精确有理数，使用完整 XYZ、带二阶角权的 Fourier 主范数。得到

$$
K_N=1.1020850879\,10^{-16},\qquad
\eta_1=1.3925617146\,10^{-19},\qquad
e_g\le2.7851234293\,10^{-19}.
$$

该显式圆领满足 R6 的嵌套平面投影充分条件。额外**假设**全圆领背景曲率 $B\le8.001$ 时，同一有理预算给 full-vector Darboux 算子上界约 `1.986e-14`、主曲率上界约 `8.001`。本文件没有将这个 B 假设伪装成已完成的背景区间证书。

如此小的数不表示存在性缺口消失。固定有限深度上的 Hermite 扰动一般仍有非零度量缺陷；机器计算分辨不出它，也不能据此声称它正是某个精确非线性尾。

### 4.5 固定帽和时间参数

上下 cuff 内接固定平盘。用本题 R8 的多项式 bump，在上帽半径 `r_c/2` 的三个 120° 中心、下帽中心各放一个互不相交的标记，支撑半径 `r_c/8`，中心曲率依次为

$$
8.2,\quad8.25,\quad8.3,\quad8.35.
$$

四中心的仿射行列式约 `−0.00603505`。所有 marker 都在固定 cap 内，支撑不靠近 cuff。仅当其余曲面的完整曲率上界严格小于 `8.2` 等 R8 输入支付后，才能用它们推出实际像变化对应 $\delta_E>0$；这里的样本曲率不是该输入的严格替代。

这些是 **q003 的参数**。生成器提供显式 `--marker-kappas`，下一候选必须重选并重新核对曲率及 reach；例如 body 已超过 `8.35` 的候选不能复用本例标记。新标记曲率也会改变 reach 的局部预算，不能只把数值调高而不复核整个 D。

采用

$$
\alpha=\pi t/2,\quad0\le t\le1,\qquad
F_t(s,\theta)=R_\alpha F_0(s,\theta-\alpha)
$$

于整个活动环带，固定帽上取 $F_t=F_0$。线性 Hermite 操作与此作用交换，旋转背景不变。连续作用在真正 C² 图上时给 C² 拓扑连续族，不需要 C³。

网格取 θ 的均匀 96 点，三个相位通过材料索引平移后再作空间旋转。固定 cap 与 cuff 顶点逐字节复用。握持集合 H 可取两整个帽的并：原 README 明确允许 H 不连通，其内部非空。所选两个 pole 的距离约 `3.71658768`；这里只给它与点云直径的比较，没有代替整图直径证书。

## 5. 本轮数值结果与确切量词

### 5.1 显式表示的空间样本

| 对象 / 诊断 | 数值 | 范围 |
|---|---:|---|
| finite tail exporter 的 metric operator defect | 1.4210×10⁻¹¹ | 全导出跨中的指定 fractions × 64 angles |
| exporter 完整 XYZ Darboux 矩阵 Frobenius norm | 3.4859×10⁻⁶ | 对二阶表示敏感；不是 cut 误差，也不是 metric norm |
| exporter actual principal curvature | 7.99426 | 同一有限图的样本 |
| prefix 归一化 metric entry 最大误差 | 1.1033×10⁻¹⁰ | mesh rings × 96；算子范数可用其两倍放宽 |
| prefix actual principal curvature | 8.05870 | 同一 mesh 空间样本 |
| tail / collar mesh metric entry 最大误差 | 8.4333×10⁻¹³ / 4.4409×10⁻¹⁶ | 稀疏 mesh 环；不覆盖所有薄胞元 |
| prefix $\beta_\theta$ / upward J 最小值 | 0.997220 / 0.0717699 | 样本 |
| tail $\beta_\theta$ / inward J 最小值 | 0.999999958 / 2.0623×10⁻⁸ | 样本；tail 径向方向已转换为向 cuff |
| cuff 的 J | 0 | 真实平极限；这里应接 R6 投影/固定盘论证，不能要求 R9 的严格 J 在平盘继续成立 |

每个 PLY 有 53,090 顶点、106,176 三角面；Euler 特征为 2，每边恰两面，没有零面积三角面。gzip 文件分别为 `839089`、`876733`、`845828` B，解压后均 `2707821` B。**水密拓扑不等于空间无自交证明。**

点云的直径下界与原点球直径上界在本组样本上相同，均为

$$
D_{\mathrm{cloud}}=3.7316831035823843.
$$

相位 π/4、π/2 的点云 Hausdorff 距离为 `0.00433392542`、`0.00599912877`，后一比值 `0.00160762010`。这是离散点云之间的 Hausdorff 距离，既没有自动包围连续曲面的 Hausdorff 距离，也没有验证本题幅度门槛。

### 5.2 真正消去连续时间的交叉点对样本

[normal-samples NPZ](geometric-actual-q003-closed-normal-samples.npz) 包含 root R11 helper 所需的四个键：`moving_xyz`、`moving_normal`、`fixed_xyz`、`fixed_normal`；另保留源顶点索引、C/P 类别和 τ。文件仅 `279382` B。

`root_phase_reach.py` 对 12,528 个活动样本与 1,538 个固定样本（含 79 个 marker 样本）计算四个 normal-chord branch 的精确连续相位最小值，共 19,268,064 个空间点对。取

$$
\tau=.03D_{\mathrm{cloud}}=0.11195049310747153.
$$

负 margin 点对数为 0，最小 margin `3.87901338e-9`，最小化相位约 `2.22529480`，出现在下端圆领与固定平帽 cuff 附近。相位消元覆盖全部实数 α，比指定 `[0,π/2]` 更强，但**空间仍是有限样本**。这里没有检查所有 A–A、固定片内部点对，也没有连续直径上界。接近对角线时 margin 本来趋零，不能用一个正的网格 margin 直接声称全空间稳定；后续需要局部曲率/连续性与远离对角线的空间区间预算。

## 6. 从当前有限流程到精确闭图，必须补的具体输入

### 6.1 真正无限尾

需在当前固定 g 上得到完整 Fourier 的高度 U，满足完整 Darboux 方程、Φ=1、平移 period=0、正投影余量，并在所有整胞元上有统一 C² 深部控制。R20 证明的是它自己的字面源和深 trace family；当前仍需要源转移/新源定理或相应的固定 g 后验/全频收敛论证。

有限远端 Robin、一个 M 的小残差和某几个深端口很小均不能替代这些输入。即使重新作更深的 Hermite 层，固定的浅处角向残差也不会因此消失。

### 6.2 真实 C² cuff，不只是端点小

旋转背景这一半已有直接的 R28 路线：

$$
W_n=\epsilon R\delta_n^{7/4}/r_c^7,\qquad
B_n=\frac{\sqrt{12}W_nJ_n}{r_c c_n\delta_n}+\frac{7W_n}{r_c},
$$

$$
J_n=30(6e)^{-2/3}\log(2R/\delta_n^2)^{1/3}+15/(4e).
$$

当前参数代入 n=160 的数值代表为 `W160≈7.06194e-83`、`B160≈8.71445e-4`，并随深度衰减；它们控制的是**未修改的旋转深背景**。本轮背景数值积分省略的更深高度代表上界约 `2.51e-134`，不包含有限积分、alpha、校准与舍入误差。有限积分和反函数检查的最大 radius residual `2.26e-16`、split-height difference `1.97e-14` 也只是数值诊断。

非轴对称部分还需证明所有整胞元上的 Cartesian 二阶偏离趋零，并在同一 mean/center/phase gauge 下比较公共外域。R6 末节和 R31 所需的是这种强范数 Cauchy 条件，不是只看 $A_j(r_N)$。

### 6.3 有限头与 Cartesian seam

实际切口的高度、均值一阶/二阶导数必须一起匹配；常数平移只能调整高度，不能调整其导数。本题 R10 证明：在同一 C¹ metric、非退化平面投影和正确 orientation 下，完整高度两-jet 决定沿 connected seam 的 Cartesian 两-jet，至多差一次平面刚体规范。

当前 root audit 和本轮独立 integrated reconstruction 已把小 q 的实际 seam 误差压到约 `1e-12`。下一步的严格/收敛工作应控制完整源轨迹和表示误差；不能把两-jet 检查通过直接升级为无限闭合。

### 6.4 同一 g 的可执行细化

可以在保持当前 checkpoint 的 physical metric 参数、phase interval、caps 和规范约定下依次做：

1. 固定实际 tail response，增加 integrated export 的径向 steps、角向 quadrature/degree，单独量化本轮 `3.49e-6` full-vector Darboux 表示误差；这不需要重做幅度设计。
2. 使用相同冻结 profile 做 prefix/source 与 full-spectrum tail 的细化，重新比较 cut 的完整 Cartesian jets、mean derivatives、公共外域 C² 差，而不只比较一个标量 DN。
3. 在同一无限背景上增加真实非线性深度，记录同一 gauge 下的整胞元两-jet 和公共外域 Cauchy 账本。要区分边界求解变化、表示变化和最后 Hermite 层预算。
4. 用真实闭图的空间区间/近对角线曲率控制接上 R9、R6 和 R11。neck 的原点支撑可能为负，不能照搬原 flat17 的正支撑 reach 证书。

这些步骤是新的可执行工作，不是本轮已经完成的 G5 证据。当前 κ 与 cross-pair 样本干净，只说明这张小幅度有限图值得继续审计。

## 7. 小文件依赖与复现

本轮 source cache 共 87 个小文件，由 root 从同一 pinned commit 提取。新接口没有改动原课题文件。核心入口为：

| 本题 helper | 固定来源/功能 |
|---|---|
| [geometric-tail-integrated-export.mjs](../computations/geometric-tail-integrated-export.mjs) | 读取 `visible/scripts/db6f-tail-increment-export-v2.mjs`，逐项检查并替换 C3 格；接 `78718-tail-fourier-root-split-engine.mjs`；记录实际新增引擎 hashes |
| [geometric-tail-background-samples.mjs](../computations/geometric-tail-background-samples.mjs) | `closing_weighted_tail.mjs` + `closing_recalibrated_tail.mjs` 的同源原函数，不使用原候选写死的 alpha 或曲率证书 |
| [geometric-tail-collar-budget.py](../computations/geometric-tail-collar-budget.py) | 原 `db6f_tail_integrated.py` 读取器 + smooth-unrippled/R6；直接用本图 endpoint binary 系数作有理计算 |
| [geometric-closed-assembly.py](../computations/geometric-closed-assembly.py) | 本题 SavedPrefix、原 integrated-tail reader、完整材料角/均值/两jet、R8 固定帽、root R11 接口 |

还需要 source 中的 `950f-tail-subdivision.mjs`、完整 split-flux/physical-jet/relative-development 引擎链，以及 `f6tail_relative_spatial_jets.mjs`、`f6tail_relative_development.mjs`。它们的路径和 SHA256 在 tail manifest 和 adapter metadata 中。原 `db6f-export-closed-mesh.py` 对原 whole-map certificate 有防串图绑定，不能移除检查后冒充当前候选的证书；这里使用新的数值装配 helper，明确不继承该认证状态。

从本课题目录运行，选择一个**新的**输出目录以保留旧运行：

```bash
task_source=/workspace/scratch/83b864ada613/visible-flex-source/topics/visible-flexible-closed-surface
task_output=/tmp/visible-flex-q003-reproduction
mkdir -p "$task_output"

node computations/geometric-tail-integrated-export.mjs \
  --source-topic "$task_source" \
  notes/root-neck-q003-actual-outer-m8-tail-response_0003.json.gz \
  "$task_output/tail" --depth 8 --steps 16 --angular-nodes 256 \
  --degree 47 --audit-angular-nodes 64 --difference-step 0.00005 --grid chebyshev

python computations/geometric-closed-assembly.py plan \
  --source-topic "$task_source" \
  --checkpoint notes/root-neck-q003-actual-outer-m8.json.gz \
  --port computations/alternative-neck-provider-smallcut30-port.json \
  --tail-manifest "$task_output/tail-manifest.json" --out-prefix "$task_output/closed" \
  --marker-kappas 8.2 8.25 8.3 8.35

node computations/geometric-tail-background-samples.mjs \
  --source-topic "$task_source" --manifest "$task_output/tail-manifest.json" \
  --radii "$task_output/closed-radii.json" --out "$task_output/closed-heights.json"

python computations/geometric-tail-collar-budget.py \
  --source-topic "$task_source" --manifest "$task_output/tail-manifest.json" \
  --assume-background-curvature 8.001 --out "$task_output/collar-budget.json"

python computations/geometric-closed-assembly.py render \
  --source-topic "$task_source" \
  --checkpoint notes/root-neck-q003-actual-outer-m8.json.gz \
  --port computations/alternative-neck-provider-smallcut30-port.json \
  --tail-manifest "$task_output/tail-manifest.json" --out-prefix "$task_output/closed" \
  --plan "$task_output/closed-plan.json" --heights "$task_output/closed-heights.json"
```

最后一步已包含 R11 连续相位交叉点对诊断。三个 PLY 使用 binary little-endian xyz float64、一个 A/C/P 顶点标签和 int32 三角面；gzip 仅压缩文件，不改坐标。

高于当前 M8 的运行须相应增大 source angular count、degree 和网格 angular count；endpoint packet 至少要求 `degree >= spacing*modes`，不能沿用一个不足以容纳完整高度谱的 degree。当前 cut correction 用 256 点全角 Fourier 表示，仅供其 Nyquist 范围内的有限谱。

8 个 raw derivative 块是可由已存 tail checkpoint 和脚本确定性重建的中间数据。遵照根 README 的数据规则，若需要压低提交总量，可以只保留生成器、manifest/hashes、圆领预算、完整网格和小法向包；复现时先运行 exporter 重新生成 blocks。无论选择哪种保存方式，不能把仅存在的 manifest 误报成所有 derivative blocks 已随提交分发。
