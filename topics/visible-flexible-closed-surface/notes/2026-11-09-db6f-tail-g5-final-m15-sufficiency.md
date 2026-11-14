# README G5：最终 M15 数值收敛证据的最小闭合条件

2026-11-09，`/root/tail_theory`。**只读审查与条件式实施清单，不是 M15 成功报告，也不是新的完成门。** 本轮只读取既有闭合文件并做元数据/哈希比较，没有新求解、root、flow、导出或连续后端运行；没有读取活动 continuation 的状态作为完成输入。

## 1. 结论先行

若未来取得原方程的**完整 M15/N512 prefix+tail 真联解**，并对其唯一明确闭图证明全曲面、全相位的实际相对 metric 误差

$$
\mathcal E_{15}\le B=\frac1{500000000}=2\times10^{-9},
$$

则不应自动再加“最终 M15 必须做一次 p8/steps32→64 真联解”或“所有 $C^2$ 图差必须到机器精度”的完成门。README G5 的容差对象是**实际等距误差**；此处 B 保持原主求解容差，未借较松 BC 容差放宽。

但一个孤立的 `metric<=B` 或 solver-success 标记仍不能自动替代 G5。最后必须把这张实际图接入已存在的**同一固定问题的网格/频率轨迹**，实际完成计划中的 N256→N512 真校正，执行新图的完整后验误差与实际下降检查，冻结包含成功、平台和失败记录的收敛账本，并保留时间全量词的解析证明。现有材料已经提供前段轨迹；缺的是尚不存在的最终 M15 端点及其真实连接。

因此，在题设假定的新图完整界已经通过之后，**最少还要实际执行的误差比较**是：用指定 M12 实际点下界与新 M15 全域上界运行已审 `db6f-audit-terminal-error-gate.py` 的正常候选分支，而不是继续引用它目前的 M12 负例测试。再将这次结果与 R21 已证的 M8→M12 实际下降和本文分项账本合并。这个正常门本身仍不自动把 `G5` 布尔值置真。

若所有这些条件及 README 其余门、最终独立完整重跑均付清，可以如实称为**达到原容差的数值完成**；必须同时说明没有证明非线性无限尾严格存在或整个加密序列有一个 $C^2$ 精确极限。README 第7项明确要求披露此差距，不能把数值完成改写为严格存在定理。

## 2. 原文要求与不能混同的四种误差

README 完成标准第5项要求固定几何——度量、参数、$t$ 范围不变——在网格、频率和时间加密下，使等距误差下降至机器精度或求解容差；仅靠改变层数/尺度等物理渐近参数压小构造缺陷不够。第1项另要求每张族是闭 $C^2$ 且随时间在 $C^2$ 中连续；第3/6项要求全时实际 reach；第7项保留数值与严格存在之间的差距。[S1]

本题应分别报告：

| 量 | 本次完成判断中的角色 |
|---|---|
| 原 BVP/RK/moment/shooting residual | 验证确实解了声明的离散原方程；不能直接当作 metric。 |
| 保存实际有限闭图对固定 $g$ 的全域 metric 误差 | G4/G5 的主要容差对象，最终须有完整连续证书达到 B。 |
| 两档有限图的 $C^0,C^1,C^2$ 差 | 辨别表示、积分和规范差异的证据；不是 README 给出的额外机器精度阈值。 |
| `fullD`、`fullTensor`、形式曲率或源两 jet mismatch | 诊断量，不能改名为 metric；也不能代替实际图曲率、公共两 jet 恒等。 |

更小的连续证书上界不一定意味着实际误差下降。已有 R21 和新 terminal gate 用旧图的**严格实际下界**与新图的完整上界分离两者，避免仅因验证包变紧就宣称数值解改善。[S3,S9]

## 3. 实际已经存在的离散序列

本轮从六份真实已关闭 prefix CP 及其自己指向的最后真实 tail response 重新提取下表；完整路径、SHA、节点数和残差在 `tail-g5-closed-sequence-inputs.json`。全部六份 `frozen_profile/chart/warp_reference_q/physical_port_sha256/physical_tail_parameters/physical_tail_cut` 逐值完全相同，canonical SHA 为 `811e8cdccbad6edd4c487afc8ec07c16d519995cd9c5b182bc79ab327f414071`。这项字典检查与 R21 的数学目标识别互补，不用哈希取代函数定义。

| 已闭求解 | prefix 角数 | prefix 节点 | prefix tol | 尾 shooting 深度 | parts×steps / raw profile | 尾角 N | 尾 tol |
|---|---:|---:|---:|---:|---:|---:|---:|
| M8/32 设计联解 | 256 | 778 | $2\cdot10^{-7}$ | 10 | $2\times32=64$ | 256 | $2\cdot10^{-9}$ |
| M8/64 固定 g | 256 | 2570 | $2\cdot10^{-9}$ | 10 | $2\times64=128$ | 256 | $2\cdot10^{-9}$ |
| M8/128 固定 g | 256 | 2570 | $2\cdot10^{-9}$ | 10 | $2\times128=256$ | 256 | $2\cdot10^{-9}$ |
| M12 固定 g | 512 | 2570 | $2\cdot10^{-9}$ | 12 | $4\times64=256$ | 512 | $2\cdot10^{-9}$ |
| M14/N256 固定 g | 512 | 2633 | $2\cdot10^{-9}$ | 12 | $8\times32=256$ | 256 | $2\cdot10^{-9}$ |
| M14/N512 真校正 | 512 | 2633 | $2\cdot10^{-9}$ | 12 | $8\times32=256$ | 512 | $2\cdot10^{-9}$ |
| 最终 M15/N512 计划 | 512 | 尚未有最终值 | 原 $2\cdot10^{-9}$ | 12 | $8\times32=256$ | 512 | 原 $2\cdot10^{-9}$ |

几点不可省略：

1. M8/32 的 CP 是确定最终 delta 的设计联解，`fixed_metric=False`、prefix tol 为 $2\cdot10^{-7}$。完成这次设计后冻结其 delta，后面研究的是这一固定目标；不能把该历史求解描述成从一开始就在原 $2\cdot10^{-9}$ prefix 容差运行。
2. 从 M8/128 到 M12、M14 和预期 M15，每 raw profile 的普通 RK 步数都是256。改变 shooting parts 不等于增加总原生径向分辨率；不能把 p4→p8 单独说成一次步长加密。
3. M14 相对 M12 的 prefix metric **诊断**回升，必须保留。N256→512 真校正和更紧 collocation 容差试验都没有解释它。不能把 M14 从历史中删掉，或声称全部已试频率单调。其尚未产生与 R21 同等级的完整实际闭图误差证书，诊断数值也不能冒充该全域量。
4. 原 M15/M16 失败路径、低 floor 诊断和零初猜 pilot 都是闭合的失败/中间记录，不构成成功收敛点。
5. 目前 $H_j(s)=s^{j+1}H_{target,j}$ 的 continuation 改变了内层边值。直到 $s=1$、原真 prefix 外层和最终 N512 校正闭合之前，它只是初猜路径，不能拿小 s 的小误差冒充固定最终问题的 G5 加密。旧 pure 小振幅或 q=.02 端迹同样不能替代宏观图的证据。

原固定 g 记录还给出了 M8 真径向32→64→128的 prefix 差值显著缩小，而其 metric 在角频平台上；M12提高频率后 prefix/source/actualXYZ metric 明显下降。这些是有用的误差分层证据，范围分别见原记录，不能把它们称为所有高模的统一 RK 误差定理。[S2,S4]

## 4. 三种“深度”和两个角数必须分开

### 4.1 同一无限背景上的数值深度

固定物理背景的 protectCell=160、有限 source 校准表0–159、源指数、尺度比、cap/warp 参数和更深无限源均不变。`closing_recalibrated_tail.mjs` 的 source 创建明确使用 `modes:1, depth:protectCell, steps:1, quadrature:16`，而不是把当前 shooting 的 M、steps 或 N 喂回去重新设计背景；表的 calibrationSteps=512 保持。精确径向 alpha 仍由同一个真宽度积分定义。[S3,S11]

数值 shooting depth10或12，是在该固定背景上截断待解的有限边值系统；export depth8，是从已有 CP 选择外域并接 R6 圆领的位置。二者都不等于物理 protectCell160，也不能互换标签。

M12 同一最终 CP 的 N=6/8/10/12 端迹账本给 R6 metric 界依次约 $2.09\cdot10^{-11}$、$1.52\cdot10^{-23}$、$7.55\cdot10^{-36}$、$2.73\cdot10^{-48}$。这是**同 g 上数值闭合操作**的深度证据，且外部源误差没有因这些层数变化而被隐去。它不是四个重新求解的深端 BVP，更不是无限稳定图存在定理。[S5]

最终 M15 必须核自己的实际 collar。上表来自另一 CP，且 source 端迹 packet 的 planar 保留阶与完整 exporter 不同，不能直接贴到新图。若新图完整 tail 证书已包含实际 collar 并达到 B，就没有依据仅为“再加一层”而强制生成另一个图。若 collar 自身占用门槛或出现深度平台，才需要针对该缺口增加数值深度并重核新图；不能改物理层尺度或 taper。

### 4.2 Galerkin M、角求积 N 和 XYZ 表示阶

源 M 控制求解未知 Fourier 模；尾 quadrature N 控制有限角求积的原 moment/RK/DN；prefix angular、seam angular_samples 和诊断角数又是不同参数。M15 的最终 N256→512 必须是真原方程校正，不能只改 exporter 的 angular-nodes。[S6]

完整尾的 planar signed Fourier cutoff K 和径向 Hermite 网格定义实际有限图。原 R18 的 K96/N256/4638节点，到 R21 的 K192/N512/18553节点，确有表示加密；M12第二档20953节点另提供共同外域对照。最终 M15 的 endpoint-critical 表示采用已审的新节点规则，实际节点/系数仍必须由最终成功 CP 导出后记录，不能用 quarter 的 plan-only 节点数假称已导出。

exporter 的 angular-nodes 同时改变局部 root/RK 求积和 Fourier 提取，不是纯显示分辨率；固定 CP 后增加 flow-steps 也不是重新 shooting。两档 exporter 是两个明确的有限图，报告其实际定义即可，不能给它们换成另一实验名称。

## 5. 时间方向已被解析覆盖，不需人为制造时间误差

在活动带的物理角坐标中，$g$ 是旋转对称度量，令 $\tau_\alpha$ 表示角平移。R17/R21 定义

$$
F_\alpha=R_\alpha\circ F_0\circ\tau_{-\alpha},
\qquad \alpha(t)=2\pi t/3,\quad 0\le t\le1.
$$

空间旋转保持欧氏度量，角平移保持活动带上的 $g$。因此

$$
F_\alpha^*e-g
=\tau_{-\alpha}^*(F_0^*e-g).
$$

把一个 $g$ 单位正交标架通过 $\tau_{-\alpha}$ 推前仍得到 $g$ 单位正交标架，所以相对 tensor 的 operator norm 在对应点相等。角平移是活动带的双射，故其空间 supremum **对所有实数相位完全相同**。固定帽单独满足 $F_t=F_0$，其目标是固定诱导度量，误差为零。分块的公共两 jet 保证全局 $C^2$，不必把“带上角平移、帽上恒等”硬说成整个参数面上的一个全局角平移。

这里的平移是物理 $\theta$，不是直接把适应性角 $\psi$ 减去 $\alpha$；两者由冻结关系 $\theta=\psi-e(s)\sin(3\psi)/3$ 区分。最终家族必须沿该已审定义构造。

所以本算法没有时间步长引入的 metric 截断误差。解析全时证书已经比任意有限时间加密更强；不能要求一个本来已精确消去的时间误差继续严格下降。若干 t 网格用于第7项的交付/实现核对，不能代替上述全时证明，也不必为 G5 重跑密集的时间采样。[S3,S10]

## 6. 若新完整误差到 B，为什么不自动追加最终高模 RK 门

直接认证的新有限图满足 $\mathcal E_{15}\le B$，就排除了**这张图的实际净 metric 缺陷大于 B**。它并不说明源 RK 的独立误差、某个 Fourier 系数误差或所有二阶 jet 都各自小于 B；这些是不同命题。

已有 M8 网格轨迹、M12 的更高频/更细实际表示、明确的 R19 表示一致性和同 g 的 R6 误差机制，再加一个达到原容差的最终 M15 图，足以形成题目要求的**数值收敛证据包**。README 没有要求在每个最终阶数上把所有离散方向分别做完一次单因素实验，更没有要求一个已经达到原容差的分量再严格下降。

作为可审主线，应明确写出指定完整图的实际下降子序列

$$
F^8\longrightarrow F^{12}\longrightarrow F^{15},
$$

同时完整保留 M14 非单调诊断和其它失败尝试。R21 已证明 $\mathcal E_{12}<\frac{50}{393}\mathcal E_8$；若未来 terminal 正常门通过，则由指定 M12 点下界与新完整界证明

$$
\mathcal E_{12}>9.79415\,\mathcal E_{15}.
$$

这才是两次实际改善，不是对几个可任选上界的挑选。它不声称所有曾试过的 M 都单调，也不证明无限序列必然继续下降。有限计算本来不能给出后一个严格极限定理，必须按第7项如实说明。

若还要**额外断言最终源 RK 已经单独收敛**，现有 M8 对照确实不够，应做同 M15/N512/p8/depth12 的 steps32→64 原真联解，再比较实际图；固定 CP 的 exporter 加密不能代付。但这个额外源命题不是在完整 metric 已到 B 后自动新增的 README 门。

## 7. 必需动作与有证据才触发的加密

| 类别 | 最小动作及验收 |
|---|---|
| 尚必需：真正最终源 | continuation 到原 s=1 后完成原 M15 prefix 外层，再按已审 N512 接续计划真实校正。所有原 tol/BC/floor、真实最后 audit、源哈希、PP 分片及 cut 请求连接闭合。 |
| 尚必需：新实际图 | 从这一最终 CP 导出明确的 XYZ、同图 R6、共同两 jet、镜像和固定帽；核新数据不变量，重证其完整 metric、实际曲率/支撑、握持和非全等。 |
| 尚必需：真正到原容差 | 新 whole 的精确全域误差必须 $\le1/500000000$；不能只过原 whole 的 $10^{-6}$ 门，也不能以 source residual 代替。 |
| 尚必需：实际下降与身份 | 实际运行 terminal gate 正常分支，把新图接到固定 M12 点见证；保留 same-g、同时间范围、同图证书和一次 bridge 转移。当前负例 PASS 不支付此项。 |
| 尚必需：冻结 G5 账本 | 记录本文六个旧闭点、最终 M15、每张实际图的 source/表示/验证参数及误差类型；将 M8/M12实际改善与新比较合并，保留 M14/失败/平台。明确时间方向由解析式覆盖。 |
| 触发：最终原生径向 | 只有实际新 metric 未达到原容差、出现无法解释的径向平台，或要报告最终原 RK 的独立收敛时，再做同 M15/N512 的真 steps32→64 校正；不把 exporter 代替。 |
| 触发：XYZ 表示 | 若新实际图被确认仍受插值/保留阶限制，固定相应源条件，仅针对已定位盒或 K 作更细实际图，再核其完整证书。不能仅凭大 fullTensor 或 rr 差自动加门。 |
| 触发：验证过估计 | 若实际点/采样与连续包宽分析显示瓶颈在背景供应或 Bernstein/角盒，细化验证包/域；这是同图证书收紧，不计作实际误差下降。 |
| 触发：R6 深度 | 只有该新图自身圆领误差预算未付或深度效应未被现有界覆盖时增加 export/shooting 数值深度；不改物理 protectCell/尺度/目标。 |
| 无需新增：时间步 | 对已审相位作用的族不需要时间积分/时间网格误差实验；但须核最终家族确沿此作用，不能仅检查端点。 |
| README最后仍必需 | 同一冻结最终图的若干 t 网格、文件大小及闭合/固定帽检查；未参与最终解计算者从明确前置初猜独立重跑最终成功原联解、表示、完整认证和网格。无需重跑所有历史失败路径。 |

若最终 N512 图误差高于 B，则本节的假设不成立，G5仍开。应该依据实际误差来源继续细化，不能把 B 改成较松数值，也不能把某次偶然较小的局部/源诊断解释为整图通过。

## 8. 对已有 final pipeline 的具体补记

既有 `tail-final-m15-minimal-pipeline` 和 `audit-m15-certification-readiness` 的数学分层正确，但其中若干“尚待实现”已经由后续闭件完成；旧文件保持原字节，本稿作只读补记：

- endpoint-critical exporter 已实现且独审/plan 重放通过：`db6f-prefix-endpoint-critical-increment-export.mjs`，SHA `993dc6a180b917132d8284fae6c6366b45dddd883f9c09ab50b2b1dcf87f593b`。仍未对最终 M15 完整导出。
- transfer-v3 与 consumer-v3 已成对独审，真实 quarter 仅做过参数预检；正式新 manifest 的转包仍须实际执行。
- terminal error gate 已完成全文审及真实 M12 负例重放；未来正常分支仍未执行。
- 真 N512 接续已有具体原 driver 模板；原 plan 中“建议N512”的部分应按本次最终流程落实，不能把角N只改在 exporter。
- 原文已经把最终径向对照写为“若还需排除新的径向限制”，与本次不自动追加门一致。新的 G5 汇总要补出**何者已付、何者仅为条件触发**，避免为了把表填满机械重跑所有轴。
- 缺的最终联合账本不能由一个 terminal PASS 布尔值代替。它应把实际图的连续误差、历史 refinement 和上述全时恒等式一起引用，同时保留严格存在性缺口。

R19只对“给定存在的 $C^2$ 源图及受控导数数据”证明积分 Fr 表示收敛；其误差中有 $\varepsilon_1/L$。它排除一种表示固有缺陷，但没有认证源 ODE/Fourier/无限尾存在。最终每张图的精确 $C^2$ 拼接和实际曲率须各自付清；两图 rr 差尚未到机器精度不能另作 G5 阻断，也不能借 R19 把未知源误差说成已界定。[S7,S8]

## 9. 来源与审查范围

以下均为本题仓库内已经读取的原始问题、真实闭记录或已审结果。精确文件哈希集合保存在同 stem 的 `-sources.json`；六份 CP 元数据摘录另见 `tail-g5-closed-sequence-inputs.json`。

- **[S1]** `README.md`，完成标准1–7，尤其第5项及第7项。
- **[S2]** `notes/2026-11-09-db6f-prefix-fixed-g-convergence.md`；其中原 M16“running”等历史状态不是当前完成状态，本稿只使用已有闭点及其原作用域；六份真实 CP/最后 tail 的身份另已核。
- **[S3]** `results/R21-m12-whole-map-and-actual-metric-decrease.md`，§1–3及固定 g 定义、实际改善。
- **[S4]** `notes/2026-11-09-db6f-prefix-m14-q512-and-m15-failure.md`，真实 M14/N512 校正及原 M15 失败范围。
- **[S5]** `notes/2026-11-09-db6f-tail-m12-depth-collar.md`，宏观同 CP 深度6/8/10/12账本及明确限制；与实际 exporter collar 不混用。
- **[S6]** `notes/2026-11-09-db6f-prefix-final-m15-n512-followup.md`，未来N512原方程接续、真实验收和两个角数。
- **[S7]** `results/R19-integrated-fr-conditional-c2-convergence.md`，§2–5的条件一致性与作用域。
- **[S8]** `notes/2026-11-09-db6f-tail-m12-critical-two-grids.md`；`notes/2026-11-09-db6f-prefix-tail-m12-critical-c2.md`，同CP表示双档、连续差界及不新增C²门的明确范围。
- **[S9]** `notes/2026-11-09-db6f-audit-terminal-error-gate-method.md` 及 `scripts/db6f-audit-terminal-error-gate.py`，终值门、实际下降与非自动G5声明。
- **[S10]** `results/R17-exact-finite-visible-closed-geometry.md`，公共C²接合、空间旋转/材料角作用和固定帽；实际范围以R21同图输入为准。
- **[S11]** `scripts/closing_recalibrated_tail.mjs` 的 `createRecalibrationFactory` source创建，`scripts/closing_weighted_tail.mjs`，以及 `scripts/950f-prefix-adaptive-chart-bvp-v2.py` 的冻结角定义。目标的严格数学身份另由R21及六背景证明链支付。
- **[S12]** `notes/2026-11-09-db6f-tail-final-m15-minimal-pipeline.md` 与 `notes/2026-11-09-db6f-audit-m15-certification-readiness.md`，本稿仅补充分层验收，不改旧计划或阈值。

本稿是对 README 数值完成标准的有理由的实施判断，不是从有限个数据点证明一个无限极限定理。新 M15 尚无本稿假设的最终完整图或正常终门成功报告，故当前研究状态仍为进行中。
