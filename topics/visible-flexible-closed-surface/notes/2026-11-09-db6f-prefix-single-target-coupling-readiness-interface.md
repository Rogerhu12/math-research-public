# 独立 single-target 真成功后的原 coupled 接口：条件式静态说明

作者：/root/coupled_prefix，2026-11-09。

**这是一份未执行的条件说明，不是 readiness。** 原 continuation02 的专用门、进度与输出保持原样。本稿编写结束时，root 已报告独立 single-target 运行关闭失败，因此下述正条件未满足；本轮没有生成 ready 文件、coupled config 或启动绑定，也没有实现新的通用准备器。失败本身另按真实闭运行审查，不在这里推测原因或安排重试。

## 1. 两条来源身份必须分开

已审单请求 runner 是 scripts/db6f-prefix-single-audited-target-v2.py，SHA 173d03b8c02107349275ad58509cd24d09963c6e26a09e17458507db1e20c7c5；它独立请求固定 goal、Jacobian 和 source audit。原 scripts/db6f-prefix-prepare-final-m15-coupling-v2.py 则专门绑定 continuation02 的完整 progress/reproduction/目标终点/退出。两者不是同一个运行。

若将来另有真正成功的 single-target 记录，可新增明确的来源核查记录，例如状态 READY_SINGLE_TARGET_DN_FOR_ORIGINAL_PREFIX_UNSOLVED，source_kind 为 standalone-single-audited-target-v2。不得改名旧失败包、填造 target_reached/target_audited，也不得修改或调用旧 preparer 来让不同运行冒充02完成。原02若先完成，直接使用它自己的正式门即可；本说明不要求额外执行一套竞争的 coupled 求解。

## 2. 新身份记录允许成立的完整有限条件

只复用已审 runner 的有限接受逻辑及原 prefix restart 检查，不增添数学门。必须在实际进程闭合后一起核实：

1. root 的真实工具观察记录属于该 single-target 命令、会话和输出 stem，实际工具退出0。它绑定该次原 reproduction、config、summary、实际 response，以及实际 runner 和输入来源的 SHA/bytes。summary 的 intended_runner_exit_code 或文件存在不能替代真实工具退出。
2. summary 实际状态为 TARGET_DN_CONVERGED_AND_AUDITED_PREFIX_UNSOLVED，actual_request_count=1、actual_worker_exit_code=0，所有 client/response-validation/worker-exit 错误为空。其引用的 config/reproduction/response 与真实闭文件严格匹配。原失败 summary 不得重标状态。
3. 原响应属于该单次运行，不是 warm 输入、iteration CP 或另一条 continuation 的响应。request 的物理 height 精确复制原 affine target，jacobian 与 audit 都是实际 JSON True。原成功 schema、finite 非 bool residual 在 [0,2e-9)、705项 Jacobian、17键完整 cutJets、8项完整 source audit、状态维数和 raw 映射，全部按已审 v2 的严格数值／canonical 类型身份门核实。
4. 原响应的八源为 continuation-client 加原 trial-worker/core/split 等冻结集合，来源 SHA 和66项原定义绑定一致。逐模 warm 仍只作为输入 provenance：其77项绑定和独审来源保留，不能把“初猜构造 PASS”当作求解成功。
5. config 与原 from-affine 实际配置除五个 I/O 键外严格 canonical 相同。原 g、M15、spacing3、depth12、parts8、steps32、N256、36轮、tol2e-9、默认floor0.05和默认边界修正均保留。历史 CP 参数只可排除五I/O与历史 maxIterations 作定义比较，实际新运行参数还须匹配本次真正 config。
6. 原 affine prefix、两个系数块、原命令绑定及 restart-check 的全部既有绑定仍匹配。原 restart 物理网格2633节点已付的逐位一致性、原自由 support 参数和真实 cut 重建规则保持，不因为尾成功就改 prefix 数据或目标标签。

不能机械照抄旧02专用门的 history[-1].norm==residual 条件：原单次 shooting 可能在第36个接受步后作最后一次完整 evaluate，最终原 residual 与 history 最后基点 norm 可以不同。已审 v2 正确使用真正最终 residual 和完整 Jacobian；新来源核查保留这个语义，不从基点历史另造一次不存在的评价。

source audit 仍是有限源 jet 数值诊断；它不是 full XYZ 连续 metric、嵌入或闭图证书。上述条件只允许准备原 prefix 联解，状态始终包含 PREFIX_UNSOLVED。

## 3. 实际路径及来源链

本次计划／实际单请求 stem 为：

    P = /workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-harmonic-s1-audited-target-01

应核的闭文件为 P-config.json、P-reproduction.json、P-summary.json 和 P_tail_0001.json.gz，再附 root 的真实观察记录。这里的 P_tail_0001 必须自身真正通过第2节；路径存在不够。本次它已失败，故不能作为下面的已解 initialCheckpoint。

原 prefix 命令来自：

    notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-from-affine-input-bindings.json

其 SHA 为 457d4a5fbbb3730eafb2b4f6f8d4fc5429676d877e7a346d59b49fcf1b930913。原 --restart 始终是 notes/2026-11-09-db6f-prefix-flat-v17v18-m15-affine-cut-predictor-from14q512.json.gz（SHA4a13e132…）。它继续是 UNSOLVED 的辅助 prefix，不能因另一个尾成功改其 actual_nonlinear_tail 标签。

原重启记录 notes/2026-11-09-db6f-prefix-final-m15-restart-check.json 的 SHA 为 c9390004df97d2db00e7ba2ac87eba95a6f256be95ea4f3ed12368ed4e13d2c6；物理网格重建逐位相同，但从 PPoly 取得的 cut H 与保存 affine goal 最大差1.6940658945086007e-21。这个真实差异保留。将来新的尾 client 从成功响应只读取 states/parameters/cutHeight，在新 H 上仍执行原全模线性边界修正和真正 DN；不能覆写 prefix cut 来伪造逐位一致。

## 4. 真条件满足时，原 coupled 输入只改什么

为避免与原02 after-amplitude 路径混淆，可选一个新的独立输出 stem：

    O = /workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-after-single-target

它只是建议路径，本稿没有创建这些文件。新的 O-tail-config.json 必须从原 from-affine tail-config 完整复制，且仅改变：

| 键 | 新值 |
|---|---|
| initialCheckpoint | 真正通过第2节的单请求 response 文件 |
| traceFile | O-tail-trace.jsonl |
| iterationCheckpointFile | O-tail-iteration.json.gz |
| trialDiagnosticFile | O-tail-trials.jsonl |
| trialStatePrefix | O-tail-stage-input |

不要从 zero pilot 配置复制，correctInitialBoundary 保持原键缺省真。配置中的历史初猜路径只影响初始化，原自由 cut/support 外层仍可改变边值；最终成功的固定 H 尾并不自动给出联解。

argv 从原绑定的 command 列表完整复制，**只有 --tail-config 与 --out-prefix 后的两个字符串变化**。原 flat-trial-coupled wrapper、source-root、profile、chart、linear-port、--restart 全保留。其余原参数如下：

| 参数 | 原值 |
|---|---|
| amplitude / warp-reference / modes | .1 / .1 / 15 |
| prefix angular / audit-angular | 512 / 1024 |
| tail quadrature | 256，由原 tail-config 决定 |
| nodes / max-nodes | 1601 / 4500；preserve-restart 实际使用保存的2633初始节点 |
| tol / bc-tol / physical-bc-tol | 2e-9 / 1e-8 / 2e-11 |
| node-heap | 1536 |
| 原旗标 | fixed、warmup-scales 空列表、lagged-tail、preserve-restart-mesh |

--warmup-scales 后立即是 --lagged-tail，因此不重新请求一串小 H。tail true-DN warm 路径保持原算法。support 振幅依旧是原 BVP 自由参数，不将 .1 的固定归一化误当锁定实际 support。

新 O-input-bindings.json 应同时绑定新 single-target readiness/真实观察、上述真实响应、原 prefix 所有绑定、restart-check、两份互补独审以及新 O config。使用原 scripts/db6f-prefix-run-bound-command.py 启动时必须由 root 从仓库根目录执行；该 launcher 不主动 chdir 到 metadata 的 cwd。

    cd /workspace/scratch/db6f0b0e7462/math-research
    python topics/visible-flexible-closed-surface/scripts/db6f-prefix-run-bound-command.py \
      topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-after-single-target-input-bindings.json

此命令现在不能运行，因为真实正条件和上述文件尚未成立／创建。

## 5. 后续真正联解及 source 身份边界

原 coupled wrapper 会把 shared-client 导入重定向到原 trial-client。因而它随后真实响应的八源集合，其 client 项是 db6f-prefix-tail-trial-client.py；先前单请求的 client 项则是 db6f-prefix-tail-continuation-client.py。两者已审数学路径相同，但新响应必须按实际装载源记录核实，不能直接复制旧八源名单。新 client 缓存为空，也不把成功 single-target 的 Jacobian 直接冒充新 H 的真 DN。

原 outer 仍须：原 BVP success 与原 tol、每次候选高度的真 DN 校正、最后原 scaled/physical BC、真正 seam_audit 的 Jacobian/source audit以及真实关闭记录。原 mean/nonmean 两 jet mismatch、sourceMetric、actualXYZMetric 和 fullTensor 保持不同含义。之后同 g 的最终 N512 真校正、实际 XYZ/公共 C² 表示与连续证书仍按原计划进行，本说明不提前支付它们。

本稿只读原源与闭输入的身份；没有新 solver、后端、候选或伪造 positive fixture。由于本次独立 s=1 请求已经失败，本轮止于保存此条件接口；原 continuation02 的自然推进与正式门继续独立有效。
