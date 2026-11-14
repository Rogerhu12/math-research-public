# restart8000 真成功后的完整生产链与纯计划器

2026-11-10，Astra-visible-flex-78718bd0 / numerical_recovery。
**状态：冻结供全文复核的来源/命令计划；尚无正向成功计划，尚未执行任何本轮新图后端。**
restart8000-01 的 root 工具 session 2770 后来不可访问，且无 CP/summary/guard-completion，
其自然出口未知。另名 restart8000-02 已由 root 以 ef2882/session72917 实际启动，
由 root 独占持续监控。本文不消费该 session，不据遗留 mtime、日志或 guard 自报推断出口。

本文件替代旧 `numerical-post-csc-chain.md` 作为**新的条件入口说明**；旧文的 run02
后来已真实失败，其历史文件和结论不改写。本轮后端只能消费实际通过完整新 final 的
restart8000 CP 及它自己最后的真实 audited tail，不消费 run02 失败 CP 或首包作成品。

## 1. 已冻结的新纯计划器，仍待独立全文审查

`scripts/78718-plan-post-restart8000-v1.py`，32,491 B，SHA256
`c6ef233eb40517bf1986b3ea25d0bb31d102d4b219727c6d69a97b38ee1e0456`。

其唯一功能是：

1. 要求显式传入新 launch、root 实际成功出口、已保存的完整新 final 报告。
2. 逐字钉住 `78718-prefix-audit-restart8000-v1.py`，重新运行其原完整
   `validate_inputs` 和 `final_audit`；新鲜结果必须与传入 final 报告逐字段相等。
3. 从通过审计的实际 CP 的 `tail_seam.tail_record` 解析自有末包，核其属于
   实际 `tail_calls` 且在完整 final 的已闭文件中。未知未来 CP/尾不预填 SHA。
4. 复核原生产来源、43份 source-root 副本、原 M8 背景和六定义、证明头部与旧 M12 参照。
5. 只写未来步骤的结构化 argv、真实预存文件 SHA、依赖和互斥分支；不执行任何 argv，
   不调用 producer、solver、候选初始化或物理 callback，不创建未来生产目录。

当前 `v1` 的可执行族仅为原单容器 prefix。另名无损存储族仍在单独完整审查，
不得把同名步骤悄悄替换为它。真正单容器超限后，才按第9节的明确新身份接续。
计划器并不是新数学验收门；它把已有完整 final 和既有来源约束接到未来命令。

### 已实际执行的小检查

| 实际工具回执 | 真实退出 | 范围和结果 |
|---|---:|---|
| `a0190a` | 0 | 源码 compile + `verify_fixed_inputs()`；127个文件绑定，原来源和背景齐；0 solver/producer，未调用 command plan。 |
| `767cf2` | 2 | 用真实 restart8000-02 launch，但未来 root exit 文件不存在；拒绝、0生产 argv。 |
| `c67b35` | 2 | 尝试给同一新 launch 借用 run02 实际失败观察；拒绝 `Wrong actual root observation identity`，0生产 argv。 |

完整静态输入报告 `numerical-post-restart8000-static-inputs-01.json` 为65,775 B，
SHA `34981c529934ebccf9a85ae8dd5b41b8359930d828e7faae7d6117b4d52aff4b`。
两份负门报告分别为266 B/SHA `542903ae4255fad4a58f569ada19c3aad299cc750a2a702084a079825fd805c0`
和269 B/SHA `d33813790de79a23589262f44db58aedebdd383b155b5b7f881374f5e668c393`。
不存在成功 CP 时没有制造正例或成功计划。原终门仍缺26件 M12 对象及由待取 packet
头部决定的一份 data 后代；报告明确把预期 SHA 与实际已观察 SHA 分开。

## 2. 唯一允许开始生产的真实入口

先由 root 取得自己的真实自然 exit0，并写出绑定完整闭文件的观察。
只有以下新完整 final 正常通过，才可用第二条纯计划命令。
下列 `root-observed-exit`、`final-audit`、`production-plan` 均是**约定的新输出路径**；
本文不声称它们已经存在。若 root 实际观察文件另名，必须传真实文件路径。

```sh
VF_REPO=/workspace/scratch/78718bd0c4a9/math-research
VF_T="$VF_REPO/topics/visible-flexible-closed-surface"
VF_S="$VF_T/scripts"
VF_N="$VF_T/notes"
VF_PY=/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python
VF_NODE=/opt/codex/runtimes/codex-primary-runtime/dependencies/node/bin/node
VF_SRC="$VF_T/repro/source-root"
VF_OLD=/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface
VF_STEM=2026-11-10-78718-numerical-m14-restart8000-02
VF_LAUNCH="$VF_N/$VF_STEM-launch.json"
VF_OBS="$VF_N/$VF_STEM-root-observed-exit.json"
VF_FINAL="$VF_N/$VF_STEM-final-audit-01.json"
VF_PLAN="$VF_N/$VF_STEM-production-plan-01.json"
VF_RUN="$VF_N/2026-11-10-78718-numerical-closed-restart8000-02-original"
cd "$VF_REPO"

"$VF_PY" "$VF_S/78718-prefix-audit-restart8000-v1.py" \
  --launch "$VF_LAUNCH" --mode final --observed-execution "$VF_OBS" --out "$VF_FINAL"
"$VF_PY" "$VF_S/78718-plan-post-restart8000-v1.py" \
  --launch "$VF_LAUNCH" --observed-execution "$VF_OBS" --final-audit "$VF_FINAL" \
  --run-directory "$VF_RUN" --out "$VF_PLAN"
```

必须得到 `PASS_ROOT_OBSERVED_RESTART8000_M14_W14_FINITE_COUPLED_CLOSE`。
只读首包不能替代：01 的首包审计 `9ab005` exit0、02 的 `e52903` exit0，
均仅 `PASS_FIRST_ACTUAL_M14_DN_ONLY`，残差 `6.168952323652266e-10`、616项 Jacobian。
它们没有证明任何新的 inner BVP、outer、末审或整图完成。

`VF_PCP`、`VF_TCP` 必须分别取**成功计划**的
`own_successful_checkpoint.path`、`own_final_audited_tail.path`；不得猜尾调用编号。
成功计划保存这两个实际身份，并重新绑定 reproduction、root observation、全部实际 PP。
`VF_RUN` 必须尚不存在，之后才按计划创建。每个后端真实执行时保留 argv/cwd/environment、
自然出口、输入与来源 SHA、全部输出 SHA/尺寸和完成字段；任何局部记录不冒充完成。

## 3. 固定前提、最小表示和原命令来源

| 角色 | 本题 notes 下已核文件 |
|---|---|
| `VF_OLD_TAIL` | `2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json`，连同8个原 raw gzip |
| `VF_BG_K` | `2026-11-09-db6f-audit-tail-tight-final-packet.json`及其原 NPZ |
| `VF_BG_E` | `2026-11-09-db6f-audit-tail-lowmetric-final-packet.json`及其原 NPZ |
| `VF_BG_H` | `2026-11-09-db6f-tail-background-height-rigorous.json` |
| `VF_BG_A` | `2026-11-09-db6f-audit-positive-radial-alpha.json` |
| `VF_CAL` | `2026-11-09-db6f-tail-finite-source-calibrations.json` |
| `VF_ALPHA` | `2026-11-09-db6f-tail-tight-alpha.json` |
| `VF_PORT` | 重建旧 topic 的 `notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json` |

上述变量的完整路径由成功计划 `fixed_input_roles` 给出。五份固定小索引硬钉原 SHA，
来源闭包包括 original literal source 62件、source-root 43件及原径向锚检查/点界依赖。
这只是预存背景与代码完整；没有把旧 M8/M12 的图证书转赠本次未知新图。

同 g 物理量及 source M14/N512、native depth12/parts8/steps32 均沿用新完整 final。
当前后端初档保持：tail export depth8/degree192、angular512、flow32；
prefix Cartesian M24/angular768/mean quadrature8/subdivide1；common-cut width.15。
M24 是有限 Cartesian 表示，并不是 source 的24个未知模；common-cut 会从实际尾的
全部 signed modes 扩列，不能省略 degree192 要求的列。原2e−9不放宽，不附加 S64/C³ 门。

## 4. 自有尾、径向精确锚、collar 和一阶界

```sh
"$VF_NODE" --max-old-space-size=1536 "$VF_S/db6f-prefix-endpoint-critical-increment-export.mjs" \
  "$VF_TCP" "$VF_RUN/tail" --source-root "$VF_SRC" \
  --depth 8 --steps 32 --flow-steps 32 --angular-nodes 512 --degree 192 \
  --grid critical --critical-cells 0 --critical-base-steps 64 \
  --critical-ratio .05 --endpoint-ratio .025 --difference-step .00005 \
  --audit-angular-nodes 128 --audit-fractions .25,.5,.75
"$VF_PY" "$VF_S/db6f-tail-radial-invariant.py" \
  "$VF_RUN/tail-manifest.json" "$VF_RUN/tail-radial.json"
"$VF_PY" "$VF_S/db6f-tail-collar-exact-check.py" \
  "$VF_RUN/tail-collar.json" "$VF_RUN/tail-collar-check.json"
"$VF_PY" "$VF_S/db6f-tail-first-bounds-stream.py" \
  "$VF_RUN/tail-manifest.json" "$VF_RUN/tail-first.json" --batch 128
```

exporter 写 manifest 后还须写自己的 collar，所以必须等自然退出与全部输出关闭。
原 IntegratedTail/radial 检查读取所有真实分片，验证 SHA、共享行、有限数、正增量和
精确锚恒等式；不是只看一个 finished 标志。当前尾格式本来已分片，无须另做存储转换。

## 5. 基础 prefix、目标、桥和共同 cut

```sh
"$VF_PY" "$VF_S/78718-run-file-cap.py" -- \
  "$VF_PY" "$VF_S/db6f-root-mirror-hermite.py" \
  --source-root "$VF_SRC" --checkpoint "$VF_PCP" --linear-port "$VF_PORT" \
  --out-prefix "$VF_RUN/prefix-base" --modes 24 --angular 768 \
  --quadrature 8 --subdivide 1 --ell 0
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
  --bridge "$VF_RUN/bridge.json" --width .15 --out "$VF_RUN/closed-map.json"
"$VF_PY" "$VF_S/db6f-root-common-cut-v2.py" geometry \
  --geometry "$VF_RUN/closed-map.json" --angular 256 --radial 1 \
  --out "$VF_RUN/prefix-geometry.json"
"$VF_PY" "$VF_S/db6f-root-common-cut-v2.py" metric \
  --geometry "$VF_RUN/closed-map.json" --target "$VF_RUN/prefix-target.json" \
  --out "$VF_RUN/prefix-baseline-metric.json"
"$VF_PY" "$VF_S/db6f-root-common-cut-v2.py" moment \
  --geometry "$VF_RUN/closed-map.json" --angular 512 --radial 1 \
  --out "$VF_RUN/prefix-moment.json"
```

文件 cap 仅为存储控制：RLIMIT_FSIZE=4,999,999。若实际超限失败，保留真实失败记录，
不把半个容器当成图，不删改旧绑定，也不降低数学分辨率。
基础图 metric 是 exact bridge 的真实输入，不能用共同图报告替代。

用精确 Fraction 比较本次 baseline 的 `epsilon*(1+eta)+eta` 与 `1/500000000`。
足够就选完整 baseline；不足则按它自己的 worst interval 作原局部角诊断，确认是可收紧
过估计后才运行下面的**完整**角分支。不得把带 `--intervals` 的局部报告送入终门。

```sh
"$VF_PY" "$VF_S/db6f-audit-prefix-angular-metric.py" \
  --geometry "$VF_RUN/closed-map.json" --target "$VF_RUN/prefix-target.json" \
  --baseline "$VF_RUN/prefix-baseline-metric.json" --bridge "$VF_RUN/bridge.json" \
  --budget 2e-9 --initial-arcs 128 --max-depth 4 \
  --out "$VF_RUN/prefix-angular-metric.json"
```

`VF_P=baseline` 对应 `VF_PREFIX_METRIC=.../prefix-baseline-metric.json`；
`VF_P=angular` 对应本次完整 `prefix-angular-metric.json`。
只按实际闭证书选择。common-cut 的 metric 分支不读 angular/radial，
改这两个参数不能收紧该 metric；target 转移只作一次。

## 6. 同一固定背景转到新尾，完整新尾证书

```sh
"$VF_PY" "$VF_S/db6f-tail-transfer-background-v3.py" \
  --old-manifest "$VF_OLD_TAIL" --packet "$VF_BG_K" \
  --new-manifest "$VF_RUN/tail-manifest.json" --out-prefix "$VF_RUN/background-k"
"$VF_PY" "$VF_S/db6f-audit-tail-stream.py" \
  --manifest "$VF_RUN/tail-manifest.json" --packet "$VF_RUN/background-k.json" \
  --angular 128 --radial 1 --background-curvature 6 --direct-threshold 8.5 \
  --block-size 128 --out "$VF_RUN/tail-full.json"
```

没有 limit 或局部 span，须包含 collar(-1)和全部有限跨。8.5仅为算法切换阈值。
如果 full 本身已经足够，令 `VF_TMODE=full`，不要重复 metric-only。
只有真实需要时才使用以下同 manifest 完整分支，并令 `VF_TMODE=metric-only`：

```sh
"$VF_PY" "$VF_S/db6f-tail-transfer-background-v3.py" \
  --old-manifest "$VF_OLD_TAIL" --packet "$VF_BG_E" \
  --new-manifest "$VF_RUN/tail-manifest.json" --out-prefix "$VF_RUN/background-e"
"$VF_PY" "$VF_S/db6f-audit-tail-metric-only.py" \
  --manifest "$VF_RUN/tail-manifest.json" --packet "$VF_RUN/background-e.json" \
  --radial 1 --block-size 128 --out "$VF_RUN/tail-metric.json"
"$VF_PY" "$VF_S/db6f-audit-complete-metric-report.py" \
  --report "$VF_RUN/tail-metric.json" --curvature-report "$VF_RUN/tail-full.json" \
  --out "$VF_RUN/tail-completeness.json"
```

可复用的是同一 w/w_r 的原已审值包，曲率/新扰动/全时支撑等必须由新实际图重算。
首 DN 的参数预检不代替这里真实 `--new-manifest` 的转移和完整后端。

## 7. 新闭预算、普通 whole、原2e−9正常终门

以下 `VF_P`、`VF_TMODE` 仅从本次已实际完整的分支选择；计划器提供四条互斥 route 的
完整字面 argv，并为每条最终输出另名，自己不选择或执行。

```sh
VF_ROUTE="$VF_P-$VF_TMODE"
"$VF_PY" "$VF_S/db6f-audit-closed-budget-transfer-v3.py" \
  --geometry "$VF_RUN/closed-map.json" --geometry-certificate "$VF_RUN/prefix-geometry.json" \
  --metric-certificate "$VF_PREFIX_METRIC" --moment-certificate "$VF_RUN/prefix-moment.json" \
  --tail-first "$VF_RUN/tail-first.json" --height "$VF_BG_H" --positive-alpha "$VF_BG_A" \
  --background-transfer "$VF_RUN/background-k.json" --out "$VF_RUN/closed-budget-$VF_P.json"
```

完整 full 已足够时，whole 的命令**没有**可选 metric-only 参数：

```sh
"$VF_PY" "$VF_S/db6f-root-whole-metric-reach-v2.py" \
  --closed-budget "$VF_RUN/closed-budget-$VF_P.json" \
  --tail-certificate "$VF_RUN/tail-full.json" --out "$VF_RUN/whole-$VF_ROUTE.json"
```

只有实际选用完整 metric-only 时，使用另一个互斥 argv：

```sh
"$VF_PY" "$VF_S/db6f-root-whole-metric-reach-v2.py" \
  --closed-budget "$VF_RUN/closed-budget-$VF_P.json" --tail-certificate "$VF_RUN/tail-full.json" \
  --tail-metric-certificate "$VF_RUN/tail-metric.json" --out "$VF_RUN/whole-$VF_ROUTE.json"
```

两条都不能用不存在的报告占位。真正最后采用原正常候选入口：

```sh
"$VF_PY" "$VF_S/db6f-audit-terminal-error-gate.py" \
  --whole "$VF_RUN/whole-$VF_ROUTE.json" --prefix-target "$VF_RUN/prefix-target.json" \
  --out "$VF_RUN/terminal-$VF_ROUTE.json"
```

普通 whole 的1e−6不等于终门通过；终门固定精确 `1/500000000`。
它还读取原 M12 真点下界和相应真实文件，不能改写该参照或改用负例模式宣称成功。
当前26件缺项在静态输入报告的 `terminal_reference_objects` 中，逐件带原预期 SHA；
24个 M12 raw 合80,730,280 B，另有原尾 CP 和点 packet 头。点 packet 的数据文件名及
SHA 必须在真实取回头后派生，当前明确未知。到新图有希望进入终门时由 root 终端精确取回；
无需为 background transfer 预先读取这些大 M12 数据，也不能称最终门完全不需要它们。

## 8. 同图网格、逐帧读回和最终独立运行

```sh
"$VF_PY" "$VF_S/db6f-export-closed-mesh.py" plan \
  --geometry "$VF_RUN/closed-map.json" --whole-certificate "$VF_RUN/whole-$VF_ROUTE.json" \
  --out-prefix "$VF_RUN/mesh-$VF_ROUTE" --angular 144 --prefix-intervals 128 \
  --tail-intervals 64 --collar-intervals 4 --cap-intervals 12
"$VF_NODE" --max-old-space-size=1536 "$VF_S/db6f-tail-sample-background-height.mjs" \
  --manifest "$VF_RUN/tail-manifest.json" --calibrations "$VF_CAL" --alpha "$VF_ALPHA" \
  --radii "$VF_RUN/mesh-$VF_ROUTE-radii.json" --source-root "$VF_SRC" \
  --out "$VF_RUN/mesh-$VF_ROUTE-heights.json"
"$VF_PY" "$VF_S/db6f-export-closed-mesh.py" build \
  --plan "$VF_RUN/mesh-$VF_ROUTE-plan.json" --height-samples "$VF_RUN/mesh-$VF_ROUTE-heights.json" \
  --out-prefix "$VF_RUN/mesh-$VF_ROUTE"
```

从此**实际关闭的** mesh manifest 的 `mesh_files` 依次取 exact time
`0`、`1/4`、`1/2`，核真实文件 SHA/尺寸，再为每件执行：

```sh
"$VF_PY" "$VF_S/db6f-audit-closed-mesh.py" \
  --mesh "$VF_ACTUAL_ONE_PLY" --out "$VF_ACTUAL_NEW_PL_REPORT" --batch 2048
```

扩展名由实际 raw 大小决定，不能预猜 `.ply` 或 `.ply.gz`。因此计划的这三步是带明确
manifest 字段选择器的 `argv_template`，尚未谎称已解析为字面 argv。
每件必须<5MB、>1MB压缩，核闭连通有向流形/PL嵌入及真实共同面表、固定mask和顶点位模式。
全时间 C²/等距/reach 来自原连续后端和相位作用，不能由三张网格推断；高度样本亦非严格顶点误差证。

独立者实际用同一 plan 构建后可调用原
`db6f-tail-review-closed-mesh.py --manifest ... --replay-manifest ... --out ...`；
计划只把其**尚不存在的真实独立 replay manifest**列为必须外部输入，不造文件或摘要。
同 plan byte review 是局部网格核查，不能替代 README 的原种子 solver→新有限图→全部后端→网格独跑。
原种子的精确路径、SHA和 cold8000/两段重放范围另见
`numerical-original-independent-seed-scope.md`；其真正公开祖先是旧 M14/N512，不是本轮失败 CP。

## 9. 原容器超限时的明确储存分支

`78718-prefix-byte-shards-v1.py` 等新族是新身份的无损存储，不是无法恢复的旧 A/B。
core 合成测试及 producer/reader 接线不等于最终 candidate 实际运行。
独审已指出 v1 两个局部来源账本的3条旧路径；root 正以另名 v2/v3 系列处理并复核，
本计划器不修改这些冻结源，也不提前消费尚未被完整审查的新 terminal。

只有真实原容器超限时，按已审完整族另出新计划和新命名空间，保持全部模式、节点、
float位值及逻辑 NPZ 字节，不降低分辨率。需要切换的真实 consumer 闭包见
`numerical-storage-production-routing.md`：fullxyz/mirror、continuous/polynomial/supplier、
common-cut/moment、angular与closed-budget、mesh/export/review和最后 prefix terminal。
原 whole-v2、exact-bridge、背景高度 sampler、PL checker和全部原 tail 后端仍可保留。
原 terminal 的单一物理 NPZ SHA语义必须由新存储 terminal 真正支付，不能只改 producer。

上述为条件执行接线，无本轮新连续证书或最终图。README的基本完成尚未达到，
达到后仍继续强振幅/商位移/reach目标，不作阶段性收尾。

## 来源

- `2026-11-09-db6f-root-final-m14-w14-entry-and-export.md`：原已审 M14 初档与2e−9。
- `2026-11-09-db6f-audit-final-independent-pipeline.md`：真实全链、径向锚及 mesh 接口。
- `2026-11-09-db6f-prefix-final-m15-metric-risk-order.md`：真实误差诊断和 CLI 边界。
- `2026-11-10-78718-audit-restart8000-entry.md`：完整新主源/输入/出口门独审。
- 原 source inventory、M8背景、fixed-proof/preflight 报告：本计划器逐项重核的固定来源。
- `2026-11-10-78718-numerical-storage-production-routing.md`：纯静态储存消费者闭包。
