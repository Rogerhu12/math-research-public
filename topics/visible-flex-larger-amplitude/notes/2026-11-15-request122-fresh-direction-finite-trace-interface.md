# Request122：同一次 fresh 原模型与 R273 方向上的两份有限 root 轨迹方向导数

- 类型：公开 Actions 实验接口与源码接线；尚无本请求数值结果。
- 作者：ChatGPT（exact_refinement）；日期：2026-11-15。
- 本课题根规则：科学仅公开 Actions；本地只源码、字节与语法。可重算数值原件仅留 runner 临时目录，不上传 artifact、Release 或 Git。
- 依据：[R283 有限 root 轨迹微分](../results/R283-finite-root-trace-differentiation-with-literal-tables.md)；[冻结方向导数实现](2026-11-15-native-finite-root-trace-direction-implementation-interface.md)。

## 1. 本请求实际做什么

从 actual91 保存的 actual73 失败 **BASE** 恢复完整 577×224 初猜。使用当时的真实 H、target、sigma、far、原 configuration/source/cells/graphs/gains，并通过原构造器重建一个新 worker。在该 worker 的第一次原 `evaluate(...,true)` 返回后，保存本次完整 576 段 J/r 与全部边界、状态，使用原 R273 动态 QR 与 exact row kernel 求一次全 577 节点方向，eta 明确为 1。

随后只从这次实际调用生成一份新的完整 packet。冻结的有限轨迹 JVP 对同一 packet、同一 delta，在 alpha=0 上分别执行 `original` 和 `refined` 两个 root policy。两次都包含完整 226 维 RK 状态、576 段、全部 cut/stage/far 129248 原行以及原 sigma。它们各自选出并记录自己的真实 root 分支，不共享或伪造对方的分支。

两次尝试完成、返回 partial，或留下真实错误后，独立桥主动结束这个实验 worker。停止点在第一次 correction 内、原十档 nonlinear trial 之前。新流程不运行原 32 轮到收敛，不声称完成 endpoint J、fresh audit、native 或 fullDN。原未改的 solve/evaluate/trial 源文仍被核对并保留，受控停止是新实验策略，而不是原方程或原线搜索失败。

113 源和已发布的三个 JVP 实现文件一字不改；113 在自己的 Actions 运行，不被122取消或设为前置。此次不加载已删除的113 packet/result/delta，也不以一个旧 SHA 假造恢复。

## 2. 唯一真实数值来源

### 2.1 actual91 完整输入包

| 项 | 固定值 |
|---|---|
| run | `43672150224` |
| source | `b78f0dd1471a118d2ed21467602509d188c2ab67` |
| artifact | `14145200674` |
| name | `visible-mainline-modelresponse-43672150224-1` |
| ZIP bytes | `10267458` |
| ZIP SHA256 | `78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6` |
| actual91 result SHA256 | `0b7200064336361ecb36b0627495fca298b7af758ed37d34d6ae6b1a1898db04` |
| binding SHA256 | `0119e12bfc7f98732189b76b3fdfa23ae05229937a8ea998c9aa38890ff11d0a` |
| selected BASE raw SHA256 | `f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6` |

该 state 来自 actual73 的 call1/iteration2/sequence2：run `43657001633`，source `9515d5aaf7c68f8efd366438d6bd81ce73c3486f`，`native_accepted=false`。它不是 actual83 的 trial state，也不是可复用成功 cache。原 `root_20261115_fetch_native_word_parent91.py` 和512247运输内核验证整个已有包；原 parent binder验证实际原字段和 raw words。

### 2.2 原构造器的两个 historical ready

仅恢复 immutable commit `8bd267107cc8710d371f3b62c02986655ac965b0` 中两份原件至 runner，并设置原有 env slot：

| env | 原 notes 文件 | bytes | SHA256 |
|---|---|---:|---|
| `VISIBLE_FLEX_FROZEN_LEDGER_READY` | `2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json` | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| `VISIBLE_FLEX_FROZEN_STORED_READY` | `2026-11-13-strong-m28-recovered-full-audit-r1-ready.json` | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |

两个 Git blob分别为 `4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3`、`b6c44fe237750f13c8b10366f15525b481a74e09`。恢复时同时核 commit/path/blob/size/SHA。它们只付构造器的冻结几何输入，不是新的成功 native 锚。

原 `exact_20261114_public_resume.py` 恢复已声明78个公开源。此次没有使用 small-core 的四数学输入，因此不恢复它们，不把它们列作新实验前置。原91配置由原 binder提供，不读取已经移除的 HEAD 默认 ready JSON。

## 3. 新旧源码边界

新文件仅两个：

- `geometry_20261115_native_trace122_probe.py`：来源、运行时三小源生成、观察日志、受控结束、策略 wall guard、紧凑 report。
- `geometry_20261115_native_trace122_experiment.mjs`：同一实际 packet 的两 policy调度，使用已冻结 packet writer和 Python launcher。

新 probe按完整 SHA读取冻结113 source factory；仅改变新 producer/schema/名称和实验执行控制，在全 fresh R273 方向验证后插入两次调用并受控结束。生成的 adapter、QR、hook实际完整 SHA及 driver实际 SHA都在日志。旧 adapter/QR 数学沿原冻结 source；原 factor engine为 `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33`，exact kernel为 `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f`。

冻结实际 JVP依赖：

| 源 | SHA256 |
|---|---|
| `geometry_20261115_native_trace_variation128.cpp` | `8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d` |
| `geometry_20261115_native_trace_variation128.py` | `8229212bb6804db7eee99ea661a490d3cced756e8a98471c09e22ad74cdb8b76` |
| `geometry_20261115_native_trace_variation128_bridge.mjs` | `61e21ded03f1569c7d05742d3059553d1f3830c52a62643fd64883bc821c83a7` |
| 被 include 的原113 CPP | `1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d` |
| 原113 packet writer baseline | `3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8` |
| 原113 source factory | `ba3564ca6ef5329326861a66a948292280e2ab9e311eb8912c11d4e24d7d8409` |

request列33个完整 source SHA，含原113的28个身份闭包与5个新/已冻 trace文件。78个 restored source继续由原 public resume实际恢复核验；不能把33误称含全部78内容的数组清单。

## 4. 实际 trace 数学范围

JVP计算的是选定成功有限 root轨迹的理想实表达链式导数在 binary128 中的数值执行。原 literal64 的 w、w2、E、gram、三角表等逐 word提升，不能把独立保存的 C当成 F关于 e的真 Jacobian，也不能把新结果称 IEEE roundmap 的导数。

每个成功更新保真实 F、真实 C及接受 alpha；对实际 Cholesky步骤和两次实际三角回代逐步微分，再更新方向。第一次就返回的 n=0分支、fallback、30次outer/20档root trial以及最大29次成功更新范围均沿冻结实现。完整 RHS/RK保226行；shape224反馈，均值行完整保留；出口仅原Pi除port。第 n段取 node n+1入、node n出，cut/stage/far原序和原sigma不改。

两个政策分别为：

- `original`：原 binary64 `8e-14`、`5e-12` literal精确提升后的 stop/fallback。
- `refined`：原113明确采用的 binary128 decimal `1e-28`、`5e-27`。

它们可能产生不同有限轨迹，也可能一个完整、另一个partial。一次方向不是完整224输入列的J，不付连续导数、分支稳定区间、导数误差界、fullDN端点灵敏度或全native收敛。原64 J只是本次实际 delta的生产者，新trace action不被冒称与原64 J逐字相同。原 exact saved-row读回也不被冒称新128模型的精确证明。

## 5. 时间与进程

packet及binding成功写成后开始7200s JVP阶段时钟。fresh原64 model、完整R273和packet/profile/cusp导出在这个时钟之前。第一policy科学预算为 `min(3600, remaining−300)`，第二policy用 `remaining−300`；300秒为冻结launcher的180秒编译与120秒child收尾 allowance。少于60秒科学额度时该slot明确 `attempted=false`，不伪造结果。

第二policy不检查第一policy的 residual、是否complete或是否成功才启动；仅使用真实剩余 wall time以及同一输入身份。第一policy的编译、root failure或partial都保实际状态。每次调用的 Python guard、launcher、compiler、C++保在原规则runner同一进程组内，没有 detached science子树。

guard在分配的剩余wall内等待；预留最后5秒，对它实际创建的 launcher descendants记录 `/proc` PID/start-time，先TERM再KILL相同start-time进程，避免误杀复用PID。规则变更时原runner的组信号可同时停止所有这些进程。实际已返回summary/receipt才会被声称存在，超时未形成的报告明确missing。

最后原response读回、hash/元数据打印和清理是科学子进程结束后的文件工作。它不增加RHS/JVP。总job350min、scientific step320min沿113资源包络；这不保证数值一定完成。资源耗尽、规则变更、编译错误与原root/科学失败各保真实字段，不当成原nonlinear gate拒绝。

## 6. 受控停止和三种状态分开

新hook发出 `native122_controlled_worker_stop`，然后抛出精确标记：

```text
REQUEST122_CONTROLLED_STOP_AFTER_FIRST_FRESH_DIRECTION_AND_TRACE_POLICIES
```

原worker用原协议返回该失败文本，原client关闭。新entry逐字读回这个响应，并单独报告：

1. `procedure_complete`：一次fresh snapshot、一次R273、两slot、受控marker及原协议marker已实际闭合；没有把任何 residual阈值当新gate。
2. `science_directions_complete`：两个冻结消费者各自实际 `complete=true`。即使协议收尾失败，也保这两个科学对象自己的原complete状态。
3. `native_accepted=false`、`fullDN_completed=false`、`complete224_trace_J_computed=false`、`original_ten_trials_or_final_J_audit_executed=false`：这是有意停止路径的执行范围；若未观察到协议停止、而返回意外原native响应，执行状态保留为unknown并保存实际response字段，不能以意图冒实际。

entry exit0只表示实验工程闭合且两方向完整；exit3表示工程闭合但至少一个方向不完整；exit2表示实际工程/来源/协议未闭合。它们都不是原native接受。原driver的exit2与sentinel失败响应照原值保存，不隐藏或改成原native成功。

## 7. CLI、工作流和输出

独立trigger：`computations/public-native-trace-direction-request.json`。独立workflow：`.github/workflows/visible-larger-public-native-trace-direction.yml`。concurrency `visible-larger-public-native-trace-direction`，不取消113。

```bash
python -u geometry_20261115_native_trace122_probe.py \
  --trace-budget-seconds 7200 --trace-threads 2 \
  --original91-directory "$VISIBLE_PARENT91" \
  --source-topic "$VISIBLE_SOURCE_TOPIC" \
  --eta 1 --node-heap 6144 --exact-workers 2 \
  --max-factor-bytes 2147483648 \
  --out "$VISIBLE_OUT/native-work"
```

该入口放在原3b8规则runner下，使用本请求明确已读的74c08/bff8双README实际字节覆盖旧嵌入baseline。原2700秒真pull/rebase/规则差异停止逻辑不改，H必须有唯一规则行。原sciencecheckout保持触发SHA；`merge.stat=false`避免删除旧raw的无关diffstat。token仅原取件step与规则同步step环境，科学代码不读取或落文件token。

源码/预算元数据与完整compact policy实际标量进入compute日志。主要事件：

- `native122_fresh_direction_for_trace`：fresh原norm、state/十阵SHA、当前snapshot、delta SHA、完整QR实际factor_summary和129248原行exact scalar。
- `native122_actual_packet`：新packet/binding SHA、实际调用来源、policy/预算；不存在旧113packet身份声称。
- `native122_policy_started`、`native122_policy_returned`或`native122_policy_not_started`：每slot真实预算、child/guard状态、实际summary/report/manifest/array receipts和完整compact标量。
- `native122_finite_trace_policies_complete`、`native122_controlled_worker_stop`及 `native122_final`：工程与科学状态分开。

最终summary schema为 `request122-fresh-native-direction-finite-trace-experiment-summary-v1`。新policy组合schema为 `request122-fresh-actual-direction-two-base-traces-v1`。冻结launcher/reportschema不改。

final summary通过GITHUB_OUTPUT传独立report job，最多90000字节，明确SHA/bytes且不含显示分隔LF。report只打印 `BEGIN_VISIBLE122_SCALAR_SUMMARY` / `END_VISIBLE122_SCALAR_SUMMARY` 中间原JSON和identity。若超限，fallback保原summary SHA、真实状态和已在compute日志输出的完整compact政策事实，不填假0或假成功；若早期失败没有summary，report明确missing。report job为 `if: always()`，不以compute绿灯隐去partial。

临时完整snapshot十阵、所有R273因子/常数、delta及整数ledger按原算法生成；两policy消费结束后才删除本次iteration。临时packet只生成一次并在两consumer后删除。冻结launcher先hash所有已返文件再清自己的raw/executable；coordinator读summary后清该policy目录。最后原client关闭/完整response读取后清本次owned输出，readonly actual91目录仅改当前uid目录mode后清除。不上传任何可重算raw，也不把它们换名为小文本保留。

## 8. 已完成静态范围与仍待真实Actions

本地只执行源码字符串生成、Python AST/compile、Node语法、workflow shell语法、inline Python AST与实际source SHA检查。生成的三runtime源与driver均保真实完整identity；没有导入科学模块、创建native构造器、运行任一packet/root/RHS/QR/JVP、构造数值fixture或执行新范数。

真实风险仍包括完整root方向在预算内是否完成、微分分支中实际数值非有限、binary128 scalar读回动态范围、policy分支差异及GNU运行时/进程收尾。它们由真正Actions原记录回答，不额外设数值调度门；没有未来run、JVP值、成功native或接受结果被预写。本次不修改R283结论边界，不代替后续完整224列、当前native高精度状态持有者或全DN导数实现。

完整diff、语法回执与生成的runtime源码仅是可重得的临时静态工作件；公开保存本请求脚本/参数/接口及未来run与SHA和紧凑真实结论即可。
