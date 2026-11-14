# G5 加密轴澄清与同一 M14/W14 的可选原生径向接口

2026-11-09，`/root/coupled_prefix`。本稿只读复核既有说明、三个历史 M8 真联解及当前 true M14 的冻结输入；没有读取活动 trace 来推断结果，没有运行 BVP、DN、root、RK、导出或连续后端，也没有创建未来配置、候选 CP 或成功包。旧稿、当前运行和所有旧绑定保持原字节。

## 1. 澄清对象与原有 G5 判断

澄清对象是 **root/H 即时文字中“native N256→512”可能误导的简称**。全文复读的 `tail-g5-final-m15-sufficiency` §3、§4.2、§6，以及 `prefix-final-m15-n512-followup` §1，已经正确区分尾角求积与原生径向 RK；两份旧稿没有这项记账错误，无需撤销其原审查。

准确表达应为：

> 尾角求积 `quadrature=256→512` 的原方程真校正；`shootingParts=8`、`steps=32` 保持，每个 raw profile 仍有 256 个基础 RK 区间。

下文把尾角数写作 $N_\theta$，每个 shooting stage 的基础 RK 步数写作 $S$，shooting parts 写作 $P$。`N512` 不是 512 个径向 RK 步，也不是 512 个 Fourier 未知模，更不是更改 `calibrationSteps` 的指令。

本稿**不新增 G5 完成门**。旧 G5 稿的充分条件仍是：真正最终同一问题的联合源、明确的完整实际闭图、全域实际等距误差达到原 $B=2\times10^{-9}$、与已有加密轨迹的真实身份和误差下降联系、全时解析证明及最终独立完整重跑。它从未要求每个最终模数都再做一套独立 RK 实验。若额外要断言“当前高模源 RK 误差已单独收敛”，或者已定位实际误差仍受该轴限制，才使用本稿 §4 的可选接口。

旧稿的 M15 是当时具体路线的名字，不是 README 强制的模数。当前 M14/W14 若将来取得完整真联解并支付相同的实际图与 G5 证据，可以作为同一冻结几何的候选；本稿不预判其成功。当前已在 $N_\theta=512$ 运行，并不需要把它先改回 256 再称为“径向加密”。若另做同 W14 的 256/512 对照，该实验仍须明确称为**角求积对照**。

## 2. 各轴的实际来源

| 数值量 | 当前 true M14 输入 | 改变的对象 |
|---|---:|---|
| Fourier 模数 $M$ / spacing | 14 / 3 | 有限投影未知量；不是角求积节点数。 |
| 尾 `quadrature` $N_\theta$ | 512 | 原 moment root、RHS、variational RK 与 DN 的角规则。256→512 必须重新真求解。 |
| 尾 `shootingParts` $P$ | 8 | 每个 raw profile 的 multiple-shooting 分段和端口未知量布局。 |
| 尾 `steps` $S$ | 32 | 每 stage 的基础 RK 网格；当前每 raw profile 为 $PS=256$。 |
| 尾 `auditSteps` | 32 | 成功源响应的诊断遍历步数；单改它不会重新求解 shooting 方程。 |
| `linearSteps` / `linearFar` | 256 / 32 | 原稳定线性图及远端 Robin 的数值构造；与非线性 `steps` 分开。 |
| prefix `--angular` | 512 | prefix Fourier 投影角规则；与尾 $N_\theta$ 是独立输入。 |
| prefix `--audit-angular` | 1024 | 保存 prefix 诊断的角数，不是求解加密。 |
| seam `angular_samples` | 原公式将为 896 | $\max(512,64M)$；最终是否实际产生仍须闭包审计。 |
| prefix mesh / `max_nodes` | 保存初值、自适应 / 6500 | 经向配点；不能由尾 `quadrature` 推出其网格变化。 |
| W14 | 原已审二幂正对角 | 同一未知量/残差的坐标共轭，改变误差控制与数值轨迹；不是新增 Fourier 模。 |
| `calibrationSteps` / `warpSteps` | 512 / 16 | 冻结背景生成设置，本次两条加密接口都不改变。 |
| shooting depth / protectCell | 12 / 160 | 同一无限背景的有限求解截断 / 冻结物理源表；不能混用。 |
| 导出 Hermite 网格 / planar Fourier cutoff | 尚无此新 CP 的导出 | 定义实际有限 XYZ 图；固定旧 CP 后只加密导出，不等于原生 shooting 重求。 |

`950f-tail-subdivision.mjs` 把 raw profile 的 $x\in[0,1]$ 分成 $P$ 个 stage，每个 stage 按 $S$ 个基础区间积分。因此 raw 参数中的基础最大步长为

$$
\Delta x_{\mathrm{base}}=\frac1{PS}.
$$

这个 $x$ 不是物理半径 $r$。当前 cusp-aware 两条实现又把基础区间在原 profile 的 `integrationBreakpoints` 处切开：state-only 使用 `splitIntegrationInterval`，variational 使用 `integrationGrid`。所以 $PS$ 是**基础区间数**，并非有 cusp 时全部实际 RK 子步数的严格等式。将 $S$ 加倍保留旧均匀节点和同一 cusp 点，确实细化原生积分；不更改 profile。

`closing_recalibrated_tail.mjs` 创建背景 source 时显式使用 `modes:1, depth:protectCell, steps:1, quadrature:16`。外层 `steps`、$N_\theta$ 不会通过该调用重新设计背景。固定背景的函数身份仍由原几何证明及全部冻结来源共同支付，不只靠相同数字字典。

## 3. 已有 M8 原生径向证据逐字段复核

本次直接读三个已闭 prefix CP，再按各自 `tail_seam.tail_record` 读它自己的最终真响应；核 CP/响应 SHA 等于旧 `tail-g5-closed-sequence-inputs.json`，响应 config 等于 CP 的 `tail_config`。新伴随 `-metadata.json` 保存完整路径、精确 SHA 和以下小字段，不含大数组。

| 真实已闭项 | M8/32 设计联解 | M8/64 固定 g | M8/128 固定 g |
|---|---:|---:|---:|
| prefix angular | 256 | 256 | 256 |
| prefix tol | $2\times10^{-7}$ | $2\times10^{-9}$ | $2\times10^{-9}$ |
| prefix `fixed_metric` | false | true | true |
| prefix 节点 | 778 | 2570 | 2570 |
| physical shooting depth | 10 | 10 | 10 |
| parts $P$ | 2 | 2 | 2 |
| native steps $S$ | 32 | 64 | 128 |
| auditSteps | 32 | 64 | 128 |
| 基础 $PS$ | 64 | 128 | 256 |
| 尾角 $N_\theta$ | 256 | 256 | 256 |
| `linearFar` / `linearSteps` | 32 / 256 | 32 / 256 | 32 / 256 |
| `calibrationSteps` | 512 | 512 | 512 |
| tail solveTolerance | $2\times10^{-9}$ | $2\times10^{-9}$ | $2\times10^{-9}$ |
| tail maxIterations | 30 | 36 | 36 |
| response parameters 的 stage `depth` | 180 | 180 | 180 |
| 原 floor | .05 | .05 | .05 |
| 最后请求 Jac / audit | true / true | true / true | true / true |
| 最后 residual | $1.3505653752886372\times10^{-10}$ | $1.872382418274325\times10^{-10}$ | $8.191673022591901\times10^{-11}$ |

三份 CP 均保存真实 `solver_success=true`、`actual_nonlinear_tail=true`，末响应均真实 `converged=true`。三个输出的原六个冻结物理字段逐值同；第一行在设计求解后选择这些最终字段，不能把它说成从求解一开始便固定 g 或已用后两行的 prefix 容差。

所以**原生径向轴已有实际完成的求解与比较证据**，不是尚待未来 N512 才首次支付。其范围必须保留：

- 32→64 同时收紧 prefix 容差并增加配点，因此不是严格单因素实验；64→128 保持后者容差及2570节点。
- 64 与128的实际 DN 求解路线不同（原每次真 DN / 已审 outer-actual-inner-affine），二者最后都重新通过原真方程与实际 seam；这不是把仿射响应列作真解。
- 原 `prefix-fixed-g-convergence` 的共同物理坐标比较是 prefix 的采样 $C^2$ 诊断，不是新的全域误差定理。该表的源 metric 平台和非单调尾采样最大值也不能隐藏。
- 这条已有轨迹可以作为原 G5 证据包的径向部分；它不是所有后来 M14/M15 的统一 RK 误差上界，更不能单独宣布 G5 完成。

## 4. 未来真正 M14/W14 结果后的最小可选径向接口

### 4.1 前置输入必须是真正关闭的联合结果

baseline 必须是当前或后来同一 M14/W14/N512 的真正成功 prefix CP、全部 PPoly 分片，以及它**自己**指向的最后 Jac/audit 真 tail response。须由其专属 readonly final auditor 核原 RMS、真实 outer BC、末 seam 身份、有限系数、同 g 和 root 实际工具退出。不能用 affine01、首个真 DN、活动 iteration、捕获异常后的 exit0 或未成功的 continuation 代替。

本稿不称当前这些文件已经产生。当前运行 `spectral-true-m14q512-01` 的输入已闭，运行结果尚待 root 观察；本稿没有读取活动输出来确认它。

### 4.2 仅改非线性径向策略和独立 I/O

从 baseline 的完整 config 复制，第一档只将

```text
steps:       32 -> 64
auditSteps:  32 -> 64
```

其余数值与物理键逐字段、逐类型保持：M14、spacing3、tail $N_\theta=512$、depth12、parts8、linearFar32、linearSteps256、原背景/calibration/cusp 设置、tail tol $2\times10^{-9}$、maxIterations36、原默认 floor .05，以及开启的原 boundary warm 修正。

`auditSteps` 同步只让源诊断与新原生步数对应；**真正改变 shooting 方程的是 `steps`**。保持 `linearSteps=256` 是为了把远端线性图固定在同一个离散边界，隔离本次非线性 RK 轴。若以后有证据指向该线性图的误差，另作有标签的 `linearSteps` 加密并重新真解；不得把此处 s64 宣称为所有径向近似都已独立收敛。

五个原 I/O 键按原协议隔离：`initialCheckpoint` 改为 baseline 自己的最后真 tail；`traceFile`、存在时的 `iterationCheckpointFile`、`trialDiagnosticFile`、`trialStatePrefix` 指向全新 stem。不存在的可选键仍保持不存在；普通 shared client 不消费两个 trial 路径。

### 4.3 warm 与原自由 cut 外层

同 $M=14$、depth12、parts8 时，所有新 stage 仍对齐旧 stage。原 `remeshCheckpoint` 读取旧保存 Q/Pi，在整数 `rawLeft*oldParts` 分支直接复制；不会为了改变 `steps` 而调用插值 RK。它构造旧 engine 供潜在插值，但本布局不进入该积分分支。state 数仍865、每行28，raw镜像仍13行，stage depth仍864。

这只提供初猜。fresh shared client 的 cache 为空，新 `dn` 按 `steps=64` 创建；原 warm ratio 和全模线性 boundary 修正仍保留。prefix 继续从原保存的物理 PPoly/mesh 初始化，$p_0$ 与其余自由参数继续由**原自由 cut BVP**求解，不强制保持旧 H。原 restart 的舍入差只走既有 boundary warm 协议，不改写旧解。

W14、prefix角512、audit角1024、tol $2\times10^{-9}$、bc_tol $10^{-8}$、physical_bc_tol $2\times10^{-11}$、max_nodes6500、Node heap1536保持。仍用空 `--warmup-scales`、`--fixed --lagged-tail --preserve-restart-mesh`；每个候选仍取当前 s64 的真 DN/J，原最多8轮 outer 及最终 `jacobian=true,audit=true` seam 不变。

### 4.4 当前硬绑定入口不能直接改 config 后复用

当前 `db6f-prefix-spectral-true-m14.py` 的 `validate_inputs` 明确要求 steps32/auditSteps32、原参考输入和完整 config 同一；其 auditor 又把 response.parameters 与旧真实 warm 参数作严格比较。因此，只改 config 或 command 再调用当前已审 selector，会被身份门正确拒绝。

将来若启动此轴，应另建**最小新版本** selector/preparer/auditor，并重新审其差分，保持当前已绑源码不动：

1. 接受一个通过当前专属 final audit 的 baseline；绑定其实际 CP、全部系数、最后 tail、reproduction、root 观察与审计报告。
2. 由 baseline 构造唯一允许的下一 config：上节两个数值键及独立 I/O；所有剩余键 canonical 同一。response.parameters 同样只允许这两个数值键与 I/O 的明确变化，不能用无范围的参数忽略表。
3. 原 delegated parser argv 只替 `--restart`、`--tail-config`、`--out-prefix` 为上述 baseline/new stem；profile/chart/port/source-root及全部原求解参数保持。继续由新 selector 注入同一已审 W14；**直接运行原 flat-coupled.py 不会自动获得 W14**。
4. 新实际 command 仍沿 `python <新selector> --launch <新绑定launch>` 协议，由 root 持有工具会话。这里没有创建该未来 selector、launch 或可执行命令，也没有把旧 s32 launch 冒充新 s64 来源。
5. 保留原运行期 Newton、物理回调和返回物理 PPoly 身份门。M14 的43状态/14参数/13 correction scales、616 Jacobian项、17 jets字段、8 audit字段、896 seam角数等尺寸不变。

原八个 shared 数学源无需因 `steps` 改变而修改；新 Python 选择层与参数绑定有新的诚实身份。几何证书必须绑定新实际图；旧 XYZ、prefix/尾 metric、reach 和握持数值不能转移为新图的结论。

## 5. 最小序列、停止位置与 G5 范围

条件序列为

$$
(M14,W14,N_\theta512,P8,S32)
\longrightarrow
(M14,W14,N_\theta512,P8,S64)
\longrightarrow
(M14,W14,N_\theta512,P8,S128),
$$

最后一箭头只在需要分辨径向平台、给出第二对差值，或明确研究该独立源误差时实施；不是预先新增的完成门。三档基础 raw RK 区间数是256、512、1024，全部同一物理 g、原 tol 和同一时间范围。prefix自适应网格及自由端迹可随真耦合响应变化；这是同一问题的解，不是另设一个固定 H 的辅助问题。

每档都必须有真正全 outer 和自己最后的 audit seam，再按最终管线生成自己的完整 XYZ/C²公共接缝及全域证书。仅将 exporter 的 `flow-steps` 或 Hermite 节点加密、只重算一次源 RHS、只取得较小 DN residual，均不构成上述箭头。

已有 M8 的径向轨迹继续保留；已有 M12 的实际全图下降及当前待解的 M14/W14 也必须分别注明各自的模数、角规则、native RK、配点策略、XYZ表示与验证网格。W14 的引入不是纯模数实验，不能把改善全部归因于 M12→M14。

若指定的新完整图已达到 $2\times10^{-9}$ 并付清旧 G5 充分条件及 README 其它门，不因本稿再强制加一档 s64。若未达到，按已定位误差来源继续工作；本稿既不放宽容差，也不提前宣布径向一定是主因。时间方向仍由原已审相位作用的全时恒等式覆盖，不添加虚构的时间积分误差。

## 6. 精确来源与复核范围

同 stem 的 `-sources.json` 记录实际读取且不可变的来源 SHA/字节，包括 README、两份旧稿、旧 G5 六点表、原生积分/细分/warm/背景 source、当前 true selector/preparer/auditor/config/launch，以及三个历史 M8 CP 和其各自最终 tail。`-metadata.json` 是本次直接从这些真实闭包提取的小字段，不包含新候选数据。

本次历史参数复核只重读已有文件，不重跑历史 solver；其来源范围和旧数值/连续证书区别均保留。HANDOFF 的即时状态由 root 更新，本稿不绑定会继续变化的 HANDOFF 文件，也未对它作编辑。
