# 谱权坐标接入原 M14 真联解：最小静态接口

2026-11-09，`/root/coupled_prefix`。**仅纸面与冻结源码阅读；没有实现新选择器、生成新配置或调用初始化、BVP、DN、root、flow。** 本稿不假定尚未运行的谱权 affine 试验会成功或改善 metric。来源及本文哈希见同 stem 的 `-sources.json`。

## 1. 结论与不变的目标

若已准备的 M14/N512 affine 谱权试验实际改善了保存的物理 prefix，可用一个另存的选择器把**同一已审谱权 callable**接到原 `db6f-prefix-coupled.py` 的真实外层。原代码两处 BVP 调用都解析其 module-global `solve_bvp`，不必改 PDE、边界、tail engine 或冻结原文件。新运行仍必须完成自己的真实 DN/J、原外层 BC 和最后真实 seam audit；affine 成功本身不能支付这些条件。

README 的完成标准没有规定必须取 M15。M12→M14 已增加 Fourier 模数，若将来 M14 的真实完整图达到原 $2\cdot10^{-9}$ 求解精度目标，就应按同 $g$ 的实际加密证据评价。此前 M14 非单调结果必须保留；加入谱权同时改变数值误差控制，不能把新旧差异声称为纯模数效应。此处也未降低 README 的任何几何、全时或独立重跑要求。

候选保留的设置为：

| 项目 | M14 真联解设置 |
|---|---|
| 固定几何 | 原 flat17 frozen profile、chart、physical tail parameters/cut、`warp_reference_q=.1`；原有限校准与 exact target 不改 |
| prefix | $M=14$，`angular=512`，`audit-angular=1024`，固定 gauge `.1`，原自由参数继续求解 |
| tail | spacing3、physical depth12、parts8、steps/auditSteps32、N512、36 轮、`solveTolerance=2e-9` |
| 原 guard | `projectionFloor` 省略时仍由已绑源码取 `.05`；`correctInitialBoundary` 省略时原修正保持开启 |
| prefix 原门 | `tol=2e-9`、`bc_tol=1e-8`、`physical_bc_tol=2e-11` |
| 资源预算 | 若采用 affine 试验的 `max_nodes=6500`，明确它相对旧 M14 的4000只是上限变化，须由 root 先核资源 |

所有“相同配置”均应按 canonical JSON 保留键存在性及 bool/number 类型，不能用 Python 的 `True==1` 作为同一物理输入证明。

## 2. 权重改变什么

原前缀有 $n=3M+1=43$ 个状态，$p\in\mathbb R^{14}$。已审 `db6f-root-spectral-collocation-v2.py` 取

$$
W=\operatorname{diag}(1,w_1,\ldots,w_M,w_1,\ldots,w_M,w_1,\ldots,w_M),
\qquad 1+(3j)^2\le w_j<2(1+(3j)^2),
$$

其中每个 $w_j$ 是二的幂，M14 最大值2048。置 $u=Wy$ 后，原离散前缀方程及 BC 被等价写为

$$
u'=W f(x,W^{-1}u,p),\qquad b(W^{-1}u_a,W^{-1}u_b,p)=0.
$$

实际 Jacobian 是 $W f_yW^{-1},Wf_p$，两端 BC Jacobian 的状态列除以 $W$；$p$、BC 值、物理角基及 $g$ 不变。`TailMixin` 因而收到物理 $y,p$，请求的高度仍是 $H=\sigma q_gY_Z$，没有额外的谱权乘因子。

这不是逐位相同的 Newton 轨迹。带权归一残差的一维形式为 $|y'_j-f_j|/(w_j^{-1}+|f_j|)$，原形式为 $|y'_j-f_j|/(1+|f_j|)$；误差控制更关注原本很小的高模分量，且原 domain-aware Newton 的步范数/回溯也在所传入的数值坐标中计算。零点集合不变，不保证节点数、收敛速度或实际 metric 改善。

已审 callable 返回**物理** `y/yp/sol`，`sol` 仍是数值 chart 坐标上的 cubic PPoly，并重新计算原物理 RMS/BC；不能把其带权 RMS 写作原物理 RMS。它只会把原 residual 门不合格的成功降级，不会把原失败升级。随后继续原代码的
`chart(sol.x,p0)`、`flow.c2_interpolant(physical)`、`adaptive.audit` 和 `seam_audit`。
新保存对象是原定义的物理 quintic；cubic 的 RMS 并不等于该 quintic 的连续 metric。未知量的二幂缩放还保留原 round-trip/有限性拒绝；不以截断或裁剪绕过异常。

## 3. 最小选择器的实际插入点

未来新文件可加载冻结 `db6f-prefix-flat-coupled.py`，取得 `.m`，只替换其 `m.solve_bvp`，再调用原 `m.main()`。本稿**没有创建这个文件**。保留原 flat patch、原 parser、原 source-root 安装、原 BVP 类与全部 callback，且不替换 `TailMixin`、`AffineTailForInnerBVP` 或 `solve_with_actual_tail`。

必要的薄审计层应围住每次谱权 callable：

1. 原 main 在首次 BVP 前会调用 `f6curve_domain_newton.install()`。在实际调用时核 `_bvp.solve_newton is domain_newton.solve_newton`，并绑定该运行函数的文件、源码 SHA、qualname 与11参数签名；返回/异常时保留身份核查结果。SciPy 磁盘 SHA 只支付其被审布局，不能替代运行期 patched 函数身份。
2. 每次仍接原 `fun/fun_jac/bc/bc_jac`，原参数及容差；记录该调用的 weighted/physical residual、节点数、状态和异常。原代码调用前后将 `o.tail` 暂设 affine、再用 `finally` 恢复真正 tail 的控制流保持。
3. 将谱权记录及新选择器/已审模块/完整旧源闭包放进**独立运行 reproduction**，绑定最后 CP/summary/seam。原 main 不保存 `spectral_coordinate_audit`，所以只替换 callable 后不能声称这些信息已自动进入原 CP。
4. 不把新选择器冒写成旧 driver SHA；不改真实 tail 包的八源身份。纯 prefix 谱权选择器属于新的 prefix 来源，tail 仍是原 shared 八源。若以后另采用线性 DN adapter，则必须另外绑定那个真实来源，不能混称本最小方案。

原 lagged 路径保持完整：初始真实 `solve(H, jacobian=True, audit=False)`；最多8次内层谱权 BVP；每次内层成功后对其新 $H$ 重求真实 DN/J，再按原 `o.bc` 检查；末 seam 调用 `jacobian=True,audit=True`。这不是把 frozen affine port 作为最终端口。

## 4. 优先用 M14 自己的真实闭输入

基线 stem 是
`2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14`。
其真实 CP SHA 为 `3df8eefb18c4271283c7ae2b076afcda3fb42b169c8a7296ee4bce3e3b3ad3d0`，自己的最后 `_tail_0002.json.gz` SHA 为 `009bf5472ca412fae7d900d4ec18d26cd217221138666c2899dfceb3ead8f762`。这是已有完整 M14 来源，不是当前 M15 延拓记录。

准备前复核这份 CP/summary/reproduction、所有系数分片及它自己的 `tail_seam.tail_record`；原 `load_checkpoint` 不主动核分片声明 SHA，须由新准备绑定支付。直接用这份真实 prefix 作 `--restart`，以自己的真实末 tail 作 `initialCheckpoint`。原 preserve-restart 的六个固定字段检查、物理 mesh/chart 反解、自由参数及入口初猜修正原样保留。实际首请求的 $H$ 以重建初猜为准，不能假定 PPoly round-trip 与旧记录逐位相等；仍让原全模线性边界修正和真实 DN 验收处理它。

若将来想把谱权 affine 产物改作初猜，它只能作为**明确 UNSOLVED 的几何初猜**另绑，仍用真实 tail warm 并对新 $H$ 真求解；不能保留其 affine 结果而改标签称“真联解”。当前最小入口优先上述原 M14 真闭输入，避免同时引入另一个 warm 改动。

新 tail config 从该基线完整复制；N512 首轮除下表 I/O 外全同：

| I/O 键 | 独立新路径 |
|---|---|
| `initialCheckpoint` | 上述自己的真实 `_tail_0002.json.gz` |
| `traceFile` | 新 stem 的 `-tail-trace.jsonl` |
| `iterationCheckpointFile` | 新 stem 的 `-tail-iteration.json.gz` |
| `trialDiagnosticFile`、`trialStatePrefix`（若存在） | 新 stem 对应路径；普通 shared 源不消费这两键，但仍不得指向旧输出 |

真实旧 M14 config 没有后两键，应保留这种缺席；不需为本方案添加它们。原 `freeze-refine.py` 不能直接选择谱权入口，且不全面隔离五 I/O，不应声称其原 CLI 已实现本方案。使用其原子 coupled argv，在新选择器、tail-config、out-prefix、restart 与明确节点预算这些位置作可审替换即可。

下列是**未来模板，第一项选择器尚未实现，不能直接运行**。cwd 为仓库根，`TOPIC=topics/visible-flexible-closed-surface` 仅为短写：

```bash
python <NEW_REVIEWED_SPECTRAL_COUPLED_SELECTOR> \
  --source-root "$TOPIC/repro/source-root" \
  --profile "$TOPIC/notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14-frozen-profile.json" \
  --chart "$TOPIC/notes/2026-11-09-950f-prefix-adaptive-chart.json" \
  --linear-port "$TOPIC/notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json" \
  --tail-config <NEW_M14_N512_CONFIG> --out-prefix <NEW_UNUSED_STEM> \
  --restart "$TOPIC/notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14.json.gz" \
  --amplitude .1 --warp-reference .1 --modes 14 \
  --angular 512 --audit-angular 1024 --nodes 1601 --max-nodes 6500 \
  --tol 2e-9 --bc-tol 1e-8 --physical-bc-tol 2e-11 --node-heap 1536 \
  --fixed --warmup-scales --lagged-tail --preserve-restart-mesh
```

`--warmup-scales` 明确为空。`--nodes1601` 不覆盖保存 mesh；实际节点以原 restart diagnostics 为准。新 stdout/reproduction/guard/观察文件也各用新 stem，拒绝覆盖。原 coupled 会捕获异常而仍可能工具 exit0；独立 reproduction 与 root 的真实工具观察必须分开，不能由程序自填“真实退出”。

## 5. 真正关闭时的 M14 等价 schema

不是删除 M15 门，而是另建 M14 运行身份并代入原维数公式：

| 对象 | M14 | M15 原门 |
|---|---:|---:|
| prefix 状态 $3M+1$ |43|46|
| 自由参数 / 中央高模尺度 |14 / 13|15 / 14|
| tail `heightJetJacobian` $(3M+2)M$ |616|705|
| `jets` |14个标量 + 三个长14向量|14个标量 + 三个长15向量|
| staged states / rawStates |865×28 / 13×28|865×30 / 13×30|
| seam 角样本 `max(512,64*M)` |896|960|

shape、有限非bool、typed config、真正八源、原 `<2e-9` tail residual、Jac/audit 真请求及八项 audit 字段均保留。必须沿新 CP 的 `tail_seam.tail_record` 定位最后包，并核请求的真实 $H=\sigma q_gY_Z$、jets/residual/config 与同一 CP；不能猜固定 call 序号。最后请求 audit 真会绕过原 shared cache。

关闭审计还须核新 root 工具观察、summary/CP 无 error且 `solver_success is True`、完整 coeff/hash/严格 mesh、原物理 RMS、所有实际 outer 检查的成功及末原 BC、最后完整 seam。原 main 在 seam 前先保存一次 CP：文件存在、actual_nonlinear_tail 标志或 exit0 均不能代替完整成功。谱权 inner 记录只是额外来源/诊断，不增加二 jet 数值门；既有 seam 误差如实单列。

## 6. 角求积、模数与表示的接续

若需要同权重的 N256→N512 对照，只改 tail `quadrature` 与新运行 I/O，prefix angular512、M14、W、parts8/steps32/depth12及全部物理键均固定。使用各自真实 warm 或已闭结果的同布局 state copy，仅作初猜；新 N 必须重新 root/flow/DN/outer，不能把 exporter N512 当成真 N512 联解。原同布局 remesh 不需 raw-lift，但复制旧 momentum 不等于新角规则下已满足方程。

这只付角求积轴，不是径向 RK 加密；parts8×steps32仍是每 raw profile256步。是否另需径向一档，按现有 G5 审查及新实际误差判断，不自动追加，也不称已有 M14 数据完成了未做的独立对照。

新真实图必须再生成/认证。已审 flat loader、mirror、common-cut-v2、target supplier、prefix-angular、tail stream/transfer与终门本身可按实际 M/manifest 使用；旧数值界不能转移给新图。endpoint exporter从 CP读取 M并按 raw 标签选恢复层，不硬编码M15。固定 degree192 时 M14 的 height有15项，planar有128项，$C=143$、stride575，1000行原始数据4,600,000B；仍核实际压缩文件<5MB。common-cut按尾的完整 signed basis补足模式，不能把 solver M14误作最终Cartesian cutoff。

需要另建入口的主要是**运行身份工具**：

| 当前入口 | M14所需处理 |
|---|---|
| `prepare-final-m15-coupling-v3.py` | 明确绑定 M15/continuation03/s1/705；不调用、不修改。M14用自己的真实闭来源和新launch。 |
| `audit-matched-cut-closed-v2.py` | 明确绑定121输入、M15 matched stem、trial八源及705/46/30；另建上述M14普通shared运行审计，保留其所有数学门。 |
| `spectral-affine-replay.py` | 永远 frozen_affine_dn/actualFalse；不能翻标志当真runner。新的真入口走原coupled。 |
| 原 M15 final pipeline 文本和新 linear-DN policy | 不能沿用其具体CP/stem/目标/八或九源身份；算法泛用部分可引用，实际新输入单独绑定。 |
| `audit-terminal-error-gate.py` | 正常candidate路径未硬编码M15；M12 reference是同g比较基线。保留真实新manifest和全部完整证书，exact bridge预算只转一次。 |

完成图仍须 whole metric、reach、握持/非全等、全 $t$ 与实际网格证据。若新实际图误差没有到原门，应继续同 $g$ 的误差定位/加密，不能靠给带权 norm重新命名、改 $g$ 或容差来完成 G5。

## 7. 本稿执行边界

本轮只读取冻结代码及已闭M14 metadata，生成本文和来源账本。没有生成未来 config/CP/launch，未导入或实例化 candidate类，未调用任何 solver/root/flow。资源候选审查是另一份只读清单，不作为本数学接口的计算证据。可行的是接线与方程等价性；收敛、谱权实际改善、新闭图认证及未参与者完整重跑均尚未发生。
