# step02 的实际参数、D5/D8 初值与共轭节点检查

2026-11-12，constructive-route。除引用 R48 的准确多项式/算术结论外，
本文全部返回、旋转、参数和几何数字均为**浮点数值证据**。
本次最重要的失败诊断是：48 节点插值上很小的共轭误差，送回实际射线
后大了约两个数量级。新的节点已经保全，继续修正同一对象。

## 1. 固定输入和真实局部参数的含义

起点是 data/phase_ring_continuation/type_fixed_step02.npz，
SHA256 05d3e59cf338c5d2a2bde13aad7bf1d4e5247c326efb46b3148793e75a7ea883。
原始三列是同目录 type_fixed_step02_schur_directions.npz，
SHA256 941c19642b4e74cbe5d68c311629bbe66f05df16fca26692c541ed61d6f29629。
这些是保持 beta4 腰值及 radius_shift 的有限最小残差方向；不是精确 PDE
切向，也不是固定目标度量的齐次核。

将三列按 step02 参数文件中的准确保存 eigenbasis 组合，取
$$
\eta_*= (0.002,\ 0.0002,\ 0),\qquad
V_*=(B\eta_*)^\top D.
$$
相应三个 mean 增量约为
$$
(-0.00197280301407605,\ -0.00009938846082313814,\
 0.00037171252535751775).
$$
探索点按 phase vector 的 $v_0+pV_*$ 生成，保存每个实际浮点向量。
在某个保存点上计算微分时，使用以该点为原点、方向为同一 $V_*$
的局部曲线；重新计算该点的相位二 jet、mean 输出、目标曲率及转折根。
浮点矩阵结合次序的微小差异没有被宣称为精确 dyadic 家族恒等式。

参数微分使用同步目标
$$
g_0(p)=E(p,x)\,dx^2+a(p,x)^2\,d\theta^2,\qquad E=\langle|F_x|^2\rangle.
$$
这里 $a$ 是保存的周长半径，radius_shift 固定。选定一个点后才可将其
目标度量冻结供 R37 Newton 使用。返回的判别式始终是
$$
\widehat\Delta=(-K_0)G_{\rm actual}^{\,2},
$$
不能将 $G_{\rm actual}$ 预先替换成 $E a^2$。

所有原二进制图仍有未支付的微小径向反射缺陷。现有射线以正侧根定义
两端 $\pm t$、在端点用正侧导数作镜像，因此本文不是原始二进制图的
严格 operator map；详见 principal-map-reflection-caveat 笔记。

## 2. 48 主节点与 48 参数列

从已保存的 32 条主射线出发，以 Hermite/PCHIP 分歧选出 16 个新中点，
只补这些实际射线。补点直接观察到旧 32 点 Hermite 中点误差可达
$0.0099199$，所以旋转估计的一致性不能替代函数插值误差界。

完成文件：

- phase24-corrected-step02-principal-map48-adaptive.json；
- phase24-corrected-step02-parameter-map48.json；
- phase24-corrected-step02-rotation48.json。

前两文件在 notes/2026-11-12- 前缀下；SHA 以 R48-and-parameter-frozen-manifest
为准。48 个参数节点中，soft eigen 列范围为
$[0.0068986241,0.0479088529]$，middle 为
$[0.1008204593,7.3010448106]$。这些数字是同图实际 moving-root 导数，
包括两端的端点项，并不来自径向作用量。

旧最小 middle 节点的独立中心差分 $h=2\cdot10^{-5}$ 得
$0.2358053110$，而变分输运给 $0.2359836576$，差约
$1.7835\cdot10^{-4}$；应保留这个误差，不称机器精度一致。

## 3. 正探针与 16/29 检查

$p=1$ 的新 NPZ 是 type_fixed_step02_positive_twist_probe.npz，
SHA256 06d0710ee40590c88897936d19b67971fd67745163597ed7bf1f91c95ec56ef3。
它没有 Newton 校正；只是相同曲线上的真实有限几何。
全体样本的 metric 最大约 $8.02181\cdot10^{-5}$，腰差/直径代理
$0.0515027324$，外侧样本保持正曲率，中央 $N<0$。
R44 中实际有限 $W$ 的各预算在采样处仍有余量；它们不是连续参数管证书。

同 48 起角重新算返回后，probe-base 的逐节点位移全部为正，
范围约 $[5.18787\cdot10^{-5},0.001494198]$。然而 probe 接近 $16/29$：

| 插值 | $R^{29}(\theta)-\theta-16L$ 的 16385 点范围 | 变号周期点 |
|---|---|---:|
| 使用真实角导数的 Hermite | $[-0.000990875,-0.0000152572]$ | 0 |
| 单调 PCHIP | $[-0.00493839,0.00332273]$ | 58 |

PCHIP 的点分成 29 个吸引和 29 个排斥点。Hermite 的无变号不排除切触根。
因此**没有证明实际 probe 锁在 16/29**，也不能因为两个旋转估计接近就
忽略这项高周期分歧。文件为 step02-probe-period29.json。

## 4. D5/D8 的第一个实际几何定位

准确目标见 R48：
$$
\rho_5=(15121+\sqrt5)/27422,\qquad
\rho_8=(4852+\sqrt8)/8804.
$$
先在 base/probe 两份实际图的仿射插值族中求有限 Fourier 共轭和参数。
这只是初值选择，不是实际几何参数方程。得到：

| 目标 | 仿射初始 $p$ | 实际另存 NPZ 的 SHA256 |
|---|---:|---|
| D5 | 0.41143386520907216 | a042a48e7245e6dbba9466bad493e439e84c375a37b92f32ddaee60e3274c275 |
| D8 | 0.23253149685574986 | 61de372c2fce6d4dfc8fe8f38e02bbcb3846e40eba6fc1bf0d5e08d6e6f8b44f |

文件名分别为 type_fixed_step02_d5_probe.npz、type_fixed_step02_d8_probe.npz。
两点的实际 target 根分别约 $0.2383951489395$、$0.2383841966946$，
metric 样本最大约 $7.91744\cdot10^{-5}$、$7.88598\cdot10^{-5}$；
腰差比例代理约 $0.0515017003$、$0.0515013867$。两点全外区样本均正，
固定原 beta4 规范，未替换 canonical step02。

对这两份实际 NPZ 又各自重算同样的 48 起角：

- D5 Hermite/PCHIP 的 100000 步平均估计约
  $0.5515018919/0.5514984042$；
- D8 约 $0.5514354794/0.5514305724$。

各自有限迭代区间仍有约 $10^{-5}$ 尺度，且不含插值、ODE 或舍入误差。
旋转数由轨道迭代算，不是一步位移的角均值。

在实际 D5 点与 $p=1$ probe 间再次作局部仿射模型，会给约 $p=0.40720$
的 D5 初值。**下一节的真实 H 节点表明，这个精细修正不可信。**
D8 的同类模型修正也只留作历史初始化，不迁移为真实参数结论。

## 5. R48 的准确 $H_0$ 与实际节点反证

从第一个 D5 仿射解选择 finite Fourier $H_0$，然后把它重新定义成
R48 中完全明确的 dyadic 多项式。准确整数卷积证明全实圆周正导及
$s_x=1/32$ 上 $M_0<4.587414,R_0<7.254348$。这里 $x=4\theta$，
所以物理角带宽是 $1/128$。

在同一实际 D5 NPZ a042a48... 上，直接积分
$$
\theta_i=H_0(2\pi i/64)/4
$$
对应的 64 条新射线；同时算 $R'(\theta_i)$ 和局部真实 $V_*$
参数列。没有通过已有 48 节点插值获得这些数值。
文件 step02-d5-actual-conjugacy-nodes64.json 给：
$$
\max_i|4R(H_0(x_i)/4)-H_0(x_i+2\pi\rho_5)|
 \simeq0.00683174292,
$$
$$
\max_i|R'(H_0(x_i)/4)H_0'(x_i)-H_0'(x_i+2\pi\rho_5)|
 \simeq0.0575544835.
$$
相比之下，48 节点插值模型上的离网格误差只有约 $10^{-4}$。
这是真实的新误差证据，原数据与失败结论均保留。

同一次新射线给出的 R31 加权参数量为
$$
\frac{\partial_p[4R_p(H_0(x_i)/4)]}
     {H_0'(x_i+2\pi\rho_5)}
 \in[0.000300067057,0.004535420943],
$$
64 节点均值约 $0.002310293739$。加权误差均值约
$-0.0000645280671$，对应 R31 一步参数预测 $+0.0279306765$。
这与上节仿射插值推的负向小修正相反。
上述均值及范围还是实节点浮点值，不是 Wiener 横截证书。

脚本为了只算实际一条曲线，新增 CurveGeometry adapter；
它未改冻结的三列 geometry evaluator，并在三个实际点与填零的三列
版本逐值比较六个变分 jet，最大差为 $0$。这只验证接口实现一致性。

## 6. 同点独立参数差分与下一次更新

在上述 D5 图的 $H_0(0)/4$ 点，独立重新计算目标根并用更紧的
$2\cdot10^{-11}$ ODE 容差，得到变分参数列约 $0.000890204014$。
实际独立差分为：

| 参数步长 | 一阶中心差分 | 与变分差 | 二阶中心差商 |
|---|---:|---:|---:|
| 0.05 | 0.0008901878591 | $-1.6155\cdot10^{-8}$ | $-2.9967\cdot10^{-5}$ |
| 0.025 | 0.0008900730956 | $-1.3092\cdot10^{-7}$ | $-3.0743\cdot10^{-5}$ |

较小步长并未给出更小误差。因此这些仅支持导数的符号和量级，
**不授予二阶导数的上界 $T$**，也不把指定 solver 容差称为全局误差界。
完整样本/根/向量 hashes 在 step02-d5-curve-finite-differences.json。

将 64 个实际 H 节点按 degree-one 提升归回同一角周期，和原 48 条
实际射线合并，得到同源 112 节点图。再用 64 个真实参数列建立
$F_\delta^{\rm model}=F_0^{\rm interp}+\delta(\partial_pF_0)^{\rm interp}$，
而不是在返回角上人为加常数。有限共轭修正结果：

- N257：局部参数步 $0.02990978137$；
- N513：局部参数步 $0.02991762660$，全局标记 $p=0.4413514918092046$；
- N513 离网格模型误差约 $7.45902\cdot10^{-6}$；
- 正导样本约 $[0.3544633,1.8071752]$。

文件为 step02-d5-map112.json、step02-d5-local-jet-conjugacy.json，
新共轭 NPZ 为 type_fixed_step02_d5_local_jet_conjugacy.npz。
这些模型省略真实参数 Taylor 项；新几何、新 H 仍必须各自保存、
重新作 dyadic 逆导数证明，并再次直接积分实际 H 节点。当前正继续这一步，
没有把 N513 的离散收敛当作实际共轭。

## 7. 精确重做入口

以下均从本课题目录运行；推荐设置 OPENBLAS_NUM_THREADS=1。
全部输入 SHA 见本文及 R48-and-parameter-frozen-manifest。

32→48 实际主图：

    python scripts/fourfold_phase_refine_map.py \
      --checkpoint data/phase_ring_continuation/type_fixed_step02.npz \
      --base-map notes/2026-11-12-phase24-corrected-step02-principal-map32.json \
      --out notes/2026-11-12-phase24-corrected-step02-principal-map48-adaptive.json \
      --branch-checkpoint data/phase_ring_continuation/type_fixed_step02_refine_branch.npz \
      --new-rays 16 --block-size 8 --resume

16 参数列→同一 48 角：

    python scripts/fourfold_phase_refine_parameter_map.py \
      --checkpoint data/phase_ring_continuation/type_fixed_step02.npz \
      --directions data/phase_ring_continuation/type_fixed_step02_schur_directions.npz \
      --base-parameters notes/2026-11-12-phase24-corrected-step02-parameter-map16.json \
      --target-map notes/2026-11-12-phase24-corrected-step02-principal-map48-adaptive.json \
      --out notes/2026-11-12-phase24-corrected-step02-parameter-map48.json \
      --branch-checkpoint data/phase_ring_continuation/type_fixed_step02_parameter_refine_branch.npz \
      --block-size 4 --resume

生成第一个 D5 实际几何：

    python scripts/fourfold_phase_parameter_probe.py \
      --checkpoint data/phase_ring_continuation/type_fixed_step02.npz \
      --directions data/phase_ring_continuation/type_fixed_step02_schur_directions.npz \
      --parameter-map notes/2026-11-12-phase24-corrected-step02-parameter-map48.json \
      --trial-checkpoint data/phase_ring_continuation/type_fixed_step02_d5_probe.npz \
      --out notes/2026-11-12-step02-d5-geometry.json \
      --eigen-parameters .0008228677304181443 .00008228677304181443 0

D8 将 eigen-parameters 换成 .0004650629937114997、.000046506299371149975、0；
同时把输出 d5 名改为 d8。正 probe 则采用 .002、.0002、0。
每个新几何的 48 图均用四分之一周期相同初角，但重新计算全部目标/根/射线：

    python scripts/fourfold_phase_evaluate_map_grid.py \
      --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_probe.npz \
      --angle-grid notes/2026-11-12-phase24-corrected-step02-principal-map48-adaptive.json \
      --out notes/2026-11-12-step02-d5-map48.json \
      --branch-checkpoint data/phase_ring_continuation/type_fixed_step02_d5_principal_branch.npz \
      --tolerance 2e-8 --block-size 8 --resume

最初仿射共轭：

    python scripts/fourfold_circle_conjugacy.py \
      --base-map notes/2026-11-12-phase24-corrected-step02-principal-map48-adaptive.json \
      --probe-map notes/2026-11-12-step02-positive-twist-probe-map48.json \
      --out notes/2026-11-12-step02-d5-affine-conjugacy.json \
      --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_affine_conjugacy.npz \
      --target D5

R48 多项式预算命令在该结果 §3。直接 H 节点与真正参数列：

    python scripts/fourfold_phase_conjugacy_nodes.py \
      --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_probe.npz \
      --directions data/phase_ring_continuation/type_fixed_step02_schur_directions.npz \
      --parameter-map notes/2026-11-12-phase24-corrected-step02-parameter-map48.json \
      --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_dyadic_conjugacy.json \
      --out notes/2026-11-12-step02-d5-actual-conjugacy-nodes64.json \
      --branch-checkpoint data/phase_ring_continuation/type_fixed_step02_d5_Hnodes_branch.npz \
      --rays 64 --block-size 8 --tolerance 2e-8 --resume

真实节点驱动的 112 图模型修正：

    python scripts/fourfold_circle_local_jet_conjugacy.py \
      --base-map notes/2026-11-12-step02-d5-map48.json \
      --actual-Hnodes notes/2026-11-12-step02-d5-actual-conjugacy-nodes64.json \
      --initial-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_affine_conjugacy.npz \
      --merged-map notes/2026-11-12-step02-d5-map112.json \
      --out notes/2026-11-12-step02-d5-local-jet-conjugacy.json \
      --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_local_jet_conjugacy.npz \
      --target D5 --base-global-parameter .41143386520907216 --sizes 257 513

独立差分使用 fourfold_phase_map_finite_difference.py，输入同 D5 NPZ、
directions、parameter-map 和 dyadic-conjugacy，指定 --steps .05 .025
--tolerance 2e-11。其默认 conjugacy-angle 为 $0$。
旋转和 period29 程序分别是 fourfold_circle_map_rotation.py 与
fourfold_circle_periodic_orbits.py；后者参数 --denominator 29 --winding 16。

全部完成文件与 live 文件分别保全；没有因为新节点暴露较大误差而删除旧图。
主目标的实际全频逆、精确闭族和几何比例仍未完成。
