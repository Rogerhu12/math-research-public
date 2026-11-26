# 新场的真实 mean1168 切口高度：连续径向积分入口

维护：Astra-held10-06bbeb39-20261126 / seam_geometry。2026-11-26 UTC。

## 当前实际状态

新增
[seam_certify_true_cut_height.py](../scripts/resume_20261126/seam_certify_true_cut_height.py)
把**同一新场**的真实核心均值节点包围、完整物理 quintic、原固定角图和真实桥相位接成一个可执行的高度积分入口。它输出

$$
Z_c=\int_0^{s_c}M_*(s)\,ds,
\qquad
M_*(s)=\frac1{1168}\sum_{j=0}^{1167}V_z(s,\psi_j),
\qquad Z(0)=0.
$$

本条只准备新的连续证明入口。当前已执行 §5 的源码编译和参数解析；**没有运行新场的完整积分，没有新的 $Z_c$ 数值证书**。原 R60 的高度区间没有作为输入或默认预算。新 warm 核的真实积分包围由 §2 绑定的独立入口提供，原 $\lambda<1/499$ 的粗 tube 不适用于新的 $\lambda=1$ 场。

## 1. 一个明确的公共 $C^2$ 图

物理文件、数值规范和原目标度量不改写。要积分的连续图沿用 R59/R62 已说明的公共表示，全部参数取自这次输入：

- $Y$ 的每个内部节点取右侧原字面值、一阶、二阶；最后节点取最末左侧二jet。相邻段以精确有理五次 Hermite 连接。跨越前缀—桥入口的原区间保留同一个多项式。
- 角图 spline 使用同样的公共右二jet，然后乘原来的晚期五次 cutoff。
- 前缀的振幅是本次冻结的实际 $\delta$。原有理速度表按本次字面 `prefix_end` 一次归一时长，仍在两端精确给出 $(a,a',a'')=(1,0,0)$。
- 桥的相位和 $L_1,L_2,L_3$ 取原 `ShortBridge` 字面参数，入口半径为 $1$。半径定义为相位正弦的**真实原函数**；末段解析延拓至本次 `physical.x[-1]`，与切口 trace 入口的定义相同。
- 核心 lift 是这次真实 R53 与 supported material-phase 核减去同一冻结 Fourier 投影，保留原窗口 $[.5s_b,.9s_b]$。其高度分量与完整角图对流均按实际输入保留。

独立的新辅助库
[seam_m3_prefix_pieces.py](../scripts/resume_20261126/seam_m3_prefix_pieces.py)
保留原 `explicit_m24_prefix_pieces.py` 的精确有理公式，按本次实际模式数 $M$ 验证 $n=3M+1$ 与完整频率 $3,6,\ldots,3M$。旧 M24 文件不改动，也不把旧证书数字扩给新模式数。精确端点恒等式重新用于这些**新系数**；新入口另把桥段的共享 Hermite 公式逐项验算。

这里选择的是明确的连续表示。其与原浮点查询器、原目标度量的转移仍需在该新场的完整度量证明中支付；高度积分不会把这种转移写成零，也不会重新选择目标度量。

精确端点代数通过并保存小报告后，积分器释放 $Y$ 的两份大型 Fraction 临时字典并回收内存；严格区间系数、完整 profile/lift、原输入和公共 Hermite 定义全部保留。这只调整证明临时对象的生命周期，不重舍入或更改数学图。

## 2. 真核心包围与字面均值规则

暖 v2、v3 源分别经过 `warm_fixed_m3_model_v2.accepted_input`、`warm_fixed_m3_model_v3.accepted_input` 的完整接受门。若源是同一 Cartesian 图的重新表达，保留 `solver_invoked=false` 及原求解器出处；不会把它冒充新的 BVP 返回。实际 nonlinear-DN 源先经过集中 `warm_actual_dn_acceptance.accepted_actual_input`，核验真实返回的 RMS、边界、完整有限度量、原 outer check、全高/J 包及全部源身份，再用只读 loader 恢复明确版本的冻结几何。输出保存所调用接受门的路径和 SHA；未知模型版本不进入计算。

核心区间文件必须绑定相同 `source_run_sha256`、`physical_sha256`、实际 $M$、模型版本、warm 定义和实际 oracle/kernel/provider 源。若实际来源为 v3，还逐项核验完整 `warm_definition`、`phase_basis`、`basis_anchor_v2_run`、`basis_anchor_v2_sha256` 和 `linear_source_model_kind`。v3 使用补弧上的真频率 $j\pi/(\pi/3-S)$；它的真核心 oracle 必须明确处理这一个完整族，不能沿用 v2 的 $3j$ 控制 span。物理状态 Fourier 频率仍是 $3j$，与核心控制频率分开绑定。它的 `H1,H2` 是 Cartesian 分量，形状为 `(2,1168,3)`，两层分别是严格下界和上界。原完整 `exact_lift_initial` 向量还必须逐字等于本次 loader 的实际投影；不截断高模式投影来构造核心 lift。

特别地，均值节点是原数组

~~~python
psi = 2 * np.pi * np.arange(1168) / 1168
~~~

中的字面 binary64 数；数组 SHA 为
`f4834f978de38046e374b020d2a928d293fc405f794159e40e2271f4ee9bd9cf`。
核心真实周期仍是 $2\pi/3$，三角函数也是真函数；**这不把均值节点替换成精确的 $2\pi j/1168$**。导出的 `psi_lo` 和 `psi_hi` 必须逐项等于原字面节点，随后在这些精确二进制有理数上评价严格三角区间。

`--allow-intermediate-lambda` 可以显式核验一个当前已接受的中间场；默认要求实际 $\lambda=1$。这条选项不改变完成标准或几何合同。

## 3. 完整均值与严格径向覆盖

令 $\theta=\psi-e(s)\sin(3\psi)/3$，$\rho=\theta_\psi$。脚本先在 $\psi$ 极标架中合并 Fourier 场与真实 lift 的一、二阶角导数，再旋转到 $\theta$ 标架。圆基准在 $U,V$ 中解析消去，随后按实际 Frenet 定义计算

$$
T=\frac U{|U|},\quad
N=\frac{V-(T\cdot V)T}{|V-(T\cdot V)T|},\quad
B=T\times N,\quad
\alpha=-\frac{a'}{|U\times V|/|U|^3}.
$$

有限均值的完整被积函数是

$$
V_z=\alpha N_z+\sqrt{1-\alpha^2}\,B_z
       -\frac{e'\sin(3\psi)}{3\rho}\,F_{\psi,z}.
$$

没有使用精确等距假设，亦没有删去角图对流。平方根、标架分母、半径和 $\rho$ 必须在每个接受径向盒内有有效正下界。由正交归一，
$\alpha N+\sqrt{1-\alpha^2}B$ 的范数为 $1$，故其 $z$ 分量可以严格与 $[-1,1]$ 相交；对流项独立保留。

分割包括全部物理 quintic、角图 spline、归一速度表、lift、晚期 cutoff 和桥相位拼点。每个叶区间 $J=[l,r]$ 直接求连续值域

$$
M_*(J)\subset[m_J^-,m_J^+].
$$

不满足正性或所需宽度的区间继续二分；`--max-cells` 是每轮进入前检查的**全部径向盒尝试次数**上限，包括接受和拒绝的盒。未解决时输出确切失败区间和未覆盖项，不把已积出的部分称为 $Z_c$。完成后使用精确有理数相加

$$
\sum_J(r-l)m_J^-\le Z_c\le\sum_J(r-l)m_J^+.
$$

所有浮点区间端点在最终相加前解释为其精确 binary64 有理数，故累加本身不再产生未记账舍入。

桥半径中心值使用相位正弦的 40 阶截断包围。若 $p$ 是实际相位上界，点 $s$ 的原函数误差不超过

$$
(s-s_b)\frac{p^{41}}{41!}.
$$

径向盒内部再使用 $|a'|=|\sin\phi|\le1$，把中心值扩张半盒宽。这里既未使用原 GL64 半径作为真实原函数，也未调用旧桥场的积分或度量证书。公共系数、角图和 $a$ 的二jet相接，且所有有限均值节点处标架非退化，所以该均值原函数在前缀—桥接口与内部节点处是共同的 $C^2$ 高度。

## 4. 原尾零模的绝对放置

可选 `--tail-geometry-bundle` 必须来自同一物理前缀高度引用、相同 $M$ 和原物理端口，并绑定实际 accepted packet、原 native mean-chain、共享 $R$ manifest 及 stage 0 的 `mapHash`。其 cut 系数中的零模还必须逐字等于原 mean-chain 的 $\mu_c$。当前已有 whole-tail 入口的 M24 合同没有随本高度入口扩大；若真实尾在另一模式数上求得，须先使用针对该实际模式数的明确尾部导出与认证版本。

随后明确使用一个全尾常数

$$
z_b=Z_c+\mu_c.
$$

这个定义保留原非旋转 mean，且不用区间中点选取 $Z_c$。脚本仅当新得到的区间包含于 $[1/10,32/25]$ 时，标记 R58 的绝对放置条件已付。完整记录保留原 warm/full-height 身份；高度常数相接本身仍不证明 full H、Cartesian 两jet接缝或整体几何。

## 5. 运行与小记录

~~~bash
python "$TOPIC/scripts/resume_20261126/seam_certify_true_cut_height.py" \
  --source-run "$NEW/run.json" \
  --physical "$NEW/physical.npz" \
  --core-mean-certificate "$CORE/mean1168-core.json" \
  --core-mean-intervals "$CORE/mean1168-core-intervals.npz" \
  --interval-kernel "$INTERVAL_KERNEL" \
  --tail-geometry-bundle "$TAIL/geometry-bundle.json" \
  --outdir "$WORK/new-true-cut-height"
~~~

核心文件路径示意的是调用接口，不表示这些真实新场文件已经存在。完整叶区间文件和核心数组只保留在 runner；仓库只接收源、说明和实际执行后的紧凑证据。当前实际检查是 `python -m py_compile` 与 `--help` 均 exit 0，另以两个旋转截面恒等式检查标架归一化：纯旋转截面为 $M_*(s)=\sqrt{1-(a')^2}$；在 $a=1$ 上加入常数径向扰动 $R_0$ 时为 $M_*(s)=\sqrt{1-((1+R_0)a')^2}$。两例都包住对应解析值，前一例保留非零角图及角图径向导数。

新的维度库另外用 M16、M24、M32 三个小型制造多项式检查精确端点二jet；M24 情形的全部 exact field/chart 系数、端点目标、profile 多项式和分割与原库逐项相同。动态均值还在 M16/M32 的最高高度模式上核对

$$
F(\psi)=(\cos\psi,\sin\psi,\varepsilon\cos(m\psi)),
\quad
M_*=\frac1{1168}\sum_j
\frac1{\sqrt{1+\varepsilon^2m^2\sin^2(m\psi_j)
                 +\varepsilon^2m^4\cos^2(m\psi_j)}},
$$

其中 $a'=0$、$m=3M$，核验保留的完整最高模式角导数和标架归一化。两例严格均值区间包含该显式有限和的高精度核对值。这些只是新代码的公式及维度核对，不是本课题新场证书；没有重新运行任何旧实际场积分或证书。
