# 固定 $g$ 的最终误差与实际下降：纯元数据后验门

作者：`/root/independent_geometry`，2026-11-09。

**本程序只合成已经严格认证且经过审查的完整有限图证书。它支付固定 $g$ 下的末端误差门及一次真实误差下降，不自动支付 G5 总门、最终独立全流程、无限存在或 README 完成。**

实现：`scripts/db6f-audit-terminal-error-gate.py`，SHA256 `1be7add52ec2c06653a2a64baa8653e675559a55551cf22603d14a80f9cfb234`。旧 `db6f-root-whole-metric-reach-v2.py` 和既有 M8/M12 文件保持原字节。程序没有导入数值后端，只有标准库 JSON、gzip 包装、流式 SHA256 与 Fraction 算术。

当前已实际运行的唯一算例是**真实、已冻结 M12 证据的负向检查**，结果为 `EXPECTED_REJECTION`。正常未来候选分支尚未执行；没有生成假候选、假 packet 或假 manifest。

## 1. 要证明的命题

对已明确组装的闭族 $F_t$，定义实际全域相对误差

$$
\mathcal E(F)=\sup_{t,x}\left\|
g^{-1/2}(F_t^*e-g)g^{-1/2}
\right\|_{\mathrm{op}}.
$$

程序固定原目标容差

$$
B=\frac1{500000000}=2\times10^{-9}.
$$

它没有可用于放宽门槛的 CLI 参数，不把浮点 `2e-9` 当成精确有理门槛。正常模式的结论是以下条件命题：若所有被绑定的解析、连续覆盖及闭图组装证书有效且已审，则

$$
\mathcal E(F_{\rm new})\le U\le B,
\qquad
\mathcal E(F_{12})>\frac{195883}{20000}\,\mathcal E(F_{\rm new}).
$$

程序核文件、对象和算术连接，没有重新生成上述连续证书。它不把求解器 residual、Galerkin/RK 诊断、节点采样或某个局部 angular 上界当成完整曲面误差。

## 2. 固定的旧 M12 见证

旧对象只取已审 R21 critical 第一档：

| 对象 | 冻结 SHA256 |
|---|---|
| M12 point 报告 | `13311ea4ecb781d0607ff6b58880c5f70bd79db2df2527aa9de3b6d9ad2e1b5e` |
| common-cut 几何 | `253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2` |
| critical-r01 manifest | `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104` |
| 完整 whole-v2 汇总 | `f329aaea39722b02b48ce98fe11e4232ae2c60b57a94789b071dfb5c915f49c5` |
| point 方法稿 | `955a6550b43efb88f25767eaa0636fdb2be6eb397175507319c96fdddb2b8f92` |
| point 独审 | `0105a546e1978533a9d6769204cd5910cede0e323b945b860806cf4f5da66466` |

M12 point 报告的身份在 `inputs.manifest / inputs.geometry / inputs.whole` 中；它与旧 M8 报告的顶层格式不同。本程序显式处理这个 schema，没有仅替换旧实际下降脚本的 witness 文件名。它核实际文件、point 与 geometry/whole/packet 的连接、六项背景及点公式源文件，并流式重哈希该真实 manifest 的数据分片。没有调用 point 算法重搜或重新数值积分。

报告的 `whole_actual_metric_error_lower_exact` 必须等于所选见证的精确 binary Fraction，且必须等于已独审端点

$$
L=\frac{370012576184137}{18889465931478580854784}
>1.95883\times10^{-8}.
$$

这里使用的是实际图上的合法单点下界，故 $\mathcal E(F_{12})\ge L$。不以 `requested_lower_proved` 布尔值或十进显示代替该精确量。

## 3. 同一个目标 $g$ 的身份门

正常模式从实际 whole 沿引用读入新 closed-budget 及其七个输入。新账本必须是已审 `db6f-audit-closed-budget-transfer-v3.py`（SHA `5ef8d229e0a19bc83381a2cdcaef8b24309e00a1fdc6b9409b20d7ca34092e49`）；whole 必须是冻结的 whole-v2（SHA `20d9b6127625595afaf14daac4d23ccdd68d10f5d3a36d0697472f5df50d8fc3`）。本程序不会为某个未知未来来源自动放宽允许集合。

### 3.1 前缀与材料坐标

新 common-cut 图及其 base 图的下列定义与旧 R21 目标一致：

- `frozen_profile`：含方向、vu/vd、ramp、cycles、cut、ramp law/eta 与 delta。
- 完整 `chart`：不是仅比较 chart 的说明字符串。
- `warp_reference_q`、`ell`。
- profile loader 与 profile implementation 的指定源码 SHA；实际文件也重核。

共同 cut、镜像和 tail reader 实现同样 pin 已审源码。几何必须是 `exact-common-cut-prefix`，并保留精确共同两 jet 与精确入口镜像的定义标记。其原始数据、base、checkpoint、port、最终 tail manifest 均按实际文件身份连接。

嵌入未知量 $q$、Fourier 系数、节点、求解状态和尾部数值网格不要求与 M12 相同。它们改变候选图，而不是许可修改目标 $g$；新图依赖的界仍须由新图自己的证书支付。

### 3.2 精确桥与较早的数值网格

程序比较现有实际下降证明使用的完整 exact bridge 字段：精确 cut 半径/斜率/二阶量、`exact_pt / exact_ps / exact_L`、根盒端值和正导数界、唯一根标记、`arclength_rescale / phase_upper` 以及已审桥实现。新桥必须绑定新 base 和实际目标 packet；目标 packet 的 frozen profile、bridge constants、供应器源、扩展 guard 与数据 SHA 也核对。

**桥证书可以引用同 $g$ 的较早数值 tail manifest。** 例如真实 M12 桥的支持 manifest 是 uniform `b202b471…`，而 R21 实际图的尾是 critical `cc23977e…`。桥的作用是确认精确目标和 cut，不是向新图转移旧尾误差或曲率。

桥 JSON 只保存该支持 manifest 的 SHA，没有文件路径。若它与最终 manifest 不同，正常 CLI 必须显式给 `--bridge-tail-manifest` 指向真实文件，程序核该 SHA、完成状态、实际 checkpoint，以及所有非数值白名单参数与最终候选及已审 M12 的一致性。即使 SHA 相同，也核其 checkpoint 参数连接。没有按文件名猜支持网格。

因此，许可的差异仅是数值表示/求解记录；所有影响 exact cut、root、target 的物理参数都保持固定。六项 calibration/alpha 背景定义另有固定实际文件门，不能由较早网格的 `physicalStats`、近似高度或单个 scalar $\eta$ 重新定义 $g$。

### 3.3 六项背景与严格参数策略

`checkpoint / calibrations / alpha / cell_zero_A / inner_A / outer_B` 六键必须齐全，各自固定为已审实际文件 SHA，并与 M12 point 目标映射一致。height 与 positive-alpha 沿用已审固定背景证明；tight-alpha 的 A/B、calibration、checkpoint 与共同 bookkeeping 连接也重核。

新 closed-budget 的正式 transfer 必须来自已审 producer v3，具有实际 `finished=True` 和 `mode=finite-background-grid-transfer`，而不是参数预检。程序 pin producer、旧 base 与 canonical policy SHA `2b4fd1d141d9116157037d05748ab2a019c9033441453ee8e6ab917eb355eae3`，比较旧新全部参数并核原包/原 data/新 data。

参数比较使用键存在性与严格 canonical JSON。除原数值键及四个已审 I/O/分配键之外的改变均拒绝；未知 `null`、布尔/数字别名及其嵌套变化不能隐身。新四键的类型也有明确门。

固定帽使用同一 R16 bump/cuff 定义；帽的竖直平移保持其诱导度量。该事实及固定源码/物理 cuff 的一致性解释 cap 的共同目标，不要求不同候选的帽绝对高度相同。

## 4. 新图必须使用自己的完整证书

### 4.1 前缀与精确桥转移

前缀 geometry、metric 和 moment 必须绑定**最终新 common-cut JSON**。不能把未修正的 base metric 接到已修正图，不能借用 M12 geometry 或 κ。新 tail-first 也必须绑定最终实际 tail manifest。

前缀 metric 允许两个已审来源：原系数后端或 first-tier angular wrapper。原后端报告未保存 target 文件路径，故必须显式给 `--prefix-target`；angular 报告通过 `inputs.target` 读取真实路径，若同时显式提供，也须同 SHA。

Angular 报告必须完整：全部目标区间、`requested_intervals=None`、完整分区复读标记、正确的最终图/base/target/bridge/baseline 身份，以及全部已写 row/summary 文件。selected-only 报告被拒绝。原后端也须全部 interval 覆盖。程序不把某两个局部测试通过解释成全域证书。

设对源目标的完整前缀上界为 $\epsilon$，桥给相对目标差异 $\eta$。沿已审变更度量不等式，真正固定 $g$ 的上界为

$$
U_p=\epsilon(1+\eta)+\eta.
$$

程序用精确 binary Fraction 和精确有理运算计算它，与 closed-budget 及 whole 对应字段比较。对 angular 输出，还核其 saved source exact 字段与兼容数值字段相同，再核已经输出的 exact-target 字段。**只转移一次**，不能把已转移字段重新当作 $\epsilon$。

### 4.2 整尾与圆领

完整 tail metric/κ 证书必须具有最终同一 manifest SHA、自己的 packet/data/row 文件和完整 tail+collar 范围；跨度、分区数量、所选范围和完成标记相互一致，曲率未决项必须全部解决。实际新 manifest 的分片 SHA、字节数、共享行数量与实际 checkpoint 也重核，但不解码数值数组或求值多项式。

背景曲率复用的是相同固定背景已证 $K_{\rm bg}\le6$；不得用更小但未证的 CLI 假设制造新图 κ。新图的 perturbation 曲率仍来自其自己的完整证书。

若给更紧 metric-only 证书，它也须完整、同最终 manifest、同六项背景、自己的 packet/data/row 文件，并明确没有曲率结论。此时可以保留**同一个新图**的原完整 κ 上界；不能借用旧 M12 或另一个 exporter 网格的 κ。

记两个有效尾误差界为 $U_f,U_m$，则

$$
U_t=\min(U_f,U_m)
$$

（没有 metric-only 时取 $U_t=U_f$）。帽的固定目标误差为零，因此

$$
U=\max\{U_p,U_t,0\}.
$$

程序精确核 whole 的原尾界、所选尾界和整体最大值。它也核 whole 的 prefix/tail/cap κ 来自此候选的三个分量，并重新核 $K=\max(K_p,K_t,10/3)$ 与 R10 的 $\min(\sigma,1/K)$ 算术连接。这里不重新认证曲率，只防止在汇总时换入另一张图的界。

在此后验门中，row/partition 文件只重新计算 hash；程序不逐行重证分区覆盖，也不从每个连续叶盒重新求全局最大值。完整覆盖依赖已审连续证书，另核其完整标记、计数、范围及对象连接。whole-v2 已有的行检查与最终独立完整重放不被这次元数据检查替代。

全相位上界沿已审 R17 空间旋转/材料角作用与固定帽组装。程序要求相应闭图/全相位前提；完整解析组装的有效性仍由既有已审方法和本候选实际证书支付。

## 5. 终值与严格实际下降的精确证明

后验门直接判定 $0\le U\le B$。原 whole-v2 的 $10^{-6}$ 成功标志不能代替这一步。

令

$$
F=\frac{195883}{20000}=9.79415.
$$

已审旧下界给出精确正余量

$$
L-FB=
\frac{61863470598928509}
{23058430092136939520000000000000}>0.
$$

若新图通过 $U\le B$，则

$$
\mathcal E(F_{12})\ge L>FU\ge F\mathcal E(F_{\rm new}).
$$

程序仍显式计算并保存 `L-F*U`，要求其严格为正。使用乘法不除以新误差，因此包含 $\mathcal E(F_{\rm new})=0$ 的情况。若打印 $L/U$，只能把它当界的比例，不能未经严格余量证明便把它写成实际误差比的严格下界；本程序不需要该除法。

通过时输出 `PASS-terminal-fixed-g-error-and-one-actual-decrease`，以及精确 $B,U,L,F$ 和两个严格余量。身份/来源错误立即拒绝且不写成功报告；数值门未过时输出 `REJECTED-terminal-error-or-decrease-gate`、`certificate_issued=False`，以非零退出码结束。

## 6. 真实 M12 的唯一负向实跑

命令从仓库根目录执行：

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-audit-terminal-error-gate.py \
  --check-m12-negative \
  --out topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-audit-terminal-error-m12-negative.json
```

该模式与 `--whole` 互斥，也禁止未来 target 或桥支持输入；只读已指定的真实 M12 引用。它不进入正常候选分支，不为旧 closed-budget v2 或旧 transfer 放宽正常入口，不生成新 packet/manifest。

真实完整 M12 上界为

$$
U_{12}=
\frac{38493756262750339563330485335957988971213899}
{1496577676626844588240573268701473812127674924007424}>B.
$$

同时 $L>B$。前一条说明当前完整上界不能通过新门；后一条更强，证明该**实际 M12 图**不可能具有 $\mathcal E\le B$，不是仅仅估计偏松。因此这个真实对象是合法的负向测试，不是人工制造的坏 packet。

实际执行 exit 0，测试状态为 **`EXPECTED_REJECTION`**，并明确：`test_only=True`、`certificate_issued=False`、`candidate_binding_branch_executed=False`、`future_candidate_was_created=False`。测试程序退出 0 表示预期拒绝被正确观察，不表示任何新图通过。

该次运行重核 48 个真实文件，用时约 0.324 秒，峰值子进程 RSS 16,183,296 bytes。输出 SHA256 为 `3f75f6668aaf0c90dbca169e353a6eb9d8df38de8e01b24acf0bafcd7daaa213`；同 stem 的 `.log` 和 `.execution.json` 保存实际 argv、源开始/结束 SHA、退出码和资源记录。没有重新运行 point、grid、metric、κ、root、flow 或 solver。

## 7. 正常入口的未来使用与剩余责任

只有实际最终图及全部已审输入已经存在，才运行正常模式：

```bash
python scripts/db6f-audit-terminal-error-gate.py \
  --whole <实际已成的最终whole报告> \
  --out <新的后验报告路径>
```

若使用原 prefix 后端而非 angular 的显式 inputs，加 `--prefix-target <实际目标文件>`。若桥保存的支持网格 SHA 与最终 manifest 不同，加 `--bridge-tail-manifest <该真实支持manifest>`。这些是明确的真实输入路径要求，不是待创建的示例 packet。输出路径已存在时程序拒绝覆盖。

源代码和本稿另交未参与实现者独立审查；本次正常候选路径只做静态接口检查，没有未来完整图的实跑或 PASS 记录。后续实际候选必须重新执行它，并仍保留最终未参与优化者的端到端重跑职责。

无论负向测试还是正常门成功，报告都保持 `fixed_g_convergence_gate_5_paid=False`、`independent_final_full_pipeline_verified=False`、`infinite_solution_existence_proved=False`、`README_complete=False`。后验误差门与一次真实改善是完整研究证据链中的两个明确组成部分，不能借布尔标记替代其余完成条件。
