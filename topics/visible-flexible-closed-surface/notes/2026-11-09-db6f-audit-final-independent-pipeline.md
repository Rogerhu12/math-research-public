# 最终 M15 的独立端到端重跑：最小顺序、命令与产物

2026-11-09，`/root/independent_geometry`。**状态：仅静态源码核查及条件式执行协议；最终候选尚未交付，本轮没有执行下列命令。** 未启动求解、root、flow、导出、区间后端或网格验证，没有创建未来 packet，没有修改已闭件。

## 1. 什么才算本题的独立全流程

README 要求由未参与计算者独立重跑生成与核对流程。按当前分工，审计者不参与最终 M15 的数值生产、初猜选择、调参或优化；其此前实现/审查通用验证器、复算 M8/M12 中间证据的经历如实保留。通用验证器自身另有独立代码审稿。不能把原生产者重跑一次或几位作者分别复算最后的 JSON，合称为这项最终独立重跑。

**最小完整链仍包含一次真正的最终前缀/尾联合求解、重新生成两侧有限表示、重新组合公共接缝、实际全域连续认证及同图网格重建。** `whole-metric-reach-v2` 和 `terminal-error-gate` 只是最后的组合门，不能替代这些运算。

独立重跑不要求重新探索所有失败初猜，也不要求再次搜索物理参数。使用作者原最终成功命令的**真实前置 seed**，按完全冻结的算法、参数、分辨率和停止门重新执行即可。该 seed 可以是已有已审的 warm/较粗解；不能为省事把所审的最终 CP 临时换成 seed，再将零更新或只读验算称为从原输入重跑。原失败记录和 M14 非单调结果仍保留在完整研究历史中。

已审固定背景、精确参数及原公共结构定理可以作为输入复用；无需重新积分同一份已独立重放的 160-cell 背景。本次任务不是重证明所有前置定理。

## 2. 冻结包必须先给出的真实输入

以下内容由最终候选生产者在实际成功后冻结；本文不预造文件或猜 tail call 编号。

| 类别 | 必须存在的实际对象 |
|---|---|
| 最终成功命令 | 原完整 argv、cwd、环境/运行时版本、源码清单、实际自然退出记录、原 prefix restart 与 tail warm seed，以及生成 config 的明确差分。 |
| 最终真联解 | 已关闭 prefix CP、全部 PP gzip 系数块、summary、最后真实 `tail_seam.tail_record`、其 request/response/config/source 哈希和全部实际 outer 检查。不是 affine predictor、单独 s=1 尾或 iteration CP。 |
| 固定物理问题 | `frozen_profile`、chart、linear port、`warp_reference_q`、cut/cuff、校准表、精确 alpha/桥定义及相位区间。实际 support 振幅是解的未知量，不把它当作必须锁死的物理参数。 |
| 每次离散设置 | M、prefix angular/audit-angular、tail N、physical depth、parts、native RK steps、容差与 guard；另列 XYZ 导出的 depth、网格、flow-steps、角节点、保留阶、差分步长。它们不能互换含义。 |
| 最终有限图 | prefix shared-jet/Hermite、tail manifest 与所有分片/实际 collar、共同 cut metadata、最终采用的全部证明输入与完整证书。 |
| G5 主线 | 同 g 的原网格/频率轨迹、实际误差下降证据、最终达到原求解容差的连续界，以及仍保留的失败/非单调记录。需补的原生径向对照若有，必须作为明确任务冻结。 |
| G7 | 最终图自己的采样计划、数值高度来源、三件网格及其验证记录；不能把旧 M8 文件当作最终 M15 交付。 |

来源核查不能只记录顶层 driver 的 SHA。应包含实际导入的本题源、真实 shared 或 trial 八源集合、`repro/source-snapshot-manifest.json` 的 43 个递归源副本、profile/chart/port、seed、PP 分片、背景六定义文件和所有下游 producer。Node 的 `VISIBLE_FLEX_SOURCE_ROOT`/`CLOSING_TAIL_CACHE` 指向同一冻结快照，不依赖旧临时工作区。

本轮静态核查的 40 个源码与 10 个文档/快照索引绑定保存在 `audit-final-independent-pipeline-sources.json`，SHA256 `31a745c87f654e90c0795e1b6fab6fc13f31d592d85dcaacc6e1f300fec3a936`。它是当前接口版本索引，**不是未来最终运行的来源清单**。最终若实现有变化，必须另冻、另审真实新版本，不能沿用旧 SHA。

## 3. 隔离、来源比较与退出证据

使用未用过的输出目录和 fresh Python/Node 进程。共享的已冻结输入可以只读复用；不需要复制大数据，也不需要改动主工作树。所有命令从仓库根 cwd 执行，输入与输出均给绝对路径，以满足 angular wrapper 的来源解析要求。

独立运行的 binding 与作者 binding 保留明确差分：只改本次输出/日志路径，必要时改为同哈希的来源路径；原 seed、原数值选项和原物理配置不变。`--out-prefix`、trace/iteration/trial 路径等必须指向新命名空间，避免覆盖原输出。未知配置差异仍 fail-closed。

`db6f-prefix-run-bound-command.py` 可以核 `bound_files` 并实际执行绑定 argv，保存另一个 reproduction；但它不自动证明绑定清单完整，也不自动验证数学成功。prefix main 捕获异常后可能正常退出；还可能在 seam audit 之前已经写过带 `solver_success` 的 CP。尾 exporter 也先写 manifest、随后写 collar。因此每一步必须同时留下：

- 真正观察到的自然退出码；
- 开始/结束时输入及源码 SHA、完整 argv/cwd；
- 最终成功字段、无 error、完整末端产物和全部输出 SHA；
- 在运行未结束前不能把已有文件或 `finished` 片段当作完整证据。

不以 `/proc` 中找不到进程替代退出证据。不因 traceback 被 main 捕获而忽略 summary 的失败状态。新运行的审计记录必须由观察者写出，不能复制作者的结束记录。

## 4. 最小执行依赖次序

| 顺序 | 真正执行的工作 | 独立留下的最少产物 |
|---:|---|---|
| 0 | 源/物理定义/原成功命令与前置 seed 的静态预检 | replay binding、精确允许差分、环境及输入 hash 清单。 |
| 1 | 原最终真实 prefix + nonlinear DN 联解 | 新 CP/PP 块、summary、真实 outer checks、最后新 audit response、运行记录。 |
| 2 | 新 tail XYZ 增量导出与 radial/collar 检查 | 新 manifest、全部分片、同图 collar、精确锚不变量与 first-jet 证书。 |
| 3 | 新 prefix shared-jet/mirror 表示与 analytic target | 基础图及数据、新 target 包；精确入口镜像调整记录。 |
| 4 | 基础图 metric、exact bridge、common-cut make | 基础 metric、新桥证书、真实 cut 两 jet 修正及闭图 metadata。 |
| 5 | 共同图完整 geometry、metric、moment；必要的完整 angular 认证 | 本图全部连续位置/曲率/见证/矩与目标 metric 证书及逐叶文件。 |
| 6 | 同 g 的两份背景包分别转到新尾网格 | 新紧曲率包与新低 metric 包，精确分区及六定义身份。 |
| 7 | 新尾完整实际曲率/metric 与完整 metric-only 后端 | 全部有限跨加 collar 的真实运行、完整 rows、覆盖检查。 |
| 8 | 新 closed budget、whole、原 $2\cdot10^{-9}$ 终门 | 同一候选图的完整 Fraction 组合和正常正向门报告。 |
| 9 | G5 证据核对及必要的已冻结 refinement 分支 | 同物理问题、实际下降及原容差的统一账本。 |
| 10 | 同一闭图 plan/高度/build/三件 PL 验证 | 新网格、固定帽 mask、逐 PLY 和跨时刻复核。 |
| 11 | 输出逐项比对与最终独立报告 | 原/复跑计算对象的身份、误差/差异、来源闭包、实际完成记录。 |

依赖允许在有内存预算时并行：tail 导出与 prefix 基础表示互不依赖；尾区间证书与前缀 geometry/moment 可分别执行。但 common-cut 必须使用已完成的实际 tail，最终组合必须等所有输入关闭。最小性指不重跑无关探索，不指跳过真实运算。

## 5. 求解层：确实需要重求一次原最终联解

优先使用作者最终真实 argv 的绑定版，而不是重新发明一个“接近”的命令：

```sh
"$VF_PY" "$VF_S/db6f-prefix-run-bound-command.py" "$VF_REPLAY_SOLVE_BINDING"
```

`VF_REPLAY_SOLVE_BINDING` 是未来从原最终成功输入建立的新绑定；当前不存在。binding 中的 `command` 必须实际调用原 coupled driver。当前已审 N512 方案调用 `db6f-prefix-flat-coupled.py`，它加载原 `db6f-prefix-coupled.py` 并安装同一 flat profile；不能换成 affine-only driver。

本次静态核过的原子命令接口为：

```sh
"$VF_PY" "$VF_S/db6f-prefix-flat-coupled.py" \
  --source-root "$VF_SRC" --profile "$VF_PROFILE" --chart "$VF_CHART" \
  --linear-port "$VF_PORT" --tail-config "$VF_REPLAY_TAIL_CONFIG" \
  --out-prefix "$VF_RUN/solve" --restart "$VF_SEED_PREFIX" \
  --amplitude "$VF_GAUGE" --warp-reference "$VF_WARP" --modes "$VF_M" \
  --angular "$VF_PREFIX_N" --audit-angular "$VF_PREFIX_AUDIT_N" \
  --nodes "$VF_INITIAL_NODES" --max-nodes "$VF_MAX_NODES" \
  --tol 2e-9 --bc-tol 1e-8 --physical-bc-tol 2e-11 --node-heap "$VF_NODE_HEAP" \
  --fixed --warmup-scales --lagged-tail --preserve-restart-mesh
```

这是接口模板，不是本轮生成的 ready launch。所有 `VF_*` 都由未来冻结输入给定；`VF_S` 是 scripts 绝对路径，`VF_SRC` 是快照 source-root，`VF_RUN` 是全新输出目录。原最终命令若使用不同的已审选项，应忠实重放它；不得由审计者现在选值。当前计划的 M15/N512/depth12/p8/steps32 与原停止门见 `prefix-final-m15-n512-followup.md`。native steps 将来若已合法加密，以真实冻结版本为准。

运行后的必要核查：

1. `solver_success is True`、`fixed_metric is True`、`actual_nonlinear_tail is True`，无 error，原 RMS collocation 门和最后真 outer BC 门达标。
2. 最后 tail 必须沿新 prefix 的 `tail_seam.tail_record` 解析，不能猜 `_tail_0001`。其 `request.jacobian` 与 `request.audit` 都为真，真实 shooting converged 且残差达原门。
3. 新 fresh shared client 的缓存初始为空；源码明确 audit 请求不走缓存。实际最后 audit 文件和请求需存在，不能只复制旧 response 字段。
4. M15 的 705 项 DN Jacobian、cut jets 的原 14 个标量及三个长度 15 向量、audit 八个数必须有限且不是 bool/null。响应、请求、CP.cutHeight 和 prefix seam 值一致。N、native depth/parts/steps 与实际最终配置一致。
5. 全部 PP 分片 SHA/大小/槽覆盖、真实递增 mesh 和 basis 检查另付。原 `load_checkpoint` 读取 PP 数据并不会自动核所有声明 SHA。

独立性不要求重走每一段 amplitude continuation。若最终成功命令的真实 seed 是已审 N256 联解，使用它作为明确输入后重求 N512 已构成新的真实计算。若最终作者选择另一成功路径，以其实际完整复现包为准。只重解最后一个固定 H 的尾不能代替自由 cut 的联合求解。

## 6. 实际有限表示与前缀连续证书

以下各变量同样是未来冻结参数或新运行产物。`VF_PCP` 指本次真正闭合的 prefix CP；`VF_TCP` 从其最后 seam 解析。`VF_RUN/tail-manifest.json` 等是命令约定的**新输出名**，不是声称文件现已存在。

### 6.1 尾导出及自身接口

当前已审端点扩展 exporter 为 `db6f-prefix-endpoint-critical-increment-export.mjs`，SHA `993dc6a180b917132d8284fae6c6366b45dddd883f9c09ab50b2b1dcf87f593b`。它是完整导出入口；下面不得加 `--plan-only`：

```sh
"$VF_NODE" "$VF_S/db6f-prefix-endpoint-critical-increment-export.mjs" \
  "$VF_TCP" "$VF_RUN/tail" --source-root "$VF_SRC" \
  --depth "$VF_EXPORT_DEPTH" --steps "$VF_EXPORT_STEPS" \
  --grid critical --critical-cells "$VF_CRITICAL_CELLS" \
  --critical-ratio "$VF_CRITICAL_RATIO" --critical-base-steps "$VF_CRITICAL_BASE" \
  --endpoint-ratio "$VF_ENDPOINT_RATIO" --flow-steps "$VF_FLOW_STEPS" \
  --angular-nodes "$VF_EXPORT_N" --degree "$VF_EXPORT_DEGREE" \
  --difference-step "$VF_FD_STEP" --audit-angular-nodes "$VF_XYZ_AUDIT_N" \
  --audit-fractions "$VF_XYZ_AUDIT_FRACTIONS"

"$VF_PY" "$VF_S/db6f-tail-radial-invariant.py" \
  "$VF_RUN/tail-manifest.json" "$VF_RUN/tail-radial-invariant.json"
"$VF_PY" "$VF_S/db6f-tail-collar-exact-check.py" \
  "$VF_RUN/tail-collar.json" "$VF_RUN/tail-collar-exact.json"
"$VF_PY" "$VF_S/db6f-tail-first-bounds-stream.py" \
  "$VF_RUN/tail-manifest.json" "$VF_RUN/tail-first.json" --batch 128
```

确认自然 exit 0、finished、实际所有分片 hash/有限值/共享行、正增量和精确 $\beta\sum\ell_i=r_{out}-r_{in}$。保存本次自己的 `-collar.json`。collar exact 报告是有限端迹层的条件账本；真正闭图的 collar 已由随后 first/full 后端一起覆盖，不能拿旧 N8/10 source 包替换。

M、N、native RK、export steps 和 flow-steps 分开记录。提高 exporter N 会改变其 moment/RK engine，不等于纯空间采样加密；提高 export steps 不等于从头重求更细 native RK 的原 DN。不得用两种操作的名字互相替代。

### 6.2 基础 prefix、目标包、桥与公共 cut

```sh
"$VF_PY" "$VF_S/db6f-root-mirror-hermite.py" \
  --source-root "$VF_SRC" --checkpoint "$VF_PCP" --linear-port "$VF_PORT" \
  --out-prefix "$VF_RUN/prefix-base" --modes "$VF_CARTESIAN_M" \
  --angular "$VF_CARTESIAN_N" --quadrature "$VF_MEAN_QUADRATURE" \
  --subdivide "$VF_PREFIX_SUBDIVIDE" --ell 0

"$VF_PY" "$VF_S/db6f-audit-metric-supplier.py" \
  --geometry "$VF_RUN/prefix-base.json" --source-root "$VF_SRC" \
  --out-prefix "$VF_RUN/prefix-target"
"$VF_PY" "$VF_S/db6f-audit-metric-polynomial.py" \
  --geometry "$VF_RUN/prefix-base.json" --target "$VF_RUN/prefix-target.json" \
  --out "$VF_RUN/prefix-base-metric.json"
"$VF_PY" "$VF_S/db6f-root-exact-bridge.py" \
  --geometry "$VF_RUN/prefix-base.json" --target "$VF_RUN/prefix-target.json" \
  --tail-manifest "$VF_RUN/tail-manifest.json" \
  --metric-certificate "$VF_RUN/prefix-base-metric.json" --out "$VF_RUN/bridge.json"

"$VF_PY" "$VF_S/db6f-root-common-cut-v2.py" make \
  --geometry "$VF_RUN/prefix-base.json" --tail "$VF_RUN/tail-manifest.json" \
  --bridge "$VF_RUN/bridge.json" --width "$VF_COMMON_CUT_WIDTH" \
  --out "$VF_RUN/closed-map.json"
```

保留精确 mean increments、镜像入口置零条件及调整量、各数据 hash、cut 修正的完整 Cartesian 两 jet。solver M15 不等于 Cartesian cutoff；common-cut 会按实际尾模式扩充列数。基础图 metric 是当前 bridge CLI 的真实依赖，不能用共同图的报告顶替以节省一次计算。桥的唯一根/目标转移须绑定本次对象，不能仅复制旧 eta。

### 6.3 同一共同图的完整前缀认证

```sh
"$VF_PY" "$VF_S/db6f-root-common-cut-v2.py" geometry \
  --geometry "$VF_RUN/closed-map.json" --angular "$VF_GEOMETRY_ANGULAR" \
  --radial "$VF_GEOMETRY_RADIAL" --out "$VF_RUN/prefix-geometry.json"
"$VF_PY" "$VF_S/db6f-root-common-cut-v2.py" metric \
  --geometry "$VF_RUN/closed-map.json" --target "$VF_RUN/prefix-target.json" \
  --out "$VF_RUN/prefix-baseline-metric.json"
"$VF_PY" "$VF_S/db6f-root-common-cut-v2.py" moment \
  --geometry "$VF_RUN/closed-map.json" --angular "$VF_MOMENT_ANGULAR" \
  --radial "$VF_MOMENT_RADIAL" --out "$VF_RUN/prefix-moment.json"
```

最终 baseline 若已以原目标严格达到 B，可以直接使用这份完整证书，无须额外角细分。若作者的最终流程确实依赖第一档 angular，则独立重跑其完整模式：

```sh
"$VF_PY" "$VF_S/db6f-audit-prefix-angular-metric.py" \
  --geometry "$VF_RUN/closed-map.json" --target "$VF_RUN/prefix-target.json" \
  --baseline "$VF_RUN/prefix-baseline-metric.json" --bridge "$VF_RUN/bridge.json" \
  --budget 2e-9 --initial-arcs "$VF_ANGULAR_ARCS" --max-depth "$VF_ANGULAR_DEPTH" \
  --out "$VF_RUN/prefix-angular-metric.json"
```

完整运行省略 `--intervals`，核所有叶的精确覆盖、正分母、完整标志及 `entire_prefix_target_met`。全局继承分支可以复用**本次已真正重新计算**的 baseline；不能只输入作者 baseline，让继承输出冒充独立区间重跑。

`VF_PREFIX_METRIC` 随后选本次 baseline 或本次完整 angular 报告。后者的 `metric_operator_upper` 仍是源目标界，closed-budget 从此字段转移一次；不把已转移字段再转。common-cut `metric` 分支不读取其共享 parser 的 `--angular/--radial`，不能靠调这两个旗标细化 metric。也不能用未安装 common-cut adapter 的原 polynomial CLI 认证共同图。详见已冻 `prefix-final-m15-metric-risk-order.md`。

## 7. 固定背景复用与新尾完整区间重跑

当前可复用原 M8 背景紧包和低 metric 包及其已审独立重放记录，背景六定义 hash 保持。它们是固定函数 $w,w_r$ 的证明输入，不是旧 M8/M12 的实际曲率/metric。任何为了最终预算新改过的 supplier/局部修包，需先有相应独立解析审查及实际 producer 重放，再冻结为输入；不能只验证输出 hash 就把未审新包含性补上。

当前显式 transfer v3 `bdf6307f…` 与 closed-budget consumer `5ef8d229…` 已完成互审及参数预检。最终必须调用真实 `--new-manifest` 分支，不是 quarter 的 preflight：

```sh
"$VF_PY" "$VF_S/db6f-tail-transfer-background-v3.py" \
  --old-manifest "$VF_BACKGROUND_SOURCE_MANIFEST" --packet "$VF_BACKGROUND_K_PACKET" \
  --new-manifest "$VF_RUN/tail-manifest.json" --out-prefix "$VF_RUN/background-k"
"$VF_PY" "$VF_S/db6f-tail-transfer-background-v3.py" \
  --old-manifest "$VF_BACKGROUND_SOURCE_MANIFEST" --packet "$VF_BACKGROUND_E_PACKET" \
  --new-manifest "$VF_RUN/tail-manifest.json" --out-prefix "$VF_RUN/background-e"

"$VF_PY" "$VF_S/db6f-audit-tail-stream.py" \
  --manifest "$VF_RUN/tail-manifest.json" --packet "$VF_RUN/background-k.json" \
  --angular "$VF_TAIL_ANGULAR" --radial "$VF_TAIL_RADIAL" \
  --background-curvature 6 --direct-threshold "$VF_DIRECT_THRESHOLD" \
  --block-size 128 --out "$VF_RUN/tail-full.json"
"$VF_PY" "$VF_S/db6f-audit-tail-metric-only.py" \
  --manifest "$VF_RUN/tail-manifest.json" --packet "$VF_RUN/background-e.json" \
  --radial "$VF_TAIL_METRIC_RADIAL" --block-size 128 \
  --out "$VF_RUN/tail-metric.json"
"$VF_PY" "$VF_S/db6f-audit-complete-metric-report.py" \
  --report "$VF_RUN/tail-metric.json" --curvature-report "$VF_RUN/tail-full.json" \
  --out "$VF_RUN/tail-completeness.json"
```

不得设置 `--limit` 或只选局部 span。核范围为 `[-1,N]`、所有 $N$ 个有限跨及 collar 完整、packet 精确覆盖、全 rows 最大值和哈希。metric-only 不含曲率；本图自己的完整实际曲率仍来自前一条 full 命令。complete-report 只是逐行/分区/身份检查，不能替代实际 full 和 metric-only 运行。

如果最终作者只使用一份 full 包且它已经给出完整 B 门，则不必机械再跑第二份 metric-only；必须忠实重跑最终证明真正依赖的最小集合。当前已审低 metric 合成路径通常需要上述两份。

## 8. 新图组合、原容差与 G5

```sh
"$VF_PY" "$VF_S/db6f-audit-closed-budget-transfer-v3.py" \
  --geometry "$VF_RUN/closed-map.json" --geometry-certificate "$VF_RUN/prefix-geometry.json" \
  --metric-certificate "$VF_PREFIX_METRIC" --moment-certificate "$VF_RUN/prefix-moment.json" \
  --tail-first "$VF_RUN/tail-first.json" --height "$VF_BACKGROUND_HEIGHT" \
  --positive-alpha "$VF_POSITIVE_ALPHA" --background-transfer "$VF_RUN/background-k.json" \
  --out "$VF_RUN/closed-budget.json"
"$VF_PY" "$VF_S/db6f-root-whole-metric-reach-v2.py" \
  --closed-budget "$VF_RUN/closed-budget.json" --tail-certificate "$VF_RUN/tail-full.json" \
  --tail-metric-certificate "$VF_RUN/tail-metric.json" --out "$VF_RUN/whole.json"
"$VF_PY" "$VF_S/db6f-audit-terminal-error-gate.py" \
  --whole "$VF_RUN/whole.json" --prefix-target "$VF_RUN/prefix-target.json" \
  --out "$VF_RUN/terminal-error.json"
```

若未使用独立 metric-only，省略 whole 的相应选项。若 bridge 正当引用另一份数值 manifest，终门须另给 `--bridge-tail-manifest` 并支付同一物理 cut/参数/六定义；当前从新真实 manifest 建桥的顺序无需这个例外。

正常终门是 `--whole`，**不是**已运行过的 `--check-m12-negative`。必须实际取得新图 $\mathcal E\le1/500000000$ 及严格实际改善结论。旧 M12 点 lower、旧 M8→M12 下降的已审证明可作为输入；不能仅比较两个上界。

此时仍须写统一 G5 账本：同 g 原 refinement 主线、各算子的含义、保留 M14 非单调历史、实际 M8→M12→最终图严格下降及到原容差的证据。单个 terminal PASS 不自动等于 G5。R17 相位共轭和固定旋转 g 使 metric 空间 supremum 对相位不变，全部 t 已解析支付，不新增“t 采样误差也必须下降”的门。每图已有 C²/真实曲率证书时，也不要求两图 C² 差必须到机器精度。

不无条件新增“最终 M15 必须 native steps32→64”这一任务。若现有固定 g 加密记录和最终原容差证据已足够，最终审计只核它们。若出现新的平台、最终误差未达门，或要独立宣称原 RK 截断误差已经收敛，则按冻结 G5 计划增加同 M/N/g 的原生径向真联解对照；固定 CP 后增密 exporter 不算该对照。若证明确实引用两张有限图的连续 C² 差，才用参数化 `db6f-prefix-tail-c2-stream-v2.py first second out --batch 128` 重跑该已明确范围的比较。

后到的只读 G5 说明 `tail-g5-final-m15-sufficiency.md`（SHA `f3b37b270e7f347952053279ceaea775e924191e45ed70eea99268eb0901b0fb`）§1/5/6 已与 README 对照：活动带上相位作用保持 g 正交标架与相对 tensor 范数，固定帽单独处理；该条件式数值完成解释没有取消其余六门。有限下降记录不是无限极限定理，最终须明确原 RK 独立误差和无限尾严格存在仍未由这些记录证明。README 最后还要求最低标准达成后继续推进更强目标并报告三个归一比值的最大已达水平；本协议不取消该后续研究要求。

当前 R25 球界脚本固定旧 R21 M12，不能移用其数值。最终若采用相同公式收紧新图 D，应另有已审、实际新图绑定的轻账本并重放；这不是基本 $D\le3.92$ 组合之外自动新增的门。

## 9. G7：重新生成同图三件网格并真正读回

`db6f-export-closed-mesh.py` 并未硬锁 M8：它按给定 geometry/whole/实际 manifest 选择已审 common-cut 实现，重新评价材料角、尾和帽。因此可以对最终已认证图使用其现有参数化入口：

```sh
"$VF_PY" "$VF_S/db6f-export-closed-mesh.py" plan \
  --geometry "$VF_RUN/closed-map.json" --whole-certificate "$VF_RUN/whole.json" \
  --out-prefix "$VF_RUN/mesh" --angular "$VF_MESH_ANGULAR" \
  --prefix-intervals "$VF_MESH_PREFIX" --tail-intervals "$VF_MESH_TAIL" \
  --collar-intervals "$VF_MESH_COLLAR" --cap-intervals "$VF_MESH_CAP"
"$VF_NODE" "$VF_S/db6f-tail-sample-background-height.mjs" \
  --manifest "$VF_RUN/tail-manifest.json" --calibrations "$VF_CALIBRATIONS" \
  --alpha "$VF_TIGHT_ALPHA" --radii "$VF_RUN/mesh-radii.json" \
  --source-root "$VF_SRC" --out "$VF_RUN/mesh-heights.json"
"$VF_PY" "$VF_S/db6f-export-closed-mesh.py" build \
  --plan "$VF_RUN/mesh-plan.json" --height-samples "$VF_RUN/mesh-heights.json" \
  --out-prefix "$VF_RUN/mesh"
```

从新 mesh manifest 读取实际三件文件名；不要猜扩展名或复制旧网格。对每件实际执行：

```sh
"$VF_PY" "$VF_S/db6f-audit-closed-mesh.py" \
  --mesh "$VF_ACTUAL_ONE_MESH_FILE" --out "$VF_NEW_ONE_MESH_AUDIT" --batch 2048
```

三个时刻为 $0,1/4,1/2$，角节点须是 12 的倍数。按实际输出核连通闭有向流形、边/顶点 link 和径向 PL 嵌入证明；仅 exporter 打印 `mesh_generated` 不够。还要读回三件文件，比较共同面表、固定 mask 和固定顶点位模式，验证材料相位、上下完整 Z 镜像和帽公式。

现有参数化 `db6f-tail-review-closed-mesh.py --manifest ... --replay-manifest ... --out ...` 可用于同一 plan 的独立 build 对照：它核真实三件字节、材料角反解、相位、固定帽及镜像；固定的只是已审 exporter SHA 和原帽定义，不是 M8 的顶点数。它要求两份 manifest 的 plan 哈希相同，不能把路径不同的新 plan 偷称为相同。

最小无改码用法是：独立重新产生 plan/高度，先逐项确认连续图的数学数据、采样点与高度数值同作者一致；若两者只有路径等来源元数据不同，保留这次生成证据，并明确以作者冻结的同一 plan/高度输入作一次独立 `build`，再调用上述 byte-replay checker。第二次 build 很小，且必须报告输入切换，不能用它代替前面的独立数值高度与图生成。如果独立生成的数学图或采样数据不同，该同 plan 字节对照不适用，不能切回作者输入来掩盖差异。如果改为一般化 plan 比较器，应另冻、另审；现在不预写适配器。固定顶点的严格位模式核对应使用 float64 的整数位视图；通用 helper 的浮点 `array_equal` 本身不区分正零与负零。

`db6f-root-review-visible-m8-replays.py` 硬编码旧文件名、67250 顶点和4610固定点，不能直接用于 M15。每件文件必须小于5MB，超过1MB压缩；保留原点/模型单位和数值采样标签。现有 height helper 不是严格顶点误差证，PL 证书也不证明其与连续图的距离；连续图的 C²/metric/reach 来自前面的独立连续认证，数值网格与严格无限存在的差距照实说明。

## 10. 必须独立交付的产物清单

1. **运行来源包**：作者冻结包身份、独立 replay binding、仅 I/O 差分、完整源/输入 SHA、真实运行环境/命令/退出记录。
2. **新真实联解**：自己的 prefix CP/全部 PP 数据、summary/outer checks、最后真实 audited tail、trace；所有有限性和闭合门核查。
3. **新明确有限表示**：自己的 prefix 数据、tail 全部分片/manifest/collar、精确径向不变量及镜像入口记录。
4. **新的共同闭图**：target、基础 metric、bridge、common-cut metadata 和完整两 jet/gauge 身份。
5. **完整连续证书**：该图自身 prefix geometry/metric/moment、尾 first/full/必要 metric-only、所有叶/row shards、精确覆盖与源绑定。
6. **精确完整组合**：closed budget、whole、正常 terminal 及全部同图标量，不仅是重抄原账本。
7. **统一 G5 核对**：同物理问题/时间范围的 refinement 记录、真实下降、原容差及剩余误差类别；实际补算的分支若有，单独绑定。
8. **同图网格交付**：新 plan/radii/heights、三件PLY或gzip、固定 mask、三个完整PL报告及跨时刻独立复核。
9. **最后独立报告**：每个阶段是否真正新执行、哪些已审前提复用、原/复跑数据与数值结论如何比较、哪些条件仍未知。只在上述真实完成后声明最终独立流程完成。

每个后端必须留自己的真实全域输出，不以作者 report 作为完成缓存。数组/GZIP 的字节可以直接比；含路径/时间的元数据应按明确白名单比较，不能要求换目录后整个 JSON 必然同 hash，也不能用“忽略元数据”掩盖参数或数学数据变化。

若重新求解/导出的数值 payload 不同，即使只差若干 ulp，也不能继续声称它与作者是同一精确有限图或套用作者证书。保留差异和真实来源；要么在冻结环境下恢复完全相同的数学 payload，要么将独立产物明确作为另一张同 g 图并对其全部重新认证、由最终交接选择实际交付对象。不得截断、复制或修写系数来凑 hash，不得在独立验收中调参优化。

## 11. 已明确的接口边界与尚待的最终输入

- 旧 `tail-final-m15-minimal-pipeline.md` 中“endpoint exporter 尚未实现”“transfer 适配拟实现”属于当时状态。当前应分别使用已审 `993dc6…` 入口及 v3 producer/consumer；它们对最终图的实际正向运行仍待发生。
- `prefix-prepare-final-m15-coupling-v2` 是 continuation/N256 的特定准备门，不能直接泛化为最终 N512 close checker。其严格数值 jets 谓词可作参考，最终 schema 和来源必须来自真实最终记录。
- `prefix-source-availability.py` 期望 `dependencies.files` 是字典；`repro/source-snapshot-manifest.json` 的 files 是列表。不能给出错误的“直接喂快照索引”的复跑命令。最终 bound_files 应显式包含快照逐文件 SHA 和本地实际依赖；若写新 preflight 只做这项 schema 对接，须留真实新实现身份。
- 当前 final whole/terminal 明确不自动宣告 G5 或独立全流程。最终完成报告是额外的已观察结果，不改旧 report 的 scope flag 来制造完成记录。
- 未知项仍是：最终真正成功 CP/配对末尾、原成功 argv 与 seed、最终采用的表示和验证选项、是否有新 supplier/表示适配、是否需额外 refinement 分支。本文不为这些项填造未来路径、参数或成功状态。

以上是静态可执行接口核查，不是任何最终命令已经成功的报告。当前 README/G5 与最终独立运行均保持未完成。
