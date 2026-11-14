# 真正 M15/N256 联解后的 N512 原方程校正入口

2026-11-09，`/root/coupled_prefix`。**只读核查与条件式命令模板；未生成未来配置、未启动 solver，也未把当前 continuation 当成完整 M15 联解。** 这是原 final-m15-coupling-plan §3 末段、tail-final-m15-minimal-pipeline §1–2 所要求的 N512 真校正的具体补充，不重建通用准备器。

## 1. 已闭 M14 的参照与本次唯一数值变化

参照是 `2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14` 的完整 prefix CP、reproduction、summary 与 `tail_seam.tail_record` 指向的 `_tail_0002.json.gz`。本次只读检查得到：

- N256/N512 的 frozen_profile、chart、physical_tail_parameters 逐值同；prefix angular 均为512。
- 两份 tail_config 只在 `quadrature` 与三个 I/O 路径不同，全部其它键逐值同。
- N512 prefix 确实 `solver_success=True`，原 collocation residual 为 $1.9978998186646144\times10^{-9}$；最后原 BC residual 为 $2.0843158108768282\times10^{-14}$。
- 最后 `_tail_0002` 请求 `jacobian=True,audit=True`，真实 converged，shooting residual $5.397833270174952\times10^{-10}$。其 config、jets、residual 与最终 prefix 的 tail_seam 逐值吻合。
- 当时的 freeze-refine driver SHA256 与当前文件同为 `ad2bc1113795446f6be86d4f6efb8482967a05beaf986a233599733e1395cc7c`；最后响应绑定的八个普通 shared 源码也全部与当前字节相同。

这个参照只证明原接口确实产生过 N512 真校正；不保证 M15 收敛或 metric 改善。M14 的 prefix metric 非单调结论仍保留。

本次未来 M15 校正保持 $M=15$、spacing3、physical depth12、p8、steps32、原 $g$、原容差和 guard。数值方程只将 tail 的角规则 $N=256$ 改为512：

| 项目 | 本次设置与含义 |
|---|---|
| tail `quadrature` | **256→512**，改变有限角求积的原 moment/root/ODE/DN，必须重新真解 |
| prefix `--angular` | 保持512；与 tail N 是两个独立参数 |
| prefix `--audit-angular` | 保持1024；只用于保存的 prefix 诊断 |
| seam `angular_samples` | 原代码 `max(512,64*M)`，M15 为960，不是 tail N |
| `calibrationSteps` | 保持512；背景构造输入，不能混作本次尾角加密 |
| `quadratureTolerance` / `warpSteps` | 保持原 $2\times10^{-10}$ / 16，仍属同背景的生成设置 |
| `auditSteps` / `steps` / `shootingParts` | 保持32 / 32 / 8；没有径向加密 |
| prefix `tol / bc_tol / physical_bc_tol` | 保持 $2\times10^{-9}/10^{-8}/2\times10^{-11}$ |
| tail `solveTolerance / maxIterations / projectionFloor` | 保持 $2\times10^{-9}$ / 36 / .05；floor 省略时仍由绑定源码默认 .05 |

`closing_recalibrated_tail.mjs` 的背景 source 创建使用固定内部角数16及原 calibration 输入，不消费外层 `quadrature` 来改变几何；外层 N 被 shared-core/shared-split 用于本次 momentum engine。保持全部物理键和冻结 profile，避免把两类“quadrature”混同。

## 2. 未来输入及闭合门

若原 final v2 计划成功，预期 baseline 为
`2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-after-amplitude.json.gz`。
这是**未来路径模板**；本稿没有声称它已经存在或成功。实际名称变化时，应显式替换模板并绑定真实文件。

必须使用这份真正完整的 prefix CP 及它自己指向的最后 audited tail，不能用 affine predictor、continuation 的单独 s=1 response、早期 `_tail_0001` 或 iteration CP。至少核：

1. 工具自然退出证据、summary、CP 都已关闭；`solver_success is True`、`config.actual_nonlinear_tail is True`、`fixed_metric is True`、无 error，原 collocation residual 达标。`actual_outer_checks` 最后一项是成功原 BC 检查，缩放 residual $\le10^{-8}$，对应物理边界门 $2\times10^{-11}$。
2. `tail_seam` 存在且它的 `tail_record` 能在 CP 同目录解析到真实闭响应；prefix 与响应的 tail_config 相同，最后请求为 jacobian/audit 真，真实 residual $<2\times10^{-9}$，`failed` 不存在。
3. prefix 的全部 `pp_coefficient_chunks` 存在、字节数/hash 与元数据同，状态分片连续覆盖 $3M+1=46$ 个槽；mesh 严增且与分片形状一致。原 load_checkpoint 读取系数但**不会主动核其声明的 SHA**，因此这些绑定须另核，不能只靠 loader 成功。
4. baseline profile/chart/port/warp gauge 与原固定问题一致，M15 的全部自由参数保留；新 config 不继承零态 pilot 的 `correctInitialBoundary=false`。

原 coupled main 会先保存一次带 `solver_success` 的 CP，之后才执行 prefix audit 与 seam_audit 再保存。原 freeze-refine 只断言前两个成功标志，且 Python main 捕获异常后仍可能 exit0。因此 CP 文件存在、driver assert 通过或工具 exit0 都不能替代上述闭合门。

输入依赖为 baseline metadata、全部 PP gzip 分片、baseline 最后 tail response、原 chart、原 linear port、冻结 source-root snapshot，以及实际被调用的 flat/prefix/shared 源码。无需复制旧的大数据；绑定其现有文件。未来 config/profile/argv 的 SHA 要在实际生成后记录，本稿不预造它们。

## 3. 原 warm 协议：同阶直接使用真实末响应

新 `initialCheckpoint` 取
`baseline.parent / baseline['tail_seam']['tail_record']` 的绝对路径。原 shared-worker 从 `record.response.checkpoint` 读取 states、parameters 和 cutHeight；这些值仅作初猜，不复制旧 converged/audit 结论。几何对照键有意不含 quadrature，因此允许同 $g$ 改 N。

同 $M=15$、physicalDepth12、parts8 时，原 remeshCheckpoint 的所有 `rawLeft*8` 都为整数，走已存节点复制分支；不补深度，不需 `--raw-lift-warm`。它仍会构造潜在插值使用的旧 N engine，但本布局不调用它的 RK。M14 参照确实执行过 raw-lift；本次省略的是一个可选初猜转换，不是删掉新 N 的原方程验收。

复制旧 momentum 数值不意味着其在新有限 N 下具有完全相同 raw slope，更不意味着已解 N512 方程。fresh shared client 的 cache_key/cache_value 均为空；实际 DN 与替换 engine 按当前 N512 建造，不能返回旧 N256 响应。

原 ratio 初猜和缺省为真的边界修正照常保留：
$$
\Delta Q_j=H_j/r_{\rm cut}^4-Q_{0,j}^{\rm initial}.
$$
对全部模加入原有限线性 warm 解后，仍调用原 nonlinear solve。prefix restart 由原保存 PPoly、物理 mesh 和 chart 恢复，自由 support 振幅通过原参数 $p_0$ 继续求解。PPoly 重建产生的 cut 高度舍入差不能通过修改已存解消除，只走原边界 warm 校正和新真实 DN。

`tail_theory` 已只读复核上述窄接口；没有额外 root/flow 调用。

## 4. 最小未来配置与原 driver 命令

令新输出 stem 为
`2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q512-outer-from15`，使用尚未被用过的路径。真正输入闭合后，root 才复制 baseline 的 frozen_profile 为该 stem 的 `-frozen-profile.json`，复制其完整 tail_config 为 `-tail-config.json`，仅改：

| 键 | 新值 |
|---|---|
| `quadrature` | 512 |
| `initialCheckpoint` | baseline 最后 `tail_seam.tail_record` 的绝对路径 |
| `traceFile` | 新 stem 的 `-tail-trace.jsonl` 绝对路径 |
| `iterationCheckpointFile` | 新 stem 的 `-tail-iteration.json.gz` 绝对路径 |
| `trialDiagnosticFile`，若原来存在 | 新 stem 的 `-tail-trials.jsonl` 绝对路径 |
| `trialStatePrefix`，若原来存在 | 新 stem 的 `-tail-stage-input` 绝对路径 |

其余键逐值保持，包括 sharedEngines=true、原 harmonicAmplitudePredictor、全部 calibration/physical 参数与容差。两个 trial 路径在普通 shared 源图中没有读取点；仍指向新 stem，以避免旧路径误导后续接手者。此处没有提前生成配置。

原 freeze-refine CLI 没有覆盖这两个 trial 路径的选项，写完 config 后立即启动；不能声称它单条 CLI 会完成上表。为同时保留原源码并显式规范这些 I/O 键，直接使用它在已闭 M14 reproduction 中实际调用的原子命令 `db6f-prefix-flat-coupled.py`。这不是 trial wrapper：实际八源应绑定 **shared** client/worker/core/split、950f subdivision/remesh、closing weighted/recalibrated，不能套用 continuation 的 trial 八源集合。

以下为**尚未运行**的完整命令模板，cwd 为本题目录：

```bash
python scripts/db6f-prefix-flat-coupled.py \
  --source-root repro/source-root \
  --profile notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q512-outer-from15-frozen-profile.json \
  --chart notes/2026-11-09-950f-prefix-adaptive-chart.json \
  --linear-port notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json \
  --tail-config notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q512-outer-from15-tail-config.json \
  --out-prefix notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q512-outer-from15 \
  --restart notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-after-amplitude.json.gz \
  --amplitude .1 --warp-reference .1 --modes 15 \
  --angular 512 --audit-angular 1024 --nodes 1601 --max-nodes 4500 \
  --tol 2e-9 --bc-tol 1e-8 --physical-bc-tol 2e-11 --node-heap 1536 \
  --fixed --warmup-scales --lagged-tail --preserve-restart-mesh \
  > notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q512-outer-from15-run.log 2>&1
```

`--warmup-scales` 的列表为空；不重回小 H。`--nodes1601` 不强制覆盖保存的自适应 mesh；真实初始化节点数以原 preserve-restart diagnostics 为准。命令保留原8轮 outer：inner 只暂用仿射 DN，候选必须重新取 N512 真 DN/J，按原 BC 判定。root 仍负责真实工具会话和新输入/源码/argv/退出绑定；直调 prefix driver 不会自动写 freeze-refine 的 reproduction 文件，不能假称已有。

## 5. N512 真正最后 tail_seam 的 schema 检查

完成后沿 **新 prefix CP 的 tail_seam.tail_record** 读取实际响应，不能猜测 call 序号。原 seam_audit 明确调用 `jacobian=True,audit=True`，audit 会绕过 client cache；所以应有真实新响应文件。核对：

- record 恰有 request/response/config/source_sha256，request height 长度15、有限非bool，jacobian/audit 都严格为 true；config.quadrature=512。
- response.converged 严格 true、residual 有限非bool且 $<2\times10^{-9}$；heightJetJacobian 长度 $(3M+2)M=705$，所有项有限非bool。
- jets 恰为原14个有限非bool标量及 height/slope/second 三个长度15的有限非bool列表。可复用已审 final-preparer-v2 的 `valid_cut_jets` 定义作为 schema 参考，**不能执行其 N256/continuation 专用整套 gate 来验这份新图**。
- audit 恰有 fullD、normalizedFullDefect、minLeading、minD、formalCurvature、maxPhysicalPV、actualMetric、holonomy 八个有限非bool标量；不能接受 null、字符串或 bool 替代数值。
- checkpoint.parameters 的 modes15、spacing3、quadrature512、physicalDepth12、shootingParts8、steps32、projectionFloor.05 正确。注意其 `depth` 是 stage 数864，不能与 config.depth12 混同；865个 states 各30项，rawNode 长13，rawStates 与其索引逐项对应，全部有限。
- request.height 与 checkpoint.cutHeight 逐值同；响应 jets/residual 与 prefix tail_seam 逐值同；new config 与响应 config 逐值同；八个真正 shared 源码 hash 完全匹配。必要时从保存 PPoly 实际求 cut 的 $H=\sigma q_gY_Z$ 对照请求，不假定它与旧 N256 cut 严格不变。
- 单列最终 mean/nonmean 一、二 jet mismatch、prefix/sourceMetric 与 actualXYZMetric。seam 的 cut_metric_c1_fft_l1、Darboux/fullD 都不是 metric；源 audit actualMetric 也不是保存全 XYZ 图的连续证书。

即便上述数值校正闭合，后续新 XYZ/公共 C²接缝及连续全图验证仍按已审最小流程重做。若 M15/N512 的实际源误差没有达标，如实保存；本计划不更改 G5 的容差，也不保证角加密必然解决高模问题。
